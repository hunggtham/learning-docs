# Số và các hệ số: mở rộng universe để phép toán có nơi tồn tại

> **Mạch đọc:** Đọc **Số và các hệ số: mở rộng universe để phép toán có nơi tồn tại** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Một number hệ thống (system / 시스템) được chọn theo operations ta cần** sang **2. Natural numbers: arithmetic của counting**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Số (number / 수) không phải một collection ký hiệu rời rạc. Mỗi hệ số xuất hiện vì hệ trước đó không còn đủ để giữ một số thao tác (operation / 연산) hoặc limit quan trọng.

Ta có thể nhìn lịch sử mở rộng như một phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬):

```text
đếm
→ số tự nhiên
→ cần phép trừ
→ số nguyên
→ cần phép chia
→ số hữu tỉ
→ cần giới hạn không bị “rơi ra ngoài”
→ số thực
→ cần nghiệm cho polynomial như x²+1=0
→ số phức
```

Mô hình tư duy (mental model / 사고 모델) này hữu ích hơn học `N ⊂ Z ⊂ Q ⊂ R ⊂ C` như một chuỗi ký hiệu cần nhớ.

## 1. Một number hệ thống (system / 시스템) được chọn theo operations ta cần

Một set số có thể **closed** dưới một thao tác (operation / 연산): thực hiện thao tác (operation / 연산) trên members vẫn cho kết quả (result / 결과) nằm trong set.

Natural numbers closed dưới addition và multiplication:

```math
3+5=8\in\mathbb N
```

```math
3\cdot5=15\in\mathbb N.
```

Nhưng không closed dưới subtraction:

```math
3-5=-2\notin\mathbb N.
```

Điểm này giải thích vì sao negative numbers không phải “phần phụ kỳ lạ”; chúng hoàn tất một thao tác (operation / 연산) mà counting numbers chưa giữ được.

## 2. Natural numbers: arithmetic của counting

Số tự nhiên (natural numbers / 자연수) thường được viết

```math
\mathbb N=\{0,1,2,3,\ldots\}
```

hoặc bắt đầu từ 1 tùy convention.

Natural numbers mô hình (model / 모델) count của discrete objects. Với `n` objects, addition mô tả combining collections, multiplication mô tả repeated groups.

Peano-style viewpoint còn cho thấy arithmetic có thể được xây từ successor thao tác (operation / 연산), nhưng phạm vi (scope / 범위) hiện tại không cần formal axiomatization đầy đủ. Điều quan trọng là hiểu natural numbers mang **discrete thứ tự (order / 순서) + arithmetic cấu trúc (structure / 구조)**.

## 3. Integers: thêm direction quanh zero

Số nguyên (integers / 정수):

```math
\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}.
```

Integers làm subtraction closed:

```math
3-5=-2\in\mathbb Z.
```

Negative number nên được hiểu như direction/opposite trong additive cấu trúc (structure / 구조), không chỉ là “debt number”.

Mỗi integer `a` có additive inverse `-a` sao cho

```math
a+(-a)=0.
```

Đây là cầu nối (bridge / 브리지) đầu tiên tới group-like algebraic thinking: thao tác (operation / 연산) có định danh (identity / 식별자) và inverse.

Integers vẫn không closed dưới division:

```math
1/2\notin\mathbb Z.
```

## 4. Rational numbers: hoàn tất phép chia giữa integers

Số hữu tỉ (rational numbers / 유리수) có dạng

```math
\frac pq,
\qquad p,q\in\mathbb Z,
\qquad q\ne0.
```

Mỗi rational có nhiều representations:

```math
\frac12=\frac24=\frac{50}{100}.
```

Vì vậy rational number về structural sense là **equivalence lớp (class / 클래스) của fractions**, không phải một particular pair numerator/denominator.

Two fractions

```math
\frac ab,\qquad\frac cd
```

represent cùng rational khi

```math
ad=bc
```

với denominators nonzero.

Đây là liên kết (connection / 연결) giữa number các hệ thống (systems / 시스템들) và equivalence relations.

