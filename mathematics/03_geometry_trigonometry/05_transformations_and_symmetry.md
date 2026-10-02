# Phép biến hình và đối xứng: transformations, invariants và symmetry

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phép biến hình và đối xứng: transformations, invariants và symmetry**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Transformation là một hàm (function / 함수) trên không gian (space / 공간)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Translation: move mà không đổi shape** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối transformations với symmetry, invariants và geometry, để biến đổi được đọc qua đại lượng không đổi.

Phép biến hình (geometric transformation / 기하변환) là một ánh xạ (mapping / 매핑) biến points thành points. Thay vì chỉ hỏi “shape này trông như thế nào?”, transformation viewpoint hỏi câu sâu hơn:

> Nếu ta move, rotate, reflect, quy mô (scale / 규모) hoặc thay đổi (change / 변경) coordinates, properties nào thay đổi và properties nào được bảo toàn?

Câu hỏi về **invariants** này là cầu nối (bridge / 브리지) trực tiếp từ hình học (geometry / 기하학) sang matrices, group lý thuyết (theory / 이론), physics, computer graphics và hiện đại (modern / 현대적) machine học tập (learning / 학습).

## 1. Transformation là một hàm (function / 함수) trên không gian (space / 공간)

Nếu không gian (space / 공간) là `S`, transformation có thể viết

```math
T:S\to S.
```

Mỗi điểm (point / 지점) `x` được map tới điểm (point / 지점) mới `T(x)`.

Một transformation có thể đại diện cho nhiều ý nghĩa:

- đối tượng (object / 객체) thực sự di chuyển trong một fixed frame;
- coordinate frame thay đổi còn đối tượng (object / 객체) đứng yên;
- dữ liệu (data / 데이터) được normalized/augmented;
- trạng thái (state / 상태) của hệ thống (system / 시스템) chuyển sang trạng thái (state / 상태) mới.

Do đó trước khi thao tác formula cần rõ interpretation của transformation.

> **Chuyển mạch:** Trong **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **2. Translation: move mà không đổi shape** tiếp nhận điểm tựa từ **1. Transformation là một hàm (function / 함수) trên không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Rotation: preserve inner-product hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Translation: move mà không đổi shape

Translation bởi véc-tơ (vector / 벡터) `t`:

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

Nhưng nó không phải tuyến tính (linear / 선형) transformation trên ordinary position vectors vì

```math
T(0)=t\ne0.
```

Nó là affine transformation.

> **Chuyển mạch:** Ở chặng này của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **3. Rotation: preserve inner-product hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **2. Translation: move mà không đổi shape** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Composition của rotations giải thích angle addition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Rotation: preserve inner-product hình học (geometry / 기하학)

