# Quan sát sâu hệ thống: strace, perf và tracing

> **Mạch đọc:** Đọc **Quan sát sâu hệ thống: strace, perf và tracing** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Tracing khác logging như thế nào?** sang **strace: quan sát lời gọi hệ thống**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi log ứng dụng không đủ, bước tiếp theo không nhất thiết là thêm `DEBUG` rồi restart. Linux cung cấp nhiều cơ chế để quan sát một tiến trình đang làm gì ở ranh giới kernel, đang tiêu CPU ở đâu và đang chờ loại tài nguyên nào.

Các công cụ như `strace`, `perf`, `pidstat`, `lsof`, `ss` và eBPF-based tools mở rộng khả năng quan sát mà không cần sửa mã (code / 코드) ngay lập tức.

## Tracing khác logging như thế nào?

Logging là dữ liệu ứng dụng chủ động phát ra. Tracing cấp hệ điều hành có thể quan sát hành vi ngay cả khi ứng dụng (application / 애플리케이션) không log.

Ví dụ ứng dụng (application / 애플리케이션) chỉ báo:

```text
request timeout
```

Nhưng tracing có thể giúp phân biệt:

- tiến trình (process / 프로세스) đang `connect()` mãi tới phụ thuộc (dependency / 의존성);
- đọc tệp (file / 파일) cấu hình (config / 설정) bị `EACCES`;
- gọi `futex()` nhiều vì tranh chấp khóa (lock contention / 잠금 경합);
- liên tục `stat()` hàng nghìn tệp (file / 파일);
- `read()` từ socket trả chậm;
- CPU đang bị consume trong một hàm (function / 함수) cụ thể.

## `strace`: quan sát lời gọi hệ thống

`strace` theo dõi hệ thống (system / 시스템) calls và signals của tiến trình (process / 프로세스).

Chạy một command dưới strace:

```bash
strace ls /tmp
```

Đầu ra (output / 출력) khá dài vì một chương trình đơn giản vẫn cần tải (load / 로드) libraries, inspect locale, mở directory và ghi đầu ra (output / 출력).

Do đó nên filter.

### Theo dõi file-related calls

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
strace -e trace=file cat /etc/hosts
```

Hoặc cụ thể:

```bash
strace -e openat,read,write,close cat /etc/hosts
```

### Theo dõi mạng (network / 네트워크)

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
strace -e trace=network curl -s https://example.com >/dev/null
```

Có thể thấy `socket()`, `connect()`, `sendto()`, `recvfrom()` hoặc calls liên quan.

## Attach vào tiến trình đang chạy

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
sudo strace -p 1234
```

Điều này attach debugger-like observer vào tiến trình (process / 프로세스) hiện tại.

Cần thận trọng trên môi trường vận hành (production / 운영 환경). `strace` có overhead, đặc biệt với tiến trình (process / 프로세스) có syscall tỷ lệ (rate / 비율) cao.

Nên:

- dấu vết (trace / 추적) trong thời gian ngắn;
- filter syscalls;
- ghi đầu ra (output / 출력) ra tệp (file / 파일);
- tránh attach hàng loạt threads nếu không cần.

Ví dụ:

```bash
sudo timeout 10s strace -tt -T -p 1234 -e trace=network -o /tmp/strace-net.txt
```

`-tt` thêm timestamp chi tiết. `-T` cho thời gian syscall. `timeout` giới hạn tracing 10 giây.

## `-f` và multi-thread/tiến trình (process / 프로세스)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
strace -f command
```

`-f` theo child processes/threads phù hợp theo hiện thực (implementation / 구현).

Với Java, đầu ra (output / 출력) có thể rất lớn vì JVM có nhiều threads. Chỉ dùng khi thực sự cần và nên filter mạnh.

## Đọc lỗi syscall

Ví dụ:

```text
openat(..., "/opt/app/config.yml", O_RDONLY) = -1 EACCES (Permission denied)
```

Đây là bằng chứng (evidence / 증거) rất trực tiếp: kernel từ chối open với `EACCES`.

