# Bias, Variance và khả năng khái quát hóa

Machine Learning không được đánh giá bằng khả năng ghi nhớ training data mà bằng khả năng **khái quát hóa (generalization / 일반화)** sang những mẫu chưa từng thấy nhưng vẫn thuộc môi trường mục tiêu. Đây là điểm phân biệt quan trọng giữa học và ghi nhớ.

Ba khái niệm giúp phân tích vấn đề này là **độ lệch (bias)**, **phương sai (variance)** và **nhiễu không thể loại bỏ (irreducible noise)**. Chúng không chỉ là từ vựng dùng để giải thích overfitting; chúng còn là khung tư duy để hiểu model capacity, regularization, kích thước dữ liệu và ensemble.

## Training error không phải mục tiêu cuối cùng

Một mô hình có thể đạt training loss gần 0 bằng cách ghi nhớ dataset. Nếu đầu vào tương lai khác những example đã thấy, prediction vẫn có thể thất bại.

Ta thật sự quan tâm tới rủi ro kỳ vọng:

\[
R(f)=\mathbb E_{(X,Y)\sim P}[L(Y,f(X))]
\]

nhưng chỉ quan sát được một mẫu hữu hạn. Thiết kế validation/test cố gắng ước lượng rủi ro này dưới các giả định về phân phối tương lai.

Khoảng cách khái quát hóa:

\[
Gap=R_{test}-R_{train}
\]

là một tín hiệu hữu ích, nhưng cách diễn giải phụ thuộc test split có thật sự đại diện cho deployment hay không.

## Bias trong phân rã Bias–Variance

Ở đây **bias** không phải social bias hay fairness bias. Nó là sai lệch có hệ thống do họ mô hình hoặc thủ tục học không thể, hoặc không có xu hướng, nắm được quan hệ thật.

Với hồi quy squared error, trong các giả định phù hợp:

\[
\mathbb E[(Y-\hat f(x))^2]
=Bias^2+Variance+Noise
\]

Bias cao nghĩa mô hình liên tục bỏ sót cấu trúc, ví dụ cố fit một đường thẳng cho quan hệ rất cong.

Variance cao nghĩa mô hình thay đổi mạnh chỉ vì training sample thay đổi nhẹ.

Noise là phần bất định không thể loại bỏ hoàn toàn chỉ bằng mô hình tốt hơn nếu feature quan sát không chứa đủ thông tin.

## Underfitting và Overfitting

**Underfitting** thường xảy ra khi model capacity quá thấp, representation nghèo hoặc optimization chưa đủ. Training error và validation error đều cao.

**Overfitting** xảy ra khi mô hình học quá nhiều chi tiết hoặc noise riêng của training sample khiến validation và generalization kém. Training error thấp nhưng validation error cao hơn đáng kể.

Tuy nhiên Deep Learning hiện đại làm hình ảnh textbook đơn giản trở nên phức tạp hơn. Neural network dư tham số có thể nội suy toàn bộ training set nhưng vẫn generalize tốt nhờ regularization tường minh hoặc ngầm, quy mô dữ liệu và bias của optimization.

Vì vậy quy tắc “số tham số lớn hơn số mẫu thì chắc chắn overfit” không phải nguyên lý phổ quát.

## Model Capacity

**Khả năng biểu diễn của mô hình (model capacity)** mô tả mức phong phú của lớp hàm mà mô hình có thể đại diện.

Ví dụ Linear Regression với ít feature có capacity thấp; Decision Tree sâu cao hơn; neural network lớn có capacity rất cao.

Capacity cao làm giảm approximation bias vì mô hình có thể biểu diễn nhiều cấu trúc hơn, nhưng đồng thời mở ra nhiều nghiệm có khả năng fit cả noise.

Regularization và dữ liệu giúp giới hạn quá trình học để chọn nghiệm có generalization tốt hơn.

## Thiên lệch quy nạp

Không một mô hình nào có thể học từ dữ liệu hữu hạn mà hoàn toàn không mang giả định.

Linear model giả định quan hệ hữu ích gần tuyến tính trong representation hiện tại. CNN giả định locality và cấu trúc dịch chuyển. Decision Tree giả định có thể chia không gian bằng nhiều threshold. Transformer giả định tương tác token có thể học qua attention và layer dùng chung.

Inductive bias phù hợp với domain giúp mô hình học hiệu quả hơn từ ít dữ liệu hơn.

## Regularization

### Regularization tường minh

L2:

\[
J=\hat R+\lambda\|\theta\|_2^2
\]

L1, dropout, label smoothing, data augmentation và nhiều kỹ thuật khác đưa các preference khác nhau vào quá trình học.

### Early Stopping

Trong training lặp, validation performance có thể đạt mức tốt nhất trước khi training loss xuống thấp nhất.

Dừng sớm giúp ngăn mô hình tiếp tục fit những chi tiết quá đặc thù của training sample.

### Data Augmentation

Các phép lật/crop ảnh, perturbation âm thanh hoặc biến đổi văn bản hợp lệ mã hóa giả định rằng label không nên thay đổi dưới một số transformation.

Augmentation không chỉ “tạo thêm dữ liệu”; nó đưa inductive bias vào mô hình.

## Thêm dữ liệu thay đổi trade-off như thế nào?

Với một họ mô hình phù hợp, thêm dữ liệu đại diện thường làm giảm variance và khiến estimate ổn định hơn.

Nhưng thêm dữ liệu từ sai distribution không nhất thiết giúp. Duplicate, dữ liệu kém chất lượng hoặc biased cũng không tạo lượng thông tin độc lập mới tương đương số dòng tăng thêm.

