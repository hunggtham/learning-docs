# Quan hệ ẩn, tham số và tọa độ cực

> **Mạch đọc:** Đọc **Quan hệ ẩn, tham số và tọa độ cực** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Implicit quan hệ (relation / 관계)** sang **Implicit differentiation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Không phải mọi geometric đối tượng (object / 객체) hoặc tiến trình (process / 프로세스) được mô tả tốt bằng dạng `y=f(x)`. Một circle chẳng hạn thất bại vertical-line kiểm thử (test / 테스트) nếu cố coi toàn bộ circle là một single-valued hàm (function / 함수) của `x`. Điều đó không có nghĩa circle “không thể dùng toán”; chỉ có nghĩa biểu diễn (representation / 표현) `y=f(x)` không phù hợp.

## Implicit quan hệ (relation / 관계)

Thay vì isolate đầu ra (output / 출력), ta có thể viết quan hệ (relation / 관계):

```math
F(x,y)=0.
```

Circle tâm origin radius `r`:

```math
x^2+y^2-r^2=0.
```

Equation này mô tả ràng buộc (constraint / 제약조건) giữa coordinates mà không chọn `x` hay `y` làm privileged đầu vào (input / 입력).

Implicit biểu diễn (representation / 표현) hữu ích khi đối tượng (object / 객체) có symmetry hoặc khi solving explicitly tạo nhiều branches.


> **Chuyển mạch:** Từ **Implicit quan hệ (relation / 관계)**, ta sang **Implicit differentiation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Implicit differentiation

Nếu `F(x,y)=0` và locally `y` có thể được xem như hàm (function / 함수) của `x`, differentiate theo `x`:

```math
F_x+F_y\frac{dy}{dx}=0.
```

Nếu `F_y\neq0`,

```math
\frac{dy}{dx}=-\frac{F_x}{F_y}.
```

Với circle:

```math
2x+2y\frac{dy}{dx}=0,
```

nên

```math
\frac{dy}{dx}=-\frac{x}{y}.
```

Điều kiện `F_y\neq0` nhắc ta rằng biểu diễn (representation / 표현) cục bộ (local / 로컬) `y(x)` có thể breakdown tại vertical tangents.


> **Chuyển mạch:** Từ **Implicit differentiation**, ta sang **Parametric biểu diễn (representation / 표현)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Parametric biểu diễn (representation / 표현)

Một curve có thể được sinh bằng parameter `t`:

```math
x=x(t),\qquad y=y(t).
```

Circle có biểu diễn (representation / 표현) tự nhiên:

```math
x=r\cos t,
```

```math
y=r\sin t.
```

Khi `t` chạy từ `0` tới `2\pi`, điểm (point / 지점) đi một vòng circle.

Parameter không nhất thiết là thời gian (time / 시간), nhưng trong motion problems nó thường là thời gian (time / 시간). Khi đó derivative véc-tơ (vector / 벡터)

```math
\frac{dr}{dt}
=
\begin{bmatrix}
x'(t)\\y'(t)
\end{bmatrix}
```

là velocity.

Nếu `x'(t)\neq0`, slope của curve là

```math
\frac{dy}{dx}=\frac{dy/dt}{dx/dt}.
```

Đây là chuỗi (chain / 사슬) quy tắc (rule / 규칙) dưới biểu diễn (representation / 표현) tham số.


> **Chuyển mạch:** Từ **Parametric biểu diễn (representation / 표현)**, ta sang **Arc length** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Arc length

Trong một small thời gian (time / 시간) `dt`, displacement xấp xỉ

```math
ds\approx\sqrt{(dx)^2+(dy)^2}.
```

Với `dx=x'(t)dt`, `dy=y'(t)dt`:

```math
ds\approx\sqrt{x'(t)^2+y'(t)^2}\,dt.
```

Do đó length từ `t=a` tới `b`:

```math
L=\int_a^b\sqrt{x'(t)^2+y'(t)^2}\,dt.
```

Pythagoras + calculus tạo formula này; không cần xem nó như quy tắc (rule / 규칙) độc lập.


> **Chuyển mạch:** Từ **Arc length**, ta sang **Polar coordinates** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Polar coordinates

