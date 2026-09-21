# Nhiệt động lực học hóa học — thế hóa học, hoạt độ và hệ nhiều thành phần

> **Nhiệt động lực học hóa học (chemical thermodynamics / 화학 열역학)** mở rộng các khái niệm về năng lượng, entropy và Gibbs sang hỗn hợp nhiều thành phần. Khái niệm trung tâm là **thế hóa học (chemical potential, \(\mu_i\) / 화학 퍼텐셜)**: mức thay đổi cận biên của năng lượng tự do Gibbs khi thêm một lượng nhỏ tiểu phần vào hệ trong điều kiện xác định.

Thế hóa học là ngôn ngữ chung giúp nối nhiều hiện tượng tưởng như tách biệt: khuếch tán, hòa tan, cân bằng pha, phản ứng hóa học, thẩm thấu, điện hóa và vận chuyển qua màng.

Chapter này tập trung vào **định nghĩa và công cụ nhiệt động cho hệ nhiều thành phần**: đại lượng mol riêng phần, hoạt độ, fugacity, tính không lý tưởng, Gibbs–Duhem và thế điện hóa. Chapter [Nhiệt động lực học của cân bằng](../07_chemical_equilibrium/04_thermodynamics_of_equilibrium.md) sẽ dùng các công cụ này để phân tích điều kiện cân bằng phản ứng và pha. Hai chapter bổ sung cho nhau thay vì lặp cùng mục tiêu.

Nếu các nền tảng chưa chắc, nên quay lại [năng lượng, nhiệt và công](./00_energy_heat_and_work.md), [entropy](./02_entropy.md) và [năng lượng tự do Gibbs](./03_gibbs_free_energy.md).

## Phương trình vi phân của Gibbs

Với hệ nhiều thành phần:

\[
dG=VdP-SdT+\sum_i\mu_i dn_i
\]

Phương trình này nói Gibbs có thể thay đổi vì:

- áp suất thay đổi;
- nhiệt độ thay đổi;
- thành phần hệ thay đổi.

Ở nhiệt độ và áp suất không đổi:

\[
dG=\sum_i\mu_i dn_i
\]

Khi đó thay đổi thành phần trở thành trọng tâm của nhiệt động lực học hóa học.

## Thế hóa học là Gibbs mol riêng phần

Định nghĩa:

\[
\mu_i=
\left(
\frac{\partial G}{\partial n_i}
\right)_{T,P,n_{j\ne i}}
\]

Đây không phải đơn giản là \(G/n_i\). Nó là đạo hàm: nếu thêm một lượng rất nhỏ tiểu phần \(i\) trong khi giữ \(T,P\) và lượng các thành phần khác cố định, năng lượng tự do Gibbs thay đổi bao nhiêu.

Trong hỗn hợp, môi trường xung quanh tiểu phần rất quan trọng. Một mol ethanol thêm vào ethanol tinh khiết và một mol ethanol thêm vào dung dịch nước loãng không có cùng thế hóa học.

## Đại lượng mol riêng phần

Cùng logic áp dụng cho bất kỳ đại lượng mở rộng \(X\):

\[
\bar X_i=
\left(
\frac{\partial X}{\partial n_i}
\right)_{T,P,n_j}
\]

Ví dụ:

- thể tích mol riêng phần \(\bar V_i\);
- enthalpy mol riêng phần \(\bar H_i\);
- thế hóa học \(\bar G_i=\mu_i\).

Trong hỗn hợp:

\[
X=\sum_i n_i\bar X_i
\]

cho các đại lượng mở rộng phù hợp.

## Vì sao thể tích khi trộn không cộng đơn giản?

Nếu trộn nước và ethanol, cách các phân tử đóng gói thay đổi do liên kết hydrogen và sự tái tổ chức cấu trúc.

Do đó nói chung:

\[
V_{mixture}
\ne V_{water,pure}+V_{ethanol,pure}
\]

ở cùng số mol tương ứng.

Thể tích mol riêng phần mô tả đóng góp thực của từng thành phần trong chính môi trường hỗn hợp.

Đây là lý do khi pha dung dịch chính xác phải **pha loãng tới thể tích cuối** thay vì giả định các thể tích ban đầu cộng đúng tuyệt đối.

## Thế hóa học của khí lý tưởng

Với thành phần khí lý tưởng \(i\):

\[
\mu_i=\mu_i^\circ(T)+RT\ln\frac{P_i}{P^\circ}
\]

