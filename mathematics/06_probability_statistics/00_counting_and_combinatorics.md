# Đếm và tổ hợp: cấu trúc của không gian khả năng

Tổ hợp (combinatorics / 조합론) nghiên cứu cách đếm số cấu hình có thể có mà không cần liệt kê từng trường hợp. Đây là nền của xác suất rời rạc, complexity, search space, hashing, coding và nhiều bài toán tối ưu.

Mental model quan trọng:

```text
object space
→ decompose choices
→ remove symmetry / double counting
→ count configurations
→ infer probability or computational cost
```

Combinatorics không chỉ là nhớ `n!` hay `C(n,k)`. Nó là kỹ năng nhìn một configuration như kết quả của nhiều quyết định nhỏ hơn.

## 1. Rule of sum và rule of product

Nếu một task có hai nhóm cases **rời nhau**, với `m` và `n` possibilities, total:

```math
m+n.
```

Nếu một process có hai stages, stage 1 có `m` choices và với mỗi choice stage 2 có `n` choices, total:

```math
mn.
```

Product rule là nền của rất nhiều công thức đếm.

Ví dụ password gồm 8 lowercase letters:

```math
26^8
```

possible strings, nếu repetition được phép.

## 2. Khi nào product rule sai?

Product rule không yêu cầu probability independence, nhưng yêu cầu cấu trúc choice count ở mỗi stage được biết rõ.

Nếu number of choices stage sau phụ thuộc vào stage trước, ta phải cộng theo branches:

```math
\sum_i \text{choices after branch }i.
```

Ví dụ chọn two distinct digits: digit đầu có 10 choices, digit sau chỉ còn 9:

```math
10\cdot9.
```

Không thể dùng `10^2` nếu repetition bị cấm.

## 3. Permutation: order tạo configuration mới

Sắp `n` distinct objects:

```math
n!=n(n-1)\cdots1.
```

Chọn và sắp `k` từ `n`:

```math
P(n,k)=\frac{n!}{(n-k)!}.
```

Key question luôn là:

> Đổi thứ tự có tạo outcome khác không?

Nếu có, permutation-like counting phù hợp.

## 4. Combination: quotient out order

Nếu order không matter, mỗi subset size `k` bị permutation count lặp `k!` lần, nên:

```math
\binom nk=\frac{n!}{k!(n-k)!}.
```

Combination có symmetry:

```math
\binom nk=\binom n{n-k}.
```

Lý do: chọn `k` phần tử để giữ tương đương chọn `n-k` phần tử để bỏ.

## 5. Binomial coefficient như nhiều thứ cùng lúc

`\binom nk` không chỉ là “công thức chọn”. Nó đồng thời là:

```text
number of k-subsets
coefficient trong (a+b)^n
number of binary strings length n có exactly k ones
number of paths với k moves theo một direction
```

Connections này rất quan trọng vì cùng một structure xuất hiện dưới nhiều representations.

## 6. Binomial theorem từ counting choices

Trong:

```math
(a+b)^n,
```

mỗi factor đóng góp `a` hoặc `b`.

Muốn term chứa `b^k`, ta chọn `k` trong `n` factors lấy `b`:

```math
(a+b)^n=
\sum_{k=0}^n
\binom nk a^{n-k}b^k.
```

Coefficient không xuất hiện magic; nó đếm số ways tạo cùng monomial.

## 7. Pascal identity

```math
\binom nk
=
\binom{n-1}{k}
+
\binom{n-1}{k-1}.
```

Proof idea: chọn `k` từ `n` objects. Fix một object đặc biệt.

Cases:

```text
không chọn object đó → C(n-1,k)
chọn object đó → C(n-1,k-1)
```

Hai cases rời nhau và cover toàn bộ possibilities.

Đây là classic combinatorial proof: chứng minh identity bằng cách đếm cùng một set theo hai cách.

## 8. Stars and bars

Số nonnegative integer solutions của:

```math
x_1+\cdots+x_k=n
```

là:

```math
\binom{n+k-1}{k-1}.
```

Ta encode `n` identical items bằng stars và `k-1` separators bằng bars.

Ví dụ:

```text
***|*||**
```

có thể encode distribution `(3,1,0,2)`.

Assumption quan trọng: items identical, boxes distinguishable, values nonnegative.

Nếu constraints đổi, formula cũng đổi.

## 9. Inclusion–exclusion: sửa double counting

Hai sets:

```math
|A\cup B|
=|A|+|B|-|A\cap B|.
```

Ba sets:

```math
|A\cup B\cup C|
=
|A|+|B|+|C|
-|A\cap B|-|A\cap C|-|B\cap C|
+|A\cap B\cap C|.
```

Pattern alternating signs vì intersections bị đếm thừa nhiều lần.

Inclusion–exclusion là một primitive rất quan trọng trong probability và discrete mathematics.

## 10. Complement counting

