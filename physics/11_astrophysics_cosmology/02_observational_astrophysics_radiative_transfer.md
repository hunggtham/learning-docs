# Vật lý thiên văn quan sát và truyền bức xạ: từ photon tới suy luận vật lý

Vật lý thiên văn khác nhiều nhánh Vật lý trong phòng thí nghiệm ở một điểm cơ bản: ta thường không thể trực tiếp điều khiển hệ đang nghiên cứu. Ta không thể thay đổi nhiệt độ của một ngôi sao rồi đo lại, cũng không thể đặt một thiên hà vào thiết bị thử nghiệm khác.

Thay vào đó, ta nhận tín hiệu từ xa rồi giải bài toán ngược:

```text
nguồn vật lý
→ bức xạ được phát ra
→ truyền qua môi trường
→ kính thiên văn và detector
→ dữ liệu
→ mô hình suy luận
→ tham số vật lý của nguồn
```

Vì vậy để hiểu thiên văn học ở mức vật lý, cần hiểu không chỉ sao và thiên hà hoạt động thế nào mà còn **bức xạ mang thông tin thế nào, bị biến đổi ra sao và độ bất định của suy luận xuất hiện ở đâu**.

## Cường độ riêng và thông lượng

Một nguồn không chỉ có “độ sáng”. Bức xạ còn phụ thuộc hướng, tần số và vị trí.

Một đại lượng cơ bản là **cường độ riêng (specific intensity)** `I_\nu`, có thể hiểu là năng lượng truyền qua một diện tích, trong một khoảng thời gian, theo một khoảng tần số và một góc khối xác định.

Thông lượng phổ là

```math
F_\nu
=
\int I_\nu\cos\theta\,d\Omega.
```

Với nguồn đẳng hướng có độ sáng phổ `L_\nu`, ở khoảng cách `d` trong không gian Euclid gần đúng,

```math
F_\nu
=
\frac{L_\nu}{4\pi d^2}.
```

Quy luật nghịch đảo bình phương xuất hiện vì cùng một công suất bị trải trên mặt cầu diện tích `4\pi d^2`.

## Vì sao cường độ riêng quan trọng?

Một tính chất hữu ích là trong chân không không hấp thụ và không phát xạ, `I_\nu` dọc một tia được bảo toàn trong mô tả cổ điển thích hợp.

Điều này khác thông lượng tổng, vốn thay đổi với khoảng cách do góc khối mà nguồn chiếm trên bầu trời thay đổi.

Phân biệt intensity, flux và luminosity giúp tránh nhiều nhầm lẫn khi chuyển từ “tín hiệu detector đo được” sang “công suất thật của nguồn”.

## Phương trình truyền bức xạ

Khi bức xạ đi qua vật chất, hai quá trình cơ bản xảy ra:

- hấp thụ làm giảm cường độ;
- phát xạ thêm photon vào tia.

Phương trình truyền bức xạ (radiative transfer equation / 복사 전달 방정식) có dạng

```math
\frac{dI_\nu}{ds}
=
-j_{abs}+j_{emit},
```

thường viết chính xác hơn là

```math
\frac{dI_\nu}{ds}
=
-\alpha_\nu I_\nu+j_\nu,
```

trong đó `\alpha_\nu` là hệ số hấp thụ và `j_\nu` là hệ số phát xạ.

Định nghĩa **source function**

```math
S_\nu=\frac{j_\nu}{\alpha_\nu}
```

cho phép viết

```math
\frac{dI_\nu}{d\tau_\nu}
=
-I_\nu+S_\nu,
```

với độ sâu quang học

```math
d\tau_\nu=\alpha_\nu ds.
```

## Độ sâu quang học

Nếu

```math
\tau_\nu\ll1,
```

môi trường **quang học mỏng (optically thin)**: phần lớn photon đi qua mà không bị hấp thụ.

Nếu

```math
\tau_\nu\gg1,
```

môi trường **quang học dày (optically thick)**: bức xạ quan sát chủ yếu xuất phát từ lớp gần nơi `\tau_\nu\sim1`.

Đây là lý do “bề mặt” của một ngôi sao trong quan sát không nhất thiết là một ranh giới vật chất sắc nét. Photosphere gần đúng là lớp mà photon có xác suất thoát ra đáng kể.

## Nghiệm cho môi trường đồng nhất

Nếu `S_\nu` không đổi dọc đường đi,

```math
I_\nu(\tau)
=
I_\nu(0)e^{-\tau}
+
S_\nu(1-e^{-\tau}).
```

Công thức này chứa hai giới hạn quan trọng.

Nếu `\tau\ll1`,

```math
I_\nu
\approx
I_\nu(0)(1-\tau)+S_\nu\tau.
```

Nếu `\tau\gg1`,

```math
I_\nu\rightarrow S_\nu.
```

