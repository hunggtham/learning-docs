# Anomaly Detection: khi điều quan trọng là những gì hiếm hoặc khác thường

**Anomaly Detection (이상 탐지 / phát hiện bất thường)** tìm các quan sát khác đáng kể so với hành vi được xem là bình thường. Giao dịch gian lận, xâm nhập mạng, cảm biến lỗi, đăng nhập bất thường hay sản phẩm lỗi trong dây chuyền đều có thể được mô hình hóa như bài toán phát hiện bất thường.

Khó khăn cốt lõi là **anomaly thường hiếm, phụ thuộc mạnh vào ngữ cảnh và đôi khi chưa từng xuất hiện trong dữ liệu huấn luyện có nhãn**. Vì vậy Anomaly Detection không chỉ là binary classification với class imbalance; trong nhiều trường hợp ta phải học trước một mô hình về “bình thường”, rồi đo mức lệch khỏi mô hình đó.

## Anomaly không đồng nghĩa outlier thống kê

Một điểm nằm xa mean có thể là outlier thống kê nhưng hoàn toàn hợp lệ trong domain.

Ngược lại, một giao dịch fraud có amount rất bình thường nhưng trở nên đáng ngờ vì tổ hợp thời gian, thiết bị, vị trí và lịch sử tài khoản.

Vì vậy anomaly luôn phụ thuộc vào ngữ cảnh và representation.

Ba dạng thường gặp:

- **bất thường điểm (point anomaly)**: một quan sát riêng lẻ khác thường;
- **bất thường theo ngữ cảnh (contextual anomaly)**: chỉ bất thường trong bối cảnh cụ thể, ví dụ đăng nhập lúc 3 giờ sáng từ quốc gia mới;
- **bất thường tập thể (collective anomaly)**: từng điểm riêng lẻ có vẻ bình thường nhưng cả chuỗi hoặc nhóm tạo pattern bất thường.

## Phát hiện bất thường bằng mô hình thống kê

Nếu giả định dữ liệu bình thường tuân theo Gaussian:

\[
x\sim\mathcal N(\mu,\Sigma)
\]

có thể dùng likelihood hoặc density. Một điểm có:

\[
p(x)<\epsilon
\]

có thể bị đánh dấu.

Khoảng cách Mahalanobis:

\[
d_M(x)=\sqrt{(x-\mu)^T\Sigma^{-1}(x-\mu)}
\]

xử lý correlation và scale của feature tốt hơn Euclidean distance trong mô hình Gaussian đa biến.

Tuy nhiên giả định Gaussian có thể sai nghiêm trọng với dữ liệu đa mode hoặc phi tuyến.

## z-score và thống kê bền vững

Một quy tắc một biến đơn giản:

\[
z=\frac{x-\mu}{\sigma}
\]

có thể đánh dấu khi `|z|>3`, chẳng hạn.

Nếu outlier làm mean và standard deviation bị méo, có thể dùng median và **Median Absolute Deviation (MAD)**:

\[
MAD=median(|x_i-median(x)|)
\]

Threshold nên được chọn theo mức false positive mà hệ thống vận hành chấp nhận được, không chỉ theo quy ước `3σ`.

## Isolation Forest

Isolation Forest dựa trên trực giác: anomaly vừa hiếm vừa khác nên thường dễ bị cô lập bằng các phép split ngẫu nhiên hơn điểm bình thường.

Hệ thống xây nhiều random tree; đường đi từ root tới leaf cô lập thường ngắn hơn với anomaly.

Ưu điểm là không cần ước lượng density tường minh, scale khá tốt trên dữ liệu bảng nhiều chiều và ít giả định phân phối hơn mô hình Gaussian.

Tuy nhiên hiệu quả vẫn phụ thuộc representation, tỷ lệ contamination và cách chọn threshold.

## One-Class SVM

One-Class SVM học một ranh giới bao quanh vùng dữ liệu được xem là bình thường trong kernel feature space. Điểm nằm ngoài vùng đó được xem như anomaly.

Phương pháp này có thể hữu ích với dataset vừa phải, nhưng cần lưu ý chi phí kernel và độ nhạy với hyperparameter.

## Local Outlier Factor

**Local Outlier Factor (LOF)** so sánh mật độ cục bộ của một điểm với mật độ của các láng giềng.

Nếu mật độ quanh điểm thấp đáng kể so với neighborhood, điểm đó có anomaly score cao.

Cách này hữu ích khi dataset có nhiều vùng mật độ toàn cục khác nhau, nhưng vẫn chịu các vấn đề quen thuộc của nearest-neighbor và high-dimensional geometry.

## Phát hiện dựa trên lỗi tái tạo

Autoencoder có thể được train trên dữ liệu phần lớn là bình thường:

\[
x\rightarrow z\rightarrow\hat x
\]

Nếu pattern bình thường được tái tạo tốt còn pattern lạ được tái tạo kém, reconstruction error:

