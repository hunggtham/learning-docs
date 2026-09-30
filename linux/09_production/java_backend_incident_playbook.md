# Java Backend sự cố (incident / 인시던트) Playbook trên Linux

> **Mạch đọc:** Đọc **Java Backend sự cố (incident / 인시던트) Playbook trên Linux** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Bắt đầu từ thời điểm và phạm vi ảnh hưởng** sang **Bước 1: systemd nghĩ dịch vụ (service / 서비스) đang ở trạng thái nào?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi một Java backend trên Linux gặp sự cố, việc chạy ngẫu nhiên `top`, `tail -f` rồi restart thường chỉ giúp khôi phục tạm thời mà không cho biết nguyên nhân. Một playbook tốt phải nối được ba lớp: **JVM**, **Linux tiến trình (process / 프로세스)/tài nguyên (resource / 자원)**, và **mạng (network / 네트워크)/phụ thuộc (dependency / 의존성)**.

Chương này không thay thế tài liệu JVM chuyên sâu. Mục tiêu là xây một quy trình thực tế để một backend nhà phát triển (developer / 개발자) đang SSH vào máy chủ (server / 서버) có thể đi từ symptom tới bằng chứng (evidence / 증거) có cấu trúc.

## Bắt đầu từ thời điểm và phạm vi ảnh hưởng

Trước mọi command, xác định:

```text
lỗi bắt đầu lúc nào?
bao nhiêu request/user bị ảnh hưởng?
chỉ một instance hay toàn bộ service?
có deployment/config/package change gần đó không?
```

Sau đó ghi lại ngữ cảnh (context / 맥락) của host:

```bash
date '+%F %T %Z %z'
hostname
uptime
```

Timestamp rất quan trọng vì log, metrics và triển khai (deployment / 배포) sự kiện (event / 이벤트) phải được ghép trên cùng timeline.

## Bước 1: systemd nghĩ dịch vụ (service / 서비스) đang ở trạng thái nào?

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
systemctl status app --no-pager
systemctl show app -p MainPID -p User -p Group -p ExecStart -p ActiveEnterTimestamp
journalctl -u app -n 300 --no-pager
```

Ba command này cho biết dịch vụ (service / 서비스) manager nhìn thấy tiến trình (process / 프로세스) nào, chạy bằng định danh (identity / 식별자) nào, command thực tế là gì và log gần nhất ra sao.

Nếu dịch vụ (service / 서비스) `failed`, đừng restart ngay nếu có thể lấy thêm bằng chứng (evidence / 증거) trước.

## Bước 2: xác định đúng JVM

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
pgrep -af 'java.*app'
```

hoặc:

```bash
jps -lv
```

Không dựa vào PID được ghi lại từ sự cố (incident / 인시던트) cũ vì PID có thể được tái sử dụng.

Sau khi xác định PID:

```bash
PID=12345
ps -p "$PID" -o pid,ppid,user,%cpu,%mem,rss,vsz,nlwp,etime,cmd
```

Điều này tạo snapshot ban đầu về CPU, bộ nhớ (memory / 메모리), luồng thực thi (thread / 스레드) count và thời gian chạy.

## Bước 3: tiến trình (process / 프로세스) tồn tại có nghĩa ứng dụng (application / 애플리케이션) healthy không?

Không. Kiểm tra socket:

```bash
sudo ss -lntp | grep ':8080'
```

Sau đó cục bộ (local / 로컬) health:

```bash
curl -fsS -v http://127.0.0.1:8080/health
```

Có bốn tình huống cơ bản:

```text
không process
process nhưng không listener
listener nhưng health fail/hang
local health tốt nhưng external request fail
```

Mỗi trường hợp dẫn tới nhánh điều tra khác.

## Tiến trình (process / 프로세스) biến mất

Nếu JVM không còn tồn tại, cần biết nó tự exit, bị systemd stop, bị OOM kill hay bị tín hiệu (signal / 신호).

