# Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Bắt đầu từ chuỗi (chain / 사슬) quy tắc (rule / 규칙)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Một scalar example** để đem mô hình vào tình huống cụ thể. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Backpropagation (역전파 / lan truyền ngược) thường bị mô tả như “thuật toán giúp neural mạng (network / 네트워크) học”. Chính xác hơn, backpropagation là một **efficient thuật toán (algorithm / 알고리즘) để tính gradients của một scalar đầu ra (output / 출력), thường là mất mát (loss / 손실), đối với rất nhiều intermediate values và parameters trong computational đồ thị (graph / 그래프)**.

Học tập (learning / 학습) còn cần optimizer dùng gradients để cập nhật (update / 업데이트) parameters. Backprop chỉ trả lời:

> Nếu parameter thay đổi rất nhỏ, mất mát (loss / 손실) sẽ thay đổi theo hướng và mức nào?

## Bắt đầu từ chuỗi (chain / 사슬) quy tắc (rule / 규칙)

Nếu:

\[
y=f(u),\qquad u=g(x)
\]

thì:

\[
\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}
\]

Neural mạng (network / 네트워크) chỉ là composition lớn hơn:

\[
L=f_L(f_{L-1}(...f_1(x)))
\]

Backprop áp dụng chuỗi (chain / 사슬) quy tắc (rule / 규칙) theo reverse topological thứ tự (order / 순서) của computation đồ thị (graph / 그래프).

> **Chuyển mạch:** Trong **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Bắt đầu từ chuỗi (chain / 사슬) quy tắc (rule / 규칙)** cho ta quy tắc; **Một scalar example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Reverse-Mode Automatic Differentiation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một scalar example

Giả sử:

\[
z=wx+b
\]

\[
\hat y=\sigma(z)
\]

\[
L=\frac12(\hat y-y)^2
\]

Muốn độ dốc (gradient / 기울기) theo `w`:

\[
\frac{\partial L}{\partial w}
=\frac{\partial L}{\partial \hat y}
\frac{\partial \hat y}{\partial z}
\frac{\partial z}{\partial w}
\]

Từng factor:

\[
\frac{\partial L}{\partial \hat y}=\hat y-y
\]

\[
\frac{\partial \hat y}{\partial z}=\sigma(z)(1-\sigma(z))
\]

\[
\frac{\partial z}{\partial w}=x
\]

nên:

\[
\frac{\partial L}{\partial w}=(\hat y-y)\sigma(z)(1-\sigma(z))x
\]

Không có magic. Đây chỉ là chuỗi (chain / 사슬) quy tắc (rule / 규칙) qua các operations đã chạy ở forward pass.

