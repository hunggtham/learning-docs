# Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Linux như môi trường thực thi production**. Route đi từ process/thread → filesystem/network namespaces → service manager → signals/resources → container/runtime behavior, để troubleshooting bắt đầu từ cơ chế kernel.

## 1. Vì sao DevOps phải hiểu Linux dù đang dùng bộ chứa (container / 컨테이너)

Bộ chứa (container / 컨테이너) không loại bỏ hệ điều hành; nó thay cách tiến trình (process / 프로세스) nhìn hệ điều hành. Một tải công việc (workload / 워크로드) trong bộ chứa (container / 컨테이너) cuối cùng vẫn được kernel schedule, cấp bộ nhớ (memory / 메모리), xử lý tệp (file / 파일) descriptor, socket, tín hiệu (signal / 신호) và I/O. Vì vậy khi môi trường vận hành (production / 운영 환경) có CPU throttling, OOM kill, tệp (file / 파일) descriptor exhaustion hoặc tiến trình (process / 프로세스) không nhận tín hiệu (signal / 신호) shutdown, chỉ biết `docker ps` hay `kubectl get pods` là chưa đủ.

Chapter này không viết lại Operating các hệ thống (systems / 시스템들). Mục tiêu là nối các lớp trừu tượng (abstraction / 추상화) Linux quan trọng với công việc vận hành. Nền sâu hơn về kernel/syscall xem [canonical OS foundation](../../computer_science/basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md), tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) xem [processes, threads và scheduling](../../computer_science/basic/03_operating_systems/01_processes_threads_and_scheduling.md), filesystem/I/O xem [filesystems, storage và I/O](../../computer_science/basic/03_operating_systems/04_filesystems_storage_and_io.md).

> **Chuyển mạch:** Trong **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **1. Vì sao DevOps phải hiểu Linux dù đang dùng bộ chứa (container / 컨테이너)** xác định đầu vào; **2. tiến trình (process / 프로세스) là đơn vị đầu tiên để suy luận** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. dịch vụ (service / 서비스) manager và supervision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. tiến trình (process / 프로세스) là đơn vị đầu tiên để suy luận

Một dịch vụ (service / 서비스) đang chạy không phải “một ứng dụng” theo nghĩa trừu tượng. Ở mức OS, nó là một hoặc nhiều tiến trình (process / 프로세스) có PID, address không gian (space / 공간), open tệp (file / 파일) descriptor, credential, môi trường (environment / 환경), hiện tại (current / 현재) working directory và set tài nguyên (resource / 자원) limit. Mọi câu hỏi vận hành nên dần quy về các trạng thái (state / 상태) có thể quan sát này.

Khi dịch vụ (service / 서비스) “không chạy”, cần tách ít nhất bốn khả năng. tiến trình (process / 프로세스) chưa được tạo. tiến trình (process / 프로세스) tạo rồi thoát ngay. tiến trình (process / 프로세스) còn sống nhưng không listen. tiến trình (process / 프로세스) listen nhưng đường đi của yêu cầu (request path / 요청 경로) không tới được. Bốn trạng thái này có biểu hiện bên ngoài gần giống nhau nhưng bằng chứng (evidence / 증거) khác nhau.

Ví dụ, một dịch vụ (service / 서비스) Java chạy dưới `systemd` có thể kiểm tra theo chuỗi:

```bash
systemctl status orders.service
journalctl -u orders.service --since "10 min ago"
ps -ef | grep java
ss -lntp
```

Lệnh không phải đáp án; mỗi lệnh kiểm tra một giả thuyết. `systemctl` kiểm tra supervisor trạng thái (state / 상태), `journalctl` kiểm tra vòng đời (lifecycle / 생명주기) bằng chứng (evidence / 증거), `ps` kiểm tra tiến trình (process / 프로세스) existence, `ss` kiểm tra socket/listener.

> **Chuyển mạch:** Ở chặng này của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **2. tiến trình (process / 프로세스) là đơn vị đầu tiên để suy luận** xác định đầu vào; **3. dịch vụ (service / 서비스) manager và supervision** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. tín hiệu (signal / 신호) và graceful shutdown** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. dịch vụ (service / 서비스) manager và supervision

Một tiến trình (process / 프로세스) môi trường vận hành (production / 운영 환경) cần vòng đời (lifecycle / 생명주기) manager. `systemd` hoặc bộ chứa (container / 컨테이너) orchestrator làm nhiều hơn “start chương trình”: chúng định nghĩa khi nào restart, môi trường (environment / 환경) nào được inject, phụ thuộc (dependency / 의존성) nào phải có, log đi đâu và tín hiệu (signal / 신호) nào được gửi khi shutdown.

