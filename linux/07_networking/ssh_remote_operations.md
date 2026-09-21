# SSH, khóa, đường hầm và thao tác từ xa

SSH (Secure Shell / 보안 셸) giải quyết một vấn đề sâu hơn việc "mở terminal từ xa": làm sao thiết lập một **kênh giao tiếp được mã hóa và xác thực** qua một mạng không hoàn toàn đáng tin cậy. Kênh này bảo vệ tính bí mật (confidentiality), tính toàn vẹn (integrity) và danh tính của hai đầu kết nối. Trên đó có thể mở shell từ xa, chạy câu lệnh, truyền tệp và tạo đường hầm mạng.

## SSH nằm ở đâu trong ngăn xếp mạng?

SSH thường chạy trên TCP, mặc định cổng 22. Trước khi xác thực SSH diễn ra, máy khách vẫn phải giải quyết DNS, định tuyến và khả năng kết nối TCP.

```bash
nc -vz server.example.com 22
ssh -v user@server.example.com
```

Nếu TCP không kết nối được, thay đổi khóa SSH thường không giải quyết vấn đề. Nếu TCP kết nối được nhưng xác thực thất bại, phạm vi điều tra chuyển lên tầng giao thức SSH và danh tính.

## Danh tính máy chủ và host key

Khi kết nối lần đầu, SSH client yêu cầu xác nhận **dấu vân tay khóa máy chủ (host key fingerprint)**. Cơ chế này giúp máy khách xác minh danh tính máy chủ và giảm nguy cơ tấn công trung gian (man-in-the-middle) khi mô hình tin cậy được quản lý đúng.

`known_hosts` lưu những danh tính máy chủ đã biết. Cảnh báo host key thay đổi không nên được "sửa" bằng cách xóa mục tương ứng ngay lập tức; trước hết cần xác minh máy chủ có thực sự được cài lại, thay khóa hay đang có bất thường về bảo mật hoặc đường mạng.

## Xác thực người dùng

SSH có thể dùng mật khẩu, xác thực bằng khóa công khai và các cơ chế khác. Với xác thực khóa, máy khách giữ **khóa riêng tư (private key)**; máy chủ lưu khóa công khai được cho phép, thường trong `~/.ssh/authorized_keys`.

Khóa riêng tư không được gửi sang máy chủ như mật khẩu. Máy khách chứng minh rằng mình đang sở hữu khóa thông qua giao thức mật mã.

```bash
ssh -i ~/.ssh/prod_key app@server
```

Quyền của khóa riêng tư cần đủ chặt:

```bash
chmod 600 ~/.ssh/prod_key
chmod 700 ~/.ssh
```

## Mô hình khóa công khai và khóa riêng tư

Khóa công khai có thể phân phối tới nơi cần xác minh danh tính; khóa riêng tư phải được giữ bí mật. Nếu khóa riêng tư bị lộ, kẻ tấn công có thể giả mạo danh tính tại những nơi khóa đó được cho phép, trừ khi còn các lớp kiểm soát khác.

Vì vậy quản lý khóa thực chất là một phần của **quản lý danh tính**, không chỉ là quản lý tệp.

## Gỡ lỗi quá trình xác thực

```bash
ssh -vvv user@host
```

Đầu ra chi tiết cho biết cấu hình nào được áp dụng, khóa nào được đưa ra thử, phương thức xác thực nào được dùng và giao thức tiến triển tới đâu. Không nên chỉ nhìn dòng cuối `Permission denied`; cần xác định khóa nào thực sự được thử và máy chủ chấp nhận hay từ chối ở bước nào.

Nhật ký phía máy chủ tùy bản phân phối:

```bash
journalctl -u ssh
journalctl -u sshd
```

## `~/.ssh/config`

Thay vì nhớ một câu lệnh dài:

```sshconfig
Host prod-app
    HostName 10.0.1.20
    User app
    Port 22
    IdentityFile ~/.ssh/prod_key
    ServerAliveInterval 60
```

sau đó có thể dùng:

```bash
ssh prod-app
```

Tệp cấu hình giúp chuẩn hóa kết nối nhưng có thể chứa metadata về hạ tầng, vì vậy cần cân nhắc quyền truy cập và việc đưa vào hệ thống quản lý mã nguồn.

## Máy trung gian: jump host / bastion

Máy chủ riêng tư thường không mở SSH trực tiếp ra Internet. Máy khách đi qua một **máy trung gian (jump host / bastion)**:

```bash
ssh -J user@bastion app@10.0.1.20
```

`ProxyJump` làm đường kết nối rõ ràng hơn việc SSH lồng thủ công. Có thể khai báo `ProxyJump` trong `~/.ssh/config`.

Lợi ích bảo mật đến từ việc giảm bề mặt tấn công của các máy riêng tư, nhưng bastion trở thành một điểm kiểm soát có giá trị cao và cần được gia cố, ghi nhật ký và kiểm tra truy cập cẩn thận.

## Chuyển tiếp cổng cục bộ

Giả sử cơ sở dữ liệu chỉ có thể truy cập từ bastion hoặc mạng nội bộ:

```bash
ssh -N -L 15432:db.internal:5432 user@bastion
```

Ứng dụng cục bộ kết nối tới `localhost:15432`; SSH chuyển các byte qua kênh mã hóa tới bastion, sau đó bastion kết nối tiếp tới `db.internal:5432`.

Mô hình tư duy:

```text
ứng dụng cục bộ -> localhost:15432 -> SSH tunnel -> bastion -> db.internal:5432
```

