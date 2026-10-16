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

#### Sơ đồ ASCII trực quan hóa cơ chế CASCADE REVOKE

```text
1. TRƯỜNG HỢP WITH GRANT OPTION (Object Privilege):
   [Lee (Owner)] --- (cấp SELECT kèm GRANT OPTION) ---> [Kim] --- (cấp SELECT) ---> [Park]
         |
         X (Lee REVOKE Kim)
         |
         v
   [Kim bị thu hồi] ======= (TỰ ĐỘNG CASCADE) ======> [Park cũng BỊ THU HỒI]

2. TRƯỜNG HỢP WITH ADMIN OPTION (System Privilege / Role):
   [Lee (DBA)] --- (cấp CREATE TABLE kèm ADMIN OPTION) ---> [Kim] --- (cấp CREATE TABLE) ---> [Park]
         |
         X (Lee REVOKE Kim)
         |
         v
   [Kim bị thu hồi]    x x x (KHÔNG CASCADE) x x x    [Park VẪN GIỮ NGUYÊN QUYỀN]
```

---

## 5. Bảng ma trận so sánh Oracle vs SQL Server về DCL và Phân quyền

| Tiêu chí bảo mật | Oracle Database | Microsoft SQL Server | Điểm khác biệt thi cử SQLD |
| :--- | :--- | :--- | :--- |
| **Phân loại quyền** | Quyền hệ thống (System) và Quyền đối tượng (Object) | Server-level, Database-level và Schema/Object-level | Phân biệt rõ quyền trên toàn hệ thống vs quyền trên từng bảng cụ thể. |
| **Cấp quyền quản trị hệ thống** | `WITH ADMIN OPTION` | `WITH GRANT OPTION` (dùng chung cho mọi cấp độ) | Đề thi SQLD kiểm tra rất kỹ từ khóa `WITH ADMIN OPTION` của Oracle. |
| **Cấp quyền đối tượng cấp tiếp** | `WITH GRANT OPTION` | `WITH GRANT OPTION` | Cả hai đều kích hoạt thu hồi dây chuyền (`CASCADE`). |
| **Cú pháp thu hồi dây chuyền** | Tự động CASCADE khi thu hồi quyền đối tượng | Bắt buộc phải thêm từ khóa `CASCADE`: `REVOKE ... CASCADE` | Oracle tự động dây chuyền, SQL Server yêu cầu mệnh đề rõ ràng. |
| **Cấp quyền trên danh sách cột** | `GRANT UPDATE (col) ON emp TO user` | `GRANT UPDATE ON emp(col) TO user` | Cả hai đều hỗ trợ phân quyền chi tiết tới cấp cột (Column-level security). |
| **Quyền REFERENCES qua Role** | **Bị cấm hoàn toàn** (chỉ cấp trực tiếp cho User) | Hỗ trợ cấp thông qua Role | Bẫy lý thuyết kinh điển của Oracle SQLD. |
| **Kích hoạt Role trong phiên** | Có hiệu lực khi đăng nhập lại hoặc dùng `SET ROLE` | Role có hiệu lực ngay lập tức trong phiên | Quyền cấp trực tiếp có hiệu lực ngay; cấp qua Role cần active trong phiên. |

---

## 6. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

> [!WARNING]
> Dưới đây là 5 cạm bẫy "bẫy điểm" phổ biến nhất về DCL và Phân quyền:

### Cạm bẫy 1: Nhầm lẫn cơ chế CASCADE giữa `WITH GRANT OPTION` và `WITH ADMIN OPTION`
- **Quy tắc vàng:**
  - `WITH GRANT OPTION` (Object Privilege): **CÓ CASCADE** (dây chuyền). Trung gian mất quyền $\rightarrow$ Người được trung gian cấp cũng mất quyền sạch sẽ.
  - `WITH ADMIN OPTION` (System Privilege / Role): **KHÔNG CASCADE** (độc lập). Trung gian mất quyền $\rightarrow$ Người được trung gian cấp vẫn an toàn giữ nguyên quyền.

