# PKI, certificate validation, mTLS và service identity

TLS thường được tóm tắt là “mã hóa connection”, nhưng trước khi encryption có ý nghĩa, client phải biết mình đang nói chuyện với đúng peer. **Public Key Infrastructure (PKI / 공개키 기반 구조)** giải quyết bài toán bind public key với identity thông qua certificate, trust anchor và validation rules.

## Certificate là một signed assertion

X.509 certificate chứa public key cùng identity/constraints và chữ ký của issuer. Chữ ký không nói “entity này tốt”; nó nói issuer chứng thực binding theo policy của issuer.

Trust vì thế là một chain: leaf certificate → intermediate CA → root CA mà client đã cấu hình làm trust anchor.

## Validation không chỉ kiểm tra chữ ký

Client cần kiểm tra chain signatures, validity period, hostname/service identity, key usage/extended key usage, constraints và các policy liên quan. Một certificate có chữ ký hợp lệ nhưng hostname không khớp vẫn không chứng minh đúng server mà user định kết nối.

Security bug thường xuất hiện khi application “bỏ qua certificate error để test” rồi behavior đó lọt vào production.

## Hostname verification là identity check

Trong HTTPS, client so hostname mục tiêu với Subject Alternative Name phù hợp. DNS đưa client tới IP; certificate validation chứng minh endpoint trình bày credential cho identity mong đợi. Hai cơ chế giải quyết hai câu hỏi khác nhau.

Nếu chỉ verify CA chain mà không verify hostname, một certificate hợp lệ cho domain khác có thể bị chấp nhận sai context.

## TLS server authentication và mTLS

TLS thông thường xác thực server với client; client có thể xác thực ở application layer bằng cookie/token. **Mutual TLS (mTLS / 상호 TLS)** yêu cầu client cũng trình certificate để server xác thực cryptographic identity của client.

mTLS phù hợp service-to-service environments vì identity có thể gắn với workload/service thay vì human password. Nhưng certificate issuance, rotation, revocation và policy distribution trở thành operational system cần quản lý.

## Identity khác authorization

Certificate chứng minh “peer là service A” không tự động nghĩa service A được đọc customer table. Authentication cung cấp principal; authorization quyết định principal được phép làm gì.

Một architecture tốt không encode mọi authorization vào certificate. Identity nên ổn định đủ để policy layer quyết định quyền theo context.

## Short-lived certificate và rotation

Certificate lifetime ngắn giảm cửa sổ lạm dụng credential bị lộ và giảm phụ thuộc revocation. Đổi lại hệ thống issuance/renewal phải rất đáng tin cậy. Nếu control plane cấp certificate ngừng hoạt động đủ lâu, workload mới hoặc certificate sắp hết hạn có thể mất khả năng giao tiếp.

Security mechanism vì thế cũng là reliability dependency.

## Revocation khó trong distributed environment

CRL/OCSP cho phép kiểm tra certificate bị revoke, nhưng availability, caching và privacy tạo trade-off. Nhiều internal PKI ưu tiên short-lived credentials để giảm nhu cầu revocation phức tạp.

Không có một policy duy nhất cho mọi hệ thống; threat model và operational capability quyết định.

## Service mesh không loại bỏ trust design

Service mesh có thể tự động cấp workload identity và thiết lập mTLS giữa proxies. Điều đó giảm boilerplate trong application nhưng không loại bỏ câu hỏi: CA nào được tin, namespace nào có thể impersonate service nào, policy được phân phối ra sao và control plane compromise có blast radius gì.

Automation di chuyển complexity chứ không làm complexity biến mất.

## Certificate pinning

Pinning có thể giảm trust surface bằng cách yêu cầu key/certificate cụ thể, nhưng rotation trở nên khó. Pin sai hoặc quên backup pin có thể gây outage. Mobile/app environments đôi khi dùng pinning khi threat model phù hợp; internal services thường cần cân nhắc operational recovery trước.

## Mental model

> PKI là hệ thống phân phối và kiểm chứng identity, không chỉ file certificate. TLS bảo vệ channel; certificate validation bind channel với peer identity; mTLS đưa identity tới cả hai phía; authorization vẫn là layer riêng. Thiết kế tốt phải đồng thời reasoning trust root, issuance, rotation, revocation và failure mode.