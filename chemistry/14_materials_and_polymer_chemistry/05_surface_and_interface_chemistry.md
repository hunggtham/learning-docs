# Hóa học bề mặt và mặt phân cách — nơi các pha gặp nhau và phản ứng tập trung

> **Mặt phân cách (interface / 계면)** là vùng biên giữa hai pha. **Bề mặt (surface / 표면)** thường dùng khi một pha tiếp xúc với khí hoặc chân không. Nguyên tử và phân tử ở vùng biên có môi trường phối trí không đối xứng so với vật liệu khối, nên năng lượng tự do, mật độ electron và khả năng phản ứng có thể khác rõ rệt.

Ăn mòn, xúc tác dị thể, bám dính, làm ướt, pin, cảm biến và chế tạo bán dẫn đều là những ví dụ mà hóa học vùng biên có thể quyết định hành vi của toàn hệ.

Các prerequisite quan trọng gồm [lực liên phân tử](../02_chemical_bonding/07_intermolecular_forces.md), [chất lỏng](../03_matter_and_phases/01_liquids.md), [nhiệt động lực học hóa học](../05_thermodynamics/04_chemical_thermodynamics.md), [động học](../06_chemical_kinetics/00_reaction_rates.md) và [chất bán dẫn](./03_semiconductors.md).

## Vì sao tạo bề mặt tốn năng lượng tự do?

Trong khối vật liệu, một nguyên tử thường được bao quanh tương đối đầy đủ bởi các hàng xóm. Ở bề mặt, một phần tương tác bị mất hoặc thay đổi. Vì vậy tạo thêm diện tích bề mặt thường làm tăng năng lượng tự do.

Nếu các yếu tố khác gần như không đổi:

\[
G_{surface}=\gamma A
\]

trong đó `γ` là năng lượng tự do bề mặt và `A` là diện tích.

Hệ có xu hướng giảm diện tích bề mặt nếu việc đó làm tổng năng lượng tự do giảm. Đây là một lý do giọt nhỏ có xu hướng tròn và hạt nano có xu hướng kết tụ hoặc thiêu kết.

### Vì sao giọt có xu hướng hình cầu?

Với cùng thể tích, hình cầu có diện tích bề mặt nhỏ nhất. Ở kích thước nhỏ, năng lượng bề mặt chi phối mạnh nên giọt tiến gần dạng cầu. Ở kích thước lớn, trọng lực bắt đầu cạnh tranh và làm giọt dẹt hơn.

### Sức căng bề mặt và năng lượng bề mặt

Với chất lỏng, phân tử có thể tái sắp xếp tương đối dễ nên **sức căng bề mặt (surface tension)** là đại lượng thuận tiện.

Với chất rắn, **năng lượng tự do bề mặt (surface free energy)** thường thích hợp hơn vì từng mặt tinh thể có thể có năng lượng khác nhau và mạng tinh thể không tái sắp xếp dễ như chất lỏng.

## Mặt tinh thể và khả năng phản ứng

Các mặt tinh thể khác nhau có mật độ nguyên tử, mức phối trí và cấu trúc electron khác nhau. Mặt có nhiều nguyên tử thiếu phối trí thường có năng lượng cao hơn và có thể phản ứng mạnh hơn.

Hình dạng hạt nano vì vậy là kết quả cạnh tranh giữa:

- năng lượng tự do của từng mặt;
- tốc độ gắn tiền chất lên từng mặt;
- chất hấp phụ hoặc phối tử ưu tiên một mặt cụ thể;
- điều kiện động học trong quá trình tăng trưởng.

Trong xúc tác, hình học của tâm hấp phụ cũng thay đổi theo mặt tinh thể, nên hoạt tính và độ chọn lọc không chỉ phụ thuộc “nguyên tố nào” mà còn phụ thuộc “bề mặt nào”.

## Độ cong và áp suất Laplace

Với giọt cầu:

\[
\Delta P=\frac{2\gamma}{r}
\]

Bán kính càng nhỏ, chênh áp qua mặt phân cách càng lớn.

