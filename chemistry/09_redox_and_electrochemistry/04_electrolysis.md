# Điện phân — dùng công điện để thúc đẩy biến đổi hóa học

> **Điện phân (electrolysis / 전기분해)** sử dụng công điện từ nguồn bên ngoài để thúc đẩy phản ứng oxy hóa–khử theo chiều không tự phát trong điều kiện đang xét. Nếu pin Galvani chuyển năng lượng tự do hóa học thành công điện, thì bình điện phân làm chiều ngược lại: dùng điện năng để thay đổi thành phần hóa học.

Điện phân là nền cho mạ điện, tinh luyện và điều chế kim loại, sản xuất chlorine–kiềm, tạo hydrogen, điện khử `CO2`, sạc pin và nhiều công nghệ chuyển đổi năng lượng. Muốn hiểu một hệ điện phân thực, cần nối đồng thời nhiệt động lực học, động học điện cực, vận chuyển khối, vật liệu và an toàn.

## Pin Galvani và bình điện phân

Trong cả hai hệ:

```text
anode   = nơi xảy ra oxy hóa
cathode = nơi xảy ra khử
```

Điểm khác nằm ở chiều tự phát của phản ứng tổng.

Trong pin Galvani:

```text
ΔG < 0 theo chiều vận hành
phản ứng hóa học → công điện
```

Trong bình điện phân:

```text
ΔG > 0 cho chiều mong muốn nếu không cấp công ngoài
công điện → biến đổi hóa học
```

Nguồn điện ngoài tạo một chênh lệch thế đủ lớn để đẩy electron theo chiều cần thiết.

## Dấu điện cực

Trong một bình điện phân điển hình, nguồn điện kéo electron khỏi anode và cung cấp electron cho cathode.

Do đó thường có:

```text
anode   → nối phía dương của nguồn
cathode → nối phía âm của nguồn
```

Tuy nhiên dấu điện cực không phải định nghĩa nền. Cách nhớ chắc chắn hơn là:

```text
anode   → oxy hóa
cathode → khử
```

Quy tắc này vẫn đúng khi chuyển giữa pin Galvani, bình điện phân và các hệ điện hóa khác.

## Điện lượng là số electron đã được truyền

Nếu dòng điện \(I\) chạy trong thời gian \(t\):

\[
Q=It
\]

với:

\[
1\,A=1\,C/s
\]

Số mol electron được truyền là:

\[
n_{e^-}=\frac{Q}{F}
\]

trong đó:

\[
F\approx96485\,C/mol\,e^-
\]

là **hằng số Faraday (Faraday constant)**.

Chuỗi suy luận là:

```text
dòng điện × thời gian
→ điện lượng
→ mol electron
→ mol chất theo hệ số phản ứng
```

Điện phân vì vậy có thể được nhìn như một phép **đếm electron bằng điện lượng**.

## Định luật Faraday của điện phân

Với bán phản ứng:

\[
M^{z+}+ze^-\rightarrow M
\]

số mol kim loại lý tưởng được tạo là:

\[
n_M=\frac{Q}{zF}
\]

Khối lượng tương ứng:

\[
m_M=\frac{QM_M}{zF}
\]

trong đó \(M_M\) là khối lượng mol của kim loại.

Công thức này chỉ cho lượng lý tưởng khi toàn bộ điện lượng đi vào đúng phản ứng mong muốn.

## Ví dụ: mạ đồng

Tại cathode:

\[
Cu^{2+}+2e^-\rightarrow Cu
\]

Nếu dòng `2.00 A` chạy trong `30.0 phút`:

\[
Q=(2.00)(30.0\times60)=3600\,C
\]

Số mol electron:

\[
n_e=\frac{3600}{96485}\approx0.0373\,mol
\]

Số mol Cu lý tưởng:

\[
n_{Cu}=\frac{0.0373}{2}\approx0.0187\,mol
\]

Khối lượng Cu lý tưởng:

\[
m\approx0.0187\times63.55\approx1.19\,g
\]

Nếu thí nghiệm chỉ thu được `1.07 g`, phần chênh lệch có thể đến từ phản ứng phụ, thất thoát vật liệu hoặc sai số đo.

