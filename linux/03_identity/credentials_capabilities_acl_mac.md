# Danh tính Linux sâu hơn: credentials, capabilities, ACL và MAC

Chương [Người dùng, nhóm, quyền truy cập và đặc quyền](./users_groups_permissions.md) trình bày mô hình quyền cơ bản. Chương này đi sâu vào cách kernel thật sự gắn **credentials** với process, cách quyền được kiểm tra qua UID/GID, ACL, capabilities, namespace và Mandatory Access Control, cũng như vì sao “chmod 777” vẫn có thể không làm một thao tác thành công.

## Kernel kiểm tra ai đang thực hiện thao tác bằng cách nào?

Kernel không hỏi “người dùng đăng nhập tên gì?” theo nghĩa giao diện. Nó nhìn **credentials của process**.

Một process có nhiều identity fields hơn chỉ một UID:

- real UID;
- effective UID;
- saved set-user-ID;
- real/effective/saved GID;
- supplementary groups;
- capabilities;
- user namespace context;
- security labels tùy SELinux/AppArmor.

Có thể quan sát một phần:

```bash
cat /proc/<PID>/status | grep -E 'Uid|Gid|Groups|Cap'
```

## Real UID và effective UID

**Real UID** thường phản ánh user khởi tạo process.

**Effective UID** là identity kernel thường dùng cho nhiều kiểm tra quyền filesystem.

Setuid binary tồn tại chính vì hai giá trị này có thể khác nhau.

Ví dụ `passwd` cần cập nhật dữ liệu mà user bình thường không thể ghi trực tiếp. Binary có thể chạy với effective privilege cao hơn trong phạm vi code được kiểm soát.

## Saved UID

Saved set-user-ID cho phép một process tạm drop privilege rồi có thể lấy lại trong những điều kiện nhất định.

Đây là pattern phổ biến trong daemon truyền thống:

```text
start với privilege cao
→ mở resource đặc quyền
→ drop privilege
→ xử lý request bằng user ít quyền hơn
```

Thiết kế này giảm blast radius nếu phần xử lý request có bug.

## Supplementary groups

Một process có thể thuộc nhiều group ngoài primary GID.

```bash
id appuser
```

Khi systemd khởi chạy service, groups có thể khác phiên SSH của bạn.

```bash
cat /proc/<PID>/status | grep Groups
```

Nếu permission dựa vào group nhưng process không thật sự có group đó, `ls -l` nhìn file đúng vẫn không giúp.

## Credential inheritance

Child process thường kế thừa credentials từ parent, sau đó có thể thay đổi theo API/policy.

Đây là lý do shell, sudo, systemd và container runtime đều quan trọng: chúng quyết định credentials của process cuối cùng.

## `sudo` thực sự làm gì?

`sudo` đọc policy rồi chạy command dưới target identity.

Nó không chỉ “thêm root”. Nó có thể:

- chọn target user;
- đặt environment;
- ghi audit/log;
- giới hạn command;
- yêu cầu authentication;
- thay group context.

Kiểm tra policy được phép:

```bash
sudo -l
```

`sudoers` quá rộng như:

```text
ALL=(ALL) NOPASSWD: ALL
```

thực tế gần như trao full root capability cho account đó.

## `su` và `sudo -i` khác nhau về context

`su`, `su -`, `sudo -u`, `sudo -i` tạo environment/login semantics khác nhau.

Một command chạy thành công dưới `sudo -i` không chứng minh service account có quyền tương tự.

Khi debug nên tái hiện đúng identity:

```bash
sudo -u appuser -- /usr/bin/test -r /opt/app/config.yml
```

## Permission check trên pathname

Để đọc:

```text
/a/b/c.txt
```

kernel cần traverse `/`, `/a`, `/a/b` và cuối cùng kiểm tra object `c.txt`.

Execute bit trên directory mang nghĩa **search/traverse**, không phải “chạy folder”.

Dùng:

```bash
namei -l /a/b/c.txt
```

để thấy permission từng component.

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

## Default ACL trên directory

Directory có thể có **default ACL** để file/subdirectory mới kế thừa policy.

```bash
setfacl -d -m g:appops:rwx /srv/shared
```

Điều này hữu ích cho thư mục chia sẻ nhiều service/user.

