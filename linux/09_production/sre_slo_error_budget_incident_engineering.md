# SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ máy chủ (server / 서버) health tới dịch vụ (service / 서비스) độ tin cậy (reliability / 신뢰성)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **SLI là gì?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối SRE với SLO, error budget và incident engineering, để quyết định tốc độ phát hành dựa trên độ tin cậy đo được.

Linux cung cấp các chỉ số về CPU, bộ nhớ (memory / 메모리), I/O, mạng (network / 네트워크) và tiến trình (process / 프로세스). Nhưng môi trường vận hành (production / 운영 환경) độ tin cậy (reliability / 신뢰성) không được quyết định chỉ bằng việc các chỉ số đó “trông đẹp”. Câu hỏi quan trọng hơn là: **người dùng đang nhận được mức dịch vụ nào, hệ thống có đáp ứng mục tiêu đã cam kết không, và khi có lỗi thì ta ưu tiên phục hồi hay điều tra như thế nào?**

Đây là vùng giao giữa Linux operations và **Site độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) (SRE)**.

## Từ máy chủ (server / 서버) health tới dịch vụ (service / 서비스) độ tin cậy (reliability / 신뢰성)

Một máy chủ (server / 서버) có CPU 20%, RAM còn nhiều và disk chưa đầy vẫn có thể phục vụ người dùng rất tệ nếu phụ thuộc (dependency / 의존성) hết thời gian chờ (timeout / 타임아웃) hoặc ứng dụng (application / 애플리케이션) lỗi (error / 오류) tỷ lệ (rate / 비율) cao.

Ngược lại một máy chủ (server / 서버) CPU 80% vẫn có thể hoàn toàn ổn nếu độ trễ (latency / 지연 시간) và lỗi (error / 오류) tỷ lệ (rate / 비율) nằm trong mục tiêu.

Do đó:

```text
resource health ≠ user-visible reliability
```

Tài nguyên (resource / 자원) metrics là nguyên nhân tiềm năng hoặc tín hiệu hỗ trợ, không phải mục tiêu cuối cùng.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **SLI là gì?** nối từ **Từ máy chủ (server / 서버) health tới dịch vụ (service / 서비스) độ tin cậy (reliability / 신뢰성)** sang **SLO là gì?**, vì cơ chế trước tạo đầu vào cho bước sau.

## SLI là gì?

**Chỉ số mức dịch vụ (service Level Indicator - SLI)** là đại lượng đo trải nghiệm hoặc kết quả dịch vụ.

Ví dụ:

- tỷ lệ yêu cầu (request / 요청) thành công;
- p95/p99 độ trễ (latency / 지연 시간);
- tỷ lệ job hoàn thành đúng thời gian;
- tỷ lệ dữ liệu được xử lý chính xác;
- availability từ góc nhìn người dùng.

SLI nên đo gần trải nghiệm thực tế nhất có thể.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **SLO là gì?** nối từ **SLI là gì?** sang **SLA khác SLO**, vì cơ chế trước tạo đầu vào cho bước sau.

## SLO là gì?

**Mục tiêu mức dịch vụ (service Level Objective - SLO)** là mục tiêu cụ thể cho SLI trong một khoảng thời gian.

Ví dụ:

```text
99.9% request thành công trong 30 ngày
```

hoặc:

```text
99% request có latency < 300 ms trong 28 ngày
```

SLO là mục tiêu kỹ thuật/nội bộ để điều khiển quyết định độ tin cậy (reliability / 신뢰성).

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **SLA khác SLO** nối từ **SLO là gì?** sang **Lỗi (error / 오류) ngân sách (budget / 예산)**, vì cơ chế trước tạo đầu vào cho bước sau.

## SLA khác SLO

**dịch vụ (service / 서비스) mức (level / 수준) Agreement (SLA)** thường là cam kết kinh doanh hoặc hợp đồng, có thể kèm penalty.

SLO thường là mục tiêu nội bộ nên chặt hơn SLA để có an toàn (safety / 안전) margin.

Không nên dùng hai thuật ngữ như đồng nghĩa.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Lỗi (error / 오류) ngân sách (budget / 예산)** nối từ **SLA khác SLO** sang **Vì sao lỗi (error / 오류) ngân sách (budget / 예산) hữu ích?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lỗi (error / 오류) ngân sách (budget / 예산)

