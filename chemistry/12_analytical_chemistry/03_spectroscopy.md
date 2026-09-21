# Phổ học — biến tương tác vật chất–bức xạ thành thông tin hóa học

> **Phổ học (spectroscopy / 분광학)** khai thác thông tin hóa học từ cách vật chất hấp thụ, phát xạ hoặc tán xạ bức xạ điện từ. Ý tưởng thống nhất là: nguyên tử và phân tử có các trạng thái năng lượng lượng tử hóa, còn bức xạ dùng để thăm dò chênh lệch năng lượng giữa các trạng thái đó.

Phổ học không phải một thiết bị duy nhất. Đây là một họ phương pháp, trong đó **thang năng lượng quyết định bậc tự do nào của vật chất được quan sát**.

Các prerequisite quan trọng gồm [bức xạ điện từ và lượng tử hóa](../01_atomic_structure/01_electromagnetic_radiation_and_quantization.md), [mô hình lượng tử của nguyên tử](../01_atomic_structure/02_quantum_model_of_atom.md), [liên kết cộng hóa trị](../02_chemical_bonding/02_covalent_bonding.md) và [đo lường/lấy mẫu](./00_measurement_and_sampling.md).

## Năng lượng photon và vì sao bước sóng quan trọng

Photon có năng lượng:

\[
E=h\nu=\frac{hc}{\lambda}
\]

Tần số càng cao thì năng lượng photon càng lớn; bước sóng càng dài thì năng lượng càng thấp.

Các chuyển động phân tử có thang năng lượng khác nhau:

```text
tần số vô tuyến → chuyển mức spin hạt nhân (NMR)
vi sóng          → chuyển mức quay
hồng ngoại       → dao động phân tử
khả kiến / UV    → chuyển mức electron hóa trị
tia X            → electron lõi / cấu trúc ở thang nguyên tử
```

Thứ tự này xuất phát từ chính thang năng lượng lượng tử của các bậc tự do khác nhau.

## Hấp thụ, phát xạ và tán xạ

Trong **phổ hấp thụ (absorption spectroscopy)**, mẫu lấy đi photon có năng lượng phù hợp với một chuyển mức được phép.

Trong **phổ phát xạ (emission spectroscopy)**, hệ kích thích trở về trạng thái thấp hơn và phát photon.

Trong **phương pháp tán xạ (scattering)**, photon thay đổi hướng và đôi khi thay đổi năng lượng. Raman là ví dụ tán xạ không đàn hồi liên hệ với dao động phân tử.

Cùng một phân tử vì vậy có thể cung cấp nhiều loại thông tin bổ sung tùy kênh tương tác được đo.

## Quy tắc chọn — đủ năng lượng chưa chắc tạo tín hiệu mạnh

Ngay cả khi photon có năng lượng khớp `ΔE`, cường độ chuyển mức còn phụ thuộc đối xứng và cách bức xạ ghép với trạng thái phân tử.

Trong IR, một dao động phải làm thay đổi mômen lưỡng cực để hoạt động mạnh.

Trong Raman, dao động phải làm thay đổi khả năng phân cực.

Với chuyển mức điện tử, các quy tắc chọn về đối xứng và spin cũng ảnh hưởng cường độ.

Do đó **không có đỉnh mạnh** không đồng nghĩa **không có mô-típ cấu trúc**; chuyển mức có thể yếu hoặc bị cấm theo quy tắc chọn.

## Định luật Beer–Lambert — biến hấp thụ thành nồng độ

Với nhiều dung dịch loãng và đồng nhất:

\[
A=\varepsilon bc
\]

trong đó:

- `A`: độ hấp thụ;
- `ε`: hệ số hấp thụ mol;
- `b`: chiều dài quang học;
- `c`: nồng độ.

Độ truyền qua:

\[
T=\frac{I}{I_0}
\]

và:

\[
A=-\log_{10}T=\log_{10}\frac{I_0}{I}
\]

Logarithm xuất hiện vì suy giảm cường độ ánh sáng tích lũy theo dạng nhân qua các lớp mỏng liên tiếp của mẫu.

### Suy ra dạng hàm mũ

Nếu với lớp mỏng `dx`:

\[
dI=-kcI\,dx
\]

thì tích phân cho:

\[
\ln\frac{I}{I_0}=-kcb
\]

Đổi sang logarithm cơ số 10 thu được dạng Beer–Lambert.

Vì vậy đây không chỉ là công thức thực nghiệm; nó phản ánh một mô hình xác suất hấp thụ gần không đổi theo chiều dài đường quang.

### Vì sao Beer–Lambert lệch tuyến tính?

Các nguyên nhân thường gặp gồm:

