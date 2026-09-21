# Thẩm định phương pháp và chemometrics — từ dữ liệu đo tới bằng chứng định lượng đáng tin cậy

> **Thẩm định phương pháp (method validation / 분석법 검증)** trả lời câu hỏi: một phương pháp đo có thực sự phù hợp với mục đích sử dụng đã định hay không? **Chemometrics (hóa lượng học / 화학계량학)** sử dụng thống kê, đại số tuyến tính và mô hình tính toán để trích xuất thông tin hóa học từ dữ liệu nhiều chiều. Hai lĩnh vực gặp nhau ở một điểm chung: không chỉ tạo ra con số, mà phải chứng minh con số đó có ý nghĩa trong điều kiện thực tế.

Một phương pháp có thể cho đường chuẩn đẹp nhưng vẫn không phù hợp nếu mẫu thật có hiệu ứng nền mạnh. Một mô hình máy học có thể có sai số trung bình thấp nhưng thất bại ở vùng nồng độ hoặc loại mẫu quan trọng. Vì vậy thẩm định không phải bước thủ tục ở cuối; nó là quá trình kiểm tra có hệ thống các giả định của toàn chuỗi đo.

# Bắt đầu từ mục đích sử dụng

Không tồn tại một bộ tiêu chí thẩm định giống hệt cho mọi phương pháp. Phương pháp dùng để sàng lọc nhanh khác phương pháp dùng để định lượng thuốc trong huyết tương, kiểm soát tạp chất dược phẩm hay xác nhận giới hạn pháp lý trong nước uống.

Trước khi chọn chỉ tiêu, cần xác định:

- chất phân tích là gì;
- nền mẫu nào;
- khoảng nồng độ nào;
- quyết định nào sẽ dựa trên kết quả;
- mức độ sai số có thể chấp nhận;
- mẫu có cần định tính, định lượng hay cả hai;
- yêu cầu về tốc độ, chi phí và thông lượng.

Một phương pháp “rất chính xác” nhưng quá chậm hoặc không ổn định với mẫu thực tế có thể vẫn không phù hợp với mục đích.

# Độ chọn lọc và tính đặc hiệu

**Độ chọn lọc (selectivity)** là khả năng đo chất phân tích khi có các thành phần khác trong mẫu.

Nếu tín hiệu của chất cần đo chồng với tạp chất, độ chụm tốt không cứu được kết quả vì thiết bị đang đo tổng tín hiệu từ nhiều nguồn.

Độ chọn lọc có thể đến từ:

- phản ứng hóa học chọn lọc;
- bước tách trước đo;
- bước sóng đặc trưng;
- tỉ số khối lượng trên điện tích trong MS;
- thời gian lưu sắc ký;
- điện thế điện cực;
- mô hình đa biến.

Tính chọn lọc vì vậy là thuộc tính của **toàn phương pháp**, không phải chỉ của detector.

## Thử nghiệm nhiễu

Một cách kiểm tra thực tế là thêm các chất có khả năng gây nhiễu vào nền mẫu rồi quan sát mức thay đổi kết quả.

Nếu chất phân tích là \(A\) và chất gây nhiễu là \(I\), câu hỏi không chỉ là “\(I\) có tín hiệu không?” mà còn là:

- tín hiệu của \(I\) có chồng lên \(A\) không;
- \(I\) có làm thay đổi hiệu suất chiết không;
- \(I\) có ức chế hoặc tăng ion hóa không;
- \(I\) có phản ứng với thuốc thử không;
- \(I\) có làm detector bão hòa không.

# Khoảng đo và tuyến tính

**Khoảng đo (range)** là vùng mà phương pháp đạt các yêu cầu đã đặt về độ đúng, độ chụm và mô hình tín hiệu.

Tuyến tính chỉ là một mô hình khả dĩ:

\[
y=a+bx
\]

Không nên coi tuyến tính là mặc định chỉ vì phần mềm hồi quy trả ra một đường thẳng.

Khi nồng độ tăng, có thể xuất hiện:

- detector bão hòa;
- tự hấp thụ;
- hiệu ứng ion hóa;
- cân bằng hóa học thay đổi;
- độ nhớt hoặc nền thay đổi;
- phương sai tăng theo tín hiệu.

Vì vậy cần xem phần dư, không chỉ nhìn \(R^2\).

# Độ đúng và độ chệch

**Độ đúng (trueness)** có thể được đánh giá bằng:

- vật liệu chuẩn được chứng nhận;
- phương pháp tham chiếu;
- mẫu thêm chuẩn;
- so sánh liên phòng thí nghiệm.

