# Chất bán dẫn — hóa học của vùng năng lượng, khuyết tật và pha tạp

> **Chất bán dẫn (semiconductor / 반도체)** là vật liệu mà mật độ và chuyển động của hạt tải điện có thể được điều chỉnh rất mạnh bằng nhiệt độ, ánh sáng, điện trường, thành phần hóa học, khuyết tật và pha tạp có kiểm soát. Điểm quan trọng không phải là “độ dẫn nằm giữa kim loại và chất cách điện”, mà là khả năng **thiết kế quần thể electron và lỗ trống bằng hóa học vật liệu**.

Chương này nối trực tiếp các ý tưởng từ [orbital phân tử](../02_chemical_bonding/06_molecular_orbital_theory.md), [chất rắn](../03_matter_and_phases/02_solids.md), [xu hướng tuần hoàn](../01_atomic_structure/04_periodic_table_and_periodic_trends.md) và [hóa học bề mặt – mặt phân cách](./05_surface_and_interface_chemistry.md).

## Từ orbital phân tử tới vùng năng lượng

Khi hai nguyên tử tương tác, các orbital nguyên tử tổ hợp thành orbital liên kết và phản liên kết. Khi rất nhiều nguyên tử tạo thành tinh thể, mỗi mức năng lượng nguyên tử tạo ra số lượng trạng thái gần như liên tục. Với số nguyên tử vĩ mô, ta mô tả tập trạng thái đó bằng **vùng năng lượng (energy band)**.

```text
một nguyên tử
→ vài nguyên tử
→ nhiều orbital phân tử gần nhau
→ tinh thể vĩ mô
→ vùng năng lượng
```

Vùng chứa phần lớn electron hóa trị được gọi là **vùng hóa trị (valence band)**. Vùng cao hơn, nơi electron có thể tham gia dẫn điện hiệu quả, là **vùng dẫn (conduction band)**. Khoảng năng lượng giữa hai vùng là **vùng cấm (band gap, Eg)**.

Lý thuyết vùng vì vậy không tách khỏi hóa học liên kết; nó là phần mở rộng của tư duy orbital phân tử tới chất rắn gồm rất nhiều nguyên tử tương tác tuần hoàn.

## Kim loại, chất bán dẫn và chất cách điện

Trong mô hình đơn giản, kim loại có vùng bị chiếm một phần hoặc các vùng chồng lấp. Chất bán dẫn có vùng cấm đủ nhỏ để nhiệt hoặc photon có thể tạo hạt tải đáng kể. Chất cách điện thường có vùng cấm lớn hơn.

Không tồn tại một giá trị `Eg` duy nhất phân chia ba loại vật liệu. Độ dẫn còn phụ thuộc mật độ hạt tải, độ linh động, khuyết tật, mức pha tạp và nhiệt độ.

Đây là một ví dụ quan trọng của nguyên tắc xuyên suốt thư viện: **một thông số riêng lẻ hiếm khi quyết định toàn bộ hành vi của hệ**.

## Bán dẫn nội tại

Trong bán dẫn tinh khiết như silicon, nhiệt hoặc photon có thể kích thích electron từ vùng hóa trị lên vùng dẫn:

```text
electron ở vùng hóa trị
→ electron ở vùng dẫn
+ một trạng thái thiếu electron trong vùng hóa trị
```

Trạng thái thiếu electron được mô tả như một **lỗ trống (hole)** có điện tích hiệu dụng dương.

Trong bán dẫn nội tại:

\[
n=p=n_i
\]

với `n` là mật độ electron, `p` là mật độ lỗ trống và `ni` là mật độ hạt tải nội tại.

Gần đúng:

\[
n_i\propto e^{-E_g/(2k_BT)}
\]

Biểu thức này cho thấy vì sao chỉ thay đổi vừa phải nhiệt độ hoặc vùng cấm cũng có thể làm mật độ hạt tải thay đổi nhiều bậc độ lớn.

## Độ dẫn điện: mật độ hạt tải chưa phải toàn bộ câu chuyện

Một biểu thức cơ bản là:

