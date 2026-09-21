# Cơ chế phản ứng — từ phương trình tổng tới con đường vi mô

> **Cơ chế phản ứng (reaction mechanism / 반응 메커니즘)** là mô hình mô tả chuỗi các bước vi mô biến chất phản ứng thành sản phẩm. Phương trình hóa học tổng chỉ là hạch toán đầu vào–đầu ra; cơ chế cố gắng giải thích **liên kết nào thay đổi trước, chất trung gian nào xuất hiện, trạng thái chuyển tiếp nào phải vượt qua và bước nào kiểm soát tốc độ trong từng điều kiện**.

Hai phản ứng có cùng phương trình tổng có thể đi qua cơ chế hoàn toàn khác nhau và vì thế có tốc độ, độ chọn lọc và đáp ứng với xúc tác khác nhau. Do đó cơ chế không thể suy ra chỉ từ việc cân bằng phương trình.

# Bước cơ bản và phản ứng tổng

Một **bước cơ bản (elementary step / 단일 단계 반응)** là một sự kiện vi mô duy nhất trong mô hình cơ chế.

Ví dụ:

\[
A+B\rightarrow I
\]

nếu thực sự là một bước cơ bản lưỡng phân tử, định luật tác dụng khối lượng cho:

\[
r=k[A][B]
\]

Nhưng nếu cùng phương trình \(A+B\to I\) chỉ là viết tắt cho ba bước bên trong, không được tự động dùng hệ số stoichiometric làm reaction order.

## Molecularity khác reaction order

**Số phân tử tham gia bước cơ bản (molecularity)** là số tiểu phần cùng tham gia một elementary event. Nó chỉ có ý nghĩa cho bước cơ bản và thường là một hoặc hai; ba hạt cùng gặp đúng cấu hình ít phổ biến hơn nhiều.

**Bậc phản ứng (reaction order)** là số mũ thực nghiệm trong rate law và có thể bằng 0, phân số hoặc âm.

Hai khái niệm chỉ trùng trong trường hợp đơn giản của elementary step tuân mass action.

# Chất trung gian và chất xúc tác

**Chất trung gian (intermediate / 반응 중간체)** được tạo ở một bước rồi tiêu thụ ở bước khác, nên không xuất hiện trong phương trình tổng.

**Chất xúc tác (catalyst)** tham gia cơ chế nhưng được tái sinh sau một chu trình tổng.

Ví dụ:

\[
A+Catalyst\rightarrow I
\]

\[
I+B\rightarrow P+Catalyst
\]

Catalyst bị tiêu thụ ở bước đầu nhưng xuất hiện lại ở bước sau. Intermediate I thì được tạo rồi mất.

Sự phân biệt này giúp kiểm tra một cơ chế có được cộng đúng hay không.

# Cộng các bước để kiểm tra bảo toàn

Một cơ chế hợp lệ tối thiểu phải cộng lại thành phương trình tổng sau khi triệt tiêu intermediate và catalyst.

Ví dụ:

\[
NO_2+NO_2\rightarrow NO_3+NO
\]

\[
NO_3+CO\rightarrow NO_2+CO_2
\]

Cộng và triệt tiêu \(NO_3\) cùng một \(NO_2\):

\[
NO_2+CO\rightarrow NO+CO_2
\]

Nếu cơ chế không thể tái tạo stoichiometry tổng, nó sai ngay từ mức bảo toàn vật chất.

# “Bước chậm nhất quyết định tốc độ” — hữu ích nhưng không đủ

Trong mô hình đơn giản, nếu một bước chậm hơn hẳn các bước còn lại, tốc độ toàn quá trình có thể gần tốc độ của bước đó.

Tuy nhiên một mạng thật có thể có:

- bước thuận nghịch nhanh trước bước tạo sản phẩm;
- nhiều hàng rào gần tương đương;
- intermediate tích lũy;
- nhiều nhánh sản phẩm;
- catalyst resting state;
- thay đổi rate control theo nồng độ hoặc nhiệt độ.

Vì thế câu “rate-determining step” là một approximation. Trong cơ chế phức tạp, **mức kiểm soát tốc độ (degree of rate control)** được phân bố trên nhiều bước và có thể thay đổi theo điều kiện.

# Xấp xỉ tiền cân bằng

Giả sử:

