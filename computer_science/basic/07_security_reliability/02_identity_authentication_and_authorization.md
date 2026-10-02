# Danh tính, xác thực và phân quyền

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Identity, authentication và authorization**. Route đi từ identity claims → authentication factors → authorization policy/scope → sessions/cookies → OAuth/OIDC và service identity, để “ai là ai” được tách khỏi “được làm gì”.

Hệ thống danh tính cần trả lời ba câu hỏi khác nhau: **đây là ai hoặc thực thể nào, họ chứng minh danh tính bằng gì, và họ được phép làm gì?** Nhầm lẫn giữa **xác thực (authentication)** và **phân quyền (authorization)** là nguyên nhân phổ biến của lỗi bảo mật.

## Danh tính

**Danh tính (identity / 신원)** là định danh tương đối ổn định cho người dùng, dịch vụ, thiết bị hoặc khối lượng công việc trong một miền quản lý. Tên đăng nhập hoặc email có thể thay đổi, vì vậy mã định danh chủ thể nội bộ (subject ID) thường phù hợp hơn cho liên kết lâu dài.

Danh tính có vòng đời: cấp mới, đăng ký thông tin xác thực, thay đổi vai trò, tạm khóa và xóa. Tài khoản hoặc khóa bị bỏ quên sau khi không còn sử dụng là một rủi ro bảo mật.

> **Chuyển mạch:** Trong **Danh tính, xác thực và phân quyền**, **Xác thực** tiếp nhận điểm tựa từ **Danh tính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân quyền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xác thực

**Xác thực (authentication / 인증)** kiểm tra rằng bên đang yêu cầu thực sự kiểm soát thông tin hoặc yếu tố xác thực gắn với danh tính. Mật khẩu, khóa phần cứng, TOTP, chứng chỉ và sinh trắc học là các cơ chế khác nhau với mô hình đe dọa khác nhau.

Các yếu tố thường được chia thành thứ người dùng biết, thứ người dùng sở hữu và đặc điểm của chính người dùng. **Xác thực đa yếu tố (Multi-Factor Authentication — MFA)** mạnh khi các yếu tố đủ độc lập; mật khẩu và PIN đi qua cùng một kênh không tự động tạo thành hai yếu tố độc lập có ý nghĩa.

Một lần đăng nhập thành công không có nghĩa phiên làm việc sẽ đáng tin vô thời hạn. Sự kiện xác thực luôn có mức bảo đảm, thời điểm và bối cảnh cụ thể.

> **Chuyển mạch:** Ở chặng này của **Danh tính, xác thực và phân quyền**, **Phân quyền** tiếp nhận điểm tựa từ **Xác thực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xác thực không đồng nghĩa với phân quyền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân quyền

**Phân quyền (authorization / 인가)** quyết định một hành động trên một tài nguyên có được phép hay không. Một số mô hình phổ biến gồm:

- **RBAC**: quyền gắn với vai trò, danh tính nhận vai trò.
- **ABAC**: chính sách dựa trên thuộc tính của chủ thể, tài nguyên, môi trường và hành động.
- **ACL**: tài nguyên liệt kê chủ thể và quyền tương ứng.
- **Capability-based**: việc sở hữu một đơn vị từ (token / 토큰) hoặc tham chiếu không thể giả mạo trao quyền thực hiện hành động nhất định.

Hệ thống thực tế thường kết hợp nhiều mô hình.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính, xác thực và phân quyền**, **Xác thực không đồng nghĩa với phân quyền** tiếp nhận điểm tựa từ **Phân quyền** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phiên làm việc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xác thực không đồng nghĩa với phân quyền

Máy chủ có thể biết yêu cầu đến từ người dùng 123 nhưng vẫn phải kiểm tra người dùng 123 có quyền đọc đơn hàng 999 hay không. Các lỗ hổng IDOR/BOLA xuất hiện khi endpoint nhận mã đối tượng rồi chỉ kiểm tra người dùng đã đăng nhập, nhưng không kiểm tra quyền sở hữu hoặc chính sách truy cập đối tượng.

Mỗi lần truy cập tài nguyên cần được kiểm tra quyền đầy đủ tại điểm thực thi, thay vì chỉ dựa vào giao diện phía người dùng.

> **Chuyển mạch:** Trong **Danh tính, xác thực và phân quyền**, **Phiên làm việc** tiếp nhận điểm tựa từ **Xác thực không đồng nghĩa với phân quyền** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cookie và bảo mật trình duyệt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phiên làm việc

Sau khi xác thực, máy chủ có thể tạo **mã phiên (session ID)** và lưu nó trong cookie, trong khi trạng thái phiên nằm ở phía máy chủ. Hệ thống dựa trên đơn vị từ (token / 토큰) có thể mang các tuyên bố đã ký, ví dụ JWT, nhưng đơn vị từ (token / 토큰) vẫn phải được kiểm tra chữ ký, bên phát hành, đối tượng nhận, thời hạn, thời điểm có hiệu lực, trạng thái khóa và bối cảnh phân quyền.

JWT không tự làm hệ thống trở thành “không trạng thái” nếu việc thu hồi đơn vị từ (token / 토큰), trạng thái người dùng, quyền hoặc refresh đơn vị từ (token / 토큰) vẫn cần dữ liệu phía máy chủ.

