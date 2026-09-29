# Bioinformatics, thuật toán và Omics Workflow — Bioinformatics Algorithms and Omics Workflows (생물정보학, 알고리즘과 오믹스 워크플로)

> **Mạch đọc:** Đọc **Bioinformatics, thuật toán và Omics Workflow — Bioinformatics Algorithms and Omics Workflows (생물정보학, 알고리즘과 오믹스 워크플로)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Từ molecule sang digital đối tượng (object / 객체)** sang **2. siêu dữ liệu (metadata / 메타데이터) là một phần của dữ liệu (data / 데이터)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi Biology tạo ra hàng triệu chuỗi (sequence / 시퀀스), expression giá trị (value / 값) hoặc ảnh (image / 이미지) tính năng (feature / 기능), dữ liệu (data / 데이터) không còn có thể được hiểu bằng cách đọc từng dòng. **Sinh tin học (bioinformatics / 생물정보학)** xuất hiện ở đúng điểm này: dùng thuật toán, thống kê và mô hình dữ liệu (data model / 데이터 모델) để biến đo lường (measurement / 측정) thành suy luận sinh học (biological inference).

Chapter này không dạy một công cụ (tool / 도구) cụ thể. Mục tiêu là xây mô hình tư duy (mental model / 사고 모델) từ tín hiệu thô (raw signal) → tệp (file / 파일) → QC → biểu diễn (representation / 표현) → thuật toán (algorithm / 알고리즘) → mô hình thống kê (statistical model) → diễn giải (interpretation). Khi hiểu luồng (flow / 흐름) này, FASTQ, BAM, VCF, BLAST, RNA-seq hay single-cell không còn là những tên riêng rời rạc mà là các stage trong một lập luận (reasoning / 추론) chuỗi xử lý (pipeline / 파이프라인).

> **Mô hình tư duy:** bioinformatics không “khám phá truth trực tiếp từ dữ liệu (data / 데이터)”. Nó liên tục nén và biến đổi dữ liệu (data / 데이터). Mỗi transformation thêm giả định (assumption / 가정); vì vậy một conclusion tốt phải dấu vết (trace / 추적) được ngược về raw bằng chứng (evidence / 증거).

## 1. Từ molecule sang digital đối tượng (object / 객체)

Sequencer quan sát biochemical sự kiện (event / 이벤트) rồi cơ sở (base / 기반) caller chuyển tín hiệu (signal / 신호) thành chuỗi (sequence / 시퀀스) văn bản (text / 텍스트) và điểm chất lượng (quality score). Từ thời điểm đó, molecule trở thành digital bản ghi (record / 레코드).

Một raw read không biết mình thuộc gene nào hay có mutation gì. Nó chỉ là trình tự (sequence) + siêu dữ liệu (metadata / 메타데이터) + chất lượng (quality / 품질). Ý nghĩa sinh học (biological meaning) xuất hiện dần qua suy luận ở bước sau (downstream inference).

Các format phổ biến phản ánh stage đó. FASTQ giữ read và chất lượng. FASTA giữ trình tự. SAM/BAM/CRAM mô tả căn chỉnh (alignment). VCF mô tả variant candidate. GTF/GFF mô tả genomic tính năng (feature / 기능).

Format không chỉ là cú pháp (syntax / 문법) IT; nó encode **trạng thái (state / 상태) của lập luận (reasoning / 추론)**.

## 2. siêu dữ liệu (metadata / 메타데이터) là một phần của dữ liệu (data / 데이터)

Chuỗi (sequence / 시퀀스) không đủ. mẫu (sample / 표본) thuộc tissue nào, treatment gì, batch nào, thời gian (time / 시간) điểm (point / 지점) nào, patient nào, replicate nào — tất cả là siêu dữ liệu.

Nếu siêu dữ liệu (metadata / 메타데이터) sai hoặc ambiguous, phân tích (analysis / 분석) có thể technically hoàn hảo nhưng kết luận sinh học (biological conclusion) vô nghĩa.

