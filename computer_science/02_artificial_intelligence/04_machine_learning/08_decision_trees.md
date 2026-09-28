# Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng

> **Mạch đọc:** Đặt **quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Từ partition tới prediction** sang **Greedy huấn luyện (training / 학습)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Cây quyết định (decision tree / 의사결정 트리) tiếp cận prediction theo cách khác mô hình tuyến tính (linear model / 선형 모델) và k-NN. Thay vì dùng một weighted sum toàn cục hoặc so khoảng cách, cây (tree / 트리) liên tục đặt câu hỏi về tính năng (feature / 기능) để chia dữ liệu (data / 데이터) thành các vùng ngày càng homogeneous.

Một cây (tree / 트리) có thể được đọc như một chuỗi quy tắc (rule / 규칙):

```text
Nếu age < 30?
├── Yes: nếu income > 50M? → class A
└── No:  nếu tenure < 2?   → class B
```

Sự trực quan này làm cây (tree / 트리) dễ giải thích, nhưng cơ chế huấn luyện (training / 학습) phía sau vẫn là một tối ưu hóa (optimization / 최적화) bài toán (problem / 문제): chọn split nào làm các child nodes “tốt hơn” nút (node / 노드) hiện tại.

## Từ partition tới prediction

Giả sử classification. Tại mỗi nút (node / 노드) ta chọn tính năng (feature / 기능) `j` và threshold `t`:

\[
x_j\le t
\]

để chia samples thành left/right subsets.

Mục tiêu là làm lớp (class / 클래스) phân phối (distribution / 분포) trong mỗi child nút (node / 노드) thuần hơn.

Một impurity measure phổ biến là **Gini impurity**:

\[
Gini=1-\sum_k p_k^2
\]

Nếu nút (node / 노드) chỉ chứa một lớp (class / 클래스), Gini = 0.

Entropy:

\[
H=-\sum_k p_k\log p_k
\]

cũng có thể dùng. Split chất lượng (quality / 품질) thường dựa trên impurity reduction:

\[
Gain=I(parent)-\frac{n_L}{n}I(left)-\frac{n_R}{n}I(right)
\]

Cây (tree / 트리) chọn split có gain cao nhất tại bước hiện tại.

## Greedy huấn luyện (training / 학습)

Huấn luyện (training / 학습) cây quyết định (decision tree / 의사결정 트리) thường là greedy: tại mỗi nút (node / 노드) chọn locally best split, không tìm kiếm (search / 검색) mọi possible complete cây (tree / 트리).

Điều này làm huấn luyện (training / 학습) khả thi nhưng không đảm bảo global-optimal cây (tree / 트리).

Đây là một example quan trọng của AI kỹ thuật (engineering / 엔지니어링): ta chấp nhận heuristic/greedy tối ưu hóa (optimization / 최적화) vì chính xác (exact / 정확한) combinatorial tối ưu hóa (optimization / 최적화) quá đắt.

## Regression Trees

Với regression, leaf đầu ra (output / 출력) thường là mean mục tiêu (target / 대상) của samples trong leaf.

Split có thể minimize weighted variance hoặc squared lỗi (error / 오류):

\[
SSE=\sum_{i\in leaf}(y_i-\bar y)^2
\]

Cây (tree / 트리) vì vậy tạo piecewise-constant approximation của mục tiêu (target / 대상) hàm (function / 함수).

## Tại sao cây (tree / 트리) có thể mô hình (model / 모델) nonlinear tương tác (interaction / 상호작용)?

Giả sử kết quả (outcome / 결과) chỉ cao khi cả `x1 > 5` và `x2 < 3`. cây (tree / 트리) dễ encode tương tác (interaction / 상호작용) bằng sequential splits.

Mô hình tuyến tính (linear model / 선형 모델) cần tường minh (explicit / 명시적) tương tác (interaction / 상호작용) tính năng (feature / 기능); cây (tree / 트리) tự discover conditional tương tác (interaction / 상호작용) thông qua branch cấu trúc (structure / 구조).

Điều này là lý do tree-based các mô hình (models / 모델들) cực mạnh với tabular dữ liệu (data / 데이터).

## Overfitting

Một cây (tree / 트리) sâu có thể tiếp tục split cho tới khi leaf gần như memorize huấn luyện (training / 학습) samples. huấn luyện (training / 학습) lỗi (error / 오류) rất thấp nhưng variance cao.

Điều khiển (control / 제어) độ phức tạp (complexity / 복잡도) bằng:

- `max_depth`;
- `min_samples_split`;
- `min_samples_leaf`;
- `max_leaf_nodes`;
- pruning.

**Pruning (가지치기 / cắt tỉa)** loại branch có improvement nhỏ so với độ phức tạp (complexity / 복잡도).

Cost-complexity mục tiêu (objective / 목표) có dạng:

\[
R_\alpha(T)=R(T)+\alpha|T|
\]

