# Sai số, độ không đảm bảo và phân tích dữ liệu — biết một con số đáng tin đến mức nào

> Một giá trị đo không kèm **độ không đảm bảo (uncertainty / 측정 불확도)** và bối cảnh phương pháp là một thông tin chưa hoàn chỉnh. Trong khoa học đo lường, mục tiêu không phải tạo ra một con số trông thật chính xác, mà là hiểu con số đó được tạo ra như thế nào, những nguồn biến thiên và độ chệch nào có thể ảnh hưởng nó, và mức độ tin cậy hợp lý của kết luận rút ra từ dữ liệu.

Hóa học thực nghiệm luôn đi qua một chuỗi: mẫu thật → thao tác lấy mẫu và chuẩn bị → phản ứng hoặc phép tách → tín hiệu thiết bị → hiệu chuẩn → tính toán → kết luận. Mỗi mắt xích có thể thêm biến thiên, độ chệch hoặc giả định. Vì thế phân tích dữ liệu không phải bước làm đẹp con số ở cuối thí nghiệm; nó là phần của chính mô hình đo.

## Sai số và độ không đảm bảo không phải cùng một khái niệm

**Sai số (error)** là độ lệch giữa kết quả đo và giá trị thật hoặc giá trị tham chiếu phù hợp:

\[
error=x_{measured}-x_{reference}
\]

Nếu giá trị thật không biết chính xác — trường hợp rất phổ biến — thì sai số thật cũng không thể biết chính xác.

**Độ không đảm bảo (measurement uncertainty)** mô tả mức phân tán hợp lý của các giá trị có thể gán cho đại lượng cần đo dựa trên thông tin hiện có. Nó không nói rằng phép đo “sai”, mà nói rằng dữ liệu và mô hình chỉ cho phép ta biết đại lượng tới một mức giới hạn nhất định.

Ví dụ, báo cáo:

\[
c=(10.24\pm0.08)\;mg/L
\]

có ý nghĩa hơn nhiều so với chỉ viết `10.240000 mg/L`, vì phần \(\pm0.08\) cho biết độ phân giải thông tin thực sự của phép đo.

## Đại lượng cần đo và mô hình đo

Trước khi nói về sai số, phải xác định rõ **đại lượng cần đo (measurand)** là gì. “Nồng độ sắt trong nước” có thể nghĩa là sắt tổng sau phá mẫu, sắt hòa tan sau lọc 0,45 µm, \(Fe^{2+}\), hay tổng \(Fe^{2+}+Fe^{3+}\). Các định nghĩa khác nhau dẫn đến quy trình và kết quả khác nhau.

Phần lớn phép đo không quan sát trực tiếp đại lượng đích. Kết quả được suy ra từ các đại lượng đầu vào:

\[
y=f(x_1,x_2,\ldots,x_n)
\]

Ví dụ trong chuẩn độ, nồng độ mẫu có thể phụ thuộc nồng độ dung dịch chuẩn, thể tích chuẩn đã dùng, thể tích mẫu, tỉ lệ hóa lượng và hệ số pha loãng. Trong quang phổ, nồng độ có thể được suy từ tín hiệu hấp thụ và đường hiệu chuẩn.

Mỗi biến đầu vào đều có độ không đảm bảo. Vì vậy kết quả cuối phải phản ánh cách các độ không đảm bảo đó truyền qua mô hình.

## Độ đúng, độ chụm và độ chệch

Ba ý tưởng thường bị trộn lẫn là **độ chụm (precision)**, **độ đúng theo nghĩa gần giá trị tham chiếu (trueness)** và **độ chính xác tổng quát (accuracy)**.

Độ chụm mô tả mức độ các kết quả lặp lại nằm gần nhau. Nếu đo cùng một mẫu nhiều lần và thu được 10.21, 10.22, 10.21, 10.23 mg/L, phép đo có độ chụm cao.

Độ đúng mô tả mức độ giá trị trung bình gần giá trị tham chiếu. Nếu giá trị tham chiếu thực tế là 11.00 mg/L thì một chuỗi kết quả quanh 10.22 mg/L vẫn có thể rất chụm nhưng bị **độ chệch (bias)** lớn.

Điểm cốt lõi là: lặp lại nhiều lần chỉ giúp hiểu biến thiên ngẫu nhiên tốt hơn; nó không tự sửa một phương pháp bị chệch có hệ thống.

## Biến thiên ngẫu nhiên

