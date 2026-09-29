# Phân giải đường dẫn, mount không gian tên (namespace / 네임스페이스) và góc nhìn filesystem của tiến trình

> **Mạch đọc:** Đọc **Phân giải đường dẫn, mount không gian tên (namespace / 네임스페이스) và góc nhìn filesystem của tiến trình** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Pathname chỉ là tên, không phải đối tượng (object / 객체)** sang **Bắt đầu từ gốc (root / 루트) hoặc hiện tại (current / 현재) working directory**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Trong Linux, đường dẫn không phải là “địa chỉ tuyệt đối” tồn tại độc lập với mọi tiến trình. Khi một tiến trình mở `/etc/hosts`, kernel phải bắt đầu từ gốc (root / 루트) filesystem mà tiến trình đó nhìn thấy, đi qua từng thành phần đường dẫn, áp dụng mount điểm (point / 지점), symbolic link, permission và không gian tên (namespace / 네임스페이스) để cuối cùng tìm ra đối tượng (object / 객체) thực sự.

Hiểu **phân giải đường dẫn (path resolution)** và **mount không gian tên (namespace / 네임스페이스)** giúp giải thích rất nhiều lỗi khó: tệp (file / 파일) có tồn tại trên host nhưng bộ chứa (container / 컨테이너) không thấy, bind mount che nội dung cũ, `chroot` không phải sandbox hoàn chỉnh, dịch vụ (service / 서비스) nhìn filesystem khác shell, hoặc một đường dẫn (path / 경로) giống nhau nhưng trỏ tới đối tượng (object / 객체) khác nhau.

## Pathname chỉ là tên, không phải đối tượng (object / 객체)

Một pathname như:

```text
/opt/app/config.yml
```

là một chuỗi tên cần được phân giải qua cây không gian tên (namespace / 네임스페이스). đối tượng (object / 객체) thật phía sau là inode/dentry/filesystem đối tượng (object / 객체).

Nếu rename hoặc mount thay đổi không gian tên (namespace / 네임스페이스), cùng pathname có thể trỏ tới đối tượng (object / 객체) khác mà tiến trình (process / 프로세스) không nhất thiết thay đổi mã (code / 코드).

## Bắt đầu từ gốc (root / 루트) hoặc hiện tại (current / 현재) working directory

Đường dẫn tuyệt đối bắt đầu từ gốc (root / 루트) mà tiến trình (process / 프로세스) nhìn thấy:

```text
/etc/hosts
```

Đường dẫn tương đối bắt đầu từ hiện tại (current / 현재) working directory:

```text
./config.yml
```

Kernel giữ filesystem ngữ cảnh (context / 맥락) của tiến trình (process / 프로세스), gồm gốc (root / 루트) và working directory.

Quan sát:

```bash
readlink /proc/<PID>/cwd
readlink /proc/<PID>/root
```

Hai tiến trình (process / 프로세스) khác nhau có thể có gốc (root / 루트) khác nhau nếu dùng chroot/bộ chứa (container / 컨테이너)/mount không gian tên (namespace / 네임스페이스).

## Dentry bộ nhớ đệm (cache / 캐시) và đường dẫn (path / 경로) lookup

Kernel cần phân giải từng thành phần:

```text
/
→ opt
→ app
→ config.yml
```

VFS dùng dentry bộ nhớ đệm (cache / 캐시) để tăng tốc lookup tên đã từng truy cập. Vì vậy đường dẫn (path / 경로) lookup không phải lúc nào cũng chạm lưu trữ (storage / 저장소).

Điều này nối trực tiếp với VFS và page bộ nhớ đệm (cache / 캐시) nhưng là hai bộ nhớ đệm (cache / 캐시) khác mục đích: dentry bộ nhớ đệm (cache / 캐시) giúp tên → đối tượng (object / 객체), page bộ nhớ đệm (cache / 캐시) giúp tệp (file / 파일) offset → page dữ liệu.

