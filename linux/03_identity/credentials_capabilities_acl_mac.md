# Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kernel kiểm tra ai đang thực hiện thao tác bằng cách nào?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Real UID và effective UID** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối credentials với UID, capabilities, ACL và MAC, để giải thích quyết định truy cập của kernel theo từng lớp chính sách.

Chương [Người dùng, nhóm, quyền truy cập và đặc quyền](./users_groups_permissions.md) trình bày mô hình quyền cơ bản. Chương này đi sâu vào cách kernel thật sự gắn **credentials** với tiến trình (process / 프로세스), cách quyền được kiểm tra qua UID/GID, ACL, capabilities, không gian tên (namespace / 네임스페이스) và Mandatory kiểm soát truy cập (access control / 접근 제어), cũng như vì sao “chmod 777” vẫn có thể không làm một thao tác thành công.

## Kernel kiểm tra ai đang thực hiện thao tác bằng cách nào?

Kernel không hỏi “người dùng đăng nhập tên gì?” theo nghĩa giao diện. Nó nhìn **credentials của tiến trình (process / 프로세스)**.

Một tiến trình (process / 프로세스) có nhiều định danh (identity / 식별자) fields hơn chỉ một UID:

- real UID;
- effective UID;
- saved set-user-ID;
- real/effective/saved GID;
- supplementary groups;
- capabilities;
- người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) ngữ cảnh (context / 맥락);
- bảo mật (security / 보안) labels tùy SELinux/AppArmor.

Có thể quan sát một phần:

```bash
cat /proc/<PID>/status | grep -E 'Uid|Gid|Groups|Cap'
```

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Real UID và effective UID** tiếp nhận điểm tựa từ **Kernel kiểm tra ai đang thực hiện thao tác bằng cách nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Saved UID** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Real UID và effective UID

**Real UID** thường phản ánh người dùng (user / 사용자) khởi tạo tiến trình (process / 프로세스).

**Effective UID** là định danh (identity / 식별자) kernel thường dùng cho nhiều kiểm tra quyền filesystem.

Setuid nhị phân (binary / 이진) tồn tại chính vì hai giá trị này có thể khác nhau.

Ví dụ `passwd` cần cập nhật dữ liệu mà người dùng (user / 사용자) bình thường không thể ghi trực tiếp. nhị phân (binary / 이진) có thể chạy với effective privilege cao hơn trong phạm vi mã (code / 코드) được kiểm soát.

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Saved UID** tiếp nhận điểm tựa từ **Real UID và effective UID** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Supplementary groups** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Saved UID

Saved set-user-ID cho phép một tiến trình (process / 프로세스) tạm drop privilege rồi có thể lấy lại trong những điều kiện nhất định.

Đây là mẫu (pattern / 패턴) phổ biến trong daemon truyền thống:

```text
start với privilege cao
→ mở resource đặc quyền
→ drop privilege
→ xử lý request bằng user ít quyền hơn
```

Thiết kế này giảm blast radius nếu phần xử lý yêu cầu (request / 요청) có bug.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Supplementary groups** tiếp nhận điểm tựa từ **Saved UID** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Credential inheritance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Supplementary groups

Một tiến trình (process / 프로세스) có thể thuộc nhiều group ngoài primary GID.

```bash
id appuser
```

Khi systemd khởi chạy dịch vụ (service / 서비스), groups có thể khác phiên SSH của bạn.

```bash
cat /proc/<PID>/status | grep Groups
```

Nếu permission dựa vào group nhưng tiến trình (process / 프로세스) không thật sự có group đó, `ls -l` nhìn tệp (file / 파일) đúng vẫn không giúp.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Credential inheritance** tiếp nhận điểm tựa từ **Supplementary groups** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **sudo thực sự làm gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Credential inheritance

Child tiến trình (process / 프로세스) thường kế thừa credentials từ parent, sau đó có thể thay đổi theo API/chính sách (policy / 정책).

Đây là lý do shell, sudo, systemd và bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) đều quan trọng: chúng quyết định credentials của tiến trình (process / 프로세스) cuối cùng.

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **sudo thực sự làm gì?** tiếp nhận điểm tựa từ **Credential inheritance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **su và sudo -i khác nhau về ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `sudo` thực sự làm gì?

`sudo` đọc chính sách (policy / 정책) rồi chạy command dưới mục tiêu (target / 대상) định danh (identity / 식별자).

