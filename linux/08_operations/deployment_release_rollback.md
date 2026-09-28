# Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux

> **Mạch đọc:** Đọc **triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Desired trạng thái (state / 상태) và thời gian chạy (runtime / 런타임) trạng thái (state / 상태)** sang **bản phát hành (release / 릴리스) directory thay vì ghi đè trực tiếp**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Triển khai (deployment / 배포) không chỉ là bản sao (copy / 복사) tệp (file / 파일) mới rồi restart ứng dụng (application / 애플리케이션). Trong môi trường vận hành (production / 운영 환경), một triển khai (deployment / 배포) tốt phải kiểm soát **phiên bản nào đang chạy, thay đổi trạng thái (state / 상태) theo thứ tự nào, cách xác minh sau thay đổi, và cách quay lại trạng thái an toàn nếu lỗi**.

Nếu không có mô hình này, máy chủ (server / 서버) dễ rơi vào trạng thái “cấu hình (config / 설정) mới nhưng nhị phân (binary / 이진) cũ”, “nhị phân (binary / 이진) mới nhưng dịch vụ (service / 서비스) chưa restart”, hoặc quay lui (rollback / 롤백) chỉ quay sản phẩm tạo ra (artifact / 산출물) nhưng không quay cơ sở dữ liệu (database / 데이터베이스)/cấu hình (config / 설정) tương ứng.

## Desired trạng thái (state / 상태) và thời gian chạy (runtime / 런타임) trạng thái (state / 상태)

Một sản phẩm tạo ra (artifact / 산출물) mới tồn tại trên disk không có nghĩa tiến trình (process / 프로세스) đang dùng sản phẩm tạo ra (artifact / 산출물) đó.

```bash
ls -l /opt/app/app.jar
pgrep -af 'java.*app.jar'
systemctl show app -p MainPID -p ExecStart
```

Ba quan sát này trả lời ba câu khác nhau: tệp (file / 파일) nào tồn tại, tiến trình (process / 프로세스) nào đang chạy, và systemd được cấu hình chạy command nào.

Triển khai (deployment / 배포) phải xác minh **thời gian chạy (runtime / 런타임) trạng thái (state / 상태)**, không chỉ tệp (file / 파일) trạng thái (state / 상태).

## Bản phát hành (release / 릴리스) directory thay vì ghi đè trực tiếp

Một mẫu (pattern / 패턴) an toàn hơn:

```text
/opt/app/releases/2026-09-20_203000/
/opt/app/releases/2026-09-20_213000/
/opt/app/current -> /opt/app/releases/2026-09-20_213000/
```

Mỗi bản phát hành (release / 릴리스) là immutable sau khi tạo. `current` là symlink trỏ tới bản phát hành (release / 릴리스) đang active.

Ưu điểm là quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물) có thể chỉ cần chuyển symlink về bản phát hành (release / 릴리스) trước, thay vì cố tái tạo tệp (file / 파일) cũ từ trí nhớ.

## Chuẩn bị bản phát hành (release / 릴리스) trước khi switch

Không nên bản sao (copy / 복사) sản phẩm tạo ra (artifact / 산출물) trực tiếp lên đường dẫn (path / 경로) mà tiến trình (process / 프로세스) đang sử dụng nếu có thể tránh.

Luồng (flow / 흐름) tốt hơn:

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

Nếu CI/CD cung cấp checksum mong đợi, so sánh giúp phát hiện sản phẩm tạo ra (artifact / 산출물) hỏng hoặc nhầm phiên bản (version / 버전).

## Atomic switch bằng symlink

Có thể tạo symlink mới rồi rename:

```bash
ln -s /opt/app/releases/2026-09-20_213000 /opt/app/current.new
mv -T /opt/app/current.new /opt/app/current
```

Rename trong cùng filesystem thường atomic ở không gian tên (namespace / 네임스페이스) mức (level / 수준). Điều này giảm khoảng thời gian `current` ở trạng thái nửa vời.

Cần kiểm tra option `mv -T` có trên hệ thống tương ứng; GNU coreutils hỗ trợ nhưng portability khác nhau.

## Cấu hình (config / 설정) có vòng đời (lifecycle / 생명주기) riêng

Sản phẩm tạo ra (artifact / 산출물) và cấu hình (config / 설정) không nhất thiết nên phiên bản (version / 버전) cùng cách.

Nếu cấu hình (config / 설정) chứa secret hoặc environment-specific values, có thể đặt ngoài bản phát hành (release / 릴리스) directory:

```text
/etc/myapp/application-prod.yml
/opt/app/releases/<version>/app.jar
```

Dịch vụ (service / 서비스) trỏ rõ:

```ini
ExecStart=/usr/bin/java -jar /opt/app/current/app.jar --spring.config.location=/etc/myapp/application-prod.yml
```

Như vậy quay lui (rollback / 롤백) nhị phân (binary / 이진) không vô tình quay lui (rollback / 롤백) secret hoặc môi trường (environment / 환경) setting.

