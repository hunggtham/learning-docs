# Vũ trụ sơ khai, vật chất tối và năng lượng tối

Vũ trụ sơ khai (early universe / 초기 우주) là chế độ nóng và đậm đặc nơi sự giãn nở của không-thời gian, vật lý hạt và nhiệt động lực học cùng quyết định tiến hóa của Vũ trụ.

**Vật chất tối (dark matter / 암흑물질)** và **năng lượng tối (dark energy / 암흑에너지)** là tên của hai thành phần được suy ra từ nhiều quan sát hấp dẫn và vũ trụ học. Bản chất vi mô của chúng vẫn chưa được xác định đầy đủ.

## Big Bang không phải một vụ nổ tại một điểm trong không gian

Vũ trụ học hiện đại mô tả chính hình học không-thời gian đang giãn nở.

Trong xấp xỉ đồng nhất và đẳng hướng ở quy mô lớn, sự giãn nở được mô tả bằng hệ số tỉ lệ `a(t)`.

Các thiên hà xa không nên được hình dung như mảnh vỡ bay từ một tâm duy nhất vào một không gian trống có sẵn. Mỗi người quan sát comoving đều thấy các thiên hà xa rời nhau theo cùng một quy luật giãn nở lớn-scale.

## Phương trình Friedmann

Từ phương trình Einstein với metric FLRW, ta thu được phương trình Friedmann

```math
H^2
=\left(\frac{\dot a}{a}\right)^2
=\frac{8\pi G}{3}\rho
-\frac{kc^2}{a^2}
+\frac{\Lambda c^2}{3}.
```

Trong đó:

- `H=\dot a/a` là tốc độ giãn nở tương đối;
- `\rho` là mật độ năng lượng tổng;
- `k` mô tả độ cong không gian trong quy ước FLRW;
- `\Lambda` là hằng số vũ trụ.

Phương trình có hình thức gợi nhớ cân bằng năng lượng, nhưng ý nghĩa đầy đủ đến từ thuyết tương đối rộng chứ không phải cơ học vụ nổ Newton.

Đơn vị của `H` là nghịch đảo thời gian. Vì vậy `1/H` cung cấp một thang thời gian vũ trụ đặc trưng, dù tuổi thực của Vũ trụ còn phụ thuộc lịch sử `H(t)`.

## Phương trình liên tục và cách mật độ thay đổi theo `a`

Bảo toàn năng lượng–động lượng trong nền FLRW dẫn tới

```math
\dot\rho
+3H\left(\rho+\frac{p}{c^2}\right)=0.
```

Nếu phương trình trạng thái có dạng

```math
p=w\rho c^2,
```

thì

```math
\rho\propto a^{-3(1+w)}.
```

Ba trường hợp quan trọng:

### Vật chất không tương đối tính

Với `w\approx0`,

```math
\rho_m\propto a^{-3}.
```

Mật độ giảm chủ yếu vì cùng lượng vật chất được phân bố trong thể tích tăng theo `a^3`.

### Bức xạ

Với `w=1/3`,

```math
\rho_r\propto a^{-4}.
```

Ngoài sự pha loãng theo thể tích, năng lượng mỗi photon còn giảm do redshift.

### Hằng số vũ trụ

Với `w=-1`,

```math
\rho_\Lambda=\text{hằng số}.
```

Do các thành phần thay đổi theo `a` khác nhau, thành phần chi phối Vũ trụ cũng thay đổi theo thời đại.

## Redshift và hệ số tỉ lệ

Với photon truyền trong nền vũ trụ giãn nở,

```math
1+z
=\frac{a(t_0)}{a(t_{emit})}.
```

Bước sóng photon tăng cùng hệ số tỉ lệ.

Ở redshift nhỏ, quan hệ có thể gần giống Doppler cổ điển. Ở redshift lớn, không nên dùng trực tiếp công thức Doppler không tương đối tính để diễn giải. Cosmological redshift phản ánh hình học và lịch sử giãn nở của không-thời gian.

## Lịch sử nhiệt của Vũ trụ

Đi ngược theo thời gian, mật độ và nhiệt độ tăng.

Một chuỗi khái niệm đơn giản là

```text
vũ trụ nóng, ion hóa
→ nucleosynthesis
→ plasma photon–baryon
→ recombination
→ photon decoupling
→ CMB
→ hình thành cấu trúc
```

Khi Vũ trụ đủ nóng, vật chất tồn tại dưới dạng plasma ion hóa. Khi nguội, hạt nhân nhẹ hình thành; sau đó electron kết hợp với hạt nhân trung hòa và photon có thể truyền tự do xa hơn.

## Big Bang nucleosynthesis

Trong vài phút đầu, nhiệt độ và mật độ cho phép phản ứng hạt nhân tạo chủ yếu:

- hydrogen;
- helium;
- deuterium;
- một lượng nhỏ lithium và các đồng vị nhẹ khác.

Dự đoán abundance phụ thuộc mật độ baryon và tốc độ phản ứng hạt nhân.

