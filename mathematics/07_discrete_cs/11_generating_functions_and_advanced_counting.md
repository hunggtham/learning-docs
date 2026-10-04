# Generating functions và advanced counting: biến bài toán đếm thành algebra

> **Mạch đọc:** Chapter này đi sau [Đếm và tổ hợp](../06_probability_statistics/00_counting_and_combinatorics.md) và [Dãy, chuỗi và recurrence](../02_functions/03_sequences_series_and_recurrence.md). Mục tiêu là đi từ “đếm trực tiếp” sang một cách nhìn mạnh hơn: encode cả một dãy số đếm vào một hàm, rồi dùng algebra để thao tác trên dãy đó.

Tổ hợp (combinatorics / 조합론) thường bắt đầu bằng permutation, combination, inclusion–exclusion và recurrence. Nhưng nhiều bài toán khó không có công thức đóng dễ nhìn. Ta có thể biết dãy số phải thỏa một recurrence, hoặc biết mỗi object được ghép từ nhiều thành phần, nhưng việc đếm trực tiếp vẫn rối.

**Hàm sinh (generating function / 생성함수)** giải quyết vấn đề này bằng một bước đổi biểu diễn:

```text
sequence of numbers
      ↓ encode
formal power series
      ↓ algebra
coefficient extraction
      ↓ decode
answer to counting problem
```

Điểm quan trọng là generating function thường không được dùng như một ordinary numerical function để “thế x = 0.7 rồi tính”. Nó chủ yếu là một **container đại số cho coefficients**.

---

## 1. Ordinary generating function là gì?

Cho một dãy

```math
a_0,a_1,a_2,\ldots
```

**ordinary generating function — OGF (일반 생성함수)** của dãy là

```math
A(x)=\sum_{n\ge0}a_nx^n.
```

Ví dụ nếu

```math
a_n=1
```

cho mọi `n≥0`, thì

```math
A(x)=1+x+x^2+x^3+\cdots.
```

Formal identity quen thuộc:

```math
A(x)=\frac1{1-x}.
```

Trong combinatorics, câu quan trọng là:

```math
[x^n]A(x)=a_n,
```

trong đó `[x^n]A(x)` nghĩa coefficient của `x^n` trong `A(x)`.

Ta có thể coi generating function như một “database nén” chứa toàn bộ dãy `a_n`.

---

## 2. Formal power series khác analytic power series

Trong calculus/analysis, power series thường đi cùng câu hỏi hội tụ:

```math
\sum a_nx^n
```

hội tụ với những `x` nào?

Trong **formal power series (형식적 멱급수)**, ta tạm bỏ câu hỏi numeric convergence. Ta chỉ thao tác coefficients theo algebraic rules.

Ví dụ:

```math
(1-x)(1+x+x^2+x^3+\cdots)=1
```

được hiểu coefficient-by-coefficient.

Điều này cho phép dùng identity

```math
\frac1{1-x}=\sum_{n\ge0}x^n
```

như một algebraic identity của formal series.

Khi bài toán cần analytic asymptotics, convergence trở lại quan trọng. Nhưng cho nhiều bài counting elementary, formal viewpoint đủ và sạch hơn.

---

## 3. Addition của generating functions = chia bài toán thành cases

Nếu

```math
A(x)=\sum a_nx^n,
\qquad
B(x)=\sum b_nx^n,
```

thì

```math
A(x)+B(x)=\sum (a_n+b_n)x^n.
```

Vì vậy addition tương ứng với việc count hai families rời nhau.

Ví dụ nếu `a_n` đếm valid strings type A và `b_n` đếm valid strings type B, không overlap, thì total count

```math
c_n=a_n+b_n
```

có generating function

```math
C(x)=A(x)+B(x).
```

Đây là generating-function version của rule of sum.

---

## 4. Multiplication = ghép hai structures và convolution

Product:

```math
A(x)B(x)
=
\left(\sum_{i\ge0}a_ix^i\right)
\left(\sum_{j\ge0}b_jx^j\right).
```

Coefficient của `x^n` là

```math
[x^n]A(x)B(x)
=
\sum_{k=0}^{n}a_kb_{n-k}.
```

Đây là **convolution (합성곱)**.

