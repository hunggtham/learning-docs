# Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Alphabet, string và ngôn ngữ (language / 언어)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Recognizer và decider khác nhau ở termination** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối automata với formal language và computability, để phân biệt máy nhận dạng được ngôn ngữ nào với bài toán không thể quyết định.

Một chương trình cụ thể trả lời câu hỏi “máy này làm gì?”. Lý thuyết tính toán (theory of computation / 계산이론) hỏi câu sâu hơn:

> Loại bộ nhớ (memory / 메모리) nào cần để nhận biết một mẫu (pattern / 패턴)? bài toán (problem / 문제) nào có thuật toán (algorithm / 알고리즘) giải được? Nếu giải được thì cần bao nhiêu tài nguyên (resource / 자원)?

Ba tầng nên được tách rõ:

```text
formal language
→ model of computation
→ computability
→ complexity
```

Formal ngôn ngữ (language / 언어) nói tập đầu vào (input / 입력) nào được chấp nhận. Automaton nói machine cần cấu trúc (structure / 구조) bộ nhớ (memory / 메모리) nào để nhận tập đó. Computability hỏi có thuật toán (algorithm / 알고리즘) luôn cho answer hay không. độ phức tạp (complexity / 복잡도) hỏi nếu có thì chi phí (cost / 비용) tăng theo đầu vào (input / 입력) kích thước (size / 크기) thế nào.

## 1. Alphabet, string và ngôn ngữ (language / 언어)

Một **alphabet / 알파벳** `Σ` là finite set symbols. Một **string / 문자열** là finite chuỗi (sequence / 시퀀스) symbols từ `Σ`.

Ký hiệu:

```math
\Sigma^*
```

là tập mọi finite strings trên `Σ`, gồm cả empty string `ε`.

Một **formal ngôn ngữ (language / 언어)** chỉ là subset:

```math
L\subseteq\Sigma^*.
```

Ví dụ với `Σ={0,1}`, ngôn ngữ (language / 언어)

```text
mọi binary strings có số lượng 1 chẵn
```

là một subset của `Σ*`.

Điểm quan trọng: ngôn ngữ (language / 언어) ở đây không cần “meaning” như ngôn ngữ tự nhiên. Nó là một **set-membership bài toán (problem / 문제)**:

```text
input string w
→ hỏi w ∈ L hay không
```

Đây là cầu nối (bridge / 브리지) từ set lý thuyết (theory / 이론) sang computation.

