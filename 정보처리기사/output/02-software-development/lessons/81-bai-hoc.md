# 33. DBMS (데이터베이스 관리 시스템)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của Hệ thống Quản trị Cơ sở Dữ liệu (DBMS - Database Management System) như một phần mềm trung gian giữa người dùng và cơ sở dữ liệu.
- Ghi nhớ sâu sắc 3 chức năng thiết yếu của DBMS: Chức năng Định nghĩa (정의 기능), Chức năng Thao tác (조작 기능), và Chức năng Điều khiển (제어 기능).
- Phân tích toàn diện các ưu điểm (giảm trùng lặp, bảo đảm tính độc lập, toàn vẹn) và nhược điểm (chi phí đắt đỏ, phức tạp, nguy cơ tắc nghẽn khi gặp sự cố) của việc áp dụng DBMS.

## 핵심 키워드 (Từ khóa)
- DBMS (Database Management System / 데이터베이스 관리 시스템)
- 정의 기능 (Definition Function / DDL / 데이터 구조 및 제약조건)
- 조작 기능 (Manipulation Function / DML / CRUD 인터페이스)
- 제어 기능 (Control Function / DCL / 무결성, 보안, 권한, 병행 제어)
- 데이터 중복 최소화 (Redundancy Minimization)
- 데이터 독립성 (Data Independence)

## 선행·연결 개념 (Kiến thức liên kết)
- [80-bai-hoc.md](80-bai-hoc.md): Danh sách liên tục và danh sách liên kết.
- [82-bai-hoc.md](82-bai-hoc.md): Tài liệu ghi chú phát hành phần mềm (Release Note).
- [정보처리기사/output/03-database-construction/lessons/01-bai-hoc.md](../../03-database-construction/lessons/01-bai-hoc.md): Tổng quan kiến trúc hệ thống cơ sở dữ liệu.

## 읽는 방법 (Cách đọc)
- Học theo bộ ba chức năng "Đ - T - Đ" (D - M - C):
  - **정의 (Definition - Định nghĩa):** Tạo khung bảng, kiểu dữ liệu, các ràng buộc (Primary Key, Foreign Key).
  - **조작 (Manipulation - Thao tác):** Cho phép người dùng thêm, sửa, xóa, tìm kiếm dữ liệu (Select, Insert, Update, Delete) một cách thuận tiện.
  - **제어 (Control - Điều khiển):** Đảm bảo an toàn thông tin, kiểm tra tính toàn vẹn, phân quyền người dùng, kiểm soát đồng thời (Concurrency Control) và khôi phục khi có sự cố.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 3 chức năng thiết yếu của DBMS (DBMS 필수 기능 3가지):**

| Chức năng | Ngôn ngữ đối ứng | Trách nhiệm và hành vi cốt lõi |
| :--- | :--- | :--- |
| **1. 정의 기능 (Định nghĩa)** | **DDL (Data Definition Language)** | Xác định cấu trúc logic và vật lý của dữ liệu; chỉ định kiểu dữ liệu, độ dài, mối quan hệ và các ràng buộc toàn vẹn |
| **2. 조작 기능 (Thao tác)** | **DML (Data Manipulation Language)** | Cung cấp phương tiện giao tiếp để người dùng yêu cầu các thao tác tìm kiếm (Retrieve), chèn (Insert), sửa (Update), xóa (Delete) dữ liệu |
| **3. 제어 기능 (Điều khiển)** | **DCL (Data Control Language)** | Đảm bảo tính chính xác và an toàn của dữ liệu: kiểm soát tính toàn vẹn (Integrity), bảo mật (Security), phân quyền truy cập, khôi phục sự cố (Recovery), và điều khiển đồng thời (Concurrency Control) |

- **Bảng tổng hợp Ưu điểm và Nhược điểm của DBMS:**

| Nhóm | Đặc tính chi tiết chuẩn đề thi |
| :--- | :--- |
| **Ưu điểm (장점)** | - **데이터 중복의 최소화 (Tối thiểu hóa trùng lặp dữ liệu)**; **데이터의 독립성 보장 (Bảo đảm tính độc lập dữ liệu)** logic và vật lý; **일관성 및 무결성 유지 (Duy trì tính nhất quán và toàn vẹn)** dữ liệu; **보안 유지 및 실시간 처리 (Bảo đảm an toàn bảo mật và xử lý thời gian thực)**; Chia sẻ dữ liệu đồng thời giữa nhiều ứng dụng |
| **Nhược điểm (단점)** | - **비용 증가 (Chi phí đắt đỏ):** Tốn kém chi phí bản quyền phần mềm và phần cứng cấu hình cao; **전문가 부족 (Thiếu chuyên gia):** Đòi hỏi kỹ sư DBA có trình độ chuyên môn cao; **복잡성 (Cấu trúc phức tạp):** Hệ thống cồng kềnh, khó quản trị hơn hệ thống tệp truyền thống; **집중 과부하 및 백업/회복 곤란 (Nguy cơ nghẽn tập trung):** Khi DBMS gặp sự cố sập thì toàn bộ các ứng dụng phụ thuộc đều bị gián đoạn, việc sao lưu phục hồi tốn thời gian |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh hệ thống DBMS với Hệ thống tệp truyền thống (File System):**
  - Hệ thống tệp (File System) khiến dữ liệu bị phân tán trên từng file riêng của từng chương trình, dẫn đến hai tai họa lớn: **Trùng lặp dữ liệu (데이터 중복성)** và **Phụ thuộc dữ liệu (데이터 종속성)** (sửa file cấu trúc thì code phải viết lại).
  - DBMS ra đời loại bỏ triệt để vấn đề phụ thuộc dữ liệu bằng kiến trúc ánh xạ 3 tầng lược đồ.

### 복습 체크리스트
- [ ] Ghi nhớ 3 chức năng sống còn của DBMS: 정의 (Definition), 조작 (Manipulation), 제어 (Control).
- [ ] Nhớ các ưu điểm cốt lõi: Giảm trùng lặp, đảm bảo tính độc lập dữ liệu, duy trì tính toàn vẹn.
- [ ] Nêu được các nhược điểm: Chi phí cao, cấu trúc phức tạp, nguy cơ tắc nghẽn tập trung khi xảy ra sự cố.
