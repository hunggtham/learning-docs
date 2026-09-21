# Đo lường và lấy mẫu — từ câu hỏi hóa học tới bằng chứng đáng tin cậy

> **Hóa phân tích (analytical chemistry / 분석화학)** không chỉ trả lời “trong mẫu có gì?” và “có bao nhiêu?”. Nhiệm vụ sâu hơn là xây dựng một chuỗi suy luận có thể kiểm tra được từ vật thể thật ngoài thế giới → mẫu đại diện → mẫu phòng thí nghiệm → tín hiệu thiết bị → mô hình hiệu chuẩn → kết quả cùng độ không đảm bảo.

Một thiết bị cực kỳ chính xác không thể cứu một mẫu lấy sai. Một đường hiệu chuẩn đẹp không thể sửa việc chất phân tích đã bị mất trong bước phá mẫu. Hóa phân tích vì thế là **khoa học về chất lượng của bằng chứng đo lường**.

# Bắt đầu từ câu hỏi, không bắt đầu từ thiết bị

Trước khi chọn HPLC, ICP-MS hay chuẩn độ, phải xác định rõ câu hỏi.

Ví dụ “đo chì trong nước” vẫn chưa đủ. Cần hỏi:

- chì tổng hay chì hòa tan?
- mẫu tại vòi, trong đường ống hay trong nguồn nước?
- giá trị tức thời hay trung bình theo thời gian?
- cần so với tiêu chuẩn pháp lý hay nghiên cứu cơ chế?
- mức nồng độ dự kiến là µg/L hay mg/L?

Những lựa chọn này quyết định cách lấy mẫu, bảo quản, phá mẫu và giới hạn phát hiện cần thiết.

## Đại lượng cần đo

**Đại lượng cần đo (measurand)** là đại lượng được định nghĩa cụ thể mà phép đo muốn xác định.

Một định nghĩa tốt phải chỉ rõ:

- chất hoặc dạng hóa học;
- nền mẫu;
- điều kiện hoặc quy ước thao tác;
- đơn vị;
- đôi khi cả thời gian/vị trí.

Ví dụ “sắt hòa tan” trong môi trường thường được định nghĩa thao tác bằng phần đi qua một kích thước màng lọc nhất định. Đây không nhất thiết đồng nghĩa với “mọi nguyên tử Fe tồn tại dưới dạng ion đơn lẻ”.

# Chuỗi phân tích

Một quy trình phân tích có thể được nhìn như:

```text
quần thể / hệ thật
→ kế hoạch lấy mẫu
→ mẫu sơ cấp
→ giảm và đồng nhất mẫu
→ chuẩn bị mẫu
→ phép đo
→ hiệu chuẩn
→ xử lý dữ liệu
→ độ không đảm bảo
→ kết luận
```

Mỗi bước có thể làm thay đổi chất phân tích hoặc thêm độ không đảm bảo.

Một nguyên tắc quan trọng là **độ tin cậy cuối cùng bị giới hạn bởi mắt xích yếu nhất**.

# Lấy mẫu — sai số thường lớn hơn người mới học tưởng

Thiết bị có thể đo lặp với RSD 0,5%, nhưng nếu vật liệu không đồng nhất và mẫu lấy không đại diện, sai số lấy mẫu có thể hàng chục phần trăm.

Đất, quặng, thực phẩm, bột dược phẩm, dòng nước thải và nguyên liệu công nghiệp đều có thể biến thiên mạnh theo không gian hoặc thời gian.

## Quần thể và mẫu

**Quần thể (population)** là toàn bộ hệ mà ta muốn suy luận.

**Mẫu (sample)** là phần vật chất hữu hạn được lấy ra để đại diện cho quần thể đó.

Kết quả phân tích đúng trên mẫu nhưng mẫu không đại diện vẫn không trả lời đúng câu hỏi ban đầu.

# Biến thiên không gian và thời gian

Một hồ nước có thể phân tầng theo độ sâu. Một ống khói có nồng độ thay đổi theo tải nhà máy. Một đống quặng có hạt giàu kim loại phân bố không đều.

Vì vậy kế hoạch lấy mẫu phải xét:

- vị trí;
- thời điểm;
- tần suất;
- thể tích/khối lượng mẫu;
- mức độ trộn;
- quy mô hạt.

Không có “một mẫu đại diện” độc lập với câu hỏi và cấu trúc biến thiên của hệ.

# Mẫu ngẫu nhiên, phân tầng và mẫu tổ hợp

## Lấy mẫu ngẫu nhiên

Chọn đơn vị sao cho mỗi phần của quần thể có cơ hội được lấy hợp lý. Cách này giảm thiên lệch do người lấy mẫu chọn điểm thuận tiện.

## Lấy mẫu phân tầng

