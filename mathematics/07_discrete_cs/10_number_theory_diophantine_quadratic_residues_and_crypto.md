# Number theory nâng cao: Diophantine equations, quadratic residues và cryptographic structures

> **Mạch đọc:** Chapter này tiếp nối [Number theory và modular arithmetic](./04_number_theory_and_modular_arithmetic.md) và [Abstract algebra nâng cao](./09_abstract_algebra_quotients_actions_and_field_extensions.md). Chapter trước đã có gcd, Bézout, congruence, modular inverse, Fermat/Euler, CRT và finite fields; ở đây ta đi tiếp vào những structures thường xuất hiện trong một university number-theory course.

Number theory có một đặc trưng thú vị: statement rất elementary có thể dẫn tới structure sâu. Câu hỏi “integer solutions có tồn tại không?” đưa ta tới gcd và congruences; câu hỏi “một number có phải square modulo `p` không?” đưa tới multiplicative groups và quadratic reciprocity; câu hỏi “rational nào approximate irrational tốt nhất?” đưa tới continued fractions.

## 1. Diophantine equation: equation nhưng solutions bị giới hạn trong integers

Một **phương trình Diophantine (Diophantine equation / 디오판토스 방정식)** là polynomial equation nơi ta tìm integer hoặc rational solutions.

Khác với ordinary algebra, existence over `\mathbb R` không đủ. Ví dụ

```math
2x+4y=3
```

có infinitely many real solutions nhưng không có integer solution.

Integer constraint làm divisibility trở thành central structure.

## 2. Linear Diophantine equation `ax+by=c`

Xét

```math
ax+by=c,
\qquad a,b,c\in\mathbb Z.
```

Bézout cho criterion chính xác:

```math
ax+by=c
```

có integer solution iff

```math
\gcd(a,b)\mid c.
```

Vì mọi linear combination `ax+by` phải divisible bởi `gcd(a,b)`. Ngược lại, nếu `d=gcd(a,b)` divide `c`, Bézout representation của `d` có thể scale lên `c`.

## 3. General solution của linear Diophantine equation

Giả sử `(x_0,y_0)` là một solution và

```math
d=\gcd(a,b).
```

Mọi integer solutions là

```math
x=x_0+\frac{b}{d}t,
```

```math
y=y_0-\frac{a}{d}t,
```

với `t\in\mathbb Z`.

Đây là một one-dimensional lattice of solutions trên plane.

Geometric viewpoint giúp nối Diophantine equations với lattice geometry: real line `ax+by=c` chứa continuous points, còn integer solutions là những lattice points line đó đi qua.

## 4. Congruence như impossibility filter

Trước khi tìm solutions, reduce equation modulo một small base có thể nhanh chóng chứng minh impossible.

Ví dụ muốn integer solutions của

```math
x^2+y^2=3.
```

Modulo 4, mỗi square chỉ congruent `0` hoặc `1`. Tổng hai squares chỉ có thể `0,1,2 mod 4`, không thể `3`. Vậy no integer solutions.

Đây là local obstruction:

```text
if equation impossible modulo m
→ impossible over integers
```

Converse không luôn đúng: solvable modulo every small modulus không necessarily guarantee global integer solution.

## 5. Multiplicative order

Nếu `gcd(a,n)=1`, **multiplicative order / 곱셈위수** của `a modulo n` là smallest positive integer `k` sao cho

```math
a^k\equiv1\pmod n.
```

Order đo cycle length của repeated multiplication by `a` trong unit group modulo `n`.

Euler's theorem bảo đảm order divide

```math
\varphi(n).
```

vì order của an element divide group order theo Lagrange.

Thus Fermat/Euler can be reframed as group theory rather than isolated exponent tricks.

## 6. Primitive roots

Nếu multiplicative group modulo `n` là cyclic, tồn tại element `g` generate toàn group. Such `g` gọi là **primitive root / 원시근**.

Modulo prime `p`, group

```math
\mathbb F_p^\times
```

có order `p-1` và là cyclic.

Do đó có `g` sao cho every nonzero residue viết được:

```math
g^k\pmod p.
```

Điều này biến multiplication thành exponent arithmetic modulo `p-1`.

## 7. Discrete logarithm

Nếu `g` generate a cyclic group và

