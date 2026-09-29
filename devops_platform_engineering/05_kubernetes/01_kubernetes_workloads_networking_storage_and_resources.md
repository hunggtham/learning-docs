# Kubernetes tải công việc (workload / 워크로드), networking, lưu trữ (storage / 저장소), scheduling và tài nguyên (resource / 자원) hành vi (behavior / 동작)

> **Mạch đọc:** Đọc **Kubernetes tải công việc (workload / 워크로드), networking, lưu trữ (storage / 저장소), scheduling và tài nguyên (resource / 자원) hành vi (behavior / 동작)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Chọn lớp trừu tượng tải công việc (workload abstraction / 워크로드 추상화) theo định danh (identity / 식별자) và vòng đời (lifecycle / 생명주기)** sang **2. Pod là đơn vị lập lịch (scheduling unit / 스케줄링 단위), không phải durable machine**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. Chọn lớp trừu tượng tải công việc (workload abstraction / 워크로드 추상화) theo định danh (identity / 식별자) và vòng đời (lifecycle / 생명주기)

`Deployment` phù hợp phần lớn stateless replica có thể thay thế. `StatefulSet` thêm stable định danh (identity / 식별자)/thứ tự (order / 순서) và thường đi với persistent volume. `DaemonSet` bảo đảm tải công việc (workload / 워크로드) chạy trên tập nút (node / 노드) phù hợp. `Job` mô tả công việc cần hoàn thành; `CronJob` tạo Job theo lịch.

Đừng chọn kind theo tên quen thuộc. Hãy hỏi instance định danh (identity / 식별자) có quan trọng không, công việc chạy liên tục hay hoàn thành, cần một bản sao trên mỗi nút (node / 노드) hay replica tùy ý, lưu trữ (storage / 저장소) có gắn với định danh (identity / 식별자) không.

## 2. Pod là đơn vị lập lịch (scheduling unit / 스케줄링 단위), không phải durable machine

Pod là đơn vị được scheduler đặt lên nút (node / 노드). bộ chứa (container / 컨테이너) trong cùng Pod chia mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) và có thể chia volume. Pod có IP riêng nhưng định danh (identity / 식별자) của Pod thường ephemeral. Khi triển khai (deployment / 배포) thay Pod, IP mới có thể xuất hiện.

Vì vậy ứng dụng (application / 애플리케이션) không nên lưu danh sách Pod IP cứng. khám phá dịch vụ (service discovery / 서비스 디스커버리) và stable lớp trừu tượng dịch vụ (service abstraction / 서비스 추상화) tồn tại để decouple bên tiêu thụ (consumer / 소비자) khỏi instance vòng đời (lifecycle / 생명주기).

## 3. dịch vụ (service / 서비스) và endpoint

`Service` cung cấp logical endpoint cho một tập backend được chọn qua selector hoặc endpoint cơ chế (mechanism / 메커니즘). Nó không “chứa traffic”; mặt phẳng dữ liệu (data plane / 데이터 플레인) như kube-proxy/eBPF hiện thực (implementation / 구현) thực hiện forwarding.

Troubleshooting cần tách đối tượng (object / 객체) đúng với packet đường dẫn (path / 경로). dịch vụ (service / 서비스) đối tượng (object / 객체) đúng nhưng endpoint rỗng thì selector/readiness có vấn đề. Endpoint đúng nhưng traffic thất bại (fail / 실패) thì xem cổng đích (target port / 대상 포트), chính sách mạng (network policy / 네트워크 정책), mặt phẳng dữ liệu (data plane / 데이터 플레인) hoặc ứng dụng (application / 애플리케이션) listener.

Request-path mô hình tư duy (mental model / 사고 모델) đã có tại [DNS, TLS và request path](../01_runtime_foundations/01_network_dns_tls_and_request_path.md).

## 4. Ingress/Gateway và north-south traffic

Traffic từ ngoài cluster thường qua bộ cân bằng tải (load balancer / 로드 밸런서) rồi ingress/gateway controller. tài nguyên (resource / 자원) API mô tả routing intent; controller phải biến intent thành data-plane cấu hình (configuration / 구성).

Nếu sửa Ingress mà tuyến (route / 경로) không đổi, kiểm tra controller đã observe generation mới chưa, cấu hình (config / 설정) reconcile có lỗi không và bên ngoài (external / 외부) bộ cân bằng tải (load balancer / 로드 밸런서)/DNS đã hội tụ chưa. Đây vẫn là control-loop debugging.

## 5. ConfigMap và Secret không giải quyết toàn bộ cấu hình (config / 설정) vòng đời (lifecycle / 생명주기)

`ConfigMap` và `Secret` đưa cấu hình (configuration / 구성) vào tải công việc (workload / 워크로드), nhưng cách ứng dụng (application / 애플리케이션) nhận cập nhật (update / 업데이트) quyết định hành vi (behavior / 동작). môi trường (environment / 환경) variable thường chỉ có giá trị khi tiến trình (process / 프로세스) start. Volume-mounted cấu hình (config / 설정) có thể cập nhật tệp (file / 파일) nhưng ứng dụng (application / 애플리케이션) có thể không reload.

