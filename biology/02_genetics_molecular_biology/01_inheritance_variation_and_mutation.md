# Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Alen (allele), genotype và kiểu hình (phenotype)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Diploid organism và nhiễm sắc thể tương đồng (homologous chromosome)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Chapter trước giải thích DNA lưu thông tin (information / 정보) và biểu hiện gen (gene expression) biến chuỗi (sequence / 시퀀스) thành hàm (function / 함수). Nhưng heredity chỉ thật sự trở thành vấn đề khi organism tạo offspring: **allele nào được truyền, chromosome phân ly ra sao, recombination tạo combination mới thế nào, và vì sao offspring vừa giống vừa khác parent?**

Đây là nơi molecular genetics gặp meiosis, xác suất (probability / 확률) và population thinking.

> **mô hình tư duy (mental model / 사고 모델):** inheritance không phải “trait đi nguyên vẹn từ parent sang child”. Cái được truyền là vật chất di truyền (genetic material); phenotype xuất hiện sau khi allele tương tác với nhau, với mạng lưới điều hòa (regulatory network) và với môi trường (environment / 환경).

## 1. Alen (allele), genotype và kiểu hình (phenotype)

Một **alen (alen / 대립유전자)** là một phiên bản (version / 버전) của locus/gen (gene). **Kiểu gen (genotype) (kiểu gene / 유전자형)** mô tả allele composition; **kiểu hình (kiểu hình / 표현형)** là trait quan sát/đo được.

Genotype không đồng nghĩa phenotype. Cùng genotype có thể cho phenotype khác do môi trường (environment / 환경), development và stochastic factor. Ngược lại, phenotype tương tự có thể đến từ nhiều genotype khác nhau.

> **Chuyển mạch:** Allele/genotype/phenotype link genetic state to observable trait; diploid homologs carry paired copies, and meiosis separates them into haploid gametes.

## 2. Diploid organism và nhiễm sắc thể tương đồng (homologous chromosome)

Human somatic cell điển hình là diploid: có hai set chromosome, một từ mẹ và một từ cha.

Hai chromosome tương ứng gọi là **các nhiễm sắc thể tương đồng (homologous chromosomes)**. Chúng mang cùng loại locus theo cùng thứ tự (order / 순서) gần tương ứng nhưng có thể chứa allele khác nhau.

Nhiễm sắc tử chị em (sister chromatid) thì khác: đó là hai bản sao (copy / 복사) của cùng chromosome sau DNA replication.

Phân biệt homolog với nhiễm sắc tử chị em là điều bắt buộc để hiểu meiosis.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **3. Meiosis tạo gamete haploid** tiếp nhận điểm tựa từ **2. Diploid organism và nhiễm sắc thể tương đồng (homologous chromosome)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Phân ly độc lập (independent assortment): variation xuất hiện từ cách chromosome xếp ngẫu nhiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Meiosis tạo gamete haploid

Meiosis giảm số lượng nhiễm sắc thể (chromosome number) từ diploid xuống haploid để khi fertilization kết hợp hai gamete, diploid number được phục hồi.

Meiosis I tách nhiễm sắc thể tương đồng; meiosis II tách nhiễm sắc tử chị em.

Nếu không có reduction division, số lượng nhiễm sắc thể sẽ double mỗi generation.

Meiosis vì vậy là lời giải structural cho sinh sản hữu tính (sexual reproduction).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **4. Phân ly độc lập (independent assortment): variation xuất hiện từ cách chromosome xếp ngẫu nhiên** tiếp nhận điểm tựa từ **3. Meiosis tạo gamete haploid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Trao đổi chéo: homolog không chỉ chia ngẫu nhiên, chúng còn trao đổi đoạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Phân ly độc lập (independent assortment): variation xuất hiện từ cách chromosome xếp ngẫu nhiên

Mỗi homologous pair có orientation tương đối độc lập ở metaphase I. Vì vậy maternal/paternal chromosome combination trong gamete thay đổi.

