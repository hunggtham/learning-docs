# Bức xạ điện từ, tán xạ và anten: khi điện tích gia tốc phát sóng

## Vì sao điện tích đứng yên không liên tục phát bức xạ?

Một điện tích đứng yên tạo điện trường tĩnh. Một điện tích chuyển động thẳng đều tạo trường điện từ khác, nhưng trong chân không nó không liên tục phát bức xạ chỉ vì đang chuyển động.

Bức xạ điện từ (electromagnetic radiation / 전자기 복사) xuất hiện khi phân bố điện tích và dòng điện thay đổi theo thời gian theo cách tạo ra nhiễu động có thể tách khỏi nguồn và mang năng lượng ra xa.

Gần nguồn, trường có thể chứa phần phản kháng (reactive field) lưu trữ năng lượng rồi trao đổi trở lại với nguồn. Ở vùng xa, thành phần bức xạ giảm theo `1/r` và mang dòng năng lượng ra ngoài.

## Thế trễ: trường phản ứng với trạng thái quá khứ của nguồn

Thông tin điện từ không truyền tức thời. Thế tại điểm quan sát và thời gian `t` phụ thuộc vào nguồn tại **thời gian trễ (retarded time)**

```math
t_r=t-\frac{R}{c},
```

trong đó `R` là khoảng cách từ phần tử nguồn tới điểm quan sát.

Đây là hệ quả của phương trình sóng cho thế điện từ trong gauge Lorenz. Nếu nguồn thay đổi tại một thời điểm, người quan sát cách 300 km chỉ nhận được ảnh hưởng sau khoảng `1 ms`.

Sự trễ này là nền tảng cho việc nguồn dao động tạo ra sóng lan truyền.

## Bức xạ từ lưỡng cực điện

Một trong những nguồn bức xạ đơn giản nhất là mômen lưỡng cực điện

```math
\mathbf p(t)=\sum_i q_i\mathbf r_i.
```

Nếu lưỡng cực dao động điều hòa,

```math
\mathbf p(t)=\mathbf p_0\cos\omega t,
```

thì trong vùng xa, độ lớn trường điện bức xạ có dạng tỉ lệ

```math
E_{rad}\propto
\frac{\omega^2p_0}{c^2r}\sin\theta.
```

Từ cấu trúc này có ba kết luận quan trọng:

- trường bức xạ giảm theo `1/r`, nên cường độ giảm theo `1/r^2`;
- bức xạ mạnh hơn khi chuyển động điện tích có gia tốc đặc trưng lớn hơn;
- lưỡng cực phát yếu dọc theo trục của nó và mạnh nhất theo phương vuông góc trục.

Do đó đồ thị bức xạ của anten không nhất thiết đẳng hướng.

## Công thức Larmor

Trong giới hạn không tương đối tính, công suất bức xạ của điện tích điểm có gia tốc `a` là

```math
P=\frac{q^2a^2}{6\pi\varepsilon_0c^3}.
```

Đây là công thức Larmor (Larmor formula / 라모어 공식).

Nó cho thấy gia tốc của điện tích là nguồn cơ bản của bức xạ cổ điển. Tuy nhiên, khi áp dụng cho anten, vật chất hoặc máy gia tốc, phải xét thêm chuyển động tập thể, độ kết hợp pha, hiệu ứng trễ và thuyết tương đối.

Không thể luôn cộng đơn giản công suất của từng electron nếu chuyển động của chúng có tương quan pha.

## Vector Poynting và dòng năng lượng

Dòng năng lượng điện từ được mô tả bởi vector Poynting

```math
\mathbf S=\frac{1}{\mu_0}\mathbf E\times\mathbf B.
```

Trong vùng xa của sóng điện từ, `\mathbf E`, `\mathbf B` và hướng truyền vuông góc nhau.

Với sóng phẳng điều hòa,

```math
\langle S\rangle
=\frac12c\varepsilon_0E_0^2.
```

Định lý Poynting biểu diễn bảo toàn năng lượng giữa điện tích, dòng điện và trường. Trong anten phát, công điện từ nguồn được chuyển thành năng lượng trường rồi chảy ra không gian.

## Anten không bắn electron tới máy thu

