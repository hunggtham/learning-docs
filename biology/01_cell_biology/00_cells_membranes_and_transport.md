# Tế bào, bào quan, màng và vận chuyển — Cells, Organelles, Membranes and Transport (세포, 세포소기관, 막과 수송)

Sau khi đã có molecule, enzyme và energy, ta mới có “nguyên liệu”. Nhưng một đống molecule trong một cốc nước vẫn chưa phải tế bào. Sự sống cần **organization**: các reaction phải được đặt đúng chỗ, nồng độ phải được kiểm soát, molecule phải được đưa qua ranh giới, và những process không tương thích cần được tách ra.

Đó là lý do **tế bào (cell / 세포)** là mental model trung tâm của Sinh học.

## Tế bào giải quyết bốn bài toán cơ bản

Một cell phải đồng thời giải quyết bốn vấn đề:

1. tạo boundary để có “bên trong” riêng;
2. kiểm soát vật chất đi vào và đi ra;
3. tổ chức reaction thành các region hoặc compartment;
4. duy trì information và energy flow.

Nếu thiếu boundary, concentration gradient biến mất. Nếu thiếu transport, cell không lấy được nutrient và không thải waste. Nếu thiếu organization, reaction cạnh tranh lẫn nhau. Nếu thiếu energy và information, structure không thể được duy trì lâu dài.

> **Mental model:** cell là một micro-environment được kiểm soát, không phải một túi nước chứa organelle.

## Prokaryotic cell — nhỏ nhưng không “đơn giản”

**Tế bào nhân sơ (prokaryotic cell / 원핵세포)** gồm Bacteria và Archaea. Chúng không có nucleus được bao bởi membrane.

DNA thường nằm trong vùng gọi là **nucleoid (vùng nhân / 핵양체)**. Ribosome tổng hợp protein nằm trong cytoplasm. Plasma membrane kiểm soát trao đổi. Nhiều bacteria có cell wall giúp giữ shape và chống osmotic stress.

Một bacterium có thể nhỏ hơn nhiều eukaryotic cell nhưng vẫn thực hiện sensing, movement, gene regulation, metabolism và communication. Vì vậy “prokaryote = primitive” là cách hiểu sai.

## Eukaryotic cell — compartmentalization tạo thêm khả năng kiểm soát

**Tế bào nhân thực (eukaryotic cell / 진핵세포)** có nucleus và nhiều organelle được membrane bao quanh.

### Nucleus

**Nucleus (nhân / 핵)** giữ phần lớn DNA của eukaryotic cell. Nuclear envelope tách genome khỏi cytoplasm nhưng có **nuclear pore** kiểm soát RNA và protein đi qua.

Việc tách transcription trong nucleus khỏi translation ngoài cytoplasm giúp eukaryote có thêm tầng regulation.

### Ribosome

**Ribosome (리보솜)** không phải membrane-bound organelle, nhưng là molecular machine cốt lõi. Nó đọc mRNA và nối amino acid thành protein.

Ribosome xuất hiện ở mọi dạng sống đã biết, cho thấy protein synthesis là process rất cổ.

### Endoplasmic reticulum

**Lưới nội chất (endoplasmic reticulum, ER / 소포체)** là mạng membrane.

**Rough ER** có ribosome bám và liên quan đến synthesis protein sẽ được tiết ra ngoài cell, đưa vào membrane hoặc nhiều organelle.

**Smooth ER** tham gia lipid synthesis, detoxification và calcium storage tùy loại cell.

### Golgi apparatus

**Bộ máy Golgi (Golgi apparatus / 골지체)** nhận protein/lipid từ ER, modify, sort và đóng gói chúng vào vesicle.

Một cách hình dung hữu ích là ER tạo nhiều “product”, còn Golgi là trung tâm processing và routing. Nhưng đây chỉ là analogy; trong cell, vesicle traffic rất động và hai hệ thống liên tục tương tác.

### Lysosome

**Lysosome (tiêu thể / 리소좀)** chứa enzyme hoạt động tốt trong môi trường acid. Nó phân giải macromolecule, damaged organelle và material cell đưa vào.

Lysosome không “tiêu mọi thứ bừa bãi” vì enzyme được compartmentalized và pH bên trong khác cytosol.

### Peroxisome

