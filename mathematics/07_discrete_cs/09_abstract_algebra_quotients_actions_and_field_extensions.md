# Abstract algebra nâng cao: quotients, group actions, ideals và field extensions

> **Mạch đọc:** Chapter này tiếp nối [Groups, rings, fields và algebraic structures](./08_groups_rings_fields_and_algebraic_structures.md). Chapter trước trả lời “group/ring/field là gì?”; chapter này hỏi sâu hơn: **làm sao phân rã một structure, quotient phần dư thừa, nhìn symmetry qua action, và xây field lớn hơn để giải equations?**

Abstract algebra trở nên mạnh khi ta thôi xem group/ring/field như một collection definitions và bắt đầu dùng **structure-preserving maps** để so sánh objects. Ba ideas xuyên suốt là:

```text
substructure
→ quotient
→ homomorphism/isomorphism
```

và một direction khác:

```text
group
→ acts on another set
→ orbits + stabilizers reveal symmetry
```

Cuối cùng với fields:

```text
polynomial has no root in current field
→ extend the field
→ study how roots can be permuted while preserving algebra
→ Galois theory
```

## 1. Cosets: nhìn group theo các bản dịch của subgroup

Cho subgroup `H≤G`. Với `g\in G`, **left coset / 왼쪽 잉여류** là

```math
gH=\{gh:h\in H\}.
```

Tương tự right coset:

```math
Hg=\{hg:h\in H\}.
```

Trong additive group `\mathbb Z`, lấy subgroup `3\mathbb Z`. Cosets là

```math
0+3\mathbb Z,
\quad
1+3\mathbb Z,
\quad
2+3\mathbb Z.
```

Đây chính là residue classes modulo 3.

Coset nên được nhìn như “same subgroup pattern nhưng shifted”. Mỗi coset có cùng cardinality với `H` vì map

```math
h\mapsto gh
```

là bijection.

## 2. Lagrange's theorem: subgroup size phải divide group size

Nếu finite group `G` được partition thành disjoint cosets của `H`, mỗi coset có `|H|` elements. Vì vậy

```math
|G|=[G:H]|H|,
```

trong đó `[G:H]` là **index / 지수**: số cosets.

Do đó

```math
|H|\mid |G|.
```

Đây là **Lagrange's theorem**.

Một consequence quan trọng: order của mỗi element `g` divide `|G|`, vì cyclic subgroup generated bởi `g` có size bằng order của `g`.

Lagrange cho necessary condition cho subgroup sizes, không phải sufficient condition: một divisor của `|G|` không bảo đảm luôn tồn tại subgroup có size đó.

## 3. Normal subgroup: khi cosets có thể trở thành một group mới

Ta muốn set of cosets `G/H` có multiplication:

```math
(gH)(kH)=(gk)H.
```

Nhưng operation này chỉ well-defined nếu representative choice không làm kết quả đổi.

Condition cần là `H` **normal / 정규부분군**, ký hiệu

```math
H\trianglelefteq G.
```

Một characterization:

```math
gH=Hg
\qquad \forall g\in G.
```

Hoặc equivalent:

```math
gHg^{-1}=H.
```

Khi đó cosets tạo **quotient group / 몫군**:

```math
G/H.
```

Mental picture: quotient group coi mọi elements trong cùng coset như một macro-state.

## 4. Vì sao kernel luôn normal?

Với homomorphism

```math
\varphi:G\to K,
```

kernel là

```math
\ker\varphi=\{g\in G:\varphi(g)=e_K\}.
```

Nếu `h\in\ker\varphi`, thì

```math
\varphi(ghg^{-1})
=
\varphi(g)\varphi(h)\varphi(g)^{-1}
=
\varphi(g)e\varphi(g)^{-1}
=e.
```

Do đó

```math
ghg^{-1}\in\ker\varphi.
```

nên kernel normal.

Điều này không accidental. Kernel chính xác là phần information bị homomorphism collapse về identity; để quotient nhất quán với group operation, collapsed part phải normal.

## 5. First Isomorphism Theorem

Một theorem trung tâm:

```math
G/\ker\varphi
\cong
\operatorname{im}\varphi.
```

Nghĩa là nếu ta quotient khỏi exactly information mà map không phân biệt, structure còn lại isomorphic với image.

Đây là pattern xuất hiện khắp mathematics:

```text
original object
÷ indistinguishable directions
= effective image
```

Trong linear algebra:

```math
V/\ker T\cong\operatorname{im}T.
```

Rank–nullity là dimensional shadow của same idea.

## 6. Isomorphism: khi hai structures khác representation nhưng giống algebra

