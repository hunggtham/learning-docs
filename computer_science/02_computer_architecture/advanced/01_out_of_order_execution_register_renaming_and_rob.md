# Out-of-order execution, register renaming và reorder buffer

Một CPU hiện đại không đơn giản lấy một instruction, chạy xong rồi mới lấy instruction tiếp theo. Nếu instruction đang chờ cache, phép nhân hoặc branch result mà các instruction độc lập phía sau đã sẵn sàng, việc để pipeline đứng yên sẽ lãng phí execution units. **Thực thi ngoài thứ tự (out-of-order execution, OoO / 비순차 실행)** giải quyết vấn đề đó bằng cách cho CPU thực thi micro-operations theo dependency và resource readiness, trong khi vẫn giữ một invariant quan trọng: trạng thái kiến trúc mà software quan sát phải tương thích với contract của ISA.

Chương này cần được đọc như một bài toán giữ invariant dưới performance pressure: **execution được phép reorder để che latency; retirement, exception và rollback phải khôi phục một architectural history hợp lệ.**

## 1. Program order, execution order và retirement order là ba thứ khác nhau

Cần tách ba khái niệm:

```text
program order
= thứ tự instruction trong machine-code stream

execution order
= thứ tự µop thật sự sử dụng execution units

retirement/commit order
= thứ tự kết quả trở thành architectural state chính thức
```

CPU có thể execute instruction trẻ hơn trước instruction già hơn nếu dependency cho phép, nhưng thường retire theo program order. Invariant này giúp giữ **precise exception**: nếu instruction 15 page fault, OS phải thấy state như thể các instruction sau 15 chưa commit.

## 2. Instruction được biến thành micro-operation như thế nào?

ISA instruction là contract với software. Bên trong processor, một instruction có thể được decode thành một hoặc nhiều **micro-operation (µop)**. Front-end fetch/decode tạo stream; rename/scheduler/back-end quyết định µop nào có đủ operand và execution port phù hợp để chạy.

Mental model:

```text
fetch → decode → rename → dispatch
                         ↓
                issue / scheduling window
                    ↓       ↓       ↓
                   ALU     load    vector ...
                    \       |       /
                     complete
                        ↓
                       ROB
                        ↓
                     retire
```

Đây gần như một data-flow machine speculative nằm bên trong vỏ architectural-order.

## 3. True dependency mới là constraint dữ liệu thật

Ví dụ:

```text
1: r1 = load [A]
2: r2 = r1 + 1
3: r3 = r4 * r5
4: r6 = r3 + 2
```

Instruction 2 có **RAW dependency (Read After Write)** với 1 nên phải chờ. Instruction 3 độc lập với load ở 1 và có thể chạy trong lúc cache miss đang được xử lý. Instruction 4 chỉ cần chờ 3.

OoO engine tìm independent work trong một instruction window để overlap latency.

## 4. Vì sao register renaming tồn tại?

Architectural register names có thể tạo dependency giả.

```text
1: r1 = r2 + r3
2: r4 = r1 + 1
3: r1 = r5 + r6
```

Instruction 3 ghi lại tên `r1`, nhưng không phụ thuộc value của instruction 1. Đây là **WAW (Write After Write)** về tên. Tương tự, WAR (Write After Read) có thể xuất hiện khi instruction trẻ ghi một tên mà instruction già còn cần đọc.

**Đổi tên thanh ghi (register renaming / 레지스터 리네이밍)** ánh xạ architectural registers sang physical registers lớn hơn:

```text
architectural r1 version A → physical P17
architectural r1 version B → physical P42
```

Renaming loại false dependency, để scheduler chỉ bị giới hạn bởi true data dependency và resource constraints.

## 5. Rename table, physical registers và lifetime

Rename stage giữ mapping từ architectural register tới physical register chứa version mới nhất. Khi instruction tạo value mới, CPU cấp physical register mới và cập nhật mapping cho instruction sau.

