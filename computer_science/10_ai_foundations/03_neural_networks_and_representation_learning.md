# Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Neural networks và representation learning**. Route đi từ neuron/layers → forward pass/loss → gradient descent/batching → CNN/sequence/attention → embeddings/capacity scaling, để biểu diễn được nối với objective và optimization.

Neural mạng (network / 네트워크) là parameterized hàm (function / 함수) composition có khả năng học nonlinear representations từ dữ liệu (data / 데이터). Tên “neural” lấy cảm hứng sinh học lịch sử nhưng hiện đại (modern / 현대적) deep học tập (learning / 학습) nên được hiểu bằng tuyến tính (linear / 선형) algebra, nonlinear functions, tối ưu hóa (optimization / 최적화) và dữ liệu (data / 데이터)—not như mô phỏng não đầy đủ.

## Neuron như affine transform + nonlinearity

Một đơn vị (unit / 단위) cơ bản tính:

\[
z = w^T x + b,
\qquad a = \phi(z)
\]

Nếu chỉ ngăn xếp (stack / 스택) tuyến tính (linear / 선형) layers không có nonlinear activation, toàn mạng (network / 네트워크) vẫn collapse thành một tuyến tính (linear / 선형) transformation. Nonlinearity tạo khả năng biểu diễn functions phức tạp.

> **Nối mạch:** Neuron là affine transform cộng nonlinearity; layers ghép các biến đổi thành representation, rồi forward pass tạo prediction để loss đo sai lệch cần tối ưu.

## Layers và representations

Early layers có thể học cục bộ (local / 로컬)/simple patterns; deeper layers compose thành higher-level features. Nhưng interpretation không phải luôn human-readable.

Biểu diễn (representation / 표현) học tập (learning / 학습) giảm nhu cầu hand-engineer features, đổi lại cần dữ liệu (data / 데이터)/compute và làm nội bộ (internal / 내부) hành vi (behavior / 동작) khó giải thích hơn.

> **Nối mạch:** **Forward pass và mất mát (loss / 손실)** nối từ **Layers và representations** sang **Độ dốc (gradient / 기울기) descent**, vì cơ chế trước tạo đầu vào cho bước sau.

## Forward pass và mất mát (loss / 손실)

Đầu vào (input / 입력) đi qua layers tạo prediction. mất mát (loss / 손실) so prediction với mục tiêu (target / 대상)/mục tiêu (objective / 목표).

Huấn luyện (training / 학습) cần độ dốc (gradient / 기울기) của mất mát (loss / 손실) theo mọi parameters. Backpropagation là efficient ứng dụng (application / 애플리케이션) của chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên computation đồ thị (graph / 그래프), không phải một học tập (learning / 학습) quy tắc (rule / 규칙) bí ẩn độc lập khỏi calculus.

> **Nối mạch:** **Độ dốc (gradient / 기울기) descent** nối từ **Forward pass và mất mát (loss / 손실)** sang **Batch và stochasticity**, vì cơ chế trước tạo đầu vào cho bước sau.

## Độ dốc (gradient / 기울기) descent

Parameters cập nhật (update / 업데이트) theo hướng giảm mất mát (loss / 손실):

\[
\theta \leftarrow \theta - \eta \nabla_\theta L
\]

Học tập (learning / 학습) tỷ lệ (rate / 비율) `η` quá lớn có thể diverge; quá nhỏ huấn luyện (training / 학습) chậm. Adaptive optimizers như Adam điều chỉnh cập nhật (update / 업데이트) dựa moments của gradients.

Tối ưu hóa (optimization / 최적화) landscape non-convex; chính xác (exact / 정확한) toàn cục (global / 전역) optimum không thường là yêu cầu (requirement / 요구사항) để generalize tốt.

> **Nối mạch:** **Batch và stochasticity** nối từ **Độ dốc (gradient / 기울기) descent** sang **CNN intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Batch và stochasticity

Full-batch độ dốc (gradient / 기울기) dùng toàn dataset mỗi step; SGD/minibatch dùng subset, giảm per-step chi phí (cost / 비용) và thêm noise có thể giúp exploration/generalization.

Batch kích thước (size / 크기) ảnh hưởng bộ nhớ (memory / 메모리), thông lượng (throughput / 처리량) và tối ưu hóa (optimization / 최적화) dynamics.

> **Nối mạch:** **CNN intuition** nối từ **Batch và stochasticity** sang **Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention**, vì cơ chế trước tạo đầu vào cho bước sau.

## CNN intuition

Convolutional neural networks khai thác locality và weight sharing trên grid-like dữ liệu (data / 데이터) như images. Same filter dùng ở nhiều positions tạo translation-related inductive độ lệch (bias / 편향).

> **Nối mạch:** **CNN intuition** đặt đầu vào cho **Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention**, rồi **Embeddings** mở rộng hệ quả.

## Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention

RNN xử lý trạng thái (state / 상태) theo chuỗi (sequence / 시퀀스) nhưng khó parallelize dài và có độ dốc (gradient / 기울기) issues. Attention cho mỗi position tính weighted tương tác (interaction / 상호작용) với positions khác.

Transformer dùng self-attention + feed-forward blocks và positional thông tin (information / 정보), trở thành kiến trúc (architecture / 아키텍처) nền cho ngôn ngữ (language / 언어)/vision/multimodal các mô hình (models / 모델들).

> **Nối mạch:** **Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention** đặt đầu vào cho **Embeddings**, rồi **Sức chứa (capacity / 용량) và scaling** mở rộng hệ quả.

## Embeddings

Embedding map discrete symbols/items vào vectors sao cho hình học (geometry / 기하학) phản ánh learned relationships theo huấn luyện (training / 학습) mục tiêu (objective / 목표).

Similarity trong embedding không gian (space / 공간) là model-dependent. Cosine gần không có nghĩa entities “giống nhau mọi nghĩa”; chỉ theo biểu diễn (representation / 표현) learned.

> **Nối mạch:** **Sức chứa (capacity / 용량) và scaling** nối từ **Embeddings** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sức chứa (capacity / 용량) và scaling

Tăng parameters/dữ liệu (data / 데이터)/compute có thể cải thiện hiệu năng (performance / 성능) nhưng chi phí (cost / 비용) năng lượng (energy / 에너지), độ trễ (latency / 지연 시간) và bộ nhớ (memory / 메모리) tăng. Quantization, pruning, distillation và efficient architectures trade accuracy/compute.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Sức chứa (capacity / 용량) và scaling** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Neural mạng (network / 네트워크) học giống não.”** Inspiration lịch sử không đồng nghĩa biological fidelity.

**“Deep học tập (learning / 학습) không cần tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링).”** kiến trúc (architecture / 아키텍처), tokenization, preprocessing, labels và mục tiêu (objective / 목표) vẫn encode các giả định (assumptions / 가정들).

**“Attention là explanation.”** Attention weights không tự động là nhân quả (causal / 인과적) explanation của mô hình (model / 모델) quyết định (decision / 결정).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Deep mạng (network / 네트워크) là differentiable program whose nội bộ (internal / 내부) biểu diễn (representation / 표현) được học bằng gradient-based tối ưu hóa (optimization / 최적화) để phục vụ mục tiêu (objective / 목표) trên dữ liệu (data / 데이터).

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc [linear algebra](../../mathematics/04_vectors_linear_algebra/01_matrices_and_linear_systems.md), [matrix calculus/autodiff](../../mathematics/04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md), [gradient descent](../../mathematics/08_optimization_numerical/01_gradient_descent_and_convexity.md) và [ML foundations](./02_machine_learning_foundations.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
