# 데이터 통신 기초, 변조 및 전송 제어 (Cơ sở truyền thông dữ liệu, Baseband/Broadband, Điều chế tín hiệu & Đa hợp)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 yếu tố cơ bản của hệ thống truyền thông dữ liệu (Nguồn phát Source, Nơi nhận Sink, Môi trường Medium) và phân biệt 3 phương thức truyền: Đơn công (단방향 - Simplex), Bán song công (반이중 - Half-Duplex), Song công toàn phần (전이중 - Full-Duplex).
- Phân biệt sâu sắc giữa truyền dẫn Băng tần cơ sở (**베이스밴드 - Baseband**) và Băng thông rộng (**브로드밴드 - Broadband**).
- Làm chủ các kỹ thuật điều chế tín hiệu tương tự (**AM, FM, PM**) và kỹ thuật điều chế số (**ASK, FSK, PSK, QAM**) cùng 3 bước chuyển đổi tương tự sang số **PCM** (표본화 Sampling $\rightarrow$ 양자화 Quantization $\rightarrow$ 부호화 Encoding).
- Phân biệt kỹ thuật ghép kênh: **FDM** (phân chia tần số, cần dải bảo vệ Guard Band), **TDM** (đồng bộ vs thống kê), và **WDM** (phân chia bước sóng quang).
- Phân biệt cơ chế kiểm soát lỗi Sửa lỗi chuyển tiếp (**FEC - Mã Hamming**) và Yêu cầu phát lại tự động (**ARQ**), cùng hai phương thức chuyển mạch gói: **Datagram** và **Virtual Circuit**.

