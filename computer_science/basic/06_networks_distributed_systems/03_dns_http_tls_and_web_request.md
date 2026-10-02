# DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **DNS, HTTP, TLS và một web request end-to-end**. Route đi từ URL/DNS → transport connection → TLS identity/keys → HTTP semantics → cache/proxy/load balancer, để một request được truy nguyên từ tên miền tới response.

Gõ một URL trông như một thao tác đơn giản, nhưng trình duyệt (browser / 브라우저) phải phân giải tên miền, tìm đường mạng, thiết lập kết nối truyền tải và ngữ cảnh bảo mật, trao đổi HTTP, nhận dữ liệu rồi phân tích và hiển thị nội dung. Chương này dùng một yêu cầu web để nối nhiều tầng của hệ thống mạng.

## Cấu trúc của URL

`https://example.com:443/path?q=1` chứa lược đồ (scheme) `https`, máy chủ `example.com`, cổng tùy chọn, đường dẫn và chuỗi truy vấn. Scheme cho biết giao thức được kỳ vọng; tên miền không phải chính địa chỉ IP.

> **Chuyển mạch:** Trong **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **DNS** tiếp nhận điểm tựa từ **Cấu trúc của URL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thiết lập kết nối truyền tải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DNS

**Hệ thống tên miền (Domain Name System — DNS / 도메인 이름 시스템)** là hệ thống đặt tên phân cấp và phân tán. Bộ phân giải (resolver) tìm các bản ghi như A, AAAA, CNAME, MX hoặc TXT thông qua bộ nhớ đệm (cache / 캐시) và hạ tầng máy chủ đệ quy/chính thức.

DNS dùng thời gian sống **TTL (Time To Live)** để lưu kết quả tạm thời, giảm độ trễ và tải. Vì có bộ nhớ đệm (cache / 캐시), thay đổi bản ghi không xuất hiện đồng thời trên toàn Internet. Kết quả “không tồn tại” cũng có thể được lưu tạm theo quy tắc riêng.

DNS có thể chạy trên UDP hoặc TCP; các biến thể mã hóa như DoH và DoT bảo vệ truy vấn trên đường truyền. Đường đi thực tế phụ thuộc vào thiết bị và mạng đang sử dụng.

Phân phối nhiều địa chỉ bằng DNS không tự động tương đương với cân bằng tải có kiểm tra sức khỏe mạnh, vì hành vi bộ nhớ đệm (cache / 캐시) và resolver vẫn ảnh hưởng kết quả.

> **Chuyển mạch:** Ở chặng này của **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Thiết lập kết nối truyền tải** tiếp nhận điểm tựa từ **DNS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mục tiêu của TLS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thiết lập kết nối truyền tải

Sau khi có địa chỉ đích và đường định tuyến, máy khách mở kết nối truyền tải. Với HTTPS truyền thống trên TCP, bắt tay TCP tạo kết nối, sau đó bắt tay TLS xác thực máy chủ và thương lượng khóa. Với HTTP/3, QUIC tích hợp nhiều chức năng truyền tải và bảo mật trên UDP.

Tái sử dụng kết nối giúp giảm chi phí phải bắt tay lại nhiều lần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Mục tiêu của TLS** tiếp nhận điểm tựa từ **Thiết lập kết nối truyền tải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ nghĩa HTTP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mục tiêu của TLS

**tầng vận chuyển (transport layer / 전송 계층) bảo mật (security / 보안) (TLS)** cung cấp tính bí mật, tính toàn vẹn và xác thực đối tác; trường hợp phổ biến là xác thực máy chủ bằng chứng chỉ trong hạ tầng khóa công khai (PKI), còn chứng chỉ phía máy khách là tùy chọn.

TLS không bảo đảm ứng dụng là đáng tin hoặc lô-gic (logic / 논리) phân quyền là đúng. Nó bảo vệ các thuộc tính của kênh truyền dưới những giả định nhất định.

### Mật mã đối xứng và khóa công khai

Cơ chế khóa công khai được dùng để xác thực và thiết lập bí mật chung; dữ liệu khối lượng lớn sau đó được bảo vệ bằng khóa đối xứng hiệu quả hơn, thường qua cơ chế AEAD. Các cấu hình TLS hiện đại thường dùng trao đổi khóa tạm thời để có **bí mật chuyển tiếp (forward secrecy)**.

Xem [nền tảng mật mã học](../07_security_reliability/01_cryptography_foundations.md).

> **Chuyển mạch:** Trong **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Ngữ nghĩa HTTP** tiếp nhận điểm tựa từ **Mục tiêu của TLS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ đệm HTTP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ nghĩa HTTP

Một yêu cầu HTTP có phương thức, đích, header và phần thân tùy chọn. Phản hồi có mã trạng thái, header và phần thân. Các phương thức mang những quy ước như an toàn hoặc bất biến khi lặp lại (idempotent), nhưng việc triển khai phía máy chủ vẫn có thể vi phạm quy ước đó.

