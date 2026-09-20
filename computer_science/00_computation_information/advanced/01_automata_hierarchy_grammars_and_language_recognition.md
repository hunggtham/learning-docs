# Automata hierarchy, grammars và language recognition

Formal language theory nối ba thứ tưởng tách biệt: cách mô tả một tập strings, loại machine có thể nhận diện tập đó và lượng memory machine cần. Khi nhìn theo hướng này, regex, parser và Turing machine không còn là danh sách công cụ rời rạc mà nằm trên một hierarchy về expressive power.

## Language là một tập strings

Cho alphabet `Σ`, một formal language là subset của `Σ*`. Grammar mô tả cách sinh strings; recognizer/automaton trả lời string có thuộc language hay không. Hai representation khác nhau có thể mô tả cùng language class.

## Finite automata và regular languages

DFA/NFA có hữu hạn states và không có memory tăng theo input. Chúng phù hợp pattern cần nhớ lượng state hữu hạn: token đơn giản, protocol state nhỏ, lexical scanning.

Regular expression trong formal-language sense tương ứng regular languages. Regex engine thực tế có thể thêm backreference hoặc feature vượt regular power, vì vậy cần phân biệt mathematical regex với implementation cụ thể.

## Pushdown automata và context-free languages

Nested structure như balanced parentheses cần nhớ depth không giới hạn. Pushdown automaton thêm stack, đủ để nhận nhiều context-free languages. Context-free grammar vì thế phù hợp syntax tree của programming language.

Parser không chỉ “match text”; nó reconstruct hierarchical structure từ token stream theo grammar.

## Context-sensitive và Turing-complete models

Khi machine có memory linh hoạt hơn, expressive power tăng. Turing machine cung cấp model tổng quát cho computability. Nhưng power tăng thường làm analysis khó hơn: nhiều property dễ quyết định trên finite-state system trở thành khó hoặc undecidable trên general program.

## Chomsky hierarchy là memory hierarchy về mặt trực giác

Có thể đọc hierarchy như câu hỏi: recognizer cần bao nhiêu cấu trúc memory để phân biệt histories quan trọng? Finite state nhớ hữu hạn summary; stack nhớ nested history; general tape/memory cho computation tổng quát.

Đây là trực giác hữu ích hơn học thuộc Type-3/2/1/0 mà không hiểu mechanism.

## Compiler pipeline

Lexer thường dùng regular machinery để biến characters thành tokens. Parser dùng grammar mạnh hơn để tạo syntax tree. Semantic analysis sau đó cần symbol table, type environment và context mà pure CFG không biểu diễn hết.

Việc compiler chia phases phản ánh hierarchy của information: dùng mechanism đơn giản nhất đủ cho từng layer giúp implementation dễ reasoning và tối ưu hơn.

## Protocol và verification

Nếu protocol có thể abstract thành finite states, model checking có thể explore state graph exhaustively trong bound phù hợp. Khi state chứa unbounded queue/counter, state space có thể vô hạn và verification cần abstraction.

Do đó chọn model yếu hơn khi đủ dùng không phải hạn chế; nó tạo khả năng phân tích mạnh hơn.

## Pumping lemma và giới hạn representation

Pumping lemma có thể chứng minh một số language không regular, nhưng nó là necessary property chứ không phải tool duy nhất. Mental model quan trọng là finite automaton có hữu hạn states: với input đủ dài, state phải lặp; machine không thể nhớ arbitrary amount of structure.

## Mental model

> Formal-language hierarchy là hierarchy của memory và expressive power. Model càng mạnh, càng mô tả được nhiều computation nhưng càng khó phân tích. Engineering tốt thường chọn model yếu nhất vẫn đủ biểu đạt problem vì restriction tạo ra decidability, tooling và performance.