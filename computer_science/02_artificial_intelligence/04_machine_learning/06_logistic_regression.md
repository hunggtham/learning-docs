# Logistic Regression: từ tuyến tính (linear / 선형) score tới xác suất phân loại

> **Mạch đọc:** Đặt **Logistic Regression: từ tuyến tính (linear / 선형) score tới xác suất phân loại** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Tại sao tuyến tính (linear / 선형) Regression không phù hợp trực tiếp cho nhị phân (binary / 이진) classification?** sang **Odds và log-odds**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Logistic Regression (로지스틱 회귀 / hồi quy logistic) có tên chứa “regression” nhưng thường được dùng cho **classification**. Ý tưởng trung tâm rất đơn giản: trước hết tính một tuyến tính (linear / 선형) score, sau đó biến score đó thành probability-like đầu ra (output / 출력) bằng sigmoid.

Mô hình (model / 모델) này quan trọng vì nó tạo cây cầu trực tiếp giữa tuyến tính (linear / 선형) Algebra, xác suất (probability / 확률), Maximum Likelihood, Cross-Entropy và quyết định (decision / 결정) ranh giới (boundary / 경계). Nhiều classifier hiện đại vẫn dùng cùng lô-gic (logic / 논리) ở đầu ra (output / 출력) tầng (layer / 계층).

## Tại sao tuyến tính (linear / 선형) Regression không phù hợp trực tiếp cho nhị phân (binary / 이진) classification?

Nếu mục tiêu (target / 대상) chỉ nhận `0` hoặc `1`, mô hình tuyến tính (linear model / 선형 모델):

\[
\hat y=\mathbf w^T\mathbf x+b
\]

có thể đầu ra (output / 출력) `-3.2` hoặc `1.8`, không phù hợp để interpret như xác suất (probability / 확률).

Ta cần một hàm (function / 함수) map real line vào `(0,1)`.

Sigmoid:

\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]

với:

\[
z=\mathbf w^T\mathbf x+b
\]

cho:

\[
p(y=1\mid x)=\sigma(z)
\]

Khi `z=0`, xác suất (probability / 확률) là `0.5`. `z` càng dương thì xác suất (probability / 확률) tiến về `1`; càng âm thì tiến về `0`.

## Odds và log-odds

Xác suất (probability / 확률) `p` có odds:

\[
\frac{p}{1-p}
\]

Log-odds hoặc **logit**:

\[
\log\frac{p}{1-p}
\]

Logistic Regression assume log-odds là tuyến tính (linear / 선형) hàm (function / 함수) của đầu vào (input / 입력):

\[
\log\frac{p}{1-p}=\mathbf w^T\mathbf x+b
\]

Đây là interpretation chính xác hơn câu “xác suất (probability / 확률) tuyến tính theo tính năng (feature / 기능)”. xác suất (probability / 확률) không tuyến tính; log-odds mới tuyến tính (linear / 선형).

Nếu coefficient `w_j` tăng một đơn vị trong `x_j`, odds được nhân với:

\[
e^{w_j}
\]

khi giữ tính năng (feature / 기능) khác cố định.

## Maximum Likelihood dẫn tới nhị phân (binary / 이진) Cross-Entropy

Với Bernoulli mục tiêu (target / 대상):

\[
y\sim Bernoulli(p)
\]

likelihood của một mẫu (sample / 표본):

\[
P(y\mid x)=p^y(1-p)^{1-y}
\]

Log-likelihood:

\[
\log P(y\mid x)=y\log p+(1-y)\log(1-p)
\]

Maximize likelihood tương đương minimize negative log-likelihood:

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

Đây chính là **nhị phân (binary / 이진) cross-entropy**.

Vì vậy sigmoid và cross-entropy không phải hai recipe vô tình ghép với nhau. Chúng xuất phát từ một probabilistic mô hình (model / 모델) thống nhất.

## Quyết định (decision / 결정) ranh giới (boundary / 경계)

