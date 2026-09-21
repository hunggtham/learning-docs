# Polymer — khi kiến trúc chuỗi trở thành tính chất vật liệu

> **Polymer (고분자)** là đại phân tử được tạo từ nhiều đơn vị lặp hoặc nhiều đơn vị có quan hệ cấu trúc. Chỉ biết loại monomer chưa đủ để dự đoán vật liệu cuối cùng. Tính chất xuất hiện từ **chiều dài chuỗi, kiến trúc chuỗi, lập thể, lực liên phân tử, độ kết tinh, sự vướng chuỗi, liên kết ngang và tốc độ chuyển động phân tử theo thời gian**.

Vật liệu polymer vì vậy không chỉ là “một phân tử rất lớn”. Nó là quần thể chuỗi dài có phân bố kích thước, cấu dạng và cách sắp xếp khác nhau. Hành vi tập thể của quần thể này tạo độ dẻo, độ đàn hồi, độ nhớt, độ bền và khả năng gia công.

Các prerequisite quan trọng gồm [liên kết cộng hóa trị](../02_chemical_bonding/02_covalent_bonding.md), [lực liên phân tử](../02_chemical_bonding/07_intermolecular_forces.md), [chất rắn](../03_matter_and_phases/02_solids.md), [nhiệt động lực học](../05_thermodynamics/04_chemical_thermodynamics.md) và [động học](../06_chemical_kinetics/00_reaction_rates.md).

## Vì sao chiều dài chuỗi làm vật liệu đổi bản chất?

Phân tử nhỏ có thể khuếch tán và tái sắp xếp tương đối tự do. Khi chuỗi dài lên, chúng bắt đầu xuyên qua và **vướng vào nhau (entanglement)**.

Một đoạn chuỗi muốn di chuyển phải phối hợp với nhiều đoạn lân cận. Thời gian thư giãn tăng mạnh và vật liệu xuất hiện **tính đàn nhớt (viscoelasticity)**: có thể phản ứng giống chất rắn đàn hồi hoặc chất lỏng nhớt tùy thang thời gian quan sát.

Khi khối lượng phân tử vượt ngưỡng vướng chuỗi, nhiều tính chất cơ học tăng mạnh rồi dần bão hòa. Dưới ngưỡng đó, vật liệu có thể mềm, yếu hoặc giống sáp hơn.

## Kiến trúc chuỗi

Chuỗi có thể có nhiều kiến trúc:

- thẳng;
- phân nhánh;
- hình sao;
- dạng lược;
- mạng liên kết ngang;
- copolymer khối hoặc ghép.

Kiến trúc quyết định khả năng đóng gói và chuyển động.

HDPE có chuỗi tương đối thẳng nên đóng gói tốt và kết tinh mạnh hơn. LDPE có nhiều nhánh nên đóng gói kém hơn, mật độ thấp hơn và mềm hơn. Epoxy sau đóng rắn tạo mạng liên kết ngang nên không thể nóng chảy lại giống **nhựa nhiệt dẻo (thermoplastic)** thông thường.

## Trùng hợp tăng trưởng chuỗi

Trong **trùng hợp tăng trưởng chuỗi (chain-growth polymerization / 연쇄 중합)**, một tâm hoạt động ở đầu chuỗi liên tục cộng monomer.

### Khơi mào

Chất khơi mào tạo gốc:

\[
I\rightarrow2R^\bullet
\]

Gốc cộng vào liên kết đôi của monomer và tạo đầu chuỗi hoạt động mới.

### Phát triển mạch

\[
P_n^\bullet+M\rightarrow P_{n+1}^\bullet
\]

Sau mỗi bước, tâm hoạt động vẫn tồn tại ở đầu chuỗi.

### Kết thúc và chuyển mạch

Hai gốc có thể kết hợp hoặc xảy ra disproportionation, làm mất tâm hoạt động.

Ngoài ra có **chuyển mạch (chain transfer)**, trong đó tâm hoạt động chuyển sang phân tử khác và làm thay đổi phân bố chiều dài chuỗi.