Biến thiên ngẫu nhiên có thể đến từ nhiễu detector, khác biệt thao tác bơm mẫu, dao động nhiệt độ, thay đổi nhỏ của thể tích, tiếng ồn điện hoặc hàng loạt yếu tố nhỏ không kiểm soát hoàn toàn.

Nếu các quan sát độc lập và có phương sai hữu hạn, sai số chuẩn của trung bình giảm xấp xỉ theo:

\[
SE(\bar{x})=\frac{s}{\sqrt n}
\]

Điều này giải thích vì sao tăng số phép lặp có thể cải thiện ước lượng trung bình. Tuy nhiên nó **không** có nghĩa mọi độ không đảm bảo đều giảm vô hạn theo \(1/\sqrt n\). Độ chệch hiệu chuẩn, mẫu không đại diện hoặc drift có tương quan có thể đặt ra giới hạn mà việc đo lặp không thể vượt qua.

## Hiệu ứng hệ thống và nguồn độ chệch

Các nguồn gây độ chệch thường gồm:

- sai lệch hiệu chuẩn;
- độ tinh khiết thuốc thử khác giá trị giả định;
- thu hồi không hoàn toàn khi chiết hoặc phá mẫu;
- hiệu ứng nền (matrix effect);
- hiệu chỉnh mẫu trắng không đúng;
- dụng cụ thể tích bị lệch hiệu chuẩn;
- nhiễm bẩn kéo dài;
- tổn thất chất phân tích do hấp phụ hoặc bay hơi.

Muốn phát hiện chúng phải dùng bằng chứng độc lập như vật liệu chuẩn được chứng nhận, mẫu thêm chuẩn, chuẩn kiểm tra, so sánh phương pháp hoặc thử nghiệm thu hồi.

## Trung bình, phương sai và độ lệch chuẩn

Với \(n\) kết quả \(x_i\), trung bình mẫu là:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

Phương sai mẫu:

\[
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
\]

và độ lệch chuẩn:

\[
s=\sqrt{s^2}
\]

Mẫu số \(n-1\) xuất hiện vì khi dùng chính dữ liệu để ước lượng trung bình, ta đã tiêu tốn một bậc tự do. Dưới các giả định quen thuộc, cách tính này tránh đánh giá thấp phương sai quần thể.

**Độ lệch chuẩn (standard deviation, SD)** mô tả độ phân tán của các quan sát riêng lẻ. **Sai số chuẩn của trung bình (standard error, SE)** mô tả độ không chắc của ước lượng trung bình do lấy mẫu hữu hạn. Hai đại lượng trả lời hai câu hỏi khác nhau và không nên dùng thay nhau.

## Độ lệch chuẩn tương đối

Độ lệch chuẩn tương đối:

\[
RSD=\frac{s}{\bar{x}}\times100\%
\]

cho phép so sánh độ chụm ở các thang nồng độ khác nhau. Tuy nhiên khi \(\bar{x}\) gần 0, RSD trở nên rất lớn hoặc mất ý nghĩa, nên không nên sử dụng máy móc.

## Khoảng tin cậy

Nếu dữ liệu gần phân bố chuẩn, độc lập và phương sai chưa biết, khoảng tin cậy cho trung bình có thể viết:

\[
\bar{x}\pm t_{\alpha/2,\,n-1}\frac{s}{\sqrt n}
\]

Khi \(n\) nhỏ, hệ số \(t\) lớn hơn vì bản thân ước lượng phương sai còn không chắc chắn.

Trong cách diễn giải tần suất (frequentist), khoảng tin cậy 95% không có nghĩa “xác suất giá trị thật nằm trong khoảng cụ thể này là 95%”. Ý nghĩa chính xác hơn là: nếu lặp lại toàn bộ quy trình rất nhiều lần dưới cùng giả định, khoảng được xây dựng theo quy tắc này sẽ bao phủ tham số thật khoảng 95% số lần.

Đây là một ví dụ cho thấy cần phân biệt **mô hình thống kê** với cách nói trực giác hàng ngày.

## Độ không đảm bảo loại A và loại B

Trong đo lường, người ta thường phân loại cách đánh giá độ không đảm bảo thành:

**Loại A (Type A)**: được ước lượng bằng phân tích thống kê từ các phép đo lặp.

**Loại B (Type B)**: được suy từ chứng chỉ hiệu chuẩn, thông số thiết bị, dữ liệu tham chiếu, kinh nghiệm trước đây hoặc hiểu biết kỹ thuật khác.

