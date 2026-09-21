# Decision Tree: học bằng cách chia không gian thành các vùng

**Decision Tree (의사결정나무 / cây quyết định)** tiếp cận dự đoán theo cách khác Linear Regression hay k-NN. Thay vì dùng một tổng có trọng số toàn cục hoặc dựa vào khoảng cách, cây liên tục đặt câu hỏi về feature để chia dữ liệu thành các vùng ngày càng đồng nhất hơn về target.

Một cây có thể được đọc như chuỗi quy tắc:

```text
Nếu age < 30?
├── Có: nếu income > 50M? → class A
└── Không: nếu tenure < 2? → class B
```

Sự trực quan này làm Decision Tree dễ giải thích, nhưng training phía sau vẫn là một bài toán tối ưu: chọn phép chia (split) nào làm các node con “tốt hơn” node hiện tại theo một tiêu chí xác định.

## Từ phân vùng tới dự đoán

Trong classification, tại mỗi node ta có thể chọn feature `j` và threshold `t`:

\[
x_j\le t
\]

để chia dữ liệu thành hai tập trái/phải.

Mục tiêu là làm phân phối lớp trong mỗi node con trở nên thuần hơn.

Một thước đo độ hỗn tạp phổ biến là **Gini impurity**:

\[
Gini=1-\sum_k p_k^2
\]

Nếu node chỉ chứa một lớp thì `Gini = 0`.

Entropy:

\[
H=-\sum_k p_k\log p_k
\]

cũng có thể được sử dụng.

Chất lượng split thường được đo bằng mức giảm độ hỗn tạp:

\[
Gain=I(parent)-\frac{n_L}{n}I(left)-\frac{n_R}{n}I(right)
\]

Cây ưu tiên split có gain cao nhất ở bước hiện tại.

## Training tham lam

Decision Tree thường được huấn luyện theo chiến lược **tham lam (greedy)**: ở mỗi node, chọn split tốt nhất tại thời điểm đó thay vì thử toàn bộ mọi cây hoàn chỉnh có thể có.

Cách này làm training khả thi về mặt tính toán nhưng không bảo đảm tìm được cây tối ưu toàn cục.

Đây là một ví dụ quan trọng trong AI Engineering: chấp nhận heuristic hoặc greedy optimization vì bài toán tổ hợp chính xác quá đắt.

## Regression Tree

Trong hồi quy, output ở leaf thường là trung bình target của các mẫu rơi vào leaf đó.

Split có thể được chọn để giảm phương sai hoặc tổng bình phương sai số:

\[
SSE=\sum_{i\in leaf}(y_i-\bar y)^2
\]

Vì vậy Regression Tree tạo một xấp xỉ dạng hằng theo từng vùng (piecewise-constant approximation) của hàm mục tiêu.

## Vì sao Tree mô hình hóa interaction và phi tuyến tốt?

Giả sử outcome chỉ cao khi đồng thời `x1 > 5` và `x2 < 3`. Cây có thể biểu diễn điều kiện này tự nhiên bằng hai split liên tiếp.

Mô hình tuyến tính sẽ cần thêm interaction feature rõ ràng, trong khi tree tự phát hiện tương tác có điều kiện thông qua cấu trúc nhánh.

Đây là một trong những lý do tree-based model rất mạnh với dữ liệu dạng bảng (tabular data).

## Overfitting

Một cây quá sâu có thể tiếp tục chia cho tới khi mỗi leaf gần như ghi nhớ từng mẫu training. Training error khi đó rất thấp nhưng variance cao.

Có thể kiểm soát độ phức tạp bằng các tham số như:

- `max_depth`;
- `min_samples_split`;
- `min_samples_leaf`;
- `max_leaf_nodes`;
- pruning.

**Cắt tỉa (pruning / 가지치기)** loại bỏ các nhánh mang lại cải thiện quá nhỏ so với độ phức tạp tăng thêm.

Một objective kiểu cost-complexity có dạng:

\[
R_\alpha(T)=R(T)+\alpha|T|
\]

trong đó `|T|` đại diện cho số leaf hoặc một thước đo độ phức tạp của cây.

## Tính không ổn định

