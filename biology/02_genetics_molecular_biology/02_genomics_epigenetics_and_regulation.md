# Genomics, Epigenetics và Điều hòa hệ gene — Genomics, Epigenetics and Regulation (유전체학, 후성유전학과 조절)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Genomics, Epigenetics và Điều hòa hệ gene — Genomics, Epigenetics and Regulation (유전체학, 후성유전학과 조절)**. Route đi từ genome và chromatin → accessibility/epigenetic marks → enhancer, promoter và mạng điều hòa → biểu hiện theo mô, thời gian và môi trường, để “có gene” không bị đồng nhất với “gene đang hoạt động”.

Hai chapter trước đi từ DNA chuỗi (sequence / 시퀀스) tới protein rồi sang inheritance. Bây giờ ta zoom out. Một cell không vận hành bằng một gene riêng lẻ mà bằng **toàn bộ genome và mạng lưới điều hòa (regulatory network)**. Hàng nghìn gene có thể thay expression cùng lúc; chromatin quyết định vùng nào accessible; environmental tín hiệu (signal / 신호) đổi transcriptional program; population chứa hàng triệu variant.

Chapter này trả lời câu hỏi: **làm thế nào genome lớn được tổ chức, điều hòa và đo lường ở quy mô toàn hệ?**

> **mô hình tư duy (mental model / 사고 모델):** genomics không phải “genetics nhưng nhiều gene hơn”. Nó thay đổi đơn vị tư duy từ locus riêng lẻ sang mẫu (pattern / 패턴) toàn genome, mạng (network / 네트워크) và tín hiệu thống kê (statistical signal) trong dữ liệu lớn.

## 1. Genome không chỉ là danh sách gene

Eukaryotic genome gồm coding gene, RNA không mã hóa (noncoding RNA) gen (gene), promoter, enhancer, repeat, centromere, telomere và nhiều region có chức năng (function)/regulatory lịch sử (history / 이력) khác nhau.

Protein (protein)-trình tự mã hóa (coding sequence) chỉ chiếm một phần nhỏ genome human. Nhưng không nên nhảy từ đó tới kết luận “mọi DNA không mã hóa (noncoding DNA) đều functional”. Một phần có regulatory role, một phần structural/repetitive, một phần có thể gần neutral.

Genomics phải phân biệt **chuỗi (sequence / 시퀀스) tồn tại** với **chuỗi (sequence / 시퀀스) có selected biological hàm (function / 함수)**.

> **Nối mạch:** Genome includes regulatory context, not only gene list; chromatin adds organization, and euchromatin/heterochromatin form a dynamic accessibility spectrum.

## 2. Chromatin tạo tầng (layer / 계층) organization đầu tiên

DNA eukaryote quấn quanh histone tạo nucleosome. Nucleosome tiếp tục organize thành higher-order chromatin.

DNA packaging giải hai bài toán tưởng mâu thuẫn:

- compact genome rất dài vào nucleus;
- vẫn cho sao chép (replication)/phiên mã (transcription)/repair machinery truy cập đúng nơi.

Vì vậy chromatin không phải packaging thụ động. Nó là regulatory substrate.

> **Nối mạch:** Chromatin provides the regulatory substrate; accessibility varies by locus, cell type, and time, while histone marks modify that state through writer–reader–eraser networks rather than a fixed on/off dictionary.

## 3. Euchromatin và heterochromatin là spectrum, không phải hai hộp tuyệt đối

**Euchromatin** thường accessible/transcriptionally active hơn; **heterochromatin** compact hơn và thường ít active.

Nhưng trạng thái nhiễm sắc chất (chromatin state) phụ thuộc locus, loại tế bào (cell type) và thời gian (time / 시간). Một region có thể đổi khả năng tiếp cận (accessibility / 접근성) khi differentiation hoặc signaling.

Hệ gen (genome) giống thư viện (library / 라이브러리) mà mỗi loại tế bào mở một subset shelf khác nhau.

> **Nối mạch:** Euchromatin/heterochromatin describe an accessibility spectrum; histone acetylation or methylation changes reader recruitment in context, and DNA methylation adds a complementary memory layer.

## 4. Biến đổi histone (histone modification): “mã (code / 코드)” nhưng không phải dictionary đơn giản

Histone tail có thể acetylated, methylated, phosphorylated và nhiều modification khác.