Nếu có \(n\) chromosome pair và bỏ qua tái tổ hợp (recombination), số combination từ phân ly độc lập là khoảng:

\[
2^n
\]

Ở humans với 23 pair, con số đã hơn tám triệu combination trước khi tính trao đổi chéo (crossing-over).

Sinh sản hữu tính tạo variation khổng lồ từ mechanics của meiosis.

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **5. Trao đổi chéo: homolog không chỉ chia ngẫu nhiên, chúng còn trao đổi đoạn** tiếp nhận điểm tựa từ **4. Phân ly độc lập (independent assortment): variation xuất hiện từ cách chromosome xếp ngẫu nhiên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Mendel: từ mẫu hình (pattern) phenotype suy ra đơn vị (unit / 단위) inheritance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Trao đổi chéo: homolog không chỉ chia ngẫu nhiên, chúng còn trao đổi đoạn

Trong prophase I, nhiễm sắc thể tương đồng pair và non-nhiễm sắc tử chị em có thể recombine.

**Trao đổi chéo (교차)** tạo chromosome mosaic chứa segment từ maternal/paternal homolog.

Recombination vừa tăng variation vừa có vai trò giúp homolog segregation đúng qua chiasma.

Distance giữa loci ảnh hưởng xác suất (probability / 확률) tái tổ hợp, tạo cơ sở genetic ánh xạ (mapping / 매핑).

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **6. Mendel: từ mẫu hình (pattern) phenotype suy ra đơn vị (unit / 단위) inheritance** tiếp nhận điểm tựa từ **5. Trao đổi chéo: homolog không chỉ chia ngẫu nhiên, chúng còn trao đổi đoạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Dominant và recessive không có nghĩa “mạnh” và “yếu”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Mendel: từ mẫu hình (pattern) phenotype suy ra đơn vị (unit / 단위) inheritance

Mendel nghiên cứu pea trước khi biết DNA/nhiễm sắc thể (chromosome). Từ ratio offspring, ông suy ra trait được truyền qua discrete factor.

Ngày nay ta nối mô hình (model / 모델) Mendel với chromosome hành vi (behavior / 동작).

**Law of segregation** phản ánh hai alen ở diploid individual được phân ly vào gamete qua meiosis.

**Phân ly độc lập** đúng xấp xỉ cho gene trên chromosome khác nhau hoặc đủ xa nhau; linked gene là limitation quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **7. Dominant và recessive không có nghĩa “mạnh” và “yếu”** tiếp nhận điểm tựa từ **6. Mendel: từ mẫu hình (pattern) phenotype suy ra đơn vị (unit / 단위) inheritance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Molecular basis của dominance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Dominant và recessive không có nghĩa “mạnh” và “yếu”

Nếu heterozygote phenotype giống một homozygote, allele thể hiện được gọi **dominant** trong ngữ cảnh (context / 맥락) trait đó; allele kia **recessive**.

Dominance là mối quan hệ (relationship) kiểu hình giữa allele, không phải thuộc tính (property / 속성) đạo đức hay evolutionary superiority.

Một recessive allele vẫn có thể phổ biến. Một dominant disease allele vẫn có thể rare.

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **8. Molecular basis của dominance** tiếp nhận điểm tựa từ **7. Dominant và recessive không có nghĩa “mạnh” và “yếu”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Punnett square là xác suất (probability / 확률) công cụ (tool / 도구), không phải machine dự đoán family cụ thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Molecular basis của dominance

Nhiều recessive loss-of-chức năng (function) allele xảy ra vì một functional bản sao (copy / 복사) tạo đủ protein (protein) cho phenotype bình thường; đây là **haplosufficiency**.

Trong trường hợp khác, một bản sao (copy / 복사) không đủ (**haploinsufficiency**) hoặc mutant protein interfere với normal protein (**dominant negative**), làm inheritance dominant.

