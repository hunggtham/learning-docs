# 소프트웨어 비용 산정 기법 (Software Cost Estimation)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống phân loại các phương pháp ước tính chi phí phần mềm: Phương pháp tiếp cận từ trên xuống (**하향식 - Top-Down**) và Phương pháp tiếp cận từ dưới lên (**상향식 - Bottom-Up**).
- Phân biệt sự khác nhau giữa Phương pháp chuyên gia phán đoán (전문가 감정 기법) và Kỹ thuật Delphi (델파이 기법 - chuyên gia ẩn danh qua nhiều vòng để đạt đồng thuận).
- Thấu hiểu và thuộc lòng 3 mô hình ước tính toán học kinh điển thuộc nhóm Bottom-Up: **COCOMO** (Boehm), **Putnam** (Rayleigh-Norden curve), và **Điểm chức năng FP** (Function Point - Albrecht).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 비용 산정 (Software Cost Estimation)
- 하향식 산정 (Top-Down: 전문가 감정, 델파이 기법)
- 상향식 산정 (Bottom-Up: LOC, 수학적 산정 기법)
- COCOMO 모형 (Organic, Semi-Detached, Embedded)
- Putnam 모형 (Rayleigh-Norden 곡선, SLIM)
- 기능 점수 모형 (Function Point - Albrecht, IOQFI)
- 델파이 기법 (Delphi Technique - 익명성, 편견 배제)

## 선행·연결 개념 (Kiến thức liên kết)
- [07-bai-hoc.md](07-bai-hoc.md): Quản lý tiến độ dự án bằng PERT/CPM và đường găng Critical Path.
- [09-bai-hoc.md](09-bai-hoc.md): Chuyên sâu về 3 mô hình toán học COCOMO, Putnam và Function Point.
- [10-bai-hoc.md](10-bai-hoc.md): Các tiêu chuẩn chất lượng quy trình phần mềm (ISO 12207, CMMI, SPICE).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh hai trường phái tiếp cận trong đề thi:
  - **하향식 (Top-Down - Từ trên xuống):** Không chia nhỏ dòng code mà ước tính tổng thể dựa trên kinh nghiệm:
    - *전문가 감정:* Mời 1-2 chuyên gia đầu ngành ước lượng nhanh $\rightarrow$ Dễ bị thiên kiến chủ quan.
    - *델파이 (Delphi):* Mời một hội đồng chuyên gia ước lượng **ẩn danh (익명성)** qua nhiều vòng thẩm định trung gian cho tới khi đạt được sự đồng thuận thống nhất.
  - **상향식 (Bottom-Up - Từ dưới lên):** Chia nhỏ phần mềm thành từng hàm, đếm dòng code LOC hoặc điểm chức năng FP rồi dùng công thức toán học cộng dồn lên.
  - **Khẩu quyết 5 yếu tố của FP:** **I.O.Q.F.I** (Input, Output, inQuiry, File, Interface).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các phương pháp ước tính chi phí phần mềm:**

| Nhóm tiếp cận | Tên phương pháp kỹ thuật | Cơ chế vận hành & Đặc điểm nhận diện thi cử |
| :--- | :--- | :--- |
| **하향식** (Top-Down / Từ trên xuống) | **전문가 감정 기법** (Expert Judgment) | Dự toán dựa trên kinh nghiệm thực tế của chuyên gia; nhanh chóng nhưng mang nặng tính chủ quan, dễ sai lệch nếu chuyên gia chưa từng làm dự án tương tự. |
| **하향식** (Top-Down / Từ trên xuống) | **델파이 기법** (Delphi Technique) | Loại bỏ định kiến chủ quan bằng cách gửi phiếu khảo sát dự toán **hoàn toàn ẩn danh (익명성)** tới nhiều chuyên gia; tổng hợp kết quả và cho khảo sát lại qua nhiều vòng cho đến khi hội tụ về con số thống nhất. |
| **상향식** (Bottom-Up / Từ dưới lên) | **LOC 기법** (Lines of Code) | Phân rã hệ thống thành các module nhỏ, dự toán số dòng code chi tiết và quy đổi ra công số nỗ lực Man-Month. |
| **상향식** (Bottom-Up / Từ dưới lên) | **수학적 산정 모형** (Mathematical Models) | Sử dụng các công thức thống kê hồi quy từ các dự án lịch sử lớn (COCOMO, Putnam, Function Point). |

- **2. Bảng tổng hợp 3 mô hình ước tính toán học kinh điển:**

| Mô hình toán học | Tác giả đề xuất | Tham số đầu vào cốt lõi | Đặc điểm kỹ thuật then chốt |
| :--- | :--- | :--- | :--- |
| **COCOMO** | **Barry Boehm** | Dòng mã nguồn (LOC / KDSI) | Chia thành 3 quy mô rõ rệt: **Organic** (`≤ 50 KDSI`), **Semi-Detached** (`> 50 ~ 300 KDSI`), và **Embedded** (`> 300 KDSI`). Có 3 mức độ chi tiết: Basic, Intermediate, Detailed. |
| **Putnam** | **Larry Putnam** | Vòng đời và nỗ lực theo thời gian | Ứng dụng đường cong phân phối nhân lực **Rayleigh-Norden**; công cụ phần mềm tự động hóa đại diện là **SLIM**. |
| **기능 점수 (FP)** | **Allan Albrecht** | Yêu cầu chức năng người dùng (5 yếu tố IOQFI) | Đo lường độ lớn phần mềm độc lập hoàn toàn với ngôn ngữ lập trình (Java hay C đều có cùng điểm FP nếu cùng tính năng); tính toán dựa trên độ phức tạp dữ liệu và giao tiếp. |

- **3. 5 thành phần cấu thành Điểm chức năng (FP - Function Point):**
  1. **자료 입력 (Data Input / ILF):** Màn hình nhập dữ liệu người dùng.
  2. **정보 출력 (Information Output / EIF):** Báo cáo kết xuất, đồ thị hiển thị.
  3. **사용자 질의 (User Inquiry):** Chức năng tra cứu thông tin tức thời.
  4. **내부 논리 파일 (Internal Logical Files):** Các bảng cơ sở dữ liệu nội bộ hệ thống quản lý.
  5. **외부 인터페이스 파일 (External Interface Files):** Các tệp dữ liệu chia sẻ hoặc API giao tiếp với hệ thống bên ngoài.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **3 cấp độ chi tiết của mô hình COCOMO (Boehm):**
  1. *Basic COCOMO (기본형):* Chỉ dựa vào số dòng lệnh LOC để tính nỗ lực sơ bộ.
  2. *Intermediate COCOMO (중간형):* Bổ sung thêm 15 hệ số chi phí (Cost Drivers) thuộc 4 nhóm: Sản phẩm, Phần cứng, Con người, Dự án.
  3. *Detailed COCOMO (발전형):* Tính toán chi tiết đến từng phân hệ và từng giai đoạn trong chu trình phát triển phần mềm.

### 복습 체크리스트
- [ ] Phân biệt được: Kỹ thuật Delphi thuộc nhóm Top-Down và có đặc điểm cốt lõi là ẩn danh (익명성).
- [ ] Nhớ tác giả của các mô hình: COCOMO do Boehm, FP do Albrecht, Putnam gắn với Rayleigh-Norden.
- [ ] Ghi nhớ 3 phân cấp của COCOMO: Organic (`≤ 50 KDSI`), Semi-Detached (`> 50 ~ 300 KDSI`), Embedded (`> 300 KDSI`).
- [ ] Thuộc 5 yếu tố đo lường của Function Point theo khẩu quyết: **I-O-Q-F-I**.