Nếu threshold là `0.5`:

\[
\sigma(z)\ge0.5 \iff z\ge0
\]

Quyết định (decision / 결정) ranh giới (boundary / 경계):

\[
\mathbf w^T\mathbf x+b=0
\]

Trong 2D, đây là đường thẳng; trong higher dimension là hyperplane.

Logistic Regression vì vậy là tuyến tính (linear / 선형) classifier trong original tính năng (feature / 기능) không gian (space / 공간).

Nếu cần nonlinear ranh giới (boundary / 경계), có thể thêm transformed features hoặc dùng nonlinear mô hình (model / 모델).

## Xác suất (probability / 확률) đầu ra (output / 출력) không tự động calibrated

Logistic Regression thường có xác suất (probability / 확률) interpretation tốt khi mô hình (model / 모델) specification phù hợp, nhưng calibration vẫn phải kiểm tra.

Nếu mô hình (model / 모델) nói `p≈0.8` cho nhiều samples, ideally khoảng 80% trong nhóm đó positive.

Calibration có thể đánh giá bằng độ tin cậy (reliability / 신뢰성) diagram, Brier score hoặc expected calibration lỗi (error / 오류).

Một classifier có AUC cao nhưng calibration kém vẫn có thể gây bài toán (problem / 문제) nếu downstream hệ thống (system / 시스템) dùng score như rủi ro (risk / 위험) xác suất (probability / 확률).

## Threshold không phải luôn 0.5

Prediction xác suất (probability / 확률) và quyết định (decision / 결정) hành động (action / 동작) là hai tầng khác nhau.

Giả sử fraud detection: false negative có chi phí (cost / 비용) lớn hơn false positive. Threshold có thể chọn `0.2` thay vì `0.5` để tăng recall.

Quyết định (decision / 결정) quy tắc (rule / 규칙) tổng quát nên dựa vào expected chi phí (cost / 비용):

\[
Choose\ hành động (action / 동작)\ a=\arg\min_a \mathbb E[chi phí (cost / 비용)(a,Y)\mid x]
\]

Do đó threshold phải được chọn theo operational mục tiêu (objective / 목표), không theo convention.

## Lớp (class / 클래스) imbalance

Trong rare-event classification, accuracy dễ misleading.

Nếu positive tỷ lệ (rate / 비율) `0.1%`, mô hình (model / 모델) luôn predict negative đã đạt `99.9%` accuracy.

Ta cần nhìn precision, recall, PR-AUC, calibration và expected nghiệp vụ (business / 비즈니스) chi phí (cost / 비용).

Lớp (class / 클래스) weighting có thể thay mất mát (loss / 손실):

\[
L=-[w_1y\log p+w_0(1-y)\log(1-p)]
\]

nhưng weighting cũng có thể thay xác suất (probability / 확률) calibration. Nếu cần calibrated xác suất (probability / 확률), phải đánh giá lại sau huấn luyện (training / 학습).

## Regularization

L2-regularized logistic regression:

\[
J(\mathbf w)=\frac1n\sum_iL_i+\lambda\|\mathbf w\|_2^2
\]

L1 regularization có thể tạo sparse coefficients.

Regularization đặc biệt hữu ích khi tính năng (feature / 기능) dimension lớn hoặc features correlated.

## Multiclass: Softmax Regression

Với `K` classes, mô hình (model / 모델) tạo logits:

\[
z_k=\mathbf w_k^T\mathbf x+b_k
\]

Softmax:

\[
p(y=k\mid x)=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Cross-entropy:

\[
L=-\log p(y_{true}\mid x)
\]

Đây còn được gọi là multinomial logistic regression hoặc softmax regression.

Neural mạng (network / 네트워크) classifier thường chỉ thay phần tính năng (feature / 기능) extractor; cuối cùng vẫn có tuyến tính (linear / 선형) logits + softmax.

## Numerical stability

Tính sigmoid naive với `e^{-z}` có thể overflow khi `z` rất âm. Softmax naive cũng có overflow.

Hiện thực (implementation / 구현) môi trường vận hành (production / 운영 환경) dùng stable formulations như log-sum-exp và khung phần mềm (framework / 프레임워크) primitives (`BCEWithLogitsLoss`, `CrossEntropyLoss`) thay vì tự sigmoid rồi log.

Ví dụ mathematically:

\[
\log\sum_i e^{z_i}
\]

được tính ổn định bằng:

\[
m+\log\sum_i e^{z_i-m},\quad m=\max_i z_i
\]

Đây là liên kết (connection / 연결) trực tiếp tới Numerical Computation.

## Interpretability và giới hạn

Coefficients tương đối dễ inspect, nhưng “dễ đọc coefficient” không đồng nghĩa nhân quả (causal / 인과적) interpretability.

Tính năng (feature / 기능) correlation, omitted variables, dữ liệu (data / 데이터) selection và transformations đều ảnh hưởng coefficients.

Nếu đầu vào (input / 입력) là one-hot categories hoặc standardized features, coefficient meaning cũng phụ thuộc biểu diễn (representation / 표현).

## Liên kết (connection / 연결) tới ngôn ngữ (language / 언어) các mô hình (models / 모델들)

Ngôn ngữ (language / 언어) mô hình (model / 모델) đầu ra (output / 출력) tầng (layer / 계층) tạo logits cho vocabulary, sau đó softmax tạo next-token phân phối (distribution / 분포):

\[
p(token=k\mid context)=softmax(z)_k
\]

Cấu trúc mathematical này là multiclass logistic regression ở quy mô rất lớn, trong đó hidden biểu diễn (representation / 표현) `h` được Deep Neural mạng (network / 네트워크)/Transformer tạo ra trước:

\[
z=W_{out}h+b
\]

Vì vậy Logistic Regression không phải “thuật toán (algorithm / 알고리즘) cũ không liên quan LLM”; nó là building khối (block / 블록) còn hiện diện ở đầu ra (output / 출력) phân phối (distribution / 분포).

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Features
   ↓
Linear score (logit)
   ↓
Sigmoid / Softmax
   ↓
Probability distribution
   ↓
Threshold / decision policy
```

Hãy giữ tách hai câu hỏi: mô hình (model / 모델) ước lượng xác suất (probability / 확률) gì, và hệ thống (system / 시스템) dùng xác suất (probability / 확률) đó để ra quyết định thế nào.

## Dùng chung (common / 공통) Misconceptions

### “Sigmoid đầu ra (output / 출력) 0.9 nghĩa chắc chắn 90% đúng”

Chỉ khi mô hình (model / 모델) calibrated trên relevant phân phối (distribution / 분포).

### “Threshold phải là 0.5”

Không. Threshold phụ thuộc chi phí (cost / 비용), lớp (class / 클래스) prevalence và operational các ràng buộc (constraints / 제약조건들).

### “Logistic Regression không dùng được nonlinear tính năng (feature / 기능)”

Có thể dùng polynomial/tương tác (interaction / 상호작용)/engineered features; quyết định (decision / 결정) ranh giới (boundary / 경계) chỉ tuyến tính (linear / 선형) trong transformed tính năng (feature / 기능) không gian (space / 공간).

### “Softmax xác suất (probability / 확률) là confidence tuyệt đối của mô hình (model / 모델)”

Softmax chỉ normalize logits. Neural mạng (network / 네트워크) có thể overconfident, đặc biệt under phân phối (distribution / 분포) shift.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem lại [Loss, Objective and Risk](./04_loss_objective_and_risk.md), [Probability for AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Information Theory](../01_mathematical_foundations/05_information_theory.md).

Xem tiếp: [Model Evaluation](./15_model_evaluation.md) để hiểu ROC, PR curve, calibration và threshold selection.
