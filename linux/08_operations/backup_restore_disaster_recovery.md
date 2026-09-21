# Backup, Restore và Disaster Recovery trên Linux

Backup không phải là việc “có một bản copy ở đâu đó”. Giá trị thực của backup chỉ xuất hiện khi dữ liệu có thể được phục hồi đúng, trong thời gian chấp nhận được và với mức mất dữ liệu nằm trong giới hạn nghiệp vụ. Vì vậy backup phải được thiết kế cùng với **restore** và **disaster recovery (DR)** ngay từ đầu.

Một file `.tar.gz` tồn tại không chứng minh hệ thống có thể phục hồi sau sự cố. Nếu không biết nó được tạo từ lúc nào, có đầy đủ dữ liệu hay không, có checksum không, có restore test không và phụ thuộc nào cần phục hồi cùng, đó chỉ là một artifact chưa được chứng minh.

## Xác định thứ cần bảo vệ

Trước khi chọn command, cần biết tài sản nào thực sự quan trọng. Một Linux application server có thể gồm:

```text
application artifact
configuration
secrets
user-uploaded files
database data
certificates/keys
systemd units
reverse proxy config
scheduled jobs
operational metadata
```

Không phải tất cả đều cần backup giống nhau. Artifact có thể rebuild từ CI, nhưng database hoặc user upload có thể không thể tái tạo.

## RPO và RTO

Hai khái niệm nền tảng:

**RPO (Recovery Point Objective)** là lượng dữ liệu tối đa có thể mất tính theo thời gian. RPO 15 phút nghĩa business chấp nhận mất tối đa khoảng 15 phút dữ liệu gần nhất trong disaster scenario được định nghĩa.

**RTO (Recovery Time Objective)** là thời gian tối đa mong muốn để dịch vụ được khôi phục sau sự cố.

Hai con số này quyết định kiến trúc backup. Backup mỗi đêm không thể đáp ứng RPO 15 phút cho database thay đổi liên tục.

## Backup file đơn giản bằng `tar`

Với static configuration hoặc directory phù hợp:

```bash
tar -czf app-config-$(date +%F).tar.gz /etc/myapp
```

Trước restore nên inspect archive:

```bash
tar -tzf app-config-2026-09-20.tar.gz | less
```

Không extract trực tiếp vào `/` nếu chưa kiểm tra path và nội dung archive. Có thể extract vào staging directory:

```bash
mkdir -p /tmp/restore-check
tar -xzf app-config-2026-09-20.tar.gz -C /tmp/restore-check
```

Sau đó compare trước khi ghi đè production.

## `rsync` không tự động là backup

`rsync` rất tốt để đồng bộ:

```bash
rsync -aH --delete /data/ backup-host:/backup/data/
```

Nhưng nếu source bị xóa hoặc ransomware mã hóa dữ liệu, mirror với `--delete` có thể đồng bộ luôn trạng thái hỏng sang destination.

Vì vậy backup cần **versioning/history/immutability** phù hợp, không chỉ mirror latest state.

`rsync --delete` luôn nên dry-run trước khi dùng thủ công:

```bash
rsync -aHn --delete /data/ backup-host:/backup/data/
```

## Snapshot

Filesystem, LVM, VM hoặc cloud volume có thể hỗ trợ snapshot. Snapshot tạo một point-in-time view nhanh, nhưng không phải lúc nào cũng là backup độc lập.

Nếu snapshot nằm cùng storage/account và storage đó hỏng hoặc bị xóa, snapshot có thể biến mất cùng. Snapshot phù hợp làm một lớp recovery nhanh, nhưng long-term backup thường cần domain failure khác.

## Crash-consistent và application-consistent

Nếu snapshot block device trong khi database đang ghi, snapshot có thể **crash-consistent**: tương tự trạng thái disk khi máy mất điện. Database engine tốt thường có recovery log để phục hồi, nhưng điều đó khác với **application-consistent backup** được tạo qua cơ chế database hỗ trợ.

