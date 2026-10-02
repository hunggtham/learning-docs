# Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**. Route đi từ language/string → finite automata và regular languages → pushdown/context-free → Turing machines/hierarchy, để khả năng nhận dạng được nối với bộ nhớ và sức biểu đạt.

Formal ngôn ngữ (language / 언어) lý thuyết (theory / 이론) nối ba thứ tưởng tách biệt: cách mô tả một tập strings, loại machine có thể nhận diện tập đó và lượng bộ nhớ (memory / 메모리) machine cần. Khi nhìn theo hướng này, regex, parser và Turing machine không còn là danh sách công cụ rời rạc mà nằm trên một hierarchy về expressive power.

## Ngôn ngữ (language / 언어) là một tập strings

Cho alphabet `Σ`, một formal ngôn ngữ (language / 언어) là subset của `Σ*`. Grammar mô tả cách sinh strings; recognizer/automaton trả lời string có thuộc ngôn ngữ (language / 언어) hay không. Hai biểu diễn (representation / 표현) khác nhau có thể mô tả cùng ngôn ngữ (language / 언어) lớp (class / 클래스).

> **Chuyển mạch:** Trong **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**, **Finite automata và regular languages** tiếp nhận điểm tựa từ **Ngôn ngữ (language / 언어) là một tập strings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pushdown automata và context-free languages** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Finite automata và regular languages

DFA/NFA có hữu hạn states và không có bộ nhớ (memory / 메모리) tăng theo đầu vào (input / 입력). Chúng phù hợp mẫu (pattern / 패턴) cần nhớ lượng trạng thái (state / 상태) hữu hạn: đơn vị từ (token / 토큰) đơn giản, giao thức (protocol / 프로토콜) trạng thái (state / 상태) nhỏ, lexical scanning.

Regular expression trong formal-language sense tương ứng regular languages. Regex engine thực tế có thể thêm backreference hoặc tính năng (feature / 기능) vượt regular power, vì vậy cần phân biệt mathematical regex với hiện thực (implementation / 구현) cụ thể.

> **Chuyển mạch:** Ở chặng này của **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**, **Pushdown automata và context-free languages** tiếp nhận điểm tựa từ **Finite automata và regular languages** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Context-sensitive và Turing-complete các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pushdown automata và context-free languages

Nested cấu trúc (structure / 구조) như balanced parentheses cần nhớ độ sâu (depth / 깊이) không giới hạn. Pushdown automaton thêm ngăn xếp (stack / 스택), đủ để nhận nhiều context-free languages. Context-free grammar vì thế phù hợp cú pháp (syntax / 문법) cây (tree / 트리) của programming ngôn ngữ (language / 언어).

Parser không chỉ “match văn bản (text / 텍스트)”; nó reconstruct hierarchical cấu trúc (structure / 구조) từ đơn vị từ (token / 토큰) stream theo grammar.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**, **Context-sensitive và Turing-complete các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Pushdown automata và context-free languages** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chomsky hierarchy là bộ nhớ (memory / 메모리) hierarchy về mặt trực giác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Context-sensitive và Turing-complete các mô hình (models / 모델들)

Khi machine có bộ nhớ (memory / 메모리) linh hoạt hơn, expressive power tăng. Turing machine cung cấp mô hình (model / 모델) tổng quát cho computability. Nhưng power tăng thường làm phân tích (analysis / 분석) khó hơn: nhiều thuộc tính (property / 속성) dễ quyết định trên finite-state hệ thống (system / 시스템) trở thành khó hoặc undecidable trên general program.

> **Chuyển mạch:** Trong **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**, **Chomsky hierarchy là bộ nhớ (memory / 메모리) hierarchy về mặt trực giác** tiếp nhận điểm tựa từ **Context-sensitive và Turing-complete các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trình biên dịch (compiler / 컴파일러) chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chomsky hierarchy là bộ nhớ (memory / 메모리) hierarchy về mặt trực giác

