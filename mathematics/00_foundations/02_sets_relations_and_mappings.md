# Tập hợp, quan hệ và ánh xạ: từ membership đến cấu trúc

Tập hợp (set / 집합), quan hệ (relation / 관계) và ánh xạ (mapping / 사상) là ba lớp abstraction xuất hiện gần như khắp toán học và Computer Science. Set trả lời **đối tượng nào đang thuộc universe ta xét**. Relation trả lời **những cặp nào được xem là có liên hệ**. Function/mapping thêm discipline: **mỗi input phải đi tới đúng một output**.

Điểm quan trọng là ba concept này không phải ba chapter rời nhau. Chúng tạo một dependency chain:

```text
membership
→ subset
→ product space
→ relation
→ equivalence / order
→ function
→ injective / surjective / bijective
→ quotient / inverse / structure preservation
```

## 1. Set là abstraction về membership

Nếu `x` thuộc set `A`:

```math
x\in A.
```

Nếu không:

```math
x\notin A.
```

Ordinary set không quan tâm order hay duplicate. `{1,2,2,3}` biểu diễn cùng set với `{1,2,3}`.

Điều này khác list/array, nơi order và multiplicity thường là part of meaning.

Set abstraction mạnh vì nó cho phép ta tách **identity của elements** khỏi **cách lưu trữ chúng**. Trong probability, event là subset của sample space. Trong optimization, feasible set chứa mọi decision hợp lệ. Trong databases, một query predicate chọn một subset của rows về mặt conceptual, dù SQL thực tế có bag semantics và NULL.

## 2. Subset: universal statement dưới dạng set language

`A` là subset của `B` nếu

```math
A\subseteq B
```

nghĩa là

```math
\forall x\;(x\in A\Rightarrow x\in B).
```

Đây là connection trực tiếp giữa set theory và logic.

Muốn chứng minh hai sets bằng nhau, strategy canonical là **double inclusion**:

```text
A ⊆ B
B ⊆ A
```

Vì set được xác định hoàn toàn bởi membership, nếu hai sets chứa đúng cùng elements thì chúng bằng nhau.

## 3. Empty set và vacuous truth

Tập rỗng (empty set / 공집합)

```math
\varnothing
```

là subset của mọi set.

Lý do không phải convention tùy ý. `∅⊆A` nghĩa:

```math
\forall x\;(x\in\varnothing\Rightarrow x\in A).
```

Không có `x` nào thuộc `∅`, nên không tồn tại counterexample làm implication sai.

Đây là ví dụ quan trọng của vacuous truth. Cùng pattern xuất hiện trong graph theory, universal quantification và proofs trên empty structures.

## 4. Union, intersection, difference và complement

Union:

```math
A\cup B
```

chứa elements thuộc `A` hoặc `B` hoặc cả hai.

Intersection:

```math
A\cap B
```

chứa elements thuộc cả hai.

Difference:

```math
A\setminus B
```

chứa elements thuộc `A` nhưng không thuộc `B`.

Nếu có universe `U`, complement:

```math
A^c=U\setminus A.
```

Membership biến các identities này thành Boolean logic. Ví dụ:

```math
x\in(A\cap B)
\iff
(x\in A)\land(x\in B).
```

Do đó De Morgan cho sets:

```math
(A\cup B)^c=A^c\cap B^c
```

và

```math
(A\cap B)^c=A^c\cup B^c.
```

không phải hai formula ngẫu nhiên; chúng là De Morgan logic applied vào membership predicates.

## 5. Cartesian product tạo không gian của possible pairs

Tích Descartes (Cartesian product / 데카르트 곱):

```math
A\times B
=
\{(a,b):a\in A,b\in B\}.
```

Nếu

```text
A={1,2}
B={x,y}
```

thì

```text
A×B={(1,x),(1,y),(2,x),(2,y)}.
```

Cartesian product quan trọng vì nó tạo universe cho relation.

Ví dụ:

```text
Users × Products
```

là mọi user-product pairs có thể có. “User purchased product” chỉ chọn một subset của possible pairs đó.

