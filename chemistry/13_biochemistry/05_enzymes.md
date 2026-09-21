# Enzyme — chất xúc tác phân tử và kiểm soát động học

> **Enzyme (효소)** là chất xúc tác sinh học làm tăng tốc phản ứng bằng cách hạ hàng rào năng lượng tự do hoạt hóa nhưng không thay đổi nhiệt động lực học tổng thể của phản ứng. Phần lớn enzyme là protein, nhưng RNA xúc tác (**ribozyme**) cho thấy khả năng xúc tác là tính chất của cấu trúc và động lực học phân tử, không phải đặc quyền của protein.

Enzyme không “cung cấp năng lượng” cho phản ứng. Nó tạo một vi môi trường trong đó trạng thái chuyển tiếp có thể đạt được qua con đường có hàng rào thấp hơn.

Trước khi đọc sâu, nên nối lại các prerequisite:

- [Năng lượng tự do Gibbs](../05_thermodynamics/03_gibbs_free_energy.md) để hiểu `ΔG`, cân bằng và hàng rào năng lượng;
- [Động học phản ứng](../06_chemical_kinetics/00_reaction_rates.md) và [cơ chế phản ứng](../06_chemical_kinetics/02_reaction_mechanisms.md) để hiểu rate law, trạng thái chuyển tiếp và trạng thái ổn định;
- [Acid–base](../08_acids_bases/00_acid_base_models.md) để hiểu proton transfer và `pKa` cục bộ;
- [Hóa học phối trí](../10_inorganic_chemistry/03_coordination_chemistry.md) để hiểu cofactor kim loại;
- [Lực liên phân tử](../02_chemical_bonding/07_intermolecular_forces.md) để hiểu nhận diện cơ chất và ổn định trạng thái chuyển tiếp.

## Nhiệt động lực học và động học — nguyên lý đầu tiên

Với phản ứng:

\[
S\rightleftharpoons P
\]

hằng số cân bằng phụ thuộc chênh lệch năng lượng tự do chuẩn:

\[
\Delta G^\circ=-RT\ln K
\]

Enzyme không thay `ΔG°` hay `K`. Nó hạ năng lượng tự do hoạt hóa cho cả chiều thuận lẫn chiều nghịch.

```text
không enzyme → hàng rào hoạt hóa cao
có enzyme     → con đường thay thế có hàng rào thấp hơn

ΔG giữa chất đầu và sản phẩm: không đổi
K cân bằng:                 không đổi
thời gian đạt cân bằng:     thay đổi mạnh
```

Nếu cân bằng ưu tiên cơ chất, thêm enzyme chỉ làm hệ đạt cân bằng nhanh hơn; nó không ép sản phẩm vượt giới hạn nhiệt động.

## Vị trí hoạt động là một vi môi trường hóa học

**Vị trí hoạt động (active site / 활성 부위)** không chỉ là “lỗ vừa với cơ chất”. Đây là môi trường được tổ chức gồm residue xúc tác, nước liên kết, ion kim loại, cofactor và trường tĩnh điện.

Các tính chất cục bộ có thể khác dung dịch khối:

- hằng số điện môi hiệu dụng khác;
- `pKa` của residue bị dịch;
- nước có thể bị loại ra hoặc định vị chính xác;
- cấu dạng cơ chất bị giới hạn;
- điện tích của trạng thái chuyển tiếp được ổn định chọn lọc.

Vì vậy xúc tác enzyme có thể được nhìn như **kỹ thuật môi trường phản ứng ở thang nanomet**.

## Các chiến lược xúc tác

### Hiệu ứng gần nhau và định hướng

Hai chất phản ứng trong dung dịch phải va chạm với hình học phù hợp. Enzyme đưa các nhóm phản ứng lại gần, giảm chi phí entropy định hướng và tăng xác suất va chạm hữu ích.

Điều này không có nghĩa “đưa gần nhau là đủ”; cấu dạng và hướng orbital vẫn phải phù hợp với cơ chế.

### Xúc tác acid–base tổng quát

Residue như histidine, aspartate, glutamate, lysine, cysteine hoặc tyrosine có thể cho hoặc nhận proton.

`pKa` hiệu dụng của chúng có thể khác amino acid tự do vì điện tích lân cận, liên kết hydrogen và mức tiếp xúc dung môi.

