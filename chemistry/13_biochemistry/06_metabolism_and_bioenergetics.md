# Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**. Route đi từ dị hóa/đồng hóa và thế hóa học → chất mang electron/ATP → gradient ion và ghép năng lượng → flux qua mạng phản ứng, điều hòa và cân bằng vật chất, để giải thích tế bào vận hành ngoài cân bằng mà vẫn giữ được tổ chức.

> **Chuyển hóa (metabolism / 대사)** là mạng phản ứng hóa học liên kết với nhau để biến đổi vật chất, lưu trữ/giải phóng năng lượng tự do và duy trì tổ chức tế bào. **Sinh năng lượng (bioenergetics / 생물에너지학)** nghiên cứu cách tế bào ghép phản ứng thuận lợi với phản ứng bất lợi, di chuyển electron, tạo độ dốc (gradient / 기울기) ion và biến độ dốc (gradient / 기울기) đó thành công hóa học.

Chuyển hóa không nên được học như danh sách con đường. Nó là một **mạng phản ứng ngoài cân bằng có ghép nối**, trong đó thông lượng thay đổi theo nguồn dinh dưỡng, trạng thái năng lượng và nhu cầu sinh tổng hợp.

Các prerequisite quan trọng:

- [Năng lượng tự do Gibbs](../05_thermodynamics/03_gibbs_free_energy.md) để hiểu `ΔG`, ghép phản ứng và động lực nhiệt động;
- [Cân bằng hóa học](../07_chemical_equilibrium/00_dynamic_equilibrium.md) để phân biệt equilibrium với steady trạng thái (state / 상태);
- [Điện thế pin và Nernst](../09_redox_and_electrochemistry/03_cell_potential_and_nernst_equation.md) để hiểu dòng electron và `ΔG = -nFΔE`;
- [Enzyme](./05_enzymes.md) để hiểu kiểm soát động học;
- [Ma trận hóa lượng và mạng phản ứng](../04_chemical_quantities/06_stoichiometric_matrices_and_reaction_networks.md) để hiểu thông lượng và FBA.

## Dị hóa và đồng hóa

**Dị hóa (catabolism / 이화작용)** phân giải phân tử giàu năng lượng thành sản phẩm nhỏ hơn và thu một phần năng lượng tự do vào ATP, NADH hoặc độ dốc (gradient / 기울기) ion.

**Đồng hóa (anabolism / 동화작용)** dùng năng lượng tự do và tiền chất để xây protein, acid nucleic, lipid, polysaccharide và các chất chuyển hóa chuyên biệt.

Hai hệ không độc lập. Dị hóa cung cấp năng lượng và khung carbon; nhu cầu đồng hóa lại điều chỉnh thông lượng dị hóa.

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Vì sao tế bào dùng nhiều bước thay vì một phản ứng khổng lồ?** nối từ **Dị hóa và đồng hóa** sang **Năng lượng tự do Gibbs trong tế bào**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao tế bào dùng nhiều bước thay vì một phản ứng khổng lồ?

Oxy hóa hoàn toàn glucose thành `CO2` và `H2O` rất thuận lợi về nhiệt động.

Nếu giải phóng toàn bộ năng lượng trong một bước không kiểm soát, phần lớn sẽ chuyển thành nhiệt và khó ghép vào công hữu ích.

Tế bào chia quá trình thành nhiều bước do enzyme xúc tác. Mỗi bước có thể:

- thu một phần năng lượng;
- tạo chất mang electron;
- tạo chất trung gian có thể chuyển sang đường khác;
- tạo điểm điều hòa.

