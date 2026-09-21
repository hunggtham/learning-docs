# Người dùng, nhóm, quyền truy cập và đặc quyền

Mô hình quyền của Linux tồn tại vì một máy có thể chạy nhiều tiến trình thuộc nhiều danh tính bảo mật khác nhau nhưng cùng chia sẻ hệ thống tệp, mạng và thiết bị. Câu hỏi nền tảng không phải "nên chmod số nào?" mà là: **tiến trình nào đang yêu cầu thao tác trên đối tượng nào, với thông tin xác thực nào, và kernel đang áp dụng chính sách nào?**

## Người dùng không chỉ là tên đăng nhập

Kernel chủ yếu làm việc với **UID (User ID)** và **GID (Group ID)** dạng số. Tên người dùng và tên nhóm là ánh xạ dễ đọc cho con người do cơ sở dữ liệu không gian người dùng như `/etc/passwd`, `/etc/group` hoặc dịch vụ thư mục cung cấp.

```bash
id
id appuser
getent passwd appuser
```

`id` cho thấy danh tính hiệu lực (effective identity) và các nhóm bổ sung (supplementary groups). Trong môi trường Hàn Quốc, người dùng là **사용자**, nhóm là **그룹**, quyền truy cập là **권한**.

Một tiến trình kế thừa thông tin xác thực từ tiến trình tạo ra nó rồi có thể thay đổi danh tính thông qua các cơ chế được kiểm soát. Vì vậy khi ứng dụng không đọc được tệp, cần hỏi **dịch vụ thực sự đang chạy bằng người dùng nào**, chứ không phải quản trị viên SSH đang đăng nhập bằng tài khoản nào.

```bash
systemctl show app -p User -p Group
ps -o user,group,pid,cmd -p <PID>
```

## Các bit quyền truy cập

Chế độ quyền Unix truyền thống chia thành chủ sở hữu (owner), nhóm (group), người khác (others) và ba quyền cơ bản:

- `r` — đọc (read);
- `w` — ghi (write);
- `x` — thực thi hoặc đi xuyên thư mục (execute/search).

```text
-rwxr-x---
```

Có thể đọc thành: owner `rwx`, group `r-x`, others `---`.

Cách viết bằng số dùng các giá trị bit 4/2/1:

```text
7 = 4+2+1 = rwx
6 = 4+2   = rw-
5 = 4+1   = r-x
4 = 4     = r--
```

Vì vậy `chmod 640 config.yml` nghĩa là chủ sở hữu được đọc/ghi, nhóm được đọc và người khác không có quyền.

Nếu chỉ học các con số mà không hiểu ý nghĩa của quyền trên thư mục, việc đặt quyền rất dễ sai.

## Quyền trên tệp và thư mục có ý nghĩa khác nhau

Với tệp thông thường, `r` cho phép đọc nội dung, `w` cho phép sửa nội dung, `x` cho phép thực thi nếu định dạng tệp và trình thông dịch phù hợp.

Với thư mục, `r` liên quan tới việc liệt kê tên, `w` liên quan tới việc thay đổi các mục thư mục, còn `x` mang nghĩa **tìm kiếm/đi xuyên (search/traverse)**. Để mở `/opt/app/config/a.yml`, tiến trình phải có khả năng đi xuyên các thư mục cha.

```bash
namei -l /opt/app/config/a.yml
```

Câu lệnh này rất hữu ích khi tệp cuối cùng có quyền `644` nhưng ứng dụng vẫn báo `Permission denied`.

## Tại sao xóa tệp lại phụ thuộc quyền của thư mục?

Xóa một đường dẫn là thay đổi mục thư mục. Vì vậy khả năng chạy `rm file` phụ thuộc mạnh vào quyền của thư mục chứa nó, chứ không chỉ phụ thuộc bit ghi trên bản thân tệp. Đây là hệ quả trực tiếp của mô hình vùng tên trong [Hệ thống tệp, đường dẫn, inode và liên kết](../01_filesystem/filesystem_paths_inodes_links.md).

## Chủ sở hữu

