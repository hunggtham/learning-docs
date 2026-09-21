# Đồng dạng, diện tích, thể tích và scaling laws: khi dimension quyết định tốc độ tăng

Đồng dạng (similarity / 닮음) nói hai objects có cùng shape nhưng khác scale. Ý tưởng này có vẻ elementary, nhưng nó là một trong những cửa ngõ quan trọng nhất từ school geometry sang dimensional analysis, physical scaling, image processing, data complexity và high-dimensional thinking.

Nếu mọi length scale bởi factor `k`, area không scale `k` mà scale `k^2`; volume scale `k^3`. Reason không phải rule để nhớ, mà vì mỗi independent length dimension đóng góp một factor `k`.

## Similarity là bảo toàn shape, không phải bảo toàn size

Hai figures similar khi corresponding angles equal và corresponding lengths proportional.

Nếu scale factor là `k`:

```math
L'=kL.
```

Mọi corresponding length ratios đều bằng `k`.

Congruence là special case `k=1`: same shape và same size.

Similarity cho phép ta reason bằng ratios mà không cần biết absolute scale.

## Similar triangles: vì sao side ratios bằng nhau?

Nếu hai triangles có same angles, corresponding sides scale uniformly. Có thể tưởng tượng one triangle là zoomed version của other.

Do đó:

```math
\frac{a'}a
=
\frac{b'}b
=
\frac{c'}c
=k.
```

Đây là foundation của trigonometric ratios. Sine/cosine depend only on angle vì all right triangles with same acute angle are similar.

## Worked example — đo chiều cao bằng shadow

Một person cao 1.8 m tạo shadow dài 1.2 m. Cùng lúc, building shadow dài 20 m.

Sun angle same, nên triangles similar:

```math
\frac{h_{building}}{20}
=
\frac{1.8}{1.2}.
```

Thus

```math
h_{building}
=20\times1.5
=30\text{ m}.
```

Assumption quan trọng: same sun angle và ground approximately level. Nếu measurements khác time/slope, proportional model breaks.

## Area scaling: vì sao exponent là 2?

Rectangle:

```math
A=LW.
```

Scale both lengths by `k`:

```math
A'
=(kL)(kW)
=k^2LW
=k^2A.
```

Same principle applies to any similar planar shape, not just rectangles. Area has dimension length².

Double all lengths:

```math
k=2
\Rightarrow
A'=4A.
```

This surprises intuition because “twice as wide and twice as tall” multiplies, not adds.

## Volume scaling: exponent 3

Box:

```math
V=LWH.
```

Uniform scaling:

```math
V'
=(kL)(kW)(kH)
=k^3V.
```

Double side lengths → volume ×8.

This has direct consequences for storage, material, weight, heat capacity and voxel grids.

## Surface-to-volume ratio: why small things exchange faster

Surface area scales `k^2`; volume scales `k^3`. Therefore

```math
\frac{S}{V}
\propto
\frac1k.
```

As object gets larger, surface per unit volume decreases.

Consequences:

- small animals lose heat faster relative to body mass;
- small particles react/dissolve faster due to larger relative surface;
- cooling and heat-transfer designs depend on surface area;
- cells face transport constraints as size grows.

This is a geometric reason for many biological/engineering scaling patterns.

## Scaling law không chỉ là geometry

General form:

```math
Q\propto L^\alpha.
```

Exponent `\alpha` says how quantity changes with characteristic scale.

For ideal geometry:

```text
length      α=1
area        α=2
volume      α=3
```

But real systems may have other exponents because constraints, network structure or fractal geometry alter effective dimension.

## Log-log plots reveal power laws

If

```math
Q=cL^\alpha,
```

take logs:

```math
\log Q
=
\log c+\alpha\log L.
```

On log-log coordinates, ideal power law becomes a line with slope `\alpha`.

This is widely used in physics, biology, finance and network science—but fitting a straight log-log line does not prove a true power-law mechanism. Data range, noise model and alternatives matter.

## Image resolution: 2D scaling in computing

Suppose image width and height both doubled while pixel density per coordinate unit stays same.

Pixel count multiplies by

```math
2\times2=4.
```

If each pixel stores 4 bytes, raw memory also roughly ×4.

A model or filter with work proportional to pixels may scale ×4 even though “resolution doubled” sounds like ×2.

This is why linear resolution and total data size must be distinguished.

