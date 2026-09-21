# Thống kê cho Trí tuệ nhân tạo

**Thống kê (Statistics / 통계학)** giải quyết một mâu thuẫn nằm ở trung tâm của học máy: ta chỉ quan sát một **mẫu hữu hạn (finite sample)** nhưng lại muốn mô hình hoạt động tốt trên dữ liệu chưa từng thấy. Tập huấn luyện không phải toàn bộ thế giới; nó chỉ là một mẫu được thu thập theo một quy trình cụ thể, trong một khoảng thời gian cụ thể, với sai số đo lường, thiên lệch lựa chọn và thông tin bị thiếu.

Vì vậy thống kê trong AI không chỉ là “trung bình, trung vị và biểu đồ”. Nó cung cấp khung để hỏi: dữ liệu đến từ đâu, ước lượng đáng tin tới mức nào, mô hình có khái quát hóa không, chênh lệch chỉ số có thực sự có ý nghĩa không, và khi phân phối triển khai thay đổi thì kết luận cũ còn đúng đến đâu.

Xem trước: [Xác suất cho AI](./02_probability_for_ai.md).

## Quần thể, mẫu và quá trình sinh dữ liệu

**Quần thể (population / 모집단)** là tập hoặc quá trình ta thực sự quan tâm. **Mẫu (sample / 표본)** là phần dữ liệu quan sát được.

Trong học máy, cách nhìn mạnh hơn là giả sử tồn tại một phân phối sinh dữ liệu chưa biết:

\[
(X,Y)\sim P_{data}
\]

Ta chỉ quan sát tập dữ liệu:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Nếu các mẫu thực sự **độc lập và cùng phân phối (independent and identically distributed - i.i.d.)** từ `P_data`, nhiều công cụ thống kê hoạt động khá thuận lợi. Tuy nhiên dữ liệu production thường vi phạm giả định này: sự kiện của cùng người dùng có tương quan theo thời gian, chính sách gợi ý ảnh hưởng dữ liệu được thu thập, kẻ gian thích nghi với bộ phát hiện, hoặc nhật ký chỉ chứa những người đã đi qua một bộ lọc trước đó.

Do đó, trước mọi suy luận thống kê cần hỏi: **quy trình lấy mẫu là gì?**

## Thống kê mô tả: hiểu dữ liệu trước khi xây mô hình

Trung bình:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

mô tả tâm dữ liệu theo trung bình số học nhưng nhạy với ngoại lệ.

Trung vị là phân vị 50%, bền vững hơn trước các giá trị cực đoan.

Phương sai mẫu:

\[
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
\]

đo mức phân tán. Việc dùng `n-1` thay vì `n` giúp tạo ước lượng không chệch cho phương sai quần thể dưới các giả định chuẩn.

Các phân vị giúp hiểu phần đuôi của phân phối. Trong giám sát độ trễ, p50, p95 và p99 thường hữu ích hơn trung bình vì trải nghiệm người dùng có thể bị chi phối bởi độ trễ đuôi.

Thống kê mô tả chỉ mô tả mẫu đã quan sát; nó không tự suy ra quan hệ nhân quả hoặc hiệu năng tương lai.

## Bộ ước lượng và giá trị ước lượng

Một **bộ ước lượng (estimator / 추정량)** là quy tắc hoặc hàm dùng mẫu để ước lượng đại lượng chưa biết của quần thể. Kết quả cụ thể từ một tập dữ liệu là **giá trị ước lượng (estimate / 추정값)**.

Ví dụ, trung bình mẫu `\bar X` là bộ ước lượng của trung bình quần thể `μ`.

Ta có thể đánh giá bộ ước lượng bằng nhiều thuộc tính.

**Độ chệch (bias)**:

\[
Bias(\hat\theta)=\mathbb{E}[\hat\theta]-\theta
\]

**Phương sai (variance)**:

\[
Var(\hat\theta)
\]

**Sai số bình phương trung bình (Mean Squared Error - MSE)**:

\[
MSE(\hat\theta)=Bias(\hat\theta)^2+Var(\hat\theta)
\]