\[
A(x)=\|x-\hat x\|
\]

có thể dùng làm anomaly score.

Tuy nhiên autoencoder có capacity lớn đôi khi vẫn tái tạo anomaly rất tốt.

Vì vậy reconstruction error không tự động là xác suất anomaly.

## Anomaly Detection cho chuỗi thời gian

Time series cần mô hình hành vi kỳ vọng theo trend, seasonality và dependency theo thời gian.

Một cách phổ biến là dùng phần dư:

\[
r_t=y_t-\hat y_t
\]

rồi đánh dấu khi residual vượt threshold.

Giá trị `100` có thể hoàn toàn bình thường vào giờ cao điểm nhưng bất thường vào ban đêm. Vì vậy baseline phải có ngữ cảnh.

Bất thường theo chuỗi có thể cần change-point detection, forecasting model hoặc state-space model.

## Fraud Detection có giám sát khác gì?

Nếu có đủ fraud label đáng tin cậy, supervised classification thường mạnh hơn một anomaly detector không giám sát.

Anomaly Detection hữu ích hơn khi label rất ít, cần phát hiện kiểu tấn công mới, hành vi bình thường dễ mô hình hóa hơn hành vi xấu hoặc định nghĩa anomaly thay đổi theo thời gian.

Hệ production thường kết hợp nhiều tầng:

```text
supervised risk model
+ business rules
+ anomaly score
+ human review
```

## Chọn threshold

Anomaly algorithm thường trả một score `s(x)`, còn hệ thống cảnh báo cần threshold.

Threshold quyết định sự đánh đổi:

```text
threshold thấp → nhiều alert hơn → recall cao hơn, false positive nhiều hơn
threshold cao → ít alert hơn → tải vận hành thấp hơn, bỏ sót nhiều hơn
```

Nếu đội review chỉ xử lý được 500 case mỗi ngày, capacity chính là một ràng buộc thật.

Threshold phải gắn với ngân sách cảnh báo và tổn thất kỳ vọng, không chỉ với metric offline.

## Mất cân bằng cực mạnh và Precision–Recall

Trong bài toán anomaly, positive thường rất hiếm nên ROC-AUC có thể nhìn rất đẹp dù số false positive tuyệt đối vẫn quá lớn.

Precision–Recall curve thường cung cấp thông tin thực dụng hơn.

Ví dụ có 1 triệu giao dịch và chỉ 100 fraud. False-positive rate 1% vẫn tạo khoảng 10.000 cảnh báo sai — gần như không thể vận hành dù specificity 99% nghe rất cao.

## Concept Drift

“Bình thường” hôm nay có thể không còn bình thường sau product launch, thay đổi mùa hoặc khi attacker thay chiến thuật.

Hệ Anomaly Detection cần theo dõi distribution của score, tỷ lệ alert và outcome đã xác minh.

Threshold tĩnh rất dễ xuống cấp theo thời gian.

Trong fraud hoặc security, môi trường còn mang tính đối kháng: attacker có thể chủ động thích nghi với chính sách phát hiện.

## Phát hiện và tìm nguyên nhân là hai bài toán khác nhau

Anomaly score chỉ nói quan sát khác pattern kỳ vọng, không giải thích nguyên nhân.

Hệ thống vận hành còn cần các tín hiệu chẩn đoán như feature contribution, ví dụ bình thường gần nhất, rule bị vi phạm, timeline hoặc workflow điều tra.

**Phát hiện (detection)** và **phân tích nguyên nhân gốc (root-cause analysis)** là hai layer khác nhau.

## Mô hình tư duy

> Anomaly Detection = xây một mô hình về hành vi bình thường hoặc kỳ vọng, sau đó đo xem quan sát mới lệch khỏi mô hình đó tới mức nào trong đúng ngữ cảnh.

## Các hiểu lầm thường gặp

### “Anomaly chỉ đơn giản là điểm hiếm”

Không. Hành vi hiếm nhưng hợp lệ chưa chắc là anomaly; ngữ cảnh và hậu quả mới quyết định ý nghĩa.

### “Unsupervised Anomaly Detection không cần label”

Training có thể không dùng label, nhưng threshold, evaluation và tuning production vẫn rất cần outcome đã xác minh hoặc feedback từ domain expert.

### “Reconstruction error cao nghĩa chắc chắn fraud”

Không. Nó chỉ là một score độ lệch theo representation và autoencoder hiện tại.

### “Accuracy 99% là tốt cho Anomaly Detection”

Không. Với positive cực hiếm, accuracy gần như vô nghĩa nếu không nhìn confusion matrix, precision, recall và số alert thực tế.

## Liên kết kiến thức

Anomaly Detection nối [Xác suất](../01_mathematical_foundations/02_probability_for_ai.md), [k-NN](./07_knn_and_distance_based_learning.md), [Clustering](./11_clustering.md), [Đánh giá mô hình](./15_model_evaluation.md) và các phần sau về AI Security và Monitoring.