Combinatorial meaning:

> Nếu một object size `n` được ghép từ object A size `k` và object B size `n-k`, product của generating functions tự động cộng qua mọi cách chia size.

Ví dụ:

```text
left component size k
+
right component size n-k
```

cho mọi `k=0,...,n`.

Đây là reason multiplication của generating functions mạnh: nó encode toàn bộ “chia tổng size giữa các thành phần” trong một phép nhân.

---

## 5. Shift của sequence = nhân với x

Nếu

```math
A(x)=a_0+a_1x+a_2x^2+\cdots,
```

thì

```math
xA(x)=a_0x+a_1x^2+a_2x^3+\cdots.
```

Multiplication by `x` dịch index lên một bước.

Tương tự:

```math
x^kA(x)
```

dịch `k` bước.

Điều này là chìa khóa để biến recurrence thành algebraic equation.

---

## 6. Từ recurrence Fibonacci đến generating function

Cho

```math
F_0=0,\qquad F_1=1,
```

và

```math
F_n=F_{n-1}+F_{n-2},\qquad n\ge2.
```

Đặt

```math
F(x)=\sum_{n\ge0}F_nx^n.
```

Viết recurrence dưới dạng sum:

```math
\sum_{n\ge2}F_nx^n
=
\sum_{n\ge2}F_{n-1}x^n
+
\sum_{n\ge2}F_{n-2}x^n.
```

Left side:

```math
F(x)-F_0-F_1x=F(x)-x.
```

First right side:

```math
x\sum_{n\ge2}F_{n-1}x^{n-1}=xF(x).
```

Second right side:

```math
x^2\sum_{n\ge2}F_{n-2}x^{n-2}=x^2F(x).
```

Do đó:

```math
F(x)-x=xF(x)+x^2F(x).
```

Suy ra:

```math
F(x)=\frac{x}{1-x-x^2}.
```

Một recurrence vô hạn đã trở thành một rational expression hữu hạn.

Đây là core pattern:

```text
recurrence
→ multiply by x^n
→ sum over n
→ shift indices
→ solve algebraically for generating function
```

---

## 7. Partial fractions giúp lấy closed form

Denominator

```math
1-x-x^2
```

factor theo roots liên quan đến golden ratio.

Sau partial fraction decomposition, ta thu được coefficient formula tương đương Binet formula.

Điểm cần học không phải memorize Binet formula. Quan trọng là:

> Recurrence linear với constant coefficients thường tạo rational generating function, và poles của generating function encode exponential growth modes của sequence.

Điều này nối trực tiếp với characteristic roots trong recurrence và eigenvalues trong linear algebra.

---

## 8. Generating function của một số building blocks

Một vài patterns rất hay gặp.

### Chọn bất kỳ số lượng objects giống nhau

```math
1+x+x^2+\cdots=\frac1{1-x}.
```

### Chọn tối đa một object

```math
1+x.
```

### Chọn ít nhất một

```math
x+x^2+x^3+\cdots=\frac{x}{1-x}.
```

### Chọn số lượng chẵn

```math
1+x^2+x^4+\cdots=\frac1{1-x^2}.
```

Các factors này có thể nhân với nhau để encode constraints độc lập trên tổng size.

---

## 9. Coin-change như coefficient extraction

Giả sử có coin denominations `1,2,5`, mỗi loại dùng không giới hạn.

Generating function:

```math
\frac1{1-x}
\frac1{1-x^2}
\frac1{1-x^5}.
```

Coefficient

```math
[x^n]
\frac1{(1-x)(1-x^2)(1-x^5)}
```

là số ways tạo total `n` nếu thứ tự coin không được phân biệt.

Tại sao?

- factor `1/(1-x)` chọn số coin 1;
- factor `1/(1-x^2)` chọn số coin 2;
- factor `1/(1-x^5)` chọn số coin 5;
- multiplication cộng exponents, tức cộng total value.

Generating functions biến constraints cộng thành multiplication của series.

---

## 10. Bounded choices

Nếu item weight `w` được dùng tối đa `m` lần:

```math
1+x^w+x^{2w}+\cdots+x^{mw}.
```

Ví dụ coin `5` dùng tối đa hai lần:

```math
1+x^5+x^{10}.
```

Điều này giúp model inventory limits, bounded integer partitions và resource allocation.

---

## 11. Integer partitions

Một **partition (phân hoạch số nguyên / 정수 분할)** của `n` là cách viết `n` thành sum của positive integers, bỏ qua order.

Generating function kinh điển:

```math
P(x)
=
\prod_{k=1}^{\infty}\frac1{1-x^k}.
```

Vì factor cho `k`:

```math
1+x^k+x^{2k}+\cdots
```

cho phép chọn `0,1,2,...` copies của part size `k`.

Coefficient `[x^n]P(x)` đếm partitions của `n`.

Ví dụ này cho thấy infinite product không phải decorative formula: mỗi factor đại diện cho một independent combinatorial choice.

---

## 12. Differentiation của generating function encode weighted indices

Nếu

```math
A(x)=\sum_{n\ge0}a_nx^n,
```

thì formally

```math
A'(x)=\sum_{n\ge1}na_nx^{n-1}.
```

Do đó

```math
xA'(x)=\sum_{n\ge1}na_nx^n.
```

Operator

```math
x\frac d{dx}
```

biến coefficient `a_n` thành `na_n`.

Điều này hữu ích khi counts được weight bởi size hoặc khi cần moments trong probability generating functions.

---

## 13. Probability generating function

Nếu random variable rời rạc không âm `X` có

```math
P(X=n)=p_n,
```

thì **probability generating function — PGF (확률 생성함수)**:

```math
G_X(s)=\mathbb E[s^X]
=\sum_{n\ge0}p_ns^n.
```

Ta có:

```math
G_X(1)=1.
```

Và khi conditions phù hợp:

```math
G_X'(1)=\mathbb E[X].
```

Nếu `X,Y` independent nonnegative integer-valued, thì

```math
G_{X+Y}(s)=G_X(s)G_Y(s).
```

Lý do chính là independence biến expectation của product thành product của expectations.

Đây là same algebraic multiplication/convolution pattern như combinatorics.

---

## 14. Exponential generating functions

Với labeled structures, ordinary generating function đôi khi không tự nhiên.

**Exponential generating function — EGF (지수 생성함수)**:

```math
A(x)=\sum_{n\ge0}a_n\frac{x^n}{n!}.
```

Factor `n!` xuất hiện vì labels có permutations.

EGF đặc biệt hợp với structures trên labeled sets: permutations, set partitions, labeled trees và nhiều combinatorial classes.

Mental distinction:

```text
OGF → thường hợp cho unlabeled size-composition
EGF → thường hợp cho labeled combinatorial structures
```

Đây là heuristic, không phải luật tuyệt đối.

---

## 15. Derangements và inclusion–exclusion

Một derangement là permutation không có fixed point.

Inclusion–exclusion cho count:

```math
D_n
=
n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.
```

Asymptotically:

```math
D_n\approx \frac{n!}{e}.
```

Đây là example tốt cho thấy combinatorics hiện đại dùng nhiều representations cùng lúc:

```text
permutation structure
→ inclusion–exclusion
→ exponential series
→ asymptotic approximation
```

Không nên cố ép mọi problem vào một single technique.

---

## 16. The probabilistic method: chứng minh tồn tại bằng randomness

Một trong những ideas mạnh nhất của modern combinatorics là **phương pháp xác suất (probabilistic method / 확률적 방법)**.

Pattern:

1. define random object;
2. define bad quantity/event;
3. show probability bad outcome < 1, hoặc expected bad count < 1;
4. conclude tồn tại ít nhất một object tốt.

Ta có thể chứng minh existence mà không construct object explicitly.

Ví dụ nếu random construction có

```math
P(\text{good})>0,
```

thì logically phải có ít nhất một good object.

Điểm sâu:

> Randomness ở đây là công cụ chứng minh existence, không có nghĩa object cần “thực sự random” khi được sử dụng.

---

## 17. First-moment method

Nếu `X` là số bad structures và

```math
\mathbb E[X]<1,
```

thì phải tồn tại một outcome với

```math
X=0.
```

Lý do: `X` nonnegative integer. Nếu mọi outcome đều có ít nhất một bad structure thì expectation không thể < 1.

