# 2. 대칭 키 vs 비대칭 키 & 서비스 공격 기법 (Mật mã & Các Kỹ thuật Tấn công Dịch vụ)

## 학습 목표 (Mục tiêu)
- Phân biệt toàn diện hai hệ mật mã: Khóa đối xứng (대칭키) và Khóa bất đối xứng (비대칭키) về tốc độ, cách quản lý khóa và công thức số lượng khóa ($n(n-1)/2$ vs $2n$).
- Nắm vững bản chất kỹ thuật của các hình thức tấn công dịch vụ kinh điển: Backdoor, Keylogger, Rootkit, Ransomware, Botnet Zombie PC.
- Phân biệt các hình thức lừa đảo phi kỹ thuật (Social Engineering): Phishing (Email), Smishing (SMS), Qshing (QR Code).
- Hiểu rõ cơ chế các cuộc tấn công mạng: Zero-Day Attack, Nghe lén (Sniffing), Giả mạo danh tính (Spoofing: IP, ARP), và Chiếm phiên (Session Hijacking).

## 핵심 키워드 (Từ khóa)
- **대칭키 vs 비대칭키**: Đối xứng (cùng 1 khóa, nhanh, DES/AES), Bất đối xứng (cặp Public/Private, chậm, an toàn phân phối khóa, RSA/ECC).
- **악성 도구 (Malware Tools)**: 백도어 (Backdoor), 키로거 (Keylogger), 루트킷 (Rootkit - tàng hình giữ quyền root), 랜섬웨어 (Ransomware).
- **사회공학 (Social Engineering)**: 피싱 (Phishing - Email), 스미싱 (Smishing - SMS), 큐싱 (Qshing - QR Code).
- **네트워크 공격 (Network Attacks)**: 제로데이 공격 (Zero-Day Attack), 스니핑 (Sniffing - nghe lén), 스푸핑 (Spoofing - giả mạo IP/MAC), 세션 하이재킹 (Session Hijacking).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [34-bai-hoc.md](34-bai-hoc.md) (Công nghệ mã hóa đối xứng và bất đối xứng).
- Liên kết với [35-bai-hoc.md](35-bai-hoc.md) (Công thức tính số lượng khóa).
- Liên kết với [27-bai-hoc.md](27-bai-hoc.md) (Các hình thức tấn công và đe dọa bảo mật).

## 읽는 방법 (Cách đọc)
- Phân biệt các thuật ngữ tấn công hay nhầm lẫn:
  - Giả mạo IP, địa chỉ MAC để lừa máy trạm $\rightarrow$ **Spoofing (스푸핑)**.
  - Lén lút bắt gói tin trên đường truyền mạng để đọc trộm dữ liệu $\rightarrow$ **Sniffing (스니핑)**.
  - Lừa đảo qua tin nhắn điện thoại SMS $\rightarrow$ **Smishing (스미싱)**; qua mã QR $\rightarrow$ **Qshing (큐싱)**.
  - Bộ công cụ che giấu sự xâm nhập và giữ quyền quản trị tối cao $\rightarrow$ **Rootkit (루트킷)**.
  - Tấn công ngay khi lỗ hổng vừa được phát hiện, chưa có bản vá $\rightarrow$ **Zero-Day Attack (제로데이)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh Mật mã Khóa đối xứng vs Khóa bất đối xứng
| Tiêu chí so sánh | Mật mã khóa đối xứng (대칭키) | Mật mã khóa bất đối xứng (비대칭키) |
| :--- | :--- | :--- |
| **Bản chất khóa** | Khóa mã hóa **giống hệt** khóa giải mã (Khóa bí mật) | Khóa mã hóa (**Public Key**) khác khóa giải mã (**Private Key**) |
| **Tốc độ xử lý** | **Rất nhanh**, tối ưu cho mã hóa khối lượng dữ liệu lớn | **Chậm**, chi phí tính toán toán học cao |
| **Công thức số khóa ($n$ người)** | $\frac{n(n-1)}{2}$ khóa bí mật | $2n$ khóa (mỗi người 1 Public và 1 Private) |
| **Phân phối khóa** | Khó khăn (phải tìm kênh an toàn tuyệt đối để chia sẻ khóa) | Rất dễ dàng (khóa Public Key có thể công bố rộng rãi) |
| **Thuật toán tiêu biểu** | **DES, 3DES, AES, SEED, ARIA** (Block); **RC4** (Stream) | **RSA** (thừa số nguyên tố), **ECC** (đường cong elip), Diffie-Hellman |

