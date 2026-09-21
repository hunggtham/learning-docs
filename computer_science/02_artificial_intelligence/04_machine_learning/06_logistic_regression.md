# Logistic Regression: từ điểm tuyến tính tới xác suất phân loại

**Logistic Regression (로지스틱 회귀 / hồi quy logistic)** có tên chứa “regression” nhưng thường được dùng cho **phân loại (classification)**. Ý tưởng trung tâm rất đơn giản: trước hết tính một điểm tuyến tính (linear score), sau đó biến điểm đó thành đầu ra có thể diễn giải gần như xác suất bằng hàm sigmoid.

Mô hình này quan trọng vì nó tạo cây cầu trực tiếp giữa Đại số tuyến tính, Xác suất, Maximum Likelihood, Cross-Entropy và ranh giới quyết định (decision boundary). Nhiều classifier hiện đại vẫn dùng cùng cấu trúc ở layer đầu ra.

## Vì sao Linear Regression không phù hợp trực tiếp cho phân loại nhị phân?

Nếu target chỉ nhận `0` hoặc `1`, mô hình tuyến tính:

\[
\hat y=\mathbf w^T\mathbf x+b
\]

có thể trả `-3.2` hoặc `1.8`, nên không phù hợp để diễn giải trực tiếp như xác suất.

Ta cần một hàm ánh xạ toàn bộ trục số thực vào khoảng `(0,1)`.

Hàm sigmoid:

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

Khi `z=0`, xác suất bằng `0.5`. `z` càng dương thì xác suất tiến gần `1`; `z` càng âm thì tiến gần `0`.

## Odds và log-odds

Với xác suất `p`, odds được định nghĩa:

\[
\frac{p}{1-p}
\]

Log-odds, hay **logit**, là:

\[
\log\frac{p}{1-p}
\]

Logistic Regression giả định log-odds là một hàm tuyến tính của đầu vào:

\[
\log\frac{p}{1-p}=\mathbf w^T\mathbf x+b
\]

Đây là cách hiểu chính xác hơn câu “xác suất tuyến tính theo feature”. Xác suất không tuyến tính; chính log-odds mới tuyến tính.

Nếu `x_j` tăng một đơn vị và các feature khác giữ cố định, odds được nhân với:

\[
e^{w_j}
\]

Đây là cách thường dùng để diễn giải hệ số của Logistic Regression.

## Maximum Likelihood dẫn tới Binary Cross-Entropy

Với target Bernoulli:

\[
y\sim Bernoulli(p)
\]

likelihood của một mẫu là:

\[
P(y\mid x)=p^y(1-p)^{1-y}
\]

Log-likelihood:

\[
\log P(y\mid x)=y\log p+(1-y)\log(1-p)
\]

Tối đa hóa likelihood tương đương với tối thiểu hóa negative log-likelihood:

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

Đây chính là **binary cross-entropy**.

Vì vậy sigmoid và cross-entropy không phải hai “công thức tình cờ ghép lại”. Chúng xuất phát từ cùng một mô hình xác suất thống nhất.

## Ranh giới quyết định

Nếu threshold là `0.5`:

\[
\sigma(z)\ge0.5 \iff z\ge0
\]

Ranh giới quyết định là:

\[
\mathbf w^T\mathbf x+b=0
\]

Trong không gian hai chiều, đây là một đường thẳng; ở nhiều chiều hơn là một siêu phẳng (hyperplane).

Vì vậy Logistic Regression là bộ phân loại tuyến tính trong không gian feature hiện tại.

Nếu cần ranh giới phi tuyến, có thể thêm feature biến đổi hoặc dùng mô hình phi tuyến.

## Đầu ra xác suất không tự động được hiệu chuẩn

Logistic Regression thường có cách diễn giải xác suất khá tự nhiên khi mô hình được đặc tả phù hợp, nhưng vẫn phải kiểm tra **hiệu chuẩn (calibration)**.

Nếu mô hình nhiều lần dự đoán `p≈0.8`, một hệ được calibration tốt sẽ có khoảng 80% trường hợp trong nhóm đó thật sự positive.

Có thể đánh giá calibration bằng reliability diagram, Brier score hoặc Expected Calibration Error.

Một classifier có AUC cao nhưng calibration kém vẫn có thể gây vấn đề nếu hệ thống phía sau dùng score như xác suất rủi ro thực sự.

## Threshold không bắt buộc là 0.5

Xác suất dự đoán và hành động quyết định là hai tầng khác nhau.

Ví dụ trong fraud detection, false negative có thể tốn kém hơn false positive. Khi đó threshold có thể chọn `0.2` thay vì `0.5` để tăng recall.

Quy tắc quyết định tổng quát nên dựa trên chi phí kỳ vọng:

\[
Choose\ action\ a=\arg\min_a \mathbb E[Cost(a,Y)\mid x]
\]

Do đó threshold nên được chọn theo mục tiêu vận hành, không phải theo thói quen.

## Mất cân bằng lớp

