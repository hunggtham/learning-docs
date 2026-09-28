# Phép biến hình và đối xứng: transformations, invariants và symmetry

> **Mạch đọc:** Đọc **Phép biến hình và đối xứng: transformations, invariants và symmetry** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Transformation là một hàm (function / 함수) trên không gian (space / 공간)** sang **2. Translation: move mà không đổi shape**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Phép biến hình (geometric transformation / 기하변환) là một ánh xạ (mapping / 매핑) biến points thành points. Thay vì chỉ hỏi “shape này trông như thế nào?”, transformation viewpoint hỏi câu sâu hơn:

> Nếu ta move, rotate, reflect, quy mô (scale / 규모) hoặc thay đổi (change / 변경) coordinates, properties nào thay đổi và properties nào được bảo toàn?

Câu hỏi về **invariants** này là cầu nối (bridge / 브리지) trực tiếp từ hình học (geometry / 기하학) sang matrices, group lý thuyết (theory / 이론), physics, computer graphics và hiện đại (modern / 현대적) machine học tập (learning / 학습).

## 1. Transformation là một hàm (function / 함수) trên không gian (space / 공간)

Nếu không gian (space / 공간) là `S`, transformation có thể viết

```math
T:S\to S.
```

Mỗi điểm (point / 지점) `x` được map tới điểm (point / 지점) mới `T(x)`.

Một transformation có thể đại diện cho nhiều ý nghĩa:

- đối tượng (object / 객체) thực sự di chuyển trong một fixed frame;
- coordinate frame thay đổi còn đối tượng (object / 객체) đứng yên;
- dữ liệu (data / 데이터) được normalized/augmented;
- trạng thái (state / 상태) của hệ thống (system / 시스템) chuyển sang trạng thái (state / 상태) mới.

Do đó trước khi thao tác formula cần rõ interpretation của transformation.

## 2. Translation: move mà không đổi shape

Translation bởi véc-tơ (vector / 벡터) `t`:

```math
T(x)=x+t.
```

Trong 2D:

```math
(x,y)\mapsto(x+a,y+b).
```

Translation bảo toàn:

- distances;
- angles;
- parallelism;
- orientation;
- area/volume.

Nhưng nó không phải tuyến tính (linear / 선형) transformation trên ordinary position vectors vì

```math
T(0)=t\ne0.
```

Nó là affine transformation.

## 3. Rotation: preserve inner-product hình học (geometry / 기하학)

Rotation quanh origin angle `\theta`:

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Với véc-tơ (vector / 벡터) `x`, rotated véc-tơ (vector / 벡터) là

```math
x'=R(\theta)x.
```

Tại sao rotation preserve length?

Vì

```math
R^TR=I.
```

Do đó

```math
\|Rx\|^2
=(Rx)^T(Rx)
=x^TR^TRx
=x^Tx
=\|x\|^2.
```

Rotation không chỉ “trông như quay”; algebraically nó preserve dot products và vì thế preserve lengths/angles.

## 4. Composition của rotations giải thích angle addition

Nếu rotate `\alpha`, sau đó rotate `\beta`:

```math
R(\beta)R(\alpha)=R(\alpha+\beta).
```

Khai triển phép nhân ma trận (matrix multiplication / 행렬 곱셈) cho ra sine/cosine addition identities.

Vì thế identities như

```math
\cos(\alpha+\beta)
=
\cos\alpha\cos\beta-\sin\alpha\sin\beta
```

không phải công thức tách rời; chúng encode composition của rotations.

## 5. Reflection: preserve distance nhưng flip orientation

Reflection qua x-axis:

```math
(x,y)\mapsto(x,-y).
```

Ma trận (matrix / 행렬):

```math
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}.
```

Reflection preserve length/angle nhưng determinant bằng `-1`, biểu thị orientation bị đảo.

Rotation ma trận (matrix / 행렬) 2D có determinant `+1`.

Determinant vì vậy không chỉ đo volume scaling; sign còn encode orientation thay đổi (change / 변경).

## 6. Scaling: uniform và non-uniform khác nhau

Uniform scaling:

```math
x\mapsto kx.
```

Length quy mô (scale / 규모) `|k|`, area quy mô (scale / 규모) `k^2`, volume quy mô (scale / 규모) `|k|^3` trong 3D.

Nếu quy mô (scale / 규모) khác nhau theo axes:

```math
S=
\begin{bmatrix}
a&0\\
0&b
\end{bmatrix},
```

thì circle thường thành ellipse nếu `a\ne b`.

Non-uniform scaling không preserve angles nói chung. Do đó “quy mô (scale / 규모)” không phải một lớp (class / 클래스) invariance duy nhất.