## Quyền `x` trên thư mục là quyền traverse

Để mở:

```text
/a/b/c.txt
```

Tiến trình (process / 프로세스) cần có khả năng traverse qua `/a` và `/a/b`, không chỉ quyền trên tệp (file / 파일) cuối cùng.

```bash
namei -l /a/b/c.txt
```

Đây là công cụ rất hữu ích để tìm thành phần (component / 컴포넌트) nào gây `Permission denied`.

## Symbolic link

Symlink chứa pathname khác. Khi lookup gặp symlink, kernel có thể tiếp tục phân giải mục tiêu (target / 대상).

```bash
ln -s /srv/releases/v2 /opt/app/current
```

`/opt/app/current/config.yml` phụ thuộc mục tiêu (target / 대상) hiện tại của symlink.

Symlink vòng lặp (loop / 루프) hoặc quá nhiều lần dereference có thể gây `ELOOP`.

```bash
readlink -f /opt/app/current
```

## Hard link khác symlink ở tầng không gian tên (namespace / 네임스페이스)

Hard link là nhiều directory entry cùng trỏ tới inode. Symlink là tệp (file / 파일) đặc biệt chứa pathname mục tiêu (target / 대상).

Vì vậy đổi mục tiêu (target / 대상) symlink không đổi inode của tệp (file / 파일) đích cũ; còn hard link vẫn giữ cùng đối tượng (object / 객체) cho tới khi link count về 0 và không còn open tham chiếu (reference / 참조).

## Mount điểm (point / 지점) thay đổi không gian tên (namespace / 네임스페이스)

Khi mount filesystem lên `/data`, directory `/data` cũ bị che trong không gian tên (namespace / 네임스페이스) hiện tại.

```text
trước mount:
/data -> directory trên root fs

sau mount:
/data -> root của filesystem khác
```

Dữ liệu cũ không bị xóa; nó chỉ bị che.

Unmount sẽ làm không gian tên (namespace / 네임스페이스) cũ hiện lại.

## Bind mount

Bind mount cho phép cùng subtree xuất hiện ở đường dẫn (path / 경로) khác:

```bash
mount --bind /opt/app/data /srv/data
```

Hai pathname có thể cùng dẫn đến underlying objects giống nhau.

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) dùng bind mount rất nhiều để đưa cấu hình (config / 설정), secret, volume hoặc socket host vào bộ chứa (container / 컨테이너).

## Mount không gian tên (namespace / 네임스페이스)

Mount không gian tên (namespace / 네임스페이스) cho phép các nhóm tiến trình (process / 프로세스) nhìn **cây mount khác nhau**.

Một mount được tạo trong không gian tên (namespace / 네임스페이스) A có thể không xuất hiện trong không gian tên (namespace / 네임스페이스) B.

Quan sát không gian tên (namespace / 네임스페이스):

```bash
ls -l /proc/<PID>/ns/mnt
```

Hai tiến trình (process / 프로세스) có symlink không gian tên (namespace / 네임스페이스) inode khác nhau nghĩa là chúng ở mount không gian tên (namespace / 네임스페이스) khác.

Có thể vào không gian tên (namespace / 네임스페이스) bằng:

```bash
sudo nsenter -t <PID> -m
```

Sau đó `mount`, `findmnt`, `ls` sẽ nhìn theo không gian tên (namespace / 네임스페이스) của tiến trình (process / 프로세스) đích.

## Dùng chung (shared / 공유), slave, private propagation

Mount không gian tên (namespace / 네임스페이스) không chỉ là bản sao (copy / 복사) tĩnh. Mount propagation quyết định mount sự kiện (event / 이벤트) có lan giữa các không gian tên (namespace / 네임스페이스) liên quan hay không.

Các chế độ (mode / 모드) quan trọng gồm:

- dùng chung (shared / 공유);
- slave;
- private;
- unbindable.

