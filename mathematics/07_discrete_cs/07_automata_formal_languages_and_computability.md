# Automata, formal languages và computability: từ finite memory đến giới hạn của algorithm

Một chương trình cụ thể trả lời câu hỏi “máy này làm gì?”. Lý thuyết tính toán (theory of computation / 계산이론) hỏi câu sâu hơn:

> Loại memory nào cần để nhận biết một pattern? Problem nào có algorithm giải được? Nếu giải được thì cần bao nhiêu resource?

Ba tầng nên được tách rõ:

```text
formal language
→ model of computation
→ computability
→ complexity
```

Formal language nói tập input nào được chấp nhận. Automaton nói machine cần structure memory nào để nhận tập đó. Computability hỏi có algorithm luôn cho answer hay không. Complexity hỏi nếu có thì cost tăng theo input size thế nào.

## 1. Alphabet, string và language

Một **alphabet / 알파벳** `Σ` là finite set symbols. Một **string / 문자열** là finite sequence symbols từ `Σ`.

Ký hiệu:

```math
\Sigma^*
```

là tập mọi finite strings trên `Σ`, gồm cả empty string `ε`.

Một **formal language (ngôn ngữ hình thức / 형식언어)** chỉ là subset:

```math
L\subseteq\Sigma^*.
```

Ví dụ với `Σ={0,1}`, language

```text
mọi binary strings có số lượng 1 chẵn
```

là một subset của `Σ*`.

Điểm quan trọng: language ở đây không cần “meaning” như ngôn ngữ tự nhiên. Nó là một **set-membership problem**:

```text
input string w
→ hỏi w ∈ L hay không
```

Đây là bridge từ set theory sang computation.

## 2. Recognizer và decider khác nhau ở termination

Một machine **recognize** language nếu:

```text
w ∈ L  → eventually accept
w ∉ L  → có thể reject hoặc chạy mãi
```

Một machine **decide** language nếu nó luôn halt và trả đúng yes/no.

Sự khác nhau này nhỏ về wording nhưng rất lớn về logic. Một procedure chỉ “eventually tìm ra yes” chưa đủ để làm production decision system nếu no-case có thể chạy vô hạn.

## 3. DFA: finite state là finite memory

Một **deterministic finite automaton (DFA / 결정적 유한 오토마타)** có thể formalize bằng 5-tuple:

```math
M=(Q,\Sigma,\delta,q_0,F)
```

trong đó:

- `Q` là finite set states;
- `Σ` là input alphabet;
- `δ:Q×Σ→Q` là transition function;
- `q_0` là start state;
- `F⊆Q` là accepting states.

Machine đọc input từ trái sang phải. Tại mỗi thời điểm, toàn bộ information mà machine giữ về prefix đã đọc phải được nén vào **một state hữu hạn**.

Đó là bản chất của finite automaton.

### Worked example: parity của số lượng `1`

Ta chỉ cần hai states:

```text
EVEN
ODD
```

Mỗi `1` toggle state; `0` giữ state.

Machine không cần nhớ count chính xác. Nó chỉ cần equivalence class của count modulo 2.

Đây là một pattern quan trọng:

> State không cần giữ toàn history; nó chỉ cần giữ information từ history còn relevant cho future decision.

Mental model này xuất hiện trong protocol state machines, parsers, dynamic programming và Markov models.

## 4. NFA không mạnh hơn DFA về language class

**Nondeterministic finite automaton (NFA / 비결정적 유한 오토마타)** có thể có nhiều possible transitions cho một symbol và epsilon transitions.

NFA nhìn có vẻ “mạnh” hơn, nhưng mọi NFA đều có thể convert thành equivalent DFA bằng subset construction.

DFA state mới represent một set possible NFA states.

Nếu NFA có `n` states, equivalent DFA trong worst case có thể cần tới `2^n` states.

Điều này minh họa distinction quan trọng:

```text
expressive power giống nhau
≠ representation cost giống nhau
```

## 5. Regular expressions và automata

Classical **regular expression / 정규표현식** và finite automata mô tả cùng class: **regular languages / 정규언어**.

Quan hệ concept:

```text
regex syntax
↔ regular language
↔ finite automaton
```

Compiler lexical analysis thường convert token patterns thành automata-like machinery.

