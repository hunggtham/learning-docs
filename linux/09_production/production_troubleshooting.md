# Xử lý sự cố Linux trong môi trường production

Xử lý sự cố (troubleshooting) không phải khả năng nhớ thật nhiều câu lệnh. Bản chất của nó là quá trình thu hẹp không gian giả thuyết bằng bằng chứng. Kỹ sư nhiều kinh nghiệm thường xử lý nhanh hơn không phải vì gõ lệnh nhanh hơn, mà vì biết **câu hỏi tiếp theo nào có khả năng phân biệt hai nguyên nhân đang được nghi ngờ**.

## Triệu chứng không phải nguyên nhân gốc

"API timeout", "Java chết", "hệ thống tệp đầy" hoặc "CPU cao" đều chỉ là triệu chứng. Timeout có thể đến từ DNS, kết nối TCP, thread pool, khóa cơ sở dữ liệu hoặc dịch vụ phía sau. Tiến trình Java biến mất có thể do ứng dụng crash, systemd dừng dịch vụ, OOM killer hoặc một người vận hành gửi signal.

Mục tiêu đầu tiên là mô tả triệu chứng đủ cụ thể:

```text
Ai hoặc hệ thống nào quan sát thấy lỗi?
Lỗi được quan sát từ đâu?
Bắt đầu từ thời điểm nào?
Ảnh hưởng tất cả yêu cầu hay chỉ một phần?
Có triển khai hoặc thay đổi cấu hình nào gần thời điểm đó không?
```

## Quan sát trước khi thay đổi trạng thái

Khởi động lại có thể là hành động phục hồi đúng khi SLA quan trọng, nhưng nó cũng xóa một phần bằng chứng khi đang chạy. Nếu có đủ thời gian an toàn, nên chụp lại trạng thái trước:

```bash
date '+%F %T %Z'
hostname
systemctl status app --no-pager
journalctl -u app -n 300 --no-pager
pgrep -af 'java.*app'
sudo ss -lntp
free -h
df -h
uptime
```

Với Java bị treo hoặc dùng CPU cao, nếu chính sách cho phép nên lấy thread dump trước khi restart:

```bash
jcmd <PID> Thread.print > /tmp/thread-$(date +%s).txt
```

## Chẩn đoán theo từng lớp

Một dịch vụ web có thể được kiểm tra theo chuỗi phụ thuộc:

```text
trạng thái systemd
 -> tiến trình
 -> socket đang lắng nghe
 -> health endpoint cục bộ
 -> phụ thuộc cục bộ
 -> mạng của host
 -> proxy / load balancer
 -> đường đi từ máy khách
```

Nếu `curl localhost` thất bại, chưa cần bắt đầu ở firewall bên ngoài. Nếu kiểm tra cục bộ thành công nhưng truy cập từ xa thất bại, đường xử lý lõi trong ứng dụng ít có khả năng là lớp đầu tiên bị lỗi.

Cách tiếp cận này gần với tìm kiếm nhị phân: ưu tiên quan sát có **lượng thông tin thu được cao (information gain)** để loại bỏ nhiều giả thuyết cùng lúc.

## Dịch vụ không khởi động được

Bắt đầu bằng:

```bash
systemctl status app --no-pager
journalctl -xeu app
systemctl cat app
```

Từ lỗi cụ thể mới kiểm tra tệp thực thi, thư mục làm việc, danh tính, biến môi trường và quyền truy cập.

```bash
systemctl show app -p User -p Group -p WorkingDirectory -p ExecStart
namei -l /opt/app/app.jar
```

Không nên sửa `chmod` trước khi biết chính xác thao tác nào đang bị từ chối.

## Tiến trình tồn tại nhưng API không hoạt động

```bash
pgrep -af 'java.*app'
sudo ss -lntp | grep ':8080'
curl -fsS -v http://127.0.0.1:8080/health
```