Nhiều bài dễ hơn nếu đếm complement trước.

Birthday collision:

```math
P(\text{at least one collision})
=1-P(\text{no collision}).
```

Với `n` people, idealized 365 equally likely birthdays:

```math
P(\text{no collision})
=
\frac{365}{365}
\frac{364}{365}
\cdots
\frac{365-n+1}{365}.
```

Complement strategy là pattern general: “at least one” thường dễ xử lý qua “none”.

## 11. Pigeonhole principle

Nếu nhiều hơn `n` objects được map vào `n` boxes, ít nhất một box nhận ≥2 objects.

Generalized form: `N` objects vào `k` boxes ⇒ có box chứa ít nhất

```math
\left\lceil\frac Nk\right\rceil
```

objects.

Trong hashing, collision là unavoidable nếu key space lớn hơn bucket space. Good hash chỉ phân bố collisions tốt hơn; không loại được định lý.

## 12. Bijection proof

Một technique mạnh là tìm bijection giữa hai sets để chứng minh chúng có cùng cardinality.

Ví dụ `k`-subsets của `n` objects biject với `(n-k)`-subsets bằng complement map.

Bijection không chỉ chứng minh count; nó giải thích **vì sao** hai quantities giống nhau.

## 13. Recurrence trong counting

Nhiều counting sequences thỏa recurrence.

Ví dụ binary strings length `n` không chứa consecutive `1` có count liên hệ Fibonacci.

Reasoning: split theo last bit.

```text
ends in 0 → previous n-1 bits valid
ends in 1 → previous bit phải 0 → reduce về n-2
```

Do đó:

```math
a_n=a_{n-1}+a_{n-2}.
```

Combinatorics và recurrence/DP gặp nhau ở đây.

## 14. Generating functions intuition

Nếu sequence counts là `a_n`, generating function:

```math
A(x)=\sum_{n\ge0}a_nx^n.
```

Nó encode whole count sequence vào một algebraic object.

Operations trên generating functions có thể transform recurrence thành algebra. Đây là advanced bridge giữa combinatorics, power series và algorithm analysis.

## 15. Asymptotic counting

Exact count không phải lúc nào cần thiết. Với large `n`, growth class thường quan trọng hơn.

Ví dụ:

```math
n!\gg c^n\gg n^k
```

cho fixed `c>1`, `k`.

Stirling approximation:

```math
n!\approx\sqrt{2\pi n}\left(\frac ne\right)^n.
```

Nó cho logarithm của factorial gần:

```math
\log n!\approx n\log n-n.
```

Điều này xuất hiện trong entropy, counting states và complexity.

## 16. Search-space explosion

`n` independent binary decisions tạo:

```math
2^n
```

subsets.

Permutation search tạo:

```math
n!
```

possibilities.

Đây là lý do brute force nhanh chóng bất khả thi. Complexity thường bắt đầu từ combinatorial count của search space.

## 17. Counting và probability

Khi outcomes equally likely:

```math
P(A)=\frac{|A|}{|\Omega|}.
```

Nhưng combinatorics chỉ cung cấp counts. Assumption equally likely phải đến từ probability model.

Sai lầm phổ biến là đếm đúng nhưng model xác suất sai.

## 18. Hypergeometric vs binomial connection

Sampling **without replacement** tạo dependence.

Nếu population có `K` successes trong `N`, draw `n` without replacement, số successes `X` có hypergeometric probability:

```math
P(X=k)
=
\frac{\binom Kk\binom{N-K}{n-k}}
{\binom Nn}.
```

Binomial phù hợp hơn khi trials independent với constant success probability.

Combinatorial structure giúp thấy assumption difference ngay lập tức.

## 19. Worked example: committee constraint

Có 6 engineers và 4 designers. Chọn committee 4 người có ít nhất 1 designer.

Total committees:

```math
\binom{10}{4}=210.
```

Committees không có designer:

```math
\binom64=15.
```

Vậy valid:

```math
210-15=195.
```

Complement counting đơn giản hơn sum cases theo number designers.

## 20. AI, coding và combinatorics

Feature subset selection có `2^d` subsets. Sequence models có vocabulary `V` và length `n` tạo raw string space size `V^n`. Error-correcting codes chọn codewords trong Hamming space với distance constraints.

Trong AI, combinatorial explosion giải thích vì sao search cần heuristics, dynamic programming, branch-and-bound hoặc approximation.

## Mental Model

> Combinatorics là algebra của finite possibility spaces. Product rule tạo choices; symmetry loại overcount; inclusion–exclusion sửa overlap; bijection giải thích equal counts; asymptotics cho biết space lớn nhanh đến mức nào.

## Common Misconceptions

Permutation và combination khác ở việc order có meaning hay không. Counting product rule không phải probability independence. `n!` và `2^n` đều “lớn” nhưng growth rất khác. Đếm favorable/total chỉ cho probability khi outcomes thực sự equiprobable theo model.
