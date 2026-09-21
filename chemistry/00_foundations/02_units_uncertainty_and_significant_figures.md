# Đơn vị, độ không đảm bảo và chữ số có nghĩa

Hóa học là một khoa học định lượng. Khi nói một phản ứng “nhanh”, một dung dịch “đậm đặc” hay một vật “nặng”, ta mới chỉ có mô tả định tính. Muốn so sánh, kiểm chứng và tính toán, ta cần **phép đo (measurement)**. Nhưng phép đo không bao giờ hoàn toàn tách khỏi giới hạn của thiết bị và phương pháp.

Vì vậy một con số trong Hóa học phải luôn được đọc cùng ba câu hỏi: **đại lượng gì, đơn vị gì, và độ tin cậy tới đâu?**

## Đơn vị SI và các đơn vị dẫn xuất

Hệ SI (**International System of Units / 국제단위계**) cung cấp một chuẩn chung để phép đo có thể so sánh giữa các phòng thí nghiệm và quốc gia.

Trong Hóa học, một số đơn vị cơ bản và đơn vị dẫn xuất xuất hiện thường xuyên:

| Đại lượng | Đơn vị SI | Ký hiệu | Tiếng Hàn |
|---|---|---|---|
| chiều dài (length) | mét (metre) | `m` | 미터 |
| khối lượng (mass) | kilogram | `kg` | 킬로그램 |
| thời gian (time) | giây (second) | `s` | 초 |
| nhiệt độ (temperature) | kelvin | `K` | 켈빈 |
| lượng chất (amount of substance) | mol (mole) | `mol` | 몰 |
| cường độ dòng điện (electric current) | ampere | `A` | 암페어 |

Trong phòng thí nghiệm, gram, milliliter, centimeter và độ Celsius thường thuận tiện hơn. Việc dùng đơn vị không phải đơn vị cơ bản không có vấn đề nếu phép đổi rõ ràng và nhất quán.

## Tiền tố là cách quản lý thang độ lớn

Hóa học trải rộng từ thang nguyên tử tới thang vĩ mô. **Tiền tố đơn vị (prefix)** giúp biểu diễn các thang này mà không phải viết quá nhiều số 0.

Ví dụ:

\[
1\;\mathrm{nm}=10^{-9}\;\mathrm{m}
\]

\[
1\;\mathrm{\mu L}=10^{-6}\;\mathrm{L}
\]

\[
1\;\mathrm{mmol}=10^{-3}\;\mathrm{mol}
\]

Điều quan trọng không phải học thuộc mọi tiền tố mà là nhìn chúng như lũy thừa của 10. Khi đó đổi đơn vị trở thành một bài đại số với lũy thừa.

## Phân tích thứ nguyên như một hệ thống kiểm tra logic

**Phân tích thứ nguyên (dimensional analysis / 차원 분석)** dùng đơn vị như các thừa số đại số.

Giả sử khối lượng riêng là `1.25 g/mL` và thể tích là `40.0 mL`. Khối lượng phải là:

\[
m=\rho V
\]

\[
m=1.25\frac{\mathrm{g}}{\mathrm{mL}}\times40.0\;\mathrm{mL}=50.0\;\mathrm{g}
\]

`mL` triệt tiêu và còn lại `g`, đúng với thứ nguyên của khối lượng. Nếu kết quả cuối cùng vẫn còn `g/mL`, đó là dấu hiệu phương trình hoặc cách thiết lập phép tính sai.

Phân tích thứ nguyên vì vậy giống một dạng **kiểm tra kiểu dữ liệu (type checking)** trong lập trình. Trình biên dịch có thể ngăn thao tác giữa các kiểu dữ liệu không tương thích; trong Vật lý và Hóa học, đơn vị giúp phát hiện một số lỗi đại số tương tự.

## Độ đúng và độ chụm không đồng nghĩa

Hai khái niệm này thường bị dùng lẫn.

**Độ đúng (accuracy / 정확도)** mô tả mức độ gần với giá trị tham chiếu hoặc giá trị được chấp nhận.

**Độ chụm (precision / 정밀도)** mô tả mức độ gần nhau giữa nhiều phép đo lặp lại.

Một cân bị lệch hiệu chuẩn có thể cho `10.52, 10.52, 10.53 g` khi giá trị đúng là `10.00 g`. Dữ liệu có độ chụm cao nhưng độ đúng thấp.

Ngược lại, một thiết bị có nhiều nhiễu có thể cho `9.8, 10.2, 10.0 g`. Trung bình gần giá trị đúng nhưng từng phép đo có độ chụm kém.

