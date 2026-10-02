# Photon, độ kết hợp, phát xạ kích thích và laser

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Photon, coherence, stimulated emission và laser**. Route đi từ quantized field → photon statistics → coherence → stimulated emission → optical cavity/laser behavior, để laser nối vi mô với chùm sáng có tổ chức.

Quang sóng giải thích rất tốt giao thoa, nhiễu xạ và sự lan truyền của ánh sáng. Tuy nhiên, khi ánh sáng trao đổi năng lượng với vật chất ở thang nguyên tử, mô tả cổ điển không còn đủ. Photon, chuyển mức lượng tử, độ kết hợp và động lực học không cân bằng của môi trường hoạt tính là những khái niệm cần thiết để hiểu laser.

## Photon: lượng tử của trường điện từ

Một photon có năng lượng

```math
E=h\nu=\hbar\omega
```

và động lượng trong chân không

```math
p=\frac{h}{\lambda}=\hbar k.
```

Không nên hình dung photon như một viên bi nhỏ mang theo một đoạn sóng cổ điển. Trong lý thuyết trường lượng tử, photon là một lượng tử kích thích của chế độ (mode / 모드) trường điện từ. Tính chất hạt xuất hiện rõ trong quá trình hấp thụ và phát xạ rời rạc; tính chất sóng xuất hiện qua pha, giao thoa và phân bố xác suất.

Hiệu ứng quang điện là ví dụ quan trọng. Năng lượng electron bật ra phụ thuộc tần số photon chứ không chỉ cường độ ánh sáng:

```math
K_{max}=h\nu-\Phi,
```

trong đó `\Phi` là công thoát của vật liệu.

Cường độ lớn hơn chủ yếu làm tăng số photon tới trong một đơn vị thời gian; nếu từng photon có năng lượng dưới ngưỡng thì chỉ tăng cường độ không tự giải phóng electron trong mô hình đơn photon đơn giản.

> **Chuyển mạch:** Trong **Photon, độ kết hợp, phát xạ kích thích và laser**, **Độ kết hợp là gì?** tiếp nhận điểm tựa từ **Photon: lượng tử của trường điện từ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ hai mức năng lượng đến hấp thụ và phát xạ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ kết hợp là gì?

Độ kết hợp (coherence / 결맞음) đo mức độ ổn định của quan hệ pha giữa các trường ở những thời điểm hoặc vị trí khác nhau.

Độ kết hợp thời gian (temporal coherence) liên hệ với tương quan pha theo thời gian và độ rộng phổ. Một nguồn có linewidth hẹp thường có thời gian kết hợp dài hơn. Theo bậc độ lớn,

```math
\tau_c\sim\frac{1}{\Delta\nu},
```

và trong chân không,

```math
L_c\sim c\tau_c.
```

Độ kết hợp không gian (spatial coherence) liên hệ với tương quan pha giữa hai điểm khác nhau trên wavefront. Nó quyết định khả năng tạo vân giao thoa rõ khi hai phần của trường được tái kết hợp.

Độ kết hợp không đồng nghĩa với đơn sắc tuyệt đối. Một laser thật luôn có linewidth hữu hạn và coherence thời gian (time / 시간) hữu hạn.

> **Chuyển mạch:** Ở chặng này của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Từ hai mức năng lượng đến hấp thụ và phát xạ** tiếp nhận điểm tựa từ **Độ kết hợp là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ số Einstein và cân bằng chi tiết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ hai mức năng lượng đến hấp thụ và phát xạ

Xét hai mức nguyên tử

```math
E_2>E_1
```

với

```math
E_2-E_1=h\nu.
```

Có ba quá trình cơ bản:

- hấp thụ (absorption): photon làm hệ chuyển từ `E_1` lên `E_2`;
- phát xạ tự phát (spontaneous emission): trạng thái kích thích tự phân rã và phát photon;
- phát xạ kích thích (stimulated emission): trường tới kích thích trạng thái `E_2` phát photon vào chế độ (mode / 모드) tương thích.

