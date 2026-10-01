# Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**. Route đi từ cân bằng phân bố giữa pha động/tĩnh → hệ số lưu giữ và tốc độ di chuyển → độ chọn lọc, độ phân giải và hình dạng peak → định lượng/nhận diện, để nối cơ chế tách với giới hạn cột và detector.

> **Sắc ký (chromatography / 크로마토그래피)** tách các thành phần của hỗn hợp vì mỗi chất phân tích dành một phần thời gian khác nhau trong **pha động (mobile phase)** và **pha tĩnh (stationary phase)**. Một khác biệt rất nhỏ về mức ưu tiên giữa hai pha, khi được lặp lại hàng nghìn lần dọc cột, có thể tạo chênh lệch thời gian lưu đủ lớn để đo và định lượng.

Mô hình tư duy sâu hơn không phải “các chất chạy với tốc độ khác nhau”, mà là:

```text
phân bố vi mô lặp lại
+ truyền khối hữu hạn
+ dòng pha động
→ thời gian lưu và độ rộng đỉnh
```

Các prerequisite quan trọng gồm [lực liên phân tử](../02_chemical_bonding/07_intermolecular_forces.md), [dung dịch và độ tan](../03_matter_and_phases/04_solutions_and_solubility.md), [acid–base](../08_acids_bases/00_acid_base_models.md) và [đo lường/lấy mẫu](./00_measurement_and_sampling.md).

## Từ một lần phân bố tới một đỉnh sắc ký

Hãy hình dung phân tử chất phân tích liên tục chuyển giữa hai trạng thái:

```text
pha động ⇌ pha tĩnh
```

Khi ở pha động, phân tử di chuyển cùng dung môi hoặc khí mang. Khi tương tác với pha tĩnh, nó di chuyển chậm hơn hoặc gần như tạm dừng so với dòng pha động.

Chất có xu hướng ở pha tĩnh mạnh hơn sẽ dành nhiều thời gian bị giữ lại hơn và ra khỏi cột muộn hơn.

Các phân tử giống nhau không trải qua chính xác cùng một chuỗi hấp phụ–giải hấp hoặc phân bố. Sự khác nhau mang tính thống kê này tạo **độ rộng đỉnh (peak width)** thay vì một thời điểm ra cột duy nhất.

Vì vậy một phép tách tốt phải thỏa hai điều:

- các chất khác nhau có thời gian lưu trung bình đủ khác nhau;
- các phân tử của cùng một chất có phân bố thời gian lưu đủ hẹp.

> **Chuyển mạch:** Mỗi lần chất phân bố giữa hai pha góp phần tạo đỉnh; hệ số phân bố quyết định mức giữ, còn thời gian lưu phải được đọc cùng thời gian chết để tách retention khỏi transit.

## Cân bằng phân bố

Một hệ số phân bố đơn giản:

\[
K=\frac{C_s}{C_m}
\]

trong đó `Cs` là nồng độ chất phân tích trong pha tĩnh, còn `Cm` là nồng độ trong pha động.

`K` lớn thường nghĩa chất được giữ lại mạnh hơn.

Sắc ký thực có thể dựa trên hấp phụ, phân bố, trao đổi ion, loại trừ kích thước hoặc ái lực đặc hiệu. Điểm thống nhất là chất phân tích phải có mức ưu tiên khác nhau giữa các trạng thái có thể tiếp cận.

> **Chuyển mạch:** Ở chặng này của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Thời gian lưu và thời gian chết** tiếp nhận điểm tựa từ **Cân bằng phân bố** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ chọn lọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thời gian lưu và thời gian chết

**Thời gian lưu (retention time, tR)** là thời gian từ lúc đưa mẫu vào hệ tới vị trí cực đại của đỉnh chất phân tích.

**Thời gian chết (dead time/hold-up time, tM)** là thời gian một chất gần như không bị giữ lại cần để đi qua hệ.

Hệ số lưu:

\[
k'=\frac{t_R-t_M}{t_M}
\]

cho biết phần thời gian bổ sung do tương tác với pha tĩnh.

