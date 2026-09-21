# Hằng số cân bằng — định lượng vị trí cân bằng và nối với thế hóa học

> **Hằng số cân bằng (equilibrium constant, \(K\) / 평형 상수)** định lượng tỉ lệ hoạt độ của sản phẩm và chất phản ứng tại cân bằng cho một phương trình phản ứng được viết theo một dạng stoichiometric cụ thể và tại một nhiệt độ xác định.

Điểm quan trọng là `K` không phải một “con số ma thuật của phản ứng”. Nó là kết quả của chênh lệch **thế hóa học chuẩn** giữa hai phía, và nó chỉ có ý nghĩa khi phương trình phản ứng, trạng thái chuẩn và nhiệt độ đã được xác định rõ.

## Từ thế hóa học tới K

Với phản ứng:

\[
aA+bB\rightleftharpoons cC+dD
\]

**thương số phản ứng (reaction quotient, \(Q\))** được định nghĩa bằng hoạt độ:

\[
Q=\frac{a_C^ca_D^d}{a_A^aa_B^b}
\]

Biến thiên năng lượng tự do của phản ứng tại trạng thái bất kỳ là:

\[
\Delta_rG=\Delta_rG^\circ+RT\ln Q
\]

Tại cân bằng:

\[
\Delta_rG=0
\]

nên:

\[
\Delta_rG^\circ=-RT\ln K
\]

và:

\[
Q=K
\]

Vì vậy `K` mã hóa chênh lệch năng lượng tự do chuẩn theo dạng hàm mũ.

Nếu \(\Delta_rG^\circ\) thay đổi chỉ vài kJ/mol, `K` có thể thay đổi nhiều lần vì hàm mũ rất nhạy.

## Vì sao hoạt độ quan trọng hơn nồng độ?

Nồng độ cho biết có bao nhiêu species trong một thể tích. Nhưng trong dung dịch thật, các species tương tác với nhau nên “khả năng phản ứng hiệu dụng” không còn tỉ lệ hoàn hảo với nồng độ.

Hoạt độ được viết:

\[
a_i=\gamma_i\frac{c_i}{c^\circ}
\]

Trong đó \(\gamma_i\) là **hệ số hoạt độ (activity coefficient)**.

Khi dung dịch rất loãng và gần lý tưởng:

\[
\gamma_i\approx1
\]

nên:

\[
a_i\approx\frac{c_i}{c^\circ}
\]

Nhưng ở lực ion đáng kể, đặc biệt với ion đa điện tích, \(\gamma_i\) có thể lệch đáng kể khỏi 1.

Do đó một “hằng số cân bằng theo nồng độ” có thể thay đổi theo nền điện ly, trong khi hằng số nhiệt động xây từ hoạt độ vẫn giữ ý nghĩa nhất quán hơn.

## Hoạt độ của khí và pha tinh khiết

Với khí lý tưởng:

\[
a_i\approx\frac{P_i}{P^\circ}
\]

Với chất rắn tinh khiết hoặc chất lỏng tinh khiết trong pha riêng:

\[
a\approx1
\]

nên chúng không xuất hiện tường minh trong các biểu thức cân bằng đơn giản hóa.

Ví dụ:

\[
CaCO_3(s)\rightleftharpoons CaO(s)+CO_2(g)
\]

\[
K\approx\frac{P_{CO_2}}{P^\circ}
\]

Lượng chất rắn có thể thay đổi mà `K` không đổi miễn là các pha tinh khiết tương ứng vẫn còn hiện diện.

## Độ lớn của K

Nếu:

\[
K\gg1
\]

cân bằng nghiêng về sản phẩm khi so theo trạng thái chuẩn.

Nếu:

\[
K\ll1
\]

cân bằng nghiêng về chất phản ứng.

Nhưng “nghiêng về” không có nghĩa chỉ một phía tồn tại.

Ví dụ nếu:

\[
K=10^6
\]

vẫn có thể còn chất phản ứng đo được, đặc biệt nếu nồng độ ban đầu rất lớn hoặc stoichiometry phức tạp.

