# Production troubleshooting: từ symptom đến evidence xuyên tầng

## 1. Troubleshooting là bài toán giảm không gian giả thuyết

Production system có nhiều layer nên đoán tool-first rất tốn thời gian. Quy trình tốt bắt đầu bằng symptom cụ thể, time window và scope rồi dùng evidence để loại trừ từng lớp.

Hỏi trước: ai bị ảnh hưởng; tất cả request hay một region/tenant; bắt đầu lúc nào; có thay đổi gần đó không; failure là error, latency, stale data hay capacity.

## 2. Chuỗi layer chuẩn

Một đường suy luận thực dụng:

```text
user symptom
→ edge/DNS/TLS
→ routing/load balancer
→ service endpoint
→ pod/process/runtime
→ node/kernel resources
→ downstream dependency
→ data/consistency
→ recent change/control plane
```

Không phải incident nào đi hết chuỗi. Mục tiêu là tìm layer đầu tiên nơi expected state khác actual state.

## 3. Change correlation không bằng causation

Deployment ngay trước incident là suspect mạnh nhưng chưa phải chứng minh. Có thể traffic spike, dependency outage hoặc certificate expiry trùng thời điểm.

Dùng version dimension/canary comparison để tăng confidence. Nếu chỉ pod version mới lỗi còn cũ khỏe cùng node/traffic, evidence mạnh hơn chỉ nhìn timestamp.

## 4. Golden signals trước, detail sau

Bắt đầu traffic/rate, error, latency và saturation phù hợp service. Sau đó drill down dimension: version, zone, endpoint, dependency. Không mở 20 dashboard cùng lúc.

Nếu error tăng nhưng latency không tăng, có thể validation/config nhanh fail. Nếu latency tăng trước error, có thể saturation/dependency timeout. Pattern thời gian giúp định hướng.

## 5. CPU incident

CPU cao có thể là traffic tăng, hot loop, GC, encryption/compression hoặc retry storm. CPU thấp vẫn có latency nếu throttled quota, I/O wait hoặc downstream.

Kiểm tra demand và throughput trước khi scale. Nếu throughput không tăng cùng CPU, code/path có thể kém hiệu quả. Nếu scale app làm DB pressure tăng, cần tìm bottleneck thật.

## 6. Memory incident

Memory tăng tuyến tính theo thời gian gợi leak/cache không bound; jump sau deploy gợi changed footprint; OOM theo load peak gợi capacity/limit.

Trong container, phân biệt runtime heap và cgroup memory. OOM event/exit evidence quan trọng hơn giả định “Java heap còn thấp nên không thể OOM”.

## 7. Network/timeout incident

Tách DNS → TCP → TLS → HTTP. `timeout` có thể ở connect hoặc read. Proxy và application có timeout riêng. Trace cho biết hop nào chiếm thời gian.

Retry storm thường làm đồ thị request outbound tăng nhanh hơn inbound. Đây là dấu hiệu amplification.

## 8. Kubernetes Pending/CrashLoop/NotReady

`Pending`: scheduler/storage/constraint. `ImagePullBackOff`: registry/name/auth/network. `CrashLoopBackOff`: process start rồi thoát lặp; xem exit/log/config. `NotReady`: process chạy nhưng readiness contract fail. OOMKilled: memory boundary/evidence.

Tên status là entry point, không phải root cause.

## 9. Database dependency

App latency tăng có thể do connection pool exhausted, slow query, lock contention hoặc DB resource saturation. Connection pool wait time khác query execution time. Nếu pool wait cao nhưng query latency bình thường, có thể pool size/concurrency/leak.

Scale app replicas làm tổng pool lớn hơn nên phải tính DB max connections toàn hệ thống.

## 10. Queue/backlog

Queue depth tăng vì producer nhanh hơn consumer hoặc consumer chậm/fail. Depth một mình không đủ; message age cho biết user delay. Nếu autoscale consumer nhưng downstream DB bottleneck, throughput có thể không tăng.

Poison message có thể làm consumer retry cùng item; cần dead-letter/idempotency strategy theo domain.

## 11. Config/secret failure

Config change có thể không tạo deployment event nếu chỉnh ngoài pipeline. Vì vậy config revision cần telemetry. Secret rotation failure thường biểu hiện partial: instance restart mới dùng credential mới, instance cũ vẫn dùng old; khi old revoked mới bắt đầu fail.

Luôn xác định effective config trong process, không chỉ object/config store.

## 12. Certificate expiry

Cert incident có timestamp rất rõ nhưng có thể chỉ ảnh hưởng một client trust store hoặc hostname. Kiểm tra chain, SAN, expiry và trust path. Alert expiry phải đủ sớm để rotation có thời gian, nhưng test rotation mới là control mạnh hơn alert.

## 13. Disk incident

Disk usage 100% có thể làm DB/log agent/app fail dây chuyền. Kiểm tra block, inode, deleted-open files và volume class. Cleanup emergency phải tránh xóa evidence/data cần recovery.

## 14. Control plane vs data plane

Kubernetes API hoặc cloud API lỗi không luôn nghĩa application traffic down. Ngược lại data plane có thể lỗi dù control plane báo resource Healthy.

Xác định layer trước action. Repeated deploy trong control-plane outage có thể tích queue thay đổi và gây burst khi hồi phục.

## 15. Recovery action phải có expected effect

Trước restart/scale/rollback, nói rõ: giả thuyết gì, metric nào sẽ đổi nếu đúng, bao lâu đánh giá, cách undo. Trong incident nhanh có thể viết ngắn nhưng vẫn giữ discipline.

Điều này ngăn nhiều người làm action đối nghịch và giúp timeline có ý nghĩa.

## 16. Preserve evidence và reproducibility

Nếu phải restart để recover, capture log/event/core/thread dump khi feasible. Sau đó tái tạo failure trong staging/load test từ artifact/config tương ứng.

Không phải incident nào tìm được single root cause. Có thể ghi causal factors và uncertainty rõ ràng tốt hơn bịa một “root cause” đơn giản.

## 17. Senior note: troubleshooting giỏi là hiểu boundary

Một operator senior không nhất thiết nhớ nhiều lệnh hơn; họ biết command nào trả lời câu hỏi nào, dữ liệu nằm ở layer nào và khi nào abstraction bị rò.

Platform nên hỗ trợ drill-down từ service catalog → deployment → pod → node → trace/log/metric mà vẫn giữ ownership và version context. Đây là nơi developer experience và incident response gặp nhau.