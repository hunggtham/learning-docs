# Phương pháp điện phân tích — biến điện thế, dòng và điện lượng thành thông tin định lượng

> **Hóa điện phân tích (electroanalytical chemistry / 전기분석화학)** sử dụng các hiện tượng điện hóa để nhận biết hoặc định lượng chất trong mẫu. Điện thế phản ánh trạng thái nhiệt động gần cân bằng, dòng phản ánh tốc độ truyền điện tích và vận chuyển chất, còn điện lượng phản ánh tổng số electron đã trao đổi. Muốn từ ba tín hiệu này suy ra nồng độ đáng tin cậy, phải kiểm soát thêm điện cực, ma trận mẫu, hiệu chuẩn, phản ứng phụ và độ không đảm bảo.

Chương này tập trung vào **phép đo và suy luận phân tích**. Lý thuyết chi tiết về Butler–Volmer, Tafel, khuếch tán, RDE và EIS được đặt tại [Động học điện hóa và trở kháng](../09_redox_and_electrochemistry/06_electrochemical_kinetics_and_impedance.md). Cách phân chia này tránh lặp nội dung: điện hóa học giải thích cơ chế, còn điện phân tích hỏi cách dùng cơ chế đó để tạo số liệu hóa học đáng tin cậy.

## Ba cửa sổ đo của điện phân tích

Có thể tổ chức phần lớn phương pháp điện phân tích theo ba đại lượng.

### Điện thế

Nếu gần cân bằng và dòng rất nhỏ, điện thế mang thông tin về hoạt độ của các tiểu phần theo quan hệ kiểu Nernst.

### Dòng điện

Nếu đặt hoặc quét điện thế để tạo phản ứng, dòng phụ thuộc đồng thời:

```text
nồng độ
+ động học chuyển electron
+ vận chuyển khối
+ diện tích điện cực
+ phản ứng nền
```

### Điện lượng

Tích phân dòng theo thời gian cho tổng điện lượng:

\[
Q=\int I\,dt
\]

Nếu phản ứng có hóa lượng electron xác định, điện lượng có thể được chuyển trực tiếp thành số mol.

Ba phép đo này trả lời ba câu hỏi khác nhau; không nên dùng một đại lượng như thể nó chứa toàn bộ thông tin của hai đại lượng còn lại.

## Một điện cực không có “điện thế tuyệt đối” đo trực tiếp

Thiết bị luôn đo chênh lệch điện thế giữa các điện cực.

Một phép đo thế đơn giản có thể viết:

```text
điện cực chỉ thị
│
dung dịch mẫu
│
cầu nối điện ly
│
điện cực tham chiếu
```

Điện áp đo được chứa đóng góp từ:

- điện cực chỉ thị hoặc điện cực làm việc;
- điện cực tham chiếu;
- thế nối lỏng;
- đôi khi sụt áp và nhiễu thiết bị.

Vì vậy điện cực tham chiếu là một phần của mô hình đo, không chỉ là “dây nối thứ hai”.

Xem nền nhiệt động: [Điện thế pin và phương trình Nernst](../09_redox_and_electrochemistry/03_cell_potential_and_nernst_equation.md).

## Đo thế — lấy thông tin khi dòng gần bằng 0

**Đo thế (potentiometry)** đo điện áp trong điều kiện dòng ròng rất nhỏ.

Với bán phản ứng tổng quát:

\[
aOx+ne^-\rightleftharpoons bRed
\]

quan hệ Nernst có dạng:

\[
E=E^\circ-\frac{RT}{nF}\ln Q
\]

Điều quan trọng cho phân tích là \(Q\) được xây từ **hoạt độ (activity)**. Nồng độ chỉ thay thế trực tiếp cho hoạt độ khi xấp xỉ lý tưởng đủ tốt hoặc khi phương pháp hiệu chuẩn đã kiểm soát ảnh hưởng nền.

## Điện cực pH — ví dụ điển hình của phép đo hoạt độ

Điện cực thủy tinh tạo thế màng phụ thuộc chênh lệch hoạt độ proton giữa dung dịch bên trong và mẫu.