Sự phù hợp giữa abundance nguyên thủy quan sát được và mô hình nucleosynthesis là một bằng chứng độc lập cho Vũ trụ sơ khai nóng.

Các nguyên tố nặng hơn không được tạo chủ yếu trong Big Bang vì Vũ trụ nguội và giãn quá nhanh, đồng thời có các bottleneck hạt nhân. Chúng được tổng hợp về sau trong sao và các sự kiện bùng nổ.

## Recombination và nền vi sóng vũ trụ

Trước recombination, photon tán xạ mạnh với electron tự do, nên photon và baryon tạo một chất lưu ghép.

Hấp dẫn có xu hướng nén overdensity, còn áp suất bức xạ chống lại sự nén. Cạnh tranh này tạo các dao động acoustic.

Khi electron kết hợp với hạt nhân và photon decouple, pattern dao động được ghi lại trong anisotropy của nền vi sóng vũ trụ (CMB).

CMB ngày nay gần phổ vật đen ở khoảng `2.7 K`.

Phổ công suất anisotropy chứa các acoustic peak. Vị trí và độ cao của chúng cung cấp ràng buộc lên:

- hình học vũ trụ;
- mật độ baryon;
- mật độ vật chất tối;
- phổ nhiễu loạn ban đầu;
- các tham số vũ trụ học khác.

Đây là ví dụ đẹp: dao động giống âm thanh trong plasma sơ khai được đọc lại từ bầu trời microwave hàng tỷ năm sau.

## Vật chất tối: biết qua hấp dẫn nhưng chưa biết hạt vi mô

Bằng chứng cho thành phần hấp dẫn không phát sáng đáng kể đến từ nhiều thang:

- đường cong quay thiên hà;
- thấu kính hấp dẫn;
- động lực cụm thiên hà;
- CMB;
- cấu trúc lớn;
- sự tăng trưởng của cấu trúc;
- các hệ va chạm cụm nơi phân bố khối lượng từ lensing lệch khỏi khí nóng phát tia X.

Từ “tối” nghĩa thành phần này không tương tác điện từ đủ mạnh để phát hoặc hấp thụ ánh sáng theo cách vật chất baryon thông thường.

Nó không có nghĩa tuyệt đối không có bất kỳ tương tác nào ngoài hấp dẫn.

Có nhiều ứng viên hạt mới, nhưng chưa có định danh vi mô được xác nhận chắc chắn.

Các mô hình hấp dẫn sửa đổi cũng được nghiên cứu. Một mô hình thay thế phải giải thích đồng thời toàn bộ tập quan sát, không chỉ một đường cong quay riêng lẻ.

## Vật chất tối và hình thành cấu trúc

Vật chất tối lạnh có áp suất hiệu dụng nhỏ trên nhiều thang vũ trụ học quan trọng, nên có thể bắt đầu kết tụ hấp dẫn sớm hơn baryon trong một số thời kỳ.

Các halo vật chất tối tạo giếng thế; khí baryon rơi vào, shock, làm lạnh và sau đó hình thành sao cùng thiên hà.

Mô phỏng cấu trúc lớn tiến hóa các điều kiện ban đầu dưới hấp dẫn và sự giãn nở để so sánh cosmic web, halo và clustering quan sát được.

## Năng lượng tối và giãn nở tăng tốc

Quan sát supernova Type Ia xa, kết hợp CMB và cấu trúc lớn, cho thấy lịch sử giãn nở phù hợp với sự tăng tốc ở thời kỳ muộn.

Trong mô hình `\Lambda CDM` đơn giản nhất, năng lượng tối là hằng số vũ trụ có mật độ gần không đổi và áp suất âm.

Phương trình gia tốc có dạng

```math
\frac{\ddot a}{a}
=-\frac{4\pi G}{3}
\left(
\rho+\frac{3p}{c^2}
\right).
```

Nếu áp suất đủ âm, biểu thức trong ngoặc có thể làm `\ddot a>0`.

Không nên hình dung năng lượng tối như một “lực đẩy” cục bộ giữa hai vật. Nó là thành phần của tensor năng lượng–động lượng ảnh hưởng động lực giãn nở của không-thời gian ở quy mô vũ trụ.

## Mật độ tới hạn và tham số mật độ

Mật độ tới hạn được định nghĩa

```math
\rho_c=\frac{3H^2}{8\pi G}.
```

Từ đó

```math
\Omega_i=\frac{\rho_i}{\rho_c}.
```

Các `\Omega` cho vật chất, bức xạ, năng lượng tối và curvature giúp mô tả ngân sách vũ trụ theo dạng vô thứ nguyên.

Lưu ý `\rho_c` thay đổi theo `H(t)`, nên `\Omega_i` cũng có thể thay đổi theo thời gian dù quy luật scaling của `\rho_i` đã biết.

## Inflation

Inflation là giai đoạn giãn nở tăng tốc rất sớm được đề xuất để giải quyết một số bài toán điều kiện ban đầu của cosmology.

Nó giúp giải thích:

- horizon problem: các vùng CMB rất xa có nhiệt độ gần nhau;
- flatness problem: curvature được đẩy gần giá trị phẳng;
- nguồn nhiễu loạn ban đầu: fluctuation lượng tử có thể được kéo giãn tới thang vũ trụ trong nhiều mô hình.

Inflation là một framework thành công về nhiều mặt nhưng cơ chế vi mô cụ thể và trường gây inflation vẫn là chủ đề nghiên cứu.

Không nên trình bày một inflation model cụ thể như lời giải duy nhất đã được chứng minh.

## Baryogenesis và bất đối xứng vật chất–phản vật chất

Vũ trụ quan sát được bị chi phối bởi vật chất. Nếu trạng thái ban đầu đối xứng vật chất–phản vật chất, cần cơ chế tạo baryon asymmetry.

Các điều kiện Sakharov chỉ ra ba thành phần thường cần:

- vi phạm số baryon;
- vi phạm C và CP;
- rời cân bằng nhiệt.

Mô hình Chuẩn chứa một số thành phần này nhưng trong các kịch bản đơn giản thường không đủ để tạo bất đối xứng quan sát được.

Đây là một cầu nối mở giữa cosmology và vật lý hạt.

## Neutrino trong vũ trụ học

Neutrino relic ảnh hưởng cả lịch sử giãn nở và hình thành cấu trúc.

Do có khối lượng nhỏ và free-streaming, neutrino làm giảm clustering ở một số thang.

Dữ liệu vũ trụ học vì vậy có thể ràng buộc tổng khối lượng neutrino theo cách bổ sung cho thí nghiệm phòng lab.

## Tương lai của Vũ trụ

Tương lai giãn nở phụ thuộc tính chất của năng lượng tối và thành phần vũ trụ.

Nếu năng lượng tối là hằng số vũ trụ dương không đổi, Vũ trụ về dài hạn tiến tới chế độ tăng tốc kiểu de Sitter; các cấu trúc không liên kết ở rất xa dần vượt chân trời quan sát.

Nếu phương trình trạng thái của dark energy động, kịch bản tương lai có thể khác.

Dữ liệu hiện tại ràng buộc nhiều mô hình nhưng không cho phép nói rằng bản chất vi mô của dark energy đã được hiểu.

## Miền áp dụng và giới hạn

Phương trình Friedmann ở trên giả sử Vũ trụ đồng nhất và đẳng hướng ở quy mô lớn. Nó không mô tả trực tiếp cấu trúc cục bộ như thiên hà hoặc cụm thiên hà.

`\Lambda CDM` là mô hình hiện tượng học rất thành công nhưng không đồng nghĩa với việc ta đã biết hạt dark matter hoặc cơ chế microscopic của dark energy.

Các suy luận vũ trụ học còn phụ thuộc model, calibration, selection effect và tổ hợp dataset. Vì vậy tham số tốt nhất luôn cần đi cùng uncertainty và giả định mô hình.

## Mô hình tư duy (Mental Model)

Vũ trụ học mô tả sự tiến hóa đồng thời của **hình học không-thời gian** và **nội dung năng lượng–vật chất**.

```text
early hot universe
→ thermal / particle processes
→ recombination + CMB
→ gravitational growth
→ stars / galaxies / cosmic web
→ late-time accelerated expansion
```

Vật chất tối và năng lượng tối là tên cho các hiệu ứng/thành phần cần thiết trong mô hình quan sát hiện tại; tên gọi không đồng nghĩa với việc bản chất vi mô đã được xác định.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Big Bang xảy ra tại một điểm trong không gian”

Không trong mô hình đồng nhất chuẩn. Hệ số tỉ lệ mô tả sự giãn nở của khoảng cách comoving trên toàn không gian.

### “Vật chất tối chắc chắn là hố đen”

Không. Vật thể compact có thể đóng góp một phần trong một số miền khối lượng, nhưng toàn bộ bằng chứng cosmological không được giải thích đơn giản bằng hố đen sao thông thường.

### “Năng lượng tối là lực đẩy các thiên hà cục bộ”

Không nên hình dung như vậy. Các hệ liên kết như nguyên tử, hệ Mặt Trời hoặc thiên hà không đơn giản giãn theo Hubble flow.

### “Redshift lớn có thể đổi thẳng thành vận tốc bằng `v=cz`”

Chỉ đúng xấp xỉ ở `z` nhỏ. Ở `z` lớn phải dùng mô hình cosmological distance–redshift.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Thuyết tương đối rộng](../07_relativity/01_general_relativity.md), [Thiên hà và vũ trụ học](01_galaxies_cosmology.md), [Cơ học thống kê](../04_thermal_statistical/03_ensembles_partition_functions.md).

**Liên hệ tiếp:** [Bất ổn hấp dẫn và hình thành cấu trúc](04_gravitational_instability_structure_formation.md), [Mô hình Chuẩn](../09_atomic_nuclear_particle/03_particle_standard_model.md), [Trường lượng tử](../09_atomic_nuclear_particle/05_quantum_fields_symmetry_interactions.md), [Suy luận dữ liệu](../12_experimental_computational/03_data_inference_inverse_problems.md).
