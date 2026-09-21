# Suy luận dữ liệu, khớp mô hình và bài toán ngược trong Vật lý

## Phép đo không kết thúc khi có một con số

Detector có thể tạo điện áp, số đếm, phổ hoặc ảnh. Nhưng câu hỏi vật lý thường liên quan tới đại lượng không quan sát trực tiếp như:

- khối lượng;
- thời gian sống;
- hệ số khuếch tán;
- nhiệt độ;
- cường độ trường;
- phân bố nguồn;
- tham số của mô hình.

Suy luận thống kê (statistical inference / 통계적 추론) là quá trình đi từ dữ liệu và mô hình thuận tới phát biểu có định lượng về tham số hoặc mô hình.

Không tồn tại suy luận hoàn toàn “không mô hình”. Ngay cả phép lấy trung bình cũng giả sử các mẫu đang đo cùng một đại lượng có ý nghĩa và có cấu trúc thống kê phù hợp.

## Luôn bắt đầu bằng mô hình thuận

Một mô hình đơn giản có thể viết

```math
y_i=f(x_i;\theta)+\epsilon_i.
```

Trong đó:

- `\theta` là tham số cần suy ra;
- `f` là mô hình vật lý;
- `\epsilon_i` biểu diễn nhiễu đo và/hoặc sai khác mô hình.

Mô hình thuận (forward model) trả lời:

> nếu tham số thật là `\theta`, thiết bị sẽ tạo dữ liệu có phân bố như thế nào?

Bài toán ngược (inverse problem) hỏi hướng ngược lại:

> dữ liệu đã quan sát cho phép suy ra gì về `\theta` hoặc nguồn ẩn?

Nếu forward model sai, optimizer tốt đến đâu cũng chỉ tìm tham số tốt nhất cho một mô hình sai.

## Least squares xuất hiện từ giả định nhiễu Gaussian

Nếu sai số độc lập Gaussian với độ lệch chuẩn đã biết `\sigma_i`, likelihood có dạng

```math
p(y|\theta)
\propto
\exp\left[
-\frac12
\sum_i
\frac{(y_i-f_i(\theta))^2}{\sigma_i^2}
\right].
```

Tối đa hóa likelihood tương đương tối thiểu hóa

```math
\chi^2
=\sum_i
\frac{(y_i-f_i(\theta))^2}{\sigma_i^2}.
```

Vì vậy least squares không phải “phương pháp mặc định luôn đúng”. Nó xuất hiện tự nhiên khi mô hình nhiễu Gaussian phù hợp.

Nếu dữ liệu là số đếm Poisson, có outlier đuôi nặng hoặc có tương quan, loss function phù hợp sẽ khác.

## Sai số có tương quan và ma trận covariance

Nếu các phép đo có sai số tương quan, cần dùng ma trận covariance `C`:

```math
\chi^2
=(\mathbf y-\mathbf f)^T
C^{-1}
(\mathbf y-\mathbf f).
```

Bỏ qua correlation có thể:

- đánh giá thấp uncertainty;
- gán trọng số sai cho dữ liệu;
- làm tham số bị bias.

Sai số hiệu chuẩn chung là ví dụ điển hình tạo correlation giữa nhiều điểm dữ liệu.

## Độ bất định của tham số và độ cong likelihood

Gần nghiệm tốt nhất, nếu log-likelihood gần parabol, ta có thể xấp xỉ posterior hoặc likelihood bằng Gaussian.

Hessian của negative log-likelihood mô tả độ cong cục bộ. Nghịch đảo Hessian thường cho xấp xỉ covariance của tham số.

Tuy nhiên xấp xỉ này có thể thất bại khi:

- posterior lệch mạnh;
- có nhiều mode;
- tham số bị chặn bởi biên vật lý;
- mô hình phi tuyến mạnh;
- tồn tại degeneracy dài và cong.

Khi đó cần profile likelihood, bootstrap, Markov Chain Monte Carlo hoặc phương pháp sampling khác.

## Suy luận Bayes

Định lý Bayes là

```math
p(\theta|D)
=\frac{p(D|\theta)p(\theta)}{p(D)}.
```

Trong đó:

- `p(D|\theta)` là likelihood từ mô hình đo;
- `p(\theta)` là prior;
- `p(\theta|D)` là posterior;
- `p(D)` là evidence chuẩn hóa.

Prior không phải giấy phép để đưa ý kiến tùy ý vào kết quả. Nó phải có lý do, được khai báo rõ và nên được kiểm tra độ nhạy.

Khi dữ liệu yếu, prior có thể ảnh hưởng đáng kể. Khi dữ liệu rất mạnh, likelihood thường chi phối nhiều hơn.

## Identifiability: dữ liệu có thật sự phân biệt được tham số không?

Một mô hình có thể khớp dữ liệu rất đẹp nhưng tham số vẫn không nhận dạng được duy nhất.

Ví dụ nếu đầu ra chỉ phụ thuộc tích

```math
ab,
```

thì từ một loại phép đo ta có thể không tách được `a` và `b` riêng lẻ.