\[
\sigma=q(n\mu_n+p\mu_p)
\]

trong đó `μn` và `μp` là độ linh động của electron và lỗ trống.

Pha tạp thường làm tăng mật độ hạt tải, nhưng tạp chất, phonon và khuyết tật cũng có thể làm giảm độ linh động do tăng tán xạ. Vì vậy tăng nồng độ chất pha tạp không làm độ dẫn tăng vô hạn.

Đây là một **đánh đổi (trade-off)** thực tế:

```text
pha tạp nhiều hơn
→ nhiều hạt tải hơn
nhưng đồng thời
→ nhiều tâm tán xạ hơn
```

Thiết kế vật liệu phải tối ưu cả hai phía.

## Mức Fermi — thế hóa học của electron

**Mức Fermi (Fermi level, EF)** đóng vai trò như thế hóa học của electron trong mô tả thống kê. Xác suất một trạng thái năng lượng `E` được chiếm tuân phân bố Fermi–Dirac:

\[
f(E)=\frac{1}{e^{(E-E_F)/(k_BT)}+1}
\]

Trong bán dẫn nội tại, `EF` thường nằm gần giữa vùng cấm. Pha tạp cho electron làm `EF` dịch về phía vùng dẫn; pha tạp nhận electron làm `EF` dịch về phía vùng hóa trị.

Điểm cần hiểu là mức Fermi không phải “một electron cụ thể”. Nó là đại lượng nhiệt động thống kê mô tả quần thể trạng thái điện tử.

## Pha tạp — thiết kế khuyết tật có chủ ý

Silicon có bốn electron hóa trị. Thay một phần rất nhỏ nguyên tử Si bằng nguyên tố khác có thể thay đổi quần thể hạt tải rất mạnh.

### Bán dẫn loại n

Nguyên tố nhóm 15 như P, As hoặc Sb có năm electron hóa trị. Bốn electron tham gia liên kết với mạng Si, còn electron thứ năm tương đối dễ được kích thích vào vùng dẫn.

Nguyên tử kiểu này là **chất cho electron (donor)**. Sau khi cho electron, tâm donor trở thành ion dương gần như cố định trong mạng.

### Bán dẫn loại p

Nguyên tố nhóm 13 như B có ba electron hóa trị. Khi thay Si, nó tạo trạng thái có thể nhận electron từ vùng hóa trị và để lại lỗ trống di động.

Nguyên tử kiểu này là **chất nhận electron (acceptor)**. Sau khi nhận electron, tâm acceptor mang điện tích âm gần như cố định.

Pha tạp vì thế nên được hiểu là **hóa học khuyết tật điểm có kiểm soát**, không phải đơn giản “làm bẩn tinh thể”.

## Trung hòa điện tích và quan hệ tác dụng khối

Ở cân bằng, tổng điện tích của electron, lỗ trống và các tâm pha tạp ion hóa phải thỏa điều kiện trung hòa điện tích.

Trong vùng bán dẫn không suy biến, thường có:

\[
np=n_i^2
\]

Nếu pha tạp loại n làm `n >> ni`, thì:

\[
p\approx\frac{n_i^2}{n}
\]

Nghĩa là tăng hạt tải đa số đồng thời làm hạt tải thiểu số giảm. Quan hệ này trở nên rất quan trọng khi xét tiếp giáp, tái hợp và dòng rò.

## Tiếp giáp p–n — khuếch tán tự tạo điện trường

Khi đặt vùng p cạnh vùng n, electron khuếch tán từ n sang p còn lỗ trống khuếch tán từ p sang n vì chênh lệch nồng độ.

Khi hạt tải di động rời vùng gần mặt phân cách, các ion pha tạp cố định bị lộ ra:

```text
phía n → donor dương cố định
phía p → acceptor âm cố định
```

Các điện tích cố định tạo **vùng nghèo hạt tải (depletion region)** và một điện trường nội tại chống lại khuếch tán tiếp tục.

Cân bằng được thiết lập khi xu hướng khuếch tán do gradient nồng độ được cân bằng bởi chuyển động trôi do điện trường. Đây là cân bằng điện hóa chứ không phải một “bức tường” vật lý.