Nó không chỉ “thêm gốc (root / 루트)”. Nó có thể:

- chọn mục tiêu (target / 대상) người dùng (user / 사용자);
- đặt môi trường (environment / 환경);
- ghi kiểm tra (audit / 감사)/log;
- giới hạn command;
- yêu cầu authentication;
- thay group ngữ cảnh (context / 맥락).

Kiểm tra chính sách (policy / 정책) được phép:

```bash
sudo -l
```

`sudoers` quá rộng như:

```text
ALL=(ALL) NOPASSWD: ALL
```

thực tế gần như trao full gốc (root / 루트) năng lực (capability / 역량) cho account đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **su và sudo -i khác nhau về ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **sudo thực sự làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Permission check trên pathname** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `su` và `sudo -i` khác nhau về ngữ cảnh (context / 맥락)

`su`, `su -`, `sudo -u`, `sudo -i` tạo môi trường (environment / 환경)/login ngữ nghĩa (semantics / 의미론) khác nhau.

Một command chạy thành công dưới `sudo -i` không chứng minh dịch vụ (service / 서비스) account có quyền tương tự.

Khi gỡ lỗi (debug / 디버그) nên tái hiện đúng định danh (identity / 식별자):

```bash
sudo -u appuser -- /usr/bin/test -r /opt/app/config.yml
```

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **su và sudo -i khác nhau về ngữ cảnh (context / 맥락)** xác định đầu vào; **Permission check trên pathname** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **ACL mask** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Permission check trên pathname

Để đọc:

```text
/a/b/c.txt
```

kernel cần traverse `/`, `/a`, `/a/b` và cuối cùng kiểm tra đối tượng (object / 객체) `c.txt`.

Execute bit trên directory mang nghĩa **tìm kiếm (search / 검색)/traverse**, không phải “chạy folder”.

Dùng:

```bash
namei -l /a/b/c.txt
```

để thấy permission từng thành phần (component / 컴포넌트).

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Permission check trên pathname** xác định đầu vào; **ACL mask** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Default ACL trên directory** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ACL mask

POSIX ACL có một khái niệm dễ gây nhầm: **mask**.

Ví dụ:

```bash
getfacl file.txt
```

có thể thấy:

```text
user::rw-
user:deploy:rw-
group::r--
mask::r--
other::---
```

Dù entry `deploy` là `rw-`, mask chỉ `r--`, nên effective permission có thể chỉ còn read.

Đây là lý do `getfacl` đôi khi hiển thị comment `#effective:r--`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Default ACL trên directory** tiếp nhận điểm tựa từ **ACL mask** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Setgid trên directory** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Default ACL trên directory

Directory có thể có **default ACL** để tệp (file / 파일)/subdirectory mới kế thừa chính sách (policy / 정책).

```bash
setfacl -d -m g:appops:rwx /srv/shared
```

Điều này hữu ích cho thư mục chia sẻ nhiều dịch vụ (service / 서비스)/người dùng (user / 사용자).

Nhưng ACL inheritance phức tạp hơn chế độ (mode / 모드) bits đơn giản; cần document rõ để tránh chính sách (policy / 정책) “ẩn”.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Setgid trên directory** tiếp nhận điểm tựa từ **Default ACL trên directory** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sticky bit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Setgid trên directory

Nếu directory có setgid bit:

```bash
chmod g+s /srv/shared
```

Tệp (file / 파일) mới thường kế thừa group của directory thay vì primary group của tiến trình (process / 프로세스), tùy filesystem ngữ nghĩa (semantics / 의미론).

Đây là mẫu (pattern / 패턴) tốt cho dùng chung (shared / 공유) workspace.

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Sticky bit** tiếp nhận điểm tựa từ **Setgid trên directory** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Setuid và setgid nhị phân (binary / 이진)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sticky bit

Trên directory writable chung như `/tmp`, sticky bit hạn chế việc người dùng (user / 사용자) xóa tệp (file / 파일) của người khác.

```bash
ls -ld /tmp
```

thường thấy:

```text
drwxrwxrwt
```

