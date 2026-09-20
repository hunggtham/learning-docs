# Parsing, AST và language front-end

Compiler/interpreter không thể trực tiếp “hiểu source code” như text tự do. Nó phải biến character stream thành structured representation theo grammar. Quá trình này nối string algorithms, formal languages, trees, semantics và error reporting.

## Từ bytes đến tokens

Lexer/tokenizer (어휘 분석기) nhóm characters thành tokens như identifier, number, keyword, operator.

Ví dụ source:

```text
x = price * 1.1
```

có thể thành:

```text
IDENT(x) ASSIGN IDENT(price) STAR NUMBER(1.1)
```

Lexer cần xử lý longest match, escapes, comments, Unicode identifiers và lexical ambiguity tùy language.

## Grammar mô tả cấu trúc hợp lệ

Parser dùng grammar để xác định sequence tokens có structure nào. Context-free grammar thường đủ cho syntax chính của programming languages.

Ví dụ precedence cần làm `a + b * c` thành `a + (b * c)` thay vì `(a + b) * c`. Grammar hoặc parser strategy encode precedence/associativity.

Recursive descent dễ viết thủ công; LL/LR families dựa trên parsing theory; parser combinators biểu diễn parsers như composable functions.

## Parse tree và AST khác nhau

Concrete parse tree giữ nhiều grammar details như parentheses/nonterminals. Abstract Syntax Tree (AST / 추상 구문 트리) bỏ syntax noise và giữ semantic structure.

Ví dụ `1 + 2 * 3` có AST đại ý:

```text
   +
  / \
 1   *
    / \
   2   3
```

AST là interface giữa syntax và semantic analysis.

## Semantic analysis

Một program có thể parse đúng nhưng semantic sai:

```text
unknownName + 3
```

nếu `unknownName` chưa được declared. Name resolution xây mapping identifiers → declarations/scopes. Type checking xác minh operations phù hợp types. Control-flow analysis có thể kiểm tra unreachable code hoặc definite assignment.

Compiler symbol table là data structure quản lý bindings theo nested scopes.

## Intermediate Representation

AST thường quá gần source và machine code quá gần hardware. Compiler chuyển sang Intermediate Representation (IR / 중간 표현) để optimization/lowering dễ hơn.

IR có thể là three-address code, SSA (Static Single Assignment) hoặc graph-based representation. SSA làm mỗi variable version được assign một lần, giúp data-flow dependencies rõ.

## Error recovery và diagnostics

Parser thực tế không nên dừng ở typo đầu tiên nếu IDE cần hiển thị nhiều errors. Error recovery cố tìm synchronization point và tiếp tục parse.

Diagnostic tốt cần source span, expected tokens, context và đôi khi fix suggestion. Đây là nơi compiler construction gặp HCI: error message là user interface cho programming language.

## Incremental parsing

IDE không muốn parse toàn file từ đầu sau mỗi keystroke. Incremental parser tái sử dụng tree parts không thay đổi. Tree-sitter là ví dụ ecosystem dùng incremental concrete syntax trees.

Pattern “reuse unaffected state after local change” giống incremental build, cache invalidation và reactive UI.

## Parsing ngoài compiler

JSON/XML parsers, SQL parser, command-line shell, config language và network protocol decoders đều áp dụng concepts tương tự: tokenize/parse/validate/construct structured data.

Security concern quan trọng là parser differential: hai components parse cùng bytes khác nhau có thể tạo vulnerability, ví dụ HTTP request smuggling.

## Common Misconceptions

**“Regex có thể parse mọi programming language.”** Regex thường phù hợp lexical patterns; nested recursive structure cần grammar mạnh hơn trong general case.

**“AST chính là source code dưới dạng tree.”** AST intentionally bỏ nhiều syntactic details và có thể normalize nhiều surface forms thành cùng structure.

**“Parse thành công nghĩa là program hợp lệ.”** Semantic checks còn phải xác minh names, types và language rules.

## Mental Model

> Language front-end là chuỗi transformations bảo toàn meaning ngày càng rõ hơn: characters → tokens → syntax tree → semantically annotated representation → IR.

## Kết nối

Xem [string algorithms](../01_algorithms_data_structures/09_string_algorithms_and_text_indexing.md), [compiler/VM/JIT](./03_compilers_interpreters_vm_and_jit.md) và [automata/formal languages](../../mathematics/07_discrete_cs/07_automata_formal_languages_and_computability.md).