Rotation quanh origin angle `\theta`:

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Với véc-tơ (vector / 벡터) `x`, rotated véc-tơ (vector / 벡터) là

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **4. Composition của rotations giải thích angle addition** tiếp nhận điểm tựa từ **3. Rotation: preserve inner-product hình học (geometry / 기하학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Reflection: preserve distance nhưng flip orientation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Composition của rotations giải thích angle addition

Nếu rotate `\alpha`, sau đó rotate `\beta`:

```math
R(\beta)R(\alpha)=R(\alpha+\beta).
```

Khai triển phép nhân ma trận (matrix multiplication / 행렬 곱셈) cho ra sine/cosine addition identities.

Vì thế identities như

```math
\cos(\alpha+\beta)
=
\cos\alpha\cos\beta-\sin\alpha\sin\beta
```

không phải công thức tách rời; chúng encode composition của rotations.

> **Chuyển mạch:** Trong **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **5. Reflection: preserve distance nhưng flip orientation** tiếp nhận điểm tựa từ **4. Composition của rotations giải thích angle addition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Scaling: uniform và non-uniform khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Reflection: preserve distance nhưng flip orientation

Reflection qua x-axis:

```math
(x,y)\mapsto(x,-y).
```

Ma trận (matrix / 행렬):

```math
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}.
```

Reflection preserve length/angle nhưng determinant bằng `-1`, biểu thị orientation bị đảo.

Rotation ma trận (matrix / 행렬) 2D có determinant `+1`.

Determinant vì vậy không chỉ đo volume scaling; sign còn encode orientation thay đổi (change / 변경).

> **Chuyển mạch:** Ở chặng này của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **6. Scaling: uniform và non-uniform khác nhau** tiếp nhận điểm tựa từ **5. Reflection: preserve distance nhưng flip orientation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Shear: shape thay đổi (change / 변경) mà area có thể giữ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Scaling: uniform và non-uniform khác nhau

Uniform scaling:

```math
x\mapsto kx.
```

Length quy mô (scale / 규모) `|k|`, area quy mô (scale / 규모) `k^2`, volume quy mô (scale / 규모) `|k|^3` trong 3D.

Nếu quy mô (scale / 규모) khác nhau theo axes:

```math
S=
\begin{bmatrix}
a&0\\
0&b
\end{bmatrix},
```

thì circle thường thành ellipse nếu `a\ne b`.

Non-uniform scaling không preserve angles nói chung. Do đó “quy mô (scale / 규모)” không phải một lớp (class / 클래스) invariance duy nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **7. Shear: shape thay đổi (change / 변경) mà area có thể giữ** tiếp nhận điểm tựa từ **6. Scaling: uniform và non-uniform khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Affine transformations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Shear: shape thay đổi (change / 변경) mà area có thể giữ

Shear ma trận (matrix / 행렬):

```math
H=
\begin{bmatrix}
1&k\\
0&1
\end{bmatrix}.
```

Nó nghiêng shape mà determinant vẫn bằng 1, nên area preserved dù angles không preserved.

Đây là example quan trọng: same determinant không nghĩa same hình học (geometry / 기하학). Determinant chỉ capture volume scaling, không capture mọi distortion.

> **Chuyển mạch:** Trong **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **8. Affine transformations** tiếp nhận điểm tựa từ **7. Shear: shape thay đổi (change / 변경) mà area có thể giữ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Homogeneous coordinates: biến affine composition thành phép nhân ma trận (matrix multiplication / 행렬 곱셈)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Affine transformations

Affine map có dạng

```math
T(x)=Ax+b.
```

`A` xử lý tuyến tính (linear / 선형) part; `b` translation.

Affine transformations preserve:

- lines;
- parallelism;
- ratios dọc cùng line;
- affine combinations.

Nhưng chúng không nhất thiết preserve lengths hay angles.

Computer graphics và computer vision dùng affine các mô hình (models / 모델들) rất nhiều vì chúng đủ flexible nhưng vẫn algebraically manageable.

> **Chuyển mạch:** Ở chặng này của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **9. Homogeneous coordinates: biến affine composition thành phép nhân ma trận (matrix multiplication / 행렬 곱셈)** tiếp nhận điểm tựa từ **8. Affine transformations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. thứ tự (order / 순서) matters vì composition thường không commutative** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Homogeneous coordinates: biến affine composition thành phép nhân ma trận (matrix multiplication / 행렬 곱셈)

Translation không represent được bằng ordinary `2×2` tuyến tính (linear / 선형) ma trận (matrix / 행렬) trên `(x,y)`. Ta augment coordinate:

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

Giờ translation, rotation, quy mô (scale / 규모), shear có thể compose bằng phép nhân ma trận (matrix multiplication / 행렬 곱셈).

Trong 3D, graphics thường dùng `4×4` homogeneous matrices.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **10. thứ tự (order / 순서) matters vì composition thường không commutative** tiếp nhận điểm tựa từ **9. Homogeneous coordinates: biến affine composition thành phép nhân ma trận (matrix multiplication / 행렬 곱셈)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Symmetry là transformation làm đối tượng (object / 객체) bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. thứ tự (order / 순서) matters vì composition thường không commutative

Nói chung

```math
T_2\circ T_1\ne T_1\circ T_2.
```

Ví dụ rotate đối tượng (object / 객체) quanh origin rồi translate khác với translate trước rồi rotate; ở trường hợp (case / 사례) thứ hai translation véc-tơ (vector / 벡터) cũng bị rotation tác động.

Đây là nguồn bug phổ biến trong graphics engines và robotics transforms.

### Worked intuition

Điểm (point / 지점) `(1,0)`:

1. rotate 90° → `(0,1)`;
2. translate `(1,0)` → `(1,1)`.

Nếu translate trước:

1. `(1,0)+(1,0)=(2,0)`;
2. rotate 90° → `(0,2)`.

Kết quả khác nhau.

> **Chuyển mạch:** Trong **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **11. Symmetry là transformation làm đối tượng (object / 객체) bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **10. thứ tự (order / 순서) matters vì composition thường không commutative** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Symmetries tạo group cấu trúc (structure / 구조)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Symmetry là transformation làm đối tượng (object / 객체) bất biến (invariant / 불변식)

Đối tượng (object / 객체) có symmetry nếu tồn tại transformation `T` sao cho

```math
T(X)=X
```

ở mức đối tượng (object / 객체)/set.

Circle bất biến (invariant / 불변식) dưới mọi rotation quanh center.

Square bất biến (invariant / 불변식) dưới rotations multiples 90° và một số reflections.

Symmetry không chỉ là aesthetic thuộc tính (property / 속성); nó nói đối tượng (object / 객체) có redundant descriptions dưới certain transformations.

> **Chuyển mạch:** Ở chặng này của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **12. Symmetries tạo group cấu trúc (structure / 구조)** tiếp nhận điểm tựa từ **11. Symmetry là transformation làm đối tượng (object / 객체) bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Invariance và equivariance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Symmetries tạo group cấu trúc (structure / 구조)

Các symmetries của một đối tượng (object / 객체) có thể compose. Chúng có:

- định danh (identity / 식별자) transformation;
- closure dưới composition;
- inverse;
- associativity.

Đó chính là group cấu trúc (structure / 구조).

Vì vậy group lý thuyết (theory / 이론) xuất hiện tự nhiên từ hình học (geometry / 기하학): nó formalize algebra của transformations giữ đối tượng (object / 객체) unchanged.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **13. Invariance và equivariance** tiếp nhận điểm tựa từ **12. Symmetries tạo group cấu trúc (structure / 구조)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Physics: symmetry và conservation laws** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Invariance và equivariance

Hai ideas này đặc biệt quan trọng trong ML.

Hàm (function / 함수) bất biến (invariant / 불변식) nếu

```math
f(Tx)=f(x).
```

Ví dụ ảnh (image / 이미지) classifier lý tưởng có thể muốn label không đổi dưới small translation.

Ánh xạ (mapping / 매핑) equivariant nếu

```math
f(Tx)=T'f(x).
```

Ví dụ segmentation mask nên shift cùng ảnh (image / 이미지) đầu vào (input / 입력).

Bất biến (invariant / 불변식) đầu ra (output / 출력) bỏ transformation tác động (effect / 효과); equivariant đầu ra (output / 출력) transform có cấu trúc cùng đầu vào (input / 입력).

> **Chuyển mạch:** Trong **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **14. Physics: symmetry và conservation laws** tiếp nhận điểm tựa từ **13. Invariance và equivariance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Computer Graphics: transformation chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Physics: symmetry và conservation laws

Trong physics, symmetry của laws liên hệ sâu với conserved quantities qua Noether's theorem.

Ví dụ:

- invariance theo thời gian (time / 시간) translation ↔ năng lượng (energy / 에너지) conservation;
- spatial translation ↔ momentum conservation;
- rotation symmetry ↔ angular momentum conservation.

Ý tưởng cốt lõi: nếu description vật lý không thay đổi dưới một continuous transformation, có cấu trúc (structure / 구조) được bảo toàn.

> **Chuyển mạch:** Ở chặng này của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **14. Physics: symmetry và conservation laws** xác định đầu vào; **15. Computer Graphics: transformation chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. Robotics: frames và rigid-body transforms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Computer Graphics: transformation chuỗi xử lý (pipeline / 파이프라인)

Một vertex thường đi qua:

```text
model
→ world
→ view
→ projection
→ screen
```

Mỗi stage là transformation có ngữ nghĩa (semantics / 의미론) riêng.

Một ma trận (matrix / 행렬) numerically correct vẫn có thể dùng sai nếu:

- multiplication thứ tự (order / 순서) sai;
- row-vector/column-vector convention bị mix;
- left-handed/right-handed hệ thống (system / 시스템) bị nhầm;
- object-space transform bị apply trong world không gian (space / 공간).

Hình học (geometry / 기하학) + ngữ nghĩa (semantics / 의미론) quan trọng hơn cú pháp (syntax / 문법) ma trận (matrix / 행렬).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **15. Computer Graphics: transformation chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **16. Robotics: frames và rigid-body transforms** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **17. AI: dữ liệu (data / 데이터) augmentation và symmetry các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Composition dùng ma trận (matrix / 행렬) products. Inverse cho phép chuyển đo lường (measurement / 측정) giữa sensor, robot và world frames.

Đây là practical ứng dụng (application / 애플리케이션) của affine transformations và group-like cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **16. Robotics: frames và rigid-body transforms** nêu điều cần giải thích; **17. AI: dữ liệu (data / 데이터) augmentation và symmetry các giả định (assumptions / 가정들)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. Finance: transformations của coordinate biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. AI: dữ liệu (data / 데이터) augmentation và symmetry các giả định (assumptions / 가정들)

Khi augment ảnh (image / 이미지) bằng crop/rotate/flip, ta đang encode belief rằng mục tiêu (target / 대상) hành vi (behavior / 동작) nên bất biến (invariant / 불변식)/equivariant dưới transformations đó.

Nếu giả định (assumption / 가정) sai, augmentation có thể harmful. Ví dụ flip chữ hoặc medical images có thể thay meaning.

Do đó symmetry trong ML không chỉ là trick; nó là prior về cấu trúc (structure / 구조) của tác vụ (task / 작업).

> **Chuyển mạch:** Ở chặng này của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **17. AI: dữ liệu (data / 데이터) augmentation và symmetry các giả định (assumptions / 가정들)** nêu điều cần giải thích; **18. Finance: transformations của coordinate biểu diễn (representation / 표현)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. Active vs passive transformation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Finance: transformations của coordinate biểu diễn (representation / 표현)

Portfolio returns có thể chuyển từ asset basis sang factor basis. rủi ro (risk / 위험) biểu diễn (representation / 표현) thay đổi nhưng underlying economic exposure có thể được giữ dưới invertible coordinate thay đổi (change / 변경).

PCA cũng tìm rotation-like orthogonal basis nơi covariance trở nên diagonal.

Đây là cùng principle: chọn transformation để làm cấu trúc (structure / 구조) dễ đọc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **19. Active vs passive transformation** tiếp nhận điểm tựa từ **18. Finance: transformations của coordinate biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Active vs passive transformation

Một subtle distinction:

**Active transformation:** đối tượng (object / 객체)/véc-tơ (vector / 벡터) được move trong fixed coordinates.

**Passive transformation:** đối tượng (object / 객체) không đổi, coordinate basis thay đổi.

Hai viewpoints có formulas closely related nhưng inverse/convention khác nhau.

Nhiều nhầm lẫn trong mechanics, graphics và tensor calculus đến từ không nói rõ viewpoint.

> **Chuyển mạch:** Trong **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **19. Active vs passive transformation** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Transformation là một hành động (action / 동작) lên không gian (space / 공간); symmetry là hành động (action / 동작) mà đối tượng (object / 객체) không thay đổi; invariants là properties transformation giữ lại. hình học (geometry / 기하학) trở nên sâu khi ta ngừng nhìn chỉ vào shapes và bắt đầu nhìn vào transformations giữa representations.

> **Chuyển mạch:** Ở chặng này của **Phép biến hình và đối xứng: transformations, invariants và symmetry**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**Mọi ma trận (matrix / 행렬) 2D là rotation.** Không; ma trận (matrix / 행렬) có thể quy mô (scale / 규모), shear, reflect hoặc collapse dimensions.

**Translation là tuyến tính (linear / 선형).** Không trong ordinary coordinates vì origin không được giữ; nó là affine.

**Transformation thứ tự (order / 순서) không quan trọng.** Sai trong general trường hợp (case / 사례); composition thường noncommutative.

**dữ liệu (data / 데이터) augmentation luôn tốt.** Chỉ khi chosen transformation thực sự preserve/equivariantly transform mục tiêu (target / 대상) ngữ nghĩa (semantics / 의미론).

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
