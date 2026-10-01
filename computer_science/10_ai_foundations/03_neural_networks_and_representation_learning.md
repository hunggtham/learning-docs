# Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Neuron như affine transform + nonlinearity** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Layers và representations** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Neural mạng (network / 네트워크) là parameterized hàm (function / 함수) composition có khả năng học nonlinear representations từ dữ liệu (data / 데이터). Tên “neural” lấy cảm hứng sinh học lịch sử nhưng hiện đại (modern / 현대적) deep học tập (learning / 학습) nên được hiểu bằng tuyến tính (linear / 선형) algebra, nonlinear functions, tối ưu hóa (optimization / 최적화) và dữ liệu (data / 데이터)—not như mô phỏng não đầy đủ.

## Neuron như affine transform + nonlinearity

Một đơn vị (unit / 단위) cơ bản tính:

\[
z = w^T x + b,
\qquad a = \phi(z)
\]

Nếu chỉ ngăn xếp (stack / 스택) tuyến tính (linear / 선형) layers không có nonlinear activation, toàn mạng (network / 네트워크) vẫn collapse thành một tuyến tính (linear / 선형) transformation. Nonlinearity tạo khả năng biểu diễn functions phức tạp.

> **Chuyển mạch:** Neuron là affine transform cộng nonlinearity; layers ghép các biến đổi thành representation, rồi forward pass tạo prediction để loss đo sai lệch cần tối ưu.

## Layers và representations

Early layers có thể học cục bộ (local / 로컬)/simple patterns; deeper layers compose thành higher-level features. Nhưng interpretation không phải luôn human-readable.

Biểu diễn (representation / 표현) học tập (learning / 학습) giảm nhu cầu hand-engineer features, đổi lại cần dữ liệu (data / 데이터)/compute và làm nội bộ (internal / 내부) hành vi (behavior / 동작) khó giải thích hơn.

> **Chuyển mạch:** Ở chặng này của **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **Forward pass và mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Layers và representations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ dốc (gradient / 기울기) descent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Forward pass và mất mát (loss / 손실)

Đầu vào (input / 입력) đi qua layers tạo prediction. mất mát (loss / 손실) so prediction với mục tiêu (target / 대상)/mục tiêu (objective / 목표).

Huấn luyện (training / 학습) cần độ dốc (gradient / 기울기) của mất mát (loss / 손실) theo mọi parameters. Backpropagation là efficient ứng dụng (application / 애플리케이션) của chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên computation đồ thị (graph / 그래프), không phải một học tập (learning / 학습) quy tắc (rule / 규칙) bí ẩn độc lập khỏi calculus.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **Độ dốc (gradient / 기울기) descent** tiếp nhận điểm tựa từ **Forward pass và mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch và stochasticity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) descent

Parameters cập nhật (update / 업데이트) theo hướng giảm mất mát (loss / 손실):

\[
\theta \leftarrow \theta - \eta \nabla_\theta L
\]

Học tập (learning / 학습) tỷ lệ (rate / 비율) `η` quá lớn có thể diverge; quá nhỏ huấn luyện (training / 학습) chậm. Adaptive optimizers như Adam điều chỉnh cập nhật (update / 업데이트) dựa moments của gradients.

Tối ưu hóa (optimization / 최적화) landscape non-convex; chính xác (exact / 정확한) toàn cục (global / 전역) optimum không thường là yêu cầu (requirement / 요구사항) để generalize tốt.

> **Chuyển mạch:** Trong **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **Batch và stochasticity** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) descent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CNN intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch và stochasticity

Full-batch độ dốc (gradient / 기울기) dùng toàn dataset mỗi step; SGD/minibatch dùng subset, giảm per-step chi phí (cost / 비용) và thêm noise có thể giúp exploration/generalization.

Batch kích thước (size / 크기) ảnh hưởng bộ nhớ (memory / 메모리), thông lượng (throughput / 처리량) và tối ưu hóa (optimization / 최적화) dynamics.

> **Chuyển mạch:** Ở chặng này của **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **CNN intuition** tiếp nhận điểm tựa từ **Batch và stochasticity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CNN intuition

Convolutional neural networks khai thác locality và weight sharing trên grid-like dữ liệu (data / 데이터) như images. Same filter dùng ở nhiều positions tạo translation-related inductive độ lệch (bias / 편향).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **CNN intuition** xác định đầu vào; **Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention

RNN xử lý trạng thái (state / 상태) theo chuỗi (sequence / 시퀀스) nhưng khó parallelize dài và có độ dốc (gradient / 기울기) issues. Attention cho mỗi position tính weighted tương tác (interaction / 상호작용) với positions khác.

Transformer dùng self-attention + feed-forward blocks và positional thông tin (information / 정보), trở thành kiến trúc (architecture / 아키텍처) nền cho ngôn ngữ (language / 언어)/vision/multimodal các mô hình (models / 모델들).

> **Chuyển mạch:** Trong **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và attention** xác định đầu vào; **Embeddings** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Sức chứa (capacity / 용량) và scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Embeddings

Embedding map discrete symbols/items vào vectors sao cho hình học (geometry / 기하학) phản ánh learned relationships theo huấn luyện (training / 학습) mục tiêu (objective / 목표).

Similarity trong embedding không gian (space / 공간) là model-dependent. Cosine gần không có nghĩa entities “giống nhau mọi nghĩa”; chỉ theo biểu diễn (representation / 표현) learned.

> **Chuyển mạch:** Ở chặng này của **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **Sức chứa (capacity / 용량) và scaling** tiếp nhận điểm tựa từ **Embeddings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức chứa (capacity / 용량) và scaling

Tăng parameters/dữ liệu (data / 데이터)/compute có thể cải thiện hiệu năng (performance / 성능) nhưng chi phí (cost / 비용) năng lượng (energy / 에너지), độ trễ (latency / 지연 시간) và bộ nhớ (memory / 메모리) tăng. Quantization, pruning, distillation và efficient architectures trade accuracy/compute.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Sức chứa (capacity / 용량) và scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Neural mạng (network / 네트워크) học giống não.”** Inspiration lịch sử không đồng nghĩa biological fidelity.

**“Deep học tập (learning / 학습) không cần tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링).”** kiến trúc (architecture / 아키텍처), tokenization, preprocessing, labels và mục tiêu (objective / 목표) vẫn encode các giả định (assumptions / 가정들).

**“Attention là explanation.”** Attention weights không tự động là nhân quả (causal / 인과적) explanation của mô hình (model / 모델) quyết định (decision / 결정).

> **Chuyển mạch:** Trong **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Deep mạng (network / 네트워크) là differentiable program whose nội bộ (internal / 내부) biểu diễn (representation / 표현) được học bằng gradient-based tối ưu hóa (optimization / 최적화) để phục vụ mục tiêu (objective / 목표) trên dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **Neural networks và biểu diễn (representation / 표현) học tập (learning / 학습)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [linear algebra](../../mathematics/04_vectors_linear_algebra/01_matrices_and_linear_systems.md), [matrix calculus/autodiff](../../mathematics/04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md), [gradient descent](../../mathematics/08_optimization_numerical/01_gradient_descent_and_convexity.md) và [ML foundations](./02_machine_learning_foundations.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
