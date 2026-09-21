# Bảo mật Linux và gia cố máy chủ

**Gia cố bảo mật (security hardening)** không phải một checklist kiểu "tắt càng nhiều càng tốt". Mục tiêu là giảm xác suất và mức ảnh hưởng khi hệ thống bị xâm nhập, đồng thời vẫn giữ hệ thống vận hành đúng chức năng. Muốn làm đúng cần hiểu **tài sản cần bảo vệ, danh tính, ranh giới tin cậy (trust boundary), bề mặt tấn công (attack surface) và khả năng phục hồi**.

## Mô hình đe dọa phải có trước cấu hình

Một máy chủ build nội bộ và một API công khai trên Internet có **mô hình đe dọa (threat model)** khác nhau. Trước khi gia cố, cần biết dữ liệu nào quan trọng, ai cần truy cập, mạng nào được tin cậy, dịch vụ nào phải công khai và loại thất bại nào có thể chấp nhận.

Không tồn tại một tệp `sysctl.conf` thần kỳ phù hợp cho mọi máy chủ.

## Đặc quyền tối thiểu

Tiến trình chỉ nên có những quyền nó thật sự cần. Thay vì chạy ứng dụng Java bằng `root`, nên tạo người dùng dịch vụ riêng và chỉ cấp quyền đọc/ghi trên những đường dẫn cần thiết.

```ini
[Service]
User=app
Group=app
```

Nếu ứng dụng chỉ cần một đặc quyền cụ thể, Linux capabilities hoặc cơ chế cô lập của systemd có thể giảm quyền so với việc cấp toàn bộ quyền root.

Nguyên tắc **đặc quyền tối thiểu (least privilege / 최소 권한)** làm giảm phạm vi ảnh hưởng khi ứng dụng bị khai thác.

## Giảm bề mặt tấn công

Mỗi dịch vụ đang lắng nghe trên mạng là một điểm vào tiềm năng. Có thể kiểm tra bằng:

```bash
sudo ss -lntup
```

Với từng listener, hãy hỏi: dịch vụ này có thật sự cần thiết không? có cần bind trên mọi giao diện hay chỉ loopback/IP nội bộ? firewall hoặc chính sách mạng có giới hạn nguồn truy cập không?

Gia cố tốt thường bắt đầu bằng nguyên tắc đơn giản: **không phơi bày những gì không cần phơi bày**.

## Gia cố SSH

Xác thực bằng khóa công khai, vô hiệu hóa tài khoản không dùng, giới hạn mạng nguồn và kiểm tra lịch sử truy cập thường quan trọng hơn việc chỉ đổi cổng SSH để giảm nhiễu quét tự động.

Việc xác minh host key phải được tôn trọng. Khóa riêng tư cần được bảo vệ bằng quyền hệ thống tệp, passphrase và chính sách `ssh-agent` phù hợp.

Không nên sửa `sshd_config` theo một checklist ngẫu nhiên rồi khởi động lại ngay. Trước hết hãy kiểm tra cấu hình:

```bash
sudo sshd -t
```

Khi thay đổi SSH từ xa, nên giữ một phiên phục hồi đang mở cho tới khi xác nhận cấu hình mới hoạt động, tránh tự khóa mình khỏi máy chủ.

## Quản lý bản vá

Lỗ hổng đã biết trong gói phần mềm cũ là một đường tấn công phổ biến. Việc cập nhật gói cần có kiểm kê phiên bản, kiểm thử, kế hoạch triển khai và khả năng quay lui.

Vá bảo mật là một **vòng đời**, không phải sự kiện một lần. Cập nhật kernel đôi khi cần khởi động lại để mã mới thật sự được sử dụng.

```bash
uname -r
cat /etc/os-release
```

Kiểm kê phiên bản giúp biết trạng thái thực tế của máy thay vì chỉ biết "đã chạy update".

## Quyền tệp và bí mật

Bí mật không nên để người dùng khác đọc được:

```bash
chmod 600 secret.env
chown app:app secret.env
```

Nhưng quyền của hệ thống tệp chỉ là một lớp. Bí mật có thể rò rỉ qua bản dump biến môi trường, lịch sử câu lệnh, đối số tiến trình, nhật ký, bản sao lưu hoặc artifact của CI.

Vì vậy `chmod 600` chưa phải toàn bộ quá trình **quản lý bí mật (secret management)**.

## Firewall

Firewall trên host giới hạn đường truyền mạng theo chính sách. Linux hiện đại có nftables; các bản phân phối có thể cung cấp lớp quản lý như firewalld hoặc UFW.

```bash
sudo nft list ruleset
```

Luật firewall phải phù hợp với security group trên cloud, load balancer và địa chỉ bind của ứng dụng. Nhiều lớp chính sách có thể cùng tác động lên một kết nối.

## SELinux và AppArmor

