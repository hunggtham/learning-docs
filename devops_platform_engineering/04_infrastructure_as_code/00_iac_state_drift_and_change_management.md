# Hạ tầng dưới dạng mã (infrastructure as code / 코드형 인프라): desired trạng thái (state / 상태), trạng thái (state / 상태) mô hình (model / 모델), drift và vòng đời (lifecycle / 생명주기)

> **Mạch đọc:** Đọc **hạ tầng dưới dạng mã (infrastructure as code / 코드형 인프라): desired trạng thái (state / 상태), trạng thái (state / 상태) mô hình (model / 모델), drift và vòng đời (lifecycle / 생명주기)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. IaC giải quyết vấn đề nào** sang **2. Declarative và imperative**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. IaC giải quyết vấn đề nào

Hạ tầng thủ công có một lỗi cấu trúc: actual trạng thái (state / 상태) tồn tại trong cloud/provider nhưng intent lại nằm trong trí nhớ, ticket hoặc tài liệu dễ cũ. hạ tầng dưới dạng mã (infrastructure as code / 코드형 인프라) đưa intent vào tệp (file / 파일) có phiên bản (version / 버전) điều khiển (control / 제어) để thay đổi có thể rà soát (review / 검토), preview và lặp lại.

IaC không đơn thuần là “script tạo máy chủ (server / 서버)”. Điểm mạnh nhất của declarative IaC là mô tả desired trạng thái (state / 상태) rồi để engine tính khác biệt với known actual trạng thái (state / 상태)/provider trạng thái (state / 상태).

## 2. Declarative và imperative

Imperative automation mô tả chuỗi (sequence / 시퀀스): tạo mạng (network / 네트워크), tạo VM, gắn disk. Declarative cấu hình (configuration / 구성) nói muốn có mạng (network / 네트워크)/VM/disk với thuộc tính (property / 속성) nào. Engine xây phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), đọc trạng thái (state / 상태) và gọi provider API để hội tụ.

Declarative không loại bỏ imperative. Provider vẫn thực hiện API thao tác (operation / 연산) theo thứ tự. Lợi ích là người dùng (user / 사용자) thao tác ở cấp trạng thái (state / 상태)/bất biến (invariant / 불변식) thay vì tự viết mọi nhánh “nếu tài nguyên (resource / 자원) tồn tại thì...”.

## 3. trạng thái (state / 상태) là phần của tính đúng đắn (correctness / 정확성)

Terraform và các engine tương tự cần trạng thái (state / 상태) để map tài nguyên (resource / 자원) trong mã (code / 코드) với remote đối tượng (object / 객체) và siêu dữ liệu (metadata / 메타데이터) vòng đời (lifecycle / 생명주기). trạng thái (state / 상태) không chỉ là bộ nhớ đệm (cache / 캐시) có thể bỏ tùy ý. Nếu trạng thái (state / 상태) mất hoặc có hai writer đồng thời, engine có thể tạo duplicate, destroy sai tài nguyên (resource / 자원) hoặc không biết quyền sở hữu (ownership / 소유권).

Remote trạng thái (state / 상태) backend thường cần locking/tính đồng thời (concurrency / 동시성) điều khiển (control / 제어), kiểm soát truy cập (access control / 접근 제어), encryption và backup/versioning. Không nên lần ghi nhận (commit / 커밋) trạng thái (state / 상태) chứa giá trị nhạy cảm vào repository công khai (public / 공개).

## 4. Plan không phải lời tiên tri tuyệt đối

`plan` là dự đoán dựa trên cấu hình (configuration / 구성), trạng thái (state / 상태) đã biết và provider read tại thời điểm đó. Giữa plan và apply, bên ngoài (external / 외부) trạng thái (state / 상태) có thể thay đổi. Provider API cũng có eventual consistency hoặc computed giá trị (value / 값) chỉ biết sau create.

Do đó rà soát (review / 검토) plan rất hữu ích nhưng không chứng minh apply chắc chắn đúng. chuỗi xử lý (pipeline / 파이프라인) cần capture plan sản phẩm tạo ra (artifact / 산출물) phù hợp, hạn chế khoảng cách thời gian và quyền thay đổi, rồi verify actual trạng thái (state / 상태) sau apply.

