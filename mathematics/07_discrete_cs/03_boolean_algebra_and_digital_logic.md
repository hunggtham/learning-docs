# Boolean algebra và logic số: từ mệnh đề đến circuit và computation

Boolean algebra (불 대수 / Boolean algebra) là một algebra của hai trạng thái, thường biểu diễn bằng `false/true` hoặc `0/1`. Nó nằm ở giao điểm của logic, discrete mathematics, programming và digital hardware.

Điều quan trọng không phải chỉ nhớ AND/OR/NOT, mà hiểu ba layer khác nhau:

```text
logical meaning
→ algebraic representation
→ computational / circuit implementation
```

Một expression có thể truth-equivalent với expression khác nhưng runtime behavior vẫn khác nếu language có short-circuit, side effects hoặc nullable logic.

## 1. Boolean value là một model của decision state

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

đảo truth value.

AND (논리곱 / conjunction):

```math
P\land Q
```

đúng khi cả hai đúng.

OR (논리합 / disjunction):

```math
P\lor Q
```

trong logic toán là inclusive OR: đúng nếu ít nhất một operand đúng.

XOR (배타적 논리합 / exclusive OR):

```math
P\oplus Q
```

đúng khi chính xác một trong hai đúng.

## 3. Truth table là exhaustive finite proof

Với `n` Boolean inputs có

```math
2^n
```

possible assignments.

Truth table liệt kê output trên tất cả assignments. Vì state space hữu hạn, nếu hai expressions có cùng output trên mọi row, ta đã chứng minh chúng equivalent trong propositional Boolean logic.

Đây là một dạng brute-force proof.

Nhưng cost tăng exponential theo `n`, nên truth tables không scale cho logic lớn. Điều này dẫn tới symbolic simplification, SAT solving và formal methods.

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

Cùng structure xuất hiện trong set theory:

```math
(A\cap B)^c=A^c\cup B^c.
```

Đây không phải coincidence: set membership là Boolean predicate.

## 5. Boolean algebra identities không phải list rời rạc

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

Absorption có intuition rõ: nếu `P` đã true, thêm case “P và Q” không mở rộng truth set của `P`.

## 6. Algebraic representation với 0/1

Nếu encode false/true bằng 0/1, một số operations có arithmetic-like forms:

```math
P\land Q=PQ
```

và XOR tương ứng addition modulo 2:

```math
P\oplus Q=P+Q\pmod 2.
```

Boolean OR không đơn giản là ordinary addition vì `1+1=2`, trong khi `1 OR 1=1`. Một polynomial representation là:

```math
P\lor Q=P+Q-PQ
```

trên values `0,1`.

Điều này cho thấy Boolean logic có thể được study algebraically.

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

Đây chính là addition trong field `GF(2)` ở mức bit.

Connection này rất quan trọng trong coding theory, parity checks, linear feedback systems và binary linear algebra.

## 8. Functionally complete gate sets

NAND:

```math
P\uparrow Q=\neg(P\land Q)
```

NOR:

```math
P\downarrow Q=\neg(P\lor Q).
```

Mỗi loại gate riêng có thể build mọi Boolean function, tức functionally complete.

Ví dụ từ NAND:

```math
\neg P=P\uparrow P.
```

Sau đó dùng NAND của các NAND để reconstruct AND/OR.

Ý nghĩa engineering: hardware architecture có thể chuẩn hóa primitive gate rồi synthesize logic phức tạp.

## 9. Sum-of-products và product-of-sums

Mọi Boolean function hữu hạn có thể viết bằng canonical forms.

Sum-of-products (SOP) lấy OR của các AND terms corresponding các truth-table rows output 1.

Product-of-sums (POS) dùng AND của OR clauses corresponding rows output 0.

Đây là bridge từ truth table sang circuit synthesis và SAT/CNF reasoning.

## 10. CNF và SAT

Conjunctive Normal Form (CNF) là AND của clauses, mỗi clause là OR của literals.

Ví dụ:

```math
(P\lor\neg Q)\land(R\lor Q).
```

SAT problem hỏi có assignment nào làm toàn formula true không.

SAT là một trong những central problems của theoretical CS. Dù worst-case exponential theo known complexity theory, modern SAT solvers cực mạnh trên nhiều practical instances nhờ propagation, conflict learning và heuristics.

