# Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ separating hyperplane tới margin** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Tại sao margin có ý nghĩa?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối support vector machines với margin, kernel và optimization, để boundary phân loại được gắn với hình học và regularization.

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

> **Chuyển mạch:** Trong **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Tại sao margin có ý nghĩa?** tiếp nhận điểm tựa từ **Từ separating hyperplane tới margin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hỗ trợ (support / 지원) Vectors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao margin có ý nghĩa?

Nếu có nhiều boundaries đều classify huấn luyện (training / 학습) set hoàn hảo, ranh giới (boundary / 경계) đi sát dữ liệu (data / 데이터) points dễ thay đổi prediction khi đầu vào (input / 입력) perturb nhẹ. Large margin chọn solution có buffer lớn hơn.

Đây là một inductive độ lệch (bias / 편향) về robustness/generalization.

> **Chuyển mạch:** Ở chặng này của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Hỗ trợ (support / 지원) Vectors** tiếp nhận điểm tựa từ **Tại sao margin có ý nghĩa?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Soft Margin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hỗ trợ (support / 지원) Vectors

Chỉ những points nằm trên hoặc trong margin quyết định optimum mạnh nhất. Chúng gọi là **hỗ trợ (support / 지원) vectors (서포트 벡터)**.

Points rất xa ranh giới (boundary / 경계) thường không ảnh hưởng solution nếu các ràng buộc (constraints / 제약조건들) đã satisfied.

Đây là reason SVM có tên như vậy: ranh giới (boundary / 경계) được “đỡ” bởi trọng yếu (critical / 중요) examples.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Soft Margin** tiếp nhận điểm tựa từ **Hỗ trợ (support / 지원) Vectors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hinge mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Hinge mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Soft Margin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính năng (feature / 기능) Scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hinge mất mát (loss / 손실)

Soft-margin SVM có thể viết gần với regularized empirical rủi ro (risk / 위험):

\[
J(w)=\frac12\|w\|^2+C\sum_i\max(0,1-y_if(x_i))
\]

Hinge mất mát (loss / 손실) bằng zero khi example không chỉ đúng mà còn nằm ngoài margin.

> **Chuyển mạch:** Ở chặng này của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Tính năng (feature / 기능) Scaling** tiếp nhận điểm tựa từ **Hinge mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kernel Trick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính năng (feature / 기능) Scaling

SVM phụ thuộc dot products/distances, nên tính năng (feature / 기능) quy mô (scale / 규모) rất quan trọng. Một tính năng (feature / 기능) magnitude lớn có thể dominate hình học (geometry / 기하학).

Standardization thường là preprocessing mặc định cho SVM.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Kernel Trick** tiếp nhận điểm tựa từ **Tính năng (feature / 기능) Scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kernel không phải magic similarity bất kỳ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Kernel không phải magic similarity bất kỳ** tiếp nhận điểm tựa từ **Kernel Trick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **C và gamma** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kernel không phải magic similarity bất kỳ

Kernel hợp lệ cần thỏa properties để tương ứng inner sản phẩm (product / 제품) trong một tính năng (feature / 기능) không gian (space / 공간), thường liên quan positive semidefinite Gram ma trận (matrix / 행렬).

Không phải mọi similarity hàm (function / 함수) tùy ý đều có thể dùng như kernel mà vẫn giữ lý thuyết (theory / 이론)/tối ưu hóa (optimization / 최적화) properties.

> **Chuyển mạch:** Ở chặng này của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **C và gamma** tiếp nhận điểm tựa từ **Kernel không phải magic similarity bất kỳ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Computational scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## C và gamma

Với RBF SVM:

- `C` điều khiển penalty cho classification errors/margin violations;
- `γ` điều khiển mức cục bộ (local / 로컬) của kernel.

`γ` quá lớn làm mỗi điểm (point / 지점) influence vùng rất nhỏ → ranh giới (boundary / 경계) phức tạp/high variance.

`γ` quá nhỏ làm influence quá rộng → mô hình (model / 모델) quá smooth/high độ lệch (bias / 편향).

