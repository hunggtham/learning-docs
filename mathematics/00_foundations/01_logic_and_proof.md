# Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Mệnh đề: đơn vị cơ bản của lập luận (reasoning / 추론)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. AND, OR, XOR và cách conditions tạo cấu trúc** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối mệnh đề với suy luận và chứng minh, để xác định giả thiết nào thực sự nâng đỡ kết luận.

Lô-gic (logic / 논리) không nói một tiền đề có đúng ngoài đời hay không. Nó trả lời câu hỏi khác: **nếu chấp nhận các tiền đề hiện có, kết luận nào thực sự theo sau?** Đây là lý do lô-gic (logic / 논리) đứng trước proof, discrete mathematics, algorithms, xác suất (probability / 확률), cơ sở dữ liệu (database / 데이터베이스) predicates và formal xác minh (verification / 확인).

Một cách nhìn hữu ích là tách ba tầng:

```text
mô hình / giả định
→ quy tắc suy luận
→ kết luận
```

Nếu giả định (assumption / 가정) sai, lập luận (reasoning / 추론) hoàn hảo vẫn có thể cho conclusion vô ích. Nếu giả định (assumption / 가정) đúng nhưng suy luận (inference / 추론) sai, conclusion không được bảo đảm. Vì vậy mathematical rigor không thay thế modeling judgment; hai việc giải quyết hai loại lỗi khác nhau.

## 1. Mệnh đề: đơn vị cơ bản của lập luận (reasoning / 추론)

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

không phải chỉ `x<5`, vì phủ định phải bao phủ **mọi trường hợp (case / 사례) không thuộc statement gốc**.

Đây là một mẫu (pattern / 패턴) quan trọng: khi negate một claim, ta không đoán câu “nghe đối lập”; ta lấy complement lô-gic (logic / 논리) của toàn bộ điều kiện (condition / 조건).

> **Nối mạch:** Trong **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **2. AND, OR, XOR và cách conditions tạo cấu trúc** nối từ **1. Mệnh đề: đơn vị cơ bản của lập luận (reasoning / 추론)** sang **3. Implication: statement về việc counterexample không được phép tồn tại**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Điểm đáng học không phải bảng truth bảng (table / 테이블) riêng lẻ mà là việc **compound điều kiện (condition / 조건) có thể được xem như một đối tượng (object / 객체) toán học**. Điều này nối trực tiếp sang Boolean algebra, circuit thiết kế (design / 설계), SQL predicates và program guards.

> **Nối mạch:** Ở chặng này của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **2. AND, OR, XOR và cách conditions tạo cấu trúc** nêu quy tắc; **3. Implication: statement về việc counterexample không được phép tồn tại** thử quy tắc trong tình huống, rồi **4. Converse, inverse, contrapositive** mở rộng hệ quả.

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

Trong software requirements, “nếu người dùng (user / 사용자) là admin thì có quyền X” không nói rằng chỉ admin mới có quyền X. Suy ngược thành “có quyền X ⇒ admin” là đổi implication thành converse mà không có cơ sở.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **3. Implication: statement về việc counterexample không được phép tồn tại** nêu quy tắc; **4. Converse, inverse, contrapositive** thử quy tắc trong tình huống, rồi **5. Necessary và sufficient conditions** mở rộng hệ quả.

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

Đây không phải mẹo proof. Nó đến từ việc hai statements loại trừ cùng một bad trường hợp (case / 사례): `p` đúng nhưng `q` sai.

Ví dụ:

> Nếu `n` chia hết cho 4 thì `n` chẵn.

Contrapositive:

> Nếu `n` không chẵn thì `n` không chia hết cho 4.

Converse:

> Nếu `n` chẵn thì `n` chia hết cho 4.

sai vì `6` là counterexample.

> **Nối mạch:** Trong **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **5. Necessary và sufficient conditions** nối từ **4. Converse, inverse, contrapositive** sang **6. Quantifiers: nơi rất nhiều proof sai**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Necessary và sufficient conditions

Nếu

```math
p\Rightarrow q,
```

thì `p` là sufficient điều kiện (condition / 조건) cho `q`, còn `q` là necessary điều kiện (condition / 조건) cho `p`.

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

Đây là mẫu (pattern / 패턴) thường xuyên trong set equality, invertibility, characterization theorems và equivalence of thuật toán (algorithm / 알고리즘) conditions.

> **Nối mạch:** Ở chặng này của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **6. Quantifiers: nơi rất nhiều proof sai** nối từ **5. Necessary và sufficient conditions** sang **7. De Morgan: lô-gic (logic / 논리) của complement**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Đây là nguồn (source / 소스) của nhiều nhầm lẫn trong phân tích (analysis / 분석), algorithms và tối ưu hóa (optimization / 최적화) guarantees.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **7. De Morgan: lô-gic (logic / 논리) của complement** nối từ **6. Quantifiers: nơi rất nhiều proof sai** sang **8. Proof không phải một format duy nhất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. De Morgan: lô-gic (logic / 논리) của complement

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