Vì vậy “Kubernetes đã cập nhật (update / 업데이트) Secret” không đồng nghĩa ứng dụng (application / 애플리케이션) đang dùng secret mới. Rotation phải có end-to-end vòng đời (lifecycle / 생명주기): issue → distribute → reload/restart → verify → revoke old.

Secrets ở mức cryptography/key vòng đời (lifecycle / 생명주기) xem [canonical secrets, KMS, HSM và rotation](../../computer_science/07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

## 6. Persistent Volume là đặc tả hợp đồng (contract / 계약) lưu trữ (storage / 저장소)

PersistentVolume/PersistentVolumeClaim tách nhu cầu lưu trữ (storage / 저장소) khỏi hiện thực (implementation / 구현). StorageClass mô tả lớp (class / 클래스)/provisioning chính sách (policy / 정책). Nhưng Kubernetes không biến stateful hệ thống (system / 시스템) thành stateless.

Cơ sở dữ liệu (database / 데이터베이스) vẫn cần consistency, backup, replication và khôi phục (recovery / 복구) ngữ nghĩa (semantics / 의미론). Volume replication không tự động tương đương application-consistent backup. Snapshot lúc cơ sở dữ liệu (database / 데이터베이스) đang ghi có thể cần coordination để khôi phục nhất quán.

## 7. yêu cầu (request / 요청) và limit có hai vai trò khác nhau

Tài nguyên (resource / 자원) `request` là đầu vào (input / 입력) quan trọng cho scheduling và sức chứa (capacity / 용량) accounting. `limit` là ranh giới (boundary / 경계) thời gian chạy (runtime / 런타임) tùy tài nguyên (resource / 자원). giới hạn bộ nhớ (memory limit / 메모리 제한) thường có thể dẫn đến OOM kill khi vượt; Giới hạn CPU (CPU limit / CPU 제한) thường throttle.

Nếu yêu cầu (request / 요청) thấp hơn usage thực quá nhiều, scheduler có thể nhồi quá nhiều tải công việc (workload / 워크로드) lên nút (node / 노드) và tạo contention. Nếu yêu cầu (request / 요청) quá cao, cluster có sức chứa (capacity / 용량) nhưng scheduler không dùng được hiệu quả. điều chỉnh tài nguyên (resource tuning / 리소스 튜닝) vì vậy là bài toán statistical/sức chứa (capacity / 용량), không phải bản sao (copy / 복사) template.

## 8. QoS và eviction dưới pressure

Khi nút (node / 노드) chịu bộ nhớ (memory / 메모리)/disk pressure, kubelet có thể evict tải công việc (workload / 워크로드). Priority và tài nguyên (resource / 자원) cấu hình (configuration / 구성) ảnh hưởng tải công việc (workload / 워크로드) nào được giữ. dịch vụ trọng yếu (critical service / 핵심 서비스) cần hiểu nút (node / 노드) thất bại (failure / 실패)/eviction hành vi (behavior / 동작) thay vì chỉ tăng replicas.

Một triển khai (deployment / 배포) ba replica nhưng cả ba nằm cùng nút (node / 노드) hoặc cùng miền lỗi (failure domain / 장애 도메인) vẫn có availability thấp. Anti-affinity/topology spread giúp phân tán, nhưng càng nhiều ràng buộc (constraint / 제약조건) càng có nguy cơ unschedulable khi sức chứa (capacity / 용량) nhỏ.

## 9. Probe: startup, readiness, liveness

Startup probe giúp ứng dụng khởi động chậm tránh bị liveness kill sớm. Readiness quyết định traffic eligibility. Liveness quyết định restart khi tiến trình (process / 프로세스) được xem là không tự hồi phục.

Một probe tốt phải rẻ, ổn định và phản ánh ngữ nghĩa (semantics / 의미론) đúng. Liveness không nên gọi một phụ thuộc (dependency / 의존성) xa nếu phụ thuộc (dependency / 의존성) outage không thể được chữa bằng restart cục bộ (local / 로컬) tiến trình (process / 프로세스). Nếu mỗi pod restart vì DB down, restart storm có thể làm khôi phục (recovery / 복구) tệ hơn.

## 10. HPA và autoscaling là phản hồi (feedback / 피드백) controller

Horizontal Pod Autoscaler quan sát chỉ số (metric / 지표) rồi thay desired replica count. Đây là một vòng điều khiển (control loop / 제어 루프) có delay. chỉ số (metric / 지표) tăng → quy mô (scale / 규모) out → pod schedule/start/warm → traffic phân phối → chỉ số (metric / 지표) thay đổi.

Nếu vòng lặp (loop / 루프) phản ứng quá nhanh với noisy chỉ số (metric / 지표), replica có thể dao động. Nếu phản ứng quá chậm, người dùng (user / 사용자) chịu độ trễ (latency / 지연 시간) trước khi sức chứa (capacity / 용량) đến. chỉ số (metric / 지표) chọn cho autoscaling phải liên hệ demand và bottleneck. CPU không phải lúc nào cũng phù hợp; hàng đợi (queue / 큐) độ sâu (depth / 깊이) hoặc tính đồng thời (concurrency / 동시성) có thể phản ánh tải công việc (workload / 워크로드) tốt hơn.

## 11. Cluster autoscaling và tương tác (interaction / 상호작용) giữa vòng điều khiển (control loop / 제어 루프)

HPA có thể yêu cầu thêm Pod nhưng scheduler không có chỗ. Cluster autoscaler thấy unschedulable Pod rồi tăng nút (node / 노드). Cloud provider tạo VM mất thời gian. Nếu traffic spike ngắn hơn nút (node / 노드) provisioning thời gian (time / 시간), autoscaling không cứu được spike đó.

Đây là lý do cần sức chứa (capacity / 용량) buffer, tỷ lệ (rate / 비율) limiting và tải (load / 로드) shedding. Autoscaling không thay thế sức chứa (capacity / 용량) planning.

## 12. Rolling cập nhật (update / 업데이트) và availability math

Triển khai (deployment / 배포) rollout dùng các tham số như `maxUnavailable` và `maxSurge` để điều khiển bao nhiêu replica cũ có thể mất và bao nhiêu replica mới có thể thêm. Nhưng availability thật còn phụ thuộc readiness thời gian (time / 시간), sức chứa (capacity / 용량), PodDisruptionBudget, nút (node / 노드) drain và downstream.

Nếu cluster không có headroom để surge, rollout có thể stuck dù cấu hình (config / 설정) hợp lý trên giấy.

## 13. Scheduling ràng buộc (constraint / 제약조건) như chính sách (policy / 정책)

Nút (node / 노드) selector, affinity, taint/toleration và topology spread là ngôn ngữ mô tả placement. Dùng quá nhiều hard ràng buộc (constraint / 제약조건) làm scheduling brittle. Ưu tiên soft preference khi nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) không bắt buộc.