Trong đó `|T|` là số leaf hoặc measure độ phức tạp (complexity / 복잡도).

## Instability

Một limitation lớn: cây quyết định (decision tree / 의사결정 트리) có high variance. Thay đổi nhỏ trong dữ liệu huấn luyện (training data / 학습 데이터) có thể thay split đầu, kéo theo toàn bộ cấu trúc (structure / 구조) phía dưới khác.

Đây là lý do ensemble methods như Random Forest và độ dốc (gradient / 기울기) Boosting rất thành công: chúng giảm hoặc khai thác instability của individual cây (tree / 트리).

## Missing values và categorical variables

Hiện thực (implementation / 구현) khác nhau xử lý category/missing theo cách khác nhau. One-hot encoding không phải luôn tốt nhất cho cây (tree / 트리).

Một số thư viện (library / 라이브러리) hiện đại tìm split categorical trực tiếp hoặc có bản địa (native / 네이티브) missing-value routing.

Cần hiểu ngữ nghĩa (semantics / 의미론) của khung phần mềm (framework / 프레임워크) thay vì assume mọi cây (tree / 트리) hiện thực (implementation / 구현) giống nhau.

## Tính năng (feature / 기능) importance

Cây (tree / 트리) có thể tính impurity-based tính năng (feature / 기능) importance bằng tổng impurity reduction do tính năng (feature / 기능) tạo ra.

Nhưng measure này có độ lệch (bias / 편향), đặc biệt với continuous/high-cardinality features.

Permutation importance thường đáng tin hơn về “mô hình (model / 모델) dependence”: shuffle một tính năng (feature / 기능) và đo hiệu năng (performance / 성능) giảm bao nhiêu.

Tuy nhiên cả hai vẫn không tự động là nhân quả (causal / 인과적) importance.

## Quyết định (decision / 결정) đường dẫn (path / 경로) và cục bộ (local / 로컬) explanation

Một prediction có thể dấu vết (trace / 추적) qua đường dẫn (path / 경로):

```text
income > 50M
→ age < 35
→ debt_ratio < 0.2
→ approve
```

Điều này dễ kiểm tra (audit / 감사) hơn neural mạng (network / 네트워크), nhưng với ensemble hàng nghìn trees thì toàn cục (global / 전역) interpretability giảm đáng kể.

## Axis-aligned partition

Tiêu chuẩn (standard / 표준) cây (tree / 트리) split theo một tính năng (feature / 기능) tại một thời điểm, nên ranh giới (boundary / 경계) thường axis-aligned.

Một diagonal ranh giới (boundary / 경계) có thể cần nhiều rectangular partitions để approximate.

Đây là inductive độ lệch (bias / 편향) của cây (tree / 트리).

## Cây (tree / 트리) không cần tính năng (feature / 기능) scaling

Vì split dựa trên thứ tự (ordering / 순서)/threshold, monotonic scaling thường không đổi split cấu trúc (structure / 구조). Đây là khác biệt với k-NN/SVM/gradient-based tuyến tính (linear / 선형) các mô hình (models / 모델들).

Nhưng preprocessing vẫn quan trọng cho missing/category ngữ nghĩa (semantics / 의미론) và leakage.

## Mô hình tư duy (mental model / 사고 모델)

> cây quyết định (decision tree / 의사결정 트리) học bằng cách đặt liên tiếp những câu hỏi làm mục tiêu (target / 대상) phân phối (distribution / 분포) trong mỗi vùng đơn giản hơn.

## Dùng chung (common / 공통) Misconceptions

### “cây (tree / 트리) dễ đọc nên cây (tree / 트리) luôn interpretable”

Cây (tree / 트리) nhỏ dễ đọc; cây (tree / 트리) sâu hoặc ensemble lớn thì không.

### “tính năng (feature / 기능) importance của cây (tree / 트리) cho biết tính năng (feature / 기능) quan trọng trong thế giới thật”

Nó chỉ phản ánh dependence của fitted mô hình (model / 모델) dưới dữ liệu (data / 데이터)/chỉ số (metric / 지표) hiện tại.

### “cây (tree / 트리) không overfit vì quy tắc (rule / 규칙) rất đơn giản”

Cây (tree / 트리) sâu có thể memorize dữ liệu (data / 데이터) rất mạnh.

### “cây (tree / 트리) không cần preprocessing”

Không cần scaling như distance-based mô hình (model / 모델), nhưng dữ liệu (data / 데이터) leakage, category handling và missingness vẫn rất quan trọng.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Cây quyết định (decision tree / 의사결정 트리) nối trực tiếp tới [Ensemble Learning](./09_ensemble_learning.md). Một single cây (tree / 트리) thường không phải final answer; Random Forest giảm variance bằng averaging, còn độ dốc (gradient / 기울기) Boosting xây trees tuần tự để sửa residual/errors.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 what is machine learning](./00_what_is_machine_learning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
