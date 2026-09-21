# Phonon, khuyết tật, kích thích tập thể và vật chất tô pô

## Tinh thể không phải một mạng nguyên tử đứng yên

Trong mô hình dải năng lượng đơn giản, các ion thường được vẽ như những điểm mạng cố định. Nhưng ở nhiệt độ hữu hạn, nguyên tử dao động quanh vị trí cân bằng. Vì các nguyên tử liên kết với nhau, những dao động này không phải `N` dao động tử hoàn toàn độc lập.

Nếu tuyến tính hóa lực quanh trạng thái cân bằng và chéo hóa hệ dao động ghép, ta thu được các mode chuẩn. Trong cơ học lượng tử, năng lượng của mỗi mode bị lượng tử hóa. Lượng tử của dao động mạng được gọi là **phonon (포논)**.

Phonon không phải một loại nguyên tử mới. Nó là quasiparticle: cách đóng gói một kích thích tập thể của rất nhiều nguyên tử thành một đối tượng hiệu dụng có năng lượng và động lượng tinh thể.

## Nhánh acoustic và optical phonon

Với ô cơ sở chỉ có một nguyên tử, nhánh tần số thấp thường là nhánh âm học (acoustic). Khi

```math
k\to0,
```

các nguyên tử lân cận dao động gần cùng pha và

```math
\omega\to0.
```

Ở bước sóng dài,

```math
\omega\approx v_s k,
```

trong đó `v_s` là vận tốc âm trong tinh thể.

Nếu ô cơ sở có nhiều nguyên tử, có thể xuất hiện nhánh quang học (optical), nơi các mạng con dao động tương đối với nhau. Một số mode quang học ghép mạnh với bức xạ hồng ngoại hoặc tán xạ Raman.

## Mô hình Debye và nhiệt dung mạng

Định lý phân bố đều cổ điển dự đoán nhiệt dung mạng ở nhiệt độ cao gần

```math
C_V\approx3Nk_B.
```

Nhưng ở nhiệt độ thấp, dự đoán này thất bại.

Mô hình Debye xem phổ phonon âm học gần liên tục đến một tần số cắt `\omega_D` và dự đoán

```math
C_V\propto T^3
```

ở nhiệt độ thấp.

Nguyên nhân là thống kê lượng tử làm các mode tần số cao khó được kích thích khi `k_BT` nhỏ hơn năng lượng lượng tử của chúng.

Đây là một trong những thành công sớm cho thấy tính chất nhiệt của chất rắn phải được hiểu bằng các kích thích lượng tử tập thể.

## Electron–phonon scattering và điện trở

Trong mạng tuần hoàn hoàn hảo, electron Bloch không thể được hình dung đơn giản như viên bi liên tục va vào từng ion. Tính tuần hoàn đã được xây vào trạng thái Bloch.

Điện trở xuất hiện khi tính tuần hoàn bị phá hoặc khi electron trao đổi động lượng với:

- phonon;
- tạp chất;
- khuyết tật;
- biên mẫu;
- các excitation khác.

Ở nhiệt độ hữu hạn, số phonon nhiệt tăng và electron–phonon scattering thường làm điện trở kim loại tăng.

Khi làm lạnh, số phonon giảm và điện trở của kim loại tinh khiết giảm cho tới khi tán xạ do tạp chất hoặc biên chi phối phần điện trở dư.

Quy tắc Matthiessen đôi khi xấp xỉ điện trở tổng bằng tổng các cơ chế độc lập, nhưng không phải định luật chính xác trong mọi vật liệu.

## Khuyết tật là một phần bình thường của vật liệu thật

Tinh thể hoàn hảo là mô hình lý tưởng. Vật liệu thực có thể chứa:

- vacancy: thiếu nguyên tử ở một nút mạng;
- interstitial: nguyên tử nằm ở vị trí xen kẽ;
- substitutional impurity: nguyên tử khác thay nguyên tử nền;
- dislocation: khuyết tật đường;
- grain boundary: biên giữa các hạt tinh thể có hướng khác nhau.

Khuyết tật không nhất thiết là “xấu”.

Pha tạp bán dẫn cố ý đưa impurity vào để điều khiển mật độ hạt tải. Dislocation chi phối biến dạng dẻo của kim loại. Color center tạo trạng thái quang học. Grain boundary ảnh hưởng độ bền, khuếch tán và độ dẫn.

## Dislocation và biến dạng dẻo

