# Internet — một trang web đến màn hình của bạn như thế nào?

Khi gõ một URL rồi nhấn Enter, cảm giác giống như trình duyệt “đi thẳng” tới website. Thực tế, trình duyệt phải tìm địa chỉ, thiết lập kết nối, gửi gói tin qua nhiều mạng độc lập, tới máy chủ hoặc mạng phân phối nội dung, rồi nhận dữ liệu quay lại. Chapter này dùng luồng đó để nối kiến thức mạng máy tính với hạ tầng Internet thật ở Hàn Quốc và Việt Nam.

## 1. Luồng end-to-end

```text
Browser / App
    ↓
Wi‑Fi AP hoặc 4G/5G base station
    ↓
Access network của ISP
    ↓
ISP backbone
    ↓
Peering / Internet Exchange hoặc IP transit
    ↓
CDN / data center / cloud network
    ↓
Web server / application
    ↓
Response quay lại người dùng
```

Trước khi gửi HTTP request, thiết bị thường cần phân giải tên miền bằng hệ thống tên miền (Domain Name System, DNS / 도메인 네임 시스템). `example.com` phải được ánh xạ thành địa chỉ IP. Sau đó TCP hoặc QUIC tạo trạng thái truyền dữ liệu; với HTTPS, TLS xác thực server và thiết lập khóa mã hóa. Những bước này thuộc logic giao thức, còn Internet thật sự là bài toán **định tuyến liên miền (inter-domain routing / 도메인 간 라우팅)** giữa hàng nghìn mạng tự trị.

Mỗi nhà mạng lớn vận hành một hệ tự trị (Autonomous System, AS / 자율 시스템) với ASN riêng. Bên trong mạng, router chọn đường theo giao thức nội bộ; giữa các AS, Border Gateway Protocol (BGP / 경계 경로 프로토콜) trao đổi thông tin “prefix nào có thể đi qua mạng nào”. Vì vậy Internet không có một “router trung tâm”. Nó hoạt động nhờ nhiều mạng đồng ý trao đổi lưu lượng qua peering hoặc mua IP transit.

## 2. Internet Exchange làm gì?

Nếu ISP A và ISP B đều ở cùng quốc gia nhưng phải gửi lưu lượng qua một nhà cung cấp quốc tế rồi vòng trở lại, đường truyền dài hơn, đắt hơn và phụ thuộc hơn. Điểm trao đổi Internet (Internet Exchange Point, IXP / 인터넷 교환 지점) cho phép các mạng gặp nhau tại hạ tầng chung để peering trực tiếp.

Việt Nam có Vietnam National Internet eXchange (VNIX), do VNNIC vận hành. VNNIC mô tả VNIX là hạ tầng trao đổi lưu lượng trong nước giữa ISP, có điểm kết nối ở nhiều vùng và giúp lưu lượng nội địa không phải đi vòng qua quốc tế. Đây là ví dụ rất rõ cho việc một IXP giảm độ trễ và chi phí transit.

Hàn Quốc có thị trường kết nối nội địa trưởng thành hơn với nhiều backbone, data center và peering thương mại. Cơ chế vẫn giống nhau: nội dung càng được cache gần người dùng và các mạng càng peering trực tiếp, số hop và phụ thuộc vào tuyến quốc tế càng giảm.

## 3. CDN thay đổi đường đi như thế nào?

Mạng phân phối nội dung (Content Delivery Network, CDN / 콘텐츠 전송 네트워크) đặt bản sao nội dung ở nhiều điểm. Khi người dùng ở Seoul xem một video, request có thể được đưa tới edge server ở Hàn Quốc thay vì origin server ở Mỹ. Tương tự, người dùng ở Hà Nội hoặc TP.HCM có thể nhận nội dung từ cache trong nước hoặc khu vực.

Điểm quan trọng là “website ở đâu” không còn là một câu hỏi một địa điểm. DNS, anycast, CDN và cloud routing có thể khiến cùng một tên miền được phục vụ từ nhiều thành phố khác nhau.

## 4. Hàn Quốc và Việt Nam khác nhau ở đâu?

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Last mile | Mật độ fiber và hạ tầng đô thị rất cao; fixed broadband và mobile broadband cùng mạnh | Fiber đô thị phát triển nhanh, mobile broadband có vai trò lớn ở nhiều khu vực |
| Nội địa hóa traffic | Nhiều data center, CDN và mạng peering trong nước | VNIX là hạ tầng quốc gia quan trọng để giữ traffic nội địa trong nước |
| Quốc tế | Nhiều tuyến quốc tế và hệ sinh thái data center dày | Cáp quang biển có vai trò đặc biệt rõ; sự cố nhiều tuyến cùng lúc có thể ảnh hưởng trải nghiệm quốc tế |
| Điều phối tài nguyên Internet | KRNIC/KISA và hệ sinh thái viễn thông quản lý tài nguyên, an toàn mạng theo phạm vi tương ứng | VNNIC quản lý `.vn`, IP/ASN, DNS quốc gia và VNIX |

Đừng hiểu bảng trên thành “Internet Hàn Quốc là một mạng” và “Internet Việt Nam là một mạng”. Cả hai đều là tập hợp nhiều AS. Khác biệt chủ yếu nằm ở mật độ hạ tầng, mức độ nội địa hóa nội dung, topology và năng lực dự phòng.

## 5. Khi Internet chậm, lỗi có thể nằm ở đâu?

Một speed test nhanh không chứng minh mọi website sẽ nhanh. Có ít nhất sáu lớp có thể trở thành bottleneck: Wi‑Fi trong nhà; last mile của ISP; congestion trong backbone; peering/transit; tuyến quốc tế; hoặc server/CDN của dịch vụ. DNS chậm, packet loss hoặc routing bất thường cũng tạo cảm giác “mạng yếu” dù băng thông lý thuyết cao.

Mental model quan trọng là:

```text
Trải nghiệm ≠ chỉ băng thông access
Trải nghiệm = access + routing + peering + latency + loss + server capacity
```

Từ đây có thể đi sâu sang [`../../computer_science/`](../../computer_science/README.md) cho TCP/IP và network protocols, hoặc sang [cloud computing](../cloud-computing/README.md) để hiểu phía server mà request vừa đi tới.

## Nguồn chính thức tham chiếu

- VNNIC — vai trò quản lý tài nguyên Internet, DNS quốc gia và VNIX: https://vnnic.vn/en/about-vnnic
- VNNIC — VNIX: https://www.vnnic.vn/en/vnix/introduction