Acetyl hóa histone (histone acetylation) thường liên hệ chromatin accessible hơn vì giảm positive charge/thu hút reader protein, nhưng nhân quả (causal / 인과적) tác động (effect / 효과) phụ thuộc ngữ cảnh (context / 맥락).

Methyl hóa histone (histone methylation) đặc biệt không có nghĩa “methylation = repression”; vị trí residue quyết định association. H3K4me3 thường liên hệ active promoter, H3K27me3 thường repression trong ngữ cảnh (context / 맥락) eukaryote.

Không nên học epigenetics như bảng “mark này bật, mark kia tắt” mà phải hiểu mark nằm trong mạng (network / 네트워크) writer–reader–eraser.

> **Nối mạch:** Histone marks recruit regulatory machinery at particular residues; CpG methylation can stabilize repression or cell memory, but its developmental dynamics require a precise definition of epigenetics rather than a universal “silencing” rule.

## 5. Methyl hóa DNA (DNA methylation)

Ở mammals, Methyl hóa DNA thường xảy ra tại cytosine trong CpG ngữ cảnh (context / 맥락). Promoter CpG methylation có thể liên hệ transcriptional repression, nhưng genome-wide interpretation phức tạp hơn.

Methylation mẫu (pattern / 패턴) có thể được bản sao (copy / 복사) tương đối qua phân chia tế bào (cell division), tạo một phần cellular bộ nhớ (memory / 메모리).

Nhưng methylation cũng động (dynamic / 동적) trong phát triển (development), germline và bệnh (disease).

> **Nối mạch:** DNA methylation is one mechanism among chromatin states and heritable regulation; the definition must distinguish somatic memory from stronger transgenerational claims before scaling to X-chromosome inactivation.

## 6. Epigenetics chính xác là gì?

Thuật ngữ **epigenetics** thường bị dùng quá rộng. Một definition hữu ích là study of heritable/stable thay đổi (change / 변경) in điều hòa gen (gene regulation) or trạng thái nhiễm sắc chất không yêu cầu thay đổi (change / 변경) DNA chuỗi (sequence / 시퀀스).

Trong somatic cell, epigenetic bộ nhớ (memory / 메모리) giúp daughter cell giữ định danh (identity / 식별자). Trong transgenerational inheritance, claim phải mạnh hơn: mark/tác động (effect / 효과) phải vượt qua germline reprogramming và truyền qua generation.

Ở mammals, nhiều epigenetic mark bị reset mạnh trong gametogenesis/early embryo. Vì vậy câu “stress của bố mẹ chắc chắn truyền epigenetically cho cháu” cần bằng chứng (evidence / 증거) rất cẩn thận.

> **Nối mạch:** **7. X-chromosome inactivation: epigenetic regulation ở chromosome quy mô (scale / 규모)** nối từ **6. Epigenetics chính xác là gì?** sang **8. In dấu hệ gen (genomic imprinting): parent-of-origin tác động (effect / 효과)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. X-chromosome inactivation: epigenetic regulation ở chromosome quy mô (scale / 규모)

Ở female mammals, một X chromosome phần lớn bị inactivate để balance dosage với male XY.

Long RNA không mã hóa XIST và chromatin modification tham gia tiến trình (process / 프로세스). Inactivation xảy ra sớm trong development và được duy trì qua nhiều phân chia tế bào.

Kết quả là female tissue có mosaic cell dùng X maternal hoặc paternal khác nhau.

Đây là ví dụ epigenetic trạng thái (state / 상태) ổn định tạo phenotype mosaic mà DNA chuỗi (sequence / 시퀀스) không đổi.

> **Nối mạch:** **8. In dấu hệ gen (genomic imprinting): parent-of-origin tác động (effect / 효과)** nối từ **7. X-chromosome inactivation: epigenetic regulation ở chromosome quy mô (scale / 규모)** sang **9. Enhancer và 3D genome**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. In dấu hệ gen (genomic imprinting): parent-of-origin tác động (effect / 효과)

Một số gen biểu hiện khác nhau tùy allele đến từ bố hay mẹ do imprint mark được thiết lập trong germline.

Imprinting cho thấy hai allele cùng chuỗi (sequence / 시퀀스) không nhất thiết hàm (function / 함수) equivalent nếu epigenetic lịch sử (history / 이력) khác nhau.

Nhưng imprinting chỉ áp dụng subset gene; không phải quy tắc (rule / 규칙) chung của genome.

