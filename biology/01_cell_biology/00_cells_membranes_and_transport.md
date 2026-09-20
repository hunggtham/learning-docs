# Tế bào, màng và vận chuyển — Cells, Membranes and Transport (세포·세포막·수송)

Tế bào (Cell / 세포) là đơn vị nhỏ nhất có thể tự duy trì nhiều đặc tính cốt lõi của sự sống. Hiểu tế bào không nên bắt đầu bằng việc học thuộc tên bào quan, mà bằng một vấn đề: làm thế nào một hệ hóa học có thể giữ được “bên trong” khác “bên ngoài”, kiểm soát vật chất đi qua biên giới, tạo năng lượng và tổ chức hàng nghìn phản ứng cùng lúc?

## Hai chiến lược tổ chức lớn

Tế bào nhân sơ (Prokaryotic Cell / 원핵세포) không có nucleus được bao bởi membrane và thường có genome dạng circular chromosome nằm trong nucleoid. Bacteria và Archaea thuộc nhóm này. Tế bào nhân thực (Eukaryotic Cell / 진핵세포) có nucleus và nhiều membrane-bound organelles như mitochondria, endoplasmic reticulum và Golgi apparatus.

Khác biệt này không có nghĩa prokaryote “nguyên thủy và đơn giản” theo nghĩa kém tinh vi. Bacteria có regulatory network, membrane system, quorum sensing và metabolic diversity rất cao. Eukaryote đổi lại complexity bằng compartmentalization: chia không gian thành các vùng có chemistry khác nhau.

## Màng tế bào tạo ra một thế giới bên trong

Màng sinh chất (Plasma Membrane / 세포막) chủ yếu gồm phospholipid bilayer cùng protein, cholesterol và carbohydrate. Phospholipid có đầu ưa nước và đuôi kỵ nước. Trong nước, cấu trúc bilayer hình thành tự phát do hydrophobic effect.

Màng không phải bức tường kín. Nó là selective barrier. Các molecule nhỏ không phân cực như O₂ và CO₂ đi qua dễ hơn ion hoặc molecule phân cực lớn. Protein màng cung cấp channel, transporter, receptor và enzyme.

> Mental model: membrane là một API boundary của tế bào. Không phải mọi thứ được phép đi qua; entry, exit và signaling đều qua những interface có rule.

## Khuếch tán và gradient

Khuếch tán (Diffusion / 확산) là chuyển động ròng của particle từ vùng concentration cao sang thấp do chuyển động nhiệt ngẫu nhiên. Không có “molecule biết đường đi xuống gradient”; direction ở cấp hệ xuất hiện từ probability.

Nếu một molecule cần protein channel nhưng vẫn đi theo electrochemical gradient, đó là khuếch tán được hỗ trợ (Facilitated Diffusion / 촉진 확산). Quá trình này không trực tiếp tiêu ATP.

Với ion, concentration gradient chưa đủ. Điện tích màng cũng tác động, nên ta nói gradient điện hóa (Electrochemical Gradient / 전기화학적 기울기).

## Osmosis và nước

Thẩm thấu (Osmosis / 삼투) là movement của nước qua semipermeable membrane theo chênh lệch water potential. Trong cách nói đơn giản, nước có xu hướng đi về phía có nồng độ solute không thấm qua màng cao hơn.

Khái niệm isotonic, hypotonic và hypertonic mô tả ảnh hưởng của dung dịch lên cell volume. Animal cell trong hypotonic solution có thể trương và lyse; plant cell có cell wall nên turgor pressure lại là điều cần thiết để cây đứng vững.

## Active transport và gradient như một dạng năng lượng

Vận chuyển chủ động (Active Transport / 능동수송) di chuyển substance ngược gradient và cần energy. Na⁺/K⁺ ATPase ở animal cell dùng ATP để bơm 3 Na⁺ ra và 2 K⁺ vào mỗi cycle. Gradient này sau đó được dùng cho electrical signaling, nutrient transport và cell volume.

Đây là ví dụ của energy coupling. ATP không trực tiếp “đẩy” mọi molecule; nó tạo gradient, rồi gradient được tái sử dụng. Secondary active transport như sodium-glucose symporter khai thác chính cơ chế này.

## Bào quan như các reaction environment

Nucleus giữ phần lớn genomic DNA. Ribosome thực hiện translation. Rough ER xử lý nhiều protein đi vào secretory pathway; smooth ER tham gia lipid synthesis và calcium storage. Golgi sửa đổi, sort và đóng gói cargo. Lysosome chứa enzyme phân giải trong môi trường acidic. Mitochondrion thực hiện phần lớn aerobic ATP production.

Không nên xem organelle như những “phòng ban” tách biệt hoàn toàn. Chúng liên kết bằng vesicle traffic, contact sites, cytoskeleton và signaling. Mitochondria cũng giao tiếp với nucleus để điều chỉnh metabolism và stress response.

## Cytoskeleton và hình học động

Bộ xương tế bào (Cytoskeleton / 세포골격) gồm microfilament, intermediate filament và microtubule. Nó duy trì shape, vận chuyển cargo và tham gia division. Motor protein như kinesin, dynein và myosin biến chemical energy thành mechanical movement.

Ở đây biology nối trực tiếp với physics: movement phát sinh từ force, binding kinetics, Brownian motion và molecular conformational change.

## Surface area và giới hạn kích thước

Khi kích thước cell tăng, volume tăng theo lập phương chiều dài, còn surface area chỉ tăng theo bình phương. Nếu cell quá lớn, membrane area không tăng đủ nhanh so với nhu cầu trao đổi của cytoplasm.

Với sphere bán kính `r`:

```math
\text{Surface area}=4\pi r^2,\qquad \text{Volume}=\frac{4}{3}\pi r^3
```

Do đó:

```math
\frac{SA}{V}=\frac{3}{r}
```

Tỷ lệ giảm khi `r` tăng. Đây là lý do nhiều cell nhỏ hiệu quả hơn một cell khổng lồ, và vì sao intestine, lung hay root tạo fold/branch để tăng area.

## Endosymbiosis

Lý thuyết nội cộng sinh (Endosymbiotic Theory / 세포내공생설) giải thích mitochondria và chloroplast có nguồn gốc từ bacteria từng sống trong ancestor cell. Bằng chứng gồm double membrane, circular DNA, bacterial-like ribosome và cách division tương tự binary fission.

## Common misconceptions

“Mọi chất đi từ nơi nhiều sang nơi ít” không đúng khi có active transport, electrical gradient hoặc reaction liên tục tiêu thụ sản phẩm. “Màng chỉ là lớp lipid” cũng sai vì phần lớn specificity của transport và signaling đến từ protein màng.

## Kết nối

Cell boundary tạo nền cho [[01_metabolism_respiration_photosynthesis]] vì respiration và photosynthesis phụ thuộc vào membrane gradient. Receptor trên màng dẫn sang [[02_cell_signaling_and_cell_cycle]]. DNA trong nucleus và protein synthesis nối trực tiếp tới [[../02_genetics_molecular_biology/00_dna_genes_and_gene_expression]].
