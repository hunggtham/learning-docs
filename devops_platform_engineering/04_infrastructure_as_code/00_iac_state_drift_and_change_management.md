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

## 14. Apply là transaction không hoàn chỉnh

Nhiều người vô thức nghĩ `apply` giống một database transaction: hoặc mọi thứ thành công, hoặc mọi thứ rollback. Thực tế provider API thường không cung cấp atomic transaction xuyên nhiều resource. Engine có thể tạo network thành công, tạo database thất bại, rồi dừng ở trạng thái **một phần đã thay đổi**.

Vì vậy failure handling phải bắt đầu từ câu hỏi: operation nào đã thực sự commit ở provider, state đã ghi nhận đến đâu, resource nào đang tồn tại nhưng chưa đạt desired graph và chạy lại apply sẽ làm gì. Idempotency/convergence giúp retry an toàn hơn, nhưng không biến sequence thành atomic.

Một runbook tốt cho IaC failure không bắt đầu bằng “rerun”. Nó bắt đầu bằng refresh/read actual state, xác định side effect đã xảy ra và chỉ retry khi biết engine sẽ tiếp tục từ state đúng.

## 15. Lock bảo vệ writer concurrency, không bảo vệ mọi race

State locking ngăn hai apply cùng sửa một state backend tại cùng thời điểm. Nhưng nó không ngăn người khác thay cloud resource qua console, controller khác sửa cùng field, hoặc provider-side automation chạy giữa plan và apply.

Do đó locking chỉ giải một loại race: **concurrent state writer**. Ownership và policy mới giải race giữa nhiều control plane. Khi thấy plan thay đổi ngoài dự kiến ngay sau một apply thành công, hãy tìm external actor/controller thay vì chỉ nghi state lock hỏng.

## 16. Eventual consistency làm dependency graph có thời gian

IaC graph mô tả thứ tự logic nhưng provider có thể trả “create thành công” trước khi resource hoàn toàn visible cho API khác. Ví dụ identity vừa tạo có thể chưa được authorization subsystem nhận ra ngay; DNS/resource attachment có thể cần thời gian hội tụ.

Provider implementation thường thêm retry/backoff cho những trường hợp này, nhưng user vẫn cần nhận diện eventual consistency để không chèn `sleep 60` như một fix ngẫu nhiên. Fix tốt hơn là chờ condition có semantics, retry theo bounded backoff hoặc để provider/controller sở hữu dependency readiness.

`depends_on` chỉ nói A phải được tạo trước B; nó không tự chứng minh A đã **usable** theo business contract.

## 17. Refactor configuration không được đồng nghĩa recreate infrastructure

Khi cấu trúc code thay đổi — đổi tên module, tách module, đổi logical address — intent business có thể giữ nguyên nhưng address trong state thay đổi. Nếu không dùng move/import/state-migration semantics phù hợp, engine có thể hiểu đây là “xóa cũ, tạo mới”.

Vì vậy refactor IaC có hai lớp review: semantic diff của hạ tầng và refactor diff của code. Mục tiêu lý tưởng của một refactor thuần túy là plan no-op đối với remote object. Nếu plan cho thấy replace resource stateful, phải dừng và xác nhận đó có thực sự là intent hay chỉ là state-address mismatch.

## 18. Provider và module version là dependency production

IaC engine, provider plugin và module đều tiến hóa. Một upgrade provider có thể đổi default, schema hoặc diff behavior dù configuration của bạn không đổi. Vì vậy version pinning và upgrade testing quan trọng như dependency ứng dụng.

Nhưng pin vĩnh viễn cũng tạo debt. Pattern tốt là khóa version trong normal run, rồi mở explicit upgrade change có release note review, plan comparison và staged environment verification. Với module platform dùng chung, compatibility contract và migration guide phải được coi như API evolution.

## 19. Destroy là operation có asymmetry

Tạo resource thường có thể retry; destroy có thể không thể đảo. Xóa bucket, key, database hoặc network route có hậu quả khác nhau và đôi khi làm mất chính dữ liệu cần để rollback.

Critical resource nên có layered protection phù hợp: lifecycle protection ở IaC, retention/backup ở service, policy hạn chế identity được destroy và review riêng cho destructive plan. Không một lớp nào đủ một mình vì emergency hoặc migration thật sự vẫn có lúc cần phá protection.

Senior reasoning ở đây là phân biệt **reversible change** và **irreversible change**. Hai thay đổi có cùng số dòng diff nhưng risk class hoàn toàn khác nhau.

## 20. Unknown value là một phần semantics của plan

Có những thuộc tính chỉ biết sau khi resource được tạo, ví dụ generated ID, hostname, assigned IP hoặc provider-computed field. Trong plan, chúng có thể ở trạng thái “known after apply”. Đây không phải lỗi hiển thị; nó phản ánh rằng engine chưa có đủ information để tính toàn bộ graph trước mutation.

