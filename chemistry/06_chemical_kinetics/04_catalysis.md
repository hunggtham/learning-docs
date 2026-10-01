# Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Chất xúc tác thực sự làm gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Chu trình xúc tác — chất xúc tác là một mạng phản ứng nhỏ** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> **Chất xúc tác (catalyst / 촉매)** làm tăng tốc độ phản ứng bằng cách cung cấp cơ chế hoặc con đường có hàng rào hoạt hóa hiệu dụng thấp hơn, đồng thời được tái sinh trong chu trình xúc tác tổng. Chất xúc tác không làm thay đổi \(\Delta G^\circ\) hay hằng số cân bằng của phản ứng ròng.

Một cách nhìn sâu hơn là: xúc tác **tái thiết kế cảnh quan động học** giữa chất phản ứng và sản phẩm. Chất xúc tác tạo các chất trung gian, trạng thái chuyển tiếp và bề mặt tương tác mới sao cho một hoặc nhiều hàng rào năng lượng giảm xuống, đồng thời có thể làm một con đường phản ứng trở nên ưu tiên hơn các con đường cạnh tranh.

## Chất xúc tác thực sự làm gì?

Nếu phản ứng không xúc tác phải đi qua một hàng rào cao, chất xúc tác có thể:

- liên kết với chất phản ứng;
- ổn định trạng thái chuyển tiếp;
- định hướng các chất phản ứng;
- chia phản ứng thành nhiều bước có hàng rào thấp hơn;
- tạo chất trung gian có phản ứng tính cao hơn;
- thay đổi môi trường điện tử hoặc acid–cơ sở (base / 기반) cục bộ.

Năng lượng tự do của trạng thái đầu và cuối không đổi. Thứ thay đổi là **địa hình năng lượng giữa chúng**.

Chất xúc tác làm tăng cả tốc độ thuận và tốc độ nghịch theo nguyên lý thuận nghịch vi mô, nên hệ đạt cân bằng nhanh hơn nhưng thành phần cân bằng không bị chất xúc tác dịch chuyển.

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Chu trình xúc tác — chất xúc tác là một mạng phản ứng nhỏ** tiếp nhận điểm tựa từ **Chất xúc tác thực sự làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tốc độ quay vòng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chu trình xúc tác — chất xúc tác là một mạng phản ứng nhỏ

Một **chu trình xúc tác (catalytic cycle)** thường gồm nhiều bước cơ bản:

```text
C + A ⇌ C–A
C–A → C–B
C–B → C + B
```

Ở đây `C` được tái sinh sau một vòng, còn A biến thành B.

Tuy nhiên trạng thái chiếm ưu thế của chất xúc tác trong thực nghiệm có thể không phải dạng `C` được vẽ ở đầu sơ đồ. Dạng xuất hiện nhiều nhất gọi là **trạng thái nghỉ (resting state)**.

Điều này quan trọng vì nồng độ của trạng thái nghỉ có thể lớn nhưng bước chứa nó chưa chắc là bước chậm nhất theo nghĩa cơ chế.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Tốc độ quay vòng** tiếp nhận điểm tựa từ **Chu trình xúc tác — chất xúc tác là một mạng phản ứng nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bước quyết định tốc độ không phải lúc nào cũng là một bước duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tốc độ quay vòng

Hai đại lượng thường dùng để đánh giá xúc tác là:

**Số vòng quay (turnover number, TON)**:

\[
TON=\frac{n_{sản phẩm (product / 제품)}}{n_{catalyst}}
\]

cho biết một đơn vị catalyst tạo được bao nhiêu đơn vị sản phẩm trước khi mất hoạt tính.

**Tần suất quay vòng (turnover frequency, TOF)**:

\[
TOF=\frac{1}{n_{catalyst}}\frac{dn_{sản phẩm (product / 제품)}}{dt}
\]

cho biết tốc độ tạo sản phẩm trên mỗi lượng catalyst.