Chuyển hóa vì vậy giống **hệ chuyển đổi năng lượng nhiều tầng** hơn là một lần “đốt cháy” duy nhất.

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Năng lượng tự do Gibbs trong tế bào** nối từ **Vì sao tế bào dùng nhiều bước thay vì một phản ứng khổng lồ?** sang **Ghép phản ứng — năng lượng tự do cộng được**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Ghép phản ứng — năng lượng tự do cộng được** nối từ **Năng lượng tự do Gibbs trong tế bào** sang **ATP — chất trung gian chuyển nhóm, không phải “pin năng lượng” cô lập**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **ATP — chất trung gian chuyển nhóm, không phải “pin năng lượng” cô lập** nối từ **Ghép phản ứng — năng lượng tự do cộng được** sang **Trạng thái năng lượng adenylate**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Trạng thái năng lượng adenylate** nối từ **ATP — chất trung gian chuyển nhóm, không phải “pin năng lượng” cô lập** sang **Cofactor oxy hóa–khử — mang electron dưới dạng hóa học**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Cofactor oxy hóa–khử — mang electron dưới dạng hóa học** nối từ **Trạng thái năng lượng adenylate** sang **Điện thế oxy hóa–khử và dòng electron**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Điện thế oxy hóa–khử và dòng electron** nối từ **Cofactor oxy hóa–khử — mang electron dưới dạng hóa học** sang **Đường phân — đọc bằng lô-gic (logic / 논리) hóa học thay vì thuộc mười tên phản ứng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Điện thế oxy hóa–khử và dòng electron

Điện thế khử thực tế phụ thuộc thành phần qua phương trình Nernst.

Về nhiệt động, electron có xu hướng truyền từ cặp có điện thế khử thấp hơn tới cặp có điện thế khử cao hơn.

Quan hệ:

\[
\Delta G=-nF\Delta E
\]

nối trực tiếp điện hóa với sinh năng lượng.

`O2` là chất nhận electron cuối mạnh trong hô hấp hiếu khí vì khử oxygen thành nước cho `ΔE` dương lớn và vì vậy `ΔG` âm đáng kể.

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Đường phân — đọc bằng lô-gic (logic / 논리) hóa học thay vì thuộc mười tên phản ứng** nối từ **Điện thế oxy hóa–khử và dòng electron** sang **Lên men — tái sinh NAD+**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đường phân — đọc bằng lô-gic (logic / 논리) hóa học thay vì thuộc mười tên phản ứng

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Lên men — tái sinh NAD+** nối từ **Đường phân — đọc bằng lô-gic (logic / 논리) hóa học thay vì thuộc mười tên phản ứng** sang **Oxy hóa pyruvate và acetyl-CoA**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lên men — tái sinh NAD+

Đường phân cần NAD+.

Nếu NADH không được oxy hóa lại, pool NAD+ cạn và đường phân dừng.

Lên men chuyển electron từ NADH sang phân tử hữu cơ có nguồn từ pyruvate.

Ví dụ lactate:

\[
pyruvate+NADH+H^+\rightarrow lactate+NAD^+
\]

Vai trò chính của lên men là **tái sinh NAD+**, không phải tạo lượng ATP lớn ngoài phần đã có từ đường phân.

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Oxy hóa pyruvate và acetyl-CoA** nối từ **Lên men — tái sinh NAD+** sang **Chu trình acid citric — vừa oxy hóa vừa cung cấp tiền chất**, vì cơ chế trước tạo đầu vào cho bước sau.

## Oxy hóa pyruvate và acetyl-CoA

Trong điều kiện hiếu khí, pyruvate được chuyển thành acetyl-CoA, đồng thời tạo `CO2` và NADH.

Coenzyme A tạo thioester có thế chuyển acyl cao.

Thioester được giải thích chi tiết ở [acid carboxylic và dẫn xuất](../11_organic_chemistry/08_carboxylic_acids_and_derivatives.md).

Acetyl-CoA là nút giao giữa carbohydrate, acid béo và amino acid.

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Chu trình acid citric — vừa oxy hóa vừa cung cấp tiền chất** nối từ **Oxy hóa pyruvate và acetyl-CoA** sang **Chuỗi truyền electron — biến năng lượng redox thành độ dốc (gradient / 기울기) proton**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chu trình acid citric — vừa oxy hóa vừa cung cấp tiền chất

Acetyl-CoA ngưng tụ với oxaloacetate rồi trải qua tái sắp xếp, oxy hóa và khử carboxyl.