Nếu ứng dụng (application / 애플리케이션) tự fork, daemonize và giữ PID tệp (file / 파일) trong khi supervisor cũng mong tiến trình (process / 프로세스) chạy foreground, quyền sở hữu (ownership / 소유권) vòng đời (lifecycle / 생명주기) bị chia đôi. môi trường vận hành (production / 운영 환경) practice hiện đại thường để tiến trình (process / 프로세스) chính chạy foreground và để supervisor quản restart, health và shutdown.

Điều cần hiểu là parent/child quyền sở hữu (ownership / 소유권). Nếu supervisor nghĩ tiến trình (process / 프로세스) đã chết trong khi child vẫn còn, có thể xuất hiện orphan hoặc duplicated dịch vụ (service / 서비스). Nếu tiến trình (process / 프로세스) PID 1 trong bộ chứa (container / 컨테이너) không forward/reap tín hiệu (signal / 신호) đúng, graceful shutdown và zombie handling có thể hỏng. Đây là lý do “tiến trình (process / 프로세스) mô hình (model / 모델)” quan trọng hơn câu lệnh start.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **4. tín hiệu (signal / 신호) và graceful shutdown** tiếp nhận điểm tựa từ **3. dịch vụ (service / 서비스) manager và supervision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. tệp (file / 파일) descriptor và socket là tài nguyên hữu hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. tín hiệu (signal / 신호) và graceful shutdown

Khi deploy phiên bản mới, orchestrator thường không “tắt điện” ngay. Nó yêu cầu tải công việc (workload / 워크로드) dừng bằng tín hiệu (signal / 신호), cho một khoảng grace period, rồi mới force kill nếu tiến trình (process / 프로세스) không thoát. ứng dụng (application / 애플리케이션) môi trường vận hành (production / 운영 환경) phải coi shutdown là một giao thức (protocol / 프로토콜).

Một chuỗi (sequence / 시퀀스) tốt thường là: ngừng nhận yêu cầu (request / 요청) mới, cho bộ cân bằng tải (load balancer / 로드 밸런서)/endpoints cập nhật, hoàn tất hoặc hủy yêu cầu (request / 요청) đang xử lý theo deadline, flush trạng thái (state / 상태)/log cần thiết, đóng liên kết (connection / 연결) pool và thoát. Nếu ứng dụng (application / 애플리케이션) bắt tín hiệu (signal / 신호) nhưng mất 90 giây trong khi grace period là 30 giây, cuối cùng vẫn bị kill giữa giao dịch (transaction / 트랜잭션).

Điểm cấp cao (senior / 시니어) cần nhớ: “graceful” phải được chứng minh bằng traffic hành vi (behavior / 동작) chứ không phải chỉ có shutdown hook trong mã (code / 코드).

> **Chuyển mạch:** Trong **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **5. tệp (file / 파일) descriptor và socket là tài nguyên hữu hạn** tiếp nhận điểm tựa từ **4. tín hiệu (signal / 신호) và graceful shutdown** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. bộ nhớ (memory / 메모리): RSS không phải toàn bộ câu chuyện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. tệp (file / 파일) descriptor và socket là tài nguyên hữu hạn

Linux biểu diễn nhiều I/O tài nguyên (resource / 자원) bằng tệp (file / 파일) descriptor (FD). Socket, tệp (file / 파일), pipe và nhiều kernel đối tượng (object / 객체) đều tiêu tốn FD. Một dịch vụ (service / 서비스) leak liên kết (connection / 연결) có thể vẫn còn CPU và bộ nhớ (memory / 메모리) nhưng không mở thêm socket/tệp (file / 파일) được.

`ulimit -n` cho biết giới hạn ở shell hiện tại nhưng dịch vụ (service / 서비스) có thể chạy dưới limit khác do `systemd`, bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) hoặc chính sách (policy / 정책). Khi thấy lỗi “too many open files”, đừng chỉ tăng limit. Trước hết phải hỏi số FD tăng vì tải công việc (workload / 워크로드) hợp lệ hay leak; loại FD nào đang chiếm; liên kết (connection / 연결) pool có close đúng không; downstream độ trễ (latency / 지연 시간) có làm socket sống lâu bất thường không.

Có thể kiểm tra theo PID:

```bash
ls /proc/<pid>/fd | wc -l
lsof -p <pid>
```