Tăng áp suất riêng phần làm thế hóa học tăng theo logarithm.

Nếu hai vùng có cùng nhiệt độ nhưng \(P_i\) khác nhau và tiểu phần có thể di chuyển, sẽ có lực dẫn động truyền khối từ vùng có \(\mu_i\) cao tới vùng có \(\mu_i\) thấp cho tới khi đạt điều kiện cân bằng thích hợp.

## Hoạt độ — cách viết tổng quát

Nhiệt động lực học dùng:

\[
\mu_i=\mu_i^\circ+RT\ln a_i
\]

**Hoạt độ (activity, \(a_i\))** là biến thành phần hiệu dụng không thứ nguyên được định nghĩa sao cho quan hệ thế hóa học có dạng trên.

Về logic, hoạt độ không chỉ là “nồng độ đã sửa”. Nó được định nghĩa qua thế hóa học; hệ số hoạt độ là cách nối hoạt độ với một thang nồng độ cụ thể.

## Hệ số hoạt độ

Trên thang nồng độ dung dịch:

\[
a_i=\gamma_i\frac{c_i}{c^\circ}
\]

Trong giới hạn dung dịch loãng lý tưởng:

\[
\gamma_i\to1
\]

Nhưng tương tác ion–ion, dung môi–chất tan và hiệu ứng đóng gói làm \(\gamma_i\ne1\).

Vì cân bằng hóa học và thế điện hóa phụ thuộc hoạt độ, chỉ biết nồng độ đôi khi chưa đủ.

## Lực ion

Với dung dịch điện ly:

\[
I=\frac12\sum_i c_i z_i^2
\]

Độ lớn điện tích được bình phương nên ion hai điện tích ảnh hưởng khí quyển ion mạnh hơn ion một điện tích ở cùng nồng độ.

Ở lực ion thấp, định luật giới hạn Debye–Hückel:

\[
\log\gamma_i\approx-Az_i^2\sqrt I
\]

cho xấp xỉ định tính và định lượng bậc đầu.

Ở lực ion cao hơn cần các mô hình mở rộng như Debye–Hückel mở rộng, Davies, SIT hoặc Pitzer tùy hệ.

## Vì sao hoạt độ của một ion riêng lẻ khó đo trực tiếp?

Dung dịch vĩ mô phải gần trung hòa điện tích. Thí nghiệm điện hóa thường đo tổ hợp thế hóa học của nhiều ion cùng với ảnh hưởng của điện cực tham chiếu và thế nối lỏng.

Do đó hệ số hoạt độ của một ion riêng lẻ phụ thuộc quy ước; hệ số hoạt độ ion trung bình của điện ly dễ liên hệ với đại lượng thực nghiệm hơn.

Điểm này đặc biệt quan trọng khi hiểu pH nhiệt động ở mức đo lường học.

## Fugacity cho khí thực

Khí lý tưởng dùng áp suất trực tiếp. Với khí thực, ta dùng **hoạt áp (fugacity, \(f\))**:

\[
\mu_i=\mu_i^\circ+RT\ln\frac{f_i}{f^\circ}
\]

với:

\[
f_i=\phi_iP_i
\]

trong đó \(\phi_i\) là **hệ số fugacity (fugacity coefficient)**.

Khi áp suất đủ thấp:

\[
\phi_i\to1
\]

và fugacity tiến gần áp suất.

Ở quy trình áp suất cao, cân bằng pha/phản ứng thường cần phương trình trạng thái như Peng–Robinson hoặc Soave–Redlich–Kwong để ước lượng fugacity.

## Dung dịch lý tưởng và định luật Raoult

Trong dung dịch lỏng lý tưởng:

\[
a_i=x_i
\]

nếu chọn trạng thái chuẩn là chất lỏng tinh khiết phù hợp.

Định luật Raoult:

\[
P_i=x_iP_i^*
\]

xuất hiện khi thế hóa học của thành phần trong pha lỏng và pha hơi bằng nhau dưới các giả định lý tưởng.

Vì vậy Raoult không phải một quy tắc thực nghiệm tách rời; nó xuất phát từ điều kiện cân bằng thế hóa học.

## Định luật Henry — trạng thái chuẩn khác

Với chất tan rất loãng, trạng thái chuẩn kiểu Raoult có thể không thuận tiện. Định luật Henry:

\[
P_i=K_Hx_i
\]

mô tả hành vi của chất tan loãng.

