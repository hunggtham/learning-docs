# Complexity classes beyond P/NP: co-NP, PSPACE, EXP và randomized classes

Khi nói một bài toán “khó”, ta cần hỏi **khó theo resource nào** và **input tăng thì resource tăng theo hàm nào**. Một bài toán có thể cần rất nhiều time nhưng ít memory; một bài khác có thể giải nhanh nếu chấp nhận xác suất lỗi rất nhỏ; một problem có certificate kiểm tra nhanh nhưng chưa biết cách tìm solution nhanh.

**Complexity theory (lý thuyết độ phức tạp / 계산 복잡도 이론)** tổ chức các decision problems thành class dựa trên resource bound và computational model.

Mental model:

```text
problem family
→ input size n
→ computational model
→ resource bound: time / space / randomness / interaction
→ complexity class
→ reductions / completeness
→ consequence nếu class collapse hoặc tách nhau
```

Chapter này mở rộng từ P/NP sang co-NP, PSPACE, EXP và randomized classes, nhưng mục tiêu không phải thuộc sơ đồ class. Mục tiêu là biết mỗi class đang nói gì về **evidence, search, resource và uncertainty**.

## 1. Complexity là asymptotic resource của problem family

Một instance cụ thể có thể chạy nhanh hoặc chậm vì implementation/hardware. Complexity class nói về family khi input size tăng.

Decision problem được dùng vì output chỉ `yes/no`, giúp định nghĩa class sạch. Optimization/search problem thường có thể liên hệ với decision version nhưng không phải lúc nào implementation cost giống nhau.

Ví dụ SAT decision hỏi:

```text
Có assignment nào làm formula đúng không?
```

khác với task tìm assignment cụ thể hoặc tối ưu một objective.

## 2. P: giải được bằng polynomial time trên deterministic machine

`P` chứa decision problems có algorithm deterministic chạy polynomial theo input size:

```text
O(n^k)
```

cho một constant `k` nào đó.

Polynomial không đồng nghĩa “nhanh trong thực tế”. `n^100` là polynomial nhưng vô dụng cho input lớn. Ngược lại exponential algorithm có thể đủ nhanh khi parameter nhỏ.

Ý nghĩa lý thuyết của P là một boundary robust cho efficient computation dưới nhiều reasonable machine models, không phải SLA production.

## 3. NP: yes-instance có certificate kiểm tra polynomial

Một definition hữu ích của `NP`:

```text
x ∈ L
iff
exists certificate w of polynomial length
such that verifier V(x,w) accepts in polynomial time
```

SAT: certificate là assignment. Hamiltonian cycle: certificate là sequence vertex. Verifier kiểm tra nhanh solution được đưa sẵn.

NP không có nghĩa “non-polynomial”. Nó là **nondeterministic polynomial time** hoặc tương đương certificate-verification view.

Mọi problem trong P cũng thuộc NP vì nếu tự giải nhanh được thì verification không khó hơn.

Câu hỏi nổi tiếng `P = NP?` vẫn chưa được giải quyết. Không được viết tài liệu như thể `P ≠ NP` đã là theorem.

## 4. co-NP: certificate cho phía “no” theo complement

Với language `L`, complement `L̄` chứa các input không thuộc `L`. `co-NP` là class các problem mà complement thuộc NP.

Trực giác:

```text
NP     → yes có witness kiểm tra nhanh
co-NP  → no có witness kiểm tra nhanh cho problem gốc
```

Ví dụ TAUT hỏi formula Boolean có đúng với mọi assignment không. Complement là “tồn tại assignment làm formula sai”, có witness kiểm tra nhanh, nên TAUT thuộc co-NP.

Không biết liệu `NP = co-NP` hay không. Nếu một NP-complete problem cũng được chứng minh nằm trong co-NP theo cách dẫn tới equality phù hợp, hậu quả complexity rất lớn.

## 5. Certificate view giúp phân biệt search và proof

Trong engineering, ta thường gặp asymmetric work:

```text
finding solution may be expensive
checking proposed solution may be cheap
```

Constraint solver có thể mất lâu để tìm schedule, nhưng verifier độc lập kiểm tra schedule hợp lệ nhanh. Compiler optimizer có thể search plan khó, nhưng checker có thể xác nhận một số invariant của result.

