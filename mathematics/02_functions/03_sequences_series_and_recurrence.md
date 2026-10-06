# Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. chuỗi (sequence / 시퀀스) là hàm (function / 함수) trên discrete chỉ mục (index / 인덱스)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. tường minh (explicit / 명시적) formula và recurrence encode thông tin (information / 정보) khác nhau** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối sequences, series và recurrence với quy luật sinh, hội tụ và dự báo, để phân biệt tổng hữu hạn với quá trình lặp.

Dãy số (sequence / 수열) là hàm (function / 함수) có lĩnh vực (domain / 도메인) rời rạc, thường là

```math
n=0,1,2,\ldots
```

Thay vì hỏi “đầu ra (output / 출력) thay đổi thế nào theo real đầu vào (input / 입력) liên tục?”, chuỗi (sequence / 시퀀스) hỏi “trạng thái (state / 상태) ở step `n` là gì?”. Đây là ngôn ngữ tự nhiên của monthly balance, iteration, population generations, thuật toán (algorithm / 알고리즘) thời gian chạy (runtime / 런타임) và discrete-time các hệ thống (systems / 시스템들).

Ba khái niệm cần phân biệt ngay từ đầu:

```text
sequence   → values theo từng step
recurrence → rule chuyển từ state cũ sang state mới
series     → accumulation của sequence terms
```

## 1. chuỗi (sequence / 시퀀스) là hàm (function / 함수) trên discrete chỉ mục (index / 인덱스)

Một chuỗi (sequence / 시퀀스) có thể viết

```math
a_0,a_1,a_2,\ldots
```

hoặc như hàm (function / 함수):

```math
a:\mathbb N\to\mathbb R.
```

Ví dụ:

```math
a_n=2n+1.
```

Các terms:

```text
1,3,5,7,...
```

Cách nhìn hàm (function / 함수) giúp chuỗi (sequence / 시퀀스) nối tự nhiên với limits, asymptotics và algorithms.

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **1. chuỗi (sequence / 시퀀스) là hàm (function / 함수) trên discrete chỉ mục (index / 인덱스)** đặt đầu vào cho **2. tường minh (explicit / 명시적) formula và recurrence encode thông tin (information / 정보) khác nhau**, rồi **3. Arithmetic chuỗi (sequence / 시퀀스) = constant additive thay đổi (change / 변경)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. tường minh (explicit / 명시적) formula và recurrence encode thông tin (information / 정보) khác nhau

Tường minh (explicit / 명시적) form:

```math
a_n=2n+1
```

cho phép jump trực tiếp tới term `n`.

Recursive form:

```math
a_{n+1}=a_n+2,
\qquad a_0=1
```

nhấn mạnh chuyển tiếp (transition / 전이) quy tắc (rule / 규칙).

Hai representations có thể mô tả cùng chuỗi (sequence / 시퀀스) nhưng phục vụ questions khác nhau.

Tường minh (explicit / 명시적) formula phù hợp random truy cập (access / 접근). Recurrence phù hợp tiến trình (process / 프로세스) evolution.

Trong computing, đây gần distinction giữa:

```text
closed-form evaluation
vs
state iteration
```

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **2. tường minh (explicit / 명시적) formula và recurrence encode thông tin (information / 정보) khác nhau** đặt đầu vào cho **3. Arithmetic chuỗi (sequence / 시퀀스) = constant additive thay đổi (change / 변경)**, rồi **4. Arithmetic series và vì sao sum quy mô (scale / 규모) như n²** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. Arithmetic chuỗi (sequence / 시퀀스) = constant additive thay đổi (change / 변경)

Nếu difference constant `d`:

```math
a_{n+1}-a_n=d,
```

thì

```math
a_n=a_0+nd.
```

Đây là discrete counterpart của tuyến tính (linear / 선형) hàm (function / 함수).

Mental liên kết (connection / 연결):

```text
constant discrete difference → linear sequence
constant derivative → linear continuous function
```