Nếu SLO là 99.9%, phần còn lại là **ngân sách lỗi (error budget)**:

```text
100% - 99.9% = 0.1%
```

Trong 30 ngày:

```text
30 × 24 × 60 = 43,200 phút
0.1% ≈ 43.2 phút
```

Con số này chỉ là trực giác nếu SLI đo availability theo thời gian; với request-based SLI, ngân sách (budget / 예산) tính trên số yêu cầu (request / 요청) xấu.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Vì sao lỗi (error / 오류) ngân sách (budget / 예산) hữu ích?** nối từ **Lỗi (error / 오류) ngân sách (budget / 예산)** sang **Good sự kiện (event / 이벤트) và bad sự kiện (event / 이벤트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao lỗi (error / 오류) ngân sách (budget / 예산) hữu ích?

Độ tin cậy (reliability / 신뢰성) tuyệt đối 100% thường cực kỳ đắt và có thể làm tốc độ thay đổi chậm. lỗi (error / 오류) ngân sách (budget / 예산) tạo một ngôn ngữ chung:

```text
nếu budget còn nhiều
→ có thể chấp nhận nhiều thay đổi hơn

nếu budget gần cạn
→ ưu tiên reliability, giảm risky changes
```

Đây là cơ chế cân bằng tốc độ phát triển và độ ổn định.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Good sự kiện (event / 이벤트) và bad sự kiện (event / 이벤트)** nối từ **Vì sao lỗi (error / 오류) ngân sách (budget / 예산) hữu ích?** sang **Phạm vi (scope / 범위) của denominator**, vì cơ chế trước tạo đầu vào cho bước sau.

## Good sự kiện (event / 이벤트) và bad sự kiện (event / 이벤트)

Với request-based availability:

```text
SLI = good requests / valid requests
```

Cần định nghĩa “good” cẩn thận. HTTP 200 chưa chắc là thành công nếu phản hồi (response / 응답) sai nghiệp vụ. HTTP 500 có thể là lỗi rõ ràng, nhưng hết thời gian chờ (timeout / 타임아웃) ở bộ cân bằng tải (load balancer / 로드 밸런서) cũng phải được tính dù backend không ghi log.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Phạm vi (scope / 범위) của denominator** nối từ **Good sự kiện (event / 이벤트) và bad sự kiện (event / 이벤트)** sang **Availability và độ trễ (latency / 지연 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phạm vi (scope / 범위) của denominator

Không phải yêu cầu (request / 요청) nào cũng nên vào denominator. Ví dụ traffic health check nội bộ có thể làm số liệu đẹp giả tạo nếu chiếm tỷ lệ lớn.

SLI phải phản ánh traffic có ý nghĩa với người dùng.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Phạm vi (scope / 범위) của denominator** nêu quy tắc; **Availability và độ trễ (latency / 지연 시간)** thử quy tắc trong tình huống, rồi **Percentile độ trễ (latency / 지연 시간)** mở rộng hệ quả.

## Availability và độ trễ (latency / 지연 시간)

Dịch vụ (service / 서비스) có thể trả phản hồi (response / 응답) thành công nhưng quá chậm để hữu ích. Vì vậy thường cần nhiều SLI:

```text
availability SLI
latency SLI
correctness SLI
freshness SLI
```

Tùy sản phẩm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Availability và độ trễ (latency / 지연 시간)** nêu quy tắc; **Percentile độ trễ (latency / 지연 시간)** thử quy tắc trong tình huống, rồi **Percentile không cộng trực tiếp** mở rộng hệ quả.

## Percentile độ trễ (latency / 지연 시간)

Average độ trễ (latency / 지연 시간) thường che tail độ trễ (latency / 지연 시간).

Ví dụ:

```text
90 request = 50 ms
9 request  = 500 ms
1 request  = 10 s
```

Average có thể vẫn nhìn chấp nhận được nhưng 1% người dùng trải nghiệm rất tệ.

Do đó p95/p99 thường quan trọng trong môi trường vận hành (production / 운영 환경).

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Percentile không cộng trực tiếp** nối từ **Percentile độ trễ (latency / 지연 시간)** sang **Burn tỷ lệ (rate / 비율)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Percentile không cộng trực tiếp

Không nên lấy p99 của từng dịch vụ (service / 서비스) rồi cộng để suy ra p99 end-to-end. Percentile không có tính cộng tuyến đơn giản như average.

Muốn hiểu đường đi của yêu cầu (request path / 요청 경로), phân tán (distributed / 분산) tracing hoặc histogram đúng cách hữu ích hơn.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Burn tỷ lệ (rate / 비율)** nối từ **Percentile không cộng trực tiếp** sang **Multi-window alert**, vì cơ chế trước tạo đầu vào cho bước sau.

## Burn tỷ lệ (rate / 비율)

**Burn tỷ lệ (rate / 비율)** cho biết lỗi (error / 오류) ngân sách (budget / 예산) đang bị tiêu nhanh gấp bao nhiêu tốc độ cho phép.

Nếu ngân sách (budget / 예산) 30 ngày nhưng tốc độ lỗi hiện tại có thể làm cạn ngân sách (budget / 예산) trong vài giờ, đó là burn tỷ lệ (rate / 비율) rất cao.

Burn-rate alert thường tốt hơn alert trực tiếp “lỗi (error / 오류) tỷ lệ (rate / 비율) > X” vì nó liên hệ lỗi với SLO.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Multi-window alert** nối từ **Burn tỷ lệ (rate / 비율)** sang **Page, ticket và dashboard khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## Multi-window alert

Một mẫu (pattern / 패턴) phổ biến là kết hợp cửa sổ ngắn và dài:

```text
short window
→ phát hiện sự cố lớn nhanh

long window
→ tránh alert vì spike ngắn không đáng kể
```

Ví dụ một quy tắc (rule / 규칙) có thể yêu cầu burn tỷ lệ (rate / 비율) cao ở cả 5 phút và 1 giờ trước khi page.

Mục tiêu là cân bằng detection speed với alert noise.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Page, ticket và dashboard khác nhau** nối từ **Multi-window alert** sang **Symptom-based alerting**, vì cơ chế trước tạo đầu vào cho bước sau.

## Page, ticket và dashboard khác nhau

Không phải chỉ số (metric / 지표) bất thường nào cũng cần đánh thức người trực.

Một phân loại hữu ích:

```text
page
→ cần hành động ngay để bảo vệ SLO/user

ticket
→ cần xử lý nhưng không khẩn cấp

dashboard
→ dùng quan sát/trend/capacity
```

Alert tốt phải gắn với hành động.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Symptom-based alerting** nối từ **Page, ticket và dashboard khác nhau** sang **Cause-based alert vẫn có vai trò**, vì cơ chế trước tạo đầu vào cho bước sau.

## Symptom-based alerting

Alert tốt thường bắt đầu từ triệu chứng người dùng:

- yêu cầu (request / 요청) failures;
- độ trễ (latency / 지연 시간) vượt SLO;
- hàng đợi (queue / 큐) không hoàn thành;
- dữ liệu stale.

Tài nguyên (resource / 자원) alerts như CPU cao hữu ích nhưng nên là supporting alert hoặc sức chứa (capacity / 용량) tín hiệu (signal / 신호) nếu chưa gây impact.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Cause-based alert vẫn có vai trò** nối từ **Symptom-based alerting** sang **Sự cố (incident / 인시던트) là gì?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cause-based alert vẫn có vai trò

Một số nguyên nhân cần alert trước khi người dùng (user / 사용자) impact rõ ràng, ví dụ disk sắp đầy hoặc certificate sắp hết hạn.

Điểm quan trọng là phải biết alert thuộc loại **symptom** hay **cause** để đặt severity và phản hồi (response / 응답) phù hợp.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Sự cố (incident / 인시던트) là gì?** nối từ **Cause-based alert vẫn có vai trò** sang **Sự cố (incident / 인시던트) commander**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sự cố (incident / 인시던트) là gì?

Sự cố (incident / 인시던트) là sự kiện môi trường vận hành (production / 운영 환경) làm dịch vụ suy giảm đáng kể hoặc có nguy cơ cao vi phạm mục tiêu.

Không phải mọi lỗi log đều là sự cố (incident / 인시던트).

Sự cố (incident / 인시던트) management cần ba dòng công việc song song:

```text
1. phục hồi dịch vụ
2. giao tiếp/trạng thái
3. thu thập bằng chứng và điều tra
```

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Sự cố (incident / 인시던트) commander** nối từ **Sự cố (incident / 인시던트) là gì?** sang **Operational roles**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sự cố (incident / 인시던트) commander

Trong sự cố lớn, nên có vai trò điều phối thay vì mọi kỹ sư cùng gõ lệnh không phối hợp.

**sự cố (incident / 인시던트) commander** tập trung vào:

- ưu tiên hành động;
- phân công;
- quyết định quay lui (rollback / 롤백)/failover;
- duy trì timeline;
- giảm xung đột thao tác.

Người hiểu sâu kỹ thuật nhất không nhất thiết phải là sự cố (incident / 인시던트) commander.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Operational roles** nối từ **Sự cố (incident / 인시던트) commander** sang **Timeline**, vì cơ chế trước tạo đầu vào cho bước sau.

## Operational roles

Tùy tổ chức có thể tách:

- sự cố (incident / 인시던트) commander;
- operations lead;
- communications lead;
- subject-matter experts.

Trong nhóm (team / 팀) nhỏ, một người có thể kiêm nhiều vai trò.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Timeline** nối từ **Operational roles** sang **Detection, acknowledgement, mitigation, khôi phục (recovery / 복구)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Timeline

Timeline chính xác cực kỳ quan trọng:

```text
14:02 deploy version A
14:05 latency tăng
14:07 alert firing
14:10 rollback bắt đầu
14:14 error rate phục hồi
```

Đối chiếu timeline với log/systemd/deploy lịch sử (history / 이력) giúp tránh suy đoán bằng trí nhớ sau sự cố.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Detection, acknowledgement, mitigation, khôi phục (recovery / 복구)** nối từ **Timeline** sang **MTTR dễ bị hiểu sai**, vì cơ chế trước tạo đầu vào cho bước sau.

## Detection, acknowledgement, mitigation, khôi phục (recovery / 복구)

Có thể tách thời gian sự cố (incident / 인시던트):

```text
T0: failure bắt đầu
T1: phát hiện
T2: người vận hành nhận biết
T3: mitigation bắt đầu
T4: service phục hồi
```

Từ đó có các khoảng:

- thời gian (time / 시간) to detect;
- thời gian (time / 시간) to acknowledge;
- thời gian (time / 시간) to mitigate;
- thời gian (time / 시간) to recover.

Không nên gom tất cả thành một MTTR duy nhất nếu muốn cải tiến đúng chỗ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **MTTR dễ bị hiểu sai** nối từ **Detection, acknowledgement, mitigation, khôi phục (recovery / 복구)** sang **Khôi phục (recovery / 복구) trước, RCA sau**, vì cơ chế trước tạo đầu vào cho bước sau.

## MTTR dễ bị hiểu sai

MTTR có thể được dùng cho mean thời gian (time / 시간) to repair/recover/resolve tùy tổ chức. Nếu không định nghĩa rõ, chỉ số (metric / 지표) dễ gây hiểu nhầm.

Nên ưu tiên định nghĩa cụ thể từng timestamp và percentile của thời gian xử lý.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Khôi phục (recovery / 복구) trước, RCA sau** nối từ **MTTR dễ bị hiểu sai** sang **Safe quay lui (rollback / 롤백)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khôi phục (recovery / 복구) trước, RCA sau

Khi người dùng (user / 사용자) impact lớn, mục tiêu đầu tiên thường là giảm impact:

```text
rollback
failover
scale out
feature flag off
traffic shed
```

Không cần biết toàn bộ nguyên nhân gốc (root cause / 근본 원인) trước khi thực hiện mitigation an toàn.

Nhưng phải thu thập bằng chứng (evidence / 증거) trước khi thao tác nếu có thể.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Safe quay lui (rollback / 롤백)** nối từ **Khôi phục (recovery / 복구) trước, RCA sau** sang **Tải (load / 로드) shedding**, vì cơ chế trước tạo đầu vào cho bước sau.

## Safe quay lui (rollback / 롤백)

Quay lui (rollback / 롤백) chỉ an toàn nếu trạng thái (state / 상태)/dữ liệu (data / 데이터) lược đồ (schema / 스키마) còn tương thích.

Nếu bản phát hành (release / 릴리스) mới đã chạy irreversible cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션), nhị phân (binary / 이진) quay lui (rollback / 롤백) có thể không đủ.

Do đó sự cố (incident / 인시던트) kỹ thuật (engineering / 엔지니어링) liên kết trực tiếp với triển khai (deployment / 배포) thiết kế (design / 설계).

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Tải (load / 로드) shedding** nối từ **Safe quay lui (rollback / 롤백)** sang **Graceful degradation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tải (load / 로드) shedding

Khi hệ thống overload, cố phục vụ mọi yêu cầu (request / 요청) có thể làm tất cả cùng hết thời gian chờ (timeout / 타임아웃). **tải (load / 로드) shedding** chủ động từ chối một phần traffic để bảo vệ cốt lõi (core / 핵심) dịch vụ (service / 서비스).

Ví dụ:

```text
100% request → overload → 0% useful result
```

có thể tệ hơn:

```text
80% request accepted → healthy latency
20% rejected nhanh
```

Tùy nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론).

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Graceful degradation** nối từ **Tải (load / 로드) shedding** sang **Thử lại (retry / 재시도) storm**, vì cơ chế trước tạo đầu vào cho bước sau.

