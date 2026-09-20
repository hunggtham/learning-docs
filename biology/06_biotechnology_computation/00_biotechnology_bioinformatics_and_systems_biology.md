# Công nghệ sinh học, tin sinh học và sinh học hệ thống — Biotechnology, Bioinformatics and Systems Biology (생명공학, 생물정보학과 시스템생물학)

Nếu các chapter trước xây biology như một knowledge graph, biotechnology là lúc ta dùng chính graph đó để can thiệp và đo lường. PCR không phải một trick tách biệt; nó là DNA replication được đưa vào test tube. CRISPR không xuất hiện từ hư không; nó được tái sử dụng từ microbial defense. Sequencing biến chemical polymer thành digital data. Bioinformatics dùng algorithm để suy lại sequence, variation và relationship.

Vì vậy chapter này được viết như một chuỗi “mechanism → tool → data → inference”, không phải danh sách công nghệ.

## 1. Từ cơ chế tự nhiên đến công cụ

Công nghệ sinh học thường bắt đầu bằng một observation về natural mechanism.

DNA polymerase copy template → ta xây PCR.

Restriction enzyme cắt DNA → ta dùng cloning.

Bacterial plasmid tự replicate → ta dùng vector.

CRISPR-Cas nhận diện sequence → ta dùng gene editing.

Fluorescent protein phát sáng → ta dùng reporter.

Pattern chung:

```text
natural mechanism
      ↓
isolate / engineer component
      ↓
control condition
      ↓
measure or manipulate biology
```

## 2. PCR: replication được điều khiển theo chu kỳ

**PCR (polymerase chain reaction / 중합효소 연쇄반응)** khuếch đại một DNA region.

Ta cần template DNA, primer, nucleotide và thermostable DNA polymerase.

Một cycle có ba logic step:

1. denaturation: tách double strand bằng nhiệt;
2. annealing: primer bind sequence bổ sung;
3. extension: polymerase kéo dài từ primer.

Nếu efficiency lý tưởng, số copy tăng gần exponential theo số cycle:

\[
N_n \approx N_0 2^n
\]

Đây là exponential growth model quay lại trong molecular experiment.

## 3. Primer tạo specificity

PCR không khuếch đại “mọi DNA”. Primer define boundary region.

Nếu primer match nhiều site, non-specific product xuất hiện. Nếu temperature annealing quá thấp, mismatch dễ xảy ra; quá cao, primer khó bind.

Vì vậy PCR design là application của base pairing thermodynamics.

## 4. Gel electrophoresis: charge + size trở thành separation

DNA backbone mang negative charge. Trong electric field, DNA di chuyển về positive electrode.

Gel matrix cản fragment lớn nhiều hơn fragment nhỏ, nên fragment nhỏ chạy xa hơn.

Một kỹ thuật lab đơn giản kết hợp chemistry của phosphate charge với physics của porous medium.

## 5. Recombinant DNA và plasmid

Plasmid là circular DNA có thể replicate trong bacteria.

Nếu insert gene vào plasmid, transform bacteria và select cell mang plasmid, ta có thể clone DNA hoặc expression protein.

Vector thường có origin of replication, selectable marker và cloning/expression region.

Đây là việc biến natural bacterial DNA element thành engineering platform.

## 6. DNA sequencing: từ molecule sang string

Sequencing đo order A/C/G/T.

Sanger sequencing dùng chain-terminating nucleotide để tạo fragment có length khác nhau rồi đọc order.

Modern high-throughput sequencing tạo hàng triệu read song song.

Nhưng machine output chưa phải “genome”. Nó là measurement cần computation.

## 7. Read, coverage và error

Một **read** là đoạn sequence máy đo được.

Nếu genome được đọc nhiều lần, ta có **coverage** cao hơn, giúp distinguish sequencing error khỏi true variant.

Coverage không phân bố hoàn toàn đều; GC content, library preparation và mapping ambiguity tạo bias.

Do đó experimental design và computational interpretation phải đi cùng nhau.

## 8. Mapping và alignment

Nếu có reference genome, read có thể được **mapped** tới vị trí giống nhất.

Sequence alignment tìm cách đặt character tương đồng cạnh nhau, cho phép mismatch và gap.

Một scoring scheme đơn giản thưởng match, phạt mismatch/gap.

Dynamic programming như Needleman–Wunsch/Smith–Waterman giải alignment optimal trong model nhất định.

Biology ở đây gặp algorithms trực tiếp.

## 9. BLAST: similarity search không đồng nghĩa identity

BLAST tìm sequence region tương tự trong database nhanh hơn full dynamic-programming exhaustive search.

High similarity có thể gợi ý homology/function nhưng không tự động chứng minh cùng function.

E-value và score giúp đánh giá match có đáng chú ý so với chance không.

Again: computational hit là evidence, không phải final biological conclusion.

## 10. Genome assembly: reconstruct whole từ fragment

Nếu không dựa reference, ta phải assemble read thành longer contig.

Short-read assembly thường dùng overlap/de Bruijn graph concept.

Repeat region làm assembly khó vì cùng sequence có thể xuất hiện ở nhiều vị trí.