Độ cong cũng ảnh hưởng thế hóa học. Hạt rất nhỏ có thể có xu hướng hòa tan mạnh hơn hạt lớn. Đây là nền nhiệt động của **chín Ostwald (Ostwald ripening)**, trong đó vật chất chuyển dần từ hạt nhỏ sang hạt lớn.

## Làm ướt và góc tiếp xúc

Khi một giọt nằm trên chất rắn, hình dạng cân bằng phản ánh ba năng lượng mặt phân cách.

Phương trình Young:

\[
\gamma_{SV}=\gamma_{SL}+\gamma_{LV}\cos\theta
\]

trong đó `SV`, `SL`, `LV` tương ứng rắn–hơi, rắn–lỏng và lỏng–hơi.

Góc tiếp xúc nhỏ thường biểu thị làm ướt tốt hơn. Tuy nhiên `θ` không phải một hằng số tuyệt đối của “vật liệu”. Nó còn phụ thuộc độ nhám, nhiễm bẩn, không đồng nhất hóa học, góc tiến/góc lùi và lịch sử giọt.

Vì vậy suy năng lượng bề mặt từ một góc tiếp xúc đơn lẻ có thể gây hiểu sai.

## Độ nhám khuếch đại hành vi làm ướt

Trong mô hình Wenzel:

\[
\cos\theta^*=r\cos\theta
\]

với `r > 1` là hệ số nhám.

Mô hình Cassie–Baxter mô tả trường hợp giọt nằm trên hỗn hợp rắn–không khí do túi khí bị giữ lại trong cấu trúc bề mặt.

Bề mặt siêu kỵ nước thường cần đồng thời:

```text
hóa học năng lượng bề mặt thấp
+ cấu trúc nhám thích hợp
→ góc tiếp xúc rất lớn
```

“Kỵ nước” vì vậy là kết quả của cả hóa học và hình học.

## Hấp phụ và hấp thụ không phải cùng một quá trình

**Hấp phụ (adsorption / 흡착)** là sự tích tụ chất tại bề mặt hoặc mặt phân cách.

**Hấp thụ (absorption)** là chất đi vào thể tích pha khối.

Phân biệt này quan trọng vì cơ chế, động học và mô hình định lượng khác nhau.

### Hấp phụ vật lý và hấp phụ hóa học

**Hấp phụ vật lý (physisorption)** chủ yếu đến từ lực phân tán, tĩnh điện và các tương tác không cộng hóa trị; thường thuận nghịch hơn.

**Hấp phụ hóa học (chemisorption)** liên quan tạo liên kết hóa học đặc hiệu hơn và có thể có hàng rào hoạt hóa đáng kể.

Hai loại này là hai đầu của một phổ; hệ thực có thể mang cả hai đặc tính.

## Mô hình Langmuir

Langmuir giả định:

- các tâm hấp phụ tương đương;
- mỗi tâm chứa tối đa một phân tử;
- tương tác bên giữa chất hấp phụ không đáng kể;
- hấp phụ và giải hấp đạt cân bằng.

Độ phủ bề mặt:

\[
\theta=\frac{KP}{1+KP}
\]

Ở áp suất thấp, `θ ≈ KP`; ở áp suất cao, bề mặt tiến tới bão hòa.

Mô hình rất hữu ích vì gắn được công thức với cơ chế đơn giản, nhưng bề mặt thật thường không đồng nhất và chất hấp phụ có thể tương tác với nhau.

## Freundlich và BET — mô hình trả lời câu hỏi khác nhau

Phương trình Freundlich:

\[
q=KC^n
\]

là mô hình thực nghiệm hữu ích cho bề mặt không đồng nhất nhưng ít thông tin cơ chế hơn Langmuir.

Mô hình **BET (Brunauer–Emmett–Teller)** dùng hấp phụ đa lớp để ước lượng diện tích bề mặt riêng từ dữ liệu hấp phụ khí.

Giá trị BET không phải “diện tích hình học tuyệt đối”; nó là diện tích có thể tiếp cận đối với chất dò trong điều kiện và mô hình đã chọn.

## Chu trình xúc tác dị thể

Một phản ứng trên chất xúc tác rắn có thể gồm:

```text
vận chuyển chất phản ứng tới bề mặt
→ hấp phụ
→ hoạt hóa liên kết
→ phản ứng bề mặt
→ khuếch tán bề mặt nếu cần
→ giải hấp sản phẩm
→ vận chuyển sản phẩm khỏi bề mặt
```

