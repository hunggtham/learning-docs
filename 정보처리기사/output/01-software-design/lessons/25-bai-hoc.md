# 1. 소프트웨어 아키텍처 (Software Architecture)

## 학습 목표 (Mục tiêu)
- Phân biệt rạch ròi giữa Thiết kế mức cao (`상위 설계` - High-level Design) và Thiết kế mức thấp (`하위 설계` - Low-level Design) trong quy trình phát triển phần mềm.
- Thuộc nằm lòng mô hình kiến trúc 4+1 góc nhìn (`4+1 View Model` do Philippe Kruchten đề xuất) và vai trò trung tâm của Use Case View.
- Nắm vững đối tượng và mục đích của từng góc nhìn trong 4+1 View: Logical View, Implementation View, Process View, và Deployment View.

## 핵심 키워드 (Từ khóa)
- 상위 설계 (Thiết kế mức cao / Kiến trúc tổng thể / High-level Design)
- 하위 설계 (Thiết kế mức thấp / Thiết kế chi tiết / Low-level Design)
- 4+1 View Model (Mô hình 4+1 góc nhìn kiến trúc)
- 유스케이스 뷰 (Use Case View / Trung tâm kiểm chứng)
- 논리 뷰 (Logical View / Class, Object)
- 구현 뷰 (Implementation View / Component, Source code)
- 프로세스 뷰 (Process View / Thread, Concurrency)
- 배포 뷰 (Deployment View / Hardware, Network)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([5. 소프트웨어 아키텍처 및 설계](24-bai-hoc.md)):** Sau khi xem xét các mẫu kiến trúc tổng quát và tiêu chuẩn ISO 9126, bài này đi sâu vào phương pháp luận phân cấp thiết kế và mô hình hóa đa chiều 4+1 View.
- **Tiếp nối sang bài sau ([6. 객체지향](26-bai-hoc.md)):** Chuyển từ góc nhìn kiến trúc vĩ mô sang các khái niệm nền tảng của Lập trình hướng đối tượng (OOP: Class, Object, Encapsulation, Polymorphism).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chắc chắn bảng phân loại: cái gì thuộc "상위 설계" (Kiến trúc, DB, Giao diện phân hệ) và cái gì thuộc "하위 설계" (Thuật toán, Cấu trúc dữ liệu nội bộ module).
- Đọc TẦNG B để hiểu tại sao số 1 trong "4+1" lại đóng vai trò sợi dây xâu chuỗi và xác nhận tính toàn vẹn của cả 4 góc nhìn kỹ thuật còn lại.

---

## 1. 소프트웨어 아키텍처 (Software Architecture)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **So sánh đối chiếu 상위 설계 vs 하위 설계:**
  - **1. 상위 설계 (High-level Design - Thiết kế mức cao / Thiết kế kiến trúc):**
    - Trọng tâm: Bức tranh toàn cảnh hệ thống từ trên xuống (`시스템의 전체적인 구조`).
    - Các hạng mục cốt lõi:
      - `아키텍처 설계 (Thiết kế kiến trúc)`: Phân chia hệ thống thành các phân hệ (Subsystems).
      - `데이터베이스 설계 (Thiết kế CSDL)`: Lược đồ quan hệ, mô hình E-R logic.
      - `시스템 인터페이스 정의 (Định nghĩa giao diện hệ thống)`: Giao thức và định dạng dữ liệu trao đổi giữa các phân hệ và hệ thống bên ngoài.
  - **2. 하위 설계 (Low-level Design - Thiết kế mức thấp / Thiết kế chi tiết / 모듈 설계):**
    - Trọng tâm: Logic bên trong của từng đơn vị mô-đun chức năng riêng biệt.
    - Các hạng mục cốt lõi:
      - `모듈 내부 알고리즘 (Thuật toán nội bộ của mô-đun)`: Các bước logic xử lý (Flowchart, N-S chart).
      - `모듈 내부 자료 구조 (Cấu trúc dữ liệu nội bộ)`: Biến cục bộ, mảng, danh sách liên kết.
      - `오퍼레이션 상세 로직 (Logic chi tiết của hàm)`: Mã giả (Pseudocode) trước khi lập trình.
