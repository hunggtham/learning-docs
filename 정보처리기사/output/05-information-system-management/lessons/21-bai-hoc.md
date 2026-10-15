# 네트워크 및 정보 침해 공격 (Network & Info Security Attacks)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế tấn công và công cụ khai thác của các hình thức tấn công từ chối dịch vụ phân tán (**DDoS - Distributed Denial of Service**): Kiến trúc Master-Agent (Trin00, TFN, TFN2K, Stacheldraht).
- Phân biệt các kỹ thuật tấn công mạng kinh điển: **SMURFING** (lợi dụng ICMP Echo Request gửi tới địa chỉ Broadcast), Chiếm đoạt phiên làm việc (**세션 하이재킹 - Session Hijacking**), và Làm tràn bảng MAC của Switch (**스위치 재밍 - Switch Jamming / MAC Flooding**).
- Nhận diện các phương thức tấn công thiết bị không dây Bluetooth: **BlueSnarf** (đánh cắp tệp danh bạ), **BlueBug** (chiếm quyền điều khiển nghe lén), và **BlueJacking** (gửi tin nhắn rác nặc danh).

## 핵심 키워드 (Từ khóa)
- DDoS 공격 (분산 서비스 거부 - Agent/Zombie PC)
- DDoS 공격 도구 (Trin00, TFN, TFN2K, Stacheldraht)
- 스머핑 (SMURFING - ICMP Broadcast 악용)
- 세션 하이재킹 (Session Hijacking - TCP Sequence Number 예측)
- 스위치 재밍 (Switch Jamming - MAC Flooding, 허브화)
- 블루투스 3대 공격 (BlueSnarf, BlueBug, BlueJacking)
- 제로 데이 공격 (Zero-Day Attack) & 랜섬웨어 (Ransomware)

## 선행·연결 개념 (Kiến thức liên kết)
- [20-bai-hoc.md](20-bai-hoc.md): Cấu trúc hình học mạng và các chuẩn IEEE 802.
- [22-bai-hoc.md](22-bai-hoc.md): Các công nghệ phòng thủ an ninh mạng (VPN, SSH, Tường lửa).
- [27-bai-hoc.md](27-bai-hoc.md): Các lỗ hổng ứng dụng web và đe dọa an ninh nâng cao.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh các hình thức tấn công trong đề thi:
  - **SMURFING:** Lợi dụng giao thức **ICMP**; kẻ tấn công giả mạo IP nguồn là IP của nạn nhân rồi gửi gói tin **Ping tới địa chỉ Broadcast** của một mạng lớn $\rightarrow$ Hàng nghìn máy tính đồng loạt gửi trả lời về nạn nhân làm nạn nhân tê liệt.
  - **스위치 재밍 (Switch Jamming):** Bơm hàng triệu địa chỉ **MAC giả mạo** làm tràn bộ nhớ CAM của Switch $\rightarrow$ Switch mất khả năng chuyển mạch thông minh và **tự động thoái hóa biến thành một chiếc Dummy Hub** $\rightarrow$ Kẻ tấn công tha hồ nghe lén (Sniffing).
  - Khẩu quyết Bluetooth:
    - **BlueSnarf:** Snarf = Snatch (Cướp đoạt tệp tin, danh bạ dữ liệu).
    - **BlueBug:** Bug = Con bọ (Gài bọ nghe lén, chiếm quyền điều khiển cuộc gọi).
    - **BlueJacking:** Jacking = Hijack (Gửi tin nhắn rác, spam quấy rối).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các hình thức tấn công mạng (Network Attacks):**

| Tên đòn tấn công | Cơ chế kỹ thuật chi tiết | Hậu quả an ninh & Dấu hiệu nhận diện |
| :--- | :--- | :--- |
| **DDoS** (Distributed DoS) | Kẻ tấn công (Attacker) điều khiển máy chủ chỉ huy (Master/Handler) ra lệnh cho hàng nghìn máy tính ma (Agent / Zombie PC / Botnet) đồng loạt xả lưu lượng khổng lồ vào máy chủ mục tiêu. | Làm cạn kiệt băng thông đường truyền hoặc tài nguyên CPU/RAM của máy chủ; **4 công cụ tấn công DDoS kinh điển trong đề thi: Trin00, TFN, TFN2K, Stacheldraht**. |
| **스머핑 (SMURFING)** | Kẻ tấn công gửi liên tục các gói tin `ICMP Echo Request` (Ping) tới địa chỉ Broadcast của một mạng trung gian (Amplifier), nhưng **giả mạo địa chỉ IP nguồn (IP Spoofing) là địa chỉ của nạn nhân**. | Toàn bộ các máy tính trong mạng trung gian đồng loạt gửi gói tin trả lời `ICMP Echo Reply` dồn dập về phía nạn nhân, làm sập mạng nạn nhân ngay lập tức. |
| **세션 하이재킹** (Session Hijacking) | Kẻ tấn công theo dõi, tính toán và dự đoán số thứ tự tuần tự (**TCP Sequence Number**) trong phiên truyền thông giữa Client và Server để ngắt kết nối hợp lệ của Client và chiếm đoạt phiên làm việc của người dùng đã xác thực. | Vượt qua cơ chế xác thực đăng nhập mà không cần biết mật khẩu tài khoản của người dùng. |
| **스위치 재밍** (Switch Jamming) | Kẻ tấn công liên tục phát các khung Ethernet chứa địa chỉ MAC nguồn giả mạo ngẫu nhiên với tốc độ cực cao, làm tràn bộ nhớ bảng địa chỉ (**CAM Table**) của thiết bị Switch. | Switch rơi vào trạng thái lỗi an toàn (**Fail-Open**), tự động chuyển sang hoạt động như một **Dummy Hub** (phát sóng Broadcast tới mọi cổng), cho phép kẻ tấn công thu bắt toàn bộ gói tin trong mạng (Sniffing). |

