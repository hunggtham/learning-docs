# Machine Learning là gì?

**Machine Learning (ML / 기계학습 / học máy)** nghiên cứu cách xây dựng hệ thống có thể cải thiện hiệu quả trên một nhiệm vụ bằng dữ liệu hoặc kinh nghiệm, thay vì lập trình viên phải mã hóa toàn bộ hành vi bằng các quy tắc cố định.

Điểm cốt lõi không phải là “máy tự học như con người”. Một hệ Machine Learning thường gồm họ mô hình (model family), tham số (parameters), hàm mục tiêu (objective), dữ liệu và quy trình tối ưu hóa. Trong quá trình huấn luyện (training), các tham số được điều chỉnh để mô hình nắm được cấu trúc thống kê trong dữ liệu. Khi triển khai, các tham số đã học được dùng để tạo dự đoán hoặc biểu diễn cho dữ liệu mới.

Machine Learning là một hướng tiếp cận lớn bên trong Trí tuệ nhân tạo, không đồng nghĩa với toàn bộ AI. Tìm kiếm, logic, lập kế hoạch và giải ràng buộc vẫn thuộc AI dù không nhất thiết học tham số từ dữ liệu.

Xem trước: [AI vs ML vs DL vs Generative AI](../00_foundations/05_ai_vs_ml_vs_dl_vs_generative_ai.md).

## Từ quy tắc viết tay tới ánh xạ được học

Lập trình truyền thống thường có dạng:

```text
Quy tắc + Đầu vào → Đầu ra
```

Machine Learning có giám sát thường có dạng:

```text
Dữ liệu huấn luyện + Đầu ra mong muốn
            ↓
        Thuật toán học
            ↓
        Mô hình đã học
            ↓
Đầu vào mới → Dự đoán
```

Ví dụ với bộ lọc thư rác. Một quy tắc kiểu `contains "free" → spam` rất dễ bị phá vỡ vì chỉ nhìn một tín hiệu đơn lẻ. Bộ phân loại có thể học cách kết hợp người gửi, phân phối token, liên kết, metadata và lịch sử gửi thư.

Tuy nhiên mô hình đã học vẫn chỉ là một thành phần phần mềm. Lập trình viên và nhóm sản phẩm vẫn phải quyết định cách thu thập dữ liệu, biến mục tiêu, đặc trưng hoặc biểu diễn, họ mô hình, hàm mục tiêu, cách đánh giá và chính sách triển khai.

## Một bài toán học hình thức

Trong học có giám sát, giả sử có tập dữ liệu:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Mô hình:

\[
f_\theta:X\rightarrow Y
\]

Dự đoán:

\[
\hat y=f_\theta(x)
\]

Quá trình huấn luyện tìm tham số:

\[
\theta^*=\arg\min_\theta \hat R(\theta)
\]

với rủi ro thực nghiệm (empirical risk):

\[
\hat R(\theta)=\frac{1}{n}\sum_i L(f_\theta(x_i),y_i)
\]

Tuy nhiên mục tiêu thật không phải ghi nhớ tập huấn luyện. Ta muốn rủi ro kỳ vọng thấp trên dữ liệu tương lai:

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P_{target}}[L(f_\theta(X),Y)]
\]

Khoảng cách giữa hiệu quả trên dữ liệu đã thấy và hiệu quả trên dữ liệu tương lai chính là vấn đề trung tâm của **khả năng khái quát hóa (generalization)**.

## Nhiệm vụ, kinh nghiệm và thước đo hiệu quả

Một cách định nghĩa cổ điển xem một chương trình là “học” từ kinh nghiệm `E` đối với nhiệm vụ `T` và thước đo `P` nếu hiệu quả trên `T`, đo bằng `P`, tăng lên nhờ `E`.

Khung này hữu ích vì buộc ta phải nói rõ:

```text
Task        → hệ thống phải làm gì?
Experience  → học từ dữ liệu hoặc tương tác nào?
Performance → tốt hay xấu được đo bằng gì?
```

Nếu ba yếu tố này còn mơ hồ thì câu “dùng Machine Learning” chưa phải là định nghĩa bài toán.

## Học có giám sát