### Phân cực thuận

Điện áp ngoài làm giảm rào thế của tiếp giáp, cho phép hạt tải đa số vượt qua dễ hơn và dòng tăng mạnh.

### Phân cực ngược

Điện áp ngoài làm tăng rào thế đối với hạt tải đa số. Dòng chủ yếu đến từ hạt tải thiểu số cho tới khi các cơ chế đánh thủng trở nên đáng kể.

Tính bất đối xứng này là nền của diode.

## Ví dụ suy luận: vì sao một lượng tạp chất rất nhỏ vẫn có tác động lớn?

Một tinh thể Si chứa số nguyên tử cực lớn. Dù chỉ một phần triệu vị trí mạng được thay bằng donor, số tâm cho electron trên mỗi centimet khối vẫn có thể rất lớn so với mật độ hạt tải nội tại.

Do đó “nồng độ nguyên tử nhỏ” không đồng nghĩa “ảnh hưởng điện tử nhỏ”. Điều đúng hơn là so mật độ chất pha tạp với `ni` và với mật độ trạng thái điện tử liên quan.

## Sinh hạt tải và tái hợp

Electron và lỗ trống có thể tái hợp, giải phóng năng lượng dưới dạng nhiệt hoặc photon. Ngược lại, nhiệt hoặc ánh sáng có thể tạo cặp electron–lỗ trống.

Ba cơ chế tái hợp quan trọng gồm:

- tái hợp bức xạ;
- tái hợp qua tâm khuyết tật Shockley–Read–Hall;
- tái hợp Auger ở mật độ hạt tải cao.

Khuyết tật tạo mức năng lượng nằm sâu trong vùng cấm có thể bắt electron hoặc lỗ trống và rút ngắn **thời gian sống hạt tải (carrier lifetime)**. Vì thế tạp nhiễm rất nhỏ vẫn có thể làm thiết bị suy giảm rõ rệt.

## Vùng cấm trực tiếp và gián tiếp

Trạng thái electron trong tinh thể có cả năng lượng và xung lượng tinh thể `k`.

Trong **bán dẫn vùng cấm trực tiếp (direct-band-gap semiconductor)**, cực đại vùng hóa trị và cực tiểu vùng dẫn nằm gần cùng giá trị `k`, nên tái hợp bức xạ có thể phát photon hiệu quả.

GaAs và GaN là ví dụ quan trọng trong LED và laser.

Silicon có vùng cấm gián tiếp. Tái hợp bức xạ thường cần thêm phonon để bảo toàn xung lượng, nên Si rất hữu ích cho điện tử nhưng không phải vật liệu phát sáng hiệu quả như nhiều bán dẫn III–V.

## Hấp thụ ánh sáng và pin mặt trời

Photon có năng lượng:

\[
h\nu\ge E_g
\]

có thể tạo cặp electron–lỗ trống.

Trong **pin quang điện (photovoltaic cell)**, điện trường nội tại ở tiếp giáp hoặc tiếp giáp dị thể giúp tách các hạt tải trước khi chúng tái hợp, từ đó tạo dòng và điện áp hữu ích.

Vùng cấm tạo đánh đổi:

```text
Eg quá lớn
→ bỏ lỡ nhiều photon năng lượng thấp

Eg quá nhỏ
→ hấp thụ nhiều photon hơn
→ nhưng phần năng lượng vượt Eg dễ mất thành nhiệt
```

Vì vậy thiết kế vật liệu quang điện là bài toán tối ưu giữa hấp thụ, tái hợp, điện áp và khả năng thu hạt tải.

## LED — thành phần hóa học quyết định màu

Ở phân cực thuận, electron và lỗ trống được bơm vào vùng hoạt động. Trong vật liệu vùng cấm trực tiếp, tái hợp bức xạ cho photon có năng lượng gần:

\[
E_{photon}\approx E_g
\]

Thay đổi thành phần hợp kim như InGaN/GaN hoặc AlGaInP làm thay đổi `Eg`, từ đó thay đổi bước sóng và màu phát xạ.

Chuỗi suy luận là:

