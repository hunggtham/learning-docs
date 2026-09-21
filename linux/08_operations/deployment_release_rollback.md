# Deployment, Release và Rollback trên Linux

Deployment không chỉ là copy file mới rồi restart application. Trong production, một deployment tốt phải kiểm soát **phiên bản nào đang chạy, thay đổi state theo thứ tự nào, cách xác minh sau thay đổi, và cách quay lại trạng thái an toàn nếu lỗi**.

Nếu không có mô hình này, server dễ rơi vào trạng thái “config mới nhưng binary cũ”, “binary mới nhưng service chưa restart”, hoặc rollback chỉ quay artifact nhưng không quay database/config tương ứng.

## Desired state và runtime state

Một artifact mới tồn tại trên disk không có nghĩa process đang dùng artifact đó.

```bash
ls -l /opt/app/app.jar
pgrep -af 'java.*app.jar'
systemctl show app -p MainPID -p ExecStart
```

Ba quan sát này trả lời ba câu khác nhau: file nào tồn tại, process nào đang chạy, và systemd được cấu hình chạy command nào.

Deployment phải xác minh **runtime state**, không chỉ file state.

## Release directory thay vì ghi đè trực tiếp

Một pattern an toàn hơn:

```text
/opt/app/releases/2026-09-20_203000/
/opt/app/releases/2026-09-20_213000/
/opt/app/current -> /opt/app/releases/2026-09-20_213000/
```

Mỗi release là immutable sau khi tạo. `current` là symlink trỏ tới release đang active.

Ưu điểm là rollback artifact có thể chỉ cần chuyển symlink về release trước, thay vì cố tái tạo file cũ từ trí nhớ.

## Chuẩn bị release trước khi switch

Không nên copy artifact trực tiếp lên path mà process đang sử dụng nếu có thể tránh.

Flow tốt hơn:

```text
upload artifact
→ verify checksum
→ extract/copy vào release directory mới
→ validate config
→ kiểm tra permission/owner
→ switch current
→ restart/reload
→ health check
```

Ví dụ checksum:

```bash
sha256sum app.jar
```

Nếu CI/CD cung cấp checksum mong đợi, so sánh giúp phát hiện artifact hỏng hoặc nhầm version.

## Atomic switch bằng symlink

Có thể tạo symlink mới rồi rename:

```bash
ln -s /opt/app/releases/2026-09-20_213000 /opt/app/current.new
mv -T /opt/app/current.new /opt/app/current
```

Rename trong cùng filesystem thường atomic ở namespace level. Điều này giảm khoảng thời gian `current` ở trạng thái nửa vời.

Cần kiểm tra option `mv -T` có trên hệ thống tương ứng; GNU coreutils hỗ trợ nhưng portability khác nhau.

## Config có lifecycle riêng

Artifact và config không nhất thiết nên version cùng cách.

Nếu config chứa secret hoặc environment-specific values, có thể đặt ngoài release directory:

```text
/etc/myapp/application-prod.yml
/opt/app/releases/<version>/app.jar
```

Service trỏ rõ:

```ini
ExecStart=/usr/bin/java -jar /opt/app/current/app.jar --spring.config.location=/etc/myapp/application-prod.yml
```

Như vậy rollback binary không vô tình rollback secret hoặc environment setting.

Ngược lại, config schema thay đổi cùng code phải có compatibility strategy rõ.

## Database migration là phần khó nhất của rollback

Binary thường rollback được tương đối dễ; database migration có thể không.

Nếu version mới xóa column hoặc đổi dữ liệu không tương thích, quay binary cũ có thể không chạy nữa.

Một chiến lược an toàn là **expand–migrate–contract**:

```text
1. Add schema mới nhưng giữ schema cũ
2. Deploy code tương thích cả hai
3. Migrate/backfill dữ liệu
4. Chuyển traffic sang behavior mới
5. Sau khi ổn định mới xóa schema cũ
```

Cách này làm rollback trong giai đoạn đầu dễ hơn.

## Restart, reload và zero-downtime

Một single-instance service restart thường tạo downtime ngắn. Với nhiều instances sau load balancer, có thể rolling deployment:

```text
remove instance A khỏi traffic
→ deploy A
→ health check A
→ đưa A lại traffic
→ lặp với B
```

Đây là orchestration ở tầng cao hơn systemd. Systemd quản lý process lifecycle của từng host, còn load balancer/orchestrator quản lý traffic giữa nhiều instances.

## Health check phải phản ánh readiness

Một process vừa tồn tại chưa chắc sẵn sàng nhận traffic.

```bash
curl -fsS http://127.0.0.1:8080/health
```

Health endpoint nên phân biệt khi cần:

- liveness: process/app còn sống;
- readiness: app đã sẵn sàng phục vụ;
- dependency health: DB/cache/downstream có cần healthy không.

Không nên làm health check quá sâu đến mức một dependency chập chờn làm toàn fleet bị restart liên tục.

## Smoke test sau deployment