Bất kỳ bước nào cũng có thể giới hạn tốc độ tổng.

Đây là lý do tăng hoạt tính nội tại của một tâm xúc tác có thể không cải thiện tốc độ thiết bị nếu hệ đang bị giới hạn bởi vận chuyển khối.

## Nguyên lý Sabatier và đánh đổi độ bền hấp phụ

Một chất xúc tác tốt thường phải liên kết trung gian **không quá yếu và không quá mạnh**.

```text
hấp phụ quá yếu
→ khó hoạt hóa chất phản ứng

hấp phụ quá mạnh
→ trung gian/sản phẩm khó rời
→ bề mặt bị che phủ
```

Đánh đổi này là trực giác nền của nhiều **đồ thị núi lửa (volcano plot)**, nơi hoạt tính cực đại xuất hiện ở vùng năng lượng hấp phụ trung gian.

## Langmuir–Hinshelwood và Eley–Rideal

Trong cơ chế **Langmuir–Hinshelwood**, cả hai chất phản ứng đều hấp phụ trước khi phản ứng.

Trong cơ chế **Eley–Rideal**, một chất đã hấp phụ phản ứng trực tiếp với chất còn lại từ pha khí hoặc dung dịch.

Vì độ phủ thay đổi theo áp suất hoặc nồng độ, bậc phản ứng quan sát có thể thay đổi theo điều kiện. Do đó không nên suy cơ chế chỉ từ một bậc phản ứng đo tại một điều kiện duy nhất.

## Ngộ độc và chất xúc tiến

Một tạp chất hấp phụ quá mạnh có thể chiếm tâm hoạt động và gây **ngộ độc xúc tác (catalyst poisoning)**. Sulfur trên nhiều bề mặt kim loại là ví dụ điển hình.

Ngược lại, **chất xúc tiến (promoter)** có thể không trực tiếp xúc tác bước phản ứng chính nhưng làm thay đổi độ phân tán, trạng thái điện tử, hình học hoặc độ bền của pha hoạt động.

Chất xúc tác công nghiệp vì vậy thường là hệ đa thành phần, không phải một nguyên tố tinh khiết đơn giản.

## Bề mặt có thể tái cấu trúc trong khi phản ứng

Dưới nhiệt độ, áp suất và thế hóa học khác nhau, bề mặt có thể thay đổi cấu trúc, trạng thái oxy hóa hoặc lớp chất hấp phụ.

Bề mặt đo trong chân không sau khi làm nguội chưa chắc giống bề mặt đang hoạt động trong thiết bị phản ứng.

Các kỹ thuật **đo khi đang vận hành (operando)** cố gắng quan sát vật liệu trong điều kiện gần trạng thái chức năng thật.

Điều này nhắc một nguyên tắc quan trọng: **cấu trúc của chất xúc tác là một biến động, không nhất thiết là một ảnh tĩnh**.

## Lớp điện kép ở mặt phân cách điện cực–điện ly

Khi điện cực mang điện tích, ion và phân tử dung môi trong điện ly tái sắp xếp để bù điện tích.

Các mô hình lịch sử gồm:

- Helmholtz: lớp đặc giống tụ điện;
- Gouy–Chapman: thêm vùng ion khuếch tán;
- Stern: kết hợp lớp đặc và lớp khuếch tán.

Mặt phân cách thật còn có hấp phụ đặc hiệu, cấu trúc dung môi và phản ứng điện cực.

Điện dung vi phân:

\[
C=\frac{dQ}{dV}
\]

Vật liệu **siêu tụ điện (supercapacitor)** tận dụng diện tích bề mặt rất lớn để lưu điện tích trong lớp điện kép hoặc thông qua **giả điện dung (pseudocapacitance)**.

Động học chuyển electron chi tiết, Butler–Volmer, Tafel và EIS được trình bày ở [Động học điện hóa và trở kháng](../09_redox_and_electrochemistry/06_electrochemical_kinetics_and_impedance.md); chương này chỉ giữ phần cần thiết để hiểu vai trò của mặt phân cách.