Không copy trực tiếp data directory của database đang chạy rồi giả định backup hợp lệ. Hãy dùng backup mechanism của database hoặc snapshot procedure đã được chứng minh.

## Database backup

Mỗi database có chiến lược riêng. Có thể có logical backup, physical backup, WAL/binlog/archive log và point-in-time recovery.

Điểm quan trọng ở Linux level là hiểu backup command chỉ là một phần của data-consistency protocol.

Ví dụ logical dump thường tạo dữ liệu portable hơn nhưng restore có thể chậm với database lớn. Physical backup nhanh hơn nhưng phụ thuộc version/storage layout nhiều hơn.

## Point-in-Time Recovery

PITR cho phép restore base backup rồi replay transaction logs tới một thời điểm trước sự cố.

Mental model:

```text
base backup
+ continuous transaction log archive
→ restore tới time T
```

Điều này rất hữu ích khi lỗi logic xảy ra, ví dụ accidental delete lúc 15:37. Backup nightly chỉ cho trạng thái đêm trước, còn PITR có thể tiến sát thời điểm trước lỗi.

## Backup configuration và secrets

Config có thể nằm trong Git, nhưng production secrets không nên commit vào repo.

Nếu secret store hoặc certificate là dependency quan trọng, DR plan phải nói rõ cách khôi phục chúng. Restore app binary mà thiếu TLS private key, DB credential hoặc encryption key có thể làm dữ liệu không dùng được.

Encryption key mất có thể đồng nghĩa backup encrypted vĩnh viễn không thể giải mã.

## Encryption at rest

Backup chứa production data phải được bảo vệ. Có thể cần encryption ở backup tool, storage provider hoặc filesystem layer.

Nhưng encryption tạo thêm key-management dependency. Không lưu encryption key duy nhất cùng nơi với backup duy nhất rồi gọi đó là disaster recovery.

## Backup offsite và failure domain

Nếu production disk và backup disk cùng máy, cháy disk/controller hoặc operator `rm` có thể phá cả hai.

Một chiến lược thường có nhiều failure domains:

```text
local fast recovery copy
+ remote/offsite backup
+ immutable/versioned copy
```

Tùy độ quan trọng dữ liệu, có thể tham khảo nguyên tắc 3-2-1: nhiều bản copy, nhiều loại media/storage và ít nhất một bản ở failure domain khác. Đây là heuristic, không phải luật tuyệt đối.

## Immutability

Immutable hoặc object-lock backup giúp chống accidental deletion/ransomware trong retention period.

Tuy nhiên nếu credential có quyền phá retention hoặc account root bị compromise, “immutable” có thể không còn ý nghĩa. Security design phải xem cả identity và policy boundary.

## Checksum và integrity

Sau khi tạo backup, có thể lưu checksum:

```bash
sha256sum backup.tar.gz > backup.tar.gz.sha256
```

Verify:

```bash
sha256sum -c backup.tar.gz.sha256
```

Checksum phát hiện corruption/change nhưng không chứng minh dữ liệu bên trong đúng về mặt ứng dụng. Cần restore test để chứng minh tầng cao hơn.

## Retention

Giữ backup mãi mãi thường không thực tế. Có thể có policy:

```text
hourly: 48 giờ
daily: 30 ngày
weekly: 12 tuần
monthly: 12 tháng
```

Retention phải dựa business/legal/storage constraints. Cleanup cũng là destructive automation nên cần kiểm tra, log và tránh pattern wildcard nguy hiểm.

## Restore test

Đây là phần quan trọng nhất nhưng thường bị bỏ qua.

Một restore test có thể là:

```text
1. tạo môi trường trống
2. lấy backup theo đúng procedure
3. verify checksum
4. restore file/database
5. khởi động service
6. chạy health + business smoke test
7. đo thời gian thực tế
```