Complexity theory formalize một phần trực giác này, nhưng không nên suy ra mọi “dễ verify, khó find” đều là NP-complete.

## 6. Reduction là ngôn ngữ so sánh độ khó

Polynomial-time reduction từ `A` sang `B` nghĩa là nếu có solver hiệu quả cho `B`, ta có thể dùng nó giải `A` với overhead polynomial.

```text
A ≤p B
```

Nếu mọi problem trong class `C` reduce tới `B`, `B` là `C-hard`. Nếu thêm `B ∈ C`, nó là `C-complete`.

Complete problem là đại diện cho difficulty của class dưới reduction notion đã chọn.

Reduction direction rất dễ nhầm. Để chứng minh `B` khó, reduce **problem đã biết khó A vào B**, không làm ngược lại.

## 7. NP-completeness không nói instance nào cũng khó

Một NP-complete problem có thể có nhiều instance dễ. SAT solver hiện đại giải rất nhiều formula lớn nhờ structure, heuristics, clause learning và preprocessing.

Worst-case hardness không phủ nhận practical success.

Ngược lại benchmark dễ không phủ nhận worst-case hardness. Cần phân biệt:

```text
worst-case complexity
average-case under distribution
parameterized structure
real workload distribution
```

Security còn quan tâm average-case/hard-on-distribution nhiều hơn worst-case đơn thuần, vì attacker gặp key/instance được sinh theo distribution cụ thể.

## 8. Space là resource khác time

`PSPACE` chứa decision problems giải được bằng polynomial **space**, không giới hạn polynomial time.

Một machine dùng polynomial memory có thể chạy rất lâu, thậm chí exponential time, miễn workspace không vượt polynomial bound.

Ta có containment cơ bản:

```text
P ⊆ NP ⊆ PSPACE ⊆ EXP
```

Một số inclusion có thể strict nhưng không phải tất cả separation đã được chứng minh.

Space có thể reuse. Một depth-first search trên state space khổng lồ có thể cần ít memory hơn breadth-first traversal dù time rất lớn.

## 9. PSPACE và game/planning có alternating choices

Nhiều game hoặc planning problem có chuỗi lựa chọn “ta chọn, đối thủ chọn, ta chọn...” và horizon polynomial nhưng state tree exponential.

Quantified Boolean Formula (QBF) là canonical PSPACE-complete problem:

```text
∃x ∀y ∃z ... φ(x,y,z,...)
```

Khác SAT chỉ có existential assignment, QBF xen kẽ existential/universal choice. Evaluation cần reasoning qua game tree của quantifier.

Connection này dẫn tự nhiên tới interactive proof và alternating computation.

## 10. EXP: exponential time nhưng vẫn có cấu trúc resource bound

`EXP` thường chỉ problems giải deterministic trong time `2^{poly(n)}`.

Exponential không đồng nghĩa undecidable. Một problem có thể decidable nhưng cần resource cực lớn theo worst case.

Đây là distinction quan trọng:

```text
undecidable
→ không có algorithm tổng quát luôn quyết định

intractable under known complexity
→ có algorithm, nhưng resource growth rất lớn
```

Đọc lại [Formal models, reductions và computability](./00_formal_models_reductions_and_computability.md).

## 11. Space hierarchy và time hierarchy: thêm resource thật sự tăng power

Hierarchy theorems cho thấy dưới điều kiện phù hợp, cho machine nhiều time/space asymptotically hơn thực sự cho phép giải thêm problem.

Điều này quan trọng vì không phải mọi complexity-class separation đều bí ẩn. Một số separation như giữa các bound đủ cách nhau đã được chứng minh; các câu hỏi khó như P vs NP nằm ở boundary tinh tế hơn.

Mental model:

```text
more allowed resource
can increase computable decision power
```

nhưng exact boundary phụ thuộc class/model.

## 12. Randomized algorithms thêm random bits như resource

Randomized complexity class cho algorithm được dùng random choices.

Một số class quan trọng:

### RP

Nếu answer là `no`, algorithm luôn reject đúng. Nếu answer là `yes`, algorithm accept với probability đủ lớn, thường ít nhất một constant như `1/2`.

Đây là **one-sided error**.

### co-RP

Đối xứng phía còn lại: yes-side luôn đúng, no-side có bounded probability error theo convention tương ứng.

