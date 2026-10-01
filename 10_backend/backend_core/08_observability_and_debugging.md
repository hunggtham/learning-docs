# 08. khả năng quan sát (observability / 관측 가능성) và debugging

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **08. khả năng quan sát (observability / 관측 가능성) và debugging**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Ba tín hiệu, một câu hỏi** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **Debugging vòng lặp (loop / 루프)** để kiểm tra nhận định bằng tiêu chí hoặc phép thử. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Ba tín hiệu, một câu hỏi

- **Logs**: sự kiện có ngữ cảnh, yêu cầu (request / 요청) ID, actor/tenant đã redact.
- **Metrics**: xu hướng và tỷ lệ (rate, error, duration, saturation).
- **Traces**: quan hệ nhân quả giữa yêu cầu (request / 요청) và phụ thuộc (dependency / 의존성) spans.

Khả năng quan sát (observability / 관측 가능성) không phải bật thật nhiều log. Cần chọn tín hiệu (signal / 신호) phân biệt các giả
thuyết: độ trễ (latency / 지연 시간) tăng ở hàng đợi (queue / 큐) hay cơ sở dữ liệu (database / 데이터베이스), lỗi theo tenant hay toàn hệ thống,
chỉ hết thời gian chờ (timeout / 타임아웃) hay đã lần ghi nhận (commit / 커밋).

> **Chuyển mạch:** Ba tín hiệu chỉ hữu ích khi chúng trả lời được một symptom cụ thể. **Debugging vòng lặp (loop / 루프)** dùng logs, metrics và traces để khoanh boundary đầu tiên bị phá; sau đó **Độ tin cậy (reliability / 신뢰성) signals** chuyển bằng chứng ấy thành tín hiệu vận hành.

## Debugging vòng lặp (loop / 루프)

1. Viết symptom có mốc thời gian, phạm vi (scope / 범위) và expected hành vi (behavior / 동작).
2. Đặt vài giả thuyết có thể bác bỏ.
3. Tìm bằng chứng (evidence / 증거) từ dấu vết (trace / 추적), log, chỉ số (metric / 지표), DB trạng thái (state / 상태) và deploy/thay đổi (change / 변경) lịch sử (history / 이력).
4. Khoanh ranh giới (boundary / 경계) đầu tiên nơi bất biến (invariant / 불변식) bị phá.
5. Mitigate an toàn, rồi tạo reproduction và fix lâu dài.

Correlation ID cần truyền qua HTTP, job và message; ngữ cảnh dấu vết (trace context / 추적 컨텍스트) không nên bị
drop ở adapter. chỉ số (metric / 지표) label không được chứa người dùng (user / 사용자) ID/card number vô hạn cardinality.
Log structured, có severity và sampling; redact secret trước khi serialize.

> **Chuyển mạch:** Sau khi khoanh symptom và boundary, reliability signals cho biết sự cố có lan rộng và có hành động nào sẵn sàng hay không. **Đào sâu: từ telemetry đến nhân quả (causal / 인과적) đồ thị (graph / 그래프)** nối các tín hiệu thành chuỗi nguyên nhân thay vì xem dashboard rời rạc.

## Độ tin cậy (reliability / 신뢰성) signals

Theo dõi availability, độ trễ (latency / 지연 시간) percentile, lỗi (error / 오류) lớp (class / 클래스), saturation, hàng đợi (queue / 큐) age,
DB pool và bộ nhớ đệm (cache / 캐시) hit/stale. Dashboard phải nối symptom với đơn vị sở hữu (owner / 오너) và runbook;
alert một chỉ số (metric / 지표) không có hành động thường tạo noise.

Khi sự cố (incident / 인시던트), tách mitigation (rollback, rate limit, disable feature, drain
queue) khỏi root-cause fix. Ghi rõ điều gì đã biết, điều gì chưa biết và bằng chứng (evidence / 증거)
nào làm thay đổi quyết định.

Nền fault tolerance và khả năng quan sát (observability / 관측 가능성) sâu hơn nằm ở [Security & Reliability](../../computer_science/07_security_reliability/README.md).

> **Chuyển mạch:** Causal graph đặt deploy, saturation, latency, timeout và duplicate work trên cùng một đường đi. **Bài tập suy luận** kiểm tra khả năng đọc đường đi đó bằng một p99 tăng nhưng error rate chưa tăng.

## Đào sâu: từ telemetry đến nhân quả (causal / 인과적) đồ thị (graph / 그래프)

Telemetry có giá trị khi nối được nhân quả:

