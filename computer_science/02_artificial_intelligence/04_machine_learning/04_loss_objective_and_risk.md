# Loss, Objective và Risk trong Machine Learning

Machine Learning không học một cách mơ hồ. Muốn model thay đổi parameters theo hướng có ích, ta cần biến câu hỏi “model đang làm tốt đến đâu?” thành một đại lượng có thể tính được. Từ đây xuất hiện ba concept dễ bị trộn lẫn: **loss function (손실 함수 / hàm mất mát)**, **objective function (목적 함수 / hàm mục tiêu)** và **risk (위험 / rủi ro kỳ vọng)**.

Một prediction có thể đúng hoặc sai theo rất nhiều mức độ. Loss là cách ta gán một con số cho sai lệch đó. Nhưng loss trên từng sample chưa phải mục tiêu cuối cùng; model cần hoạt động tốt trên distribution thực tế, không chỉ trên training data. Vì vậy statistical learning theory đưa ta từ loss cục bộ tới empirical risk và expected risk.

## Từ prediction tới measurable error

Giả sử model nhận input `x`, tạo prediction:

\[
\hat{y}=f_\theta(x)
\]

và ground truth là `y`. Loss function:

\[
L(y,\hat{y})
\]

đo mức độ prediction không phù hợp target theo một tiêu chí cụ thể.

Điểm quan trọng là loss **không phải “sai số tự nhiên tồn tại sẵn trong thế giới”**. Nó là một thiết kế. Chọn loss nào tức là ta quyết định kiểu sai nào đáng bị phạt mạnh hơn.

Ví dụ regression có thể dùng Mean Squared Error:

\[
L=(y-\hat y)^2
\]

Sai số lớn bị bình phương nên bị phạt rất mạnh. Nếu dữ liệu có outlier, MSE có thể khiến optimizer dành nhiều effort cho một số điểm cực đoan.

Mean Absolute Error:

\[
L=|y-\hat y|
\]

ít nhạy với outlier hơn. Chỉ khác loss function, behavior học được đã có thể thay đổi rõ rệt.

## Loss và probabilistic modeling

Nhiều loss không phải công thức arbitrary mà xuất phát từ statistical assumptions.

Nếu giả định regression noise là Gaussian:

\[
y=f_\theta(x)+\epsilon,\qquad \epsilon\sim\mathcal N(0,\sigma^2)
\]

thì maximizing likelihood tương đương minimizing squared error, bỏ qua constant.

Điều này cho insight quan trọng:

> Chọn loss thường tương đương chọn một assumption về data-generating process.

Với classification, cross-entropy loss xuất hiện tự nhiên từ negative log-likelihood.

Nếu target class là `y` và model output distribution `p_\theta(y\mid x)`, loss:

\[
L=-\log p_\theta(y\mid x)
\]

phạt model rất mạnh khi nó gán xác suất thấp cho đáp án đúng.

Đây là nền trực tiếp của language-model training: next-token prediction thường minimize token-level negative log-likelihood.

## Từ sample loss tới empirical risk

Training dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Empirical risk:

\[
\hat R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(y_i,f_\theta(x_i))
\]

là average loss trên observed sample.

**Empirical Risk Minimization (ERM / 경험적 위험 최소화)** chọn parameters:

\[
\hat\theta=\arg\min_\theta \hat R(\theta)
\]

Đây là abstraction đứng sau rất nhiều supervised-learning algorithms.

Nhưng mục tiêu thực không phải làm dataset lịch sử hài lòng. Ta muốn tốt trên future examples từ distribution `P(X,Y)`:

\[
R(\theta)=\mathbb E_{(x,y)\sim P}[L(y,f_\theta(x))]
\]

Đây là **expected risk / population risk**. Vì không biết distribution thật, ta dùng empirical risk như estimator.

Khoảng cách giữa hai thứ này chính là trung tâm của generalization.

## Objective function rộng hơn loss

Trong thực tế objective thường có thêm regularization:

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

`Ω(θ)` có thể penalize model complexity hoặc parameter magnitude.

Ví dụ L2 regularization:

\[
\Omega(\theta)=\|\theta\|_2^2
\]

khuyến khích weight nhỏ hơn.

L1 regularization:

\[
\Omega(\theta)=\|\theta\|_1
\]

có xu hướng tạo sparse parameters.

Objective còn có thể chứa nhiều term:

\[
J=J_{task}+\alpha J_{aux}+\beta J_{constraint}
\]

Trong modern AI, multi-task learning, representation learning và alignment thường dùng objective composed như vậy.

## Surrogate loss: optimize thứ dễ tính để đạt mục tiêu khó hơn

Nhiều business metric hoặc task metric không differentiable.