Điểm đặc biệt của phát xạ kích thích là photon mới có tần số, phân cực và pha liên hệ với trường kích thích. Đây là cơ chế tạo khuếch đại kết hợp trong laser.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Hệ số Einstein và cân bằng chi tiết** tiếp nhận điểm tựa từ **Từ hai mức năng lượng đến hấp thụ và phát xạ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Population inversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ số Einstein và cân bằng chi tiết

Einstein mô tả ba quá trình bằng các hệ số `A` và `B`.

Nếu `N_1`, `N_2` là population của hai mức, còn `\rho(\nu)` là mật độ năng lượng phổ của trường, thì ở dạng sơ đồ:

```math
R_{abs}=B_{12}\rho(\nu)N_1,
```

```math
R_{stim}=B_{21}\rho(\nu)N_2,
```

```math
R_{sp}=A_{21}N_2.
```

Trong cân bằng nhiệt, các population tuân phân bố Boltzmann nên mức thấp thường đông hơn mức cao. Khi đó hấp thụ không tự nhiên bị vượt qua bởi phát xạ kích thích. Vì vậy để có khuếch đại quang học thuần, cần đưa môi trường ra khỏi cân bằng.

> **Chuyển mạch:** Trong **Photon, độ kết hợp, phát xạ kích thích và laser**, **Population inversion** tiếp nhận điểm tựa từ **Hệ số Einstein và cân bằng chi tiết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao laser hai mức lý tưởng khó hoạt động liên tục?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Population inversion

Population inversion là trạng thái trong đó population hiệu dụng của mức laser trên lớn hơn mức laser dưới theo điều kiện tạo gain của chuyển mức.

Một biểu thức gain tín hiệu nhỏ có dạng

```math
g(\nu)
\propto
N_2\sigma_{21}(\nu)-N_1\sigma_{12}(\nu),
```

trong đó `\sigma` là tiết diện chuyển mức.

Nếu

```math
N_2\sigma_{21}>N_1\sigma_{12},
```

môi trường có gain dương tại tần số đó.

Population inversion không phải trạng thái cân bằng nhiệt thông thường. Nó phải được duy trì bằng pumping: quang học, điện, dòng điện, va chạm hoặc cơ chế khác.

> **Chuyển mạch:** Ở chặng này của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Vì sao laser hai mức lý tưởng khó hoạt động liên tục?** tiếp nhận điểm tựa từ **Population inversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tỷ lệ (rate / 비율) equations: laser bắt đầu dao động như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao laser hai mức lý tưởng khó hoạt động liên tục?

Trong hệ hai mức thuần túy, cùng trường cộng hưởng vừa gây hấp thụ vừa gây phát xạ kích thích. Khi pumping mạnh, population hai mức có xu hướng tiến gần nhau, khiến rất khó duy trì inversion ổn định.

Do đó laser thực tế thường dùng hệ ba mức hoặc bốn mức.

Trong laser ba mức, hạt được bơm lên trạng thái cao rồi nhanh chóng thư giãn xuống mức laser trên. Mức laser dưới thường là gần ground trạng thái (state / 상태) nên cần pumping mạnh để vượt population của mức dưới.

Trong laser bốn mức, mức laser dưới nhanh chóng phân rã xuống mức thấp hơn, vì vậy population của mức laser dưới có thể giữ nhỏ. Điều này làm inversion dễ đạt hơn và giảm threshold.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Tỷ lệ (rate / 비율) equations: laser bắt đầu dao động như thế nào?** tiếp nhận điểm tựa từ **Vì sao laser hai mức lý tưởng khó hoạt động liên tục?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cavity quang học và chế độ (mode / 모드) dọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tỷ lệ (rate / 비율) equations: laser bắt đầu dao động như thế nào?

Một mô hình tối giản dùng hai biến: population inversion `N` và số photon trong cavity `S`.

Dạng khái niệm của tỷ lệ (rate / 비율) equations là

```math
\frac{dN}{dt}
=R_p-\frac{N}{\tau_N}-GNS,
```

