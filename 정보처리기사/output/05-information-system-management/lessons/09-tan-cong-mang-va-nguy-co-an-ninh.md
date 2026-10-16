# 네트워크 침해 공격 및 보안 위협 (Tấn công mạng & Nguy cơ đe dọa an ninh thông tin: DoS/DDoS, XSS, Spoofing, Malware)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc mạng điều khiển, cơ chế vận hành và các công cụ khai thác của tấn công từ chối dịch vụ phân tán (**DDoS - Distributed Denial of Service**): Trin00, TFN, TFN2K, Stacheldraht.
- Phân tích bản chất kỹ thuật của 6 đòn tấn công từ chối dịch vụ (DoS) kinh điển: **SYN Flooding**, **SMURFING**, **Ping of Death**, **TearDrop**, **Land Attack**, và **HTTP GET Flooding**.
- Phân biệt các kỹ thuật nghe lén (**Sniffing**), giả mạo danh tính (**IP/ARP/DNS Spoofing**) và chiếm đoạt phiên làm việc (**Session Hijacking**).
- Hiểu rõ cơ chế làm tràn bảng MAC của thiết bị chuyển mạch (**스위치 재밍 - Switch Jamming / MAC Flooding**) và các hình thức tấn công không dây Bluetooth (**Bluebugging, Bluesnarfing, Bluejacking**).
- Phân loại các chủng loại mã độc nguy hiểm (**Ransomware, Rootkit, Botnet, Keylogger, Backdoor**) và các hình thức lừa đảo phi kỹ thuật (**Phishing, Smishing, Qshing**).

