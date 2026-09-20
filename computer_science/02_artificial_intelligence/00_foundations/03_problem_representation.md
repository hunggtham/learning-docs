# Problem Representation trong AI

Trước khi một AI system có thể search, learn, reason hoặc optimize, problem phải được chuyển thành một **representation (표현 / biểu diễn)** mà máy có thể thao tác. Đây là bước thường bị xem nhẹ vì nó nằm trước algorithm, nhưng representation quyết định rất lớn việc bài toán có dễ giải hay không.

Máy không nhận “ý nghĩa” trực tiếp. Nó nhận bits, numbers, tokens, tensors, graphs hoặc symbolic structures. Vì vậy câu hỏi đầu tiên không phải “model nào mạnh nhất?”, mà là:

> **Ta đang biểu diễn thế giới như thế nào, và representation đó giữ lại hoặc làm mất thông tin gì?**

## Từ real-world problem tới computational problem

Giả sử muốn xây hệ thống tìm đường trong Seoul. Real world gồm đường phố, traffic, one-way road, thời gian, weather, accidents và vô số chi tiết. Không thể đưa “thế giới thật” nguyên trạng vào algorithm. Ta phải chọn abstraction.

Một representation đơn giản:

```text
Intersection → node
Road         → edge
Travel time  → edge weight
Current place → start node
Destination   → goal node
```

Khi đó problem thực được chuyển thành graph search.

Nếu chỉ dùng distance làm edge weight, system có thể chọn đường ngắn nhưng kẹt xe. Nếu dùng expected travel time, representation tốt hơn cho objective “đến nhanh”. Nếu cần tránh toll road, representation lại phải thêm constraint hoặc cost.

Representation vì vậy luôn gắn với **mục tiêu và assumption**.

## State Space

Trong classical AI, một problem thường được mô hình hóa bằng:

- **initial state**;
- **state space**;
- **actions/operators**;
- **transition model**;
- **goal test**;
- **path cost** nếu cần.

Ví dụ 8-puzzle, mỗi cách sắp xếp tile là một state. Move một tile tạo state mới. Search algorithm không cần biết puzzle là “đồ chơi”; nó chỉ cần state representation và transition rules.

State space có thể cực lớn. Với `n` binary variables, đã có tới:

\[
2^n
\]

possible states. Đây là nguồn gốc của **combinatorial explosion (조합 폭발)**.

Representation tốt đôi khi giảm search space mạnh hơn việc thay algorithm.

## Features trong Machine Learning

Trong classical Machine Learning, input thường được biểu diễn bằng feature vector:

\[
\mathbf{x} = [x_1, x_2, \dots, x_d]
\]

Ví dụ credit-risk model có thể dùng:

```text
age
income
loan_amount
debt_ratio
payment_history_length
number_of_late_payments
```

Model không thấy “khách hàng” như con người. Nó thấy vector numbers.

Feature engineering là quá trình thiết kế representation hữu ích từ raw data. Nếu feature không chứa signal cần thiết, model tốt đến đâu cũng khó học được mapping mong muốn.

## Representation Learning

Deep Learning thay đổi cách xây representation. Thay vì engineer tự chọn mọi feature, model học intermediate representations từ data.

Một image classifier có thể biến:

```text
pixels
  ↓
local edges / textures
  ↓
shapes / parts
  ↓
higher-level visual features
  ↓
class prediction
```

Đây không phải hierarchy cố định tuyệt đối, nhưng cho thấy idea: hidden layers transform raw representation thành spaces phù hợp hơn cho task.

Trong NLP, token IDs được map thành **embedding vectors (임베딩 벡터)**. Transformer tiếp tục biến embeddings thành contextual representations, nghĩa là representation của cùng một word có thể khác tùy surrounding context.

## Symbolic Representation

Không phải representation nào cũng là vector. Knowledge có thể được biểu diễn bằng symbol, predicate, rule hoặc graph.

Ví dụ:

```text
works_for(Alice, CompanyA)
located_in(CompanyA, Seoul)
```

Một knowledge graph có thể biểu diễn entity và relation:

```text
Alice ──works_for──> CompanyA ──located_in──> Seoul
```

Symbolic representation có lợi khi structure và relationship cần explicit semantics. Vector representation có lợi khi cần similarity, pattern learning và differentiable optimization. Hybrid systems có thể dùng cả hai.

## Probability Distribution như Representation

Khi uncertainty quan trọng, state không nên được biểu diễn như một fact duy nhất mà có thể là distribution.

Ví dụ system localization không chắc robot đang ở đâu:

\[
P(Location = A)=0.6
\]
\[
P(Location = B)=0.3
\]
\[
P(Location = C)=0.1
\]

Representation này giữ uncertainty thay vì ép chọn một answer quá sớm.

Đây là nền cho Bayesian reasoning, hidden-state models và probabilistic robotics.

## Sequence Representation

Language, audio và time series có order. Nếu chỉ xem các element như unordered set, ta mất information quan trọng.

Câu:

```text
Dog bites man
```

khác:

```text
Man bites dog
```

dù chứa cùng words.

Sequence models vì vậy cần encode order bằng recurrence, positional information hoặc architecture khác.

