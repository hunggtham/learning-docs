# Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. chuỗi (sequence / 시퀀스) và series khác nhau ở đối tượng (object / 객체) đang hội tụ** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Geometric series là prototype của convergence** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối chuỗi vô hạn với hội tụ, chuỗi lũy thừa và bán kính hội tụ, để biết khi nào phép biến đổi vô hạn còn giữ ý nghĩa.

Một chuỗi vô hạn (infinite series / 무한급수) không phải “cộng xong vô hạn số”. Nó là một statement về **limit của các tổng hữu hạn**.

Nếu

```math
S_N=\sum_{n=1}^{N}a_n,
```

thì

```math
\sum_{n=1}^{\infty}a_n=S
```

nghĩa là

```math
\lim_{N\to\infty}S_N=S.
```

Do đó mọi lập luận (reasoning / 추론) về infinite series cuối cùng đều quay về ba câu hỏi:

```text
partial sums có bị bounded không?
partial sums có settle về một limit không?
tail còn lại sau N terms có nhỏ đến đâu?
```

## 1. chuỗi (sequence / 시퀀스) và series khác nhau ở đối tượng (object / 객체) đang hội tụ

Chuỗi (sequence / 시퀀스):

```math
a_1,a_2,a_3,\ldots
```

Series:

```math
a_1+a_2+a_3+\cdots
```

Series convergence thực chất là convergence của chuỗi (sequence / 시퀀스) partial sums:

```math
S_1,S_2,S_3,\ldots
```

Đây là reason điều kiện (condition / 조건)

```math
a_n\to0
```

chỉ là necessary, không sufficient.

Terms nhỏ dần không guarantee cumulative sum bounded.

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **1. chuỗi (sequence / 시퀀스) và series khác nhau ở đối tượng (object / 객체) đang hội tụ** đặt đầu vào cho **2. Geometric series là prototype của convergence**, rồi **3. Infinite series là approximation + lỗi (error / 오류) ngân sách (budget / 예산)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Geometric series là prototype của convergence

Cho

```math
S_N=1+r+r^2+\cdots+r^N.
```

Nhân `r`:

```math
rS_N=r+r^2+\cdots+r^{N+1}.
```

Subtract:

```math
(1-r)S_N=1-r^{N+1}.
```

Do đó

```math
S_N=\frac{1-r^{N+1}}{1-r}.
```

Nếu `|r|<1`:

```math
r^{N+1}\to0,
```

nên

```math
\sum_{n=0}^{\infty}r^n
=\frac1{1-r}.
```

Nếu `|r|\ge1`, terms không decay phù hợp và series không converge theo ordinary sense.

Geometric series là benchmark vì nhiều convergence tests hỏi: tail có behave giống geometric decay không?

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **3. Infinite series là approximation + lỗi (error / 오류) ngân sách (budget / 예산)** nối từ **2. Geometric series là prototype của convergence** sang **4. Vì sao an → 0 chưa đủ?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Infinite series là approximation + lỗi (error / 오류) ngân sách (budget / 예산)

Trong computation ta chỉ dùng finite `N`:

```math
S_N=\sum_{n=0}^{N}a_n.
```

True infinite sum nếu tồn tại:

```math
S=S_N+R_N
```

với remainder/tail:

```math
R_N=\sum_{n=N+1}^{\infty}a_n.
```

Một convergence theorem hữu ích không chỉ nói “converges”, mà nên giúp bound `R_N`.

Với geometric series:

```math
|R_N|
\le
\frac{|r|^{N+1}}{1-|r|}.
```

Convergence vì vậy nối pure phân tích (analysis / 분석) với numerical lỗi (error / 오류) điều khiển (control / 제어).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **4. Vì sao an → 0 chưa đủ?** nối từ **3. Infinite series là approximation + lỗi (error / 오류) ngân sách (budget / 예산)** sang **5. p-series cho benchmark polynomial decay**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Vì sao a_n → 0 chưa đủ?

Harmonic series:

```math
\sum_{n=1}^{\infty}\frac1n
```

diverges dù

```math
\frac1n\to0.
```

Grouping proof:

```text
1
+ 1/2
+ (1/3+1/4)
+ (1/5+...+1/8)
+ ...
```

Mỗi khối (block / 블록) sau khối (block / 블록) đầu có sum ít nhất `1/2`.