Finite difference đóng vai trò gần giống derivative trong discrete setting.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **3. Arithmetic chuỗi (sequence / 시퀀스) = constant additive thay đổi (change / 변경)** đặt đầu vào cho **4. Arithmetic series và vì sao sum quy mô (scale / 규모) như n²**, rồi **5. Geometric chuỗi (sequence / 시퀀스) = constant multiplicative thay đổi (change / 변경)** mở rộng hệ quả hoặc giới hạn liên quan.

## 4. Arithmetic series và vì sao sum quy mô (scale / 규모) như n²

Tổng:

```math
S_n=1+2+\cdots+n.
```

Pair first + last:

```text
1+n
2+(n-1)
3+(n-2)
...
```

mỗi pair sum `n+1`.

Kết quả:

```math
S_n=\frac{n(n+1)}2.
```

Nếu term grow như `O(n)`, cumulative sum thường grow như `O(n^2)`.

Đây là intuition quan trọng trong phân tích độ phức tạp (complexity analysis / 복잡도 분석): accumulation tăng thứ tự (order / 순서) growth lên một bậc trong nhiều trường hợp polynomial.

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **4. Arithmetic series và vì sao sum quy mô (scale / 규모) như n²** đặt đầu vào cho **5. Geometric chuỗi (sequence / 시퀀스) = constant multiplicative thay đổi (change / 변경)**, rồi **6. Derive finite geometric sum thay vì học thuộc** mở rộng hệ quả hoặc giới hạn liên quan.

## 5. Geometric chuỗi (sequence / 시퀀스) = constant multiplicative thay đổi (change / 변경)

Nếu ratio constant `r`:

```math
a_{n+1}=ra_n,
```

thì

```math
a_n=a_0r^n.
```

Đây là discrete exponential growth/decay.

Nếu `|r|<1`, magnitude decay.

Nếu `r>1`, growth exponential.

Nếu `r<0`, signs alternate.

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **5. Geometric chuỗi (sequence / 시퀀스) = constant multiplicative thay đổi (change / 변경)** đặt đầu vào cho **6. Derive finite geometric sum thay vì học thuộc**, rồi **7. Infinite geometric series là limit của partial sums** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. Derive finite geometric sum thay vì học thuộc

Cho

```math
S_n=a_0+a_0r+\cdots+a_0r^{n-1}.
```

Nhân `r`:

```math
rS_n=a_0r+a_0r^2+\cdots+a_0r^n.
```

Subtract:

```math
S_n-rS_n=a_0-a_0r^n.
```

Do đó

```math
S_n=a_0\frac{1-r^n}{1-r},
\qquad r\ne1.
```

Formula xuất hiện vì shift-by-one làm almost all terms cancel.

Đây là một proof mẫu (pattern / 패턴) rất phổ biến: transform expression để cấu trúc (structure / 구조) cancellation lộ ra.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **6. Derive finite geometric sum thay vì học thuộc** đặt tiêu chí; **7. Infinite geometric series là limit của partial sums** dùng tiêu chí đó để kiểm tra ranh giới, rồi **8. Recurrence là equation của chuyển tiếp trạng thái (state transition / 상태 전이)** mở rộng hệ quả.

## 7. Infinite geometric series là limit của partial sums

Ta không “cộng xong vô hạn terms”. Ta định nghĩa

```math
\sum_{k=0}^{\infty}a_0r^k
=
\lim_{n\to\infty}S_n.
```

Nếu `|r|<1`:

```math
r^n\to0
```

nên

```math
\sum_{k=0}^{\infty}a_0r^k
=
\frac{a_0}{1-r}.
```

Điều kiện (condition / 조건) `|r|<1` là essential giả định (assumption / 가정), không phải decoration.

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **7. Infinite geometric series là limit của partial sums** đặt tiêu chí; **8. Recurrence là equation của chuyển tiếp trạng thái (state transition / 상태 전이)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **9. tuyến tính (linear / 선형) first-order recurrence** mở rộng hệ quả.

## 8. Recurrence là equation của chuyển tiếp trạng thái (state transition / 상태 전이)

