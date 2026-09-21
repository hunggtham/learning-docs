# Computability và giới hạn của tính toán

Khi học programming, ta dễ hình thành cảm giác rằng mọi bài toán chỉ cần “đủ code và đủ CPU”. Theory of Computation (이론 전산학 / lý thuyết tính toán) cho thấy có ít nhất ba tầng khác nhau: có bài toán **không thể được giải bằng algorithm nói chung**; có bài toán computable nhưng quá đắt về resource; và có bài toán tractable nếu chọn đúng algorithm/model.

Chapter này tập trung tầng đầu: computability (계산 가능성 / khả năng tính toán) và những giới hạn mang tính nguyên lý.

## Một computation model cần những gì?

Để nói “algorithm nào cũng không giải được”, ta phải có model đủ tổng quát về computation. Turing machine là model cổ điển: một tape vô hạn về lý thuyết, head đọc/ghi symbols, finite control state và transition rules. Nó rất đơn giản nhưng có sức biểu đạt tương đương nhiều models tổng quát khác theo Church–Turing thesis.

Church–Turing thesis không phải theorem vật lý chứng minh mọi máy có thể tưởng tượng đều bị giới hạn như Turing machine. Nó là claim nền tảng rằng mọi function có thể được tính theo nghĩa effective procedure đều computable bởi Turing machine hoặc model tương đương.

Programming languages general-purpose hiện đại về lý thuyết thường Turing-complete nếu có đủ memory và control constructs. Điều đó không có nghĩa chúng giống nhau về performance, safety hay ergonomics; chỉ nói về class functions có thể biểu đạt.

## Decidable và undecidable

Một decision problem hỏi yes/no. Nếu tồn tại algorithm luôn terminate và trả lời đúng cho mọi input, problem là decidable (결정 가능). Nếu không có algorithm như vậy, problem undecidable (결정 불가능).

Ví dụ nổi tiếng là **Halting Problem**: cho program `P` và input `x`, liệu có algorithm tổng quát `H(P,x)` luôn xác định đúng `P(x)` sẽ halt hay chạy vô hạn không? Turing chứng minh không tồn tại algorithm tổng quát như vậy.

### Intuition của proof bằng contradiction

Giả sử tồn tại `H(P,x)` trả lời đúng việc `P(x)` halt. Ta xây program `D(P)`:

```text
if H(P, P) says "halts":
    loop forever
else:
    halt
```

Giờ hỏi `D(D)` làm gì. Nếu `H(D,D)` nói halt, `D` cố tình loop. Nếu nói loop, `D` halt. Cả hai đều contradiction. Vì vậy giả định tồn tại `H` là sai.

Điểm quan trọng không phải memorize trick mà là self-reference tạo một input phá mọi decider giả định.

## Tại sao undecidability liên quan công việc thực?

Static analyzer, compiler và IDE có thể tìm nhiều bugs, nhưng không thể có một tool tổng quát hoàn hảo quyết định mọi semantic property của mọi program. Rice's theorem tổng quát hóa rằng mọi non-trivial semantic property của partial functions computed by programs là undecidable trong model đủ mạnh.

Điều này giải thích tại sao verification thực tế phải dùng restrictions, approximations, annotations hoặc domain-specific models. Type checker có thể bảo đảm class lỗi nhất định vì language/type system giới hạn câu hỏi. Model checker có thể exhaust state space hữu hạn. Linter chấp nhận false positives/negatives để hữu ích thực dụng.

## Recognizable khác decidable

Có problems mà nếu answer là “yes”, một machine có thể eventually accept, nhưng nếu answer “no” có thể chạy mãi. Đây là recognizable/semi-decidable (반결정 가능). Distinction này quan trọng trong theory vì “có thể xác nhận lời giải khi tìm thấy” không đồng nghĩa “luôn quyết định được có lời giải hay không”.

## Formal languages và automata như phổ models

Finite automata chỉ có finite memory, nhận regular languages. Pushdown automata có stack, nhận context-free languages và phù hợp với nhiều nested syntactic structures. Turing machines có unbounded read/write memory về lý thuyết, mạnh hơn.

Hierarchy này cho thấy thêm memory/structure làm model mạnh hơn. Compiler thực tế dùng finite automata cho lexical analysis và grammar/parsing techniques cho syntax, nhưng semantics của general programs vượt xa finite-state reasoning đơn giản.

Xem thêm phần compiler tại [Compiler, Interpreter, VM và JIT](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md).

## Computable không có nghĩa practical

Một problem có algorithm vẫn có thể cần resource khổng lồ. Đây là vùng của computational complexity. `O(2^n)` algorithm có thể terminate về lý thuyết nhưng không khả thi khi `n` lớn. Complexity classes như P, NP, PSPACE phân loại problems theo resources.

P gồm decision problems solvable in polynomial time trên deterministic model. NP có thể mô tả là problems mà một proposed solution có thể được verified in polynomial time. Câu hỏi `P = NP?` vẫn mở; không nên diễn giải NP là “non-polynomial” hoặc “không giải được”.

Chapter [Complexity & asymptotic analysis](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) tập trung reasoning resources thực dụng hơn.

## Randomness và approximation không phá giới hạn logic

Randomized algorithms có thể cải thiện expected performance hoặc cho xác suất đúng rất cao. Approximation algorithms có thể tìm lời giải gần optimal cho optimization problems khó. Heuristics có thể giải tốt workloads thực tế. Nhưng các kỹ thuật này thay specification hoặc guarantees; chúng không biến undecidable general problem thành decidable một cách thần kỳ.

## Mental Model

> Có ba câu hỏi khác nhau: **Có tồn tại algorithm không? Algorithm đó cần bao nhiêu resource? Implementation cụ thể chạy tốt trên workload/hardware này không?** Computability, complexity và systems performance trả lời ba tầng khác nhau.

## Common Misconceptions

**“Turing-complete nghĩa là ngôn ngữ mạnh/nhanh hơn.”** Nó chỉ nói về expressiveness lý thuyết dưới assumptions lý tưởng, không về performance hay software quality.

**“NP nghĩa là không polynomial.”** NP là nondeterministic polynomial time / polynomial-time verifiable theo characterization phổ biến. Có problems thuộc cả P và NP.

**“Undecidable nghĩa là không bao giờ giải được instance nào.”** Ta vẫn giải được nhiều instances hoặc restricted subclasses. Điều không thể là một algorithm tổng quát luôn đúng và terminate cho mọi instance theo problem specification.

## Kết nối

Computability đặt “biên ngoài” cho CS. Phía bên trong biên, [algorithmic thinking](../01_algorithms_data_structures/00_algorithmic_thinking_and_correctness.md) và [complexity](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) giúp chọn phương pháp; [testing/verification](../07_security_reliability/04_testing_verification_and_debugging.md) cho thấy cách thực tế xây confidence mà không giả định có một oracle hoàn hảo.