Ở 25 °C, độ dốc Nernst lý tưởng có độ lớn gần:

\[
59.16\;\mathrm{mV/pH}
\]

Nhưng điện cực thực còn chịu ảnh hưởng của:

- nhiệt độ;
- lão hóa màng;
- thế nối lỏng;
- nhiễm bẩn;
- thời gian đáp ứng;
- sai lệch ở vùng pH rất cao hoặc rất thấp.

Do đó máy pH cần được hiệu chuẩn bằng dung dịch đệm phù hợp. Nếu mẫu dự kiến quanh pH 7–9, dùng chuẩn bao quanh vùng đo thường có ý nghĩa hơn việc chỉ hiệu chuẩn ở một đầu thang.

## Điện cực chọn lọc ion

**Điện cực chọn lọc ion (ion-selective electrode, ISE)** dùng màng có độ ưu tiên tương đối với một ion.

Đáp ứng lý tưởng hóa:

\[
E=K+\frac{RT}{zF}\ln a_i
\]

với \(z\) là điện tích ion.

Từ khóa cần nhấn mạnh là **chọn lọc tương đối**. Màng không “nhìn thấy duy nhất” ion mục tiêu; ion khác có thể gây nhiễu nếu tương tác với màng đủ mạnh.

## Hệ số chọn lọc và ion gây nhiễu

Các phương trình kiểu Nicolsky–Eisenman mở rộng đáp ứng ISE để tính thêm đóng góp của ion gây nhiễu.

Trong thực hành, câu hỏi quan trọng là:

```text
mẫu thật chứa ion nào?
nồng độ của chúng lớn bao nhiêu?
điện cực chọn lọc mục tiêu tốt hơn chúng tới mức nào?
```

Một ISE hoạt động tốt trong chuẩn đơn giản có thể cho bias lớn trong nước biển, huyết thanh hoặc dịch công nghiệp có lực ion cao.

## Lực ion và dung dịch điều chỉnh

Hệ số hoạt độ thay đổi khi lực ion thay đổi. Vì vậy hai dung dịch có cùng nồng độ ion mục tiêu nhưng ma trận ion khác nhau có thể cho điện thế khác.

Một chiến lược là thêm **dung dịch điều chỉnh lực ion (ionic strength adjuster)** vào cả chuẩn và mẫu.

Mục đích không phải “thêm hóa chất cho đủ quy trình”, mà là làm môi trường hoạt độ của chuẩn và mẫu tương đồng hơn để calibration có thể chuyển được từ chuẩn sang mẫu.

## Thế nối lỏng là một nguồn sai số thật

Tại ranh giới giữa hai dung dịch điện ly khác thành phần, các ion khuếch tán với độ linh động khác nhau và có thể tạo **thế nối lỏng (liquid-junction potential)**.

Điện cực tham chiếu thường dùng điện ly nồng độ cao và cặp ion có độ linh động tương đối gần nhau để giảm hiệu ứng này.

Nhưng thế nối không biến mất tuyệt đối. Với phép đo độ chính xác cao, đây là một thành phần của ngân sách độ không đảm bảo.

## Voltammetry — điều khiển điện thế và quan sát dòng

Trong **voltammetry**, điện thế của điện cực làm việc được điều khiển theo một chương trình, còn dòng được đo như đáp ứng.

Hệ ba điện cực thường có:

- điện cực làm việc;
- điện cực tham chiếu;
- điện cực đối.

**Potentiostat** điều khiển điện thế điện cực làm việc so với tham chiếu và dẫn phần lớn dòng qua điện cực đối.

Cấu trúc này giúp điện cực tham chiếu duy trì trạng thái ổn định hơn.

## Dòng Faraday và dòng điện dung

Dòng đo thường chứa nhiều thành phần.

### Dòng Faraday

Xuất hiện khi có phản ứng chuyển electron:

\[
Ox+ne^-\rightleftharpoons Red
\]

Dòng này có thể mang thông tin về chất phân tích.

### Dòng điện dung

Khi điện thế thay đổi, lớp điện kép được nạp hoặc xả. Dòng này có thể xuất hiện mà không có phản ứng oxy hóa–khử ròng.