```bash
chown app:app application.yml
```

làm thay đổi người sở hữu và nhóm. Thao tác đệ quy:

```bash
chown -R app:app /opt/app
```

có phạm vi ảnh hưởng lớn. Một thói quen tốt trong production là kiểm tra cây thư mục trước và tránh chạy lệnh đệ quy trên đường dẫn chưa được xác minh.

## Vì sao `chmod -R 777` là một cách làm không tốt?

`777` cấp quyền đọc, ghi và thực thi cho tất cả các nhóm quyền. Nó có thể làm triệu chứng về quyền biến mất nhưng đồng thời phá vỡ ranh giới bảo mật và cấp bit thực thi cho những tệp dữ liệu không cần thực thi.

Khi cần đặt quyền cho cả cây thư mục, thường nên phân biệt thư mục và tệp:

```bash
find /opt/app -type d -exec chmod 755 {} +
find /opt/app -type f -exec chmod 644 {} +
```

Sau đó chỉ cấp quyền đặc biệt cho tệp thực thi, cấu hình hoặc bí mật theo nhu cầu thực tế.

Nguyên tắc **đặc quyền tối thiểu (least privilege / 최소 권한)** yêu cầu chỉ cấp khả năng cần thiết cho một nhiệm vụ, thay vì mở quyền rộng chỉ để việc gỡ lỗi trở nên dễ hơn.

## `umask`

Khi tiến trình tạo tệp với một chế độ quyền yêu cầu, **`umask`** loại bỏ một số quyền mặc định.

```bash
umask
```

Giá trị thường gặp `0022` thường dẫn tới tệp có quyền `644` và thư mục `755` khi chương trình yêu cầu chế độ mặc định tương ứng. Vì thế hai dịch vụ có `umask` khác nhau có thể tạo ra tệp với quyền khác nhau dù mã nguồn giống nhau.

## Nhóm như một cơ chế chia sẻ quyền

Thay vì mở quyền rộng cho `others`, một nhóm người dùng hoặc dịch vụ có thể dùng chung một group. Ví dụ ứng dụng cần ghi nhật ký và nhóm vận hành cần đọc:

```text
owner: app
group: appops
mode : 640
```

Kiểm tra thành viên nhóm:

```bash
id username
getent group appops
```

Sau khi thêm một người dùng vào nhóm, phiên đăng nhập hiện tại có thể chưa nhận nhóm bổ sung mới cho tới khi mở phiên mới hoặc áp dụng cơ chế cập nhật tương ứng.

## `sudo`: ủy quyền đặc quyền

`sudo` không đơn giản là "biến thành root". Nó áp dụng chính sách để cho phép một danh tính chạy câu lệnh dưới danh tính đích, thường là `root`.

```bash
sudo systemctl restart nginx
```

Cách này thường tốt hơn giữ một shell root trong thời gian dài vì hành động cụ thể hơn và dễ kiểm tra lịch sử hơn.

```bash
sudo -u appuser env
```

chạy câu lệnh dưới danh tính khác, hữu ích khi muốn tái hiện môi trường và quyền của tài khoản dịch vụ.

`sudo -i` mở shell đăng nhập của root và nên dùng thận trọng vì từ thời điểm đó mọi câu lệnh đều có phạm vi ảnh hưởng lớn hơn.

## ACL: khi owner/group/others chưa đủ

**Danh sách kiểm soát truy cập (Access Control List / ACL)** theo POSIX cho phép cấp quyền chi tiết cho thêm người dùng hoặc nhóm mà không phải thay đổi mô hình chủ sở hữu chính.

```bash
getfacl file
setfacl -m u:deploy:r file
```

ACL hữu ích nhưng cũng làm chính sách quyền trở nên khó nhìn hơn. `ls -l` có thể hiển thị dấu `+`; nếu chỉ nhìn các bit quyền cơ bản, quản trị viên có thể bỏ sót ACL bổ sung.

## Các bit chế độ đặc biệt

