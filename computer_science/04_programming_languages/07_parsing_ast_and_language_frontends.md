# Parsing, AST và ngôn ngữ (language / 언어) front-end

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Parsing, AST và language front-ends**. Route đi từ bytes/chars → tokens → grammar/parser → AST/name resolution, để frontend giữ được cả cấu trúc cú pháp lẫn ngữ nghĩa cần cho compiler.

Trình biên dịch (compiler / 컴파일러)/trình thông dịch (interpreter / 인터프리터) không thể trực tiếp “hiểu mã nguồn (source code / 소스 코드)” như văn bản (text / 텍스트) tự do. Nó phải biến character stream thành structured biểu diễn (representation / 표현) theo grammar. Quá trình này nối string algorithms, formal languages, trees, ngữ nghĩa (semantics / 의미론) và lỗi (error / 오류) reporting.

## Từ bytes đến tokens

Lexer/tokenizer (어휘 분석기) nhóm characters thành tokens như identifier, number, từ khóa (keyword / 키워드), operator.

Ví dụ nguồn (source / 소스):

```text
x = price * 1.1
```

có thể thành:

```text
IDENT(x) ASSIGN IDENT(price) STAR NUMBER(1.1)
```

Lexer cần xử lý longest match, escapes, comments, Unicode identifiers và lexical ambiguity tùy ngôn ngữ (language / 언어).

> **Nối mạch:** **Grammar mô tả cấu trúc hợp lệ** nối từ **Từ bytes đến tokens** sang **Parse cây (tree / 트리) và AST khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## Grammar mô tả cấu trúc hợp lệ

Parser dùng grammar để xác định chuỗi (sequence / 시퀀스) tokens có cấu trúc (structure / 구조) nào. Context-free grammar thường đủ cho cú pháp (syntax / 문법) chính của programming languages.

Ví dụ precedence cần làm `a + b * c` thành `a + (b * c)` thay vì `(a + b) * c`. Grammar hoặc parser chiến lược (strategy / 전략) encode precedence/associativity.

Recursive descent dễ viết thủ công; LL/LR families dựa trên parsing lý thuyết (theory / 이론); parser combinators biểu diễn parsers như composable functions.

> **Nối mạch:** **Parse cây (tree / 트리) và AST khác nhau** nối từ **Grammar mô tả cấu trúc hợp lệ** sang **Ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Parse cây (tree / 트리) và AST khác nhau

Concrete parse cây (tree / 트리) giữ nhiều grammar details như parentheses/nonterminals. Abstract cú pháp (syntax / 문법) cây (tree / 트리) bỏ cú pháp (syntax / 문법) noise và giữ ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조).

Ví dụ `1 + 2 * 3` có AST đại ý:

```text
   +
  / \
 1   *
    / \
   2   3
```

AST là giao diện (interface / 인터페이스) giữa cú pháp (syntax / 문법) và ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석).

> **Nối mạch:** **Ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석)** nối từ **Parse cây (tree / 트리) và AST khác nhau** sang **Intermediate biểu diễn (representation / 표현)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석)

Một program có thể parse đúng nhưng ngữ nghĩa (semantic / 의미적) sai:

```text
unknownName + 3
```

nếu `unknownName` chưa được declared. Name resolution xây ánh xạ (mapping / 매핑) identifiers → declarations/scopes. kiểu (type / 타입) checking xác minh operations phù hợp types. Control-flow phân tích (analysis / 분석) có thể kiểm tra unreachable mã (code / 코드) hoặc definite assignment.

Trình biên dịch (compiler / 컴파일러) symbol bảng (table / 테이블) là cấu trúc dữ liệu (data structure / 자료구조) quản lý bindings theo nested scopes.

> **Nối mạch:** **Intermediate biểu diễn (representation / 표현)** nối từ **Ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석)** sang **Lỗi (error / 오류) khôi phục (recovery / 복구) và diagnostics**, vì cơ chế trước tạo đầu vào cho bước sau.

## Intermediate biểu diễn (representation / 표현)