Mendelian label có molecular cơ chế (mechanism / 메커니즘) phía sau.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **9. Punnett square là xác suất (probability / 확률) công cụ (tool / 도구), không phải machine dự đoán family cụ thể** tiếp nhận điểm tựa từ **8. Molecular basis của dominance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. sản phẩm (product / 제품) quy tắc (rule / 규칙) và sum quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Punnett square là xác suất (probability / 확률) công cụ (tool / 도구), không phải machine dự đoán family cụ thể

Cross Aa × Aa cho kiểu gen xác suất (probability / 확률):

\[
P(AA)=1/4,\quad P(Aa)=1/2,\quad P(aa)=1/4
\]

Nếu complete dominance, phenotype ratio expected 3:1.

Nhưng mỗi child là sự kiện (event / 이벤트) mới; bốn child không bắt buộc có đúng ba dominant và một recessive phenotype.

Expected ratio xuất hiện khi mẫu (sample / 표본) đủ lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **10. sản phẩm (product / 제품) quy tắc (rule / 규칙) và sum quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **9. Punnett square là xác suất (probability / 확률) công cụ (tool / 도구), không phải machine dự đoán family cụ thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. kiểm thử (test / 테스트) cross và suy luận (inference / 추론) kiểu gen** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. sản phẩm (product / 제품) quy tắc (rule / 규칙) và sum quy tắc (rule / 규칙)

Nếu hai independent sự kiện (event / 이벤트) cùng xảy ra:

\[
P(A\cap B)=P(A)P(B)
\]

Nếu hỏi một trong các mutually exclusive kết quả (outcome / 결과):

\[
P(A\cup B)=P(A)+P(B)
\]

Xác suất (probability / 확률) giúp giải genetic cross phức tạp mà không cần vẽ Punnett square khổng lồ.

Math ở đây mô tả bất định (uncertainty / 불확실성) của gamete combination.

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **11. kiểm thử (test / 테스트) cross và suy luận (inference / 추론) kiểu gen** tiếp nhận điểm tựa từ **10. sản phẩm (product / 제품) quy tắc (rule / 규칙) và sum quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Trội không hoàn toàn (incomplete dominance) và đồng trội (codominance)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. kiểm thử (test / 테스트) cross và suy luận (inference / 추론) kiểu gen

Nếu individual có dominant phenotype nhưng genotype có thể AA hoặc Aa, crossing với homozygous recessive có thể cung cấp bằng chứng (evidence / 증거).

Nếu offspring recessive xuất hiện, parent dominant phải mang recessive allele.

Đây là ví dụ scientific suy luận (inference / 추론): phenotype offspring cung cấp dữ liệu (data / 데이터) để suy genotype không quan sát trực tiếp.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **12. Trội không hoàn toàn (incomplete dominance) và đồng trội (codominance)** tiếp nhận điểm tựa từ **11. kiểm thử (test / 테스트) cross và suy luận (inference / 추론) kiểu gen** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Pleiotropy và polygenic trait** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Trội không hoàn toàn (incomplete dominance) và đồng trội (codominance)

Không phải mọi locus theo complete dominance.

Trong **trội không hoàn toàn**, heterozygote có phenotype intermediate. Trong **đồng trội**, hai allele sản phẩm (product / 제품) đều thể hiện rõ.

ABO blood group là ví dụ đồng trội giữa IA và IB, đồng thời cả hai dominant so với i theo kiểu hình kháng nguyên (antigen).

Một locus có thể có **multiple alleles** trong population dù mỗi diploid individual chỉ mang tối đa hai alen ở locus đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **13. Pleiotropy và polygenic trait** tiếp nhận điểm tựa từ **12. Trội không hoàn toàn (incomplete dominance) và đồng trội (codominance)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Epistasis: gene tương tác gene** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Pleiotropy và polygenic trait

