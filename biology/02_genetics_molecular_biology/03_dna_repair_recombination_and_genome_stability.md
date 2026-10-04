# Sửa chữa DNA, tái tổ hợp và ổn định genome — DNA Repair, Recombination and Genome Stability (DNA 복구, 재조합과 유전체 안정성)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Sửa chữa DNA, tái tổ hợp và ổn định genome — DNA Repair, Recombination and Genome Stability (DNA 복구, 재조합과 유전체 안정성)**. Route đi từ tổn thương và lỗi sao chép → proofreading/sửa chữa → tái tổ hợp và checkpoint → ổn định genome, ung thư và tiến hóa, để đánh giá một cơ chế bằng cả độ chính xác lẫn chi phí sinh học.

Sau khi học DNA replication, biểu hiện gen (gene expression), inheritance và đột biến (mutation), một câu hỏi quan trọng xuất hiện: **nếu DNA luôn bị chemical damage và replication không hoàn hảo, vì sao genome vẫn đủ ổn định để cell sống nhiều năm và lineage tồn tại qua hàng triệu generation?** Câu trả lời là genome không phải một “tệp (file / 파일) read-only”. Nó được proofread, kiểm tra, sửa chữa, tái tổ hợp, đóng gói và đôi khi hy sinh cả tế bào (cell) để bảo vệ sinh vật (organism).

Chapter này nối những chủ đề thường bị học tách rời: độ chính xác sao chép (replication fidelity), Tổn thương DNA (DNA damage), đột biến, tái tổ hợp (recombination), nhiễm sắc thể (chromosome) kiến trúc (architecture / 아키텍처), điểm kiểm soát chu kỳ tế bào (cell-cycle checkpoint), lão hóa (aging), cancer và tiến hóa (evolution). Nhìn chung, chúng đều xoay quanh một sự đánh đổi (trade-off / 트레이드오프): **thông tin (information / 정보) phải đủ ổn định để phenotype hoạt động, nhưng variation vẫn phải tồn tại để evolution xảy ra.**

> **mô hình tư duy (mental model / 사고 모델):** độ ổn định hệ gen (genome stability) không có nghĩa genome không thay đổi. Nó có nghĩa cell quản lý thay đổi (change / 변경): sửa phần lớn damage, cho phép một số variation tồn tại, và kích hoạt checkpoint hoặc chết tế bào (cell death) khi rủi ro (risk / 위험) vượt ngưỡng.

## 1. Tổn thương DNA là trạng thái bình thường của một molecule sống trong chemistry hoạt động

DNA bị hỏng không chỉ do radiation hay toxin. Water có thể thúc đẩy hydrolysis; cơ sở (base / 기반) có thể deaminate; reactive oxygen species từ metabolism có thể oxidize nucleotide; chạc sao chép (replication fork) có thể stall; chromosome có thể bị mechanical stress khi segregation.

Vì vậy mỗi cell sống trong **damage–repair balance** liên tục. Đây là điểm quan trọng: repair hệ thống (system / 시스템) không chỉ là emergency phản hồi (response / 응답). Nó là hạ tầng (infrastructure / 인프라) thường trực giống hệ thống bảo trì của một mạng máy tính luôn hoạt động.

Cần phân biệt **Tổn thương DNA (tổn thương DNA / DNA 손상)** với **đột biến (đột biến / 돌연변이)**. Damage là trạng thái hóa học hoặc structural abnormality. Nếu được sửa đúng, trình tự (sequence) ban đầu được khôi phục. Mutation là chuỗi (sequence / 시퀀스) thay đổi (change / 변경) đã trở thành ổn định qua sao chép (replication). Damage có thể dẫn tới mutation, nhưng hai khái niệm không đồng nghĩa.

> **Nối mạch:** DNA damage là trạng thái thường trực; polymerase fidelity giảm lỗi lúc sao chép, còn error rate nhân với genome size dự đoán gánh nặng đột biến trước khi xét repair và recombination.

## 2. Độ chính xác sao chép bắt đầu ngay tại DNA polymerase

DNA polymerase chọn nucleotide dựa trên complementarity và hình học (geometry / 기하학) của trung tâm hoạt động (active site). Nhưng cơ sở (base / 기반) pairing không hoàn hảo tuyệt đối; misincorporation vẫn xảy ra.

Nhiều polymerase có **đọc sửa (proofreading) (교정 기능)** qua 3'→5' exonuclease activity. Khi nucleotide sai làm hình học (geometry / 기하학) bất thường, polymerase có thể lùi lại, cắt nucleotide đó rồi tiếp tục synthesis.

