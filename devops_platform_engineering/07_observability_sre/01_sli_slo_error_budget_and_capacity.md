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

## 22. Admission control giữ hệ thống trong vùng có thể phục vụ

Khi một service đã ở gần saturation, nhận thêm mọi request không phải lúc nào cũng tăng useful throughput. Work mới có thể chỉ làm queue dài hơn, timeout nhiều hơn và giữ resource lâu hơn. Admission control đặt một giới hạn trước khi work đi sâu vào hệ thống: concurrent request limit, queue bound, rate limit hoặc per-tenant budget.

Mental model quan trọng là **protect useful work, không maximize accepted work**. Nếu service xử lý ổn định 800 request/s nhưng nhận 1.500 request/s rồi để tất cả chờ 20 giây trước khi timeout, user experience và resource usage đều tệ hơn việc reject nhanh phần vượt khả năng với signal retry rõ.

Admission point nên đặt gần resource khan hiếm mà nó bảo vệ. Limit ở edge có thể bảo vệ toàn service; semaphore ở application có thể bảo vệ thread/connection pool; quota ở downstream bảo vệ database hoặc external API. Một limit quá xa bottleneck có thể không kiểm soát đúng resource pressure.

## 23. Concurrency limit nên dựa trên latency và resource budget, không chỉ CPU

Một service I/O-bound có thể CPU thấp nhưng connection pool hoặc downstream concurrency đã đầy. Vì vậy autoscaling chỉ theo CPU và admission chỉ theo request rate đều có thể miss bottleneck.

Nếu mỗi request giữ một DB connection trung bình 200 ms và DB chỉ dành 400 connection hữu ích cho service, concurrency vượt xa 400 sẽ chủ yếu tạo wait. Giới hạn application concurrency quanh downstream budget thường ổn định hơn việc mở pool vô hạn.

Adaptive concurrency control có thể điều chỉnh limit theo latency/saturation signal, nhưng controller phải phản ứng chậm hơn noise và có floor/ceiling. Nếu limit controller, autoscaler và retry cùng phản ứng mạnh trên cùng signal, hệ thống có thể oscillate.

## 24. Failover capacity phải được reserve trước failure

Một hệ thống chạy bình thường ở 70–80% utilization mỗi zone có thể nhìn “hiệu quả”, nhưng nếu một zone mất và traffic dồn sang phần còn lại, capacity có thể lập tức vượt saturation cliff. Headroom cần được tính theo failure model, không chỉ daily peak.

Ví dụ ba zone mỗi zone phục vụ 1/3 traffic. Nếu thiết kế chịu mất một zone mà vẫn giữ SLO, hai zone còn lại phải hấp thụ khoảng 1,5 lần load bình thường, cộng thêm rollout/autoscaling delay. Capacity target vì vậy thường thấp hơn mức utilization tối đa kỹ thuật.

Điều tương tự áp dụng cho database replica, queue consumer, NAT gateway, external API quota và CI runner. “Có redundancy” nhưng không có **spare capacity under failover** chỉ tạo redundancy hình thức.

## 25. Correlated failure phá assumption độc lập

Nhiều mô hình reliability ngầm giả định replica hoặc zone fail độc lập. Thực tế dependency chung như DNS, identity provider, registry, certificate authority, control plane, shared network hoặc bad rollout có thể làm nhiều replica fail cùng lúc.

Vì vậy redundancy phải hỏi **common-mode dependency nào còn dùng chung**. Hai region cùng dùng một global configuration rollout hoặc cùng một external API chưa chắc tạo independence thực sự.

Load test/failure exercise nên bao gồm correlated event: secret rotation sai toàn fleet, DNS degradation, policy rollout chặn deploy hoặc regional dependency failure. Đây là cách kiểm tra blast radius của shared control plane, không chỉ process crash đơn lẻ.

## 26. Brownout là intentional degradation để bảo vệ core SLO

Trong overload, một service có thể tạm tắt feature không thiết yếu thay vì để toàn request path chậm. Ví dụ bỏ recommendation, giảm image transformation chất lượng cao, defer analytics hoặc trả stale-but-safe cache cho một số read path.

Brownout khác outage ngẫu nhiên ở chỗ degradation được thiết kế trước, observable và reversible. Feature nào được bỏ phải dựa trên business criticality và data correctness; không phải mọi operation đều có thể stale hoặc async.

Một platform tốt cho phép declare priority class hoặc degradation mode đủ rõ để incident response không phải phát minh logic mới giữa lúc hệ thống đang cháy.

## 27. Error budget policy phải điều khiển decision, không chỉ tạo dashboard

Một SLO chỉ có giá trị tổ chức khi budget state thay đổi hành vi. Nếu budget cháy nhưng release cadence, review depth và reliability backlog không thay đổi, SLO chỉ là reporting.

Policy có thể nói khi burn kéo dài thì giảm risky rollout, bắt buộc canary, ưu tiên reliability work hoặc yêu cầu owner review. Nhưng policy không nên cơ học đến mức mọi budget dip nhỏ đều đóng băng delivery; cần phân biệt transient event, known incident và structural unreliability.

Senior SRE xem error budget như **feedback controller cho engineering decision**. Signal phải gần user impact, action phải proportional và sau khi reliability hồi phục, constraint cũng phải được nới lại thay vì trở thành permanent bureaucracy.

## 28. SLO traffic thấp cần semantics khác service nhiều request

