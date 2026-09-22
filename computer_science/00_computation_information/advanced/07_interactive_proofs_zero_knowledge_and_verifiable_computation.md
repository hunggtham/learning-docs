# Interactive proofs, zero-knowledge và verifiable computation

Trong NP-style verification, prover đưa một certificate và verifier kiểm tra. Nhưng interaction tạo thêm khả năng: verifier có thể gửi challenge ngẫu nhiên, prover trả lời, rồi verifier dùng nhiều vòng để kiểm tra một claim mà không tự làm toàn bộ computation.

Từ đây xuất hiện ba ý tưởng lớn:

```text
interactive proof
→ kiểm tra claim bằng interaction + randomness

zero-knowledge
→ chứng minh claim mà không tiết lộ thêm secret witness

verifiable computation
→ outsource computation nhưng vẫn kiểm tra result rẻ hơn việc chạy lại toàn bộ
```

Chapter này không nhằm biến người đọc thành cryptographer. Mục tiêu là xây mental model về **completeness, soundness, knowledge leakage, commitment, challenge và verification cost** để hiểu proof systems hiện đại mà không dừng ở buzzword như ZK, SNARK hay STARK.

## 1. Prover mạnh, verifier rẻ

Ta có hai actor:

**Prover (người chứng minh / 증명자)** có thể có computation power lớn hoặc biết secret witness.

**Verifier (người kiểm chứng / 검증자)** muốn kiểm tra claim với ít resource hơn và không tin prover.

Protocol là state machine:

```text
claim x
→ prover message
→ verifier challenge/randomness
→ prover response
→ ...
→ verifier accept/reject
```

Interaction cho verifier tạo uncertainty mà prover không biết trước khi commit một phần state, làm cheating khó hơn.

## 2. Completeness và soundness

Một proof protocol cần ít nhất hai contract.

**Completeness**: nếu statement đúng và prover honest có witness hợp lệ, verifier accept với xác suất cao.

**Soundness**: nếu statement sai, cheating prover không thể làm verifier accept ngoài xác suất nhỏ.

```text
true statement + honest prover
→ accept

false statement + arbitrary cheating prover
→ reject với xác suất cao
```

Soundness có thể là statistical hoặc computational tùy protocol/assumption.

Một proof “thường pass” nhưng không có soundness argument chỉ là test, không phải proof system theo nghĩa mạnh.

## 3. Tại sao randomness giúp verifier

Nếu verifier luôn gửi cùng challenge biết trước, prover có thể chuẩn bị response giả chỉ cho challenge đó.

Random challenge buộc prover phải có state đủ nhất quán để trả lời nhiều khả năng.

Trực giác giống kiểm tra một object lớn bằng spot-checking có cấu trúc. Nếu prover không biết verifier sẽ hỏi vị trí/combination nào, việc giả mạo toàn bộ consistency khó hơn.

Nhưng sampling ngẫu nhiên chỉ tạo soundness khi mathematical structure bảo đảm cheating làm nhiều challenge thất bại. “Randomly check vài dòng” không tự động là cryptographic proof.

## 4. Interactive proof mở rộng verification power

Complexity theory cho thấy interaction + randomness có sức mạnh đáng ngạc nhiên. Kết quả nổi tiếng `IP = PSPACE` nói rằng class problem có interactive proof polynomial-time verifier bằng PSPACE.

Điểm cần hiểu không phải thuộc theorem để dùng hàng ngày, mà là insight:

```text
verification power
không chỉ phụ thuộc local compute của verifier
mà còn phụ thuộc protocol interaction + randomness
```

Đọc prerequisite: [Complexity classes beyond P/NP](./06_complexity_classes_conp_pspace_exp_and_randomized_classes.md).

## 5. Proof of knowledge khác proof of statement

Một protocol có thể chứng minh “statement đúng” hoặc mạnh hơn là prover **biết witness** tương ứng theo formal extractor notion.

Ví dụ authentication muốn chứng minh client biết secret key chứ không chỉ statement “có ai đó tồn tại biết key”.

Proof-of-knowledge reasoning cần cẩn thận: từ “knowledge” trong cryptography có formal meaning qua khả năng extractor lấy witness từ prover đáp ứng protocol, không phải đọc tâm trí actor.

## 6. Commitment: khóa lựa chọn trước khi thấy challenge

**Commitment scheme** giống phong bì số:

```text
commit phase:
prover chọn value v + randomness r
→ commitment c

open phase:
prover reveal v,r
→ verifier check c
```

Hai property chính:

**Hiding**: commitment không tiết lộ value trước khi open.

**Binding**: prover không thể dễ dàng mở cùng commitment thành hai value khác nhau.

