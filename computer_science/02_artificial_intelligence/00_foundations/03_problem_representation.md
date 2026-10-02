# Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Problem representation trong AI**. Route đi từ real-world goal/constraints → state-space/actions → transition/cost model → observability and uncertainty, để bài toán tính toán giữ được phần quan trọng của bài toán gốc.

Trước khi một AI hệ thống (system / 시스템) có thể tìm kiếm (search / 검색), learn, reason hoặc optimize, bài toán (problem / 문제) phải được chuyển thành một **biểu diễn (representation / 표현)** mà máy có thể thao tác. Đây là bước thường bị xem nhẹ vì nó nằm trước thuật toán (algorithm / 알고리즘), nhưng biểu diễn (representation / 표현) quyết định rất lớn việc bài toán có dễ giải hay không.

Máy không nhận “ý nghĩa” trực tiếp. Nó nhận bits, numbers, tokens, tensors, graphs hoặc symbolic structures. Vì vậy câu hỏi đầu tiên không phải “mô hình (model / 모델) nào mạnh nhất?”, mà là:

> **Ta đang biểu diễn thế giới như thế nào, và biểu diễn (representation / 표현) đó giữ lại hoặc làm mất thông tin gì?**

## Từ real-world bài toán (problem / 문제) tới computational bài toán (problem / 문제)

Giả sử muốn xây hệ thống tìm đường trong Seoul. Real world gồm đường phố, traffic, one-way road, thời gian, weather, accidents và vô số chi tiết. Không thể đưa “thế giới thật” nguyên trạng vào thuật toán (algorithm / 알고리즘). Ta phải chọn lớp trừu tượng (abstraction / 추상화).

Một biểu diễn (representation / 표현) đơn giản:

```text
Intersection → node
Road         → edge
Travel time  → edge weight
Current place → start node
Destination   → goal node
```

Khi đó bài toán (problem / 문제) thực được chuyển thành đồ thị (graph / 그래프) tìm kiếm (search / 검색).

Nếu chỉ dùng distance làm edge weight, hệ thống (system / 시스템) có thể chọn đường ngắn nhưng kẹt xe. Nếu dùng expected travel thời gian (time / 시간), biểu diễn (representation / 표현) tốt hơn cho mục tiêu (objective / 목표) “đến nhanh”. Nếu cần tránh toll road, biểu diễn (representation / 표현) lại phải thêm ràng buộc (constraint / 제약조건) hoặc chi phí (cost / 비용).

Biểu diễn (representation / 표현) vì vậy luôn gắn với **mục tiêu và giả định (assumption / 가정)**.

> **Chuyển mạch:** Trong **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Trạng thái (state / 상태) không gian (space / 공간)** tiếp nhận điểm tựa từ **Từ real-world bài toán (problem / 문제) tới computational bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Features trong Machine học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trạng thái (state / 상태) không gian (space / 공간)

Trong classical AI, một bài toán (problem / 문제) thường được mô hình hóa bằng:

- **initial trạng thái (state / 상태)**;
- **trạng thái (state / 상태) không gian (space / 공간)**;
- **actions/operators**;
- **chuyển tiếp (transition / 전이) mô hình (model / 모델)**;
- **goal kiểm thử (test / 테스트)**;
- **đường dẫn (path / 경로) chi phí (cost / 비용)** nếu cần.

Ví dụ 8-puzzle, mỗi cách sắp xếp tile là một trạng thái (state / 상태). Move một tile tạo trạng thái (state / 상태) mới. tìm kiếm (search / 검색) thuật toán (algorithm / 알고리즘) không cần biết puzzle là “đồ chơi”; nó chỉ cần trạng thái (state / 상태) biểu diễn (representation / 표현) và chuyển tiếp (transition / 전이) rules.

Trạng thái (state / 상태) không gian (space / 공간) có thể cực lớn. Với `n` nhị phân (binary / 이진) variables, đã có tới:

\[
2^n
\]

possible states. Đây là nguồn gốc của **combinatorial explosion (조합 폭발)**.

