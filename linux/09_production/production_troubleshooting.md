# Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Triệu chứng không phải nguyên nhân gốc** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Quan sát trước khi thay đổi trạng thái** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối production troubleshooting với triệu chứng, telemetry, hypothesis và rollback, để xử lý sự cố theo bằng chứng thay vì đoán.

Xử lý sự cố (troubleshooting) không phải khả năng nhớ thật nhiều câu lệnh. Bản chất của nó là quá trình thu hẹp không gian giả thuyết bằng bằng chứng. Kỹ sư nhiều kinh nghiệm thường xử lý nhanh hơn không phải vì gõ lệnh nhanh hơn, mà vì biết **câu hỏi tiếp theo nào có khả năng phân biệt hai nguyên nhân đang được nghi ngờ**.

## Triệu chứng không phải nguyên nhân gốc

"API hết thời gian chờ (timeout / 타임아웃)", "Java chết", "hệ thống tệp đầy" hoặc "CPU cao" đều chỉ là triệu chứng. hết thời gian chờ (timeout / 타임아웃) có thể đến từ DNS, kết nối TCP, luồng thực thi (thread / 스레드) pool, khóa cơ sở dữ liệu hoặc dịch vụ phía sau. Tiến trình Java biến mất có thể do ứng dụng crash, systemd dừng dịch vụ, OOM killer hoặc một người vận hành gửi tín hiệu (signal / 신호).

Mục tiêu đầu tiên là mô tả triệu chứng đủ cụ thể:

```text
Ai hoặc hệ thống nào quan sát thấy lỗi?
Lỗi được quan sát từ đâu?
Bắt đầu từ thời điểm nào?
Ảnh hưởng tất cả yêu cầu hay chỉ một phần?
Có triển khai hoặc thay đổi cấu hình nào gần thời điểm đó không?
```

> **Nối mạch:** Trong **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Quan sát trước khi thay đổi trạng thái** nối từ **Triệu chứng không phải nguyên nhân gốc** sang **Chẩn đoán theo từng lớp**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Với Java bị treo hoặc dùng CPU cao, nếu chính sách cho phép nên lấy luồng thực thi (thread / 스레드) dump trước khi restart:

```bash
jcmd <PID> Thread.print > /tmp/thread-$(date +%s).txt
```

> **Nối mạch:** Ở chặng này của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Chẩn đoán theo từng lớp** nối từ **Quan sát trước khi thay đổi trạng thái** sang **Dịch vụ không khởi động được**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Dịch vụ không khởi động được** nối từ **Chẩn đoán theo từng lớp** sang **Tiến trình tồn tại nhưng API không hoạt động**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Tiến trình tồn tại nhưng API không hoạt động** nối từ **Dịch vụ không khởi động được** sang **CPU cao**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tiến trình tồn tại nhưng API không hoạt động

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
pgrep -af 'java.*app'
sudo ss -lntp | grep ':8080'
curl -fsS -v http://127.0.0.1:8080/health
```

Nếu không có listener, hãy kiểm tra nhật ký khởi động, cấu hình và địa chỉ bind. Nếu listener tồn tại nhưng `curl` bị treo, các giả thuyết có thể là cạn luồng thực thi (thread / 스레드) pool, deadlock, phụ thuộc bên ngoài hoặc trạng thái ứng dụng. Nếu `curl` cục bộ thành công, chuyển sang định tuyến, firewall, bộ cân bằng tải (load balancer / 로드 밸런서) và DNS.

> **Nối mạch:** Ở chặng này của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **CPU cao** nối từ **Tiến trình tồn tại nhưng API không hoạt động** sang **Bộ nhớ tăng hoặc tiến trình bị kết thúc**, vì cơ chế trước tạo đầu vào cho bước sau.

## CPU cao

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
uptime
nproc
top
pidstat -p <PID> 1
pidstat -t -p <PID> 1
```

Với Java, cần đối chiếu luồng dùng CPU cao với luồng thực thi (thread / 스레드) dump. Lấy nhiều mẫu cách nhau vài giây giúp phân biệt công việc tăng tải tạm thời với vòng lặp hoặc đường mã luôn nóng.

Không nên tăng CPU ngay nếu CPU cao chỉ là hệ quả của một cơn bão thử lại (retry / 재시도) do dịch vụ phụ thuộc đang lỗi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Bộ nhớ tăng hoặc tiến trình bị kết thúc** nối từ **CPU cao** sang **Hệ thống tệp hết dung lượng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bộ nhớ tăng hoặc tiến trình bị kết thúc

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
free -h
ps -p <PID> -o pid,%mem,rss,vsz,etime,cmd
journalctl -k | grep -i -E 'oom|out of memory|killed process'
```

Nếu ứng dụng chạy trong bộ chứa (container / 컨테이너), cần kiểm tra giới hạn bộ nhớ của cgroup/bộ chứa (container / 컨테이너). Việc host còn nhiều RAM không đủ để loại trừ OOM trong cgroup.

Rò rỉ bộ nhớ cần xu hướng theo thời gian và bằng chứng ở thời gian chạy (runtime / 런타임); một ảnh chụp RSS không thể chỉ ra đối tượng Java nào đang bị giữ lại.

> **Nối mạch:** Trong **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Hệ thống tệp hết dung lượng** nối từ **Bộ nhớ tăng hoặc tiến trình bị kết thúc** sang **Lỗi mạng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hệ thống tệp hết dung lượng

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
df -h
df -i
sudo du -xhd1 /var 2>/dev/null | sort -hr
sudo lsof +L1
```