Ngược lại, cấu hình (config / 설정) lược đồ (schema / 스키마) thay đổi cùng mã (code / 코드) phải có tính tương thích (compatibility / 호환성) chiến lược (strategy / 전략) rõ.

## Cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) là phần khó nhất của quay lui (rollback / 롤백)

Nhị phân (binary / 이진) thường quay lui (rollback / 롤백) được tương đối dễ; cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) có thể không.

Nếu phiên bản (version / 버전) mới xóa column hoặc đổi dữ liệu không tương thích, quay nhị phân (binary / 이진) cũ có thể không chạy nữa.

Một chiến lược an toàn là **expand–migrate–đặc tả hợp đồng (contract / 계약)**:

```text
1. Add schema mới nhưng giữ schema cũ
2. Deploy code tương thích cả hai
3. Migrate/backfill dữ liệu
4. Chuyển traffic sang behavior mới
5. Sau khi ổn định mới xóa schema cũ
```

Cách này làm quay lui (rollback / 롤백) trong giai đoạn đầu dễ hơn.

## Restart, reload và zero-downtime

Một single-instance dịch vụ (service / 서비스) restart thường tạo downtime ngắn. Với nhiều instances sau bộ cân bằng tải (load balancer / 로드 밸런서), có thể rolling triển khai (deployment / 배포):

```text
remove instance A khỏi traffic
→ deploy A
→ health check A
→ đưa A lại traffic
→ lặp với B
```

Đây là orchestration ở tầng cao hơn systemd. Systemd quản lý tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) của từng host, còn bộ cân bằng tải (load balancer / 로드 밸런서)/orchestrator quản lý traffic giữa nhiều instances.

## Health check phải phản ánh readiness

Một tiến trình (process / 프로세스) vừa tồn tại chưa chắc sẵn sàng nhận traffic.

```bash
curl -fsS http://127.0.0.1:8080/health
```

Health endpoint nên phân biệt khi cần:

- liveness: tiến trình (process / 프로세스)/app còn sống;
- readiness: app đã sẵn sàng phục vụ;
- phụ thuộc (dependency / 의존성) health: DB/bộ nhớ đệm (cache / 캐시)/downstream có cần healthy không.

Không nên làm health check quá sâu đến mức một phụ thuộc (dependency / 의존성) chập chờn làm toàn fleet bị restart liên tục.

## Smoke kiểm thử (test / 테스트) sau triển khai (deployment / 배포)

Health 200 chưa đủ chứng minh nghiệp vụ (business / 비즈니스) đường dẫn (path / 경로) chính hoạt động. Một smoke kiểm thử (test / 테스트) nhỏ có thể kiểm tra endpoint quan trọng với read-only hoặc synthetic yêu cầu (request / 요청).

Ví dụ:

```bash
curl -fsS https://api.example.com/version
curl -fsS https://api.example.com/health
```

Nếu có `/version`, phản hồi (response / 응답) nên cho biết bản dựng (build / 빌드)/phiên bản (version / 버전) để xác minh đúng bản phát hành (release / 릴리스) đang phục vụ.

## Phiên bản (version / 버전) bằng chứng (evidence / 증거)

Một triển khai (deployment / 배포) đáng tin nên có cách trả lời:

```text
commit nào?
build nào?
artifact checksum nào?
config version nào?
deploy lúc nào?
ai/automation nào deploy?
```

Có thể lưu siêu dữ liệu (metadata / 메타데이터) cạnh bản phát hành (release / 릴리스):

```text
VERSION
COMMIT_SHA
BUILD_TIME
CHECKSUMS
```

Điều này giúp sự cố (incident / 인시던트) timeline chính xác hơn.

## Quay lui (rollback / 롤백) trigger

Quay lui (rollback / 롤백) không nên dựa chỉ vào cảm giác “có vẻ lỗi”. Nên có signals rõ như:

```text
health check fail liên tục
error rate tăng vượt baseline
latency tăng mạnh
critical business test fail
startup fail
```

Với thay đổi risky, cần định nghĩa quay lui (rollback / 롤백) criteria trước triển khai (deployment / 배포).

## Quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물)

Nếu bản phát hành (release / 릴리스) cũ vẫn còn:

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

Quay lui (rollback / 롤백) là một triển khai (deployment / 배포) khác, không phải nút “undo” thần kỳ.

## Backup trước edit thủ công

Nếu buộc phải sửa cấu hình (config / 설정) trực tiếp:

```bash
cp -a /etc/myapp/app.conf /etc/myapp/app.conf.$(date +%F_%H%M%S).bak
```

Sau edit, validate bằng công cụ (tool / 도구) của ứng dụng nếu có trước reload.

Với Nginx:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Mẫu (pattern / 패턴) **validate → apply** nên được ưu tiên.

## Permission và đơn vị sở hữu (owner / 오너) của bản phát hành (release / 릴리스)

