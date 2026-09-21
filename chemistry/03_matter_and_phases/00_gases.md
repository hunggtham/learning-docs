# Chất khí — từ chuyển động phân tử tới khí thực

> **Chất khí (gas / 기체)** là trạng thái vật chất trong đó khoảng cách trung bình giữa các hạt thường lớn hơn nhiều kích thước riêng của chúng và các hạt chuyển động liên tục trong không gian. Vì vậy khí dễ nén, nhanh chóng lấp đầy bình chứa và thể hiện rất rõ mối liên hệ giữa chuyển động vi mô với các đại lượng vĩ mô như áp suất, nhiệt độ và thể tích.

Chương này bắt đầu từ mô hình khí lý tưởng để xây trực giác, sau đó mở rộng sang phân bố vận tốc, va chạm phân tử, khí hỗn hợp, khuếch tán và cuối cùng là khí thực. Mục tiêu không phải học thuộc nhiều công thức khí, mà hiểu chúng là các lớp mô hình có phạm vi áp dụng khác nhau.

## Từ hiện tượng vĩ mô tới mô hình vi mô

Nếu ép piston của một ống tiêm kín, thể tích giảm và áp suất tăng. Nếu đun nóng một quả bóng mềm, thể tích thường tăng. Nếu mở một lọ chất có mùi trong phòng, các phân tử khí dần phân tán ra xa nguồn.

Ba quan sát này có cùng gốc vi mô: các hạt khí chuyển động liên tục, va chạm với nhau và với thành bình.

**Áp suất (pressure / 압력)** ở cấp vĩ mô được định nghĩa:

\[
P=\frac{F}{A}
\]

Ở cấp vi mô, lực trung bình lên thành bình xuất hiện vì phân tử thay đổi động lượng khi va chạm. Một va chạm riêng lẻ rất nhỏ, nhưng số va chạm khổng lồ tạo ra áp suất ổn định ở thang quan sát.

Đây là một ví dụ quan trọng về **tính chất nổi lên (emergent property)**: áp suất không phải thuộc tính của một phân tử đơn lẻ, mà là kết quả thống kê của cả tập hợp hạt.

## Bốn biến trạng thái cơ bản

Một mẫu khí đơn giản thường được mô tả bằng:

- áp suất \(P\);
- thể tích \(V\);
- nhiệt độ tuyệt đối \(T\);
- lượng chất \(n\).

Các biến này liên hệ bởi **phương trình khí lý tưởng (ideal gas law / 이상 기체 방정식)**:

\[
PV=nRT
\]

Trong đó \(R\) là hằng số khí.

Trong hệ SI:

\[
R=8.314\;\mathrm{J\,mol^{-1}\,K^{-1}}
\]

Nếu dùng `L·atm`:

\[
R=0.082057\;\mathrm{L\,atm\,mol^{-1}\,K^{-1}}
\]

Điều quan trọng là phải dùng **nhiệt độ tuyệt đối theo Kelvin**, vì tỉ lệ trong mô hình khí liên quan tới năng lượng nhiệt tuyệt đối chứ không phải mốc tùy ý của thang Celsius.

## Boyle, Charles và Avogadro là các lát cắt của cùng một quan hệ

Nếu giữ \(n\) và \(T\) không đổi:

\[
PV=\text{hằng số}
\]

nên:

\[
P\propto \frac{1}{V}
\]