Trong probability, joint sample space thường là product của component spaces khi model phù hợp. Trong state machines, state-action pairs cũng có product structure.

## 6. Relation là subset của product space

Một binary relation `R` từ `A` tới `B` là

```math
R\subseteq A\times B.
```

Nếu `(a,b)∈R`, ta nói `a` liên hệ với `b`.

Ví dụ relation “employee works for company” là subset của

```text
Employees × Companies.
```

Relation “user follows user” là subset của

```text
Users × Users.
```

Graph directed cũng có thể nhìn như relation trên vertices: edge `(u,v)` nghĩa `uRv`.

Đây là reason graph theory, database relations và order relations có family resemblance: tất cả đều bắt đầu từ **which tuples are allowed**.

## 7. Properties của relation và ý nghĩa structural

### Reflexive

```math
aRa
```

cho mọi `a`.

### Symmetric

```math
aRb\Rightarrow bRa.
```

### Antisymmetric

```math
aRb\land bRa\Rightarrow a=b.
```

Antisymmetric không có nghĩa “không symmetric”; nó nói mutual relation giữa distinct elements bị cấm.

### Transitive

```math
aRb\land bRc\Rightarrow aRc.
```

Những properties này không chỉ là checklist. Chúng quyết định relation tạo ra structure gì.

## 8. Equivalence relation: formal hóa “khác representation nhưng cùng object class”

Equivalence relation (quan hệ tương đương / 동치관계) là reflexive, symmetric và transitive.

Ví dụ modulo 3:

```math
a\sim b
\iff
3\mid(a-b).
```

Integers được partition thành ba equivalence classes:

```text
[0], [1], [2]
```

Mọi integer nằm đúng một class.

Điểm sâu là equivalence relation cho phép ta **collapse details không quan trọng**. Thay vì phân biệt mọi integer, modulo 3 chỉ giữ remainder class.

Cùng idea xuất hiện khi:

- coi fractions `1/2` và `2/4` là cùng rational number;
- coi vectors khác nhau bởi một transformation nào đó là same orbit/class;
- quotient spaces trong algebra/topology;
- canonicalization trong software.

## 9. Partial order: formal hóa dependency và hierarchy

Partial order (thứ tự bộ phận / 부분순서) thường reflexive, antisymmetric và transitive.

Không phải mọi pair đều cần comparable.

Ví dụ set inclusion:

```math
A\subseteq B
```

là partial order trên power set.

Dependency relations cũng thường partial-order-like khi không có cycles. Hai tasks độc lập có thể không đứng trước/sau nhau.

Total order thêm requirement rằng mọi pair comparable. Number line với `≤` là total order; dependency DAG nói chung không phải total order.

## 10. Function là relation có tính đơn trị toàn phần

Function

```math
f:A\to B
```

có thể được xem là relation `R⊆A×B` thỏa:

1. với mọi `a∈A`, tồn tại output;
2. output đó là duy nhất.

Nói cách khác, mỗi input có **exactly one** output.

Function không cần formula. Lookup table, parser, database projection, image transform hay trained model đều có thể là functions nếu mapping deterministic trong model đang xét.

## 11. Domain, codomain và image không thể bỏ qua

Trong

```math
f:A\to B,
```

`A` là domain, `B` là codomain.

Image/range là subset của `B` thực sự được hit:

```math
f(A)=\{f(a):a\in A\}.
```

Cùng formula nhưng khác domain/codomain có thể là functions khác nhau về structural properties.

Ví dụ `f(x)=x^2`:

```math
f:\mathbb R\to\mathbb R
```

không surjective.

Nhưng

```math
f:[0,\infty)\to[0,\infty)
```

là bijective.

Vì vậy domain/codomain không phải metadata phụ.

## 12. Injective, surjective, bijective như information behavior

Injective (đơn ánh / 단사):

```math
f(a)=f(b)\Rightarrow a=b.
```

Different inputs không collapse vào cùng output. Theo information viewpoint, injective mapping không mất distinction giữa inputs.

Surjective (toàn ánh / 전사): mọi output trong codomain reachable.

