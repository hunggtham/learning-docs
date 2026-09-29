# Kubernetes: reconciliation, API objects và điều khiển (control / 제어) plane

> **Mạch đọc:** Đọc **Kubernetes: reconciliation, API objects và điều khiển (control / 제어) plane** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Kubernetes không phải “Docker chạy nhiều máy”** sang **2. API đối tượng (object / 객체) là đặc tả hợp đồng (contract / 계약) trạng thái (state / 상태)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. Kubernetes không phải “Docker chạy nhiều máy”

Kubernetes tồn tại vì khi số tải công việc (workload / 워크로드) và nút (node / 노드) tăng, việc tự quyết định bộ chứa (container / 컨테이너) chạy ở đâu, restart thế nào, tuyến (route / 경로) tới instance nào và rollout phiên bản mới trở thành một bài toán orchestration có trạng thái (state / 상태). Kubernetes giải bài toán này bằng một kiến trúc rất nhất quán: người dùng khai báo trạng thái mong muốn (desired state), điều khiển (control / 제어) plane lưu và quan sát trạng thái (state / 상태), controller liên tục đối soát (reconciliation) để actual trạng thái (state / 상태) tiến gần desired trạng thái (state / 상태).

Mô hình tư duy (mental model / 사고 모델) cốt lõi:

```text
user / automation
      ↓
 Kubernetes API
      ↓ desired state
 persistent control-plane state
      ↓ watch
 controllers + scheduler
      ↓ act
 kubelet / networking / storage / runtime
      ↓
 actual workload state
      └──── feedback/status ────→ API
```

Nếu chỉ nhớ YAML trường dữ liệu (field / 필드) mà không hiểu vòng này, rất dễ nhầm “tài nguyên (resource / 자원) đã tạo” với “ứng dụng (application / 애플리케이션) đã chạy đúng”.

## 2. API đối tượng (object / 객체) là đặc tả hợp đồng (contract / 계약) trạng thái (state / 상태)

Một đối tượng (object / 객체) Kubernetes thường có `metadata`, `spec` và `status`. `spec` chủ yếu mô tả điều người dùng muốn. `status` là quan sát của controller về trạng thái hiện tại. Generation, conditions và observed trạng thái (state / 상태) cho biết controller đã xử lý spec mới tới đâu.

Vì vậy khi `kubectl apply` thành công, điều chắc chắn nhất chỉ là API máy chủ (server / 서버) chấp nhận yêu cầu (request / 요청). triển khai (deployment / 배포) có thể vẫn chưa rollout, pod có thể Pending, ảnh (image / 이미지) pull có thể thất bại (fail / 실패) hoặc readiness có thể chưa đạt.

Đây là khác biệt giữa control-plane acknowledgement và data-plane kết quả (outcome / 결과).

## 3. API máy chủ (server / 서버) là front door của điều khiển (control / 제어) plane

API máy chủ (server / 서버) xác thực yêu cầu (request / 요청), kiểm tra authorization/admission, validate đối tượng (object / 객체) rồi lưu trạng thái (state / 상태). Các controller và thành phần (component / 컴포넌트) khác watch API thay vì sửa trực tiếp cơ sở dữ liệu (database / 데이터베이스) control-plane.

Điều này tạo một đặc tả hợp đồng (contract / 계약) mạnh: API là ranh giới (boundary / 경계) thống nhất cho người dùng, controller và automation. Nó cũng làm API máy chủ (server / 서버) trở thành ranh giới bảo mật (security boundary / 보안 경계); RBAC quá rộng nghĩa automation có thể thay nhiều trạng thái (state / 상태) hơn dự kiến.

## 4. etcd và consistency của cluster trạng thái (state / 상태)

Kubernetes thường dùng `etcd` làm persistent store cho control-plane trạng thái (state / 상태). Không cần trở thành chuyên gia Raft để sử dụng Kubernetes, nhưng phải hiểu rằng cluster trạng thái (state / 상태) là phân tán (distributed / 분산) durable trạng thái (state / 상태) và backup/restore nó khác backup ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터).

Consensus, log replication và snapshot cơ chế (mechanism / 메커니즘) được đào sâu tại [Computer Science — consensus, log replication và snapshots](../../computer_science/06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md). DevOps cần quan tâm vận hành: control-plane backup, tính tương thích (compatibility / 호환성) khi upgrade và khôi phục (recovery / 복구) procedure đã được kiểm thử (test / 테스트) hay chưa.

