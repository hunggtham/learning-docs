# Độ phức tạp (complexity / 복잡도) classes beyond P/NP: co-NP, PSPACE, EXP và randomized classes

> **Mạch đọc:** Đặt **độ phức tạp (complexity / 복잡도) classes beyond P/NP: co-NP, PSPACE, EXP và randomized classes** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. độ phức tạp (complexity / 복잡도) là asymptotic tài nguyên (resource / 자원) của bài toán (problem / 문제) family** sang **2. P: giải được bằng polynomial thời gian (time / 시간) trên deterministic machine**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi nói một bài toán “khó”, ta cần hỏi **khó theo tài nguyên (resource / 자원) nào** và **đầu vào (input / 입력) tăng thì tài nguyên (resource / 자원) tăng theo hàm nào**. Một bài toán có thể cần rất nhiều thời gian (time / 시간) nhưng ít bộ nhớ (memory / 메모리); một bài khác có thể giải nhanh nếu chấp nhận xác suất lỗi rất nhỏ; một bài toán (problem / 문제) có certificate kiểm tra nhanh nhưng chưa biết cách tìm solution nhanh.

**độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론)** tổ chức các quyết định (decision / 결정) problems thành lớp (class / 클래스) dựa trên tài nguyên (resource / 자원) bound và computational mô hình (model / 모델).

Mô hình tư duy (mental model / 사고 모델):

```text
problem family
→ input size n
→ computational model
→ resource bound: time / space / randomness / interaction
→ complexity class
→ reductions / completeness
→ consequence nếu class collapse hoặc tách nhau
```

Chapter này mở rộng từ P/NP sang co-NP, PSPACE, EXP và randomized classes, nhưng mục tiêu không phải thuộc sơ đồ lớp (class / 클래스). Mục tiêu là biết mỗi lớp (class / 클래스) đang nói gì về **bằng chứng (evidence / 증거), tìm kiếm (search / 검색), tài nguyên (resource / 자원) và bất định (uncertainty / 불확실성)**.

## 1. độ phức tạp (complexity / 복잡도) là asymptotic tài nguyên (resource / 자원) của bài toán (problem / 문제) family

Một instance cụ thể có thể chạy nhanh hoặc chậm vì hiện thực (implementation / 구현)/hardware. độ phức tạp (complexity / 복잡도) lớp (class / 클래스) nói về family khi đầu vào (input / 입력) kích thước (size / 크기) tăng.

Quyết định (decision / 결정) bài toán (problem / 문제) được dùng vì đầu ra (output / 출력) chỉ `yes/no`, giúp định nghĩa lớp (class / 클래스) sạch. tối ưu hóa (optimization / 최적화)/tìm kiếm (search / 검색) bài toán (problem / 문제) thường có thể liên hệ với quyết định (decision / 결정) phiên bản (version / 버전) nhưng không phải lúc nào hiện thực (implementation / 구현) chi phí (cost / 비용) giống nhau.

Ví dụ SAT quyết định (decision / 결정) hỏi:

```text
Có assignment nào làm formula đúng không?
```

khác với tác vụ (task / 작업) tìm assignment cụ thể hoặc tối ưu một mục tiêu (objective / 목표).

## 2. P: giải được bằng polynomial thời gian (time / 시간) trên deterministic machine

`P` chứa quyết định (decision / 결정) problems có thuật toán (algorithm / 알고리즘) deterministic chạy polynomial theo đầu vào (input / 입력) kích thước (size / 크기):

```text
O(n^k)
```

cho một constant `k` nào đó.

Polynomial không đồng nghĩa “nhanh trong thực tế”. `n^100` là polynomial nhưng vô dụng cho đầu vào (input / 입력) lớn. Ngược lại exponential thuật toán (algorithm / 알고리즘) có thể đủ nhanh khi parameter nhỏ.

Ý nghĩa lý thuyết của P là một ranh giới (boundary / 경계) robust cho efficient computation dưới nhiều reasonable machine các mô hình (models / 모델들), không phải SLA môi trường vận hành (production / 운영 환경).

