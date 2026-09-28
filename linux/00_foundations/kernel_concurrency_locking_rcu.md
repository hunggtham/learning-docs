# Đồng thời, khóa và RCU trong Linux kernel

> **Mạch đọc:** Đọc **Đồng thời, khóa và RCU trong Linux kernel** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **tính đồng thời (concurrency / 동시성) khác parallelism** sang **Race điều kiện (condition / 조건) hình thành như thế nào?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi một máy chỉ có một CPU và kernel chỉ xử lý từng việc nối tiếp, bảo vệ trạng thái chung tương đối đơn giản. Nhưng Linux hiện đại chạy trên nhiều cốt lõi (core / 핵심), xử lý nhiều tiến trình (process / 프로세스), interrupt, softirq và kernel worker đồng thời. Cùng một cấu trúc dữ liệu có thể bị nhiều thực thi (execution / 실행) ngữ cảnh (context / 맥락) truy cập gần như cùng lúc.

Vì vậy một trong những nền tảng quan trọng nhất của kernel là **đồng thời (concurrency)**: làm sao cho nhiều luồng thực thi cùng tiến triển mà không làm hỏng trạng thái chung, không deadlock và không tạo độ trễ (latency / 지연 시간) không cần thiết.

Chương này không nhằm dạy viết kernel mô-đun (module / 모듈). Mục tiêu là hiểu vì sao Linux có spinlock, mutex, atomic thao tác (operation / 연산), wait hàng đợi (queue / 큐), seqlock và RCU; khi nào mã (code / 코드) được phép ngủ; và những thành phần nguyên thủy (primitive / 기본 요소) này liên hệ thế nào tới hiện tượng môi trường vận hành (production / 운영 환경) như tranh chấp khóa (lock contention / 잠금 경합), softirq backlog hoặc luồng thực thi (thread / 스레드) chờ `futex()`.

## Tính đồng thời (concurrency / 동시성) khác parallelism

**Đồng thời (concurrency)** nghĩa nhiều công việc có vòng đời chồng lấn và hệ thống phải quản lý tương tác giữa chúng. **Song song (parallelism)** nghĩa nhiều công việc thực sự chạy cùng lúc trên nhiều CPU/cốt lõi (core / 핵심).

Một máy một cốt lõi (core / 핵심) vẫn có tính đồng thời (concurrency / 동시성) do scheduler xen kẽ tiến trình (process / 프로세스) và do interrupt có thể xảy ra. Máy nhiều cốt lõi (core / 핵심) thêm parallelism, khiến race điều kiện (condition / 조건) có thể xuất hiện thực sự cùng thời điểm.

## Race điều kiện (condition / 조건) hình thành như thế nào?

Giả sử hai CPU cùng tăng một biến đếm:

```text
counter = counter + 1
```

Ở mã nguồn (source code / 소스 코드) đây trông như một thao tác. Ở machine mức (level / 수준) nó có thể gồm:

```text
load counter
add 1
store counter
```

Nếu hai CPU đọc cùng giá trị trước khi một CPU ghi lại, một lần tăng có thể bị mất.

Đây là **race điều kiện (condition / 조건)**: kết quả phụ thuộc thứ tự xen kẽ của các thao tác (operation / 연산) mà chương trình không kiểm soát đúng.

## “Chạy trong kernel” không có nghĩa là không bị tranh chấp

Một hiểu lầm phổ biến là kernel là một khối mã (code / 코드) duy nhất nên tự nhiên tuần tự. Thực tế kernel có thể xử lý đồng thời:

- lời gọi hệ thống (system call / 시스템 호출) từ nhiều tiến trình (process / 프로세스) trên nhiều CPU;
- interrupt trên nhiều CPU;
- softirq;
- kernel luồng thực thi (thread / 스레드);
- workqueue;
- timer callback;
- scheduler activity.

Một cấu trúc dữ liệu (data structure / 자료구조) toàn cục phải được thiết kế cho mô hình này.

## Trọng yếu (critical / 중요) section

**Vùng tới hạn (critical section)** là đoạn mã (code / 코드) thao tác trạng thái cần được bảo vệ khỏi truy cập đồng thời không an toàn.

