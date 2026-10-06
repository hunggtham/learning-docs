# Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ derivative một biến đến differential nhiều biến** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Độ dốc (gradient / 기울기)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối matrix calculus với Jacobian, Hessian và autodiff, để đạo hàm nhiều biến đi vào tối ưu và tính toán tự động.

Khi một hàm (function / 함수) nhận scalar và trả scalar, đạo hàm quen thuộc là một số. Nhưng trong tối ưu hóa (optimization / 최적화), machine học tập (learning / 학습), robotics, graphics và scientific computing, đầu vào (input / 입력) thường là véc-tơ (vector / 벡터) hoặc ma trận (matrix / 행렬) và đầu ra (output / 출력) cũng có thể là véc-tơ (vector / 벡터). Lúc đó câu hỏi “đạo hàm là gì?” cần được mở rộng thành **ma trận (matrix / 행렬) calculus (행렬 미적분)**.

Mục tiêu của ma trận (matrix / 행렬) calculus không phải tạo thêm ký hiệu phức tạp. Nó cung cấp ngôn ngữ để mô tả độ nhạy của một hệ nhiều biến: nếu từng đầu vào (input / 입력) thay đổi rất nhỏ, đầu ra (output / 출력) thay đổi theo hướng nào và mạnh đến mức nào?

## Từ derivative một biến đến differential nhiều biến

Với hàm (function / 함수) scalar

```math
f:\mathbb R\to\mathbb R,
```

derivative tại `x` là số `f'(x)` sao cho

```math
f(x+\Delta x)\approx f(x)+f'(x)\Delta x
```

khi `Δx` nhỏ.

Tư tưởng này quan trọng hơn công thức derivative. Derivative là **tuyến tính (linear / 선형) approximation tốt nhất ở cục bộ (local / 로컬) neighborhood**.

Với hàm (function / 함수) nhiều biến

```math
f:\mathbb R^n\to\mathbb R,
```

ta muốn một tuyến tính (linear / 선형) map biến perturbation `Δx` thành perturbation của đầu ra (output / 출력):

```math
f(x+\Delta x)\approx f(x)+\nabla f(x)^T\Delta x.
```

Độ dốc (gradient / 기울기) xuất hiện vì đầu ra (output / 출력) là scalar còn đầu vào (input / 입력) là véc-tơ (vector / 벡터).

> **Nối mạch:** Trong **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Độ dốc (gradient / 기울기)** nối từ **Từ derivative một biến đến differential nhiều biến** sang **Jacobian**, vì cơ chế trước tạo đầu vào cho bước sau.

## Độ dốc (gradient / 기울기)

Với

```math
x=(x_1,\dots,x_n)^T,
```

Độ dốc (gradient / 기울기) là

```math
\nabla f(x)=
\begin{bmatrix}
\partial f/\partial x_1\\
\vdots\\
\partial f/\partial x_n
\end{bmatrix}.
```

Độ dốc (gradient / 기울기) không đơn thuần là danh sách (list / 목록) partial derivatives. Trong Euclidean không gian (space / 공간) nó chỉ direction của mức tăng nhanh nhất của hàm (function / 함수), còn magnitude cho biết cục bộ (local / 로컬) sensitivity theo direction đó.

Ví dụ

```math
f(x)=x^Tx.
```

Vì

```math
f(x)=\sum_i x_i^2,
```

nên

```math
\nabla f(x)=2x.
```

Điều này giải thích vì sao L2 regularization tạo độ dốc (gradient / 기울기) kéo parameter về origin.

> **Nối mạch:** Ở chặng này của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Jacobian** nối từ **Độ dốc (gradient / 기울기)** sang **Ví dụ Jacobian**, vì cơ chế trước tạo đầu vào cho bước sau.

## Jacobian

Nếu

```math
f:\mathbb R^n\to\mathbb R^m,
```

thì mỗi đầu ra (output / 출력) thành phần (component / 컴포넌트) phụ thuộc vào nhiều đầu vào (input / 입력) components. **Jacobian (야코비안)** gom tất cả first-order partial derivatives vào một ma trận (matrix / 행렬):

```math
J_f(x)=
\begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}.
```

Kích thước của Jacobian là `m × n` nếu đầu vào (input / 입력) dimension là `n` và đầu ra (output / 출력) dimension là `m`.

Cục bộ (local / 로컬) approximation trở thành

```math
f(x+\Delta x)\approx f(x)+J_f(x)\Delta x.
```

Đây chính là tuyến tính (linear / 선형) transformation tốt nhất xấp xỉ hàm (function / 함수) nonlinear gần `x`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Jacobian** nêu quy tắc; **Ví dụ Jacobian** thử quy tắc trong tình huống, rồi **Chuỗi (chain / 사슬) quy tắc (rule / 규칙) ở dạng ma trận (matrix / 행렬)** mở rộng hệ quả.