Nếu biết hệ có các vùng khác nhau — ví dụ độ sâu, khu sản xuất hoặc loại đất — có thể chia thành tầng rồi lấy trong từng tầng.

Điều này thường hiệu quả hơn ngẫu nhiên hoàn toàn khi biến thiên giữa các tầng lớn.

## Mẫu tổ hợp

Nhiều mẫu nhỏ được gộp thành một mẫu chung để ước lượng giá trị trung bình.

Ưu điểm là giảm chi phí phân tích. Nhược điểm là mất thông tin về biến thiên từng điểm và có thể che khuất hotspot.

# Kích thước mẫu và tính không đồng nhất

Nếu chất phân tích nằm trong các hạt hiếm, lấy quá ít vật liệu làm kết quả dao động mạnh.

Giảm kích thước hạt và đồng nhất mẫu có thể giảm sai số do phân bố hạt, nhưng bản thân nghiền/trộn có thể gây:

- nhiễm từ thiết bị;
- mất chất bay hơi;
- oxy hóa;
- hấp phụ nước.

Vì vậy chuẩn bị mẫu luôn là một đánh đổi giữa tính đại diện và nguy cơ làm thay đổi hóa học.

# Giảm mẫu mà không làm mất tính đại diện

Trong mẫu rắn khối lượng lớn, không thể phân tích toàn bộ. Các kỹ thuật chia mẫu như riffle splitting hoặc chia tư nhằm giảm khối lượng mà vẫn giữ phân bố thành phần.

Lấy một thìa từ mặt trên đống bột là cách giảm mẫu rất tệ vì hiện tượng phân tầng kích thước và khối lượng riêng có thể làm thành phần mặt trên khác phần trong.

# Bảo quản mẫu — mẫu tiếp tục “sống” sau khi lấy

Sau lấy mẫu, hóa học có thể tiếp tục thay đổi:

- khí thoát hoặc hòa tan;
- vi sinh vật chuyển hóa;
- kim loại kết tủa hoặc hấp phụ lên thành bình;
- chất hữu cơ bị quang phân;
- trạng thái oxy hóa thay đổi;
- nước bay hơi.

Bảo quản có thể cần làm lạnh, acid hóa, tránh ánh sáng, lọc ngay hoặc kiểm soát headspace tùy chất phân tích.

Bảo quản không phải thao tác hành chính; nó là một phần của mô hình hóa học.

# Chuỗi quản lý mẫu và truy xuất nguồn gốc

Trong phân tích pháp lý, môi trường hoặc công nghiệp, cần biết:

- ai lấy mẫu;
- ở đâu và khi nào;
- bình chứa nào;
- điều kiện bảo quản;
- ai nhận và phân tích;
- mọi lần chuyển giao.

**Chuỗi quản lý mẫu (chain of custody)** giúp đảm bảo kết quả có thể truy về đúng mẫu vật lý ban đầu.

# Chuẩn bị mẫu — biến hệ thật thành dạng đo được

Các bước có thể gồm:

- hòa tan;
- phá mẫu acid;
- nung;
- chiết;
- lọc;
- ly tâm;
- pha loãng;
- cô đặc;
- dẫn xuất hóa;
- làm sạch nền.

Mỗi bước có hai câu hỏi:

1. chất phân tích có được giữ lại định lượng không?
2. nền mẫu có được chuyển thành dạng tương thích với phép đo không?

# Mẫu trắng — tìm tín hiệu không đến từ mẫu

**Mẫu trắng (blank)** có nhiều loại.

### Mẫu trắng thuốc thử

Chứa thuốc thử nhưng không có mẫu, giúp phát hiện nhiễm từ hóa chất.

### Mẫu trắng phương pháp

Đi qua toàn bộ quy trình chuẩn bị, giúp thấy nhiễm từ dụng cụ và thao tác.

### Mẫu trắng hiện trường

Được xử lý tại hiện trường tương tự mẫu thật, giúp phát hiện nhiễm trong lấy và vận chuyển.

Một tín hiệu nền ổn định có thể trừ được; nền biến thiên hoặc gần mức chất phân tích sẽ làm độ không đảm bảo tăng mạnh.

# Thêm chuẩn và thu hồi

Nếu thêm lượng chất phân tích biết trước vào mẫu rồi đưa qua toàn quy trình:

\[
\%Recovery=
\frac{C_{spiked}-C_{original}}{C_{added}}\times100\%
\]

**Thu hồi (recovery)** giúp phát hiện tổn thất hoặc hiệu ứng nền.

Nếu một phương pháp đo lặp rất đẹp nhưng chỉ thu hồi 75%, nó có độ chụm tốt nhưng độ đúng kém.

# Vật liệu chuẩn được chứng nhận