Vì vậy phân bố khối lượng phân tử phụ thuộc đồng thời tốc độ khơi mào, phát triển, kết thúc và chuyển mạch.

### Các cơ chế tăng trưởng chuỗi khác

Trùng hợp cation và anion sử dụng tâm hoạt động mang điện tích.

**Trùng hợp sống (living polymerization)** hạn chế kết thúc và chuyển mạch không thuận nghịch. Nếu số chuỗi gần như cố định, có thể kiểm soát khối lượng phân tử và tạo copolymer khối chính xác hơn.

Xúc tác Ziegler–Natta hoặc metallocene còn có thể điều khiển cách monomer chèn vào chuỗi và nhờ đó điều khiển **độ trật tự lập thể dọc mạch (tacticity)**.

## Trùng hợp tăng trưởng bậc

Trong **trùng hợp tăng trưởng bậc (step-growth polymerization / 단계 성장 중합)**, bất kỳ hai phân tử có nhóm chức tương thích đều có thể phản ứng: monomer–monomer, monomer–oligomer hoặc oligomer–oligomer.

Ví dụ:

- diacid + diol → polyester;
- dẫn xuất diacid + diamine → polyamide;
- diisocyanate + polyol → polyurethane.

Khác với tăng trưởng chuỗi, khối lượng phân tử rất cao chỉ xuất hiện khi độ chuyển hóa nhóm chức đã cực lớn.

### Phương trình Carothers

Với monomer hai chức lý tưởng và độ chuyển hóa `p`:

\[
X_n=\frac1{1-p}
\]

Nếu `p = 0.90`, `Xn = 10`. Nếu `p = 0.99`, `Xn = 100`. Muốn `Xn ≈ 1000`, cần `p ≈ 0.999`.

Điều này cho thấy chỉ một sai lệch nhỏ về độ chuyển hóa hoặc tỉ lệ nhóm chức cũng có thể giới hạn mạnh chiều dài chuỗi.

## Copolymer — dùng trình tự monomer để lập trình vật liệu

Khi dùng nhiều loại monomer, có thể tạo:

- copolymer ngẫu nhiên;
- copolymer xen kẽ;
- copolymer khối;
- copolymer ghép.

Trong copolymer khối, các đoạn không tương hợp có xu hướng tách pha. Nhưng vì chúng vẫn nối với nhau bằng liên kết cộng hóa trị, tách pha chỉ xảy ra ở kích thước nano.

Kết quả có thể là miền hình cầu, trụ hoặc lớp mỏng.

Đây là ví dụ rõ ràng cho chuỗi:

```text
hóa học monomer
→ kiến trúc chuỗi
→ tự lắp ghép trung mô
→ tính chất vật liệu
```

## Polymer không có một “khối lượng phân tử” duy nhất

Mẫu polymer thật thường có phân bố chiều dài chuỗi.

Khối lượng phân tử trung bình theo số:

\[
M_n=\frac{\sum N_iM_i}{\sum N_i}
\]

Khối lượng phân tử trung bình theo khối lượng:

\[
M_w=\frac{\sum N_iM_i^2}{\sum N_iM_i}
\]

Thông thường:

\[
M_w\ge M_n
\]

Độ phân tán:

\[
Đ=\frac{M_w}{M_n}
\]

Khi nói “khối lượng phân tử polymer”, phải nói rõ đang dùng `Mn`, `Mw` hay đại lượng nào khác.

## Cấu dạng chuỗi — polymer là đối tượng thống kê

Các liên kết đơn cho phép rất nhiều góc quay, nên một chuỗi có số cấu dạng khổng lồ.

Trong mô hình cuộn ngẫu nhiên lý tưởng:

\[
R\propto\sqrt N
\]

với `N` là số đoạn thống kê.

Đây là liên hệ trực tiếp giữa vật lý polymer và bước đi ngẫu nhiên trong xác suất.

Chuỗi thật còn chịu ảnh hưởng của thể tích loại trừ, độ cứng mạch và chất lượng dung môi, nên quan hệ tỉ lệ có thể khác mô hình lý tưởng.

## Sự vướng chuỗi và chuyển động reptation

