# Vật lý thực nghiệm: hiệu chuẩn, độ bất định, khớp dữ liệu và suy luận

## Một lý thuyết phải đối chiếu được với quan sát

Vật lý là khoa học thực nghiệm. Một mô hình (model) có thể đẹp về toán học, có đối xứng rõ ràng và nhất quán nội tại, nhưng giá trị khoa học của nó phụ thuộc vào việc tạo ra dự đoán có thể so sánh với quan sát. Vật lý thực nghiệm (experimental physics / 실험물리학) vì vậy không chỉ là thu thập thật nhiều số liệu; nó là quá trình thiết kế phép đo sao cho một đại lượng vật lý được biến thành tín hiệu quan sát được, đồng thời hiểu rõ thiết bị, nhiễu, sai lệch và độ bất định đi kèm.

Vật lý tính toán (computational physics / 계산물리학) bổ sung cho quá trình này bằng các phương pháp số (numerical methods). Ta dùng chúng khi phương trình quá phức tạp để giải chính xác bằng giải tích, hoặc khi cần suy ra tham số của mô hình từ dữ liệu thực nghiệm.

## Chuỗi đo lường

Một phép đo hiếm khi đọc trực tiếp đại lượng cần biết. Với cảm biến nhiệt độ, chuỗi đo có thể được hình dung như sau:

```text
nhiệt độ
→ tính chất vật liệu thay đổi
→ điện áp hoặc điện trở thay đổi
→ mạch tương tự
→ bộ chuyển đổi ADC
→ hàm hiệu chuẩn
→ nhiệt độ được báo cáo
```

Mỗi bước có một hàm truyền (transfer function), mức nhiễu (noise), độ phi tuyến và khả năng tạo sai lệch (bias). Vì vậy khi phần mềm hiển thị `23.7 °C`, con số đó là kết quả cuối của cả một chuỗi vật lý–điện tử–tính toán, chứ không phải giá trị được lấy trực tiếp từ tự nhiên.

## Hiệu chuẩn

Hiệu chuẩn (calibration / 교정) là quá trình so sánh đáp ứng của thiết bị với chuẩn hoặc giá trị tham chiếu đã biết để xây dựng quan hệ giữa tín hiệu thô và đại lượng vật lý.

Nếu cảm biến gần tuyến tính,

```math
V=aT+b,
```

thì các phép đo chuẩn cho phép ước lượng `a` và `b`. Với cảm biến phi tuyến, quan hệ có thể là

```math
V=f(T),
```

và ta cần xác định hoặc khớp hàm ngược để suy ra `T` từ `V`.

Hiệu chuẩn không loại bỏ hoàn toàn độ bất định. Bản thân giá trị chuẩn, phép khớp và độ ổn định của thiết bị đều có độ bất định, nên chúng phải được truyền tới kết quả cuối.

## Sai số ngẫu nhiên và sai số hệ thống

Sai số ngẫu nhiên (random error) làm các lần đo dao động quanh một giá trị. Nếu các phép đo độc lập, có cùng phân bố và độ lệch chuẩn `\sigma`, độ bất định của giá trị trung bình thường giảm gần theo

```math
\sigma_{\bar x}=\frac{\sigma}{\sqrt N}.
```

Tuy nhiên quy luật này không tự động đúng khi dữ liệu có tương quan theo thời gian, trôi chậm hoặc nhiễu có cấu trúc.

Sai số hệ thống (systematic error) khác về bản chất. Nếu nhiệt kế luôn lệch `+0.5 °C`, đo một triệu lần có thể làm giá trị trung bình rất ổn định nhưng vẫn sai khoảng `0.5 °C`. Vì vậy cần phân biệt **độ chụm (precision)**, tức mức độ các phép đo lặp lại gần nhau, với **độ đúng (accuracy)**, tức mức độ kết quả gần giá trị thực hoặc giá trị tham chiếu.

## Lan truyền độ bất định

Nếu đại lượng cần tính là

```math
y=f(x_1,x_2,\ldots),
```

và các độ bất định đủ nhỏ, với các biến gần độc lập, ta có xấp xỉ

```math
\sigma_y^2\approx
\sum_i\left(\frac{\partial f}{\partial x_i}\right)^2\sigma_i^2.
```

Nếu các biến có tương quan, phải bổ sung các hạng hiệp phương sai (covariance). Công thức cho thấy đạo hàm không chỉ mô tả tốc độ biến thiên; nó còn đo độ nhạy của kết quả đối với độ bất định của từng đầu vào.

## Chữ số có nghĩa không thay thế phân tích độ bất định

Quy tắc chữ số có nghĩa (significant figures) chỉ là quy ước trình bày. Một kết quả như

```math
L=(12.43\pm0.02)\,cm
```

mang nhiều thông tin hơn việc viết rất nhiều chữ số thập phân mà không giải thích độ tin cậy. Khi độ chính xác quan trọng, cần nêu cách đo, độ bất định và điều kiện thực nghiệm chứ không chỉ làm tròn số.