Nhưng ACL inheritance phức tạp hơn mode bits đơn giản; cần document rõ để tránh policy “ẩn”.

## Setgid trên directory

Nếu directory có setgid bit:

```bash
chmod g+s /srv/shared
```

file mới thường kế thừa group của directory thay vì primary group của process, tùy filesystem semantics.

Đây là pattern tốt cho shared workspace.

## Sticky bit

Trên directory writable chung như `/tmp`, sticky bit hạn chế việc user xóa file của người khác.

```bash
ls -ld /tmp
```

thường thấy:

```text
drwxrwxrwt
```

Chữ `t` là sticky bit.

## Setuid và setgid binary

Setuid binary có thể chạy với effective UID của owner.

Đây là cơ chế quyền rất mạnh và là bề mặt tấn công quan trọng.

Tìm setuid files:

```bash
find / -xdev -perm -4000 -type f 2>/dev/null
```

Không nên xóa tùy tiện vì nhiều system utilities hợp lệ dùng setuid.

## Capabilities: chia nhỏ quyền root

Linux chia một phần đặc quyền root thành **capabilities**.

Ví dụ:

- `CAP_NET_BIND_SERVICE` — bind port thấp;
- `CAP_CHOWN` — thay ownership;
- `CAP_SYS_ADMIN` — một capability cực rộng;
- `CAP_NET_ADMIN` — thay network config;
- `CAP_SYS_PTRACE` — tracing process trong nhiều tình huống.

Danh sách chính xác phụ thuộc kernel version.

## Capability sets

Process có nhiều tập capability:

- permitted;
- effective;
- inheritable;
- bounding;
- ambient.

Không cần thuộc toàn bộ bitmask ngay, nhưng cần hiểu rằng “process có capability” không chỉ là một boolean đơn giản.

Xem:

```bash
capsh --print
```

hoặc:

```bash
getpcaps <PID>
```

nếu tool có sẵn.

## File capabilities

Có thể gắn capability vào executable:

```bash
sudo setcap cap_net_bind_service=+ep /opt/app/server
getcap /opt/app/server
```

Ứng dụng có thể bind port 80 mà không chạy full root.

Nhưng file capability cũng cần quản lý như privilege-bearing metadata.

## `CAP_SYS_ADMIN` không phải capability “nhỏ”

`CAP_SYS_ADMIN` bao trùm rất nhiều operation và thường được ví như “new root”.

Nếu mục tiêu là least privilege, tránh cấp nó chỉ vì một permission issue chưa hiểu.

## Bounding set

Capability bounding set giới hạn capability process descendants có thể đạt được.

Systemd có:

```ini
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
```

để giảm privilege surface.

## Ambient capabilities

Ambient set giúp truyền capabilities qua `execve()` trong một số flow không setuid.

Systemd có:

```ini
AmbientCapabilities=CAP_NET_BIND_SERVICE
```

Cần hiểu rõ trước khi dùng; capability propagation là một phần security model phức tạp.

## `no_new_privs`

Kernel có flag **no_new_privs** ngăn process tăng privilege qua `execve()` bằng một số mechanism.

Systemd:

```ini
NoNewPrivileges=true
```

Container runtimes cũng dùng flag này trong hardening.

## User namespace

User namespace làm UID/GID trong namespace có thể map sang UID/GID khác trên host.

Ví dụ conceptual:

```text
inside container UID 0
        ↓ mapping
host UID 100000
```

Do đó “root trong container” không nhất thiết là host root nếu user namespace được cấu hình đúng.

## Rootless container

Rootless container dựa nhiều vào user namespace để cho user thường chạy container runtime mà không cần host root toàn phần.

Tuy nhiên có các giới hạn về networking, device access và kernel features.

## DAC và MAC

Classic Unix mode/ACL là **Discretionary Access Control (DAC)**.

Owner/root có quyền thay policy trong phạm vi DAC.

**Mandatory Access Control (MAC)** thêm policy do hệ thống áp đặt, ví dụ SELinux/AppArmor.

Một operation phải vượt qua nhiều lớp:

```text
DAC permission
   ↓
capabilities
   ↓
MAC policy
   ↓
mount/security constraints
```

## SELinux mental model

SELinux gán **security context** cho process và object.

Ví dụ:

```bash
ls -Z /var/www/html
ps -eZ | head
```

