# Tín hiệu tế bào, chu kỳ tế bào và cái chết tế bào — Cell Signaling, Cell Cycle and Cell Death (세포 신호전달, 세포주기, 세포사멸)

Một tế bào không thể chỉ ăn nutrient rồi tự chạy mãi. Nó phải biết môi trường thay đổi ra sao, các tế bào bên cạnh đang làm gì, có đủ nutrient không, DNA có bị hỏng không và có nên phân chia hay dừng lại.

Vì vậy, sự sống cần **cell signaling (truyền tín hiệu tế bào / 세포 신호전달)** và **cell-cycle control (điều khiển chu kỳ tế bào / 세포주기 조절)**.

## Signaling bắt đầu từ một vấn đề rất cơ bản

Một hormone có thể ở ngoài cell nhưng lại làm gene expression bên trong nucleus thay đổi. Làm sao information vượt qua membrane?

Membrane không nhất thiết cho signaling molecule đi vào. Thay vào đó, cell có thể dùng **receptor (thụ thể / 수용체)** để nhận signal và chuyển thông tin sang dạng mà interior của cell hiểu được.

Pattern tổng quát thường là:

```text
signal → receptor → transduction → response
```

Đây là một abstraction rất mạnh. Hormone, neurotransmitter, growth factor và immune signal đều có thể được nhìn bằng pattern này.

## Ligand và receptor

**Ligand (phối tử / 리간드)** là molecule bind vào receptor.

Receptor không chỉ “nhận biết” ligand; binding thường làm receptor đổi conformation. Conformation change đó có thể activate enzyme, mở ion channel hoặc tạo docking site cho protein khác.

Điều quan trọng là specificity không bao giờ tuyệt đối kiểu khóa–chìa cứng nhắc. Binding phụ thuộc shape, charge, concentration và affinity.

## Membrane receptor và intracellular receptor

Hydrophilic signal khó đi qua lipid bilayer nên thường bind **cell-surface receptor**.

Steroid hormone có tính hydrophobic hơn và có thể đi qua membrane, bind **intracellular receptor** trong cytoplasm hoặc nucleus. Receptor–hormone complex có thể trực tiếp ảnh hưởng transcription.

Đây là lý do cùng gọi là “hormone signaling” nhưng mechanism có thể rất khác nhau.

## Signal transduction — biến một tín hiệu thành chuỗi phản ứng

Sau khi receptor được activated, signal thường không đi thẳng tới một target duy nhất. Nó đi qua **signal transduction pathway (경로)**.

Một protein activate protein tiếp theo, rồi tiếp theo nữa. Nhiều pathway dùng **protein phosphorylation**: kinase gắn phosphate, phosphatase tháo phosphate.

Phosphorylation có thể đổi shape, activity hoặc localization của protein.

### Tại sao cascade hữu ích?

Cascade cho ba lợi ích lớn.

Thứ nhất là **amplification**. Một receptor activated có thể activate nhiều molecule downstream, nên signal nhỏ tạo response lớn.

Thứ hai là **control points**. Nhiều stage tạo nơi để pathway bị tăng, giảm hoặc cross-talk với pathway khác.

Thứ ba là **branching**. Một signal có thể tạo nhiều response cùng lúc.

## Second messenger

Một số pathway dùng **second messenger (chất truyền tin thứ hai / 2차 전달자)** như cAMP, Ca²⁺ hoặc IP₃.

Ligand ngoài cell là first messenger. Receptor activate process tạo second messenger bên trong cell.

Second messenger thường nhỏ, khuếch tán nhanh và giúp amplify signal.

Ca²⁺ đặc biệt thú vị vì cell giữ cytosolic Ca²⁺ rất thấp so với extracellular space hoặc ER. Vì vậy mở channel giải phóng Ca²⁺ tạo signal mạnh mà cell có thể tắt bằng pump.

## GPCR — một receptor family cực lớn

**G-protein-coupled receptor (GPCR / G단백질 연결 수용체)** có bảy transmembrane segment điển hình.

Khi ligand bind, receptor activate G protein. G protein sau đó điều khiển enzyme hoặc channel downstream.

Nhiều receptor cho smell, hormone và neurotransmitter thuộc family này.

