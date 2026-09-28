# GitOps: desired trạng thái (state / 상태) trong Git và reconciliation liên tục

> **Mạch đọc:** Đọc **GitOps: desired trạng thái (state / 상태) trong Git và reconciliation liên tục** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. GitOps giải vấn đề “ai đã thay cluster?”** sang **2. Pull mô hình (model / 모델) giảm credential exposure**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. GitOps giải vấn đề “ai đã thay cluster?”

CI/CD truyền thống có thể dùng chuỗi xử lý (pipeline / 파이프라인) giữ credential rồi chạy `kubectl apply`. Mô hình này hoạt động, nhưng push-based triển khai (deployment / 배포) khiến chuỗi xử lý (pipeline / 파이프라인) trực tiếp thay remote trạng thái (state / 상태). GitOps đảo chiều: desired trạng thái (state / 상태) được lần ghi nhận (commit / 커밋) vào repository; tác nhân (agent / 에이전트)/controller gần cluster watch repository và reconcile actual trạng thái (state / 상태).

```text
change request → Git review → desired state commit
                           ↓
                    GitOps controller
                           ↓ compare
                    cluster actual state
                           ↓ reconcile
                    Kubernetes/resources
```

Mục tiêu không phải dùng Git vì Git “thần kỳ”, mà là tạo nguồn chuẩn (source of truth / 정본) có lịch sử (history / 이력), rà soát (review / 검토) và một reconciliation vòng lặp (loop / 루프) rõ quyền sở hữu (ownership / 소유권).

## 2. Pull mô hình (model / 모델) giảm credential exposure

Trong pull-based GitOps, CI hiện vật bản dựng (build artifact / 빌드 산출물) và cập nhật desired trạng thái (state / 상태)/bản phát hành (release / 릴리스) siêu dữ liệu (metadata / 메타데이터) nhưng không nhất thiết cầm credential cluster quyền rộng. Controller trong môi trường (environment / 환경) có permission phù hợp để apply.

Điều này cải thiện ranh giới bảo mật (security boundary / 보안 경계) nhưng không tự động an toàn. Nếu repository ghi (write / 쓰기) permission quá rộng, attacker sửa desired trạng thái (state / 상태) vẫn có thể điều khiển cluster. Git permission trở thành một phần môi trường vận hành (production / 운영 환경) authorization mô hình (model / 모델).

## 3. nguồn chuẩn (source of truth / 정본) phải có quyền sở hữu (ownership / 소유권) rõ

Một trường dữ liệu (field / 필드) không thể đồng thời được GitOps controller, HPA và người dùng `kubectl edit` quản theo ý khác nhau mà không có xung đột (conflict / 충돌). Ví dụ HPA sở hữu replica count động, nên GitOps cấu hình (config / 설정) cần tránh liên tục kéo replicas về con số tĩnh không phù hợp.

Mỗi tầng (layer / 계층) cần quyết định trường dữ liệu (field / 필드) quyền sở hữu (ownership / 소유권). Git quản cấu trúc/chính sách (policy / 정책) ổn định; thời gian chạy (runtime / 런타임) controller quản trạng thái (state / 상태) động theo đặc tả hợp đồng (contract / 계약). Nếu không, reconciliation tạo oscillation.

## 4. Drift detection là năng lực (capability / 역량) cốt lõi

Vì controller so desired với actual, thay đổi trực tiếp cluster sẽ xuất hiện drift và có thể bị revert. Đây là lợi thế lớn nhưng cũng ảnh hưởng emergency thao tác (operation / 연산).

Nếu operator sửa live trạng thái (state / 상태) để chữa sự cố (incident / 인시던트), GitOps có thể vài giây sau ghi đè. Quy trình emergency cần biết pause/suspend reconciliation, hoặc tốt hơn là đưa thay đổi (change / 변경) qua nguồn chuẩn (source of truth / 정본) đủ nhanh. Sau sự cố (incident / 인시던트), mọi emergency patch phải được reconcile ngược về Git để không tạo lịch sử giả.

## 5. Promotion mô hình (model / 모델)

