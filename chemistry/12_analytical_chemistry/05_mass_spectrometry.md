# Phổ khối — đo tỉ số khối lượng trên điện tích của ion

> **Phổ khối (mass spectrometry, MS / 질량분석법)** chuyển nguyên tử hoặc phân tử thành ion trong pha khí, tách hoặc đo các ion theo **tỉ số khối lượng trên điện tích \(m/z\)** rồi phát hiện chúng. Phổ thu được có thể cung cấp khối lượng phân tử, mẫu đồng vị, công thức nguyên tố, mảnh cấu trúc và lượng tương đối.

MS thường được ví như “cân ở thang phân tử”, nhưng phép ví này chưa đủ. Máy phổ khối không cân trực tiếp phân tử trung hòa; nó điều khiển **chuyển động của hạt mang điện** trong điện trường hoặc từ trường rồi suy `m/z` từ chuyển động đó.

Các prerequisite hữu ích gồm [bức xạ và lượng tử hóa](../01_atomic_structure/01_electromagnetic_radiation_and_quantization.md), [đồng vị](../01_atomic_structure/00_atoms_elements_and_isotopes.md), [cơ chế phản ứng hữu cơ](../11_organic_chemistry/03_organic_reaction_mechanisms.md) và [sắc ký](./04_chromatography.md).

## Vì sao phải tạo ion?

Lực điện tác dụng lên hạt:

\[
F=qE
\]

và lực Lorentz trong từ trường:

\[
F=q\mathbf{v}\times\mathbf{B}
\]

Phân tử trung hòa có tổng điện tích `q = 0`, nên không thể được điều khiển bằng điện trường hoặc từ trường theo cách hữu ích như ion.

Do đó mọi phép MS đều bắt đầu bằng ion hóa.

Hệ quả quan trọng là: **phổ quan sát được không chỉ phụ thuộc phân tử ban đầu mà còn phụ thuộc cách ion được tạo**.

## Kiến trúc chung của thiết bị

Một máy phổ khối có thể được xem như chuỗi mô-đun:

```text
đưa mẫu vào
→ nguồn ion
→ bộ phân tích khối
→ bộ phát hiện
→ xử lý dữ liệu
```

Nguồn ion quyết định những ion nào được tạo. Bộ phân tích quyết định cách phân biệt `m/z`. Bộ phát hiện biến số ion tới thành tín hiệu điện. Phần mềm hiệu chuẩn và dựng phổ.

Nếu một mô-đun tạo thiên lệch, mô-đun phía sau không thể tự động “sửa” hoàn toàn thiên lệch đó.

## Ion hóa — chọn mức phân mảnh phù hợp

### Ion hóa electron

**Ion hóa electron (electron ionization, EI)** cho phân tử pha khí tiếp xúc với electron năng lượng cao, thường gần 70 eV:

\[
M+e^-\rightarrow M^{+\bullet}+2e^-
\]

Ion gốc phân tử thường có nội năng cao và phân mảnh mạnh.

EI thường được gọi là **ion hóa cứng (hard ionization)**. Việc phân mảnh mạnh không chỉ là nhược điểm; các mẫu mảnh tái lập tốt giúp so với thư viện phổ nên EI rất mạnh trong GC–MS của hợp chất hữu cơ bay hơi.

Đỉnh ion phân tử yếu hoặc vắng mặt không có nghĩa phân tử ban đầu “không tồn tại”; nó có thể phân mảnh quá nhanh sau ion hóa.

### Ion hóa hóa học

**Ion hóa hóa học (chemical ionization, CI)** ion hóa khí thuốc thử trước rồi truyền proton hoặc điện tích cho chất phân tích.

Phương pháp thường mềm hơn EI và hay giữ ion gần phân tử, ví dụ:

\[
[M+H]^+
\]

EI và CI vì vậy trả lời hai câu hỏi bổ sung:

```text
EI → phân tử vỡ như thế nào?
CI → khối lượng gần phân tử là bao nhiêu?
```

### Ion hóa phun điện

**Ion hóa phun điện (electrospray ionization, ESI)** bắt đầu từ dung dịch, tạo các giọt mang điện trong điện trường mạnh. Dung môi bay hơi, giọt co lại và cuối cùng tạo ion pha khí.