> **Nối mạch:** **9. Enhancer và 3D genome** nối từ **8. In dấu hệ gen (genomic imprinting): parent-of-origin tác động (effect / 효과)** sang **10. Cắt nối thay thế (alternative splicing) mở rộng transcriptome**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Enhancer và 3D genome

Enhancer có thể nằm rất xa promoter theo tuyến tính (linear / 선형) DNA nhưng ở gần trong 3D nucleus do chromatin folding.

Hệ gen được organize thành vòng lặp (loop / 루프)/lĩnh vực (domain / 도메인) làm regulatory element gặp mục tiêu (target / 대상) gene.

Do đó distance “trên chuỗi (sequence / 시퀀스)” và distance “trong không gian nucleus” là hai khái niệm khác.

Structural variant phá ranh giới (boundary / 경계) hoặc đưa enhancer gần gene khác có thể gây misregulation.

> **Nối mạch:** **10. Cắt nối thay thế (alternative splicing) mở rộng transcriptome** nối từ **9. Enhancer và 3D genome** sang **11. RNA regulation sau phiên mã**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Cắt nối thay thế (alternative splicing) mở rộng transcriptome

Một gene có thể tạo nhiều mRNA isoform bằng lựa chọn exon khác nhau. Splicing factor và tế bào (cell) trạng thái (state / 상태) quyết định mẫu (pattern / 패턴).

Vì vậy số protein isoform có thể lớn hơn số gen mã hóa protein (protein-coding gene).

Tuy nhiên không phải mọi transcript isoform đều stable/functional; omics dữ liệu (data / 데이터) cần kiểm tra hợp lệ (validation / 검증).

> **Nối mạch:** **11. RNA regulation sau phiên mã** nối từ **10. Cắt nối thay thế (alternative splicing) mở rộng transcriptome** sang **12. Protein mức (level / 수준) cũng là một tầng (layer / 계층) regulation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. RNA regulation sau phiên mã

mRNA stability, localization và translation efficiency được regulation bởi RNA-liên kết (binding) protein và miRNA.

**microRNA (miRNA / 마이크로RNA)** có thể base-pair mục tiêu (target / 대상) mRNA và giảm translation hoặc thúc degradation.

Điều hòa (regulation) sau phiên mã cho phép cell phản ứng nhanh mà không cần thay transcription ngay lập tức.

> **Nối mạch:** **12. Protein mức (level / 수준) cũng là một tầng (layer / 계층) regulation** nối từ **11. RNA regulation sau phiên mã** sang **13. “Omics” là gì?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Protein mức (level / 수준) cũng là một tầng (layer / 계층) regulation

Mức độ phong phú của bản phiên mã (transcript abundance) không đồng nghĩa mức độ phong phú của protein (protein abundance). Translation tỷ lệ (rate / 비율), phân giải protein (protein degradation), modification và định vị (localization) đều ảnh hưởng hàm (function / 함수).

Ubiquitin–proteasome hệ thống (system / 시스템) đánh dấu nhiều protein để phân giải (degradation).

Vì vậy RNA-seq chỉ quan sát một tầng (layer / 계층). Muốn hiểu phenotype cần tích hợp proteomics/metabolomics/functional assay.

> **Nối mạch:** **13. “Omics” là gì?** nối từ **12. Protein mức (level / 수준) cũng là một tầng (layer / 계층) regulation** sang **14. Giải trình tự (sequencing): đọc hàng triệu fragment rồi reconstruct picture**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. “Omics” là gì?

Các lĩnh vực (domain / 도메인) omics đo nhiều thành phần (component / 컴포넌트) cùng lúc:

- hệ gen học (genomics): DNA chuỗi (sequence / 시퀀스)/biến dị (variation);
- transcriptomics: RNA;
- epigenomics: chromatin/DNA mark;
- proteomics: protein;
- metabolomics: metabolite.

Không nên nghĩ multi-omics đơn giản là “càng nhiều dữ liệu (data / 데이터) càng tốt”. Mỗi tầng (layer / 계층) có nhiễu (noise), hiệu ứng lô (batch effect) và phép đo (measurement) độ lệch (bias / 편향) riêng; tích hợp (integration / 통합) cần mô hình (model / 모델) và biological question rõ.

> **Nối mạch:** **14. Giải trình tự (sequencing): đọc hàng triệu fragment rồi reconstruct picture** nối từ **13. “Omics” là gì?** sang **15. Hệ gen tham chiếu (reference genome) không phải “genome chuẩn của loài”**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Giải trình tự (sequencing): đọc hàng triệu fragment rồi reconstruct picture

