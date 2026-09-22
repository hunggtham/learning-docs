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