Physical register cũ không thể tái sử dụng ngay vì instruction speculative hoặc instruction chưa retire có thể vẫn tham chiếu nó. Free-list/lifetime management vì vậy gắn trực tiếp với retirement state.

Đây là một invariant nội bộ: **physical storage không được tái sử dụng khi vẫn còn architectural/speculative dependency hợp lệ tới version cũ**.

## 6. Reservation station / issue queue và wakeup-select

Sau rename, µops đi vào scheduling structures. Entry giữ operation, source tags/readiness và destination. Khi producer complete, dependent entries được wake up; scheduler chọn ready µops cho execution ports.

Đây không phải FIFO. Wakeup/select phải chạy cực nhanh mỗi cycle, nên scheduler width, issue-window size và bypass network tạo trade-off area/power/frequency.

Window lớn hơn có thể tìm nhiều independent work hơn, nhưng complexity tăng nhanh. Performance không tăng miễn phí chỉ bằng cách “cho nhiều instruction in-flight”.

## 7. Reorder Buffer giữ architectural invariant

**Reorder Buffer (ROB / 재정렬 버퍼)** theo dõi instructions theo program order sau khi chúng vào speculative back-end. Execution có thể complete out of order, nhưng ROB cho phép retire theo thứ tự.

ROB entry cần metadata đủ để biết instruction complete chưa, exception có xảy ra không, branch speculation có hợp lệ không và resource nào được release khi retire.

Invariant cốt lõi:

> Speculative execution được phép tạo intermediate state, nhưng software chỉ được quan sát architectural state tương ứng với một prefix hợp lệ của instruction stream.

## 8. Precise exception giải thích vì sao retirement order quan trọng

Giả sử instruction 10 page fault nhưng 11–20 đã execute. Nếu side effects của 11–20 trở thành architectural state không thể rollback, OS không thể xử lý exception như thể fault xảy ra chính xác tại instruction 10.

ROB dừng retirement tại faulting instruction, squash work trẻ hơn và chuyển control sang handler với state chính xác.

Đây là connection trực tiếp giữa microarchitecture và OS abstraction: page fault/signal/debugger chỉ hoạt động hợp lý vì processor giữ precise-state contract.

## 9. Memory operation khó hơn register dependency

Register dependency biết từ operand names sau rename. Memory dependency chỉ rõ khi addresses được tính.

```text
store [p] = 10
load  [q]
```

Nếu chưa biết `p == q`, CPU phải quyết định có cho load chạy sớm không. **Load/Store Queue (LSQ)**, memory disambiguation và dependency prediction giúp khai thác parallelism.

Nếu prediction sai và load đã đọc value không hợp lệ, dependent work phải replay hoặc squash. Performance pressure vì thế tạo speculation thêm một tầng ngoài branch prediction.

## 10. Store buffer nối OoO với memory ordering

Store có thể complete trong pipeline nhưng chưa globally visible. Store buffer giữ write trong khi coherence/ownership được xử lý. CPU có thể forward store cho load cùng core trước khi core khác thấy value.

Điều này nối trực tiếp tới [memory consistency và ordering](./00_memory_consistency_cache_coherence_and_ordering.md). OoO execution và memory ordering liên quan nhưng không phải cùng khái niệm: retirement order giữ architectural register/exception state, còn cross-core memory visibility tuân ISA memory model.

## 11. Branch speculation và rollback

OoO gần như luôn đi cùng branch prediction. Nếu processor chờ biết chắc mọi branch mới fetch tiếp, pipeline sẽ thường xuyên rỗng.

Speculative path có thể decode/execute sâu phía sau unresolved branch. Khi prediction đúng, latency bị che. Khi sai, processor phải khôi phục rename/checkpoint state và squash younger work.

Mispredict cost tăng khi pipeline sâu và lượng in-flight work lớn. Vì vậy prediction accuracy có tác động phi tuyến tới IPC trong nhiều workload.

## 12. Pointer chasing: khi OoO không tìm được việc độc lập

Ví dụ linked-list traversal:

```text
node = node.next
node = node.next
node = node.next
```

Address load tiếp theo chỉ biết sau khi load trước hoàn thành. Đây là dependency chain dài. ROB lớn hay nhiều ALU không tạo parallelism nếu workload không có independent work.

Ngược lại, xử lý nhiều array elements độc lập có thể tạo memory-level parallelism và vectorization tốt hơn.

Đây là connection quan trọng giữa data structure/layout và microarchitecture: hai thuật toán cùng Big-O có thể khác đáng kể về cache locality và available parallelism.

## 13. Performance pressure và giới hạn thực tế

Các resource hữu hạn gồm:

```text
ROB entries
issue/scheduling queue
physical registers
load/store queue
execution ports
memory-level parallelism slots
branch checkpoints
```

Khi một resource đầy, front-end/back-end có thể stall dù resource khác còn rảnh. Vì vậy câu “CPU utilization 100%” chưa giải thích bottleneck microarchitecture.

Power/thermal limits cũng quan trọng: window rộng và wakeup/select lớn tiêu tốn năng lượng; mobile/server cores chọn điểm cân bằng khác nhau.

## 14. Production evidence

Khi nghi OoO/back-end bottleneck, evidence hữu ích gồm sampling profiler + hardware performance counters: retired instructions, cycles, IPC, branch miss, cache/TLB miss, backend/frontend stalled cycles và memory-bandwidth pressure tùy CPU/tool.

Tên counter khác theo microarchitecture; mục tiêu không phải học thuộc event name mà là phân biệt các hypothesis:

```text
ít instruction parallelism?
branch speculation thất bại?
cache miss/pointer chasing?
execution-port pressure?
front-end không cấp đủ µop?
```

Static assembly inspection hữu ích nhưng không thay runtime evidence vì cache miss và branch behavior phụ thuộc workload.

## 15. Failure mode: correctness và security khác performance

OoO engine bình thường phải giữ architectural correctness qua ROB/rollback. Nhưng speculative microarchitectural state như cache có thể để lại side effect dù speculative instruction không retire. Đây là nền tảng reasoning cho Spectre-class side channels.

Điểm quan trọng là tách hai contract:

```text
architectural correctness:
wrong-path result không được commit thành architectural state

microarchitectural confidentiality:
wrong-path execution không được làm lộ secret qua timing side channel
```

Contract thứ nhất có thể đúng trong khi contract thứ hai bị khai thác. Không cần tạo chapter công nghệ riêng để thấy mental model này.

## 16. Common Misconceptions

**“Out-of-order nghĩa CPU thay đổi logic chương trình.”** Không. CPU reorder nội bộ nhưng phải giữ architectural contract.

**“Register renaming là compiler optimization.”** Compiler cũng có register allocation/renaming, nhưng hardware renaming diễn ra động để loại false dependency giữa in-flight instructions.

**“Instruction complete nghĩa đã commit.”** Không. Instruction có thể complete nhưng vẫn speculative và chưa retire.

**“ROB càng lớn thì luôn càng nhanh.”** Không. Nếu workload là dependency chain hoặc memory bandwidth đã saturated, window lớn hơn có thể không tạo speedup tương xứng.

## 17. Mô hình tư duy

> OoO CPU là speculative data-flow engine nằm sau một architectural-order contract. **Renaming loại false dependency; scheduler tìm ready work; LSQ suy luận memory dependency; ROB giữ precise retirement; rollback xóa speculative path sai.** Performance phụ thuộc lượng independent work thật sự và khả năng che latency, không chỉ GHz hay số execution units.

## Kết nối

Đọc cùng [Memory consistency và ordering](./00_memory_consistency_cache_coherence_and_ordering.md), [Branch prediction và speculation](./02_branch_prediction_speculation_and_pipeline_recovery.md), [Cache hierarchy](./03_advanced_cache_hierarchy_prefetching_and_replacement.md) và OS advanced về page fault/syscall. Khi debug performance xuyên tầng, nối tiếp [Debugging across abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).