Nếu `k'` quá nhỏ, các chất dễ đồng rửa giải gần thời gian chết. Nếu `k'` quá lớn, thời gian phân tích dài và đỉnh có thể bị mở rộng không cần thiết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Độ chọn lọc** tiếp nhận điểm tựa từ **Thời gian lưu và thời gian chết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ phân giải — khoảng cách giữa đỉnh so với độ rộng đỉnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ chọn lọc

Với hai chất:

\[
\alpha=\frac{k'_2}{k'_1},\qquad k'_2>k'_1
\]

**Độ chọn lọc (selectivity, α)** mô tả khả năng hệ pha động–pha tĩnh phân biệt hai chất.

Nếu `α ≈ 1`, kéo dài cột hoặc tăng số đĩa chỉ giúp giới hạn. Thay đổi hóa học pha tĩnh, pH, dung môi hoặc nhiệt độ thường hiệu quả hơn vì nó thay đổi chính chênh lệch tương tác giữa hai chất.

> **Chuyển mạch:** Trong **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Độ phân giải — khoảng cách giữa đỉnh so với độ rộng đỉnh** tiếp nhận điểm tựa từ **Độ chọn lọc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lý thuyết đĩa — mô hình thống kê, không có các đĩa thật trong cột** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ phân giải — khoảng cách giữa đỉnh so với độ rộng đỉnh

Một biểu thức thường dùng:

\[
R_s=\frac{2(t_{R2}-t_{R1})}{w_1+w_2}
\]

Hai đỉnh được tách tốt khi khoảng cách giữa tâm đủ lớn so với độ rộng của chúng.

Độ phân giải phụ thuộc đồng thời:

```text
hiệu suất cột N
+ độ chọn lọc α
+ mức lưu k'
```

Do đó “giữ lâu hơn” không phải chiến lược chung cho mọi phép tách.

> **Chuyển mạch:** Ở chặng này của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Lý thuyết đĩa — mô hình thống kê, không có các đĩa thật trong cột** tiếp nhận điểm tựa từ **Độ phân giải — khoảng cách giữa đỉnh so với độ rộng đỉnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao đỉnh rộng ra — phương trình Van Deemter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lý thuyết đĩa — mô hình thống kê, không có các đĩa thật trong cột

Hiệu suất cột thường được biểu diễn bằng **số đĩa lý thuyết (theoretical plates)**:

\[
N=16\left(\frac{t_R}{w_b}\right)^2
\]

khi dùng độ rộng tại đường nền `wb`.

Chiều cao tương đương một đĩa:

\[
H=\frac{L}{N}
\]

`H` càng nhỏ thì hiệu suất trên một đơn vị chiều dài cột càng cao.

Các “đĩa” chỉ là mô hình thống kê cho quá trình phân bố lặp lại; chúng không phải các ngăn vật lý thật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Vì sao đỉnh rộng ra — phương trình Van Deemter** tiếp nhận điểm tựa từ **Lý thuyết đĩa — mô hình thống kê, không có các đĩa thật trong cột** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sắc ký khí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao đỉnh rộng ra — phương trình Van Deemter

Một dạng phổ biến:

\[
H=A+\frac{B}{u}+Cu
\]

với `u` là vận tốc tuyến tính của pha động.

### Thành phần A — khuếch tán xoáy

Trong cột nhồi, phân tử có thể đi theo các đường dài ngắn khác nhau quanh hạt. Hạt đồng đều và cách nhồi tốt giúp giảm khác biệt đường đi.

### Thành phần B/u — khuếch tán dọc

Chất phân tích khuếch tán dọc trục cột. Khi dòng rất chậm, phân tử có nhiều thời gian khuếch tán hơn nên dải mở rộng.

Hiệu ứng này đặc biệt đáng kể trong sắc ký khí vì khuếch tán pha khí nhanh.

### Thành phần Cu — trở lực truyền khối

Nếu dòng quá nhanh, chất phân tích không kịp tiến gần cân bằng giữa hai pha. Một số phân tử ở pha tĩnh bị “tụt lại” so với phân tử trong pha động, làm đỉnh rộng ra.

Vì vậy tăng lưu lượng có đánh đổi rõ ràng:

```text
lưu lượng tăng
→ thời gian chạy giảm
nhưng
→ truyền khối kém cân bằng hơn
→ có thể giảm hiệu suất
```