Mục tiêu của synchronization không phải “khóa càng nhiều càng tốt”. Khóa quá rộng làm giảm parallelism và tăng contention.

Thiết kế tốt cố giảm phạm vi dùng chung (shared / 공유) mutable trạng thái (state / 상태) và giữ trọng yếu (critical / 중요) section đủ ngắn.

## Atomic thao tác (operation / 연산)

Một số thao tác nhỏ có thể dùng **atomic thao tác (operation / 연산)**, tức thao tác (operation / 연산) mà các CPU khác không quan sát thấy trạng thái trung gian theo guarantee tương ứng.

Ví dụ kernel có các thành phần nguyên thủy (primitive / 기본 요소) atomic counter thay vì bảo vệ mọi increment bằng mutex.

Atomic thao tác (operation / 연산) hữu ích cho thao tác nhỏ, nhưng không giải quyết giao dịch (transaction / 트랜잭션) gồm nhiều bước lô-gic (logic / 논리).

Nếu cần bảo đảm quan hệ:

```text
kiểm tra trạng thái A
rồi cập nhật B
rồi cập nhật C
```

một atomic increment riêng lẻ thường không đủ.

## Spinlock: chờ bằng cách quay

**Spinlock** phù hợp khi trọng yếu (critical / 중요) section rất ngắn và ngữ cảnh (context / 맥락) không thể ngủ.

Khi khóa (lock / 잠금) đang bị giữ, CPU chờ có thể “spin”, tức lặp kiểm tra cho tới khi khóa (lock / 잠금) được giải phóng.

Mô hình tư duy (mental model / 사고 모델):

```text
CPU 0: acquire -> critical section -> release
CPU 1:          spin spin spin -> acquire
```

Nếu giữ spinlock quá lâu, CPU khác đốt CPU thời gian (time / 시간) chỉ để chờ. Vì vậy spinlock phải đi kèm discipline rất chặt.

## Vì sao interrupt ngữ cảnh (context / 맥락) cần thành phần nguyên thủy (primitive / 기본 요소) khác tiến trình (process / 프로세스) ngữ cảnh (context / 맥락)?

Mã (code / 코드) trong interrupt ngữ cảnh (context / 맥락) không thể hành xử giống một tiến trình (process / 프로세스) bình thường. Nó không có quyền ngủ tùy ý chờ một mutex rồi để scheduler xử lý như luồng thực thi (thread / 스레드) thông thường.

Vì vậy kernel phải phân biệt ngữ cảnh (context / 맥락):

- tiến trình (process / 프로세스) ngữ cảnh (context / 맥락);
- interrupt ngữ cảnh (context / 맥락);
- softirq ngữ cảnh (context / 맥락);
- preemption trạng thái (state / 상태).

Một thành phần nguyên thủy (primitive / 기본 요소) hợp lệ ở tiến trình (process / 프로세스) ngữ cảnh (context / 맥락) có thể không hợp lệ trong interrupt ngữ cảnh (context / 맥락).

Đây là lý do câu hỏi “khóa (lock / 잠금) nào nhanh hơn?” quá đơn giản. Câu hỏi đúng trước tiên là **ngữ cảnh (context / 맥락) này có được phép sleep không?**

## Mutex: chờ bằng cách ngủ

**Mutex** thường dùng khi holder có thể giữ khóa (lock / 잠금) lâu hơn và waiter được phép sleep.

Thay vì quay CPU vô ích, tác vụ (task / 작업) không lấy được mutex có thể bị khối (block / 블록), scheduler chạy tác vụ (task / 작업) khác, rồi tác vụ (task / 작업) được wake khi khóa (lock / 잠금) sẵn sàng.

Điều này giảm lãng phí CPU nhưng có chi phí scheduling/wakeup.

Spinlock và mutex vì vậy không chỉ khác hiện thực (implementation / 구현); chúng phù hợp với hai mô hình chờ khác nhau.

## Semaphore

