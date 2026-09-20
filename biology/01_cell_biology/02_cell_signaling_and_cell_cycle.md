# Truyền tín hiệu và chu kỳ tế bào — Cell Signaling and Cell Cycle (세포 신호전달과 세포주기)

Chương trước kết thúc bằng một câu hỏi: metabolism phải được regulation, vậy cell **biết** lúc nào cần tăng hay giảm activity bằng cách nào? Một liver cell phải phản ứng với insulin khác một neuron; một immune cell phải nhận ra tín hiệu nguy hiểm; một cell đang thiếu nutrient có thể dừng division. Tất cả những việc đó yêu cầu một hệ nhận tín hiệu, truyền tín hiệu và thay đổi response.

Vì vậy signaling không phải một chủ đề đứng ngoài metabolism. Nó là layer control nằm trên metabolism, transport, gene expression và cell division.

## 1. Từ stimulus đến response

Một **signal (tín hiệu / 신호)** chỉ có ý nghĩa khi cell có machinery để nhận và diễn giải nó.

Một hormone trong blood có thể đi qua rất nhiều tissue, nhưng chỉ cell có receptor phù hợp mới phản ứng mạnh. Vì vậy specificity không nhất thiết nằm ở signal; nó có thể nằm ở receptor và downstream network.

Flow cơ bản:

```text
signal
  ↓
receptor
  ↓
signal transduction
  ↓
change in enzyme / ion / gene expression
  ↓
cellular response
```

Đây là cùng logic sensor → controller → actuator đã gặp ở feedback control.

## 2. Receptor: biến thông tin ngoài cell thành state bên trong

Có hai family lớn cần phân biệt.

Nếu ligand không dễ qua membrane, receptor thường nằm trên plasma membrane. Ligand bind ngoài cell làm protein đổi conformation ở trong cell.

Nếu ligand nhỏ và lipid-soluble, như steroid hormone, nó có thể đi qua membrane và bind intracellular receptor, sau đó complex tác động lên gene expression.

Điểm lớn không phải học thuộc loại hormone nào. Hãy hỏi: **signal có qua bilayer được không?** Chemistry của molecule quyết định architecture signaling phù hợp.

## 3. Signal transduction: vì sao không nối receptor trực tiếp tới mọi response?

Một receptor có thể activate nhiều protein downstream. Việc có nhiều bước trung gian mang ba lợi ích.

Thứ nhất, **amplification**. Một receptor active có thể activate nhiều molecule tiếp theo.

Thứ hai, **integration**. Một protein downstream có thể nhận input từ nhiều pathway.

Thứ ba, **branching**. Một signal có thể đồng thời đổi metabolism, cytoskeleton và gene expression.

Vì vậy signaling pathway thường là network hơn là line thẳng.

## 4. Phosphorylation: một switch hóa học tái sử dụng nhiều lần

Protein kinase gắn phosphate vào protein; phosphatase tháo phosphate.

Phosphorylation có thể làm protein đổi shape, localization hoặc binding partner.

Điểm quan trọng là phosphate không phải “on” trong mọi case. Có protein được activate khi phosphorylated, có protein bị inhibited.

Mental model đúng là:

> phosphorylation là một cách **thay đổi state** của protein nhanh và reversible.

## 5. Second messenger: small molecule truyền signal trong cell

Một số receptor activate molecule nhỏ như cAMP, IP₃ hoặc Ca²⁺.

**Second messenger (chất truyền tin thứ hai / 2차 전달자)** giúp signal lan nhanh và amplify.

Ca²⁺ đặc biệt thú vị. Cytosolic Ca²⁺ bình thường được giữ thấp. Khi channel mở, Ca²⁺ tăng nhanh và bind protein sensor. Vì baseline thấp, một increase nhỏ về absolute amount có thể tạo signal rõ.

Đây là ví dụ khác của principle gradient: cell tạo chênh lệch trước, rồi khai thác chênh lệch như information.

## 6. Feedback trong signaling

Pathway signaling thường tự điều chỉnh.

Negative feedback giúp signal không kéo dài quá mức. Positive feedback có thể tạo switch-like transition.

Ví dụ trong cell cycle, một số kinase activate process dẫn tới activation mạnh hơn của chính network, giúp cell chuyển dứt khoát từ stage này sang stage khác.

Điều này cho thấy feedback không chỉ giữ stability; đôi khi nó giúp system chuyển state.

## 7. Cell phải quyết định khi nào divide

Division tốn resource và tạo risk. DNA phải được copy chính xác, chromosome phải segregate đúng, cell phải đủ lớn và environment phải cho phép.

Do đó cell cycle không thể là clock chạy tự động.

**Cell cycle (chu kỳ tế bào / 세포주기)** ở eukaryote thường được mô tả bằng G1, S, G2 và M.

- G1: growth và kiểm tra condition;
- S: DNA replication;
- G2: preparation và kiểm tra sau replication;
- M: mitosis + cytokinesis.