Một **isomorphism / 동형사상** là bijective homomorphism. Nếu

```math
G\cong H,
```

thì từ viewpoint group theory, chúng có cùng operation structure dù elements được represented khác nhau.

Ví dụ complex unit circle under multiplication và angles modulo `2\pi` under addition encode same rotational structure.

Isomorphism giúp phân biệt:

```text
representation difference
vs
structural difference
```

Đây là một recurring mental model trong math, software abstraction và data modeling.

## 7. Group action: group tác động lên một set

Một **group action / 군 작용** của `G` lên set `X` gán mỗi `g\in G` một transformation của `X` sao cho:

```math
e\cdot x=x
```

và

```math
(g_1g_2)\cdot x
=
g_1\cdot(g_2\cdot x).
```

Group không chỉ tồn tại abstractly; action nói group **làm gì** lên objects.

Ví dụ symmetry group của square acts on:

- vertices;
- edges;
- diagonals;
- colorings.

Cùng group nhưng different actions reveal different information.

## 8. Orbit và stabilizer

Với `x\in X`, **orbit / 궤도** là set mọi positions reachable:

```math
\operatorname{Orb}(x)=\{g\cdot x:g\in G\}.
```

**Stabilizer / 안정자군** là elements giữ `x` fixed:

```math
\operatorname{Stab}(x)
=
\{g\in G:g\cdot x=x\}.
```

Orbit–Stabilizer Theorem cho finite group:

```math
|G|
=
|\operatorname{Orb}(x)|
\cdot
|\operatorname{Stab}(x)|.
```

Intuition:

```text
all symmetries
=
ways to move x
×
symmetries invisible at x
```

Đây là Lagrange theorem được nhìn qua an action.

## 9. Counting with symmetry: Burnside idea

Nếu muốn count distinct colorings up to rotation/reflection, ordinary counting overcounts configurations được xem equivalent dưới symmetry.

**Burnside's lemma** nói số orbits bằng average number of fixed points:

```math
|X/G|
=
\frac{1}{|G|}
\sum_{g\in G}|\operatorname{Fix}(g)|.
```

Điều đáng học là strategy:

> Thay vì enumerate equivalence classes trực tiếp, average những configurations được từng symmetry giữ cố định.

Group actions vì vậy nối abstract algebra với combinatorics.

## 10. Sylow theorems: prime-factor structure của finite groups

Nếu

```math
|G|=p^k m,
\qquad p\nmid m,
```

một **Sylow p-subgroup / 실로우 p-부분군** có order `p^k`.

Sylow theorems, ở mức conceptual, nói:

1. subgroup lớn nhất theo prime-power part tồn tại;
2. mọi Sylow `p`-subgroups conjugate;
3. số Sylow subgroups bị arithmetic constraints.

Ví dụ nếu `|G|=15=3\cdot5`, number of Sylow-5 subgroups `n_5` phải thỏa

```math
n_5\equiv1\pmod5
```

và

```math
n_5\mid3.
```

Chỉ possibility là `n_5=1`, nên Sylow-5 subgroup unique và do đó normal.

Sylow theory biến prime factorization của group order thành structural information về group.

## 11. Ring homomorphism và ideals

Trong rings, analogue của normal subgroup là **ideal / 아이디얼**.

Một subset `I\subseteq R` là ideal nếu nó closed under addition/subtraction và absorb multiplication bởi ring elements:

```math
r\in R,\ a\in I
\Rightarrow
ra\in I
```

(and `ar\in I` trong two-sided setting).

Với ring homomorphism

```math
\varphi:R\to S,
```

kernel là ideal.

Ta có first isomorphism pattern:

```math
R/\ker\varphi
\cong
\operatorname{im}\varphi.
```

Normal subgroups và ideals cùng đóng vai trò “collapsible substructures”.

## 12. Quotient ring và modular arithmetic

Trong integers, ideal generated bởi `n` là

```math
(n)=n\mathbb Z.
```

Quotient ring

```math
\mathbb Z/(n)
```

chính là arithmetic modulo `n`.

Nếu `p` prime:

```math
\mathbb Z/(p)
```

là field.

Nếu `n` composite, zero divisors xuất hiện nên quotient thường chỉ là ring.

Như vậy modulo arithmetic không phải một trick riêng; nó là canonical quotient construction.

## 13. Principal ideals và gcd viewpoint

Trong `\mathbb Z`, mọi ideal có dạng

```math
(n).
```

Do đó `\mathbb Z` là a **principal ideal domain (PID / 주 아이디얼 정역)**.

Ideal generated bởi `a,b`:

```math
(a,b)=\{ax+by:x,y\in\mathbb Z\}.
```

Bézout identity nói trong integers:

```math
(a,b)=(\gcd(a,b)).
```

GCD vì vậy không chỉ là “greatest divisor”; nó là generator của smallest ideal chứa cả `a` và `b`.

Đây là deeper structural interpretation của Euclidean algorithm.

## 14. Polynomial rings và irreducibility

Với field `F`, polynomial ring

```math
F[x]
```

có nhiều analogies với integers:

```text
integer primes
↔ irreducible polynomials

integer factorization
↔ polynomial factorization

gcd of integers
↔ polynomial gcd
```

Polynomial `p(x)` là **irreducible / 기약** over `F` nếu không factor thành lower-degree nonconstant polynomials trong `F[x]`.

Quan trọng: irreducibility phụ thuộc field.

Ví dụ

```math
x^2+1
```

irreducible over `\mathbb R`, nhưng factor over `\mathbb C`:

```math
x^2+1=(x-i)(x+i).
```

## 15. Quotient by irreducible polynomial tạo field extension

Nếu `p(x)` irreducible over field `F`, quotient

```math
F[x]/(p(x))
```

là field.

Ví dụ từ `\mathbb R` và polynomial

```math
x^2+1,
```

quotient construction tạo object `\alpha` satisfying

```math
\alpha^2+1=0.
```

Ta có thể identify `\alpha` với `i`, dẫn tới complex numbers.

Conceptual pattern:

> Muốn một polynomial có root nhưng current field không chứa root đó, ta có thể enlarge field bằng cách formally adjoin một root.

## 16. Field extension

Nếu `F\subseteq K` và cả hai là fields, `K/F` là **field extension / 체 확장**.

`K` có thể được xem như vector space over `F`. Dimension

```math
[K:F]
```

gọi là degree của extension.

Ví dụ

```math
[\mathbb C:\mathbb R]=2
```

vì mọi complex number viết unique:

```math
a+bi,
\qquad a,b\in\mathbb R.
```

Basis là `{1,i}`.

Đây là một strong bridge giữa field theory và linear algebra.

## 17. Algebraic elements và minimal polynomial

Element `\alpha` trong extension `K/F` gọi là **algebraic over F / 대수적** nếu tồn tại nonzero polynomial `p(x)\in F[x]` sao cho

```math
p(\alpha)=0.
```

Có một monic irreducible polynomial degree nhỏ nhất gọi là **minimal polynomial / 최소다항식**.

Nếu minimal polynomial degree là `d`, simple extension `F(\alpha)` thường có basis

```math
1,\alpha,\alpha^2,\ldots,\alpha^{d-1}.
```

và

```math
[F(\alpha):F]=d.
```

Polynomial equation và vector-space dimension bắt đầu nối trực tiếp.

## 18. Finite fields beyond prime fields

Prime field

```math
\mathbb F_p
```

có `p` elements.

Nhưng finite fields còn tồn tại với size

```math
p^n
```

cho prime `p` và positive integer `n`.

Một construction điển hình:

```math
\mathbb F_{p^n}
\cong
\mathbb F_p[x]/(f(x))
```

với `f(x)` irreducible degree `n`.

Ví dụ finite fields này là nền của:

- error-correcting codes;
- AES-like finite-field arithmetic;
- algebraic coding theory;
- elliptic-curve arithmetic over finite fields.

## 19. Splitting field: nơi polynomial tách hoàn toàn

Cho polynomial `f(x)\in F[x]`. **Splitting field / 분해체** là smallest field extension nơi `f` factor hoàn toàn thành linear factors.

Ví dụ `x^2-2` trên `\mathbb Q` cần adjoin `\sqrt2`:

```math
\mathbb Q(\sqrt2).
```

Polynomial có roots `\pm\sqrt2`, và cả hai nằm trong field này.

Splitting field không chỉ “thêm roots”; nó tạo minimal algebraic universe đủ để chứa toàn bộ root structure.

## 20. Galois group: symmetry của roots giữ nguyên base field

Cho extension `K/F`. Một **field automorphism / 체 자기동형사상** của `K` fixing `F` giữ mọi element của `F` unchanged.

Collection các automorphisms đó tạo group:

```math
\operatorname{Gal}(K/F).
```

Ví dụ với

```math
K=\mathbb Q(\sqrt2),
```

map

```math
\sqrt2\mapsto-\sqrt2
```

preserves rational numbers và field operations. Cùng identity map, ta có group size 2.

Galois group encode ways roots can be permuted while preserving every algebraic relation visible từ base field.