General first-order recurrence:

```math
a_{n+1}=F(a_n,n).
```

Nếu `F` không phụ thuộc tường minh (explicit / 명시적) vào `n`:

```math
a_{n+1}=F(a_n),
```

ta có discrete dynamical hệ thống (system / 시스템).

Fixed điểm (point / 지점) `a_*` thỏa

```math
F(a_*)=a_*.
```

Stability hỏi nếu bắt đầu gần `a_*`, iterations có quay về đó không.

Đây là cầu nối (bridge / 브리지) sang numerical methods, tối ưu hóa (optimization / 최적화) và điều khiển (control / 제어).

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **9. tuyến tính (linear / 선형) first-order recurrence** nối từ **8. Recurrence là equation của chuyển tiếp trạng thái (state transition / 상태 전이)** sang **10. Finance example: balance recurrence**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. tuyến tính (linear / 선형) first-order recurrence

Xét

```math
a_{n+1}=ra_n+b.
```

Fixed điểm (point / 지점) nếu `r\ne1`:

```math
a_*=
\frac{b}{1-r}.
```

Subtract fixed điểm (point / 지점):

```math
u_n=a_n-a_*.
```

thì

```math
u_{n+1}=ru_n.
```

Do đó

```math
u_n=r^nu_0
```

và

```math
a_n=a_*+r^n(a_0-a_*).
```

Nếu `|r|<1`, trạng thái (state / 상태) converge tới fixed điểm (point / 지점).

Nếu `|r|>1`, deviations grow.

Đây là một example quan trọng: đổi variables có thể biến recurrence có constant forcing thành geometric recurrence đơn giản.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **9. tuyến tính (linear / 선형) first-order recurrence** nêu quy tắc; **10. Finance example: balance recurrence** thử quy tắc trong tình huống, rồi **11. Fibonacci: recurrence thứ tự (order / 순서) 2** mở rộng hệ quả.

## 10. Finance example: balance recurrence

Nếu account balance tăng tỷ lệ (rate / 비율) `r` mỗi period và thêm contribution `c` cuối period:

```math
B_{n+1}=(1+r)B_n+c.
```

Đây là affine recurrence.

Repeated substitution tạo:

```math
B_n=(1+r)^nB_0
+c\sum_{k=0}^{n-1}(1+r)^k.
```

Geometric sum cho closed form.

Compound interest và annuity formulas thực chất là recurrence + geometric series.

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **10. Finance example: balance recurrence** nêu quy tắc; **11. Fibonacci: recurrence thứ tự (order / 순서) 2** thử quy tắc trong tình huống, rồi **12. Characteristic equation intuition** mở rộng hệ quả.

## 11. Fibonacci: recurrence thứ tự (order / 순서) 2

Fibonacci:

```math
F_{n+1}=F_n+F_{n-1}.
```

Trạng thái (state / 상태) ở step `n+1` cần hai previous values.

Ta gom thành véc-tơ (vector / 벡터) trạng thái (state / 상태):

```math
\begin{bmatrix}
F_{n+1}\\
F_n
\end{bmatrix}
=
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}
\begin{bmatrix}
F_n\\
F_{n-1}
\end{bmatrix}.
```

Sau nhiều steps:

```math
x_n=A^nx_0.
```

Eigenvalues của `A` giải thích long-run growth tỷ lệ (rate / 비율).

Đây là liên kết (connection / 연결) sâu giữa recurrence và tuyến tính (linear / 선형) algebra.

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **12. Characteristic equation intuition** nối từ **11. Fibonacci: recurrence thứ tự (order / 순서) 2** sang **13. Recurrence trong thuật toán (algorithm / 알고리즘) phân tích (analysis / 분석)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Characteristic equation intuition

Với homogeneous recurrence:

```math
a_{n+2}=pa_{n+1}+qa_n,
```

thử solution exponential:

```math
a_n=r^n.
```

Substitute:

```math
r^{n+2}=pr^{n+1}+qr^n.
```

