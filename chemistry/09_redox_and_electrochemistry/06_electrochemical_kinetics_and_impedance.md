# Động học điện hóa và trở kháng — từ điện thế cân bằng tới tốc độ phản ứng thực tế

> Nhiệt động lực học điện hóa cho biết phản ứng oxy hóa–khử có xu hướng thuận lợi tới đâu; **động học điện hóa (electrochemical kinetics / 전기화학 반응속도론)** cho biết cần đẩy điện thế ra khỏi cân bằng bao nhiêu để tạo tốc độ phản ứng mong muốn. **Phổ trở kháng điện hóa (electrochemical impedance spectroscopy, EIS / 전기화학 임피던스 분광법)** dùng đáp ứng theo tần số để tách các quá trình xảy ra ở những thang thời gian khác nhau.

Chương này là cầu nối giữa [điện thế pin và phương trình Nernst](./03_cell_potential_and_nernst_equation.md), [điện phân](./04_electrolysis.md), [pin và ăn mòn](./05_batteries_corrosion_and_energy_storage.md) và [phương pháp điện phân tích](../12_analytical_chemistry/06_electroanalytical_methods.md). Nếu chưa quen với khuếch tán, có thể xem lại [chất khí](../03_matter_and_phases/00_gases.md) và [động học hóa học](../06_chemical_kinetics/00_reaction_rates.md) để nhớ cách gradient và tốc độ phản ứng được mô hình hóa.

## Điện thế cân bằng không quyết định dòng điện

Xét bán phản ứng:

\[
Ox+ne^-\rightleftharpoons Red
\]

Phương trình Nernst cho điện thế cân bằng:

\[
E_{eq}=E^\circ-\frac{RT}{nF}\ln Q
\]

Tại \(E=E_{eq}\), phản ứng vi mô vẫn có thể xảy ra theo cả hai chiều nhưng dòng ròng bằng 0 vì tốc độ oxy hóa và khử cân bằng nhau.

Muốn tạo dòng ròng hữu hạn, điện cực thường phải bị đẩy khỏi cân bằng. Độ lệch:

\[
\eta=E-E_{eq}
\]

được gọi là **quá thế (overpotential)**.

Có thể hiểu:

```text
Nernst → vị trí cân bằng nhiệt động
quá thế → mức dịch khỏi cân bằng
động học → dòng điện sinh ra từ mức dịch đó
```

Đây là điểm quan trọng: điện thế lớn không tự động đồng nghĩa dòng lớn nếu hàng rào chuyển electron hoặc vận chuyển khối vẫn chậm.

## Mật độ dòng trao đổi — phản ứng có thể nhanh dù dòng ròng bằng 0

Tại cân bằng, dòng oxy hóa và dòng khử có độ lớn bằng nhau. Thang tốc độ của sự trao đổi hai chiều đó được mô tả bằng **mật độ dòng trao đổi (exchange current density, \(j_0\))**.

Nếu \(j_0\) lớn, bề mặt trao đổi electron nhanh và chỉ cần quá thế nhỏ để tạo dòng ròng đáng kể. Nếu \(j_0\) nhỏ, cần quá thế lớn hơn cho cùng mật độ dòng.

Ví dụ, phản ứng tạo hydrogen trên Pt thường có động học thuận lợi hơn trên nhiều vật liệu khác. Khác biệt này không đến từ phương trình Nernst; nó đến từ năng lượng hấp phụ trung gian, cấu trúc bề mặt và hàng rào hoạt hóa.

## Phương trình Butler–Volmer

Một dạng thường dùng của **Butler–Volmer** là:

\[
j=j_0\left[
\exp\left(\frac{\alpha nF\eta}{RT}\right)-
\exp\left(-\frac{(1-\alpha)nF\eta}{RT}\right)
\right]
\]

Trong đó:

- \(j\): mật độ dòng ròng;
- \(j_0\): mật độ dòng trao đổi;
- \(\eta\): quá thế;
- \(\alpha\): hệ số chuyển điện tích;
- \(n\): số electron trong bước mô hình;
- \(F\): hằng số Faraday.

Thông điệp quan trọng hơn việc ghi nhớ biểu thức là: trong vùng chuyển điện tích chi phối, tốc độ phản ứng điện cực thay đổi rất mạnh theo quá thế.

