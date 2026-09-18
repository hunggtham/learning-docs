# Hình học tọa độ: biến không gian thành algebra

Hình học tọa độ (Analytic geometry / 해석기하학) nối geometry với algebra bằng cách gán numbers cho positions. Khi point trở thành tuple `(x,y)`, questions hình học có thể được giải bằng equations.

## Cartesian coordinates

Trong 2D, hai perpendicular axes xác định mỗi point bởi ordered pair `(x,y)`. `x` cho displacement horizontal từ origin, `y` vertical.

Trong 3D thêm `z`. Trong higher dimensions, point có thể là vector `(x_1,...,x_n)`, dù ta không còn visualize trực tiếp.

## Distance formula

Giữa points `P(x_1,y_1)` và `Q(x_2,y_2)`, horizontal difference là

```math
\Delta x=x_2-x_1
```

vertical difference:

```math
\Delta y=y_2-y_1
```

Pythagorean theorem cho

```math
d=\sqrt{(\Delta x)^2+(\Delta y)^2}
```

Trong `n` dimensions:

```math
d(\mathbf x,\mathbf y)=\sqrt{\sum_{i=1}^n(x_i-y_i)^2}
```

Đây là Euclidean distance và chính là L2 norm của difference vector.

## Midpoint

Midpoint là average coordinates:

```math
M=\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\right)
```

Tại sao average? Vì midpoint phải nằm half-way theo mỗi axis; parameterization line segment

```math
P+t(Q-P)
```

với `t=1/2` cho formula này.

## Slope

Slope line qua hai points:

```math
m=\frac{y_2-y_1}{x_2-x_1}
```

là ratio vertical change trên horizontal change. Nếu denominator 0, line vertical và slope theo representation này undefined.

Slope liên hệ tangent angle `θ` qua

```math
m=\tan\theta
```

khi line không vertical.

## Equation of a line

Point-slope form:

```math
y-y_1=m(x-x_1)
```

nói displacement từ point known phải follow slope ratio.

General form:

```math
Ax+By+C=0
```

có vector normal `(A,B)` perpendicular với line. Representation này hữu ích vì vertical lines không cần special case `x=c` ngoài form general.

## Circle equation

Circle center `(h,k)`, radius `r` là set points distance `r` từ center:

```math
(x-h)^2+(y-k)^2=r^2
```

Equation không cần học thuộc nếu nhớ definition circle = constant-distance locus.

## Conic sections

Parabola, ellipse và hyperbola có thể định nghĩa bằng distance relationships. Parabola là set points equidistant from a focus và directrix. Ellipse có constant sum of distances tới hai foci; hyperbola có constant absolute difference.

Các definitions này giải thích optical properties và orbital models tốt hơn chỉ nhớ standard equations.

## Coordinate transforms

Đổi coordinate system không nhất thiết đổi geometric object. Một point physical có thể có coordinates khác dưới origin/basis khác.

Trong graphics, world coordinates, camera coordinates và screen coordinates là các representations của cùng scene qua transformations.

## Mental Model

> Coordinate geometry gắn một numerical address cho position. Sau đó distance, angle và shape trở thành equations. Geometry không biến mất; algebra chỉ trở thành ngôn ngữ tính toán của geometry.

## Common Misconceptions

Coordinates không phải bản thân point; chúng phụ thuộc coordinate system. Slope undefined cho vertical line không có nghĩa line “không có direction”. Distance formula là Pythagorean theorem áp vào coordinate differences.

## Worked Example: distance từ point tới line

Line

```math
Ax+By+C=0
```

có normal vector `n=(A,B)`. Với point `P=(x_0,y_0)`, signed projection của displacement lên unit normal dẫn tới distance

```math
d=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}
```

Numerator đo line equation residual tại point; denominator normalize length của normal. Đây là bridge trực tiếp từ analytic geometry tới projection trong linear algebra.

## Coordinate system và numerical data

Latitude/longitude không phải Cartesian coordinates trên flat plane toàn cầu. Nếu tính distance xa bằng Euclidean formula trực tiếp trên degrees, model geometry sai. Geographic systems cần spherical/ellipsoidal geometry hoặc suitable map projection. Đây là ví dụ điển hình cho việc “có coordinates” không đồng nghĩa Euclidean distance hợp lệ.
