# 4. 오류 제어 및 교환 방식 (Kiểm soát lỗi & Chuyển mạch)

## 학습 목표 (Mục tiêu)
- Nắm vững các nguyên nhân vật lý gây lỗi đường truyền dữ liệu: Suy hao (감쇠), Méo trễ (지연 왜곡), Nhiễu xuyên âm (누화 잡음), và Nhiễu xung đột biến (**충격성 잡음 - Impulse Noise**, nguyên nhân chính gây lỗi trong truyền thông số).
- Phân biệt chi tiết sự khác nhau mang tính bản chất giữa Sửa lỗi chuyển tiếp (**FEC - Forward Error Correction**) tự sửa lỗi không cần kênh ngược (Mã Hamming) và Yêu cầu phát lại tự động (**ARQ / BEC**).
- So sánh các phương thức chuyển mạch mạng: Chuyển mạch kênh (**회선 교환 - Circuit Switching**) và Chuyển mạch gói (**패킷 교환 - Packet Switching: Mạch ảo Virtual Circuit vs Datagram**).

## 핵심 키워드 (Từ khóa)
- 전송 오류 요인 (충격성 잡음 - Impulse Noise, 감쇠, 누화)
- FEC (Forward Error Correction - 순방향 오류 수정, 해밍 코드, 역채널 불필요)
- BEC / ARQ (Automatic Repeat reQuest - 역방향 오류 제어)
- Stop-and-Wait ARQ vs Go-Back-N ARQ vs Selective Repeat ARQ
- 회선 교환 (Circuit Switching - 전용선, 점유형, 실시간 전화)
- 패킷 교환 (Packet Switching - 저장-전송 Store-and-Forward)
- 가상 회선 (Virtual Circuit - X.25) vs 데이터그램 (Datagram - IP)

## 선행·연결 개념 (Kiến thức liên kết)
- [14-bai-hoc.md](14-bai-hoc.md): Kỹ thuật đa hợp ghép kênh FDM và TDM.
- [16-bai-hoc.md](16-bai-hoc.md): Lỗi mã nguồn phần mềm và các nguy cơ lạm dụng API.
- [19-bai-hoc.md](19-bai-hoc.md): Các thiết bị mạng viễn thông (Repeater, Bridge, Switch, Router).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong các câu hỏi đề thi:
  - Khi hỏi: "Kỹ thuật kiểm soát lỗi nào gửi kèm các bit dư thừa để bên nhận **tự phát hiện và tự sửa lỗi trực tiếp mà KHÔNG CẦN KÊNH TRUYỀN NGƯỢC (역채널 불필요)**?" $\rightarrow$ Chọn ngay **FEC (순방향 오류 수정)**, ví dụ kinh điển là **Mã Hamming (해밍 코드)**.
  - Phân biệt 2 dạng chuyển mạch gói:
    - **가상 회선 (Virtual Circuit):** Thiết lập đường dẫn logic trước khi truyền, các gói tin **luôn đến đích đúng theo thứ tự ban đầu** (ví dụ giao thức X.25).
    - **데이터그램 (Datagram):** Mỗi gói tin được định tuyến hoàn toàn độc lập, có thể đi qua các tuyến đường khác nhau và **có thể đến đích sai thứ tự** (ví dụ giao thức IP của Internet).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Các nguyên nhân gây lỗi đường truyền dữ liệu:**

| Tác nhân gây lỗi | Tên tiếng Hàn & Anh | Bản chất vật lý & Đặc điểm thi cử |
| :--- | :--- | :--- |
| **Nhiễu xung** | **충격성 잡음** (Impulse Noise) | Phát sinh do sét đánh hoặc tia lửa điện áp đột biến; là **nguyên nhân hàng đầu gây lỗi bit (Burst Error) trong truyền thông số tốc độ cao**. |
| **Suy hao** | **감쇠** (Attenuation) | Tín hiệu bị yếu dần theo khoảng cách truyền; khắc phục bằng bộ khuếch đại (Amplifier) hoặc bộ tái sinh lặp (Repeater). |
| **Xuyên âm** | **누화 잡음** (Crosstalk Noise) | Từ trường của dây truyền lân cận cảm ứng sang dây bên cạnh (ví dụ nghe thấy tiếng người khác nói chèn vào đường dây điện thoại). |
| **Méo trễ** | **지연 왜곡** (Delay Distortion) | Các thành phần tần số khác nhau của cùng một tín hiệu di chuyển với vận tốc khác nhau trên dây dẫn, đến nơi nhận cọc cạch không đồng thời. |

- **2. Bảng đối chiếu cơ chế kiểm soát lỗi: FEC vs ARQ (BEC):**

