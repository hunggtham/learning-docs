# Advanced Computation & thông tin (information / 정보)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Advanced Computation & thông tin (information / 정보)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Chuẩn gốc (canonical / 정본) chapters** chỉ đường quay lại owner và tài liệu chuẩn khi cần đào sâu; sau đó sang **Lập luận (reasoning / 추론) đường dẫn (path / 경로)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Thư viện (library / 라이브러리) này mở rộng từ [foundation Computation & Information](../../basic/00_computation_information/00_what_computer_science_studies.md). Các chapter tập trung vào formal lập luận (reasoning / 추론): computer có thể biểu diễn gì, tính được gì, kiểm chứng được gì, tài nguyên (resource / 자원) nào giới hạn computation, bất định (uncertainty / 불확실성) được đo thế nào và tương tác (interaction / 상호작용)/randomness thay đổi xác minh (verification / 확인) power ra sao.

## Chuẩn gốc (canonical / 정본) chapters

1. [Formal models, reductions và computability](./00_formal_models_reductions_and_computability.md)
2. [Automata hierarchy, grammars và language recognition](./01_automata_hierarchy_grammars_and_language_recognition.md)
3. [Rice's theorem, semantic properties và static-analysis limits](./02_rices_theorem_semantic_properties_and_static_analysis_limits.md)
4. [Kolmogorov complexity, compression và incompressibility](./03_kolmogorov_complexity_compression_and_incompressibility.md)
5. [Information theory, coding bounds và noisy channels](./04_information_theory_coding_bounds_and_noisy_channels.md)
6. [Randomness, entropy sources và computational unpredictability](./05_randomness_entropy_sources_and_computational_unpredictability.md)
7. [Complexity classes beyond P/NP: co-NP, PSPACE, EXP và randomized classes](./06_complexity_classes_conp_pspace_exp_and_randomized_classes.md)
8. [Interactive proofs, zero-knowledge và verifiable computation](./07_interactive_proofs_zero_knowledge_and_verifiable_computation.md)

> **Chuyển mạch:** Trong **Advanced Computation & thông tin (information / 정보)**, **Chuẩn gốc (canonical / 정본) chapters** xác định đầu vào; **Lập luận (reasoning / 추론) đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Các distinction bắt buộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lập luận (reasoning / 추론) đường dẫn (path / 경로)

Nhánh học (track / 트랙) này không phải một danh sách lý thuyết rời rạc. Nó tạo chuỗi phụ thuộc (dependency / 의존성):

```text
formal model
→ computability / undecidability
→ semantic-analysis limits
→ description length / incompressibility
→ probability / entropy / coding
→ entropy source / pseudorandomness
→ resource-bounded complexity
→ proof / interaction / verifiable computation
```

Ba chapter đầu trả lời **computer có thể nhận biết và quyết định điều gì trong nguyên tắc**. Kolmogorov độ phức tạp (complexity / 복잡도) và thông tin (information / 정보) lý thuyết (theory / 이론) chuyển sang câu hỏi **một đối tượng (object / 객체)/phân phối (distribution / 분포) thực sự chứa bao nhiêu bất định (uncertainty / 불확실성) hoặc regularity**. Randomness phân biệt entropy thật với deterministic expansion và computational unpredictability. độ phức tạp (complexity / 복잡도) classes thêm giới hạn thời gian (time / 시간)/không gian (space / 공간)/randomness. Interactive proofs cho thấy xác minh (verification / 확인) power còn phụ thuộc tương tác (interaction / 상호작용), challenge và proof cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Advanced Computation & thông tin (information / 정보)**, **Lập luận (reasoning / 추론) đường dẫn (path / 경로)** xác định đầu vào; **Các distinction bắt buộc** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Liên kết (connection / 연결) với Mathematics và các lĩnh vực (domain / 도메인) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các distinction bắt buộc

Khi đọc hết nhánh học (track / 트랙), người đọc cần phân biệt được:

```text
undecidable
≠ computationally expensive

Kolmogorov complexity của một object
≠ Shannon entropy của một distribution

statistical randomness
≠ algorithmic incompressibility
≠ cryptographic unpredictability

worst-case hardness
≠ practical hardness của mọi instance

proof of a relation
≠ authorization / freshness / availability của toàn system
```

Các distinction này là prerequisite cho static phân tích (analysis / 분석), cryptography, compression, randomized algorithms, cơ sở dữ liệu (database / 데이터베이스) encoding, machine học tập (learning / 학습) và verifiable các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced Computation & thông tin (information / 정보)**, sau nội dung của **Các distinction bắt buộc**, **Liên kết (connection / 연결) với Mathematics và các lĩnh vực (domain / 도메인) khác** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Cách đọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) với Mathematics và các lĩnh vực (domain / 도메인) khác