## 5. Drift là sự khác biệt về quyền sở hữu (ownership / 소유권)

Drift xuất hiện khi tài nguyên (resource / 자원) bị sửa ngoài IaC, provider đổi default/hành vi (behavior / 동작) hoặc phụ thuộc (dependency / 의존성) bên ngoài thay đổi. Không phải mọi drift đều nguy hiểm, nhưng drift không có đơn vị sở hữu (owner / 오너) là nguy hiểm.

Tổ chức cần quyết định: console thay đổi (change / 변경) có bị cấm hoàn toàn; emergency thay đổi (change / 변경) được phép nhưng phải back-port vào mã (code / 코드); hay một số trường dữ liệu (field / 필드) deliberately ignored vì controller khác sở hữu. quyền sở hữu (ownership / 소유권) phải tường minh (explicit / 명시적) để hai controller không “đánh nhau” liên tục.

## 6. Idempotency và convergence

Một apply ổn định sau khi desired trạng thái (state / 상태) đã đạt thường không nên tạo thay đổi (change / 변경) mới vô cớ. Nếu chạy mỗi lần lại thay tài nguyên (resource / 자원), có thể provider dùng nondeterministic đầu vào (input / 입력), generated timestamp hoặc cấu hình (config / 설정) không normalize.

Convergence quan trọng với automation. nền tảng (platform / 플랫폼) không thể tự reconcile an toàn nếu hành động (action / 동작) mỗi lần làm trạng thái (state / 상태) trôi thêm.

## 7. tài nguyên (resource / 자원) đồ thị (graph / 그래프) và blast radius

IaC engine xây phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) để biết thứ tự (order / 순서). Nhưng đồ thị (graph / 그래프) kỹ thuật không luôn phản ánh blast radius nghiệp vụ (business / 비즈니스). Thay một dùng chung (shared / 공유) mạng (network / 네트워크) tuyến (route / 경로) có thể ảnh hưởng hàng trăm dịch vụ (service / 서비스) dù diff chỉ một dòng.

Ranh giới mô-đun (module boundary / 모듈 경계) và trạng thái (state / 상태) ranh giới (boundary / 경계) nên tính theo quyền sở hữu (ownership / 소유권)/blast radius, không chỉ theo loại tài nguyên (resource / 자원). Một trạng thái (state / 상태) tệp (file / 파일) khổng lồ cho toàn công ty tạo tranh chấp khóa (lock contention / 잠금 경합) và khiến một apply có quyền rất rộng. Quá nhiều trạng thái (state / 상태) siêu nhỏ lại tăng coordination chi phí (cost / 비용). ranh giới (boundary / 경계) đúng thường theo nhóm (team / 팀)/lĩnh vực (domain / 도메인)/môi trường (environment / 환경) và vòng đời (lifecycle / 생명주기) tương đối độc lập.

## 8. mô-đun (module / 모듈) là lớp trừu tượng (abstraction / 추상화) có đặc tả hợp đồng (contract / 계약)

Mô-đun (module / 모듈) không nên chỉ bọc vài tài nguyên (resource / 자원) để giảm số dòng. mô-đun (module / 모듈) tốt encode chính sách (policy / 정책)/default, expose đầu vào (input / 입력) thực sự cần, giữ đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약) ổn định và có versioning chiến lược (strategy / 전략).

Nếu mô-đun (module / 모듈) expose mọi thuộc tính (property / 속성) y hệt provider, nó không giảm cognitive tải (load / 로드). Nếu mô-đun (module / 모듈) giấu quá nhiều nhưng không có escape hatch, người dùng (user / 사용자) fork mô-đun (module / 모듈) và nền tảng (platform / 플랫폼) mất điều khiển (control / 제어). Đây là cùng bài toán lớp trừu tượng (abstraction / 추상화) của kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링).

## 9. vòng đời (lifecycle / 생명주기) của thay đổi phá hủy

Rename logical tài nguyên (resource / 자원) trong mã (code / 코드) có thể được engine hiểu là destroy old + create new nếu không có move/import ngữ nghĩa (semantics / 의미론). Với stateful tài nguyên (resource / 자원), đây có thể là dữ liệu (data / 데이터) mất mát (loss / 손실).