Trong phân tích vết, dòng điện dung có thể trở thành nền lớn so với tín hiệu Faraday.

Do đó thiết kế dạng xung, chọn thời điểm đọc tín hiệu và trừ nền có thể quan trọng không kém độ nhạy của detector điện tử.

## Vận chuyển chất tới bề mặt điện cực

Chất phân tích tới bề mặt bằng ba cơ chế chính:

1. **khuếch tán (diffusion)** do gradient nồng độ;
2. **đối lưu (convection)** do dòng chất lỏng hoặc khuấy;
3. **di chuyển trong điện trường (migration)** của ion.

Trong nhiều phép voltammetry, điện ly nền được thêm với nồng độ lớn để giảm đóng góp migration của chất phân tích, làm bài toán chủ yếu phụ thuộc khuếch tán.

Định luật Fick:

\[
J=-D\frac{dC}{dx}
\]

và quan hệ dòng–thông lượng:

\[
i=nFAJ
\]

cho thấy tín hiệu điện có thể là ảnh trực tiếp của vận chuyển vật chất.

## Voltammetry vòng — công cụ cơ chế trước khi là công cụ định lượng

**Voltammetry vòng (cyclic voltammetry, CV)** quét điện thế theo một chiều rồi đảo ngược.

Một cặp oxy hóa/khử có thể tạo peak thuận và peak nghịch. Hình dạng và vị trí peak chứa thông tin về:

- điện thế oxy hóa–khử;
- độ thuận nghịch điện hóa;
- khuếch tán;
- hấp phụ;
- phản ứng hóa học ghép sau hoặc trước bước electron.

CV thường rất mạnh để kiểm tra cơ chế và chọn vùng điện thế trước khi xây phương pháp định lượng.

## Randles–Ševčík như một mô hình chẩn đoán

Trong điều kiện khuếch tán phẳng và hệ thuận nghịch phù hợp:

\[
i_p\propto n^{3/2}AD^{1/2}C\nu^{1/2}
\]

với \(\nu\) là tốc độ quét.

Nếu:

\[
i_p\propto\nu^{1/2}
\]

đó là dấu hiệu phù hợp với hệ bị chi phối mạnh bởi khuếch tán.

Nếu dòng tỷ lệ gần \(\nu\), hấp phụ bề mặt có thể đóng góp lớn.

Đây là **dấu hiệu chẩn đoán**, không phải quy tắc tuyệt đối áp dụng cho mọi cơ chế và hình học điện cực.

## Khi động học chuyển electron trở nên quan trọng

Nếu chuyển electron chậm, bề mặt không duy trì được trạng thái gần Nernst khi điện thế thay đổi nhanh.

Khi đó peak có thể dịch, khoảng cách peak tăng hoặc hình dạng đường cong thay đổi.

Lý thuyết Butler–Volmer, Tafel, mật độ dòng trao đổi và quá thế được trình bày chi tiết tại [Động học điện hóa và trở kháng](../09_redox_and_electrochemistry/06_electrochemical_kinetics_and_impedance.md). Trong điện phân tích, ta chủ yếu dùng chúng để trả lời:

> tín hiệu thay đổi vì nồng độ thay đổi, hay vì động học bề mặt thay đổi?

Phân biệt hai nguyên nhân này rất quan trọng khi xây calibration.

## Phản ứng hóa học ghép với chuyển electron

Một số mô-típ thường ký hiệu:

```text
E   : bước electron
EC  : electron → phản ứng hóa học
CE  : phản ứng hóa học → electron
ECE : electron → hóa học → electron
```

Nếu sản phẩm khử nhanh chóng phản ứng thành chất khác, peak hồi trong CV có thể giảm hoặc biến mất.

Do đó peak mất đi có thể là bằng chứng cơ chế, không nhất thiết là lỗi thiết bị.

## Amperometry — giữ điện thế và đo dòng theo thời gian

Trong **amperometry**, điện thế được giữ tại vùng mà chất phân tích phản ứng, rồi dòng được theo dõi.

Nếu vận chuyển khối được kiểm soát và phản ứng đủ chọn lọc, dòng có thể liên hệ với nồng độ.

