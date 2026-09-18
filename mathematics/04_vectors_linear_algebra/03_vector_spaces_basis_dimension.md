# Không gian vector, cơ sở và số chiều

Không gian vector (Vector space / 벡터공간) là tập các objects có thể cộng và scalar-multiply theo rules nhất quán. Các objects không nhất thiết là geometric arrows; chúng có thể là polynomials, functions, signals hoặc matrices.

## Span

Cho vectors `v_1,...,v_k`, span là mọi linear combinations:

```math
\operatorname{span}\{v_1,\ldots,v_k\}
=
\left\{\sum_i c_iv_i\right\}
```

Trong 3D, một nonzero vector span một line qua origin; hai independent vectors span a plane; ba independent vectors có thể span toàn `R^3`.

## Linear independence

Vectors independent nếu equation

```math
c_1v_1+\cdots+c_kv_k=0
```

chỉ có solution all coefficients zero.

Nếu có nontrivial solution, một vector có thể được express từ others, nghĩa information redundancy.

Trong feature engineering, highly dependent features không thêm independent dimension và có thể gây multicollinearity.

## Basis

Basis là tập vừa linearly independent vừa span whole space. Nó là minimal coordinate system đủ để represent mọi vector uniquely.

Standard basis `R^3`:

```math
e_1=(1,0,0),\quad e_2=(0,1,0),\quad e_3=(0,0,1)
```

nhưng vô số bases khác tồn tại.

## Dimension

Dimension là number of vectors trong any basis của space. Tính chất sâu là mọi bases của finite-dimensional vector space có cùng cardinality.

Dimension đo degrees of freedom độc lập cần để mô tả state.

## Change of basis

Một vector vật lý không đổi khi đổi basis; chỉ coordinates đổi. Nếu basis phù hợp problem, computation đơn giản hơn.

PCA chọn basis theo directions variance lớn của data. Fourier transform đổi signal từ time-coordinate basis sang frequency basis. Cả hai là examples “same object, new coordinates”.

## Subspace

Subspace là subset cũng là vector space dưới same operations. Column space, null space, eigenspaces đều là subspaces.

Nếu subspace không chứa zero vector, nó không thể là linear subspace. Một affine plane không qua origin là translated subspace, không phải subspace strict.

## Orthogonal basis

Nếu basis vectors mutually orthogonal và normalized, coordinates dễ tính qua dot products. Orthonormal basis giúp numerical stability và giải thích projections.

## Curse of dimensionality

Higher dimension cho expressive capacity nhưng geometry trở nên counterintuitive. Grid có `k` values mỗi dimension thì total points `k^d`, exponential theo dimension `d`.

Nearest-neighbor distances cũng có thể concentrate; data trở nên sparse relative to volume. Vì vậy nhiều ML methods cần dimensionality reduction, regularization hoặc assumptions về lower-dimensional structure.

## Mental Model

> Vector space là universe của allowable linear combinations. Basis là bộ “trục tư duy” tối thiểu để mô tả mọi state; dimension là số independent degrees of freedom.

## Common Misconceptions

Basis không unique; dimension thì invariant. Nhiều coordinates không nhất thiết nhiều information nếu vectors/features dependent. Affine set không qua origin không phải linear subspace.