> **Chuyển mạch:** Ở chặng này của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Một scalar example** cho ta quy tắc; **Reverse-Mode Automatic Differentiation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cục bộ (local / 로컬) gradients và upstream độ dốc (gradient / 기울기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reverse-Mode Automatic Differentiation

Nếu có millions parameters nhưng chỉ một scalar mất mát (loss / 손실), ta cần derivatives:

\[
\frac{\partial L}{\partial \theta_1},...,
\frac{\partial L}{\partial \theta_m}
\]

Reverse-mode AD cực hiệu quả vì một backward traversal có thể compute độ dốc (gradient / 기울기) cho tất cả parameters với chi phí (cost / 비용) cùng thứ tự (order / 순서) với forward pass, thường vài lần forward chi phí (cost / 비용) chứ không `m` forward passes.

Backpropagation trong neural networks là ứng dụng (application / 애플리케이션) đặc biệt của reverse-mode automatic differentiation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Cục bộ (local / 로컬) gradients và upstream độ dốc (gradient / 기울기)** tiếp nhận điểm tựa từ **Reverse-Mode Automatic Differentiation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Branching đồ thị (graph / 그래프) và độ dốc (gradient / 기울기) accumulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cục bộ (local / 로컬) gradients và upstream độ dốc (gradient / 기울기)

Mỗi thao tác (operation / 연산) chỉ cần biết:

1. cục bộ (local / 로컬) derivative của đầu ra (output / 출력) theo inputs;
2. độ dốc (gradient / 기울기) đã truyền từ downstream.

Ví dụ `z=a+b`:

\[
\frac{\partial z}{\partial a}=1,\qquad \frac{\partial z}{\partial b}=1
\]

Nếu upstream độ dốc (gradient / 기울기) là:

\[
\bar z=\frac{\partial L}{\partial z}
\]

thì:

\[
\bar a=\bar z,
\qquad
\bar b=\bar z
\]

Với multiply `z=ab`:

\[
\bar a=\bar z\cdot b,
\qquad
\bar b=\bar z\cdot a
\]

Autograd frameworks compose thousands such cục bộ (local / 로컬) rules.

> **Chuyển mạch:** Trong **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Branching đồ thị (graph / 그래프) và độ dốc (gradient / 기울기) accumulation** tiếp nhận điểm tựa từ **Cục bộ (local / 로컬) gradients và upstream độ dốc (gradient / 기울기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Véc-tơ (vector / 벡터)/Jacobian perspective** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Branching đồ thị (graph / 그래프) và độ dốc (gradient / 기울기) accumulation

Nếu một tensor ảnh hưởng mất mát (loss / 손실) qua nhiều paths:

\[
L=f(x)+g(x)
\]

thì:

\[
\frac{dL}{dx}=f'(x)+g'(x)
\]

Backward phải **sum gradients từ mọi downstream paths**.

Đây là lý do frameworks accumulate gradients. Trong PyTorch, gọi `.backward()` nhiều lần mà không zero gradients có thể cộng độ dốc (gradient / 기울기) ngoài ý muốn — hoặc intentionally để độ dốc (gradient / 기울기) accumulation across mini-batches.

> **Chuyển mạch:** Ở chặng này của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Véc-tơ (vector / 벡터)/Jacobian perspective** tiếp nhận điểm tựa từ **Branching đồ thị (graph / 그래프) và độ dốc (gradient / 기울기) accumulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backprop qua tuyến tính (linear / 선형) tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Véc-tơ (vector / 벡터)/Jacobian perspective

Nếu hàm (function / 함수):

\[
y=f(x)
\]

với vectors, derivative là Jacobian:

\[
J_{ij}=\frac{\partial y_i}{\partial x_j}
\]

Nhưng backprop không cần materialize full Jacobian khổng lồ. Nó computes **vector-Jacobian products (VJP)** efficiently.

Nếu upstream độ dốc (gradient / 기울기) `v=∂L/∂y`, backward computes:

\[
v^TJ
\]

mà không xây `J` đầy đủ.

Điều này cực quan trọng cho bộ nhớ (memory / 메모리)/compute feasibility.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Backprop qua tuyến tính (linear / 선형) tầng (layer / 계층)** tiếp nhận điểm tựa từ **Véc-tơ (vector / 벡터)/Jacobian perspective** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backprop qua activation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backprop qua tuyến tính (linear / 선형) tầng (layer / 계층)

Batch form:

\[
Z=XW^T+b
\]

Nếu upstream:

\[
G_Z=\frac{\partial L}{\partial Z}
\]

thì:

\[
\frac{\partial L}{\partial W}=G_Z^TX
\]

\[
\frac{\partial L}{\partial X}=G_ZW
\]

\[
\frac{\partial L}{\partial b}=\sum_{batch}G_Z
\]

Đây là ma trận (matrix / 행렬) multiplications — lý do GPU rất phù hợp cả forward và backward.

> **Chuyển mạch:** Trong **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Backprop qua activation** tiếp nhận điểm tựa từ **Backprop qua tuyến tính (linear / 선형) tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sigmoid + Cross-Entropy simplification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backprop qua activation

Elementwise activation:

\[
h=\phi(z)
\]

thì:

\[
\frac{\partial L}{\partial z}
=rac{\partial L}{\partial h}\odot\phi'(z)
\]

Nếu `φ'(z)` thường gần zero, độ dốc (gradient / 기울기) shrink. Đây là vanishing-gradient liên kết (connection / 연결).

> **Chuyển mạch:** Ở chặng này của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Sigmoid + Cross-Entropy simplification** tiếp nhận điểm tựa từ **Backprop qua activation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vanishing Gradients** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sigmoid + Cross-Entropy simplification

Nhị phân (binary / 이진) sigmoid:

\[
p=\sigma(z)
\]

BCE mất mát (loss / 손실):

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

Derivative simplifies đẹp:

\[
\frac{\partial L}{\partial z}=p-y
\]

Softmax + cross-entropy multiclass cũng có analogous kết quả (result / 결과):

\[
\frac{\partial L}{\partial z_k}=p_k-y_k
\]

Sự cancellation này giúp độ dốc (gradient / 기울기) hành vi (behavior / 동작) và numerical hiện thực (implementation / 구현) tốt hơn việc treat từng khối (block / 블록) naive.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Vanishing Gradients** tiếp nhận điểm tựa từ **Sigmoid + Cross-Entropy simplification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exploding Gradients** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vanishing Gradients

Độ dốc (gradient / 기울기) qua độ sâu (depth / 깊이) là sản phẩm (product / 제품) của many Jacobians:

\[
\frac{\partial L}{\partial h^{(l)}}
=J_{l+1}^TJ_{l+2}^T...J_L^T
\frac{\partial L}{\partial h^{(L)}}
\]

Nếu norms thường <1, sản phẩm (product / 제품) shrink exponentially. Early layers nhận tín hiệu (signal / 신호) rất nhỏ.

Sigmoid/tanh saturation làm bài toán (problem / 문제) nặng hơn.

Solutions/lịch sử (history / 이력):

- ReLU-family activations;
- Xavier/He initialization;
- normalization;
- residual connections;
- gated architectures.

> **Chuyển mạch:** Trong **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Exploding Gradients** tiếp nhận điểm tựa từ **Vanishing Gradients** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Residual liên kết (connection / 연결) và độ dốc (gradient / 기울기) highway** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exploding Gradients

Nếu Jacobian products có norms >1 repeatedly, gradients explode. Symptoms:

- mất mát (loss / 손실) NaN/Inf;
- huge parameter cập nhật (update / 업데이트);
- unstable huấn luyện (training / 학습).

Mitigations:

- appropriate initialization;
- normalization;
- smaller học tập (learning / 학습) tỷ lệ (rate / 비율);
- độ dốc (gradient / 기울기) clipping.

Độ dốc (gradient / 기울기) norm clipping:

\[
g\leftarrow g\cdot\min\left(1,\frac{c}{\|g\|}\right)
\]

limits toàn cục (global / 전역) độ dốc (gradient / 기울기) norm to threshold `c`.

> **Chuyển mạch:** Ở chặng này của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, sau nội dung của **Exploding Gradients**, **Residual liên kết (connection / 연결) và độ dốc (gradient / 기울기) highway** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Độ dốc (gradient / 기울기) Checkpointing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Residual liên kết (connection / 연결) và độ dốc (gradient / 기울기) highway

Residual khối (block / 블록):

\[
y=x+F(x)
\]

Derivative:

\[
\frac{\partial y}{\partial x}=I+\frac{\partial F}{\partial x}
\]

Định danh (identity / 식별자) term tạo direct độ dốc (gradient / 기울기) đường dẫn (path / 경로), giúp very deep networks trainable hơn.

Transformers và ResNets đều phụ thuộc insight này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Độ dốc (gradient / 기울기) Checkpointing** tiếp nhận điểm tựa từ **Residual liên kết (connection / 연결) và độ dốc (gradient / 기울기) highway** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Stop độ dốc (gradient / 기울기) / Detach** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) Checkpointing

Backward cần activations từ forward. Nếu mô hình (model / 모델) lớn, bộ nhớ (memory / 메모리) cao.

Checkpointing chỉ store một số activations; backward recompute missing forward segments.

Sự đánh đổi (trade-off / 트레이드오프):

```text
less memory
↔
more compute
```

Đây là các hệ thống (systems / 시스템들) consequence trực tiếp của backprop phụ thuộc (dependency / 의존성).

> **Chuyển mạch:** Trong **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Stop độ dốc (gradient / 기울기) / Detach** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) Checkpointing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Higher-Order Gradients** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stop độ dốc (gradient / 기울기) / Detach

