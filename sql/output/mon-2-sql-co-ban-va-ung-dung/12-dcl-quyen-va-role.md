<!-- lecture-contract: v2 -->
# DCL, quyền và Role (Data Control Language)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **DCL, quyền và Role**. Route đi từ security model → System Privileges vs Object Privileges → Centralized management with `ROLE` → CASCADE mechanism comparison: `WITH GRANT OPTION` vs `WITH ADMIN OPTION`.

> **Mục tiêu:** Nắm vững cơ chế phân quyền bằng `GRANT`, thu hồi quyền bằng `REVOKE`, phân biệt rạch ròi giữa Quyền hệ thống và Quyền đối tượng, quản trị tập trung qua `ROLE`, và nắm chắc bản chất thu hồi dây chuyền (CASCADE) của `WITH GRANT OPTION` so với `WITH ADMIN OPTION` trong đề thi SQLD.

> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 100–103.

---

### 1. DCL (Data Control Language) — Ngôn ngữ điều khiển dữ liệu

> **KR:** DCL은 데이터베이스 객체에 대한 접근 권한을 부여(GRANT)하거나 이미 부여된 권한을 회수(REVOKE)하여 데이터 보안과 무결성을 유지하는 언어이다.

Trong cơ sở dữ liệu quan hệ, tài khoản người dùng (`User`) mặc định không thể kết nối hoặc truy cập bảng của người khác nếu chưa được cấp phép.
- **`GRANT`:** Cấp phát quyền hoặc Role cho người dùng.
- **`REVOKE`:** Thu hồi quyền hoặc Role đã cấp.

---

### 2. Phân biệt Quyền hệ thống (System Privilege) vs Quyền đối tượng (Object Privilege)

Đây là phân loại nền tảng quan trọng nhất của phân quyền trong CSDL:

| Tiêu chí phân biệt | Quyền hệ thống (시스템 권한) | Quyền đối tượng (오브젝트 권한) |
| --- | --- | --- |
| **Phạm vi tác động** | Toàn bộ cơ sở dữ liệu hoặc schema (liên quan đến DDL và quản trị). | Thao tác trên **một đối tượng CSDL cụ thể** (bảng, view, sequence). |
| **Các quyền tiêu biểu** | `CREATE SESSION` (đăng nhập DB), `CREATE TABLE`, `CREATE VIEW`, `CREATE USER`, `DROP ANY TABLE`. | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `ALTER`, `REFERENCES`, `INDEX`. |
| **Thực thể có quyền cấp** | Quản trị viên hệ thống (DBA / SYS / SYSTEM). | Chủ sở hữu đối tượng (`Owner`) hoặc Quản trị viên DBA. |
| **Cú pháp mệnh đề** | Không có mệnh đề `ON object`. | **Bắt buộc có mệnh đề `ON object`**. |
| **Tùy chọn ủy quyền tiếp** | **`WITH ADMIN OPTION`** | **`WITH GRANT OPTION`** |

```sql
-- 1. Cấp quyền hệ thống (System Privileges)
-- Cho phép user_a đăng nhập và tạo bảng trong schema của mình
GRANT CREATE SESSION, CREATE TABLE TO user_a;

-- 2. Cấp quyền đối tượng (Object Privileges)
-- Cho phép user_b truy vấn và cập nhật trên bảng emp của hr
GRANT SELECT, UPDATE ON hr.emp TO user_b;

-- Cho phép user_b chỉ cập nhật trên cột sal của bảng emp
GRANT UPDATE (sal) ON hr.emp TO user_b;
```

#### Quy tắc kiểm tra cú pháp trong đề thi
- Một câu lệnh `GRANT` hoặc `REVOKE` có thể xử lý đồng thời **nhiều quyền** hoặc **nhiều tài khoản người dùng**.
- Tuy nhiên, đối với quyền đối tượng, **chỉ được phép chỉ định duy nhất 1 đối tượng** trong mệnh đề `ON` (viết `GRANT SELECT ON emp, dept TO user_a;` sẽ báo lỗi cú pháp).
- Quyền `REFERENCES` (tạo khóa ngoại trỏ tới bảng khác) chỉ có thể cấp cho User, không thể cấp thông qua Role.

---

### 3. ROLE (Vai trò) — Quản trị nhóm quyền tập trung

> **KR:** ROLE은 다수의 권한을 하나의 묶음으로 정의하여 사용자에게 부여하는 객체이다. 권한 관리의 효율성과 일관성을 크게 향상시킨다.

Khi doanh nghiệp có hàng trăm nhân viên, việc cấp phát từng quyền riêng lẻ cho từng tài khoản sẽ gây hỗn loạn và khó thu hồi khi nhân viên chuyển nhóm. `ROLE` đóng vai trò là một túi chứa gom nhóm nhiều quyền:

```sql
-- 1. Quản trị viên tạo Role
CREATE ROLE dev_role;

-- 2. Gán các quyền cần thiết vào Role
GRANT CREATE TABLE, CREATE VIEW TO dev_role;        -- Quyền hệ thống
GRANT SELECT, INSERT, UPDATE ON emp TO dev_role;    -- Quyền đối tượng

-- 3. Gán Role cho các tài khoản người dùng
GRANT dev_role TO dev_user1, dev_user2;
```

