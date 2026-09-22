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