```text
thành phần nguyên tử
→ cấu trúc vùng năng lượng
→ năng lượng photon
→ màu phát xạ
```

## Bán dẫn hợp chất và vùng cấm rộng

Các vật liệu III–V như GaAs, GaN, InP và AlGaAs có thể cung cấp vùng cấm trực tiếp, độ linh động cao hoặc khả năng điều chỉnh vùng cấm bằng hợp kim hóa.

GaN và SiC là ví dụ vật liệu vùng cấm rộng. Chúng chịu điện trường đánh thủng và nhiệt độ cao tốt, vì vậy rất quan trọng trong điện tử công suất.

Nhưng vùng cấm rộng không tự động làm thiết bị “tốt hơn”. Chất lượng tinh thể, tiếp xúc điện, độ linh động, độ dẫn nhiệt và công nghệ chế tạo vẫn quyết định hiệu năng thực.

## Tiếp giáp dị thể và độ lệch vùng

Khi ghép hai chất bán dẫn khác nhau, biên vùng hóa trị và vùng dẫn thường không thẳng hàng. **Độ lệch vùng (band offset)** có thể giữ electron hoặc lỗ trống trong một vùng không gian hẹp, tạo giếng lượng tử.

**Tiếp giáp dị thể (heterojunction)** là nền của nhiều laser bán dẫn, transistor độ linh động cao và pin mặt trời nhiều lớp.

Lợi ích điện tử chỉ đạt được khi mặt phân cách có mật độ khuyết tật thấp và sai khác hằng số mạng được kiểm soát. Nếu không, mặt phân cách có thể trở thành nơi tái hợp thay vì nơi điều khiển hạt tải.

## Tinh thể đơn và độ tinh khiết cực cao

Trong bán dẫn, tạp chất ở mức ppm, ppb hoặc thấp hơn vẫn có thể tác động mạnh. Vì vậy “tinh sạch” ở đây nghĩa là kiểm soát thành phần tới cấp nguyên tử.

Silicon điện tử được tinh chế qua các tiền chất dễ bay hơi, sau đó chuyển lại thành Si tinh khiết. Tinh thể đơn có thể được nuôi bằng phương pháp Czochralski hoặc vùng nổi (**float-zone**).

Oxygen, carbon, lệch mạng và khuyết tật điểm phải được kiểm soát vì chúng ảnh hưởng mật độ hạt tải, thời gian sống và độ tin cậy thiết bị.

### Tinh luyện vùng

Nếu một tạp chất ưu tiên pha lỏng hơn pha rắn, một vùng nóng chảy hẹp di chuyển dọc thỏi có thể kéo tạp chất tập trung dần về một đầu.

Đây là ứng dụng trực tiếp của cân bằng pha và hệ số phân bố vào sản xuất vật liệu siêu tinh khiết.

## Oxy hóa silicon và vai trò của SiO₂

Silicon tạo oxide bền:

\[
Si+O_2\rightarrow SiO_2
\]

hoặc trong hơi nước:

\[
Si+2H_2O\rightarrow SiO_2+2H_2
\]

`SiO2` từng và vẫn đóng nhiều vai trò quan trọng như điện môi, lớp thụ động và lớp hỗ trợ công nghệ chế tạo. Chất lượng mặt phân cách Si/SiO₂ là một lý do nền công nghệ silicon phát triển mạnh.

## Lắng đọng màng — hóa học bề mặt trở thành công nghệ chế tạo

### Lắng đọng hơi hóa học

**Lắng đọng hơi hóa học (chemical vapor deposition, CVD)** dùng tiền chất khí phản ứng hoặc phân hủy trên tấm nền để tạo màng.

Tốc độ và chất lượng màng phụ thuộc đồng thời vào:

- độ bay hơi của tiền chất;
- động học phản ứng bề mặt;
- vận chuyển khối;
- nhiệt độ;
- phản ứng phụ trong pha khí.

Ở nhiệt độ thấp hoặc dòng tiền chất lớn, giới hạn có thể khác hẳn so với vùng nhiệt độ cao. Vì thế tối ưu CVD là bài toán ghép giữa kinetics và transport, không chỉ là chọn một phản ứng hóa học.