Semaphore biểu diễn một số lượng permit thay vì chỉ trạng thái locked/unlocked. Nó có thể phù hợp khi có N tài nguyên (resource / 자원) tương đương.

Trong user-space, liên kết (connection / 연결) pool có mô hình tư duy (mental model / 사고 모델) gần giống semaphore: chỉ một số lượng giới hạn yêu cầu (request / 요청) được giữ liên kết (connection / 연결) cùng lúc.

Kernel có nhiều thành phần nguyên thủy (primitive / 기본 요소) hiện đại chuyên biệt hơn cho từng use trường hợp (case / 사례); không nên coi semaphore là thành phần nguyên thủy (primitive / 기본 요소) mặc định cho mọi synchronization.

## Read-write khóa (lock / 잠금)

Nếu tải công việc (workload / 워크로드) có nhiều reader và ít writer, reader-writer khóa (lock / 잠금) cho phép nhiều reader cùng truy cập khi không có writer.

Tuy nhiên loại khóa (lock / 잠금) này không tự động nhanh hơn mutex. Overhead, starvation và cache-line contention có thể khiến lợi ích phụ thuộc tải công việc (workload / 워크로드).

Một thiết kế read-heavy cực lớn có thể phù hợp hơn với RCU.

## Seqlock

**chuỗi (sequence / 시퀀스) khóa (lock / 잠금) (seqlock)** tối ưu cho trường hợp reader rất nhanh và có thể thử lại (retry / 재시도).

Writer cập nhật chuỗi (sequence / 시퀀스) counter quanh quá trình ghi. Reader:

1. đọc chuỗi (sequence / 시퀀스);
2. đọc dữ liệu;
3. kiểm tra chuỗi (sequence / 시퀀스) có thay đổi không;
4. nếu thay đổi thì đọc lại.

Reader có thể không cần khối (block / 블록) writer, nhưng phải chấp nhận thử lại (retry / 재시도) và không phù hợp với mọi loại dữ liệu.

## RCU là gì?

**Read-Copy-Update (RCU)** là kỹ thuật synchronization quan trọng trong Linux cho tải công việc (workload / 워크로드) đọc cực nhiều, ghi ít.

Ý tưởng khái niệm:

```text
reader đọc phiên bản hiện tại gần như không khóa
writer tạo/cập nhật phiên bản mới
writer publish pointer mới
phiên bản cũ chỉ được giải phóng sau khi chắc chắn reader cũ đã rời critical section
```

Thay vì bắt mọi reader tranh một khóa (lock / 잠금), RCU tối ưu read đường dẫn (path / 경로).

## Grace period trong RCU

Sau khi writer thay pointer, vẫn có thể có reader đang giữ tham chiếu (reference / 참조) tới đối tượng (object / 객체) cũ.

Writer không thể `free()` đối tượng (object / 객체) cũ ngay.

RCU chờ một **grace period**: khoảng thời gian đủ để các reader trước đó hoàn tất trọng yếu (critical / 중요) section liên quan. Sau đó đối tượng (object / 객체) cũ mới được reclaim an toàn.

Điểm sâu ở đây là synchronization không chỉ là “ai được vào trọng yếu (critical / 중요) section”. Nó còn là **quản lý thời gian tồn tại (lifetime / 수명) của đối tượng (object / 객체) khi reader lockless vẫn có thể giữ tham chiếu (reference / 참조)**.

## Tham chiếu (reference / 참조) counting

Một kỹ thuật khác để quản lý thời gian tồn tại (lifetime / 수명) là **đếm tham chiếu (reference counting)**.

Khi có thêm tham chiếu (reference / 참조), count tăng; khi bản phát hành (release / 릴리스) tham chiếu (reference / 참조), count giảm. đối tượng (object / 객체) chỉ được free khi count về 0.

Linux dùng nhiều dạng tham chiếu (reference / 참조) counting cho kernel đối tượng (object / 객체).

Nhưng tham chiếu (reference / 참조) counting không giải quyết mọi race. Nếu luồng thực thi (thread / 스레드) cố tăng count sau khi đối tượng (object / 객체) đã về 0 và đang được free, vẫn cần quy tắc publication/thời gian tồn tại (lifetime / 수명) đúng.