Nhưng regex engines trong programming languages có thể thêm backreferences, lookarounds hoặc implementation-specific features mạnh hơn formal regular expressions. Vì vậy:

```text
“regex trong theory”
≠ luôn giống hoàn toàn “regex engine trong production”
```

## 6. Vì sao finite memory có giới hạn?

Xét language:

```math
L=\{0^n1^n:n\ge0\}.
```

Để quyết định membership, machine cần compare exact count leading zeros với trailing ones.

Một DFA có finite states. Nếu đọc đủ nhiều zeros, theo pigeonhole principle hai different prefix lengths phải đưa machine vào cùng state.

Khi đó machine không còn distinguish hai counts khác nhau, nhưng future suffix cần distinction đó.

Đây là intuition của **pumping lemma / 펌핑 보조정리** và Myhill–Nerode style reasoning.

### Proof idea quan trọng

Giới hạn không đến từ “DFA chạy chậm”. Nó đến từ **information capacity của state**.

Finite number states chỉ encode finite number equivalence classes của histories.

## 7. Context-free grammar: recursion trong syntax

Một **context-free grammar (CFG / 문맥 자유 문법)** gồm variables/nonterminals, terminals, start symbol và production rules.

Ví dụ balanced parentheses có recursive structure:

```text
S → SS
S → (S)
S → ε
```

Grammar không chỉ list valid strings; nó mô tả cách strings được **generated recursively**.

Parse tree là proof rằng một string được derive từ grammar.

Đây là bridge giữa formal language, recursion và compiler parsing.

## 8. Pushdown automaton: thêm stack thì memory thay đổi qualitatively

Một **pushdown automaton (PDA / 푸시다운 오토마타)** là finite control cộng một stack.

Stack cho phép memory unbounded theo depth, nhưng chỉ truy cập theo LIFO.

Balanced parentheses là example tự nhiên:

```text
'(' → push
')' → pop
```

Nếu closing bracket xuất hiện khi stack empty hoặc final stack không empty, input invalid.

Một stack đủ cho many nested syntactic structures, nhưng không phải mọi computation.

## 9. Chomsky hierarchy như hierarchy của structural memory

Có thể nhìn formal language classes theo increasing expressive power:

```text
regular
⊂ context-free
⊂ context-sensitive
⊂ recursively enumerable
```

Không nên học hierarchy chỉ như taxonomy. Mental model là:

```text
pattern phức tạp hơn
→ cần richer memory / computational model
```

Regular languages dùng finite state. Context-free languages tương ứng stack-like memory. Turing machines có general unbounded read/write tape.

## 10. Turing machine: abstraction tối giản của general computation

Một **Turing machine / 튜링 기계** có:

- finite state control;
- tape chia thành cells;
- read/write head;
- transition rule dựa trên current state + current symbol.

Tape là unbounded trong mathematical model.

Machine rất primitive, nhưng có thể simulate conventional algorithms ở theoretical level.

### Universal Turing machine

Một machine có thể nhận encoding của another machine + input và simulate nó.

Đây là conceptual ancestor của stored-program computing:

```text
program cũng là data
```

Điều này mở đường cho self-reference, interpreters và undecidability proofs.

## 11. Church–Turing thesis là thesis, không phải ordinary theorem

**Church–Turing thesis / 처치-튜링 명제** nói roughly:

> Mọi effectively computable procedure theo intuitive notion có thể được model bằng Turing-computable function.

Nó không phải theorem từ axioms thuần túy vì “effectively computable” ban đầu là informal concept.

Điều làm thesis mạnh là nhiều independently developed models — lambda calculus, recursive functions, Turing machines — hội tụ về cùng computability class.

## 12. Decidable, recognizable và undecidable

Một language **decidable / 결정가능** nếu có machine luôn halt và trả đúng membership.

Một language **recognizable / 인식가능** nếu yes-instances eventually accept nhưng no-instances có thể loop forever.

Một problem **undecidable / 결정불가능** nếu không tồn tại total algorithm giải đúng mọi input.

Undecidable không nghĩa:

```text
algorithm hiện tại chưa đủ tốt
```

mà nghĩa:

```text
đã chứng minh không có total algorithm cho general case trong model
```

## 13. Halting problem và diagonalization

Halting problem hỏi:

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

Nếu `H(D,D)` nói halt, definition của `D` khiến nó loop.
Nếu nói loop, `D` halt.

