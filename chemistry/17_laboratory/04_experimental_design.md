# Thiết kế thí nghiệm — biến câu hỏi thành bằng chứng có thể diễn giải

> Một thí nghiệm hóa học không chỉ là “làm theo quy trình rồi ghi con số”. Nó là một **hệ thống suy luận được thiết kế có chủ ý**: thay đổi hoặc quan sát các biến đã định nghĩa, kiểm soát những giải thích thay thế, đo bằng phương pháp có giới hạn đã biết và thu đủ bằng chứng độc lập để phân biệt hiệu ứng hóa học thật với nhiễu, sai lệch hoặc yếu tố gây nhiễu.

Tăng số phép đo không thể cứu một câu hỏi được đặt sai. Việc đầu tiên là xác định **so sánh nào thực sự trả lời câu hỏi**.

## Bắt đầu từ câu hỏi nhân quả hoặc mô tả

Ví dụ:

- tăng nhiệt độ có làm tốc độ phản ứng tăng khi các điều kiện khác giữ nguyên không?
- nồng độ Fe trong mẫu nước này là bao nhiêu?
- chất xúc tác nào cho độ chọn lọc cao nhất ở cùng mức chuyển hóa?
- một xử lý có làm tốc độ ăn mòn thay đổi không?

Những câu hỏi này cần thiết kế khác nhau.

Thí nghiệm nhân quả chủ động thay đổi một yếu tố và hỏi điều gì thay đổi do chính yếu tố đó. Phép đo phân tích lại có thể chỉ nhằm ước lượng một đại lượng chưa biết với hệ hiệu chuẩn có khả năng truy xuất. Thí nghiệm sàng lọc có thể nhằm tìm những yếu tố quan trọng trước khi cơ chế được hiểu đầy đủ.

## Định nghĩa biến theo cách có thể đo

Câu “phản ứng nhanh hơn” còn mơ hồ nếu chưa định nghĩa cách đo.

Có thể dùng tốc độ ban đầu \(dC/dt\) gần \(t=0\), chu kỳ bán rã, thời gian đạt 90% chuyển hóa hoặc hằng số tốc độ biểu kiến từ mô hình động học.

Tương tự, “hiệu suất” có thể nghĩa hiệu suất khối lượng phân lập, phần trăm diện tích GC hoặc mức chuyển hóa.

Định nghĩa thao tác rõ ràng ngăn việc thay đổi cách hiểu sau khi đã nhìn dữ liệu.

## Đơn vị thí nghiệm và tính độc lập

**Đơn vị thí nghiệm (experimental unit)** là đơn vị nhỏ nhất được gán điều kiện xử lý độc lập.

Nếu chỉ có một bình phản ứng được pha rồi tiêm HPLC ba lần, ba chromatogram là **lặp kỹ thuật (technical replicate)** chứ không phải ba thí nghiệm độc lập. Chúng đo độ lặp lại của tiêm mẫu và thiết bị nhưng cùng chia sẻ mọi sai số từ một lần tổng hợp.

Ba bình được chuẩn bị độc lập lại cung cấp thông tin mạnh hơn về biến thiên của cả quá trình.

Nhầm lặp kỹ thuật với lặp độc lập gọi là **giả lặp (pseudoreplication)** và thường làm độ không đảm bảo bị đánh giá thấp một cách giả tạo.

## Mẫu trắng và đối chứng

### Mẫu trắng

**Mẫu trắng (blank)** chứa mọi thành phần ngoại trừ chất phân tích hoặc thành phần phản ứng chính, dùng để đo nền từ thuốc thử, dung môi, bình chứa và thiết bị.

Ví dụ có mẫu trắng dung môi trong quang phổ, mẫu trắng thuốc thử trong chuẩn độ hoặc mẫu trắng phương pháp đi qua toàn bộ bước tiêu hủy/chiết.

### Đối chứng âm

Điều kiện được kỳ vọng không tạo hiệu ứng mục tiêu. Nó giúp phát hiện nhiễm bẩn hoặc đáp ứng không đặc hiệu.

### Đối chứng dương

Hệ đã biết có khả năng tạo đáp ứng. Nó xác minh rằng phương pháp có thể phát hiện hiệu ứng khi hiệu ứng thực sự tồn tại.

### Đối chứng nền mẫu

Trong hóa phân tích, nền không chứa chất phân tích hoặc nền được thêm chuẩn giúp kiểm tra xem thành phần mẫu có thay đổi hiệu suất chiết hay tín hiệu đầu dò không.

