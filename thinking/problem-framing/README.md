# Problem Framing — Đặt đúng bài toán trước khi giải

Problem framing (định khung vấn đề / 문제 프레이밍) là bước xác định **ta đang cố hiểu, giải thích hay thay đổi điều gì** trước khi chọn dữ liệu, mô hình hoặc giải pháp. Một lời giải chính xác cho một câu hỏi sai vẫn là một quyết định tệ; một optimization rất tốt trên sai objective thậm chí có thể làm hệ thống tệ hơn nhanh hơn.

Chapter này không sở hữu logic, measurement hay optimization theory. Logic sâu nằm ở [Philosophy](../../philosophy/README.md), research question và operationalization nằm ở [Research Methods](../../research_methods/README.md), optimization formal nằm ở [Mathematics](../../mathematics/README.md). Vai trò của `thinking/` là biến các nền tảng đó thành một workflow dùng được trước debugging, project planning, research, business analysis hay quyết định cá nhân.

Mental model cốt lõi là:

```text
observation / complaint / request
→ actor + desired outcome
→ current state + gap
→ scope + constraints
→ measurable signals
→ plausible frames / causes / options
→ evidence that distinguishes them
→ only then choose action
```

## 1. Symptom, problem và cause là ba lớp khác nhau

Một symptom là điều quan sát được. Problem là khoảng cách giữa trạng thái hiện tại và trạng thái mong muốn. Cause là cơ chế tạo ra hoặc duy trì khoảng cách đó. Ba lớp thường bị trộn thành một câu.

Ví dụ:

```text
Symptom:
website chậm

Possible problem statements:
checkout P95 latency > target trong giờ cao điểm
mobile users bỏ trang trước khi payment page render
batch job chiếm connection pool và ảnh hưởng request online

Possible causes:
query chậm
lock contention
asset quá lớn
third-party API
GC pressure
network path
```

“Website chậm” chưa phải diagnosis và cũng chưa đủ để chọn solution. Nếu nhảy thẳng từ symptom sang “thêm server”, ta đang biến một hypothesis thành problem definition.

Điểm cần giữ lại là: **observation cho biết nơi cần điều tra, không tự xác định cause hoặc action**. Từ đây cần viết problem statement có cấu trúc để biết chính xác gap nào đang được giải.

## 2. Một problem statement tốt phải nói rõ ai, trạng thái nào và khoảng cách nào

Một format thực dụng:

```text
Actor / stakeholder:
ai đang chịu outcome?

Current state:
điều gì đang xảy ra?

Desired state:
trạng thái nào được coi là tốt hơn?

Gap:
khác biệt giữa current và desired nằm ở đâu?

Constraint:
những giới hạn nào không thể bỏ qua?

Metric / evidence:
làm sao biết gap đã giảm?

Scope:
phần nào thuộc và không thuộc bài toán?

Time horizon:
đang tối ưu hôm nay, quý này hay nhiều năm?
```

Ví dụ “cải thiện việc học” quá rộng. Một frame tốt hơn có thể là:

```text
Actor: người học
Current: đọc nhiều nhưng recall sau 7 ngày thấp
Desired: recall và apply được core concepts sau 7 ngày
Constraint: 60 phút/ngày
Metric: delayed retrieval score + application task
Scope: một môn cụ thể trong 6 tuần
```

Format không phải bureaucratic template. Nó buộc ta expose những điều thường bị ẩn: **ai là người hưởng lợi, outcome nào thật sự quan trọng và horizon nào đang được tối ưu**.

## 3. Outcome phải được operationalize trước khi metric trở thành target

Các từ như “quality”, “productivity”, “engagement”, “understanding”, “reliability” hoặc “health” quá rộng để đo trực tiếp nếu chưa nói rõ chúng có nghĩa gì trong context.

Operationalization là chuyển concept thành observation hoặc measurement có thể dùng được. Nhưng một measurement vẫn chỉ là representation của outcome.

