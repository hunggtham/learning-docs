# Boolean algebra và lô-gic (logic / 논리) số: từ mệnh đề đến circuit và computation

> **Mạch đọc:** Đọc **Boolean algebra và lô-gic (logic / 논리) số: từ mệnh đề đến circuit và computation** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Boolean giá trị (value / 값) là một mô hình (model / 모델) của quyết định (decision / 결정) trạng thái (state / 상태)** sang **2. Basic operations**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Boolean algebra (불 대수 / Boolean algebra) là một algebra của hai trạng thái, thường biểu diễn bằng `false/true` hoặc `0/1`. Nó nằm ở giao điểm của lô-gic (logic / 논리), discrete mathematics, programming và digital hardware.

Điều quan trọng không phải chỉ nhớ AND/OR/NOT, mà hiểu ba tầng (layer / 계층) khác nhau:

```text
logical meaning
→ algebraic representation
→ computational / circuit implementation
```

Một expression có thể truth-equivalent với expression khác nhưng hành vi thời gian chạy (runtime behavior / 런타임 동작) vẫn khác nếu ngôn ngữ (language / 언어) có short-circuit, side effects hoặc nullable lô-gic (logic / 논리).

## 1. Boolean giá trị (value / 값) là một mô hình (model / 모델) của quyết định (decision / 결정) trạng thái (state / 상태)

Ta thường dùng

```text
0 = false
1 = true
```

nhưng `0` và `1` ở đây không nhất thiết mang meaning arithmetic thông thường; chúng đại diện hai truth states.

Boolean variable `P` không “đo” quantity liên tục. Nó trả lời một proposition:

```text
isAuthenticated?
hasPermission?
featureEnabled?
```

## 2. Basic operations

Phủ định (NOT / 부정):

```math
\neg P
```

đảo truth giá trị (value / 값).

AND (논리곱 / conjunction):

```math
P\land Q
```

đúng khi cả hai đúng.

OR (논리합 / disjunction):

```math
P\lor Q
```

trong lô-gic (logic / 논리) toán là inclusive OR: đúng nếu ít nhất một operand đúng.

XOR (배타적 논리합 / exclusive OR):

```math
P\oplus Q
```

đúng khi chính xác một trong hai đúng.

## 3. Truth bảng (table / 테이블) là exhaustive finite proof

Với `n` Boolean inputs có

```math
2^n
```

possible assignments.

Truth bảng (table / 테이블) liệt kê đầu ra (output / 출력) trên tất cả assignments. Vì trạng thái (state / 상태) không gian (space / 공간) hữu hạn, nếu hai expressions có cùng đầu ra (output / 출력) trên mọi row, ta đã chứng minh chúng equivalent trong propositional Boolean lô-gic (logic / 논리).

Đây là một dạng brute-force proof.

Nhưng chi phí (cost / 비용) tăng exponential theo `n`, nên truth tables không quy mô (scale / 규모) cho lô-gic (logic / 논리) lớn. Điều này dẫn tới symbolic simplification, SAT solving và formal methods.

## 4. De Morgan's laws từ viewpoint complement

```math
\neg(P\land Q)
\equiv
\neg P\lor\neg Q
```

```math
\neg(P\lor Q)
\equiv
\neg P\land\neg Q.
```

Intuition:

- “không phải cả hai đều đúng” nghĩa ít nhất một cái sai;
- “không có cái nào đúng” nghĩa cả hai đều sai.

Cùng cấu trúc (structure / 구조) xuất hiện trong set lý thuyết (theory / 이론):

```math
(A\cap B)^c=A^c\cup B^c.
```

Đây không phải coincidence: set membership là Boolean predicate.

## 5. Boolean algebra identities không phải danh sách (list / 목록) rời rạc

Một số identities:

```math
P\lor P=P
```

```math
P\land P=P
```

```math
P\lor(P\land Q)=P
```

```math
P\land(P\lor Q)=P.
```

Absorption có intuition rõ: nếu `P` đã true, thêm trường hợp (case / 사례) “P và Q” không mở rộng truth set của `P`.

## 6. Algebraic biểu diễn (representation / 표현) với 0/1

Nếu encode false/true bằng 0/1, một số operations có arithmetic-like forms:

```math
P\land Q=PQ
```

và XOR tương ứng addition modulo 2:

```math
P\oplus Q=P+Q\pmod 2.
```

Boolean OR không đơn giản là ordinary addition vì `1+1=2`, trong khi `1 OR 1=1`. Một polynomial biểu diễn (representation / 표현) là:

```math
P\lor Q=P+Q-PQ
```

trên values `0,1`.

