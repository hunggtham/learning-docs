# Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc

Lý thuyết số (number theory / 정수론) nghiên cứu integers, divisibility và các structures sinh ra từ arithmetic rời rạc. Đây là một lĩnh vực cho thấy rất rõ cách một concept “thuần toán” có thể trở thành nền của algorithms, hashing, cyclic systems, error checking và cryptographic mathematics.

Mục tiêu của chapter này không phải nhớ các theorem riêng lẻ, mà hiểu một learning flow:

```text
integer structure
→ divisibility
→ gcd / Euclidean algorithm
→ primes
→ congruence classes
→ modular inverses
→ finite algebraic systems
→ efficient computation
```

## 1. Divisibility là structural relation

Với integers `a,b`, ta viết

```math
a\mid b
```

nếu tồn tại integer `k` sao cho

```math
b=ak.
```

Definition này mạnh hơn “chia ra được số nguyên” vì nó cho phép proof algebraic trực tiếp.

Ví dụ nếu

```math
a\mid b
\quad\text{và}\quad
a\mid c,
```

thì tồn tại `m,n` với

```math
b=am,\qquad c=an.
```

Do đó với integers `r,s`:

```math
rb+sc=a(rm+sn),
```

nên

```math
a\mid(rb+sc).
```

Đây là source của rất nhiều arguments về gcd và congruence.

## 2. Division algorithm

Với integer `a` và positive integer `n`, tồn tại duy nhất integers `q,r` sao cho

```math
a=qn+r,
\qquad 0\le r<n.
```

`q` là quotient, `r` remainder.

Đây là theorem formal hóa intuition “chia lấy phần nguyên và phần dư”.

Nó là nền của Euclidean algorithm và modular arithmetic.

## 3. GCD là greatest common structure

Greatest common divisor:

```math
\gcd(a,b)
```

là positive integer lớn nhất chia cả `a` và `b`.

Ví dụ:

```math
\gcd(84,30)=6.
```

Nhưng definition “largest shared factor” chưa cho algorithm hiệu quả. Euclid tìm structure sâu hơn.

## 4. Euclidean algorithm: vì sao thay `(a,b)` bằng `(b,r)` được?

Viết

```math
a=qb+r.
```

Một number `d` chia cả `a,b` iff nó chia cả `b,r` vì

```math
r=a-qb.
```

Do đó:

```math
\gcd(a,b)=\gcd(b,r).
```

Lặp process làm second argument giảm:

```text
252 = 105·2 + 42
105 = 42·2 + 21
42  = 21·2 + 0
```

nên

```math
\gcd(252,105)=21.
```

Điểm quan trọng là mỗi step không “đoán” gcd; nó thay problem bằng equivalent smaller problem.

## 5. Termination và algorithmic reasoning

Remainder luôn thỏa

```math
0\le r<b.
```

nên sequence remainders là decreasing nonnegative integers. Nó không thể giảm vô hạn, nên algorithm terminate.

Đây là ví dụ number theory nối trực tiếp với proof of termination trong algorithms.

## 6. Bézout identity

Có integers `x,y` sao cho

```math
ax+by=\gcd(a,b).
```

Extended Euclidean algorithm không chỉ tìm gcd; nó tìm luôn coefficients `x,y`.

Ví dụ với `30,18`:

```math
\gcd(30,18)=6.
```

Ta có thể tìm:

```math
6=2(18)-1(30).
```

Bézout identity là bridge trực tiếp tới modular inverse.

## 7. Prime numbers là atoms của multiplication

Prime (số nguyên tố / 소수) là integer >1 chỉ có positive divisors `1` và chính nó.

Composite numbers có factorization thành smaller integers.

Fundamental Theorem of Arithmetic nói mọi integer `n>1` có prime factorization duy nhất up to order:

```math
n=p_1^{a_1}\cdots p_k^{a_k}.
```

Prime factorization đóng vai trò như “coordinate system” cho multiplicative structure của positive integers.

## 8. GCD/LCM từ prime exponents

Nếu

```math
n=\prod p_i^{a_i},
\qquad
m=\prod p_i^{b_i},
```

thì

```math
\gcd(n,m)=\prod p_i^{\min(a_i,b_i)}
```

và

```math
\operatorname{lcm}(n,m)=\prod p_i^{\max(a_i,b_i)}.
```

Điều này giải thích vì sao:

```math
\gcd(n,m)\operatorname{lcm}(n,m)=|nm|.
```