Năng lượng được giữ trong NADH, FADH2 và GTP/ATP tương đương.

Chu trình còn cung cấp chất trung gian cho sinh tổng hợp nên được gọi là **amphibolic**.

Khi chất trung gian bị rút ra, **phản ứng bổ sung (anaplerotic reaction)** bù lại pool trung gian.

Do đó chu trình vừa là đường oxy hóa vừa là trung tâm phân phối carbon.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Chu trình acid citric — vừa oxy hóa vừa cung cấp tiền chất** đặt đầu vào cho **Chuỗi truyền electron — biến năng lượng redox thành độ dốc (gradient / 기울기) proton**, rồi **Động lực proton** mở rộng hệ quả hoặc giới hạn liên quan.

## Chuỗi truyền electron — biến năng lượng redox thành độ dốc (gradient / 기울기) proton

NADH cho electron vào chuỗi hô hấp ở màng trong ty thể.

Electron đi qua các chất mang có điện thế khử tăng dần về phía `O2`.

Một số phức hợp ghép chuyển electron thuận lợi với bơm proton ra khỏi ma trận (matrix / 행렬).

Chuỗi biến đổi:

```text
năng lượng redox
→ công bơm proton
→ gradient điện hóa
```

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Chuỗi truyền electron — biến năng lượng redox thành độ dốc (gradient / 기울기) proton** đặt đầu vào cho **Động lực proton**, rồi **ATP synthase — ghép độ dốc (gradient / 기울기) với chuyển động cấu dạng** mở rộng hệ quả hoặc giới hạn liên quan.

## Động lực proton

Độ dốc (gradient / 기울기) proton có hai thành phần:

1. chênh lệch hoạt độ proton;
2. chênh lệch điện thế màng.

Với ion điện tích `z`:

\[
\Delta\mu=RT\ln\frac{a_2}{a_1}+zF\Delta\psi
\]

Đây là **thế điện hóa**: tổng của đóng góp hóa học và điện.

Màng vì vậy vừa có đặc tính của pin nồng độ vừa có đặc tính của tụ điện.

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **ATP synthase — ghép độ dốc (gradient / 기울기) với chuyển động cấu dạng** nối từ **Động lực proton** sang **Phosphoryl hóa oxy hóa và hiện tượng mất ghép**, vì cơ chế trước tạo đầu vào cho bước sau.

## ATP synthase — ghép độ dốc (gradient / 기울기) với chuyển động cấu dạng

Proton đi xuống độ dốc (gradient / 기울기) qua phần `F0` của ATP synthase và gây chuyển động quay.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Phosphoryl hóa oxy hóa và hiện tượng mất ghép** nối từ **ATP synthase — ghép độ dốc (gradient / 기울기) với chuyển động cấu dạng** sang **β-oxy hóa acid béo**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phosphoryl hóa oxy hóa và hiện tượng mất ghép

Chuỗi truyền electron và tổng hợp ATP được ghép qua độ dốc (gradient / 기울기) proton.

Nếu màng trở nên thấm proton, hiện tượng **mất ghép (uncoupling)** xảy ra:

```text
truyền electron vẫn chạy
nhưng gradient bị tiêu tán
→ tổng hợp ATP giảm
→ nhiệt tăng
```

UCP1 trong mô mỡ nâu khai thác cơ chế này để sinh nhiệt.

Hiện tượng mất ghép là bằng chứng mạnh cho cơ chế hóa thẩm.

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **β-oxy hóa acid béo** nối từ **Phosphoryl hóa oxy hóa và hiện tượng mất ghép** sang **Tổng hợp acid béo không phải β-oxy hóa chạy ngược**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Tổng hợp acid béo không phải β-oxy hóa chạy ngược** tổng hợp từ **β-oxy hóa acid béo** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Chuyển hóa amino acid và nitrogen** mở rộng hệ quả hoặc giới hạn liên quan.

## Tổng hợp acid béo không phải β-oxy hóa chạy ngược

Sinh tổng hợp dùng enzyme khác, protein mang acyl, NADPH và phân ngăn khác.