## Graceful degradation

Một dịch vụ (service / 서비스) có thể giữ chức năng chính nhưng tạm tắt chức năng phụ:

```text
recommendation unavailable
nhưng checkout vẫn hoạt động
```

Thiết kế degradation đường dẫn (path / 경로) trước sự cố (incident / 인시던트) tốt hơn phát minh trong lúc khẩn cấp.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Thử lại (retry / 재시도) storm** nối từ **Graceful degradation** sang **Exponential backoff và jitter**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thử lại (retry / 재시도) storm

Thử lại (retry / 재시도) không có backoff/jitter có thể biến lỗi nhỏ thành outage lớn:

```text
backend chậm
→ client timeout
→ tất cả retry ngay
→ backend tải cao hơn
→ chậm hơn
```

Đây là vòng phản hồi (feedback loop / 피드백 루프) dương nguy hiểm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Exponential backoff và jitter** nối từ **Thử lại (retry / 재시도) storm** sang **Circuit breaker**, vì cơ chế trước tạo đầu vào cho bước sau.

## Exponential backoff và jitter

Một thử lại (retry / 재시도) chính sách (policy / 정책) tốt thường có:

- giới hạn số lần thử lại (retry / 재시도);
- exponential backoff;
- jitter;
- thử lại (retry / 재시도) chỉ lỗi phù hợp;
- deadline tổng thể.