Ví dụ:

```text
Goal: học hiểu
Possible measures:
- delayed recall
- explain in own words
- solve transfer problem
- detect misconception

Weak proxy if used alone:
- số giờ ngồi học
- số trang đã đọc
```

Hoặc:

```text
Goal: software reliability
Possible measures:
- availability
- error rate
- recovery time
- failed transaction rate

Weak proxy if used alone:
- số test cases
```

Không có metric hoàn hảo. Câu hỏi đúng là:

```text
Metric này capture phần nào của outcome?
Phần nào nó bỏ sót?
Nếu metric trở thành target, behavior nào có thể game nó?
```

Khi proxy trở thành target, incentives có thể làm quan hệ proxy–outcome suy yếu. Đây là nơi frame nối sang [Incentives](../incentives/README.md) và [Systems Thinking](../systems-thinking/README.md).

## 4. Constraint khác objective, và resource khác bottleneck

Một frame thường hỏng vì mọi giới hạn đều được gọi là “vấn đề”. Hãy tách:

```text
Objective:
điều muốn tối đa/minimize

Constraint:
điều không được vi phạm hoặc khó thay đổi

Resource:
input có thể tăng/giảm

Bottleneck:
constraint hiện đang giới hạn throughput/outcome mạnh nhất
```

Ví dụ team có thể “thiếu developer”, nhưng bottleneck thực là review queue, environment approval hoặc requirement churn. Tăng developer gấp đôi có thể chỉ làm queue lớn hơn.

Một sanity question hữu ích:

> Nếu tăng resource X lên gấp đôi mà outcome gần như không đổi, X có thật là bottleneck hiện tại không?

Bottleneck cũng có thể di chuyển. Sau khi giải DB latency, bottleneck chuyển sang third-party API. Vì vậy framing không phải một lần làm rồi đóng; nó phải được update khi system state thay đổi.

## 5. Decomposition tốt tạo ra điểm đo hoặc điểm can thiệp

Một vấn đề lớn nên được phân rã thành các phần có causal, functional hoặc accounting meaning.

Ví dụ:

```text
Revenue
= number of active customers
× purchase frequency
× average order value
```

Hoặc latency:

```text
end-to-end latency
= client/network
+ edge/proxy
+ application
+ database
+ external dependency
```

Decomposition tốt giúp hỏi “component nào đóng góp nhiều nhất?” hoặc “can thiệp nào thay đổi component này?”. Decomposition tệ chỉ đổi tên vấn đề thành nhiều bullet không có quan hệ.

Có ba test nhanh:

1. Các phần có giải thích hoặc reconstruct được whole không?
2. Mỗi phần có thể quan sát hoặc kiểm tra riêng không?
3. Một intervention vào phần đó có thể thay outcome theo mechanism hợp lý không?

Nếu không, decomposition có thể chỉ là taxonomy trang trí.

## 6. Luôn tạo ít nhất hai competing frames khi stakes đủ lớn

Một frame duy nhất dễ biến assumption thành fact. Khi vấn đề material, thử viết ít nhất hai cách giải thích hoặc hai cách đặt mục tiêu.

Ví dụ sales giảm:

```text
Frame A: acquisition problem
traffic/lead volume giảm

Frame B: conversion problem
traffic ổn nhưng checkout/conversion giảm

Frame C: retention problem
new sales ổn nhưng repeat purchase giảm
```

Mỗi frame dẫn đến evidence và action khác nhau. Thay vì tranh luận bằng narrative, hỏi:

```text
Evidence nào nếu xuất hiện sẽ làm Frame A mạnh hơn B?
Evidence nào sẽ falsify frame hiện tại?
```

Đây là cầu nối tự nhiên sang [Argument & Evidence Mapping](../practice/06_argument_and_evidence_mapping.md) và [Causal Reasoning](../causal-reasoning/README.md).

