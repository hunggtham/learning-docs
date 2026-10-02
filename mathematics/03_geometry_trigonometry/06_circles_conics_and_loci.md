# Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Circle: giữ một distance không đổi** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. mức (level / 수준) set và normal véc-tơ (vector / 벡터)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối circles, conics và loci với focus, distance và equation, để đường cong được dựng từ điều kiện hình học.

Quỹ tích (locus / 자취) là tập hợp mọi điểm thỏa một điều kiện. Cách nhìn này mạnh hơn việc học riêng từng phương trình circle, parabola, ellipse hay hyperbola, vì nó trả lời câu hỏi bản chất: **đường cong này tồn tại vì ràng buộc (constraint / 제약조건) nào?**

Một conic có thể được nhìn đồng thời theo ba lớp:

```text
geometric constraint
→ algebraic equation
→ transformed coordinate representation
```

Khi ba lớp này được nối với nhau, tiêu chuẩn (standard / 표준) forms không còn là công thức phải ghi nhớ.

## 1. Circle: giữ một distance không đổi

Cho tâm

```math
C=(h,k)
```

và bán kính `r`. Điểm `P=(x,y)` thuộc circle khi

```math
CP=r.
```

Dùng distance formula:

```math
\sqrt{(x-h)^2+(y-k)^2}=r,
```

nên

```math
(x-h)^2+(y-k)^2=r^2.
```

Đây là phương trình đường tròn (circle / 원) vì nó chỉ encode một distance ràng buộc (constraint / 제약조건).

### Worked example

Circle tâm `(2,-1)`, radius `3`:

```math
(x-2)^2+(y+1)^2=9.
```

Điểm `(5,-1)` nằm trên circle vì distance tới center bằng 3.

> **Chuyển mạch:** Trong **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **2. mức (level / 수준) set và normal véc-tơ (vector / 벡터)** tiếp nhận điểm tựa từ **1. Circle: giữ một distance không đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Parabola: cân bằng distance tới điểm (point / 지점) và line** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. mức (level / 수준) set và normal véc-tơ (vector / 벡터)

Viết

```math
F(x,y)=(x-h)^2+(y-k)^2-r^2.
```

Circle là mức (level / 수준) set

```math
F(x,y)=0.
```

Độ dốc (gradient / 기울기):

```math
\nabla F=(2(x-h),2(y-k)).
```

Độ dốc (gradient / 기울기) hướng theo radius. Vì độ dốc (gradient / 기울기) vuông góc với mức (level / 수준) curve, tangent tại một điểm trên circle vuông góc với radius.

Đây là cầu nối (bridge / 브리지) trực tiếp tới multivariable calculus: hình học (geometry / 기하학) của tangent/normal xuất hiện từ độ dốc (gradient / 기울기) của ràng buộc (constraint / 제약조건).

> **Chuyển mạch:** Ở chặng này của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **3. Parabola: cân bằng distance tới điểm (point / 지점) và line** tiếp nhận điểm tựa từ **2. mức (level / 수준) set và normal véc-tơ (vector / 벡터)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Ellipse: tổng hai distance không đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Parabola: cân bằng distance tới điểm (point / 지점) và line

Parabola (포물선) là locus của các điểm có distance tới focus bằng distance tới directrix.

Cho focus `(0,p)` và directrix `y=-p`. Với `P=(x,y)`:

```math
\sqrt{x^2+(y-p)^2}=|y+p|.
```

Bình phương:

```math
x^2+(y-p)^2=(y+p)^2.
```

Simplify:

```math
x^2=4py.
```

Như vậy tiêu chuẩn (standard / 표준) form đến từ distance definition, không phải từ việc “nhớ dạng parabola”.

### Reflective thuộc tính (property / 속성)

Trong ideal hình học (geometry / 기하학), ray song song với axis của parabola phản xạ qua tangent và đi qua focus. Đây là lý do parabolic reflector xuất hiện trong antenna, telescope và satellite dish.

Điểm quan trọng là ứng dụng (application / 애플리케이션) này phụ thuộc thêm vật lý (physical / 물리적) law về reflection; geometric shape cung cấp cấu trúc (structure / 구조), physics cung cấp cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **4. Ellipse: tổng hai distance không đổi** tiếp nhận điểm tựa từ **3. Parabola: cân bằng distance tới điểm (point / 지점) và line** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Hyperbola: hiệu hai distance không đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Ellipse: tổng hai distance không đổi

Ellipse (타원) là locus của các điểm `P` sao cho

```math
PF_1+PF_2=2a.
```

Trong principal coordinates:

```math
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,
\qquad a\ge b>0.
```

Focal distance:

```math
c^2=a^2-b^2.
```

Eccentricity:

```math
e=\frac ca,
```

với

```text
circle: e=0
ellipse: 0<e<1
```