Mô hình tư duy hữu ích là replication có nhiều lớp defense:

```text
base selection
→ polymerase proofreading
→ post-replication mismatch repair
→ checkpoint nếu damage vẫn còn
```

Mỗi tầng (layer / 계층) giảm lỗi (error / 오류) thêm một bậc. Đây là redundancy có chủ đích: thông tin (information / 정보) quan trọng đến mức evolution đầu tư nhiều cơ chế (mechanism / 메커니즘) độc lập để bảo vệ nó.

> **Nối mạch:** DNA polymerase đặt nền độ chính xác; error rate và genome size liên kết thành giới hạn định lượng. **Mismatch repair** tiếp theo sửa phần lỗi còn sót sau replication.

## 3. Tỉ lệ lỗi (error rate) và genome kích thước (size / 크기) liên kết toán học

Nếu xác suất (probability / 확률) lỗi mỗi cơ sở (base / 기반) là \(\mu\) và genome segment có chiều dài \(L\), xác suất một bản sao (copy / 복사) không có lỗi trong approximation đơn giản là:

\[
Q=(1-\mu)^L
\]

Khi \(L\) tăng, cùng tỉ lệ lỗi sẽ tạo nhiều lỗi tuyệt đối hơn. Điều đó giải thích vì sao organism có genome lớn cần độ chính xác sao chép và repair mạnh hơn. Nó cũng nối trực tiếp với [Nguồn gốc sự sống và tiến hóa sớm](../00_foundations/03_origin_of_life_and_early_evolution.md): muốn thông tin (information / 정보) sức chứa (capacity / 용량) tăng, sao chép accuracy phải tăng tương ứng.

Tuy nhiên “lỗi (error / 오류) càng thấp càng tốt” không phải kết luận cuối cùng. Fidelity có energetic và kinetic chi phí (cost / 비용); hơn nữa evolution cần variation. Hệ thống sinh học (biological system) tối ưu sự đánh đổi (trade-off / 트레이드오프), không tối đa một chỉ số (metric / 지표) duy nhất.

> **Nối mạch:** **4. Sửa chữa bắt cặp sai (mismatch repair): sửa lỗi còn sót sau sao chép** nối từ **3. Tỉ lệ lỗi (error rate) và genome kích thước (size / 크기) liên kết toán học** sang **5. Sửa chữa cắt bỏ cơ sở (base / 기반) (base excision repair): sửa lesion nhỏ ở từng cơ sở (base / 기반)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Sửa chữa bắt cặp sai (mismatch repair): sửa lỗi còn sót sau sao chép

**Sửa chữa bắt cặp sai, MMR (불일치 복구)** nhận biết cơ sở (base / 기반) pair sai hoặc small insertion/deletion vòng lặp (loop / 루프) còn sót sau sao chép. hệ thống (system / 시스템) cắt đoạn chứa mismatch rồi resynthesize dựa trên strand đúng.

Ý tưởng sâu ở đây là repair cần biết **template nào đáng tin hơn**. Trong nhiều ngữ cảnh (context / 맥락), newly synthesized strand được nhận diện nhờ tín hiệu (signal / 신호) liên quan replication trạng thái (state / 상태). Sau khi mismatch được excise, DNA polymerase và ligase hoàn thiện patch.

Defect MMR làm tốc độ đột biến (mutation rate) tăng mạnh. Điều này giúp hiểu **mutator phenotype**: cancer có thể không cần mutation đầu tiên trực tiếp kích hoạt proliferation; chỉ cần phá gen (gene) giữ hệ gen (genome) ổn định, toàn clone sau đó tạo mutation nhanh hơn và tăng cơ hội xuất hiện driver mutation.

> **Nối mạch:** **5. Sửa chữa cắt bỏ cơ sở (base / 기반) (base excision repair): sửa lesion nhỏ ở từng cơ sở (base / 기반)** nối từ **4. Sửa chữa bắt cặp sai (mismatch repair): sửa lỗi còn sót sau sao chép** sang **6. Sửa chữa cắt bỏ nucleotit (nucleotide excision repair): cắt cả đoạn khi helix bị biến dạng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Sửa chữa cắt bỏ cơ sở (base / 기반) (base excision repair): sửa lesion nhỏ ở từng cơ sở (base / 기반)

**Sửa chữa cắt bỏ cơ sở (base / 기반), BER (염기 절제 복구)** xử lý lesion nhỏ như deamination hay oxidation mà không làm helix méo mạnh.