Rà soát (review / 검토) IaC phải đọc hành động (action / 동작) ngữ nghĩa (semantics / 의미론), không chỉ diff văn bản (text / 텍스트). Các dấu hiệu `destroy`, `replace`, force-new thuộc tính (property / 속성), tuyến (route / 경로)/ACL thay đổi (change / 변경) và định danh (identity / 식별자) permission thay đổi (change / 변경) cần được highlight theo rủi ro (risk / 위험) lớp (class / 클래스).

## 10. Secret trong IaC

“Sensitive” trong CLI đầu ra (output / 출력) không có nghĩa secret không nằm trong trạng thái (state / 상태). Một giá trị (value / 값) được đánh dấu nhạy cảm có thể vẫn được backend lưu để engine quản tài nguyên (resource / 자원). Vì vậy secret management phải xem trạng thái (state / 상태) backend là sensitive asset.

Tốt hơn là IaC tạo tham chiếu (reference / 참조)/permission tới secret hệ thống (system / 시스템), còn secret giá trị (value / 값) vòng đời (lifecycle / 생명주기) được quản ở secret manager khi phù hợp. Nếu provider bắt buộc giá trị (value / 값) đi qua trạng thái (state / 상태), phải bảo vệ backend tương ứng.

## 11. Import và brownfield

Hệ thống thật thường có tài nguyên (resource / 자원) tạo thủ công từ trước. IaC adoption không nhất thiết destroy/recreate. Import đưa existing đối tượng (object / 객체) vào quyền sở hữu (ownership / 소유권) map, sau đó cấu hình (configuration / 구성) phải được chỉnh đến khi plan không còn surprise.

Quá trình brownfield nên đi từng ranh giới (boundary / 경계) nhỏ: inventory → import → normalize → plan no-op → sau đó mới refactor mô-đun (module / 모듈). Không vừa import vừa redesign lớn vì khó biết diff đến từ quyền sở hữu (ownership / 소유권) hay thiết kế (design / 설계) thay đổi (change / 변경).

## 12. CI/CD cho IaC

Một luồng (flow / 흐름) điển hình là format/validate, static/chính sách (policy / 정책) check, plan trên pull yêu cầu (request / 요청), rà soát (review / 검토), merge rồi apply bằng định danh (identity / 식별자) kiểm soát. môi trường vận hành (production / 운영 환경) credential không nên nằm trên laptop từng nhà phát triển (developer / 개발자) nếu automation có thể làm đơn vị sở hữu (owner / 오너).

Apply cần serialization theo trạng thái (state / 상태) ranh giới (boundary / 경계) và nhật ký kiểm tra (audit log / 감사 로그). Emergency đường dẫn (path / 경로) vẫn cần, nhưng emergency thay đổi (change / 변경) phải quay lại nguồn chuẩn (source of truth / 정본) nhanh để drift không trở thành permanent fork.

## 13. cấp cao (senior / 시니어) ghi chú (note / 노트): IaC là một controller chưa chắc chạy liên tục

Hãy nhìn IaC qua mô hình tư duy (mental model / 사고 모델) vòng điều khiển (control loop / 제어 루프). cấu hình (config / 설정) là desired trạng thái (state / 상태), provider đối tượng (object / 객체) là actual trạng thái (state / 상태), trạng thái (state / 상태) tệp (file / 파일) là ánh xạ (mapping / 매핑)/known trạng thái (state / 상태), plan là diff computation, apply là actuation. Một số GitOps/IaC controller chạy liên tục; Terraform CLI truyền thống thường chạy theo sự kiện (event / 이벤트).

Khi hiểu như vậy, câu hỏi rõ hơn: ai trigger reconciliation; bao lâu drift được phát hiện; nếu hai controller cùng quản một trường dữ liệu (field / 필드) thì sao; thất bại (failure / 실패) giữa apply để lại trạng thái (state / 상태) nào; và bằng chứng (evidence / 증거) nào chứng minh convergence.

IaC thành công khi hạ tầng trở thành hệ thống thay đổi có rà soát (review / 검토), định danh (identity / 식별자), quay lui (rollback / 롤백)/khôi phục (recovery / 복구) và quyền sở hữu (ownership / 소유권) rõ, không chỉ khi “mọi tài nguyên (resource / 자원) đã viết bằng HCL”.