Có hai thứ thường được promote: sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) và cấu hình (configuration / 구성). Một bản phát hành (release / 릴리스) tốt cập nhật ảnh (image / 이미지) digest/phiên bản (version / 버전) trong desired-state repo. Promotion từ staging đến môi trường vận hành (production / 운영 환경) không nên rebuild ảnh (image / 이미지); nó thay tham chiếu (reference / 참조) đến cùng sản phẩm tạo ra (artifact / 산출물) đã được kiểm chứng.

Có thể dùng repository/branch/directory khác nhau cho môi trường (environment / 환경). Không có một bố cục (layout / 레이아웃) duy nhất đúng. ranh giới (boundary / 경계) cần phản ánh quyền sở hữu (ownership / 소유권), rà soát (review / 검토) permission và blast radius.

## 6. Reconciliation interval và eventual hành vi (behavior / 동작)

Git lần ghi nhận (commit / 커밋) không đồng nghĩa cluster thay ngay. Controller phải fetch, kết xuất (render / 렌더링), diff, apply rồi downstream controller tiếp tục reconcile. Có nhiều delay nối tiếp.

Khi người dùng (user / 사용자) hỏi “merge rồi sao môi trường vận hành (production / 운영 환경) chưa đổi?”, cần xem GitOps controller đã thấy revision chưa, kết xuất (render / 렌더링) có thành công không, apply có bị chính sách (policy / 정책) chặn không, tải công việc (workload / 워크로드) controller đã rollout chưa và readiness/xác minh (verification / 확인) thế nào.

## 7. Sync success không bằng bản phát hành (release / 릴리스) success

GitOps UI xanh có thể chỉ nghĩa manifests đã apply và resources đạt điều kiện (condition / 조건) controller mong chờ. nghiệp vụ (business / 비즈니스) chỉ số (metric / 지표) vẫn có thể xấu. Vì vậy progressive delivery/xác minh (verification / 확인) nên nối GitOps trạng thái (state / 상태) với khả năng quan sát (observability / 관측 가능성) tín hiệu (signal / 신호).

Điều khiển (control / 제어) plane chứng minh trạng thái (state / 상태) convergence; data-plane telemetry chứng minh người dùng (user / 사용자) kết quả (outcome / 결과).

## 8. Secret trong GitOps

Git repository không nên chứa plaintext môi trường vận hành (production / 운영 환경) secret. Có nhiều mẫu (pattern / 패턴): encrypted secret tệp (file / 파일), bên ngoài (external / 외부) secret tham chiếu (reference / 참조), secret-store CSI/controller hoặc generated short-lived credential. Lựa chọn phụ thuộc trust mô hình (model / 모델).

Điểm cần giữ là Git lưu intent/tham chiếu (reference / 참조) hoặc ciphertext phù hợp, còn key vòng đời (lifecycle / 생명주기) và kiểm soát truy cập (access control / 접근 제어) nằm ở bảo mật (security / 보안) hệ thống (system / 시스템). “Private repository” không phải lý do đủ để lần ghi nhận (commit / 커밋) plaintext secret.

## 9. Rendering và template độ phức tạp (complexity / 복잡도)

Helm/Kustomize/template làm giảm duplicate nhưng có thể biến desired trạng thái (state / 상태) thành chương trình khó dự đoán. Nếu phải chạy nhiều tầng (layer / 계층) templating mới biết manifest cuối cùng, rà soát (review / 검토) chất lượng (quality / 품질) giảm.

Nền tảng (platform / 플랫폼) nên giữ lớp trừu tượng (abstraction / 추상화) đủ cao nhưng đầu ra (output / 출력) inspectable. Reviewer cần thấy effective diff hoặc có tooling kết xuất (render / 렌더링) đáng tin. lớp trừu tượng (abstraction / 추상화) không được làm chuỗi nhân quả (causal chain / 인과 사슬) biến mất.

## 10. GitOps với hạ tầng (infrastructure / 인프라)

GitOps không giới hạn Kubernetes. Một controller có thể reconcile cloud tài nguyên (resource / 자원)/IaC từ Git. Tuy nhiên phải tránh hai vòng điều khiển (control loop / 제어 루프) cùng sở hữu tài nguyên (resource / 자원). Nếu Terraform chuỗi xử lý (pipeline / 파이프라인) và Crossplane/operator cùng quản một cơ sở dữ liệu (database / 데이터베이스) trường dữ liệu (field / 필드), drift vòng lặp (loop / 루프) có thể liên tục ghi đè.

## 11. thất bại (failure / 실패) scenario