Nếu không có listener, hãy kiểm tra nhật ký khởi động, cấu hình và địa chỉ bind. Nếu listener tồn tại nhưng `curl` bị treo, các giả thuyết có thể là cạn thread pool, deadlock, phụ thuộc bên ngoài hoặc trạng thái ứng dụng. Nếu `curl` cục bộ thành công, chuyển sang định tuyến, firewall, load balancer và DNS.

## CPU cao

```bash
uptime
nproc
top
pidstat -p <PID> 1
pidstat -t -p <PID> 1
```

Với Java, cần đối chiếu luồng dùng CPU cao với thread dump. Lấy nhiều mẫu cách nhau vài giây giúp phân biệt công việc tăng tải tạm thời với vòng lặp hoặc đường mã luôn nóng.

Không nên tăng CPU ngay nếu CPU cao chỉ là hệ quả của một cơn bão retry do dịch vụ phụ thuộc đang lỗi.

## Bộ nhớ tăng hoặc tiến trình bị kết thúc

```bash
free -h
ps -p <PID> -o pid,%mem,rss,vsz,etime,cmd
journalctl -k | grep -i -E 'oom|out of memory|killed process'
```

Nếu ứng dụng chạy trong container, cần kiểm tra giới hạn bộ nhớ của cgroup/container. Việc host còn nhiều RAM không đủ để loại trừ OOM trong cgroup.

Rò rỉ bộ nhớ cần xu hướng theo thời gian và bằng chứng ở runtime; một ảnh chụp RSS không thể chỉ ra đối tượng Java nào đang bị giữ lại.

## Hệ thống tệp hết dung lượng

```bash
df -h
df -i
sudo du -xhd1 /var 2>/dev/null | sort -hr
sudo lsof +L1
```

Chuỗi này giúp phân biệt hết byte lưu trữ, hết inode, tệp còn nhìn thấy trong cây thư mục và tệp đã xóa nhưng vẫn đang mở.

Nếu nhật ký quá lớn, hãy tìm nguyên nhân tăng trưởng trước khi chỉ xóa tệp. Một vòng lặp retry có thể tạo bão log, và việc đầy đĩa khi đó chỉ là triệu chứng phía sau.

## Lỗi mạng

Phía máy khách:

```bash
dig +short service.example.com
ip route get <IP>
nc -vz <IP> <PORT>
curl -fsS -v https://service.example.com/health
```

Phía máy chủ:

```bash
sudo ss -lntp | grep ':PORT'
sudo tcpdump -ni any port PORT
```

Nếu gói tin không tới host, khởi động lại ứng dụng không sửa được đường truyền mạng.

## Đối chiếu theo dòng thời gian

Một trong những câu hỏi có giá trị nhất là: **điều gì đã thay đổi ngay trước khi triệu chứng xuất hiện?**

Kiểm tra artifact triển khai, `mtime` của cấu hình, lịch sử gói, thời điểm dịch vụ khởi động lại và nhật ký:

```bash
systemctl show app -p ActiveEnterTimestamp
find /opt/app -type f -newermt '2026-09-20 15:30' -ls
```

Tương quan không tự động chứng minh quan hệ nhân quả, nhưng một thay đổi xảy ra sát thời điểm lỗi là giả thuyết mạnh để kiểm tra tiếp.

## Chẩn đoán so sánh

Nếu có hai máy chủ A và B có cấu hình tương tự nhưng chỉ A bị lỗi, hãy so sánh các chiều quan trọng:

```text
hash của artifact
khác biệt cấu hình
biến môi trường
kernel / bản phân phối
áp lực tài nguyên
định tuyến / DNS
phiên bản gói
mount / quyền truy cập
```

```bash
sha256sum app.jar
diff -u config-A config-B
```

So với một máy khỏe mạnh thường giúp thu hẹp không gian tìm kiếm nhanh hơn việc đọc hàng nghìn dòng log mà không có giả thuyết.

## Phục hồi khác với tìm nguyên nhân gốc