## 핵심 키워드 (Từ khóa song ngữ)
- 서비스 거부 공격 (DoS — Denial of Service, làm cạn kiệt tài nguyên mạng và hệ thống)
- 분산 서비스 거부 공격 (DDoS — Distributed DoS, kiến trúc Attacker $\rightarrow$ Master $\rightarrow$ Agent/Zombie)
- DDoS 공격 도구 (DDoS Attack Tools — Trin00, TFN, TFN2K, Stacheldraht)
- SYN 플러딩 (SYN Flooding — Lợi dụng cơ chế bắt tay 3 bước TCP, làm tràn Backlog Queue)
- 스머핑 (SMURFING — Giả mạo IP nguồn nạn nhân, gửi ICMP Echo Request tới địa chỉ Broadcast)
- 죽음의 핑 (Ping of Death — Gói tin Ping phân mảnh vượt quá $65,535\text{ bytes}$ gây tràn đệm)
- 티어드롭 (TearDrop — Cố tình làm chồng lấn Offset phân mảnh IP gây sập hệ điều hành)
- 랜드 어택 (Land Attack — Giả mạo IP nguồn và IP đích giống hệt nhau tạo vòng lặp vô tận)
- ARP 스푸핑 (ARP Spoofing — Đầu độc bảng ánh xạ ARP Poisoning để thực hiện tấn công MITM)
- 스위치 재밍 (Switch Jamming — Làm tràn bảng MAC buộc Switch phát tán Broadcast như Hub)
- 블루투스 공격 (Bluetooth Attacks — Bluebugging chiếm quyền, Bluesnarfing trích xuất dữ liệu, Bluejacking gửi tin rác)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Khi các cơ chế xác thực và phân quyền tại [08-xac-thuc-va-kiem-soat-truy-cap.md](08-xac-thuc-va-kiem-soat-truy-cap.md) được thiết lập, kẻ tấn công không thể đăng nhập trực tiếp sẽ chuyển sang phá hoại tính khả dụng (Availability) bằng các cuộc tấn công từ chối dịch vụ hoặc nghe lén trộm dữ liệu trên đường truyền.
- **Đang giải quyết gì (Current Problem):** Bài học này bóc tách toàn diện dấu hiệu nhận biết, cơ chế kỹ thuật và hậu quả của tất cả các hình thức tấn công mạng, giao thức và mã độc thường xuyên xuất hiện trong đề thi Kỹ sư CNTT.
- **Dùng đi đâu (Forward Handoff):** Để phát hiện và ngăn chặn các đòn tấn công mạng này, quản trị viên cần triển khai hệ thống Tường lửa, IDS/IPS, WAF và giám sát tệp nhật ký hệ thống Linux được trình bày trong [10-giai-phap-va-thiet-bi-bao-mat-mang.md](10-giai-phap-va-thiet-bi-bao-mat-mang.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **DDoS Tools:** Nhớ tên 4 công cụ kinh điển: **Trin00, TFN, TFN2K, Stacheldraht**.
- **Bộ 6 đòn tấn công DoS kinh điển (Phải nhận diện bằng từ khóa kỹ thuật):**
  - Nhắc đến **"TCP 3-Way Handshake"**, **"SYN gói tin gửi liên tục với IP giả"**, **"Backlog Queue tràn"** $\rightarrow$ Chọn **SYN Flooding**.
  - Nhắc đến **"ICMP Echo Request"**, **"IP nguồn giả mạo là IP nạn nhân"**, **"Gửi tới Broadcast mạng trung gian"** $\rightarrow$ Chọn **스머핑 (SMURF / Smurfing)**.
  - Nhắc đến **"Kích thước gói tin lớn hơn $65,535\text{ bytes}$"**, **"Tràn đệm khi Reassembly"** $\rightarrow$ Chọn **죽음의 핑 (Ping of Death)**.
  - Nhắc đến **"Phân mảnh IP (Fragmentation)"**, **"Trường Offset chồng lấn nhau (Overlapping)"** $\rightarrow$ Chọn **티어드롭 (TearDrop)**.
  - Nhắc đến **"IP nguồn và IP đích giống hệt nhau (Source IP = Dest IP)"** $\rightarrow$ Chọn **랜드 어택 (Land Attack)**.
  - Nhắc đến **"HTTP GET liên tục đòi xử lý tài nguyên nặng làm cạn kiệt Web Server"** $\rightarrow$ Chọn **HTTP GET 플러딩 (CC Attack)**.
- **Tấn công Switch & Bluetooth:**
  - Làm tràn bảng MAC biến Switch thành Hub $\rightarrow$ **스위치 재밍 (Switch Jamming)**.
  - Tấn công Bluetooth: Chiếm quyền điều khiển $\rightarrow$ **Bluebugging**; Trích xuất dữ liệu $\rightarrow$ **Bluesnarfing**; Gửi tin nhắn rác nặc danh $\rightarrow$ **Bluejacking**.

---

## 네트워크 침해 공격 및 보안 위협

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tấn công từ chối dịch vụ phân tán (DDoS)
- **Kiến trúc mạng tấn công DDoS:**
  - **Attacker (공격자):** Kẻ chủ mưu phát lệnh tấn công.
  - **Master / Handler (마스터):** Máy chủ trung gian bị kẻ tấn công chiếm quyền kiểm soát để điều phối các máy con.
  - **Agent / Zombie PC (에이전트):** Đội quân hàng ngàn máy tính bị lây nhiễm mã độc (Botnet) trực tiếp xả lưu lượng tấn công vào mục tiêu.
  - **Target (공격 대상):** Hệ thống máy chủ nạn nhân bị tê liệt do quá tải tài nguyên.
- **Các công cụ tấn công DDoS tiêu biểu trong đề thi:**
  - **Trin00:** Công cụ DDoS sử dụng giao thức UDP để làm ngập lụt băng thông.
  - **TFN (Tribe Flood Network):** Hỗ trợ đa dạng tấn công SYN Flood, UDP Flood, ICMP Echo Flood.
  - **TFN2K:** Phiên bản nâng cấp mã hóa lưu lượng điều khiển và làm xáo trộn cổng giao tiếp.
  - **Stacheldraht:** Kết hợp tính năng của Trin00 và TFN, có cơ chế tự động cập nhật mã độc cho các Agent.

#### 2. Sáu đòn tấn công DoS kinh điển

| Tên đòn tấn công | Tên tiếng Hàn | Cơ chế kỹ thuật chi tiết | Biện pháp phòng vệ chuẩn |
| :--- | :--- | :--- | :--- |
| **SYN Flooding** | **SYN 플러딩** | Lợi dụng cơ chế bắt tay 3 bước của TCP. Kẻ tấn công gửi liên tiếp các gói tin `SYN` với địa chỉ IP nguồn giả mạo. Máy chủ nạn nhân cấp phát bộ nhớ, gửi lại `SYN+ACK` và chờ đợi phản hồi `ACK`. Do IP giả mạo không bao giờ gửi lại `ACK`, hàng đợi kết nối nửa mở (**Backlog Queue**) bị lấp đầy hoàn toàn, làm máy chủ từ chối mọi kết nối hợp lệ mới. | - Thu ngắn thời gian chờ Timeout.<br>- Tăng kích thước Backlog Queue.<br>- Kích hoạt tính năng **SYN Cookie** trên hệ điều hành. |
| **Smurfing** | **스머핑** | Kẻ tấn công gửi gói tin `ICMP Echo Request` (Ping) với **địa chỉ IP nguồn giả mạo chính là địa chỉ IP của máy chủ nạn nhân** tới **địa chỉ Quảng bá (Directed Broadcast)** của một mạng trung gian. Toàn bộ hàng trăm máy tính trong mạng trung gian đồng loạt gửi gói tin trả lời `ICMP Echo Reply` về máy nạn nhân, làm sập đường truyền mạng. | Cấu hình Router chặn các gói tin Broadcast từ ngoài vào (`no ip directed-broadcast`), tắt phản hồi ICMP trên thiết bị. |
| **Ping of Death** | **죽음의 핑** | Giao thức IP giới hạn kích thước tối đa của một gói tin là $65,535\text{ bytes}$. Kẻ tấn công dùng lệnh Ping chia nhỏ một gói tin có dung lượng khổng lồ thành nhiều mảnh (Fragments). Khi máy nạn nhân thực hiện tái lắp ghép (Reassembly) các mảnh này, bộ nhớ đệm hệ điều hành bị tràn, làm treo máy hoặc khởi động lại đột ngột. | Cấu hình tường lửa lọc bỏ các gói tin ICMP có kích thước phân mảnh bất thường, vá lỗi hệ điều hành. |
| **TearDrop** | **티어드롭** | Khi truyền gói tin lớn qua mạng, IP chia nhỏ gói tin và dùng trường **Fragment Offset** để ghi lại vị trí ghép nối. Kẻ tấn công cố tình thay đổi trường này để các mảnh bị **chồng lấn lên nhau (Overlapping)**. Quá trình tái lắp ghép trên máy nạn nhân gặp lỗi logic không xử lý được, gây cạn kiệt tài nguyên CPU và làm sập máy chủ. | Cập nhật bản vá hệ điều hành kiểm tra tính hợp lệ của trường Offset trước khi tái lắp ghép. |
| **Land Attack** | **랜드 어택** | Kẻ tấn công gửi gói tin TCP `SYN` có **địa chỉ IP nguồn và IP đích giống hệt nhau** (đồng thời Port nguồn = Port đích), đều trỏ về địa chỉ IP của nạn nhân. Máy nạn nhân nhận gói tin và tự động gửi gói tin trả lời lại cho chính mình, tạo thành vòng lặp vô tận làm tê liệt hoàn toàn CPU và RAM. | Cấu hình tường lửa chặn ngay các gói tin có địa chỉ IP nguồn trùng với địa chỉ IP nội bộ của hệ thống. |
| **HTTP GET Flooding** | **HTTP GET 플러딩 (CC Attack)** | Tấn công tầng ứng dụng (L7). Kẻ tấn công gửi liên tục các yêu cầu HTTP GET hợp lệ đòi truy xuất các trang web có nội dung nặng hoặc truy vấn CSDL phức tạp, làm cạn kiệt tài nguyên xử lý của Web Server mà không cần dùng băng thông quá lớn. | Sử dụng thiết bị tường lửa ứng dụng web (**WAF**), chặn theo tần suất yêu cầu (Rate Limiting), dùng Captcha. |

#### 3. Các kỹ thuật tấn công nghe lén, giả mạo và chuyển mạch
- **스니핑 (Sniffing — Nghe lén):**
  - Kẻ tấn công chuyển card mạng sang chế độ **Promiscuous Mode** để thu thập toàn bộ các gói tin truyền qua mạng nội bộ (LAN).
  - *Phòng vệ:* Bắt buộc mã hóa toàn bộ dữ liệu truyền tải (dùng HTTPS, SSH, IPsec VPN).
- **스푸핑 (Spoofing — Giả mạo):**
  - **ARP Spoofing:** Kẻ tấn công gửi liên tục các bản tin `ARP Reply` giả mạo nhằm đầu độc bảng ánh xạ IP-MAC (**ARP Poisoning**) của các máy trong mạng, mạo danh Gateway để toàn bộ lưu lượng mạng đều đi qua máy kẻ tấn công (tấn công Man-in-the-Middle).
  - **IP Spoofing:** Giả mạo IP nguồn của một máy tính tin cậy để vượt qua hàng rào kiểm soát IP của tường lửa.
  - **DNS Spoofing:** Can thiệp làm sai lệch bản ghi DNS để chuyển hướng người dùng sang máy chủ giả mạo.
- **스위치 재밍 (Switch Jamming / MAC Flooding):**
  - Kẻ tấn công gửi liên tục hàng triệu địa chỉ MAC nguồn giả mạo vào cổng của Switch, làm **tràn bộ nhớ bảng địa chỉ MAC (CAM Table)**. Khi bảng MAC bị đầy, Switch không thể học địa chỉ mới và tự động chuyển sang chế độ dự phòng an toàn (**Fail-Open**), biến Switch thông minh thành một thiết bị Hub phát tán (Broadcast) toàn bộ lưu lượng ra mọi cổng, giúp kẻ tấn công nghe lén toàn bộ mạng dễ dàng.

#### 4. Các hình thức tấn công không dây Bluetooth
- **1. Bluebugging (블루버깅):** Hình thức nguy hiểm nhất; kẻ tấn công khai thác lỗ hổng bảo mật Bluetooth để chiếm toàn quyền kiểm soát thiết bị nạn nhân từ xa (tự động gọi điện, nhắn tin, nghe lén cuộc gọi).
- **2. Bluesnarfing (블루스나핑):** Kẻ tấn công truy cập trái phép và trích xuất dữ liệu nhạy cảm (danh bạ, lịch làm việc, tin nhắn SMS, hình ảnh) từ thiết bị nạn nhân qua kết nối Bluetooth.
- **3. Bluejacking (블루재킹):** Gửi các tin nhắn văn bản, hình ảnh hoặc danh thiếp nặc danh không mong muốn (Spam) tới các thiết bị Bluetooth xung quanh trong phạm vi phủ sóng.

#### 5. Chủng loại mã độc và kỹ thuật lừa đảo
- **랜섬웨어 (Ransomware):** Mã độc mã hóa toàn bộ tệp tin quan trọng trên máy nạn nhân và yêu cầu trả tiền chuộc để lấy khóa giải mã.
- **루트킷 (Rootkit):** Tập hợp các công cụ ngầm ẩn mình sâu trong nhân hệ điều hành (Kernel Level), che giấu các tiến trình, tệp tin độc hại và duy trì quyền truy cập quản trị cho kẻ tấn công.
- **Lừa đảo phi kỹ thuật (Social Engineering):**
  - **Phishing (피싱):** Gửi email giả mạo các tổ chức tài chính uy tín lừa người dùng nhập mật khẩu.
  - **Smishing (스미싱):** Lừa đảo qua tin nhắn điện thoại (SMS) có chứa đường link độc hại.
  - **Qshing (큐싱):** Chèn mã QR giả mạo đè lên mã QR thanh toán chuẩn để chuyển hướng người dùng cài mã độc.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Cơ chế hoạt động của kỹ thuật phòng thủ SYN Cookie
Khi máy chủ web đối mặt với cuộc tấn công SYN Flooding khổng lồ:
1. Thông thường, máy chủ phải cấp phát một vùng nhớ nhỏ trong hàng đợi **Backlog Queue** để lưu trạng thái kết nối nửa mở (Half-open connection).
2. Khi bật **SYN Cookie**, máy chủ sẽ **KHÔNG cấp phát bộ nhớ** cho kết nối khi nhận được gói tin `SYN`.
3. Thay vào đó, máy chủ tính toán một giá trị Sequence Number khởi tạo đặc biệt dựa trên địa chỉ IP nguồn, Port nguồn, thời gian và một khóa bí mật, rồi gửi lại trong gói tin `SYN+ACK`.
4. Chỉ khi nào máy khách thực sự gửi lại gói tin `ACK` chứa giá trị Sequence Number hợp lệ, máy chủ mới tính toán ngược lại để xác minh và lúc đó mới chính thức cấp phát tài nguyên bộ nhớ cho kết nối. Kỹ thuật này giúp máy chủ hoàn toàn miễn nhiễm với việc bị làm tràn hàng đợi kết nối.

---

### 복습 체크리스트
- [ ] Nhớ tên 4 công cụ DDoS kinh điển: Trin00, TFN, TFN2K, Stacheldraht.
- [ ] Phân biệt chính xác 6 đòn DoS:
  - SYN Flooding (TCP 3-Way Handshake, tràn Backlog Queue).
  - Smurfing (ICMP Echo Request gửi tới Broadcast với IP nguồn nạn nhân).
  - Ping of Death (Gói tin Ping $> 65,535\text{ bytes}$ gây tràn đệm khi Reassembly).
  - TearDrop (Phân mảnh IP có Offset chồng lấn nhau gây sập HĐH).
  - Land Attack (IP nguồn = IP đích, tự gửi trả lời cho chính mình).
  - HTTP GET Flooding (Tấn công tầng ứng dụng làm cạn kiệt Web Server).
- [ ] Nắm được cơ chế Switch Jamming: Làm tràn bảng MAC buộc Switch phát tán lưu lượng như Hub.
- [ ] Phân biệt 3 đòn tấn công Bluetooth: Bluebugging (chiếm quyền), Bluesnarfing (trộm dữ liệu), Bluejacking (gửi tin rác).
- [ ] Hiểu rõ kỹ thuật SYN Cookie: Ngăn chặn SYN Flooding bằng cách không cấp phát bộ nhớ cho kết nối nửa mở.