- nồng độ cao làm tương tác giữa phân tử thay đổi;
- cân bằng acid–base hoặc kết hợp làm dạng hấp thụ thay đổi theo nồng độ;
- ánh sáng tạp tới bộ phát hiện;
- băng thông nguồn quá rộng;
- mẫu tán xạ;
- cuvet hoặc chiều dài quang học không nhất quán.

Do đó cần thẩm định đường hiệu chuẩn trong đúng khoảng làm việc.

## UV–Vis — chuyển mức electron hóa trị

UV–Vis thường thăm dò chuyển mức electron hóa trị.

Các hệ hữu cơ có thể có chuyển mức `π→π*` hoặc `n→π*`. Phức kim loại chuyển tiếp có thể cho chuyển `d–d` hoặc chuyển điện tích.

### Liên hợp và dịch đỏ

Mở rộng liên hợp thường làm khoảng HOMO–LUMO giảm.

Vì:

\[
\Delta E=\frac{hc}{\lambda}
\]

nên khoảng năng lượng nhỏ hơn tương ứng hấp thụ ở bước sóng dài hơn, gọi là **dịch đỏ (bathochromic/red shift)**.

Đây là lý do hệ liên hợp lớn có thể hấp thụ ánh sáng khả kiến và có màu.

### UV–Vis định lượng

Một quy trình định lượng tốt thường gồm:

1. chọn bước sóng phù hợp;
2. chuẩn bị mẫu trắng;
3. chuẩn bị dãy chuẩn;
4. đo độ hấp thụ;
5. khớp mô hình hiệu chuẩn;
6. kiểm tra phần dư và độ tuyến tính;
7. đo mẫu chưa biết trong khoảng đã thẩm định.

Dùng một điểm chuẩn đơn lẻ yếu hơn nhiều so với một đường hiệu chuẩn được kiểm tra đúng nghĩa.

## Phổ hồng ngoại — dao động phân tử

Phân tử không phải các thanh cứng đứng yên. Liên kết kéo giãn, góc uốn và nhiều nhóm nguyên tử dao động phối hợp.

Với mô hình dao động hai nguyên tử đơn giản:

\[
\tilde\nu\propto\sqrt{\frac{k}{\mu}}
\]

trong đó `k` là hằng số lực và `μ` là khối lượng giảm.

Liên kết mạnh hơn thường dao động ở tần số cao hơn; nguyên tử nặng hơn làm tần số thấp hơn.

### Vì sao dải carbonyl mạnh?

Dao động kéo giãn `C=O` làm mômen lưỡng cực thay đổi mạnh, nên thường cho dải hấp thụ mạnh khoảng `1650–1800 cm⁻¹`, tùy nhóm chức, liên hợp, ứng suất vòng và môi trường.

Liên hợp thường làm tần số kéo giãn carbonyl giảm vì mật độ electron π được phi định xứ và phần đặc tính liên kết đôi giảm.

### O–H và liên kết hydrogen

O–H tự do có thể cho dải tương đối sắc. Liên kết hydrogen tạo một phân bố rộng môi trường liên kết và thường làm dải rộng hơn, đồng thời dịch về tần số thấp hơn.

Do đó độ rộng dải đôi khi phản ánh **phân bố trạng thái hóa học**, không chỉ nhiễu thiết bị.

### Vùng dấu vân tay

Dưới khoảng `1500 cm⁻¹`, nhiều dao động ghép tạo mẫu phổ phức tạp.

Vùng này hữu ích để xác nhận danh tính vì hai hợp chất có cùng nhóm chức vẫn có thể có mẫu dấu vân tay khác nhau.

## Raman — bổ sung cho IR

Raman đo tán xạ không đàn hồi. Một dao động có hoạt tính Raman khi nó làm thay đổi khả năng phân cực của phân tử.

Một số dao động đối xứng yếu trong IR có thể mạnh trong Raman.

Do hai kỹ thuật có quy tắc chọn khác nhau, IR và Raman thường bổ sung lẫn nhau thay vì thay thế nhau.

Raman đặc biệt hữu ích với nhiều mẫu nước, nhưng huỳnh quang nền có thể che tín hiệu Raman yếu.

## NMR — cấu trúc qua môi trường spin hạt nhân

Một số hạt nhân có spin khác 0. Trong từ trường `B0`, các trạng thái spin bị tách năng lượng. Bức xạ tần số vô tuyến gây chuyển mức giữa chúng.

Các hạt nhân thường dùng gồm `1H`, `13C`, `19F` và `31P`.

### Dịch chuyển hóa học