Giả sử môi trường vận hành (production / 운영 환경) đang sync revision R, lần ghi nhận (commit / 커밋) R+1 đổi triển khai (deployment / 배포) nhưng controller báo `OutOfSync`. Trước hết kiểm tra controller có fetch repo/auth được không. Nếu kết xuất (render / 렌더링) thất bại (fail / 실패), sửa nguồn (source / 소스)/template. Nếu diff tồn tại nhưng apply bị deny, xem admission/chính sách (policy / 정책)/RBAC. Nếu apply thành công nhưng app chưa healthy, rời GitOps tầng (layer / 계층) và điều tra Kubernetes/tải công việc (workload / 워크로드)/data-plane.

Giữ tầng (layer / 계층) ranh giới (boundary / 경계) giúp không biến mọi lỗi thành “ArgoCD lỗi”.

## 12. cấp cao (senior / 시니어) ghi chú (note / 노트): GitOps là operational đặc tả hợp đồng (contract / 계약)

GitOps có giá trị khi tạo đặc tả hợp đồng (contract / 계약): mọi desired môi trường vận hành (production / 운영 환경) thay đổi (change / 변경) có lịch sử (history / 이력); reconciliation định danh (identity / 식별자) rõ; drift observable; manual thay đổi (change / 변경) có chính sách (policy / 정책); promotion giữ sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자); quay lui (rollback / 롤백)/roll-forward có thể thao tác bằng revision có kiểm soát.

Nếu nhóm (team / 팀) vẫn thường xuyên `kubectl edit`, controller hay bị disable và nguồn chuẩn (source of truth / 정본) không phản ánh môi trường vận hành (production / 운영 환경), tổ chức chỉ có GitOps công cụ (tool / 도구) chứ chưa có GitOps operating mô hình (model / 모델).

## 13. Git là nguồn (source / 소스) of desired trạng thái (state / 상태), không phải nguồn (source / 소스) of toàn bộ reality

Git có thể nói tải công việc (workload / 워크로드) **nên** chạy ảnh (image / 이미지) digest D với cấu hình (config / 설정) C. Nó không chứa toàn bộ trạng thái thời gian chạy (runtime / 런타임) như pod nào đang crash, HPA vừa quy mô (scale / 규모) bao nhiêu, cloud bộ cân bằng tải (load balancer / 로드 밸런서) đã provision xong chưa hay cơ sở dữ liệu (database / 데이터베이스) đang replication lag.

Vì vậy câu “Git là nguồn chuẩn (source of truth / 정본)” cần đọc chính xác hơn: Git là nguồn chuẩn (source of truth / 정본) cho **intent thuộc quyền sở hữu (ownership / 소유권) của GitOps**. Actual trạng thái (state / 상태) vẫn phải được quan sát từ điều khiển (control / 제어) plane/mặt phẳng dữ liệu (data plane / 데이터 플레인). Khi sự cố (incident / 인시던트) xảy ra, không được kết luận “Git đúng nên môi trường vận hành (production / 운영 환경) phải đúng”.

## 14. trường dữ liệu (field / 필드) quyền sở hữu (ownership / 소유권) phải được thiết kế như API quyền sở hữu (ownership / 소유권)

Kubernetes và các controller có thể cùng chạm một đối tượng (object / 객체). Một số cơ chế apply có siêu dữ liệu (metadata / 메타데이터) trường dữ liệu (field / 필드) manager giúp theo dõi ai sở hữu trường dữ liệu (field / 필드) nào, nhưng công cụ (tool / 도구) không thể tự quyết định quyền sở hữu (ownership / 소유권) nghiệp vụ (business / 비즈니스).

Ví dụ triển khai (deployment / 배포) template, ảnh (image / 이미지) và chính sách (policy / 정책) có thể thuộc GitOps; replica count thuộc HPA; annotation do dịch vụ (service / 서비스) mesh controller inject; status thuộc tải công việc (workload / 워크로드) controller. Nếu Git kết xuất (render / 렌더링) cả trường dữ liệu (field / 필드) động mà không có lý do, reconciliation có thể liên tục overwrite controller khác.

