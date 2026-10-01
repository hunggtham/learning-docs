# Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Định danh (identity / 식별자) activation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Sigmoid** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Activation hàm (function / 함수) thường được giới thiệu như một danh sách `sigmoid`, `tanh`, `ReLU`, `GELU`. Cách học đó dễ biến thành thuộc lòng. Bản chất sâu hơn là: activation quyết định **hình dạng transformation**, **độ dốc (gradient / 기울기) luồng (flow / 흐름)** và **statistical hành vi (behavior / 동작)** của hidden representations.

Nếu bỏ activation giữa các affine layers, toàn mạng (network / 네트워크) collapse thành một affine transformation. Vì vậy nonlinearity là điều kiện để độ sâu (depth / 깊이) tạo expressivity mới.

## Định danh (identity / 식별자) activation

\[
\phi(z)=z
\]

Không thêm nonlinearity. Hữu ích ở regression đầu ra (output / 출력) hoặc một số residual/projection khối (block / 블록), nhưng nếu mọi hidden tầng (layer / 계층) đều định danh (identity / 식별자) thì deep ngăn xếp (stack / 스택) vẫn tuyến tính (linear / 선형).

> **Chuyển mạch:** Trong **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Sigmoid** tiếp nhận điểm tựa từ **Định danh (identity / 식별자) activation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **tanh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sigmoid

\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]

Phạm vi (range / 범위) `(0,1)`. Derivative:

\[
\sigma'(z)=\sigma(z)(1-\sigma(z))
\]

Maximum derivative chỉ `0.25`; khi `|z|` lớn, derivative gần zero. Đây là **saturation**, gây vanishing gradients khi ngăn xếp (stack / 스택) sâu.

Sigmoid vẫn rất phù hợp ở nhị phân (binary / 이진) xác suất (probability / 확률) đầu ra (output / 출력) hoặc gates trong LSTM, nơi bounded giá trị (value / 값) có ngữ nghĩa (semantic / 의미적) rõ.

> **Chuyển mạch:** Ở chặng này của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **tanh** tiếp nhận điểm tựa từ **Sigmoid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ReLU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tanh

\[
tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}
\]

Phạm vi (range / 범위) `(-1,1)`, zero-centered hơn sigmoid.

Derivative:

\[
1-tanh^2(z)
\]

vẫn saturate khi magnitude lớn.

Historically tanh tốt hơn sigmoid cho hidden layers trong nhiều early networks, nhưng ReLU-family thường easier train deep feed-forward nets.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **ReLU** tiếp nhận điểm tựa từ **tanh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dying ReLU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ReLU

\[
ReLU(z)=\max(0,z)
\]

Derivative:

\[
ReLU'(z)=
\begin{cases}
0,&z<0\\
1,&z>0
\end{cases}
\]

Tại zero derivative convention tùy hiện thực (implementation / 구현), nhưng single điểm (point / 지점) không tạo issue lớn trong continuous huấn luyện (training / 학습).

Ưu điểm:

- không saturate ở positive side;
- computation đơn giản;
- sparse activations;
- độ dốc (gradient / 기울기) có thể luồng (flow / 흐름) tốt hơn sigmoid/tanh.

> **Chuyển mạch:** Trong **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Dying ReLU** tiếp nhận điểm tựa từ **ReLU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **GELU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dying ReLU

Nếu đơn vị (unit / 단위) rơi vào region `z<0` cho hầu hết inputs, độ dốc (gradient / 기울기) qua ReLU = 0 nên đơn vị (unit / 단위) có thể không recover. học tập (learning / 학습) tỷ lệ (rate / 비율) quá lớn hoặc bad initialization làm rủi ro (risk / 위험) tăng.

Variants:

**Leaky ReLU**:

\[
\phi(z)=\max(\alpha z,z)
\]

cho small negative slope.

**PReLU** học `α`.

**ELU/SELU** có smooth negative region với goals khác về activation statistics.