Vì partial sums tăng thêm ít nhất một amount cố định qua infinitely many blocks, chúng không bounded.

Key lesson:

> cục bộ (local / 로컬) smallness của term không quyết định toàn cục (global / 전역) accumulation.

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **5. p-series cho benchmark polynomial decay** nối từ **4. Vì sao an → 0 chưa đủ?** sang **6. Integral kiểm thử (test / 테스트) nối discrete sum với continuous area**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. p-series cho benchmark polynomial decay

Series

```math
\sum_{n=1}^{\infty}\frac1{n^p}
```

converges iff

```math
p>1.
```

Nếu `p=1`, harmonic series diverges.

Nếu `p>1`, decay đủ nhanh.

Nếu `p<1`, decay còn chậm hơn harmonic.

p-series là benchmark cho algebraic/polynomial tail, giống geometric series là benchmark cho exponential tail.

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **6. Integral kiểm thử (test / 테스트) nối discrete sum với continuous area** nối từ **5. p-series cho benchmark polynomial decay** sang **7. Comparison kiểm thử (test / 테스트) là asymptotic domination**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Integral kiểm thử (test / 테스트) nối discrete sum với continuous area

Nếu `f(x)` positive, continuous, decreasing và

```math
a_n=f(n),
```

thì hành vi (behavior / 동작) của

```math
\sum_{n=1}^{\infty}a_n
```

liên hệ với

```math
\int_1^{\infty}f(x)\,dx.
```

Intuition: rectangles dưới/trên curve bound lẫn nhau.

Với

```math
f(x)=x^{-p},
```

integral converges iff `p>1`, cho p-series criterion.

Đây là một example quan trọng về liên kết kiến thức (knowledge connection / 지식 연결):

