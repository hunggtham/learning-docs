# Hàm mất mát, hàm mục tiêu và rủi ro trong Machine Learning

Machine Learning không thể “học” theo một ý niệm mơ hồ. Muốn mô hình thay đổi tham số theo hướng hữu ích, ta phải biến câu hỏi “mô hình đang làm tốt đến đâu?” thành một đại lượng có thể tính được. Từ đây xuất hiện ba khái niệm rất dễ bị trộn lẫn: **hàm mất mát (loss function / 손실 함수)**, **hàm mục tiêu (objective function / 목적 함수)** và **rủi ro kỳ vọng (risk / 위험)**.

Một dự đoán có thể sai ở nhiều mức độ khác nhau. Hàm mất mát gán một con số cho mức sai lệch đó. Tuy nhiên mất mát trên từng mẫu chưa phải mục tiêu cuối cùng; mô hình phải hoạt động tốt trên phân phối dữ liệu thực tế, không chỉ trên training data. Vì vậy lý thuyết học thống kê đi từ loss ở từng mẫu tới rủi ro thực nghiệm và rủi ro kỳ vọng.

## Từ dự đoán tới sai số có thể đo được

Giả sử mô hình nhận đầu vào `x`, tạo dự đoán:

\[
\hat{y}=f_\theta(x)
\]

và nhãn thật là `y`. Hàm mất mát:

\[
L(y,\hat{y})
\]

đo mức độ dự đoán không phù hợp với target theo một tiêu chí cụ thể.

Điểm quan trọng là loss **không phải một “sai số tự nhiên” tồn tại sẵn trong thế giới**. Nó là một lựa chọn thiết kế. Chọn loss nào đồng nghĩa với quyết định loại lỗi nào sẽ bị phạt mạnh hơn.

Ví dụ hồi quy có thể dùng Mean Squared Error:

\[
L=(y-\hat y)^2
\]

Sai số lớn bị bình phương nên bị phạt rất mạnh. Nếu dữ liệu có outlier, MSE có thể khiến optimizer dành nhiều sức để giảm lỗi ở một vài điểm cực đoan.

Mean Absolute Error:

\[
L=|y-\hat y|
\]

ít nhạy với outlier hơn. Chỉ thay loss function cũng có thể làm hành vi học được thay đổi đáng kể.

## Loss và mô hình xác suất

Nhiều hàm mất mát không phải công thức được chọn tùy ý mà xuất phát từ giả định thống kê.

Nếu giả định nhiễu hồi quy là Gaussian:

\[
y=f_\theta(x)+\epsilon,\qquad \epsilon\sim\mathcal N(0,\sigma^2)
\]

thì tối đa hóa likelihood tương đương với tối thiểu hóa squared error, bỏ qua các hằng số không ảnh hưởng tới nghiệm tối ưu.

Điều này dẫn tới một trực giác quan trọng:

> Chọn loss thường cũng đồng nghĩa với chọn một giả định về quá trình sinh dữ liệu (data-generating process).

Trong classification, cross-entropy xuất hiện tự nhiên từ negative log-likelihood.

Nếu lớp đúng là `y` và mô hình tạo phân phối:

\[
p_\theta(y\mid x)
\]

thì loss:

\[
L=-\log p_\theta(y\mid x)
\]

phạt rất mạnh khi mô hình gán xác suất thấp cho đáp án đúng.

Đây cũng là nền tảng trực tiếp của language-model training: dự đoán token tiếp theo thường tối ưu negative log-likelihood ở mức token.

## Từ loss từng mẫu tới rủi ro thực nghiệm

Với dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

rủi ro thực nghiệm (empirical risk) là:

\[
\hat R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(y_i,f_\theta(x_i))
\]

tức loss trung bình trên mẫu quan sát được.

**Empirical Risk Minimization (ERM / 경험적 위험 최소화)** chọn tham số:

\[
\hat\theta=\arg\min_\theta \hat R(\theta)
\]

Đây là abstraction đứng sau rất nhiều thuật toán supervised learning.

Tuy nhiên mục tiêu thật không phải làm dataset lịch sử “hài lòng”. Ta muốn mô hình hoạt động tốt trên dữ liệu tương lai lấy từ phân phối `P(X,Y)`:

\[
R(\theta)=\mathbb E_{(x,y)\sim P}[L(y,f_\theta(x))]
\]

Đây là **rủi ro kỳ vọng (expected risk / population risk)**.

Vì không biết toàn bộ phân phối thật, ta dùng empirical risk như một ước lượng. Khoảng cách giữa hai loại rủi ro chính là vấn đề trung tâm của generalization.

## Hàm mục tiêu rộng hơn loss

Trong thực tế, objective thường chứa thêm regularization:

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

`Ω(θ)` có thể phạt độ phức tạp hoặc độ lớn tham số.

Ví dụ L2 regularization:

\[
\Omega(\theta)=\|\theta\|_2^2
\]

khuyến khích trọng số nhỏ hơn.

L1 regularization:

\[
\Omega(\theta)=\|\theta\|_1
\]

thường tạo nghiệm thưa hơn trong nhiều bài toán.

Objective cũng có thể gồm nhiều thành phần:

\[
J=J_{task}+\alpha J_{aux}+\beta J_{constraint}
\]

Trong AI hiện đại, multi-task learning, representation learning và alignment thường dùng objective dạng kết hợp như vậy.

## Surrogate loss: tối ưu thứ dễ tính để phục vụ mục tiêu khó hơn

Nhiều metric nghiệp vụ hoặc task metric không khả vi.

Accuracy phụ thuộc vào `argmax`, nên không tạo gradient hữu ích trực tiếp. Vì vậy có thể train bằng cross-entropy nhưng đánh giá bằng accuracy, F1 hoặc AUC.

