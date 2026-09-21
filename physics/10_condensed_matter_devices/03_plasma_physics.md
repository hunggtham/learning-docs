# Vật lý plasma: gần trung hòa, che chắn Debye, sóng tập thể và giam giữ

Plasma không chỉ là “khí rất nóng”. Điều làm plasma khác một khí ion hóa loãng thông thường là các hạt mang điện không còn tương tác chủ yếu theo từng cặp độc lập; chúng cùng tạo trường điện từ, và chính các trường đó lại điều khiển chuyển động của cả quần thể hạt. Tính tập thể (collective behavior / 집단 거동) là điểm cốt lõi.

## Khi nào một khí ion hóa được xem là plasma?

Một môi trường thể hiện hành vi plasma rõ khi ít nhất ba điều kiện mang tính thang đo được thỏa mãn:

1. Kích thước hệ lớn hơn đáng kể chiều dài Debye `\lambda_D`.
2. Trong một “quả cầu Debye” có nhiều hạt, để che chắn là một hiệu ứng tập thể trơn thay vì dao động mạnh do vài hạt riêng lẻ.
3. Tần số quan sát đủ thấp hoặc thời gian quan sát đủ dài để plasma có thể thiết lập đáp ứng tập thể.

Điều này cho thấy “tỉ lệ ion hóa cao” chưa đủ để định nghĩa plasma.

## Tính gần trung hòa

Ở thang lớn hơn `\lambda_D`, mật độ electron và ion thường gần nhau:

```math
n_e\approx Z n_i.
```

Mật độ điện tích ròng nhỏ so với tổng mật độ hạt. Tuy nhiên “gần trung hòa” không có nghĩa điện trường bằng không ở mọi nơi.

Nếu một vùng xuất hiện dư điện tích, điện trường sinh ra kéo các hạt mang điện theo hướng khôi phục cân bằng. Vì vậy quasi-neutrality là một trạng thái động lực học tự tổ chức của plasma.

## Suy ra chiều dài Debye

Xét ion nặng gần đứng yên và electron ở cân bằng nhiệt trong một thế điện `\phi`. Mật độ electron gần Boltzmann:

```math
n_e\approx n_0\exp\left(\frac{e\phi}{k_BT_e}\right).
```

Khi `|e\phi|\ll k_BT_e`, tuyến tính hóa:

```math
n_e\approx n_0\left(1+\frac{e\phi}{k_BT_e}\right).
```

Kết hợp với phương trình Poisson,

```math
\nabla^2\phi=-\frac{\rho}{\varepsilon_0},
```

ta thu được dạng

```math
\nabla^2\phi\approx\frac{\phi}{\lambda_D^2},
```

với

```math
\lambda_D=\sqrt{\frac{\varepsilon_0k_BT_e}{n_ee^2}}.
```

Nghiệm quanh một điện tích thử có dạng gần Yukawa:

```math
\phi(r)\propto\frac{e^{-r/\lambda_D}}{r}.
```

Ở khoảng cách lớn hơn vài `\lambda_D`, ảnh hưởng Coulomb của điện tích riêng lẻ bị che chắn mạnh.

## Số hạt trong quả cầu Debye

Một tiêu chí quan trọng là

```math
N_D\sim \frac43\pi n_e\lambda_D^3\gg1.
```

Khi có rất nhiều hạt trong thể tích Debye, mô tả trung bình trường (mean-field) trở nên hợp lý và thăng giáng rời rạc từng hạt tương đối nhỏ.

## Dao động plasma electron

Nếu toàn bộ đám electron bị dịch một đoạn nhỏ so với nền ion nặng, điện tích tách ra tạo trường phục hồi.

Phương trình chuyển động tuyến tính dẫn tới

```math
\ddot x+\omega_{pe}^2x=0,
```

với

```math
\omega_{pe}=\sqrt{\frac{n_ee^2}{m_e\varepsilon_0}}.
```

Đây là tần số plasma electron. Nó là một tần số tập thể, không phải tần số va chạm của một electron riêng lẻ.

## Sóng điện từ trong plasma lạnh

Với plasma electron lạnh không từ hóa, quan hệ tán sắc của sóng điện từ đơn giản có dạng

```math
\omega^2=\omega_{pe}^2+c^2k^2.
```

Nếu

```math
\omega<\omega_{pe},
```

`k` trở thành ảo và sóng không lan truyền sâu vào plasma; trường suy giảm theo khoảng cách.

Điều này giải thích vì sao tầng điện ly có thể phản xạ một số tần số vô tuyến nhưng cho tần số cao hơn đi qua.

## Chuyển động của hạt trong từ trường

Với từ trường đều,

```math
m\frac{d\vec v}{dt}=q\vec v\times\vec B.
```

Thành phần vận tốc song song `\vec B` giữ nguyên, còn thành phần vuông góc tạo chuyển động tròn với tần số cyclotron

```math
\omega_c=\frac{|q|B}{m}.
```