## Ví dụ Jacobian

Xét

```math
f(x,y)=
\begin{bmatrix}
x^2y\\
\sin x+y
\end{bmatrix}.
```

Jacobian là

```math
J_f(x,y)=
\begin{bmatrix}
2xy & x^2\\
\cos x & 1
\end{bmatrix}.
```

Nếu đầu vào (input / 입력) dịch một lượng nhỏ `(Δx,Δy)`, ma trận (matrix / 행렬) này dự đoán first-order thay đổi (change / 변경) của cả hai đầu ra (output / 출력).

> **Nối mạch:** Trong **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Ví dụ Jacobian** nêu quy tắc; **Chuỗi (chain / 사슬) quy tắc (rule / 규칙) ở dạng ma trận (matrix / 행렬)** thử quy tắc trong tình huống, rồi **Hessian** mở rộng hệ quả.

## Chuỗi (chain / 사슬) quy tắc (rule / 규칙) ở dạng ma trận (matrix / 행렬)

Nếu

```math
x\xrightarrow{g}y\xrightarrow{f}z,
```

thì

```math
J_{f\circ g}(x)=J_f(g(x))J_g(x).
```

Thứ tự nhân ma trận (matrix / 행렬) phản ánh đúng luồng (flow / 흐름) của perturbation: perturbation ở `x` trước hết bị `J_g` biến đổi thành perturbation ở `y`, rồi `J_f` biến đổi tiếp thành perturbation ở `z`.

Đây chính là nền tảng toán học của backpropagation.

> **Nối mạch:** Ở chặng này của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Chuỗi (chain / 사슬) quy tắc (rule / 규칙) ở dạng ma trận (matrix / 행렬)** đặt đầu vào cho **Hessian**, rồi **Quadratic form** mở rộng hệ quả hoặc giới hạn liên quan.

## Hessian

Với scalar hàm (function / 함수) `f:R^n→R`, đạo hàm bậc hai được gom vào **Hessian (헤시안)**:

```math
H_f(x)=
\begin{bmatrix}
\frac{\partial^2f}{\partial x_1^2} & \cdots & \frac{\partial^2f}{\partial x_1\partial x_n}\\
\vdots & \ddots & \vdots\\
\frac{\partial^2f}{\partial x_n\partial x_1} & \cdots & \frac{\partial^2f}{\partial x_n^2}
\end{bmatrix}.
```

Độ dốc (gradient / 기울기) nói slope. Hessian nói slope đang thay đổi ra sao, tức cục bộ (local / 로컬) curvature.

Taylor approximation bậc hai là

```math
f(x+\Delta x)\approx f(x)+\nabla f(x)^T\Delta x+
\frac12\Delta x^T H_f(x)\Delta x.
```

Nếu Hessian positive definite tại stationary điểm (point / 지점), hàm (function / 함수) cục bộ (local / 로컬) cong lên theo mọi direction và điểm đó là strict cục bộ (local / 로컬) minimum. Nếu Hessian có cả positive và negative eigenvalues, stationary điểm (point / 지점) là saddle điểm (point / 지점).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Quadratic form** nối từ **Hessian** sang **Đạo hàm theo ma trận (matrix / 행렬)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quadratic form

Với

```math
f(x)=\frac12x^TAx+b^Tx+c
```

và `A` symmetric,

```math
\nabla f(x)=Ax+b,
```

```math
H_f(x)=A.
```

Quadratic functions đặc biệt quan trọng vì curvature là constant. Nhiều tối ưu hóa (optimization / 최적화) algorithms cục bộ (local / 로컬) xem nonlinear mục tiêu (objective / 목표) như một quadratic approximation.

> **Nối mạch:** Trong **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Đạo hàm theo ma trận (matrix / 행렬)** nối từ **Quadratic form** sang **Differential notation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đạo hàm theo ma trận (matrix / 행렬)

Giả sử

```math
f(X)=\operatorname{tr}(X^TAX).
```

Nếu `A` symmetric,

```math
\nabla_X f=2AX.
```

Ma trận (matrix / 행렬) calculus thường dùng dấu vết (trace / 추적) identities để biến expressions về dạng dễ differentiate. Một định danh (identity / 식별자) rất hữu ích là

```math
\operatorname{tr}(ABC)=\operatorname{tr}(BCA)=\operatorname{tr}(CAB).
```

Dấu vết (trace / 추적) cho phép đưa differential về dạng

```math
df=\operatorname{tr}(G^T dX),
```

sau đó đọc độ dốc (gradient / 기울기) `G`.

