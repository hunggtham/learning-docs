# Đồng dạng, diện tích, thể tích và scaling laws

Đồng dạng (Similarity / 닮음) nói hai objects có cùng shape nhưng khác scale. Nếu mọi length scale bởi factor `k`, area scale bởi `k^2`, volume bởi `k^3`. Đây là một trong những examples rõ nhất về cách dimension quyết định power law.

## Length scaling

Nếu original length `L`, scaled:

```math
L'=kL.
```

Perimeter cũng linear theo `k` vì là sum lengths.

## Area scaling

Rectangle:

```math
A=LW.
```

Scale cả dimensions:

```math
A'=(kL)(kW)=k^2A.
```

Vì area có hai independent length dimensions.

Nếu phóng ảnh width và height gấp 2, pixel area requirement ở same density tăng khoảng 4 lần.

## Volume scaling

Box:

```math
V=LWH.
```

Scale mỗi dimension `k`:

```math
V'=k^3V.
```

Một cube side gấp 2 có volume gấp 8.

## Surface-to-volume ratio

Surface area scale `k^2`, volume scale `k^3`, nên ratio

```math
\frac{surface}{volume}
```

scale như `1/k`.

Điều này ảnh hưởng heat loss, biology và engineering. Smaller objects có surface relative volume lớn hơn, nên exchange với environment proportionally mạnh hơn.

## Similar triangles và indirect measurement

Nếu triangles similar, corresponding side ratios equal. Shadows có thể dùng để đo height: cùng sun angle tạo similar right triangles.

Nếu người cao `h_p` có shadow `s_p`, building shadow `s_b`, thì

```math
\frac{h_b}{s_b}=\frac{h_p}{s_p}
```

nên

```math
h_b=s_b\frac{h_p}{s_p}.
```

Đây là modeling dựa trên same angle assumption.

## Resolution và computing

Nếu tăng linear resolution image từ 1080p-like dimensions theo factor 2 mỗi chiều, pixel count tăng factor 4. Memory, processing và bandwidth có thể tăng gần theo pixel count nếu các factors khác constant.

3D voxel grid tăng nghiêm trọng hơn: double resolution mỗi spatial dimension làm voxel count tăng factor 8.

Đây là curse of dimensionality ở một form trực quan: scale theo mỗi dimension nhân vào nhau.

## Power laws

General dimensional reasoning: quantity phụ thuộc characteristic length `L` theo dimension `d` thường scale approximately

```math
Q\propto L^d.
```

Nhưng real systems có constraints khác nên không được assume blindly. Fractals thậm chí có effective non-integer dimension.

## Mental Model

> Scale không chỉ làm object “to hơn”. Mỗi independent dimension đóng góp một factor scale. Vì vậy length, area, volume và high-dimensional data growth có powers khác nhau.

## Common Misconceptions

Double diameter không double area/volume. Similarity cần uniform scale và corresponding angles, không chỉ “nhìn giống”. Scaling laws là model; physical properties khác có thể không scale đơn giản cùng geometry.
