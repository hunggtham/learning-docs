# Hình học Euclid: từ trực giác không gian đến cấu trúc bất biến

Hình học Euclid (Euclidean geometry / 유클리드 기하학) là mô hình toán học của không gian “phẳng” mà ta gặp trong phần lớn bài toán hình học phổ thông, cơ học cổ điển, bản vẽ kỹ thuật và nhiều hệ tọa độ cục bộ trong computing. Điều quan trọng không phải chỉ là nhớ công thức diện tích hay góc, mà là hiểu **space đang cho phép những quan hệ nào giữa điểm, đường, khoảng cách, góc và phép biến hình**.

Một chapter hình học tốt cần trả lời hai câu hỏi song song:

1. object nào đang được mô tả?
2. property nào không đổi khi ta di chuyển hoặc biểu diễn object theo cách khác?

Đây là bridge trực tiếp sang vector, matrix, symmetry, topology, graphics và physics.

## 1. Từ vật thể thật đến object lý tưởng

Điểm (point / 점) là một vị trí không có kích thước. Đường thẳng (line / 직선) là object một chiều kéo dài vô hạn hai phía. Mặt phẳng (plane / 평면) là object hai chiều vô hạn.

Trong thực tế, nét bút có thickness và mặt bàn không hoàn toàn phẳng. Geometry bỏ các chi tiết vật lý đó để giữ lại structure của vị trí và quan hệ.

Đây là ví dụ đầu tiên về mathematical modeling:

```text
real object
→ ignore irrelevant physical detail
→ keep geometric relation
→ reason in ideal model
```

Khi dùng kết quả hình học cho đời thực, ta luôn phải nhớ bước quay lại model: nếu object vật lý cong, biến dạng hoặc measurement có noise, Euclidean result chỉ là approximation.

## 2. Axiom: toán học không bắt đầu từ hư không

Một hệ hình học cần axioms/postulates — các quy tắc nền được chấp nhận làm starting point.

Một postulate đặc trưng của Euclidean geometry là parallel postulate: qua một point ngoài một line, có đúng một line song song với line đó.

Điều này nghe hiển nhiên vì trực giác của ta được xây từ không gian gần phẳng. Nhưng nếu đổi model space, statement không còn đúng.

Trên sphere, “đường thẳng tự nhiên” được thay bằng geodesic như great circle. Hai great circles thường giao nhau. Vì vậy theorem hình học phải luôn được hiểu cùng assumptions về space.

## 3. Distance là structure, không chỉ là formula

Khoảng cách (distance / 거리) là một function đo separation giữa points.

Trong Euclidean plane, nếu hai points có difference vector

```math
(\Delta x,\Delta y),
```

thì Pythagoras cho

```math
d=\sqrt{(\Delta x)^2+(\Delta y)^2}.
```

Formula này không phải definition phổ quát của “distance”. Nó là distance do Euclidean inner-product structure tạo ra.

Một metric nói chung cần các tính chất như:

```text
non-negativity
identity of indiscernibles
symmetry
triangle inequality
```

Do đó Manhattan distance, graph shortest-path distance hay cosine distance-like measures có thể phù hợp hơn trong domain khác.

## 4. Góc là quan hệ giữa directions

Góc (angle / 각) đo độ quay giữa hai rays/directions.

Degree chia full rotation thành 360 phần. Radian dùng arc length:

```math
\theta=\frac{s}{r}.
```

Vì vậy

```math
s=r\theta.
```

Radian là natural unit vì nó không cần conversion constant khi làm calculus. Các limits nền như

```math
\lim_{x\to0}\frac{\sin x}{x}=1
```

chỉ có form sạch như vậy khi `x` đo bằng radian.

## 5. Congruence: cùng shape và cùng size

Hai figures congruent (합동 / congruent) nếu có thể đưa trùng nhau bằng rigid transformations: translation, rotation hoặc reflection.

Rigid transformation bảo toàn distance. Vì distance được bảo toàn, angle cũng được bảo toàn.