Biểu diễn (representation / 표현) tốt đôi khi giảm tìm kiếm (search / 검색) không gian (space / 공간) mạnh hơn việc thay thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Ở chặng này của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Features trong Machine học tập (learning / 학습)** tiếp nhận điểm tựa từ **Trạng thái (state / 상태) không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biểu diễn (representation / 표현) học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Features trong Machine học tập (learning / 학습)

Trong classical Machine học tập (learning / 학습), đầu vào (input / 입력) thường được biểu diễn bằng tính năng (feature / 기능) véc-tơ (vector / 벡터):

\[
\mathbf{x} = [x_1, x_2, \dots, x_d]
\]

Ví dụ credit-risk mô hình (model / 모델) có thể dùng:

```text
age
income
loan_amount
debt_ratio
payment_history_length
number_of_late_payments
```

Mô hình (model / 모델) không thấy “khách hàng” như con người. Nó thấy véc-tơ (vector / 벡터) numbers.

Tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링) là quá trình thiết kế biểu diễn (representation / 표현) hữu ích từ raw dữ liệu (data / 데이터). Nếu tính năng (feature / 기능) không chứa tín hiệu (signal / 신호) cần thiết, mô hình (model / 모델) tốt đến đâu cũng khó học được ánh xạ (mapping / 매핑) mong muốn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Biểu diễn (representation / 표현) học tập (learning / 학습)** tiếp nhận điểm tựa từ **Features trong Machine học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Symbolic biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn (representation / 표현) học tập (learning / 학습)

Deep học tập (learning / 학습) thay đổi cách xây biểu diễn (representation / 표현). Thay vì engineer tự chọn mọi tính năng (feature / 기능), mô hình (model / 모델) học intermediate representations từ dữ liệu (data / 데이터).

Một ảnh (image / 이미지) classifier có thể biến:

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

Đây không phải hierarchy cố định tuyệt đối, nhưng cho thấy idea: hidden layers transform raw biểu diễn (representation / 표현) thành spaces phù hợp hơn cho tác vụ (task / 작업).

Trong NLP, đơn vị từ (token / 토큰) IDs được map thành **embedding vectors (임베딩 벡터)**. Transformer tiếp tục biến embeddings thành contextual representations, nghĩa là biểu diễn (representation / 표현) của cùng một word có thể khác tùy surrounding ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Trong **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Symbolic biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **Biểu diễn (representation / 표현) học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xác suất (probability / 확률) phân phối (distribution / 분포) như biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symbolic biểu diễn (representation / 표현)

Không phải biểu diễn (representation / 표현) nào cũng là véc-tơ (vector / 벡터). kiến thức (knowledge / 지식) có thể được biểu diễn bằng symbol, predicate, quy tắc (rule / 규칙) hoặc đồ thị (graph / 그래프).

Ví dụ:

```text
works_for(Alice, CompanyA)
located_in(CompanyA, Seoul)
```

Một kiến thức (knowledge / 지식) đồ thị (graph / 그래프) có thể biểu diễn thực thể (entity / 엔터티) và quan hệ (relation / 관계):

```text
Alice ──works_for──> CompanyA ──located_in──> Seoul
```

Symbolic biểu diễn (representation / 표현) có lợi khi cấu trúc (structure / 구조) và relationship cần tường minh (explicit / 명시적) ngữ nghĩa (semantics / 의미론). véc-tơ (vector / 벡터) biểu diễn (representation / 표현) có lợi khi cần similarity, mẫu (pattern / 패턴) học tập (learning / 학습) và differentiable tối ưu hóa (optimization / 최적화). Hybrid các hệ thống (systems / 시스템들) có thể dùng cả hai.

> **Chuyển mạch:** Ở chặng này của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Xác suất (probability / 확률) phân phối (distribution / 분포) như biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **Symbolic biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi (sequence / 시퀀스) biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xác suất (probability / 확률) phân phối (distribution / 분포) như biểu diễn (representation / 표현)