> **Chuyển mạch:** Ở chặng này của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **GELU** tiếp nhận điểm tựa từ **Dying ReLU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SiLU / Swish** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## GELU

Gaussian lỗi (error / 오류) tuyến tính (linear / 선형) đơn vị (unit / 단위) (GELU) phổ biến trong Transformers:

\[
GELU(x)=x\Phi(x)
\]

với `Φ` là CDF của tiêu chuẩn (standard / 표준) normal.

Intuitively, GELU gate đầu vào (input / 입력) smoothly theo magnitude thay vì hard zero như ReLU.

Approximation thường dùng:

\[
0.5x\left(1+tanh\left[\sqrt{2/\pi}(x+0.044715x^3)\right]\right)
\]

Transformer variants cũng dùng SiLU/SwiGLU.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **SiLU / Swish** tiếp nhận điểm tựa từ **GELU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gated tuyến tính (linear / 선형) Units và SwiGLU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SiLU / Swish

\[
SiLU(x)=x\sigma(x)
\]

Smooth, non-monotonic nhẹ ở negative region và được dùng trong nhiều hiện đại (modern / 현대적) architectures.

> **Chuyển mạch:** Trong **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Gated tuyến tính (linear / 선형) Units và SwiGLU** tiếp nhận điểm tựa từ **SiLU / Swish** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Softmax không phải hidden activation thông thường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gated tuyến tính (linear / 선형) Units và SwiGLU

Transformer feed-forward blocks hiện đại thường dùng gated activation:

\[
SwiGLU(x)=(xW_1)\odot SiLU(xW_2)
\]

rồi projection tiếp theo.

Gating cho phép multiplicative tương tác (interaction / 상호작용) giữa learned projections, tăng expressivity so với một activation scalar đơn giản.

> **Chuyển mạch:** Ở chặng này của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Softmax không phải hidden activation thông thường** tiếp nhận điểm tựa từ **Gated tuyến tính (linear / 선형) Units và SwiGLU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Activation và độ dốc (gradient / 기울기) luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Softmax không phải hidden activation thông thường

Softmax:

\[
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

biến véc-tơ (vector / 벡터) logits thành phân phối (distribution / 분포) sum=1. Nó thường dùng ở multiclass đầu ra (output / 출력) và attention weights, không làm hidden activation generic như ReLU/GELU.

Softmax couples dimensions: thay một logit ảnh hưởng probabilities của mọi classes.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Softmax không phải hidden activation thông thường** xác định đầu vào; **Activation và độ dốc (gradient / 기울기) luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Đầu ra (output / 출력) activation phải match mục tiêu (target / 대상)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Activation và độ dốc (gradient / 기울기) luồng (flow / 흐름)

Backprop qua chuỗi (chain / 사슬) sản phẩm (product / 제품):

\[
\frac{\partial L}{\partial h^{(l)}}=rac{\partial L}{\partial h^{(l+1)}}\frac{\partial h^{(l+1)}}{\partial h^{(l)}}
\]

Nếu derivatives liên tục <1 mạnh, độ dốc (gradient / 기울기) shrink qua độ sâu (depth / 깊이). Nếu Jacobian norms >1 liên tục, độ dốc (gradient / 기울기) có thể explode.

Activation choice tương tác với initialization, normalization, residual connections và kiến trúc (architecture / 아키텍처); không thể đánh giá riêng lẻ.

> **Chuyển mạch:** Trong **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Activation và độ dốc (gradient / 기울기) luồng (flow / 흐름)** xác định đầu vào; **Đầu ra (output / 출력) activation phải match mục tiêu (target / 대상)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Differentiability có bắt buộc tuyệt đối không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đầu ra (output / 출력) activation phải match mục tiêu (target / 대상)

Regression unbounded → thường định danh (identity / 식별자).

Nhị phân (binary / 이진) classification → sigmoid xác suất (probability / 확률) hoặc logits + numerically stable BCE-with-logits.

Mutually exclusive multiclass → softmax.

Multi-label → independent sigmoid per label.

Positive quantity → có thể softplus/exponential tùy probabilistic mô hình (model / 모델).

Variance parameter cần >0 → softplus thường useful.

Activation ở đầu ra (output / 출력) là một modeling giả định (assumption / 가정), không chỉ hiện thực (implementation / 구현) detail.

> **Chuyển mạch:** Ở chặng này của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Differentiability có bắt buộc tuyệt đối không?** tiếp nhận điểm tựa từ **Đầu ra (output / 출력) activation phải match mục tiêu (target / 대상)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Activation statistics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differentiability có bắt buộc tuyệt đối không?

Gradient-based huấn luyện (training / 학습) cần useful derivatives gần như mọi nơi, nhưng hàm (function / 함수) không cần differentiable tại mọi single điểm (point / 지점). ReLU là example.

Discrete operations như `argmax` thường không differentiable và được đặt ngoài huấn luyện (training / 학습) đường dẫn (path / 경로) hoặc xử lý bằng relaxations/estimators.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Activation statistics** tiếp nhận điểm tựa từ **Differentiability có bắt buộc tuyệt đối không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Why ReLU changed Deep học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Activation statistics

Nếu activations liên tục có mean/variance drift qua layers, tối ưu hóa (optimization / 최적화) khó. Initialization và normalization cố giữ quy mô (scale / 규모) tín hiệu (signal / 신호) hợp lý.

Self-normalizing networks từng thiết kế SELU + initialization để activation statistics converge về stable phạm vi (range / 범위) under các giả định (assumptions / 가정들).

Hiện đại (modern / 현대적) Transformers thường dựa LayerNorm/RMSNorm + residual pathways.

> **Chuyển mạch:** Trong **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Why ReLU changed Deep học tập (learning / 학습)** tiếp nhận điểm tựa từ **Activation statistics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why ReLU changed Deep học tập (learning / 학습)

ReLU không phải nguyên nhân duy nhất, nhưng cùng better initialization và GPUs, nó giảm saturation bài toán (problem / 문제) trong deep feed-forward/CNN networks, giúp huấn luyện (training / 학습) độ sâu (depth / 깊이) lớn hơn thực dụng.

Historical progress thường đến từ tương tác (interaction / 상호작용) của nhiều improvements, không single magic activation.

> **Chuyển mạch:** Ở chặng này của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Why ReLU changed Deep học tập (learning / 학습)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Activation hàm (function / 함수) là “shape điều khiển (control / 제어)” của learned transformation: nó quyết định tầng (layer / 계층) có thể bend biểu diễn (representation / 표현) không gian (space / 공간) thế nào và độ dốc (gradient / 기울기) đi qua transformation ra sao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “ReLU tốt nhất nên cứ dùng ReLU”

Kiến trúc (architecture / 아키텍처)/lĩnh vực (domain / 도메인) matter. Transformers thường dùng GELU/SiLU/SwiGLU; RNN gates dùng sigmoid/tanh.

### “Sigmoid lỗi thời”

Không. Nó vẫn natural cho Bernoulli đầu ra (output / 출력) và gating.

### “Softmax làm mô hình (model / 모델) confident hơn”

Softmax chỉ normalize logits; temperature/quy mô (scale / 규모) ảnh hưởng sharpness, không đảm bảo tính đúng đắn (correctness / 정확성)/calibration.

### “Activation chỉ ảnh hưởng expressivity”

Nó còn ảnh hưởng tối ưu hóa (optimization / 최적화), độ dốc (gradient / 기울기) luồng (flow / 흐름), activation statistics và numerical hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **Activation Functions: tại sao Neural mạng (network / 네트워크) cần Nonlinearity?**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Calculus](../01_mathematical_foundations/04_calculus_for_ai.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md), [Initialization and Normalization](./06_initialization_and_normalization.md).

Xem tiếp: [Forward Propagation](./03_forward_propagation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
