# Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao eigenvectors là câu hỏi tự nhiên?** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **Từ Av = λv đến characteristic equation** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối eigenvalues/eigenvectors với invariant directions và dynamics, để nhận ra cấu trúc không đổi dưới một phép biến đổi.

Một ma trận (matrix / 행렬) không chỉ là bảng số. Khi ma trận (matrix / 행렬) `A` tác động lên véc-tơ (vector / 벡터), nó có thể quy mô (scale / 규모), rotate, shear hoặc combine nhiều effects cùng lúc. Một cách rất mạnh để hiểu transformation là tìm những directions đặc biệt mà transformation không làm đổi direction, chỉ thay đổi magnitude và có thể đảo hướng.

Một nonzero véc-tơ (vector / 벡터) `v` là **eigenvector (고유벡터)** của `A` nếu

```math
Av=\lambda v,
```

trong đó `λ` là **eigenvalue (고유값)** tương ứng.

Equation này nói rằng `v` là direction mà transformation hành xử đơn giản nhất: sau transformation, véc-tơ (vector / 벡터) vẫn nằm trên cùng line với véc-tơ (vector / 벡터) ban đầu.

## Vì sao eigenvectors là câu hỏi tự nhiên?

Giả sử `A` biến đổi cả không gian. Với một arbitrary véc-tơ (vector / 벡터), đầu ra (output / 출력) có thể khó hiểu. Nhưng nếu tìm được basis gồm eigenvectors, mọi thành phần (component / 컴포넌트) theo từng eigenvector chỉ bị nhân với một scalar riêng.

Thay vì một transformation phức tạp, ta có nhiều independent one-dimensional scalings.

Đó là lý do eigen decomposition xuất hiện trong động (dynamic / 동적) các hệ thống (systems / 시스템들), PCA, Markov chains, differential equations, đồ thị (graph / 그래프) algorithms và stability phân tích (analysis / 분석).

> **Chuyển mạch:** Trong **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Từ Av = λv đến characteristic equation** tiếp nhận điểm tựa từ **Vì sao eigenvectors là câu hỏi tự nhiên?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ 2×2** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ `Av = λv` đến characteristic equation

Ta rewrite

```math
Av=\lambda v
```

thành

```math
(A-\lambda I)v=0.
```

Muốn có nonzero solution `v`, ma trận (matrix / 행렬) `A-λI` phải singular. Vì vậy

```math
\det(A-\lambda I)=0.
```

Equation này gọi là **characteristic equation**.

Polynomial

```math
p_A(\lambda)=\det(A-\lambda I)
```

là characteristic polynomial. Roots của polynomial là eigenvalues.

> **Chuyển mạch:** Ở chặng này của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Từ Av = λv đến characteristic equation** cho ta quy tắc; **Ví dụ 2×2** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Eigenspace** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ 2×2

Cho

```math
A=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
```

Ta solve

```math
\det(A-\lambda I)
=
\det\begin{bmatrix}2-\lambda&1\\1&2-\lambda\end{bmatrix}
=(2-\lambda)^2-1.
```

Do đó

```math
(2-\lambda)^2=1,
```

nên eigenvalues là

```math
\lambda_1=3,\qquad \lambda_2=1.
```

Với `λ=3`, solve

```math
(A-3I)v=0
```

cho direction

```math
v_1\propto\begin{bmatrix}1\\1\end{bmatrix}.
```

Với `λ=1`,

```math
v_2\propto\begin{bmatrix}1\\-1\end{bmatrix}.
```

Hai eigenvectors trực giao vì ma trận (matrix / 행렬) symmetric.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Ví dụ 2×2** cho ta quy tắc; **Eigenspace** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Algebraic multiplicity và geometric multiplicity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Eigenspace

Với eigenvalue `λ`, tất cả eigenvectors tương ứng cùng zero véc-tơ (vector / 벡터) tạo thành null không gian (space / 공간)

```math
E_\lambda=\ker(A-\lambda I).
```

Đây là **eigenspace (고유공간)**.

Một eigenvalue có thể có nhiều linearly independent eigenvectors. Dimension của eigenspace gọi là **geometric multiplicity**.

> **Chuyển mạch:** Trong **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Algebraic multiplicity và geometric multiplicity** tiếp nhận điểm tựa từ **Eigenspace** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Diagonalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Algebraic multiplicity và geometric multiplicity

Nếu eigenvalue `λ` xuất hiện `k` lần như gốc (root / 루트) của characteristic polynomial, `k` là **algebraic multiplicity**.

Geometric multiplicity là

```math
\dim\ker(A-\lambda I).
```

Luôn có

```math
1\le \text{geometric multiplicity}
\le \text{algebraic multiplicity}.
```