Cùng cấu trúc (structure / 구조) xuất hiện trong set lý thuyết (theory / 이론):

```math
(A\cap B)^c=A^c\cup B^c
```

```math
(A\cup B)^c=A^c\cap B^c.
```

Và trong mã (code / 코드):

```text
!(isAdmin && isActive)
```

logic-equivalent với

```text
!isAdmin || !isActive
```

nhưng hành vi thời gian chạy (runtime behavior / 런타임 동작) có thể khác nếu expressions có side effects hoặc short-circuit ngữ nghĩa (semantics / 의미론) phức tạp. Đây là ví dụ cho distinction giữa **logical equivalence** và **operational equivalence**.

> **Nối mạch:** Trong **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **8. Proof không phải một format duy nhất** nối từ **7. De Morgan: lô-gic (logic / 논리) của complement** sang **9. Mathematical induction: proof trên recursive cấu trúc (structure / 구조)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Proof không phải một format duy nhất

Proof là chuỗi lập luận (reasoning / 추론) biến các giả định (assumptions / 가정들) thành conclusion bằng các bước hợp lệ. phương thức (method / 메서드) được chọn theo cấu trúc (structure / 구조) của claim.

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

Proof mạnh vì nó expose cấu trúc (structure / 구조) “even = 2×integer”, không vì nó dài.

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

Contradiction proof đặc biệt hữu ích khi statement nói một đối tượng (object / 객체) **không thể tồn tại**.

### Proof by cases

Khi lĩnh vực (domain / 도메인) tự nhiên chia thành finite cases, proof từng trường hợp (case / 사례) có thể hợp lý. Ví dụ integer hoặc chẵn hoặc lẻ.

Điểm quan trọng là cases phải **exhaustive** và ideally disjoint để không bỏ sót trạng thái.

### Existence proof

Có hai kiểu chính.

Constructive proof đưa ra đối tượng (object / 객체) cụ thể.

Non-constructive proof chứng minh đối tượng (object / 객체) phải tồn tại mà không nhất thiết cho thuật toán (algorithm / 알고리즘) để tìm nó.

Mathematics chấp nhận cả hai; khoa học máy tính (computer science / 컴퓨터 과학) thường quan tâm thêm câu hỏi computational: “tồn tại” có đi kèm cách tìm hiệu quả không?

> **Nối mạch:** Ở chặng này của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **9. Mathematical induction: proof trên recursive cấu trúc (structure / 구조)** nối từ **8. Proof không phải một format duy nhất** sang **10. Invariants: proof bằng điều không đổi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Mathematical induction: proof trên recursive cấu trúc (structure / 구조)

Quy nạp toán học (mathematical induction / 수학적 귀납법) có hai phần:

1. cơ sở (base / 기반) trường hợp (case / 사례);
2. inductive step `P(k)→P(k+1)`.

Ví dụ:

```math
1+2+\cdots+n=\frac{n(n+1)}2.
```

Cơ sở (base / 기반) trường hợp (case / 사례) `n=1` đúng.

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

Induction không nói “statement đúng cho `k` vì ta muốn thế”. Inductive hypothesis là giả định (assumption / 가정) **cục bộ trong bước chứng minh implication**.

Strong induction cho phép giả sử statement đúng cho mọi values nhỏ hơn `n`, rất tự nhiên trong divide-and-conquer và recurrence proofs.

Structural induction áp cùng idea cho trees, cú pháp (syntax / 문법) trees, recursive dữ liệu (data / 데이터) structures và formal languages.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **10. Invariants: proof bằng điều không đổi** nối từ **9. Mathematical induction: proof trên recursive cấu trúc (structure / 구조)** sang **11. Counterexample: công cụ mạnh nhất để phá universal claim**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Invariants: proof bằng điều không đổi

Bất biến (invariant / 불변식) là thuộc tính (property / 속성) được giữ qua mỗi transformation hoặc iteration.

Trong vòng lặp (loop / 루프) proof, ta thường có:

```text
initialization
→ maintenance
→ termination
```

Đây chính là induction trên số iteration.

Trong algorithms, chọn đúng bất biến (invariant / 불변식) thường khó hơn algebra sau đó. Ví dụ tìm kiếm nhị phân (binary search / 이진 탐색) giữ bất biến (invariant / 불변식) rằng nếu mục tiêu (target / 대상) tồn tại thì nó vẫn nằm trong hiện tại (current / 현재) interval.

Trong physics, conservation laws đóng vai trò tương tự ở mức (level / 수준) mô hình (model / 모델): một quantity không đổi dưới dynamics nhất định.

> **Nối mạch:** Trong **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **10. Invariants: proof bằng điều không đổi** nêu quy tắc; **11. Counterexample: công cụ mạnh nhất để phá universal claim** thử quy tắc trong tình huống, rồi **12. Proof idea và formal proof** mở rộng hệ quả.

## 11. Counterexample: công cụ mạnh nhất để phá universal claim