Trong bài toán sự kiện hiếm, accuracy rất dễ gây hiểu nhầm.

Nếu positive rate chỉ `0.1%`, mô hình luôn đoán negative vẫn đạt `99.9%` accuracy.

Cần xem thêm precision, recall, PR-AUC, calibration và chi phí nghiệp vụ kỳ vọng.

Có thể dùng trọng số lớp trong loss:

\[
L=-[w_1y\log p+w_0(1-y)\log(1-p)]
\]

nhưng việc weighting cũng có thể làm thay đổi calibration. Nếu cần xác suất được hiệu chuẩn tốt, phải kiểm tra lại sau training.

## Regularization

Logistic Regression với L2 có hàm mục tiêu:

\[
J(\mathbf w)=\frac1n\sum_iL_i+\lambda\|\mathbf w\|_2^2
\]

L1 regularization có thể làm nhiều hệ số trở thành 0 và tạo nghiệm thưa.

Regularization đặc biệt hữu ích khi số chiều feature lớn hoặc các feature có tương quan mạnh.

## Phân loại nhiều lớp: Softmax Regression

Với `K` lớp, mô hình tạo logit:

\[
z_k=\mathbf w_k^T\mathbf x+b_k
\]

Softmax biến chúng thành phân phối xác suất:

\[
p(y=k\mid x)=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Cross-entropy:

\[
L=-\log p(y_{true}\mid x)
\]

Cách này còn được gọi là **multinomial logistic regression** hoặc **softmax regression**.

Trong neural network classifier, phần feature extractor có thể rất phức tạp nhưng layer cuối vẫn thường là linear logits + softmax.

## Ổn định số

Tính sigmoid trực tiếp bằng `e^{-z}` có thể overflow khi `z` rất âm. Softmax tính ngây thơ cũng có nguy cơ overflow khi logit lớn.

Implementation production thường dùng các công thức ổn định như log-sum-exp và primitive của framework như `BCEWithLogitsLoss` hoặc `CrossEntropyLoss`, thay vì tự gọi sigmoid rồi lấy log.

Ví dụ:

\[
\log\sum_i e^{z_i}
\]

được tính ổn định bằng:

\[
m+\log\sum_i e^{z_i-m},\quad m=\max_i z_i
\]

Đây là liên hệ trực tiếp với Tính toán số (Numerical Computation).

## Khả năng diễn giải và giới hạn

Hệ số của Logistic Regression tương đối dễ kiểm tra, nhưng “đọc được coefficient” không đồng nghĩa với diễn giải nhân quả.

Tương quan giữa feature, biến bị bỏ sót, cách lấy mẫu dữ liệu và phép biến đổi feature đều ảnh hưởng tới hệ số.

Nếu input đã được one-hot encoding hoặc standardization, ý nghĩa của hệ số cũng phụ thuộc chính cách biểu diễn đó.

## Liên hệ với Language Model

Layer đầu ra của language model tạo logit cho toàn bộ vocabulary, sau đó softmax biến logit thành phân phối token tiếp theo:

\[
p(token=k\mid context)=softmax(z)_k
\]

Cấu trúc toán học này rất gần với multiclass logistic regression ở quy mô lớn, trong đó biểu diễn ẩn `h` được Transformer tạo ra trước:

\[
z=W_{out}h+b
\]

Vì vậy Logistic Regression không phải một thuật toán “cũ và không liên quan tới LLM”; nguyên lý của nó vẫn nằm ngay trong output distribution của mô hình hiện đại.

## Mô hình tư duy

```text
Feature
   ↓
Điểm tuyến tính / logit
   ↓
Sigmoid / Softmax
   ↓
Phân phối xác suất
   ↓
Threshold / chính sách quyết định
```

Luôn tách hai câu hỏi: mô hình đang ước lượng xác suất gì, và hệ thống sẽ dùng xác suất đó để ra hành động như thế nào.

## Các hiểu lầm thường gặp

### “Sigmoid trả 0.9 nghĩa là chắc chắn 90% đúng”

Không. Chỉ có thể diễn giải như vậy khi mô hình đã được calibration tốt trên distribution liên quan.

### “Threshold phải là 0.5”

Không. Threshold phụ thuộc chi phí, tỷ lệ lớp và ràng buộc vận hành.

### “Logistic Regression không dùng được feature phi tuyến”

Sai. Có thể thêm polynomial feature hoặc interaction; ranh giới chỉ tuyến tính trong **không gian feature đã biến đổi**.

### “Softmax probability là confidence tuyệt đối”

Không. Softmax chỉ chuẩn hóa logit. Neural network vẫn có thể overconfident, đặc biệt khi distribution shift.

## Liên kết kiến thức

Xem lại [Hàm mất mát, hàm mục tiêu và rủi ro](./04_loss_objective_and_risk.md), [Xác suất cho AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Lý thuyết thông tin](../01_mathematical_foundations/05_information_theory.md).

Xem tiếp: [Đánh giá mô hình](./15_model_evaluation.md) để hiểu ROC, PR curve, calibration và lựa chọn threshold.