# 204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và mục tiêu của phân tích hướng đối tượng (객체지향 분석 - Object-Oriented Analysis / OOA): Trích xuất thực thể, thuộc tính, phương thức và mối quan hệ từ yêu cầu người dùng.
- Nhận diện các phương pháp luận phân tích hướng đối tượng tiêu biểu: Booch, Jacobson (Use Case), Coad/Yourdon (E-R Diagram), và Wirfs-Brock.
- Thuộc lòng thứ tự 3 mô hình phân tích kinh điển trong phương pháp OMT của Rumbaugh (럼바우 기법) theo khẩu quyết **객동기** và loại biểu đồ đặc trưng tương ứng với từng mô hình.

## 핵심 키워드 (Từ khóa)
- 객체지향 분석 (Object-Oriented Analysis - OOA)
- 럼바우 분석 기법 (Rumbaugh OMT Method)
- 객체 모델링 (Object Modeling - 객체 다이어그램)
- 동적 모델링 (Dynamic Modeling - 상태 다이어그램)
- 기능 모델링 (Functional Modeling - 자료 흐름도 DFD)
- 암기 공식 (객동기)
- Booch (미시적/거시적) & Jacobson (Use Case)

## 선행·연결 개념 (Kiến thức liên kết)
- [63-bai-hoc.md](63-bai-hoc.md): Xử lý mã nguồn ngoài hành tinh (Alien Code).
- [65-bai-hoc.md](65-bai-hoc.md): Thiết kế và lập trình hướng đối tượng (OOD & OOP).
- [66-bai-hoc.md](66-bai-hoc.md): Tái sử dụng phần mềm và kiến trúc hướng thành phần (Component).

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT Hàn Quốc, câu hỏi về phương pháp phân tích Rumbaugh xuất hiện với tần suất dày đặc nhất:
  - Khẩu quyết thứ tự thực hiện 3 bước:
    $$\mathbf{객 \rightarrow 동 \rightarrow 기}$$
    - **객**체 모델링 (Object Modeling): Mô hình tĩnh, quan trọng nhất $\rightarrow$ dùng **객체 다이어그램 (Object Diagram)**.
    - **동**적 모델링 (Dynamic Modeling): Biến đổi trạng thái theo thời gian $\rightarrow$ dùng **상태도 (State Diagram)**.
    - **기**능 모델링 (Functional Modeling): Dòng dữ liệu chuyển hóa $\rightarrow$ dùng **자료 흐름도 (DFD - Data Flow Diagram)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phương pháp phân tích OMT của Rumbaugh (럼바우 기법):**

| Thứ tự thực hiện | Mô hình phân tích | Nội dung khảo sát cốt lõi | Biểu đồ công cụ chủ đạo |
| :---: | :--- | :--- | :--- |
| **Bước 1** | **객체 모델링** (Object Modeling) | Khảo sát cấu trúc tĩnh của hệ thống; nhận diện các đối tượng, thuộc tính, phép toán và quan hệ liên kết giữa các lớp. **Là bước quan trọng nhất và được tiến hành đầu tiên.** | **객체 다이어그램** (Object Diagram) |
| **Bước 2** | **동적 모델링** (Dynamic Modeling) | Mô tả hành vi tương tác, sự biến đổi trạng thái của đối tượng theo dòng chảy thời gian và các sự kiện kích hoạt (Event-driven). | **상태도** (State Diagram) |
| **Bước 3** | **기능 모델링** (Functional Modeling) | Mô tả cách thức các giá trị dữ liệu được chuyển hóa, tính toán và luân chuyển giữa các tiến trình chức năng bên trong hệ thống. | **자료 흐름도** (DFD - Data Flow Diagram) |

- **2. Bảng nhận diện nhanh các phương pháp luận OOA khác:**

| Tên phương pháp luận | Đặc điểm nhận diện trong câu hỏi thi |
| :--- | :--- |
| **Booch (부치)** | Kết hợp đồng thời cả quy trình phát triển vi mô (Micro Process) và vĩ mô (Macro Process). |
| **Jacobson (제이콥슨)** | Lấy **Use Case (유스케이스)** làm trung tâm dẫn dắt toàn bộ quy trình phân tích và thiết kế. |
| **Coad / Yourdon** | Ứng dụng mô hình thực thể mối quan hệ (**E-R 다이어그램**) làm cầu nối phân tích. |
| **Wirfs-Brock** | Coi phân tích và thiết kế là tiến trình liên tục, **không phân chia ranh giới rõ ràng** giữa hai giai đoạn. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ thực tế minh họa 3 mô hình Rumbaugh trong nghiệp vụ Máy rút tiền ATM:**
  1. *Object Modeling:* Xác định thực thể `Khách hàng`, `Thẻ ATM`, `Tài khoản ngân hàng`, `Máy rút tiền`.
  2. *Dynamic Modeling:* Mô tả chuỗi trạng thái máy ATM: Chờ khách $\rightarrow$ Nhận thẻ $\rightarrow$ Xác thực PIN $\rightarrow$ Nhả tiền $\rightarrow$ Trả thẻ. Nếu nhập sai PIN 3 lần thì chuyển sang trạng thái "Khóa thẻ".
  3. *Functional Modeling:* Dữ liệu số tiền yêu cầu rút được kiểm tra số dư, trừ tiền trong cơ sở dữ liệu và chuyển thành lệnh đếm tiền gửi ra khay tiền mặt (DFD).

### 복습 체크리스트
- [ ] Thuộc làu khẩu quyết thứ tự Rumbaugh: **객동기** (객체 $\rightarrow$ 동적 $\rightarrow$ 기능).
- [ ] Ghép đúng công cụ tương ứng: 객체 = 객체 다이어그램, 동적 = 상태도, 기능 = DFD.
- [ ] Nhớ Booch kết hợp vi mô/vĩ mô; Jacobson tập trung vào Use Case.
- [ ] Khẳng định 객체 모델링 (Object Modeling) là bước quan trọng nhất được làm đầu tiên.
