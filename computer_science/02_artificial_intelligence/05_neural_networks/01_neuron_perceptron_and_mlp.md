# Neuron, Perceptron và Multi-Layer Perceptron

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Neuron, Perceptron và Multi-Layer Perceptron**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Artificial neuron** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Perceptron lịch sử** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Artificial neuron là building khối (block / 블록) đơn giản: nhận véc-tơ (vector / 벡터) đầu vào (input / 입력), tính weighted sum, thêm độ lệch (bias / 편향) rồi qua activation. Nhưng để hiểu vì sao neural mạng (network / 네트워크) hoạt động, cần phân biệt rõ **perceptron**, **neuron hiện đại**, **single-layer mạng (network / 네트워크)** và **Multi-Layer Perceptron (MLP / 다층 퍼셉트론)**.

## Artificial neuron

Một đơn vị (unit / 단위):

\[
z=\mathbf w^T\mathbf x+b
\]

\[
a=\phi(z)
\]

`w` xác định direction/sensitivity, `b` dịch quyết định (decision / 결정) threshold, `φ` tạo nonlinearity.

Nếu `φ` là định danh (identity / 식별자), đơn vị (unit / 단위) chỉ là tuyến tính (linear / 선형) regression thành phần (component / 컴포넌트). Nếu sigmoid, có logistic hành vi (behavior / 동작). Nếu ReLU, đầu ra (output / 출력) zero cho negative preactivation và tuyến tính (linear / 선형) cho positive.

> **Chuyển mạch:** Trong **Neuron, Perceptron và Multi-Layer Perceptron**, **Perceptron lịch sử** tiếp nhận điểm tựa từ **Artificial neuron** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tầng (layer / 계층) dưới dạng ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Perceptron lịch sử

Perceptron nhị phân (binary / 이진) dùng threshold/sign activation:

\[
\hat y=sign(\mathbf w^T\mathbf x+b)
\]

Học tập (learning / 학습) quy tắc (rule / 규칙) cập nhật (update / 업데이트) khi misclassified:

\[
\mathbf w\leftarrow \mathbf w+\eta y\mathbf x
\]

cho labels `y∈{-1,+1}` trong simplified form.

Perceptron Convergence Theorem nói nếu dữ liệu (data / 데이터) linearly separable, thuật toán (algorithm / 알고리즘) hội tụ sau hữu hạn mistakes.

Nhưng XOR không linearly separable, nên single perceptron không solve được. Limitation này thúc đẩy multi-layer networks.

> **Chuyển mạch:** Ở chặng này của **Neuron, Perceptron và Multi-Layer Perceptron**, **Tầng (layer / 계층) dưới dạng ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **Perceptron lịch sử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Layer Perceptron** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tầng (layer / 계층) dưới dạng ma trận (matrix / 행렬)

Thay vì một neuron, tầng (layer / 계층) có `m` units:

\[
\mathbf z=W\mathbf x+\mathbf b
\]

với:

\[
W\in\mathbb R^{m\times d}
\]

Sau activation:

\[
\mathbf h=\phi(\mathbf z)
\]

Mỗi row của `W` là weight véc-tơ (vector / 벡터) của một đơn vị (unit / 단위). GPU có thể tính hàng nghìn units song song bằng phép nhân ma trận (matrix multiplication / 행렬 곱셈).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Neuron, Perceptron và Multi-Layer Perceptron**, **Multi-Layer Perceptron** tiếp nhận điểm tựa từ **Tầng (layer / 계층) dưới dạng ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hidden units đang học gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Layer Perceptron

MLP ngăn xếp (stack / 스택) fully-connected layers:

\[
h^{(1)}=\phi(W^{(1)}x+b^{(1)})
\]

\[
h^{(2)}=\phi(W^{(2)}h^{(1)}+b^{(2)})
\]

\[
\hat y=g(W^{(3)}h^{(2)}+b^{(3)})
\]

Hidden layers không có mục tiêu (target / 대상) trực tiếp. Chúng được shaped bởi final mất mát (loss / 손실) thông qua backpropagation.

> **Chuyển mạch:** Trong **Neuron, Perceptron và Multi-Layer Perceptron**, **Hidden units đang học gì?** tiếp nhận điểm tựa từ **Multi-Layer Perceptron** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đầu ra (output / 출력) tầng (layer / 계층) phụ thuộc tác vụ (task / 작업)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hidden units đang học gì?

Không nên assume mỗi hidden đơn vị (unit / 단위) tương ứng một concept rõ như “mắt mèo”. biểu diễn (representation / 표현) thường phân tán (distributed / 분산).

