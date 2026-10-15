# 091: 스키마 (Schema)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của Lược đồ cơ sở dữ liệu (스키마 - Schema): bản thiết kế cấu trúc, kiểu dữ liệu, mối quan hệ và các ràng buộc toàn vẹn của toàn bộ hệ thống cơ sở dữ liệu.
- Phân biệt sâu sắc 3 góc nhìn lược đồ theo tiêu chuẩn ANSI/SPARC: Lược đồ ngoài (외부 스키마), Lược đồ quan niệm (개념 스키마), và Lược đồ trong (내부 스키마).
- Hiểu rõ vai trò của Quản trị viên cơ sở dữ liệu (DBA) đối với Lược đồ quan niệm - tầng lược đồ trung tâm đại diện cho tri thức dữ liệu của toàn tổ chức.

## 핵심 키워드 (Từ khóa)
- 스키마 (Schema / 데이터베이스 구조와 제약조건)
- 외부 스키마 (External Schema / 사용자 뷰 / 서브스키마)
- 개념 스키마 (Conceptual Schema / 범기관적 관점 / 전체 논리 구조)
- 내부 스키마 (Internal Schema / 물리적 저장 구조 / 시스템 관점)
- DDL (Data Definition Language / 데이터 정의어)
- 메타데이터 (Metadata / 데이터 사전에 저장)

## 선행·연결 개념 (Kiến thức liên kết)
- [94-bai-hoc.md](94-bai-hoc.md): Tính độc lập dữ liệu (Logical & Physical).
- [96-bai-hoc.md](96-bai-hoc.md): Lập trình SQL thủ tục (Procedural SQL).
- [71-bai-hoc.md](71-bai-hoc.md): Kiến trúc ba tầng lược đồ trong cơ sở dữ liệu.

## 읽는 방법 (Cách đọc)
- Phân biệt 3 góc nhìn (Perspective) của Schema:
  - **외부 스키마 (External):** Góc nhìn của từng **Người dùng / Lập trình viên** (User/Programmer View). Tùy theo vai trò, mỗi người chỉ nhìn thấy một góc nhỏ của cơ sở dữ liệu (thường thông qua các View). Có thể có vô số 외부 스키마.
  - **개념 스키마 (Conceptual):** Góc nhìn của **Doanh nghiệp / DBA** (Enterprise/Global View). Thể hiện toàn bộ thực thể, bảng, thuộc tính, khóa chính/ngoại và quy tắc nghiệp vụ. Chỉ có **duy nhất 1** 개념 스키마 trong một hệ thống DB.
  - **내부 스키마 (Internal):** Góc nhìn của **Hệ thống lưu trữ / Đĩa cứng** (Physical Storage View). Định nghĩa cách tổ chức bản ghi thực tế, độ dài byte, con trỏ và chỉ mục trên thiết bị nhớ. Chỉ có **duy nhất 1** 내부 스키마.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 3 tầng lược đồ cơ sở dữ liệu:**

| Tầng lược đồ | Tên gọi tương đương | Đối tượng phục vụ chính | Nội dung định nghĩa cốt lõi |
| :--- | :--- | :--- | :--- |
| **외부 스키마 (External)** | **사용자 뷰 (User View)**, 서브스키마 (Sub-schema) | Người dùng cuối, Lập trình viên giao diện | Cấu trúc dữ liệu logic cần thiết cho một ứng dụng cụ thể; che giấu dữ liệu không liên quan |
| **개념 스키마 (Conceptual)** | **전체적인 뷰 (Global View)**, Thông thường gọi tắt là "스키마" | Quản trị viên cơ sở dữ liệu (DBA), Kiến trúc sư dữ liệu | Định nghĩa toàn bộ cấu trúc bảng, kiểu dữ liệu, mối quan hệ thực thể, ràng buộc toàn vẹn và bảo mật |
| **내부 스키마 (Internal)** | **저장 스키마 (Storage View)**, 물리적 스키마 | Hệ điều hành, Kỹ sư hệ thống DBMS engine | Định dạng bản ghi vật lý, biểu diễn dữ liệu dạng nhị phân, cấu trúc cây chỉ mục (B-Tree/Hash), phương pháp đánh địa chỉ đĩa |

- **Đặc điểm sống còn của Schema:**
  - Lược đồ được định nghĩa bằng ngôn ngữ định nghĩa dữ liệu **DDL (Data Definition Language)**.
  - Nội dung mô tả lược đồ được lưu trữ an toàn trong **Từ điển dữ liệu (Data Dictionary)** dưới dạng Siêu dữ liệu (**메타데이터 - Metadata**).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa Schema và Instance:**
  - **스키마 (Schema):** Là khung cấu trúc tĩnh (khuôn đúc), rất ít khi thay đổi (ví dụ: khai báo bảng `Student(id INT, name VARCHAR(50))`).
  - **인스턴스 (Instance):** Là tập hợp các bản ghi dữ liệu thực tế tại một thời điểm cụ thể (nước đổ vào khuôn), liên tục thay đổi theo thời gian khi người dùng thêm/sửa/xóa bản ghi.

### 복습 체크리스트
- [ ] Phân biệt được 외부 (User view), 개념 (Global logic view), 내부 (Storage physical view).
- [ ] Nhớ số lượng: DB có thể có nhiều 외부 스키마, nhưng chỉ có 1 개념 스키마 và 1 내부 스키마.
- [ ] Nhớ Schema được định nghĩa bằng DDL và lưu trữ dưới dạng Metadata trong Data Dictionary.
- [ ] Phân biệt được Schema (khung tĩnh) và Instance (dữ liệu biến động theo thời gian).