Trong **học có giám sát (supervised learning)**, dữ liệu có nhãn mục tiêu.

Với hồi quy (regression):

\[
y\in\mathbb{R}
\]

Ví dụ gồm dự đoán giá, nhu cầu hoặc độ trễ.

Với phân loại (classification):

\[
y\in\{1,...,K\}
\]

Ví dụ gồm gian lận/không gian lận hoặc phân loại tài liệu.

Mô hình học mối quan hệ giữa đầu vào và mục tiêu.

## Học không giám sát

Trong **học không giám sát (unsupervised learning)**, không có nhãn mục tiêu rõ ràng như supervised learning.

Mục tiêu có thể là clustering, giảm chiều, ước lượng mật độ, học biểu diễn hoặc khám phá cấu trúc bất thường.

“Không giám sát” không có nghĩa mô hình không có hàm mục tiêu. Thuật toán vẫn tối ưu một tiêu chí cụ thể như lỗi tái tạo, likelihood hoặc mục tiêu clustering.

## Học tự giám sát

Trong **học tự giám sát (self-supervised learning)**, tín hiệu huấn luyện được tạo từ chính dữ liệu.

Ví dụ language modeling:

```text
các token trước đó → dự đoán token tiếp theo
```

Hoặc masked modeling:

```text
đầu vào bị che một phần → khôi phục nội dung bị thiếu
```

Contrastive learning tạo các cặp dương/âm từ phép biến đổi hoặc đồng xuất hiện.

Self-supervision cho phép học từ lượng dữ liệu thô rất lớn mà không cần con người gán nhãn từng mẫu. Foundation model hiện đại dựa mạnh vào mô hình huấn luyện này.

## Học bán giám sát

**Học bán giám sát (semi-supervised learning)** kết hợp một lượng nhỏ dữ liệu có nhãn với lượng lớn dữ liệu chưa gán nhãn.

Các phương pháp có thể dùng pseudo-label, consistency regularization, mô hình sinh hoặc pretraining biểu diễn.

Mục tiêu là tận dụng cấu trúc trong dữ liệu chưa gán nhãn mà không tin mù quáng vào các nhãn giả có thể sai.

## Reinforcement Learning

Trong Reinforcement Learning, tác nhân tương tác với môi trường và nhận phần thưởng thay vì nhận đáp án đúng cho từng hành động.

```text
trạng thái → hành động → chuyển trạng thái → phần thưởng
```

Các thách thức gồm phần thưởng trễ, exploration và dữ liệu phụ thuộc vào chính policy hiện tại.

Reinforcement Learning là một mô hình học khác với supervised learning thông thường và được tách thành folder riêng sau này.

## Học trực tuyến

Trong **học trực tuyến (online learning)**, mô hình cập nhật liên tục hoặc tuần tự khi dữ liệu mới đến.

Cách này hữu ích khi phân phối thay đổi hoặc dữ liệu đến theo luồng.

Các vấn đề cần xử lý gồm concept drift, thích nghi quá mức với dữ liệu mới, nhãn đến trễ và vòng phản hồi.

Online learning không đồng nghĩa với online inference. Một mô hình hoàn toàn có thể phục vụ request theo thời gian thực nhưng chỉ được huấn luyện lại theo batch.

## Học theo lô

Trong **học theo lô (batch learning)**, hệ thống huấn luyện trên một snapshot dữ liệu cố định, triển khai mô hình rồi tái huấn luyện định kỳ.

Cách này đơn giản hơn về vận hành và dễ tái lập hơn.

Nhiều hệ production vẫn sử dụng batch retraining dù inference diễn ra thời gian thực.

## Học dựa trên mẫu và học dựa trên mô hình

Phương pháp **dựa trên mẫu (instance-based)** giữ lại các mẫu huấn luyện và so sánh dữ liệu mới với những mẫu đã lưu, ví dụ k-NN.

Phương pháp **dựa trên mô hình (model-based)** học một tập tham số tóm tắt cấu trúc dữ liệu, ví dụ linear regression.

Sự đánh đổi có thể nhìn như:

```text
lưu nhiều dữ liệu và tính nhiều lúc inference
        so với
nén cấu trúc vào tham số trong quá trình training
```

