# Phân hạch và nhiệt hạch — đưa hạt nhân về trạng thái liên kết bền hơn

> **Phân hạch (fission / 핵분열)** chia một hạt nhân rất nặng thành các mảnh khối lượng trung bình; **nhiệt hạch (fusion / 핵융합)** kết hợp các hạt nhân nhẹ thành hạt nhân nặng hơn. Cả hai có thể giải phóng năng lượng vì sản phẩm dịch về vùng có năng lượng liên kết trên mỗi nucleon cao hơn. Nguyên lý nền không phải “tách thì sinh năng lượng” hay “ghép thì sinh năng lượng”, mà là **hệ chuyển tới trạng thái hạt nhân liên kết chặt hơn**.

Chapter này dựa trực tiếp trên [năng lượng liên kết hạt nhân](./00_atomic_nucleus.md), [động học phân rã](./01_radioactivity.md) và [giá trị Q, tiết diện, neutron moderation](./02_nuclear_reactions.md). Khi đi tới chuyển nhiệt thành điện, có thể liên hệ lại [nhiệt động lực học](../05_thermodynamics/00_energy_heat_and_work.md); khi đi tới hư hại do neutron, các ý tưởng về [khuyết tật vật liệu](../14_materials_and_polymer_chemistry/01_metals_ceramics_and_glasses.md) trở nên quan trọng.

## Đường cong năng lượng liên kết là bức tranh thống nhất

Năng lượng liên kết trung bình trên mỗi nucleon tăng nhanh từ hydrogen tới vùng Fe/Ni, rồi giảm chậm ở các hạt nhân nặng hơn.

Vì vậy:

```text
hạt nhân nhẹ → nhiệt hạch có thể giải phóng năng lượng
hạt nhân rất nặng → phân hạch có thể giải phóng năng lượng
```

Các hạt nhân gần vùng sắt đã nằm gần cực đại độ bền liên kết, nên việc phân hạch hoặc nhiệt hạch quanh vùng này thường không giải phóng năng lượng lớn theo cách của các hạt rất nhẹ hoặc rất nặng.

## Cơ chế phân hạch — từ biến dạng tới tách đôi

Một hạt nhân nặng có thể hấp thụ neutron hoặc nhận kích thích khác rồi trở nên biến dạng.

Hai xu hướng cạnh tranh xuất hiện. Thành phần liên kết hạt nhân giống sức căng bề mặt ưu tiên hình dạng gọn, còn lực đẩy Coulomb giữa proton lại làm các vùng giàu proton có xu hướng tách xa nhau.

Nếu biến dạng vượt **hàng rào phân hạch (fission barrier)**, hạt nhân có thể tách thành các mảnh riêng biệt.

## Sản phẩm phân hạch điển hình

Phân hạch của actinide nặng thường tạo hai mảnh không hoàn toàn bằng nhau, kèm một số neutron và bức xạ gamma.

Các mảnh phân hạch thường giàu neutron nên tiếp tục phân rã beta về các đồng vị bền hơn.

Chính sự phân rã chậm của các sản phẩm này góp phần tạo **nhiệt phân rã (decay heat)** sau khi phản ứng dây chuyền đã dừng.

## Neutron tức thời và neutron trễ

Phần lớn neutron phân hạch được phát ra gần như ngay lập tức và được gọi là **neutron tức thời (prompt neutron)**.

Một phần nhỏ được phát ra sau khi một số sản phẩm phân hạch trải qua phân rã beta; đó là **neutron trễ (delayed neutron)**.

Tỉ lệ neutron trễ nhỏ nhưng rất quan trọng với khả năng điều khiển động học lò phản ứng vì nó kéo dài thang thời gian đáp ứng của hệ.

## Phản ứng dây chuyền

Một neutron gây phân hạch; phân hạch giải phóng nhiều neutron; một phần các neutron đó lại có thể gây phân hạch tiếp theo.

Hệ số nhân neutron \(k\) mô tả xu hướng này:

```text
k < 1  dưới tới hạn
k = 1  tới hạn, quần thể neutron ổn định trung bình
k > 1  trên tới hạn, quần thể có xu hướng tăng
```

Trong lò phản ứng điện hạt nhân, mục tiêu vận hành là giữ phản ứng dây chuyền được kiểm soát gần trạng thái tới hạn với các cơ chế phản hồi, điều khiển và dừng an toàn.

### Ví dụ suy luận: vì sao `k = 1` không có nghĩa “nguy hiểm nhất”?

`k = 1` chỉ nói rằng trung bình mỗi thế hệ neutron tạo ra đủ neutron hữu hiệu để duy trì thế hệ kế tiếp ở cùng mức. Hệ có an toàn hay không còn phụ thuộc độ lớn công suất, tốc độ phản hồi, khả năng loại nhiệt, trạng thái vật liệu và biên độ điều khiển. Một thuật ngữ neutron-kinetics không thể thay thế toàn bộ đánh giá an toàn hệ thống.

## Kinh tế neutron

Không phải neutron nào sinh ra cũng gây phân hạch tiếp theo. Neutron có thể thoát khỏi hệ, bị hấp thụ mà không gây phân hạch, bị làm chậm tới vùng năng lượng có tiết diện khác hoặc tương tác với vật liệu không phân hạch.

Vì vậy hình học và thành phần vật liệu quyết định mạnh hành vi của chuỗi neutron.

## Vật liệu phân hạch và vật liệu sinh nhiên liệu

**Đồng vị phân hạch được (fissile isotope)** có thể duy trì phản ứng dây chuyền phân hạch với neutron thích hợp, chẳng hạn U-235 hoặc Pu-239.

**Đồng vị sinh nhiên liệu (fertile isotope)** không nhất thiết phân hạch hiệu quả với neutron chậm nhưng có thể bắt neutron rồi biến đổi thành đồng vị fissile, ví dụ chuỗi từ U-238 tới Pu-239.

Đây là phân loại theo con đường phản ứng hạt nhân, không đơn giản là “phóng xạ hay không phóng xạ”.

## Làm chậm neutron

Trong nhiều thiết kế lò phản ứng, neutron nhanh sinh ra từ phân hạch được làm chậm vì tiết diện phân hạch của U-235 với neutron nhiệt tương đối lớn.

Nước nhẹ, nước nặng và graphite là những ví dụ về **chất làm chậm (moderator)**.

Chất làm chậm chủ yếu giảm năng lượng neutron qua tán xạ, còn vật liệu hấp thụ điều khiển lại loại neutron khỏi quần thể. Hai vai trò này không giống nhau.

## Khái niệm kiểm soát lò phản ứng

Một hệ điện hạt nhân có kiểm soát kết hợp nhiều thành phần như nhiên liệu, chất làm chậm khi cần, vật liệu hấp thụ điều khiển, chất tải nhiệt, kết cấu bao che, hệ giám sát và cơ chế dừng.

Ở cấp khái niệm, bài toán vật lý là **quản lý phản ứng dây chuyền đồng thời loại nhiệt một cách ổn định**.

## Phản hồi âm

Hành vi an toàn hơn thường đi kèm các hệ số phản hồi khiến nhiệt độ tăng làm độ phản ứng giảm.

Ví dụ, nhiệt độ nhiên liệu tăng có thể làm các cộng hưởng hấp thụ neutron rộng hơn do hiệu ứng Doppler, khiến xác suất bắt neutron của một số đồng vị tăng và làm xu hướng nhân neutron giảm.

Phản hồi âm giúp hệ có khả năng tự ổn định hơn trước một số nhiễu loạn, nhưng không thay thế các hệ bảo vệ chủ động và thụ động khác.

## Nhiệt phân rã

Ngay cả sau khi phản ứng dây chuyền phân hạch dừng, nhiều sản phẩm phân hạch vẫn tiếp tục phân rã phóng xạ và sinh nhiệt.