Điều này làm cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계), quy ước đặt tên (naming convention) và từ vựng được kiểm soát (controlled vocabulary) trở thành thành phần (component / 컴포넌트) của chất lượng khoa học (scientific quality).

## 3. QC phải diễn ra trước suy luận (inference / 추론)

Adapter contamination, low-quality tail, unusual GC content, overrepresented chuỗi (sequence / 시퀀스) hoặc duplicated read có thể báo vấn đề kỹ thuật (technical issue).

Nhưng QC chỉ số (metric / 지표) không có ngưỡng phổ quát (universal threshold). High duplication có thể bình thường trong targeted amplicon sequencing nhưng suspicious trong whole-genome thư viện (library / 라이브러리).

QC vì vậy là **đánh giá theo bối cảnh (contextual diagnosis)**, không phải đạt/không đạt (pass/fail) máy móc.

## 4. Phred score là probabilistic siêu dữ liệu (metadata / 메타데이터)

Phred chất lượng (quality / 품질):

\[
Q=-10\log_{10}P(error)
\]

Q30 tương ứng estimated xác suất lỗi (error probability) khoảng 0.001. Log quy mô (scale / 규모) giúp biểu diễn bất định (uncertainty / 불확실성) nhỏ gọn.

Nhưng điểm chất lượng vẫn là mô hình (model / 모델) estimate từ machine hành vi (behavior / 동작). “Q30” không nghĩa cơ sở (base / 기반) chắc chắn đúng; nó nghĩa instrument/mô hình (model / 모델) đánh giá độ tin cậy (confidence) ở mức tương ứng.

## 5. Căn chỉnh trình tự (sequence alignment) biến biological similarity thành bài toán tối ưu (optimization problem)

Hai chuỗi (sequence / 시퀀스) có thể khác do substitution, insertion hoặc deletion. Alignment chèn gap để tìm correspondence.

Ta định nghĩa score cho match, mismatch và gap. Sau đó thuật toán (algorithm / 알고리즘) tìm alignment tối ưu theo score đó.

Căn chỉnh toàn cục (global alignment) thích hợp khi hai chuỗi (sequence / 시퀀스) tương đồng gần toàn chiều dài; căn chỉnh cục bộ (local alignment) tìm region giống nhau tốt nhất.

Biological question “hai chuỗi (sequence / 시퀀스) có quan hệ không?” trở thành computational bài toán (problem / 문제) “alignment nào có score cao dưới mô hình (model / 모델) đã chọn?”.

## 6. động (dynamic / 동적) programming: chính xác (exact / 정확한) solution có chi phí (cost / 비용)

Needleman–Wunsch và Smith–Waterman dùng động (dynamic / 동적) programming. Với chuỗi (sequence / 시퀀스) length \(m\) và \(n\), thời gian (time / 시간)/bộ nhớ (memory / 메모리) thường tăng theo tích của chiều dài trong hiện thực (implementation / 구현) cơ bản.

Khi cơ sở dữ liệu (database / 데이터베이스) có millions chuỗi (sequence / 시퀀스), chạy chính xác (exact / 정확한) thuật toán (algorithm / 알고리즘) với mọi pair quá đắt. Đây là nơi heuristic xuất hiện.

Khoa học máy tính (computer science / 컴퓨터 과학) không chỉ giúp chạy nhanh hơn; nó quyết định loại approximation nào ta chấp nhận để quy mô (scale / 규모) biological question.

## 7. BLAST: heuristic đánh đổi completeness lấy speed

BLAST tìm short matching word rồi extend candidate region thay vì exhaustively thử mọi alignment.

Kết quả nhanh và thường biologically useful, nhưng “BLAST hit” không tự chứng minh hàm (function / 함수). Similarity có thể do dùng chung (shared / 공유) lĩnh vực (domain / 도메인), repetitive region hoặc dùng chung (common / 공통) ancestry xa.

Chức năng (function) suy luận (inference / 추론) nên xem coverage, định danh (identity / 식별자), conserved lĩnh vực (domain / 도메인), synteny, phylogeny và ideally experiment.