## 5. Controller là vòng điều khiển (control loop / 제어 루프) có quyền sở hữu (ownership / 소유권) trường dữ liệu (field / 필드)

Triển khai (deployment / 배포) controller, ReplicaSet controller, nút (node / 노드) controller và nhiều controller khác đều watch trạng thái (state / 상태) rồi tạo hành động (action / 동작). Một controller tốt có tính lặp an toàn (idempotent): chạy lại không được tạo trạng thái (state / 상태) sai chỉ vì sự kiện (event / 이벤트) bị duplicate.

Điểm dễ bỏ qua là nhiều controller có thể tương tác trên cùng đối tượng (object / 객체) đồ thị (graph / 그래프). triển khai (deployment / 배포) tạo ReplicaSet; ReplicaSet tạo Pod; scheduler gán Pod vào nút (node / 노드); kubelet làm bộ chứa (container / 컨테이너) chạy; CNI cung cấp mạng (network / 네트워크); CSI cung cấp volume. Khi Pod không Ready, thất bại (failure / 실패) có thể nằm ở bất kỳ stage nào.

Troubleshooting Kubernetes vì vậy nên đọc đối tượng (object / 객체) đồ thị (graph / 그래프) và sự kiện (event / 이벤트) chuỗi (chain / 사슬), không chỉ restart pod.

## 6. Scheduler quyết định placement, không chạy tải công việc (workload / 워크로드)

Scheduler chọn nút (node / 노드) phù hợp cho Pod dựa trên ràng buộc (constraint / 제약조건), yêu cầu tài nguyên (resource request / 리소스 요청), affinity/anti-affinity, taint/toleration và plugin scoring. Sau khi binding, kubelet trên nút (node / 노드) mới thực hiện việc kéo ảnh (image / 이미지), mount volume và gọi thời gian chạy (runtime / 런타임).

Nếu Pod `Pending`, trước hết xem scheduler/sự kiện (event / 이벤트). Nếu Pod đã `Scheduled` nhưng bộ chứa (container / 컨테이너) không start, tìm kiếm (search / 검색) không gian (space / 공간) chuyển sang kubelet/thời gian chạy (runtime / 런타임)/ảnh (image / 이미지)/lưu trữ (storage / 저장소). Tách stage giúp giảm đoán mò.

## 7. Kubelet nối desired Pod với nút (node / 노드) reality

Kubelet là nút (node / 노드) tác nhân (agent / 에이전트). Nó quan sát Pod được assign cho nút (node / 노드), phối hợp thời gian chạy (runtime / 런타임)/mạng (network / 네트워크)/lưu trữ (storage / 저장소) và báo status về API. Kubelet không phải scheduler và không tự chọn tải công việc (workload / 워크로드) từ cluster.

Khi nút (node / 노드) mất liên lạc với điều khiển (control / 제어) plane, Pod tiến trình (process / 프로세스) có thể còn chạy một thời gian trong khi cluster không còn chắc về trạng thái (state / 상태). Đây là ví dụ phân tán (distributed / 분산) các hệ thống (systems / 시스템들): “không nhận heartbeat” không chứng minh tiến trình (process / 프로세스) chết. thất bại (failure / 실패) detector luôn có bất định (uncertainty / 불확실성). Nền sâu xem [failure detectors, membership và gossip](../../computer_science/06_networks_distributed_systems/advanced/01_failure_detectors_membership_and_gossip.md).

## 8. Declarative trạng thái (state / 상태) không có nghĩa mọi thay đổi đều safe

Kubernetes dễ apply cấu hình (config / 설정) nhưng không hiểu nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식). Nếu giảm replica từ 10 xuống 1, API vẫn có thể chấp nhận. Nếu readiness probe sai, controller có thể rollout tải công việc (workload / 워크로드) không thực sự usable. Declarative engine bảo đảm convergence theo spec; con người/nền tảng (platform / 플랫폼) phải bảo đảm spec đúng và rollout chính sách (policy / 정책) phù hợp.

