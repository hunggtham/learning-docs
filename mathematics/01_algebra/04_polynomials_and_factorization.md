# Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Polynomial là gì và vì sao nó đặc biệt?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Leading term và large-scale hành vi (behavior / 동작)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối polynomials với roots và factorization, để chuyển bài toán nghiệm thành cấu trúc nhân tử có thể kiểm tra.

Đa thức (polynomial / 다항식) thường được gặp đầu tiên như biểu thức

```math
P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
```

nhưng cách nhìn hữu ích hơn là: polynomial là một lớp (class / 클래스) functions có **algebraic cấu trúc (structure / 구조) rất giàu nhưng vẫn dễ tính toán**. Chúng cộng, nhân, đạo hàm, tích phân và approximate tốt; roots của chúng encode hình học (geometry / 기하학); factorization làm lộ cấu trúc (structure / 구조) ẩn; còn trong numerical methods và computer algebra, biểu diễn (representation / 표현) của polynomial ảnh hưởng trực tiếp tới stability và chi phí (cost / 비용).

## 1. Polynomial là gì và vì sao nó đặc biệt?

Một polynomial một biến có finite sum của nonnegative integer powers:

```math
P(x)=\sum_{k=0}^n a_kx^k.
```

Bậc (degree / 차수) là largest `k` sao cho `a_k\ne0`.

Ví dụ

```math
P(x)=3x^4-2x+1
```

có degree 4.

Polynomial đặc biệt vì nhiều operations giữ ta ở cùng family:

- tổng hai polynomials vẫn là polynomial;
- sản phẩm (product / 제품) vẫn là polynomial;
- derivative vẫn là polynomial;
- antiderivative cũng là polynomial cộng constant.

Closure này làm polynomial trở thành “working ngôn ngữ (language / 언어)” tự nhiên của algebra và calculus.