Hyperparameter tìm kiếm (search / 검색) cần nested/correct kiểm tra hợp lệ (validation / 검증) để tránh optimistic độ lệch (bias / 편향).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Computational scaling** tiếp nhận điểm tựa từ **C và gamma** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SVM vs Logistic Regression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Computational scaling

Kernel SVM cần pairwise relationships giữa huấn luyện (training / 학습) points; bộ nhớ (memory / 메모리)/thời gian (time / 시간) có thể tăng rất mạnh với `n`.

Vì vậy kernel SVM phù hợp hơn small/medium datasets. Large-scale problems thường dùng tuyến tính (linear / 선형) SVM, approximate kernels hoặc các mô hình (models / 모델들) khác.

> **Chuyển mạch:** Trong **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **SVM vs Logistic Regression** tiếp nhận điểm tựa từ **Computational scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kernels và Neural biểu diễn (representation / 표현) học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SVM vs Logistic Regression

Cả hai có tuyến tính (linear / 선형) quyết định (decision / 결정) ranh giới (boundary / 경계) nếu dùng raw tuyến tính (linear / 선형) features.

Logistic Regression optimize probabilistic log-loss và đầu ra (output / 출력) xác suất (probability / 확률) mô hình (model / 모델) trực tiếp.

SVM optimize margin/hinge mục tiêu (objective / 목표); raw quyết định (decision / 결정) score không phải calibrated xác suất (probability / 확률).

Nếu cần xác suất (probability / 확률), có thể calibrate SVM bằng Platt scaling hoặc isotonic regression trên held-out dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Kernels và Neural biểu diễn (representation / 표현) học tập (learning / 학습)** tiếp nhận điểm tựa từ **SVM vs Logistic Regression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kernels và Neural biểu diễn (representation / 표현) học tập (learning / 학습)

Kernel methods encode nonlinear similarity thông qua fixed/designed kernel. Deep học tập (learning / 학습) học biểu diễn (representation / 표현) `φ_θ(x)` từ dữ liệu (data / 데이터).

Có thể nhìn một neural mạng (network / 네트워크) như học tính năng (feature / 기능) không gian (space / 공간) rồi dùng simple đầu ra (output / 출력) head. Difference lớn là tính năng (feature / 기능) map trong deep học tập (learning / 학습) được learned jointly, thay vì kernel fixed trước.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Kernels và Neural biểu diễn (representation / 표현) học tập (learning / 학습)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> SVM hỏi: ranh giới (boundary / 경계) nào không chỉ đúng trên dữ liệu huấn luyện (training data / 학습 데이터) mà còn giữ khoảng cách an toàn lớn nhất với trọng yếu (critical / 중요) examples?

Kernel mở rộng câu hỏi này sang một tính năng (feature / 기능) không gian (space / 공간) nonlinear mà ta có thể không cần biểu diễn trực tiếp.

> **Chuyển mạch:** Trong **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “hỗ trợ (support / 지원) vectors là mọi points gần ranh giới (boundary / 경계)”

Theo tối ưu hóa (optimization / 최적화), hỗ trợ (support / 지원) vectors là points có nonzero dual coefficients; chúng là points active trong solution.

### “SVM luôn tốt cho high-dimensional dữ liệu (data / 데이터)”

Tuyến tính (linear / 선형) SVM có thể rất mạnh với sparse high-dimensional dữ liệu (data / 데이터) như văn bản (text / 텍스트), nhưng kernel SVM có scaling issue theo cỡ mẫu (sample size / 표본 크기).

### “Kernel trick giống neural mạng (network / 네트워크) hidden tầng (layer / 계층)”

Cả hai tạo effective nonlinear biểu diễn (representation / 표현), nhưng kernel map thường fixed/implicit còn neural biểu diễn (representation / 표현) learned.

### “SVM score là xác suất (probability / 확률)”

Không. Margin score cần calibration nếu muốn probabilistic interpretation.

> **Chuyển mạch:** Ở chặng này của **Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machines: margin, hình học (geometry / 기하학) và kernel**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

SVM nối [Optimization](../01_mathematical_foundations/06_optimization.md), [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Bias–Variance](./14_bias_variance_and_generalization.md).

Xem tiếp: [Clustering](./11_clustering.md), nơi không còn mục tiêu (target / 대상) labels để định nghĩa ranh giới (boundary / 경계).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
