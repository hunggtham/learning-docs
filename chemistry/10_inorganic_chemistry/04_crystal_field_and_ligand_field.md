# Trường tinh thể và trường phối tử — sự tách mức orbital d

> **Lý thuyết trường tinh thể (crystal field theory, CFT / 결정장 이론)** mô hình hóa phối tử như nguồn trường tĩnh điện làm mất tính suy biến của các orbital d trên kim loại. **Lý thuyết trường phối tử (ligand field theory, LFT / 리간드장 이론)** mở rộng mô hình đó bằng liên kết orbital phân tử và thành phần cộng hóa trị. Hai mô hình giúp giải thích màu sắc, từ tính, trạng thái spin, hình học và một phần khả năng phản ứng của phức kim loại chuyển tiếp.

Điểm quan trọng nhất không phải học thuộc sơ đồ \(t_{2g}\) và \(e_g\), mà hiểu rằng **đối xứng của môi trường phối tử làm các orbital d tương tác khác nhau**, từ đó tái định hình trạng thái điện tử của tâm kim loại.

Chapter này tiếp nối trực tiếp [cấu hình electron](../01_atomic_structure/03_electron_configuration.md), [orbital phân tử](../02_chemical_bonding/06_molecular_orbital_theory.md) và [hóa học phối trí](./03_coordination_chemistry.md). Khi phần màu sắc và chuyển mức xuất hiện, [phổ học](../12_analytical_chemistry/03_spectroscopy.md) cung cấp góc nhìn phép đo; khi phần spin và vật liệu xuất hiện, các ý tưởng sẽ nối tiếp sang [hóa học trạng thái rắn và khuyết tật](./05_solid_state_and_defect_chemistry.md).

## Bắt đầu từ ion kim loại tự do

Một ion kim loại chuyển tiếp cô lập trong môi trường cầu lý tưởng có năm orbital d cùng năng lượng; chúng được gọi là **suy biến (degenerate)**.

Năm orbital có định hướng không gian khác nhau. \(d_{z^2}\) và \(d_{x^2-y^2}\) có các thùy hướng dọc các trục tọa độ, trong khi \(d_{xy}\), \(d_{xz}\), \(d_{yz}\) chủ yếu hướng giữa các trục.

Khi phối tử tiến tới theo một hình học xác định, khác biệt định hướng trở thành khác biệt về năng lượng tương tác. Đây là điểm cốt lõi: **hình học không chỉ thay đổi hình dáng phân tử mà còn thay đổi Hamiltonian điện tử**.

## Trường bát diện — vì sao \(e_g\) cao hơn \(t_{2g}\)

Trong phức bát diện, sáu phối tử nằm dọc \(+x,-x,+y,-y,+z,-z\).

Hai orbital \(d_{x^2-y^2}\) và \(d_{z^2}\) hướng trực tiếp về phía phối tử nên chịu đẩy tĩnh điện và tương tác orbital mạnh hơn. Chúng tăng năng lượng và tạo tập \(e_g\).

Ba orbital \(d_{xy}\), \(d_{xz}\), \(d_{yz}\) hướng giữa các trục phối tử nên tương tác trực tiếp yếu hơn và tạo tập \(t_{2g}\) năng lượng thấp hơn.

Khoảng cách năng lượng giữa hai tập gọi là **độ tách bát diện \(\Delta_o\) (octahedral splitting)**.

## Tâm trọng năng lượng — sự tách mức không tự tạo hay phá năng lượng orbital trung bình

Trong CFT tĩnh điện thuần túy, sự tách mức được đo tương đối so với mức trung bình ban đầu:

\[
t_{2g}: -0.4\Delta_o
\]

\[
e_g: +0.6\Delta_o
\]

Ba orbital \(t_{2g}\) và hai orbital \(e_g\) cho tổng có trọng số:

\[
3(-0.4\Delta_o)+2(+0.6\Delta_o)=0
\]

Điều này không có nghĩa tổng năng lượng phân tử không thay đổi khi phối tử liên kết. Nó chỉ nói phần tách mức d trong mô hình CFT được tham chiếu quanh năng lượng trung bình của năm orbital d.

## Cách electron chiếm mức: cạnh tranh giữa tách mức và ghép đôi

Khi điền electron d, hệ phải cân nhắc hai loại chi phí năng lượng:

- đưa electron lên tập orbital cao hơn, tốn khoảng \(\Delta_o\);
- ghép hai electron trong cùng orbital, tốn **năng lượng ghép đôi \(P\) (pairing energy)** do đẩy electron–electron và mất một phần ổn định trao đổi.

Nếu:

\[
\Delta_o < P
\]

thì trạng thái **spin cao (high spin)** thường thuận lợi hơn.