Phương trình này vẫn là mô hình. Khi cơ chế gồm nhiều bước, hấp phụ mạnh, tái cấu trúc bề mặt hoặc vận chuyển khối chi phối, một tập tham số Butler–Volmer đơn giản có thể không đủ mô tả toàn bộ hệ.

## Vùng gần cân bằng và điện trở chuyển điện tích

Khi \(|\eta|\) đủ nhỏ, có thể tuyến tính hóa Butler–Volmer:

\[
j\approx\frac{nFj_0}{RT}\eta
\]

Từ đó xuất hiện **điện trở chuyển điện tích (charge-transfer resistance, \(R_{ct}\))**.

Về mặt tỷ lệ:

\[
R_{ct}\propto\frac{RT}{nFj_0}
\]

Do đó:

```text
j0 lớn → chuyển electron nhanh → Rct nhỏ
j0 nhỏ → chuyển electron chậm → Rct lớn
```

Đây là lý do \(R_{ct}\) thường được dùng trong EIS để theo dõi pin, ăn mòn, cảm biến và xúc tác.

## Quan hệ Tafel

Ở quá thế đủ lớn để một nhánh trong Butler–Volmer chi phối, có thể thu được dạng gần tuyến tính:

\[
\eta=a+b\log j
\]

Đây là **phương trình Tafel (Tafel equation)**.

Độ dốc Tafel có thể chứa thông tin về hệ số chuyển điện tích và đôi khi gợi ý cơ chế. Tuy nhiên không nên gán một cơ chế chỉ dựa trên một độ dốc đo được.

Đường Tafel thực có thể bị méo bởi:

- sụt áp điện trở;
- vận chuyển khối;
- thay đổi diện tích hoạt tính;
- bọt khí;
- nhiều phản ứng song song;
- bề mặt thay đổi trong lúc đo.

Do đó Tafel chỉ hữu ích khi vùng dữ liệu thực sự thuộc chế độ động học phù hợp.

## Ba nguồn phân cực chính

Điện áp vận hành thực thường khác điện thế cân bằng do ba nhóm tổn thất chính.

### Phân cực hoạt hóa

Xuất phát từ hàng rào chuyển electron hoặc các bước phản ứng bề mặt.

### Phân cực điện trở

Do điện trở của:

- chất điện ly;
- màng ngăn;
- điện cực;
- bộ góp dòng;
- tiếp xúc điện.

Tổn thất gần:

\[
\Delta V_{ohmic}=IR
\]

### Phân cực nồng độ

Xuất hiện khi phản ứng tiêu thụ chất tại bề mặt nhanh hơn tốc độ vận chuyển từ dung dịch hoặc pha rắn tới vị trí phản ứng.

Ba đóng góp có thể chồng lên nhau. Vì vậy khi điện áp pin tụt dưới tải, không thể quy mọi tổn thất cho “điện trở trong” theo nghĩa thuần ohmic.

## Dòng giới hạn và vận chuyển khối

Nếu chuyển electron rất nhanh, bước giới hạn có thể trở thành việc đưa chất phản ứng tới bề mặt.

Một biểu thức trực giác cho dòng giới hạn là:

\[
i_L\sim nFA\frac{DC}{\delta}
\]

trong đó:

- \(D\): hệ số khuếch tán;
- \(C\): nồng độ trong pha khối;
- \(\delta\): chiều dày lớp khuếch tán hiệu dụng.

Khuấy mạnh hơn hoặc tạo dòng chảy có kiểm soát làm \(\delta\) nhỏ hơn và tăng dòng giới hạn.

Khi hệ đã bị giới hạn vận chuyển, tăng quá thế thêm không làm dòng tăng tương ứng; thay vào đó phản ứng phụ có thể tăng.

## Điện cực đĩa quay — kiểm soát thủy động lực học

**Điện cực đĩa quay (rotating disk electrode, RDE)** tạo trường dòng chảy có thể tái lập, nhờ đó lớp khuếch tán được kiểm soát tốt hơn.

Phương trình Levich cho quan hệ gần:

\[
i_L\propto nFAD^{2/3}\nu^{-1/6}\omega^{1/2}C
\]

với \(\nu\) là độ nhớt động học và \(\omega\) là tốc độ góc.

Quan hệ:

\[
i_L\propto\omega^{1/2}
\]

cho phép kiểm tra xem dòng có chịu ảnh hưởng mạnh của vận chuyển khối hay không.

