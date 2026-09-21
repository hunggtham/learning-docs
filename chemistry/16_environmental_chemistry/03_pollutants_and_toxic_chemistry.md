# Chất ô nhiễm và hóa học độc chất — liều, dạng tồn tại, phơi nhiễm và số phận môi trường

> **Hóa học độc chất (toxic chemistry / 독성 화학)** không thể được suy ra chỉ từ tên một chất. Mức gây hại phụ thuộc **liều × đường phơi nhiễm × thời gian × dạng hóa học × chuyển hóa × độ nhạy của đối tượng**. Trong môi trường còn phải xét vận chuyển, độ bền và khả năng chất thật sự tới được sinh vật hay cơ quan đích.

Chương này nối trực tiếp với [hóa học nước](./01_water_chemistry.md), [hóa học đất](./02_soil_chemistry.md), [động học phản ứng](../06_chemical_kinetics/00_reaction_rates.md), [hóa học phối trí](../10_inorganic_chemistry/03_coordination_chemistry.md), [redox](../09_redox_and_electrochemistry/00_oxidation_and_reduction.md), [hóa học hữu cơ](../11_organic_chemistry/03_organic_reaction_mechanisms.md) và [đo lường/lấy mẫu](../12_analytical_chemistry/00_measurement_and_sampling.md).

## Mối nguy không đồng nghĩa rủi ro

**Mối nguy (hazard / 유해성)** là khả năng nội tại của một tác nhân gây hại.

**Rủi ro (risk / 위험도)** phụ thuộc thêm mức phơi nhiễm.

```text
hazard cao + exposure gần 0
→ risk thực có thể thấp

hazard vừa + exposure kéo dài rộng khắp
→ risk quần thể có thể đáng kể
```

Do đó phát hiện một chất trong mẫu chưa đủ để kết luận mức nguy hiểm thực tế.

## “Liều tạo nên độc tính” — nhưng liều nào?

“Liều” có thể nghĩa:

- liều ngoài cơ thể;
- liều hấp thụ;
- nồng độ trong máu;
- liều tại mô đích;
- nồng độ đỉnh;
- tổng phơi nhiễm tích lũy.

Cùng liều ngoài không đảm bảo cùng liều trong vì hấp thu, phân bố, chuyển hóa và thải trừ khác nhau.

## Đường phơi nhiễm

Các đường chính gồm:

- hít;
- ăn/uống;
- da;
- đường xuyên mô trong bối cảnh y tế/nghề nghiệp.

Đường tiếp xúc thay đổi tốc độ hấp thu và mức chuyển hóa trước khi chất tới tuần hoàn chung.

Một chất hít vào có thể tới phổi rất nhanh, trong khi chất ăn vào có thể trải qua acid dạ dày và chuyển hóa qua gan trước.

## Độc tính cấp và mãn

**Độc tính cấp (acute toxicity)** xuất hiện sau phơi nhiễm ngắn hoặc liều cao.

**Độc tính mãn (chronic toxicity)** liên quan phơi nhiễm kéo dài/lặp lại và có thể gây ảnh hưởng cơ quan, thần kinh, sinh sản hoặc ung thư.

`LD50` chỉ là một endpoint tử vong cấp trong điều kiện thử nghiệm cụ thể, không phải “điểm độc tính tổng quát”.

## Quan hệ liều–đáp ứng

Một số tác động có ngưỡng tương đối rõ; một số loại rủi ro được mô hình hóa bảo thủ hơn theo giả định không ngưỡng tùy mục đích quản lý.

Các đại lượng thường gặp gồm:

- NOAEL;
- LOAEL;
- liều chuẩn (benchmark dose);
- liều tham chiếu.

Chúng là kết quả của mô hình và dữ liệu, không phải hằng số phân tử bất biến.

## Độc động học — cơ thể làm gì với chất?

Độc động học thường được tổ chức bằng `ADME`:

```text
Absorption   → hấp thu
Distribution → phân bố
Metabolism   → chuyển hóa
Excretion    → thải trừ
```

Nồng độ tại mô đích là kết quả của cả bốn quá trình.

### Mô hình một ngăn và thời gian bán thải

Nếu thải trừ gần bậc nhất:

\[
C(t)=C_0e^{-kt}
\]

\[
t_{1/2}=\frac{\ln2}{k}
\]

Nếu chất được đưa vào lặp lại nhanh hơn tốc độ thải trừ, nồng độ có thể tích lũy tới trạng thái gần ổn định.

Đây là ứng dụng trực tiếp của động học bậc nhất, không phải một công thức độc học tách biệt.

## Chuyển hóa có thể giải độc hoặc hoạt hóa độc tính

Chuyển hóa thường làm phân tử phân cực hơn và dễ thải hơn, nhưng có thể tạo chất trung gian phản ứng mạnh hơn chất mẹ.

