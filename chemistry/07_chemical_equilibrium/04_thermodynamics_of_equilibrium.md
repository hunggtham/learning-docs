# Nhiệt động lực học của cân bằng — từ Gibbs tới thành phần và pha cân bằng

> Cân bằng hóa học không phải một tập hợp quy tắc rời như `K`, `Q`, Le Châtelier, `Ksp`, `Ka` hay `Kf`. Tất cả đều có thể được nhìn trong một khuôn khổ duy nhất: **hệ thay đổi thành phần cho tới khi thế nhiệt động phù hợp đạt cực tiểu dưới các ràng buộc bảo toàn**.

Trong điều kiện nhiệt độ và áp suất không đổi, thế đó là năng lượng tự do Gibbs \(G\). Cách nhìn này nối cân bằng phản ứng, cân bằng pha, hòa tan, acid–base, tạo phức và điện hóa vào cùng một ngôn ngữ.

Chapter này **không định nghĩa lại đầy đủ** thế hóa học, hoạt độ, fugacity hay đại lượng mol riêng phần. Các công cụ đó đã được xây ở [Nhiệt động lực học hóa học](../05_thermodynamics/04_chemical_thermodynamics.md). Ở đây mục tiêu là dùng chúng để trả lời bốn câu hỏi:

```text
hệ sẽ dịch chuyển theo hướng nào?
điều kiện nào xác định trạng thái cân bằng?
thành phần/phân bố pha ở cân bằng là gì?
nghiệm toán học nào thực sự bền về nhiệt động?
```

## Từ mức tiến triển phản ứng tới độ dốc của Gibbs

Xét một phản ứng có hệ số hóa lượng có dấu \(\nu_i\). Khi phản ứng tiến một lượng vi phân \(d\xi\):

\[
dn_i=\nu_i d\xi
\]

Ở \(T,P\) không đổi:

\[
dG=\sum_i\mu_i dn_i
\]

nên:

\[
\left(\frac{dG}{d\xi}\right)_{T,P}
=\sum_i\nu_i\mu_i
=\Delta_rG
\]

Vì vậy **năng lượng Gibbs phản ứng** chính là độ dốc của Gibbs theo mức tiến triển phản ứng.

```text
ΔrG < 0 → đi thuận làm G giảm
ΔrG > 0 → đi nghịch làm G giảm
ΔrG = 0 → điểm dừng theo tọa độ phản ứng
```

Đây là nền nhiệt động của hướng phản ứng.

## Cân bằng bền cần nhiều hơn \(dG/d\xi=0\)

Điều kiện:

\[
\frac{dG}{d\xi}=0
\]

chỉ cho một điểm dừng. Để cân bằng bền cục bộ còn cần độ cong theo hướng biến đổi khả dĩ là dương:

\[
\frac{d^2G}{d\xi^2}>0
\]

Nếu độ cong âm, trạng thái đó không bền trước nhiễu nhỏ.

Ý tưởng ổn định này mở rộng trực tiếp sang tách pha, spinodal decomposition và nhiều hiện tượng vật liệu.

## Từ thế hóa học tới \(Q\) và \(K\)

Ta dùng quan hệ đã xây ở thermodynamics:

\[
\mu_i=\mu_i^\circ+RT\ln a_i
\]

và:

\[
\Delta_rG=\sum_i\nu_i\mu_i
\]

suy ra:

\[
\Delta_rG
=\Delta_rG^\circ
+RT\ln\prod_i a_i^{\nu_i}
\]

Định nghĩa:

\[
Q=\prod_i a_i^{\nu_i}
\]

nên:

\[
\Delta_rG=\Delta_rG^\circ+RT\ln Q
\]

Tại cân bằng:

\[
\Delta_rG=0,\qquad Q=K
\]

suy ra:

\[
\Delta_rG^\circ=-RT\ln K
\]

Hằng số cân bằng vì thế là cách mã hóa chênh lệch năng lượng tự do chuẩn bằng hàm logarithm/exponential.

## Vì sao \(K\) phụ thuộc cách viết phương trình?

Nếu đảo phản ứng:

\[
\Delta_rG^\circ_{rev}=-\Delta_rG^\circ
\]

nên:

\[
K_{rev}=K^{-1}
\]

Nếu nhân phương trình phản ứng với \(m\):

\[
\Delta_rG^\circ_{new}=m\Delta_rG^\circ
\]

nên:

\[
K_{new}=K^m
\]

Điều này chứng minh \(K\) không phải thuộc tính của “một cặp chất” độc lập với phương trình. Nó thuộc về **một phản ứng được định nghĩa với hóa lượng cụ thể**.

## Phản ứng ghép

Nếu cộng hai phản ứng:

\[
R_1+R_2=R_3
\]

thì:

\[
\Delta G_3^\circ
=\Delta G_1^\circ+
\Delta G_2^\circ
\]