`/proc` là nguồn bằng chứng (evidence / 증거) mạnh vì nó cho thấy kernel đang nhìn tiến trình (process / 프로세스) như thế nào.

> **Chuyển mạch:** Ở chặng này của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **6. bộ nhớ (memory / 메모리): RSS không phải toàn bộ câu chuyện** tiếp nhận điểm tựa từ **5. tệp (file / 파일) descriptor và socket là tài nguyên hữu hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. CPU usage khác CPU entitlement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. bộ nhớ (memory / 메모리): RSS không phải toàn bộ câu chuyện

Môi trường vận hành (production / 운영 환경) thường hiển thị một số “bộ nhớ (memory / 메모리) usage”, nhưng số đó có thể đại diện RSS, working set, cgroup usage hoặc chỉ số (metric / 지표) thời gian chạy (runtime / 런타임). Page bộ nhớ đệm (cache / 캐시), mapped tệp (file / 파일), vùng nhớ động (heap / 힙) và bản địa (native / 네이티브) allocation có ngữ nghĩa (semantics / 의미론) khác nhau.

Một dịch vụ (service / 서비스) có thể bị OOM dù host còn bộ nhớ (memory / 메모리) nếu cgroup limit đã chạm. Ngược lại, host có bộ nhớ (memory / 메모리) pressure dù từng bộ chứa (container / 컨테이너) chưa chạm limit. Kernel reclaim, page bộ nhớ đệm (cache / 캐시) và bộ nhớ (memory / 메모리) pressure được đào sâu tại [memory pressure, reclaim và page faults](../../computer_science/03_operating_systems/advanced/02_page_faults_reclaim_dirty_pages_and_memory_pressure.md).

Về vận hành, hãy tách ba câu hỏi: ứng dụng (application / 애플리케이션) đang giữ bộ nhớ (memory / 메모리) nào; bộ chứa (container / 컨테이너)/cgroup đang bị giới hạn thế nào; host/nút (node / 노드) đang chịu pressure ra sao. Nếu chỉ nhìn một dashboard ứng dụng (application / 애플리케이션) vùng nhớ động (heap / 힙), bạn có thể bỏ sót bản địa (native / 네이티브) bộ nhớ (memory / 메모리) hoặc kernel pressure.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **7. CPU usage khác CPU entitlement** tiếp nhận điểm tựa từ **6. bộ nhớ (memory / 메모리): RSS không phải toàn bộ câu chuyện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Filesystem và “disk full”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. CPU usage khác CPU entitlement

`100% CPU` chỉ có nghĩa khi biết đơn vị đo. Trên host nhiều cốt lõi (core / 핵심), một tiến trình (process / 프로세스) một-thread có thể dùng đầy một cốt lõi (core / 핵심) nhưng chỉ chiếm phần nhỏ tổng host. Trong bộ chứa (container / 컨테이너), CPU yêu cầu (request / 요청)/limit có thể thêm một tầng entitlement. Khi tải công việc (workload / 워크로드) bị CFS throttling, độ trễ (latency / 지연 시간) có thể tăng dù nút (node / 노드) chưa “100% CPU”.

Do đó lập luận (reasoning / 추론) đúng là: demand bao nhiêu, allocation/limit bao nhiêu, scheduler cho chạy thực tế bao nhiêu, hàng đợi (queue / 큐)/run thời gian (time / 시간) tăng ra sao. Nền scheduler xem [scheduler internals](../../computer_science/03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md).

