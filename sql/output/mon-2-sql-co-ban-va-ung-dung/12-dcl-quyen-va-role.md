<!-- lecture-contract: v2 -->
# DCL, quyền và Role (Data Control Language)

> **Mục tiêu:** Nắm vững cơ chế phân quyền bằng `GRANT`, thu hồi quyền bằng `REVOKE`, quản trị tập trung quyền qua `ROLE`, và phân biệt cốt lõi giữa `WITH GRANT OPTION` và `WITH ADMIN OPTION` trong đề thi SQLD.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 100–103.
>
> **Mạch kiến thức:** Bài trước đã tạo dựng các bảng và đối tượng lưu trữ. Bài này kiểm soát lớp an ninh: *Ai có quyền xem, sửa dữ liệu hoặc can thiệp vào cấu trúc hệ thống?*

---

### 1. DCL (Data Control Language) — Ngôn ngữ điều khiển dữ liệu

> **KR:** DCL은 데이터베이스 객체에 대한 접근 권한을 부여(GRANT)하거나 이미 부여된 권한을 회수(REVOKE)하여 데이터 보안과 무결성을 유지하는 언어이다.

Trong cơ sở dữ liệu quan hệ, tài khoản người dùng (`User`) mặc định không thể truy cập hay thao tác trên bảng của người khác nếu chưa được cấp phép.
- **Phân loại quyền trong DBMS:**
  1. **오브젝트 권한 (Object Privilege - Quyền đối tượng):** Cho phép thao tác dữ liệu trên một đối tượng cụ thể (`SELECT`, `INSERT`, `UPDATE`, `DELETE` trên bảng/view). Quyền này do chính chủ sở hữu đối tượng (`Owner`) hoặc quản trị viên cấp.
  2. **시스템 권한 (System Privilege - Quyền hệ thống):** Cho phép thực thi các tác vụ quản trị hệ thống hoặc DDL diện rộng (`CREATE TABLE`, `CREATE VIEW`, `CREATE USER`, `DROP ANY TABLE`). Quyền này chỉ do DBA (quản trị viên) cấp phát.

---

### 2. GRANT와 REVOKE의 문법 및 규칙 — Cấp và thu hồi quyền

> **KR:** 권한을 부여할 때는 반드시 객체 소유자나 관리자 계정으로 접속해야 하며, 하나의 명령어로 여러 유저 또는 여러 권한을 동시에 처리할 수 있다.

```sql
-- Cấp quyền đối tượng (Object Privilege)
GRANT SELECT, INSERT ON emp TO user_a, user_b;

-- Cấp quyền hệ thống (System Privilege - Thực hiện bởi DBA)
GRANT CREATE TABLE, CREATE VIEW TO user_a;

-- Thu hồi quyền
REVOKE INSERT ON emp FROM user_a;
REVOKE CREATE VIEW FROM user_a;
```

- **Quy tắc thi trắc nghiệm:**
  - Một câu lệnh `GRANT` hoặc `REVOKE` có thể thao tác với **nhiều quyền** hoặc **nhiều tài khoản** cùng lúc.
  - Tuy nhiên, trong một câu lệnh quyền đối tượng, **chỉ áp dụng trên 1 đối tượng duy nhất** (không viết `ON emp, dept`).
  - Nếu thu hồi một quyền mà người dùng chưa từng được cấp (hoặc đã bị thu hồi trước đó), hệ thống sẽ báo lỗi.

---

### 3. ROLE (Vai trò) — Quản trị nhóm quyền tập trung

> **KR:** ROLE은 다수의 권한을 하나의 묶음으로 정의하여 사용자에게 부여하는 객체이다. 권한 관리의 효율성과 일관성을 크게 향상시킨다.

Khi số lượng người dùng trong tổ chức tăng cao, việc cấp phát từng quyền riêng lẻ cho từng người là rất tốn công và dễ sai sót. `ROLE` ra đời đóng vai trò trung gian gom nhóm các quyền lại với nhau:

```sql
-- 1. Quản trị viên tạo Role
CREATE ROLE dev_role;

-- 2. Cấp các quyền cần thiết vào Role
GRANT SELECT, INSERT, UPDATE ON emp TO dev_role;
GRANT SELECT ON dept TO dev_role;

-- 3. Gán Role cho người dùng
GRANT dev_role TO dev_user1, dev_user2;
```

