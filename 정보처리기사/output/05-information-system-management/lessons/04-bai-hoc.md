# 5과목 추가: 소프트웨어 재사용, 산정 기법, 프레임워크

## 학습 목표 (Mục tiêu)
- Tổng hợp toàn diện mối liên kết kiến trúc giữa việc tái sử dụng phần mềm (소프트웨어 재사용), các mô hình toán học ước tính chi phí và công số dự án (소프트웨어 산정 기법), và khung phát triển ứng dụng (프레임워크).
- Phân biệt hai phương pháp tái sử dụng cốt lõi: Tái sử dụng tổng hợp lắp ghép khối (**합성 중심 - Composition-based / CBD**) và Tái sử dụng phát sinh tự động (**생성 중심 - Generation-based**).
- Nắm vững công thức quy đổi nỗ lực nhân tháng (Man-Month / MM) theo dòng mã nguồn LOC và các phân loại quy mô COCOMO kinh điển (`≤ 50 KDSI`, `> 50 ~ 300 KDSI`, `> 300 KDSI`).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 재사용 (Software Reuse)
- 합성 중심 (Composition / Block Building) vs 생성 중심 (Generation)
- 비용 산정 기법 (Cost Estimation Models)
- LOC (Lines of Code) & Man-Month (인월 계산)
- COCOMO 모형 (Organic, Semi-Detached, Embedded)
- 제어의 역전 (Inversion of Control - IoC)
- CBD (Component-Based Development)

## 선행·연결 개념 (Kiến thức liên kết)
- [03-bai-hoc.md](03-bai-hoc.md): Đặc tính của Framework và công nghệ ảo hóa SDE.
- [05-bai-hoc.md](05-bai-hoc.md): Chuyên sâu về Framework phát triển phần mềm và các bẫy phân biệt.
- [06-bai-hoc.md](06-bai-hoc.md): Quản lý dự án phần mềm và công thức tính LOC/Man-Month.

## 읽는 방법 (Cách đọc)
- Bản đồ kết nối kiến thức ôn thi:
  - Về **Tái sử dụng (Reuse):**
    - **합성 중심 (Composition):** Lấy các linh kiện/component có sẵn ghép lại thành phần mềm mới (kiểu Lego).
    - **생성 중심 (Generation):** Dựa vào mô tả trừu tượng và mẫu (Template) để phần mềm tự động sinh ra mã nguồn mới.
  - Về **COCOMO (Boehm):** Nhớ ranh giới phân loại không chồng lấn:
    - **조직형 (Organic):** Dưới hoặc bằng 50.000 dòng lệnh (`≤ 50 KDSI`).
    - **반분리형 (Semi-Detached):** Từ trên 50 đến 300.000 dòng (`> 50 ~ 300 KDSI`).
    - **내장형 (Embedded):** Trên 300.000 dòng lệnh (`> 300 KDSI`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 2 trường phái tái sử dụng phần mềm:**

| Trường phái tái sử dụng | Bản chất kỹ thuật & Phương thức hoạt động | Ví dụ thực tiễn |
| :--- | :--- | :--- |
| **합성 중심** (Composition-based / Khối ghép) | Lắp ráp, liên kết các khối thành phần (Component) đã được đóng gói sẵn và kiểm thử độc lập từ trước thông qua các giao diện chuẩn (Interface). | Phát triển dựa trên thành phần (**CBD**), ghép module giỏ hàng và module cổng thanh toán. |
| **생성 중심** (Generation-based / Phát sinh) | Sử dụng công cụ tự động hóa nhận diện tham số và mô hình thiết kế trừu tượng để **tự động sinh ra mã nguồn mới hoàn chỉnh**. | Công cụ sinh mã từ sơ đồ UML, các trình biên dịch mẫu Code Generator, ORM reverse engineering. |

- **2. Bảng tổng hợp các mô hình ước tính chi phí dự án phần mềm:**

| Mô hình ước tính | Cơ sở dữ liệu tính toán | Công thức / Đặc điểm thi cử |
| :--- | :--- | :--- |
| **LOC 기법** (Lines of Code) | Đếm tổng số dòng mã nguồn dự kiến (dựa trên giá trị Lạc quan, Bi quan, Kỳ vọng). | $\text{Nỗ lực (Man-Month)} = \frac{\text{Tổng LOC}}{\text{Năng suất 1 người/tháng}} = \text{Thời gian} \times \text{Nhân lực}$. |
| **COCOMO** (Boehm) | Phân loại quy mô dự án theo độ phức tạp và kích cỡ mã nguồn (KDSI). | 3 loại hình: **Organic** (`≤ 50 KDSI`), **Semi-Detached** (`> 50 ~ 300 KDSI`), và **Embedded** (`> 300 KDSI`). |
| **Putnam** | Dự báo nỗ lực theo chu kỳ thời gian dựa trên đường cong **Rayleigh-Norden**. | Công cụ ước lượng tự động hóa đại diện là **SLIM**. |
| **FP** (Function Point - Albrecht) | Đo lường giá trị chức năng hệ thống cung cấp cho người dùng độc lập với ngôn ngữ. | Dựa trên 5 yếu tố đo lường: Dữ liệu nhập (Input), Dữ liệu xuất (Output), Truy vấn (Inquiry), Tệp nội bộ (Internal Files), và Giao tiếp ngoài (External Interfaces). |

- **3. Hạt nhân của Khung phát triển phần mềm (Framework):**
  - **IoC (Inversion of Control):** Điểm phân biệt bản chất giữa Framework và Library.
  - Tái sử dụng ở cấp độ kiến trúc toàn vẹn: Framework đóng gói toàn bộ quy trình vận hành luồng điều khiển, lập trình viên chỉ cần "cắm" các thành phần vào các điểm mở rộng (Extension Points / Hot Spots).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối quan hệ giữa CBD và Framework:**
  - Framework cung cấp môi trường Container và các quy tắc giao tiếp (Protocol/Contract).
  - Component là các đơn vị nghiệp vụ thực thi cắm vào Container đó. Nhờ có Framework chuẩn hóa môi trường, các Component từ nhiều nhà cung cấp khác nhau mới có thể tích hợp và trao đổi thông tin trơn tru mà không xảy ra xung đột kiến trúc.

### 복습 체크리스트
- [ ] Phân biệt được: 합성 중심 (Ghép component như Lego) vs 생성 중심 (Tự động sinh mã nguồn mới).
- [ ] Ghi nhớ chính xác 3 phân cấp quy mô của COCOMO: Organic (`≤ 50 KDSI`), Semi-Detached (`> 50 ~ 300 KDSI`), Embedded (`> 300 KDSI`).
- [ ] Nhớ mô hình Putnam gắn với đường cong Rayleigh-Norden và công cụ SLIM.
- [ ] Thuộc 5 yếu tố của Function Point (I-O-Q-F-I): Input, Output, Inquiry, File, Interface.
