# Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ partition tới prediction** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Greedy huấn luyện (training / 학습)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Greedy huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **Từ partition tới prediction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Regression Trees** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Greedy huấn luyện (training / 학습)

Huấn luyện (training / 학습) cây quyết định (decision tree / 의사결정 트리) thường là greedy: tại mỗi nút (node / 노드) chọn locally best split, không tìm kiếm (search / 검색) mọi possible complete cây (tree / 트리).

Điều này làm huấn luyện (training / 학습) khả thi nhưng không đảm bảo global-optimal cây (tree / 트리).

Đây là một example quan trọng của AI kỹ thuật (engineering / 엔지니어링): ta chấp nhận heuristic/greedy tối ưu hóa (optimization / 최적화) vì chính xác (exact / 정확한) combinatorial tối ưu hóa (optimization / 최적화) quá đắt.

> **Chuyển mạch:** Ở chặng này của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Regression Trees** tiếp nhận điểm tựa từ **Greedy huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tại sao cây (tree / 트리) có thể mô hình (model / 모델) nonlinear tương tác (interaction / 상호작용)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Regression Trees

Với regression, leaf đầu ra (output / 출력) thường là mean mục tiêu (target / 대상) của samples trong leaf.

Split có thể minimize weighted variance hoặc squared lỗi (error / 오류):

\[
SSE=\sum_{i\in leaf}(y_i-\bar y)^2
\]

Cây (tree / 트리) vì vậy tạo piecewise-constant approximation của mục tiêu (target / 대상) hàm (function / 함수).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Tại sao cây (tree / 트리) có thể mô hình (model / 모델) nonlinear tương tác (interaction / 상호작용)?** tiếp nhận điểm tựa từ **Regression Trees** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Overfitting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao cây (tree / 트리) có thể mô hình (model / 모델) nonlinear tương tác (interaction / 상호작용)?

Giả sử kết quả (outcome / 결과) chỉ cao khi cả `x1 > 5` và `x2 < 3`. cây (tree / 트리) dễ encode tương tác (interaction / 상호작용) bằng sequential splits.

Mô hình tuyến tính (linear model / 선형 모델) cần tường minh (explicit / 명시적) tương tác (interaction / 상호작용) tính năng (feature / 기능); cây (tree / 트리) tự discover conditional tương tác (interaction / 상호작용) thông qua branch cấu trúc (structure / 구조).

Điều này là lý do tree-based các mô hình (models / 모델들) cực mạnh với tabular dữ liệu (data / 데이터).

> **Chuyển mạch:** Trong **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Overfitting** tiếp nhận điểm tựa từ **Tại sao cây (tree / 트리) có thể mô hình (model / 모델) nonlinear tương tác (interaction / 상호작용)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Instability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Instability** tiếp nhận điểm tựa từ **Overfitting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Missing values và categorical variables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Instability

Một limitation lớn: cây quyết định (decision tree / 의사결정 트리) có high variance. Thay đổi nhỏ trong dữ liệu huấn luyện (training data / 학습 데이터) có thể thay split đầu, kéo theo toàn bộ cấu trúc (structure / 구조) phía dưới khác.

Đây là lý do ensemble methods như Random Forest và độ dốc (gradient / 기울기) Boosting rất thành công: chúng giảm hoặc khai thác instability của individual cây (tree / 트리).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Missing values và categorical variables** tiếp nhận điểm tựa từ **Instability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính năng (feature / 기능) importance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Missing values và categorical variables

Hiện thực (implementation / 구현) khác nhau xử lý category/missing theo cách khác nhau. One-hot encoding không phải luôn tốt nhất cho cây (tree / 트리).

Một số thư viện (library / 라이브러리) hiện đại tìm split categorical trực tiếp hoặc có bản địa (native / 네이티브) missing-value routing.

Cần hiểu ngữ nghĩa (semantics / 의미론) của khung phần mềm (framework / 프레임워크) thay vì assume mọi cây (tree / 트리) hiện thực (implementation / 구현) giống nhau.

> **Chuyển mạch:** Trong **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Tính năng (feature / 기능) importance** tiếp nhận điểm tựa từ **Missing values và categorical variables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quyết định (decision / 결정) đường dẫn (path / 경로) và cục bộ (local / 로컬) explanation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính năng (feature / 기능) importance