Histidine đặc biệt linh hoạt vì trạng thái proton hóa của nó thường nằm gần vùng pH sinh lý, cho phép vừa cho vừa nhận proton trong các bước khác nhau.

### Xúc tác cộng hóa trị

Enzyme có thể tạm thời tạo liên kết cộng hóa trị với cơ chất, mở một con đường phản ứng khác.

Ví dụ:

- serine protease tạo chất trung gian acyl–enzyme;
- lysine có thể tạo base Schiff;
- cysteine thiolate có thể làm tác nhân ái nhân mạnh.

Liên kết tạm thời phải được phá ở bước sau để tái sinh enzyme; nếu không, enzyme trở thành thuốc thử hóa lượng chứ không còn là chất xúc tác.

### Xúc tác ion kim loại

Kim loại có thể:

- hoạt động như acid Lewis;
- ổn định điện tích âm;
- định hướng cơ chất;
- hoạt hóa nước;
- tham gia chuyển electron.

`Zn2+` trong carbonic anhydrase làm giảm `pKa` hiệu dụng của nước phối trí, tạo hydroxide ái nhân gần `CO2`.

Tâm Fe/Cu có thể tham gia chuyển electron hoặc hoạt hóa `O2`.

Đây là cầu nối trực tiếp giữa enzyme học và hóa học phối trí.

### Ổn định trạng thái chuyển tiếp

Vị trí hoạt động thường bổ sung hình học và điện tích tốt hơn cho trạng thái chuyển tiếp so với cơ chất ở trạng thái cơ bản.

Nếu enzyme liên kết cơ chất quá mạnh ở cấu trúc bền ban đầu, nó có thể làm hố năng lượng cơ chất sâu hơn và vô tình tăng hàng rào tương đối.

Một chất xúc tác tốt vì vậy cần ưu tiên **ổn định trạng thái chuyển tiếp**, không chỉ “giữ cơ chất chặt”.

### Loại bớt solvat hóa

Một tác nhân ái nhân mang điện trong nước được ổn định mạnh bởi lớp solvat hóa.

Loại một phần dung môi có thể làm nó phản ứng mạnh hơn nếu vị trí hoạt động thay thế các tương tác bị mất bằng tương tác có định hướng phù hợp.

Enzyme vì vậy có thể đổi solvat hóa khối lấy môi trường phản ứng được tổ chức chính xác hơn.

## Năng lượng liên kết, khớp cảm ứng và ensemble cấu dạng

Mô hình **ổ khóa–chìa khóa (lock-and-key)** diễn đạt được độ chọn lọc nhưng quá cứng.

Protein liên tục dao động giữa nhiều cấu dạng. Cơ chất có thể ưu tiên một số cấu dạng có sẵn rồi làm hệ điều chỉnh thêm — kết hợp giữa **chọn lọc cấu dạng (conformational selection)** và **khớp cảm ứng (induced fit)**.

Enzyme vì vậy là một **ensemble động**, không phải cấu trúc bất động.

## Mô hình Michaelis–Menten

Một sơ đồ tối giản:

\[
E+S\xrightleftharpoons[k_{-1}]{k_1}ES\xrightarrow{k_{cat}}E+P
\]

Với điều kiện tốc độ ban đầu và giả định trạng thái ổn định:

\[
v=\frac{V_{max}[S]}{K_M+[S]}
\]

trong đó:

\[
V_{max}=k_{cat}[E]_T
\]

và:

\[
K_M=\frac{k_{-1}+k_{cat}}{k_1}
\]

Phương trình này không phải định luật phổ quát của mọi enzyme. Nó là kết quả của **một mô hình cơ chế cụ thể + tập giả định cụ thể**.

### Khi nồng độ cơ chất thấp

Nếu:

\[
[S]\ll K_M
\]

thì:

\[
v\approx\frac{V_{max}}{K_M}[S]
\]

Tốc độ gần bậc một theo cơ chất.

### Khi nồng độ cơ chất cao

Nếu:

\[
[S]\gg K_M
\]

thì:

\[
v\approx V_{max}
\]

Phần lớn vị trí hoạt động đã bị chiếm; thêm cơ chất làm tốc độ tăng rất ít.

### Khi [S] = KM

\[
v=\frac{V_{max}}2
\]

