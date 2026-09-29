# Ngôn ngữ đại số: biểu diễn cấu trúc bằng ký hiệu

> **Mạch đọc:** Đọc **Ngôn ngữ đại số: biểu diễn cấu trúc bằng ký hiệu** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Variable có nhiều vai trò** sang **2. lĩnh vực (domain / 도메인) là part of algebra, không phải footnote**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đại số (algebra / 대수학) bắt đầu khi ta ngừng giải từng bài toán bằng số cụ thể và chuyển sang lập luận (reasoning / 추론) trên **cấu trúc (structure / 구조)**. Ký hiệu cho phép ta giữ một quantity chưa biết, một parameter có thể thay đổi, hoặc một mẫu (pattern / 패턴) áp dụng cho cả family problems.

Ví dụ thay vì xử lý riêng “3 hộp, mỗi hộp 5 món”, “3 hộp, mỗi hộp 8 món”, ta viết

```math
3x.
```

Ký hiệu `x` không làm bài toán trừu tượng vô ích; nó loại chi tiết không cần thiết để giữ relationship cần lập luận (reasoning / 추론).

## 1. Variable có nhiều vai trò

Biến (variable / 변수) không đồng nghĩa “ẩn số”.

Trong

```math
x+3=10,
```

`x` là unknown cần solve.

Trong

```math
y=2x+1,
```

`x` là đầu vào (input / 입력) và `y` phụ thuộc vào `x`.

Trong

```math
f(x;\theta),
```

`x` có thể là đầu vào (input / 입력) còn `\theta` là parameter xác định member trong hàm (function / 함수) family.

Trong xác suất (probability / 확률), `X` có thể là random variable. Trong programming, variable là một binding/tham chiếu (reference / 참조) trong mô hình thực thi (execution model / 실행 모델).

Các usages liên quan qua idea “symbol đại diện quantity”, nhưng ngữ nghĩa (semantics / 의미론) khác nhau. Vì vậy ngữ cảnh (context / 맥락) và lĩnh vực (domain / 도메인) phải được nói rõ.

## 2. lĩnh vực (domain / 도메인) là part of algebra, không phải footnote

Một symbol chỉ meaningful cùng universe values nó được phép nhận.

Nếu `x` là số người:

```math
x\in\mathbb Z_{\ge0}
```

có thể hợp lý.

Nếu `x` là continuous thời gian (time / 시간):

```math
x\in\mathbb R_{\ge0}.
```

Equation

```math
x^2=2
```

không có rational solution nhưng có real solutions.

Equation

```math
x^2=-1
```

không có real solution nhưng có complex solutions.

Do đó solution set không tồn tại độc lập với lĩnh vực (domain / 도메인).

## 3. Expression, equation, định danh (identity / 식별자) và hàm (function / 함수) khác nhau

Biểu thức (expression / 식)

```math
3x+2
```

là đối tượng (object / 객체) tạo giá trị (value / 값) khi `x` được gán.

Equation

```math
3x+2=14
```

là ràng buộc (constraint / 제약조건); nó đúng chỉ cho một số values.

Định danh (identity / 식별자)

```math
(a+b)^2=a^2+2ab+b^2
```

là equality đúng cho mọi values trong lĩnh vực (domain / 도메인) thích hợp.

Hàm (function / 함수)

```math
f(x)=3x+2
```

là ánh xạ (mapping / 매핑), không chỉ expression bên phải.

Phân biệt này quan trọng vì cách lập luận (reasoning / 추론) khác nhau: expression được simplify/evaluate, equation được solve, định danh (identity / 식별자) được prove, hàm (function / 함수) được analyze như ánh xạ (mapping / 매핑).

## 4. Dấu bằng là statement về sameness

Dấu `=` không nghĩa “bây giờ tính kết quả”. Nó khẳng định hai expressions represent cùng giá trị (value / 값)/đối tượng (object / 객체) trong ngữ cảnh (context / 맥락).

Từ

```math
x+5=12,
```

trừ 5 hai vế:

```math
x+5-5=12-5
```

cho

```math
x=7.
```

Cơ chế sâu hơn “cân hai vế” là: ta apply cùng reversible transformation

```math
T(t)=t-5
```

lên cả hai sides.

Khi transformation one-to-one trên lĩnh vực (domain / 도메인) đang xét, equality quan hệ (relation / 관계) được preserve theo hai chiều.

## 5. Equivalence transformation vs implication-only transformation

Không phải algebraic manipulation nào cũng reversible.

Ví dụ

```math
x=2
```

implies

```math
x^2=4,
```

nhưng reverse không đúng vì `x=-2` cũng thỏa squared equation.

Vì vậy squaring có thể **mở rộng** solution set.

Chia hai vế cho expression có thể **thu hẹp** solution set nếu expression có thể bằng zero.

Ví dụ:

```math
x^2=x.
```

Chia cho `x` cho `x=1`, nhưng làm mất gốc (root / 루트) `x=0`.

Cách structure-preserving hơn:

```math
x^2-x=0
```

