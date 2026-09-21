# Phép biến hình và đối xứng: transformations, invariants và symmetry

Phép biến hình (geometric transformation / 기하변환) là một mapping biến points thành points. Thay vì chỉ hỏi “shape này trông như thế nào?”, transformation viewpoint hỏi câu sâu hơn:

> Nếu ta move, rotate, reflect, scale hoặc change coordinates, properties nào thay đổi và properties nào được bảo toàn?

Câu hỏi về **invariants** này là bridge trực tiếp từ geometry sang matrices, group theory, physics, computer graphics và modern machine learning.

## 1. Transformation là một function trên space

Nếu space là `S`, transformation có thể viết

```math
T:S\to S.
```

Mỗi point `x` được map tới point mới `T(x)`.

Một transformation có thể đại diện cho nhiều ý nghĩa:

- object thực sự di chuyển trong một fixed frame;
- coordinate frame thay đổi còn object đứng yên;
- data được normalized/augmented;
- state của system chuyển sang state mới.

Do đó trước khi thao tác formula cần rõ interpretation của transformation.

## 2. Translation: move mà không đổi shape

Translation bởi vector `t`:

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

Nhưng nó không phải linear transformation trên ordinary position vectors vì

```math
T(0)=t\ne0.
```

Nó là affine transformation.

## 3. Rotation: preserve inner-product geometry

Rotation quanh origin angle `\theta`:

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Với vector `x`, rotated vector là

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

Khai triển matrix multiplication cho ra sine/cosine addition identities.

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

Matrix:

```math
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}.
```

Reflection preserve length/angle nhưng determinant bằng `-1`, biểu thị orientation bị đảo.

Rotation matrix 2D có determinant `+1`.

Determinant vì vậy không chỉ đo volume scaling; sign còn encode orientation change.

## 6. Scaling: uniform và non-uniform khác nhau

Uniform scaling:

```math
x\mapsto kx.
```

Length scale `|k|`, area scale `k^2`, volume scale `|k|^3` trong 3D.

Nếu scale khác nhau theo axes:

```math
S=
\begin{bmatrix}
a&0\\
0&b
\end{bmatrix},
```

thì circle thường thành ellipse nếu `a\ne b`.

Non-uniform scaling không preserve angles nói chung. Do đó “scale” không phải một class invariance duy nhất.

## 7. Shear: shape change mà area có thể giữ

Shear matrix:

```math
H=
\begin{bmatrix}
1&k\\
0&1
\end{bmatrix}.
```

Nó nghiêng shape mà determinant vẫn bằng 1, nên area preserved dù angles không preserved.

Đây là example quan trọng: same determinant không nghĩa same geometry. Determinant chỉ capture volume scaling, không capture mọi distortion.

## 8. Affine transformations

Affine map có dạng

```math
T(x)=Ax+b.
```

`A` xử lý linear part; `b` translation.

Affine transformations preserve:

- lines;
- parallelism;
- ratios dọc cùng line;
- affine combinations.

Nhưng chúng không nhất thiết preserve lengths hay angles.

Computer graphics và computer vision dùng affine models rất nhiều vì chúng đủ flexible nhưng vẫn algebraically manageable.

## 9. Homogeneous coordinates: biến affine composition thành matrix multiplication

Translation không represent được bằng ordinary `2×2` linear matrix trên `(x,y)`. Ta augment coordinate:

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

Giờ translation, rotation, scale, shear có thể compose bằng matrix multiplication.

Trong 3D, graphics thường dùng `4×4` homogeneous matrices.

## 10. Order matters vì composition thường không commutative

Nói chung

```math
T_2\circ T_1\ne T_1\circ T_2.
```

Ví dụ rotate object quanh origin rồi translate khác với translate trước rồi rotate; ở case thứ hai translation vector cũng bị rotation tác động.

Đây là nguồn bug phổ biến trong graphics engines và robotics transforms.

### Worked intuition

Point `(1,0)`:

1. rotate 90° → `(0,1)`;
2. translate `(1,0)` → `(1,1)`.

Nếu translate trước:

1. `(1,0)+(1,0)=(2,0)`;
2. rotate 90° → `(0,2)`.

Kết quả khác nhau.