DNA glycosylase nhận biết cơ sở (base / 기반) bất thường và bỏ cơ sở (base / 기반), để lại AP site. Enzyme khác cắt backbone, polymerase điền nucleotide mới và ligase nối lại.

BER cho thấy double-stranded DNA có một lợi thế sâu: **redundancy**. Khi một strand bị damage cục bộ, strand đối diện thường giữ thông tin (information / 정보) để phục hồi. DNA vì vậy vừa là lưu trữ (storage / 저장소) medium vừa có built-in error-correction lô-gic (logic / 논리) ở structural mức (level / 수준).

> **Nối mạch:** **6. Sửa chữa cắt bỏ nucleotit (nucleotide excision repair): cắt cả đoạn khi helix bị biến dạng** nối từ **5. Sửa chữa cắt bỏ cơ sở (base / 기반) (base excision repair): sửa lesion nhỏ ở từng cơ sở (base / 기반)** sang **7. Direct reversal và tại sao đôi khi “sửa” không cần cắt DNA**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Sửa chữa cắt bỏ nucleotit (nucleotide excision repair): cắt cả đoạn khi helix bị biến dạng

**Sửa chữa cắt bỏ nucleotit, NER (뉴클레오타이드 절제 복구)** xử lý lesion cồng kềnh làm biến dạng helix, như một số UV-induced photoproduct.

Thay vì chỉ bỏ một cơ sở (base / 기반), hệ thống (system / 시스템) nhận structural distortion, cắt một đoạn oligonucleotide chứa lesion, rồi polymerase resynthesize và ligase seal.

Một lesson quan trọng là repair pathway được chọn theo **loại damage**, không phải theo một thuật toán (algorithm / 알고리즘) duy nhất. Biology dùng modular repair kiến trúc (architecture / 아키텍처) vì lesion có vật lý (physical / 물리적) chemistry khác nhau.

> **Nối mạch:** **7. Direct reversal và tại sao đôi khi “sửa” không cần cắt DNA** nối từ **6. Sửa chữa cắt bỏ nucleotit (nucleotide excision repair): cắt cả đoạn khi helix bị biến dạng** sang **8. Đứt gãy hai mạch (double-strand break): khi cả hai bản template cùng bị đứt**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Direct reversal và tại sao đôi khi “sửa” không cần cắt DNA

Một số damage có thể được đảo trực tiếp về chemical trạng thái (state / 상태) ban đầu. Concept này được gọi chung là **direct reversal**. Ở nhiều organism, photolyase có thể dùng light năng lượng (energy / 에너지) để sửa một số UV-induced lesion; ở human, pathway cụ thể này không đóng vai trò tương tự như ở nhiều species khác.

Điểm cần nhớ không phải tên enzyme, mà là lôgic (logic): nếu chemical modification có thể reverse trực tiếp, việc cắt backbone là không cần thiết. Repair chiến lược (strategy / 전략) phản ánh chemistry của lesion.

> **Nối mạch:** **8. Đứt gãy hai mạch (double-strand break): khi cả hai bản template cùng bị đứt** nối từ **7. Direct reversal và tại sao đôi khi “sửa” không cần cắt DNA** sang **9. Tế bào-cycle phase quyết định repair choice**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Đứt gãy hai mạch (double-strand break): khi cả hai bản template cùng bị đứt

**Đứt gãy hai mạch, DSB (이중가닥 절단)** nguy hiểm vì continuity của cả hai strand bị mất. Nếu repair sai, chromosome có thể deletion, inversion hoặc translocation.

Hai chiến lược chính là **Nối đầu không tương đồng (non-homologous end joining), NHEJ** và **Tái tổ hợp tương đồng (homologous recombination), HR**.

NHEJ nối hai đầu gãy tương đối trực tiếp. Nó nhanh và hoạt động ngay cả khi không có homologous template gần đó, nhưng processing đầu gãy có thể làm mất/thêm vài nucleotide.

HR dùng homologous chuỗi (sequence / 시퀀스), thường nhiễm sắc tử chị em (sister chromatid), làm template nên có thể chính xác hơn. Nhưng HR thuận lợi nhất ở phase khi nhiễm sắc tử chị em đã tồn tại.

Sự đánh đổi (trade-off / 트레이드오프) rất rõ: **speed và availability** của NHEJ đối lại **khuôn (template)-based fidelity** của HR.