> **Chuyển mạch:** Trong **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **8. Filesystem và “disk full”** tiếp nhận điểm tựa từ **7. CPU usage khác CPU entitlement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. bằng chứng (evidence / 증거) ladder cho Linux sự cố (incident / 인시던트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Filesystem và “disk full”

“Disk full” có thể là hết khối (block / 블록), hết inode, filesystem read-only sau lỗi, quota bị chạm hoặc tầng (layer / 계층) writable của bộ chứa (container / 컨테이너) đầy. `df -h` chỉ trả lời một phần. `df -i` kiểm tra inode; `du` giúp tìm cây (tree / 트리) sử dụng dung lượng nhưng có thể không thấy tệp (file / 파일) đã xóa mà tiến trình (process / 프로세스) còn giữ open FD.

Một tình huống điển hình là log tệp (file / 파일) lớn bị `rm`, nhưng tiến trình (process / 프로세스) vẫn giữ FD. Tên tệp (file / 파일) biến mất khỏi directory nhưng khối (block / 블록) chưa được giải phóng cho tới khi FD đóng. `lsof +L1` có thể lộ trường hợp này. Đây là ví dụ rõ cho việc mô hình tư duy (mental model / 사고 모델) filesystem quan trọng hơn thao tác xóa tệp (file / 파일).

> **Chuyển mạch:** Ở chặng này của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **8. Filesystem và “disk full”** nêu điều cần giải thích; **9. bằng chứng (evidence / 증거) ladder cho Linux sự cố (incident / 인시던트)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. môi trường vận hành (production / 운영 환경) bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. bằng chứng (evidence / 증거) ladder cho Linux sự cố (incident / 인시던트)

Khi một tải công việc (workload / 워크로드) lỗi, nên đi từ bằng chứng (evidence / 증거) ít phá hoại đến sâu hơn. Trước hết xác định symptom và thời gian (time / 시간) cửa sổ (window / 윈도우). Sau đó kiểm tra tiến trình (process / 프로세스)/dịch vụ (service / 서비스) trạng thái (state / 상태), logs/events, listener/socket, tài nguyên (resource / 자원) pressure, phụ thuộc (dependency / 의존성) connectivity. Chỉ khi các lớp này không đủ mới đi sâu vào `/proc`, syscall tracing, packet capture hoặc kernel bằng chứng (evidence / 증거).

Đừng restart quá sớm nếu chưa thu bằng chứng (evidence / 증거) tối thiểu. Restart có thể phục hồi dịch vụ (service / 서비스) nhưng đồng thời xóa trạng thái (state / 상태) quý giá để tìm nguyên nhân gốc (root cause / 근본 원인). Trong sự cố (incident / 인시던트) có người dùng (user / 사용자) impact lớn, khôi phục (recovery / 복구) vẫn ưu tiên; nhưng nên có quy ước ai capture bằng chứng (evidence / 증거) nào trước khi restart khi thời gian cho phép.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **9. bằng chứng (evidence / 증거) ladder cho Linux sự cố (incident / 인시던트)** nêu điều cần giải thích; **10. môi trường vận hành (production / 운영 환경) bất biến (invariant / 불변식)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. tải (load / 로드) average không đồng nghĩa CPU utilization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. môi trường vận hành (production / 운영 환경) bất biến (invariant / 불변식)

Một dịch vụ (service / 서비스) vận hành tốt cần có vòng đời (lifecycle / 생명주기) rõ ràng: tiến trình (process / 프로세스) foreground, supervisor quyền sở hữu (ownership / 소유권), tín hiệu (signal / 신호) handling, tài nguyên (resource / 자원) ranh giới (boundary / 경계), log/telemetry đường dẫn (path / 경로) và health ngữ nghĩa (semantics / 의미론) nhất quán. bộ chứa (container / 컨테이너) hay VM chỉ thay packaging và isolation ranh giới (boundary / 경계); bất biến (invariant / 불변식) này vẫn còn.

> **Chuyển mạch:** Trong **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **11. tải (load / 로드) average không đồng nghĩa CPU utilization** tiếp nhận điểm tựa từ **10. môi trường vận hành (production / 운영 환경) bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Pressure Stall thông tin (information / 정보) giúp đo thời gian tải công việc (workload / 워크로드) bị thiếu tài nguyên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. tải (load / 로드) average không đồng nghĩa CPU utilization

`load average` trên Linux gần với số tác vụ (task / 작업) đang muốn chạy hoặc đang ở một số trạng thái chờ không ngắt được, chứ không phải phần trăm CPU. Vì vậy tải (load / 로드) cao có thể đến từ CPU run hàng đợi (queue / 큐) lớn, nhưng cũng có thể đến từ I/O hoặc kernel wait. Một máy 16 CPU với tải (load / 로드) 8 có ý nghĩa khác máy 2 CPU với tải (load / 로드) 8.

Khi độ trễ (latency / 지연 시간) tăng cùng tải (load / 로드) average, đừng kết luận “thiếu CPU” trước khi xem run hàng đợi (queue / 큐), CPU utilization, I/O wait và pressure. Đây là ví dụ điển hình của việc một chỉ số (metric / 지표) tổng hợp chỉ là đầu mối, không phải diagnosis.

> **Chuyển mạch:** Ở chặng này của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **12. Pressure Stall thông tin (information / 정보) giúp đo thời gian tải công việc (workload / 워크로드) bị thiếu tài nguyên** tiếp nhận điểm tựa từ **11. tải (load / 로드) average không đồng nghĩa CPU utilization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Cgroup v2: tài nguyên (resource / 자원) điều khiển (control / 제어) là hierarchy chứ không chỉ một con số limit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Pressure Stall thông tin (information / 정보) giúp đo thời gian tải công việc (workload / 워크로드) bị thiếu tài nguyên

Pressure Stall thông tin (information / 정보) (PSI) cho biết trong một khoảng thời gian, tác vụ (task / 작업) đã phải chờ vì thiếu CPU, bộ nhớ (memory / 메모리) hoặc I/O bao lâu. Đây là góc nhìn khác utilization. CPU có thể chưa 100% trung bình nhưng một tải công việc (workload / 워크로드) latency-sensitive vẫn chịu pressure do cgroup quota hoặc run hàng đợi (queue / 큐). bộ nhớ (memory / 메모리) usage có thể chưa chạm limit nhưng reclaim liên tục làm tác vụ (task / 작업) stall.

Trong sự cố (incident / 인시던트), PSI hữu ích vì nó hỏi trực tiếp: “tải công việc (workload / 워크로드) có đang bị trì hoãn bởi tài nguyên (resource / 자원) contention không?”. Sau đó mới đi sâu xem contention đến từ cgroup ranh giới (boundary / 경계), nút (node / 노드) overcommit, reclaim, lưu trữ (storage / 저장소) độ trễ (latency / 지연 시간) hay tải công việc (workload / 워크로드) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **12. Pressure Stall thông tin (information / 정보) giúp đo thời gian tải công việc (workload / 워크로드) bị thiếu tài nguyên** đã nêu tiêu chí phân biệt, còn **13. Cgroup v2: tài nguyên (resource / 자원) điều khiển (control / 제어) là hierarchy chứ không chỉ một con số limit** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. OOM phải xác định phạm vi (scope / 범위): tiến trình (process / 프로세스), cgroup hay host** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Cgroup v2: tài nguyên (resource / 자원) điều khiển (control / 제어) là hierarchy chứ không chỉ một con số limit

Trong hệ thống dùng cgroup v2, CPU, bộ nhớ (memory / 메모리) và nhiều tài nguyên (resource / 자원) được quản theo một hierarchy thống nhất. tải công việc (workload / 워크로드) có thể chịu ràng buộc (constraint / 제약조건) từ chính cgroup của nó và từ ancestor. Vì vậy “bộ chứa (container / 컨테이너) limit là X” chưa đủ nếu nút (node / 노드) hoặc parent slice đang có chính sách (policy / 정책) khác.

Bộ nhớ (memory / 메모리) điều khiển (control / 제어) cũng không chỉ có hard limit. Các ngưỡng như `memory.high` có thể tạo reclaim/throttling pressure trước khi `memory.max` dẫn tới OOM. Về operational lập luận (reasoning / 추론), điều quan trọng là phân biệt **pressure** với **hard thất bại (failure / 실패)**: dịch vụ (service / 서비스) có thể chậm nghiêm trọng trước khi bị kill.

> **Chuyển mạch:** Trong **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **13. Cgroup v2: tài nguyên (resource / 자원) điều khiển (control / 제어) là hierarchy chứ không chỉ một con số limit** đã nêu tiêu chí phân biệt, còn **14. OOM phải xác định phạm vi (scope / 범위): tiến trình (process / 프로세스), cgroup hay host** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. cấp cao (senior / 시니어) walkthrough: độ trễ (latency / 지연 시간) tăng nhưng CPU dashboard chỉ 45%** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. OOM phải xác định phạm vi (scope / 범위): tiến trình (process / 프로세스), cgroup hay host

Một dòng log “OOM” chưa nói rõ miền lỗi (failure domain / 장애 도메인). Có trường hợp tiến trình (process / 프로세스)/thời gian chạy (runtime / 런타임) tự ném lỗi vì vùng nhớ động (heap / 힙) limit. Có trường hợp cgroup OOM kill vì tải công việc (workload / 워크로드) vượt bộ nhớ (memory / 메모리) ranh giới (boundary / 경계). Có trường hợp host chịu toàn cục (global / 전역) bộ nhớ (memory / 메모리) pressure và kernel chọn victim.

Ba trường hợp cần bằng chứng (evidence / 증거) khác nhau. thời gian chạy (runtime / 런타임) vùng nhớ động (heap / 힙) metrics trả lời câu hỏi bên trong tiến trình (process / 프로세스). Cgroup events trả lời tải công việc (workload / 워크로드) có chạm ranh giới (boundary / 경계) không. Kernel log/nút (node / 노드) pressure trả lời host có thiếu bộ nhớ (memory / 메모리) toàn cục không. Chỉ tăng vùng nhớ động (heap / 힙) hoặc tăng pod limit mà không xác định phạm vi (scope / 범위) có thể chuyển thất bại (failure / 실패) sang tầng khác.

> **Chuyển mạch:** Ở chặng này của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **14. OOM phải xác định phạm vi (scope / 범위): tiến trình (process / 프로세스), cgroup hay host** xác định đầu vào; **15. cấp cao (senior / 시니어) walkthrough: độ trễ (latency / 지연 시간) tăng nhưng CPU dashboard chỉ 45%** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. Dirty page và writeback có thể tạo độ trễ (latency / 지연 시간) trước khi disk “đầy”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. cấp cao (senior / 시니어) walkthrough: độ trễ (latency / 지연 시간) tăng nhưng CPU dashboard chỉ 45%

Giả sử `orders-api` p99 tăng từ 200 ms lên 2 giây, nút (node / 노드) CPU trung bình 45%. Kết luận “CPU không phải vấn đề” là quá sớm. Hãy kiểm tra CPU quota/throttling của tải công việc (workload / 워크로드), run hàng đợi (queue / 큐)/PSI, số luồng thực thi (thread / 스레드) runnable, GC và phụ thuộc (dependency / 의존성) wait.

Nếu throttling tăng đúng lúc độ trễ (latency / 지연 시간) tăng, tải công việc (workload / 워크로드) có thể đang đòi nhiều CPU hơn entitlement dù host còn idle sức chứa (capacity / 용량). Nếu không throttling nhưng PSI I/O tăng, nguyên nhân có thể là lưu trữ (storage / 저장소). Nếu cả hai bình thường nhưng luồng thực thi (thread / 스레드) dump cho thấy nhiều luồng thực thi (thread / 스레드) chờ liên kết (connection / 연결) pool, bottleneck chuyển sang downstream.

Cách lập luận (reasoning / 추론) này giữ nguyên nguyên tắc của chapter: một chỉ số (metric / 지표) ở một tầng (layer / 계층) không phủ định pressure ở tầng (layer / 계층) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **16. Dirty page và writeback có thể tạo độ trễ (latency / 지연 시간) trước khi disk “đầy”** tiếp nhận điểm tựa từ **15. cấp cao (senior / 시니어) walkthrough: độ trễ (latency / 지연 시간) tăng nhưng CPU dashboard chỉ 45%** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Listen socket có hàng đợi (queue / 큐) trước khi ứng dụng (application / 애플리케이션) accept() liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Dirty page và writeback có thể tạo độ trễ (latency / 지연 시간) trước khi disk “đầy”

Khi tiến trình (process / 프로세스) ghi tệp (file / 파일), nhiều ghi (write / 쓰기) không lập tức đi thẳng xuống lưu trữ (storage / 저장소); dữ liệu có thể đi vào page bộ nhớ đệm (cache / 캐시) rồi kernel flush dần xuống thiết bị. Điều này làm ghi (write / 쓰기) bình thường nhìn rất nhanh, nhưng nếu tốc độ dirty dữ liệu (data / 데이터) cao hơn tốc độ writeback lâu đủ, kernel phải throttle writer hoặc ứng dụng (application / 애플리케이션) gặp burst độ trễ (latency / 지연 시간) khi flush/fsync.

Vì vậy một dịch vụ (service / 서비스) ghi log, temporary tệp (file / 파일) hoặc cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) có thể xuất hiện p99 độ trễ (latency / 지연 시간) tăng trong khi disk usage vẫn còn nhiều. bằng chứng (evidence / 증거) cần nối ứng dụng (application / 애플리케이션) ghi (write / 쓰기) độ trễ (latency / 지연 시간), I/O PSI, thiết bị (device / 장치) độ trễ (latency / 지연 시간)/hàng đợi (queue / 큐) và dirty/writeback hành vi (behavior / 동작). “Disk chưa đầy” chỉ loại trừ sức chứa (capacity / 용량) theo dung lượng, không loại trừ saturation theo thông lượng (throughput / 처리량)/độ trễ (latency / 지연 시간).