Một hidden véc-tơ (vector / 벡터) `h` có thể encode multiple factors qua directions/subspaces. tầng (layer / 계층) sau combine chúng thành higher-order features.

Interpretability cần empirical phân tích (analysis / 분석), không thể suy meaning chỉ từ đơn vị (unit / 단위) chỉ mục (index / 인덱스).

> **Chuyển mạch:** Ở chặng này của **Neuron, Perceptron và Multi-Layer Perceptron**, **Đầu ra (output / 출력) tầng (layer / 계층) phụ thuộc tác vụ (task / 작업)** tiếp nhận điểm tựa từ **Hidden units đang học gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch dimension** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đầu ra (output / 출력) tầng (layer / 계층) phụ thuộc tác vụ (task / 작업)

Nhị phân (binary / 이진) classification thường dùng one logit + sigmoid hoặc two logits + softmax.

Multiclass:

\[
\mathbf p=softmax(Wh+b)
\]

Regression có thể dùng tuyến tính (linear / 선형) đầu ra (output / 출력).

Multi-label classification thường dùng independent sigmoid per label, không softmax, vì labels không mutually exclusive.

Đầu ra (output / 출력) activation/mất mát (loss / 손실) phải match probabilistic cấu trúc (structure / 구조) của mục tiêu (target / 대상).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Neuron, Perceptron và Multi-Layer Perceptron**, **Batch dimension** tiếp nhận điểm tựa từ **Đầu ra (output / 출력) tầng (layer / 계층) phụ thuộc tác vụ (task / 작업)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parameter count** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch dimension

Thực tế đầu vào (input / 입력) batch:

\[
X\in\mathbb R^{B\times d}
\]

Forward:

\[
Z=XW^T+b
\]

Broadcast độ lệch (bias / 편향) trên `B` samples.

Tensor-shape lập luận (reasoning / 추론) là skill trọng yếu (critical / 중요) khi implement neural networks.

> **Chuyển mạch:** Trong **Neuron, Perceptron và Multi-Layer Perceptron**, **Parameter count** tiếp nhận điểm tựa từ **Batch dimension** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MLP cho tabular dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parameter count

Fully connected tầng (layer / 계층) từ `d_in` tới `d_out` có:

\[
d_{in}d_{out}+d_{out}
\]

parameters.

Nếu ảnh (image / 이미지) 224×224×3 flatten trực tiếp (~150k features) rồi connect 4096 hidden units, parameters >600M chỉ tầng (layer / 계층) đầu. Đây là lý do CNN dùng locality/weight sharing thay dense MLP cho images.

Kiến trúc (architecture / 아키텍처) phản ánh structural các giả định (assumptions / 가정들) của modality.

> **Chuyển mạch:** Ở chặng này của **Neuron, Perceptron và Multi-Layer Perceptron**, **Parameter count** nêu điều cần giải thích; **MLP cho tabular dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quyết định (decision / 결정) regions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MLP cho tabular dữ liệu (data / 데이터)

MLP có thể dùng tabular dữ liệu (data / 데이터), nhưng độ dốc (gradient / 기울기) Boosted Trees thường rất competitive khi dữ liệu (data / 데이터) kích thước (size / 크기) vừa và heterogeneous. Neural các mô hình (models / 모델들) có lợi khi:

- dataset lớn;
- learned embeddings/categories;
- multimodal inputs;
- end-to-end biểu diễn (representation / 표현) học tập (learning / 학습);
- transfer/pretraining.

Không nên chọn MLP chỉ vì “deep học tập (learning / 학습) hiện đại hơn”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Neuron, Perceptron và Multi-Layer Perceptron**, **MLP cho tabular dữ liệu (data / 데이터)** nêu điều cần giải thích; **Quyết định (decision / 결정) regions** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Độ lệch (bias / 편향) term là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyết định (decision / 결정) regions

ReLU MLP tạo piecewise-linear hàm (function / 함수). Mỗi mẫu (pattern / 패턴) ReLU active/inactive xác định một cục bộ (local / 로컬) tuyến tính (linear / 선형) region.

Độ sâu (depth / 깊이) có thể tạo rất nhiều regions, cho quyết định (decision / 결정) ranh giới (boundary / 경계) phức tạp dù mỗi thành phần nguyên thủy (primitive / 기본 요소) thao tác (operation / 연산) đơn giản.

> **Chuyển mạch:** Trong **Neuron, Perceptron và Multi-Layer Perceptron**, **Độ lệch (bias / 편향) term là gì?** tiếp nhận điểm tựa từ **Quyết định (decision / 결정) regions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dense liên kết (connection / 연결) và sparsity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ lệch (bias / 편향) term là gì?