Cây (tree / 트리) có thể tính impurity-based tính năng (feature / 기능) importance bằng tổng impurity reduction do tính năng (feature / 기능) tạo ra.

Nhưng measure này có độ lệch (bias / 편향), đặc biệt với continuous/high-cardinality features.

Permutation importance thường đáng tin hơn về “mô hình (model / 모델) dependence”: shuffle một tính năng (feature / 기능) và đo hiệu năng (performance / 성능) giảm bao nhiêu.

Tuy nhiên cả hai vẫn không tự động là nhân quả (causal / 인과적) importance.

> **Chuyển mạch:** Ở chặng này của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Tính năng (feature / 기능) importance** xác định đầu vào; **Quyết định (decision / 결정) đường dẫn (path / 경로) và cục bộ (local / 로컬) explanation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Axis-aligned partition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyết định (decision / 결정) đường dẫn (path / 경로) và cục bộ (local / 로컬) explanation

Một prediction có thể dấu vết (trace / 추적) qua đường dẫn (path / 경로):

```text
income > 50M
→ age < 35
→ debt_ratio < 0.2
→ approve
```

Điều này dễ kiểm tra (audit / 감사) hơn neural mạng (network / 네트워크), nhưng với ensemble hàng nghìn trees thì toàn cục (global / 전역) interpretability giảm đáng kể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Quyết định (decision / 결정) đường dẫn (path / 경로) và cục bộ (local / 로컬) explanation** xác định đầu vào; **Axis-aligned partition** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Cây (tree / 트리) không cần tính năng (feature / 기능) scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Axis-aligned partition

Tiêu chuẩn (standard / 표준) cây (tree / 트리) split theo một tính năng (feature / 기능) tại một thời điểm, nên ranh giới (boundary / 경계) thường axis-aligned.

Một diagonal ranh giới (boundary / 경계) có thể cần nhiều rectangular partitions để approximate.

Đây là inductive độ lệch (bias / 편향) của cây (tree / 트리).

> **Chuyển mạch:** Trong **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Cây (tree / 트리) không cần tính năng (feature / 기능) scaling** tiếp nhận điểm tựa từ **Axis-aligned partition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cây (tree / 트리) không cần tính năng (feature / 기능) scaling

Vì split dựa trên thứ tự (ordering / 순서)/threshold, monotonic scaling thường không đổi split cấu trúc (structure / 구조). Đây là khác biệt với k-NN/SVM/gradient-based tuyến tính (linear / 선형) các mô hình (models / 모델들).

Nhưng preprocessing vẫn quan trọng cho missing/category ngữ nghĩa (semantics / 의미론) và leakage.

> **Chuyển mạch:** Ở chặng này của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Cây (tree / 트리) không cần tính năng (feature / 기능) scaling** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> cây quyết định (decision tree / 의사결정 트리) học bằng cách đặt liên tiếp những câu hỏi làm mục tiêu (target / 대상) phân phối (distribution / 분포) trong mỗi vùng đơn giản hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “cây (tree / 트리) dễ đọc nên cây (tree / 트리) luôn interpretable”

Cây (tree / 트리) nhỏ dễ đọc; cây (tree / 트리) sâu hoặc ensemble lớn thì không.

### “tính năng (feature / 기능) importance của cây (tree / 트리) cho biết tính năng (feature / 기능) quan trọng trong thế giới thật”

Nó chỉ phản ánh dependence của fitted mô hình (model / 모델) dưới dữ liệu (data / 데이터)/chỉ số (metric / 지표) hiện tại.

### “cây (tree / 트리) không overfit vì quy tắc (rule / 규칙) rất đơn giản”

Cây (tree / 트리) sâu có thể memorize dữ liệu (data / 데이터) rất mạnh.

### “cây (tree / 트리) không cần preprocessing”

Không cần scaling như distance-based mô hình (model / 모델), nhưng dữ liệu (data / 데이터) leakage, category handling và missingness vẫn rất quan trọng.

> **Chuyển mạch:** Trong **Quyết định (decision / 결정) Trees: học bằng cách chia không gian thành các vùng**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Cây quyết định (decision tree / 의사결정 트리) nối trực tiếp tới [Ensemble Learning](./09_ensemble_learning.md). Một single cây (tree / 트리) thường không phải final answer; Random Forest giảm variance bằng averaging, còn độ dốc (gradient / 기울기) Boosting xây trees tuần tự để sửa residual/errors.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
