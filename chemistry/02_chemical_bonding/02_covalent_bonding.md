# Liên kết cộng hóa trị — tổ chức mật độ electron giữa nhiều hạt nhân

> **Liên kết cộng hóa trị (covalent bond / 공유 결합)** là kiểu liên kết trong đó mật độ electron được chia sẻ hoặc phi định xứ giữa hai hay nhiều hạt nhân, và cách tổ chức electron này làm tổng năng lượng của hệ giảm xuống so với các mảnh tách rời.

Cụm “hai nguyên tử dùng chung một cặp electron” là cách biểu diễn rất hữu ích trong lý thuyết Lewis, nhưng electron thật không ngồi giữa hai nguyên tử như hai người cùng giữ một vật. Liên kết là một **trạng thái lượng tử của mật độ electron** trong trường của nhiều hạt nhân.

## Phân tử hydrogen — ví dụ tối giản

Hai nguyên tử hydrogen riêng lẻ, mỗi nguyên tử có một electron `1s`. Khi đưa hai nguyên tử lại gần, các orbital nguyên tử chồng phủ lên nhau.

Một tổ hợp làm mật độ electron tăng trong vùng giữa hai hạt nhân có thể giảm năng lượng vì mỗi electron bị hút bởi cả hai proton và giúp che bớt lực đẩy hạt nhân–hạt nhân.

Nhưng nếu hai proton tiến quá gần, lực đẩy Coulomb giữa các hạt nhân và lực đẩy lượng tử do chồng lấn electron tăng mạnh.

Do đó năng lượng theo khoảng cách có một cực tiểu:

```text
xa nhau      → tương tác nhỏ
lại gần      → năng lượng giảm
đúng khoảng  → cực tiểu năng lượng
quá gần      → năng lượng tăng rất mạnh
```

Khoảng cách tại cực tiểu chính là **độ dài liên kết cân bằng**.

## Tại sao mật độ electron giữa hai hạt nhân tạo liên kết?

Nếu electron tập trung giữa hai hạt nhân, lực hút electron–hạt nhân tác dụng theo hướng giữ hai hạt nhân lại gần nhau.

Có thể hình dung electron density ở giữa như một “vùng keo lượng tử”, nhưng phải nhớ đây chỉ là trực giác. Bản chất chính xác đến từ nghiệm của Hamiltonian nhiều hạt.

## Mô hình cặp electron Lewis

**Cấu trúc Lewis (Lewis structure / 루이스 구조)** mô tả electron hóa trị bằng chấm và liên kết bằng các cặp electron dùng chung.

Ví dụ hydrogen:

```text
H:H   hoặc   H—H
```

Mô hình Lewis rất mạnh trong việc theo dõi:

- tổng electron hóa trị;
- connectivity;
- điện tích hình thức;
- octet;
- cộng hưởng.

Nhưng nó không trực tiếp mô tả:

- hình dạng orbital;
- năng lượng orbital;
- spin coupling;
- mật độ xác suất liên tục;
- phi định xứ thực sự.

Vì vậy Lewis là mô hình bookkeeping rất tốt, không phải bản đồ mật độ electron thực.

## Liên kết đơn, đôi và ba

Trong biểu diễn Lewis, liên kết đơn thường tương ứng với một cặp electron dùng chung; liên kết đôi có hai cặp; liên kết ba có ba cặp.

Trong nhiều họ gồm cùng loại nguyên tử, khi **bậc liên kết (bond order)** tăng thì độ dài liên kết thường giảm và độ bền thường tăng.

Ví dụ giữa hai carbon:

```text
độ dài: C–C > C=C > C≡C
độ bền: C≡C > C=C > C–C
```

Nhưng không nên hiểu “liên kết đôi mạnh gấp đôi liên kết đơn”. Năng lượng không tăng tuyến tính vì thành phần sigma và pi có bản chất chồng phủ khác nhau.

## Liên kết sigma và pi

Trong ngôn ngữ của lý thuyết liên kết hóa trị:

- **liên kết sigma (σ bond / 시그마 결합)** hình thành từ chồng phủ trực diện theo trục liên hạt nhân;
- **liên kết pi (π bond / 파이 결합)** hình thành từ chồng phủ bên của orbital có orientation phù hợp.

Một liên kết đôi thường gồm:

\[
1\sigma+1\pi
\]

Liên kết ba thường gồm:

\[
1\sigma+2\pi
\]

