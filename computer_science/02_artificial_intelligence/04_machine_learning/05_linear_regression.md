# Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Linear regression**. Route đi từ feature/target relationship → matrix formulation → least squares/regularization → residual diagnostics → prediction uncertainty, để mô hình tuyến tính nối với dữ liệu và giả định.

Tuyến tính (linear / 선형) Regression (선형 회귀 / hồi quy tuyến tính) là một trong những mô hình (model / 모델) đơn giản nhất trong Machine học tập (learning / 학습), nhưng giá trị của nó không nằm ở việc “dễ”. Nó là nơi nhiều idea cốt lõi gặp nhau: biểu diễn (representation / 표현) bằng véc-tơ (vector / 벡터), parameterized hàm (function / 함수), mất mát (loss / 손실), tối ưu hóa (optimization / 최적화), probabilistic các giả định (assumptions / 가정들), regularization, độ lệch (bias / 편향)–variance và interpretability.

Nếu hiểu tuyến tính (linear / 선형) Regression đúng bản chất, nhiều neural-network concept sau này sẽ trở nên tự nhiên hơn vì một tầng (layer / 계층) neural cơ bản cũng bắt đầu bằng phép biến đổi tuyến tính.

## Bài toán: từ nhiều yếu tố tới một đại lượng cần dự đoán

Giả sử muốn dự đoán giá nhà từ diện tích, tuổi nhà và khoảng cách tới ga tàu. Ta biểu diễn đầu vào (input / 입력) bằng véc-tơ (vector / 벡터):

\[
\mathbf{x}=[x_1,x_2,x_3]^T
\]

Mô hình (model / 모델) giả định đầu ra (output / 출력) có thể được xấp xỉ bằng weighted sum:

\[
\hat y=\mathbf w^T\mathbf x+b
\]

Mỗi weight `w_j` cho biết khi tính năng (feature / 기능) `x_j` thay đổi một đơn vị, prediction thay đổi bao nhiêu nếu giữ các tính năng (feature / 기능) khác cố định, trong phạm vi các giả định (assumptions / 가정들) của mô hình (model / 모델).

Từ `linear` ở đây nói về **tuyến tính (linear / 선형) theo parameters/features đã biểu diễn**, không nhất thiết nói raw-world relationship phải là đường thẳng đơn giản. Nếu thêm tính năng (feature / 기능) `x^2`, mô hình (model / 모델) vẫn tuyến tính (linear / 선형) theo parameters:

\[
\hat y=w_0+w_1x+w_2x^2
\]

Đây là polynomial regression nhưng vẫn thuộc linear-model family.

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Ma trận (matrix / 행렬) form** tiếp nhận điểm tựa từ **Bài toán: từ nhiều yếu tố tới một đại lượng cần dự đoán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Least Squares xuất hiện từ đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ma trận (matrix / 행렬) form

Với `n` samples, `d` features:

\[
X\in\mathbb R^{n\times d},\qquad \mathbf w\in\mathbb R^d
\]

Prediction toàn dataset:

\[
\hat{\mathbf y}=X\mathbf w+b\mathbf 1
\]

Nếu absorb độ lệch (bias / 편향) vào một cột toàn `1`, ta viết gọn:

\[
\hat{\mathbf y}=X\boldsymbol\beta
\]

Ma trận (matrix / 행렬) view quan trọng vì huấn luyện (training / 학습) hiện đại xử lý batch bằng vectorized tuyến tính (linear / 선형) algebra thay vì vòng lặp (loop / 루프) từng row.

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Least Squares xuất hiện từ đâu?** tiếp nhận điểm tựa từ **Ma trận (matrix / 행렬) form** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Closed-form solution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Least Squares xuất hiện từ đâu?

Ta thường minimize sum of squared errors:

\[
J(\mathbf w)=\sum_{i=1}^n(y_i-\mathbf w^T\mathbf x_i)^2
\]

Tại sao bình phương?

Một lý do computational: hàm trơn và convex, độ dốc (gradient / 기울기) dễ tính.

Một lý do statistical sâu hơn: nếu assume noise Gaussian độc lập với variance cố định:

\[
y_i=\mathbf w^T\mathbf x_i+\epsilon_i,\qquad \epsilon_i\sim\mathcal N(0,\sigma^2)
\]

thì maximizing likelihood của dữ liệu (data / 데이터) tương đương minimizing squared lỗi (error / 오류).

Vì vậy least squares không phải quy tắc (rule / 규칙) arbitrary; nó gắn với một probabilistic mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Closed-form solution** tiếp nhận điểm tựa từ **Least Squares xuất hiện từ đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Geometric interpretation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Closed-form solution

Nếu `X^T X` invertible, nghiệm Ordinary Least Squares:

\[
\hat{\mathbf w}=(X^TX)^{-1}X^T\mathbf y
\]