> **Nối mạch:** Ở chặng này của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Differential notation** nối từ **Đạo hàm theo ma trận (matrix / 행렬)** sang **Shape checking**, vì cơ chế trước tạo đầu vào cho bước sau.

## Differential notation

Thay vì ghi partial derivative trực tiếp, có thể làm việc với differential.

Nếu

```math
y=Ax,
```

thì

```math
dy=A\,dx.
```

Nếu

```math
f=x^TAx,
```

thì

```math
df=d(x^T)Ax+x^TA\,dx.
```

Sau biến đổi,

```math
df=x^T(A^T+A)dx.
```

nên

```math
\nabla f=(A+A^T)x.
```

Nếu `A` symmetric thì độ dốc (gradient / 기울기) trở thành `2Ax`.

Differential notation thường giảm lỗi transpose khi expression phức tạp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Shape checking** nối từ **Differential notation** sang **Forward-mode automatic differentiation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Shape checking

Trong ma trận (matrix / 행렬) calculus, kiểm tra shape là phương pháp debugging rất mạnh. Nếu `x∈R^n`, độ dốc (gradient / 기울기) của scalar theo `x` phải có `n` components. Nếu `f:R^n→R^m`, Jacobian phải ánh xạ perturbation dimension `n` sang đầu ra (output / 출력) perturbation dimension `m`.

Nếu một expression derivative tạo shape không phù hợp với vai trò tuyến tính (linear / 선형) map của nó, nhiều khả năng notation hoặc transpose đang sai.

> **Nối mạch:** Trong **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Forward-mode automatic differentiation** nối từ **Shape checking** sang **Reverse-mode automatic differentiation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Forward-mode automatic differentiation

**Automatic differentiation — AD (자동미분)** không phải symbolic differentiation và cũng không phải numerical finite difference.

Ý tưởng là decomposed computation thành elementary operations và propagate derivative chính xác theo chuỗi (chain / 사슬) quy tắc (rule / 규칙).

Ví dụ

```math
u=x^2,
```

```math
v=\sin u,
```

```math
y=3v.
```

Forward chế độ (mode / 모드) propagate cùng lúc giá trị (value / 값) và derivative:

```math
\dot u=2x\dot x,
```

```math
\dot v=\cos(u)\dot u,
```

```math
\dot y=3\dot v.
```

Nếu đầu vào (input / 입력) dimension nhỏ và đầu ra (output / 출력) dimension lớn, forward chế độ (mode / 모드) thường phù hợp.