Nhưng ý quan trọng hơn tên phase là: mỗi transition cần control logic.

## 8. Checkpoint: không phải một “cổng” vật lý

**Checkpoint (điểm kiểm soát / 체크포인트)** là network đánh giá condition trước khi cell tiến sang state tiếp.

Ví dụ, DNA damage có thể activate pathway làm cell cycle arrest để repair. Nếu damage không sửa được, cell có thể đi vào senescence hoặc apoptosis.

Checkpoint vì thế nối signaling với genome integrity.

## 9. Cyclin và CDK: logic của state transition

**Cyclin-dependent kinase (CDK)** là kinase điều khiển nhiều event của cell cycle. CDK activity phụ thuộc cyclin, mà cyclin amount thay đổi theo thời gian.

Cyclin được synthesized rồi degraded theo sequence, tạo oscillation.

Ta có một control loop:

```text
cyclin accumulation
   ↓
CDK activation
   ↓
cell-cycle events
   ↓
cyclin destruction
   ↓
CDK activity falls
```

Cell cycle vì thế là một dynamical system, không chỉ danh sách stage.

## 10. Mitosis: bài toán phân chia thông tin đã copy

Sau S phase, mỗi chromosome đã được duplicated thành sister chromatids.

Mitosis phải đảm bảo mỗi daughter cell nhận một copy.

Spindle microtubule attach chromosome qua kinetochore. Chromosome alignment và tension được monitored. Khi condition phù hợp, sister chromatids tách và đi về hai pole.

Cytoskeleton đã học ở chapter membrane/organization giờ trở thành machine cơ học cho chromosome segregation.

## 11. Meiosis: division phục vụ sexual reproduction

Meiosis khác mitosis vì mục tiêu không phải tạo hai cell giống nhau, mà giảm chromosome number và tạo variation cho gamete.

Một diploid cell trải qua một round DNA replication nhưng hai round division.

Homologous chromosome pair trong meiosis I và có thể crossing-over. Điều này tạo recombination.

Vì vậy meiosis là bridge trực tiếp từ cell cycle sang genetics.

## 12. Apoptosis: chết có chương trình là một phần của multicellular life

Một multicellular organism không chỉ cần cell growth; nó cần loại bỏ cell đúng lúc.

**Apoptosis (chết tế bào theo chương trình / 세포자멸사)** là process regulated, khác với cell rupture hỗn loạn.

Trong development, apoptosis giúp sculpt structure. Trong immunity, nó loại bỏ một số cell không cần nữa. Khi DNA damage quá lớn, apoptosis có thể ngăn cell nguy hiểm tiếp tục division.

Đây là một ví dụ nghịch lý thú vị: ở organism đa bào, survival của whole system đôi khi đòi hỏi death của component cell.

## 13. Cancer: khi growth control bị phá vỡ

Cancer không phải “cell tăng trưởng nhanh” đơn giản. Nó là evolutionary process ở cell population trong body.

Mutation có thể activate growth-promoting pathway, disable tumor suppressor, giảm apoptosis hoặc tăng genomic instability. Cell có advantage proliferative sẽ expand clone.

Qua nhiều round selection trong tissue environment, tumor có thể tích lũy thêm trait.

Như vậy cancer nối signaling, cell cycle, mutation và evolution.

## 14. Signaling không chỉ điều khiển division

Insulin signaling đổi glucose uptake và metabolism. Growth factor đổi proliferation. Neurotransmitter đổi ion channel. Cytokine đổi immune state. Hormone steroid đổi transcription.

Cùng architecture receptor → transduction → response được tái sử dụng ở nhiều scale.

Đây là lý do học signaling một lần tốt sẽ giúp physiology dễ hơn rất nhiều.

## 15. Cross-talk: pathway không sống trong sơ đồ riêng

Textbook thường vẽ pathway thành các line riêng để dễ đọc. Trong cell thật, pathway cross-talk.

Một kinase có thể được activate bởi nhiều upstream signal. Một transcription factor có thể nhận input từ stress và hormone. Metabolic state có thể ảnh hưởng signaling qua ATP/AMP ratio.

Do đó response của cell phụ thuộc **context**, không chỉ ligand.

## 16. Từ signaling sang genetics: response dài hạn cần information system

Nhiều cellular response ngắn hạn chỉ đổi state protein hiện có. Nhưng nếu cell muốn thay đổi lâu hơn, nó thường thay đổi gene expression.

Ví dụ hormone có thể làm tăng transcription enzyme; differentiation thay đổi hàng trăm gene; immune activation đổi expression program.

Do đó câu hỏi tiếp theo trở thành:

**Gene là gì? DNA lưu information bằng cách nào? Cell copy DNA ra sao? Sequence DNA được chuyển thành RNA và protein như thế nào?**

Cell signaling đã đưa ta tới molecular genetics một cách tự nhiên.

Tiếp tục với [[../02_genetics_molecular_biology/00_dna_genes_and_gene_expression]].