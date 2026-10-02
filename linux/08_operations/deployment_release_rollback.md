# Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Desired trạng thái (state / 상태) và thời gian chạy (runtime / 런타임) trạng thái (state / 상태)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Bản phát hành (release / 릴리스) directory thay vì ghi đè trực tiếp** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối deployment với release, rollback và blast radius, để thay đổi production có đường lui và tiêu chí dừng rõ ràng.

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

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Bản phát hành (release / 릴리스) directory thay vì ghi đè trực tiếp** tiếp nhận điểm tựa từ **Desired trạng thái (state / 상태) và thời gian chạy (runtime / 런타임) trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuẩn bị bản phát hành (release / 릴리스) trước khi switch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bản phát hành (release / 릴리스) directory thay vì ghi đè trực tiếp

Một mẫu (pattern / 패턴) an toàn hơn:

```text
/opt/app/releases/2026-09-20_203000/
/opt/app/releases/2026-09-20_213000/
/opt/app/current -> /opt/app/releases/2026-09-20_213000/
```

Mỗi bản phát hành (release / 릴리스) là immutable sau khi tạo. `current` là symlink trỏ tới bản phát hành (release / 릴리스) đang active.

Ưu điểm là quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물) có thể chỉ cần chuyển symlink về bản phát hành (release / 릴리스) trước, thay vì cố tái tạo tệp (file / 파일) cũ từ trí nhớ.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Chuẩn bị bản phát hành (release / 릴리스) trước khi switch** tiếp nhận điểm tựa từ **Bản phát hành (release / 릴리스) directory thay vì ghi đè trực tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Atomic switch bằng symlink** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Atomic switch bằng symlink** tiếp nhận điểm tựa từ **Chuẩn bị bản phát hành (release / 릴리스) trước khi switch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấu hình (config / 설정) có vòng đời (lifecycle / 생명주기) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Atomic switch bằng symlink

Có thể tạo symlink mới rồi rename:

```bash
ln -s /opt/app/releases/2026-09-20_213000 /opt/app/current.new
mv -T /opt/app/current.new /opt/app/current
```

Rename trong cùng filesystem thường atomic ở không gian tên (namespace / 네임스페이스) mức (level / 수준). Điều này giảm khoảng thời gian `current` ở trạng thái nửa vời.

