# Chuẩn độ acid–base — đọc đường cong như một bản đồ cân bằng

> **Chuẩn độ (titration / 적정)** dùng một thuốc thử có nồng độ đã biết để đưa hệ đi qua một chuỗi trạng thái acid–base có kiểm soát. Giá trị của chuẩn độ không chỉ nằm ở thể tích tại điểm cuối. Toàn bộ đường cong pH theo thể tích chứa thông tin về hóa lượng, \(pK_a\), khả năng đệm, trạng thái proton hóa và độ mạnh tương đối của acid/base.

Vì vậy một đường chuẩn độ nên được đọc như **bản đồ các cơ chế cân bằng lần lượt trở thành chi phối**.

# Điểm tương đương và điểm kết thúc

**Điểm tương đương (equivalence point / 당량점)** là trạng thái lý thuyết nơi lượng acid và base đã phản ứng đúng theo tỉ lệ hóa lượng.

**Điểm kết thúc (endpoint / 종말점)** là tín hiệu thực nghiệm dùng để xác định gần điểm tương đương, chẳng hạn đổi màu chỉ thị hoặc điểm uốn của đường pH.

Hai điểm không đồng nhất tuyệt đối.

Sai lệch thể tích:

\[
\Delta V=V_{endpoint}-V_{equivalence}
\]

là một nguồn độ chệch. Chỉ thị tốt hoặc thuật toán phát hiện tốt nhằm làm \(\Delta V\) nhỏ so với độ không đảm bảo tổng thể.

# Bốn vùng của chuẩn độ acid yếu bằng base mạnh

Xét acid đơn chức:

\[
HA+OH^-\rightarrow A^-+H_2O
\]

Đường chuẩn độ có thể chia thành bốn vùng khái niệm.

## 1. Trước khi thêm base — cân bằng phân ly của acid yếu

Ban đầu:

\[
HA\rightleftharpoons H^++A^-
\]

và:

\[
K_a=\frac{[H^+][A^-]}{[HA]}
\]

Nếu acid không quá loãng và phân ly nhỏ, có thể dùng gần đúng:

\[
[H^+]\approx\sqrt{K_aC_0}
\]

Nhưng gần đúng này phải được kiểm tra; ở dung dịch rất loãng, tự ion hóa của nước và activity có thể trở nên quan trọng.

## 2. Trước điểm tương đương — vùng đệm

Một phần \(HA\) đã biến thành \(A^-\), nên hệ chứa cặp acid/base liên hợp.

Phương trình Henderson–Hasselbalch:

\[
pH=pK_a+\log\frac{[A^-]}{[HA]}
\]

là một biểu diễn thuận tiện của cân bằng, với điều kiện các giả định về activity và trạng thái hệ đủ phù hợp.

Điều đáng chú ý là pH trong vùng này phụ thuộc mạnh vào **tỉ số** \([A^-]/[HA]\), không chỉ tổng nồng độ.

## 3. Nửa điểm tương đương

Khi lượng base đã thêm bằng một nửa lượng cần tới equivalence point:

\[
n_{A^-}=n_{HA}
\]

nên:

\[
\boxed{pH\approx pK_a}
\]

Đây là một trong những cách trực tiếp nhất để đọc \(pK_a\) từ đường chuẩn độ thực nghiệm.

Tuy nhiên trong hệ hoạt độ không lý tưởng hoặc acid nhiều chức, phép đọc có thể cần hiệu chỉnh.

## 4. Tại điểm tương đương — base liên hợp thủy phân

Tại equivalence point, hầu hết \(HA\) đã chuyển thành \(A^-\).

\[
A^-+H_2O\rightleftharpoons HA+OH^-
\]

với:

\[
K_b=\frac{K_w}{K_a}
\]

Do đó pH thường >7 cho acid yếu chuẩn độ bằng base mạnh.

Điểm này cho thấy một nguyên tắc quan trọng: **pH tại equivalence point do sản phẩm hóa lượng tiếp tục cân bằng với nước quyết định**.

## 5. Sau điểm tương đương — titrant dư chi phối

Sau equivalence point, lượng \(OH^-\) dư thường lớn hơn đóng góp thủy phân của \(A^-\), nên pH được tính chủ yếu từ base mạnh dư sau khi xét thể tích tổng.

# Acid mạnh – base mạnh

Với:

\[
H^++OH^-\rightarrow H_2O
\]

trước equivalence point, pH do \(H^+\) dư; sau đó do \(OH^-\) dư.

Tại 25 °C trong dung dịch lý tưởng đủ loãng, pH gần 7 ở equivalence point.