Bijective (song ánh / 전단사): vừa injective vừa surjective.

Bijective mapping có inverse:

```math
f^{-1}:B\to A.
```

Đây là lý do invertibility gắn với information preservation.

Lossless encoding cần recovery mapping; unique IDs cần injectivity; coordinate changes dùng bijections trên suitable domains.

## 13. Composition: nối mappings thành pipeline

Nếu

```math
f:A\to B,
\qquad
g:B\to C,
```

thì

```math
(g\circ f)(x)=g(f(x)).
```

Composition là ngôn ngữ của pipelines.

Trong software:

```text
raw input
→ parse
→ validate
→ transform
→ serialize
```

Trong neural networks, layers compose thành model. Trong geometry, transformations compose. Trong category theory, composition trở thành central primitive.

Composition generally không commutative:

```math
g\circ f\ne f\circ g.
```

Order matters vì intermediate spaces/meaning khác nhau.

## 14. Cardinality: đo size bằng bijection

Với finite sets, cardinality chỉ là count.

Với infinite sets, definition bằng bijection trở nên sâu hơn. Natural numbers và even numbers có cùng cardinality vì

```math
n\mapsto 2n
```

là bijection.

Điều này phá intuition hữu hạn “proper subset luôn nhỏ hơn”.

Cantor's diagonal idea còn cho thấy power set của một set có cardinality strictly lớn hơn chính set đó:

```math
|A|<|\mathcal P(A)|.
```

Với finite set `|A|=n`:

```math
|\mathcal P(A)|=2^n
```

vì mỗi element tương ứng một include/exclude bit.

## 15. Power set và state-space explosion

Power set không chỉ là concept pure math. Nếu system có `n` Boolean flags, mỗi subset các flags-on là một state, nên có

```math
2^n
```

possible states.

Đây là source của combinatorial explosion trong exhaustive search, feature subsets, access combinations và state verification.

Set theory vì vậy nối trực tiếp sang complexity.

## 16. Database connection: relation toán học và SQL relation không hoàn toàn giống nhau

Relational model toán học gần với set of tuples. SQL tables thực tế có thể cho duplicate rows và `NULL`, nên SQL semantics không trùng set theory thuần.

Điều này là ví dụ quan trọng của model layering:

```text
mathematical relation
≠ implementation data structure
```

Nhưng set/relation thinking vẫn giúp hiểu joins, keys, functional dependencies và normalization.

## 17. Probability connection

Sample space `Ω` là set outcomes; event `A` là subset:

```math
A\subseteq\Omega.
```

Intersection là “A và B”, union là “A hoặc B”, complement là “không A”.

Probability measure gán number cho subsets/events. Vì vậy probability theory xây trực tiếp trên set logic.

Conditional probability còn có thể nhìn như việc **restrict universe sang event B đã biết xảy ra**, rồi renormalize probability trong universe mới.

## 18. Common proof strategies với sets

Để chứng minh

```math
A=B,
```

chọn arbitrary `x`, rồi chứng minh

```math
x\in A\iff x\in B.
```

Hoặc double inclusion.

Để chứng minh two sets disjoint:

```math
A\cap B=\varnothing,
```

show rằng giả sử `x` thuộc cả hai dẫn tới contradiction.

Proof set identities thường trở thành propositional logic sau khi expand membership definitions.

## Mental Model

> Set định nghĩa **universe của objects**. Cartesian product tạo **universe của possible tuples**. Relation chọn **tuples được phép nối**. Equivalence relation gom representations thành classes; partial order tạo hierarchy/dependency; function ép mỗi input đi tới đúng một output. Phần lớn cấu trúc toán học cao hơn chỉ là thêm rules lên những nền này.

## Common Misconceptions

Set không phải list: order và duplicates không thuộc ordinary set. `A⊂B` convention có thể khác textbook về proper subset, nên nên dùng ký hiệu rõ. Antisymmetric không phải opposite của symmetric. Codomain không nhất thiết bằng image. Injective không imply surjective. Với infinite sets, proper subset có thể có cùng cardinality với parent set.