Admission chính sách (policy / 정책), defaults, quotas và nền tảng (platform / 플랫폼) abstractions tồn tại để encode những bất biến (invariant / 불변식) tổ chức muốn giữ trước khi trạng thái (state / 상태) đi vào cluster.

## 9. Labels và selectors tạo quan hệ động

Kubernetes dùng label/selector để liên kết đối tượng (object / 객체) như dịch vụ (service / 서비스)→Pod hoặc triển khai (deployment / 배포)→ReplicaSet. Đây là lớp trừu tượng (abstraction / 추상화) mạnh nhưng cũng là nguồn thất bại (failure / 실패) tinh vi: typo label có thể làm dịch vụ (service / 서비스) không còn endpoint dù Pod healthy.

Selector nên được coi là relational đặc tả hợp đồng (contract / 계약). Thay label chiến lược (strategy / 전략) có thể có blast radius lớn hơn diff YAML thể hiện.

## 10. không gian tên (namespace / 네임스페이스) là organizational ranh giới (boundary / 경계), không phải ranh giới bảo mật (security boundary / 보안 경계) tuyệt đối

Không gian tên (namespace / 네임스페이스) giúp phạm vi (scope / 범위) name, RBAC, quota và chính sách (policy / 정책), nhưng tải công việc (workload / 워크로드) ở hai không gian tên (namespace / 네임스페이스) không mặc định bị network-isolated. bảo mật (security / 보안) cần nhiều lớp: RBAC, chính sách mạng (network policy / 네트워크 정책), tải công việc (workload / 워크로드) định danh (identity / 식별자), pod bảo mật (security / 보안) và secret ranh giới (boundary / 경계).

Dùng không gian tên (namespace / 네임스페이스) như đơn vị (unit / 단위) quyền sở hữu (ownership / 소유권)/tenancy là hợp lý khi đi kèm chính sách (policy / 정책) rõ; không nên giả định “khác không gian tên (namespace / 네임스페이스) nên không thể ảnh hưởng nhau”.

## 11. Custom tài nguyên (resource / 자원) và operator

Custom tài nguyên (resource / 자원) Definition mở rộng API để nền tảng (platform / 플랫폼) tự định nghĩa desired trạng thái (state / 상태) mới. Operator/controller đọc tài nguyên (resource / 자원) đó rồi reconcile bên ngoài (external / 외부)/nội bộ (internal / 내부) tài nguyên (resource / 자원).

Ví dụ `Database` custom tài nguyên (resource / 자원) có thể đại diện intent “tôi cần PostgreSQL plan X”, còn controller tạo cloud cơ sở dữ liệu (database / 데이터베이스), secret tham chiếu (reference / 참조) và monitoring. Đây là cầu nối (bridge / 브리지) trực tiếp sang kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링).

Nhưng CRD chỉ đáng có khi có stable lĩnh vực (domain / 도메인) mô hình (model / 모델). Nếu mọi cloud trường dữ liệu (field / 필드) bị expose nguyên xi, nền tảng (platform / 플랫폼) chỉ đổi YAML shape mà chưa tạo lớp trừu tượng (abstraction / 추상화).

## 12. bằng chứng (evidence / 증거) khi gỡ lỗi (debug / 디버그) vòng điều khiển (control loop / 제어 루프)

Thứ tự hữu ích là đọc `spec`, `status.conditions`, `events`, child resources và nút (node / 노드)/thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거). Hỏi controller nào đang sở hữu bước hiện tại và desired/actual khác nhau ở đâu.

Ví dụ triển khai (deployment / 배포) không Available: xem desired replicas và conditions; ReplicaSet có pod chưa; Pod Pending hay Running; nếu Running thì Ready chưa; nếu không Ready thì probe/ứng dụng (application / 애플리케이션); nếu Pending thì scheduler sự kiện (event / 이벤트); nếu ImagePullBackOff thì registry/auth/ảnh (image / 이미지).

## 13. cấp cao (senior / 시니어) ghi chú (note / 노트): Kubernetes là nhiều vòng điều khiển (control loop / 제어 루프) lồng nhau

Một ứng dụng Kubernetes thường nằm trong nhiều vòng lặp (loop / 루프): triển khai (deployment / 배포) controller, HPA, GitOps controller, dịch vụ (service / 서비스) mesh controller, cloud bộ cân bằng tải (load balancer / 로드 밸런서) controller và autoscaler. Hai controller cùng sửa một trường dữ liệu (field / 필드) có thể tạo oscillation.