Quan hệ này giúp `KM` dễ diễn giải thực nghiệm, nhưng không có nghĩa `KM` luôn là hằng số ái lực.

## KM không đồng nhất với ái lực liên kết

Hằng số Michaelis:

\[
K_M=\frac{k_{-1}+k_{cat}}{k_1}
\]

trong khi hằng số phân ly cơ chất:

\[
K_D=\frac{k_{-1}}{k_1}
\]

Chỉ khi:

\[
k_{cat}\ll k_{-1}
\]

thì:

\[
K_M\approx K_D
\]

Vì vậy `KM` là tham số động học tổng hợp chứ không phải “ái lực” phổ quát.

## Số vòng xúc tác và hiệu suất xúc tác

\[
k_{cat}=\frac{V_{max}}{[E]_T}
\]

cho biết số phân tử cơ chất tối đa mà một vị trí hoạt động chuyển hóa trong một đơn vị thời gian khi bão hòa.

Ở nồng độ cơ chất thấp, đại lượng hữu ích là:

\[
\frac{k_{cat}}{K_M}
\]

Nó kết hợp khả năng bắt cơ chất với tốc độ chuyển hóa.

Một số enzyme đạt giá trị gần giới hạn khuếch tán khoảng:

\[
10^8-10^9\;M^{-1}s^{-1}
\]

Khi đó cải thiện hóa học nội tại thêm nữa không giúp nhiều nếu bước chậm đã trở thành việc cơ chất khuếch tán tới enzyme.

Đây là cầu nối tới [khuếch tán trong chất lỏng](../03_matter_and_phases/01_liquids.md) và [giới hạn vận chuyển trong động học](../06_chemical_kinetics/04_catalysis.md).

## Ý tưởng trạng thái ổn định

Với phức `ES`:

\[
\frac{d[ES]}{dt}=k_1[E][S]-(k_{-1}+k_{cat})[ES]
\]

Giả định trạng thái ổn định nói rằng sau giai đoạn đầu ngắn:

\[
\frac{d[ES]}{dt}\approx0
\]

`ES` vẫn liên tục được tạo và tiêu thụ, nhưng hai tốc độ gần cân bằng nhau.

Điều này **không đồng nghĩa cân bằng nhiệt động**. Đây là trạng thái ổn định động học của một chất trung gian.

Xem thêm [cơ chế phản ứng và steady-state approximation](../06_chemical_kinetics/02_reaction_mechanisms.md).

## Ức chế enzyme

Chất ức chế vừa là công cụ cơ chế vừa là nền của dược lý học.

### Ức chế cạnh tranh

Chất ức chế cạnh tranh với cơ chất để liên kết enzyme tự do.

Trong mô hình lý tưởng:

- `KM` biểu kiến tăng;
- `Vmax` không đổi.

Nồng độ cơ chất cao có thể cạnh tranh lại vì cả cơ chất và chất ức chế cùng nhắm enzyme tự do.

### Ức chế uncompetitive

Chất ức chế chỉ liên kết phức `ES`.

Trong mô hình lý tưởng:

- `KM` biểu kiến giảm;
- `Vmax` giảm cùng hệ số.

### Ức chế hỗn hợp

Chất ức chế có thể liên kết cả `E` và `ES` với ái lực khác nhau.

`Vmax` giảm; `KM` biểu kiến có thể tăng hoặc giảm tùy trạng thái nào được ưu tiên.

### Ức chế không cạnh tranh thuần túy

Đây là trường hợp đặc biệt của ức chế hỗn hợp khi chất ức chế liên kết `E` và `ES` tương đương nhau.

Khi đó `Vmax` giảm còn `KM` gần như không đổi trong mô hình lý tưởng.

Enzyme thật thường có hành vi phức tạp hơn các nhãn hoàn hảo này.

## Ức chế không thuận nghịch

Một số chất ức chế tạo liên kết cộng hóa trị hoặc làm enzyme mất hoạt tính lâu hơn thang thời gian thí nghiệm.

Trong trường hợp này, hằng số cân bằng `Ki` đơn giản không đủ; các tham số phụ thuộc thời gian như `kinact` và hằng số liên kết biểu kiến trở nên quan trọng.

Nhiều thuốc khai thác ức chế cộng hóa trị có chủ đích, nhưng trade-off là phải đạt độ chọn lọc cao để tránh phản ứng ngoài mục tiêu.

