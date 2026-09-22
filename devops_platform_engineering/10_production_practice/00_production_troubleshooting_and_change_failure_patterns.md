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

## 18. Latency phải tách queue time và service time

Một request chậm không có nghĩa code xử lý business logic chậm. Tổng latency có thể gồm chờ connection pool, chờ thread/executor, chờ queue, thời gian CPU thực thi, GC pause, network và downstream.

Nếu application trace chỉ đo từ lúc handler bắt đầu, thời gian request nằm chờ trước handler có thể biến mất khỏi trace. Vì vậy cần đặt instrumentation ở boundary phù hợp và so client-observed latency với server span. Khoảng chênh là clue cho proxy/network/queue/scheduling.

Một hệ thống saturation thường biểu hiện service time chưa tăng nhiều nhưng queue time tăng mạnh. Scale đúng bottleneck hoặc shed load sẽ giảm queue; tối ưu code handler trong trường hợp đó có thể không chạm nguyên nhân chính.

## 19. Coordinated omission có thể làm load test nói dối

Nếu load generator gửi request tiếp theo chỉ sau khi request trước hoàn thành, khi service chậm nó tự động giảm arrival rate. Kết quả latency nhìn “đỡ xấu” đúng lúc production thật sẽ tiếp tục nhận traffic và queue tăng.

Load test cần mô phỏng arrival pattern thực tế đủ tốt và ghi nhận request đáng lẽ đã đến trong thời gian service stall. Nếu không, throughput/latency benchmark có thể bỏ sót saturation cliff.

Điều cần nhớ không phải một tool benchmark cụ thể, mà là assumption của workload generator: closed-loop hay open-loop, concurrency cố định hay arrival rate cố định, data/cache có đại diện production không.

## 20. Failure case: rollout tạo burst 502 dù Pod không crash

Giả sử mỗi rollout xuất hiện 502 trong 3–5 giây. Pod cũ nhận `SIGTERM` và đóng listener gần như ngay lập tức. Tuy nhiên endpoint/load-balancer propagation mất vài giây nên một phần request vẫn route tới Pod đang shutdown.

Evidence: 502 tập trung đúng termination timestamp, process exit code bình thường, không OOM, Pod mới Ready, application log Pod cũ có shutdown event ngay trước connection reset. Đây không phải “Kubernetes không stable”; là termination/data-plane race.

Mitigation có thể gồm readiness/draining choreography và graceful shutdown để Pod ngừng nhận traffic trước khi listener biến mất, đồng thời giữ grace period đủ cho in-flight request. Sau fix cần canary rollout và quan sát 5xx theo pod/version/termination event.

## 21. Failure case: Java heap chỉ 60% nhưng container bị OOMKilled

Giả sử dashboard JVM cho heap 1,2 GiB trên max heap 2 GiB, trong khi Pod memory limit là 2 GiB và vẫn bị OOMKilled. Heap metric không bao gồm mọi memory: metaspace, thread stack, direct buffer, native library, mmap/page cache accounting tùy context và runtime overhead đều có thể góp vào cgroup usage.

Evidence chain cần nối `lastState/exit`, cgroup/container memory metric, node event và JVM native/heap telemetry. Nếu cgroup usage chạm 2 GiB nhưng heap không chạm max, nguyên nhân là total process/container footprint vượt boundary, không phải heap OOM.

Fix có thể là giảm heap target để chừa native headroom, sửa direct-buffer/thread leak hoặc tăng limit sau capacity review. Chỉ đặt `-Xmx` bằng đúng container limit là một anti-pattern vì giả định heap là toàn bộ memory.

## 22. Failure case: scale application làm outage database nặng hơn

Traffic tăng làm latency app tăng. Team scale từ 20 lên 100 replica. Mỗi replica có pool tối đa 50 connection nên theoretical connection demand tăng từ 1.000 lên 5.000, trong khi DB chỉ chịu khoảng 1.500 concurrent connection hữu ích. DB bắt đầu queue/lock/context overhead, latency tăng thêm và retry khuếch đại load.

Evidence tốt là app replica count tăng trước DB connection saturation; throughput business không tăng tương ứng; pool wait/query latency và outbound retry tăng. Root cause không phải “thiếu replica”, mà là bottleneck downstream và thiếu connection/concurrency budget end-to-end.

Mitigation có thể giới hạn app concurrency/pool, shed load, giảm retry và scale DB nếu có headroom. Long-term fix là capacity model nối autoscaling application với downstream budget.