> **Nối mạch:** **9. Tế bào-cycle phase quyết định repair choice** nối từ **8. Đứt gãy hai mạch (double-strand break): khi cả hai bản template cùng bị đứt** sang **10. Tái tổ hợp tương đồng: repair machinery được tái sử dụng để tạo biến dị (variation)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Tế bào-cycle phase quyết định repair choice

Repair pathway không hoạt động trong vacuum. Khi tế bào ở G1 chưa có nhiễm sắc tử chị em, HR bị hạn chế. Sau DNA replication ở S/G2, nhiễm sắc tử chị em cung cấp template tốt hơn.

Vì vậy độ ổn định hệ gen nối trực tiếp với [Truyền tín hiệu và Chu kỳ tế bào](../01_cell_biology/02_cell_signaling_and_cell_cycle.md). Điểm kiểm soát chu kỳ tế bào không chỉ hỏi “đã đủ lớn chưa?” mà còn hỏi genome có đủ an toàn để tiếp tục không.

Nếu Tổn thương DNA quá nhiều, cell có thể pause cycle, repair, senescence hoặc apoptosis. Continuation của chu kỳ tế bào (cell cycle) là một **quyết định (decision / 결정) under rủi ro (risk / 위험)**.

> **Nối mạch:** **10. Tái tổ hợp tương đồng: repair machinery được tái sử dụng để tạo biến dị (variation)** nối từ **9. Tế bào-cycle phase quyết định repair choice** sang **11. Recombination khác mutation ở đâu?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Tái tổ hợp tương đồng: repair machinery được tái sử dụng để tạo biến dị (variation)

Trong meiosis, cell chủ động tạo programmed DSB rồi dùng tái tổ hợp tương đồng để tạo trao đổi chéo (crossing-over). Nghe có vẻ nghịch lý: vì sao hệ gen-protection machinery lại tạo break?

Trao đổi chéo vừa tạo allele combination mới vừa giúp nhiễm sắc thể tương đồng (homologous chromosome) liên kết vật lý để segregation trong meiosis I chính xác hơn. Tiến hóa đã tái sử dụng repair machinery thành công cụ reproductive.

Do đó recombination là ví dụ đẹp cho một motif sinh học: **cơ chế (mechanism / 메커니즘) ban đầu giải một ràng buộc (constraint / 제약조건) có thể được co-opt cho hàm (function / 함수) mới**.

> **Nối mạch:** **11. Recombination khác mutation ở đâu?** nối từ **10. Tái tổ hợp tương đồng: repair machinery được tái sử dụng để tạo biến dị (variation)** sang **12. Chạc sao chép stress: genome damage có thể sinh ra ngay trong quá trình bản sao (copy / 복사)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Recombination khác mutation ở đâu?

Mutation tạo chuỗi (sequence / 시퀀스) thay đổi (change / 변경) mới. Recombination chủ yếu reshuffle chuỗi (sequence / 시퀀스)/haplotype đã tồn tại.

Nếu chromosome homolog mang `AB` và `ab`, trao đổi chéo có thể tạo `Ab` và `aB` mà không cần nucleotide mới. Vì vậy sinh sản hữu tính (sexual reproduction) có thể tạo combinatorial diversity rất lớn ngay cả khi tốc độ đột biến mỗi generation tương đối thấp.

Mutation tạo “new letters”; recombination tạo “new arrangement of existing paragraphs”. Cả hai đều quan trọng cho evolution nhưng theo cách khác nhau.

> **Nối mạch:** **12. Chạc sao chép stress: genome damage có thể sinh ra ngay trong quá trình bản sao (copy / 복사)** nối từ **11. Recombination khác mutation ở đâu?** sang **13. Telomere: chromosome tuyến tính (linear / 선형) tạo một bài toán (problem / 문제) mới**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Chạc sao chép stress: genome damage có thể sinh ra ngay trong quá trình bản sao (copy / 복사)

DNA bộ máy sao chép (replication machinery) phải đi qua repeat, tightly bound protein, unusual DNA cấu trúc (structure / 구조) và vùng transcription active. Fork có thể slow hoặc stall. Nếu fork collapse, DSB có thể xuất hiện.

**Căng thẳng sao chép (replication stress) (복제 스트레스)** vì vậy là cầu nối (bridge / 브리지) giữa normal replication và genome instability. Oncogene thúc cell proliferate quá mạnh có thể tăng căng thẳng sao chép, tạo thêm damage và đột biến — một phản hồi dương (positive feedback) nguy hiểm trong tumor evolution.