Nếu tổng số independent eigenvectors đủ bằng dimension của không gian (space / 공간), ma trận (matrix / 행렬) diagonalizable.

> **Chuyển mạch:** Ở chặng này của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Diagonalization** tiếp nhận điểm tựa từ **Algebraic multiplicity và geometric multiplicity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Powers của ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Diagonalization

Nếu `A` có `n` independent eigenvectors `v_1,...,v_n`, đặt chúng làm columns của `P`:

```math
P=[v_1\ v_2\ \cdots\ v_n].
```

Gọi

```math
D=\operatorname{diag}(\lambda_1,\dots,\lambda_n).
```

Ta có

```math
AP=PD
```

và do `P` invertible,

```math
A=PDP^{-1}.
```

Đây không phải chỉ là trick algebra. `P^{-1}` đổi coordinates từ tiêu chuẩn (standard / 표준) basis sang eigenbasis, `D` quy mô (scale / 규모) từng eigen-coordinate độc lập, rồi `P` đổi trở lại original basis.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Powers của ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **Diagonalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động (dynamic / 동적) các hệ thống (systems / 시스템들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Powers của ma trận (matrix / 행렬)

Từ

```math
A=PDP^{-1}
```

suy ra

```math
A^k=PD^kP^{-1}.
```

Vì `D` diagonal,

```math
D^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k).
```

Repeated transformation vì vậy được hiểu qua powers của eigenvalues.

> **Chuyển mạch:** Trong **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Động (dynamic / 동적) các hệ thống (systems / 시스템들)** tiếp nhận điểm tựa từ **Powers của ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Spectral radius** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động (dynamic / 동적) các hệ thống (systems / 시스템들)

Discrete hệ tuyến tính (linear system / 선형 시스템)

```math
x_{k+1}=Ax_k
```

cho

```math
x_k=A^kx_0.
```

Nếu decompose initial trạng thái (state / 상태) theo eigenvectors,

```math
x_0=c_1v_1+\cdots+c_nv_n,
```

thì

```math
x_k=c_1\lambda_1^kv_1+\cdots+c_n\lambda_n^kv_n.
```

Mỗi eigenmode evolve độc lập.

Nếu `|λ|<1`, chế độ (mode / 모드) decay. Nếu `|λ|>1`, chế độ (mode / 모드) grow. Nếu `λ=-1`, sign alternate. Nếu `λ` complex, chế độ (mode / 모드) thường encode rotation/oscillation.

> **Chuyển mạch:** Ở chặng này của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Spectral radius** tiếp nhận điểm tựa từ **Động (dynamic / 동적) các hệ thống (systems / 시스템들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Complex eigenvalues** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spectral radius

**Spectral radius (스펙트럴 반지름)** là

```math
\rho(A)=\max_i|\lambda_i|.
```

Trong nhiều tuyến tính (linear / 선형) iterative các hệ thống (systems / 시스템들), spectral radius quyết định long-term growth hoặc convergence.

Ví dụ nếu phương thức (method / 메서드) có lỗi (error / 오류) cập nhật (update / 업데이트)

```math
e_{k+1}=Ae_k,
```

thì `ρ(A)<1` thường là central điều kiện (condition / 조건) để lỗi (error / 오류) decay asymptotically.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Complex eigenvalues** tiếp nhận điểm tựa từ **Spectral radius** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Defective matrices** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Complex eigenvalues

Một real ma trận (matrix / 행렬) có thể có complex eigenvalues. Ví dụ rotation ma trận (matrix / 행렬)

```math
R=\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
```

có eigenvalues

```math
e^{i\theta},\qquad e^{-i\theta}.
```

Trong real plane không có nonzero direction giữ nguyên dưới nontrivial rotation, nhưng khi mở rộng sang complex không gian (space / 공간), rotation được biểu diễn (representation / 표현) như multiplication bởi complex phases.

Điều này nối eigenanalysis với complex numbers và oscillation.

> **Chuyển mạch:** Trong **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Defective matrices** tiếp nhận điểm tựa từ **Complex eigenvalues** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Jordan form intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Defective matrices

Không phải ma trận (matrix / 행렬) nào cũng diagonalizable.

Ví dụ

```math
A=\begin{bmatrix}1&1\\0&1\end{bmatrix}
```

có characteristic polynomial

```math
(1-\lambda)^2,
```

nên eigenvalue `1` có algebraic multiplicity 2. Nhưng

```math
A-I=\begin{bmatrix}0&1\\0&0\end{bmatrix}
```

có null không gian (space / 공간) dimension 1. Chỉ có một independent eigenvector.

Ma trận (matrix / 행렬) như vậy gọi là **defective** và không diagonalizable.

> **Chuyển mạch:** Ở chặng này của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Jordan form intuition** tiếp nhận điểm tựa từ **Defective matrices** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Symmetric matrices và spectral theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Jordan form intuition

Khi ma trận (matrix / 행렬) không diagonalizable, ta vẫn có thể đưa nó về Jordan form trên complex numbers dưới broad conditions.

Một Jordan khối (block / 블록) có dạng

```math
J=\begin{bmatrix}
\lambda&1&0&\cdots\\
0&\lambda&1&\cdots\\
\vdots&&\ddots&1\\
0&\cdots&0&\lambda
\end{bmatrix}.
```

Extra ones trên superdiagonal encode thất bại (failure / 실패) to have enough eigenvectors.

Jordan form quan trọng về lý thuyết (theory / 이론), dù numerically thường không stable để compute trực tiếp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Symmetric matrices và spectral theorem** tiếp nhận điểm tựa từ **Jordan form intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Positive definite matrices** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symmetric matrices và spectral theorem

Nếu `A` là real symmetric,

```math
A=A^T,
```

thì mọi eigenvalues đều real và tồn tại orthonormal eigenbasis.

Ta có

```math
A=Q\Lambda Q^T
```

với `Q` orthogonal.

Đây là **spectral theorem**.

Nó đặc biệt quan trọng vì covariance matrices và Hessians của sufficiently smooth scalar functions là symmetric.

> **Chuyển mạch:** Trong **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Positive definite matrices** tiếp nhận điểm tựa từ **Symmetric matrices và spectral theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rayleigh quotient** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Positive definite matrices

Một symmetric ma trận (matrix / 행렬) `A` positive definite nếu

```math
x^TAx>0
```

cho mọi `x≠0`.

Với symmetric `A`, điều này tương đương mọi eigenvalues đều positive.

Nếu tất cả eigenvalues nonnegative, ma trận (matrix / 행렬) positive semidefinite.

Điều này liên hệ trực tiếp với convexity của quadratic functions và covariance cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Rayleigh quotient** tiếp nhận điểm tựa từ **Positive definite matrices** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PCA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rayleigh quotient

Cho symmetric `A`, define

```math
R_A(x)=\frac{x^TAx}{x^Tx}.
```

Rayleigh quotient cho effective scaling của quadratic form theo direction `x`.

Ta có

```math
\lambda_{min}\le R_A(x)\le\lambda_{max}.
```

Maximum Rayleigh quotient đạt tại eigenvector của largest eigenvalue; minimum đạt tại eigenvector của smallest eigenvalue.

Đây là foundation của PCA, spectral methods và tối ưu hóa (optimization / 최적화) algorithms.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **PCA** tiếp nhận điểm tựa từ **Rayleigh quotient** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SVD và eigen decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PCA

Covariance ma trận (matrix / 행렬)

```math
\Sigma=\frac1nX^TX
```

là symmetric positive semidefinite.

Eigenvectors của `Σ` chỉ principal directions của dữ liệu (data / 데이터). Eigenvalues đo variance theo các directions đó.

PCA chọn eigenvectors tương ứng với largest eigenvalues để giữ directions chứa nhiều variance nhất.

Điều này không có nghĩa “largest eigenvalue luôn là tính năng (feature / 기능) quan trọng nhất”. Interpretation chỉ đúng trong ngữ cảnh (context / 맥락) covariance và PCA mục tiêu (objective / 목표).

> **Chuyển mạch:** Trong **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **SVD và eigen decomposition** tiếp nhận điểm tựa từ **PCA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Markov chains** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SVD và eigen decomposition

Với general ma trận (matrix / 행렬) `A`, SVD luôn tồn tại:

```math
A=U\Sigma V^T.
```

Right singular vectors là eigenvectors của

```math
A^TA,
```

left singular vectors là eigenvectors của

```math
AA^T.
```

Squared singular values là eigenvalues tương ứng.

SVD robust hơn eigen decomposition cho rectangular matrices và nhiều numerical tasks.

> **Chuyển mạch:** Ở chặng này của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Markov chains** tiếp nhận điểm tựa từ **SVD và eigen decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đồ thị (graph / 그래프) spectral methods** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Markov chains

Nếu chuyển tiếp (transition / 전이) ma trận (matrix / 행렬) `P` dùng row-vector convention, stationary phân phối (distribution / 분포) `π` thỏa

```math
\pi=\pi P.
```

Vì vậy `π` là left eigenvector với eigenvalue 1.

Repeated multiplication bởi chuyển tiếp (transition / 전이) ma trận (matrix / 행렬) damp nhiều modes khác nhau; long-run hành vi (behavior / 동작) thường dominated bởi eigenvalue magnitude lớn nhất, đặc biệt eigenvalue 1 trong ergodic chains.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Đồ thị (graph / 그래프) spectral methods** tiếp nhận điểm tựa từ **Markov chains** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differential equations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồ thị (graph / 그래프) spectral methods

Đồ thị (graph / 그래프) Laplacian

```math
L=D-A
```

trong đó `D` là degree ma trận (matrix / 행렬) và `A` adjacency ma trận (matrix / 행렬), có eigenstructure encode connectivity của đồ thị (graph / 그래프).

Số zero eigenvalues liên quan số connected components. Eigenvector tương ứng với second-smallest eigenvalue, gọi là Fiedler véc-tơ (vector / 벡터), được dùng trong spectral clustering và đồ thị (graph / 그래프) partitioning.

> **Chuyển mạch:** Trong **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Differential equations** tiếp nhận điểm tựa từ **Đồ thị (graph / 그래프) spectral methods** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Power iteration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential equations

Tuyến tính (linear / 선형) ODE hệ thống (system / 시스템)

```math
\frac{dx}{dt}=Ax
```

có solution

```math
x(t)=e^{At}x(0).
```

Nếu `A` diagonalizable,

```math
e^{At}=Pe^{Dt}P^{-1},
```

và each chế độ (mode / 모드) evolve như

```math
e^{\lambda_i t}.
```

Real part của eigenvalue quyết định growth/decay; imaginary part quyết định oscillation frequency.

> **Chuyển mạch:** Ở chặng này của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Power iteration** tiếp nhận điểm tựa từ **Differential equations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Numerical sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Power iteration

Nếu một ma trận (matrix / 행렬) có unique dominant eigenvalue theo magnitude và initial véc-tơ (vector / 벡터) có thành phần (component / 컴포넌트) theo dominant eigenvector, repeated multiplication

```math
x_{k+1}=Ax_k
```

rồi normalize sẽ hướng tới dominant eigenvector.

Đây là **power iteration**.

Thuật toán (algorithm / 알고리즘) giải thích trực giác vì sao repeated transformation làm dominant chế độ (mode / 모드) lấn át các modes nhỏ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Numerical sensitivity** tiếp nhận điểm tựa từ **Power iteration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Numerical sensitivity

Eigenvalues của symmetric matrices thường numerically well-behaved hơn eigenvalues của highly non-normal matrices.

Một ma trận (matrix / 행렬) có eigenvalues nhìn ổn định vẫn có thể có transient amplification nếu eigenvectors gần linearly dependent. Vì vậy eigenvalues không phải toàn bộ story trong stability phân tích (analysis / 분석).

Conditioning của eigenproblem quan trọng khi dùng eigenvalues từ floating-point computation.

> **Chuyển mạch:** Trong **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Numerical sensitivity** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Hãy xem tuyến tính (linear / 선형) transformation như một machine trộn nhiều directions. Eigenvectors là những directions mà machine không trộn với directions khác; nó chỉ quy mô (scale / 규모). Khi một eigenbasis tồn tại, ta đổi coordinates để nhìn machine như nhiều independent scalar multipliers.

Eigenvalues sau đó trở thành “growth factors” của các natural modes. Repeated dynamics, covariance hình học (geometry / 기하학), đồ thị (graph / 그래프) diffusion và differential equations đều dùng cùng cấu trúc (structure / 구조) này.

> **Chuyển mạch:** Ở chặng này của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

Eigenvector không thể là zero véc-tơ (vector / 벡터). Không phải every ma trận (matrix / 행렬) diagonalizable. Repeated eigenvalue không đồng nghĩa có nhiều independent eigenvectors tương ứng.

Largest eigenvalue không luôn “quan trọng nhất” nếu chưa xác định bài toán (problem / 문제). Trong PCA nó liên quan maximum variance; trong dynamics magnitude lớn có thể dominate long-term hành vi (behavior / 동작); trong tối ưu hóa (optimization / 최적화) Hessian eigenvalues encode curvature.

Complex eigenvalues của real ma trận (matrix / 행렬) không phải lỗi. Chúng thường encode rotations và oscillations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eigenvalues và eigenvectors: những directions tự nhiên của tuyến tính (linear / 선형) transformation**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Nên đọc cùng [Determinant, rank, null space và inverse](./07_determinant_rank_nullspace_and_inverse.md), [SVD và decompositions](./05_least_squares_svd_and_decompositions.md), [Stochastic processes và Markov chains](../06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md), [Differential equations](../05_calculus/05_differential_equations.md) và [Optimization](../08_optimization_numerical/00_optimization.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
