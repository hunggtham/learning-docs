# GitOps: desired state trong Git và reconciliation liên tục

## 1. GitOps giải vấn đề “ai đã thay cluster?”

CI/CD truyền thống có thể dùng pipeline giữ credential rồi chạy `kubectl apply`. Mô hình này hoạt động, nhưng push-based deployment khiến pipeline trực tiếp thay remote state. GitOps đảo chiều: desired state được commit vào repository; agent/controller gần cluster watch repository và reconcile actual state.

```text
change request → Git review → desired state commit
                           ↓
                    GitOps controller
                           ↓ compare
                    cluster actual state
                           ↓ reconcile
                    Kubernetes/resources
```

Mục tiêu không phải dùng Git vì Git “thần kỳ”, mà là tạo source of truth có history, review và một reconciliation loop rõ ownership.

## 2. Pull model giảm credential exposure

Trong pull-based GitOps, CI build artifact và cập nhật desired state/release metadata nhưng không nhất thiết cầm credential cluster quyền rộng. Controller trong environment có permission phù hợp để apply.

Điều này cải thiện security boundary nhưng không tự động an toàn. Nếu repository write permission quá rộng, attacker sửa desired state vẫn có thể điều khiển cluster. Git permission trở thành một phần production authorization model.

## 3. Source of truth phải có ownership rõ

Một field không thể đồng thời được GitOps controller, HPA và người dùng `kubectl edit` quản theo ý khác nhau mà không có conflict. Ví dụ HPA sở hữu replica count động, nên GitOps config cần tránh liên tục kéo replicas về con số tĩnh không phù hợp.

Mỗi layer cần quyết định field ownership. Git quản cấu trúc/policy ổn định; runtime controller quản state động theo contract. Nếu không, reconciliation tạo oscillation.

## 4. Drift detection là capability cốt lõi

Vì controller so desired với actual, thay đổi trực tiếp cluster sẽ xuất hiện drift và có thể bị revert. Đây là lợi thế lớn nhưng cũng ảnh hưởng emergency operation.

Nếu operator sửa live state để chữa incident, GitOps có thể vài giây sau ghi đè. Quy trình emergency cần biết pause/suspend reconciliation, hoặc tốt hơn là đưa change qua source of truth đủ nhanh. Sau incident, mọi emergency patch phải được reconcile ngược về Git để không tạo lịch sử giả.

## 5. Promotion model

Có hai thứ thường được promote: artifact identity và configuration. Một release tốt cập nhật image digest/version trong desired-state repo. Promotion từ staging đến production không nên rebuild image; nó thay reference đến cùng artifact đã được kiểm chứng.

Có thể dùng repository/branch/directory khác nhau cho environment. Không có một layout duy nhất đúng. Boundary cần phản ánh ownership, review permission và blast radius.

## 6. Reconciliation interval và eventual behavior

Git commit không đồng nghĩa cluster thay ngay. Controller phải fetch, render, diff, apply rồi downstream controller tiếp tục reconcile. Có nhiều delay nối tiếp.

Khi user hỏi “merge rồi sao production chưa đổi?”, cần xem GitOps controller đã thấy revision chưa, render có thành công không, apply có bị policy chặn không, workload controller đã rollout chưa và readiness/verification thế nào.

## 7. Sync success không bằng release success

GitOps UI xanh có thể chỉ nghĩa manifests đã apply và resources đạt condition controller mong chờ. Business metric vẫn có thể xấu. Vì vậy progressive delivery/verification nên nối GitOps state với observability signal.

Control plane chứng minh state convergence; data-plane telemetry chứng minh user outcome.

## 8. Secret trong GitOps

Git repository không nên chứa plaintext production secret. Có nhiều pattern: encrypted secret file, external secret reference, secret-store CSI/controller hoặc generated short-lived credential. Lựa chọn phụ thuộc trust model.

Điểm cần giữ là Git lưu intent/reference hoặc ciphertext phù hợp, còn key lifecycle và access control nằm ở security system. “Private repository” không phải lý do đủ để commit plaintext secret.

## 9. Rendering và template complexity