> **Chuyển mạch:** Trong **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Sắc ký khí** tiếp nhận điểm tựa từ **Vì sao đỉnh rộng ra — phương trình Van Deemter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sắc ký lỏng và HPLC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sắc ký khí

**Sắc ký khí (gas chromatography, GC)** dùng khí làm pha động. Chất phân tích phải đủ bay hơi và đủ bền nhiệt trong điều kiện đo.

Thời gian lưu phụ thuộc cả độ bay hơi lẫn tương tác với pha tĩnh. Hai chất có nhiệt độ sôi gần nhau vẫn có thể tách nếu độ phân cực hoặc tương tác đặc hiệu khác nhau.

### Lập trình nhiệt độ

Với hỗn hợp có khoảng độ bay hơi rộng, nhiệt độ cố định thấp giữ chất nặng quá lâu, còn nhiệt độ quá cao làm chất nhẹ tách kém.

**Lập trình nhiệt độ (temperature programming)** bắt đầu thấp rồi tăng dần để cân bằng hai yêu cầu.

### Bộ dò trong GC

**Bộ dò ion hóa ngọn lửa (flame ionization detector, FID)** nhạy với nhiều hợp chất hữu cơ và có khoảng tuyến tính rộng.

**Bộ dò dẫn nhiệt (thermal conductivity detector, TCD)** tổng quát hơn nhưng thường kém nhạy hơn.

**GC–MS** ghép sự tách theo thời gian với thông tin `m/z` và phân mảnh từ phổ khối.

> **Chuyển mạch:** Ở chặng này của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Sắc ký lỏng và HPLC** tiếp nhận điểm tựa từ **Sắc ký khí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **pH và ion hóa — sắc ký cũng là hóa học acid–cơ sở (base / 기반)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sắc ký lỏng và HPLC

Trong sắc ký lỏng, chất phân tích, dung môi và pha tĩnh tương tác đồng thời nên hóa học hệ thường phong phú hơn GC.

**Sắc ký lỏng hiệu năng cao (high-performance liquid chromatography, HPLC)** dùng áp suất cao để đẩy pha động qua lớp hạt nhỏ và nhồi chặt, cho hiệu suất tách cao với tốc độ phân tích thực tế.

### Sắc ký pha đảo

Pha tĩnh thường kỵ nước, ví dụ silica gắn C18, còn pha động phân cực hơn như hỗn hợp nước–acetonitrile hoặc nước–methanol.

Chất kỵ nước thường bị giữ mạnh hơn. Tăng tỷ lệ dung môi hữu cơ thường làm pha động “mạnh” hơn và giảm thời gian lưu.

### Sắc ký pha thường

Pha tĩnh phân cực và pha động ít phân cực hơn. Chất phân cực thường tương tác mạnh hơn với pha tĩnh và bị giữ lâu hơn.

### Rửa giải đẳng dòng và độ dốc (gradient / 기울기)

**Rửa giải đẳng dòng (isocratic elution)** giữ thành phần pha động không đổi.

**Rửa giải độ dốc (gradient / 기울기) (gradient elution)** thay đổi thành phần pha động theo thời gian.

Độ dốc (gradient / 기울기) đặc biệt hữu ích khi hỗn hợp có chất lưu rất yếu và rất mạnh. Nó tương tự vai trò lập trình nhiệt độ trong GC: giữ điều kiện nhẹ ở đầu để tách chất ra sớm, rồi tăng sức rửa giải để đưa chất giữ mạnh ra khỏi cột.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **pH và ion hóa — sắc ký cũng là hóa học acid–cơ sở (base / 기반)** tiếp nhận điểm tựa từ **Sắc ký lỏng và HPLC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sắc ký trao đổi ion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## pH và ion hóa — sắc ký cũng là hóa học acid–cơ sở (base / 기반)

Nếu chất phân tích có thể proton hóa hoặc khử proton, điện tích và độ kỵ nước sẽ phụ thuộc pH.

Với acid:

\[
HA\rightleftharpoons H^++A^-
\]

Dạng `HA` trung hòa thường có xu hướng lưu mạnh hơn trong pha đảo so với `A−` mang điện.