## 3. NP: yes-instance có certificate kiểm tra polynomial

Một definition hữu ích của `NP`:

```text
x ∈ L
iff
exists certificate w of polynomial length
such that verifier V(x,w) accepts in polynomial time
```

SAT: certificate là assignment. Hamiltonian cycle: certificate là chuỗi (sequence / 시퀀스) vertex. Verifier kiểm tra nhanh solution được đưa sẵn.

NP không có nghĩa “non-polynomial”. Nó là **nondeterministic polynomial thời gian (time / 시간)** hoặc tương đương certificate-verification view.

Mọi bài toán (problem / 문제) trong P cũng thuộc NP vì nếu tự giải nhanh được thì xác minh (verification / 확인) không khó hơn.

Câu hỏi nổi tiếng `P = NP?` vẫn chưa được giải quyết. Không được viết tài liệu như thể `P ≠ NP` đã là theorem.

## 4. co-NP: certificate cho phía “no” theo complement

Với ngôn ngữ (language / 언어) `L`, complement `L̄` chứa các đầu vào (input / 입력) không thuộc `L`. `co-NP` là lớp (class / 클래스) các bài toán (problem / 문제) mà complement thuộc NP.

Trực giác:

```text
NP     → yes có witness kiểm tra nhanh
co-NP  → no có witness kiểm tra nhanh cho problem gốc
```

Ví dụ TAUT hỏi formula Boolean có đúng với mọi assignment không. Complement là “tồn tại assignment làm formula sai”, có witness kiểm tra nhanh, nên TAUT thuộc co-NP.

Không biết liệu `NP = co-NP` hay không. Nếu một NP-complete bài toán (problem / 문제) cũng được chứng minh nằm trong co-NP theo cách dẫn tới equality phù hợp, hậu quả độ phức tạp (complexity / 복잡도) rất lớn.

## 5. Certificate view giúp phân biệt tìm kiếm (search / 검색) và proof

Trong kỹ thuật (engineering / 엔지니어링), ta thường gặp asymmetric công việc (work / 작업):

```text
finding solution may be expensive
checking proposed solution may be cheap
```

Ràng buộc (constraint / 제약조건) solver có thể mất lâu để tìm schedule, nhưng verifier độc lập kiểm tra schedule hợp lệ nhanh. trình biên dịch (compiler / 컴파일러) optimizer có thể tìm kiếm (search / 검색) plan khó, nhưng checker có thể xác nhận một số bất biến (invariant / 불변식) của kết quả (result / 결과).

Độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) formalize một phần trực giác này, nhưng không nên suy ra mọi “dễ verify, khó find” đều là NP-complete.

## 6. Reduction là ngôn ngữ so sánh độ khó

Polynomial-time reduction từ `A` sang `B` nghĩa là nếu có solver hiệu quả cho `B`, ta có thể dùng nó giải `A` với overhead polynomial.

```text
A ≤p B
```

Nếu mọi bài toán (problem / 문제) trong lớp (class / 클래스) `C` reduce tới `B`, `B` là `C-hard`. Nếu thêm `B ∈ C`, nó là `C-complete`.

Complete bài toán (problem / 문제) là đại diện cho difficulty của lớp (class / 클래스) dưới reduction notion đã chọn.

Reduction direction rất dễ nhầm. Để chứng minh `B` khó, reduce **bài toán (problem / 문제) đã biết khó A vào B**, không làm ngược lại.

## 7. NP-completeness không nói instance nào cũng khó

Một NP-complete bài toán (problem / 문제) có thể có nhiều instance dễ. SAT solver hiện đại giải rất nhiều formula lớn nhờ cấu trúc (structure / 구조), heuristics, clause học tập (learning / 학습) và preprocessing.

Worst-case hardness không phủ nhận practical success.

Ngược lại benchmark dễ không phủ nhận worst-case hardness. Cần phân biệt:

