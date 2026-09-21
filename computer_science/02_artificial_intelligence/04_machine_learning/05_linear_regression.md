# Linear Regression: từ quan hệ tuyến tính tới mô hình dự đoán

**Linear Regression (선형 회귀 / hồi quy tuyến tính)** là một trong những mô hình đơn giản nhất của Machine Learning, nhưng giá trị của nó không nằm ở việc “dễ”. Đây là nơi nhiều ý tưởng nền tảng gặp nhau: biểu diễn bằng vector, hàm có tham số, hàm mất mát, tối ưu hóa, giả định xác suất, regularization, bias–variance và khả năng diễn giải.

Nếu hiểu Linear Regression từ bản chất, nhiều khái niệm của neural network sau này sẽ trở nên tự nhiên hơn, vì một layer neural cơ bản cũng bắt đầu từ một phép biến đổi tuyến tính.

## Bài toán: từ nhiều yếu tố tới một đại lượng cần dự đoán

Giả sử muốn dự đoán giá nhà từ diện tích, tuổi ngôi nhà và khoảng cách tới ga tàu. Ta biểu diễn đầu vào bằng vector:

\[
\mathbf{x}=[x_1,x_2,x_3]^T
\]

Mô hình giả định đầu ra có thể được xấp xỉ bằng tổng có trọng số:

\[
\hat y=\mathbf w^T\mathbf x+b
\]

Mỗi trọng số (weight) `w_j` mô tả mức dự đoán thay đổi khi feature `x_j` tăng một đơn vị trong điều kiện các feature còn lại được giữ cố định và các giả định của mô hình vẫn phù hợp.

Từ `linear` ở đây nói về **tính tuyến tính theo tham số và feature đã biểu diễn**, không có nghĩa quan hệ ngoài thế giới thật bắt buộc phải là một đường thẳng đơn giản. Nếu thêm feature `x^2`:

\[
\hat y=w_0+w_1x+w_2x^2
\]

thì ta có polynomial regression, nhưng mô hình vẫn tuyến tính theo các tham số `w_0,w_1,w_2`.

## Dạng ma trận

Với `n` mẫu và `d` feature:

\[
X\in\mathbb R^{n\times d},\qquad \mathbf w\in\mathbb R^d
\]

Dự đoán cho toàn bộ dataset có thể viết:

\[
\hat{\mathbf y}=X\mathbf w+b\mathbf 1
\]

Nếu gộp bias vào một cột toàn số `1`, ta viết gọn:

\[
\hat{\mathbf y}=X\boldsymbol\beta
\]

Cách nhìn bằng ma trận rất quan trọng vì training hiện đại xử lý cả batch bằng đại số tuyến tính vector hóa thay vì lặp thủ công qua từng dòng.

## Least Squares xuất hiện từ đâu?

Ta thường tối thiểu hóa tổng bình phương sai số:

\[
J(\mathbf w)=\sum_{i=1}^n(y_i-\mathbf w^T\mathbf x_i)^2
\]

Vì sao lại bình phương?

Về mặt tính toán, hàm này trơn và lồi nên gradient dễ tính và bài toán dễ tối ưu.

Về mặt thống kê, nếu giả định nhiễu độc lập và có phân phối Gaussian với phương sai cố định:

\[
y_i=\mathbf w^T\mathbf x_i+\epsilon_i,\qquad \epsilon_i\sim\mathcal N(0,\sigma^2)
\]

thì tối đa hóa likelihood của dữ liệu tương đương với tối thiểu hóa squared error.

Vì vậy phương pháp bình phương tối thiểu (least squares) không phải một quy tắc tùy ý; nó gắn với một mô hình xác suất cụ thể.

## Nghiệm dạng đóng

Nếu `X^T X` khả nghịch, nghiệm của Ordinary Least Squares có dạng:

\[
\hat{\mathbf w}=(X^TX)^{-1}X^T\mathbf y
\]

Đây được gọi là **nghiệm dạng đóng (closed-form solution)** vì có thể biểu diễn trực tiếp bằng công thức thay vì phải lặp nhiều bước tối ưu.