## 14. Apply là giao dịch (transaction / 트랜잭션) không hoàn chỉnh

Nhiều người vô thức nghĩ `apply` giống một cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션): hoặc mọi thứ thành công, hoặc mọi thứ quay lui (rollback / 롤백). Thực tế provider API thường không cung cấp atomic giao dịch (transaction / 트랜잭션) xuyên nhiều tài nguyên (resource / 자원). Engine có thể tạo mạng (network / 네트워크) thành công, tạo cơ sở dữ liệu (database / 데이터베이스) thất bại, rồi dừng ở trạng thái **một phần đã thay đổi**.

Vì vậy thất bại (failure / 실패) handling phải bắt đầu từ câu hỏi: thao tác (operation / 연산) nào đã thực sự lần ghi nhận (commit / 커밋) ở provider, trạng thái (state / 상태) đã ghi nhận đến đâu, tài nguyên (resource / 자원) nào đang tồn tại nhưng chưa đạt desired đồ thị (graph / 그래프) và chạy lại apply sẽ làm gì. Idempotency/convergence giúp thử lại (retry / 재시도) an toàn hơn, nhưng không biến chuỗi (sequence / 시퀀스) thành atomic.

Một runbook tốt cho IaC thất bại (failure / 실패) không bắt đầu bằng “rerun”. Nó bắt đầu bằng refresh/read actual trạng thái (state / 상태), xác định side tác động (effect / 효과) đã xảy ra và chỉ thử lại (retry / 재시도) khi biết engine sẽ tiếp tục từ trạng thái (state / 상태) đúng.

## 15. khóa (lock / 잠금) bảo vệ writer tính đồng thời (concurrency / 동시성), không bảo vệ mọi race

Trạng thái (state / 상태) locking ngăn hai apply cùng sửa một trạng thái (state / 상태) backend tại cùng thời điểm. Nhưng nó không ngăn người khác thay cloud tài nguyên (resource / 자원) qua console, controller khác sửa cùng trường dữ liệu (field / 필드), hoặc provider-side automation chạy giữa plan và apply.

Do đó locking chỉ giải một loại race: **concurrent trạng thái (state / 상태) writer**. quyền sở hữu (ownership / 소유권) và chính sách (policy / 정책) mới giải race giữa nhiều điều khiển (control / 제어) plane. Khi thấy plan thay đổi ngoài dự kiến ngay sau một apply thành công, hãy tìm bên ngoài (external / 외부) actor/controller thay vì chỉ nghi trạng thái (state / 상태) khóa (lock / 잠금) hỏng.

## 16. Eventual consistency làm phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) có thời gian

IaC đồ thị (graph / 그래프) mô tả thứ tự lô-gic (logic / 논리) nhưng provider có thể trả “create thành công” trước khi tài nguyên (resource / 자원) hoàn toàn visible cho API khác. Ví dụ định danh (identity / 식별자) vừa tạo có thể chưa được authorization subsystem nhận ra ngay; DNS/tài nguyên (resource / 자원) attachment có thể cần thời gian hội tụ.

Provider hiện thực (implementation / 구현) thường thêm thử lại (retry / 재시도)/backoff cho những trường hợp này, nhưng người dùng (user / 사용자) vẫn cần nhận diện eventual consistency để không chèn `sleep 60` như một fix ngẫu nhiên. Fix tốt hơn là chờ điều kiện (condition / 조건) có ngữ nghĩa (semantics / 의미론), thử lại (retry / 재시도) theo bounded backoff hoặc để provider/controller sở hữu phụ thuộc (dependency / 의존성) readiness.

`depends_on` chỉ nói A phải được tạo trước B; nó không tự chứng minh A đã **usable** theo nghiệp vụ (business / 비즈니스) đặc tả hợp đồng (contract / 계약).

## 17. Refactor cấu hình (configuration / 구성) không được đồng nghĩa recreate hạ tầng (infrastructure / 인프라)

Khi cấu trúc mã (code / 코드) thay đổi — đổi tên mô-đun (module / 모듈), tách mô-đun (module / 모듈), đổi logical address — intent nghiệp vụ (business / 비즈니스) có thể giữ nguyên nhưng address trong trạng thái (state / 상태) thay đổi. Nếu không dùng move/import/state-migration ngữ nghĩa (semantics / 의미론) phù hợp, engine có thể hiểu đây là “xóa cũ, tạo mới”.