```math
x(x-1)=0,
```

nên

```math
x=0\quad\text{hoặc}\quad x=1.
```

Khi manipulate equation, câu hỏi cần hỏi là:

> Bước này bảo toàn equivalence hay chỉ tạo implication một chiều?

## 6. Arithmetic laws là rules của cấu trúc (structure / 구조)

Các law nền:

Commutative:

```math
a+b=b+a,
\qquad
ab=ba.
```

Associative:

```math
(a+b)+c=a+(b+c),
```

```math
(ab)c=a(bc).
```

Distributive:

```math
a(b+c)=ab+ac.
```

Định danh (identity / 식별자):

```math
a+0=a,
\qquad
a\cdot1=a.
```

Inverse:

```math
a+(-a)=0,
```

và với `a\ne0`:

```math
a\cdot a^{-1}=1.
```

Những laws này giải thích tại sao symbolic transformations hợp lệ. Abstract algebra sau này chỉ formalize structures có một subset các laws như vậy.

## 7. Distributive law: cầu nối (bridge / 브리지) giữa multiplication và addition

Distributive law giải thích vì sao có thể mở ngoặc và phân phối một phép nhân qua phép cộng. Đây không chỉ là mẹo biến đổi; nó bảo toàn cùng một quantity khi đổi cách biểu diễn.

```math
a(b+c)=ab+ac.
```

Hình học: rectangle height `a`, width `b+c` có area bằng tổng area hai rectangles widths `b,c`.

Algebraically, law cho phép chuyển giữa two representations:

```text
factored form ↔ expanded form
```

Hai forms bằng nhau nhưng expose different cấu trúc (structure / 구조).

Expanded form tốt cho collecting coefficients. Factored form làm zeros/dùng chung (common / 공통) factors rõ hơn.

Đại số thường là **chọn biểu diễn (representation / 표현) phù hợp với câu hỏi**, không phải luôn “rút gọn nhất”.

## 8. Factorization là reverse kỹ thuật (engineering / 엔지니어링) cấu trúc (structure / 구조)

Từ

```math
ab+ac
```

nhận ra dùng chung (common / 공통) factor `a`:

```math
ab+ac=a(b+c).
```

Với polynomial:

```math
x^2-5x+6=(x-2)(x-3).
```

Factored form expose roots ngay.

Cùng đối tượng (object / 객체) có thể có nhiều useful forms:

```text
expanded
factored
vertex form
matrix form
log form
```

Transformation giữa representations là central skill xuyên suốt Mathematics thư viện (library / 라이브러리).

## 9. Exponent laws không phải bảng cần thuộc riêng

Với integer positive exponents:

```math
a^m a^n=a^{m+n}
```

vì ta concatenate `m` factors với `n` factors.

Division:

```math
\frac{a^m}{a^n}=a^{m-n}
```

khi `a\ne0`.

Muốn law nhất quán khi `m=n`:

```math
\frac{a^m}{a^m}=1=a^0,
```

nên

```math
a^0=1.
```

Muốn law tiếp tục đúng với negative exponents:

```math
a^{-n}=\frac1{a^n}.
```

Fractional exponents kết nối exponentiation với roots:

```math
a^{1/n}=\sqrt[n]{a}
```

trong lĩnh vực (domain / 도메인) thích hợp.

Một quy tắc (rule / 규칙) tốt nên được nhìn như **extension chosen to preserve structural consistency**.

## 10. Units là một dạng algebra

Nếu

```math
v=\frac dt,
```

với distance meter và thời gian (time / 시간) second, đơn vị (unit / 단위):

```text
m/s
```

behaves algebraically.

Nếu

```math
a=\frac{v}{t},
```

Đơn vị (unit / 단위):

```text
m/s².
```

Dimensional phân tích (analysis / 분석) có thể detect impossible formulas trước khi numeric calculation bắt đầu.

Ví dụ cộng

```text
3 meters + 5 seconds
```

không có vật lý (physical / 물리적) meaning trong ordinary mô hình (model / 모델) dù numbers `3+5` tính được.

Đây là reminder rằng symbolic algebra phải respect ngữ nghĩa (semantic / 의미적) kiểu (type / 타입) của quantities.

## 11. Algebraic rearrangement là solving for perspective

Formula

```math
v=\frac dt
```

có thể rearrange:

```math
d=vt,
```

hoặc

```math
t=\frac dv
```

với `v\ne0`.

Ta không tạo laws mới; ta thay perspective xem quantity nào là unknown.

Trong kỹ thuật (engineering / 엔지니어링), finance và software sức chứa (capacity / 용량) planning, cùng một mô hình (model / 모델) được rearrange tùy quantity cần estimate.

## 12. Parameters, constants và variables

Trong

```math
y=ax+b,
```

`x` là independent variable, `y` dependent variable, `a,b` là parameters xác định line.

Nếu đang fit regression, `a,b` là unknown parameters cần estimate từ dữ liệu (data / 데이터).

