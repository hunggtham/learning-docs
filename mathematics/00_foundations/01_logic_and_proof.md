# Logic và chứng minh

Logic (Logic / 논리) là hạ tầng của suy luận toán học. Nó không quyết định tiền đề của ta có đúng ngoài đời hay không; nó quyết định nếu chấp nhận các tiền đề đó thì kết luận nào bắt buộc theo sau. Điều này giống một type checker cho reasoning: nó không đảm bảo business requirement đúng, nhưng có thể phát hiện những phép suy luận không hợp lệ trong hệ quy tắc đã định.

## Mệnh đề và giá trị chân lý

Mệnh đề (Proposition / 명제) là câu có thể được gán giá trị đúng hoặc sai trong ngữ cảnh xác định. “7 là số nguyên tố” là mệnh đề. “Hãy mở cửa” không phải mệnh đề vì đó là mệnh lệnh. “x > 3” chưa phải một mệnh đề hoàn chỉnh nếu chưa biết `x` hoặc chưa lượng hóa nó.

Ký hiệu thường dùng:

```text
p, q, r
```

để đại diện cho các mệnh đề.

## Phủ định

Phủ định (Negation / 부정) của `p`, ký hiệu

```math
\neg p
```

có giá trị chân lý ngược lại với `p`.

Nếu `p` là “x > 5”, phủ định chính xác là

```math
x \le 5
```

không phải chỉ `x < 5`, vì trường hợp `x=5` cũng phải nằm trong phủ định.

## AND, OR và XOR

Phép hội (Conjunction / 논리곱) `p∧q` đúng khi cả hai đúng.

Phép tuyển (Disjunction / 논리합) `p∨q` trong logic toán thường là inclusive OR: đúng nếu ít nhất một trong hai đúng, kể cả khi cả hai đều đúng.

XOR (Exclusive OR / 배타적 논리합) đúng khi chính xác một trong hai đúng.

Trong programming, khác biệt inclusive OR và XOR xuất hiện trực tiếp trong boolean expressions và bit operations.

## Implication: nếu p thì q

Mệnh đề kéo theo (Implication / 함의)

```math
p\Rightarrow q
```

chỉ sai khi `p` đúng nhưng `q` sai.

Điều này ban đầu dễ gây khó hiểu. Tại sao nếu `p` sai thì implication được xem là đúng? Vì implication tuyên bố rằng không tồn tại trường hợp `p` xảy ra mà `q` không xảy ra. Nếu `p` không xảy ra, ta chưa tìm được counterexample cho claim đó.

Trong requirements, “nếu user là admin thì user được phép truy cập” không nói gì về non-admin. Một lỗi reasoning phổ biến là suy ngược rằng “nếu được phép truy cập thì chắc chắn là admin”. Điều đó không đi theo implication ban đầu.

## Converse, inverse và contrapositive

Từ

```math
p\Rightarrow q
```

ta có converse

```math
q\Rightarrow p
```

và contrapositive

```math
\neg q\Rightarrow \neg p.
```

Implication ban đầu luôn logically equivalent với contrapositive, nhưng không nhất thiết equivalent với converse.

Ví dụ:

> Nếu một integer chia hết cho 4 thì nó chẵn.

Contrapositive:

> Nếu integer không chẵn thì nó không chia hết cho 4.

đúng.

Converse:

> Nếu integer chẵn thì nó chia hết cho 4.

sai; `6` là counterexample.

## Necessary và sufficient

Nếu

```math
p\Rightarrow q,
```

thì `p` là sufficient condition cho `q`, còn `q` là necessary condition cho `p`.

Ví dụ chia hết cho 4 là sufficient để chẵn. Chẵn là necessary để chia hết cho 4.

Nếu cả hai chiều đúng:

```math
p\Leftrightarrow q
```

ta có “if and only if”, hay điều kiện cần và đủ (Necessary and sufficient condition / 필요충분조건).

## Quantifiers

Lượng từ phổ quát (Universal quantifier / 전칭 기호)