Có thể đọc hierarchy như câu hỏi: recognizer cần bao nhiêu cấu trúc bộ nhớ (memory / 메모리) để phân biệt histories quan trọng? Finite trạng thái (state / 상태) nhớ hữu hạn summary; ngăn xếp (stack / 스택) nhớ nested lịch sử (history / 이력); general tape/bộ nhớ (memory / 메모리) cho computation tổng quát.

Đây là trực giác hữu ích hơn học thuộc Type-3/2/1/0 mà không hiểu cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Ở chặng này của **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**, **Chomsky hierarchy là bộ nhớ (memory / 메모리) hierarchy về mặt trực giác** xác định đầu vào; **Trình biên dịch (compiler / 컴파일러) chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Giao thức (protocol / 프로토콜) và xác minh (verification / 확인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trình biên dịch (compiler / 컴파일러) chuỗi xử lý (pipeline / 파이프라인)

Lexer thường dùng regular machinery để biến characters thành tokens. Parser dùng grammar mạnh hơn để tạo cú pháp (syntax / 문법) cây (tree / 트리). ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석) sau đó cần symbol bảng (table / 테이블), kiểu (type / 타입) môi trường (environment / 환경) và ngữ cảnh (context / 맥락) mà pure CFG không biểu diễn hết.

Việc trình biên dịch (compiler / 컴파일러) chia phases phản ánh hierarchy của thông tin (information / 정보): dùng cơ chế (mechanism / 메커니즘) đơn giản nhất đủ cho từng tầng (layer / 계층) giúp hiện thực (implementation / 구현) dễ lập luận (reasoning / 추론) và tối ưu hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**, **Trình biên dịch (compiler / 컴파일러) chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **Giao thức (protocol / 프로토콜) và xác minh (verification / 확인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Pumping lemma và giới hạn biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giao thức (protocol / 프로토콜) và xác minh (verification / 확인)

Nếu giao thức (protocol / 프로토콜) có thể abstract thành finite states, mô hình (model / 모델) checking có thể explore trạng thái (state / 상태) đồ thị (graph / 그래프) exhaustively trong bound phù hợp. Khi trạng thái (state / 상태) chứa unbounded hàng đợi (queue / 큐)/counter, trạng thái (state / 상태) không gian (space / 공간) có thể vô hạn và xác minh (verification / 확인) cần lớp trừu tượng (abstraction / 추상화).

Do đó chọn mô hình (model / 모델) yếu hơn khi đủ dùng không phải hạn chế; nó tạo khả năng phân tích mạnh hơn.

> **Chuyển mạch:** Trong **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**, **Giao thức (protocol / 프로토콜) và xác minh (verification / 확인)** đã nêu tiêu chí phân biệt, còn **Pumping lemma và giới hạn biểu diễn (representation / 표현)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pumping lemma và giới hạn biểu diễn (representation / 표현)

Pumping lemma có thể chứng minh một số ngôn ngữ (language / 언어) không regular, nhưng nó là necessary thuộc tính (property / 속성) chứ không phải công cụ (tool / 도구) duy nhất. mô hình tư duy (mental model / 사고 모델) quan trọng là finite automaton có hữu hạn states: với đầu vào (input / 입력) đủ dài, trạng thái (state / 상태) phải lặp; machine không thể nhớ arbitrary amount of cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Automata hierarchy, grammars và ngôn ngữ (language / 언어) recognition**, **Pumping lemma và giới hạn biểu diễn (representation / 표현)** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Formal-language hierarchy là hierarchy của bộ nhớ (memory / 메모리) và expressive power. mô hình (model / 모델) càng mạnh, càng mô tả được nhiều computation nhưng càng khó phân tích. kỹ thuật (engineering / 엔지니어링) tốt thường chọn mô hình (model / 모델) yếu nhất vẫn đủ biểu đạt bài toán (problem / 문제) vì restriction tạo ra decidability, tooling và hiệu năng (performance / 성능).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
