# Decision Trees: học bằng cách chia không gian thành các vùng

Decision Tree (의사결정나무 / cây quyết định) tiếp cận prediction theo cách khác linear model và k-NN. Thay vì dùng một weighted sum toàn cục hoặc so khoảng cách, tree liên tục đặt câu hỏi về feature để chia data thành các vùng ngày càng homogeneous.

Một tree có thể được đọc như một chuỗi rule:

```text
Nếu age < 30?
├── Yes: nếu income > 50M? → class A
└── No:  nếu tenure < 2?   → class B
```

Sự trực quan này làm tree dễ giải thích, nhưng cơ chế training phía sau vẫn là một optimization problem: chọn split nào làm các child nodes “tốt hơn” node hiện tại.

## Từ partition tới prediction

Giả sử classification. Tại mỗi node ta chọn feature `j` và threshold `t`:

\[
x_j\le t
\]

để chia samples thành left/right subsets.

Mục tiêu là làm class distribution trong mỗi child node thuần hơn.

Một impurity measure phổ biến là **Gini impurity**:

\[
Gini=1-\sum_k p_k^2
\]

Nếu node chỉ chứa một class, Gini = 0.

Entropy:

\[
H=-\sum_k p_k\log p_k
\]

cũng có thể dùng. Split quality thường dựa trên impurity reduction:

\[
Gain=I(parent)-\frac{n_L}{n}I(left)-\frac{n_R}{n}I(right)
\]

Tree chọn split có gain cao nhất tại bước hiện tại.

## Greedy training

Training decision tree thường là greedy: tại mỗi node chọn locally best split, không search mọi possible complete tree.

Điều này làm training khả thi nhưng không đảm bảo global-optimal tree.

Đây là một example quan trọng của AI engineering: ta chấp nhận heuristic/greedy optimization vì exact combinatorial optimization quá đắt.

## Regression Trees

Với regression, leaf output thường là mean target của samples trong leaf.

Split có thể minimize weighted variance hoặc squared error:

\[
SSE=\sum_{i\in leaf}(y_i-\bar y)^2
\]

Tree vì vậy tạo piecewise-constant approximation của target function.

## Tại sao tree có thể model nonlinear interaction?

Giả sử outcome chỉ cao khi cả `x1 > 5` và `x2 < 3`. Tree dễ encode interaction bằng sequential splits.

Linear model cần explicit interaction feature; tree tự discover conditional interaction thông qua branch structure.

Điều này là lý do tree-based models cực mạnh với tabular data.

## Overfitting

Một tree sâu có thể tiếp tục split cho tới khi leaf gần như memorize training samples. Training error rất thấp nhưng variance cao.

Control complexity bằng:

- `max_depth`;
- `min_samples_split`;
- `min_samples_leaf`;
- `max_leaf_nodes`;
- pruning.

**Pruning (가지치기 / cắt tỉa)** loại branch có improvement nhỏ so với complexity.

Cost-complexity objective có dạng:

\[
R_\alpha(T)=R(T)+\alpha|T|
\]

Trong đó `|T|` là số leaf hoặc measure complexity.

## Instability

Một limitation lớn: decision tree có high variance. Thay đổi nhỏ trong training data có thể thay split đầu, kéo theo toàn bộ structure phía dưới khác.

Đây là lý do ensemble methods như Random Forest và Gradient Boosting rất thành công: chúng giảm hoặc khai thác instability của individual tree.

## Missing values và categorical variables

Implementation khác nhau xử lý category/missing theo cách khác nhau. One-hot encoding không phải luôn tốt nhất cho tree.

Một số library hiện đại tìm split categorical trực tiếp hoặc có native missing-value routing.

Cần hiểu semantics của framework thay vì assume mọi tree implementation giống nhau.

## Feature importance

Tree có thể tính impurity-based feature importance bằng tổng impurity reduction do feature tạo ra.

Nhưng measure này có bias, đặc biệt với continuous/high-cardinality features.

Permutation importance thường đáng tin hơn về “model dependence”: shuffle một feature và đo performance giảm bao nhiêu.

Tuy nhiên cả hai vẫn không tự động là causal importance.

## Decision path và local explanation

Một prediction có thể trace qua path:

```text
income > 50M
→ age < 35
→ debt_ratio < 0.2
→ approve
```

Điều này dễ audit hơn neural network, nhưng với ensemble hàng nghìn trees thì global interpretability giảm đáng kể.

## Axis-aligned partition

Standard tree split theo một feature tại một thời điểm, nên boundary thường axis-aligned.

Một diagonal boundary có thể cần nhiều rectangular partitions để approximate.

Đây là inductive bias của tree.

## Tree không cần feature scaling

Vì split dựa trên ordering/threshold, monotonic scaling thường không đổi split structure. Đây là khác biệt với k-NN/SVM/gradient-based linear models.

Nhưng preprocessing vẫn quan trọng cho missing/category semantics và leakage.

## Mental Model

> Decision Tree học bằng cách đặt liên tiếp những câu hỏi làm target distribution trong mỗi vùng đơn giản hơn.

## Common Misconceptions

### “Tree dễ đọc nên tree luôn interpretable”

Tree nhỏ dễ đọc; tree sâu hoặc ensemble lớn thì không.

### “Feature importance của tree cho biết feature quan trọng trong thế giới thật”

Nó chỉ phản ánh dependence của fitted model dưới data/metric hiện tại.

### “Tree không overfit vì rule rất đơn giản”

Tree sâu có thể memorize data rất mạnh.

### “Tree không cần preprocessing”

Không cần scaling như distance-based model, nhưng data leakage, category handling và missingness vẫn rất quan trọng.

## Knowledge Connection

Decision Tree nối trực tiếp tới [Ensemble Learning](./09_ensemble_learning.md). Một single tree thường không phải final answer; Random Forest giảm variance bằng averaging, còn Gradient Boosting xây trees tuần tự để sửa residual/errors.