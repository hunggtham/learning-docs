# Tốc độ phản ứng — đo sự thay đổi hóa học theo thời gian

> **Động học hóa học (chemical kinetics / 화학 반응 속도론)** nghiên cứu phản ứng xảy ra nhanh đến mức nào, tốc độ phụ thuộc điều kiện ra sao và những bước vi mô nào tạo nên tốc độ quan sát được. Nhiệt động lực học cho biết một biến đổi có thuận lợi hay không; động học cho biết hệ có thể đi tới trạng thái đó trong microsecond, vài giờ hay hàng triệu năm.

Một phản ứng có thể rất thuận lợi về năng lượng tự do nhưng vẫn gần như không xảy ra ở nhiệt độ phòng nếu con đường phản ứng có hàng rào lớn. Vì vậy muốn hiểu một quá trình hóa học thực tế phải luôn tách hai câu hỏi:

```text
Nhiệt động lực học: hệ muốn đi về đâu?
Động học: hệ đi tới đó nhanh đến mức nào và bằng con đường nào?
```

## Tốc độ là mức thay đổi theo thời gian

Xét phản ứng tổng quát:

\[
aA+bB\rightarrow cC+dD
\]

Khi phản ứng diễn ra, nồng độ chất phản ứng giảm còn nồng độ sản phẩm tăng. Nếu chỉ viết \(-d[A]/dt\), con số thu được phụ thuộc hệ số hóa lượng của A. Để mọi chất cho cùng một giá trị tốc độ phản ứng, ta chuẩn hóa theo hệ số:

\[
r=-\frac{1}{a}\frac{d[A]}{dt}
=-\frac{1}{b}\frac{d[B]}{dt}
=\frac{1}{c}\frac{d[C]}{dt}
=\frac{1}{d}\frac{d[D]}{dt}
\]

Dấu âm xuất hiện cho chất phản ứng vì nồng độ giảm theo thời gian. Đây là ví dụ quan trọng cho việc **hóa lượng và động học không tách rời nhau**: phương trình hóa học cho biết các tốc độ thay đổi nồng độ phải liên hệ với nhau theo tỉ lệ nào.

## Tốc độ trung bình và tốc độ tức thời

Trong một khoảng hữu hạn:

\[
r_{avg}=-\frac{1}{a}\frac{\Delta[A]}{\Delta t}
\]

được gọi là **tốc độ trung bình (average rate)**.

Nhưng tốc độ thường thay đổi liên tục. Giá trị tại một thời điểm là giới hạn khi khoảng thời gian tiến tới 0:

\[
r=-\frac{1}{a}\frac{d[A]}{dt}
\]

Về hình học, đó là độ dốc tiếp tuyến của đường nồng độ–thời gian. Vì vậy đạo hàm không phải công cụ toán học được gắn thêm vào động học; nó chính là ngôn ngữ tự nhiên để mô tả “tốc độ thay đổi ngay lúc này”.

## Vì sao phản ứng thường chậm dần?

Nếu tốc độ phụ thuộc nồng độ chất phản ứng, khi phản ứng tiêu thụ chúng thì xác suất tạo các cấu hình phản ứng phù hợp giảm. Do đó nhiều đường nồng độ–thời gian có độ dốc lớn lúc đầu rồi nhỏ dần.

Nhưng đây không phải quy luật bắt buộc. Hệ có thể tăng tốc nếu sản phẩm xúc tác chính phản ứng, tạo **tự xúc tác (autocatalysis)**. Các mạng phản ứng còn có thể có giai đoạn cảm ứng, dao động, nhiều đỉnh tốc độ hoặc chuyển cơ chế theo thời gian.

Do đó hình dạng đường nồng độ–thời gian chính là dữ liệu về cơ chế chứ không chỉ là một đường để tính độ dốc.

## Tốc độ phản ứng không nhất thiết là tốc độ phản ứng nội tại

