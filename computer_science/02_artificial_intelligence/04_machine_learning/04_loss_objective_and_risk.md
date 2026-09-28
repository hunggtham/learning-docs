# Mất mát (loss / 손실), mục tiêu (objective / 목표) và rủi ro (risk / 위험) trong Machine học tập (learning / 학습)

> **Mạch đọc:** Đặt **mất mát (loss / 손실), mục tiêu (objective / 목표) và rủi ro (risk / 위험) trong Machine học tập (learning / 학습)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Từ prediction tới measurable lỗi (error / 오류)** sang **mất mát (loss / 손실) và probabilistic modeling**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Machine học tập (learning / 학습) không học một cách mơ hồ. Muốn mô hình (model / 모델) thay đổi parameters theo hướng có ích, ta cần biến câu hỏi “mô hình (model / 모델) đang làm tốt đến đâu?” thành một đại lượng có thể tính được. Từ đây xuất hiện ba concept dễ bị trộn lẫn: **hàm mất mát (loss function / 손실 함수)**, **mục tiêu (objective / 목표) hàm (function / 함수)** và **rủi ro (risk / 위험)**.

Một prediction có thể đúng hoặc sai theo rất nhiều mức độ. mất mát (loss / 손실) là cách ta gán một con số cho sai lệch đó. Nhưng mất mát (loss / 손실) trên từng mẫu (sample / 표본) chưa phải mục tiêu cuối cùng; mô hình (model / 모델) cần hoạt động tốt trên phân phối (distribution / 분포) thực tế, không chỉ trên dữ liệu huấn luyện (training data / 학습 데이터). Vì vậy statistical học tập (learning / 학습) lý thuyết (theory / 이론) đưa ta từ mất mát (loss / 손실) cục bộ tới empirical rủi ro (risk / 위험) và expected rủi ro (risk / 위험).

## Từ prediction tới measurable lỗi (error / 오류)

Giả sử mô hình (model / 모델) nhận đầu vào (input / 입력) `x`, tạo prediction:

\[
\hat{y}=f_\theta(x)
\]

và ground truth là `y`. hàm mất mát (loss function / 손실 함수):

\[
L(y,\hat{y})
\]

đo mức độ prediction không phù hợp mục tiêu (target / 대상) theo một tiêu chí cụ thể.

Điểm quan trọng là mất mát (loss / 손실) **không phải “sai số tự nhiên tồn tại sẵn trong thế giới”**. Nó là một thiết kế. Chọn mất mát (loss / 손실) nào tức là ta quyết định kiểu sai nào đáng bị phạt mạnh hơn.

Ví dụ regression có thể dùng Mean Squared lỗi (error / 오류):

\[
L=(y-\hat y)^2
\]

Sai số lớn bị bình phương nên bị phạt rất mạnh. Nếu dữ liệu có outlier, MSE có thể khiến optimizer dành nhiều effort cho một số điểm cực đoan.

Mean Absolute lỗi (error / 오류):

\[
L=|y-\hat y|
\]

ít nhạy với outlier hơn. Chỉ khác hàm mất mát (loss function / 손실 함수), hành vi (behavior / 동작) học được đã có thể thay đổi rõ rệt.

## Mất mát (loss / 손실) và probabilistic modeling

Nhiều mất mát (loss / 손실) không phải công thức arbitrary mà xuất phát từ statistical các giả định (assumptions / 가정들).

Nếu giả định regression noise là Gaussian:

\[
y=f_\theta(x)+\epsilon,\qquad \epsilon\sim\mathcal N(0,\sigma^2)
\]

thì maximizing likelihood tương đương minimizing squared lỗi (error / 오류), bỏ qua constant.

Điều này cho insight quan trọng:

> Chọn mất mát (loss / 손실) thường tương đương chọn một giả định (assumption / 가정) về data-generating tiến trình (process / 프로세스).

Với classification, cross-entropy mất mát (loss / 손실) xuất hiện tự nhiên từ negative log-likelihood.

Nếu mục tiêu (target / 대상) lớp (class / 클래스) là `y` và mô hình (model / 모델) đầu ra (output / 출력) phân phối (distribution / 분포) `p_\theta(y\mid x)`, mất mát (loss / 손실):

\[
L=-\log p_\theta(y\mid x)
\]

phạt mô hình (model / 모델) rất mạnh khi nó gán xác suất thấp cho đáp án đúng.

Đây là nền trực tiếp của language-model huấn luyện (training / 학습): next-token prediction thường minimize token-level negative log-likelihood.

## Từ mẫu (sample / 표본) mất mát (loss / 손실) tới empirical rủi ro (risk / 위험)

Huấn luyện (training / 학습) dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Empirical rủi ro (risk / 위험):

\[
\hat R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(y_i,f_\theta(x_i))
\]