Khi nền tảng (platform / 플랫폼) tự động hóa nhiều hơn, câu hỏi quan trọng không phải “controller có chạy không?” mà là **ai sở hữu trường dữ liệu (field / 필드) nào, vòng điều khiển (control loop / 제어 루프) có stable không, độ trễ (latency / 지연 시간) của phản hồi (feedback / 피드백) là bao lâu và thất bại (failure / 실패) có bị khuếch đại giữa các vòng lặp (loop / 루프) không?**

## 14. API cập nhật (update / 업데이트) là optimistic tính đồng thời (concurrency / 동시성), không phải khóa đối tượng (object / 객체) dài hạn

Kubernetes đối tượng (object / 객체) thay đổi liên tục bởi nhiều actor. API không giữ một khóa (lock / 잠금) dài quanh đối tượng (object / 객체) để ngăn mọi writer. Thay vào đó, mỗi phiên bản (version / 버전) trạng thái (state / 상태) có định danh (identity / 식별자)/phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터); cập nhật (update / 업데이트) có thể bị từ chối nếu actor dựa trên trạng thái (state / 상태) cũ.

Mô hình tư duy (mental model / 사고 모델) là optimistic tính đồng thời (concurrency / 동시성): đọc trạng thái (state / 상태), tính thay đổi, cố ghi; nếu đối tượng (object / 객체) đã đổi, reconcile lại trên trạng thái (state / 상태) mới. Controller vì vậy phải chấp nhận xung đột (conflict / 충돌)/thử lại (retry / 재시도) thay vì giả định sự kiện (event / 이벤트) chỉ đến đúng một lần và trạng thái (state / 상태) đứng yên trong lúc xử lý.

Đối với operator/nền tảng (platform / 플랫폼) controller tự viết, lô-gic (logic / 논리) “read-modify-write” cần idempotent và chịu xung đột (conflict / 충돌). Nếu thử lại (retry / 재시도) tạo duplicate bên ngoài (external / 외부) tài nguyên (resource / 자원), bug nằm ở controller đặc tả hợp đồng (contract / 계약) chứ không phải API máy chủ (server / 서버).

## 15. `resourceVersion`, generation và observedGeneration trả lời câu hỏi khác nhau

`resourceVersion` giúp nhận diện phiên bản đối tượng (object / 객체) trong API/lưu trữ (storage / 저장소)/watch ngữ nghĩa (semantics / 의미론). `metadata.generation` thường tăng khi desired spec thay đổi. Controller có thể ghi `observedGeneration`/điều kiện (condition / 조건) để nói nó đã xử lý generation nào.

Khi spec vừa đổi nhưng status vẫn xấu, hãy hỏi controller đã observe generation mới chưa. Nếu chưa, lỗi có thể ở controller hàng đợi (queue / 큐)/watch. Nếu đã observe nhưng điều kiện (condition / 조건) vẫn thất bại (fail / 실패), controller đã xử lý intent và tìm thấy thất bại (failure / 실패) downstream.

Điều này tốt hơn nhìn timestamp hoặc chỉ chờ vài giây theo cảm giác.

## 16. Admission nằm trên ghi (write / 쓰기) đường dẫn (path / 경로) nên chính sách (policy / 정책) có thể ảnh hưởng availability của điều khiển (control / 제어) plane

Một yêu cầu (request / 요청) tạo/sửa đối tượng (object / 객체) thường đi qua authentication, authorization, defaulting/kiểm tra hợp lệ (validation / 검증) và có thể qua admission chính sách (policy / 정책)/webhook trước khi persist. Admission cho phép encode guardrail nhưng cũng thêm phụ thuộc (dependency / 의존성) vào ghi (write / 쓰기) đường dẫn (path / 경로).

Nếu admission webhook hết thời gian chờ (timeout / 타임아웃)/thất bại (fail / 실패) theo chính sách (policy / 정책) fail-closed, deploy có thể bị chặn diện rộng. Nếu fail-open, availability tốt hơn nhưng bảo mật (security / 보안) bất biến (invariant / 불변식) có thể tạm không được enforce. Đây là sự đánh đổi (trade-off / 트레이드오프) phải quyết định theo loại chính sách (policy / 정책), không có default đúng cho mọi quy tắc (rule / 규칙).

