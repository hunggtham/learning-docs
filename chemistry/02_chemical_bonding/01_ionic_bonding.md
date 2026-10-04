# Liên kết ion — từ lực Coulomb tới mạng tinh thể, khuyết tật và tính chất vật liệu

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Liên kết ion — từ lực Coulomb tới mạng tinh thể, khuyết tật và tính chất vật liệu**. Route đi từ ion formation → Coulomb/lattice energy → crystal packing/defects → conductivity, brittleness và solubility, để không nhầm một cặp ion với toàn bộ mạng tinh thể.

> **Liên kết ion (ionic bonding / 이온 결합)** là cách mô tả liên kết khi sự phân tách điện tích đủ lớn để hệ có thể được hiểu hữu ích như các cation và anion tương tác chủ yếu bằng lực hút tĩnh điện. Trong chất rắn ion, đối tượng cấu trúc quan trọng thường không phải một “phân tử NaCl riêng lẻ” mà là một **mạng tinh thể mở rộng (extended crystal lattice)**.

Điểm quan trọng là không nên hình dung liên kết ion như một quá trình đơn giản gồm “nguyên tử A cho electron cho B rồi hai ion hút nhau”. Sự tạo thành chất rắn ion là kết quả của **một bài toán năng lượng tập thể** gồm ion hóa, ái lực electron, lực hút Coulomb, lực đẩy ở khoảng cách ngắn, hình học mạng, entropy và đôi khi cả đóng góp cộng hóa trị đáng kể.

## Từ sự hình thành ion đến tinh thể

Một cách giải thích quá ngắn thường nói sodium cho chlorine một electron, tạo `Na+` và `Cl-`, rồi hai ion hút nhau. Cách nói này giúp hạch toán electron nhưng bỏ mất câu hỏi năng lượng: tạo `Na+` từ Na cần năng lượng ion hóa; nhận electron vào Cl giải phóng một phần năng lượng; sau đó việc nhiều ion sắp xếp thành mạng tinh thể giải phóng thêm năng lượng đáng kể.

Muốn hiểu vì sao NaCl bền, phải xét **toàn bộ chu trình năng lượng**, không chỉ bước chuyển electron.

Có thể hình dung chuỗi lô-gic (logic / 논리):

```text
nguyên tử trung hòa
→ tạo ion riêng lẻ
→ các ion tương tác
→ hình thành mạng tinh thể
→ mạng thư giãn về cấu trúc có năng lượng thấp
```

Bước tạo ion có thể tốn năng lượng, nhưng sự tạo mạng có thể bù lại rất mạnh. Đây là lý do “electron transfer” không tự nó quyết định chất ion có bền hay không.

> **Nối mạch:** Phần hình thành ion mới chỉ nêu nguồn điện tích; **Lực hút Coulomb trong mạng tinh thể** mở rộng nó thành tổng tương tác hút–đẩy của cả mạng. Vì vậy **Năng lượng mạng tinh thể** là bước kế tiếp để định lượng độ bền của cấu trúc.

## Lực hút Coulomb trong mạng tinh thể

Với hai điện tích điểm, năng lượng tương tác có dạng:

\[
V(r)=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r}
\]

Vì `q_1q_2 < 0` cho cation–anion nên tương tác là hút. Tuy nhiên trong tinh thể, mỗi ion tương tác với rất nhiều ion khác, gồm cả lực hút và lực đẩy.

Nếu chỉ giữ lực Coulomb, mô hình sẽ dự đoán các ion trái dấu tiến sát vô hạn. Điều đó không xảy ra vì khi các đám mây electron chồng lấn quá mạnh, **lực đẩy Pauli và lực đẩy khoảng cách ngắn** tăng rất nhanh.

Một mô hình trực giác là:

\[
U(r)\approx -\frac{A}{r}+\frac{B}{r^n}
\]

Hạng thứ nhất là hút Coulomb, hạng thứ hai mô tả lực đẩy ngắn hạn. Khoảng cách cân bằng xuất hiện tại cực tiểu của tổng năng lượng.