Accuracy chứa discrete `argmax`, nên gradient không hữu ích trực tiếp. Ta thường train bằng cross-entropy rồi evaluate bằng accuracy/F1/AUC.

Cross-entropy lúc này là **surrogate loss**: objective có mathematical properties thuận lợi để optimization, hy vọng cải thiện metric ta thực sự quan tâm.

Từ đây có một distinction quan trọng:

```text
Training objective != Evaluation metric != Business objective
```

Ví dụ fraud model có thể optimize log loss, được evaluate bằng precision/recall, nhưng business thật quan tâm money saved, investigation cost và customer friction.

Production ML thất bại nhiều khi không phải vì optimizer yếu, mà vì ba tầng objective này không aligned.

## Class imbalance và asymmetric cost

Nếu 99.9% transactions bình thường, model đoán luôn “normal” có accuracy rất cao nhưng vô dụng.

Loss cần phản ánh asymmetric consequences. Weighted cross-entropy:

\[
L=-w_y\log p(y\mid x)
\]

cho phép rare class có influence lớn hơn.

Một hướng khác là resampling, focal loss hoặc decision threshold dựa trên cost.

Quan trọng: **loss weighting và thresholding giải quyết các tầng khác nhau**. Weight thay learning dynamics; threshold thay decision rule sau khi model tạo score.

## Hinge loss và margin

Support Vector Machine dùng hinge loss:

\[
L=\max(0,1-yf(x))
\]

với `y∈{-1,+1}`.

Không chỉ yêu cầu prediction đúng sign, hinge loss còn muốn point nằm ngoài margin. Điều này đưa geometric principle trực tiếp vào objective.

Xem thêm: [Support Vector Machines](./10_support_vector_machines.md).

## Robust losses

Nếu MSE quá nhạy outlier nhưng MAE khó optimize mượt tại zero, Huber loss kết hợp hai behavior:

\[
L_\delta(a)=
\begin{cases}
\frac12a^2,& |a|\le\delta\\
\delta(|a|-\frac12\delta),& |a|>\delta
\end{cases}
\]

Error nhỏ dùng quadratic behavior; error lớn chuyển sang linear.

Đây là ví dụ điển hình của engineering trade-off giữa statistical robustness và optimization properties.

## Multi-objective optimization trong AI system

Một recommender không chỉ cần engagement. Nếu chỉ optimize click, system có thể học clickbait. Objective thực tế có thể phải balance retention, diversity, fairness, latency và safety.

Một LLM system cũng tương tự. Quality, factuality, helpfulness, latency, token cost và safety có thể xung đột.

Không phải mọi trade-off đều nên nhét vào một scalar loss. Có trường hợp cần hard constraint, policy layer hoặc multi-stage system.

## Objective misspecification

Optimizer thực hiện đúng điều objective yêu cầu, không phải điều con người “thực sự muốn nhưng không encode”.

Nếu reward proxy có loophole, model có thể exploit proxy. Đây là một dạng **Goodhart's Law**: khi measure trở thành target, measure có thể mất khả năng phản ánh goal ban đầu.

Connection này nối supervised ML với Reinforcement Learning và AI Safety.

## Mental Model

Hãy nhìn learning theo chuỗi:

```text
Real goal
   ↓ approximation
Evaluation metric
   ↓ optimization-friendly proxy
Training objective
   ↓ sample-level signal
Loss
   ↓ gradients / algorithm
Parameter update
```

Mỗi mũi tên là nơi mismatch có thể xuất hiện.

## Common Misconceptions

### “Loss thấp nghĩa model tốt”

Chỉ đúng nếu nói rõ loss nào và trên distribution nào. Training loss thấp có thể đi cùng severe overfitting.

### “Cross-entropy và accuracy là hai cách đo giống nhau”

Accuracy chỉ quan tâm predicted class cuối cùng; cross-entropy còn nhạy với probability assigned. Một model đúng nhưng cực kỳ uncertain và một model đúng với probability 0.999 có cùng accuracy nhưng loss khác mạnh.

### “Regularization chỉ là mẹo chống overfitting”

Regularization encode preference/inductive bias về solution. Nó thay optimization landscape và hypothesis được ưu tiên.

### “Nếu objective đúng thì production behavior chắc chắn đúng”

Không. Distribution shift, data pipeline lỗi, calibration, threshold, system interaction và user feedback đều có thể làm behavior khác training assumptions.

## Knowledge Connection

Loss nối Probability, Information Theory và Optimization. Risk nối Statistics với generalization. Objective nối mathematical training với product design và AI Safety.

Xem tiếp: [Linear Regression](./05_linear_regression.md), [Logistic Regression](./06_logistic_regression.md), [Bias, Variance and Generalization](./14_bias_variance_and_generalization.md) và [Model Evaluation](./15_model_evaluation.md).