Chính sách (policy / 정책) engine cần hết thời gian chờ (timeout / 타임아웃) nhỏ hợp lý, HA, telemetry và staged rollout. Một webhook toàn cục (global / 전역) chậm có thể làm người dùng nghĩ “Kubernetes API chậm” trong khi read đường dẫn (path / 경로) vẫn bình thường.

## 17. Watch biến polling thành sự kiện (event / 이벤트) stream nhưng không xóa nhu cầu resync

Controller thường `list` để có snapshot rồi `watch` thay đổi. Watch có thể bị ngắt; sự kiện (event / 이벤트) có thể được coalesced hoặc controller restart. Vì vậy controller không nên dựa vào giả định (assumption / 가정) “tôi sẽ nhận chính xác từng sự kiện (event / 이벤트) một lần”.

Reconciliation mẫu (pattern / 패턴) mạnh vì sự kiện (event / 이벤트) chỉ là **hint rằng trạng thái (state / 상태) có thể cần xử lý**. Controller đọc hiện tại (current / 현재) desired/actual trạng thái (state / 상태) và hội tụ. Đây là lý do idempotency quan trọng hơn event-processing chính xác từng message.

Khi controller backlog lớn, sự kiện (event / 이벤트) delivery vẫn tiếp tục nhưng reconciliation độ trễ (latency / 지연 시간) tăng. chỉ số (metric / 지표) hàng đợi (queue / 큐) độ sâu (depth / 깊이)/reconcile duration/lỗi (error / 오류) tỷ lệ (rate / 비율) của controller trở thành bằng chứng (evidence / 증거) quan trọng.

## 18. công việc (work / 작업) hàng đợi (queue / 큐) và backoff bảo vệ điều khiển (control / 제어) plane khỏi hot vòng lặp (loop / 루프)

Nếu reconcile thất bại (failure / 실패) ngay lập tức được thử lại (retry / 재시도) không giới hạn, một đối tượng (object / 객체) lỗi có thể tạo hot vòng lặp (loop / 루프), làm API/provider bị spam và che tải công việc (workload / 워크로드) khác. Controller thường cần tỷ lệ (rate / 비율) limit/backoff và phân biệt transient thất bại (failure / 실패) với invalid desired trạng thái (state / 상태).

Ví dụ bên ngoài (external / 외부) cloud API đang outage: thử lại (retry / 재시도) có bounded exponential backoff hợp lý hơn hàng nghìn yêu cầu (request / 요청)/giây. Ngược lại spec invalid nên surface điều kiện (condition / 조건) rõ để người dùng (user / 사용자) sửa, không thử lại (retry / 재시도) vô hạn như thể phụ thuộc (dependency / 의존성) sẽ tự hồi.

Một controller tốt không chỉ “eventually reconcile”; nó phải reconcile theo cách không tự khuếch đại outage.

## 19. API máy chủ (server / 서버) saturation có thể đến từ máy khách (client / 클라이언트) hành xử xấu

Điều khiển (control / 제어) plane có finite CPU/bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소) bandwidth và yêu cầu (request / 요청) ngân sách (budget / 예산). máy khách (client / 클라이언트) danh sách (list / 목록) toàn bộ cluster quá thường xuyên, controller tạo cập nhật (update / 업데이트) storm hoặc automation thử lại (retry / 재시도) không backoff có thể gây pressure.

Khi API độ trễ (latency / 지연 시간) tăng, cần phân dimension read/ghi (write / 쓰기), tài nguyên (resource / 자원) kind, máy khách (client / 클라이언트) định danh (identity / 식별자)/user-agent, yêu cầu (request / 요청) tỷ lệ (rate / 비율) và etcd/lưu trữ (storage / 저장소) độ trễ (latency / 지연 시간). quy mô (scale / 규모) điều khiển (control / 제어) plane có thể cần nhưng trước hết tìm noisy máy khách (client / 클라이언트)/vòng điều khiển (control loop / 제어 루프).

Nền tảng (platform / 플랫폼) controller nên dùng informer/bộ nhớ đệm (cache / 캐시)/watch phù hợp thay vì polling full danh sách (list / 목록) ngắn chu kỳ nếu không cần.