Vì vậy refactor IaC có hai lớp rà soát (review / 검토): ngữ nghĩa (semantic / 의미적) diff của hạ tầng và refactor diff của mã (code / 코드). Mục tiêu lý tưởng của một refactor thuần túy là plan no-op đối với remote đối tượng (object / 객체). Nếu plan cho thấy replace tài nguyên (resource / 자원) stateful, phải dừng và xác nhận đó có thực sự là intent hay chỉ là state-address mismatch.

## 18. Provider và mô-đun (module / 모듈) phiên bản (version / 버전) là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경)

IaC engine, provider plugin và mô-đun (module / 모듈) đều tiến hóa. Một upgrade provider có thể đổi default, lược đồ (schema / 스키마) hoặc diff hành vi (behavior / 동작) dù cấu hình (configuration / 구성) của bạn không đổi. Vì vậy phiên bản (version / 버전) pinning và upgrade testing quan trọng như phụ thuộc (dependency / 의존성) ứng dụng.

Nhưng pin vĩnh viễn cũng tạo debt. mẫu (pattern / 패턴) tốt là khóa phiên bản (version / 버전) trong normal run, rồi mở tường minh (explicit / 명시적) upgrade thay đổi (change / 변경) có bản phát hành (release / 릴리스) ghi chú (note / 노트) rà soát (review / 검토), plan comparison và staged môi trường (environment / 환경) xác minh (verification / 확인). Với mô-đun (module / 모듈) nền tảng (platform / 플랫폼) dùng chung, tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약) và di chuyển (migration / 마이그레이션) guide phải được coi như API evolution.

## 19. Destroy là thao tác (operation / 연산) có asymmetry

Tạo tài nguyên (resource / 자원) thường có thể thử lại (retry / 재시도); destroy có thể không thể đảo. Xóa bucket, key, cơ sở dữ liệu (database / 데이터베이스) hoặc mạng (network / 네트워크) tuyến (route / 경로) có hậu quả khác nhau và đôi khi làm mất chính dữ liệu cần để quay lui (rollback / 롤백).

Trọng yếu (critical / 중요) tài nguyên (resource / 자원) nên có layered protection phù hợp: vòng đời (lifecycle / 생명주기) protection ở IaC, retention/backup ở dịch vụ (service / 서비스), chính sách (policy / 정책) hạn chế định danh (identity / 식별자) được destroy và rà soát (review / 검토) riêng cho destructive plan. Không một lớp nào đủ một mình vì emergency hoặc di chuyển (migration / 마이그레이션) thật sự vẫn có lúc cần phá protection.

Cấp cao (senior / 시니어) lập luận (reasoning / 추론) ở đây là phân biệt **reversible thay đổi (change / 변경)** và **irreversible thay đổi (change / 변경)**. Hai thay đổi có cùng số dòng diff nhưng rủi ro (risk / 위험) lớp (class / 클래스) hoàn toàn khác nhau.

## 20. Unknown giá trị (value / 값) là một phần ngữ nghĩa (semantics / 의미론) của plan

Có những thuộc tính chỉ biết sau khi tài nguyên (resource / 자원) được tạo, ví dụ generated ID, hostname, assigned IP hoặc provider-computed trường dữ liệu (field / 필드). Trong plan, chúng có thể ở trạng thái “known after apply”. Đây không phải lỗi hiển thị; nó phản ánh rằng engine chưa có đủ thông tin (information / 정보) để tính toàn bộ đồ thị (graph / 그래프) trước mutation.

Điều này quan trọng khi chính sách (policy / 정책) hoặc downstream tài nguyên (resource / 자원) phụ thuộc vào giá trị (value / 값) chưa biết. Một chính sách (policy / 정책) chỉ kiểm tra văn bản (text / 텍스트) plan mà giả định mọi trường dữ liệu (field / 필드) đã concrete có thể bỏ sót rủi ro (risk / 위험). Ngược lại, cố ép mọi giá trị (value / 값) thành known bằng dữ liệu (data / 데이터) lookup hoặc script ngoài có thể tạo hidden phụ thuộc (dependency / 의존성) mới.