## Quan hệ Koutecký–Levich

Nếu cả động học điện cực và vận chuyển khối đều quan trọng:

\[
\frac{1}{i}=\frac{1}{i_k}+\frac{1}{i_L}
\]

Có thể hình dung hai giới hạn này như hai “điện trở tốc độ” mắc nối tiếp: dòng tổng bị giới hạn bởi cả phản ứng bề mặt và khả năng cung cấp chất.

Điểm mạnh của cách biểu diễn này là tách được dòng động học \(i_k\) khỏi dòng giới hạn \(i_L\) dưới những giả định thích hợp.

## Cấu trúc bề mặt quyết định động học

Một tên nguyên tố không đủ mô tả hoạt tính điện hóa. Tốc độ phản ứng còn phụ thuộc:

- mặt tinh thể;
- mật độ khuyết tật;
- độ nhám;
- kích thước hạt;
- lớp oxide;
- chất hấp phụ;
- pH;
- cation/anion của điện ly;
- dung môi;
- thế điện cực trước lịch sử đo.

Bề mặt Pt sạch, Pt bị CO hấp phụ và nanoparticle Pt trên carbon đều có thể hành xử khác nhau dù cùng là Pt.

Đây là cầu nối trực tiếp với [hóa học bề mặt và giao diện](../14_materials_and_polymer_chemistry/05_surface_and_interface_chemistry.md).

## Xúc tác điện hóa

Xúc tác điện hóa không thay đổi điện thế cân bằng của phản ứng tổng. Nó thay đổi hàng rào hoạt hóa và năng lượng của các chất trung gian, nhờ đó giảm quá thế cần cho một mật độ dòng xác định.

Trong điện phân nước, hai phản ứng quan trọng là:

- **phản ứng tạo hydrogen (hydrogen evolution reaction, HER)**;
- **phản ứng tạo oxygen (oxygen evolution reaction, OER)**.

OER thường chậm hơn vì cần nhiều bước chuyển proton/electron và hình thành liên kết O–O.

Một chất xúc tác tốt không chỉ cần hoạt tính cao. Nó còn phải có:

```text
độ chọn lọc
+ độ bền
+ vật liệu đủ phổ biến/kinh tế
+ khả năng vận hành ở mật độ dòng thực tế
```

## Điện thế khởi phát không phải hằng số cơ bản

Trong đường cong dòng–điện thế, **điện thế khởi phát (onset potential)** thường được báo cáo như điểm dòng bắt đầu tăng đáng kể.

Nhưng giá trị này phụ thuộc:

- ngưỡng dòng được chọn;
- diện tích chuẩn hóa;
- tốc độ quét;
- điện trở chưa bù;
- dòng điện dung nền;
- độ nhạy thiết bị.

Vì vậy so sánh xúc tác chỉ bằng một giá trị onset có thể gây hiểu sai.

## Chuẩn hóa dòng điện

Dòng điện có thể được chuẩn hóa theo:

- diện tích hình học;
- diện tích bề mặt điện hóa hoạt động (**electrochemically active surface area, ECSA**);
- khối lượng xúc tác;
- số tâm hoạt tính ước lượng.

Mỗi cách trả lời một câu hỏi khác nhau.

Một điện cực xốp có dòng tổng rất lớn chưa chắc từng tâm phản ứng có hoạt tính cao; nó có thể đơn giản sở hữu nhiều diện tích bề mặt hơn.

## Hiệu suất Faraday

Dòng có thể được chia cho nhiều phản ứng song song. **Hiệu suất Faraday (Faradaic efficiency, FE)** đo phần điện lượng đi vào sản phẩm mong muốn:

\[
FE=\frac{Q_{sản\ phẩm}}{Q_{tổng}}
\]

Một xúc tác có mật độ dòng lớn nhưng FE thấp có thể chủ yếu tạo sản phẩm phụ.

Đánh giá điện xúc tác vì vậy cần xem đồng thời:

```text
hoạt tính
+ độ chọn lọc
+ độ bền
+ hiệu suất năng lượng
```

## Điện trở dung dịch và bù iR

Nếu chất điện ly có điện trở \(R_s\), sụt áp gần:

\[
\Delta V=iR_s
\]

Điện thế thực tại **giao diện điện cực–điện ly (electrode–electrolyte interface)** do đó có thể khác điện thế thiết bị đặt vào.

