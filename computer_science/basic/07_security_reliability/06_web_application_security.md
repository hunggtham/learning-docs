# Web ứng dụng (application / 애플리케이션) bảo mật (security / 보안)

> **Mạch đọc:** Đọc **Web ứng dụng (application / 애플리케이션) bảo mật (security / 보안)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Same-Origin chính sách (policy / 정책)** sang **XSS: dữ liệu (data / 데이터) trở thành mã (code / 코드)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Web bảo mật (security / 보안) không phải danh sách payloads như `' OR 1=1`. Nó bắt đầu từ trust boundaries: trình duyệt (browser / 브라우저) chạy mã (code / 코드) từ nhiều origins, máy chủ (server / 서버) nhận đầu vào (input / 입력) từ clients không đáng tin, cookies/tokens đi qua mạng (network / 네트워크), backend truy cập cơ sở dữ liệu (database / 데이터베이스) và bên ngoài (external / 외부) services. Vulnerability xuất hiện khi dữ liệu (data / 데이터) vượt ranh giới (boundary / 경계) mà các giả định (assumptions / 가정들) không được enforce.

## Same-Origin chính sách (policy / 정책)

Trình duyệt (browser / 브라우저) Same-Origin chính sách (policy / 정책) (SOP) giới hạn script từ một origin đọc resources của origin khác. Origin thường được xác định bởi scheme + host + cổng (port / 포트).

SOP là isolation ranh giới (boundary / 경계) của nền tảng Web (web platform / 웹 플랫폼). CORS không “bật bảo mật (security / 보안)”; nó là cơ chế (mechanism / 메커니즘) máy chủ (server / 서버) dùng để nới quyền cross-origin read cho origins được phép.


> **Chuyển mạch:** Từ **Same-Origin chính sách (policy / 정책)**, ta sang **XSS: dữ liệu (data / 데이터) trở thành mã (code / 코드)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## XSS: dữ liệu (data / 데이터) trở thành mã (code / 코드)

Cross-Site Scripting xảy ra khi attacker-controlled dữ liệu (data / 데이터) được trình thông dịch (interpreter / 인터프리터) của trình duyệt (browser / 브라우저) coi là executable script/markup trong ngữ cảnh (context / 맥락) không intended.

Defense cốt lõi là context-aware đầu ra (output / 출력) encoding và tránh dangerous sinks. HTML văn bản (text / 텍스트), HTML attribute, JavaScript string và URL contexts cần encoding khác nhau.

Content bảo mật (security / 보안) chính sách (policy / 정책) (CSP) thêm defense-in-depth bằng cách giới hạn sources/thực thi (execution / 실행) modes, nhưng không thay thế đầu ra (output / 출력) an toàn (safety / 안전).


> **Chuyển mạch:** Từ **XSS: dữ liệu (data / 데이터) trở thành mã (code / 코드)**, ta sang **CSRF: trình duyệt (browser / 브라우저) mang credentials ngoài ý muốn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## CSRF: trình duyệt (browser / 브라우저) mang credentials ngoài ý muốn

Cross-Site yêu cầu (request / 요청) Forgery lợi dụng việc trình duyệt (browser / 브라우저) tự động gửi credentials như cookies tới mục tiêu (target / 대상) site khi người dùng (user / 사용자) bị dụ tạo yêu cầu (request / 요청) từ site khác.

Defenses gồm SameSite cookies, anti-CSRF tokens và checking origin/referer trong phù hợp ngữ cảnh (context / 맥락). Nếu auth dùng bearer đơn vị từ (token / 토큰) chỉ gửi qua tường minh (explicit / 명시적) JavaScript header và attacker site không đọc đơn vị từ (token / 토큰), threat mô hình (model / 모델) khác.


> **Chuyển mạch:** Từ **CSRF: trình duyệt (browser / 브라우저) mang credentials ngoài ý muốn**, ta sang **SQL/command injection** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## SQL/command injection

Injection xảy ra khi untrusted dữ liệu (data / 데이터) được concatenate vào ngôn ngữ (language / 언어)/mã (code / 코드) ngữ cảnh (context / 맥락). Prepared statements tách truy vấn (query / 쿼리) cấu trúc (structure / 구조) khỏi dữ liệu (data / 데이터) parameters.

Same principle áp dụng shell command, LDAP, template và expression languages: **dữ liệu (data / 데이터) không được trở thành cú pháp (syntax / 문법) ngoài ý muốn**.


> **Chuyển mạch:** Từ **SQL/command injection**, ta sang **SSRF và trust vào mạng (network / 네트워크) location** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## SSRF và trust vào mạng (network / 네트워크) location