## Hiệu suất Faraday

**Hiệu suất Faraday (Faradaic efficiency, FE)** đo phần điện lượng thực sự tạo sản phẩm mong muốn:

\[
FE=\frac{Q_{sản\ phẩm\ mong\ muốn}}{Q_{tổng}}
\]

Hoặc nếu biết lượng sản phẩm:

\[
FE=\frac{n_{sản\ phẩm}zF}{Q_{tổng}}
\]

khi hệ số electron `z` đã được xác định rõ.

Nếu nhiều sản phẩm cùng hình thành, tổng FE của tất cả con đường Faraday có thể gần 100% khi mọi sản phẩm đều được định lượng đầy đủ.

FE thấp thường cho thấy điện lượng bị tiêu thụ bởi phản ứng phụ hoặc cân bằng vật chất chưa được theo dõi đầy đủ.

## Hiệu suất năng lượng khác hiệu suất Faraday

Một hệ có FE gần 100% vẫn có thể tiêu tốn nhiều điện năng nếu điện áp vận hành cao.

Năng lượng điện cung cấp:

\[
W_{elec}=\int VI\,dt
\]

Nếu điện áp gần như không đổi:

\[
W_{elec}\approx VIt
\]

**Hiệu suất năng lượng (energy efficiency)** so sánh năng lượng hóa học hữu ích được lưu trong sản phẩm với điện năng đầu vào.

Do đó:

```text
hiệu suất Faraday → electron đi vào sản phẩm nào?
hiệu suất năng lượng → phải trả bao nhiêu điện năng cho sản phẩm đó?
```

Hai đại lượng trả lời hai câu hỏi khác nhau.

## Điện áp thuận nghịch và điện áp thực

Nhiệt động lực học cho điện áp thuận nghịch tối thiểu tương ứng với biến thiên Gibbs:

\[
\Delta G=nFE_{rev}
\]

cho chiều điện phân theo quy ước phù hợp.

Nhưng một cell thực phải vượt thêm nhiều tổn thất. Có thể viết khái niệm:

\[
V_{cell}
=E_{rev}
+\eta_{anode}
+\eta_{cathode}
+IR
+\eta_{transport}
\]

Các phần bổ sung gồm:

- quá thế hoạt hóa;
- tổn thất điện trở;
- phân cực nồng độ;
- tổn thất do bọt khí, tiếp xúc hoặc hình học thiết bị.

Vì vậy điện năng tiêu thụ thực tế luôn lớn hơn giới hạn thuận nghịch nếu cùng trạng thái đầu và cuối.

## Quá thế và động học điện cực

Tại điện thế cân bằng, dòng Faraday ròng bằng 0. Muốn tạo mật độ dòng hữu ích, điện thế điện cực phải lệch khỏi giá trị cân bằng.

Độ lệch đó gọi là **quá thế (overpotential, \(\eta\))**.

Phương trình Butler–Volmer mô tả gần đúng quan hệ giữa mật độ dòng và quá thế:

\[
j=j_0\left[
\exp\left(\frac{\alpha nF\eta}{RT}\right)
-
\exp\left(-\frac{(1-\alpha)nF\eta}{RT}\right)
\right]
\]

Trong đó \(j_0\) là **mật độ dòng trao đổi (exchange current density)**.

Một chất xúc tác điện hóa tốt thường làm tăng \(j_0\) hoặc giảm quá thế cần thiết để đạt một mật độ dòng xác định.

## Phản ứng cạnh tranh tại điện cực

Trong dung dịch nước, một ion không mặc nhiên được phóng điện chỉ vì mang điện tích.

Tại cathode có thể đồng thời cạnh tranh:

- khử ion kim loại;
- tạo `H2` từ proton hoặc nước;
- khử dung môi;
- khử các tiểu phần khác.

Tại anode có thể cạnh tranh:

- oxy hóa anion;
- tạo `O2` từ nước;
- oxy hóa điện cực;
- oxy hóa dung môi.

Sản phẩm thực phụ thuộc đồng thời vào:

```text
thế nhiệt động
+ quá thế
+ nồng độ / hoạt độ
+ vật liệu điện cực
+ vận chuyển khối
+ trạng thái bề mặt
```