Do đó pH tương đối với `pKa` có thể làm thay đổi mạnh thời gian lưu, độ chọn lọc và hình dạng đỉnh.

Nhóm silanol trên silica cũng có thể ion hóa và tương tác với chất phân tích cơ sở (base / 기반). Chọn **dung dịch đệm (buffer)** vì vậy là một phần của hóa học phương pháp, không chỉ là cài đặt vận hành.

> **Chuyển mạch:** Trong **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Sắc ký trao đổi ion** tiếp nhận điểm tựa từ **pH và ion hóa — sắc ký cũng là hóa học acid–cơ sở (base / 기반)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sắc ký loại trừ kích thước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sắc ký trao đổi ion

Pha tĩnh mang nhóm điện tích cố định. Chất mang điện trái dấu bị giữ bởi tương tác tĩnh điện.

Thay đổi nồng độ muối hoặc pH làm thay đổi cạnh tranh và có thể rửa giải chất phân tích.

Phương pháp được dùng nhiều cho protein, amino acid và ion vô cơ.

> **Chuyển mạch:** Ở chặng này của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Sắc ký loại trừ kích thước** tiếp nhận điểm tựa từ **Sắc ký trao đổi ion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sắc ký ái lực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sắc ký loại trừ kích thước

Pha tĩnh xốp phân tách chủ yếu theo kích thước thủy động lực học.

Phân tử lớn không vào được nhiều lỗ xốp nên đi đường ngắn hơn và ra trước. Phân tử nhỏ tiếp cận được nhiều thể tích lỗ hơn nên ra muộn.

Trong chế độ này, tương tác hấp phụ mạnh với bề mặt thường là điều không mong muốn vì nó phá vỡ lô-gic (logic / 논리) tách theo kích thước.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Sắc ký ái lực** tiếp nhận điểm tựa từ **Sắc ký loại trừ kích thước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sắc ký đối quang** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sắc ký ái lực

**Sắc ký ái lực (affinity chromatography)** dùng pha tĩnh có phối tử liên kết chọn lọc với mục tiêu, ví dụ kháng thể–kháng nguyên, chất tương tự cơ chất hoặc chelate kim loại.

Phương pháp đánh đổi tính tổng quát để lấy độ chọn lọc rất cao và đặc biệt hữu ích trong tinh sạch phân tử sinh học.

> **Chuyển mạch:** Trong **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Sắc ký đối quang** tiếp nhận điểm tựa từ **Sắc ký ái lực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đưa mẫu vào cột và hiện tượng quá tải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sắc ký đối quang

Hai **đồng phân đối quang (enantiomer)** có tính chất giống nhau trong môi trường không đối quang nhưng tạo các tương tác diastereomer khác nhau với pha tĩnh đối quang.

Chênh lệch rất nhỏ về năng lượng tự do tương tác có thể tích lũy thành chênh lệch thời gian lưu đủ để tách.

Đây là ví dụ trực tiếp của việc hóa lập thể trở thành công nghệ phân tách.

> **Chuyển mạch:** Ở chặng này của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Đưa mẫu vào cột và hiện tượng quá tải** tiếp nhận điểm tựa từ **Sắc ký đối quang** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kéo đuôi và nhô đầu đỉnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đưa mẫu vào cột và hiện tượng quá tải

Nếu đưa quá nhiều chất lên cột, pha tĩnh đi vào vùng phi tuyến. Đỉnh có thể kéo đuôi, nhô đầu hoặc biến dạng, làm độ phân giải giảm.

**Quá tải khối lượng (mass overload)** xảy ra khi số tâm tương tác hữu hạn bắt đầu bão hòa.

Ngoài ra, thể tích tiêm hoặc dung môi mẫu quá mạnh so với pha động ban đầu có thể làm dải mẫu mở rộng ngay từ đầu.

Vì vậy chuẩn bị mẫu là một phần của hiệu năng sắc ký, không phải bước tách rời.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Kéo đuôi và nhô đầu đỉnh** tiếp nhận điểm tựa từ **Đưa mẫu vào cột và hiện tượng quá tải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Định lượng — diện tích đỉnh không tự động bằng nồng độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kéo đuôi và nhô đầu đỉnh

