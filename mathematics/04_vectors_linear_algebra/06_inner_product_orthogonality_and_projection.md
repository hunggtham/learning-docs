# Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Inner sản phẩm (product / 제품) là generalized notion của alignment** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Norm xuất hiện từ self-alignment** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối inner product với orthogonality và projection, để khoảng cách, góc và xấp xỉ dùng cùng một cấu trúc hình học.

Dot sản phẩm (product / 제품) trong `\mathbb R^n` thường được học như một công thức:

```math
u\cdot v=\sum_i u_iv_i.
```

Nhưng ý nghĩa sâu hơn là: nó tạo ra hình học (geometry / 기하학). Từ một inner sản phẩm (product / 제품), ta có length, angle, perpendicularity, projection, orthogonal basis và least squares.

Vì vậy chapter này nên được đọc như một chuỗi phụ thuộc (dependency / 의존성):

```text
inner product
→ norm
→ angle
→ orthogonality
→ projection
→ orthogonal decomposition
→ least squares
→ QR / Fourier / PCA
```

## 1. Inner sản phẩm (product / 제품) là generalized notion của alignment

Trong Euclidean không gian (space / 공간):

```math
\langle u,v\rangle=u^Tv.
```

Một inner sản phẩm (product / 제품) abstract cần thỏa các properties như linearity, symmetry/conjugate symmetry và positive definiteness.

Trên real véc-tơ (vector / 벡터) không gian (space / 공간):

```math
\langle u,v\rangle=\langle v,u\rangle
```

và

```math
\langle v,v\rangle>0
```

cho mọi `v\ne0`.

Điều này cho phép định nghĩa hình học (geometry / 기하학) mà không phụ thuộc vào coordinate biểu diễn (representation / 표현) cụ thể.

> **Chuyển mạch:** Trong **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **2. Norm xuất hiện từ self-alignment** tiếp nhận điểm tựa từ **1. Inner sản phẩm (product / 제품) là generalized notion của alignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Cauchy–Schwarz là theorem làm angle hợp lệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Norm xuất hiện từ self-alignment

Length được định nghĩa bởi

```math
\|v\|=\sqrt{\langle v,v\rangle}.
```

Distance:

```math
d(u,v)=\|u-v\|.
```

Pythagoras chỉ là một consequence của inner sản phẩm (product / 제품) cấu trúc (structure / 구조).

Nếu

```math
\langle u,v\rangle=0,
```

thì

```math
\|u+v\|^2
=\|u\|^2+\|v\|^2.
```

Derivation:

```math
\|u+v\|^2
=\langle u+v,u+v\rangle
```

```math
=\|u\|^2+2\langle u,v\rangle+\|v\|^2.
```

Cross term biến mất khi vectors orthogonal.

> **Chuyển mạch:** Ở chặng này của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **3. Cauchy–Schwarz là theorem làm angle hợp lệ** tiếp nhận điểm tựa từ **2. Norm xuất hiện từ self-alignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Orthogonality là independence theo hình học (geometry / 기하학) đang chọn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Cauchy–Schwarz là theorem làm angle hợp lệ

Ta muốn define

```math
\cos\theta=
\frac{\langle u,v\rangle}
{\|u\|\|v\|}.
```

Để expression nằm trong `[-1,1]`, cần theorem:

```math
|\langle u,v\rangle|
\le
\|u\|\|v\|.
```

Đây là bất đẳng thức Cauchy–Schwarz (Cauchy–Schwarz inequality / 코시-슈바르츠 부등식).

Proof idea: norm luôn nonnegative. Xét

```math
\|u-tv\|^2\ge0
```

như một quadratic theo `t`. Discriminant không thể dương theo cách tạo giá trị âm, dẫn tới Cauchy–Schwarz.

Theorem này không chỉ technical; nó bảo đảm notion cosine/angle consistent.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **4. Orthogonality là independence theo hình học (geometry / 기하학) đang chọn** tiếp nhận điểm tựa từ **3. Cauchy–Schwarz là theorem làm angle hợp lệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Projection là nearest-point bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Orthogonality là independence theo hình học (geometry / 기하학) đang chọn

Hai vectors trực giao khi

```math
\langle u,v\rangle=0.
```

Nếu một set gồm các nonzero mutually orthogonal vectors, set đó linearly independent.

Proof idea: nếu

```math
c_1v_1+\cdots+c_kv_k=0,
```

inner sản phẩm (product / 제품) hai vế với `v_j`:

```math
c_j\|v_j\|^2=0,
```

nên `c_j=0`.

Orthogonality làm coefficients tách rời nhau rất mạnh.