Do đó nên nghĩ về quy mô dữ liệu theo **độ đa dạng hiệu dụng và độ bao phủ (effective diversity and coverage)** chứ không chỉ số record.

## Learning Curve

Biểu đồ hiệu quả theo kích thước training set giúp chẩn đoán:

```text
training error cao, validation error cao và gần nhau
→ có thể bias cao

training rất tốt, validation kém và gap lớn
→ có thể variance cao

validation tiếp tục cải thiện rõ khi thêm dữ liệu
→ dữ liệu bổ sung có khả năng hữu ích
```

Learning curve thường hữu ích hơn việc chỉ gắn nhãn “overfit” từ một snapshot metric.

## Cross-Validation

k-fold cross-validation chia data thành `k` fold; mỗi lần train trên `k-1` fold rồi validation trên fold còn lại.

Cách này làm estimate bớt phụ thuộc vào một random split cụ thể và cho thấy variability giữa các fold.

Tuy nhiên random k-fold không phù hợp với mọi bài toán. Time series cần split theo thời gian; nhiều dòng của cùng user cần group split; spatial data có autocorrelation có thể cần spatial split.

Validation scheme phải mô phỏng đúng ranh giới deployment.

## Distribution Shift

Lý thuyết generalization cơ bản thường giả định train và test đến từ cùng hoặc các distribution có quan hệ rõ ràng. Production lại thường gặp shift.

Các dạng hữu ích gồm:

- **covariate shift**: `P(X)` thay đổi;
- **label/prior shift**: `P(Y)` thay đổi;
- **concept shift**: `P(Y|X)` thay đổi.

Fraud là ví dụ điển hình của concept drift khi attacker thay chiến thuật.

Một mô hình có IID test score rất cao vẫn có thể thất bại mạnh dưới distribution shift.

## Shortcut Learning

Mô hình có thể khai thác một correlation dễ nhưng không bền vững.

Ví dụ bộ phân loại ảnh y tế học watermark của bệnh viện thay vì pattern bệnh lý. Nếu train/test đều chia từ cùng nguồn, metric vẫn cao; khi sang bệnh viện khác performance sụp đổ.

Đây là thất bại generalization do dữ liệu và representation, không chỉ do “quá nhiều tham số”.

## Tương quan giả

Một feature có thể tương quan với target do hoàn cảnh lịch sử chứ không phải quan hệ ổn định.

Khi môi trường thay đổi, correlation đó biến mất và mô hình thất bại.

Domain knowledge, external validation và stress test rất quan trọng để phát hiện việc mô hình phụ thuộc vào những tín hiệu mong manh.

## Double Descent

Trực giác cổ điển thường mô tả test error giảm rồi tăng khi complexity vượt điểm tối ưu.

Trong một số mô hình dư tham số hiện đại xuất hiện hiện tượng **double descent**: error tăng gần ngưỡng nội suy rồi lại giảm khi mô hình tiếp tục lớn hơn.

Điều này cho thấy bias–variance vẫn là một khung tư duy hữu ích, nhưng đường cong chữ U đơn giản không mô tả đầy đủ hành vi Deep Learning hiện đại.

## Ensemble và Variance

Bagging và Random Forest giảm variance bằng cách lấy trung bình nhiều mô hình có lỗi không hoàn toàn tương quan.

Boosting thường tập trung giảm bias bằng cách sửa lỗi tuần tự, nhưng cũng có cơ chế regularization như shrinkage, giới hạn độ sâu tree hoặc subsampling.

Xem: [Ensemble Learning](./09_ensemble_learning.md).

## Generalization trong LLM

LLM pretraining không chỉ đơn giản là “ghi nhớ Internet”. Mô hình học pattern thống kê và representation có khả năng tái kết hợp để xử lý nhiều input chưa thấy nguyên văn.

Tuy nhiên memorization vẫn tồn tại, đặc biệt với chuỗi hiếm hoặc dữ liệu lặp nhiều.

In-context learning, domain shift, contamination và benchmark leakage làm việc đánh giá generalization của LLM phức tạp hơn supervised tabular ML rất nhiều.

Các chương LLM phía sau sẽ mở rộng các vấn đề này.

## Mô hình tư duy

```text
Mẫu dữ liệu quan sát
   ↓ thuật toán học + inductive bias
Giả thuyết được chọn
   ↓
Hiệu quả trên distribution mới
```

Khi mô hình thất bại, nên kiểm tra bốn tầng:

```text
Representation có đủ tín hiệu không?
Model capacity có phù hợp không?
Learning / regularization đang ưu tiên nghiệm nào?
Validation có giống deployment distribution không?
```

## Các hiểu lầm thường gặp

### “Overfitting nghĩa là mô hình có quá nhiều tham số”

Không. Parameter count chỉ là một yếu tố; dữ liệu, architecture, regularization, optimization và task đều quan trọng.

### “Train và test đều tốt nghĩa là mô hình robust”

Chỉ khi test thật sự đại diện deployment. IID split có thể bỏ sót shortcut hoặc distribution shift.

### “Thêm data luôn giải quyết overfitting”

Không. Dữ liệu mới phải có thông tin, đa dạng và liên quan tới distribution mục tiêu.

### “Bias trong bias–variance chính là fairness bias”

Không. Đây là statistical estimation bias; fairness bias là một khái niệm khác dù có thể tương tác trong hệ thống thực tế.

## Liên kết kiến thức

Generalization nối [Thống kê cho AI](../01_mathematical_foundations/03_statistics_for_ai.md), [Bài toán học và thiên lệch quy nạp](./01_learning_problem_and_inductive_bias.md), [Training/Validation/Testing](./03_training_validation_and_testing.md), [Ensemble Learning](./09_ensemble_learning.md) và [Đánh giá mô hình](./15_model_evaluation.md).