Khi bất định (uncertainty / 불확실성) quan trọng, trạng thái (state / 상태) không nên được biểu diễn như một fact duy nhất mà có thể là phân phối (distribution / 분포).

Ví dụ hệ thống (system / 시스템) localization không chắc robot đang ở đâu:

\[
P(Location = A)=0.6
\]
\[
P(Location = B)=0.3
\]
\[
P(Location = C)=0.1
\]

Biểu diễn (representation / 표현) này giữ bất định (uncertainty / 불확실성) thay vì ép chọn một answer quá sớm.

Đây là nền cho Bayesian lập luận (reasoning / 추론), hidden-state các mô hình (models / 모델들) và probabilistic robotics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Xác suất (probability / 확률) phân phối (distribution / 분포) như biểu diễn (representation / 표현)** xác định đầu vào; **Chuỗi (sequence / 시퀀스) biểu diễn (representation / 표현)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Đồ thị (graph / 그래프) biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) biểu diễn (representation / 표현)

Ngôn ngữ (language / 언어), audio và thời gian (time / 시간) series có thứ tự (order / 순서). Nếu chỉ xem các element như unordered set, ta mất thông tin (information / 정보) quan trọng.

Câu:

```text
Dog bites man
```

khác:

```text
Man bites dog
```

dù chứa cùng words.

Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) vì vậy cần encode thứ tự (order / 순서) bằng recurrence, positional thông tin (information / 정보) hoặc kiến trúc (architecture / 아키텍처) khác.

Transformer không có recurrence tự nhiên như RNN nên cần **positional encoding / positional biểu diễn (representation / 표현)** để biết đơn vị từ (token / 토큰) thứ tự (order / 순서).

> **Chuyển mạch:** Trong **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Chuỗi (sequence / 시퀀스) biểu diễn (representation / 표현)** xác định đầu vào; **Đồ thị (graph / 그래프) biểu diễn (representation / 표현)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Continuous biểu diễn (representation / 표현) và Embedding không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồ thị (graph / 그래프) biểu diễn (representation / 표현)

Khi relationship quan trọng hơn vị trí trong chuỗi (sequence / 시퀀스), đồ thị (graph / 그래프) là lớp trừu tượng (abstraction / 추상화) tự nhiên.

Xã hội (social / 사회적) mạng (network / 네트워크), molecule, road mạng (network / 네트워크), phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), kiến thức (knowledge / 지식) đồ thị (graph / 그래프) đều có thể biểu diễn:

\[
G=(V,E)
\]

trong đó `V` là vertices/nodes và `E` là edges.

Đồ thị (graph / 그래프) biểu diễn (representation / 표현) cho phép lập luận (reasoning / 추론) về connectivity, neighborhood, shortest đường dẫn (path / 경로), centrality và message passing.

> **Chuyển mạch:** Ở chặng này của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Continuous biểu diễn (representation / 표현) và Embedding không gian (space / 공간)** tiếp nhận điểm tựa từ **Đồ thị (graph / 그래프) biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lossy và Lossless biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Continuous biểu diễn (representation / 표현) và Embedding không gian (space / 공간)

Embedding đưa discrete đối tượng (object / 객체) vào continuous véc-tơ (vector / 벡터) không gian (space / 공간):

\[
f: đối tượng (object / 객체) \rightarrow \mathbb{R}^d
\]

Nếu huấn luyện (training / 학습) mục tiêu (objective / 목표) được thiết kế phù hợp, ngữ nghĩa (semantic / 의미적) relationship có thể phản ánh bằng hình học (geometry / 기하학) trong véc-tơ (vector / 벡터) không gian (space / 공간). Hai document có meaning gần nhau có thể có cosine similarity cao hơn.

Điều này là nền cho ngữ nghĩa (semantic / 의미적) tìm kiếm (search / 검색), recommendation và RAG.