Đây là graph problem sinh ra trực tiếp từ physical constraint của sequencing.

## 11. Variant calling: từ read difference tới genotype

Sau mapping, ta tìm position read khác reference.

Nhưng mismatch có thể do sequencing error, mapping error hoặc true variant.

Variant caller dùng depth, base quality, allele fraction và statistical model để estimate genotype.

Data pipeline vì thế là inference under uncertainty.

## 12. RNA-seq: đo gene expression trên quy mô genome

RNA được convert thành cDNA rồi sequencing. Read count liên quan abundance transcript.

Nhưng raw count phụ thuộc sequencing depth và gene length/context, nên cần normalization tùy analysis.

Differential-expression test phải xét biological replicate và variance.

Một heatmap đẹp không thay thế experimental design tốt.

## 13. Single-cell omics: average có thể che mất heterogeneity

Bulk RNA-seq trộn signal nhiều cell. Single-cell RNA-seq đo từng cell, giúp phát hiện cell type/state hiếm.

Nhưng data sparse và noisy hơn. Analysis cần dimension reduction, clustering và careful interpretation.

Đây là nơi statistics/ML hỗ trợ biology, nhưng cluster không tự động tương đương “cell type thật” nếu thiếu biological validation.

## 14. CRISPR-Cas: từ bacterial immunity tới gene editing

CRISPR-Cas system tự nhiên dùng guide RNA để nhận sequence complementary và Cas protein cắt target.

Trong gene editing, ta design guide RNA tới genomic target.

Sau double-strand break, cell repair bằng pathway như NHEJ hoặc HDR. Editing outcome phụ thuộc chính repair machinery của host.

Tool vì thế không “viết DNA tùy ý” một cách magic; nó tạo targeted damage rồi khai thác repair.

## 15. Off-target và delivery là phần của problem

Một editor tốt không chỉ cần cắt target in vitro. Nó phải đến đúng cell/tissue, đủ expression, ít immune/toxic effect và hạn chế off-target.

Engineering challenge luôn gồm system context, không chỉ molecular specificity.

## 16. Synthetic biology: thiết kế circuit bằng component sinh học

Synthetic biology cố xây circuit gene có behavior mong muốn.

Promoter, repressor, activator và sensor có thể ghép thành logical function.

Ví dụ negative-feedback circuit ổn định expression; toggle switch dùng positive feedback để giữ hai state.

Control theory và gene regulation gặp nhau ở đây.

## 17. Systems biology: khi một gene không đủ giải thích phenotype

Nhiều phenotype xuất hiện từ network interaction.

Systems biology dùng network, differential equation và multi-omics để mô hình hóa system-level behavior.

Ví dụ signaling pathway có feedback, metabolic network có flux constraint, gene-regulatory network có attractor.

Mục tiêu không phải vẽ network càng lớn càng tốt, mà tìm model đủ để predict response và test experiment.

## 18. Machine learning trong biology

ML có thể classify cell, predict protein structure/property, detect image pattern hoặc estimate risk từ high-dimensional data.

Nhưng prediction khác explanation.

Một model có accuracy cao có thể exploit confounder. Biological validation vẫn cần để nói mechanism.

Causal inference và experimental intervention là bổ sung quan trọng cho predictive ML.

## 19. Protein structure prediction nối sequence với function

Protein chapter đã xây sequence → folding → function.

Computational structure prediction cố estimate 3D structure từ sequence và evolutionary information.

Structure prediction mạnh giúp hypothesis about binding/function, nhưng dynamic, post-translational modification và cellular environment vẫn cần experiment.

## 20. Database và reproducibility

Bioinformatics phụ thuộc database lớn: genome reference, protein sequence, structure, expression dataset.

Pipeline phải track software version, parameter, reference build và sample metadata.

Đây là điểm software engineering gặp science: reproducibility cần version control, container, workflow và provenance.

## 21. Experimental causality: đo nhiều chưa đủ

Omics thường nói “A associated B”. Gene editing, knockdown/overexpression hoặc controlled perturbation giúp test causality.

Một strong workflow:

```text
observation
 ↓
hypothesis
 ↓
perturbation
 ↓
measurement
 ↓
model update
```

Science tiến theo loop này, không phải data collection một chiều.

## 22. Ethical layer

Gene editing, human genomic data, synthetic organism và clinical prediction có ethical issue: consent, privacy, equity, off-target risk và ecological consequence.

Biological capability không tự trả lời “nên làm gì”. Scientific understanding phải được kết hợp ethical/legal/social reasoning.

## 23. Từ biotechnology sang connections tổng thể

Biotechnology cho thấy các concept tưởng xa nhau thực ra dùng chung pattern:

- PCR dùng exponential amplification;
- sequencing dùng probability/statistics;
- assembly dùng graph;
- systems biology dùng differential equation;
- ML dùng optimization;
- CRISPR dùng base pairing + microbial evolution.

Chương cuối [[../90_connections/00_biology_math_computation_and_scale]] sẽ gom các pattern toán–tính toán này theo cách xuyên toàn library, để người đọc thấy cùng một mental model tái xuất từ molecule đến ecosystem.