\[
A+B\rightleftharpoons I\qquad fast
\]

\[
I\rightarrow P\qquad slower
\]

Nếu bước đầu gần cân bằng:

\[
K=\frac{[I]}{[A][B]}
\]

nên:

\[
[I]=K[A][B]
\]

Tốc độ tạo P:

\[
r=k_2[I]=k_2K[A][B]
\]

Rate law quan sát được chứa A và B dù bước tạo sản phẩm trực tiếp chỉ chứa I.

Đây là ví dụ cho cách một intermediate vô hình được loại bằng quan hệ nhiệt động.

# Xấp xỉ trạng thái ổn định

Nếu intermediate được tạo và tiêu thụ liên tục nhưng không tích lũy đáng kể:

\[
\frac{d[I]}{dt}\approx0
\]

Giả sử:

\[
A\xrightarrow{k_1}I
\]

\[
I\xrightarrow{k_2}P
\]

\[
I\xrightarrow{k_3}Q
\]

thì:

\[
\frac{d[I]}{dt}=k_1[A]-(k_2+k_3)[I]\approx0
\]

suy ra:

\[
[I]\approx\frac{k_1[A]}{k_2+k_3}
\]

Từ đó có thể suy tốc độ tạo P và Q.

**Xấp xỉ trạng thái ổn định (steady-state approximation)** là công cụ nền trong kinetics enzyme, atmospheric chemistry, combustion và catalytic networks.

# Cân bằng và trạng thái ổn định không giống nhau

Ở **cân bằng (equilibrium)**, các reaction flux thuận và nghịch cân bằng sao cho không có động lực Gibbs ròng.

Ở **trạng thái ổn định (steady state)**, concentration có thể không đổi nhưng vẫn có dòng vật chất liên tục qua hệ:

```text
input → intermediate → product → output
```

Tế bào sống và reactor liên tục thường ở steady state rất xa equilibrium. Nhầm hai khái niệm này làm sai cách hiểu cả sinh hóa và engineering.

# Trạng thái chuyển tiếp không phải intermediate

**Trạng thái chuyển tiếp (transition state / 전이 상태)** là vùng cực đại năng lượng tự do dọc một tọa độ phản ứng. Nó không phải một loài bền có thể chứa trong bình.

Intermediate tương ứng với một cực tiểu cục bộ trên bề mặt năng lượng và đôi khi có thể quan sát hoặc bẫy được.

Một sơ đồ đơn giản:

```text
reactant
   ↑ TS1
   ↓
intermediate
   ↑ TS2
   ↓
product
```

Mỗi elementary step có một transition-state region riêng.

# Tọa độ phản ứng chỉ là lát cắt đơn giản hóa

Biểu đồ một chiều “năng lượng theo reaction coordinate” hữu ích để học, nhưng phân tử thật có nhiều bậc tự do. Bề mặt năng lượng tiềm năng hoặc **bề mặt năng lượng tự do (free-energy surface)** là không gian nhiều chiều.

Một reaction coordinate tốt phải nén những chuyển động quan trọng — kéo giãn liên kết, chuyển proton, thay đổi góc, solvation — thành một biến có ý nghĩa.

Trong simulation, chọn sai reaction coordinate có thể che mất barrier thật hoặc tạo barrier giả.

# Nguyên lý thuận nghịch vi mô

**Thuận nghịch vi mô (microscopic reversibility)** nói rằng ở equilibrium, đường vi mô thuận và nghịch phải tương thích với nhau.

Nếu một cơ chế thuận đi qua các intermediate cụ thể, cơ chế nghịch không thể tùy ý dùng một chuỗi hoàn toàn không tương thích mà vẫn tuyên bố cùng equilibrium elementary process.

Điều này tạo liên kết giữa kinetics và thermodynamics, và đặt constraint lên ratio của forward/reverse rate constants.

# Detailed balance

Trong một mạng ở equilibrium, với các điều kiện thích hợp, từng cặp elementary flux thuận–nghịch có thể cân bằng:

\[
r_i^+=r_i^-
\]

Khái niệm **cân bằng chi tiết (detailed balance)** mạnh hơn chỉ nói tổng concentration không đổi. Nó giúp kiểm tra thermodynamic consistency của kinetic models.