Đối chứng về bản chất là công cụ phát hiện **các giải thích thay thế**.

## Lặp lại

Lặp lại giúp ước lượng biến thiên và cho phép suy luận thống kê.

**Lặp kỹ thuật** là đo lại cùng một mẫu đã chuẩn bị, chủ yếu phản ánh độ chụm thiết bị.

**Lặp chuẩn bị/quy trình** là chuẩn bị mẫu độc lập từ cùng vật liệu, vì vậy đưa thêm biến thiên của pipette, chiết, tiêu hủy và các thao tác khác.

**Lặp độc lập hoặc lặp sinh học** lấy từ các nguồn độc lập, phản ánh biến thiên thật giữa đơn vị mẫu hoặc quần thể.

Số lần lặp phù hợp phụ thuộc phương sai dự kiến, kích thước hiệu ứng và mức tin cậy cần đạt. “Ba lần lặp” là quy ước thường gặp chứ không phải định luật thống kê.

## Ngẫu nhiên hóa

Giả sử chất xúc tác A luôn được chạy trước B rồi C, trong khi nhiệt độ thiết bị tăng dần hoặc cột suy giảm theo thời gian. Khi đó danh tính chất xúc tác bị trộn với thời gian.

Ngẫu nhiên hóa thứ tự chạy giúp phân bố xu hướng thời gian giữa các nhóm.

Ngẫu nhiên hóa không làm drift biến mất; nó chỉ ngăn drift luôn đi cùng một điều kiện xử lý.

## Chặn theo yếu tố gây nhiễu đã biết

Nếu một yếu tố phi mục tiêu đã biết rõ, có thể nhóm các đơn vị tương tự thành **khối (block)**.

Ví dụ block có thể là ngày đo, thiết bị, lô thuốc thử, lô wafer hoặc nguồn mẫu.

So sánh xử lý bên trong mỗi block cho phép mô hình thống kê tách biến thiên do block khỏi hiệu ứng cần nghiên cứu.

## Làm mù

Khi phép đo chứa quyết định chủ quan như đọc điểm cuối, chấm ảnh microscopy hoặc chọn peak, biết trước điều kiện mẫu có thể ảnh hưởng phán đoán.

**Làm mù (blinding)** danh tính mẫu giúp giảm sai lệch quan sát.

Phân tích tự động cũng có thể bị bias nếu tham số được chỉnh sau khi người phân tích đã nhìn nhãn nhóm, vì vậy tự động hóa không tự động loại bỏ thiên lệch.

## Hiệu chuẩn là một phần của thiết kế

Đường hiệu chuẩn chính là một thí nghiệm xây dựng quan hệ giữa đầu vào đã biết và tín hiệu thiết bị.

Một hiệu chuẩn tốt nên bao phủ vùng nồng độ mẫu, có đủ điểm để kiểm tra hình dạng mô hình, dùng chuẩn độc lập khi có thể, không dựa duy nhất vào `R²` và có mẫu kiểm soát chất lượng không dùng để fit đường.

Ngoại suy ngoài vùng hiệu chuẩn giả định đáp ứng vẫn giữ nguyên ở nơi chưa từng được kiểm nghiệm.

## Phương pháp thêm chuẩn cho ảnh hưởng nền

Khi nền mẫu thay đổi độ nhạy, có thể thêm các lượng chất phân tích đã biết trực tiếp vào nhiều phần của chính mẫu rồi fit tín hiệu theo lượng bổ sung.

Ngoại suy về tín hiệu 0 cho phép ước lượng lượng ban đầu.

Cách này hiệu chỉnh một số ảnh hưởng nền vì chuẩn và mẫu cùng nền, nhưng tốn thêm phép đo và giả định ảnh hưởng nền tương đối ổn định trong dải bổ sung.

## Thiết kế nhân tố — vì sao thay từng biến một dễ bỏ sót tương tác

Giả sử hiệu suất phụ thuộc nhiệt độ \(T\) và lượng chất xúc tác \(C\).

Nếu tác động của nhiệt độ khác nhau khi lượng xúc tác thấp so với khi cao, hai yếu tố có **tương tác (interaction)**.

Thiết kế nhân tố 2×2 có thể ước lượng hiệu ứng chính của \(T\), hiệu ứng chính của \(C\) và tương tác \(T\times C\).

