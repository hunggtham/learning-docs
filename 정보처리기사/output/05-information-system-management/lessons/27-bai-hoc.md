# 10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)

## 학습 목표 (Mục tiêu)
- Nhận diện bản chất kỹ thuật và cơ chế phòng chống các lỗ hổng phần mềm web phổ biến: SQL Injection, XSS, Buffer Overflow, Path Traversal.
- Phân tích cơ chế các đòn tấn công từ chối dịch vụ (DoS/DDoS) kinh điển: Ping of Death, SMURFING, Ping Flood và các công cụ DDoS phân tán (Trin00, TFN, Stacheldraht).
- Phân biệt các loại mã độc và kỹ thuật xâm nhập hệ thống: Worm, Virus, Ransomware, Keylogger, Backdoor, Honeypot.
- Nắm vững các hình thức tấn công tầng mạng đặc thù: Switch Jamming và các kiểu tấn công Bluetooth (BlueJacking, BlueSnarf, BlueBug, BluePrinting).

## 핵심 키워드 (Từ khóa)
- **웹 취약점 (Web Vulnerabilities)**: SQL Injection (SQL 삽입), XSS (크로스사이트 스크립팅), 버퍼 오버플로 (Stack Guard), 경로 조작 (Path Traversal).
- **DoS/DDoS 공격**: Ping of Death (ICMP gói quá khổ), SMURFING (IP/ICMP spoofing khuếch đại), Session Hijacking, DPI (Deep Packet Inspection).
- **Mã độc & Đe dọa**: 웜 (Worm - tự nhân bản qua mạng), 바이러스 (Virus - cần file ký chủ), 랜섬웨어 (Ransomware), 키로거 (Keylogger), 백도어 (Back Door), 허니팟 (Honeypot - hệ thống mồi nhử).
- **특수 공격 (Specialized Attacks)**: 스위치 재밍 (Switch Jamming - làm tràn bảng MAC), 블루스나프 (BlueSnarf - trộm file), 블루재킹 (BlueJacking - spam tin nhắn).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [26-bai-hoc.md](26-bai-hoc.md) (정보 보안 일반 및 시스템 보안 - Nền tảng CIA Triad).
- Liên kết với [21-bai-hoc.md](21-bai-hoc.md) (네트워크 및 정보 공격 - Phân loại DDoS và tấn công mạng).
- Liên kết với [32-bai-hoc.md](32-bai-hoc.md) (보안 취약점 및 보안 기능 - Chi tiết kỹ thuật Buffer Overflow, CSRF).

## 읽는 방법 (Cách đọc)
- Phân biệt rõ các loại tấn công Bluetooth: Blue**Jacking** = **Gửi tin nhắn rác**, Blue**Snarf** = **Đánh cắp dữ liệu/danh bạ**, Blue**Bug** = **Chiếm quyền điều khiển thiết bị**.
- Ghi nhớ bản chất SMURFING: Giả mạo IP nạn nhân gửi gói ICMP Echo Request tới địa chỉ Broadcast của mạng khuếch đại.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Lỗ hổng Web và Ứng dụng
| Tên lỗ hổng (KR / EN) | Cơ chế tấn công | Biện pháp phòng vệ chủ chốt |
| :--- | :--- | :--- |
| **SQL 삽입 (SQL Injection)** | Chèn chuỗi lệnh SQL độc hại vào trường nhập liệu để bẻ gãy cấu trúc câu truy vấn | Sử dụng Prepared Statements (Parameterized Queries), kiểm tra kiểu dữ liệu đầu vào |
| **XSS (Cross-Site Scripting)** | Chèn mã kịch bản độc hại (JavaScript) vào trang web để đánh cắp Cookie/Session của người dùng khác | HTML Entity Encoding (chuyển đổi `<, >, &`), bộ lọc XSS filter, CSP |
| **메모리 버퍼 오버플로 (Buffer Overflow)** | Ghi dữ liệu vượt quá kích thước vùng nhớ đệm được cấp phát nhằm chiếm quyền điều khiển con trỏ lệnh EIP | Sử dụng hàm an toàn (`strncpy`), bật cơ chế Stack Guard (Canary), ASLR, DEP/NX |
| **경로 조작 (Path Traversal)** | Sử dụng ký tự đại diện (`../`) để truy cập các tệp tin hệ thống nhạy cảm ngoài thư mục gốc web | Chuẩn hóa đường dẫn (canonicalization), xác thực chặt chẽ danh sách trắng (whitelist) tên file |

