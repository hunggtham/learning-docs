# Số phức: từ nghiệm phương trình đến rotation

> **Mạch đọc:** Đọc **Số phức: từ nghiệm phương trình đến rotation** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Định nghĩa** sang **Complex plane**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Số phức (Complex number / 복소수) thường bị giới thiệu như cách “cho phép căn bậc hai của số âm”, nhưng vai trò của nó sâu hơn nhiều. Complex numbers biến rotation và oscillation thành algebra của multiplication.

## Định nghĩa

Một complex number có dạng

```math
z=a+bi
```

với `a,b∈R` và

```math
i^2=-1
```

`a` là real part, `b` là imaginary coefficient.

Hai complex numbers bằng nhau khi real parts và imaginary parts tương ứng bằng nhau.

## Complex plane

Ta biểu diễn `z=a+bi` như điểm (point / 지점) `(a,b)` trên mặt phẳng. Horizontal axis là real axis, vertical axis là imaginary axis.

Magnitude/modulus:

```math
|z|=\sqrt{a^2+b^2}
```

chính là Euclidean distance từ origin.

Angle `θ` so với positive real axis gọi là argument.

## Addition và multiplication

Addition:

```math
(a+bi)+(c+di)=(a+c)+(b+d)i
```

là véc-tơ (vector / 벡터) addition trên plane.

Multiplication:

```math
(a+bi)(c+di)=(ac-bd)+(ad+bc)i
```

Điều thú vị là multiplication không chỉ thay magnitude mà còn cộng angles.

## Polar form

Nếu `r=|z|` và angle `θ`, thì

```math
z=r(\cos\theta+i\sin\theta)
```

Euler formula cho

```math
e^{i\theta}=\cos\theta+i\sin\theta
```

nên

```math
z=re^{i\theta}
```

Nếu

```math
z_1=r_1e^{i\theta_1},\qquad z_2=r_2e^{i\theta_2}
```

thì

```math
z_1z_2=r_1r_2e^{i(\theta_1+\theta_2)}
```

Multiplication nhân magnitudes và cộng angles. Đây là lý do complex number là biểu diễn (representation / 표현) cực gọn cho rotation.

## Nhân với i là quay 90°

Lấy `z=a+bi`:

```math
iz=ai+b i^2=-b+ai
```

Điểm (point / 지점) `(a,b)` biến thành `(-b,a)`, chính là rotation 90° counterclockwise.

Vì vậy `i` không chỉ là “imaginary”; multiplication by `i` là một transformation hình học cụ thể.

## Conjugate

Complex conjugate:

```math
\bar z=a-bi
```

Reflection qua real axis. sản phẩm (product / 제품):

```math
z\bar z=a^2+b^2=|z|^2
```

Điều này giúp division:

```math
\frac{1}{a+bi}=\frac{a-bi}{a^2+b^2}
```

với `z≠0`.

## Roots of unity

Solutions của

```math
z^n=1
```

là

```math
z_k=e^{2\pi i k/n},\qquad k=0,1,\ldots,n-1
```

chúng nằm đều trên đơn vị (unit / 단위) circle. Cấu trúc này là nền của discrete Fourier transform và FFT.

## Signals và phasors

Một sinusoid

```math
A\cos(\omega t+\phi)
```

có thể được xử lý thông qua real part của

```math
Ae^{i(\omega t+\phi)}
```

Differentiation chỉ nhân thêm `iω`, khiến calculus của oscillations đơn giản hơn. Electrical kỹ thuật (engineering / 엔지니어링) dùng phasors vì lý do này.

## Mô hình tư duy (mental model / 사고 모델)

> Complex number là một điểm (point / 지점)/véc-tơ (vector / 벡터) 2D được trang bị phép multiplication đặc biệt: multiplication vừa quy mô (scale / 규모) vừa rotate. Vì vậy nó là ngôn ngữ tự nhiên của periodicity, waves và frequency-domain computation.

## Dùng chung (common / 공통) Misconceptions

“Imaginary” không có nghĩa vô nghĩa hoặc giả. Complex numbers có geometric interpretation rõ ràng. `i` không nằm “lớn hơn” hay “nhỏ hơn” real numbers theo total thứ tự (order / 순서) tương thích với arithmetic. Magnitude `|z|` là real non-negative, không phải lấy absolute giá trị (value / 값) từng thành phần (component / 컴포넌트) rồi cộng.

## Worked Example: giải phương trình bậc hai có nghiệm phức

Xét

```math
x^2-2x+5=0
```

Discriminant:

```math
\Delta=(-2)^2-4(1)(5)=4-20=-16
```

Quadratic formula cho

```math
x=\frac{2\pm\sqrt{-16}}{2}=1\pm2i
```

Hai roots là conjugates. Điều này không phải coincidence: polynomial có real coefficients, nên nếu `a+bi` là gốc (root / 루트) thì conjugate `a-bi` cũng là gốc (root / 루트). Khi substitute conjugate, các real coefficients không thay đổi và complex conjugation commute với addition/multiplication.

Nhìn trên complex plane, roots `(1,2)` và `(1,-2)` phản xạ qua real axis. biểu diễn (representation / 표현) hình học khiến “conjugate pair” trở thành một symmetry statement.

## Liên kết kiến thức (knowledge connection / 지식 연결): rotation ma trận (matrix / 행렬) và complex multiplication

Ma trận (matrix / 행렬) rotation 2D:

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
```

apply lên véc-tơ (vector / 벡터) `(x,y)`. Nếu encode điểm (point / 지점) thành `z=x+iy`, multiply bằng `e^{i\theta}` tạo đúng coordinates rotated tương tự. Complex multiplication và rotation ma trận (matrix / 행렬) là hai representations của cùng transformation.

Trong mã (code / 코드) xử lý 2D rotations, ma trận (matrix / 행렬) form generalizes dễ tới affine pipelines, còn complex form có thể compact hơn nếu chỉ cần planar rotations/scales.

## Liên kết kiến thức

Nên đọc cùng [Trigonometry](../03_geometry_trigonometry/04_trigonometry.md) để thấy đơn vị (unit / 단위) circle và rotation, [Eigenvalues và eigenvectors](../04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md) để nối complex modes với tuyến tính (linear / 선형) dynamics, và [Complex analysis](../05_calculus/12_complex_analysis_and_analytic_functions.md) khi cần mở rộng calculus sang complex plane.

Ứng dụng downstream quan trọng nhất nằm ở [Fourier, Signals và Frequency](../09_connections/05_fourier_signals_and_frequency.md) và [Laplace/Z-transform và Dynamic Systems](../09_connections/06_laplace_z_transform_and_dynamic_systems.md). Các links này là chuẩn gốc (canonical / 정본) đường dẫn (path / 경로) thay cho việc lặp lại cùng explanation ở nhiều chapter.

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 algebraic language](./00_algebraic_language.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