Hiện đại (modern / 현대적) short-read sequencing tạo rất nhiều fragment chuỗi (sequence / 시퀀스). Bioinformatics phải quality-control, align vào tham chiếu (reference / 참조) hoặc assemble, rồi count/lời gọi (call / 호출) variant.

Một read ngắn không tự cho biết nó đến từ gene nào nếu region repetitive. ánh xạ (mapping / 매핑) bất định (uncertainty / 불확실성) là một limitation thực.

Long-read sequencing giúp resolve structural variant/repeat tốt hơn nhưng có sự đánh đổi (trade-off / 트레이드오프) về chi phí (cost / 비용)/lỗi (error / 오류)/nền tảng (platform / 플랫폼).

Technology choice phụ thuộc question.

> **Nối mạch:** Sequencing reconstructs hàng triệu fragment; reference genome cung cấp hệ quy chiếu nhưng không phải genome “chuẩn” duy nhất. **Variant calling** kiểm tra khác biệt có ý nghĩa gì.

## 15. Hệ gen tham chiếu (reference genome) không phải “genome chuẩn của loài”

Hệ gen tham chiếu là một coordinate khung phần mềm (framework / 프레임워크) được xây từ mẫu (sample / 표본)/assembly. Nó không đại diện mọi allele trong quần thể (population).

Hệ gen toàn quần thể (pangenome) approach cố biểu diễn diversity tốt hơn tuyến tính (linear / 선형) tham chiếu (reference / 참조) duy nhất.

Đây là ví dụ dữ liệu (data / 데이터) biểu diễn (representation / 표현) ảnh hưởng suy luận sinh học (biological inference).

> **Nối mạch:** Reference genome làm nền; variant calling mô tả khác biệt so với nền đó. **GWAS** kiểm tra khi association xuất hiện ở quy mô population.

## 16. Gọi biến thể (variant calling): chuỗi (sequence / 시퀀스) khác tham chiếu (reference / 참조) chưa chắc gây bệnh

Genomic variant có thể dùng chung (common / 공통)/rare, coding/noncoding, neutral/deleterious/beneficial tùy ngữ cảnh (context / 맥락).

Classification pathogenicity cần population tần số (frequency), functional bằng chứng (evidence / 증거), segregation, computational prediction và dữ liệu lâm sàng (clinical data).

Không thể nhìn “có đột biến (mutation)” rồi kết luận disease. Mọi người đều mang rất nhiều variant.

> **Nối mạch:** Variant calling cung cấp danh sách khác biệt; GWAS tìm association; **Linkage disequilibrium** kiểm tra vì biến thể đi cùng nhau làm inference khó hơn.

## 17. GWAS: tìm association ở quy mô quần thể (population scale)

**Nghiên cứu liên kết toàn hệ gen (genome-wide association study) (GWAS / 전장유전체 연관분석)** kiểm thử (test / 테스트) association giữa variant và trait trên genome.

Vì kiểm thử (test / 테스트) hàng triệu variant, multiple-testing correction rất nghiêm ngặt. Quần thể cấu trúc (structure / 구조) cũng có thể gây confounding.

GWAS tín hiệu (signal / 신호) thường chỉ ra region liên quan trait, không tự chứng minh variant nào nhân quả (causal / 인과적) hoặc cơ chế (mechanism / 메커니즘) gì.

Association phải được follow bằng fine ánh xạ (mapping / 매핑), functional experiment và biological lập luận (reasoning / 추론).

> **Nối mạch:** GWAS tìm association ở population scale; linkage disequilibrium giới hạn inference. **Polygenic score** tiếp tục bằng cách gộp nhiều biến thể có hiệu ứng nhỏ.

## 18. Mất cân bằng liên kết (linkage disequilibrium): biến thể (variant) đi cùng nhau làm suy luận (inference / 추론) khó hơn

Nearby allele có thể correlated trong quần thể do dùng chung (shared / 공유) ancestry/recombination lịch sử (history / 이력). Đây là **mất cân bằng liên kết, LD**.

Một SNP GWAS significant có thể chỉ là tag đi cùng nhân quả (causal / 인과적) variant.

Vì vậy statistical association và molecular causation là hai bước khác nhau.