Server-Side yêu cầu (request / 요청) Forgery làm backend fetch attacker-controlled destination. Nếu backend có quyền truy cập (access / 접근) nội bộ (internal / 내부) siêu dữ liệu (metadata / 메타데이터)/admin services, attacker piggybacks trust của máy chủ (server / 서버).

Defense cần URL kiểm tra hợp lệ (validation / 검증), mạng (network / 네트워크) egress chính sách (policy / 정책), allowlist và protection against DNS rebinding/redirect tricks tùy threat mô hình (model / 모델).


> **Chuyển mạch:** Từ **SSRF và trust vào mạng (network / 네트워크) location**, ta sang **Session bảo mật (security / 보안)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Session bảo mật (security / 보안)

Session ID/đơn vị từ (token / 토큰) là bearer năng lực (capability / 역량): ai sở hữu có thể impersonate người dùng (user / 사용자) trong phạm vi quyền. Tokens cần entropy đủ, secure vận chuyển (transport / 전송), appropriate thời gian tồn tại (lifetime / 수명), rotation/revocation chiến lược (strategy / 전략).

Cookie flags `Secure`, `HttpOnly`, `SameSite` bảo vệ các threat khác nhau. `HttpOnly` giảm script truy cập (access / 접근) nhưng không làm XSS vô hại vì injected script vẫn có thể gửi requests dưới session.


> **Chuyển mạch:** Từ **Session bảo mật (security / 보안)**, ta sang **Authentication không kết thúc ở login** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Authentication không kết thúc ở login

Password reset, email thay đổi (change / 변경), MFA khôi phục (recovery / 복구) và account linking đều là authentication flows. Attacker thường tìm weakest khôi phục (recovery / 복구) đường dẫn (path / 경로) thay vì phá strongest login đường dẫn (path / 경로).

Authorization phải check server-side trên mỗi sensitive đối tượng (object / 객체)/hành động (action / 동작). Hidden button trong UI không phải kiểm soát truy cập (access control / 접근 제어).


> **Chuyển mạch:** Từ **Authentication không kết thúc ở login**, ta sang **tệp (file / 파일) upload** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tệp (file / 파일) upload

Upload tệp (file / 파일) kết hợp content-type ambiguity, parser bugs, đường dẫn (path / 경로) traversal, executable content và lưu trữ (storage / 저장소) permissions. Safe thiết kế (design / 설계) thường tách upload lưu trữ (storage / 저장소) khỏi executable web gốc (root / 루트), rename generated IDs, validate kiểu (type / 타입)/content và scan/tiến trình (process / 프로세스) trong constrained môi trường (environment / 환경).


> **Chuyển mạch:** Từ **tệp (file / 파일) upload**, ta sang **bảo mật (security / 보안) headers và trình duyệt (browser / 브라우저) primitives** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bảo mật (security / 보안) headers và trình duyệt (browser / 브라우저) primitives

HSTS ép HTTPS cho future requests; CSP giới hạn content thực thi (execution / 실행); frame-ancestors/X-Frame-Options giảm clickjacking; Referrer-Policy kiểm soát referrer leakage.

Headers chỉ hiệu quả khi hiểu threat tương ứng, không phải checklist score.


> **Chuyển mạch:** Từ **bảo mật (security / 보안) headers và trình duyệt (browser / 브라우저) primitives**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Frontend kiểm tra hợp lệ (validation / 검증) đủ vì người dùng (user / 사용자) không sửa được UI.”** máy khách (client / 클라이언트) hoàn toàn attacker-controlled.

**“JWT an toàn hơn session.”** JWT chỉ là đơn vị từ (token / 토큰) format/signing mô hình (model / 모델); vòng đời (lifecycle / 생명주기), lưu trữ (storage / 저장소), revocation và authorization vẫn quyết định bảo mật (security / 보안).

**“HTTPS ngăn XSS/SQL injection.”** TLS bảo vệ dữ liệu (data / 데이터) in transit, không sửa ứng dụng (application / 애플리케이션) lô-gic (logic / 논리).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Web bảo mật (security / 보안) là kiểm soát trình thông dịch (interpreter / 인터프리터) boundaries, origin boundaries, credential boundaries và authorization boundaries. Mỗi lần dữ liệu (data / 데이터) đổi ngữ cảnh (context / 맥락), phải hỏi ai kiểm soát nó và thành phần (component / 컴포넌트) tiếp theo sẽ diễn giải nó như dữ liệu (data / 데이터) hay mã (code / 코드).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [threat models](./00_threat_models_and_security_principles.md), [identity/auth](./02_identity_authentication_and_authorization.md), [software vulnerabilities](./03_software_vulnerabilities.md) và [HTTP/TLS](../06_networks_distributed_systems/03_dns_http_tls_and_web_request.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 threat models and security principles](./00_threat_models_and_security_principles.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