## Lineweaver–Burk và giới hạn của tuyến tính hóa

Lấy nghịch đảo Michaelis–Menten:

\[
\frac1v=\frac{K_M}{V_{max}}\frac1{[S]}+\frac1{V_{max}}
\]

tạo đồ thị Lineweaver–Burk.

Cách này hữu ích về lịch sử và trực quan hóa, nhưng phép nghịch đảo khuếch đại sai số ở nồng độ cơ chất thấp.

Phân tích hiện đại thường khớp trực tiếp mô hình phi tuyến.

Đây là bài học thống kê quan trọng: **biến đổi đại số thành đường thẳng không đồng nghĩa tạo ước lượng tốt hơn**.

## Dị lập thể và tính hợp tác

Nhiều enzyme điều hòa có nhiều tiểu đơn vị hoặc nhiều vị trí liên kết và không tuân Michaelis–Menten đơn giản.

Đường cong sigmoidal có thể xuất hiện do **tính hợp tác (cooperativity)**, khi liên kết tại một vị trí làm thay đổi phân bố cấu dạng và ái lực/hoạt tính ở vị trí khác.

Phương trình Hill thường dùng như mô hình hiện tượng:

\[
\theta=\frac{[L]^{n_H}}{K_{0.5}^{n_H}+[L]^{n_H}}
\]

`nH > 1` gợi ý tính hợp tác dương, nhưng `nH` không tự động bằng số vị trí liên kết thật.

### Mô hình MWC như cách nhìn ensemble

Trong mô hình Monod–Wyman–Changeux, protein có thể phân bố giữa trạng thái kiểu `T` và `R`.

Ligand ưu tiên một trạng thái và làm phân bố dân số cấu dạng dịch chuyển.

Dị lập thể vì vậy có thể được hiểu như **tái phân bố ensemble cấu dạng**, không phải công tắc cơ học cứng.

## Phụ thuộc pH

Residue xúc tác phải có trạng thái proton hóa phù hợp.

Nếu một nhóm phải proton hóa còn nhóm khác phải khử proton, hoạt tính có thể tạo đường cong hình chuông theo pH.

pH tối ưu quan sát được phụ thuộc:

- `pKa` của residue xúc tác;
- trạng thái ion hóa cơ chất;
- độ bền protein;
- bước giới hạn tốc độ.

Vì vậy “pH tối ưu” không phải một con số cố định độc lập với điều kiện.

## Phụ thuộc nhiệt độ

Tốc độ phản ứng sơ cấp thường tăng theo nhiệt độ theo logic Arrhenius/Eyring.

Nhưng protein đồng thời có thể mất cấu trúc hoạt động khi nhiệt độ tăng.

Hoạt tính quan sát là kết quả cạnh tranh:

```text
nhiệt độ tăng
→ phản ứng hóa học nhanh hơn
nhưng đồng thời
→ xác suất mất cấu trúc hoạt động tăng
```

Do đó nhiệt độ tối ưu không phải bằng chứng rằng enzyme “thích” một nhiệt độ theo nghĩa đơn giản; nó là điểm cân bằng giữa động học và ổn định cấu trúc.

## Cofactor và coenzyme

Nhiều enzyme cần thành phần ngoài protein.

### Cofactor kim loại

Các ion thường gặp gồm Zn, Mg, Fe, Cu và Mn.

### Coenzyme

Các coenzyme quan trọng gồm NAD+, FAD, PLP, CoA, thiamine pyrophosphate và biotin.

Coenzyme mở rộng không gian phản ứng mà chuỗi bên amino acid có thể thực hiện.

Ví dụ:

- NAD+ chuyển tương đương hydride;
- PLP ổn định chất trung gian dạng carbanion;
- biotin mang `CO2` đã được hoạt hóa;
- CoA mang nhóm acyl.

Nhiều vitamin là tiền chất coenzyme, giải thích vì sao phân tử dinh dưỡng nhỏ có thể ảnh hưởng mạng chuyển hóa rất rộng.

## Độ đặc hiệu enzyme

Độ đặc hiệu xuất phát từ tổng hợp của:

- tương tác liên kết;
- hình học;
- động lực cấu dạng;
- trạng thái proton hóa;
- ổn định trạng thái chuyển tiếp.