`setuid`, `setgid` và **sticky bit** có ý nghĩa đặc biệt. Ví dụ sticky bit trên thư mục dùng chung như `/tmp` giúp hạn chế người dùng xóa mục thư mục thuộc người dùng khác dù thư mục có quyền ghi chung.

```bash
ls -ld /tmp
```

thường cho thấy ký tự `t` ở cuối phần quyền.

Tệp thực thi có `setuid` có thể làm tiến trình nhận `effective UID` theo chủ sở hữu của tệp trong các điều kiện phù hợp. Vì vậy cơ chế này có ảnh hưởng bảo mật lớn và không nên dùng như đường tắt để xử lý vấn đề quyền truy cập.

## Capabilities

Trong Unix truyền thống, root mang một gói đặc quyền rất lớn. **Linux capabilities** chia một phần đặc quyền thành các đơn vị nhỏ hơn như `CAP_NET_BIND_SERVICE`.

Ví dụ một tiến trình có thể được phép gắn vào cổng đặc quyền mà không cần toàn bộ quyền root, tùy mô hình triển khai. Đây là cách nguyên tắc đặc quyền tối thiểu được đưa xuống mức thông tin xác thực của kernel.

## SELinux và AppArmor

Các bit quyền truyền thống là một dạng **kiểm soát truy cập tùy ý (Discretionary Access Control / DAC)**. Bản phân phối Linux có thể bổ sung **kiểm soát truy cập bắt buộc (Mandatory Access Control / MAC)** như SELinux hoặc AppArmor. Vì vậy đặt `777` vẫn có thể không đủ nếu chính sách MAC từ chối thao tác.

Họ RHEL thường gặp SELinux; Ubuntu thường gặp AppArmor. Khi quyền trên tệp có vẻ đúng nhưng thao tác vẫn bị từ chối, cần kiểm tra khung bảo mật tương ứng thay vì tiếp tục mở rộng `chmod`.

## Quyền của khóa SSH

OpenSSH cố tình từ chối dùng khóa riêng tư có quyền quá rộng:

```bash
chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh
```

Đây không phải sự khó chịu vô lý. Khóa riêng tư là bí mật xác thực; nếu người dùng khác đọc được thì ranh giới danh tính không còn ý nghĩa.

## Mô hình tư duy (Mental Model)

Đừng chỉ hỏi "tệp có quyền gì?". Hãy nhìn toàn bộ chuỗi quyết định:

```text
thông tin xác thực của tiến trình
       +
quyền đi xuyên đường dẫn
       +
chủ sở hữu / mode / ACL của đối tượng
       +
chính sách MAC / bảo mật
       +
ràng buộc mount và runtime
       ↓
thao tác được cho phép hoặc bị từ chối
```

Quyền truy cập là một quyết định đối với **một thao tác cụ thể**, không phải thuộc tính đúng/sai đơn giản kiểu "tệp có truy cập được hay không".

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`777` giải quyết được vấn đề quyền."** Nó chỉ mở DAC rất rộng và có thể hoàn toàn không chạm tới nguyên nhân thật.

**"Root luôn không bị giới hạn."** Namespace, capability, MAC, mount chỉ đọc và chính sách container vẫn có thể giới hạn hoạt động.

**"Tệp ghi được thì chắc chắn xóa được."** `unlink` phụ thuộc mục thư mục và quyền của thư mục chứa.

**"Quản trị viên SSH đọc được nên dịch vụ cũng đọc được."** Hai tiến trình có thể chạy với thông tin xác thực hoàn toàn khác nhau.

**"`ls -l` cho thấy toàn bộ chính sách bảo mật."** ACL, SELinux/AppArmor và capabilities có thể bổ sung các ràng buộc khác.

## Kết nối kiến thức

Quyền truy cập chỉ có ý nghĩa khi gắn với danh tính của tiến trình. [Tiến trình, luồng, tín hiệu và tác vụ](../04_process/processes_threads_signals_jobs.md) giải thích vòng đời tiến trình và quyền gửi signal; [Bảo mật và gia cố hệ thống](../08_operations/security_hardening.md) mở rộng từ quyền tệp sang bề mặt tấn công và chính sách máy chủ.