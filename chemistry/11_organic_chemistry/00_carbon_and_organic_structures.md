# Carbon và cấu trúc hữu cơ — từ hóa trị carbon đến kiến trúc phân tử

> **Hóa học hữu cơ (organic chemistry / 유기화학)** không nên được hiểu đơn giản là “hóa học của các hợp chất chứa carbon”. Giá trị thực sự của lĩnh vực này nằm ở việc carbon có thể tạo ra những **đồ thị phân tử (molecular graphs)** cực kỳ đa dạng, trong khi phân bố electron, hình học và nhóm chức biến các đồ thị đó thành một cảnh quan phản ứng có logic.

## Vì sao carbon tạo được sự đa dạng đặc biệt

Carbon có bốn electron hóa trị và kích thước nguyên tử tương đối nhỏ. Điều này cho phép nó tạo liên kết σ C–C và C–H bền, đồng thời orbital 2p chồng phủ hiệu quả để tạo liên kết π ổn định.

Ba đặc điểm phối hợp tạo nên sự đa dạng của hóa hữu cơ:

1. **khả năng tạo mạch (catenation)** — carbon liên kết bền với chính carbon;
2. **khả năng tạo liên kết bội (multiple bonding)** — C=C, C≡C và các hệ liên hợp bền;
3. **khả năng liên kết với dị nguyên tử (heteroatom compatibility)** — carbon liên kết với H, O, N, S, P, halogen, kim loại và nhiều nguyên tố khác.

Silicon cũng thuộc nhóm 14 và thường hóa trị bốn, nhưng liên kết Si–Si yếu hơn, độ chồng phủ π giữa các orbital 3p kém hơn, còn liên kết Si–O rất mạnh. Vì vậy hóa học silicon thiên về silicate và mạng mở rộng hơn là tạo sự đa dạng khung carbon giống thế giới sinh học.

## Khung carbon như một đồ thị

Có thể xem một phân tử hữu cơ như một đồ thị:

```text
nguyên tử = nút
liên kết = cạnh
bậc liên kết / điện tích / lập thể = metadata
```

Công thức phân tử chỉ cho biết số lượng các nguyên tử, không xác định cách chúng nối với nhau.

Ví dụ \(C_4H_{10}\) có thể là n-butane hoặc isobutane. Cùng công thức nhưng kết nối khác nhau làm nhiệt độ sôi, cấu dạng và môi trường phản ứng khác nhau.

Đây là liên hệ trực tiếp với khoa học máy tính: hóa tin học (cheminformatics) biểu diễn phân tử bằng đồ thị để tìm kiếm, tạo fingerprint, so khớp cấu trúc con và huấn luyện mô hình máy học.

## Lai hóa là mô hình hình học, không phải một sự kiện vật lý riêng biệt

Môi trường cục bộ quanh carbon thường được mô tả bằng mô hình lai hóa:

| Mô hình | Hình học | Góc gần đúng | Mô-típ điển hình |
|---|---|---:|---|
| sp3 | tứ diện | 109.5° | carbon trong alkane |
| sp2 | tam giác phẳng | 120° | carbon trong alkene/carbonyl |
| sp | tuyến tính | 180° | carbon trong alkyne/nitrile |

Lai hóa (hybridization) là một cấu trúc toán học của mô hình liên kết hóa trị cục bộ. Nguyên tử không “thực hiện lai hóa” như một bước vật lý riêng trước khi tạo liên kết.

Mô hình orbital phân tử có thể mô tả cùng hệ bằng orbital phi định xứ mà không cần xem orbital lai hóa như những vật thể tồn tại độc lập.

## Thành phần s và hệ quả hóa học

Orbital sp có khoảng 50% đặc tính s, sp2 khoảng 33%, sp3 khoảng 25%. Mật độ electron trong orbital có nhiều đặc tính s hơn nằm trung bình gần hạt nhân hơn.

Điều này giúp giải thích vì sao liên kết C–H ở alkyne đầu mạch có tính acid cao hơn C–H ở alkene và alkane:

```text
sp C–H  >  sp2 C–H  >  sp3 C–H
(độ acid)
```

Base liên hợp trên carbon sp được ổn định hơn vì điện tích âm nằm trong orbital có mật độ gần hạt nhân hơn.

## Liên kết sigma và pi

**Liên kết σ (sigma bond / 시그마 결합)** hình thành từ chồng phủ trực diện dọc trục nối hai hạt nhân. **Liên kết π (pi bond / 파이 결합)** hình thành từ chồng phủ bên của hai orbital p song song.

C=C gồm một liên kết σ và một liên kết π. C≡C gồm một liên kết σ và hai liên kết π.

Tương tác π thường yếu hơn thành phần σ tương ứng và mật độ electron nằm lộ ra phía trên/dưới trục liên kết, nên các hệ π thường dễ bị tác nhân điện ly (electrophile) tấn công hơn.

Sự hạn chế quay của C=C cũng xuất phát từ yêu cầu giữ các orbital p song song. Quay 90° phá chồng phủ π và tốn năng lượng đáng kể.

## Biểu diễn — học đọc hình cấu trúc như đọc mã nguồn

Hóa hữu cơ dùng nhiều mức biểu diễn:

- công thức phân tử;
- công thức thu gọn;
- cấu trúc Lewis;
- công thức khung đường gấp khúc (skeletal/line-angle formula);
- biểu diễn lập thể nêm–gạch (wedge-dash);
- hình chiếu Newman;
- hình chiếu Fischer;
- cấu dạng ghế;
- sơ đồ orbital.

Không biểu diễn nào “chính là phân tử”. Mỗi biểu diễn chỉ giữ lại một tập thông tin phù hợp với câu hỏi đang xét.

Trong công thức khung, mỗi đỉnh hoặc đầu mút không ghi ký hiệu thường là carbon, còn hydrogen gắn với carbon được hiểu ngầm để thỏa hóa trị. Dị nguyên tử và hydrogen gắn với dị nguyên tử thường được viết rõ.

## Hóa trị và điện tích hình thức

Một số khuôn mẫu trung hòa thường gặp:

| Nguyên tử | Mẫu trung hòa phổ biến |
|---|---|
| C | 4 liên kết |
| N | 3 liên kết + 1 cặp electron tự do |
| O | 2 liên kết + 2 cặp electron tự do |
| halogen | 1 liên kết + 3 cặp electron tự do |

Tuy nhiên chất trung gian mang điện như carbocation, carbanion, oxonium, ammonium và gốc tự do không tuân hoàn toàn các mẫu này.

Điện tích hình thức:

\[
FC=V-N-\frac{B}{2}
\]

là công cụ ghi sổ electron, không phải điện tích riêng phần đo được trên nguyên tử.

## Cộng hưởng thay đổi khả năng phản ứng chứ không chỉ “vẽ thêm cấu trúc”

Nếu electron có thể phi định xứ trên nhiều nguyên tử mà không thay đổi cách các nguyên tử nối nhau, ta có thể vẽ nhiều **cấu trúc cộng hưởng (resonance contributors)**.

Cation allyl, cation benzyl, carboxylate, amide và enolate đều được ổn định nhờ phi định xứ electron.

Cộng hưởng ảnh hưởng:

- độ dài liên kết;
- độ acid/base;
- tính ái nhân và ái điện;
- hàng rào quay;
- phổ học;
- độ chọn lọc phản ứng.

Ví dụ liên kết C–N trong amide ngắn hơn liên kết đơn C–N thông thường vì cộng hưởng tạo một phần đặc tính liên kết đôi. Vì vậy liên kết peptide gần phẳng và bị hạn chế quay.

## Hiệu ứng cảm ứng và hiệu ứng cộng hưởng

Ảnh hưởng điện tử có thể truyền qua phân tử bằng nhiều con đường.

