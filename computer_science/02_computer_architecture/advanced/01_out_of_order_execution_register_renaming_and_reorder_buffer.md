# Out-of-order execution, register renaming và reorder buffer

Một CPU hiện đại không đơn giản lấy một instruction, chạy xong rồi mới lấy instruction tiếp theo. Nếu làm như vậy, pipeline thường xuyên bị bỏ trống vì instruction chờ cache, chờ phép nhân, chờ branch hoặc chờ kết quả trước đó. **Out-of-order execution (OoO / 비순차 실행)** giải quyết vấn đề bằng cách cho CPU thực thi instruction theo thứ tự tài nguyên và dependency cho phép, trong khi vẫn cố giữ kết quả quan sát bên ngoài giống như chương trình chạy đúng thứ tự kiến trúc.

## Instruction order có nhiều nghĩa khác nhau

Cần tách ba thứ: program order là thứ tự instruction trong machine code; execution order là thứ tự micro-operations thật sự đi qua execution units; retirement/commit order là thứ tự CPU làm kết quả trở thành architectural state chính thức.

CPU có thể execute instruction thứ 20 trước instruction thứ 15 nếu chúng độc lập, nhưng thường vẫn **retire in order**. Đây là cách giữ precise exception: nếu instruction 15 page fault, software phải thấy trạng thái như thể các instruction sau nó chưa commit.

## Data dependency mới là constraint thật

Ví dụ:

```text
1: r1 = load [A]
2: r2 = r1 + 1
3: r3 = r4 * r5
4: r6 = r3 + 2
```

Instruction 2 phải chờ 1 vì có **RAW dependency — Read After Write**. Nhưng 3 độc lập với 1 và có thể chạy trong lúc load `[A]` đang miss cache. Instruction 4 chỉ cần chờ 3.

OoO engine cố tìm những instruction sẵn sàng như vậy trong một **instruction window** rồi gửi chúng tới ALU, load/store unit, vector unit hoặc multiplier tương ứng.

## Vì sao register renaming cần thiết?

Không phải mọi dependency nhìn thấy trong source register đều là dependency dữ liệu thật.

```text
1: r1 = r2 + r3
2: r4 = r1 + 1
3: r1 = r5 + r6
```

Instruction 3 ghi lại `r1`, nhưng nó không phụ thuộc kết quả của instruction 1. Đây là **WAW — Write After Write** về tên register. Tương tự, **WAR — Write After Read** có thể xuất hiện khi instruction sau ghi một register mà instruction trước còn cần đọc.

CPU dùng **register renaming** để ánh xạ architectural registers như `r1`, `rax`, `x0` sang một tập physical registers lớn hơn.

Conceptually:

```text
architectural r1 version A -> physical P17
architectural r1 version B -> physical P42
```

Sau renaming, false dependency biến mất. Chỉ true dependency giữa producer và consumer còn lại.

## Rename table và physical register file

Rename stage giữ mapping từ architectural register tới physical register mới nhất. Khi một instruction tạo value mới, CPU cấp một physical register mới và cập nhật mapping cho instruction sau.

Physical register cũ không thể tái sử dụng ngay vì instruction đang chạy hoặc speculative state có thể vẫn tham chiếu nó. CPU cần cơ chế biết khi nào register cũ thực sự không còn cần, thường liên quan retirement/free list.

Điểm quan trọng là renaming không phải compiler variable rename. Nó xảy ra động, từng cycle, để khai thác parallelism chỉ có thể biết rõ khi runtime latency thực tế xuất hiện.

## Reservation stations / issue queue

Sau decode và rename, micro-operations thường đi vào queue nơi operand có thể chưa sẵn sàng. Entry ghi operation, physical source tags, destination và trạng thái readiness.

Khi producer hoàn thành, kết quả hoặc tag được broadcast/wakeup. Consumer đang chờ chuyển thành ready và scheduler có thể issue nó tới execution unit.

Đây là một **data-flow machine nhỏ** nằm bên trong CPU: operation chạy khi input ready, không nhất thiết khi nó đứng đầu program order.

## Reorder Buffer — cầu nối giữa execution và architectural state