## 11. Symmetry là transformation làm object invariant

Object có symmetry nếu tồn tại transformation `T` sao cho

```math
T(X)=X
```

ở mức object/set.

Circle invariant dưới mọi rotation quanh center.

Square invariant dưới rotations multiples 90° và một số reflections.

Symmetry không chỉ là aesthetic property; nó nói object có redundant descriptions dưới certain transformations.

## 12. Symmetries tạo group structure

Các symmetries của một object có thể compose. Chúng có:

- identity transformation;
- closure dưới composition;
- inverse;
- associativity.

Đó chính là group structure.

Vì vậy group theory xuất hiện tự nhiên từ geometry: nó formalize algebra của transformations giữ object unchanged.

## 13. Invariance và equivariance

Hai ideas này đặc biệt quan trọng trong ML.

Function invariant nếu

```math
f(Tx)=f(x).
```

Ví dụ image classifier lý tưởng có thể muốn label không đổi dưới small translation.

Mapping equivariant nếu

```math
f(Tx)=T'f(x).
```

Ví dụ segmentation mask nên shift cùng image input.

Invariant output bỏ transformation effect; equivariant output transform có cấu trúc cùng input.

## 14. Physics: symmetry và conservation laws

Trong physics, symmetry của laws liên hệ sâu với conserved quantities qua Noether's theorem.

Ví dụ:

- invariance theo time translation ↔ energy conservation;
- spatial translation ↔ momentum conservation;
- rotation symmetry ↔ angular momentum conservation.

Ý tưởng cốt lõi: nếu description vật lý không thay đổi dưới một continuous transformation, có structure được bảo toàn.

## 15. Computer Graphics: transformation pipeline

Một vertex thường đi qua:

```text
model
→ world
→ view
→ projection
→ screen
```

Mỗi stage là transformation có semantics riêng.

Một matrix numerically correct vẫn có thể dùng sai nếu:

- multiplication order sai;
- row-vector/column-vector convention bị mix;
- left-handed/right-handed system bị nhầm;
- object-space transform bị apply trong world space.

Geometry + semantics quan trọng hơn syntax matrix.

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

Composition dùng matrix products. Inverse cho phép chuyển measurement giữa sensor, robot và world frames.

Đây là practical application của affine transformations và group-like structure.

## 17. AI: data augmentation và symmetry assumptions

Khi augment image bằng crop/rotate/flip, ta đang encode belief rằng target behavior nên invariant/equivariant dưới transformations đó.

Nếu assumption sai, augmentation có thể harmful. Ví dụ flip chữ hoặc medical images có thể thay meaning.

Do đó symmetry trong ML không chỉ là trick; nó là prior về structure của task.

## 18. Finance: transformations của coordinate representation

Portfolio returns có thể chuyển từ asset basis sang factor basis. Risk representation thay đổi nhưng underlying economic exposure có thể được giữ dưới invertible coordinate change.

PCA cũng tìm rotation-like orthogonal basis nơi covariance trở nên diagonal.

Đây là cùng principle: chọn transformation để làm structure dễ đọc.

## 19. Active vs passive transformation

Một subtle distinction:

**Active transformation:** object/vector được move trong fixed coordinates.

**Passive transformation:** object không đổi, coordinate basis thay đổi.

Hai viewpoints có formulas closely related nhưng inverse/convention khác nhau.

Nhiều nhầm lẫn trong mechanics, graphics và tensor calculus đến từ không nói rõ viewpoint.

## Mental Model

> Transformation là một action lên space; symmetry là action mà object không thay đổi; invariants là properties transformation giữ lại. Geometry trở nên sâu khi ta ngừng nhìn chỉ vào shapes và bắt đầu nhìn vào transformations giữa representations.

## Common Misconceptions

**Mọi matrix 2D là rotation.** Không; matrix có thể scale, shear, reflect hoặc collapse dimensions.

**Translation là linear.** Không trong ordinary coordinates vì origin không được giữ; nó là affine.

**Transformation order không quan trọng.** Sai trong general case; composition thường noncommutative.

**Data augmentation luôn tốt.** Chỉ khi chosen transformation thực sự preserve/equivariantly transform target semantics.