Electron che chắn hạt nhân khỏi từ trường ngoài. Cấu trúc electron cục bộ làm mỗi hạt nhân cảm nhận một từ trường hiệu dụng khác nhau.

**Dịch chuyển hóa học (chemical shift)** được báo cáo tương đối:

\[
\delta=\frac{\nu-\nu_{ref}}{\nu_{instrument}}\times10^6\;\mathrm{ppm}
\]

Dùng ppm làm giá trị gần độc lập với độ mạnh từ trường thiết bị.

### Tích phân

Trong `1H NMR`, với điều kiện thu phù hợp, diện tích tích phân có thể tỉ lệ với số proton tương đương.

Tuy nhiên trao đổi proton, bão hòa, thời gian thư giãn và chồng tín hiệu có thể làm tích phân đơn giản bị sai.

### Ghép spin–spin

Các hạt nhân lân cận không tương đương có thể tương tác qua liên kết và làm một tín hiệu tách thành **cụm vạch (multiplet)**.

Trong trường hợp bậc một đơn giản, quy tắc `n+1` xuất hiện khi một proton ghép với `n` proton lân cận tương đương.

**Hằng số ghép J** được đo bằng Hz và chứa thông tin cấu trúc; trong nhiều hệ còn phụ thuộc góc nhị diện.

### 13C NMR

`13C` có độ phong phú tự nhiên thấp nên tín hiệu yếu hơn `1H`.

Khử ghép proton băng rộng làm phổ đơn giản hơn, thường gần một tín hiệu cho mỗi carbon không tương đương về môi trường hóa học.

### NMR hai chiều

Khi phổ một chiều quá chật, thí nghiệm 2D tạo thêm chiều tương quan.

- COSY: tương quan proton–proton;
- HSQC: tương quan H–C chủ yếu qua một liên kết;
- HMBC: tương quan H–C qua nhiều liên kết.

Các thí nghiệm này biến xác định cấu trúc thành bài toán dựng lại đồ thị từ nhiều ràng buộc phổ.

## Huỳnh quang

Một phân tử hấp thụ photon, lên trạng thái kích thích, mất một phần năng lượng qua quá trình không bức xạ rồi phát photon năng lượng thấp hơn.

Kết quả thường là **dịch Stokes (Stokes shift)**: bước sóng phát xạ dài hơn bước sóng kích thích.

Huỳnh quang có thể rất nhạy vì photon phát ra được đo trên nền thấp.

Nhưng cường độ còn phụ thuộc hiệu suất lượng tử, dập tắt huỳnh quang, oxygen, nồng độ và hình học thiết bị.

Ở nồng độ cao, **hiệu ứng lọc trong (inner-filter effect)** có thể làm tín hiệu lệch khỏi tuyến tính.

## Phổ nguyên tử

Các phương pháp hấp thụ hoặc phát xạ nguyên tử đo chuyển mức đặc trưng nguyên tố sau khi mẫu được nguyên tử hóa.

### AAS

**Phổ hấp thụ nguyên tử (atomic absorption spectroscopy, AAS)** đo ánh sáng bị hấp thụ bởi nguyên tử trạng thái cơ bản.

Nguồn sáng đặc trưng nguyên tố giúp tăng độ chọn lọc.

### ICP-OES

**Phổ phát xạ quang plasma cảm ứng (ICP-OES)** dùng plasma rất nóng để nguyên tử hóa và kích thích mẫu. Nguyên tử hoặc ion phát các bước sóng đặc trưng, cho phép phân tích nhiều nguyên tố cùng lúc.

### ICP-MS

ICP cũng có thể làm nguồn ion cho MS, kết hợp nguyên tử hóa hiệu quả với khả năng phát hiện nguyên tố và đồng vị rất nhạy.

## Phương pháp tia X

Tia X có bước sóng cùng cỡ khoảng cách nguyên tử trong vật liệu.

### Nhiễu xạ tia X

Giao thoa tăng cường tuân theo quan hệ Bragg:

\[
n\lambda=2d\sin\theta
\]

Mẫu nhiễu xạ mã hóa cấu trúc tuần hoàn của mật độ electron trong tinh thể.

### XPS

**Phổ quang electron tia X (X-ray photoelectron spectroscopy, XPS)** đo động năng electron lõi bị bật ra để suy năng lượng liên kết, thành phần nguyên tố và trạng thái hóa học gần bề mặt.

Cùng dùng tia X nhưng XRD và XPS trả lời những câu hỏi khác nhau vì cơ chế tương tác khác nhau.

## Độ phân giải, băng thông và tỉ số tín hiệu/nhiễu

**Độ phân giải (resolution)** mô tả khả năng phân biệt hai đặc trưng phổ gần nhau.