là average mất mát (loss / 손실) trên observed mẫu (sample / 표본).

**Empirical rủi ro (risk / 위험) Minimization (ERM / 경험적 위험 최소화)** chọn parameters:

\[
\hat\theta=\arg\min_\theta \hat R(\theta)
\]

Đây là lớp trừu tượng (abstraction / 추상화) đứng sau rất nhiều supervised-learning algorithms.

Nhưng mục tiêu thực không phải làm dataset lịch sử hài lòng. Ta muốn tốt trên future examples từ phân phối (distribution / 분포) `P(X,Y)`:

\[
R(\theta)=\mathbb E_{(x,y)\sim P}[L(y,f_\theta(x))]
\]

Đây là **expected rủi ro (risk / 위험) / population rủi ro (risk / 위험)**. Vì không biết phân phối (distribution / 분포) thật, ta dùng empirical rủi ro (risk / 위험) như estimator.

Khoảng cách giữa hai thứ này chính là trung tâm của generalization.

## Mục tiêu (objective / 목표) hàm (function / 함수) rộng hơn mất mát (loss / 손실)

Trong thực tế mục tiêu (objective / 목표) thường có thêm regularization:

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

`Ω(θ)` có thể penalize mô hình (model / 모델) độ phức tạp (complexity / 복잡도) hoặc parameter magnitude.

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

Mục tiêu (objective / 목표) còn có thể chứa nhiều term:

\[
J=J_{tác vụ (task / 작업)}+\alpha J_{aux}+\beta J_{ràng buộc (constraint / 제약조건)}
\]

Trong hiện đại (modern / 현대적) AI, multi-task học tập (learning / 학습), biểu diễn (representation / 표현) học tập (learning / 학습) và alignment thường dùng mục tiêu (objective / 목표) composed như vậy.

## Surrogate mất mát (loss / 손실): optimize thứ dễ tính để đạt mục tiêu khó hơn

Nhiều nghiệp vụ (business / 비즈니스) chỉ số (metric / 지표) hoặc tác vụ (task / 작업) chỉ số (metric / 지표) không differentiable.

Accuracy chứa discrete `argmax`, nên độ dốc (gradient / 기울기) không hữu ích trực tiếp. Ta thường train bằng cross-entropy rồi evaluate bằng accuracy/F1/AUC.

Cross-entropy lúc này là **surrogate mất mát (loss / 손실)**: mục tiêu (objective / 목표) có mathematical properties thuận lợi để tối ưu hóa (optimization / 최적화), hy vọng cải thiện chỉ số (metric / 지표) ta thực sự quan tâm.

Từ đây có một distinction quan trọng:

```text
Training objective != Evaluation metric != Business objective
```

Ví dụ fraud mô hình (model / 모델) có thể optimize log mất mát (loss / 손실), được evaluate bằng precision/recall, nhưng nghiệp vụ (business / 비즈니스) thật quan tâm money saved, investigation chi phí (cost / 비용) và customer friction.

Môi trường vận hành (production / 운영 환경) ML thất bại nhiều khi không phải vì optimizer yếu, mà vì ba tầng mục tiêu (objective / 목표) này không aligned.

## Lớp (class / 클래스) imbalance và asymmetric chi phí (cost / 비용)

Nếu 99.9% transactions bình thường, mô hình (model / 모델) đoán luôn “normal” có accuracy rất cao nhưng vô dụng.

Mất mát (loss / 손실) cần phản ánh asymmetric consequences. Weighted cross-entropy:

\[
L=-w_y\log p(y\mid x)
\]

cho phép rare lớp (class / 클래스) có influence lớn hơn.

Một hướng khác là resampling, focal mất mát (loss / 손실) hoặc quyết định (decision / 결정) threshold dựa trên chi phí (cost / 비용).

Quan trọng: **mất mát (loss / 손실) weighting và thresholding giải quyết các tầng khác nhau**. Weight thay học tập (learning / 학습) dynamics; threshold thay quyết định (decision / 결정) quy tắc (rule / 규칙) sau khi mô hình (model / 모델) tạo score.

## Hinge mất mát (loss / 손실) và margin

Hỗ trợ (support / 지원) véc-tơ (vector / 벡터) Machine dùng hinge mất mát (loss / 손실):

\[
L=\max(0,1-yf(x))
\]

với `y∈{-1,+1}`.

Không chỉ yêu cầu prediction đúng sign, hinge mất mát (loss / 손실) còn muốn điểm (point / 지점) nằm ngoài margin. Điều này đưa geometric principle trực tiếp vào mục tiêu (objective / 목표).

Xem thêm: [Support Vector Machines](./10_support_vector_machines.md).

## Robust losses