Thử lại (retry / 재시도) phải nằm trong **ngân sách thời gian chờ (timeout budget / 타임아웃 예산)** end-to-end.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Circuit breaker** nối từ **Exponential backoff và jitter** sang **Bulkhead**, vì cơ chế trước tạo đầu vào cho bước sau.

## Circuit breaker

Circuit breaker tạm ngừng gọi phụ thuộc (dependency / 의존성) khi thất bại (failure / 실패) tỷ lệ (rate / 비율) cao, giúp giảm áp lực và thất bại (fail / 실패) fast.

Nhưng threshold/khôi phục (recovery / 복구) sai có thể gây oscillation hoặc giữ dịch vụ (service / 서비스) ở trạng thái mở quá lâu.

Đây là điều khiển (control / 제어) hệ thống (system / 시스템), không phải magic mẫu (pattern / 패턴).

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Bulkhead** nối từ **Circuit breaker** sang **Hàng đợi (queue / 큐) và backpressure**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bulkhead

**Bulkhead** tách tài nguyên (resource / 자원) pool để một phụ thuộc (dependency / 의존성) hoặc tải công việc (workload / 워크로드) không làm cạn toàn bộ luồng thực thi (thread / 스레드)/liên kết (connection / 연결) của dịch vụ (service / 서비스).

