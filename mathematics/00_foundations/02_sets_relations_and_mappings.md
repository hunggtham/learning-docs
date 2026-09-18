# Tập hợp, quan hệ và ánh xạ

Tập hợp (Set / 집합) là một cách gom các đối tượng theo membership. Ý tưởng nghe đơn giản nhưng nó là hạ tầng chung cho phần lớn toán học hiện đại: domain của hàm là một set, solution của equation là một set, rows thỏa `WHERE` tạo một subset của table result, và probability event cũng được mô hình hóa như subset của sample space.

## Membership

Nếu `x` thuộc set `A`, viết

```math
x\in A.
```

Nếu không:

```math
x\notin A.
```

Set quan tâm membership chứ không quan tâm order và duplicate theo definition thông thường. `{1,2,2,3}` biểu diễn cùng set với `{1,2,3}`.

Điều này khác list/array trong programming, nơi order và duplicates thường có ý nghĩa.

## Subset

`A` là subset của `B` nếu mọi element của `A` cũng thuộc `B`:

```math
A\subseteq B.
```

Nếu `A⊆B` và `B⊆A` thì

```math
A=B.
```

Đây là phương pháp phổ biến để chứng minh hai sets bằng nhau: chứng minh containment theo cả hai hướng.

## Empty set

Tập rỗng (Empty set / 공집합)

```math
\varnothing
```

không có element nào.

Nó là subset của mọi set. Lý do đến từ logic: để bác bỏ `∅⊆A`, cần tìm một element thuộc `∅` nhưng không thuộc `A`; nhưng không có element nào để làm counterexample.

## Union, intersection và difference

Hợp (Union / 합집합):

```math
A\cup B
```

gồm elements thuộc `A` hoặc `B` hoặc cả hai.

Giao (Intersection / 교집합):

```math
A\cap B
```

gồm elements thuộc cả hai.

Hiệu (Set difference / 차집합):

```math
A\setminus B
```

gồm elements thuộc `A` nhưng không thuộc `B`.

Các operations này có connection trực tiếp với boolean logic và database filtering.

## Complement

Nếu có universe `U`, complement của `A` là

```math
A^c=U\setminus A.
```

De Morgan:

```math
(A\cup B)^c=A^c\cap B^c
```

```math
(A\cap B)^c=A^c\cup B^c.
```

Cấu trúc này giống boolean conditions vì membership có thể xem như true/false.

## Cartesian product

Tích Descartes (Cartesian product / 데카르트 곱)

```math
A\times B
```

là set của ordered pairs `(a,b)` với `a∈A,b∈B`.

Nếu

```text
A={1,2}
B={x,y}
```

thì

```text
A×B={(1,x),(1,y),(2,x),(2,y)}
```

Cartesian product là nền để định nghĩa relation và function.

## Relation

Quan hệ (Relation / 관계) từ `A` tới `B` là một subset của

```math
A\times B.
```

Tức relation chỉ định cặp nào được xem là có liên hệ.

Ví dụ relation “user follows user” trong social network là subset của

```text
Users × Users
```

Relation “employee worksFor company” là subset của

```text
Employees × Companies.
```

Database relation trong relational model có conceptual connection với set of tuples, mặc dù SQL implementation có thêm concerns như duplicates và NULL.

## Equivalence relation

Một equivalence relation (Quan hệ tương đương / 동치관계) có ba properties:

- reflexive: `a~a`;
- symmetric: `a~b ⇒ b~a`;
- transitive: `a~b` và `b~c ⇒ a~c`.

Nó partition set thành equivalence classes.

Ví dụ integers cùng remainder modulo 3:

```math
a\sim b
\iff
3\mid(a-b).
```

Mỗi integer rơi vào một trong ba classes remainder `0,1,2`.

Đây là nền cho modular arithmetic.

## Order relation

Quan hệ thứ tự (Order relation / 순서관계) mô tả notion “trước/sau”, “nhỏ/lớn” hoặc dependency.

Partial order không yêu cầu mọi pair đều comparable. Trong Git commit DAG, một commit có thể là ancestor của commit khác, nhưng hai commits ở hai branches có thể không phải ancestor của nhau. Dependency graphs và package version constraints thường có structures gần partial order.

## Mapping và function

Ánh xạ (Mapping / 사상) gán elements từ một set tới set khác. Function là mapping với requirement rằng mỗi input trong domain có chính xác một output.

Viết

```math
f:A\to B.
```

`A` là domain, `B` là codomain.

Function có thể được xem như một special relation `R⊆A×B` sao cho với mỗi `a∈A`, tồn tại đúng một pair `(a,b)` trong relation.

Điều này giúp thấy function không nhất thiết phải là formula. Lookup table, hash function, image transformation và trained ML model đều có thể được xem như mappings.

## Injective, surjective, bijective

Injective (Đơn ánh / 단사) nghĩa different inputs không collapse vào cùng output:

```math
f(a)=f(b)\Rightarrow a=b.
```

Surjective (Toàn ánh / 전사) nghĩa mọi element trong codomain được hit bởi ít nhất một input.

Bijective (Song ánh / 전단사) nghĩa cả injective và surjective.

Bijective function có inverse function trên codomain tương ứng, vì mỗi output có exactly one input nguồn.

Trong data engineering, unique identifier gần với injectivity: nếu hai entities khác nhau nhận cùng ID, information bị mất. Compression lossless cần mapping đủ để recover original data, conceptually liên quan invertibility.

## Cardinality

Lực lượng (Cardinality / 기수) đo số lượng elements trong set.

Với finite sets, đó đơn giản là count. Với infinite sets, tình hình thú vị hơn. Natural numbers và even numbers có cùng cardinality vì mapping

```math
n\mapsto2n
```

là bijection, dù even numbers có vẻ chỉ là “một nửa” natural numbers.

Đây là một ví dụ cho thấy intuition hữu hạn không phải lúc nào kéo sang vô hạn được.

## Power set

Power set `P(A)` là set của mọi subsets của `A`.

Nếu `A` có `n` elements:

```math
|\mathcal P(A)|=2^n.
```

Lý do: mỗi element có hai choices độc lập — include hoặc exclude. Với `n` elements, số bit patterns là `2^n`.

Connection với computing rất trực tiếp: một subset của `n` flags có thể được represent bằng `n` bits.

## Mental Model

> Set trả lời “những object nào đang nằm trong universe của ta?”. Relation trả lời “những pairs nào được nối với nhau?”. Function là relation có kỷ luật hơn: mỗi input đi tới đúng một output. Từ ba ý tưởng này có thể xây database relation, graph, probability event, state transition và nhiều cấu trúc khác.

## Common Misconceptions

Codomain không nhất thiết bằng actual image của function. Function injective không có nghĩa surjective. Set không phải list: order và duplicate không thuộc bản chất của ordinary set. Với infinite sets, “subset nhỏ hơn” không nhất thiết có cardinality nhỏ hơn.