Nếu:

\[
\Delta_o > P
\]

thì trạng thái **spin thấp (low spin)** có thể thuận lợi hơn.

Cạnh tranh này đặc biệt quan trọng với cấu hình bát diện \(d^4\) đến \(d^7\). Với \(d^1\)–\(d^3\), chưa cần ghép đôi để ở lại \(t_{2g}\); còn \(d^8\)–\(d^{10}\) có mức chiếm electron bị ràng buộc hơn.

## Ví dụ: Fe(II) d6

\(Fe^{2+}\) là \(d^6\).

Trong trường yếu, cấu hình spin cao có bốn electron độc thân. Trong trường mạnh, cấu hình spin thấp \(d^6\) có:

\[
t_{2g}^6e_g^0
\]

và tất cả electron được ghép đôi.

Vì vậy cùng trạng thái oxy hóa Fe(II) nhưng phối tử khác nhau có thể tạo hành vi từ tính hoàn toàn khác. Chỉ biết số oxy hóa chưa đủ để suy trạng thái spin.

## Năng lượng ổn định trường tinh thể

**Năng lượng ổn định trường tinh thể (crystal-field stabilization energy, CFSE / 결정장 안정화 에너지)** đo mức ổn định tương đối so với tâm trọng do electron chiếm các orbital đã tách mức.

Ví dụ với cấu hình bát diện \(d^3\):

\[
CFSE = 3(-0.4\Delta_o) = -1.2\Delta_o
\]

Nếu có ghép đôi electron, khi so sánh tổng năng lượng còn phải cộng thêm các hạng năng lượng ghép đôi.

CFSE giúp giải thích định tính năng lượng hydrat hóa, hình học ưu tiên, vị trí ion trong chất rắn và một số xu hướng động học. Tuy nhiên nó không phải tổng năng lượng liên kết của toàn phức.

### Giới hạn của CFSE

Hai phức có CFSE tương tự chưa chắc có độ bền nhiệt động, tốc độ thế phối tử hay năng lượng liên kết giống nhau. CFSE chỉ là một đóng góp điện tử trong một mô hình có độ phân giải hữu hạn; solvat hóa, entropy, cộng hóa trị và cấu trúc phối tử vẫn có thể thay đổi mạnh tổng \(\Delta G\).

## Dãy phổ hóa học — bản chất phối tử thay đổi \(\Delta\)

Các phối tử không tạo trường có độ mạnh giống nhau. Một dãy gần đúng từ trường yếu tới mạnh là:

\[
I^- < Br^- < Cl^- < F^- < H_2O < NH_3 < en < CN^- < CO
\]

Thứ tự chi tiết có thể phụ thuộc hoàn cảnh, nhưng xu hướng phản ánh tương tác liên kết thực chứ không phải một danh sách tùy ý.

Phối tử trường yếu thường tạo \(\Delta_o\) nhỏ và ưu tiên spin cao. Phối tử trường mạnh tạo tách mức lớn hơn và có thể ưu tiên spin thấp.

## Vì sao CO và CN− là phối tử trường mạnh — cần mô hình trường phối tử và orbital phân tử

CFT thuần túy chỉ nói phối tử “tạo trường” nhưng không giải thích sâu vì sao phối tử nhận π lại mạnh.

Trong LFT, cho σ từ phối tử tạo các tổ hợp liên kết và phản liên kết. Với phối tử nhận π như CO, orbital d kiểu \(t_{2g}\) đã chiếm trên kim loại có thể cho ngược electron vào orbital \(\pi^*\) của phối tử. Tương tác này làm ổn định tập \(t_{2g}\) và tăng \(\Delta_o\).

Ngược lại, phối tử cho π có các orbital π đã chiếm tương tác với \(t_{2g}\) của kim loại, có thể nâng năng lượng các orbital này và làm giảm độ tách mức.

Vì vậy dãy phổ hóa học xuất hiện từ **đối xứng orbital + mức tương hợp năng lượng + khả năng cho/nhận π**.

## Trường tứ diện — thứ tự đảo nhưng độ tách nhỏ hơn

Trong phức tứ diện, phối tử tiến vào theo hướng giữa các trục tọa độ. Do đó các orbital từng hướng trực tiếp tới phối tử trong hình học bát diện không còn chịu tương tác mạnh nhất theo cùng cách.

Thứ tự tách mức đảo: tập \(e\) thấp hơn và tập \(t_2\) cao hơn. Độ tách thường nhỏ:

\[
\Delta_t \approx \frac{4}{9}\Delta_o
\]

khi so sánh lý tưởng cùng kim loại và phối tử.

Vì \(\Delta_t\) nhỏ, chi phí đưa electron lên mức cao thường thấp hơn ghép đôi; do đó phức tứ diện gần như luôn spin cao.