```math
\frac{dS}{dt}
=GNS-\frac{S}{\tau_p}+\beta\frac{N}{\tau_N}.
```

`R_p` là tốc độ pumping, `\tau_N` là thời gian tồn tại (lifetime / 수명) của excitation, `\tau_p` là photon thời gian tồn tại (lifetime / 수명) trong cavity, `G` là hệ số coupling/gain và `\beta` mô tả phần phát xạ tự phát đi vào chế độ (mode / 모드) laser.

Dưới threshold, mất mát (loss / 손실) thắng gain và photon trong chế độ (mode / 모드) laser không tự duy trì. Khi inversion đủ lớn để

```math
G N_{th}\approx\frac{1}{\tau_p},
```

net gain cân bằng mất mát (loss / 손실). Trên threshold, trường trong cavity tăng mạnh cho tới khi gain saturation và depletion của inversion tạo trạng thái xác lập mới.

Đây là lý do threshold không chỉ là “đủ nhiều photon”; nó là điều kiện động lực học giữa pumping, gain và mất mát (loss / 손실).

> **Chuyển mạch:** Trong **Photon, độ kết hợp, phát xạ kích thích và laser**, **Cavity quang học và chế độ (mode / 모드) dọc** tiếp nhận điểm tựa từ **Tỷ lệ (rate / 비율) equations: laser bắt đầu dao động như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Threshold từ round-trip gain và mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cavity quang học và chế độ (mode / 모드) dọc

Hai gương tạo resonator. Với cavity đơn giản dài `L`, điều kiện cộng hưởng gần là

```math
2nL=m\lambda,
```

nên tần số chế độ (mode / 모드) xấp xỉ

```math
\nu_m\approx\frac{mc}{2nL}.
```

Khoảng cách giữa hai chế độ (mode / 모드) dọc liên tiếp, hay free spectral phạm vi (range / 범위) (FSR), là

```math
\Delta\nu_{FSR}\approx\frac{c}{2nL}.
```

Môi trường gain chỉ khuếch đại trong một dải tần hữu hạn. Vì vậy chế độ (mode / 모드) laser thực tế được chọn bởi sự chồng lấp giữa spectrum gain và resonances của cavity.

> **Chuyển mạch:** Ở chặng này của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Threshold từ round-trip gain và mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Cavity quang học và chế độ (mode / 모드) dọc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Linewidth, photon thời gian tồn tại (lifetime / 수명) và chất lượng (quality / 품질) factor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Threshold từ round-trip gain và mất mát (loss / 손실)

Nếu `g` là hệ số gain trên đơn vị chiều dài, `\alpha_i` là nội bộ (internal / 내부) mất mát (loss / 손실), còn hai gương có reflectivity `R_1`, `R_2`, điều kiện threshold đơn giản có thể viết

```math
e^{2(g-\alpha_i)L}R_1R_2=1.
```

Lấy log,

```math
g_{th}
=
\alpha_i+
\frac{1}{2L}\ln\left(\frac{1}{R_1R_2}\right).
```

Công thức này cho thấy threshold phụ thuộc đồng thời vào vật liệu gain, mất mát (loss / 손실) nội tại, độ dài cavity và độ phản xạ gương.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Linewidth, photon thời gian tồn tại (lifetime / 수명) và chất lượng (quality / 품질) factor** tiếp nhận điểm tựa từ **Threshold từ round-trip gain và mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Coherence và linewidth qua Fourier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Linewidth, photon thời gian tồn tại (lifetime / 수명) và chất lượng (quality / 품질) factor

Photon không tồn tại mãi trong cavity. Nếu năng lượng trường suy giảm theo thời gian đặc trưng `\tau_p`, linewidth cavity có bậc

```math
\Delta\nu_c\sim\frac{1}{2\pi\tau_p}.
```

Chất lượng (quality / 품질) factor

```math
Q=\frac{\omega_0}{\Delta\omega}
```

đo mức hẹp của resonance.

Laser linewidth còn bị ảnh hưởng bởi nhiễu pha và phát xạ tự phát. Vì vậy cavity có `Q` cao giúp nhưng không tự bảo đảm linewidth bằng không.