Đây là phần quan trọng với bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) và Kubernetes vì mount trên host có thể cần hoặc không cần propagate vào bộ chứa (container / 컨테이너).

Kiểm tra:

```bash
findmnt -o TARGET,PROPAGATION
```

## `chroot` không phải bộ chứa (container / 컨테이너)

`chroot` đổi gốc (root / 루트) directory mà tiến trình (process / 프로세스) nhìn thấy, nhưng không tự cô lập:

- PID;
- mạng (network / 네트워크);
- người dùng (user / 사용자);
- mount;
- capabilities;
- cgroup.

Vì vậy `chroot` không phải ranh giới bảo mật (security boundary / 보안 경계) đầy đủ.

Bộ chứa (container / 컨테이너) ghép nhiều không gian tên (namespace / 네임스페이스) và chính sách (policy / 정책) khác nhau, trong đó mount không gian tên (namespace / 네임스페이스) chỉ là một phần.

## `pivot_root`

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) thường cần thay gốc (root / 루트) filesystem sâu hơn `chroot`. `pivot_root()` cho phép đổi gốc (root / 루트) mount của không gian tên (namespace / 네임스페이스) và di chuyển gốc (root / 루트) cũ sang vị trí khác trước khi unmount.

Đây là cơ chế nền tảng để bộ chứa (container / 컨테이너) nhìn ảnh (image / 이미지) gốc (root / 루트) filesystem như `/` riêng.

## Overlay filesystem

Ảnh bộ chứa (container image / 컨테이너 이미지) thường dùng layered filesystem như OverlayFS.

Khái niệm gồm:

```text
lower layers: read-only image layers
upper layer : writable container layer
merged view : filesystem process nhìn thấy
```

Khi sửa tệp (file / 파일) từ lower tầng (layer / 계층), copy-up có thể tạo bản sao ở upper tầng (layer / 계층).

Điều này có ảnh hưởng hiệu năng và ngữ nghĩa (semantics / 의미론), nhất là tải công việc (workload / 워크로드) ghi nhiều.

## Đường dẫn (path / 경로) resolution và race điều kiện (condition / 조건)

Mẫu (pattern / 패턴):

```text
check path
→ sau đó open path
```

có thể có race nếu attacker hoặc tiến trình (process / 프로세스) khác đổi không gian tên (namespace / 네임스페이스)/đường dẫn (path / 경로) giữa hai bước.

Đây là lý do API hiện đại như `openat()`, `openat2()` và dirfd-based operations tồn tại để giảm ambiguity và kiểm soát resolution tốt hơn.

## `openat()` và dirfd

Thay vì luôn lookup từ cwd/gốc (root / 루트), `openat()` cho phép bắt đầu từ directory tệp (file / 파일) descriptor.

Điều này hữu ích cho mã (code / 코드) cần thao tác trong directory đã mở và giảm phụ thuộc vào cwd có thể thay đổi.

`openat2()` trên Linux mới hơn thêm flags để kiểm soát resolution như không đi qua symlink hoặc không thoát khỏi subtree tùy use trường hợp (case / 사례).

## Deleted cwd và deleted tệp (file / 파일)

Tiến trình (process / 프로세스) có thể giữ hiện tại (current / 현재) working directory tới directory đã bị unlink khỏi không gian tên (namespace / 네임스페이스). `/proc/<PID>/cwd` có thể hiển thị `(deleted)`.

Tương tự tệp (file / 파일) descriptor vẫn giữ inode sau khi pathname bị unlink.

Điều này nhắc lại nguyên tắc quan trọng: không gian tên (namespace / 네임스페이스) name và đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) không giống nhau.

## Mount options là chính sách (policy / 정책) tầng (layer / 계층)

Mount có thể thêm chính sách (policy / 정책):

- `ro`;
- `noexec`;
- `nosuid`;
- `nodev`;
- `relatime`;
- `noatime`;
- filesystem-specific options.