Sản phẩm tạo ra (artifact / 산출물) đúng nhưng đơn vị sở hữu (owner / 오너) sai vẫn làm dịch vụ (service / 서비스) thất bại (fail / 실패).

```bash
namei -l /opt/app/current/app.jar
ls -l /opt/app/current/app.jar
systemctl show app -p User -p Group
```

Triển khai (deployment / 배포) automation nên set quyền sở hữu (ownership / 소유권)/chế độ (mode / 모드) theo desired trạng thái (state / 상태), không phụ thuộc tệp (file / 파일) upload tạo ra permission ngẫu nhiên.

## Disk không gian (space / 공간) và retention

Giữ nhiều releases hỗ trợ quay lui (rollback / 롤백) nhưng cũng dùng disk.

Không nên `rm -rf releases/*` rồi giữ mỗi hiện tại (current / 현재). Thay vào đó giữ N bản phát hành (release / 릴리스) gần nhất và chỉ cleanup sau khi xác định hiện tại (current / 현재)/previous.

Trước cleanup:

```bash
df -h /opt/app
ls -ltr /opt/app/releases
readlink -f /opt/app/current
```

## Logging triển khai (deployment / 배포) sự kiện (event / 이벤트)

Sự cố (incident / 인시던트) phân tích (analysis / 분석) rất cần biết triển khai (deployment / 배포) xảy ra lúc nào.

Có thể ghi sự kiện (event / 이벤트) vào log/journal hoặc hệ thống triển khai (deployment / 배포):

```bash
logger -t deploy "myapp version=2026.09.20.2 deployed"
```

Sau đó:

```bash
journalctl -t deploy
```

Timeline “lỗi (error / 오류) bắt đầu 30 giây sau deploy” là bằng chứng (evidence / 증거) mạnh dù chưa phải proof nguyên nhân.

## Canary triển khai (deployment / 배포)

Thay vì đưa phiên bản (version / 버전) mới cho 100% traffic, canary chỉ nhận một phần nhỏ. Nếu metrics tốt mới mở rộng.

Canary giảm blast radius nhưng yêu cầu hạ tầng (infrastructure / 인프라) routing/khả năng quan sát (observability / 관측 가능성) đủ tốt. Nó không phải chỉ là chạy một tiến trình (process / 프로세스) kiểm thử (test / 테스트) trên máy chủ (server / 서버) nếu tiến trình (process / 프로세스) đó không nhận traffic thực tế tương tự môi trường vận hành (production / 운영 환경).

## Blue–green triển khai (deployment / 배포)

Hai environments `blue` và `green` tồn tại song song. Một phía đang active, phía kia nhận bản phát hành (release / 릴리스) mới. Sau kiểm tra hợp lệ (validation / 검증), traffic switch sang môi trường (environment / 환경) mới.

Quay lui (rollback / 롤백) có thể nhanh bằng switch ngược, nhưng cơ sở dữ liệu (database / 데이터베이스)/trạng thái dùng chung (shared state / 공유 상태) vẫn là phần cần tính tương thích (compatibility / 호환성).

## Mô hình tư duy (mental model / 사고 모델)

Triển khai (deployment / 배포) là một **controlled chuyển tiếp trạng thái (state transition / 상태 전이)**:

```text
known old state
→ prepare new state
→ validate before activation
→ activate
→ verify externally observable behavior
→ keep rollback path
```

Mọi bước nên để lại bằng chứng (evidence / 증거) và có thất bại (failure / 실패) handling rõ.

## Những hiểu lầm phổ biến

**“bản sao (copy / 복사) jar thành công nghĩa deploy thành công.”** tiến trình (process / 프로세스) có thể vẫn chạy jar cũ.

**“quay lui (rollback / 롤백) nhị phân (binary / 이진) là quay lui (rollback / 롤백) toàn hệ thống.”** cơ sở dữ liệu (database / 데이터베이스)/cấu hình (config / 설정)/bên ngoài (external / 외부) side effects có thể không quay lui (rollback / 롤백) được.

**“Restart dịch vụ (service / 서비스) là health check.”** Restart thành công chỉ nói tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) không báo lỗi ngay.

**“Giữ bản phát hành (release / 릴리스) cũ là đủ quay lui (rollback / 롤백).”** Cần sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정) tính tương thích (compatibility / 호환성), cơ sở dữ liệu (database / 데이터베이스) chiến lược (strategy / 전략) và procedure đã thử.

## Kết nối kiến thức

Chương này liên kết [Filesystem và Symlink](../01_filesystem/filesystem_paths_inodes_links.md), [systemd và Services](../05_system/systemd_boot_services.md), [Bash Scripting đáng tin cậy](../02_shell/bash_scripting_reliability.md), [Backup và Restore](./backup_restore_disaster_recovery.md) và [Production Troubleshooting](../09_production/production_troubleshooting.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [backup restore disaster recovery](./backup_restore_disaster_recovery.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
