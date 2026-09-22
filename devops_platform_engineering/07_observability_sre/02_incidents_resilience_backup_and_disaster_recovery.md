# Incident, resilience, backup và disaster recovery

## 1. Incident response tối ưu recovery trước root cause

Trong sự cố có user impact, hai mục tiêu khác nhau: phục hồi service và hiểu nguyên nhân gốc. Chúng có thể trùng nhưng không luôn trùng. Restart, failover hoặc disable feature có thể phục hồi nhanh nhưng không giải thích root cause.

Incident process tốt tách vai trò và thời gian. Stabilize trước; preserve evidence khi có thể; rồi investigation sâu sau khi impact giảm.

## 2. Severity dựa trên impact

Severity nên phản ánh phạm vi user/business, mức mất dữ liệu, security impact và thời gian, không phản ánh “bug có vẻ khó”. Database CPU 100% mà user không bị ảnh hưởng có thể chưa là incident lớn; payment double-charge dù traffic nhỏ có thể rất nghiêm trọng.

Rule rõ giúp escalation nhất quán.

## 3. Incident command giảm coordination chaos

Khi nhiều người cùng sửa production, nguy cơ action conflict tăng. Incident commander điều phối priority/decision; người vận hành thực hiện; communication role cập nhật stakeholder. Team nhỏ có thể gộp role nhưng vẫn cần một owner quyết định rõ.

Timeline phải ghi event và action: alert lúc nào, deploy nào trước đó, action gì đã làm, metric phản ứng ra sao. Timeline sau này là dữ liệu cho postmortem.

## 4. Mitigation có thể tăng blast radius

Trong incident, “scale mọi thứ lên” hoặc “restart toàn bộ” dễ làm mất evidence và gây thundering herd. Action nên có hypothesis, expected outcome và rollback.

Ví dụ connection pool exhaustion do DB chậm: tăng replicas app có thể tăng tổng connection và làm DB tệ hơn. Mitigation hợp lý có thể là giảm concurrency, shed load hoặc disable expensive path.

## 5. Runbook phải là decision support

Runbook tốt không chỉ ghi lệnh. Nó nêu symptom, điều kiện áp dụng, evidence cần kiểm tra, action, expected result, nguy cơ và cách undo. Lệnh copy-paste không có context có thể nguy hiểm hơn không có runbook.

Runbook nên được test trong game day/incident thật và cập nhật khi assumption đổi.

## 6. Postmortem tìm cơ chế, không tìm người để quy lỗi

“Engineer chạy nhầm command” là mô tả trigger, chưa phải root cause đủ sâu. Hỏi vì sao một command có blast radius lớn, vì sao review/guardrail thiếu, vì sao production credential cho phép, vì sao signal không cảnh báo sớm.

Blameless không nghĩa không có accountability. Ownership vẫn rõ, nhưng analysis tập trung hệ thống để failure tương tự khó tái diễn.

## 7. Action item phải thay đổi hệ thống

Action “cẩn thận hơn” gần như không tạo control mới. Action tốt có owner và deadline, ví dụ thêm policy ngăn wildcard permission, thêm canary check, tự động expire certificate hoặc test restore hàng quý.

Không nên tạo hàng chục action low-value sau mỗi incident. Ưu tiên thay đổi giảm xác suất hoặc blast radius của failure class quan trọng.

## 8. Resilience khác redundancy

Thêm replica tăng redundancy nhưng resilience còn gồm detection, failover, degradation, recovery và learning. Ba replica cùng zone không chịu được zone failure. Multi-zone nhưng cùng database single point vẫn chưa đủ.

Hãy vẽ failure domain: process, pod, node, rack/zone, region, control plane, identity provider, DNS, registry, CI và human operation. Availability end-to-end bị chi phối bởi dependency graph.

## 9. Backup không phải recovery

Có file backup chưa chứng minh khôi phục được. Backup có thể corrupt, thiếu key giải mã, không chứa transaction log cần thiết hoặc restore mất quá lâu so với mục tiêu.