> **Chuyển mạch:** Trong **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **2. Recognizer và decider khác nhau ở termination** tiếp nhận điểm tựa từ **1. Alphabet, string và ngôn ngữ (language / 언어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. DFA: finite trạng thái (state / 상태) là finite bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Recognizer và decider khác nhau ở termination

Một machine **recognize** ngôn ngữ (language / 언어) nếu:

```text
w ∈ L  → eventually accept
w ∉ L  → có thể reject hoặc chạy mãi
```

Một machine **decide** ngôn ngữ (language / 언어) nếu nó luôn halt và trả đúng yes/no.

Sự khác nhau này nhỏ về wording nhưng rất lớn về lô-gic (logic / 논리). Một procedure chỉ “eventually tìm ra yes” chưa đủ để làm môi trường vận hành (production / 운영 환경) quyết định (decision / 결정) hệ thống (system / 시스템) nếu no-case có thể chạy vô hạn.

> **Chuyển mạch:** Ở chặng này của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **3. DFA: finite trạng thái (state / 상태) là finite bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **2. Recognizer và decider khác nhau ở termination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. NFA không mạnh hơn DFA về ngôn ngữ (language / 언어) lớp (class / 클래스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. DFA: finite trạng thái (state / 상태) là finite bộ nhớ (memory / 메모리)

Một **deterministic finite automaton (DFA / 결정적 유한 오토마타)** có thể formalize bằng 5-tuple:

```math
M=(Q,\Sigma,\delta,q_0,F)
```

trong đó:

- `Q` là finite set states;
- `Σ` là đầu vào (input / 입력) alphabet;
- `δ:Q×Σ→Q` là chuyển tiếp (transition / 전이) hàm (function / 함수);
- `q_0` là start trạng thái (state / 상태);
- `F⊆Q` là accepting states.

Machine đọc đầu vào (input / 입력) từ trái sang phải. Tại mỗi thời điểm, toàn bộ thông tin (information / 정보) mà machine giữ về prefix đã đọc phải được nén vào **một trạng thái (state / 상태) hữu hạn**.

Đó là bản chất của finite automaton.

### Worked example: parity của số lượng `1`

Ta chỉ cần hai states:

```text
EVEN
ODD
```

Mỗi `1` toggle trạng thái (state / 상태); `0` giữ trạng thái (state / 상태).

Machine không cần nhớ count chính xác. Nó chỉ cần equivalence lớp (class / 클래스) của count modulo 2.

Đây là một mẫu (pattern / 패턴) quan trọng:

> trạng thái (state / 상태) không cần giữ toàn lịch sử (history / 이력); nó chỉ cần giữ thông tin (information / 정보) từ lịch sử (history / 이력) còn relevant cho future quyết định (decision / 결정).

Mô hình tư duy (mental model / 사고 모델) này xuất hiện trong giao thức (protocol / 프로토콜) trạng thái (state / 상태) machines, parsers, động (dynamic / 동적) programming và Markov các mô hình (models / 모델들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **4. NFA không mạnh hơn DFA về ngôn ngữ (language / 언어) lớp (class / 클래스)** tiếp nhận điểm tựa từ **3. DFA: finite trạng thái (state / 상태) là finite bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Regular expressions và automata** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. NFA không mạnh hơn DFA về ngôn ngữ (language / 언어) lớp (class / 클래스)

**Nondeterministic finite automaton (NFA / 비결정적 유한 오토마타)** có thể có nhiều possible transitions cho một symbol và epsilon transitions.

NFA nhìn có vẻ “mạnh” hơn, nhưng mọi NFA đều có thể convert thành equivalent DFA bằng subset construction.

DFA trạng thái (state / 상태) mới represent một set possible NFA states.

Nếu NFA có `n` states, equivalent DFA trong worst trường hợp (case / 사례) có thể cần tới `2^n` states.

Điều này minh họa distinction quan trọng:

```text
expressive power giống nhau
≠ representation cost giống nhau
```

> **Chuyển mạch:** Trong **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **5. Regular expressions và automata** tiếp nhận điểm tựa từ **4. NFA không mạnh hơn DFA về ngôn ngữ (language / 언어) lớp (class / 클래스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Vì sao finite bộ nhớ (memory / 메모리) có giới hạn?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Regular expressions và automata

Classical **regular expression / 정규표현식** và finite automata mô tả cùng lớp (class / 클래스): **regular languages / 정규언어**.

Quan hệ concept:

```text
regex syntax
↔ regular language
↔ finite automaton
```

Trình biên dịch (compiler / 컴파일러) lexical phân tích (analysis / 분석) thường convert đơn vị từ (token / 토큰) patterns thành automata-like machinery.

Nhưng regex engines trong programming languages có thể thêm backreferences, lookarounds hoặc implementation-specific features mạnh hơn formal regular expressions. Vì vậy:

```text
“regex trong theory”
≠ luôn giống hoàn toàn “regex engine trong production”
```

> **Chuyển mạch:** Ở chặng này của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **5. Regular expressions và automata** đã nêu tiêu chí phân biệt, còn **6. Vì sao finite bộ nhớ (memory / 메모리) có giới hạn?** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **7. Context-free grammar: recursion trong cú pháp (syntax / 문법)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Vì sao finite bộ nhớ (memory / 메모리) có giới hạn?

Xét ngôn ngữ (language / 언어):

```math
L=\{0^n1^n:n\ge0\}.
```

Để quyết định membership, machine cần compare chính xác (exact / 정확한) count leading zeros với trailing ones.

Một DFA có finite states. Nếu đọc đủ nhiều zeros, theo pigeonhole principle hai different prefix lengths phải đưa machine vào cùng trạng thái (state / 상태).

Khi đó machine không còn distinguish hai counts khác nhau, nhưng future suffix cần distinction đó.

Đây là intuition của **pumping lemma / 펌핑 보조정리** và Myhill–Nerode style lập luận (reasoning / 추론).

### Proof idea quan trọng

Giới hạn không đến từ “DFA chạy chậm”. Nó đến từ **thông tin (information / 정보) sức chứa (capacity / 용량) của trạng thái (state / 상태)**.

Finite number states chỉ encode finite number equivalence classes của histories.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **6. Vì sao finite bộ nhớ (memory / 메모리) có giới hạn?** đã nêu tiêu chí phân biệt, còn **7. Context-free grammar: recursion trong cú pháp (syntax / 문법)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. Pushdown automaton: thêm ngăn xếp (stack / 스택) thì bộ nhớ (memory / 메모리) thay đổi qualitatively** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Context-free grammar: recursion trong cú pháp (syntax / 문법)

Một **context-free grammar (CFG / 문맥 자유 문법)** gồm variables/nonterminals, terminals, start symbol và môi trường vận hành (production / 운영 환경) rules.

Ví dụ balanced parentheses có recursive cấu trúc (structure / 구조):

```text
S → SS
S → (S)
S → ε
```

Grammar không chỉ danh sách (list / 목록) valid strings; nó mô tả cách strings được **generated recursively**.

Parse cây (tree / 트리) là proof rằng một string được derive từ grammar.

Đây là cầu nối (bridge / 브리지) giữa formal ngôn ngữ (language / 언어), recursion và trình biên dịch (compiler / 컴파일러) parsing.

> **Chuyển mạch:** Trong **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **8. Pushdown automaton: thêm ngăn xếp (stack / 스택) thì bộ nhớ (memory / 메모리) thay đổi qualitatively** tiếp nhận điểm tựa từ **7. Context-free grammar: recursion trong cú pháp (syntax / 문법)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Chomsky hierarchy như hierarchy của structural bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Pushdown automaton: thêm ngăn xếp (stack / 스택) thì bộ nhớ (memory / 메모리) thay đổi qualitatively

Một **pushdown automaton (PDA / 푸시다운 오토마타)** là finite điều khiển (control / 제어) cộng một ngăn xếp (stack / 스택).

Ngăn xếp (stack / 스택) cho phép bộ nhớ (memory / 메모리) unbounded theo độ sâu (depth / 깊이), nhưng chỉ truy cập theo LIFO.

Balanced parentheses là example tự nhiên:

```text
'(' → push
')' → pop
```

Nếu closing bracket xuất hiện khi ngăn xếp (stack / 스택) empty hoặc final ngăn xếp (stack / 스택) không empty, đầu vào (input / 입력) invalid.

Một ngăn xếp (stack / 스택) đủ cho many nested syntactic structures, nhưng không phải mọi computation.

> **Chuyển mạch:** Ở chặng này của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **9. Chomsky hierarchy như hierarchy của structural bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **8. Pushdown automaton: thêm ngăn xếp (stack / 스택) thì bộ nhớ (memory / 메모리) thay đổi qualitatively** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Turing machine: lớp trừu tượng (abstraction / 추상화) tối giản của general computation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Chomsky hierarchy như hierarchy của structural bộ nhớ (memory / 메모리)

Có thể nhìn formal ngôn ngữ (language / 언어) classes theo increasing expressive power:

```text
regular
⊂ context-free
⊂ context-sensitive
⊂ recursively enumerable
```

Không nên học hierarchy chỉ như taxonomy. mô hình tư duy (mental model / 사고 모델) là:

```text
pattern phức tạp hơn
→ cần richer memory / computational model
```

Regular languages dùng finite trạng thái (state / 상태). Context-free languages tương ứng stack-like bộ nhớ (memory / 메모리). Turing machines có general unbounded read/ghi (write / 쓰기) tape.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **10. Turing machine: lớp trừu tượng (abstraction / 추상화) tối giản của general computation** tiếp nhận điểm tựa từ **9. Chomsky hierarchy như hierarchy của structural bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Church–Turing thesis là thesis, không phải ordinary theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Turing machine: lớp trừu tượng (abstraction / 추상화) tối giản của general computation

Một **Turing machine / 튜링 기계** có:

- finite trạng thái (state / 상태) điều khiển (control / 제어);
- tape chia thành cells;
- read/ghi (write / 쓰기) head;
- chuyển tiếp (transition / 전이) quy tắc (rule / 규칙) dựa trên trạng thái hiện tại (current state / 현재 상태) + hiện tại (current / 현재) symbol.

Tape là unbounded trong mathematical mô hình (model / 모델).

Machine rất thành phần nguyên thủy (primitive / 기본 요소), nhưng có thể simulate conventional algorithms ở theoretical mức (level / 수준).

### Universal Turing machine

Một machine có thể nhận encoding của another machine + đầu vào (input / 입력) và simulate nó.

Đây là conceptual ancestor của stored-program computing:

```text
program cũng là data
```

Điều này mở đường cho self-reference, interpreters và undecidability proofs.

> **Chuyển mạch:** Trong **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **11. Church–Turing thesis là thesis, không phải ordinary theorem** tiếp nhận điểm tựa từ **10. Turing machine: lớp trừu tượng (abstraction / 추상화) tối giản của general computation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Decidable, recognizable và undecidable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Church–Turing thesis là thesis, không phải ordinary theorem

**Church–Turing thesis / 처치-튜링 명제** nói roughly:

> Mọi effectively computable procedure theo intuitive notion có thể được mô hình (model / 모델) bằng Turing-computable hàm (function / 함수).

Nó không phải theorem từ axioms thuần túy vì “effectively computable” ban đầu là informal concept.

Điều làm thesis mạnh là nhiều independently developed các mô hình (models / 모델들) — lambda calculus, recursive functions, Turing machines — hội tụ về cùng computability lớp (class / 클래스).

> **Chuyển mạch:** Ở chặng này của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **12. Decidable, recognizable và undecidable** tiếp nhận điểm tựa từ **11. Church–Turing thesis là thesis, không phải ordinary theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Halting bài toán (problem / 문제) và diagonalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Decidable, recognizable và undecidable

Một ngôn ngữ (language / 언어) **decidable / 결정가능** nếu có machine luôn halt và trả đúng membership.

Một ngôn ngữ (language / 언어) **recognizable / 인식가능** nếu yes-instances eventually accept nhưng no-instances có thể vòng lặp (loop / 루프) forever.

Một bài toán (problem / 문제) **undecidable / 결정불가능** nếu không tồn tại total thuật toán (algorithm / 알고리즘) giải đúng mọi đầu vào (input / 입력).

Undecidable không nghĩa:

```text
algorithm hiện tại chưa đủ tốt
```

mà nghĩa:

```text
đã chứng minh không có total algorithm cho general case trong model
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **13. Halting bài toán (problem / 문제) và diagonalization** tiếp nhận điểm tựa từ **12. Decidable, recognizable và undecidable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Reduction: chuyển difficulty từ bài toán (problem / 문제) này sang bài toán (problem / 문제) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Halting bài toán (problem / 문제) và diagonalization

Halting bài toán (problem / 문제) hỏi:

```text
given program P and input x,
P(x) có halt không?
```

Giả sử tồn tại decider:

```text
H(P,x)
```

trả đúng cho mọi pair.

Xây machine `D(P)`:

```text
if H(P,P) says HALT:
    loop forever
else:
    halt
```

Bây giờ chạy:

```text
D(D)
```

Nếu `H(D,D)` nói halt, definition của `D` khiến nó vòng lặp (loop / 루프).
Nếu nói vòng lặp (loop / 루프), `D` halt.

Cả hai đều contradiction.

Cốt lõi (core / 핵심) proof mẫu (pattern / 패턴) là **self-reference + diagonalization**.

Cùng family lập luận (reasoning / 추론) xuất hiện trong Cantor, Gödel và nhiều impossibility results.

> **Chuyển mạch:** Trong **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **14. Reduction: chuyển difficulty từ bài toán (problem / 문제) này sang bài toán (problem / 문제) khác** tiếp nhận điểm tựa từ **13. Halting bài toán (problem / 문제) và diagonalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Computability khác độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Reduction: chuyển difficulty từ bài toán (problem / 문제) này sang bài toán (problem / 문제) khác

Một **reduction / 환원** biến instance của bài toán (problem / 문제) `A` thành instance của `B` sao cho solve `B` giúp solve `A`.

Lô-gic (logic / 논리):

```text
A known hard/impossible
A reduces to B
→ B cannot be easier in relevant sense
```

Để prove `B` undecidable, ta thường lấy known undecidable `A` và show:

```text
nếu có decider cho B
→ xây được decider cho A
→ contradiction
```

Direction của reduction rất hay bị nhầm. Muốn chứng minh `B` hard, reduce **known hard A into B**, không phải ngược lại.

> **Chuyển mạch:** Ở chặng này của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **15. Computability khác độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **14. Reduction: chuyển difficulty từ bài toán (problem / 문제) này sang bài toán (problem / 문제) khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. NP-completeness và reduction mindset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Computability khác độ phức tạp (complexity / 복잡도)

Một bài toán (problem / 문제) có thể:

```text
decidable nhưng cực kỳ expensive
```

hoặc:

```text
undecidable
```

Hai claims khác tầng.

Độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) đặt tài nguyên (resource / 자원) bound lên computable problems.

### P

`P` là lớp (class / 클래스) quyết định (decision / 결정) problems solvable in polynomial thời gian (time / 시간) bằng deterministic mô hình (model / 모델).

### NP

`NP` là lớp (class / 클래스) problems mà yes-certificate có thể verify in polynomial thời gian (time / 시간).

`NP` không có nghĩa “non-polynomial”.

Câu hỏi:

```text
P = NP ?
```

vẫn open.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **16. NP-completeness và reduction mindset** tiếp nhận điểm tựa từ **15. Computability khác độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. trạng thái (state / 상태) machines trong kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. NP-completeness và reduction mindset

Một bài toán (problem / 문제) là **NP-hard** nếu mọi bài toán (problem / 문제) trong NP reduce đến nó theo suitable polynomial-time reduction.

Nó là **NP-complete** nếu vừa NP-hard vừa nằm trong NP.

Practical lesson không phải “NP-complete thì bỏ cuộc”. Nó nói general chính xác (exact / 정확한) bài toán (problem / 문제) có bằng chứng (evidence / 증거) mạnh về difficulty, nên kỹ thuật (engineering / 엔지니어링) có thể chuyển sang:

```text
special structure
approximation
heuristics
parameterization
branch-and-bound
relaxation
```

Đây là cầu nối (bridge / 브리지) trực tiếp sang tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Trong **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **17. trạng thái (state / 상태) machines trong kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)** tiếp nhận điểm tựa từ **16. NP-completeness và reduction mindset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. mô hình (model / 모델) checking liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. trạng thái (state / 상태) machines trong kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)

Automata không chỉ là lý thuyết (theory / 이론).

Authentication luồng (flow / 흐름):

```text
LOGGED_OUT
→ AUTHENTICATING
→ LOGGED_IN
→ EXPIRED
```

Mạng (network / 네트워크) giao thức (protocol / 프로토콜), workflow engine, UI trạng thái (state / 상태), parser và phân tán (distributed / 분산) dịch vụ (service / 서비스) vòng đời (lifecycle / 생명주기) đều có thể mô hình (model / 모델) bằng chuyển tiếp (transition / 전이) các hệ thống (systems / 시스템들).

Benefit của tường minh (explicit / 명시적) máy trạng thái (state machine / 상태 머신) là làm illegal transitions lộ ra.

Nhưng môi trường vận hành (production / 운영 환경) các hệ thống (systems / 시스템들) có tính đồng thời (concurrency / 동시성), partial thất bại (failure / 실패) và thời gian (time / 시간). Khi trạng thái (state / 상태) của nhiều components tương tác, simple DFA viewpoint có thể phải nâng thành sản phẩm (product / 제품) trạng thái (state / 상태) không gian (space / 공간), temporal lô-gic (logic / 논리) hoặc distributed-state mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, sau nội dung của **17. trạng thái (state / 상태) machines trong kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)**, **18. mô hình (model / 모델) checking liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **19. Parser, grammar và ngữ nghĩa (semantic / 의미적) các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. mô hình (model / 모델) checking liên kết (connection / 연결)

Nếu hệ thống (system / 시스템) có finite trạng thái (state / 상태) không gian (space / 공간) đủ nhỏ, ta có thể explore trạng thái (state / 상태) đồ thị (graph / 그래프) để verify properties:

```text
bad state có reachable không?
deadlock có thể xảy ra không?
request có eventually được response không?
```

**mô hình (model / 모델) checking / 모델 검사** nối automata với formal xác minh (verification / 확인).

Trạng thái (state / 상태) explosion là bottleneck: nếu `k` components mỗi thành phần (component / 컴포넌트) có `m` states, naive sản phẩm (product / 제품) có thể có `m^k` toàn cục (global / 전역) states.

Combinatorics quay trở lại ngay trong xác minh (verification / 확인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **19. Parser, grammar và ngữ nghĩa (semantic / 의미적) các ràng buộc (constraints / 제약조건들)** tiếp nhận điểm tựa từ **18. mô hình (model / 모델) checking liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. dùng chung (common / 공통) thất bại (failure / 실패) modes khi lập luận (reasoning / 추론) về computation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Parser, grammar và ngữ nghĩa (semantic / 의미적) các ràng buộc (constraints / 제약조건들)

CFG có thể mô tả nested cú pháp (syntax / 문법) như expressions và blocks.

Nhưng programming ngôn ngữ (language / 언어) validity còn gồm các ràng buộc (constraints / 제약조건들) như:

```text
variable phải được declared
function call phải match type/signature
break phải ở đúng context
```

Nhiều các ràng buộc (constraints / 제약조건들) không chỉ context-free cú pháp (syntax / 문법). trình biên dịch (compiler / 컴파일러) kiến trúc (architecture / 아키텍처) thường tách:

```text
lexing
→ parsing
→ semantic analysis
→ type checking
```

Đây là example đẹp của việc chọn computational mô hình (model / 모델) phù hợp từng tầng (layer / 계층).

> **Chuyển mạch:** Trong **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **20. dùng chung (common / 공통) thất bại (failure / 실패) modes khi lập luận (reasoning / 추론) về computation** tiếp nhận điểm tựa từ **19. Parser, grammar và ngữ nghĩa (semantic / 의미적) các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. dùng chung (common / 공통) thất bại (failure / 실패) modes khi lập luận (reasoning / 추론) về computation

### “Regex giải được mọi parsing bài toán (problem / 문제)”

Không đúng theo formal regular-language mô hình (model / 모델); nested recursion cần richer machinery.

### “Turing-computable nghĩa practical”

Không. Một thuật toán (algorithm / 알고리즘) có thể computable nhưng chi phí (cost / 비용) astronomical.

### “Undecidable nghĩa mọi instance impossible”

Không. Nhiều specific instances có thể dễ. Claim là không có one total thuật toán (algorithm / 알고리즘) giải **mọi** instance của general bài toán (problem / 문제).

### “NP-hard nghĩa không có thuật toán (algorithm / 알고리즘) hữu ích”

Không. Approximation, special cases và heuristics có thể rất hiệu quả.

> **Chuyển mạch:** Ở chặng này của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** tiếp nhận điểm tựa từ **20. dùng chung (common / 공통) thất bại (failure / 실패) modes khi lập luận (reasoning / 추론) về computation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Automata nằm tại intersection của nhiều chủ đề:

```text
set theory → language as subset of Σ*
graph theory → state-transition graph
recursion → grammar / parse tree
combinatorics → state explosion
logic → decidability / proofs
optimization → NP-hard search problems
software → protocols / parsers / workflows
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Khi gặp một computational bài toán (problem / 문제), đừng hỏi ngay “dùng thuật toán (algorithm / 알고리즘) nào?”. Trước hết hỏi đầu vào (input / 입력) ngôn ngữ (language / 언어) là gì, machine cần bộ nhớ (memory / 메모리) cấu trúc (structure / 구조) nào, bài toán (problem / 문제) có decidable không, rồi mới hỏi độ phức tạp (complexity / 복잡도). Nhiều confusion trong CS đến từ việc trộn bốn tầng này thành một.

> **Chuyển mạch:** Trong **Automata, formal languages và computability: từ finite bộ nhớ (memory / 메모리) đến giới hạn của thuật toán (algorithm / 알고리즘)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

Finite automaton không “yếu” vì chạy ít bước; nó bị giới hạn bởi finite trạng thái (state / 상태) bộ nhớ (memory / 메모리). NFA và DFA có cùng expressive power nhưng có thể khác rất lớn về biểu diễn (representation / 표현) kích thước (size / 크기). Church–Turing thesis không phải benchmark speed. Turing machine là lớp trừu tượng (abstraction / 추상화), không phải hardware thiết kế (design / 설계). Reduction direction phải đọc cẩn thận. Undecidability và intractability là hai loại limitation khác nhau.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
