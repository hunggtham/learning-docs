# SLI, SLO, error budget và capacity: reliability có mục tiêu

## 1. Reliability không thể chỉ là “càng cao càng tốt”

Nếu mục tiêu mơ hồ là 100% uptime, mọi thay đổi đều có thể bị coi là nguy hiểm và cost sẽ tăng vô hạn. SRE đưa reliability về bài toán có contract đo được: service nào quan trọng, user nhìn thấy behavior nào, mức không hoàn hảo nào chấp nhận được và trong cửa sổ nào.

## 2. SLI phải gần user experience

Chỉ báo mức dịch vụ (Service Level Indicator — SLI) là phép đo. Ví dụ availability SLI không nên đơn giản là process uptime; process sống nhưng trả 500 vẫn không phục vụ user.

Một request-based SLI có thể là:

```text
good events / valid events
```

“Good” phải định nghĩa theo contract: status code, latency threshold và loại request. Một số 4xx do client sai có thể không tính là service failure; một số business response HTTP 200 nhưng nội dung thất bại vẫn phải tính xấu.

## 3. SLO là mục tiêu trong cửa sổ

Mục tiêu mức dịch vụ (Service Level Objective — SLO) nói SLI cần đạt bao nhiêu trong khoảng thời gian. Ví dụ 99.9% request hợp lệ thành công trong 30 ngày.

99.9% không phải “chỉ khác 99% một chút”. Error budget giảm khoảng mười lần. Vì vậy số SLO phải gắn với user/business need, architecture và cost.

## 4. Error budget biến reliability thành constraint cho change

Nếu SLO là 99.9%, phần 0.1% còn lại là error budget. Budget không phải quota để cố tình gây lỗi; nó là ngôn ngữ cân bằng innovation và stability.

Khi service tiêu budget nhanh, team có evidence để ưu tiên reliability work hoặc giảm change risk. Khi budget còn nhiều, không nên dùng “sợ downtime” làm lý do chặn mọi cải tiến.

## 5. Burn rate tốt hơn alert theo snapshot

Alert “error rate > 1% 5 phút” không tự hiểu SLO. Burn rate hỏi service đang tiêu error budget nhanh hơn tốc độ cho phép bao nhiêu lần. Kết hợp cửa sổ ngắn và dài giúp bắt outage lớn nhanh nhưng giảm noise do spike nhỏ.

Mental model là: nếu tiếp tục với tốc độ lỗi hiện tại, budget sẽ hết khi nào.

## 6. Latency SLO cần distribution

Average latency che tail. User thường cảm nhận p95/p99 hoặc threshold-based good event. Một SLI “99% request dưới 500 ms” trực tiếp hơn average 200 ms nếu 1% request treo 20 giây.

Tuy nhiên percentile aggregation giữa service/window có caveat; histogram bucket và event-based SLI thường dễ reasoning hơn khi xây SLO pipeline.

## 7. Dependency và composite SLO

Một service phụ thuộc DB, cache và payment provider. Availability end-to-end không thể cao tùy ý nếu dependency yếu và không có redundancy/degradation.

SLO architecture phải hỏi dependency failure nào có thể degrade gracefully. Ví dụ recommendation service down có thể bỏ recommendation thay vì fail checkout. Đây là design decision, không phải monitoring config.

## 8. Capacity là ability giữ SLO dưới load

Capacity planning không phải dự báo chính xác tương lai. Nó là giữ đủ headroom để demand variation, node failure và rollout không đẩy hệ thống qua saturation cliff.

Ba khái niệm cần tách: utilization cho biết resource đang dùng bao nhiêu; saturation cho biết demand đang chờ; throughput cho biết hệ thống hoàn thành bao nhiêu work. Khi utilization gần 100%, latency thường tăng phi tuyến do queueing.

## 9. Autoscaling không thay thế capacity planning

Autoscaler có delay và có thể scale đúng resource nhưng bottleneck nằm ở dependency khác. Thêm application replicas có thể làm database connection storm nặng hơn.