```text
discrete accumulation ↔ continuous accumulation
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **7. Comparison kiểm thử (test / 테스트) là asymptotic domination** nối từ **6. Integral kiểm thử (test / 테스트) nối discrete sum với continuous area** sang **8. Limit comparison tập trung vào asymptotic ratio**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Comparison kiểm thử (test / 테스트) là asymptotic domination

Nếu eventually

```math
0\le a_n\le b_n
```

và

```math
\sum b_n
```

converges, thì

```math
\sum a_n
```

converges.

Ngược lại nếu

```math
a_n\ge b_n\ge0
```

và `\sum b_n` diverges, thì `\sum a_n` diverges.

Comparison không cần chính xác (exact / 정확한) sum. Nó chỉ cần relative tail kích thước (size / 크기).

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **7. Comparison kiểm thử (test / 테스트) là asymptotic domination** đặt tiêu chí; **8. Limit comparison tập trung vào asymptotic ratio** dùng tiêu chí đó để kiểm tra ranh giới, rồi **9. Ratio kiểm thử (test / 테스트) nhìn geometric shrink tỷ lệ (rate / 비율)** mở rộng hệ quả.

## 8. Limit comparison tập trung vào asymptotic ratio

Nếu

```math
\lim_{n\to\infty}\frac{a_n}{b_n}=c,
\qquad 0<c<\infty,
```

với positive terms, thì hai series có cùng convergence hành vi (behavior / 동작).

Reason: eventually chúng chỉ khác nhau bởi constant factors.

Đây là series phiên bản (version / 버전) của asymptotic equivalence.

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **8. Limit comparison tập trung vào asymptotic ratio** đặt tiêu chí; **9. Ratio kiểm thử (test / 테스트) nhìn geometric shrink tỷ lệ (rate / 비율)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **10. gốc (root / 루트) kiểm thử (test / 테스트) nhìn exponential quy mô (scale / 규모) trực tiếp** mở rộng hệ quả.

## 9. Ratio kiểm thử (test / 테스트) nhìn geometric shrink tỷ lệ (rate / 비율)

Cho

```math
L=
\lim_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|.
```

Nếu `L<1`, tail behaves roughly geometric → absolute convergence.

Nếu `L>1`, terms không tiến về zero đúng cách → divergence.

Nếu `L=1`, kiểm thử (test / 테스트) inconclusive.

Ratio kiểm thử (test / 테스트) đặc biệt mạnh khi factorial/exponential terms xuất hiện.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **10. gốc (root / 루트) kiểm thử (test / 테스트) nhìn exponential quy mô (scale / 규모) trực tiếp** nối từ **9. Ratio kiểm thử (test / 테스트) nhìn geometric shrink tỷ lệ (rate / 비율)** sang **11. Alternating series và cancellation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. gốc (root / 루트) kiểm thử (test / 테스트) nhìn exponential quy mô (scale / 규모) trực tiếp

Cho

```math
L=
\limsup_{n\to\infty}|a_n|^{1/n}.
```

Nếu `L<1`, absolute convergence.

Nếu `L>1`, divergence.

Gốc (root / 루트) kiểm thử (test / 테스트) hữu ích khi term có cấu trúc (structure / 구조) `(... )^n`.

Ratio và gốc (root / 루트) tests đều hỏi cùng một deep question:

> asymptotic multiplicative decay có factor dưới 1 không?

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **11. Alternating series và cancellation** nối từ **10. gốc (root / 루트) kiểm thử (test / 테스트) nhìn exponential quy mô (scale / 규모) trực tiếp** sang **12. Absolute vs conditional convergence**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Alternating series và cancellation

Series alternating:

```math
\sum_{n=1}^{\infty}(-1)^{n+1}b_n,
\qquad b_n\ge0.
```

Nếu `b_n` decrease về 0, alternating series kiểm thử (test / 테스트) cho convergence.

Reason trực giác: partial sums overshoot/undershoot limit với oscillation ngày càng nhỏ.

Remainder bound:

```math
|R_N|\le b_{N+1}.
```

Đây là một trong những lỗi (error / 오류) bounds rất practical.

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **12. Absolute vs conditional convergence** nối từ **11. Alternating series và cancellation** sang **13. Rearrangement cho thấy infinite sums khác finite sums**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Absolute vs conditional convergence

Absolute convergence:

```math
\sum|a_n|<\infty.
```

Thì `\sum a_n` converge.

Conditional convergence xảy ra khi `\sum a_n` converge nhưng `\sum|a_n|` diverges.

Alternating harmonic:

```math
1-\frac12+\frac13-\frac14+\cdots
```

là example.

Absolute convergence mạnh hơn vì rearrangement hành vi (behavior / 동작) ổn định hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **13. Rearrangement cho thấy infinite sums khác finite sums** nối từ **12. Absolute vs conditional convergence** sang **14. Cauchy criterion nhìn tail thay vì unknown limit**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Rearrangement cho thấy infinite sums khác finite sums

Finite addition commutative/associative không gây vấn đề.

Nhưng với conditionally convergent series, rearranging terms có thể đổi sum hoặc làm diverge (Riemann rearrangement phenomenon).

Điều này không “phá” arithmetic; nó cho thấy limit tiến trình (process / 프로세스) thêm các giả định (assumptions / 가정들) vào phép cộng vô hạn.

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **13. Rearrangement cho thấy infinite sums khác finite sums** đặt tiêu chí; **14. Cauchy criterion nhìn tail thay vì unknown limit** dùng tiêu chí đó để kiểm tra ranh giới, rồi **15. Power series là polynomial với infinitely many degrees** mở rộng hệ quả.

## 14. Cauchy criterion nhìn tail thay vì unknown limit

Series converge iff:

```math
\forall\varepsilon>0,
\exists N
```

sao cho với mọi `m>n\ge N`:

```math
\left|
\sum_{k=n+1}^{m}a_k
\right|<\varepsilon.
```

Interpretation:

> sufficiently far out, every finite chunk của tail phải có total contribution arbitrarily small.

Cauchy criterion rất quan trọng vì không cần biết limit `S` trước.

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **14. Cauchy criterion nhìn tail thay vì unknown limit** đặt tiêu chí; **15. Power series là polynomial với infinitely many degrees** dùng tiêu chí đó để kiểm tra ranh giới, rồi **16. Radius of convergence đến từ coefficient growth** mở rộng hệ quả.

## 15. Power series là polynomial với infinitely many degrees

Power series quanh center `a`:

```math
\sum_{n=0}^{\infty}c_n(x-a)^n.
```

Nó không chỉ là một series number; convergence phụ thuộc `x`.

Thường tồn tại radius `R` sao cho:

```text
|x-a| < R  → absolute convergence
|x-a| > R  → divergence
|x-a| = R  → phải xét riêng
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **16. Radius of convergence đến từ coefficient growth** nối từ **15. Power series là polynomial với infinitely many degrees** sang **17. Endpoint hành vi (behavior / 동작) cần check riêng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Radius of convergence đến từ coefficient growth

