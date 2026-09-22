# Infrastructure as Code: desired state, state model, drift và lifecycle

## 1. IaC giải quyết vấn đề nào

Hạ tầng thủ công có một lỗi cấu trúc: actual state tồn tại trong cloud/provider nhưng intent lại nằm trong trí nhớ, ticket hoặc tài liệu dễ cũ. Infrastructure as Code (IaC / 코드형 인프라) đưa intent vào file có version control để thay đổi có thể review, preview và lặp lại.

IaC không đơn thuần là “script tạo server”. Điểm mạnh nhất của declarative IaC là mô tả desired state rồi để engine tính khác biệt với known actual state/provider state.

## 2. Declarative và imperative

Imperative automation mô tả sequence: tạo network, tạo VM, gắn disk. Declarative configuration nói muốn có network/VM/disk với property nào. Engine xây dependency graph, đọc state và gọi provider API để hội tụ.

Declarative không loại bỏ imperative. Provider vẫn thực hiện API operation theo thứ tự. Lợi ích là user thao tác ở cấp state/invariant thay vì tự viết mọi nhánh “nếu resource tồn tại thì...”.

## 3. State là phần của correctness

Terraform và các engine tương tự cần state để map resource trong code với remote object và metadata lifecycle. State không chỉ là cache có thể bỏ tùy ý. Nếu state mất hoặc có hai writer đồng thời, engine có thể tạo duplicate, destroy sai resource hoặc không biết ownership.

Remote state backend thường cần locking/concurrency control, access control, encryption và backup/versioning. Không nên commit state chứa giá trị nhạy cảm vào repository public.

## 4. Plan không phải lời tiên tri tuyệt đối

`plan` là dự đoán dựa trên configuration, state đã biết và provider read tại thời điểm đó. Giữa plan và apply, external state có thể thay đổi. Provider API cũng có eventual consistency hoặc computed value chỉ biết sau create.

Do đó review plan rất hữu ích nhưng không chứng minh apply chắc chắn đúng. Pipeline cần capture plan artifact phù hợp, hạn chế khoảng cách thời gian và quyền thay đổi, rồi verify actual state sau apply.

## 5. Drift là sự khác biệt về ownership

Drift xuất hiện khi resource bị sửa ngoài IaC, provider đổi default/behavior hoặc dependency bên ngoài thay đổi. Không phải mọi drift đều nguy hiểm, nhưng drift không có owner là nguy hiểm.

Tổ chức cần quyết định: console change có bị cấm hoàn toàn; emergency change được phép nhưng phải back-port vào code; hay một số field deliberately ignored vì controller khác sở hữu. Ownership phải explicit để hai controller không “đánh nhau” liên tục.

## 6. Idempotency và convergence

Một apply ổn định sau khi desired state đã đạt thường không nên tạo change mới vô cớ. Nếu chạy mỗi lần lại thay resource, có thể provider dùng nondeterministic input, generated timestamp hoặc config không normalize.

Convergence quan trọng với automation. Platform không thể tự reconcile an toàn nếu action mỗi lần làm state trôi thêm.

## 7. Resource graph và blast radius

IaC engine xây dependency graph để biết order. Nhưng graph kỹ thuật không luôn phản ánh blast radius business. Thay một shared network route có thể ảnh hưởng hàng trăm service dù diff chỉ một dòng.

Module boundary và state boundary nên tính theo ownership/blast radius, không chỉ theo loại resource. Một state file khổng lồ cho toàn công ty tạo lock contention và khiến một apply có quyền rất rộng. Quá nhiều state siêu nhỏ lại tăng coordination cost. Boundary đúng thường theo team/domain/environment và lifecycle tương đối độc lập.

## 8. Module là abstraction có contract

Module không nên chỉ bọc vài resource để giảm số dòng. Module tốt encode policy/default, expose input thực sự cần, giữ output contract ổn định và có versioning strategy.

Nếu module expose mọi property y hệt provider, nó không giảm cognitive load. Nếu module giấu quá nhiều nhưng không có escape hatch, user fork module và platform mất control. Đây là cùng bài toán abstraction của Platform Engineering.

## 9. Lifecycle của thay đổi phá hủy

Rename logical resource trong code có thể được engine hiểu là destroy old + create new nếu không có move/import semantics. Với stateful resource, đây có thể là data loss.

Review IaC phải đọc action semantics, không chỉ diff text. Các dấu hiệu `destroy`, `replace`, force-new property, route/ACL change và identity permission change cần được highlight theo risk class.

## 10. Secret trong IaC

“Sensitive” trong CLI output không có nghĩa secret không nằm trong state. Một value được đánh dấu nhạy cảm có thể vẫn được backend lưu để engine quản resource. Vì vậy secret management phải xem state backend là sensitive asset.

Tốt hơn là IaC tạo reference/permission tới secret system, còn secret value lifecycle được quản ở secret manager khi phù hợp. Nếu provider bắt buộc value đi qua state, phải bảo vệ backend tương ứng.

## 11. Import và brownfield

Hệ thống thật thường có resource tạo thủ công từ trước. IaC adoption không nhất thiết destroy/recreate. Import đưa existing object vào ownership map, sau đó configuration phải được chỉnh đến khi plan không còn surprise.

Quá trình brownfield nên đi từng boundary nhỏ: inventory → import → normalize → plan no-op → sau đó mới refactor module. Không vừa import vừa redesign lớn vì khó biết diff đến từ ownership hay design change.

## 12. CI/CD cho IaC

Một flow điển hình là format/validate, static/policy check, plan trên pull request, review, merge rồi apply bằng identity kiểm soát. Production credential không nên nằm trên laptop từng developer nếu automation có thể làm owner.

Apply cần serialization theo state boundary và audit log. Emergency path vẫn cần, nhưng emergency change phải quay lại source of truth nhanh để drift không trở thành permanent fork.

## 13. Senior note: IaC là một controller chưa chắc chạy liên tục

Hãy nhìn IaC qua mental model control loop. Config là desired state, provider object là actual state, state file là mapping/known state, plan là diff computation, apply là actuation. Một số GitOps/IaC controller chạy liên tục; Terraform CLI truyền thống thường chạy theo event.

Khi hiểu như vậy, câu hỏi rõ hơn: ai trigger reconciliation; bao lâu drift được phát hiện; nếu hai controller cùng quản một field thì sao; failure giữa apply để lại state nào; và evidence nào chứng minh convergence.

IaC thành công khi hạ tầng trở thành hệ thống thay đổi có review, identity, rollback/recovery và ownership rõ, không chỉ khi “mọi resource đã viết bằng HCL”.