```text
worst-case complexity
average-case under distribution
parameterized structure
real workload distribution
```

Bảo mật (security / 보안) còn quan tâm average-case/hard-on-distribution nhiều hơn worst-case đơn thuần, vì attacker gặp key/instance được sinh theo phân phối (distribution / 분포) cụ thể.

## 8. không gian (space / 공간) là tài nguyên (resource / 자원) khác thời gian (time / 시간)

`PSPACE` chứa quyết định (decision / 결정) problems giải được bằng polynomial **không gian (space / 공간)**, không giới hạn polynomial thời gian (time / 시간).

Một machine dùng polynomial bộ nhớ (memory / 메모리) có thể chạy rất lâu, thậm chí exponential thời gian (time / 시간), miễn workspace không vượt polynomial bound.

Ta có containment cơ bản:

```text
P ⊆ NP ⊆ PSPACE ⊆ EXP
```

Một số inclusion có thể strict nhưng không phải tất cả separation đã được chứng minh.

Không gian (space / 공간) có thể reuse. Một depth-first tìm kiếm (search / 검색) trên trạng thái (state / 상태) không gian (space / 공간) khổng lồ có thể cần ít bộ nhớ (memory / 메모리) hơn breadth-first traversal dù thời gian (time / 시간) rất lớn.

## 9. PSPACE và game/planning có alternating choices

Nhiều game hoặc planning bài toán (problem / 문제) có chuỗi lựa chọn “ta chọn, đối thủ chọn, ta chọn...” và horizon polynomial nhưng trạng thái (state / 상태) cây (tree / 트리) exponential.

Quantified Boolean Formula (QBF) là chuẩn gốc (canonical / 정본) PSPACE-complete bài toán (problem / 문제):

```text
∃x ∀y ∃z ... φ(x,y,z,...)
```

Khác SAT chỉ có existential assignment, QBF xen kẽ existential/universal choice. Evaluation cần lập luận (reasoning / 추론) qua game cây (tree / 트리) của quantifier.

Liên kết (connection / 연결) này dẫn tự nhiên tới interactive proof và alternating computation.

## 10. EXP: exponential thời gian (time / 시간) nhưng vẫn có cấu trúc tài nguyên (resource / 자원) bound

`EXP` thường chỉ problems giải deterministic trong thời gian (time / 시간) `2^{poly(n)}`.

Exponential không đồng nghĩa undecidable. Một bài toán (problem / 문제) có thể decidable nhưng cần tài nguyên (resource / 자원) cực lớn theo worst trường hợp (case / 사례).

Đây là distinction quan trọng:

```text
undecidable
→ không có algorithm tổng quát luôn quyết định

intractable under known complexity
→ có algorithm, nhưng resource growth rất lớn
```

Đọc lại [Formal models, reductions và computability](./00_formal_models_reductions_and_computability.md).

## 11. không gian (space / 공간) hierarchy và thời gian (time / 시간) hierarchy: thêm tài nguyên (resource / 자원) thật sự tăng power

Hierarchy theorems cho thấy dưới điều kiện phù hợp, cho machine nhiều thời gian (time / 시간)/không gian (space / 공간) asymptotically hơn thực sự cho phép giải thêm bài toán (problem / 문제).

Điều này quan trọng vì không phải mọi complexity-class separation đều bí ẩn. Một số separation như giữa các bound đủ cách nhau đã được chứng minh; các câu hỏi khó như P vs NP nằm ở ranh giới (boundary / 경계) tinh tế hơn.

Mô hình tư duy (mental model / 사고 모델):

```text
more allowed resource
can increase computable decision power
```

nhưng chính xác (exact / 정확한) ranh giới (boundary / 경계) phụ thuộc lớp (class / 클래스)/mô hình (model / 모델).

## 12. Randomized algorithms thêm random bits như tài nguyên (resource / 자원)

Randomized độ phức tạp (complexity / 복잡도) lớp (class / 클래스) cho thuật toán (algorithm / 알고리즘) được dùng random choices.