Cauchy–Hadamard formula:

```math
\frac1R
=
\limsup_{n\to\infty}|c_n|^{1/n}.
```

Trong many textbook cases, ratio kiểm thử (test / 테스트) cho:

```math
R=
\lim_{n\to\infty}
\left|
\frac{c_n}{c_{n+1}}
\right|
```

nếu limit phù hợp tồn tại.

Radius encode competition giữa coefficient growth và power `(x-a)^n`.

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **17. Endpoint hành vi (behavior / 동작) cần check riêng** nối từ **16. Radius of convergence đến từ coefficient growth** sang **18. Term-by-term differentiation/tích hợp (integration / 통합)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Endpoint hành vi (behavior / 동작) cần check riêng

Ví dụ power series có `R=1`.

Tại `x=1`, series có thể converge.

Tại `x=-1`, có thể diverge hoặc converge conditionally.

Radius chỉ quyết định inside/outside; ranh giới (boundary / 경계) thường cần kiểm thử (test / 테스트) riêng.

Đây là dùng chung (common / 공통) exam trap nhưng sâu hơn là ranh giới (boundary / 경계) thường có qualitatively different cancellation.

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **18. Term-by-term differentiation/tích hợp (integration / 통합)** nối từ **17. Endpoint hành vi (behavior / 동작) cần check riêng** sang **19. Geometric series như generator**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Term-by-term differentiation/tích hợp (integration / 통합)

Inside radius of convergence, power series behave rất tốt.

Nếu

```math
f(x)=\sum_{n=0}^{\infty}c_n(x-a)^n,
```

thì trong interior:

```math
f'(x)=
\sum_{n=1}^{\infty}
nc_n(x-a)^{n-1}
```

và

```math
\int f(x)dx
=
C+
\sum_{n=0}^{\infty}
\frac{c_n}{n+1}(x-a)^{n+1}.
```

Radius remains the same, though endpoints may thay đổi (change / 변경) hành vi (behavior / 동작).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **19. Geometric series như generator** nối từ **18. Term-by-term differentiation/tích hợp (integration / 통합)** sang **20. Series solution của differential equations**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Geometric series như generator

Định danh (identity / 식별자):

```math
\frac1{1-x}
=
1+x+x^2+x^3+\cdots,
\qquad |x|<1.
```

Differentiate:

```math
\frac1{(1-x)^2}
=
1+2x+3x^2+\cdots.
```

Integrate:

```math
-\ln(1-x)
=
x+\frac{x^2}{2}+\frac{x^3}{3}+\cdots.
```

Một simple series định danh (identity / 식별자) có thể generate cả family identities.

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **20. Series solution của differential equations** nối từ **19. Geometric series như generator** sang **21. Series trong numerical computing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Series solution của differential equations

Nếu closed-form solution khó, assume

```math
y(x)=\sum_{n=0}^{\infty}a_nx^n.
```

Substitute vào ODE để derive recurrence cho coefficients `a_n`.

Đây là cầu nối (bridge / 브리지):

```text
differential equation
→ power series
→ coefficient recurrence
```

Special functions thường xuất hiện theo cách này.

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **21. Series trong numerical computing** nối từ **20. Series solution của differential equations** sang **22. Slow convergence vs acceleration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Series trong numerical computing

Máy tính luôn truncate:

```math
f(x)\approx\sum_{n=0}^{N}a_n.
```

Practical accuracy phụ thuộc:

- truncation lỗi (error / 오류);
- rounding lỗi (error / 오류);
- cancellation;
- evaluation thứ tự (order / 순서);
- distance tới convergence ranh giới (boundary / 경계).