Trong hệ thật, tốc độ quan sát có thể bị giới hạn bởi một quá trình vật lý khác trước khi hóa học kịp chi phối.

Ví dụ một phản ứng trên bề mặt chất rắn có thể gồm:

```text
khuếch tán chất phản ứng tới bề mặt
→ hấp phụ
→ phản ứng hóa học bề mặt
→ giải hấp sản phẩm
→ khuếch tán sản phẩm ra môi trường
```

Nếu khuếch tán chậm nhất, tăng hoạt tính hóa học của xúc tác có thể không làm tốc độ tổng tăng đáng kể. Tương tự, trong phản ứng khí–lỏng, tốc độ khuấy có thể ảnh hưởng tốc độ quan sát vì nó thay đổi truyền khối.

Khi nghiên cứu động học, phải hỏi: **ta đang đo động học hóa học thật hay đang đo giới hạn vận chuyển?**

## Các yếu tố làm tốc độ thay đổi

Nồng độ hoặc hoạt độ ảnh hưởng số cấu hình phản ứng khả dụng. Với khí, áp suất riêng phần đóng vai trò tương tự nồng độ trong nhiều mô hình.

Nhiệt độ thay đổi phân bố năng lượng và vì thế làm hằng số tốc độ thay đổi mạnh. Đây là nền cho phương trình Arrhenius.

Dung môi có thể ổn định chất phản ứng, trạng thái chuyển tiếp hoặc ion trung gian ở mức khác nhau; vì thế cùng một phản ứng có thể nhanh chậm rất khác trong hai dung môi.

Diện tích bề mặt quyết định số vị trí tiếp xúc trong phản ứng dị thể. Bột thường phản ứng nhanh hơn khối rắn cùng khối lượng vì diện tích tiếp xúc lớn hơn.

Ánh sáng có thể tạo trạng thái kích thích hoặc gốc tự do, mở ra con đường phản ứng không tồn tại trong trạng thái cơ bản.

Chất xúc tác thay đổi cơ chế và hàng rào hoạt hóa nhưng không thay đổi hằng số cân bằng của phản ứng ròng.

## Thuyết va chạm — mô hình trực giác đầu tiên

Trong pha khí loãng, một trực giác ban đầu là các phân tử phải gặp nhau để phản ứng. Nhưng không phải va chạm nào cũng thành công.

Có thể hình dung:

```text
tốc độ phản ứng
≈ tần suất gặp nhau
× xác suất có đủ năng lượng
× xác suất có định hướng/cấu hình phù hợp
```

Mô hình này giải thích được vì sao tăng nồng độ thường tăng số lần gặp và vì sao nhiệt độ tăng có thể tăng mạnh phần va chạm đủ năng lượng.

Tuy nhiên nó không đủ để mô tả đầy đủ dung dịch, phản ứng qua phức chất, động học enzyme, bề mặt rắn hoặc xuyên hầm lượng tử. Cần xem nó là một mô hình nhập môn chứ không phải hình ảnh cuối cùng của trạng thái chuyển tiếp.

## Làm thế nào đo tốc độ nếu không nhìn thấy phân tử?

Thiết bị thường không đo “tốc độ phản ứng” trực tiếp. Ta đo một **tín hiệu quan sát được (observable)** có quan hệ với thành phần rồi lấy dữ liệu theo thời gian.

Ví dụ, nếu một chất hấp thụ ánh sáng theo Beer–Lambert:

\[
A=\varepsilon bc
\]

thì absorbance theo thời gian có thể chuyển thành nồng độ theo thời gian.

Các cách khác gồm đo:

- áp suất hoặc thể tích khí;
- pH;
- độ dẫn điện;
- khối lượng;
- tín hiệu quang phổ;
- diện tích peak sắc ký;
- điện thế hoặc dòng điện;
- tín hiệu huỳnh quang.