Điều này cho thấy Boolean lô-gic (logic / 논리) có thể được study algebraically.

## 7. XOR và arithmetic modulo 2

XOR có properties:

```math
x\oplus0=x
```

```math
x\oplus x=0
```

```math
x\oplus y=y\oplus x.
```

Associativity cho phép:

```math
x\oplus y\oplus x=y.
```

Đây chính là addition trong trường dữ liệu (field / 필드) `GF(2)` ở mức bit.

Liên kết (connection / 연결) này rất quan trọng trong coding lý thuyết (theory / 이론), parity checks, tuyến tính (linear / 선형) phản hồi (feedback / 피드백) các hệ thống (systems / 시스템들) và nhị phân (binary / 이진) tuyến tính (linear / 선형) algebra.

## 8. Functionally complete gate sets

NAND:

```math
P\uparrow Q=\neg(P\land Q)
```

NOR:

```math
P\downarrow Q=\neg(P\lor Q).
```

Mỗi loại gate riêng có thể bản dựng (build / 빌드) mọi Boolean hàm (function / 함수), tức functionally complete.

Ví dụ từ NAND:

```math
\neg P=P\uparrow P.
```

Sau đó dùng NAND của các NAND để reconstruct AND/OR.

Ý nghĩa kỹ thuật (engineering / 엔지니어링): hardware kiến trúc (architecture / 아키텍처) có thể chuẩn hóa thành phần nguyên thủy (primitive / 기본 요소) gate rồi synthesize lô-gic (logic / 논리) phức tạp.

## 9. Sum-of-products và product-of-sums

Mọi Boolean hàm (function / 함수) hữu hạn có thể viết bằng chuẩn gốc (canonical / 정본) forms.

Sum-of-products (SOP) lấy OR của các AND terms corresponding các truth-table rows đầu ra (output / 출력) 1.

Product-of-sums (POS) dùng AND của OR clauses corresponding rows đầu ra (output / 출력) 0.

Đây là cầu nối (bridge / 브리지) từ truth bảng (table / 테이블) sang circuit synthesis và SAT/CNF lập luận (reasoning / 추론).

## 10. CNF và SAT

Conjunctive Normal Form (CNF) là AND của clauses, mỗi clause là OR của literals.

Ví dụ:

```math
(P\lor\neg Q)\land(R\lor Q).
```

SAT bài toán (problem / 문제) hỏi có assignment nào làm toàn formula true không.

SAT là một trong những central problems của theoretical CS. Dù worst-case exponential theo known độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론), hiện đại (modern / 현대적) SAT solvers cực mạnh trên nhiều practical instances nhờ propagation, xung đột (conflict / 충돌) học tập (learning / 학습) và heuristics.

Boolean algebra vì vậy nối trực tiếp sang độ phức tạp (complexity / 복잡도) và xác minh (verification / 확인).

## 11. Short-circuit ngữ nghĩa (semantics / 의미론): logical equivalence không luôn là operational equivalence

Trong nhiều languages:

```text
A && B
```

không evaluate `B` nếu `A` false.

Trong pure Boolean algebra:

```math
A\land B=B\land A.
```

Nhưng nếu `A` hoặc `B` có side effects, exceptions hoặc expensive computation, đổi thứ tự (order / 순서) có thể đổi hành vi thời gian chạy (runtime behavior / 런타임 동작).

Do đó cần tách:

```text
truth semantics
vs
execution semantics
```

## 12. Three-valued lô-gic (logic / 논리) và NULL

SQL không dùng Boolean hai-valued đơn giản khi có `NULL`; nó dùng three-valued lô-gic (logic / 논리) với `UNKNOWN`.

Ví dụ:

```sql
NULL = 5
```

không trả `FALSE` mà conceptually `UNKNOWN`.

Vì vậy transformation Boolean textbook có thể cần caution trong SQL predicates.

`NOT UNKNOWN` vẫn `UNKNOWN`.

Đây là ví dụ lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론) mở rộng Boolean mô hình (model / 모델).

## 13. Bitwise operations

Bitwise AND/OR/XOR apply từng bit của integer biểu diễn (representation / 표현).

Ví dụ permissions:

```text
READ  = 001
WRITE = 010
EXEC  = 100
```

Combine:

```text
READ | WRITE = 011
```

Check ghi (write / 쓰기):

```text
mask & WRITE != 0
```

Bit mask là cách đóng gói nhiều Boolean flags vào integer.

## 14. Logical operator khác bitwise operator

Trong nhiều languages:

```text
&& / ||
```

là logical, thường short-circuit.

```text
& / |
```