Tuy nhiên cần tránh misconception rằng embedding không gian (space / 공간) là “bản đồ hoàn hảo của meaning”. hình học (geometry / 기하학) phụ thuộc mô hình (model / 모델), dữ liệu (data / 데이터) và mục tiêu (objective / 목표). Similarity chỉ số (metric / 지표) chỉ có ý nghĩa trong ngữ cảnh (context / 맥락) của biểu diễn (representation / 표현) đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Lossy và Lossless biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **Continuous biểu diễn (representation / 표현) và Embedding không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Invariance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lossy và Lossless biểu diễn (representation / 표현)

Một biểu diễn (representation / 표현) có thể làm mất thông tin.

Ví dụ resize ảnh (image / 이미지) từ `4000×3000` xuống `224×224` làm mất chi tiết. Tokenization có thể chia văn bản (text / 텍스트) theo cách làm rare word trở thành nhiều subword. Aggregating sự kiện (event / 이벤트) logs theo ngày có thể làm mất temporal thứ tự (ordering / 순서) trong từng phút.

Mất mát (loss / 손실) không nhất thiết xấu. Compression có thể loại bỏ detail không cần thiết và làm bài toán (problem / 문제) tractable. Câu hỏi đúng là: **thông tin bị mất có quan trọng cho tác vụ (task / 작업) hay không?**

> **Chuyển mạch:** Trong **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Invariance** tiếp nhận điểm tựa từ **Lossy và Lossless biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dimensionality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Invariance

Một biểu diễn (representation / 표현) tốt thường cố encode những transformation không nên làm thay đổi meaning của tác vụ (task / 작업).

Ví dụ đối tượng (object / 객체) classifier nên ideally nhận ra cùng đối tượng (object / 객체) dù dịch chuyển nhẹ trong ảnh (image / 이미지). Đây là một dạng translation invariance/equivariance liên quan tới CNN.

Trong văn bản (text / 텍스트), ý nghĩa (semantic meaning / 의미적 뜻) đôi khi nên bất biến (invariant / 불변식) với thay đổi format hoặc whitespace nhưng không bất biến (invariant / 불변식) với word thứ tự (order / 순서).

Thiết kế biểu diễn (representation / 표현) liên quan sâu tới các giả định (assumptions / 가정들) về invariance.

> **Chuyển mạch:** Ở chặng này của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Dimensionality** tiếp nhận điểm tựa từ **Invariance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biểu diễn (representation / 표현) và cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dimensionality

Véc-tơ (vector / 벡터) có quá nhiều dimensions có thể gây computational chi phí (cost / 비용) và statistical difficulty. Đây là bối cảnh của **curse of dimensionality**.

Khi dimensionality tăng, dữ liệu (data / 데이터) trở nên sparse hơn trong không gian (space / 공간). Distance chỉ số (metric / 지표) cũng có thể kém discriminative hơn. Dimensionality reduction như PCA cố giữ important variance trong không gian (space / 공간) nhỏ hơn.

Deep biểu diễn (representation / 표현) học tập (learning / 학습) cũng thường tạo latent không gian (space / 공간) có cấu trúc (structure / 구조) hữu ích hơn raw đầu vào (input / 입력).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Dimensionality** nêu điều cần giải thích; **Biểu diễn (representation / 표현) và cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Biểu diễn (representation / 표현) và mục tiêu (objective / 목표) cùng quyết định học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn (representation / 표현) và cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마)

Trong Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학), cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) cũng là một dạng biểu diễn (representation / 표현) của lĩnh vực (domain / 도메인). Một AI ứng dụng (application / 애플리케이션) thường phải cầu nối (bridge / 브리지) nhiều biểu diễn (representation / 표현):

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

Bug có thể xuất hiện ở ranh giới (boundary / 경계) giữa các biểu diễn (representation / 표현), không chỉ trong mô hình (model / 모델).

Ví dụ nếu cơ sở dữ liệu (database / 데이터베이스) lưu date sai timezone, mô hình (model / 모델) downstream có thể lập luận (reasoning / 추론) sai dù mô hình (model / 모델) “thông minh”.