Nếu phải trượt toàn bộ một mặt phẳng nguyên tử hoàn hảo đồng thời, ứng suất cần thiết rất lớn.

Dislocation cho phép sự trượt tiến triển cục bộ từng bước, làm ứng suất cần thiết nhỏ hơn nhiều bậc độ lớn.

Biến cứng (work hardening) xảy ra khi biến dạng làm mật độ dislocation tăng và các dislocation cản trở chuyển động của nhau.

Ủ nhiệt (annealing) có thể làm khuyết tật tái sắp xếp hoặc giảm mật độ.

Vì vậy tính cơ học vĩ mô của kim loại nổi lên từ cấu trúc và động lực của các khuyết tật vi mô.

## Quasiparticle: electron trong vật liệu không còn là electron “trần”

Trong vật liệu tương tác, một electron làm phân cực môi trường và liên hệ với nhiều bậc tự do khác.

Ở năng lượng thấp, ta thường mô tả excitation bằng quasiparticle có:

- khối lượng hiệu dụng `m^*`;
- thời gian sống hữu hạn;
- điện tích hoặc moment hiệu dụng;
- quan hệ tán sắc đã được tái chuẩn hóa.

Electron dải, lỗ trống, phonon, magnon và exciton đều là ví dụ quasiparticle theo những nghĩa khác nhau.

Ý tưởng này lặp lại xuyên suốt vật lý: mô hình ở đúng thang không nhất thiết dùng đối tượng cơ bản nhất của tự nhiên.

## Magnon và tính từ tập thể

Trong sắt từ, dao động tập thể của spin tạo spin wave. Lượng tử của spin wave được gọi là magnon (마그논).

Miền từ hình thành để giảm năng lượng từ tĩnh; domain wall là cấu trúc mở rộng phân cách các miền.

Công nghệ bộ nhớ khai thác việc chuyển trạng thái từ, còn spintronics sử dụng spin bên cạnh điện tích như một bậc tự do mang thông tin.

## Pha tô pô: khi cấu trúc toàn cục quan trọng hơn tham số trật tự cục bộ

Phân loại pha truyền thống thường dựa trên phá vỡ đối xứng và tham số trật tự.

Tuy nhiên, hiệu ứng Hall lượng tử và chất cách điện tô pô cho thấy hai pha có thể có cùng đối xứng cục bộ nhưng khác nhau bởi một bất biến tô pô.

Trong hiệu ứng Hall lượng tử nguyên,

```math
\sigma_{xy}=\nu\frac{e^2}{h},
```

với `\nu` là số nguyên trong chế độ lý tưởng.

Độ bền của lượng tử hóa liên hệ với topology của các trạng thái lượng tử đã chiếm, chứ không chỉ với từng tham số vật liệu vi mô.

## Bulk–boundary correspondence

Nếu hai vùng bulk thuộc hai lớp tô pô khác nhau, biên giữa chúng không thể luôn được biến đổi trơn từ pha này sang pha kia mà vẫn giữ gap và symmetry bảo vệ.

Do đó biên có thể bắt buộc chứa các trạng thái đặc biệt.

Đây là **bulk–boundary correspondence**: bất biến tô pô của bulk dự đoán cấu trúc trạng thái ở biên.

## Chất cách điện tô pô

Topological insulator có bulk cách điện nhưng có trạng thái dẫn ở bề mặt hoặc cạnh trong điều kiện phù hợp.

Từ “được bảo vệ” không có nghĩa hoàn toàn không tán xạ. Nó nghĩa một số cơ chế mở gap hoặc backscattering bị cấm hoặc suy giảm nếu symmetry bảo vệ và cấu trúc gap vẫn còn.

Nhiệt độ, tạp chất từ, tiếp xúc, tương tác và hình học mẫu vẫn có thể làm transport thực khác lý tưởng.

## Vật liệu hai chiều và giảm số chiều

Graphene, transition-metal dichalcogenide và các vật liệu lớp cho thấy giảm số chiều thay đổi mạnh:

- mật độ trạng thái;
- screening;
- exciton;
- dao động nhiệt;
- khả năng xuất hiện các pha tập thể.

Trong graphene, phổ năng lượng gần điểm Dirac gần tuyến tính. Quasiparticle năng lượng thấp có thể được mô tả bằng Hamiltonian giống Dirac.

Đây là phát biểu hiệu dụng ở năng lượng thấp, không có nghĩa electron cơ bản mất khối lượng nghỉ trong chân không.

## Siêu dẫn như trạng thái lượng tử tập thể

