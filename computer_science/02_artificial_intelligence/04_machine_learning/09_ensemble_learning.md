# Ensemble Learning: kết hợp nhiều mô hình để tạo hệ thống mạnh hơn

**Ensemble Learning (앙상블 학습 / học tổ hợp mô hình)** bắt đầu từ một quan sát đơn giản: một mô hình riêng lẻ có thể mắc lỗi do nhiễu, khác biệt của mẫu dữ liệu hoặc giới hạn của họ hàm. Nếu kết hợp nhiều mô hình có kiểu sai khác nhau, dự đoán tổng hợp có thể ổn định và chính xác hơn.

Hai họ quan trọng nhất là **bagging** và **boosting**. Cả hai đều dùng nhiều learner, nhưng cơ chế gần như đối lập: bagging huấn luyện các mô hình tương đối độc lập rồi lấy trung bình để giảm variance; boosting xây mô hình tuần tự, mỗi mô hình mới cố sửa phần mà ensemble hiện tại còn làm chưa tốt.

## Vì sao lấy trung bình có thể giảm variance?

Giả sử các estimator có cùng variance `σ²` và correlation theo cặp là `ρ`. Variance của trung bình từ `M` mô hình xấp xỉ:

\[
Var(\bar f)\approx \rho\sigma^2+\frac{1-\rho}{M}\sigma^2
\]

Khi `M` tăng, phần nhiễu độc lập giảm dần. Nhưng nếu các mô hình gần như hoàn toàn tương quan (`ρ≈1`), việc lấy trung bình hầu như không giúp.

Trực giác cốt lõi là:

> Ensemble cần cả **mô hình đủ mạnh** và **sự đa dạng giữa các mô hình**.

## Bagging

**Bootstrap Aggregating (Bagging / 배깅)** tạo nhiều dataset bootstrap bằng cách lấy mẫu có hoàn lại từ training set. Mỗi mô hình được train trên một mẫu hơi khác nhau; prediction cuối được lấy trung bình hoặc bỏ phiếu.

Decision Tree đặc biệt phù hợp với bagging vì cây riêng lẻ có variance cao: chỉ thay đổi một ít dữ liệu cũng có thể thay cấu trúc cây đáng kể. Trung bình hóa nhiều cây giúp hệ thống ổn định hơn.

## Random Forest

Random Forest bổ sung thêm một nguồn ngẫu nhiên: tại mỗi split, cây chỉ được xem xét một tập con ngẫu nhiên của các feature.

Điều này làm giảm correlation giữa các tree. Nếu mọi tree đều luôn thấy cùng một feature vượt trội ở root, chúng có xu hướng trở nên rất giống nhau; random feature subset buộc các cây khám phá nhiều cấu trúc khác nhau hơn.

Classification:

\[
\hat y=mode\{f_1(x),...,f_M(x)\}
\]

Regression:

\[
\hat y=\frac1M\sum_{m=1}^M f_m(x)
\]

Random Forest thường là baseline mạnh cho dữ liệu bảng vì ít cần scaling, xử lý tốt interaction phi tuyến và thường không quá nhạy hyperparameter như boosting.

## Đánh giá Out-of-Bag

Mỗi bootstrap sample bỏ lại khoảng 36,8% các mẫu training duy nhất. Những mẫu không được dùng để train một tree được gọi là **out-of-bag (OOB)** đối với tree đó.

Ta có thể lấy prediction từ những tree mà mẫu đang xét thuộc OOB rồi tổng hợp để ước lượng performance mà không cần một validation set riêng trong một số trường hợp.

Tuy nhiên OOB không sửa được các vấn đề như leakage theo thời gian hoặc theo group. Thiết kế split vẫn phải phù hợp bài toán.

## Boosting: sửa lỗi theo từng bước

Boosting xây một mô hình cộng dồn:

\[
F_M(x)=\sum_{m=1}^{M}\alpha_m h_m(x)
\]

Mỗi learner `h_m` mới được thêm vào để cải thiện objective của ensemble hiện tại.

## AdaBoost

AdaBoost tăng trọng số của những mẫu bị phân loại sai để learner tiếp theo chú ý chúng nhiều hơn.

```text
Mô hình 1 → tìm các mẫu bị sai
        ↓
tăng trọng số các mẫu khó
        ↓
Mô hình 2 → tập trung hơn vào lỗi
        ↓
bỏ phiếu có trọng số
```

Điểm quan trọng là các learner không còn hoàn toàn độc lập; mô hình sau phụ thuộc trực tiếp vào lỗi của mô hình trước.

## Gradient Boosting

Gradient Boosting có cách hiểu tổng quát hơn. Ở mỗi bước, learner mới được huấn luyện để xấp xỉ **gradient âm của hàm mất mát đối với prediction hiện tại**.

Với hồi quy squared error, gradient âm chính là phần dư:

\[
r_i=y_i-F_{m-1}(x_i)
\]

