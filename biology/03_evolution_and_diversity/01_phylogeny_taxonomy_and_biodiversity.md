# Phylogeny, Taxonomy và Đa dạng sinh học — Phylogeny, Taxonomy and Biodiversity (계통학, 분류학과 생물다양성)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phylogeny, Taxonomy và Đa dạng sinh học — Phylogeny, Taxonomy and Biodiversity (계통학, 분류학과 생물다양성)**. Route đi từ đặc điểm và dữ liệu trình tự → cây phát sinh và nhóm đơn ngành → phân loại/tên gọi → nguồn gốc và phân bố đa dạng, để taxonomy phản ánh quan hệ tiến hóa thay vì chỉ là hệ thống nhãn.

Tiến hóa (evolution) cho ta một hình ảnh quan trọng: lịch sử (history / 이력) của life không phải chiếc thang mà là **cây phân nhánh**. Population tách ra, divergence tích lũy, lineage mới hình thành. Chapter này trả lời ba câu hỏi nối tiếp nhau: làm sao reconstruct cây lịch sử đó, làm sao đặt tên/phân loại organism theo ancestry, và biodiversity hiện tại được tổ chức ra sao?

> **mô hình tư duy (mental model / 사고 모델):** phylogeny là hypothesis về lịch sử phân nhánh; taxonomy là hệ thống tên/phân loại cố gắng phản ánh lịch sử (history / 이력) đó; biodiversity là kết quả hiện tại của hàng tỷ năm branching, extinction và ecological diversification.

## 1. cây (tree / 트리) of life không phải “thứ bậc tiến hóa”

Một cây phát sinh chủng loại (phylogenetic tree) gồm nút (node / 노드) và branch. nút (node / 노드) trong cây (tree / 트리) thường biểu diễn tổ tiên chung (common ancestor); tip là dòng dõi (lineage)/species sampled.

Hai tip nằm cạnh nhau trên hình không nhất thiết “giống nhau hơn”; điều quan trọng là **tổ tiên chung gần nhất (most recent common ancestor)**.

Không có tip nào “cao cấp hơn” tip khác. Human và chimpanzee đều là lineage hiện đại, mỗi bên có lịch sử (history / 이력) riêng từ tổ tiên chung.

> **Nối mạch:** Tree of life encodes branching ancestry, not a ladder; reading topology correctly lets homology signal shared origin while analogy signals convergent function.

## 2. Cách đọc một cây (tree / 트리) đúng

Nếu nút (node / 노드) chia thành A và B, A và B là **nhóm chị em (sister taxa)**. Một group gồm ancestor và toàn bộ descendant gọi là **clade (nhánh đơn ngành / 단계통군)**.

Cây (tree / 트리) có thể rotate quanh nút (node / 노드) mà relationship không đổi. Vì vậy thứ tự (order / 순서) trái–phải của tip thường không mang meaning evolutionary progress.

Độ dài nhánh (branch length) chỉ có meaning nếu cây (tree / 트리) được quy mô (scale / 규모) theo amount thay đổi (change / 변경) hoặc thời gian (time / 시간); không phải mọi cây (tree / 트리) đều như vậy.

> **Nối mạch:** **3. Homology và analogy** nối từ **2. Cách đọc một cây (tree / 트리) đúng** sang **4. Đặc điểm dẫn xuất chung (shared derived character)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Homology và analogy

**Cấu trúc tương đồng (homologous structure) (구조적 상동성)** giống nhau do dùng chung (shared / 공유) ancestry. Forelimb của human, bat và whale có same basic bone mẫu (pattern / 패턴) vì thừa hưởng từ tetrapod ancestor.

**Analogous/đặc điểm hội tụ (convergent feature)** có hàm (function / 함수) tương tự nhưng evolve độc lập, như wing của bird và insect.

Phân biệt homology với convergence cực kỳ quan trọng khi reconstruct cây (tree / 트리).

> **Nối mạch:** **4. Đặc điểm dẫn xuất chung (shared derived character)** nối từ **3. Homology và analogy** sang **5. Molecular phylogenetics**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Đặc điểm dẫn xuất chung (shared derived character)