Commitment tạo temporal invariant:

```text
prover phải khóa lựa chọn
trước khi biết challenge tiếp theo
```

Nó là primitive quan trọng trong zero-knowledge, coin flipping, MPC và nhiều protocol khác.

## 7. Sigma protocol intuition

Nhiều identification/proof-of-knowledge protocol có ba bước dạng:

```text
commitment a
→ random challenge e
→ response z
```

thường gọi là **Σ-protocol** vì transcript có ba nhánh message.

Các property như completeness, special soundness và honest-verifier zero-knowledge có thể được chứng minh cho construction cụ thể.

Điểm reasoning quan trọng: cùng commitment mà trả lời đúng hai challenge khác nhau đôi khi cho phép extractor recover witness. Vì vậy prover không biết witness khó chuẩn bị state chịu được challenge ngẫu nhiên.

## 8. Zero-knowledge: verifier học gì ngoài truth của statement?

Một proof có thể sound nhưng leak witness. **Zero-knowledge (ZK / 영지식 증명)** thêm privacy property: verifier không học thêm thông tin đáng kể ngoài việc statement đúng.

Formal intuition dùng **simulator**. Nếu có algorithm tạo transcript không phân biệt được với interaction thật mà không biết witness, transcript thật không mang extra knowledge mà verifier có thể khai thác.

Mental model:

```text
real interaction with witness
≈
simulated view without witness
```

Dấu `≈` có thể là perfect, statistical hoặc computational indistinguishability tùy definition.

Zero-knowledge không có nghĩa “không có data nào được gửi”. Có transcript, commitment, proof bytes; property là transcript không tiết lộ knowledge ngoài statement theo model.

## 9. Ví dụ trực giác: chứng minh biết password mà không gửi password

Authentication cổ điển gửi password qua secure channel rồi server so hash. ZK-style identification hướng tới proof rằng client biết secret tương ứng public relation mà không truyền secret itself.

Nhưng zero-knowledge không tự động giải quyết phishing, compromised endpoint hoặc stolen session token. Nếu malware đọc witness trước proof hoặc hijack authenticated session sau proof, privacy của transcript không cứu được system.

Security boundary vẫn phải đi end-to-end.

## 10. Fiat–Shamir: biến challenge interactive thành deterministic hash challenge

Một số public-coin interactive protocols có thể được chuyển thành non-interactive proof/signature-like construction bằng **Fiat–Shamir heuristic**:

```text
challenge = H(statement, commitment, context...)
```

Thay vì verifier gửi random challenge, prover tính challenge từ hash transcript/context.

Security reasoning thường dựa trên random-oracle model hoặc assumptions/construction cụ thể. Không được hiểu đơn giản “hash là random nên interaction biến mất miễn phí”. Domain separation, transcript binding và context phải đúng để tránh replay/cross-protocol issue.

## 11. Non-interactive proof cần setup/assumption gì?

Khi không có live verifier challenge, system cần nguồn public parameters hoặc cryptographic assumption tạo unpredictability/binding tương đương.

Một số proof system dùng **trusted setup** để tạo structured reference string. Nếu toxic waste bị giữ và attacker khai thác được, soundness có thể bị phá tùy scheme.

Các scheme khác dùng transparent setup hoặc public randomness nhưng trả cost khác về proof size, verification time hoặc prover work.

Không có câu “trusted setup luôn xấu” hoặc “transparent luôn tốt”. Phải so threat model và operational lifecycle.

## 12. Succinct proof: verifier rẻ nhưng prover thường đắt

Một mục tiêu của verifiable computation là:

```text
computation C(x) = y
→ prover chạy computation + tạo proof π
→ verifier kiểm tra (x,y,π)
```

Verification có thể nhỏ hơn nhiều so với chạy lại `C`.

Nhưng prover phải encode computation thành constraint system/circuit/trace và tạo proof. Prover cost có thể lớn hơn native computation đáng kể.

Do đó “verification rẻ” không đồng nghĩa “system tổng thể rẻ”. Cần cost model:

```text
prover CPU/GPU/memory
proof generation latency
proof size
network/storage
verifier cost
setup/key lifecycle
```

## 13. Arithmetic circuit và constraint representation

Proof system không hiểu source code như developer. Computation thường được hạ xuống representation toán học: arithmetic circuit, rank-1 constraint system, polynomial relation hoặc execution trace tùy family.

Compiler/prover pipeline:

```text
program / relation
→ circuit/constraints/trace
→ witness assignment
→ polynomial/commitment machinery
→ proof
```

Một operation rẻ trên CPU chưa chắc rẻ trong circuit. Bitwise operation, range check, hash function hoặc memory access có cost profile khác tùy proof system.