Tính nhận dạng cục bộ liên hệ với ma trận độ nhạy hoặc Jacobian. Nếu hai cột gần phụ thuộc tuyến tính, hai tham số tạo degeneracy.

Thiết kế thí nghiệm tốt không chỉ nhằm giảm noise; nó chọn điều kiện đo sao cho các tham số ảnh hưởng dữ liệu theo những hướng khác nhau, phá degeneracy.

## Bài toán ngược ill-posed

Một bài toán ngược bị coi là không chỉnh (ill-posed) khi một trong các tính chất sau thất bại:

- nghiệm tồn tại;
- nghiệm duy nhất;
- nghiệm phụ thuộc ổn định vào dữ liệu.

Deconvolution ảnh, tomography và nhiều bài toán dựng nguồn là ví dụ điển hình.

Với hệ tuyến tính

```math
A\mathbf x=\mathbf y,
```

nếu `A` có singular value rất nhỏ, phép nghịch đảo trực tiếp sẽ khuếch đại mạnh thành phần noise theo các hướng tương ứng.

## Regularization

Tikhonov regularization giải bài toán kiểu

```math
\min_x
\|Ax-y\|^2
+\lambda\|Lx\|^2.
```

Hạng đầu buộc nghiệm khớp dữ liệu. Hạng thứ hai đưa vào giả định như:

- nghiệm nhỏ;
- nghiệm trơn;
- đạo hàm nhỏ;
- cấu trúc vật lý đã biết.

`\lambda` điều khiển đánh đổi giữa khớp dữ liệu và độ ổn định.

Regularization không phục hồi thông tin đã mất một cách thần kỳ. Nó thêm cấu trúc tiên nghiệm để chọn một nghiệm ổn định trong tập nghiệm còn phù hợp với dữ liệu nhiễu.

## Singular Value Decomposition

Phân rã SVD là

```math
A=U\Sigma V^T.
```

Các singular value nhỏ tương ứng với những hướng trong không gian tham số mà dữ liệu gần như không ràng buộc được.

SVD vì vậy là công cụ quan trọng để chẩn đoán:

- ill-conditioning;
- parameter degeneracy;
- multicollinearity;
- độ phân giải thực của bài toán ngược.

## Chọn mô hình và overfitting

Thêm tham số thường giúp giảm residual trên tập dữ liệu đã dùng để fit. Nhưng câu hỏi khoa học là:

> cải thiện đó có đủ để biện minh cho độ phức tạp tăng thêm không?

Các công cụ như AIC, BIC, likelihood-ratio test, cross-validation hoặc Bayesian evidence có giả định khác nhau.

Không tồn tại một quy tắc “score lớn nhất chính là mô hình thật”. Chọn mô hình phải cân bằng:

- khả năng mô tả dữ liệu;
- năng lực dự đoán dữ liệu mới;
- độ phức tạp;
- khả năng diễn giải vật lý.

## Phân tích residual

Sau khi fit,

```math
r_i=y_i-f_i(\hat\theta).
```

Residual nên được kiểm tra theo:

- thời gian;
- vị trí;
- tần số;
- nhiệt độ;
- cường độ;
- các biến điều khiển khác.

Pattern có cấu trúc trong residual thường là dấu hiệu:

- thiếu physics;
- calibration sai;
- noise model sai;
- correlation chưa được mô hình hóa.

Reduced chi-square gần 1 không tự động chứng minh mô hình đúng. Một mô hình sai với uncertainty bị thổi phồng cũng có thể cho chỉ số đẹp.

## Detection significance và look-elsewhere effect

Nếu quét hàng nghìn tần số, vị trí hoặc khối lượng để tìm peak, xác suất có ít nhất một fluctuation lớn tăng lên so với một phép thử duy nhất.

Đây là look-elsewhere effect.

Khi báo significance phải xét số lượng và correlation giữa các phép thử.

P-value cũng không phải xác suất giả thuyết null là đúng. Nó là xác suất thu được statistic ít nhất cực đoan như quan sát nếu giả thuyết null và các giả định mô hình là đúng.

## Khớp tham số không đồng nghĩa với suy luận nhân quả

Một correlation tốt hoặc model fit tốt không tự chứng minh quan hệ nhân quả.

Trong phòng thí nghiệm, intervention, randomization và control condition giúp tách confounder.

Trong thiên văn hoặc địa vật lý quan sát, không thể tùy ý can thiệp vào hệ. Khi đó lập luận nhân quả cần dựa trên:

- mô hình cơ chế;
- nhiều dấu hiệu độc lập;
- natural experiment;
- dự đoán có thể kiểm tra thêm.

## Simulation-based inference

Một số mô hình thuận dễ mô phỏng nhưng likelihood gần như không thể viết hoặc tính trực tiếp.

Các phương pháp như Approximate Bayesian Computation, neural density estimation hoặc likelihood-free inference dùng simulation để học quan hệ giữa tham số và dữ liệu.

Machine learning có thể rất mạnh, nhưng assumption không biến mất. Chúng chuyển sang:

- simulator;
- prior;
- training distribution;
- architecture;
- preprocessing;
- calibration của mô hình học máy.