**Peroxisome (과산화소체)** tham gia oxidation của một số fatty acid và detoxification. Reaction trong peroxisome có thể tạo hydrogen peroxide, nên organelle cũng chứa enzyme để xử lý nó.

### Mitochondrion

**Mitochondrion (ty thể / 미토콘드리아)** là nơi phần lớn aerobic cellular respiration ở eukaryote xảy ra.

Mitochondria có double membrane và DNA riêng. Điều này liên quan đến **endosymbiotic theory (thuyết nội cộng sinh / 세포내공생설)**: tổ tiên mitochondria từng là bacterium sống tự do rồi đi vào quan hệ cộng sinh lâu dài với cell khác.

### Chloroplast

Ở plant và algae, **chloroplast (lục lạp / 엽록체)** chuyển light energy thành chemical energy qua photosynthesis. Chloroplast cũng có double membrane và DNA riêng, hỗ trợ endosymbiotic origin tương tự.

## Cytoskeleton — cell không phải túi mềm vô định hình

**Cytoskeleton (bộ xương tế bào / 세포골격)** là network protein filament giúp giữ shape, vận chuyển cargo, tạo movement và phân chia chromosome.

Ba nhóm lớn thường được nhắc là actin filament, intermediate filament và microtubule.

Microtubule hoạt động như track cho motor protein. Actin tham gia shape change, muscle contraction và cell movement. Đây là một ví dụ nơi structure ở nano-scale tạo motion ở cell-scale.

## Surface area to volume ratio — tại sao cell thường nhỏ?

Khi kích thước linear của vật thể tăng, surface area tăng gần theo bình phương còn volume tăng theo lập phương.

Với cube cạnh \(L\):

\[
A=6L^2
\]

\[
V=L^3
\]

Do đó:

\[
\frac{A}{V}=\frac{6}{L}
\]

Khi \(L\) tăng, surface-area-to-volume ratio giảm.

Cell lớn hơn có nhiều volume cần nutrient và waste exchange, nhưng membrane area không tăng nhanh tương ứng. Đây là một reason cell size bị constraint.

Cơ thể lớn giải quyết bằng cách có rất nhiều cell nhỏ và tạo specialized exchange surface như alveoli và intestinal villi.

## Plasma membrane — boundary có tính chọn lọc

**Màng sinh chất (plasma membrane / 세포막)** chủ yếu gồm phospholipid bilayer với protein, cholesterol và carbohydrate.

Phospholipid có hydrophilic head và hydrophobic tail. Trong water, hydrophobic effect làm tail hướng vào nhau và head hướng ra aqueous environment.

Bilayer vừa ổn định vừa fluid. Molecule lipid và nhiều protein có thể di chuyển theo mặt phẳng membrane.

Mô hình này thường gọi là **fluid mosaic model (mô hình khảm lỏng / 유동 모자이크 모델)**.

## Selective permeability — cái gì đi qua được?

Small nonpolar molecule như O₂ và CO₂ có thể diffuse qua lipid bilayer khá dễ.

Ion và phần lớn polar molecule khó qua vì core của bilayer hydrophobic. Chúng thường cần membrane protein.

Điều này biến membrane từ “barrier thụ động” thành một interface có thể regulate exchange.

## Diffusion — từ random motion đến net movement

Molecule trong solution chuyển động ngẫu nhiên. Nếu concentration một phía cao hơn, nhiều molecule sẽ rời phía đó hơn theo thống kê, tạo **net diffusion** xuống concentration gradient.

Diffusion không cần ATP trực tiếp.

Khi equilibrium đạt được, molecule vẫn chuyển động; chỉ là không còn net movement đáng kể giữa hai bên.

## Osmosis — water movement qua membrane

**Osmosis (thẩm thấu / 삼투)** là net movement của water qua selectively permeable membrane do difference về effective solute concentration và water potential.

Ở mức trực giác, phía có nhiều solute không qua membrane thường có ít “free water tendency” hơn, nên water có xu hướng di chuyển về phía đó.

### Tonicity

**Isotonic (đẳng trương / 등장성)**: cell không có net water gain/loss lớn.

**Hypotonic (nhược trương / 저장성)**: environment có effective solute concentration thấp hơn cell; water có xu hướng đi vào.

**Hypertonic (ưu trương / 고장성)**: environment có effective solute concentration cao hơn; water có xu hướng đi ra.

