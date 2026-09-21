# Phân giải đường dẫn, mount namespace và góc nhìn filesystem của tiến trình

Trong Linux, đường dẫn không phải là “địa chỉ tuyệt đối” tồn tại độc lập với mọi tiến trình. Khi một tiến trình mở `/etc/hosts`, kernel phải bắt đầu từ root filesystem mà tiến trình đó nhìn thấy, đi qua từng thành phần đường dẫn, áp dụng mount point, symbolic link, permission và namespace để cuối cùng tìm ra object thực sự.

Hiểu **phân giải đường dẫn (path resolution)** và **mount namespace** giúp giải thích rất nhiều lỗi khó: file có tồn tại trên host nhưng container không thấy, bind mount che nội dung cũ, `chroot` không phải sandbox hoàn chỉnh, service nhìn filesystem khác shell, hoặc một path giống nhau nhưng trỏ tới object khác nhau.

## Pathname chỉ là tên, không phải object

Một pathname như:

```text
/opt/app/config.yml
```

là một chuỗi tên cần được phân giải qua cây namespace. Object thật phía sau là inode/dentry/filesystem object.

Nếu rename hoặc mount thay đổi namespace, cùng pathname có thể trỏ tới object khác mà process không nhất thiết thay đổi code.

## Bắt đầu từ root hoặc current working directory

Đường dẫn tuyệt đối bắt đầu từ root mà process nhìn thấy:

```text
/etc/hosts
```

Đường dẫn tương đối bắt đầu từ current working directory:

```text
./config.yml
```

Kernel giữ filesystem context của process, gồm root và working directory.

Quan sát:

```bash
readlink /proc/<PID>/cwd
readlink /proc/<PID>/root
```

Hai process khác nhau có thể có root khác nhau nếu dùng chroot/container/mount namespace.

## Dentry cache và path lookup

Kernel cần phân giải từng thành phần:

```text
/
→ opt
→ app
→ config.yml
```

VFS dùng dentry cache để tăng tốc lookup tên đã từng truy cập. Vì vậy path lookup không phải lúc nào cũng chạm storage.

Điều này nối trực tiếp với VFS và page cache nhưng là hai cache khác mục đích: dentry cache giúp tên → object, page cache giúp file offset → page dữ liệu.

## Quyền `x` trên thư mục là quyền traverse

Để mở:

```text
/a/b/c.txt
```

process cần có khả năng traverse qua `/a` và `/a/b`, không chỉ quyền trên file cuối cùng.

```bash
namei -l /a/b/c.txt
```

Đây là công cụ rất hữu ích để tìm component nào gây `Permission denied`.

## Symbolic link

Symlink chứa pathname khác. Khi lookup gặp symlink, kernel có thể tiếp tục phân giải target.

```bash
ln -s /srv/releases/v2 /opt/app/current
```

`/opt/app/current/config.yml` phụ thuộc target hiện tại của symlink.

Symlink loop hoặc quá nhiều lần dereference có thể gây `ELOOP`.

```bash
readlink -f /opt/app/current
```

## Hard link khác symlink ở tầng namespace

Hard link là nhiều directory entry cùng trỏ tới inode. Symlink là file đặc biệt chứa pathname target.

Vì vậy đổi target symlink không đổi inode của file đích cũ; còn hard link vẫn giữ cùng object cho tới khi link count về 0 và không còn open reference.

## Mount point thay đổi namespace

Khi mount filesystem lên `/data`, directory `/data` cũ bị che trong namespace hiện tại.

```text
trước mount:
/data -> directory trên root fs

sau mount:
/data -> root của filesystem khác
```

Dữ liệu cũ không bị xóa; nó chỉ bị che.

Unmount sẽ làm namespace cũ hiện lại.

## Bind mount

Bind mount cho phép cùng subtree xuất hiện ở path khác:

```bash
mount --bind /opt/app/data /srv/data
```

Hai pathname có thể cùng dẫn đến underlying objects giống nhau.

Container runtime dùng bind mount rất nhiều để đưa config, secret, volume hoặc socket host vào container.

## Mount namespace

Mount namespace cho phép các nhóm process nhìn **cây mount khác nhau**.

Một mount được tạo trong namespace A có thể không xuất hiện trong namespace B.

Quan sát namespace:

```bash
ls -l /proc/<PID>/ns/mnt
```

Hai process có symlink namespace inode khác nhau nghĩa là chúng ở mount namespace khác.

Có thể vào namespace bằng:

```bash
sudo nsenter -t <PID> -m
```

Sau đó `mount`, `findmnt`, `ls` sẽ nhìn theo namespace của process đích.

## Shared, slave, private propagation

Mount namespace không chỉ là copy tĩnh. Mount propagation quyết định mount event có lan giữa các namespace liên quan hay không.

Các mode quan trọng gồm:

- shared;
- slave;
- private;
- unbindable.

Đây là phần quan trọng với container runtime và Kubernetes vì mount trên host có thể cần hoặc không cần propagate vào container.

Kiểm tra:

```bash
findmnt -o TARGET,PROPAGATION
```

