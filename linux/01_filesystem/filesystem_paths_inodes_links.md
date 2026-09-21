# Hệ thống tệp, đường dẫn, inode và liên kết

Một trong những lỗi tư duy phổ biến khi học Linux là đồng nhất "tệp" với "tên tệp". Nếu hiểu rằng **đường dẫn (pathname)** chỉ là một tên trong **vùng tên (namespace)** dẫn tới một đối tượng của hệ thống tệp, nhiều hành vi tưởng như kỳ lạ sẽ trở nên hợp lý: một liên kết cứng (hard link) có thể tạo thêm tên cho cùng dữ liệu, đổi tên thường rất nhanh, và một tệp đã `rm` vẫn có thể chiếm dung lượng nếu tiến trình còn mở nó.

## Từ thiết bị lưu trữ khối tới hệ thống tệp

Ổ đĩa hoặc SSD về cơ bản cung cấp khả năng lưu trữ theo các khối (block). Nếu hệ thống chỉ có số thứ tự khối, ứng dụng phải tự nhớ khối nào thuộc tệp nào, đâu là siêu dữ liệu (metadata), đâu là vùng trống và làm sao phục hồi sau sự cố. **Hệ thống tệp (filesystem / 파일 시스템)** tạo ra một cấu trúc dữ liệu cao hơn để quản lý vùng tên, metadata, phân bổ không gian và tính nhất quán.

Các hệ thống tệp Linux phổ biến gồm ext4 và XFS. Hệ thống tệp không chỉ "chứa tệp"; nó định nghĩa cách các đối tượng, dữ liệu và metadata được tổ chức trên thiết bị lưu trữ.

## Đường dẫn là cách tìm đối tượng, không phải bản thân dữ liệu

Đường dẫn tuyệt đối bắt đầu từ thư mục gốc `/`:

```text
/var/log/myapp/app.log
```

Kernel phân giải từng thành phần: `/` → `var` → `log` → `myapp` → `app.log`. Vì vậy thư mục không chỉ là một "folder giao diện" mà tham gia trực tiếp vào việc ánh xạ tên tới đối tượng trong hệ thống tệp.

Đường dẫn tương đối được phân giải từ **thư mục làm việc hiện tại (current working directory)**:

```bash
pwd
cd /var/log
less myapp/app.log
```

`myapp/app.log` ở đây phụ thuộc vào thư mục hiện tại. Đây là lý do script dùng trong production phải thận trọng với đường dẫn tương đối: cùng một script chạy từ thư mục làm việc khác có thể tác động tới một đối tượng khác.

## Inode: danh tính của đối tượng trong hệ thống tệp

Trên nhiều hệ thống tệp kiểu Unix, **`inode` (아이노드)** chứa metadata của đối tượng như loại đối tượng, chủ sở hữu, quyền truy cập, dấu thời gian, kích thước và các tham chiếu tới vùng dữ liệu. Tên tệp không nằm trong `inode` theo cách người mới thường hình dung; **mục thư mục (directory entry)** ánh xạ một tên tới số `inode`.

Có thể quan sát bằng:

```bash
ls -li file.txt
stat file.txt
```

Tùy chọn `-i` hiển thị số `inode`.

Mô hình tư duy đơn giản:

```text
đường dẫn -> mục thư mục -> inode -> dữ liệu
```

Mô hình này đã đủ mạnh để suy luận nhiều tình huống thực tế dù chi tiết triển khai của từng hệ thống tệp có thể phức tạp hơn.

## Liên kết cứng: nhiều tên cùng trỏ tới một inode

Tạo liên kết cứng:

```bash
ln original.txt second-name.txt
ls -li original.txt second-name.txt
```

Hai mục thư mục có thể trỏ tới cùng một `inode`. Nếu sửa nội dung qua một tên, đọc qua tên kia cũng thấy thay đổi vì đây không phải hai bản sao độc lập.

`stat` cho thấy **số lượng liên kết (link count)**. Đối tượng dữ liệu chỉ có thể được thu hồi khi không còn liên kết thư mục thích hợp và không còn tham chiếu đang mở cần giữ đối tượng tồn tại.

Liên kết cứng thông thường không vượt qua ranh giới hệ thống tệp vì số `inode` chỉ có ý nghĩa trong hệ thống tệp tương ứng. Linux cũng thường không cho người dùng tạo hard link tới thư mục để tránh tạo chu trình phức tạp trong cây thư mục.

