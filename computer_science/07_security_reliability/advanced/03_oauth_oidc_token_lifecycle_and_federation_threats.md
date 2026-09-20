# OAuth, OIDC, vòng đời token và rủi ro liên kết danh tính

OAuth 2.x và OpenID Connect thường bị gom thành “đăng nhập bằng token”, nhưng chúng giải quyết các bài toán khác nhau. OAuth chủ yếu cung cấp **ủy quyền được ủy nhiệm (delegated authorization)**; OIDC bổ sung lớp danh tính để ứng dụng khách biết người dùng đã được xác thực là ai.

## Các vai trò trong OAuth

OAuth tách ứng dụng muốn gọi API khỏi máy chủ cấp quyền. Ứng dụng khách (client) nhận access token có phạm vi và đối tượng nhận cụ thể rồi gửi token đó tới máy chủ tài nguyên (resource server).

Token không nên được hiểu là “mật khẩu mới dùng ở mọi nơi”. Nó có bên phát hành, đối tượng nhận, thời hạn và tập quyền cụ thể.

## Authorization Code và PKCE

Ứng dụng công khai như mobile app hoặc ứng dụng chạy trong trình duyệt không thể giữ `client secret` thật sự bí mật. **PKCE (Proof Key for Code Exchange)** tạo cặp verifier/challenge để nếu authorization code bị chặn, kẻ tấn công khác vẫn khó đổi mã đó thành token.

Tính an toàn đến từ việc ràng buộc bước đổi mã với chính phiên client đã bắt đầu luồng, không phải từ việc nhúng một secret tĩnh vào file ứng dụng.

## OIDC và ID token

OIDC bổ sung **ID token** chứa các claim về sự kiện xác thực và danh tính người dùng. ID token dành cho client kiểm tra danh tính; access token dành cho API kiểm tra quyền truy cập. Dùng ID token như một bearer token chung cho API làm lẫn ranh giới tin cậy và đối tượng nhận.

## Xác minh token

Resource server cần kiểm tra chữ ký hoặc MAC theo giao thức, bên phát hành, đối tượng nhận, thời hạn và các claim liên quan. Chỉ giải mã phần Base64 của JWT không phải là xác minh.

Xoay khóa (key rotation) yêu cầu chiến lược dùng JWKS và cache phù hợp. Cache quá lâu có thể giữ khóa đã bị thu hồi; tải khóa lại ở mọi yêu cầu lại tạo thêm dependency và độ trễ.

## Refresh token

Access token sống ngắn làm giảm khoảng thời gian token bị lộ có thể bị lạm dụng, nhưng cần cơ chế làm mới. **Refresh token** thường có quyền mạnh hơn và sống lâu hơn, nên việc xoay token, thu hồi và lưu trữ an toàn đặc biệt quan trọng.

Cơ chế phát hiện tái sử dụng refresh token có thể giúp nhận ra một “họ token” đã bị đánh cắp trong mô hình rotation.

## Bearer token và bằng chứng sở hữu

**Bearer token** trao quyền cho bất kỳ ai đang giữ token. Nếu token rò qua log, vùng lưu trữ trình duyệt hoặc proxy, kẻ tấn công có thể phát lại token trong thời hạn còn hiệu lực.

Token ràng buộc mTLS hoặc cơ chế kiểu DPoP cố gắn token với một khóa và bằng chứng từ client, giảm khả năng phát lại nhưng làm giao thức và vận hành phức tạp hơn.

## Rủi ro trong liên kết danh tính

Open redirect, mix-up attack, CSRF trong luồng redirect, dùng sai `nonce`/`state` và bài toán confused deputy xuất hiện vì nhiều bên trao đổi qua trình duyệt, kênh phía trước và kênh phía sau.

`state` giúp ràng buộc phản hồi ủy quyền với giao dịch mà client đã bắt đầu; `nonce` của OIDC giúp ràng buộc ID token với yêu cầu xác thực. Hai trường này bảo vệ các mối đe dọa khác nhau.

## Scope không thay thế mô hình phân quyền

Scope thường chỉ mô tả quyền ở mức khá thô. API vẫn cần phân quyền ở cấp đối tượng: người dùng có `read:account` không có nghĩa họ được đọc tài khoản của người khác.

Xác thực trả lời “đây là ai”; phân quyền trả lời “thực thể này được làm gì với tài nguyên nào trong ngữ cảnh nào”.

## Mô hình tư duy

> OAuth/OIDC là giao thức liên kết nhiều ranh giới tin cậy. Token chỉ an toàn khi bên phát hành, đối tượng nhận, thời hạn, cơ chế ràng buộc và luồng chuyển hướng đều đúng. Đừng suy luận từ hình dạng JWT; hãy suy luận từ quyền lực được trao và những nơi token có thể bị phát lại.