## 23. Failure case: config store đúng nhưng process vẫn dùng config cũ

ConfigMap/secret manager cho thấy value mới, nhưng một số instance vẫn behavior cũ. Có thể process chỉ đọc config lúc startup, volume sync có delay, reload hook fail hoặc connection đã mở bằng credential cũ.

Troubleshooting phải xác định **effective config** của từng process/version, không dừng ở source of truth. Nếu chỉ instance chưa restart lỗi, hypothesis mạnh là lifecycle/reload. Nếu tất cả instance nhận file mới nhưng behavior không đổi, xem application reload semantics.

Platform nên expose config revision trong telemetry/status để operator nối runtime behavior với exact config, giống artifact version.

## 24. Evidence matrix giúp điều tra song song mà không hỗn loạn

Trong incident lớn, thay vì năm người cùng mở log, có thể chia hypothesis theo layer với expected evidence. Ví dụ một người kiểm tra change/version, một người dependency/DB, một người node/resource, một người traffic edge. Mỗi nhánh phải trả về kết luận có thể bác bỏ: “không thấy version correlation”, “DB pool wait tăng từ 10 ms lên 900 ms”, không phải “DB có vẻ ổn”.

Incident commander sau đó cập nhật hypothesis tree. Cách này tận dụng parallelism mà vẫn tránh action conflict.

## 25. Mitigation thành công không chứng minh root cause

Restart làm service khỏe lại có thể do xóa leaked state, reset connection, di chuyển Pod sang node khác hoặc đơn giản trùng lúc dependency hồi phục. “Restart fixed it” là observation, chưa phải explanation.

Sau recovery, cần hỏi state nào đã bị reset và evidence nào phân biệt hypothesis. Nếu không còn evidence, postmortem nên ghi uncertainty và thêm instrumentation để lần sau phân biệt, thay vì gán root cause giả chắc chắn.

## 26. Production debugging nên kết thúc bằng cải thiện hệ thống

Mỗi incident có ba loại output tiềm năng: fix defect trực tiếp, tăng khả năng phát hiện/chẩn đoán, và giảm blast radius/recovery time. Ví dụ một memory leak cần code fix; thiếu cgroup metric cần observability fix; rollout ồ ạt cần delivery guardrail.

Nếu chỉ sửa defect mà không cải thiện signal hoặc safety khi failure class có thể tái diễn, learning loop chưa đóng. Troubleshooting là input cho Platform Engineering: failure lặp lại ở nhiều team nên được biến thành default, guardrail hoặc self-service diagnostic capability.

## 27. Counterfactual tốt hơn narrative sau sự cố

Sau incident rất dễ kể một câu chuyện mượt: “deploy X làm latency tăng nên X là nguyên nhân”. Causal confidence mạnh hơn khi có counterfactual: cohort không nhận X có khỏe không; rollback X có đảo signal trong cùng traffic/dependency không; một zone/version tương đương có behavior khác không.

Canary, version dimension, tenant cohort và region split tạo natural experiment. Chúng không chứng minh tuyệt đối nhưng giúp phân biệt correlation với mechanism.

Khi không có counterfactual, postmortem nên nói rõ evidence level. Một hypothesis có timeline phù hợp nhưng chưa được reproduce khác với root cause đã được isolation/reproduction xác nhận.

## 28. Nhiều feedback loop có thể tạo oscillation dù từng loop “đúng”

Production hiện đại có HPA, cluster autoscaler, retry, circuit breaker, load balancer health check, queue autoscaler và GitOps/controller cùng phản ứng với signal. Nếu response time và gain không được phối hợp, chúng có thể đẩy hệ thống qua lại.

Ví dụ latency tăng → HPA scale app → DB connection tăng → DB chậm hơn → retry tăng → latency tăng thêm. Sau đó circuit breaker mở → load giảm → HPA scale down; breaker đóng → traffic dồn lại và chu kỳ lặp.

Khi metric dao động tuần hoàn, đừng chỉ debug component riêng. Hãy vẽ loop: **signal nào kích action nào, delay bao lâu, action thay resource/load gì, loop khác quan sát signal gì**. Oscillation thường là property của interaction, không phải một controller đơn độc.

## 29. Client timeout không có nghĩa server đã dừng work

Một request timeout ở client/proxy có thể vẫn tiếp tục chạy trong server hoặc downstream nếu cancellation không propagate. Client retry sau timeout có thể tạo hai operation đồng thời. Với write không idempotent, đây là đường tới duplicate side effect.