Eccentricity đo degree mà conic lệch khỏi circle-like hình học (geometry / 기하학).

### Kepler liên kết (connection / 연결)

Trong ideal two-body mô hình (model / 모델), planetary orbit là ellipse với central body ở một focus. Nhưng đây là consequence của inverse-square dynamics, không phải chỉ vì “ellipse trông giống orbit”. hình học (geometry / 기하학) và vật lý (physical / 물리적) dynamics cần được phân biệt.

> **Chuyển mạch:** Trong **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **5. Hyperbola: hiệu hai distance không đổi** tiếp nhận điểm tựa từ **4. Ellipse: tổng hai distance không đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Một definition thống nhất bằng eccentricity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Hyperbola: hiệu hai distance không đổi

Hyperbola (쌍곡선) thỏa

```math
|PF_1-PF_2|=2a.
```

Tiêu chuẩn (standard / 표준) form:

```math
\frac{x^2}{a^2}-\frac{y^2}{b^2}=1.
```

Asymptotes:

```math
y=\pm\frac ba x.
```

Asymptote không phải một phần của hyperbola. Nó mô tả direction mà curve tiến gần khi `|x|` lớn.

### Localization example

Nếu hai sensors đo chênh lệch thời gian đến của một tín hiệu (signal / 신호), chênh lệch distance tới hai sensors gần như cố định. Locus khả dĩ là hyperbola. Nhiều sensor pairs cho nhiều hyperbolas; intersection cho estimate nguồn (source / 소스) position.

Đây là ví dụ đẹp về hình học (geometry / 기하학) → inverse bài toán (problem / 문제).

> **Chuyển mạch:** Ở chặng này của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **6. Một definition thống nhất bằng eccentricity** tiếp nhận điểm tựa từ **5. Hyperbola: hiệu hai distance không đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. General quadratic equation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Một definition thống nhất bằng eccentricity

Một cách unified hơn dùng focus `F`, directrix `L` và eccentricity `e`:

```math
\frac{\text{distance}(P,F)}{\text{distance}(P,L)}=e.
```

Từ đó:

```text
e < 1 → ellipse
 e = 1 → parabola
 e > 1 → hyperbola
```

Circle có thể xem như limiting/special symmetric trường hợp (case / 사례).

Cách này cho thấy các conics không phải bốn families hoàn toàn tách rời; chúng là các regimes của cùng một distance-ratio idea.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **7. General quadratic equation** tiếp nhận điểm tựa từ **6. Một definition thống nhất bằng eccentricity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Vì sao rotation loại được cross term xy?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. General quadratic equation

General conic equation:

```math
Ax^2+Bxy+Cy^2+Dx+Ey+F=0.
```

Quadratic part được encode bởi symmetric ma trận (matrix / 행렬)

```math
Q=
\begin{bmatrix}
A & B/2\\
B/2 & C
\end{bmatrix}.
```

Viết compact:

```math
x^TQx+d^Tx+F=0.
```

Đây là cầu nối (bridge / 브리지) trực tiếp từ analytic hình học (geometry / 기하학) sang quadratic forms trong tuyến tính (linear / 선형) algebra.

> **Chuyển mạch:** Trong **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **8. Vì sao rotation loại được cross term xy?** tiếp nhận điểm tựa từ **7. General quadratic equation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Classification bằng B^2-4AC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Vì sao rotation loại được cross term `xy`?

Symmetric ma trận (matrix / 행렬) `Q` có orthogonal eigenbasis. Nếu đổi coordinates sang eigenvectors của `Q`, ma trận (matrix / 행렬) trở thành diagonal:

```math
Q=P\Lambda P^T.
```

Trong rotated coordinates, quadratic part không còn mixed term `xy`.

Vì vậy “rotate axes to simplify conic” thực chất là **diagonalize a symmetric quadratic form**.

Đây là cùng cấu trúc (structure / 구조) xuất hiện trong PCA, covariance ellipses và Hessian phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **9. Classification bằng B^2-4AC** tiếp nhận điểm tựa từ **8. Vì sao rotation loại được cross term xy?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Parametric, implicit và ma trận (matrix / 행렬) representations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Classification bằng `B^2-4AC`

Under non-degenerate real conditions:

```text
B² - 4AC < 0 → ellipse-type
B² - 4AC = 0 → parabola-type
B² - 4AC > 0 → hyperbola-type
```

Nhưng đây không phải complete classification nếu không xét tuyến tính (linear / 선형)/constant terms và degeneracy. Equation có thể collapse thành pair of lines, a điểm (point / 지점) hoặc empty set.

Quy tắc (rule / 규칙) chỉ có meaning khi các giả định (assumptions / 가정들) được nói rõ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **10. Parametric, implicit và ma trận (matrix / 행렬) representations** tiếp nhận điểm tựa từ **9. Classification bằng B^2-4AC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Conics và tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Parametric, implicit và ma trận (matrix / 행렬) representations

