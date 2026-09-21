# Thương số phản ứng — xác định chiều dịch chuyển từ trạng thái hiện tại

> **Thương số phản ứng (reaction quotient, \(Q\) / 반응 지수)** có cùng cấu trúc toán học với hằng số cân bằng nhưng được tính từ **trạng thái hiện tại** của hệ. Nếu \(K\) mô tả vị trí cân bằng ở một nhiệt độ xác định, thì \(Q\) là tọa độ tức thời cho biết hỗn hợp đang nằm ở phía nào so với vị trí đó.

Đây là một trong những công cụ reasoning mạnh nhất của hóa học cân bằng vì nó thay thế các khẩu hiệu kiểu “hệ sẽ chống lại thay đổi” bằng một tiêu chuẩn định lượng.

## Định nghĩa tổng quát

Với phản ứng:

\[
aA+bB\rightleftharpoons cC+dD
\]

thương số phản ứng nhiệt động:

\[
Q=\frac{a_C^ca_D^d}{a_A^aa_B^b}
\]

trong đó \(a_i\) là **hoạt độ (activity)**.

Tại cân bằng:

\[
Q=K
\]

Ngoài cân bằng, \(Q\) có thể nhỏ hơn hoặc lớn hơn \(K\).

## Vì sao so sánh Q với K cho biết chiều tự diễn ra?

Ta có:

\[
\Delta_rG=\Delta_rG^\circ+RT\ln Q
\]

và:

\[
\Delta_rG^\circ=-RT\ln K
\]

kết hợp lại:

\[
\Delta_rG=RT\ln\frac{Q}{K}
\]

Do đó:

```text
Q < K → ΔrG < 0 → chiều thuận làm G giảm
Q > K → ΔrG > 0 → chiều nghịch làm G giảm
Q = K → ΔrG = 0 → cân bằng
```

Đây không phải mẹo ghi nhớ. Nó là hệ quả trực tiếp của chemical potential và Gibbs free energy.

## Q không phải “lượng sản phẩm”

Một sai lầm phổ biến là nghĩ \(Q<K\) nghĩa “sản phẩm đang ít”. Q là **tỉ số hoạt độ có lũy thừa stoichiometric**, nên kết luận phải dựa trên toàn biểu thức.

Ví dụ:

\[
N_2+3H_2\rightleftharpoons2NH_3
\]

\[
Q=\frac{a_{NH_3}^2}{a_{N_2}a_{H_2}^3}
\]

Một thay đổi nhỏ ở \(H_2\) có thể ảnh hưởng Q mạnh vì lũy thừa ba.

## Q là “ảnh chụp”, K là “đích”

Có thể hình dung:

```text
composition hiện tại → tính Q
K tại nhiệt độ đó → vị trí equilibrium
so Q/K → chiều thermodynamic driving force
```

K không phụ thuộc composition ban đầu; Q thì thay đổi mỗi khi composition, pressure hoặc activity thay đổi.

## Khí lý tưởng

Với khí gần lý tưởng:

\[
a_i\approx\frac{P_i}{P^\circ}
\]

nên Q có thể tính bằng áp suất riêng phần.

Ví dụ:

\[
2SO_2+O_2\rightleftharpoons2SO_3
\]

\[
Q_p\approx
\frac{(P_{SO_3}/P^\circ)^2}
{(P_{SO_2}/P^\circ)^2(P_{O_2}/P^\circ)}
\]

Nếu nén hệ, các partial pressures thay đổi và Q có thể thay đổi ngay trước khi composition kịp phản ứng. Chính thay đổi Q đó tạo driving force mới.

## Dung dịch và hoạt độ

Trong dung dịch loãng:

\[
a_i\approx\frac{[i]}{c^\circ}
\]

nhưng khi ionic strength cao:

\[
a_i=\gamma_i\frac{[i]}{c^\circ}
\]

với \(\gamma_i\) là **hệ số hoạt độ (activity coefficient)**.

Nếu chỉ dùng concentration trong nước biển hoặc electrolyte đậm đặc, Q tính được có thể lệch đáng kể khỏi thermodynamic Q.

Đây là lý do pH, solubility, electrochemistry và speciation ở hệ đậm đặc cần activity models.

## Chất rắn và chất lỏng tinh khiết

Hoạt độ của một pha tinh khiết ở trạng thái chuẩn gần 1, nên nó thường không xuất hiện tường minh trong Q.

Ví dụ:

\[
CaCO_3(s)\rightleftharpoons CaO(s)+CO_2(g)
\]

\[
Q\approx\frac{P_{CO_2}}{P^\circ}
\]

Thêm nhiều \(CaCO_3\) rắn hơn không trực tiếp làm Q đổi miễn pha đó đã hiện diện và vẫn tinh khiết. Đây là điểm mà reasoning “tăng reactant → shift right” kiểu máy móc có thể sai.

# Q sau một perturbation

Giả sử hệ ban đầu ở equilibrium, nên:

\[
Q=K
\]

Ta đột ngột thêm A. Ngay sau khi thêm nhưng **trước khi reaction kịp đáp ứng**, \(a_A\) tăng nên Q thay đổi.

Nếu A ở denominator, Q giảm:

\[
Q<K
\]

sau đó reaction tiến thuận cho tới khi Q trở về K.

Cách chia quá trình thành:

```text
1. perturbation làm Q thay đổi tức thời
2. reaction response làm composition đổi
3. equilibrium mới khi Q = K
```

là cách hiểu sâu hơn Le Châtelier.

# Bảng ICE — công cụ hạch toán, không phải định luật

Với:

\[
A\rightleftharpoons B
\]

ban đầu:

\[
[A]_0=a,\qquad[B]_0=b
\]

nếu phản ứng tiến thuận lượng \(x\):

\[
[A]=a-x
\]

\[
[B]=b+x
\]

Tại equilibrium:

\[
K=\frac{b+x}{a-x}
\]

**ICE (Initial–Change–Equilibrium)** chỉ là bảng giúp tổ chức stoichiometric bookkeeping. Physics nằm trong conservation + equilibrium condition, không nằm trong chữ ICE.

# Extent of reaction là cách tổng quát hơn ICE

Với nhiều species, dùng **mức tiến triển phản ứng (extent of reaction, \(\xi\))**:

\[
dn_i=\nu_i d\xi
\]

nên:

\[
n_i=n_{i,0}+\nu_i\xi
\]

Sau đó Q trở thành hàm của \(\xi\):

\[
Q=Q(\xi)
\]

Equilibrium được tìm từ:

\[
Q(\xi_{eq})=K
\]

Cách này thống nhất ICE table với thermodynamics và mở rộng tự nhiên sang reaction networks.

# Xấp xỉ “x nhỏ” phải được kiểm tra

Trong weak equilibrium, ta thường gặp:

\[
K=\frac{x^2}{C_0-x}
\]

Nếu \(x\ll C_0\), có thể gần đúng:

\[
C_0-x\approx C_0
\]

Nhưng approximation phải được **kiểm tra sau khi giải**.

“Quy tắc 5%” chỉ là heuristic cho một mức accuracy nhất định. Nếu mục tiêu là analytical chemistry chính xác cao, 5% có thể hoàn toàn không chấp nhận được.

# Khi phương trình equilibrium có nhiều nghiệm toán học

Một phương trình polynomial có thể cho nhiều roots, nhưng không phải root nào cũng có ý nghĩa vật lý.

Nghiệm phải thỏa:

- concentration không âm;
- conservation laws;
- extent nằm trong giới hạn reactants available;
- phase assumptions ban đầu còn hợp lệ.

Đây là lý do solving equilibrium không chỉ là giải đại số rồi chọn một số.

# Cân bằng ghép — Q của một phản ứng không tồn tại cô lập

Trong dung dịch thật, một species có thể tham gia nhiều equilibria đồng thời.

Ví dụ metal \(M^{2+}\) có thể:

\[
M^{2+}+L^-\rightleftharpoons ML^+
\]

trong khi ligand proton hóa:

\[
HL\rightleftharpoons H^++L^-
\]

và metal hydroxide kết tủa:

\[
M^{2+}+2OH^-\rightleftharpoons M(OH)_2(s)
\]

Thêm acid làm thay đổi ligand speciation, rồi gián tiếp thay complex formation và solubility. Không thể giải từng equilibrium như các bài toán hoàn toàn độc lập.

# Mass balance

Nếu tổng ligand là \(C_L\):

\[
C_L=[HL]+[L^-]+[ML^+]+...
\]

Đây là **cân bằng vật chất (mass balance)**.

# Charge balance

Dung dịch vĩ mô phải gần trung hòa điện tích:

\[
\sum_i z_i[i]=0
\]

Đây là **cân bằng điện tích (charge balance)**.

Kết hợp mass balances, charge balance và equilibrium constants tạo một hệ nonlinear equations đủ để xác định speciation.