Mỗi phép đo có **độ phân giải thời gian (time resolution)**. Nếu phản ứng xảy ra trong 1 ms nhưng thiết bị chỉ ghi mỗi 1 s, phần quan trọng nhất của động học đã bị mất.

## Phép đo phải nhanh hơn quá trình muốn nghiên cứu

Nếu thời gian trộn dung dịch là 5 s còn phản ứng hoàn tất trong 1 s, dữ liệu thu được chủ yếu phản ánh quá trình trộn chứ không phải động học nội tại.

Đối với phản ứng cực nhanh có thể cần:

- stopped-flow;
- temperature-jump;
- laser flash photolysis;
- pump–probe spectroscopy.

Nguyên tắc chung là **thời gian đáp ứng của phép đo phải nhỏ hơn đáng kể thang thời gian của hiện tượng cần suy ra**.

## Tốc độ ban đầu

**Tốc độ ban đầu (initial rate)** được lấy gần \(t=0\), khi nồng độ chưa thay đổi nhiều và sản phẩm còn rất ít.

Điều này có hai lợi ích. Thứ nhất, các nồng độ ban đầu dễ biết chính xác. Thứ hai, ảnh hưởng của phản ứng nghịch, ức chế bởi sản phẩm hoặc phản ứng phụ thường nhỏ hơn ở giai đoạn đầu.

Bằng cách lặp thí nghiệm với các nồng độ ban đầu khác nhau, ta có thể suy ra bậc phản ứng trong phương trình tốc độ.

## Từ dữ liệu rời rạc tới đạo hàm — nhiễu là vấn đề thật

Nếu dữ liệu nồng độ được đo tại các thời điểm rời rạc, tính đạo hàm bằng hiệu hữu hạn:

\[
\frac{dC}{dt}\approx\frac{C(t+\Delta t)-C(t)}{\Delta t}
\]

có thể làm nhiễu tăng mạnh, đặc biệt khi \(\Delta t\) nhỏ. Vì vậy trong thực nghiệm hiện đại thường tốt hơn khi **fit một mô hình động học trực tiếp vào toàn bộ dữ liệu** thay vì lấy đạo hàm từng cặp điểm nhiễu.

Đây là điểm nối giữa động học, thống kê và phân tích dữ liệu.

## Mức tiến triển phản ứng và tốc độ tiến triển

Trong [hóa lượng](../04_chemical_quantities/06_stoichiometric_matrices_and_reaction_networks.md), mức tiến triển \(\xi\) mô tả phản ứng đã tiến xa bao nhiêu. Tốc độ phản ứng có thể hiểu như tốc độ biến đổi của mức tiến triển trên thể tích:

\[
r=\frac{1}{V}\frac{d\xi}{dt}
\]

với hệ đồng nhất có thể tích phù hợp. Cách nhìn này làm rõ rằng các đạo hàm nồng độ của từng chất chỉ là những hình chiếu khác nhau của cùng một tiến trình hóa lượng.

## Hệ kín, hệ dòng liên tục và trạng thái ổn định

Trong bình kín, nồng độ thay đổi theo thời gian vì phản ứng tiêu thụ và tạo chất.

Trong reactor dòng liên tục, một chất có thể liên tục đi vào và ra. Khi tốc độ vào, ra và phản ứng cân bằng nhau, nồng độ có thể không đổi theo thời gian dù phản ứng vẫn diễn ra liên tục. Đây là **trạng thái ổn định (steady state)**, không phải cân bằng nhiệt động.

Sự phân biệt này rất quan trọng trong kỹ thuật hóa học, sinh học tế bào và hóa học khí quyển.

## Động học và định luật bảo toàn

Một mô hình tốc độ không được phép vi phạm bảo toàn nguyên tố hay điện tích. Với mạng phản ứng:

\[
\frac{d\mathbf n}{dt}=S\mathbf r
\]

