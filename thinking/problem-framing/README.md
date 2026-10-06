# Problem Framing — Đặt đúng bài toán trước khi giải

Problem framing (định khung vấn đề / 문제 프레이밍) là bước xác định **ta đang cố giải quyết điều gì** trước khi chọn dữ liệu, mô hình hay hành động. Một lời giải chính xác cho một câu hỏi sai vẫn là một quyết định tệ.

Trang này là integration layer. Logic sâu nằm ở [Philosophy](../../philosophy/README.md), measurement và research question nằm ở [Research Methods](../../research_methods/README.md), optimization nằm ở [Mathematics](../../mathematics/README.md).

## 1. Tách symptom khỏi problem

Ví dụ:

```text
Symptom: website chậm
Possible problems:
- server latency tăng
- query database chậm
- asset quá lớn
- client render nặng
- network của user kém
```

“Website chậm” chưa phải causal diagnosis. Nó chỉ là observation cần decomposition.

## 2. Viết problem statement có cấu trúc

```text
Actor: ai đang gặp vấn đề?
Current state: hiện tại điều gì đang xảy ra?
Desired state: muốn đạt trạng thái nào?
Gap: khác biệt nằm ở đâu?
Constraint: tiền, thời gian, luật, năng lực, dữ liệu?
Metric: biết đã cải thiện bằng cách nào?
Scope: phần nào thuộc / không thuộc bài toán?
```

Nếu không thể nói rõ desired state và metric, rất dễ tối ưu một proxy không liên quan đến outcome thực.

## 3. Outcome ≠ proxy

Proxy là chỉ số đại diện cho outcome nhưng không phải outcome.

Ví dụ:

```text
Goal: học hiểu
Proxy: số giờ học

Goal: software reliability
Proxy: số test case

Goal: business health
Proxy: traffic
```

Proxy hữu ích nếu quan hệ với outcome đủ mạnh. Khi proxy trở thành target, incentive có thể làm quan hệ đó suy yếu. Handoff sang [Incentives](../incentives/README.md).

## 4. Decompose trước khi optimize

Một vấn đề lớn thường nên tách thành các subproblem có causal hoặc operational meaning.

```text
Revenue
= number of customers
× purchase frequency
× average order value
```

Decomposition tốt tạo ra nơi có thể đo và can thiệp. Decomposition tệ chỉ đổi tên vấn đề thành nhiều từ nhỏ hơn.

## 5. Constraint thật sự là gì?

Không phải mọi resource đều là bottleneck.

Một team có thể thiếu developer nhưng bottleneck thực là review, deployment approval hoặc unclear requirements. Một người có thể nghĩ thiếu thời gian nhưng bottleneck là switching cost và attention.

Hỏi:

> Nếu tăng resource X thêm 2 lần mà outcome gần như không đổi, X có thật là constraint chính không?

## 6. Reframe bằng counterfactual

Thay vì hỏi:

> “Làm sao làm X nhanh hơn?”

hãy thử:

> “Nếu không cần làm X thì sao?”
> “Mục tiêu phía sau X là gì?”
> “Điều gì phải đúng để X không còn là bottleneck?”

Reframing không phải sáng tạo vô hạn; nó phải giữ nguyên objective và constraints quan trọng.

## 7. Avoid solution-first framing

“Chúng ta cần AI”, “cần microservices”, “cần mua cổ phiếu X” đều là solution statement, không phải problem statement.

Đổi thành:

```text
Problem
→ evidence
→ constraints
→ options
→ selection criteria
→ solution
```

## 8. Stop condition

Một problem frame đủ tốt khi:

- outcome và actor rõ;
- metric không đánh tráo outcome;
- constraints chính đã explicit;
- có ít nhất hai plausible explanations hoặc options;
- biết evidence nào sẽ phân biệt chúng;
- biết phần nào đang nằm ngoài scope.

## 9. Operationalize outcome và giữ boundary của model

Một desired state chỉ dùng được khi có cách quan sát hoặc kiểm tra. Hãy tách `construct` (ví dụ “reliability” hoặc “học hiểu”) khỏi indicator/proxy đang dùng để đo nó, rồi ghi điều kiện mà proxy có thể lệch khỏi outcome. Nếu không, ta dễ biến thứ dễ đếm thành thứ cần tối ưu.

Tiếp theo, ghi model boundary: thời gian nào, population nào, actor nào và failure mode nào không được bao phủ. Boundary không làm bài toán yếu đi; nó nói rõ kết luận đang có hiệu lực ở đâu và khi nào phải chuyển sang [Model Selection](../model-selection/README.md) hoặc [Research Methods](../../research_methods/README.md) để chọn cách đo khác.

## 10. Competing frames trước khi chọn giải pháp

Với vấn đề material, viết ít nhất hai frame hợp lý và chỉ ra prediction hoặc action khác nhau của chúng. Ví dụ “website chậm” có thể là capacity problem, dependency problem hoặc user-perception problem; mỗi frame cần evidence phân biệt và owner xử lý khác nhau.

Artifact tối thiểu là một problem brief gồm `outcome → proxy → constraints → boundary → competing frames → discriminating evidence → stop condition`. Khi các frame hội tụ vào cùng một hành động, mới có lý do để chuyển sang [Decision Making](../decision-making/README.md); nếu không, giữ bất định thay vì ép một câu trả lời sớm.

## Connections

- [Critical Thinking](../critical-thinking/README.md): kiểm tra claim sau khi câu hỏi đã được frame.
- [Causal Reasoning](../causal-reasoning/README.md): phân biệt symptom, mechanism và cause.
- [Decision Making](../decision-making/README.md): chuyển frame thành options và action.
- [Systems Thinking](../systems-thinking/README.md): frame vấn đề có feedback và nhiều actor.
- [PMP](../../pmp/README.md): scope, constraints và project objectives.
- [Computer Science](../../computer_science/README.md): debugging, requirements và system decomposition.