# Conditional equilibrium constant

Nếu chỉ một fraction ligand tồn tại ở dạng reactive \(L^-\), apparent complex formation có thể viết bằng **hằng số điều kiện (conditional constant)** phụ thuộc pH.

Điều này rất quan trọng trong EDTA titration và metal speciation: intrinsic \(K_f\) có thể rất lớn nhưng effective binding ở pH thấp yếu hơn vì ligand bị proton hóa.

# Saturation quotient — Q cho precipitation

Với:

\[
MX(s)\rightleftharpoons M^++X^-
\]

ion activity product:

\[
Q_{sp}=a_{M^+}a_{X^-}
\]

so với \(K_{sp}\):

```text
Qsp < Ksp → chưa bão hòa
Qsp = Ksp → cân bằng với solid
Qsp > Ksp → precipitation thermodynamically favored
```

Nhưng \(Q_{sp}>K_{sp}\) không đảm bảo kết tủa xuất hiện ngay; nucleation barrier là vấn đề động học.

Đây là ví dụ trực tiếp cho việc thermodynamic driving force và kinetics phải được tách biệt.

# Reaction quotient trong electrochemistry

Phương trình Nernst:

\[
E=E^\circ-\frac{RT}{nF}\ln Q
\]

cho thấy cell voltage thay đổi khi composition thay đổi.

Khi cell discharge, Q tiến dần về K và driving force giảm. Tại equilibrium:

\[
Q=K
\]

và cell không còn khả năng sinh công điện thuận nghịch ròng.

Vì vậy Q là cầu nối giữa equilibrium chemistry và battery voltage.

# Reaction quotient trong biology

Một phản ứng sinh hóa có \(\Delta G^\circ>0\) vẫn có thể đi thuận trong tế bào nếu concentration ratios làm Q đủ nhỏ:

\[
\Delta G=\Delta G^\circ+RT\ln Q<0
\]

Tế bào duy trì non-equilibrium concentrations bằng metabolism và transport. Do đó biết standard free energy chưa đủ để biết direction trong vivo.

# Giải equilibrium bằng máy tính

Hệ nhiều equilibria thường được giải bằng numerical root finding hoặc Gibbs minimization.

Một workflow:

```text
chọn species
→ viết equilibrium constants
→ viết mass/charge balances
→ chọn variables như log concentration
→ solve nonlinear system
→ kiểm tra conservation và phase stability
```

Dùng \(\log c\) làm variable giúp concentration luôn dương và xử lý range nhiều orders of magnitude.

Các phần mềm địa hóa, combustion equilibrium và aqueous speciation đều dùng tư duy này.

# Sensitivity — equilibrium composition nhạy với parameter nào?

Nếu \(K\) có uncertainty hoặc temperature thay đổi, equilibrium composition cũng thay đổi.

Có thể hỏi:

\[
\frac{\partial x_{eq}}{\partial \ln K}
\]

để biết species nào nhạy nhất với equilibrium data.

Trong environmental modeling, uncertainty của formation constants có thể trở thành uncertainty lớn của predicted mobility/toxicity.

# Những hiểu lầm thường gặp

### “Q<K nghĩa số mol sản phẩm ít hơn chất phản ứng”

Không. Q là một tỉ số có exponents và activities.

### “Q cho biết reaction nhanh theo chiều nào”

Q cho thermodynamic direction. Tốc độ cần kinetics.

### “ICE table là định luật hóa học”

Không. Nó chỉ là bookkeeping format.

### “Qsp>Ksp thì kết tủa xuất hiện tức thì”

Không. Supersaturation có thể tồn tại nếu nucleation chậm.

### “Mỗi equilibrium trong dung dịch có thể giải độc lập”

Không khi chúng chia sẻ species. Phải giải coupled system.

## Mô hình tư duy

Hãy xem \(Q\) như **tọa độ composition trên địa hình Gibbs**:

```text
Q/K < 1 → slope xuống theo chiều thuận
Q/K > 1 → slope xuống theo chiều nghịch
Q/K = 1 → slope bằng 0 tại equilibrium
```

Trong hệ phức tạp, không còn một Q đơn lẻ mà là một mạng các reaction quotients bị ràng buộc bởi mass balance, charge balance và phase constraints.

Xem tiếp: [Nguyên lý Le Châtelier](./03_le_chatelier_principle.md) và [Nhiệt động lực học của cân bằng](./04_thermodynamics_of_equilibrium.md).