# Anomaly Detection: khi điều quan trọng là những gì hiếm hoặc khác thường

> **Mạch đọc:** Đặt **Anomaly Detection: khi điều quan trọng là những gì hiếm hoặc khác thường** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Anomaly không đồng nghĩa outlier thống kê** sang **Statistical anomaly detection**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Anomaly Detection (이상 탐지 / phát hiện bất thường) tìm observations khác đáng kể so với hành vi (behavior / 동작) được xem là bình thường. Fraud giao dịch (transaction / 트랜잭션), mạng (network / 네트워크) intrusion, defective sensor, unusual login và manufacturing defect đều có thể được phrased như anomaly problems.

Khó khăn cốt lõi là **anomaly thường hiếm, thay đổi theo ngữ cảnh (context / 맥락) và đôi khi chưa từng xuất hiện trong labeled dữ liệu huấn luyện (training data / 학습 데이터)**. Vì vậy anomaly detection không chỉ là nhị phân (binary / 이진) classification với lớp (class / 클래스) imbalance; nhiều trường hợp ta phải học “normality” trước rồi đo deviation.

## Anomaly không đồng nghĩa outlier thống kê

Một điểm (point / 지점) xa mean có thể là statistical outlier nhưng hoàn toàn hợp lệ trong lĩnh vực (domain / 도메인). Ngược lại, một fraud giao dịch (transaction / 트랜잭션) có amount bình thường nhưng bất thường vì thời gian (time / 시간)/thiết bị (device / 장치)/location combination.

Anomaly luôn phụ thuộc ngữ cảnh (context / 맥락) và biểu diễn (representation / 표현).

Ba loại thường gặp:

- **điểm (point / 지점) anomaly**: observation riêng lẻ khác thường.
- **Contextual anomaly**: chỉ bất thường trong ngữ cảnh (context / 맥락), ví dụ login 3AM từ country mới.
- **Collective anomaly**: từng điểm (point / 지점) bình thường nhưng chuỗi (sequence / 시퀀스)/mẫu (pattern / 패턴) cả nhóm bất thường.

## Statistical anomaly detection

Nếu assume normal dữ liệu (data / 데이터) theo Gaussian:

\[
x\sim\mathcal N(\mu,\Sigma)
\]

có thể dùng likelihood/density. điểm (point / 지점) có:

\[
p(x)<\epsilon
\]

được flag.

Mahalanobis distance:

\[
d_M(x)=\sqrt{(x-\mu)^T\Sigma^{-1}(x-\mu)}
\]

account correlations và tính năng (feature / 기능) quy mô (scale / 규모) tốt hơn Euclidean distance.

Nhưng Gaussian giả định (assumption / 가정) có thể sai nghiêm trọng với multimodal/nonlinear dữ liệu (data / 데이터).

## z-score và robust statistics

Univariate quy tắc (rule / 규칙) đơn giản:

\[
z=\frac{x-\mu}{\sigma}
\]

flag `|z|>3` chẳng hạn.

Nếu outliers làm mean/std bị distort, robust alternatives dùng median và MAD:

\[
MAD=median(|x_i-median(x)|)
\]

Quy tắc (rule / 규칙) threshold phải dựa vào operational false-positive tolerance, không chỉ convention `3σ`.

## Isolation Forest

Isolation Forest dựa trên idea: anomaly hiếm và khác nên dễ bị “isolate” bằng random splits hơn normal points.

Bản dựng (build / 빌드) random trees; đường dẫn (path / 경로) length từ gốc (root / 루트) tới isolated leaf ngắn hơn cho anomaly.

Ưu điểm:

- không cần density estimation tường minh (explicit / 명시적);
- quy mô (scale / 규모) khá tốt high-dimensional tabular dữ liệu (data / 데이터);
- ít giả định (assumption / 가정) phân phối (distribution / 분포).

Nhưng hiệu năng (performance / 성능) vẫn phụ thuộc biểu diễn (representation / 표현) và contamination/threshold selection.

## One-Class SVM

One-Class SVM học ranh giới (boundary / 경계) bao quanh region normal dữ liệu (data / 데이터) trong kernel tính năng (feature / 기능) không gian (space / 공간). Points ngoài region được xem anomaly.

Nó hữu ích cho moderate dataset nhưng kernel scaling và hyperparameter sensitivity cần lưu ý.

## Cục bộ (local / 로컬) Outlier Factor

LOF so cục bộ (local / 로컬) density của điểm (point / 지점) với densities neighbors. điểm (point / 지점) có density thấp hơn neighborhood đáng kể sẽ anomalous.

Điều này giúp khi dữ liệu (data / 데이터) có regions với toàn cục (global / 전역) densities khác nhau, nhưng nearest-neighbor issues và dimension cao vẫn tồn tại.

## Reconstruction-based detection

Autoencoder train trên mostly-normal dữ liệu (data / 데이터):

\[
x\rightarrow z\rightarrow\hat x
\]

Nếu normal patterns reconstruct tốt còn unusual patterns reconstruct kém, reconstruction lỗi (error / 오류):

\[
A(x)=\|x-\hat x\|
\]

