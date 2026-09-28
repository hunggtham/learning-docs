# Đồng dạng, diện tích, thể tích và scaling laws: khi dimension quyết định tốc độ tăng

> **Mạch đọc:** Đọc **Đồng dạng, diện tích, thể tích và scaling laws: khi dimension quyết định tốc độ tăng** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Similarity là bảo toàn shape, không phải bảo toàn kích thước (size / 크기)** sang **Similar triangles: vì sao side ratios bằng nhau?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đồng dạng (similarity / 닮음) nói hai objects có cùng shape nhưng khác quy mô (scale / 규모). Ý tưởng này có vẻ elementary, nhưng nó là một trong những cửa ngõ quan trọng nhất từ school hình học (geometry / 기하학) sang dimensional phân tích (analysis / 분석), vật lý (physical / 물리적) scaling, xử lý ảnh (image processing / 이미지 처리), dữ liệu (data / 데이터) độ phức tạp (complexity / 복잡도) và high-dimensional thinking.

Nếu mọi length quy mô (scale / 규모) bởi factor `k`, area không quy mô (scale / 규모) `k` mà quy mô (scale / 규모) `k^2`; volume quy mô (scale / 규모) `k^3`. Reason không phải quy tắc (rule / 규칙) để nhớ, mà vì mỗi independent length dimension đóng góp một factor `k`.

## Similarity là bảo toàn shape, không phải bảo toàn kích thước (size / 크기)

Hai figures similar khi corresponding angles equal và corresponding lengths proportional.

Nếu quy mô (scale / 규모) factor là `k`:

```math
L'=kL.
```

Mọi corresponding length ratios đều bằng `k`.

Congruence là special trường hợp (case / 사례) `k=1`: same shape và same kích thước (size / 크기).

Similarity cho phép ta reason bằng ratios mà không cần biết absolute quy mô (scale / 규모).

## Similar triangles: vì sao side ratios bằng nhau?

Nếu hai triangles có same angles, corresponding sides quy mô (scale / 규모) uniformly. Có thể tưởng tượng one triangle là zoomed phiên bản (version / 버전) của other.

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

Giả định (assumption / 가정) quan trọng: same sun angle và ground approximately mức (level / 수준). Nếu measurements khác thời gian (time / 시간)/slope, proportional mô hình (model / 모델) breaks.

## Area scaling: vì sao exponent là 2?

Rectangle:

```math
A=LW.
```

Quy mô (scale / 규모) both lengths by `k`:

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

This has direct consequences for lưu trữ (storage / 저장소), material, weight, heat sức chứa (capacity / 용량) and voxel grids.

## Surface-to-volume ratio: why small things exchange faster

Surface area scales `k^2`; volume scales `k^3`. Therefore

```math
\frac{S}{V}
\propto
\frac1k.
```

As đối tượng (object / 객체) gets larger, surface per đơn vị (unit / 단위) volume decreases.

Consequences:

- small animals lose heat faster relative to body mass;
- small particles react/dissolve faster due to larger relative surface;
- cooling and heat-transfer designs depend on surface area;
- cells face vận chuyển (transport / 전송) các ràng buộc (constraints / 제약조건들) as kích thước (size / 크기) grows.

This is a geometric reason for many biological/kỹ thuật (engineering / 엔지니어링) scaling patterns.

## Scaling law không chỉ là hình học (geometry / 기하학)

General form:

```math
Q\propto L^\alpha.
```

Exponent `\alpha` says how quantity changes with characteristic quy mô (scale / 규모).

For ideal hình học (geometry / 기하학):

```text
length      α=1
area        α=2
volume      α=3
```

But real các hệ thống (systems / 시스템들) may have other exponents because các ràng buộc (constraints / 제약조건들), mạng (network / 네트워크) cấu trúc (structure / 구조) or fractal hình học (geometry / 기하학) alter effective dimension.

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

This is widely used in physics, biology, finance and mạng (network / 네트워크) science—but fitting a straight log-log line does not prove a true power-law cơ chế (mechanism / 메커니즘). dữ liệu (data / 데이터) phạm vi (range / 범위), noise mô hình (model / 모델) and alternatives matter.

## Ảnh (image / 이미지) resolution: 2D scaling in computing

Suppose ảnh (image / 이미지) width and height both doubled while điểm ảnh (pixel / 픽셀) density per coordinate đơn vị (unit / 단위) stays same.

Điểm ảnh (pixel / 픽셀) count multiplies by

```math
2\times2=4.
```

If each điểm ảnh (pixel / 픽셀) stores 4 bytes, raw bộ nhớ (memory / 메모리) also roughly ×4.

A mô hình (model / 모델) or filter with công việc (work / 작업) proportional to pixels may quy mô (scale / 규모) ×4 even though “resolution doubled” sounds like ×2.