## 7. Shear: shape thay đổi (change / 변경) mà area có thể giữ

Shear ma trận (matrix / 행렬):

```math
H=
\begin{bmatrix}
1&k\\
0&1
\end{bmatrix}.
```

Nó nghiêng shape mà determinant vẫn bằng 1, nên area preserved dù angles không preserved.

Đây là example quan trọng: same determinant không nghĩa same hình học (geometry / 기하학). Determinant chỉ capture volume scaling, không capture mọi distortion.

## 8. Affine transformations

Affine map có dạng

```math
T(x)=Ax+b.
```

`A` xử lý tuyến tính (linear / 선형) part; `b` translation.

Affine transformations preserve:

- lines;
- parallelism;
- ratios dọc cùng line;
- affine combinations.

Nhưng chúng không nhất thiết preserve lengths hay angles.

Computer graphics và computer vision dùng affine các mô hình (models / 모델들) rất nhiều vì chúng đủ flexible nhưng vẫn algebraically manageable.

## 9. Homogeneous coordinates: biến affine composition thành phép nhân ma trận (matrix multiplication / 행렬 곱셈)

Translation không represent được bằng ordinary `2×2` tuyến tính (linear / 선형) ma trận (matrix / 행렬) trên `(x,y)`. Ta augment coordinate:

```math
\tilde x=
\begin{bmatrix}
x\\y\\1
\end{bmatrix}.
```

Affine transform trở thành

```math
\begin{bmatrix}
a&b&t_x\\
c&d&t_y\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
x\\y\\1
\end{bmatrix}.
```

Giờ translation, rotation, quy mô (scale / 규모), shear có thể compose bằng phép nhân ma trận (matrix multiplication / 행렬 곱셈).

Trong 3D, graphics thường dùng `4×4` homogeneous matrices.

## 10. thứ tự (order / 순서) matters vì composition thường không commutative

Nói chung

```math
T_2\circ T_1\ne T_1\circ T_2.
```

Ví dụ rotate đối tượng (object / 객체) quanh origin rồi translate khác với translate trước rồi rotate; ở trường hợp (case / 사례) thứ hai translation véc-tơ (vector / 벡터) cũng bị rotation tác động.

Đây là nguồn bug phổ biến trong graphics engines và robotics transforms.

### Worked intuition

Điểm (point / 지점) `(1,0)`:

1. rotate 90° → `(0,1)`;
2. translate `(1,0)` → `(1,1)`.

Nếu translate trước:

1. `(1,0)+(1,0)=(2,0)`;
2. rotate 90° → `(0,2)`.

Kết quả khác nhau.

## 11. Symmetry là transformation làm đối tượng (object / 객체) bất biến (invariant / 불변식)

Đối tượng (object / 객체) có symmetry nếu tồn tại transformation `T` sao cho

```math
T(X)=X
```

ở mức đối tượng (object / 객체)/set.

Circle bất biến (invariant / 불변식) dưới mọi rotation quanh center.

Square bất biến (invariant / 불변식) dưới rotations multiples 90° và một số reflections.

Symmetry không chỉ là aesthetic thuộc tính (property / 속성); nó nói đối tượng (object / 객체) có redundant descriptions dưới certain transformations.

## 12. Symmetries tạo group cấu trúc (structure / 구조)

Các symmetries của một đối tượng (object / 객체) có thể compose. Chúng có:

- định danh (identity / 식별자) transformation;
- closure dưới composition;
- inverse;
- associativity.

Đó chính là group cấu trúc (structure / 구조).

Vì vậy group lý thuyết (theory / 이론) xuất hiện tự nhiên từ hình học (geometry / 기하학): nó formalize algebra của transformations giữ đối tượng (object / 객체) unchanged.

## 13. Invariance và equivariance

Hai ideas này đặc biệt quan trọng trong ML.

Hàm (function / 함수) bất biến (invariant / 불변식) nếu

```math
f(Tx)=f(x).
```

Ví dụ ảnh (image / 이미지) classifier lý tưởng có thể muốn label không đổi dưới small translation.

Ánh xạ (mapping / 매핑) equivariant nếu

```math
f(Tx)=T'f(x).
```

Ví dụ segmentation mask nên shift cùng ảnh (image / 이미지) đầu vào (input / 입력).

Bất biến (invariant / 불변식) đầu ra (output / 출력) bỏ transformation tác động (effect / 효과); equivariant đầu ra (output / 출력) transform có cấu trúc cùng đầu vào (input / 입력).

## 14. Physics: symmetry và conservation laws

Trong physics, symmetry của laws liên hệ sâu với conserved quantities qua Noether's theorem.

