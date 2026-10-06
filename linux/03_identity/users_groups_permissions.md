# Người dùng, nhóm, quyền truy cập và đặc quyền

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Người dùng, nhóm, quyền truy cập và đặc quyền**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Người dùng không chỉ là tên đăng nhập** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Các bit quyền truy cập** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối user/group với permission bits và đặc quyền, để xác định chính xác danh tính nào bị kernel từ chối trên đối tượng nào.

Mô hình quyền của Linux tồn tại vì một máy có thể chạy nhiều tiến trình thuộc nhiều danh tính bảo mật khác nhau nhưng cùng chia sẻ hệ thống tệp, mạng và thiết bị. Câu hỏi nền tảng không phải "nên chmod số nào?" mà là: **tiến trình nào đang yêu cầu thao tác trên đối tượng nào, với thông tin xác thực nào, và kernel đang áp dụng chính sách nào?**

## Người dùng không chỉ là tên đăng nhập

Kernel chủ yếu làm việc với **UID (user ID)** và **GID (Group ID)** dạng số. Tên người dùng và tên nhóm là ánh xạ dễ đọc cho con người do cơ sở dữ liệu không gian người dùng như `/etc/passwd`, `/etc/group` hoặc dịch vụ thư mục cung cấp.

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

> **Nối mạch:** Trong **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Các bit quyền truy cập** nối từ **Người dùng không chỉ là tên đăng nhập** sang **Quyền trên tệp và thư mục có ý nghĩa khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các bit quyền truy cập

Chế độ quyền Unix truyền thống chia thành chủ sở hữu (owner), nhóm (group), người khác (others) và ba quyền cơ bản:

- `r` — đọc (read);
- `w` — ghi (write / 쓰기);
- `x` — thực thi hoặc đi xuyên thư mục (execute/search).

```text
-rwxr-x---
```

Có thể đọc thành: đơn vị sở hữu (owner / 오너) `rwx`, group `r-x`, others `---`.

Cách viết bằng số dùng các giá trị bit 4/2/1:

```text
7 = 4+2+1 = rwx
6 = 4+2   = rw-
5 = 4+1   = r-x
4 = 4     = r--
```

Vì vậy `chmod 640 config.yml` nghĩa là chủ sở hữu được đọc/ghi, nhóm được đọc và người khác không có quyền.

Nếu chỉ học các con số mà không hiểu ý nghĩa của quyền trên thư mục, việc đặt quyền rất dễ sai.

> **Nối mạch:** Ở chặng này của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Quyền trên tệp và thư mục có ý nghĩa khác nhau** nối từ **Các bit quyền truy cập** sang **Tại sao xóa tệp lại phụ thuộc quyền của thư mục?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quyền trên tệp và thư mục có ý nghĩa khác nhau

Với tệp thông thường, `r` cho phép đọc nội dung, `w` cho phép sửa nội dung, `x` cho phép thực thi nếu định dạng tệp và trình thông dịch phù hợp.

Với thư mục, `r` liên quan tới việc liệt kê tên, `w` liên quan tới việc thay đổi các mục thư mục, còn `x` mang nghĩa **tìm kiếm/đi xuyên (search/traverse)**. Để mở `/opt/app/config/a.yml`, tiến trình phải có khả năng đi xuyên các thư mục cha.

```bash
namei -l /opt/app/config/a.yml
```

Câu lệnh này rất hữu ích khi tệp cuối cùng có quyền `644` nhưng ứng dụng vẫn báo `Permission denied`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Tại sao xóa tệp lại phụ thuộc quyền của thư mục?** nối từ **Quyền trên tệp và thư mục có ý nghĩa khác nhau** sang **Chủ sở hữu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tại sao xóa tệp lại phụ thuộc quyền của thư mục?

Xóa một đường dẫn là thay đổi mục thư mục. Vì vậy khả năng chạy `rm file` phụ thuộc mạnh vào quyền của thư mục chứa nó, chứ không chỉ phụ thuộc bit ghi trên bản thân tệp. Đây là hệ quả trực tiếp của mô hình vùng tên trong [Hệ thống tệp, đường dẫn, inode và liên kết](../01_filesystem/filesystem_paths_inodes_links.md).