Do đó tham chiếu (reference / 참조) counting và locking thường phối hợp thay vì thay thế hoàn toàn nhau.

## Bộ nhớ (memory / 메모리) thứ tự (ordering / 순서): atomic chưa chắc đủ

CPU và trình biên dịch (compiler / 컴파일러) có thể sắp xếp lại thao tác (operation / 연산) trong giới hạn bộ nhớ (memory / 메모리) mô hình (model / 모델) để tối ưu hiệu năng.

Vì vậy concurrent mã (code / 코드) cần quan tâm không chỉ “thao tác (operation / 연산) có atomic không” mà còn “các CPU khác được phép quan sát thứ tự bộ nhớ (memory / 메모리) thao tác (operation / 연산) ra sao”.

Kernel sử dụng **bộ nhớ (memory / 메모리) barrier** và ngữ nghĩa (semantics / 의미론) acquire/bản phát hành (release / 릴리스) trong nhiều thành phần nguyên thủy (primitive / 기본 요소).

Ví dụ writer muốn publish đối tượng (object / 객체):

```text
ghi toàn bộ fields của object
        ↓
publish pointer
```

Nếu CPU khác nhìn pointer trước khi nhìn đầy đủ trường dữ liệu (field / 필드) cập nhật (update / 업데이트), reader có thể thấy đối tượng (object / 객체) chưa hoàn chỉnh. thành phần nguyên thủy (primitive / 기본 요소) synchronization phải thiết lập thứ tự (ordering / 순서) cần thiết.

Đây là lý do viết lock-free mã (code / 코드) chính xác khó hơn rất nhiều so với chỉ dùng atomic integer.

## Bộ nhớ đệm (cache / 캐시) coherence và false sharing

Nhiều CPU cốt lõi (core / 핵심) có bộ nhớ đệm (cache / 캐시) riêng nhưng phải duy trì coherence cho bộ nhớ (memory / 메모리) chia sẻ.

Nếu nhiều cốt lõi (core / 핵심) liên tục ghi vào cùng bộ nhớ đệm (cache / 캐시) line, bộ nhớ đệm (cache / 캐시) line có thể “ping-pong” giữa cốt lõi (core / 핵심) và làm hiệu năng (performance / 성능) giảm mạnh.

Ngay cả khi hai biến lô-gic (logic / 논리) khác nhau nhưng nằm cùng bộ nhớ đệm (cache / 캐시) line, chúng vẫn có thể gây **false sharing**.

Vì vậy scalability của kernel không chỉ phụ thuộc số khóa (lock / 잠금); bố cục (layout / 레이아웃) dữ liệu và locality cũng quan trọng.

## Per-CPU dữ liệu (data / 데이터)

Một chiến lược giảm contention là giữ dữ liệu **per-CPU** thay vì dùng một biến toàn cục (global / 전역).

Ví dụ mỗi CPU có counter riêng rồi tổng hợp khi cần. cập nhật (update / 업데이트) fast đường dẫn (path / 경로) không phải tranh cùng một bộ nhớ đệm (cache / 캐시) line.

Đánh đổi là việc đọc tổng giá trị phức tạp hơn và có thể chỉ nhất quán tương đối tùy ngữ nghĩa (semantics / 의미론).

Đây là mẫu (pattern / 패턴) rất quan trọng trong kernel hiệu năng (performance / 성능).

## Wait hàng đợi (queue / 큐)

Khi tác vụ (task / 작업) phải chờ một điều kiện (condition / 조건), kernel không nên busy-spin vô hạn trong tiến trình (process / 프로세스) ngữ cảnh (context / 맥락). tác vụ (task / 작업) có thể ngủ trên **wait hàng đợi (queue / 큐)**.

Mô hình tư duy (mental model / 사고 모델):

```text
condition chưa đúng
→ task đăng ký chờ
→ task sleep
→ producer/event thay đổi state
→ wake_up
→ task runnable
→ scheduler cho chạy lại
```

Socket read, pipe, thiết bị (device / 장치) I/O và nhiều subsystem sử dụng những ý tưởng tương tự.