Đỉnh lý tưởng thường gần dạng Gaussian đối xứng, nhưng hệ thực có thể lệch.

**Kéo đuôi (tailing)** có thể do tâm hấp phụ thứ cấp, giải hấp chậm hoặc tương tác với silanol hoạt động.

**Nhô đầu (fronting)** thường liên quan quá tải hoặc hấp phụ phi tuyến.

Hình dạng đỉnh là tín hiệu chẩn đoán về hóa học cột, tình trạng bề mặt và điều kiện đưa mẫu.

> **Chuyển mạch:** Trong **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Định lượng — diện tích đỉnh không tự động bằng nồng độ** tiếp nhận điểm tựa từ **Kéo đuôi và nhô đầu đỉnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phát triển phương pháp là bài toán tối ưu đa mục tiêu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Định lượng — diện tích đỉnh không tự động bằng nồng độ

Trong vùng đáp ứng đã thẩm định, diện tích đỉnh của **bộ dò (detector)** có thể liên hệ với lượng chất phân tích.

Các chiến lược hiệu chuẩn gồm:

- hiệu chuẩn ngoài;
- chuẩn nội;
- thêm chuẩn trong nền mẫu phức.

Chuẩn nội giúp bù một phần biến thiên thể tích tiêm hoặc đáp ứng hệ. Thêm chuẩn có thể giảm sai lệch do hiệu ứng nền.

Sự tách sắc ký làm giảm nhiễu nhưng không tự động loại bỏ mọi hiệu ứng nền. Phần này nối trực tiếp với [thẩm định phương pháp và hóa lượng học](./07_method_validation_and_chemometrics.md).

> **Chuyển mạch:** Ở chặng này của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Phát triển phương pháp là bài toán tối ưu đa mục tiêu** tiếp nhận điểm tựa từ **Định lượng — diện tích đỉnh không tự động bằng nồng độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ghép LC–MS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phát triển phương pháp là bài toán tối ưu đa mục tiêu

Có thể điều chỉnh:

- hóa học pha tĩnh;
- thành phần pha động;
- pH và dung dịch đệm;
- nhiệt độ;
- lưu lượng;
- chương trình độ dốc (gradient / 기울기);
- kích thước cột;
- kích thước hạt.

Một phương pháp tốt phải cân bằng:

```text
độ phân giải
+ thời gian phân tích
+ áp suất
+ độ bền vững
+ độ nhạy
+ khả năng tương thích bộ dò
```

Không tồn tại một cấu hình “tốt nhất” độc lập với mục đích phân tích.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Ghép LC–MS** tiếp nhận điểm tựa từ **Phát triển phương pháp là bài toán tối ưu đa mục tiêu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sắc ký đồ và xử lý dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ghép LC–MS

LC tách hỗn hợp theo thời gian; MS tách ion theo `m/z` và cung cấp thông tin khối lượng/phân mảnh.

Ghép hai kỹ thuật làm giảm mạnh sự mơ hồ khi định danh. Tuy nhiên pha động phải tương thích với nguồn ion hóa; muối không bay hơi có thể gây ức chế ion hóa và làm bẩn nguồn.

Đây là một sự đánh đổi (trade-off / 트레이드오프) hệ thống quan trọng:

```text
điều kiện tối ưu cho sắc ký
không nhất thiết
= điều kiện tối ưu cho phổ khối
```

Thiết kế phương pháp phải tối ưu toàn chuỗi đo.

> **Chuyển mạch:** Trong **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Ghép LC–MS** nêu điều cần giải thích; **Sắc ký đồ và xử lý dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Ví dụ suy luận: vì sao tăng chiều dài cột không phải lúc nào cũng là cách tốt nhất?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sắc ký đồ và xử lý dữ liệu

**Sắc ký đồ (chromatogram)** là chuỗi tín hiệu theo thời gian gồm đường nền, nhiễu và các đỉnh.

Phần mềm có thể thực hiện:

- hiệu chỉnh đường nền;
- làm mượt;
- phát hiện đỉnh;
- tích phân;
- căn chỉnh thời gian lưu;
- hiệu chuẩn.

Trong metabolomics hoặc proteomics, hàng nghìn đặc trưng trên nhiều mẫu cần thống kê đa biến và máy học.

