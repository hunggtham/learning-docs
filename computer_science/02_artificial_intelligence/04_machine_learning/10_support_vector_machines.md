# Support Vector Machine: biên, hình học và kernel

**Support Vector Machine (SVM / 서포트 벡터 머신)** xây dựng bộ phân loại dựa trên một nguyên lý hình học: không chỉ tìm một siêu phẳng (hyperplane) tách các lớp, mà tìm siêu phẳng có **biên an toàn (margin)** lớn. Margin là khoảng cách giữa ranh giới quyết định và những điểm huấn luyện gần ranh giới nhất.

SVM quan trọng không chỉ vì bản thân thuật toán. Nó giúp hiểu rõ regularization, tối ưu lồi, đối ngẫu (duality), kernel và hình học của không gian biểu diễn.

## Từ siêu phẳng phân tách tới margin

Bộ phân loại nhị phân có dạng:

\[
f(x)=\mathbf w^T\mathbf x+b
\]

Ranh giới quyết định:

\[
\mathbf w^T\mathbf x+b=0
\]

Với nhãn `y∈{-1,+1}`, nếu dữ liệu phân tách tuyến tính được, ta muốn:

\[
y_i(\mathbf w^T\mathbf x_i+b)\ge1
\]

Margin hình học tỷ lệ nghịch với norm của trọng số:

\[
margin=\frac{2}{\|\mathbf w\|}
\]

Do đó tối đa hóa margin tương đương tối thiểu hóa:

\[
\frac12\|\mathbf w\|^2
\]

với các ràng buộc phân loại tương ứng.

## Vì sao margin có ý nghĩa?

Nếu có nhiều ranh giới đều phân loại hoàn hảo training set, ranh giới nằm quá sát các điểm dữ liệu dễ đổi prediction chỉ vì đầu vào bị nhiễu nhẹ.

Ranh giới có margin lớn tạo vùng đệm rộng hơn.

Đây là một **thiên lệch quy nạp (inductive bias)** hướng tới độ bền và khả năng khái quát hóa tốt hơn.

## Support Vector

Chỉ một số điểm nằm trên hoặc bên trong margin ảnh hưởng trực tiếp mạnh nhất tới nghiệm tối ưu. Chúng được gọi là **vector hỗ trợ (support vector / 서포트 벡터)**.

Các điểm nằm rất xa ranh giới thường không còn ảnh hưởng tới nghiệm sau khi ràng buộc của chúng đã được thỏa mãn.

Tên “Support Vector Machine” xuất phát từ chính việc ranh giới được “đỡ” bởi những mẫu quan trọng này.

## Soft Margin

Dữ liệu thực tế thường không thể phân tách hoàn hảo. Ta thêm biến nới lỏng (slack variable) `ξ_i`:

\[
y_i(\mathbf w^T\mathbf x_i+b)\ge1-\xi_i,\qquad \xi_i\ge0
\]

Hàm mục tiêu:

\[
\min_{w,b,\xi}\frac12\|w\|^2+C\sum_i\xi_i
\]

`C` điều khiển sự đánh đổi:

- `C` lớn: phạt mạnh các vi phạm margin hoặc lỗi phân loại, cố fit training data hơn;
- `C` nhỏ: chấp nhận thêm vi phạm để giữ margin rộng hơn.

Đây chính là một dạng regularization trade-off.

## Hinge Loss

Soft-margin SVM có thể viết gần với bài toán empirical risk có regularization:

\[
J(w)=\frac12\|w\|^2+C\sum_i\max(0,1-y_if(x_i))
\]

**Hinge loss** bằng 0 khi mẫu không chỉ được phân loại đúng mà còn nằm ngoài margin yêu cầu.

## Chuẩn hóa feature

SVM phụ thuộc vào dot product và hình học của feature space, vì vậy scale của feature rất quan trọng.

Một feature có độ lớn lớn hơn nhiều có thể chi phối toàn bộ geometry.

Standardization vì thế thường là bước tiền xử lý mặc định khi dùng SVM.

## Kernel Trick

Nếu các lớp không thể phân tách tuyến tính trong không gian gốc, ta có thể ánh xạ đầu vào qua một phép biến đổi phi tuyến:

\[
\phi(x)
\]

rồi học một ranh giới tuyến tính trong không gian mới.

Dạng đối ngẫu của SVM phụ thuộc vào các tích vô hướng:

\[
\phi(x_i)^T\phi(x_j)
\]

Nếu có một hàm kernel:

\[
K(x_i,x_j)=\phi(x_i)^T\phi(x_j)
\]

thì không cần tính trực tiếp toàn bộ tọa độ của `φ(x)`. Đây là **kernel trick**.

RBF kernel:

\[
K(x,z)=\exp(-\gamma\|x-z\|^2)
\]

cho phép tạo ranh giới phi tuyến rất linh hoạt.

## Kernel không phải bất kỳ hàm similarity nào

Một kernel hợp lệ phải thỏa các tính chất để có thể được diễn giải như tích vô hướng trong một không gian feature, thường liên quan tới ma trận Gram bán xác định dương (positive semidefinite).

Vì vậy không phải bất kỳ hàm similarity tự chế nào cũng có thể thay vào kernel mà vẫn giữ các bảo đảm lý thuyết và tính chất tối ưu hóa.

## C và gamma

Với RBF SVM:

- `C` điều khiển mức phạt lỗi và vi phạm margin;
- `γ` điều khiển mức độ cục bộ của kernel.

`γ` quá lớn làm ảnh hưởng của mỗi điểm rất hẹp, tạo ranh giới phức tạp và variance cao.

`γ` quá nhỏ làm ảnh hưởng trải quá rộng, tạo mô hình quá mượt và bias cao.

Các hyperparameter này nên được chọn bằng validation đúng cách, đặc biệt khi có nested search để tránh optimistic bias.

## Khả năng mở rộng tính toán

Kernel SVM cần tính hoặc sử dụng quan hệ theo cặp giữa các mẫu training, nên thời gian và bộ nhớ có thể tăng rất mạnh theo `n`.

Vì vậy kernel SVM thường phù hợp hơn với dataset nhỏ hoặc vừa. Với dữ liệu rất lớn, linear SVM, approximate kernel hoặc họ mô hình khác thường thực tế hơn.

## SVM và Logistic Regression

Nếu dùng raw linear feature, cả hai đều có ranh giới quyết định tuyến tính.

Logistic Regression tối ưu log-loss theo cách diễn giải xác suất và trực tiếp tạo xác suất mô hình.

SVM tối ưu margin và hinge loss; score thô của SVM không phải xác suất đã hiệu chuẩn.

Nếu cần probability, có thể calibration SVM bằng Platt scaling hoặc isotonic regression trên held-out data.

## Kernel và Representation Learning

Kernel method mã hóa nonlinear similarity bằng một kernel được chọn trước.

Deep Learning học trực tiếp một phép biến đổi:

\[
\phi_\theta(x)
\]

Từ góc nhìn này, neural network có thể được xem là học feature space rồi dùng một output head tương đối đơn giản phía sau.

Khác biệt lớn là feature map trong Deep Learning được học cùng task, còn kernel thường được cố định hoặc xác định trước.

## Mô hình tư duy

> SVM hỏi: trong số các ranh giới có thể phân loại dữ liệu, ranh giới nào giữ khoảng cách an toàn lớn nhất với những mẫu quan trọng nhất?

Kernel mở rộng cùng ý tưởng sang một không gian feature phi tuyến mà ta không nhất thiết phải biểu diễn trực tiếp.

## Các hiểu lầm thường gặp

### “Support vector là mọi điểm gần boundary”

Không chính xác. Theo bài toán tối ưu, support vector là các điểm có dual coefficient khác 0 và thực sự hoạt động trong nghiệm cuối.

### “SVM luôn tốt cho dữ liệu nhiều chiều”

Linear SVM thường rất mạnh với dữ liệu sparse nhiều chiều như văn bản, nhưng kernel SVM có vấn đề scaling theo số lượng mẫu.

### “Kernel trick giống một hidden layer neural”

Hai cơ chế đều tạo khả năng phi tuyến, nhưng kernel map thường cố định hoặc ngầm định, còn neural representation được học từ dữ liệu.

### “SVM score là xác suất”

Không. Margin score cần được calibration nếu muốn diễn giải theo xác suất.

## Liên kết kiến thức

SVM nối [Tối ưu hóa](../01_mathematical_foundations/06_optimization.md), [Đại số tuyến tính](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Bias–Variance](./14_bias_variance_and_generalization.md).

Xem tiếp: [Clustering](./11_clustering.md), nơi không còn label để trực tiếp xác định ranh giới phân loại.