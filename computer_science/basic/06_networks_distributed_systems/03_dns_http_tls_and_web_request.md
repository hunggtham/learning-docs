# DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web

Gõ một URL trông như một thao tác đơn giản, nhưng trình duyệt (browser) phải phân giải tên miền, tìm đường mạng, thiết lập kết nối truyền tải và ngữ cảnh bảo mật, trao đổi HTTP, nhận dữ liệu rồi phân tích và hiển thị nội dung. Chương này dùng một yêu cầu web để nối nhiều tầng của hệ thống mạng.

## Cấu trúc của URL

`https://example.com:443/path?q=1` chứa lược đồ (scheme) `https`, máy chủ `example.com`, cổng tùy chọn, đường dẫn và chuỗi truy vấn. Scheme cho biết giao thức được kỳ vọng; tên miền không phải chính địa chỉ IP.

## DNS

**Hệ thống tên miền (Domain Name System — DNS / 도메인 이름 시스템)** là hệ thống đặt tên phân cấp và phân tán. Bộ phân giải (resolver) tìm các bản ghi như A, AAAA, CNAME, MX hoặc TXT thông qua cache và hạ tầng máy chủ đệ quy/chính thức.

DNS dùng thời gian sống **TTL (Time To Live)** để lưu kết quả tạm thời, giảm độ trễ và tải. Vì có cache, thay đổi bản ghi không xuất hiện đồng thời trên toàn Internet. Kết quả “không tồn tại” cũng có thể được lưu tạm theo quy tắc riêng.

DNS có thể chạy trên UDP hoặc TCP; các biến thể mã hóa như DoH và DoT bảo vệ truy vấn trên đường truyền. Đường đi thực tế phụ thuộc vào thiết bị và mạng đang sử dụng.

Phân phối nhiều địa chỉ bằng DNS không tự động tương đương với cân bằng tải có kiểm tra sức khỏe mạnh, vì hành vi cache và resolver vẫn ảnh hưởng kết quả.

## Thiết lập kết nối truyền tải

Sau khi có địa chỉ đích và đường định tuyến, máy khách mở kết nối truyền tải. Với HTTPS truyền thống trên TCP, bắt tay TCP tạo kết nối, sau đó bắt tay TLS xác thực máy chủ và thương lượng khóa. Với HTTP/3, QUIC tích hợp nhiều chức năng truyền tải và bảo mật trên UDP.

Tái sử dụng kết nối giúp giảm chi phí phải bắt tay lại nhiều lần.

## Mục tiêu của TLS

**Transport Layer Security (TLS)** cung cấp tính bí mật, tính toàn vẹn và xác thực đối tác; trường hợp phổ biến là xác thực máy chủ bằng chứng chỉ trong hạ tầng khóa công khai (PKI), còn chứng chỉ phía máy khách là tùy chọn.

TLS không bảo đảm ứng dụng là đáng tin hoặc logic phân quyền là đúng. Nó bảo vệ các thuộc tính của kênh truyền dưới những giả định nhất định.

### Mật mã đối xứng và khóa công khai

Cơ chế khóa công khai được dùng để xác thực và thiết lập bí mật chung; dữ liệu khối lượng lớn sau đó được bảo vệ bằng khóa đối xứng hiệu quả hơn, thường qua cơ chế AEAD. Các cấu hình TLS hiện đại thường dùng trao đổi khóa tạm thời để có **bí mật chuyển tiếp (forward secrecy)**.

Xem [nền tảng mật mã học](../07_security_reliability/01_cryptography_foundations.md).

## Ngữ nghĩa HTTP

Một yêu cầu HTTP có phương thức, đích, header và phần thân tùy chọn. Phản hồi có mã trạng thái, header và phần thân. Các phương thức mang những quy ước như an toàn hoặc bất biến khi lặp lại (idempotent), nhưng việc triển khai phía máy chủ vẫn có thể vi phạm quy ước đó.

HTTP/1.1 dùng định dạng văn bản và kết nối duy trì; HTTP/2 ghép nhiều luồng nhị phân trên một kết nối; HTTP/3 ánh xạ ngữ nghĩa HTTP lên các luồng QUIC. Ngữ nghĩa ứng dụng vẫn tương đối ổn định dù cơ chế đóng khung và truyền tải thay đổi.