Wait hàng đợi (queue / 큐) nối synchronization với scheduler.

## Futex: phần lớn khóa (lock / 잠금) ở user-space, kernel chỉ can thiệp khi tranh chấp

Trong user-space, pthread mutex và nhiều thời gian chạy (runtime / 런타임) khóa (lock / 잠금) có thể dựa trên **futex (fast userspace mutex)**.

Fast đường dẫn (path / 경로) khi khóa (lock / 잠금) không bị tranh có thể hoàn tất bằng atomic thao tác (operation / 연산) trong người dùng (user / 사용자) không gian (space / 공간) mà không gọi kernel.

Khi có contention, luồng thực thi (thread / 스레드) dùng `futex()` lời gọi hệ thống (system call / 시스템 호출) để ngủ/wake thông qua kernel.

Mô hình tư duy (mental model / 사고 모델):

```text
uncontended lock
→ user-space atomic only

contended lock
→ futex syscall
→ waiter sleep
→ wake later
```

Đây là một ví dụ đẹp về thiết kế tránh privilege chuyển tiếp (transition / 전이) khi chưa cần.

Nếu `strace` cho thấy nhiều `futex()` chờ lâu, đó có thể là dấu hiệu contention ở thời gian chạy (runtime / 런타임)/ứng dụng (application / 애플리케이션), không phải kernel “bị chậm”.

## Deadlock

Deadlock có thể xảy ra khi nhiều thực thi (execution / 실행) ngữ cảnh (context / 맥락) giữ tài nguyên rồi chờ lẫn nhau.

Ví dụ:

```text
Task A giữ lock X, chờ lock Y
Task B giữ lock Y, chờ lock X
```

Không tác vụ (task / 작업) nào tiến triển được.

Kernel mã (code / 코드) phải dùng quy tắc khóa (lock / 잠금) thứ tự (ordering / 순서) rất chặt.

Ở tầng ứng dụng (application / 애플리케이션), cùng nguyên lý xuất hiện với Java monitor, cơ sở dữ liệu (database / 데이터베이스) row khóa (lock / 잠금) hoặc phân tán (distributed / 분산) khóa (lock / 잠금).

## Khóa (lock / 잠금) thứ tự (ordering / 순서)

Một cách tránh deadlock là định nghĩa thứ tự lấy khóa (lock / 잠금) cố định:

```text
luôn acquire A trước B
```

Nếu mọi đường mã (code / 코드) tuân thủ cùng thứ tự, vòng chờ A↔B bị loại bỏ.

Đây là ví dụ cho thấy tính đúng đắn (correctness / 정확성) của synchronization là thuộc tính của **toàn bộ giao thức (protocol / 프로토콜)**, không phải của từng khóa (lock / 잠금) riêng lẻ.

## Priority inversion

Tác vụ (task / 작업) ưu tiên cao có thể bị khối (block / 블록) bởi tác vụ (task / 작업) ưu tiên thấp đang giữ khóa (lock / 잠금). Nếu tác vụ (task / 작업) ưu tiên trung bình liên tục chiếm CPU, tác vụ (task / 작업) thấp khó chạy để bản phát hành (release / 릴리스) khóa (lock / 잠금), khiến tác vụ (task / 작업) cao bị trì hoãn gián tiếp.

Đây là **priority inversion**.

Một số hệ thống dùng priority inheritance trong thành phần nguyên thủy (primitive / 기본 요소) phù hợp để giảm vấn đề này.

Khái niệm quan trọng với real-time tải công việc (workload / 워크로드) và latency-sensitive hệ thống (system / 시스템).

## Preemption và trọng yếu (critical / 중요) section

Nếu kernel tác vụ (task / 작업) đang sửa cấu trúc per-CPU rồi bị migrate giữa CPU ở thời điểm không phù hợp, invariants có thể bị phá.

Vì vậy một số trọng yếu (critical / 중요) section cần kiểm soát preemption hoặc di chuyển (migration / 마이그레이션).

Nhưng disable preemption quá lâu làm tăng scheduling độ trễ (latency / 지연 시간).