**Pleiotropy**: một gene ảnh hưởng nhiều trait vì protein tham gia tiến trình (process / 프로세스) chung hoặc nhiều tissue.

**Polygenic trait**: nhiều gene đóng góp một trait. Height, skin pigmentation và nhiều tính trạng định lượng (quantitative trait) thuộc kiểu này.

Điều này phá mô hình (model / 모델) “một gene — một trait” vốn chỉ hữu ích trong một số trường hợp (case / 사례) đơn giản.

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **14. Epistasis: gene tương tác gene** tiếp nhận điểm tựa từ **13. Pleiotropy và polygenic trait** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Linkage: gene gần nhau không assort hoàn toàn độc lập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Epistasis: gene tương tác gene

Trong **epistasis (상위성)**, tác động (effect / 효과) của allele ở một locus phụ thuộc genotype ở locus khác.

Ví dụ pathway pigment có enzyme A tạo precursor và enzyme B chuyển precursor thành pigment. Nếu A mất hàm (function / 함수), B có phiên bản (version / 버전) nào cũng không tạo pigment.

Phenotype là đầu ra (output / 출력) của pathway, không phải tổng độc lập của từng gene.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **15. Linkage: gene gần nhau không assort hoàn toàn độc lập** tiếp nhận điểm tựa từ **14. Epistasis: gene tương tác gene** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Sex-linked inheritance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Linkage: gene gần nhau không assort hoàn toàn độc lập

Gene trên cùng chromosome có tendency đi cùng nhau. Recombination có thể tách chúng.

Tái tổ hợp frequency tăng theo genetic distance ở khoảng phù hợp. 1% tái tổ hợp được dùng định nghĩa khoảng 1 centimorgan trong ánh xạ (mapping / 매핑) cổ điển.

Nhưng frequency không tăng tuyến tính vô hạn; multiple crossover làm ánh xạ (mapping / 매핑) dài cần mô hình (model / 모델) correction.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **16. Sex-linked inheritance** tiếp nhận điểm tựa từ **15. Linkage: gene gần nhau không assort hoàn toàn độc lập** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Mutation tạo allele mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Sex-linked inheritance

Gene trên sex chromosome tạo mẫu hình inheritance khác autosomal gene.

Ở X-linked recessive trait, male XY chỉ có một X nên allele recessive trên X có thể biểu hiện ngay nếu không có bản sao (copy / 복사) tương ứng trên Y.

Nhưng sex determination và sex-linked biology đa dạng giữa species; không nên lấy human XY làm universal mô hình (model / 모델).

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **17. Mutation tạo allele mới** tiếp nhận điểm tựa từ **16. Sex-linked inheritance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Germline và đột biến soma (somatic mutation)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Mutation tạo allele mới

Recombination chỉ shuffle variation sẵn có; **đột biến (mutation)** tạo trình tự (sequence) variation mới.

Điểm (point / 지점) mutation có thể là chuyển tiếp (transition / 전이)/transversion; insertion/deletion có thể gây frameshift nếu nằm coding region và length không chia hết cho 3.

Large-scale variant gồm duplication, deletion, inversion, translocation và copy-number variation.

Tác động (effect / 효과) phụ thuộc locus, regulatory ngữ cảnh (context / 맥락) và môi trường.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **18. Germline và đột biến soma (somatic mutation)** tiếp nhận điểm tựa từ **17. Mutation tạo allele mới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Tốc độ đột biến (mutation rate) và selection không phải cùng thứ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Germline và đột biến soma (somatic mutation)

**Đột biến dòng mầm (germline mutation)** có thể truyền cho offspring nếu nằm lineage tạo gamete.

**Đột biến soma** xảy ra trong body cell và thường không truyền qua reproduction, nhưng có thể ảnh hưởng clone cell — rất quan trọng trong cancer.