## Liên kết tượng trưng: một đối tượng chứa đường dẫn tới tên khác

**Liên kết tượng trưng (symbolic link / 심볼릭 링크)** khác với hard link. Nó là một đối tượng riêng chứa đường dẫn đích:

```bash
ln -s /opt/app/releases/2026-09-20 /opt/app/current
ls -l /opt/app/current
```

Khi truy cập `current`, quá trình phân giải đường dẫn tiếp tục theo đích của symlink. Vì đích là một đường dẫn, symlink có thể vượt ranh giới hệ thống tệp và có thể trở thành **liên kết hỏng (broken link)** nếu đích biến mất.

Một mẫu triển khai thường gặp:

```text
/opt/app/releases/v1
/opt/app/releases/v2
/opt/app/current -> /opt/app/releases/v2
```

Chuyển symlink `current` cho phép đổi bản phát hành nhanh mà không cần sao chép lại toàn bộ thư mục. Đây là ứng dụng trực tiếp của việc tách **tên** khỏi **đối tượng/dữ liệu**.

## Tại sao xóa tệp đang mở vẫn có thể chiếm dung lượng?

Giả sử ứng dụng đang ghi vào `app.log`, sau đó quản trị viên chạy:

```bash
rm app.log
```

`rm` chủ yếu gỡ liên kết giữa tên trong thư mục và đối tượng bên dưới. Nếu tiến trình vẫn giữ **bộ mô tả tệp đang mở (open file descriptor)** tới `inode`, kernel phải giữ đối tượng vì tiến trình vẫn sử dụng nó. `ls` không còn thấy tên đường dẫn, nhưng `df` có thể chưa giảm dung lượng sử dụng.

Có thể tìm các tệp đã bị xóa tên nhưng vẫn đang được mở:

```bash
sudo lsof +L1
```

Đây là một tình huống production rất quan trọng để hiểu mô hình tham chiếu của `inode`. Khởi động lại tiến trình có thể làm tham chiếu được giải phóng, nhưng trước đó cần xác nhận đúng tiến trình và nguyên nhân khiến nhật ký tăng bất thường.

## `df` và `du` trả lời hai câu hỏi khác nhau

`df` hỏi hệ thống tệp về dung lượng đã phân bổ và còn khả dụng:

```bash
df -h
```

`du` duyệt cây thư mục và cộng dung lượng của các đối tượng có thể nhìn thấy qua vùng tên:

```bash
du -xhd1 /var | sort -hr
```

Vì hai công cụ đo theo cách khác nhau, kết quả có thể lệch đáng kể, đặc biệt khi có tệp đã xóa nhưng vẫn mở, điểm gắn kết (mount) hoặc tệp thưa (sparse file). Không nên kết luận một công cụ "sai" trước khi hiểu câu hỏi mà nó đang trả lời.

## Mount: ghép nhiều hệ thống tệp vào một vùng tên chung

Linux không trình bày mỗi thiết bị lưu trữ bằng một ký tự ổ đĩa riêng như `C:` hoặc `D:`. Một hệ thống tệp được **gắn (mount / 마운트)** vào một **điểm gắn kết (mount point)** trong cây thư mục chung.

```bash
findmnt
findmnt /data
lsblk -f
```

Ví dụ một hệ thống tệp trên thiết bị khác có thể được gắn tại `/data`. Khi tiến trình đi qua `/data`, nó bước vào hệ thống tệp khác nhưng đường dẫn vẫn nằm trong cùng cây bắt đầu từ `/`.

Điều này giải thích vì sao `du /` có thể vô tình đi vào NFS hoặc một volume lớn. Tùy chọn `-x` yêu cầu `du` không vượt sang hệ thống tệp khác:

```bash
sudo du -xhd1 / | sort -hr
```

## Cấu trúc thư mục chuẩn và các quy ước phổ biến

Không phải mọi bản phân phối giống hoàn toàn, nhưng một số đường dẫn có vai trò thường gặp:

| Đường dẫn | Vai trò thường gặp |
|---|---|
| `/etc` | cấu hình hệ thống và ứng dụng |
| `/var` | dữ liệu thay đổi thường xuyên như nhật ký, hàng đợi, bộ nhớ đệm |
| `/var/log` | nhật ký hệ thống và ứng dụng theo cách tổ chức truyền thống |
| `/home` | thư mục cá nhân của người dùng thông thường |
| `/root` | thư mục cá nhân của `root` |
| `/tmp` | dữ liệu tạm thời |
| `/usr` | phần lớn chương trình, thư viện và dữ liệu của không gian người dùng |
| `/opt` | phần mềm tùy chọn hoặc bên thứ ba, thường dùng cho ứng dụng nội bộ |
| `/run` | trạng thái tạm thời của lần khởi động hiện tại |
| `/proc` | hệ thống tệp giả cho trạng thái tiến trình và kernel |
| `/sys` | `sysfs` cho mô hình thiết bị và kernel |
| `/dev` | các nút thiết bị (device node) |

