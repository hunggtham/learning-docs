# Mạng, DNS, socket và cổng

Khi một ứng dụng không kết nối được tới máy chủ khác, câu "mạng lỗi" quá rộng để có thể hành động chính xác. Mạng trên Linux có nhiều lớp: phân giải tên, chọn đường đi, giao diện mạng, khả năng tiếp cận IP, kết nối tầng vận chuyển, socket lắng nghe, TLS và giao thức ứng dụng. Xử lý sự cố hiệu quả là xác định **lớp đầu tiên mà trạng thái quan sát được khác với điều ta kỳ vọng**.

## Từ tên dịch vụ tới gói tin

Giả sử ứng dụng gọi:

```text
https://api.example.com:443/orders
```

Trước khi một yêu cầu HTTP tới được máy chủ đích, máy khách thường phải phân giải hostname thành địa chỉ IP, chọn tuyến và địa chỉ nguồn, thiết lập kết nối TCP, thực hiện bắt tay TLS rồi mới trao đổi HTTP. Thất bại ở mỗi giai đoạn tạo ra triệu chứng khác nhau.

## Giao diện mạng và địa chỉ IP

```bash
ip addr
```

hiển thị các **giao diện mạng (network interface)** và địa chỉ tương ứng. Một máy có thể có nhiều giao diện: NIC vật lý, loopback, bridge của container, VPN hoặc tunnel.

`127.0.0.1` thuộc loopback và chỉ dùng cho giao tiếp nội bộ trong cùng host. Nếu dịch vụ chỉ gắn vào `127.0.0.1:8080`, máy từ xa không thể kết nối qua giao diện bên ngoài dù `curl` chạy cục bộ vẫn thành công.

## Định tuyến

Địa chỉ IP đích không tự nói gói tin sẽ đi qua giao diện nào. **Bảng định tuyến (routing table)** của kernel quyết định chặng kế tiếp và đường đi từ địa chỉ nguồn:

```bash
ip route
ip route get 10.0.0.20
```

`ip route get` đặc biệt hữu ích vì cho thấy tuyến mà kernel thực sự sẽ chọn cho một địa chỉ đích cụ thể.

## DNS

Con người và ứng dụng thường dùng hostname, còn tầng mạng cần địa chỉ IP. **DNS (Domain Name System / 도메인 이름 시스템)** cung cấp cơ chế phân giải tên phân tán.

```bash
dig api.example.com
dig +short api.example.com
```

Nếu DNS trả về IP sai, bắt đầu gỡ lỗi ở tầng HTTP là đi sai lớp.

DNS còn có bộ nhớ đệm và TTL. Thay đổi bản ghi không có nghĩa mọi resolver hoặc máy khách đều thấy giá trị mới ngay lập tức.

## Cổng và socket

Cổng (port) không phải là tiến trình. Số cổng là một phần của điểm cuối ở tầng vận chuyển. Tiến trình máy chủ tạo **socket**, gắn địa chỉ/cổng bằng `bind` rồi bắt đầu `listen`.

```bash
sudo ss -lntp
```

Các tùy chọn: `-l` chỉ socket đang lắng nghe, `-n` giữ địa chỉ/cổng ở dạng số, `-t` chọn TCP, `-p` hiển thị thông tin tiến trình.

Kiểm tra cổng 8080:

```bash
sudo ss -lntp | grep ':8080'
```

Nếu tiến trình tồn tại nhưng không có socket lắng nghe, dịch vụ chưa sẵn sàng ở tầng mạng.

## Địa chỉ bind rất quan trọng

Các listener sau có phạm vi truy cập khác nhau:

```text
127.0.0.1:8080
0.0.0.0:8080
10.0.0.5:8080
[::]:8080
```

`0.0.0.0` thường biểu thị gắn vào mọi địa chỉ IPv4 cục bộ. `127.0.0.1` chỉ dành cho loopback. Với IPv6, cần xem thêm cấu hình socket và nền tảng cụ thể.

Vì vậy câu "cổng 8080 đang mở" vẫn thiếu chính xác nếu không nói rõ địa chỉ bind, giao thức và tiến trình lắng nghe.

## Các trạng thái kết nối TCP

```bash
sudo ss -antp | grep ':8080'
```

Một số trạng thái quan trọng:

- `LISTEN`: socket đang chờ kết nối vào;
- `ESTAB`: kết nối đã được thiết lập;
- `SYN-SENT`: phía máy khách đã gửi SYN và đang chờ phản hồi;
- `SYN-RECV`: phía máy chủ đang ở giữa quá trình bắt tay;
- `TIME-WAIT`: kết nối đã đóng nhưng TCP còn giữ trạng thái tạm thời;
- `CLOSE-WAIT`: phía bên kia đã đóng nhưng ứng dụng cục bộ chưa đóng socket.

Nhiều `CLOSE-WAIT` kéo dài có thể gợi ý vấn đề vòng đời tài nguyên trong ứng dụng. Ngược lại, nhiều `TIME-WAIT` không tự động là lỗi; TCP cần trạng thái này để xử lý các gói đến muộn và đảm bảo ngữ nghĩa của việc tái sử dụng kết nối.

## `Connection refused` khác timeout như thế nào?