Một human body vì vậy không hoàn toàn genetic-uniform; mosaicism có thể xuất hiện.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **19. Tốc độ đột biến (mutation rate) và selection không phải cùng thứ** tiếp nhận điểm tựa từ **18. Germline và đột biến soma (somatic mutation)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Chromosome không phân ly (nondisjunction)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Tốc độ đột biến (mutation rate) và selection không phải cùng thứ

Mutation xuất hiện không vì sinh vật (organism) “cần” thích nghi (adaptation). Mutation nguồn (source / 소스) có độ lệch (bias / 편향) nhưng không được tạo ra có định hướng phù hợp future fitness theo cách Lamarck đơn giản.

Selection acts **sau khi variation tồn tại** bằng differential reproduction/survival.

Phân biệt nguồn (source / 소스) variation với filter variation là nền của evolution.

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **20. Chromosome không phân ly (nondisjunction)** tiếp nhận điểm tựa từ **19. Tốc độ đột biến (mutation rate) và selection không phải cùng thứ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Quantitative genetics: trait liên tục được phân tích thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Chromosome không phân ly (nondisjunction)

Nếu homolog hoặc nhiễm sắc tử chị em không phân ly đúng, gamete có số lượng nhiễm sắc thể bất thường.

Sau fertilization có thể tạo **aneuploidy**.

Tác động (effect / 효과) thường lớn vì dosage của hàng trăm gene thay đổi cùng lúc.

Age-related thay đổi (change / 변경) trong meiosis có thể ảnh hưởng rủi ro (risk / 위험) ở một số aneuploidy, nhưng cơ chế (mechanism / 메커니즘) phức tạp hơn một nguyên nhân đơn.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **21. Quantitative genetics: trait liên tục được phân tích thế nào?** tiếp nhận điểm tựa từ **20. Chromosome không phân ly (nondisjunction)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Heritability: một khái niệm rất dễ hiểu sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Quantitative genetics: trait liên tục được phân tích thế nào?

Nhiều trait tạo phân phối (distribution / 분포) liên tục vì nhiều locus + môi trường.

Ta có thể phân rã phenotypic variance khái niệm:

\[
V_P=V_G+V_E+V_{G\times E}+...
\]

Trong đó genetic variance, environmental variance và gen–môi trường (environment / 환경) tương tác (interaction / 상호작용) cùng đóng góp.

