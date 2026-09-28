# Từ tuyến tính (linear / 선형) các mô hình (models / 모델들) tới Neural Networks

> **Mạch đọc:** Đặt **Từ tuyến tính (linear / 선형) các mô hình (models / 모델들) tới Neural Networks** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Một tuyến tính (linear / 선형) tầng (layer / 계층) thực sự làm gì?** sang **XOR: vì sao một ranh giới (boundary / 경계) tuyến tính không đủ?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Neural mạng (network / 네트워크) không xuất hiện vì tuyến tính (linear / 선형)/logistic regression “sai”, mà vì nhiều relationship trong thế giới không thể biểu diễn tốt bằng một toàn cục (global / 전역) tuyến tính (linear / 선형) ranh giới (boundary / 경계) trên raw features. Ý tưởng cốt lõi của neural mạng (network / 네트워크) là **compose nhiều transformations và học biểu diễn (representation / 표현) trung gian**, thay vì yêu cầu con người hand-engineer toàn bộ nonlinear features.

Chapter này tạo cầu nối từ Machine học tập (learning / 학습) cổ điển sang Deep học tập (learning / 학습). Nếu nắm được lý do composition + nonlinearity cần thiết, neural mạng (network / 네트워크) sẽ không còn là một “hộp đen nhiều tầng (layer / 계층)”.

## Một tuyến tính (linear / 선형) tầng (layer / 계층) thực sự làm gì?

Tuyến tính (linear / 선형)/affine transformation:

\[
\mathbf z=W\mathbf x+\mathbf b
\]

biến véc-tơ (vector / 벡터) đầu vào (input / 입력) thành véc-tơ (vector / 벡터) mới bằng rotate/quy mô (scale / 규모)/shear/dự án (project / 프로젝트) + shift theo geometric interpretation.

Nếu ngăn xếp (stack / 스택) hai tuyến tính (linear / 선형) layers mà không có nonlinear hàm (function / 함수):

\[
\mathbf h=W_1\mathbf x+b_1
\]

\[
\mathbf y=W_2\mathbf h+b_2
\]

thì:

\[
\mathbf y=W_2W_1\mathbf x+(W_2b_1+b_2)
\]

vẫn chỉ là **một affine transformation duy nhất**.

Do đó độ sâu (depth / 깊이) chỉ có ý nghĩa expressive nếu giữa layers có nonlinearity hoặc cơ chế (mechanism / 메커니즘) khác không collapse thành một tuyến tính (linear / 선형) map.

## XOR: vì sao một ranh giới (boundary / 경계) tuyến tính không đủ?

XOR có truth bảng (table / 테이블):

```text
x1 x2 | y
0  0  | 0
0  1  | 1
1  0  | 1
1  1  | 0
```

Không có một đường thẳng trong 2D tách hai positive points khỏi hai negative points.

Nhưng nếu tạo hidden biểu diễn (representation / 표현) phù hợp, bài toán (problem / 문제) có thể trở nên linearly separable ở không gian (space / 공간) mới.

Đây là essence của neural networks:

> Không nhất thiết cố tìm quyết định (decision / 결정) ranh giới (boundary / 경계) phức tạp trong raw không gian (space / 공간); hãy học một transformation đưa dữ liệu (data / 데이터) sang biểu diễn (representation / 표현) không gian (space / 공간) nơi tác vụ (task / 작업) trở nên đơn giản hơn.

## Hand-Engineered Features vs Learned Features

Classical ML thường có chuỗi xử lý (pipeline / 파이프라인):

```text
raw input
→ domain feature engineering
→ linear/tree model
```

Ví dụ văn bản (text / 텍스트) classification từng dùng word counts, TF-IDF, n-grams.

Deep học tập (learning / 학습) chuyển nhiều burden sang mô hình (model / 모델):

```text
raw-ish input
→ learned representations
→ learned representations sâu hơn
→ task output
```

Ảnh (image / 이미지) mạng (network / 네트워크) có thể học edges → textures → parts → object-level representations. Transformer học contextual đơn vị từ (token / 토큰) representations qua nhiều layers.

Điều này không có nghĩa tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링) biến mất. Tokenization, normalization, dữ liệu (data / 데이터) augmentation, kiến trúc (architecture / 아키텍처), position encoding và ngữ cảnh (context / 맥락) construction đều là biểu diễn (representation / 표현) decisions.