Độ chệch có thể viết:

\[
bias=\bar{x}-x_{ref}
\]

hoặc ở dạng tương đối:

\[
relative\ bias=\frac{\bar{x}-x_{ref}}{x_{ref}}\times100\%
\]

Nếu không có giá trị tham chiếu đáng tin cậy, việc nói phương pháp “đúng” chỉ dựa trên độ lặp lại là không hợp lệ.

# Độ chụm có nhiều tầng

Độ chụm không phải một con số duy nhất.

## Độ lặp lại

**Độ lặp lại (repeatability)** đo biến thiên khi điều kiện gần như không đổi:

- cùng người thao tác;
- cùng thiết bị;
- khoảng thời gian ngắn;
- cùng phòng thí nghiệm.

## Độ chụm trung gian

**Độ chụm trung gian (intermediate precision)** mở rộng sang khác ngày, khác người, khác lô thuốc thử hoặc đôi khi khác thiết bị trong cùng phòng thí nghiệm.

## Độ tái lập

**Độ tái lập (reproducibility)** thường liên quan khác phòng thí nghiệm.

Phương pháp có repeatability tốt nhưng reproducibility kém có thể quá phụ thuộc vào thao tác hoặc thiết bị cụ thể.

# Độ bền vững của phương pháp

**Độ bền vững (robustness)** hỏi: nếu thay đổi nhỏ, có chủ ý quanh điều kiện danh định, kết quả có còn ổn định không?

Ví dụ:

- pH thay đổi ±0,1;
- nhiệt độ cột thay đổi vài độ;
- tốc độ dòng thay đổi vài phần trăm;
- thời gian chiết thay đổi nhẹ;
- nồng độ thuốc thử thay đổi trong sai số pha chế thực tế.

Một phương pháp chỉ hoạt động tại một điểm điều kiện rất hẹp sẽ khó chuyển giao vào vận hành thường ngày.

# Độ nhạy

Trong mô hình tuyến tính, **độ nhạy (sensitivity)** thường liên hệ với độ dốc:

\[
sensitivity=\frac{dy}{dx}\approx b
\]

Độ dốc lớn nghĩa tín hiệu thay đổi nhiều khi nồng độ thay đổi nhỏ.

Tuy nhiên độ nhạy cao không tự đồng nghĩa giới hạn phát hiện thấp. Nếu nhiễu nền cũng lớn, khả năng phân biệt chất phân tích vẫn kém.

Một cách trực giác:

```text
khả năng phát hiện tốt
≈ tín hiệu thay đổi mạnh / nhiễu nền nhỏ
```

# LOD và LOQ phải gắn với mục đích

**Giới hạn phát hiện (LOD)** là vùng mà sự hiện diện của chất phân tích có thể được phân biệt hợp lý với nền.

**Giới hạn định lượng (LOQ)** yêu cầu mức độ không đảm bảo đủ nhỏ để báo cáo một giá trị định lượng hữu ích.

Một biểu thức đơn giản thường gặp:

\[
LOD\sim\frac{k\sigma}{b}
\]

với \(\sigma\) mô tả biến thiên nền và \(b\) là độ dốc hiệu chuẩn.

Nhưng công thức không thay thế việc xác nhận thực nghiệm ở vùng nồng độ thấp. Nếu mức pháp lý quan trọng là 5 µg/L, phương pháp phải được kiểm tra thật quanh vùng đó, không chỉ suy LOD từ đường chuẩn nồng độ cao.

# Hiệu ứng nền

**Hiệu ứng nền (matrix effect)** xảy ra khi các thành phần khác trong mẫu làm tín hiệu của analyte thay đổi.

Trong LC–MS, chất đồng rửa giải có thể ức chế hoặc tăng ion hóa. Trong quang phổ nguyên tử, độ nhớt, muối và thành phần acid có thể thay đổi vận chuyển mẫu hoặc quá trình nguyên tử hóa.

Một cách định lượng đơn giản:

\[
ME=\frac{slope_{matrix}}{slope_{solvent}}
\]

Nếu tỉ số khác đáng kể 1, hiệu chuẩn trong dung môi tinh khiết có thể không đại diện cho mẫu thật.

Các chiến lược gồm:

- chuẩn nội;
- hiệu chuẩn nền tương hợp;
- thêm chuẩn;
- pha loãng nền;
- tách nền trước đo.

# Hiệu suất thu hồi và hiệu ứng nền không giống nhau

