# Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**. Route đi từ câu hỏi sinh học → đo lường/PCR và thao tác vật liệu di truyền → dữ liệu trình tự → mô hình hệ thống và thiết kế sinh học, để công nghệ luôn gắn với mục tiêu, kiểm soát và bằng chứng.

Toàn bộ các chapter trước xây một đồ thị kiến thức (knowledge graph) từ molecule tới ecosystem. Biotechnology bắt đầu khi ta hỏi một câu mới: **nếu đã hiểu cơ chế (mechanism / 메커니즘), ta có thể đo, khuếch đại, chỉnh sửa hoặc thiết kế nó như thế nào?** Bioinformatics xuất hiện khi dữ liệu quá lớn để xử lý thủ công; sinh học hệ thống (systems biology) xuất hiện khi danh sách thành phần (component / 컴포넌트) không còn đủ để giải thích hành vi (behavior / 동작) của mạng (network / 네트워크).

> **mô hình tư duy (mental model / 사고 모델):** công nghệ sinh học (biotechnology) biến biological cơ chế (mechanism / 메커니즘) thành công cụ (tool / 도구); sinh tin học (bioinformatics) biến biological dữ liệu (data / 데이터) thành biểu diễn (representation / 표현) có thể tính toán; sinh học hệ thống biến danh sách (list / 목록) thành phần (component / 컴포넌트) thành mô hình (model / 모델) về tương tác (interaction / 상호작용) và động lực học (dynamics).

## 1. Biotechnology không bắt đầu từ CRISPR

Con người đã dùng lên men (fermentation), selective breeding và food biotechnology từ lâu trước sinh học phân tử (molecular biology).

Hiện đại (modern / 현대적) biotechnology khác ở mức precision: ta có thể isolate DNA, amplify chuỗi (sequence / 시퀀스), trình tự (sequence) hệ gen (genome), edit locus và measure thousands gene cùng lúc.

Nhưng mỗi công cụ (tool / 도구) vẫn dựa cơ chế (mechanism / 메커니즘) tự nhiên: PCR dùng DNA polymerase; restriction enzyme đến từ bacterial defense; CRISPR đến từ microbial immunity.

> **Chuyển mạch:** Biotechnology begins with measurement/manipulation tools, not only CRISPR; PCR amplifies target DNA, and primer design determines specificity and failure modes.

## 2. PCR: làm một đoạn DNA trở thành hàng triệu bản sao (copy / 복사)

**Polymerase chuỗi (chain / 사슬) reaction, PCR (중합효소연쇄반응)** cần template DNA, two primers, thermostable DNA polymerase, nucleotide và buffer.

Một cycle gồm:

1. denaturation: tách Mạch DNA (DNA strand) bằng heat;
2. annealing: primer bind chuỗi (sequence / 시퀀스) complement;
3. extension: polymerase kéo dài.

Nếu efficiency lý tưởng, amount mục tiêu (target / 대상) tăng gần:

\[
N_n=N_0 2^n
\]

sau \(n\) cycle. Real efficiency thấp hơn 100% và reaction cuối sẽ plateau.

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **3. Primer tạo độ đặc hiệu (specificity)** tiếp nhận điểm tựa từ **2. PCR: làm một đoạn DNA trở thành hàng triệu bản sao (copy / 복사)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. qPCR và quantitative thinking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Primer tạo độ đặc hiệu (specificity)

PCR không “bản sao (copy / 복사) toàn genome”. Primer xác định ranh giới (boundary / 경계) region được khuếch đại.

Primer thiết kế (design / 설계) phải cân nhắc melting temperature, GC content, secondary cấu trúc (structure / 구조) và off-target binding.

Một mismatch gần 3′ end có thể ảnh hưởng extension mạnh hơn một mismatch ở vị trí khác.

Specificity là nhận dạng phân tử (molecular recognition) vấn đề (problem).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **4. qPCR và quantitative thinking** tiếp nhận điểm tựa từ **3. Primer tạo độ đặc hiệu (specificity)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. RT-PCR: RNA phải được chuyển thành DNA trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. qPCR và quantitative thinking

**qPCR** đo huỳnh quang (fluorescence) theo cycle để estimate initial template amount.