Trong anten phát, electron trong vật dẫn chủ yếu dao động cục bộ. Chúng không bay từ trạm phát tới điện thoại.

Thứ truyền qua không gian là trường điện từ mang năng lượng và thông tin.

Với dipole nửa bước sóng, chiều dài đặc trưng gần

```math
L\approx\frac{\lambda}{2}.
```

Lý do là phân bố dòng điện và điều kiện biên tạo cộng hưởng hiệu quả ở thang này.

Trong anten thực, chiều dài tối ưu còn phụ thuộc môi trường điện môi, đường kính dây, cấu trúc cấp nguồn, matching và các vật thể lân cận.

## Ghép trở kháng và công suất phản xạ

Anten là tải của đường truyền. Nếu trở kháng anten `Z_L` khác trở kháng đặc trưng `Z_0` của đường truyền, một phần sóng sẽ phản xạ.

Hệ số phản xạ là

```math
\Gamma=\frac{Z_L-Z_0}{Z_L+Z_0}.
```

Ghép trở kháng tốt giúp giảm phản xạ và truyền công suất hiệu quả tới anten.

Trong kỹ thuật RF, VSWR là một cách biểu diễn mức mismatch. Phản xạ lớn không chỉ giảm công suất phát mà còn có thể tạo sóng đứng với điện áp hoặc dòng điện cục bộ cao trên đường truyền.

## Tán xạ: vật chất tạo trường thứ cấp như thế nào?

Tán xạ (scattering / 산란) là sự phân bố lại năng lượng và hướng truyền của sóng khi tương tác với vật chất.

Ở mức vi mô, điện trường tới làm các điện tích liên kết hoặc tự do dao động. Các điện tích gia tốc này tạo trường điện từ thứ cấp. Giao thoa giữa trường tới và trường thứ cấp tạo nên truyền qua, phản xạ và tán xạ.

## Tán xạ Rayleigh

Khi kích thước hạt nhỏ hơn nhiều bước sóng, trong chế độ Rayleigh ta có gần đúng

```math
I_{scat}\propto\frac{1}{\lambda^4}.
```

Bước sóng ngắn bị tán xạ mạnh hơn, góp phần làm bầu trời nhìn xanh.

Khi Mặt Trời ở thấp gần chân trời, ánh sáng đi qua quãng đường khí quyển dài hơn. Thành phần xanh bị tán xạ khỏi đường nhìn trực tiếp nhiều hơn, nên ánh sáng còn lại giàu đỏ/cam hơn.

## Tán xạ Mie

Khi kích thước hạt so sánh được với bước sóng, định luật `1/\lambda^4` không còn phù hợp.

Lý thuyết Mie cho cấu trúc góc phức tạp và phụ thuộc màu yếu hơn. Các giọt nước trong mây nằm trong chế độ này, góp phần làm mây thường trắng hoặc xám thay vì xanh.

## Hấp thụ và phát xạ

Vật chất có các cộng hưởng điện tử, dao động và quay. Trường tới có thể truyền năng lượng vào các bậc tự do bên trong.

Hệ số hấp thụ phụ thuộc tần số và vật liệu. Ở cân bằng nhiệt, phát xạ và hấp thụ liên hệ với nhau qua detailed balance.

Phổ vật đen vì vậy không chỉ là hiện tượng “vật nóng phát sáng”; nó phản ánh cân bằng thống kê giữa mode trường điện từ và vật chất.

## Phản lực bức xạ và giới hạn của điện tích điểm cổ điển

Nếu điện tích phát năng lượng ra ngoài, chuyển động của nó phải chịu phản lực để bảo toàn năng lượng–động lượng.

Mô hình phản lực bức xạ của điện tích điểm cổ điển có thể xuất hiện các nghiệm bệnh lý như runaway acceleration nếu dùng một cách ngây thơ.

Đây là dấu hiệu cho thấy mô hình điện tích điểm cổ điển có giới hạn ở thang rất ngắn. Điện động lực học lượng tử mô tả phát xạ trong một khung sâu hơn.

## Bức xạ tương đối tính: synchrotron và beaming

Khi hạt tích điện tương đối tính chuyển động cong trong từ trường, nó phát bức xạ synchrotron (synchrotron radiation / 싱크로트론 복사).

