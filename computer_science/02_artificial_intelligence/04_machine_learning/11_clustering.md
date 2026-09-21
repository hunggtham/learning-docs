# Clustering: tìm cấu trúc khi không có nhãn

**Clustering (군집화 / phân cụm)** là một họ phương pháp học không giám sát (unsupervised learning), trong đó mục tiêu là nhóm các quan sát thành những **cụm (cluster)** có mức tương đồng nội bộ cao và khác biệt đủ rõ với các cụm khác. Nghe có vẻ đơn giản, nhưng ngay lập tức xuất hiện hai câu hỏi khó: **“giống nhau” theo nghĩa nào, và thật sự có bao nhiêu cụm?**

Không có ground-truth label để trả lời trực tiếp. Vì vậy clustering phụ thuộc rất mạnh vào cách biểu diễn dữ liệu, metric khoảng cách, giả định của thuật toán và mục tiêu sử dụng phía sau.

## Clustering không trung lập “khám phá cấu trúc tự nhiên”

Cùng một dataset có thể tạo ra kết quả rất khác nếu thay đổi:

- scale của feature;
- Euclidean distance hay cosine similarity;
- số cụm `k`;
- phương pháp dựa trên mật độ thay vì centroid;
- representation đầu vào.

Vì vậy cluster là kết quả của:

```text
dữ liệu
+ biểu diễn
+ định nghĩa similarity
+ thuật toán
```

chứ không phải một object có sẵn mà thuật toán chỉ việc “nhìn thấy”.

## k-Means

k-Means giả định cần tìm `k` tâm cụm (centroid):

\[
\mu_1,...,\mu_k
\]

để tối thiểu hóa tổng bình phương khoảng cách bên trong cụm:

\[
J=\sum_{i=1}^{n}\|x_i-\mu_{c_i}\|^2
\]

Thuật toán Lloyd lặp hai bước:

1. gán mỗi điểm vào centroid gần nhất;
2. tính lại centroid bằng trung bình của các điểm đang thuộc cụm đó.

Mỗi vòng lặp không làm objective tăng, nhưng nghiệm cuối chỉ có thể là tối ưu cục bộ.

## Hình học của k-Means

Vì dùng squared Euclidean distance và mean, k-Means ưu tiên các cụm gần dạng cầu hoặc lồi, với kích thước và mật độ tương đối tương đồng.

Nếu dữ liệu có cụm hình vòng cung, mật độ rất khác nhau hoặc nhiều outlier, k-Means có thể tạo partition không phù hợp với cấu trúc ta mong muốn.

Feature scaling đặc biệt quan trọng vì squared distance rất dễ bị feature có scale lớn chi phối.

## Khởi tạo và k-Means++

Khởi tạo centroid ngẫu nhiên có thể dẫn tới nghiệm cục bộ kém.

**k-Means++** chọn các centroid ban đầu trải rộng hơn theo chiến lược có trọng số khoảng cách, nhờ đó thường cải thiện độ ổn định và chất lượng nghiệm.

Dù vậy, thực tế vẫn nên chạy nhiều lần với các initialization khác nhau rồi chọn nghiệm có inertia hoặc objective tốt hơn.

## Chọn số cụm k

Không có một công thức chung cho mọi dataset.

**Elbow method** xem mức giảm của within-cluster sum of squares khi tăng `k`, rồi tìm điểm mà lợi ích bắt đầu giảm mạnh.

**Silhouette coefficient** cho điểm `i`:

\[
s(i)=\frac{b(i)-a(i)}{\max(a(i),b(i))}
\]

trong đó `a(i)` là khoảng cách trung bình tới các điểm trong cụm hiện tại, còn `b(i)` là khoảng cách trung bình nhỏ nhất tới một cụm khác.

Tuy nhiên metric nội tại không thay thế ý nghĩa của domain. “Tách đẹp về toán học” không đồng nghĩa “có ý nghĩa nghiệp vụ”.

## Gaussian Mixture Model

k-Means gán mỗi điểm cứng vào đúng một cụm. **Gaussian Mixture Model (GMM)** giả định dữ liệu được sinh từ hỗn hợp nhiều phân phối Gaussian:

\[
p(x)=\sum_{k=1}^{K}\pi_k\mathcal N(x\mid\mu_k,\Sigma_k)
\]

Mỗi điểm có một mức trách nhiệm (responsibility):

\[
P(z=k\mid x)
\]

cho biết xác suất điểm thuộc thành phần `k`.

GMM thường được train bằng Expectation-Maximization (EM):

- **E-step**: ước lượng responsibility với tham số hiện tại;
- **M-step**: cập nhật tham số để tối đa hóa expected complete-data log-likelihood.

Nhờ covariance, GMM có thể mô tả các cụm dạng ellipse linh hoạt hơn k-Means, nhưng đổi lại phụ thuộc vào giả định Gaussian mixture.

## Hierarchical Clustering

Hierarchical clustering tạo ra **cây phân cấp (dendrogram)** thay vì chỉ một partition duy nhất.