TON phản ánh tuổi thọ tổng, còn TOF phản ánh hoạt tính theo thời gian. Một catalyst có TOF cao nhưng nhanh chết vẫn có TON thấp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Bước quyết định tốc độ không phải lúc nào cũng là một bước duy nhất** tiếp nhận điểm tựa từ **Tốc độ quay vòng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chu trình năng lượng tự do** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bước quyết định tốc độ không phải lúc nào cũng là một bước duy nhất

Trong sách cơ bản thường nhắc **bước quyết định tốc độ (rate-determining step)** như bước chậm nhất. Khái niệm này hữu ích nhưng đôi khi quá đơn giản.

Trong chu trình nhiều bước, tốc độ tổng có thể chịu ảnh hưởng đồng thời của nhiều trạng thái chuyển tiếp và trạng thái trung gian.

Một khái niệm sâu hơn là **mức độ kiểm soát tốc độ (degree of rate control)**: nếu thay đổi năng lượng của một trạng thái chuyển tiếp một chút mà tốc độ tổng thay đổi mạnh, trạng thái đó có mức kiểm soát tốc độ lớn.

Điều này hữu ích khi thiết kế catalyst vì nó trả lời câu hỏi thực tế hơn:

> nên ổn định trạng thái nào để tốc độ toàn chu trình tăng nhiều nhất?

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Chu trình năng lượng tự do** tiếp nhận điểm tựa từ **Bước quyết định tốc độ không phải lúc nào cũng là một bước duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trạng thái trung gian quá bền có thể làm catalyst chậm đi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chu trình năng lượng tự do

Với mỗi bước trong catalytic cycle, có thể vẽ:

- năng lượng của chất trung gian;
- năng lượng trạng thái chuyển tiếp;
- hàng rào năng lượng tự do hoạt hóa \(\Delta G^\ddagger\).

Theo lý thuyết trạng thái chuyển tiếp:

\[
k\approx\frac{k_BT}{h}e^{-\Delta G^\ddagger/(RT)}
\]

Vì hàm mũ phụ thuộc \(\Delta G^\ddagger\), giảm vài kJ/mol ở hàng rào phù hợp có thể làm tốc độ thay đổi đáng kể.

Đây là lý do tối ưu hóa catalyst thường tập trung vào **năng lượng trạng thái chuyển tiếp**, không chỉ năng lượng liên kết của chất trung gian.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Trạng thái trung gian quá bền có thể làm catalyst chậm đi** tiếp nhận điểm tựa từ **Chu trình năng lượng tự do** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xúc tác đồng thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trạng thái trung gian quá bền có thể làm catalyst chậm đi

Ổn định chất trung gian không phải lúc nào cũng tốt.

Nếu catalyst gắn quá mạnh với một chất trung gian, hố năng lượng trở nên quá sâu. Bước thoát khỏi hố đó có thể có hàng rào rất lớn.

Đây là trực giác phía sau nguyên lý Sabatier:

> catalyst tốt thường phải liên kết “vừa đủ” — không quá yếu để không hoạt hóa được, cũng không quá mạnh để sản phẩm hoặc trung gian bị giữ lại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Xúc tác đồng thể** tiếp nhận điểm tựa từ **Trạng thái trung gian quá bền có thể làm catalyst chậm đi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xúc tác acid–cơ sở (base / 기반)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xúc tác đồng thể

Trong **xúc tác đồng thể (homogeneous catalysis)**, chất xúc tác cùng pha với chất phản ứng, thường trong dung dịch.

Phức kim loại chuyển tiếp có thể thay đổi trạng thái oxi hóa, phối trí với cơ chất và tạo điều kiện hoạt hóa liên kết.

Các bước điển hình trong organometallic catalysis gồm:

- phối trí ligand/substrate;
- cộng oxy hóa (oxidative addition);
- loại khử (reductive elimination);
- chèn chuyển vị (migratory insertion);
- loại beta-hydride;
- trao đổi ligand.

Không phải mọi chu trình đều có tất cả các bước này, nhưng chúng là “từ vựng cơ chế” quan trọng.

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Xúc tác acid–cơ sở (base / 기반)** tiếp nhận điểm tựa từ **Xúc tác đồng thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xúc tác dị thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xúc tác acid–cơ sở (base / 기반)

Xúc tác acid có thể proton hóa một nhóm chức và làm nó trở thành electrophile mạnh hơn hoặc nhóm rời tốt hơn.