Vì vậy quy tắc “cation về cathode, anion về anode” không đủ để dự đoán sản phẩm.

## Điện phân NaCl nóng chảy

NaCl nóng chảy chứa chủ yếu các ion `Na+` và `Cl−`.

Tại cathode:

\[
Na^++e^-\rightarrow Na
\]

Tại anode:

\[
2Cl^-\rightarrow Cl_2+2e^-
\]

Do không có nước, không xuất hiện cạnh tranh tạo hydrogen hoặc oxygen từ nước.

Đây là cơ sở của quá trình Downs để sản xuất sodium kim loại.

## Vì sao không thể sản xuất sodium bằng NaCl nước?

Trong dung dịch nước, khử nước hoặc proton để tạo hydrogen thuận lợi hơn việc tạo sodium kim loại trong điều kiện thông thường.

Ngay cả nếu một lượng Na được tạo thành, nó cũng phản ứng rất mạnh với nước.

Do đó sản xuất sodium cần **chất điện ly không nước**, thường là muối nóng chảy.

Đây là ví dụ rõ cho việc **hóa học dung môi (solvent chemistry)** quyết định sản phẩm điện phân.

## Quá trình chlorine–kiềm

Trong điện phân dung dịch NaCl công nghiệp:

Tại anode:

\[
2Cl^-\rightarrow Cl_2+2e^-
\]

Tại cathode:

\[
2H_2O+2e^-\rightarrow H_2+2OH^-
\]

Sản phẩm chính là:

```text
Cl2
H2
NaOH trong dung dịch
```

Màng chọn lọc ion giúp tách sản phẩm và hạn chế chlorine phản ứng với hydroxide.

Quá trình này cho thấy vận chuyển ion qua màng quan trọng không kém phản ứng điện cực.

## Điện phân nước

Phản ứng tổng:

\[
2H_2O\rightarrow2H_2+O_2
\]

Ở khoảng `25 °C` trong điều kiện chuẩn phù hợp, điện áp thuận nghịch gần:

\[
1.23\,V
\]

Thiết bị thực phải dùng điện áp cao hơn vì động học của **phản ứng tạo hydrogen (hydrogen evolution reaction, HER)** và đặc biệt **phản ứng tạo oxygen (oxygen evolution reaction, OER)**, cộng thêm tổn thất điện trở và vận chuyển khối.

## Phản ứng tạo hydrogen

Trong môi trường acid, phương trình tổng có thể viết:

\[
2H^++2e^-\rightarrow H_2
\]

Trong môi trường base, nước thường là nguồn proton trực tiếp.

Cơ chế có thể gồm các trung gian hydrogen hấp phụ và các bước Volmer, Tafel hoặc Heyrovsky tùy vật liệu xúc tác và môi trường.

Platinum có hoạt tính HER rất cao trong nhiều điều kiện, nhưng chi phí lớn thúc đẩy nghiên cứu các chất xúc tác thay thế.

## Phản ứng tạo oxygen

Trong acid, có thể viết:

\[
2H_2O\rightarrow O_2+4H^++4e^-
\]

OER là phản ứng nhiều electron–proton và phải hình thành liên kết O–O. Nó thường có quá thế lớn hơn HER và trở thành nút thắt động học của điện phân nước.

Các oxide dựa trên Ni/Fe, `IrO2`, `RuO2` và nhiều hệ khác được sử dụng hoặc nghiên cứu tùy pH, nhiệt độ và loại điện phân.

## Tách khí là yêu cầu an toàn

Hydrogen và oxygen có thể tạo hỗn hợp dễ cháy hoặc nổ.

Thiết bị điện phân phải kiểm soát:

- màng hoặc separator;
- chênh lệch áp suất;
- độ tinh khiết khí;
- sự xuyên khí giữa hai ngăn.

Do đó hiệu suất điện hóa không thể tách khỏi thiết kế an toàn.

## Điện phân kiềm, PEM và oxide rắn

Các công nghệ điện phân nước khác nhau sử dụng chất điện ly và vật liệu khác nhau.

**Điện phân kiềm (alkaline electrolysis)** dùng môi trường kiềm, cho phép dùng nhiều vật liệu tương đối rẻ.