Operational lesson là lưu trữ (storage / 저장소) có ít nhất hai loại headroom: còn bao nhiêu bytes và còn bao nhiêu dịch vụ (service / 서비스) tỷ lệ (rate / 비율) cho I/O. Hai thứ không thay thế nhau.

> **Chuyển mạch:** Trong **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, sau nội dung của **16. Dirty page và writeback có thể tạo độ trễ (latency / 지연 시간) trước khi disk “đầy”**, **17. Listen socket có hàng đợi (queue / 큐) trước khi ứng dụng (application / 애플리케이션) accept() liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **18. tài nguyên (resource / 자원) limit có nhiều tầng và effective limit là tầng chặt nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Listen socket có hàng đợi (queue / 큐) trước khi ứng dụng (application / 애플리케이션) `accept()` liên kết (connection / 연결)

Một tiến trình (process / 프로세스) có thể đang `LISTEN` nhưng vẫn không theo kịp liên kết (connection / 연결) mới. Kernel giữ trạng thái (state / 상태) cho liên kết (connection / 연결) setup và hàng đợi liên kết (connection / 연결) đã hoàn thành chờ ứng dụng (application / 애플리케이션) `accept()`. Nếu ứng dụng (application / 애플리케이션) vòng lặp sự kiện (event loop / 이벤트 루프)/luồng thực thi (thread / 스레드) pool bị stall hoặc accept tỷ lệ (rate / 비율) thấp hơn arrival tỷ lệ (rate / 비율), hàng đợi (queue / 큐) có thể đầy và máy khách (client / 클라이언트) thấy hết thời gian chờ (timeout / 타임아웃)/reset dù tiến trình (process / 프로세스) vẫn sống và cổng (port / 포트) vẫn mở.

