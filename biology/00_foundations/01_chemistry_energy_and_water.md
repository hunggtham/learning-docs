# Hóa học của sự sống, nước và năng lượng — Chemistry of Life (생명의 화학)

Sinh học không thể tách khỏi hóa học vì mọi cấu trúc sống đều được xây bằng nguyên tử và phân tử. Điều đặc biệt không nằm ở việc sinh vật sử dụng những nguyên tố “khác lạ”, mà ở cách các nguyên tử được liên kết, sắp xếp và trao đổi năng lượng trong những network phản ứng có kiểm soát.

## Carbon tạo ra không gian cấu trúc lớn

Carbon (탄소) có bốn electron hóa trị và thường tạo bốn liên kết cộng hóa trị. Khả năng liên kết với chính nó và với hydrogen, oxygen, nitrogen, sulfur hay phosphorus tạo ra lượng cấu trúc cực lớn. Từ cùng vài nguyên tố có thể xuất hiện glucose, fatty acid, amino acid, nucleotide và hàng triệu organic molecule khác.

Các nhóm chức (Functional Group / 작용기) quyết định nhiều tính chất hóa học của molecule. Hydroxyl làm tăng polarity; carboxyl có thể nhường proton; amino có thể nhận proton; phosphate mang điện tích âm và đặc biệt quan trọng trong ATP, DNA và signaling.

## Nước không chỉ là dung môi

Nước (Water / 물) có hình học phân cực. Oxygen hút electron mạnh hơn hydrogen nên molecule có partial negative charge gần oxygen và partial positive charge gần hydrogen. Từ đó xuất hiện liên kết hydrogen (Hydrogen Bond / 수소 결합), yếu hơn covalent bond nhưng khi có số lượng lớn lại quyết định nhiều hiện tượng sinh học.

Nước có nhiệt dung cao, vì vậy nhiệt độ cơ thể và môi trường nước không biến đổi quá đột ngột. Nó cũng tạo hiệu ứng kỵ nước (Hydrophobic Effect / 소수성 효과): các phần không phân cực có xu hướng tụ lại để giảm diện tích tiếp xúc với nước. Chính cơ chế này giúp phospholipid tự tạo bilayer và protein gấp thành cấu trúc ba chiều.

> Mental model: nước không phải “background”; nó là một participant định hình cấu trúc và động học của hệ sống.

## pH và cân bằng acid–base

pH đo nồng độ ion hydrogen theo thang logarithm:

```math
pH=-\log_{10}[H^+]
```

Nếu `[H⁺]` tăng 10 lần thì pH giảm 1 đơn vị. Scale logarithmic cần thiết vì nồng độ proton trong các hệ sinh học có thể thay đổi qua nhiều bậc độ lớn.

Protein rất nhạy với pH vì điện tích của amino acid side chain thay đổi theo môi trường. Điều đó có thể làm thay đổi cấu trúc và active site của enzyme. Buffer (완충 용액) giúp chống lại biến động pH bằng cách nhận hoặc nhường proton. Máu người duy trì khoảng pH hẹp vì enzyme, ion transport và gas exchange phụ thuộc mạnh vào điều kiện này.

## Bốn nhóm đại phân tử

Carbohydrate (탄수화물) vừa là nguồn năng lượng vừa là vật liệu cấu trúc. Lipid (지질) lưu năng lượng dài hạn, tạo membrane và tham gia signaling. Protein (단백질) thực hiện phần lớn “công việc” của tế bào: enzyme, transport, receptor, motor, structural component. Nucleic acid (핵산), đặc biệt DNA và RNA, lưu trữ và truyền information.

Polymer thường hình thành bằng dehydration reaction và bị tách bằng hydrolysis. Tuy nhiên, không nên học bốn nhóm này như bốn box độc lập. Trong tế bào, glycoprotein, lipoprotein, nucleotide cofactor và membrane complex liên kết chúng thành một network chung.

## Enzyme và năng lượng hoạt hóa

Một phản ứng có thể thuận lợi về thermodynamics nhưng xảy ra cực chậm nếu activation energy cao. Enzyme (효소) làm giảm năng lượng hoạt hóa bằng cách stabilizing transition state, định hướng substrate hoặc tạo microenvironment thích hợp.

Enzyme không “tạo” năng lượng và không thay đổi cân bằng cuối cùng của phản ứng. Nó chỉ giúp hệ đạt cân bằng nhanh hơn. Đây là điểm dễ nhầm.

Tốc độ enzyme thường phụ thuộc vào substrate concentration và có thể được mô hình hóa gần đúng bằng Michaelis–Menten:

```math
v=\frac{V_{max}[S]}{K_m+[S]}
```

Công thức này không phải luật phổ quát cho mọi enzyme, nhưng nó cho intuition quan trọng: khi substrate còn thấp, tăng substrate làm tốc độ tăng rõ; khi enzyme gần bão hòa, tốc độ tiến dần tới `Vmax`.

## Năng lượng tự do và spontaneity

Năng lượng tự do Gibbs (Gibbs Free Energy / 깁스 자유에너지) được viết:

```math
\Delta G=\Delta H-T\Delta S
```

Nếu `ΔG < 0`, process có thể tự phát về thermodynamics trong điều kiện đó. “Tự phát” không có nghĩa “xảy ra nhanh”; một phản ứng vẫn có thể cần enzyme vì kinetic barrier.

Tế bào thường ghép phản ứng không thuận lợi với phản ứng giải phóng năng lượng. ATP là carrier trung tâm trong coupling này. Khi ATP hydrolysis được coupling đúng cách với một process cần năng lượng, tổng `ΔG` của hệ có thể âm.

## ATP không phải pin chứa năng lượng một cách đơn giản

ATP (Adenosine Triphosphate / 아데노신 삼인산) thường được gọi là “energy currency”. Cách nói này hữu ích nhưng dễ khiến người học tưởng năng lượng nằm trong một “liên kết giàu năng lượng” duy nhất. Thực tế, ATP hydrolysis thuận lợi vì products có trạng thái ổn định hơn nhờ resonance, hydration và giảm repulsion giữa các phosphate.

ATP đóng vai trò transfer năng lượng và phosphate group trong những reaction network nhanh. Fat là kho năng lượng dài hạn tốt hơn nhiều.

## Thermodynamics và sự sống

Entropy của riêng một tế bào có thể giảm khi nó xây cấu trúc phức tạp, nhưng tổng entropy của hệ gồm tế bào và môi trường vẫn tăng. Tế bào duy trì order bằng cách tiêu thụ free energy và thải heat.

Điều này giải thích tại sao homeostasis luôn có cost. Gradient ion qua membrane, protein folding, DNA repair và muscle contraction đều đòi hỏi năng lượng trực tiếp hoặc gián tiếp.

## Kết nối

Những nguyên lý ở đây được dùng trực tiếp trong [[../01_cell_biology/00_cells_membranes_and_transport]] và [[../01_cell_biology/01_metabolism_respiration_photosynthesis]]. pH, enzyme kinetics và free-energy coupling cũng trở lại trong physiology và biotechnology.