Điều này nối trực tiếp liên kết ion với ý tưởng tổng quát về **cảnh quan thế năng (potential-energy landscape)**.

> **Nối mạch:** Mô hình Coulomb cho biết lực thay đổi theo khoảng cách; **Năng lượng mạng tinh thể** gom các tương tác đó thành đại lượng của toàn mạng. **Hằng số Madelung — hình học trở thành năng lượng** tiếp tục chỉ ra vì sao cùng điện tích nhưng cách sắp xếp khác lại cho năng lượng khác.

## Năng lượng mạng tinh thể

**Năng lượng mạng tinh thể (lattice energy / 격자 에너지)** mô tả năng lượng liên quan tới việc tạo mạng tinh thể từ ion khí hoặc phá mạng thành ion khí, tùy quy ước. Khi đọc số liệu luôn phải kiểm tra định nghĩa dấu.

Về xu hướng, lực hút mạng mạnh hơn khi điện tích ion lớn và bán kính ion nhỏ:

\[
|U|\propto\frac{|z_+z_-|}{r}
\]

Do đó MgO với `Mg²+` và `O²-` thường có năng lượng mạng lớn hơn đáng kể so với NaCl có ion đơn điện tích với kích thước tương tự.

Nhưng đây mới là xu hướng bậc nhất. Hình học mạng cũng quan trọng.

> **Nối mạch:** Sau khi tách ảnh hưởng của điện tích và khoảng cách trong **Năng lượng mạng tinh thể**, **Hằng số Madelung** đưa hình học phối trí vào công thức. **Chu trình Born–Haber** dùng đại lượng mạng này trong một cân bằng năng lượng có thể kiểm chứng.

## Hằng số Madelung — hình học trở thành năng lượng

Trong mạng tinh thể, một ion tương tác với tất cả các ion còn lại. Tổng tương tác Coulomb có thể được gom vào **hằng số Madelung (Madelung constant)**, ký hiệu thường là \(M\).

Một biểu thức lý tưởng hóa kiểu Born–Landé có dạng:

\[
U=-\frac{N_A M z_+z_-e^2}{4\pi\varepsilon_0r_0}
\left(1-\frac{1}{n}\right)
\]

Trong đó:

- \(N_A\): hằng số Avogadro;
- \(M\): hằng số Madelung, phụ thuộc cấu trúc mạng;
- \(z_+,z_-\): điện tích ion;
- \(r_0\): khoảng cách lân cận gần nhất;
- \(n\): tham số liên quan lực đẩy khoảng cách ngắn.

Ý nghĩa quan trọng hơn công thức là: **cùng loại ion nhưng cách sắp xếp khác nhau có thể tạo năng lượng mạng khác nhau**.

Vì vậy cấu trúc tinh thể không chỉ là hình học trang trí; nó là một phần của nhiệt động lực học.

> **Nối mạch:** **Hằng số Madelung** mô tả đóng góp hình học, còn **Chu trình Born–Haber** đặt nó cạnh ion hóa, ái lực electron và nguyên tử hóa để suy ra năng lượng mạng. Kết quả cần được diễn giải trên đúng đối tượng là **chất rắn ion**, không phải một phân tử riêng.

## Chu trình Born–Haber: dùng bảo toàn năng lượng để suy luận

**Chu trình Born–Haber (Born–Haber cycle / 보른-하버 순환)** dùng định luật Hess để phân tách quá trình tạo chất rắn ion thành các bước giả định như:

```text
nguyên tử hóa
→ ion hóa cation
→ nhận electron của anion
→ tạo mạng tinh thể
```

Mục tiêu không phải khẳng định tinh thể thật sự hình thành đúng theo trình tự đó. Chu trình chỉ tận dụng việc enthalpy là **hàm trạng thái (state function)**: tổng biến thiên năng lượng không phụ thuộc con đường giả định.