### Lắng đọng lớp nguyên tử

**Lắng đọng lớp nguyên tử (atomic layer deposition, ALD)** dùng các phản ứng bề mặt tự giới hạn theo chu kỳ:

```text
bề mặt + tiền chất A
→ bề mặt bão hòa A
→ rửa khí dư
→ tiền chất B phản ứng
→ tạo lớp mới
→ rửa khí dư
→ lặp lại
```

Vì mỗi nửa chu kỳ dừng khi các tâm phản ứng trên bề mặt đã bão hòa, ALD có thể tạo màng rất đồng đều trên cấu trúc ba chiều phức tạp.

Đánh đổi là tốc độ lắng đọng thường thấp hơn nhiều phương pháp khác.

## Khắc vật liệu

### Khắc ướt

Dung dịch phản ứng với lớp cần loại bỏ. Cơ chế có thể đẳng hướng hoặc phụ thuộc mặt tinh thể.

### Khắc plasma và khắc ion phản ứng

Plasma tạo gốc tự do và ion hoạt tính. Thành phần hóa học tạo sản phẩm dễ bay hơi, còn bắn phá ion theo hướng giúp tăng tính dị hướng.

Khắc kích thước nanomet vì vậy là bài toán ghép giữa hóa học plasma và vật lý bề mặt.

## Hóa học chất cản quang

**Chất cản quang (photoresist)** biến mẫu ánh sáng thành khác biệt độ tan hóa học.

Chất cản quang dương thường trở nên dễ hòa tan hơn ở vùng đã chiếu sáng. Chất cản quang âm thường tạo liên kết ngang hoặc giảm độ tan sau chiếu sáng, tùy hệ hóa học.

Các hệ khuếch đại hóa học tạo **acid quang sinh (photoacid)**; một sự kiện hấp thụ photon có thể khởi phát nhiều phản ứng giải bảo vệ sau đó. Độ nhạy tăng nhưng đổi lại phải kiểm soát khuếch tán acid và độ nhám biên mẫu.

Đây là một trade-off điển hình giữa **độ nhạy và độ phân giải không gian**.

## Điện môi hằng số cao và cổng kim loại

Khi lớp `SiO2` cổng quá mỏng, electron có thể xuyên hầm lượng tử làm dòng rò tăng.

Vật liệu điện môi hằng số cao như `HfO2` cho phép đạt điện dung lớn với chiều dày vật lý lớn hơn.

Nhưng thay vật liệu tạo ra hóa học mặt phân cách mới, trạng thái bẫy mới và yêu cầu lắng đọng mới. Khi kích thước thiết bị tiến tới cấp nguyên tử, nhiều vấn đề vốn tưởng là “điện tử” thực chất trở thành bài toán hóa học vật liệu.

## Khuyết tật — có loại hữu ích, có loại gây hại

Chất pha tạp thay thế là một loại khuyết tật hữu ích. Ngược lại, **khuyết nút (vacancy)**, nguyên tử xen kẽ, liên kết treo và tạp nhiễm có thể tạo trạng thái bẫy, tăng tán xạ hoặc giảm thời gian sống hạt tải.

Hydrogen có thể thụ động hóa một số liên kết treo.

Mục tiêu kỹ thuật không phải “tinh thể hoàn hảo tuyệt đối”, mà là **đúng loại khuyết tật, ở đúng vị trí, với nồng độ phù hợp**.

## Giam giữ lượng tử ở kích thước nano

Khi kích thước bán dẫn tiến gần bước sóng de Broglie của hạt tải hoặc bán kính Bohr của exciton, trạng thái năng lượng bắt đầu phụ thuộc mạnh vào kích thước.

Trong **chấm lượng tử (quantum dot)**, hạt nhỏ hơn thường có khoảng cách mức năng lượng lớn hơn và có thể phát ánh sáng bước sóng ngắn hơn.

Cùng thành phần hóa học nhưng kích thước khác nhau có thể cho màu khác. Đây là ví dụ rõ cho việc kích thước trở thành một biến thiết kế vật liệu, bên cạnh thành phần hóa học.