> **Nối mạch:** Ở chặng này của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Reverse-mode automatic differentiation** nối từ **Forward-mode automatic differentiation** sang **Backpropagation là reverse-mode AD trên computational đồ thị (graph / 그래프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Reverse-mode automatic differentiation

Reverse chế độ (mode / 모드) trước tiên chạy computation forward để lưu intermediate values, sau đó đi ngược đồ thị (graph / 그래프) để propagate sensitivities từ đầu ra (output / 출력) về inputs.

Với scalar mất mát (loss / 손실) `L`, ta propagate các quantities dạng

```math
\bar x=\frac{\partial L}{\partial x}.
```

Mỗi thao tác (operation / 연산) cục bộ (local / 로컬) biết cách nhận upstream độ dốc (gradient / 기울기) và tạo downstream gradients.

Nếu

```math
y=f(x),
```

thì reverse chế độ (mode / 모드) thực hiện vector-Jacobian sản phẩm (product / 제품) thay vì materialize full Jacobian.

Đây là lý do reverse chế độ (mode / 모드) cực kỳ hiệu quả khi đầu ra (output / 출력) là một scalar mất mát (loss / 손실) còn mô hình (model / 모델) có hàng triệu parameters.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Backpropagation là reverse-mode AD trên computational đồ thị (graph / 그래프)** nối từ **Reverse-mode automatic differentiation** sang **Finite difference và vì sao không dùng để train mạng (network / 네트워크)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Backpropagation là reverse-mode AD trên computational đồ thị (graph / 그래프)

Trong neural mạng (network / 네트워크), layers tạo một computational đồ thị (graph / 그래프). Forward pass tính activations và mất mát (loss / 손실). Backward pass áp dụng chuỗi (chain / 사슬) quy tắc (rule / 규칙) từ mất mát (loss / 손실) về từng parameter.

Ví dụ tuyến tính (linear / 선형) tầng (layer / 계층)

```math
y=Wx+b
```

với upstream độ dốc (gradient / 기울기) `g=∂L/∂y` cho

```math
\frac{\partial L}{\partial x}=W^Tg,
```

```math
\frac{\partial L}{\partial W}=gx^T,
```

```math
\frac{\partial L}{\partial b}=g.
```

Ba công thức này không phải mẹo deep học tập (learning / 학습); chúng là ma trận (matrix / 행렬) chuỗi (chain / 사슬) quy tắc (rule / 규칙).

> **Nối mạch:** Trong **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Finite difference và vì sao không dùng để train mạng (network / 네트워크)** nối từ **Backpropagation là reverse-mode AD trên computational đồ thị (graph / 그래프)** sang **Jacobian-vector sản phẩm (product / 제품) và vector-Jacobian sản phẩm (product / 제품)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Finite difference và vì sao không dùng để train mạng (network / 네트워크)

Derivative có thể xấp xỉ bằng

```math
f'(x)\approx\frac{f(x+h)-f(x)}{h}.
```

Nhưng `h` quá lớn tạo truncation lỗi (error / 오류); `h` quá nhỏ tạo floating-point cancellation. Với hàng triệu parameters, finite difference còn yêu cầu số lần evaluate hàm (function / 함수) rất lớn.

Automatic differentiation tránh hai vấn đề đó bằng cách tính derivative qua algebra của computation đồ thị (graph / 그래프) ở machine precision.

> **Nối mạch:** Ở chặng này của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Jacobian-vector sản phẩm (product / 제품) và vector-Jacobian sản phẩm (product / 제품)** nối từ **Finite difference và vì sao không dùng để train mạng (network / 네트워크)** sang **Hessian-vector sản phẩm (product / 제품)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Jacobian-vector sản phẩm (product / 제품) và vector-Jacobian sản phẩm (product / 제품)

Trong các hệ thống (systems / 시스템들) lớn ta hiếm khi muốn materialize Jacobian đầy đủ.

Forward chế độ (mode / 모드) thường tính

```math
Jv,
```

nghĩa là tác động (effect / 효과) của perturbation direction `v` lên đầu ra (output / 출력).

Reverse chế độ (mode / 모드) thường tính

```math
v^TJ,
```

nghĩa là propagate sensitivity từ đầu ra (output / 출력) backward.

Cách nhìn này giải thích hiệu năng (performance / 성능) của hiện đại (modern / 현대적) autodiff frameworks tốt hơn việc tưởng rằng chúng xây một giant Jacobian ma trận (matrix / 행렬).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Hessian-vector sản phẩm (product / 제품)** nối từ **Jacobian-vector sản phẩm (product / 제품) và vector-Jacobian sản phẩm (product / 제품)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hessian-vector sản phẩm (product / 제품)

Second-order tối ưu hóa (optimization / 최적화) đôi khi cần curvature nhưng Hessian `n×n` quá lớn để materialize. Có thể tính trực tiếp

```math
Hv
```

bằng combinations của automatic differentiation mà không lưu toàn bộ Hessian.

Điều này quan trọng trong Newton-CG, curvature phân tích (analysis / 분석) và một số meta-learning methods.

> **Nối mạch:** Trong **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Hessian-vector sản phẩm (product / 제품)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Derivative nhiều chiều nên được hiểu như một **tuyến tính (linear / 선형) map của perturbations**. độ dốc (gradient / 기울기), Jacobian và Hessian chỉ là các representations khác nhau của cục bộ (local / 로컬) sensitivity và curvature. Automatic differentiation là kỹ thuật thực thi chuỗi (chain / 사슬) quy tắc (rule / 규칙) trên computational đồ thị (graph / 그래프) mà không cần viết symbolic derivative bằng tay.

> **Nối mạch:** Ở chặng này của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

Độ dốc (gradient / 기울기) không phải lúc nào cũng là “derivative duy nhất” của véc-tơ (vector / 벡터) hàm (function / 함수); vector-output hàm (function / 함수) tự nhiên có Jacobian. Backpropagation cũng không phải một thuật toán (algorithm / 알고리즘) tối ưu hóa (optimization / 최적화) riêng: nó là cách tính gradients. độ dốc (gradient / 기울기) descent mới là thuật toán (algorithm / 알고리즘) dùng gradients đó để cập nhật (update / 업데이트) parameters.

Autodiff không phải finite difference. Nó không perturb đầu vào (input / 입력) bằng một `h` nhỏ mà propagate derivatives qua các elementary operations.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Ma trận (matrix / 행렬) calculus, Jacobian, Hessian và automatic differentiation**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức

Nên đọc sau [Multivariable calculus](../05_calculus/04_multivariable_calculus.md), [Linear transformations](./02_linear_transformations.md) và [Tensor & multilinear algebra](./08_tensors_and_multilinear_algebra.md). Chapter này nối trực tiếp tới [Gradient descent và convexity](../08_optimization_numerical/01_gradient_descent_and_convexity.md), [Taylor approximation](../05_calculus/08_taylor_series_and_local_approximation.md) và toàn bộ machine học tập (learning / 학습) tối ưu hóa (optimization / 최적화).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