Nếu MSE quá nhạy outlier nhưng MAE khó optimize mượt tại zero, Huber mất mát (loss / 손실) kết hợp hai hành vi (behavior / 동작):

\[
L_\delta(a)=
\begin{cases}
\frac12a^2,& |a|\le\delta\\
\delta(|a|-\frac12\delta),& |a|>\delta
\end{cases}
\]

Lỗi (error / 오류) nhỏ dùng quadratic hành vi (behavior / 동작); lỗi (error / 오류) lớn chuyển sang tuyến tính (linear / 선형).

Đây là ví dụ điển hình của kỹ thuật (engineering / 엔지니어링) sự đánh đổi (trade-off / 트레이드오프) giữa statistical robustness và tối ưu hóa (optimization / 최적화) properties.

## Multi-objective tối ưu hóa (optimization / 최적화) trong AI hệ thống (system / 시스템)

Một recommender không chỉ cần engagement. Nếu chỉ optimize click, hệ thống (system / 시스템) có thể học clickbait. mục tiêu (objective / 목표) thực tế có thể phải balance retention, diversity, fairness, độ trễ (latency / 지연 시간) và an toàn (safety / 안전).

Một LLM hệ thống (system / 시스템) cũng tương tự. chất lượng (quality / 품질), factuality, helpfulness, độ trễ (latency / 지연 시간), đơn vị từ (token / 토큰) chi phí (cost / 비용) và an toàn (safety / 안전) có thể xung đột.

Không phải mọi sự đánh đổi (trade-off / 트레이드오프) đều nên nhét vào một scalar mất mát (loss / 손실). Có trường hợp cần hard ràng buộc (constraint / 제약조건), chính sách (policy / 정책) tầng (layer / 계층) hoặc multi-stage hệ thống (system / 시스템).

## Mục tiêu (objective / 목표) misspecification

Optimizer thực hiện đúng điều mục tiêu (objective / 목표) yêu cầu, không phải điều con người “thực sự muốn nhưng không encode”.

Nếu reward proxy có loophole, mô hình (model / 모델) có thể exploit proxy. Đây là một dạng **Goodhart's Law**: khi measure trở thành mục tiêu (target / 대상), measure có thể mất khả năng phản ánh goal ban đầu.

Liên kết (connection / 연결) này nối supervised ML với Reinforcement học tập (learning / 학습) và AI an toàn (safety / 안전).

## Mô hình tư duy (mental model / 사고 모델)

Hãy nhìn học tập (learning / 학습) theo chuỗi:

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

## Dùng chung (common / 공통) Misconceptions

### “mất mát (loss / 손실) thấp nghĩa mô hình (model / 모델) tốt”

Chỉ đúng nếu nói rõ mất mát (loss / 손실) nào và trên phân phối (distribution / 분포) nào. huấn luyện (training / 학습) mất mát (loss / 손실) thấp có thể đi cùng severe overfitting.

### “Cross-entropy và accuracy là hai cách đo giống nhau”

Accuracy chỉ quan tâm predicted lớp (class / 클래스) cuối cùng; cross-entropy còn nhạy với xác suất (probability / 확률) assigned. Một mô hình (model / 모델) đúng nhưng cực kỳ uncertain và một mô hình (model / 모델) đúng với xác suất (probability / 확률) 0.999 có cùng accuracy nhưng mất mát (loss / 손실) khác mạnh.

### “Regularization chỉ là mẹo chống overfitting”

Regularization encode preference/inductive độ lệch (bias / 편향) về solution. Nó thay tối ưu hóa (optimization / 최적화) landscape và hypothesis được ưu tiên.

### “Nếu mục tiêu (objective / 목표) đúng thì môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작) chắc chắn đúng”

Không. phân phối (distribution / 분포) shift, dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) lỗi, calibration, threshold, hệ thống (system / 시스템) tương tác (interaction / 상호작용) và người dùng (user / 사용자) phản hồi (feedback / 피드백) đều có thể làm hành vi (behavior / 동작) khác huấn luyện (training / 학습) các giả định (assumptions / 가정들).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Mất mát (loss / 손실) nối xác suất (probability / 확률), thông tin (information / 정보) lý thuyết (theory / 이론) và tối ưu hóa (optimization / 최적화). rủi ro (risk / 위험) nối Statistics với generalization. mục tiêu (objective / 목표) nối mathematical huấn luyện (training / 학습) với sản phẩm (product / 제품) thiết kế (design / 설계) và AI an toàn (safety / 안전).

Xem tiếp: [Linear Regression](./05_linear_regression.md), [Logistic Regression](./06_logistic_regression.md), [Bias, Variance and Generalization](./14_bias_variance_and_generalization.md) và [Model Evaluation](./15_model_evaluation.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 what is machine learning](./00_what_is_machine_learning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