> **Chuyển mạch:** Trong **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Biểu diễn (representation / 표현) và cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마)** nêu điều cần giải thích; **Biểu diễn (representation / 표현) và mục tiêu (objective / 목표) cùng quyết định học tập (learning / 학습)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn (representation / 표현) và mục tiêu (objective / 목표) cùng quyết định học tập (learning / 학습)

Mô hình (model / 모델) không tự nhiên học “meaning”. Nó học biểu diễn (representation / 표현) hữu ích để minimize mục tiêu (objective / 목표).

Nếu contrastive huấn luyện (training / 학습) kéo positive pairs gần nhau và đẩy negative pairs xa nhau, embedding hình học (geometry / 기하학) sẽ phản ánh mục tiêu (objective / 목표) đó.

Nếu ngôn ngữ (language / 언어) mô hình (model / 모델) được train bằng next-token prediction, hidden biểu diễn (representation / 표현) được shaped bởi nhiệm vụ dự đoán đơn vị từ (token / 토큰) tiếp theo.

Do đó:

```text
Data + Architecture + Objective → Learned Representation
```

Không nên tách biểu diễn (representation / 표현) khỏi huấn luyện (training / 학습) mục tiêu (objective / 목표).

> **Chuyển mạch:** Ở chặng này của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Biểu diễn (representation / 표현) và mục tiêu (objective / 목표) cùng quyết định học tập (learning / 학습)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Hãy nghĩ biểu diễn (representation / 표현) như **API giữa thế giới và thuật toán (algorithm / 알고리즘)**.

API tốt expose đúng thông tin (information / 정보) ở lớp trừu tượng (abstraction / 추상화) phù hợp. API tệ che mất tín hiệu (signal / 신호) cần thiết hoặc expose quá nhiều irrelevant detail.

Khi mô hình (model / 모델) thất bại, đừng chỉ hỏi “cần mô hình (model / 모델) lớn hơn không?”. Hãy hỏi biểu diễn (representation / 표현) có khiến bài toán (problem / 문제) khó một cách không cần thiết hay không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Raw dữ liệu (data / 데이터) luôn tốt nhất vì mô hình (model / 모델) tự học được hết”

Không đúng trong mọi trường hợp. End-to-end học tập (learning / 학습) có thể mạnh nhưng cần dữ liệu (data / 데이터), compute và kiến trúc (architecture / 아키텍처) phù hợp. lĩnh vực (domain / 도메인) các ràng buộc (constraints / 제약조건들) hoặc structured features đôi khi cải thiện mẫu (sample / 표본) efficiency và độ tin cậy (reliability / 신뢰성).

### “Embedding = meaning”

Embedding là learned numerical biểu diễn (representation / 표현) phục vụ một mục tiêu (objective / 목표). Nó có thể capture nhiều ngữ nghĩa (semantic / 의미적) regularity nhưng không phải meaning theo nghĩa tuyệt đối.

### “Nhiều tính năng (feature / 기능) hơn luôn tốt hơn”

Tính năng (feature / 기능) irrelevant có thể tăng noise, chi phí (cost / 비용), overfitting rủi ro (risk / 위험) và leakage. chất lượng (quality / 품질) của biểu diễn (representation / 표현) quan trọng hơn count đơn thuần.

> **Chuyển mạch:** Trong **Bài toán (problem / 문제) biểu diễn (representation / 표현) trong AI**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Bài toán (problem / 문제) biểu diễn (representation / 표현) nối trực tiếp tới dữ liệu (data / 데이터) Structures, tuyến tính (linear / 선형) Algebra, xác suất (probability / 확률), thông tin (information / 정보) lý thuyết (theory / 이론), cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계), tín hiệu (signal / 신호) Processing và Software kiến trúc (architecture / 아키텍처). Đây là lý do AI không thể tách khỏi Khoa học máy tính (computer science / 컴퓨터 과학) nền tảng.

Xem tiếp: [AI System Architecture](./04_ai_system_architecture.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
