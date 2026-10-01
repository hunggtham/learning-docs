# Clustering: tìm cấu trúc (structure / 구조) khi không có labels

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Clustering không “khám phá sự thật tự nhiên” một cách trung lập** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **k-Means** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Clustering (군집화 / phân cụm) là family của unsupervised học tập (learning / 학습) nơi ta muốn nhóm observations thành những clusters có nội bộ (internal / 내부) similarity cao và khác nhau đủ rõ. Nghe đơn giản, nhưng ngay lập tức xuất hiện câu hỏi khó: **“giống nhau” theo nghĩa nào, và bao nhiêu cluster thực sự tồn tại?**

Không có ground-truth label để trả lời trực tiếp. Vì vậy clustering phụ thuộc rất mạnh vào biểu diễn (representation / 표현), distance, algorithmic các giả định (assumptions / 가정들) và mục tiêu sử dụng.

## Clustering không “khám phá sự thật tự nhiên” một cách trung lập

Cùng một dataset có thể được cluster khác nhau nếu:

- quy mô (scale / 규모) features khác;
- dùng Euclidean hay cosine distance;
- chọn k khác;
- dùng density-based thay centroid-based phương thức (method / 메서드);
- biểu diễn (representation / 표현) khác.

Do đó cluster là kết quả của **dữ liệu (data / 데이터) + biểu diễn (representation / 표현) + similarity notion + thuật toán (algorithm / 알고리즘)**, không phải đối tượng (object / 객체) có sẵn mà thuật toán (algorithm / 알고리즘) chỉ việc “nhìn thấy”.

> **Chuyển mạch:** Trong **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **k-Means** tiếp nhận điểm tựa từ **Clustering không “khám phá sự thật tự nhiên” một cách trung lập** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hình học (geometry / 기하학) của k-Means** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## k-Means

k-Means giả định cần tìm `k` centroids:

\[
\mu_1,...,\mu_k
\]

để minimize within-cluster squared distance:

\[
J=\sum_{i=1}^{n}\|x_i-\mu_{c_i}\|^2
\]

Thuật toán (algorithm / 알고리즘) Lloyd lặp hai bước:

1. assign mỗi điểm (point / 지점) tới centroid gần nhất;
2. recompute centroid là mean của assigned points.

Mỗi iteration không làm mục tiêu (objective / 목표) tăng, nhưng solution có thể chỉ là cục bộ (local / 로컬) optimum.

> **Chuyển mạch:** Ở chặng này của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Hình học (geometry / 기하학) của k-Means** tiếp nhận điểm tựa từ **k-Means** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Initialization và k-Means++** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hình học (geometry / 기하학) của k-Means

Vì dùng squared Euclidean distance và mean, k-Means ưu tiên clusters gần dạng spherical/convex với quy mô (scale / 규모) tương tự.

Nếu cluster hình vòng cung, density khác nhau hoặc có outliers mạnh, k-Means có thể tạo partition không phù hợp.

Tính năng (feature / 기능) scaling rất quan trọng vì squared distance bị quy mô (scale / 규모) dominate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Initialization và k-Means++** tiếp nhận điểm tựa từ **Hình học (geometry / 기하학) của k-Means** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chọn k** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Initialization và k-Means++

Random initialization có thể dẫn tới poor cục bộ (local / 로컬) solution. **k-Means++** chọn initial centroids spread out hơn theo distance-weighted chiến lược (strategy / 전략) và thường cải thiện stability.

Best practice vẫn là chạy nhiều initializations và chọn run có inertia/mục tiêu (objective / 목표) tốt.

> **Chuyển mạch:** Trong **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Chọn k** tiếp nhận điểm tựa từ **Initialization và k-Means++** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gaussian Mixture các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chọn k

Không có một universal formula.

**Elbow phương thức (method / 메서드)** nhìn reduction trong within-cluster sum of squares khi tăng `k` và tìm điểm improvement bắt đầu giảm.

**Silhouette coefficient** cho điểm (point / 지점) `i`:

\[
s(i)=\frac{b(i)-a(i)}{\max(a(i),b(i))}
\]

trong đó `a(i)` là average distance trong cluster hiện tại, `b(i)` là lowest average distance tới cluster khác.

Nhưng chỉ số (metric / 지표) nội tại không thay thế lĩnh vực (domain / 도메인) usefulness. “Mathematically separated” không đồng nghĩa “nghiệp vụ (business / 비즈니스) meaningful”.

> **Chuyển mạch:** Ở chặng này của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Gaussian Mixture các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Chọn k** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hierarchical Clustering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gaussian Mixture các mô hình (models / 모델들)

k-Means gán hard cluster. Gaussian Mixture mô hình (model / 모델) (GMM) giả định dữ liệu (data / 데이터) sinh từ mixture distributions:

\[
p(x)=\sum_{k=1}^{K}\pi_k\mathcal N(x\mid\mu_k,\Sigma_k)
\]

Đầu ra (output / 출력) responsibility:

\[
P(z=k\mid x)
\]

là soft cluster assignment.

GMM thường train bằng Expectation-Maximization (EM):

- **E-step**: estimate responsibilities với hiện tại (current / 현재) parameters;
- **M-step**: cập nhật (update / 업데이트) parameters để maximize expected complete-data log-likelihood.

