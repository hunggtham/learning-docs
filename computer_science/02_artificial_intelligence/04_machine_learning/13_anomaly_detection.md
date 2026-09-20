# Anomaly Detection: khi điều quan trọng là những gì hiếm hoặc khác thường

Anomaly Detection (이상 탐지 / phát hiện bất thường) tìm observations khác đáng kể so với behavior được xem là bình thường. Fraud transaction, network intrusion, defective sensor, unusual login và manufacturing defect đều có thể được phrased như anomaly problems.

Khó khăn cốt lõi là **anomaly thường hiếm, thay đổi theo context và đôi khi chưa từng xuất hiện trong labeled training data**. Vì vậy anomaly detection không chỉ là binary classification với class imbalance; nhiều trường hợp ta phải học “normality” trước rồi đo deviation.

## Anomaly không đồng nghĩa outlier thống kê

Một point xa mean có thể là statistical outlier nhưng hoàn toàn hợp lệ trong domain. Ngược lại, một fraud transaction có amount bình thường nhưng bất thường vì time/device/location combination.

Anomaly luôn phụ thuộc context và representation.

Ba loại thường gặp:

- **Point anomaly**: observation riêng lẻ khác thường.
- **Contextual anomaly**: chỉ bất thường trong context, ví dụ login 3AM từ country mới.
- **Collective anomaly**: từng point bình thường nhưng sequence/pattern cả nhóm bất thường.

## Statistical anomaly detection

Nếu assume normal data theo Gaussian:

\[
x\sim\mathcal N(\mu,\Sigma)
\]

có thể dùng likelihood/density. Point có:

\[
p(x)<\epsilon
\]

được flag.

Mahalanobis distance:

\[
d_M(x)=\sqrt{(x-\mu)^T\Sigma^{-1}(x-\mu)}
\]

account correlations và feature scale tốt hơn Euclidean distance.

Nhưng Gaussian assumption có thể sai nghiêm trọng với multimodal/nonlinear data.

## z-score và robust statistics

Univariate rule đơn giản:

\[
z=\frac{x-\mu}{\sigma}
\]

flag `|z|>3` chẳng hạn.

Nếu outliers làm mean/std bị distort, robust alternatives dùng median và MAD:

\[
MAD=median(|x_i-median(x)|)
\]

Rule threshold phải dựa vào operational false-positive tolerance, không chỉ convention `3σ`.

## Isolation Forest

Isolation Forest dựa trên idea: anomaly hiếm và khác nên dễ bị “isolate” bằng random splits hơn normal points.

Build random trees; path length từ root tới isolated leaf ngắn hơn cho anomaly.

Ưu điểm:

- không cần density estimation explicit;
- scale khá tốt high-dimensional tabular data;
- ít assumption distribution.

Nhưng performance vẫn phụ thuộc representation và contamination/threshold selection.

## One-Class SVM

One-Class SVM học boundary bao quanh region normal data trong kernel feature space. Points ngoài region được xem anomaly.

Nó hữu ích cho moderate dataset nhưng kernel scaling và hyperparameter sensitivity cần lưu ý.

## Local Outlier Factor

LOF so local density của point với densities neighbors. Point có density thấp hơn neighborhood đáng kể sẽ anomalous.

Điều này giúp khi data có regions với global densities khác nhau, nhưng nearest-neighbor issues và dimension cao vẫn tồn tại.

## Reconstruction-based detection

Autoencoder train trên mostly-normal data:

\[
x\rightarrow z\rightarrow\hat x
\]

Nếu normal patterns reconstruct tốt còn unusual patterns reconstruct kém, reconstruction error:

\[
A(x)=\|x-\hat x\|
\]

có thể là anomaly score.

Nhưng high-capacity autoencoder đôi khi reconstruct anomaly cũng tốt. Reconstruction error không tự động là anomaly probability.

## Time-Series Anomaly Detection

Time series cần model expected behavior theo trend, seasonality và temporal dependency.

Residual approach:

\[
r_t=y_t-\hat y_t
\]

flag khi residual vượt threshold.

Một value `100` có thể bình thường lúc peak hour nhưng abnormal lúc night. Contextual baseline vì vậy quan trọng.

Sequence anomalies có thể cần change-point detection, forecasting models hoặc state-space models.

## Supervised Fraud Detection khác gì?

Nếu có đủ labeled fraud examples và labels reliable, supervised classification thường mạnh hơn unsupervised anomaly detector.

Anomaly methods hữu ích khi:

- labels rất ít;
- muốn detect novel attacks;
- normal behavior dễ model hơn anomalies;
- anomaly definition thay đổi.

Production system thường hybrid: supervised risk model + rules + anomaly score + human review.

## Threshold selection

Anomaly algorithms thường output score `s(x)`, còn alert cần threshold.

Threshold quyết định trade-off:

```text
lower threshold → more alerts → higher recall, more false positives
higher threshold → fewer alerts → lower operational load, more misses
```

Nếu review team chỉ xử lý 500 cases/day, capacity là constraint thật. Threshold optimization cần tie với alert budget và expected loss.

## Extreme class imbalance và Precision-Recall

Anomaly tasks hiếm positive nên ROC-AUC có thể trông tốt dù false positives tuyệt đối quá nhiều.

Precision-Recall curve thường informative hơn.

Ví dụ 1 triệu transactions, 100 fraud. False-positive rate 1% tạo ~10,000 false alerts — operationally unusable dù specificity 99% nghe rất cao.

## Concept Drift

“Normal” hôm nay có thể không còn normal sau product launch, season change hoặc attacker adaptation.

Anomaly system cần monitoring score distribution, alert rate và confirmed outcomes. Static threshold dễ degrade.

Fraud/security đặc biệt adversarial: attacker phản ứng với detection policy.

## Root Cause vs Detection

Anomaly score chỉ nói observation khác expected pattern; nó không giải thích nguyên nhân.

Operational system cần diagnostics: feature contributions, nearest normal examples, violated rules, timeline context hoặc downstream investigation workflow.

Detection và root-cause analysis là hai layers khác nhau.

## Mental Model

> Anomaly Detection = xây một model về “normal/expected behavior”, rồi đo mức observation mới deviates khỏi model đó dưới context phù hợp.

## Common Misconceptions

### “Anomaly là điểm hiếm”

Rare nhưng legitimate behavior không nhất thiết anomaly; context và impact matter.

### “Unsupervised anomaly detection không cần labels”

Training có thể không cần labels, nhưng threshold/evaluation/production tuning vẫn rất cần confirmed outcomes hoặc domain feedback.

### “Reconstruction error cao nghĩa chắc chắn fraud”

Nó chỉ là deviation score theo autoencoder representation.

### “99% accuracy là tốt trong anomaly detection”

Với rare positives, accuracy gần như vô nghĩa nếu không nhìn confusion matrix, precision, recall và alert volume.

## Knowledge Connection

Anomaly Detection nối [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [k-NN](./07_knn_and_distance_based_learning.md), [Clustering](./11_clustering.md), [Model Evaluation](./15_model_evaluation.md) và sau này AI Security/Monitoring.