This is why tuyến tính (linear / 선형) resolution and total dữ liệu (data / 데이터) kích thước (size / 크기) must be distinguished.

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

This is high-dimensional phiên bản (version / 버전) of area/volume scaling.

## Similarity and coordinate transformations

Uniform scaling ma trận (matrix / 행렬) in 2D:

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

This connects elementary hình học (geometry / 기하학) with tuyến tính (linear / 선형) algebra and Jacobian determinants: determinant measures cục bộ (local / 로컬) volume scaling.

## Non-uniform scaling

If x-direction scales `a` and y-direction scales `b`:

```math
S=
\begin{bmatrix}
a&0\\0&b
\end{bmatrix}.
```

Area quy mô (scale / 규모):

```math
|\det S|=|ab|.
```

Shape generally changes unless `a=b`, so transformation is not similarity in Euclidean sense.

Uniform scaling preserves angles; nonuniform scaling usually does not.

## Physics liên kết (connection / 연결) — square-cube law

Suppose an animal/cấu trúc (structure / 구조) is scaled geometrically by `k`.

Mass roughly follows volume:

```math
M\propto k^3.
```

Cross-sectional area supporting tải (load / 로드) may quy mô (scale / 규모) only:

```math
A\propto k^2.
```

So stress-like tải (load / 로드) per area can grow with `k`. A giant scaled-up animal cannot simply keep identical proportions and material strength.

This is why geometric similarity does not guarantee vật lý (physical / 물리적) similarity.

## Reynolds number and dimensionless similarity

In fluid mechanics, two geometrically similar các hệ thống (systems / 시스템들) can behave differently if dimensionless parameters differ. Reynolds number compares inertial and viscous effects.

This illustrates a deeper lesson: hình học (geometry / 기하학) gives one tầng (layer / 계층) of similarity; động (dynamic / 동적) similarity needs relevant dimensionless ratios to match too.

## Finance liên kết (connection / 연결) — scaling rủi ro (risk / 위험) with thời gian (time / 시간) is not always tuyến tính (linear / 선형)

Under ideal independent-return các giả định (assumptions / 가정들), variance of sum over `n` periods scales roughly `n`, while tiêu chuẩn (standard / 표준) deviation scales `\sqrt n`.

This is another scaling law, but exponent comes from probabilistic independence cấu trúc (structure / 구조), not geometric dimension.

Thus “how quantity scales” always reflects underlying cơ chế (mechanism / 메커니즘).

## AI liên kết (connection / 연결) — mô hình (model / 모델)/dữ liệu (data / 데이터) scaling

Compute, parameter count, ngữ cảnh (context / 맥락) length and dataset kích thước (size / 크기) interact through different powers. Attention with full pairwise đơn vị từ (token / 토큰) interactions has roughly quadratic sequence-length công việc (work / 작업):

```math
O(n^2).
```

Doubling chuỗi (sequence / 시퀀스) length can quadruple pairwise tương tác (interaction / 상호작용) count. This is analogous to area scaling: all pairs form a two-dimensional combinatorial grid.

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

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Uniform geometric scaling assumes same shape. Real vật lý (physical / 물리적) các hệ thống (systems / 시스템들) often violate material, gravity, heat-transfer or structural các ràng buộc (constraints / 제약조건들).

Power-law fit over narrow phạm vi (range / 범위) can be misleading. Log transformation changes lỗi (error / 오류) cấu trúc (structure / 구조). Similarity relations can thất bại (fail / 실패) when offsets/fixed costs exist.

High-dimensional dữ liệu (data / 데이터) often lies on lower-dimensional manifolds, so naive `k^d` grid thinking may overstate effective độ phức tạp (complexity / 복잡도) if exploitable cấu trúc (structure / 구조) exists.

## Mô hình tư duy (mental model / 사고 모델)

> Scaling asks how many independent directions are being enlarged and how the quantity depends on them. Each multiplicative dimension contributes a factor. Area, volume, determinant, voxel count, pairwise interactions and curse of dimensionality are variations of one idea: growth compounds across dimensions.

## Dùng chung (common / 공통) Misconceptions

**“Double kích thước (size / 크기) means double area/volume.”** Only lengths double; area ×4, volume ×8.

**“Objects that look similar behave physically the same.”** Geometric similarity does not guarantee động (dynamic / 동적)/material similarity.

**“Power-law line on log-log plot proves a power law.”** It does not; competing các mô hình (models / 모델들) and noise các giả định (assumptions / 가정들) matter.

**“Dimension is always an integer count of axes.”** Effective/fractal dimension can arise from scaling hành vi (behavior / 동작).

**“More resolution costs linearly.”** In 2D/3D/high-dimensional grids, dữ liệu (data / 데이터) kích thước (size / 크기) scales with powers of tuyến tính (linear / 선형) resolution.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 euclidean geometry](./00_euclidean_geometry.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
