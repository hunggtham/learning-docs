# 1. 데이터 통신 개요 (Tổng quan Truyền thông Dữ liệu)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cấu trúc thành phần và công thức bản chất của truyền thông dữ liệu (데이터 통신 = 데이터 전송 기술 + 데이터 처리 기술).
- Thuộc lòng 3 yếu tố cơ bản bắt buộc cấu thành một hệ thống truyền thông thông tin: Nguồn phát (**정보원 - Source**), Nơi nhận (**수신원 - Sink**), và Môi trường truyền dẫn (**전송 매체 - Transmission Medium**).
- Ghi nhớ các cột mốc lịch sử phát triển của các hệ thống truyền thông dữ liệu kinh điển: **SAGE** (hệ thống đầu tiên), **SABRE** (hệ thống thương mại đầu tiên), **ARPANET** (tiền thân Internet), và **ALOHA** (mạng không dây đầu tiên).

## 핵심 키워드 (Từ khóa)
- 데이터 통신 (Data Communication)
- 통신의 3요소 (정보원, 수신원, 전송 매체)
- 데이터 전송 기술 + 데이터 처리 기술
- SAGE (최초의 데이터 통신 시스템 - 군사 방공망)
- SABRE (최초의 상업용 데이터 통신 - 항공기 예약)
- ARPANET (인터넷의 효시 - 최초의 패킷 교환망)
- ALOHA (최초의 무선 패킷 통신망)

## 선행·연결 개념 (Kiến thức liên kết)
- [11-bai-hoc.md](11-bai-hoc.md): Tiêu chuẩn chất lượng quy trình phần mềm (ISO 12207, CMMI, SPICE).
- [13-bai-hoc.md](13-bai-hoc.md): Phương thức truyền dữ liệu (Đơn công, Bán song công, Song công toàn phần) và điều chế.
- [14-bai-hoc.md](14-bai-hoc.md): Kỹ thuật ghép kênh đa hợp (FDM, TDM, STDM, ATDM).

## 읽는 방법 (Cách đọc)
- Điểm mấu chốt khi giải câu hỏi lịch sử và khái niệm trong đề thi kỹ sư CNTT:
  - Khái niệm: Truyền thông dữ liệu là sự kết hợp giữa **Kỹ thuật truyền dẫn viễn thông (전송)** và **Kỹ thuật xử lý dữ liệu bằng máy tính (처리)**.
  - 3 yếu tố cơ bản: **Nguồn phát (정보원), Nơi nhận (수신원), Môi trường truyền (전송 매체)**.
  - Các hệ thống lịch sử trong đề thi:
    - Hỏi hệ thống truyền thông dữ liệu **đầu tiên trên thế giới**: Chọn **SAGE** (quân sự Mỹ).
    - Hỏi hệ thống truyền thông dữ liệu **thương mại đầu tiên**: Chọn **SABRE** (vé máy bay American Airlines).
    - Hỏi mạng truyền thông là **tiền thân (mẹ đẻ) của Internet**: Chọn **ARPANET** (mạng chuyển mạch gói đầu tiên).
    - Hỏi mạng gói **không dây đầu tiên**: Chọn **ALOHA** (Đại học Hawaii).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Cấu trúc cấu thành hệ thống truyền thông thông tin:**

$$\mathbf{\text{데이터 통신} = \text{데이터 전송 기술 (Viễn thông)} + \text{데이터 처리 기술 (Máy tính)}}$$

| 3 yếu tố cốt lõi của truyền thông | Tên tiếng Hàn & Anh | Vai trò chức năng trong hệ thống |
| :--- | :--- | :--- |
| **1. Nguồn phát** | **정보원** (Information Source / Transmitter) | Nơi sinh ra thông tin ban đầu (người nói, máy tính phát dữ liệu, cảm biến nhiệt độ). |
| **2. Nơi nhận** | **수신원** (Receiver / Sink) | Nơi tiếp nhận, giải mã và hiển thị thông tin cho đối tượng đích sử dụng. |
| **3. Môi trường truyền** | **전송 매체** (Transmission Medium) | Con đường vật lý kết nối giữa nguồn phát và nơi nhận. Gồm môi trường có định hướng (Cáp đồng xoắn đôi Twisted Pair, Cáp đồng trục Coaxial, Cáp sợi quang Optical Fiber) và môi trường không định hướng (Sóng vô tuyến Radio, Vi ba Microwave, Tia hồng ngoại). |

- **2. Bảng các hệ thống truyền thông dữ liệu mang tính bước ngoặt lịch sử:**

| Tên hệ thống | Thời gian | Đơn vị phát triển | Vị thế lịch sử & Đặc điểm thi cử |
| :--- | :---: | :--- | :--- |
| **SAGE** | 1958 | Không quân Mỹ & IBM | **Hệ thống truyền thông dữ liệu ĐẦU TIÊN trên thế giới**; hệ thống phòng không quân sự kết nối các trạm radar từ xa về máy tính trung tâm để cảnh báo sớm máy bay ném bom. |
| **SABRE** | 1960 | American Airlines & IBM | **Hệ thống truyền thông dữ liệu THƯƠNG MẠI ĐẦU TIÊN**; hệ thống đặt chỗ và bán vé máy bay theo thời gian thực kết nối hàng nghìn thiết bị đầu cuối trên toàn nước Mỹ. |
| **ARPANET** | 1969 | Bộ Quốc phòng Mỹ (DARPA) | **Mạng chuyển mạch gói (Packet Switching) đầu tiên** trên thế giới, là tiền thân trực tiếp của mạng Internet toàn cầu ngày nay; khai sinh giao thức TCP/IP. |
| **ALOHA** | 1970 | Đại học Hawaii | **Mạng truyền dữ liệu vô tuyến (không dây) đầu tiên**; đặt nền móng lý thuyết cho cơ chế tranh chấp đường truyền CSMA/CD và chuẩn mạng cục bộ Ethernet. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Đặc trưng của tín hiệu số (Digital Signal) so với tín hiệu tương tự (Analog Signal):**
  - Tín hiệu số chỉ mang hai mức điện áp rời rạc (0 và 1), có khả năng chống nhiễu (Noise Immunity) cực cao và dễ dàng tái sinh nguyên vẹn qua các bộ lặp (Repeater).
  - Tín hiệu tương tự biến thiên liên tục theo thời gian, dễ bị suy hao, méo dạng và lẫn tạp âm khi truyền khoảng cách xa qua các bộ khuếch đại (Amplifier).

### 복습 체크리스트
- [ ] Ghi nhớ công thức: Truyền thông dữ liệu = Kỹ thuật truyền dẫn + Kỹ thuật xử lý bằng máy tính.
- [ ] Kể tên 3 yếu tố cơ bản của truyền thông: Nguồn phát (정보원), Nơi nhận (수신원), Môi trường truyền (전송 매체).
- [ ] Nhớ SAGE là hệ thống truyền dữ liệu đầu tiên, SABRE là hệ thống thương mại đầu tiên.
- [ ] Nhớ ARPANET là mạng chuyển mạch gói đầu tiên và là cội nguồn của mạng Internet.