Bán kính Larmor là

```math
r_L=\frac{mv_\perp}{|q|B}.
```

Nếu `r_L` nhỏ hơn nhiều thang chiều dài của hệ, hạt được xem là bị từ hóa mạnh.

## Trôi `E×B`

Khi có điện trường vuông góc từ trường, tâm quỹ đạo cyclotron trôi với vận tốc

```math
\vec v_{E\times B}=\frac{\vec E\times\vec B}{B^2}.
```

Điểm đặc biệt là vận tốc trôi này không phụ thuộc khối lượng hoặc dấu điện tích. Electron và ion cùng trôi theo một hướng, nên đây là một vận chuyển tập thể rất quan trọng.

## Gradient-B và curvature drift

Nếu `B` không đều hoặc đường sức cong, electron và ion có thể có các drift khác hướng vì chúng phụ thuộc dấu điện tích. Sự tách drift này tạo dòng điện và ảnh hưởng ổn định của plasma giam giữ.

Do đó hình học từ trường trong tokamak không chỉ có nhiệm vụ “giữ hạt chạy vòng tròn”; nó phải kiểm soát cả nhiều loại drift và bất ổn định.

## Plasma như một chất lưu

Ở thang đủ lớn so với quãng đường tự do trung bình và khi phân bố gần cân bằng cục bộ, ta có thể lấy các moment của phương trình động học để xây mô hình chất lưu.

Các phương trình cơ bản gồm bảo toàn số hạt, động lượng và năng lượng. Với plasma dẫn điện, từ trường ghép trực tiếp vào phương trình động lượng.

## Từ thủy động lực học (MHD)

Trong MHD lý tưởng, plasma được xem là chất lưu dẫn điện rất tốt. Một phương trình quan trọng là

```math
\frac{\partial\vec B}{\partial t}
=\nabla\times(\vec v\times\vec B).
```

Nó dẫn tới trực giác “đường sức từ bị đông cứng vào chất lưu” (flux freezing) trong giới hạn điện trở rất nhỏ.

Khái niệm này giúp hiểu gió Mặt Trời, cấu trúc từ trong plasma thiên văn và nhiều hiện tượng giam giữ từ.

## Sóng Alfvén

Trong plasma từ hóa, lực căng của từ trường đóng vai trò gần như dây đàn hồi. Nhiễu loạn có thể lan dọc trường với vận tốc Alfvén

```math
v_A=\frac{B}{\sqrt{\mu_0\rho}}.
```

Sóng Alfvén xuất hiện trong plasma Mặt Trời, từ quyển và thiết bị nhiệt hạch. Đây là ví dụ rõ cho việc sóng trong plasma không chỉ là sóng âm hay sóng điện từ thông thường.

## Tái kết nối từ

Trong MHD lý tưởng, topology của đường sức từ được giữ gần như cố định. Nhưng khi điện trở, hiệu ứng Hall hoặc động học vi mô trở nên quan trọng trong một vùng nhỏ, cấu hình từ trường có thể thay đổi topology và giải phóng năng lượng nhanh.

Quá trình này gọi là tái kết nối từ (magnetic reconnection). Nó liên quan tới flare Mặt Trời, magnetosphere và các sự kiện giải phóng năng lượng trong plasma phòng thí nghiệm.

## Phương trình Vlasov và mô tả động học

Khi va chạm yếu, mô hình chất lưu có thể bỏ mất cấu trúc quan trọng của phân bố vận tốc. Khi đó dùng hàm phân bố

```math
f(\vec x,\vec v,t)
```

và phương trình Vlasov:

```math
\frac{\partial f}{\partial t}
+\vec v\cdot\nabla_x f
+\frac{q}{m}(\vec E+\vec v\times\vec B)\cdot\nabla_v f=0.
```

Phương trình này mô tả tiến hóa không va chạm của phân bố hạt dưới trường tự nhất quán.

## Landau damping

Một trong những kết quả sâu của lý thuyết động học là sóng plasma có thể bị tắt dần ngay cả khi không có va chạm rõ rệt.

Những hạt có vận tốc gần vận tốc pha của sóng trao đổi năng lượng cộng hưởng với sóng. Tùy độ dốc của phân bố vận tốc tại vận tốc cộng hưởng, tổng năng lượng có thể truyền từ sóng sang hạt.

Landau damping cho thấy một mô hình chất lưu đơn giản có thể bỏ qua những hiệu ứng nằm trong cấu trúc của không gian vận tốc.

## Va chạm và độ ghép plasma

Tỉ lệ giữa năng lượng thế Coulomb điển hình và năng lượng nhiệt được mô tả bởi tham số ghép

```math
\Gamma\sim\frac{e^2/(4\pi\varepsilon_0a)}{k_BT},
```

với `a` là khoảng cách liên hạt điển hình.