Hai vấn đề thường bị gộp là:

- **thu hồi (recovery)**: mất bao nhiêu analyte trong chuẩn bị mẫu;
- **hiệu ứng nền**: cùng một lượng analyte đi vào detector nhưng tín hiệu thay đổi bao nhiêu do nền.

Một phương pháp có thể thu hồi 70% nhưng rất lặp lại và có chuẩn nội bù tốt. Ngược lại, thu hồi gần 100% nhưng ion hóa bị nền ức chế không ổn định vẫn làm kết quả kém.

# Tính ổn định

Chất phân tích có thể thay đổi trong:

- thời gian chờ trên autosampler;
- đông–rã đông nhiều lần;
- bảo quản dài ngày;
- tiếp xúc ánh sáng;
- thay đổi pH;
- tiếp xúc vật liệu bình chứa.

Thẩm định độ ổn định cần tái hiện đúng điều kiện vận hành thật. Một mẫu ổn định ở -80 °C không chứng minh nó ổn định 24 giờ trên autosampler ở nhiệt độ phòng.

# Carryover

**Nhiễm kéo theo (carryover)** xảy ra khi mẫu nồng độ cao để lại chất trong kim tiêm, đường ống, injector hoặc cột và ảnh hưởng mẫu tiếp theo.

Kiểm tra đơn giản là chạy mẫu trắng sau mẫu nồng độ cao và đánh giá tín hiệu còn lại.

Carryover đặc biệt nguy hiểm khi chuỗi mẫu có khoảng nồng độ rộng.

# Độ không đảm bảo và tiêu chí chấp nhận

Thẩm định tốt phải nối từng chỉ tiêu với quyết định sử dụng.

Ví dụ nếu cần phân biệt 9,5 mg/L với giới hạn 10 mg/L, độ không đảm bảo ±2 mg/L là quá lớn dù độ lặp lại có vẻ tốt.

Kết quả nên được hiểu dưới dạng:

\[
result\pm uncertainty
\]

và tiêu chí chấp nhận phải phản ánh hậu quả của quyết định sai.

# Chemometrics — khi một tín hiệu trở thành ma trận dữ liệu

Nhiều kỹ thuật hiện đại không cho một số đơn lẻ mà cho vector hoặc ma trận:

- phổ UV–Vis theo bước sóng;
- phổ IR/Raman;
- phổ NMR;
- chromatogram nhiều peak;
- dữ liệu MS nhiều ion;
- dữ liệu cảm biến theo thời gian.

Ta có thể biểu diễn dữ liệu:

\[
\mathbf X\in\mathbb R^{n\times p}
\]

với \(n\) mẫu và \(p\) biến đo.

Nếu \(p\) lớn và các biến tương quan mạnh, phân tích từng biến riêng lẻ không còn hiệu quả.

# Tiền xử lý dữ liệu không phải bước trung tính

Các thao tác như:

- trừ nền;
- chuẩn hóa;
- căn chỉnh peak;
- làm trơn;
- đạo hàm phổ;
- mean-centering;
- scaling;

đều thay đổi hình học của dữ liệu.

Ví dụ autoscaling:

\[
z_{ij}=\frac{x_{ij}-\bar{x}_j}{s_j}
\]

làm mỗi biến có phương sai gần 1, nhờ đó biến có đơn vị lớn không tự chi phối mô hình.

Nhưng nếu phương sai lớn chính là thông tin hóa học quan trọng, scaling có thể làm suy yếu tín hiệu đó. Tiền xử lý vì vậy phải dựa trên cơ chế đo.

# PCA — tìm các trục biến thiên chính

**Phân tích thành phần chính (principal component analysis, PCA)** phân rã dữ liệu gần dạng:

\[
\mathbf X=\mathbf T\mathbf P^T+\mathbf E
\]

trong đó:

- \(\mathbf T\): điểm số (scores), biểu diễn mẫu trong không gian mới;
- \(\mathbf P\): tải (loadings), cho biết biến gốc đóng góp thế nào;
- \(\mathbf E\): phần chưa giải thích.

PCA là phương pháp **không giám sát (unsupervised)**. Nó tìm hướng có phương sai lớn, không tự biết nhóm mẫu nào “đúng” hay “sai”.

Một cụm tách trong PCA không tự chứng minh khác biệt hóa học có ý nghĩa; cần xem loadings và cơ chế hóa học phía sau.

# Hình học của PCA

Nếu dữ liệu ban đầu có hàng trăm bước sóng nhưng phần lớn thay đổi cùng nhau, PCA có thể nén chúng xuống vài trục.