Đôi khi muốn giá trị (value / 값) participate forward nhưng không receive độ dốc (gradient / 기울기).

`detach` / stop-gradient tạo ranh giới (boundary / 경계) trong đồ thị (graph / 그래프).

Use cases:

- mục tiêu (target / 대상) networks;
- contrastive học tập (learning / 학습) tricks;
- teacher-student setup;
- preventing unwanted parameter updates.

Dùng sai có thể silently break học tập (learning / 학습).

> **Chuyển mạch:** Ở chặng này của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Higher-Order Gradients** tiếp nhận điểm tựa từ **Stop độ dốc (gradient / 기울기) / Detach** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backprop không phải biologically plausible explanation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Higher-Order Gradients

Backprop thường compute first-order gradients. Một số algorithms cần độ dốc (gradient / 기울기) of độ dốc (gradient / 기울기), Hessian-vector products hoặc meta-learning derivatives.

Khung phần mềm (framework / 프레임워크) có thể bản dựng (build / 빌드) đồ thị (graph / 그래프) of backward computation nếu configured, nhưng bộ nhớ (memory / 메모리)/compute tăng mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Backprop không phải biologically plausible explanation** tiếp nhận điểm tựa từ **Higher-Order Gradients** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ dốc (gradient / 기울기) không phải explanation của mô hình (model / 모델) prediction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backprop không phải biologically plausible explanation