Nếu restore chưa từng được chạy, RTO chỉ là giả định.

## Restore vào staging trước production

Với file config:

```bash
mkdir -p /tmp/restore-verify
tar -xzf backup.tar.gz -C /tmp/restore-verify
```

Sau đó:

```bash
diff -ru /etc/myapp /tmp/restore-verify/etc/myapp
```

Cách này giảm rủi ro overwrite ngay dữ liệu đang chạy.

## Permission, owner và extended metadata

Backup chỉ content nhưng mất owner, mode, ACL hoặc symlink có thể không phục hồi behavior đầy đủ.

`tar`/`rsync` có options preserve metadata nhưng cần test dưới quyền phù hợp. Với ACL/xattr, có thể cần option riêng tùy tool/filesystem.

Sau restore hãy kiểm tra:

```bash
ls -la
getfacl <path>
namei -l <path>
```

nếu permission là phần của failure.

## Backup đang chạy mà disk đầy

Backup có thể tự tạo incident nếu ghi vào cùng filesystem gần đầy.

Trước large backup:

```bash
df -h /backup
```

Trong automation cần capacity threshold, retention cleanup an toàn và monitoring.

Không tạo `.tar.gz` khổng lồ trong `/tmp` rồi mới upload nếu `/tmp` nằm trên root filesystem nhỏ.

## Monitoring backup freshness

Job “exit 0” chưa chắc backup usable. Nên monitor:

```text
last successful backup time
backup size bất thường
checksum/integrity result
upload status
restore-test status
retention state
```

Một backup 0 byte được tạo đúng giờ vẫn có thể làm cron trông “thành công” nếu script không validate output.

## Disaster Recovery runbook

DR runbook nên trả lời cụ thể:

```text
ai được quyền quyết định DR?
nguồn backup ở đâu?
credential/key lấy ở đâu?
restore infrastructure trước hay data trước?
DNS/traffic switch thế nào?
version ứng dụng nào tương thích backup?
smoke test nào chứng minh recovery?
rollback DR nếu restore sai thế nào?
```

Runbook càng phụ thuộc trí nhớ của một người càng rủi ro.

## Restore order

Trong hệ thống nhiều dependency, thứ tự có thể là:

```text
network/storage
→ database
→ secrets/config
→ application
→ reverse proxy/load balancer
→ scheduled jobs
→ traffic
```

Không có thứ tự chung cho mọi hệ thống, nhưng dependency graph phải rõ.

## Mô hình tư duy (Mental Model)

Backup là **khả năng quay từ trạng thái hỏng về một trạng thái đã biết và sử dụng được**.

```text
protected data
→ captured consistently
→ stored in independent failure domain
→ integrity verified
→ retained theo policy
→ regularly restored and tested
```

Nếu thiếu bước cuối, backup chưa được chứng minh.

## Những hiểu lầm phổ biến

**“Có snapshot là có backup.”** Snapshot có thể cùng failure domain và không độc lập.

**“Rsync mirror là backup.”** Mirror có thể sao chép luôn deletion/corruption.

**“Backup job success là dữ liệu restore được.”** Chỉ restore test mới chứng minh end-to-end.

**“Backup database data directory bằng `cp` là đủ.”** Consistency phụ thuộc database engine và trạng thái write.

**“Giữ backup cùng server vẫn an toàn vì ở disk khác.”** Một host compromise hoặc operational mistake có thể ảnh hưởng cả hai.

## Kết nối kiến thức

Backup liên hệ [Storage và Filesystems](../06_resources/storage_filesystems.md), [I/O Performance](../06_resources/io_performance.md), [Scheduling và Automation](./scheduling_automation.md), [Security và Hardening](./security_hardening.md), [Deployment và Rollback](./deployment_release_rollback.md) và quy trình incident trong [Production Troubleshooting](../09_production/production_troubleshooting.md).