Đánh đổi độ chệch–phương sai ở mức bộ ước lượng liên hệ trực tiếp với đánh đổi bias–variance trong học máy.

## Luật số lớn

**Luật số lớn (Law of Large Numbers)** nói rằng, dưới các điều kiện phù hợp, trung bình mẫu hội tụ về giá trị kỳ vọng khi kích thước mẫu tăng.

Đây là lý do nhiều ước lượng thực nghiệm ổn định hơn khi có nhiều dữ liệu.

Tuy nhiên, “nhiều dữ liệu” không tự sửa được thiên lệch lấy mẫu. Nếu quy trình lựa chọn mẫu bị sai, một tỷ bản ghi thiên lệch vẫn có thể ước lượng sai quần thể mục tiêu với độ chính xác rất cao.

> **Nhiều dữ liệu giúp giảm sai số ngẫu nhiên; nó không tự loại bỏ thiên lệch có hệ thống.**

## Định lý Giới hạn Trung tâm

**Định lý Giới hạn Trung tâm (Central Limit Theorem - CLT / 중심극한정리)** giải thích vì sao phân phối của trung bình mẫu đã chuẩn hóa thường tiến gần phân phối Gaussian khi kích thước mẫu lớn và các điều kiện phù hợp được thỏa mãn, ngay cả khi từng quan sát riêng lẻ không có phân phối Gaussian.

Đây là nền cho sai số chuẩn và nhiều khoảng tin cậy.

Tuy nhiên CLT không phải lý do để giả định mọi phân phối trong học máy đều Gaussian. Đuôi dày, phụ thuộc mạnh hoặc mẫu nhỏ có thể khiến xấp xỉ kém.

## Sai số chuẩn

Độ lệch chuẩn mô tả mức phân tán của các quan sát. **Sai số chuẩn (standard error)** mô tả độ bất định của bộ ước lượng.

Với trung bình mẫu và dữ liệu i.i.d.:

\[
SE(\bar X)=\frac{s}{\sqrt{n}}
\]

Nếu kích thước mẫu tăng 4 lần, sai số chuẩn giảm xấp xỉ 2 lần chứ không phải 4 lần.

Trong đánh giá mô hình, một chỉ số được tính trên 100 mẫu và cùng chỉ số đó trên 100.000 mẫu không nên được tin như nhau dù giá trị điểm giống hệt.

## Khoảng tin cậy

**Khoảng tin cậy (confidence interval)** được xây bằng một thủ tục có thuộc tính bao phủ xác định.

Xấp xỉ khoảng 95% cho trung bình trong trường hợp mẫu lớn:

\[
\bar{x}\pm1.96\,SE
\]

Một hiểu lầm phổ biến là nói “có 95% xác suất trung bình thật nằm trong khoảng đã tính”. Trong cách diễn giải tần suất cổ điển, tham số được xem là cố định; chính thủ tục tạo khoảng mới có tỷ lệ bao phủ dài hạn 95% dưới các giả định.

Trong AI thực tế, điểm quan trọng là **báo cáo độ bất định thay vì chỉ báo cáo một ước lượng điểm**.

## Kiểm định giả thuyết

**Kiểm định giả thuyết (hypothesis testing)** bắt đầu từ giả thuyết không `H_0`, thống kê kiểm định và phân phối lấy mẫu khi `H_0` đúng.

**Giá trị p (p-value)** là xác suất quan sát dữ liệu ít nhất cực đoan như dữ liệu hiện tại nếu `H_0` đúng; nó không phải xác suất `H_0` đúng.

Giá trị p nhỏ cũng không nói hiệu ứng lớn. Với tập dữ liệu rất lớn, hiệu ứng cực nhỏ có thể có ý nghĩa thống kê nhưng gần như không đáng kể trong thực tế.

Trong thử nghiệm A/B cho sản phẩm AI, cần xem đồng thời:

- kích thước hiệu ứng;
- khoảng tin cậy;
- kích thước mẫu;
- vấn đề kiểm định nhiều lần;
- tác động kinh doanh;
- các chỉ số bảo vệ (guardrail metrics).

## So sánh nhiều giả thuyết