Ví dụ:

```text
payment pool riêng
reporting pool riêng
```

Reporting chậm không làm payment hết luồng thực thi (thread / 스레드).

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Hàng đợi (queue / 큐) và backpressure** nối từ **Bulkhead** sang **Saturation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hàng đợi (queue / 큐) và backpressure

Hàng đợi (queue / 큐) hấp thụ burst nhưng không tạo sức chứa (capacity / 용량). Nếu arrival tỷ lệ (rate / 비율) trung bình > dịch vụ (service / 서비스) tỷ lệ (rate / 비율), hàng đợi (queue / 큐) sẽ tăng tới giới hạn.

Do đó alert hàng đợi (queue / 큐) độ sâu (depth / 깊이) cần liên hệ với processing tỷ lệ (rate / 비율) và age của item.

Một hàng đợi (queue / 큐) có 10,000 item nhưng xử lý 100,000/s có thể ổn; hàng đợi (queue / 큐) 100 item nhưng mỗi item chờ 30 phút có thể rất xấu.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Saturation** nối từ **Hàng đợi (queue / 큐) và backpressure** sang **RED phương thức (method / 메서드)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Saturation

Trong USE phương thức (method / 메서드):

```text
Utilization
Saturation
Errors
```

**Saturation** là lượng công việc đang chờ tài nguyên, ví dụ run hàng đợi (queue / 큐) hoặc I/O hàng đợi (queue / 큐). Đây thường là dấu hiệu gần bottleneck hơn utilization đơn lẻ.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **RED phương thức (method / 메서드)** nối từ **Saturation** sang **Correlate SLI với Linux metrics**, vì cơ chế trước tạo đầu vào cho bước sau.