## Hàm (function / 함수) Composition

Một neural mạng (network / 네트워크) có thể viết:

\[
f(x)=f_L(f_{L-1}(...f_2(f_1(x))))
\]

Mỗi tầng (layer / 계층) thường:

\[
h^{(l)}=\phi(W^{(l)}h^{(l-1)}+b^{(l)})
\]

`φ` là activation/nonlinearity.

Độ sâu (depth / 깊이) cho phép mô hình (model / 모델) tái sử dụng intermediate features. Thay vì học trực tiếp raw pixels → lớp (class / 클래스), mạng (network / 네트워크) có thể xây hierarchy.

## Universal Approximation không có nghĩa “mạng (network / 네트워크) học được mọi thứ dễ dàng”

Universal Approximation Theorem nói under conditions, một sufficiently wide mạng (network / 네트워크) có thể approximate continuous functions trên compact lĩnh vực (domain / 도메인) tốt tùy ý.

Nhưng theorem **không** nói:

- độ dốc (gradient / 기울기) descent sẽ tìm được parameters đó;
- cần ít dữ liệu (data / 데이터);
- mạng (network / 네트워크) sẽ generalize;
- biểu diễn (representation / 표현) sẽ interpretable;
- compute hữu hạn là đủ.

Expressivity, trainability và generalization là ba vấn đề khác nhau.

## Width và độ sâu (depth / 깊이)

Width tăng số units trong tầng (layer / 계층); độ sâu (depth / 깊이) tăng số composed transformations.

Một số functions có thể represent compactly bằng deep mạng (network / 네트워크) nhưng cần exponentially many units nếu shallow. độ sâu (depth / 깊이) tạo compositional efficiency khi bài toán (problem / 문제) có hierarchical cấu trúc (structure / 구조).

Tuy nhiên deeper không luôn better: tối ưu hóa (optimization / 최적화), độ trễ (latency / 지연 시간), bộ nhớ (memory / 메모리) và overfitting/instability matter.

## Parameters và kiến trúc (architecture / 아키텍처)

Parameters gồm weights/biases học từ dữ liệu (data / 데이터).

Kiến trúc (architecture / 아키텍처) quyết định computation đồ thị (graph / 그래프): số tầng (layer / 계층), hidden dimension, connections, activation, normalization, attention/convolution etc.

Kiến trúc (architecture / 아키텍처) là một mạnh **inductive độ lệch (bias / 편향)**.

CNN encode locality/weight sharing. RNN encode recurrence. Transformer encode content-dependent interactions through attention.

## Neural mạng (network / 네트워크) là differentiable program

Một useful mô hình tư duy (mental model / 사고 모델):

> Neural mạng (network / 네트워크) là một parameterized differentiable program.

Forward pass chạy program để tạo đầu ra (output / 출력). mất mát (loss / 손실) đo đầu ra (output / 출력). Backpropagation dùng chuỗi (chain / 사슬) quy tắc (rule / 규칙) để tính sensitivity của mất mát (loss / 손실) đối với parameters. Optimizer thay parameters.

```text
Input
 ↓
Differentiable computation graph fθ
 ↓
Prediction
 ↓
Loss
 ↓ backward
Gradients
 ↓ optimizer
Updated θ
```

Đây là cốt lõi (core / 핵심) huấn luyện (training / 학습) vòng lặp (loop / 루프) của Deep học tập (learning / 학습).

## Neural mạng (network / 네트워크) không nhất thiết mô phỏng brain

Names như neuron, synapse đến từ historical inspiration, nhưng hiện đại (modern / 현대적) neural networks không phải realistic simulation của biological brain.

Artificial neuron thường chỉ tính weighted sum + activation. Transformer càng xa neuron sinh học trực tiếp.

Biological analogy hữu ích ở mức lịch sử/intuitive inspiration, nhưng không nên dùng để suy luận technical hành vi (behavior / 동작).

## Phân tán (distributed / 분산) biểu diễn (representation / 표현)

Trong symbolic hệ thống (system / 시스템), concept có thể map tới tường minh (explicit / 명시적) symbol. Neural networks thường dùng **phân tán (distributed / 분산) biểu diễn (representation / 표현)**: thông tin (information / 정보) được encode qua mẫu (pattern / 패턴) của nhiều dimensions/units.