### Cạm bẫy 2: Lỗi cú pháp khi chỉ định nhiều đối tượng trong mệnh đề `ON`
- **Hợp lệ:**
  - Cấp nhiều quyền cho 1 người: `GRANT SELECT, INSERT ON emp TO user_a;`
  - Cấp 1 quyền cho nhiều người: `GRANT SELECT ON emp TO user_a, user_b;`
- **BẤY SAI CÚ PHÁP:**
  - Cấp quyền trên nhiều bảng cùng lúc: `GRANT SELECT ON emp, dept TO user_a;`
  - **LỖI:** Mệnh đề `ON` đối tượng chỉ được phép chứa duy nhất **1 tên bảng/view/đối tượng**! Muốn cấp nhiều bảng phải viết thành từng câu lệnh riêng biệt.

### Cạm bẫy 3: Cố gắng thu hồi quyền đối tượng vượt cấp
- Trong chuỗi: `A (Owner)` $\rightarrow$ cấp cho `B` (với `GRANT OPTION`) $\rightarrow$ `B` cấp tiếp cho `C`.
- **Hỏi:** `A` có thể phát lệnh `REVOKE SELECT ON emp FROM C;` được không?
- **Trả lời:** **KHÔNG THỂ!** Hệ thống sẽ báo lỗi. `A` chỉ có quyền thu hồi từ `B`. Nếu muốn tước quyền của `C`, `A` phải thu hồi quyền của `B` (để cơ chế CASCADE tự động kéo theo `C`), hoặc yêu cầu chính `B` thực hiện lệnh thu hồi đối với `C`.

### Cạm bẫy 4: Quyền tạo khóa ngoại `REFERENCES` không thể cấp thông qua ROLE
- Khi lập trình viên muốn tạo một bảng con có khóa ngoại tham chiếu đến bảng của schema khác:
  ```sql
  -- LỖI NẾU CẤP QUA ROLE:
  GRANT REFERENCES ON dept TO dev_role; -- Sẽ bị từ chối khi tạo FK!
  ```
- **Quy tắc Oracle:** Quyền `REFERENCES` tiềm ẩn nguy cơ khóa chặt bảng cha (ngăn chặn thao tác xóa bảng, xóa dòng). Do đó Oracle bắt buộc quyền này phải được cấp **trực tiếp cho User** (`GRANT REFERENCES ON dept TO dev_user;`), tuyệt đối không cho phép kế thừa gián tiếp qua Role.

### Cạm bẫy 5: Thu hồi quyền cá nhân khi quyền đó nằm trong ROLE
- Người dùng `user_a` được gán `dev_role`, trong đó `dev_role` có quyền `SELECT ON emp`.
- Quản trị viên muốn tước quyền xem bảng của riêng `user_a` nên gõ:
  ```sql
  REVOKE SELECT ON emp FROM user_a;
  ```
- **LỖI ORA-01927:** Cannot REVOKE privileges you did not grant!
- Vì quyền này được cấp cho Role chứ không phải cấp riêng lẻ cho `user_a`. Muốn tước quyền, DBA bắt buộc phải thu hồi toàn bộ Role (`REVOKE dev_role FROM user_a;`) hoặc rút quyền đó ra khỏi Role.

---

## 7. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1: Chuỗi thu hồi quyền đối tượng WITH GRANT OPTION (Độ khó: Trung bình)
Người dùng `USER_A` là chủ sở hữu bảng `EMPLOYEES`. Các thao tác phân quyền được thực hiện tuần tự như sau:
1. `USER_A`: `GRANT SELECT ON EMPLOYEES TO USER_B WITH GRANT OPTION;`
2. `USER_B`: `GRANT SELECT ON EMPLOYEES TO USER_C;`
3. `USER_A`: `REVOKE SELECT ON EMPLOYEES FROM USER_B;`

Hỏi sau bước 3, quyền `SELECT` trên bảng `EMPLOYEES` của `USER_B` và `USER_C` như thế nào?

A. Cả `USER_B` và `USER_C` đều bị mất quyền `SELECT`.
B. `USER_B` bị mất quyền, nhưng `USER_C` vẫn giữ nguyên quyền `SELECT`.
C. Lệnh ở bước 3 bị lỗi do `USER_B` đã cấp quyền cho `USER_C`.
D. `USER_B` vẫn giữ quyền, chỉ có quyền ủy quyền tiếp của `USER_B` bị hủy.

