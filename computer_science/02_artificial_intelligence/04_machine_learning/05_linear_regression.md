# Linear Regression: từ quan hệ tuyến tính tới mô hình dự đoán

Linear Regression (선형 회귀 / hồi quy tuyến tính) là một trong những model đơn giản nhất trong Machine Learning, nhưng giá trị của nó không nằm ở việc “dễ”. Nó là nơi nhiều idea cốt lõi gặp nhau: representation bằng vector, parameterized function, loss, optimization, probabilistic assumptions, regularization, bias–variance và interpretability.

Nếu hiểu Linear Regression đúng bản chất, nhiều neural-network concept sau này sẽ trở nên tự nhiên hơn vì một layer neural cơ bản cũng bắt đầu bằng phép biến đổi tuyến tính.

## Bài toán: từ nhiều yếu tố tới một đại lượng cần dự đoán

Giả sử muốn dự đoán giá nhà từ diện tích, tuổi nhà và khoảng cách tới ga tàu. Ta biểu diễn input bằng vector:

\[
\mathbf{x}=[x_1,x_2,x_3]^T
\]

Model giả định output có thể được xấp xỉ bằng weighted sum:

\[
\hat y=\mathbf w^T\mathbf x+b
\]

Mỗi weight `w_j` cho biết khi feature `x_j` thay đổi một đơn vị, prediction thay đổi bao nhiêu nếu giữ các feature khác cố định, trong phạm vi assumptions của model.

Từ `linear` ở đây nói về **linear theo parameters/features đã biểu diễn**, không nhất thiết nói raw-world relationship phải là đường thẳng đơn giản. Nếu thêm feature `x^2`, model vẫn linear theo parameters:

\[
\hat y=w_0+w_1x+w_2x^2
\]

Đây là polynomial regression nhưng vẫn thuộc linear-model family.

## Matrix form

Với `n` samples, `d` features:

\[
X\in\mathbb R^{n\times d},\qquad \mathbf w\in\mathbb R^d
\]

Prediction toàn dataset:

\[
\hat{\mathbf y}=X\mathbf w+b\mathbf 1
\]

Nếu absorb bias vào một cột toàn `1`, ta viết gọn:

\[
\hat{\mathbf y}=X\boldsymbol\beta
\]

Matrix view quan trọng vì training hiện đại xử lý batch bằng vectorized linear algebra thay vì loop từng row.

## Least Squares xuất hiện từ đâu?

Ta thường minimize sum of squared errors:

\[
J(\mathbf w)=\sum_{i=1}^n(y_i-\mathbf w^T\mathbf x_i)^2
\]

Tại sao bình phương?

Một lý do computational: hàm trơn và convex, gradient dễ tính.

Một lý do statistical sâu hơn: nếu assume noise Gaussian độc lập với variance cố định:

\[
y_i=\mathbf w^T\mathbf x_i+\epsilon_i,\qquad \epsilon_i\sim\mathcal N(0,\sigma^2)
\]

thì maximizing likelihood của data tương đương minimizing squared error.

Vì vậy least squares không phải rule arbitrary; nó gắn với một probabilistic model.

## Closed-form solution

Nếu `X^T X` invertible, nghiệm Ordinary Least Squares:

\[
\hat{\mathbf w}=(X^TX)^{-1}X^T\mathbf y
\]

Công thức này đến từ việc đặt gradient của squared error bằng zero.

Nhưng production code hiếm khi trực tiếp tính matrix inverse vì numerical stability. Thực tế thường dùng QR decomposition, SVD hoặc iterative optimization.

Với dataset lớn hoặc model mở rộng, gradient descent thường phù hợp hơn.

## Geometric interpretation

`Xw` nằm trong column space của `X`. Least squares tìm vector prediction gần `y` nhất trong subspace đó.

Residual:

\[
\mathbf r=\mathbf y-X\hat{\mathbf w}
\]

ở optimum trực giao với column space:

\[
X^T\mathbf r=0
\]

Đây là projection geometry. Nhìn như vậy giúp hiểu vì sao linear regression gắn chặt với Linear Algebra, không chỉ là “vẽ best-fit line”.

## Feature scaling và conditioning

Về lý thuyết closed-form regression có thể handle feature scales khác nhau. Nhưng optimization và numerical computation thường nhạy với scale.

Nếu một feature nằm khoảng `0–1`, feature khác khoảng `0–1,000,000`, gradient landscape có thể bị kéo dài theo các direction khác nhau, làm gradient descent chậm.

Standardization:

\[
z=\frac{x-\mu}{\sigma}
\]

không làm model “thông minh hơn”, nhưng làm optimization dễ hơn và regularization comparable hơn giữa features.

## Multicollinearity

Nếu hai features gần như linear combination của nhau, `X^T X` trở nên ill-conditioned. Parameters có thể cực kỳ unstable: prediction vẫn khá ổn nhưng individual coefficients thay mạnh khi data thay nhẹ.