Health 200 chưa đủ chứng minh business path chính hoạt động. Một smoke test nhỏ có thể kiểm tra endpoint quan trọng với read-only hoặc synthetic request.

Ví dụ:

```bash
curl -fsS https://api.example.com/version
curl -fsS https://api.example.com/health
```

Nếu có `/version`, response nên cho biết build/version để xác minh đúng release đang phục vụ.

## Version evidence

Một deployment đáng tin nên có cách trả lời:

```text
commit nào?
build nào?
artifact checksum nào?
config version nào?
deploy lúc nào?
ai/automation nào deploy?
```

Có thể lưu metadata cạnh release:

```text
VERSION
COMMIT_SHA
BUILD_TIME
CHECKSUMS
```

Điều này giúp incident timeline chính xác hơn.

## Rollback trigger

Rollback không nên dựa chỉ vào cảm giác “có vẻ lỗi”. Nên có signals rõ như:

```text
health check fail liên tục
error rate tăng vượt baseline
latency tăng mạnh
critical business test fail
startup fail
```

Với thay đổi risky, cần định nghĩa rollback criteria trước deployment.

## Rollback artifact

Nếu release cũ vẫn còn:

```bash
ln -s /opt/app/releases/2026-09-20_203000 /opt/app/current.new
mv -T /opt/app/current.new /opt/app/current
sudo systemctl restart app
```

Sau đó **vẫn phải verify**:

```bash
systemctl status app --no-pager
curl -fsS http://127.0.0.1:8080/health
```

Rollback là một deployment khác, không phải nút “undo” thần kỳ.

## Backup trước edit thủ công

Nếu buộc phải sửa config trực tiếp:

```bash
cp -a /etc/myapp/app.conf /etc/myapp/app.conf.$(date +%F_%H%M%S).bak
```

Sau edit, validate bằng tool của ứng dụng nếu có trước reload.

Với Nginx:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Pattern **validate → apply** nên được ưu tiên.

## Permission và owner của release

Artifact đúng nhưng owner sai vẫn làm service fail.

```bash
namei -l /opt/app/current/app.jar
ls -l /opt/app/current/app.jar
systemctl show app -p User -p Group
```

Deployment automation nên set ownership/mode theo desired state, không phụ thuộc file upload tạo ra permission ngẫu nhiên.

## Disk space và retention

Giữ nhiều releases hỗ trợ rollback nhưng cũng dùng disk.

Không nên `rm -rf releases/*` rồi giữ mỗi current. Thay vào đó giữ N release gần nhất và chỉ cleanup sau khi xác định current/previous.

Trước cleanup:

```bash
df -h /opt/app
ls -ltr /opt/app/releases
readlink -f /opt/app/current
```

## Logging deployment event

Incident analysis rất cần biết deployment xảy ra lúc nào.

Có thể ghi event vào log/journal hoặc hệ thống deployment:

```bash
logger -t deploy "myapp version=2026.09.20.2 deployed"
```

Sau đó:

```bash
journalctl -t deploy
```

Timeline “error bắt đầu 30 giây sau deploy” là evidence mạnh dù chưa phải proof nguyên nhân.

## Canary deployment

Thay vì đưa version mới cho 100% traffic, canary chỉ nhận một phần nhỏ. Nếu metrics tốt mới mở rộng.

Canary giảm blast radius nhưng yêu cầu infrastructure routing/observability đủ tốt. Nó không phải chỉ là chạy một process test trên server nếu process đó không nhận traffic thực tế tương tự production.

## Blue–green deployment

Hai environments `blue` và `green` tồn tại song song. Một phía đang active, phía kia nhận release mới. Sau validation, traffic switch sang environment mới.

Rollback có thể nhanh bằng switch ngược, nhưng database/shared state vẫn là phần cần compatibility.

## Mô hình tư duy (Mental Model)

Deployment là một **controlled state transition**:

```text
known old state
→ prepare new state
→ validate before activation
→ activate
→ verify externally observable behavior
→ keep rollback path
```

Mọi bước nên để lại evidence và có failure handling rõ.

## Những hiểu lầm phổ biến

**“Copy jar thành công nghĩa deploy thành công.”** Process có thể vẫn chạy jar cũ.

**“Rollback binary là rollback toàn hệ thống.”** Database/config/external side effects có thể không rollback được.

**“Restart service là health check.”** Restart thành công chỉ nói process lifecycle không báo lỗi ngay.

**“Giữ release cũ là đủ rollback.”** Cần artifact, config compatibility, database strategy và procedure đã thử.

## Kết nối kiến thức

Chương này liên kết [Filesystem và Symlink](../01_filesystem/filesystem_paths_inodes_links.md), [systemd và Services](../05_system/systemd_boot_services.md), [Bash Scripting đáng tin cậy](../02_shell/bash_scripting_reliability.md), [Backup và Restore](./backup_restore_disaster_recovery.md) và [Production Troubleshooting](../09_production/production_troubleshooting.md).