Chu trình Born–Haber rất hữu ích khi một thành phần như năng lượng mạng khó đo trực tiếp nhưng các đại lượng còn lại có thể lấy từ thực nghiệm.

Đây là một ví dụ điển hình cho việc nhiệt động lực học cho phép suy ra một đại lượng vi mô từ một chuỗi đại lượng vĩ mô.

> **Nối mạch:** Chu trình năng lượng giải thích vì sao mạng bền; **chất rắn ion không gồm các phân tử độc lập** xác định cách đọc công thức như đơn vị tỉ lệ. Từ mô hình mạng đó, **Số phối trí và tỉ lệ bán kính** cho biết các ion được sắp xếp ra sao.

## Chất rắn ion không gồm các phân tử độc lập

Trong tinh thể NaCl, mỗi `Na+` được bao quanh bởi nhiều `Cl-` và ngược lại. Công thức `NaCl` biểu diễn **đơn vị công thức (formula unit)**, tức tỉ lệ nguyên tử tối giản bảo đảm trung hòa điện tích, chứ không nhất thiết là một phân tử rời rạc.

Điều này góp phần giải thích vì sao nhiều chất rắn ion có nhiệt độ nóng chảy cao: muốn làm mạng mất trật tự phải thắng một tập hợp lớn các tương tác tĩnh điện trên toàn mạng.

> **Nối mạch:** Khi công thức được hiểu là mạng mở rộng, **Số phối trí và tỉ lệ bán kính** cung cấp mô hình hình học đầu tiên cho các lân cận. **Bán kính ion không phải hằng số tuyệt đối** nhắc rằng mô hình ấy phụ thuộc môi trường phối trí và trạng thái điện tử.

## Số phối trí và tỉ lệ bán kính

Trong mạng ion, **số phối trí (coordination number)** mô tả số ion trái dấu lân cận gần nhất quanh một ion.

Ví dụ mô hình NaCl có phối trí 6:6; kiểu CsCl có phối trí 8:8; nhiều cấu trúc khác có phối trí 4, 6 hoặc 8 tùy kích thước tương đối và kiểu đóng gói.

Quy tắc **tỉ lệ bán kính (radius-ratio rule)** đôi khi được dùng để dự đoán hình học phối trí từ tỉ lệ bán kính cation/anion. Tuy nhiên đây chỉ là mô hình hình học sơ bộ vì ion không phải những quả cầu cứng hoàn hảo và mức độ cộng hóa trị cũng có thể đáng kể.

Một cách hiểu tốt hơn là: cấu trúc được chọn bởi **tổng năng lượng tự do thấp nhất**, trong đó kích thước ion là một yếu tố hình học quan trọng nhưng không phải yếu tố duy nhất.

> **Nối mạch:** Quy tắc tỉ lệ bán kính chỉ là xấp xỉ vì bán kính thay đổi theo phối trí và oxy hóa. Biết giới hạn đó giúp đọc **Độ dẫn điện** qua khoảng cách, khuyết tật và khả năng ion rời vị trí mạng.

## Bán kính ion không phải hằng số tuyệt đối

Bán kính của cùng một ion có thể thay đổi theo:

- số phối trí;
- trạng thái spin;
- trạng thái oxy hóa;
- môi trường liên kết.

Ví dụ cation ở trạng thái oxy hóa cao thường nhỏ hơn cùng nguyên tố ở trạng thái oxy hóa thấp vì lực hút hạt nhân hiệu dụng trên mỗi electron lớn hơn.

Do đó bảng bán kính ion phải luôn được hiểu gắn với quy ước và môi trường phối trí.

> **Nối mạch:** Kích thước và phối trí quyết định mức ion bị giữ trong mạng, nhưng dẫn điện chỉ xuất hiện khi hạt mang điện có đường di chuyển. **Khuyết tật Schottky và Frenkel** cung cấp chính những đường đi vi mô đó.

## Độ dẫn điện — cần hạt mang điện có khả năng di chuyển

