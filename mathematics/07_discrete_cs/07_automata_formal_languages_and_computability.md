# Automata, formal languages và computability

Một chương trình thực thi một computation, nhưng trước khi nói về language như Java hay Python, theoretical computer science đặt câu hỏi cơ bản hơn: **computation là gì, machine tối thiểu nào đủ để nhận biết một pattern, và có problems nào không thể được giải bởi bất kỳ algorithm nào không?**

## Alphabet, string và language

Alphabet `\Sigma` là finite set symbols. Một string là finite sequence các symbols. Tập mọi finite strings viết `\Sigma^*`.

Formal language (형식언어) chỉ là subset:

```math
L\subseteq\Sigma^*.
```

Ví dụ với `\Sigma={0,1}`, language các strings có số lượng `1` chẵn là một subset của mọi binary strings.

Khái niệm này tách syntax khỏi meaning: trước tiên ta hỏi string có thuộc tập pattern hợp lệ hay không.

## Finite automaton

Deterministic finite automaton (DFA / 결정적 유한 오토마타) gồm finite states, input alphabet, transition function, start state và accepting states.

Machine đọc từng symbol và update state. State encode lượng memory hữu hạn cần thiết về prefix đã đọc.

Ví dụ để kiểm tra parity của số `1`, chỉ cần hai states: EVEN và ODD. Mỗi `1` toggle state; mỗi `0` giữ state.

Regular expressions và finite automata có expressive power tương đương cho regular languages. Đây là nền của lexical analysis, pattern matching và protocol state machines.

## Vì sao finite memory có giới hạn?

Language

```math
L=\{0^n1^n:n\ge0\}
```

yêu cầu remember exact count of leading zeros để compare với trailing ones. Finite automaton có finite states nên với count đủ lớn phải reuse state và mất distinction cần thiết.

Pumping lemma formalizes loại limitation này.

## Context-free grammar và stack

Context-free grammar (CFG / 문맥 자유 문법) sinh strings bằng production rules. Pushdown automaton có thêm stack, cho memory dạng last-in-first-out.

Balanced parentheses cần stack-like structure: mỗi opening bracket push, mỗi closing bracket pop matching type.

Programming language parsers thường dùng context-free structure cho nested syntax, dù real languages còn có context-sensitive constraints xử lý ở semantic phases.

## Turing machine

Turing machine là abstract model có finite control nhưng tape unbounded. Dù cực kỳ đơn giản, nó capture notion rộng của effective computation.

Church–Turing thesis nói mọi effectively calculable function theo intuitive notion có thể được tính bởi Turing machine. Đây là thesis về correspondence của models, không phải theorem chứng minh từ formal axioms về thế giới vật lý.

## Decidability

Một language/problem decidable nếu tồn tại algorithm luôn halt và trả đúng yes/no cho mọi input.

Một problem recognizable có thể accept yes-instances nhưng có thể chạy mãi trên no-instances.

Sự khác biệt “luôn kết thúc” rất quan trọng: existence of a procedure không đủ nếu procedure có thể không terminate khi answer là no.

## Halting problem

Halting problem hỏi: cho program `P` và input `x`, `P(x)` có halt hay không?

Không tồn tại algorithm tổng quát quyết định đúng cho mọi possible program/input pair.

Proof dùng self-reference/diagonalization. Giả sử có `H(P,x)` quyết định halting. Ta xây program `D(P)` làm ngược: nếu `H(P,P)` nói halt thì `D` loop forever; nếu nói không halt thì `D` halt. Chạy `D(D)` tạo contradiction.

Kết quả này không nói “debugging là vô vọng”. Nó nói không có universal perfect halting decider cho mọi programs.

## Reductions

Reduction biến một problem A thành problem B sao cho solver cho B có thể giải A. Nếu A đã biết impossible và A reduces to B, thì B cũng impossible theo relevant sense.

Trong complexity theory, reductions cũng dùng để so hardness, ví dụ polynomial-time reductions trong NP-completeness.

## P, NP và tractability

Class P chứa decision problems solvable in polynomial time by deterministic machine. NP chứa problems mà yes-certificate có thể verify in polynomial time.

`P=NP?` vẫn là open problem. Không nên nói NP nghĩa “non-polynomial”; tên lịch sử là nondeterministic polynomial time.

Complexity khác computability: một problem có thể decidable nhưng computationally impractical; undecidable còn mạnh hơn — không có total algorithm nào cả.

## Knowledge Connection

Automata nối graph/state transition với language recognition. Grammars nối recursion với parse trees. Computability nối logic với limits của algorithms. Complexity thêm resource constraints lên problems vốn computable.

## Mental Model

> Formal language nói “inputs hợp lệ là tập nào”; automaton nói “machine cần loại memory nào để nhận tập đó”; computability hỏi “có algorithm luôn giải được không”; complexity hỏi “nếu giải được thì tốn bao nhiêu resource”.

## Common Misconceptions

Regex trong modern programming engines có thể có features mạnh hơn formal regular expressions cổ điển. NP không có nghĩa “không polynomial”. Undecidable không đồng nghĩa “chưa tìm ra thuật toán”; đó là proof rằng không có total algorithm cho general case trong model. Turing machine không phải hardware proposal mà là abstraction của computation.