Đây là abstraction boundary quan trọng khi thiết kế ZK application.

## 14. SNARK là family property, không phải một algorithm duy nhất

**SNARK** thường mở rộng thành *Succinct Non-interactive Argument of Knowledge*. Các construction khác nhau có assumption, setup, proof size và prover/verifier cost khác nhau.

Từ **argument** thường ngụ ý soundness chống prover computationally bounded thay vì information-theoretic prover vô hạn.

Không nên nói “SNARK dùng elliptic curve” như universal truth; nhiều construction dùng primitive khác nhau. Hãy đọc theo property contract, không theo brand name.

## 15. STARK intuition

**STARK** thường nhấn mạnh scalable transparent argument of knowledge, dùng hash/polynomial commitment techniques thay vì trusted setup kiểu một số SNARK cổ điển và hướng tới post-quantum-friendly assumptions ở primitive nhất định.

Trade-off thường khác về proof size, prover cost và implementation complexity.

Điểm cần giữ: SNARK/STARK label không đủ để chọn system. Phải so:

```text
statement/circuit shape
prover resources
verification budget
proof size/network
setup trust
cryptographic assumptions
recursion needs
implementation maturity
```

## 16. Soundness error và amplification

Nhiều probabilistic proof có non-zero soundness error. Repetition hoặc larger challenge field có thể giảm error, nhưng cost tăng.

Security parameter phải được chọn theo threat model và số proof toàn hệ thống, không chỉ một lần verify.

Nếu một proof có failure probability cực nhỏ mỗi instance nhưng system verify hàng tỷ instance, aggregate risk vẫn cần reasoning.

## 17. Public verifiability vs designated verifier

Một proof có thể được bất kỳ ai verify bằng public data hoặc chỉ verifier có secret mới verify.

Public verifiability hữu ích cho audit, blockchain hoặc artifact provenance, nhưng transcript dễ được lưu/chia sẻ hơn. Designated-verifier protocol có privacy/trust property khác.

Requirement “ai cần verify?” phải được xác định trước khi chọn proof primitive.

## 18. Recursive proofs và aggregation

Một proof system có thể chứng minh statement “proof khác đã verify đúng”. Từ đó có recursion/aggregation:

```text
proof_1 + proof_2 + ...
→ aggregate/recursive proof
→ verifier check compact result
```

Use case gồm rollup, long computation folding hoặc proof chain. Nhưng recursion đòi proof-friendly verification circuit và tạo complexity mới về state/public input.

Aggregation không tự động bảo đảm data availability. Có thể chứng minh state transition hợp lệ nhưng user vẫn không có data cần để reconstruct state.

## 19. Verifiable computation không thay thế availability và authorization

Proof trả lời câu “computation/result có thỏa relation không?”. Nó không tự động trả lời:

- input có được authorized không;
- data có sẵn để user dùng không;
- timestamp/order có đúng business semantics không;
- external oracle có nói thật không;
- endpoint tạo witness có bị compromise không.

Proof system chỉ bảo vệ invariant được encode vào statement.

```text
what is not constrained
is not proven
```

Đây là rule quan trọng nhất khi review ZK/verifiable design.

## 20. Zero-knowledge và privacy metadata

Ngay cả khi proof body zero-knowledge, metadata vẫn có thể leak:

- ai gửi proof;
- thời điểm;
- proof frequency;
- public input;
- network path;
- transaction graph;
- proof size nếu variable.

Privacy phải reasoning end-to-end, không dừng ở cryptographic primitive.

## 21. Trusted setup lifecycle và ceremony

Nếu scheme cần setup, operational questions gồm:

```text
ai tham gia setup?
bao nhiêu participant cần honest?
transcript có public audit không?
toxic waste có thể bị recover không?
parameter có circuit-specific hay universal/updatable?
rotation/migration diễn ra thế nào?
```

Multi-party ceremony có thể giảm trust bằng assumption “ít nhất một participant xóa secret contribution đúng cách”, nhưng implementation/ceremony evidence vẫn quan trọng.

## 22. Side channel ở prover/verifier implementation

Mathematical zero-knowledge không bảo đảm implementation không leak witness qua timing, memory access, logs hoặc crash dump.

Nếu witness là secret key, prover code vẫn là security-critical code. Constant-time primitive, secret memory handling và telemetry redaction có thể cần thiết.

Cross-link:

- [Security boundaries, attack chains và exploitability](../../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md)
- [Secret, KMS, HSM, rotation và envelope encryption](../../07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md)

## 23. Example: outsourced database query