Capacity model cần tìm bottleneck chain: ingress, app CPU/memory, connection pool, DB, queue consumer, external API. Load test phải tái tạo traffic shape và data behavior đủ thực tế.

## 10. Resource request là capacity reservation

Trong Kubernetes, request ảnh hưởng scheduling. Tổng request là một cách biểu diễn demand reserved trên cluster. Nếu team cố hạ request để “tiết kiệm”, scheduler có thể overpack và reliability giảm.

FinOps tốt không tối ưu con số bill độc lập; nó tối ưu cost trên mỗi capability/SLO với headroom hợp lý.

## 11. Queueing và backpressure

Khi arrival rate vượt service rate, queue tăng. Queue giúp hấp thụ burst nhưng không tạo capacity. Nếu backlog tăng lâu, latency theo queue age tăng và cuối cùng hệ thống phải reject/drop/degrade.

Backpressure truyền tín hiệu ngược để producer giảm tốc. Nếu không có, upstream có thể tiếp tục đẩy work vào downstream đã saturation.

## 12. Load shedding và graceful degradation

Khi không thể phục vụ tất cả, chọn bỏ work ít quan trọng có kiểm soát tốt hơn để toàn hệ thống collapse. Rate limit, admission control, queue limit và priority là các cơ chế.

Ví dụ checkout giữ core operation nhưng tắt recommendation/analytics sync. Đây là reliability architecture được quyết định trước incident.

## 13. SLO cho platform

Platform team cũng có user là developer/product team. SLI có thể gồm time-to-create service, pipeline availability, deployment success signal, environment provisioning latency hoặc support response cho critical path.

Không nên chọn vanity metric như “số cluster được quản”. Platform SLO phải phản ánh user journey.

## 14. Senior note: reliability là budget allocation

CPU headroom, replica, multi-zone, test time, review effort và engineering attention đều là budget. SLO cung cấp objective để phân bổ chúng. Nếu service vượt xa SLO với cost cao, có thể đang over-engineer. Nếu budget luôn cháy, architecture/change process có debt.

SRE trưởng thành không phải làm mọi service cực kỳ redundant; nó làm mức reliability **có chủ đích, đo được và phù hợp giá trị**.

## 15. Worked example: 99.9% thực sự cho phép bao nhiêu failure

Với SLO time-based 99.9% trong 30 ngày, tổng cửa sổ có 43.200 phút. Phần 0,1% tương ứng khoảng 43,2 phút không đáp ứng SLO. Con số này chỉ đúng nếu SLI thực sự là time-based availability; request-based SLI phải tính theo event.

Nếu có 1.000.000 request hợp lệ trong cửa sổ và SLO là 99.9% good events, error budget là 1.000 bad events. Một outage 5 phút ở giờ thấp điểm và một outage 5 phút ở giờ cao điểm có thể tiêu budget request-based rất khác nhau. Đây là lý do phải định nghĩa SLI trước rồi mới diễn giải “bao nhiêu downtime”.

## 16. Burn rate là tốc độ tiêu budget tương đối

Giả sử SLO cho phép bad-event ratio 0,1%. Nếu trong một window service đang có 1% bad event, nó đang burn nhanh khoảng 10 lần tốc độ bền vững. Nếu giữ nguyên, error budget của cả cửa sổ dài sẽ bị tiêu nhanh hơn nhiều so với thiết kế.

Burn rate giúp thống nhất severity theo SLO. Một spike 5% kéo dài vài phút có thể đáng page ngay vì burn cực nhanh; 0,12% kéo dài ngắn có thể chưa cần đánh thức người trực nếu budget/window còn khỏe. Alert policy thực tế thường kết hợp nhiều window để vừa nhạy với outage lớn vừa tránh noise.

Điều quan trọng không phải thuộc một bộ threshold cố định, mà hiểu ratio:

```text
burn rate = observed bad-event rate / allowed bad-event rate
```