và:

\[
K_3=K_1K_2
\]

Đây là nền nhiệt động cho ghép phản ứng trong chuyển hóa sinh học hoặc tổng hợp hóa học.

Một phản ứng riêng lẻ có \(K<1\) vẫn có thể được kéo theo chiều thuận nếu được ghép cơ chế với phản ứng thứ hai có lực dẫn động đủ lớn và hai phản ứng chia sẻ chất trung gian phù hợp.

## Hoạt độ và fugacity — dùng, không định nghĩa lại

Trong dung dịch loãng gần lý tưởng:

\[
a_i\approx\frac{c_i}{c^\circ}
\]

Nhưng tổng quát:

\[
a_i=\gamma_i\frac{c_i}{c^\circ}
\]

Với khí thực, hoạt độ được biểu diễn qua fugacity:

\[
a_i=\frac{f_i}{f^\circ}
\]

Ý nghĩa và mô hình của \(\gamma_i\), fugacity, trạng thái chuẩn, Debye–Hückel, Pitzer, Raoult và Henry được trình bày ở [Nhiệt động lực học hóa học](../05_thermodynamics/04_chemical_thermodynamics.md). Trong chapter này chỉ cần giữ nguyên tắc:

> **\(K\) nhiệt động được xây từ hoạt độ, không phải từ nồng độ thô.**

Vì vậy hằng số biểu kiến dựa trên nồng độ có thể thay đổi khi lực ion, áp suất hoặc nền dung môi thay đổi.

Điều này đặc biệt quan trọng trong nước biển, điện ly pin đậm đặc, acid/base đậm đặc, dung dịch protein và nước muối địa hóa.

## Ảnh hưởng của nhiệt độ lên \(K\)

Quan hệ van ’t Hoff:

\[
\frac{d\ln K}{dT}
=\frac{\Delta H^\circ}{RT^2}
\]

Nếu \(\Delta H^\circ\) gần không đổi trong khoảng nhiệt độ hẹp:

\[
\ln\frac{K_2}{K_1}
=-\frac{\Delta H^\circ}{R}
\left(\frac1{T_2}-\frac1{T_1}\right)
\]

Đây là dạng định lượng của ảnh hưởng nhiệt độ lên cân bằng.

Nếu \(\Delta C_p\) đáng kể, \(\Delta H^\circ\) và \(\Delta S^\circ\) cũng thay theo nhiệt độ nên giả định enthalpy không đổi mất dần độ chính xác.

## Hiệu chỉnh theo nhiệt dung

Định luật Kirchhoff:

\[
\frac{d\Delta H}{dT}=\Delta C_p
\]

cho phép cập nhật enthalpy phản ứng theo nhiệt độ.

Khi cần dự đoán \(K\) trên khoảng nhiệt độ rộng, phải tích hợp sự thay đổi của các hàm nhiệt động thay vì ngoại suy một \(\Delta H\) cố định quá xa.

## Cân bằng pha là điều kiện bằng nhau của thế hóa học

Với thành phần \(i\) tồn tại trong hai pha \(\alpha\) và \(\beta\), cân bằng yêu cầu:

\[
\mu_i^\alpha=
\mu_i^\beta
\]

Nếu thế hóa học trong pha lỏng cao hơn pha hơi, chuyển lỏng → hơi làm Gibbs giảm; nếu ngược lại, ngưng tụ thuận lợi.

Tại cân bằng hai pha, không còn lực dẫn động ròng cho truyền vật chất.

## Phương trình Clapeyron

Dọc đường biên pha:

\[
\frac{dP}{dT}
=\frac{\Delta S_{tr}}{\Delta V_{tr}}
=\frac{\Delta H_{tr}}{T\Delta V_{tr}}
\]

Phương trình này giải thích độ dốc của đường đồng tồn tại pha từ enthalpy và thay đổi thể tích.

Đối với hóa hơi, \(\Delta V\) thường lớn và có thể dùng gần đúng khí lý tưởng để suy dạng Clausius–Clapeyron.

## Tiếp tuyến chung và tách pha trong hỗn hợp

Với hỗn hợp hai thành phần ở \(T,P\) cố định, đồ thị Gibbs mol theo thành phần có thể có vùng mà một pha đồng nhất không phải cực tiểu toàn cục.

Hai pha có thành phần \(x_\alpha\), \(x_\beta\) cùng tồn tại khi một **tiếp tuyến chung (common tangent)** chạm đường Gibbs ở hai điểm.

Sự bằng nhau của độ dốc tương ứng với sự bằng nhau của thế hóa học giữa hai pha.

Đây là nền của giản đồ pha hợp kim, trộn polymer và chiết lỏng–lỏng.

## Spinodal và trạng thái siêu bền

Một hỗn hợp có thể nằm trong vùng:

\[
\frac{d^2G}{dx^2}<0
\]

nơi nhiễu thành phần nhỏ tự phát lớn lên — **phân hủy spinodal (spinodal decomposition)**.

Ở vùng siêu bền ngoài spinodal nhưng vẫn trong khoảng không trộn lẫn, tách pha thuận lợi về nhiệt động nhưng cần vượt hàng rào tạo mầm.

Điều này minh họa rõ:

```text
thermodynamics → trạng thái cuối ưu tiên
kinetics       → hệ có vượt được hàng rào hay không
```

## Quá bão hòa không đồng nghĩa đã cân bằng

Một dung dịch có thể có:

\[
Q_{sp}>K_{sp}
\]

nhưng vẫn trong suốt nếu chưa tạo mầm tinh thể.

Đó là trạng thái siêu bền: kết tủa làm Gibbs giảm nhưng cần tạo mặt phân cách mới nên xuất hiện hàng rào tạo mầm.

Thêm tinh thể mồi cung cấp bề mặt sẵn có, giảm chi phí tạo mầm và có thể làm kết tủa bắt đầu gần như tức thời.

## Cực tiểu hóa Gibbs cho nhiều phản ứng

Với hàng chục tiểu phần, thay vì chọn một tập phản ứng rồi giải từng \(K\), có thể cực tiểu hóa:

\[
G=\sum_i n_i\mu_i
\]

với ràng buộc bảo toàn nguyên tố:

\[
A\mathbf n=\mathbf b
\]

và:

\[
n_i\ge0
\]

Cách này không phụ thuộc vào lựa chọn một tập phản ứng độc lập cụ thể. Nó đặc biệt hữu ích trong cháy, luyện kim và cân bằng nhiệt độ cao.

## Nhân tử Lagrange và bảo toàn nguyên tố

Cực tiểu Gibbs dưới các ràng buộc bảo toàn có thể dùng nhân tử Lagrange.

Về mặt toán học, thành phần cân bằng là nghiệm tối ưu có ràng buộc. Đây là liên hệ trực tiếp giữa nhiệt động lực học hóa học và lý thuyết tối ưu.

## Dạng tồn tại trong dung dịch

Cân bằng dung dịch thường được giải bằng một cách khác: hệ phương trình **cân bằng khối lượng + cân bằng điện tích + quan hệ cân bằng**.

Ví dụ acid hai proton:

\[
H_2A\rightleftharpoons H^++HA^-
\]

\[
HA^-\rightleftharpoons H^++A^{2-}
\]

Cân bằng khối lượng:

\[
C_T=[H_2A]+[HA^-]+[A^{2-}]
\]

kết hợp cân bằng điện tích và \(K_{a1},K_{a2}\) xác định phân bố dạng tồn tại.

Đây vẫn là cùng một nhiệt động lực học, chỉ được biểu diễn dưới dạng giải hệ phương trình thay vì cực tiểu hóa trực tiếp.

## Hằng số cân bằng có điều kiện

Nếu phản ứng chính phụ thuộc một tiểu phần chỉ tồn tại theo phân số \(\alpha\), có thể dùng hằng số hiệu dụng.

Ví dụ phối tử \(L\) bị proton hóa. Chỉ dạng tự do \(L\) liên kết kim loại:

\[
M+L\rightleftharpoons ML
\]

Nếu phân số phối tử tự do là \(\alpha_L\):

\[
K_f'=\alpha_LK_f
\]

Vì \(\alpha_L\) phụ thuộc pH, khả năng liên kết biểu kiến cũng phụ thuộc pH dù \(K_f\) nội tại không đổi.

Đây là cách cân bằng acid–base ghép vào [hóa học phối trí](../10_inorganic_chemistry/03_coordination_chemistry.md).

## Thế điện hóa trong cân bằng

Với ion điện tích \(z_i\) trong điện thế \(\phi\):

\[
\tilde\mu_i=
\mu_i+z_iF\phi
\]

là **thế điện hóa (electrochemical potential)**.

Cân bằng ion qua màng không chỉ yêu cầu thế hóa học bằng nhau mà yêu cầu thế điện hóa phù hợp.

Từ đây xuất hiện phương trình Nernst, điện thế màng và điện áp pin. Phần nền được xây chi tiết ở [Nhiệt động lực học hóa học](../05_thermodynamics/04_chemical_thermodynamics.md) và [phương trình Nernst](../09_redox_and_electrochemistry/03_cell_potential_and_nernst_equation.md).

## Thẩm thấu cũng là cân bằng thế hóa học

Qua màng bán thấm, dung môi dịch chuyển cho tới khi thế hóa học của dung môi đạt điều kiện cân bằng giữa hai phía.

Chênh lệch áp suất cần để ngăn dòng dung môi là áp suất thẩm thấu.

Trong dung dịch loãng:

\[
\Pi\approx cRT
\]

Đây là cùng framework thế hóa học, không phải một hiện tượng tách biệt khỏi cân bằng hóa học.

## Cân bằng trong sinh học

Nhiều cân bằng liên kết có dạng:

\[
P+L\rightleftharpoons PL
\]

với hằng số phân ly:

\[
K_d=\frac{[P][L]}{[PL]}
\]

Nhưng tế bào nhìn chung không ở cân bằng toàn cục. Chuyển hóa ATP, vận chuyển qua màng và metabolism duy trì nhiều thế hóa học xa cân bằng.

Do đó **xấp xỉ cân bằng cục bộ** có thể hữu ích cho một subsystem dù toàn tế bào ở trạng thái ổn định ngoài cân bằng.

## Cân bằng trong pin và lưu trữ năng lượng

Điện áp hở mạch liên hệ với năng lượng Gibbs phản ứng:

\[
\Delta G=-nFE
\]

Phương trình Nernst mô tả đóng góp của thành phần.

Khi pin phóng điện tiến gần trạng thái cân bằng hơn, công thuận nghịch khả dụng giảm. Nhưng pin thật còn có quá thế động học và tổn hao ohmic, nên điện áp đầu cực dưới tải không bằng điện áp cân bằng.

Đây là điểm nối giữa cân bằng nhiệt động và động học điện hóa.

## Bộ giải số và kiểm tra ổn định

Một bộ giải số không nên chỉ trả “đã hội tụ”. Cần kiểm tra:

- cân bằng nguyên tố;
- cân bằng điện tích;
- lượng các tiểu phần không âm;
- độ bền pha;
- hoạt độ nằm trong phạm vi hợp lệ của mô hình;
- Gibbs có thực sự là cực tiểu hay không.

Một nghiệm của hệ phương trình có thể không phải cân bằng vật lý.

### Ví dụ reasoning: vì sao nghiệm toán học chưa đủ?

Một solver có thể tìm được nghiệm thỏa phương trình cân bằng nhưng đặt hệ ở nhánh siêu bền hoặc dùng hệ số hoạt độ ngoài phạm vi mô hình. Vì vậy validation phải kiểm tra cả **conservation + model validity + thermodynamic stability**, không chỉ residual nhỏ.

## Những hiểu lầm thường gặp

### “Cân bằng là nơi chất phản ứng và sản phẩm bằng nhau”

Không. Cân bằng là cực tiểu nhiệt động dưới các ràng buộc; thành phần phụ thuộc \(K\), tổng lượng và điều kiện hệ.

### “\(K\) là một hằng số nồng độ tuyệt đối”

Không. \(K\) nhiệt động được xây từ hoạt độ. Hằng số biểu kiến dựa trên nồng độ có thể phụ thuộc lực ion và quy ước.

### “Nếu kết tủa thuận lợi thì chất rắn xuất hiện ngay”

Không. Động học tạo mầm có thể tạo trạng thái siêu bền.

### “Cân bằng phản ứng và cân bằng pha là hai lý thuyết khác nhau”

Không. Cả hai đều có thể viết bằng điều kiện thế hóa học và cực tiểu hóa thế nhiệt động thích hợp.

### “Bộ giải số hội tụ nghĩa kết quả đúng”

Không. Cần kiểm tra bảo toàn, ràng buộc vật lý, phạm vi mô hình và độ bền nhiệt động.

### “Thermodynamics of equilibrium phải định nghĩa lại toàn bộ activity/fugacity”

Không. Đây là chapter ứng dụng. Định nghĩa và mô hình tính không lý tưởng thuộc [Nhiệt động lực học hóa học](../05_thermodynamics/04_chemical_thermodynamics.md).

## Mô hình tư duy

Có thể nén toàn bộ cân bằng hóa học vào một sơ đồ:

```text
thành phần + T + P
→ thế hóa học μi
→ Gibbs G
→ cực tiểu hóa dưới ràng buộc
→ thành phần / pha cân bằng
```

Các công cụ quen thuộc chỉ là nhiều giao diện cho cùng framework:

```text
K và Q        → nhìn theo tọa độ phản ứng
Ka/Ksp/Kf     → cân bằng chuyên biệt
phase diagram → nhìn theo độ bền pha
Nernst        → nhìn theo thế điện hóa
speciation    → nhìn theo cân bằng khối/điện tích
G minimizer   → nhìn theo tối ưu toàn cục
```

Xem tiếp: [Các mô hình acid–base](../08_acids_bases/00_acid_base_models.md), [Điện hóa](../09_redox_and_electrochemistry/03_cell_potential_and_nernst_equation.md) và quay lại [Nhiệt động lực học hóa học](../05_thermodynamics/04_chemical_thermodynamics.md) nếu cần activity/fugacity/nonideality chi tiết hơn.