Khi thấy đối tượng (object / 객체) “cứ đổi qua đổi lại”, hãy kiểm tra kiểm tra (audit / 감사)/sự kiện (event / 이벤트)/managed-field bằng chứng (evidence / 증거) và vẽ bảng quyền sở hữu (ownership / 소유권). Đây thường là control-loop xung đột (conflict / 충돌) chứ không phải random drift.

## 15. quay lui (rollback / 롤백) Git revision không quay lui (rollback / 롤백) bên ngoài (external / 외부) trạng thái (state / 상태)

Revert lần ghi nhận (commit / 커밋) có thể đưa manifest về phiên bản trước, nhưng không chắc đảo được cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션), message lược đồ (schema / 스키마), bên ngoài (external / 외부) side tác động (effect / 효과) hoặc cloud tài nguyên (resource / 자원) đã mutate. Git lịch sử (history / 이력) chỉ phiên bản (version / 버전) hóa intent; bên ngoài (external / 외부) trạng thái (state / 상태) có vòng đời (lifecycle / 생명주기) riêng.

Do đó GitOps quay lui (rollback / 롤백) phải dùng cùng tính tương thích (compatibility / 호환성) lập luận (reasoning / 추론) như CI/CD quay lui (rollback / 롤백). Nếu bản phát hành (release / 릴리스) N+1 đã ghi dữ liệu (data / 데이터) mà N không đọc được, revert ảnh (image / 이미지) tham chiếu (reference / 참조) có thể làm outage nặng hơn. Expand-and-contract, forward-compatible lược đồ (schema / 스키마) và roll-forward đường dẫn (path / 경로) vẫn cần.

## 16. Promotion repo có thể tạo race nếu nhiều actor sửa cùng môi trường (environment / 환경)

Hai automation cùng mở thay đổi (change / 변경) cho môi trường vận hành (production / 운영 환경) có thể từng pass kiểm thử (test / 테스트) riêng nhưng khi merge liên tiếp lại tạo combination chưa được verify. Ví dụ bản phát hành (release / 릴리스) A nâng ứng dụng (application / 애플리케이션), bản phát hành (release / 릴리스) B đổi cấu hình (config / 설정)/phụ thuộc (dependency / 의존성); mỗi PR xanh trên cơ sở (base / 기반) cũ nhưng môi trường vận hành (production / 운영 환경) nhận A+B.

Chuỗi xử lý (pipeline / 파이프라인) nên verify effective desired trạng thái (state / 상태) gần với revision cuối sẽ reconcile, hoặc serialize/rerun xác minh (verification / 확인) khi cơ sở (base / 기반) thay đổi. Đây là cùng vấn đề stale plan ở IaC: bằng chứng (evidence / 증거) phải gắn với trạng thái (state / 상태) gần trạng thái (state / 상태) thực sự được apply.

## 17. Emergency thay đổi (change / 변경) cần một giao thức (protocol / 프로토콜) trước sự cố (incident / 인시던트)

Nếu GitOps controller tự-heal mạnh, live patch có thể bị revert đúng lúc operator đang mitigate. Nhưng tắt controller tùy tiện cũng làm mất an toàn (safety / 안전) net và tạo drift không visible.

Nền tảng (platform / 플랫폼) nên định nghĩa break-glass luồng (flow / 흐름): ai được suspend reconciliation, phạm vi (scope / 범위) nào, trong bao lâu, thay đổi (change / 변경) live được ghi ở đâu, khi nào back-port vào Git và điều kiện resume. Sau resume cần verify controller không “undo” mitigation theo desired trạng thái (state / 상태) cũ.

## 18. Repository bảo mật (security / 보안) là môi trường vận hành (production / 운영 환경) bảo mật (security / 보안)

Khi Git lần ghi nhận (commit / 커밋) có thể dẫn tới môi trường vận hành (production / 운영 환경) reconciliation, branch protection, reviewer permission, bot đơn vị từ (token / 토큰), webhook/controller credential và phụ thuộc (dependency / 의존성) của rendering chuỗi xử lý (pipeline / 파이프라인) đều trở thành part of môi trường vận hành (production / 운영 환경) trust chuỗi (chain / 사슬).

Một repository private nhưng đơn vị từ (token / 토큰) bot bị lộ vẫn không an toàn. Ngược lại, lần ghi nhận (commit / 커밋) signing đơn lẻ cũng không đủ nếu signer có quyền quá rộng hoặc controller không verify chính sách (policy / 정책). bảo mật (security / 보안) chapter sẽ đào sâu nguyên tắc định danh (identity / 식별자) + provenance + authorization thay vì dựa vào một điều khiển (control / 제어) đơn lẻ.