Chữ `t` là sticky bit.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Setuid và setgid nhị phân (binary / 이진)** tiếp nhận điểm tựa từ **Sticky bit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Capabilities: chia nhỏ quyền gốc (root / 루트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Setuid và setgid nhị phân (binary / 이진)

Setuid nhị phân (binary / 이진) có thể chạy với effective UID của đơn vị sở hữu (owner / 오너).

Đây là cơ chế quyền rất mạnh và là bề mặt tấn công quan trọng.

Tìm setuid files:

```bash
find / -xdev -perm -4000 -type f 2>/dev/null
```

Không nên xóa tùy tiện vì nhiều hệ thống (system / 시스템) utilities hợp lệ dùng setuid.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Capabilities: chia nhỏ quyền gốc (root / 루트)** tiếp nhận điểm tựa từ **Setuid và setgid nhị phân (binary / 이진)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Năng lực (capability / 역량) sets** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Capabilities: chia nhỏ quyền gốc (root / 루트)

Linux chia một phần đặc quyền gốc (root / 루트) thành **capabilities**.

Ví dụ:

- `CAP_NET_BIND_SERVICE` — bind cổng (port / 포트) thấp;
- `CAP_CHOWN` — thay quyền sở hữu (ownership / 소유권);
- `CAP_SYS_ADMIN` — một năng lực (capability / 역량) cực rộng;
- `CAP_NET_ADMIN` — thay mạng (network / 네트워크) cấu hình (config / 설정);
- `CAP_SYS_PTRACE` — tracing tiến trình (process / 프로세스) trong nhiều tình huống.

Danh sách chính xác phụ thuộc kernel phiên bản (version / 버전).

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Năng lực (capability / 역량) sets** tiếp nhận điểm tựa từ **Capabilities: chia nhỏ quyền gốc (root / 루트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tệp (file / 파일) capabilities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lực (capability / 역량) sets

Tiến trình (process / 프로세스) có nhiều tập năng lực (capability / 역량):

- permitted;
- effective;
- inheritable;
- bounding;
- ambient.

Không cần thuộc toàn bộ bitmask ngay, nhưng cần hiểu rằng “tiến trình (process / 프로세스) có năng lực (capability / 역량)” không chỉ là một boolean đơn giản.

Xem:

```bash
capsh --print
```

hoặc:

```bash
getpcaps <PID>
```

nếu công cụ (tool / 도구) có sẵn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Tệp (file / 파일) capabilities** tiếp nhận điểm tựa từ **Năng lực (capability / 역량) sets** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CAPSYSADMIN không phải năng lực (capability / 역량) “nhỏ”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tệp (file / 파일) capabilities

Có thể gắn năng lực (capability / 역량) vào executable:

```bash
sudo setcap cap_net_bind_service=+ep /opt/app/server
getcap /opt/app/server
```

Ứng dụng có thể bind cổng (port / 포트) 80 mà không chạy full gốc (root / 루트).

Nhưng tệp (file / 파일) năng lực (capability / 역량) cũng cần quản lý như privilege-bearing siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **CAPSYSADMIN không phải năng lực (capability / 역량) “nhỏ”** tiếp nhận điểm tựa từ **Tệp (file / 파일) capabilities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bounding set** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `CAP_SYS_ADMIN` không phải năng lực (capability / 역량) “nhỏ”

`CAP_SYS_ADMIN` bao trùm rất nhiều thao tác (operation / 연산) và thường được ví như “new gốc (root / 루트)”.

Nếu mục tiêu là least privilege, tránh cấp nó chỉ vì một permission issue chưa hiểu.

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Bounding set** tiếp nhận điểm tựa từ **CAPSYSADMIN không phải năng lực (capability / 역량) “nhỏ”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ambient capabilities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bounding set

Năng lực (capability / 역량) bounding set giới hạn năng lực (capability / 역량) tiến trình (process / 프로세스) descendants có thể đạt được.

Systemd có:

```ini
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
```

để giảm privilege surface.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Ambient capabilities** tiếp nhận điểm tựa từ **Bounding set** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **nonewprivs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ambient capabilities

Ambient set giúp truyền capabilities qua `execve()` trong một số luồng (flow / 흐름) không setuid.

Systemd có:

```ini
AmbientCapabilities=CAP_NET_BIND_SERVICE
```

Cần hiểu rõ trước khi dùng; năng lực (capability / 역량) propagation là một phần bảo mật (security / 보안) mô hình (model / 모델) phức tạp.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **nonewprivs** tiếp nhận điểm tựa từ **Ambient capabilities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `no_new_privs`

Kernel có flag **no_new_privs** ngăn tiến trình (process / 프로세스) tăng privilege qua `execve()` bằng một số cơ chế (mechanism / 메커니즘).

Systemd:

```ini
NoNewPrivileges=true
```

Bộ chứa (container / 컨테이너) runtimes cũng dùng flag này trong hardening.

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)** tiếp nhận điểm tựa từ **nonewprivs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rootless bộ chứa (container / 컨테이너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)

Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) làm UID/GID trong không gian tên (namespace / 네임스페이스) có thể map sang UID/GID khác trên host.

