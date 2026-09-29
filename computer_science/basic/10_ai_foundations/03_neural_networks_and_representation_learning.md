# Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)

> **Mạch đọc:** Đọc **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Neuron như affine transform + nonlinearity** sang **Layers và representations**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Neural mạng (network / 네트워크) là parameterized hàm (function / 함수) composition có khả năng học nonlinear representations từ dữ liệu (data / 데이터). Tên “neural” lấy cảm hứng sinh học lịch sử nhưng hiện đại (modern / 현대적) deep học tập (learning / 학습) nên được hiểu bằng tuyến tính (linear / 선형) algebra, nonlinear functions, tối ưu hóa (optimization / 최적화) và dữ liệu (data / 데이터)—not như mô phỏng não đầy đủ.

## Neuron như affine transform + nonlinearity

Một đơn vị (unit / 단위) cơ bản tính:

\[
z = w^T x + b,
\qquad a = \phi(z)
\]

Nếu chỉ ngăn xếp (stack / 스택) tuyến tính (linear / 선형) layers không có nonlinear activation, toàn mạng (network / 네트워크) vẫn collapse thành một tuyến tính (linear / 선형) transformation. Nonlinearity tạo khả năng biểu diễn functions phức tạp.


> **Chuyển mạch:** Từ **Neuron như affine transform + nonlinearity**, ta sang **Layers và representations** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Layers và representations

Early layers có thể học cục bộ (local / 로컬)/simple patterns; deeper layers compose thành higher-level features. Nhưng interpretation không phải luôn human-readable.

Biểu diễn (representation / 표현) học tập (learning / 학습) giảm nhu cầu hand-engineer features, đổi lại cần dữ liệu (data / 데이터)/compute và làm nội bộ (internal / 내부) hành vi (behavior / 동작) khó giải thích hơn.


> **Chuyển mạch:** Từ **Layers và representations**, ta sang **Forward pass và mất mát (loss / 손실)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Forward pass và mất mát (loss / 손실)

Đầu vào (input / 입력) đi qua layers tạo prediction. mất mát (loss / 손실) so prediction với mục tiêu (target / 대상)/mục tiêu (objective / 목표).

Huấn luyện (training / 학습) cần độ dốc (gradient / 기울기) của mất mát (loss / 손실) theo mọi parameters. Backpropagation là efficient ứng dụng (application / 애플리케이션) của chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên computation đồ thị (graph / 그래프), không phải một học tập (learning / 학습) quy tắc (rule / 규칙) bí ẩn độc lập khỏi calculus.


> **Chuyển mạch:** Từ **Forward pass và mất mát (loss / 손실)**, ta sang **độ dốc (gradient / 기울기) descent** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ dốc (gradient / 기울기) descent

Parameters cập nhật (update / 업데이트) theo hướng giảm mất mát (loss / 손실):

\[
\theta \leftarrow \theta - \eta \nabla_\theta L
\]

Học tập (learning / 학습) tỷ lệ (rate / 비율) `η` quá lớn có thể diverge; quá nhỏ huấn luyện (training / 학습) chậm. Adaptive optimizers như Adam điều chỉnh cập nhật (update / 업데이트) dựa moments của gradients.

Tối ưu hóa (optimization / 최적화) landscape non-convex; chính xác (exact / 정확한) toàn cục (global / 전역) optimum không thường là yêu cầu (requirement / 요구사항) để generalize tốt.


> **Chuyển mạch:** Từ **độ dốc (gradient / 기울기) descent**, ta sang **Batch và stochasticity** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Batch và stochasticity

Full-batch độ dốc (gradient / 기울기) dùng toàn dataset mỗi step; SGD/minibatch dùng subset, giảm per-step chi phí (cost / 비용) và thêm noise có thể giúp exploration/generalization.

Batch kích thước (size / 크기) ảnh hưởng bộ nhớ (memory / 메모리), thông lượng (throughput / 처리량) và tối ưu hóa (optimization / 최적화) dynamics.


> **Chuyển mạch:** Từ **Batch và stochasticity**, ta sang **CNN intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## CNN intuition

Convolutional neural networks khai thác locality và weight sharing trên grid-like dữ liệu (data / 데이터) như images. Same filter dùng ở nhiều positions tạo translation-related inductive độ lệch (bias / 편향).


> **Chuyển mạch:** Từ **CNN intuition**, ta sang **chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention

RNN xử lý trạng thái (state / 상태) theo chuỗi (sequence / 시퀀스) nhưng khó parallelize dài và có độ dốc (gradient / 기울기) issues. Attention cho mỗi position tính weighted tương tác (interaction / 상호작용) với positions khác.

Transformer dùng self-attention + feed-forward blocks và positional thông tin (information / 정보), trở thành kiến trúc (architecture / 아키텍처) nền cho ngôn ngữ (language / 언어)/vision/multimodal các mô hình (models / 모델들).


> **Chuyển mạch:** Từ **chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention**, ta sang **Embeddings** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Embeddings

Embedding map discrete symbols/items vào vectors sao cho hình học (geometry / 기하학) phản ánh learned relationships theo huấn luyện (training / 학습) mục tiêu (objective / 목표).

Similarity trong embedding không gian (space / 공간) là model-dependent. Cosine gần không có nghĩa entities “giống nhau mọi nghĩa”; chỉ theo biểu diễn (representation / 표현) learned.


> **Chuyển mạch:** Từ **Embeddings**, ta sang **sức chứa (capacity / 용량) và scaling** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sức chứa (capacity / 용량) và scaling

Tăng parameters/dữ liệu (data / 데이터)/compute có thể cải thiện hiệu năng (performance / 성능) nhưng chi phí (cost / 비용) năng lượng (energy / 에너지), độ trễ (latency / 지연 시간) và bộ nhớ (memory / 메모리) tăng. Quantization, pruning, distillation và efficient architectures trade accuracy/compute.


> **Chuyển mạch:** Từ **sức chứa (capacity / 용량) và scaling**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Neural mạng (network / 네트워크) học giống não.”** Inspiration lịch sử không đồng nghĩa biological fidelity.

**“Deep học tập (learning / 학습) không cần tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링).”** kiến trúc (architecture / 아키텍처), tokenization, preprocessing, labels và mục tiêu (objective / 목표) vẫn encode các giả định (assumptions / 가정들).

**“Attention là explanation.”** Attention weights không tự động là nhân quả (causal / 인과적) explanation của mô hình (model / 모델) quyết định (decision / 결정).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Deep mạng (network / 네트워크) là differentiable program whose nội bộ (internal / 내부) biểu diễn (representation / 표현) được học bằng gradient-based tối ưu hóa (optimization / 최적화) để phục vụ mục tiêu (objective / 목표) trên dữ liệu (data / 데이터).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [linear algebra](../../../mathematics/04_vectors_linear_algebra/01_matrices_and_linear_systems.md), [matrix calculus/autodiff](../../../mathematics/04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md), [gradient descent](../../../mathematics/08_optimization_numerical/01_gradient_descent_and_convexity.md) và [ML foundations](./02_machine_learning_foundations.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 ai problem formulation search and agents](./00_ai_problem_formulation_search_and_agents.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
