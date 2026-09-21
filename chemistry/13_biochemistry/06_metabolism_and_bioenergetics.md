# Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do

> **Chuyển hóa (metabolism / 대사)** là mạng phản ứng hóa học liên kết với nhau để biến đổi vật chất, lưu trữ/giải phóng năng lượng tự do và duy trì tổ chức tế bào. **Sinh năng lượng (bioenergetics / 생물에너지학)** nghiên cứu cách tế bào ghép phản ứng thuận lợi với phản ứng bất lợi, di chuyển electron, tạo gradient ion và biến gradient đó thành công hóa học.

Chuyển hóa không nên được học như danh sách con đường. Nó là một **mạng phản ứng ngoài cân bằng có ghép nối**, trong đó thông lượng thay đổi theo nguồn dinh dưỡng, trạng thái năng lượng và nhu cầu sinh tổng hợp.

Các prerequisite quan trọng:

- [Năng lượng tự do Gibbs](../05_thermodynamics/03_gibbs_free_energy.md) để hiểu `ΔG`, ghép phản ứng và động lực nhiệt động;
- [Cân bằng hóa học](../07_chemical_equilibrium/00_dynamic_equilibrium.md) để phân biệt equilibrium với steady state;
- [Điện thế pin và Nernst](../09_redox_and_electrochemistry/03_cell_potential_and_nernst_equation.md) để hiểu dòng electron và `ΔG = -nFΔE`;
- [Enzyme](./05_enzymes.md) để hiểu kiểm soát động học;
- [Ma trận hóa lượng và mạng phản ứng](../04_chemical_quantities/06_stoichiometric_matrices_and_reaction_networks.md) để hiểu thông lượng và FBA.

## Dị hóa và đồng hóa

**Dị hóa (catabolism / 이화작용)** phân giải phân tử giàu năng lượng thành sản phẩm nhỏ hơn và thu một phần năng lượng tự do vào ATP, NADH hoặc gradient ion.

**Đồng hóa (anabolism / 동화작용)** dùng năng lượng tự do và tiền chất để xây protein, acid nucleic, lipid, polysaccharide và các chất chuyển hóa chuyên biệt.

Hai hệ không độc lập. Dị hóa cung cấp năng lượng và khung carbon; nhu cầu đồng hóa lại điều chỉnh thông lượng dị hóa.

## Vì sao tế bào dùng nhiều bước thay vì một phản ứng khổng lồ?

Oxy hóa hoàn toàn glucose thành `CO2` và `H2O` rất thuận lợi về nhiệt động.

Nếu giải phóng toàn bộ năng lượng trong một bước không kiểm soát, phần lớn sẽ chuyển thành nhiệt và khó ghép vào công hữu ích.

Tế bào chia quá trình thành nhiều bước do enzyme xúc tác. Mỗi bước có thể:

- thu một phần năng lượng;
- tạo chất mang electron;
- tạo chất trung gian có thể chuyển sang đường khác;
- tạo điểm điều hòa.

Chuyển hóa vì vậy giống **hệ chuyển đổi năng lượng nhiều tầng** hơn là một lần “đốt cháy” duy nhất.

## Năng lượng tự do Gibbs trong tế bào

Với phản ứng trong điều kiện tế bào:

\[
\Delta G=\Delta G^{\circ'}+RT\ln Q
\]

Sinh hóa thường dùng `ΔG°'`, trạng thái chuẩn biến đổi gần pH 7, thay vì xem `H+` tự do ở 1 M.

Điểm quyết định là **ΔG thực tế**, không chỉ `ΔG°'`.

Một phản ứng có `ΔG°' > 0` vẫn có thể chạy thuận nếu tỉ lệ cơ chất/sản phẩm làm `Q` đủ nhỏ hoặc nếu phản ứng được ghép với quá trình khác.

Do đó:

```text
ΔG°' → mốc chuẩn
ΔG   → động lực thật trong điều kiện hiện tại
```

## Ghép phản ứng — năng lượng tự do cộng được

Giả sử:

\[
A\rightarrow B,\qquad \Delta G_1>0
\]

và:

\[
C\rightarrow D,\qquad \Delta G_2<0
\]

Nếu hai phản ứng được ghép qua chất trung gian chung:

\[
A+C\rightarrow B+D
\]

thì:

\[
\Delta G_{total}=\Delta G_1+\Delta G_2
\]

Nếu tổng âm, quá trình ghép có thể thuận lợi.

Câu “ATP cung cấp năng lượng” chỉ là cách nói ngắn cho việc ghép nhiệt động thông qua một cơ chế hóa học thật sự.

## ATP — chất trung gian chuyển nhóm, không phải “pin năng lượng” cô lập

Thủy phân ATP:

\[
ATP+H_2O\rightarrow ADP+P_i
\]

thường có `ΔG` âm trong điều kiện tế bào.

Các đóng góp gồm:

- sản phẩm được ổn định cộng hưởng tốt hơn;
- giảm đẩy tĩnh điện;
- ADP và `Pi` được hydrat hóa tốt;
- tỉ lệ ATP/ADP/Pi trong tế bào giữ `Q` thuận lợi.

Nói “phá liên kết phosphate giải phóng năng lượng” là gây hiểu sai. Phá liên kết luôn cần năng lượng; phản ứng tổng thuận lợi vì trạng thái sản phẩm được ổn định tốt hơn.

### Ghép chuyển phosphoryl

Tế bào thường chuyển phosphate từ ATP sang cơ chất để tạo chất trung gian hoạt hóa:

```text
cơ chất
+ ATP
→ cơ chất phosphoryl hóa
→ phản ứng tiếp theo thuận lợi hơn
```

Ghép xảy ra qua chất trung gian chung, không phải vì năng lượng “chảy” trực tiếp từ ATP sang phân tử bên cạnh.

## Trạng thái năng lượng adenylate

**Điện tích năng lượng adenylate (adenylate energy charge)**:

\[
EC=\frac{[ATP]+\frac12[ADP]}{[ATP]+[ADP]+[AMP]}
\]

Adenylate kinase xúc tác:

\[
2ADP\rightleftharpoons ATP+AMP
\]

Một thay đổi nhỏ của ATP có thể gây thay đổi tương đối lớn của AMP, làm AMP trở thành tín hiệu nhạy về thiếu năng lượng.

## Cofactor oxy hóa–khử — mang electron dưới dạng hóa học

Tế bào hiếm khi dùng electron tự do trong dung dịch. Electron được chuyển qua các cofactor.

### NAD+/NADH

NAD+ nhận tương đương hydride:

\[
NAD^++H^-\rightarrow NADH
\]

Trong dị hóa, NAD+ thường oxy hóa cơ chất và trở thành NADH. NADH sau đó cho electron vào chuỗi hô hấp.

### NADP+/NADPH

Hóa học cặp NADP+/NADPH gần NAD+/NADH, nhưng tế bào duy trì các pool ở trạng thái khác nhau.

NADPH thường được giữ ở trạng thái khử để cung cấp electron cho sinh tổng hợp và hệ chống oxy hóa.

### FAD/FADH2

Flavin có thể tham gia chuyển một hoặc hai electron và thường gắn chặt với enzyme.

Thế oxy hóa–khử của cofactor phụ thuộc mạnh môi trường protein.

## Điện thế oxy hóa–khử và dòng electron

Điện thế khử thực tế phụ thuộc thành phần qua phương trình Nernst.

Về nhiệt động, electron có xu hướng truyền từ cặp có điện thế khử thấp hơn tới cặp có điện thế khử cao hơn.

Quan hệ:

\[
\Delta G=-nF\Delta E
\]

nối trực tiếp điện hóa với sinh năng lượng.

`O2` là chất nhận electron cuối mạnh trong hô hấp hiếu khí vì khử oxygen thành nước cho `ΔE` dương lớn và vì vậy `ΔG` âm đáng kể.

## Đường phân — đọc bằng logic hóa học thay vì thuộc mười tên phản ứng

**Đường phân (glycolysis)** chuyển glucose thành pyruvate qua chuỗi enzyme trong bào tương.

### Pha đầu tư

ATP phosphoryl hóa glucose và các chất trung gian fructose.

Phosphate có nhiều vai trò:

- giữ chất chuyển hóa trong tế bào vì phân tử mang điện đi qua màng kém;
- tạo điểm nhận diện cho enzyme;
- hoạt hóa phân tử cho bước biến đổi sau.

Fructose-1,6-bisphosphate bị cắt thành hai phân tử ba carbon bằng hóa học aldol, nối trực tiếp với [hóa học carbonyl](../11_organic_chemistry/07_carbonyl_chemistry.md).

### Pha thu hồi

Glyceraldehyde-3-phosphate bị oxy hóa trong khi NAD+ bị khử.

Các chất trung gian phosphate có thế chuyển nhóm cao sau đó tạo ATP bằng **phosphoryl hóa mức cơ chất (substrate-level phosphorylation)**.

Năng lượng oxy hóa được giữ lại trong NADH và các nhóm phosphate hoạt hóa thay vì mất hoàn toàn thành nhiệt.

## Lên men — tái sinh NAD+

Đường phân cần NAD+.

Nếu NADH không được oxy hóa lại, pool NAD+ cạn và đường phân dừng.

Lên men chuyển electron từ NADH sang phân tử hữu cơ có nguồn từ pyruvate.

Ví dụ lactate:

\[
pyruvate+NADH+H^+\rightarrow lactate+NAD^+
\]

Vai trò chính của lên men là **tái sinh NAD+**, không phải tạo lượng ATP lớn ngoài phần đã có từ đường phân.

## Oxy hóa pyruvate và acetyl-CoA

Trong điều kiện hiếu khí, pyruvate được chuyển thành acetyl-CoA, đồng thời tạo `CO2` và NADH.

Coenzyme A tạo thioester có thế chuyển acyl cao.

Thioester được giải thích chi tiết ở [acid carboxylic và dẫn xuất](../11_organic_chemistry/08_carboxylic_acids_and_derivatives.md).

Acetyl-CoA là nút giao giữa carbohydrate, acid béo và amino acid.

## Chu trình acid citric — vừa oxy hóa vừa cung cấp tiền chất

Acetyl-CoA ngưng tụ với oxaloacetate rồi trải qua tái sắp xếp, oxy hóa và khử carboxyl.

Năng lượng được giữ trong NADH, FADH2 và GTP/ATP tương đương.

Chu trình còn cung cấp chất trung gian cho sinh tổng hợp nên được gọi là **amphibolic**.

Khi chất trung gian bị rút ra, **phản ứng bổ sung (anaplerotic reaction)** bù lại pool trung gian.

Do đó chu trình vừa là đường oxy hóa vừa là trung tâm phân phối carbon.

## Chuỗi truyền electron — biến năng lượng redox thành gradient proton

NADH cho electron vào chuỗi hô hấp ở màng trong ty thể.

Electron đi qua các chất mang có điện thế khử tăng dần về phía `O2`.

Một số phức hợp ghép chuyển electron thuận lợi với bơm proton ra khỏi matrix.

Chuỗi biến đổi:

```text
năng lượng redox
→ công bơm proton
→ gradient điện hóa
```

## Động lực proton

Gradient proton có hai thành phần:

1. chênh lệch hoạt độ proton;
2. chênh lệch điện thế màng.

Với ion điện tích `z`:

\[
\Delta\mu=RT\ln\frac{a_2}{a_1}+zF\Delta\psi
\]

Đây là **thế điện hóa**: tổng của đóng góp hóa học và điện.

Màng vì vậy vừa có đặc tính của pin nồng độ vừa có đặc tính của tụ điện.

## ATP synthase — ghép gradient với chuyển động cấu dạng

Proton đi xuống gradient qua phần `F0` của ATP synthase và gây chuyển động quay.

Chuyển động cơ học/cấu dạng trong `F1` làm thay đổi ái lực của vị trí xúc tác đối với ADP, `Pi` và ATP.

Chuỗi chuyển đổi năng lượng:

```text
oxy hóa chất dinh dưỡng
→ NADH/FADH2
→ truyền electron
→ gradient proton
→ chuyển động cơ học/cấu dạng
→ tổng hợp ATP
```

Đây là ví dụ rõ về sự ghép giữa hóa học, điện hóa và máy phân tử.

## Phosphoryl hóa oxy hóa và hiện tượng mất ghép

Chuỗi truyền electron và tổng hợp ATP được ghép qua gradient proton.

Nếu màng trở nên thấm proton, hiện tượng **mất ghép (uncoupling)** xảy ra:

```text
truyền electron vẫn chạy
nhưng gradient bị tiêu tán
→ tổng hợp ATP giảm
→ nhiệt tăng
```

UCP1 trong mô mỡ nâu khai thác cơ chế này để sinh nhiệt.

Hiện tượng mất ghép là bằng chứng mạnh cho cơ chế hóa thẩm.

## β-oxy hóa acid béo

Acid béo được hoạt hóa thành acyl-CoA rồi rút ngắn hai carbon mỗi vòng, tạo acetyl-CoA, NADH và FADH2.

Chuỗi lặp gồm:

```text
oxy hóa
→ hydrat hóa
→ oxy hóa
→ thiolysis
```

Acid béo chứa carbon ở trạng thái khử mạnh nên cho nhiều tương đương khử khi oxy hóa.

Mỡ cũng lưu ít nước hơn glycogen nên có mật độ năng lượng theo khối lượng cao hơn.

## Tổng hợp acid béo không phải β-oxy hóa chạy ngược

Sinh tổng hợp dùng enzyme khác, protein mang acyl, NADPH và phân ngăn khác.

Các bước không thuận nghịch được “đi vòng” bằng phản ứng riêng, giúp tránh hai con đường đối nghịch cùng chạy mạnh và lãng phí năng lượng.

Đây là nguyên lý chung: **đường dị hóa và đồng hóa thường khác nhau tại các bước xa cân bằng**.

## Chuyển hóa amino acid và nitrogen

Nhóm amino được chuyển qua phản ứng transamination, thường dùng PLP.

Nitrogen cuối cùng phải được xử lý vì ammonia tự do độc ở nồng độ cao.

Ở động vật có vú, chu trình urea chuyển nitrogen thành urea để bài tiết.

Khung carbon của amino acid đi vào mạng trung tâm tại pyruvate, acetyl-CoA hoặc chất trung gian TCA.

## Phản ứng gần cân bằng và xa cân bằng

Nhiều bước chuyển hóa hoạt động gần cân bằng và có thể đổi chiều khi tỉ lệ cơ chất/sản phẩm thay đổi.

Các bước điều hòa chính thường có `ΔG` thực âm mạnh và xa cân bằng.

Những bước này tạo hướng cho con đường và thường cần enzyme khác khi đi theo chiều ngược trong pathway đối nghịch.

Đây là cầu nối trực tiếp tới [cân bằng động](../07_chemical_equilibrium/00_dynamic_equilibrium.md).

## Điều hòa chuyển hóa

Thông lượng phụ thuộc nhiều tầng:

- mức sẵn có của cơ chất;
- ức chế bởi sản phẩm;
- chất điều hòa dị lập thể;
- biến đổi cộng hóa trị;
- lượng enzyme;
- phân ngăn;
- hormone và tín hiệu.

ATP cao thường ức chế một số điểm kiểm soát dị hóa; AMP/ADP báo hiệu nhu cầu năng lượng.

Điều hòa chuyển hóa về bản chất là **điều khiển phản hồi của mạng phản ứng hóa học**.

## Phân ngăn

Tế bào nhân thực tách các con đường theo không gian.

Ví dụ:

- đường phân: bào tương;
- TCA và phosphoryl hóa oxy hóa: chủ yếu ty thể;
- tổng hợp acid béo và β-oxy hóa: dùng vị trí và hệ enzyme khác nhau.

Phân ngăn cho phép duy trì pH, trạng thái redox, tỉ lệ chất chuyển hóa và tập enzyme khác nhau tại mỗi vùng.

Động lực nhiệt động vì vậy mang tính cục bộ, không được quyết định bởi một “nồng độ toàn tế bào” duy nhất.

## Thông lượng khác nồng độ

Một chất chuyển hóa có thể giữ nồng độ gần như không đổi trong khi lượng vật chất đi qua mỗi giây rất lớn, nếu tốc độ tạo và tiêu thụ gần bằng nhau.

Do đó:

```text
nồng độ ≠ thông lượng
biến trạng thái ≠ tốc độ dòng
```

**Phân tích thông lượng chuyển hóa (metabolic flux analysis)** thường dùng chất đánh dấu đồng vị như `13C` để theo dõi carbon qua mạng.

## Trạng thái ổn định ngoài cân bằng

Tế bào sống duy trì nhiều nồng độ gần ổn định dù phản ứng liên tục xảy ra.

Đây là **trạng thái ổn định (steady state)** chứ không phải cân bằng nhiệt động.

```text
equilibrium
→ không có dòng ròng

steady state sống
→ có dòng liên tục
→ nồng độ vẫn có thể gần ổn định
```

Sự sống duy trì tổ chức bằng cách liên tục tiêu thụ nguồn năng lượng tự do và thải entropy/nhiệt ra môi trường.

## Các loại oxygen phản ứng và hệ chống oxy hóa

Chuỗi truyền electron không hoàn toàn kín. Một phần electron có thể rò và khử oxygen không hoàn toàn, tạo superoxide và các loại oxygen phản ứng khác.

Tế bào dùng superoxide dismutase, catalase, glutathione và hệ phụ thuộc NADPH để kiểm soát stress oxy hóa.

ROS không hoàn toàn “xấu”; ở mức kiểm soát chúng còn tham gia tín hiệu. Vấn đề xuất hiện khi tốc độ tạo vượt khả năng trung hòa và sửa chữa.

## Chuyển hóa như đồ thị và ma trận hóa lượng

Mạng chuyển hóa có thể biểu diễn bằng đồ thị hoặc ma trận.

Nếu `S` là ma trận hóa lượng và `v` là vector thông lượng, trạng thái ổn định của chất trung gian thường được viết:

\[
S\mathbf{v}=0
\]

Đây là nền của **phân tích cân bằng thông lượng (flux balance analysis, FBA)**.

Phương trình này không tự cho một nghiệm duy nhất; cần thêm ràng buộc biên và thường cần một hàm mục tiêu hoặc dữ liệu thực nghiệm.

Xem nền toán/hóa lượng ở [Ma trận hóa lượng và mạng phản ứng](../04_chemical_quantities/06_stoichiometric_matrices_and_reaction_networks.md).

## Ví dụ suy luận: vì sao ATP cao không có nghĩa mọi phản ứng tổng hợp tự chạy?

ATP làm một phản ứng bất lợi trở nên khả thi chỉ khi có cơ chế ghép thật sự, ví dụ chuyển phosphate hoặc tạo chất trung gian chung.

Nếu hai phản ứng không được ghép về mặt cơ chế, chỉ đặt chúng cùng trong một dung dịch không làm `ΔG` tự cộng theo con đường mong muốn.

Do đó **thermodynamic coupling cần chemical coupling**.

## Ví dụ suy luận: vì sao nồng độ pyruvate ổn định không chứng minh glycolysis chậm?

Pyruvate có thể được tạo rất nhanh và đồng thời bị tiêu thụ rất nhanh.

Nếu hai tốc độ gần bằng nhau, nồng độ vẫn gần ổn định trong khi thông lượng lớn.

Muốn biết tốc độ mạng phải đo flux, không chỉ chụp nồng độ tại một thời điểm.

## Những hiểu lầm thường gặp

### “ATP lưu năng lượng trong một liên kết đặc biệt và giải phóng khi phá liên kết”

Không. Phá liên kết cần năng lượng; phản ứng tổng thể thuận lợi vì sản phẩm được ổn định tốt hơn.

### “NADH chính là ATP”

Không. NADH mang tương đương khử; oxy hóa NADH có thể được ghép gián tiếp với tạo ATP.

### “Lên men tạo rất nhiều ATP”

Không. Vai trò redox chính của lên men là tái sinh NAD+; ATP chủ yếu đến từ đường phân.

### “Chuyển hóa có xu hướng đạt cân bằng”

Tế bào duy trì trạng thái ổn định ngoài cân bằng với thông lượng liên tục.

### “Nồng độ cho biết mức hoạt động của con đường”

Không. Nồng độ là biến trạng thái; thông lượng là tốc độ dòng vật chất.

### “FBA dự đoán chính xác tốc độ chỉ từ stoichiometry”

Không. Stoichiometry xác định không gian nghiệm khả thi; dự đoán cụ thể cần thêm ràng buộc và giả định.

## Mô hình tư duy

Hãy xem chuyển hóa như **mạng chuyển đổi năng lượng và vật chất có dòng liên tục**:

```text
nguồn carbon / electron
→ enzyme và pathway
→ chất mang năng lượng / electron
→ gradient điện hóa
→ ATP + sinh tổng hợp + công tế bào
→ nhiệt + sản phẩm thải
```

Thermodynamics xác định động lực; kinetics xác định tốc độ; stoichiometry giới hạn quan hệ dòng; enzyme và tín hiệu điều khiển phân bố thông lượng.

Xem tiếp: [Hóa học môi trường](../16_environmental_chemistry/00_atmospheric_chemistry.md) để thấy cùng logic mạng phản ứng, redox và steady state ở một hệ lớn hơn tế bào.