## 21. Galois correspondence intuition

Galois theory thiết lập correspondence giữa:

```text
subgroups of Galois group
        ↔
intermediate fields
```

Structural message:

> Symmetry của roots và hierarchy của field extensions là hai descriptions của cùng information.

Đây là một trong những examples đẹp nhất của mathematics nơi a group-theoretic object classify a field-theoretic object.

## 22. Solvability by radicals: vì sao quintic story liên quan group theory?

Quadratic, cubic và quartic equations có formulas bằng radicals. General quintic không có universal radicals formula.

Galois theory không nói “quintic không giải được”; nhiều individual quintics vẫn có solvable forms hoặc special roots. Statement đúng hơn:

> General polynomial degree 5 trở lên không có formula bằng finite combination của arithmetic operations và radicals analogous to quadratic formula.

Criterion liên quan **solvability of its Galois group**.

Đây là extraordinary conceptual leap:

```text
question about formulas for polynomial roots
        ↓
question about symmetry group structure
```

## 23. Connection với linear algebra

Linear algebra là một special algebraic theory:

- vector space defined over a field;
- linear maps are structure-preserving maps;
- kernel/image obey isomorphism pattern;
- quotient spaces collapse null directions;
- eigenvalues may require field extension.

Ví dụ real matrix có characteristic polynomial không có real roots; moving from `\mathbb R` to `\mathbb C` may expose eigenvalues/eigenvectors.

## 24. Connection với number theory

Advanced number theory uses algebra heavily:

```text
integers → rings
congruences → quotient rings
units modulo n → groups
finite fields → field theory
quadratic residues → multiplicative group structure
algebraic integers → number fields
```

Đọc tiếp [Number theory nâng cao](./10_number_theory_diophantine_quadratic_residues_and_crypto.md) để thấy these structures operationally.

## 25. Connection với coding và cryptography

Error-correcting codes often work over `\mathbb F_q`, where vectors/polynomials carry finite-field structure.

Cryptographic systems use groups/fields where selected computational problems are hard. But abstract algebra alone không guarantee security: practical security còn cần parameter choices, protocol proofs, implementation discipline và side-channel considerations.

Mathematics cung cấp operation structure; cryptographic engineering quyết định structure đó được dùng an toàn hay không.

## Mental Model

> Abstract algebra nâng cao là nghệ thuật **nén structure mà không mất operations quan trọng**. Coset/quotient collapse distinctions; homomorphism cho biết distinction nào bị mất; isomorphism nói hai representations thực chất giống nhau; group action biến symmetry thành motion; ideal làm quotient ring hợp lệ; field extension tạo universe đủ lớn để polynomial roots tồn tại; Galois group biến relations giữa roots thành symmetry.

## Common Misconceptions

**“Mọi subgroup đều cho quotient group.”** Không; cần normal subgroup.

**“Nếu `|H|` divide `|G|` thì subgroup `H` chắc tồn tại.”** Lagrange chỉ cho necessary condition. Sylow/Cauchy và structure cụ thể mới cung cấp thêm existence information.

**“Ideal chỉ là subgroup của ring dưới addition.”** Chưa đủ; ideal còn phải absorb multiplication bởi ring elements.

**“Irreducible polynomial là polynomial không factor ở đâu cả.”** Irreducibility phụ thuộc coefficient field.

**“Field extension chỉ là thêm một symbol mới.”** Symbol phải obey algebraic relations; resulting object cần preserve field axioms và thường có vector-space structure over base field.

**“Galois theory chứng minh mọi degree-5 equation vô nghiệm.”** Sai. Nó nói về absence of a universal radicals solution for general quintic và connects solvability by radicals với group structure.

## Nguồn học miễn phí để đi sâu

- Thomas W. Judson, **Abstract Algebra: Theory and Applications** — official open textbook: https://judsonbooks.org/abstract-algebra-theory-and-applications/ . Nội dung đi từ group theory qua Sylow, rings, integral domains, vector spaces, fields tới Galois theory.
- Abakcus, **Free Math Textbooks from University Mathematicians** — https://abakcus.com/book-lists/free-math-textbooks . Dùng như catalog để phát hiện open textbooks; ưu tiên đọc bản từ tác giả/trường đại học.

> **Bàn giao:** Đọc [Number theory nâng cao](./10_number_theory_diophantine_quadratic_residues_and_crypto.md) để thấy group/field structures được dùng trong quadratic residues, discrete logarithms và elliptic curves; hoặc quay lại [Linear Algebra](../04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md) để đối chiếu quotient/kernel/image trong setting tuyến tính.