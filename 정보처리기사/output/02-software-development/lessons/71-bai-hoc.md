# 9. 스키마 3계층 (Three-Schema Architecture)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc kiến trúc 3 tầng lược đồ cơ sở dữ liệu theo tiêu chuẩn ANSI/SPARC: Lược đồ ngoài (외부 스키마), Lược đồ quan niệm (개념 스키마), và Lược đồ trong (내부 스키마).
- Hiểu rõ chức năng, đối tượng phục vụ và góc nhìn dữ liệu của từng tầng lược đồ trong hệ quản trị cơ sở dữ liệu.
- Giải thích được cơ chế đảm bảo tính độc lập dữ liệu (데이터 독립성): Tính độc lập logic (논리적 독립성) và Tính độc lập vật lý (물리적 독립성).

## 핵심 키워드 (Từ khóa)
- 스키마 3계층 (Three-Schema Architecture / ANSI/SPARC)
- 외부 스키마 (External Schema / 사용자 뷰 / 서브스키마)
- 개념 스키마 (Conceptual Schema / 전체 논리적 구조 / 제약조건)
- 내부 스키마 (Internal Schema / 물리적 저장구조 / 레코드 형식)
- 논리적 데이터 독립성 (Logical Data Independence)
- 물리적 데이터 독립성 (Physical Data Independence)

## 선행·연결 개념 (Kiến thức liên kết)
- [70-bai-hoc.md](70-bai-hoc.md): Công cụ kiểm chứng giao diện phần mềm.
- [72-bai-hoc.md](72-bai-hoc.md): Định luật Pareto trong kiểm thử phần mềm.
- [정보처리기사/output/03-database-construction/lessons/01-bai-hoc.md](../../03-database-construction/lessons/01-bai-hoc.md): Khái niệm cơ sở dữ liệu và hệ thống quản lý cơ sở dữ liệu.

## 읽는 방법 (Cách đọc)
- Phân biệt 3 góc nhìn từ ngoài vào trong:
  - **외부 스키마 (External - Tầng Ngoài):** Góc nhìn của từng **Người dùng cá nhân hoặc Lập trình viên** (User View). Một DB có thể có nhiều lược đồ ngoài (ví dụ: các View).
  - **개념 스키마 (Conceptual - Tầng Quan niệm):** Góc nhìn **Logic tổng thể** của toàn bộ tổ chức (Community View). Chỉ có duy nhất 1 lược đồ quan niệm thể hiện tất cả bảng, quan hệ, và ràng buộc toàn vẹn.
  - **내부 스키마 (Internal - Tầng Trong):** Góc nhìn **Vật lý** trên thiết bị lưu trữ (Physical Storage). Thể hiện cách bố trí bản ghi, chỉ mục, con trỏ và định dạng tệp trên ổ cứng.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 tầng lược đồ ANSI/SPARC:**

| Tầng lược đồ | Tên tiếng Hàn & Anh | Đối tượng sử dụng | Nội dung và phạm vi thể hiện |
| :--- | :--- | :--- | :--- |
| **Tầng Ngoài** | **외부 스키마 (External Schema)** | Người dùng cuối, Lập trình viên ứng dụng | Còn gọi là **서브스키마 (Sub-schema)** hoặc **사용자 뷰 (User View)**; chỉ hiển thị phần dữ liệu liên quan đến nghiệp vụ cụ thể của từng nhóm người dùng |
| **Tầng Quan niệm** | **개념 스키마 (Conceptual Schema)** | Quản trị viên CSDL (DBA), Thiết kế hệ thống | Thể hiện cấu trúc **toàn bộ dữ liệu logic của tổ chức**; định nghĩa các thực thể (Entity), quan hệ (Relationship), ràng buộc toàn vẹn, bảo mật |
| **Tầng Trong** | **내부 스키마 (Internal Schema)** | Kỹ sư hệ thống lưu trữ, DBMS engine | Cấu trúc **lưu trữ vật lý thực tế trên đĩa cứng**; bao gồm định dạng bản ghi, thứ tự vật lý, chỉ mục (B-Tree/Hash), phương pháp đánh địa chỉ |

- **Hai cấp độ độc lập dữ liệu (데이터 독립성):**

| Loại độc lập | Tầng ánh xạ (Mapping) | Ý nghĩa kỹ thuật cốt lõi |
| :--- | :--- | :--- |
| **논리적 독립성 (Độc lập logic)** | **외부 - 개념 사상 (External - Conceptual Mapping)** | Khi thay đổi cấu trúc bảng hoặc lược đồ quan niệm (thêm/xóa cột), các chương trình ứng dụng và lược đồ ngoài **không bị ảnh hưởng, không cần viết lại** |
| **물리적 독립성 (Độc lập vật lý)** | **개념 - 내부 사상 (Conceptual - Internal Mapping)** | Khi cấu trúc lưu trữ vật lý trên đĩa thay đổi (đổi dung lượng block, tái cấu trúc file, thêm index mới), lược đồ quan niệm và ứng dụng logic **hoàn toàn không bị thay đổi** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa View trong SQL và Lược đồ ngoài:**
  - Lệnh tạo `CREATE VIEW user_view AS SELECT id, name FROM employee;` chính là việc tạo ra một phần của Lược đồ ngoài (External Schema), che giấu thông tin nhạy cảm như mức lương hoặc số an sinh xã hội khỏi người dùng thông thường.
  - Nhờ có hai lớp ánh xạ (Mapping), DBMS có thể dịch yêu cầu từ góc nhìn của người dùng (External) xuống cấu trúc quan niệm (Conceptual) rồi thành các địa chỉ khối đĩa vật lý (Internal) một cách hoàn toàn tự động.

### 복습 체크리스트
- [ ] Phân biệt được 3 tầng: 외부 (User View), 개념 (Toàn thể logic), 내부 (Lưu trữ vật lý).
- [ ] Nhớ mỗi DB có nhiều 외부 스키마 nhưng chỉ có 1 개념 스키마 và 1 내부 스키마.
- [ ] Nắm được tính độc lập logic (sửa 개념 không làm sửa 외부) và độc lập vật lý (sửa 내부 không làm sửa 개념).