**Phục hồi (recovery)** đưa dịch vụ trở về trạng thái có thể chấp nhận. **Phân tích nguyên nhân gốc (root-cause analysis)** giải thích chuỗi nguyên nhân và cách ngăn lặp lại. Có thể restart để phục hồi trước rồi điều tra dựa trên bằng chứng đã chụp lại. Không nên nhầm "restart xong hết lỗi" với một lời giải thích nguyên nhân.

Một phân tích sau sự cố tốt nên hỏi: yếu tố kích hoạt là gì? điều kiện tiềm ẩn nào cho phép lỗi lan rộng? hệ thống phát hiện và phục hồi ra sao? thay đổi nào làm giảm khả năng tái diễn?

## Chọn công cụ theo câu hỏi

| Câu hỏi | Công cụ quan sát phù hợp |
|---|---|
| Systemd đang nhìn dịch vụ như thế nào? | `systemctl status/show` |
| Dịch vụ đã ghi gì vào nhật ký? | `journalctl -u` |
| Tiến trình nào đang tồn tại? | `pgrep`, `ps` |
| Luồng nào đang dùng CPU? | `pidstat -t`, công cụ runtime |
| Cổng nào đang lắng nghe? | `ss -lntp`, `lsof -i` |
| HTTP cục bộ có hoạt động? | `curl -fsS -v` |
| Hệ thống tệp còn bao nhiêu dung lượng? | `df` |
| Thư mục nào dùng nhiều dung lượng? | `du` |
| Tệp đã xóa nào vẫn đang mở? | `lsof +L1` |
| Có áp lực RAM không? | `free`, `vmstat` |
| Kernel có OOM hoặc lỗi I/O không? | `journalctl -k`, `dmesg` |
| DNS và định tuyến ra sao? | `ip route`, `dig` |
| Gói tin có tới host không? | `tcpdump` |

Bảng này không thay thế suy luận; nó chỉ ánh xạ **câu hỏi** sang **nguồn bằng chứng** phù hợp.

## Mô hình tư duy (Mental Model)

Troubleshooting có thể xem như quá trình **cắt tỉa đồ thị nguyên nhân (causal graph pruning)**. Mỗi câu lệnh nên được chạy vì nó trả lời một câu hỏi có khả năng loại bỏ các nhánh trong cây giả thuyết.

Thay vì chạy 30 câu lệnh theo thói quen, hãy xác định trước: "Nếu kết quả là A thì tôi sẽ nghi X; nếu là B thì chuyển sang Y." Khi đó terminal trở thành công cụ đo lường theo phương pháp khoa học thay vì một nghi thức lặp lại.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Kỹ sư senior chỉ là người biết nhiều câu lệnh hơn."** Giá trị lớn hơn nằm ở mô hình hệ thống và khả năng chọn giả thuyết cần kiểm tra.

**"Restart thành công nghĩa là đã sửa xong."** Phục hồi không chứng minh nguyên nhân gốc.

**"Dòng lỗi cuối cùng trong log chính là nguyên nhân."** Nó có thể chỉ là hậu quả phía sau; cần dựng lại chuỗi thời gian và quan hệ nhân quả.

**"Một metric cao chắc chắn là nút thắt."** Cần đặt nó trong bối cảnh workload và đối chiếu với các bằng chứng khác.

**"Gỡ lỗi production nên thay đổi nhanh để thử."** Thay đổi không kiểm soát có thể làm mất bằng chứng và tăng phạm vi ảnh hưởng.

## Checklist production ngắn

Khi chưa biết bắt đầu từ đâu, có thể dùng chuỗi quan sát tương đối an toàn sau:

```bash
date '+%F %T %Z'
hostname
systemctl status app --no-pager
journalctl -u app -n 200 --no-pager
pgrep -af 'java.*app'
sudo ss -lntp
curl -fsS -v http://127.0.0.1:8080/health
free -h
df -h
uptime
```

Sau đó **không tiếp tục một cách máy móc**. Hãy chọn nhánh điều tra tiếp theo dựa trên kết quả vừa quan sát.