> **Chuyển mạch:** Trong **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **5. Projection là nearest-point bài toán (problem / 문제)** tiếp nhận điểm tựa từ **4. Orthogonality là independence theo hình học (geometry / 기하학) đang chọn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Orthogonal decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Projection là nearest-point bài toán (problem / 문제)

Muốn approximate `v` bằng véc-tơ (vector / 벡터) trên line span bởi `u`:

```math
cu.
```

Ta minimize

```math
\|v-cu\|^2.
```

Điều kiện optimum cho

```math
c=
\frac{\langle v,u\rangle}
{\langle u,u\rangle}.
```

Do đó

```math
\operatorname{proj}_u(v)
=
\frac{\langle v,u\rangle}
{\langle u,u\rangle}u.
```

Nếu `u` đơn vị (unit / 단위) length:

```math
\operatorname{proj}_u(v)=\langle v,u\rangle u.
```

Projection formula không phải arbitrary formula; nó là solution của **closest điểm (point / 지점) in a subspace**.

> **Chuyển mạch:** Ở chặng này của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **6. Orthogonal decomposition** tiếp nhận điểm tựa từ **5. Projection là nearest-point bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Projection theorem trên subspace** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Orthogonal decomposition

Ta có thể viết

```math
v=v_{\parallel}+v_{\perp}
```

với

```math
v_{\parallel}=\operatorname{proj}_U(v)
```

và

```math
v_{\perp}=v-v_{\parallel}.
```

Điều kiện:

```math
v_{\perp}\perp U.
```

Mô hình tư duy (mental model / 사고 모델):

```text
vector = explainable component + residual component
```

Đây chính là hình học (geometry / 기하학) của regression.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **7. Projection theorem trên subspace** tiếp nhận điểm tựa từ **6. Orthogonal decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Least squares là projection, không phải regression trick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Projection theorem trên subspace

Nếu `U` là finite-dimensional subspace trong Euclidean không gian (space / 공간), mỗi véc-tơ (vector / 벡터) `v` có unique decomposition:

```math
v=u+r,
```

với

```math
u\in U,
\qquad
r\in U^\perp.
```

`u` là unique điểm (point / 지점) trong `U` gần `v` nhất.

Điều này giải thích vì sao least squares solution có residual orthogonal với column không gian (space / 공간).

> **Chuyển mạch:** Trong **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **8. Least squares là projection, không phải regression trick** tiếp nhận điểm tựa từ **7. Projection theorem trên subspace** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Vì sao orthonormal basis đặc biệt?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Least squares là projection, không phải regression trick

Cho hệ thống (system / 시스템) overdetermined:

```math
Ax\approx b.
```

Outputs reachable bởi mô hình (model / 모델) nằm trong column không gian (space / 공간):

```math
\mathcal C(A).
```

Ta chọn `\hat x` để

```math
A\hat x
```

là projection của `b` lên `\mathcal C(A)`.

Residual:

```math
r=b-A\hat x
```

phải orthogonal với every column của `A`:

```math
A^Tr=0.
```

Suy ra:

```math
A^TA\hat x=A^Tb.
```

Normal equations là consequence của orthogonality.

> **Chuyển mạch:** Ở chặng này của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **9. Vì sao orthonormal basis đặc biệt?** tiếp nhận điểm tựa từ **8. Least squares là projection, không phải regression trick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Gram–Schmidt: remove explained components** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Vì sao orthonormal basis đặc biệt?

Basis `q_1,\ldots,q_n` orthonormal nếu

```math
\langle q_i,q_j\rangle
=
\begin{cases}
1&i=j\\
0&i\ne j.
\end{cases}
```

Khi đó coordinates của `x` chỉ là projections:

```math
x=
\sum_i
\langle x,q_i\rangle q_i.
```

Không cần solve general hệ tuyến tính (linear system / 선형 시스템).

Ma trận (matrix / 행렬) `Q` với orthonormal columns thỏa:

```math
Q^TQ=I.
```

Do đó norm được bảo toàn:

```math
\|Qx\|=\|x\|.
```

Orthogonal matrices là geometry-preserving transforms.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **10. Gram–Schmidt: remove explained components** tiếp nhận điểm tựa từ **9. Vì sao orthonormal basis đặc biệt?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Classical Gram–Schmidt vs numerical stability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Gram–Schmidt: remove explained components

Bắt đầu independent vectors `v_1,\ldots,v_k`.

Set:

```math
u_1=v_1.
```

Sau đó:

```math
u_2=v_2-
\operatorname{proj}_{u_1}(v_2).
```

General:

```math
u_j
=
v_j-
\sum_{i<j}
\operatorname{proj}_{u_i}(v_j).
```

Ta liên tục trừ đi components đã được explain bởi previous directions.

Normalize:

```math
q_i=\frac{u_i}{\|u_i\|}.
```