Loại A/B mô tả **cách đánh giá**, không hoàn toàn đồng nghĩa với “ngẫu nhiên/hệ thống”. Một chứng chỉ hiệu chuẩn chẳng hạn có thể chứa cả nhiều thành phần khác nhau.

## Độ không đảm bảo chuẩn

Để cộng các nguồn độ không đảm bảo, ta thường quy chúng về dạng tương đương độ lệch chuẩn \(u(x_i)\).

Nếu chỉ biết một đại lượng nằm đều trong khoảng \(\pm a\), có thể dùng phân bố chữ nhật:

\[
u=\frac{a}{\sqrt3}
\]

Nếu giá trị gần trung tâm có khả năng cao hơn và hai đầu ít khả năng hơn, mô hình tam giác có thể cho:

\[
u=\frac{a}{\sqrt6}
\]

Việc chọn phân bố phải dựa trên thông tin thật về nguồn sai lệch, không phải chọn công thức nào cho số nhỏ hơn.

## Lan truyền độ không đảm bảo

Với mô hình:

\[
y=f(x_1,\ldots,x_n)
\]

xấp xỉ bậc nhất cho độ không đảm bảo chuẩn kết hợp là:

\[
u_c^2(y)=\sum_i\left(\frac{\partial f}{\partial x_i}\right)^2u^2(x_i)
+2\sum_{i<j}\frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j}u(x_i,x_j)
\]

Các đạo hàm:

\[
c_i=\frac{\partial f}{\partial x_i}
\]

được gọi là **hệ số nhạy (sensitivity coefficient)**. Chúng cho biết một thay đổi nhỏ ở từng đầu vào ảnh hưởng kết quả mạnh đến mức nào.

Hạng hiệp phương sai \(u(x_i,x_j)\) rất quan trọng nếu các đầu vào có tương quan. Bỏ qua tương quan có thể làm đánh giá độ không đảm bảo quá lớn hoặc quá nhỏ.

### Ví dụ: nồng độ từ khối lượng và thể tích

Nếu:

\[
c=\frac{m}{MV}
\]

và xem \(M\) là hằng số tham chiếu, \(m\) và \(V\) độc lập, thì gần đúng:

\[
\left(\frac{u_c}{c}\right)^2\approx
\left(\frac{u_m}{m}\right)^2+
\left(\frac{u_V}{V}\right)^2
\]

Nếu độ không đảm bảo tương đối của thể tích lớn hơn nhiều so với cân, việc mua cân tốt hơn gần như không cải thiện kết quả. Đây là giá trị thực tế của **ngân sách độ không đảm bảo (uncertainty budget)**: nó chỉ ra mắt xích nào đáng đầu tư cải thiện.

## Tương quan và sai lệch chung nguồn

Giả sử hai thể tích đều được đo bằng cùng một pipet bị lệch +0,5%. Sai lệch của chúng không độc lập mà có chung nguồn hiệu chuẩn.

Trong một tỉ số, phần sai lệch chung có thể triệt tiêu một phần. Trong phép cộng hoặc hiệu theo cấu trúc khác, chúng có thể cộng hưởng.

Vì vậy quy tắc “cứ lấy căn tổng bình phương” chỉ đúng khi giả định độc lập là hợp lý.

## Lan truyền bằng Monte Carlo

Phương pháp đạo hàm phù hợp khi độ không đảm bảo nhỏ và mô hình gần tuyến tính trong vùng quan tâm. Với mô hình phi tuyến mạnh, phân bố bất đối xứng, giới hạn vật lý hoặc nhiều tương tác, mô phỏng **Monte Carlo** thường trực quan và bền hơn.

Quy trình cơ bản:

1. gán phân bố hợp lý cho từng đầu vào;
2. lấy mẫu ngẫu nhiên từ các phân bố đó;
3. tính đầu ra qua mô hình hàng nghìn hoặc hàng triệu lần;
4. dùng phân bố đầu ra để ước lượng trung vị, khoảng phủ hoặc độ không đảm bảo.

Đây là điểm nối trực tiếp giữa hóa học, xác suất và lập trình khoa học.

## Độ không đảm bảo mở rộng

Độ không đảm bảo chuẩn kết hợp \(u_c\) có thể nhân với **hệ số phủ (coverage factor)** \(k\):

\[
U=ku_c
\]

Trong nhiều điều kiện gần chuẩn, \(k\approx2\) thường tương ứng xấp xỉ vùng phủ 95%, nhưng ý nghĩa chính xác còn phụ thuộc phân bố và bậc tự do hiệu dụng.

Kết quả có thể báo cáo:

\[
y\pm U\quad(k=2)
\]

và phải nêu rõ cách xác định \(U\), thay vì chỉ viết dấu \(\pm\) mà không giải thích.

## Chữ số có nghĩa không thay thế lý thuyết độ không đảm bảo

Các quy tắc chữ số có nghĩa hữu ích để tránh báo cáo quá nhiều chữ số, nhưng chỉ là quy ước truyền đạt đơn giản.

Trong tính toán nên giữ thêm chữ số bảo vệ rồi làm tròn ở cuối. Một cách trình bày phổ biến là giữ một hoặc hai chữ số có nghĩa cho độ không đảm bảo và làm tròn giá trị đo tới cùng hàng thập phân.

Ví dụ:

```text
12.3478 ± 0.1832
→ 12.35 ± 0.18
```

Viết `12.347800 ± 0.18` tạo ấn tượng sai rằng các chữ số cuối có ý nghĩa thực nghiệm.

# Hồi quy hiệu chuẩn

Một đường hiệu chuẩn tuyến tính đơn giản có dạng:

\[
y=a+bx+\varepsilon
\]

trong đó \(x\) là nồng độ chuẩn đã biết, \(y\) là tín hiệu, \(a\) là hệ số chặn, \(b\) là độ nhạy và \(\varepsilon\) là phần sai lệch chưa được mô hình giải thích.

**Bình phương tối thiểu thông thường (ordinary least squares, OLS)** thường giả định sai số chủ yếu nằm ở trục \(y\), các điểm độc lập và phương sai gần như không đổi.

Trong hóa phân tích, phương sai thường tăng khi nồng độ tăng. Hiện tượng này gọi là **phương sai không đồng nhất (heteroscedasticity)**. Khi đó hồi quy có trọng số (weighted least squares) với trọng số gần \(1/\sigma_i^2\) có thể phù hợp hơn nếu mô hình phương sai được xác lập hợp lý.

## Vì sao \(R^2\) cao chưa đủ

Một đường có \(R^2=0.9999\) vẫn có thể không phù hợp nếu:

- tồn tại độ cong có hệ thống;
- phần dư thay đổi theo nồng độ;
- một điểm biên chi phối toàn bộ đường;
- vùng nồng độ thấp được mô tả kém;
- mẫu trắng có độ chệch;
- phương sai thay đổi mạnh theo tín hiệu.

Vì vậy phải xem đồ thị phần dư, chuẩn kiểm tra độc lập, vùng hiệu chuẩn và sai số dự đoán — không chỉ nhìn một con số \(R^2\).

## Dự đoán ngược từ tín hiệu sang nồng độ

Trong hiệu chuẩn, ta xây mô hình từ nồng độ đã biết tới tín hiệu rồi dùng tín hiệu của mẫu để suy ngược nồng độ. Đây là một **bài toán nghịch đảo (inverse prediction)**.

Độ không đảm bảo của nồng độ suy ra phụ thuộc:

- độ dốc đường chuẩn;
- độ phân tán phần dư;
- số điểm chuẩn;
- cách phân bố điểm chuẩn trên miền;
- số lần đo mẫu;
- độ không đảm bảo của chính dung dịch chuẩn.

Gần tín hiệu mẫu trắng, độ không đảm bảo tương đối thường tăng rất mạnh dù \(R^2\) vẫn gần 1.

## Giới hạn phát hiện và giới hạn định lượng

**Giới hạn phát hiện (limit of detection, LOD)** mô tả mức tín hiệu/nồng độ mà tại đó có thể phân biệt hợp lý chất phân tích với nền hoặc mẫu trắng.

**Giới hạn định lượng (limit of quantitation, LOQ)** yêu cầu độ không đảm bảo đủ nhỏ để báo cáo một con số định lượng có ích.

Không tồn tại một công thức LOD duy nhất đúng cho mọi phương pháp. Một biểu thức đơn giản thường gặp là:

\[
LOD\sim\frac{k\sigma_{blank}}{slope}
\]

nhưng giá trị \(k\), cách ước lượng \(\sigma\), ma trận mẫu và tiêu chí xác nhận phải phù hợp với phương pháp cụ thể.

Báo cáo một nồng độ thấp hơn vùng định lượng đáng tin cậy với nhiều chữ số thập phân là tạo **độ chính xác giả (false precision)**.

## Thu hồi và mẫu thêm chuẩn

Nếu thêm một lượng biết trước \(C_{added}\) vào mẫu:

\[
\%Recovery=
\frac{C_{spiked}-C_{original}}{C_{added}}\times100\%
\]