Nền tảng (platform / 플랫폼) nên expose intent như “GPU tải công việc (workload / 워크로드)”, “zone-spread dịch vụ (service / 서비스)”, “stateful-high-io” thay vì yêu cầu mọi nhà phát triển (developer / 개발자) hiểu toàn bộ label topology của cluster.

## 14. thất bại (failure / 실패) walkthrough

Pod `Pending`: đọc events để biết insufficient CPU, taint, PVC hoặc affinity. Pod `Running` nhưng `NotReady`: xem readiness, ứng dụng (application / 애플리케이션) và phụ thuộc (dependency / 의존성). Pod restart: xem `lastState`, exit mã (code / 코드), OOM/sự kiện (event / 이벤트), liveness. dịch vụ (service / 서비스) 503: xem endpoints/readiness trước proxy cấu hình (config / 설정). độ trễ (latency / 지연 시간) tăng khi CPU đồ thị (graph / 그래프) không cao: kiểm tra throttling, hàng đợi (queue / 큐), downstream và nút (node / 노드) pressure.

## 15. cấp cao (senior / 시니어) ghi chú (note / 노트): lớp trừu tượng (abstraction / 추상화) phải giữ được chuỗi nhân quả (causal chain / 인과 사슬)

Kubernetes có nhiều đối tượng (object / 객체) và controller, nhưng operator giỏi luôn giữ chuỗi nhân quả (causal chain / 인과 사슬): desired đối tượng (object / 객체) → controller quyết định (decision / 결정) → child tài nguyên (resource / 자원) → scheduler/nút (node / 노드) → thời gian chạy (runtime / 런타임) → mạng (network / 네트워크)/lưu trữ (storage / 저장소) → ứng dụng (application / 애플리케이션) tín hiệu (signal / 신호). nền tảng (platform / 플랫폼) tốt có thể che bớt đối tượng (object / 객체) bình thường nhưng phải cho phép mở chuỗi nhân quả (causal chain / 인과 사슬) khi sự cố (incident / 인시던트).

## 16. Scheduling là bài toán feasibility trước, scoring sau

Scheduler không bắt đầu bằng việc “chọn nút (node / 노드) tốt nhất”. Trước hết nó loại các nút (node / 노드) không thể chạy Pod theo ràng buộc (constraint / 제약조건) và yêu cầu tài nguyên (resource request / 리소스 요청). Sau khi có tập nút (node / 노드) khả thi, scoring mới xếp hạng lựa chọn.

Điều này giải thích một thất bại (failure / 실패) hay gặp: cluster nhìn tổng thể còn nhiều CPU nhưng Pod vẫn `Pending`. sức chứa (capacity / 용량) có thể bị phân mảnh. Ví dụ còn bốn nút (node / 노드), mỗi nút (node / 노드) rảnh 1 CPU nhưng Pod yêu cầu (request / 요청) 2 CPU; tổng free là 4 CPU nhưng không nút (node / 노드) nào đủ 2 CPU. Đây là khác biệt giữa **aggregate sức chứa (capacity / 용량)** và **schedulable sức chứa (capacity / 용량)**.

Yêu cầu tài nguyên (resource request / 리소스 요청) vì vậy vừa là reservation mô hình (model / 모델) vừa là đầu vào (input / 입력) bin-packing. yêu cầu (request / 요청) thấp quá tạo overcommit thời gian chạy (runtime / 런타임); cao quá tạo fragmentation và tăng nút (node / 노드) count. Tuning phải nhìn phân phối (distribution / 분포) theo replica, không chỉ tổng usage.

## 17. PodDisruptionBudget không phải availability guarantee