### BPP

**Bounded-error probabilistic polynomial time** cho phép error hai phía nhưng probability bị chặn dưới một constant nhỏ hơn `1/2`, ví dụ `1/3`.

Quan trọng là error có thể giảm bằng independent repetition/majority nếu random trials phù hợp:

```text
constant error
→ repeat
→ aggregate
→ exponentially smaller error
```

với polynomial overhead cho mức confidence hợp lý.

### ZPP

Zero-error probabilistic polynomial expected time có thể nhìn như algorithm không trả answer sai nhưng runtime là random variable với expected polynomial bound.

## 13. Monte Carlo và Las Vegas

Trong algorithm engineering, terminology thường dùng:

**Monte Carlo**: runtime bounded nhưng có xác suất answer sai.

**Las Vegas**: answer luôn đúng nhưng runtime random.

Không phải mọi textbook map terminology hoàn toàn một-một với complexity class, nhưng distinction về **error vs runtime uncertainty** rất hữu ích.

Ví dụ randomized quicksort luôn sort đúng nhưng runtime phụ thuộc random pivot; đây là Las Vegas-style reasoning về performance.

## 14. Amplification không sửa systematic bias

Lặp randomized algorithm chỉ giảm error nếu trial cung cấp independence/condition phù hợp.

Nếu RNG bị correlated hoặc algorithm có deterministic blind spot, repeat cùng failure mode không giúp.

```text
independent random error
→ repetition helps

systematic model error
→ repetition may repeat the same mistake
```

Đây là bridge tới [Randomness, entropy sources và computational unpredictability](./05_randomness_entropy_sources_and_computational_unpredictability.md).

## 15. Pseudorandomness và derandomization

Nếu random bits có thể được thay bằng pseudorandom generator phù hợp mà algorithm không phân biệt hiệu quả, một randomized algorithm có thể được mô phỏng deterministic trong một số setting.

**Derandomization** nghiên cứu khi randomness thực sự tăng computational power hay chỉ giúp thiết kế algorithm đơn giản/nhanh hơn.

Quan hệ chính xác giữa BPP và P là chủ đề sâu; không nên tuyên bố equality chưa chứng minh như fact. Tuy nhiên nhiều kết quả cho thấy randomness và hardness assumption có connection chặt.

## 16. Pseudo-polynomial time: nhìn input encoding

Một algorithm chạy `O(nW)` có thể trông polynomial nếu `W` là numeric value. Nhưng nếu `W` được encode binary, input chỉ cần `log W` bits.

Do đó `O(W)` có thể exponential theo **input length**.

Knapsack dynamic programming theo capacity là ví dụ kinh điển pseudo-polynomial.

Complexity luôn đo theo size của representation, không theo magnitude được viết ra nếu hai thứ khác nhau.

## 17. Strong vs weak NP-hardness

Pseudo-polynomial algorithm dẫn tới distinction giữa weakly và strongly NP-hard trong optimization problems số học.

Weakly NP-hard problem có thể trở nên tractable khi numeric parameters nhỏ/bounded, trong khi strong NP-hardness vẫn tồn tại ngay khi numeric values bị giới hạn polynomial phù hợp.

Đây là lý do “NP-hard” chưa đủ để chọn implementation; parameter distribution thực tế có thể làm dynamic programming rất hiệu quả.

## 18. Parameterized complexity: hỏi exponential theo cái gì

Một problem có thể khó theo tổng input `n` nhưng dễ nếu một parameter `k` nhỏ:

```text
T(n,k) = f(k) × poly(n)
```

Đây là **fixed-parameter tractable (FPT)** form.

Ví dụ production có graph rất lớn nhưng treewidth, solution size hoặc number of exceptional constraints nhỏ. Parameterized viewpoint có thể cho algorithm practical dù general problem khó.

Mental model:

```text
“exponential” chưa đủ
→ exponential theo n hay theo một parameter nhỏ?
```

## 19. Approximation và hardness of approximation

Nếu exact optimization quá khó, ta có thể chấp nhận solution gần optimum với approximation ratio được chứng minh.

Nhưng không phải mọi NP-hard problem có approximation tốt. Complexity theory còn nghiên cứu giới hạn approximation dưới assumption nhất định.

Engineering decision vì vậy có ba tầng:

```text
exact algorithm
approximation with guarantee
heuristic without worst-case guarantee
```

Heuristic có thể rất tốt thực tế nhưng evidence khác proof guarantee.

Cross-link DSA: [Hard problems, reductions và approximation](../../01_algorithms_data_structures/advanced/04_algorithmic_paradigms/09_hard_problems_reductions_and_approximation.md).

## 20. Complexity class không phải performance benchmark

Hai algorithm cùng `O(n log n)` có constant, cache locality, vectorization và parallelism khác nhau. Một polynomial algorithm có thể chậm hơn exponential algorithm trên input nhỏ.

Complexity theory bỏ nhiều chi tiết microarchitecture để tập trung scaling law. Production performance phải nối thêm:

```text
asymptotic work
→ memory access
→ cache/NUMA
→ parallelism
→ I/O/network
→ queueing
→ latency/cost
```

Do đó class là upper-level feasibility reasoning, không thay benchmark.

## 21. Complexity và cryptography

Cryptography không chỉ cần “problem worst-case khó”. Nó cần attacker khó giải instance được sinh theo distribution cụ thể, với resource/threat model cụ thể.

Một NP-complete problem không tự động là primitive cryptographic tốt. Nếu random instances hầu hết dễ, worst-case hardness không bảo vệ key.

Security thường dựa trên stronger average-case/computational assumptions và concrete parameter sizes.

## 22. Complexity và proof systems

NP có certificate một chiều: prover đưa witness, verifier check. Nếu cho verifier tương tác nhiều vòng với prover và dùng randomness, class các statement có thể verify hiệu quả mở rộng đáng kể.

Đây là motivation cho [Interactive proofs, zero-knowledge và verifiable computation](./07_interactive_proofs_zero_knowledge_and_verifiable_computation.md).

## 23. Những nhầm lẫn thường gặp

**“NP là non-polynomial.”** Sai.

**“NP-complete nghĩa mọi instance đều chậm.”** Sai; đây là worst-case class statement.

**“P là nhanh.”** Không nhất thiết trong practical constants/input sizes.

**“Exponential nghĩa undecidable.”** Sai; EXP vẫn là decidable resource-bounded class.

**“Randomized algorithm không đáng tin.”** Bounded error có thể được quantify/amplify; reliability contract phải nói rõ xác suất.

**“P ≠ NP đã được chứng minh.”** Chưa.

**“NP-hard problem không thể giải thực tế.”** Không; structure, parameter, approximation và heuristic có thể làm workload cụ thể tractable.

## 24. Class map để reasoning

Một containment map cơ bản:

```text
P
⊆ NP
⊆ PSPACE
⊆ EXP
```

và:

```text
P ⊆ co-NP?   P chắc chắn nằm trong cả NP và co-NP
NP ?= co-NP  chưa biết
P ?= NP      chưa biết
```

Randomized classes tạo trục khác về error/randomness. Không nên ép chúng vào một line duy nhất nếu chưa nói rõ known containment và assumption.

## 25. Checklist reasoning

```text
Problem là decision, search hay optimization?
Input size được đo theo representation nào?
Resource đang giới hạn là time, space hay randomness?
Certificate/witness tồn tại cho phía yes hay no?
Reduction direction nào đang được dùng?
Statement là theorem đã chứng minh hay open problem?
Worst case có đại diện workload distribution thực tế không?
Có parameter nhỏ, approximation hoặc heuristic structure không?
Randomized error là one-sided, two-sided hay zero-error expected-time?
Production bottleneck có thực sự do asymptotic complexity hay do memory/I/O/queueing?
```

## Kết luận

Complexity classes là bản đồ của **resource-bounded computation**, không phải bảng xếp hạng “dễ/khó” đơn giản.

```text
P        → deterministic polynomial time
NP       → yes-witness polynomially verifiable
co-NP    → complement có NP-style witness
PSPACE   → polynomial workspace
EXP      → exponential-time decidable computation
RP/BPP/ZPP → polynomial computation với các contract khác nhau về randomness/error
```

Giá trị thực tế nằm ở việc biết một problem đang khó vì search space, memory, uncertainty hay representation; biết theorem nào thật sự tồn tại; và biết khi nào cần chuyển từ exact solution sang parameterization, approximation, randomization hoặc domain-specific structure.