Một mathematically convergent series có thể là numerically poor thuật toán (algorithm / 알고리즘) nếu convergence quá chậm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **22. Slow convergence vs acceleration** nối từ **21. Series trong numerical computing** sang **23. xác suất (probability / 확률) liên kết (connection / 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Slow convergence vs acceleration

Harmonic-like tails hoặc `r` gần 1 làm convergence rất chậm.

Nếu geometric ratio `r=0.999`, cần rất nhiều terms.

Môi trường vận hành (production / 운영 환경) numerical methods thường dùng transformed approximations, rational approximants hoặc convergence acceleration thay vì raw summation.

Mathematical convergence không đồng nghĩa computational efficiency.

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, sau nội dung của **22. Slow convergence vs acceleration**, **23. xác suất (probability / 확률) liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **24. Finance liên kết (connection / 연결): present giá trị (value / 값) as geometric-like series** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. xác suất (probability / 확률) liên kết (connection / 연결)

Expected giá trị (value / 값) của discrete random variable là series:

```math
E[X]=\sum_x xP(X=x).
```

Interchanging sums/limits/expectations cần convergence conditions.

Absolute convergence/integrability giúp justify manipulations mà finite sums cho phép tự do hơn.

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **24. Finance liên kết (connection / 연결): present giá trị (value / 값) as geometric-like series** nối từ **23. xác suất (probability / 확률) liên kết (connection / 연결)** sang **25. CS liên kết (connection / 연결): geometric công việc (work / 작업) bounds**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Finance liên kết (connection / 연결): present giá trị (value / 값) as geometric-like series

Perpetuity payment `C` với discount tỷ lệ (rate / 비율) `r>0`:

```math
PV
=
\sum_{n=1}^{\infty}
\frac{C}{(1+r)^n}.
```

Đây là geometric series với ratio

```math
\frac1{1+r}<1.
```

Do đó

```math
PV=\frac Cr.
```

Formula finance nổi tiếng chỉ là geometric-series convergence dưới các giả định (assumptions / 가정들) constant payment/tỷ lệ (rate / 비율).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **25. CS liên kết (connection / 연결): geometric công việc (work / 작업) bounds** nối từ **24. Finance liên kết (connection / 연결): present giá trị (value / 값) as geometric-like series** sang **26. Worked example: lỗi (error / 오류) mục tiêu (target / 대상)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. CS liên kết (connection / 연결): geometric công việc (work / 작업) bounds

Động (dynamic / 동적) array doubling costs:

```text
1 + 2 + 4 + ... + n
```

là finite geometric sum `O(n)`.

Reverse-looking shrink processes:

```text
n + n/2 + n/4 + ...
```

cũng bounded bởi `2n`.

Geometric series là foundation của many amortized/divide-and-conquer arguments.

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **25. CS liên kết (connection / 연결): geometric công việc (work / 작업) bounds** nêu quy tắc; **26. Worked example: lỗi (error / 오류) mục tiêu (target / 대상)** thử quy tắc trong tình huống, rồi **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả.

## 26. Worked example: lỗi (error / 오류) mục tiêu (target / 대상)

Approximate

```math
\frac1{1-r}
```

bằng first `N+1` geometric terms.

Tail:

```math
|R_N|
=
\frac{|r|^{N+1}}{1-|r|}.
```

Muốn lỗi (error / 오류) < `\varepsilon`:

```math
\frac{|r|^{N+1}}{1-|r|}<\varepsilon.
```

Taking logs cho minimum `N`.

Series convergence biến thành kỹ thuật (engineering / 엔지니어링) question: bao nhiêu terms đủ?

> **Nối mạch:** Ở chặng này của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **26. Worked example: lỗi (error / 오류) mục tiêu (target / 대상)** nêu quy tắc; **Liên kết kiến thức (knowledge connection / 지식 연결)** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối đặt hội tụ và power series cạnh approximation, probability, differential equations và numerical computation. Hãy xem điều kiện hội tụ như ranh giới an toàn của phép biến đổi.

```text
sequence limits
→ partial sums
→ convergence tests
→ error bounds
→ power series
→ Taylor series
→ ODE series solutions
→ numerical approximation
→ probability expectations
→ finance discounting
→ algorithmic geometric bounds
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Infinite series là một **accumulation tiến trình (process / 프로세스) controlled by a limit**. Convergence không hỏi từng term có nhỏ không; nó hỏi **remaining tail có thể làm arbitrarily small không**. Power series thêm một variable vào tiến trình (process / 프로세스) này, biến convergence thành một thuộc tính (property / 속성) của region quanh center.

> **Nối mạch:** Trong **Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

`a_n\to0` không đủ cho series convergence. “Convergent” không nghĩa fast enough for computation. Absolute và conditional convergence không interchangeable. Power series không automatically valid cho mọi `x`. Endpoints phải được check riêng. Rearrangement của conditionally convergent series có thể đổi result. Một theorem cho convergence mà không có useful error bound đôi khi chưa đủ cho numerical use.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
