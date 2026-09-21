# Journald, rsyslog và đường đi của nhật ký trong Linux

Chương [Nhật ký, journal và khả năng quan sát hệ thống](./logging_journal_observability.md) giải thích vai trò của log như một nguồn bằng chứng. Chương này đi sâu vào pipeline log ở tầng Linux: stdout/stderr của service đi đâu, `systemd-journald` lưu dữ liệu thế nào, `rsyslog` hoặc syslog daemon tham gia ở đâu, vì sao log có thể bị mất, và log rotation phải phối hợp với file descriptor của process ra sao.

## Một dòng log đi đâu?

Với service systemd, application thường ghi ra stdout/stderr.

Systemd có thể nối các stream này vào journal.

Mental model đơn giản:

```text
application stdout/stderr
        ↓
systemd service plumbing
        ↓
systemd-journald
        ↓
journal storage
        ├─ journalctl
        ├─ forward to syslog/rsyslog
        └─ forward/export to centralized logging
```

Nhưng application cũng có thể tự ghi file riêng, nên production có thể tồn tại song song nhiều đường log.

## stdout và stderr không tự có file log

Nếu Java app chạy:

```bash
java -jar app.jar
```

trong terminal, stdout/stderr đi terminal.

Nếu systemd quản lý service, descriptors có thể được nối theo `StandardOutput=` và `StandardError=`.

Mặc định trên nhiều systemd systems, output đi journal.

Kiểm tra unit:

```bash
systemctl cat app.service
systemctl show app -p StandardOutput -p StandardError
```

## Journald lưu metadata, không chỉ text

Mỗi journal entry có thể kèm metadata như:

- `_PID`;
- `_UID`;
- `_GID`;
- `_SYSTEMD_UNIT`;
- `_COMM`;
- `_EXE`;
- `_BOOT_ID`;
- `_HOSTNAME`;
- `PRIORITY`.

Xem chi tiết:

```bash
journalctl -u app -o verbose -n 1
```

Điều này giải thích vì sao `journalctl -u app` mạnh hơn `grep app` trên text log: nó lọc bằng structured metadata.

## Boot ID

Mỗi lần boot có một `_BOOT_ID` khác.

Xem boots:

```bash
journalctl --list-boots
```

Log boot trước:

```bash
journalctl -b -1
```

Đây là công cụ quan trọng khi server vừa reboot sau kernel panic hoặc maintenance.

## Journal volatile và persistent

Journald có thể lưu journal dưới:

```text
/run/log/journal
```

cho volatile storage hoặc:

```text
/var/log/journal
```

cho persistent storage, tùy config/distribution.

Nếu journal chỉ volatile, reboot sẽ mất log cũ.

Kiểm tra:

```bash
journalctl --disk-usage
ls -ld /var/log/journal /run/log/journal 2>/dev/null
```

## `Storage=`

Trong `journald.conf`, `Storage=` có thể có các mode như:

```text
auto
volatile
persistent
none
```

Semantics cụ thể phụ thuộc systemd version.

Production cần quyết định retention theo operational requirement thay vì để mặc định mà không biết.

## Journal size và retention

Các cấu hình có thể gồm:

```text
SystemMaxUse=
SystemKeepFree=
SystemMaxFileSize=
MaxRetentionSec=
```

Không nên đặt retention chỉ dựa trên “30 ngày nghe hợp lý”.

Cần tính:

```text
log rate × retention window × compression/overhead
```

và chừa headroom cho incident burst.

## Log burst

Một lỗi retry có thể làm log rate tăng hàng chục lần.

Nếu retention chỉ được sizing theo average rate, disk có thể đầy trong incident.

Capacity planning log cần tính burst scenario.

## Journald rate limiting

Journald có cơ chế rate limit để tránh một service flood toàn hệ thống.

Các cấu hình liên quan có thể gồm:

```text
RateLimitIntervalSec=
RateLimitBurst=
```

Nếu vượt giới hạn, một số messages có thể bị suppressed.

Do đó “application nói đã log” không chắc mọi message đều còn trong journal.

## Rate limit là bảo vệ và cũng là loss mode

Rate limiting bảo vệ disk/CPU nhưng có thể làm mất chi tiết đúng lúc incident.

Thiết kế tốt cần:

- alert khi suppressed messages xuất hiện;
- log sampling hợp lý;
- không tạo retry log spam;
- giữ error summaries quan trọng.

## Priority

Syslog/journal dùng priority levels như:

```text
emerg
alert
crit
err
warning
notice
info
debug
```

Filter:

```bash
journalctl -p err..alert
```

Application framework level như `ERROR`, `WARN` không phải lúc nào map hoàn hảo sang syslog priority nếu chỉ ghi plain stdout.