Đây là conceptual foundation của QR decomposition.

> **Chuyển mạch:** Trong **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **11. Classical Gram–Schmidt vs numerical stability** tiếp nhận điểm tựa từ **10. Gram–Schmidt: remove explained components** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Inner sản phẩm (product / 제품) không nhất thiết là ordinary dot sản phẩm (product / 제품)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Classical Gram–Schmidt vs numerical stability

Trong chính xác (exact / 정확한) arithmetic, Gram–Schmidt đẹp.

Trong floating điểm (point / 지점), classical Gram–Schmidt có thể mất orthogonality khi vectors gần linearly dependent.

Modified Gram–Schmidt hoặc Householder QR thường numerically stable hơn.

Đây là distinction quan trọng:

```text
mathematically equivalent
≠ numerically equivalent
```

> **Chuyển mạch:** Ở chặng này của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **12. Inner sản phẩm (product / 제품) không nhất thiết là ordinary dot sản phẩm (product / 제품)** tiếp nhận điểm tựa từ **11. Classical Gram–Schmidt vs numerical stability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. hàm (function / 함수) spaces cũng có inner sản phẩm (product / 제품)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Inner sản phẩm (product / 제품) không nhất thiết là ordinary dot sản phẩm (product / 제품)

Ta có thể define weighted inner sản phẩm (product / 제품):

```math
\langle x,y\rangle_M=x^TMy
```

với `M` symmetric positive definite.

Khi đó hình học (geometry / 기하학) thay đổi: angle, norm và “nearest” đều phụ thuộc `M`.

Mahalanobis distance trong statistics:

```math
d(x,\mu)^2
=(x-\mu)^T\Sigma^{-1}(x-\mu)
```

là Euclidean-like hình học (geometry / 기하학) sau khi account covariance scaling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **13. hàm (function / 함수) spaces cũng có inner sản phẩm (product / 제품)** tiếp nhận điểm tựa từ **12. Inner sản phẩm (product / 제품) không nhất thiết là ordinary dot sản phẩm (product / 제품)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Cosine similarity và embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. hàm (function / 함수) spaces cũng có inner sản phẩm (product / 제품)

Ví dụ:

```math
\langle f,g\rangle
=
\int_a^b f(x)g(x)\,dx.
```

Functions orthogonal nếu integral sản phẩm (product / 제품) bằng zero.

Sine/cosine functions ở appropriate frequencies tạo orthogonal family.

Fourier coefficients là projections:

```text
signal
→ project onto frequency basis
→ coefficients
```

Fourier phân tích (analysis / 분석) vì vậy là tuyến tính (linear / 선형) algebra trong infinite-dimensional hàm (function / 함수) không gian (space / 공간).

> **Chuyển mạch:** Trong **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **14. Cosine similarity và embeddings** tiếp nhận điểm tựa từ **13. hàm (function / 함수) spaces cũng có inner sản phẩm (product / 제품)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Projection ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Cosine similarity và embeddings

Cosine similarity:

```math
\cos\theta
=
\frac{x^Ty}{\|x\|\|y\|}.
```

Nó bỏ magnitude và đo directional alignment.

Trong embedding không gian (space / 공간), interpretation phụ thuộc mô hình (model / 모델) huấn luyện (training / 학습) hình học (geometry / 기하학). High cosine similarity không universal đồng nghĩa “semantically same”; nó chỉ nói biểu diễn (representation / 표현) vectors align theo chỉ số (metric / 지표) được chọn.

> **Chuyển mạch:** Ở chặng này của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **15. Projection ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **14. Cosine similarity và embeddings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Pythagorean năng lượng (energy / 에너지) decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Projection ma trận (matrix / 행렬)

Nếu columns của `Q` orthonormal span subspace `U`, projection ma trận (matrix / 행렬) là

```math
P=QQ^T.
```

Properties:

```math
P^2=P
```

(idempotent) và

```math
P^T=P
```

(symmetric).

`P^2=P` có meaning: dự án (project / 프로젝트) lần hai không thay gì thêm.

Nếu `A` full column rank nhưng columns chưa orthonormal:

```math
P=A(A^TA)^{-1}A^T.
```

Trong hiện thực (implementation / 구현), thường không form expression này tường minh (explicit / 명시적) nếu numerical stability quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **16. Pythagorean năng lượng (energy / 에너지) decomposition** tiếp nhận điểm tựa từ **15. Projection ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. PCA liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Pythagorean năng lượng (energy / 에너지) decomposition

Nếu

```math
v=u+r,
\qquad u\perp r,
```

thì

```math
\|v\|^2=\|u\|^2+\|r\|^2.
```

Trong regression:

```text
signal explained by model + residual
```