## Quy trình chế tạo chip là một hệ hóa học tích hợp

Một chu trình chế tạo hiện đại lặp nhiều bước:

```text
làm sạch
→ oxy hóa / lắng đọng
→ quang khắc
→ khắc
→ cấy ion / pha tạp
→ ủ
→ kim loại hóa
→ đánh bóng cơ–hóa (CMP)
→ thụ động hóa
```

Mỗi bước thay đổi bề mặt, mặt phân cách, phân bố chất pha tạp hoặc khuyết tật. Nhiễm bẩn ở một công đoạn có thể làm giảm **tỷ lệ chip đạt yêu cầu (yield)** ở công đoạn rất xa phía sau.

Vì vậy chế tạo bán dẫn là hệ tích hợp của hóa bề mặt, hóa phân tích, plasma, polymer, điện hóa, động học, vận chuyển và khoa học vật liệu.

## Ví dụ suy luận: vì sao điện áp hở mạch tốt nhưng pin mặt trời vẫn có hiệu suất thấp?

Điện áp hở mạch chủ yếu phản ánh chênh lệch thế hóa điện có thể duy trì. Hiệu suất thực còn phụ thuộc liệu photon có được hấp thụ hay không, hạt tải có tái hợp trước khi tới điện cực không, điện trở nội có lớn không và tiếp xúc có chọn lọc hạt tải tốt không.

Do đó một chỉ số điện áp không đủ để đánh giá toàn thiết bị. Đây cũng là logic tương tự trong pin điện hóa: thermodynamics đặt giới hạn, còn kinetics và transport quyết định hiệu suất vận hành.

## Những hiểu lầm thường gặp

### “Chất bán dẫn chỉ là vật liệu dẫn điện ở mức trung gian”

Không. Đặc tính quan trọng là khả năng điều khiển mật độ và chuyển động hạt tải trên nhiều bậc độ lớn.

### “Pha tạp nghĩa là thêm rất nhiều tạp chất”

Không. Một nồng độ nguyên tử rất nhỏ vẫn có thể lớn hơn rất nhiều mật độ hạt tải nội tại.

### “Lỗ trống là một hạt dương được đưa vào tinh thể”

Không. Lỗ trống là **chuẩn hạt (quasiparticle)** mô tả trạng thái thiếu electron trong một vùng gần đầy.

### “Biết vùng cấm là biết độ dẫn”

Không. Cần thêm mật độ hạt tải, độ linh động, mức pha tạp, khuyết tật và nhiệt độ.

### “Mặt phân cách chỉ là đường biên hình học”

Không. Nó có thể có liên kết chưa bão hòa, điện tích, dipole, khuyết tật và trạng thái bẫy riêng, đủ để chi phối toàn thiết bị.

### “Chế tạo chip chủ yếu là quang khắc”

Quang khắc chỉ là một phần. Lắng đọng, khắc, làm sạch, oxy hóa, pha tạp, kiểm soát mặt phân cách và nhiễm bẩn đều có vai trò nền tảng.

## Mô hình tư duy

Hãy xem chất bán dẫn như **một tinh thể mà quần thể trạng thái điện tử có thể được lập trình bằng hóa học**:

```text
thành phần + cấu trúc tinh thể
→ vùng năng lượng
→ pha tạp + khuyết tật
→ mật độ hạt tải + độ linh động
→ mặt phân cách + tái hợp
→ hành vi thiết bị
```

Lý thuyết vùng cho biết trạng thái nào được phép tồn tại; pha tạp và khuyết tật quyết định có bao nhiêu hạt tải; mặt phân cách và quy trình chế tạo quyết định chúng di chuyển, bị bẫy và tái hợp ra sao. Kiến trúc thiết bị sau đó chuyển sự điều khiển vi mô này thành logic, ánh sáng hoặc chuyển đổi năng lượng.

Xem tiếp: [Vật liệu nano](./04_nanomaterials.md) và [Hóa học bề mặt – mặt phân cách](./05_surface_and_interface_chemistry.md).