## Structured fields

Application có thể gửi structured fields qua journald API hoặc logger integration.

Điều này cho phép query theo field thay vì parse message string.

Tuy nhiên nhiều Java apps vẫn gửi JSON/plain text qua stdout, sau đó centralized collector parse tiếp.

## Syslog là gì?

Syslog là một family protocol/convention lâu đời để chuyển log giữa applications/daemon.

Daemon như `rsyslog` có thể:

- nhận local syslog;
- đọc journal;
- ghi file;
- forward qua network;
- filter theo facility/priority;
- transform message.

Journald và rsyslog không nhất thiết loại trừ nhau.

## Journald → rsyslog

Một architecture phổ biến:

```text
service
 ↓
journald
 ↓
rsyslog
 ↓
/var/log/... hoặc remote collector
```

Tùy config, rsyslog có thể đọc journal qua module/interface thay vì journald forward raw socket.

## `/dev/log`

Các applications truyền thống có thể gửi syslog tới Unix socket như `/dev/log`.

Trên systemd systems, journald có thể nhận traffic này.

Do đó service không nhất thiết ghi stdout mới vào journal.

## File logging trực tiếp

Một Java app có thể dùng Logback/Log4j để ghi:

```text
/var/log/app/app.log
```

Khi đó pipeline có thể bỏ qua journald cho business log.

Trade-off:

- file format/rotation do application kiểm soát;
- dễ tail;
- nhưng metadata systemd ít hơn;
- phải quản lý rotation và disk riêng.

## Ai nên chịu trách nhiệm rotation?

Có ba lựa chọn thường gặp:

```text
application rotates
logrotate rotates
journal handles retention
```

Không nên để application và logrotate cùng rotate cùng một file mà không hiểu interaction.

## Rename rotation

Một pattern:

```text
app.log → app.log.1
new app.log được tạo
```

Process phải đóng/reopen file để ghi vào file mới.

Nếu process vẫn giữ FD tới inode cũ, nó tiếp tục ghi vào `app.log.1` hoặc inode đã unlink.

## `copytruncate`

`logrotate` có option `copytruncate`:

```text
copy current file → rotated copy
truncate original file in place
```

Ưu điểm: application không cần reopen FD.

Nhược điểm: có race window giữa copy và truncate; một số log lines có thể mất hoặc duplicate.

Do đó reopen-by-signal thường tốt hơn nếu application hỗ trợ.

## Signal để reopen log

Một số daemons nhận `SIGHUP` để reopen log files.

`logrotate` có thể có `postrotate`:

```bash
systemctl kill -s HUP service
```

Nhưng behavior là application-specific; không gửi HUP nếu chưa biết daemon xử lý thế nào.

## Deleted-open log

Case kinh điển:

```text
admin rm app.log
process vẫn giữ FD
→ path biến mất
→ process vẫn ghi inode cũ
→ disk vẫn đầy
```

Tìm:

```bash
sudo lsof +L1
```

Fix phải làm process close/reopen FD hoặc restart an toàn.

## Journal vacuum

Có thể giảm journal bằng:

```bash
sudo journalctl --vacuum-time=7d
sudo journalctl --vacuum-size=1G
```

Nhưng vacuum trong incident chỉ là recovery action. Cần tìm tại sao log tăng và chỉnh retention/capacity.

## Kernel logs

Kernel messages có thể vào journal:

```bash
journalctl -k
```

`dmesg` đọc kernel ring buffer.

Hai nguồn liên quan nhưng không hoàn toàn giống về persistence và metadata.

Sau reboot, `dmesg` chỉ phản ánh boot hiện tại, còn persistent journal có thể giữ boot trước.

## Audit log

Linux Audit subsystem có thể ghi security-relevant events qua `auditd`.

Ví dụ SELinux AVC denials thường nằm trong audit trail.

Audit log có semantics khác application log; retention và tamper resistance có thể cần nghiêm ngặt hơn.

## Centralized logging

Một host đơn lẻ có thể mất disk hoặc bị compromise. Production thường forward log tới hệ thống tập trung.

Mental model:

```text
application
→ local collector
→ network buffer/queue
→ centralized backend
→ index/storage
→ query/alert
```

Mỗi mũi tên là một failure point.

## At-most-once và at-least-once trong log shipping

Log forwarder có thể ưu tiên:

- low latency nhưng chấp nhận loss;
- durable queue và retry;
- at-least-once dẫn tới duplicate.

Vì vậy centralized logs có thể thiếu hoặc duplicate entries.

Không nên giả định log pipeline có exactly-once semantics.

## Buffer trên disk