## Bộ nhớ đệm HTTP

Trình duyệt, CDN, proxy và máy chủ gốc đều có thể lưu phản hồi theo `Cache-Control`, các bộ xác thực như `ETag`/`Last-Modified` và ngữ nghĩa của yêu cầu. Cache có thể biến một lần gọi mạng thành phản hồi cục bộ hoặc từ nút biên, nhưng tạo thêm bài toán về độ mới và vô hiệu hóa dữ liệu cũ.

`Cache-Control: max-age` xác định khoảng thời gian phản hồi còn được xem là mới. Khi cần kiểm tra lại, máy khách có thể gửi yêu cầu có điều kiện và nhận `304 Not Modified`. Nội dung nhạy cảm hoặc riêng theo người dùng cần sử dụng cẩn thận các chỉ thị như `private`, `no-store` và `Vary`.

## Cookie và phiên làm việc

HTTP hoạt động theo mô hình yêu cầu/phản hồi; trạng thái phiên của ứng dụng có thể được duy trì bằng cookie hoặc token. Các thuộc tính `Secure`, `HttpOnly` và `SameSite` ảnh hưởng cách cookie được gửi qua mạng, truy cập từ script và sử dụng giữa các site.

Cookie tự nó không phải cơ chế xác thực. Nó là phương tiện lưu và truyền dữ liệu, thường chứa mã định danh phiên.

## Proxy, CDN và bộ cân bằng tải

TLS có thể kết thúc tại CDN hoặc bộ cân bằng tải, sau đó yêu cầu được chuyển tới backend qua một kết nối khác. Vì vậy đối tác mà máy khách trực tiếp nhìn thấy có thể là nút biên chứ không phải máy chủ ứng dụng cuối cùng.

Các header như `Forwarded` hoặc `X-Forwarded-*` truyền ngữ cảnh ban đầu theo quy ước và chỉ nên được tin cậy khi chúng đến từ proxy nằm trong vùng kiểm soát.

## Một yêu cầu từ đầu đến cuối

```text
URL
 ↓
phân giải tên bằng DNS
 ↓
định tuyến IP / ARP-ND / khung liên kết
 ↓
kết nối TCP hoặc QUIC
 ↓
xác thực TLS + thiết lập khóa
 ↓
yêu cầu HTTP
 ↓
reverse proxy / ứng dụng / cơ sở dữ liệu / cache
 ↓
phản hồi HTTP
 ↓
TLS / truyền tải / IP / liên kết theo chiều ngược lại
 ↓
trình duyệt phân tích / hiển thị / thực thi
```

Mỗi mũi tên là một ranh giới có kiểu lỗi, độ trễ và đặc tính bảo mật riêng.

## Mô hình tư duy

> Một yêu cầu web không đơn giản là “HTTP đi tới máy chủ”. Nó là một **chuỗi máy trạng thái (state machine) và ranh giới tin cậy**, kèm theo cache và proxy có thể kết thúc một kết nối rồi tạo kết nối mới.

## Những hiểu nhầm thường gặp

**“HTTPS nghĩa là website an toàn.”** Không đúng. TLS bảo vệ kênh truyền và danh tính theo PKI; ứng dụng vẫn có thể độc hại hoặc có lỗ hổng.

**“DNS ánh xạ một tên miền tới đúng một máy chủ.”** Không đúng. Nhiều bản ghi, CDN, anycast, bộ cân bằng tải và cache làm ánh xạ trở nên động và có thể nhiều–nhiều.

**“HTTP không lưu trạng thái nên ứng dụng không thể có phiên.”** Không đúng. Trạng thái phiên được xây thêm bằng cookie, token và vùng lưu trữ phía máy chủ.

## Kết nối

Luồng đầy đủ được mở rộng thêm trong [Trình duyệt → Cơ sở dữ liệu](../90_connections/01_browser_to_database_request.md). Chi tiết bảo mật nằm ở [danh tính và xác thực](../07_security_reliability/02_identity_authentication_and_authorization.md), còn truy cập dữ liệu được nối với [thực thi truy vấn](../05_data_databases/03_indexes_and_query_execution.md).
