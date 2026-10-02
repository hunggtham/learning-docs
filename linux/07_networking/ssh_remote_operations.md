# SSH, khóa, đường hầm và thao tác từ xa

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **SSH, khóa, đường hầm và thao tác từ xa**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **SSH nằm ở đâu trong ngăn xếp mạng?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Danh tính máy chủ và host key** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối SSH với trust, authentication và remote operations, để mỗi phiên quản trị có thể được kiểm chứng từ khóa đến lệnh chạy.

SSH (Secure Shell / 보안 셸) giải quyết một vấn đề sâu hơn việc "mở terminal từ xa": làm sao thiết lập một **kênh giao tiếp được mã hóa và xác thực** qua một mạng không hoàn toàn đáng tin cậy. Kênh này bảo vệ tính bí mật (confidentiality), tính toàn vẹn (integrity) và danh tính của hai đầu kết nối. Trên đó có thể mở shell từ xa, chạy câu lệnh, truyền tệp và tạo đường hầm mạng.

## SSH nằm ở đâu trong ngăn xếp mạng?

SSH thường chạy trên TCP, mặc định cổng 22. Trước khi xác thực SSH diễn ra, máy khách vẫn phải giải quyết DNS, định tuyến và khả năng kết nối TCP.

```bash
nc -vz server.example.com 22
ssh -v user@server.example.com
```

Nếu TCP không kết nối được, thay đổi khóa SSH thường không giải quyết vấn đề. Nếu TCP kết nối được nhưng xác thực thất bại, phạm vi điều tra chuyển lên tầng giao thức SSH và danh tính.

> **Chuyển mạch:** Trong **SSH, khóa, đường hầm và thao tác từ xa**, **Danh tính máy chủ và host key** tiếp nhận điểm tựa từ **SSH nằm ở đâu trong ngăn xếp mạng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xác thực người dùng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Danh tính máy chủ và host key

Khi kết nối lần đầu, SSH máy khách (client / 클라이언트) yêu cầu xác nhận **dấu vân tay khóa máy chủ (host key fingerprint)**. Cơ chế này giúp máy khách xác minh danh tính máy chủ và giảm nguy cơ tấn công trung gian (man-in-the-middle) khi mô hình tin cậy được quản lý đúng.

`known_hosts` lưu những danh tính máy chủ đã biết. Cảnh báo host key thay đổi không nên được "sửa" bằng cách xóa mục tương ứng ngay lập tức; trước hết cần xác minh máy chủ có thực sự được cài lại, thay khóa hay đang có bất thường về bảo mật hoặc đường mạng.

> **Chuyển mạch:** Ở chặng này của **SSH, khóa, đường hầm và thao tác từ xa**, **Xác thực người dùng** tiếp nhận điểm tựa từ **Danh tính máy chủ và host key** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình khóa công khai và khóa riêng tư** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SSH, khóa, đường hầm và thao tác từ xa**, **Mô hình khóa công khai và khóa riêng tư** tiếp nhận điểm tựa từ **Xác thực người dùng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gỡ lỗi quá trình xác thực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình khóa công khai và khóa riêng tư

Khóa công khai có thể phân phối tới nơi cần xác minh danh tính; khóa riêng tư phải được giữ bí mật. Nếu khóa riêng tư bị lộ, kẻ tấn công có thể giả mạo danh tính tại những nơi khóa đó được cho phép, trừ khi còn các lớp kiểm soát khác.

Vì vậy quản lý khóa thực chất là một phần của **quản lý danh tính**, không chỉ là quản lý tệp.