## 8. E-value và significance của chuỗi (sequence / 시퀀스) match

BLAST E-value gần biểu diễn số match có score tương tự hoặc tốt hơn kỳ vọng xuất hiện ngẫu nhiên trong cơ sở dữ liệu (database / 데이터베이스) theo mô hình (model / 모델) nhất định.

Cơ sở dữ liệu (database / 데이터베이스) càng lớn, chance match càng nhiều. Vì vậy cùng score có significance khác khi tìm kiếm (search / 검색) cơ sở dữ liệu (database / 데이터베이스) khác kích thước (size / 크기).

Đây là lesson statistical quan trọng: bằng chứng (evidence / 증거) strength phụ thuộc tìm kiếm (search / 검색) không gian (space / 공간).

## 9. Hệ gen tham chiếu (reference genome) là coordinate hệ thống (system / 시스템), không phải “genome chuẩn tuyệt đối”

Tham chiếu (reference / 참조) giúp read có coordinate chung. Nhưng tham chiếu (reference / 참조) là biểu diễn (representation / 표현) cụ thể, không chứa mọi haplotype hoặc structural variant trong quần thể (population).

Read từ region divergent hoặc repeat có thể map khó. **Sai lệch do tham chiếu (reference bias)** xảy ra khi chuỗi xử lý (pipeline / 파이프라인) ưu tiên allele giống tham chiếu (reference / 참조).

Hệ gen toàn quần thể (pangenome) biểu diễn (representation / 표현) cố mô hình hóa nhiều đường dẫn (path / 경로)/haplotype hơn, thường bằng graph-like cấu trúc (structure / 구조).

## 10. Chất lượng ánh xạ (mapping quality) là bất định (uncertainty / 불확실성) về vị trí

Short read ở repeat region có thể align nhiều nơi. Mapper phải chọn best location, đánh multi-mapping hoặc bỏ read.

Chất lượng ánh xạ phản ánh confidence placement. Vì vậy statement “read này thuộc gene X” cũng là suy luận (inference / 추론) có độ bất định (uncertainty / 불확실성).

Nếu downstream variant caller bỏ qua bất định (uncertainty / 불확실성) ánh xạ (mapping / 매핑), dương tính giả (false positive) có thể tăng.

## 11. Coverage là redundancy, nhưng coverage thực không đều

Approximation:

\[
Coverage\approx\frac{N\times L}{G}
\]

với \(N\) số read, \(L\) read length và \(G\) genome kích thước (size / 크기).

Coverage cao tạo redundancy giúp phân biệt sequencing lỗi (error / 오류) khỏi variant thật. Nhưng GC độ lệch (bias / 편향), capture efficiency và mappability làm độ sâu (depth / 깊이) không đều.

“30× hệ gen (genome)” là average, không nghĩa mọi cơ sở (base / 기반) đều được đọc 30 lần.

## 12. Gọi biến thể (variant calling) là probabilistic quyết định (decision / 결정)

Giả sử tại một locus có 18 read A và 12 read G. Có thể mẫu (sample / 표본) heterozygous, nhưng cũng có thể ánh xạ (mapping / 매핑) độ lệch (bias / 편향), contamination hoặc sequencing lỗi (error / 오류).

Variant caller so likelihood của genotype hypothesis dựa trên cơ sở (base / 기반) chất lượng (quality / 품질), chất lượng ánh xạ, allele balance và mô hình (model / 모델) ploidy.

VCF vì vậy không phải danh sách (list / 목록) truth. Nó là collection of candidate variant + bằng chứng (evidence / 증거) + filter.

## 13. Germline và somatic workflow dùng biological prior khác nhau

Germline diploid variant thường có allele fraction gần 0, 0.5 hoặc 1 trong ideal mẫu (sample / 표본).

Tumor mẫu (sample / 표본) có purity <100%, subclone, copy-number alteration và normal-cell admixture. Somatic variant fraction vì vậy có thể thấp hoặc lệch.