- **Mô hình 4+1 View của Philippe Kruchten:**
  - Mục đích: Mô tả kiến trúc phần mềm một cách toàn diện từ góc nhìn của nhiều bên liên quan khác nhau (Người dùng, Lập trình viên, Quản trị viên hệ thống, Kỹ sư tích hợp).
  - **Cấu trúc 5 góc nhìn:**
    1. **유스케이스 뷰 (Use Case View - Góc nhìn ca sử dụng - Cái gốc "+1"):**
       - **Đóng vai trò trung tâm (+1)**; mô tả các chức năng và hành vi của hệ thống nhìn từ người dùng cuối (`최종 사용자`).
       - Dùng làm thước đo kiểm chứng và thúc đẩy sự phát triển của cả 4 view kỹ thuật còn lại.
    2. **논리 뷰 (Logical View - Góc nhìn logic):**
       - Dành cho **Thiết kế viên và Lập trình viên**.
       - Mô tả cấu trúc hướng đối tượng bên trong (Lớp, Thuộc tính, Phương thức, Gói, Quan hệ kế thừa).
    3. **구현 뷰 / 컴포넌트 뷰 (Implementation View - Góc nhìn triển khai):**
       - Dành cho **Nhóm phát triển phần mềm**.
       - Mô tả cấu trúc các tệp mã nguồn, thư viện liên kết (.jar, .dll), mô-đun phần mềm và các thành phần có thể thực thi.
    4. **프로세스 뷰 (Process View - Góc nhìn tiến trình):**
       - Dành cho **Kỹ sư tích hợp hệ thống**.
       - Mô tả khía cạnh phi chức năng: Tính đồng thời (`동시성 - Concurrency`), luồng xử lý (Threads), đồng bộ hóa và hiệu năng hệ thống.
    5. **배포 뷰 (Deployment View - Góc nhìn phân bố vật lý):**
       - Dành cho **Kỹ sư hệ thống và Quản trị viên hạ tầng**.
       - Mô tả cách bố trí các thành phần phần mềm trên các nút phần cứng vật lý (Servers), cấu hình mạng và thiết bị ngoại vi.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Thuật toán chi tiết của mô-đun (모듈 알고리즘) thuộc thiết kế mức cao (상위 설계)?"* -> **Sai**. Thuộc **Thiết kế mức thấp (하위 설계)**.
  - **Bẫy 2 (4+1 View):** Góc nhìn nào đóng vai trò trung tâm liên kết 4 góc nhìn còn lại trong mô hình 4+1 View? -> **유스케이스 뷰 (Use Case View)**.
  - **Bẫy 3:** *"Góc nhìn nào mô tả các luồng chạy đồng thời (동시성) và tiến trình hệ thống?"* -> **프로세스 뷰 (Process View)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Mức cao vẽ Kiến trúc và CSDL; Mức thấp vẽ Thuật toán và Dữ liệu mô-đun; 4+1 View lấy Use Case làm trung tâm soi chiếu Logic, Triển khai, Tiến trình và Phân bố".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ánh xạ sơ đồ UML vào mô hình 4+1 View:**
  - `Use Case View` $\longleftrightarrow$ Use Case Diagram
  - `Logical View` $\longleftrightarrow$ Class Diagram, Object Diagram
  - `Implementation View` $\longleftrightarrow$ Component Diagram, Package Diagram
  - `Process View` $\longleftrightarrow$ Activity Diagram, Sequence Diagram
  - `Deployment View` $\longleftrightarrow$ Deployment Diagram

### 복습 체크리스트
- [ ] Phân loại chính xác các hạng mục công việc thành 상위 설계 (Kiến trúc, DB) hoặc 하위 설계 (Thuật toán, Mô-đun).
- [ ] Kể tên đầy đủ 5 góc nhìn trong mô hình 4+1 View của Kruchten.
- [ ] Giải thích tại sao 유스케이스 뷰 (Use Case View) lại là trung tâm (+1).
- [ ] Phân biệt đối tượng phục vụ của Logical View (dev), Process View (concurrency), và Deployment View (hạ tầng phần cứng).