Với service xử lý hàng triệu request mỗi giờ, một tỷ lệ bad-event có sample đủ lớn để burn-rate ổn định. Nhưng một admin API chỉ có vài chục request mỗi ngày có thể bị một lỗi duy nhất làm tỷ lệ lỗi nhảy rất mạnh. Alert theo phần trăm lúc này dễ vừa noisy vừa chậm.

Low-traffic SLO nên hỏi user journey thực sự là gì. Có thể synthetic transaction định kỳ phù hợp hơn request ratio; hoặc measurement window cần dài hơn; hoặc cần kết hợp event count tối thiểu trước khi diễn giải một tỷ lệ. Không nên giả định cùng một công thức alert phù hợp cho checkout 50.000 request/s và backup-restore API 20 lần/ngày.

Điểm quan trọng là **mẫu quan sát (sample) quyết định độ ổn định của phép đo**. SLO là contract sản phẩm, nhưng signal dùng để đánh giá contract vẫn chịu giới hạn thống kê.

## 29. Valid-event denominator là một phần của correctness

Trong công thức `good / valid`, denominator quyết định SLO đang nói về population nào. Nếu pipeline vô tình loại request timeout trước khi chúng tới application log, hoặc bỏ tenant/region lỗi vì label missing, SLI có thể đẹp lên chính vì bad event biến mất khỏi denominator.

Do đó cần định nghĩa nơi đo và điều kiện eligibility. Edge/load balancer thường nhìn được cả request không tới application; application nhìn được business outcome sâu hơn. Với critical journey, đôi khi cần kết hợp nhiều sensor để tránh survivorship bias.

Một SLI review tốt không chỉ hỏi “good event là gì?” mà hỏi thêm **event nào có quyền biến mất khỏi phép tính và tại sao**.

## 30. Window semantics thay đổi hành vi của error budget

Rolling window 30 ngày, calendar month và fixed release window không tương đương. Rolling window luôn trượt theo thời gian nên một incident lớn dần rời khỏi window; calendar window reset ở mốc lịch; release window gắn reliability với một cohort/version cụ thể.

Không có một loại window luôn đúng. Rolling window phù hợp vận hành liên tục; calendar window dễ align reporting; cohort/release window hữu ích khi muốn so rollout. Điều quan trọng là policy phải biết window nào đang điều khiển decision, nếu không team có thể thấy “budget hồi phục” chỉ vì đồng hồ reset chứ system chưa đáng tin hơn.

## 31. SLO cho asynchronous work nên đo age và completion semantics

Queue consumer hoặc batch pipeline không có “request latency” giống HTTP. User có thể quan tâm việc message được xử lý trong 5 phút, report hoàn tất trước 08:00 hoặc data freshness không quá 15 phút.

SLI phù hợp có thể là tỷ lệ work item hoàn tất trước deadline hoặc age của oldest valid item. Queue depth đơn thuần không đủ: 100.000 item mới có thể ít nghiêm trọng hơn 1.000 item đã chờ 6 giờ.

Với retry, cần quyết định success sau retry còn là good event không và deadline tính từ attempt đầu hay cuối. Đây là nơi domain semantics phải đi trước metric syntax.

## 32. Composite journey cần phân biệt serial dependency và fallback path

Nếu một user journey bắt buộc đi qua A rồi B rồi C và failure tương đối độc lập, end-to-end success không thể tốt hơn các thành phần và thường thấp hơn từng thành phần riêng. Nhưng nếu B có cache/fallback hoặc C chỉ chạy cho 10% request, cách composition thay đổi.

Vì vậy không nên nhân các số availability một cách máy móc nếu topology có conditional path, retry, quorum hoặc graceful degradation. Trước hết vẽ journey graph: dependency nào mandatory, dependency nào optional, branch nào chiếm bao nhiêu traffic và failure nào được che bởi fallback.

SLO decomposition là bài toán architecture trước khi là bài toán số học.

## 33. Multi-SLI service cần biết trade-off giữa availability, latency và correctness

Một service có thể tăng availability bằng cách trả stale cache, nhưng freshness/correctness giảm. Có thể giữ latency thấp bằng fail-fast, nhưng tỷ lệ request thành công giảm. Vì vậy chỉ một SLO có thể tạo incentive lệch.

Critical capability thường cần một tập nhỏ SLI bổ sung nhau: success/correctness, latency/freshness và đôi khi durability. Các SLI này không nên biến thành dashboard hàng chục mục tiêu; mỗi cái phải đại diện một failure dimension user thực sự quan tâm.

Brownout càng làm điều này rõ: core availability có thể đạt trong khi quality tier đang giảm có chủ đích. Reliability contract phải cho phép nói chính xác **điều gì đang được giữ và điều gì đang được hy sinh**.

## 34. SLO measurement pipeline cũng cần version và audit

Đổi query, bucket, denominator, label mapping hoặc data source có thể làm SLO nhảy mà service behavior không đổi. Đây là change production vì error budget state có thể điều khiển release policy và paging.

Measurement definition nên được versioned/reviewed; khi migration lớn có thể chạy old/new song song để so difference trước khi đổi source of truth. Dashboard nên cho biết SLO definition revision hoặc change event để operator phân biệt reliability regression với measurement change.

Senior reasoning coi SLO pipeline là một control system: **sensor definition sai có thể làm actuator engineering ra quyết định sai**, dù application hoàn toàn không thay đổi.