Cả hai đều contradiction.

Core proof pattern là **self-reference + diagonalization**.

Cùng family reasoning xuất hiện trong Cantor, Gödel và nhiều impossibility results.

## 14. Reduction: chuyển difficulty từ problem này sang problem khác

Một **reduction / 환원** biến instance của problem `A` thành instance của `B` sao cho solve `B` giúp solve `A`.

Logic:

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

## 15. Computability khác complexity

Một problem có thể:

```text
decidable nhưng cực kỳ expensive
```

hoặc:

```text
undecidable
```

Hai claims khác tầng.

Complexity theory đặt resource bound lên computable problems.

### P

`P` là class decision problems solvable in polynomial time bằng deterministic model.

### NP

`NP` là class problems mà yes-certificate có thể verify in polynomial time.

`NP` không có nghĩa “non-polynomial”.

Câu hỏi:

```text
P = NP ?
```

vẫn open.

## 16. NP-completeness và reduction mindset

Một problem là **NP-hard** nếu mọi problem trong NP reduce đến nó theo suitable polynomial-time reduction.

Nó là **NP-complete** nếu vừa NP-hard vừa nằm trong NP.

Practical lesson không phải “NP-complete thì bỏ cuộc”. Nó nói general exact problem có evidence mạnh về difficulty, nên engineering có thể chuyển sang:

```text
special structure
approximation
heuristics
parameterization
branch-and-bound
relaxation
```

Đây là bridge trực tiếp sang optimization.

## 17. State machines trong software engineering

Automata không chỉ là theory.

Authentication flow:

```text
LOGGED_OUT
→ AUTHENTICATING
→ LOGGED_IN
→ EXPIRED
```

Network protocol, workflow engine, UI state, parser và distributed service lifecycle đều có thể model bằng transition systems.

Benefit của explicit state machine là làm illegal transitions lộ ra.

Nhưng production systems có concurrency, partial failure và time. Khi state của nhiều components tương tác, simple DFA viewpoint có thể phải nâng thành product state space, temporal logic hoặc distributed-state model.

## 18. Model checking connection

Nếu system có finite state space đủ nhỏ, ta có thể explore state graph để verify properties:

```text
bad state có reachable không?
deadlock có thể xảy ra không?
request có eventually được response không?
```

**Model checking / 모델 검사** nối automata với formal verification.

State explosion là bottleneck: nếu `k` components mỗi component có `m` states, naive product có thể có `m^k` global states.

Combinatorics quay trở lại ngay trong verification.

## 19. Parser, grammar và semantic constraints

CFG có thể mô tả nested syntax như expressions và blocks.

Nhưng programming language validity còn gồm constraints như:

```text
variable phải được declared
function call phải match type/signature
break phải ở đúng context
```

Nhiều constraints không chỉ context-free syntax. Compiler architecture thường tách:

```text
lexing
→ parsing
→ semantic analysis
→ type checking
```

Đây là example đẹp của việc chọn computational model phù hợp từng layer.

## 20. Common failure modes khi reasoning về computation

### “Regex giải được mọi parsing problem”

Không đúng theo formal regular-language model; nested recursion cần richer machinery.

### “Turing-computable nghĩa practical”

Không. Một algorithm có thể computable nhưng cost astronomical.

### “Undecidable nghĩa mọi instance impossible”

Không. Nhiều specific instances có thể dễ. Claim là không có one total algorithm giải **mọi** instance của general problem.

### “NP-hard nghĩa không có algorithm hữu ích”

Không. Approximation, special cases và heuristics có thể rất hiệu quả.

## Knowledge Connection

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

## Mental Model

> Khi gặp một computational problem, đừng hỏi ngay “dùng algorithm nào?”. Trước hết hỏi input language là gì, machine cần memory structure nào, problem có decidable không, rồi mới hỏi complexity. Nhiều confusion trong CS đến từ việc trộn bốn tầng này thành một.

## Common Misconceptions

Finite automaton không “yếu” vì chạy ít bước; nó bị giới hạn bởi finite state memory. NFA và DFA có cùng expressive power nhưng có thể khác rất lớn về representation size. Church–Turing thesis không phải benchmark speed. Turing machine là abstraction, không phải hardware design. Reduction direction phải đọc cẩn thận. Undecidability và intractability là hai loại limitation khác nhau.