Trong **agglomerative clustering**, ban đầu mỗi điểm là một cụm riêng, sau đó các cụm được gộp dần.

Cách đo khoảng cách giữa hai cụm gọi là **linkage**:

- single linkage: lấy cặp điểm gần nhất;
- complete linkage: lấy cặp xa nhất;
- average linkage: lấy khoảng cách trung bình;
- Ward linkage: ưu tiên mức tăng variance nhỏ nhất.

Mỗi linkage mang một inductive bias khác nhau về hình dạng cụm.

Dendrogram đặc biệt hữu ích khi domain có cấu trúc phân cấp hoặc khi chưa muốn chốt số cụm từ đầu.

## DBSCAN: phân cụm dựa trên mật độ

DBSCAN định nghĩa vùng có mật độ cao bằng bán kính `ε` và `min_samples`.

Hai ưu điểm chính là:

- không cần xác định trước số cluster;
- có thể tìm cụm có hình dạng bất kỳ và đánh dấu điểm nhiễu.

Tuy nhiên nếu mật độ giữa các vùng khác nhau mạnh, một `ε` toàn cục khó phù hợp cho tất cả.

Trong không gian nhiều chiều, khoảng cách cũng trở nên kém ý nghĩa hơn.

## HDBSCAN

HDBSCAN mở rộng ý tưởng phân cụm mật độ bằng cấu trúc phân cấp và độ ổn định của cluster.

Nó thường xử lý dữ liệu có mật độ thay đổi tốt hơn DBSCAN và cho phép phân loại noise hoặc outlier linh hoạt hơn.

## Clustering văn bản và embedding

Bag-of-words thô thường rất nhiều chiều. Quy trình hiện đại thường có dạng:

```text
Tài liệu
   ↓ embedding model
Vector ngữ nghĩa
   ↓ có thể giảm chiều
Clustering
   ↓
kiểm tra các mẫu đại diện / đặt tên cluster
```

Tuy nhiên chất lượng cluster phụ thuộc mạnh vào objective của embedding model.

Một embedding được tối ưu cho retrieval chưa chắc là embedding tối ưu cho clustering.

## Đặt tên cho cluster

Thuật toán thường chỉ trả ID như `0`, `1`, `2`. Nó không tự cho biết cluster “có nghĩa là gì”.

Con người hoặc một hệ downstream phải xem example, centroid, từ khóa hoặc đặc trưng tiêu biểu rồi gán diễn giải.

LLM có thể hỗ trợ tóm tắt nội dung cluster, nhưng label do LLM tạo vẫn chỉ là một lớp diễn giải, không phải bằng chứng về một “category ẩn thật sự” tồn tại khách quan.

## Đánh giá clustering

Nếu có external label, có thể dùng Adjusted Rand Index hoặc Normalized Mutual Information để so partition với nhãn tham chiếu.

Nếu không có label, các metric nội tại như silhouette hoặc Davies–Bouldin chỉ đo tính chất hình học dưới metric đã chọn.

Trong thực tế, điều quan trọng thường là **giá trị ở downstream**: cluster có giúp segmentation, anomaly analysis, sampling hay ra quyết định tốt hơn không?

## Ví dụ phân khúc khách hàng

Nếu cluster khách hàng bằng annual spend, visit frequency và recency, cách chuẩn hóa scale quyết định trực tiếp hình học.

Nếu annual spend dùng đơn vị KRW với giá trị rất lớn, nó có thể chi phối toàn bộ khoảng cách.

Sau clustering, segment chỉ hữu ích nếu đủ ổn định và có thể hành động. Một “Cluster 3” nhìn đẹp trên scatter plot nhưng thay hoàn toàn sau một tháng có thể không có nhiều giá trị vận hành.

## Mô hình tư duy

> Clustering không hỏi “label đúng là gì?”, mà hỏi “với representation và giả định similarity hiện tại, cách chia nào tạo ra cấu trúc hữu ích?”.

## Các hiểu lầm thường gặp

### “Unsupervised nghĩa là không có giả định”

Ngược lại. Vì không có label hướng dẫn, giả định từ representation và thuật toán càng quan trọng.

### “k-Means tìm ra cluster tự nhiên của dữ liệu”

Không. Nó tối ưu squared distance tới centroid và do đó ưu tiên một loại geometry cụ thể.

### “Silhouette cao chứng minh segmentation có ý nghĩa”

Không. Nó chỉ cho thấy mức phân tách theo metric đã chọn. Ý nghĩa nghiệp vụ cần được kiểm chứng riêng.

### “Cluster embedding chính là category ngữ nghĩa thật”

Không. Hình học embedding phụ thuộc objective và corpus huấn luyện. Category cuối cùng vẫn là một cách diễn giải.

## Liên kết kiến thức

Clustering nối [k-NN và học dựa trên khoảng cách](./07_knn_and_distance_based_learning.md), [Giảm chiều](./12_dimensionality_reduction.md), [Representation Learning](../05_neural_networks/08_representation_learning.md) và [Anomaly Detection](./13_anomaly_detection.md).