Các bước không thuận nghịch được “đi vòng” bằng phản ứng riêng, giúp tránh hai con đường đối nghịch cùng chạy mạnh và lãng phí năng lượng.

Đây là nguyên lý chung: **đường dị hóa và đồng hóa thường khác nhau tại các bước xa cân bằng**.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Chuyển hóa amino acid và nitrogen** tổng hợp từ **Tổng hợp acid béo không phải β-oxy hóa chạy ngược** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Phản ứng gần cân bằng và xa cân bằng** mở rộng hệ quả hoặc giới hạn liên quan.

## Chuyển hóa amino acid và nitrogen

Nhóm amino được chuyển qua phản ứng transamination, thường dùng PLP.

Nitrogen cuối cùng phải được xử lý vì ammonia tự do độc ở nồng độ cao.

Ở động vật có vú, chu trình urea chuyển nitrogen thành urea để bài tiết.

Khung carbon của amino acid đi vào mạng trung tâm tại pyruvate, acetyl-CoA hoặc chất trung gian TCA.

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Phản ứng gần cân bằng và xa cân bằng** nối từ **Chuyển hóa amino acid và nitrogen** sang **Điều hòa chuyển hóa**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phản ứng gần cân bằng và xa cân bằng

Nhiều bước chuyển hóa hoạt động gần cân bằng và có thể đổi chiều khi tỉ lệ cơ chất/sản phẩm thay đổi.

Các bước điều hòa chính thường có `ΔG` thực âm mạnh và xa cân bằng.

Những bước này tạo hướng cho con đường và thường cần enzyme khác khi đi theo chiều ngược trong pathway đối nghịch.

Đây là cầu nối trực tiếp tới [cân bằng động](../07_chemical_equilibrium/00_dynamic_equilibrium.md).

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Điều hòa chuyển hóa** nối từ **Phản ứng gần cân bằng và xa cân bằng** sang **Phân ngăn**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Phân ngăn** nối từ **Điều hòa chuyển hóa** sang **Thông lượng khác nồng độ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phân ngăn

Tế bào nhân thực tách các con đường theo không gian.

Ví dụ:

- đường phân: bào tương;
- TCA và phosphoryl hóa oxy hóa: chủ yếu ty thể;
- tổng hợp acid béo và β-oxy hóa: dùng vị trí và hệ enzyme khác nhau.

Phân ngăn cho phép duy trì pH, trạng thái redox, tỉ lệ chất chuyển hóa và tập enzyme khác nhau tại mỗi vùng.

Động lực nhiệt động vì vậy mang tính cục bộ, không được quyết định bởi một “nồng độ toàn tế bào” duy nhất.

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Thông lượng khác nồng độ** nối từ **Phân ngăn** sang **Trạng thái ổn định ngoài cân bằng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thông lượng khác nồng độ

Một chất chuyển hóa có thể giữ nồng độ gần như không đổi trong khi lượng vật chất đi qua mỗi giây rất lớn, nếu tốc độ tạo và tiêu thụ gần bằng nhau.

Do đó:

```text
nồng độ ≠ thông lượng
biến trạng thái ≠ tốc độ dòng
```

**Phân tích thông lượng chuyển hóa (metabolic flux analysis)** thường dùng chất đánh dấu đồng vị như `13C` để theo dõi carbon qua mạng.

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Trạng thái ổn định ngoài cân bằng** nối từ **Thông lượng khác nồng độ** sang **Các loại oxygen phản ứng và hệ chống oxy hóa**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Các loại oxygen phản ứng và hệ chống oxy hóa** nối từ **Trạng thái ổn định ngoài cân bằng** sang **Chuyển hóa như đồ thị và ma trận hóa lượng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các loại oxygen phản ứng và hệ chống oxy hóa

Chuỗi truyền electron không hoàn toàn kín. Một phần electron có thể rò và khử oxygen không hoàn toàn, tạo superoxide và các loại oxygen phản ứng khác.