Collector như Fluent Bit, Vector, Filebeat hoặc rsyslog có thể buffer trên memory/disk.

Disk buffer giúp chịu network outage nhưng cũng chiếm disk và cần capacity planning.

## Backpressure trong logging

Nếu log sink chậm, producer/collector phải quyết định:

```text
block application?
drop logs?
buffer memory?
buffer disk?
```

Nếu synchronous logging block request thread, outage của logging backend có thể làm business API chậm.

Đây là coupling nguy hiểm.

## Async logging

Java logger có thể dùng async appender để tách request thread khỏi I/O log.

Nhưng queue hữu hạn.

Khi queue đầy, policy có thể block hoặc drop.

Async không xóa bottleneck; nó chỉ thêm buffer và thay failure behavior.

## Log và dữ liệu nhạy cảm

Không log:

- password;
- access token;
- full private key;
- card data;
- unnecessary personal data.

Masking phải xảy ra trước khi message đi vào pipeline.

Xóa khỏi dashboard sau khi đã ingest không có nghĩa dữ liệu đã biến mất khỏi storage/backup.

## Retention khác backup

Giữ log 30 ngày trong Elasticsearch không phải backup.

Retention chỉ nói dữ liệu còn query được bao lâu.

Backup/archival cần policy riêng về restore và integrity.

## Time ordering

Distributed logs không có một global clock tuyệt đối hoàn hảo.

Ngay cả khi NTP đồng bộ, network delay và buffering có thể làm ingestion order khác event order.

Nên giữ event timestamp tại source và trace/request ID.

## Multiline stack trace

Java exception có nhiều dòng.

Collector phải biết multiline rules, nếu không mỗi stack frame có thể thành một log event riêng.

Structured JSON với exception field có thể giúp nhưng vẫn cần strategy cho stack trace.

## Log schema

Một schema tốt thường có:

```text
timestamp
level
service
host / instance
request_id / trace_id
logger
message
error_type
stack_trace
```

Không phải mọi event cần mọi field, nhưng consistency giúp query.

## Cardinality

Field như `user_id`, `request_id` có cardinality rất cao.

Index mọi field cardinality cao có thể làm logging backend tốn memory/storage.

Observability schema cần cân bằng query usefulness với cost.

## Một case: API latency tăng cùng log volume

Chuỗi có thể là:

```text
upstream timeout
→ retry
→ mỗi retry ghi stack trace
→ log volume tăng 100×
→ async queue đầy
→ logging chuyển sang block
→ request threads chờ logger
→ API latency tăng
```

Log lúc này không chỉ là bằng chứng; nó trở thành một phần nguyên nhân.

## Case: disk đầy nhưng `du` không thấy file lớn

Khả năng:

```text
logrotate/unlink
→ process giữ old FD
→ `ls` không thấy
→ `df` vẫn đầy
```

Kiểm tra:

```bash
sudo lsof +L1
```

## Case: journal không có log boot trước

Kiểm tra:

```bash
journalctl --list-boots
ls -ld /var/log/journal
```

Nếu storage volatile, log boot cũ có thể đã mất.

Đây là design decision cần sửa trước incident tiếp theo.

## Case: centralized logging mất vài phút dữ liệu

Cần kiểm tra từng đoạn:

```text
application emitted?
local journal/file có entry?
collector đọc được?
collector queue/backpressure?
network tới backend?
backend ingest/index?
query filter/timezone đúng?
```

Không nên kết luận “application không log” chỉ vì dashboard không thấy.

## Mô hình tư duy

Log là một pipeline dữ liệu:

```text
producer
→ local transport
→ local storage/buffer
→ shipper
→ network
→ central backend
→ index/query
```

Mỗi layer có buffering, retention, rate limit và failure mode riêng.

## Những hiểu lầm phổ biến

**“Journal có log nghĩa centralized backend chắc chắn có.”** Forwarder/network/backend có thể lỗi.

**“Logrotate xóa file là giải phóng disk.”** Không nếu process còn giữ FD.

**“Async logging không ảnh hưởng application.”** Queue đầy vẫn có thể block hoặc drop.

**“Càng nhiều DEBUG càng dễ điều tra.”** Có thể tạo noise, cost và thậm chí I/O bottleneck.

**“Centralized log là source of truth tuyệt đối.”** Pipeline có thể drop, duplicate hoặc reorder events.

## Kết nối kiến thức

Đọc [VFS/page cache/writeback](../01_filesystem/vfs_page_cache_writeback.md) để hiểu log I/O, [Time/clock/NTP](./time_clock_ntp.md) để hiểu timestamp correlation, và [Observability/tracing](../09_production/observability_tracing_strace_perf.md) để kết hợp log với metrics và tracing.