Xúc tác cơ sở (base / 기반) có thể lấy proton và tạo nucleophile hoặc carbanion mạnh hơn.

Với **xúc tác acid–cơ sở (base / 기반) tổng quát (general acid/base catalysis)**, species khác dung môi trực tiếp tham gia chuyển proton trong trạng thái chuyển tiếp.

Với **xúc tác acid–cơ sở (base / 기반) riêng (specific acid/base catalysis)**, tốc độ chủ yếu phụ thuộc nồng độ `H3O+` hoặc `OH−` sau khi cân bằng proton hóa nhanh đã được thiết lập.

Phân biệt này rất quan trọng trong cơ chế enzyme và động học dung dịch.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Xúc tác dị thể** tiếp nhận điểm tựa từ **Xúc tác acid–cơ sở (base / 기반)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hấp phụ Langmuir** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xúc tác dị thể

Trong **xúc tác dị thể (heterogeneous catalysis)**, chất xúc tác và chất phản ứng nằm ở các pha khác nhau, thường là chất phản ứng khí/lỏng trên bề mặt rắn.

Một chuỗi điển hình:

```text
vận chuyển khối từ pha lớn
→ khuếch tán tới bề mặt
→ hấp phụ
→ khuếch tán/định hướng trên bề mặt
→ phản ứng bề mặt
→ giải hấp
→ vận chuyển sản phẩm ra ngoài
```

Bất kỳ bước nào cũng có thể trở thành giới hạn tốc độ trong điều kiện phù hợp.

Do đó tốc độ đo được không phải lúc nào cũng là tốc độ phản ứng hóa học nội tại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Hấp phụ Langmuir** tiếp nhận điểm tựa từ **Xúc tác dị thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cơ chế Langmuir–Hinshelwood và Eley–Rideal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hấp phụ Langmuir

Một mô hình cơ bản giả định bề mặt có số site hữu hạn và mỗi site chứa tối đa một adsorbate.

Với hấp phụ đơn giản:

\[
\theta=\frac{KP}{1+KP}
\]

Trong đó \(\theta\) là phần site bị chiếm.

Ở áp suất thấp:

\[
\theta\approx KP
\]

Ở áp suất cao:

\[
\theta\rightarrow1
\]

Bề mặt bị bão hòa. Khi đó tăng áp suất chất phản ứng có thể không còn tăng tốc độ nhiều nữa.

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Hấp phụ Langmuir** xác định đầu vào; **Cơ chế Langmuir–Hinshelwood và Eley–Rideal** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Nguyên lý Sabatier và đồ thị núi lửa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cơ chế Langmuir–Hinshelwood và Eley–Rideal

Trong cơ chế **Langmuir–Hinshelwood**, cả hai chất phản ứng đều hấp phụ rồi phản ứng trên bề mặt.

Trong cơ chế **Eley–Rideal**, một chất ở pha khí/lỏng phản ứng trực tiếp với species đã hấp phụ.

Hai mô hình tạo phương trình tốc độ khác nhau. Vì vậy dependence của tốc độ lên áp suất/nồng độ có thể giúp phân biệt cơ chế bề mặt.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Cơ chế Langmuir–Hinshelwood và Eley–Rideal** xác định đầu vào; **Nguyên lý Sabatier và đồ thị núi lửa** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Scaling relations — giới hạn của việc tối ưu một trung gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguyên lý Sabatier và đồ thị núi lửa

Chất phản ứng phải bám đủ mạnh để được hoạt hóa nhưng không mạnh tới mức sản phẩm không thể rời khỏi bề mặt.

**Đồ thị núi lửa (volcano plot)** biểu diễn hoạt tính theo một descriptor như năng lượng hấp phụ.

Phía trái của “núi” có thể là vùng liên kết quá yếu; phía phải là vùng liên kết quá mạnh. Vùng giữa cho cân bằng tối ưu giữa hoạt hóa và giải hấp.