## Dòng Faraday và dòng không Faraday

**Dòng Faraday (Faradaic current)** đi kèm phản ứng oxy hóa–khử có chuyển electron qua mặt phân cách.

**Dòng không Faraday (non-Faradaic current)** chủ yếu liên quan nạp/xả lớp điện kép mà không có biến đổi redox ròng.

Trong phép đo thực, hai thành phần có thể cùng xuất hiện và phải được tách bằng thiết kế thí nghiệm hoặc mô hình phù hợp.

## Lớp liên pha điện ly rắn trong pin lithium-ion

Ở điện cực âm của pin lithium-ion, điện ly có thể bị khử và tạo **lớp liên pha điện ly rắn (solid electrolyte interphase, SEI)**.

Một SEI hữu ích phải đồng thời:

- cho `Li+` đi qua;
- cản electron;
- bền hóa học và cơ học;
- hạn chế điện ly tiếp tục phân hủy.

SEI quá dày làm tăng điện trở. SEI nứt rồi tái tạo liên tục tiêu thụ lithium khả dụng và điện ly.

Đây là ví dụ điển hình cho việc tính năng của vật liệu khối có thể tốt nhưng tuổi thọ thiết bị vẫn bị giới hạn bởi hóa học mặt phân cách.

## Bám dính — nhiều cơ chế cùng đóng góp

Độ bám dính có thể đến từ:

- làm ướt tốt;
- tương tác acid–base;
- liên kết cộng hóa trị;
- khóa cơ học trên bề mặt nhám;
- khuếch tán và đan xen chuỗi polymer;
- trạng thái ứng suất dư.

**Phá hủy tại mặt phân cách (adhesive failure)** xảy ra ngay giữa hai pha. **Phá hủy nội khối (cohesive failure)** xảy ra bên trong một pha vật liệu.

Phân biệt hai kiểu này cho biết nên cải thiện hóa học bề mặt hay tính chất cơ học khối.

## Chuẩn bị bề mặt

Dầu, bụi hoặc một lớp oxide yếu có thể tạo **lớp biên yếu (weak boundary layer)** và làm liên kết thất bại dù chất kết dính rất tốt.

Xử lý plasma, corona, UV–ozone hoặc phản ứng hóa học có thể tạo nhóm phân cực, loại nhiễm bẩn hoặc tăng năng lượng bề mặt.

Trong sản xuất, bước làm sạch và hoạt hóa bề mặt thường quan trọng ngang với việc chọn chất kết dính.

## Lớp đơn phân tử tự lắp ghép

Các phân tử có đầu neo lên bề mặt và đuôi chức năng có thể tự tổ chức thành **lớp đơn tự lắp ghép (self-assembled monolayer, SAM)**.

Ví dụ:

- thiol trên vàng;
- silane trên oxide.

Một lớp chỉ dày cỡ phân tử có thể thay đổi độ ướt, công thoát electron, tương hợp sinh học, chống ăn mòn hoặc độ chọn lọc của cảm biến.

## Mặt phân cách trong bán dẫn

Khuyết tật ở mặt phân cách oxide–bán dẫn hoặc kim loại–bán dẫn có thể tạo **trạng thái bẫy (trap state)**, bắt hạt tải và làm giảm độ linh động hoặc làm điện áp ngưỡng bị trôi.

Thụ động hóa bề mặt nhằm loại bỏ hoặc bão hòa các liên kết treo.

Trong transistor hiện đại, chất lượng mặt phân cách có thể quan trọng hơn độ tinh khiết của silicon trong khối. Xem thêm [Chất bán dẫn](./03_semiconductors.md).

### Rào Schottky

Tiếp xúc kim loại–bán dẫn có thể tạo rào năng lượng phụ thuộc công thoát electron và trạng thái mặt phân cách.

Mô hình lý tưởng có thể lệch khỏi thực nghiệm vì dipole bề mặt, hóa học tiếp xúc và hiện tượng **ghim mức Fermi (Fermi-level pinning)**.

## Tăng trưởng màng mỏng

### Lắng đọng hơi hóa học

Trong **CVD**, tiền chất khí phản ứng hoặc phân hủy trên bề mặt. Chất lượng màng phụ thuộc đồng thời động học bề mặt và vận chuyển tiền chất.