Phylogenetic suy luận (inference / 추론) tìm **dùng chung (shared / 공유) derived characters (synapomorphy / 공유파생형질)** — trait xuất hiện ở tổ tiên chung gần và được descendant chia sẻ.

Một trait ancestral quá rộng thường không giúp phân giải relationship gần.

Ví dụ vertebral column giúp define vertebrate clade nhưng không phân biệt mammal species với nhau.

> **Nối mạch:** **5. Molecular phylogenetics** nối từ **4. Đặc điểm dẫn xuất chung (shared derived character)** sang **6. Căn chỉnh trình tự (sequence alignment) là bước lập luận (reasoning / 추론) chứ không chỉ thao tác kỹ thuật**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Molecular phylogenetics

DNA/protein (protein) trình tự (sequence) cung cấp rất nhiều character. Nếu chuỗi (sequence / 시퀀스) tương đồng do dùng chung (common / 공통) ancestry, mẫu hình (pattern) mutation có thể giúp suy cây (tree / 트리).

Nhưng gene cây (tree / 트리) có thể khác species cây (tree / 트리) do phân loại dòng dõi chưa hoàn tất (incomplete lineage sorting), introgression hoặc chuyển gen ngang (horizontal gene transfer).

Một gene không phải luôn đại diện toàn lịch sử (history / 이력) của species.