Recovery test phải thực sự tạo environment, restore data, chạy consistency/business validation và đo thời gian.

## 10. RPO và RTO

Recovery Point Objective (RPO) trả lời chấp nhận mất bao nhiêu dữ liệu theo thời gian. Recovery Time Objective (RTO) trả lời chấp nhận mất capability bao lâu.

Hai mục tiêu dẫn tới architecture khác nhau. RPO gần zero có thể cần synchronous/continuous replication và transaction semantics mạnh. RTO vài phút cần automation/failover khác RTO một ngày.

Không nên chọn RPO/RTO theo mong muốn kỹ thuật; business impact phải quyết định.

## 11. Replication không thay backup

Replication sao chép cả thay đổi tốt và xấu. Nếu user delete data hoặc ransomware/corruption propagate, replica có thể hỏng giống primary. Backup point-in-time độc lập tạo recovery option khác.

Ngược lại, backup mỗi ngày không cung cấp failover nhanh. Resilience thường cần cả replication và backup với mục tiêu khác nhau.

## 12. Disaster recovery và control plane dependency

DR plan phải xét cả dependency ngoài application: DNS, IAM, KMS/key, artifact registry, secret store, network, IaC state và CI/CD. Nếu restore database ở region B nhưng encryption key/identity policy chỉ tồn tại region A, data vẫn vô dụng.

Một lỗi phổ biến là DR document giả định tool dùng để restore vẫn khả dụng trong thảm họa. Cần kiểm tra bootstrap path.

## 13. Game day và chaos experiment

Chaos engineering có giá trị khi kiểm tra hypothesis cụ thể về resilience, không phải phá production ngẫu nhiên. Ví dụ: “mất một node không làm SLO checkout vi phạm quá X phút”. Experiment cần steady-state metric, blast radius giới hạn, stop condition và rollback.

Bắt đầu staging/lab không có nghĩa đủ; production có traffic/data/dependency khác. Nhưng production experiment phải có maturity và guardrail tương ứng.

## 14. Senior note: phục hồi là một product capability

Backup, failover và incident process không nên là tài liệu tồn tại riêng. Chúng là capability cần version, test, ownership và telemetry. Nếu recovery chỉ được thử khi disaster thật xảy ra, đó không phải plan mà là hy vọng.

Một platform trưởng thành biến recovery path thành workflow lặp lại: snapshot/backup tự động, restore drill, environment bootstrap bằng code, access khẩn cấp được audit và communication template sẵn.

## 15. MTTR nên được phân rã để biết đang tối ưu phần nào

Một con số MTTR tổng hợp có thể che nhiều vấn đề khác nhau. Có thể tách timeline thành detection, triage/understanding, mitigation, repair và verification. Hai incident cùng mất 60 phút nhưng một cái mất 50 phút mới phát hiện, cái kia phát hiện ngay nhưng rollback không chạy được, cần cải tiến hoàn toàn khác nhau.

Một decomposition thực dụng:

```text
failure begins
→ detected
→ acknowledged / triaged
→ mitigation starts
→ user impact recovered
→ permanent repair
→ learning/action closed
```

Không nhất thiết mọi tổ chức phải dùng cùng tên metric. Điều quan trọng là timestamp có semantics rõ để tránh “MTTR giảm” chỉ vì đổi cách bắt đầu/kết thúc đồng hồ.

## 16. Backup consistency có nhiều mức

Snapshot storage không tự động bảo đảm application-consistent state. Với database đang ghi, snapshot crash-consistent có thể tương đương mất điện đột ngột: engine phải dựa WAL/journal/recovery khi restore. Một số hệ thống cần quiesce, checkpoint hoặc coordination giữa nhiều volume/component để tạo backup nhất quán.

Nếu application có nhiều datastore, restore mỗi datastore về thời điểm khác nhau còn có thể vi phạm business invariant dù từng database riêng lẻ đều hợp lệ. Ví dụ order state ở DB A đã commit nhưng payment event ở store B restore về trước đó.