## 5. Decimal expansion và rationality

Finite decimal luôn rational:

```math
0.125=\frac{125}{1000}=\frac18.
```

Repeating decimal cũng rational. Với

```math
x=0.333\ldots,
```

nhân 10:

```math
10x=3.333\ldots
```

trừ:

```math
9x=3
```

nên

```math
x=\frac13.
```

General fact: real number có eventually repeating decimal expansion iff nó rational.

Điều này cho thấy biểu diễn (representation / 표현) bằng digits chứa thông tin (information / 정보) về algebraic nature của number.

## 6. Irrational numbers: rational line có “holes” đối với limits

Số vô tỉ (irrational numbers / 무리수) không thể biểu diễn thành ratio của two integers.

`√2` là classic example. Proof by contradiction cho thấy giả sử

```math
\sqrt2=\frac ab
```

ở lowest terms dẫn tới `a,b` đều chẵn, contradiction.

Irrational không nghĩa “không approximate được”. Rational numbers dense trong reals: có thể approximate `√2`, `π`, `e` tùy ý chính xác.

Vấn đề là approximation không bằng chính xác (exact / 정확한) membership.

## 7. Real numbers và completeness

Số thực (real numbers / 실수) thường được visualized như mọi points trên continuous number line.

Nhưng thuộc tính (property / 속성) quan trọng nhất cho calculus là **completeness**.

Intuition: nếu một tiến trình (process / 프로세스) rational approximations đang hội tụ về một location “đáng lẽ phải có”, real-number hệ thống (system / 시스템) không để location đó bị thiếu.

Một formulation quan trọng là least-upper-bound thuộc tính (property / 속성): mọi nonempty subset của `R` bị chặn trên có supremum trong `R`.

Một formulation khác dùng Cauchy sequences: chuỗi (sequence / 시퀀스) các real numbers mà terms trở nên arbitrarily close với nhau phải converge tới một real number.

Rationals không complete. Có rational Cauchy sequences converge về `√2`, nhưng `√2∉Q`.

Đây là reason Real phân tích (analysis / 분석) dành nhiều thời gian cho completeness: limits, derivatives, integrals dựa vào việc limiting objects không biến mất khỏi number hệ thống (system / 시스템).

## 8. Absolute giá trị (value / 값): từ sign tới chỉ số (metric / 지표)

Giá trị tuyệt đối (absolute value / 절댓값)

```math
|x|
```

đo distance từ `x` tới zero.

Khoảng cách giữa `a,b`:

```math
|a-b|.
```

Triangle inequality:

```math
|a+b|\le|a|+|b|.
```

Không nên nhìn đây chỉ là inequality để biến đổi. Nó nói đường dẫn (path / 경로) trực tiếp không dài hơn đi qua intermediate decomposition.

Mẫu (pattern / 패턴) này mở rộng tới véc-tơ (vector / 벡터) norms:

```math
\|u+v\|\le\|u\|+\|v\|.
```

Vì vậy absolute giá trị (value / 값) là first example của norm/chỉ số (metric / 지표) cấu trúc (structure / 구조).

## 9. thứ tự (order / 순서): cái mà complex numbers sẽ không giữ nguyên theo cùng cách

Real numbers có total thứ tự (order / 순서):

```math
x<y,\quad x=y,\quad x>y
```

với exactly one trường hợp (case / 사례) true.

Thứ tự (order / 순서) tương thích với addition và positive multiplication.

Nhiều inequalities dựa trên cấu trúc (structure / 구조) này.

Complex numbers không có natural total thứ tự (order / 순서) tương thích với trường dữ liệu (field / 필드) operations theo cách reals có. Vì vậy khi mở rộng number hệ thống (system / 시스템), ta gain solutions/rotation cấu trúc (structure / 구조) nhưng không giữ mọi thuộc tính (property / 속성) cũ.

Đây là lesson tổng quát: extension thường giải quyết một limitation nhưng đổi set of structures available.

## 10. Complex numbers: closure cho polynomial equations và rotation

