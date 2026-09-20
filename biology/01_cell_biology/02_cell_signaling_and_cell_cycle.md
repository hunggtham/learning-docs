# Truyền tín hiệu tế bào và chu kỳ tế bào — Cell Signaling and Cell Cycle (세포 신호전달·세포주기)

Một tế bào không chỉ cần metabolism; nó còn phải biết khi nào nên thay đổi hoạt động, khi nào nên phân chia và khi nào nên dừng lại. Truyền tín hiệu tế bào (Cell Signaling / 세포 신호전달) là cách tế bào biến information từ môi trường hoặc từ cell khác thành thay đổi bên trong. Chu kỳ tế bào (Cell Cycle / 세포주기) là chương trình kiểm soát việc tăng trưởng, sao chép DNA và phân chia.

## Từ signal đến response

Một signal có thể là hormone, neurotransmitter, growth factor, light, ion hoặc mechanical force. Signal được receptor nhận biết. Receptor sau đó tạo ra một chuỗi biến đổi gọi là signal transduction pathway.

Ba ý chính thường xuất hiện là reception, transduction và response. Đây không phải ba hộp cứng nhắc mà là ba lớp logic: nhận information, xử lý/khuếch đại information, rồi tạo behavior.

Receptor màng thường cần thiết khi ligand không thể đi qua lipid bilayer. Steroid hormone lại có thể xuyên membrane và gắn intracellular receptor.

## Phosphorylation như một cơ chế switch

Protein kinase (단백질 인산화효소) gắn phosphate lên protein; phosphatase loại phosphate. Phosphorylation có thể thay đổi shape, activity hoặc interaction của protein.

Điều này tạo một loại molecular switch có thể đảo trạng thái nhanh. Trong software, có thể hình dung đây là state transition trong một event-driven system, nhưng biology phức tạp hơn vì cùng một protein có thể có nhiều phosphorylation site và nhiều pathway giao nhau.

## Second messenger và amplification

Các second messenger như cAMP, Ca²⁺ hoặc IP₃ truyền signal bên trong cell. Một receptor được kích hoạt có thể tạo nhiều second messenger, mỗi messenger lại ảnh hưởng nhiều target. Vì vậy một signal ban đầu nhỏ có thể được khuếch đại mạnh.

Calcium là ví dụ đặc biệt. Cytosolic Ca²⁺ thường được giữ ở mức thấp. Khi channel mở, một pulse calcium trở thành signal cho muscle contraction, secretion hoặc gene expression.

> Mental model: signaling là computation bằng molecule. Input được encode thành concentration, localization, phosphorylation state và timing; network xử lý rồi tạo output.

## Feedback và network behavior

Negative feedback giúp ổn định system; positive feedback có thể tạo switch hoặc self-reinforcing response. Insulin–glucose regulation là ví dụ homeostatic negative feedback. Blood clotting chứa nhiều positive-feedback step để response diễn ra nhanh khi vessel bị tổn thương.

Signaling pathway hiếm khi tuyến tính hoàn toàn. Cross-talk giữa pathway khiến cùng một signal có thể tạo response khác nhau trong các cell type khác nhau.

## Chu kỳ tế bào

Eukaryotic cell cycle thường gồm G1, S, G2 và M phase. Trong S phase, DNA được replicate. M phase bao gồm mitosis và cytokinesis. Nhiều cell có thể rời cycle sang G0, nơi chúng không tích cực phân chia.

Cyclin (사이클린) và cyclin-dependent kinase, CDK (사이클린 의존성 키나아제), tạo regulatory engine. Cyclin concentration thay đổi theo cycle; CDK activation giúp đẩy cell qua các transition.

## Checkpoint không phải đồng hồ tuyệt đối

Checkpoint kiểm tra xem điều kiện có phù hợp để chuyển stage hay không. G1/S checkpoint phản ánh growth signal, nutrient và DNA damage. G2/M checkpoint kiểm tra DNA replication. Spindle checkpoint kiểm tra chromosome attachment trước khi sister chromatids tách.

Nếu DNA damage nghiêm trọng, p53 có thể kích hoạt cell-cycle arrest hoặc apoptosis. Đây là cơ chế bảo vệ chống việc truyền lỗi sang daughter cell.

## Mitosis và meiosis khác nhau ở mục tiêu

Mitosis tạo daughter cells gần như giữ nguyên chromosome number, cần cho growth và tissue repair. Meiosis tạo haploid gamete và tạo variation thông qua crossing over và independent assortment.

Meiosis được nối sâu hơn với inheritance trong [[../02_genetics_molecular_biology/01_inheritance_variation_and_mutation]].

## Cancer như failure của regulatory network

Ung thư (Cancer / 암) không phải một bệnh duy nhất mà là nhóm bệnh trong đó cell lineage tích lũy alteration làm tăng proliferation, giảm apoptosis, thay đổi metabolism và có thể xâm lấn tissue.

Oncogene thường là phiên bản hoạt hóa quá mức của gene thúc đẩy growth; tumor suppressor gene thường hạn chế growth hoặc bảo vệ genome. Một mutation đơn lẻ thường chưa đủ; cancer evolution diễn ra qua nhiều step và selection bên trong tissue.

## Common misconceptions

“Cell division càng nhanh càng tốt” là sai. Multicellular organism cần balance giữa growth và control. “Mọi mutation gây cancer” cũng sai; phần lớn mutation là neutral hoặc không đủ để tạo malignant phenotype.

## Kết nối

Signaling dựa trên membrane trong [[00_cells_membranes_and_transport]] và ATP/metabolism trong [[01_metabolism_respiration_photosynthesis]]. Cell cycle phụ thuộc DNA replication và repair, được phát triển ở [[../02_genetics_molecular_biology/00_dna_genes_and_gene_expression]] và [[../02_genetics_molecular_biology/01_inheritance_variation_and_mutation]].