Nếu kiểm định 100 giả thuyết với ngưỡng 0.05, ngay cả khi tất cả giả thuyết không đều đúng, vẫn kỳ vọng xuất hiện một số dương tính giả.

Các phương pháp như Bonferroni hoặc kiểm soát **tỷ lệ phát hiện sai (False Discovery Rate - FDR)** xử lý vấn đề này theo những cách khác nhau.

Trong thử nghiệm học máy, tìm siêu tham số hoặc đánh giá trên nhiều nhiệm vụ có thể tạo ra rất nhiều cơ hội “chọn kết quả đẹp”. Nếu chỉ báo cáo lần chạy tốt nhất mà không tính đến quá trình tìm kiếm, kết quả sẽ trông ổn định hơn thực tế.

## Tập huấn luyện, xác thực và kiểm thử là sự tách biệt thống kê

Tập huấn luyện dùng để khớp tham số.

Tập xác thực dùng để chọn siêu tham số, kiến trúc, ngưỡng hoặc phiên bản mô hình.

Tập kiểm thử nên đóng vai trò ước lượng cuối cùng tương đối độc lập sau khi quá trình lựa chọn mô hình kết thúc.

Nếu liên tục nhìn kết quả kiểm thử rồi chỉnh mô hình, tập kiểm thử đã trở thành tập xác thực về mặt chức năng thống kê. Đây là **quá khớp tập kiểm thử (test-set overfitting)**.

Một quy trình sạch:

```text
Dữ liệu huấn luyện
    ↓ khớp tham số
Các mô hình ứng viên
    ↓ lựa chọn bằng tập xác thực
Mô hình đã chọn
    ↓ đánh giá trên tập kiểm thử giữ lại
Ước lượng được báo cáo
```

Trong production, giữ lại dữ liệu theo thời gian thường phù hợp hơn chia ngẫu nhiên nếu mục tiêu thật là dự đoán tương lai.

## Rò rỉ dữ liệu

**Rò rỉ dữ liệu (data leakage / 데이터 누수)** xảy ra khi quá trình huấn luyện được tiếp cận thông tin không hợp lệ tại thời điểm dự đoán hoặc vô tình dùng thông tin từ tập xác thực/kiểm thử.

Ví dụ, mô hình dự đoán khách hàng rời bỏ dịch vụ dùng đặc trưng “ngày đóng tài khoản”. Mô hình có thể đạt độ chính xác cực cao, nhưng đặc trưng đó chỉ tồn tại sau sự kiện cần dự đoán.

Rò rỉ có thể tinh vi hơn:

- chuẩn hóa trên toàn bộ dữ liệu trước khi chia tập;
- cùng một người dùng xuất hiện ở cả train và test;
- đặc trưng được suy ra từ nhãn;
- dùng thông tin tương lai trong chuỗi thời gian;
- tiền xử lý hoặc embedding học từ nhãn của tập giữ lại.

Rò rỉ làm kết quả đánh giá lạc quan giả tạo.

## Rủi ro thực nghiệm và rủi ro kỳ vọng

Ta muốn tối thiểu hóa rủi ro kỳ vọng:

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P_{data}}[L(f_\theta(X),Y)]
\]

nhưng trong thực tế chỉ tính được rủi ro thực nghiệm:

\[
\hat R(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i)
\]

Nếu mô hình quá linh hoạt, nó có thể giảm `\hat R` bằng cách khớp những chi tiết riêng của tập huấn luyện mà không giảm rủi ro thật. Đây là bản chất của quá khớp.

## Khả năng khái quát hóa

**Khả năng khái quát hóa (generalization / 일반화)** là khả năng duy trì hiệu năng trên dữ liệu chưa thấy từ phân phối mục tiêu.

Khái quát hóa không đơn giản là “độ chính xác test cao”. Nếu phân phối test khác phân phối triển khai, kết quả test không còn đại diện tốt cho mục tiêu thực.

Một mô hình có thể khái quát hóa tốt trong cùng phân phối nhưng thất bại khi địa lý, mùa vụ, loại thiết bị, chính sách, hành vi người dùng hoặc ngôn ngữ thay đổi.

