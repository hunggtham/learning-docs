# 3. 다중화 및 전송 제어 (Đa hợp & Điều khiển truyền)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế vận hành và lợi ích kinh tế của kỹ thuật đa hợp ghép kênh (**다중화 - Multiplexing**) trong việc tối ưu hóa hiệu suất đường truyền viễn thông.
- Phân biệt sự khác nhau mang tính bản chất giữa Ghép kênh phân chia theo tần số (**FDM - Frequency Division Multiplexing**) cần dải bảo vệ (Guard Band) và Ghép kênh phân chia theo thời gian (**TDM - Time Division Multiplexing**).
- So sánh chi tiết hai biến thể của TDM: Ghép kênh đồng bộ (**STDM - Synchronous TDM**) với các khe thời gian cố định và Ghép kênh thống kê/bất đồng bộ (**ATDM - Asynchronous / Statistical TDM**) với cơ chế cấp phát động khe thời gian.

## 핵심 키워드 (Từ khóa)
- 다중화기 (Multiplexer - MUX)
- FDM (Frequency Division Multiplexing - 주파수 분할, 아날로그)
- 보호 대역 (Guard Band - 신호 간섭 방지, 대역폭 낭비)
- TDM (Time Division Multiplexing - 시분할, 디지털)
- STDM (동기식 시분할 - 고정 슬롯 할당, 비효율)
- ATDM / 통계적 시분할 (Statistical TDM - 동적 슬롯 할당, 고효율)
- WDM (Wavelength Division Multiplexing - 광섬유 파장 분할)

## 선행·연결 개념 (Kiến thức liên kết)
- [13-bai-hoc.md](13-bai-hoc.md): Phương thức truyền dữ liệu và các kỹ thuật điều chế số.
- [15-bai-hoc.md](15-bai-hoc.md): Kiểm soát lỗi FEC/ARQ và các phương thức chuyển mạch mạng.
- [18-bai-hoc.md](18-bai-hoc.md): Công nghệ mạng và hạ tầng viễn thông mới (SDN, NFV).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong các câu hỏi trắc nghiệm của đề thi:
  - Khi hỏi: "Kỹ thuật chia đường truyền thành nhiều kênh có tần số khác nhau và **bắt buộc phải có dải bảo vệ (Guard Band / 보호 대역)** để tránh chồng chéo tín hiệu là gì?" $\rightarrow$ Chọn ngay **FDM (주파수 분할 다중화)**.
  - Phân biệt giữa STDM và ATDM:
    - **STDM (Đồng bộ):** Cấp khe thời gian **CỐ ĐỊNH** cho từng thiết bị; máy nào không có dữ liệu thì khe thời gian đó **bị bỏ trống lãng phí** $\rightarrow$ Hiệu suất đường truyền thấp.
    - **ATDM (Thống kê / Bất đồng bộ):** **CHỈ CẤP PHÁT KHE THỜI GIAN ĐỘNG** cho các thiết bị thực sự đang có dữ liệu cần gửi; loại bỏ hoàn toàn các khe rỗng $\rightarrow$ Hiệu suất sử dụng đường truyền đạt mức tối đa.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các công nghệ ghép kênh đa hợp (Multiplexing):**

| Loại ghép kênh | Ký hiệu & Nguyên lý kỹ thuật | Tín hiệu áp dụng | Đặc điểm kỹ thuật then chốt |
| :--- | :--- | :--- | :--- |
| **Phân chia tần số** | **FDM** (Frequency Division) | **Tín hiệu tương tự** (Analog) | Chia toàn bộ độ rộng băng thông thành nhiều dải tần con; **bắt buộc phải có dải đệm bảo vệ (보호 대역 - Guard Band)** giữa các kênh lân cận để chống giao thoa sóng, gây lãng phí một phần băng thông. |
| **Phân chia thời gian** | **TDM** (Time Division) | **Tín hiệu số** (Digital) | Chia sẻ toàn bộ băng thông đường truyền bằng cách chia nhỏ dòng thời gian thành các **khe thời gian (시간 슬롯 - Time Slots)** luân phiên cực ngắn cho từng kênh. |
| **Phân chia bước sóng** | **WDM** (Wavelength Division) | **Tín hiệu quang** (Light/Optical) | Ứng dụng trên sợi cáp quang (Optical Fiber); truyền đồng thời nhiều chùm tia sáng có bước sóng ($\lambda$) khác nhau trên cùng một sợi quang; băng thông cực đại (hàng Tbps). |

- **2. Bảng phân biệt sâu sắc: STDM vs ATDM:**

| Tiêu chuẩn so sánh | 동기식 시분할 (STDM - Synchronous TDM) | 비동기식/통계적 시분할 (ATDM - Statistical TDM) |
| :--- | :--- | :--- |
| **Cơ chế cấp phát khe thời gian** | **Cố định theo chu kỳ** cho từng thiết bị đầu cuối, bất kể thiết bị đó có đang gửi dữ liệu hay không. | **Cấp phát động (Dynamic Allocation)**; chỉ những thiết bị đang có dữ liệu thực tế mới được cấp khe. |
| **Xử lý khi thiết bị rảnh rỗi** | Khe thời gian vẫn được phát ra dưới dạng **khe rỗng (Idle Slot / Không có dữ liệu)**, gây lãng phí. | Không lãng phí khe; nhường toàn bộ năng lực đường truyền cho các thiết bị đang bận gửi dữ liệu. |
| **Cấu trúc khung dữ liệu** | Không cần thông tin địa chỉ đích; vị trí khe tương ứng ngầm định với số hiệu kênh. | **Bắt buộc phải gắn kèm thông tin địa chỉ (Address)** của thiết bị vào đầu mỗi khe thời gian để nơi nhận biết dữ liệu của ai. |
| **Hiệu suất đường truyền** | Hiệu suất thấp đến trung bình. | **Hiệu suất đường truyền rất cao** (Thường gấp 2 đến 4 lần so với STDM). |
| **Chi phí thiết bị** | Cấu trúc mạch đơn giản, giá thành thấp. | Cần bộ đệm nhớ tạm (Buffer) và mạch điều khiển phức tạp, giá thành đắt hơn. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kỹ thuật Đa truy nhập phân chia theo mã (CDMA - Code Division Multiple Access):**
  - Khác với FDM (chia tần số) và TDM (chia thời gian), CDMA cho phép tất cả người dùng truyền dữ liệu đồng thời trên cùng một dải tần số duy nhất tại cùng một thời điểm. Mỗi người dùng được gán một mã giả ngẫu nhiên trực giao (Orthogonal PN Code) độc nhất, bên nhận dùng mã này để tách riêng tín hiệu mong muốn ra khỏi tập hợp tín hiệu nhiễu chung.

### 복습 체크리스트
- [ ] Ghi nhớ FDM dùng cho tín hiệu Analog và bắt buộc phải có Guard Band (보호 대역).
- [ ] Nhớ TDM dùng cho tín hiệu Digital thông qua chia nhỏ các khe thời gian (Time Slots).
- [ ] Phân biệt được: STDM cấp khe cố định gây lãng phí khe rỗng, ATDM cấp khe động cho thiết bị có dữ liệu.
- [ ] Nhớ ATDM bắt buộc phải gắn thêm địa chỉ vào khe thời gian để nhận diện luồng dữ liệu.