có thể là bitwise hoặc non-short-circuit Boolean tùy ngôn ngữ (language / 언어)/kiểu (type / 타입).

Không được swap operators chỉ vì truth bảng (table / 테이블) trên pure booleans trông giống nhau.

## 15. Boolean minimization

Simplification có hai goals khác nhau:

```text
hardware → ít gates / delay / power
software → readability / maintainability / fewer branches
```

Karnaugh maps giúp visualize adjacent minterms khác một bit để combine.

Algorithmic synthesis dùng Quine–McCluskey hoặc hiện đại (modern / 현대적) lô-gic (logic / 논리) synthesis methods.

Nhưng minimal gate expression không nhất thiết là readable nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙).

## 16. Worked Example: simplify nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙)

Cho quy tắc (rule / 규칙):

```text
allow = admin OR (active AND owner)
```

Deny:

```text
NOT allow
```

De Morgan:

```text
NOT admin AND NOT(active AND owner)
```

rồi:

```text
NOT admin AND (NOT active OR NOT owner)
```

Lô-gic (logic / 논리) đúng, nhưng môi trường vận hành (production / 운영 환경) mã (code / 코드) còn phải xét role hierarchy, nullable trạng thái (state / 상태) và side-effect permission checks.

## 17. Worked Example: parity

Parity của bits:

```math
p=b_1\oplus b_2\oplus\cdots\oplus b_n.
```

`p=1` nếu số bit 1 là odd.

Nếu một single bit flip xảy ra, parity đổi, nên detect được single-bit lỗi (error / 오류).

Nhưng hai bit flips có thể giữ parity, nên parity check không detect mọi lỗi (error / 오류).

Đây là lesson chung: algebraic bất biến (invariant / 불변식) có detection power cụ thể, không phải guarantee universal.

## 18. Boolean ma trận (matrix / 행렬) và đồ thị (graph / 그래프) reachability

Adjacency ma trận (matrix / 행렬) `A` của đồ thị (graph / 그래프) có thể được interpreted trên Boolean semiring:

```text
addition → OR
multiplication → AND
```

Khi đó powers của adjacency ma trận (matrix / 행렬) encode existence của paths theo Boolean composition.

Điều này cho thấy cùng ma trận (matrix / 행렬) cú pháp (syntax / 문법) có thể chạy trên algebra khác nhau và meaning thay đổi theo operations nền.

## 19. liên kết (connection / 연결) với AI

Quyết định (decision / 결정) trees, nhị phân (binary / 이진) masks, attention masks và thresholded predicates đều dùng Boolean cấu trúc (structure / 구조).

Nhưng neural networks chủ yếu dùng continuous differentiable computation; Boolean decisions thường xuất hiện ở dữ liệu (data / 데이터) preprocessing, masking hoặc discrete điều khiển (control / 제어) tầng (layer / 계층).

Một hard Boolean threshold mất độ dốc (gradient / 기울기), nên huấn luyện (training / 학습) differentiable các hệ thống (systems / 시스템들) thường dùng soft approximations như sigmoid/softmax trước khi discretize.

## 20. liên kết (connection / 연결) với hardware

Transistor networks implement switching hành vi (behavior / 동작). lô-gic (logic / 논리) gates abstract vật lý (physical / 물리적) voltage ranges thành discrete states.

Boolean mô hình (model / 모델) bỏ qua analog effects như propagation delay, noise margin và metastability. Digital lô-gic (logic / 논리) tính đúng đắn (correctness / 정확성) vẫn cần timing/electrical các giả định (assumptions / 가정들).

## Mô hình tư duy (mental model / 사고 모델)

> Boolean algebra là algebra của predicates và decisions. Truth bảng (table / 테이블) cho ngữ nghĩa (semantics / 의미론); algebraic identities cho transformation; gates/bit operations cho hiện thực (implementation / 구현). Cùng expression có ba mặt: nó nghĩa gì, nó được simplify thế nào, và máy thực thi nó ra sao.

## Dùng chung (common / 공통) Misconceptions

**“OR nghĩa exactly one true.”** Không; đó là XOR.

**“Truth-equivalent mã (code / 코드) luôn runtime-equivalent.”** Không nếu có short-circuit/side effects.

**“Bitwise và logical operators interchangeable.”** Không.

**“NULL trong SQL chỉ là false.”** Không; nó tạo unknown ngữ nghĩa (semantics / 의미론).

**“Parity detect mọi corruption.”** Không; detection năng lực (capability / 역량) phụ thuộc lỗi (error / 오류) mẫu (pattern / 패턴).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 graph theory](./00_graph_theory.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