Liên kết π hạn chế quay vì xoay quanh trục làm hai orbital p mất sự song song tối ưu.

Đây là nền tảng hình học của:

- đồng phân cis/trans;
- đồng phân E/Z;
- độ phẳng của alkene;
- conjugation.

## Liên kết cộng hóa trị và obitan phân tử

Trong **lý thuyết obitan phân tử (molecular orbital theory)**, hai atomic orbitals có thể tổ hợp thành:

- orbital liên kết;
- orbital phản liên kết.

Ví dụ đơn giản:

\[
1s_A+1s_B\rightarrow\sigma_{1s}
\]

và:

\[
1s_A-1s_B\rightarrow\sigma_{1s}^*
\]

Orbital liên kết có mật độ electron tăng giữa các hạt nhân.

Orbital phản liên kết có node giữa hai hạt nhân và electron ở đó làm liên kết yếu đi.

Điều này giúp giải thích sâu hơn vì sao không phải chỉ “có electron” là tạo liên kết; **electron nằm ở orbital nào** mới quyết định hiệu ứng liên kết.

## Bậc liên kết trong MO

Một định nghĩa hữu ích:

\[
BO=\frac{N_{bonding}-N_{antibonding}}{2}
\]

Nếu electron đi vào orbital phản liên kết, bond order giảm.

Ví dụ này quan trọng khi giải thích:

- ion hóa phân tử;
- trạng thái kích thích;
- quang hóa;
- phản ứng làm yếu liên kết.

## HOMO và LUMO

Trong phân tử, **HOMO** là orbital phân tử bị chiếm có năng lượng cao nhất; **LUMO** là orbital chưa chiếm có năng lượng thấp nhất.

Nhiều phản ứng có thể hiểu bằng tương tác giữa:

```text
HOMO của nucleophile
↔
LUMO của electrophile
```

Đây là cách nối liên kết cộng hóa trị với lý thuyết orbital biên (**frontier molecular orbital theory**).

Nếu hai orbital có:

- năng lượng tương thích;
- đối xứng phù hợp;
- overlap tốt;

thì tương tác có thể mạnh hơn.

## Độ phân cực của liên kết

Trong liên kết H–H hoặc Cl–Cl, khả năng hút electron của hai hạt nhân gần như giống nhau nên mật độ electron tương đối đối xứng.

Trong H–Cl, chlorine có độ âm điện lớn hơn nên mật độ electron lệch về phía Cl:

```text
Hδ+ — Clδ−
```

Liên kết vẫn là cộng hóa trị nhưng có phân cực.

Chênh lệch độ âm điện giúp dự đoán xu hướng, nhưng không có một ngưỡng tuyệt đối biến liên kết từ “cộng hóa trị” thành “ion”. Hai mô hình nằm trên một phổ liên tục.

## Độ âm điện không phải đại lượng độc lập với môi trường

Giá trị độ âm điện trong bảng là mô hình hữu ích, nhưng khả năng hút electron thực tế phụ thuộc:

- trạng thái oxy hóa;
- hybridization;
- môi trường phối trí;
- điện tích tổng;
- nhóm thế xung quanh.

Do đó không nên suy mọi phân bố electron chỉ từ một bảng độ âm điện.

## Mômen lưỡng cực

Độ phân cực có thể được biểu diễn bằng **mômen lưỡng cực (dipole moment / 쌍극자 모멘트)**:

\[
\mu=qr
\]

Trong mô hình đơn giản, `q` là độ lớn phân tách điện tích và `r` là khoảng cách.

Mômen lưỡng cực phân tử là tổng vector của:

- dipole liên kết;
- ảnh hưởng lone pair;
- hình học toàn phân tử.

`CO2` có hai liên kết C=O phân cực nhưng phân tử không phân cực vì hai vector triệt tiêu trong cấu trúc tuyến tính.

Do đó:

```text
độ phân cực liên kết ≠ độ phân cực phân tử
```

## Khả năng phân cực

**Khả năng phân cực (polarizability)** mô tả mức độ đám mây electron dễ bị biến dạng bởi điện trường hoặc species lân cận.

Nguyên tử lớn, electron ngoài xa nucleus và đám mây electron mềm thường dễ phân cực hơn.

Polarizability ảnh hưởng:

- lực London;
- refractive index;
- tương tác ion–induced dipole;
- mức cộng hóa trị trong chất ion;
- tính chất quang học.

Đây là cầu nối giữa covalent bonding và intermolecular forces.