Evidence cần so client timeout timestamp với server trace và downstream operation. Nếu server hoàn thành sau khi client đã bỏ, latency/error dashboard phía client và server có thể kể hai câu chuyện khác nhau.

Deadline propagation, cancellation và idempotency key là reliability mechanism. Troubleshooting phải hỏi “work đã bị hủy thật chưa?” thay vì đồng nhất timeout với failure kết thúc.

## 30. Partial failure nên được cắt theo cohort trước khi nhìn global average

Một incident có thể chỉ ảnh hưởng node image mới, AZ cụ thể, tenant tier, certificate chain cũ, IPv6 path, browser version hoặc shard dữ liệu. Global error 2% có thể là 100% failure của một cohort nhỏ.

Dimension hữu ích nhất thường là dimension gần failure boundary: version, zone, node pool, target dependency, config revision, identity principal, shard/partition. High-cardinality không có nghĩa phải index mọi thứ vô hạn; cần chọn dimension có khả năng phân biệt hypothesis.

Câu hỏi senior là: **những request fail có điểm chung nào mà request thành công không có?** Đây thường là đường ngắn nhất tới isolation boundary.

## 31. Recovery storm là một failure phase riêng

Khi dependency hoặc control plane hồi phục, hệ thống chưa chắc ổn ngay. Backlog, retry queue, reconnect, cache miss, image pull, leader election và pod restart có thể đồng loạt tạo load lớn hơn steady state trước outage.

Nếu operator thấy dependency “đã xanh” nhưng latency tiếp tục xấu, hãy kiểm tra recovery workload: queue age đang drain ra sao, reconnect rate, cache hit, DB connection churn, controller backlog và node provisioning.

Recovery cần throttling/ramp-up giống startup. Mở toàn bộ traffic ngay khi health check xanh có thể tạo second outage.

## 32. Brownout cần được phân biệt với silent data-quality failure

Graceful degradation có chủ đích có thể trả stale cache, bỏ recommendation hoặc defer non-critical work. Nhưng nếu telemetry chỉ nhìn HTTP 200, brownout và business correctness failure có thể bị che.

Degradation mode phải có explicit signal: feature disabled, data freshness, fallback ratio, stale age hoặc quality tier. SLO có thể cho core availability xanh trong khi product quality giảm; dashboard phải cho operator biết đây là intentional degraded mode hay unknown failure.

Troubleshooting không nên “fix” brownout ngay nếu nó đang bảo vệ core flow. Trước hết xác nhận trigger, protected invariant và điều kiện thoát mode.

## 33. Clock và event ordering có thể làm timeline đánh lừa

Log từ nhiều host/service có thể lệch clock, batch trước khi ship hoặc ghi timestamp ở thời điểm khác nhau. Trace span cũng có sampling/clock assumption. Vì vậy thứ tự hiển thị không luôn bằng causal order tuyệt đối.

Khi vài giây quyết định hypothesis, ưu tiên correlation ID/trace parent, sequence/version, deployment event từ source of truth và monotonic duration trong cùng process hơn việc so raw wall-clock timestamp giữa host.

NTP/clock health vẫn quan trọng, nhưng incident analysis nên biết uncertainty của timeline thay vì suy luận causality từ chênh 200 ms không đáng tin.

## 34. Negative evidence có giá trị nếu biết detector đáng tin tới đâu

“Không có log error” chỉ loại trừ hypothesis nếu code path chắc chắn phải log và log pipeline không mất dữ liệu. “Không thấy CPU cao” chỉ hữu ích nếu metric resolution bắt được spike và đúng cgroup/node. Absence of evidence không tự động là evidence of absence.

Mỗi signal có detection boundary: sampling, retention, scrape interval, dropped log, missing label hoặc instrumentation gap. Senior debugging luôn hỏi **nếu hypothesis đúng, detector này có chắc nhìn thấy không?**

Khi detector yếu, kết luận đúng là “chưa quan sát được”, không phải “đã loại trừ”. Điều này giúp hypothesis tree trung thực hơn và thường chỉ ra observability debt cần sửa sau incident.

## 35. Causal graph tốt hơn một timeline phẳng khi nhiều yếu tố tương tác

Timeline chỉ nói sự kiện nào xảy ra trước sau. Causal graph cố gắng biểu diễn dependency: traffic tăng làm queue tăng; queue tăng làm latency tăng; timeout làm retry tăng; retry lại làm traffic downstream tăng. Một node có thể vừa là hậu quả của cause trước vừa trở thành cause của failure tiếp theo.