Tiến trình (process / 프로세스) có permission tệp (file / 파일) đúng vẫn có thể bị chính sách (policy / 정책) mount chặn.

## Gỡ lỗi (debug / 디버그) “tệp (file / 파일) tồn tại nhưng tiến trình (process / 프로세스) không thấy”

Quy trình tốt:

```bash
readlink /proc/<PID>/root
readlink /proc/<PID>/cwd
ls -l /proc/<PID>/ns/mnt
findmnt -T /path
namei -l /path
sudo nsenter -t <PID> -m -- ls -l /path
```

Nếu host thấy tệp (file / 파일) nhưng không gian tên (namespace / 네임스페이스) tiến trình (process / 프로세스) không thấy, vấn đề không nằm ở Java tệp (file / 파일) API mà ở filesystem view.

## Systemd và filesystem không gian tên (namespace / 네임스페이스)

Systemd có thể tạo không gian tên (namespace / 네임스페이스) riêng bằng directives như:

- `ProtectSystem=`;
- `ProtectHome=`;
- `PrivateTmp=`;
- `ReadOnlyPaths=`;
- `BindPaths=`.

Vì vậy dịch vụ (service / 서비스) có thể nhìn `/tmp` hoặc filesystem khác shell admin.

Đây là một nguyên nhân rất thực tế khi “SSH thấy tệp (file / 파일) nhưng dịch vụ (service / 서비스) không thấy”.

## Bộ chứa (container / 컨테이너) volume

Trong Docker/Kubernetes, volume/bind mount được đưa vào mount không gian tên (namespace / 네임스페이스) của bộ chứa (container / 컨테이너).

Nếu mount nhầm đường dẫn (path / 경로), có thể che tệp (file / 파일) có sẵn trong ảnh (image / 이미지).

Ví dụ ảnh (image / 이미지) có `/app/config/default.yml`, nhưng mount empty directory lên `/app/config` sẽ làm tệp (file / 파일) trong ảnh (image / 이미지) không còn thấy ở merged không gian tên (namespace / 네임스페이스).

## Mô hình tư duy

Khi tiến trình (process / 프로세스) truy cập một đường dẫn (path / 경로), hãy nghĩ theo chuỗi:

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

Đường dẫn (path / 경로) không phải đối tượng (object / 객체). Nó là một truy vấn vào không gian tên (namespace / 네임스페이스) động.

## Những hiểu lầm phổ biến

**“Đường dẫn tuyệt đối nghĩa là mọi tiến trình (process / 프로세스) thấy cùng đối tượng (object / 객체).”** Không nếu gốc (root / 루트)/mount không gian tên (namespace / 네임스페이스) khác nhau.

**“Mount xóa dữ liệu directory cũ.”** Không; nó thường che không gian tên (namespace / 네임스페이스) cũ.

**“chroot là bộ chứa (container / 컨테이너).”** Không; nó chỉ thay gốc (root / 루트) đường dẫn (path / 경로) view.

**“tệp (file / 파일) tồn tại trên host thì bộ chứa (container / 컨테이너) chắc chắn thấy.”** Chỉ nếu không gian tên (namespace / 네임스페이스)/mount đưa nó vào.

**“Permission đúng thì open chắc chắn thành công.”** Mount option, không gian tên (namespace / 네임스페이스), LSM và symlink resolution vẫn có thể chặn.

## Kết nối kiến thức

Chương này nối [filesystem/inode/link](./filesystem_paths_inodes_links.md), [VFS](./vfs_page_cache_writeback.md), [credentials/capabilities](../03_identity/credentials_capabilities_acl_mac.md), [systemd sandboxing](../05_system/systemd_units_dependencies_resources.md) và [namespace/container](../09_production/namespaces_cgroups_seccomp.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [files streams descriptors](./files_streams_descriptors.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