## Parametric và Non-Parametric

Mô hình **tham số (parametric)** có số chiều tham số cố định không phụ thuộc trực tiếp vào số lượng mẫu, ví dụ linear regression.

Mô hình **phi tham số (non-parametric)** có độ phức tạp hiệu dụng có thể tăng khi dữ liệu tăng, ví dụ k-NN hoặc một số kernel method.

“Non-parametric” không có nghĩa là “không có tham số”; nó chỉ nói cấu trúc mô hình không bị giới hạn bởi một vector tham số hữu hạn cố định theo cùng cách như parametric model.

## Mô hình sinh và mô hình phân biệt

Mô hình phân biệt có thể học trực tiếp:

\[
P(Y\mid X)
\]

hoặc học ranh giới quyết định.

Mô hình sinh học phân phối chung:

\[
P(X,Y)
\]

hoặc `P(X)`.

Mô hình sinh có thể tạo mẫu mới và mô hình hóa biến ẩn hoặc dữ liệu thiếu, nhưng đôi khi phải giải một bài toán rộng hơn mức cần thiết nếu mục tiêu cuối chỉ là phân loại.

Thuật ngữ Generative AI hiện đại rộng hơn rất nhiều so với khái niệm “generative classifier” cổ điển.

## Biểu diễn là một phần của quá trình học

Thế giới thật phải được chuyển thành một dạng biểu diễn mà thuật toán xử lý được.

Machine Learning truyền thống thường có:

```text
dữ liệu thô → feature được thiết kế thủ công → mô hình
```

Deep Learning thường có:

```text
dữ liệu gần thô → biểu diễn được học → dự đoán
```

Feature engineering không biến mất. Hệ thống vẫn đưa ra nhiều quyết định về tokenization, normalization, aggregation, metadata và architecture.

## Tham số và siêu tham số

**Tham số (parameter)** được học từ dữ liệu huấn luyện, ví dụ trọng số, hệ số hoặc giá trị split của tree.

**Siêu tham số (hyperparameter)** được cấu hình bên ngoài vòng fitting chính, ví dụ learning rate, regularization strength, độ sâu cây, số neighbor hoặc lựa chọn kiến trúc.

Siêu tham số thường được lựa chọn bằng validation data. Nếu liên tục điều chỉnh dựa trên test set, test set sẽ không còn là phép đánh giá độc lập.

## Không gian giả thuyết

Họ mô hình xác định tập các hàm mà thuật toán có thể lựa chọn:

\[
\mathcal H=\{f_\theta:\theta\in\Theta\}
\]

Mô hình tuyến tính chỉ tìm trong các hàm có cấu trúc tuyến tính hoặc affine. Deep neural network định nghĩa một lớp hàm phong phú hơn rất nhiều.

Thuật toán học không tìm trong “mọi trí tuệ có thể có”; nó chỉ tìm trong không gian giả thuyết do kiến trúc, cách tham số hóa và optimizer cho phép.

## Thiên lệch quy nạp

Một tập dữ liệu hữu hạn có thể được giải thích bởi rất nhiều giả thuyết. Để khái quát hóa, hệ thống bắt buộc phải ưu tiên một số lời giải hơn các lời giải khác.

**Thiên lệch quy nạp (inductive bias / 귀납 편향)** có thể đến từ kiến trúc mô hình, regularization, optimizer, data augmentation, biểu diễn feature hoặc pretraining.

Không tồn tại quá trình học hoàn toàn không có giả định.

Xem thêm: [Bài toán học và thiên lệch quy nạp](./01_learning_problem_and_inductive_bias.md).

## Khả năng khái quát hóa

Mô hình có thể đạt hiệu quả gần như hoàn hảo trên training data nhưng kém trên dữ liệu tương lai.

**Overfitting** xảy ra khi mô hình học quá nhiều chi tiết đặc thù hoặc nhiễu của mẫu huấn luyện thay vì cấu trúc có thể tái sử dụng.

**Underfitting** xảy ra khi mô hình, biểu diễn hoặc quá trình tối ưu không đủ khả năng nắm cấu trúc cần thiết.