> **Chuyển mạch:** Trong **Photon, độ kết hợp, phát xạ kích thích và laser**, **Coherence và linewidth qua Fourier** tiếp nhận điểm tựa từ **Linewidth, photon thời gian tồn tại (lifetime / 수명) và chất lượng (quality / 품질) factor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chế độ (mode / 모드) locking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coherence và linewidth qua Fourier

Một trường gần đơn sắc có thể duy trì pha trong thời gian dài. Ngược lại, pulse rất ngắn cần phổ rộng.

Quan hệ bất định Fourier có dạng bậc độ lớn

```math
\Delta t\,\Delta\nu\gtrsim O(1).
```

Do đó pulse femtosecond không thể đồng thời có spectrum cực hẹp.

Đây là liên hệ quan trọng giữa laser liên tục narrow-linewidth và laser ultrafast: hai hệ tối ưu những thuộc tính khác nhau của cùng cấu trúc thời gian–tần số.

> **Chuyển mạch:** Ở chặng này của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Chế độ (mode / 모드) locking** tiếp nhận điểm tựa từ **Coherence và linewidth qua Fourier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Laser bán dẫn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chế độ (mode / 모드) locking

Nếu nhiều chế độ (mode / 모드) dọc có pha ngẫu nhiên, tổng trường không tạo pulse ngắn ổn định. Nếu pha tương đối giữa các chế độ (mode / 모드) được khóa, chúng giao thoa tăng cường tại những thời điểm nhất định và triệt tiêu ở phần lớn thời gian còn lại.

Kết quả là train pulse ngắn lặp lại với chu kỳ gần thời gian round trip của cavity.

Chế độ (mode / 모드) locking là một ví dụ trực tiếp cho thấy pulse ngắn không xuất hiện vì “laser bật tắt rất nhanh” theo nghĩa đơn giản; nó xuất hiện từ sự khóa pha của nhiều chế độ (mode / 모드) phổ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Laser bán dẫn** tiếp nhận điểm tựa từ **Chế độ (mode / 모드) locking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Laser, LED và đèn nhiệt khác nhau ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Laser bán dẫn

Trong laser bán dẫn, electron trong dải dẫn và lỗ trống trong dải hóa trị tái hợp để phát photon. Phân cực thuận của tiếp giáp P–N hoặc cấu trúc dị thể bơm hạt tải vào vùng hoạt tính.

Khi quasi-Fermi levels và mật độ hạt tải đạt điều kiện thích hợp, vật liệu có optical gain. Cavity thường được tạo ngay trong chip bằng các mặt phản xạ hoặc cấu trúc quang tử.

Laser bán dẫn nối trực tiếp band lý thuyết (theory / 이론) với photonics: band gap đặt thang năng lượng photon, density of states ảnh hưởng gain spectrum, còn carrier recombination và cavity mất mát (loss / 손실) quyết định threshold cùng efficiency.

> **Chuyển mạch:** Trong **Photon, độ kết hợp, phát xạ kích thích và laser**, **Laser, LED và đèn nhiệt khác nhau ở đâu?** tiếp nhận điểm tựa từ **Laser bán dẫn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ: ước lượng FSR của cavity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Laser, LED và đèn nhiệt khác nhau ở đâu?

LED dựa chủ yếu vào phát xạ tự phát. Photon phát ra có pha tương đối phần lớn không được khóa, nên độ kết hợp thấp hơn laser.

Laser dựa trên stimulated emission cộng cavity phản hồi (feedback / 피드백) và population inversion. Điều này tạo directionality, linewidth hẹp hơn và coherence cao hơn.

Đèn nhiệt tạo bức xạ từ một phân bố rộng chế độ (mode / 모드) và tần số gần cân bằng nhiệt. Cường độ lớn không biến một nguồn nhiệt thành laser.

> **Chuyển mạch:** Ở chặng này của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Laser, LED và đèn nhiệt khác nhau ở đâu?** cho ta quy tắc; **Ví dụ: ước lượng FSR của cavity** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Điều kiện áp dụng và giới hạn mô hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ: ước lượng FSR của cavity