Nhưng ngay cả trong hệ này, “pH = 7” không phải chân lý độc lập nhiệt độ vì:

\[
K_w=K_w(T)
\]

và pH trung tính thay đổi theo nhiệt độ.

# Base yếu – acid mạnh

Logic đối xứng với acid yếu.

Trước equivalence point xuất hiện vùng đệm \(B/BH^+\); tại nửa tương đương:

\[
pOH\approx pK_b
\]

hoặc có thể biểu diễn qua \(pK_a\) của \(BH^+\).

Tại equivalence point, acid liên hợp \(BH^+\) thủy phân làm pH <7 trong điều kiện thông thường.

# Độ dốc quanh điểm tương đương quyết định khả năng định vị endpoint

Không phải mọi chuẩn độ đều có một bước nhảy pH sắc nét.

Độ dốc giảm khi:

- acid/base quá yếu;
- dung dịch quá loãng;
- \(pK_a\) gần vùng pH nơi nước tự ion hóa chi phối;
- hai bước proton hóa chồng lấp;
- activity và nền mẫu phức tạp.

Nếu đường cong quá phẳng, việc chọn chỉ thị màu chính xác trở nên khó, dù buret có độ phân giải rất tốt.

Đây là ví dụ cho thấy **giới hạn hóa học có thể quan trọng hơn giới hạn dụng cụ**.

# Chất chỉ thị acid–base

Một chỉ thị thường là acid yếu:

\[
HIn\rightleftharpoons H^++In^-
\]

Hai dạng có màu khác nhau.

Tỉ số:

\[
\frac{[In^-]}{[HIn]}=10^{pH-pK_a^{indicator}}
\]

thay đổi khoảng 100 lần khi pH đi qua vùng \(pK_a\pm1\). Đây là lý do vùng chuyển màu thường trải trên khoảng vài đơn vị pH quanh \(pK_a\) của chỉ thị.

Chỉ thị nên được chọn sao cho vùng chuyển nằm trong phần dốc của đường chuẩn độ.

# Vì sao phenolphthalein và methyl orange phù hợp cho các hệ khác nhau?

Phenolphthalein đổi màu trong vùng base nhẹ, nên thường phù hợp hơn với acid yếu–base mạnh.

Methyl orange chuyển ở pH acid hơn, có thể phù hợp với acid mạnh–base yếu.

Không nên học thuộc tên chỉ thị tách khỏi đường cong; hãy **đặt vùng chuyển của chỉ thị lên đồ thị pH–V** và xem nó có nằm trong vùng nhảy không.

# Acid đa proton

Với acid hai proton:

\[
H_2A\rightleftharpoons H^++HA^-
\]

\[
HA^-\rightleftharpoons H^++A^{2-}
\]

có hai hằng số \(K_{a1}\), \(K_{a2}\).

Nếu hai \(pK_a\) cách nhau đủ xa, đường chuẩn độ có thể xuất hiện hai vùng đệm và hai equivalence point.

Nếu chúng quá gần, các bước chồng lấp và không thể tách rõ bằng đường pH đơn giản.

Do đó số proton “có thể nhường” về công thức không tự động bằng số endpoint có thể quan sát.

# Điểm tương đương giữa hai bước và loài amphiprotic

Ở equivalence point đầu của một acid hai proton, dung dịch có thể chủ yếu chứa loài \(HA^-\), vừa có khả năng nhận vừa nhường proton.

Trong điều kiện lý tưởng phù hợp:

\[
pH\approx\frac{1}{2}(pK_{a1}+pK_{a2})
\]

Đây là kết quả từ tính amphiprotic của loài trung gian, không phải công thức cần học thuộc độc lập.

# Buffer capacity trên đường chuẩn độ

Vùng gần \(pH=pK_a\) không chỉ có \([HA]=[A^-]\); nó còn là vùng hệ chống biến đổi pH tương đối hiệu quả.

**Khả năng đệm (buffer capacity)** phụ thuộc tổng nồng độ acid + base liên hợp. Hai buffer cùng tỉ số \([A^-]/[HA]\) có cùng pH nhưng buffer đậm đặc hơn chống thêm acid/base tốt hơn.

Trên đường chuẩn độ, điều này biểu hiện bằng độ dốc nhỏ hơn trong vùng đệm.

# Chuẩn độ điện thế — dùng toàn bộ đường cong thay vì một màu

Điện cực pH cho phép ghi liên tục:

\[
pH=f(V_{titrant})
\]

Equivalence point có thể được ước lượng từ:

- điểm uốn của đường cong;
- cực đại \(dpH/dV\);
- thay đổi dấu đạo hàm bậc hai;
- fit một mô hình cân bằng.

Dùng toàn bộ đường cong có lợi khi mẫu màu, đục hoặc khi endpoint quang khó quan sát.

# Đạo hàm giúp thấy endpoint nhưng cũng khuếch đại nhiễu

Tính đạo hàm số từ dữ liệu làm nhiễu đo tăng rõ.

Do đó cần:

- bước thể tích nhỏ hợp lý quanh endpoint;
- điện cực ổn định trước khi ghi;
- tránh làm trơn dữ liệu quá mức làm dịch endpoint.

Đây là một ví dụ của đánh đổi giữa độ phân giải và nhiễu trong xử lý dữ liệu.

# Chuẩn độ ngược acid–base

Nếu analyte rắn phản ứng chậm với acid, có thể thêm dư một lượng acid biết trước, để phản ứng hoàn toàn rồi chuẩn độ acid dư bằng base.

Ví dụ carbonat rắn:

\[
CO_3^{2-}+2H^+\rightarrow CO_2+H_2O
\]

Sau khi biết lượng \(H^+\) còn dư, lấy lượng ban đầu trừ đi sẽ cho lượng đã phản ứng với carbonate.

# Ảnh hưởng của CO₂ trong chuẩn độ base

NaOH hấp thụ CO₂:

\[
2OH^-+CO_2\rightarrow CO_3^{2-}+H_2O
\]

Điều này làm nồng độ base mạnh thay đổi và tạo carbonate, ảnh hưởng đường chuẩn độ.

Vì vậy NaOH chính xác thường cần:

- bảo quản hạn chế CO₂;
- chuẩn hóa định kỳ;
- dùng nước và thao tác phù hợp.

# Hoạt độ và lực ion

Các công thức pH dựa trên nồng độ là gần đúng cho dung dịch loãng.

Về nguyên tắc:

\[
pH=-\log a_{H^+}
\]

Trong nền điện ly mạnh hoặc mẫu có lực ion cao, hệ số hoạt độ thay đổi và đường chuẩn độ có thể lệch khỏi dự đoán nồng độ lý tưởng.

Đây là lý do chuẩn độ trong nước biển, dung dịch công nghiệp hoặc nền muối cao cần thận trọng hơn hệ textbook loãng.

# Nhiệt độ

Nhiệt độ ảnh hưởng:

- \(K_w\);
- \(K_a\), \(K_b\);
- đáp ứng điện cực;
- thể tích dung dịch;
- tốc độ cân bằng.

Vì vậy pH và endpoint không hoàn toàn độc lập nhiệt độ.

# Từ đường cong sang suy luận hóa học

Một đường chuẩn độ tốt có thể cho:

- nồng độ analyte từ equivalence volume;
- \(pK_a\) từ half-equivalence;
- số bước proton hóa có thể phân giải;
- dấu hiệu acid/base mạnh hoặc yếu;
- khả năng đệm theo độ dốc;
- dấu hiệu phản ứng phụ nếu đường cong khác mô hình.

Đây là lý do chuẩn độ vừa là phương pháp định lượng vừa là thí nghiệm cân bằng.

# Những hiểu lầm thường gặp

### “Điểm tương đương luôn pH = 7”

Không. Chỉ gần đúng cho một số hệ acid mạnh–base mạnh ở điều kiện thích hợp.

### “Chất chỉ thị đổi màu đúng tại equivalence point”

Không. Chỉ thị có vùng chuyển; endpoint được thiết kế để gần equivalence point.

### “Half-equivalence luôn áp dụng cho mọi acid đa chức giống nhau”

Không. Các bước có thể chồng lấp và activity có thể làm mô hình đơn giản sai lệch.

### “Đường chuẩn độ chỉ dùng để tìm thể tích cuối”

Không. Hình dạng toàn đường chứa thông tin cân bằng và buffer.

### “pH meter loại bỏ mọi sai số endpoint”

Không. Điện cực có drift, thời gian đáp ứng, calibration và junction potential.

# Mô hình tư duy

Một phép chuẩn độ acid–base là **quá trình chủ động di chuyển hệ qua không gian thành phần**. Ở mỗi thể tích titrant, thành phần mới quyết định cân bằng proton hóa và pH. Equivalence point là mốc bảo toàn vật chất; đường cong xung quanh nó là dấu vết của nhiệt động acid–base.

Xem tiếp: [Cân bằng độ tan](./05_solubility_equilibria.md) và [Phân tích thể tích](../12_analytical_chemistry/01_volumetric_analysis.md).