Do đó `ss -lntp` xác nhận listener tồn tại nhưng chưa chứng minh listener đang phục vụ đủ nhanh. Khi có connect thất bại (failure / 실패) dưới tải (load / 로드), cần nối socket backlog/accept hành vi (behavior / 동작) với ứng dụng (application / 애플리케이션) luồng thực thi (thread / 스레드) trạng thái (state / 상태), CPU throttling và event-loop độ trễ (latency / 지연 시간).

Đây là cùng mô hình tư duy (mental model / 사고 모델) queueing: kernel hàng đợi (queue / 큐) hấp thụ burst, nhưng hàng đợi (queue / 큐) không tạo thêm dịch vụ (service / 서비스) sức chứa (capacity / 용량). Nếu producer liên kết (connection / 연결) đến nhanh hơn ứng dụng (application / 애플리케이션) nhận lâu đủ, thất bại (failure / 실패) cuối cùng vẫn xuất hiện.

> **Chuyển mạch:** Ở chặng này của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **17. Listen socket có hàng đợi (queue / 큐) trước khi ứng dụng (application / 애플리케이션) accept() liên kết (connection / 연결)** đã nêu tiêu chí phân biệt, còn **18. tài nguyên (resource / 자원) limit có nhiều tầng và effective limit là tầng chặt nhất** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **19. Clock là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경) dù không tiêu CPU đáng kể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. tài nguyên (resource / 자원) limit có nhiều tầng và effective limit là tầng chặt nhất