Công thức này đến từ việc đặt độ dốc (gradient / 기울기) của squared lỗi (error / 오류) bằng zero.

Nhưng môi trường vận hành (production / 운영 환경) mã (code / 코드) hiếm khi trực tiếp tính ma trận (matrix / 행렬) inverse vì numerical stability. Thực tế thường dùng QR decomposition, SVD hoặc iterative tối ưu hóa (optimization / 최적화).

Với dataset lớn hoặc mô hình (model / 모델) mở rộng, độ dốc (gradient / 기울기) descent thường phù hợp hơn.

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Geometric interpretation** tiếp nhận điểm tựa từ **Closed-form solution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính năng (feature / 기능) scaling và conditioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Geometric interpretation

`Xw` nằm trong column không gian (space / 공간) của `X`. Least squares tìm véc-tơ (vector / 벡터) prediction gần `y` nhất trong subspace đó.

Residual:

\[
\mathbf r=\mathbf y-X\hat{\mathbf w}
\]

ở optimum trực giao với column không gian (space / 공간):

\[
X^T\mathbf r=0
\]

Đây là projection hình học (geometry / 기하학). Nhìn như vậy giúp hiểu vì sao tuyến tính (linear / 선형) regression gắn chặt với tuyến tính (linear / 선형) Algebra, không chỉ là “vẽ best-fit line”.

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Tính năng (feature / 기능) scaling và conditioning** tiếp nhận điểm tựa từ **Geometric interpretation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multicollinearity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính năng (feature / 기능) scaling và conditioning

Về lý thuyết closed-form regression có thể handle tính năng (feature / 기능) scales khác nhau. Nhưng tối ưu hóa (optimization / 최적화) và numerical computation thường nhạy với quy mô (scale / 규모).

Nếu một tính năng (feature / 기능) nằm khoảng `0–1`, tính năng (feature / 기능) khác khoảng `0–1,000,000`, độ dốc (gradient / 기울기) landscape có thể bị kéo dài theo các direction khác nhau, làm độ dốc (gradient / 기울기) descent chậm.

Standardization:

\[
z=\frac{x-\mu}{\sigma}
\]

không làm mô hình (model / 모델) “thông minh hơn”, nhưng làm tối ưu hóa (optimization / 최적화) dễ hơn và regularization comparable hơn giữa features.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Multicollinearity** tiếp nhận điểm tựa từ **Tính năng (feature / 기능) scaling và conditioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ridge Regression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multicollinearity

Nếu hai features gần như tuyến tính (linear / 선형) combination của nhau, `X^T X` trở nên ill-conditioned. Parameters có thể cực kỳ unstable: prediction vẫn khá ổn nhưng individual coefficients thay mạnh khi dữ liệu (data / 데이터) thay nhẹ.

Ví dụ `income_in_won` và `income_in_thousand_won` chứa gần như cùng thông tin (information / 정보).

Điểm cần phân biệt:

> Stable prediction và stable interpretation không phải cùng một thuộc tính (property / 속성).

Regularization hoặc tính năng (feature / 기능) redesign thường giúp.

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Ridge Regression** tiếp nhận điểm tựa từ **Multicollinearity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lasso Regression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Ridge chấp nhận một ít độ lệch (bias / 편향) để giảm variance — một example điển hình của độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Lasso Regression** tiếp nhận điểm tựa từ **Ridge Regression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tương tác (interaction / 상호작용) và nonlinearity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lasso Regression

Lasso dùng L1:

\[
J=\|\mathbf y-X\mathbf w\|_2^2+\lambda\|\mathbf w\|_1
\]

L1 có hình học (geometry / 기하학) khiến nhiều coefficients có thể bị đẩy chính xác về zero, nên đôi khi đóng vai trò tính năng (feature / 기능) selection.