## Năng lượng phân ly liên kết và năng lượng liên kết trung bình

**Năng lượng phân ly liên kết (bond dissociation energy, BDE)** là enthalpy cần để phá một liên kết cụ thể theo cơ chế đồng ly trong một phân tử xác định, thường ở pha khí.

Ví dụ:

\[
R-H\rightarrow R^\bullet+H^\bullet
\]

BDE phụ thuộc mạnh vào stability của radical tạo ra.

Trong khi đó **năng lượng liên kết trung bình (average bond enthalpy)** là giá trị trung bình từ nhiều phân tử khác nhau.

Hai khái niệm không nên dùng thay nhau khi cần độ chính xác cơ chế.

## Năng lượng liên kết và năng lượng phản ứng

Có thể ước lượng:

\[
\Delta H_{rxn}\approx\sum D(\text{liên kết bị phá})-\sum D(\text{liên kết được tạo})
\]

Đây là xấp xỉ vì bảng thường dùng bond enthalpy trung bình và môi trường pha khí.

Công thức giúp sửa một hiểu lầm phổ biến:

> phá liên kết **cần năng lượng**; phản ứng tỏa nhiệt khi các liên kết mới hình thành giải phóng nhiều năng lượng hơn lượng cần để phá liên kết cũ.

## Phá liên kết đồng ly và dị ly

Một liên kết A–B có thể phá theo hai kiểu.

**Đồng ly (homolysis)**:

\[
A-B\rightarrow A^\bullet+B^\bullet
\]

Mỗi mảnh nhận một electron.

**Dị ly (heterolysis)**:

\[
A-B\rightarrow A^++B^-
\]

hoặc ngược lại tùy phân cực.

Môi trường dung môi ảnh hưởng rất mạnh đến heterolysis vì ion cần được solvate.

Khác biệt này rất quan trọng trong hóa hữu cơ và cơ chế phản ứng.

## Liên kết cho–nhận

Trong **liên kết cho–nhận (coordinate covalent bond / 배위 공유 결합)**, cả hai electron của cặp liên kết ban đầu đến từ cùng một nguyên tử theo bookkeeping Lewis.

Ví dụ:

\[
NH_3+H^+\rightarrow NH_4^+
\]

Cặp electron không liên kết trên nitrogen tạo liên kết với proton.

Sau khi liên kết hình thành, không tồn tại “một loại liên kết vật lý riêng” chỉ vì nguồn gốc ban đầu của electron khác nhau.

Điều này nối Lewis acid–base với coordination chemistry.

## Cộng hưởng và phi định xứ

Một cấu trúc Lewis đôi khi không đủ.

Ion carbonate `CO3²⁻` có nhiều resonance contributors hợp lệ.

Các hình này không phải phân tử nhảy qua lại giữa nhiều cấu trúc. Trạng thái thật có electron phi định xứ trên nhiều bond.

Kết quả là ba liên kết C–O có độ dài gần nhau thay vì một đôi và hai đơn hoàn toàn tách biệt.

## Năng lượng cộng hưởng

Trạng thái phi định xứ thường có năng lượng thấp hơn bất kỳ cấu trúc localized đơn lẻ tương ứng.

Sự hạ năng lượng đó thường được gọi định tính là **ổn định cộng hưởng (resonance stabilization)**.

Nó quan trọng trong:

- carboxylate;
- benzene;
- amide;
- allyl system;
- aromatic ion.

## Conjugation

Nếu nhiều orbital p liên tiếp có thể overlap:

```text
p–p–p–p...
```

electron π có thể phi định xứ trên nhiều nguyên tử.

Conjugation làm thay đổi:

- bond length;
- màu sắc;
- HOMO–LUMO gap;
- reactivity;
- stability.

Đây là lý do polyene dài hấp thụ ánh sáng ở wavelength dài hơn.

## Hyperconjugation

**Siêu liên hợp (hyperconjugation)** là tương tác giữa orbital sigma, thường C–H/C–C, với orbital p hoặc π lân cận.

Nó góp phần giải thích:

- stability của carbocation;
- stability của alkene thay thế;
- conformational preferences.

Không nên mô tả mọi xu hướng này chỉ bằng “inductive effect”.

## Liên kết đa tâm

Không phải mọi liên kết cộng hóa trị đều phù hợp mô hình “hai tâm–hai electron”.