Rà soát (review / 검토) IaC trưởng thành phân biệt ba trạng thái: giá trị (value / 값) đã biết từ cấu hình (config / 설정)/trạng thái (state / 상태), giá trị (value / 값) đọc từ remote hiện tại, và giá trị (value / 값) chỉ hình thành sau actuation. Confidence của plan phải tương ứng với mức thông tin (information / 정보) thật sự có sẵn.

## 21. Replacement thứ tự (ordering / 순서) là availability quyết định (decision / 결정), không chỉ vòng đời (lifecycle / 생명주기) flag

Khi một thuộc tính (property / 속성) bắt buộc replace tài nguyên (resource / 자원), có hai thứ tự (order / 순서) tổng quát: destroy old rồi create new, hoặc create replacement trước rồi retire old. `create-before-destroy` có thể giảm downtime nhưng chỉ hoạt động nếu provider cho phép hai tài nguyên (resource / 자원) cùng tồn tại, quota còn đủ và name/định danh (identity / 식별자) không xung đột (conflict / 충돌).

Với stateful tài nguyên (resource / 자원), tạo song song còn kéo theo dữ liệu (data / 데이터) sync/cutover. Với mạng (network / 네트워크) tuyến (route / 경로) hoặc singleton định danh (identity / 식별자), hai bản cùng tồn tại có thể tạo ambiguity. Vì vậy replacement chiến lược (strategy / 전략) phải dựa trên tài nguyên (resource / 자원) ngữ nghĩa (semantics / 의미론), không phải bật một flag chung cho mọi mô-đun (module / 모듈).

Một plan có chữ `replace` nên kích hoạt câu hỏi: có downtime không, có double-capacity headroom không, dữ liệu (data / 데이터)/trạng thái (state / 상태) chuyển thế nào, endpoint/định danh (identity / 식별자) cutover ra sao và quay lui (rollback / 롤백) mục tiêu (target / 대상) còn tồn tại bao lâu.

## 22. dữ liệu (data / 데이터) nguồn (source / 소스) và remote lookup có thể biến build-plan thành phụ thuộc (dependency / 의존성) thời gian chạy (runtime / 런타임)

IaC thường đọc thông tin từ tài nguyên (resource / 자원) ngoài quyền sở hữu (ownership / 소유권) của trạng thái (state / 상태) hiện tại: ảnh (image / 이미지) ID mới nhất, subnet được nhóm (team / 팀) khác tạo, secret siêu dữ liệu (metadata / 메타데이터) hoặc account dữ liệu (data / 데이터). Những lookup này tiện nhưng làm plan phụ thuộc trạng thái bên ngoài (external / 외부) tại thời điểm chạy.

Nếu truy vấn (query / 쿼리) “latest ảnh (image / 이미지)” trả giá trị mới vào ngày mai, cùng nguồn (source / 소스) lần ghi nhận (commit / 커밋) có thể plan khác. Nếu nhóm (team / 팀) khác rename/tag tài nguyên (resource / 자원), apply của bạn có thể thất bại (fail / 실패) dù mã (code / 코드) không đổi. Vì vậy remote lookup cũng phải có đặc tả hợp đồng (contract / 계약) về quyền sở hữu (ownership / 소유권), stability và versioning.

Khi reproducibility quan trọng, nên pin định danh (identity / 식별자) cụ thể hoặc promote giá trị (value / 값) qua giao diện (interface / 인터페이스) rõ thay vì truy vấn “mới nhất” ngầm. Đây là cùng nguyên tắc với sản phẩm tạo ra (artifact / 산출물) bản dựng (build / 빌드): hidden mutable đầu vào (input / 입력) làm bằng chứng (evidence / 증거) yếu đi.

## 23. trạng thái (state / 상태) khôi phục (recovery / 복구) phải tránh biến backup cũ thành authority sai

Backend trạng thái (state / 상태) được backup/versioned là cần thiết, nhưng restore trạng thái (state / 상태) snapshot cũ không tự động restore cloud tài nguyên (resource / 자원) về thời điểm cũ. Remote đối tượng (object / 객체) có thể đã thay đổi sau snapshot. Nếu nạp trạng thái (state / 상태) cũ rồi apply ngay, engine có thể đưa ra mutation nguy hiểm dựa trên ánh xạ (mapping / 매핑) stale.