## 19. cấp cao (senior / 시니어) walkthrough: trạng thái cứ bị đổi ngược sau vài phút

Giả sử operator tăng replicas từ 10 lên 20 để mitigate traffic spike. Vài phút sau nó quay về 10. Có ít nhất ba possibility: GitOps đang reconcile spec 10; HPA đang tính desired 10; hoặc một automation khác patch trường dữ liệu (field / 필드).

Đừng tiếp tục `kubectl scale` nhiều lần. Hãy xác định actor từ sự kiện (event / 이벤트)/kiểm tra (audit / 감사)/trường dữ liệu (field / 필드) quyền sở hữu (ownership / 소유권), rồi sửa desired đơn vị sở hữu (owner / 오너) đúng. Nếu HPA sở hữu replica, thay chính sách (policy / 정책)/chỉ số (metric / 지표)/minimum phù hợp. Nếu GitOps sở hữu, emergency thay đổi (change / 변경) phải đi qua Git hoặc suspend theo giao thức (protocol / 프로토콜).

Đây là lợi ích của GitOps khi được vận hành đúng: drift không chỉ bị sửa, mà còn buộc tổ chức phải làm rõ **ai có quyền định nghĩa trạng thái (state / 상태) nào**.

## 20. Revision observed, revision applied và revision serving traffic là ba trạng thái (state / 상태) khác nhau

Một GitOps controller có thể đã fetch lần ghi nhận (commit / 커밋) `R2`, kết xuất (render / 렌더링) thành công và ghi tài nguyên (resource / 자원) vào API nhưng tải công việc (workload / 워크로드) vẫn đang phục vụ phần lớn traffic bằng sản phẩm tạo ra (artifact / 산출물) từ `R1`. Nếu chỉ lưu một nhãn “Synced R2”, operator dễ nghĩ môi trường vận hành (production / 운영 환경) đã hoàn tất bản phát hành (release / 릴리스).

Một chuỗi nhân quả (causal chain / 인과 사슬) hữu ích là:

```text
Git revision observed
→ rendered desired state
→ API objects applied
→ workload controller observed generation
→ new replicas Ready
→ routing đưa traffic tới replica mới
→ telemetry xác nhận outcome của artifact/config mới
```

Bản phát hành (release / 릴리스) siêu dữ liệu (metadata / 메타데이터) nên cho phép nối các trạng thái (state / 상태) này. Điều này đặc biệt quan trọng khi quay lui (rollback / 롤백) hoặc sự cố (incident / 인시던트) xảy ra giữa rollout: nguồn (source / 소스) desired trạng thái (state / 상태) có thể là R2 nhưng actual fleet là mixture R1/R2.

## 21. Git/repository outage ảnh hưởng khả năng đổi trạng thái (state / 상태), không nhất thiết traffic hiện tại

Nếu repository hoặc Git provider down, controller có thể không fetch revision mới nhưng tải công việc (workload / 워크로드) đang chạy vẫn khỏe. Đây là control-plane phụ thuộc (dependency / 의존성) giống registry/cloud API: mặt phẳng dữ liệu (data plane / 데이터 플레인) có thể tiếp tục nhưng deploy, khôi phục (recovery / 복구) hoặc quy mô (scale / 규모) đường dẫn (path / 경로) liên quan desired trạng thái (state / 상태) bị giới hạn.

Runbook cần biết controller giữ bộ nhớ đệm (cache / 캐시)/revision cuối ra sao và hành vi (behavior / 동작) khi không reach repo: giữ last-known desired trạng thái (state / 상태), thất bại (fail / 실패) closed hay liên tục thử lại (retry / 재시도). thử lại (retry / 재시도) fan-out từ hàng trăm cluster/controller còn có thể gây thundering herd khi Git provider hồi phục.

Do đó Git availability cần được đánh giá theo **thay đổi (change / 변경)/khôi phục (recovery / 복구) năng lực (capability / 역량)**, không chỉ “ứng dụng (application / 애플리케이션) uptime hiện tại”.

## 22. Rendering phải deterministic đủ để revision có nghĩa