## 7. Scope phải được vẽ để tránh giải một hệ thống vô hạn

Không có scope, một problem có thể expand mãi:

```text
slow query
→ schema
→ application design
→ architecture
→ team process
→ company incentives
→ industry regulation
```

Các layer trên có thể đều liên quan, nhưng decision hiện tại không nhất thiết cần giải tất cả.

Một scope boundary tốt nói rõ:

```text
In scope:
những layer có thể quan sát/can thiệp trong horizon này

Out of scope:
những layer được giữ cố định cho decision hiện tại

Escalation trigger:
evidence nào khiến phải mở rộng scope
```

Scope không có nghĩa phủ nhận system context. Nó là cách giữ analysis tractable và định nghĩa lúc nào phải mở frame.

## 8. Perspective thay đổi frame, nhưng không phải perspective nào cũng ngang nhau

Cùng một system có thể có nhiều stakeholder:

```text
customer
operator
employee
shareholder
regulator
supplier
```

Ví dụ một policy giảm waiting time cho customer nhưng tăng workload cho staff; một architecture giảm developer friction nhưng tăng operational complexity.

Khi stakeholder conflict tồn tại, problem statement nên nói rõ:

```text
whose outcome?
whose cost?
which constraint?
```

Điều này không biến mọi value judgment thành technical problem. Nó chỉ ngăn việc giấu distributional trade-off trong một metric duy nhất.

## 9. Reframing dùng để kiểm tra objective, không phải brainstorming vô hạn

Một cách reframe mạnh là hỏi mục tiêu phía sau action hiện tại.

Thay vì:

> “Làm sao làm X nhanh hơn?”

hãy thử:

```text
Tại sao cần X?
Outcome phía sau X là gì?
Có cách đạt outcome mà không cần X không?
Nếu bỏ X, constraint nào xuất hiện?
Điều gì phải đúng để X không còn là bottleneck?
```

Ví dụ “cần automate report này” có thể reframe thành “stakeholder cần signal nào để ra quyết định?”. Có khi solution tốt là xóa report, đổi metric hoặc event-triggered alert chứ không automate file hiện tại.

Reframing chỉ tốt khi vẫn giữ objective và constraints quan trọng. Đổi câu hỏi tới mức tránh problem thật không phải creativity mà là evasion.

## 10. Solution-first framing là một failure mode đặc biệt nguy hiểm

Các câu sau là solution statement:

```text
chúng ta cần AI
chúng ta cần microservices
cần tuyển thêm người
cần mua cổ phiếu X
cần migrate database
```

Chuyển chúng về dạng:

```text
Problem / outcome
→ evidence current state
→ constraints
→ plausible options
→ selection criteria
→ information needed
→ solution
```

Một solution có thể đúng, nhưng nó phải sống sót sau khi competing alternatives được tạo. Nếu solution được cố định từ đầu, analysis sau đó dễ trở thành justification exercise.

## 11. Nested problem: không phải mọi subproblem đều đáng giải

Một large problem tạo ra nhiều subproblem. Nhưng subproblem chỉ đáng ưu tiên nếu nó materially ảnh hưởng objective hoặc information value.

Có thể dùng ba câu:

```text
Nếu subproblem này được giải hoàn toàn, outcome chính thay đổi bao nhiêu?
Nếu bỏ qua nó, downside lớn nhất là gì?
Có evidence rẻ nào để biết nó có đáng đào sâu không?
```

Đây là nơi framing nối với [Value of Information](../value-of-information/README.md): không phải uncertainty nào cũng đáng research như nhau.

## 12. Một frame tốt phải chứa update trigger

Problem frame không nên trở thành doctrine. Hãy ghi trước evidence nào sẽ khiến ta đổi frame.

Ví dụ:

```text
Current frame:
DB contention là bottleneck chính.

Update trigger:
Nếu DB wait time <10% total latency nhưng P95 vẫn cao,
chuyển investigation sang application/external dependency.
```