NaCl rắn không dẫn điện tốt dù chứa các hạt mang điện, vì ion bị giữ tại các vị trí mạng và không thể dịch chuyển xa.

Khi nóng chảy hoặc hòa tan trong nước, ion trở nên linh động và có thể mang dòng điện. Đây là mối nối trực tiếp giữa **độ linh động vi mô (microscopic mobility)** và **độ dẫn điện vĩ mô (macroscopic conductivity)**.

Trong một số chất rắn ion đặc biệt, ion vẫn có thể di chuyển qua các khuyết tật mạng ngay ở trạng thái rắn. Đó là nền tảng của **chất dẫn ion rắn (solid ionic conductor)** dùng trong pin, pin nhiên liệu và cảm biến.

> **Nối mạch:** **Khuyết tật Schottky và Frenkel** giải thích cách mạng tự tạo vacancy hoặc vị trí xen kẽ để ion dịch chuyển. Khi muốn điều chỉnh mật độ khuyết tật có chủ ý, ta chuyển sang **pha tạp khác hóa trị và bù điện tích**.

## Khuyết tật Schottky và Frenkel

Tinh thể ion thật không hoàn hảo.

**Khuyết tật Schottky (Schottky defect)** là tổ hợp khuyết nút cation và anion được tạo sao cho tổng điện tích vẫn trung hòa.

**Khuyết tật Frenkel (Frenkel defect)** xảy ra khi một ion rời vị trí mạng bình thường và đi vào vị trí xen kẽ.

Khuyết tật không chỉ là “lỗi”. Chúng tạo đường cho:

- khuếch tán ion;
- dẫn ion;
- phản ứng trạng thái rắn;
- quá trình thiêu kết;
- sự trao đổi ion.

Trong vật liệu chức năng, mật độ khuyết tật thường được **thiết kế có chủ ý**.

> **Nối mạch:** Từ vacancy tự phát, **pha tạp khác hóa trị** cho thấy cách thiết kế khuyết tật và bù điện tích để tăng dẫn ion. Nhưng thay đổi mạng cũng tác động đến cơ học, nên **Tính giòn** là hệ quả tiếp theo cần giải thích.

## Pha tạp khác hóa trị và bù điện tích

Nếu thay một ion bằng ion có hóa trị khác, mạng phải bù điện tích.

Ví dụ khi pha `Y³+` vào `ZrO₂`, một phần `Zr⁴+` bị thay bởi `Y³+`. Mạng tạo vacancy oxygen để giữ trung hòa điện tích.

Các vacancy oxygen này làm ion `O²−` di chuyển dễ hơn, tạo chất điện ly rắn hữu ích trong pin nhiên liệu oxide rắn.

Đây là ví dụ rất rõ cho chuỗi:

```text
thành phần pha tạp
→ khuyết tật điện tích
→ độ linh động ion
→ tính chất điện
→ chức năng thiết bị
```

> **Nối mạch:** Pha tạp và khuyết tật làm đổi cách các mặt mạng trượt, từ đó giải thích **tính giòn** thay vì coi đây là thuộc tính ghi nhớ. Để chuyển từ cơ học sang hóa học dung dịch, **độ tan trong nước** cần cân bằng năng lượng mạng với solvat hóa.

## Tính giòn

Tinh thể ion thường giòn. Khi một lớp mạng bị trượt, các ion cùng điện tích có thể bị đưa đến gần nhau. Lực đẩy mạnh làm tinh thể nứt thay vì biến dạng dẻo liên tục như nhiều kim loại.

Tính chất cơ học này không phải một dữ kiện phải học thuộc; nó có thể suy ra từ trật tự điện tích trong mạng tinh thể và số lượng hệ trượt khả dụng.

Tuy nhiên không phải mọi chất rắn ion đều giòn giống nhau. Vi cấu trúc, khuyết tật, kích thước hạt và mức cộng hóa trị có thể thay đổi cơ chế phá hủy.

