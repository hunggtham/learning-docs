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