Backup design vì vậy phải xác định consistency boundary, không chỉ “snapshot đã success”. Database internals sâu hơn giữ ở canonical Data & Databases; DevOps cần bảo đảm restore workflow hiểu application contract.

## 17. Point-in-time recovery cần cả base backup và log chain usable

Point-in-time recovery thường dựa trên một base snapshot/backup cộng chuỗi log/transaction change tới mốc cần phục hồi. Có backup full nhưng thiếu một đoạn log hoặc key giải mã có thể làm recovery tới thời điểm mục tiêu bất khả thi.

Restore drill nên kiểm tra chain end-to-end, không chỉ list file tồn tại. RPO thực tế được quyết định bởi log shipping/retention và mốc gần nhất có thể phục hồi thành công, không phải con số trong policy document.

## 18. DR bootstrap phải được xem như dependency closure

Khi region chính mất, recovery environment cần một tập tối thiểu dependency để có thể tự dựng phần còn lại. Nếu IaC state backend, DNS admin, KMS key, identity provider và artifact registry đều chỉ truy cập được từ region đã mất, automation DR có thể không khởi động.

Hãy vẽ bootstrap graph và hỏi component nào cần tồn tại trước để tạo component sau. Một số control-plane asset cần replication/cross-region access độc lập với application data. Recovery plan tốt biết **thứ tự khởi động** chứ không chỉ danh sách resource.

## 19. Failover cũng là một distributed-state change

Chuyển traffic sang replica/region mới cần đảm bảo writer ownership. Nếu old primary chưa chắc đã chết mà new primary được mở write không có fencing, split brain có thể xuất hiện. Đây là lý do lease/fencing/consensus là canonical dependency quan trọng cho HA.

Ở DevOps layer, runbook phải biết failure detector có uncertainty và thao tác promote/failback có condition nào. “Không ping được primary nên promote ngay” có thể nguy hiểm nếu network partition chỉ tách operator khỏi primary nhưng primary vẫn phục vụ một phần traffic.

## 20. Failback thường khó hơn failover

Sau khi chạy ở DR region nhiều giờ, data/state mới đã sinh ở nơi dự phòng. Chuyển ngược không phải chỉ đổi DNS về. Cần đồng bộ data direction, bảo đảm old primary đã catch up hoặc rebuild, kiểm tra version/config drift và staged traffic return.

Một DR plan chỉ mô tả failover mà không có failback/reconciliation để lại hệ thống ở trạng thái tạm kéo dài và tăng risk cho incident tiếp theo.

## 21. Chaos experiment cần phân biệt hypothesis failure với experiment failure

Nếu experiment inject network loss nhưng tool inject chỉ vào một subset khác dự kiến, kết quả không chứng minh system resilient. Experiment phải verify fault thực sự xảy ra, steady-state signal được đo đúng và stop condition hoạt động.

Ví dụ hypothesis “mất một zone checkout vẫn đạt SLO”. Experiment cần chứng minh workload/traffic của zone thật sự unavailable, không phải scheduler vô tình chưa đặt replica ở zone đó. Sau đó mới đọc SLO/user impact.

## 22. Senior walkthrough: backup hàng ngày nhưng RTO vẫn không đạt

Giả sử backup database 500 GB chạy mỗi ngày thành công. Disaster thật cần restore sang region khác; tải backup mất 2 giờ, replay log 90 phút, provisioning network/secret thêm 45 phút, validation 30 phút. Tổng recovery hơn 4 giờ trong khi RTO business là 60 phút.

Backup success rate 100% không giải quyết mismatch này. Kiến trúc cần thay đổi: warm standby, snapshot locality, pre-provisioned capacity, faster restore path hoặc điều chỉnh RTO nếu cost không hợp lý.

Đây là ví dụ vì sao RTO là end-to-end capability metric, không phải thuộc tính của một backup job.