Do đó việc làm mát vẫn cần thiết sau khi tắt lò. “Dừng phản ứng dây chuyền” không có nghĩa công suất nhiệt lập tức trở về 0.

## Chu trình nhiên liệu hạt nhân

Một chu trình nhiên liệu có thể bao gồm khai thác và chuẩn bị nhiên liệu, làm giàu trong một số hệ, chiếu xạ trong lò phản ứng, làm nguội và lưu giữ nhiên liệu đã qua sử dụng, tái xử lý ở một số mô hình và cuối cùng là điều kiện hóa hoặc thải bỏ chất thải.

Tác động môi trường vì vậy cần được đánh giá trên toàn chu trình chứ không chỉ trong lõi lò phản ứng.

## Nhiên liệu đã qua sử dụng

Nhiên liệu đã qua sử dụng có thể chứa uranium còn lại, sản phẩm phân hạch, nguyên tố siêu uranium và sản phẩm kích hoạt.

Mức sinh nhiệt và độc tính phóng xạ thay đổi theo thời gian vì mỗi đồng vị có chu kỳ bán rã khác nhau.

## Quản lý chất thải hạt nhân

Chiến lược quản lý phụ thuộc hoạt độ, chu kỳ bán rã, mức sinh nhiệt và dạng hóa học của chất thải.

Các đồng vị sống ngắn giảm đáng kể hoạt độ sau nhiều chu kỳ bán rã; các actinide sống lâu đòi hỏi chiến lược cô lập lâu dài hơn.

Vật liệu cố định chất thải và các hàng rào địa chất được thiết kế để giảm khả năng phát tán ra môi trường trong thời gian cần thiết.

## Chuyển năng lượng phân hạch thành điện

Phần lớn năng lượng động học của các mảnh phân hạch cuối cùng chuyển thành nhiệt qua va chạm trong nhiên liệu.

Nhiệt sau đó được chuyển sang chất tải nhiệt và hệ chuyển đổi nhiệt động như turbine hơi trong nhiều nhà máy.

Vì vậy ở cấp vĩ mô, nhà máy điện hạt nhân vẫn là một hệ động cơ nhiệt; điểm khác là nguồn nhiệt đến từ phản ứng hạt nhân thay vì phản ứng cháy. Giới hạn hiệu suất vì thế vẫn liên quan đến nhiệt động lực học của chu trình nhiệt, không phải chỉ đến năng lượng mỗi phân hạch.

## Nhiệt hạch — vượt lực đẩy Coulomb

Hai hạt nhân tích điện dương đẩy nhau bằng lực Coulomb.

Để nhiệt hạch xảy ra, chúng phải tiến đủ gần để tương tác hạt nhân mạnh trở nên đáng kể.

Theo cơ học cổ điển điều này cần động năng rất cao; xuyên hầm lượng tử cho phép một phần va chạm tạo phản ứng ngay cả khi năng lượng thấp hơn đỉnh hàng rào Coulomb.

## Nhiệt hạch trong sao

Các sao giống Mặt Trời chủ yếu sử dụng chuỗi proton–proton, có phản ứng tổng quát gần:

\[
4p\rightarrow{}^4He+\text{năng lượng}+\text{neutrino}+...
\]

Khối lượng sản phẩm helium nhỏ hơn tổng khối lượng bốn proton ban đầu; chênh lệch xuất hiện dưới dạng năng lượng giải phóng.

## Vì sao sao cần nhiệt độ rất cao

Nhiệt độ cao tạo phân bố vận tốc rộng và tăng tần suất va chạm giữa ion.

Tốc độ nhiệt hạch phụ thuộc đồng thời vào phần đuôi năng lượng cao của phân bố Maxwell–Boltzmann và xác suất xuyên hầm. Sự kết hợp này tạo vùng năng lượng hiệu quả thường gọi là **đỉnh Gamow (Gamow peak)**.