```math
y=g^x,
```

finding `y` từ `x` bằng repeated squaring thường efficient. Reverse problem—finding `x` từ `g,y`—là **discrete logarithm problem / 이산로그 문제**.

Notation:

```math
x=\log_g y
```

nhưng đây không phải ordinary real logarithm.

Asymmetry “forward easy, inverse believed hard for suitable groups/parameters” là basis của several cryptographic constructions.

Important: hardness phụ thuộc group và parameter choices; không phải mọi discrete-log instance đều hard.

## 8. Quadratic residues

Cho odd prime `p`. Một nonzero residue `a` là **quadratic residue / 이차잉여** modulo `p` nếu tồn tại `x` sao cho

```math
x^2\equiv a\pmod p.
```

Nếu không, `a` là quadratic nonresidue.

Ví dụ modulo 7:

```text
1² ≡ 1
2² ≡ 4
3² ≡ 2
4² ≡ 2
5² ≡ 4
6² ≡ 1
```

Nonzero quadratic residues là `{1,2,4}`.

Exactly half of nonzero residues are squares because map

```math
x\mapsto x^2
```

identifies `x` và `-x`.

## 9. Legendre symbol

Với odd prime `p`, **Legendre symbol / 르장드르 기호**:

```math
\left(\frac ap\right)
=
\begin{cases}
0,&p\mid a,\\
1,&a\text{ is a nonzero quadratic residue mod }p,\\
-1,&a\text{ is a quadratic nonresidue mod }p.
\end{cases}
```

Nó compress question “is `a` a square modulo `p`?” thành multiplicative symbol.

Key property:

```math
\left(\frac{ab}{p}\right)
=
\left(\frac ap\right)
\left(\frac bp\right).
```

Quadratic-residue behavior therefore respects multiplicative structure.

## 10. Euler's criterion

For `p` odd prime and `p\nmid a`:

```math
\left(\frac ap\right)
\equiv
 a^{(p-1)/2}
\pmod p.
```

Right side must be `±1 mod p`.

Why? In cyclic group `\mathbb F_p^\times`, write

```math
a=g^k.
```

Then `a` is a square iff `k` even. Raising to `(p-1)/2` detects parity of exponent:

```math
(g^k)^{(p-1)/2}
=
(-1)^k.
```

Euler criterion is therefore a character of the multiplicative group, not arbitrary exponent magic.

## 11. Quadratic reciprocity: relation giữa “p square mod q?” và “q square mod p?”

For distinct odd primes `p,q`, **quadratic reciprocity / 이차상호법칙** states:

```math
\left(\frac pq\right)
\left(\frac qp\right)
=
(-1)^{\frac{(p-1)(q-1)}{4}}.
```

Equivalent:

- if at least one of `p,q` is `1 mod 4`, the two symbols are equal;
- if both are `3 mod 4`, signs are opposite.

The theorem is striking because it connects two modular worlds that appear unrelated.

It lets difficult residue questions be transformed recursively into smaller ones, somewhat analogous to Euclidean algorithm reducing gcd problems.

## 12. Supplementary laws

Two useful rules:

```math
\left(\frac{-1}{p}\right)
=
(-1)^{(p-1)/2},
```

so `-1` is square modulo `p` iff

```math
p\equiv1\pmod4.
```

And

```math
\left(\frac{2}{p}\right)
=
(-1)^{(p^2-1)/8}.
```

These supplement reciprocity and make Legendre-symbol calculations algorithmic.

## 13. Continued fractions

A real number can be expanded as a **continued fraction / 연분수**:

```math
x=a_0+\cfrac{1}{a_1+\cfrac{1}{a_2+\cdots}}.
```

For example:

```math
\sqrt2=[1;2,2,2,\ldots].
```

Truncating expansion gives **convergents / 수렴분수**:

```text
1,
3/2,
7/5,
17/12,
41/29,
...
```

These rational numbers approximate `\sqrt2` exceptionally well relative to denominator size.

## 14. Why continued fractions matter

Given irrational `x`, convergents solve a practical approximation problem:

> Among rationals with bounded denominator, which ones approximate `x` unusually well?

This connects number theory to:

- rational approximation;
- Diophantine approximation;
- numerical representation;
- periodicity properties of quadratic irrationals.