Chuỗi dài không thể đi xuyên qua nhau. Chúng bị ràng buộc tô-pô bởi các chuỗi lân cận và tạo mạng vướng.

Ở thang thời gian ngắn, điểm vướng hành xử gần giống liên kết ngang tạm thời.

Ở thời gian dài hơn và nhiệt độ đủ cao, chuỗi có thể trượt dọc một “ống” hiệu dụng do các chuỗi xung quanh tạo ra. Chuyển động này gọi là **reptation**.

Đây là lý do độ nhớt của polymer nóng chảy tăng rất mạnh khi khối lượng phân tử vượt ngưỡng vướng chuỗi.

## Chuyển thủy tinh Tg

**Chuyển thủy tinh (glass transition / 유리전이)** không phải nóng chảy cân bằng bậc nhất.

Đó là vùng nhiệt độ nơi chuyển động phối hợp của các đoạn chuỗi trở nên đủ nhanh trên thang thời gian phép đo.

Dưới `Tg`, chuyển động đoạn mạch chậm; vật liệu thường cứng và dễ giòn hơn.

Trên `Tg`, các đoạn mạch có nhiều tự do hơn; vật liệu có thể mềm, dai hoặc cao su tùy kiến trúc.

Vì đây là hiện tượng động học, `Tg` quan sát được phụ thuộc tốc độ gia nhiệt và tần số phép đo.

Cùng một polymer có thể trông cứng dưới tác động rất nhanh nhưng mềm hơn dưới tải kéo dài.

## Nóng chảy Tm và độ kết tinh

Polymer bán tinh thể chứa cả vùng tinh thể có trật tự và vùng vô định hình.

Vùng tinh thể có thể nóng chảy gần `Tm`, còn vùng vô định hình thể hiện `Tg`.

Khả năng kết tinh tăng khi chuỗi có cấu trúc đều, ít nhánh và lập thể có trật tự.

Độ kết tinh thường làm tăng mật độ, độ cứng, độ bền hóa học và khả năng cản khuếch tán, nhưng có thể làm vật liệu đục hơn hoặc giảm độ dai va đập.

### Tacticity — lập thể dọc chuỗi

Với polymer vinyl có nhóm thế, thường phân biệt:

- isotactic;
- syndiotactic;
- atactic.

Trật tự lập thể tốt giúp chuỗi đóng gói đều hơn và thuận lợi cho kết tinh.

## Liên kết ngang

Liên kết ngang cộng hóa trị nối các chuỗi và hạn chế dòng chảy vĩnh viễn.

Mật độ liên kết ngang thấp tạo **chất đàn hồi (elastomer)**: chuỗi có thể kéo giãn nhưng mạng giữ chúng lại và tạo khả năng hồi phục.

Mật độ liên kết ngang cao tạo **nhựa nhiệt rắn (thermoset)**: mạng ba chiều cứng, không nóng chảy và tái định hình như nhựa nhiệt dẻo.

Lưu hóa cao su là ví dụ kinh điển; cầu sulfur hạn chế trượt vĩnh viễn giữa chuỗi.

## Đàn hồi cao su là một “lò xo entropy”

Khi cao su bị kéo, chuỗi duỗi hơn và số cấu dạng có thể có giảm.

Hệ có xu hướng trở về trạng thái cuộn hơn vì trạng thái đó có entropy cấu dạng cao hơn.

Do đó lực hồi của cao su có thành phần entropy lớn. Đây là ví dụ cho tính chất cơ học vĩ mô xuất phát từ thống kê cấu dạng phân tử, không chỉ từ liên kết bị kéo như lò xo cơ học.

## Tính đàn nhớt

Polymer có nhiều thời gian thư giãn nên đáp ứng phụ thuộc thời gian.

### Từ biến

Dưới ứng suất cố định, biến dạng tăng dần theo thời gian khi chuỗi tái sắp xếp.

### Thư giãn ứng suất

Dưới biến dạng cố định, ứng suất giảm theo thời gian vì cấu trúc phân tử tìm được trạng thái ít căng hơn.

### Phụ thuộc tần số