Tương tự với interrupt disable: nó là công cụ mạnh nhưng kéo dài thời gian interrupt bị chặn có thể gây độ trễ (latency / 지연 시간) toàn hệ thống.

## Interrupt disabling không phải khóa (lock / 잠금) tổng quát

Trên máy nhiều CPU, disable interrupt trên CPU hiện tại không ngăn CPU khác truy cập dùng chung (shared / 공유) dữ liệu (data / 데이터).

Do đó mã (code / 코드) SMP vẫn cần synchronization phù hợp.

Điều này cho thấy nhiều kỹ thuật từng đủ trên uniprocessor không đủ trên hệ thống đa cốt lõi (core / 핵심).

## RCU, khóa (lock / 잠금) và scalability

Có thể hình dung một phổ thiết kế:

```text
coarse global lock
    ↓ dễ đúng, nhưng contention cao
fine-grained locks
    ↓ parallel hơn, protocol phức tạp hơn
per-CPU / lockless / RCU
    ↓ scalability cao trong workload phù hợp
    ↓ reasoning khó hơn nhiều
```

Không có thành phần nguyên thủy (primitive / 기본 요소) “tốt nhất”. Lựa chọn phụ thuộc read/ghi (write / 쓰기) ratio, sleepability, độ trễ (latency / 지연 시간), thời gian tồn tại (lifetime / 수명) và tính đúng đắn (correctness / 정확성) requirements.

## Quan sát contention từ người dùng (user / 사용자) không gian (space / 공간)

Không cần viết kernel mã (code / 코드) vẫn có thể quan sát triệu chứng synchronization.

```bash
pidstat -w -p <PID> 1
perf sched timehist
perf lock record -- <command>
```

Khả năng công cụ phụ thuộc kernel/cấu hình (config / 설정)/permission.

Với Java:

```bash
jcmd <PID> Thread.print
```

Luồng thực thi (thread / 스레드) dump có thể cho thấy nhiều luồng thực thi (thread / 스레드) BLOCKED trên cùng monitor. Đây là tầng ứng dụng (application / 애플리케이션), nhưng mô hình tư duy (mental model / 사고 모델) contention giống kernel: nhiều thực thi (execution / 실행) ngữ cảnh (context / 맥락) cạnh tranh trạng thái dùng chung (shared state / 공유 상태).

## Ngữ cảnh (context / 맥락) switch tự nguyện và không tự nguyện

Một tác vụ (task / 작업) có thể tự nguyện nhường CPU vì chờ khóa (lock / 잠금)/I/O hoặc bị scheduler preempt.

`pidstat -w` có thể cung cấp số ngữ cảnh (context / 맥락) switch tự nguyện và không tự nguyện.

Con số cao không tự động xấu. Cần đặt cạnh tải công việc (workload / 워크로드), độ trễ (latency / 지연 시간) và blocking mô hình (model / 모델).

Một máy chủ (server / 서버) xử lý nhiều blocking I/O tự nhiên có nhiều ngữ cảnh (context / 맥락) switch hơn một vòng tính CPU đơn luồng.

## Khóa (lock / 잠금) convoy

Nếu nhiều tác vụ (task / 작업) cùng chờ một khóa (lock / 잠금) và sau mỗi lần bản phát hành (release / 릴리스) chỉ một tác vụ (task / 작업) tiến lên rất ngắn rồi lại tranh khóa (lock / 잠금), hệ thống có thể tạo **khóa (lock / 잠금) convoy**.

Thông lượng (throughput / 처리량) giảm dù CPU vẫn hoạt động mạnh.

Mẫu này cũng xuất hiện ở cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool, synchronized section hoặc toàn cục (global / 전역) hàng đợi (queue / 큐) trong ứng dụng (application / 애플리케이션).

## Thundering herd

Nếu một sự kiện (event / 이벤트) đánh thức quá nhiều waiter nhưng chỉ một hoặc vài waiter có thể thực sự làm việc, các tác vụ (task / 작업) còn lại tốn CPU để wake rồi ngủ lại.

Đây là **thundering herd**.