Đây là ví dụ cho thiết kế catalyst dựa trên **descriptor vật lý** thay vì thử ngẫu nhiên.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Nguyên lý Sabatier và đồ thị núi lửa** đã nêu tiêu chí phân biệt, còn **Scaling relations — giới hạn của việc tối ưu một trung gian** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Truyền khối và phản ứng nội tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scaling relations — giới hạn của việc tối ưu một trung gian

Trên nhiều bề mặt, năng lượng hấp phụ của các chất trung gian không hoàn toàn độc lập. Nếu thay đổi vật liệu để ổn định A*, ta có thể đồng thời ổn định B* theo một quan hệ gần tuyến tính.

Những **quan hệ tỉ lệ (scaling relations)** này tạo giới hạn cho hiệu suất catalyst: không thể tối ưu từng intermediate riêng rẽ một cách tùy ý.

Một hướng thiết kế hiện đại là phá các quan hệ này bằng:

- site nhiều chức năng;
- hợp kim;
- giao diện (interface / 인터페이스);
- catalyst phân tử;
- điện trường hoặc môi trường đặc biệt.

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Scaling relations — giới hạn của việc tối ưu một trung gian** đã nêu tiêu chí phân biệt, còn **Truyền khối và phản ứng nội tại** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Hệ số hiệu dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truyền khối và phản ứng nội tại

Nếu chất phản ứng tới bề mặt chậm hơn phản ứng hóa học, tốc độ đo được bị giới hạn bởi truyền khối.

Trong hạt catalyst xốp, còn có khuếch tán trong lỗ xốp.

**Môđun Thiele (Thiele modulus)** là một đại lượng không thứ nguyên so sánh tốc độ phản ứng với tốc độ khuếch tán nội hạt.

Khi phản ứng rất nhanh so với khuếch tán, phần bên trong hạt không được sử dụng hiệu quả.

Điều này giải thích vì sao catalyst có hoạt tính hóa học cao hơn chưa chắc tạo reactor nhanh hơn nếu vận chuyển (transport / 전송) trở thành nút thắt.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Hệ số hiệu dụng** tiếp nhận điểm tựa từ **Truyền khối và phản ứng nội tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xúc tác enzyme** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ số hiệu dụng

**Hệ số hiệu dụng (effectiveness factor)**:

\[
\eta=\frac{\văn bản (text / 텍스트){tốc độ thực trong hạt}}{\văn bản (text / 텍스트){tốc độ nếu toàn hạt ở nồng độ bề mặt}}
\]

Nếu \(\eta<1\), khuếch tán nội hạt đang làm giảm mức sử dụng catalyst.

Đây là cầu nối giữa hóa động học và kỹ thuật phản ứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Xúc tác enzyme** tiếp nhận điểm tựa từ **Hệ số hiệu dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu quả xúc tác enzyme** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xúc tác enzyme

**Enzyme (효소)** là chất xúc tác sinh học. Vị trí hoạt động tạo một vi môi trường có hình học, điện trường và tương tác động phù hợp để ổn định trạng thái chuyển tiếp.

Không nên chỉ hiểu enzyme theo mô hình “ổ khóa–chìa khóa” cứng nhắc. Sự thích nghi cấu dạng, tập hợp nhiều cấu dạng và ổn định trạng thái chuyển tiếp đều quan trọng.

Với nhiều hệ enzyme, mô hình Michaelis–Menten cho:

\[
v=\frac{V_{max}[S]}{K_M+[S]}
\]

Ở `[S]` thấp, tốc độ gần tỉ lệ với `[S]`. Ở `[S]` cao, enzyme tiến tới bão hòa và tốc độ gần `V_max`.

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Hiệu quả xúc tác enzyme** tiếp nhận điểm tựa từ **Xúc tác enzyme** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ chọn lọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu quả xúc tác enzyme

Ở nồng độ substrate thấp:

\[
v\approx\frac{k_{cat}}{K_M}[E][S]
\]

Tỉ số:

\[
\frac{k_{cat}}{K_M}
\]

được dùng như thước đo hiệu quả xúc tác trong vùng dilute substrate.

Một số enzyme tiến gần giới hạn khuếch tán, nghĩa là gần như mỗi lần substrate gặp enzyme đúng cách đều dẫn đến phản ứng.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Độ chọn lọc** tiếp nhận điểm tựa từ **Hiệu quả xúc tác enzyme** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngộ độc xúc tác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ chọn lọc