Ứng dụng gồm:

- cảm biến glucose;
- detector điện hóa sau sắc ký;
- cảm biến oxygen;
- biosensor enzyme.

Nhược điểm lớn là các chất gây nhiễu có thể phản ứng tại cùng điện thế, vì vậy selectivity thường phải đến từ màng, enzyme, catalyst hoặc bước tách trước đó.

## Chronoamperometry — tín hiệu thời gian của khuếch tán

Sau bước nhảy điện thế, dòng khuếch tán trên điện cực phẳng lý tưởng thường giảm theo quan hệ Cottrell:

\[
i(t)=nFAC\sqrt{\frac{D}{\pi t}}
\]

Theo thời gian, lớp khuếch tán dày hơn và gradient nồng độ giảm, nên dòng giảm.

Đây là một ví dụ tốt cho việc tín hiệu điện hóa không chỉ phụ thuộc nồng độ mà còn phụ thuộc **thời gian kể từ khi điều kiện biên thay đổi**.

## Điện cực đĩa quay trong phương pháp đo

**Điện cực đĩa quay (rotating disk electrode, RDE)** tạo đối lưu có kiểm soát và làm vận chuyển khối dễ tái lập hơn.

Thay đổi tốc độ quay cho phép phân biệt phần dòng do vận chuyển với phần do động học phản ứng.

Chi tiết phương trình Levich và Koutecký–Levich được giữ ở chapter lý thuyết điện hóa để tránh lặp. Trong phân tích, giá trị của RDE nằm ở việc tạo **điều kiện vận chuyển có thể kiểm soát và tái lập**.

## Coulometry — đếm electron bằng điện lượng

**Coulometry** đo:

\[
Q=\int I\,dt
\]

Nếu mỗi mol chất phân tích trao đổi \(z\) mol electron và hiệu suất dòng đạt gần 100%:

\[
n_{analyte}=\frac{Q}{zF}
\]

Ưu điểm lớn là điện lượng có thể được đo rất chính xác mà không cần chuẩn nồng độ titrant như trong volumetry.

Nhược điểm là phản ứng phụ, dòng nền hoặc chuyển hóa không hoàn toàn làm điện lượng không còn tương ứng riêng với chất phân tích.

## Chuẩn độ coulometric

Thay vì chuẩn bị titrant có nồng độ biết trước, có thể tạo titrant **ngay trong cell (in situ)** bằng điện phân.

Nếu dòng gần không đổi:

\[
Q=It
\]

Từ thời gian tới điểm cuối, suy ra số mol chất phản ứng đã được tạo điện hóa.

Cách này hữu ích khi titrant khó bảo quản hoặc lượng cần dùng rất nhỏ.

## Đo độ dẫn

**Độ dẫn điện (conductivity)** của dung dịch phụ thuộc nồng độ, điện tích và độ linh động của tất cả ion.

Một biểu thức khái niệm:

\[
\kappa\sim\sum_i c_i z_i u_i
\]

Nhiệt độ ảnh hưởng mạnh vì độ nhớt và độ linh động ion thay đổi. Vì vậy đo độ dẫn chính xác thường phải kiểm soát hoặc hiệu chỉnh nhiệt độ.

## Chuẩn độ dẫn điện

Trong chuẩn độ acid mạnh bằng base mạnh, \(H^+\) có độ linh động rất cao dần bị thay bằng các ion kém linh động hơn, nên độ dẫn giảm.

Sau điểm tương đương, \(OH^-\) dư làm độ dẫn tăng trở lại.

Đường cong độ dẫn vì vậy có thể cho điểm tương đương ngay cả khi mẫu đục hoặc có màu, nơi chỉ thị quang học kém thuận tiện.

## Voltammetry xung và stripping — tăng tỷ lệ tín hiệu/nền

Các kỹ thuật xung như **differential-pulse voltammetry** hoặc **square-wave voltammetry** chọn thời điểm lấy mẫu dòng để giảm ảnh hưởng của dòng điện dung.

Trong **stripping voltammetry**, chất phân tích được tích lũy trước lên điện cực, sau đó được hòa tan hoặc oxy hóa/khử trở lại trong bước đo.