Đây là một idea sâu: thay vì so từng cạnh/góc riêng lẻ, ta có thể hỏi liệu có một transformation bảo toàn structure đưa object A thành object B hay không.

Trong modern mathematics, classification thông qua allowed transformations là một strategy rất phổ biến.

## 6. Similarity: cùng shape, khác scale

Hai figures similar (닮음 / similarity) khi angles tương ứng bằng nhau và lengths tương ứng theo cùng một scale factor.

Nếu scale factor là `k`, thì

```math
L' = kL,
```

area scale:

```math
A'=k^2A,
```

và volume scale:

```math
V'=k^3V.
```

Điều này không phải ba rule riêng. Nó đến từ số dimensions độc lập đóng góp factor `k`.

Similarity nối geometry với dimensional analysis, image resizing, map scale và square-cube law trong biology/engineering.

## 7. Triangle là primitive structure của Euclidean geometry

Triangle đặc biệt vì ba non-collinear points xác định một shape tối giản trong plane.

Các theorem về congruence như SSS, SAS, ASA không chỉ là exam rules; chúng nói lượng information tối thiểu nào đủ để xác định triangle duy nhất đến rigid motion.

Ví dụ, biết ba cạnh `a,b,c` thỏa triangle inequality:

```math
a+b>c,
```

và cyclic variants, thì triangle được xác định đến congruence.

Triangle inequality phản ánh ý tưởng: đường đi trực tiếp giữa hai points không dài hơn đường vòng qua point thứ ba.

## 8. Tổng góc tam giác và assumption Euclidean

Trong Euclidean plane:

```math
\alpha+\beta+\gamma=\pi.
```

Một proof idea là kẻ line qua một vertex song song với cạnh đối diện rồi dùng alternate interior angles.

Proof này dùng parallel postulate. Vì vậy theorem không hoàn toàn “tự nhiên” ngoài context Euclidean.

Trên sphere, triangle angle sum có thể lớn hơn `π`; trong hyperbolic geometry có thể nhỏ hơn `π`.

Đây là lesson quan trọng về theorem assumptions: proof cho ta biết theorem đang dựa vào structure nào.

## 9. Pythagoras như orthogonal decomposition

Trong right triangle:

```math
c^2=a^2+b^2.
```

Ở mức sâu hơn, theorem nói squared norm cộng được theo các directions orthogonal:

```math
\|u+v\|^2=\|u\|^2+\|v\|^2
```

khi

```math
u\cdot v=0.
```

Vì vậy Pythagoras không dừng ở geometry school; nó đi thẳng sang vectors, least squares, variance decomposition và Hilbert-space intuition.

## 10. Circle là locus của constant distance

Circle center `c` radius `r` được định nghĩa bởi

```math
\|x-c\|=r.
```

Trong Cartesian coordinates:

```math
(x-h)^2+(y-k)^2=r^2.
```

Equation đến từ definition, không cần học thuộc độc lập.

Circle symmetry giải thích nhiều tính chất: mọi rotation quanh center giữ circle không đổi.

Trong physics và engineering, symmetry thường giúp giảm số variables cần xét.

## 11. Area là measure phải tương thích với decomposition

Area không chỉ là collection formulas. Ta muốn một measure có tính chất:

- nonnegative;
- congruent figures có same area;
- nếu figure chia thành non-overlapping parts thì total area bằng sum parts.

Rectangle:

```math
A=wh.
```

Triangle:

```math
A=\frac12bh
```

có thể derive bằng ghép hai triangles thành parallelogram.

Parallelogram có cùng area với rectangle base-height tương ứng vì shear giữ base và perpendicular height.

Circle:

```math
A=\pi r^2.
```

Một intuition là chia thành nhiều sectors rồi sắp xen kẽ. Khi số sectors tăng, shape tiến gần rectangle có height `r` và width `\pi r`.

Đây là bridge tự nhiên từ geometry sang limit/integration.

## 12. Volume và Cavalieri intuition

Prism/cylinder có