Nhưng nếu features strongly correlated, việc chọn tính năng (feature / 기능) nào có thể unstable. Không nên interpret “coefficient zero” như proof rằng variable hoàn toàn không liên quan real-world kết quả (outcome / 결과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Tương tác (interaction / 상호작용) và nonlinearity** tiếp nhận điểm tựa từ **Lasso Regression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Residual phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tương tác (interaction / 상호작용) và nonlinearity

Nếu ảnh hưởng của `x1` phụ thuộc `x2`, mô hình (model / 모델) tuyến tính đơn giản thiếu tương tác (interaction / 상호작용).

Ta có thể thêm:

\[
x_1x_2
\]

vào tính năng (feature / 기능) set:

\[
\hat y=w_0+w_1x_1+w_2x_2+w_3x_1x_2
\]

Mô hình (model / 모델) vẫn tuyến tính (linear / 선형) theo parameters nhưng biểu diễn relationship phong phú hơn.

Điều này minh họa principle chung:

> mô hình (model / 모델) sức chứa (capacity / 용량) phụ thuộc cả hàm (function / 함수) family lẫn biểu diễn (representation / 표현).

Deep học tập (learning / 학습) sau này giảm nhu cầu handcraft tương tác (interaction / 상호작용) bằng cách học biểu diễn (representation / 표현).

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Residual phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **Tương tác (interaction / 상호작용) và nonlinearity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Causality: coefficient không tự động là nhân quả (causal / 인과적) tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Residual phân tích (analysis / 분석)

Sau huấn luyện (training / 학습), residual không chỉ là số để tính RMSE. mẫu (pattern / 패턴) trong residual có thể reveal mô hình (model / 모델) misspecification.

Nếu residual tăng theo fitted giá trị (value / 값), variance có thể không constant. Nếu residual có cấu trúc (structure / 구조) theo thời gian (time / 시간), observations có thể không independent. Nếu residual cong theo tính năng (feature / 기능), tuyến tính (linear / 선형) form đang bỏ lỡ nonlinearity.

Residual phân tích (analysis / 분석) là cầu nối (bridge / 브리지) giữa statistical modeling và mô hình (model / 모델) debugging.

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Causality: coefficient không tự động là nhân quả (causal / 인과적) tác động (effect / 효과)** tiếp nhận điểm tựa từ **Residual phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Causality: coefficient không tự động là nhân quả (causal / 인과적) tác động (effect / 효과)

Nếu coefficient `w_income > 0`, ta chỉ biết trong mô hình (model / 모델)/dữ liệu (data / 데이터), income có association với đầu ra (output / 출력) sau khi conditioning trên included variables.

Không thể tự động kết luận “tăng income gây đầu ra (output / 출력) tăng” vì confounding, selection độ lệch (bias / 편향) và reverse causality có thể tồn tại.

Prediction và nhân quả (causal / 인과적) suy luận (inference / 추론) là hai mục tiêu khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Evaluation** tiếp nhận điểm tựa từ **Causality: coefficient không tự động là nhân quả (causal / 인과적) tác động (effect / 효과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết (connection / 연결) tới Neural Networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation

Dùng chung (common / 공통) regression metrics:

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

`R²` đo improvement tương đối so với baseline predict mean trên cùng mẫu (sample / 표본). Nó có thể âm trên kiểm thử (test / 테스트) dữ liệu (data / 데이터) nếu mô hình (model / 모델) tệ hơn baseline.

Không nên dùng một chỉ số (metric / 지표) mà không hiểu nghiệp vụ (business / 비즈니스) meaning của lỗi (error / 오류) quy mô (scale / 규모).

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, sau nội dung của **Evaluation**, **Liên kết (connection / 연결) tới Neural Networks** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) tới Neural Networks

Một neural tầng (layer / 계층) thường có dạng:

\[
\mathbf z=W\mathbf x+\mathbf b
\]

Nếu không có activation/nonlinear composition, nhiều tầng (layer / 계층) tuyến tính collapse thành một tuyến tính (linear / 선형) transformation duy nhất.

Vì vậy tuyến tính (linear / 선형) Regression là điểm xuất phát tự nhiên để hiểu tại sao neural mạng (network / 네트워크) cần nonlinearity.

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết (connection / 연결) tới Neural Networks** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Tuyến tính (linear / 선형) Regression có thể được nén thành:

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “tuyến tính (linear / 선형) Regression chỉ dùng khi đồ thị (graph / 그래프) là đường thẳng”

Sai. tính năng (feature / 기능) transformations và interactions có thể tạo nonlinear relationship theo raw đầu vào (input / 입력) trong khi mô hình (model / 모델) vẫn tuyến tính (linear / 선형) theo parameters.

### “Coefficient lớn nghĩa tính năng (feature / 기능) quan trọng hơn”

Không thể so trực tiếp nếu tính năng (feature / 기능) scales khác nhau. Correlation giữa features cũng làm coefficient interpretation phức tạp.

### “R² cao nghĩa mô hình (model / 모델) tốt”

Không đủ. Leakage, overfitting, phân phối (distribution / 분포) shift hoặc mục tiêu (target / 대상) definition sai vẫn có thể tạo R² đẹp.

### “Closed-form luôn tốt hơn độ dốc (gradient / 기울기) descent vì chính xác (exact / 정확한)”

Không. Dataset kích thước (size / 크기), numerical conditioning và tính năng (feature / 기능) dimension quyết định phương thức (method / 메서드) thực tế.

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Regression: từ quan hệ tuyến tính tới mô hình dự đoán**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tuyến tính (linear / 선형) Regression nối [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [Optimization](../01_mathematical_foundations/06_optimization.md) và [Bias–Variance](./14_bias_variance_and_generalization.md).

Xem tiếp: [Logistic Regression](./06_logistic_regression.md), nơi cùng tuyến tính (linear / 선형) score được biến thành probabilistic classifier.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