> **Nối mạch:** **19. Điểm đa gen (polygenic score)** nối từ **18. Mất cân bằng liên kết (linkage disequilibrium): biến thể (variant) đi cùng nhau làm suy luận (inference / 추론) khó hơn** sang **20. Hệ gen học đơn tế bào (single-cell genomics): trung bình có thể che mất loại tế bào**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Điểm đa gen (polygenic score)

Nhiều complex trait chịu contribution từ rất nhiều variant tác động (effect / 효과) nhỏ. **Điểm đa gen** cộng weighted allele tác động (effect / 효과) từ GWAS.

Score có thể có predictive giá trị (value / 값) trong population tương tự dữ liệu huấn luyện (training data / 학습 데이터) nhưng transfer giữa ancestry/population có thể giảm vì LD, tần số alen (allele frequency) và môi trường (environment / 환경) khác.

Đây là limitation quan trọng khi đưa genomics vào medicine.

> **Nối mạch:** **20. Hệ gen học đơn tế bào (single-cell genomics): trung bình có thể che mất loại tế bào** nối từ **19. Điểm đa gen (polygenic score)** sang **21. Development như một bài toán regulatory trạng thái (state / 상태)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Hệ gen học đơn tế bào (single-cell genomics): trung bình có thể che mất loại tế bào

Bulk RNA-seq đo average của hàng triệu cell. Nếu tissue gồm nhiều loại tế bào, thay đổi (change / 변경) composition có thể bị nhầm là expression thay đổi (change / 변경) trong từng cell.

Single-cell RNA-seq tách profile từng cell (với sampling/noise limitation), cho phép identify loại tế bào/trạng thái (state / 상태) và trajectory.

Nhưng “cluster” trong dữ liệu (data / 데이터) không tự động bằng biological loại tế bào; annotation cần marker, ngữ cảnh (context / 맥락) và kiểm tra hợp lệ (validation / 검증).

> **Nối mạch:** **21. Development như một bài toán regulatory trạng thái (state / 상태)** nối từ **20. Hệ gen học đơn tế bào (single-cell genomics): trung bình có thể che mất loại tế bào** sang **22. Mạng lưới điều hòa gen (gene regulatory network)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Development như một bài toán regulatory trạng thái (state / 상태)

Fertilized egg tạo rất nhiều loại tế bào gần cùng genome. Difference đến từ mạng lưới điều hòa, trạng thái nhiễm sắc chất và signaling lịch sử (history / 이력).

Development có thể hình dung như hệ thống (system / 시스템) đi qua landscape trạng thái (state / 상태): tín hiệu (signal / 신호) activate yếu tố phiên mã (transcription factor), factor mở/đóng regulatory program, cell commitment dần ổn định.

Đây là cầu nối (bridge / 브리지) sang development chương (chapter).

> **Nối mạch:** **22. Mạng lưới điều hòa gen (gene regulatory network)** nối từ **21. Development như một bài toán regulatory trạng thái (state / 상태)** sang **23. Epigenetic bộ nhớ (memory / 메모리) và cell định danh (identity / 식별자)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Mạng lưới điều hòa gen (gene regulatory network)

Một yếu tố phiên mã có thể regulate nhiều gene; nhiều factor cùng điều khiển (control / 제어) một gene; phản hồi (feedback / 피드백) tạo stable trạng thái (state / 상태).

Mạng (network / 네트워크) motif như phản hồi dương (positive feedback) có thể khóa cell định danh (identity / 식별자). Phản hồi âm (negative feedback) giới hạn tín hiệu (signal / 신호). Feedforward vòng lặp (loop / 루프) có thể lọc transient đầu vào (input / 입력).

Molecular mạng (network / 네트워크) và tư duy hệ thống (systems thinking) gặp nhau trực tiếp ở đây.

> **Nối mạch:** **23. Epigenetic bộ nhớ (memory / 메모리) và cell định danh (identity / 식별자)** nối từ **22. Mạng lưới điều hòa gen (gene regulatory network)** sang **24. Environmental phản hồi (response / 응답) và plasticity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Epigenetic bộ nhớ (memory / 메모리) và cell định danh (identity / 식별자)

Khi cell divide, daughter cell cần không chỉ bản sao (copy / 복사) DNA mà còn khôi phục trạng thái nhiễm sắc chất và transcriptional program.

Một phần thông tin (information / 정보) được duy trì qua biến đổi histone, Methyl hóa DNA, phiên mã-factor mạng (network / 네트워크) và spatial organization.