Ví dụ một số chất được chuyển hóa thành **tác nhân ái điện (electrophile)** có thể phản ứng cộng hóa trị với protein hoặc DNA.

Do đó “chất mẹ biến mất” không đồng nghĩa “hệ đã được giải độc”.

### Pha I và pha II

Phản ứng pha I thường gồm oxy hóa, khử hoặc thủy phân; cytochrome P450 tham gia nhiều hệ.

Phản ứng pha II thường gắn thêm nhóm phân cực như glucuronide, sulfate hoặc glutathione.

Cách chia này là khung tổ chức; con đường thật có thể không luôn đi tuần tự I → II.

### Glutathione và electrophile

Glutathione có thể bắt chất trung gian ái điện:

```text
GSH + electrophile
→ chất liên hợp
```

Nếu hệ giải độc bị quá tải, phản ứng cộng hóa trị với đại phân tử sinh học có thể tăng.

## Dạng tồn tại hóa học quyết định hành vi

Cùng một nguyên tố có thể có độc tính và độ linh động rất khác tùy trạng thái oxy hóa, ligand và dạng pha.

### Mercury

`Hg0` dễ bay hơi và đặc biệt quan trọng qua đường hít. `Hg2+` có hành vi phân bố khác. Methylmercury có khả năng tích lũy sinh học và đi vào hệ thần kinh mạnh hơn nhiều dạng vô cơ.

### Chromium

Cr(III) và Cr(VI) khác mạnh về trạng thái oxy hóa, hình học ion, vận chuyển qua màng và tính phản ứng.

Vì vậy “tổng Cr” không mô tả đầy đủ rủi ro.

Phần này nối trực tiếp với khái niệm **speciation** trong [hóa học nước](./01_water_chemistry.md) và [hóa vô cơ](../10_inorganic_chemistry/00_inorganic_compounds.md).

## Redox và stress oxy hóa

Một số kim loại hoặc quinone có thể tham gia chu trình redox và tạo tiểu phân oxygen phản ứng.

Ví dụ phản ứng Fenton:

\[
Fe^{2+}+H_2O_2\rightarrow Fe^{3+}+OH^-+\cdot OH
\]

Gốc hydroxyl phản ứng rất nhanh gần nơi được tạo.

**Stress oxy hóa (oxidative stress)** xuất hiện khi tốc độ tạo các tiểu phân phản ứng vượt khả năng chống oxy hóa và sửa chữa của hệ.

ROS không phải lúc nào cũng “xấu”; chúng còn tham gia tín hiệu tế bào. Vấn đề là **liều, vị trí và khả năng kiểm soát**.

## Chất ô nhiễm hữu cơ bền

**Chất ô nhiễm hữu cơ bền (persistent organic pollutants, POPs)** thường có một số đặc điểm:

- bền môi trường;
- ưa lipid;
- có thể vận chuyển xa;
- tích lũy sinh học;
- gây độc.

Các ví dụ lịch sử gồm PCB và một số thuốc trừ sâu organochlorine.

## Tích lũy và khuếch đại sinh học

**Tích lũy sinh học (bioaccumulation)** xảy ra khi tốc độ hấp thu vượt tốc độ thải trong khoảng thời gian đủ dài.

**Bioconcentration** nhấn mạnh hấp thu trực tiếp từ môi trường xung quanh.

**Khuếch đại sinh học (biomagnification)** mô tả nồng độ tăng qua các bậc dinh dưỡng khi chất bền được truyền qua thức ăn.

Không phải mọi chất bền đều khuếch đại giống nhau vì chuyển hóa và thải trừ khác nhau.

## Hệ số phân bố octanol/nước

Một chỉ báo về xu hướng ưa lipid là:

\[
K_{ow}=\frac{C_{octanol}}{C_{water}}
\]

`log Kow` cao thường liên hệ xu hướng phân bố vào pha hữu cơ/lipid.

Nhưng với chất có thể ion hóa, **hệ số phân bố D ở pH xác định** thường hữu ích hơn vì phần ion hóa có hành vi khác dạng trung hòa.

Đây là ứng dụng của phân bố pha và acid–base, không chỉ là một chỉ số độc học độc lập.

## PFAS — một họ hóa chất, không phải một chất duy nhất

Nhiều PFAS có các phần carbon fluor hóa với liên kết C–F bền.

Tuy nhiên độ dài chuỗi, nhóm đầu và tiền chất làm vận chuyển, hấp phụ và tích lũy sinh học khác nhau mạnh.

Một số PFAS chuỗi ngắn linh động trong nước; một số chất chuỗi dài liên kết mạnh hơn với protein/trầm tích.

Cụm từ “forever chemicals” dễ nhớ nhưng không thay thế phân tích hóa học từng cấu trúc và sản phẩm biến đổi.