Policy quyết định domain của process có được access type của file không.

Đây là lý do mode `777` vẫn có thể bị SELinux deny.

## SELinux mode

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

Không nên disable SELinux chỉ để “fix nhanh”. Permissive mode có thể dùng có kiểm soát để quan sát denial mà chưa enforce, nhưng production policy cần theo quy trình phù hợp.

## Audit log

SELinux denial thường xuất hiện trong audit logs.

Tùy distro:

```bash
ausearch -m avc -ts recent
```

hoặc xem journal/audit log.

Cần đọc denial để biết source context, target context và operation.

## `restorecon`

Nếu file bị copy/move theo cách làm context sai, có thể dùng:

```bash
restorecon -Rv /var/www/html
```

để khôi phục context theo policy mặc định.

Không nên dùng `chcon` làm fix vĩnh viễn nếu policy mapping chưa được cấu hình, vì relabel có thể mất thay đổi.

## AppArmor mental model

AppArmor thường dựa nhiều vào pathname/profile hơn SELinux label model.

Kiểm tra:

```bash
aa-status
```

Profile quy định executable được access path/capability nào.

Ubuntu thường gặp AppArmor nhiều hơn SELinux.

## Seccomp không phải permission filesystem

**seccomp** lọc system calls process được phép gọi.

Một process có thể có file permission đầy đủ nhưng vẫn bị seccomp chặn syscall cụ thể.

Container runtime thường áp seccomp profile mặc định.

## Mount flags cũng là security policy

Các options:

```text
nosuid
noexec
nodev
ro
```

có thể chặn behavior dù mode/capability nhìn hợp lệ.

Kiểm tra:

```bash
findmnt -T /path -o TARGET,SOURCE,FSTYPE,OPTIONS
```

## Linux Security Module

SELinux, AppArmor và các framework khác tích hợp qua **Linux Security Module (LSM)** framework.

Điều này cho phép kernel gọi security hooks ở nhiều operation như open, exec, socket.

Security không chỉ nằm ở filesystem.

## Audit process credentials khi debug

Một flow thực tế:

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

## Một case: Java service không đọc được certificate

File:

```text
/etc/app/tls/private.key
```

có mode:

```text
-rw-r----- root tls 0640
```

Service chạy `User=app`, nhưng không có group `tls`.

SSH admin root đọc được nên tưởng permission đúng.

Kiểm tra:

```bash
id app
systemctl show app -p User -p Group
```

Fix đúng có thể là thêm supplementary group hoặc thay ownership/policy phù hợp, không phải `chmod 777`.

## Case: bind port 80 nhưng không muốn root

Thay vì chạy application full root, có thể:

- reverse proxy ở port 80/443 rồi app chạy 8080;
- cấp `CAP_NET_BIND_SERVICE`;
- dùng systemd socket activation.

Mỗi cách có trade-off khác.

## Case: permission đúng nhưng vẫn `Permission denied`

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

Đây là cách tiếp cận theo layer thay vì mở quyền ngẫu nhiên.

## Mô hình tư duy

Một quyết định security của kernel có thể xem như:

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

## Những hiểu lầm phổ biến

**“Root bỏ qua mọi policy.”** Root mạnh nhưng vẫn có thể bị namespace, MAC, seccomp, read-only mount và capability bounding giới hạn.

**“ACL chỉ thêm quyền.”** ACL mask có thể làm effective permission thấp hơn entry nhìn thấy.

**“Capability luôn an toàn hơn root.”** Chỉ khi capability set đủ nhỏ; `CAP_SYS_ADMIN` vẫn cực rộng.

**“SELinux deny nghĩa SELinux bị lỗi.”** Thường policy đang bảo vệ theo đúng thiết kế; cần xác định application có thật sự cần access không.

**“Root trong container = host root.”** Không nhất thiết nếu user namespace mapping được dùng.

## Kết nối kiến thức

Đọc [Systemd sâu hơn](../05_system/systemd_units_dependencies_resources.md) để thấy cách service manager áp credentials/capabilities, [Namespace/cgroup/seccomp](../09_production/namespaces_cgroups_seccomp.md) để hiểu container isolation, và [Security hardening](../08_operations/security_hardening.md) để đặt các cơ chế này vào threat model tổng thể.