Tuy nhiên thuật toán tốt không thể khôi phục thông tin hóa học đã mất do chuẩn bị mẫu kém, cột không ổn định hoặc đồng rửa giải nghiêm trọng.

> **Chuyển mạch:** Ở chặng này của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Sắc ký đồ và xử lý dữ liệu** cho ta quy tắc; **Ví dụ suy luận: vì sao tăng chiều dài cột không phải lúc nào cũng là cách tốt nhất?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Ví dụ suy luận: vì sao một đỉnh đẹp vẫn có thể cho kết quả sai?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ suy luận: vì sao tăng chiều dài cột không phải lúc nào cũng là cách tốt nhất?

Tăng chiều dài thường làm tăng số đĩa và có thể cải thiện độ phân giải. Nhưng nó cũng tăng thời gian chạy và áp suất, trong khi nếu `α` gần 1 thì lợi ích rất hạn chế.

Nếu hai chất tương tác gần như giống nhau với pha tĩnh, thay đổi pH hoặc hóa học pha tĩnh để tăng độ chọn lọc thường hiệu quả hơn nhiều so với chỉ kéo dài cột.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Ví dụ suy luận: vì sao tăng chiều dài cột không phải lúc nào cũng là cách tốt nhất?** cho ta quy tắc; **Ví dụ suy luận: vì sao một đỉnh đẹp vẫn có thể cho kết quả sai?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Những hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ suy luận: vì sao một đỉnh đẹp vẫn có thể cho kết quả sai?

Một đỉnh đối xứng và tách rõ không chứng minh nó chỉ chứa một chất duy nhất. Hai chất có thể đồng rửa giải gần hoàn toàn và tạo một đỉnh trông đẹp.

Định danh đáng tin cần thêm thông tin trực giao như phổ khối, phổ UV, chuẩn tham chiếu hoặc thay đổi điều kiện tách.

Đây là lý do sắc ký vừa là bài toán phân tách vừa là bài toán **bằng chứng định danh**.

> **Chuyển mạch:** Trong **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Ví dụ suy luận: vì sao một đỉnh đẹp vẫn có thể cho kết quả sai?** cho ta quy tắc; **Những hiểu lầm thường gặp** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm thường gặp

### “Giữ lâu hơn luôn tách tốt hơn”

Không. Độ phân giải phụ thuộc độ chọn lọc, hiệu suất và độ rộng đỉnh, không chỉ thời gian lưu.

### “Thời gian lưu xác định duy nhất một hợp chất”

Không. Nhiều chất có thể có thời gian lưu gần nhau hoặc đồng rửa giải.

### “Tăng lưu lượng luôn rút ngắn phân tích mà không có đánh đổi”

Không. Lưu lượng cao làm trở lực truyền khối và áp suất tăng.

### “Sắc ký chỉ là phân tách vật lý”

Không. Sự lưu giữ bị chi phối bởi tương tác hóa học, ion hóa, solvat hóa, hấp phụ và kích thước phân tử.

### “Cột có số đĩa cao thì phương pháp chắc chắn tốt”

Không. Nếu độ chọn lọc kém hoặc mẫu bị quá tải, số đĩa cao không giải quyết được vấn đề cốt lõi.

> **Chuyển mạch:** Ở chặng này của **Sắc ký — tách chất bằng sự phân bố khác nhau giữa hai pha**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Hãy xem sắc ký như **một cuộc đua gồm hàng nghìn lần tạm dừng thuận nghịch**:

```text
độ chọn lọc
→ hai chất có ưu tiên pha khác nhau bao nhiêu?

hiệu suất
→ các phân tử cùng loại có lịch sử di chuyển nhất quán tới đâu?

truyền khối + dòng chảy
→ có thể chạy nhanh tới mức nào trước khi dải bị nhòe?
```

Một phép tách tốt xuất hiện khi ba yếu tố này được tối ưu cùng nhau, không phải khi một thông số riêng lẻ đạt cực đại.

Xem tiếp: [Phổ khối](./05_mass_spectrometry.md) và [Thẩm định phương pháp và hóa lượng học](./07_method_validation_and_chemometrics.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
