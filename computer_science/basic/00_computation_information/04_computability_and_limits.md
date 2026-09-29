# Computability và giới hạn của tính toán

> **Mạch đọc:** Đọc **Computability và giới hạn của tính toán** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Một computation mô hình (model / 모델) cần những gì?** sang **Decidable và undecidable**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi học programming, ta dễ hình thành cảm giác rằng mọi bài toán chỉ cần “đủ mã (code / 코드) và đủ CPU”. lý thuyết (theory / 이론) of Computation (이론 전산학 / lý thuyết tính toán) cho thấy có ít nhất ba tầng khác nhau: có bài toán **không thể được giải bằng thuật toán (algorithm / 알고리즘) nói chung**; có bài toán computable nhưng quá đắt về tài nguyên (resource / 자원); và có bài toán tractable nếu chọn đúng thuật toán (algorithm / 알고리즘)/mô hình (model / 모델).

Chapter này tập trung tầng đầu: computability (계산 가능성 / khả năng tính toán) và những giới hạn mang tính nguyên lý.

## Một computation mô hình (model / 모델) cần những gì?

Để nói “thuật toán (algorithm / 알고리즘) nào cũng không giải được”, ta phải có mô hình (model / 모델) đủ tổng quát về computation. Turing machine là mô hình (model / 모델) cổ điển: một tape vô hạn về lý thuyết, head đọc/ghi symbols, finite điều khiển (control / 제어) trạng thái (state / 상태) và chuyển tiếp (transition / 전이) rules. Nó rất đơn giản nhưng có sức biểu đạt tương đương nhiều các mô hình (models / 모델들) tổng quát khác theo Church–Turing thesis.

Church–Turing thesis không phải theorem vật lý chứng minh mọi máy có thể tưởng tượng đều bị giới hạn như Turing machine. Nó là claim nền tảng rằng mọi hàm (function / 함수) có thể được tính theo nghĩa effective procedure đều computable bởi Turing machine hoặc mô hình (model / 모델) tương đương.

Programming languages general-purpose hiện đại về lý thuyết thường Turing-complete nếu có đủ bộ nhớ (memory / 메모리) và điều khiển (control / 제어) constructs. Điều đó không có nghĩa chúng giống nhau về hiệu năng (performance / 성능), an toàn (safety / 안전) hay ergonomics; chỉ nói về lớp (class / 클래스) functions có thể biểu đạt.


> **Chuyển mạch:** Từ **Một computation mô hình (model / 모델) cần những gì?**, ta sang **Decidable và undecidable** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Decidable và undecidable

Một quyết định (decision / 결정) bài toán (problem / 문제) hỏi yes/no. Nếu tồn tại thuật toán (algorithm / 알고리즘) luôn terminate và trả lời đúng cho mọi đầu vào (input / 입력), bài toán (problem / 문제) là decidable (결정 가능). Nếu không có thuật toán (algorithm / 알고리즘) như vậy, bài toán (problem / 문제) undecidable (결정 불가능).

Ví dụ nổi tiếng là **Halting bài toán (problem / 문제)**: cho program `P` và đầu vào (input / 입력) `x`, liệu có thuật toán (algorithm / 알고리즘) tổng quát `H(P,x)` luôn xác định đúng `P(x)` sẽ halt hay chạy vô hạn không? Turing chứng minh không tồn tại thuật toán (algorithm / 알고리즘) tổng quát như vậy.

### Intuition của proof bằng contradiction

Giả sử tồn tại `H(P,x)` trả lời đúng việc `P(x)` halt. Ta xây program `D(P)`:

```text
if H(P, P) says "halts":
    loop forever
else:
    halt
```

Giờ hỏi `D(D)` làm gì. Nếu `H(D,D)` nói halt, `D` cố tình vòng lặp (loop / 루프). Nếu nói vòng lặp (loop / 루프), `D` halt. Cả hai đều contradiction. Vì vậy giả định tồn tại `H` là sai.

Điểm quan trọng không phải memorize trick mà là self-reference tạo một đầu vào (input / 입력) phá mọi decider giả định.


> **Chuyển mạch:** Từ **Decidable và undecidable**, ta sang **Tại sao undecidability liên quan công việc thực?** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tại sao undecidability liên quan công việc thực?

Static analyzer, trình biên dịch (compiler / 컴파일러) và IDE có thể tìm nhiều bugs, nhưng không thể có một công cụ (tool / 도구) tổng quát hoàn hảo quyết định mọi ngữ nghĩa (semantic / 의미적) thuộc tính (property / 속성) của mọi program. Rice's theorem tổng quát hóa rằng mọi non-trivial ngữ nghĩa (semantic / 의미적) thuộc tính (property / 속성) của partial functions computed by programs là undecidable trong mô hình (model / 모델) đủ mạnh.

Điều này giải thích tại sao xác minh (verification / 확인) thực tế phải dùng restrictions, approximations, annotations hoặc domain-specific các mô hình (models / 모델들). kiểu (type / 타입) checker có thể bảo đảm lớp (class / 클래스) lỗi nhất định vì ngôn ngữ (language / 언어)/hệ kiểu (type system / 타입 시스템) giới hạn câu hỏi. mô hình (model / 모델) checker có thể exhaust trạng thái (state / 상태) không gian (space / 공간) hữu hạn. Linter chấp nhận false positives/negatives để hữu ích thực dụng.