Các API như `epoll` và cơ chế wakeup hiện đại cố giảm vấn đề này trong những use trường hợp (case / 사례) nhất định.

## Kernel lockup và watchdog

Nếu CPU mắc quá lâu trong kernel mà không schedule hoặc interrupt đúng cách, hệ thống có thể báo soft lockup/hard lockup tùy tình huống.

Kiểm tra kernel log:

```bash
journalctl -k | grep -Ei 'lockup|stall|hung task|rcu'
```

Các cảnh báo này không giống ứng dụng (application / 애플리케이션) deadlock thông thường. Chúng cho thấy kernel thực thi (execution / 실행) hoặc CPU progress đang có vấn đề nghiêm trọng hơn.

## RCU stall

Kernel có thể báo RCU stall nếu grace period không thể tiến triển như dự kiến, ví dụ CPU giữ trạng thái khiến RCU không nhận được quiescent trạng thái (state / 상태) trong thời gian dài.

Đây là dấu hiệu cần xem CPU lockup, interrupt/preemption hoặc kernel/mô-đun (module / 모듈) hành vi (behavior / 동작), không nên xử lý bằng cách tăng hết thời gian chờ (timeout / 타임아웃) một cách mù quáng.

## Mô hình tư duy (mental model / 사고 모델)

Hãy xem kernel như một hệ thống nhiều thực thi (execution / 실행) ngữ cảnh (context / 맥락) cùng thao tác một đồ thị đối tượng (object / 객체) sống động.

Synchronization phải giải quyết ba câu hỏi:

```text
1. Ai được truy cập cùng lúc?
2. Những operation phải được quan sát theo thứ tự nào?
3. Object được phép tồn tại đến khi nào?
```

Khóa (lock / 잠금) giải quyết phần mutual exclusion. bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) giải quyết visibility/thứ tự (order / 순서). tham chiếu (reference / 참조) counting và RCU giải quyết thời gian tồn tại (lifetime / 수명) trong nhiều thiết kế.

## Những hiểu lầm phổ biến

**“Atomic nghĩa là thread-safe cho toàn bộ thuật toán.”** Atomic chỉ bảo vệ ngữ nghĩa (semantics / 의미론) của thao tác (operation / 연산) tương ứng; bất biến (invariant / 불변식) nhiều bước có thể vẫn race.

**“Spinlock nhanh hơn mutex nên nên dùng spinlock.”** Nếu waiter có thể sleep hoặc trọng yếu (critical / 중요) section dài, spin có thể lãng phí CPU nghiêm trọng.

**“RCU là một mutex nhanh.”** RCU là một mô hình synchronization/thời gian tồn tại (lifetime / 수명) khác, đặc biệt tối ưu read-heavy tải công việc (workload / 워크로드).

**“Disable interrupt là đủ để bảo vệ dùng chung (shared / 공유) dữ liệu (data / 데이터).”** Không trên SMP; CPU khác vẫn có thể truy cập.

**“Nhiều ngữ cảnh (context / 맥락) switch chắc chắn là lỗi.”** Phải hiểu blocking mô hình (model / 모델) và tải công việc (workload / 워크로드) trước.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Chương này nên được đọc cùng:

- [CPU privilege và syscall path](./cpu_privilege_exceptions_syscall_path.md) để biết các thực thi (execution / 실행) ngữ cảnh (context / 맥락) đi vào kernel thế nào;
- [Interrupt và softirq](./interrupts_softirq_device_model.md) để hiểu ngữ cảnh (context / 맥락) không được sleep;
- [Process, thread và scheduler](../04_process/processes_threads_signals_jobs.md);
- [Kernel scheduler deep dive](../06_resources/kernel_scheduler_deep_dive.md);
- [IPC](../04_process/interprocess_communication.md) để nối wait hàng đợi (queue / 큐), futex, socket và event-driven I/O;
- [Tracing](../09_production/observability_tracing_strace_perf.md) để quan sát contention và off-CPU thời gian (time / 시간).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [cpu privilege exceptions syscall path](./cpu_privilege_exceptions_syscall_path.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
