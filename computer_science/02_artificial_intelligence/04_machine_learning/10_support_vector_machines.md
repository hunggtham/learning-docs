# Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel

> **Mạch đọc:** Đặt **hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Từ separating hyperplane tới margin** sang **Tại sao margin có ý nghĩa?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machine (SVM / 서포트 벡터 머신) xây classifier từ một geometric principle: không chỉ tìm hyperplane phân tách classes, mà tìm hyperplane có **margin** lớn. Margin là khoảng cách an toàn giữa quyết định (decision / 결정) ranh giới (boundary / 경계) và những huấn luyện (training / 학습) points gần ranh giới (boundary / 경계) nhất.

SVM quan trọng không chỉ vì bản thân thuật toán (algorithm / 알고리즘); nó giúp hiểu regularization, convex tối ưu hóa (optimization / 최적화), duality, kernels và biểu diễn (representation / 표현) hình học (geometry / 기하학).

## Từ separating hyperplane tới margin

Nhị phân (binary / 이진) classifier:

\[
f(x)=\mathbf w^T\mathbf x+b
\]

Quyết định (decision / 결정) ranh giới (boundary / 경계):

\[
\mathbf w^T\mathbf x+b=0
\]

Với labels `y∈{-1,+1}`, nếu dữ liệu (data / 데이터) linearly separable ta muốn:

\[
y_i(\mathbf w^T\mathbf x_i+b)\ge1
\]

Geometric margin tỉ lệ nghịch với norm của weight:

\[
margin=\frac{2}{\|\mathbf w\|}
\]

Maximize margin tương đương minimize:

\[
\frac12\|\mathbf w\|^2
\]

subject to classification các ràng buộc (constraints / 제약조건들).

## Tại sao margin có ý nghĩa?

Nếu có nhiều boundaries đều classify huấn luyện (training / 학습) set hoàn hảo, ranh giới (boundary / 경계) đi sát dữ liệu (data / 데이터) points dễ thay đổi prediction khi đầu vào (input / 입력) perturb nhẹ. Large margin chọn solution có buffer lớn hơn.

Đây là một inductive độ lệch (bias / 편향) về robustness/generalization.

## Hỗ trợ (support / 지원) Vectors

Chỉ những points nằm trên hoặc trong margin quyết định optimum mạnh nhất. Chúng gọi là **hỗ trợ (support / 지원) vectors (서포트 벡터)**.

Points rất xa ranh giới (boundary / 경계) thường không ảnh hưởng solution nếu các ràng buộc (constraints / 제약조건들) đã satisfied.

Đây là reason SVM có tên như vậy: ranh giới (boundary / 경계) được “đỡ” bởi trọng yếu (critical / 중요) examples.

## Soft Margin

Real dữ liệu (data / 데이터) thường không perfectly separable. Introduce slack variables `ξ_i`:

\[
y_i(\mathbf w^T\mathbf x_i+b)\ge1-\xi_i,\qquad \xi_i\ge0
\]

Mục tiêu (objective / 목표):

\[
\min_{w,b,\xi}\frac12\|w\|^2+C\sum_i\xi_i
\]

`C` điều khiển (control / 제어) sự đánh đổi (trade-off / 트레이드오프):

- large `C`: phạt huấn luyện (training / 학습) violations mạnh, fit dữ liệu (data / 데이터) hơn;
- small `C`: chấp nhận violations để giữ margin rộng hơn.

Đây là regularization sự đánh đổi (trade-off / 트레이드오프) dưới một form khác.

## Hinge mất mát (loss / 손실)

Soft-margin SVM có thể viết gần với regularized empirical rủi ro (risk / 위험):

\[
J(w)=\frac12\|w\|^2+C\sum_i\max(0,1-y_if(x_i))
\]

Hinge mất mát (loss / 손실) bằng zero khi example không chỉ đúng mà còn nằm ngoài margin.

## Tính năng (feature / 기능) Scaling

SVM phụ thuộc dot products/distances, nên tính năng (feature / 기능) quy mô (scale / 규모) rất quan trọng. Một tính năng (feature / 기능) magnitude lớn có thể dominate hình học (geometry / 기하학).

Standardization thường là preprocessing mặc định cho SVM.

## Kernel Trick

Nếu classes không linearly separable trong original không gian (space / 공간), ta có thể map đầu vào (input / 입력) qua nonlinear tính năng (feature / 기능) map:

\[
\phi(x)
\]

rồi học tuyến tính (linear / 선형) separator trong transformed không gian (space / 공간).

Dual form của SVM phụ thuộc vào inner products:

\[
\phi(x_i)^T\phi(x_j)
\]

Nếu có kernel hàm (function / 함수):

\[
K(x_i,x_j)=\phi(x_i)^T\phi(x_j)
\]

thì không cần compute `φ(x)` explicitly. Đây là **kernel trick**.

RBF kernel:

\[
K(x,z)=\exp(-\gamma\|x-z\|^2)
\]