Một tiến trình (process / 프로세스) có thể chịu `RLIMIT_NOFILE`, `systemd` đơn vị (unit / 단위) limit, cgroup ranh giới (boundary / 경계), bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) setting và node-level pressure cùng lúc. Operator thường nhìn một tầng rồi nghĩ đó là “limit thực”. Thực tế effective hành vi (behavior / 동작) đến từ ràng buộc (constraint / 제약조건) chặt nhất trên đường thực thi.

Ví dụ shell tương tác báo `ulimit -n` rất cao nhưng dịch vụ (service / 서비스) đơn vị (unit / 단위) có `LimitNOFILE` thấp hơn; hoặc bộ chứa (container / 컨테이너) giới hạn bộ nhớ (memory limit / 메모리 제한) 4 GiB nhưng parent cgroup của cả tải công việc (workload / 워크로드) lớp (class / 클래스) đang bị pressure. Vì vậy bằng chứng (evidence / 증거) phải lấy từ ngữ cảnh (context / 맥락) của chính tiến trình (process / 프로세스)/dịch vụ (service / 서비스), không lấy từ shell khác rồi suy diễn.

Mô hình tư duy (mental model / 사고 모델) này áp dụng rộng hơn Linux: môi trường vận hành (production / 운영 환경) lớp trừu tượng (abstraction / 추상화) thường là composition của nhiều chính sách (policy / 정책); giá trị hiển thị ở một tầng (layer / 계층) chỉ có nghĩa trong ranh giới (boundary / 경계) đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **18. tài nguyên (resource / 자원) limit có nhiều tầng và effective limit là tầng chặt nhất** đã nêu tiêu chí phân biệt, còn **19. Clock là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경) dù không tiêu CPU đáng kể** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **20. cấp cao (senior / 시니어) walkthrough: API hết thời gian chờ (timeout / 타임아웃) tăng cùng log burst nhưng CPU và DB đều bình thường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Clock là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경) dù không tiêu CPU đáng kể