#### 2. Các hình thức Tấn công Dịch vụ và Mã độc Hệ thống
- **Backdoor (백도어 - Cửa sau)**: Lối vào bí mật được cài cắm nhằm vượt qua các quy trình kiểm tra xác thực an ninh thông thường, cho phép kẻ tấn công tái thâm nhập máy chủ bất cứ lúc nào.
- **Keylogger (키로거)**: Mã độc ghi lại toàn bộ các thao tác gõ phím của người dùng nhằm đánh cắp tài khoản, mật khẩu và thông tin thẻ tín dụng.
- **Rootkit (루트킷)**: Tập hợp các chương trình độc hại chuyên dụng được thiết kế nhằm **che giấu sự hiện diện của hacker** trong hệ thống (ẩn tệp tin, ẩn tiến trình, ẩn cổng mạng) và duy trì quyền quản trị cao nhất (Root/Administrator).
- **Zombie PC & Botnet**: Các máy tính cá nhân bị lây nhiễm mã độc Bot, chịu sự điều khiển từ xa của máy chủ chỉ huy (C&C Server - Command and Control) của hacker tạo thành mạng máy tính ma (Botnet) để đồng loạt phát động các đợt tấn công từ chối dịch vụ phân tán (DDoS).
- **Ransomware (랜섬웨어)**: Mã độc tự động mã hóa toàn bộ dữ liệu quan trọng của nạn nhân bằng thuật toán mã hóa mạnh và đòi tiền chuộc (Ransom) để cung cấp khóa giải mã.

#### 3. Tấn công Phi kỹ thuật (Social Engineering) và Mạng
| Hình thức tấn công | Phương thức thực hiện | Mục tiêu đánh cắp |
| :--- | :--- | :--- |
| **Phishing (피싱)** | Gửi **Email giả mạo** các tổ chức tài chính, ngân hàng, công ty uy tín | Đánh lừa nạn nhân đăng nhập vào trang web giả để cướp tài khoản |
| **Smishing (스미싱)** | Gửi **tin nhắn SMS** chứa đường link độc hại (ví dụ: thông báo trúng thưởng, thông báo giao hàng giả) | Lừa người dùng nhấn link tải mã độc APK về điện thoại |
| **Qshing (큐싱)** | Sử dụng **mã QR độc hại** dán đè lên mã QR thanh toán thật tại các nhà hàng, cửa hàng | Chuyển hướng người dùng tới trang web độc hại hoặc đánh cắp tiền |
| **Zero-Day Attack** | Tấn công khai thác lỗ hổng bảo mật trong khoảng thời gian **từ lúc lỗ hổng được phát hiện cho tới khi bản vá được phát hành** | Xâm nhập hệ thống mà các giải pháp diệt virus truyền thống chưa kịp cập nhật mẫu nhận diện |
| **Sniffing (스니핑)** | Bắt và phân tích thụ động các gói tin truyền qua mạng nội bộ | Đọc trộm thông tin bản rõ nhạy cảm (Mật khẩu truyền qua HTTP/FTP) |
| **Spoofing (스푸핑)** | Giả mạo địa chỉ IP nguồn (IP Spoofing) hoặc địa chỉ MAC (ARP Spoofing) | Đánh lừa hệ thống xác thực mạng hoặc chiếm quyền định tuyến |
| **Session Hijacking** | Đánh cắp hoặc dự đoán Session ID hợp lệ của người dùng đang đăng nhập | Chiếm đoạt phiên làm việc mà không cần biết mật khẩu của nạn nhân |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Mẹo ghi nhớ dễ thuộc cho kỳ thi
- **Spoof** = 속이다 (Fake / Lừa gạt danh tính).
- **Sniff** = 킁킁거리다 (Đánh hơi / Nghe lén trộm gói tin).
- **Phishing** = Password Fishing (Câu mật khẩu qua email).
- **Smishing** = **SMS** + Phishing (Lừa qua tin nhắn SMS).
- **Qshing** = **QR Code** + Phishing (Lừa qua mã QR).

---

### 복습 체크리스트
- [ ] Tính số lượng khóa cần thiết cho mạng 10 người dùng theo hệ mật đối xứng và hệ mật bất đối xứng?
- [ ] Bộ công cụ Rootkit có vai trò chính là gì đối với hacker sau khi đã xâm nhập thành công hệ thống?
- [ ] Phân biệt 3 hình thức lừa đảo phi kỹ thuật: Phishing, Smishing, và Qshing?
- [ ] Tấn công Zero-Day Attack là gì và tại sao các phần mềm diệt virus Signature-based lại bất lực trước dạng tấn công này?