**Hiệu ứng cảm ứng (inductive effect / 유도 효과)** truyền sự phân cực qua liên kết σ và giảm nhanh theo khoảng cách. Nguyên tử hoặc nhóm có độ âm điện cao thường rút mật độ electron qua cảm ứng.

**Hiệu ứng cộng hưởng (resonance effect / 공명 효과)** cần hệ orbital liên hợp và có thể truyền hiệu ứng cho/nhận electron qua hệ π.

Một nhóm thế có thể vừa rút electron theo cảm ứng vừa cho electron theo cộng hưởng, như halogen trên vòng thơm. Vì vậy không nên gắn nhãn “nhóm đẩy electron” hoặc “nhóm hút electron” như một thuộc tính nhị phân tuyệt đối trong mọi tình huống.

## Liên hợp

**Liên hợp (conjugation / 공액)** xảy ra khi các orbital p kề nhau có thể chồng phủ liên tục, cho phép electron phi định xứ.

Ví dụ:

```text
C=C–C=C      diene liên hợp
C=C–C=O      enone
benzene      liên hợp vòng
amide        cặp electron tự do trên N liên hợp với C=O
```

Liên hợp thường làm hệ có năng lượng thấp hơn, thay đổi độ dài liên kết và giảm khoảng HOMO–LUMO. Đây là lý do các hệ liên hợp mở rộng hấp thụ ánh sáng ở bước sóng dài hơn và tạo màu trong thuốc nhuộm/chất màu.

## Siêu liên hợp

Mật độ electron từ liên kết σ C–H/C–C có thể tương tác với orbital trống hoặc orbital phản liên kết \(\pi^*\) lân cận. **Siêu liên hợp (hyperconjugation / 초공액)** góp phần ổn định carbocation, gốc tự do và alkene có mức thế cao hơn.

Đây là tương tác orbital thực, không chỉ là khẩu quyết “nhóm alkyl đẩy electron”.

## Cấu dạng — cùng kết nối nhưng khác năng lượng

Quay quanh liên kết σ tạo ra các **cấu dạng (conformers)**. Chúng thường chuyển đổi qua lại mà không cần phá liên kết.

Ở ethane, dạng so le có năng lượng thấp hơn dạng che khuất. Ở butane, dạng anti thấp năng lượng hơn dạng gauche vì hai nhóm methyl ở xa nhau hơn.

Chênh lệch năng lượng đến từ kết hợp của ứng suất xoắn, cản trở lập thể và hiệu ứng orbital; không nên quy toàn bộ cho việc “nguyên tử va vào nhau”.

## Cycloalkane và ứng suất vòng

**Ứng suất vòng (ring strain)** gồm nhiều đóng góp:

- ứng suất góc;
- ứng suất xoắn;
- tương tác xuyên vòng ở vòng lớn;
- ràng buộc cấu dạng.

Cyclopropane buộc góc C–C–C gần 60°, rất xa góc tứ diện lý tưởng. Cyclobutane giảm che khuất bằng cách uốn khỏi mặt phẳng nhưng vẫn còn ứng suất đáng kể.

Cyclohexane dạng ghế gần góc lý tưởng và có các liên kết gần so le nên đặc biệt bền.

## Cyclohexane dạng ghế — axial và equatorial

Mỗi carbon trong dạng ghế có một vị trí **trục (axial)** và một vị trí **xích đạo (equatorial)**. Lật vòng đổi axial ↔ equatorial nhưng giữ hướng lên/xuống của nhóm thế.

Nhóm thế lớn thường ưu tiên equatorial vì dạng axial chịu tương tác 1,3-diaxial.

Tư duy này quan trọng cho cơ chế phản ứng: nhiều phản ứng loại hoặc thế trong hệ vòng phụ thuộc việc orbital có thể sắp xếp đúng hướng hình học hay không.

## Tính chất vật lý xuất hiện từ cấu trúc

Tính chất vật lý của hợp chất hữu cơ không phải danh sách sự kiện rời rạc. Chúng xuất hiện từ tương tác phân tử.

