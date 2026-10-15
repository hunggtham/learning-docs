# 1. 소프트웨어 개발 방법론 및 프레임워크 (Phương pháp luận & Framework phát triển PM)

## 학습 목표 (Mục tiêu)
- Nắm vững đặc trưng, triết lý và sự tiến hóa của các phương pháp luận phát triển phần mềm kinh điển: Phương pháp luận cấu trúc (구조적 방법론), Phương pháp luận kỹ nghệ thông tin (정보공학 방법론), Phương pháp luận phát triển dựa trên thành phần (CBD 방법론), và Phương pháp luận linh hoạt (Agile).
- Phân biệt sự khác nhau giữa cách tiếp cận trọng tâm xử lý (Process-centric trong Structured) và trọng tâm dữ liệu (Data-centric trong Information Engineering với mô hình ERD).
- Thấu hiểu bản chất của phương pháp luận CBD (Component-Based Development) – lắp ráp các khối thành phần có sẵn (Lego architecture) và vai trò tăng tốc của khung phát triển phần mềm (Framework).

## 핵심 키워드 (Từ khóa)
- 구조적 방법론 (Structured Methodology - Process 중심, Divide & Conquer)
- 정보공학 방법론 (Information Engineering - Data 중심, ERD)
- 객체지향 방법론 (Object-Oriented - 캡슐화, 상속, 다형성)
- 컴포넌트 기반 방법론 (CBD - Component-Based Development, 조립)
- 애자일 방법론 (Agile - 변화 대응, 고객 소통)
- 소프트웨어 프레임워크 (Framework - 반제품 소프트웨어)

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): May đo phương pháp luận (Tailoring) và các Framework máy chủ phổ biến.
- [03-bai-hoc.md](03-bai-hoc.md): Đặc tính của Framework (IoC) và các công nghệ phần mềm mới (SDDC, SDN).
- [06-bai-hoc.md](06-bai-hoc.md): Quản lý dự án phần mềm và các mô hình ước tính chi phí.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh 4 phương pháp luận cốt lõi trong đề thi kỹ sư CNTT:
  - **구조적 (Cấu trúc):** Từ khóa **"처리(Process) 중심"** (Lấy tiến trình làm trung tâm), áp dụng nguyên lý **"Chia để trị" (분할과 정복 - Divide and Conquer)**, công cụ đại diện là DFD (Sơ đồ dòng dữ liệu) và Mini-spec.
  - **정보공학 (Kỹ nghệ thông tin):** Từ khóa **"자료(Data) 중심"** (Lấy dữ liệu làm trung tâm), lập mô hình dữ liệu bằng **"ERD" (Entity-Relationship Diagram)**.
  - **컴포넌트 기반 (CBD):** Từ khóa **"컴포넌트 조립"** (Lắp ráp các thành phần có sẵn như Lego), tăng tối đa tỷ lệ tái sử dụng, phân tích tạo ra tài liệu định nghĩa yêu cầu.
  - **프레임워크 (Framework):** Phần mềm **bán thành phẩm (반제품)** cung cấp sẵn cấu trúc và thành phần dùng chung, giải phóng sự phụ thuộc vào nhà thầu.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các phương pháp luận phát triển phần mềm kinh điển:**

| Phương pháp luận | Trọng tâm thiết kế | Nguyên lý kỹ thuật cốt lõi | Công cụ & Sản phẩm đầu ra đại diện |
| :--- | :--- | :--- | :--- |
| **구조적 방법론** (Structured) | **Xử lý / Tiến trình** (Process-centric) | Áp dụng nguyên tắc **Chia để trị (분할과 정복)** để phân rã hệ thống phức tạp thành các module con đơn giản; tiếp cận từ trên xuống (Top-down). | Sơ đồ luồng dữ liệu (DFD), Từ điển dữ liệu (DD), Đặc tả mini (Mini-spec), Biểu đồ cấu trúc (Structure Chart). |
| **정보공학 방법론** (Information Engineering) | **Dữ liệu / Thông tin** (Data-centric) | Coi dữ liệu là tài sản chiến lược lâu dài của doanh nghiệp; quy trình nghiệp vụ có thể đổi nhưng cấu trúc dữ liệu luôn ổn định. | **Sơ đồ quan hệ thực thể (ERD)**, Ma trận phân tích chức năng - dữ liệu (CRUD Matrix). |
| **객체지향 방법론** (Object-Oriented) | **Đối tượng thực thể** (Object-centric) | Gom dữ liệu và các hàm thao tác trên dữ liệu đó thành các Lớp đối tượng; hỗ trợ Đóng gói, Kế thừa, Đa hình. | Biểu đồ UML (Class Diagram, Use Case Diagram, Sequence Diagram), Phương pháp OMT của Rumbaugh. |
| **CBD 방법론** (Component-Based) | **Thành phần độc lập** (Component-centric) | Lắp ráp và tích hợp các khối thành phần (Component) độc lập đã được kiểm thử và đóng gói sẵn như trò chơi xếp hình Lego. | Kho lưu trữ thành phần (Component Repository), Tài liệu định nghĩa yêu cầu người dùng, Hợp đồng giao diện (Interface Contract). |
| **애자일 방법론** (Agile) | **Con người & Giao tiếp** (People/Agility) | Thích ứng linh hoạt với sự thay đổi của yêu cầu người dùng thông qua các chu kỳ lặp ngắn (Sprint 1-4 tuần); ưu tiên phần mềm chạy tốt hơn tài liệu đồ sộ. | Scrum (Product Backlog, Daily Standup), Extreme Programming XP (Pair Programming, TDD, CI/CD). |

- **2. Khái niệm Khung phát triển phần mềm (Software Framework):**
  - Là hệ thống phần mềm ở dạng **bán thành phẩm (반제품)**, cung cấp sẵn kiến trúc chuẩn, các lớp trừu tượng và các module hạ tầng dùng chung (kết nối DB, quản lý transaction, xử lý ngoại lệ, bảo mật).
  - Lập trình viên không phải viết lại mã nguồn nền móng mà chỉ tập trung cài đặt logic nghiệp vụ đặc thù, giúp nâng cao chất lượng và giải quyết triệt để sự phụ thuộc vào từng nhà thầu riêng lẻ.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh vòng đời phát triển giữa Structured và CBD:**
  - Trong phương pháp luận cấu trúc, vòng đời SDLC đi tuần tự: Phân tích yêu cầu $\rightarrow$ Thiết kế $\rightarrow$ Cài đặt mã từ số 0 $\rightarrow$ Kiểm thử.
  - Trong phương pháp luận CBD, giai đoạn thiết kế tập trung vào việc **khảo sát và tuyển chọn các thành phần có sẵn trên thị trường** (Commercial Off-The-Shelf - COTS) để tích hợp, chỉ phát triển mới những thành phần nghiệp vụ cá biệt hóa chưa từng có.

### 복습 체크리스트
- [ ] Phân biệt được: Phương pháp cấu trúc lấy Xử lý (Process) làm trung tâm, Kỹ nghệ thông tin lấy Dữ liệu (Data - ERD) làm trung tâm.
- [ ] Nhớ nguyên lý cốt lõi của phương pháp cấu trúc: Chia để trị (분할과 정복 - Divide and Conquer).
- [ ] Nhớ CBD là phương pháp phát triển bằng cách lắp ráp các thành phần có sẵn (Lego).
- [ ] Nắm được định nghĩa Framework: Phần mềm bán thành phẩm (반제품) cung cấp cấu trúc dùng chung.