Plasma nhiệt hạch thường ở chế độ ghép yếu `\Gamma\ll1`, trong khi plasma bụi hoặc vật chất mật độ cao có thể đạt chế độ ghép mạnh hơn, nơi tương quan hạt trở nên quan trọng.

## Giam giữ từ và tokamak

Tokamak dùng từ trường toroidal kết hợp poloidal để tạo đường sức xoắn quanh torus. Mục tiêu là giữ hạt nóng tránh tiếp xúc trực tiếp với thành thiết bị đủ lâu để phản ứng nhiệt hạch xảy ra đáng kể.

Nhưng plasma có nhiều bất ổn định MHD và vi mô. Vì vậy “tạo từ trường mạnh” chưa đủ; phải tối ưu hình học, profile dòng, pressure gradient và turbulence.

## Tiêu chuẩn Lawson

Một cách đánh giá điều kiện nhiệt hạch là tích mật độ và thời gian giam giữ năng lượng. Với nhiệt độ thích hợp, hệ cần đạt một ngưỡng của

```math
n\tau_E
```

hoặc dạng triple product

```math
nT\tau_E.
```

Đây là lý do nhiệt độ rất cao chỉ là một phần bài toán. Plasma quá loãng hoặc thất thoát năng lượng quá nhanh vẫn không đạt điều kiện phát năng lượng ròng.

## Vì sao plasma trên Trái Đất cần nóng hơn lõi Mặt Trời?

Mặt Trời có mật độ lớn và được hấp dẫn giam giữ trong thời gian khổng lồ. Thiết bị nhiệt hạch trên Trái Đất có mật độ và thời gian giam giữ khác rất nhiều, nên phải bù bằng nhiệt độ cao hơn và kiểm soát plasma tinh vi hơn.

Không có mâu thuẫn trong việc plasma tokamak có nhiệt độ ion cao hơn lõi Mặt Trời nhưng vẫn khó đạt năng lượng ròng.

## Plasma trong thiên văn học

Phần lớn vật chất nhìn thấy trong vũ trụ ở trạng thái plasma: khí giữa các sao, corona Mặt Trời, gió sao, môi trường bồi tụ và nhiều dòng tia thiên văn.

Trong những môi trường này, va chạm hạt đôi khi rất hiếm nhưng trường điện từ tập thể vẫn tổ chức chuyển động trên thang lớn.

## Mô phỏng plasma

### MHD

Giải phương trình chất lưu và Maxwell ở thang lớn. Phù hợp khi phân bố hạt gần đủ để mô tả bằng moment vĩ mô.

### Particle-in-cell (PIC)

Theo dõi nhiều hạt đại diện trên lưới trường điện từ. Phương pháp này giữ được nhiều hiệu ứng động học hơn nhưng đắt tính toán.

### Hybrid model

Có thể mô tả ion như hạt còn electron như chất lưu, hoặc ghép nhiều thang theo nhu cầu bài toán.

Việc chọn mô hình phải dựa vào thang Debye, bán kính Larmor, tần số plasma, tần số cyclotron, quãng đường tự do trung bình và thang không gian–thời gian cần nghiên cứu.

## Mô hình tư duy (Mental Model)

Plasma là hệ nhiều thang. Ở thang rất nhỏ cần động học hạt; ở thang trung gian cần phân bố vận tốc; ở thang lớn có thể dùng chất lưu và MHD. Không có một mô hình duy nhất tối ưu cho mọi plasma.

Câu hỏi đầu tiên nên là: **thang quan sát của ta so với `\lambda_D`, `r_L`, quãng đường tự do trung bình và các tần số đặc trưng như `\omega_p`, `\omega_c` ra sao?**

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Plasma chỉ là khí nóng”

Không. Một số plasma lạnh có nhiệt độ ion hoặc khí nền thấp nhưng electron năng lượng cao; hành vi tập thể mới là đặc trưng chính.

### “Quasi-neutral nghĩa điện trường bằng không”

Không. Điện trường nhỏ cục bộ có thể cực kỳ quan trọng trong việc duy trì trạng thái gần trung hòa hoặc tạo sheath.

### “Tokamak chỉ cần nam châm thật mạnh”

Không. Giam giữ phụ thuộc topology từ trường, drift, turbulence, pressure gradient và nhiều bất ổn định.

### “MHD luôn đủ cho plasma”

Không. Khi hiệu ứng động học trong không gian vận tốc quan trọng, cần mô hình Vlasov hoặc PIC.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Cơ học chất lưu](../03_continuum/00_fluids.md), [Maxwell và sóng điện từ](../05_electromagnetism/04_maxwell_em_waves.md), [Lý thuyết động học và Boltzmann](../04_thermal_statistical/06_kinetic_theory_boltzmann_equation.md).

**Liên hệ tiếp:** [Vật lý sao](../11_astrophysics_cosmology/00_stars_compact_objects.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md), [Chuyển pha và truyền nhiệt](../04_thermal_statistical/02_phase_transitions_heat_transfer.md).
