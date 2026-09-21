# Logic và chứng minh: ngôn ngữ của suy luận đúng

Logic (logic / 논리) không nói một tiền đề có đúng ngoài đời hay không. Nó trả lời câu hỏi khác: **nếu chấp nhận các tiền đề hiện có, kết luận nào thực sự theo sau?** Đây là lý do logic đứng trước proof, discrete mathematics, algorithms, probability, database predicates và formal verification.

Một cách nhìn hữu ích là tách ba tầng:

```text
mô hình / giả định
→ quy tắc suy luận
→ kết luận
```

Nếu assumption sai, reasoning hoàn hảo vẫn có thể cho conclusion vô ích. Nếu assumption đúng nhưng inference sai, conclusion không được bảo đảm. Vì vậy mathematical rigor không thay thế modeling judgment; hai việc giải quyết hai loại lỗi khác nhau.

## 1. Mệnh đề: đơn vị cơ bản của reasoning

Mệnh đề (proposition / 명제) là câu có thể được gán giá trị đúng hoặc sai trong một ngữ cảnh xác định.

“7 là số nguyên tố” là một proposition. “Mở cửa đi” không phải proposition vì đó là command. Câu `x > 3` chưa phải một proposition hoàn chỉnh nếu `x` chưa được gán hoặc chưa được lượng hóa.

Ta thường ký hiệu propositions bằng `p`, `q`, `r`.

Phủ định (negation / 부정) của `p` được viết

```math
\neg p.
```

Nếu `p` là `x>5`, phủ định chính xác là

```math
x\le 5,
```

không phải chỉ `x<5`, vì phủ định phải bao phủ **mọi case không thuộc statement gốc**.

Đây là một pattern quan trọng: khi negate một claim, ta không đoán câu “nghe đối lập”; ta lấy complement logic của toàn bộ condition.

## 2. AND, OR, XOR và cách conditions tạo cấu trúc

Phép hội (conjunction / 논리곱)

```math
p\land q
```

chỉ đúng khi cả `p` và `q` đúng.

Phép tuyển (disjunction / 논리합)

```math
p\lor q
```

trong toán học thường là inclusive OR: ít nhất một proposition đúng, kể cả trường hợp cả hai cùng đúng.

XOR (exclusive OR / 배타적 논리합) chỉ đúng khi chính xác một trong hai đúng.

Điểm đáng học không phải bảng truth table riêng lẻ mà là việc **compound condition có thể được xem như một object toán học**. Điều này nối trực tiếp sang Boolean algebra, circuit design, SQL predicates và program guards.

## 3. Implication: statement về việc counterexample không được phép tồn tại

Implication

```math
p\Rightarrow q
```

thường được đọc “nếu `p` thì `q`”. Nó chỉ sai khi `p` đúng và `q` sai.

Tại sao khi `p` sai implication lại không bị xem là sai? Vì claim thực chất nói:

> Không tồn tại trường hợp nào `p` xảy ra nhưng `q` không xảy ra.

Một counterexample của `p→q` phải thỏa

```text
p = true
q = false
```

Ví dụ:

> Nếu một integer chia hết cho 4 thì nó chẵn.

Muốn bác bỏ, cần tìm một số chia hết cho 4 nhưng không chẵn. Không tìm được chỉ bằng vài examples chưa phải proof, nhưng nó cho ta biết **dạng counterexample cần tìm**.

Trong software requirements, “nếu user là admin thì có quyền X” không nói rằng chỉ admin mới có quyền X. Suy ngược thành “có quyền X ⇒ admin” là đổi implication thành converse mà không có cơ sở.

## 4. Converse, inverse, contrapositive

Từ

```math
p\Rightarrow q
```

converse là

```math
q\Rightarrow p,
```

inverse là

```math
\neg p\Rightarrow\neg q,
```

và contrapositive là

```math
\neg q\Rightarrow\neg p.
```

Original implication luôn equivalent với contrapositive:

```math
p\Rightarrow q
\iff
\neg q\Rightarrow\neg p.
```

Đây không phải mẹo proof. Nó đến từ việc hai statements loại trừ cùng một bad case: `p` đúng nhưng `q` sai.

Ví dụ:

> Nếu `n` chia hết cho 4 thì `n` chẵn.

Contrapositive:

> Nếu `n` không chẵn thì `n` không chia hết cho 4.

Converse:

> Nếu `n` chẵn thì `n` chia hết cho 4.

sai vì `6` là counterexample.

## 5. Necessary và sufficient conditions

Nếu

```math
p\Rightarrow q,
```