Cycle threshold thấp hơn thường gợi ý starting amount cao hơn vì mẫu (sample / 표본) đạt detectable fluorescence sớm hơn.

Quantification cần tiêu chuẩn (standard / 표준)/normalization và efficiency giả định (assumption / 가정); Ct giá trị (value / 값) không nên so trực tiếp vô điều kiện giữa assay khác nhau.

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **5. RT-PCR: RNA phải được chuyển thành DNA trước** tiếp nhận điểm tựa từ **4. qPCR và quantitative thinking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Gel electrophoresis: phân tử (molecule) được tách nhờ charge và ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. RT-PCR: RNA phải được chuyển thành DNA trước

RNA không được tiêu chuẩn (standard / 표준) DNA polymerase PCR bản sao (copy / 복사) trực tiếp. **Reverse transcriptase** tạo complementary DNA (cDNA), sau đó PCR amplify cDNA.

Technique này dùng đo transcript hoặc detect RNA virus trong nhiều assay.

Tên “RT-PCR” đôi khi bị dùng lẫn với real-time PCR; ngữ cảnh (context / 맥락) phải rõ.

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **6. Gel electrophoresis: phân tử (molecule) được tách nhờ charge và ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **5. RT-PCR: RNA phải được chuyển thành DNA trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Restriction enzyme và recombinant DNA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Gel electrophoresis: phân tử (molecule) được tách nhờ charge và ma trận (matrix / 행렬)

DNA mang negative charge do phosphate backbone nên chạy về positive electrode trong điện trường (electric field).

Agarose gel tạo mesh; fragment nhỏ di chuyển nhanh hơn fragment lớn trong điều kiện (condition / 조건) phù hợp.

Band position được so với DNA ladder để estimate kích thước (size / 크기).

Electrophoresis biến kích thước (size / 크기) molecular thành spatial mẫu (pattern / 패턴) nhìn thấy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **7. Restriction enzyme và recombinant DNA** tiếp nhận điểm tựa từ **6. Gel electrophoresis: phân tử (molecule) được tách nhờ charge và ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Transformation và chọn lọc (selection)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Restriction enzyme và recombinant DNA

Restriction enzyme nhận chuỗi (sequence / 시퀀스) đặc hiệu và cắt DNA. DNA ligase nối fragment.

Plasmid véc-tơ (vector / 벡터) có origin replication, selectable marker và cloning site. Insert được ligate vào plasmid rồi đưa vào bacteria để propagate/expression.

Recombinant DNA là “assembly” dựa recognition chuỗi (sequence / 시퀀스) và cellular bộ máy sao chép (replication machinery).

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **8. Transformation và chọn lọc (selection)** tiếp nhận điểm tựa từ **7. Restriction enzyme và recombinant DNA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. DNA sequencing: từ molecule thành string dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Transformation và chọn lọc (selection)

Không phải bacterial cell nào cũng nhận plasmid. Selectable marker như kháng kháng sinh (antibiotic resistance) trong lab giúp giữ cell mang plasmid trên medium có antibiotic tương ứng.

Đây là artificial selection ở microbial culture.

Marker lab cần biosafety và thiết kế (design / 설계) phù hợp; concept không đồng nghĩa clinical resistance management.

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **8. Transformation và chọn lọc (selection)** nêu điều cần giải thích; **9. DNA sequencing: từ molecule thành string dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Sequencing chuỗi xử lý (pipeline / 파이프라인) cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. DNA sequencing: từ molecule thành string dữ liệu (data / 데이터)

Sanger sequencing dùng chain-terminating nucleotide để đọc chuỗi (sequence / 시퀀스), phù hợp fragment nhỏ/kiểm tra hợp lệ (validation / 검증).

Next-generation sequencing song song hóa hàng triệu fragment, tạo massive read dataset.

Long-read nền tảng (platform / 플랫폼) đọc fragment dài hơn, hữu ích cho repeat, structural variant và assembly.

