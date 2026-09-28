# DCL, quyền và Role

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 100–103.
>
> **Liên kết bài trước:** bảng (table / 테이블), view, chuỗi (sequence / 시퀀스) và synonym là các đối tượng (object / 객체) cần được bảo vệ. DCL xác định tài khoản nào có thể làm gì với từng đối tượng (object / 객체) hoặc với hệ thống.

## 1. DCL (Data Control Language) (ngôn ngữ điều khiển dữ liệu)

> **KR:** DCL은 객체에 대한 권한을 부여(GRANT)하거나 권한을 회수(REVOKE)하는 데이터 제어어이다.

DCL quản lý privilege (Privilege) (quyền). Chủ sở hữu bảng (table / 테이블) có thể cấp/thu hồi quyền truy vấn và sửa dữ liệu cho tài khoản khác; quyền trên đối tượng (object / 객체) khác với quyền quản trị hệ thống. Hai lệnh cốt lõi là `GRANT` (Grant) (cấp quyền) và `REVOKE` (Revoke) (thu hồi quyền).

## 2. 권한 (Privilege) (quyền)

> **KR:** 본인 소유가 아닌 테이블은 원칙적으로 조회 불가하며, 필요 시 소유자가 다른 계정에 조회·수정 권한을 부여한다.

Một người dùng (user / 사용자) (User) (tài khoản) không mặc nhiên truy vấn bảng không do mình sở hữu. đối tượng (object / 객체) privilege (Object Privilege) (quyền đối tượng) kiểm soát hành động với bảng cụ thể: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`. hệ thống (system / 시스템) privilege (System Privilege) (quyền hệ thống) kiểm soát tác vụ hệ thống/DDL, ví dụ `CREATE TABLE` hoặc `DROP ANY TABLE`; PDF nêu chỉ administrator (Administrator) (quản trị viên) có thể cấp/thu hồi hệ thống (system / 시스템) privilege.

Oracle minh họa `SCOTT` là người dùng (user / 사용자) mẫu, `SYS` là tài khoản có DBA role và `SYSTEM` là tài khoản DBA được cấu hình khi cài đặt. Với SQL máy chủ (server / 서버), đối tượng (object / 객체) thuộc lược đồ (schema / 스키마) (Schema) (lược đồ), không trực tiếp thuộc người dùng (user / 사용자): `dbo.table_name` có `dbo` là lược đồ (schema / 스키마); người dùng (user / 사용자) cần quyền trên đối tượng (object / 객체) thuộc lược đồ (schema / 스키마) đó.

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

Không gộp nhiều đối tượng (object / 객체) trong cùng một GRANT đối tượng (object / 객체) privilege theo ví dụ PDF; hãy cấp theo từng đối tượng (object / 객체). Trong SQL máy chủ (server / 서버), hình thức ý tưởng là `GRANT SELECT ON schema_name.table_name TO user_name`.

## 4. REVOKE (Revoke) (thu hồi quyền)

> **KR:** REVOKE는 동시에 여러 권한 또는 여러 유저로부터 권한을 회수할 수 있지만, 이미 회수된 권한을 재회수할 수 없다.

```sql
REVOKE SELECT, UPDATE, INSERT ON emp FROM a;
REVOKE SELECT ON emp FROM a, b;
```

Tương tự GRANT, không thu hồi nhiều đối tượng (object / 객체) trong một lệnh đối tượng (object / 객체) privilege theo ví dụ PDF. Sau khi quyền đã bị thu hồi, cố thu hồi cùng quyền đó lần nữa là lỗi; đây là chi tiết dễ bị hỏi khi đọc lựa chọn đúng/sai.

## 5. ROLE (Role) (vai trò)

> **KR:** ROLE은 사용자와 권한 사이에서 중개 역할을 하며 다양한 권한의 묶음이다.

Role gom nhiều quyền thành một gói để tránh cấp từng quyền lặp lại cho nhiều người dùng (user / 사용자). DBA tạo role, cấp đối tượng (object / 객체)/hệ thống (system / 시스템) privilege cho role, rồi cấp role cho người dùng (user / 사용자) hoặc role khác. Khi số người dùng tăng, role giảm công sức vận hành và làm chính sách quyền nhất quán hơn.

```sql
CREATE ROLE role1;
GRANT SELECT ON emp TO role1;
GRANT SELECT ON dept TO role1;
GRANT role1 TO a;
```

> **KR:** 직접 부여된 권한은 즉시 반영되지만 ROLE은 재접속해야 권한이 부여된다.

Theo PDF, quyền cấp trực tiếp phản ánh ngay trong session đang kết nối; role cần đăng nhập lại để nhận hiệu lực. Khi thu hồi một quyền khỏi role, các người dùng (user / 사용자) có role đó mất quyền tương ứng ngay và không cần cấp lại role.

## 6. 역할을 통한 권한 회수 (thu hồi quyền qua role)

> **KR:** ROLE을 통해 부여한 권한은 직접 회수할 수 없고 ROLE을 통한 회수만 가능하다.

Nếu `A` nhận `SELECT ON EMP` qua `ROLE1`, không được `REVOKE SELECT ON EMP FROM A` trực tiếp từ người sở hữu đối tượng (object / 객체); phải `REVOKE SELECT ON EMP FROM ROLE1`. Đây là hệ quả lô-gic (logic / 논리) của nguồn quyền: quyền cần được thu hồi ở đúng “đường” mà nó được cấp.

## 7. WITH GRANT OPTION và WITH ADMIN OPTION

> **KR:** WITH GRANT OPTION은 오브젝트 권한을 다른 사용자에게 부여할 수 있게 하고, WITH ADMIN OPTION은 시스템 권한 또는 ROLE 권한을 부여할 수 있게 한다.

`WITH GRANT OPTION` (Grant Option) (quyền cấp tiếp quyền đối tượng) áp dụng cho đối tượng (object / 객체) privilege. `WITH ADMIN OPTION` (Admin Option) (quyền cấp tiếp quyền hệ thống/role) áp dụng cho hệ thống (system / 시스템) privilege hoặc role. Cả hai tạo “trung gian quản trị”, nhưng quy tắc thu hồi khác nhau.

| Tùy chọn | Dùng cho | Khi thu hồi quyền của người trung gian |
| --- | --- | --- |
| `WITH GRANT OPTION` | đối tượng (object / 객체) privilege | Quyền mà trung gian đã cấp cho người thứ ba cũng bị thu hồi theo. |
| `WITH ADMIN OPTION` | hệ thống (system / 시스템) privilege hoặc role | Có thể thu hồi trực tiếp từ trung gian; quyền trung gian đã cấp cho người thứ ba vẫn còn. |

Ví dụ PDF: `lee` cấp đối tượng (object / 객체) privilege cho `kim` bằng `WITH GRANT OPTION`, rồi `kim` cấp DML cho `park`; khi `lee` thu hồi quyền của `kim`, quyền của `park` cũng mất. Nếu `lee` cấp hệ thống (system / 시스템) privilege bằng `WITH ADMIN OPTION`, `kim` cấp DDL cho `park`; khi thu hồi `kim`, quyền của `park` vẫn giữ. Hãy luôn xác định đề đang nói về đối tượng (object / 객체) hay hệ thống (system / 시스템)/role trước khi suy ra kết quả thu hồi.