Một số phân tử electron-deficient như diborane có **liên kết ba tâm hai electron (3-center–2-electron bond)**.

Điều này cho thấy octet/Lewis là mô hình rất mạnh nhưng không phải quy luật tuyệt đối của mọi compound.

## Hypervalency

Các phân tử như `PF5`, `SF6` thường được dạy bằng “mở rộng octet bằng orbital d”. Cách giải thích đó quá đơn giản và trong nhiều trường hợp không còn được xem là mô hình tốt.

Mô tả hiện đại thường nhấn mạnh:

- liên kết phân cực;
- delocalization;
- 3-center–4-electron bonding;
- molecular orbitals.

Điều quan trọng là không gắn một hình hybridization đơn giản như lời giải vật lý tuyệt đối.

## Liên kết cộng hóa trị trong chất rắn

Không phải mọi chất cộng hóa trị tồn tại dưới dạng phân tử nhỏ.

Kim cương là **chất rắn mạng cộng hóa trị (covalent network solid)**: mỗi carbon liên kết trong mạng ba chiều.

Silicon, SiC, SiO2 và BN cũng có các dạng mạng mở rộng.

Tính chất của mạng phụ thuộc:

- connectivity;
- dimensionality;
- band structure;
- defect;
- topology.

## Cùng nguyên tố, topology khác, tính chất khác

Carbon tạo:

- kim cương;
- graphite;
- graphene;
- fullerene;
- nanotube.

Composition đều là carbon, nhưng cách orbital và topology liên kết khác nhau làm tính chất điện, cơ và quang khác rất mạnh.

Đây là ví dụ rõ ràng rằng:

```text
thành phần hóa học không đủ
→ phải biết cấu trúc liên kết
```

## Liên kết và trạng thái kích thích

Khi phân tử hấp thụ photon, electron có thể chuyển từ orbital liên kết sang orbital phản liên kết.

Nếu bond order giảm đáng kể, liên kết có thể yếu đi hoặc đứt.

Đây là nền tảng của:

- photodissociation;
- quang hóa;
- cis–trans photoisomerization;
- photopolymerization.

Vì vậy bonding không chỉ quyết định cấu trúc ground state mà còn quyết định phản ứng ở excited state.

## Liên kết và spectroscopy

Các vibration stretching/bending phụ thuộc bond stiffness và reduced mass.

Gần đúng oscillator điều hòa:

\[
\nu\propto\sqrt{\frac{k}{\mu}}
\]

Liên kết mạnh hơn thường có force constant lớn hơn và vibration frequency cao hơn, nhưng conjugation, hydrogen bonding và môi trường làm peak dịch chuyển.

Đây là cách spectroscopy “nhìn thấy” bonding gián tiếp.

## Các hiểu lầm thường gặp

### “Liên kết cộng hóa trị nghĩa là electron được chia đều”

Không. Mật độ electron có thể lệch mạnh nếu hai nguyên tử khác nhau về độ âm điện.

### “Liên kết đôi mạnh gấp đôi liên kết đơn”

Không. Một double bond gồm sigma + pi và đóng góp năng lượng không tuyến tính.

### “Cấu trúc cộng hưởng là các cấu trúc phân tử nhảy qua lại”

Không. Chúng là nhiều cách biểu diễn cùng một trạng thái electron phi định xứ.

### “Mọi liên kết đều là hai tâm–hai electron”

Không. Có multicenter bonding và các hệ phi định xứ rộng hơn.

### “Hybridization là hình ảnh lượng tử duy nhất đúng”

Không. Hybridization là mô hình localized bonding hữu ích; MO theory có thể cho mô tả khác nhưng tương thích về dự đoán.

### “Phá liên kết giải phóng năng lượng”

Không. Phá bond cần năng lượng; quá trình tổng có thể tỏa nhiệt vì bond mới hình thành bù nhiều hơn.

## Mô hình tư duy

Liên kết cộng hóa trị là **cách hệ tổ chức mật độ electron để hạ năng lượng trong trường của nhiều hạt nhân**. Lewis giúp hạch toán electron; valence-bond theory giúp mô tả overlap và liên kết cục bộ; molecular-orbital theory mô tả delocalization và orbital phản liên kết. Không mô hình nào cần được xem là “hình ảnh duy nhất của thực tại”; mỗi mô hình trả lời một lớp câu hỏi khác nhau.

Xem tiếp: [Cấu trúc Lewis và cộng hưởng](./03_lewis_structures_and_resonance.md).