Điều này quan trọng khi policy hoặc downstream resource phụ thuộc vào value chưa biết. Một policy chỉ kiểm tra text plan mà giả định mọi field đã concrete có thể bỏ sót risk. Ngược lại, cố ép mọi value thành known bằng data lookup hoặc script ngoài có thể tạo hidden dependency mới.

Review IaC trưởng thành phân biệt ba trạng thái: value đã biết từ config/state, value đọc từ remote hiện tại, và value chỉ hình thành sau actuation. Confidence của plan phải tương ứng với mức information thật sự có sẵn.

## 21. Replacement ordering là availability decision, không chỉ lifecycle flag

Khi một property bắt buộc replace resource, có hai order tổng quát: destroy old rồi create new, hoặc create replacement trước rồi retire old. `create-before-destroy` có thể giảm downtime nhưng chỉ hoạt động nếu provider cho phép hai resource cùng tồn tại, quota còn đủ và name/identity không conflict.

Với stateful resource, tạo song song còn kéo theo data sync/cutover. Với network route hoặc singleton identity, hai bản cùng tồn tại có thể tạo ambiguity. Vì vậy replacement strategy phải dựa trên resource semantics, không phải bật một flag chung cho mọi module.

Một plan có chữ `replace` nên kích hoạt câu hỏi: có downtime không, có double-capacity headroom không, data/state chuyển thế nào, endpoint/identity cutover ra sao và rollback target còn tồn tại bao lâu.

## 22. Data source và remote lookup có thể biến build-plan thành dependency runtime

IaC thường đọc thông tin từ resource ngoài ownership của state hiện tại: image ID mới nhất, subnet được team khác tạo, secret metadata hoặc account data. Những lookup này tiện nhưng làm plan phụ thuộc trạng thái external tại thời điểm chạy.

Nếu query “latest image” trả giá trị mới vào ngày mai, cùng source commit có thể plan khác. Nếu team khác rename/tag resource, apply của bạn có thể fail dù code không đổi. Vì vậy remote lookup cũng phải có contract về ownership, stability và versioning.

Khi reproducibility quan trọng, nên pin identity cụ thể hoặc promote value qua interface rõ thay vì truy vấn “mới nhất” ngầm. Đây là cùng nguyên tắc với artifact build: hidden mutable input làm evidence yếu đi.

## 23. State recovery phải tránh biến backup cũ thành authority sai

Backend state được backup/versioned là cần thiết, nhưng restore state snapshot cũ không tự động restore cloud resource về thời điểm cũ. Remote object có thể đã thay đổi sau snapshot. Nếu nạp state cũ rồi apply ngay, engine có thể đưa ra mutation nguy hiểm dựa trên mapping stale.

Recovery đúng thường tách hai bước: phục hồi metadata state đủ để đọc được ownership, sau đó refresh/reconcile với actual remote state trước khi cho phép destructive action. Với resource quan trọng, cần test runbook “state backend mất/corrupt” như một failure class riêng.

State backup bảo vệ **knowledge về ownership**, không phải backup data/application resource. Hai loại recovery phải được thiết kế riêng.

## 24. Policy trên plan và policy trên actual state bảo vệ hai thời điểm khác nhau

Policy-as-code trước apply cho feedback sớm: cấm public exposure, enforce tag, giới hạn instance class hoặc destroy. Nhưng plan có unknown value và race; sau apply actual state có thể khác vì provider default, external controller hoặc eventual behavior.

Vì vậy critical invariant có thể cần nhiều lớp: policy trong code/module default, policy ở plan/admission trước mutation, và continuous audit trên actual cloud state. Mục tiêu không phải duplicate mọi rule ba lần mà đặt enforcement tại boundary nơi violation có thể phát sinh.

Một rule security cần chặn trước creation khác với một rule hygiene có thể detect rồi remediate sau. Fail-closed hay eventual remediation là risk decision, không chỉ lựa chọn tool.

## 25. Senior walkthrough: plan “không downtime” nhưng apply vẫn kẹt vì quota

Giả sử module thay launch configuration và dùng replacement trước khi destroy để giữ capacity. Plan trông an toàn: tạo 20 instance mới rồi bỏ 20 instance cũ. Nhưng account chỉ còn quota cho 5 instance. Apply tạo 5 rồi provider reject phần còn lại; old fleet vẫn tồn tại nhưng rollout mắc giữa chừng.

Failure không nằm ở diff business mà ở **temporary capacity required by transition**. Safe-change review phải tính steady-state capacity và transition-state capacity riêng. Canary, surge, replacement, DR failover đều có cùng pattern: safety thường cần headroom tạm thời.

Bài học tổng quát là IaC plan cần được đọc như một state transition có resource/time/failure semantics, không phải như ảnh chụp before/after.