Do hiệu ứng tương đối tính, bức xạ tập trung mạnh vào một nón hẹp gần hướng vận tốc tức thời.

Bức xạ synchrotron có vai trò:

- gây mất năng lượng đáng kể trong máy gia tốc electron;
- tạo nguồn tia X mạnh trong synchrotron facility;
- là công cụ chẩn đoán jet thiên văn, pulsar và tàn dư siêu tân tinh.

## Radar, thông tin vô tuyến và viễn thám

Radar phát xung điện từ và đo tín hiệu tán xạ trở về. Khoảng cách liên hệ với thời gian truyền khứ hồi:

```math
R=\frac{c\Delta t}{2}.
```

Dịch Doppler cung cấp vận tốc xuyên tâm.

Viễn thám khai thác phụ thuộc theo tần số và phân cực của tán xạ để suy ra mưa, thực vật, băng, địa hình hoặc đặc tính khí quyển.

Đây là cầu nối trực tiếp giữa điện từ học, xử lý tín hiệu, estimation và phần cứng truyền thông.

## Miền gần và miền xa

Không có một khoảng cách duy nhất đúng cho mọi anten, nhưng về nguyên tắc:

- miền gần chứa thành phần phản kháng đáng kể và phụ thuộc mạnh hình học nguồn;
- miền xa có dạng sóng bức xạ ổn định hơn, với trường giảm gần `1/r`.

Với anten kích thước đặc trưng `D`, tiêu chuẩn miền xa thường liên quan tỉ số kiểu

```math
r\gg\frac{2D^2}{\lambda}.
```

Hệ số cụ thể phụ thuộc định nghĩa kỹ thuật, nhưng ý tưởng quan trọng là phải biết mình đang đo trường phản kháng gần nguồn hay trường bức xạ thật sự.

## Kiểm tra thứ nguyên và bậc độ lớn

Công suất Larmor có đơn vị watt. Vector Poynting có đơn vị

```text
W/m²
```

vì nó biểu diễn công suất qua một đơn vị diện tích.

Nếu cường độ vùng xa giảm theo `1/r^2`, tích cường độ trên mặt cầu `4\pi r^2` sẽ gần không đổi nếu bỏ hấp thụ. Đây là một kiểm tra trực tiếp của bảo toàn năng lượng.

## Mô hình tư duy (Mental Model)

Bức xạ là phần của trường điện từ có thể tách khỏi nguồn và mang năng lượng ra xa. Điện tích gia tốc tạo nhiễu động; hình học và pha của nhiều điện tích quyết định pattern phát; vật chất nhận sóng rồi tạo trường thứ cấp quan sát được dưới dạng phản xạ, hấp thụ và tán xạ.

Có thể hình dung chuỗi:

```text
nguồn dòng/điện tích thay đổi
→ thế trễ
→ trường gần + trường bức xạ
→ dòng Poynting
→ lan truyền
→ tương tác vật chất
→ tán xạ / hấp thụ / thu anten
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Anten gửi electron qua không khí”

Không. Electron chủ yếu dao động cục bộ trong vật dẫn; trường điện từ mang năng lượng và thông tin.

### “Cường độ giảm vì photon tự mất năng lượng khi đi xa”

Trong chân không lý tưởng, photon không mất năng lượng chỉ vì khoảng cách tăng. Flux trải trên diện tích lớn hơn nên cường độ giảm.

### “Mọi điện tích đang chuyển động đều phát bức xạ”

Không. Chuyển động thẳng đều trong hệ quán tính không tương đương với chuyển động có gia tốc phát bức xạ.

### “Mọi vùng gần anten đều có thể dùng công thức sóng phẳng vùng xa”

Không. Ở miền gần, cấu trúc trường phụ thuộc nguồn và có thành phần phản kháng đáng kể.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Maxwell và sóng điện từ](04_maxwell_em_waves.md), [Thế điện từ và gauge](06_potentials_gauge.md), [Đường truyền](05_transmission_lines_waveguides.md).

**Liên hệ tiếp:** [Quang học sóng](../06_optics/01_wave_optics.md), [Thiên văn quan sát và truyền bức xạ](../11_astrophysics_cosmology/02_observational_astrophysics_radiative_transfer.md), [Động lực lượng tử và tán xạ](../08_quantum/06_time_dependent_scattering.md).