**CRM (certified reference material)** là vật liệu có giá trị tham chiếu cùng độ không đảm bảo được xác lập bằng quy trình đo lường phù hợp.

Phân tích CRM như một mẫu thật giúp kiểm tra toàn bộ chuỗi phương pháp, không chỉ đường hiệu chuẩn của thiết bị.

CRM đặc biệt có giá trị vì nó cung cấp điểm neo độc lập với chuẩn do chính phòng thí nghiệm tự pha.

# Hiệu chuẩn — ánh xạ tín hiệu sang lượng chất

Thiết bị thường cho tín hiệu \(y\), còn ta cần nồng độ hoặc lượng chất \(x\).

Mô hình đơn giản:

\[
y=mx+b
\]

nhưng đường thẳng chỉ hợp lệ trong vùng đã được kiểm chứng.

Hiệu chuẩn tốt cần:

- bao phủ vùng nồng độ mẫu;
- có đủ điểm để phát hiện độ cong;
- dùng chuẩn ổn định;
- kiểm tra phần dư;
- có QC độc lập.

Không nên ngoại suy xa ngoài vùng chuẩn chỉ vì phần mềm vẫn trả ra một con số.

# Hiệu chuẩn ngoài

Trong **hiệu chuẩn ngoài (external calibration)**, chuẩn và mẫu được đo riêng.

Phương pháp đơn giản và hiệu quả khi chuẩn và mẫu có nền tương tự hoặc hiệu ứng nền không đáng kể.

# Chuẩn nội

Một **chuẩn nội (internal standard)** được thêm lượng cố định vào cả chuẩn và mẫu. Tỉ số tín hiệu analyte/chuẩn nội có thể bù các biến thiên như thể tích tiêm, mất mẫu hoặc hiệu suất ion hóa.

Chuẩn nội tốt phải hành xử tương tự chất phân tích nhưng vẫn phân biệt được trong detector.

Trong MS, đồng vị đánh dấu thường là chuẩn nội rất mạnh vì hóa học gần giống analyte.

# Phương pháp thêm chuẩn

Khi nền mẫu làm độ nhạy khác chuẩn trong dung môi sạch, có thể thêm các lượng analyte biết trước trực tiếp vào các aliquot của mẫu.

Sau đó dùng quan hệ tín hiệu–lượng thêm để suy nồng độ ban đầu.

**Thêm chuẩn (standard addition)** giúp bù một số hiệu ứng nền, nhưng tốn công hơn và giả định nền không thay đổi đáng kể giữa các mức thêm.

# Độ nhạy và độ chọn lọc

**Độ nhạy (sensitivity)** thường liên hệ độ dốc tín hiệu theo nồng độ.

**Độ chọn lọc (selectivity)** mô tả khả năng phân biệt chất phân tích trước chất gây nhiễu.

Một detector có thể cực nhạy nhưng vô dụng nếu nhiều chất khác tạo cùng tín hiệu.

Trong thực tế, độ chọn lọc thường được tạo từ nhiều lớp:

```text
chuẩn bị mẫu
+ phép tách
+ hóa học phản ứng
+ detector
+ mô hình dữ liệu
```

# Giới hạn phát hiện và giới hạn định lượng

**LOD (limit of detection)** liên quan khả năng phân biệt tín hiệu của analyte với nền.

**LOQ (limit of quantitation)** yêu cầu kết quả số có độ không đảm bảo đủ nhỏ cho mục đích sử dụng.

Một biểu thức minh họa thường gặp:

\[
LOD\sim\frac{k\sigma_{blank}}{m}
\]

với \(m\) là độ dốc hiệu chuẩn. Nhưng lựa chọn \(k\), cách ước lượng nhiễu và ma trận mẫu phải được thẩm định.

LOD không phải “chữ số nhỏ nhất máy hiển thị”.

# Khoảng làm việc và tính tuyến tính

**Khoảng làm việc (working range)** là vùng mà phương pháp đạt các tiêu chí hiệu năng yêu cầu.

Ở nồng độ thấp, nhiễu nền chi phối. Ở nồng độ cao, detector có thể bão hòa hoặc phản ứng hóa học không còn tuyến tính.

Một phương pháp vì vậy có thể có vùng rất rộng nhưng chỉ một phần là tuyến tính.

# Validation — chứng minh phương pháp phù hợp mục đích

**Thẩm định phương pháp (method validation)** không hỏi “phương pháp có tốt không?” một cách chung chung. Nó hỏi “phương pháp có đủ tốt cho mục đích cụ thể này không?”.

Các đặc tính thường cần đánh giá:

- độ đúng;
- độ chụm;
- độ chọn lọc;
- LOD/LOQ;
- khoảng làm việc;
- tuyến tính hoặc mô hình đáp ứng;
- độ bền vững trước thay đổi nhỏ (robustness);
- độ không đảm bảo.