Ví dụ:

- invariance theo thời gian (time / 시간) translation ↔ năng lượng (energy / 에너지) conservation;
- spatial translation ↔ momentum conservation;
- rotation symmetry ↔ angular momentum conservation.

Ý tưởng cốt lõi: nếu description vật lý không thay đổi dưới một continuous transformation, có cấu trúc (structure / 구조) được bảo toàn.

## 15. Computer Graphics: transformation chuỗi xử lý (pipeline / 파이프라인)

Một vertex thường đi qua:

```text
model
→ world
→ view
→ projection
→ screen
```

Mỗi stage là transformation có ngữ nghĩa (semantics / 의미론) riêng.

Một ma trận (matrix / 행렬) numerically correct vẫn có thể dùng sai nếu:

- multiplication thứ tự (order / 순서) sai;
- row-vector/column-vector convention bị mix;
- left-handed/right-handed hệ thống (system / 시스템) bị nhầm;
- object-space transform bị apply trong world không gian (space / 공간).

Hình học (geometry / 기하학) + ngữ nghĩa (semantics / 의미론) quan trọng hơn cú pháp (syntax / 문법) ma trận (matrix / 행렬).

## 16. Robotics: frames và rigid-body transforms

Rigid transformation trong 3D combine rotation `R` và translation `t`:

```math
x'=Rx+t.
```

Homogeneous form:

```math
\begin{bmatrix}
R&t\\
0&1
\end{bmatrix}.
```

Composition dùng ma trận (matrix / 행렬) products. Inverse cho phép chuyển đo lường (measurement / 측정) giữa sensor, robot và world frames.

Đây là practical ứng dụng (application / 애플리케이션) của affine transformations và group-like cấu trúc (structure / 구조).

## 17. AI: dữ liệu (data / 데이터) augmentation và symmetry các giả định (assumptions / 가정들)

Khi augment ảnh (image / 이미지) bằng crop/rotate/flip, ta đang encode belief rằng mục tiêu (target / 대상) hành vi (behavior / 동작) nên bất biến (invariant / 불변식)/equivariant dưới transformations đó.

Nếu giả định (assumption / 가정) sai, augmentation có thể harmful. Ví dụ flip chữ hoặc medical images có thể thay meaning.

Do đó symmetry trong ML không chỉ là trick; nó là prior về cấu trúc (structure / 구조) của tác vụ (task / 작업).

## 18. Finance: transformations của coordinate biểu diễn (representation / 표현)

Portfolio returns có thể chuyển từ asset basis sang factor basis. rủi ro (risk / 위험) biểu diễn (representation / 표현) thay đổi nhưng underlying economic exposure có thể được giữ dưới invertible coordinate thay đổi (change / 변경).

PCA cũng tìm rotation-like orthogonal basis nơi covariance trở nên diagonal.

Đây là cùng principle: chọn transformation để làm cấu trúc (structure / 구조) dễ đọc.

## 19. Active vs passive transformation

Một subtle distinction:

**Active transformation:** đối tượng (object / 객체)/véc-tơ (vector / 벡터) được move trong fixed coordinates.

**Passive transformation:** đối tượng (object / 객체) không đổi, coordinate basis thay đổi.

Hai viewpoints có formulas closely related nhưng inverse/convention khác nhau.

Nhiều nhầm lẫn trong mechanics, graphics và tensor calculus đến từ không nói rõ viewpoint.

## Mô hình tư duy (mental model / 사고 모델)

> Transformation là một hành động (action / 동작) lên không gian (space / 공간); symmetry là hành động (action / 동작) mà đối tượng (object / 객체) không thay đổi; invariants là properties transformation giữ lại. hình học (geometry / 기하학) trở nên sâu khi ta ngừng nhìn chỉ vào shapes và bắt đầu nhìn vào transformations giữa representations.

## Dùng chung (common / 공통) Misconceptions

**Mọi ma trận (matrix / 행렬) 2D là rotation.** Không; ma trận (matrix / 행렬) có thể quy mô (scale / 규모), shear, reflect hoặc collapse dimensions.

**Translation là tuyến tính (linear / 선형).** Không trong ordinary coordinates vì origin không được giữ; nó là affine.

**Transformation thứ tự (order / 순서) không quan trọng.** Sai trong general trường hợp (case / 사례); composition thường noncommutative.

**dữ liệu (data / 데이터) augmentation luôn tốt.** Chỉ khi chosen transformation thực sự preserve/equivariantly transform mục tiêu (target / 대상) ngữ nghĩa (semantics / 의미론).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 euclidean geometry](./00_euclidean_geometry.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