> **Nối mạch:** Trong **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Chủ sở hữu** nối từ **Tại sao xóa tệp lại phụ thuộc quyền của thư mục?** sang **Vì sao chmod -R 777 là một cách làm không tốt?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chủ sở hữu

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
chown app:app application.yml
```

làm thay đổi người sở hữu và nhóm. Thao tác đệ quy:

```bash
chown -R app:app /opt/app
```

có phạm vi ảnh hưởng lớn. Một thói quen tốt trong môi trường vận hành (production / 운영 환경) là kiểm tra cây thư mục trước và tránh chạy lệnh đệ quy trên đường dẫn chưa được xác minh.

> **Nối mạch:** Ở chặng này của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Vì sao chmod -R 777 là một cách làm không tốt?** nối từ **Chủ sở hữu** sang **umask**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao `chmod -R 777` là một cách làm không tốt?

`777` cấp quyền đọc, ghi và thực thi cho tất cả các nhóm quyền. Nó có thể làm triệu chứng về quyền biến mất nhưng đồng thời phá vỡ ranh giới bảo mật và cấp bit thực thi cho những tệp dữ liệu không cần thực thi.

Khi cần đặt quyền cho cả cây thư mục, thường nên phân biệt thư mục và tệp:

```bash
find /opt/app -type d -exec chmod 755 {} +
find /opt/app -type f -exec chmod 644 {} +
```

Sau đó chỉ cấp quyền đặc biệt cho tệp thực thi, cấu hình hoặc bí mật theo nhu cầu thực tế.

Nguyên tắc **đặc quyền tối thiểu (least privilege / 최소 권한)** yêu cầu chỉ cấp khả năng cần thiết cho một nhiệm vụ, thay vì mở quyền rộng chỉ để việc gỡ lỗi trở nên dễ hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **umask** nối từ **Vì sao chmod -R 777 là một cách làm không tốt?** sang **Nhóm như một cơ chế chia sẻ quyền**, vì cơ chế trước tạo đầu vào cho bước sau.

## `umask`

Khi tiến trình tạo tệp với một chế độ quyền yêu cầu, **`umask`** loại bỏ một số quyền mặc định.

```bash
umask
```

Giá trị thường gặp `0022` thường dẫn tới tệp có quyền `644` và thư mục `755` khi chương trình yêu cầu chế độ mặc định tương ứng. Vì thế hai dịch vụ có `umask` khác nhau có thể tạo ra tệp với quyền khác nhau dù mã nguồn giống nhau.

> **Nối mạch:** Trong **Người dùng, nhóm, quyền truy cập và đặc quyền**, **umask** đặt đầu vào cho **Nhóm như một cơ chế chia sẻ quyền**, rồi **sudo: ủy quyền đặc quyền** mở rộng hệ quả hoặc giới hạn liên quan.

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

> **Nối mạch:** Ở chặng này của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Nhóm như một cơ chế chia sẻ quyền** đặt đầu vào cho **sudo: ủy quyền đặc quyền**, rồi **ACL: khi đơn vị sở hữu (owner / 오너)/group/others chưa đủ** mở rộng hệ quả hoặc giới hạn liên quan.

## `sudo`: ủy quyền đặc quyền

`sudo` không đơn giản là "biến thành gốc (root / 루트)". Nó áp dụng chính sách để cho phép một danh tính chạy câu lệnh dưới danh tính đích, thường là `root`.

```bash
sudo systemctl restart nginx
```

Cách này thường tốt hơn giữ một shell gốc (root / 루트) trong thời gian dài vì hành động cụ thể hơn và dễ kiểm tra lịch sử hơn.

```bash
sudo -u appuser env
```

chạy câu lệnh dưới danh tính khác, hữu ích khi muốn tái hiện môi trường và quyền của tài khoản dịch vụ.

`sudo -i` mở shell đăng nhập của gốc (root / 루트) và nên dùng thận trọng vì từ thời điểm đó mọi câu lệnh đều có phạm vi ảnh hưởng lớn hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Người dùng, nhóm, quyền truy cập và đặc quyền**, sau nội dung của **sudo: ủy quyền đặc quyền**, **ACL: khi đơn vị sở hữu (owner / 오너)/group/others chưa đủ** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Các bit chế độ đặc biệt** mở rộng hệ quả hoặc giới hạn liên quan.

## ACL: khi đơn vị sở hữu (owner / 오너)/group/others chưa đủ

**Danh sách kiểm soát truy cập (Access Control List / ACL)** theo POSIX cho phép cấp quyền chi tiết cho thêm người dùng hoặc nhóm mà không phải thay đổi mô hình chủ sở hữu chính.

```bash
getfacl file
setfacl -m u:deploy:r file
```

ACL hữu ích nhưng cũng làm chính sách quyền trở nên khó nhìn hơn. `ls -l` có thể hiển thị dấu `+`; nếu chỉ nhìn các bit quyền cơ bản, quản trị viên có thể bỏ sót ACL bổ sung.

> **Nối mạch:** Trong **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Các bit chế độ đặc biệt** nối từ **ACL: khi đơn vị sở hữu (owner / 오너)/group/others chưa đủ** sang **Capabilities**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các bit chế độ đặc biệt

`setuid`, `setgid` và **sticky bit** có ý nghĩa đặc biệt. Ví dụ sticky bit trên thư mục dùng chung như `/tmp` giúp hạn chế người dùng xóa mục thư mục thuộc người dùng khác dù thư mục có quyền ghi chung.

```bash
ls -ld /tmp
```

thường cho thấy ký tự `t` ở cuối phần quyền.

Tệp thực thi có `setuid` có thể làm tiến trình nhận `effective UID` theo chủ sở hữu của tệp trong các điều kiện phù hợp. Vì vậy cơ chế này có ảnh hưởng bảo mật lớn và không nên dùng như đường tắt để xử lý vấn đề quyền truy cập.

> **Nối mạch:** Ở chặng này của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Capabilities** nối từ **Các bit chế độ đặc biệt** sang **SELinux và AppArmor**, vì cơ chế trước tạo đầu vào cho bước sau.

## Capabilities

Trong Unix truyền thống, gốc (root / 루트) mang một gói đặc quyền rất lớn. **Linux capabilities** chia một phần đặc quyền thành các đơn vị nhỏ hơn như `CAP_NET_BIND_SERVICE`.

Ví dụ một tiến trình có thể được phép gắn vào cổng đặc quyền mà không cần toàn bộ quyền gốc (root / 루트), tùy mô hình triển khai. Đây là cách nguyên tắc đặc quyền tối thiểu được đưa xuống mức thông tin xác thực của kernel.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **SELinux và AppArmor** nối từ **Capabilities** sang **Quyền của khóa SSH**, vì cơ chế trước tạo đầu vào cho bước sau.

## SELinux và AppArmor

Các bit quyền truyền thống là một dạng **kiểm soát truy cập tùy ý (Discretionary Access Control / DAC)**. Bản phân phối Linux có thể bổ sung **kiểm soát truy cập bắt buộc (Mandatory Access Control / MAC)** như SELinux hoặc AppArmor. Vì vậy đặt `777` vẫn có thể không đủ nếu chính sách MAC từ chối thao tác.

Họ RHEL thường gặp SELinux; Ubuntu thường gặp AppArmor. Khi quyền trên tệp có vẻ đúng nhưng thao tác vẫn bị từ chối, cần kiểm tra khung bảo mật tương ứng thay vì tiếp tục mở rộng `chmod`.

> **Nối mạch:** Trong **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Quyền của khóa SSH** nối từ **SELinux và AppArmor** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quyền của khóa SSH

OpenSSH cố tình từ chối dùng khóa riêng tư có quyền quá rộng:

```bash
chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh
```

Đây không phải sự khó chịu vô lý. Khóa riêng tư là bí mật xác thực; nếu người dùng khác đọc được thì ranh giới danh tính không còn ý nghĩa.

> **Nối mạch:** Ở chặng này của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Quyền của khóa SSH** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Những hiểu lầm phổ biến (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`777` giải quyết được vấn đề quyền."** Nó chỉ mở DAC rất rộng và có thể hoàn toàn không chạm tới nguyên nhân thật.

**"gốc (root / 루트) luôn không bị giới hạn."** không gian tên (namespace / 네임스페이스), năng lực (capability / 역량), MAC, mount chỉ đọc và chính sách bộ chứa (container / 컨테이너) vẫn có thể giới hạn hoạt động.

**"Tệp ghi được thì chắc chắn xóa được."** `unlink` phụ thuộc mục thư mục và quyền của thư mục chứa.

**"Quản trị viên SSH đọc được nên dịch vụ cũng đọc được."** Hai tiến trình có thể chạy với thông tin xác thực hoàn toàn khác nhau.

**"`ls -l` cho thấy toàn bộ chính sách bảo mật."** ACL, SELinux/AppArmor và capabilities có thể bổ sung các ràng buộc khác.

> **Nối mạch:** Trong **Người dùng, nhóm, quyền truy cập và đặc quyền**, **Kết nối kiến thức** nối từ **Những hiểu lầm phổ biến (Common Misconceptions)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết nối kiến thức

Quyền truy cập chỉ có ý nghĩa khi gắn với danh tính của tiến trình. [Tiến trình, luồng, tín hiệu và tác vụ](../04_process/processes_threads_signals_jobs.md) giải thích vòng đời tiến trình và quyền gửi signal; [Bảo mật và gia cố hệ thống](../08_operations/security_hardening.md) mở rộng từ quyền tệp sang bề mặt tấn công và chính sách máy chủ.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