Vì vậy không phải mọi hạt đều phải có động năng cao hơn hàng rào Coulomb cổ điển.

## Nhiệt hạch trên Trái Đất

Một phản ứng được nghiên cứu nhiều là deuterium–tritium:

\[
D+T\rightarrow{}^4He+n+17.6\,MeV
\]

Phản ứng này được quan tâm vì có tiết diện tương đối thuận lợi ở vùng nhiệt độ plasma có thể tiếp cận hơn so với nhiều phản ứng nhiệt hạch khác.

## Plasma

Ở nhiệt độ nhiệt hạch, vật chất ở trạng thái **plasma**, trong đó electron và ion không còn tạo nguyên tử trung hòa ổn định như ở điều kiện thường.

Các hạt tích điện tương tác tập thể với trường điện từ. Để thu được năng lượng, plasma phải được giữ đủ nóng và đủ đặc trong thời gian đủ lâu để tốc độ phản ứng cạnh tranh được với các cơ chế mất năng lượng.

## Tiêu chí Lawson

Hiệu năng nhiệt hạch phụ thuộc vào mật độ hạt, thời gian giam giữ năng lượng và nhiệt độ.

Một đại lượng tổng hợp thường được biểu diễn bằng **tích ba (triple product)**:

\[
nT\tau_E
\]

Hệ phải đạt một mức đủ lớn, tùy phản ứng và cấu hình, để hướng tới điều kiện tạo năng lượng ròng.

### Trade-off của Lawson

Không thể chỉ tăng một biến mà bỏ qua các biến còn lại. Tăng mật độ có thể làm va chạm hữu ích nhiều hơn nhưng cũng làm các bất ổn và tải vật liệu thay đổi; tăng nhiệt độ giúp tốc độ nhiệt hạch nhưng làm yêu cầu giam giữ khó hơn; tăng thời gian giam giữ đòi hỏi kiểm soát mất mát và ổn định plasma tốt hơn. Nhiệt hạch là bài toán **đồng thời về reaction rate, confinement và materials**, không phải chỉ đạt một “nhiệt độ đủ cao”.

## Giam giữ từ

Tokamak và stellarator sử dụng từ trường để dẫn hướng các hạt tích điện, vì plasma nhiệt độ rất cao không thể tiếp xúc trực tiếp lâu với thành vật liệu.

Các thách thức chính gồm nhiễu loạn plasma, mất ổn định, thoát nhiệt và tương tác plasma–thành.

## Giam giữ quán tính

Một hướng khác là nén rất nhanh viên nhiên liệu nhỏ bằng laser hoặc chùm hạt.

Mục tiêu là đạt mật độ rất cao trong thời gian rất ngắn trước khi mục tiêu giãn nở trở lại.

Giam giữ từ và giam giữ quán tính giải cùng bài toán tổng quát bằng hai miền mật độ–thời gian khác nhau.

## Thách thức tritium

Tritium là đồng vị phóng xạ và nguồn tự nhiên rất hạn chế.

Nhiều ý tưởng lò nhiệt hạch dự kiến sinh tritium từ lithium bằng neutron nhiệt hạch.

Điều này tạo thêm bài toán về vật liệu hạt nhân, hóa học, quản lý đồng vị và kỹ thuật, vượt ra ngoài riêng vật lý plasma.

## Hư hại vật liệu do neutron

Phản ứng D–T tạo neutron năng lượng cao. Neutron có thể làm bật nguyên tử khỏi vị trí mạng, tạo khuyết tật và kích hoạt vật liệu cấu trúc.

Vì vậy hệ nhiệt hạch vẫn phải giải quyết các vấn đề vật liệu dưới bức xạ, dù chu trình nhiên liệu khác phân hạch.

Các khái niệm vacancy, interstitial, dislocation và suy giảm tính cơ có thể liên hệ lại [vật liệu kim loại/gốm/thủy tinh](../14_materials_and_polymer_chemistry/01_metals_ceramics_and_glasses.md).