Chuỗi này giúp phân biệt hết byte lưu trữ, hết inode, tệp còn nhìn thấy trong cây thư mục và tệp đã xóa nhưng vẫn đang mở.

Nếu nhật ký quá lớn, hãy tìm nguyên nhân tăng trưởng trước khi chỉ xóa tệp. Một vòng lặp thử lại (retry / 재시도) có thể tạo bão log, và việc đầy đĩa khi đó chỉ là triệu chứng phía sau.

> **Nối mạch:** Ở chặng này của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Lỗi mạng** nối từ **Hệ thống tệp hết dung lượng** sang **Đối chiếu theo dòng thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Lỗi mạng** đặt tiêu chí; **Đối chiếu theo dòng thời gian** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Chẩn đoán so sánh** mở rộng hệ quả.

## Đối chiếu theo dòng thời gian

Một trong những câu hỏi có giá trị nhất là: **điều gì đã thay đổi ngay trước khi triệu chứng xuất hiện?**

Kiểm tra sản phẩm tạo ra (artifact / 산출물) triển khai, `mtime` của cấu hình, lịch sử gói, thời điểm dịch vụ khởi động lại và nhật ký:

```bash
systemctl show app -p ActiveEnterTimestamp
find /opt/app -type f -newermt '2026-09-20 15:30' -ls
```

Tương quan không tự động chứng minh quan hệ nhân quả, nhưng một thay đổi xảy ra sát thời điểm lỗi là giả thuyết mạnh để kiểm tra tiếp.

> **Nối mạch:** Trong **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Đối chiếu theo dòng thời gian** đặt tiêu chí; **Chẩn đoán so sánh** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Phục hồi khác với tìm nguyên nhân gốc** mở rộng hệ quả.

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

> **Nối mạch:** Ở chặng này của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Chẩn đoán so sánh** đặt tiêu chí; **Phục hồi khác với tìm nguyên nhân gốc** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Chọn công cụ theo câu hỏi** mở rộng hệ quả.

## Phục hồi khác với tìm nguyên nhân gốc

**Phục hồi (recovery)** đưa dịch vụ trở về trạng thái có thể chấp nhận. **Phân tích nguyên nhân gốc (root-cause analysis)** giải thích chuỗi nguyên nhân và cách ngăn lặp lại. Có thể restart để phục hồi trước rồi điều tra dựa trên bằng chứng đã chụp lại. Không nên nhầm "restart xong hết lỗi" với một lời giải thích nguyên nhân.

Một phân tích sau sự cố tốt nên hỏi: yếu tố kích hoạt là gì? điều kiện tiềm ẩn nào cho phép lỗi lan rộng? hệ thống phát hiện và phục hồi ra sao? thay đổi nào làm giảm khả năng tái diễn?

> **Nối mạch:** Đặt trong câu hỏi lớn của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Chọn công cụ theo câu hỏi** nối từ **Phục hồi khác với tìm nguyên nhân gốc** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chọn công cụ theo câu hỏi

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

| Câu hỏi | Công cụ quan sát phù hợp |
|---|---|
| Systemd đang nhìn dịch vụ như thế nào? | `systemctl status/show` |
| Dịch vụ đã ghi gì vào nhật ký? | `journalctl -u` |
| Tiến trình nào đang tồn tại? | `pgrep`, `ps` |
| Luồng nào đang dùng CPU? | `pidstat -t`, công cụ thời gian chạy (runtime / 런타임) |
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

> **Nối mạch:** Trong **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Chọn công cụ theo câu hỏi** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Troubleshooting có thể xem như quá trình **cắt tỉa đồ thị nguyên nhân (causal graph pruning)**. Mỗi câu lệnh nên được chạy vì nó trả lời một câu hỏi có khả năng loại bỏ các nhánh trong cây giả thuyết.

Thay vì chạy 30 câu lệnh theo thói quen, hãy xác định trước: "Nếu kết quả là A thì tôi sẽ nghi X; nếu là B thì chuyển sang Y." Khi đó terminal trở thành công cụ đo lường theo phương pháp khoa học thay vì một nghi thức lặp lại.

> **Nối mạch:** Ở chặng này của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Những hiểu lầm phổ biến (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Checklist môi trường vận hành (production / 운영 환경) ngắn** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Kỹ sư cấp cao (senior / 시니어) chỉ là người biết nhiều câu lệnh hơn."** Giá trị lớn hơn nằm ở mô hình hệ thống và khả năng chọn giả thuyết cần kiểm tra.

**"Restart thành công nghĩa là đã sửa xong."** Phục hồi không chứng minh nguyên nhân gốc.

**"Dòng lỗi cuối cùng trong log chính là nguyên nhân."** Nó có thể chỉ là hậu quả phía sau; cần dựng lại chuỗi thời gian và quan hệ nhân quả.

**"Một chỉ số (metric / 지표) cao chắc chắn là nút thắt."** Cần đặt nó trong bối cảnh tải công việc (workload / 워크로드) và đối chiếu với các bằng chứng khác.

**"Gỡ lỗi môi trường vận hành (production / 운영 환경) nên thay đổi nhanh để thử."** Thay đổi không kiểm soát có thể làm mất bằng chứng và tăng phạm vi ảnh hưởng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Xử lý sự cố Linux trong môi trường vận hành (production / 운영 환경)**, **Checklist môi trường vận hành (production / 운영 환경) ngắn** nối từ **Những hiểu lầm phổ biến (Common Misconceptions)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Checklist môi trường vận hành (production / 운영 환경) ngắn

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

> **Bàn giao:** Sau **Checklist môi trường vận hành (production / 운영 환경) ngắn**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