Bước làm giàu trước giúp tăng độ nhạy cho phân tích vết.

Trade-off là phương pháp trở nên nhạy với:

- trạng thái bề mặt;
- thời gian tích lũy;
- chất cạnh tranh;
- tốc độ khuấy;
- điều kiện stripping.

## EIS trong điện phân tích — dùng như tín hiệu, không lặp lại toàn bộ lý thuyết

**Phổ trở kháng điện hóa (EIS)** có thể được dùng để theo dõi thay đổi giao diện do chất phân tích liên kết, enzyme phản ứng hoặc lớp màng biến đổi.

Lý thuyết về Nyquist, Bode, Randles, CPE, Warburg và DRT nằm ở [Động học điện hóa và trở kháng](../09_redox_and_electrochemistry/06_electrochemical_kinetics_and_impedance.md).

Trong bối cảnh phân tích, câu hỏi chính là:

```text
đại lượng EIS nào thay đổi theo analyte?
quan hệ đó có chọn lọc không?
calibration có ổn định theo thời gian không?
ma trận mẫu có làm giao diện thay đổi độc lập với analyte không?
```

Một mạch tương đương khớp đẹp không tự chứng minh cảm biến có tính đặc hiệu hóa học.

## Bề mặt điện cực và fouling

Điện cực là một giao diện hoạt động hóa học, nên trạng thái bề mặt có thể thay đổi sau mỗi mẫu.

Protein, polymer, oxide hoặc sản phẩm phản ứng có thể bám lên điện cực và gây **bám bẩn bề mặt (fouling)**.

Hệ quả:

- diện tích hoạt tính giảm;
- động học chuyển electron thay đổi;
- dòng nền thay đổi;
- calibration trôi.

Do đó quy trình phân tích có thể cần:

- đánh bóng;
- làm sạch điện hóa;
- tái tạo màng;
- giới hạn số lần dùng;
- mẫu kiểm soát định kỳ.

Một điện cực rất nhạy khi mới chế tạo nhưng trôi mạnh sau năm mẫu chưa phải là cảm biến định lượng tốt.

## Hiệu chuẩn và hiệu ứng nền

Tín hiệu điện hóa có thể phụ thuộc:

- pH;
- lực ion;
- oxygen hòa tan;
- chất tạo phức;
- độ nhớt;
- surfactant;
- fouling;
- thành phần dung môi.

Vì vậy calibration trong nước tinh khiết có thể không chuyển được sang huyết thanh, thực phẩm hoặc nước thải.

Các chiến lược gồm:

- hiệu chuẩn nền tương hợp (**matrix matching**);
- thêm chuẩn (**standard addition**);
- chuẩn nội trong hệ phù hợp;
- tiền xử lý hoặc tách nền;
- pha loãng mẫu nếu độ nhạy cho phép.

Xem thêm: [Thẩm định phương pháp và chemometrics](./07_method_validation_and_chemometrics.md).

## Cảm biến điện hóa — nhận diện phải đi trước chuyển đổi tín hiệu

Một cảm biến có thể được mô tả:

```text
nhận diện hóa học/sinh học
→ thay đổi trạng thái giao diện hoặc phản ứng
→ điện thế / dòng / trở kháng thay đổi
→ calibration
→ ước lượng lượng chất
```

Hiệu năng phải được đánh giá theo nhiều chiều:

- độ nhạy;
- độ chọn lọc;
- khoảng làm việc;
- LOD/LOQ;
- thời gian đáp ứng;
- drift;
- độ lặp lại;
- fouling;
- tuổi thọ;
- sai khác giữa các lô cảm biến.

Một prototype cho tín hiệu lớn với chuẩn tinh khiết chưa đủ chứng minh nó là cảm biến tốt trong mẫu thực.

## Ví dụ: cảm biến glucose

Enzyme glucose oxidase tạo ra một chuỗi biến đổi có thể ghép với phép đo điện hóa.

Có thể hình dung:

```text
glucose khuếch tán qua màng
→ enzyme phản ứng
→ chất trung gian hoặc mediator thay đổi trạng thái redox
→ electron chuyển với điện cực
→ dòng được đo
```