**Điện phân PEM (proton-exchange membrane electrolysis)** dùng màng trao đổi proton, đạt mật độ dòng cao nhưng thường cần vật liệu quý bền trong môi trường acid ở anode.

**Điện phân oxide rắn (solid-oxide electrolysis)** hoạt động ở nhiệt độ cao với chất dẫn ion ceramic và có thể sử dụng một phần năng lượng dưới dạng nhiệt.

Không có công nghệ tốt nhất cho mọi mục tiêu. Các đánh đổi gồm:

- hiệu suất;
- chi phí vốn;
- tuổi thọ vật liệu;
- mật độ dòng;
- điều kiện nhiệt độ và áp suất;
- nguồn nhiệt và nguồn điện sẵn có.

## Điện áp nhiệt trung hòa

Với phản ứng tách nước:

\[
\Delta H=\Delta G+T\Delta S
\]

**Điện áp nhiệt trung hòa (thermoneutral voltage)** được định nghĩa:

\[
E_{th}=\frac{\Delta H}{nF}
\]

Ở nhiệt độ phòng, giá trị này lớn hơn điện áp thuận nghịch dựa trên `ΔG`.

Nếu cell vận hành dưới điện áp nhiệt trung hòa, nó phải hấp thụ một phần nhiệt từ môi trường để cân bằng năng lượng. Nếu vận hành cao hơn, phần điện năng dư có xu hướng chuyển thành nhiệt.

Khái niệm này rất quan trọng khi thiết kế quản lý nhiệt cho máy điện phân.

## Mạ điện

Vật cần phủ kim loại thường đóng vai trò cathode:

\[
M^{z+}+ze^-\rightarrow M(s)
\]

Nhưng chất lượng lớp mạ không chỉ phụ thuộc tổng điện lượng. Nó còn phụ thuộc:

- mật độ dòng;
- tốc độ tạo mầm;
- chuẩn bị bề mặt;
- chất phụ gia và chất tạo phức;
- pH;
- nhiệt độ;
- khuấy trộn;
- hình học điện cực và khả năng phân bố lớp mạ.

Nếu mật độ dòng quá cao, vận chuyển ion không theo kịp và lớp mạ có thể thô, xốp hoặc dạng nhánh.

## Tạo mầm trong kết tủa điện hóa

Kim loại mới không nhất thiết phủ đều thành một lớp nguyên tử ngay từ đầu. Nó có thể tạo các đảo nhỏ, sau đó các đảo lớn dần và hợp nhất.

Năng lượng bề mặt và quá thế ảnh hưởng mật độ mầm và kích thước hạt.

Đây là điểm nối giữa electrochemistry, lý thuyết tạo mầm và khoa học vật liệu.

## Điện tinh luyện

Trong **điện tinh luyện (electrorefining)** đồng, anode đồng thô hòa tan:

\[
Cu\rightarrow Cu^{2+}+2e^-
\]

Ion `Cu²+` được tái kết tủa thành đồng tinh khiết tại cathode.

Tạp chất có hành vi khác nhau tùy thế redox và độ tan; một số tích tụ thành bùn anode.

Quá trình khai thác độ chọn lọc điện hóa để tinh chế kim loại ở quy mô công nghiệp.

## Điện thắng kim loại

**Điện thắng (electrowinning)** thu kim loại từ dung dịch chứa ion kim loại, thường sau bước hòa tách quặng.

Khác với điện tinh luyện, anode không nhất thiết là chính kim loại mục tiêu ở dạng thô.

Điện thắng Cu, Zn và nhiều kim loại khác là cầu nối giữa luyện kim và electrochemistry.

## Điện phân nhôm Hall–Héroult

Ion `Al³+` rất khó khử trong dung dịch nước. Công nghiệp hòa tan alumina trong cryolite nóng chảy rồi điện phân ở nhiệt độ cao.

Tại cathode tạo nhôm lỏng. Anode carbon tham gia phản ứng với các tiểu phần oxygen và dần bị tiêu hao thành `CO2` hoặc `CO`.