```text
deploy/config change
  → pool saturation / queue age
  → dependency latency
  → request timeout
  → retry / duplicate work
  → user-visible error
```

Dấu vết (trace / 추적) span nên có thao tác (operation / 연산) name, peer, status, hết thời gian chờ (timeout / 타임아웃)/deadline và thử lại (retry / 재시도)
attempt; không đưa payload nhạy cảm vào span. Log mỗi sự kiện (event / 이벤트) một lần ở tầng (layer / 계층) có
ngữ cảnh (context / 맥락) tốt nhất, tránh log cùng exception ở mọi tầng (layer / 계층) rồi làm sai tỷ lệ.

Label `user_id`, yêu cầu (request / 요청) ID hoặc raw URL có thể làm chỉ số (metric / 지표) backend nổ
cardinality. Đưa chúng vào dấu vết (trace / 추적)/log; chỉ số (metric / 지표) dùng tuyến (route / 경로) template, status lớp (class / 클래스) và
bounded dimensions. Tail sampling nên giữ dấu vết (trace / 추적) lỗi, độ trễ (latency / 지연 시간) cao và một mẫu
success để so sánh.

Mitigation môi trường vận hành (production / 운영 환경) phải có quay lui (rollback / 롤백)/expiry/kiểm tra (audit / 감사): disable tính năng (feature / 기능), giảm
traffic, pause bên tiêu thụ (consumer / 소비자), tăng sức chứa (capacity / 용량) hoặc chuyển read-only. Không sửa dữ liệu
trực tiếp chỉ để dashboard “xanh”.

> **Chuyển mạch:** Bài tập p99 buộc chọn metric/span có giá trị chẩn đoán trước khi timeout xuất hiện. **Health, SLO và privacy-safe telemetry** tiếp tục bằng cách biến chẩn đoán thành probe, budget và dữ liệu được phép lưu.

## Bài tập suy luận

Một endpoint p99 tăng từ 200 ms lên 2 s nhưng lỗi (error / 오류) tỷ lệ (rate / 비율) chưa tăng. Chọn ba
chỉ số (metric / 지표)/span cần xem trước, phân biệt queueing với cơ sở dữ liệu (database / 데이터베이스) độ trễ (latency / 지연 시간), và nêu alert
nào nên kích hoạt trước khi người dùng gặp hết thời gian chờ (timeout / 타임아웃).

> **Chuyển mạch:** Probe, SLO và privacy classification biến kết quả debugging thành điều kiện vận hành có thể kiểm tra. Phần này khép mạch bằng cách nối health/readiness với user-visible outcome và retention có mục đích.

## Health, SLO và privacy-safe telemetry

`liveness` trả lời tiến trình (process / 프로세스) còn tiến triển không; `readiness` trả lời instance có
nên nhận traffic; `startup` dành cho initialization dài. Readiness không nên
check mọi phụ thuộc (dependency / 의존성) ở mỗi probe rồi tạo thundering herd. Khi drain, đánh dấu
not-ready trước, ngừng nhận công việc (work / 작업) mới, hoàn tất hoặc trả lease công việc (work / 작업) đang chạy,
rồi shutdown trong grace period có giới hạn.

SLO nên gắn với user-visible kết quả (outcome / 결과): availability, độ trễ (latency / 지연 시간) theo tuyến (route / 경로)/lớp (class / 클래스),
job completion hoặc freshness. lỗi (error / 오류) ngân sách (budget / 예산) dùng để quyết định bản phát hành (release / 릴리스)/quay lui (rollback / 롤백),
không phải chỉ là dashboard. Alert cần symptom, đơn vị sở hữu (owner / 오너), cửa sổ (window / 윈도우) và hành động; alert
chỉ vì CPU cao có thể bỏ sót độ trễ (latency / 지연 시간) do khóa (lock / 잠금) hoặc phụ thuộc (dependency / 의존성).

Telemetry phải có dữ liệu (data / 데이터) classification. Không dùng raw email, đơn vị từ (token / 토큰), cookie,
yêu cầu (request / 요청) body hay full truy vấn (query / 쿼리) làm label/log mặc định. Dùng allowlist trường dữ liệu (field / 필드), redaction
trước serialize, retention theo purpose và truy cập (access / 접근) kiểm tra (audit / 감사) cho log/traces.

> **Bàn giao:** Giữ lại debugging loop, causal telemetry, SLO và privacy classification; quay về [README](./README.md) khi cần nối sang testing, retry hoặc security reliability.