## 3D voxel grids: cubic explosion

Double resolution in x, y, z:

```math
2^3=8.
```

Voxels ×8.

Triple resolution:

```math
3^3=27.
```

This quickly makes 3D simulations, medical imaging and volumetric neural networks memory-heavy.

## Curse of dimensionality as generalized scaling

If each of `d` dimensions has `k` grid positions, total grid cells:

```math
k^d.
```

Here exponent is dimension itself. Even moderate `k` becomes huge when `d` large.

For `k=10`, `d=8`:

```math
10^8=100,000,000.
```

This is high-dimensional version of area/volume scaling.

## Similarity and coordinate transformations

Uniform scaling matrix in 2D:

```math
S=
\begin{bmatrix}
k&0\\0&k
\end{bmatrix}.
```

Its determinant:

```math
\det S=k^2,
```

which exactly equals area scaling factor.

In 3D uniform scaling determinant is `k^3`.

This connects elementary geometry with linear algebra and Jacobian determinants: determinant measures local volume scaling.

## Non-uniform scaling

If x-direction scales `a` and y-direction scales `b`:

```math
S=
\begin{bmatrix}
a&0\\0&b
\end{bmatrix}.
```

Area scale:

```math
|\det S|=|ab|.
```

Shape generally changes unless `a=b`, so transformation is not similarity in Euclidean sense.

Uniform scaling preserves angles; nonuniform scaling usually does not.

## Physics connection — square-cube law

Suppose an animal/structure is scaled geometrically by `k`.

Mass roughly follows volume:

```math
M\propto k^3.
```

Cross-sectional area supporting load may scale only:

```math
A\propto k^2.
```

So stress-like load per area can grow with `k`. A giant scaled-up animal cannot simply keep identical proportions and material strength.

This is why geometric similarity does not guarantee physical similarity.

## Reynolds number and dimensionless similarity

In fluid mechanics, two geometrically similar systems can behave differently if dimensionless parameters differ. Reynolds number compares inertial and viscous effects.

This illustrates a deeper lesson: geometry gives one layer of similarity; dynamic similarity needs relevant dimensionless ratios to match too.

## Finance connection — scaling risk with time is not always linear

Under ideal independent-return assumptions, variance of sum over `n` periods scales roughly `n`, while standard deviation scales `\sqrt n`.

This is another scaling law, but exponent comes from probabilistic independence structure, not geometric dimension.

Thus “how quantity scales” always reflects underlying mechanism.

## AI connection — model/data scaling

Compute, parameter count, context length and dataset size interact through different powers. Attention with full pairwise token interactions has roughly quadratic sequence-length work:

```math
O(n^2).
```

Doubling sequence length can quadruple pairwise interaction count. This is analogous to area scaling: all pairs form a two-dimensional combinatorial grid.

## Fractal dimension: effective scaling can be non-integer

For some complex shapes, measured detail scales like

```math
N(\epsilon)
\propto
\epsilon^{-D}
```

with non-integer `D`.

Coastlines, branching patterns and strange attractors can have effective dimensions between familiar integer values.

This shows dimension is fundamentally a scaling concept, not only “number of axes”.

## Assumptions và failure modes

Uniform geometric scaling assumes same shape. Real physical systems often violate material, gravity, heat-transfer or structural constraints.

Power-law fit over narrow range can be misleading. Log transformation changes error structure. Similarity relations can fail when offsets/fixed costs exist.

High-dimensional data often lies on lower-dimensional manifolds, so naive `k^d` grid thinking may overstate effective complexity if exploitable structure exists.

## Mental Model

> Scaling asks how many independent directions are being enlarged and how the quantity depends on them. Each multiplicative dimension contributes a factor. Area, volume, determinant, voxel count, pairwise interactions and curse of dimensionality are variations of one idea: growth compounds across dimensions.

## Common Misconceptions

**“Double size means double area/volume.”** Only lengths double; area ×4, volume ×8.

**“Objects that look similar behave physically the same.”** Geometric similarity does not guarantee dynamic/material similarity.

**“Power-law line on log-log plot proves a power law.”** It does not; competing models and noise assumptions matter.

**“Dimension is always an integer count of axes.”** Effective/fractal dimension can arise from scaling behavior.

**“More resolution costs linearly.”** In 2D/3D/high-dimensional grids, data size scales with powers of linear resolution.