Nếu ứng dụng (application / 애플리케이션) khung phần mềm (framework / 프레임워크) chỉ báo “failed to tải (load / 로드) cấu hình (configuration / 구성)”, strace giúp xuống đúng tầng (layer / 계층).

Các errno thường gặp:

- `ENOENT` — đối tượng (object / 객체)/đường dẫn (path / 경로) thành phần (component / 컴포넌트) không tồn tại;
- `EACCES` — bị từ chối quyền;
- `ECONNREFUSED` — kết nối bị từ chối;
- `ETIMEDOUT` — hết thời gian chờ (timeout / 타임아웃);
- `EMFILE` — tiến trình (process / 프로세스) hết tệp (file / 파일) descriptor limit;
- `ENOSPC` — không còn không gian (space / 공간)/tài nguyên (resource / 자원) tương ứng.

## Khi strace cho thấy `futex()` rất nhiều

`futex` là thành phần nguyên thủy (primitive / 기본 요소) kernel thường được thời gian chạy (runtime / 런타임) sử dụng để xây mutex/điều kiện (condition / 조건) synchronization.

Nếu Java tiến trình (process / 프로세스) bị hang và strace chỉ thấy nhiều `futex`, điều đó không tự động nghĩa kernel lỗi. Có thể threads đang chờ khóa (lock / 잠금)/điều kiện (condition / 조건).

Bước tiếp theo thường là luồng thực thi (thread / 스레드) dump:

```bash
jcmd <PID> Thread.print
```

Hệ điều hành cho thấy “đang chờ synchronization”; JVM cho biết Java monitor/ngăn xếp (stack / 스택) nào liên quan.

Đây là ví dụ kết hợp hai tầng khả năng quan sát (observability / 관측 가능성).

## `perf`: quan sát CPU thực thi (execution / 실행)

`perf` dùng kernel hiệu năng (performance / 성능) subsystem để thu thập hardware/software counters và sampling profiles.

Các command cơ bản:

```bash
perf stat command
```

có thể báo CPU cycles, instructions, ngữ cảnh (context / 맥락) switches và counters khác tùy quyền/hardware.

Sampling tiến trình (process / 프로세스):

```bash
sudo perf top -p 1234
```

hoặc bản ghi (record / 레코드):

```bash
sudo perf record -F 99 -p 1234 -g -- sleep 30
sudo perf report
```

`-F 99` sampling khoảng 99 Hz. `-g` cố thu lời gọi (call / 호출) đồ thị (graph / 그래프).

## Sampling thay vì dấu vết (trace / 추적) mọi sự kiện (event / 이벤트)

`strace` có thể observe gần như từng syscall, còn `perf` thường sampling CPU instruction thực thi (execution / 실행).

Sampling chấp nhận không thấy mọi sự kiện (event / 이벤트) để đổi lấy overhead thấp hơn và profile thống kê.

Đây là cùng tư duy với statistics: không cần đo mọi instruction để biết phần lớn CPU thời gian (time / 시간) tập trung ở đâu.

## Java và perf

JIT làm Java profiling ở OS mức (level / 수준) phức tạp hơn bản địa (native / 네이티브) nhị phân (binary / 이진) vì mã (code / 코드) được sinh thời gian chạy (runtime / 런타임). Tooling như async-profiler thường phù hợp hơn cho JVM và có thể dùng perf events bên dưới.

Khi Java high CPU, một workflow tốt có thể là:

```text
pidstat/top xác định PID
    ↓
pidstat -t xác định thread
    ↓
JVM thread dump / async-profiler
    ↓
perf nếu cần OS/native-level evidence
```

Không nên bắt đầu bằng công cụ (tool / 도구) phức tạp nhất.

