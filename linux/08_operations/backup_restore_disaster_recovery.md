# Backup, Restore và Disaster khôi phục (recovery / 복구) trên Linux

> **Mạch đọc:** Đọc **Backup, Restore và Disaster khôi phục (recovery / 복구) trên Linux** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Xác định thứ cần bảo vệ** sang **RPO và RTO**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Backup không phải là việc “có một bản bản sao (copy / 복사) ở đâu đó”. Giá trị thực của backup chỉ xuất hiện khi dữ liệu có thể được phục hồi đúng, trong thời gian chấp nhận được và với mức mất dữ liệu nằm trong giới hạn nghiệp vụ. Vì vậy backup phải được thiết kế cùng với **restore** và **disaster khôi phục (recovery / 복구) (DR)** ngay từ đầu.

Một tệp (file / 파일) `.tar.gz` tồn tại không chứng minh hệ thống có thể phục hồi sau sự cố. Nếu không biết nó được tạo từ lúc nào, có đầy đủ dữ liệu hay không, có checksum không, có restore kiểm thử (test / 테스트) không và phụ thuộc nào cần phục hồi cùng, đó chỉ là một sản phẩm tạo ra (artifact / 산출물) chưa được chứng minh.

## Xác định thứ cần bảo vệ

Trước khi chọn command, cần biết tài sản nào thực sự quan trọng. Một Linux ứng dụng (application / 애플리케이션) máy chủ (server / 서버) có thể gồm:

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

Không phải tất cả đều cần backup giống nhau. sản phẩm tạo ra (artifact / 산출물) có thể rebuild từ CI, nhưng cơ sở dữ liệu (database / 데이터베이스) hoặc người dùng (user / 사용자) upload có thể không thể tái tạo.

## RPO và RTO

Hai khái niệm nền tảng:

**RPO (Recovery Point Objective)** là lượng dữ liệu tối đa có thể mất tính theo thời gian. RPO 15 phút nghĩa nghiệp vụ (business / 비즈니스) chấp nhận mất tối đa khoảng 15 phút dữ liệu gần nhất trong disaster scenario được định nghĩa.

**RTO (Recovery Time Objective)** là thời gian tối đa mong muốn để dịch vụ được khôi phục sau sự cố.

Hai con số này quyết định kiến trúc backup. Backup mỗi đêm không thể đáp ứng RPO 15 phút cho cơ sở dữ liệu (database / 데이터베이스) thay đổi liên tục.

## Backup tệp (file / 파일) đơn giản bằng `tar`

Với static cấu hình (configuration / 구성) hoặc directory phù hợp:

```bash
tar -czf app-config-$(date +%F).tar.gz /etc/myapp
```

Trước restore nên inspect archive:

```bash
tar -tzf app-config-2026-09-20.tar.gz | less
```

Không extract trực tiếp vào `/` nếu chưa kiểm tra đường dẫn (path / 경로) và nội dung archive. Có thể extract vào staging directory:

```bash
mkdir -p /tmp/restore-check
tar -xzf app-config-2026-09-20.tar.gz -C /tmp/restore-check
```

Sau đó compare trước khi ghi đè môi trường vận hành (production / 운영 환경).

## `rsync` không tự động là backup

`rsync` rất tốt để đồng bộ:

```bash
rsync -aH --delete /data/ backup-host:/backup/data/
```

Nhưng nếu nguồn (source / 소스) bị xóa hoặc ransomware mã hóa dữ liệu, mirror với `--delete` có thể đồng bộ luôn trạng thái hỏng sang destination.

Vì vậy backup cần **versioning/lịch sử (history / 이력)/immutability** phù hợp, không chỉ mirror latest trạng thái (state / 상태).

`rsync --delete` luôn nên dry-run trước khi dùng thủ công:

```bash
rsync -aHn --delete /data/ backup-host:/backup/data/
```

## Snapshot

Filesystem, LVM, VM hoặc cloud volume có thể hỗ trợ snapshot. Snapshot tạo một point-in-time view nhanh, nhưng không phải lúc nào cũng là backup độc lập.

Nếu snapshot nằm cùng lưu trữ (storage / 저장소)/account và lưu trữ (storage / 저장소) đó hỏng hoặc bị xóa, snapshot có thể biến mất cùng. Snapshot phù hợp làm một lớp khôi phục (recovery / 복구) nhanh, nhưng long-term backup thường cần lĩnh vực (domain / 도메인) thất bại (failure / 실패) khác.

## Crash-consistent và application-consistent

