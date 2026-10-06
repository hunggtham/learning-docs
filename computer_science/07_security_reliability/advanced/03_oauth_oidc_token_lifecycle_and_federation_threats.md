# OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Các vai trò trong OAuth** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Authorization mã (code / 코드) và PKCE** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối OAuth/OIDC với token lifecycle, federation và threats, để identity flow được kiểm soát từ cấp token đến thu hồi.

OAuth 2.x và OpenID Connect thường bị gom thành “đăng nhập bằng đơn vị từ (token / 토큰)”, nhưng chúng giải quyết các bài toán khác nhau. OAuth chủ yếu cung cấp **ủy quyền được ủy nhiệm (delegated authorization)**; OIDC bổ sung lớp danh tính để ứng dụng khách biết người dùng đã được xác thực là ai.

## Các vai trò trong OAuth

OAuth tách ứng dụng muốn gọi API khỏi máy chủ cấp quyền. Ứng dụng khách (client) nhận truy cập (access / 접근) đơn vị từ (token / 토큰) có phạm vi và đối tượng nhận cụ thể rồi gửi đơn vị từ (token / 토큰) đó tới máy chủ tài nguyên (resource server).

Đơn vị từ (token / 토큰) không nên được hiểu là “mật khẩu mới dùng ở mọi nơi”. Nó có bên phát hành, đối tượng nhận, thời hạn và tập quyền cụ thể.

> **Nối mạch:** **Authorization mã (code / 코드) và PKCE** nối từ **Các vai trò trong OAuth** sang **OIDC và ID đơn vị từ (token / 토큰)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Authorization mã (code / 코드) và PKCE

Ứng dụng công khai như mobile app hoặc ứng dụng chạy trong trình duyệt không thể giữ `client secret` thật sự bí mật. **PKCE (Proof Key for Code Exchange)** tạo cặp verifier/challenge để nếu authorization mã (code / 코드) bị chặn, kẻ tấn công khác vẫn khó đổi mã đó thành đơn vị từ (token / 토큰).

Tính an toàn đến từ việc ràng buộc bước đổi mã với chính phiên máy khách (client / 클라이언트) đã bắt đầu luồng, không phải từ việc nhúng một secret tĩnh vào tệp (file / 파일) ứng dụng.

> **Nối mạch:** **OIDC và ID đơn vị từ (token / 토큰)** nối từ **Authorization mã (code / 코드) và PKCE** sang **Xác minh đơn vị từ (token / 토큰)**, vì cơ chế trước tạo đầu vào cho bước sau.

## OIDC và ID đơn vị từ (token / 토큰)

OIDC bổ sung **ID đơn vị từ (token / 토큰)** chứa các claim về sự kiện xác thực và danh tính người dùng. ID đơn vị từ (token / 토큰) dành cho máy khách (client / 클라이언트) kiểm tra danh tính; truy cập (access / 접근) đơn vị từ (token / 토큰) dành cho API kiểm tra quyền truy cập. Dùng ID đơn vị từ (token / 토큰) như một bearer đơn vị từ (token / 토큰) chung cho API làm lẫn ranh giới tin cậy và đối tượng nhận.

> **Nối mạch:** **Xác minh đơn vị từ (token / 토큰)** nối từ **OIDC và ID đơn vị từ (token / 토큰)** sang **Refresh đơn vị từ (token / 토큰)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Xác minh đơn vị từ (token / 토큰)

Tài nguyên (resource / 자원) máy chủ (server / 서버) cần kiểm tra chữ ký hoặc MAC theo giao thức, bên phát hành, đối tượng nhận, thời hạn và các claim liên quan. Chỉ giải mã phần Base64 của JWT không phải là xác minh.

Xoay khóa (key rotation) yêu cầu chiến lược dùng JWKS và bộ nhớ đệm (cache / 캐시) phù hợp. bộ nhớ đệm (cache / 캐시) quá lâu có thể giữ khóa đã bị thu hồi; tải khóa lại ở mọi yêu cầu lại tạo thêm phụ thuộc (dependency / 의존성) và độ trễ.

> **Nối mạch:** **Refresh đơn vị từ (token / 토큰)** nối từ **Xác minh đơn vị từ (token / 토큰)** sang **Bearer đơn vị từ (token / 토큰) và bằng chứng sở hữu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Refresh đơn vị từ (token / 토큰)