Ở môi trường cân bằng nhiệt cục bộ, source function tiến gần hàm Planck, nên vật quang học dày có phổ gần vật đen.

## Vật đen và định luật Planck

Phổ vật đen được mô tả bởi

```math
B_\nu(T)
=
\frac{2h\nu^3}{c^2}
\frac{1}{e^{h\nu/k_BT}-1}.
```

Hai giới hạn của công thức rất hữu ích.

Khi

```math
h\nu\ll k_BT,
```

ta có giới hạn Rayleigh–Jeans

```math
B_\nu\approx\frac{2\nu^2k_BT}{c^2}.
```

Khi

```math
h\nu\gg k_BT,
```

phổ giảm xấp xỉ theo hàm mũ Wien.

Định luật Stefan–Boltzmann

```math
F=\sigma T^4
```

thu được khi tích phân phổ vật đen trên toàn bộ tần số và góc.

## Vạch phổ hình thành thế nào?

Một vạch hấp thụ xuất hiện khi lớp vật chất tương đối lạnh nằm trước nguồn continuum nóng hơn và hấp thụ photon ở các tần số chuyển mức đặc trưng.

Vạch phát xạ có thể xuất hiện khi khí loãng được kích thích rồi phát photon khi chuyển về mức thấp hơn.

Độ mạnh vạch không chỉ phụ thuộc “có nguyên tố đó hay không”. Nó còn phụ thuộc:

- nhiệt độ và phân bố mức năng lượng;
- trạng thái ion hóa;
- mật độ;
- độ sâu quang học;
- vận tốc vi mô và vĩ mô;
- hình học nguồn.

Do đó suy ra thành phần hóa học từ phổ là bài toán vật lý thống kê và truyền bức xạ, không phải chỉ khớp một danh sách bước sóng.

## Doppler và vận tốc đường ngắm

Ở vận tốc nhỏ so với `c`, dịch Doppler gần đúng là

```math
\frac{\Delta\lambda}{\lambda_0}
\approx
\frac{v_r}{c}.
```

`v_r` là thành phần vận tốc theo đường ngắm.

Do chỉ đo thành phần đường ngắm, spectroscopy không tự cho toàn bộ vectơ vận tốc ba chiều.

Khi vận tốc relativistic, phải dùng công thức Doppler tương đối tính đầy đủ.

## Độ rộng vạch

Vạch quang phổ không có độ rộng bằng không.

Chuyển động nhiệt tạo Doppler broadening với độ rộng đặc trưng tăng gần theo

```math
\Delta v_{thermal}
\sim
\sqrt{\frac{k_BT}{m}}.
```

Các cơ chế khác gồm:

- natural broadening do thời gian sống hữu hạn;
- pressure broadening do va chạm;
- rotational broadening do sao quay;
- turbulent broadening do vận tốc ngẫu nhiên quy mô lớn hơn nhiệt.

Việc tách các cơ chế này là một bài toán suy luận mô hình.

## Độ phân giải phổ

Khả năng phân biệt hai bước sóng gần nhau thường mô tả bằng

```math
R=\frac{\lambda}{\Delta\lambda}.
```

Nếu `R` quá thấp, các vạch gần nhau hòa trộn và thông tin vận tốc hoặc thành phần bị mất.

Tăng độ phân giải không phải miễn phí: photon bị phân chia vào nhiều bin phổ hơn, có thể làm SNR trên mỗi bin giảm nếu tổng photon không đổi.

Đây là một ví dụ rõ của đánh đổi giữa độ phân giải và độ nhạy.

## Magnitude và thang logarit

Thiên văn học truyền thống dùng độ sáng biểu kiến dạng magnitude:

```math
m_1-m_2
=
-2.5\log_{10}
\left(
\frac{F_1}{F_2}
\right).
```

Vì thang đảo chiều, vật sáng hơn có magnitude nhỏ hơn.

Magnitude tuyệt đối thường được định nghĩa là magnitude mà vật sẽ có nếu đặt ở khoảng cách chuẩn 10 parsec.

Quan hệ distance modulus gần đúng là

```math
m-M
=
5\log_{10}\left(\frac d{10\,pc}\right)
```

khi bỏ qua extinction và các hiệu chỉnh khác.

## Extinction và reddening

Bụi liên sao hấp thụ và tán xạ ánh sáng, thường mạnh hơn ở bước sóng ngắn, làm nguồn trông mờ và đỏ hơn.

Nếu không hiệu chỉnh extinction, ta có thể suy ra sai nhiệt độ, độ sáng và khoảng cách.

Đây là ví dụ điển hình của một **nuisance parameter**: đại lượng không phải mục tiêu chính nhưng nếu bỏ qua sẽ làm tham số quan tâm bị lệch.

## Kính thiên văn đo gì?