Điểm này sửa một misconception: mutation không chỉ đến từ “environmental mutagen”; chính việc cell cố bản sao (copy / 복사) genome dưới pressure cũng có thể tạo damage.

> **Nối mạch:** **13. Telomere: chromosome tuyến tính (linear / 선형) tạo một bài toán (problem / 문제) mới** nối từ **12. Chạc sao chép stress: genome damage có thể sinh ra ngay trong quá trình bản sao (copy / 복사)** sang **14. Telomere, senescence và cancer là một sự đánh đổi (trade-off / 트레이드오프) multicellular**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Telomere: chromosome tuyến tính (linear / 선형) tạo một bài toán (problem / 문제) mới

Tuyến tính (linear / 선형) chromosome gặp **end-sao chép bài toán (problem / 문제)** vì conventional polymerase không thể bản sao (copy / 복사) hoàn chỉnh phần cuối mạch theo sau (lagging strand) sau khi primer cuối bị bỏ.

**Telomere (텔로미어)** gồm repeated DNA và protein complex bảo vệ chromosome end. **Telomerase (텔로머레이스)** dùng RNA template nội tại để kéo dài telomeric repeat.

Telomere còn giải một bài toán (problem / 문제) nhận diện: chromosome end tự nhiên phải không bị nhầm với DSB. Nếu repair machinery coi telomere như break và nối hai nhiễm sắc thể, genome sẽ cực kỳ bất ổn.

Vì vậy telomere vừa là sao chép solution vừa là định danh (identity / 식별자) tín hiệu (signal / 신호) cho chromosome end.

> **Nối mạch:** **14. Telomere, senescence và cancer là một sự đánh đổi (trade-off / 트레이드오프) multicellular** nối từ **13. Telomere: chromosome tuyến tính (linear / 선형) tạo một bài toán (problem / 문제) mới** sang **15. Transposable Element: genome chứa thành phần có “lợi ích riêng”**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Telomere, senescence và cancer là một sự đánh đổi (trade-off / 트레이드오프) multicellular

Nhiều somatic cell có telomerase thấp. Sau nhiều division, telomere có thể ngắn đến mức kích hoạt DNA-damage phản hồi (response / 응답) và **senescence (lão hóa tế bào / 세포 노화)**.

Điều này giới hạn proliferation — có lợi để giảm cancer rủi ro (risk / 위험) — nhưng cũng làm tissue renewal giảm theo tuổi. Nhiều tumor tái kích hoạt telomerase hoặc alternative telomere maintenance để vượt proliferative limit.

Do đó aging và cancer không phải hai chủ đề hoàn toàn tách rời. Cả hai chạm vào cùng sự đánh đổi (trade-off / 트레이드오프) giữa tissue regeneration và suppression của uncontrolled proliferation.

> **Nối mạch:** **15. Transposable Element: genome chứa thành phần có “lợi ích riêng”** nối từ **14. Telomere, senescence và cancer là một sự đánh đổi (trade-off / 트레이드오프) multicellular** sang **16. Biến thể cấu trúc (structural variation): mutation không chỉ là đổi một nucleotide**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Transposable Element: genome chứa thành phần có “lợi ích riêng”

**Transposable Element, TE (전이인자)** có thể di chuyển hoặc bản sao (copy / 복사) trong hệ gen. DNA transposon và retrotransposon dùng cơ chế (mechanism / 메커니즘) khác nhau, nhưng cùng có khả năng tạo insertion, rearrangement và regulatory thay đổi (change / 변경).

TE có thể gây damage nếu insert vào coding/vùng điều hòa (regulatory region). Nhưng qua evolutionary thời gian (time / 시간), nhiều chuỗi (sequence / 시퀀스) nguồn gốc TE được host co-opt làm enhancer, promoter hoặc thành phần regulatory.

Đây là ví dụ xung đột (conflict / 충돌)–sự phối hợp (cooperation) ở quy mô phân tử (molecular scale): element có replication interest riêng nhưng sản phẩm (product / 제품) của nó đôi khi trở thành raw material cho host evolution.

> **Nối mạch:** **16. Biến thể cấu trúc (structural variation): mutation không chỉ là đổi một nucleotide** nối từ **15. Transposable Element: genome chứa thành phần có “lợi ích riêng”** sang **17. p53 và Tổn thương DNA phản hồi (response / 응답): repair phải được nối với quyết định (decision / 결정)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Biến thể cấu trúc (structural variation): mutation không chỉ là đổi một nucleotide