| Tiêu chuẩn so sánh | 순방향 오류 수정 (FEC - Forward Error Correction) | 역방향 오류 제어 (ARQ - Automatic Repeat reQuest) |
| :--- | :--- | :--- |
| **Nguyên lý hoạt động** | Máy phát gán thêm các bit mã hóa sửa lỗi dư thừa (như **Hamming Code**, Reed-Solomon); bên nhận tự tính toán và **tự động sửa đúng bit lỗi tại chỗ**. | Máy thu phát hiện gói tin bị lỗi (qua kiểm tra CRC, Parity) và gửi tín hiệu **NAK (Negative ACK) yêu cầu máy phát gửi lại gói tin đó**. |
| **Nhu cầu kênh ngược** | **Hoàn toàn không cần kênh ngược (역채널 불필요)**; cực kỳ hữu ích cho truyền thông vệ tinh hoặc phát thanh 1 chiều. | **Bắt buộc phải có kênh truyền ngược 2 chiều** để bên nhận gửi tín hiệu phản hồi xác nhận ACK/NAK. |
| **Hiệu suất đường truyền** | Chi phí phụ trội (Overhead) bit dư thừa rất cao; làm giảm băng thông hữu ích. | Tận dụng băng thông tốt khi đường truyền sạch ít lỗi; chỉ tốn tài nguyên khi phải gửi lại nhiều. |

- **3. Bảng phân loại các kỹ thuật ARQ (Yêu cầu phát lại tự động):**
  - **Stop-and-Wait ARQ:** Phát 1 gói $\rightarrow$ Dừng lại chờ ACK $\rightarrow$ Nhận được ACK mới phát gói kế tiếp $\rightarrow$ Cấu trúc đơn giản nhất nhưng hiệu suất đường truyền cực thấp.
  - **Go-Back-N ARQ:** Sử dụng cửa sổ trượt (Sliding Window) phát liên tục $N$ gói. Nếu gói $k$ bị lỗi hoặc thất lạc $\rightarrow$ Máy phát buộc phải **gửi lại toàn bộ từ gói $k$ đến hết các gói sau đó**.
  - **Selective Repeat ARQ:** Máy thu có bộ đệm lưu trữ; khi gói $k$ bị lỗi $\rightarrow$ **Chỉ gửi lại duy nhất đúng gói tin $k$ bị hỏng**, các gói đúng khác vẫn được giữ lại $\rightarrow$ Hiệu suất cao nhất nhưng bộ nhớ đệm bên nhận phức tạp.

- **4. Bảng phân biệt: Chuyển mạch kênh vs Chuyển mạch gói:**

| Tiêu chí | 회선 교환 (Circuit Switching) | 패킷 교환 (Packet Switching) |
| :--- | :--- | :--- |
| **Thiết lập kết nối** | Bắt buộc phải **thiết lập một đường truyền vật lý chuyên dụng riêng** trước khi bắt đầu đàm thoại. | Không cần chiếm dụng kênh vật lý; dữ liệu được băm nhỏ thành các gói tin (Packets) độc lập. |
| **Chiếm dụng tài nguyên** | Kênh truyền bị chiếm giữ độc quyền trong suốt phiên làm việc, dù hai bên im lặng không nói gì thì kênh vẫn bị khóa. | Các gói tin từ nhiều người dùng khác nhau **chia sẻ chung đường truyền linh hoạt** (Ghép kênh thống kê). |
| **Độ trễ truyền dẫn** | Thời gian thiết lập kênh ban đầu lâu, nhưng khi đã kết nối thì **độ trễ truyền gần như bằng 0** (Real-time). | Có độ trễ tích lũy qua từng nút mạng (Store-and-Forward Delay) do router phải lưu tạm vào bộ đệm và tra bảng định tuyến. |
| **Ví dụ hệ thống** | Mạng điện thoại cố định truyền thống PSTN. | Mạng máy tính Internet (IP), Mạng di động 4G/5G, X.25, Frame Relay. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Công thức tính số bit chẵn lẻ kiểm tra lỗi của Mã Hamming (Hamming Code):**
  - Để mã hóa được $m$ bit dữ liệu và phát hiện/sửa lỗi 1 bit bằng $p$ bit kiểm tra chẵn lẻ (Parity bits), số bit $p$ phải thỏa mãn bất đẳng thức:
    $$2^p \ge m + p + 1$$
  - *Ví dụ:* Nếu cần truyền 4 bit dữ liệu ($m = 4$), ta cần tìm số $p$ nhỏ nhất sao cho $2^p \ge 4 + p + 1$. Với $p = 3$, ta có $2^3 = 8 \ge 4 + 3 + 1 = 8$ (Thỏa mãn). Vậy tổng độ dài gói tin mã hóa là $4 + 3 = 7$ bit (Mã Hamming (7, 4)).

### 복습 체크리스트
- [ ] Ghi nhớ Impulse Noise (충격성 잡음) là nguyên nhân gây lỗi chính trong truyền thông số.
- [ ] Nhớ FEC tự sửa lỗi không cần kênh ngược (dùng mã Hamming).
- [ ] Phân biệt được: Go-Back-N gửi lại từ gói lỗi trở đi, Selective Repeat chỉ gửi lại đúng gói lỗi.
- [ ] Phân biệt được: Mạch ảo (Virtual Circuit) đến đích đúng thứ tự, Datagram đến đích độc lập có thể sai thứ tự.
- [ ] Nhớ mạng điện thoại PSTN là chuyển mạch kênh (Circuit), Internet là chuyển mạch gói (Packet).