ESI phù hợp với peptide, protein, chất chuyển hóa và dược chất phân cực.

Đặc điểm nổi bật là **đa điện tích (multiple charging)**. Một protein có thể mang nhiều proton:

\[
\frac{M+zH}{z}
\]

nên phân tử có khối lượng hàng chục kDa vẫn có thể xuất hiện trong vùng `m/z` chỉ vài nghìn.

Chuỗi trạng thái điện tích sau đó được **giải chập (deconvolution)** để suy khối lượng trung hòa.

### MALDI

**Ion hóa giải hấp laser hỗ trợ nền (matrix-assisted laser desorption/ionization, MALDI)** trộn chất phân tích với một nền hấp thụ ánh sáng. Xung laser truyền năng lượng cho nền, hỗ trợ giải hấp và ion hóa chất phân tích.

MALDI thường tạo chủ yếu ion đơn điện tích và ghép thuận lợi với máy thời gian bay. Nó được dùng nhiều cho peptide, polymer và phổ khối tạo ảnh.

### APCI và APPI

**Ion hóa hóa học áp suất khí quyển (APCI)** và **ion hóa quang áp suất khí quyển (APPI)** mở rộng LC–MS tới các hợp chất ít phù hợp với ESI.

Lựa chọn nguồn ion phải dựa trên độ phân cực, độ bay hơi, kích thước phân tử, nhóm chức và mục tiêu phân tích.

## Bộ phân tích khối

### Tứ cực

Bộ phân tích tứ cực dùng bốn thanh điện cực với điện áp RF/DC. Chỉ các ion có `m/z` phù hợp mới có quỹ đạo ổn định đi qua trong một điều kiện điện áp nhất định.

Quét điện áp cho phép lần lượt truyền các dải `m/z` khác nhau.

Tứ cực bền, thực dụng và đặc biệt mạnh trong định lượng mục tiêu, nhất là hệ ba tứ cực.

### Thời gian bay

Trong **time-of-flight (TOF)**, nếu ion nhận gần cùng động năng:

\[
KE=\frac12mv^2=qV
\]

thì:

\[
v=\sqrt{\frac{2qV}{m}}
\]

và với chiều dài đường bay `L`:

\[
t=\frac{L}{v}\propto\sqrt{\frac{m}{q}}
\]

Ion có `m/z` lớn hơn thường tới bộ phát hiện muộn hơn.

Hệ thực dùng quang học ion và **gương ion (reflectron)** để giảm ảnh hưởng của độ phân tán động năng và tăng độ phân giải.

### Bẫy ion

**Bẫy ion (ion trap)** giữ ion trong trường điện RF rồi đẩy các nhóm ion ra theo điều kiện có kiểm soát.

Ưu điểm là có thể thực hiện nhiều cấp phân mảnh `MS^n` trong cùng thiết bị.

### Orbitrap

Orbitrap giữ ion trong trường tĩnh điện. Tần số dao động dọc trục phụ thuộc `m/z`; dòng ảnh được ghi lại rồi biến đổi Fourier để dựng phổ.

Độ phân giải và độ chính xác khối lượng cao làm Orbitrap phổ biến trong proteomics và metabolomics.

### FT-ICR

**Cộng hưởng cyclotron ion biến đổi Fourier (Fourier-transform ion cyclotron resonance, FT-ICR)** đo tần số cyclotron của ion trong từ trường mạnh.

Nó có thể đạt độ phân giải rất cao nhưng đổi lại cần nam châm mạnh, thiết bị phức tạp và chi phí cao.

## Độ phân giải và độ chính xác khối lượng

Độ phân giải thường được định nghĩa:

\[
R=\frac{m}{\Delta m}
\]

trong đó `Δm` phụ thuộc quy ước đo độ rộng đỉnh.

**Độ chính xác khối lượng (mass accuracy)** mô tả độ lệch giữa giá trị đo và giá trị tham chiếu:

\[
error\,(ppm)=\frac{m_{đo}-m_{tham\ chiếu}}{m_{tham\ chiếu}}\times10^6
\]

Hai khái niệm khác nhau:

```text
độ phân giải cao
→ tách được hai tín hiệu rất gần nhau

độ chính xác cao
→ giá trị đo gần giá trị đúng
```