Tiêu chí chấp nhận phải liên hệ quyết định thực tế. Đo tạp chất dược phẩm ở ppm cần yêu cầu khác đo thành phần chính ở %.

# Độ chụm có nhiều tầng

### Độ lặp lại (repeatability)

Cùng người, cùng thiết bị, điều kiện gần nhau, thời gian ngắn.

### Độ chụm trung gian (intermediate precision)

Thay đổi ngày, người phân tích hoặc thiết bị trong cùng phòng thí nghiệm.

### Độ tái lập (reproducibility)

So sánh giữa phòng thí nghiệm.

Một phương pháp có repeatability rất tốt vẫn có thể tái lập kém nếu phụ thuộc thao tác tinh tế không được chuẩn hóa.

# QA và QC

**Bảo đảm chất lượng (quality assurance, QA)** là hệ thống thiết kế để quá trình có khả năng tạo dữ liệu đáng tin.

**Kiểm soát chất lượng (quality control, QC)** là các phép kiểm trong quá trình để phát hiện khi hệ đang lệch.

QC có thể gồm:

- blank;
- mẫu lặp;
- mẫu thêm chuẩn;
- CRM;
- chuẩn kiểm tra độc lập;
- biểu đồ kiểm soát;
- kiểm tra lại hiệu chuẩn.

QA/QC không phải thủ tục giấy tờ tách khỏi hóa học; nó là cách kiểm tra giả định của mô hình đo.

# Biểu đồ kiểm soát và drift

Đo cùng một mẫu QC theo thời gian có thể phát hiện:

- drift từ từ;
- thay đổi bậc sau bảo trì;
- tăng độ phân tán;
- sai lệch theo lô thuốc thử.

Một phép hiệu chuẩn có thể “pass” hôm nay nhưng hệ đã trôi so với nhiều tuần trước. Dữ liệu theo thời gian giúp thấy điều đó.

# Độ không đảm bảo — ghép toàn bộ chuỗi

Kết quả cuối không chỉ mang độ không đảm bảo của detector. Nó có thể nhận đóng góp từ:

- lấy mẫu;
- cân/thể tích;
- độ tinh khiết chuẩn;
- thu hồi;
- đường hiệu chuẩn;
- độ lặp lại;
- hiệu ứng nền;
- bảo quản.

Nếu lấy mẫu chi phối 15% nhưng instrument chỉ 1%, tối ưu detector từ 1% xuống 0,2% gần như không thay đổi chất lượng kết luận.

Đây là lý do cần xây **ngân sách độ không đảm bảo** thay vì chỉ nhìn specification của máy.

# Thiết kế phương pháp theo “fitness for purpose”

Một phương pháp không cần tối đa mọi chỉ số.

Nếu quyết định chỉ cần biết “nồng độ có vượt 100 mg/L hay không?”, một phương pháp nhanh với độ không đảm bảo 2 mg/L có thể hoàn toàn đủ.

Ngược lại, nếu cần phân biệt 99,8 và 100,2 mg/L, yêu cầu hoàn toàn khác.

Chất lượng phân tích luôn phải gắn với quyết định mà dữ liệu hỗ trợ.

# Những hiểu lầm thường gặp

### “Máy càng đắt thì kết quả càng đúng”

Không. Lấy mẫu, chuẩn bị mẫu và hiệu chuẩn có thể chi phối sai số.

### “Đo lặp nhiều lần sẽ giải quyết mẫu không đại diện”

Không. Lặp cùng mẫu chỉ đo cùng một phần quần thể chính xác hơn.

### “LOD càng thấp thì phương pháp càng tốt”

Không nhất thiết. Nếu độ chọn lọc kém hoặc độ đúng không đạt, LOD thấp không cứu được phương pháp.

### “Hiệu chuẩn tuyến tính có \(R^2\) cao nghĩa là hợp lệ”

Không. Cần xem phần dư, khoảng nồng độ và QC độc lập.

### “QC là thủ tục quản lý, không phải khoa học”

QC chính là phép thử thực nghiệm cho giả định rằng quy trình vẫn đang hoạt động như mô hình.

# Mô hình tư duy

Hãy xem một kết quả phân tích như **một chuỗi suy luận từ thế giới thật tới một con số**. Muốn con số đáng tin, từng mắt xích phải trả lời được câu hỏi: mẫu có đại diện không, chất phân tích có được bảo toàn không, tín hiệu có chọn lọc không, hiệu chuẩn có đúng vùng không, và độ không đảm bảo cuối cùng có phù hợp với quyết định cần đưa ra không.

Xem tiếp: [Phân tích thể tích](./01_volumetric_analysis.md) và [Sai số, độ không đảm bảo và phân tích dữ liệu](../17_laboratory/05_error_uncertainty_and_data_analysis.md).