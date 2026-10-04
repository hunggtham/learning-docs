# Neural Networks kiến thức (knowledge / 지식) tầng (layer / 계층)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Neural Networks kiến thức (knowledge / 지식) tầng (layer / 계층)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Phụ thuộc (dependency / 의존성) map** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Chapters** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của neural networks, rồi nối representation, optimization, generalization và deployment.

Folder này giải thích Neural Networks (신경망 / mạng nơ-ron) như một **parameterized differentiable computation hệ thống (system / 시스템)**, không như một collection khung phần mềm (framework / 프레임워크) APIs. Nó nối trực tiếp Machine học tập (learning / 학습), tuyến tính (linear / 선형) Algebra, Calculus và tối ưu hóa (optimization / 최적화) với Deep học tập (learning / 학습) architectures phía sau.

## Phụ thuộc (dependency / 의존성) map

Sơ đồ hoặc danh sách này mô tả thứ tự phụ thuộc của các khái niệm. Hãy đọc theo mũi tên để biết phần nào là prerequisite, phần nào là ứng dụng và khi nào cần quay lại nền tảng.

```mermaid
flowchart TD
    A[00 From Linear Models to Neural Networks] --> B[01 Neuron, Perceptron & MLP]
    B --> C[02 Activation Functions]
    C --> D[03 Forward Propagation]
    D --> E[04 Backpropagation]
    E --> F[05 Gradient Descent & Optimizers]
    C --> G[06 Initialization & Normalization]
    E --> G
    F --> G
    G --> H[07 Regularization]
    H --> I[08 Representation Learning]
    F --> J[09 Training Dynamics]
    G --> J
    H --> J
    I --> J
```

> **Chuyển mạch:** **Dependency map** đưa người học từ tensor và gradient đến architecture; **Mental model của toàn tầng** giữ liên hệ giữa representation, optimization và failure mode.

## Chapters

**[00 — From Linear Models to Neural Networks](./00_from_linear_models_to_neural_networks.md)** giải thích vì sao ngăn xếp (stack / 스택) tuyến tính (linear / 선형) layers không có nonlinearity vẫn collapse thành một tuyến tính (linear / 선형) transformation, XOR và biểu diễn (representation / 표현) học tập (learning / 학습) motivation.

**[01 — Neuron, Perceptron & MLP](./01_neuron_perceptron_and_mlp.md)** đi từ weighted sum + activation tới multilayer biểu diễn (representation / 표현), tensor shape, parameter count và output-head ngữ nghĩa (semantics / 의미론).

**[02 — Activation Functions](./02_activation_functions.md)** giải thích sigmoid/tanh/ReLU/GELU/SiLU/SwiGLU qua expressivity, saturation, độ dốc (gradient / 기울기) luồng (flow / 흐름) và kiến trúc (architecture / 아키텍처) ngữ cảnh (context / 맥락).

**[03 — Forward Propagation](./03_forward_propagation.md)** xem mô hình (model / 모델) như computational đồ thị (graph / 그래프), bao gồm batching, broadcasting, train/eval hành vi (behavior / 동작), activation bộ nhớ (memory / 메모리), checkpointing và mixed precision.

**[04 — Backpropagation](./04_backpropagation.md)** derivation chuỗi (chain / 사슬) quy tắc (rule / 규칙)/reverse-mode AD, vector-Jacobian products, độ dốc (gradient / 기울기) accumulation, vanishing/exploding độ dốc (gradient / 기울기) và residual độ dốc (gradient / 기울기) paths.

**[05 — Gradient Descent & Optimizers](./05_gradient_descent_and_optimizers.md)** nối SGD, momentum, Adam/AdamW, schedules, warmup, batch kích thước (size / 크기), clipping và optimizer-state bộ nhớ (memory / 메모리).

**[06 — Initialization & Normalization](./06_initialization_and_normalization.md)** giải thích Xavier/He, BatchNorm, LayerNorm, RMSNorm, Pre-Norm/Post-Norm và tín hiệu (signal / 신호) statistics.

**[07 — Regularization](./07_regularization.md)** cover weight decay, dropout, early stopping, augmentation, label smoothing, kiến trúc (architecture / 아키텍처) độ lệch (bias / 편향), pretraining và LoRA như constrained adaptation.

**[08 — Representation Learning](./08_representation_learning.md)** đi từ embedding hình học (geometry / 기하학), contrastive học tập (learning / 학습), chỉ số (metric / 지표) học tập (learning / 학습), autoencoder, transfer, collapse, invariance/equivariance tới biểu diễn (representation / 표현) drift trong môi trường vận hành (production / 운영 환경).

**[09 — Training Dynamics](./09_deep_learning_training_dynamics.md)** tổng hợp học tập (learning / 학습) curves, cập nhật (update / 업데이트)/độ dốc (gradient / 기울기)/activation diagnostics, curriculum/dữ liệu (data / 데이터) mixture, catastrophic forgetting, checkpointing, phân tán (distributed / 분산) batch và systematic debugging.

> **Chuyển mạch:** Ở chặng này của **Neural Networks kiến thức (knowledge / 지식) tầng (layer / 계층)**, **Mô hình tư duy (mental model / 사고 모델) của toàn tầng (layer / 계층)** gom các mảnh từ **Chapters** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Chuyển tiếp sang Deep học tập (learning / 학습) Architectures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델) của toàn tầng (layer / 계층)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Input representation
      ↓
Parameterized computation graph
      ↓ forward
Prediction / loss
      ↓ backward
Gradients
      ↓ optimizer + schedule
Updated parameters
      ↓ repeated experience
Learned internal representation
```

Kiến trúc (architecture / 아키텍처) quyết định đồ thị (graph / 그래프) và inductive độ lệch (bias / 편향). mất mát (loss / 손실) quyết định tín hiệu (signal / 신호). Backprop tính credit/blame. Optimizer quyết định cập nhật (update / 업데이트) trajectory. dữ liệu (data / 데이터) phân phối (distribution / 분포) quyết định experience. Generalization vẫn phải được chứng minh bằng evaluation ngoài huấn luyện (training / 학습) set.

> **Chuyển mạch:** **Mental model** đã làm rõ layer, gradient và inductive bias; **Deep Learning Architectures** mở rộng chúng thành CNN, sequence và attention theo từng owner kỹ thuật.

## Chuyển tiếp sang Deep học tập (learning / 학습) Architectures

`06_deep_learning_architectures/` sẽ trả lời câu hỏi: nếu MLP general-purpose như vậy, vì sao cần CNN, RNN, attention, Transformer, Autoencoder, VAE, GAN và Diffusion?

Câu trả lời là **structure và inductive bias**. Image có local spatial structure; sequence có temporal/order dependency; generative modeling cần probabilistic/data-generation objectives khác nhau. Các architecture mới không bỏ core neural-network mechanics ở folder này; chúng tổ chức computation graph theo những assumptions hiệu quả hơn.

> **Bàn giao:** Sau **Chuyển tiếp sang Deep học tập (learning / 학습) Architectures**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