Nếu cùng Git revision kết xuất (render / 렌더링) ra manifest khác vì chart phụ thuộc (dependency / 의존성) `latest`, remote lookup mutable, môi trường (environment / 환경) variable ngoài nguồn (source / 소스) hoặc plugin phiên bản (version / 버전) khác, lần ghi nhận (commit / 커밋) SHA không còn là định danh (identity / 식별자) đầy đủ của desired trạng thái (state / 상태).

GitOps tốt cố gắng phiên bản (version / 버전) hóa rendering inputs: chart/mô-đun (module / 모듈) phụ thuộc (dependency / 의존성), plugin/công cụ (tool / 도구) phiên bản (version / 버전), values và bên ngoài (external / 외부) tham chiếu (reference / 참조) quan trọng. Nếu đầu ra (output / 출력) cần remote dữ liệu (data / 데이터), phải biết remote đầu vào (input / 입력) đó thuộc đặc tả hợp đồng (contract / 계약) nào và có được snapshot/pin không.

Mô hình tư duy (mental model / 사고 모델) giống reproducible bản dựng (build / 빌드): **desired-state sản phẩm tạo ra (artifact / 산출물)** cũng nên có đầu vào (input / 입력) closure đủ rõ. “Git không đổi nhưng cluster diff đổi” là dấu hiệu có mutable đầu vào (input / 입력) ngoài Git hoặc controller/hành vi thời gian chạy (runtime behavior / 런타임 동작) thay đổi.

## 23. Prune/delete có rủi ro (risk / 위험) lớp (class / 클래스) khác apply/cập nhật (update / 업데이트)

GitOps thường có khả năng xóa tài nguyên (resource / 자원) khi đối tượng (object / 객체) biến mất khỏi desired nguồn (source / 소스). Đây là convergence hợp lý nhưng destructive ngữ nghĩa (semantics / 의미론) khác create/cập nhật (update / 업데이트). Một rename/move sai đường dẫn (path / 경로) hoặc selector phạm vi (scope / 범위) rộng có thể làm controller hiểu tài nguyên (resource / 자원) không còn được mong muốn và prune hàng loạt.

Trọng yếu (critical / 중요) tài nguyên (resource / 자원) cần protection phù hợp: rà soát (review / 검토) effective diff, deletion chính sách (policy / 정책)/retention, finalizer hoặc tường minh (explicit / 명시적) allow-prune tùy kiến trúc (architecture / 아키텍처). Nhưng protection không được biến thành tài nguyên (resource / 자원) vĩnh viễn không ai xóa được.

Cấp cao (senior / 시니어) rà soát (review / 검토) nên highlight **đối tượng (object / 객체) leaving desired set** như một chuyển tiếp trạng thái (state transition / 상태 전이) riêng, không chỉ nhìn số dòng Git bị xóa.

## 24. phụ thuộc (dependency / 의존성) thứ tự (ordering / 순서) không chứng minh readiness của phụ thuộc (dependency / 의존성)

GitOps công cụ (tool / 도구) có thể hỗ trợ wave/thứ tự (order / 순서)/hook để apply cơ sở dữ liệu (database / 데이터베이스) trước ứng dụng (application / 애플리케이션), CRD trước Custom tài nguyên (resource / 자원) hoặc không gian tên (namespace / 네임스페이스) trước tải công việc (workload / 워크로드). Nhưng “đã apply trước” khác “đã usable”. cơ sở dữ liệu (database / 데이터베이스) đối tượng (object / 객체) Created chưa chắc endpoint ready; CRD registered chưa chắc conversion webhook healthy.

Thứ tự (ordering / 순서) chỉ giải phụ thuộc (dependency / 의존성) về mutation chuỗi (sequence / 시퀀스). Readiness phụ thuộc (dependency / 의존성) cần điều kiện (condition / 조건) ngữ nghĩa (semantics / 의미론) và hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) phù hợp. Chèn sleep cố định thường che propagation thời gian (time / 시간) thay vì mô hình (model / 모델) phụ thuộc (dependency / 의존성).

Nếu ứng dụng (application / 애플리케이션) phải đợi di chuyển (migration / 마이그레이션) hoàn tất, di chuyển (migration / 마이그레이션) completion nên có durable status/bằng chứng (evidence / 증거) mà bản phát hành (release / 릴리스) controller có thể đọc, không chỉ dựa vào thứ tự tệp (file / 파일) trong repository.