```bash
journalctl -u app --since '30 minutes ago'
journalctl -k --since '30 minutes ago' | grep -i -E 'oom|out of memory|killed process|segfault'
```

Nếu thấy OOM killer, ứng dụng (application / 애플리케이션) log có thể chỉ dừng đột ngột mà không có Java exception cuối cùng.

## CPU cao

Trước hết xác nhận CPU high là sustained hay chỉ spike:

```bash
pidstat -p "$PID" 1 10
```

Sau đó xem luồng thực thi (thread / 스레드):

```bash
pidstat -t -p "$PID" 1
```

Lấy luồng thực thi (thread / 스레드) dump:

```bash
jcmd "$PID" Thread.print > /tmp/thread-$(date +%s).txt
```

Một snapshot luồng thực thi (thread / 스레드) dump đôi khi chưa đủ. Nếu sự cố (incident / 인시던트) kéo dài, lấy 3 dump cách nhau vài giây để xem cùng luồng thực thi (thread / 스레드) có tiếp tục chạy cùng ngăn xếp (stack / 스택) hay không.

```bash
for i in 1 2 3; do
  jcmd "$PID" Thread.print > "/tmp/thread-$i.txt"
  sleep 5
done
```

Nếu một luồng thực thi (thread / 스레드) dùng CPU cao liên tục và ngăn xếp (stack / 스택) lặp lại cùng đường đi mã (code path / 코드 경로), hypothesis về hot vòng lặp (loop / 루프)/hot phương thức (method / 메서드) mạnh hơn.

## CPU cao do GC

CPU cao không nhất thiết là nghiệp vụ (business / 비즈니스) mã (code / 코드). JVM có thể dành nhiều thời gian garbage collection.

```bash
jcmd "$PID" GC.heap_info
jstat -gcutil "$PID" 1000 10
```

Công cụ (tool / 도구) availability phụ thuộc JDK. Nếu old generation gần full và full GC lặp lại, cần liên hệ vùng nhớ động (heap / 힙) pressure, allocation tỷ lệ (rate / 비율) và GC logs.

Không tăng `-Xmx` ngay khi chưa biết host/bộ chứa (container / 컨테이너) giới hạn bộ nhớ (memory limit / 메모리 제한); vùng nhớ động (heap / 힙) lớn hơn có thể đẩy tiến trình (process / 프로세스) vào cgroup/host OOM.

## Bộ nhớ (memory / 메모리) tăng

Linux view:

```bash
ps -p "$PID" -o pid,rss,vsz,%mem,etime,cmd
free -h
cat /proc/$PID/status | grep -E 'VmRSS|VmSize|Threads'
```

JVM view:

```bash
jcmd "$PID" GC.heap_info
jcmd "$PID" VM.flags
```

Nếu vùng nhớ động (heap / 힙) ổn nhưng RSS tăng, hãy nghĩ tới direct buffers, metaspace, luồng thực thi (thread / 스레드) stacks, bản địa (native / 네이티브) thư viện (library / 라이브러리) hoặc mapped bộ nhớ (memory / 메모리).

Java tiến trình (process / 프로세스) bộ nhớ (memory / 메모리) không bằng `-Xmx`.

## Nghi bộ nhớ (memory / 메모리) leak

Không kết luận leak từ một snapshot. Cần trend theo thời gian và tải công việc (workload / 워크로드).

Một vùng nhớ động (heap / 힙) histogram có thể cung cấp bằng chứng (evidence / 증거):

```bash
jcmd "$PID" GC.class_histogram > /tmp/histo.txt
```

Vùng nhớ vùng nhớ động (heap / 힙) dump có thể rất lớn và gây I/O/lưu trữ (storage / 저장소) pressure, vì vậy không tạo bừa trên filesystem gần đầy. Trước khi dump:

```bash
df -h /tmp
```