## 17. Little's Law nối queue với latency

Trong một hệ thống ổn định, Little's Law cho một mental model rất mạnh:

```text
L = λ × W
```

`L` là lượng work trung bình đang ở trong hệ thống, `λ` là throughput/arrival rate trung bình, `W` là thời gian trung bình một work item ở trong hệ thống. Đây không phải công thức để dự đoán mọi spike, mà là sanity check cho queue/capacity.

Ví dụ service xử lý trung bình 100 request/s và mỗi request ở trong system 0,2 giây thì concurrency trung bình xấp xỉ 20. Nếu latency tăng lên 1 giây trong khi throughput tương tự, số request in-flight trung bình tăng lên khoảng 100. Connection pool, thread pool và memory pressure có thể tăng theo dù traffic không đổi.

Đây là lý do latency degradation tự nó có thể tạo thêm resource pressure.

## 18. Khi arrival rate lớn hơn service rate, backlog tăng theo thời gian

Nếu producer đưa vào `λ` work/giây nhưng consumer chỉ xử lý `μ` work/giây và `λ > μ`, queue sẽ tăng gần theo chênh lệch `λ - μ` trong giai đoạn đó. Autoscaling chỉ cứu được nếu cuối cùng làm `μ` vượt `λ` trước khi queue age vi phạm SLO hoặc storage/TTL bị chạm.

Ví dụ queue nhận 1.200 message/s nhưng consumer chỉ hoàn thành 1.000 message/s. Backlog tăng khoảng 200 message mỗi giây. Sau 10 phút đã có khoảng 120.000 message tích thêm, chưa tính traffic biến động. “Queue vẫn hoạt động” không có nghĩa system healthy; message age mới phản ánh user delay.

## 19. Retry cần một budget riêng

Retry làm arrival rate mà downstream nhìn thấy lớn hơn user traffic. Nếu mỗi request có tối đa ba attempt, outage downstream có thể khiến request rate thực tế tiến gần nhiều lần traffic gốc. Nhiều layer cùng retry — SDK, service mesh, load balancer, application — còn có thể nhân lên mạnh hơn.

Một reliability design tốt xác định retry budget: operation nào retry được, tổng deadline, attempt tối đa, backoff/jitter và layer nào sở hữu retry. Khi downstream saturation, load shedding/circuit breaking có thể quan trọng hơn cố tăng success bằng retry.

## 20. Dependency budget phải được phân bổ có chủ đích

Một checkout service có SLO 99.9% nhưng gọi tuần tự nhiều dependency critical thì end-to-end reliability chịu ảnh hưởng của tất cả dependency. Không thể chỉ đặt cho mỗi dependency cùng 99.9% rồi kỳ vọng composition vẫn đạt 99.9%.

Có ba cách xử lý chính: dependency phải mạnh hơn SLO end-to-end; system thêm redundancy/fallback/cache; hoặc flow được thiết kế để dependency không critical, ví dụ recommendation fail thì checkout vẫn tiếp tục.

Đây là nơi SLO trở thành input cho architecture. SLO không phải dashboard decoration; nó quyết định chỗ nào cần redundancy, chỗ nào có thể degrade và chỗ nào cost thêm không tạo giá trị.

## 21. Capacity test phải đo saturation cliff, không chỉ peak throughput

Một load test chỉ hỏi “tối đa bao nhiêu request/s” dễ bỏ qua behavior khi vượt ngưỡng. Điều quan trọng hơn là khi load tăng, latency, error, queue, GC, connection pool và downstream pressure thay đổi theo curve nào; khi load giảm lại system có hồi phục hay không.

Một service có thể đạt 5.000 request/s trong test ngắn nhưng sau vài phút connection queue tích tụ, tail latency tăng và retry đẩy database vào collapse. Capacity usable phải là vùng hệ thống giữ SLO ổn định với headroom cho rollout/failure, không phải con số throughput lớn nhất từng thấy.