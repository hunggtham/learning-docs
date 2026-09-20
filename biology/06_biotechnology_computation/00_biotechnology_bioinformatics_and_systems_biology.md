# Công nghệ sinh học, tin sinh học và systems biology — Biotechnology, Bioinformatics and Systems Biology (생명공학·생물정보학·시스템생물학)

Công nghệ sinh học (Biotechnology / 생명공학) sử dụng organism, cell hoặc biomolecule để tạo sản phẩm, đo lường hệ sống hoặc thay đổi biological process. Tin sinh học (Bioinformatics / 생물정보학) dùng algorithm, statistics và computation để phân tích biological data. Systems biology (시스템생물학) cố hiểu behavior của whole network thay vì chỉ từng component riêng lẻ.

## PCR: khuếch đại một vùng DNA

Polymerase chain reaction, PCR (중합효소연쇄반응), giải quyết một bài toán cơ bản: nếu ta chỉ có lượng DNA rất nhỏ, làm sao tạo đủ copy để đo hoặc phân tích?

PCR lặp lại ba pha chính. Denaturation tách hai DNA strand bằng nhiệt. Annealing cho primer gắn vào sequence bổ sung. Extension dùng thermostable DNA polymerase kéo dài strand mới.

Sau mỗi cycle lý tưởng, số copy target gần gấp đôi. Nếu efficiency là 100%, sau `n` cycle số copy xấp xỉ:

```math
N_n=N_0 2^n
```

Đây là exponential growth. Trong thực tế efficiency thấp hơn và reaction dần plateau do reagent limitation và by-product.

## Gel electrophoresis

DNA mang điện tích âm nhờ phosphate backbone. Trong electric field, DNA di chuyển qua gel về phía electrode dương. Fragment nhỏ đi qua matrix dễ hơn nên di chuyển xa hơn fragment lớn.

Gel không “đọc sequence”; nó chủ yếu tách fragment theo size. Sequencing là bài toán khác.

## DNA sequencing

Sanger sequencing dùng chain-terminating nucleotide để suy ra sequence từ fragment length. Next-generation sequencing tạo hàng triệu read song song, đổi bài toán biology thành data-processing problem lớn.

Một sequencing workflow hiện đại thường gồm sample preparation, library construction, sequencing, quality control, alignment hoặc assembly, variant calling và downstream interpretation.

Sai số có thể xuất hiện ở mọi stage, nên bioinformatics không chỉ là “chạy tool” mà là quản lý uncertainty và bias.

## CRISPR-Cas

CRISPR-Cas bắt nguồn từ adaptive defense của bacteria và archaea. Trong genome editing, guide RNA đưa Cas nuclease tới DNA target có sequence phù hợp và điều kiện motif thích hợp.

Sau DNA cut, cell repair bằng non-homologous end joining hoặc homology-directed repair. NHEJ thường tạo insertion/deletion nhỏ; HDR có thể dùng repair template để tạo edit có định hướng.

> Mental model: CRISPR không phải “bút sửa DNA chính xác tuyệt đối”. Nó là hệ định vị molecular + enzyme cắt/chỉnh, còn outcome cuối phụ thuộc repair pathway của cell.

Off-target effect, mosaicism, delivery và cell-type specificity là những constraint quan trọng.

## Recombinant DNA và protein production

Gene có thể được đưa vào plasmid vector rồi transform vào bacteria hoặc expression system khác. Promoter, selectable marker, replication origin và cloning site là những component phổ biến.

Nếu mục tiêu là sản xuất protein người, expression host phải phù hợp với folding và post-translational modification. Bacteria nhanh và rẻ nhưng không thực hiện nhiều eukaryotic modification như mammalian cell.

## Synthetic biology

Synthetic biology (합성생물학) cố thiết kế biological system theo engineering principles. Một gene circuit có thể có sensor, regulatory module và output, giống logic circuit ở mức abstraction.