Một hạn chế lớn của Decision Tree là **variance cao**. Chỉ một thay đổi nhỏ trong training data cũng có thể làm split đầu tiên thay đổi, kéo theo toàn bộ cấu trúc phía dưới khác đi.

Đây chính là lý do các phương pháp tổ hợp mô hình (ensemble) như Random Forest và Gradient Boosting rất thành công: chúng giảm hoặc khai thác sự không ổn định của từng tree riêng lẻ.

## Missing value và feature phân loại

Mỗi implementation có thể xử lý categorical feature và missing value theo cách khác nhau. One-hot encoding không phải lúc nào cũng là cách tốt nhất cho tree.

Một số thư viện hiện đại hỗ trợ split trực tiếp trên category hoặc định tuyến missing value theo cơ chế riêng.

Vì vậy cần hiểu semantics của framework đang dùng thay vì giả định mọi Decision Tree implementation đều giống nhau.

## Độ quan trọng của feature

Tree có thể tính **impurity-based feature importance** bằng tổng mức giảm impurity mà từng feature tạo ra.

Tuy nhiên metric này có thiên lệch, đặc biệt với feature liên tục hoặc feature có cardinality cao.

**Permutation importance** đo một cách khác: xáo trộn một feature rồi xem performance giảm bao nhiêu.

Permutation importance thường phản ánh mức phụ thuộc của mô hình tốt hơn trong nhiều trường hợp, nhưng cả hai loại importance vẫn không đồng nghĩa với tác động nhân quả ngoài thế giới thật.

## Đường ra quyết định và giải thích cục bộ

Một prediction có thể được truy vết theo đúng đường đi trong cây:

```text
income > 50M
→ age < 35
→ debt_ratio < 0.2
→ approve
```

Với cây nhỏ, cách này dễ audit hơn neural network.

Tuy nhiên khi dùng ensemble với hàng trăm hoặc hàng nghìn tree, khả năng diễn giải toàn cục giảm đáng kể.

## Phân vùng song song với trục

Decision Tree chuẩn thường chia theo một feature tại một thời điểm. Vì vậy ranh giới quyết định thường **song song với các trục (axis-aligned)**.

Một ranh giới chéo mượt có thể cần rất nhiều hình chữ nhật nhỏ để xấp xỉ.

Đây chính là một inductive bias của tree.

## Tree thường không cần chuẩn hóa scale

Vì split dựa trên thứ tự và threshold, một phép biến đổi đơn điệu của feature thường không thay đổi logic chia cây theo cùng cách như k-NN hoặc các mô hình dựa trên khoảng cách.

Do đó Decision Tree thường không cần standardization để hoạt động tốt.

Tuy nhiên preprocessing vẫn rất quan trọng với missing value, categorical encoding và data leakage.

## Mô hình tư duy

> Decision Tree học bằng cách liên tục đặt những câu hỏi làm phân phối target trong từng vùng trở nên đơn giản và thuần hơn.

## Các hiểu lầm thường gặp

### “Tree dễ đọc nên mọi Tree đều dễ giải thích”

Không. Cây nhỏ dễ đọc; cây rất sâu hoặc ensemble lớn thì không còn đơn giản nữa.

### “Feature importance của Tree cho biết feature quan trọng ngoài thế giới thật”

Không. Nó chỉ phản ánh mức mô hình hiện tại phụ thuộc vào feature dưới dữ liệu và metric hiện tại.

### “Tree không overfit vì rule rất đơn giản”

Sai. Một cây đủ sâu có thể ghi nhớ training data rất mạnh.

### “Tree không cần preprocessing”

Không đúng. Nó không cần scaling giống k-NN, nhưng leakage, category handling và missingness vẫn có thể làm mô hình sai nghiêm trọng.

## Liên kết kiến thức

Decision Tree nối trực tiếp tới [Ensemble Learning](./09_ensemble_learning.md). Một cây đơn lẻ thường chưa phải lựa chọn tốt nhất: Random Forest giảm variance bằng trung bình hóa nhiều cây, còn Gradient Boosting xây cây tuần tự để sửa phần sai còn lại của mô hình trước đó.