Trong đo động học chính xác, cần xác định và bù \(iR\) hợp lý.

Bù quá mức có thể gây dao động hoặc tạo dữ liệu giả. Bù không đủ làm đường phân cực trông kém hơn động học thật.

## Lớp điện kép

Tại giao diện điện cực–điện ly, điện tích điện tử trong điện cực được cân bằng bởi ion và phân cực dung môi ở phía điện ly.

Giao diện vì vậy có **điện dung lớp kép (double-layer capacitance, \(C_{dl}\))**.

Dòng nạp điện dung:

\[
i_C=C\frac{dV}{dt}
\]

không cần phản ứng oxy hóa–khử ròng.

Dòng điện dung phải được phân biệt với **dòng Faraday (Faradaic current)** do phản ứng chuyển electron.

## Vì sao EIS dùng tín hiệu xoay chiều nhỏ?

Trong EIS, hệ được đặt gần một trạng thái vận hành rồi áp một nhiễu nhỏ dạng sin:

\[
E(t)=E_0+\Delta E\sin(\omega t)
\]

Nếu biên độ đủ nhỏ để đáp ứng gần tuyến tính, dòng có thể viết gần đúng:

\[
i(t)=I_0\sin(\omega t+\phi)
\]

Tỉ số trong miền tần số định nghĩa **trở kháng (impedance)**:

\[
Z(\omega)=\frac{\tilde E(\omega)}{\tilde I(\omega)}
\]

Khác với điện trở DC, trở kháng có cả độ lớn và pha.

## Số phức trong biểu diễn trở kháng

Ta thường viết:

\[
Z=Z'+jZ''
\]

với:

- \(Z'\): phần thực;
- \(Z''\): phần ảo;
- \(j=\sqrt{-1}\).

Điện trở thuần có pha 0°. Tụ điện lý tưởng có:

\[
Z_C=\frac{1}{j\omega C}
\]

và cuộn cảm lý tưởng:

\[
Z_L=j\omega L
\]

Trong hệ điện hóa, đáp ứng cảm có thể đến từ dây dẫn hoặc một số cơ chế hấp phụ/bề mặt, nên không nên tự động quy mọi loop cảm cho một cuộn cảm vật lý thực sự trong cell.

## Vì sao quét tần số giúp tách cơ chế?

Mỗi quá trình có một thang thời gian đặc trưng.

Với phần tử RC:

\[
\tau\sim RC
\]

Với khuếch tán qua chiều dài \(L\):

\[
\tau_D\sim\frac{L^2}{D}
\]

Tần số cao nhạy với các quá trình nhanh; tần số thấp cho phép các quá trình chậm có thời gian đáp ứng.

Trực giác cốt lõi của EIS là:

> tần số đóng vai trò như một bộ lọc theo thang thời gian.

## Mạch Randles — mô hình tương đương tối thiểu

Một mô hình thường dùng gồm:

```text
Rs — [Rct || Cdl] — thành phần khuếch tán
```

Trong đó:

- \(R_s\): điện trở dung dịch;
- \(R_{ct}\): điện trở chuyển điện tích;
- \(C_{dl}\): điện dung lớp kép;
- phần khuếch tán mô tả vận chuyển khối.

Mạch tương đương là **mô hình toán học**, không phải sơ đồ linh kiện vật lý thật được giấu bên trong cell.

Nhiều mạch khác nhau có thể khớp cùng dữ liệu khá tốt. Vì vậy mô hình phải được ràng buộc bởi cơ chế hóa–lý và hình học hệ.

## Biểu đồ Nyquist

**Biểu đồ Nyquist** thường vẽ:

\[
-Z''\;\text{theo}\;Z'
\]

Trong mô hình đơn giản, bán nguyệt có thể liên hệ với nhánh \(R_{ct}\parallel C_{dl}\), còn đoạn gần 45° ở tần số thấp có thể gợi ý khuếch tán kiểu Warburg.

Nhưng không nên “đọc hình” rồi gán cơ chế ngay lập tức. Nhiều hệ vật lý khác nhau có thể tạo hình dạng tương tự.

## Biểu đồ Bode

Biểu đồ Bode thường thể hiện:

- \(|Z|\) theo tần số;
- góc pha theo tần số.

Dạng này thuận tiện để quan sát nhiều hằng số thời gian trải trên nhiều bậc tần số.

Đỉnh hoặc vai của góc pha có thể gợi ý một quá trình thư giãn riêng biệt, nhưng vẫn cần mô hình hỗ trợ.

## Phần tử pha không đổi

Bề mặt thật thường không hành xử như tụ điện lý tưởng do độ nhám, phân bố tâm phản ứng và tính không đồng nhất.

Một mô hình thực nghiệm phổ biến là **phần tử pha không đổi (constant phase element, CPE)**:

\[
Z_{CPE}=\frac{1}{Q(j\omega)^n}
\]

với:

\[
0<n\le1
\]

Khi \(n=1\), biểu thức trở về tụ điện lý tưởng.

CPE là phần tử mô hình hóa. Không nên tự động gán một ý nghĩa vi mô duy nhất cho mọi giá trị \(n\).

## Trở kháng Warburg và khuếch tán

Với khuếch tán bán vô hạn lý tưởng:

\[
Z_W\propto\frac{1-j}{\sqrt{\omega}}
\]

Trong biểu đồ Nyquist, điều này thường tạo đoạn gần 45°.

Trong pin thật, chiều dài khuếch tán hữu hạn, hình học hạt, độ xốp điện cực và trạng thái sạc làm đáp ứng phức tạp hơn nhiều.

Do đó “đuôi 45° = một hệ số khuếch tán duy nhất” thường là diễn giải quá mức.

## EIS trong pin lithium-ion

Một phổ trở kháng pin có thể chứa đóng góp từ:

- điện trở điện ly;
- màng SEI;
- chuyển điện tích;
- khuếch tán ion trong hạt;
- tiếp xúc điện;
- điện cực xốp.

Khi pin lão hóa, \(R_{ct}\), điện trở màng hoặc đặc trưng khuếch tán có thể thay đổi.

Nhưng EIS không tự trả lời “cơ chế lão hóa là gì”. Cần kết hợp với dữ liệu cấu trúc, thành phần bề mặt, dung lượng, microscopy hoặc spectroscopy để gán nguyên nhân đáng tin cậy.

Xem thêm: [Pin, ăn mòn và lưu trữ năng lượng](./05_batteries_corrosion_and_energy_storage.md).

## EIS trong ăn mòn và lớp phủ

Trong nghiên cứu ăn mòn, điện trở phân cực hoặc \(R_{ct}\) cao thường liên hệ với tốc độ phản ứng điện hóa thấp hơn trong cùng mô hình phù hợp.

Một lớp phủ bảo vệ có thể thêm các hằng số thời gian liên quan tới:

- điện dung lớp phủ;
- điện trở lỗ xốp;
- phản ứng tại kim loại bên dưới.

Theo dõi phổ theo thời gian có thể phát hiện sự xâm nhập nước/ion trước khi hư hỏng nhìn thấy bằng mắt.

## Ba điều kiện nền để EIS có ý nghĩa

### Gần tuyến tính

Nhiễu phải đủ nhỏ để hệ đáp ứng gần tuyến tính quanh điểm làm việc.

### Gần bất biến theo thời gian

Trong lúc quét phổ, hệ không được thay đổi quá nhanh.

Nếu trạng thái sạc (**state of charge, SOC**) trôi mạnh hoặc bề mặt tái cấu trúc nhanh, các điểm tần số đo ở thời điểm khác nhau không còn thuộc cùng một hệ gần bất biến.

### Nhân quả

Đáp ứng phải tuân quan hệ nhân quả vật lý.

Các kiểm tra kiểu **Kramers–Kronig** có thể giúp đánh giá tính tự nhất quán của dữ liệu.

## Nguy cơ khi khớp mạch tương đương

Một mạch có nhiều tham số thường có thể khớp dữ liệu tốt hơn, nhưng đường khớp đẹp không chứng minh cơ chế đúng.

Cần hỏi:

- tham số có giá trị vật lý hợp lý không;
- các tham số có tương quan mạnh không;
- dữ liệu có bao phủ đủ dải tần không;
- mô hình có ổn định giữa các lần đo không;
- có bằng chứng độc lập hỗ trợ cách gán cơ chế không.

Đây là bài toán **nhận dạng mô hình (model identification)**, không chỉ là bài toán tối ưu đường cong.

## Phân bố thời gian thư giãn

**Phân bố thời gian thư giãn (distribution of relaxation times, DRT)** cố gắng biểu diễn phổ như tổng đóng góp của nhiều thang thời gian mà không cần chọn trước một mạch tương đương quá cụ thể.

DRT có thể giúp tách các quá trình chồng lấp, nhưng đây là một bài toán nghịch đảo không ổn định và thường cần **điều chuẩn (regularization)**.

Một đỉnh DRT không nên tự động được gán cho một cơ chế nếu chưa có bằng chứng bổ sung.

## Liên hệ với hệ điều khiển và xử lý tín hiệu

EIS có thể được nhìn như phép phân tích hàm truyền của một hệ hóa–điện:

```text
nhiễu điện thế/dòng
→ hệ điện hóa
→ đáp ứng dòng/điện thế
→ biên độ + pha theo tần số
```

Vì vậy các khái niệm số phức, Fourier, hệ tuyến tính và hàm truyền xuất hiện tự nhiên trong điện hóa.

Đây là một trong những cầu nối rõ nhất giữa Hóa học, Vật lý, Điện tử và xử lý tín hiệu.

## Ví dụ suy luận: vì sao điện áp hở mạch tốt nhưng công suất kém?

Một cell nghỉ lâu có thể đo điện áp hở mạch gần bình thường. Giá trị này chủ yếu phản ánh trạng thái nhiệt động.

Khi nối tải lớn, điện áp có thể tụt mạnh nếu:

- \(R_s\) lớn;
- \(R_{ct}\) lớn;
- khuếch tán ion chậm;
- tiếp xúc điện kém.

Vì vậy điện áp hở mạch không đủ để đánh giá khả năng cấp công suất.

## Ví dụ suy luận: so sánh hai chất xúc tác

Giả sử trong cùng điều kiện, xúc tác A cần quá thế 250 mV để đạt `10 mA/cm²`, còn B cần 400 mV.

Ở điểm làm việc đó, A có động học thuận lợi hơn.

Tuy nhiên chưa thể kết luận A “tốt hơn toàn diện” nếu chưa biết:

- hiệu suất Faraday;
- độ bền;
- loại sản phẩm;
- mức tải vật liệu;
- chi phí;
- điện áp toàn cell.

Đây là ví dụ điển hình của **trade-off**: một chỉ số hoạt tính không thể đại diện toàn bộ hiệu năng hệ.

## Những hiểu lầm thường gặp

### “Điện thế Nernst càng lớn thì dòng càng lớn”

Không. Nernst mô tả cân bằng; dòng phụ thuộc động học và vận chuyển khối.

### “Quá thế chỉ là tổn thất điện trở”

Không. Quá thế có thể đến từ chuyển điện tích, nồng độ và cơ chế bề mặt, không chỉ từ sụt áp ohmic.

### “Bán nguyệt Nyquist luôn là chuyển điện tích”

Không. Cần mô hình vật lý và dữ liệu hỗ trợ.

### “Mạch càng nhiều phần tử thì mô hình càng chính xác”

Không. Quá nhiều tham số có thể tạo **quá khớp (overfitting)** và làm mất khả năng nhận dạng.

### “EIS luôn không xâm lấn”

Biên độ nhiễu nhỏ, nhưng hệ vẫn có thể thay đổi nếu thời gian quét dài hoặc điểm làm việc không ổn định.

## Mô hình tư duy

Hãy tách điện hóa thành ba câu hỏi:

1. **Nhiệt động lực học:** cân bằng nằm ở điện thế nào?
2. **Động học và vận chuyển:** cần quá thế bao nhiêu để tạo dòng mong muốn?
3. **Động lực học theo thời gian:** quá trình nào phản ứng ở thang thời gian nào?

Nernst trả lời câu đầu. Butler–Volmer, Tafel và các mô hình vận chuyển trả lời câu hai. EIS dùng miền tần số để tách câu ba thành các quá trình có tốc độ đặc trưng khác nhau.

Xem tiếp hoặc đối chiếu với [Điện thế pin và phương trình Nernst](./03_cell_potential_and_nernst_equation.md), [Điện phân](./04_electrolysis.md), [Pin, ăn mòn và lưu trữ năng lượng](./05_batteries_corrosion_and_energy_storage.md) và [Phương pháp điện phân tích](../12_analytical_chemistry/06_electroanalytical_methods.md).