Genome có thể thay đổi ở quy mô (scale / 규모) lớn qua deletion, duplication, inversion, translocation và copy-number variation.

**Gene duplication** đặc biệt quan trọng. Sau duplication, một bản sao (copy / 복사) có thể duy trì hàm (function / 함수) cũ trong khi bản sao (copy / 복사) kia tích lũy thay đổi (change / 변경). bản sao (copy / 복사) mới có thể mất hàm (function / 함수), chia nhỏ hàm (function / 함수) với bản sao (copy / 복사) cũ hoặc phát triển hàm (function / 함수) mới.

Nhiều gene family và molecular innovation có nguồn gốc từ lô-gic (logic / 논리) duplication–divergence. Genome evolution vì vậy là lịch sử (history / 이력) của cả base-level thay đổi (change / 변경) và kiến trúc-level thay đổi (change / 변경).

> **Nối mạch:** **17. p53 và Tổn thương DNA phản hồi (response / 응답): repair phải được nối với quyết định (decision / 결정)** nối từ **16. Biến thể cấu trúc (structural variation): mutation không chỉ là đổi một nucleotide** sang **18. Somatic và Đột biến dòng mầm (germline mutation) có consequence khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. p53 và Tổn thương DNA phản hồi (response / 응답): repair phải được nối với quyết định (decision / 결정)

Cell cần đánh giá damage có sửa được không. Một nút (node / 노드) quan trọng trong nhiều mammalian cell là p53. Tổn thương DNA có thể làm pathway ổn định p53; p53 kích hoạt gene liên quan cell-cycle arrest, repair, senescence hoặc apoptosis tùy ngữ cảnh (context / 맥락).

Điểm quan trọng không phải xem p53 như “gene chống ung thư đơn lẻ”, mà như một **quyết định (decision / 결정) nút (node / 노드)** nối thông tin (information / 정보) về damage với hành động (action / 동작) của whole cell.

Nếu damage nhẹ, pause và repair có lợi. Nếu damage quá nặng, apoptosis có thể tốt hơn cho organism dù bất lợi cho tế bào đó. Đây là ví dụ sinh vật-level fitness thắng cell-level survival.

> **Nối mạch:** **18. Somatic và Đột biến dòng mầm (germline mutation) có consequence khác nhau** nối từ **17. p53 và Tổn thương DNA phản hồi (response / 응답): repair phải được nối với quyết định (decision / 결정)** sang **19. Mosaicism: một body không hoàn toàn có một genome duy nhất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Somatic và Đột biến dòng mầm (germline mutation) có consequence khác nhau

**Đột biến dòng mầm (생식계열 돌연변이)** có thể truyền cho offspring và đi vào quần thể (population) gene pool. **Đột biến soma (somatic mutation) (체세포 돌연변이)** thường chỉ ảnh hưởng lineage tế bào trong body.

```text
Germline mutation
→ inheritance
→ population variation
→ evolution qua generation

Somatic mutation
→ clonal mosaicism
→ tissue dysfunction / tumor evolution
→ consequence trong một organism
```

Cùng molecular sự kiện (event / 이벤트) nhưng quy mô (scale / 규모) khác tạo ý nghĩa sinh học (biological meaning) khác. Đây là lý do “mutation tốt hay xấu?” là câu hỏi thiếu ngữ cảnh (context / 맥락).

> **Nối mạch:** **19. Mosaicism: một body không hoàn toàn có một genome duy nhất** nối từ **18. Somatic và Đột biến dòng mầm (germline mutation) có consequence khác nhau** sang **20. Tốc độ đột biến là phenotype có thể tiến hóa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Mosaicism: một body không hoàn toàn có một genome duy nhất

Mặc dù textbook thường nói mọi somatic cell có cùng genome, mutation tích lũy trong development và aging tạo **khảm soma (somatic mosaicism) (체세포 모자이크)**. Một clone có variant riêng có thể chiếm một fraction tissue.

Phần lớn mosaic variant không gây phenotype rõ. Một số ảnh hưởng developmental disorder, aging hoặc cancer rủi ro (risk / 위험). Điều này bổ sung nuance cho statement “mọi cell có cùng DNA”: đúng như approximation nền tảng, nhưng organism thật là một population dòng dõi (lineage) cell có lịch sử (history / 이력) mutation riêng.

> **Nối mạch:** **20. Tốc độ đột biến là phenotype có thể tiến hóa** nối từ **19. Mosaicism: một body không hoàn toàn có một genome duy nhất** sang **21. Tình huống phân tích (case study): BRCA pathway và synthetic lethality như lô-gic (logic / 논리) sinh học hệ thống (systems biology)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Tốc độ đột biến là phenotype có thể tiến hóa