Backprop là computational tối ưu hóa (optimization / 최적화) thuật toán (algorithm / 알고리즘), không phải established mô hình (model / 모델) về cách biological brain learns. Research có biologically plausible alternatives, nhưng kỹ thuật (engineering / 엔지니어링) success của backprop không chứng minh brain dùng same cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Trong **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Độ dốc (gradient / 기울기) không phải explanation của mô hình (model / 모델) prediction** tiếp nhận điểm tựa từ **Backprop không phải biologically plausible explanation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Debugging gradients** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) không phải explanation của mô hình (model / 모델) prediction

Độ dốc (gradient / 기울기) `∂output/∂input` có thể dùng saliency, nhưng độ dốc (gradient / 기울기) chỉ cục bộ (local / 로컬) sensitivity. Nó không automatically là nhân quả (causal / 인과적) explanation hay full lập luận (reasoning / 추론) dấu vết (trace / 추적).

> **Chuyển mạch:** Ở chặng này của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Debugging gradients** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) không phải explanation của mô hình (model / 모델) prediction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Debugging gradients

Useful diagnostics:

- độ dốc (gradient / 기울기) norm per tầng (layer / 계층);
- parameter norm/cập nhật (update / 업데이트) ratio;
- percent zero độ dốc (gradient / 기울기);
- NaN/Inf;
- exploding/vanishing across độ sâu (depth / 깊이).

Finite-difference độ dốc (gradient / 기울기) check cho small mạng (network / 네트워크):

\[
\frac{\partial L}{\partial \theta}
\approx
\frac{L(\theta+\epsilon)-L(\theta-\epsilon)}{2\epsilon}
\]

có thể verify custom backward hiện thực (implementation / 구현). Không dùng cho large-scale huấn luyện (training / 학습) vì expensive/numerically sensitive.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Debugging gradients** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Forward:
parameters → intermediate values → loss

Backward:
loss sensitivity
← local derivative
← local derivative
← ...
→ gradient for every parameter
```

Backprop không “biết” cách sửa mô hình (model / 모델) theo ý nghĩa (semantic meaning / 의미적 뜻). Nó chỉ propagate quantitative credit/blame defined bởi mất mát (loss / 손실) và computation đồ thị (graph / 그래프).

> **Chuyển mạch:** Trong **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Backpropagation = độ dốc (gradient / 기울기) Descent”

Backprop tính gradients. độ dốc (gradient / 기울기) Descent/Adam dùng gradients để cập nhật (update / 업데이트).

### “Autograd nghĩa không cần hiểu derivatives”

Không hiểu độ dốc (gradient / 기울기) luồng (flow / 흐름) khiến khó gỡ lỗi (debug / 디버그) saturation, detach, exploding độ dốc (gradient / 기울기), custom operations và huấn luyện (training / 학습) instability.

### “độ dốc (gradient / 기울기) lớn nghĩa tính năng (feature / 기능) quan trọng”

Độ dốc (gradient / 기울기) là cục bộ (local / 로컬) sensitivity, phụ thuộc quy mô (scale / 규모)/điểm (point / 지점)/mô hình (model / 모델); không tự động là toàn cục (global / 전역) importance.

### “Backward pass lưu toàn bộ Jacobian”

Reverse-mode AD dùng VJP/cục bộ (local / 로컬) rules để tránh materialize full Jacobians.

> **Chuyển mạch:** Ở chặng này của **Backpropagation: chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên Computational đồ thị (graph / 그래프)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Calculus for AI](../01_mathematical_foundations/04_calculus_for_ai.md), [Forward Propagation](./03_forward_propagation.md) và tiếp theo [Gradient Descent and Optimizers](./05_gradient_descent_and_optimizers.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