## RED phương thức (method / 메서드)

Cho request-driven dịch vụ (service / 서비스):

```text
Rate
Errors
Duration
```

RED giúp nhìn dịch vụ (service / 서비스) từ bên ngoài; USE giúp nhìn tài nguyên (resource / 자원) từ bên trong.

Hai phương pháp bổ sung nhau.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Correlate SLI với Linux metrics** nối từ **RED phương thức (method / 메서드)** sang **Sức chứa (capacity / 용량) headroom**, vì cơ chế trước tạo đầu vào cho bước sau.

## Correlate SLI với Linux metrics

Ví dụ p99 độ trễ (latency / 지연 시간) tăng:

```text
SLI latency xấu
    ↓
kiểm tra RED
    ↓
request rate có tăng?
error có tăng?
    ↓
kiểm tra USE
    ↓
CPU saturation?
memory pressure?
I/O queue?
network retransmission?
```

Đây là cách nối nghiệp vụ (business / 비즈니스) symptom với Linux bằng chứng (evidence / 증거).

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Sức chứa (capacity / 용량) headroom** nối từ **Correlate SLI với Linux metrics** sang **Miền lỗi (failure domain / 장애 도메인)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sức chứa (capacity / 용량) headroom

Nếu dịch vụ (service / 서비스) chỉ khỏe khi CPU < 70%, phần còn lại là headroom để hấp thụ burst/thất bại (failure / 실패).

Sức chứa (capacity / 용량) planning không nên tối ưu “average utilization cao nhất có thể”; cần đủ margin cho:

- nút (node / 노드) thất bại (failure / 실패);
- traffic spike;
- deploy overlap;
- GC/compaction;
- thử lại (retry / 재시도) burst.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Miền lỗi (failure domain / 장애 도메인)** nối từ **Sức chứa (capacity / 용량) headroom** sang **N+1 sức chứa (capacity / 용량)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Miền lỗi (failure domain / 장애 도메인)

Không chỉ số lượng instance mà vị trí của chúng quan trọng.

```text
10 instance cùng một host
```

không có độ tin cậy (reliability / 신뢰성) giống:

```text
10 instance phân bố nhiều host/AZ
```

SLO cần xem xét miền lỗi (failure domain / 장애 도메인) thực tế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **N+1 sức chứa (capacity / 용량)** nối từ **Miền lỗi (failure domain / 장애 도메인)** sang **Cascading thất bại (failure / 실패)**, vì cơ chế trước tạo đầu vào cho bước sau.

## N+1 sức chứa (capacity / 용량)

Nếu hệ thống cần chịu được mất một nút (node / 노드), sức chứa (capacity / 용량) còn lại sau khi mất nút (node / 노드) vẫn phải đáp ứng traffic mục tiêu.

Nếu 4 nút (node / 노드) mỗi nút (node / 노드) chạy 25% tải (load / 로드), mất một nút (node / 노드) làm ba nút (node / 노드) còn lại khoảng 33%. Nếu bình thường mỗi nút (node / 노드) đã 80%, mất một nút (node / 노드) có thể gây cascade overload.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Cascading thất bại (failure / 실패)** nối từ **N+1 sức chứa (capacity / 용량)** sang **Postmortem**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cascading thất bại (failure / 실패)

