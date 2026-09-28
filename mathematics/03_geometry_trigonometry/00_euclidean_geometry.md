# Hình học Euclid: từ trực giác không gian đến cấu trúc bất biến

> **Mạch đọc:** Đọc **Hình học Euclid: từ trực giác không gian đến cấu trúc bất biến** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Từ vật thể thật đến đối tượng (object / 객체) lý tưởng** sang **2. Axiom: toán học không bắt đầu từ hư không**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Hình học Euclid (Euclidean geometry / 유클리드 기하학) là mô hình toán học của không gian “phẳng” mà ta gặp trong phần lớn bài toán hình học phổ thông, cơ học cổ điển, bản vẽ kỹ thuật và nhiều hệ tọa độ cục bộ trong computing. Điều quan trọng không phải chỉ là nhớ công thức diện tích hay góc, mà là hiểu **không gian (space / 공간) đang cho phép những quan hệ nào giữa điểm, đường, khoảng cách, góc và phép biến hình**.

Một chapter hình học tốt cần trả lời hai câu hỏi song song:

1. đối tượng (object / 객체) nào đang được mô tả?
2. thuộc tính (property / 속성) nào không đổi khi ta di chuyển hoặc biểu diễn đối tượng (object / 객체) theo cách khác?

Đây là cầu nối (bridge / 브리지) trực tiếp sang véc-tơ (vector / 벡터), ma trận (matrix / 행렬), symmetry, topology, graphics và physics.

## 1. Từ vật thể thật đến đối tượng (object / 객체) lý tưởng

Điểm (point / 점) là một vị trí không có kích thước. Đường thẳng (line / 직선) là đối tượng (object / 객체) một chiều kéo dài vô hạn hai phía. Mặt phẳng (plane / 평면) là đối tượng (object / 객체) hai chiều vô hạn.

Trong thực tế, nét bút có thickness và mặt bàn không hoàn toàn phẳng. hình học (geometry / 기하학) bỏ các chi tiết vật lý đó để giữ lại cấu trúc (structure / 구조) của vị trí và quan hệ.

Đây là ví dụ đầu tiên về mathematical modeling:

```text
real object
→ ignore irrelevant physical detail
→ keep geometric relation
→ reason in ideal model
```

Khi dùng kết quả hình học cho đời thực, ta luôn phải nhớ bước quay lại mô hình (model / 모델): nếu đối tượng (object / 객체) vật lý cong, biến dạng hoặc đo lường (measurement / 측정) có noise, Euclidean kết quả (result / 결과) chỉ là approximation.

## 2. Axiom: toán học không bắt đầu từ hư không

Một hệ hình học cần axioms/postulates — các quy tắc nền được chấp nhận làm starting điểm (point / 지점).

Một postulate đặc trưng của Euclidean hình học (geometry / 기하학) là parallel postulate: qua một điểm (point / 지점) ngoài một line, có đúng một line song song với line đó.

Điều này nghe hiển nhiên vì trực giác của ta được xây từ không gian gần phẳng. Nhưng nếu đổi mô hình (model / 모델) không gian (space / 공간), statement không còn đúng.

Trên sphere, “đường thẳng tự nhiên” được thay bằng geodesic như great circle. Hai great circles thường giao nhau. Vì vậy theorem hình học phải luôn được hiểu cùng các giả định (assumptions / 가정들) về không gian (space / 공간).

## 3. Distance là cấu trúc (structure / 구조), không chỉ là formula

Khoảng cách (distance / 거리) là một hàm (function / 함수) đo separation giữa points.

Trong Euclidean plane, nếu hai points có difference véc-tơ (vector / 벡터)

```math
(\Delta x,\Delta y),
```

thì Pythagoras cho

```math
d=\sqrt{(\Delta x)^2+(\Delta y)^2}.
```

Formula này không phải definition phổ quát của “distance”. Nó là distance do Euclidean inner-product cấu trúc (structure / 구조) tạo ra.

Một chỉ số (metric / 지표) nói chung cần các tính chất như:

```text
non-negativity
identity of indiscernibles
symmetry
triangle inequality
```

Do đó Manhattan distance, đồ thị (graph / 그래프) shortest-path distance hay cosine distance-like measures có thể phù hợp hơn trong lĩnh vực (domain / 도메인) khác.

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

Radian là natural đơn vị (unit / 단위) vì nó không cần conversion constant khi làm calculus. Các limits nền như

```math
\lim_{x\to0}\frac{\sin x}{x}=1
```

chỉ có form sạch như vậy khi `x` đo bằng radian.