Ví dụ conceptual:

```text
inside container UID 0
        ↓ mapping
host UID 100000
```

Do đó “gốc (root / 루트) trong bộ chứa (container / 컨테이너)” không nhất thiết là host gốc (root / 루트) nếu người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) được cấu hình đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Rootless bộ chứa (container / 컨테이너)** tiếp nhận điểm tựa từ **Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DAC và MAC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rootless bộ chứa (container / 컨테이너)

Rootless bộ chứa (container / 컨테이너) dựa nhiều vào người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) để cho người dùng (user / 사용자) thường chạy bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) mà không cần host gốc (root / 루트) toàn phần.

Tuy nhiên có các giới hạn về networking, thiết bị (device / 장치) truy cập (access / 접근) và kernel features.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **DAC và MAC** tiếp nhận điểm tựa từ **Rootless bộ chứa (container / 컨테이너)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SELinux mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DAC và MAC

Classic Unix chế độ (mode / 모드)/ACL là **Discretionary kiểm soát truy cập (access control / 접근 제어) (DAC)**.

Đơn vị sở hữu (owner / 오너)/gốc (root / 루트) có quyền thay chính sách (policy / 정책) trong phạm vi DAC.

**Mandatory kiểm soát truy cập (access control / 접근 제어) (MAC)** thêm chính sách (policy / 정책) do hệ thống áp đặt, ví dụ SELinux/AppArmor.

Một thao tác (operation / 연산) phải vượt qua nhiều lớp:

```text
DAC permission
   ↓
capabilities
   ↓
MAC policy
   ↓
mount/security constraints
```

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **SELinux mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **DAC và MAC** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **SELinux chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SELinux mô hình tư duy (mental model / 사고 모델)

SELinux gán **bảo mật (security / 보안) ngữ cảnh (context / 맥락)** cho tiến trình (process / 프로세스) và đối tượng (object / 객체).

Ví dụ:

```bash
ls -Z /var/www/html
ps -eZ | head
```

Chính sách (policy / 정책) quyết định lĩnh vực (domain / 도메인) của tiến trình (process / 프로세스) có được truy cập (access / 접근) kiểu (type / 타입) của tệp (file / 파일) không.

Đây là lý do chế độ (mode / 모드) `777` vẫn có thể bị SELinux deny.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **SELinux chế độ (mode / 모드)** gom các mảnh từ **SELinux mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Nhật ký kiểm tra (audit log / 감사 로그)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SELinux chế độ (mode / 모드)

Kiểm tra:

```bash
getenforce
```

Có thể thấy:

```text
Enforcing
Permissive
Disabled
```

Không nên disable SELinux chỉ để “fix nhanh”. Permissive chế độ (mode / 모드) có thể dùng có kiểm soát để quan sát denial mà chưa enforce, nhưng môi trường vận hành (production / 운영 환경) chính sách (policy / 정책) cần theo quy trình phù hợp.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Nhật ký kiểm tra (audit log / 감사 로그)** tiếp nhận điểm tựa từ **SELinux chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **restorecon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhật ký kiểm tra (audit log / 감사 로그)

SELinux denial thường xuất hiện trong kiểm tra (audit / 감사) logs.

Tùy distro:

```bash
ausearch -m avc -ts recent
```

hoặc xem journal/nhật ký kiểm tra (audit log / 감사 로그).

Cần đọc denial để biết nguồn (source / 소스) ngữ cảnh (context / 맥락), mục tiêu (target / 대상) ngữ cảnh (context / 맥락) và thao tác (operation / 연산).

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **restorecon** tiếp nhận điểm tựa từ **Nhật ký kiểm tra (audit log / 감사 로그)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **AppArmor mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `restorecon`