Một số lớp (class / 클래스) quan trọng:

### RP

Nếu answer là `no`, thuật toán (algorithm / 알고리즘) luôn reject đúng. Nếu answer là `yes`, thuật toán (algorithm / 알고리즘) accept với xác suất (probability / 확률) đủ lớn, thường ít nhất một constant như `1/2`.

Đây là **one-sided lỗi (error / 오류)**.

### co-RP

Đối xứng phía còn lại: yes-side luôn đúng, no-side có bounded xác suất (probability / 확률) lỗi (error / 오류) theo convention tương ứng.

### BPP

**Bounded-error probabilistic polynomial thời gian (time / 시간)** cho phép lỗi (error / 오류) hai phía nhưng xác suất (probability / 확률) bị chặn dưới một constant nhỏ hơn `1/2`, ví dụ `1/3`.

Quan trọng là lỗi (error / 오류) có thể giảm bằng independent repetition/majority nếu random trials phù hợp:

```text
constant error
→ repeat
→ aggregate
→ exponentially smaller error
```

với polynomial overhead cho mức confidence hợp lý.

### ZPP

Zero-error probabilistic polynomial expected thời gian (time / 시간) có thể nhìn như thuật toán (algorithm / 알고리즘) không trả answer sai nhưng thời gian chạy (runtime / 런타임) là random variable với expected polynomial bound.

## 13. Monte Carlo và Las Vegas

Trong thuật toán (algorithm / 알고리즘) kỹ thuật (engineering / 엔지니어링), terminology thường dùng:

**Monte Carlo**: thời gian chạy (runtime / 런타임) bounded nhưng có xác suất answer sai.

**Las Vegas**: answer luôn đúng nhưng thời gian chạy (runtime / 런타임) random.

Không phải mọi textbook map terminology hoàn toàn một-một với độ phức tạp (complexity / 복잡도) lớp (class / 클래스), nhưng distinction về **lỗi (error / 오류) vs thời gian chạy (runtime / 런타임) bất định (uncertainty / 불확실성)** rất hữu ích.

Ví dụ randomized quicksort luôn sort đúng nhưng thời gian chạy (runtime / 런타임) phụ thuộc random pivot; đây là Las Vegas-style lập luận (reasoning / 추론) về hiệu năng (performance / 성능).

## 14. Amplification không sửa systematic độ lệch (bias / 편향)

Lặp randomized thuật toán (algorithm / 알고리즘) chỉ giảm lỗi (error / 오류) nếu trial cung cấp independence/điều kiện (condition / 조건) phù hợp.

Nếu RNG bị correlated hoặc thuật toán (algorithm / 알고리즘) có deterministic blind spot, repeat cùng dạng thất bại (failure mode / 실패 모드) không giúp.

```text
independent random error
→ repetition helps

systematic model error
→ repetition may repeat the same mistake
```

Đây là cầu nối (bridge / 브리지) tới [Randomness, entropy sources và computational unpredictability](./05_randomness_entropy_sources_and_computational_unpredictability.md).

## 15. Pseudorandomness và derandomization

Nếu random bits có thể được thay bằng pseudorandom generator phù hợp mà thuật toán (algorithm / 알고리즘) không phân biệt hiệu quả, một randomized thuật toán (algorithm / 알고리즘) có thể được mô phỏng deterministic trong một số setting.

**Derandomization** nghiên cứu khi randomness thực sự tăng computational power hay chỉ giúp thiết kế thuật toán (algorithm / 알고리즘) đơn giản/nhanh hơn.

Quan hệ chính xác giữa BPP và P là chủ đề sâu; không nên tuyên bố equality chưa chứng minh như fact. Tuy nhiên nhiều kết quả cho thấy randomness và hardness giả định (assumption / 가정) có liên kết (connection / 연결) chặt.

## 16. Pseudo-polynomial thời gian (time / 시간): nhìn đầu vào (input / 입력) encoding