Cùng raw read nhưng mô hình (model / 모델) biological khác làm suy luận (inference / 추론) khác.

## 14. Copy-number và structural variant cần bằng chứng (evidence / 증거) khác SNV

Large deletion, duplication, inversion hoặc translocation không thể luôn detect bằng single-base mismatch.

Ta cần độ sâu (depth / 깊이) thay đổi (change / 변경), discordant paired-end orientation, split read hoặc long-read spanning sự kiện (event / 이벤트).

Điều này cho thấy thuật toán (algorithm / 알고리즘) phụ thuộc **signature vật lý mà experiment tạo ra**.

## 15. Genome assembly: reconstruction không có tham chiếu (reference / 참조)

Assembly ghép read thành contig/scaffold. Với short read, **de Bruijn đồ thị (graph / 그래프)** thường biểu diễn k-mer overlap.

Repeat tạo branch, sequencing lỗi (error / 오류) tạo spur, heterozygosity tạo alternative đường dẫn (path / 경로). Long read span repeat tốt hơn nhưng có lỗi (error / 오류) profile riêng.

Assembly là đồ thị (graph / 그래프) reconstruction dưới incomplete/noisy dữ liệu (data / 데이터).

## 16. k-mer kích thước (size / 크기) là sự đánh đổi (trade-off / 트레이드오프)

k nhỏ tăng overlap nhưng làm repeat khó phân biệt. k lớn tăng uniqueness nhưng yêu cầu read dài và đủ coverage.

Không có k “tốt nhất” universal. Parameter phản ánh sự đánh đổi (trade-off / 트레이드오프) giữa connectivity và độ đặc hiệu (specificity).

Đây là example thuật toán (algorithm / 알고리즘) parameter có biological consequence.

## 17. Annotation: chuỗi (sequence / 시퀀스) không tự nói “đây là gen (gene)”

Gene annotation kết hợp open reading frame, splice tín hiệu (signal / 신호), transcript bằng chứng (evidence / 증거), protein homology và comparative genomics.

Annotation cơ sở dữ liệu (database / 데이터베이스) có phiên bản (version / 버전) và độ bất định. Một gene mô hình (model / 모델) có thể được sửa khi RNA-seq hoặc long-read transcript bằng chứng (evidence / 증거) mới xuất hiện.

Do đó downstream phân tích (analysis / 분석) phải ghi hệ gen tham chiếu **và annotation phiên bản (version / 버전)**.

## 18. RNA-seq: count không phải expression tuyệt đối trực tiếp

RNA-seq workflow thường gồm QC → căn chỉnh/pseudoalignment → counting → normalization → biểu hiện khác biệt (differential expression).

Raw count phụ thuộc thư viện (library / 라이브러리) kích thước (size / 크기), mức độ phong phú của bản phiên mã (transcript abundance) và technical độ lệch (bias / 편향). Transcript length ảnh hưởng xác suất (probability / 확률) read xuất hiện trong within-sample comparison.

Normalization cố tạo comparable quy mô (scale / 규모) giữa mẫu (sample / 표본) nhưng luôn có giả định (assumption / 가정).

## 19. Normalization có thể che toàn cục (global / 전역) shift

Nhiều phương thức (method / 메서드) giả định phần lớn gene không đổi extreme hoặc composition không đổi quá mạnh.

Nếu treatment làm toàn cục (global / 전역) RNA môi trường vận hành (production / 운영 환경) tăng gần toàn transcriptome, relative normalization có thể làm thay đổi (change / 변경) trông nhỏ đi.

Đây là reason spike-in điều khiển (control / 제어) đôi khi hữu ích: bên ngoài (external / 외부) tham chiếu (reference / 참조) giúp nhận biết toàn cục (global / 전역) scaling.

## 20. Biểu hiện khác biệt và kiểm định nhiều lần (multiple testing)

Nếu kiểm thử (test / 테스트) 20,000 gene với p<0.05 mà không correction, dương tính giả xuất hiện nhiều chỉ do chance.