Một hệ có thể rất phân giải nhưng hiệu chuẩn kém, hoặc ngược lại.

## Khối lượng chính xác và công thức nguyên tố

Khối lượng chính xác của đồng vị không phải số nguyên tuyệt đối.

Ví dụ CO và `N2` cùng có khối lượng danh nghĩa 28 nhưng khối lượng chính xác khác nhau đủ để MS độ phân giải cao phân biệt.

Khối lượng chính xác kết hợp mẫu đồng vị có thể giới hạn tập công thức phân tử ứng viên, nhưng hiếm khi tự chứng minh một cấu trúc duy nhất.

## Mẫu đồng vị

Độ phong phú tự nhiên của đồng vị tạo cụm đỉnh đặc trưng.

Với hợp chất chứa carbon, đỉnh `M+1` thường có đóng góp lớn từ `13C`.

Chlorine có tỉ lệ `35Cl/37Cl` gần 3:1, nên phân tử chứa một Cl thường cho cặp `M:M+2` xấp xỉ 3:1.

Bromine có `79Br/81Br` gần 1:1 nên cặp `M/M+2` có cường độ gần bằng nhau.

Nhiều nguyên tử halogen làm mẫu đồng vị mở rộng theo phân bố gần nhị thức.

### Khoảng cách đồng vị tiết lộ trạng thái điện tích

Với ion đơn điện tích, hai đỉnh đồng vị kế nhau cách gần 1 đơn vị `m/z`.

Với `z = 2`, khoảng cách gần 0.5; với `z = 3`, gần 0.333.

Do đó phổ độ phân giải cao có thể suy trạng thái điện tích từ chính khoảng cách đồng vị.

## Phân mảnh — suy cấu trúc từ cách ion bị vỡ

Ion không vỡ hoàn toàn ngẫu nhiên. Con đường phân mảnh phụ thuộc:

- vị trí điện tích;
- độ bền liên kết;
- ổn định cộng hưởng;
- khả năng chuyển vị;
- nội năng của ion.

Phổ EI hữu cơ thường có cắt α gần dị nguyên tử, mảnh benzyl và carbocation được ổn định tốt.

Các nguyên lý này nối trực tiếp với [cơ chế phản ứng hữu cơ](../11_organic_chemistry/03_organic_reaction_mechanisms.md), nhưng pha khí có điều kiện năng lượng và solvat hóa rất khác dung dịch nên không thể áp dụng máy móc mọi cơ chế dung dịch.

## Phổ khối nối tiếp — MS/MS

Một ion tiền chất được chọn, phân mảnh, sau đó các ion sản phẩm được phân tích:

```text
tất cả ion
→ chọn ion tiền chất
→ kích hoạt / va chạm
→ ion sản phẩm
→ phổ MS/MS
```

**Phân ly do va chạm (collision-induced dissociation, CID/HCD)** rất phổ biến. Ion va với khí trơ, chuyển động năng thành nội năng cho tới khi liên kết bị phá.

### Hệ ba tứ cực

Cấu hình điển hình:

```text
Q1 → buồng va chạm q2 → Q3
```

Q1 chọn ion tiền chất, q2 tạo mảnh, Q3 phân tích ion sản phẩm.

Trong **theo dõi phản ứng chọn lọc/nhiều phản ứng (SRM/MRM)**, thiết bị theo dõi các cặp chuyển tiếp tiền chất → mảnh cụ thể. Điều này tạo độ chọn lọc và độ nhạy cao cho định lượng mục tiêu.

## Proteomics — từ phổ mảnh tới trình tự peptide

Peptide được ion hóa bằng ESI rồi phân mảnh. Trong CID/HCD, cắt khung peptide thường tạo các dãy ion như `b` và `y`.

Chênh lệch khối lượng giữa các mảnh liên tiếp có thể tương ứng với **gốc amino acid (amino-acid residue)**.

Nhận diện protein hiện đại thường kết hợp phổ MS/MS với thuật toán tìm kiếm cơ sở dữ liệu thay vì giải toàn bộ phổ thủ công.

Proteomics vì vậy là hệ tích hợp:

```text
hóa học mẫu
+ tách sắc ký
+ ion hóa
+ phổ mảnh
+ thống kê
+ thuật toán cơ sở dữ liệu
```

## Metabolomics và nhận diện phân tử nhỏ