Độ chính xác sao chép và repair machinery bản thân cũng do gene encode. Vì vậy tốc độ đột biến không phải constant tuyệt đối; nó có thể thay đổi qua tiến hóa.

High tốc độ đột biến tạo nhiều beneficial variant hơn khi môi trường (environment / 환경) đổi nhanh, nhưng cũng tạo nhiều đột biến có hại (deleterious mutation). Low tốc độ đột biến bảo vệ genome nhưng giảm exploration. Kích thước quần thể (population size), reproduction chế độ (mode / 모드) và ecological ngữ cảnh (context / 맥락) ảnh hưởng sự đánh đổi (trade-off / 트레이드오프) này.

RNA virus thường có tốc độ đột biến cao hơn cellular organism; DNA organism đầu tư mạnh hơn vào đọc sửa/repair. Không có một tốc độ đột biến “tối ưu cho mọi life”.

> **Nối mạch:** **20. Tốc độ đột biến là phenotype có thể tiến hóa** nêu quy tắc; **21. Tình huống phân tích (case study): BRCA pathway và synthetic lethality như lô-gic (logic / 논리) sinh học hệ thống (systems biology)** thử quy tắc trong tình huống, rồi **22. Tình huống phân tích lập luận (reasoning / 추론): tại sao repair “quá tích cực” cũng có thể nguy hiểm?** mở rộng hệ quả.

## 21. Tình huống phân tích (case study): BRCA pathway và synthetic lethality như lô-gic (logic / 논리) sinh học hệ thống (systems biology)

Một số protein BRCA tham gia tái tổ hợp tương đồng repair. Khi tumor mất HR hàm (function / 함수), nó phụ thuộc mạnh hơn vào repair pathway khác để sống.

Nếu một second pathway bị inhibit, combination có thể gây **synthetic lethality**: mất A riêng chưa chết, mất B riêng chưa chết, nhưng mất cả A và B làm cell không sống được.

Trường hợp (case / 사례) này quan trọng vì nó nối độ ổn định hệ gen với sinh học hệ thống và therapy: weakness của mạng (network / 네트워크) có thể xuất hiện không ở một gene riêng mà ở **phụ thuộc (dependency / 의존성) tạo bởi mạng (network / 네트워크) trạng thái**.

> **Nối mạch:** **21. Tình huống phân tích (case study): BRCA pathway và synthetic lethality như lô-gic (logic / 논리) sinh học hệ thống (systems biology)** nêu quy tắc; **22. Tình huống phân tích lập luận (reasoning / 추론): tại sao repair “quá tích cực” cũng có thể nguy hiểm?** thử quy tắc trong tình huống, rồi **23. Giải trình tự (sequencing) đo lường (measurement / 측정) cũng có bài toán fidelity giống replication** mở rộng hệ quả.

## 22. Tình huống phân tích lập luận (reasoning / 추론): tại sao repair “quá tích cực” cũng có thể nguy hiểm?

Nếu DSB xảy ra ở repeat-rich region, nối nhầm hai trình tự giống nhau nhưng ở vị trí khác có thể gây deletion hoặc translocation. Repair nhanh không đồng nghĩa repair đúng.

Điều này minh họa principle chung: hệ thống sinh học không tối ưu speed riêng, mà phải sự đánh đổi (trade-off / 트레이드오프) speed, fidelity và availability của template. NHEJ hữu ích vì nhanh, nhưng khi accuracy cực quan trọng và nhiễm sắc tử chị em có sẵn, HR thường cho tuyến (route / 경로) an toàn hơn.

> **Nối mạch:** **22. Tình huống phân tích lập luận (reasoning / 추론): tại sao repair “quá tích cực” cũng có thể nguy hiểm?** nêu quy tắc; **23. Giải trình tự (sequencing) đo lường (measurement / 측정) cũng có bài toán fidelity giống replication** thử quy tắc trong tình huống, rồi **24. Các hiểu lầm phổ biến (common misconceptions)** mở rộng hệ quả.

## 23. Giải trình tự (sequencing) đo lường (measurement / 측정) cũng có bài toán fidelity giống replication

Khi giải trình tự (sequencing), instrument cũng có tỉ lệ lỗi. Một variant thấy trong read có thể là biological variant thật hoặc technical lỗi (error / 오류). Coverage, cơ sở (base / 기반) chất lượng (quality / 품질), chất lượng ánh xạ (mapping quality) và strand balance giúp phân biệt tín hiệu (signal / 신호) khỏi noise.

