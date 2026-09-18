# Cấu trúc đại số: group, ring và field

Khi học algebra ở trường, ta thường thao tác với numbers và symbols. **Đại số trừu tượng (Abstract Algebra / 추상대수학)** hỏi một câu sâu hơn: điều gì trong các phép tính thực sự quan trọng? Nếu ta bỏ đi bản chất “đây là số thực” và chỉ giữ rules của operations, nhiều systems rất khác nhau hóa ra có cùng structure.

Chương này giới thiệu group, ring và field ở mức nền tảng. Mục tiêu không phải biến bộ sách thành một course abstract algebra chuyên sâu, mà để các topics symmetry, modular arithmetic, linear algebra và cryptography có chung ngôn ngữ.

## Binary operation và closure

Một **phép toán hai ngôi (Binary Operation / 이항연산)** trên set `S` nhận hai elements của `S` và trả về một element của `S`:

```math
*:S\times S\to S.
```

Condition output vẫn nằm trong `S` gọi là **closure / 닫힘성**.

Addition trên integers closed vì tổng hai integers vẫn integer. Division trên integers không closed vì `1/2` không phải integer. Chỉ riêng observation này đã cho thấy một operation không thể được tách khỏi domain mà nó đang hoạt động.

## Group: structure của symmetry và reversible operations

Một **nhóm (Group / 군)** là set `G` với operation `*` thỏa bốn properties:

1. closure;
2. associativity: `(a*b)*c=a*(b*c)`;
3. có identity element `e` sao cho `e*a=a*e=a`;
4. mỗi `a` có inverse `a^{-1}` sao cho `a*a^{-1}=e`.

Nếu thêm commutativity `a*b=b*a`, group gọi là **Abelian group / 아벨군**.

Integers dưới addition tạo Abelian group: identity là `0`, inverse của `a` là `-a`. Nonzero real numbers dưới multiplication cũng là Abelian group: identity `1`, inverse `1/a`.

## Symmetry group

Hãy xét một hình vuông. Ta có thể rotate `0°,90°,180°,270°` hoặc reflect theo các axes/diagonals mà hình vẫn trùng với chính nó. Các transformations đó có thể compose; có identity; mỗi transformation có inverse. Chúng tạo **dihedral group** của square.

Đây là reason group theory gắn chặt với symmetry. Group không cần elements là numbers; elements có thể là rotations, permutations, matrices hoặc operations.

Trong graphics và robotics, rigid-body transformations compose thành algebraic structures. Trong cryptography, operations trên finite groups cung cấp mathematical setting cho nhiều protocols.

## Subgroup và generated structure

Một subset `H⊆G` là **subgroup / 부분군** nếu nó tự tạo group dưới cùng operation. Ví dụ even integers là subgroup của integers dưới addition.

Một element hoặc subset có thể **generate / 생성** subgroup bằng cách áp dụng operation và inverses lặp lại. Trong cyclic group, một element `g` generate toàn group:

```math
G=\{g^k\mid k\in\mathbb Z\}.
```

Trong modular addition `Z_n`, element `1` generate mọi residues. Element khác có thể generate chỉ subset tùy gcd với `n`.

## Homomorphism: map giữ structure

Một **đồng cấu (Homomorphism / 준동형사상)** giữa groups là map `f:G→H` sao cho

```math
f(a*b)=f(a)\circ f(b).
```

Map không nhất thiết giữ raw representation; nó giữ operation structure. Đây là concept recurring khắp mathematics: linear map giữ addition/scalar multiplication; graph homomorphism giữ adjacency theo nghĩa thích hợp; compiler transformations tốt cố giữ semantics dù representation đổi.

Kernel của homomorphism là elements map về identity. Image là phần của target thực sự reachable. Ideas kernel/image xuất hiện lại trong linear algebra như null space/range.

## Ring: hai operations tương tác

Một **vành (Ring / 환)** thường có addition và multiplication. Addition tạo Abelian group; multiplication associative; và multiplication distributive over addition:

```math
 a(b+c)=ab+ac,
\qquad
(a+b)c=ac+bc.
```