Sản xuất nhôm nguyên sinh vì vậy tiêu tốn nhiều điện năng. Tái chế nhôm tiết kiệm năng lượng đáng kể vì tránh phải lặp lại bước khử điện hóa từ oxide.

## Điện khử CO₂

`CO2` có thể được điện hóa thành CO, formate, ethylene, alcohol và các sản phẩm khác tùy chất xúc tác.

Thách thức gồm:

- nhiều con đường phản ứng cạnh tranh;
- HER cạnh tranh;
- độ chọn lọc sản phẩm;
- vận chuyển `CO2` tới bề mặt;
- tạo carbonate;
- hiệu suất năng lượng;
- tách sản phẩm.

Hiệu suất Faraday cao chưa đủ để kết luận quy trình hiệu quả. Còn phải xem điện áp cell, tỷ lệ carbon thực sự đi vào sản phẩm và chi phí tách.

## Điện tổng hợp hữu cơ

Điện cực có thể thay một phần chất oxy hóa hoặc chất khử stoichiometric bằng electron từ mạch điện.

Điều này có tiềm năng giảm chất thải, nhưng vẫn phải đánh giá:

- dung môi và chất điện ly;
- vật liệu điện cực;
- độ chọn lọc;
- nguồn điện;
- xử lý và tách sản phẩm phía sau.

Nói “electron là thuốc thử sạch” chỉ có ý nghĩa khi đánh giá toàn bộ vòng đời và vật liệu phụ trợ.

## Khi vận chuyển khối trở thành giới hạn

Nếu bề mặt điện cực tiêu thụ chất phản ứng nhanh hơn tốc độ chất đó được đưa tới bề mặt:

\[
C_{surface}<C_{bulk}
\]

một lớp khuếch tán hình thành.

Dòng giới hạn gần đúng tỷ lệ với:

\[
i_{lim}\propto nFAD\frac{C_{bulk}}{\delta}
\]

trong đó \(\delta\) là chiều dày hiệu dụng của lớp khuếch tán.

Khuấy, tạo dòng chảy hoặc dùng điện cực quay làm \(\delta\) nhỏ hơn và tăng vận chuyển khối.

Nếu tiếp tục tăng điện áp sau khi đã bị giới hạn vận chuyển, phản ứng phụ có thể tăng thay vì sản lượng mong muốn.

## Ảnh hưởng của bọt khí

Phản ứng tạo khí sinh bọt trên điện cực. Bọt có thể:

- che diện tích hoạt động;
- tăng điện trở hiệu dụng;
- thay đổi vận chuyển khối cục bộ;
- tạo lực cơ học khi tách khỏi bề mặt;
- đồng thời tăng khuấy trộn cục bộ.

Do đó máy điện phân phải quản lý bọt khí chứ không chỉ tối ưu chất xúc tác.

## Phân bố dòng điện

Trường điện và hình học làm mật độ dòng không đồng đều. Các góc và cạnh có thể tập trung dòng, gây lớp mạ dày cục bộ hoặc tăng nguy cơ dendrite.

Thiết kế hình dạng điện cực, khoảng cách, độ dẫn điện ly và cách cấp dòng là một bài toán ghép giữa electrochemistry và kỹ thuật thiết bị.

## Sạc pin là điện phân có kiểm soát

Khi sạc pin thứ cấp, nguồn ngoài ép phản ứng cell đi ngược chiều phóng điện.

Về bản chất đây là một quá trình điện phân trong thiết bị lưu trữ năng lượng.

Sạc quá nhanh có thể thúc đẩy:

- mạ lithium;
- phân hủy chất điện ly;
- sinh khí;
- biến dạng và nứt vật liệu điện cực.

Do đó bộ sạc phải giới hạn điện áp, dòng điện và nhiệt độ theo nhiệt động lực học, động học và vận chuyển của cell.

## Hiệu suất Coulomb trong pin

Trong một chu kỳ:

\[
CE=\frac{Q_{phóng}}{Q_{sạc}}
\]

hoặc quy ước tương đương phù hợp với cách đo.

Nếu CE nhỏ hơn 100%, một phần điện lượng mỗi chu kỳ bị mất vào phản ứng phụ.

Ngay cả `99.9%` cũng có thể chưa đủ cho hàng nghìn chu kỳ vì tổn thất tích lũy theo thời gian.