Khả năng khái quát hóa không chỉ phụ thuộc số lượng tham số. Quy mô và độ đa dạng dữ liệu, inductive bias, optimization, regularization và mức độ khớp giữa training distribution với deployment distribution đều quan trọng.

## Phân phối dữ liệu rất quan trọng

Dữ liệu huấn luyện thường được xem như lấy từ `P_train`, còn dữ liệu triển khai đến từ `P_deploy`.

Nếu:

\[
P_{train}\neq P_{deploy}
\]

thì phép đánh giá cũ có thể không còn đại diện cho thực tế.

“Accuracy của mô hình” không phải một thuộc tính phổ quát; nó luôn gắn với một population, khoảng thời gian và miền dữ liệu cụ thể.

## Dữ liệu được sinh ra bởi hệ thống

Dataset không phải bản chụp trung lập của thực tế. Nó phản ánh chính sách thu thập.

Ví dụ chỉ các khoản vay đã được phê duyệt mới có nhãn trả nợ; recommender chỉ quan sát phản hồi trên item đã hiển thị; nhãn fraud phụ thuộc quy trình điều tra; dữ liệu y tế phản ánh những người thật sự đi khám.

Những cơ chế này tạo selection bias và feedback loop.

## Hàm mất mát không phải mục tiêu ngoài đời thực

Quá trình huấn luyện cần một tín hiệu toán học có thể tối ưu, ví dụ cross-entropy.

Nhưng mục tiêu nghiệp vụ có thể là:

```text
giảm tổn thất do gian lận
đồng thời giữ trải nghiệm khách hàng tốt
```

Loss, metric và chính sách quyết định phải được nối với nhau cẩn thận.

Một mô hình xác suất có thể tốt nhưng threshold sai vẫn làm sản phẩm hoạt động tệ.

## Dự đoán và quyết định là hai lớp khác nhau

Mô hình có thể trả:

\[
P(fraud\mid x)=0.72
\]

Lớp quyết định sau đó chọn:

```text
phê duyệt
đưa vào kiểm tra thủ công
chặn
```

Quyết định cuối phụ thuộc vào chi phí, năng lực xử lý và chính sách.

Không nên nhét toàn bộ business logic vào mô hình nếu các quy tắc có thể được biểu diễn rõ và dễ kiểm toán hơn ở lớp ngoài.

## Tương quan và nhân quả

Machine Learning thường học mối liên hệ trong dữ liệu quan sát. Một feature dự đoán tốt một outcome không có nghĩa can thiệp vào feature đó sẽ làm outcome thay đổi theo cùng cách.

Ví dụ người dùng liên hệ support có thể có churn rate cao hơn. Điều đó không có nghĩa bắt người dùng liên hệ support sẽ làm churn tăng.

Nếu mục tiêu là chọn hành động làm thay đổi thế giới, causal reasoning có thể cần thiết.

## Data leakage

**Rò rỉ dữ liệu (data leakage)** xảy ra khi mô hình vô tình sử dụng thông tin tương lai hoặc thông tin từ target mà tại thời điểm dự đoán thực tế không có.

Khi đó metric training/test có thể rất đẹp nhưng triển khai thất bại.

Trong nhiều dự án, leakage nguy hiểm hơn cả việc chọn “sai thuật toán”.

Xem: [Dữ liệu, feature và label](./02_data_features_and_labels.md).

## Đánh giá là một phần của định nghĩa mô hình trong thực tế

Không thể nói một mô hình “tốt” nếu chưa xác định metric và population đánh giá.

Trong bài toán fraud mất cân bằng mạnh, accuracy 99,9% vẫn có thể chỉ là mô hình luôn dự đoán “không gian lận”.

Precision, recall, PR-AUC, expected cost và calibration có thể quan trọng hơn rất nhiều.

## Baseline

Trước khi dùng mô hình phức tạp, nên xây một baseline đơn giản như majority class, mean predictor, quy tắc thủ công hoặc linear/logistic regression.

Nếu hệ thống phức tạp chỉ tốt hơn baseline rất ít, chi phí vận hành tăng thêm có thể không đáng.

Baseline cũng là công cụ phát hiện lỗi pipeline. Nếu mô hình phức tạp còn tệ hơn một phương án rất đơn giản, cần kiểm tra dữ liệu và target trước khi tối ưu thuật toán.