PodDisruptionBudget (PDB) chủ yếu giới hạn một số **voluntary disruption** như nút (node / 노드) drain/maintenance theo cơ chế có tôn trọng PDB. Nó không ngăn nút (node / 노드) crash, kernel panic hay ứng dụng (application / 애플리케이션) tiến trình (process / 프로세스) chết.

Do đó một PDB `minAvailable: 2` không có nghĩa “luôn luôn có ít nhất hai Pod”. Nếu hai nút (node / 노드) cùng mất đột ngột, PDB không thể ngăn thất bại (failure / 실패). Ngược lại, PDB quá chặt có thể chặn maintenance/upgrade nếu tải công việc (workload / 워크로드) không có đủ replica hoặc cluster thiếu sức chứa (capacity / 용량) tạo replacement.

Mô hình tư duy (mental model / 사고 모델) đúng là: PDB bảo vệ ngân sách (budget / 예산) cho planned eviction, còn high availability cần topology, replica, sức chứa (capacity / 용량) và phụ thuộc (dependency / 의존성) redundancy.

## 18. Priority và preemption đổi thất bại (failure / 실패) từ “không schedule được” thành “ai bị đẩy ra”

Khi cluster thiếu tài nguyên (resource / 자원), Pod priority có thể cho phép tải công việc (workload / 워크로드) quan trọng giành chỗ bằng cách preempt tải công việc (workload / 워크로드) thấp hơn. Đây là cơ chế chính sách (policy / 정책) mạnh nhưng có sự đánh đổi (trade-off / 트레이드오프): trọng yếu (critical / 중요) tải công việc (workload / 워크로드) có thể phục hồi nhanh hơn trong khi batch/dev tải công việc (workload / 워크로드) bị gián đoạn.

Nếu mọi nhóm (team / 팀) tự đánh tải công việc (workload / 워크로드) của mình là priority cao nhất, cơ chế (mechanism / 메커니즘) mất tác dụng. Priority lớp (class / 클래스) phải gắn với nghiệp vụ (business / 비즈니스) criticality và quản trị (governance / 거버넌스). Preemption cũng không tạo thêm sức chứa (capacity / 용량); nó chỉ phân bổ lại scarcity.

## 19. Topology spread cần hiểu miền lỗi (failure domain / 장애 도메인) thật

Replica “nằm trên ba nút (node / 노드) khác nhau” chưa chắc độc lập nếu ba nút (node / 노드) cùng zone, cùng rack hoặc cùng autoscaling group có thất bại (failure / 실패) chung. Topology spread/anti-affinity chỉ hữu ích nếu label topology phản ánh miền lỗi (failure domain / 장애 도메인) có ý nghĩa.

Ngược lại, yêu cầu spread quá cứng trong cluster nhỏ có thể làm Pod `Pending` trong lúc sự cố (incident / 인시던트). nền tảng (platform / 플랫폼) nên phân biệt bất biến (invariant / 불변식) bắt buộc — ví dụ replica trọng yếu (critical / 중요) phải trải ít nhất hai zone — với preference có thể nới khi sức chứa (capacity / 용량) căng.

## 20. Readiness và termination có một race cửa sổ (window / 윈도우)

Khi một Pod bị terminate, nhiều subsystem cần hội tụ: Pod nhận termination tín hiệu (signal / 신호), readiness/endpoints thay đổi, proxy/bộ cân bằng tải (load balancer / 로드 밸런서) cập nhật tuyến (route / 경로) và liên kết (connection / 연결) hiện tại drain. Những bước này không xảy ra atomically.

Nếu ứng dụng (application / 애플리케이션) đóng listener ngay lập tức trong khi proxy vẫn còn tuyến (route / 경로) tới endpoint vài giây, người dùng (user / 사용자) có thể thấy burst 502/liên kết (connection / 연결) reset trong rollout dù readiness probe trước đó hoàn toàn đúng. Graceful termination vì vậy cần phối hợp ứng dụng (application / 애플리케이션) shutdown với endpoint propagation và liên kết (connection / 연결) draining.

Một chuỗi (sequence / 시퀀스) thường an toàn hơn là: đánh dấu tải công việc (workload / 워크로드) không còn sẵn sàng nhận traffic, cho mặt phẳng dữ liệu (data plane / 데이터 플레인) đủ thời gian cập nhật, dừng nhận yêu cầu (request / 요청) mới, hoàn tất in-flight yêu cầu (request / 요청) trong deadline, rồi tiến trình (process / 프로세스) thoát trước khi grace period kết thúc. chính xác (exact / 정확한) cơ chế (mechanism / 메커니즘) tùy ingress/thời gian chạy (runtime / 런타임) nhưng chuỗi nhân quả (causal chain / 인과 사슬) giống nhau.

## 21. HPA chỉ số (metric / 지표) phải gắn với công việc (work / 작업), không chỉ tài nguyên (resource / 자원)

CPU-based HPA hoạt động tốt khi CPU gần tỷ lệ với demand. Nhưng với I/O-bound dịch vụ (service / 서비스), CPU thấp không có nghĩa còn sức chứa (capacity / 용량). hàng đợi (queue / 큐) bên tiêu thụ (consumer / 소비자) có thể phù hợp hơn với hàng đợi (queue / 큐) age/độ sâu (depth / 깊이); yêu cầu (request / 요청) dịch vụ (service / 서비스) có thể quy mô (scale / 규모) theo tính đồng thời (concurrency / 동시성) hoặc yêu cầu (request / 요청) tỷ lệ (rate / 비율) nếu tín hiệu (signal / 신호) đáng tin.