Một thuật toán (algorithm / 알고리즘) chạy `O(nW)` có thể trông polynomial nếu `W` là numeric giá trị (value / 값). Nhưng nếu `W` được encode nhị phân (binary / 이진), đầu vào (input / 입력) chỉ cần `log W` bits.

Do đó `O(W)` có thể exponential theo **đầu vào (input / 입력) length**.

Knapsack động (dynamic / 동적) programming theo sức chứa (capacity / 용량) là ví dụ kinh điển pseudo-polynomial.

Độ phức tạp (complexity / 복잡도) luôn đo theo kích thước (size / 크기) của biểu diễn (representation / 표현), không theo magnitude được viết ra nếu hai thứ khác nhau.

## 17. Strong vs weak NP-hardness

Pseudo-polynomial thuật toán (algorithm / 알고리즘) dẫn tới distinction giữa weakly và strongly NP-hard trong tối ưu hóa (optimization / 최적화) problems số học.

Weakly NP-hard bài toán (problem / 문제) có thể trở nên tractable khi numeric parameters nhỏ/bounded, trong khi strong NP-hardness vẫn tồn tại ngay khi numeric values bị giới hạn polynomial phù hợp.

Đây là lý do “NP-hard” chưa đủ để chọn hiện thực (implementation / 구현); parameter phân phối (distribution / 분포) thực tế có thể làm động (dynamic / 동적) programming rất hiệu quả.

## 18. Parameterized độ phức tạp (complexity / 복잡도): hỏi exponential theo cái gì

Một bài toán (problem / 문제) có thể khó theo tổng đầu vào (input / 입력) `n` nhưng dễ nếu một parameter `k` nhỏ:

```text
T(n,k) = f(k) × poly(n)
```

Đây là **fixed-parameter tractable (FPT)** form.

Ví dụ môi trường vận hành (production / 운영 환경) có đồ thị (graph / 그래프) rất lớn nhưng treewidth, solution kích thước (size / 크기) hoặc number of exceptional các ràng buộc (constraints / 제약조건들) nhỏ. Parameterized viewpoint có thể cho thuật toán (algorithm / 알고리즘) practical dù general bài toán (problem / 문제) khó.

Mô hình tư duy (mental model / 사고 모델):

```text
“exponential” chưa đủ
→ exponential theo n hay theo một parameter nhỏ?
```

## 19. Approximation và hardness of approximation

Nếu chính xác (exact / 정확한) tối ưu hóa (optimization / 최적화) quá khó, ta có thể chấp nhận solution gần optimum với approximation ratio được chứng minh.

Nhưng không phải mọi NP-hard bài toán (problem / 문제) có approximation tốt. độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) còn nghiên cứu giới hạn approximation dưới giả định (assumption / 가정) nhất định.

Kỹ thuật (engineering / 엔지니어링) quyết định (decision / 결정) vì vậy có ba tầng:

```text
exact algorithm
approximation with guarantee
heuristic without worst-case guarantee
```

Heuristic có thể rất tốt thực tế nhưng bằng chứng (evidence / 증거) khác proof guarantee.

Cross-link DSA: [Hard problems, reductions và approximation](../../01_algorithms_data_structures/advanced/04_algorithmic_paradigms/09_hard_problems_reductions_and_approximation.md).

## 20. độ phức tạp (complexity / 복잡도) lớp (class / 클래스) không phải hiệu năng (performance / 성능) benchmark

Hai thuật toán (algorithm / 알고리즘) cùng `O(n log n)` có constant, bộ nhớ đệm (cache / 캐시) locality, vectorization và parallelism khác nhau. Một polynomial thuật toán (algorithm / 알고리즘) có thể chậm hơn exponential thuật toán (algorithm / 알고리즘) trên đầu vào (input / 입력) nhỏ.

Độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) bỏ nhiều chi tiết microarchitecture để tập trung scaling law. môi trường vận hành (production / 운영 환경) hiệu năng (performance / 성능) phải nối thêm:

```text
asymptotic work
→ memory access
→ cache/NUMA
→ parallelism
→ I/O/network
→ queueing
→ latency/cost
```

Do đó lớp (class / 클래스) là upper-level feasibility lập luận (reasoning / 추론), không thay benchmark.

## 21. độ phức tạp (complexity / 복잡도) và cryptography

Cryptography không chỉ cần “bài toán (problem / 문제) worst-case khó”. Nó cần attacker khó giải instance được sinh theo phân phối (distribution / 분포) cụ thể, với tài nguyên (resource / 자원)/threat mô hình (model / 모델) cụ thể.

Một NP-complete bài toán (problem / 문제) không tự động là thành phần nguyên thủy (primitive / 기본 요소) cryptographic tốt. Nếu random instances hầu hết dễ, worst-case hardness không bảo vệ key.

Bảo mật (security / 보안) thường dựa trên stronger average-case/computational các giả định (assumptions / 가정들) và concrete parameter sizes.

## 22. độ phức tạp (complexity / 복잡도) và proof các hệ thống (systems / 시스템들)

NP có certificate một chiều: prover đưa witness, verifier check. Nếu cho verifier tương tác nhiều vòng với prover và dùng randomness, lớp (class / 클래스) các statement có thể verify hiệu quả mở rộng đáng kể.

Đây là motivation cho [Interactive proofs, zero-knowledge và verifiable computation](./07_interactive_proofs_zero_knowledge_and_verifiable_computation.md).

## 23. Những nhầm lẫn thường gặp

**“NP là non-polynomial.”** Sai.

**“NP-complete nghĩa mọi instance đều chậm.”** Sai; đây là worst-case lớp (class / 클래스) statement.

**“P là nhanh.”** Không nhất thiết trong practical constants/đầu vào (input / 입력) sizes.

**“Exponential nghĩa undecidable.”** Sai; EXP vẫn là decidable resource-bounded lớp (class / 클래스).

**“Randomized thuật toán (algorithm / 알고리즘) không đáng tin.”** Bounded lỗi (error / 오류) có thể được quantify/amplify; độ tin cậy (reliability / 신뢰성) đặc tả hợp đồng (contract / 계약) phải nói rõ xác suất.

**“P ≠ NP đã được chứng minh.”** Chưa.

**“NP-hard bài toán (problem / 문제) không thể giải thực tế.”** Không; cấu trúc (structure / 구조), parameter, approximation và heuristic có thể làm tải công việc (workload / 워크로드) cụ thể tractable.

## 24. lớp (class / 클래스) map để lập luận (reasoning / 추론)

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

Randomized classes tạo trục khác về lỗi (error / 오류)/randomness. Không nên ép chúng vào một line duy nhất nếu chưa nói rõ known containment và giả định (assumption / 가정).

## 25. Checklist lập luận (reasoning / 추론)

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

Độ phức tạp (complexity / 복잡도) classes là bản đồ của **resource-bounded computation**, không phải bảng xếp hạng “dễ/khó” đơn giản.

```text
P        → deterministic polynomial time
NP       → yes-witness polynomially verifiable
co-NP    → complement có NP-style witness
PSPACE   → polynomial workspace
EXP      → exponential-time decidable computation
RP/BPP/ZPP → polynomial computation với các contract khác nhau về randomness/error
```

Giá trị thực tế nằm ở việc biết một bài toán (problem / 문제) đang khó vì tìm kiếm (search / 검색) không gian (space / 공간), bộ nhớ (memory / 메모리), bất định (uncertainty / 불확실성) hay biểu diễn (representation / 표현); biết theorem nào thật sự tồn tại; và biết khi nào cần chuyển từ chính xác (exact / 정확한) solution sang parameterization, approximation, randomization hoặc domain-specific cấu trúc (structure / 구조).

> **Bàn giao:** Sau **Kết luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 formal models reductions and computability](./00_formal_models_reductions_and_computability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