False Discovery tỷ lệ (rate / 비율) giúp kiểm soát expected false discovery proportion trong khung phần mềm (framework / 프레임워크) nhất định.

Nhưng adjusted p-value nhỏ vẫn cần tác động (effect / 효과) kích thước (size / 크기). Gene thay 1.03× với huge n có thể significant mà biological relevance thấp.

## 21. PCA: nhìn cấu trúc (structure / 구조) high-dimensional bằng vài trục

Mỗi mẫu (sample / 표본) expression là véc-tơ (vector / 벡터) hàng nghìn chiều. PCA tìm orthogonal direction capture variance lớn.

PCA plot giúp detect batch, outlier hoặc major biological separation. Nhưng principal thành phần (component / 컴포넌트) chỉ tối đa variance; nó không tự mang meaning biological.

Loading và siêu dữ liệu (metadata / 메타데이터) cần để interpret axis.

## 22. Clustering là hypothesis generator, không phải truth generator

Clustering nhóm cell/mẫu (sample / 표본) theo similarity. Kết quả phụ thuộc tính năng (feature / 기능) selection, normalization, distance chỉ số (metric / 지표) và độ phân giải (resolution).

Một cluster đẹp không tự chứng minh “loại tế bào (cell type) mới”. Cần marker, developmental ngữ cảnh (context / 맥락) và ideally kiểm tra hợp lệ (validation / 검증).

Thuật toán (algorithm / 알고리즘) tạo partition; biologist gắn interpretation.

## 23. Single-cell RNA-seq: từ average sang phân phối (distribution / 분포)

Bulk RNA-seq trộn nhiều cell. Single-cell phân giải heterogeneity và rare population.

Nhưng capture efficiency thấp, count sparse và nhiều zero. Zero có thể nghĩa gene off hoặc transcript bị missed.

Vì vậy single-cell phân tích (analysis / 분석) cần mô hình (model / 모델) count noise và tránh đọc heatmap như đo lường (measurement / 측정) hoàn hảo.

## 24. UMAP/t-SNE: visualization không bảo toàn mọi khoảng cách

Giảm chiều dữ liệu (dimensionality reduction) nén hàng nghìn dimension xuống 2D/3D. cục bộ (local / 로컬) neighborhood có thể hữu ích, nhưng toàn cục (global / 전역) distance và cluster gap trên plot không nên overinterpret.

Một plot đẹp là biểu diễn (representation / 표현) của thuật toán (algorithm / 알고리즘), không phải microscope ảnh (image / 이미지) của “tế bào (cell)-state không gian (space / 공간)”.

## 25. Pseudotime: reconstruct dynamics từ snapshot

Developmental single-cell dataset thường chứa nhiều cell ở trạng thái (state / 상태) khác nhau. thuật toán (algorithm / 알고리즘) có thể thứ tự (order / 순서) cell thành **pseudotime** dựa trên manifold/đồ thị (graph / 그래프).

Pseudotime không phải actual chronological thời gian (time / 시간). Nó là inferred progression dưới giả định (assumption / 가정) rằng sampled states lie along chuyển tiếp (transition / 전이) đường dẫn (path / 경로).

Kiểm tra hợp lệ (validation / 검증) bằng lineage tracing hoặc time-course giúp mạnh hơn.

## 26. Epigenomics: khả năng tiếp cận (accessibility / 접근성) và binding không đồng nghĩa causality

ATAC-seq đo khả năng tiếp cận nhiễm sắc chất (chromatin accessibility). ChIP-seq đo enrichment DNA fragment associated với protein/histone mark. Methyl hóa DNA (DNA methylation) phép thử (assay) đo methylation trạng thái (state / 상태).

Kết hợp epigenomics với RNA-seq giúp xây regulatory hypothesis. Nhưng open enhancer correlated với gene up không tự chứng minh enhancer gây expression.

CRISPR perturb enhancer hoặc reporter assay có thể kiểm tra nhân quả (causal / 인과적) role.