Do đó khái quát hóa luôn tương đối với một họ phân phối hoặc môi trường vận hành cụ thể.

## Đánh đổi độ chệch–phương sai

Trong hồi quy với sai số bình phương, sai số dự đoán kỳ vọng có thể được diễn giải gần đúng:

\[
Error \approx Bias^2 + Variance + Irreducible\ Noise
\]

Độ chệch cao thường xảy ra khi giả định của mô hình quá hạn chế và mô hình thiếu khớp.

Phương sai cao xảy ra khi mô hình quá nhạy với dao động của mẫu và dễ quá khớp.

Học sâu hiện đại phức tạp hơn đường cong bias–variance trong giáo trình; mô hình có rất nhiều tham số vẫn có thể khái quát hóa tốt nhờ dữ liệu lớn, tối ưu hóa, điều chuẩn và các thiên kiến ngầm. Vì vậy bias–variance là một mô hình tư duy hữu ích, không phải lý thuyết hoàn chỉnh cho mọi mạng nơ-ron.

## Điều chuẩn như một ưu tiên thống kê

Điều chuẩn thêm một ưu tiên bên ngoài việc khớp dữ liệu huấn luyện thuần túy:

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

Điều chuẩn L2 ưu tiên tham số nhỏ hơn. Tăng cường dữ liệu (data augmentation) mã hóa các tính bất biến. Dừng sớm giới hạn quỹ đạo tối ưu hóa. Dropout đưa cấu trúc ngẫu nhiên vào quá trình huấn luyện.

Theo góc nhìn thống kê, điều chuẩn làm giảm độ linh hoạt hiệu dụng hoặc mã hóa giả định tiên nghiệm để cải thiện khả năng khái quát hóa.

## Xác thực chéo

**Xác thực chéo K-fold (K-fold cross-validation)** chia dữ liệu thành `K` phần, huấn luyện trên `K-1` phần và đánh giá phần còn lại, rồi lặp lại.

Phương pháp này hữu ích khi dữ liệu nhỏ và muốn sử dụng dữ liệu hiệu quả hơn để ước lượng hiệu năng.

Tuy nhiên K-fold ngẫu nhiên không phù hợp với mọi nhiệm vụ. Chuỗi thời gian cần cách chia theo thời gian. Dữ liệu có nhiều hàng cho cùng bệnh nhân/người dùng cần chia theo nhóm để tránh rò rỉ thực thể.

Chiến lược chia dữ liệu phải mô phỏng đúng ranh giới triển khai.

## Bootstrap

**Bootstrap** lấy `n` quan sát có hoàn lại từ tập dữ liệu đã quan sát, lặp nhiều lần để xấp xỉ phân phối lấy mẫu của một thống kê.

Nó hữu ích để ước lượng độ bất định của chỉ số khi công thức giải tích khó áp dụng.

Ví dụ, muốn xây khoảng tin cậy cho F1 hoặc chênh lệch giữa hai mô hình, paired bootstrap trên cùng tập kiểm thử thường cho thông tin hữu ích.

Bootstrap cũng có giả định riêng; dữ liệu phụ thuộc mạnh cần biến thể theo khối hoặc xử lý theo miền.

## Mất cân bằng lớp và tỷ lệ nền

Nếu tỷ lệ gian lận là 0.1%, mô hình luôn dự đoán “không gian lận” có độ chính xác 99.9% nhưng hoàn toàn vô dụng.

Chỉ số phải phản ánh nhu cầu quyết định.

Độ chính xác dương (precision):

\[
Precision=\frac{TP}{TP+FP}
\]

Độ bao phủ dương (recall):

\[
Recall=\frac{TP}{TP+FN}
\]

Tỷ lệ dương tính giả:

\[
FPR=\frac{FP}{FP+TN}
\]

Tỷ lệ nền ảnh hưởng mạnh tới precision. Cùng một mô hình với độ nhạy/độ đặc hiệu giống nhau có thể có precision rất khác khi tỷ lệ lớp dương của quần thể thay đổi.

## Ngưỡng là tham số quyết định, không phải “sự thật của mô hình”