Transformer không có recurrence tự nhiên như RNN nên cần **positional encoding / positional representation** để biết token order.

## Graph Representation

Khi relationship quan trọng hơn vị trí trong sequence, graph là abstraction tự nhiên.

Social network, molecule, road network, dependency graph, knowledge graph đều có thể biểu diễn:

\[
G=(V,E)
\]

trong đó `V` là vertices/nodes và `E` là edges.

Graph representation cho phép reasoning về connectivity, neighborhood, shortest path, centrality và message passing.

## Continuous Representation và Embedding Space

Embedding đưa discrete object vào continuous vector space:

\[
f: Object \rightarrow \mathbb{R}^d
\]

Nếu training objective được thiết kế phù hợp, semantic relationship có thể phản ánh bằng geometry trong vector space. Hai document có meaning gần nhau có thể có cosine similarity cao hơn.

Điều này là nền cho semantic search, recommendation và RAG.

Tuy nhiên cần tránh misconception rằng embedding space là “bản đồ hoàn hảo của meaning”. Geometry phụ thuộc model, data và objective. Similarity metric chỉ có ý nghĩa trong context của representation đó.

## Lossy và Lossless Representation

Một representation có thể làm mất thông tin.

Ví dụ resize image từ `4000×3000` xuống `224×224` làm mất chi tiết. Tokenization có thể chia text theo cách làm rare word trở thành nhiều subword. Aggregating event logs theo ngày có thể làm mất temporal ordering trong từng phút.

Loss không nhất thiết xấu. Compression có thể loại bỏ detail không cần thiết và làm problem tractable. Câu hỏi đúng là: **thông tin bị mất có quan trọng cho task hay không?**

## Invariance

Một representation tốt thường cố encode những transformation không nên làm thay đổi meaning của task.

Ví dụ object classifier nên ideally nhận ra cùng object dù dịch chuyển nhẹ trong image. Đây là một dạng translation invariance/equivariance liên quan tới CNN.

Trong text, semantic meaning đôi khi nên invariant với thay đổi format hoặc whitespace nhưng không invariant với word order.

Thiết kế representation liên quan sâu tới assumptions về invariance.

## Dimensionality

Vector có quá nhiều dimensions có thể gây computational cost và statistical difficulty. Đây là bối cảnh của **curse of dimensionality**.

Khi dimensionality tăng, data trở nên sparse hơn trong space. Distance metric cũng có thể kém discriminative hơn. Dimensionality reduction như PCA cố giữ important variance trong space nhỏ hơn.

Deep representation learning cũng thường tạo latent space có structure hữu ích hơn raw input.

## Representation và Database Schema

Trong Software Engineering, database schema cũng là một dạng representation của domain. Một AI application thường phải bridge nhiều representation:

```text
Relational rows
    ↓
Application objects
    ↓
Serialized text / structured prompt
    ↓
Tokens
    ↓
Embeddings / hidden states
    ↓
Model output
    ↓
Structured application state
```

Bug có thể xuất hiện ở boundary giữa các representation, không chỉ trong model.

Ví dụ nếu database lưu date sai timezone, model downstream có thể reasoning sai dù model “thông minh”.

## Representation và Objective cùng quyết định learning

Model không tự nhiên học “meaning”. Nó học representation hữu ích để minimize objective.

Nếu contrastive training kéo positive pairs gần nhau và đẩy negative pairs xa nhau, embedding geometry sẽ phản ánh objective đó.

Nếu language model được train bằng next-token prediction, hidden representation được shaped bởi nhiệm vụ dự đoán token tiếp theo.

Do đó:

```text
Data + Architecture + Objective → Learned Representation
```

Không nên tách representation khỏi training objective.

## Mental Model

Hãy nghĩ representation như **API giữa thế giới và algorithm**.

API tốt expose đúng information ở abstraction phù hợp. API tệ che mất signal cần thiết hoặc expose quá nhiều irrelevant detail.

Khi model thất bại, đừng chỉ hỏi “cần model lớn hơn không?”. Hãy hỏi representation có khiến problem khó một cách không cần thiết hay không.

## Common Misconceptions

### “Raw data luôn tốt nhất vì model tự học được hết”

Không đúng trong mọi trường hợp. End-to-end learning có thể mạnh nhưng cần data, compute và architecture phù hợp. Domain constraints hoặc structured features đôi khi cải thiện sample efficiency và reliability.

### “Embedding = meaning”

Embedding là learned numerical representation phục vụ một objective. Nó có thể capture nhiều semantic regularity nhưng không phải meaning theo nghĩa tuyệt đối.

### “Nhiều feature hơn luôn tốt hơn”

Feature irrelevant có thể tăng noise, cost, overfitting risk và leakage. Quality của representation quan trọng hơn count đơn thuần.

## Knowledge Connection

Problem representation nối trực tiếp tới Data Structures, Linear Algebra, Probability, Information Theory, Database Design, Signal Processing và Software Architecture. Đây là lý do AI không thể tách khỏi Computer Science nền tảng.

Xem tiếp: [AI System Architecture](./04_ai_system_architecture.md).