có geometric decomposition liên quan sum of squares dưới các giả định (assumptions / 가정들)/setup phù hợp.

Trong tín hiệu (signal / 신호) processing, orthogonal basis cũng cho năng lượng (energy / 에너지) decomposition.

> **Chuyển mạch:** Trong **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, sau nội dung của **16. Pythagorean năng lượng (energy / 에너지) decomposition**, **17. PCA liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **18. Physics liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. PCA liên kết (connection / 연결)

PCA tìm directions orthonormal sao cho projected variance lớn nhất sequentially.

First principal thành phần (component / 컴포넌트) solve conceptually:

```math
\max_{\|u\|=1}
\operatorname{Var}(Xu).
```

Projection lên low-dimensional principal subspace giữ lại nhiều squared năng lượng (energy / 에너지)/variance nhất theo criterion PCA.

Orthogonality làm selected directions không redundant theo Euclidean hình học (geometry / 기하학).

> **Chuyển mạch:** Ở chặng này của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **18. Physics liên kết (connection / 연결)** tiếp nhận điểm tựa từ **17. PCA liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Proof idea: best projection vì residual orthogonal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Physics liên kết (connection / 연결)

Công việc (work / 작업):

```math
W=F\cdot d
```

chỉ thành phần (component / 컴포넌트) của force theo displacement đóng góp.

Projection giải thích trực tiếp:

```text
force perpendicular to motion → zero work contribution
```

Inner sản phẩm (product / 제품) là “alignment multiplier”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **19. Proof idea: best projection vì residual orthogonal** tiếp nhận điểm tựa từ **18. Physics liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. các giả định (assumptions / 가정들) và chỉ số (metric / 지표) choice** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Proof idea: best projection vì residual orthogonal

Giả sử `p` là projection của `v` lên subspace `U`, residual `r=v-p` orthogonal `U`.

Cho bất kỳ `u\in U`:

```math
v-u=(v-p)+(p-u)=r+(p-u).
```

Hai terms orthogonal, nên Pythagoras:

```math
\|v-u\|^2
=\|r\|^2+\|p-u\|^2
\ge\|r\|^2.
```

Equality chỉ khi `u=p`.

Đây là proof hình học rằng projection là nearest điểm (point / 지점).

> **Chuyển mạch:** Trong **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **20. các giả định (assumptions / 가정들) và chỉ số (metric / 지표) choice** tiếp nhận điểm tựa từ **19. Proof idea: best projection vì residual orthogonal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. các giả định (assumptions / 가정들) và chỉ số (metric / 지표) choice

Projection phụ thuộc inner sản phẩm (product / 제품).

Nếu tính năng (feature / 기능) scales khác nhau mạnh, ordinary Euclidean inner sản phẩm (product / 제품) có thể tạo hình học (geometry / 기하학) không phù hợp.

Standardization, whitening hoặc weighted metrics không chỉ preprocessing cosmetic; chúng thay notion length, angle và nearest điểm (point / 지점).

> **Chuyển mạch:** Ở chặng này của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, sau nội dung của **20. các giả định (assumptions / 가정들) và chỉ số (metric / 지표) choice**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Inner sản phẩm (product / 제품) nối:

```text
Pythagoras
→ norm / angle
→ orthogonality
→ projection
→ least squares
→ QR
→ Fourier
→ PCA
→ cosine similarity
→ weighted statistical geometry
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Inner sản phẩm (product / 제품) là **máy đo alignment**. Orthogonality nghĩa “không share thành phần (component / 컴포넌트)” theo hình học (geometry / 기하학) đã chọn. Projection là **best approximation trong một subspace**. Least squares, Fourier coefficients, PCA và nhiều regression methods đều là các phiên bản của cùng một câu hỏi: phần nào của đối tượng (object / 객체) nằm trong không gian (space / 공간) ta có thể represent?

> **Chuyển mạch:** Trong **Inner sản phẩm (product / 제품), trực giao và phép chiếu: hình học (geometry / 기하학) từ một phép đo alignment**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

Orthogonality phụ thuộc inner sản phẩm (product / 제품), không phải một notion tuyệt đối trong mọi hình học (geometry / 기하학). Zero véc-tơ (vector / 벡터) orthogonal với mọi véc-tơ (vector / 벡터) nhưng không thể normalize. Normal equations đúng về lý thuyết nhưng có thể kém ổn định hơn QR/SVD. Cosine similarity bỏ magnitude nhưng không xóa mọi độ lệch (bias / 편향) của biểu diễn (representation / 표현). Gram–Schmidt trong chính xác (exact / 정확한) math và floating-point hiện thực (implementation / 구현) không có cùng numerical hành vi (behavior / 동작).

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