Helm/Kustomize/template làm giảm duplicate nhưng có thể biến desired state thành chương trình khó dự đoán. Nếu phải chạy nhiều layer templating mới biết manifest cuối cùng, review quality giảm.

Platform nên giữ abstraction đủ cao nhưng output inspectable. Reviewer cần thấy effective diff hoặc có tooling render đáng tin. Abstraction không được làm causal chain biến mất.

## 10. GitOps với infrastructure

GitOps không giới hạn Kubernetes. Một controller có thể reconcile cloud resource/IaC từ Git. Tuy nhiên phải tránh hai control loop cùng sở hữu resource. Nếu Terraform pipeline và Crossplane/operator cùng quản một database field, drift loop có thể liên tục ghi đè.

## 11. Failure scenario

Giả sử production đang sync revision R, commit R+1 đổi Deployment nhưng controller báo `OutOfSync`. Trước hết kiểm tra controller có fetch repo/auth được không. Nếu render fail, sửa source/template. Nếu diff tồn tại nhưng apply bị deny, xem admission/policy/RBAC. Nếu apply thành công nhưng app chưa healthy, rời GitOps layer và điều tra Kubernetes/workload/data-plane.

Giữ layer boundary giúp không biến mọi lỗi thành “ArgoCD lỗi”.

## 12. Senior note: GitOps là operational contract

GitOps có giá trị khi tạo contract: mọi desired production change có history; reconciliation identity rõ; drift observable; manual change có policy; promotion giữ artifact identity; rollback/roll-forward có thể thao tác bằng revision có kiểm soát.

Nếu team vẫn thường xuyên `kubectl edit`, controller hay bị disable và source of truth không phản ánh production, tổ chức chỉ có GitOps tool chứ chưa có GitOps operating model.

## 13. Git là source of desired state, không phải source of toàn bộ reality

Git có thể nói workload **nên** chạy image digest D với config C. Nó không chứa toàn bộ trạng thái runtime như pod nào đang crash, HPA vừa scale bao nhiêu, cloud load balancer đã provision xong chưa hay database đang replication lag.

Vì vậy câu “Git là source of truth” cần đọc chính xác hơn: Git là source of truth cho **intent thuộc ownership của GitOps**. Actual state vẫn phải được quan sát từ control plane/data plane. Khi incident xảy ra, không được kết luận “Git đúng nên production phải đúng”.

## 14. Field ownership phải được thiết kế như API ownership

Kubernetes và các controller có thể cùng chạm một object. Một số cơ chế apply có metadata field manager giúp theo dõi ai sở hữu field nào, nhưng tool không thể tự quyết định ownership business.

Ví dụ Deployment template, image và policy có thể thuộc GitOps; replica count thuộc HPA; annotation do service mesh controller inject; status thuộc workload controller. Nếu Git render cả field động mà không có lý do, reconciliation có thể liên tục overwrite controller khác.

Khi thấy object “cứ đổi qua đổi lại”, hãy kiểm tra audit/event/managed-field evidence và vẽ bảng ownership. Đây thường là control-loop conflict chứ không phải random drift.

## 15. Rollback Git revision không rollback external state

Revert commit có thể đưa manifest về phiên bản trước, nhưng không chắc đảo được database migration, message schema, external side effect hoặc cloud resource đã mutate. Git history chỉ version hóa intent; external state có lifecycle riêng.

Do đó GitOps rollback phải dùng cùng compatibility reasoning như CI/CD rollback. Nếu release N+1 đã ghi data mà N không đọc được, revert image reference có thể làm outage nặng hơn. Expand-and-contract, forward-compatible schema và roll-forward path vẫn cần.

## 16. Promotion repo có thể tạo race nếu nhiều actor sửa cùng environment

Hai automation cùng mở change cho production có thể từng pass test riêng nhưng khi merge liên tiếp lại tạo combination chưa được verify. Ví dụ release A nâng application, release B đổi config/dependency; mỗi PR xanh trên base cũ nhưng production nhận A+B.