**Tỉ số tín hiệu/nhiễu (signal-to-noise ratio, SNR)** mô tả mức tín hiệu nổi lên so với nhiễu.

Nếu nhiễu ngẫu nhiên độc lập chiếm ưu thế, lấy trung bình `N` lần quét thường cho:

\[
SNR\propto\sqrt N
\]

Muốn tăng SNR gấp đôi thường phải tăng thời gian đo xấp xỉ bốn lần.

Đây là một trade-off thực nghiệm rất quan trọng giữa **chất lượng dữ liệu và thời gian đo**.

## Hiệu chuẩn và đường nền là một phần của phép đo

Phổ đo được là tổng hợp của:

```text
tín hiệu hóa học thật
+ nền mẫu
+ đáp ứng thiết bị
+ nhiễu
+ xử lý dữ liệu
```

Trôi đường nền, sai hiệu chuẩn bước sóng, đáp ứng bộ phát hiện hoặc trừ nền không phù hợp đều có thể tạo đặc trưng giả.

Vì vậy “phổ đẹp” chưa đủ; cần biết đường xử lý dữ liệu đã được thực hiện như thế nào.

## Kết hợp nhiều kỹ thuật phổ

Một phổ đơn lẻ thường không đủ để chứng minh cấu trúc hữu cơ phức tạp.

Một bộ bằng chứng mạnh có thể gồm:

- IR → nhóm chức;
- UV–Vis → liên hợp và hệ hấp thụ điện tử;
- `1H/13C/2D NMR` → môi trường và kết nối nguyên tử;
- MS → khối lượng, công thức và mảnh;
- XRD đơn tinh thể → cấu trúc 3D trong pha rắn.

Đây là **hợp nhất thông tin (information fusion)**: mỗi kỹ thuật ràng buộc một chiều khác nhau của bản sắc hóa học.

## Ví dụ suy luận: vì sao một dải IR biến mất chưa chắc nhóm chức đã biến mất?

Cường độ IR phụ thuộc thay đổi mômen lưỡng cực trong dao động. Nếu cấu trúc hoặc đối xứng làm chuyển mức rất yếu, dải có thể khó quan sát dù liên kết vẫn tồn tại.

Ngoài ra chồng dải, nền dung môi hoặc nồng độ thấp cũng có thể che tín hiệu.

Do đó cần phân biệt **không quan sát được tín hiệu** với **chứng minh không có cấu trúc**.

## Ví dụ suy luận: vì sao một tín hiệu NMR rộng có thể mang thông tin cơ chế?

Nếu phân tử trao đổi giữa nhiều trạng thái với tốc độ gần thang thời gian NMR, các tín hiệu có thể rộng ra hoặc hợp nhất.

Thay đổi nhiệt độ rồi quan sát độ rộng và vị trí tín hiệu có thể cung cấp thông tin về động học trao đổi, không chỉ về cấu trúc tĩnh.

Phổ học vì vậy có thể thăm dò cả **cấu trúc lẫn động lực học phân tử**.

## Những hiểu lầm thường gặp

### “Một đỉnh cho biết trực tiếp cấu trúc”

Không. Đỉnh chỉ là một chuyển mức quan sát được. Cấu trúc được suy từ tập hợp nhiều ràng buộc.

### “Beer–Lambert luôn tuyến tính”

Không. Nó phụ thuộc nồng độ, dạng tồn tại hóa học và giả định thiết bị.

### “Tần số IR chỉ phụ thuộc loại liên kết”

Không. Liên hợp, ứng suất vòng, liên kết hydrogen và môi trường điện tử đều làm dịch tần số.

### “NMR là ảnh chụp phân tử”

Không. NMR phản ánh môi trường từ và tương tác được lấy trung bình trên thang thời gian của thí nghiệm.

### “Tín hiệu mạnh hơn luôn nghĩa nồng độ cao hơn”

Không. Cường độ còn phụ thuộc hệ số đáp ứng, xác suất chuyển mức, điều kiện thiết bị và xử lý dữ liệu.

## Mô hình tư duy

Hãy xem phổ học như **thăm dò khoảng năng lượng**:

```text
chọn vùng bức xạ
→ ghép với bậc tự do phù hợp
→ tạo chuyển mức / tán xạ
→ đo năng lượng + cường độ + hình dạng
→ suy ràng buộc hóa học
```

Phổ không phải ảnh trực tiếp của phân tử. Nó là tập bằng chứng được tạo bởi quy tắc lượng tử, trạng thái mẫu và thiết bị đo.

Xem tiếp: [Sắc ký](./04_chromatography.md), [Phổ khối](./05_mass_spectrometry.md).