## 27. Proteomics và metabolomics đưa ta gần phenotype hơn nhưng tăng ambiguity khác

Mass spectrometry đo mass-to-charge mẫu (pattern / 패턴) rồi infer peptide/protein (protein)/metabolite định danh (identity / 식별자).

Mức độ phong phú của protein (protein abundance) chịu translation, phân giải (degradation), modification. Metabolite phản ánh mạng (network / 네트워크) trạng thái (state / 상태) gần reaction flux nhưng annotation có thể khó.

Không tầng (layer / 계층) omics nào “cao hơn” tuyệt đối. Mỗi tầng (layer / 계층) có ý nghĩa sinh học và phép đo (measurement) độ lệch (bias / 편향) riêng.

## 28. Multi-omics tích hợp (integration / 통합): nhiều tầng (layer / 계층) không tự động tạo hiểu biết

Kết hợp genome, epigenome, transcriptome, proteome và metabolome tăng ngữ cảnh (context / 맥락) nhưng dimension và missing dữ liệu (data / 데이터) cũng tăng.

Một useful chiến lược (strategy / 전략) là đặt nhân quả (causal / 인과적) question rõ: variant có đổi chromatin không, chromatin có đổi expression không, expression có đổi protein/metabolite không?

Tích hợp (integration / 통합) tốt đi theo biological cơ chế (mechanism / 메커니즘), không chỉ concatenate ma trận (matrix / 행렬).

## 29. Mạng lưới (network) sinh học (biology): đồ thị (graph / 그래프) hữu ích nhưng edge cần bằng chứng (evidence / 증거) kiểu (type / 타입)

Nút (node / 노드) có thể là gen/protein/metabolite; edge là tương tác (interaction / 상호작용)/điều hòa (regulation).

Degree, centrality và quần xã (community) cấu trúc (structure / 구조) giúp tìm organization. Nhưng cơ sở dữ liệu (database / 데이터베이스) tương tác (interaction / 상호작용) biased về gene nổi tiếng; co-expression edge không giống physical-binding edge.

Mọi mạng (network / 네트워크) visualization nên hỏi: **edge nghĩa gì và bằng chứng (evidence / 증거) từ đâu?**

## 30. Học máy (machine learning): prediction khác explanation

ML có thể classify ảnh (image / 이미지), predict phenotype hoặc infer protein đặc tính (property). Nhưng high kiểm thử (test / 테스트) accuracy không tự chứng minh mô hình (model / 모델) học biology đúng.

Mô hình (model / 모델) có thể học batch, hospital, scanner hoặc ancestry confounder.

Prediction trả lời “có dự đoán được không?”. Causality trả lời “thay X có làm Y đổi không?”. Hai câu hỏi khác nhau.

## 31. Train/kiểm tra hợp lệ (validation / 검증)/kiểm thử (test / 테스트) và rò rỉ dữ liệu (data leakage)

Huấn luyện (training / 학습) set fit mô hình (model / 모델). kiểm tra hợp lệ (validation / 검증) set tune hyperparameter. kiểm thử (test / 테스트) set estimate hiệu năng (performance / 성능) cuối trên unseen dữ liệu (data / 데이터).

**Rò rỉ dữ liệu** xảy ra khi thông tin (information / 정보) kiểm thử (test / 테스트) lọt vào tập luyện (training). Trong sinh học, dùng chung (common / 공통) leak là mẫu (sample / 표본) từ cùng patient hoặc same clone bị split ngẫu nhiên vào cả train và kiểm thử (test / 테스트).

Mô hình khi đó có thể memorize individual-specific tín hiệu (signal / 신호) thay vì general biological quy tắc (rule / 규칙).

## 32. Cross-validation phải tôn trọng đơn vị (unit / 단위) độc lập

Nếu đơn vị (unit / 단위) biological thật là patient, split nên theo patient, không theo ảnh (image / 이미지) patch hay cell riêng lẻ từ cùng patient.