## 20. Upgrade cluster là tính tương thích (compatibility / 호환성) bài toán (problem / 문제) nhiều chiều

Điều khiển (control / 제어) plane, kubelet, API phiên bản (version / 버전), admission webhook, CRD và controller/operator đều có vòng đời (lifecycle / 생명주기) phiên bản (version / 버전). “Cluster upgrade thành công” không chỉ là API máy chủ (server / 서버) lên phiên bản (version / 버전) mới; tải công việc (workload / 워크로드)/controller cũ có thể dùng API đã deprecated hoặc các giả định (assumptions / 가정들) cũ.

Môi trường vận hành (production / 운영 환경) upgrade cần inventory API usage, tính tương thích (compatibility / 호환성) của extension/controller, staged nút (node / 노드)/control-plane rollout theo hỗ trợ (support / 지원) ma trận (matrix / 행렬) và quay lui (rollback / 롤백)/khôi phục (recovery / 복구) plan. CRD conversion/admission thành phần (component / 컴포넌트) đặc biệt nhạy vì chúng nằm trên API đường dẫn (path / 경로).

Không cần thuộc mọi phiên bản (version / 버전) quy tắc (rule / 규칙) trong chapter này; bất biến (invariant / 불변식) là **phiên bản (version / 버전) skew phải nằm trong tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약) được hỗ trợ (support / 지원) và được kiểm thử (test / 테스트) trước môi trường vận hành (production / 운영 환경)**.

## 21. cấp cao (senior / 시니어) walkthrough: deploy toàn cluster bị treo nhưng ứng dụng (application / 애플리케이션) traffic vẫn khỏe

Giả sử nhiều nhóm (team / 팀) cùng báo `kubectl apply` hết thời gian chờ (timeout / 타임아웃), GitOps controller backlog tăng, nhưng người dùng (user / 사용자) traffic ứng dụng (application / 애플리케이션) vẫn bình thường. Đây là clue điều khiển (control / 제어) plane ghi (write / 쓰기) đường dẫn (path / 경로) lỗi chứ không phải mặt phẳng dữ liệu (data plane / 데이터 플레인) outage.

Kiểm tra API yêu cầu (request / 요청) độ trễ (latency / 지연 시간) theo verb, admission webhook độ trễ (latency / 지연 시간)/lỗi (error / 오류), etcd/lưu trữ (storage / 저장소), controller máy khách (client / 클라이언트) thử lại (retry / 재시도). Nếu một validating webhook mới deploy có độ trễ (latency / 지연 시간) 8–10 giây và mọi create/cập nhật (update / 업데이트) đều đi qua nó, gốc (root / 루트) tầng (layer / 계층) khá rõ.

Mitigation có thể quay lui (rollback / 롤백)/phạm vi (scope / 범위) lại webhook theo chính sách (policy / 정책); không nên restart ứng dụng (application / 애플리케이션) pods vì chúng không nằm trên thất bại (failure / 실패) đường dẫn (path / 경로). Đây là giá trị của control-plane/data-plane separation trong lập luận (reasoning / 추론).

## 22. Finalizer biến delete thành giao thức (protocol / 프로토콜), không phải một thao tác tức thời

Khi đối tượng (object / 객체) có cleanup bên ngoài cluster — cloud cơ sở dữ liệu (database / 데이터베이스), bộ cân bằng tải (load balancer / 로드 밸런서), DNS bản ghi (record / 레코드), volume hoặc secret — xóa API đối tượng (object / 객체) ngay có thể làm mất dấu tài nguyên (resource / 자원) cần cleanup. Finalizer cho phép đối tượng (object / 객체) đi vào trạng thái terminating trong khi controller hoàn tất side tác động (effect / 효과) rồi mới cho deletion kết thúc.

Bất biến (invariant / 불변식) là: **đừng xóa bản ghi (record / 레코드) điều phối trước khi hoàn tất cleanup bắt buộc**. Nhưng finalizer cũng tạo dạng thất bại (failure mode / 실패 모드): controller chết, credential mất hoặc provider outage có thể làm đối tượng (object / 객체) kẹt `Terminating` vô thời hạn.