> **Chuyển mạch:** Trong **SSH, khóa, đường hầm và thao tác từ xa**, **Gỡ lỗi quá trình xác thực** tiếp nhận điểm tựa từ **Mô hình khóa công khai và khóa riêng tư** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **/.ssh/config** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gỡ lỗi quá trình xác thực

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
ssh -vvv user@host
```

Đầu ra chi tiết cho biết cấu hình nào được áp dụng, khóa nào được đưa ra thử, phương thức xác thực nào được dùng và giao thức tiến triển tới đâu. Không nên chỉ nhìn dòng cuối `Permission denied`; cần xác định khóa nào thực sự được thử và máy chủ chấp nhận hay từ chối ở bước nào.

Nhật ký phía máy chủ tùy bản phân phối:

```bash
journalctl -u ssh
journalctl -u sshd
```

> **Chuyển mạch:** Ở chặng này của **SSH, khóa, đường hầm và thao tác từ xa**, **/.ssh/config** tiếp nhận điểm tựa từ **Gỡ lỗi quá trình xác thực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Máy trung gian: jump host / bastion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Tệp cấu hình giúp chuẩn hóa kết nối nhưng có thể chứa siêu dữ liệu (metadata / 메타데이터) về hạ tầng, vì vậy cần cân nhắc quyền truy cập và việc đưa vào hệ thống quản lý mã nguồn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SSH, khóa, đường hầm và thao tác từ xa**, **Máy trung gian: jump host / bastion** tiếp nhận điểm tựa từ **/.ssh/config** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển tiếp cổng cục bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Máy trung gian: jump host / bastion

Máy chủ riêng tư thường không mở SSH trực tiếp ra Internet. Máy khách đi qua một **máy trung gian (jump host / bastion)**:

```bash
ssh -J user@bastion app@10.0.1.20
```

`ProxyJump` làm đường kết nối rõ ràng hơn việc SSH lồng thủ công. Có thể khai báo `ProxyJump` trong `~/.ssh/config`.

Lợi ích bảo mật đến từ việc giảm bề mặt tấn công của các máy riêng tư, nhưng bastion trở thành một điểm kiểm soát có giá trị cao và cần được gia cố, ghi nhật ký và kiểm tra truy cập cẩn thận.

> **Chuyển mạch:** Trong **SSH, khóa, đường hầm và thao tác từ xa**, **Chuyển tiếp cổng cục bộ** tiếp nhận điểm tựa từ **Máy trung gian: jump host / bastion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển tiếp từ xa và chuyển tiếp động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **SSH, khóa, đường hầm và thao tác từ xa**, **Chuyển tiếp từ xa và chuyển tiếp động** tiếp nhận điểm tựa từ **Chuyển tiếp cổng cục bộ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SCP, SFTP và rsync** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển tiếp từ xa và chuyển tiếp động

SSH còn hỗ trợ **chuyển tiếp cổng từ xa (remote forwarding)** bằng `-R` và **chuyển tiếp động SOCKS (dynamic forwarding)** bằng `-D`. Đây là các công cụ mạnh nhưng có ảnh hưởng bảo mật: đường hầm có thể vô tình vượt qua ranh giới mạng dự kiến nếu chính sách cho phép. Việc sử dụng trong môi trường vận hành (production / 운영 환경) phải tuân thủ chính sách truy cập của hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SSH, khóa, đường hầm và thao tác từ xa**, **SCP, SFTP và rsync** tiếp nhận điểm tựa từ **Chuyển tiếp từ xa và chuyển tiếp động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **rsync --delete và chạy thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

SFTP cung cấp giao thức truyền tệp trên SSH với các thao tác tương tác hoặc tự động hóa tùy máy khách (client / 클라이언트).

`rsync` phù hợp với đồng bộ lặp lại vì có thể chỉ truyền phần khác biệt và giữ nhiều loại siêu dữ liệu (metadata / 메타데이터):

```bash
rsync -avh --progress ./build/ app@server:/opt/app/
```

Dấu `/` ở cuối đường dẫn nguồn rất quan trọng: `src/` thường biểu thị nội dung bên trong thư mục, còn `src` có thể tạo thêm một cấp thư mục ở đích.

> **Chuyển mạch:** Trong **SSH, khóa, đường hầm và thao tác từ xa**, **rsync --delete và chạy thử** tiếp nhận điểm tựa từ **SCP, SFTP và rsync** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Keepalive** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **SSH, khóa, đường hầm và thao tác từ xa**, **Keepalive** tiếp nhận điểm tựa từ **rsync --delete và chạy thử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SSH tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Keepalive

Thiết bị mạng có thể ngắt phiên SSH nhàn rỗi. Tùy chọn phía máy khách:

```bash
ssh -o ServerAliveInterval=60 user@host
```

định kỳ gửi keepalive ở mức giao thức. Không nên đặt chu kỳ quá ngắn cho số lượng phiên rất lớn nếu chưa hiểu chi phí và chính sách mạng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SSH, khóa, đường hầm và thao tác từ xa**, **SSH tác nhân (agent / 에이전트)** tiếp nhận điểm tựa từ **Keepalive** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PuTTY nằm ở đâu trong mô hình này?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SSH tác nhân (agent / 에이전트)

`ssh-agent` giữ khả năng ký bằng khóa riêng tư trong phiên để tránh phải đọc khóa hoặc nhập lại passphrase liên tục. **Chuyển tiếp tác nhân (agent / 에이전트) (agent forwarding)** cho phép máy từ xa dùng tác nhân (agent / 에이전트) cục bộ nhưng cũng tạo rủi ro: nếu máy từ xa bị xâm nhập, kẻ tấn công có thể lợi dụng tác nhân (agent / 에이전트) đang được chuyển tiếp trong thời gian phiên còn tồn tại. Chỉ bật khi thực sự cần và hiểu ranh giới tin cậy.

> **Chuyển mạch:** Trong **SSH, khóa, đường hầm và thao tác từ xa**, **PuTTY nằm ở đâu trong mô hình này?** tiếp nhận điểm tựa từ **SSH tác nhân (agent / 에이전트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PuTTY nằm ở đâu trong mô hình này?

PuTTY là một SSH máy khách (client / 클라이언트) phổ biến trên Windows. Sau khi kết nối, các câu lệnh Linux không phải "câu lệnh của PuTTY"; chúng được chạy trong shell trên máy chủ Linux từ xa. PuTTY quản lý phía terminal/SSH máy khách (client / 클라이언트), còn `ls`, `ps`, `journalctl` và các chương trình khác chạy ở phía máy chủ.

> **Chuyển mạch:** Ở chặng này của **SSH, khóa, đường hầm và thao tác từ xa**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **PuTTY nằm ở đâu trong mô hình này?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

SSH tạo ra một **kênh truyền được xác thực và mã hóa**. Shell từ xa, SCP/SFTP và chuyển tiếp cổng chỉ là các dịch vụ sử dụng kênh đó. Khi lỗi, nên phân tách theo lớp:

```text
DNS / kết nối TCP
-> host key và mô hình tin cậy
-> xác thực người dùng
-> phân quyền / shell
-> ứng dụng chạy qua kênh
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SSH, khóa, đường hầm và thao tác từ xa**, **Những hiểu lầm phổ biến (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"SSH key là một tệp mật khẩu."** Xác thực khóa công khai dùng bằng chứng mật mã; khóa riêng tư không nên được gửi sang máy chủ.

**"Host key thay đổi thì cứ xóa `known_hosts`."** Cần xác minh thay đổi danh tính máy chủ trước.

**"SCP và rsync giống nhau."** Cả hai đều truyền tệp, nhưng `rsync` có ngữ nghĩa đồng bộ, so sánh khác biệt và giữ siêu dữ liệu (metadata / 메타데이터) mạnh hơn.

**"SSH tunnel làm dịch vụ được mở trực tiếp ra Internet."** Tunnel chỉ tạo đường chuyển tiếp qua các điểm cuối SSH; mức phơi bày thực tế còn phụ thuộc địa chỉ bind, chính sách và topology.

**"PuTTY có bộ câu lệnh Linux riêng."** Các câu lệnh chạy trên hệ điều hành và shell từ xa.

> **Chuyển mạch:** Trong **SSH, khóa, đường hầm và thao tác từ xa**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến (Common Misconceptions)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

SSH phụ thuộc trực tiếp vào [mạng](./networking_dns_sockets_ports.md), [người dùng và quyền truy cập](../03_identity/users_groups_permissions.md) cùng mô hình danh tính mật mã. Bảng câu lệnh thực hành nằm tại [Tham chiếu câu lệnh PuTTY/SSH Linux](../reference/putty_ssh_linux_server_commands.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