Animal cell trong strongly hypotonic solution có thể swell và lyse. Plant cell có cell wall nên pressure tăng tạo **turgor**, giúp cây đứng vững.

## Facilitated diffusion — đi xuống gradient nhưng cần protein

Một molecule có thể đi xuống concentration gradient nhưng không tự qua lipid bilayer. Khi membrane protein giúp nó đi qua mà không dùng energy trực tiếp, đó là **facilitated diffusion (khuếch tán được hỗ trợ / 촉진확산)**.

Protein có thể là **channel** tạo pore hoặc **carrier** bind molecule rồi đổi conformation.

Glucose transporter là ví dụ carrier; nhiều ion channel cho ion đi theo electrochemical gradient.

## Active transport — đi ngược gradient cần energy

**Active transport (vận chuyển chủ động / 능동수송)** đưa substance theo hướng thermodynamically unfavorable, thường ngược concentration hoặc electrochemical gradient.

### Primary active transport

Protein pump dùng energy trực tiếp, thường từ ATP.

**Na⁺/K⁺ ATPase (나트륨-칼륨 펌프)** ở animal cell dùng ATP để đưa 3 Na⁺ ra và 2 K⁺ vào mỗi cycle điển hình.

Pump giúp duy trì Na⁺ gradient, K⁺ gradient và góp phần vào membrane potential.

### Secondary active transport

Một gradient đã được tạo trước có thể dùng để drive transport chất khác.

Ví dụ, Na⁺ muốn đi vào cell theo electrochemical gradient. Transporter có thể “ghép” dòng Na⁺ này với glucose đi vào, ngay cả khi glucose đi ngược gradient riêng của nó.

Đây là **secondary active transport (2차 능동수송)**.

> **Mental model:** primary active transport dùng energy để “sạc” gradient; secondary transport dùng gradient như một battery để làm work khác.

## Electrochemical gradient và membrane potential

Ion chịu hai lực cùng lúc:

1. chemical gradient do concentration difference;
2. electrical gradient do charge difference.

Tổng hai effect là **electrochemical gradient**.

Cell membrane có **membrane potential (điện thế màng / 막전위)** vì charge không phân bố đều hai phía.

Neuron sẽ khai thác membrane potential để tạo electrical signal. Mitochondria khai thác proton gradient để tạo ATP.

## Endocytosis và exocytosis — khi cargo quá lớn

Protein lớn hoặc particle không thể đi qua channel đơn giản.

**Endocytosis (nhập bào / 세포내섭취)** dùng membrane tạo vesicle đưa material vào cell.

**Exocytosis (xuất bào / 세포외배출)** làm vesicle fuse với plasma membrane để release cargo ra ngoài.

Neuron release neurotransmitter qua exocytosis. Immune cell có thể dùng endocytosis/phagocytosis để uptake pathogen hoặc debris.

## Membrane protein — boundary trở thành interface thông minh

Membrane protein có thể làm transporter, receptor, enzyme, anchor hoặc adhesion molecule.

Một receptor ngoài cell có thể bind hormone; change conformation truyền signal vào trong. Như vậy membrane không chỉ kiểm soát vật chất mà còn kiểm soát **information flow**.

## Common misconceptions

### “Membrane là vỏ cứng bao quanh cell”

Không. Plasma membrane là cấu trúc fluid và dynamic. Protein/lipid liên tục di chuyển, vesicle liên tục fuse và budding.

### “Diffusion dừng khi equilibrium”

Không. Molecular motion vẫn tiếp tục. Equilibrium chỉ có nghĩa net flux bằng khoảng 0.

### “Active transport luôn dùng ATP trực tiếp”

Không. Secondary active transport dùng energy được lưu trong gradient do process khác tạo ra.

### “Mitochondria là nơi duy nhất tạo ATP”

Không. Glycolysis trong cytosol cũng tạo ATP. Mitochondria là nơi tạo phần lớn ATP trong aerobic eukaryotic respiration.

## Mental Model

> Cell là một system được compartmentalize. Membrane tạo boundary; organelle tạo specialized workspace; transporter kiểm soát matter flow; gradient lưu potential energy; receptor đưa information qua boundary.

Từ đây, câu hỏi tự nhiên là: **cell lấy energy ở đâu để duy trì pump, synthesis và repair?** Đó là nội dung của [[01_metabolism_respiration_photosynthesis]].