Một model số vi phạm detailed balance có thể dự đoán “máy chuyển động vĩnh cửu” hóa học dù từng rate law riêng trông hợp lý.

# Reaction intermediate có thể được phát hiện như thế nào?

Intermediate thường có lifetime ngắn, vì vậy việc phát hiện phụ thuộc thang thời gian.

Các chiến lược gồm:

- spectroscopy nhanh;
- cryogenic trapping;
- spin trapping cho radicals;
- isotope labeling;
- mass spectrometry;
- rapid quench;
- product stereochemistry;
- kinetic isotope effects.

Không quan sát được intermediate không chứng minh nó không tồn tại; lifetime có thể nằm ngoài cửa sổ của phương pháp đo.

# Đánh dấu đồng vị — theo dõi nguyên tử đi đâu

Thay một nguyên tử bằng isotope bền như \(^{13}C\), \(^{18}O\) hoặc deuterium cho phép theo dõi đường đi của nguyên tử qua phản ứng.

Nếu oxygen trong sản phẩm đến từ nước thay vì molecular oxygen, isotope labeling có thể phân biệt hai cơ chế dù sản phẩm cuối giống nhau.

Đây là ví dụ cho việc cơ chế cần bằng chứng “bên trong” chứ không chỉ yield cuối.

# Hiệu ứng đồng vị động học

Thay H bằng D làm thay đổi tần số dao động và zero-point energy của liên kết. Nếu phá hoặc hình thành liên kết X–H có vai trò đáng kể trong transition state, tốc độ có thể thay đổi.

**Hiệu ứng đồng vị động học (kinetic isotope effect, KIE)**:

\[
KIE=\frac{k_H}{k_D}
\]

là một probe cơ chế quan trọng.

Tuy nhiên KIE lớn không tự động chứng minh một cơ chế duy nhất; cần kết hợp với evidence khác và hiểu equilibrium isotope effects.

# Hammett và quan hệ năng lượng tự do tuyến tính

Trong organic chemistry, thay substituent trên một series cấu trúc có thể thay tốc độ có hệ thống. Quan hệ Hammett đơn giản:

\[
\log\frac{k}{k_0}=\rho\sigma
\]

liên hệ ảnh hưởng điện tử của substituent với sensitivity của reaction center.

Nếu một tập dữ liệu đổi slope hoặc không còn tuyến tính, đó có thể là dấu hiệu mechanism hoặc transition-state character thay đổi.

Đây là ví dụ cho cách kinetics dùng series thực nghiệm để suy electronic structure của transition state.

# Curtin–Hammett — population nhỏ vẫn có thể cho sản phẩm chính

Nếu hai conformer interconvert nhanh hơn phản ứng tạo sản phẩm:

\[
A\rightleftharpoons B
\]

và mỗi conformer đi tới sản phẩm khác, tỉ lệ sản phẩm không chỉ phụ thuộc population của A/B mà phụ thuộc **năng lượng tự do của các transition states tính từ equilibrium ensemble**.

Một conformer ít tồn tại vẫn có thể tạo sản phẩm chính nếu barrier từ nó thấp hơn đủ nhiều.

Khái niệm này rất quan trọng trong stereoselective organic chemistry và catalysis.

# Phản ứng song song và độ chọn lọc

Nếu:

\[
A\xrightarrow{k_1}P_1
\]

\[
A\xrightarrow{k_2}P_2
\]

với cơ chế đơn giản cùng bậc, selectivity tức thời gần phụ thuộc:

\[
\frac{r_1}{r_2}=\frac{k_1}{k_2}
\]

Nhiệt độ có thể làm ratio thay đổi nếu hai pathways có activation parameters khác nhau.

Đây là lý do tối ưu nhiệt độ không chỉ nhằm “phản ứng nhanh hơn” mà còn để kiểm soát sản phẩm.

# Phản ứng nối tiếp

Với:

\[
A\xrightarrow{k_1}I\xrightarrow{k_2}P
\]

intermediate I thường tăng rồi giảm theo thời gian. Nếu mục tiêu là thu I, thời điểm dừng phản ứng trở thành biến thiết kế quan trọng.

Trong manufacturing, residence time có thể quyết định selectivity nhiều không kém catalyst identity.

# Chain reactions và radicals

Một phản ứng chuỗi thường gồm:

```text
khơi mào
→ truyền chuỗi
→ phân nhánh chuỗi nếu có
→ kết thúc
```

Trong combustion, một radical có thể tạo nhiều radical mới, dẫn tới chain branching và tốc độ tăng cực nhanh.

Trong polymerization, radical propagation kéo dài chain, còn termination kiểm soát molecular-weight distribution.

Do đó “một phản ứng” có thể là một population động của reactive intermediates chứ không phải một sự kiện đơn.

# Cơ chế và mô phỏng mạng phản ứng

Với nhiều species:

\[
\frac{d\mathbf C}{dt}=S\mathbf r(\mathbf C)
\]

Mỗi column của \(S\) mô tả stoichiometry của một elementary reaction; vector \(\mathbf r\) chứa rate laws.

Solver số cho phép dự đoán concentration theo thời gian. Nhưng simulation chỉ đáng tin nếu:

- species set hợp lý;
- rate constants có evidence;
- thermodynamic reversibility được tôn trọng;
- transport không bị bỏ qua khi nó chi phối.

Mô hình lớn không tự động là mô hình đúng.

# Phân tích độ nhạy

Nếu model có hàng trăm reactions, không phải tất cả đều quan trọng như nhau trong mọi điều kiện.

**Phân tích độ nhạy (sensitivity analysis)** hỏi output thay đổi bao nhiêu khi một \(k_i\) thay đổi:

\[
S_i=\frac{\partial y}{\partial k_i}
\]

Điều này giúp tìm reaction pathways chi phối và ưu tiên rate constant nào cần đo chính xác hơn.

# Identifiability — cùng dữ liệu có thể hỗ trợ nhiều cơ chế

Một rate law khớp dữ liệu không chứng minh cơ chế là duy nhất.

Hai networks khác nhau có thể tạo concentration curves gần giống nhau trong một tập điều kiện. Đây là vấn đề **khả năng nhận dạng cơ chế (mechanism identifiability)**.

Muốn phân biệt, cần thiết kế thí nghiệm nơi hai cơ chế dự đoán khác nhau: thay isotope, temperature, pressure, concentration range hoặc đo intermediate trực tiếp.

Đây là tư duy mạnh hơn việc “fit một đường rồi chọn mechanism”.

# Cơ chế không nên chi tiết hơn bằng chứng

Nếu dữ liệu chỉ hỗ trợ một rate law hiệu dụng, việc vẽ mười intermediate đẹp mắt không làm cơ chế đáng tin hơn.

Một cơ chế khoa học tốt phải phân biệt rõ:

```text
điều đã đo
→ điều được suy ra
→ giả thuyết cơ chế
→ dự đoán có thể kiểm tra tiếp
```

Đây là nguyên tắc chung của modeling trong khoa học.

# Những hiểu lầm thường gặp

### “Intermediate là transition state”

Không. Intermediate là minimum tương đối; transition state là barrier region giữa các minima.

### “Bước chậm nhất luôn quyết định tốc độ”

Đây chỉ là approximation. Rate control có thể phân bố và thay đổi theo điều kiện.

### “Mechanism cộng đúng phương trình tổng thì mechanism đúng”

Đó chỉ là điều kiện cần. Cơ chế còn phải phù hợp rate law và evidence độc lập.

### “Khớp rate law chứng minh mechanism duy nhất”

Không. Nhiều mechanisms có thể tạo cùng rate law hiệu dụng.

### “Không nhìn thấy intermediate nghĩa nó không tồn tại”

Không. Detection phụ thuộc lifetime, concentration và time resolution.

## Mô hình tư duy

Phương trình tổng giống **API contract** nói hệ nhận gì và trả gì. Cơ chế giống **implementation bên trong** gồm nhiều trạng thái, nhánh và vòng lặp. Kinetics, isotope labeling, spectroscopy và computation là những cách quan sát implementation gián tiếp.

Một cơ chế tốt không chỉ giải thích dữ liệu cũ mà phải tạo ra **dự đoán mới có thể bị kiểm chứng**.

Xem tiếp: [Năng lượng hoạt hóa và Arrhenius](./03_activation_energy_and_arrhenius.md), [Xúc tác](./04_catalysis.md) và [Mạng phản ứng](../04_chemical_quantities/06_stoichiometric_matrices_and_reaction_networks.md).