HTTP/1.1 dùng định dạng văn bản và kết nối duy trì; HTTP/2 ghép nhiều luồng nhị phân trên một kết nối; HTTP/3 ánh xạ ngữ nghĩa HTTP lên các luồng QUIC. Ngữ nghĩa ứng dụng vẫn tương đối ổn định dù cơ chế đóng khung và truyền tải thay đổi.

> **Chuyển mạch:** Ở chặng này của **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Bộ nhớ đệm HTTP** tiếp nhận điểm tựa từ **Ngữ nghĩa HTTP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cookie và phiên làm việc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ đệm HTTP

Trình duyệt, CDN, proxy và máy chủ gốc đều có thể lưu phản hồi theo `Cache-Control`, các bộ xác thực như `ETag`/`Last-Modified` và ngữ nghĩa của yêu cầu. bộ nhớ đệm (cache / 캐시) có thể biến một lần gọi mạng thành phản hồi cục bộ hoặc từ nút biên, nhưng tạo thêm bài toán về độ mới và vô hiệu hóa dữ liệu cũ.

`Cache-Control: max-age` xác định khoảng thời gian phản hồi còn được xem là mới. Khi cần kiểm tra lại, máy khách có thể gửi yêu cầu có điều kiện và nhận `304 Not Modified`. Nội dung nhạy cảm hoặc riêng theo người dùng cần sử dụng cẩn thận các chỉ thị như `private`, `no-store` và `Vary`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Cookie và phiên làm việc** tiếp nhận điểm tựa từ **Bộ nhớ đệm HTTP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Proxy, CDN và bộ cân bằng tải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cookie và phiên làm việc

HTTP hoạt động theo mô hình yêu cầu/phản hồi; trạng thái phiên của ứng dụng có thể được duy trì bằng cookie hoặc đơn vị từ (token / 토큰). Các thuộc tính `Secure`, `HttpOnly` và `SameSite` ảnh hưởng cách cookie được gửi qua mạng, truy cập từ script và sử dụng giữa các site.

Cookie tự nó không phải cơ chế xác thực. Nó là phương tiện lưu và truyền dữ liệu, thường chứa mã định danh phiên.

> **Chuyển mạch:** Trong **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Proxy, CDN và bộ cân bằng tải** tiếp nhận điểm tựa từ **Cookie và phiên làm việc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một yêu cầu từ đầu đến cuối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proxy, CDN và bộ cân bằng tải

TLS có thể kết thúc tại CDN hoặc bộ cân bằng tải, sau đó yêu cầu được chuyển tới backend qua một kết nối khác. Vì vậy đối tác mà máy khách trực tiếp nhìn thấy có thể là nút biên chứ không phải máy chủ ứng dụng cuối cùng.

Các header như `Forwarded` hoặc `X-Forwarded-*` truyền ngữ cảnh ban đầu theo quy ước và chỉ nên được tin cậy khi chúng đến từ proxy nằm trong vùng kiểm soát.

> **Chuyển mạch:** Ở chặng này của **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Một yêu cầu từ đầu đến cuối** tiếp nhận điểm tựa từ **Proxy, CDN và bộ cân bằng tải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một yêu cầu từ đầu đến cuối

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Mô hình tư duy** gom các mảnh từ **Một yêu cầu từ đầu đến cuối** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> Một yêu cầu web không đơn giản là “HTTP đi tới máy chủ”. Nó là một **chuỗi máy trạng thái (state machine / 상태 머신) và ranh giới tin cậy**, kèm theo bộ nhớ đệm (cache / 캐시) và proxy có thể kết thúc một kết nối rồi tạo kết nối mới.

> **Chuyển mạch:** Trong **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“HTTPS nghĩa là website an toàn.”** Không đúng. TLS bảo vệ kênh truyền và danh tính theo PKI; ứng dụng vẫn có thể độc hại hoặc có lỗ hổng.

**“DNS ánh xạ một tên miền tới đúng một máy chủ.”** Không đúng. Nhiều bản ghi, CDN, anycast, bộ cân bằng tải và bộ nhớ đệm (cache / 캐시) làm ánh xạ trở nên động và có thể nhiều–nhiều.

**“HTTP không lưu trạng thái nên ứng dụng không thể có phiên.”** Không đúng. Trạng thái phiên được xây thêm bằng cookie, đơn vị từ (token / 토큰) và vùng lưu trữ phía máy chủ.

> **Chuyển mạch:** Ở chặng này của **DNS, HTTP, TLS và hành trình đầy đủ của một yêu cầu web**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Kết nối** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Luồng đầy đủ được mở rộng thêm trong [Trình duyệt → Cơ sở dữ liệu](../90_connections/01_browser_to_database_request.md). Chi tiết bảo mật nằm ở [danh tính và xác thực](../07_security_reliability/02_identity_authentication_and_authorization.md), còn truy cập dữ liệu được nối với [thực thi truy vấn](../05_data_databases/03_indexes_and_query_execution.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