thì `p` là sufficient condition cho `q`, còn `q` là necessary condition cho `p`.

“Chia hết cho 4” đủ để kết luận chẵn. “Chẵn” là điều cần nếu muốn chia hết cho 4.

Nếu cả hai chiều đều đúng:

```math
p\Leftrightarrow q,
```

ta có điều kiện cần và đủ (necessary and sufficient condition / 필요충분조건).

Một proof của `p↔q` thường cần hai proof riêng:

```text
p → q
q → p
```

Đây là pattern thường xuyên trong set equality, invertibility, characterization theorems và equivalence of algorithm conditions.

## 6. Quantifiers: nơi rất nhiều proof sai

Lượng từ phổ quát (universal quantifier / 전칭 기호)

```math
\forall x\,P(x)
```

nghĩa “với mọi `x`, `P(x)` đúng”.

Lượng từ tồn tại (existential quantifier / 존재 기호)

```math
\exists x\,P(x)
```

nghĩa “tồn tại ít nhất một `x` sao cho `P(x)` đúng”.

Negation đổi quantifier:

```math
\neg(\forall x\,P(x))
\equiv
\exists x\,\neg P(x)
```

và

```math
\neg(\exists x\,P(x))
\equiv
\forall x\,\neg P(x).
```

Vì vậy một universal claim có thể bị phá chỉ bằng **một counterexample**.

Ngược lại, để chứng minh existential claim, chỉ cần xây được một witness hợp lệ.

Thứ tự quantifier cũng quan trọng. Hai statements

```math
\forall x\,\exists y\,P(x,y)
```

và

```math
\exists y\,\forall x\,P(x,y)
```

thường rất khác nhau. Statement đầu cho phép chọn `y` khác nhau cho từng `x`; statement sau đòi một `y` duy nhất hoạt động cho mọi `x`.

Đây là source của nhiều nhầm lẫn trong analysis, algorithms và optimization guarantees.

## 7. De Morgan: logic của complement

De Morgan cho propositions:

```math
\neg(p\land q)
\equiv
\neg p\lor\neg q
```

```math
\neg(p\lor q)
\equiv
\neg p\land\neg q.
```

Cùng structure xuất hiện trong set theory:

```math
(A\cap B)^c=A^c\cup B^c
```

```math
(A\cup B)^c=A^c\cap B^c.
```

Và trong code:

```text
!(isAdmin && isActive)
```

logic-equivalent với

```text
!isAdmin || !isActive
```

nhưng runtime behavior có thể khác nếu expressions có side effects hoặc short-circuit semantics phức tạp. Đây là ví dụ cho distinction giữa **logical equivalence** và **operational equivalence**.

## 8. Proof không phải một format duy nhất

Proof là chuỗi reasoning biến assumptions thành conclusion bằng các bước hợp lệ. Method được chọn theo structure của claim.

### Direct proof

Muốn chứng minh tổng hai số chẵn là chẵn, dùng definition:

```math
a=2m,\qquad b=2n.
```

Khi đó

```math
a+b=2(m+n),
```

mà `m+n` là integer, nên `a+b` chẵn.

Proof mạnh vì nó expose structure “even = 2×integer”, không vì nó dài.

### Proof by contrapositive

Muốn chứng minh `p→q`, đôi khi `¬q→¬p` dễ hơn.

Ví dụ: nếu `n^2` chẵn thì `n` chẵn. Contrapositive là: nếu `n` lẻ thì `n^2` lẻ.

Viết `n=2k+1`:

```math
n^2=(2k+1)^2=4k^2+4k+1=2(2k^2+2k)+1,
```

nên lẻ.

### Proof by contradiction

Giả sử phủ định của conclusion rồi derive impossibility.

Proof `\sqrt2` irrational là example kinh điển. Nếu

```math
\sqrt2=\frac ab
```

ở lowest terms, thì từ

```math
a^2=2b^2
```

suy ra cả `a` và `b` chẵn, mâu thuẫn với lowest terms.

Contradiction proof đặc biệt hữu ích khi statement nói một object **không thể tồn tại**.

### Proof by cases

Khi domain tự nhiên chia thành finite cases, proof từng case có thể hợp lý. Ví dụ integer hoặc chẵn hoặc lẻ.

Điểm quan trọng là cases phải **exhaustive** và ideally disjoint để không bỏ sót trạng thái.

### Existence proof

Có hai kiểu chính.

Constructive proof đưa ra object cụ thể.

Non-constructive proof chứng minh object phải tồn tại mà không nhất thiết cho algorithm để tìm nó.