## Trực giác No Free Lunch

Không có thuật toán nào tốt nhất trên mọi quá trình sinh dữ liệu có thể có.

Một thuật toán thành công vì thiên lệch của nó phù hợp với cấu trúc thật của bài toán.

Vì vậy lựa chọn mô hình nên hỏi:

> Những giả định nào về dữ liệu và ranh giới quyết định là hợp lý trong bài toán này?

thay vì chỉ hỏi “thuật toán nào mạnh nhất?”.

## Machine Learning như quá trình nén kinh nghiệm

Huấn luyện có thể được nhìn như quá trình nén cấu trúc thống kê từ dữ liệu vào tham số và biểu diễn.

Sự nén này tất nhiên làm mất chi tiết và mang theo thiên lệch. Mô hình không phải một cơ sở dữ liệu hoàn hảo của training set, dù hiện tượng ghi nhớ dữ liệu vẫn có thể xảy ra.

Mô hình tư duy này giúp phân biệt tri thức nằm trong tham số với tri thức được truy xuất từ database hoặc RAG.

## Vòng đời Machine Learning

Một hệ ML production thường có dòng xử lý:

```text
định nghĩa bài toán
→ thu thập dữ liệu
→ validation / chia tập
→ feature / representation
→ training
→ evaluation
→ decision policy
→ deployment
→ monitoring
→ thu thập feedback
→ retraining / sửa thiết kế
```

Huấn luyện chỉ là một giai đoạn trong cả hệ thống.

## Khi không nên dùng Machine Learning

Nên ưu tiên phần mềm xác định khi quy tắc chính xác và ổn định, đầu ra phải bảo đảm đúng, không có dữ liệu đại diện, một threshold đơn giản đã đủ hoặc hậu quả sai quá cao mà không có lớp kiểm chứng.

Ví dụ công thức tính thuế nên được thực hiện bằng code hoặc rule chính xác. ML có thể hỗ trợ phân loại giấy tờ hoặc phát hiện bất thường xung quanh hệ thống đó, nhưng không nên thay thế phép tính đã có công thức rõ ràng.

## Mô hình tư duy

```text
Data        = kinh nghiệm quan sát được
Model       = họ các ánh xạ có thể chọn
Parameters  = trạng thái được học của mô hình
Loss        = tín hiệu dùng trong training
Optimizer   = cơ chế điều chỉnh tham số
Bias        = giả định dùng để ưu tiên một số lời giải
Generalization = hành vi hữu ích trên dữ liệu mục tiêu chưa thấy
Evaluation  = bằng chứng rằng hệ thống phù hợp với mục đích sử dụng
```

## Các hiểu lầm thường gặp

### “ML tự tìm quy luật nên không cần domain knowledge”

Không. Domain knowledge ảnh hưởng trực tiếp cách định nghĩa target, sampling, feature, constraint và evaluation. Một bài toán được định nghĩa sai không thể được cứu chỉ bằng mô hình mạnh hơn.

### “Training accuracy càng cao thì mô hình càng tốt”

Không. Khả năng fit dữ liệu huấn luyện có thể tiếp tục tăng trong khi generalization giảm.

### “Deep Learning đã thay thế classical ML”

Không. Bài toán dữ liệu bảng, ít dữ liệu hoặc yêu cầu latency thấp vẫn thường phù hợp với tree, linear model hoặc kiến trúc lai.

### “Unsupervised learning không có label nên mô hình tự hiểu dữ liệu”

Không. Thuật toán vẫn có objective và inductive bias xác định loại cấu trúc nào được xem là hữu ích.

## Liên kết kiến thức

Machine Learning là nơi [Thống kê](../01_mathematical_foundations/03_statistics_for_ai.md), [Tối ưu hóa](../01_mathematical_foundations/06_optimization.md) và thiết kế biểu diễn gặp nhau. Các chương tiếp theo sẽ làm rõ bài toán học trước khi đi vào từng thuật toán cụ thể.

Xem tiếp: [Bài toán học và thiên lệch quy nạp](./01_learning_problem_and_inductive_bias.md).