Force-remove finalizer chỉ nên làm khi operator hiểu orphan nào có thể còn lại và khôi phục (recovery / 복구) đường dẫn (path / 경로) là gì. “Xóa được đối tượng (object / 객체)” không đồng nghĩa bên ngoài (external / 외부) tài nguyên (resource / 자원) đã biến mất.

## 23. đơn vị sở hữu (owner / 오너) tham chiếu (reference / 참조) và garbage collection encode vòng đời (lifecycle / 생명주기) đồ thị (graph / 그래프)

Kubernetes có đối tượng (object / 객체) đồ thị (graph / 그래프): triển khai (deployment / 배포) sở hữu ReplicaSet, ReplicaSet sở hữu Pod. đơn vị sở hữu (owner / 오너) tham chiếu (reference / 참조) cho garbage collector biết tài nguyên (resource / 자원) con có vòng đời (lifecycle / 생명주기) gắn với đơn vị sở hữu (owner / 오너) nào.

Đây là khác biệt với label/selector. Label thể hiện quan hệ chọn động; đơn vị sở hữu (owner / 오너) tham chiếu (reference / 참조) thể hiện quyền sở hữu (ownership / 소유권)/vòng đời (lifecycle / 생명주기). Dùng nhầm hai khái niệm dẫn tới bug như tài nguyên (resource / 자원) con không được cleanup hoặc bị xóa ngoài ý muốn.

Operator tự viết cần nghĩ quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프) trước khi create child tài nguyên (resource / 자원). Nếu một bên ngoài (external / 외부) tài nguyên (resource / 자원) không thể biểu diễn bằng đơn vị sở hữu (owner / 오너) tham chiếu (reference / 참조), controller phải tự giữ ánh xạ (mapping / 매핑)/định danh (identity / 식별자) đủ bền để reconcile/delete an toàn.

## 24. Leader election giảm duplicate active controller nhưng không tự tạo fencing

Nhiều replica controller thường dùng lease/leader election để chỉ một instance active cho một responsibility nhất định. Nhưng mạng (network / 네트워크) partition, pause dài hoặc delayed actor có thể tạo thời điểm old leader vẫn tiếp tục side tác động (effect / 효과) dù lease đã mất.

Với hành động (action / 동작) chỉ ghi Kubernetes API, optimistic tính đồng thời (concurrency / 동시성) có thể giúp reject stale ghi (write / 쓰기). Với hệ thống bên ngoài (external system / 외부 시스템) không kiểm tra fencing đơn vị từ (token / 토큰), leader election một mình có thể chưa đủ cho thao tác (operation / 연산) nguy hiểm.

Đây là ranh giới (boundary / 경계) nơi DevOps nên chuyển sang [leases, fencing và split-brain](../../computer_science/06_networks_distributed_systems/advanced/02_leases_fencing_tokens_and_split_brain_prevention.md). Operational lesson là: **“có leader election” không tự chứng minh side tác động (effect / 효과) bên ngoài (external / 외부) không thể bị duplicate/stale actor thực hiện**.

## 25. Informer bộ nhớ đệm (cache / 캐시) tăng quy mô (scale / 규모) nhưng tạo staleness cần được chấp nhận có chủ đích

Controller thường đọc từ cục bộ (local / 로컬) bộ nhớ đệm (cache / 캐시)/informer thay vì gọi API máy chủ (server / 서버) trực tiếp cho mọi reconcile. Điều này giảm tải (load / 로드) và độ trễ (latency / 지연 시간), nhưng bộ nhớ đệm (cache / 캐시) có thể chậm hơn authoritative API trạng thái (state / 상태) một khoảng ngắn.

Controller vì vậy phải được viết theo eventual reconciliation, không dựa vào giả định (assumption / 가정) “vừa ghi xong thì bộ nhớ đệm (cache / 캐시) chắc chắn đã thấy ngay”. Nếu một bất biến (invariant / 불변식) cần read-after-write mạnh hơn, có thể phải dùng phản hồi (response / 응답) của ghi (write / 쓰기), direct read có chọn lọc hoặc generation/resourceVersion lô-gic (logic / 논리) phù hợp.