#### Đặc tính kỹ thuật quan trọng của ROLE trong đề thi
1. **Thời điểm có hiệu lực:** Quyền được cấp trực tiếp (`Direct Grant`) có hiệu lực ngay trong phiên hiện tại. Quyền cấp qua `ROLE` đòi hỏi người dùng phải **đăng nhập lại (Re-login)** hoặc thực thi lệnh `SET ROLE dev_role;` để kích hoạt trong phiên.
2. **Quy tắc thu hồi quyền qua Role:** Nếu một quyền được cấp cho người dùng thông qua Role, chủ sở hữu **không thể thu hồi trực tiếp quyền đó từ người dùng** (`REVOKE SELECT ON emp FROM dev_user1;` sẽ báo lỗi). Muốn thu hồi, quản trị viên bắt buộc phải rút quyền đó ra khỏi Role hoặc thu hồi toàn bộ Role khỏi người dùng (`REVOKE dev_role FROM dev_user1;`).

---

### 4. So sánh chuyên sâu WITH GRANT OPTION vs WITH ADMIN OPTION

Đây là một trong những câu hỏi phân loại điểm cao kinh điển nhất của kỳ thi SQLD. Cả hai đều cho phép người nhận quyền có thể ủy quyền tiếp cho người thứ ba, nhưng khác biệt hoàn toàn về cơ chế thu hồi dây chuyền (**CASCADE REVOKE**):

| Tiêu chí | `WITH GRANT OPTION` | `WITH ADMIN OPTION` |
| --- | --- | --- |
| **Phạm vi áp dụng** | **Chỉ áp dụng cho Quyền đối tượng (Object Privilege)** | **Áp dụng cho Quyền hệ thống (System Privilege) hoặc ROLE** |
| **Quan hệ ủy quyền** | Phụ thuộc phân cấp chuỗi (Hierarchy Chain). | Độc lập hoàn toàn sau khi cấp phát. |
| **Hành vi khi trung gian bị REVOKE** | **THU HỒI DÂY CHUYỀN (CASCADE REVOKE)**: Bị thu hồi thì toàn bộ cấp dưới cũng mất sạch. | **KHÔNG THU HỒI DÂY CHUYỀN (NO CASCADE)**: Bị thu hồi thì người thứ ba vẫn giữ nguyên quyền. |
| **Thu hồi vượt cấp** | Người cấp ban đầu **không thể thu hồi trực tiếp từ người thứ ba**. | Người cấp ban đầu **có thể thu hồi trực tiếp từ bất kỳ ai**. |

#### Kịch bản minh họa đề thi SQLD (Lee -> Kim -> Park)

Giả sử `Lee` là Quản trị viên (hoặc Chủ sở hữu bảng), `Kim` là Quản lý trung gian, và `Park` là Lập trình viên thứ ba.

#### Kịch bản 1: WITH GRANT OPTION (Quyền đối tượng)
1. `Lee` cấp quyền xem bảng cho `Kim` kèm quyền cấp tiếp:
   ```sql
   GRANT SELECT ON emp TO kim WITH GRANT OPTION;
   ```
2. `Kim` cấp tiếp quyền xem bảng đó cho `Park`:
   ```sql
   GRANT SELECT ON emp TO park;
   ```
3. `Lee` không thể thu hồi trực tiếp từ `Park`.
4. Khi `Lee` thu hồi quyền của `Kim`:
   ```sql
   REVOKE SELECT ON emp FROM kim;
   ```
   - **Kết quả:** Do cơ chế **CASCADE**, quyền của `Park` cũng tự động bị hủy bỏ theo! Cả `Kim` và `Park` đều không còn quyền `SELECT` trên bảng `emp`.

#### Kịch bản 2: WITH ADMIN OPTION (Quyền hệ thống)
1. `Lee` cấp quyền hệ thống cho `Kim` kèm quyền quản trị:
   ```sql
   GRANT CREATE TABLE TO kim WITH ADMIN OPTION;
   ```
2. `Kim` cấp tiếp quyền này cho `Park`:
   ```sql
   GRANT CREATE TABLE TO park;
   ```
3. `Lee` hoàn toàn có thể thu hồi trực tiếp quyền của `Park` mà không cần thông qua `Kim`.
4. Khi `Lee` thu hồi quyền của `Kim`:
   ```sql
   REVOKE CREATE TABLE FROM kim;
   ```
   - **Kết quả:** Do cơ chế **NO CASCADE**, chỉ có `Kim` bị mất quyền. Quyền `CREATE TABLE` của `Park` **vẫn tồn tại nguyên vẹn**!

---

## 5. Nối mạch sang Bài tiếp theo: PIVOT, UNPIVOT và Regular Expression

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 12 đã hoàn thiện toàn bộ hệ thống quản trị an ninh dữ liệu, phân loại Quyền hệ thống vs Quyền đối tượng và cơ chế CASCADE của `WITH GRANT OPTION` vs `WITH ADMIN OPTION`.
> - **Đang giải quyết gì:** Trong khai thác báo cáo nghiệp vụ và phân tích dữ liệu, dữ liệu chuẩn thường được lưu ở dạng dọc (Long format) nhưng người dùng đòi hỏi xoay thành ma trận chéo ngang (Wide format), hoặc cần kiểm tra lọc chuỗi theo biểu thức chính quy phức tạp?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 13 — PIVOT, UNPIVOT và Regular Expression](./13-pivot-unpivot-va-regexp.md) để học kỹ thuật xoay trục dữ liệu nâng cao (PIVOT nhiều cột/nhiều hàm, xử lý NULL trong UNPIVOT) và bộ 5 hàm `REGEXP_*` của Oracle.