#### 2. Tấn công từ chối dịch vụ (DoS / DDoS)
- **Ping of Death**: Gửi gói tin ICMP Echo Request có kích thước lớn hơn giới hạn tối đa của giao thức IP (65,535 bytes). Khi các phân mảnh (fragments) được tái tổ hợp ở máy đích, bộ đệm bị tràn gây treo máy hoặc sập hệ thống.
- **스머핑 (SMURFING)**: Kẻ tấn công gửi gói tin ICMP Echo Request giả mạo IP nguồn là địa chỉ IP của nạn nhân đến địa chỉ Broadcast của một mạng trung gian. Toàn bộ máy tính trong mạng trung gian đồng loạt phản hồi về máy nạn nhân, gây nghẽn băng thông.
- **세션 하이재킹 (Session Hijacking)**: Kẻ tấn công đánh cắp hoặc đoán Session ID hợp lệ của người dùng đang kết nối để mạo danh phiên làm việc mà không cần biết mật khẩu.
- **Công cụ DDoS phân tán kinh điển**: Trin00, TFN (Tribe Flood Network), TFN2K, Stacheldraht.
- **DPI (Deep Packet Inspection)**: Kỹ thuật kiểm tra chuyên sâu toàn bộ nội dung phần Payload của gói tin (từ tầng 2 đến tầng 7) để phát hiện và ngăn chặn xâm nhập trái phép.

#### 3. Mã độc hệ thống và Tấn công chuyên biệt
- **웜 (Worm) vs 바이러스 (Virus)**:
  - **바이러스 (Virus)**: Bắt buộc phải bám vào một tệp tin ký chủ (host file) hợp lệ và chỉ lây lan khi tệp ký chủ được thực thi.
  - **웜 (Worm)**: Chương trình độc lập có khả năng tự sao chép và tự động lây truyền qua các lỗ hổng mạng mà không cần tệp tin ký chủ.
- **허니팟 (Honeypot)**: Hệ thống bẫy được thiết lập có chủ đích để dụ dỗ kẻ tấn công xâm nhập, qua đó thu thập thông tin về kỹ thuật tấn công và làm chệch hướng khỏi các máy chủ thật.
- **스위치 재밍 (Switch Jamming / MAC Flooding)**: Gửi hàng loạt gói tin với địa chỉ MAC nguồn giả mạo để làm tràn bộ nhớ bảng CAM (Content Addressable Memory) của thiết bị Switch, ép Switch rơi vào trạng thái Fail-open (hoạt động như một Dummy Hub) để nghe lén (Sniffing).
- **Bộ tấn công không dây Bluetooth**:
  - **BlueJacking**: Gửi tin nhắn hoặc danh thiếp nặc danh không mong muốn (spam) tới thiết bị bật Bluetooth.
  - **BlueSnarf**: Khai thác lỗ hổng xác thực để đánh cắp tệp tin, danh bạ, tin nhắn từ thiết bị mục tiêu.
  - **BlueBug**: Tấn công chiếm quyền kiểm soát hoàn toàn lệnh AT của điện thoại, tự động gọi điện hoặc nghe lén.
  - **BluePrinting**: Quét tìm thông tin về nhà sản xuất, model thiết bị và phiên bản firmware Bluetooth nhằm chuẩn bị cho đợt tấn công tiếp theo.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ cơ chế tấn công SMURFING
```
[Attacker] ───(Gửi ICMP Request với IP nguồn giả = Victim IP)───► [Mạng khuếch đại (Broadcast)]
                                                                           │
                                          ┌────────────────────────────────┼────────────────────────────────┐
                                          ▼                                ▼                                ▼
                                     [Host A]                          [Host B]                          [Host C]
                                          │                                │                                │
                                          └─────────────────┬──────────────┴────────────────────────────────┘
                                                            ▼ (Hàng nghìn phản hồi ICMP Reply dội về cùng lúc)
                                                    [Victim Server] (Bị tê liệt do cạn kiệt tài nguyên)
```

#### 2. Bảng đối chiếu các hình thức tấn công Bluetooth
| Thuật ngữ | Hành động của Hacker | Mức độ nguy hại | Mẹo ghi nhớ dễ thuộc |
| :--- | :--- | :--- | :--- |
| **BlueJacking** | Gửi tin nhắn spam, quảng cáo phiền phức | Thấp | **Jacking** = **Junk message** (tin rác) |
| **BlueSnarf** | Trích xuất trộm danh bạ, tin nhắn, hình ảnh | Trung bình | **Snarf** = **Snatch files** (chộp lấy file) |
| **BlueBug** | Kiểm soát cuộc gọi, nghe lén micro, can thiệp lệnh AT | Rất cao | **Bug** = **Cài bọ nghe lén / chiếm quyền** |
| **BluePrinting** | Quét dò thông tin cấu hình phần cứng thiết bị | Do thám | **Printing** = **Lấy dấu vân tay / bản thiết kế** |

---

### 복습 체크리스트
- [ ] Sự khác biệt then chốt giữa Virus và Worm trong cơ chế lây lan là gì?
- [ ] Tấn công SMURFING lợi dụng thành phần nào của giao thức IP/ICMP để khuếch đại lưu lượng?
- [ ] Switch Jamming làm thế nào để biến Switch thông minh thành một thiết bị Dummy Hub?
- [ ] Phân biệt rõ chức năng và hậu quả của 3 hình thức tấn công Bluetooth: BlueJacking, BlueSnarf, BlueBug.