## `pidstat`: cầu nối (bridge / 브리지) giữa metrics và tracing

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
pidstat -p 1234 1
pidstat -t -p 1234 1
pidstat -d -p 1234 1
pidstat -w -p 1234 1
```

Tùy phiên bản (version / 버전), các option cho CPU, luồng thực thi (thread / 스레드), I/O và context-switch view.

`pidstat` có overhead thấp và rất phù hợp làm bước đầu trước `strace`/`perf`.

## `lsof`: đối tượng (object / 객체) relationship tracing

`lsof` không phải hiệu năng (performance / 성능) tracer nhưng cực kỳ hữu ích để trả lời “tiến trình (process / 프로세스) đang giữ cái gì?”

```bash
sudo lsof -p 1234
```

Có thể thấy:

- files;
- sockets;
- pipes;
- dùng chung (shared / 공유) libraries;
- hiện tại (current / 현재) working directory;
- deleted-open files.

Đây là cách nối tiến trình (process / 프로세스) mô hình (model / 모델) với filesystem/mạng (network / 네트워크) mô hình (model / 모델).

## `ss`: trạng thái socket

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
sudo ss -antp
```

Cho thấy TCP states và tiến trình (process / 프로세스) association khi đủ quyền.

Khi ứng dụng (application / 애플리케이션) báo liên kết (connection / 연결) pool exhaustion, nhìn số `ESTAB`, `CLOSE-WAIT`, `SYN-SENT` có thể tạo thêm hypothesis.

## `/proc/<PID>/stack` và kernel ngăn xếp (stack / 스택)

Trong một số điều kiện/quyền:

```bash
sudo cat /proc/1234/stack
```

có thể cho kernel ngăn xếp (stack / 스택) của tác vụ (task / 작업).

Nếu tiến trình (process / 프로세스) ở `D` trạng thái (state / 상태), kernel ngăn xếp (stack / 스택) đôi khi cho thấy nó đang chờ khối (block / 블록) I/O, NFS hoặc driver đường dẫn (path / 경로) nào.

Đây là diagnostic nâng cao, cần hiểu symbol/kernel ngữ cảnh (context / 맥락) trước khi kết luận.

## eBPF là gì?

**eBPF (extended Berkeley Packet Filter)** cho phép chạy các chương trình được kernel kiểm chứng tại các hook points khác nhau để thu thập/biến đổi telemetry với overhead tương đối thấp trong nhiều use trường hợp (case / 사례).

Các toolsets như BCC hoặc bpftrace có thể quan sát:

- syscall độ trễ (latency / 지연 시간);
- khối (block / 블록) I/O độ trễ (latency / 지연 시간);
- TCP retransmission;
- scheduler độ trễ (latency / 지연 시간);
- tệp (file / 파일) opens;
- hàm (function / 함수) probes.

Ví dụ bpftrace cú pháp (syntax / 문법) có thể giống:

```bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_openat { @[comm] = count(); }'
```

Nhưng availability phụ thuộc kernel, permissions và gói (package / 패키지).

## Vì sao eBPF mạnh nhưng không nên dùng mù quáng?

Nó cho visibility sâu, nhưng:

- cần quyền cao;
- có phiên bản (version / 버전)/kernel dependencies;
- truy vấn (query / 쿼리) sai có thể tạo overhead;
- đầu ra (output / 출력) dễ bị diễn giải sai nếu không hiểu kernel đường dẫn (path / 경로).

Cấp cao (senior / 시니어) không phải người luôn dùng eBPF; cấp cao (senior / 시니어) chọn **công cụ ít phức tạp nhất đủ để phân biệt giả thuyết**.

## Off-CPU phân tích (analysis / 분석)

CPU profiling chỉ cho nơi tiến trình (process / 프로세스) chạy. Nhưng độ trễ (latency / 지연 시간) có thể đến từ nơi tiến trình (process / 프로세스) **không chạy** vì đang chờ khóa (lock / 잠금), disk, mạng (network / 네트워크) hoặc scheduler.

Off-CPU phân tích (analysis / 분석) quan sát thời gian luồng thực thi (thread / 스레드) bị blocked/sleeping.

Đây là lý do API độ trễ (latency / 지연 시간) cao nhưng CPU thấp không nên kết luận “máy chủ (server / 서버) còn khỏe”.

Một hệ thống có thể dành 95% thời gian chờ cơ sở dữ liệu (database / 데이터베이스) và chỉ 5% CPU.

## Flame đồ thị (graph / 그래프)

Flame đồ thị (graph / 그래프) là cách trực quan hóa ngăn xếp (stack / 스택) samples.