## Trường vuông phẳng — vì sao hệ d8 thường ưa hình học này

Trong hình học vuông phẳng, bốn phối tử nằm trên mặt phẳng x/y và không có phối tử trục z. Orbital \(d_{x^2-y^2}\) hướng thẳng vào cả bốn phối tử nên bị nâng năng lượng rất mạnh.

Một sơ đồ tách mức điển hình cho phép hệ \(d^8\) lấp các orbital thấp hơn và để \(d_{x^2-y^2}\) trống, tạo mức ổn định lớn. Đây là lý do Pt(II), Pd(II) và nhiều phức Ni(II) trường mạnh thường có hình học vuông phẳng.

Vì vậy ưu tiên hình học có nguồn gốc điện tử, không chỉ do hình dạng lập thể.

### Ví dụ suy luận: cùng Ni(II), vì sao hình học có thể khác?

\([NiCl_4]^{2-}\) với phối tử trường yếu thường có tách mức nhỏ và hình học tứ diện spin cao. \([Ni(CN)_4]^{2-}\) với phối tử nhận π mạnh tạo trường lớn hơn, thuận lợi cho ghép đôi electron và cấu hình vuông phẳng. Ví dụ này cho thấy hình học, trạng thái spin và liên kết không phải ba phần kiến thức rời; chúng là ba biểu hiện của cùng một cảnh quan năng lượng điện tử.

## Màu sắc — từ khoảng năng lượng tới bước sóng quan sát

Nếu năng lượng photon khớp một chuyển mức điện tử:

\[
\Delta E = h\nu = \frac{hc}{\lambda}
\]

photon có thể bị hấp thụ. Phần ánh sáng còn lại tạo màu quan sát được.

Nếu \(\Delta\) lớn hơn, chuyển mức cần photon năng lượng cao hơn và vùng hấp thụ dịch về bước sóng ngắn hơn.

Tuy nhiên để hiểu cường độ màu còn phải xét các quy tắc chọn; khi cần nền tảng phép đo chi tiết hơn, xem [phổ học](../12_analytical_chemistry/03_spectroscopy.md).

### Quy tắc chọn Laporte

Trong phức bát diện có tâm đối xứng, chuyển d→d thuần túy bị hạn chế theo **quy tắc Laporte (Laporte selection rule)** nên thường yếu. Dao động phân tử hoặc mất đối xứng có thể làm quy tắc được nới lỏng một phần.

Phức tứ diện không có tâm đảo nên dải d–d thường mạnh hơn phức bát diện tương ứng.

### Quy tắc chọn spin

Chuyển mức làm thay đổi tổng bội spin thường yếu. Vì vậy cấu hình electron quyết định không chỉ vị trí năng lượng mà cả cường độ phổ.

## Phổ chuyển điện tích

**Chuyển điện tích phối tử → kim loại (ligand-to-metal charge transfer, LMCT)** xảy ra khi electron được kích thích từ orbital chủ yếu trên phối tử sang orbital chủ yếu trên kim loại. **Chuyển điện tích kim loại → phối tử (metal-to-ligand charge transfer, MLCT)** là chiều ngược lại.

Dải chuyển điện tích thường rất mạnh vì không bị hạn chế theo cách các chuyển d–d bị giới hạn.

Permanganate \(MnO_4^-\) chứa Mn(VII), cấu hình \(d^0\), nên không thể có chuyển d–d thông thường; màu tím mạnh chủ yếu đến từ kích thích chuyển điện tích. Đây là phản ví dụ rất tốt cho câu đơn giản “màu của kim loại chuyển tiếp = chuyển d–d”.

## Từ tính và trạng thái spin

Số electron độc thân quyết định hành vi từ tính định tính.

Ước lượng chỉ xét spin:

\[
\mu = \sqrt{n(n+2)}\,\mu_B
\]

với \(n\) là số electron độc thân.

Nếu mômen từ đo được khác dự đoán, có thể cần xét ghép spin–quỹ đạo, đóng góp mômen quỹ đạo hoặc tương tác phản sắt từ giữa nhiều tâm kim loại.

Đây là một ví dụ quan trọng về **giới hạn mô hình**: công thức chỉ xét spin là điểm bắt đầu, không phải mô tả đầy đủ mọi ion kim loại.

## Biến dạng Jahn–Teller — hệ có thể tự giảm đối xứng để hạ năng lượng

**Định lý Jahn–Teller (Jahn–Teller theorem)** nói rằng một phân tử phi tuyến có trạng thái cơ bản điện tử suy biến thường tự biến dạng để loại bỏ suy biến và hạ tổng năng lượng.

