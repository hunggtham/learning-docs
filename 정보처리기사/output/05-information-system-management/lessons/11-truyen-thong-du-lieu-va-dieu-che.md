# 데이터 통신 기초, 변조 및 전송 제어 (Cơ sở truyền thông dữ liệu, Điều chế tín hiệu, Đa hợp & Kiểm soát lỗi)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 yếu tố cơ bản của hệ thống truyền thông dữ liệu: Nguồn phát (**정보원 - Source**), Nơi nhận (**수신원 - Sink**), và Môi trường truyền dẫn (**전송 매체 - Medium**).
- Phân biệt các phương thức truyền dẫn theo hướng: Đơn công (**단방향 - Simplex**), Bán song công (**반이중 - Half-Duplex**), và Song công toàn phần (**전이중 - Full-Duplex**).
- So sánh sự khác nhau giữa truyền thông không đồng bộ (**비동기식 - Asynchronous** với Start/Stop bit) và truyền thông đồng bộ (**동기식 - Synchronous** với xung Clock và ký tự `SYN`).
- Làm chủ các kỹ thuật điều chế số: **ASK**, **FSK**, **PSK**, **QAM** và 3 bước chuyển đổi tương tự sang số **PCM** (표본화 Sampling $\rightarrow$ 양자화 Quantization $\rightarrow$ 부호화 Encoding).
- Phân biệt kỹ thuật ghép kênh: **FDM** (phân chia tần số, cần dải bảo vệ Guard Band) và **TDM** (đồng bộ vs bất đồng bộ/thống kê).
- Phân biệt cơ chế kiểm soát lỗi Sửa lỗi chuyển tiếp (**FEC - Mã Hamming**) và Yêu cầu phát lại tự động (**ARQ**), cùng hai phương thức chuyển mạch: **Chuyển mạch kênh (회선 교환)** và **Chuyển mạch gói (패킷 교환: Datagram vs Virtual Circuit)**.