Ở tần số cao, chuỗi không kịp tái sắp xếp nên vật liệu phản ứng cứng và đàn hồi hơn. Ở tần số thấp, nhiều cơ chế thư giãn tham gia hơn.

**Phân tích cơ động (dynamic mechanical analysis, DMA)** dùng môđun lưu trữ `E'` và môđun mất mát `E''` để tách phần năng lượng được lưu và phần bị tiêu tán.

## Tương đương thời gian–nhiệt độ

Tăng nhiệt độ làm chuyển động phân tử nhanh lên.

Do đó hành vi ở thời gian ngắn nhưng nhiệt độ cao có thể tương ứng với thời gian dài ở nhiệt độ thấp hơn.

Bằng cách dịch các đường cong đàn nhớt theo trục thời gian/tần số, có thể xây dựng **đường cong chủ (master curve)** để ngoại suy hành vi dài hạn.

Phương pháp chỉ hợp lý khi cơ chế thư giãn không thay đổi trong vùng ghép. Nếu xuất hiện chuyển pha hoặc cơ chế mới, phép dịch có thể thất bại.

## Chất hóa dẻo

Phân tử nhỏ chen giữa các chuỗi có thể tăng thể tích tự do và khả năng chuyển động, từ đó giảm `Tg`.

Chất hóa dẻo làm PVC mềm là ví dụ quen thuộc.

Đánh đổi là chất hóa dẻo có thể di chuyển ra ngoài theo thời gian, làm tính chất thay đổi và tạo vấn đề môi trường hoặc sức khỏe tùy hóa chất.

## Dung dịch polymer và chất lượng dung môi

Dung môi tốt làm tương tác polymer–dung môi đủ thuận lợi để chuỗi nở ra. Trong dung môi kém, chuỗi co lại hoặc tách pha.

Lý thuyết Flory–Huggins mô tả năng lượng tự do trộn bằng entropy và tham số tương tác `χ`.

Vì một chuỗi lớn đóng góp ít đơn vị chuyển động độc lập hơn cùng số monomer rời, entropy trộn trên mỗi monomer nhỏ hơn nhiều so với phân tử nhỏ.

Do đó chỉ một bất lợi enthalpy vừa phải cũng có thể đủ gây tách pha.

## Gia công định hình là một phần của cấu trúc vật liệu

Nhựa nhiệt dẻo có thể được gia công bằng:

- đùn;
- ép phun;
- thổi;
- kéo sợi;
- tạo hình nhiệt.

Dòng chảy và tốc độ làm nguội thay đổi:

- mức định hướng chuỗi;
- tốc độ kết tinh;
- ứng suất dư;
- hình thái pha;
- cấu trúc lớp da/lõi.

Sợi polymer sau kéo có thể bền hơn theo phương kéo vì chuỗi được định hướng.

Vì vậy cùng một **cấp nhựa thương mại (resin grade)** vẫn có thể cho tính chất khác nhau nếu lịch sử gia công khác nhau.

## Phân hủy và lão hóa

Chuỗi polymer có thể bị phá hủy bởi:

- nhiệt;
- oxygen và oxy hóa dây chuyền;
- tia UV;
- thủy phân;
- tải cơ học;
- bức xạ ion hóa.

Đứt mạch làm giảm khối lượng phân tử và thường giảm độ bền.

Ngược lại, oxy hóa hoặc bức xạ đôi khi tạo thêm liên kết ngang, làm vật liệu cứng và giòn hơn.

Chất chống oxy hóa và chất hấp thụ UV làm chậm lão hóa nhưng không loại bỏ hoàn toàn suy giảm theo thời gian.

## Tái chế và thiết kế vòng đời

### Tái chế cơ học

Polymer được phân loại, rửa, nghiền và nóng chảy lại.

Cách này tương đối trực tiếp nhưng bị giới hạn bởi nhiễm bẩn, pha trộn polymer không tương hợp và suy giảm nhiệt qua nhiều chu kỳ.

### Tái chế hóa học

Polymer có thể được **giải trùng hợp (depolymerization)** về monomer hoặc chuyển thành nguyên liệu nhỏ hơn bằng phản ứng hóa học/nhiệt phân.