## Dendrite và mạ kim loại không đồng đều

Khi kim loại bám không đều, một chỗ lồi có thể tập trung điện trường và mật độ dòng, làm nó phát triển nhanh hơn vùng xung quanh.

Dendrite có thể xuyên separator trong pin hoặc làm lớp mạ mất chất lượng.

Kiểm soát chất điện ly, mật độ dòng, bề mặt và ràng buộc cơ học là một bài toán đa vật lý.

## Nhiệt và an toàn

Điện năng đầu vào không chuyển hoàn toàn thành năng lượng tự do hóa học.

Tổn thất điện trở sinh nhiệt:

\[
P=I^2R
\]

Quá thế cũng làm tiêu tán năng lượng.

Trong hệ dòng lớn, nhiệt độ tăng lại thay đổi độ dẫn điện và động học, tạo phản hồi hai chiều giữa điện và nhiệt.

Thiết kế phải đồng thời kiểm soát:

- làm mát;
- khí sinh ra;
- tương thích vật liệu;
- cách điện;
- áp suất;
- chế độ khẩn cấp.

## Trade-off quan trọng trong thiết kế điện phân

Một cải tiến ở một chỉ tiêu có thể làm chỉ tiêu khác xấu đi.

Ví dụ:

```text
tăng mật độ dòng
→ tăng sản lượng trên diện tích
→ nhưng tăng quá thế, nhiệt và nguy cơ giới hạn vận chuyển
```

Hoặc:

```text
chất điện ly đậm đặc hơn
→ có thể tăng nồng độ chất phản ứng
→ nhưng có thể tăng độ nhớt và giảm khuếch tán
```

Hoặc:

```text
chất xúc tác hoạt tính cao
→ giảm quá thế
→ nhưng có thể đắt, độc hoặc kém bền
```

Do đó một cell tốt là kết quả tối ưu đa mục tiêu, không phải tối đa một đại lượng duy nhất.

## Các hiểu lầm thường gặp

### “Điện phân vi phạm tính tự phát của nhiệt động lực học”

Không. Nguồn điện cung cấp công để ép quá trình đi theo chiều không tự phát; xét toàn hệ vẫn tuân các định luật nhiệt động.

### “Cathode luôn là cực âm theo định nghĩa”

Không. Cathode được định nghĩa là nơi xảy ra khử. Trong điện phân nó thường là phía âm của nguồn, nhưng định nghĩa nền vẫn là phản ứng.

### “Tổng điện lượng luôn cho đúng lượng sản phẩm mong muốn”

Chỉ khi hiệu suất Faraday bằng 100% và toàn bộ sản phẩm được hạch toán đúng.

### “Chỉ cần vượt điện áp Nernst là phản ứng sẽ chạy nhanh”

Không. Quá thế, động học xúc tác và vận chuyển khối quyết định dòng thực tế.

### “Điện áp càng cao thì sản lượng luôn tăng tỷ lệ thuận”

Không. Khi bị giới hạn vận chuyển, tăng điện áp có thể chỉ làm tăng phản ứng phụ và sinh nhiệt.

### “Điện phân nước chỉ cần đúng 1.23 V trong thực tế”

`1.23 V` gần điều kiện chuẩn là giới hạn nhiệt động thuận nghịch, không phải điện áp vận hành thực tế của thiết bị.

## Mô hình tư duy

Điện phân là chuỗi chuyển đổi:

```text
nguồn điện ngoài
→ thay đổi thế điện hóa
→ chuyển electron ở hai điện cực
→ ion vận chuyển trong chất điện ly
→ thành phần hóa học thay đổi
```

Hiệu quả thực được quyết định đồng thời bởi:

```text
nhiệt động lực học
+ động học điện cực
+ vận chuyển khối
+ điện trở
+ độ chọn lọc phản ứng
+ vật liệu
+ hình học thiết bị
+ quản lý nhiệt và khí
```

Xem tiếp: [Pin, ăn mòn và lưu trữ năng lượng](./05_batteries_corrosion_and_energy_storage.md) và [Động học điện hóa và phổ trở kháng](./06_electrochemical_kinetics_and_impedance.md).