Nếu simulator không đại diện đúng thế giới thật, inference có thể rất chính xác về mặt số nhưng sai về vật lý.

## Ví dụ: đo thời gian sống của quá trình phân rã

Giả sử số hạt kỳ vọng giảm theo

```math
N(t)=N_0e^{-t/\tau}.
```

Một cách đơn giản là lấy `\ln N` rồi fit đường thẳng. Nhưng nếu dữ liệu thật là số đếm Poisson và có bin bằng 0, phép biến đổi log làm thay đổi cấu trúc noise.

Một mô hình tốt hơn là

```math
n_i\sim\mathrm{Poisson}(\mu_i),
```

với

```math
\mu_i
=N_0e^{-t_i/\tau}+b.
```

Sau đó fit trực tiếp `N_0`, `\tau` và background `b` bằng likelihood Poisson.

Bài học là: **mô hình thống kê phải đi theo cơ chế tạo dữ liệu**, không chỉ theo phép biến đổi đại số thuận tiện.

## Ví dụ: deconvolution ảnh

Giả sử ảnh đo được là

```math
\mathbf y=A\mathbf x+\boldsymbol\epsilon,
```

trong đó `A` mô tả point-spread function và sampling.

Nếu một số tần số không gian bị hệ quang học triệt tiêu mạnh, `A` gần mất hạng ở các hướng đó. Nghịch đảo trực tiếp làm noise bùng lên.

Regularization có thể ưu tiên nghiệm trơn hoặc sparse, nhưng kết quả cuối phản ánh cả dữ liệu và prior. Đây là lý do thuật toán sharpen không thể tạo lại duy nhất thông tin mà hệ quang học chưa từng ghi nhận.

## Độ bất định phải được truyền qua pipeline

Một pipeline vật lý thường có dạng

```text
raw signal
→ calibration
→ preprocessing
→ feature extraction
→ model fit
→ derived quantity
```

Uncertainty ở bước đầu có thể lan truyền, tương quan và biến dạng qua các phép biến đổi phi tuyến.

Do đó không nên chỉ gắn error bar ở cuối. Cần theo dõi covariance hoặc sampling uncertainty xuyên suốt pipeline khi nó có ảnh hưởng đáng kể.

## Reproducibility

Một kết quả inference cần đi cùng:

- nguồn và phiên bản dữ liệu;
- calibration;
- phương trình mô hình;
- assumption;
- likelihood hoặc loss;
- prior hoặc regularization;
- phiên bản code;
- uncertainty và covariance của tham số;
- residual/validation checks.

Một con số best-fit không có provenance và uncertainty rất khó audit khoa học.

## Miền áp dụng và giới hạn

Least squares chuẩn giả sử cấu trúc error phù hợp. Hessian approximation chỉ đáng tin khi posterior gần Gaussian quanh nghiệm.

Bayesian posterior chỉ có ý nghĩa trong mô hình đã chỉ định; nếu likelihood hoặc forward model sai, posterior vẫn có thể hẹp nhưng sai.

Regularization cải thiện ổn định bằng cách thêm thông tin hoặc constraint. Nó không loại bỏ tính không xác định cơ bản của dữ liệu.

## Mô hình tư duy (Mental Model)

Dữ liệu không trực tiếp “nói tham số bằng bao nhiêu”. Quan sát đi qua nhiều lớp:

```text
physical system
→ forward process
→ detector
→ calibration
→ noise
→ recorded data
```

Inference cố đi ngược chuỗi này:

```text
data
→ likelihood + model
→ parameter distribution
→ physical interpretation
```

Một inference tốt phải giữ lại uncertainty, degeneracy và model assumptions thay vì ép mọi thứ thành một con số duy nhất.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Fit đẹp nghĩa lý thuyết đúng”

Không. Nhiều mô hình có thể fit cùng một dataset hữu hạn. Prediction mới, residual và phép thử độc lập quan trọng hơn.

### “Regularization làm nghiệm khách quan hơn”

Không. Regularization thêm giả định. Nó giúp ổn định nhưng phải được báo cáo và kiểm tra độ nhạy.

### “Machine learning loại bỏ nhu cầu về mô hình vật lý”

Không. Assumption chuyển sang dữ liệu huấn luyện, simulator, architecture và preprocessing.

### “Error bar nhỏ nghĩa kết quả chắc chắn đúng”

Không. Error bar có thể chỉ phản ánh uncertainty bên trong một mô hình; systematic error hoặc model discrepancy có thể lớn hơn nhiều.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Phép đo và độ bất định](00_measurement_experiment.md), [Tín hiệu và lấy mẫu](01_signals_sampling_noise.md), [Vật lý tính toán](02_computational_physics.md).

**Liên hệ tiếp:** [Quang học Fourier và bài toán tạo ảnh](../06_optics/04_fourier_imaging_instrumentation.md), [Thiên văn quan sát](../11_astrophysics_cosmology/02_observational_astrophysics_radiative_transfer.md), [Vũ trụ sơ khai](../11_astrophysics_cosmology/03_early_universe_dark_components.md), [Các liên kết kiến thức](../13_connections/00_knowledge_connections.md).