`Connection refused` thường có nghĩa đường mạng tới host đủ để nhận phản hồi nhưng không có tiến trình lắng nghe ở điểm cuối, hoặc một thiết bị/chính sách chủ động từ chối. Timeout thường gợi ý gói tin hoặc phản hồi bị loại bỏ, tuyến/firewall có vấn đề hoặc phía đích không phản hồi.

Đây chỉ là **quy tắc kinh nghiệm (heuristic)** chứ không phải định luật. Tuy nhiên hai triệu chứng cung cấp loại bằng chứng khác nhau và không nên gộp chung thành "mạng lỗi".

## `nc` để kiểm tra tầng TCP

```bash
nc -vz 10.0.0.20 443
```

`-z` chỉ thử kết nối mà không gửi dữ liệu ứng dụng; `-v` hiển thị chi tiết hơn. Nếu TCP kết nối thành công nhưng `curl` vẫn thất bại, phạm vi điều tra chuyển lên TLS hoặc HTTP.

## `curl` để kiểm tra đường đi ở tầng ứng dụng

```bash
curl -fsS -v https://api.example.com/health
```

`-f` trả mã thoát khác 0 với lỗi HTTP, `-sS` ẩn thanh tiến trình nhưng vẫn hiện lỗi, còn `-v` hiển thị chi tiết kết nối, TLS và header.

`curl -k` bỏ qua xác minh chứng chỉ và chỉ nên dùng cho chẩn đoán tạm thời. Nó không phải cách sửa đúng cho vấn đề tin cậy TLS.

## Ưu tiên kiểm tra từ bên trong máy chủ

Với một ứng dụng máy chủ, hãy thử từ chính host trước:

```bash
curl -fsS -v http://127.0.0.1:8080/health
```

Nếu kiểm tra cục bộ thất bại, chưa cần bắt đầu ở bộ cân bằng tải hoặc firewall bên ngoài. Nếu cục bộ thành công nhưng từ xa thất bại, phạm vi điều tra chuyển sang địa chỉ bind, firewall, định tuyến, proxy/LB và chính sách mạng.

Đây là cách suy luận gần với tìm kiếm nhị phân: dùng một phép kiểm tra có khả năng loại bỏ nhiều lớp giả thuyết cùng lúc.

## Firewall

Máy Linux có thể dùng nftables, iptables, firewalld hoặc các chính sách ở tầng cloud/network. Việc `ss` cho thấy socket đang lắng nghe chỉ chứng minh trạng thái cục bộ; nó không chứng minh lưu lượng từ xa được phép đi tới.

Tùy bản phân phối có thể dùng:

```bash
sudo nft list ruleset
sudo firewall-cmd --list-all
```

Không nên thay luật firewall trên production khi chưa hiểu chính sách được quản lý ở đâu. Nhóm bảo mật cloud (security group) hoặc thiết bị mạng bên ngoài có thể là một lớp hoàn toàn khác với firewall trên host.

## Bắt gói tin

Khi các công cụ tầng cao không đủ, `tcpdump` cho phép quan sát gói tin:

```bash
sudo tcpdump -ni any port 8080
```

Nếu máy khách gửi SYN nhưng host máy chủ không nhìn thấy gói, vấn đề nằm trước host. Nếu host thấy SYN rồi trả RST, cần kiểm tra listener hoặc chính sách cục bộ. **Bắt gói (packet capture)** biến giả thuyết thành bằng chứng ở tầng mạng.

Có thể ghi ra tệp để phân tích bằng Wireshark:

```bash
sudo tcpdump -ni any port 8080 -w /tmp/8080.pcap
```

Tệp bắt gói có thể chứa dữ liệu hoặc metadata nhạy cảm, vì vậy cần quản lý cẩn thận.

## Mô hình tư duy (Mental Model)

Khi xử lý sự cố, có thể đi từ lớp thấp cần thiết lên lớp cao hơn:

```text
tên -> địa chỉ -> định tuyến -> gói tin có tới không -> socket TCP -> TLS -> HTTP / ứng dụng
```

Không phải lúc nào cũng cần kiểm tra mọi lớp. Thông báo lỗi và kiến trúc có thể giúp nhảy thẳng tới giả thuyết phù hợp, nhưng mô hình này giúp biết lớp nào vẫn chưa được chứng minh.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Ping thất bại nghĩa là server chết."** ICMP có thể bị chặn trong khi TCP vẫn hoạt động bình thường.

**"Port mở nghĩa là ứng dụng khỏe."** Socket có thể nhận kết nối nhưng endpoint nghiệp vụ vẫn thất bại.

**"Tiến trình chạy nghĩa là cổng đang lắng nghe."** Trạng thái tiến trình và trạng thái socket là hai quan sát khác nhau.

**"localhost thành công nghĩa là truy cập từ xa chắc chắn thành công."** Bind, firewall, routing và load balancer vẫn nằm ngoài đường đi cục bộ.

**"DNS chỉ đổi hostname thành một IP."** DNS còn có nhiều loại bản ghi, bộ nhớ đệm, phân phối tải và hành vi của resolver.

## Kết nối kiến thức

Socket mạng cũng được tiến trình quản lý thông qua file descriptor. [SSH và thao tác từ xa](./ssh_remote_operations.md) xây dựng giao thức bảo mật trên TCP; [Xử lý sự cố production](../09_production/production_troubleshooting.md) dùng mô hình nhiều lớp này để khoanh vùng sự cố.