## Sai số ngẫu nhiên và sai số hệ thống

**Sai số ngẫu nhiên (random error / 우연 오차)** thay đổi không hoàn toàn dự đoán được giữa các phép đo. Nhiễu điện tử, dao động nhỏ của môi trường hoặc giới hạn đọc thang đo có thể tạo sai số ngẫu nhiên. Lặp lại phép đo và lấy trung bình thường giúp giảm ảnh hưởng của loại sai số này.

**Sai số hệ thống (systematic error / 계통 오차)** đẩy kết quả theo một hướng tương đối nhất quán. Hiệu chuẩn sai, lệch điểm không hoặc thiên lệch của quy trình là các ví dụ. Lặp lại nhiều lần không tự sửa sai số hệ thống; cần tìm nguyên nhân và hiệu chỉnh phương pháp.

Đây là lý do “đo nhiều lần” không đồng nghĩa với “đúng hơn” trong mọi tình huống.

## Độ không đảm bảo: phép đo không phải một điểm tuyệt đối

Nếu một burette được đọc là `23.42 mL`, giá trị thật không nên được hình dung như một điểm hoàn hảo chính xác vô hạn. Kết quả đo tốt hơn nên được hiểu như một ước lượng kèm **độ không đảm bảo (uncertainty)**.

Có thể biểu diễn đơn giản:

\[
x = x_{measured} \pm u
\]

trong đó `u` là ước lượng độ không đảm bảo.

Ví dụ:

\[
V = 23.42 \pm 0.02\;\mathrm{mL}
\]

Điều này không có nghĩa giá trị thật chắc chắn nằm trong khoảng trên với xác suất 100%. Ý nghĩa chính xác phụ thuộc cách độ không đảm bảo được xây dựng. Trong **đo lường học (metrology)**, độ không đảm bảo được xử lý bằng khuôn khổ thống kê và hiệu chuẩn rõ ràng.

## Chữ số có nghĩa tồn tại để làm gì?

**Chữ số có nghĩa (significant figures / 유효숫자)** là quy ước giúp tránh báo cáo mức độ chính xác cao hơn dữ liệu thực sự hỗ trợ.

Nếu cân chỉ đọc tới `0.01 g`, báo cáo `12.340000 g` tạo ảo giác rằng thiết bị biết thêm nhiều chữ số mà nó không đo được.

Vì vậy chữ số có nghĩa là một cách truyền đạt giới hạn độ phân giải, không phải một quy luật tự nhiên.

### Nhận diện chữ số có nghĩa

Các chữ số khác 0 thường có nghĩa. Số 0 nằm giữa các chữ số khác 0 thường có nghĩa. Các số 0 đứng đầu chỉ định vị dấu thập phân nên không được tính là chữ số có nghĩa.

Ví dụ:

- `0.00450` có 3 chữ số có nghĩa: `4`, `5` và số 0 cuối;
- `1002` có 4 chữ số có nghĩa;
- `1500` có thể mơ hồ nếu không có cách ghi rõ.

**Ký hiệu khoa học (scientific notation)** loại bỏ sự mơ hồ:

\[
1.5\times10^3
\]

có 2 chữ số có nghĩa, còn:

\[
1.500\times10^3
\]

có 4.

## Quy tắc khi tính toán

Với phép nhân hoặc chia, kết quả thường được báo cáo với số chữ số có nghĩa bằng đầu vào có ít chữ số có nghĩa nhất.

Ví dụ:

\[
2.34\times1.2=2.808
\]

`1.2` có 2 chữ số có nghĩa nên kết quả được báo cáo là:

\[
2.8
\]

Với phép cộng hoặc trừ, giới hạn phụ thuộc vị trí thập phân chứ không phải tổng số chữ số có nghĩa.

\[
12.11+0.3=12.41
\]

`0.3` chỉ chính xác tới hàng phần mười, nên kết quả hợp lý là `12.4`.

Đây là quy ước đơn giản hóa. Trong khoa học thực nghiệm nghiêm túc, **lan truyền độ không đảm bảo (uncertainty propagation)** trực tiếp tốt hơn việc chỉ dựa vào quy tắc chữ số có nghĩa.

## Không làm tròn quá sớm

Một lỗi phổ biến là làm tròn kết quả trung gian ở từng bước. Điều này có thể tích lũy sai số làm tròn.

Giả sử cần tính:

\[
\frac{12.37\times3.42}{1.89}
\]