Truy cập (access / 접근) đơn vị từ (token / 토큰) sống ngắn làm giảm khoảng thời gian đơn vị từ (token / 토큰) bị lộ có thể bị lạm dụng, nhưng cần cơ chế làm mới. **Refresh đơn vị từ (token / 토큰)** thường có quyền mạnh hơn và sống lâu hơn, nên việc xoay đơn vị từ (token / 토큰), thu hồi và lưu trữ an toàn đặc biệt quan trọng.

Cơ chế phát hiện tái sử dụng refresh đơn vị từ (token / 토큰) có thể giúp nhận ra một “họ đơn vị từ (token / 토큰)” đã bị đánh cắp trong mô hình rotation.

> **Nối mạch:** **Refresh đơn vị từ (token / 토큰)** đặt vấn đề; **Bearer đơn vị từ (token / 토큰) và bằng chứng sở hữu** kiểm tra bằng chứng, rồi **Rủi ro trong liên kết danh tính** mở rộng hệ quả.

## Bearer đơn vị từ (token / 토큰) và bằng chứng sở hữu

**Bearer đơn vị từ (token / 토큰)** trao quyền cho bất kỳ ai đang giữ đơn vị từ (token / 토큰). Nếu đơn vị từ (token / 토큰) rò qua log, vùng lưu trữ trình duyệt hoặc proxy, kẻ tấn công có thể phát lại đơn vị từ (token / 토큰) trong thời hạn còn hiệu lực.

Đơn vị từ (token / 토큰) ràng buộc mTLS hoặc cơ chế kiểu DPoP cố gắn đơn vị từ (token / 토큰) với một khóa và bằng chứng từ máy khách (client / 클라이언트), giảm khả năng phát lại nhưng làm giao thức và vận hành phức tạp hơn.

> **Nối mạch:** **Bearer đơn vị từ (token / 토큰) và bằng chứng sở hữu** đặt vấn đề; **Rủi ro trong liên kết danh tính** kiểm tra bằng chứng, rồi **Phạm vi (scope / 범위) không thay thế mô hình phân quyền** mở rộng hệ quả.

## Rủi ro trong liên kết danh tính

Open redirect, mix-up attack, CSRF trong luồng redirect, dùng sai `nonce`/`state` và bài toán confused deputy xuất hiện vì nhiều bên trao đổi qua trình duyệt, kênh phía trước và kênh phía sau.

`state` giúp ràng buộc phản hồi ủy quyền với giao dịch mà máy khách (client / 클라이언트) đã bắt đầu; `nonce` của OIDC giúp ràng buộc ID đơn vị từ (token / 토큰) với yêu cầu xác thực. Hai trường này bảo vệ các mối đe dọa khác nhau.

> **Nối mạch:** **Phạm vi (scope / 범위) không thay thế mô hình phân quyền** nối từ **Rủi ro trong liên kết danh tính** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phạm vi (scope / 범위) không thay thế mô hình phân quyền

Phạm vi (scope / 범위) thường chỉ mô tả quyền ở mức khá thô. API vẫn cần phân quyền ở cấp đối tượng: người dùng có `read:account` không có nghĩa họ được đọc tài khoản của người khác.

Xác thực trả lời “đây là ai”; phân quyền trả lời “thực thể này được làm gì với tài nguyên nào trong ngữ cảnh nào”.

> **Nối mạch:** **Mô hình tư duy** tổng hợp từ **Phạm vi (scope / 범위) không thay thế mô hình phân quyền**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> OAuth/OIDC là giao thức liên kết nhiều ranh giới tin cậy. đơn vị từ (token / 토큰) chỉ an toàn khi bên phát hành, đối tượng nhận, thời hạn, cơ chế ràng buộc và luồng chuyển hướng đều đúng. Đừng suy luận từ hình dạng JWT; hãy suy luận từ quyền lực được trao và những nơi đơn vị từ (token / 토큰) có thể bị phát lại.

> **Bàn giao:** Giữ lại client binding, redirect/PKCE, issuer/audience/nonce validation, refresh rotation và object-level authorization trước khi tin một token. Sang [PKI/mTLS](./02_pki_certificate_validation_mtls_and_service_identity.md) khi identity cần bind vào channel/service, hoặc [Browser isolation](./05_browser_isolation_csp_samesite_and_cross_origin_trust.md) khi token đi qua ambient browser credentials; quay về [README](./README.md) để xác nhận owner.