## K phụ thuộc cách viết phương trình

Nếu đảo chiều phản ứng:

\[
K_{reverse}=\frac1{K_{forward}}
\]

Nếu nhân toàn bộ phương trình với hệ số \(n\):

\[
K_{new}=K^n
\]

Nếu cộng hai phản ứng:

\[
R_1+R_2=R_3
\]

thì:

\[
K_3=K_1K_2
\]

Điều này tương ứng với việc các \(\Delta G^\circ\) được cộng:

\[
\Delta G_3^\circ=\Delta G_1^\circ+\Delta G_2^\circ
\]

vì logarithm biến phép nhân thành phép cộng.

## Kc và Kp

Giáo trình thường dùng:

- `K_c` dựa trên nồng độ mol;
- `K_p` dựa trên áp suất riêng phần.

Với khí lý tưởng:

\[
K_p=K_c(RT)^{\Delta n_{gas}}
\]

khi các quy ước đơn vị và trạng thái chuẩn được xử lý nhất quán.

Trong nhiệt động lực học chặt chẽ, `K` được xây từ hoạt độ nên là đại lượng không thứ nguyên.

Các đơn vị đôi khi xuất hiện trong biểu thức giáo trình thực chất là dấu hiệu người ta đang dùng nồng độ/áp suất trực tiếp thay cho hoạt độ đã chuẩn hóa.

## Sự phụ thuộc vào nhiệt độ

`K` phụ thuộc nhiệt độ vì:

\[
\Delta G^\circ=\Delta H^\circ-T\Delta S^\circ
\]

**Quan hệ van 't Hoff (van 't Hoff relation)**:

\[
\frac{d\ln K}{dT}=\frac{\Delta H^\circ}{RT^2}
\]

Nếu \(\Delta H^\circ>0\), tăng nhiệt độ thường làm `K` tăng.

Nếu \(\Delta H^\circ<0\), tăng nhiệt độ thường làm `K` giảm.

Đây là mô tả định lượng sâu hơn quy tắc nhiệt độ của Le Châtelier.

## Dạng tích phân của van 't Hoff

Nếu \(\Delta H^\circ\) gần như không đổi trong khoảng nhiệt độ đang xét:

\[
\ln\frac{K_2}{K_1}
= -\frac{\Delta H^\circ}{R}
\left(\frac1{T_2}-\frac1{T_1}\right)
\]

Phương trình này cho phép ước lượng `K` ở nhiệt độ mới từ `K` đã biết và enthalpy phản ứng.

Nhưng nếu khoảng nhiệt độ lớn, \(\Delta H^\circ\) cũng thay đổi do nhiệt dung nên cần mô hình đầy đủ hơn.

## K không phụ thuộc nồng độ ban đầu

Ở cùng nhiệt độ và cùng trạng thái chuẩn, cùng phản ứng có cùng hằng số cân bằng nhiệt động.

Thành phần ban đầu chỉ quyết định hệ cần tiến xa bao nhiêu để đạt:

\[
Q=K
\]

Đây là lý do hai bình có thành phần ban đầu khác nhau có thể đạt các thành phần cân bằng khác nhau về số mol tuyệt đối nhưng vẫn thỏa cùng một quan hệ `Q = K`.

## Chất xúc tác không làm đổi K

Catalyst thay đổi các hàng rào động học nhưng không thay đổi trạng thái đầu/cuối của phản ứng tổng.

Vì vậy catalyst làm hệ đạt cân bằng nhanh hơn nhưng không làm dịch vị trí cân bằng.

Nếu một catalyst dường như làm thay đổi thành phần cuối cùng, cần kiểm tra xem:

- hệ chưa thực sự cân bằng trước đó;
- có phản ứng phụ mới;
- catalyst thay đổi pha hoặc species tồn tại;
- điều kiện nhiệt độ/áp suất đã khác.

## Nhiều cân bằng cùng tồn tại

Trong hệ thật, hiếm khi chỉ có một cân bằng duy nhất.

