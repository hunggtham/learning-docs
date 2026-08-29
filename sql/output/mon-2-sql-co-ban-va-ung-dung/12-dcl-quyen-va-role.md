# DCL, quyền và Role

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 100–103.
>
> **Liên kết bài trước:** Table, view, sequence và synonym là các object cần được bảo vệ. DCL xác định tài khoản nào có thể làm gì với từng object hoặc với hệ thống.

## 1. DCL (Data Control Language) (ngôn ngữ điều khiển dữ liệu)

> **KR:** DCL은 객체에 대한 권한을 부여(GRANT)하거나 권한을 회수(REVOKE)하는 데이터 제어어이다.

DCL quản lý privilege (Privilege) (quyền). Chủ sở hữu table có thể cấp/thu hồi quyền truy vấn và sửa dữ liệu cho tài khoản khác; quyền trên object khác với quyền quản trị hệ thống. Hai lệnh cốt lõi là `GRANT` (Grant) (cấp quyền) và `REVOKE` (Revoke) (thu hồi quyền).

## 2. 권한 (Privilege) (quyền)

> **KR:** 본인 소유가 아닌 테이블은 원칙적으로 조회 불가하며, 필요 시 소유자가 다른 계정에 조회·수정 권한을 부여한다.

Một user (User) (tài khoản) không mặc nhiên truy vấn bảng không do mình sở hữu. Object privilege (Object Privilege) (quyền đối tượng) kiểm soát hành động với bảng cụ thể: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`. System privilege (System Privilege) (quyền hệ thống) kiểm soát tác vụ hệ thống/DDL, ví dụ `CREATE TABLE` hoặc `DROP ANY TABLE`; PDF nêu chỉ administrator (Administrator) (quản trị viên) có thể cấp/thu hồi system privilege.

Oracle minh họa `SCOTT` là user mẫu, `SYS` là tài khoản có DBA role và `SYSTEM` là tài khoản DBA được cấu hình khi cài đặt. Với SQL Server, object thuộc schema (Schema) (lược đồ), không trực tiếp thuộc user: `dbo.table_name` có `dbo` là schema; user cần quyền trên object thuộc schema đó.

## 3. GRANT (Grant) (cấp quyền)

> **KR:** 권한 부여 시 반드시 테이블 소유자나 관리자 계정으로 접속해야 하며 여러 유저 또는 여러 권한을 동시에 부여할 수 있다.

```sql
-- Object privilege: một object, nhiều quyền hoặc nhiều user
GRANT SELECT ON emp TO a;
GRANT SELECT ON emp TO a, b;
GRANT SELECT, UPDATE, INSERT ON emp TO b;

-- System privilege: do quản trị viên thực hiện
GRANT CREATE TABLE TO a;
GRANT CREATE TABLE, DROP ANY TABLE TO a;
```

Không gộp nhiều object trong cùng một GRANT object privilege theo ví dụ PDF; hãy cấp theo từng object. Trong SQL Server, hình thức ý tưởng là `GRANT SELECT ON schema_name.table_name TO user_name`.

## 4. REVOKE (Revoke) (thu hồi quyền)

> **KR:** REVOKE는 동시에 여러 권한 또는 여러 유저로부터 권한을 회수할 수 있지만, 이미 회수된 권한을 재회수할 수 없다.

```sql
REVOKE SELECT, UPDATE, INSERT ON emp FROM a;
REVOKE SELECT ON emp FROM a, b;
```

Tương tự GRANT, không thu hồi nhiều object trong một lệnh object privilege theo ví dụ PDF. Sau khi quyền đã bị thu hồi, cố thu hồi cùng quyền đó lần nữa là lỗi; đây là chi tiết dễ bị hỏi khi đọc lựa chọn đúng/sai.

## 5. ROLE (Role) (vai trò)

> **KR:** ROLE은 사용자와 권한 사이에서 중개 역할을 하며 다양한 권한의 묶음이다.

Role gom nhiều quyền thành một gói để tránh cấp từng quyền lặp lại cho nhiều user. DBA tạo role, cấp object/system privilege cho role, rồi cấp role cho user hoặc role khác. Khi số người dùng tăng, role giảm công sức vận hành và làm chính sách quyền nhất quán hơn.

```sql
CREATE ROLE role1;
GRANT SELECT ON emp TO role1;
GRANT SELECT ON dept TO role1;
GRANT role1 TO a;
```

> **KR:** 직접 부여된 권한은 즉시 반영되지만 ROLE은 재접속해야 권한이 부여된다.

Theo PDF, quyền cấp trực tiếp phản ánh ngay trong session đang kết nối; role cần đăng nhập lại để nhận hiệu lực. Khi thu hồi một quyền khỏi role, các user có role đó mất quyền tương ứng ngay và không cần cấp lại role.

## 6. 역할을 통한 권한 회수 (thu hồi quyền qua role)

> **KR:** ROLE을 통해 부여한 권한은 직접 회수할 수 없고 ROLE을 통한 회수만 가능하다.

Nếu `A` nhận `SELECT ON EMP` qua `ROLE1`, không được `REVOKE SELECT ON EMP FROM A` trực tiếp từ người sở hữu object; phải `REVOKE SELECT ON EMP FROM ROLE1`. Đây là hệ quả logic của nguồn quyền: quyền cần được thu hồi ở đúng “đường” mà nó được cấp.

## 7. WITH GRANT OPTION và WITH ADMIN OPTION

> **KR:** WITH GRANT OPTION은 오브젝트 권한을 다른 사용자에게 부여할 수 있게 하고, WITH ADMIN OPTION은 시스템 권한 또는 ROLE 권한을 부여할 수 있게 한다.

`WITH GRANT OPTION` (Grant Option) (quyền cấp tiếp quyền đối tượng) áp dụng cho object privilege. `WITH ADMIN OPTION` (Admin Option) (quyền cấp tiếp quyền hệ thống/role) áp dụng cho system privilege hoặc role. Cả hai tạo “trung gian quản trị”, nhưng quy tắc thu hồi khác nhau.

| Tùy chọn | Dùng cho | Khi thu hồi quyền của người trung gian |
| --- | --- | --- |
| `WITH GRANT OPTION` | Object privilege | Quyền mà trung gian đã cấp cho người thứ ba cũng bị thu hồi theo. |
| `WITH ADMIN OPTION` | System privilege hoặc role | Có thể thu hồi trực tiếp từ trung gian; quyền trung gian đã cấp cho người thứ ba vẫn còn. |

Ví dụ PDF: `lee` cấp object privilege cho `kim` bằng `WITH GRANT OPTION`, rồi `kim` cấp DML cho `park`; khi `lee` thu hồi quyền của `kim`, quyền của `park` cũng mất. Nếu `lee` cấp system privilege bằng `WITH ADMIN OPTION`, `kim` cấp DDL cho `park`; khi thu hồi `kim`, quyền của `park` vẫn giữ. Hãy luôn xác định đề đang nói về object hay system/role trước khi suy ra kết quả thu hồi.