Điểm đáng học không phải tên của hàng trăm GPCR, mà là architecture: receptor → molecular switch → effector → second messenger.

## Receptor tyrosine kinase

**Receptor tyrosine kinase (RTK / 수용체 티로신 키나아제)** thường dimerize hoặc rearrange khi ligand bind, rồi phosphorylate tyrosine residue.

Phosphorylated site trở thành docking platform cho signaling protein.

Growth factor signaling, cell proliferation và survival thường sử dụng RTK pathway. Mutation làm pathway luôn “on” có thể góp phần vào cancer.

## Cell communication có nhiều khoảng cách

Cell không chỉ gửi hormone toàn cơ thể.

**Autocrine signaling**: cell tác động lên chính nó.

**Paracrine signaling**: signal tác động cell gần đó.

**Endocrine signaling**: hormone đi qua circulation đến target xa.

**Synaptic signaling**: neuron release neurotransmitter vào synapse.

**Direct contact**: membrane protein của hai cell trực tiếp tương tác.

Các category này giúp hiểu spatial organization của multicellular organism.

## Response phụ thuộc context

Cùng một signal có thể tạo response khác ở cell khác vì receptor và downstream machinery khác nhau.

Adrenaline chẳng hạn có thể ảnh hưởng heart cell và liver cell theo cách khác nhau. Không phải hormone “đổi tính chất”, mà target cell đọc signal qua network receptor khác nhau.

> **Mental model:** biological signal không mang toàn bộ meaning bên trong molecule. Meaning xuất hiện từ signal + receptor + trạng thái của receiving cell.

# Từ signaling sang cell cycle

Một multicellular organism lớn lên nhờ cell division, nhưng nếu cell division không được kiểm soát, tissue structure bị phá.

Vì vậy cell phải integrate signal từ nutrient, growth factor, DNA damage và neighboring cell trước khi đi qua các checkpoint.

## Cell cycle là gì?

**Cell cycle (chu kỳ tế bào / 세포주기)** là sequence từ một cell qua growth, DNA replication và division thành daughter cells.

Các phase chính:

- G1: growth và decision có tiếp tục không;
- S: DNA replication;
- G2: chuẩn bị division và kiểm tra;
- M: mitosis + cytokinesis.

Một số cell vào **G0**, trạng thái không tích cực phân chia. G0 có thể temporary hoặc rất lâu tùy cell type.

## Vì sao DNA phải replicate trước mitosis?

Mỗi daughter cell cần genome đầy đủ. Vì vậy DNA được copy trong S phase trước khi chromosome được phân tách.

Sau replication, mỗi chromosome gồm hai **sister chromatids** gần như identical, nối ở centromere region cho đến khi được tách.

Điểm quan trọng: chromosome number và DNA amount không phải cùng một khái niệm. Sau S phase DNA amount tăng gấp đôi nhưng chromosome count theo cách đếm centromere chưa nhất thiết gấp đôi.

## Mitosis — bài toán phân phối genome

**Mitosis (nguyên phân / 유사분열)** tổ chức replicated chromosome rồi phân chúng vào hai nucleus.

Thay vì học tên phase như một chant, hãy nhìn mục tiêu cơ học:

1. chromosome phải condense để dễ vận chuyển;
2. spindle microtubule phải attach đúng chromosome;
3. chromosome phải align sao cho mỗi side nhận một copy;
4. sister chromatid phải tách cùng thời điểm;
5. nucleus và cell phải tái tổ chức.

Các stage prophase, prometaphase, metaphase, anaphase, telophase chỉ là cách chia nhỏ sequence đó.

## Spindle và microtubule

**Mitotic spindle (thoi phân bào / 방추사)** được tạo chủ yếu từ microtubule.

Microtubule attach chromosome qua **kinetochore**, protein structure ở centromere region.

Dynamic polymerization/depolymerization và motor protein tạo force để chromosome di chuyển.

Đây là connection trực tiếp với cytoskeleton ở file trước.

## Checkpoint — cell không chỉ chạy theo clock

Cell cycle có **checkpoint (điểm kiểm soát / 체크포인트)**.

G1/S checkpoint đánh giá growth signal, nutrient và DNA damage trước replication.