`-N` cho biết không cần chạy lệnh từ xa, chỉ cần giữ kết nối và chuyển tiếp cổng.

Đường hầm không biến cơ sở dữ liệu thành tiến trình cục bộ; nó chỉ tạo thêm một đường truyền mạng qua SSH.

## Chuyển tiếp từ xa và chuyển tiếp động

SSH còn hỗ trợ **chuyển tiếp cổng từ xa (remote forwarding)** bằng `-R` và **chuyển tiếp động SOCKS (dynamic forwarding)** bằng `-D`. Đây là các công cụ mạnh nhưng có ảnh hưởng bảo mật: đường hầm có thể vô tình vượt qua ranh giới mạng dự kiến nếu chính sách cho phép. Việc sử dụng trong production phải tuân thủ chính sách truy cập của hệ thống.

## SCP, SFTP và `rsync`

`scp` sao chép tệp qua giao thức SSH:

```bash
scp app.jar app@server:/tmp/
scp app@server:/var/log/app.log .
```

Cổng tùy chỉnh của `scp` dùng `-P` viết hoa:

```bash
scp -P 2222 app.jar user@host:/tmp/
```

SFTP cung cấp giao thức truyền tệp trên SSH với các thao tác tương tác hoặc tự động hóa tùy client.

`rsync` phù hợp với đồng bộ lặp lại vì có thể chỉ truyền phần khác biệt và giữ nhiều loại metadata:

```bash
rsync -avh --progress ./build/ app@server:/opt/app/
```

Dấu `/` ở cuối đường dẫn nguồn rất quan trọng: `src/` thường biểu thị nội dung bên trong thư mục, còn `src` có thể tạo thêm một cấp thư mục ở đích.

## `rsync --delete` và chạy thử

Đồng bộ dạng phản chiếu:

```bash
rsync -avh --delete ./site/ server:/var/www/site/
```

`--delete` có thể xóa dữ liệu ở đích không còn tồn tại ở nguồn. Thói quen tốt ở mức vận hành nâng cao là chạy thử trước:

```bash
rsync -avhn --delete ./site/ server:/var/www/site/
```

`-n` hoặc `--dry-run` chỉ mô phỏng thay đổi. Hãy kiểm tra kết quả trước khi chạy thật.

## Keepalive

Thiết bị mạng có thể ngắt phiên SSH nhàn rỗi. Tùy chọn phía máy khách:

```bash
ssh -o ServerAliveInterval=60 user@host
```

định kỳ gửi keepalive ở mức giao thức. Không nên đặt chu kỳ quá ngắn cho số lượng phiên rất lớn nếu chưa hiểu chi phí và chính sách mạng.

## SSH agent

`ssh-agent` giữ khả năng ký bằng khóa riêng tư trong phiên để tránh phải đọc khóa hoặc nhập lại passphrase liên tục. **Chuyển tiếp agent (agent forwarding)** cho phép máy từ xa dùng agent cục bộ nhưng cũng tạo rủi ro: nếu máy từ xa bị xâm nhập, kẻ tấn công có thể lợi dụng agent đang được chuyển tiếp trong thời gian phiên còn tồn tại. Chỉ bật khi thực sự cần và hiểu ranh giới tin cậy.

## PuTTY nằm ở đâu trong mô hình này?

PuTTY là một SSH client phổ biến trên Windows. Sau khi kết nối, các câu lệnh Linux không phải "câu lệnh của PuTTY"; chúng được chạy trong shell trên máy chủ Linux từ xa. PuTTY quản lý phía terminal/SSH client, còn `ls`, `ps`, `journalctl` và các chương trình khác chạy ở phía máy chủ.

## Mô hình tư duy (Mental Model)

SSH tạo ra một **kênh truyền được xác thực và mã hóa**. Shell từ xa, SCP/SFTP và chuyển tiếp cổng chỉ là các dịch vụ sử dụng kênh đó. Khi lỗi, nên phân tách theo lớp:

```text
DNS / kết nối TCP
-> host key và mô hình tin cậy
-> xác thực người dùng
-> phân quyền / shell
-> ứng dụng chạy qua kênh
```

## Những hiểu lầm phổ biến (Common Misconceptions)

**"SSH key là một tệp mật khẩu."** Xác thực khóa công khai dùng bằng chứng mật mã; khóa riêng tư không nên được gửi sang máy chủ.

**"Host key thay đổi thì cứ xóa `known_hosts`."** Cần xác minh thay đổi danh tính máy chủ trước.

**"SCP và rsync giống nhau."** Cả hai đều truyền tệp, nhưng `rsync` có ngữ nghĩa đồng bộ, so sánh khác biệt và giữ metadata mạnh hơn.

**"SSH tunnel làm dịch vụ được mở trực tiếp ra Internet."** Tunnel chỉ tạo đường chuyển tiếp qua các điểm cuối SSH; mức phơi bày thực tế còn phụ thuộc địa chỉ bind, chính sách và topology.

**"PuTTY có bộ câu lệnh Linux riêng."** Các câu lệnh chạy trên hệ điều hành và shell từ xa.

## Kết nối kiến thức

SSH phụ thuộc trực tiếp vào [mạng](./networking_dns_sockets_ports.md), [người dùng và quyền truy cập](../03_identity/users_groups_permissions.md) cùng mô hình danh tính mật mã. Bảng câu lệnh thực hành nằm tại [Tham chiếu câu lệnh PuTTY/SSH Linux](../reference/putty_ssh_linux_server_commands.md).