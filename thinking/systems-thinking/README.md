# Systems Thinking — Nhìn quan hệ, feedback và delay thay vì chỉ nhìn từng phần

Tư duy hệ thống (systems thinking / 시스템 사고) hỏi cách nhiều thành phần tương tác theo thời gian. Nó hữu ích khi linear intuition thất bại vì feedback loops, delays, bottlenecks, adaptation hoặc emergent behavior.

## 1. Stock và flow

**Stock** là thứ tích lũy tại một thời điểm; **flow** là tốc độ làm stock tăng/giảm.

Ví dụ:

```text
Cash balance = stock
Income / spending per month = flows

Backlog = stock
Incoming / completed tasks per day = flows
```

Nhầm stock với flow tạo nhiều reasoning errors: revenue cao không đồng nghĩa cash reserve cao; hiring rate cao không đồng nghĩa headcount lập tức tăng tương ứng.

## 2. Feedback loops

### Reinforcing loop

Một change tự khuếch đại: network effects, compounding, bank run, viral growth.

### Balancing loop

System chống lại change: thermostat, price response, capacity constraints, homeostasis.

Cùng một intervention có thể đi qua cả hai loop.

## 3. Delay

Cause và effect thường cách nhau về thời gian. Nếu actor phản ứng trước khi effect cũ xuất hiện, system có thể oscillate hoặc overcorrect.

Ví dụ inventory ordering, monetary policy, hiring/training và distributed-system autoscaling đều có delay.

## 4. Bottleneck

System throughput thường bị giới hạn bởi constraint hẹp nhất. Tối ưu phần không phải bottleneck có thể làm local metric đẹp hơn mà không tăng global output.

Hỏi:

```text
Where does work queue?
What resource is saturated?
If this constraint doubles, what becomes the next constraint?
```

## 5. Second-order effects

First-order: intervention tác động trực tiếp gì?

Second-order: actor và system phản ứng lại intervention như thế nào?

Ví dụ incentive tăng sales có thể tăng sales ngắn hạn nhưng cũng tăng low-quality customers, support load và churn. Đây là điểm nối trực tiếp sang [Incentives](../incentives/README.md).

## 6. Local optimization vs global outcome

Mỗi team tối ưu KPI riêng có thể làm toàn system tệ đi. Queue, handoff và externality thường nằm ở boundary giữa components.

Systems thinking vì vậy không chỉ vẽ diagram; nó cần measurement và causal evidence để biết loop nào thật sự mạnh.

## 7. Practical mapping

Khi gặp system phức tạp:

1. xác định boundary;
2. list stocks/flows;
3. identify actors và incentives;
4. vẽ reinforcing/balancing loops;
5. đánh dấu delays;
6. tìm bottleneck;
7. tìm common-cause failure;
8. hỏi intervention tạo adaptation nào;
9. chọn metric ở system level;
10. test với data.

## Connections

- [Biology](../../biology/README.md): homeostasis, ecology, systems biology.
- [Economics](../../economics/README.md): equilibrium, markets, feedback và policy response.
- [Sociology](../../sociology/README.md): institutions, networks and collective behavior.
- [Computer Science](../../computer_science/README.md): distributed systems, queues, feedback control.
- [Data Engineering](../../data_engineering/README.md): pipeline bottlenecks, backpressure, capacity.
- [Incentives](../incentives/README.md) và [Game Theory](../game-theory/README.md): adaptive actors inside systems.