Khi incident phức tạp, hãy vẽ arrow “A có thể làm B bằng mechanism nào?” thay vì chỉ liệt kê timestamp. Nếu không mô tả được mechanism nối hai event, correlation cần được giữ ở mức hypothesis.

Causal graph cũng giúp phân biệt trigger, amplifier và latent condition. Bad deploy có thể là trigger, retry policy là amplifier, còn thiếu admission control là điều kiện khiến blast radius lớn.

## 36. Intervention tạo evidence mạnh nhưng đồng thời làm system thay đổi

Rollback, scale, disable feature hoặc restart vừa là mitigation vừa là experiment. Nếu rollback làm error giảm, confidence vào change tăng — nhưng traffic, cache, dependency hoặc autoscaler cũng có thể đổi cùng lúc.

Một intervention hữu ích nên thay ít biến nhất có thể trong giới hạn incident safety và ghi rõ expected effect. Khi có thể, dùng cohort nhỏ/canary thay vì toàn fleet để giữ comparison group. Khi user impact buộc phải hành động mạnh, ưu tiên recovery nhưng đừng overclaim causal certainty sau đó.

Production không phải laboratory sạch. Discipline nằm ở việc biết intervention nào đã phá counterfactual nào.

## 37. Incident state-change discipline ngăn operator tự tạo race

Trong incident lớn, nhiều người cùng scale, patch config, restart và rollback có thể làm actual state thay đổi nhanh hơn khả năng quan sát. Evidence thu ở phút 10 có thể không còn mô tả state sau action phút 11.

Nên có một owner cho mutation path hoặc ít nhất serialized log: action nào, target/revision nào, ai thực hiện, expected effect, timestamp và rollback condition. Read-only investigation có thể parallel; state mutation cần coordination mạnh hơn.

Điều này đặc biệt quan trọng với controller/GitOps: manual patch có thể bị reconcile ngược, tạo cảm giác system “tự thay đổi” trong khi hai actor đang tranh ownership.

## 38. Detector coverage nên được xem như bản đồ, không phải danh sách dashboard

Một organization thường biết rõ các failure đã instrument nhưng ít biết vùng mù. Có thể lập coverage map theo failure class: edge reachability, business correctness, dependency latency, resource pressure, data freshness, queue age, control-plane convergence và security authorization.

Với mỗi class, hỏi sensor nằm ở đâu, sampling/freshness ra sao, failure nào sensor không nhìn thấy và signal mất thì có được phát hiện không. Coverage map không cần hoàn hảo; mục tiêu là biết “unknown unknown” nào đang hoàn toàn phụ thuộc complaint của user.

Incident mới phát hiện vùng mù nên tạo observability action cụ thể, không chỉ thêm dashboard chung chung.

## 39. Fault injection chỉ tạo evidence nếu experiment có control và verification

Inject 500 ms network delay rồi thấy latency tăng không dạy nhiều nếu không xác nhận delay thật sự đi vào path nào, cohort nào bị ảnh hưởng và control cohort nào không bị inject.

Một experiment tốt định nghĩa hypothesis, fault boundary, steady-state metric, stop condition, control/comparison group và evidence chứng minh injection đã hoạt động. Nếu tool báo “fault injected” nhưng packet path thực không qua target đó, kết luận resilience là vô nghĩa.

Fault injection có giá trị nhất khi kiểm tra một invariant cụ thể, ví dụ “mất một replica không làm checkout burn budget > X”, không phải khi chỉ cố tạo chaos cho giống production.

## 40. Senior walkthrough: restart giúp ngay nhưng root cause vẫn chưa rõ

Giả sử service latency tăng dần, restart toàn replica làm latency trở lại bình thường. Có ít nhất vài hypothesis: memory/cache leak, connection pool state xấu, thread starvation, DNS/connection refresh hoặc workload được reschedule khỏi node lỗi.

Restart đã reset nhiều state cùng lúc nên intervention có độ phân giải thấp. Sau incident, hãy tìm cohort/process evidence còn giữ được, thử targeted restart hoặc reproduction trong environment kiểm soát, và bổ sung metric cho state nghi ngờ.

Kết luận trưởng thành là: **restart chứng minh failure phụ thuộc một state đã bị reset, nhưng chưa xác định state nào**. Giữ uncertainty chính xác tốt hơn gán nhãn “memory leak” chỉ vì restart có hiệu quả.