Một khối lượng tiền chất chính xác có thể tương ứng nhiều đồng phân cấu trúc.

Độ tin cậy nhận diện tăng khi ghép:

```text
khối lượng chính xác
+ mẫu đồng vị
+ thời gian lưu
+ phổ MS/MS
+ chất chuẩn thật nếu có
```

Đây là điểm quan trọng về bằng chứng: **khối lượng chính xác không đồng nghĩa nhận diện cấu trúc duy nhất**.

## Định lượng — số ion không tự động bằng nồng độ

Bộ phát hiện đo ion tới thiết bị, không đo trực tiếp số phân tử trung hòa ban đầu.

Các chất khác nhau có hiệu suất ion hóa khác nhau. Thành phần nền có thể cạnh tranh trong ESI và gây **ức chế hoặc tăng cường ion hóa (ion suppression/enhancement)**.

Vì vậy không nên so trực tiếp diện tích đỉnh thô của hai chất khác nhau để suy nồng độ nếu chưa biết hệ số đáp ứng.

### Chuẩn nội đánh dấu đồng vị bền

**Chuẩn nội đánh dấu đồng vị bền (stable-isotope-labeled internal standard)** có hành vi chiết, sắc ký và ion hóa rất gần chất phân tích nhưng `m/z` khác.

Tỉ số chất phân tích/chuẩn nội giúp bù nhiều biến thiên trong chuẩn bị mẫu và ion hóa.

## Hiệu ứng nền

Trong LC–ESI–MS, muối, phospholipid hoặc thành phần nền đồng rửa giải có thể thay đổi hóa học giọt và hiệu suất ion hóa.

Một đỉnh sắc ký đẹp vẫn có thể cho kết quả định lượng sai nếu hiệu ứng nền không được kiểm soát.

Các chiến lược gồm:

- hiệu chuẩn nền tương hợp;
- làm sạch mẫu;
- pha loãng khi phù hợp;
- chuẩn nội đánh dấu đồng vị;
- đánh giá hiệu ứng nền trong thẩm định phương pháp.

Xem thêm [Thẩm định phương pháp và hóa lượng học](./07_method_validation_and_chemometrics.md).

## Ion cộng hợp và hóa học trong nguồn

Phổ ESI có thể xuất hiện nhiều **ion cộng hợp (adduct)**:

```text
[M+H]+
[M+Na]+
[M+NH4]+
[M-H]-
[2M+H]+
```

Một hợp chất vì vậy có thể tạo nhiều đỉnh.

Nếu coi mỗi đỉnh là một phân tử khác nhau sẽ tạo độ phức tạp giả. Mẫu ion cộng hợp, khoảng cách đồng vị và đồng rửa giải sắc ký giúp nhóm các đỉnh liên quan.

## Hiệu chuẩn và khối lượng khóa

Bộ phân tích phải được hiệu chuẩn để ánh xạ thời gian, quỹ đạo hoặc tần số đo sang `m/z`.

Nhiệt độ, trôi điện áp và nhiễm bẩn có thể làm hiệu chuẩn lệch.

Một ion tham chiếu nội hoặc **khối lượng khóa (lock mass)** có thể giúp sửa trôi trong quá trình thu dữ liệu.

Thông số “độ chính xác danh nghĩa” của thiết bị không có nhiều ý nghĩa nếu hiệu chuẩn thực tế không được kiểm soát.

## Khoảng động và bão hòa bộ phát hiện

Dòng ion quá mạnh có thể làm bộ phát hiện hoặc khả năng chứa điện tích của bẫy bị bão hòa. Dòng quá yếu có thể chìm trong nhiễu.

Do đó phát triển phương pháp phải tối ưu **khoảng động (dynamic range)** chứ không chỉ đẩy độ nhạy lên tối đa.

Đánh đổi thường là:

```text
độ nhạy cao hơn
↔ nguy cơ bão hòa / phi tuyến / nhiễu nền lớn hơn
```

## Phổ khối tạo ảnh

**Phổ khối tạo ảnh MALDI (MALDI imaging)** ghi phổ tại nhiều tọa độ trên mô hoặc bề mặt mẫu. Với một `m/z` được chọn, phần mềm dựng bản đồ phân bố không gian.