Pipeline nên verify effective desired state gần với revision cuối sẽ reconcile, hoặc serialize/rerun verification khi base thay đổi. Đây là cùng vấn đề stale plan ở IaC: evidence phải gắn với state gần state thực sự được apply.

## 17. Emergency change cần một protocol trước incident

Nếu GitOps controller tự-heal mạnh, live patch có thể bị revert đúng lúc operator đang mitigate. Nhưng tắt controller tùy tiện cũng làm mất safety net và tạo drift không visible.

Platform nên định nghĩa break-glass flow: ai được suspend reconciliation, scope nào, trong bao lâu, change live được ghi ở đâu, khi nào back-port vào Git và điều kiện resume. Sau resume cần verify controller không “undo” mitigation theo desired state cũ.

## 18. Repository security là production security

Khi Git commit có thể dẫn tới production reconciliation, branch protection, reviewer permission, bot token, webhook/controller credential và dependency của rendering pipeline đều trở thành part of production trust chain.

Một repository private nhưng token bot bị lộ vẫn không an toàn. Ngược lại, commit signing đơn lẻ cũng không đủ nếu signer có quyền quá rộng hoặc controller không verify policy. Security chapter sẽ đào sâu nguyên tắc identity + provenance + authorization thay vì dựa vào một control đơn lẻ.

## 19. Senior walkthrough: trạng thái cứ bị đổi ngược sau vài phút

Giả sử operator tăng replicas từ 10 lên 20 để mitigate traffic spike. Vài phút sau nó quay về 10. Có ít nhất ba possibility: GitOps đang reconcile spec 10; HPA đang tính desired 10; hoặc một automation khác patch field.

Đừng tiếp tục `kubectl scale` nhiều lần. Hãy xác định actor từ event/audit/field ownership, rồi sửa desired owner đúng. Nếu HPA sở hữu replica, thay policy/metric/minimum phù hợp. Nếu GitOps sở hữu, emergency change phải đi qua Git hoặc suspend theo protocol.

Đây là lợi ích của GitOps khi được vận hành đúng: drift không chỉ bị sửa, mà còn buộc tổ chức phải làm rõ **ai có quyền định nghĩa state nào**.

## 20. Revision observed, revision applied và revision serving traffic là ba state khác nhau

Một GitOps controller có thể đã fetch commit `R2`, render thành công và ghi resource vào API nhưng workload vẫn đang phục vụ phần lớn traffic bằng artifact từ `R1`. Nếu chỉ lưu một nhãn “Synced R2”, operator dễ nghĩ production đã hoàn tất release.

Một causal chain hữu ích là:

```text
Git revision observed
→ rendered desired state
→ API objects applied
→ workload controller observed generation
→ new replicas Ready
→ routing đưa traffic tới replica mới
→ telemetry xác nhận outcome của artifact/config mới
```

Release metadata nên cho phép nối các state này. Điều này đặc biệt quan trọng khi rollback hoặc incident xảy ra giữa rollout: source desired state có thể là R2 nhưng actual fleet là mixture R1/R2.

## 21. Git/repository outage ảnh hưởng khả năng đổi state, không nhất thiết traffic hiện tại

Nếu repository hoặc Git provider down, controller có thể không fetch revision mới nhưng workload đang chạy vẫn khỏe. Đây là control-plane dependency giống registry/cloud API: data plane có thể tiếp tục nhưng deploy, recovery hoặc scale path liên quan desired state bị giới hạn.

Runbook cần biết controller giữ cache/revision cuối ra sao và behavior khi không reach repo: giữ last-known desired state, fail closed hay liên tục retry. Retry fan-out từ hàng trăm cluster/controller còn có thể gây thundering herd khi Git provider hồi phục.

Do đó Git availability cần được đánh giá theo **change/recovery capability**, không chỉ “application uptime hiện tại”.

## 22. Rendering phải deterministic đủ để revision có nghĩa

Nếu cùng Git revision render ra manifest khác vì chart dependency `latest`, remote lookup mutable, environment variable ngoài source hoặc plugin version khác, commit SHA không còn là identity đầy đủ của desired state.