Nếu snapshot khối (block / 블록) thiết bị (device / 장치) trong khi cơ sở dữ liệu (database / 데이터베이스) đang ghi, snapshot có thể **crash-consistent**: tương tự trạng thái disk khi máy mất điện. cơ sở dữ liệu (database / 데이터베이스) engine tốt thường có khôi phục (recovery / 복구) log để phục hồi, nhưng điều đó khác với **application-consistent backup** được tạo qua cơ chế cơ sở dữ liệu (database / 데이터베이스) hỗ trợ.

Không bản sao (copy / 복사) trực tiếp dữ liệu (data / 데이터) directory của cơ sở dữ liệu (database / 데이터베이스) đang chạy rồi giả định backup hợp lệ. Hãy dùng backup cơ chế (mechanism / 메커니즘) của cơ sở dữ liệu (database / 데이터베이스) hoặc snapshot procedure đã được chứng minh.

## Cơ sở dữ liệu (database / 데이터베이스) backup

Mỗi cơ sở dữ liệu (database / 데이터베이스) có chiến lược riêng. Có thể có logical backup, vật lý (physical / 물리적) backup, WAL/binlog/archive log và point-in-time khôi phục (recovery / 복구).

Điểm quan trọng ở Linux mức (level / 수준) là hiểu backup command chỉ là một phần của data-consistency giao thức (protocol / 프로토콜).

Ví dụ logical dump thường tạo dữ liệu portable hơn nhưng restore có thể chậm với cơ sở dữ liệu (database / 데이터베이스) lớn. vật lý (physical / 물리적) backup nhanh hơn nhưng phụ thuộc phiên bản (version / 버전)/lưu trữ (storage / 저장소) bố cục (layout / 레이아웃) nhiều hơn.

## Point-in-Time khôi phục (recovery / 복구)

PITR cho phép restore cơ sở (base / 기반) backup rồi replay giao dịch (transaction / 트랜잭션) logs tới một thời điểm trước sự cố.

Mô hình tư duy (mental model / 사고 모델):

```text
base backup
+ continuous transaction log archive
→ restore tới time T
```

Điều này rất hữu ích khi lỗi lô-gic (logic / 논리) xảy ra, ví dụ accidental delete lúc 15:37. Backup nightly chỉ cho trạng thái đêm trước, còn PITR có thể tiến sát thời điểm trước lỗi.

## Backup cấu hình (configuration / 구성) và secrets

Cấu hình (config / 설정) có thể nằm trong Git, nhưng môi trường vận hành (production / 운영 환경) secrets không nên lần ghi nhận (commit / 커밋) vào repo.

Nếu secret store hoặc certificate là phụ thuộc (dependency / 의존성) quan trọng, DR plan phải nói rõ cách khôi phục chúng. Restore app nhị phân (binary / 이진) mà thiếu TLS private key, DB credential hoặc encryption key có thể làm dữ liệu không dùng được.

Encryption key mất có thể đồng nghĩa backup encrypted vĩnh viễn không thể giải mã.

## Encryption at rest

Backup chứa môi trường vận hành (production / 운영 환경) dữ liệu (data / 데이터) phải được bảo vệ. Có thể cần encryption ở backup công cụ (tool / 도구), lưu trữ (storage / 저장소) provider hoặc filesystem tầng (layer / 계층).

Nhưng encryption tạo thêm key-management phụ thuộc (dependency / 의존성). Không lưu encryption key duy nhất cùng nơi với backup duy nhất rồi gọi đó là disaster khôi phục (recovery / 복구).

## Backup offsite và miền lỗi (failure domain / 장애 도메인)

Nếu môi trường vận hành (production / 운영 환경) disk và backup disk cùng máy, cháy disk/controller hoặc operator `rm` có thể phá cả hai.

Một chiến lược thường có nhiều thất bại (failure / 실패) domains:

```text
local fast recovery copy
+ remote/offsite backup
+ immutable/versioned copy
```

Tùy độ quan trọng dữ liệu, có thể tham khảo nguyên tắc 3-2-1: nhiều bản bản sao (copy / 복사), nhiều loại media/lưu trữ (storage / 저장소) và ít nhất một bản ở miền lỗi (failure domain / 장애 도메인) khác. Đây là heuristic, không phải luật tuyệt đối.

## Immutability

Immutable hoặc object-lock backup giúp chống accidental deletion/ransomware trong retention period.

Tuy nhiên nếu credential có quyền phá retention hoặc account gốc (root / 루트) bị compromise, “immutable” có thể không còn ý nghĩa. bảo mật (security / 보안) thiết kế (design / 설계) phải xem cả định danh (identity / 식별자) và chính sách (policy / 정책) ranh giới (boundary / 경계).

## Checksum và integrity

Sau khi tạo backup, có thể lưu checksum:

```bash
sha256sum backup.tar.gz > backup.tar.gz.sha256
```

Verify:

```bash
sha256sum -c backup.tar.gz.sha256
```

Checksum phát hiện corruption/thay đổi (change / 변경) nhưng không chứng minh dữ liệu bên trong đúng về mặt ứng dụng. Cần restore kiểm thử (test / 테스트) để chứng minh tầng cao hơn.

## Retention

Giữ backup mãi mãi thường không thực tế. Có thể có chính sách (policy / 정책):

```text
hourly: 48 giờ
daily: 30 ngày
weekly: 12 tuần
monthly: 12 tháng
```

Retention phải dựa nghiệp vụ (business / 비즈니스)/legal/lưu trữ (storage / 저장소) các ràng buộc (constraints / 제약조건들). Cleanup cũng là destructive automation nên cần kiểm tra, log và tránh mẫu (pattern / 패턴) wildcard nguy hiểm.

## Restore kiểm thử (test / 테스트)

Đây là phần quan trọng nhất nhưng thường bị bỏ qua.

Một restore kiểm thử (test / 테스트) có thể là:

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

## Restore vào staging trước môi trường vận hành (production / 운영 환경)

Với tệp (file / 파일) cấu hình (config / 설정):

```bash
mkdir -p /tmp/restore-verify
tar -xzf backup.tar.gz -C /tmp/restore-verify
```

Sau đó:

```bash
diff -ru /etc/myapp /tmp/restore-verify/etc/myapp
```

Cách này giảm rủi ro overwrite ngay dữ liệu đang chạy.

## Permission, đơn vị sở hữu (owner / 오너) và extended siêu dữ liệu (metadata / 메타데이터)

Backup chỉ content nhưng mất đơn vị sở hữu (owner / 오너), chế độ (mode / 모드), ACL hoặc symlink có thể không phục hồi hành vi (behavior / 동작) đầy đủ.

`tar`/`rsync` có options preserve siêu dữ liệu (metadata / 메타데이터) nhưng cần kiểm thử (test / 테스트) dưới quyền phù hợp. Với ACL/xattr, có thể cần option riêng tùy công cụ (tool / 도구)/filesystem.

Sau restore hãy kiểm tra:

```bash
ls -la
getfacl <path>
namei -l <path>
```

nếu permission là phần của thất bại (failure / 실패).

## Backup đang chạy mà disk đầy

Backup có thể tự tạo sự cố (incident / 인시던트) nếu ghi vào cùng filesystem gần đầy.

Trước large backup:

```bash
df -h /backup
```

Trong automation cần sức chứa (capacity / 용량) threshold, retention cleanup an toàn và monitoring.

Không tạo `.tar.gz` khổng lồ trong `/tmp` rồi mới upload nếu `/tmp` nằm trên gốc (root / 루트) filesystem nhỏ.

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

Một backup 0 byte được tạo đúng giờ vẫn có thể làm cron trông “thành công” nếu script không validate đầu ra (output / 출력).

## Disaster khôi phục (recovery / 복구) runbook

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

## Restore thứ tự (order / 순서)

Trong hệ thống nhiều phụ thuộc (dependency / 의존성), thứ tự có thể là:

```text
network/storage
→ database
→ secrets/config
→ application
→ reverse proxy/load balancer
→ scheduled jobs
→ traffic
```

Không có thứ tự chung cho mọi hệ thống, nhưng phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) phải rõ.

## Mô hình tư duy (mental model / 사고 모델)

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

**“Có snapshot là có backup.”** Snapshot có thể cùng miền lỗi (failure domain / 장애 도메인) và không độc lập.

**“Rsync mirror là backup.”** Mirror có thể sao chép luôn deletion/corruption.

**“Backup job success là dữ liệu restore được.”** Chỉ restore kiểm thử (test / 테스트) mới chứng minh end-to-end.

**“Backup cơ sở dữ liệu (database / 데이터베이스) dữ liệu (data / 데이터) directory bằng `cp` là đủ.”** Consistency phụ thuộc cơ sở dữ liệu (database / 데이터베이스) engine và trạng thái ghi (write / 쓰기).

**“Giữ backup cùng máy chủ (server / 서버) vẫn an toàn vì ở disk khác.”** Một host compromise hoặc operational mistake có thể ảnh hưởng cả hai.

## Kết nối kiến thức

Backup liên hệ [Storage và Filesystems](../06_resources/storage_filesystems.md), [I/O Performance](../06_resources/io_performance.md), [Scheduling và Automation](./scheduling_automation.md), [Security và Hardening](./security_hardening.md), [Deployment và Rollback](./deployment_release_rollback.md) và quy trình sự cố (incident / 인시던트) trong [Production Troubleshooting](../09_production/production_troubleshooting.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [deployment release rollback](./deployment_release_rollback.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