## 5. Congruence: cùng shape và cùng kích thước (size / 크기)

Hai figures congruent (합동 / congruent) nếu có thể đưa trùng nhau bằng rigid transformations: translation, rotation hoặc reflection.

Rigid transformation bảo toàn distance. Vì distance được bảo toàn, angle cũng được bảo toàn.

Đây là một idea sâu: thay vì so từng cạnh/góc riêng lẻ, ta có thể hỏi liệu có một transformation bảo toàn cấu trúc (structure / 구조) đưa đối tượng (object / 객체) A thành đối tượng (object / 객체) B hay không.

Trong hiện đại (modern / 현대적) mathematics, classification thông qua allowed transformations là một chiến lược (strategy / 전략) rất phổ biến.

## 6. Similarity: cùng shape, khác quy mô (scale / 규모)

Hai figures similar (닮음 / similarity) khi angles tương ứng bằng nhau và lengths tương ứng theo cùng một quy mô (scale / 규모) factor.

Nếu quy mô (scale / 규모) factor là `k`, thì

```math
L' = kL,
```

area quy mô (scale / 규모):

```math
A'=k^2A,
```

và volume quy mô (scale / 규모):

```math
V'=k^3V.
```

Điều này không phải ba quy tắc (rule / 규칙) riêng. Nó đến từ số dimensions độc lập đóng góp factor `k`.

Similarity nối hình học (geometry / 기하학) với dimensional phân tích (analysis / 분석), ảnh (image / 이미지) resizing, map quy mô (scale / 규모) và square-cube law trong biology/kỹ thuật (engineering / 엔지니어링).

## 7. Triangle là thành phần nguyên thủy (primitive / 기본 요소) cấu trúc (structure / 구조) của Euclidean hình học (geometry / 기하학)

Triangle đặc biệt vì ba non-collinear points xác định một shape tối giản trong plane.

Các theorem về congruence như SSS, SAS, ASA không chỉ là exam rules; chúng nói lượng thông tin (information / 정보) tối thiểu nào đủ để xác định triangle duy nhất đến rigid motion.

Ví dụ, biết ba cạnh `a,b,c` thỏa triangle inequality:

```math
a+b>c,
```

và cyclic variants, thì triangle được xác định đến congruence.

Triangle inequality phản ánh ý tưởng: đường đi trực tiếp giữa hai points không dài hơn đường vòng qua điểm (point / 지점) thứ ba.

## 8. Tổng góc tam giác và giả định (assumption / 가정) Euclidean

Trong Euclidean plane:

```math
\alpha+\beta+\gamma=\pi.
```

Một proof idea là kẻ line qua một vertex song song với cạnh đối diện rồi dùng alternate interior angles.

Proof này dùng parallel postulate. Vì vậy theorem không hoàn toàn “tự nhiên” ngoài ngữ cảnh (context / 맥락) Euclidean.

Trên sphere, triangle angle sum có thể lớn hơn `π`; trong hyperbolic hình học (geometry / 기하학) có thể nhỏ hơn `π`.

Đây là lesson quan trọng về theorem các giả định (assumptions / 가정들): proof cho ta biết theorem đang dựa vào cấu trúc (structure / 구조) nào.

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

Vì vậy Pythagoras không dừng ở hình học (geometry / 기하학) school; nó đi thẳng sang vectors, least squares, variance decomposition và Hilbert-space intuition.

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

Trong physics và kỹ thuật (engineering / 엔지니어링), symmetry thường giúp giảm số variables cần xét.

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

Parallelogram có cùng area với rectangle base-height tương ứng vì shear giữ cơ sở (base / 기반) và perpendicular height.

Circle:

```math
A=\pi r^2.
```

Một intuition là chia thành nhiều sectors rồi sắp xen kẽ. Khi số sectors tăng, shape tiến gần rectangle có height `r` và width `\pi r`.

Đây là cầu nối (bridge / 브리지) tự nhiên từ hình học (geometry / 기하학) sang limit/tích hợp (integration / 통합).

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

Hình học (geometry / 기하학) và calculus không phải hai thế giới tách biệt; calculus formalize accumulation của infinitesimal cross-sections.

## 13. Transformation và bất biến (invariant / 불변식)

Translation, rotation và reflection bảo toàn Euclidean distances. Uniform scaling không bảo toàn length nhưng bảo toàn angle và ratios.

Do đó mỗi transformation lớp (class / 클래스) có một tập invariants riêng.

Ví dụ:

```text
rigid motion → distance, angle, area magnitude preserved
similarity transform → angle, shape ratios preserved
projective transform → straight lines preserved, metric quantities generally not
```