Các proof toán thuần dài về xác suất (probability / 확률), combinatorics, algebra hoặc number lý thuyết (theory / 이론) nên cross-link sang `mathematics/` thay vì duplicate. Khoa học máy tính (computer science / 컴퓨터 과학) nhánh học (track / 트랙) sở hữu câu hỏi computational: mô hình (model / 모델) nào đang được dùng, tài nguyên (resource / 자원) bound nào quan trọng, biểu diễn (representation / 표현) nào làm thông tin (information / 정보)/mã (code / 코드) length thay đổi, attacker/verifier có power gì và theorem đó thay đổi kỹ thuật (engineering / 엔지니어링) quyết định (decision / 결정) ra sao.

Các liên kết (connection / 연결) quan trọng:

- compression/encoding → [`05_data_databases/advanced`](../../05_data_databases/advanced/README.md);
- randomness/cryptographic các giả định (assumptions / 가정들) → [`07_security_reliability/advanced`](../../07_security_reliability/advanced/README.md);
- randomized/approximation algorithms → [`01_algorithms_data_structures/advanced`](../../01_algorithms_data_structures/advanced/README.md);
- hàng đợi (queue / 큐)/sức chứa (capacity / 용량)/chi phí (cost / 비용) của prover hoặc heavy computation → [`08_software_systems/advanced`](../../08_software_systems/advanced/README.md);
- AI cross-entropy/suy luận (inference / 추론) các hệ thống (systems / 시스템들) → [`10_ai_foundations/advanced`](../../10_ai_foundations/advanced/README.md).

> **Chuyển mạch:** Trong **Advanced Computation & thông tin (information / 정보)**, **Cách đọc** tiếp nhận điểm tựa từ **Liên kết (connection / 연결) với Mathematics và các lĩnh vực (domain / 도메인) khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cách đọc

Nếu mới học formal CS, đọc `00 → 01 → 02` trước. Sau đó có hai tuyến tự nhiên:

```text
Information path:
03 Kolmogorov
→ 04 Information Theory
→ 05 Randomness

Computation/verification path:
06 Complexity Classes
→ 07 Interactive Proofs
```

Hai tuyến gặp nhau ở cryptography và verifiable computation, nơi randomness, computational hardness, thông tin (information / 정보) leakage và proof ngữ nghĩa (semantics / 의미론) cùng xuất hiện.

Không cần học thuộc toàn bộ lớp (class / 클래스) containment hay theorem name. Với mỗi concept, ưu tiên hỏi:

```text
Problem ban đầu là gì?
Model và representation nào được giả định?
Resource hoặc uncertainty nào đang được đo?
Theorem cho guarantee gì và không guarantee gì?
Open problem nào chưa được phép coi là fact?
Engineering system thực tế dùng concept này ở boundary nào?
```

Mục tiêu cuối cùng là dùng lý thuyết (theory / 이론) để đặt đúng câu hỏi về giới hạn, không dùng lý thuyết (theory / 이론) như vocabulary trang trí.

> **Bàn giao:** Sau **Cách đọc**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