Unlike decimal truncation, continued fractions adapt to arithmetic structure of the number.

## 15. Pell equation

Classic **Pell equation / 펠 방정식**:

```math
x^2-Dy^2=1,
```

where `D` is positive nonsquare integer.

For `D=2`, solutions include:

```math
(3,2),
(17,12),
(99,70),
\ldots
```

Notice ratios

```math
x/y
```

approximate `\sqrt2`.

Indeed:

```math
x^2-2y^2=1
```

implies

```math
\left|\frac xy-\sqrt2\right|
```

is tiny for large `y`.

Continued fractions of `\sqrt D` generate fundamental solutions systematically.

## 16. Pythagorean triples as a Diophantine family

Equation

```math
x^2+y^2=z^2
```

has infinitely many integer solutions. Primitive triples can be parameterized:

```math
x=m^2-n^2,
```

```math
y=2mn,
```

```math
z=m^2+n^2
```

under suitable coprimality/parity conditions.

This is a useful example of a broader number-theory question:

```text
Can all integer solutions be parameterized?
```

Sometimes yes, sometimes only partially, sometimes the solution set has deep geometric structure.

## 17. Primality testing khác factoring

Given integer `n`, two tasks:

```text
Is n prime?
```

and

```text
If n is composite, what are its prime factors?
```

are computationally different.

Primality can be tested efficiently without factoring `n`. Modern algorithms and probabilistic tests can establish primality much faster than generic factorization for large numbers.

This distinction matters in cryptography: “hard to factor” is not the same statement as “hard to tell whether prime”.

## 18. Probabilistic primality testing intuition

Tests such as Miller–Rabin use modular exponentiation to search for witnesses proving compositeness.

A random base may occasionally fail to expose a composite, but repeated independent bases reduce error probability rapidly for the probabilistic variant.

Conceptual pattern:

```text
cheap algebraic consistency checks
+ random witnesses
→ high-confidence compositeness/primality screening
```

This is an example where probability accelerates a number-theoretic algorithm without making theorem statements themselves approximate.

## 19. RSA mathematical structure

RSA uses arithmetic modulo

```math
N=pq
```

for large primes `p,q`.

At a high level, choose exponents `e,d` satisfying an inverse relation modulo an appropriate group exponent/totient quantity. Encryption/signature primitives involve exponentiation such as

```math
m\mapsto m^e\pmod N
```

and inverse exponent recovers the algebraic message representative under required conditions.

The mathematical insight is built from:

- modular exponentiation;
- Euler/Carmichael-style group structure;
- modular inverse;
- CRT for efficient decomposition/recombination.

Practical RSA security is not “just number theory”: secure padding, protocol design, key sizes, randomness and implementation protections are essential.

## 20. Chinese Remainder Theorem as decomposition

For coprime `m,n`:

```math
\mathbb Z/(mn)
\cong
\mathbb Z/m\times\mathbb Z/n
```

as rings.

This abstract-algebra view explains why computation modulo product can be split into independent computations modulo factors and then recombined.

CRT is thus both:

- a theorem for solving simultaneous congruences;
- a structural factorization of modular arithmetic.

## 21. Elliptic curves: cubic equations with a group law

An elliptic curve over a field often has form

```math
y^2=x^3+ax+b
```

with non-singularity condition

```math
4a^3+27b^2\ne0.
```

Over the real numbers, points form a smooth curve. Remarkably, one can define addition of points geometrically:

1. draw line through `P,Q`;
2. find third intersection with curve;
3. reflect across x-axis.

Together with a point at infinity as identity, points form an abelian group.

## 22. Why the elliptic-curve group law is natural

A line intersects a cubic in three points counting multiplicity. If two points are known, algebra determines the third. Reflection turns this three-point relation into an associative group operation.

The geometry is not a visual trick added after the fact; it reflects polynomial intersection structure.

Over finite fields, drawing disappears but algebraic formulas for point addition still work.

## 23. Elliptic curves over finite fields

Over `\mathbb F_p`, coordinates are residues modulo `p`. The curve has finitely many points, and the same group-law formulas operate using finite-field arithmetic.

This produces finite abelian groups suitable for discrete-log-based cryptographic constructions.

Elliptic-curve discrete logarithm:

```math
Q=kP
```

Given `P,Q`, recover scalar `k`.

For suitable curves/parameters, no generic algorithm comparable to integer factoring is known to solve this efficiently at cryptographic sizes, allowing smaller keys than some older groups for comparable security targets.

Again, practical security requires approved curves, protocols and implementations; mathematical group hardness is only one layer.

## 24. Number theory meets geometry

Elliptic curves show a transition:

```text
integer/rational solutions of equations
        ↓
algebraic curves
        ↓
geometry + group structure
        ↓
arithmetic information
```

Modern number theory often studies polynomial equations by attaching geometric/algebraic objects to them rather than manipulating integer equations directly.

This direction eventually leads to algebraic number theory and arithmetic geometry.

## 25. Local-to-global thinking

A recurring strategy:

```text
integer/rational problem
→ inspect modulo many primes
→ detect local constraints
→ infer global information where possible
```

But local solvability does not universally imply global solvability.

The important mental model is not “check modulo primes and you're done”, but:

> Modular reductions are projections of a difficult global problem into simpler finite worlds. Information lost in projection determines how strong the conclusion can be.

## 26. Connection với abstract algebra

Many topics above become cleaner in algebraic language:

- units modulo `n` form a group;
- quadratic residues form a subgroup-related structure;
- finite fields give cyclic multiplicative groups;
- CRT is ring isomorphism;
- elliptic-curve points form abelian groups;
- field extensions describe algebraic numbers and roots.

This is why deeper number theory and abstract algebra should be learned together rather than as unrelated subjects.

## 27. Connection với computation

Number theory is unusually algorithmic:

```text
Euclidean algorithm
fast exponentiation
modular inverse
CRT reconstruction
primality testing
continued-fraction expansion
elliptic-curve point arithmetic
```

Every theorem has a computational question:

```text
Does an object exist?
How do we construct it?
How many bit operations does construction require?
How does complexity scale with input size?
```

This connects naturally to [Algorithms and complexity](./01_algorithms_complexity_and_logarithms.md).

## Mental Model

> Number theory studies integers by repeatedly changing representation. Diophantine equations become divisibility/congruence constraints; multiplicative arithmetic becomes finite groups; “is this a square?” becomes a character/Legendre-symbol question; irrational approximation becomes continued fractions; cubic equations become elliptic-curve groups. A good representation turns infinite arithmetic search into structured finite or algebraic problems.

## Common Misconceptions

**“Nếu equation có solution modulo nhiều `m` thì chắc có integer solution.”** Không; modular solvability gives necessary local evidence, not a universal sufficient condition.

**“Euler/Fermat theorem cho exact multiplicative order.”** Không; they give an exponent that returns 1 under conditions. Actual order may be a proper divisor.

**“Quadratic residue means ordinary perfect square.”** It means square **modulo p**.

**“Primality testing và factoring là cùng độ khó.”** Không. Ta có efficient primality testing without efficient general factoring.

**“Discrete logarithm luôn hard.”** Không; hardness depends on the chosen group and parameters.

**“Elliptic-curve cryptography an toàn chỉ vì equation trông phức tạp.”** Không; security depends on precise group structure, parameters, protocols and implementation.

## Nguồn học miễn phí để đi sâu

- William Stein, **Elementary Number Theory: Primes, Congruences, and Secrets** — open-source book repository: https://github.com/williamstein/ent . Nội dung nối elementary number theory với public-key cryptography, quadratic reciprocity, continued fractions và elliptic curves.
- American Institute of Mathematics Open Textbook Initiative listing for Stein's book: https://aimath.org/textbooks/approved-textbooks/stein/ .
- Abakcus, **Free Math Textbooks from University Mathematicians** — https://abakcus.com/book-lists/free-math-textbooks . Dùng như catalog discovery; ưu tiên official author/university source khi học.

> **Bàn giao:** Nếu phần groups/fields trong chapter này còn black box, quay lại [Abstract algebra nâng cao](./09_abstract_algebra_quotients_actions_and_field_extensions.md). Nếu mục tiêu là algorithms/cryptography, đọc tiếp [Algorithms & Complexity](./01_algorithms_complexity_and_logarithms.md) và [Information Theory & Coding](./06_information_theory_and_coding.md).