Trong computer vision, chọn đúng bất biến (invariant / 불변식) giúp recognition robust hơn với camera transformation.

## 14. Coordinate hệ thống (system / 시스템) không phải hình học (geometry / 기하학) itself

Một điểm (point / 지점) có thể có nhiều coordinate representations tùy origin và basis.

Nếu đổi coordinates đúng cách, geometric distance/angle của đối tượng (object / 객체) không đổi.

Đây là một principle rất quan trọng:

> biểu diễn (representation / 표현) có thể đổi, đối tượng (object / 객체) không nhất thiết đổi.

Nó quay lại trong tuyến tính (linear / 선형) algebra với thay đổi (change / 변경) of basis, trong physics với tham chiếu (reference / 참조) frame và trong ML với biểu diễn (representation / 표현) học tập (learning / 학습).

## 15. Worked Example: indirect đo lường (measurement / 측정) bằng similarity

Một cột cao chưa biết `H` tạo shadow dài 12 m. Một người cao 1.8 m tạo shadow dài 1.5 m cùng thời điểm.

Nếu sun rays gần parallel, hai right triangles similar:

```math
\frac{H}{12}=\frac{1.8}{1.5}.
```

Do đó

```math
H=12\cdot\frac{1.8}{1.5}=14.4\text{ m}.
```

Điểm quan trọng không phải phép nhân cuối. giả định (assumption / 가정) chính là same sun angle và ground hình học (geometry / 기하학) đủ phẳng.

Nếu terrain nghiêng hoặc measurements không cùng thời điểm, mô hình (model / 모델) similarity bị phá.

## 16. Worked Example: hình học (geometry / 기하학) của tối ưu hóa (optimization / 최적화)

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

Hình học (geometry / 기하학) tạo ràng buộc (constraint / 제약조건); algebra biến thành one-variable hàm (function / 함수); calculus tìm maximum. Đây là ví dụ một bài toán (problem / 문제) đi qua nhiều layers toán học thay vì ở trong một chapter cô lập.

## 17. liên kết (connection / 연결) với Physics

Euclidean hình học (geometry / 기하학) là nền cho kinematics cục bộ (local / 로컬): displacement, velocity vectors, force decomposition và torque hình học (geometry / 기하학).

Nhưng ở large-scale curved spacetime hoặc trên curved surfaces, Euclidean các giả định (assumptions / 가정들) có thể thất bại (fail / 실패). Điều này nhắc ta rằng mô hình (model / 모델) hình học (geometry / 기하학) là một phần của physics giả định (assumption / 가정).

## 18. liên kết (connection / 연결) với Khoa học máy tính (computer science / 컴퓨터 과학)

Hình học (geometry / 기하학) xuất hiện trong:

- graphics transformations;
- collision detection;
- GIS/map projections;
- robotics localization;
- spatial databases;
- nearest-neighbor tìm kiếm (search / 검색);
- embeddings và chỉ số (metric / 지표) học tập (learning / 학습).

Nhưng computing thường phải thêm numerical concerns: floating-point tolerance, discretization, coordinate conventions và hiệu năng (performance / 성능) trade-offs.

## Mô hình tư duy (mental model / 사고 모델)

> Euclidean hình học (geometry / 기하학) là study của cấu trúc (structure / 구조) trong một không gian (space / 공간) phẳng: distance và angle tạo ra shape; transformations cho biết biểu diễn (representation / 표현)/đối tượng (object / 객체) có thể thay đổi thế nào; invariants cho biết điều gì thực sự thuộc về geometric đối tượng (object / 객체) chứ không phụ thuộc cách nhìn.

## Dùng chung (common / 공통) Misconceptions

**“Hình học = công thức diện tích.”** Không. Formula chỉ là consequences của cấu trúc (structure / 구조) và measure.

**“Tổng góc triangle luôn 180°.”** Chỉ trong Euclidean hình học (geometry / 기하학).

**“Coordinates là điểm (point / 지점).”** Coordinates là biểu diễn (representation / 표현) của điểm (point / 지점) trong một frame.

**“Hai hình nhìn giống thì similar.”** Similarity là điều kiện (condition / 조건) toán học về angles và dùng chung (common / 공통) quy mô (scale / 규모) ratio.

**“Distance Euclidean luôn hợp lý.”** Không; chỉ số (metric / 지표) phải phù hợp biểu diễn (representation / 표현) và lĩnh vực (domain / 도메인).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 coordinate geometry](./01_coordinate_geometry.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