Với môi trường vận hành (production / 운영 환경), vùng nhớ động (heap / 힙) dump procedure cần dự tính pause và disk sức chứa (capacity / 용량).

## Too many open files

Nếu log có:

```text
Too many open files
```

kiểm tra limit:

```bash
cat /proc/$PID/limits | grep -i 'open files'
```

đếm descriptor:

```bash
ls /proc/$PID/fd | wc -l
```

xem loại tài nguyên (resource / 자원):

```bash
sudo lsof -p "$PID" | head -100
```

Nếu count tăng liên tục, có thể là tệp (file / 파일)/socket/tài nguyên (resource / 자원) leak. Tăng limit chỉ kéo dài thời gian trước thất bại (failure / 실패) nếu vòng đời (lifecycle / 생명주기) bug vẫn còn.

## Luồng thực thi (thread / 스레드) count tăng

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
ps -p "$PID" -o pid,nlwp,cmd
```

Nếu luồng thực thi (thread / 스레드) count tăng không giảm, kiểm tra luồng thực thi (thread / 스레드) dump để xem pool nào tạo nhiều threads.

Mỗi luồng thực thi (thread / 스레드) tiêu thụ ngăn xếp (stack / 스택)/bản địa (native / 네이티브) resources; hàng nghìn threads có thể gây bộ nhớ (memory / 메모리) pressure và scheduling overhead ngay cả khi vùng nhớ động (heap / 힙) không lớn.

## Yêu cầu (request / 요청) hang nhưng CPU thấp

CPU thấp không nghĩa khỏe. Threads có thể đang chờ cơ sở dữ liệu (database / 데이터베이스), HTTP downstream, khóa (lock / 잠금) hoặc liên kết (connection / 연결) pool.

Luồng thực thi (thread / 스레드) dump giúp phân biệt:

```text
RUNNABLE nhưng đang socket read
WAITING/TIMED_WAITING ở pool/lock
BLOCKED trên monitor
```

Sau đó nối với Linux mạng (network / 네트워크):

```bash
ss -antp | grep "$PID"
```

và phụ thuộc (dependency / 의존성) kiểm thử (test / 테스트):

```bash
nc -vz db.internal 5432
curl -v https://downstream.example.com/health
```

Không dùng phụ thuộc (dependency / 의존성) kiểm thử (test / 테스트) có side tác động (effect / 효과) nếu endpoint không an toàn.

## Liên kết (connection / 연결) pool exhaustion

Một ứng dụng (application / 애플리케이션) có thể healthy tiến trình (process / 프로세스)/socket nhưng yêu cầu (request / 요청) chờ vì JDBC hoặc HTTP pool hết liên kết (connection / 연결).

JVM metrics/log thường là bằng chứng (evidence / 증거) tốt nhất, nhưng Linux có thể bổ sung bằng số TCP connections:

```bash
ss -antp | grep ':5432' | wc -l
```

Con số này không đồng nghĩa trực tiếp pool kích thước (size / 크기) vì có thể có nhiều tiến trình (process / 프로세스)/states, nhưng nó giúp kiểm tra hypothesis.

## Cơ sở dữ liệu (database / 데이터베이스) chậm

Nếu luồng thực thi (thread / 스레드) dump cho thấy nhiều yêu cầu (request / 요청) chờ JDBC, bước tiếp theo không phải restart JVM ngay. Cần xem DB độ trễ (latency / 지연 시간), khóa (lock / 잠금), liên kết (connection / 연결) count, slow truy vấn (query / 쿼리) và mạng (network / 네트워크) đường dẫn (path / 경로).

Từ app host:

```bash
nc -vz db.internal 5432
```

hoặc cổng (port / 포트) phù hợp. TCP success chỉ chứng minh connect tầng (layer / 계층), không chứng minh truy vấn (query / 쿼리) nhanh.

## Mạng (network / 네트워크) bên ngoài (external / 외부) thất bại (fail / 실패) nhưng localhost tốt

Nếu:

```bash
curl -fsS http://127.0.0.1:8080/health
```

thành công nhưng người dùng (user / 사용자) vẫn lỗi, kiểm tra:

```bash
sudo ss -lntp | grep ':8080'
dig +short api.example.com
curl -v https://api.example.com/health
```

Nếu app bind `127.0.0.1` nhưng proxy kỳ vọng private IP, đó là bind mismatch. Nếu proxy gọi localhost trên cùng host thì bind đó có thể hoàn toàn đúng. Kiến trúc quyết định.

## Disk full và Java

Disk full có thể làm log writer, temp tệp (file / 파일), upload, cơ sở dữ liệu (database / 데이터베이스) cục bộ (local / 로컬) hoặc JVM diagnostic thất bại (fail / 실패).

```bash
df -h
df -i
sudo du -xhd1 /var 2>/dev/null | sort -hr
sudo lsof +L1
```

Deleted log vẫn được JVM giữ open có thể làm `df` đầy nhưng `du` không thấy.

## I/O chậm

Nếu app độ trễ (latency / 지연 시간) tăng nhưng CPU thấp và luồng thực thi (thread / 스레드) dump có tệp (file / 파일) I/O:

```bash
iostat -xz 1 10
pidstat -d -p "$PID" 1
```

Nếu backend dùng mạng (network / 네트워크) filesystem hoặc cloud volume, cục bộ (local / 로컬) thiết bị (device / 장치) metrics có thể chưa đủ; xem mount nguồn (source / 소스):

```bash
findmnt /path/to/data
```

## Tệp (file / 파일)/cấu hình (config / 설정) permission

Nếu dịch vụ (service / 서비스) startup báo `Permission denied`, xác nhận dịch vụ (service / 서비스) người dùng (user / 사용자):

```bash
systemctl show app -p User -p Group
```

rồi đường dẫn (path / 경로):

```bash
namei -l /opt/app/config/application.yml
```

Không `chmod -R 777` để thử. Parent directory traverse, ACL, SELinux/AppArmor hoặc read-only mount cũng có thể là nguyên nhân.

## Chạy tay được nhưng systemd thất bại (fail / 실패)

Đây là trường hợp (case / 사례) rất phổ biến. Interactive shell có môi trường (environment / 환경) khác dịch vụ (service / 서비스).

```bash
systemctl show app -p User -p Group -p WorkingDirectory -p Environment -p ExecStart
systemctl cat app
```

Kiểm tra absolute đường dẫn (path / 경로) của Java:

```bash
command -v java
readlink -f "$(command -v java)"
```

Đưa đường dẫn rõ vào `ExecStart` tốt hơn phụ thuộc đường dẫn (path / 경로) của SSH shell.

## `jcmd` không attach được

Attach có thể phụ thuộc người dùng (user / 사용자), JVM cấu hình (configuration / 구성), không gian tên (namespace / 네임스페이스)/bộ chứa (container / 컨테이너) và permission.

Hãy thử bằng cùng dịch vụ (service / 서비스) người dùng (user / 사용자) khi phù hợp:

```bash
sudo -u appuser jcmd "$PID" VM.version
```

Không đổi quyền sở hữu (ownership / 소유권) `/tmp` hoặc tiến trình (process / 프로세스) files một cách ngẫu nhiên để làm attach hoạt động.

## Containerized Java

Nếu JVM chạy trong bộ chứa (container / 컨테이너), host PID và bộ chứa (container / 컨테이너) PID có thể khác; giới hạn bộ nhớ (memory limit / 메모리 제한) nằm ở cgroup.

Host `free -h` còn nhiều không loại trừ bộ chứa (container / 컨테이너) OOM.

Cần biết command đang chạy ở host không gian tên (namespace / 네임스페이스) hay bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스) trước khi diễn giải PID, localhost, mount hoặc mạng (network / 네트워크).

## Trước restart nên capture gì?

Nếu SLA cho phép vài chục giây thu thập bằng chứng (evidence / 증거):

```bash
date '+%F %T %Z %z'
systemctl status app --no-pager
journalctl -u app -n 300 --no-pager
ps -p "$PID" -o pid,ppid,user,%cpu,%mem,rss,vsz,nlwp,etime,cmd
jcmd "$PID" Thread.print > /tmp/thread-before-restart.txt
jcmd "$PID" GC.heap_info > /tmp/heap-before-restart.txt
ss -antp > /tmp/ss-before-restart.txt
free -h
df -h
```

Không phải sự cố (incident / 인시던트) nào cũng cần tất cả. Chọn bằng chứng (evidence / 증거) theo symptom và tránh command nặng khi máy chủ (server / 서버) đang trọng yếu (critical / 중요).

## Sau restart phải verify gì?

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
systemctl status app --no-pager
sudo ss -lntp | grep ':8080'
curl -fsS http://127.0.0.1:8080/health
journalctl -u app -n 100 --no-pager
```