G2/M checkpoint đánh giá DNA replication có hoàn tất phù hợp không.

Spindle checkpoint đánh giá chromosome có attach spindle đúng trước anaphase không.

Checkpoint không phải “người kiểm tra” riêng lẻ mà là molecular network.

## Cyclin và CDK — cơ chế của cell-cycle engine

**Cyclin-dependent kinase (CDK / 사이클린 의존성 키나아제)** là kinase điều khiển nhiều transition của cell cycle.

CDK cần bind **cyclin (사이클린)** để active phù hợp. Cyclin concentration tăng giảm theo phase.

Một cách nghĩ: CDK là engine có thể phosphorylate target, còn cyclin là key/context giúp engine active đúng thời điểm.

Protein inhibitor và checkpoint signal có thể block CDK khi điều kiện không an toàn.

## DNA damage và p53

DNA bị damage liên tục bởi replication error, reactive species và environment.

Protein **p53** đóng vai trò major tumor suppressor trong nhiều context. Khi DNA damage được detect, p53 pathway có thể làm cell-cycle arrest, tăng repair response hoặc nếu damage nghiêm trọng dẫn tới apoptosis.

Không nên học “p53 = gene chống ung thư” như definition đơn giản. Mental model chính là p53 nằm trong network quyết định **repair, stop hay die** khi genomic integrity bị đe dọa.

# Cell death — chết cũng có thể là một chương trình sinh học

Cell death không phải lúc nào cũng là accident.

## Apoptosis

**Apoptosis (chết tế bào theo chương trình / 세포자멸사)** là controlled process trong đó cell dismantle chính mình tương đối gọn gàng.

Apoptosis quan trọng trong development, immune system và loại bỏ cell bị damage.

Trong embryo, apoptosis góp phần tạo hình cấu trúc. Immune system có thể loại bỏ cell không còn cần. Cell có DNA damage quá lớn có thể self-destruct để giảm nguy cơ mutation lan truyền.

## Necrosis

**Necrosis (hoại tử / 괴사)** thường liên quan severe injury, membrane rupture và release intracellular content gây inflammation.

Thực tế cell-death biology phức tạp hơn cặp apoptosis/necrosis, có nhiều regulated death pathway. Nhưng distinction này là nền hữu ích.

## Cancer như failure của multicellular cooperation

Cancer không chỉ là “cell phân chia nhanh”. Nó là evolution-like process trong tissue khi cell acquire mutation và epigenetic change giúp bypass normal control.

Cancer cell có thể tăng proliferative signaling, resist growth suppression, avoid cell death, alter metabolism, invade tissue và tương tác với immune system.

Điều đáng hiểu là multicellular organism tồn tại vì cell **cooperate**: phân chia khi cần, ở đúng chỗ, chết khi hỏng. Cancer xuất hiện khi một lineage cell phá dần các rule cooperation đó.

## Common misconceptions

### “Signal mạnh hơn luôn tạo response mạnh hơn vô hạn”

Không. Receptor có thể saturate; pathway có negative feedback; receptor có thể desensitize.

### “Mitosis tạo variation lớn giữa daughter cell”

Thông thường mitosis nhằm tạo genome gần identical. Variation lớn hơn được tạo trong meiosis và mutation.

### “Cell death luôn là điều xấu”

Sai. Programmed cell death là component bình thường của development và tissue maintenance.

### “Cancer là một bệnh duy nhất”

Không. Cancer là nhóm rất lớn disease với tissue origin và molecular mechanism khác nhau, dù có một số hallmarks chung.

## Mental Model

> Cell signaling cho phép cell đọc context; cell cycle cho phép cell nhân bản có kiểm soát; checkpoint và apoptosis bảo vệ integrity của multicellular system. Sự sống ở cấp organism phụ thuộc không chỉ việc từng cell sống, mà việc mỗi cell biết khi nào nên hoạt động, phân chia và dừng lại.

Từ đây ta đã có nền để hỏi một câu lớn hơn: **information nào quyết định protein, receptor và cell behavior?** Câu trả lời bắt đầu từ DNA và gene expression trong [[../02_genetics_molecular_biology/00_dna_genes_and_gene_expression]].