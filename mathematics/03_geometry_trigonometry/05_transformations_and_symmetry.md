# Phép biến hình và đối xứng

Phép biến hình (Geometric transformation / 기하변환) là mapping biến points thành points. Thay vì chỉ hỏi object có shape gì, transformation viewpoint hỏi: sau khi move, rotate, reflect hoặc scale, properties nào thay đổi và properties nào giữ nguyên?

## Translation

Translation bởi vector `t`:

```math
x' = x+t
```

bảo toàn distance, angles, orientation. Trong coordinates 2D:

```math
(x,y)\mapsto(x+a,y+b).
```

## Rotation

Rotation quanh origin dùng matrix:

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
```

`R` bảo toàn length vì

```math
R^TR=I.
```

Matrices với property này là orthogonal matrices; determinant +1 tương ứng proper rotations.

## Reflection

Reflection qua x-axis:

```math
(x,y)\mapsto(x,-y).
```

Bảo toàn distances/angles nhưng đảo orientation.

## Scaling

Uniform scale `k`:

```math
(x,y)\mapsto(kx,ky).
```

Length multiply `|k|`, area `k^2`.

Non-uniform scaling có factors khác theo axes và không bảo toàn angles generally.

## Composition

Nếu apply rotation rồi translation, whole operation là composition. Order thường matter:

```text
rotate then translate ≠ translate then rotate
```

Đây là lý do transformation pipelines cần quy ước multiplication order rõ ràng.

## Homogeneous coordinates

Linear matrices thông thường không represent translation chỉ bằng multiplication trên `(x,y)`. Graphics thêm coordinate 1:

```math
\begin{bmatrix}x\\y\\1\end{bmatrix}
```

và dùng 3×3 affine matrix, cho phép translation, rotation, scaling compose dưới matrix multiplication.

3D graphics dùng 4×4 homogeneous matrices tương tự.

## Symmetry

Symmetry là transformation để object trông không đổi. Circle invariant dưới mọi rotation quanh center; square invariant dưới rotations multiples 90° và certain reflections.

Group theory nghiên cứu algebra của symmetries. Physics dùng symmetry để tìm conservation laws; ML có equivariant architectures cố respect known transformation structure.

## Invariance vs equivariance

Invariant function thỏa conceptually:

```math
f(Tx)=f(x).
```

Equivariant mapping thỏa:

```math
f(Tx)=T'f(x).
```

Classification có thể muốn object label invariant dưới small translations; segmentation output lại nên shift cùng input, tức equivariance.

## Mental Model

> Transformation viewpoint biến geometry từ việc đo từng shape thành việc nghiên cứu actions trên space và invariants của actions. Đây là bridge trực tiếp tới matrices, group theory, graphics và modern ML.

## Common Misconceptions

Mọi matrix 2D không phải rotation. Translation không phải linear transformation trên ordinary coordinate vectors vì origin không giữ nguyên. Order của transformations thường không commutative.