Kính thiên văn không đơn giản “phóng to vật thể”. Chức năng cơ bản là thu photon trên diện tích lớn và tạo phân bố ánh sáng trên detector.

Đường kính khẩu độ `D` ảnh hưởng hai yếu tố chính:

- lượng photon thu được tỉ lệ gần với `D^2`;
- giới hạn nhiễu xạ góc gần

```math
\theta\sim1.22\frac\lambda D.
```

Do đó kính lớn vừa nhạy hơn vừa có tiềm năng phân giải tốt hơn.

Tuy nhiên từ mặt đất, seeing khí quyển thường làm ảnh mờ hơn giới hạn nhiễu xạ nếu không dùng adaptive optics.

## CCD và photon counting

Detector chuyển photon thành electron hoặc tín hiệu điện tử. Một phép đo ảnh thường chịu nhiều nguồn nhiễu:

- photon shot noise;
- dark current;
- read noise;
- background sky;
- flat-field error;
- cosmic rays;
- calibration uncertainty.

Nếu số photon nguồn là `N`, shot noise lý tưởng có độ lệch chuẩn gần

```math
\sigma\sim\sqrt N.
```

nên SNR photon-limited tăng gần

```math
\mathrm{SNR}\sim\sqrt N.
```

Vì vậy muốn tăng SNR gấp đôi thường cần xấp xỉ gấp bốn số photon.

## Tích phân lâu hơn không giải quyết mọi vấn đề

Tăng exposure giúp khi noise ngẫu nhiên chi phối. Nhưng nó không tự sửa:

- saturation;
- cosmic-ray contamination;
- systematic calibration error;
- background modelling sai;
- source variability;
- tracking error.

Giống mọi thí nghiệm, nhiều dữ liệu không tự động loại sai số hệ thống.

## Parallax và khoảng cách hình học

Nếu quan sát một sao từ hai vị trí khác nhau trên quỹ đạo Trái Đất, vị trí biểu kiến của nó thay đổi so với nền xa.

Với góc parallax `p` tính bằng arcsecond,

```math
d(\mathrm{pc})=\frac1{p(\mathrm{arcsec})}.
```

Đây là phương pháp hình học trực tiếp nhưng độ chính xác giảm khi nguồn quá xa vì góc quá nhỏ.

## Thang khoảng cách

Không có một phương pháp duy nhất đo tốt mọi khoảng cách vũ trụ. Thiên văn học dùng một **thang khoảng cách (distance ladder)**:

```text
parallax
→ standard candles cục bộ
→ Cepheid / RR Lyrae
→ Type Ia supernovae
→ cosmological distance indicators
```

Mỗi bậc được hiệu chuẩn dựa trên bậc gần hơn. Vì vậy sai số hiệu chuẩn có thể lan truyền lên các khoảng cách rất lớn.

## Redshift vũ trụ học

Redshift được định nghĩa

```math
1+z
=
\frac{\lambda_{obs}}{\lambda_{emit}}.
```

Ở vận tốc nhỏ trong không gian phẳng, redshift có thể gần Doppler. Nhưng ở vũ trụ học, redshift lớn được hiểu đúng hơn từ sự giãn nở của metric không-thời gian.

Do đó không nên luôn diễn giải `z` như “thiên hà bay xuyên không gian với vận tốc `cz`”. Xấp xỉ

```math
v\approx cz
```

chỉ hữu ích ở redshift nhỏ.

## K-correction và bandpass

Khi nguồn ở redshift lớn, cùng một filter quan sát tương ứng với vùng bước sóng khác trong hệ nghỉ của nguồn.

Do đó so sánh luminosity giữa các nguồn ở redshift khác nhau cần hiệu chỉnh phổ và bandpass, thường gọi là **K-correction**.

Đây là một ví dụ cho thấy dữ liệu detector không thể được diễn giải tách rời mô hình spectral energy distribution của nguồn.

## Selection effect

Một survey giới hạn thông lượng sẽ dễ phát hiện vật sáng hơn ở khoảng cách lớn. Vì vậy mẫu quan sát không phải một mẫu ngẫu nhiên đơn giản của toàn bộ quần thể.

Nếu không mô hình selection function, ta có thể suy ra sai phân bố luminosity, khối lượng hoặc tốc độ tiến hóa của quần thể.

Đây là vấn đề chung của khoa học dữ liệu: quá trình thu thập dữ liệu là một phần của mô hình xác suất.

## Bài toán ngược trong thiên văn

Dữ liệu `D` được tạo từ tham số vật lý `\theta` thông qua một mô hình thuận:

```text
θ
→ mô hình vật lý
→ spectrum/image/light curve dự đoán
→ instrument response
→ dữ liệu dự đoán
```

Bài toán thực nghiệm đi ngược:

```text
dữ liệu
→ suy ra phân bố khả dĩ của θ
```

Theo Bayes,

```math
P(\theta|D)
\propto
P(D|\theta)P(\theta).
```

Posterior không chỉ phụ thuộc dữ liệu mà còn phụ thuộc likelihood và prior. Vì vậy khi hai phân tích dùng prior hoặc noise model khác nhau, kết quả có thể khác dù dùng cùng dữ liệu.

## Suy biến tham số

Hai bộ tham số khác nhau có thể tạo phổ hoặc ảnh rất giống nhau.

Ví dụ một nguồn đỏ có thể do:

- nhiệt độ thấp hơn;
- nhiều bụi hơn;
- redshift khác;
- metallicity khác.

Đây gọi là suy biến (degeneracy). Thêm dữ liệu ở bước sóng khác hoặc phép đo độc lập có thể phá suy biến.

## Multi-wavelength astronomy

Cùng một nguồn có thể trông rất khác ở radio, hồng ngoại, quang học, X-ray và gamma-ray vì mỗi vùng phổ nhạy với cơ chế khác nhau.

Ví dụ:

- radio có thể theo dõi synchrotron và khí lạnh;
- infrared thấy bụi ấm;
- optical thấy sao và vạch nguyên tử;
- X-ray thấy plasma rất nóng và accretion;
- gamma-ray thấy quá trình năng lượng cực cao.

Không có một band duy nhất chứa toàn bộ câu chuyện vật lý.

## Multi-messenger astronomy

Ngoài photon, thiên văn học hiện đại còn dùng:

- neutrino;
- sóng hấp dẫn;
- tia vũ trụ.

Một sự kiện được quan sát bằng nhiều messenger có thể phá các suy biến mà từng kênh riêng không giải quyết được.

Ví dụ sóng hấp dẫn cho trực tiếp thông tin động lực học compact binary, trong khi counterpart điện từ có thể cho môi trường, redshift hoặc nucleosynthesis.

## Worked reasoning: suy nhiệt độ và bán kính sao

Giả sử phổ gần vật đen cho nhiệt độ hiệu dụng `T`, còn parallax cho khoảng cách `d` và photometry cho bolometric flux `F`.

Đầu tiên,

```math
L=4\pi d^2F.
```

Mặt khác,

```math
L=4\pi R^2\sigma T^4.
```

Suy ra

```math
R
=
d\sqrt{\frac{F}{\sigma T^4}}.
```

Một phép đo bán kính vì vậy thực chất ghép nhiều tầng mô hình:

```text
parallax → distance
spectrum → temperature
photometry → flux
blackbody approximation → Stefan-Boltzmann
→ radius
```

Nếu extinction hoặc blackbody approximation sai, bán kính suy ra cũng bị lệch.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Ảnh thiên văn là hình chụp trực tiếp của vật thể như mắt người thấy”

Không nhất thiết. Nhiều ảnh là tổ hợp nhiều filter, bước sóng ngoài vùng nhìn thấy hoặc dữ liệu đã qua calibration và mapping màu.

### “Vạch phổ cho trực tiếp thành phần hóa học”

Không hoàn toàn. Cường độ vạch còn phụ thuộc nhiệt độ, ion hóa, mật độ, transfer và geometry.

### “Đo lâu hơn luôn cho kết quả đúng hơn”

Đo lâu hơn giảm một số noise thống kê nhưng không tự loại systematic error và model bias.

### “Redshift luôn bằng vận tốc chia cho `c`”

Chỉ là xấp xỉ redshift nhỏ. Ở vũ trụ học, redshift gắn với sự giãn nở không-thời gian.

## Mô hình tư duy (Mental Model)

Thiên văn học quan sát là một bài toán suy luận nhiều tầng. Photon không mang theo nhãn “nhiệt độ = 6000 K” hay “khối lượng = 1 M☉”. Ta phải xây mô hình cho nguồn, truyền bức xạ, instrument và noise rồi mới suy tham số.

Vì vậy một kết quả thiên văn tốt nên luôn trả lời bốn câu hỏi:

1. Detector thực sự đo đại lượng nào?
2. Mô hình thuận biến tham số vật lý thành dữ liệu thế nào?
3. Nguồn noise và systematic nào chi phối?
4. Tham số nào thực sự được dữ liệu ràng buộc và tham số nào còn suy biến?

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Photon, laser và coherence](../06_optics/02_photons_lasers_coherence.md), [Vật lý thực nghiệm](../12_experimental_computational/00_measurement_experiment.md), [Bài toán ngược](../12_experimental_computational/02_computational_physics.md).

**Liên hệ tiếp:** [Vật lý sao và thiên thể đặc](00_stars_compact_objects.md), [Thiên hà và vũ trụ học](01_galaxies_cosmology.md).