Một phụ thuộc (dependency / 의존성) chậm có thể giữ luồng thực thi (thread / 스레드) upstream, làm pool cạn, khiến yêu cầu (request / 요청) mới hết thời gian chờ (timeout / 타임아웃), gây thử lại (retry / 재시도) và lan ra nhiều dịch vụ (service / 서비스).

Cascading thất bại (failure / 실패) thường là chuỗi tài nguyên (resource / 자원) coupling, không chỉ một thành phần (component / 컴포넌트) lỗi.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Postmortem** nối từ **Cascading thất bại (failure / 실패)** sang **Nguyên nhân gốc (root cause / 근본 원인) không luôn là một nguyên nhân**, vì cơ chế trước tạo đầu vào cho bước sau.

## Postmortem

Sau sự cố (incident / 인시던트) đáng kể, postmortem nên ghi:

```text
impact
summary
trigger
contributing factors
timeline
detection
response
what went well
what went poorly
action items
```

Mục tiêu là cải thiện hệ thống, không tìm người để đổ lỗi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Nguyên nhân gốc (root cause / 근본 원인) không luôn là một nguyên nhân** nối từ **Postmortem** sang **Hành động (action / 동작) item tốt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Nguyên nhân gốc (root cause / 근본 원인) không luôn là một nguyên nhân

Hệ thống phức tạp thường có:

```text
trigger
+
latent condition
+
missing guardrail
+
weak detection
```

Ví dụ deploy bug là trigger, nhưng thiếu canary và quay lui (rollback / 롤백) khó mới biến nó thành outage dài.

Do đó postmortem tốt phân tích **contributing factors** thay vì cố ép mọi thứ về một “nguyên nhân gốc (root cause / 근본 원인) duy nhất”.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Hành động (action / 동작) item tốt** nối từ **Nguyên nhân gốc (root cause / 근본 원인) không luôn là một nguyên nhân** sang **Toil**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hành động (action / 동작) item tốt

Hành động (action / 동작) item nên cụ thể, có đơn vị sở hữu (owner / 오너) và tiêu chí hoàn thành.

Yếu:

```text
cẩn thận hơn khi deploy
```

Tốt hơn:

```text
thêm automated smoke test kiểm tra endpoint X trước khi chuyển 100% traffic
```

Hệ thống hóa tốt hơn nhắc nhở con người.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Toil** nối từ **Hành động (action / 동작) item tốt** sang **Runbook**, vì cơ chế trước tạo đầu vào cho bước sau.

## Toil

Trong SRE, **toil** là công việc vận hành thủ công, lặp lại, có tính tactical và tăng theo quy mô dịch vụ.

Ví dụ:

- SSH vào từng máy chủ (server / 서버) để restart định kỳ;
- sửa log rotation bằng tay;
- bản sao (copy / 복사) certificate thủ công mỗi tháng.

Automation nên giảm toil, nhưng automation kém có thể tăng blast radius. Vì vậy cần idempotency, kiểm tra hợp lệ (validation / 검증) và quay lui (rollback / 롤백).

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Runbook** nối từ **Toil** sang **Game day và chaos testing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Runbook

Runbook tốt không chỉ là danh sách command. Nó cần:

```text
symptom
preconditions
safety checks
diagnostic decision points
mitigation
verification
rollback/escalation
```

Runbook càng gần nhân quả (causal / 인과적) mô hình (model / 모델) càng hữu ích khi stress cao.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Game day và chaos testing** nối từ **Runbook** sang **Backup không có restore kiểm thử (test / 테스트) không phải guarantee**, vì cơ chế trước tạo đầu vào cho bước sau.

## Game day và chaos testing

Không nên đợi sự cố (incident / 인시던트) thật mới biết failover không hoạt động. Game day mô phỏng thất bại (failure / 실패) có kiểm soát để kiểm tra:

- alert;
- runbook;
- communication;
- backup/restore;
- sức chứa (capacity / 용량) khi mất nút (node / 노드).