> **Đáp án chính xác:** **A**
>
> **Giải thích chi tiết từng lựa chọn:**
> - Quyền `SELECT ON EMPLOYEES` là **Quyền đối tượng (Object Privilege)** được cấp kèm tùy chọn `WITH GRANT OPTION`.
> - Theo nguyên lý của cơ sở dữ liệu quan hệ, quan hệ ủy quyền đối tượng phụ thuộc chặt chẽ theo chuỗi phân cấp (Dependency Tree).
> - Khi `USER_A` thu hồi quyền từ `USER_B`, hệ thống Oracle sẽ tự động kích hoạt cơ chế **CASCADE REVOKE** (thu hồi dây chuyền). Tất cả các tài khoản nhận quyền gián tiếp từ `USER_B` (trong đó có `USER_C`) đều bị thu hồi toàn bộ quyền tương ứng.
> - Do đó cả `USER_B` và `USER_C` đều không còn quyền `SELECT`.
> - **Lựa chọn A:** Hoàn toàn chính xác.
> - **Lựa chọn B sai:** Nhầm lẫn với cơ chế NO CASCADE của WITH ADMIN OPTION.
> - **Lựa chọn C sai:** Chủ sở hữu bảng luôn có quyền thu hồi bất cứ lúc nào.
> - **Lựa chọn D sai:** Lệnh REVOKE thu hồi toàn bộ quyền chứ không chỉ thu hồi option.

---

### Câu 2: Chuỗi thu hồi quyền hệ thống WITH ADMIN OPTION (Độ khó: Trung bình)
Quản trị viên `DBA_USER` thực hiện cấp phát quyền hệ thống theo trình tự sau:
1. `DBA_USER`: `GRANT CREATE TABLE TO USER_X WITH ADMIN OPTION;`
2. `USER_X`: `GRANT CREATE TABLE TO USER_Y;`
3. `DBA_USER`: `REVOKE CREATE TABLE FROM USER_X;`

Sau bước 3, quyền `CREATE TABLE` của `USER_Y` sẽ ở trạng thái nào?

A. `USER_Y` bị mất quyền `CREATE TABLE` do cơ chế thu hồi dây chuyền.
B. `USER_Y` vẫn giữ nguyên quyền `CREATE TABLE`.
C. Câu lệnh ở bước 2 bị lỗi cú pháp vì `USER_X` không phải là DBA.
D. Cả `USER_X` và `USER_Y` đều bị khóa tài khoản tạm thời.

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - Quyền `CREATE TABLE` là **Quyền hệ thống (System Privilege)** được cấp với tùy chọn `WITH ADMIN OPTION`.
> - Đặc tính kỹ thuật của `WITH ADMIN OPTION`: Quyền sau khi được cấp phát tiếp sẽ trở nên hoàn toàn độc lập với người đã cấp nó cho mình.
> - Cơ chế thu hồi quyền hệ thống là **KHÔNG DÂY CHUYỀN (NO CASCADE)**.
> - Khi `DBA_USER` thu hồi quyền `CREATE TABLE` từ `USER_X`, chỉ có `USER_X` bị mất quyền; quyền của `USER_Y` hoàn toàn không bị ảnh hưởng và vẫn hoạt động bình thường!
> - **Lựa chọn B:** Hoàn toàn chính xác.
> - **Lựa chọn A sai:** Nhầm sang cơ chế CASCADE của quyền đối tượng WITH GRANT OPTION.
> - **Lựa chọn C sai:** Có ADMIN OPTION thì người dùng hoàn toàn có quyền cấp phát tiếp.
> - **Lựa chọn D sai:** Lệnh REVOKE không hề khóa tài khoản người dùng.

---

### Câu 3: Quy tắc cú pháp của câu lệnh DCL (Độ khó: Dễ)
Câu lệnh `GRANT` nào dưới đây sẽ **GÂY RA LỖI CÚ PHÁP** khi thực thi trong Oracle SQL?