Thành phần chính thứ nhất chọn hướng có phương sai lớn nhất. Thành phần tiếp theo vuông góc với thành phần trước và giải thích phần phương sai còn lại lớn nhất.

Đây là đại số tuyến tính của ma trận hiệp phương sai hoặc SVD, không phải một thuật toán “AI bí ẩn”.

# PLS — dự đoán nồng độ từ dữ liệu nhiều biến

**Hồi quy bình phương tối thiểu riêng phần (partial least squares, PLS)** xây các biến tiềm ẩn vừa giải thích \(X\) vừa liên hệ với biến mục tiêu \(y\).

Nó hữu ích khi:

- số biến phổ lớn;
- các biến tương quan mạnh;
- muốn định lượng từ toàn phổ thay vì một bước sóng.

Tuy nhiên PLS vẫn có thể overfit. Số thành phần phải được chọn bằng xác nhận chéo hoặc tập validation độc lập.

# Phân loại

Các bài toán như phân biệt dầu thật/giả, nguồn gốc mẫu hoặc trạng thái chất lượng có thể dùng:

- LDA;
- PLS-DA;
- SVM;
- cây quyết định;
- mô hình học máy khác.

Nhưng mục tiêu phân loại không làm biến mất yêu cầu hóa học. Nếu tập dữ liệu vô tình mã hóa batch, ngày đo hoặc thiết bị thay vì bản chất mẫu, mô hình sẽ học tín hiệu sai.

# Rò rỉ dữ liệu

**Rò rỉ dữ liệu (data leakage)** xảy ra khi thông tin từ tập kiểm tra đi vào quá trình xây mô hình.

Ví dụ:

1. chuẩn hóa toàn bộ dữ liệu trước khi chia train/test;
2. chọn biến bằng toàn bộ dữ liệu rồi mới đánh giá;
3. cùng một mẫu kỹ thuật xuất hiện ở cả train và test.

Kết quả đánh giá khi đó quá lạc quan.

Mọi bước học từ dữ liệu — scaling, chọn biến, PCA, imputation — phải được fit chỉ trên tập huấn luyện trong từng vòng validation.

# Xác nhận chéo

**Xác nhận chéo (cross-validation)** chia dữ liệu thành nhiều phần, huấn luyện trên một phần và đánh giá trên phần giữ lại.

Nhưng cách chia phải phản ánh ứng dụng thật.

Nếu nhiều phổ đến từ cùng một mẫu vật lý, không nên tách các phổ lặp của cùng mẫu vào cả train và validation vì mô hình gần như đã nhìn thấy mẫu đó.

Trong dữ liệu theo batch, có thể cần block cross-validation theo ngày, lô hoặc thiết bị.

# Tập kiểm tra độc lập

Một **tập kiểm tra ngoài (external test set)** được giữ hoàn toàn ngoài quá trình phát triển là bằng chứng mạnh hơn cho khả năng tổng quát hóa.

Nó nên đại diện cho:

- khoảng nồng độ thực;
- ma trận thực;
- nguồn mẫu thực;
- biến thiên thiết bị hoặc thời gian mà mô hình sẽ gặp.

# RMSE và sai số dự đoán

Một chỉ tiêu thường dùng:

\[
RMSE=\sqrt{\frac1n\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
\]

RMSE nhấn mạnh sai số lớn do bình phương phần dư.

Có thể bổ sung:

- MAE;
- bias;
- \(R^2\);
- phần dư theo nồng độ;
- sai số theo từng lớp mẫu.

Một chỉ tiêu trung bình duy nhất có thể che hiệu năng rất kém ở vùng nồng độ thấp nhưng quan trọng về pháp lý.

# Miền áp dụng

**Miền áp dụng (applicability domain)** là vùng không gian hóa học mà dữ liệu huấn luyện thực sự hỗ trợ dự đoán.

Một mô hình học trên nước sạch không nên được mặc định áp dụng cho huyết tương. Một mô hình NIR học từ một giống cây không chắc tổng quát cho giống khác.

Ngoại suy ngoài miền là nguồn rủi ro lớn hơn sai số nội suy thông thường.

# Outlier và leverage trong mô hình đa biến

Một mẫu có thể khác thường vì:

- lỗi đo;
- lỗi nhập dữ liệu;
- thật sự thuộc một vùng hóa học mới.

Trong không gian đa biến, có thể dùng leverage, khoảng cách Mahalanobis, Q-residual hoặc các chỉ tiêu khác để phát hiện mẫu bất thường.

Nhưng không nên tự động xóa mọi outlier. Một outlier hợp lệ có thể chính là dấu hiệu rằng miền áp dụng của phương pháp còn quá hẹp.

# Thiết kế tập chuẩn đa biến

Một mô hình tốt cần tập chuẩn bao phủ biến thiên thật:

```text
nồng độ
× nhiệt độ
× độ ẩm
× batch
× nền mẫu
× thiết bị
× thời gian
```

Nếu mọi chuẩn được pha trong cùng ngày, cùng dung môi, cùng người thao tác, mô hình có thể cho hiệu năng nội bộ đẹp nhưng thất bại khi triển khai.

# Chemometrics không thay thế hóa học

Một mô hình có thể tìm tương quan nhưng không tự chứng minh cơ chế.

Ví dụ phổ NIR dự đoán hàm lượng protein có thể sử dụng tín hiệu liên hệ với độ ẩm hoặc kích thước hạt nếu các biến đó tình cờ tương quan trong tập huấn luyện.

Do đó cần kết hợp:

- hiểu cơ chế phổ;
- thiết kế thí nghiệm;
- kiểm soát nhiễu;
- validation độc lập;
- kiểm tra độ bền theo thời gian.

# Theo dõi mô hình sau triển khai

Mô hình định lượng có thể suy giảm do:

- thiết bị lão hóa;
- thay nguồn nguyên liệu;
- thay batch thuốc thử;
- thay detector;
- thay nền mẫu;
- cập nhật quy trình sản xuất.

Đây là **trôi dữ liệu (data drift)** hoặc **trôi khái niệm (concept drift)** tùy bản chất.

Cần theo dõi chuẩn kiểm tra, phân bố tín hiệu và sai số dự đoán theo thời gian. Nếu hệ thay đổi, mô hình có thể cần hiệu chuẩn lại hoặc xây lại.

# Một workflow thẩm định hợp lý

```text
xác định mục đích
→ định nghĩa measurand
→ thiết kế lấy mẫu
→ xây phương pháp
→ kiểm tra chọn lọc
→ xác lập khoảng đo
→ đánh giá độ đúng và độ chụm
→ kiểm tra robustness và stability
→ đánh giá LOD/LOQ
→ xây ngân sách độ không đảm bảo
→ xác nhận trên mẫu độc lập
→ giám sát sau triển khai
```

Không nhất thiết mọi phương pháp đều dùng mọi bước ở cùng độ sâu, nhưng logic phải luôn quay lại câu hỏi: **bằng chứng hiện có có đủ để tin kết quả trong điều kiện sử dụng thật hay không?**

# Những hiểu lầm thường gặp

### “Validation là chạy đường chuẩn rồi xem \(R^2\)”

Không. Đường chuẩn chỉ kiểm tra một phần rất nhỏ của toàn phương pháp.

### “LOD càng thấp thì phương pháp càng tốt”

Không nhất thiết. Một LOD cực thấp vô ích nếu phương pháp thiếu chọn lọc, quá chậm hoặc không ổn định.

### “PCA cho thấy hai cụm nên hai nhóm chắc chắn khác nhau”

Không. PCA chỉ phản ánh phương sai lớn; batch, nền hoặc tiền xử lý có thể tạo cụm giả.

### “Cross-validation cao nghĩa mô hình sẽ chạy tốt ngoài thực tế”

Không nếu cách chia dữ liệu làm rò rỉ thông tin hoặc không phản ánh biến thiên triển khai.

### “Mô hình máy học có thể thay thế hiểu biết hóa học”

Không. Mô hình thống kê chỉ đáng tin trong miền dữ liệu và giả định đã được kiểm tra.

# Mô hình tư duy

Thẩm định phương pháp là **kiểm thử hợp đồng giữa phép đo và mục đích sử dụng**. Chemometrics là **cách nén và mô hình hóa dữ liệu hóa học nhiều chiều**, nhưng mọi mô hình cuối cùng vẫn phải được neo vào mẫu thật, cơ chế đo, kiểm soát chất lượng và độ không đảm bảo.

Xem thêm: [Đo lường và lấy mẫu](./00_measurement_and_sampling.md), [Quang phổ](./03_spectroscopy.md), [Sắc ký](./04_chromatography.md), [Khối phổ](./05_mass_spectrometry.md) và [Sai số, độ không đảm bảo và phân tích dữ liệu](../17_laboratory/05_error_uncertainty_and_data_analysis.md).