Chaos kỹ thuật (engineering / 엔지니어링) là phiên bản có hệ thống hơn của tư duy thử thất bại (failure / 실패) hypothesis.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Backup không có restore kiểm thử (test / 테스트) không phải guarantee** nối từ **Game day và chaos testing** sang **Thay đổi (change / 변경) thất bại (failure / 실패) tỷ lệ (rate / 비율)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Backup không có restore kiểm thử (test / 테스트) không phải guarantee

Một backup job “success” chỉ chứng minh job đã tạo đầu ra (output / 출력) theo cách nào đó. độ tin cậy (reliability / 신뢰성) yêu cầu định kỳ restore và verify ứng dụng (application / 애플리케이션)/dữ liệu (data / 데이터) consistency.

Điều này liên kết SRE với disaster khôi phục (recovery / 복구).

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Thay đổi (change / 변경) thất bại (failure / 실패) tỷ lệ (rate / 비율)** nối từ **Backup không có restore kiểm thử (test / 테스트) không phải guarantee** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thay đổi (change / 변경) thất bại (failure / 실패) tỷ lệ (rate / 비율)

Một hệ thống có thể theo dõi tỷ lệ deploy gây sự cố (incident / 인시던트)/quay lui (rollback / 롤백). Đây là một tín hiệu (signal / 신호) về chất lượng (quality / 품질) của delivery chuỗi xử lý (pipeline / 파이프라인).

Nhưng chỉ số (metric / 지표) không nên biến thành mục tiêu thưởng-phạt máy móc; nếu nhóm (team / 팀) sợ ghi nhận sự cố (incident / 인시던트) để giữ số đẹp, chỉ số (metric / 지표) đã phản tác dụng.

> **Nối mạch:** Trong **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Mô hình tư duy** tổng hợp từ **Thay đổi (change / 변경) thất bại (failure / 실패) tỷ lệ (rate / 비율)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy

SRE nối ba tầng:

```text
user-visible objective
        ↓
service behavior
        ↓
Linux/runtime/resource evidence
```

Linux metrics trả lời **vì sao** dịch vụ (service / 서비스) có thể xấu. SLO trả lời **mức xấu nào thực sự quan trọng**.

> **Nối mạch:** Ở chặng này của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Những hiểu lầm phổ biến** tổng hợp từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến

**“CPU dưới 80% nghĩa hệ thống khỏe.”** User-visible SLI có thể đang vi phạm.

**“SLO 99.9% nghĩa mỗi tháng được phép downtime 43 phút.”** Chỉ đúng với cách đo availability theo thời gian cụ thể; request-based SLI có ngữ nghĩa (semantics / 의미론) khác.

**“Mọi alert phải page.”** Page chỉ nên dành cho sự kiện cần hành động khẩn cấp.

**“Postmortem là tìm người gây lỗi.”** Mục tiêu là tìm điều kiện hệ thống cho phép sự cố (incident / 인시던트) xảy ra và kéo dài.

**“thử lại (retry / 재시도) làm hệ thống đáng tin cậy hơn.”** thử lại (retry / 재시도) không kiểm soát có thể gây thử lại (retry / 재시도) storm.

**“hàng đợi (queue / 큐) giải quyết overload.”** hàng đợi (queue / 큐) chỉ trì hoãn công việc nếu arrival tỷ lệ (rate / 비율) vượt dịch vụ (service / 서비스) tỷ lệ (rate / 비율) lâu dài.

**“Backup thành công nghĩa DR sẵn sàng.”** Chỉ restore kiểm thử (test / 테스트) mới kiểm tra khả năng phục hồi thực tế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **SRE, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và kỹ thuật xử lý sự cố**, **Kết nối kiến thức** nối từ **Những hiểu lầm phổ biến** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết nối kiến thức

Chương này nên được đọc sau [capacity planning](./capacity_planning_server_sizing.md), [production troubleshooting](./production_troubleshooting.md), [deployment/rollback](../08_operations/deployment_release_rollback.md) và [backup/DR](../08_operations/backup_restore_disaster_recovery.md). Nó cung cấp lớp ra quyết định ở trên các chỉ số (metric / 지표) Linux: khi nào cần page, khi nào quay lui (rollback / 롤백), cách định nghĩa độ tin cậy (reliability / 신뢰성) và cách biến sự cố (incident / 인시던트) thành cải tiến hệ thống.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