Nếu có endpoint phiên bản (version / 버전):

```bash
curl -fsS http://127.0.0.1:8080/version
```

để xác minh sản phẩm tạo ra (artifact / 산출물) mong muốn đang chạy.

## Khôi phục (recovery / 복구) khác nguyên nhân gốc (root cause / 근본 원인)

Restart có thể làm luồng thực thi (thread / 스레드) pool, liên kết (connection / 연결) pool, vùng nhớ động (heap / 힙) và sockets trở về trạng thái sạch. Điều đó giải thích vì sao dịch vụ (service / 서비스) “hết lỗi”, nhưng không cho biết cái gì đã tạo trạng thái xấu.

Sau khôi phục (recovery / 복구), dùng bằng chứng (evidence / 증거) đã capture để xác định chuỗi nhân quả (causal chain / 인과 사슬).

## Mô hình tư duy (mental model / 사고 모델)

Một Java dịch vụ (service / 서비스) trên Linux có thể nhìn như:

```text
systemd
  ↓
JVM process
  ├─ Java heap / native memory
  ├─ threads / scheduler
  ├─ file descriptors
  ├─ listening sockets
  └─ outbound dependency sockets
       ↓
Linux kernel
       ↓
CPU / memory / storage / network
```

Sự cố (incident / 인시던트) investigation là tìm tầng (layer / 계층) đầu tiên không còn đáp ứng expectation.