Vì protein có tính đối quang, vị trí hoạt động có thể phân biệt enantiomer và hai mặt của phân tử tiền đối quang.

Độ đặc hiệu hiếm khi tuyệt đối. Enzyme có thể nhận chất tương tự hoặc thực hiện phản ứng phụ; tiến hóa và công nghệ sinh học có thể khai thác chính tính mềm dẻo này.

## Kỹ thuật enzyme

**Tiến hóa định hướng (directed evolution)** lặp lại chu trình tạo biến thể và chọn lọc để tăng hoạt tính, độ chọn lọc hoặc độ bền.

Thiết kế dựa trên cấu trúc/cơ chế có thể thay residue ở vị trí hoạt động.

Máy học có thể giúp ưu tiên biến thể trình tự, nhưng sàng lọc thực nghiệm vẫn thiết yếu vì cảnh quan năng lượng protein và tương tác epistasis rất phức tạp.

## Đo động học enzyme đúng cách

Một thí nghiệm đáng tin cậy phải kiểm soát:

- nồng độ cơ chất;
- tổng nồng độ enzyme;
- nhiệt độ;
- pH và hệ đệm;
- lực ion;
- khoảng tốc độ ban đầu;
- ức chế bởi sản phẩm;
- phản ứng nghịch;
- độ bền enzyme trong thời gian đo.

Tốc độ ban đầu thường được dùng để giảm ảnh hưởng của cạn cơ chất và tích lũy sản phẩm.

## Ví dụ suy luận: vì sao enzyme có KM thấp chưa chắc “tốt hơn”?

`KM` thấp có thể xuất hiện vì cơ chất liên kết thuận lợi, nhưng hiệu quả xúc tác còn phụ thuộc `kcat`.

Một enzyme giữ cơ chất rất chặt nhưng chuyển hóa rất chậm có thể có `KM` thấp mà thông lượng phản ứng vẫn thấp.

Ở nồng độ cơ chất thấp, `kcat/KM` thường có ý nghĩa so sánh hơn một mình `KM`.

## Ví dụ suy luận: vì sao tăng nồng độ enzyme không làm thay đổi cân bằng?

Tăng enzyme làm cả chiều thuận và chiều nghịch đạt trạng thái cân bằng nhanh hơn.

Nếu trạng thái cuối được quyết định bởi `ΔG` và `K`, thêm chất xúc tác không làm thay đổi tỉ lệ cân bằng.

Đây là cách kiểm tra trực tiếp sự khác biệt giữa **kinetics** và **thermodynamics**.

## Những hiểu lầm thường gặp

### “Enzyme làm thay đổi cân bằng”

Không. Nó thay tốc độ và con đường phản ứng.

### “KM là ái lực liên kết”

Chỉ gần đúng trong một số giới hạn động học.

### “Chất ức chế cạnh tranh luôn nằm đúng vị trí cơ chất”

Không nhất thiết. Mô hình động học chỉ yêu cầu nó cạnh tranh với cơ chất về trạng thái enzyme tự do; hình học liên kết thật có thể phức tạp hơn.

### “Ổ khóa–chìa khóa là mô hình đầy đủ”

Không. Protein là ensemble cấu dạng động và trạng thái chuyển tiếp mới là mục tiêu ổn định quan trọng.

### “Nhiệt độ càng cao enzyme càng hoạt động mạnh”

Chỉ đúng trong vùng protein vẫn duy trì đủ cấu trúc hoạt động.

### “Steady state nghĩa là equilibrium”

Không. Trạng thái ổn định có thể có dòng vật chất liên tục; cân bằng nhiệt động không có dòng ròng.

## Mô hình tư duy

Hãy xem enzyme như **một vi môi trường phản ứng động**:

```text
nhận diện cơ chất
+ tổ chức hình học
+ proton transfer
+ tĩnh điện
+ cofactor / kim loại
+ động lực cấu dạng
→ hạ chọn lọc hàng rào trạng thái chuyển tiếp
→ tăng tốc phản ứng
```

Các phương trình động học là mô hình nén hành vi của hệ này, không phải định nghĩa đầy đủ enzyme.

Xem tiếp: [Chuyển hóa và sinh năng lượng](./06_metabolism_and_bioenergetics.md), nơi nhiều enzyme được ghép thành mạng phản ứng và gradient năng lượng.