Mạch hydrocarbon dài hơn thường có nhiệt độ sôi cao hơn vì diện tích tương tác phân tán London tăng. Phân nhánh thường làm giảm nhiệt độ sôi do giảm diện tích tiếp xúc hiệu dụng, nhưng nhiệt độ nóng chảy có thể có xu hướng khác vì đóng gói tinh thể.

Nhóm chức phân cực làm tăng tương tác lưỡng cực. Mẫu cho/nhận liên kết hydrogen ảnh hưởng độ tan và nhiệt độ sôi. Tính đối xứng đôi khi giúp đóng gói tinh thể tốt hơn và làm nhiệt độ nóng chảy tăng.

## Độ acid/base như bài toán độ bền

Thay vì học thuộc các giá trị \(pK_a\) rời rạc, hãy hỏi base hoặc acid liên hợp được ổn định như thế nào.

Các yếu tố chính gồm:

- độ âm điện;
- kích thước nguyên tử và khả năng phân cực;
- cộng hưởng;
- hiệu ứng cảm ứng;
- orbital/lai hóa;
- tính thơm;
- solvat hóa.

Một acid mạnh hơn khi base liên hợp của nó tương đối bền hơn.

## Góc nhìn orbital phân tử về khả năng phản ứng

Nhiều phản ứng hữu cơ có thể được hiểu bằng orbital biên (frontier orbitals):

- **tác nhân ái nhân (nucleophile)** cung cấp một orbital đã chiếm năng lượng tương đối cao, thường có tính HOMO;
- **tác nhân ái điện (electrophile)** cung cấp một orbital trống năng lượng tương đối thấp, thường có tính LUMO;
- phản ứng thuận lợi hơn khi năng lượng tương hợp và hình học chồng phủ phù hợp.

Ví dụ phản ứng \(S_N2\) có thể được nhìn như sự cho mật độ electron từ cặp electron tự do của nucleophile vào orbital phản liên kết \(\sigma^*\) C–LG.

## Xác định cấu trúc là bài toán ngược

Trong tổng hợp, ta đi từ cấu trúc → dự đoán tính chất và khả năng phản ứng. Trong hóa phân tích, ta giải bài toán ngược: dữ liệu phổ → các ràng buộc → cấu trúc hợp lý.

IR cho manh mối về nhóm chức, NMR cho môi trường hóa học và kết nối, MS cho khối lượng và mảnh vỡ, còn nhiễu xạ tia X có thể cho cấu trúc ba chiều trực tiếp hơn.

Vì vậy “biết vẽ cấu trúc” và “biết đọc bằng chứng” là hai mặt của cùng một kỹ năng.

## Những hiểu lầm thường gặp

### “Carbon đặc biệt chỉ vì có hóa trị 4”

Không. Hóa trị bốn + kích thước nhỏ + liên kết C–C bền + khả năng tạo liên kết π hiệu quả mới tạo nên sự đa dạng lớn.

### “Lai hóa là trạng thái vật lý đo trực tiếp được”

Không. Nó là mô hình hữu ích cho liên kết cục bộ và hình học.

### “Liên kết đơn luôn quay tự do”

Không. Quay có hàng rào năng lượng và có thể bị hạn chế mạnh bởi vòng, cản trở lập thể hoặc cộng hưởng như trong amide.

### “Các cấu trúc cộng hưởng là những tiểu phân thay nhau tồn tại”

Không. Chúng là các cách biểu diễn của một trạng thái electron phi định xứ duy nhất.

## Mô hình tư duy

Hãy xem phân tử hữu cơ là **đồ thị carbon + hình học 3D + trường mật độ electron**. Kết nối trả lời “nguyên tử nào nối với nguyên tử nào”; hình học trả lời “chúng nằm ở đâu”; phân bố electron trả lời “vị trí nào có xu hướng cho hoặc nhận electron”; cảnh quan năng lượng quyết định con đường phản ứng nào có thể xảy ra.

Xem tiếp: [Nhóm chức](./01_functional_groups.md).