Nếu tệp (file / 파일) bị bản sao (copy / 복사)/move theo cách làm ngữ cảnh (context / 맥락) sai, có thể dùng:

```bash
restorecon -Rv /var/www/html
```

để khôi phục ngữ cảnh (context / 맥락) theo chính sách (policy / 정책) mặc định.

Không nên dùng `chcon` làm fix vĩnh viễn nếu chính sách (policy / 정책) ánh xạ (mapping / 매핑) chưa được cấu hình, vì relabel có thể mất thay đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **AppArmor mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **restorecon** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Seccomp không phải permission filesystem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AppArmor mô hình tư duy (mental model / 사고 모델)

AppArmor thường dựa nhiều vào pathname/profile hơn SELinux label mô hình (model / 모델).

Kiểm tra:

```bash
aa-status
```

Profile quy định executable được truy cập (access / 접근) đường dẫn (path / 경로)/năng lực (capability / 역량) nào.

Ubuntu thường gặp AppArmor nhiều hơn SELinux.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Seccomp không phải permission filesystem** gom các mảnh từ **AppArmor mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Mount flags cũng là bảo mật (security / 보안) chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Seccomp không phải permission filesystem

**seccomp** lọc hệ thống (system / 시스템) calls tiến trình (process / 프로세스) được phép gọi.

Một tiến trình (process / 프로세스) có thể có tệp (file / 파일) permission đầy đủ nhưng vẫn bị seccomp chặn syscall cụ thể.

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) thường áp seccomp profile mặc định.

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Mount flags cũng là bảo mật (security / 보안) chính sách (policy / 정책)** tiếp nhận điểm tựa từ **Seccomp không phải permission filesystem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Linux bảo mật (security / 보안) mô-đun (module / 모듈)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mount flags cũng là bảo mật (security / 보안) chính sách (policy / 정책)

Các options:

```text
nosuid
noexec
nodev
ro
```

có thể chặn hành vi (behavior / 동작) dù chế độ (mode / 모드)/năng lực (capability / 역량) nhìn hợp lệ.

Kiểm tra:

```bash
findmnt -T /path -o TARGET,SOURCE,FSTYPE,OPTIONS
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Linux bảo mật (security / 보안) mô-đun (module / 모듈)** tiếp nhận điểm tựa từ **Mount flags cũng là bảo mật (security / 보안) chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm tra (audit / 감사) tiến trình (process / 프로세스) credentials khi gỡ lỗi (debug / 디버그)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Linux bảo mật (security / 보안) mô-đun (module / 모듈)

SELinux, AppArmor và các khung phần mềm (framework / 프레임워크) khác tích hợp qua **Linux bảo mật (security / 보안) mô-đun (module / 모듈) (LSM)** khung phần mềm (framework / 프레임워크).

Điều này cho phép kernel gọi bảo mật (security / 보안) hooks ở nhiều thao tác (operation / 연산) như open, exec, socket.

Bảo mật (security / 보안) không chỉ nằm ở filesystem.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Linux bảo mật (security / 보안) mô-đun (module / 모듈)** xác định đầu vào; **Kiểm tra (audit / 감사) tiến trình (process / 프로세스) credentials khi gỡ lỗi (debug / 디버그)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Một trường hợp (case / 사례): Java dịch vụ (service / 서비스) không đọc được certificate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra (audit / 감사) tiến trình (process / 프로세스) credentials khi gỡ lỗi (debug / 디버그)

Một luồng (flow / 흐름) thực tế:

```bash
PID=$(systemctl show -p MainPID --value app)
cat /proc/$PID/status | grep -E 'Uid|Gid|Groups|Cap'
namei -l /opt/app/config.yml
getfacl /opt/app/config.yml
findmnt -T /opt/app/config.yml
```

Nếu distro dùng SELinux:

```bash
ls -Z /opt/app/config.yml
ps -Z -p $PID
```

Nếu dùng AppArmor:

```bash
aa-status
```

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, sau khi thấy quy trình trong **Kiểm tra (audit / 감사) tiến trình (process / 프로세스) credentials khi gỡ lỗi (debug / 디버그)**, **Một trường hợp (case / 사례): Java dịch vụ (service / 서비스) không đọc được certificate** đặt nó vào một trường hợp đủ cụ thể để nhận ra điều kiện thành công và chỗ dễ sai. Từ đây, **Trường hợp (case / 사례): bind cổng (port / 포트) 80 nhưng không muốn gốc (root / 루트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một trường hợp (case / 사례): Java dịch vụ (service / 서비스) không đọc được certificate

Tệp (file / 파일):

```text
/etc/app/tls/private.key
```

có chế độ (mode / 모드):

```text
-rw-r----- root tls 0640
```

Dịch vụ (service / 서비스) chạy `User=app`, nhưng không có group `tls`.

SSH admin gốc (root / 루트) đọc được nên tưởng permission đúng.

Kiểm tra:

```bash
id app
systemctl show app -p User -p Group
```

Fix đúng có thể là thêm supplementary group hoặc thay quyền sở hữu (ownership / 소유권)/chính sách (policy / 정책) phù hợp, không phải `chmod 777`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Một trường hợp (case / 사례): Java dịch vụ (service / 서비스) không đọc được certificate** cho ta quy tắc; **Trường hợp (case / 사례): bind cổng (port / 포트) 80 nhưng không muốn gốc (root / 루트)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례): permission đúng nhưng vẫn Permission denied** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): bind cổng (port / 포트) 80 nhưng không muốn gốc (root / 루트)

Thay vì chạy ứng dụng (application / 애플리케이션) full gốc (root / 루트), có thể:

- reverse proxy ở cổng (port / 포트) 80/443 rồi app chạy 8080;
- cấp `CAP_NET_BIND_SERVICE`;
- dùng systemd socket activation.

Mỗi cách có sự đánh đổi (trade-off / 트레이드오프) khác.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Trường hợp (case / 사례): bind cổng (port / 포트) 80 nhưng không muốn gốc (root / 루트)** cho ta quy tắc; **Trường hợp (case / 사례): permission đúng nhưng vẫn Permission denied** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): permission đúng nhưng vẫn `Permission denied`

Checklist:

```text
1. process UID/GID/group?
2. traverse parent directories?
3. ACL mask?
4. mount read-only/noexec/nosuid?
5. SELinux/AppArmor?
6. container/user namespace mapping?
7. seccomp/capability requirement?
```

Đây là cách tiếp cận theo tầng (layer / 계층) thay vì mở quyền ngẫu nhiên.

> **Chuyển mạch:** Ở chặng này của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Trường hợp (case / 사례): permission đúng nhưng vẫn Permission denied** cho ta quy tắc; **Mô hình tư duy** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Một quyết định bảo mật (security / 보안) của kernel có thể xem như:

```text
process credentials
        +
namespace context
        +
DAC / ACL
        +
capabilities
        +
MAC / LSM
        +
mount / seccomp policy
        ↓
allow hoặc deny
```

Không có một câu lệnh `chmod` nào đại diện toàn bộ chuỗi này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“gốc (root / 루트) bỏ qua mọi chính sách (policy / 정책).”** gốc (root / 루트) mạnh nhưng vẫn có thể bị không gian tên (namespace / 네임스페이스), MAC, seccomp, read-only mount và năng lực (capability / 역량) bounding giới hạn.

**“ACL chỉ thêm quyền.”** ACL mask có thể làm effective permission thấp hơn entry nhìn thấy.

**“năng lực (capability / 역량) luôn an toàn hơn gốc (root / 루트).”** Chỉ khi năng lực (capability / 역량) set đủ nhỏ; `CAP_SYS_ADMIN` vẫn cực rộng.

**“SELinux deny nghĩa SELinux bị lỗi.”** Thường chính sách (policy / 정책) đang bảo vệ theo đúng thiết kế; cần xác định ứng dụng (application / 애플리케이션) có thật sự cần truy cập (access / 접근) không.

**“gốc (root / 루트) trong bộ chứa (container / 컨테이너) = host gốc (root / 루트).”** Không nhất thiết nếu người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) ánh xạ (mapping / 매핑) được dùng.

> **Chuyển mạch:** Trong **Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Đọc [Systemd sâu hơn](../05_system/systemd_units_dependencies_resources.md) để thấy cách dịch vụ (service / 서비스) manager áp credentials/capabilities, [Namespace/cgroup/seccomp](../09_production/namespaces_cgroups_seccomp.md) để hiểu bộ chứa (container / 컨테이너) isolation, và [Security hardening](../08_operations/security_hardening.md) để đặt các cơ chế này vào threat mô hình (model / 모델) tổng thể.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