### Lắng đọng lớp nguyên tử

Trong **ALD**, các tiền chất phản ứng theo chu kỳ tự giới hạn. Khả năng phủ đồng đều cấu trúc ba chiều phụ thuộc việc tiền chất có thể khuếch tán tới mọi vùng và phản ứng với đúng nhóm chức bề mặt.

Do đó lắng đọng màng không chỉ là “đưa vật liệu lên nền”; nó bắt đầu từ hóa học của các tâm bề mặt.

## Ăn mòn bắt đầu ở vùng biên

Ăn mòn kim loại là quá trình điện hóa ghép giữa vùng oxy hóa và vùng khử trên bề mặt.

Tính không đồng nhất cục bộ như pha thứ hai, biên hạt, ứng suất hoặc chênh lệch oxygen có thể tạo các pin vi mô.

**Lớp phủ (coating)**, **chất ức chế (inhibitor)** và thụ động hóa đều hoạt động bằng cách thay đổi vận chuyển chất hoặc động học phản ứng ở mặt phân cách.

Cơ chế điện hóa chi tiết được nối với [Pin, ăn mòn và lưu trữ năng lượng](../09_redox_and_electrochemistry/05_batteries_corrosion_and_energy_storage.md).

## Các kỹ thuật phân tích bề mặt

### XPS

**Quang phổ quang electron tia X (X-ray photoelectron spectroscopy, XPS)** đo năng lượng liên kết electron và cho thông tin thành phần nguyên tố, trạng thái hóa học trong lớp bề mặt cỡ nanomet.

### AES

**Phổ electron Auger (Auger electron spectroscopy, AES)** có độ nhạy bề mặt cao và sử dụng electron Auger đặc trưng để suy thành phần.

### SIMS

**Khối phổ ion thứ cấp (secondary ion mass spectrometry, SIMS)** bắn ion vào bề mặt rồi phân tích ion thứ cấp bật ra. Phương pháp rất nhạy và có thể tạo **hồ sơ theo chiều sâu (depth profile)** nhưng thường mang tính phá hủy.

### AFM

**Kính hiển vi lực nguyên tử (atomic force microscopy, AFM)** đo địa hình và lực tương tác ở thang nano.

Không kỹ thuật nào đơn độc mô tả toàn bộ mặt phân cách. Thường phải ghép thông tin thành phần, trạng thái hóa học, cấu trúc, hình thái và tính chất điện.

## Khuếch tán bề mặt và tạo mầm dị thể

Chất hấp phụ có thể nhảy giữa các tâm với tốc độ hoạt hóa:

\[
k\propto\exp\left(-\frac{E_d}{RT}\right)
\]

Khuếch tán bề mặt ảnh hưởng thiêu kết, tăng trưởng tinh thể và xúc tác.

Tạo mầm trên bề mặt thường dễ hơn tạo mầm đồng thể vì bề mặt sẵn có làm giảm năng lượng cần thiết để tạo vùng biên mới.

Đây là lý do bụi, vết xước hoặc tinh thể mồi có thể kích hoạt kết tinh.

## Chất hoạt động bề mặt, micelle và nhũ tương

**Chất hoạt động bề mặt (surfactant)** hấp phụ ở vùng dầu–nước hoặc khí–nước và làm giảm sức căng mặt phân cách.

Trên **nồng độ micelle tới hạn (critical micelle concentration, CMC)**, phân tử hoạt động bề mặt bắt đầu hình thành micelle đáng kể trong pha khối.

Tẩy rửa kết hợp nhiều cơ chế:

```text
tăng làm ướt
+ phân tán dầu
+ ổn định giọt
+ hòa tan chất kỵ nước trong micelle
```

Nhũ tương thường không bền về nhiệt động nhưng có thể bền lâu về động học. Tách kem, kết tụ giọt và chín Ostwald là các cơ chế mất ổn định khác nhau; không nên gộp tất cả thành một hiện tượng “tách lớp”.

## Mặt phân cách sinh học

Màng tế bào, bề mặt protein, vật liệu cấy ghép và lớp nhầy đều là những vùng biên hóa học phức tạp.