## Nhiệt hạch không đồng nghĩa “không có chất thải”

Nhiệt hạch tránh tạo trực tiếp phổ sản phẩm phân hạch dài như nhiên liệu phân hạch, nhưng neutron có thể kích hoạt vật liệu cấu trúc và tritium vẫn cần được quản lý.

Hồ sơ rủi ro khác phân hạch, chứ không biến mất hoàn toàn.

## Tổng hợp hạt nhân trong sao

Nhiệt hạch trong sao xây dựng các nguyên tố dần tới vùng sắt qua nhiều giai đoạn đốt hạt nhân.

Các nguyên tố nặng hơn phần lớn hình thành qua các quá trình bắt neutron trong các môi trường thiên văn như sao tiến hóa, siêu tân tinh hoặc va chạm sao neutron.

Các nguyên tố hóa học ta sử dụng vì vậy là sản phẩm của lịch sử hạt nhân thiên văn.

## Mật độ năng lượng

Phản ứng hạt nhân giải phóng năng lượng trên mỗi đơn vị khối lượng lớn hơn phản ứng cháy hóa học qua nhiều bậc độ lớn vì thang năng lượng liên kết hạt nhân là MeV trên mỗi hạt nhân, trong khi liên kết hóa học thường ở thang eV trên mỗi phân tử.

Mật độ năng lượng cao vừa là lợi thế vừa tạo yêu cầu kỹ thuật và an toàn rất lớn.

## Khác biệt an toàn giữa phân hạch và nhiệt hạch

Phân hạch có phản ứng dây chuyền và nhiệt phân rã nên cần quản lý độ phản ứng, làm mát và chất thải lâu dài.

Plasma nhiệt hạch không duy trì phản ứng nếu điều kiện giam giữ mất đi, nhưng hệ vẫn có vật liệu bị kích hoạt, tritium, từ trường mạnh và năng lượng lưu trữ đáng kể cần được quản lý.

Vì vậy không nên nén so sánh hai công nghệ thành một nhãn đơn giản “an toàn” hoặc “nguy hiểm”.

## Những hiểu lầm thường gặp

### “Cứ tách nguyên tử là giải phóng năng lượng”

Không. Chỉ khi sản phẩm có tổng khối lượng thấp hơn hoặc năng lượng liên kết thuận lợi hơn thì mới có năng lượng ròng được giải phóng.

### “Nhiệt hạch cần nhiệt độ đủ để mọi hạt vượt hàng rào Coulomb”

Không. Xuyên hầm lượng tử cho phép phản ứng xảy ra dưới năng lượng hàng rào cổ điển.

### “Nhiệt hạch không tạo bức xạ”

Không đúng. Phản ứng D–T tạo neutron năng lượng cao và có thể kích hoạt vật liệu.

### “Tới hạn nghĩa là lò phản ứng đang mất kiểm soát”

Không. Trong thuật ngữ lò phản ứng, tới hạn \(k=1\) chỉ nghĩa quần thể neutron và tốc độ phản ứng dây chuyền ổn định trung bình.

### “Mật độ năng lượng cao nghĩa công nghệ chắc chắn hiệu quả hơn”

Không. Hiệu suất chuyển đổi, kiểm soát nhiệt, vật liệu, chu trình nhiên liệu và yêu cầu an toàn quyết định hiệu quả của hệ hoàn chỉnh.

## Mô hình tư duy

Phân hạch và nhiệt hạch là **hai con đường khác nhau đi xuống cảnh quan năng lượng liên kết hạt nhân**. Phân hạch quản lý một chuỗi nhân neutron trong hạt nhân nặng; nhiệt hạch cố giữ hạt nhân nhẹ đủ gần, đủ lâu để xuyên hầm qua hàng rào Coulomb và tạo sản phẩm liên kết chặt hơn.

Xem tiếp: [Hóa phóng xạ và ứng dụng](./04_radiochemistry_and_applications.md).