Nếu đã deploy mô hình (model / 모델), chúng có thể được coi constants trong prediction.

Vai trò symbol phụ thuộc phase của bài toán (problem / 문제).

## 13. Algebra và hàm (function / 함수) composition

Expression nesting như

```math
\sqrt{3x+1}
```

có thể decompose thành functions:

```text
x
→ 3x+1
→ sqrt(.)
```

Đây là composition viewpoint.

Khi solve equation hoặc differentiate, nhìn expression cây (tree / 트리) giúp biết thao tác (operation / 연산) thứ tự (order / 순서) và inverse/chuỗi (chain / 사슬) rules phải apply theo chiều nào.

Trình biên dịch (compiler / 컴파일러) cũng parse mã nguồn (source code / 소스 코드) thành abstract cú pháp (syntax / 문법) cây (tree / 트리). Symbolic algebra hệ thống (system / 시스템) làm transformations trên trees theo rules có điều kiện.

## 14. Algebra và computational graphs

Neural mạng (network / 네트워크), spreadsheet formula, differentiable program đều có thể nhìn như computational đồ thị (graph / 그래프).

Ví dụ:

```math
z=(ax+b)^2
```

có đồ thị (graph / 그래프):

```text
x → multiply a → add b → square → z
```

Forward evaluation truyền values; reverse-mode AD truyền sensitivities ngược đồ thị (graph / 그래프).

Algebraic cấu trúc (structure / 구조) vì vậy nối trực tiếp tới automatic differentiation.

## 15. Modeling: ký hiệu chỉ hữu ích nếu ngữ nghĩa (semantics / 의미론) rõ

Giả sử total độ trễ (latency / 지연 시간):

```math
T=T_{network}+T_{server}+T_{db}.
```

Rearrange:

```math
T_{db}=T-T_{network}-T_{server}.
```

Algebra đúng. Nhưng mô hình (model / 모델) có thể sai nếu components overlap, execute concurrently, hoặc đo lường (measurement / 측정) definitions khác nhau.

Mathematics không tự đảm bảo decomposition phản ánh hệ thống (system / 시스템) thực.

Luôn tách:

```text
model assumptions
→ algebraic consequences
→ measurements / implementation
```

## 16. Symbolic simplification có thể gây numerical problems

Hai expressions mathematically equal có thể có numerical hành vi (behavior / 동작) khác nhau.

Ví dụ near `x=0`, expression

```math
\frac{1-\cos x}{x^2}
```

có thể chịu cancellation trong floating điểm (point / 지점).

Equivalent identities/series có thể evaluate ổn định hơn.

Vì vậy “algebraically simpler” không luôn “numerically better”. Numerical Methods sẽ formalize issue này bằng conditioning/stability.

## 17. dùng chung (common / 공통) mẫu (pattern / 패턴): preserve bất biến (invariant / 불변식) while changing biểu diễn (representation / 표현)

Đại số, row reduction, coordinate changes, Fourier transform, logarithm và xác suất (probability / 확률) reparameterization đều share mẫu (pattern / 패턴):

```text
same underlying object/problem
→ different representation
→ desired structure becomes easier to see
```

Đây là một trong những mô hình tư duy (mental models / 사고 모델들) quan trọng nhất của toàn Mathematics thư viện (library / 라이브러리).

## Worked Example: solve nhưng nhánh học (track / 트랙) lĩnh vực (domain / 도메인)

Giải

```math
\frac{x+1}{x-2}=3.
```

Trước hết lĩnh vực (domain / 도메인):

```math
x\ne2.
```

Nhân hai vế với `x-2` hợp lệ trên lĩnh vực (domain / 도메인) này:

```math
x+1=3(x-2).
```

Expand:

```math
x+1=3x-6.
```

Rearrange:

```math
7=2x
```

nên

```math
x=\frac72.
```

Candidate thỏa lĩnh vực (domain / 도메인), nên valid.

Việc ghi lĩnh vực (domain / 도메인) trước làm lập luận (reasoning / 추론) transparent hơn việc “cross multiply” như một ritual.

## Mô hình tư duy (mental model / 사고 모델)

> Algebra là **ngôn ngữ của representation-preserving transformations**. Variables giữ quantities chưa cố định; laws mô tả operations nào preserve cấu trúc (structure / 구조); factorization, expansion, rearrangement và substitution đổi cách nhìn để mẫu (pattern / 패턴) cần tìm lộ ra. Algebra mạnh nhất khi ta theo dõi lĩnh vực (domain / 도메인), reversibility và ngữ nghĩa (semantics / 의미론) thay vì chỉ thao tác symbols.

## Dùng chung (common / 공통) Misconceptions

Variable không luôn là unknown. `=` không phải nút “tính kết quả”. “Chuyển vế đổi dấu” chỉ là shorthand cho reversible operations. Chia/bình phương/lấy căn hai vế có thể thay solution set. Hai expressions mathematically equivalent không nhất thiết có cùng numerical stability. Simplification chỉ có nghĩa khi domain và semantic units vẫn được tôn trọng.