Cell định danh (identity / 식별자) vì vậy là **trạng thái (state / 상태) của hệ thống (system / 시스템)**, không nằm trong một gene đơn độc.

> **Nối mạch:** **24. Environmental phản hồi (response / 응답) và plasticity** nối từ **23. Epigenetic bộ nhớ (memory / 메모리) và cell định danh (identity / 식별자)** sang **25. CRISPR screen: từ edit một gene sang kiểm thử (test / 테스트) hàng nghìn gene**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Environmental phản hồi (response / 응답) và plasticity

Môi trường (environment / 환경) có thể thay signaling, hormone và biểu hiện gen (gene expression). Dinh dưỡng (nutrition), căng thẳng (stress), temperature hoặc toxin có thể tạo molecular phản hồi (response / 응답).

Nhưng “môi trường (environment / 환경) thay gene” nên nói chính xác: thường môi trường (environment / 환경) đổi **expression/regulatory trạng thái (state / 상태)**, không đổi DNA chuỗi (sequence / 시퀀스) trừ khi gây mutation.

Phân biệt biến dị di truyền (genetic variation) với regulatory plasticity giúp tránh lẫn lộn.

> **Nối mạch:** **25. CRISPR screen: từ edit một gene sang kiểm thử (test / 테스트) hàng nghìn gene** nối từ **24. Environmental phản hồi (response / 응답) và plasticity** sang **26. Sinh học hệ thống (systems biology): từ danh sách (list / 목록) thành phần (component / 컴포넌트) sang mô hình (model / 모델) tương tác (interaction / 상호작용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. CRISPR screen: từ edit một gene sang kiểm thử (test / 테스트) hàng nghìn gene

CRISPR có thể dùng để knockout/perturb hàng nghìn gene trong quần thể tế bào. Sequencing barcode/guide abundance giúp tìm gene ảnh hưởng survival hoặc phenotype.

Đây là hệ gen học theo hướng nhân quả (causal / 인과적): không chỉ quan sát association mà perturb hệ thống (system / 시스템).

Kết hợp high-throughput perturbation với single-cell readout đang cho phép map mạng lưới điều hòa sâu hơn.

> **Nối mạch:** **26. Sinh học hệ thống (systems biology): từ danh sách (list / 목록) thành phần (component / 컴포넌트) sang mô hình (model / 모델) tương tác (interaction / 상호작용)** nối từ **25. CRISPR screen: từ edit một gene sang kiểm thử (test / 테스트) hàng nghìn gene** sang **27. Tình huống phân tích (case study): cùng genome, neuron và liver cell khác nhau thế nào?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Sinh học hệ thống (systems biology): từ danh sách (list / 목록) thành phần (component / 컴포넌트) sang mô hình (model / 모델) tương tác (interaction / 상호작용)

Khi dữ liệu (data / 데이터) quá nhiều, mục tiêu không còn là danh mục (catalog / 카탈로그). **Sinh học hệ thống (시스템생물학)** xây mô hình (model / 모델) mạng (network / 네트워크) và động lực học (dynamics).

Ví dụ mạng lưới chuyển hóa (metabolic network) có nút (node / 노드) là metabolite/reaction, mạng lưới điều hòa gen có nút (node / 노드) gen/protein, edge biểu diễn tương tác (interaction / 상호작용).

Lý thuyết đồ thị (graph theory), differential equation và statistical suy luận (inference / 추론) trở thành công cụ sinh học.

Xem thêm [Biology × Mathematics × Computation × Scale](../90_connections/00_biology_math_computation_and_scale.md).

> **Nối mạch:** **26. Sinh học hệ thống (systems biology): từ danh sách (list / 목록) thành phần (component / 컴포넌트) sang mô hình (model / 모델) tương tác (interaction / 상호작용)** nêu quy tắc; **27. Tình huống phân tích (case study): cùng genome, neuron và liver cell khác nhau thế nào?** thử quy tắc trong tình huống, rồi **28. Tình huống phân tích: variant regulatory có thể mạnh như coding variant** mở rộng hệ quả.

## 27. Tình huống phân tích (case study): cùng genome, neuron và liver cell khác nhau thế nào?

Neuron và hepatocyte có gần cùng DNA chuỗi (sequence / 시퀀스). Nhưng khả năng tiếp cận nhiễm sắc chất (chromatin accessibility) khác, yếu tố phiên mã khác, enhancer active khác, RNA/protein profile khác.

Liver cell expression enzyme chuyển hóa (metabolism)/detoxification; neuron expression kênh ion (ion channel), synaptic protein.

Difference phenotype không cần genome khác. Nó cần regulatory trạng thái (state / 상태) khác.

> **Nối mạch:** **27. Tình huống phân tích (case study): cùng genome, neuron và liver cell khác nhau thế nào?** nêu quy tắc; **28. Tình huống phân tích: variant regulatory có thể mạnh như coding variant** thử quy tắc trong tình huống, rồi **29. Các hiểu lầm phổ biến (common misconceptions)** mở rộng hệ quả.

## 28. Tình huống phân tích: variant regulatory có thể mạnh như coding variant

Nếu variant nằm enhancer và làm yếu tố phiên mã bind yếu hơn, gene mục tiêu (target / 대상) có thể expression thấp trong mô (tissue)/thời gian (time / 시간) cụ thể.

Protein chuỗi (sequence / 시퀀스) hoàn toàn bình thường nhưng amount/timing sai vẫn tạo kiểu hình (phenotype).

Genetics hiện đại vì vậy phải nhìn cả coding lẫn regulatory genome.

> **Nối mạch:** **28. Tình huống phân tích: variant regulatory có thể mạnh như coding variant** nêu quy tắc; **29. Các hiểu lầm phổ biến (common misconceptions)** thử quy tắc trong tình huống, rồi **Genome chuỗi (sequence / 시퀀스) và cell trạng thái (state / 상태) là hai lớp thông tin tương tác** mở rộng hệ quả.

## 29. Các hiểu lầm phổ biến (common misconceptions)

“Epigenetic = bất kỳ thứ gì không phải DNA chuỗi (sequence / 시퀀스)” quá rộng.

“Methylation luôn tắt gene” sai.

“RNA mức (level / 수준) nói chính xác protein mức (level / 수준)” sai.

“GWAS variant là nguyên nhân” chưa chắc.

“Hệ gen tham chiếu là genome bình thường duy nhất” sai.

“Single-cell dữ liệu (data / 데이터) trực tiếp cho loại tế bào thật” sai; clustering là mô hình (model / 모델) cần interpretation.

<!-- depth-audit-2026:genome-state-causality -->

> **Nối mạch:** Misconceptions cần được đối chiếu với hai lớp: genome sequence và cell state. **Mạng điều hòa** giải thích vì sao cùng genome vẫn tạo cell khác nhau.

## Genome chuỗi (sequence / 시퀀스) và cell trạng thái (state / 상태) là hai lớp thông tin tương tác

Chuỗi (sequence / 시퀀스) cung cấp cis-regulatory element như promoter và enhancer, nhưng enhancer chỉ hoạt động khi chromatin trạng thái (state / 상태), transcription factor và topology ba chiều cho phép. Looping đưa enhancer ở xa tới promoter; architectural protein và compartment trong nucleus làm xác suất contact thay đổi. Vì vậy “gene nằm cạnh enhancer” chưa đủ để kết luận enhancer điều khiển gene đó.

Epigenetic bộ nhớ (memory / 메모리) nên được hiểu như **trạng thái điều hòa được duy trì qua thời gian** nhờ phản hồi (feedback / 피드백) giữa chromatin, transcription factor, DNA methylation và replication machinery. Nó bền hơn tín hiệu (signal / 신호) tức thời nhưng không độc lập với chuỗi (sequence / 시퀀스). Một số mark là nguyên nhân, một số là hệ quả, nhiều mark vừa phản ánh vừa ổn định trạng thái (state / 상태).

Omics chủ yếu đo correlation ở quy mô lớn. Một peak chromatin, methylation site hoặc expression signature liên hệ phenotype chưa tự chứng minh nhân quả (causal / 인과적). nhân quả (causal / 인과적) suy luận (inference / 추론) cần perturbation như CRISPRi/CRISPRa, reporter, allele-specific phân tích (analysis / 분석) hoặc experiment theo thời gian. Đây là nơi genomics gặp experimental thiết kế (design / 설계) và bioinformatics.

Population genomics cũng đang chuyển từ một tham chiếu (reference / 참조) genome sang **hệ gen toàn quần thể (pangenome)** vì structural variation và chuỗi (sequence / 시퀀스) không có trong tham chiếu (reference / 참조) cũ có thể quan trọng. “tham chiếu (reference / 참조)” là coordinate hệ thống (system / 시스템) hữu ích, không phải genome chuẩn tuyệt đối của loài.

<!-- continuity-2026:cell-identity-regulation -->

> **Nối mạch:** Genome sequence và cell state tương tác; mạng điều hòa giữ các trạng thái khác nhau. **Cầu nối sang Evolution** kiểm tra khi genome variation trở thành thay đổi quần thể.

## Cùng một genome nhưng cell khác nhau vì mạng điều hòa giữ trạng thái khác nhau

Neuron, hepatocyte và tế bào cơ gần như mang cùng DNA chuỗi (sequence / 시퀀스) nhưng dùng những phần khác nhau của genome. **Trạng thái tế bào (cell state)** xuất hiện từ tổ hợp yếu tố phiên mã, khả năng tiếp cận (accessibility / 접근성) của chromatin, enhancer–promoter contact, RNA regulation và phản hồi (feedback / 피드백) giữa các gene. Một transcription factor hiếm khi “bật một gene”; nó thường đổi xác suất hoạt động của nhiều locus trong một mạng.

Điều quan trọng là regulation có bộ nhớ (memory / 메모리) nhưng không bất biến. Positive phản hồi (feedback / 피드백) giữa transcription factor và enhancer có thể duy trì định danh (identity / 식별자) qua nhiều lần phân chia; methylation/histone trạng thái (state / 상태) góp phần ổn định khả năng tiếp cận (accessibility / 접근성). Tuy nhiên tín hiệu (signal / 신호) phát triển, stress hoặc reprogramming mạnh có thể chuyển cell sang attractor khác. Epigenetics vì vậy không phải lớp “cao hơn DNA”, mà là cơ chế trạng thái hoạt động trên genome và chịu giới hạn bởi chuỗi (sequence / 시퀀스), enzyme và môi trường tế bào.

Thất bại (failure / 실패) có thể xảy ra khi enhancer hoạt động sai cell kiểu (type / 타입), chromosome lĩnh vực (domain / 도메인) bị phá, dosage gene thay đổi hoặc epigenetic silencing không đúng. Nhiều disease-associated variant nằm ngoài coding region chính vì chúng thay regulation thay vì thay amino acid. Muốn chứng minh cơ chế cần perturb enhancer/gene trong đúng cell trạng thái (state / 상태), không chỉ dựa vào correlation trong dữ liệu omics.

> **Nối mạch:** Cầu nối sang Evolution khép mạch từ cell-state regulation tới genome variation và thay đổi quần thể.

## 30. cầu nối (bridge / 브리지): hệ gen variation trở thành evolution như thế nào?

Hệ gen học cho ta picture variation trên nhiều locus và regulatory trạng thái (state / 상태). Nhưng evolution hỏi một mức (level / 수준) khác: **tần số allele thay đổi qua generation bởi mutation, chọn lọc (selection), drift và dòng gen (gene flow) như thế nào?**

Đó là nội dung của [Tiến hóa và Di truyền quần thể](../03_evolution_and_diversity/00_evolution_and_population_genetics.md).

Phát sinh chủng loại (phylogeny) sau đó dùng chuỗi (sequence / 시퀀스) difference để reconstruct lịch sử (history / 이력); microbiology dùng chuyển gen ngang (horizontal gene transfer) và rapid evolution; bioinformatics quay lại dùng computational thuật toán (algorithm / 알고리즘) để xử lý genomic dữ liệu (data / 데이터).

> **Mô hình tư duy cuối chapter:** genome là một động (dynamic / 동적) thông tin (information / 정보) hệ thống được tổ chức trong chromatin, đọc qua mạng lưới điều hòa và biểu hiện thành nhiều molecular tầng (layer / 계층). Hệ gen học đo hệ thống ở quy mô lớn; thống kê (statistics) giúp tìm mẫu (pattern / 패턴), còn experiment mới giúp nối mẫu (pattern / 패턴) với causation.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Di truyền, Biến dị và Đột biến](01_inheritance_variation_and_mutation.md) · [Mục lục Biology](../README.md) · [Sửa chữa DNA, tái tổ hợp và ổn định genome →](03_dna_repair_recombination_and_genome_stability.md)

> **Bàn giao:** Sau **30. cầu nối (bridge / 브리지): hệ gen variation trở thành evolution như thế nào?**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
