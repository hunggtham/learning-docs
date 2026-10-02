# OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Các vai trò trong OAuth** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Authorization mã (code / 코드) và PKCE** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối OAuth/OIDC với token lifecycle, federation và threats, để identity flow được kiểm soát từ cấp token đến thu hồi.

OAuth 2.x và OpenID Connect thường bị gom thành “đăng nhập bằng đơn vị từ (token / 토큰)”, nhưng chúng giải quyết các bài toán khác nhau. OAuth chủ yếu cung cấp **ủy quyền được ủy nhiệm (delegated authorization)**; OIDC bổ sung lớp danh tính để ứng dụng khách biết người dùng đã được xác thực là ai.

## Các vai trò trong OAuth

OAuth tách ứng dụng muốn gọi API khỏi máy chủ cấp quyền. Ứng dụng khách (client) nhận truy cập (access / 접근) đơn vị từ (token / 토큰) có phạm vi và đối tượng nhận cụ thể rồi gửi đơn vị từ (token / 토큰) đó tới máy chủ tài nguyên (resource server).

Đơn vị từ (token / 토큰) không nên được hiểu là “mật khẩu mới dùng ở mọi nơi”. Nó có bên phát hành, đối tượng nhận, thời hạn và tập quyền cụ thể.

> **Chuyển mạch:** Trong **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**, **Authorization mã (code / 코드) và PKCE** tiếp nhận điểm tựa từ **Các vai trò trong OAuth** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **OIDC và ID đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Authorization mã (code / 코드) và PKCE

Ứng dụng công khai như mobile app hoặc ứng dụng chạy trong trình duyệt không thể giữ `client secret` thật sự bí mật. **PKCE (Proof Key for Code Exchange)** tạo cặp verifier/challenge để nếu authorization mã (code / 코드) bị chặn, kẻ tấn công khác vẫn khó đổi mã đó thành đơn vị từ (token / 토큰).

Tính an toàn đến từ việc ràng buộc bước đổi mã với chính phiên máy khách (client / 클라이언트) đã bắt đầu luồng, không phải từ việc nhúng một secret tĩnh vào tệp (file / 파일) ứng dụng.

> **Chuyển mạch:** Ở chặng này của **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**, **OIDC và ID đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **Authorization mã (code / 코드) và PKCE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xác minh đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OIDC và ID đơn vị từ (token / 토큰)