Công thức thu được bằng cách đặt gradient của squared error bằng 0.

Tuy nhiên code production hiếm khi trực tiếp tính ma trận nghịch đảo vì vấn đề ổn định số. Thực tế thường dùng QR decomposition, SVD hoặc các solver tuyến tính ổn định hơn. Với dataset rất lớn hoặc mô hình mở rộng, gradient descent cũng có thể phù hợp hơn.

## Cách hiểu hình học

Vector `Xw` luôn nằm trong không gian cột (column space) của `X`. Least Squares tìm điểm trong không gian con này gần `y` nhất.

Phần dư (residual):

\[
\mathbf r=\mathbf y-X\hat{\mathbf w}
\]

ở nghiệm tối ưu sẽ trực giao với column space:

\[
X^T\mathbf r=0
\]

Đây là một bài toán chiếu hình học (projection). Cách nhìn này giúp hiểu Linear Regression như một vấn đề Đại số tuyến tính chứ không đơn thuần là “vẽ đường thẳng khớp dữ liệu nhất”.

## Chuẩn hóa feature và conditioning

Về lý thuyết, nghiệm dạng đóng vẫn có thể xử lý các feature có scale khác nhau. Nhưng quá trình tối ưu và tính toán số lại nhạy với scale.

Nếu một feature nằm trong khoảng `0–1`, trong khi feature khác nằm trong khoảng `0–1,000,000`, bề mặt loss có thể bị kéo dài mạnh theo một số hướng, khiến gradient descent hội tụ chậm.

Chuẩn hóa chuẩn:

\[
z=\frac{x-\mu}{\sigma}
\]

không làm mô hình “thông minh hơn”, nhưng thường giúp bài toán tối ưu có điều kiện tốt hơn (better conditioning) và làm regularization giữa các feature dễ so sánh hơn.

## Đa cộng tuyến

Nếu hai feature gần như là tổ hợp tuyến tính của nhau, `X^T X` có thể trở nên **điều kiện kém (ill-conditioned)**.

Khi đó prediction tổng thể đôi khi vẫn tương đối ổn nhưng từng hệ số riêng lẻ có thể thay đổi rất mạnh chỉ vì dataset thay đổi nhẹ.

Ví dụ `income_in_won` và `income_in_thousand_won` gần như chứa cùng một thông tin.

Điểm cần phân biệt là:

> Dự đoán ổn định và diễn giải hệ số ổn định không phải cùng một thuộc tính.

Regularization hoặc thiết kế lại feature thường giúp giảm vấn đề này.

## Ridge Regression

Ridge Regression thêm penalty L2:

\[
J(\mathbf w)=\|\mathbf y-X\mathbf w\|_2^2+\lambda\|\mathbf w\|_2^2
\]

Nghiệm:

\[
\hat{\mathbf w}=(X^TX+\lambda I)^{-1}X^T\mathbf y
\]

Thành phần `λI` cải thiện conditioning và kéo các trọng số về gần 0 hơn.

Ridge chấp nhận thêm một ít độ lệch (bias) để giảm phương sai (variance). Đây là ví dụ kinh điển của sự đánh đổi bias–variance.

## Lasso Regression

Lasso dùng penalty L1:

\[
J=\|\mathbf y-X\mathbf w\|_2^2+\lambda\|\mathbf w\|_1
\]

Hình học của L1 khiến nhiều hệ số có thể bị đẩy chính xác về 0, nên Lasso đôi khi đồng thời đóng vai trò lựa chọn feature.

Tuy nhiên nếu nhiều feature tương quan mạnh, việc feature nào bị giữ lại hoặc loại bỏ có thể thiếu ổn định. Không nên diễn giải “coefficient bằng 0” như bằng chứng rằng biến đó hoàn toàn không liên quan tới outcome ngoài thực tế.

## Tương tác và phi tuyến

Nếu ảnh hưởng của `x1` phụ thuộc `x2`, Linear Regression đơn giản không tự biểu diễn interaction đó.

Có thể thêm feature:

\[
x_1x_2
\]

và mô hình trở thành:

\[
\hat y=w_0+w_1x_1+w_2x_2+w_3x_1x_2
\]

Mô hình vẫn tuyến tính theo tham số, nhưng biểu diễn quan hệ đã phong phú hơn.

Điều này minh họa một nguyên lý chung:

> Khả năng biểu diễn của mô hình phụ thuộc cả họ hàm lẫn cách biểu diễn đầu vào.

Deep Learning giảm nhu cầu phải thiết kế thủ công nhiều interaction bằng cách học representation qua nhiều layer.

## Phân tích phần dư

Sau training, residual không chỉ dùng để tính RMSE. Cấu trúc trong phần dư có thể cho thấy mô hình đang bị đặc tả sai.

Nếu residual tăng theo predicted value, phương sai có thể không cố định. Nếu residual có pattern theo thời gian, các quan sát có thể không độc lập. Nếu residual tạo hình cong theo một feature, dạng tuyến tính đang bỏ sót quan hệ phi tuyến.

Phân tích phần dư (residual analysis) là cầu nối giữa mô hình thống kê và quá trình debug mô hình.

## Hệ số không tự động là tác động nhân quả

Nếu `w_income > 0`, ta chỉ biết trong dữ liệu và mô hình hiện tại, `income` có liên hệ với đầu ra sau khi giữ các biến đã đưa vào mô hình cố định.

Không thể tự động kết luận “tăng income sẽ gây output tăng”, vì có thể tồn tại confounding, selection bias hoặc reverse causality.

Dự đoán và suy luận nhân quả là hai mục tiêu khác nhau.

## Đánh giá mô hình hồi quy

Các metric thường gặp:

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

`R²` đo mức cải thiện tương đối so với baseline luôn dự đoán giá trị trung bình trên cùng sample. Trên test data, `R²` có thể âm nếu mô hình còn tệ hơn baseline đó.

Không nên chọn metric chỉ vì phổ biến; cần hiểu scale của lỗi có ý nghĩa gì với bài toán nghiệp vụ.

## Liên hệ với Neural Network

Một neural layer thường có dạng:

\[
\mathbf z=W\mathbf x+\mathbf b
\]

Nếu không có activation phi tuyến, nhiều layer tuyến tính liên tiếp vẫn có thể rút gọn thành một phép biến đổi tuyến tính duy nhất.

Vì vậy Linear Regression là điểm xuất phát rất tự nhiên để hiểu tại sao neural network cần nonlinearity.

## Mô hình tư duy

Có thể nén Linear Regression thành:

```text
Biểu diễn đầu vào bằng feature
        ↓
Tính tổng tuyến tính có trọng số
        ↓
So sánh prediction với target
        ↓
Tối thiểu hóa loss phù hợp
        ↓
Kiểm tra generalization và cấu trúc residual
```

## Các hiểu lầm thường gặp

### “Linear Regression chỉ dùng khi đồ thị là đường thẳng”

Không. Feature transformation và interaction có thể tạo quan hệ phi tuyến theo raw input trong khi mô hình vẫn tuyến tính theo tham số.

### “Hệ số lớn nghĩa là feature quan trọng hơn”

Không thể so trực tiếp nếu scale của feature khác nhau. Tương quan giữa các feature cũng làm việc diễn giải hệ số phức tạp hơn.

### “R² cao nghĩa là mô hình tốt”

Không đủ. Leakage, overfitting, distribution shift hoặc target definition sai vẫn có thể tạo `R²` đẹp.

### “Closed-form luôn tốt hơn gradient descent vì chính xác”

Không. Kích thước dataset, số chiều feature và numerical conditioning quyết định phương pháp thực tế phù hợp hơn.

## Liên kết kiến thức

Linear Regression nối [Đại số tuyến tính](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Xác suất](../01_mathematical_foundations/02_probability_for_ai.md), [Tối ưu hóa](../01_mathematical_foundations/06_optimization.md) và [Bias–Variance](./14_bias_variance_and_generalization.md).

Xem tiếp: [Logistic Regression](./06_logistic_regression.md), nơi cùng một linear score được biến thành bộ phân loại xác suất.