Giả sử client gửi query cho untrusted worker và nhận result aggregate. Client muốn biết worker đã chạy đúng trên committed dataset.

Một verifiable design cần bind:

```text
dataset commitment/version
query semantics
execution relation
result
proof
```

Nếu proof chỉ chứng minh “result là sum của witness rows” nhưng không bind witness rows vào canonical dataset version, worker có thể chọn dataset khác mà vẫn tạo proof hợp lệ.

Invariant phải encode **data provenance**, không chỉ arithmetic correctness.

## 24. Example: private membership proof

User muốn chứng minh mình thuộc một allowlist mà không reveal identity cụ thể.

Possible relation:

```text
public: Merkle root R
private witness: leaf + authentication path
statement: witness opens to a member under R
```

Zero-knowledge proof có thể che leaf/path trong construction phù hợp.

Nhưng nếu root cũ vẫn được accept sau revocation, user đã bị remove vẫn có thể chứng minh membership theo stale state. Vì vậy freshness/version/epoch phải nằm trong public statement hoặc protocol context.

Cryptographic correctness không thay thế lifecycle correctness.

## 25. Proof generation dưới pressure

Production prover có thể là heavy compute service. Khi traffic tăng:

```text
proof jobs
→ queue
→ memory/accelerator pressure
→ longer proving latency
→ retries/timeouts
→ overload
```

Proof system vì vậy cũng cần capacity planning, batching, admission control và failure recovery như software system khác.

Cross-link: [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 26. Evidence và observability

Production evidence nên gồm:

```text
circuit/relation version
public input hash/version
proving key / verification key version
proof generation latency
prover memory/accelerator utilization
proof size
verification latency
verification failure reason
soundness/security parameter configuration
setup/ceremony provenance
```

Không log private witness chỉ để debug. Nếu cần reproduce, dùng synthetic fixture hoặc encrypted controlled capture với policy phù hợp.

## 27. Những nhầm lẫn thường gặp

**“Zero-knowledge nghĩa không gửi dữ liệu.”** Sai; property là không leak knowledge ngoài statement theo definition.

**“Proof đúng nghĩa input business hợp lệ.”** Chỉ nếu authorization/provenance/freshness đã được encode.

**“SNARK luôn cần trusted setup.”** Không phải mọi construction.

**“STARK luôn tốt hơn SNARK.”** Không; trade-off khác nhau.

**“Verifier rẻ nghĩa prover cũng rẻ.”** Thường sai.

**“Blockchain cần ZK thì ZK chỉ dùng cho blockchain.”** Sai; verifiable computation, privacy-preserving identity và outsourced computation đều là use case rộng hơn.

**“Cryptographic proof thay thế monitoring.”** Không. Implementation, key lifecycle, queueing và version mismatch vẫn cần evidence.

## 28. Connection map

```text
Complexity theory
→ certificate / verifier / interaction

Randomness
→ unpredictable challenge / soundness

Commitment
→ bind before challenge

Zero-knowledge
→ truth without extra witness leakage

Polynomial/circuit representation
→ encode computation as constraints

Cryptography
→ computational binding/hiding/soundness assumptions

Distributed systems
→ state/version/data availability remain separate invariants

Software systems
→ prover capacity, queueing, rollout and observability
```

## 29. Checklist reasoning

```text
Statement chính xác đang được chứng minh là gì?
Public input và private witness là gì?
Completeness/soundness contract nào được dùng?
Soundness statistical hay computational?
Verifier học gì ngoài truth của statement?
Challenge/randomness đến từ đâu?
Setup/key/parameter lifecycle thế nào?
Computation được encode thành circuit/trace ra sao?
Prover cost, proof size và verifier cost bao nhiêu?
Freshness, authorization, provenance và data availability có nằm ngoài proof không?
Metadata/implementation có leak witness không?
Evidence nào cho phép audit version và verification failure?
```

## Kết luận

Interactive proofs thay đổi cách ta nghĩ về verification: verifier không nhất thiết phải tự làm toàn bộ work để có confidence mạnh về một claim. Zero-knowledge thêm privacy contract; succinct/verifiable computation thêm mục tiêu giảm verification cost.

Mental model cần giữ:

```text
claim
→ relation/invariant
→ witness
→ commitment/challenge/proof mechanism
→ completeness + soundness
→ optional zero-knowledge
→ verification
```

Proof system chỉ mạnh bằng statement được encode, assumptions được giữ và implementation/lifecycle xung quanh nó. Khi ba phần đó được tách rõ, các thuật ngữ ZK, SNARK, STARK hay verifiable computation trở thành những engineering trade-off có thể reasoning thay vì một danh sách công nghệ bí ẩn.