Đây là cầu nối (bridge / 브리지) giữa thiết kế thực nghiệm (experimental design) và ML: independence giả định (assumption / 가정) phải phản ánh sampling quá trình (process).

## 33. tính năng (feature / 기능) importance không phải nhân quả (causal / 인과적) importance

Một gene có predictive power lớn có thể chỉ là downstream marker. SHAP/importance score cho biết mô hình (model / 모델) dùng tính năng (feature / 기능), không chứng minh gene driver disease.

Để kiểm thử (test / 테스트) driver cần perturbation hoặc nhân quả (causal / 인과적) thiết kế (design / 설계).

## 34. Quy trình có thể tái lập (reproducible workflow) là một phần của science

Phân tích (analysis / 분석) nên nhánh học (track / 트랙) dữ liệu thô (raw data) checksum, tham chiếu (reference / 참조) phiên bản (version / 버전), software phiên bản (version / 버전), tham số (parameter), môi trường (environment / 환경) và mã (code / 코드).

Workflow manager, bộ chứa (container / 컨테이너) và phiên bản (version / 버전) điều khiển (control / 제어) giúp rerun chuỗi xử lý (pipeline / 파이프라인) và dấu vết (trace / 추적) figure về nguồn (source / 소스).

Một kết quả (result / 결과) không chỉ là final plot:

```text
raw data
→ QC
→ preprocessing
→ intermediate file
→ model
→ table
→ figure
→ biological interpretation
```

Nếu chuỗi (chain / 사슬) không dấu vết (trace / 추적) được, reproducibility yếu.

## 35. Tình huống phân tích (case study): germline variant workflow end-to-end

Mẫu (sample / 표본) DNA được chuỗi (sequence / 시퀀스) thành FASTQ. QC kiểm chất lượng (quality / 품질)/adapter. Read map lên tham chiếu (reference / 참조). Duplicate/technical sản phẩm tạo ra (artifact / 산출물) được xử lý. Variant caller tính genotype likelihood. Biến thể (variant) được filter rồi annotate bằng gene/chức năng/cơ sở dữ liệu tần số (frequency).

Cuối cùng variant “pathogenic hay không” vẫn cần clinical/genetic bằng chứng (evidence / 증거), di truyền (inheritance) mẫu (pattern / 패턴) và kiểu hình (phenotype) bối cảnh (context).

Chuỗi xử lý (pipeline / 파이프라인) không biến raw read trực tiếp thành diagnosis; mỗi stage thu hẹp bất định (uncertainty / 불확실성) một phần.

## 36. Tình huống phân tích: RNA-seq biểu hiện khác biệt không dừng ở volcano plot

Sau QC và count, mô hình thống kê tìm gene khác expression. Volcano plot chỉ là visualization.

Biological lập luận (reasoning / 추론) tiếp theo hỏi pathway nào enriched, tác động (effect / 효과) có replicate không, cell composition có thay không, yếu tố phiên mã (transcription factor) nào plausible, và perturbation gene candidate có đổi phenotype không.

Omics là hypothesis engine mạnh, nhưng cơ chế (mechanism / 메커니즘) cần vòng experiment mới.

## 37. Các hiểu lầm phổ biến (common misconceptions)

“Bioinformatics chỉ là chạy công cụ (tool / 도구)” là sai. công cụ (tool / 도구) encode giả định (assumption / 가정) và tham số.

“Dataset càng lớn càng tự động đúng” sai; systematic độ lệch (bias / 편향) không biến mất khi n tăng.

“AI tìm được tính năng (feature / 기능) quan trọng nghĩa đã tìm ra cơ chế (mechanism / 메커니즘)” sai.

“Hệ gen tham chiếu là genome chuẩn của species” quá đơn giản; population có diversity và biến thể cấu trúc (structural variation).

## 38. Mô hình tư duy tổng hợp

Bioinformatics có thể nén thành luồng (flow / 흐름):

```text
measurement
→ digital representation
→ QC
→ mapping/reconstruction
→ statistical inference
→ uncertainty
→ biological hypothesis
→ experimental validation
```