Nếu làm tròn mạnh ở mỗi bước, giá trị cuối có thể lệch. Cách tốt là giữ các chữ số bảo vệ trong quá trình tính và chỉ làm tròn ở kết quả cuối được báo cáo.

Máy tính có thể giữ nhiều chữ số, nhưng nhiều chữ số trong bộ nhớ không đồng nghĩa phép đo thực tế có độ chính xác tương ứng.

## Celsius và Kelvin

Phép đổi giữa Celsius và Kelvin:

\[
T(K)=T(^\circ C)+273.15
\]

Kelvin là **thang nhiệt độ nhiệt động tuyệt đối (absolute thermodynamic temperature scale)**. `0 K` tương ứng với độ không tuyệt đối trong giới hạn lý tưởng của nhiệt động lực học.

Một chênh lệch `1 K` bằng một chênh lệch `1 °C`, nhưng hai thang có điểm 0 khác nhau.

Nhiều phương trình vật lý–hóa học như phương trình khí lý tưởng hay phương trình Arrhenius yêu cầu nhiệt độ tuyệt đối tính bằng kelvin. Dùng Celsius trực tiếp có thể làm phương trình mất ý nghĩa vật lý.

## Ký hiệu khoa học và thang logarithm

Ký hiệu khoa học đặc biệt quan trọng vì Hóa học thường xử lý các con số từ rất nhỏ tới rất lớn.

Bán kính nguyên tử có thể cỡ:

\[
10^{-10}\;\mathrm{m}
\]

trong khi một mol chứa khoảng:

\[
6.022\times10^{23}
\]

hạt.

Ngoài lũy thừa của 10, Hóa học còn dùng các **thang logarithm (logarithmic scales)** như pH. Logarithm xuất hiện vì nồng độ có thể trải qua nhiều bậc độ lớn. Ta sẽ giải thích bản chất của logarithm khi học acid–base thay vì chỉ học công thức `pH = -log[H+]`.

## Lan truyền độ không đảm bảo: ý tưởng nền tảng

Nếu kết quả được tính từ nhiều đại lượng đo, độ không đảm bảo của kết quả phụ thuộc độ không đảm bảo của các đầu vào.

Ví dụ:

\[
\rho=\frac{m}{V}
\]

Nếu cả khối lượng và thể tích đều có độ không đảm bảo, khối lượng riêng cũng phải có độ không đảm bảo. Nếu thể tích khó đo chính xác hơn nhiều so với khối lượng, phần không đảm bảo của thể tích có thể chi phối kết quả cuối.

Ý tưởng này quan trọng hơn việc thuộc từng công thức lan truyền: **chuỗi đo chỉ mạnh bằng những mắt xích có độ không đảm bảo lớn nhất**.

Trong hóa học phân tích và kỹ thuật thiết bị, đây là nền tảng để thiết kế thí nghiệm.

## Mô hình tư duy

Hãy coi mỗi số đo như một **đối tượng dữ liệu có siêu dữ liệu (data object with metadata)** chứ không chỉ là một số thực.

Nó mang theo:

- loại đại lượng;
- đơn vị;
- độ phân giải;
- độ không đảm bảo;
- phương pháp đo;
- bối cảnh hiệu chuẩn.

Viết `12.34` mà bỏ đơn vị và độ không đảm bảo giống như truyền một giá trị qua hệ thống nhưng làm mất thông tin về cấu trúc và kiểu dữ liệu.

## Các hiểu lầm thường gặp

### “Nhiều chữ số thập phân nghĩa là đúng hơn”

Không. Số chữ số thập phân chỉ thể hiện cách viết. Độ đúng phụ thuộc mức độ gần giá trị tham chiếu và chất lượng của toàn bộ quá trình đo.

### “Chữ số có nghĩa cho biết chính xác độ không đảm bảo”

Không. Chúng chỉ là quy ước thô để báo cáo độ chính xác. Hai phép đo có cùng số chữ số có nghĩa vẫn có thể có phân bố độ không đảm bảo rất khác nhau.

### “Lặp thí nghiệm đủ nhiều sẽ loại bỏ mọi sai số”

Lặp lại giúp xử lý biến thiên ngẫu nhiên, nhưng sai số hệ thống có thể vẫn tồn tại nguyên vẹn.

## Liên kết kiến thức

Sau khi biết cách quan sát và đo, ta cần một ngôn ngữ để biểu diễn thành phần và biến đổi của vật chất. Đó là vai trò của ký hiệu, công thức, phương trình và mô hình hóa học.

Xem tiếp: [Ngôn ngữ và mô hình hóa học](./03_chemical_language_and_models.md).