> **Nối mạch:** **Độ tan trong nước** vẫn quay về cùng bài toán năng lượng: phá mạng, hydrat hóa và entropy. Nếu ion còn tham gia phản ứng acid–base hoặc tạo phức, **độ tan còn phụ thuộc pH và phản ứng phụ** chứ không dừng ở một giá trị mạng.

## Độ tan trong nước là cuộc cạnh tranh nhiệt động

Việc hợp chất ion tan không chỉ phụ thuộc câu “nước phân cực”. Sự hòa tan là cạnh tranh giữa:

1. chi phí phá mạng tinh thể;
2. lợi ích hydrat hóa/solvat hóa ion;
3. biến thiên entropy khi ion phân tán vào dung dịch.

Có thể viết tổng quát:

\[
\Delta G_{dissolution}
=\Delta H_{lattice\ break}
+\Delta H_{solvation}
-T\Delta S_{dissolution}
\]

Nếu tổng \(\Delta G\) âm, hòa tan thuận lợi về nhiệt động.

Phân tử nước định hướng lưỡng cực quanh các ion và làm hạ năng lượng của ion đã tách khỏi mạng. Ion nhỏ, điện tích cao thường được hydrat hóa mạnh, nhưng đồng thời chính các ion đó cũng có thể tạo mạng rất bền.

Do đó có muối ion tan rất tốt và cũng có muối gần như không tan. Không thể suy luận đơn giản “chất ion = tan trong nước”.

> **Nối mạch:** Khi cân bằng ghép kéo ion ra khỏi dung dịch, độ tan phải được đọc cùng pH và ligand. Trường hợp đó cũng cho thấy **tính ion là một phổ liên tục**, vì phản ứng và môi trường có thể làm thay đổi mức phân cực liên kết.

## Độ tan còn phụ thuộc pH và phản ứng phụ

Nếu một ion trong muối phản ứng với `H+`, `OH−` hoặc ligand khác, cân bằng hòa tan có thể bị kéo mạnh.

Ví dụ carbonate ít tan có thể tan nhiều hơn trong acid vì `CO₃²−` bị proton hóa thành `HCO₃−` rồi `CO₂/H₂CO₃`.

Do đó độ tan của chất ion thường là một bài toán **cân bằng ghép (coupled equilibria)**, không chỉ là một con số `Ksp` độc lập.

> **Nối mạch:** Phản ứng phụ làm lộ ra rằng không có ranh giới tuyệt đối giữa “ion” và “cộng hóa trị”. **Mật độ electron và điện tích hiệu dụng** là mô tả vi mô phù hợp hơn để theo dõi phổ liên tục ấy.

## Tính ion là một phổ liên tục

Ngay cả trong hợp chất được gọi là ion, mật độ electron không phải lúc nào cũng tương ứng hoàn hảo với điện tích nguyên trên từng nguyên tử. **Sự phân cực (polarization)** và đóng góp cộng hóa trị có thể đáng kể.