Phức Cu(II) bát diện, \(d^9\), thường kéo dài hai liên kết theo trục. Biến dạng này làm tách thêm các mức orbital từng suy biến và giảm năng lượng điện tử tổng.

Đây là cầu nối sâu giữa suy biến lượng tử và hình học phân tử thực tế.

## Chuyển đổi spin

Một số phức \(d^4\)–\(d^7\) có \(\Delta_o\) và năng lượng ghép đôi gần nhau đến mức nhiệt độ, áp suất hoặc ánh sáng có thể chuyển đổi giữa trạng thái spin cao và spin thấp.

**Vật liệu chuyển spin (spin-crossover materials)** có thể thay đổi màu, từ tính và thể tích theo kích thích ngoài. Đây là cầu nối từ hóa học phối trí tới vật liệu thông minh và thiết bị phân tử.

## Ổn định trường phối tử và động học thế

Mức chiếm electron cũng ảnh hưởng độ trơ động học. Phức Cr(III) bát diện \(d^3\) chẳng hạn có CFSE đáng kể và thường thế phối tử chậm. Tuy nhiên không tồn tại một quy tắc đơn duy nhất CFSE → tốc độ; cơ chế phá liên kết, bản chất phối tử và điện tích cũng rất quan trọng.

Cần giữ hai lớp phân tích riêng:

- trường phối tử giúp hiểu đóng góp điện tử;
- động học cần mô hình trạng thái hoạt hóa và hàng rào phản ứng.

Để xem chi tiết hơn về labile/inert và cơ chế thế, quay lại [hóa học phối trí](./03_coordination_chemistry.md).

## Phức kim loại trong protein

Phối tử protein như N của histidine, S của cysteine, O của carboxylate và N của porphyrin tạo trường phối tử được tinh chỉnh rất chính xác. Fe trong hemoglobin không chỉ là “\(Fe^{2+}\) gắn protein”; mặt phẳng porphyrin, histidine gần tâm và quá trình liên kết \(O_2\) cùng thay đổi trạng thái spin và cấu trúc điện tử.

Sinh học sử dụng điều khiển trường phối tử để thực hiện oxy hóa-khử và liên kết chọn lọc trong nước theo cách ion kim loại tự do khó thực hiện an toàn.

## CFT và LFT khác nhau ở mức trừu tượng

CFT xem tương tác phối tử–kim loại chủ yếu là tĩnh điện và rất hữu ích để suy nhanh sơ đồ tách mức.

LFT dùng ngôn ngữ orbital phân tử, cho phép orbital của phối tử và kim loại trộn với nhau theo đối xứng và năng lượng. Nó giải thích tốt hơn tính cộng hóa trị, liên kết π, dãy phổ hóa học và chuyển điện tích.

CFT không “sai”; nó là mô hình độ phân giải thấp hơn với phạm vi sử dụng rõ ràng.

## Những hiểu lầm thường gặp

### “Orbital d bị tách vật lý thành nhiều mảnh”

Không. Các mức năng lượng suy biến bị tách; orbital vẫn là các trạng thái lượng tử của Hamiltonian điện tử mới.

### “Phối tử trường mạnh luôn tạo liên kết mạnh hơn”

Không. Độ tách trường phối tử và năng lượng phân ly liên kết toàn phần không phải cùng một đại lượng.

### “Mọi màu của kim loại chuyển tiếp đều là chuyển d–d”

Không. Dải chuyển điện tích có thể chiếm ưu thế và tiểu phân \(d^0/d^{10}\) vẫn có thể có màu.

### “Spin thấp nghĩa phân tử ít phản ứng hơn”

Không có quan hệ phổ quát. Khả năng phản ứng phụ thuộc mức chiếm orbital, con đường khả dụng, trạng thái oxy hóa-khử và hàng rào hoạt hóa.

### “CFT và LFT là hai lý thuyết cạnh tranh, phải chọn một”

Không. Chúng có độ chi tiết khác nhau. CFT phù hợp cho trực giác nhanh; LFT cần khi tính cộng hóa trị và tương tác π trở nên quan trọng.

## Mô hình tư duy

> Phối tử tạo một **cảnh quan năng lượng phụ thuộc đối xứng** cho electron d của kim loại. Cách electron chiếm cảnh quan này quyết định spin, phổ và một phần hình học/khả năng phản ứng. CFT cho bản đồ đơn giản; LFT giải thích bản đồ đó xuất hiện từ tương tác orbital như thế nào.

Xem tiếp: [Hóa học trạng thái rắn và khuyết tật](./05_solid_state_and_defect_chemistry.md), nơi các ý tưởng về mức năng lượng, ion kim loại và cấu trúc cục bộ được mở rộng từ một phức riêng lẻ sang mạng tinh thể và vật liệu.