OIDC bổ sung **ID đơn vị từ (token / 토큰)** chứa các claim về sự kiện xác thực và danh tính người dùng. ID đơn vị từ (token / 토큰) dành cho máy khách (client / 클라이언트) kiểm tra danh tính; truy cập (access / 접근) đơn vị từ (token / 토큰) dành cho API kiểm tra quyền truy cập. Dùng ID đơn vị từ (token / 토큰) như một bearer đơn vị từ (token / 토큰) chung cho API làm lẫn ranh giới tin cậy và đối tượng nhận.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**, **Xác minh đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **OIDC và ID đơn vị từ (token / 토큰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Refresh đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xác minh đơn vị từ (token / 토큰)

Tài nguyên (resource / 자원) máy chủ (server / 서버) cần kiểm tra chữ ký hoặc MAC theo giao thức, bên phát hành, đối tượng nhận, thời hạn và các claim liên quan. Chỉ giải mã phần Base64 của JWT không phải là xác minh.

Xoay khóa (key rotation) yêu cầu chiến lược dùng JWKS và bộ nhớ đệm (cache / 캐시) phù hợp. bộ nhớ đệm (cache / 캐시) quá lâu có thể giữ khóa đã bị thu hồi; tải khóa lại ở mọi yêu cầu lại tạo thêm phụ thuộc (dependency / 의존성) và độ trễ.

> **Chuyển mạch:** Trong **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**, **Refresh đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **Xác minh đơn vị từ (token / 토큰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bearer đơn vị từ (token / 토큰) và bằng chứng sở hữu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Refresh đơn vị từ (token / 토큰)

Truy cập (access / 접근) đơn vị từ (token / 토큰) sống ngắn làm giảm khoảng thời gian đơn vị từ (token / 토큰) bị lộ có thể bị lạm dụng, nhưng cần cơ chế làm mới. **Refresh đơn vị từ (token / 토큰)** thường có quyền mạnh hơn và sống lâu hơn, nên việc xoay đơn vị từ (token / 토큰), thu hồi và lưu trữ an toàn đặc biệt quan trọng.

Cơ chế phát hiện tái sử dụng refresh đơn vị từ (token / 토큰) có thể giúp nhận ra một “họ đơn vị từ (token / 토큰)” đã bị đánh cắp trong mô hình rotation.

> **Chuyển mạch:** Ở chặng này của **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**, **Refresh đơn vị từ (token / 토큰)** nêu điều cần giải thích; **Bearer đơn vị từ (token / 토큰) và bằng chứng sở hữu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Rủi ro trong liên kết danh tính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bearer đơn vị từ (token / 토큰) và bằng chứng sở hữu

**Bearer đơn vị từ (token / 토큰)** trao quyền cho bất kỳ ai đang giữ đơn vị từ (token / 토큰). Nếu đơn vị từ (token / 토큰) rò qua log, vùng lưu trữ trình duyệt hoặc proxy, kẻ tấn công có thể phát lại đơn vị từ (token / 토큰) trong thời hạn còn hiệu lực.

Đơn vị từ (token / 토큰) ràng buộc mTLS hoặc cơ chế kiểu DPoP cố gắn đơn vị từ (token / 토큰) với một khóa và bằng chứng từ máy khách (client / 클라이언트), giảm khả năng phát lại nhưng làm giao thức và vận hành phức tạp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**, **Bearer đơn vị từ (token / 토큰) và bằng chứng sở hữu** nêu điều cần giải thích; **Rủi ro trong liên kết danh tính** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phạm vi (scope / 범위) không thay thế mô hình phân quyền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rủi ro trong liên kết danh tính

Open redirect, mix-up attack, CSRF trong luồng redirect, dùng sai `nonce`/`state` và bài toán confused deputy xuất hiện vì nhiều bên trao đổi qua trình duyệt, kênh phía trước và kênh phía sau.

`state` giúp ràng buộc phản hồi ủy quyền với giao dịch mà máy khách (client / 클라이언트) đã bắt đầu; `nonce` của OIDC giúp ràng buộc ID đơn vị từ (token / 토큰) với yêu cầu xác thực. Hai trường này bảo vệ các mối đe dọa khác nhau.

> **Chuyển mạch:** Trong **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**, **Phạm vi (scope / 범위) không thay thế mô hình phân quyền** tiếp nhận điểm tựa từ **Rủi ro trong liên kết danh tính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phạm vi (scope / 범위) không thay thế mô hình phân quyền

Phạm vi (scope / 범위) thường chỉ mô tả quyền ở mức khá thô. API vẫn cần phân quyền ở cấp đối tượng: người dùng có `read:account` không có nghĩa họ được đọc tài khoản của người khác.

Xác thực trả lời “đây là ai”; phân quyền trả lời “thực thể này được làm gì với tài nguyên nào trong ngữ cảnh nào”.

> **Chuyển mạch:** Ở chặng này của **OAuth, OIDC, vòng đời đơn vị từ (token / 토큰) và rủi ro liên kết danh tính**, **Mô hình tư duy** gom các mảnh từ **Phạm vi (scope / 범위) không thay thế mô hình phân quyền** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> OAuth/OIDC là giao thức liên kết nhiều ranh giới tin cậy. đơn vị từ (token / 토큰) chỉ an toàn khi bên phát hành, đối tượng nhận, thời hạn, cơ chế ràng buộc và luồng chuyển hướng đều đúng. Đừng suy luận từ hình dạng JWT; hãy suy luận từ quyền lực được trao và những nơi đơn vị từ (token / 토큰) có thể bị phát lại.

> **Bàn giao:** Giữ lại client binding, redirect/PKCE, issuer/audience/nonce validation, refresh rotation và object-level authorization trước khi tin một token. Sang [PKI/mTLS](./02_pki_certificate_validation_mtls_and_service_identity.md) khi identity cần bind vào channel/service, hoặc [Browser isolation](./05_browser_isolation_csp_samesite_and_cross_origin_trust.md) khi token đi qua ambient browser credentials; quay về [README](./README.md) để xác nhận owner.