Chỉ số (metric / 지표) autoscaling còn có vấn đề cold start. Khi quy mô (scale / 규모) out, Pod mới có thể cần tải (load / 로드) lớp (class / 클래스)/JIT/bộ nhớ đệm (cache / 캐시)/mô hình (model / 모델) trước khi thực sự tăng dịch vụ (service / 서비스) tỷ lệ (rate / 비율). Nếu HPA nhìn chỉ số (metric / 지표) thay đổi nhanh hơn tải công việc (workload / 워크로드) warm-up, controller có thể overshoot rồi quy mô (scale / 규모) down, tạo oscillation.

Do đó autoscaling chính sách (policy / 정책) cần biết observation cửa sổ (window / 윈도우), stabilization, startup thời gian (time / 시간) và minimum headroom. vòng điều khiển (control loop / 제어 루프) tốt không chỉ phản ứng đúng hướng mà còn phải ổn định theo thời gian.

## 22. Autoscaling nhiều tầng có thể tạo phản hồi (feedback / 피드백) ngoài ý muốn

Giả sử HPA tăng replica vì độ trễ (latency / 지연 시간)/CPU. Pod mới không schedule được nên cluster autoscaler tăng nút (node / 노드). Khi nút (node / 노드) xuất hiện, hàng loạt Pod start cùng lúc, mở liên kết (connection / 연결) DB và warm bộ nhớ đệm (cache / 캐시). cơ sở dữ liệu (database / 데이터베이스) bị saturation, độ trễ (latency / 지연 시간) tăng thêm, HPA lại tăng replica. Một vòng lặp (loop / 루프) cục bộ (local / 로컬) hợp lý có thể khuếch đại thất bại (failure / 실패) toàn hệ thống.

Cách thiết kế trưởng thành là đặt ranh giới (boundary / 경계): max replica theo downstream sức chứa (capacity / 용량), liên kết (connection / 연결) ngân sách (budget / 예산), tỷ lệ (rate / 비율) limit, warm-up điều khiển (control / 제어) và SLO tín hiệu (signal / 신호). Autoscaler không được coi downstream là vô hạn.

## 23. cấp cao (senior / 시니어) walkthrough: rollout stuck dù tải công việc (workload / 워크로드) mới “không lỗi”

Giả sử triển khai (deployment / 배포) 20 replica dùng `maxSurge: 25%`, nhưng cluster gần đầy. Controller muốn tạo thêm 5 Pod mới trước khi xóa Pod cũ. Scheduler không tìm được nút (node / 노드) vì yêu cầu (request / 요청) không fit; cluster autoscaler không thể tạo nút (node / 노드) do cloud quota đã chạm. Pod mới `Pending`, rollout không tiến.

Ứng dụng mới không có bug, readiness chưa có cơ hội chạy. thất bại (failure / 실패) nằm ở tương tác (interaction / 상호작용) giữa rollout chính sách (policy / 정책), yêu cầu tài nguyên (resource request / 리소스 요청), cluster headroom và cloud quota. Fix có thể là tăng sức chứa (capacity / 용량)/quota, điều chỉnh rollout ngân sách (budget / 예산) hoặc giảm yêu cầu (request / 요청) sau khi có bằng chứng (evidence / 증거); restart Pod không giải được chuỗi nhân quả (causal chain / 인과 사슬).

Đây là kiểu môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) Kubernetes cần: đối tượng (object / 객체) status là symptom của nhiều vòng điều khiển (control loop / 제어 루프) lồng nhau, không phải một lỗi đơn lẻ.

## 24. Persistent volume có topology và attach vòng đời (lifecycle / 생명주기) riêng

Một PVC tồn tại không có nghĩa volume có thể mount ở mọi nút (node / 노드). Nhiều khối (block / 블록) volume gắn với zone hoặc có giới hạn số volume attach trên nút (node / 노드). Scheduler/lưu trữ (storage / 저장소) controller phải phối hợp placement với topology của volume.

Vì vậy Pod stateful có thể `Pending` dù CPU/bộ nhớ (memory / 메모리) còn nhiều nếu volume ở zone không có nút (node / 노드) phù hợp, attach limit đã chạm hoặc volume vẫn đang detach từ nút (node / 노드) cũ. Đây là thất bại (failure / 실패) đường dẫn (path / 경로) khác hoàn toàn với ứng dụng (application / 애플리케이션) startup.

Khi điều tra, nối `PVC/PV → StorageClass/topology → selected node → attach/mount event`. quy mô (scale / 규모) nút (node / 노드) ở zone khác không giúp nếu volume không di chuyển được. lưu trữ (storage / 저장소) topology phải là đầu vào (input / 입력) của sức chứa (capacity / 용량)/khôi phục (recovery / 복구) thiết kế (design / 설계), không phải chi tiết CSI bị phát hiện lần đầu trong sự cố (incident / 인시던트).