Đây là quy ước chứ không phải luật buộc mọi ứng dụng phải đặt dữ liệu theo đúng một cách duy nhất.

## Quyền truy cập trong quá trình phân giải đường dẫn

Để truy cập `/a/b/file`, quyền của riêng `file` chưa phải toàn bộ câu chuyện. Tiến trình phải có khả năng đi xuyên qua các thư mục cha. Bit thực thi `x` trên thư mục mang ý nghĩa **tìm kiếm/đi xuyên (search/traverse)**.

Khi tệp có vẻ có quyền đúng nhưng ứng dụng vẫn báo `Permission denied`, một câu lệnh rất hữu ích là:

```bash
namei -l /a/b/file
```

Nó cho phép xem quyền của từng thành phần trong đường dẫn.

## Các dấu thời gian: `mtime`, `ctime`, `atime`

`mtime` phản ánh thời điểm nội dung tệp thay đổi. `ctime` trên Unix không có nghĩa đơn giản là "thời gian tạo"; nó phản ánh thời điểm trạng thái/metadata của `inode` thay đổi. `atime` liên quan thời điểm truy cập và có thể được chính sách của hệ thống tệp tối ưu để tránh phát sinh quá nhiều thao tác ghi.

```bash
stat file.txt
```

Hiểu đúng các dấu thời gian rất quan trọng khi điều tra "tệp bị thay lúc nào". `ctime` thay đổi không nhất thiết có nghĩa nội dung thay đổi; `chmod` hoặc `chown` cũng có thể làm metadata thay đổi.

## Cạn kiệt inode

Hệ thống tệp có thể không tạo thêm tệp mới dù vẫn còn nhiều byte trống nếu tài nguyên `inode` đã cạn. Triệu chứng thường là `No space left on device` trong khi `df -h` vẫn cho thấy còn dung lượng.

```bash
df -i
```

Một ứng dụng tạo hàng triệu tệp rất nhỏ có thể gây tình huống này. Vì vậy lập kế hoạch dung lượng không chỉ là GB/TB; số lượng đối tượng cũng có thể trở thành giới hạn.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Tên tệp chính là tệp."** Tên tệp là một mục trong thư mục dẫn tới đối tượng. Hard link cho thấy cùng một đối tượng có thể có nhiều tên.

**"`rm` chắc chắn giải phóng dung lượng ngay."** Không nếu đối tượng vẫn còn tham chiếu đang mở.

**"Symlink hoàn toàn giống shortcut."** So sánh với shortcut giúp hình dung ban đầu, nhưng symlink tham gia trực tiếp vào quá trình phân giải đường dẫn và có quy tắc riêng.

**"`ctime` là thời gian tạo tệp."** Trên Unix truyền thống, `ctime` là thời gian trạng thái `inode` thay đổi.

**"Quyền của tệp đúng thì chắc chắn đọc được."** Quyền đi xuyên thư mục cha, ACL, SELinux/AppArmor và tùy chọn mount cũng có thể ảnh hưởng.

## Kết nối kiến thức

Chỉ mục cơ sở dữ liệu và cặp thư mục/`inode` của hệ thống tệp không phải cùng một cấu trúc dữ liệu, nhưng có một điểm chung đáng chú ý: cả hai đều tách **khóa tra cứu logic** khỏi **vị trí dữ liệu vật lý**. Ứng dụng dùng đường dẫn; hệ thống tệp chịu trách nhiệm phân giải và xác định đối tượng thực tế. Lớp trừu tượng này cho phép bố trí lưu trữ thay đổi mà ứng dụng không cần biết sector cụ thể.

Mô hình hệ thống tệp dẫn trực tiếp tới [Tệp, luồng dữ liệu và bộ mô tả tệp](./files_streams_descriptors.md), nơi câu hỏi chuyển từ "đối tượng nằm ở đâu trong vùng tên?" sang "tiến trình đang giữ và thực hiện I/O với đối tượng bằng cách nào?".