Phương pháp kết hợp hóa phân tích với thông tin không gian giống hiển vi, dù thiên lệch ion hóa và độ chắc chắn của định danh vẫn là thách thức.

## Xử lý dữ liệu và khoa học dữ liệu

Một thí nghiệm LC–MS có thể tạo hàng triệu điểm dữ liệu.

Quy trình tính toán thường gồm:

```text
chuyển phổ sang dạng centroid
→ phát hiện đỉnh
→ nhóm đồng vị / ion cộng hợp
→ căn chỉnh thời gian lưu
→ trừ mẫu trắng
→ chuẩn hóa
→ so khớp cơ sở dữ liệu
→ thống kê / máy học
```

Thuật toán không thể bù hoàn toàn cho hóa học không được kiểm soát. Chiết mẫu kém, ức chế ion hóa hoặc sắc ký không ổn định sẽ lan sai số tới mọi bước xử lý dữ liệu phía sau.

## Ví dụ suy luận: vì sao cùng nồng độ nhưng hai chất có diện tích đỉnh rất khác?

Hai chất có thể có cùng nồng độ nhưng khác độ proton hóa, sức căng bề mặt của giọt, khả năng desolvation và độ bền ion trong nguồn ESI.

Do đó một chất tạo ion hiệu quả hơn có thể cho tín hiệu lớn hơn nhiều dù số mol ban đầu giống nhau.

Kết luận đúng không phải “chất đó nhiều hơn”, mà là **hệ số đáp ứng khác nhau**. Đây là lý do cần hiệu chuẩn riêng hoặc chuẩn nội phù hợp.

## Ví dụ suy luận: vì sao khối lượng chính xác rất cao vẫn chưa đủ xác định cấu trúc?

Hai đồng phân có cùng công thức phân tử sẽ có cùng khối lượng đơn đồng vị.

Ngay cả khi sai số khối lượng chỉ vài ppm, MS1 vẫn không phân biệt được vị trí liên kết hoặc hóa lập thể.

Cần thêm phổ mảnh, thời gian lưu, phản ứng đặc hiệu, phổ khác hoặc chất chuẩn thật.

MS vì vậy tạo **bằng chứng mạnh**, nhưng cấu trúc hóa học vẫn là bài toán tích hợp nhiều nguồn dữ liệu.

## Những hiểu lầm thường gặp

### “Máy phổ khối đo trực tiếp khối lượng phân tử”

Không. Máy đo `m/z` của ion; khối lượng trung hòa được suy từ trạng thái điện tích và loại ion.

### “Đỉnh có m/z lớn nhất là ion phân tử”

Không nhất thiết. Có thể là ion cộng hợp, đồng vị, dimer hoặc một loài ion khác.

### “Khối lượng chính xác xác định duy nhất cấu trúc”

Không. Đồng phân có thể có cùng công thức và cùng khối lượng chính xác.

### “Có thể so diện tích đỉnh của hai chất khác nhau để suy nồng độ trực tiếp”

Không an toàn nếu chưa hiệu chuẩn hệ số đáp ứng.

### “Ion hóa mềm nghĩa là không phân mảnh”

Không. Nó chỉ làm giảm xu hướng phân mảnh; phân mảnh trong nguồn vẫn có thể xảy ra.

### “Dữ liệu nhiều hơn luôn nghĩa bằng chứng mạnh hơn”

Không. Dữ liệu lặp lại cùng một thiên lệch hóa học chỉ làm thiên lệch được đo chính xác hơn.

## Mô hình tư duy

Hãy xem MS như chuỗi biến đổi thông tin:

```text
phân tử trung hòa
→ tạo ion
→ phân tách theo m/z
→ phát hiện
→ phân mảnh khi cần
→ hiệu chuẩn
→ suy luận hóa học
```

Nguồn ion quyết định vật mang thông tin nào được tạo. Bộ phân tích biến `m/z` thành chuyển động, tần số hoặc thời gian có thể phân biệt. Phân mảnh cung cấp manh mối cấu trúc. Hiệu chuẩn và xử lý dữ liệu biến số ion thô thành bằng chứng hóa học.

Xem tiếp: [Phương pháp điện phân tích](./06_electroanalytical_methods.md) và [Thẩm định phương pháp và hóa lượng học](./07_method_validation_and_chemometrics.md).