Update trigger chống confirmation bias vì ta định nghĩa điều kiện đổi ý **trước** khi xem outcome tiếp theo.

## 13. Reusable problem-framing worksheet

```text
# Problem Frame

Observation / trigger:
Actor / stakeholder:
Current state:
Desired state:
Gap:
Time horizon:

Outcome:
Operational measure(s):
What the measure misses:

Constraints:
Resources:
Current bottleneck hypothesis:

In scope:
Out of scope:
Escalation trigger:

Competing frames / explanations:
A.
B.
C.

Evidence available:
Evidence that would distinguish frames:

Options already assumed too early:

Current best frame:
Confidence:
What would change the frame:
```

Worksheet không cần dùng đầy đủ cho việc nhỏ. Complexity của framing nên tăng theo stakes, uncertainty và irreversibility.

## 14. Common failure modes

### Symptom = cause

“CPU cao nên CPU là root cause” có thể sai; CPU cao cũng có thể là consequence.

### Proxy = outcome

Tối ưu page views, ticket count, study hours hoặc test count trong khi outcome thực không cải thiện.

### Constraint inflation

Mọi preference được gọi là constraint, làm option space nhỏ giả tạo.

### Scope creep

Mở rộng từ local issue thành “sửa toàn hệ thống” mà không có evidence cần thiết.

### Frame lock-in

Giữ frame ban đầu dù evidence mới không còn phù hợp.

### Solution laundering

Viết lại solution mong muốn dưới dạng problem để tạo cảm giác objective.

### Over-framing

Dành nhiều thời gian định nghĩa problem hơn giá trị của decision. Việc reversible/low-stakes chỉ cần lightweight frame.

## 15. Stop condition — khi nào đủ để chuyển sang analysis/action?

Một frame đủ tốt khi:

- actor và desired outcome rõ;
- current state/gap đủ observable;
- metric không bị nhầm là toàn bộ outcome;
- constraints và scope đã explicit;
- bottleneck chỉ được coi là hypothesis nếu chưa có evidence;
- có ít nhất hai plausible explanations hoặc options khi stakes đủ lớn;
- biết evidence nào có thể phân biệt chúng;
- có update trigger nếu frame sai;
- chi phí framing thêm đã lớn hơn information value thu được.

Sau điểm này, tiếp tục polishing câu chữ không làm decision tốt hơn. Hãy chuyển sang [Causal Reasoning](../causal-reasoning/README.md), [Model Selection](../model-selection/README.md), [Value of Information](../value-of-information/README.md) hoặc [Decision Making](../decision-making/README.md) tùy loại câu hỏi.

## Connections

- [Critical Thinking](../critical-thinking/README.md): kiểm tra claim sau khi câu hỏi đã được frame.
- [Argument & Evidence Mapping](../practice/06_argument_and_evidence_mapping.md): giữ competing frames, assumptions và evidence inspectable.
- [Causal Reasoning](../causal-reasoning/README.md): phân biệt symptom, mechanism và cause.
- [Model Selection](../model-selection/README.md): chọn lens sau khi objective và question type rõ.
- [Decision Making](../decision-making/README.md): chuyển frame thành options, thresholds và action.
- [Systems Thinking](../systems-thinking/README.md): mở frame khi feedback, delay và nhiều actor materially ảnh hưởng outcome.
- [Value of Information](../value-of-information/README.md): quyết định uncertainty nào đáng research.
- [PMP](../../pmp/README.md): scope, constraints, stakeholders và project objectives.
- [Computer Science](../../computer_science/README.md): requirements, debugging và system decomposition.

Điểm chốt của Problem Framing không phải “viết problem statement đẹp”. Nó là **giữ observation, objective, measurement, cause hypothesis và solution ở đúng layer**, để evidence có thể thay đổi frame trước khi ta khóa vào một action.