Đây là **định luật Boyle (Boyle's law)**. Nén khí làm mật độ phân tử tăng, do đó số lần phân tử va vào thành bình trên mỗi đơn vị thời gian tăng.

Nếu giữ \(P\) và \(n\) không đổi:

\[
V\propto T
\]

Đây là **định luật Charles (Charles's law)**. Khi nhiệt độ tăng, chuyển động phân tử mạnh hơn; để áp suất không tăng, hệ cần giãn nở.

Nếu giữ \(P\) và \(T\) không đổi:

\[
V\propto n
\]

Đây là **định luật Avogadro (Avogadro's law)**. Thêm hạt vào hệ ở cùng áp suất và nhiệt độ đòi hỏi thể tích tăng.

Ba định luật không phải ba quy tắc rời. Chúng là ba trường hợp giới hạn của \(PV=nRT\).

## Khối lượng riêng và khối lượng mol của khí

Từ:

\[
PV=nRT
\]

và:

\[
n=\frac{m}{M}
\]

suy ra:

\[
P V=\frac{m}{M}RT
\]

Với khối lượng riêng:

\[
\rho=\frac{m}{V}
\]

có:

\[
\boxed{\rho=\frac{PM}{RT}}
\]

Do đó, ở cùng nhiệt độ và áp suất, khí có khối lượng mol lớn hơn thường có khối lượng riêng lớn hơn.

Ngược lại, nếu đo được \(P,\rho,T\), có thể ước lượng khối lượng mol:

\[
M=\frac{\rho RT}{P}
\]

Đây là một ví dụ cho thấy phương trình khí có thể được dùng như công cụ suy ngược từ phép đo vĩ mô về thông tin phân tử.

## Thuyết động học phân tử

**Thuyết động học phân tử (kinetic molecular theory / 기체 분자 운동론)** giải thích vì sao phương trình khí lý tưởng xuất hiện.

Mô hình giả định:

1. kích thước riêng của phân tử rất nhỏ so với thể tích bình;
2. ngoài thời điểm va chạm, tương tác hút/đẩy giữa các phân tử có thể bỏ qua;
3. phân tử chuyển động liên tục và ngẫu nhiên;
4. va chạm là đàn hồi;
5. năng lượng động học tịnh tiến trung bình chỉ phụ thuộc nhiệt độ tuyệt đối.

Từ cơ học thống kê có thể thu được:

\[
\langle E_k\rangle=\frac{3}{2}k_BT
\]

cho một phân tử, hoặc:

\[
\langle E_k\rangle_{mol}=\frac{3}{2}RT
\]

cho một mol khí đơn nguyên tử lý tưởng xét phần tịnh tiến.

Ở cùng nhiệt độ, các loại khí có cùng **năng lượng động học tịnh tiến trung bình**, nhưng không có cùng vận tốc đặc trưng.

## Phân bố Maxwell–Boltzmann

Trong một mẫu khí ở nhiệt độ cố định, các phân tử không chạy cùng một tốc độ. Chúng liên tục va chạm và trao đổi năng lượng, tạo một **phân bố vận tốc Maxwell–Boltzmann (Maxwell–Boltzmann speed distribution)**.

Ba vận tốc thường gặp là:

- vận tốc có xác suất lớn nhất \(u_{mp}\);
- vận tốc trung bình \(\bar u\);
- vận tốc căn phương bình phương trung bình \(u_{rms}\).

Với khí lý tưởng:

\[
u_{mp}=\sqrt{\frac{2RT}{M}}
\]

\[
\bar u=\sqrt{\frac{8RT}{\pi M}}
\]

\[
u_{rms}=\sqrt{\frac{3RT}{M}}
\]

và:

\[
u_{mp}<\bar u<u_{rms}
\]

Khi nhiệt độ tăng, phân bố rộng hơn và dịch về vận tốc cao hơn. Khi khối lượng mol tăng, phân bố dịch về vận tốc thấp hơn.

Điều này rất quan trọng trong động học phản ứng: tăng nhiệt độ không chỉ tăng vận tốc trung bình mà còn tăng mạnh phần phân tử nằm ở vùng năng lượng cao của phân bố, nơi có khả năng vượt hàng rào hoạt hóa.

Xem thêm: [Năng lượng hoạt hóa và Arrhenius](../06_chemical_kinetics/03_activation_energy_and_arrhenius.md).

## Từ va chạm tới áp suất

Một kết quả của thuyết động học là:

\[
P=\frac{1}{3}\rho_m\langle u^2\rangle
\]

trong đó \(\rho_m\) là mật độ khối lượng của khí.

Quan hệ này cho thấy áp suất phụ thuộc trực tiếp vào mật độ vật chất và bình phương vận tốc đặc trưng của phân tử.

Nó cũng giải thích vì sao cùng một lượng khí trong thể tích cố định có áp suất tăng khi nhiệt độ tăng: phân tử chuyển động nhanh hơn và truyền động lượng mạnh hơn lên thành bình.

## Tần suất va chạm và quãng đường tự do trung bình

Một phân tử khí không bay mãi theo đường thẳng. Nó di chuyển một khoảng rồi va chạm và đổi hướng.

**Quãng đường tự do trung bình (mean free path, \(\lambda\))** là khoảng cách trung bình giữa hai va chạm liên tiếp.

Trong mô hình quả cầu cứng đơn giản:

\[
\lambda\approx\frac{k_BT}{\sqrt{2}\pi d^2P}
\]

với \(d\) là đường kính va chạm hiệu dụng.

Từ biểu thức này có thể suy luận:

- tăng áp suất → \(\lambda\) giảm;
- tăng nhiệt độ ở áp suất cố định → \(\lambda\) tăng;
- phân tử có tiết diện va chạm lớn → \(\lambda\) giảm.

Khái niệm này quan trọng trong chân không, khí quyển tầng cao, microfluidics và kỹ thuật chân không.

Khi kích thước thiết bị gần với quãng đường tự do trung bình, giả định môi trường liên tục của cơ học chất lưu bắt đầu suy yếu.

## Khuếch tán không đơn giản là phân tử bay thẳng từ nơi cao tới nơi thấp

**Khuếch tán (diffusion / 확산)** xuất hiện từ chuyển động nhiệt ngẫu nhiên. Ở cấp từng phân tử, quỹ đạo là một chuỗi ngẫu nhiên của nhiều va chạm; ở cấp tập thể, dòng ròng xuất hiện theo gradient nồng độ.

Định luật Fick mô tả gần đúng:

\[
J=-D\nabla c
\]

Dấu âm cho biết dòng khuếch tán ròng đi từ vùng nồng độ cao tới vùng nồng độ thấp.

Hệ số khuếch tán khí thường lớn hơn trong chất lỏng vì các phân tử khí có độ linh động cao hơn và môi trường ít đặc hơn.

Khuếch tán là cầu nối trực tiếp từ vật lý khí sang vận chuyển khối trong động học, điện hóa và kỹ thuật phản ứng.

## Thoát khí qua lỗ nhỏ và định luật Graham

**Thoát khí qua lỗ nhỏ (effusion / 분출)** là quá trình phân tử đi qua một lỗ đủ nhỏ để va chạm tại lỗ ít quan trọng hơn chuyển động nhiệt của từng phân tử.

Tốc độ thoát gần tỉ lệ nghịch với căn bậc hai khối lượng mol:

\[
\frac{r_1}{r_2}=\sqrt{\frac{M_2}{M_1}}
\]

Khí nhẹ thoát nhanh hơn vì có vận tốc nhiệt đặc trưng cao hơn.

Không nên dùng định luật Graham cho mọi bài toán dòng khí qua ống hoặc lỗ lớn; khi nhiều va chạm tập thể và chênh áp đáng kể xuất hiện, cơ học dòng chảy mới là mô hình phù hợp hơn.

## Hỗn hợp khí và áp suất riêng phần

Trong hỗn hợp khí lý tưởng:

\[
P_{total}=\sum_i P_i
\]

Đây là **định luật Dalton (Dalton's law)**.

Với phần mol:

\[
x_i=\frac{n_i}{n_{total}}
\]

thì:

\[
P_i=x_iP_{total}
\]

Áp suất riêng phần quan trọng hơn phần trăm thể tích trong nhiều bài toán hóa học vì thế hóa học và cân bằng khí phụ thuộc trực tiếp vào áp suất riêng phần hoặc fugacity.

Ví dụ trong hô hấp, không chỉ phần trăm oxygen quan trọng; áp suất khí quyển tổng cũng quyết định áp suất riêng phần oxygen.

Ở độ cao lớn, phần mol oxygen vẫn gần như không đổi nhưng áp suất khí quyển giảm, nên áp suất riêng phần oxygen giảm.

## Khí thu trên nước

Nếu khí được thu bằng cách đẩy nước, hỗn hợp phía trên mặt nước chứa cả khí cần đo và hơi nước.

Theo Dalton:

\[
P_{total}=P_{gas}+P_{H_2O}
\]

Do đó:

\[
P_{gas}=P_{total}-P_{H_2O}
\]

Đây là ví dụ thực nghiệm quan trọng cho thấy áp suất riêng phần không phải khái niệm trừu tượng: nếu quên hơi nước, số mol khí tính được sẽ bị sai.

## Khí trong phản ứng hóa lượng

Với khí gần lý tưởng:

\[
n=\frac{PV}{RT}
\]

nên có thể chuyển:

```text
P, V, T
→ mol khí
→ hệ số phản ứng
→ mol chất khác
```

Điều này nối trực tiếp chương khí với [Mol và hằng số Avogadro](../04_chemical_quantities/00_mole_and_avogadro_constant.md) và [Hóa lượng](../04_chemical_quantities/03_stoichiometry.md).

Không nên sử dụng một “thể tích mol chuẩn” duy nhất nếu đề bài không nói rõ điều kiện nhiệt độ và áp suất. Thể tích mol của khí phụ thuộc điều kiện trạng thái.

## Vì sao khí thật lệch khỏi mô hình lý tưởng?

Mô hình lý tưởng bỏ qua hai hiệu ứng:

1. phân tử có kích thước hữu hạn;
2. phân tử có lực hút và lực đẩy.

Ở áp suất thấp và nhiệt độ đủ cao, khoảng cách giữa các phân tử lớn nên hai hiệu ứng này thường nhỏ.

Khi nén mạnh, thể tích riêng của phân tử không còn bỏ qua được. Khi hạ nhiệt độ, năng lượng nhiệt giảm và lực hút liên phân tử trở nên quan trọng hơn.

Vì vậy khí thật lệch mạnh nhất khỏi lý tưởng ở **áp suất cao** và **nhiệt độ thấp**, đặc biệt gần vùng ngưng tụ.

## Hệ số nén

Mức lệch khỏi khí lý tưởng thường được biểu diễn bằng **hệ số nén (compressibility factor, \(Z\))**:

\[
Z=\frac{PV}{nRT}
\]

Với khí lý tưởng:

\[
Z=1
\]

Nếu \(Z<1\), lực hút giữa phân tử thường đang làm khí dễ nén hơn mô hình lý tưởng.

Nếu \(Z>1\), hiệu ứng thể tích loại trừ và lực đẩy khoảng cách ngắn thường chi phối.

Không nên hiểu \(Z<1\) là “khí có áp suất âm” hay \(Z>1\) là “phân tử phình to”. Nó chỉ biểu diễn mức sai lệch của quan hệ \(PV=nRT\).

## Phương trình van der Waals

Một mô hình khí thực cổ điển là:

\[
\left(P+a\frac{n^2}{V^2}\right)(V-nb)=nRT
\]

Trong đó:

- \(a\) hiệu chỉnh lực hút;
- \(b\) hiệu chỉnh thể tích bị loại trừ.

Phần hiệu chỉnh áp suất phản ánh rằng lực hút làm phân tử tới thành bình với động lượng hiệu dụng thấp hơn so với khí lý tưởng.

Phần \(V-nb\) phản ánh rằng không phải toàn bộ thể tích hình học đều khả dụng cho tâm phân tử.

Van der Waals có giá trị lớn về mặt khái niệm nhưng không phải phương trình chính xác cho mọi khí và mọi điều kiện.

## Khai triển virial

Một cách tổng quát hơn mô tả khí thật là **phương trình virial (virial equation)**:

\[
Z=1+B(T)\frac{n}{V}+C(T)\left(\frac{n}{V}\right)^2+\cdots
\]

Các hệ số virial chứa thông tin hiệu dụng về tương tác hai hạt, ba hạt và các hiệu ứng tập thể cao hơn.

Ở mật độ thấp, chỉ cần vài hạng đầu có thể đủ tốt.

Điểm quan trọng là mô hình khí thật có thể được xem như mở rộng có hệ thống quanh giới hạn khí lý tưởng.

## Nhiệt độ Boyle

Tại một nhiệt độ đặc biệt gọi là **nhiệt độ Boyle (Boyle temperature)**, hệ số virial bậc hai gần bằng 0. Khi đó, trong vùng áp suất thấp, lực hút và hiệu ứng thể tích loại trừ có thể gần triệt tiêu nhau nên khí hành xử gần lý tưởng hơn.

Điều này nhắc rằng “tính lý tưởng” không phải thuộc tính tuyệt đối của một chất; nó phụ thuộc điều kiện nhiệt độ và áp suất.

## Điểm tới hạn và sự thất bại của ranh giới khí–lỏng

Khi khí được nén và làm lạnh, nó có thể ngưng tụ thành lỏng. Đường cân bằng lỏng–hơi kết thúc tại **điểm tới hạn (critical point)**.

Trên nhiệt độ tới hạn, không thể hóa lỏng khí chỉ bằng cách tăng áp suất theo con đường đẳng nhiệt thông thường; hệ đi vào vùng chất lưu siêu tới hạn.

Gần điểm tới hạn, dao động mật độ trở nên lớn và các mô hình đơn giản như khí lý tưởng hoặc van der Waals có thể sai đáng kể về định lượng.

Phần này nối trực tiếp với [Chuyển pha và giản đồ pha](./03_phase_changes_and_phase_diagrams.md).

## Fugacity — “áp suất hiệu dụng” trong nhiệt động khí thực

Trong nhiệt động lực học, khí lý tưởng dùng áp suất riêng phần trong thế hóa học:

\[
\mu_i=\mu_i^\circ+RT\ln\frac{P_i}{P^\circ}
\]

Với khí thật, người ta thay áp suất bằng **fugacity (độ thoát, fugacity)**:

\[
\mu_i=\mu_i^\circ+RT\ln\frac{f_i}{f^\circ}
\]

Trong giới hạn áp suất thấp:

\[
f_i\rightarrow P_i
\]

Fugacity không cần được hiểu như một “áp suất mới” đo trực tiếp bằng đồng hồ. Nó là đại lượng nhiệt động giúp biểu diễn thế hóa học của khí thật bằng cấu trúc toán học tương tự khí lý tưởng.

Xem thêm: [Nhiệt động lực học hóa học](../05_thermodynamics/04_chemical_thermodynamics.md).

## Hiệu ứng Joule–Thomson và làm lạnh khí

Khi một khí thật giãn qua van tiết lưu trong quá trình gần như không đổi enthalpy, nhiệt độ có thể thay đổi. Đây là **hiệu ứng Joule–Thomson (Joule–Thomson effect)**.

Khí lý tưởng lý tưởng hóa không có hiệu ứng này vì enthalpy chỉ phụ thuộc nhiệt độ. Với khí thật, tương tác phân tử làm enthalpy phụ thuộc thêm vào mật độ và áp suất.

Tùy nhiệt độ ban đầu, một khí có thể lạnh đi hoặc nóng lên khi tiết lưu. Hiệu ứng này là nền của nhiều chu trình hóa lỏng và làm lạnh khí.

## Khí quyển là một hỗn hợp khí chịu cả nhiệt động và trọng lực

Khí quyển không có áp suất đồng đều theo độ cao. Trọng lực làm mật độ và áp suất giảm khi đi lên.

Trong mô hình đơn giản đẳng nhiệt, áp suất giảm gần theo hàm mũ:

\[
P(z)=P_0\exp\left(-\frac{Mgz}{RT}\right)
\]

Quan hệ này kết hợp:

- phương trình khí lý tưởng;
- cân bằng thủy tĩnh;
- trọng lực.

Khí quyển thực phức tạp hơn vì nhiệt độ thay đổi theo độ cao, độ ẩm, đối lưu và phản ứng quang hóa, nhưng mô hình đơn giản cho thấy cách hóa học khí nối với vật lý khí quyển.

Xem thêm: [Hóa học khí quyển](../16_environmental_chemistry/00_atmospheric_chemistry.md).

## Liên hệ với động học phản ứng

Động học khí phụ thuộc trực tiếp vào mật độ va chạm và phân bố năng lượng.

Nhưng không phải mọi va chạm đều gây phản ứng. Ngoài năng lượng đủ lớn, cấu hình va chạm và bề mặt thế năng cũng quan trọng.

Do đó chuỗi reasoning là:

```text
nhiệt độ
→ phân bố vận tốc/năng lượng
→ tần suất và năng lượng va chạm
→ xác suất vượt hàng rào hoạt hóa
→ tốc độ phản ứng
```

Đây là cầu nối tự nhiên sang [Động học hóa học](../06_chemical_kinetics/00_reaction_rates.md).

## Liên hệ với kỹ thuật chân không và điện tử

Trong buồng chân không của chế tạo bán dẫn, áp suất thấp làm quãng đường tự do trung bình tăng mạnh. Khi đó hạt có thể đi xa trước khi va chạm, điều này ảnh hưởng lắng đọng hơi vật lý, plasma, sputtering và vận chuyển precursor.

Vì vậy hiểu khí không chỉ phục vụ bài toán bình kín; nó còn là nền cho công nghệ chân không và chế tạo vật liệu điện tử.

## Ví dụ suy luận tổng hợp

Giả sử hai bình có cùng thể tích và cùng nhiệt độ. Bình A chứa `He`, bình B chứa `N2`, và hai bình có cùng áp suất.

Từ khí lý tưởng:

\[
n_A=n_B
\]

vì \(P,V,T\) giống nhau.

Nhưng:

\[
M_{He}<M_{N_2}
\]

nên He có vận tốc nhiệt đặc trưng lớn hơn:

\[
u_{rms,He}>u_{rms,N_2}
\]

Trong khi đó năng lượng động học tịnh tiến trung bình của hai khí lại bằng nhau vì nhiệt độ giống nhau.

Đây là ví dụ cho thấy phải phân biệt:

```text
năng lượng động học trung bình
≠ vận tốc trung bình
```

## Giới hạn của các mô hình trong chương

Không có một phương trình khí đơn giản nào đúng tuyệt đối cho mọi trạng thái.

- `PV=nRT` tốt ở mật độ thấp;
- van der Waals cho trực giác về lực hút và thể tích loại trừ;
- virial hữu ích để mô tả sai lệch có hệ thống ở mật độ không quá cao;
- gần điểm tới hạn hoặc trong điều kiện công nghiệp chính xác cao cần phương trình trạng thái tiên tiến hơn và dữ liệu thực nghiệm.

Một mô hình tốt không phải mô hình phức tạp nhất, mà là mô hình đơn giản nhất vẫn giữ sai số phù hợp với mục tiêu.

## Những hiểu lầm thường gặp

### “Nhiệt độ là tốc độ của phân tử”

Không. Nhiệt độ liên hệ với phân bố năng lượng và năng lượng động học trung bình, không phải một vận tốc duy nhất.

### “Các phân tử khí không có lực hút”

Chỉ khí lý tưởng giả định có thể bỏ qua tương tác. Khí thật luôn có lực liên phân tử.

### “Nếu thể tích khí tăng thì phân tử tự lớn lên”

Không. Khoảng cách trung bình giữa các phân tử tăng; kích thước từng phân tử gần như không đổi.

### “Khí nhẹ có nhiều năng lượng hơn vì chạy nhanh hơn”

Sai nếu hai khí ở cùng nhiệt độ. Chúng có cùng năng lượng động học tịnh tiến trung bình; khí nhẹ chạy nhanh hơn vì khối lượng nhỏ hơn.

### “Z khác 1 nghĩa phương trình khí lý tưởng hoàn toàn vô dụng”

Không. `Z` cho biết mức sai lệch. Nếu `Z` đủ gần 1 so với độ chính xác cần thiết, khí lý tưởng vẫn là mô hình rất hữu ích.

### “Áp suất riêng phần chỉ là phần trăm thể tích”

Trong hỗn hợp lý tưởng có liên hệ đơn giản với phần mol, nhưng ý nghĩa nhiệt động sâu hơn là đóng góp của từng cấu tử vào trạng thái hỗn hợp.

## Mô hình tư duy

Hãy đọc chất khí theo bốn lớp:

```text
chuyển động phân tử
→ va chạm và phân bố thống kê
→ P, V, T, n ở cấp vĩ mô
→ hiệu chỉnh tương tác khi khí trở nên không lý tưởng
```

Khí lý tưởng là giới hạn nền rất mạnh. Khí thực xuất hiện khi kích thước phân tử, lực tương tác và dao động mật độ không còn có thể bỏ qua.

Từ đây có thể chuyển sang [Chất lỏng](./01_liquids.md), nơi các hạt ở gần nhau đến mức tương tác liên phân tử trở thành yếu tố trung tâm.