Số phức (complex numbers / 복소수):

```math
z=a+bi,
\qquad i^2=-1.
```

Ban đầu `i` giúp equation

```math
x^2+1=0
```

có solutions `±i`.

Nhưng complex numbers mạnh hơn vai trò “chứa square gốc (root / 루트) của -1”.

Trên complex plane, `a` và `b` là two coordinates. Magnitude:

```math
|z|=\sqrt{a^2+b^2}.
```

Polar form:

```math
z=re^{i\theta}.
```

Euler quan hệ (relation / 관계):

```math
e^{i\theta}=\cos\theta+i\sin\theta.
```

Multiplication của complex numbers cộng angles và nhân magnitudes. Vì vậy multiplication tự encode rotation + scaling.

Đây là reason complex numbers xuất hiện tự nhiên trong Fourier phân tích (analysis / 분석), wave các mô hình (models / 모델들), AC circuits và điều khiển (control / 제어) các hệ thống (systems / 시스템들).

## 11. Fundamental Theorem of Algebra: vì sao C là một natural endpoint cho polynomial roots

Một polynomial nonconstant với complex coefficients có ít nhất một complex gốc (root / 루트). Từ đó polynomial degree `n` factor thành `n` tuyến tính (linear / 선형) factors khi multiplicity được count.

Conceptually, `C` là algebraically closed: polynomial equations không buộc ta tiếp tục mở rộng theo cùng kiểu như `R` phải mở sang `C` cho `x²+1=0`.

Không cần proof theorem này ở chapter foundations; proof cần complex phân tích (analysis / 분석)/algebra sâu hơn. Nhưng theorem giải thích vị trí đặc biệt của complex numbers trong algebra.

## 12. Numeral hệ thống (system / 시스템) không phải number hệ thống (system / 시스템)

Cần phân biệt:

**Number hệ thống (system / 시스템)**: mathematical objects như integers/reals.

**Numeral hệ thống (system / 시스템)**: cách viết cùng quantity bằng digits và cơ sở (base / 기반).

`11₁₀`, `1011₂`, `B₁₆` represent cùng integer.

Biểu diễn (representation / 표현) thay đổi, đối tượng (object / 객체) không đổi.

Đây là cùng mô hình tư duy (mental model / 사고 모델) đã gặp ở coordinate các hệ thống (systems / 시스템들) và basis changes.

## 13. Positional notation

Trong cơ sở (base / 기반) `b`:

```math
(d_nd_{n-1}\ldots d_0)_b
=
\sum_{k=0}^{n}d_kb^k.
```

Fractional digits dùng negative powers:

```math
0.101_2
=
2^{-1}+2^{-3}
=0.625_{10}.
```

Nhị phân (binary / 이진) cơ sở (base / 기반) 2 phù hợp digital biểu diễn (representation / 표현) vì hardware dễ distinguish two stable trạng thái (state / 상태) ranges. Nhưng nhị phân (binary / 이진) không biến quantity thành “loại số khác”.

## 14. Finite biểu diễn (representation / 표현): khi mathematics gặp machine limits

Mathematical integer là unbounded lớp trừu tượng (abstraction / 추상화). Machine integer có fixed or managed biểu diễn (representation / 표현).

Signed 32-bit phạm vi (range / 범위) thường:

```math
-2^{31}\le x\le2^{31}-1.
```

Overflow ngữ nghĩa (semantics / 의미론) phụ thuộc ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임).

Mathematical real có infinite precision lớp trừu tượng (abstraction / 추상화); floating điểm (point / 지점) chỉ represent finite subset.

IEEE-style floating điểm (point / 지점) roughly:

```math
(-1)^s\times m\times2^e.
```

Do finite significand, thao tác (operation / 연산) được rounded.

## 15. Vì sao 0.1 thường không chính xác (exact / 정확한) trong nhị phân (binary / 이진)

Decimal `0.1` tương tự `1/10`.

Một rational có finite base-`b` expansion chỉ khi denominator sau reduction có prime factors nằm trong cơ sở (base / 기반).