Cách thay từng yếu tố một (**one-factor-at-a-time**) dễ bỏ sót tương tác vì chỉ khảo sát các lát cắt rời của không gian điều kiện.

Trong tối ưu quy trình hóa học, tương tác rất phổ biến vì nhiệt độ đồng thời ảnh hưởng độ tan, hoạt tính xúc tác, phản ứng phụ và truyền khối.

## Phương pháp bề mặt đáp ứng

Sau khi sàng lọc xác định yếu tố quan trọng, **phương pháp bề mặt đáp ứng (Response Surface Methodology, RSM)** khảo sát độ cong và tìm vùng tối ưu.

Một mô hình bậc hai cục bộ có thể là:

\[
y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_{12}x_1x_2+\beta_{11}x_1^2+\beta_{22}x_2^2+\epsilon
\]

Đây là xấp xỉ thực nghiệm trong vùng đã khảo sát, không phải định luật hóa học. Điểm tối ưu dự đoán cần được kiểm chứng bằng thí nghiệm độc lập.

## Thiết kế thí nghiệm động học

Hệ đo phải có đáp ứng nhanh hơn hiện tượng cần quan sát.

Nếu phản ứng hoàn thành trong 2 giây nhưng quá trình trộn mất 5 giây, “tốc độ” đo được chủ yếu phản ánh thiết bị chứ không phản ánh động học nội tại.

Các yếu tố cần xét gồm thời gian chết của trộn, cân bằng nhiệt, độ phân giải thời gian của đầu dò, ảnh hưởng của việc lấy mẫu, thời gian dừng phản ứng và khả năng phản ứng nghịch hoặc ức chế bởi sản phẩm.

Phương pháp tốc độ ban đầu giảm ảnh hưởng thay đổi thành phần nhưng đòi hỏi dữ liệu thời gian đầu đáng tin cậy.

Fit định luật tốc độ tích phân dùng toàn bộ đường thời gian nhưng phụ thuộc mạnh hơn vào tính đúng của mô hình động học.

## Kiểm soát nhiệt độ

Tốc độ phản ứng thường thay đổi theo hàm mũ với nhiệt độ theo hành vi Arrhenius. Một sai khác nhiệt độ nhỏ không được nhận biết có thể bị nhầm thành hiệu ứng của xúc tác hoặc nhóm thế.

Cần ghi nhiệt độ thật của phản ứng chứ không chỉ nhiệt độ đặt của bể.

Với phản ứng tỏa nhiệt, nhiệt độ bên trong mẫu có thể khác môi trường do giới hạn truyền nhiệt.

## Trộn và truyền khối như yếu tố gây nhiễu

Tốc độ quan sát được có thể bị giới hạn bởi khuếch tán hoặc truyền khối thay vì động học hóa học nội tại.

Điều này đặc biệt quan trọng với xúc tác dị thể, phản ứng khí–lỏng, phản ứng bị kiểm soát bởi hòa tan và hệ điện hóa.

Thay tốc độ khuấy là một phép chẩn đoán hữu ích. Nếu tốc độ quan sát thay đổi mạnh theo mức trộn, hệ có thể chưa nằm trong vùng kiểm soát thuần bởi phản ứng hóa học.

## Kế hoạch lấy mẫu

Bản thân việc lấy mẫu có thể làm thí nghiệm thay đổi.

Rút thể tích làm lượng vật chất thay đổi; mở bình làm trao đổi khí; quá trình dừng phản ứng có thể không hoàn toàn; syringe hoặc filter có thể hấp phụ chất phân tích.

Thể tích lấy, cách dừng phản ứng và điều kiện lưu mẫu nên được định trước trước khi bắt đầu.

## Công suất thống kê và cỡ mẫu

**Công suất thống kê (statistical power)** là xác suất phát hiện một hiệu ứng thật có kích thước đã xác định dưới các giả định của mô hình.

Power tăng khi hiệu ứng thật lớn hơn, phương sai nhỏ hơn, số lặp độc lập lớn hơn hoặc nhiễu/yếu tố gây nhiễu được kiểm soát tốt hơn.

Chọn cỡ mẫu sau khi đã nhìn kết quả dễ tạo thiên lệch. Khi có thể, nên xác định trước kích thước hiệu ứng có ý nghĩa và phương sai dự kiến.

## Định trước cách phân tích