Nhiều giao thức (protocol / 프로토콜) và hệ thống phụ thuộc thời gian: TLS certificate validity, đơn vị từ (token / 토큰) expiry, phân tán (distributed / 분산) dấu vết (trace / 추적) thứ tự (ordering / 순서), lease, cron/scheduler, bộ nhớ đệm (cache / 캐시) TTL và log correlation. Nếu clock skew lớn, dịch vụ (service / 서비스) có thể thất bại (fail / 실패) authentication hoặc tạo timeline điều tra sai dù CPU/bộ nhớ (memory / 메모리)/mạng (network / 네트워크) đều khỏe.

Không nên dùng wall clock như một nguồn thứ tự (ordering / 순서) tuyệt đối cho phân tán (distributed / 분산) sự kiện (event / 이벤트). Trong sự cố (incident / 인시던트), timestamp giữa hai host lệch nhau có thể làm chuỗi nhân quả (causal chain / 인과 사슬) nhìn đảo ngược. NTP/time-sync health vì vậy là operational phụ thuộc (dependency / 의존성); còn thứ tự (ordering / 순서)/causality sâu hơn thuộc phân tán (distributed / 분산) các hệ thống (systems / 시스템들) chuẩn gốc (canonical / 정본) docs.

Khi thất bại (failure / 실패) gắn với “đơn vị từ (token / 토큰) chưa có hiệu lực”, “certificate chưa hợp lệ” hoặc sự kiện (event / 이벤트) dường như xảy ra trước cause, hãy kiểm tra clock/source-time giả định (assumption / 가정) trước khi invent một race điều kiện (condition / 조건) phức tạp.

> **Chuyển mạch:** Trong **Linux như môi trường thực thi môi trường vận hành (production / 운영 환경)**, **20. cấp cao (senior / 시니어) walkthrough: API hết thời gian chờ (timeout / 타임아웃) tăng cùng log burst nhưng CPU và DB đều bình thường** tiếp nhận điểm tựa từ **19. Clock là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경) dù không tiêu CPU đáng kể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 20. cấp cao (senior / 시니어) walkthrough: API hết thời gian chờ (timeout / 타임아웃) tăng cùng log burst nhưng CPU và DB đều bình thường

Giả sử sau khi bật gỡ lỗi (debug / 디버그) log, yêu cầu (request / 요청) p99 tăng mạnh. CPU chỉ 35%, DB độ trễ (latency / 지연 시간) không đổi, mạng (network / 네트워크) bình thường. nút (node / 노드) cho thấy I/O PSI tăng và thiết bị (device / 장치) ghi (write / 쓰기) độ trễ (latency / 지연 시간) xuất hiện burst; ứng dụng (application / 애플리케이션) luồng thực thi (thread / 스레드) dump có nhiều luồng thực thi (thread / 스레드) chờ flush/logging đường dẫn (path / 경로).

Chuỗi nhân quả (causal chain / 인과 사슬) hợp lý là log volume làm dirty dữ liệu (data / 데이터) tăng, writeback/lưu trữ (storage / 저장소) bắt đầu stall writer, yêu cầu (request / 요청) luồng thực thi (thread / 스레드) bị giữ lâu hơn, tính đồng thời (concurrency / 동시성) tăng và tail độ trễ (latency / 지연 시간) khuếch đại. Tăng CPU replica có thể không giúp nếu tất cả replica cùng ghi vào bottleneck lưu trữ (storage / 저장소)/log đường dẫn (path / 경로).

Mitigation có thể giảm log verbosity, chuyển logging sang buffered/asynchronous đường dẫn (path / 경로) có backpressure hợp lý hoặc tăng I/O sức chứa (capacity / 용량). Long-term fix là coi logging chuỗi xử lý (pipeline / 파이프라인) như phụ thuộc (dependency / 의존성) có ngân sách (budget / 예산), không phải side tác động (effect / 효과) “miễn phí” của ứng dụng (application / 애플리케이션).

> **Bàn giao:** Sau **20. cấp cao (senior / 시니어) walkthrough: API hết thời gian chờ (timeout / 타임아웃) tăng cùng log burst nhưng CPU và DB đều bình thường**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