Điểm quan trọng là **quy ước trạng thái chuẩn khác nhau** tạo các định nghĩa hoạt độ khác nhau, nhưng dự đoán vật lý vẫn nhất quán nếu toàn bộ phép tính dùng cùng một quy ước.

## Đại lượng dư và tính không lý tưởng

Độ lệch khỏi dung dịch lý tưởng có thể mô tả bằng **năng lượng Gibbs dư (excess Gibbs energy)**:

\[
G^E=G-G^{ideal}
\]

Hệ số hoạt độ liên hệ với các đạo hàm của \(G^E\).

Các mô hình như Margules, Wilson, NRTL hoặc UNIQUAC biểu diễn năng lượng tự do dư của hỗn hợp lỏng.

Đây là nền của mô phỏng quá trình, cân bằng hơi–lỏng và thiết kế phân tách.

## Độ lệch dương và âm khỏi Raoult

Nếu tương tác A–B yếu hơn trung bình của A–A và B–B, các phân tử dễ thoát khỏi pha lỏng hơn, làm áp suất hơi cao hơn lý tưởng — **độ lệch dương**.

Nếu tương tác A–B mạnh hơn, ta có **độ lệch âm**.

Độ lệch mạnh có thể tạo azeotrope, nơi thành phần pha hơi và pha lỏng bằng nhau tại một áp suất/nhiệt độ xác định.

## Azeotrope từ góc nhìn thế hóa học

Azeotrope không phải “hai chất có cùng nhiệt độ sôi”. Nó là thành phần mà cân bằng hơi–lỏng cho:

\[
y_i=x_i
\]

và chưng cất phân đoạn thông thường không thể vượt thành phần đó ở áp suất cố định.

Thay đổi áp suất hoặc thêm chất hỗ trợ tách có thể làm thay đổi cảnh quan Gibbs và vượt giới hạn của hệ ban đầu.

## Gibbs–Duhem — thế hóa học không độc lập

Với một pha đồng nhất:

\[
SdT-VdP+\sum_i n_i d\mu_i=0
\]

Ở nhiệt độ và áp suất không đổi:

\[
\sum_i n_i d\mu_i=0
\]

Đây là **phương trình Gibbs–Duhem**.

Nó nói nếu thế hóa học của một thành phần thay đổi theo thành phần hỗn hợp, thế hóa học của các thành phần khác không thể thay đổi tùy ý độc lập.

Trong hỗn hợp hai thành phần, biết hành vi hoạt độ của một thành phần đặt ràng buộc lên thành phần kia.

## Năng lượng Gibbs phản ứng

Với hệ số hóa lượng \(\nu_i\):

\[
\Delta_rG=\sum_i\nu_i\mu_i
\]

và:

\[
\Delta_rG
=\Delta_rG^\circ+RT\ln Q
\]

Nếu \(\Delta_rG<0\), một tiến triển phản ứng vi phân theo chiều thuận làm Gibbs giảm.

Tại cân bằng:

\[
\Delta_rG=0
\]

suy ra:

\[
K=\prod_i a_i^{\nu_i}
\]

Đây là cầu nối sang [cân bằng hóa học](../07_chemical_equilibrium/01_equilibrium_constant.md). Chapter này cung cấp ngôn ngữ thế hóa học; chapter cân bằng tập trung vào cách dùng nó để giải bài toán thành phần và trạng thái cân bằng.

## Ái lực hóa học

Một quy ước trong nhiệt động lực học định nghĩa **ái lực hóa học (chemical affinity)**:

\[
\mathcal A=-\Delta_rG
\]

Nếu \(\mathcal A>0\), chiều thuận có lực dẫn động nhiệt động.

Ở cân bằng:

\[
\mathcal A=0
\]

Khái niệm này đặc biệt hữu ích khi nối cân bằng với nhiệt động lực học không cân bằng.

## Cân bằng pha

Nếu thành phần \(i\) có thể chuyển giữa các pha \(\alpha\) và \(\beta\), cân bằng yêu cầu:

\[
\mu_i^\alpha=\mu_i^\beta
\]

Nếu hai giá trị chưa bằng nhau, truyền vật chất theo hướng làm tổng Gibbs giảm.

Sự sôi, hòa tan, chiết, phân bố và tách pha đều dựa trên điều kiện này.

## Hệ số phân bố

Một chất tan phân bố giữa hai pha không trộn lẫn cho tới khi thế hóa học của nó trong hai pha đạt điều kiện cân bằng.

Trong điều kiện loãng, quan hệ có thể rút gọn thành hệ số phân bố:

\[
K_D=\frac{c_{org}}{c_{aq}}
\]

Nhưng nếu chất tan ion hóa hoặc tạo phức, tỉ số phân bố phụ thuộc pH và toàn bộ bài toán dạng tồn tại.

Chiết lỏng–lỏng vì vậy là ứng dụng của **nhiệt động lực học hóa học + acid–base + cân bằng dạng tồn tại**.

## Thẩm thấu — thế hóa học của dung môi

Xét hai dung dịch ngăn bởi màng chỉ cho dung môi đi qua.

Chất tan làm thế hóa học của dung môi giảm. Dung môi có xu hướng đi về phía có thế hóa học dung môi thấp hơn cho tới khi đóng góp của chênh lệch áp suất cân bằng đóng góp do trộn.

Trong giới hạn dung dịch loãng lý tưởng:

\[
\Pi=cRT
\]

Đây là phương trình áp suất thẩm thấu van ’t Hoff.

Thẩm thấu không phải “nước muốn pha loãng nơi đậm đặc”; nó là quá trình tiến tới điều kiện cân bằng thế hóa học.

## Tính chất tập hợp

Hạ điểm đông, nâng điểm sôi và áp suất thẩm thấu phụ thuộc chủ yếu số tiểu phân chất tan trong giới hạn dung dịch loãng lý tưởng.

Nguồn gốc chung là chất tan làm giảm thế hóa học của dung môi.

Vì vậy các **tính chất tập hợp (colligative properties)** không phải nhiều quy tắc rời; chúng là các biểu hiện khác nhau của cùng một thay đổi thế hóa học.

## Thế điện hóa

Với ion có điện tích \(z_i\) trong điện thế \(\phi\):

\[
\tilde\mu_i=\mu_i+z_iF\phi
\]

Chuyển động của ion phụ thuộc gradient của **thế điện hóa (electrochemical potential)**, không chỉ gradient nồng độ.

Đây là nền cho:

- điện thế màng;
- phương trình Nernst;
- vận chuyển ion;
- pin;
- điện phân.

## Phương trình Nernst từ thế điện hóa

Ở cân bằng điện cực, thế điện hóa của các tiểu phần oxy hóa–khử và electron phải thỏa điều kiện cân bằng.

Kết quả cho phản ứng điện hóa:

\[
E=E^\circ-\frac{RT}{nF}\ln Q
\]

Điện áp là một cách biểu diễn chênh lệch năng lượng tự do trên mỗi đơn vị điện tích.

Điều này nối nhiệt động lực học hóa học trực tiếp với [điện hóa học](../09_redox_and_electrochemistry/03_cell_potential_and_nernst_equation.md), điện tử và lưu trữ năng lượng.

## Khuếch tán từ gradient thế hóa học

Định luật Fick đơn giản dùng gradient nồng độ:

\[
J=-D\nabla c
\]

nhưng mô tả nhiệt động sâu hơn cho rằng thông lượng được thúc đẩy bởi gradient thế hóa học.

Trong hỗn hợp không lý tưởng, chỉ nhìn gradient nồng độ có thể không dự đoán đúng hướng và mức truyền vật chất nếu các tương tác thành phần đủ mạnh.

Nhiệt động lực học không cân bằng phát triển quan hệ giữa thông lượng và lực nhiệt động.

## Hoạt độ nước và đời sống

Sự phát triển của vi sinh vật phụ thuộc không chỉ tổng hàm lượng nước mà còn **hoạt độ nước (water activity)**.

Muối hoặc đường đậm đặc làm thế hóa học/hoạt độ của nước giảm, khiến vi sinh vật khó duy trì cân bằng nước.

Đây là cơ sở nhiệt động của ướp muối, dùng đường đậm đặc và nhiều phương pháp bảo quản thực phẩm.

## Gấp protein và thế hóa học

Năng lượng tự do gấp protein phụ thuộc dung môi, ion, pH, chất đồng tan và nhiệt độ.

Sự chen chúc đại phân tử hoặc chất biến tính làm thay đổi thế hóa học của trạng thái gấp và không gấp.

Do đó “protein có một năng lượng gấp cố định” là mô tả quá đơn giản; độ bền là thuộc tính nhiệt động phụ thuộc môi trường.

## Độ tan — cân bằng giữa pha rắn và dung dịch

Một chất rắn tan tới khi thế hóa học của chất tan trong pha rắn và pha dung dịch đạt điều kiện cân bằng.

