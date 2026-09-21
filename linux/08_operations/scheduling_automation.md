# Lập lịch, Cron và độ tin cậy của tự động hóa

Tự động hóa (automation) không chỉ là "cho câu lệnh chạy tự động". Khi không còn người ngồi trước terminal, những giả định vốn được shell tương tác che giấu — `PATH`, thư mục làm việc, biến môi trường, nhiều lần chạy chồng lên nhau và cách báo lỗi — trở thành nguồn gây thất bại. Vì vậy một tác vụ được lập lịch cần được thiết kế như một hệ thống production nhỏ.

## Mô hình của Cron

Xem hoặc sửa `crontab` của người dùng hiện tại:

```bash
crontab -l
crontab -e
```

Một mục như:

```cron
0 2 * * * /opt/scripts/backup.sh
```

nghĩa là chạy lúc 02:00 mỗi ngày theo ngữ cảnh múi giờ và tiến trình cron đang sử dụng.

Năm trường truyền thống:

```text
phút giờ ngày-trong-tháng tháng ngày-trong-tuần
```

`*/5 * * * *` thường có nghĩa chạy mỗi 5 phút.

## Môi trường của Cron khác shell tương tác

Cron thường chạy với môi trường tối giản. Một script có thể chạy tay thành công:

```bash
./backup.sh
```

nhưng thất bại trong cron vì `java`, `python` hoặc `mysqldump` không nằm trong `PATH` của cron.

Script production nên dùng đường dẫn tuyệt đối khi phù hợp hoặc tự khai báo môi trường rõ ràng:

```bash
#!/usr/bin/env bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

Thư mục làm việc cũng không nên được giả định:

```bash
cd /opt/app || exit 1
```

## Đầu ra và lỗi

Nếu tác vụ được lập lịch thất bại nhưng không ai nhìn thấy, tự động hóa trở thành một **lỗi âm thầm (silent failure)**.

```cron
0 2 * * * /opt/scripts/backup.sh >> /var/log/app-backup.log 2>&1
```

Tốt hơn nữa là giám sát mã thoát và độ mới của bản sao lưu thay vì chỉ lưu một tệp log rồi hy vọng có người đọc.

## Nhiều lần chạy chồng lên nhau

Một tác vụ chạy mỗi 5 phút nhưng đôi lúc cần 8 phút sẽ bị chồng phiên. Hai bản chạy đồng thời có thể ghi cùng một tệp hoặc tạo tác động nghiệp vụ trùng lặp.

`flock` cung cấp khóa tệp đơn giản:

```cron
*/5 * * * * flock -n /run/myjob.lock /opt/scripts/job.sh
```

`-n` làm câu lệnh thất bại ngay nếu khóa đang được giữ. Tuy nhiên ý nghĩa của khóa phải phù hợp yêu cầu nghiệp vụ; nếu cùng tác vụ chạy trên nhiều máy, có thể cần hàng đợi hoặc khóa phân tán thay vì file lock cục bộ.

## Tính lặp an toàn (idempotency)

Tự động hóa đáng tin cậy nên cố gắng có **tính lặp an toàn (idempotency)**: chạy lại cùng thao tác không tạo trạng thái sai hoặc tác dụng phụ trùng lặp ngoài ý muốn.

`mkdir -p` là một ví dụ nhỏ: chạy nhiều lần vẫn đưa hệ thống tới cùng trạng thái mong muốn. Script triển khai có thể kiểm tra artifact hoặc phiên bản trước khi đổi symlink. Migration cơ sở dữ liệu cần cơ chế riêng để không áp dụng cùng thay đổi nhiều lần.

Idempotency liên hệ trực tiếp với hệ thống phân tán và hạ tầng dưới dạng mã (Infrastructure as Code).

## Mã thoát

Script phải trả mã khác 0 khi có thất bại thật sự mà trình lập lịch hoặc hệ thống giám sát cần phát hiện.

```bash
set -o pipefail
```

có thể giúp pipeline phản ánh lỗi ở các bước trước, nhưng cần hiểu ngữ nghĩa lỗi của Bash. Không nên thêm `|| true` chỉ để "cron không báo lỗi" nếu nó che giấu một thất bại nghiệp vụ thật.

## Bộ hẹn giờ của systemd

**Systemd timer** là một lựa chọn mạnh cho nhiều tác vụ mà trước đây thường dùng cron. Timer unit kích hoạt service unit, nhờ đó có thể tận dụng cơ chế nhật ký, danh tính, phụ thuộc và kiểm soát tài nguyên của systemd.

```bash
systemctl list-timers
```

Một lợi ích là lần chạy được lập lịch trở thành unit có journal:

```bash
journalctl -u myjob.service
```

Cron vẫn đơn giản và phù hợp với nhiều tác vụ; systemd timer hữu ích hơn khi cần tích hợp sâu với trình quản lý dịch vụ.

## Những lần chạy bị bỏ lỡ

Cron truyền thống thường không tự chạy bù một tác vụ đã bỏ lỡ trong thời gian máy tắt. Systemd timer có `Persistent=` để có thể kích hoạt một sự kiện lịch đã bỏ lỡ sau khi hệ thống khởi động lại, tùy cấu hình.

Đây là câu hỏi nghiệp vụ: nếu bản sao lưu lúc 02:00 bị bỏ lỡ vì máy chủ tắt, nên bỏ qua hay chạy ngay khi máy lên? Cấu hình bộ lập lịch phải phản ánh yêu cầu đó.

## Múi giờ và DST

Lập lịch theo thời gian lịch chịu ảnh hưởng của múi giờ và giờ mùa hè (DST). Hàn Quốc hiện không dùng DST, nhưng máy chủ hoặc ứng dụng có thể chạy UTC hoặc phục vụ vùng khác. "Mỗi ngày lúc 02:00" cần nói rõ 02:00 theo múi giờ nào nếu tính đúng nghiệp vụ phụ thuộc thời gian.

```bash
timedatectl
```

## Tự động hóa và bí mật

Không nên ghi cứng mật khẩu hoặc token trực tiếp trong dòng lệnh `crontab` nếu có thể tránh. Dòng lệnh có thể xuất hiện trong danh sách tiến trình hoặc lịch sử; tệp `crontab` và cấu hình cũng cần quyền thích hợp. Nên dùng cơ chế quản lý bí mật phù hợp với môi trường.

## Mô hình tư duy (Mental Model)

Tác vụ được lập lịch là một **tiến trình chạy không có người giám sát trực tiếp**. Vì thiếu ngữ cảnh của con người, các phụ thuộc phải được khai báo rõ: đường dẫn chương trình, danh tính, biến môi trường, thư mục làm việc, khóa, nhật ký, timeout, retry và tiêu chí thành công.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Chạy tay được thì Cron chắc chắn chạy được."** Môi trường và ngữ cảnh thực thi có thể khác.

**"Chạy mỗi 5 phút nghĩa là lúc nào cũng chỉ có một phiên."** Không đúng nếu thời gian chạy dài hơn chu kỳ.

**"Có log là đủ giám sát."** Một tác vụ đã ngừng chạy từ lâu vẫn có thể không bị phát hiện nếu không ai kiểm tra log hoặc độ mới của kết quả.

**"Retry luôn an toàn."** Thao tác không có tính idempotent có thể tạo tác dụng phụ trùng lặp.

**"Cron là lựa chọn duy nhất."** Systemd timer, bộ điều phối và trình lập lịch trong ứng dụng có ngữ nghĩa khác nhau.

## Kết nối kiến thức

Tự động hóa dựa trên [Shell](../02_shell/shell_bash_pipes_redirection.md), danh tính của tiến trình và systemd. Những nguyên tắc về idempotency, phụ thuộc rõ ràng và khả năng quan sát cũng là nền tảng của DevOps và SRE.