Một circle có implicit form:

```math
x^2+y^2=r^2.
```

Parametric form:

```math
x=r\cos t,
\qquad
y=r\sin t.
```

Implicit biểu diễn (representation / 표현) tốt cho các ràng buộc (constraints / 제약조건들), inside/outside tests và level-set lập luận (reasoning / 추론). Parametric biểu diễn (representation / 표현) tốt cho rendering, animation và đường dẫn (path / 경로) traversal.

Biểu diễn (representation / 표현) choice là một kỹ thuật (engineering / 엔지니어링) quyết định (decision / 결정), không chỉ notation preference.

> **Chuyển mạch:** Trong **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **11. Conics và tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **10. Parametric, implicit và ma trận (matrix / 행렬) representations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Conics và second-order cục bộ (local / 로컬) các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Conics và tối ưu hóa (optimization / 최적화)

Ellipse

```math
x^TQx\le1
```

với positive-definite `Q` mô tả an ellipsoidal feasible set.

Trong statistics, covariance ma trận (matrix / 행렬) tạo confidence ellipses. Trong tối ưu hóa (optimization / 최적화), quadratic các ràng buộc (constraints / 제약조건들)/objectives tạo ellipsoidal hình học (geometry / 기하학). Trong machine học tập (learning / 학습), Mahalanobis distance cũng tạo mức (level / 수준) sets dạng ellipse/ellipsoid.

> **Chuyển mạch:** Ở chặng này của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **12. Conics và second-order cục bộ (local / 로컬) các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **11. Conics và tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Worked example: classify và rotate intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Conics và second-order cục bộ (local / 로컬) các mô hình (models / 모델들)

Taylor approximation bậc hai gần trọng yếu (critical / 중요) điểm (point / 지점):

```math
f(x+\Delta)
\approx
f(x)+\frac12\Delta^TH\Delta.
```

Mức (level / 수준) sets của quadratic form `\Delta^TH\Delta` thường là ellipses/hyperbolas tùy eigenvalue signs.

Do đó conic hình học (geometry / 기하학) không chỉ là school hình học (geometry / 기하학); nó là cục bộ (local / 로컬) hình học (geometry / 기하학) của multivariable functions.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **12. Conics và second-order cục bộ (local / 로컬) các mô hình (models / 모델들)** cho ta quy tắc; **Worked example: classify và rotate intuition** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Worked example: classify và rotate intuition

Xét

```math
5x^2+4xy+2y^2=1.
```

Quadratic ma trận (matrix / 행렬):

```math
Q=
\begin{bmatrix}
5&2\\
2&2
\end{bmatrix}.
```

`Q` symmetric và positive definite, nên mức (level / 수준) set là ellipse. Cross term chỉ nói axes của ellipse không aligned với original coordinate axes. Eigenvectors của `Q` cho principal axes.

> **Chuyển mạch:** Trong **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **Worked example: classify và rotate intuition** cho ta quy tắc; **Liên kết kiến thức (knowledge connection / 지식 연결)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Conics nối nhiều chapter:

```text
Pythagorean distance
→ locus
→ quadratic equation
→ quadratic form
→ eigenvectors / axis rotation
→ Hessian geometry
→ covariance ellipse
→ optimization constraints
```

Trong Physics, conics xuất hiện trong orbital mechanics và optics. Trong AI/dữ liệu (data / 데이터), ellipsoids xuất hiện trong covariance hình học (geometry / 기하학) và Gaussian contours. Trong Finance, quadratic rủi ro (risk / 위험) các mô hình (models / 모델들) có mức (level / 수준) sets dạng ellipsoid khi covariance ma trận (matrix / 행렬) positive definite.

> **Chuyển mạch:** Ở chặng này của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Conic sections là hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들) và quadratic forms. tiêu chuẩn (standard / 표준) equation chỉ là biểu diễn (representation / 표현) thuận tiện sau khi chọn coordinate hệ thống (system / 시스템) phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đường tròn, conic sections và quỹ tích: hình học (geometry / 기하학) của distance các ràng buộc (constraints / 제약조건들)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

Ellipse không chỉ là “circle bị kéo” về definition, dù affine transform của circle tạo ellipse. Projectile đường dẫn (path / 경로) chỉ là parabola dưới các giả định (assumptions / 가정들) như constant gravity và negligible air resistance. `B²-4AC` không đủ để classify mọi degenerate trường hợp (case / 사례). Hyperbola `xy=1` vẫn là conic dù không ở tiêu chuẩn (standard / 표준) axis-aligned form; đổi coordinates có thể làm cấu trúc (structure / 구조) rõ hơn.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