Cross-entropy khi đó đóng vai trò **hàm mất mát thay thế (surrogate loss)**: một mục tiêu có tính chất toán học thuận lợi để tối ưu, với kỳ vọng rằng cải thiện nó sẽ kéo theo metric thật tốt hơn.

Phải phân biệt ba tầng:

```text
Training objective ≠ Evaluation metric ≠ Business objective
```

Ví dụ một fraud model có thể tối ưu log loss, được đánh giá bằng precision/recall, nhưng mục tiêu doanh nghiệp thực tế lại là giảm số tiền mất do gian lận, giảm chi phí điều tra và hạn chế gây phiền cho khách hàng.

Rất nhiều thất bại production đến từ việc ba tầng mục tiêu này không khớp nhau, chứ không phải optimizer yếu.

## Mất cân bằng lớp và chi phí bất đối xứng

Nếu 99,9% giao dịch là bình thường, mô hình luôn dự đoán “normal” vẫn có accuracy cực cao nhưng hoàn toàn vô dụng.

Loss có thể cần phản ánh hậu quả bất đối xứng. Weighted cross-entropy:

\[
L=-w_y\log p(y\mid x)
\]

cho phép lớp hiếm có ảnh hưởng lớn hơn trong training.

Các hướng khác gồm resampling, focal loss hoặc lựa chọn threshold theo cost.

Điểm cần phân biệt: **loss weighting và thresholding giải quyết hai tầng khác nhau**. Weight thay đổi quá trình học; threshold thay đổi quyết định sau khi mô hình đã sinh score.

## Hinge loss và margin

Support Vector Machine dùng hinge loss:

\[
L=\max(0,1-yf(x))
\]

với `y∈{-1,+1}`.

Nó không chỉ yêu cầu phân loại đúng dấu mà còn muốn điểm dữ liệu nằm ngoài một margin đủ lớn. Điều này đưa một nguyên lý hình học trực tiếp vào objective.

Xem thêm: [Support Vector Machines](./10_support_vector_machines.md).

## Robust loss

Nếu MSE quá nhạy với outlier nhưng MAE lại không mượt tại 0, Huber loss kết hợp hai hành vi:

\[
L_\delta(a)=
\begin{cases}
\frac12a^2,& |a|\le\delta\\
\delta(|a|-\frac12\delta),& |a|>\delta
\end{cases}
\]

Sai số nhỏ dùng dạng bình phương; sai số lớn chuyển sang tăng tuyến tính.

Đây là ví dụ điển hình của sự đánh đổi giữa độ bền thống kê và tính thuận lợi cho tối ưu hóa.

## Tối ưu đa mục tiêu trong hệ AI

Một recommender không chỉ cần engagement. Nếu tối ưu click duy nhất, hệ thống có thể học cách đẩy nội dung giật gân.

Objective thực tế có thể phải cân bằng retention, diversity, fairness, latency và safety.

Một hệ LLM cũng tương tự: chất lượng, factuality, helpfulness, latency, token cost và safety có thể xung đột.

Không phải mọi trade-off đều nên ép vào một scalar loss. Có trường hợp nên dùng hard constraint, policy layer hoặc hệ nhiều tầng.

## Objective misspecification

Optimizer thực hiện đúng điều objective thưởng, không phải điều con người “thực sự muốn nhưng chưa mã hóa”.

Nếu proxy có lỗ hổng, mô hình có thể khai thác lỗ hổng đó.

Đây là một dạng trực giác của **Goodhart's Law**: khi một thước đo trở thành mục tiêu tối ưu, nó có thể mất khả năng đại diện cho mục tiêu ban đầu.

Điểm này nối supervised learning với Reinforcement Learning và AI Safety.

## Mô hình tư duy

Có thể nhìn quá trình học theo chuỗi:

```text
Mục tiêu ngoài đời thực
   ↓ xấp xỉ
Evaluation metric
   ↓ chọn proxy dễ tối ưu
Training objective
   ↓ tín hiệu ở từng sample
Loss
   ↓ gradient / thuật toán
Parameter update
```

Mỗi mũi tên là một vị trí có thể xuất hiện mismatch.

## Các hiểu lầm thường gặp

### “Loss thấp nghĩa là mô hình tốt”

Chỉ đúng khi nói rõ loss nào và trên distribution nào. Training loss thấp vẫn có thể đi cùng overfitting rất nặng.

### “Cross-entropy và accuracy chỉ là hai cách đo cùng một thứ”

Không. Accuracy chỉ quan tâm class cuối cùng; cross-entropy còn nhạy với xác suất mô hình gán cho đáp án đúng. Hai mô hình có cùng accuracy nhưng mức confidence rất khác có thể có cross-entropy khác rất lớn.

### “Regularization chỉ là mẹo chống overfitting”

Không. Regularization biểu diễn một preference hoặc inductive bias về loại nghiệm được ưu tiên và làm thay đổi cả optimization landscape.

### “Objective đúng thì production behavior chắc chắn đúng”

Không. Distribution shift, data pipeline lỗi, calibration, threshold, tương tác hệ thống và feedback loop đều có thể làm hành vi khác giả định trong training.

## Liên kết kiến thức

Loss nối Xác suất, Lý thuyết thông tin và Tối ưu hóa. Risk nối Thống kê với generalization. Objective nối quá trình training toán học với thiết kế sản phẩm và AI Safety.

Xem tiếp: [Linear Regression](./05_linear_regression.md), [Logistic Regression](./06_logistic_regression.md), [Bias, Variance and Generalization](./14_bias_variance_and_generalization.md) và [Model Evaluation](./15_model_evaluation.md).