Một neuron hiếm khi tương ứng đơn giản với một ngữ nghĩa (semantic / 의미적) concept duy nhất. Meaning thường nằm trong subspace/direction/activation mẫu (pattern / 패턴).

Điều này giúp biểu diễn (representation / 표현) compositional/generalizable nhưng làm interpretability khó.

## End-to-End học tập (learning / 학습)

End-to-end huấn luyện (training / 학습) optimize một mục tiêu (objective / 목표) qua nhiều stages jointly.

Ví dụ speech recognition trước đây có chuỗi xử lý (pipeline / 파이프라인) acoustic features → phoneme mô hình (model / 모델) → ngôn ngữ (language / 언어) mô hình (model / 모델) → decoder. End-to-end mô hình (model / 모델) có thể learn ánh xạ (mapping / 매핑) audio → văn bản (text / 텍스트) với components jointly optimized.

Lợi ích: intermediate biểu diễn (representation / 표현) adapt tác vụ (task / 작업).

Rủi ro (risk / 위험): less modular/debuggable, cần more dữ liệu (data / 데이터)/compute, và thất bại (failure / 실패) origin khó dấu vết (trace / 추적).

Môi trường vận hành (production / 운영 환경) các hệ thống (systems / 시스템들) thường vẫn hybrid, không phải mọi thứ end-to-end.

## Neural Networks và probabilistic outputs

Mạng (network / 네트워크) thường đầu ra (output / 출력) logits/parameters của phân phối (distribution / 분포), không phải “answer certainty” trực tiếp.

Classification:

\[
p(y\mid x)=softmax(W_outh+b)
\]

Regression có thể đầu ra (output / 출력) mean/variance của Gaussian.

Generative các mô hình (models / 모델들) parameterize complex distributions.

Xác suất (probability / 확률)/calibration principles từ ML vẫn áp dụng.

## Quy mô (scale / 규모): dữ liệu (data / 데이터), compute, parameters

Deep học tập (learning / 학습) thành công nhờ combination:

- large datasets;
- GPU/accelerator ma trận (matrix / 행렬) computation;
- better initialization/activations/normalization;
- tối ưu hóa (optimization / 최적화) methods;
- architectures matching modalities;
- phân tán (distributed / 분산) các hệ thống (systems / 시스템들).

Không có một single “neural mạng (network / 네트워크) breakthrough” giải thích toàn bộ.

## Mô hình tư duy (mental model / 사고 모델)

```text
Linear model:
raw representation → simple decision

Neural network:
raw representation
→ learned transform
→ learned transform
→ ...
→ representation where task is easier
→ simple output head
```

## Dùng chung (common / 공통) Misconceptions

### “Neural mạng (network / 네트워크) chỉ là rất nhiều logistic regressions”

Mỗi đơn vị (unit / 단위) có tuyến tính (linear / 선형) + nonlinear thao tác (operation / 연산), nhưng composition tạo learned hierarchical representations mà một single logistic mô hình (model / 모델) không có.

### “Universal approximation nghĩa neural mạng (network / 네트워크) giải được mọi bài toán (problem / 문제)”

Biểu diễn (representation / 표현) sức chứa (capacity / 용량) không đảm bảo learnability, dữ liệu (data / 데이터) sufficiency, robustness hay tính đúng đắn (correctness / 정확성).

### “Deep học tập (learning / 학습) không cần tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링)”

Nó giảm handcraft tính năng (feature / 기능) extraction nhưng dữ liệu (data / 데이터)/biểu diễn (representation / 표현)/kiến trúc (architecture / 아키텍처) kỹ thuật (engineering / 엔지니어링) vẫn cực quan trọng.

### “Càng nhiều layers càng intelligent”

Độ sâu (depth / 깊이) chỉ hữu ích nếu kiến trúc (architecture / 아키텍처)/huấn luyện (training / 학습)/dữ liệu (data / 데이터) hỗ trợ (support / 지원). Deeper có thể khó optimize và lãng phí compute.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Chapter này nối [Linear Regression](../04_machine_learning/05_linear_regression.md), [Logistic Regression](../04_machine_learning/06_logistic_regression.md), [Calculus](../01_mathematical_foundations/04_calculus_for_ai.md) và [Optimization](../01_mathematical_foundations/06_optimization.md).

Xem tiếp: [Neuron, Perceptron and MLP](./01_neuron_perceptron_and_mlp.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 neuron perceptron and mlp](./01_neuron_perceptron_and_mlp.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