**ROB (Reorder Buffer / 재정렬 버퍼)** theo dõi instruction theo program order sau khi chúng đã được đưa vào OoO engine. Instruction có thể complete out of order, nhưng ROB cho phép retire từ đầu hàng đợi theo thứ tự.

Một ROB entry thường cần đủ metadata để biết instruction đã complete chưa, exception có xảy ra không, branch có mispredict không, và state nào cần commit/release.

Mental model:

```text
fetch/decode
   ↓
rename
   ↓
issue window ──> execution units ──> complete out of order
   ↓                                  ↓
   └──────────── ROB in program order ─┘
                       ↓
                    retire
```

## Precise exception

Giả sử instruction 10 gây page fault nhưng 11–20 đã execute xong speculative. Nếu CPU đã làm tất cả side effects thành visible ngay, OS rất khó restart chính xác tại instruction 10.

Thay vào đó, CPU chỉ commit theo ROB order. Khi tới instruction lỗi, nó dừng retirement, loại bỏ speculative work phía sau và chuyển control sang exception handler. Architectural state lúc này tương ứng một prefix hợp lệ của program.

Đây là lý do OoO không có nghĩa “mọi thứ cập nhật state tùy ý”. Phần lớn complexity tồn tại để vừa reorder nội bộ vừa giữ abstraction sequential/precise đủ mạnh cho software.

## Load/store làm bài toán khó hơn

Register dependencies tương đối rõ sau rename, nhưng memory dependency phụ thuộc address runtime.

```text
store [p] = 10
load  [q]
```

Nếu chưa biết `p == q` hay không, CPU phải quyết định có cho load chạy sớm hay không. **Memory disambiguation** dự đoán/kiểm tra dependency giữa loads và stores. Nếu CPU cho load chạy sớm rồi sau đó phát hiện conflict, execution phải replay/rollback.

Store buffer cũng cho phép store được coi là complete trong pipeline trước khi data thực sự tới cache hierarchy, tạo thêm quan hệ với memory ordering.

## Window size là một giới hạn của ILP

CPU chỉ có thể tìm independent work trong số instruction đang ở flight. ROB, issue queue, load/store queue và physical register count giới hạn instruction window.

Window lớn hơn có thể che latency tốt hơn nhưng tăng area, power, wakeup/select complexity và wire delay. Đây là trade-off microarchitecture rất thực: performance không tăng miễn phí bằng cách “cho nhiều instruction hơn”.

## Khi workload không tận dụng OoO tốt

Pointer chasing như linked list traversal có chuỗi dependency dài:

```text
node = node.next
node = node.next
node = node.next
```

Address load tiếp theo chỉ biết sau khi load trước hoàn thành. CPU không dễ tìm parallel work dù có ROB lớn. Ngược lại, loop xử lý nhiều phần tử độc lập cho phép OoO và vectorization khai thác nhiều parallelism.

Vì vậy data structure/layout ảnh hưởng trực tiếp tới khả năng CPU che memory latency.

## Mental Model

> OoO CPU là một hệ thống data-flow speculative bên trong một vỏ architectural-order. **Renaming loại false dependencies; scheduler tìm ready work; ROB khôi phục thứ tự commit và precise state.**

## Common Misconceptions

**“Out-of-order nghĩa CPU thay đổi logic của chương trình.”** CPU chỉ reorder những operation có thể reorder theo dependency/speculation rules và phải khôi phục observable architectural semantics khi cần.

**“Register renaming là compiler optimization.”** Compiler có register allocation/renaming riêng; hardware renaming giải false dependencies động giữa architectural registers và physical registers.

**“Instruction complete là đã commit.”** Một instruction có thể hoàn thành execution nhưng vẫn speculative và chưa retire.

## Kết nối

Đọc cùng [Memory consistency và ordering](./00_memory_consistency_cache_coherence_and_ordering.md), sau đó chuyển sang [Branch prediction và speculation](./02_branch_prediction_speculation_and_pipeline_recovery.md). Ở tầng OS/runtime, precise exception và page fault nối trực tiếp với advanced Operating Systems.