thì thử nghiệm thu hồi giúp kiểm tra tổn thất chuẩn bị mẫu và hiệu ứng nền. Một phương pháp có thể lặp rất đẹp nhưng thu hồi chỉ 70%; trong trường hợp đó vấn đề là độ chệch chứ không phải độ chụm.

Khoảng thu hồi chấp nhận được phụ thuộc chất phân tích, nồng độ, ma trận và mục tiêu sử dụng; không có một con số phổ quát cho mọi phép đo.

## Vật liệu chuẩn và tính liên kết chuẩn đo lường

Một kết quả có **tính liên kết chuẩn đo lường (metrological traceability)** khi nó có thể liên hệ tới chuẩn tham chiếu thông qua một chuỗi hiệu chuẩn liên tục, được ghi chép, với độ không đảm bảo ở từng mắt xích.

**Vật liệu chuẩn được chứng nhận (certified reference material, CRM)** cung cấp giá trị tham chiếu cùng độ không đảm bảo được xác lập. Dùng CRM không làm thiết bị “hoàn hảo”, nhưng tạo một neo độc lập để kiểm tra độ đúng và chuỗi truy xuất.

## Ngoại lệ dữ liệu không nên bị xóa vì gây khó chịu

Một **điểm ngoại lệ (outlier)** có thể xuất hiện do:

- nhập dữ liệu sai;
- nhiễm bẩn;
- lỗi thiết bị;
- thao tác thất bại;
- hoặc biến thiên hiếm nhưng có thật của mẫu.

Không nên nhìn kết quả rồi xóa điểm làm kết luận “đẹp hơn”. Trước hết cần tìm nguyên nhân có thể quy gán. Các kiểm định ngoại lệ như Grubbs chỉ phù hợp dưới giả định cụ thể và tốt nhất nên được quy định trước trong kế hoạch phân tích.

Nếu dữ liệu vốn có đuôi nặng hoặc phân bố không chuẩn, các phương pháp thống kê bền vững (robust statistics) có thể phù hợp hơn việc xóa điểm.

## Biểu đồ kiểm soát

Các mẫu kiểm soát chất lượng đo lặp theo thời gian có thể được biểu diễn quanh đường trung tâm và giới hạn kiểm soát.

**Biểu đồ kiểm soát (control chart)** giúp phân biệt biến thiên thường gặp của quy trình với dấu hiệu bất thường như drift, thay đổi bậc hoặc xu hướng kéo dài.

Một hệ thống có thể vượt hiệu chuẩn hôm nay nhưng trôi dần trong nhiều tuần. Theo dõi theo thời gian phát hiện vấn đề mà một lần hiệu chuẩn đơn lẻ không thấy được.

## Kiểm định giả thuyết và giá trị p

**Giá trị p (p-value)** là xác suất, dưới mô hình giả thuyết không, quan sát dữ liệu ít nhất cực đoan như dữ liệu thu được. Nó **không** phải xác suất giả thuyết không là đúng.

Một khác biệt có ý nghĩa thống kê chưa chắc có ý nghĩa hóa học hay thực tiễn. Với cỡ mẫu rất lớn, một khác biệt cực nhỏ có thể cho p rất thấp nhưng không có giá trị ứng dụng.

Vì vậy nên báo cáo đồng thời **kích thước hiệu ứng (effect size)**, khoảng tin cậy và bối cảnh hóa học.

## Nhiều phép so sánh làm tăng dương tính giả

Nếu kiểm tra 100 giả thuyết độc lập với ngưỡng \(\alpha=0.05\), ngay cả khi tất cả giả thuyết không đều đúng, ta vẫn kỳ vọng xuất hiện một số kết quả “có ý nghĩa” chỉ do ngẫu nhiên.

Trong dữ liệu phổ, omics hoặc sàng lọc nhiều hợp chất, cần cân nhắc điều chỉnh nhiều phép kiểm định hoặc kiểm soát **tỷ lệ phát hiện sai (false discovery rate, FDR)**.

## Thanh sai số phải được ghi rõ nghĩa

Một thanh sai số trên đồ thị có thể biểu diễn:

- độ lệch chuẩn SD;
- sai số chuẩn SE;
- khoảng tin cậy CI;
- hoặc độ không đảm bảo đo.

Nếu không ghi rõ, người đọc không thể biết nó mô tả độ phân tán dữ liệu hay độ không chắc của trung bình.

## Biến đổi dữ liệu