Có một symmetry thú vị:

```text
DNA polymerase: molecule → molecule copy
sequencer: molecule → digital copy
```

Cả hai đều cần lỗi (error / 오류) mô hình (model / 모델) và redundancy. Chương (chapter) [Phương pháp thực nghiệm và đo lường trong Sinh học](../06_biotechnology_computation/01_experimental_methods_and_measurement.md) và [Bioinformatics, thuật toán và Omics Workflow](../06_biotechnology_computation/02_bioinformatics_algorithms_and_omics_workflows.md) phát triển tiếp lô-gic (logic / 논리) này.

> **Nối mạch:** **23. Giải trình tự (sequencing) đo lường (measurement / 측정) cũng có bài toán fidelity giống replication** đặt vấn đề; **24. Các hiểu lầm phổ biến (common misconceptions)** kiểm tra bằng chứng, rồi **25. Mô hình tư duy tổng hợp** mở rộng hệ quả.

## 24. Các hiểu lầm phổ biến (common misconceptions)

“Mutation xảy ra vì organism cần thích nghi” là sai. Mutation không được tạo có chủ đích theo future need; selection thay đổi frequency của variation sau khi variation xuất hiện.

“DNA repair luôn làm chuỗi (sequence / 시퀀스) trở lại hoàn hảo” cũng sai. NHEJ và repair ở ngữ cảnh (context / 맥락) khó có thể để lại indel hoặc rearrangement.

“Recombination chỉ gây mutation” không đúng. Recombination là cơ chế (mechanism / 메커니즘) bình thường và thiết yếu của meiosis, đồng thời là repair pathway.

“Hệ gen ổn định nghĩa mọi cell có DNA giống hệt nhau” quá đơn giản. Khảm soma và biến thể cấu trúc tồn tại, nhưng được giữ trong giới hạn mà organism vẫn hàm (function / 함수).

> **Nối mạch:** Mô hình tư duy tổng hợp sửa các hiểu lầm của mục 24; **cầu nối sang Evolution** mang cơ chế repair, recombination và genome stability sang thay đổi quần thể.

## 25. Mô hình tư duy tổng hợp

Độ ổn định hệ gen có thể được đọc như một hierarchy:

```text
replication fidelity
→ proofreading
→ lesion-specific repair
→ DSB repair choice
→ checkpoint / cell-cycle arrest
→ apoptosis hoặc senescence nếu damage quá lớn
→ tissue-level selection và organism protection
```

Ở chiều ngược lại, những lỗi (error / 오류) thoát qua hierarchy tạo biến dị:

```text
unrepaired / misrepaired change
→ mutation / recombination / structural variation
→ phenotype
→ somatic selection hoặc germline inheritance
→ evolution
```

Stability và evolution vì vậy không đối lập. Evolution cần một hệ thống (system / 시스템) đủ ổn định để heredity có ý nghĩa, đồng thời đủ không hoàn hảo để variation tồn tại.

> **Nối mạch:** **26. cầu nối (bridge / 브리지) sang Evolution** tổng hợp kết quả từ **25. Mô hình tư duy tổng hợp** để khép mạch giải thích.

## 26. cầu nối (bridge / 브리지) sang Evolution

Sau chapter này, nguồn variation không còn là một từ chung chung “đột biến”. Ta đã thấy variation xuất phát từ replication lỗi (error / 오류), oxidative damage, repair choice, tái tổ hợp, transposable element, gene duplication và structural rearrangement.

Nhưng một variant xuất hiện trong một genome vẫn chưa phải evolution. Evolution bắt đầu khi ta theo dõi **frequency của variant trong quần thể qua nhiều generation**. Điều gì làm allele tăng? Khi nào drift mạnh hơn selection? Dòng gen (gene flow) thay population ra sao? Bottleneck làm mất diversity thế nào?

Đó chính là điểm xuất phát của [Tiến hóa và Di truyền quần thể](../03_evolution_and_diversity/00_evolution_and_population_genetics.md).

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Genomics, Epigenetics và Điều hòa hệ gene](02_genomics_epigenetics_and_regulation.md) · [Mục lục Biology](../README.md) · [Tiến hóa và Di truyền quần thể →](../03_evolution_and_diversity/00_evolution_and_population_genetics.md)

> **Bàn giao:** Sau **26. cầu nối (bridge / 브리지) sang Evolution**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