Tree mới học phần dư, rồi cập nhật:

\[
F_m(x)=F_{m-1}(x)+\eta h_m(x)
\]

`η` là learning rate hay hệ số co nhỏ (shrinkage).

Tên “Gradient Boosting” xuất phát từ việc quy trình này gần với gradient descent trong **không gian hàm (function space)** chứ không chỉ trong không gian tham số như neural network.

## XGBoost, LightGBM và CatBoost

Các implementation hiện đại bổ sung regularization, histogram-based split, xử lý song song, missing value và chiến lược cho categorical feature.

**XGBoost** nổi bật với objective có regularization và implementation rất tối ưu.

**LightGBM** sử dụng histogram và chiến lược phát triển cây hiệu quả để scale tốt trên dữ liệu bảng lớn.

**CatBoost** có nhiều kỹ thuật chuyên biệt cho categorical feature và giảm leakage khi dùng target statistics.

Không nên học ba công cụ này chỉ như API library. Chúng đều thuộc họ Gradient Boosted Decision Tree nhưng khác nhau ở thuật toán tối ưu và engineering system.

## Learning rate và số lượng tree

Learning rate nhỏ thường cần nhiều tree hơn.

Đây là sự đánh đổi giữa mức điều chỉnh nhỏ ở mỗi bước và số vòng boosting cần thiết.

Quá nhiều boosting round vẫn có thể overfit. Early stopping trên validation set là một kỹ thuật thực dụng quan trọng.

## Bagging và Boosting khác nhau thế nào?

| Khía cạnh | Bagging | Boosting |
|---|---|---|
| Mục tiêu chính | giảm variance | tiếp tục giảm bias/lỗi còn lại |
| Training | có thể song song | chủ yếu tuần tự |
| Mô hình điển hình | Random Forest | GBDT, XGBoost, LightGBM |
| Độ nhạy noise | thường bền hơn | có thể nhạy với outlier hoặc nhãn sai |
| Cơ chế | trung bình nhiều learner đa dạng | thêm learner để sửa lỗi hiện tại |

## Stacking

**Stacking** dùng prediction của nhiều base model làm input cho một meta-model.

```text
Linear model ─┐
Tree model   ─┼→ prediction ngoài fold → Meta model
Neural model ─┘
```

Điểm bắt buộc là meta-model nên train trên **out-of-fold prediction**. Nếu dùng prediction in-sample từ base model đã nhìn thấy target, leakage sẽ làm meta-model có đánh giá quá lạc quan.

## Ensemble và bất định

Mức độ bất đồng giữa các thành viên ensemble đôi khi cung cấp tín hiệu về **bất định nhận thức (epistemic uncertainty)**.

Deep ensemble huấn luyện nhiều neural network với initialization hoặc thứ tự dữ liệu khác nhau và thường tạo estimate bất định thực dụng khá tốt.

Tuy nhiên disagreement không tự động là uncertainty đã được calibration, đặc biệt nếu tất cả mô hình có cùng blind spot.

## Dữ liệu bảng và Deep Learning

Trong nhiều bài toán tabular có quy mô vừa, Gradient Boosted Tree vẫn rất cạnh tranh và đôi khi tốt hơn neural network tổng quát.

Điều này cho thấy “mô hình mới hơn” không đồng nghĩa “phù hợp hơn với mọi loại dữ liệu”.

Inductive bias của tree rất hợp với threshold, feature có scale khác nhau và interaction trong dữ liệu bảng.

## Mô hình tư duy

```text
Bagging  = nhiều mô hình đa dạng + trung bình hóa → ổn định hơn
Boosting = mô hình sau sửa lỗi mô hình trước → ensemble mạnh dần
Stacking = meta-model học cách phối hợp nhiều base model
```

## Các hiểu lầm thường gặp

### “Càng nhiều mô hình thì luôn càng tốt”

Không. Nếu các mô hình tương quan quá cao hoặc cùng mang một bias, lợi ích ensemble có thể rất nhỏ.

### “Random Forest chỉ là nhiều Decision Tree”

Chưa đủ. Random feature selection là thành phần quan trọng để làm các tree bớt tương quan.

### “Gradient Boosting train mọi tree trên target gốc”

Không. Tree sau được fit để cải thiện objective hiện tại, thường thông qua residual hoặc negative gradient.

### “Stacking chỉ cần lấy prediction rồi train thêm một model”

Không. Nếu không tạo out-of-fold prediction đúng cách, meta-model rất dễ bị leakage.

## Liên kết kiến thức

Ensemble Learning là ứng dụng trực tiếp của [Bias–Variance và Generalization](./14_bias_variance_and_generalization.md) và [Tối ưu hóa](../01_mathematical_foundations/06_optimization.md).

Xem tiếp: [Support Vector Machine](./10_support_vector_machines.md), một họ mô hình có inductive bias hình học rất khác.