Boolean algebra vì vậy nối trực tiếp sang complexity và verification.

## 11. Short-circuit semantics: logical equivalence không luôn là operational equivalence

Trong nhiều languages:

```text
A && B
```

không evaluate `B` nếu `A` false.

Trong pure Boolean algebra:

```math
A\land B=B\land A.
```

Nhưng nếu `A` hoặc `B` có side effects, exceptions hoặc expensive computation, đổi order có thể đổi runtime behavior.

Do đó cần tách:

```text
truth semantics
vs
execution semantics
```

## 12. Three-valued logic và NULL

SQL không dùng Boolean hai-valued đơn giản khi có `NULL`; nó dùng three-valued logic với `UNKNOWN`.

Ví dụ:

```sql
NULL = 5
```

không trả `FALSE` mà conceptually `UNKNOWN`.

Vì vậy transformation Boolean textbook có thể cần caution trong SQL predicates.

`NOT UNKNOWN` vẫn `UNKNOWN`.

Đây là ví dụ domain semantics mở rộng Boolean model.

## 13. Bitwise operations

Bitwise AND/OR/XOR apply từng bit của integer representation.

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

Check WRITE:

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

có thể là bitwise hoặc non-short-circuit Boolean tùy language/type.

Không được swap operators chỉ vì truth table trên pure booleans trông giống nhau.

## 15. Boolean minimization

Simplification có hai goals khác nhau:

```text
hardware → ít gates / delay / power
software → readability / maintainability / fewer branches
```

Karnaugh maps giúp visualize adjacent minterms khác một bit để combine.

Algorithmic synthesis dùng Quine–McCluskey hoặc modern logic synthesis methods.

Nhưng minimal gate expression không nhất thiết là readable business rule.

## 16. Worked Example: simplify business rule

Cho rule:

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

Logic đúng, nhưng production code còn phải xét role hierarchy, nullable state và side-effect permission checks.

## 17. Worked Example: parity

Parity của bits:

```math
p=b_1\oplus b_2\oplus\cdots\oplus b_n.
```

`p=1` nếu số bit 1 là odd.

Nếu một single bit flip xảy ra, parity đổi, nên detect được single-bit error.

Nhưng hai bit flips có thể giữ parity, nên parity check không detect mọi error.

Đây là lesson chung: algebraic invariant có detection power cụ thể, không phải guarantee universal.

## 18. Boolean matrix và graph reachability

Adjacency matrix `A` của graph có thể được interpreted trên Boolean semiring:

```text
addition → OR
multiplication → AND
```

Khi đó powers của adjacency matrix encode existence của paths theo Boolean composition.

Điều này cho thấy cùng matrix syntax có thể chạy trên algebra khác nhau và meaning thay đổi theo operations nền.

## 19. Connection với AI

Decision trees, binary masks, attention masks và thresholded predicates đều dùng Boolean structure.

Nhưng neural networks chủ yếu dùng continuous differentiable computation; Boolean decisions thường xuất hiện ở data preprocessing, masking hoặc discrete control layer.

Một hard Boolean threshold mất gradient, nên training differentiable systems thường dùng soft approximations như sigmoid/softmax trước khi discretize.

## 20. Connection với hardware

Transistor networks implement switching behavior. Logic gates abstract physical voltage ranges thành discrete states.

Boolean model bỏ qua analog effects như propagation delay, noise margin và metastability. Digital logic correctness vẫn cần timing/electrical assumptions.

## Mental Model

> Boolean algebra là algebra của predicates và decisions. Truth table cho semantics; algebraic identities cho transformation; gates/bit operations cho implementation. Cùng expression có ba mặt: nó nghĩa gì, nó được simplify thế nào, và máy thực thi nó ra sao.

## Common Misconceptions

**“OR nghĩa exactly one true.”** Không; đó là XOR.

**“Truth-equivalent code luôn runtime-equivalent.”** Không nếu có short-circuit/side effects.

**“Bitwise và logical operators interchangeable.”** Không.

**“NULL trong SQL chỉ là false.”** Không; nó tạo unknown semantics.

**“Parity detect mọi corruption.”** Không; detection capability phụ thuộc error pattern.