Cách này có thể xử lý một số dòng thải khó tái chế cơ học nhưng thường đòi hỏi năng lượng và tinh sạch lớn.

Không nên mặc định tái chế hóa học luôn tốt hơn; phải đánh giá toàn quy trình.

### Thiết kế cho tính tuần hoàn

Tái chế dễ hơn khi sản phẩm dùng ít loại polymer không tương hợp, phụ gia được kiểm soát, cấu kiện dễ tách và liên kết có thể đảo ngược khi cần.

Tính tuần hoàn vì vậy bắt đầu từ thiết kế vật liệu chứ không phải khi chất thải đã hình thành.

## Polymer sinh học và polymer có trình tự

Protein, DNA, cellulose và cao su tự nhiên đều là polymer sinh học.

Protein và acid nucleic có trình tự monomer được kiểm soát rất cao, trong khi polyethylene hàng hóa chủ yếu được mô tả bằng phân bố chiều dài, nhánh và độ kết tinh hơn là một trình tự duy nhất.

Polymer tổng hợp có trình tự kiểm soát là vùng giao giữa hóa polymer, hóa sinh và vật liệu thông tin.

## Ví dụ suy luận: vì sao hai mẫu polyethylene cùng công thức lặp nhưng tính chất khác nhau?

Cùng đơn vị lặp `–CH2–CH2–` chưa đủ xác định vật liệu.

Nếu một mẫu có ít nhánh, chuỗi có thể đóng gói tốt hơn, độ kết tinh và mật độ cao hơn. Nếu mẫu khác phân nhánh nhiều, đóng gói kém hơn và vật liệu mềm hơn.

Chuỗi suy luận là:

```text
kiến trúc chuỗi
→ khả năng đóng gói
→ độ kết tinh
→ mật độ + cơ tính + tính thấm
```

## Ví dụ suy luận: vì sao tăng khối lượng phân tử có thể làm gia công khó hơn?

Chuỗi dài hơn thường tạo nhiều vướng hơn, làm độ bền cơ tăng nhưng độ nhớt nóng chảy cũng tăng mạnh.

Vì vậy vật liệu có tính cơ học tốt hơn có thể cần nhiệt độ hoặc áp suất gia công cao hơn.

Đây là trade-off giữa **hiệu năng cơ học và khả năng gia công**.

## Những hiểu lầm thường gặp

### “Một mẫu polymer có một khối lượng phân tử”

Không. Hầu hết mẫu có phân bố; cần nói rõ `Mn`, `Mw` hoặc đại lượng khác.

### “Tg là nhiệt độ nóng chảy”

Không. `Tg` là chuyển thủy tinh của vùng vô định hình; `Tm` là nóng chảy của vùng tinh thể.

### “Liên kết ngang chỉ làm khối lượng phân tử lớn hơn”

Không. Nó thay đổi tô-pô mạng và khả năng chảy của vật liệu.

### “Phân hủy sinh học nghĩa là tự biến mất an toàn ở mọi môi trường”

Không. Tốc độ phân hủy phụ thuộc nhiệt độ, nước, vi sinh vật, hình học và hóa học sản phẩm phân hủy.

### “Tên polymer đủ để dự đoán tính chất”

Không. Cần thêm khối lượng phân tử, phân bố, nhánh, tacticity, độ kết tinh, phụ gia và lịch sử gia công.

## Mô hình tư duy

Hãy hình dung polymer như **mạng các sợi phân tử luôn chuyển động**:

```text
hóa học cục bộ
→ tương tác giữa chuỗi
→ cấu dạng thống kê
→ vướng + liên kết ngang
→ kết tinh + hình thái
→ gia công + lịch sử nhiệt
→ tính chất vật liệu theo thời gian
```

Khi đánh giá một polymer, luôn cần hỏi: **nhiệt độ bao nhiêu, thang thời gian nào, lịch sử gia công ra sao và chuỗi được tổ chức thế nào?**

Xem tiếp: [Chất bán dẫn](./03_semiconductors.md), [Vật liệu nano](./04_nanomaterials.md).