Biến đổi logarit có thể hữu ích khi sai số mang tính nhân hoặc khi quan hệ vật lý là hàm mũ. Tuy nhiên biến đổi dữ liệu đồng thời thay đổi mô hình sai số; việc chuyển ngược về thang ban đầu có thể gây độ chệch.

Do đó không nên chọn biến đổi chỉ vì đồ thị “trông thẳng hơn”. Cần hỏi mô hình nào phù hợp với cơ chế tạo dữ liệu.

# Phân tích dữ liệu có thể học trực tiếp từ kỹ thuật phần mềm

Với bộ dữ liệu lớn, một pipeline tốt nên có dạng:

```text
dữ liệu thô bất biến
→ làm sạch bằng script có thể lặp lại
→ phân tích
→ hình/bảng/kết quả
```

Không ghi đè dữ liệu thô. Các bước xử lý nên được thể hiện bằng mã nguồn hoặc quy trình có thể tái tạo. Quản lý phiên bản cho biết phân tích thay đổi khi nào; kiểm thử tự động có thể bắt lỗi chuyển đơn vị hoặc công thức; file môi trường giúp khóa phiên bản thư viện phần mềm.

Bảng tính vẫn hữu ích cho kiểm tra trực quan và phép tính đơn giản, nhưng trở nên rủi ro khi workflow phụ thuộc copy/paste thủ công, công thức ẩn và chỉnh sửa không có lịch sử.

## Ví dụ về ngân sách độ không đảm bảo

Giả sử nồng độ cuối chịu các thành phần độ không đảm bảo tương đối:

- độ tinh khiết chuẩn: 0,20%;
- cân: 0,05%;
- bình định mức: 0,10%;
- đường hiệu chuẩn: 1,20%;
- độ lặp lại chuẩn bị mẫu: 0,80%.

Nếu các thành phần gần độc lập:

\[
u_r=\sqrt{0.20^2+0.05^2+0.10^2+1.20^2+0.80^2}\%\]

Hai thành phần chi phối là đường hiệu chuẩn và chuẩn bị mẫu. Giảm độ không đảm bảo của cân từ 0,05% xuống 0,005% gần như không thay đổi tổng thể.

Đây là cách ngân sách độ không đảm bảo biến thống kê thành quyết định kỹ thuật: **cải thiện mắt xích đang chi phối, không tối ưu mắt xích vốn đã quá tốt**.

# Những hiểu lầm thường gặp

### “Sai số và độ không đảm bảo là một”

Không. Sai số là độ lệch so với giá trị thật/tham chiếu; độ không đảm bảo mô tả giới hạn tri thức về kết quả.

### “Đo lặp nhiều lần sẽ loại bỏ mọi độ không đảm bảo”

Không. Đo lặp giảm thành phần ngẫu nhiên của trung bình nhưng không tự sửa độ chệch, mẫu không đại diện hoặc sai mô hình.

### “Khoảng tin cậy 95% nghĩa là xác suất giá trị thật nằm trong khoảng này là 95%”

Không theo diễn giải tần suất nghiêm ngặt. 95% mô tả tính chất của quy trình tạo khoảng qua nhiều lần lặp giả định.

### “\(R^2\) gần 1 chứng minh phương pháp phân tích tốt”

Không. Cần xem phần dư, độ chệch, nền mẫu, kiểm chuẩn độc lập và sai số dự đoán trong vùng quan tâm.

### “Chữ số có nghĩa là phân tích độ không đảm bảo nghiêm ngặt”

Không. Chữ số có nghĩa chỉ là quy ước báo cáo gần đúng.

### “Phần mềm cho ra số nên kết quả khách quan”

Phần mềm chỉ thực hiện mô hình và lựa chọn đã được lập trình. Kết quả vẫn phụ thuộc giả định, tiền xử lý, dữ liệu đầu vào và lỗi mã nguồn.

# Mô hình tư duy

Hãy xem mỗi con số báo cáo như **đầu ra của một mô hình đo cùng một phân bố độ không đảm bảo**, chứ không phải một điểm tuyệt đối. Muốn biết có nên tin con số đó hay không, phải truy ngược chuỗi: mẫu được lấy như thế nào, tín hiệu được tạo ra sao, chuẩn nào neo phép đo, biến thiên và độ chệch xuất hiện ở đâu, chúng truyền qua công thức ra sao, và dữ liệu có thực sự hỗ trợ số chữ số cũng như kết luận được báo cáo hay không.

Xem thêm: [Hóa học và Toán học](../90_connections/chemistry_and_mathematics.md).