Integers `Z` là ring. Matrices `M_n(R)` cũng là ring dưới matrix addition/multiplication, nhưng multiplication generally không commutative.

Polynomials với coefficients trong một field tạo polynomial ring. Điều này giải thích tại sao factorization và roots có structural rules tương tự integer factorization nhưng không identical.

## Field: nơi division gần như luôn hợp lệ

Một **trường (Field / 체)** là commutative ring mà mọi nonzero element có multiplicative inverse. Real numbers `R`, rational numbers `Q` và complex numbers `C` là fields.

Finite field cũng tồn tại. Với prime `p`, residues modulo `p` tạo field `F_p` vì mọi nonzero residue coprime với `p`, nên có modular inverse.

Field quan trọng cho linear algebra: vector space được định nghĩa over a field. Khi nói vectors với real coefficients, underlying field là `R`; trong coding theory, vectors thường sống trên finite fields như `F_2`.

## Vì sao modulo composite không phải field

Xét `Z_6`. `2×3≡0 mod 6` dù cả 2 và 3 đều nonzero residues. Những elements này là **zero divisors / 영인자**. `2` không có multiplicative inverse modulo 6.

Vì vậy `Z_6` là ring nhưng không field. Ngược lại `Z_5` là field.

Điều này nối trực tiếp với condition modular inverse từ number theory:

```math
\gcd(a,n)=1.
```

Nếu `n` prime, mọi nonzero `a` thỏa condition.

## Permutations và composition

Một permutation là bijection từ finite set về chính nó. Permutations compose thành symmetric group `S_n`. Với `n≥3`, composition không commutative.

Điều này cho một example rất concrete về non-Abelian group. Thứ tự operations có ý nghĩa: swap A/B rồi B/C thường khác swap B/C rồi A/B. Trong software, sequence of state transformations cũng thường noncommutative; reorder operations có thể đổi result.

## Quotient idea và equivalence classes

Modular arithmetic có thể hiểu như quotient structure: integers được partition bởi equivalence relation

```math
a\sim b
\iff
a\equiv b\pmod n.
```

Mỗi residue class trở thành một element của `Z_n`. General abstract algebra dùng quotient groups/rings để “collapse” elements được xem equivalent và tạo structure mới.

Mental model này cũng liên hệ với data normalization và canonical representation trong computing: nhiều raw states có thể được xem là cùng một equivalence class nếu downstream behavior không phân biệt chúng.

## Connection với linear algebra

Vector spaces là algebraic structures với vector addition và scalar multiplication. Linear transformations là maps giữ structure:

```math
T(u+v)=T(u)+T(v),
\qquad
T(cv)=cT(v).
```

Kernel/image, quotient spaces, eigenstructure và matrix groups đều nằm trong cùng family ideas. Abstract algebra giúp nhìn linear algebra không chỉ là arrays of numbers mà là theory của structure-preserving transformations.

## Connection với cryptography và coding

Finite fields được dùng trong error-correcting codes, AES arithmetic và nhiều cryptographic constructions. Elliptic-curve cryptography dùng group law trên points của elliptic curve over finite fields.

Điều quan trọng là cryptographic security không đến chỉ từ “có group/field”. Nó phụ thuộc hardness assumptions, parameter sizes, protocols, randomness và implementation. Algebra cung cấp structure; security engineering cần nhiều lớp khác.

## Mental Model

> Abstract algebra bỏ bớt “object này làm bằng gì” để giữ lại “operations của nó tuân theo luật nào”. Group là reversible composition, ring là addition + multiplication có distributivity, field là môi trường mà nonzero division hoạt động. Khi hai domains share cùng algebraic structure, một theorem có thể áp dụng cho cả hai dù objects nhìn hoàn toàn khác.

## Common Misconceptions

“Group” không có nghĩa một collection bất kỳ; operation là một phần bắt buộc của definition. Cùng set với operation khác có thể tạo structure khác.

Ring không nhất thiết có commutative multiplication, và conventions về multiplicative identity có thể khác giữa textbooks. Khi đọc tài liệu, cần check definition đang dùng.

Field không phải “mọi thứ đều chia được”: division by zero vẫn undefined. Property là mọi **nonzero** element có multiplicative inverse.