## `chroot` không phải container

`chroot` đổi root directory mà process nhìn thấy, nhưng không tự cô lập:

- PID;
- network;
- user;
- mount;
- capabilities;
- cgroup.

Vì vậy `chroot` không phải security boundary đầy đủ.

Container ghép nhiều namespace và policy khác nhau, trong đó mount namespace chỉ là một phần.

## `pivot_root`

Container runtime thường cần thay root filesystem sâu hơn `chroot`. `pivot_root()` cho phép đổi root mount của namespace và di chuyển root cũ sang vị trí khác trước khi unmount.

Đây là cơ chế nền tảng để container nhìn image root filesystem như `/` riêng.

## Overlay filesystem

Container image thường dùng layered filesystem như OverlayFS.

Khái niệm gồm:

```text
lower layers: read-only image layers
upper layer : writable container layer
merged view : filesystem process nhìn thấy
```

Khi sửa file từ lower layer, copy-up có thể tạo bản sao ở upper layer.

Điều này có ảnh hưởng hiệu năng và semantics, nhất là workload ghi nhiều.

## Path resolution và race condition

Pattern:

```text
check path
→ sau đó open path
```

có thể có race nếu attacker hoặc process khác đổi namespace/path giữa hai bước.

Đây là lý do API hiện đại như `openat()`, `openat2()` và dirfd-based operations tồn tại để giảm ambiguity và kiểm soát resolution tốt hơn.

## `openat()` và dirfd

Thay vì luôn lookup từ cwd/root, `openat()` cho phép bắt đầu từ directory file descriptor.

Điều này hữu ích cho code cần thao tác trong directory đã mở và giảm phụ thuộc vào cwd có thể thay đổi.

`openat2()` trên Linux mới hơn thêm flags để kiểm soát resolution như không đi qua symlink hoặc không thoát khỏi subtree tùy use case.

## Deleted cwd và deleted file

Process có thể giữ current working directory tới directory đã bị unlink khỏi namespace. `/proc/<PID>/cwd` có thể hiển thị `(deleted)`.

Tương tự file descriptor vẫn giữ inode sau khi pathname bị unlink.

Điều này nhắc lại nguyên tắc quan trọng: namespace name và object lifetime không giống nhau.

## Mount options là policy layer

Mount có thể thêm policy:

- `ro`;
- `noexec`;
- `nosuid`;
- `nodev`;
- `relatime`;
- `noatime`;
- filesystem-specific options.

Process có permission file đúng vẫn có thể bị policy mount chặn.

## Debug “file tồn tại nhưng process không thấy”

Quy trình tốt:

```bash
readlink /proc/<PID>/root
readlink /proc/<PID>/cwd
ls -l /proc/<PID>/ns/mnt
findmnt -T /path
namei -l /path
sudo nsenter -t <PID> -m -- ls -l /path
```

Nếu host thấy file nhưng namespace process không thấy, vấn đề không nằm ở Java file API mà ở filesystem view.

## Systemd và filesystem namespace

Systemd có thể tạo namespace riêng bằng directives như:

- `ProtectSystem=`;
- `ProtectHome=`;
- `PrivateTmp=`;
- `ReadOnlyPaths=`;
- `BindPaths=`.

Vì vậy service có thể nhìn `/tmp` hoặc filesystem khác shell admin.

Đây là một nguyên nhân rất thực tế khi “SSH thấy file nhưng service không thấy”.

## Container volume

Trong Docker/Kubernetes, volume/bind mount được đưa vào mount namespace của container.

Nếu mount nhầm path, có thể che file có sẵn trong image.

Ví dụ image có `/app/config/default.yml`, nhưng mount empty directory lên `/app/config` sẽ làm file trong image không còn thấy ở merged namespace.

## Mô hình tư duy

Khi process truy cập một path, hãy nghĩ theo chuỗi:

```text
process root/cwd
→ mount namespace
→ path components
→ dentry lookup
→ symlink resolution
→ mount crossing
→ permission + LSM + mount policy
→ inode/object
```

Path không phải object. Nó là một truy vấn vào namespace động.

## Những hiểu lầm phổ biến

**“Đường dẫn tuyệt đối nghĩa là mọi process thấy cùng object.”** Không nếu root/mount namespace khác nhau.

**“Mount xóa dữ liệu directory cũ.”** Không; nó thường che namespace cũ.

**“chroot là container.”** Không; nó chỉ thay root path view.

**“File tồn tại trên host thì container chắc chắn thấy.”** Chỉ nếu namespace/mount đưa nó vào.

**“Permission đúng thì open chắc chắn thành công.”** Mount option, namespace, LSM và symlink resolution vẫn có thể chặn.

## Kết nối kiến thức

Chương này nối [filesystem/inode/link](./filesystem_paths_inodes_links.md), [VFS](./vfs_page_cache_writeback.md), [credentials/capabilities](../03_identity/credentials_capabilities_acl_mac.md), [systemd sandboxing](../05_system/systemd_units_dependencies_resources.md) và [namespace/container](../09_production/namespaces_cgroups_seccomp.md).