Một mô hình phân loại nhị phân có điểm hoặc xác suất `p`. Ngưỡng `0.5` không phải quy luật phổ quát.

Nếu chi phí âm tính giả lớn hơn dương tính giả, ngưỡng có thể cần thấp hơn.

Rủi ro kỳ vọng theo ngưỡng:

\[
Risk(t)=C_{FP}P(FP\mid t)+C_{FN}P(FN\mid t)
\]

Ngưỡng nên được chọn theo mục tiêu vận hành, năng lực xử lý và ràng buộc rủi ro. Đánh giá mô hình cần nối các chỉ số với kinh tế của quyết định.

## ROC và Precision–Recall

Đường cong ROC biểu diễn TPR theo FPR qua nhiều ngưỡng. ROC-AUC đo khả năng xếp hạng dưới một cách diễn giải xác suất nhất định.

Đường cong Precision–Recall thường hữu ích hơn khi lớp dương hiếm vì precision phản ánh trực tiếp dương tính giả so với số dự đoán dương.

Không có chỉ số tốt nhất cho mọi bài toán. Việc chọn chỉ số chính là tuyên bố về điều hệ thống coi trọng.

## Dịch chuyển phân phối

Phân phối huấn luyện:

\[
P_{train}(X,Y)
\]

Phân phối triển khai:

\[
P_{deploy}(X,Y)
\]

Nếu hai phân phối khác nhau, các giả định của mô hình bị thử thách.

Một số dạng thường gặp:

- **dịch chuyển hiệp biến (covariate shift)**: `P(X)` thay đổi;
- **dịch chuyển nhãn/tiên nghiệm (label/prior shift)**: `P(Y)` thay đổi;
- **dịch chuyển khái niệm (concept shift/drift)**: `P(Y|X)` thay đổi.

Hệ thống thực có thể kết hợp nhiều dạng, nên cách phân loại này chủ yếu dùng để chẩn đoán.

## Thiên lệch lựa chọn và vòng phản hồi

Hệ thống gợi ý chỉ quan sát phản hồi cho những nội dung mà chính nó đã hiển thị. Dữ liệu tương lai do chính sách hiện tại tạo ra.

```mermaid
flowchart LR
    M[Mô hình hiện tại] --> R[Nội dung gợi ý]
    R --> U[Người dùng được tiếp xúc]
    U --> F[Phản hồi quan sát]
    F --> D[Dữ liệu huấn luyện]
    D --> M
```

Nếu bỏ qua vòng phản hồi, mô hình có thể tự củng cố độ phổ biến và che khuất các lựa chọn mà nó chưa từng thử.

Đây là điểm nối giữa thống kê, suy luận nhân quả, bandit và hệ thống gợi ý.

## Tương quan và nhân quả

Nếu người dùng sử dụng tính năng A thường có tỷ lệ duy trì cao hơn, không có nghĩa ép mọi người dùng A sẽ làm tỷ lệ duy trì tăng. Có thể người dùng vốn đã tích cực mới tự chọn A.

Dự đoán hỏi:

> Có thể dự đoán `Y` từ `X` không?

Suy luận nhân quả hỏi:

> Nếu chủ động thay đổi `X`, `Y` sẽ thay đổi như thế nào?

Học máy rất mạnh cho dự đoán, nhưng câu hỏi nhân quả cần giả định, thí nghiệm hoặc chiến lược nhận dạng nhân quả riêng.

## Thử nghiệm A/B

Thí nghiệm ngẫu nhiên gán đơn vị vào nhóm xử lý và đối chứng để trung bình hóa nhiều yếu tố gây nhiễu.

Trong sản phẩm AI, A/B test có thể so sánh thuật toán gợi ý, chính sách xếp hạng hoặc hành vi trợ lý.

Tuy nhiên cần chú ý **ảnh hưởng chéo (interference)**: cách xử lý một người dùng có thể ảnh hưởng người khác, ví dụ trong marketplace hoặc mạng xã hội. Khi giả định độc lập giữa đơn vị bị vi phạm, phân tích chuẩn có thể gây hiểu sai.

## Đánh giá ngoại tuyến và trực tuyến