```math
V=A_{base}h.
```

vì cross-sectional area không đổi theo height.

Cavalieri principle nói nếu hai solids có same cross-sectional area ở mọi height thì volumes bằng nhau.

Ý tưởng này chính là integral intuition:

```math
V=\int A(z)\,dz.
```

Geometry và calculus không phải hai thế giới tách biệt; calculus formalize accumulation của infinitesimal cross-sections.

## 13. Transformation và invariant

Translation, rotation và reflection bảo toàn Euclidean distances. Uniform scaling không bảo toàn length nhưng bảo toàn angle và ratios.

Do đó mỗi transformation class có một tập invariants riêng.

Ví dụ:

```text
rigid motion → distance, angle, area magnitude preserved
similarity transform → angle, shape ratios preserved
projective transform → straight lines preserved, metric quantities generally not
```

Trong computer vision, chọn đúng invariant giúp recognition robust hơn với camera transformation.

## 14. Coordinate system không phải geometry itself

Một point có thể có nhiều coordinate representations tùy origin và basis.

Nếu đổi coordinates đúng cách, geometric distance/angle của object không đổi.

Đây là một principle rất quan trọng:

> representation có thể đổi, object không nhất thiết đổi.

Nó quay lại trong linear algebra với change of basis, trong physics với reference frame và trong ML với representation learning.

## 15. Worked Example: indirect measurement bằng similarity

Một cột cao chưa biết `H` tạo shadow dài 12 m. Một người cao 1.8 m tạo shadow dài 1.5 m cùng thời điểm.

Nếu sun rays gần parallel, hai right triangles similar:

```math
\frac{H}{12}=\frac{1.8}{1.5}.
```

Do đó

```math
H=12\cdot\frac{1.8}{1.5}=14.4\text{ m}.
```

Điểm quan trọng không phải phép nhân cuối. Assumption chính là same sun angle và ground geometry đủ phẳng.

Nếu terrain nghiêng hoặc measurements không cùng thời điểm, model similarity bị phá.

## 16. Worked Example: geometry của optimization

Cho tất cả rectangles có perimeter fixed `P`.

Nếu sides `x,y`:

```math
2x+2y=P.
```

Area:

```math
A=xy.
```

Substitute

```math
y=\frac P2-x
```

cho

```math
A(x)=x\left(\frac P2-x\right).
```

Geometry tạo constraint; algebra biến thành one-variable function; calculus tìm maximum. Đây là ví dụ một problem đi qua nhiều layers toán học thay vì ở trong một chapter cô lập.

## 17. Connection với Physics

Euclidean geometry là nền cho kinematics local: displacement, velocity vectors, force decomposition và torque geometry.

Nhưng ở large-scale curved spacetime hoặc trên curved surfaces, Euclidean assumptions có thể fail. Điều này nhắc ta rằng model geometry là một phần của physics assumption.

## 18. Connection với Computer Science

Geometry xuất hiện trong:

- graphics transformations;
- collision detection;
- GIS/map projections;
- robotics localization;
- spatial databases;
- nearest-neighbor search;
- embeddings và metric learning.

Nhưng computing thường phải thêm numerical concerns: floating-point tolerance, discretization, coordinate conventions và performance trade-offs.

## Mental Model

> Euclidean geometry là study của structure trong một space phẳng: distance và angle tạo ra shape; transformations cho biết representation/object có thể thay đổi thế nào; invariants cho biết điều gì thực sự thuộc về geometric object chứ không phụ thuộc cách nhìn.

## Common Misconceptions

**“Hình học = công thức diện tích.”** Không. Formula chỉ là consequences của structure và measure.

**“Tổng góc triangle luôn 180°.”** Chỉ trong Euclidean geometry.

**“Coordinates là point.”** Coordinates là representation của point trong một frame.

**“Hai hình nhìn giống thì similar.”** Similarity là condition toán học về angles và common scale ratio.

**“Distance Euclidean luôn hợp lý.”** Không; metric phải phù hợp representation và domain.