Mỗi stage vừa thêm thông tin (information / 정보) vừa làm mất một phần detail. Phân tích tốt giữ provenance và độ bất định đủ để biết conclusion mạnh đến đâu.

<!-- depth-audit-2026:ai-data-generating-process -->
## Bioinformatics phải bắt đầu từ data-generating tiến trình (process / 프로세스)

FASTQ, count ma trận (matrix / 행렬) hay embedding đều là đầu ra (output / 출력) sau nhiều transformation. mẫu (sample / 표본) collection, thư viện (library / 라이브러리) preparation, sequencing chemistry, tham chiếu (reference / 참조) alignment và filtering quyết định phân phối (distribution / 분포) của dữ liệu (data / 데이터) trước khi mô hình (model / 모델) nhìn thấy nó. Vì vậy một mẫu (pattern / 패턴) machine học tập (learning / 학습) tìm được có thể phản ánh batch, ancestry imbalance hoặc tham chiếu (reference / 참조) độ lệch (bias / 편향) thay vì cơ chế (mechanism / 메커니즘) sinh học.

**dữ liệu (data / 데이터) leakage** xảy ra khi thông tin (information / 정보) từ kiểm thử (test / 테스트) set lọt vào huấn luyện (training / 학습)/tính năng (feature / 기능) selection; **phân phối (distribution / 분포) shift** xảy ra khi population triển khai khác population train. Hai lỗi này đặc biệt nguy hiểm trong biomedical AI vì accuracy nội bộ cao có thể không giữ khi hospital, ancestry, instrument hoặc disease prevalence thay đổi.

Foundation mô hình (model / 모델) và protein ngôn ngữ (language / 언어) mô hình (model / 모델) có thể học biểu diễn (representation / 표현) mạnh từ chuỗi (sequence / 시퀀스) lớn, hỗ trợ cấu trúc (structure / 구조)/hàm (function / 함수) prediction và variant prioritization. Nhưng prediction không đồng nghĩa nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘). mô hình (model / 모델) có thể nội suy statistical regularity mà không biết intervention sẽ làm gì trong cell thật. kiểm tra hợp lệ (validation / 검증) tốt cần bên ngoài (external / 외부) dataset, perturbation experiment và bất định (uncertainty / 불확실성) calibration.

AI hữu ích nhất khi đặt trong chuỗi xử lý (pipeline / 파이프라인) `biological question → measurement → representation → model → prediction → experimental test`, không phải khi thay toàn bộ biology bằng score.

## 39. cầu nối (bridge / 브리지) sang Sinh học hệ thống (systems biology)

Omics cho ta thành phần (component / 컴포넌트) và trạng thái (state / 상태) ở quy mô (scale / 규모) lớn, nhưng vẫn chưa trả lời mạng (network / 네트워크) sẽ phản ứng thế nào khi perturb. Biết gene A và B tăng cùng nhau không nói mạng (network / 네트워크) động lực học (dynamics), phản hồi (feedback / 피드백) hay nhân quả (causal / 인과적) direction.

Bước tiếp theo là xây mô hình (model / 모델) tương tác (interaction / 상호작용), tốc độ (rate), phản hồi (feedback / 피드백) và perturbation — tức **Sinh học hệ thống**.

Xem tiếp [Sinh học hệ thống, mô hình hóa và sinh học tổng hợp](03_systems_biology_modeling_and_synthetic_biology.md).

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Phương pháp thực nghiệm và đo lường trong Sinh học](01_experimental_methods_and_measurement.md) · [Mục lục Biology](../README.md) · [Sinh học hệ thống, mô hình hóa và sinh học tổng hợp →](03_systems_biology_modeling_and_synthetic_biology.md)

> **Bàn giao:** Sau **39. cầu nối (bridge / 브리지) sang Sinh học hệ thống (systems biology)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 biotechnology bioinformatics and systems biology](./00_biotechnology_bioinformatics_and_systems_biology.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