Với cavity không khí dài

```math
L=0.30\,m,
```

FSR là

```math
\Delta\nu_{FSR}
\approx
\frac{3\times10^8}{2(0.30)}
\approx5\times10^8\,Hz.
```

Tức khoảng `500 MHz`.

Nếu gain bandwidth rộng `100 GHz`, về mặt hình học có thể chứa khoảng

```math
\frac{100\,GHz}{0.5\,GHz}\approx200
```

cavity modes. Nhưng chế độ (mode / 모드) competition, spatial hole burning, dispersion và gain saturation có thể làm số chế độ (mode / 모드) thực sự dao động nhỏ hơn nhiều.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Photon, độ kết hợp, phát xạ kích thích và laser**, trường hợp ở **Ví dụ: ước lượng FSR của cavity** cho thấy quy tắc hoạt động; **Điều kiện áp dụng và giới hạn mô hình** kiểm tra nơi quy tắc ấy không còn áp dụng hoặc dễ bị hiểu nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều kiện áp dụng và giới hạn mô hình

Mô hình Einstein hai mức bỏ qua cấu trúc mức chi tiết, broadenings và coherence giữa các trạng thái. tỷ lệ (rate / 비율) equations bỏ qua pha của trường nên không đủ để mô tả pulse ultrashort hoặc coherent transient phức tạp; khi đó cần Maxwell–Bloch equations hoặc mô hình trường–vật chất sâu hơn.

Biểu thức threshold đơn giản giả định cavity một chiều, gain đồng đều và mất mát (loss / 손실) có thể gom thành tham số hiệu dụng. Laser thật có thermal lensing, spatial modes, nonlinearities, carrier dynamics và kỹ thuật stabilization riêng.

> **Chuyển mạch:** Trong **Photon, độ kết hợp, phát xạ kích thích và laser**, **Điều kiện áp dụng và giới hạn mô hình** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Laser hình thành khi ba lớp vật lý khớp nhau: **chuyển mức lượng tử tạo khả năng phát xạ, pumping tạo trạng thái không cân bằng có gain, còn cavity chọn và phản hồi các chế độ (mode / 모드) điện từ**. Threshold là điểm gain cân bằng mất mát (loss / 손실); coherence và linewidth là kết quả của động lực học pha, cavity thời gian tồn tại (lifetime / 수명) và noise chứ không chỉ của “độ sáng”.

> **Chuyển mạch:** Ở chặng này của **Photon, độ kết hợp, phát xạ kích thích và laser**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Laser chỉ là ánh sáng rất mạnh”

Không. Một laser yếu vẫn là laser nếu nó hoạt động bằng stimulated emission với cavity/chế độ (mode / 모드) cấu trúc (structure / 구조) phù hợp. Directionality, coherence và spectral properties thường quan trọng hơn cường độ đơn thuần.

### “Population inversion nghĩa là mọi nguyên tử đều ở trạng thái kích thích”

Không. Chỉ cần population hiệu dụng của chuyển mức laser tạo net gain dương. Hệ thực có nhiều mức và nhiều quá trình relaxation.

### “Photon trong stimulated emission là bản sao cổ điển hoàn toàn của photon tới”

Phát biểu này quá thô. Quá trình lượng tử làm tăng occupation của chế độ (mode / 모드) tương thích; các tính chất quan sát như phase coherence và directionality xuất hiện từ coupling giữa trường và môi trường trong chế độ (mode / 모드) đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Photon, độ kết hợp, phát xạ kích thích và laser**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Quang sóng](01_wave_optics.md), [Nền tảng lượng tử](../08_quantum/00_quantum_foundations.md), [Vật lý nguyên tử](../09_atomic_nuclear_particle/00_atomic_physics.md).

**Liên hệ tiếp:** [Bán dẫn và thiết bị](../10_condensed_matter_devices/01_semiconductors_devices.md), [Phân cực, tán sắc và quang phi tuyến](03_polarization_dispersion_nonlinear_optics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