Khi **vật liệu sinh học (biomaterial)** tiếp xúc máu, protein thường hấp phụ gần như ngay lập tức. Tế bào sau đó tương tác chủ yếu với lớp protein đã hấp phụ chứ không còn với bề mặt nguyên sơ ban đầu.

Vì vậy tính tương hợp sinh học phải được hiểu là kết quả của:

```text
vật liệu khối
+ hóa học bề mặt
+ protein hấp phụ
+ môi trường sinh học
+ thời gian
```

không phải một nhãn cố định của vật liệu.

## Ví dụ suy luận: vì sao diện tích bề mặt lớn chưa chắc làm chất xúc tác tốt hơn?

Giả sử vật liệu A có diện tích BET gấp đôi B nhưng phần lớn diện tích của A nằm trong lỗ quá hẹp để chất phản ứng tiếp cận hoặc trên các mặt tinh thể không hoạt tính.

Khi đó diện tích hình học lớn hơn không đảm bảo tốc độ phản ứng lớn hơn. Cần hỏi **bao nhiêu diện tích có thể tiếp cận, bao nhiêu tâm thật sự hoạt động và vận chuyển có đủ nhanh không**.

## Ví dụ suy luận: vì sao lớp phủ tốt ban đầu vẫn có thể hỏng sau thời gian dài?

Một lớp phủ có thể bám dính và cách ly tốt lúc đầu nhưng nước hoặc ion vẫn khuếch tán chậm qua khuyết tật vi mô. Khi chúng tới kim loại, phản ứng điện hóa bắt đầu dưới lớp phủ, tạo sản phẩm làm tăng ứng suất và tách lớp.

Đây là bài toán ghép:

```text
khuếch tán chậm
→ hóa học điện hóa cục bộ
→ thay đổi cơ học
→ hỏng mặt phân cách
```

không thể giải thích chỉ bằng một phép đo bám dính ban đầu.

## Những hiểu lầm thường gặp

### “Bề mặt chỉ là lớp ngoài cùng của vật liệu khối”

Không. Số phối trí, trạng thái electron, thành phần và năng lượng tự do có thể khác rõ rệt so với bên trong.

### “Diện tích bề mặt càng lớn thì chất xúc tác càng tốt”

Không. Cần đúng loại tâm hoạt động, khả năng tiếp cận, độ bền cấu trúc và vận chuyển phù hợp.

### “Góc tiếp xúc cho trực tiếp một giá trị năng lượng bề mặt duy nhất”

Không. Kết quả phụ thuộc mô hình, độ nhám, không đồng nhất và hiện tượng trễ góc tiếp xúc.

### “Hiệu năng pin chủ yếu do dung lượng lý thuyết vật liệu điện cực”

Không. SEI, mặt phân cách, vận chuyển ion, phản ứng phụ và cấu trúc điện cực có thể chi phối tuổi thọ/công suất.

### “Mặt phân cách là một lớp tĩnh”

Không. Nó có thể hấp phụ, giải hấp, tái cấu trúc, oxy hóa, khử, nứt hoặc hình thành pha mới trong khi hệ vận hành.

## Mô hình tư duy

Hãy xem bề mặt và mặt phân cách như **một pha chức năng có chiều dày nhỏ nhưng tác động lớn**:

```text
cấu trúc nguyên tử bề mặt
+ thành phần
+ chất hấp phụ
+ điện tích
+ độ cong
+ vận chuyển
→ năng lượng tự do và động học vùng biên
→ hành vi vĩ mô
```

Khi một hệ có hiện tượng xảy ra tại ranh giới — xúc tác, ăn mòn, pin, cảm biến, bám dính, làm ướt, tăng trưởng màng — đừng chỉ hỏi vật liệu khối là gì. Hãy hỏi **bề mặt hiện có cấu trúc nào, đang tiếp xúc với pha nào, chất gì đang hấp phụ, và trạng thái đó thay đổi theo thời gian ra sao**.

Xem tiếp: [Chất bán dẫn](./03_semiconductors.md), [Vật liệu nano](./04_nanomaterials.md), [Động học điện hóa và trở kháng](../09_redox_and_electrochemistry/06_electrochemical_kinetics_and_impedance.md).