Khôi phục (recovery / 복구) đúng thường tách hai bước: phục hồi siêu dữ liệu (metadata / 메타데이터) trạng thái (state / 상태) đủ để đọc được quyền sở hữu (ownership / 소유권), sau đó refresh/reconcile với actual remote trạng thái (state / 상태) trước khi cho phép destructive hành động (action / 동작). Với tài nguyên (resource / 자원) quan trọng, cần kiểm thử (test / 테스트) runbook “trạng thái (state / 상태) backend mất/corrupt” như một thất bại (failure / 실패) lớp (class / 클래스) riêng.

Trạng thái (state / 상태) backup bảo vệ **kiến thức (knowledge / 지식) về quyền sở hữu (ownership / 소유권)**, không phải backup dữ liệu (data / 데이터)/ứng dụng (application / 애플리케이션) tài nguyên (resource / 자원). Hai loại khôi phục (recovery / 복구) phải được thiết kế riêng.

## 24. chính sách (policy / 정책) trên plan và chính sách (policy / 정책) trên actual trạng thái (state / 상태) bảo vệ hai thời điểm khác nhau

Policy-as-code trước apply cho phản hồi (feedback / 피드백) sớm: cấm công khai (public / 공개) exposure, enforce tag, giới hạn instance lớp (class / 클래스) hoặc destroy. Nhưng plan có unknown giá trị (value / 값) và race; sau apply actual trạng thái (state / 상태) có thể khác vì provider default, bên ngoài (external / 외부) controller hoặc eventual hành vi (behavior / 동작).

Vì vậy trọng yếu (critical / 중요) bất biến (invariant / 불변식) có thể cần nhiều lớp: chính sách (policy / 정책) trong mã (code / 코드)/mô-đun (module / 모듈) default, chính sách (policy / 정책) ở plan/admission trước mutation, và continuous kiểm tra (audit / 감사) trên actual cloud trạng thái (state / 상태). Mục tiêu không phải duplicate mọi quy tắc (rule / 규칙) ba lần mà đặt enforcement tại ranh giới (boundary / 경계) nơi violation có thể phát sinh.

Một quy tắc (rule / 규칙) bảo mật (security / 보안) cần chặn trước creation khác với một quy tắc (rule / 규칙) hygiene có thể detect rồi remediate sau. Fail-closed hay eventual remediation là rủi ro (risk / 위험) quyết định (decision / 결정), không chỉ lựa chọn công cụ (tool / 도구).

## 25. cấp cao (senior / 시니어) walkthrough: plan “không downtime” nhưng apply vẫn kẹt vì quota

Giả sử mô-đun (module / 모듈) thay launch cấu hình (configuration / 구성) và dùng replacement trước khi destroy để giữ sức chứa (capacity / 용량). Plan trông an toàn: tạo 20 instance mới rồi bỏ 20 instance cũ. Nhưng account chỉ còn quota cho 5 instance. Apply tạo 5 rồi provider reject phần còn lại; old fleet vẫn tồn tại nhưng rollout mắc giữa chừng.

Thất bại (failure / 실패) không nằm ở diff nghiệp vụ (business / 비즈니스) mà ở **temporary sức chứa (capacity / 용량) required by chuyển tiếp (transition / 전이)**. Safe-change rà soát (review / 검토) phải tính steady-state sức chứa (capacity / 용량) và transition-state sức chứa (capacity / 용량) riêng. Canary, surge, replacement, DR failover đều có cùng mẫu (pattern / 패턴): an toàn (safety / 안전) thường cần headroom tạm thời.

Bài học tổng quát là IaC plan cần được đọc như một chuyển tiếp trạng thái (state transition / 상태 전이) có tài nguyên (resource / 자원)/thời gian (time / 시간)/thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론), không phải như ảnh chụp before/after.

> **Bàn giao:** Sau **25. cấp cao (senior / 시니어) walkthrough: plan “không downtime” nhưng apply vẫn kẹt vì quota**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 cloud primitives identity network compute storage](./01_cloud_primitives_identity_network_compute_storage.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