- **2. Bảng phân loại 3 hình thức tấn công thiết bị không dây Bluetooth:**

| Tên đòn tấn công | Mục tiêu & Phương thức khai thác | Hậu quả gây hại cho thiết bị nạn nhân |
| :--- | :--- | :--- |
| **블루재킹 (BlueJacking)** | Lợi dụng tính năng kết nối OBEX (Object Exchange) của Bluetooth để gửi các danh thiếp vCard hoặc tin nhắn nặc danh không mong muốn tới các máy lân cận. | Gây phiền toái, quấy rối bằng tin nhắn rác; không gây mất mát dữ liệu nội bộ. |
| **블루스나프 (BlueSnarf)** | Khai thác lỗ hổng xác thực của giao thức OBEX Push để truy xuất trái phép vào hệ thống tệp tin nội bộ của điện thoại mà không cần sự đồng ý của chủ máy. | **Đánh cắp danh bạ điện thoại, tin nhắn SMS, lịch làm việc, hình ảnh cá nhân**. |
| **블루버그 (BlueBug)** | Khai thác lỗi phần mềm quản lý kết nối Bluetooth để tạo một kênh giao tiếp bí mật ở tầng sâu; gửi các lệnh điều khiển viễn thông AT Commands tới máy nạn nhân. | **Chiếm toàn quyền kiểm soát điện thoại, tự động thực hiện cuộc gọi, gửi tin nhắn ngầm, nghe lén đàm thoại** mà nạn nhân không hề hay biết. |

- **3. Các hiểm họa hệ thống và phần mềm khác:**
  - **Zero-Day Attack (제로 데이 공격):** Tấn công xảy ra ngay trong khoảng thời gian từ khi lỗ hổng bảo mật được phát hiện đến trước khi nhà sản xuất kịp phát hành bản vá sửa lỗi (Patch) $\rightarrow$ Hoàn toàn không có phương án phòng thủ bằng chữ ký nhận diện.
  - **Ransomware (랜섬웨어):** Mã độc xâm nhập vào máy tính, sử dụng các thuật toán mã hóa mạnh (AES, RSA) để khóa toàn bộ tệp tài liệu và đòi tiền chuộc (Ransom) bằng tiền điện tử để đổi lấy khóa giải mã.
  - **Backdoor (백도어):** Lối đi bí mật do lập trình viên hoặc kẻ xâm nhập cố tình để lại nhằm vượt qua cơ chế kiểm tra xác thực thông thường.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Biện pháp phòng thủ tấn công SMURFING:**
  - Cấu hình tất cả các thiết bị Router biên vô hiệu hóa tính năng chuyển tiếp gói tin gửi tới địa chỉ Broadcast của mạng con (Directed Broadcast); cấu hình máy chủ bỏ qua các gói tin ICMP gửi tới địa chỉ quảng bá.

### 복습 체크리스트
- [ ] Kể tên 4 công cụ tấn công DDoS kinh điển: Trin00, TFN, TFN2K, Stacheldraht.
- [ ] Nhớ cơ chế SMURFING: Giả mạo IP nguồn nạn nhân và gửi ICMP Ping tới địa chỉ Broadcast.
- [ ] Nhớ Switch Jamming làm tràn bảng CAM khiến Switch bị biến thành Dummy Hub.
- [ ] Phân biệt 3 đòn Bluetooth: BlueJacking (spam rác), BlueSnarf (trộm file danh bạ), BlueBug (nghe lén điều khiển).
- [ ] Nhớ Zero-Day Attack là đòn tấn công xảy ra trước khi có bản vá bảo mật (Patch).