## 핵심 키워드 (Từ khóa song ngữ)
- 데이터 통신 3요소 (3 Elements — 정보원 Source, 수신원 Sink, 전송 매체 Medium)
- 전송 방식 (Transmission Modes — 단방향 Simplex, 반이중 Half-Duplex, 전이중 Full-Duplex)
- 비동기식 전송 (Asynchronous — Start/Stop bit, khoảng nghỉ Idle ngẫu nhiên)
- 동기식 전송 (Synchronous — Khung Block/Frame, xung nhịp Clock, ký tự SYN)
- 변조 기법 (Modulation — ASK, FSK, PSK, QAM kết hợp biên độ và pha)
- PCM (Pulse Code Modulation — 표본화 Sampling $\ge 2 f_{max}$, 양자화 Quantization, 부호화 Encoding)
- FDM (Frequency Division Multiplexing — Tín hiệu tương tự, cần dải bảo vệ Guard Band)
- TDM (Time Division Multiplexing — Đồng bộ gán cứng khe thời gian vs Thống kê cấp động)
- FEC (Forward Error Correction — Tự sửa lỗi không cần kênh ngược, 해밍 코드 Hamming Code)
- 패킷 교환 (Packet Switching — 데이터그램 Datagram độc lập vs 가상회선 Virtual Circuit)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi hoàn thành các phương án phòng thủ an ninh và giải pháp tường lửa tại [10-giai-phap-va-thiet-bi-bao-mat-mang.md](10-giai-phap-va-thiet-bi-bao-mat-mang.md), người học cần hiểu sâu bản chất vật lý và tín hiệu của dữ liệu khi di chuyển qua dây cáp mạng viễn thông.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp toàn bộ nền tảng truyền dẫn cấp thấp: cơ chế đồng bộ bit, các phương pháp điều chế tín hiệu số, kỹ thuật ghép kênh tối ưu băng thông đường truyền và các giải thuật kiểm soát sửa lỗi dữ liệu.
- **Dùng đi đâu (Forward Handoff):** Các khối dữ liệu và khung truyền dẫn đồng bộ được tổ chức thành cấu trúc tầng chuẩn hóa trong Mô hình OSI 7 tầng và Họ giao thức TCP/IP tại [12-mang-may-tinh-va-giao-thuc-tcp-ip.md](12-mang-may-tinh-va-giao-thuc-tcp-ip.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Phương thức truyền:**
  - Nhắc đến **"Chỉ 1 chiều cố định, không thể phản hồi"** (Radio, TV) $\rightarrow$ Chọn **단방향 (Simplex)**.
  - Nhắc đến **"Truyền cả 2 chiều nhưng tại một thời điểm chỉ 1 bên truyền"** (Bộ đàm, CSMA/CD) $\rightarrow$ Chọn **반이중 (Half-Duplex)**.
  - Nhắc đến **"Truyền đồng thời cả 2 chiều tại cùng một thời điểm"** (Điện thoại, Full-duplex Switch) $\rightarrow$ Chọn **전이중 (Full-Duplex)**.
- **Đồng bộ hóa:**
  - Có **Start bit và Stop bit**, truyền từng ký tự một $\rightarrow$ **비동기식 (Asynchronous)**.
  - Truyền theo **khung Block/Frame**, dùng xung **Clock và ký tự `SYN`** $\rightarrow$ **동기식 (Synchronous)**.
- **Điều chế số (Modulation):**
  - Kết hợp thay đổi cả **Biên độ (Amplitude) và Pha (Phase)** để truyền nhiều bit trên một xung $\rightarrow$ Chọn ngay **QAM**.
  - Quy trình PCM: Nhớ đúng thứ tự 3 bước: **표본화 (Sampling) $\rightarrow$ 양자화 (Quantization) $\rightarrow$ 부호화 (Encoding)**.
  - Định lý Nyquist: Tần số lấy mẫu tối thiểu phải gấp **2 lần** tần số cực đại của tín hiệu ($f_s \ge 2 f_{max}$).
- **Ghép kênh (Multiplexing):**
  - Tín hiệu tương tự, cần **보호 대역 (Guard Band)** chống xuyên âm $\rightarrow$ **FDM**.
  - Tín hiệu số, chỉ cấp phát khe thời gian khi có dữ liệu truyền (tiết kiệm băng thông) $\rightarrow$ **비동기식/통계적 TDM (Statistical TDM)**.
- **Sửa lỗi & Chuyển mạch:**
  - Tự phát hiện và tự sửa lỗi trực tiếp tại máy nhận mà **không cần truyền lại** $\rightarrow$ Chọn **FEC (해밍 코드 - Hamming Code)**.
  - Chuyển mạch gói không thiết lập đường truyền trước, mỗi gói tin tự tìm đường độc lập $\rightarrow$ **데이터그램 (Datagram)**.
  - Chuyển mạch gói có thiết lập đường truyền logic trước khi truyền $\rightarrow$ **가상 회선 (Virtual Circuit)**.

---

## 데이터 통신 기초, 변조 및 전송 제어

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tổng quan hệ thống truyền thông dữ liệu
- **Bản chất truyền thông:** Truyền thông dữ liệu là sự kết hợp giữa **Kỹ thuật truyền dẫn dữ liệu (데이터 전송 기술)** và **Kỹ thuật xử lý máy tính (데이터 처리 기술)**.
- **3 yếu tố cơ bản:**
  1. **정보원 (Source - Nguồn phát):** Nơi sinh ra thông tin cần truyền (máy trạm, cảm biến, máy chủ).
  2. **수신원 (Sink - Nơi nhận):** Điểm cuối tiếp nhận và xử lý thông tin.
  3. **전송 매체 (Transmission Medium - Môi trường truyền dẫn):** Phương tiện vật lý kết nối giữa nguồn và nhận (cáp xoắn đôi, cáp đồng trục, cáp quang, sóng vô tuyến).

#### 2. Phân loại phương thức truyền dữ liệu

| Phương thức | Tên tiếng Hàn & Anh | Cơ chế hoạt động & Ví dụ thực tế |
| :--- | :--- | :--- |
| **Đơn công** | **단방향 (Simplex)** | Dữ liệu chỉ truyền theo **một chiều cố định duy nhất**; bên nhận không bao giờ có thể gửi phản hồi ngược lại.<br>*Ví dụ:* Truyền hình vô tuyến (TV), Đài phát thanh (Radio). |
| **Bán song công** | **반이중 (Half-Duplex)** | Dữ liệu có thể truyền theo cả hai chiều nhưng **KHÔNG ĐƯỢC ĐỒNG THỜI**; tại một thời điểm chỉ có một bên được phát tín hiệu, bên kia phải lắng nghe.<br>*Ví dụ:* Máy bộ đàm (Walkie-Talkie), cơ thức truy cập mạng LAN cổ điển **CSMA/CD**. |
| **Song công toàn phần** | **전이중 (Full-Duplex)** | Dữ liệu có thể truyền và nhận **đồng thời theo cả hai chiều tại cùng một thời điểm**.<br>*Ví dụ:* Cuộc gọi thoại điện thoại, kết nối chuyển mạch qua thiết bị Switch mạng hiện đại. |

- **So sánh truyền thông Không đồng bộ và Đồng bộ:**
  - **비동기식 전송 (Asynchronous):** Truyền từng ký tự một (7–8 bit); gắn thêm **Start bit (bit 0)** ở đầu và **Stop bit (bit 1)** ở đuôi; giữa các ký tự có khoảng thời gian nghỉ (Idle) ngẫu nhiên; không cần mạch xung nhịp Clock chung; hiệu suất thấp, phù hợp đường truyền tốc độ thấp.
  - **동기식 전송 (Synchronous):** Dữ liệu được đóng gói thành các khối lớn (**Block hoặc Frame**); sử dụng một tín hiệu xung nhịp chung (**Clock**) để bên gửi và bên nhận đồng bộ tuyệt đối về thời gian; đầu khung có các ký tự đồng bộ đặc biệt (`SYN` trong truyền hướng ký tự, cờ `01111110` trong HDLC); tốc độ cao, hiệu suất đường truyền tối đa.

#### 3. Kỹ thuật điều chế tín hiệu (Modulation)

##### A. Điều chế số sang tương tự (Digital-to-Analog)
Chuyển đổi dữ liệu nhị phân của máy tính thành sóng mang tương tự để truyền qua mạng viễn thông:
- **ASK (Amplitude Shift Keying - Điều chế biên độ):** Biểu diễn bit 0 và 1 bằng cách thay đổi biên độ của sóng mang; dễ bị nhiễu biên độ.
- **FSK (Frequency Shift Keying - Điều chế tần số):** Biểu diễn bit 0 và 1 bằng hai tần số sóng mang khác nhau; khả năng chống nhiễu tốt hơn ASK.
- **PSK (Phase Shift Keying - Điều chế pha):** Biểu diễn bit bằng cách làm lệch góc pha (Phase) của sóng mang (ví dụ: lệch $180^\circ$ cho 2 pha, lệch $90^\circ$ cho 4 pha QPSK).
- **QAM (Quadrature Amplitude Modulation - Điều chế biên độ cầu phương):**
  - **핵심 원리 (Nguyên tắc cốt lõi):** Kết hợp đồng thời việc thay đổi cả **Biên độ (Amplitude)** và **Góc pha (Phase)** của sóng mang.
  - Cho phép mỗi trạng thái tín hiệu (Baud) mang được nhiều bit thông tin (ví dụ: 16-QAM mang 4 bit/baud, 64-QAM mang 6 bit/baud), nâng tốc độ truyền dẫn dữ liệu lên mức rất cao.

##### B. Điều chế mã xung PCM (Analog-to-Digital)
Chuyển đổi tín hiệu âm thanh tương tự thành chuỗi bit số nhị phân qua 3 bước tuần tự:
1. **표본화 (Sampling - Lấy mẫu):** Trích xuất các giá trị biên độ rời rạc của tín hiệu theo từng chu kỳ thời gian nhất định. Theo **Định lý lấy mẫu Nyquist**, tần số lấy mẫu tối thiểu phải gấp đôi tần số cao nhất của tín hiệu ($f_s \ge 2 f_{max}$).
2. **양자화 (Quantization - Lượng tử hóa):** Làm tròn các giá trị biên độ mẫu liên tục thành các mức giá trị số nguyên rời rạc xác định.
3. **부호화 (Encoding - Mã hóa):** Chuyển đổi các mức giá trị lượng tử hóa thành chuỗi các bit nhị phân `0` và `1`.

#### 4. Kỹ thuật ghép kênh đa hợp (Multiplexing)
Ghép nhiều kênh truyền tín hiệu tốc độ thấp vào chung một đường truyền vật lý tốc độ cao:
- **FDM (Frequency Division Multiplexing - Ghép kênh phân chia tần số):**
  - Chia toàn bộ dải băng thông tần số của đường truyền thành nhiều dải tần con độc lập.
  - Áp dụng cho **tín hiệu tương tự (Analog)**.
  - Bắt buộc phải bố trí các **Dải tần bảo vệ (보호 대역 - Guard Band)** giữa các kênh tín hiệu liền kề để ngăn chặn hiện tượng chồng lấn và nhiễu xuyên âm.
- **TDM (Time Division Multiplexing - Ghép kênh phân chia thời gian):**
  - Chia sẻ toàn bộ dải tần nhưng phân chia thời gian sử dụng đường truyền thành các **Khe thời gian (Time Slots)** ngắn nối tiếp nhau; áp dụng cho **tín hiệu số**.
  - **동기식 TDM (Synchronous TDM):** Mỗi kênh đầu vào được gán cứng một khe thời gian cố định. Nếu kênh nào không có dữ liệu cần truyền thì khe thời gian đó vẫn bị bỏ trống, gây lãng phí dung lượng đường truyền.
  - **비동기식 / 통계적 TDM (Asynchronous / Statistical TDM):** Khe thời gian chỉ được cấp phát động cho những kênh nào thực sự đang có dữ liệu cần gửi; mỗi khe mang theo địa chỉ nhận diện; tối ưu hóa tối đa băng thông đường truyền.
- **WDM (Wavelength Division Multiplexing - Ghép kênh phân chia bước sóng):** Áp dụng trong truyền thông cáp quang, ghép nhiều chùm tia sáng có bước sóng khác nhau vào truyền trên cùng một sợi quang.

#### 5. Kiểm soát lỗi và Phương thức chuyển mạch

| Cơ chế | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Điểm thi trọng tâm |
| :--- | :--- | :--- |
| **Sửa lỗi chuyển tiếp** | **FEC (Forward Error Correction)** | Bên gửi đính kèm các bit kiểm tra dư thừa vào gói tin. Bên nhận có khả năng **tự động phát hiện VÀ tự sửa lỗi trực tiếp** trên dữ liệu nhận được mà **không cần kênh truyền phản hồi ngược lại và không cần yêu cầu truyền lại**. Thuật toán đại diện tiêu biểu là **Mã Hamming (해밍 코드)**. |
| **Yêu cầu truyền lại tự động** | **ARQ (Automatic Repeat reQuest)** | Bên nhận phát hiện lỗi bằng các mã phát hiện (Parity bit, CRC) và gửi yêu cầu bên gửi truyền lại gói tin bị lỗi (Stop-and-Wait ARQ, Go-Back-N ARQ, Selective Repeat ARQ). |
| **Chuyển mạch kênh** | **회선 교환 (Circuit Switching)** | Thiết lập một đường kết nối vật lý cố định chuyên dụng giữa 2 điểm trước khi truyền dữ liệu. Không bị trễ truyền gói tin trong quá trình liên lạc; nhưng lãng phí tài nguyên nếu đường truyền rảnh rỗi. *Ví dụ:* Mạng điện thoại PSTN. |
| **Chuyển mạch gói** | **패킷 교환 (Packet Switching)** | Dữ liệu được chia thành các gói tin nhỏ (Packets), mỗi gói tin có Header chứa thông tin điều khiển và địa chỉ đích.<br>- **데이터그램 (Datagram):** Mỗi gói tin được định tuyến độc lập, có thể đi theo các tuyến đường khác nhau và đến đích không theo thứ tự ban đầu (ví dụ: giao thức IP của Internet).<br>- **가상 회선 (Virtual Circuit):** Thiết lập một đường dẫn logic cố định trước khi truyền; các gói tin đi theo cùng một lộ trình và đến đích đúng thứ tự tuần tự. |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Cơ chế phát hiện và sửa lỗi của Mã Hamming (Hamming Code)
- Mã Hamming là kỹ thuật kiểm soát lỗi FEC kinh điển được phát minh bởi Richard Hamming:
  - Cho phép **tự phát hiện và sửa được 1 bit lỗi** duy nhất, hoặc phát hiện được 2 bit lỗi đồng thời (nhưng không sửa được 2 bit).
  - Vị trí các bit kiểm tra chẵn lẻ (Parity Bits) luôn được đặt tại các vị trí lũy thừa của 2 trong chuỗi bit ($1, 2, 4, 8, 16, \dots$).
  - Công thức xác định số lượng bit kiểm tra $p$ cần thiết cho thông điệp có $m$ bit dữ liệu:
    $$2^p \ge m + p + 1$$

---

### 복습 체크리스트
- [ ] Nhớ 3 yếu tố truyền thông: 정보원 (Nguồn phát), 수신원 (Nơi nhận), 전송 매체 (Môi trường truyền dẫn).
- [ ] Phân biệt 3 phương thức truyền: 단방향 (Simplex - 1 chiều cố định), 반이중 (Half-Duplex - 2 chiều không đồng thời), 전이중 (Full-Duplex - 2 chiều đồng thời).
- [ ] Phân biệt đồng bộ: 비동기식 (Start/Stop bit) vs 동기식 (Khung Block, xung Clock, ký tự SYN).
- [ ] Nắm vững điều chế: QAM kết hợp thay đổi cả Biên độ và Pha để tăng tốc độ truyền.
- [ ] Thuộc 3 bước PCM: 표본화 (Sampling $\ge 2 f_{max}$) $\rightarrow$ 양자화 (Quantization) $\rightarrow$ 부호화 (Encoding).
- [ ] Phân biệt ghép kênh: FDM (tần số, cần Guard Band) vs TDM (thời gian, khe thời gian).
- [ ] Khắc ghi cơ chế FEC: Tự sửa lỗi không cần gửi lại, đại diện là Mã Hamming.
- [ ] Phân biệt chuyển mạch gói: Datagram (độc lập, không theo thứ tự) vs Virtual Circuit (logic cố định, tuần tự đúng thứ tự).