GitOps tốt cố gắng version hóa rendering inputs: chart/module dependency, plugin/tool version, values và external reference quan trọng. Nếu output cần remote data, phải biết remote input đó thuộc contract nào và có được snapshot/pin không.

Mental model giống reproducible build: **desired-state artifact** cũng nên có input closure đủ rõ. “Git không đổi nhưng cluster diff đổi” là dấu hiệu có mutable input ngoài Git hoặc controller/runtime behavior thay đổi.

## 23. Prune/delete có risk class khác apply/update

GitOps thường có khả năng xóa resource khi object biến mất khỏi desired source. Đây là convergence hợp lý nhưng destructive semantics khác create/update. Một rename/move sai path hoặc selector scope rộng có thể làm controller hiểu resource không còn được mong muốn và prune hàng loạt.

Critical resource cần protection phù hợp: review effective diff, deletion policy/retention, finalizer hoặc explicit allow-prune tùy architecture. Nhưng protection không được biến thành resource vĩnh viễn không ai xóa được.

Senior review nên highlight **object leaving desired set** như một state transition riêng, không chỉ nhìn số dòng Git bị xóa.

## 24. Dependency ordering không chứng minh readiness của dependency

GitOps tool có thể hỗ trợ wave/order/hook để apply database trước application, CRD trước Custom Resource hoặc namespace trước workload. Nhưng “đã apply trước” khác “đã usable”. Database object Created chưa chắc endpoint ready; CRD registered chưa chắc conversion webhook healthy.

Ordering chỉ giải dependency về mutation sequence. Readiness dependency cần condition semantics và timeout/retry phù hợp. Chèn sleep cố định thường che propagation time thay vì model dependency.

Nếu application phải đợi migration hoàn tất, migration completion nên có durable status/evidence mà release controller có thể đọc, không chỉ dựa vào thứ tự file trong repository.

## 25. Multi-cluster fan-out làm một commit có blast radius lớn

Một repository/template có thể được hàng chục hoặc hàng trăm cluster reconcile. Đây là leverage lớn nhưng cũng biến một commit sai thành organization-wide event. “Change nhỏ trong shared base” có thể có blast radius lớn hơn một application deploy bình thường.

Platform nên hỗ trợ progressive rollout của desired-state changes: cohort/cell/canary cluster, pause giữa wave, compatibility check và global kill switch có audit. Không nên đồng bộ mọi cluster production ngay chỉ vì Git merge là atomic.

Multi-cluster GitOps vì vậy cần hai tầng progression: artifact/application rollout bên trong cluster và rollout của **platform desired state** giữa các cluster.

## 26. Secret decryption controller nằm trên trust và availability path

Nếu Git lưu ciphertext, một controller/plugin phải decrypt bằng key/identity phù hợp trước khi tạo runtime Secret. Failure có thể đến từ key rotation, KMS outage, permission drift hoặc ciphertext format/version mismatch.

Git revision có thể hoàn toàn đúng nhưng reconciliation fail ở decrypt stage. Evidence nên tách source fetch, render, decrypt, apply và workload consumption. Key rotation còn phải bảo đảm controller mới đọc được ciphertext cũ hoặc repository được re-encrypt theo migration plan.

Security gain từ encrypted Git không loại bỏ lifecycle complexity; nó chuyển plaintext boundary từ repository sang decrypt/runtime path.

## 27. Senior walkthrough: GitOps báo Synced nhưng 40% traffic vẫn ở version cũ

Giả sử controller báo revision R2 `Synced`, Deployment spec đã là image D2, nhưng metrics theo artifact cho thấy 40% request vẫn do D1 xử lý. Một số Pod D2 `Ready`, một số old Pod chưa terminate vì connection draining/PDB/capacity; service mesh giữ long-lived connection tới old endpoint.

GitOps không sai: desired object đã được áp dụng. Nhưng release chưa hội tụ ở data plane. Investigation phải chuyển xuống workload rollout, endpoint/routing và connection lifecycle.

Bài học là **sync state không phải serving state**. GitOps dashboard là một evidence source trong causal chain, không phải oracle cuối cùng của production outcome.