Mathematics chấp nhận cả hai; computer science thường quan tâm thêm câu hỏi computational: “tồn tại” có đi kèm cách tìm hiệu quả không?

## 9. Mathematical induction: proof trên recursive structure

Quy nạp toán học (mathematical induction / 수학적 귀납법) có hai phần:

1. base case;
2. inductive step `P(k)→P(k+1)`.

Ví dụ:

```math
1+2+\cdots+n=\frac{n(n+1)}2.
```

Base case `n=1` đúng.

Giả sử

```math
1+\cdots+k=\frac{k(k+1)}2.
```

Khi đó

```math
1+\cdots+k+(k+1)
=
\frac{k(k+1)}2+(k+1)
=
\frac{(k+1)(k+2)}2.
```

Induction không nói “statement đúng cho `k` vì ta muốn thế”. Inductive hypothesis là assumption **cục bộ trong bước chứng minh implication**.

Strong induction cho phép giả sử statement đúng cho mọi values nhỏ hơn `n`, rất tự nhiên trong divide-and-conquer và recurrence proofs.

Structural induction áp cùng idea cho trees, syntax trees, recursive data structures và formal languages.

## 10. Invariants: proof bằng điều không đổi

Invariant là property được giữ qua mỗi transformation hoặc iteration.

Trong loop proof, ta thường có:

```text
initialization
→ maintenance
→ termination
```

Đây chính là induction trên số iteration.

Trong algorithms, chọn đúng invariant thường khó hơn algebra sau đó. Ví dụ binary search giữ invariant rằng nếu target tồn tại thì nó vẫn nằm trong current interval.

Trong physics, conservation laws đóng vai trò tương tự ở level model: một quantity không đổi dưới dynamics nhất định.

## 11. Counterexample: công cụ mạnh nhất để phá universal claim

Nếu claim là

```math
\forall x\,P(x),
```

chỉ cần một `x` sao cho `P(x)` sai.

Ví dụ claim “mọi prime đều lẻ” bị phá bởi `2`.

Counterexample không chỉ dùng để bác bỏ. Khi tìm counterexample, ta thường học được assumption nào còn thiếu để theorem trở thành đúng.

Đây là workflow rất mạnh:

```text
conjecture
→ search edge cases
→ counterexample
→ identify missing assumption
→ refine theorem
```

Nó giống debugging specification trong software.

## 12. Proof idea và formal proof

Một proof tốt thường có hai layers.

**Proof idea** giải thích mechanism chính: invariant nào, contradiction nào, decomposition nào, induction measure nào.

**Formal proof** đảm bảo không có logical gap.

Nếu chỉ có formal symbols mà không có proof idea, người học khó transfer reasoning. Nếu chỉ có intuition mà không kiểm tra details, edge case có thể bị bỏ sót.

Tài liệu này ưu tiên intuition trước, nhưng formalism xuất hiện sau đó để khóa reasoning lại.

## 13. Proof, testing và formal verification

Testing kiểm tra finite examples. Một test suite tốt có thể tăng confidence rất nhiều nhưng không chứng minh universal property trên infinite input domain.

Proof có thể chứng minh property của một model hoặc algorithm, nhưng không bảo đảm implementation thực tế đúng nếu model/specification không match code.

Formal verification cố đưa specification, program semantics và proof vào một system machine-checkable. Tuy nhiên verification vẫn phụ thuộc vào correctness của specification và abstraction boundary.

## 14. Connection với Probability và Statistics

Logic xử lý truth dưới assumptions; probability mở rộng sang uncertainty về events. Event operations dùng cùng AND/OR/NOT structure:

```math
P(A\cap B),\qquad P(A\cup B),\qquad P(A^c).
```

Bayes reasoning cũng phụ thuộc vào việc condition/event được định nghĩa chính xác. Nếu events mơ hồ, công thức đúng vẫn cho answer không meaningful.

## Mental Model

> Logic quản lý **đường đi hợp lệ từ assumptions đến conclusions**. Proof là một chương trình reasoning: definition tạo objects, inference rules là operations, invariant/contradiction/induction là control structures, và theorem là output. Một proof tốt không chỉ đúng; nó làm lộ mechanism khiến statement buộc phải đúng.

## Common Misconceptions

`p→q` không cho phép suy `q→p`. Không tìm được proof của `p` không đồng nghĩa `¬p`. Nhiều examples phù hợp không thay proof cho universal claim, nhưng một counterexample hợp lệ đủ để phá claim đó. Inductive hypothesis không phải circular reasoning; nó là assumption trong proof của implication `P(k)→P(k+1)`. Formal proof không tự đảm bảo model ban đầu mô tả đúng reality.