Nếu claim là

```math
\forall x\,P(x),
```

chỉ cần một `x` sao cho `P(x)` sai.

Ví dụ claim “mọi prime đều lẻ” bị phá bởi `2`.

Counterexample không chỉ dùng để bác bỏ. Khi tìm counterexample, ta thường học được giả định (assumption / 가정) nào còn thiếu để theorem trở thành đúng.

Đây là workflow rất mạnh:

```text
conjecture
→ search edge cases
→ counterexample
→ identify missing assumption
→ refine theorem
```

Nó giống debugging specification trong software.

> **Nối mạch:** Ở chặng này của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **11. Counterexample: công cụ mạnh nhất để phá universal claim** nêu quy tắc; **12. Proof idea và formal proof** thử quy tắc trong tình huống, rồi **13. Proof, testing và formal xác minh (verification / 확인)** mở rộng hệ quả.

## 12. Proof idea và formal proof

Một proof tốt thường có hai layers.

**Proof idea** giải thích cơ chế (mechanism / 메커니즘) chính: bất biến (invariant / 불변식) nào, contradiction nào, decomposition nào, induction measure nào.

**Formal proof** đảm bảo không có logical gap.

Nếu chỉ có formal symbols mà không có proof idea, người học khó transfer lập luận (reasoning / 추론). Nếu chỉ có intuition mà không kiểm tra details, trường hợp biên (edge case / 경계 사례) có thể bị bỏ sót.

Tài liệu này ưu tiên intuition trước, nhưng formalism xuất hiện sau đó để khóa lập luận (reasoning / 추론) lại.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **13. Proof, testing và formal xác minh (verification / 확인)** nối từ **12. Proof idea và formal proof** sang **14. liên kết (connection / 연결) với xác suất (probability / 확률) và Statistics**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Proof, testing và formal xác minh (verification / 확인)

Testing kiểm tra finite examples. Một bộ kiểm thử (test suite / 테스트 스위트) tốt có thể tăng confidence rất nhiều nhưng không chứng minh universal thuộc tính (property / 속성) trên infinite đầu vào (input / 입력) lĩnh vực (domain / 도메인).

Proof có thể chứng minh thuộc tính (property / 속성) của một mô hình (model / 모델) hoặc thuật toán (algorithm / 알고리즘), nhưng không bảo đảm hiện thực (implementation / 구현) thực tế đúng nếu mô hình (model / 모델)/specification không match mã (code / 코드).

Formal xác minh (verification / 확인) cố đưa specification, program ngữ nghĩa (semantics / 의미론) và proof vào một hệ thống (system / 시스템) machine-checkable. Tuy nhiên xác minh (verification / 확인) vẫn phụ thuộc vào tính đúng đắn (correctness / 정확성) của specification và lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계).

> **Nối mạch:** Trong **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **14. liên kết (connection / 연결) với xác suất (probability / 확률) và Statistics** nối từ **13. Proof, testing và formal xác minh (verification / 확인)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. liên kết (connection / 연결) với xác suất (probability / 확률) và Statistics

Lô-gic (logic / 논리) xử lý truth dưới các giả định (assumptions / 가정들); xác suất (probability / 확률) mở rộng sang bất định (uncertainty / 불확실성) về events. sự kiện (event / 이벤트) operations dùng cùng AND/OR/NOT cấu trúc (structure / 구조):

```math
P(A\cap B),\qquad P(A\cup B),\qquad P(A^c).
```

Bayes lập luận (reasoning / 추론) cũng phụ thuộc vào việc điều kiện (condition / 조건)/sự kiện (event / 이벤트) được định nghĩa chính xác. Nếu events mơ hồ, công thức đúng vẫn cho answer không meaningful.

> **Nối mạch:** Ở chặng này của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **14. liên kết (connection / 연결) với xác suất (probability / 확률) và Statistics** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> lô-gic (logic / 논리) quản lý **đường đi hợp lệ từ các giả định (assumptions / 가정들) đến conclusions**. Proof là một chương trình lập luận (reasoning / 추론): definition tạo objects, suy luận (inference / 추론) rules là operations, bất biến (invariant / 불변식)/contradiction/induction là điều khiển (control / 제어) structures, và theorem là đầu ra (output / 출력). Một proof tốt không chỉ đúng; nó làm lộ cơ chế (mechanism / 메커니즘) khiến statement buộc phải đúng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lô-gic (logic / 논리) và chứng minh: ngôn ngữ của suy luận đúng**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

`p→q` không cho phép suy `q→p`. Không tìm được proof của `p` không đồng nghĩa `¬p`. Nhiều examples phù hợp không thay proof cho universal claim, nhưng một counterexample hợp lệ đủ để phá claim đó. Inductive hypothesis không phải circular lập luận (reasoning / 추론); nó là giả định (assumption / 가정) trong proof của implication `P(k)→P(k+1)`. Formal proof không tự đảm bảo mô hình (model / 모델) ban đầu mô tả đúng reality.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