> **Chuyển mạch:** Trong **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **2. Leading term và large-scale hành vi (behavior / 동작)** tiếp nhận điểm tựa từ **1. Polynomial là gì và vì sao nó đặc biệt?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Roots là nơi polynomial mất đầu ra (output / 출력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Leading term và large-scale hành vi (behavior / 동작)

Với

```math
P(x)=a_nx^n+\cdots+a_0,
```

khi `|x|` rất lớn, term `a_nx^n` thường dominate lower-order terms.

Do đó end hành vi (behavior / 동작) phụ thuộc mạnh vào degree parity và sign của `a_n`.

Nếu `n` chẵn, hai ends đi cùng direction. Nếu `n` lẻ, hai ends đi opposite directions.

Đây là first asymptotic lập luận (reasoning / 추론): không cần biết mọi coefficient để biết large-scale shape.

> **Chuyển mạch:** Ở chặng này của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **3. Roots là nơi polynomial mất đầu ra (output / 출력)** tiếp nhận điểm tựa từ **2. Leading term và large-scale hành vi (behavior / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Zero-product thuộc tính (property / 속성) biến factors thành roots** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Roots là nơi polynomial mất đầu ra (output / 출력)

Gốc (root / 루트)/zero `r` thỏa

```math
P(r)=0.
```

Graphically, đó là nơi đồ thị (graph / 그래프) gặp x-axis. Algebraically, gốc (root / 루트) liên hệ trực tiếp với factor.

Factor theorem:

```math
P(r)=0
\iff
(x-r)\mid P(x).
```

Tại sao?

Polynomial division cho

```math
P(x)=(x-r)Q(x)+R,
```

vì divisor degree 1 nên remainder là constant. Thay `x=r`:

```math
P(r)=R.
```

Vì thế `P(r)=0` khi và chỉ khi remainder bằng 0, tức `(x-r)` là chính xác (exact / 정확한) factor.

Factor theorem không phải mẹo; nó là special trường hợp (case / 사례) của polynomial division.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **4. Zero-product thuộc tính (property / 속성) biến factors thành roots** tiếp nhận điểm tựa từ **3. Roots là nơi polynomial mất đầu ra (output / 출력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Multiplicity nói gì về cục bộ (local / 로컬) hình học (geometry / 기하학)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Zero-product thuộc tính (property / 속성) biến factors thành roots

Nếu

```math
P(x)=(x-2)(x-3),
```

thì solving

```math
P(x)=0
```

trở thành

```math
(x-2)(x-3)=0.
```

Trong real/complex numbers, sản phẩm (product / 제품) bằng zero khi ít nhất một factor bằng zero, nên

```math
x=2\quad\text{hoặc}\quad x=3.
```

Factorization là powerful vì nó đổi một toàn cục (global / 전역) expression thành cục bộ (local / 로컬) conditions trên factors.

> **Chuyển mạch:** Trong **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **5. Multiplicity nói gì về cục bộ (local / 로컬) hình học (geometry / 기하학)?** tiếp nhận điểm tựa từ **4. Zero-product thuộc tính (property / 속성) biến factors thành roots** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Cùng polynomial, nhiều representations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Multiplicity nói gì về cục bộ (local / 로컬) hình học (geometry / 기하학)?

Nếu

```math
P(x)=(x-r)^mQ(x),\qquad Q(r)\ne0,
```

thì `r` có multiplicity `m`.

Nếu `m` odd, sign thường đổi khi đi qua `r`, nên đồ thị (graph / 그래프) cross x-axis.

Nếu `m` even, sign thường giữ nguyên, nên đồ thị (graph / 그래프) touch rồi turn.

Ví dụ:

```math
P(x)=(x-1)^2(x+2).
```

Gốc (root / 루트) `x=1` multiplicity 2, gốc (root / 루트) `x=-2` multiplicity 1.

Calculus giải thích sâu hơn: high multiplicity đồng nghĩa nhiều derivatives đầu tiên cũng vanish tại gốc (root / 루트).

> **Chuyển mạch:** Ở chặng này của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **6. Cùng polynomial, nhiều representations** tiếp nhận điểm tựa từ **5. Multiplicity nói gì về cục bộ (local / 로컬) hình học (geometry / 기하학)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Completing the square là biểu diễn (representation / 표현) thay đổi (change / 변경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Cùng polynomial, nhiều representations

Một trong những bài học quan trọng nhất của algebra là **biểu diễn (representation / 표현) choice matters**.

### Expanded form

Expanded form làm lộ từng hạng tử và phù hợp khi cộng, trừ hoặc so sánh hệ số. Nó là một cách biểu diễn của cùng đa thức, không phải một đa thức khác.

```math
ax^2+bx+c
```

làm coefficients và algebraic combination rõ.

### Factored form

Factored form làm lộ các nhân tử và nghiệm tiềm năng. Dùng nó khi muốn thấy cấu trúc tích hoặc giải phương trình bằng zero-product rule.

```math
a(x-r_1)(x-r_2)
```

làm roots và sign cấu trúc (structure / 구조) rõ.

### Vertex form

Vertex form làm lộ đỉnh và phép tịnh tiến của parabola. Nó nối hệ số đại số với vị trí, hướng mở và cực trị trên đồ thị.

```math
a(x-h)^2+k
```

làm extremum và hình học (geometry / 기하학) rõ.

Cùng một đối tượng (object / 객체) nhưng mỗi form trả lời một loại câu hỏi khác nhau. Đây là mẫu (pattern / 패턴) lặp lại trong tuyến tính (linear / 선형) algebra, Fourier phân tích (analysis / 분석) và numerical computing: đổi basis/biểu diễn (representation / 표현) để làm cấu trúc (structure / 구조) trở nên nhìn thấy được.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **7. Completing the square là biểu diễn (representation / 표현) thay đổi (change / 변경)** tiếp nhận điểm tựa từ **6. Cùng polynomial, nhiều representations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Polynomial division và remainder theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Completing the square là biểu diễn (representation / 표현) thay đổi (change / 변경)

Với quadratic

```math
x^2+6x+5,
```

ta thêm và bớt `9`:

```math
x^2+6x+9-9+5
```

```math
=(x+3)^2-4.
```

Expanded form giúp đọc coefficients; vertex form ngay lập tức cho vertex `(-3,-4)`.

Thao tác (operation / 연산) này cũng là nền của quadratic formula và Gaussian expressions trong xác suất (probability / 확률).

> **Chuyển mạch:** Trong **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **8. Polynomial division và remainder theorem** tiếp nhận điểm tựa từ **7. Completing the square là biểu diễn (representation / 표현) thay đổi (change / 변경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Fundamental Theorem of Algebra: vì sao complex numbers đủ?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Polynomial division và remainder theorem

Giống integer division,

```math
P(x)=D(x)Q(x)+R(x),
```

với

```math
\deg R<\deg D.
```

Khi `D(x)=x-r`, remainder là constant và bằng `P(r)`.

Điều này nối evaluation với divisibility.

Trong computer algebra, polynomial division là thành phần nguyên thủy (primitive / 기본 요소) thao tác (operation / 연산) phía sau gcd algorithms, symbolic simplification và factorization methods.

> **Chuyển mạch:** Ở chặng này của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **9. Fundamental Theorem of Algebra: vì sao complex numbers đủ?** tiếp nhận điểm tựa từ **8. Polynomial division và remainder theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Vieta relations: roots và coefficients nói cùng một story** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Fundamental Theorem of Algebra: vì sao complex numbers đủ?

Fundamental Theorem of Algebra nói rằng mọi nonconstant polynomial degree `n` với complex coefficients có exactly `n` complex roots counting multiplicity.

Nói trực giác: complex numbers tạo một number hệ thống (system / 시스템) đủ lớn để polynomial equations không cần mở rộng thêm một lớp (class / 클래스) numbers mới chỉ để tìm roots.

Ví dụ

```math
x^2+1=0
```

không có real gốc (root / 루트) nhưng có

```math
x=\pm i.
```

Vì vậy complex numbers không phải appendage kỳ lạ; chúng hoàn thiện algebra của polynomial roots.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **10. Vieta relations: roots và coefficients nói cùng một story** tiếp nhận điểm tựa từ **9. Fundamental Theorem of Algebra: vì sao complex numbers đủ?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Worked example: chọn biểu diễn (representation / 표현) đúng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Vieta relations: roots và coefficients nói cùng một story

Nếu

```math
ax^2+bx+c=a(x-r_1)(x-r_2),
```

khai triển:

```math
ax^2-a(r_1+r_2)x+ar_1r_2.
```

So coefficients:

```math
r_1+r_2=-\frac ba,
```

```math
r_1r_2=\frac ca.
```

Vieta's formulas cho thấy coefficients và roots chỉ là hai coordinate các hệ thống (systems / 시스템들) khác nhau của cùng polynomial cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **10. Vieta relations: roots và coefficients nói cùng một story** cho ta quy tắc; **11. Worked example: chọn biểu diễn (representation / 표현) đúng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **12. Polynomial interpolation: fit dữ liệu (data / 데이터) bằng polynomial có giới hạn gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Worked example: chọn biểu diễn (representation / 표현) đúng

Xét

```math
P(x)=x^2-6x+8.
```

Muốn tìm roots, factorization phù hợp:

```math
P(x)=(x-2)(x-4).
```

Roots: `2,4`.

Muốn tìm vertex, complete square:

```math
P(x)=(x-3)^2-1.
```

Vertex: `(3,-1)`.

Muốn evaluate tại many `x`, expanded/Horner biểu diễn (representation / 표현) có thể thuận tiện hơn.

Không có form “tốt nhất” tuyệt đối; form tốt phụ thuộc question.

> **Chuyển mạch:** Ở chặng này của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **11. Worked example: chọn biểu diễn (representation / 표현) đúng** cho ta quy tắc; **12. Polynomial interpolation: fit dữ liệu (data / 데이터) bằng polynomial có giới hạn gì?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **13. Taylor polynomial: polynomial như cục bộ (local / 로컬) ngôn ngữ (language / 언어) của smooth functions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Polynomial interpolation: fit dữ liệu (data / 데이터) bằng polynomial có giới hạn gì?

Qua `n+1` points có distinct x-values, tồn tại unique polynomial degree at most `n` đi qua tất cả points.

Điều này nghe rất mạnh, nhưng chính xác (exact / 정확한) interpolation không đồng nghĩa good mô hình (model / 모델).

High-degree toàn cục (global / 전역) polynomial có thể oscillate mạnh giữa mẫu (sample / 표본) points — Runge phenomenon. dữ liệu (data / 데이터) noise cũng có thể khiến chính xác (exact / 정확한) fit overfit.

Vì vậy numerical công việc (work / 작업) thường dùng splines, low-degree cục bộ (local / 로컬) approximation hoặc regularized fitting thay vì “degree càng cao càng tốt”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **12. Polynomial interpolation: fit dữ liệu (data / 데이터) bằng polynomial có giới hạn gì?** đã nêu tiêu chí phân biệt, còn **13. Taylor polynomial: polynomial như cục bộ (local / 로컬) ngôn ngữ (language / 언어) của smooth functions** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Horner's phương thức (method / 메서드): algebraic form trở thành thuật toán (algorithm / 알고리즘)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Taylor polynomial: polynomial như cục bộ (local / 로컬) ngôn ngữ (language / 언어) của smooth functions

Nếu `f` smooth quanh `a`, Taylor expansion bắt đầu:

```math
f(x)
\approx
f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2+\cdots.
```

Coefficient được chọn để polynomial match derivatives của `f` tại `a`.

Đây là lý do polynomial xuất hiện khắp calculus và numerical methods: gần một điểm (point / 지점), nhiều smooth functions behave như polynomial đến một thứ tự (order / 순서) nhất định.

Ví dụ quanh `0`:

```math
\sin x\approx x-\frac{x^3}{3!}+\frac{x^5}{5!}.
```

> **Chuyển mạch:** Trong **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **14. Horner's phương thức (method / 메서드): algebraic form trở thành thuật toán (algorithm / 알고리즘)** tiếp nhận điểm tựa từ **13. Taylor polynomial: polynomial như cục bộ (local / 로컬) ngôn ngữ (language / 언어) của smooth functions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Numerical conditioning của roots** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Horner's phương thức (method / 메서드): algebraic form trở thành thuật toán (algorithm / 알고리즘)

Thay vì evaluate

```math
P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0
```

bằng cách tính từng power riêng, viết nested:

```math
P(x)=(((a_nx+a_{n-1})x+a_{n-2})x+\cdots)+a_0.
```

Horner's phương thức (method / 메서드) dùng `O(n)` multiplications/additions và giảm intermediate công việc (work / 작업).

Ví dụ

```math
2x^3-3x^2+4x-5
```

thành

```math
((2x-3)x+4)x-5.
```

Đây là một liên kết (connection / 연결) trực tiếp giữa symbolic biểu diễn (representation / 표현) và computational efficiency.

> **Chuyển mạch:** Ở chặng này của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **15. Numerical conditioning của roots** tiếp nhận điểm tựa từ **14. Horner's phương thức (method / 메서드): algebraic form trở thành thuật toán (algorithm / 알고리즘)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Polynomials trong signals, điều khiển (control / 제어) và approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Numerical conditioning của roots

Không phải mọi gốc (root / 루트) đều numerically stable. Small perturbations coefficients có thể gây large changes roots, đặc biệt với multiple hoặc clustered roots.

Điều này quan trọng vì symbolic định danh (identity / 식별자) và numerical computation là hai tầng khác nhau. Một chính xác (exact / 정확한) polynomial theorem không guarantee floating-point root-finding sẽ easy.

Companion matrices còn cho phép chuyển polynomial-root bài toán (problem / 문제) thành eigenvalue bài toán (problem / 문제), nối algebra với tuyến tính (linear / 선형) algebra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **16. Polynomials trong signals, điều khiển (control / 제어) và approximation** tiếp nhận điểm tựa từ **15. Numerical conditioning của roots** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. thất bại (failure / 실패) modes khi factorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Polynomials trong signals, điều khiển (control / 제어) và approximation

Transfer functions thường có numerator/denominator polynomials. Roots của denominator là poles, liên quan stability của hệ động (dynamic system / 동적 시스템).

Characteristic polynomial

```math
\det(A-\lambda I)
```

có roots là eigenvalues. Vì vậy polynomial factorization kết nối trực tiếp với dynamics, điều khiển (control / 제어) và tuyến tính (linear / 선형) algebra.

> **Chuyển mạch:** Trong **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **17. thất bại (failure / 실패) modes khi factorization** tiếp nhận điểm tựa từ **16. Polynomials trong signals, điều khiển (control / 제어) và approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Applications và connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. thất bại (failure / 실패) modes khi factorization

### Không phải polynomial nào cũng factor đẹp trên integers

Ví dụ

```math
x^2-2
```

không factor thành tuyến tính (linear / 선형) factors với rational coefficients, nhưng factor trên reals:

```math
(x-\sqrt2)(x+\sqrt2).
```

### Repeated roots dễ bị bỏ sót nếu chỉ nhìn sign thay đổi (change / 변경)

Even multiplicity roots có thể touch axis mà không đổi sign.

### Chính xác (exact / 정확한) symbolic factorization và numerical factorization khác nhau

Trong high degree hoặc floating coefficients, “factor” có thể nhạy với noise và tolerance.

> **Chuyển mạch:** Ở chặng này của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **Applications và connections** tiếp nhận điểm tựa từ **17. thất bại (failure / 실패) modes khi factorization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Applications và connections

**Khoa học máy tính (computer science / 컴퓨터 과학):** Horner evaluation, symbolic algebra, polynomial hashing và coding lý thuyết (theory / 이론).

**Physics:** characteristic equations, cục bộ (local / 로컬) approximations và perturbation các mô hình (models / 모델들).

**AI:** polynomial features, kernel approximations và Taylor-based phân tích (analysis / 분석).

**Finance:** cục bộ (local / 로컬) approximations của pricing/rủi ro (risk / 위험) functions và polynomial regression, nhưng high-degree fits cần cảnh giác overfitting.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Applications và connections** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Polynomial là một đối tượng (object / 객체) có nhiều representations. Expanded coefficients, factors, roots, vertex form và Taylor form không phải các chủ đề riêng; chúng là những “camera angles” khác nhau. Algebra mạnh lên khi ta biết đổi biểu diễn (representation / 표현) để cấu trúc (structure / 구조) cần thiết trở nên nhìn thấy được.

> **Chuyển mạch:** Trong **Đa thức và phân tích nhân tử: cấu trúc (structure / 구조), roots và approximation**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**Factorization chỉ là technique để solve quadratics.** Không; nó bộc lộ gốc (root / 루트), multiplicity và structural decomposition.

**Degree cao luôn fit tốt hơn.** Không; interpolation có thể oscillate và overfit.

**gốc (root / 루트) là thuộc tính (property / 속성) tách khỏi number hệ thống (system / 시스템).** Không; factorization phụ thuộc coefficient/lĩnh vực (domain / 도메인) trường dữ liệu (field / 필드) đang dùng.

**Polynomial evaluation chỉ là thay số.** Trong computation, biểu diễn (representation / 표현) như Horner form ảnh hưởng chi phí (cost / 비용) và numerical hành vi (behavior / 동작).

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