## 25. StatefulSet stable định danh (identity / 식별자) không tự tạo dữ liệu (data / 데이터) an toàn (safety / 안전)

StatefulSet giữ ordinal/mạng (network / 네트워크) định danh (identity / 식별자) và thường gắn mỗi replica với PVC riêng. Nhưng nó không tự hiểu replication/quorum của cơ sở dữ liệu (database / 데이터베이스). Xóa hoặc restart replica theo thứ tự “đẹp” vẫn có thể mất quorum nếu dữ liệu (data / 데이터) hệ thống (system / 시스템) có topology khác Kubernetes topology.

Rolling cập nhật (update / 업데이트) của stateful tải công việc (workload / 워크로드) cần biết nút (node / 노드) nào leader, replica nào lag, partition/cập nhật (update / 업데이트) thứ tự (order / 순서) và application-level readiness thật sự có nghĩa gì. Probe chỉ trả lời điều kiện (condition / 조건) được encode; nó không thay thế consistency bất biến (invariant / 불변식) của cơ sở dữ liệu (database / 데이터베이스).

Vì vậy nền tảng (platform / 플랫폼) không nên biến StatefulSet thành “cơ sở dữ liệu (database / 데이터베이스) button” nếu không sở hữu backup, replication, upgrade và khôi phục (recovery / 복구) ngữ nghĩa (semantics / 의미론) tương ứng.

## 26. Ephemeral lưu trữ (storage / 저장소) cũng là tài nguyên (resource / 자원) có pressure và eviction

Pod có thể ghi writable tầng (layer / 계층), `emptyDir`, logs hoặc temporary files. Những bytes này dùng nút (node / 노드) ephemeral lưu trữ (storage / 저장소). tải công việc (workload / 워크로드) có CPU/bộ nhớ (memory / 메모리) khỏe nhưng vẫn bị evict hoặc thất bại (fail / 실패) khi nút (node / 노드) disk pressure nếu temporary/log đầu ra (output / 출력) tăng bất thường.

Tài nguyên (resource / 자원) planning cần nhìn cả byte sức chứa (capacity / 용량) lẫn I/O tỷ lệ (rate / 비율). Một batch job tạo hàng trăm GiB temporary dữ liệu (data / 데이터) có thể ảnh hưởng nút (node / 노드) khác dù final đầu ra (output / 출력) được upload đối tượng (object / 객체) lưu trữ (storage / 저장소). Requests/limits/quota cho ephemeral lưu trữ (storage / 저장소), log rotation và cleanup vòng đời (lifecycle / 생명주기) giúp biến tài nguyên (resource / 자원) ẩn thành đặc tả hợp đồng (contract / 계약).

Khi `DiskPressure` xuất hiện, chỉ xóa Pod thường giải phóng tạm thời nhưng không sửa producer tạo dữ liệu (data / 데이터) không bounded.

## 27. Job thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론) phải đi cùng idempotency của nghiệp vụ (business / 비즈니스) công việc (work / 작업)

`Job` có thể chạy lại Pod khi tiến trình (process / 프로세스) thất bại (fail / 실패). Điều đó tốt cho transient hạ tầng (infrastructure / 인프라) thất bại (failure / 실패) nhưng nguy hiểm nếu nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) đã side-effect một phần rồi exit trước khi ghi completion trạng thái (state / 상태).

Ví dụ job charge invoice: payment API đã nhận yêu cầu (request / 요청) nhưng tiến trình (process / 프로세스) chết trước khi lưu “done”. Pod mới chạy lại và charge lần hai nếu thao tác (operation / 연산) không có idempotency key/giao dịch (transaction / 트랜잭션) giao thức (protocol / 프로토콜) phù hợp. Kubernetes chỉ biết tiến trình (process / 프로세스) completion, không biết nghiệp vụ (business / 비즈니스) tác động (effect / 효과).

Batch nền tảng (platform / 플랫폼) nên expose thử lại (retry / 재시도)/backoff/dead-letter ngữ nghĩa (semantics / 의미론) và khuyến khích công việc (work / 작업) item có durable định danh (identity / 식별자). “At least one successful Pod” không đồng nghĩa “nghiệp vụ (business / 비즈니스) side tác động (effect / 효과) exactly once”.

## 28. CronJob phải lập luận (reasoning / 추론) về missed run và overlapping run

Scheduled job phụ thuộc controller clock, scheduling delay và previous run duration. Nếu job 10 phút nhưng chạy mỗi 5 phút, overlap có thể tạo concurrent công việc (work / 작업) ngoài ý muốn. Nếu điều khiển (control / 제어) plane down, một số schedule có thể bị trễ/missed theo chính sách (policy / 정책).

Vì vậy batch đặc tả hợp đồng (contract / 계약) cần quyết định overlap có được phép không, late thực thi (execution / 실행) còn giá trị không, deadline là gì và công việc (work / 작업) có deduplicate theo logical schedule ID không. Không nên giả định cron expression tự tạo nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성).

Một report “mỗi ngày lúc 00:00” thường thực sự có bất biến (invariant / 불변식) về dữ liệu (data / 데이터) cửa sổ (window / 윈도우), timezone và exactly-one logical đầu ra (output / 출력); đó là đặc tả ứng dụng (application contract / 애플리케이션 계약) cần được encode ngoài scheduler.