Chiều ngang biểu diễn tỷ lệ samples; chiều dọc là ngăn xếp lời gọi (call stack / 호출 스택) độ sâu (depth / 깊이). Một vùng rộng nghĩa hàm (function / 함수)/đường dẫn (path / 경로) xuất hiện trong nhiều samples.

Không nên đọc chiều ngang như timeline. Flame đồ thị (graph / 그래프) truyền thống là phân phối (distribution / 분포), không phải trình tự thời gian.

## Tracing trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)

OS tracing cho biết tiến trình (process / 프로세스)/kernel hành vi (behavior / 동작) trên một host. phân tán (distributed / 분산) tracing như OpenTelemetry cho biết đường đi của yêu cầu (request path / 요청 경로) giữa services.

Hai loại bổ sung nhau:

```text
Distributed trace: request chậm ở service B
                     ↓
Host tracing: service B chậm vì network connect / disk / CPU / lock
```

## Methodology: từ rẻ đến sâu

Một quy trình tốt thường đi từ low-overhead tới high-detail:

```text
metrics/logs
↓
ps / ss / lsof / pidstat
↓
/proc inspection
↓
strace ngắn và filtered
↓
perf / JVM profiler
↓
eBPF / kernel-level deep tracing
```

Không phải sự cố (incident / 인시던트) nào cũng cần xuống cuối.

## Ví dụ: Java dịch vụ (service / 서비스) độ trễ (latency / 지연 시간) cao nhưng CPU thấp

Bắt đầu:

```bash
pidstat -p <PID> 1
sudo ss -antp | grep <PID>
jcmd <PID> Thread.print
```

Nếu nhiều threads chờ socket read tới DB, có thể dấu vết (trace / 추적) mạng (network / 네트워크) syscalls ngắn:

```bash
sudo timeout 5s strace -tt -T -f -p <PID> -e trace=network -o /tmp/net.trace
```

Nếu bằng chứng (evidence / 증거) cho thấy `connect()` hoặc `recvfrom()` delay, chuyển investigation sang phụ thuộc (dependency / 의존성)/mạng (network / 네트워크) đường dẫn (path / 경로) thay vì tăng JVM CPU.

## Những hiểu lầm phổ biến

**“strace không thấy ứng dụng (application / 애플리케이션) hàm (function / 함수) nên vô dụng.”** Nó nhìn syscall ranh giới (boundary / 경계), rất mạnh để phân biệt filesystem/mạng (network / 네트워크)/permission/tài nguyên (resource / 자원) issues.

**“perf luôn nhẹ và an toàn.”** Sampling vẫn có overhead; lời gọi (call / 호출) đồ thị (graph / 그래프)/unwind có thể tăng chi phí.

**“Nhiều futex nghĩa kernel bug.”** Thường đó là synchronization hành vi (behavior / 동작) của thời gian chạy (runtime / 런타임)/ứng dụng (application / 애플리케이션).

**“CPU profile giải thích mọi độ trễ (latency / 지연 시간).”** Không. Off-CPU waiting có thể chiếm phần lớn thời gian.

**“eBPF là công cụ phải dùng nếu muốn được coi là cấp cao (senior / 시니어).”** Sai. công cụ (tool / 도구) choice phải dựa trên câu hỏi và thông tin (information / 정보) gain.

## Mô hình tư duy

Quan sát hệ thống có nhiều độ sâu:

```text
application logs        → application nói gì
metrics                 → hệ thống đang thay đổi ra sao
/proc, ss, lsof         → runtime objects đang ở trạng thái nào
strace                  → process đang yêu cầu kernel điều gì
perf/profile            → CPU đang chạy code ở đâu
eBPF/kernel tracing     → event path sâu trong kernel/runtime
```

Chọn tầng (layer / 계층) đủ để trả lời câu hỏi hiện tại, không chọn công cụ (tool / 도구) vì nó “nâng cao”.

Xem thêm: [Production troubleshooting](./production_troubleshooting.md), [Java backend incident playbook](./java_backend_incident_playbook.md), [`/proc` và `/sys`](../00_foundations/proc_sysfs_kernel_interfaces.md).