Đây là mô hình thống kê (statistical model) ở population mức (level / 수준), không phải decomposition cố định của một individual.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **22. Heritability: một khái niệm rất dễ hiểu sai** tiếp nhận điểm tựa từ **21. Quantitative genetics: trait liên tục được phân tích thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Gen–môi trường (environment / 환경) tương tác (interaction / 상호작용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Heritability: một khái niệm rất dễ hiểu sai

**Heritability (유전력)** là phần variance phenotype trong một population/môi trường được liên hệ với genetic variance theo mô hình (model / 모델) cụ thể.

Heritability cao không có nghĩa trait “không đổi được bởi môi trường (environment / 환경)”. Height có heritability cao trong một population nhưng nutrition vẫn ảnh hưởng growth.

Heritability cũng không nói “X% trait của một người do gen”. Nó là thuộc tính (property / 속성) của population variance, không phải individual nhân quả (causal / 인과적) percentage.

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **23. Gen–môi trường (environment / 환경) tương tác (interaction / 상호작용)** tiếp nhận điểm tựa từ **22. Heritability: một khái niệm rất dễ hiểu sai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Độ thấm (penetrance) và mức biểu hiện (expressivity)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Gen–môi trường (environment / 환경) tương tác (interaction / 상호작용)

Cùng genotype có thể phản ứng khác nhau trong môi trường (environment / 환경) khác. **Reaction norm** mô tả phenotype của genotype qua phạm vi (range / 범위) môi trường.

Ví dụ chất dinh dưỡng (nutrient), temperature hoặc stress có thể thay tác động (effect / 효과) allele.

Nature và nurture không phải hai hộp cộng độc lập; chúng tương tác.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **24. Độ thấm (penetrance) và mức biểu hiện (expressivity)** tiếp nhận điểm tựa từ **23. Gen–môi trường (environment / 환경) tương tác (interaction / 상호작용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Pedigree: suy inheritance từ family mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Độ thấm (penetrance) và mức biểu hiện (expressivity)

**Độ thấm** mô tả fraction individual mang genotype và biểu hiện phenotype xác định.

**Mức biểu hiện** mô tả mức độ phenotype khác nhau giữa người có cùng genotype.

Incomplete độ thấm có thể đến từ modifier gene, môi trường, age hoặc stochastic factor.

Điều này làm pedigree thực tế phức tạp hơn Punnett square đơn giản.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **25. Pedigree: suy inheritance từ family mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **24. Độ thấm (penetrance) và mức biểu hiện (expressivity)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Di truyền ty thể (mitochondrial inheritance)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Pedigree: suy inheritance từ family mẫu (pattern / 패턴)

Pedigree dùng symbol để biểu diễn relationship và kiểu hình qua generation.

Ta suy autosomal dominant/recessive, X-linked hoặc mitochondrial mẫu (pattern / 패턴) dựa trên transmission, nhưng cần cẩn trọng vì small family, incomplete độ thấm và new mutation có thể làm mẫu (pattern / 패턴) mơ hồ.

Pedigree là suy luận (inference / 추론) under bất định (uncertainty / 불확실성), không phải nhìn một hình rồi “đoán chắc”.

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **26. Di truyền ty thể (mitochondrial inheritance)** tiếp nhận điểm tựa từ **25. Pedigree: suy inheritance từ family mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Biến dị di truyền (genetic variation) ở quy mô quần thể (population scale)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Di truyền ty thể (mitochondrial inheritance)

Mitochondrial DNA ở human thường được truyền chủ yếu từ mẹ vì mitochondria của egg đóng góp phần lớn organelle cho embryo.

Tuy nhiên phenotype mitochondrial disease còn phụ thuộc heteroplasmy và ngưỡng (threshold) ở mô (tissue).

Non-Mendelian inheritance nhắc ta rằng Mendel là nền, không phải toàn bộ di truyền học (genetics).

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **27. Biến dị di truyền (genetic variation) ở quy mô quần thể (population scale)** tiếp nhận điểm tựa từ **26. Di truyền ty thể (mitochondrial inheritance)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Tình huống phân tích (case study): lactose persistence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Biến dị di truyền (genetic variation) ở quy mô quần thể (population scale)

Ở một individual ta nói genotype. Ở quần thể (population) ta quan tâm **tần số alen (allele frequency)** và **tần số kiểu gen (genotype frequency)**.

Đây là bước chuyển cực kỳ quan trọng. Evolution không phải “một individual đổi gene để thích nghi”; nó là thay đổi (change / 변경) phân phối (distribution / 분포) variation trong quần thể qua generation.

Mọi mutation, meiosis, recombination học trong chapter này trở thành đầu vào (input / 입력) cho di truyền học quần thể (population genetics).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **27. Biến dị di truyền (genetic variation) ở quy mô quần thể (population scale)** cho ta quy tắc; **28. Tình huống phân tích (case study): lactose persistence** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **29. Tình huống phân tích: kháng kháng sinh (antibiotic resistance) không phải bacteria “cố biến đổi”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Tình huống phân tích (case study): lactose persistence

Khả năng tiêu hóa lactose ở adulthood liên quan regulation của lactase gene và population lịch sử (history / 이력).

Ở một số population có tradition chăn nuôi/sữa, regulatory variant liên quan lactase persistence tăng frequency qua chọn lọc (selection).

Trait cho thấy liên kết (connection / 연결):

```text
regulatory DNA variant
→ gene expression after childhood
→ digestive phenotype
→ cultural/environment context
→ differential fitness historically
→ allele-frequency change
```

Gen–culture đồng tiến hóa (coevolution) nối molecular genetics, inheritance và tiến hóa (evolution).

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **28. Tình huống phân tích (case study): lactose persistence** cho ta quy tắc; **29. Tình huống phân tích: kháng kháng sinh (antibiotic resistance) không phải bacteria “cố biến đổi”** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **30. Các hiểu lầm phổ biến (common misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Tình huống phân tích: kháng kháng sinh (antibiotic resistance) không phải bacteria “cố biến đổi”

Trong bacterial population có biến dị (variation) do đột biến/chuyển gen ngang (horizontal gene transfer). Antibiotic giết susceptible cell mạnh hơn. Resistant variant survive/reproduce, làm resistance allele tăng frequency.

Selection thay composition population; antibiotic không “dạy” từng bacterium cách resistance theo nghĩa có mục tiêu.

Đây là cầu nối (bridge / 브리지) sang evolution và microbiology.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **29. Tình huống phân tích: kháng kháng sinh (antibiotic resistance) không phải bacteria “cố biến đổi”** cho ta quy tắc; **30. Các hiểu lầm phổ biến (common misconceptions)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Từ genotype đến phenotype: bản đồ không tuyến tính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Các hiểu lầm phổ biến (common misconceptions)

“Dominant allele phổ biến hơn recessive allele” sai.

“Recessive nghĩa yếu” sai.

“50% rủi ro (risk / 위험) nghĩa hai child chắc chắn một affected” sai.

“Heritability cao nghĩa môi trường (environment / 환경) không quan trọng” sai.

“Mutation xảy ra để thích nghi” sai.

“Gene và trait có ánh xạ (mapping / 매핑) một-một” hiếm khi đúng cho trait phức tạp.

<!-- depth-audit-2026:genotype-phenotype-map -->

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **Từ genotype đến phenotype: bản đồ không tuyến tính** tiếp nhận điểm tựa từ **30. Các hiểu lầm phổ biến (common misconceptions)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ cơ chế meiosis tới xác suất di truyền và bản đồ liên kết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ genotype đến phenotype: bản đồ không tuyến tính

Một allele không “chứa sẵn” phenotype. chuỗi (sequence / 시퀀스) thay đổi trước hết tác động một RNA, protein, mức biểu hiện hoặc regulatory tương tác (interaction / 상호작용); thay đổi đó đi qua mạng phát triển và physiology rồi mới thành trait đo được. Do đó cùng một mutation có thể có tác động (effect / 효과) khác nhau theo tissue, age, môi trường (environment / 환경) hoặc genetic background.

**Độ thâm nhập (penetrance)** hỏi bao nhiêu người mang genotype biểu hiện phenotype; **độ biểu hiện (expressivity)** hỏi mức độ phenotype mạnh đến đâu. Epistasis xuất hiện khi tác động (effect / 효과) của allele ở locus A phụ thuộc allele tại locus B. Đây là lý do Punnett square đúng về segregation nhưng không đủ để mô tả nhiều trait thực.

Mutation cũng có phân bố tác động (effect / 효과) rất lệch. Nhiều mutation gần neutral, một số có hại rõ, số có lợi trong một môi trường (environment / 환경) cụ thể thường nhỏ hơn. Structural variant, copy-number thay đổi (change / 변경) và regulatory variant có thể ảnh hưởng phenotype mạnh dù không đổi coding chuỗi (sequence / 시퀀스) theo cách “một cơ sở (base / 기반) → một amino acid”.

Với quantitative trait, phương sai phenotype là kết quả của nhiều locus, môi trường (environment / 환경) và tương tác. Heritability cao trong một population không có nghĩa trait “không đổi được”; nó chỉ mô tả nguồn variation dưới môi trường (environment / 환경) và population đang xét. Đây là cầu nối (bridge / 브리지) quan trọng từ inheritance sang population genetics và tránh biến statistics thành định mệnh sinh học.

<!-- continuity-2026:meiosis-linkage -->

> **Chuyển mạch:** Trong **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **Từ genotype đến phenotype: bản đồ không tuyến tính** xác định đầu vào; **Từ cơ chế meiosis tới xác suất di truyền và bản đồ liên kết** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. cầu nối (bridge / 브리지): từ family inheritance sang genome và quần thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ cơ chế meiosis tới xác suất di truyền và bản đồ liên kết

Quy luật phân ly của Mendel xuất hiện từ hành vi vật lý của chromosome: hai homolog mang các allele tương ứng bắt cặp rồi phân ly ở meiosis I; sister chromatid phân ly ở meiosis II. Khi hai locus nằm trên chromosome khác nhau, orientation của các cặp homolog tạo cơ sở cho phân ly độc lập. Khi hai locus nằm gần nhau trên cùng chromosome, chúng không còn độc lập vì được truyền cùng một đoạn DNA.

Trao đổi chéo (crossing-over) tạo recombinant chromosome. Tần số recombinant tăng khi hai locus xa nhau hơn, nhưng không thể dùng tuyến tính vô hạn vì nhiều crossover có thể che lẫn nhau; ở khoảng cách lớn, recombination fraction tiến gần 0,5 và hai locus trông gần như không liên kết. Đây là lý do bản đồ di truyền là mô hình (model / 모델) xác suất của meiosis, không phải thước đo vật lý hoàn hảo.

Thất bại (failure / 실패) ở meiosis cũng cho thấy cấu trúc tạo chức năng như thế nào. Nondisjunction làm chromosome không phân ly đúng, tạo giao tử thừa hoặc thiếu chromosome. Cơ thể có checkpoint và cơ chế cohesion để giảm lỗi, nhưng selection không thể làm lỗi về zero tuyệt đối vì replication, recombination và segregation đều có chi phí và giới hạn vật lý.

> **Chuyển mạch:** Ở chặng này của **Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)**, **Từ cơ chế meiosis tới xác suất di truyền và bản đồ liên kết** xác định đầu vào; **31. cầu nối (bridge / 브리지): từ family inheritance sang genome và quần thể** giải thích bước vận hành tạo ra kết quả kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 31. cầu nối (bridge / 브리지): từ family inheritance sang genome và quần thể

Chapter này đi từ meiosis đến allele transmission và biến dị. Nhưng hiện đại (modern / 현대적) genetics còn hỏi ở quy mô (scale / 규모) lớn hơn: hàng triệu variant trong hệ gen (genome) được tổ chức thế nào? Chromatin làm gene accessible ra sao? GWAS tìm association bằng cách nào? Transcriptomics đo expression của hàng nghìn gene ra sao?

[Genomics, Epigenetics và Điều hòa hệ gene](02_genomics_epigenetics_and_regulation.md) sẽ mở rộng sang genome-wide regulation và omics.

Sau đó [Tiến hóa và Di truyền quần thể](../03_evolution_and_diversity/00_evolution_and_population_genetics.md) sẽ lấy chính tần số alen, đột biến, recombination và mức thích nghi sinh sản (fitness) để xây lý thuyết (theory / 이론) evolution.

> **Mô hình tư duy cuối chapter:** heredity là quá trình chromosome/DNA được phân phối qua meiosis và fertilization; variation phát sinh từ đột biến + tái tổ hợp + assortment; phenotype là kết quả (outcome / 결과) của genotype trong bối cảnh (context). Khi ta chuyển từ một family sang cả quần thể, chính variation này trở thành dữ liệu cho tiến hóa.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← DNA, Gene và Biểu hiện gene](00_dna_genes_and_gene_expression.md) · [Mục lục Biology](../README.md) · [Genomics, Epigenetics và Điều hòa hệ gene →](02_genomics_epigenetics_and_regulation.md)

> **Bàn giao:** Sau **31. cầu nối (bridge / 브리지): từ family inheritance sang genome và quần thể**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