Nếu thế hóa học của chất tan trong dung dịch thấp hơn, hòa tan có xu hướng thuận lợi về nhiệt động.

Nếu dung dịch quá bão hòa, kết tinh thuận lợi về nhiệt động nhưng động học tạo mầm có thể trì hoãn quá trình.

Đây là cầu nối quan trọng giữa nhiệt động lực học và động học.

## Điện ly pin — tính không lý tưởng thật sự quan trọng

Điện ly Li-ion đậm đặc không phải dung dịch loãng lý tưởng.

Hệ số hoạt độ, ghép cặp ion, cấu trúc solvat hóa và số vận chuyển ảnh hưởng:

- điện áp pin;
- độ dẫn điện;
- phân cực nồng độ;
- động học mặt phân cách.

Vì vậy “1 M LiPF6” không đủ để mô tả đầy đủ trạng thái nhiệt động của điện ly.

Nhiệt động lực học hóa học là nền để hiểu pin vượt ra ngoài phương trình Nernst lý tưởng đơn giản.

## Nhiệt động lực học tính toán

Trong khoa học vật liệu, **CALPHAD** xây các mô hình năng lượng Gibbs của các pha từ dữ liệu thực nghiệm và tính toán.

Sau đó phần mềm cực tiểu hóa tổng Gibbs để tạo giản đồ pha nhiều thành phần.

Đây là ứng dụng trực tiếp của đại lượng mol riêng phần và cực tiểu hóa Gibbs vào thiết kế hợp kim, vật liệu pin và hệ nhiều pha.

## Trạng thái chuẩn và quy ước tham chiếu

\(\mu_i^\circ\), hoạt độ và năng lượng tự do chuẩn phụ thuộc quy ước trạng thái chuẩn.

Dự đoán vật lý không phụ thuộc quy ước nếu mọi đại lượng được dùng nhất quán.

Điều này giống việc chọn mốc thế năng: mốc tham chiếu có thể thay đổi, nhưng các chênh lệch quan sát được không đổi.

## Những hiểu lầm thường gặp

### “Thế hóa học là nồng độ”

Không. Nồng độ chỉ là một biến ảnh hưởng \(\mu\); tương tác, nhiệt độ, áp suất và trường ngoài cũng ảnh hưởng.

### “Hoạt độ chỉ là nồng độ gần đúng hơn”

Không hoàn toàn. Hoạt độ được định nghĩa thông qua thế hóa học; nồng độ cùng hệ số hoạt độ là một mô hình để biểu diễn nó.

### “Dung dịch lý tưởng nghĩa là các phân tử không tương tác”

Không. Nó nghĩa thay đổi tương tác khi trộn phù hợp với hành vi nhiệt động lý tưởng; các phân tử vẫn tương tác.

### “Azeotrope xảy ra vì hai chất có cùng nhiệt độ sôi”

Không. Nó là đặc trưng của cân bằng hơi–lỏng trong hỗn hợp không lý tưởng.

### “Nhiệt động lực học cho biết cơ chế phản ứng”

Không. Nó cho lực dẫn động và trạng thái cân bằng; cơ chế thuộc động học và cấu trúc điện tử.

### “Gradient nồng độ luôn đủ để dự đoán hướng vận chuyển”

Không trong mọi hệ. Lực dẫn động tổng quát là gradient thế hóa học hoặc thế điện hóa; tính không lý tưởng có thể làm mô tả chỉ dựa trên nồng độ thiếu thông tin.

## Mô hình tư duy

Thế hóa học là **đồng tiền chung** của nhiệt động lực học hóa học:

```text
thành phần / áp suất / tương tác / điện trường
→ μi hoặc μ̃i
→ chênh lệch tạo lực dẫn động
→ vật chất, pha hoặc phản ứng thay đổi
→ các thế thích hợp bằng nhau tại cân bằng
```

Từ cùng framework này có thể hiểu tính không lý tưởng của dung dịch, cân bằng pha, thẩm thấu, điện hóa, khuếch tán và cân bằng phản ứng mà không cần học chúng như các định luật hoàn toàn tách biệt.

Xem tiếp: [Tốc độ phản ứng](../06_chemical_kinetics/00_reaction_rates.md) để chuyển từ “hướng có lợi về nhiệt động” sang “nhanh tới đâu”, và [Nhiệt động lực học của cân bằng](../07_chemical_equilibrium/04_thermodynamics_of_equilibrium.md) để dùng thế hóa học trong bài toán cân bằng phản ứng/pha.