Nếu nồng độ oxygen, hoạt tính enzyme, độ dày màng hoặc fouling thay đổi, độ nhạy cũng thay đổi.

Vì vậy tín hiệu không chỉ phụ thuộc glucose; nó phụ thuộc cả hệ chuyển đổi.

Đây là lý do thẩm định sensor phải bao gồm điều kiện môi trường, độ ổn định và ma trận mẫu.

## Độ không đảm bảo trong điện phân tích

Nguồn độ không đảm bảo có thể đến từ:

- chuẩn bị chuẩn;
- điện cực tham chiếu;
- thế nối lỏng;
- nhiệt độ;
- diện tích/trạng thái bề mặt;
- dòng nền;
- lựa chọn baseline/peak;
- drift;
- ma trận mẫu;
- độ lặp lại quy trình làm sạch.

Trong ISE, slope Nernst và thế nối có thể quan trọng. Trong stripping voltammetry, blank và fouling có thể chi phối. Trong biosensor, biến thiên enzyme/màng có thể lớn hơn sai số điện tử của máy.

Do đó ngân sách độ không đảm bảo phải mô tả **toàn quy trình**, không chỉ thông số của potentiostat.

## Ví dụ suy luận: peak CV giảm sau nhiều lần quét nghĩa là gì?

Không nên kết luận ngay rằng nồng độ chất phân tích giảm.

Các khả năng gồm:

- analyte thật sự bị tiêu thụ;
- sản phẩm phủ điện cực;
- điện cực bị fouling;
- phản ứng hóa học ghép làm mất dạng redox;
- chất phân tích khuếch tán chậm hơn do thay đổi môi trường;
- baseline thay đổi.

Cần thiết kế thí nghiệm đối chứng để phân biệt nguyên nhân.

Đây là tư duy trung tâm của hóa phân tích: **một tín hiệu có thể có nhiều cơ chế sinh ra**.

## Những hiểu lầm thường gặp

### “Điện thế là dòng điện”

Không. Điện thế là năng lượng trên đơn vị điện tích; dòng là tốc độ truyền điện tích.

### “Thế oxy hóa–khử cao nghĩa phản ứng electron nhanh”

Không. Điện thế thuộc nhiệt động lực học; tốc độ thuộc động học và vận chuyển.

### “ISE cho trực tiếp nồng độ tuyệt đối”

Không. Nền tảng đáp ứng theo hoạt độ và còn chịu ion gây nhiễu, thế nối, nhiệt độ và hiệu chuẩn.

### “Peak CV lớn hơn nghĩa phản ứng nhanh hơn”

Không nhất thiết. Dòng còn phụ thuộc nồng độ, khuếch tán, diện tích, hấp phụ và tốc độ quét.

### “EIS khớp được mạch đẹp nghĩa cảm biến có cơ chế đúng”

Không. Nhiều mô hình có thể khớp tương tự; cần bằng chứng hóa học và validation độc lập.

### “Cảm biến càng nhạy càng tốt”

Không. Độ chọn lọc, drift, fouling, reproducibility và độ bền trong mẫu thật có thể quan trọng hơn slope cực lớn trong mẫu chuẩn.

## Mô hình tư duy

Điện phân tích là một **bài toán suy ngược**:

```text
nồng độ / activity / trạng thái hóa học
→ cân bằng + kinetics + transport + interface
→ tín hiệu điện
→ calibration/model
→ kết quả định lượng + uncertainty
```

Thiết bị chỉ đo tín hiệu ở giữa chuỗi. Chất lượng kết quả phụ thuộc việc hiểu và kiểm soát toàn bộ các bước nối tín hiệu đó với lượng chất cần báo cáo.

Xem tiếp: [Thẩm định phương pháp và chemometrics](./07_method_validation_and_chemometrics.md). Đối với lý thuyết điện hóa sâu hơn, xem [Điện thế pin và phương trình Nernst](../09_redox_and_electrochemistry/03_cell_potential_and_nernst_equation.md) và [Động học điện hóa và trở kháng](../09_redox_and_electrochemistry/06_electrochemical_kinetics_and_impedance.md).