Ví dụ `income_in_won` và `income_in_thousand_won` chứa gần như cùng information.

Điểm cần phân biệt:

> Stable prediction và stable interpretation không phải cùng một property.

Regularization hoặc feature redesign thường giúp.

## Ridge Regression

Ridge thêm L2 penalty:

\[
J(\mathbf w)=\|\mathbf y-X\mathbf w\|_2^2+\lambda\|\mathbf w\|_2^2
\]

Nghiệm:

\[
\hat{\mathbf w}=(X^TX+\lambda I)^{-1}X^T\mathbf y
\]

Term `λI` cải thiện conditioning và shrink weights.

Ridge chấp nhận một ít bias để giảm variance — một example điển hình của bias–variance trade-off.

## Lasso Regression

Lasso dùng L1:

\[
J=\|\mathbf y-X\mathbf w\|_2^2+\lambda\|\mathbf w\|_1
\]

L1 có geometry khiến nhiều coefficients có thể bị đẩy chính xác về zero, nên đôi khi đóng vai trò feature selection.

Nhưng nếu features strongly correlated, việc chọn feature nào có thể unstable. Không nên interpret “coefficient zero” như proof rằng variable hoàn toàn không liên quan real-world outcome.

## Interaction và nonlinearity

Nếu ảnh hưởng của `x1` phụ thuộc `x2`, model tuyến tính đơn giản thiếu interaction.

Ta có thể thêm:

\[
x_1x_2
\]

vào feature set:

\[
\hat y=w_0+w_1x_1+w_2x_2+w_3x_1x_2
\]

Model vẫn linear theo parameters nhưng biểu diễn relationship phong phú hơn.

Điều này minh họa principle chung:

> Model capacity phụ thuộc cả function family lẫn representation.

Deep Learning sau này giảm nhu cầu handcraft interaction bằng cách học representation.

## Residual analysis

Sau training, residual không chỉ là số để tính RMSE. Pattern trong residual có thể reveal model misspecification.

Nếu residual tăng theo fitted value, variance có thể không constant. Nếu residual có structure theo time, observations có thể không independent. Nếu residual cong theo feature, linear form đang bỏ lỡ nonlinearity.

Residual analysis là bridge giữa statistical modeling và model debugging.

## Causality: coefficient không tự động là causal effect

Nếu coefficient `w_income > 0`, ta chỉ biết trong model/data, income có association với output sau khi conditioning trên included variables.

Không thể tự động kết luận “tăng income gây output tăng” vì confounding, selection bias và reverse causality có thể tồn tại.

Prediction và causal inference là hai mục tiêu khác nhau.

## Evaluation

Common regression metrics:

\[
MAE=\frac1n\sum_i|y_i-\hat y_i|
\]

\[
MSE=\frac1n\sum_i(y_i-\hat y_i)^2
\]

\[
RMSE=\sqrt{MSE}
\]

\[
R^2=1-\frac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y)^2}
\]

`R²` đo improvement tương đối so với baseline predict mean trên cùng sample. Nó có thể âm trên test data nếu model tệ hơn baseline.

Không nên dùng một metric mà không hiểu business meaning của error scale.

## Connection tới Neural Networks

Một neural layer thường có dạng:

\[
\mathbf z=W\mathbf x+\mathbf b
\]

Nếu không có activation/nonlinear composition, nhiều layer tuyến tính collapse thành một linear transformation duy nhất.

Vì vậy Linear Regression là điểm xuất phát tự nhiên để hiểu tại sao neural network cần nonlinearity.

## Mental Model

Linear Regression có thể được nén thành:

```text
Represent input as features
        ↓
Weighted linear combination
        ↓
Compare prediction with target
        ↓
Minimize squared / chosen loss
        ↓
Inspect generalization + residual structure
```

## Common Misconceptions

### “Linear Regression chỉ dùng khi graph là đường thẳng”

Sai. Feature transformations và interactions có thể tạo nonlinear relationship theo raw input trong khi model vẫn linear theo parameters.

### “Coefficient lớn nghĩa feature quan trọng hơn”

Không thể so trực tiếp nếu feature scales khác nhau. Correlation giữa features cũng làm coefficient interpretation phức tạp.

### “R² cao nghĩa model tốt”

Không đủ. Leakage, overfitting, distribution shift hoặc target definition sai vẫn có thể tạo R² đẹp.

### “Closed-form luôn tốt hơn gradient descent vì exact”

Không. Dataset size, numerical conditioning và feature dimension quyết định method thực tế.

## Knowledge Connection

Linear Regression nối [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [Optimization](../01_mathematical_foundations/06_optimization.md) và [Bias–Variance](./14_bias_variance_and_generalization.md).

Xem tiếp: [Logistic Regression](./06_logistic_regression.md), nơi cùng linear score được biến thành probabilistic classifier.