```math
\forall x
```

nghĩa là “với mọi x”.

Lượng từ tồn tại (Existential quantifier / 존재 기호)

```math
\exists x
```

nghĩa là “tồn tại ít nhất một x”.

Negation phải đổi quantifier:

```math
\neg(\forall x\,P(x))
\equiv
\exists x\,\neg P(x)
```

Tức “không phải mọi request đều thành công” nghĩa là “có ít nhất một request không thành công”.

Tương tự:

```math
\neg(\exists x\,P(x))
\equiv
\forall x\,\neg P(x).
```

## De Morgan's laws

Cho propositions:

```math
\neg(p\land q)
\equiv
\neg p\lor\neg q
```

và

```math
\neg(p\lor q)
\equiv
\neg p\land\neg q.
```

Trong set theory, cùng cấu trúc trở thành De Morgan cho union/intersection. Trong code, nó giúp refactor conditions:

```text
!(isAdmin && isActive)
```

tương đương

```text
!isAdmin || !isActive
```

## Direct proof

Direct proof bắt đầu từ assumptions rồi dùng định nghĩa và kết quả đã biết.

Chứng minh tổng hai số chẵn là chẵn. Cho

```math
a=2m,\qquad b=2n.
```

Khi đó

```math
a+b=2(m+n)
```

nên là số chẵn.

Điểm mạnh nằm ở việc dùng definition “even = 2×integer”.

## Proof by contradiction

Chứng minh phản chứng (Proof by contradiction / 귀류법) giả sử phủ định của điều muốn chứng minh, rồi dẫn tới contradiction.

Ví dụ kinh điển: `√2` là irrational. Giả sử

```math
\sqrt2=\frac ab
```

với `a,b` là integers tối giản. Bình phương:

```math
a^2=2b^2.
```

`a^2` chẵn nên `a` chẵn; đặt `a=2k`. Khi đó

```math
4k^2=2b^2
\Rightarrow b^2=2k^2,
```

nên `b` cũng chẵn. Vậy `a,b` cùng có factor 2, mâu thuẫn với giả định phân số tối giản.

## Mathematical induction

Quy nạp toán học (Mathematical induction / 수학적 귀납법) chứng minh statement `P(n)` cho integers bằng hai bước: base case và inductive step.

Ví dụ

```math
1+2+\cdots+n=\frac{n(n+1)}2.
```

Base case `n=1` đúng.

Giả sử đúng cho `n=k`:

```math
1+\cdots+k=\frac{k(k+1)}2.
```

Với `k+1`:

```math
1+\cdots+k+(k+1)
=
\frac{k(k+1)}2+(k+1)
```

```math
=
(k+1)\left(\frac k2+1\right)
=
\frac{(k+1)(k+2)}2.
```

Nên statement đúng cho `k+1`.

Induction rất gần recursive reasoning trong computer science: nếu base case đúng và một instance đúng kéo theo next instance đúng, chain bao phủ toàn bộ domain.

## Proof và testing không thay thế nhau

Testing nhiều input có thể tăng confidence nhưng không chứng minh một universal statement trên infinite input domain. Proof có thể chứng minh algorithm đúng theo specification, nhưng proof không đảm bảo specification phản ánh đúng nhu cầu business hoặc code không có lỗi implementation nếu proof chỉ áp dụng cho model khác.

Formal verification cố thu hẹp khoảng cách này bằng cách biểu diễn specification và implementation trong systems có thể reasoning machine-checkable.

## Mental Model

> Logic là hệ thống quản lý “được phép kết luận gì từ điều gì”. Proof là chương trình chạy trong hệ thống đó: assumptions là input, inference rules là operations, theorem là output.

## Common Misconceptions

`p→q` không có nghĩa `q→p`. “Không chứng minh được p” không tự động chứng minh `¬p`. Một nghìn example phù hợp không thay proof cho universal claim, trong khi một counterexample hợp lệ đủ để phá universal claim.