> **Chuyển mạch:** Ở chặng này của **Danh tính, xác thực và phân quyền**, **Cookie và bảo mật trình duyệt** tiếp nhận điểm tựa từ **Phiên làm việc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác về OAuth 2.0 và OpenID Connect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cookie và bảo mật trình duyệt

Thuộc tính `HttpOnly` hạn chế JavaScript truy cập cookie; `Secure` yêu cầu cookie chỉ được gửi qua HTTPS; `SameSite` kiểm soát việc gửi cookie trong ngữ cảnh khác trang và hỗ trợ phòng chống CSRF. Mã phiên phải khó đoán và được bảo vệ khỏi đánh cắp hoặc cố định phiên.

**CSRF** lợi dụng việc trình duyệt tự động đính kèm thông tin xác thực vào yêu cầu khác trang. đơn vị từ (token / 토큰) chống CSRF, `SameSite` và kiểm tra nguồn yêu cầu có thể giảm rủi ro tùy kiến trúc. **XSS** có thể thực hiện hành động dưới danh nghĩa người dùng và đọc dữ liệu không được `HttpOnly` bảo vệ, vì vậy phòng chống XSS vẫn rất quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính, xác thực và phân quyền**, **Trực giác về OAuth 2.0 và OpenID Connect** tiếp nhận điểm tựa từ **Cookie và bảo mật trình duyệt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Danh tính dịch vụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác về OAuth 2.0 và OpenID Connect

OAuth 2.0 là **khung phân quyền ủy quyền (delegated authorization framework)**; OpenID Connect (OIDC) bổ sung tầng danh tính và xác thực với ID đơn vị từ (token / 토큰) cùng các endpoint chuẩn. Không nên dùng truy cập (access / 접근) đơn vị từ (token / 토큰) của OAuth như một đơn vị từ (token / 토큰) đăng nhập tùy ý nếu chưa kiểm tra đúng mục đích và ngữ nghĩa của nó.

Luồng Authorization mã (code / 코드) kết hợp PKCE là lựa chọn phổ biến cho nhiều ứng dụng công khai. Khuyến nghị triển khai có thể thay đổi theo đặc tả và nhà cung cấp, vì vậy cần theo tài liệu hiện hành của hệ thống được sử dụng.

> **Chuyển mạch:** Trong **Danh tính, xác thực và phân quyền**, **Danh tính dịch vụ** tiếp nhận điểm tựa từ **Trực giác về OAuth 2.0 và OpenID Connect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đặc quyền tối thiểu và phạm vi quyền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Danh tính dịch vụ

Microservice cũng cần danh tính máy. Các lựa chọn gồm chứng chỉ mTLS, danh tính khối lượng công việc (workload identity), đơn vị từ (token / 토큰) ngắn hạn hoặc IAM của nền tảng cloud. Chia sẻ một API key tĩnh cho nhiều dịch vụ làm mất khả năng truy vết và khiến việc xoay vòng khóa trở nên thô và rủi ro.

> **Chuyển mạch:** Ở chặng này của **Danh tính, xác thực và phân quyền**, **Đặc quyền tối thiểu và phạm vi quyền** tiếp nhận điểm tựa từ **Danh tính dịch vụ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đặc quyền tối thiểu và phạm vi quyền

Phạm vi đơn vị từ (token / 토큰) và vai trò nên giới hạn đúng những gì chủ thể cần làm. Thông tin xác thực sống ngắn giảm thời gian bị khai thác nếu rò rỉ, nhưng cơ chế làm mới và xoay vòng trở thành phần quan trọng của thiết kế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính, xác thực và phân quyền**, **Mô hình tư duy** gom các mảnh từ **Đặc quyền tối thiểu và phạm vi quyền** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Danh tính = chủ thể. Xác thực = chứng minh quyền kiểm soát danh tính. Phân quyền = quyết định chính sách cho hành động trên tài nguyên. Phiên hoặc đơn vị từ (token / 토큰) = mang bằng chứng và bối cảnh theo thời gian.** Hãy giữ các tầng này tách biệt trong thiết kế.

> **Chuyển mạch:** Trong **Danh tính, xác thực và phân quyền**, **Những hiểu lầm thường gặp** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm thường gặp

**“Người dùng đã xác thực có thể truy cập mọi mã đối tượng họ biết.”** Xác thực chỉ cho biết người dùng là ai, không cho biết họ có quyền với tài nguyên nào.

**“JWT luôn được mã hóa.”** JWT dạng JWS thông thường được ký nhưng phần payload vẫn có thể đọc; JWE là cơ chế mã hóa riêng.

**“OAuth = xác thực.”** OAuth cốt lõi giải quyết phân quyền ủy quyền; OIDC bổ sung ngữ nghĩa xác thực và danh tính.

> **Chuyển mạch:** Ở chặng này của **Danh tính, xác thực và phân quyền**, **Kết nối** tiếp nhận điểm tựa từ **Những hiểu lầm thường gặp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc thêm về ranh giới tin cậy trong [nguyên tắc bảo mật](./00_threat_models_and_security_principles.md), đơn vị từ (token / 토큰) và chứng chỉ trong [mật mã học](./01_cryptography_foundations.md), kênh trình duyệt trong [DNS/HTTP/TLS](../06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) và các kiểu tấn công ứng dụng trong [lỗ hổng phần mềm](./03_software_vulnerabilities.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