AST thường quá gần nguồn (source / 소스) và mã máy (machine code / 기계어) quá gần hardware. trình biên dịch (compiler / 컴파일러) chuyển sang Intermediate biểu diễn (representation / 표현) để tối ưu hóa (optimization / 최적화)/lowering dễ hơn.

IR có thể là three-address mã (code / 코드), SSA (Static Single Assignment) hoặc graph-based biểu diễn (representation / 표현). SSA làm mỗi variable phiên bản (version / 버전) được assign một lần, giúp data-flow dependencies rõ.

> **Nối mạch:** **Lỗi (error / 오류) khôi phục (recovery / 복구) và diagnostics** nối từ **Intermediate biểu diễn (representation / 표현)** sang **Incremental parsing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lỗi (error / 오류) khôi phục (recovery / 복구) và diagnostics

Parser thực tế không nên dừng ở typo đầu tiên nếu IDE cần hiển thị nhiều errors. lỗi (error / 오류) khôi phục (recovery / 복구) cố tìm synchronization điểm (point / 지점) và tiếp tục parse.

Diagnostic tốt cần nguồn (source / 소스) span, expected tokens, ngữ cảnh (context / 맥락) và đôi khi fix suggestion. Đây là nơi trình biên dịch (compiler / 컴파일러) construction gặp HCI: lỗi (error / 오류) message là người dùng (user / 사용자) giao diện (interface / 인터페이스) cho programming ngôn ngữ (language / 언어).

> **Nối mạch:** **Incremental parsing** nối từ **Lỗi (error / 오류) khôi phục (recovery / 복구) và diagnostics** sang **Parsing ngoài trình biên dịch (compiler / 컴파일러)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Incremental parsing

IDE không muốn parse toàn tệp (file / 파일) từ đầu sau mỗi keystroke. Incremental parser tái sử dụng cây (tree / 트리) parts không thay đổi. Tree-sitter là ví dụ ecosystem dùng incremental concrete cú pháp (syntax / 문법) trees.

Mẫu (pattern / 패턴) “reuse unaffected trạng thái (state / 상태) after cục bộ (local / 로컬) thay đổi (change / 변경)” giống incremental bản dựng (build / 빌드), bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화) và reactive UI.

> **Nối mạch:** **Parsing ngoài trình biên dịch (compiler / 컴파일러)** nối từ **Incremental parsing** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Parsing ngoài trình biên dịch (compiler / 컴파일러)

JSON/XML parsers, SQL parser, command-line shell, cấu hình (config / 설정) ngôn ngữ (language / 언어) và mạng (network / 네트워크) giao thức (protocol / 프로토콜) decoders đều áp dụng concepts tương tự: tokenize/parse/validate/construct structured dữ liệu (data / 데이터).

Bảo mật (security / 보안) concern quan trọng là parser differential: hai components parse cùng bytes khác nhau có thể tạo vulnerability, ví dụ HTTP yêu cầu (request / 요청) smuggling.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Parsing ngoài trình biên dịch (compiler / 컴파일러)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Regex có thể parse mọi programming ngôn ngữ (language / 언어).”** Regex thường phù hợp lexical patterns; nested recursive cấu trúc (structure / 구조) cần grammar mạnh hơn trong general trường hợp (case / 사례).

**“AST chính là mã nguồn (source code / 소스 코드) dưới dạng cây (tree / 트리).”** AST intentionally bỏ nhiều syntactic details và có thể normalize nhiều surface forms thành cùng cấu trúc (structure / 구조).

**“Parse thành công nghĩa là program hợp lệ.”** ngữ nghĩa (semantic / 의미적) checks còn phải xác minh names, types và ngôn ngữ (language / 언어) rules.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> ngôn ngữ (language / 언어) front-end là chuỗi transformations bảo toàn meaning ngày càng rõ hơn: characters → tokens → cú pháp (syntax / 문법) cây (tree / 트리) → semantically annotated biểu diễn (representation / 표현) → IR.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Xem [string algorithms](../01_algorithms_data_structures/09_string_algorithms_and_text_indexing.md), [compiler/VM/JIT](./03_compilers_interpreters_vm_and_jit.md) và [automata/formal languages](../../mathematics/07_discrete_cs/07_automata_formal_languages_and_computability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