Nếu `r\ne0`, divide `r^n`:

```math
r^2-pr-q=0.
```

Roots của characteristic polynomial quyết định modes của solution.

Đây hoàn toàn analogous với solving tuyến tính (linear / 선형) differential equations bằng `e^{\lambda t}`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **13. Recurrence trong thuật toán (algorithm / 알고리즘) phân tích (analysis / 분석)** nối từ **12. Characteristic equation intuition** sang **14. Memoization thay computation đồ thị (graph / 그래프), không thay recurrence definition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Recurrence trong thuật toán (algorithm / 알고리즘) phân tích (analysis / 분석)

Tìm kiếm nhị phân (binary search / 이진 탐색):

```math
T(n)=T(n/2)+c.
```

Mỗi step halve đầu vào (input / 입력), nên độ sâu (depth / 깊이) gần

```math
\log_2n.
```

Merge sort:

```math
T(n)=2T(n/2)+cn.
```

Recursion cây (tree / 트리) có `\log n` levels và mỗi mức (level / 수준) tổng công việc (work / 작업) `O(n)`:

```math
T(n)=O(n\log n).
```

Thời gian chạy (runtime / 런타임) recurrence không phải mã (code / 코드) recursion itself; nó là mathematical mô hình (model / 모델) của công việc (work / 작업) phụ thuộc (dependency / 의존성).

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **14. Memoization thay computation đồ thị (graph / 그래프), không thay recurrence definition** nối từ **13. Recurrence trong thuật toán (algorithm / 알고리즘) phân tích (analysis / 분석)** sang **15. Convergence của chuỗi (sequence / 시퀀스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Memoization thay computation đồ thị (graph / 그래프), không thay recurrence definition

Naive Fibonacci recursion recompute same states nhiều lần.

Recurrence:

```math
F_n=F_{n-1}+F_{n-2}
```

không sai. bài toán (problem / 문제) nằm ở evaluation chiến lược (strategy / 전략).

Memoization lưu solved states, biến computation từ exponential lời gọi (call / 호출) cây (tree / 트리) thành roughly tuyến tính (linear / 선형) number of distinct states.

Động (dynamic / 동적) programming = recurrence + systematic trạng thái (state / 상태) reuse/thứ tự (order / 순서).

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **14. Memoization thay computation đồ thị (graph / 그래프), không thay recurrence definition** đặt đầu vào cho **15. Convergence của chuỗi (sequence / 시퀀스)**, rồi **16. Bounded không imply convergent** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. Convergence của chuỗi (sequence / 시퀀스)

`a_n` converge tới `L` nếu:

```math
\forall\varepsilon>0,
\exists N
\text{ sao cho }
n\ge N
\Rightarrow
|a_n-L|<\varepsilon.
```

Intuition: sau một chỉ mục (index / 인덱스) đủ lớn, mọi terms còn lại nằm trong bất kỳ tolerance band nào quanh `L`.

Ví dụ:

```math
a_n=\frac1n\to0.
```

Chuỗi (sequence / 시퀀스) convergence là foundation cho series, iterative numerical methods và stochastic limit laws.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **15. Convergence của chuỗi (sequence / 시퀀스)** đặt đầu vào cho **16. Bounded không imply convergent**, rồi **17. Series là accumulation, không phải chuỗi (sequence / 시퀀스)** mở rộng hệ quả hoặc giới hạn liên quan.

## 16. Bounded không imply convergent

Chuỗi (sequence / 시퀀스)

```math
a_n=(-1)^n
```

bounded trong `[-1,1]` nhưng không converge vì oscillates giữa ±1.

Monotone bounded theorem nói nếu chuỗi (sequence / 시퀀스) monotone và bounded phù hợp thì converge.

Các giả định (assumptions / 가정들) matter: boundedness alone chưa đủ.

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **16. Bounded không imply convergent** đặt đầu vào cho **17. Series là accumulation, không phải chuỗi (sequence / 시퀀스)**, rồi **18. Vì sao an → 0 chưa đủ?** mở rộng hệ quả hoặc giới hạn liên quan.

## 17. Series là accumulation, không phải chuỗi (sequence / 시퀀스)

Cho chuỗi (sequence / 시퀀스) `a_n`, series là

```math
\sum_{n=1}^{\infty}a_n.
```

Ta define partial sums:

```math
S_N=\sum_{n=1}^{N}a_n.
```

Series converge iff chuỗi (sequence / 시퀀스) `S_N` converge.

Vì vậy series convergence là chuỗi (sequence / 시퀀스) convergence của accumulated trạng thái (state / 상태).

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **17. Series là accumulation, không phải chuỗi (sequence / 시퀀스)** đặt đầu vào cho **18. Vì sao an → 0 chưa đủ?**, rồi **19. Comparison kiểm thử (test / 테스트) là asymptotic lập luận (reasoning / 추론)** mở rộng hệ quả hoặc giới hạn liên quan.

## 18. Vì sao a_n → 0 chưa đủ?

Nếu series converge, terms phải tiến về zero:

```math
a_n\to0.
```

Nhưng converse sai.

Harmonic series:

```math
\sum_{n=1}^{\infty}\frac1n
```

diverges.

Grouping:

```text
1
+ 1/2
+ (1/3+1/4)
+ (1/5+...+1/8)
+ ...
```

mỗi khối (block / 블록) sau có sum ít nhất khoảng `1/2`, nên total không bounded.

Terms giảm nhưng không đủ nhanh.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **19. Comparison kiểm thử (test / 테스트) là asymptotic lập luận (reasoning / 추론)** nối từ **18. Vì sao an → 0 chưa đủ?** sang **20. Ratio kiểm thử (test / 테스트) nhìn multiplicative shrink**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Comparison kiểm thử (test / 테스트) là asymptotic lập luận (reasoning / 추론)

Nếu

```math
0\le a_n\le b_n
```

và

```math
\sum b_n
```

converges, thì `\sum a_n` converges.

Nếu `a_n\ge b_n\ge0` và `\sum b_n` diverges, thì `\sum a_n` diverges.

Ta không cần chính xác (exact / 정확한) sum; chỉ cần compare accumulation tỷ lệ (rate / 비율).

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **20. Ratio kiểm thử (test / 테스트) nhìn multiplicative shrink** nối từ **19. Comparison kiểm thử (test / 테스트) là asymptotic lập luận (reasoning / 추론)** sang **21. Generating-function intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Ratio kiểm thử (test / 테스트) nhìn multiplicative shrink

Ratio test so sánh độ lớn các số hạng liên tiếp để đo tốc độ co theo cấp số nhân. Điều kiện hội tụ đến từ việc chuỗi bị chi phối bởi một geometric decay đủ nhanh.

```math
L=
\lim_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|.
```

Nếu `L<1`, terms eventually shrink gần geometric factor dưới 1, nên absolute convergence.

Nếu `L>1`, terms không thể tiến về zero phù hợp.

Nếu `L=1`, kiểm thử (test / 테스트) inconclusive.

Kiểm thử (test / 테스트) không phải magic quy tắc (rule / 규칙); nó compare series với geometric hành vi (behavior / 동작).

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **21. Generating-function intuition** nối từ **20. Ratio kiểm thử (test / 테스트) nhìn multiplicative shrink** sang **22. Difference equations và điều khiển (control / 제어)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Generating-function intuition

Một chuỗi (sequence / 시퀀스) có thể encode thành power series:

```math
G(x)=\sum_{n=0}^{\infty}a_nx^n.
```

Recurrence relations có thể biến thành algebraic equations cho `G(x)`.

Generating functions là cầu nối (bridge / 브리지) từ discrete sequences sang algebra/complex phân tích (analysis / 분석)/combinatorics.

Không cần đi sâu ở chapter này; important idea là biểu diễn (representation / 표현) thay đổi (change / 변경) có thể turn recurrence into algebra.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **22. Difference equations và điều khiển (control / 제어)** nối từ **21. Generating-function intuition** sang **23. Worked example: iterative approximation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Difference equations và điều khiển (control / 제어)

Continuous các hệ thống (systems / 시스템들):

```math
\frac{dx}{dt}=Ax+Bu.
```

Discrete-time các hệ thống (systems / 시스템들):

```math
x_{k+1}=Ax_k+Bu_k.
```

Ma trận (matrix / 행렬) powers `A^k` quyết định trạng thái (state / 상태) evolution.

Eigenvalues inside đơn vị (unit / 단위) circle thường liên quan stability của discrete hệ tuyến tính (linear system / 선형 시스템), analogous real-part-negative eigenvalues trong continuous các hệ thống (systems / 시스템들).

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **22. Difference equations và điều khiển (control / 제어)** nêu quy tắc; **23. Worked example: iterative approximation** thử quy tắc trong tình huống, rồi **24. dùng chung (common / 공통) modeling patterns** mở rộng hệ quả.

## 23. Worked example: iterative approximation

Newton phương thức (method / 메서드):

```math
x_{n+1}
=
x_n-
\frac{f(x_n)}{f'(x_n)}.
```

Đây là recurrence.

Convergence phân tích (analysis / 분석) hỏi lỗi (error / 오류)

```math
e_n=x_n-x_*
```

biến đổi thế nào từ step này sang step khác.

Nếu near gốc (root / 루트):

```math
|e_{n+1}|\approx C|e_n|^2,
```

ta nói quadratic convergence.

Numerical algorithms vì vậy là dynamical các hệ thống (systems / 시스템들) trên approximation trạng thái (state / 상태).

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **23. Worked example: iterative approximation** nêu quy tắc; **24. dùng chung (common / 공통) modeling patterns** thử quy tắc trong tình huống, rồi **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả.

## 24. dùng chung (common / 공통) modeling patterns

Additive cập nhật (update / 업데이트):

```math
x_{n+1}=x_n+c
```

→ tuyến tính (linear / 선형)/arithmetic growth.

Multiplicative cập nhật (update / 업데이트):

```math
x_{n+1}=rx_n
```

→ exponential/geometric growth.

Phản hồi (feedback / 피드백) cập nhật (update / 업데이트):

```math
x_{n+1}=F(x_n)
```

→ nonlinear discrete dynamics.

Accumulation:

```math
S_{n+1}=S_n+a_{n+1}
```

→ series/ running totals.

Nhận ra mẫu (pattern / 패턴) quan trọng hơn nhớ từng formula riêng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, sau nội dung của **24. dùng chung (common / 공통) modeling patterns**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả hoặc giới hạn liên quan.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Chuỗi (sequence / 시퀀스)/recurrence nối:

```text
functions on integers
→ finite differences
→ series accumulation
→ limits
→ algorithm recurrences
→ dynamic programming
→ matrix powers/eigenvalues
→ numerical iteration
→ finance compounding
→ discrete control
```

> **Nối mạch:** Trong **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> chuỗi (sequence / 시퀀스) là trạng thái (state / 상태) theo discrete thời gian (time / 시간). Recurrence là chuyển tiếp (transition / 전이) law. Series là accumulated trạng thái (state / 상태). Khi quy tắc (rule / 규칙) additive ta thấy tuyến tính (linear / 선형) hành vi (behavior / 동작); khi multiplicative ta thấy exponential hành vi (behavior / 동작); khi quy tắc (rule / 규칙) phản hồi (feedback / 피드백) nonlinear, stability và fixed points trở thành câu hỏi trung tâm.

> **Nối mạch:** Ở chặng này của **Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

Recursive definition không đồng nghĩa recursive implementation là tốt nhất. `a_n\to0` không đủ để `\sum a_n` converge. Bounded sequence chưa chắc converge. Infinite series là limit của partial sums, không phải hành động “thực hiện vô hạn phép cộng”. Closed form không phải lúc nào cũng computationally superior; numerical stability và cost vẫn matter.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