Cần kiểm tra option `mv -T` có trên hệ thống tương ứng; GNU coreutils hỗ trợ nhưng portability khác nhau.

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Atomic switch bằng symlink** xác định đầu vào; **Cấu hình (config / 설정) có vòng đời (lifecycle / 생명주기) riêng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) là phần khó nhất của quay lui (rollback / 롤백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, cơ chế trong **Cấu hình (config / 설정) có vòng đời (lifecycle / 생명주기) riêng** cần được kiểm chứng bằng dấu vết cụ thể; **Cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) là phần khó nhất của quay lui (rollback / 롤백)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **Restart, reload và zero-downtime** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) là phần khó nhất của quay lui (rollback / 롤백)** nêu điều cần giải thích; **Restart, reload và zero-downtime** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Health check phải phản ánh readiness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Health check phải phản ánh readiness** tiếp nhận điểm tựa từ **Restart, reload và zero-downtime** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Smoke kiểm thử (test / 테스트) sau triển khai (deployment / 배포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Smoke kiểm thử (test / 테스트) sau triển khai (deployment / 배포)** tiếp nhận điểm tựa từ **Health check phải phản ánh readiness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phiên bản (version / 버전) bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Smoke kiểm thử (test / 테스트) sau triển khai (deployment / 배포)

Health 200 chưa đủ chứng minh nghiệp vụ (business / 비즈니스) đường dẫn (path / 경로) chính hoạt động. Một smoke kiểm thử (test / 테스트) nhỏ có thể kiểm tra endpoint quan trọng với read-only hoặc synthetic yêu cầu (request / 요청).

Ví dụ:

```bash
curl -fsS https://api.example.com/version
curl -fsS https://api.example.com/health
```

Nếu có `/version`, phản hồi (response / 응답) nên cho biết bản dựng (build / 빌드)/phiên bản (version / 버전) để xác minh đúng bản phát hành (release / 릴리스) đang phục vụ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Smoke kiểm thử (test / 테스트) sau triển khai (deployment / 배포)** nêu điều cần giải thích; **Phiên bản (version / 버전) bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quay lui (rollback / 롤백) trigger** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Phiên bản (version / 버전) bằng chứng (evidence / 증거)** nêu điều cần giải thích; **Quay lui (rollback / 롤백) trigger** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물)** tiếp nhận điểm tựa từ **Quay lui (rollback / 롤백) trigger** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backup trước edit thủ công** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Backup trước edit thủ công** tiếp nhận điểm tựa từ **Quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Permission và đơn vị sở hữu (owner / 오너) của bản phát hành (release / 릴리스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, sau nội dung của **Backup trước edit thủ công**, **Permission và đơn vị sở hữu (owner / 오너) của bản phát hành (release / 릴리스)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Disk không gian (space / 공간) và retention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Permission và đơn vị sở hữu (owner / 오너) của bản phát hành (release / 릴리스)

Sản phẩm tạo ra (artifact / 산출물) đúng nhưng đơn vị sở hữu (owner / 오너) sai vẫn làm dịch vụ (service / 서비스) thất bại (fail / 실패).

```bash
namei -l /opt/app/current/app.jar
ls -l /opt/app/current/app.jar
systemctl show app -p User -p Group
```

Triển khai (deployment / 배포) automation nên set quyền sở hữu (ownership / 소유권)/chế độ (mode / 모드) theo desired trạng thái (state / 상태), không phụ thuộc tệp (file / 파일) upload tạo ra permission ngẫu nhiên.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Disk không gian (space / 공간) và retention** tiếp nhận điểm tựa từ **Permission và đơn vị sở hữu (owner / 오너) của bản phát hành (release / 릴리스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logging triển khai (deployment / 배포) sự kiện (event / 이벤트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Disk không gian (space / 공간) và retention

Giữ nhiều releases hỗ trợ quay lui (rollback / 롤백) nhưng cũng dùng disk.

Không nên `rm -rf releases/*` rồi giữ mỗi hiện tại (current / 현재). Thay vào đó giữ N bản phát hành (release / 릴리스) gần nhất và chỉ cleanup sau khi xác định hiện tại (current / 현재)/previous.

Trước cleanup:

```bash
df -h /opt/app
ls -ltr /opt/app/releases
readlink -f /opt/app/current
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Logging triển khai (deployment / 배포) sự kiện (event / 이벤트)** tiếp nhận điểm tựa từ **Disk không gian (space / 공간) và retention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Canary triển khai (deployment / 배포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Canary triển khai (deployment / 배포)** tiếp nhận điểm tựa từ **Logging triển khai (deployment / 배포) sự kiện (event / 이벤트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Blue–green triển khai (deployment / 배포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Canary triển khai (deployment / 배포)

Thay vì đưa phiên bản (version / 버전) mới cho 100% traffic, canary chỉ nhận một phần nhỏ. Nếu metrics tốt mới mở rộng.

Canary giảm blast radius nhưng yêu cầu hạ tầng (infrastructure / 인프라) routing/khả năng quan sát (observability / 관측 가능성) đủ tốt. Nó không phải chỉ là chạy một tiến trình (process / 프로세스) kiểm thử (test / 테스트) trên máy chủ (server / 서버) nếu tiến trình (process / 프로세스) đó không nhận traffic thực tế tương tự môi trường vận hành (production / 운영 환경).

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Blue–green triển khai (deployment / 배포)** tiếp nhận điểm tựa từ **Canary triển khai (deployment / 배포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Blue–green triển khai (deployment / 배포)

Hai environments `blue` và `green` tồn tại song song. Một phía đang active, phía kia nhận bản phát hành (release / 릴리스) mới. Sau kiểm tra hợp lệ (validation / 검증), traffic switch sang môi trường (environment / 환경) mới.

Quay lui (rollback / 롤백) có thể nhanh bằng switch ngược, nhưng cơ sở dữ liệu (database / 데이터베이스)/trạng thái dùng chung (shared state / 공유 상태) vẫn là phần cần tính tương thích (compatibility / 호환성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Blue–green triển khai (deployment / 배포)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“bản sao (copy / 복사) jar thành công nghĩa deploy thành công.”** tiến trình (process / 프로세스) có thể vẫn chạy jar cũ.

**“quay lui (rollback / 롤백) nhị phân (binary / 이진) là quay lui (rollback / 롤백) toàn hệ thống.”** cơ sở dữ liệu (database / 데이터베이스)/cấu hình (config / 설정)/bên ngoài (external / 외부) side effects có thể không quay lui (rollback / 롤백) được.

**“Restart dịch vụ (service / 서비스) là health check.”** Restart thành công chỉ nói tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) không báo lỗi ngay.

**“Giữ bản phát hành (release / 릴리스) cũ là đủ quay lui (rollback / 롤백).”** Cần sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정) tính tương thích (compatibility / 호환성), cơ sở dữ liệu (database / 데이터베이스) chiến lược (strategy / 전략) và procedure đã thử.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포), bản phát hành (release / 릴리스) và quay lui (rollback / 롤백) trên Linux**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Chương này liên kết [Filesystem và Symlink](../01_filesystem/filesystem_paths_inodes_links.md), [systemd và Services](../05_system/systemd_boot_services.md), [Bash Scripting đáng tin cậy](../02_shell/bash_scripting_reliability.md), [Backup và Restore](./backup_restore_disaster_recovery.md) và [Production Troubleshooting](../09_production/production_troubleshooting.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