Đây là **first-moment method (일차 모멘트 방법)**.

Nó biến combinatorial existence thành expected-value calculation.

---

## 18. Linearity of expectation không cần independence

Nếu

```math
X=X_1+\cdots+X_m,
```

thì luôn có

```math
\mathbb E[X]
=
\sum_{i=1}^{m}\mathbb E[X_i],
```

ngay cả khi các `X_i` dependent.

Đây là lý do indicator variables rất mạnh trong counting/probabilistic arguments.

Ta có thể count expected number of collisions, inversions, fixed points hoặc violated constraints bằng cách sum local indicators.

---

## 19. Burnside và Pólya: quotient symmetry trước khi đếm

Một vấn đề counting khó thường đến từ symmetry: nhiều raw configurations đại diện cho cùng object.

Nếu group `G` acts trên set `X`, **Burnside's lemma (번사이드 보조정리)** cho số orbits:

```math
|X/G|
=
\frac1{|G|}
\sum_{g\in G}|\operatorname{Fix}(g)|.
```

Interpretation:

> số cấu hình “khác nhau thật sự” = average số configurations được giữ nguyên bởi mỗi symmetry.

Điều này nối trực tiếp với [Group actions](./09_abstract_algebra_quotients_actions_and_field_extensions.md).

Pólya enumeration mở rộng idea này để count colorings dưới symmetry bằng cycle index.

---

## 20. Tại sao generating functions hữu ích cho algorithms?

Không phải mọi generating-function proof trực tiếp trở thành fast algorithm. Nhưng same structure xuất hiện trong computation:

- convolution ↔ polynomial multiplication;
- recurrence ↔ rational generating function;
- coefficient extraction ↔ dynamic programming;
- FFT ↔ fast convolution;
- transfer matrix ↔ state transition counting;
- probability generating functions ↔ branching/random processes.

Ví dụ naive convolution length `n` tốn roughly

```math
O(n^2),
```

trong khi FFT-based multiplication có thể giảm về gần

```math
O(n\log n).
```

Đây là bridge combinatorics ↔ algebra ↔ numerical algorithms.

---

## 21. Generating function không phải magic formula

Failure modes phổ biến:

**Chọn sai object size.** Nếu exponent không encode đúng quantity cần đếm, coefficient extraction trả lời một câu hỏi khác.

**Nhân khi choices không independent về combinatorial structure.** Product rule cần decomposition rõ thành components.

**Quên symmetry/order.** Coin-change ordered compositions khác unordered partitions.

**Nhầm formal với analytic convergence.** Formal manipulation có thể đúng coefficient-wise dù numeric substitution không hội tụ.

**Có generating function nhưng không extract được coefficient dễ dàng.** Encode problem chỉ là nửa đầu; cần algebra, recurrence, complex analysis hoặc asymptotics để decode.

---

## 22. Mental model

> Generating function không phải một “hàm để tính giá trị”; nó là một representation của cả sequence. Addition encode union of cases, multiplication encode composition và convolution, differentiation encode weighting by index, còn algebraic singularities encode long-run growth. Khi một counting problem có recurrence hoặc được ghép từ independent-sized components, generating functions biến combinatorial structure thành algebra.

---

## 23. Mạch học tiếp

Nếu muốn đi sâu hơn:

```text
Counting basics
→ Recurrences
→ Generating functions
→ Analytic/asymptotic methods
```

hoặc:

```text
Counting
→ Graph theory
→ Network flows / matching
→ Discrete optimization
```

Đọc tiếp:

- [Network flows, matching và max-flow min-cut](./12_network_flows_matchings_and_min_cut.md)
- [Advanced abstract algebra](./09_abstract_algebra_quotients_actions_and_field_extensions.md)
- [Fourier, signals và frequency](../09_connections/05_fourier_signals_and_frequency.md) để thấy convolution xuất hiện trong continuous/discrete signal analysis.

## Further reading

- Herbert S. Wilf — *generatingfunctionology*, University of Pennsylvania.
- Mitchel T. Keller, William T. Trotter — *Applied Combinatorics*, đặc biệt các phần về generating functions, recurrence, Pólya enumeration và probabilistic methods.