Chất xúc tác có thể ưu tiên một con đường so với các con đường cạnh tranh bằng cách hạ hàng rào của một trạng thái chuyển tiếp mạnh hơn những trạng thái khác.

Nếu hai sản phẩm P1 và P2 hình thành qua hai hàng rào:

\[
\Delta G_1^\ddagger,\quad\Delta G_2^\ddagger
\]

thì tỉ lệ sản phẩm động học có thể nhạy theo:

\[
\frac{k_1}{k_2}\sim e^{-(\Delta G_1^\ddagger-\Delta G_2^\ddagger)/(RT)}
\]

Chênh lệch năng lượng nhỏ có thể tạo chọn lọc lớn.

**Xúc tác bất đối xứng (asymmetric catalysis)** tận dụng điều này để ưu tiên một enantiomer bằng môi trường trạng thái chuyển tiếp đối quang.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Ngộ độc xúc tác** tiếp nhận điểm tựa từ **Độ chọn lọc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Suy giảm hoạt tính xúc tác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngộ độc xúc tác

Một impurity hấp phụ mạnh vào site hoạt động có thể làm giảm mạnh tốc độ dù nồng độ rất thấp.

Ví dụ sulfur có thể đầu độc nhiều catalyst kim loại vì liên kết mạnh với bề mặt.

Ngộ độc khác với **ức chế thuận nghịch** nếu species có thể rời đi dễ dàng. Trong catalyst công nghiệp, phân biệt các cơ chế mất hoạt tính giúp chọn chiến lược tái sinh.

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Suy giảm hoạt tính xúc tác** tiếp nhận điểm tựa từ **Ngộ độc xúc tác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một số ví dụ công nghiệp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suy giảm hoạt tính xúc tác

Các cơ chế chính gồm:

- thiêu kết (sintering): hạt lớn lên, diện tích bề mặt giảm;
- đóng cốc (coking): carbon phủ site;
- ngộ độc hóa học;
- biến đổi pha;
- mất kim loại hoạt tính;
- hòa tan/leaching;
- biến tính enzyme.

Hoạt tính ban đầu cao không đủ; tuổi thọ và khả năng tái sinh quyết định hiệu quả thực tế.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Suy giảm hoạt tính xúc tác** cho ta quy tắc; **Một số ví dụ công nghiệp** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Xúc tác điện hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một số ví dụ công nghiệp

Quá trình Haber–Bosch dùng catalyst nền sắt để tăng tốc hoạt hóa `N₂` và hydro hóa các species bề mặt.

Bộ chuyển đổi xúc tác trên ô tô dùng hệ Pt/Pd/Rh để thúc đẩy oxi hóa CO, oxi hóa hydrocarbon và khử `NOx`.

Chất xúc tác polymer hóa có thể kiểm soát sự phát triển chuỗi, khối lượng phân tử và cấu hình lập thể của polymer.

Hydrogenation catalyst dùng kim loại như Ni, Pd hoặc Pt để hoạt hóa `H₂` và liên kết không no.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Một số ví dụ công nghiệp** cho ta quy tắc; **Xúc tác điện hóa** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Xúc tác quang** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xúc tác điện hóa

Trong điện xúc tác, tốc độ phản ứng phụ thuộc đồng thời:

- năng lượng hấp phụ;
- chuyển electron;
- thế điện cực;
- môi trường điện ly;
- cấu trúc lớp điện kép;
- vận chuyển khối.

Ví dụ phản ứng khử oxygen trong pin nhiên liệu không thể được hiểu chỉ bằng năng lượng liên kết O–metal; thế điện hóa và proton transfer cũng tham gia.

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Xúc tác quang** tiếp nhận điểm tựa từ **Xúc tác điện hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thiết kế chất xúc tác bằng tính toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xúc tác quang

Trong quang xúc tác, photon tạo trạng thái kích thích hoặc electron–hole pair có khả năng thúc đẩy phản ứng.

Một catalyst quang tốt cần đồng thời:

- hấp thụ photon phù hợp;
- tách hạt tải đủ lâu;
- chuyển điện tích tới chất phản ứng;
- hạn chế tái hợp;
- có bề mặt phản ứng chọn lọc.

Đây là giao điểm giữa quang hóa, vật liệu và xúc tác bề mặt.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Thiết kế chất xúc tác bằng tính toán** tiếp nhận điểm tựa từ **Xúc tác quang** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ cơ chế tới thiết kế catalyst** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thiết kế chất xúc tác bằng tính toán

**Lý thuyết phiếm hàm mật độ (density functional theory, DFT)** có thể ước lượng:

- năng lượng hấp phụ;
- cấu trúc trung gian;
- hàng rào phản ứng;
- điện tích và trạng thái điện tử.

Học máy có thể xây mô hình thay thế để sàng lọc nhanh hàng nghìn thành phần hoặc bề mặt trước khi làm tính toán chính xác hơn.

Tuy nhiên dự đoán catalyst cần tránh một lỗi quan trọng: tối ưu một descriptor đơn lẻ trong khi catalyst thật còn chịu ảnh hưởng của ổn định pha, vận chuyển (transport / 전송), solvent, điện trường và suy giảm hoạt tính.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Thiết kế chất xúc tác bằng tính toán** xác định đầu vào; **Từ cơ chế tới thiết kế catalyst** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Các hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ cơ chế tới thiết kế catalyst

Một chiến lược có hệ thống là:

```text
xác định mạng phản ứng
→ xác định trạng thái nghỉ
→ đo/phỏng đoán bước kiểm soát tốc độ
→ xác định descriptor năng lượng
→ sửa cấu trúc catalyst
→ kiểm tra activity + selectivity + stability
```

Đây là sự khác biệt giữa “thử catalyst” và **thiết kế catalyst dựa trên cơ chế**.

> **Chuyển mạch:** Trong **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Từ cơ chế tới thiết kế catalyst** xác định đầu vào; **Các hiểu lầm thường gặp** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các hiểu lầm thường gặp

### “Chất xúc tác làm phản ứng thuận lợi hơn về nhiệt động”

Không. Nó không đổi `ΔG` cân bằng; nó thay đổi tốc độ và con đường.

### “Chất xúc tác không bao giờ bị tiêu hao”

Trong chu trình lý tưởng, chất xúc tác được tái sinh. Trong thực tế, nó có thể suy giảm hoạt tính hoặc tham gia phản ứng phụ.

### “Càng nhiều chất xúc tác thì tốc độ luôn tăng tuyến tính”

Không. Sự truyền khối, bão hòa vị trí hoạt động và thay đổi cơ chế có thể làm quan hệ không tuyến tính.

### “Bước có hàng rào lớn nhất luôn là bước duy nhất quyết định tốc độ”

Không phải lúc nào cũng vậy. Nhiều bước và trạng thái có thể đồng thời kiểm soát tốc độ toàn chu trình.

### “Liên kết chất phản ứng càng mạnh thì catalyst càng tốt”

Không. Liên kết quá mạnh có thể làm intermediate hoặc sản phẩm không rời được bề mặt.

### “Hoạt tính cao là đủ để catalyst tốt”

Không. Độ chọn lọc, tuổi thọ, khả năng tái sinh, chi phí và vận chuyển (transport / 전송) đều quan trọng.

> **Chuyển mạch:** Ở chặng này của **Xúc tác — thay đổi con đường phản ứng mà không đổi cân bằng**, **Mô hình tư duy** gom các mảnh từ **Các hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Chất xúc tác là **kỹ sư tuyến đường trên địa hình năng lượng**. Nó không hạ thung lũng đích; nó thay đổi các đèo, hố trung gian và giao lộ giữa các con đường. Catalyst tốt không chỉ làm một bước nhanh hơn mà phải điều phối cả chu trình để chất phản ứng vào được, trạng thái chuyển tiếp được ổn định đúng mức, sản phẩm thoát ra được và catalyst sống đủ lâu để quay vòng nhiều lần.

Xem tiếp: [Cân bằng động](../07_chemical_equilibrium/00_dynamic_equilibrium.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