GMM cho elliptical clusters thông qua covariance, linh hoạt hơn k-Means nhưng dựa vào Gaussian-mixture các giả định (assumptions / 가정들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Hierarchical Clustering** tiếp nhận điểm tựa từ **Gaussian Mixture các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DBSCAN: cluster bằng density** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hierarchical Clustering

Hierarchical clustering tạo dendrogram thay vì yêu cầu một partition duy nhất.

**Agglomerative** bắt đầu mỗi điểm (point / 지점) là một cluster rồi merge dần.

Linkage quyết định distance giữa clusters:

- single linkage: nearest pair;
- complete linkage: farthest pair;
- average linkage;
- Ward linkage: minimize variance increase.

Mỗi linkage encode một cluster-shape độ lệch (bias / 편향) khác nhau.

Dendrogram hữu ích khi lĩnh vực (domain / 도메인) có hierarchy hoặc chưa muốn chốt `k` ngay.

> **Chuyển mạch:** Trong **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **DBSCAN: cluster bằng density** tiếp nhận điểm tựa từ **Hierarchical Clustering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HDBSCAN** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DBSCAN: cluster bằng density

DBSCAN định nghĩa dense regions dựa trên radius `ε` và `min_samples`.

Nó có hai lợi thế quan trọng:

- không cần specify số cluster trước;
- có thể tìm arbitrary-shaped clusters và mark noise points.

Nhưng nếu density thay đổi mạnh giữa regions, một toàn cục (global / 전역) `ε` khó phù hợp. High dimension cũng làm distance less meaningful.

> **Chuyển mạch:** Ở chặng này của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **HDBSCAN** tiếp nhận điểm tựa từ **DBSCAN: cluster bằng density** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Clustering văn bản (text / 텍스트) và embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HDBSCAN

HDBSCAN mở rộng density-based clustering bằng hierarchy/stability, thường xử lý variable density tốt hơn DBSCAN và cho noise/outlier assignment linh hoạt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Clustering văn bản (text / 텍스트) và embeddings** tiếp nhận điểm tựa từ **HDBSCAN** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cluster labeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Clustering văn bản (text / 텍스트) và embeddings

Raw bag-of-words rất high-dimensional. hiện đại (modern / 현대적) workflow thường:

```text
Documents
   ↓ embedding model
Dense semantic vectors
   ↓ optional dimensionality reduction
Clustering
   ↓ inspect representative items / labels
```

Nhưng cluster chất lượng (quality / 품질) phụ thuộc embedding mục tiêu (objective / 목표). Embedding optimized cho retrieval không chắc tối ưu cho clustering.

> **Chuyển mạch:** Trong **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Clustering văn bản (text / 텍스트) và embeddings** cho ta quy tắc; **Cluster labeling** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Evaluating clustering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cluster labeling

Thuật toán (algorithm / 알고리즘) trả cluster IDs như `0,1,2`, không tự cung cấp ý nghĩa (semantic meaning / 의미적 뜻).

Con người hoặc downstream mô hình (model / 모델) phải inspect examples/centroids/key terms để gán interpretation.

LLM có thể hỗ trợ summarize cluster content, nhưng label do LLM tạo là một tầng (layer / 계층) interpretation khác, không phải proof về latent category thật.

> **Chuyển mạch:** Ở chặng này của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Cluster labeling** cho ta quy tắc; **Evaluating clustering** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Customer segmentation example** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluating clustering

Nếu có bên ngoài (external / 외부) labels, Adjusted Rand chỉ mục (index / 인덱스), Normalized Mutual thông tin (information / 정보) có thể so partition.

Nếu không có labels, silhouette/Davies–Bouldin/nội bộ (internal / 내부) metrics chỉ đo properties liên quan hình học (geometry / 기하학).

Quan trọng nhất thường là **downstream validity**: clusters có giúp segmentation, anomaly phân tích (analysis / 분석), sampling hoặc quyết định (decision / 결정) making không?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Evaluating clustering** cho ta quy tắc; **Customer segmentation example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Customer segmentation example

Nếu cluster khách hàng bằng annual spend, visit frequency và recency, quy mô (scale / 규모)/normalization quyết định hình học (geometry / 기하학). Nếu annual spend tính KRW magnitude lớn, nó có thể dominate.

Sau clustering, segment chỉ hữu ích nếu stable và actionable. “Cluster 3” đẹp trên scatter plot nhưng thay hoàn toàn sau một tháng có thể không hữu ích cho nghiệp vụ (business / 비즈니스) thao tác (operation / 연산).

> **Chuyển mạch:** Trong **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Customer segmentation example** cho ta quy tắc; **Mô hình tư duy (mental model / 사고 모델)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Clustering không hỏi “label đúng là gì?”, mà hỏi “với biểu diễn (representation / 표현) và similarity các giả định (assumptions / 가정들) này, partition nào tạo cấu trúc (structure / 구조) hữu ích?”

> **Chuyển mạch:** Ở chặng này của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Unsupervised nghĩa không có giả định (assumption / 가정)”

Ngược lại: vì không có labels, algorithmic/biểu diễn (representation / 표현) các giả định (assumptions / 가정들) càng quan trọng.

### “k-Means tìm cluster tự nhiên”

Nó optimize squared distance tới centroids, favoring specific hình học (geometry / 기하학).

### “Silhouette cao chứng minh segmentation có ý nghĩa”

Nó chỉ cho biết separation theo chosen chỉ số (metric / 지표); nghiệp vụ (business / 비즈니스)/lĩnh vực (domain / 도메인) meaning cần kiểm tra hợp lệ (validation / 검증) khác.

### “Embedding cluster chính là ngữ nghĩa (semantic / 의미적) categories”

Embedding hình học (geometry / 기하학) phụ thuộc huấn luyện (training / 학습) mục tiêu (objective / 목표) và corpus. Categories là interpretation, không automatic truth.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Clustering: tìm cấu trúc (structure / 구조) khi không có labels**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Clustering nối [k-NN and Distance-Based Learning](./07_knn_and_distance_based_learning.md), [Dimensionality Reduction](./12_dimensionality_reduction.md), [Representation Learning](../05_neural_networks/08_representation_learning.md) và [Anomaly Detection](./13_anomaly_detection.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