Ví dụ một ion kim loại có thể đồng thời:

```text
proton hóa/deproton hóa ligand
+ tạo phức
+ thủy phân
+ kết tủa
+ oxy hóa-khử
```

Mỗi cân bằng có `K` riêng, nhưng chúng chia sẻ cùng species nên bị **ghép với nhau (coupled equilibria)**.

Đây là lý do một thay đổi pH có thể làm độ tan, màu, thế redox và khả năng tạo phức thay đổi cùng lúc.

## Ví dụ cân bằng ghép: độ tan carbonate trong acid

Xét:

\[
CaCO_3(s)\rightleftharpoons Ca^{2+}+CO_3^{2-}
\]

Nếu acid proton hóa carbonate:

\[
CO_3^{2-}+H^+\rightleftharpoons HCO_3^-
\]

và tiếp tục:

\[
HCO_3^-+H^+\rightleftharpoons CO_2+H_2O
\]

thì \(CO_3^{2-}\) tự do bị giảm.

Theo Le Châtelier hoặc trực tiếp qua `Q`, cân bằng hòa tan bị kéo sang phải.

Vì vậy acid làm `CaCO3` tan mạnh hơn dù `Ksp` riêng của phản ứng hòa tan không thay đổi.

## Hằng số cân bằng tổng từ các bước riêng

Nếu:

\[
A\rightleftharpoons B\qquad K_1
\]

và:

\[
B\rightleftharpoons C\qquad K_2
\]

thì phản ứng tổng:

\[
A\rightleftharpoons C
\]

có:

\[
K_{overall}=K_1K_2
\]

Nếu một bước có `K` rất lớn, nó có thể kéo mạnh cân bằng tổng theo một hướng.

Đây là nền tảng cho:

- hòa tan do tạo phức;
- kết tủa chọn lọc;
- proton transfer;
- chelation;
- phản ứng redox ghép.

## Hằng số điều kiện

Trong nhiều hệ, người ta gom một số cân bằng phụ vào **hằng số điều kiện (conditional equilibrium constant)**.

Ví dụ EDTA tạo phức với kim loại:

\[
M+Y^{4-}\rightleftharpoons MY
\]

Nhưng ở một pH cho trước, chỉ một phần tổng EDTA tồn tại dưới dạng `Y4−`.

Nếu:

\[
\alpha_{Y^{4-}}=\frac{[Y^{4-}]}{[Y]_{total}}
\]

thì có thể định nghĩa:

\[
K_f'=\alpha_{Y^{4-}}K_f
\]

`K_f'` cho biết độ mạnh hiệu dụng của tạo phức tại pH đó.

Đây là công cụ rất hữu ích trong hóa phân tích và hóa phối trí.

## Phân bố species và phân số alpha

Với acid đơn proton:

\[
HA\rightleftharpoons H^++A^-
\]

phân số dạng proton hóa:

\[
\alpha_{HA}=\frac{[H^+]}{[H^+]+K_a}
\]

và phân số dạng mất proton:

\[
\alpha_{A^-}=\frac{K_a}{[H^+]+K_a}
\]

Tổng:

\[
\alpha_{HA}+\alpha_{A^-}=1
\]

Với hệ đa proton, các biểu thức dài hơn nhưng nguyên tắc giống nhau.

**Biểu đồ phân bố species (speciation diagram)** chính là cách trực quan hóa các phân số này theo pH hoặc biến môi trường khác.

## Cân bằng vật chất và cân bằng điện tích

Để giải hệ nhiều cân bằng một cách tổng quát, cần kết hợp:

1. các phương trình hằng số cân bằng;
2. **cân bằng vật chất (mass balance)**;
3. **cân bằng điện tích (charge balance)**.

Ví dụ với acid tổng nồng độ \(C_T\):

\[
C_T=[HA]+[A^-]
\]

Cân bằng điện tích của dung dịch tổng quát:

\[
\sum_i z_i[i]=0
\]

Ba loại phương trình này biến bài toán cân bằng thành một hệ phương trình phi tuyến có thể giải số.