Tế bào dùng superoxide dismutase, catalase, glutathione và hệ phụ thuộc NADPH để kiểm soát stress oxy hóa.

ROS không hoàn toàn “xấu”; ở mức kiểm soát chúng còn tham gia tín hiệu. Vấn đề xuất hiện khi tốc độ tạo vượt khả năng trung hòa và sửa chữa.

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Chuyển hóa như đồ thị và ma trận hóa lượng** nối từ **Các loại oxygen phản ứng và hệ chống oxy hóa** sang **Ví dụ suy luận: vì sao ATP cao không có nghĩa mọi phản ứng tổng hợp tự chạy?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chuyển hóa như đồ thị và ma trận hóa lượng

Mạng chuyển hóa có thể biểu diễn bằng đồ thị hoặc ma trận.

Nếu `S` là ma trận hóa lượng và `v` là véc-tơ (vector / 벡터) thông lượng, trạng thái ổn định của chất trung gian thường được viết:

\[
S\mathbf{v}=0
\]

Đây là nền của **phân tích cân bằng thông lượng (flux balance analysis, FBA)**.

Phương trình này không tự cho một nghiệm duy nhất; cần thêm ràng buộc biên và thường cần một hàm mục tiêu hoặc dữ liệu thực nghiệm.

Xem nền toán/hóa lượng ở [Ma trận hóa lượng và mạng phản ứng](../04_chemical_quantities/06_stoichiometric_matrices_and_reaction_networks.md).

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Chuyển hóa như đồ thị và ma trận hóa lượng** nêu quy tắc; **Ví dụ suy luận: vì sao ATP cao không có nghĩa mọi phản ứng tổng hợp tự chạy?** thử quy tắc trong tình huống, rồi **Ví dụ suy luận: vì sao nồng độ pyruvate ổn định không chứng minh glycolysis chậm?** mở rộng hệ quả.

## Ví dụ suy luận: vì sao ATP cao không có nghĩa mọi phản ứng tổng hợp tự chạy?

ATP làm một phản ứng bất lợi trở nên khả thi chỉ khi có cơ chế ghép thật sự, ví dụ chuyển phosphate hoặc tạo chất trung gian chung.

Nếu hai phản ứng không được ghép về mặt cơ chế, chỉ đặt chúng cùng trong một dung dịch không làm `ΔG` tự cộng theo con đường mong muốn.

Do đó **thermodynamic coupling cần chemical coupling**.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Ví dụ suy luận: vì sao ATP cao không có nghĩa mọi phản ứng tổng hợp tự chạy?** nêu quy tắc; **Ví dụ suy luận: vì sao nồng độ pyruvate ổn định không chứng minh glycolysis chậm?** thử quy tắc trong tình huống, rồi **Những hiểu lầm thường gặp** mở rộng hệ quả.

## Ví dụ suy luận: vì sao nồng độ pyruvate ổn định không chứng minh glycolysis chậm?

Pyruvate có thể được tạo rất nhanh và đồng thời bị tiêu thụ rất nhanh.

Nếu hai tốc độ gần bằng nhau, nồng độ vẫn gần ổn định trong khi thông lượng lớn.

Muốn biết tốc độ mạng phải đo flux, không chỉ chụp nồng độ tại một thời điểm.

> **Nối mạch:** Trong **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Ví dụ suy luận: vì sao nồng độ pyruvate ổn định không chứng minh glycolysis chậm?** nêu quy tắc; **Những hiểu lầm thường gặp** thử quy tắc trong tình huống, rồi **Mô hình tư duy** mở rộng hệ quả.

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

> **Nối mạch:** Ở chặng này của **Chuyển hóa và sinh năng lượng — mạng phản ứng được vận hành bởi dòng năng lượng tự do**, **Mô hình tư duy** tổng hợp từ **Những hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

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

Xem tiếp: [Hóa học môi trường](../16_environmental_chemistry/00_atmospheric_chemistry.md) để thấy cùng lô-gic (logic / 논리) mạng phản ứng, redox và steady trạng thái (state / 상태) ở một hệ lớn hơn tế bào.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