Cartesian coordinates mô tả điểm (point / 지점) bằng horizontal/vertical components `(x,y)`. Polar coordinates (극좌표) dùng distance tới origin và angle:

```math
(r,\theta).
```

Conversion:

```math
x=r\cos\theta,
```

```math
y=r\sin\theta.
```

và

```math
r^2=x^2+y^2.
```

Polar biểu diễn (representation / 표현) tự nhiên cho rotational symmetry. Circle tâm origin chỉ là

```math
r=R.
```

thay vì quadratic equation.


> **Chuyển mạch:** Từ **Polar coordinates**, ta sang **Area element trong polar coordinates** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Area element trong polar coordinates

Một tiny polar cell có radial thickness `dr` và angular width `d\theta`. Arc length theo angular direction xấp xỉ

```math
r\,d\theta.
```

Nên area element:

```math
dA=r\,dr\,d\theta.
```

Factor `r` là Jacobian determinant của coordinate transformation. Xa origin, cùng angular thay đổi (change / 변경) quét arc dài hơn.


> **Chuyển mạch:** Từ **Area element trong polar coordinates**, ta sang **Khi nào biểu diễn (representation / 표현) tốt thay đổi bài toán** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Khi nào biểu diễn (representation / 표현) tốt thay đổi bài toán

Một circle trong Cartesian là quadratic ràng buộc (constraint / 제약조건); trong polar là constant radius. Một line qua origin trong polar là constant angle. Spiral có thể rất đơn giản:

```math
r=a\theta.
```

Trong graphics, robotics và điều hướng (navigation / 내비게이션), chọn coordinate frame phù hợp có thể biến complicated equations thành simple ones.


> **Chuyển mạch:** Từ **Khi nào biểu diễn (representation / 표현) tốt thay đổi bài toán**, ta sang **liên kết kiến thức (knowledge connection / 지식 연결)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Parametric curves nối functions với motion và véc-tơ (vector / 벡터) calculus. Implicit equations nối các ràng buộc (constraints / 제약조건들) với mức (level / 수준) sets/gradients. Polar coordinates nối trigonometry với Jacobian/thay đổi (change / 변경) of variables. Computer graphics dùng parametric curves cho Bézier/splines; robotics dùng multiple coordinate các hệ thống (systems / 시스템들) và transformations liên tục.


> **Chuyển mạch:** Từ **liên kết kiến thức (knowledge connection / 지식 연결)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Một đối tượng (object / 객체) toán học không bị ràng buộc vào một biểu diễn (representation / 표현). `y=f(x)`, implicit equation, parametric curve và polar coordinates có thể mô tả cùng hình học (geometry / 기하학) từ các viewpoints khác nhau. Chọn biểu diễn (representation / 표현) làm cấu trúc (structure / 구조) quan trọng trở nên đơn giản nhất.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

Parameter `t` không nhất thiết là x-coordinate hay thời gian (time / 시간). Polar coordinates không unique: `(r,\theta)` và `(r,\theta+2k\pi)` cùng điểm (point / 지점), và negative `r` có thể được reinterpreted bằng angle shift. `dy/dx=(dy/dt)/(dx/dt)` cần chú ý khi `dx/dt=0`.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Liên kết kiến thức** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết kiến thức

Nên đọc sau [Function Concept](./00_function_concept.md), [Coordinate Geometry](../03_geometry_trigonometry/01_coordinate_geometry.md) và [Trigonometry](../03_geometry_trigonometry/04_trigonometry.md). Formula arc length và implicit differentiation dùng trực tiếp [Derivatives](../05_calculus/01_derivatives.md) và [Integrals](../05_calculus/03_integrals_and_accumulation.md).

Khi chuyển sang nhiều chiều, cùng ý tưởng biểu diễn (representation / 표현)/coordinate thay đổi (change / 변경) phát triển thành [Multivariable Calculus](../05_calculus/04_multivariable_calculus.md), [Vector Calculus](../05_calculus/09_vector_calculus.md) và [Matrix Calculus/Jacobian](../04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md). hình học (geometry / 기하학) của implicit conics được đào sâu trong [Circles, Conics and Loci](../03_geometry_trigonometry/06_circles_conics_and_loci.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 function concept](./00_function_concept.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