cho nonlinear boundaries rất linh hoạt.

## Kernel không phải magic similarity bất kỳ

Kernel hợp lệ cần thỏa properties để tương ứng inner sản phẩm (product / 제품) trong một tính năng (feature / 기능) không gian (space / 공간), thường liên quan positive semidefinite Gram ma trận (matrix / 행렬).

Không phải mọi similarity hàm (function / 함수) tùy ý đều có thể dùng như kernel mà vẫn giữ lý thuyết (theory / 이론)/tối ưu hóa (optimization / 최적화) properties.

## C và gamma

Với RBF SVM:

- `C` điều khiển penalty cho classification errors/margin violations;
- `γ` điều khiển mức cục bộ (local / 로컬) của kernel.

`γ` quá lớn làm mỗi điểm (point / 지점) influence vùng rất nhỏ → ranh giới (boundary / 경계) phức tạp/high variance.

`γ` quá nhỏ làm influence quá rộng → mô hình (model / 모델) quá smooth/high độ lệch (bias / 편향).

Hyperparameter tìm kiếm (search / 검색) cần nested/correct kiểm tra hợp lệ (validation / 검증) để tránh optimistic độ lệch (bias / 편향).

## Computational scaling

Kernel SVM cần pairwise relationships giữa huấn luyện (training / 학습) points; bộ nhớ (memory / 메모리)/thời gian (time / 시간) có thể tăng rất mạnh với `n`.

Vì vậy kernel SVM phù hợp hơn small/medium datasets. Large-scale problems thường dùng tuyến tính (linear / 선형) SVM, approximate kernels hoặc các mô hình (models / 모델들) khác.

## SVM vs Logistic Regression

Cả hai có tuyến tính (linear / 선형) quyết định (decision / 결정) ranh giới (boundary / 경계) nếu dùng raw tuyến tính (linear / 선형) features.

Logistic Regression optimize probabilistic log-loss và đầu ra (output / 출력) xác suất (probability / 확률) mô hình (model / 모델) trực tiếp.

SVM optimize margin/hinge mục tiêu (objective / 목표); raw quyết định (decision / 결정) score không phải calibrated xác suất (probability / 확률).

Nếu cần xác suất (probability / 확률), có thể calibrate SVM bằng Platt scaling hoặc isotonic regression trên held-out dữ liệu (data / 데이터).

## Kernels và Neural biểu diễn (representation / 표현) học tập (learning / 학습)

Kernel methods encode nonlinear similarity thông qua fixed/designed kernel. Deep học tập (learning / 학습) học biểu diễn (representation / 표현) `φ_θ(x)` từ dữ liệu (data / 데이터).

Có thể nhìn một neural mạng (network / 네트워크) như học tính năng (feature / 기능) không gian (space / 공간) rồi dùng simple đầu ra (output / 출력) head. Difference lớn là tính năng (feature / 기능) map trong deep học tập (learning / 학습) được learned jointly, thay vì kernel fixed trước.

## Mô hình tư duy (mental model / 사고 모델)

> SVM hỏi: ranh giới (boundary / 경계) nào không chỉ đúng trên dữ liệu huấn luyện (training data / 학습 데이터) mà còn giữ khoảng cách an toàn lớn nhất với trọng yếu (critical / 중요) examples?

Kernel mở rộng câu hỏi này sang một tính năng (feature / 기능) không gian (space / 공간) nonlinear mà ta có thể không cần biểu diễn trực tiếp.

## Dùng chung (common / 공통) Misconceptions

### “hỗ trợ (support / 지원) vectors là mọi points gần ranh giới (boundary / 경계)”

Theo tối ưu hóa (optimization / 최적화), hỗ trợ (support / 지원) vectors là points có nonzero dual coefficients; chúng là points active trong solution.

### “SVM luôn tốt cho high-dimensional dữ liệu (data / 데이터)”

Tuyến tính (linear / 선형) SVM có thể rất mạnh với sparse high-dimensional dữ liệu (data / 데이터) như văn bản (text / 텍스트), nhưng kernel SVM có scaling issue theo cỡ mẫu (sample size / 표본 크기).

### “Kernel trick giống neural mạng (network / 네트워크) hidden tầng (layer / 계층)”

Cả hai tạo effective nonlinear biểu diễn (representation / 표현), nhưng kernel map thường fixed/implicit còn neural biểu diễn (representation / 표현) learned.

### “SVM score là xác suất (probability / 확률)”

Không. Margin score cần calibration nếu muốn probabilistic interpretation.

## Liên kết kiến thức (knowledge connection / 지식 연결)

SVM nối [Optimization](../01_mathematical_foundations/06_optimization.md), [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Bias–Variance](./14_bias_variance_and_generalization.md).

Xem tiếp: [Clustering](./11_clustering.md), nơi không còn mục tiêu (target / 대상) labels để định nghĩa ranh giới (boundary / 경계).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 what is machine learning](./00_what_is_machine_learning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