> **Chuyển mạch:** Từ **Tại sao undecidability liên quan công việc thực?**, ta sang **Recognizable khác decidable** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Recognizable khác decidable

Có problems mà nếu answer là “yes”, một machine có thể eventually accept, nhưng nếu answer “no” có thể chạy mãi. Đây là recognizable/semi-decidable (반결정 가능). Distinction này quan trọng trong lý thuyết (theory / 이론) vì “có thể xác nhận lời giải khi tìm thấy” không đồng nghĩa “luôn quyết định được có lời giải hay không”.


> **Chuyển mạch:** Từ **Recognizable khác decidable**, ta sang **Formal languages và automata như phổ các mô hình (models / 모델들)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Formal languages và automata như phổ các mô hình (models / 모델들)

Finite automata chỉ có finite bộ nhớ (memory / 메모리), nhận regular languages. Pushdown automata có ngăn xếp (stack / 스택), nhận context-free languages và phù hợp với nhiều nested syntactic structures. Turing machines có unbounded read/ghi (write / 쓰기) bộ nhớ (memory / 메모리) về lý thuyết, mạnh hơn.

Hierarchy này cho thấy thêm bộ nhớ (memory / 메모리)/cấu trúc (structure / 구조) làm mô hình (model / 모델) mạnh hơn. trình biên dịch (compiler / 컴파일러) thực tế dùng finite automata cho lexical phân tích (analysis / 분석) và grammar/parsing techniques cho cú pháp (syntax / 문법), nhưng ngữ nghĩa (semantics / 의미론) của general programs vượt xa finite-state lập luận (reasoning / 추론) đơn giản.

Xem thêm phần trình biên dịch (compiler / 컴파일러) tại [Compiler, Interpreter, VM và JIT](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md).


> **Chuyển mạch:** Từ **Formal languages và automata như phổ các mô hình (models / 모델들)**, ta sang **Computable không có nghĩa practical** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Computable không có nghĩa practical

Một bài toán (problem / 문제) có thuật toán (algorithm / 알고리즘) vẫn có thể cần tài nguyên (resource / 자원) khổng lồ. Đây là vùng của computational độ phức tạp (complexity / 복잡도). `O(2^n)` thuật toán (algorithm / 알고리즘) có thể terminate về lý thuyết nhưng không khả thi khi `n` lớn. độ phức tạp (complexity / 복잡도) classes như P, NP, PSPACE phân loại problems theo resources.

P gồm quyết định (decision / 결정) problems solvable in polynomial thời gian (time / 시간) trên deterministic mô hình (model / 모델). NP có thể mô tả là problems mà một proposed solution có thể được verified in polynomial thời gian (time / 시간). Câu hỏi `P = NP?` vẫn mở; không nên diễn giải NP là “non-polynomial” hoặc “không giải được”.

Chapter [Complexity & asymptotic analysis](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) tập trung lập luận (reasoning / 추론) resources thực dụng hơn.


> **Chuyển mạch:** Từ **Computable không có nghĩa practical**, ta sang **Randomness và approximation không phá giới hạn lô-gic (logic / 논리)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Randomness và approximation không phá giới hạn lô-gic (logic / 논리)

Randomized algorithms có thể cải thiện expected hiệu năng (performance / 성능) hoặc cho xác suất đúng rất cao. Approximation algorithms có thể tìm lời giải gần optimal cho tối ưu hóa (optimization / 최적화) problems khó. Heuristics có thể giải tốt workloads thực tế. Nhưng các kỹ thuật này thay specification hoặc guarantees; chúng không biến undecidable general bài toán (problem / 문제) thành decidable một cách thần kỳ.


> **Chuyển mạch:** Từ **Randomness và approximation không phá giới hạn lô-gic (logic / 논리)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Có ba câu hỏi khác nhau: **Có tồn tại thuật toán (algorithm / 알고리즘) không? thuật toán (algorithm / 알고리즘) đó cần bao nhiêu tài nguyên (resource / 자원)? hiện thực (implementation / 구현) cụ thể chạy tốt trên tải công việc (workload / 워크로드)/hardware này không?** Computability, độ phức tạp (complexity / 복잡도) và các hệ thống (systems / 시스템들) hiệu năng (performance / 성능) trả lời ba tầng khác nhau.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Turing-complete nghĩa là ngôn ngữ mạnh/nhanh hơn.”** Nó chỉ nói về expressiveness lý thuyết dưới các giả định (assumptions / 가정들) lý tưởng, không về hiệu năng (performance / 성능) hay software chất lượng (quality / 품질).

**“NP nghĩa là không polynomial.”** NP là nondeterministic polynomial thời gian (time / 시간) / polynomial-time verifiable theo characterization phổ biến. Có problems thuộc cả P và NP.

**“Undecidable nghĩa là không bao giờ giải được instance nào.”** Ta vẫn giải được nhiều instances hoặc restricted subclasses. Điều không thể là một thuật toán (algorithm / 알고리즘) tổng quát luôn đúng và terminate cho mọi instance theo bài toán (problem / 문제) specification.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Computability đặt “biên ngoài” cho CS. Phía bên trong biên, [algorithmic thinking](../01_algorithms_data_structures/00_algorithmic_thinking_and_correctness.md) và [complexity](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) giúp chọn phương pháp; [testing/verification](../07_security_reliability/04_testing_verification_and_debugging.md) cho thấy cách thực tế xây confidence mà không giả định có một oracle hoàn hảo.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 what computer science studies](./00_what_computer_science_studies.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