Không nền tảng (platform / 플랫폼) nào “tốt nhất”; choice phụ thuộc read length, độ chính xác (accuracy), thông lượng (throughput / 처리량), chi phí (cost / 비용) và câu hỏi (question).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **9. DNA sequencing: từ molecule thành string dữ liệu (data / 데이터)** nêu điều cần giải thích; **10. Sequencing chuỗi xử lý (pipeline / 파이프라인) cơ bản** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. FASTA và FASTQ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Sequencing chuỗi xử lý (pipeline / 파이프라인) cơ bản

Một genomics chuỗi xử lý (pipeline / 파이프라인) có dòng chảy (flow):

```text
biological sample
→ nucleic-acid extraction
→ library preparation
→ sequencing
→ raw reads
→ quality control
→ alignment/assembly
→ quantification/variant calling
→ statistics
→ biological interpretation
```

Mỗi arrow có giả định (assumption / 가정) và nguồn (source / 소스) lỗi (error / 오류). “dữ liệu (data / 데이터) từ máy” chưa phải kết luận sinh học (biological conclusion).

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **10. Sequencing chuỗi xử lý (pipeline / 파이프라인) cơ bản** xác định đầu vào; **11. FASTA và FASTQ** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **12. Căn chỉnh (alignment): tìm correspondence giữa chuỗi (sequence / 시퀀스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. FASTA và FASTQ

FASTA lưu chuỗi (sequence / 시퀀스) với header. FASTQ lưu chuỗi (sequence / 시퀀스) kèm điểm chất lượng (quality score) cho từng cơ sở (base / 기반).

Biểu diễn (representation / 표현) này quan trọng vì bioinformatics làm việc trên tệp (file / 파일)/cấu trúc dữ liệu (data structure / 자료구조), không trực tiếp trên tube DNA.

Biology chuyển thành computer-readable symbols.

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **11. FASTA và FASTQ** xác định đầu vào; **12. Căn chỉnh (alignment): tìm correspondence giữa chuỗi (sequence / 시퀀스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **13. BLAST: similarity tìm kiếm (search / 검색) không phải proof of hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Căn chỉnh (alignment): tìm correspondence giữa chuỗi (sequence / 시퀀스)

Căn chỉnh trình tự (sequence alignment) có thể toàn cục (global / 전역) hoặc cục bộ (local / 로컬).

Động (dynamic / 동적) programming thuật toán (algorithm / 알고리즘) như Needleman–Wunsch/Smith–Waterman tối ưu score theo match, mismatch và gap.

Thời gian (time / 시간) độ phức tạp (complexity / 복잡도) của chính xác (exact / 정확한) alignment làm database-scale tìm kiếm (search / 검색) cần heuristic/chỉ mục (index / 인덱스) chiến lược (strategy / 전략).

Đây là nơi khoa học máy tính (computer science / 컴퓨터 과학) giải biological quy mô (scale / 규모) bài toán (problem / 문제).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **12. Căn chỉnh (alignment): tìm correspondence giữa chuỗi (sequence / 시퀀스)** xác định đầu vào; **13. BLAST: similarity tìm kiếm (search / 검색) không phải proof of hàm (function / 함수)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **14. Genome assembly như bài toán reconstruction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. BLAST: similarity tìm kiếm (search / 검색) không phải proof of hàm (function / 함수)

BLAST tìm cục bộ (local / 로컬) chuỗi (sequence / 시퀀스) similarity nhanh bằng heuristic.

High similarity có thể gợi ý homology/chức năng (function), nhưng hàm (function / 함수) annotation cần ngữ cảnh (context / 맥락), lĩnh vực (domain / 도메인), phylogeny và thí nghiệm (experiment).

“BLAST hit = cùng hàm (function / 함수)” là shortcut nguy hiểm.

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **14. Genome assembly như bài toán reconstruction** tiếp nhận điểm tựa từ **13. BLAST: similarity tìm kiếm (search / 검색) không phải proof of hàm (function / 함수)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Gọi biến thể (variant calling)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Genome assembly như bài toán reconstruction

Nếu genome bị cắt thành reads, assembly phải reconstruct original chuỗi (sequence / 시퀀스).

Short-read assembler thường dùng de Bruijn đồ thị (graph / 그래프): k-mer là nút (node / 노드)/edge tùy formulation và overlap tạo đường dẫn (path / 경로).

Repeat tạo ambiguity vì cùng chuỗi (sequence / 시퀀스) xuất hiện nhiều nơi.

Long read giúp cầu nối (bridge / 브리지) repeat nhưng cũng có lỗi (error / 오류)/chi phí (cost / 비용) sự đánh đổi (trade-off / 트레이드오프).

Lý thuyết đồ thị (graph theory) trực tiếp trở thành genomics công cụ (tool / 도구).

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **15. Gọi biến thể (variant calling)** tiếp nhận điểm tựa từ **14. Genome assembly như bài toán reconstruction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. RNA-seq** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Gọi biến thể (variant calling)

Alignment read với tham chiếu (reference / 참조) cho phép detect SNV, indel và structural variant.

Nhưng sequencing lỗi (error / 오류), ánh xạ (mapping / 매핑) ambiguity, coverage thấp và mẫu (sample / 표본) mixture có thể tạo false lời gọi (call / 호출).

Variant caller dùng statistical/probabilistic mô hình (model / 모델) để phân biệt tín hiệu (signal / 신호) khỏi noise.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **16. RNA-seq** tiếp nhận điểm tựa từ **15. Gọi biến thể (variant calling)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Single-tế bào (cell) sequencing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. RNA-seq

RNA được chuyển thành cDNA/thư viện (library / 라이브러리) rồi sequencing. Read được map/quantify để estimate mức độ phong phú của bản phiên mã (transcript abundance).

Biểu hiện khác biệt (differential expression) phân tích (analysis / 분석) so điều kiện (condition / 조건) nhưng cần normalization, replicate và mô hình (model / 모델) count phân phối (distribution / 분포).

P-value nhỏ không tự có biological importance; tác động (effect / 효과) kích thước (size / 크기) và ngữ cảnh (context / 맥락) cần đi cùng.

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **17. Single-tế bào (cell) sequencing** tiếp nhận điểm tựa từ **16. RNA-seq** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Dimension reduction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Single-tế bào (cell) sequencing

Single-cell RNA-seq gắn barcode theo tế bào, cho phép profile thousands cell.

Chuỗi xử lý (pipeline / 파이프라인) thường gồm filtering, normalization, giảm chiều dữ liệu (dimensionality reduction), clustering, marker phân tích (analysis / 분석) và trajectory suy luận (inference / 추론).

Mỗi bước transform dữ liệu (data / 데이터); cluster là computational construct cần biological kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **18. Dimension reduction** tiếp nhận điểm tựa từ **17. Single-tế bào (cell) sequencing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. CRISPR-Cas genome editing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Dimension reduction

Gen (gene)-expression ma trận (matrix / 행렬) có hàng nghìn dimension. PCA tìm tuyến tính (linear / 선형) direction variance lớn; t-SNE/UMAP tạo low-dimensional visualization nonlinear.

Khoảng cách trên UMAP/t-SNE không nên đọc quá literal như vật lý (physical / 물리적) distance; parameter và tiền xử lý (preprocessing) ảnh hưởng hình.

Visualization là mô hình (model / 모델), không phải raw reality.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **19. CRISPR-Cas genome editing** tiếp nhận điểm tựa từ **18. Dimension reduction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. cơ sở (base / 기반) editing và prime editing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. CRISPR-Cas genome editing

Guide RNA đưa Cas nuclease tới mục tiêu (target / 대상) chuỗi (sequence / 시퀀스) có complementarity và PAM phù hợp. Cas tạo cut; cell repair qua NHEJ hoặc HDR có thể tạo edit.

NHEJ thường gây indel, hữu ích knockout. HDR có thể đưa template-defined thay đổi (change / 변경) nhưng efficiency/ngữ cảnh (context / 맥락) khác.

CRISPR không “viết DNA tùy ý không giới hạn”; delivery, off-target, repair biology và loại tế bào (cell type) là ràng buộc (constraint / 제약조건).

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **20. cơ sở (base / 기반) editing và prime editing** tiếp nhận điểm tựa từ **19. CRISPR-Cas genome editing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Functional genomics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. cơ sở (base / 기반) editing và prime editing

Cơ sở (base / 기반) editor kết hợp targeting CRISPR với deaminase để đổi cơ sở (base / 기반) nhất định không cần đứt gãy hai mạch (double-strand break) cổ điển trong nhiều thiết kế (design / 설계).

Prime editing dùng reverse-transcriptase-based cơ chế (mechanism / 메커니즘) và pegRNA để viết edit linh hoạt hơn ở một số bối cảnh (context).

Mỗi công cụ (tool / 도구) có edit cửa sổ (window / 윈도우), byproduct và delivery ràng buộc (constraint / 제약조건) riêng.

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **21. Functional genomics** tiếp nhận điểm tựa từ **20. cơ sở (base / 기반) editing và prime editing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Sinh học tổng hợp (synthetic biology)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Functional genomics

CRISPR screen, RNAi hoặc overexpression screen perturb thousands gene rồi đo kiểu hình (phenotype).

Observation genomics tìm association; functional genomics cố tạo nhân quả (causal / 인과적) bằng chứng (evidence / 증거) bằng perturbation.

Kết hợp screening + giải trình tự (sequencing) biến cell population thành high-throughput experiment.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **22. Sinh học tổng hợp (synthetic biology)** gom các mảnh từ **21. Functional genomics** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **23. Mạch di truyền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Sinh học tổng hợp (synthetic biology)

Sinh học tổng hợp cố thiết kế mạch di truyền (genetic circuit), con đường chuyển hóa (metabolic pathway) hoặc cell hành vi (behavior / 동작) với kỹ thuật (engineering / 엔지니어링) mindset.

Promoter, ribosome-binding site, regulator và sensor có thể xem như mô-đun (module / 모듈), nhưng biological thành phần (component / 컴포넌트) không hoàn toàn orthogonal như electronic part; ngữ cảnh (context / 맥락) và burden gây tương tác (interaction / 상호작용).

Kỹ thuật (engineering / 엔지니어링) life cần hiểu noise, evolution và host physiology.

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **23. Mạch di truyền** gom các mảnh từ **22. Sinh học tổng hợp (synthetic biology)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **24. Kỹ thuật chuyển hóa (metabolic engineering)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Mạch di truyền

Một toggle switch có thể dùng two repressors ức chế nhau để tạo tính lưỡng ổn (bistability). Oscillator dùng delayed phản hồi âm (negative feedback).

Circuit hành vi (behavior / 동작) xuất hiện từ mạng lưới (network) dynamics chứ không chỉ thành phần (component / 컴포넌트) danh sách (list / 목록).

Đây là sinh học hệ thống theo hướng thiết kế (design / 설계).

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **24. Kỹ thuật chuyển hóa (metabolic engineering)** tiếp nhận điểm tựa từ **23. Mạch di truyền** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Sinh học hệ thống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Kỹ thuật chuyển hóa (metabolic engineering)

Ta có thể redirect flux để microbe tạo drug, enzym (enzyme), biofuel hoặc chemical.

Nhưng tăng một enzyme chưa chắc tăng sản phẩm (product / 제품) nếu pathway bottleneck chuyển sang step khác hoặc cofactor thiếu.

Flux balance và systems-level mô hình (model / 모델) giúp identify bottleneck.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **25. Sinh học hệ thống** tiếp nhận điểm tựa từ **24. Kỹ thuật chuyển hóa (metabolic engineering)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Mạng lưới sinh học (biology)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Sinh học hệ thống

Sinh học hệ thống hỏi: mạng lưới đáp ứng (response) theo thời gian (time / 시간) thế nào khi thành phần (component / 컴포넌트) tương tác?

Mô hình (model / 모델) có thể dùng ordinary differential equation:

\[
\frac{dx_i}{dt}=f_i(x_1,x_2,...,u)
\]

Mỗi \(x_i\) là concentration/hoạt động (activity); hàm (function / 함수) mô tả sự tạo ra (production)/phân giải (degradation)/interactions.

Parameter fitting và phân tích độ nhạy (sensitivity analysis) giúp tìm điều khiển (control / 제어) điểm (point / 지점).

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **26. Mạng lưới sinh học (biology)** tiếp nhận điểm tựa từ **25. Sinh học hệ thống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Học máy (machine learning) trong Sinh học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Mạng lưới sinh học (biology)

Đồ thị (graph / 그래프) biểu diễn (representation / 표현):

- nút: gen/protein (protein)/metabolite/loài (species);
- edge: điều hòa (regulation), liên kết (binding), reaction, feeding.

Degree, centrality, motif và quần xã (community) cấu trúc (structure / 구조) có thể gợi ý organization.

Nhưng mạng (network / 네트워크) cơ sở dữ liệu (database / 데이터베이스) có sai lệch (bias); high-degree nút (node / 노드) đôi khi vì được nghiên cứu nhiều.

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **27. Học máy (machine learning) trong Sinh học** tiếp nhận điểm tựa từ **26. Mạng lưới sinh học (biology)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Supervised và unsupervised học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Học máy (machine learning) trong Sinh học

ML có thể classify loại tế bào, predict cấu trúc protein (protein structure)/đặc tính (property), interpret microscopy, prioritize variant hoặc mô hình (model / 모델) trình tự.

Nhưng mô hình (model / 모델) hiệu năng (performance / 성능) phụ thuộc huấn luyện (training / 학습) phân phối (distribution / 분포). Dataset leakage, lớp (class / 클래스) imbalance và quần thể (population) độ lệch (bias / 편향) có thể làm chỉ số (metric / 지표) đẹp nhưng generalization kém.

Biological ML cần bên ngoài (external / 외부) kiểm tra hợp lệ (validation / 검증) và nhân quả (causal / 인과적) caution.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **28. Supervised và unsupervised học tập (learning / 학습)** tiếp nhận điểm tựa từ **27. Học máy (machine learning) trong Sinh học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Cấu trúc protein prediction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Supervised và unsupervised học tập (learning / 학습)

Supervised học tập (learning / 학습) cần label; unsupervised tìm cấu trúc (structure / 구조) không có label rõ.

Clustering biểu hiện gen (gene expression) là unsupervised-ish discovery; disease classifier là supervised.

Không nên gọi mọi statistics trên biological dữ liệu (data / 데이터) là “AI”. công cụ (tool / 도구) phải phù hợp question.

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **29. Cấu trúc protein prediction** tiếp nhận điểm tựa từ **28. Supervised và unsupervised học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. cơ sở dữ liệu (database / 데이터베이스) và reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Cấu trúc protein prediction

Protein chuỗi (sequence / 시퀀스) chứa ràng buộc (constraint / 제약조건) shape nhưng folding chịu physics/bối cảnh. hiện đại (modern / 현대적) deep-learning mô hình (model / 모델) có thể predict cấu trúc (structure / 구조) rất tốt ở nhiều trường hợp (case / 사례).

Tuy nhiên cấu trúc (structure / 구조) prediction không tự cho chức năng, động lực học, tương tác (interaction / 상호작용) hay tác động (effect / 효과) mutation đầy đủ.

Experimental structural biology vẫn quan trọng.

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **29. Cấu trúc protein prediction** nêu điều cần giải thích; **30. cơ sở dữ liệu (database / 데이터베이스) và reproducibility** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **31. Causality: omics correlation không đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. cơ sở dữ liệu (database / 데이터베이스) và reproducibility

Bioinformatics workflow dùng hệ gen tham chiếu (reference genome), annotation phiên bản (version / 버전), software phiên bản (version / 버전) và tham số (parameter). Kết quả có thể thay khi tham chiếu (reference / 참조)/công cụ (tool / 도구) đổi.

Reproducible phân tích (analysis / 분석) cần phiên bản (version / 버전) điều khiển (control / 제어), môi trường (environment / 환경)/bộ chứa (container / 컨테이너), siêu dữ liệu (metadata / 메타데이터) và workflow documentation.

Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) trở thành một phần scientific rigor.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **30. cơ sở dữ liệu (database / 데이터베이스) và reproducibility** nêu điều cần giải thích; **31. Causality: omics correlation không đủ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **32. Ethics và quản trị (governance / 거버넌스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Causality: omics correlation không đủ

Nếu gene X expression cao ở bệnh (disease), có thể X gây disease, disease làm X tăng hoặc third factor làm cả hai.

Perturbation experiment, temporal dữ liệu (data / 데이터), genetic instrument hoặc nhân quả (causal / 인과적) mô hình (model / 모델) giúp phân biệt.

High-dimensional dữ liệu (data / 데이터) làm false correlation dễ xuất hiện; kiểm định nhiều lần (multiple testing) và replication bắt buộc.

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **32. Ethics và quản trị (governance / 거버넌스)** tiếp nhận điểm tựa từ **31. Causality: omics correlation không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Tình huống phân tích (case study): từ patient mẫu (sample / 표본) tới variant diễn giải (interpretation)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Ethics và quản trị (governance / 거버넌스)

Genome dữ liệu (data / 데이터) có privacy implication; gene editing germline có intergenerational consequence; synthetic organism có biosafety concern.

Technical ability không tự trả lời “nên làm hay không”. Ethics, điều hòa, informed consent và equity phải đi cùng technology.

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **32. Ethics và quản trị (governance / 거버넌스)** cho ta quy tắc; **33. Tình huống phân tích (case study): từ patient mẫu (sample / 표본) tới variant diễn giải (interpretation)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **34. Tình huống phân tích: engineered insulin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Tình huống phân tích (case study): từ patient mẫu (sample / 표본) tới variant diễn giải (interpretation)

Blood/mô (tissue) → DNA extraction → giải trình tự → căn chỉnh → gọi biến thể → annotation → quần thể tần số (frequency) → predicted consequence → clinical correlation/functional bằng chứng (evidence / 증거).

Mỗi bước giảm bất định (uncertainty / 불확실성) nhưng không xóa hoàn toàn.

Một report tốt phải phân biệt observation, suy luận (inference / 추론) và độ tin cậy (confidence).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **33. Tình huống phân tích (case study): từ patient mẫu (sample / 표본) tới variant diễn giải (interpretation)** cho ta quy tắc; **34. Tình huống phân tích: engineered insulin** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **35. Các hiểu lầm phổ biến (common misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Tình huống phân tích: engineered insulin

Human insulin gene/cDNA được đưa vào microbial expression hệ thống (system / 시스템); cell culture sản xuất recombinant protein; purification/kiểm soát chất lượng (quality control) tạo therapeutic sản phẩm (product / 제품).

Technology này kết nối biểu hiện gen, plasmid, lên men, sự gấp cuộn protein (protein folding) và industrial tiến trình (process / 프로세스).

> **Chuyển mạch:** Trong **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **34. Tình huống phân tích: engineered insulin** cho ta quy tắc; **35. Các hiểu lầm phổ biến (common misconceptions)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Biotechnology hiện đại là vòng thiết kế (design / 설계)–bản dựng (build / 빌드)–kiểm thử (test / 테스트)–Learn, không phải danh sách công cụ (tool / 도구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Các hiểu lầm phổ biến (common misconceptions)

“PCR cho biết có gene hoạt động” sai; tiêu chuẩn (standard / 표준) PCR chỉ detect/amplify DNA mục tiêu (target / 대상), activity cần expression assay.

“Giải trình tự đọc được genome hoàn hảo” sai; coverage, repeat và lỗi (error / 오류) tạo độ bất định (uncertainty / 불확실성).

“CRISPR cắt đúng 100%” sai; targeting/off-target/delivery/repair có giới hạn (limitation).

“More omics dữ liệu (data / 데이터) = more understanding” sai nếu question/mô hình (model / 모델) yếu.

“AI tìm được correlation thì đó là cơ chế (mechanism / 메커니즘)” sai.

<!-- depth-audit-2026:dbtl-causal-engineering -->

> **Chuyển mạch:** Ở chặng này của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **Biotechnology hiện đại là vòng thiết kế (design / 설계)–bản dựng (build / 빌드)–kiểm thử (test / 테스트)–Learn, không phải danh sách công cụ (tool / 도구)** tiếp nhận điểm tựa từ **35. Các hiểu lầm phổ biến (common misconceptions)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. cầu nối (bridge / 브리지) sang connections: Sinh học đang dùng lại cùng một số idea toán học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biotechnology hiện đại là vòng thiết kế (design / 설계)–bản dựng (build / 빌드)–kiểm thử (test / 테스트)–Learn, không phải danh sách công cụ (tool / 도구)

Sinh học kỹ thuật (engineering biology) thường chạy theo vòng **thiết kế → xây dựng → kiểm thử → học (Design–Build–Test–Learn, DBTL)**. thiết kế (design / 설계) chọn cơ chế (mechanism / 메커니즘) và mục tiêu (target / 대상); bản dựng (build / 빌드) tạo construct/cell line; kiểm thử (test / 테스트) đo phenotype; Learn cập nhật mô hình (model / 모델) rồi quay lại thiết kế (design / 설계). Nếu đo lường (measurement / 측정) không phản ánh đúng cơ chế (mechanism / 메커니즘), vòng lặp có thể tối ưu nhầm mục tiêu (objective / 목표) dù kỹ thuật thực hiện hoàn hảo.

CRISPR minh họa rõ cấu trúc (structure / 구조) → cơ chế (mechanism / 메커니즘) → thất bại (failure / 실패). Guide RNA xác định recognition; Cas tạo hoặc xúc tác biến đổi tại mục tiêu (target / 대상); DNA repair quyết định kết quả (outcome / 결과) cuối. thất bại (failure / 실패) có thể đến từ off-target, on-target rearrangement, delivery không đều hoặc mosaicism. Vì vậy “edit thành công” phải được định nghĩa bằng genotype, expression, phenotype và unintended tác động (effect / 효과) chứ không chỉ thấy một band PCR đúng kích thước.

Perturbation mạnh hơn observation cho nhân quả (causal / 인과적) suy luận (inference / 추론) nhưng vẫn cần điều khiển (control / 제어). Knockout có thể gây compensation; overexpression có thể tạo mức protein phi sinh lý; cell line khác organism. Biotechnology tốt luôn hỏi intervention đang thay nút (node / 노드) nào, mạng (network / 네트워크) có phản hồi (feedback / 피드백) gì và mô hình (model / 모델) organism bỏ qua tầng (layer / 계층) nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công nghệ sinh học, Tin sinh học và các hệ thống (systems / 시스템들) Biology — Biotechnology, Bioinformatics and các hệ thống (systems / 시스템들) Biology (생명공학, 생물정보학과 시스템생물학)**, **36. cầu nối (bridge / 브리지) sang connections: Sinh học đang dùng lại cùng một số idea toán học** tiếp nhận điểm tựa từ **Biotechnology hiện đại là vòng thiết kế (design / 설계)–bản dựng (build / 빌드)–kiểm thử (test / 테스트)–Learn, không phải danh sách công cụ (tool / 도구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 36. cầu nối (bridge / 브리지) sang connections: Sinh học đang dùng lại cùng một số idea toán học

Tới đây ta đã thấy exponential amplification, logarithm, xác suất (probability / 확률), đồ thị (graph / 그래프), hệ động (dynamic system / 동적 시스템), tối ưu hóa (optimization / 최적화) và statistics xuất hiện liên tục.

[Biology × Mathematics × Computation × Scale](../90_connections/00_biology_math_computation_and_scale.md) sẽ gom các motif này lại để cho thấy Sinh học, Toán và Khoa học máy tính (computer science / 컴퓨터 과학) không phải ba lĩnh vực (domain / 도메인) đứng cạnh nhau mà là ba cách mô tả cùng hệ thống (system / 시스템).

> **Mô hình tư duy cuối chapter:** biotechnology là “biology made operational”. Ta không thể edit hay mô hình (model / 모델) một hệ thống (system / 시스템) nếu không hiểu cơ chế (mechanism / 메커니즘); cũng không thể hiểu dữ liệu hiện đại nếu thiếu xác suất (probability / 확률), algorithms và tư duy hệ thống (systems thinking). Công nghệ mạnh nhất xuất hiện khi molecular insight, quantitative mô hình (model / 모델) và kỹ thuật (engineering / 엔지니어링) discipline gặp nhau.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Quần xã sinh học, biến đổi toàn cầu và sinh quyển](../05_ecology/02_biomes_global_change_and_biosphere.md) · [Mục lục Biology](../README.md) · [Phương pháp thực nghiệm và đo lường trong Sinh học →](01_experimental_methods_and_measurement.md)

> **Bàn giao:** Sau **36. cầu nối (bridge / 브리지) sang connections: Sinh học đang dùng lại cùng một số idea toán học**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