## 핵심 키워드 (Từ khóa song ngữ)
- 데이터 통신 3요소 (3 Elements — 정보원 Source, 수신원 Sink, 전송 매체 Medium)
- 전송 방식 (Transmission Modes — 단방향 Simplex, 반이중 Half-Duplex, 전이중 Full-Duplex)
- 베이스밴드 (Baseband — Tín hiệu số truyền trực tiếp không điều chế, 1 kênh, cự ly ngắn)
- 브로드밴드 (Broadband — Điều chế sóng mang tương tự tần số cao, đa kênh FDM, cự ly dài)
- 아날로그 변조 (Analog Modulation — AM biên độ, FM tần số chống nhiễu, PM pha)
- 디지털 변조 (Digital Modulation — ASK, FSK, PSK, QAM kết hợp biên độ và pha)
- PCM (Pulse Code Modulation — 표본화 Sampling $\ge 2 f_{max}$, 양자화 Quantization, 부호화 Encoding)
- FDM (Frequency Division Multiplexing — Tín hiệu tương tự, cần dải bảo vệ Guard Band)
- TDM (Time Division Multiplexing — Đồng bộ gán cứng khe thời gian vs Thống kê cấp động)
- WDM (Wavelength Division Multiplexing — Ghép kênh phân chia bước sóng cáp quang)
- FEC (Forward Error Correction — Tự sửa lỗi không cần kênh ngược, 해밍 코드 Hamming Code)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi hoàn thành các phương án phòng thủ an ninh và giải pháp tường lửa tại [10-giai-phap-va-thiet-bi-bao-mat-mang.md](10-giai-phap-va-thiet-bi-bao-mat-mang.md), người học cần hiểu sâu bản chất vật lý và tín hiệu của dữ liệu khi di chuyển qua dây cáp mạng viễn thông.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp toàn bộ nền tảng truyền dẫn cấp thấp: cơ chế Baseband vs Broadband, các phương pháp điều chế tương tự và kỹ thuật số, kỹ thuật ghép kênh tối ưu băng thông đường truyền và các giải thuật kiểm soát sửa lỗi dữ liệu.
- **Dùng đi đâu (Forward Handoff):** Các khối dữ liệu và khung truyền dẫn đồng bộ được tổ chức thành cấu trúc tầng chuẩn hóa trong Mô hình OSI 7 tầng và Họ giao thức TCP/IP tại [12-mang-may-tinh-va-giao-thuc-tcp-ip.md](12-mang-may-tinh-va-giao-thuc-tcp-ip.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Baseband vs Broadband:**
  - Nhắc đến **"디지털 신호를 변조하지 않고 직접 전송" (Truyền tín hiệu số trực tiếp không điều chế)** $\rightarrow$ Chọn **베이스밴드 (Baseband)** (Ethernet LAN).
  - Nhắc đến **"반송파에 변조하여 아날로그 신호로 전송, FDM 다중화" (Điều chế sóng mang tương tự, đa kênh)** $\rightarrow$ Chọn **브로드밴드 (Broadband)** (CATV, cáp quang).
- **Phương thức truyền:**
  - Nhắc đến **"Chỉ 1 chiều cố định, không thể phản hồi"** (Radio, TV) $\rightarrow$ Chọn **단방향 (Simplex)**.
  - Nhắc đến **"Truyền cả 2 chiều nhưng tại một thời điểm chỉ 1 bên truyền"** (Bộ đàm, CSMA/CD) $\rightarrow$ Chọn **반이중 (Half-Duplex)**.
  - Nhắc đến **"Truyền đồng thời cả 2 chiều tại cùng một thời điểm"** (Điện thoại, Full-duplex Switch) $\rightarrow$ Chọn **전이중 (Full-Duplex)**.
- **Điều chế tín hiệu:**
  - Điều chế tương tự chống nhiễu tốt nhất, dùng cho phát thanh chất lượng cao $\rightarrow$ **FM (주파수 변조)**.
  - Điều chế số kết hợp thay đổi cả **Biên độ (Amplitude) và Pha (Phase)** $\rightarrow$ Chọn ngay **QAM**.
  - Quy trình PCM: Nhớ đúng thứ tự 3 bước: **표본화 (Sampling) $\rightarrow$ 양자화 (Quantization) $\rightarrow$ 부호화 (Encoding)**.
  - Định lý Nyquist: Tần số lấy mẫu tối thiểu phải gấp **2 lần** tần số cực đại của tín hiệu ($f_s \ge 2 f_{max}$).
- **Ghép kênh (Multiplexing):**
  - Tín hiệu tương tự, cần **보호 대역 (Guard Band)** chống xuyên âm $\rightarrow$ **FDM**.
  - Tín hiệu số, chỉ cấp phát khe thời gian khi có dữ liệu truyền $\rightarrow$ **비동기식/통계적 TDM (Statistical TDM)**.
  - Ghép nhiều bước sóng ánh sáng trong cáp quang $\rightarrow$ **WDM**.
- **Sửa lỗi & Chuyển mạch:**
  - Tự phát hiện và tự sửa lỗi trực tiếp tại máy nhận mà **không cần truyền lại** $\rightarrow$ Chọn **FEC (해밍 코드 - Hamming Code)**.
  - Chuyển mạch gói không thiết lập đường truyền trước, mỗi gói tin tự tìm đường độc lập $\rightarrow$ **데이터그램 (Datagram)**.
  - Chuyển mạch gói có thiết lập đường truyền logic trước khi truyền $\rightarrow$ **가상 회선 (Virtual Circuit)**.

---

## 데이터 통신 기초, 변조 및 전송 제어

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tổng quan hệ thống truyền thông và Phân loại truyền dẫn
- **3 yếu tố cơ bản của hệ thống truyền thông:**
  1. **정보원 (Source - Nguồn phát):** Nơi sinh ra thông tin cần truyền (máy trạm, cảm biến, máy chủ).
  2. **수신원 (Sink - Nơi nhận):** Điểm cuối tiếp nhận và xử lý thông tin.
  3. **전송 매체 (Transmission Medium - Môi trường truyền dẫn):** Phương tiện vật lý kết nối giữa nguồn và nhận (cáp xoắn đôi, cáp đồng trục, cáp quang, sóng vô tuyến).
- **Phân loại theo hướng truyền:**

| Phương thức | Tên tiếng Hàn & Anh | Cơ chế hoạt động & Ví dụ thực tế |
| :--- | :--- | :--- |
| **Đơn công** | **단방향 (Simplex)** | Dữ liệu chỉ truyền theo một chiều cố định duy nhất; bên nhận không thể phản hồi ngược lại (Truyền hình vô tuyến TV, Đài phát thanh Radio). |
| **Bán song công** | **반이중 (Half-Duplex)** | Dữ liệu có thể truyền theo cả hai chiều nhưng không được đồng thời; tại một thời điểm chỉ có một bên được phát tín hiệu (Máy bộ đàm Walkie-Talkie, giao thức CSMA/CD). |
| **Song công toàn phần** | **전이중 (Full-Duplex)** | Dữ liệu có thể truyền và nhận đồng thời theo cả hai chiều tại cùng một thời điểm (Cuộc gọi thoại điện thoại, kết nối Full-duplex Switch mạng hiện đại). |

#### 2. Đối chiếu phương thức truyền Baseband vs Broadband

| Tiêu chí so sánh | Băng tần cơ sở (베이스밴드 - Baseband) | Băng thông rộng (브로드밴드 - Broadband) |
| :--- | :--- | :--- |
| **Bản chất tín hiệu** | Truyền trực tiếp chuỗi xung tín hiệu số nhị phân (`0` và `1`) mà **không qua điều chế tần số**. | Dùng kỹ thuật điều chế để đưa tín hiệu lên **sóng mang tương tự tần số cao (Analog Carrier)**. |
| **Khả năng ghép kênh** | Toàn bộ băng thông đường truyền chỉ dành cho **1 kênh tín hiệu duy nhất** tại một thời điểm. | Cho phép **ghép nhiều kênh tín hiệu độc lập (FDM)** truyền đồng thời trên cùng một đường dây cáp. |
| **Khoảng cách truyền** | Cự ly ngắn do tín hiệu xung số suy hao nhanh khi đi xa (phù hợp mạng cục bộ LAN nội bộ). | Cự ly truyền rất xa nhờ tần số sóng mang tương tự cao và bộ khuếch đại (phù hợp mạng đô thị WAN/MAN). |
| **Chi phí thiết bị** | Đơn giản, chi phí thấp, không cần modem điều chế phức tạp (cáp xoắn đôi Ethernet LAN). | Phải trang bị bộ giải điều chế (Modem) tại các đầu mối, chi phí hạ tầng cao hơn (truyền hình cáp CATV). |

#### 3. Kỹ thuật điều chế tín hiệu (Modulation)

##### A. Điều chế tín hiệu tương tự (Analog-to-Analog Modulation)
- **AM (Amplitude Modulation - Điều chế biên độ):** Biên độ của sóng mang thay đổi tỷ lệ thuận theo tín hiệu nguồn; tần số và pha giữ nguyên cố định; cấu tạo mạch đơn giản nhưng rất dễ bị nhiễu biên độ.
- **FM (Frequency Modulation - Điều chế tần số):** Tần số của sóng mang thay đổi theo tín hiệu nguồn; biên độ giữ nguyên cố định; khả năng chống tạp âm và nhiễu sóng vượt trội hoàn toàn so với AM, chất lượng âm thanh trung thực.
- **PM (Phase Modulation - Điều chế pha):** Góc pha của sóng mang thay đổi theo tín hiệu nguồn; thường dùng trong truyền dữ liệu số tốc độ cao.

##### B. Điều chế số sang tương tự (Digital-to-Analog Modulation)
- **ASK (Amplitude Shift Keying - Khóa dịch biên độ):** Biểu diễn bit 0 và 1 bằng hai mức biên độ sóng mang khác nhau; dễ bị ảnh hưởng bởi nhiễu đường truyền.
- **FSK (Frequency Shift Keying - Khóa dịch tần số):** Biểu diễn bit 0 và 1 bằng hai tần số sóng mang khác nhau; khả năng chống nhiễu tốt hơn ASK.
- **PSK (Phase Shift Keying - Khóa dịch pha):** Biểu diễn bit bằng các độ lệch góc pha khác nhau (ví dụ: lệch $180^\circ$ trong BPSK, lệch $90^\circ$ trong QPSK).
- **QAM (Quadrature Amplitude Modulation - Điều chế biên độ cầu phương):**
  - **핵심 원리:** Kết hợp đồng thời việc thay đổi cả **Biên độ (Amplitude)** và **Góc pha (Phase)** của sóng mang.
  - Cho phép mỗi trạng thái tín hiệu (Baud) mang được nhiều bit thông tin (ví dụ: 16-QAM mang 4 bit/baud, 64-QAM mang 6 bit/baud), tối ưu hóa tối đa dung lượng truyền tải dữ liệu.

##### C. Điều chế mã xung PCM (Analog-to-Digital Conversion)
Chuyển đổi tín hiệu âm thanh tương tự thành chuỗi bit số nhị phân qua 3 bước tuần tự:
1. **표본화 (Sampling - Lấy mẫu):** Trích xuất các giá trị biên độ rời rạc theo thời gian. Theo **Định lý lấy mẫu Nyquist**, tần số lấy mẫu tối thiểu phải gấp đôi tần số cao nhất của tín hiệu:
   $$f_s \ge 2 f_{max}$$
2. **양자화 (Quantization - Lượng tử hóa):** Làm tròn các giá trị biên độ mẫu liên tục thành các mức giá trị số nguyên rời rạc xác định; phát sinh sai số lượng tử hóa.
3. **부호화 (Encoding - Mã hóa):** Chuyển đổi các mức giá trị lượng tử hóa thành chuỗi các bit nhị phân `0` và `1`.

#### 4. Kỹ thuật ghép kênh đa hợp (Multiplexing)
Ghép nhiều kênh truyền tín hiệu tốc độ thấp vào chung một đường truyền vật lý tốc độ cao:
- **FDM (Frequency Division Multiplexing - Ghép kênh phân chia tần số):**
  - Chia toàn bộ dải băng thông tần số của đường truyền thành nhiều dải tần con độc lập; áp dụng cho **tín hiệu tương tự (Analog)**.
  - Bắt buộc phải bố trí các **Dải tần bảo vệ (보호 대역 - Guard Band)** giữa các kênh tín hiệu liền kề để ngăn chặn hiện tượng chồng lấn và nhiễu xuyên âm.
- **TDM (Time Division Multiplexing - Ghép kênh phân chia thời gian):**
  - Phân chia thời gian sử dụng đường truyền thành các **Khe thời gian (Time Slots)** ngắn nối tiếp nhau; áp dụng cho **tín hiệu số**.
  - **동기식 TDM (Synchronous TDM):** Mỗi kênh được gán cứng một khe thời gian cố định. Nếu kênh không có dữ liệu thì khe thời gian đó vẫn bị bỏ trống, gây lãng phí băng thông.
  - **비동기식 / 통계적 TDM (Asynchronous / Statistical TDM):** Khe thời gian chỉ được cấp phát động cho những kênh nào thực sự có dữ liệu cần gửi; tối ưu hóa tối đa dung lượng đường truyền.
- **WDM (Wavelength Division Multiplexing - Ghép kênh phân chia bước sóng):**
  - Kỹ thuật ghép kênh quang, truyền đồng thời nhiều chùm tia sáng có bước sóng ($\lambda$) khác nhau trên cùng một sợi cáp quang duy nhất.

#### 5. Kiểm soát lỗi và Phương thức chuyển mạch

| Cơ chế | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Điểm thi trọng tâm |
| :--- | :--- | :--- |
| **Sửa lỗi chuyển tiếp** | **FEC (Forward Error Correction)** | Bên gửi đính kèm các bit kiểm tra dư thừa. Bên nhận có khả năng **tự động phát hiện VÀ tự sửa lỗi trực tiếp** mà không cần yêu cầu truyền lại. Thuật toán đại diện tiêu biểu là **Mã Hamming (해밍 코드)**. |
| **Yêu cầu truyền lại tự động** | **ARQ (Automatic Repeat reQuest)** | Bên nhận phát hiện lỗi bằng các mã phát hiện (Parity bit, CRC) và gửi yêu cầu bên gửi truyền lại gói tin bị lỗi (Stop-and-Wait ARQ, Go-Back-N ARQ, Selective Repeat ARQ). |
| **Chuyển mạch kênh** | **회선 교환 (Circuit Switching)** | Thiết lập một đường kết nối vật lý cố định chuyên dụng giữa 2 điểm trước khi truyền dữ liệu. Không bị trễ truyền gói tin trong quá trình liên lạc; nhược điểm lãng phí tài nguyên nếu đường truyền rảnh rỗi (Mạng điện thoại thoại PSTN). |
| **Chuyển mạch gói** | **패킷 교환 (Packet Switching)** | Dữ liệu được chia thành các gói tin nhỏ (Packets). Gồm 2 dạng: **데이터그램 (Datagram)** định tuyến mỗi gói độc lập và đến đích không theo thứ tự; **가상 회선 (Virtual Circuit)** thiết lập đường dẫn logic cố định trước khi truyền, các gói đến đích đúng thứ tự tuần tự. |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Cơ chế phát hiện và sửa lỗi của Mã Hamming (Hamming Code)
- Mã Hamming là kỹ thuật kiểm soát lỗi FEC kinh điển được phát minh bởi Richard Hamming:
  - Cho phép **tự phát hiện và sửa được 1 bit lỗi** duy nhất, hoặc phát hiện được 2 bit lỗi đồng thời.
  - Vị trí các bit kiểm tra chẵn lẻ (Parity Bits) luôn được đặt tại các vị trí lũy thừa của 2 trong chuỗi bit ($1, 2, 4, 8, 16, \dots$).
  - Công thức xác định số lượng bit kiểm tra $p$ cần thiết cho thông điệp có $m$ bit dữ liệu:
    $$2^p \ge m + p + 1$$

---

### 복습 체크리스트
- [ ] Nhớ 3 yếu tố truyền thông: 정보원 (Nguồn phát), 수신원 (Nơi nhận), 전송 매체 (Môi trường truyền dẫn).
- [ ] Phân biệt Baseband (truyền tín hiệu số trực tiếp không điều chế, 1 kênh) vs Broadband (điều chế sóng mang tương tự, đa kênh FDM).
- [ ] Phân biệt 3 phương thức truyền: 단방향 (Simplex), 반이중 (Half-Duplex), 전이중 (Full-Duplex).
- [ ] Phân biệt điều chế tương tự: AM (biên độ), FM (tần số, chống nhiễu vượt trội), PM (pha).
- [ ] Nắm vững điều chế số: QAM kết hợp thay đổi cả Biên độ và Pha để tăng tốc độ truyền.
- [ ] Thuộc 3 bước PCM: 표본화 (Sampling $\ge 2 f_{max}$) $\rightarrow$ 양자화 (Quantization) $\rightarrow$ 부호화 (Encoding).
- [ ] Phân biệt ghép kênh: FDM (tần số, cần Guard Band), TDM (thời gian, đồng bộ vs thống kê), WDM (bước sóng quang).
- [ ] Khắc ghi cơ chế FEC: Tự sửa lỗi không cần gửi lại, đại diện là Mã Hamming.
- [ ] Phân biệt chuyển mạch gói: Datagram (độc lập, không theo thứ tự) vs Virtual Circuit (logic cố định, tuần tự đúng thứ tự).