Tuy nhiên biological part không modular tuyệt đối như electronic component. Context, resource competition, mutation và noise có thể làm circuit hoạt động khác dự đoán.

## Bioinformatics: sequence như dữ liệu

DNA sequence có thể biểu diễn như string trên alphabet `{A,C,G,T}`. Bài toán tìm motif, alignment và genome assembly vì vậy liên hệ trực tiếp với string algorithm, dynamic programming và graph theory.

Global alignment như Needleman–Wunsch dùng dynamic programming để tối ưu score toàn sequence. Local alignment như Smith–Waterman tìm region giống nhau mạnh nhất.

BLAST dùng heuristic để tìm sequence similarity nhanh trên database lớn. Similarity không tự động đồng nghĩa homology; homology là statement về shared ancestry, không phải percentage score.

## Genome assembly và graph

Khi sequencing tạo nhiều read ngắn, assembly cố tái dựng sequence dài. De Bruijn graph biểu diễn overlap qua k-mer và chuyển bài toán assembly thành graph traversal.

Repeat sequence tạo ambiguity vì cùng k-mer xuất hiện ở nhiều vị trí. Long-read sequencing giúp giải quyết một số repeat nhưng có error profile riêng.

## Omics và high-dimensional data

Genomics đo DNA, transcriptomics đo RNA, proteomics đo protein, metabolomics đo metabolite. Dataset thường có hàng nghìn hoặc hàng triệu feature nhưng số sample nhỏ hơn nhiều.

Điều này tạo nguy cơ overfitting và multiple testing. Statistics, dimensionality reduction, regularization và validation trở thành phần bắt buộc.

## Machine learning trong biology

Machine learning có thể dùng cho protein-structure prediction, cell-type classification, variant prioritization, image analysis hoặc drug discovery. Nhưng model tốt trên benchmark chưa chắc generalize sang hospital, population hoặc species khác.

Dataset bias, batch effect và label quality có thể mạnh hơn model architecture. Biological validation vẫn cần thiết.

## Systems biology

Một pathway có thể mô hình hóa như network node–edge. Dynamic model dùng differential equation để mô tả concentration thay đổi theo time:

```math
\frac{dx}{dt}=f(x,p,t)
```

Trong đó `x` là state vector, `p` là parameter. Feedback có thể tạo stable state, oscillation hoặc switch-like behavior.

Boolean network đơn giản hóa gene thành ON/OFF. Agent-based model mô phỏng nhiều cell/organism riêng lẻ. Không có model nào “đúng nhất” cho mọi scale; model phải khớp câu hỏi.

## Causality và experiment

Correlation từ omics data giúp tạo hypothesis nhưng không thay thế perturbation experiment. Knockout, knockdown, CRISPR edit, drug inhibition hoặc randomized intervention giúp kiểm tra causal mechanism tốt hơn.

Data science mạnh nhất khi loop được đóng: measurement → model → prediction → experiment → model revision.

## Ethics và governance

Biotechnology có thể tác động medicine, agriculture, environment và reproduction. Vì vậy technical feasibility không tự động đồng nghĩa nên triển khai.

Các vấn đề như privacy genomic data, germline editing, consent, ecological release và unequal access cần scientific evidence lẫn ethical governance.

## Common misconceptions

“AI đọc genome rồi dự đoán chắc chắn disease” là sai. Nhiều disease là polygenic, environment-dependent và prediction có uncertainty lớn.

“CRISPR sửa gene nào cũng đơn giản” cũng sai; delivery, off-target, mosaicism và biological redundancy có thể làm outcome khác kỳ vọng.

## Kết nối

PCR và CRISPR dựa trên [[../02_genetics_molecular_biology/00_dna_genes_and_gene_expression]]. Omics nối với [[../02_genetics_molecular_biology/02_genomics_epigenetics_and_regulation]]. Mathematical/computational foundation được tổng hợp trong [[../90_connections/00_biology_math_computation_and_scale]].