- **Đặc tính kỹ thuật quan trọng trong đề thi:**
  - Quyền được cấp trực tiếp (`Direct Grant`) có hiệu lực ngay lập tức trong phiên làm việc hiện tại.
  - Khi người dùng được cấp quyền thông qua `ROLE`, **người dùng bắt buộc phải ngắt kết nối và đăng nhập lại (hoặc kích hoạt `SET ROLE`)** thì quyền mới có hiệu lực.
  - Khi thu hồi quyền khỏi Role (`REVOKE SELECT ON emp FROM dev_role;`), toàn bộ người dùng đang nắm giữ Role đó lập tức mất quyền tương ứng.

> **Quy tắc thu hồi quyền qua Role:** Nếu một quyền được cấp thông qua Role, chủ sở hữu **không thể thu hồi trực tiếp từ người dùng** (`REVOKE SELECT ON emp FROM dev_user1;` sẽ lỗi). Bắt buộc phải thu hồi quyền đó ra khỏi Role hoặc thu hồi toàn bộ Role khỏi người dùng (`REVOKE dev_role FROM dev_user1;`).

---

### 4. So sánh WITH GRANT OPTION và WITH ADMIN OPTION

Đây là một trong những câu hỏi phân loại điểm cao kinh điển nhất của môn SQLD:

| Tiêu chí | `WITH GRANT OPTION` | `WITH ADMIN OPTION` |
| --- | --- | --- |
| **Phạm vi áp dụng** | **Chỉ áp dụng cho Quyền đối tượng (Object Privilege)** | **Áp dụng cho Quyền hệ thống (System Privilege) hoặc ROLE** |
| **Bản chất quyền** | Cho phép người được cấp có quyền cấp tiếp quyền đối tượng đó cho người thứ ba. | Cho phép người được cấp có quyền quản trị cấp tiếp quyền hệ thống/Role đó cho người khác. |
| **Hành vi khi thu hồi trung gian (`REVOKE`)** | **Thu hồi dây chuyền (CASCADE REVOKE)**: Nếu User A thu hồi quyền của User B, toàn bộ quyền mà User B đã cấp cho User C **cũng tự động bị thu hồi theo**. | **KHÔNG thu hồi dây chuyền (NO CASCADE)**: Nếu User A thu hồi quyền của User B, quyền mà User B đã cấp cho User C **vẫn được giữ nguyên vẹn**. |

```sql
-- Ví dụ WITH GRANT OPTION (Đối tượng)
-- SCOTT cấp cho USER_A kèm quyền cấp tiếp:
GRANT SELECT ON emp TO user_a WITH GRANT OPTION;
-- USER_A cấp tiếp cho USER_B:
GRANT SELECT ON emp TO user_b;
-- Khi SCOTT thu hồi quyền của USER_A:
REVOKE SELECT ON emp FROM user_a;
-- Kết quả: Cả USER_A và USER_B đều bị mất quyền SELECT trên bảng emp!

-- Ví dụ WITH ADMIN OPTION (Hệ thống / Role)
-- SYSTEM cấp quyền CREATE TABLE cho USER_A kèm quyền quản trị:
GRANT CREATE TABLE TO user_a WITH ADMIN OPTION;
-- USER_A cấp tiếp cho USER_B:
GRANT CREATE TABLE TO user_b;
-- Khi SYSTEM thu hồi quyền của USER_A:
REVOKE CREATE TABLE FROM user_a;
-- Kết quả: USER_A mất quyền, nhưng USER_B VẪN GIỮ NGUYÊN quyền CREATE TABLE!
```

---

## 5. Nối mạch sang Bài tiếp theo: PIVOT, UNPIVOT và Regular Expression

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 12 đã khép lại toàn bộ hệ thống quản trị an ninh dữ liệu và phân quyền DCL.
> - **Đang giải quyết gì:** Trong phân tích dữ liệu và báo cáo nghiệp vụ chuyên sâu, dữ liệu thường được lưu ở dạng dọc (Long format) nhưng người dùng cần xoay thành bảng chéo ngang (Wide format), hoặc cần lọc chuỗi theo các quy tắc mẫu phức tạp.
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 13 — PIVOT, UNPIVOT và Regular Expression](./13-pivot-unpivot-va-regexp.md) để học kỹ thuật xoay trục dữ liệu ANSI/Oracle và các hàm tìm kiếm khớp mẫu `REGEXP_*`.