Nhiều bug controller xuất hiện khi nhà phát triển (developer / 개발자) vô tình trộn ngữ nghĩa (semantics / 의미론) của bộ nhớ đệm (cache / 캐시) với ngữ nghĩa (semantics / 의미론) của cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션).

## 26. Status điều kiện (condition / 조건) phải là machine-readable đặc tả hợp đồng (contract / 계약), không phải log mini

Một CRD có `status.message = "something failed"` chưa đủ cho automation. điều kiện (condition / 조건) tốt nên có kiểu (type / 타입) ổn định, boolean/status, reason có taxonomy hữu hạn, observed generation và timestamp hữu ích.

Bên tiêu thụ (consumer / 소비자) cần phân biệt thất bại (failure / 실패) transient với terminal-invalid-spec; degraded nhưng usable với not-ready; phụ thuộc (dependency / 의존성) pending với chính sách (policy / 정책) denied. Nếu mọi lỗi đều thành `Ready=False`, nền tảng (platform / 플랫폼) người dùng (user / 사용자) phải đọc controller log để hiểu lớp trừu tượng (abstraction / 추상화) — đặc tả hợp đồng (contract / 계약) đã rò.

Status nên trả lời “controller đã observe intent nào, bất biến (invariant / 불변식) nào đang đạt, bất biến (invariant / 불변식) nào chưa và vì lý do loại nào”. Chi tiết dài vẫn có thể ở sự kiện (event / 이벤트)/log.

## 27. CRD lược đồ (schema / 스키마) evolution là API evolution thật sự

CRD không chỉ là YAML tùy ý. Khi nhiều máy khách (client / 클라이언트)/controller dùng nó, trường dữ liệu (field / 필드) rename, default thay đổi, ngữ nghĩa (semantic / 의미적) đổi hoặc phiên bản (version / 버전) conversion sai đều có thể phá môi trường vận hành (production / 운영 환경).

Một phiên bản (version / 버전) mới cần tính tương thích (compatibility / 호환성) chiến lược (strategy / 전략): trường dữ liệu (field / 필드) cũ được giữ/deprecate bao lâu, default cũ/new khác nhau thế nào, đối tượng (object / 객체) stored phiên bản (version / 버전) nào, conversion có reversible không và controller nào hỗ trợ (support / 지원) phiên bản (version / 버전) nào.

Nếu conversion webhook nằm trên API read/ghi (write / 쓰기) đường dẫn (path / 경로), availability của nó cũng trở thành control-plane phụ thuộc (dependency / 의존성). nền tảng (platform / 플랫폼) CRD vì vậy cần cùng discipline versioning/canary/quay lui (rollback / 롤백) như API công khai (public API / 공개 API).

## 28. Control-plane fairness cần bảo vệ yêu cầu (request / 요청) quan trọng khi overload

Không phải API yêu cầu (request / 요청) nào có cùng giá trị. Health/điều khiển (control / 제어) traffic, scheduler/controller hành động (action / 동작) và bulk automation có thể tranh cùng control-plane sức chứa (capacity / 용량). Nếu một máy khách (client / 클라이언트) gửi burst danh sách (list / 목록)/cập nhật (update / 업데이트) lớn, yêu cầu (request / 요청) trọng yếu (critical / 중요) có thể bị hàng đợi (queue / 큐) dài.

Operational lập luận (reasoning / 추론) nên phân loại caller/verb/tài nguyên (resource / 자원) và xem hàng đợi (queue / 큐)/rejection theo lớp (class / 클래스) khi điều khiển (control / 제어) plane pressure. tỷ lệ (rate / 비율) limit phía máy khách (client / 클라이언트), bounded tính đồng thời (concurrency / 동시성) và ưu tiên/fairness ở API đường dẫn (path / 경로) giúp tránh noisy automation làm toàn cluster mất khả năng điều khiển.

Điều này nối Kubernetes với multi-tenancy: fairness của dùng chung (shared / 공유) điều khiển (control / 제어) plane là độ tin cậy (reliability / 신뢰성) đặc tả hợp đồng (contract / 계약), không chỉ tuning hiệu năng (performance / 성능).

> **Bàn giao:** Sau **28. Control-plane fairness cần bảo vệ yêu cầu (request / 요청) quan trọng khi overload**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 kubernetes workloads networking storage and resources](./01_kubernetes_workloads_networking_storage_and_resources.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