## 9. Infinitely many primes: proof idea

Giả sử chỉ có finitely many primes:

```text
p1,p2,...,pk.
```

Xét

```math
N=p_1p_2\cdots p_k+1.
```

Không `p_i` nào chia `N` vì remainder là 1. Nhưng `N>1` phải có prime divisor. Contradiction.

Điểm đáng học không chỉ theorem mà là proof strategy: build object cố tình nằm ngoài assumed complete list.

## 10. Congruence modulo n

Ta viết

```math
a\equiv b\pmod n
```

nếu

```math
n\mid(a-b).
```

Equivalent interpretation: `a` và `b` cùng remainder khi chia cho `n`.

Ví dụ:

```math
17\equiv5\pmod{12}.
```

Congruence là một equivalence relation trên integers.

Nó partition `\mathbb Z` thành remainder classes:

```math
[0],[1],\ldots,[n-1].
```

## 11. Modular arithmetic không chỉ là `%`

Operator `%` trong programming trả remainder theo language-specific convention.

Mathematical modulo arithmetic nói về equivalence classes.

Hai statements khác nhau:

```text
-1 % 5  // implementation/language semantics
```

và

```math
-1\equiv4\pmod5.
```

Trong mathematics, class của `-1` và `4` là cùng class modulo 5.

## 12. Addition và multiplication descend xuống residue classes

Nếu

```math
a\equiv b\pmod n
```

và

```math
c\equiv d\pmod n,
```

thì

```math
a+c\equiv b+d\pmod n
```

và

```math
ac\equiv bd\pmod n.
```

Proof đến từ divisibility của differences.

Điều này làm arithmetic trên residue classes well-defined.

## 13. Modular inverse

Ta muốn `x` sao cho

```math
ax\equiv1\pmod n.
```

Điều này equivalent tồn tại integer `k`:

```math
ax-kn=1.
```

Theo Bézout, solution tồn tại iff

```math
\gcd(a,n)=1.
```

Vì vậy coprimality là condition chính xác cho invertibility modulo `n`.

## 14. Worked Example: inverse của 7 modulo 26

Euclidean algorithm:

```text
26 = 7·3 + 5
7  = 5·1 + 2
5  = 2·2 + 1
```

Back substitute:

```math
1=5-2\cdot2
```

```math
=5-2(7-5)
=3\cdot5-2\cdot7
```

```math
=3(26-3\cdot7)-2\cdot7
=3\cdot26-11\cdot7.
```

Do đó:

```math
-11\cdot7\equiv1\pmod{26}
```

nên inverse của 7 modulo 26 là

```math
15
```

vì `-11≡15 mod 26`.

## 15. Modular division không giống ordinary division

Expression

```math
\frac ab\pmod n
```

chỉ meaningful nếu `b` có inverse modulo `n`.

Ví dụ modulo 6, `2` không invertible vì

```math
\gcd(2,6)=2\ne1.
```

Không thể “chia hai vế cho 2” modulo 6 như trên real numbers mà không kiểm tra structure.

## 16. Fermat's little theorem

Nếu `p` prime và

```math
p\nmid a,
```

thì

```math
a^{p-1}\equiv1\pmod p.
```

Một proof idea xem multiplication by `a` permute nonzero residue classes modulo `p` vì `a` invertible.

Product của classes `1,...,p-1` sau permutation vẫn same modulo `p`, dẫn tới theorem.

Điểm sâu là theorem đến từ symmetry/permutation structure của invertible residues.

## 17. Euler's theorem

Nếu

```math
\gcd(a,n)=1,
```

thì

```math
a^{\varphi(n)}\equiv1\pmod n,
```

trong đó `\varphi(n)` là Euler totient: số residue classes modulo `n` coprime với `n`.

Fermat là special case khi `n=p` prime, vì

```math
\varphi(p)=p-1.
```

## 18. Fast modular exponentiation

Muốn tính

```math
a^k\bmod n
```

không cần compute giant integer `a^k` trước.

Repeated squaring dùng binary decomposition của exponent.

Ví dụ `k=13=8+4+1`:

```text
a^1
→ square: a^2
→ square: a^4
→ square: a^8
```

combine needed powers, reducing modulo `n` mỗi step.

Complexity theo number of exponent bits, roughly `O(log k)` multiplications.

Đây là connection trực tiếp number theory ↔ algorithm complexity.

## 19. Chinese Remainder Theorem intuition

Nếu moduli `m,n` coprime, pair of remainders:

```math
x\bmod m,
\qquad x\bmod n
```

xác định unique residue modulo `mn`.

Conceptually, một large cyclic state có thể decomposed thành independent smaller cyclic coordinates khi moduli coprime.

CRT là một “change of coordinates” cho modular arithmetic.

## 20. Cyclic systems trong software

Modulo xuất hiện tự nhiên khi state wraps around:

```text
clock hours
weekdays
ring buffers
circular array index
sequence counters
sharding buckets
```

Nhưng wraparound integer trong hardware không luôn equivalent với intended mathematical modulo, đặc biệt khi signed overflow semantics khác language.

## 21. Hash table connection

Hash table thường dùng mapping:

```math
bucket=h(key)\bmod m.
```

Modulo chỉ compress range. Nó không tự tạo good distribution.

Nếu upstream hash có patterns align với `m`, collisions có thể cao.

Do đó number-theoretic structure của table size đôi khi matter, nhưng modern hash-table design còn phụ thuộc load factor, mixing function và collision strategy.

## 22. Error detection và check digits

Checksum/check-digit systems thường dùng modular constraints.

Ví dụ simple digit sum modulo 10 có thể detect một số errors nhưng không phải tất cả transpositions.

Design tốt cần analyze error model và algebraic code structure.

Number theory cung cấp invariant; reliability phụ thuộc invariant detect được loại perturbation nào.

## 23. Finite fields: khi residue arithmetic trở thành field

Modulo prime `p`, nonzero residue classes đều invertible. Vì vậy

```math
\mathbb F_p
```

là field.

Modulo composite `n`, zero divisors có thể xuất hiện. Ví dụ modulo 6:

```math
2\cdot3\equiv0\pmod6
```

mặc dù neither factor congruent 0.

Do đó `\mathbb Z/6\mathbb Z` không phải field.

Đây là bridge sang algebraic structures.

## 24. Connection với cryptographic mathematics

Modular exponentiation, finite groups và finite fields xuất hiện trong nhiều cryptographic constructions.

Nhưng một theorem number theory đúng không tự đảm bảo system secure. Practical design còn phụ thuộc protocol, parameter size, randomness, implementation, side-channel resistance và threat model.

Ở đây mục tiêu chỉ là hiểu mathematical substrate, không đồng nhất “có prime/modulo” với security.

## 25. Connection với Fourier và cyclic structure

Discrete Fourier Transform làm việc với periodic/cyclic indexing. Roots of unity là solutions của

```math
z^n=1
```

trong complex numbers.

Finite cyclic structures và modular indexing vì vậy xuất hiện song song trong signal processing và number-theoretic transforms.

## 26. Worked Example: weekday arithmetic

Nếu Monday encode `0`, Tuesday `1`, ..., Sunday `6`, thì 100 days after Monday:

```math
100\equiv2\pmod7.
```

nên day là Wednesday.

Ta không cần enumerate 100 steps; modulo giữ lại đúng information relevant cho periodic state.

## 27. Proof strategy: work modulo small base để tìm impossibility

Suppose muốn chứng minh square integer không thể congruent 2 modulo 4.

Mọi integer là even hoặc odd.

Nếu `n=2k`:

```math
n^2=4k^2\equiv0\pmod4.
```

Nếu `n=2k+1`:

```math
n^2=4k^2+4k+1\equiv1\pmod4.
```

Vậy square chỉ remainder 0 hoặc 1 modulo 4, không thể 2.

Đây là proof technique rất mạnh: quotient infinite integer problem xuống finite residue classes.

## Mental Model

> Number theory nghiên cứu structure của integers dưới divisibility và multiplication. Modular arithmetic quotient infinite integers thành finite equivalence classes nhưng giữ đủ arithmetic structure để tính toán. GCD, inverse, prime factorization và congruence không phải tricks riêng lẻ; chúng là các mặt của cùng cấu trúc divisibility.

## Common Misconceptions

**“Modulo chỉ là remainder operator `%`.”** Không; mathematical modulo là equivalence relation/class structure.

**“Có thể chia modulo như ordinary arithmetic.”** Chỉ khi divisor invertible.

**“Prime factorization dễ vì theorem bảo tồn tại.”** Existence/uniqueness không nói factoring computationally cheap.

**“Fermat theorem áp cho mọi `a,p`.”** Cần conditions.

**“Modulo tự tạo hash distribution tốt.”** Không; upstream hashing và table design vẫn quyết định.
