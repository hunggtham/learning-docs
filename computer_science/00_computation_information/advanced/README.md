# Advanced Computation & Information

Library này mở rộng từ [foundation Computation & Information](../../basic/00_computation_information/00_what_computer_science_studies.md). Các chapter tập trung vào formal reasoning: computer có thể biểu diễn gì, tính được gì, kiểm chứng được gì, resource nào giới hạn computation, uncertainty được đo thế nào và interaction/randomness thay đổi verification power ra sao.

## Canonical chapters

1. [Formal models, reductions và computability](./00_formal_models_reductions_and_computability.md)
2. [Automata hierarchy, grammars và language recognition](./01_automata_hierarchy_grammars_and_language_recognition.md)
3. [Rice's theorem, semantic properties và static-analysis limits](./02_rices_theorem_semantic_properties_and_static_analysis_limits.md)
4. [Kolmogorov complexity, compression và incompressibility](./03_kolmogorov_complexity_compression_and_incompressibility.md)
5. [Information theory, coding bounds và noisy channels](./04_information_theory_coding_bounds_and_noisy_channels.md)
6. [Randomness, entropy sources và computational unpredictability](./05_randomness_entropy_sources_and_computational_unpredictability.md)
7. [Complexity classes beyond P/NP: co-NP, PSPACE, EXP và randomized classes](./06_complexity_classes_conp_pspace_exp_and_randomized_classes.md)
8. [Interactive proofs, zero-knowledge và verifiable computation](./07_interactive_proofs_zero_knowledge_and_verifiable_computation.md)

## Reasoning path

Track này không phải một danh sách lý thuyết rời rạc. Nó tạo chuỗi dependency:

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

Ba chapter đầu trả lời **computer có thể nhận biết và quyết định điều gì trong nguyên tắc**. Kolmogorov complexity và information theory chuyển sang câu hỏi **một object/distribution thực sự chứa bao nhiêu uncertainty hoặc regularity**. Randomness phân biệt entropy thật với deterministic expansion và computational unpredictability. Complexity classes thêm giới hạn time/space/randomness. Interactive proofs cho thấy verification power còn phụ thuộc interaction, challenge và proof structure.

## Các distinction bắt buộc

Khi đọc hết track, người đọc cần phân biệt được:

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

Các distinction này là prerequisite cho static analysis, cryptography, compression, randomized algorithms, database encoding, machine learning và verifiable systems.

## Connection với Mathematics và các domain khác

Các proof toán thuần dài về probability, combinatorics, algebra hoặc number theory nên cross-link sang `mathematics/` thay vì duplicate. Computer Science track sở hữu câu hỏi computational: model nào đang được dùng, resource bound nào quan trọng, representation nào làm information/code length thay đổi, attacker/verifier có power gì và theorem đó thay đổi engineering decision ra sao.

Các connection quan trọng:

- compression/encoding → [`05_data_databases/advanced`](../../05_data_databases/advanced/README.md);
- randomness/cryptographic assumptions → [`07_security_reliability/advanced`](../../07_security_reliability/advanced/README.md);
- randomized/approximation algorithms → [`01_algorithms_data_structures/advanced`](../../01_algorithms_data_structures/advanced/README.md);
- queue/capacity/cost của prover hoặc heavy computation → [`08_software_systems/advanced`](../../08_software_systems/advanced/README.md);
- AI cross-entropy/inference systems → [`10_ai_foundations/advanced`](../../10_ai_foundations/advanced/README.md).

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

Hai tuyến gặp nhau ở cryptography và verifiable computation, nơi randomness, computational hardness, information leakage và proof semantics cùng xuất hiện.

Không cần học thuộc toàn bộ class containment hay theorem name. Với mỗi concept, ưu tiên hỏi:

```text
Problem ban đầu là gì?
Model và representation nào được giả định?
Resource hoặc uncertainty nào đang được đo?
Theorem cho guarantee gì và không guarantee gì?
Open problem nào chưa được phép coi là fact?
Engineering system thực tế dùng concept này ở boundary nào?
```

Mục tiêu cuối cùng là dùng theory để đặt đúng câu hỏi về giới hạn, không dùng theory như vocabulary trang trí.