Cơ sở (base / 기반) 10 có prime factors 2 và 5, nên `1/10` finite decimal.

Cơ sở (base / 기반) 2 chỉ có factor 2; denominator 10 còn factor 5, nên expansion nhị phân (binary / 이진) repeats.

Vì vậy lỗi (error / 오류) không phải bug của floating điểm (point / 지점); nó là consequence của finite positional biểu diễn (representation / 표현).

## 16. Equality trong numerical computing

Sau floating operations, chính xác (exact / 정확한) comparison có thể thất bại (fail / 실패):

```text
0.1 + 0.2 == 0.3
```

không luôn true trong nhị phân (binary / 이진) floating arithmetic.

Nhưng solution cũng không phải dùng một `epsilon` magic cho mọi quy mô (scale / 규모).

Absolute tolerance thích hợp gần zero; relative tolerance hữu ích ở different magnitudes. Numerical comparison phải match bài toán (problem / 문제) quy mô (scale / 규모) và lỗi (error / 오류) mô hình (model / 모델).

## 17. Density và cardinality: hai notions “có nhiều số” khác nhau

Rationals và reals đều dense: giữa hai numbers khác nhau luôn có number khác.

Nhưng cardinality khác. `Q` countable; `R` uncountable.

Do đó “dense” không đồng nghĩa “có cùng kích thước (size / 크기) theo set lý thuyết (theory / 이론)”.

Đây là một trong những điểm làm infinite sets khác finite intuition.

## 18. Number các hệ thống (systems / 시스템들) và algebraic structures

Integers dưới addition tạo group; rationals/reals/complex numbers với addition/multiplication tạo fields.

Không cần học abstract algebra trước để dùng numbers, nhưng viewpoint này giải thích vì sao rules algebra giống nhau trên `Q`, `R`, `C`: chúng share trường dữ liệu (field / 필드) axioms.

Khi một thao tác (operation / 연산) không valid trong cấu trúc (structure / 구조) — ví dụ division by zero — không có symbolic trick nào cứu được.

## 19. Physics, AI và Finance connections

Physics dùng real numbers cho continuous measurements và complex numbers cho oscillatory trạng thái (state / 상태) representations.

AI dùng floating-point approximations của real-valued tuyến tính (linear / 선형) algebra; precision format (`FP32`, `FP16`, etc.) ảnh hưởng stability và hiệu năng (performance / 성능).

Finance dùng decimals/currency representations nơi nhị phân (binary / 이진) floating điểm (point / 지점) có thể không phù hợp cho chính xác (exact / 정확한) monetary accounting; fixed-point/decimal arithmetic thường phù hợp hơn cho ledger ngữ nghĩa (semantics / 의미론).

Điểm chung là **mathematical number lĩnh vực (domain / 도메인)** và **machine biểu diễn (representation / 표현)** phải được chọn riêng.

## Mô hình tư duy (mental model / 사고 모델)

> Một number hệ thống (system / 시스템) là một universe được mở rộng để giữ những operations hoặc limits ta cần. Natural numbers giữ counting; integers thêm additive inverse; rationals thêm division; reals thêm completeness; complex numbers thêm algebraic closure cho polynomial roots và hình học (geometry / 기하학) của rotation. Còn nhị phân (binary / 이진)/decimal/floating-point chỉ là representations hữu hạn của những objects đó trong một computational mô hình (model / 모델).

## Dùng chung (common / 공통) Misconceptions

Irrational không nghĩa random. Dense không nghĩa uncountable. Complex không phải “fake numbers”; chúng là extension nhất quán với rich hình học (geometry / 기하학). Decimal/nhị phân (binary / 이진) là biểu diễn (representation / 표현), không phải different quantities. Mathematical real numbers không giống floating-point numbers. Dùng tolerance không có nghĩa mọi approximate equality đều hợp lệ; tolerance phải xuất phát từ quy mô (scale / 규모) và lỗi (error / 오류) mô hình (model / 모델).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mathematical thinking](./00_mathematical_thinking.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