> **Nối mạch:** **6. Căn chỉnh trình tự (sequence alignment) là bước lập luận (reasoning / 추론) chứ không chỉ thao tác kỹ thuật** nối từ **5. Molecular phylogenetics** sang **7. Parsimony, likelihood và Bayesian suy luận (inference / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Căn chỉnh trình tự (sequence alignment) là bước lập luận (reasoning / 추론) chứ không chỉ thao tác kỹ thuật

Trước khi so difference, ta cần align nucleotide/axit amin (amino acid) sao cho position tương ứng homologous được đặt cạnh nhau.

Insertion/deletion làm alignment không trivial. thuật toán (algorithm / 알고리즘) dùng scoring cho match, mismatch, gap.

Bad alignment có thể tạo false phylogenetic tín hiệu (signal / 신호). Đây là liên kết (connection / 연결) trực tiếp với bioinformatics.

> **Nối mạch:** **7. Parsimony, likelihood và Bayesian suy luận (inference / 추론)** nối từ **6. Căn chỉnh trình tự (sequence alignment) là bước lập luận (reasoning / 추론) chứ không chỉ thao tác kỹ thuật** sang **8. hỗ trợ (support / 지원) cho branch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Parsimony, likelihood và Bayesian suy luận (inference / 추론)

**Maximum parsimony** chọn cây (tree / 트리) cần ít evolutionary thay đổi (change / 변경) nhất theo mô hình (model / 모델) đơn giản.

**Maximum likelihood** hỏi cây (tree / 트리)/mô hình (model / 모델) nào làm observed chuỗi (sequence / 시퀀스) dữ liệu (data / 데이터) có xác suất (probability / 확률) cao nhất.

**Bayesian phylogenetics** kết hợp prior với likelihood để suy posterior phân phối (distribution / 분포) của cây (tree / 트리)/tham số (parameter).

Không có phương thức (method / 메서드) “nhìn dữ liệu (data / 데이터) rồi cây (tree / 트리) tự xuất hiện”; mỗi suy luận (inference / 추론) dựa trên mô hình (model / 모델) đột biến (mutation)/tiến hóa.

> **Nối mạch:** **8. hỗ trợ (support / 지원) cho branch** nối từ **7. Parsimony, likelihood và Bayesian suy luận (inference / 추론)** sang **9. Đồng hồ phân tử (molecular clock)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. hỗ trợ (support / 지원) cho branch

Bootstrap resampling hoặc posterior xác suất (probability / 확률) được dùng đánh giá hỗ trợ (support / 지원) của clade.

Hỗ trợ (support / 지원) cao không có nghĩa cây (tree / 트리) chắc chắn tuyệt đối; nó phản ánh stability/xác suất (probability / 확률) dưới dữ liệu (data / 데이터) và mô hình đã dùng.

Bất định (uncertainty / 불확실성) nên được giữ lại thay vì ép mọi branch thành certainty.

> **Nối mạch:** **9. Đồng hồ phân tử (molecular clock)** nối từ **8. hỗ trợ (support / 지원) cho branch** sang **10. Phân loại học (taxonomy): đặt tên để communication ổn định**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Đồng hồ phân tử (molecular clock)

Nếu substitution tích lũy gần đều theo thời gian (time / 시간) ở marker phù hợp, chuỗi (sequence / 시퀀스) divergence có thể estimate split thời gian (time / 시간).

Nhưng tỷ lệ (rate / 비율) thay đổi giữa lineage/gen (gene). Calibration bằng fossil hoặc geological sự kiện (event / 이벤트) cần thiết.

Clock là mô hình (model / 모델) có lỗi (error / 오류) bar, không phải đồng hồ literal.

> **Nối mạch:** **10. Phân loại học (taxonomy): đặt tên để communication ổn định** nối từ **9. Đồng hồ phân tử (molecular clock)** sang **11. Three domains**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Phân loại học (taxonomy): đặt tên để communication ổn định

**Phân loại học (phân loại học / 분류학)** đặt tên và group organism.

Binomial nomenclature dùng genus + loài (species), ví dụ *Homo sapiens*.

Hierarchy truyền thống: lĩnh vực (domain / 도메인) → Kingdom → Phylum → lớp (class / 클래스) → thứ tự (order / 순서) → Family → Genus → Loài.

Nhưng phân loại hiện đại ngày càng ưu tiên clade và phylogeny hơn rigid rank.

> **Nối mạch:** **11. Three domains** nối từ **10. Phân loại học (taxonomy): đặt tên để communication ổn định** sang **12. Bacteria: đa dạng chuyển hóa (metabolic diversity) khổng lồ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Three domains

Life cellular hiện đại thường được chia ba lĩnh vực (domain / 도메인): **Bacteria, Archaea, Eukarya**.

Archaea từng bị gộp với bacteria vì đều prokaryotic, nhưng molecular dữ liệu (data / 데이터) cho thấy Archaea có nhiều tính năng (feature / 기능) information-processing gần Eukarya hơn theo một số hệ.

Đây là ví dụ molecular phylogeny thay đổi taxonomy.

> **Nối mạch:** **12. Bacteria: đa dạng chuyển hóa (metabolic diversity) khổng lồ** nối từ **11. Three domains** sang **13. Archaea: không chỉ organism sống ở cực hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Bacteria: đa dạng chuyển hóa (metabolic diversity) khổng lồ

Bacteria không phải synonym “germ gây bệnh”. Phần lớn bacteria không pathogenic; nhiều species essential trong chu trình dinh dưỡng (nutrient cycle), microbiome và công nghệ sinh học (biotechnology).

Bacteria có tế bào (cell) kiến trúc (architecture / 아키텍처) prokaryotic nhưng metabolism rất đa dạng: aerobic/anaerobic respiration, lên men (fermentation), quang hợp (photosynthesis), chemolithotrophy.

> **Nối mạch:** **13. Archaea: không chỉ organism sống ở cực hạn** nối từ **12. Bacteria: đa dạng chuyển hóa (metabolic diversity) khổng lồ** sang **14. Eukarya và major lineage**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Archaea: không chỉ organism sống ở cực hạn

Một số Archaea là extremophile, nhưng rất nhiều sống trong đại dương (ocean), soil và microbiome bình thường.

Methanogen là group đặc biệt tạo methane trong anaerobic môi trường (environment / 환경).

Archaea cho thấy morphology “nhìn giống bacteria” không đồng nghĩa close evolutionary relationship.

> **Nối mạch:** **14. Eukarya và major lineage** nối từ **13. Archaea: không chỉ organism sống ở cực hạn** sang **15. Plant diversity như lịch sử (history / 이력) của chuyển tiếp (transition / 전이) lên land**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Eukarya và major lineage

Eukarya gồm animal, plant, fungi và nhiều protist lineage.

“Protist” thường là convenience category hơn clade tự nhiên duy nhất.

Phát sinh chủng loại hiện đại cho thấy eukaryotic diversity sâu hơn classification schoolbook kingdom đơn giản.

> **Nối mạch:** **15. Plant diversity như lịch sử (history / 이력) của chuyển tiếp (transition / 전이) lên land** nối từ **14. Eukarya và major lineage** sang **16. Fungi: absorptive heterotroph và mạng (network / 네트워크) hyphae**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Plant diversity như lịch sử (history / 이력) của chuyển tiếp (transition / 전이) lên land

Green plant ancestry bắt đầu aquatic. Land colonization tạo thách thức (challenge): tránh mất water, hỗ trợ (support / 지원) body, vận chuyển (transport / 전송), reproduction không phụ thuộc hoàn toàn water.

Bryophyte, vascular plant, seed plant và flowering plant phản ánh các innovation như mô mạch (vascular tissue), hạt (seed), phấn hoa (pollen), hoa (flower)/fruit.

Plant biology chapter sẽ xem cơ chế (mechanism / 메커니즘) của những innovation này.

> **Nối mạch:** **16. Fungi: absorptive heterotroph và mạng (network / 네트워크) hyphae** nối từ **15. Plant diversity như lịch sử (history / 이력) của chuyển tiếp (transition / 전이) lên land** sang **17. Animal diversity và sơ đồ cơ thể (body plan)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Fungi: absorptive heterotroph và mạng (network / 네트워크) hyphae

Fungi không phải plant. Chúng lấy nutrient bằng secretion enzyme ra môi trường rồi absorb sản phẩm (product / 제품).

Hypha tạo mycelium với diện tích bề mặt (surface area) lớn, rất phù hợp decomposition và symbiosis.

Mycorrhiza nối fungi với plant gốc (root / 루트), ảnh hưởng nutrient acquisition và ecosystem chu trình dinh dưỡng.

> **Nối mạch:** **17. Animal diversity và sơ đồ cơ thể (body plan)** nối từ **16. Fungi: absorptive heterotroph và mạng (network / 네트워크) hyphae** sang **18. Biodiversity có nhiều cấp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Animal diversity và sơ đồ cơ thể (body plan)

Animal evolution tạo nhiều sơ đồ cơ thể khác nhau về symmetry, tissue tầng (layer / 계층), body cavity, segmentation và phát triển (development).

Không cần học toàn taxonomy trước để hiểu principle: chương trình phát triển (developmental program) và điều hòa gen (gene regulation) tạo kiến trúc (architecture / 아키텍처) body; selection và lịch sử (history / 이력) tạo diversification.

Vertebrate chỉ là một nhánh nhỏ trong animal diversity.

> **Nối mạch:** **18. Biodiversity có nhiều cấp** nối từ **17. Animal diversity và sơ đồ cơ thể (body plan)** sang **19. Species richness và evenness**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Biodiversity có nhiều cấp

**Đa dạng sinh học (biodiversity / 생물다양성)** gồm ít nhất:

- đa dạng di truyền (genetic diversity) trong loài;
- species diversity trong quần xã (community);
- ecosystem diversity trên landscape.

Mất biodiversity không chỉ là “mất số loài”. mất mát (loss / 손실) đa dạng di truyền làm population khó adapt; mất mát (loss / 손실) nhóm chức (functional group) có thể đổi ecosystem quá trình (process).

> **Nối mạch:** **19. Species richness và evenness** nối từ **18. Biodiversity có nhiều cấp** sang **20. Extinction là phần tự nhiên của evolution nhưng tỷ lệ (rate / 비율) quan trọng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Species richness và evenness

Community có thể có cùng số species nhưng phân phối (distribution / 분포) abundance rất khác.

**Richness** là số loài; **evenness** phản ánh abundance phân bố đều đến đâu.

Diversity chỉ mục (index / 인덱스) kết hợp hai dimension, nhưng choice chỉ số (metric / 지표) phụ thuộc question.

> **Nối mạch:** **20. Extinction là phần tự nhiên của evolution nhưng tỷ lệ (rate / 비율) quan trọng** nối từ **19. Species richness và evenness** sang **21. Bức xạ thích nghi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Extinction là phần tự nhiên của evolution nhưng tỷ lệ (rate / 비율) quan trọng

Lineage luôn xuất hiện và biến mất trong lịch sử (history / 이력). Tuyệt chủng hàng loạt (mass extinction) là period mất diversity rất nhanh ở geological quy mô (scale / 규모).

Sau tuyệt chủng (extinction), ecological niche trống có thể tạo bức xạ thích nghi (adaptive radiation) ở surviving lineage.

Hiện tại (current / 현재) extinction concern không phải vì “extinction chưa từng xảy ra”, mà vì tốc độ (rate), cause và hệ quả (consequence) đối với ecosystem/human society.

> **Nối mạch:** **21. Bức xạ thích nghi** nối từ **20. Extinction là phần tự nhiên của evolution nhưng tỷ lệ (rate / 비율) quan trọng** sang **22. Convergent evolution**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Bức xạ thích nghi

Khi lineage tiếp cận nhiều niche mới, diversification có thể nhanh. Island colonization hoặc key innovation có thể mở ecological opportunity.

Darwin’s finches thường được dùng minh họa beak diversification theo food niche.

Phát sinh chủng loại (phylogeny) + ecology cùng giải thích mẫu (pattern / 패턴).

> **Nối mạch:** **22. Convergent evolution** nối từ **21. Bức xạ thích nghi** sang **23. Chuyển gen ngang làm cây (tree / 트리) of life thành mạng (network / 네트워크) ở microbes**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Convergent evolution

Môi trường (environment / 환경) tương tự có thể favor solution tương tự ở lineage xa nhau.

Streamlined body ở shark, ichthyosaur extinct và dolphin là convergence do hydrodynamic ràng buộc (constraint / 제약조건), không phải close ancestry.

Convergence nhắc ta không suy cây (tree / 트리) chỉ từ superficial similarity.

> **Nối mạch:** **23. Chuyển gen ngang làm cây (tree / 트리) of life thành mạng (network / 네트워크) ở microbes** nối từ **22. Convergent evolution** sang **24. Nội cộng sinh (endosymbiosis) và chimeric lịch sử (history / 이력) của eukaryote**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Chuyển gen ngang làm cây (tree / 트리) of life thành mạng (network / 네트워크) ở microbes

Bacteria/Archaea có thể trao đổi gene qua transformation, transduction, conjugation.

Vì vậy một gene như kháng kháng sinh (antibiotic resistance) có lịch sử (history / 이력) khác organism dòng dõi.

Ở deep microbial evolution, “cây (tree / 트리)” đôi khi cần bổ sung mạng (network / 네트워크) reticulation.

> **Nối mạch:** **24. Nội cộng sinh (endosymbiosis) và chimeric lịch sử (history / 이력) của eukaryote** nối từ **23. Chuyển gen ngang làm cây (tree / 트리) of life thành mạng (network / 네트워크) ở microbes** sang **25. Biogeography**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Nội cộng sinh (endosymbiosis) và chimeric lịch sử (history / 이력) của eukaryote

Mitochondria bắt nguồn từ bacterial endosymbiont; chloroplast từ cyanobacterial lineage.

Eukaryotic cell vì vậy mang genetic/lịch sử (history / 이력) thành phần (component / 컴포넌트) từ nhiều lineage.

Evolution không chỉ phân nhánh; đôi khi lineage merge qua symbiosis.

> **Nối mạch:** **25. Biogeography** nối từ **24. Nội cộng sinh (endosymbiosis) và chimeric lịch sử (history / 이력) của eukaryote** sang **26. Conservation cần phylogeny**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Biogeography

Phân phối (distribution / 분포) species trên Earth chứa bằng chứng (evidence / 증거) lịch sử (history / 이력). Island species thường gần relative trên mainland/nearby island nhưng diverge sau isolation.

Continental drift cũng giải thích mẫu (pattern / 패턴) hóa thạch (fossil)/living species.

Biogeography nối evolution với geology và sinh thái học (ecology).

> **Nối mạch:** **26. Conservation cần phylogeny** nối từ **25. Biogeography** sang **27. Tình huống phân tích (case study): whale vẫn là mammal**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Conservation cần phylogeny

Nếu phải ưu tiên conservation, giữ evolutionary distinct lineage có thể bảo tồn nhiều unique lịch sử (history / 이력)/hàm (function / 함수) hơn chỉ đếm species.

Phylogenetic diversity là một dimension của biodiversity planning.

Nhưng conservation quyết định (decision / 결정) còn phụ thuộc ecology, xã hội (social / 사회적) giá trị (value / 값) và độ bất định (uncertainty / 불확실성); không có một chỉ số (metric / 지표) duy nhất quyết định mọi thứ.

> **Nối mạch:** **26. Conservation cần phylogeny** nêu quy tắc; **27. Tình huống phân tích (case study): whale vẫn là mammal** thử quy tắc trong tình huống, rồi **28. Tình huống phân tích: giant panda taxonomy** mở rộng hệ quả.

## 27. Tình huống phân tích (case study): whale vẫn là mammal

Whale sống dưới nước và body streamlined giống fish ở superficial mức (level / 수준), nhưng anatomy, development và molecular phylogeny đặt whale trong mammals, gần hippo hơn fish.

Convergent adaptation với aquatic môi trường (environment / 환경) làm body shape giống fish.

Cây (tree / 트리) thinking giúp phân biệt ancestry với hàm (function / 함수).

> **Nối mạch:** **27. Tình huống phân tích (case study): whale vẫn là mammal** nêu quy tắc; **28. Tình huống phân tích: giant panda taxonomy** thử quy tắc trong tình huống, rồi **29. Các hiểu lầm phổ biến (common misconceptions)** mở rộng hệ quả.

## 28. Tình huống phân tích: giant panda taxonomy

Hình thái (morphology)/diet từng gây tranh luận quan hệ (relation / 관계) của giant panda. Molecular bằng chứng (evidence / 증거) đặt giant panda trong bear family, còn red panda ở lineage riêng gần musteloid group hơn.

DNA dữ liệu (data / 데이터) có thể resolve ambiguity mà hình thái đơn độc khó giải.

> **Nối mạch:** **28. Tình huống phân tích: giant panda taxonomy** nêu quy tắc; **29. Các hiểu lầm phổ biến (common misconceptions)** thử quy tắc trong tình huống, rồi **Cây (tree / 트리) suy luận (inference / 추론) có thể thất bại khi mô hình (model / 모델) sai** mở rộng hệ quả.

## 29. Các hiểu lầm phổ biến (common misconceptions)

“cây (tree / 트리) tip nằm cao hơn là tiến hóa hơn” sai.

“Species hiện đại là ancestor trực tiếp của species hiện đại khác” thường sai; chúng share ancestor đã extinct hoặc ancestral population.

“Taxonomy là hệ thống cố định từ Linnaeus” sai; classification đổi theo bằng chứng (evidence / 증거) phát sinh chủng loại.

“Bacteria là một nhóm organism thành phần nguyên thủy (primitive / 기본 요소) ít diversity” sai.

“Giống morphology = gần họ” có thể sai vì convergence.

<!-- depth-audit-2026:tree-model-failure -->

> **Nối mạch:** **Cây (tree / 트리) suy luận (inference / 추론) có thể thất bại khi mô hình (model / 모델) sai** nối từ **29. Các hiểu lầm phổ biến (common misconceptions)** sang **30. cầu nối (bridge / 브리지): microbe và virus làm evolutionary quy tắc (rule / 규칙) trở nên rõ nhất**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cây (tree / 트리) suy luận (inference / 추론) có thể thất bại khi mô hình (model / 모델) sai

Nhiều substitution ở cùng một site có thể che lịch sử (history / 이력) cũ; lineage tiến hóa nhanh có thể vô tình giống nhau ở nhiều position. Nếu mô hình (model / 모델) không xử lý tỷ lệ (rate / 비율) variation hoặc composition độ lệch (bias / 편향) phù hợp, **hấp dẫn nhánh dài (long-branch attraction)** có thể kéo các lineage xa nhau thành group giả, đặc biệt với phương pháp đơn giản.

Gene cây (tree / 트리) và species cây (tree / 트리) cũng khác nhau theo cơ chế. Incomplete lineage sorting xảy ra khi ancestral polymorphism tồn tại qua nhiều speciation sự kiện (event / 이벤트); introgression đưa gene qua ranh giới (boundary / 경계) loài; HGT chuyển gene giữa lineage không theo parent–offspring. Vì vậy hiện đại (modern / 현대적) phylogenomics thường tổng hợp nhiều locus thay vì tin một gene duy nhất.

**Tái dựng trạng thái tổ tiên (ancestral-state reconstruction)** có thể estimate trait ở nút (node / 노드) quá khứ, nhưng conclusion phụ thuộc cây (tree / 트리), mô hình (model / 모델) chuyển tiếp (transition / 전이) và sampling. Càng lùi sâu, bất định (uncertainty / 불확실성) thường tăng. Phylogeny mạnh nhất khi giữ bất định (uncertainty / 불확실성) hiển thị thay vì biến hypothesis thành certainty.

Trong conservation, phylogenetic diversity bổ sung chứ không thay thế abundance, ecological hàm (function / 함수) hay extinction rủi ro (risk / 위험). Một quyết định tốt phải ghép lịch sử (history / 이력), hàm (function / 함수), population viability và xã hội (social / 사회적) ràng buộc (constraint / 제약조건); không có một chỉ số duy nhất “tối ưu biodiversity”.

> **Nối mạch:** Cầu nối về microbe và virus khép mạch bằng cách dùng failure của phylogenetic inference để làm rõ evolutionary rules.

## 30. cầu nối (bridge / 브리지): microbe và virus làm evolutionary quy tắc (rule / 규칙) trở nên rõ nhất

Phát sinh chủng loại cho ta map diversity, nhưng microbes đặt ra những câu hỏi đặc biệt: thời gian thế hệ (generation time) ngắn, population cực lớn, chuyển gen ngang mạnh, chuyển hóa (metabolism) đa dạng, virus phụ thuộc host nhưng evolution nhanh.

[Vi sinh vật và Virus](02_microorganisms_and_viruses.md) sẽ dùng chính sinh học tế bào (cell biology), genetics và evolution vừa học để hiểu microbial life và virus.

Sau đó organismal biology sẽ chuyển sang câu hỏi khác: multicellular lineage giải bài toán vận chuyển (transport / 전송), điều khiển (control / 제어) và phát triển ở whole-quy mô sinh vật (organism scale) thế nào?

> **Mô hình tư duy cuối chapter:** biodiversity không phải danh mục (catalog / 카탈로그) tĩnh. Nó là snapshot của branching lịch sử (history / 이력) cộng extinction, convergence, di chuyển (migration / 마이그레이션) và ecological diversification. Cây phát sinh chủng loại là mô hình để reconstruct lịch sử (history / 이력) đó từ bằng chứng (evidence / 증거), không phải chiếc thang xếp organism từ thấp tới cao.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Tiến hóa và Di truyền quần thể](00_evolution_and_population_genetics.md) · [Mục lục Biology](../README.md) · [Vi sinh vật và Virus →](02_microorganisms_and_viruses.md)

> **Bàn giao:** Sau **30. cầu nối (bridge / 브리지): microbe và virus làm evolutionary quy tắc (rule / 규칙) trở nên rõ nhất**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
