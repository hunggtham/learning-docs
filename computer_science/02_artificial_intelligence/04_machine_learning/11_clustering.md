# Clustering: tìm structure khi không có labels

Clustering (군집화 / phân cụm) là family của unsupervised learning nơi ta muốn nhóm observations thành những clusters có internal similarity cao và khác nhau đủ rõ. Nghe đơn giản, nhưng ngay lập tức xuất hiện câu hỏi khó: **“giống nhau” theo nghĩa nào, và bao nhiêu cluster thực sự tồn tại?**

Không có ground-truth label để trả lời trực tiếp. Vì vậy clustering phụ thuộc rất mạnh vào representation, distance, algorithmic assumptions và mục tiêu sử dụng.

## Clustering không “khám phá sự thật tự nhiên” một cách trung lập

Cùng một dataset có thể được cluster khác nhau nếu:

- scale features khác;
- dùng Euclidean hay cosine distance;
- chọn k khác;
- dùng density-based thay centroid-based method;
- representation khác.

Do đó cluster là kết quả của **data + representation + similarity notion + algorithm**, không phải object có sẵn mà algorithm chỉ việc “nhìn thấy”.

## k-Means

k-Means giả định cần tìm `k` centroids:

\[
\mu_1,...,\mu_k
\]

để minimize within-cluster squared distance:

\[
J=\sum_{i=1}^{n}\|x_i-\mu_{c_i}\|^2
\]

Algorithm Lloyd lặp hai bước:

1. assign mỗi point tới centroid gần nhất;
2. recompute centroid là mean của assigned points.

Mỗi iteration không làm objective tăng, nhưng solution có thể chỉ là local optimum.

## Geometry của k-Means

Vì dùng squared Euclidean distance và mean, k-Means ưu tiên clusters gần dạng spherical/convex với scale tương tự.

Nếu cluster hình vòng cung, density khác nhau hoặc có outliers mạnh, k-Means có thể tạo partition không phù hợp.

Feature scaling rất quan trọng vì squared distance bị scale dominate.

## Initialization và k-Means++

Random initialization có thể dẫn tới poor local solution. **k-Means++** chọn initial centroids spread out hơn theo distance-weighted strategy và thường cải thiện stability.

Best practice vẫn là chạy nhiều initializations và chọn run có inertia/objective tốt.

## Chọn k

Không có một universal formula.

**Elbow method** nhìn reduction trong within-cluster sum of squares khi tăng `k` và tìm điểm improvement bắt đầu giảm.

**Silhouette coefficient** cho point `i`:

\[
s(i)=\frac{b(i)-a(i)}{\max(a(i),b(i))}
\]

trong đó `a(i)` là average distance trong cluster hiện tại, `b(i)` là lowest average distance tới cluster khác.

Nhưng metric nội tại không thay thế domain usefulness. “Mathematically separated” không đồng nghĩa “business meaningful”.

## Gaussian Mixture Models

k-Means gán hard cluster. Gaussian Mixture Model (GMM) giả định data sinh từ mixture distributions:

\[
p(x)=\sum_{k=1}^{K}\pi_k\mathcal N(x\mid\mu_k,\Sigma_k)
\]

Output responsibility:

\[
P(z=k\mid x)
\]

là soft cluster assignment.

GMM thường train bằng Expectation-Maximization (EM):

- **E-step**: estimate responsibilities với current parameters;
- **M-step**: update parameters để maximize expected complete-data log-likelihood.

GMM cho elliptical clusters thông qua covariance, linh hoạt hơn k-Means nhưng dựa vào Gaussian-mixture assumptions.

## Hierarchical Clustering

Hierarchical clustering tạo dendrogram thay vì yêu cầu một partition duy nhất.

**Agglomerative** bắt đầu mỗi point là một cluster rồi merge dần.

Linkage quyết định distance giữa clusters:

- single linkage: nearest pair;
- complete linkage: farthest pair;
- average linkage;
- Ward linkage: minimize variance increase.

Mỗi linkage encode một cluster-shape bias khác nhau.

Dendrogram hữu ích khi domain có hierarchy hoặc chưa muốn chốt `k` ngay.

## DBSCAN: cluster bằng density

DBSCAN định nghĩa dense regions dựa trên radius `ε` và `min_samples`.

Nó có hai lợi thế quan trọng:

- không cần specify số cluster trước;
- có thể tìm arbitrary-shaped clusters và mark noise points.

Nhưng nếu density thay đổi mạnh giữa regions, một global `ε` khó phù hợp. High dimension cũng làm distance less meaningful.

## HDBSCAN

HDBSCAN mở rộng density-based clustering bằng hierarchy/stability, thường xử lý variable density tốt hơn DBSCAN và cho noise/outlier assignment linh hoạt hơn.

## Clustering text và embeddings

Raw bag-of-words rất high-dimensional. Modern workflow thường:

```text
Documents
   ↓ embedding model
Dense semantic vectors
   ↓ optional dimensionality reduction
Clustering
   ↓ inspect representative items / labels
```

Nhưng cluster quality phụ thuộc embedding objective. Embedding optimized cho retrieval không chắc tối ưu cho clustering.

## Cluster labeling

Algorithm trả cluster IDs như `0,1,2`, không tự cung cấp semantic meaning.

Con người hoặc downstream model phải inspect examples/centroids/key terms để gán interpretation.

LLM có thể hỗ trợ summarize cluster content, nhưng label do LLM tạo là một layer interpretation khác, không phải proof về latent category thật.

## Evaluating clustering

Nếu có external labels, Adjusted Rand Index, Normalized Mutual Information có thể so partition.

Nếu không có labels, silhouette/Davies–Bouldin/internal metrics chỉ đo properties liên quan geometry.

Quan trọng nhất thường là **downstream validity**: clusters có giúp segmentation, anomaly analysis, sampling hoặc decision making không?

## Customer segmentation example

Nếu cluster khách hàng bằng annual spend, visit frequency và recency, scale/normalization quyết định geometry. Nếu annual spend tính KRW magnitude lớn, nó có thể dominate.

Sau clustering, segment chỉ hữu ích nếu stable và actionable. “Cluster 3” đẹp trên scatter plot nhưng thay hoàn toàn sau một tháng có thể không hữu ích cho business operation.

## Mental Model

> Clustering không hỏi “label đúng là gì?”, mà hỏi “với representation và similarity assumptions này, partition nào tạo structure hữu ích?”

## Common Misconceptions

### “Unsupervised nghĩa không có assumption”

Ngược lại: vì không có labels, algorithmic/representation assumptions càng quan trọng.

### “k-Means tìm cluster tự nhiên”

Nó optimize squared distance tới centroids, favoring specific geometry.

### “Silhouette cao chứng minh segmentation có ý nghĩa”

Nó chỉ cho biết separation theo chosen metric; business/domain meaning cần validation khác.

### “Embedding cluster chính là semantic categories”

Embedding geometry phụ thuộc training objective và corpus. Categories là interpretation, không automatic truth.

## Knowledge Connection

Clustering nối [k-NN and Distance-Based Learning](./07_knn_and_distance_based_learning.md), [Dimensionality Reduction](./12_dimensionality_reduction.md), [Representation Learning](../05_neural_networks/08_representation_learning.md) và [Anomaly Detection](./13_anomaly_detection.md).