Các quyết định như endpoint chính, tiêu chí loại dữ liệu, phép biến đổi, mô hình và cách xử lý ngoại lệ nên được định nghĩa trước khi nhìn sự khác biệt giữa nhóm.

Phân tích khám phá vẫn rất có giá trị, nhưng cần được ghi rõ là khám phá thay vì trình bày như kiểm định đã định trước.

## Thẩm định và độ bền phương pháp

Sau khi tối ưu, cần kiểm tra xem những thay đổi nhỏ nhưng thực tế có làm kết quả đổi đáng kể không.

Ví dụ có thể thay pH một lượng nhỏ, lưu lượng vài phần trăm, nồng độ thuốc thử, ngày đo, người thao tác hoặc thiết bị.

**Độ bền (robustness)** hỏi độ nhạy với những thay đổi nhỏ có chủ ý. **Độ bền giữa điều kiện vận hành (ruggedness / intermediate precision)** xét biến thiên giữa ngày, người và thiết bị.

Một phương pháp chỉ hoạt động tại đúng một thiết lập rất hẹp thường khó chuyển giao.

## Tài liệu hóa và nguồn gốc dữ liệu

Khả năng tái lập cần nhiều hơn con số cuối.

Cần lưu danh tính, cấp và lô thuốc thử; nồng độ thật; ngày chuẩn bị; mã mẫu; thiết bị và cài đặt; file hiệu chuẩn; điều kiện môi trường; sai lệch quy trình; dữ liệu thô; script và phiên bản phần mềm.

Theo ngôn ngữ phần mềm, thí nghiệm cần đủ metadata để tái tạo “trạng thái hệ thống” của lần đo.

## Toàn vẹn dữ liệu

Không nên ghi đè dữ liệu thô bằng dữ liệu đã xử lý. Phép biến đổi nên được lưu riêng và có khả năng truy vết.

Với workflow phức tạp, script có quản lý phiên bản thường tái lập tốt hơn spreadsheet chỉnh tay vì mọi phép tính được biểu diễn rõ.

Dấu vết kiểm toán đặc biệt quan trọng khi dữ liệu hỗ trợ quyết định có kiểm soát hoặc tác động cao.

## Ví dụ so sánh hai chất xúc tác

Một thiết kế yếu:

```text
chạy A ba lần vào thứ Hai
chạy B ba lần vào thứ Ba
so sánh trung bình
```

Ngày đo và chất xúc tác bị gây nhiễu hoàn toàn.

Một thiết kế mạnh hơn:

```text
chuẩn bị các bình phản ứng độc lập
ngẫu nhiên hóa thứ tự A/B trên cả hai ngày
chặn theo ngày trong phân tích
sử dụng cùng hệ nội chuẩn
có mẫu trắng và xúc tác tham chiếu
đo conversion và selectivity tại cùng thời điểm
```

Khi đó số giải thích thay thế bị thu hẹp đáng kể.

## Những hiểu lầm thường gặp

### “Tăng số lần lặp sửa được sai lệch hệ thống”

Không. Lặp nhiều lần một phương pháp bị lệch chỉ giúp ước lượng giá trị sai với độ chụm cao hơn.

### “Ba lần đo kỹ thuật nghĩa là n=3 thí nghiệm độc lập”

Không nếu cả ba cùng xuất phát từ một đơn vị thí nghiệm.

### “R² cao chứng minh đường hiệu chuẩn hợp lệ”

Không. Phần dư, dải đo, chuẩn và mẫu QC độc lập đều quan trọng.

### “Ngẫu nhiên hóa loại bỏ mọi yếu tố gây nhiễu”

Không. Nó làm giảm liên kết hệ thống; yếu tố phi mục tiêu lớn đã biết vẫn nên được chặn hoặc kiểm soát.

### “Điểm tối ưu do mô hình dự đoán chắc chắn là tối ưu thật”

Không. Dự đoán phải được xác nhận bằng thí nghiệm.

## Mô hình tư duy

Thiết kế thí nghiệm là **kiến trúc nhân quả bao quanh một phép đo**. Mỗi biến không được kiểm soát là một lời giải thích thay thế; mỗi đối chứng, ngẫu nhiên hóa hoặc block loại bớt một phần mơ hồ; mỗi loại lặp lại ước lượng một tầng biến thiên khác nhau.

Xem tiếp: [Sai số, độ không đảm bảo và phân tích dữ liệu](./05_error_uncertainty_and_data_analysis.md).