Trong bức tranh BCS truyền thống, tương tác electron–phonon có thể tạo lực hút hiệu dụng giữa electron gần mặt Fermi, hình thành cặp Cooper.

Các cặp tạo trạng thái kết hợp có gap năng lượng.

Siêu dẫn không chỉ là “điện trở bằng 0”. Hiệu ứng Meissner cho thấy từ trường bị đẩy khỏi bulk trong điều kiện thích hợp, chứng minh đây là một pha nhiệt động riêng biệt.

Lượng tử hóa từ thông và hiệu ứng Josephson phản ánh tính kết hợp pha lượng tử ở quy mô vĩ mô.

## Tính toán vật liệu và kỹ thuật thiết bị

Các phương pháp như Density Functional Theory (DFT), molecular dynamics, Monte Carlo và tight-binding giúp dự đoán hoặc giải thích vật liệu.

Nhưng từ band structure lý tưởng tới thiết bị thật còn phải xét:

- khuyết tật;
- interface;
- contact;
- phonon;
- strain;
- vận chuyển không cân bằng.

Đó là lý do vật lý chất rắn, khoa học vật liệu, kỹ thuật bán dẫn và vật lý tính toán chồng lấn sâu.

## Liên hệ với Hóa học và Kỹ thuật vật liệu

Năng lượng liên kết hóa học quyết định cấu trúc tinh thể và độ cứng cục bộ; cấu trúc điện tử quyết định band, bonding và phản ứng bề mặt.

Khuyết tật, pha tạp và grain boundary là nơi vật lý và hóa học gặp nhau: cùng một nguyên tử tạp có thể thay mật độ hạt tải, năng lượng hình thành khuyết tật và độ ổn định pha.

Trong kỹ thuật, mục tiêu hiếm khi là “tinh thể hoàn hảo nhất”. Mục tiêu là cấu trúc vi mô tạo đúng cơ tính, điện tính, nhiệt tính hoặc quang tính cần thiết.

## Miền áp dụng và giới hạn

Phonon là quasiparticle tốt khi dao động mạng có thể được mô tả gần điều hòa và mode có thời gian sống đủ dài.

Ở nhiệt độ cao hoặc phi điều hòa mạnh, phonon–phonon scattering và biến đổi cấu trúc có thể làm bức tranh quasiparticle đơn giản kém chính xác.

Khối lượng hiệu dụng cũng chỉ có ý nghĩa trong vùng `k` nơi dispersion có thể xấp xỉ phù hợp. Topological protection luôn phụ thuộc gap, symmetry và loại nhiễu loạn.

## Mô hình tư duy (Mental Model)

Chất rắn không phải “một đống nguyên tử đứng đúng hàng”. Nó là hệ nhiều hạt có mode tập thể, khuyết tật, quasiparticle và cấu trúc toàn cục của hàm sóng.

Ở đúng thang đo, phonon hoặc electron dải có thể là đối tượng hữu ích hơn rất nhiều so với theo dõi từng hạt nhân và electron cơ bản.

```text
microscopic atoms + electrons
→ lattice + bands
→ collective modes / quasiparticles
→ defects + interactions
→ macroscopic material properties
→ device behavior
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Phonon là một hạt vật chất nhỏ nằm giữa các nguyên tử”

Không. Phonon là lượng tử của mode dao động mạng và không tồn tại như hạt tự do ngoài vật liệu.

### “Khuyết tật luôn làm vật liệu kém đi”

Không. Nhiều công nghệ cần pha tạp hoặc khuyết tật có kiểm soát.

### “Topological protection nghĩa điện trở luôn bằng 0”

Không. Bảo vệ chỉ áp dụng cho những mode và quá trình cụ thể dưới các giả định symmetry/gap nhất định.

### “Band structure lý tưởng đủ để dự đoán thiết bị thật”

Không. Interface, contact, disorder, phonon và vận chuyển không cân bằng có thể chi phối thiết bị.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Tinh thể và dải năng lượng](00_crystals_bands.md), [Thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md), [Hiện tượng tới hạn](../04_thermal_statistical/05_critical_phenomena_renormalization.md).

**Liên hệ tiếp:** [Bán dẫn và thiết bị](01_semiconductors_devices.md), [Vận chuyển và siêu dẫn](02_transport_magnetism_superconductivity.md), [BEC và siêu chảy](05_bec_superfluid_quantum_fluids.md), [Berry phase và Hall lượng tử](06_berry_phase_quantum_hall_topology.md).
