# Capacity planning, utilization knee và admission control

Capacity planning không phải lấy peak traffic rồi nhân thêm 20%. Một service có thể vẫn còn throughput capacity nhưng latency đã tăng mạnh vì queueing. Vì vậy cần hiểu quan hệ giữa **arrival rate**, **service time**, **concurrency**, **utilization** và tail latency.

## Utilization gần 100% là vùng nguy hiểm

Nếu một resource phục vụ request gần như liên tục, chỉ một burst nhỏ cũng tạo queue vì không còn idle capacity hấp thụ biến động. Khi service time cũng có variance, queue có thể tăng rất nhanh trước khi throughput graph trông “đầy”.

Điểm mà latency bắt đầu cong mạnh thường được gọi không chính thức là **utilization knee**. Operating target nên nằm trước vùng này, đặc biệt với user-facing service.

## Little's Law nối concurrency với latency

Trong stable system:

```text
L = λW
```

`L` là số request trung bình trong system, `λ` là throughput/arrival rate, `W` là thời gian trung bình request ở trong system.

Nếu service xử lý 1,000 requests/s và average end-to-end time là 0.2 s, trung bình khoảng 200 requests đang in-flight. Công thức đơn giản này rất hữu ích để sanity-check connection pool, worker concurrency và queue depth.

## Service time distribution quan trọng hơn average

Nếu 99% request mất 5 ms nhưng 1% mất 1 s, average không mô tả tốt pressure lên worker pool. Slow requests giữ resource lâu, làm request nhanh phía sau phải chờ và có thể tạo head-of-line blocking.

Capacity model vì thế cần percentile, workload mix và dependency latency, không chỉ mean RPS.

## Concurrency limit là một control loop

Tăng thread/connection vô hạn không tăng throughput vô hạn. Sau một mức, contention, cache miss, context switch, database saturation và GC có thể làm service time tăng.

**Concurrency limiting** đặt upper bound số work đang active. Excess work có thể queue có giới hạn hoặc bị reject sớm. Mục tiêu là giữ hệ thống trong vùng hiệu quả thay vì cho overload biến thành collapse.

## Admission control

**Admission control (수락 제어)** quyết định request nào được nhận khi resource khan hiếm. Một request bị từ chối nhanh với `429/503` đôi khi tốt hơn nhận tất cả rồi để mọi request timeout sau 30 giây.

Reject sớm bảo vệ resource cho work đã nhận, giảm queue và giúp caller có signal rõ để backoff/retry.

## Queue phải có giới hạn

Unbounded queue biến overload thành memory growth và latency vô hạn. Bounded queue tạo explicit failure mode: khi queue đầy, system shed load thay vì tích tụ debt không thể trả.

Queue capacity nên liên hệ với latency budget. Nếu mỗi worker xử lý 100 ms mà queue có thể chứa hàng chục nghìn request, nhiều request đã chắc chắn vượt SLO ngay khi được enqueue.

## Headroom cho failure

Capacity bình thường chưa đủ. Nếu cluster có 10 nodes nhưng phải chịu được mất 2 nodes, remaining 8 nodes phải xử lý load trong vùng an toàn. Deployment rolling update, zone failure và autoscaling delay đều tiêu thụ headroom.

N+1/N+2 planning vì thế là reliability requirement, không chỉ cost decision.

## Autoscaling không thay admission control

Autoscaler phản ứng sau khi metric thay đổi và instance mới cần startup/warmup. Burst có thể làm system sụp trước khi scale-out hoàn tất. Admission control và load shedding bảo vệ trong khoảng phản ứng đó.

Scale-to-zero hoặc cold cache còn làm service time ban đầu cao hơn, nên capacity model cần xét transient state.

## Practical workflow

Đo saturation point bằng load test có workload gần production; xác định knee của latency; chọn operating target có headroom; đặt concurrency/queue limit; định nghĩa overload response; kiểm tra behavior khi một phần capacity biến mất.

Capacity planning tốt không tìm “maximum RPS đẹp nhất” mà tìm **safe operating envelope**.

## Mental model

> Capacity là vùng hoạt động an toàn, không phải một con số throughput cực đại. Utilization cao làm queue nhạy với variance; concurrency limit giữ active work trong vùng hiệu quả; admission control biến overload thành failure có kiểm soát thay vì collapse lan truyền.