Tập kiểm thử ngoại tuyến giúp lặp nhanh và tái lập được. Thử nghiệm trực tuyến đo tác động thực trên sản phẩm.

Hai kết quả có thể không đồng ý vì chỉ số ngoại tuyến chỉ là đại diện thay thế cho mục tiêu người dùng hoặc kinh doanh.

Ví dụ, hệ thống gợi ý tăng NDCG nhưng làm bảng tin quá đồng nhất, từ đó giảm khả năng khám phá dài hạn. Đánh giá AI cần một hệ phân cấp chỉ số thay vì một điểm số duy nhất.

## Công suất thống kê

**Công suất thống kê (statistical power)** là xác suất phát hiện một hiệu ứng có kích thước đã định khi hiệu ứng đó thực sự tồn tại.

Thí nghiệm thiếu power dễ tạo kết quả không rõ ràng. Lập kế hoạch kích thước mẫu cần xem phương sai kỳ vọng, hiệu ứng nhỏ nhất cần phát hiện và mục tiêu về mức ý nghĩa/công suất.

Không nên “chạy tới khi p < 0.05 rồi dừng” nếu quy tắc dừng không được tính trong phân tích, vì dừng tùy chọn làm tăng nguy cơ dương tính giả.

## Khả năng tái lập và hạt giống ngẫu nhiên

Huấn luyện học sâu có nhiều nguồn ngẫu nhiên từ khởi tạo, thứ tự dữ liệu, dropout và kernel phần cứng không xác định hoàn toàn.

Một lần chạy duy nhất có thể không đại diện cho hiệu năng của phương pháp.

Khi khả thi, nên báo cáo nhiều lần chạy, mức biến thiên và giao thức thí nghiệm. Hạt giống ngẫu nhiên giúp tái lập nhưng không biến một kết quả thành sự thật phổ quát.

## Mô hình tư duy (mental model)

```text
Xác suất       → mô hình hóa bất định
Thống kê       → học điều đáng tin về quần thể từ mẫu hữu hạn
Tập huấn luyện → mẫu dùng để khớp mô hình
Tập xác thực   → mẫu dùng để lựa chọn
Tập kiểm thử   → mẫu dùng để ước lượng sau khi lựa chọn
Khái quát hóa  → hiệu năng ngoài mẫu đã dùng để khớp
Độ bất định    → mức chưa biết về chỉ số/tham số/dự đoán
Dịch chuyển    → môi trường triển khai không còn giống giả định lấy mẫu
```

## Các hiểu lầm thường gặp

### “Tập dữ liệu càng lớn thì thiên lệch càng ít”

Kích thước mẫu lớn làm giảm phương sai lấy mẫu nhưng thiên lệch lựa chọn có hệ thống vẫn có thể giữ nguyên hoặc mạnh hơn.

### “Độ chính xác test chính là hiệu năng thực tế”

Chỉ đúng khi phân phối kiểm thử và giao thức đánh giá đại diện đủ tốt cho môi trường triển khai mục tiêu.

### “p < 0.05 nghĩa là hiệu ứng quan trọng”

p-value không cho biết kích thước hiệu ứng hoặc ý nghĩa kinh doanh.

### “Xác thực chéo luôn tốt hơn một lần chia train/test”

Không đúng. Với dữ liệu phụ thuộc thời gian hoặc theo nhóm, cross-validation ngẫu nhiên có thể làm rò rỉ thông tin. Thiết kế chia tập phải phản ánh cách hệ thống sẽ được triển khai.

## Liên kết kiến thức

Thống kê là cầu nối giữa [Xác suất](./02_probability_for_ai.md) và học máy. Các chapter sau về khái quát hóa, đánh giá mô hình, hiệu chuẩn, thiên lệch dữ liệu và trôi dữ liệu sẽ sử dụng lại các ý tưởng ở đây.

Khi nhìn một điểm số mô hình, đừng chỉ hỏi “bao nhiêu phần trăm?”. Hãy hỏi: **trên quần thể nào, mẫu được lấy thế nào, độ bất định của ước lượng bao nhiêu, lựa chọn đã xảy ra ở đâu, và phân phối triển khai có giống phân phối đánh giá hay không?**