## Vì sao bảng ICE chỉ là trường hợp đơn giản?

Bảng `Initial–Change–Equilibrium` rất hữu ích cho một phản ứng đơn và số species ít.

Nhưng với nhiều cân bằng ghép, cách đặt một biến `x` cho tất cả thường không đủ.

Khi đó cách làm bền vững hơn là:

```text
liệt kê species
→ viết K cho từng cân bằng
→ viết mass balance
→ viết charge balance
→ giải hệ phương trình
```

Đây là cách phần mềm speciation và geochemical modeling hoạt động ở mức nền tảng.

## Độ nhạy theo K

Khi `K` rất lớn hoặc rất nhỏ, một số approximation trở nên mạnh.

Nếu:

\[
K\gg1
\]

có thể giả sử phản ứng gần hoàn toàn rồi xử lý phần cân bằng dư nhỏ.

Nếu:

\[
K\ll1
\]

có thể coi chuyển hóa nhỏ.

Nhưng khi nhiều `K` tương đương nhau, các species cạnh tranh mạnh và cần giải đồng thời.

## Cân bằng và thế hóa học

Ở cân bằng, với reaction coordinate \(\xi\):

\[
\left(\frac{\partial G}{\partial\xi}\right)_{T,P}=0
\]

Điều này tương đương:

\[
\sum_i\nu_i\mu_i=0
\]

Với:

\[
\mu_i=\mu_i^\circ+RT\ln a_i
\]

thay vào ta thu được biểu thức `Q=K`.

Do đó hằng số cân bằng không phải quy tắc riêng biệt; nó là hệ quả trực tiếp của việc **Gibbs free energy đạt cực tiểu dưới các ràng buộc**.

## Cân bằng hóa học và tối thiểu Gibbs

Trong hệ nhiều phản ứng, thay vì viết từng `K`, một cách tương đương là tối thiểu hóa tổng Gibbs free energy với các ràng buộc bảo toàn nguyên tố.

Cách này đặc biệt hữu ích trong:

- hệ đốt cháy nhiều species;
- plasma;
- cân bằng pha;
- địa hóa;
- tính toán nhiệt động công nghiệp.

Nó biến equilibrium thành một bài toán tối ưu có ràng buộc.

## Các hiểu lầm thường gặp

### “K lớn nghĩa phản ứng nhanh”

Không. `K` là đại lượng nhiệt động; tốc độ phụ thuộc hằng số tốc độ và hàng rào động học.

### “Nồng độ chất rắn tinh khiết phải đưa vào K”

Hoạt độ của pha tinh khiết được đưa vào định nghĩa trạng thái chuẩn và gần bằng 1 khi pha đó hiện diện.

### “K luôn có đơn vị”

Hằng số cân bằng nhiệt động được xây từ hoạt độ nên không thứ nguyên.

### “Thêm chất phản ứng làm K tăng”

Không. Nó làm `Q` thay đổi, còn `K` chỉ đổi nếu nhiệt độ hoặc định nghĩa trạng thái chuẩn đổi.

### “Một hệ có nhiều cân bằng có thể giải từng cân bằng hoàn toàn độc lập”

Không. Nếu các cân bằng dùng chung species, chúng bị ghép với nhau qua mass balance và charge balance.

### “Ksp nhỏ nghĩa chất luôn không tan”

Không. Proton hóa, tạo phức hoặc phản ứng phụ có thể kéo cân bằng hòa tan rất mạnh.

## Mô hình tư duy

`K` là **tọa độ nhiệt động của cân bằng trên địa hình Gibbs free energy**. Trong hệ đơn giản, nó cho tỉ lệ hoạt độ ở cân bằng. Trong hệ thật, nhiều `K` kết nối thành một mạng và cùng với bảo toàn vật chất + điện tích quyết định phân bố species. Vì vậy học `K` tốt nhất không phải là học từng công thức riêng, mà là học cách xây và giải một mạng cân bằng.

Xem tiếp: [Thương số phản ứng](./02_reaction_quotient.md).