## 29. Endpoint quy mô (scale / 규모) tạo pressure lên điều khiển (control / 제어) plane và mặt phẳng dữ liệu (data plane / 데이터 플레인)

Một dịch vụ (service / 서비스) có vài endpoint khác với một dịch vụ (service / 서비스) có hàng chục nghìn endpoint. Endpoint cập nhật (update / 업데이트), watch fan-out và proxy programming đều có chi phí (cost / 비용). Khi tải công việc (workload / 워크로드) churn lớn, điều khiển (control / 제어) plane có thể xử lý liên tục endpoint changes trong khi mặt phẳng dữ liệu (data plane / 데이터 플레인) chưa hội tụ hoàn toàn.

Vì vậy “thêm thật nhiều replica” không miễn phí. Replica count lớn tăng scheduling, ảnh (image / 이미지) pull, readiness probe, endpoint propagation, liên kết (connection / 연결) warming và khả năng quan sát (observability / 관측 가능성) cardinality. Có lúc scale-up làm độ tin cậy (reliability / 신뢰성) giảm vì control-plane/data-plane churn lớn hơn lợi ích sức chứa (capacity / 용량).

Sức chứa (capacity / 용량) kỹ thuật (engineering / 엔지니어링) cần tìm điểm mà thêm replica còn tăng thông lượng (throughput / 처리량) hữu ích, thay vì dùng replica count như actuator không giới hạn.

## 30. cấp cao (senior / 시니어) walkthrough: Pod stateful failover chậm dù nút (node / 노드) mới đã sẵn sàng

Giả sử nút (node / 노드) chứa một cơ sở dữ liệu (database / 데이터베이스) replica chết. Autoscaler tạo nút (node / 노드) mới trong 2 phút nhưng Pod vẫn `Pending` thêm 8 phút. CPU/bộ nhớ (memory / 메모리) fit và ảnh (image / 이미지) đã pull. sự kiện (event / 이벤트) cho thấy volume cũ chưa detach khỏi nút (node / 노드) mất liên lạc nên attach vào nút (node / 노드) mới bị khối (block / 블록) để tránh simultaneous writer.

Chuỗi nhân quả (causal chain / 인과 사슬) nằm ở lưu trữ (storage / 저장소) fencing/attach vòng đời (lifecycle / 생명주기), không ở scheduler sức chứa (capacity / 용량). Force-detach có thể rút ngắn khôi phục (recovery / 복구) nhưng tăng rủi ro (risk / 위험) nếu nút (node / 노드) cũ thực ra vẫn ghi được. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa khôi phục (recovery / 복구) thời gian (time / 시간) và split-brain/dữ liệu (data / 데이터) corruption.

Bài học là khôi phục (recovery / 복구) của stateful tải công việc (workload / 워크로드) bị giới hạn bởi **dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) transfer**, không chỉ bởi tốc độ tạo Pod/nút (node / 노드).

## 31. Eviction là giao thức (protocol / 프로토콜) có nhiều nguyên nhân, không phải mọi Pod biến mất đều giống nhau

Pod có thể rời nút (node / 노드) vì operator drain, cluster autoscaler scale-down, nút (node / 노드) pressure, preemption, nút (node / 노드) thất bại (failure / 실패) hoặc controller rollout. Các đường này có ngữ nghĩa (semantics / 의미론) khác nhau: có đường tôn trọng PDB, có đường không; có đường cho grace period đầy đủ, có đường tiến trình (process / 프로세스) biến mất cùng nút (node / 노드).

Runbook không nên chỉ nhìn trạng thái cuối `Terminated/Evicted`. bằng chứng (evidence / 증거) cần giữ reason, initiator, nút (node / 노드) điều kiện (condition / 조건), PDB quyết định (decision / 결정) và replacement timing. Nếu 20 Pod cùng biến mất vì autoscaler consolidation, remediation khác hoàn toàn 20 Pod bị OOM hoặc zone mất điện.

Nền tảng (platform / 플랫폼) nên coi disruption nguồn (source / 소스) như thay đổi (change / 변경) telemetry. Availability ngân sách (budget / 예산) chỉ có ý nghĩa khi biết ai đang tiêu ngân sách (budget / 예산) và cơ chế (mechanism / 메커니즘) đó có thể pause/throttle được không.

## 32. Cluster autoscaler scale-down cũng là một vòng điều khiển (control loop / 제어 루프) gây disruption

Scale-up thường được chú ý vì thiếu sức chứa (capacity / 용량), nhưng scale-down có thể tạo churn khi nút (node / 노드) vừa trở nên “ít dùng”. Evict Pod để consolidate nút (node / 노드) làm replacement schedule ở nơi khác, pull ảnh (image / 이미지), warm bộ nhớ đệm (cache / 캐시) và mở lại liên kết (connection / 연결). Nếu traffic tăng lại ngay sau đó, cluster có thể vừa quy mô (scale / 규모) down xong đã phải quy mô (scale / 규모) up.

Một hệ thống ổn định cần hysteresis/stabilization: không thu hồi sức chứa (capacity / 용량) quá nhanh chỉ vì một cửa sổ utilization thấp. Với tải công việc (workload / 워크로드) có startup lâu hoặc traffic theo burst, một phần idle headroom có thể rẻ hơn độ trễ (latency / 지연 시간)/khôi phục (recovery / 복구) chi phí (cost / 비용) của việc liên tục tạo-hủy nút (node / 노드).