Độ lệch (bias / 편향) `b` không phải statistical/xã hội (social / 사회적) độ lệch (bias / 편향). Nó giống intercept: cho phép activation threshold dịch khỏi origin.

Không có độ lệch (bias / 편향), mọi hyperplane `Wx=0` đi qua origin, hạn chế expressivity.

> **Chuyển mạch:** Ở chặng này của **Neuron, Perceptron và Multi-Layer Perceptron**, sau nội dung của **Độ lệch (bias / 편향) term là gì?**, **Dense liên kết (connection / 연결) và sparsity** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Perceptron vs Logistic Neuron** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dense liên kết (connection / 연결) và sparsity

Tiêu chuẩn (standard / 표준) MLP fully connected: mỗi đầu ra (output / 출력) đơn vị (unit / 단위) nhận toàn bộ previous hidden véc-tơ (vector / 벡터). Nhưng architectures khác có sparse/cục bộ (local / 로컬)/recurrent/attention connections.

Neural mạng (network / 네트워크) không đồng nghĩa fully connected mạng (network / 네트워크).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Neuron, Perceptron và Multi-Layer Perceptron**, **Perceptron vs Logistic Neuron** tiếp nhận điểm tựa từ **Dense liên kết (connection / 연결) và sparsity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Example: XOR bằng hidden biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Perceptron vs Logistic Neuron

Perceptron hard threshold không differentiable tại ranh giới (boundary / 경계) và độ dốc (gradient / 기울기) zero/undefined theo cách không thuận lợi cho backprop.

Sigmoid/ReLU/GELU cung cấp differentiable hoặc almost-everywhere differentiable hành vi (behavior / 동작) phù hợp gradient-based huấn luyện (training / 학습).

Hiện đại (modern / 현대적) mạng (network / 네트워크) vì vậy không train bằng classic perceptron quy tắc (rule / 규칙) trong đa số cases.

> **Chuyển mạch:** Trong **Neuron, Perceptron và Multi-Layer Perceptron**, **Perceptron vs Logistic Neuron** cho ta quy tắc; **Example: XOR bằng hidden biểu diễn (representation / 표현)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example: XOR bằng hidden biểu diễn (representation / 표현)

Một MLP có thể học hidden units đại diện regions khác nhau rồi đầu ra (output / 출력) combine chúng.

Conceptually:

```text
(x1, x2)
  ↓ hidden nonlinear features
[feature: x1 OR x2,
 feature: x1 AND x2]
  ↓ combine
XOR
```

Không cần hand-code chính xác (exact / 정확한) logical features; huấn luyện (training / 학습) có thể discover useful intermediate features.

> **Chuyển mạch:** Ở chặng này của **Neuron, Perceptron và Multi-Layer Perceptron**, **Example: XOR bằng hidden biểu diễn (representation / 표현)** cho ta quy tắc; **Mô hình tư duy (mental model / 사고 모델)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Neuron = linear measurement + nonlinear response
Layer  = many measurements learned together
MLP    = repeated representation transformation
```

Hidden layers không phải “các bước lập luận (reasoning / 추론)” theo nghĩa symbolic; chúng là learned numerical transformations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Neuron, Perceptron và Multi-Layer Perceptron**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Mỗi neuron là một tính năng (feature / 기능) có nghĩa rõ ràng”

Có thể có specialized units, nhưng thông tin (information / 정보) thường phân tán (distributed / 분산).

### “Perceptron và hiện đại (modern / 현대적) neural mạng (network / 네트워크) là cùng một thuật toán (algorithm / 알고리즘)”

Perceptron là historical linear-threshold learner. hiện đại (modern / 현대적) nets use multilayer differentiable computation + backprop/optimizers.

### “độ lệch (bias / 편향) neuron gây mô hình (model / 모델) độ lệch (bias / 편향)”

Độ lệch (bias / 편향) term chỉ là affine offset, không liên quan trực tiếp fairness độ lệch (bias / 편향).

### “MLP đủ universal nên không cần CNN/Transformer”

Theoretical expressivity không thay efficiency/inductive độ lệch (bias / 편향). Specialized architectures learn relevant cấu trúc (structure / 구조) hiệu quả hơn.

> **Chuyển mạch:** Trong **Neuron, Perceptron và Multi-Layer Perceptron**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem lại [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [From Linear Models to Neural Networks](./00_from_linear_models_to_neural_networks.md).

Xem tiếp: [Activation Functions](./02_activation_functions.md), phần quyết định layer composition có thực sự nonlinear và trainable hay không.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