## Chất gây rối loạn nội tiết

Hệ hormone hoạt động ở nồng độ thấp và phụ thuộc giai đoạn phát triển.

Chất ngoại lai có thể:

- hoạt hóa receptor;
- ức chế receptor;
- thay đổi tổng hợp hormone;
- thay đổi chuyển hóa hormone;
- ảnh hưởng protein vận chuyển.

Một số hệ có quan hệ liều–đáp ứng không đơn điệu, nên ngoại suy từ liều cao xuống liều thấp cần thận trọng.

## Độc gen và sinh ung thư

Chất độc gen có thể làm tổn thương DNA trực tiếp hoặc gián tiếp.

Một số chất được chuyển hóa thành electrophile tạo **adduct DNA**. Nếu tổn thương không được sửa trước sao chép, đột biến có thể được cố định.

Nhưng sinh ung thư là quá trình nhiều bước còn phụ thuộc sửa chữa, tăng sinh, miễn dịch và bối cảnh mô.

Đây là cầu nối trực tiếp giữa cơ chế hữu cơ và sinh học phân tử.

## Độc tính của hạt

Độc tính của hạt phụ thuộc:

- kích thước;
- hình dạng;
- thành phần;
- độ tan;
- độ phản ứng bề mặt;
- độ bền sinh học.

Hạt mịn/siêu mịn có diện tích bề mặt lớn trên đơn vị khối lượng và có thể đi sâu hơn trong hệ hô hấp.

Sợi asbestos còn có yếu tố hình học và độ bền sinh học làm quá trình loại bỏ khó hơn.

Phần nền về kích thước/bề mặt nối với [vật liệu nano](../14_materials_and_polymer_chemistry/04_nanomaterials.md).

## Chất ô nhiễm không khí và nước

Không khí có thể chứa bụi hạt, ozone, `NOx`, `SO2`, CO và VOC. Nhiều chất quan trọng là **ô nhiễm thứ cấp**, không phải chất phát thải ban đầu.

Nước có thể chứa N/P, mầm bệnh, kim loại, thuốc trừ sâu, dung môi, dược chất, PFAS và vi nhựa.

Cách xử lý phụ thuộc dạng hóa học, kích thước, pha và cơ chế phân hủy.

## Phú dưỡng

Dư nitrogen/phosphorus thúc đẩy tăng trưởng sinh khối.

Khi sinh khối phân hủy, oxygen bị tiêu thụ và có thể tạo vùng thiếu oxygen hoặc kỵ khí.

Chuỗi cơ chế đã được giải thích sâu hơn ở [hóa học nước](./01_water_chemistry.md).

## Số phận môi trường — chất đi đâu và biến đổi thế nào?

Chất ô nhiễm có thể trải qua:

- quang phân;
- thủy phân;
- oxy hóa–khử;
- phân hủy sinh học;
- hấp phụ/giải hấp;
- bay hơi;
- chuyển pha.

Sản phẩm biến đổi có thể ít độc hơn, tương đương hoặc độc hơn chất ban đầu.

## Phân hủy gần bậc nhất và giới hạn của việc nhìn nồng độ giảm

Một mô hình mất mát đơn giản:

\[
\frac{dC}{dt}=-kC
\]

\[
C=C_0e^{-kt}
\]

Nhưng nồng độ trong nước giảm có thể chỉ vì chất chuyển sang trầm tích hoặc bay vào khí, không phải vì phân tử đã bị phá hủy.

Do đó phải dùng **cân bằng khối lượng** để phân biệt:

```text
phân hủy thật
≠ chuyển sang pha khác
```

## Quang phân trực tiếp và gián tiếp

Quang phân trực tiếp yêu cầu chất hấp thụ ánh sáng ở vùng bước sóng thật sự tới môi trường.

Quang phân gián tiếp có thể xảy ra qua `OH·` hoặc trạng thái kích thích của chất hữu cơ tự nhiên.

Tốc độ phụ thuộc phổ ánh sáng, độ sâu, độ đục và thành phần nền.

Phần nền photon/phổ được nối với [phổ học](../12_analytical_chemistry/03_spectroscopy.md).

## Hấp phụ làm chậm vận chuyển nhưng không phá hủy chất

Một chất hấp phụ mạnh lên đất có thể di chuyển chậm nhưng vẫn tồn tại nguyên vẹn.

Nếu pH, độ mặn hoặc chất hữu cơ thay đổi, nó có thể giải hấp và trở lại pha nước.

Do đó **cố định** giảm phơi nhiễm hiện tại nhưng không đồng nghĩa **phân hủy**.

## Đám ô nhiễm nước ngầm

Vận chuyển dưới đất ghép:

```text
đối lưu
+ phân tán
+ hấp phụ
+ phản ứng
+ phân hủy sinh học
+ hiệu ứng mật độ
```

Hình dạng đám ô nhiễm vì vậy phản ánh cả thủy văn lẫn hóa học.

## Khung đánh giá rủi ro

Một quy trình thường gồm:

1. nhận diện mối nguy;
2. đánh giá liều–đáp ứng;
3. đánh giá phơi nhiễm;
4. đặc trưng hóa rủi ro.

Độ không đảm bảo và khác biệt giữa cá thể/quần thể phải được thể hiện rõ thay vì giấu trong một con số duy nhất.

## Đánh giá phơi nhiễm và vai trò của hóa phân tích

Cần biết:

- nồng độ;
- tần suất tiếp xúc;
- thời gian;
- đường phơi nhiễm;
- hành vi;
- nhóm nhạy cảm.

Nếu dữ liệu lấy mẫu hoặc định lượng bị bias, ước lượng rủi ro phía sau cũng bị bias.

Đây là lý do [thẩm định phương pháp](../12_analytical_chemistry/07_method_validation_and_chemometrics.md) là prerequisite thực tế của risk assessment.

## Liều tham chiếu và hệ số không đảm bảo

Mức hướng dẫn có thể được xây từ một điểm hiệu ứng rồi áp dụng hệ số không đảm bảo để xét khác biệt loài, quần thể và thiếu dữ liệu.

Các hệ số này là công cụ quản lý rủi ro, không phải ngưỡng sinh học chính xác tuyệt đối.

## Độc tính hỗn hợp

Phơi nhiễm thực tế thường gồm nhiều chất.

Tác động có thể:

- độc lập;
- cộng tính;
- hiệp đồng;
- đối kháng.

Số tổ hợp tăng rất nhanh nên đánh giá hỗn hợp là bài toán khó. Nhóm chất theo cơ chế tác động đôi khi giúp giảm độ phức tạp.

## Truyền thông rủi ro

“Phát hiện được” không đồng nghĩa “nguy hiểm”.

Giới hạn phát hiện có thể thấp hơn nhiều mức liên quan sức khỏe.

Ngược lại, “dưới giới hạn phát hiện” không có nghĩa nồng độ bằng 0.

Thông tin tốt phải phân biệt:

```text
presence
≠ hazard
≠ exposure
≠ risk
```

## Ví dụ suy luận: vì sao tổng Hg không đủ để đánh giá rủi ro ăn cá?

Hai mẫu cá có thể có cùng tổng Hg nhưng tỷ lệ methylmercury khác nhau.

Methylmercury có khả năng tích lũy và phân bố sinh học khác nhiều dạng vô cơ.

Do đó **speciation** có thể quan trọng hơn tổng nguyên tố khi đánh giá phơi nhiễm thực.

## Ví dụ suy luận: vì sao nồng độ chất ô nhiễm trong nước giảm chưa chắc môi trường đã sạch hơn?

Nếu chất hấp phụ lên trầm tích, nồng độ nước giảm nhưng tổng khối lượng trong hệ gần như không đổi.

Một thay đổi pH hoặc redox sau này có thể làm chất được giải phóng trở lại.

Cần theo dõi **mass balance + phase distribution + transformation**, không chỉ một pha nước.

## Những hiểu lầm thường gặp

### “Chất tự nhiên an toàn, chất tổng hợp nguy hiểm”

Không. Nguồn gốc không quyết định độc tính; cấu trúc, liều và phơi nhiễm mới quan trọng.

### “Chất đã biến mất khỏi nước nghĩa đã phân hủy”

Không. Nó có thể chỉ chuyển pha.

### “LD50 cho biết chất nguy hiểm trong mọi tình huống”

Không. Nó chỉ là một endpoint độc tính cấp dưới điều kiện xác định.

### “Tổng nồng độ kim loại bằng liều độc”

Không. Dạng tồn tại, khả năng sinh học và đường phơi nhiễm rất quan trọng.

### “Phát hiện bằng thiết bị nghĩa có rủi ro sức khỏe”

Không. Phát hiện chỉ nói tín hiệu vượt tiêu chí đo; risk cần thêm hazard và exposure.

## Mô hình tư duy

Hãy theo dõi chất ô nhiễm như **một dòng khối lượng đi qua nhiều trạng thái hóa học và ngăn sinh học**:

```text
nguồn
→ môi trường
→ phân bố pha / speciation
→ phơi nhiễm
→ hấp thu
→ chuyển hóa
→ mô đích
→ đáp ứng
```

Ở mỗi bước, hóa học có thể thay đổi dạng tồn tại và vì thế thay đổi tốc độ vận chuyển hoặc độc tính.

Xem tiếp: [Hóa học xanh](./04_green_chemistry.md).