## Khớp dữ liệu không phải là chứng minh lý thuyết

Giả sử mô hình dự đoán

```math
y=ax+b.
```

Phương pháp bình phương tối thiểu (least squares) có thể ước lượng tham số bằng cách tối thiểu hóa

```math
\chi^2=\sum_i\frac{(y_i-y_{model,i})^2}{\sigma_i^2}.
```

Một phép khớp tốt cho thấy dữ liệu tương thích với mô hình dưới những giả định đã chọn; nó không tự chứng minh mô hình là nguyên nhân duy nhất hay mô tả đúng bản chất. Nhiều mô hình khác nhau có thể khớp tốt cùng một tập dữ liệu hữu hạn.

Phần dư (residual) rất quan trọng. Nếu phần dư có cấu trúc thay vì phân bố ngẫu nhiên, mô hình có thể đang bỏ sót một cơ chế vật lý, một xu hướng phi tuyến hoặc một sai lệch của thiết bị.

## Kiểm định giả thuyết và mức ý nghĩa

Kiểm định giả thuyết (hypothesis testing) đánh giá mức độ dữ liệu không tương thích với một giả thuyết nền. Trong vật lý hạt, ngưỡng “5 sigma” là một quy ước rất nghiêm ngặt nhằm hạn chế phát hiện giả trong bối cảnh có nhiều phép tìm kiếm và nhiều nguồn sai số hệ thống. Nó không có nghĩa đơn giản rằng giả thuyết mới “đúng với xác suất 99.999...%”.

Cách tiếp cận tần suất (frequentist) và Bayes (Bayesian) trả lời những câu hỏi xác suất khác nhau. Khi đọc kết quả thống kê, cần biết mô hình xác suất, hàm hợp lý (likelihood), giả định và phân bố tiên nghiệm (prior) nếu có.

## Kiểm chứng mô hình và mô phỏng

Trước khi tin một kết quả số, nên kiểm tra nhiều lớp độc lập: thứ nguyên có đúng không, nghiệm có trở về trường hợp giải tích đã biết không, kết quả có hội tụ khi giảm bước lưới hoặc bước thời gian không, các định luật bảo toàn có được giữ trong phạm vi mong đợi không, và bậc độ lớn có hợp lý không.

Nếu mô phỏng quỹ đạo Trái Đất trong bài toán hai vật thể bảo toàn mà năng lượng giảm hàng chục phần trăm sau mỗi vòng, không nên vội diễn giải đó là một hiệu ứng vật lý mới. Khả năng đầu tiên cần kiểm tra là bộ tích phân số (numerical integrator), bước thời gian và cách cài đặt phương trình.

## Ước lượng Fermi và bậc độ lớn

Ước lượng Fermi (Fermi estimate) chia một đại lượng khó biết thành các yếu tố có thể ước lượng. Ví dụ lượng dữ liệu do `N` cảm biến tạo ra có thể ước lượng bằng

```math
D\sim N\times f_s\times \text{bytes/sample}\times t.
```

Mục tiêu không phải có con số chính xác ngay từ đầu mà là biết thang giá trị hợp lý. Một ước lượng tốt có thể phát hiện kết quả sai `10^3` hay `10^6` lần trước khi các phép tính chi tiết che mất trực giác.

## Mô hình tư duy (Mental Model)

Thí nghiệm không trả về “sự thật trực tiếp”. Nó trả về tín hiệu đã đi qua thiết bị, hiệu chuẩn, nhiễu và quy trình xử lý. Suy luận khoa học phải tách được đáp ứng của thiết bị, độ bất định và giả định của mô hình trước khi biến tín hiệu thành một kết luận vật lý.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nhiều dữ liệu sẽ xóa mọi sai số”

Không. Tăng số mẫu thường giúp giảm một số thành phần ngẫu nhiên, nhưng không tự sửa sai số hệ thống, trôi thiết bị hoặc mô hình sai.

### “Mô phỏng đúng nếu chương trình không có lỗi”

Không. Ngoài lỗi lập trình còn có sai số mô hình, sai số rời rạc hóa (discretization error), điều kiện biên sai, độ bất định tham số và mất ổn định số.

### “Học máy có thể thay thế mọi mô hình vật lý”

Học máy (machine learning) có thể xấp xỉ quan hệ rất phức tạp, nhưng khả năng ngoại suy, bảo toàn đại lượng, giải thích nhân quả và phạm vi dữ liệu huấn luyện vẫn là các giới hạn quan trọng. Các phương pháp kết hợp vật lý và dữ liệu thường hữu ích khi hai nguồn thông tin bổ sung cho nhau.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Đại lượng, đơn vị và độ bất định](../00_foundations/01_measurement_units_uncertainty.md).

**Liên hệ tiếp:** [Tín hiệu, nhiễu và lấy mẫu](01_signals_sampling_noise.md), [Vật lý tính toán](02_computational_physics.md).