Bằng chứng (evidence / 증거) nên nối `scale-down decision → evictions → rescheduling/warm-up → user latency/SLO → scale-up tiếp theo`. Nếu chỉ nhìn cloud chi phí (cost / 비용) giảm, ta có thể bỏ qua oscillation mà autoscaler tạo ra.

## 33. HPA, VPA và rollout có thể tranh quyền trên cùng tải công việc (workload / 워크로드)

Horizontal scaling thay replica count; vertical scaling thay yêu cầu (request / 요청)/limit; rollout thay Pod template và tạo replacement. Nếu nhiều controller cùng điều chỉnh tài nguyên (resource / 자원) mà không có quyền sở hữu (ownership / 소유권) đặc tả hợp đồng (contract / 계약), một hành động (action / 동작) có thể làm tín hiệu (signal / 신호) của controller khác đổi đột ngột.

Ví dụ VPA tăng CPU yêu cầu (request / 요청) làm Pod cũ cần recreate; scheduler cần nút (node / 노드) lớn hơn; rollout đang surge; HPA lại quy mô (scale / 규모) replica dựa trên utilization tính theo yêu cầu (request / 요청) mới. Từng controller cục bộ (local / 로컬) có thể đúng nhưng composition tạo Pending Pod, churn hoặc sức chứa (capacity / 용량) spike.

Nền tảng (platform / 플랫폼) cần xác định controller nào được phép mutate trường dữ liệu (field / 필드) nào, recommendation nào chỉ advisory và maintenance cửa sổ (window / 윈도우) nào cho disruptive resize. mô hình tư duy (mental model / 사고 모델) là **multi-controller composition**, không phải bật càng nhiều autoscaler càng tốt.

## 34. Sau thất bại (failure / 실패), topology có thể hồi phục sức chứa (capacity / 용량) nhưng chưa hồi phục redundancy

Giả sử dịch vụ (service / 서비스) ba replica trải ba zone. Một zone mất, scheduler tạo replacement ở hai zone còn lại để khôi phục replica count. Dashboard lại thấy `3/3 Ready`, nhưng thất bại (failure / 실패) tolerance đã giảm vì hai hoặc ba replica có thể tập trung vào ít miền lỗi (failure domain / 장애 도메인) hơn.

Khi zone cũ trở lại, scheduler không nhất thiết tự di chuyển Pod chỉ để tái cân bằng nếu placement hiện tại vẫn hợp lệ. Vì vậy khôi phục (recovery / 복구) criterion cần kiểm tra **redundancy/topology bất biến (invariant / 불변식)**, không chỉ desired replica count. Có thể cần controlled rebalance với disruption ngân sách (budget / 예산) và sức chứa (capacity / 용량) headroom.

Đây là distinction quan trọng giữa `capacity recovered` và `resilience recovered`.

## 35. Sidecar và init vòng đời (lifecycle / 생명주기) có thể giữ Pod chưa thật sự hoàn tất hoặc chưa thật sự sẵn sàng

Một Pod có nhiều bộ chứa (container / 컨테이너) nên vòng đời (lifecycle / 생명주기) của nghiệp vụ (business / 비즈니스) tiến trình (process / 프로세스) không luôn trùng vòng đời (lifecycle / 생명주기) toàn Pod. Init công việc (work / 작업) có thể khối (block / 블록) startup; sidecar proxy/tác nhân (agent / 에이전트) có thể cần sẵn sàng trước ứng dụng (application / 애플리케이션) traffic hoặc cần sống đủ lâu để flush telemetry/drain mạng (network / 네트워크) khi shutdown.

Nếu readiness chỉ kiểm tra ứng dụng (application / 애플리케이션) nhưng sidecar mặt phẳng dữ liệu (data plane / 데이터 플레인) chưa nhận cấu hình (config / 설정), Pod có thể được tuyến (route / 경로) quá sớm. Nếu Job nghiệp vụ (business / 비즈니스) bộ chứa (container / 컨테이너) hoàn thành nhưng helper bộ chứa (container / 컨테이너) không có completion ngữ nghĩa (semantics / 의미론) đúng, logical công việc (work / 작업) đã xong nhưng Pod vẫn chưa kết thúc như operator kỳ vọng.

Thiết kế cần xác định phụ thuộc (dependency / 의존성) thứ tự (order / 순서) giữa containers, readiness của **đường đi của yêu cầu (request path / 요청 경로) đầy đủ**, và shutdown thứ tự (order / 순서) để in-flight công việc (work / 작업)/telemetry không mất. “bộ chứa (container / 컨테이너) chính healthy” chưa chắc đồng nghĩa Pod năng lực (capability / 역량) mà người dùng (user / 사용자) cần đã healthy.

> **Bàn giao:** Sau **35. Sidecar và init vòng đời (lifecycle / 생명주기) có thể giữ Pod chưa thật sự hoàn tất hoặc chưa thật sự sẵn sàng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 kubernetes reconciliation and control plane](./00_kubernetes_reconciliation_and_control_plane.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