## Những hiểu lầm phổ biến

**“Java tiến trình (process / 프로세스) còn là app còn khỏe.”** tiến trình (process / 프로세스) có thể deadlock, pool exhaustion hoặc chưa listen.

**“CPU thấp nghĩa app không có vấn đề.”** Nhiều lỗi là waiting/blocking.

**“Xmx 4 GB nghĩa JVM chỉ dùng 4 GB RAM.”** bản địa (native / 네이티브)/off-heap/luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택)/metaspace còn nằm ngoài vùng nhớ động (heap / 힙).

**“Restart hết lỗi nghĩa JVM bug.”** Restart reset rất nhiều trạng thái (state / 상태) ở app và OS; cần bằng chứng (evidence / 증거) trước restart.

**“Too many open files chỉ cần tăng ulimit.”** Nếu có descriptor leak, tăng limit chỉ trì hoãn lỗi.

## Kết nối kiến thức

Playbook này kết hợp [Processes và Signals](../04_process/processes_threads_signals_jobs.md), [Memory](../06_resources/memory_virtual_memory.md), [CPU](../06_resources/cpu_scheduling_performance.md), [I/O Performance](../06_resources/io_performance.md), [TCP/HTTP/TLS](../07_networking/tcp_http_tls.md), [systemd](../05_system/systemd_boot_services.md) và [Production Troubleshooting](./production_troubleshooting.md).