**Kiểm soát truy cập bắt buộc (Mandatory Access Control / MAC)** giới hạn tiến trình bằng chính sách bổ sung ngoài mô hình UID/mode truyền thống. SELinux thường xuất hiện trên họ RHEL, còn AppArmor phổ biến trên Ubuntu.

Tắt SELinux hoặc AppArmor để "sửa permission" có thể làm triệu chứng biến mất nhưng đồng thời loại bỏ một ranh giới bảo mật. Cách đúng là đọc bằng chứng bị từ chối rồi sửa policy hoặc context nếu ứng dụng thật sự cần quyền đó.

## Cô lập dịch vụ bằng systemd

Systemd có nhiều chỉ thị giúp giới hạn capabilities, quyền truy cập hệ thống tệp, nâng đặc quyền và namespace tùy khả năng tương thích của dịch vụ. Ví dụ `NoNewPrivileges=`, `ProtectSystem=` hoặc `PrivateTmp=` có thể giảm bề mặt tấn công.

Không nên bật hàng loạt chỉ thị mà không kiểm thử; ứng dụng có thể cần đường dẫn hoặc system call đang bị giới hạn.

## Kiểm toán và nhật ký

Thất bại xác thực, thay đổi đặc quyền và sự kiện dịch vụ cần có chính sách lưu giữ và giám sát phù hợp. Tuy nhiên nhật ký bảo mật cũng không nên chứa bí mật hoặc dữ liệu cá nhân không cần thiết.

Điều tra sự cố bảo mật cần đồng bộ thời gian và thường cần nhật ký tập trung, vì kẻ tấn công có thể tác động lên trạng thái hoặc nhật ký cục bộ của host đã bị xâm nhập.

## Sao lưu và phục hồi cũng là bảo mật

Ransomware, câu lệnh phá hủy hoặc xâm nhập hệ thống không chỉ cần phòng ngừa. Bản sao lưu ngoại tuyến hoặc bất biến và việc kiểm thử khôi phục là những kiểm soát bảo mật quan trọng. Một bản sao lưu chưa từng được thử phục hồi mới chỉ là một giả thuyết rằng dữ liệu có thể lấy lại.

Nguyên tắc này nối bảo mật với độ tin cậy: tính sẵn sàng và khả năng phục hồi là một phần của bảo vệ hệ thống.

## Chuỗi cung ứng phần mềm

Gói phần mềm, ảnh container, dependency và artifact triển khai đều là đầu vào cần được tin cậy. Khi hệ sinh thái hỗ trợ, nên xác minh nguồn, checksum hoặc chữ ký; có chính sách phiên bản rõ; và tránh tải một script không rõ rồi pipe thẳng vào shell có đặc quyền.

Ví dụ:

```bash
curl https://example/install.sh | sudo bash
```

trao nội dung từ xa quyền thực thi ngay lập tức. An toàn hơn là tải xuống, kiểm tra nguồn/nội dung và xác minh trước khi chạy, đặc biệt trong ngữ cảnh có đặc quyền cao.

## Mô hình tư duy (Mental Model)

Bảo mật có thể được nhìn như bài toán quản lý **ai có thể gây ra thay đổi trạng thái nào, thông qua giao diện nào**. Danh tính, quyền, mức phơi bày mạng, nguồn gốc phần mềm và khả năng phục hồi đều là các phần của cùng câu hỏi.

**Phòng thủ nhiều lớp (defense in depth)** có nghĩa khi một kiểm soát thất bại, kiểm soát khác vẫn giảm mức ảnh hưởng; nó không có nghĩa chất chồng cấu hình ngẫu nhiên.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Đổi cổng SSH là biện pháp gia cố chính."** Nó giảm nhiễu quét tự động nhưng không thay thế xác thực, chính sách mạng và vá lỗi.

**"Mật khẩu root mạnh là đủ."** Bề mặt tấn công còn gồm dịch vụ, lỗ hổng, khóa, sudo, chuỗi cung ứng và lỗi ứng dụng.

**"`chmod 777` sửa được permission."** Nó phá nguyên tắc đặc quyền tối thiểu và có thể không tác động tới chính sách MAC.

**"Firewall đóng cổng nghĩa là dịch vụ an toàn."** Lỗ hổng vẫn có thể bị khai thác từ mạng hoặc máy khách đang được cho phép.

**"Có backup nghĩa là phục hồi được."** Khả năng restore phải được kiểm thử thực tế.

## Kết nối kiến thức

Bảo mật sử dụng mô hình danh tính từ [Người dùng và quyền truy cập](../03_identity/users_groups_permissions.md), mô hình mạng từ [Mạng, DNS, socket và cổng](../07_networking/networking_dns_sockets_ports.md), vòng đời gói phần mềm và khả năng quan sát hệ thống. Container không loại bỏ bảo mật của host; chúng chỉ bổ sung thêm các cơ chế cô lập và bề mặt cấu hình.