**Quy tắc Fajans (Fajans' rules)** cung cấp một quy tắc kinh nghiệm: cation nhỏ, điện tích cao dễ phân cực anion lớn và dễ làm liên kết mang tính cộng hóa trị hơn.

Ví dụ `AlCl₃` có đặc tính cộng hóa trị đáng kể hơn `NaCl` dù cả hai đều có thể được giới thiệu ban đầu bằng mô hình ion.

Điều này nhắc rằng “ion” là một mô hình hữu ích chứ không phải nhãn nhị phân tuyệt đối.

> **Nối mạch:** **Mật độ electron và điện tích hiệu dụng** nối ngôn ngữ điện tích hình thức với phân bố electron thực tế. Từ phân bố đó, **liên hệ với chất rắn và vật liệu** cho thấy liên kết ion chi phối độ cứng, dẫn điện và ổn định pha như thế nào.

## Mật độ electron và điện tích hiệu dụng

Điện tích hình thức `Na+`, `Cl−`, `Mg²+` rất hữu ích cho hóa lượng và điện trung hòa, nhưng điện tích thực suy ra từ mật độ electron có thể không bằng đúng số nguyên đó.

Các phương pháp như phân tích mật độ electron, Bader charge hoặc population phân tích (analysis / 분석) cho những giá trị phụ thuộc mô hình phân chia electron.

Điều này không làm mô hình ion “sai”. Nó chỉ cho thấy mô hình ion là một **mức trừu tượng hóa** đặc biệt hiệu quả cho nhiều tính chất tập thể.

> **Nối mạch:** Khi đã theo dõi từ mật độ electron đến tính chất vật liệu, phần **liên hệ với chất rắn và vật liệu** cho phép kiểm tra mô hình bằng các hệ quả quan sát được. **Các hiểu lầm thường gặp** tiếp theo sẽ chỉ ra nơi suy luận thường bị rút gọn quá mức.

## Liên hệ với chất rắn và vật liệu

Liên kết ion xuất hiện trong:

- muối khoáng;
- oxide gốm;
- chất điện ly rắn;
- vật liệu pin;
- perovskite ion;
- cement và khoáng vật;
- nhiều vật liệu điện môi.

Trong các hệ này, cần đi xa hơn khái niệm “cation hút anion” và xét thêm:

```text
mạng tinh thể
+ khuyết tật
+ khuếch tán
+ pha tạp
+ bề mặt
+ ranh giới hạt
```

Đây là cầu nối từ hóa học liên kết sang khoa học vật liệu.

> **Nối mạch:** Các hệ quả vật liệu cung cấp dữ liệu để đối chiếu, còn **các hiểu lầm thường gặp** cho thấy vì sao suy luận “ion = phân tử”, “ion = luôn tan” hay “điện tích hình thức = điện tích thật” đều thiếu điều kiện. **Mô hình tư duy** sẽ gom lại các điều kiện cần giữ.

## Các hiểu lầm thường gặp

### “Hợp chất ion luôn tồn tại dưới dạng phân tử riêng lẻ”

Không. Trong chất rắn, nhiều hợp chất ion tạo mạng tinh thể mở rộng.

### “Chuyển electron tự nó giải phóng đủ năng lượng để tạo muối”

Không nhất thiết. Ion hóa có thể tốn nhiều năng lượng. Sự hình thành mạng và toàn bộ chu trình nhiệt động mới quyết định độ bền tổng thể.

### “Chất ion luôn tan trong nước”

Không. Độ tan là kết quả cạnh tranh giữa năng lượng mạng, solvat hóa, entropy và các cân bằng ghép.

### “Tinh thể ion hoàn hảo mới là tinh thể tốt nhất”

Không. Nhiều vật liệu chức năng cần khuyết tật để dẫn ion, pha tạp hoặc tạo hoạt tính bề mặt.

### “Điện tích hình thức bằng đúng điện tích thực trên nguyên tử”

Không. Điện tích ion là mô hình rất hữu ích nhưng mật độ electron thật thường phân bố liên tục hơn.

> **Nối mạch:** **Mô hình tư duy** khép bài bằng chuỗi điều kiện: chuyển điện tích, tương tác mạng, hình học, khuyết tật, môi trường và hệ quả vật liệu. Chuỗi này là điểm tựa để đọc các chương liên kết hóa học khác mà không tách công thức khỏi cơ chế.

## Mô hình tư duy

Chất rắn ion là **mạng điện tích ba chiều có năng lượng được quyết định đồng thời bởi Coulomb, lực đẩy ngắn hạn, hình học mạng và khuyết tật**. Từ mô hình đó có thể suy ra không chỉ nhiệt độ nóng chảy hay độ giòn, mà còn độ tan, dẫn ion, pha tạp và hành vi của nhiều vật liệu kỹ thuật.

Xem tiếp: [Liên kết cộng hóa trị](./02_covalent_bonding.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