## 25. Multi-cluster fan-out làm một lần ghi nhận (commit / 커밋) có blast radius lớn

Một repository/template có thể được hàng chục hoặc hàng trăm cluster reconcile. Đây là leverage lớn nhưng cũng biến một lần ghi nhận (commit / 커밋) sai thành organization-wide sự kiện (event / 이벤트). “thay đổi (change / 변경) nhỏ trong dùng chung (shared / 공유) cơ sở (base / 기반)” có thể có blast radius lớn hơn một ứng dụng (application / 애플리케이션) deploy bình thường.

Nền tảng (platform / 플랫폼) nên hỗ trợ progressive rollout của desired-state changes: cohort/cell/canary cluster, pause giữa wave, tính tương thích (compatibility / 호환성) check và toàn cục (global / 전역) kill switch có kiểm tra (audit / 감사). Không nên đồng bộ mọi cluster môi trường vận hành (production / 운영 환경) ngay chỉ vì Git merge là atomic.

Multi-cluster GitOps vì vậy cần hai tầng progression: sản phẩm tạo ra (artifact / 산출물)/ứng dụng (application / 애플리케이션) rollout bên trong cluster và rollout của **nền tảng (platform / 플랫폼) desired trạng thái (state / 상태)** giữa các cluster.

## 26. Secret decryption controller nằm trên trust và availability đường dẫn (path / 경로)

Nếu Git lưu ciphertext, một controller/plugin phải decrypt bằng key/định danh (identity / 식별자) phù hợp trước khi tạo thời gian chạy (runtime / 런타임) Secret. thất bại (failure / 실패) có thể đến từ key rotation, KMS outage, permission drift hoặc ciphertext format/phiên bản (version / 버전) mismatch.

Git revision có thể hoàn toàn đúng nhưng reconciliation thất bại (fail / 실패) ở decrypt stage. bằng chứng (evidence / 증거) nên tách nguồn (source / 소스) fetch, kết xuất (render / 렌더링), decrypt, apply và tải công việc (workload / 워크로드) consumption. Key rotation còn phải bảo đảm controller mới đọc được ciphertext cũ hoặc repository được re-encrypt theo di chuyển (migration / 마이그레이션) plan.

Bảo mật (security / 보안) gain từ encrypted Git không loại bỏ vòng đời (lifecycle / 생명주기) độ phức tạp (complexity / 복잡도); nó chuyển plaintext ranh giới (boundary / 경계) từ repository sang decrypt/thời gian chạy (runtime / 런타임) đường dẫn (path / 경로).

## 27. cấp cao (senior / 시니어) walkthrough: GitOps báo Synced nhưng 40% traffic vẫn ở phiên bản (version / 버전) cũ

Giả sử controller báo revision R2 `Synced`, triển khai (deployment / 배포) spec đã là ảnh (image / 이미지) D2, nhưng metrics theo sản phẩm tạo ra (artifact / 산출물) cho thấy 40% yêu cầu (request / 요청) vẫn do D1 xử lý. Một số Pod D2 `Ready`, một số old Pod chưa terminate vì liên kết (connection / 연결) draining/PDB/sức chứa (capacity / 용량); dịch vụ (service / 서비스) mesh giữ long-lived liên kết (connection / 연결) tới old endpoint.

GitOps không sai: desired đối tượng (object / 객체) đã được áp dụng. Nhưng bản phát hành (release / 릴리스) chưa hội tụ ở mặt phẳng dữ liệu (data plane / 데이터 플레인). Investigation phải chuyển xuống tải công việc (workload / 워크로드) rollout, endpoint/routing và liên kết (connection / 연결) vòng đời (lifecycle / 생명주기).

Bài học là **sync trạng thái (state / 상태) không phải serving trạng thái (state / 상태)**. GitOps dashboard là một bằng chứng (evidence / 증거) nguồn (source / 소스) trong chuỗi nhân quả (causal chain / 인과 사슬), không phải oracle cuối cùng của môi trường vận hành (production / 운영 환경) kết quả (outcome / 결과).

> **Bàn giao:** Sau **27. cấp cao (senior / 시니어) walkthrough: GitOps báo Synced nhưng 40% traffic vẫn ở phiên bản (version / 버전) cũ**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