ma trận hóa lượng \(S\) chuyển vector tốc độ các phản ứng cơ bản thành tốc độ thay đổi số mol của các loài.

Điều này cho thấy động học phức tạp có thể được tổ chức bằng đại số tuyến tính thay vì viết riêng từng phương trình một cách rời rạc.

## Nhiệt động lực học giới hạn động học như thế nào?

Nhiệt động lực học không cho trực tiếp hằng số tốc độ, nhưng phản ứng thuận và nghịch không hoàn toàn độc lập. Ở cân bằng:

\[
k_{forward}[...] = k_{reverse}[...]
\]

và trong các hệ cơ bản phù hợp, tỉ số hằng số tốc độ liên hệ với hằng số cân bằng.

Vì thế một cơ chế động học hợp lý phải tương thích với nhiệt động lực học; không thể chọn tùy ý các hằng số thuận/nghịch nếu chúng dẫn tới một cân bằng sai.

## Ví dụ đời sống: vì sao thực phẩm để lạnh lâu hỏng hơn?

Nhiều phản ứng phân hủy và quá trình enzyme chậm đi khi nhiệt độ giảm vì hằng số tốc độ giảm. Vi sinh vật cũng có tốc độ sinh trưởng và chuyển hóa phụ thuộc nhiệt độ.

Tủ lạnh không làm thực phẩm “ngừng hóa học”. Nó đưa nhiều quá trình sang thang thời gian dài hơn. Đây là một ứng dụng trực tiếp của kinetics vào đời sống.

## Ví dụ vật liệu và pin

Pin có thể có năng lượng nhiệt động lớn nhưng công suất bị giới hạn bởi động học chuyển electron, khuếch tán ion trong điện ly và khuếch tán trong vật liệu điện cực.

Khi sạc quá nhanh, dòng yêu cầu có thể vượt tốc độ vận chuyển ion mong muốn, làm tăng phân cực và kích hoạt phản ứng phụ. Vì vậy **năng lượng** và **công suất** là hai vấn đề khác nhau: một phần của khác biệt đó chính là động học.

## Những hiểu lầm thường gặp

### “Phản ứng tỏa nhiệt mạnh chắc chắn xảy ra nhanh”

Không. \(\Delta H\) hoặc \(\Delta G\) mô tả chênh lệch trạng thái; tốc độ phụ thuộc con đường và hàng rào.

### “Tăng nồng độ luôn làm tốc độ tăng”

Không. Nếu một thành phần không xuất hiện trong phương trình tốc độ hiệu dụng, hoặc bề mặt/enzyme đã bão hòa, tốc độ có thể gần như không đổi.

### “Tốc độ phản ứng là lượng sản phẩm tạo ra”

Không. Tốc độ là **mức thay đổi trên đơn vị thời gian**, thường còn phải chuẩn hóa theo thể tích và hệ số hóa lượng.

### “Đường nồng độ phẳng nghĩa phản ứng đã đạt cân bằng”

Không nhất thiết. Hệ mở có thể ở trạng thái ổn định với dòng phản ứng khác 0.

### “Đo nhiều điểm hơn luôn cho kinetics tốt hơn”

Không nếu phép đo chậm, làm nhiễu hệ hoặc các điểm đều nằm ngoài vùng thời gian chứa thông tin về cơ chế.

## Mô hình tư duy

Hãy xem động học như một bài toán ba tầng:

```text
1. quan sát: nồng độ/tín hiệu thay đổi theo thời gian như thế nào?
2. mô hình: tốc độ hiện tại phụ thuộc trạng thái hiện tại ra sao?
3. cơ chế: những bước vi mô nào có thể tạo ra mô hình tốc độ đó?
```

Nhiệt động lực học cho “địa hình”; động học cho biết hệ di chuyển trên địa hình đó bằng con đường nào và nhanh đến mức nào.

Xem tiếp: [Phương trình tốc độ](./01_rate_laws.md).