A. `GRANT CREATE SESSION, CREATE TABLE TO DEV_USER1, DEV_USER2;`
B. `GRANT SELECT, UPDATE ON EMP TO DEV_USER1;`
C. `GRANT SELECT ON EMP, DEPT TO DEV_USER1;`
D. `GRANT UPDATE (SAL, COMM) ON EMP TO DEV_USER1;`

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Lựa chọn C:** Trong câu lệnh cấp quyền đối tượng, mệnh đề `ON` chỉ cho phép khai báo duy nhất **1 đối tượng CSDL** (bảng, view). Việc liệt kê danh sách nhiều bảng ngăn cách bởi dấu phẩy `ON EMP, DEPT` là sai cú pháp và ném lỗi `ORA-00990: missing or invalid privilege`.
> - **Lựa chọn A hợp lệ:** Cho phép cấp đồng thời nhiều quyền hệ thống cho nhiều tài khoản.
> - **Lựa chọn B hợp lệ:** Cho phép cấp đồng thời nhiều thao tác (`SELECT`, `UPDATE`) trên 1 bảng cho 1 tài khoản.
> - **Lựa chọn D hợp lệ:** Cho phép chỉ định danh sách cột được phép cập nhật `UPDATE (col1, col2)`.

---

### Câu 4: Đặc tính kỹ thuật của đối tượng ROLE (Độ khó: Cao)
Phát biểu nào sau đây là **KHÔNG CHÍNH XÁC** khi nói về `ROLE` trong hệ quản trị cơ sở dữ liệu?

A. Một `ROLE` có thể chứa đồng thời cả quyền hệ thống (System Privilege) lẫn quyền đối tượng (Object Privilege).
B. Một `ROLE` có thể được gán cho một `ROLE` khác để xây dựng mô hình phân quyền phân cấp.
C. Quyền tạo khóa ngoại `REFERENCES` trên bảng của người khác có thể được cấp phát an toàn thông qua `ROLE`.
D. Để kích hoạt các quyền được cấp thông qua `ROLE`, người dùng có thể cần thực hiện lệnh `SET ROLE` hoặc đăng nhập lại phiên mới.

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Lựa chọn C không chính xác (Là đáp án được chọn):** Theo quy định bảo mật nghiêm ngặt của Oracle, quyền `REFERENCES` (cho phép tạo ràng buộc khóa ngoại tham chiếu) **bắt buộc phải được cấp trực tiếp cho User**, tuyệt đối không thể cấp thông qua `ROLE`!
> - **Lựa chọn A đúng:** Role là túi chứa quyền tổng hợp, có thể gộp cả `CREATE TABLE` (System) lẫn `SELECT ON EMP` (Object).
> - **Lựa chọn B đúng:** Oracle hỗ trợ gán Role lồng Role (`GRANT role_a TO role_b;`).
> - **Lựa chọn D đúng:** Quyền gán trực tiếp có tác dụng ngay, nhưng quyền cấp qua Role có thể đòi hỏi active session hoặc re-login.

---

## 8. Nối mạch sang Bài tiếp theo: PIVOT, UNPIVOT và Regular Expression

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 12 đã hoàn thiện toàn bộ hệ thống quản trị an ninh dữ liệu, phân loại Quyền hệ thống vs Quyền đối tượng, cơ chế CASCADE của `WITH GRANT OPTION` vs `WITH ADMIN OPTION` và những giới hạn bảo mật của `ROLE`.
> - **Đang giải quyết gì:** Trong khai thác báo cáo nghiệp vụ và phân tích dữ liệu, dữ liệu chuẩn thường được lưu ở dạng dọc (Long format) nhưng người dùng đòi hỏi xoay thành ma trận chéo ngang (Wide format), hoặc cần kiểm tra lọc chuỗi theo biểu thức chính quy phức tạp?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 13 — PIVOT, UNPIVOT và Regular Expression](./13-pivot-unpivot-va-regexp.md) để học kỹ thuật xoay trục dữ liệu nâng cao (PIVOT nhiều cột/nhiều hàm, xử lý NULL trong UNPIVOT) và bộ 5 hàm `REGEXP_*` của Oracle.