có thể là anomaly score.

Nhưng high-capacity autoencoder đôi khi reconstruct anomaly cũng tốt. Reconstruction lỗi (error / 오류) không tự động là anomaly xác suất (probability / 확률).

## Time-Series Anomaly Detection

Thời gian (time / 시간) series cần mô hình (model / 모델) expected hành vi (behavior / 동작) theo trend, seasonality và temporal phụ thuộc (dependency / 의존성).

Residual approach:

\[
r_t=y_t-\hat y_t
\]

flag khi residual vượt threshold.

Một giá trị (value / 값) `100` có thể bình thường lúc peak hour nhưng abnormal lúc night. Contextual baseline vì vậy quan trọng.

Chuỗi (sequence / 시퀀스) anomalies có thể cần change-point detection, forecasting các mô hình (models / 모델들) hoặc state-space các mô hình (models / 모델들).

## Supervised Fraud Detection khác gì?

Nếu có đủ labeled fraud examples và labels reliable, supervised classification thường mạnh hơn unsupervised anomaly detector.

Anomaly methods hữu ích khi:

- labels rất ít;
- muốn detect novel attacks;
- normal hành vi (behavior / 동작) dễ mô hình (model / 모델) hơn anomalies;
- anomaly definition thay đổi.

Môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) thường hybrid: supervised rủi ro (risk / 위험) mô hình (model / 모델) + rules + anomaly score + human rà soát (review / 검토).

## Threshold selection

Anomaly algorithms thường đầu ra (output / 출력) score `s(x)`, còn alert cần threshold.

Threshold quyết định sự đánh đổi (trade-off / 트레이드오프):

```text
lower threshold → more alerts → higher recall, more false positives
higher threshold → fewer alerts → lower operational load, more misses
```

Nếu rà soát (review / 검토) nhóm (team / 팀) chỉ xử lý 500 cases/day, sức chứa (capacity / 용량) là ràng buộc (constraint / 제약조건) thật. Threshold tối ưu hóa (optimization / 최적화) cần tie với alert ngân sách (budget / 예산) và expected mất mát (loss / 손실).

## Extreme lớp (class / 클래스) imbalance và Precision-Recall

Anomaly tasks hiếm positive nên ROC-AUC có thể trông tốt dù false positives tuyệt đối quá nhiều.

Precision-Recall curve thường informative hơn.

Ví dụ 1 triệu transactions, 100 fraud. False-positive tỷ lệ (rate / 비율) 1% tạo ~10,000 false alerts — operationally unusable dù specificity 99% nghe rất cao.

## Concept Drift

“Normal” hôm nay có thể không còn normal sau sản phẩm (product / 제품) launch, season thay đổi (change / 변경) hoặc attacker adaptation.

Anomaly hệ thống (system / 시스템) cần monitoring score phân phối (distribution / 분포), alert tỷ lệ (rate / 비율) và confirmed outcomes. Static threshold dễ degrade.

Fraud/bảo mật (security / 보안) đặc biệt adversarial: attacker phản ứng với detection chính sách (policy / 정책).

## Nguyên nhân gốc (root cause / 근본 원인) vs Detection

Anomaly score chỉ nói observation khác expected mẫu (pattern / 패턴); nó không giải thích nguyên nhân.

Operational hệ thống (system / 시스템) cần diagnostics: tính năng (feature / 기능) contributions, nearest normal examples, violated rules, timeline ngữ cảnh (context / 맥락) hoặc downstream investigation workflow.

Detection và root-cause phân tích (analysis / 분석) là hai layers khác nhau.

## Mô hình tư duy (mental model / 사고 모델)

> Anomaly Detection = xây một mô hình (model / 모델) về “normal/expected hành vi (behavior / 동작)”, rồi đo mức observation mới deviates khỏi mô hình (model / 모델) đó dưới ngữ cảnh (context / 맥락) phù hợp.

## Dùng chung (common / 공통) Misconceptions

### “Anomaly là điểm hiếm”

Rare nhưng legitimate hành vi (behavior / 동작) không nhất thiết anomaly; ngữ cảnh (context / 맥락) và impact matter.

### “Unsupervised anomaly detection không cần labels”

Huấn luyện (training / 학습) có thể không cần labels, nhưng threshold/evaluation/môi trường vận hành (production / 운영 환경) tuning vẫn rất cần confirmed outcomes hoặc lĩnh vực (domain / 도메인) phản hồi (feedback / 피드백).

### “Reconstruction lỗi (error / 오류) cao nghĩa chắc chắn fraud”

Nó chỉ là deviation score theo autoencoder biểu diễn (representation / 표현).

### “99% accuracy là tốt trong anomaly detection”

Với rare positives, accuracy gần như vô nghĩa nếu không nhìn confusion ma trận (matrix / 행렬), precision, recall và alert volume.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Anomaly Detection nối [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [k-NN](./07_knn_and_distance_based_learning.md), [Clustering](./11_clustering.md), [Model Evaluation](./15_model_evaluation.md) và sau này AI bảo mật (security / 보안)/Monitoring.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 what is machine learning](./00_what_is_machine_learning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
