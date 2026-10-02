# Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. trạng thái (state / 상태) và thay đổi (change / 변경) trả lời hai câu hỏi khác nhau** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **2. Derivative là cục bộ (local / 로컬) tuyến tính (linear / 선형) phản hồi (response / 응답)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối rate of change với accumulation, để đạo hàm và tích phân được đọc như hai hướng của cùng một quá trình.

Một mẫu (pattern / 패턴) xuất hiện xuyên suốt calculus, physics, finance, xác suất (probability / 확률), dữ liệu (data / 데이터) các hệ thống (systems / 시스템들) và tối ưu hóa (optimization / 최적화) là:

```text
state
↔ local change
↔ accumulated change
```

Nếu không nhận ra mẫu (pattern / 패턴) này, derivative, integral, difference equation, thông lượng (throughput / 처리량), marginal chi phí (cost / 비용) và xác suất (probability / 확률) density dễ trông như các khái niệm rời rạc. Thực ra chúng thường là những phiên bản khác nhau của cùng một cấu trúc (structure / 구조).

## 1. trạng thái (state / 상태) và thay đổi (change / 변경) trả lời hai câu hỏi khác nhau

Giả sử quantity `x(t)` thay đổi theo thời gian.

`x(t)` trả lời:

```text
state hiện tại là bao nhiêu?
```

Difference:

```math
\Delta x=x(t_2)-x(t_1)
```

trả lời:

```text
state đã thay đổi bao nhiêu trên interval?
```

Average tỷ lệ (rate / 비율):

```math
\frac{\Delta x}{\Delta t}
```

trả lời:

```text
mỗi unit time, trung bình state thay đổi bao nhiêu?
```

Units giúp phân biệt ba quantities này.

Nếu `x` đo bằng meter:

```text
x           → m
Δx          → m
Δx/Δt       → m/s
```

Tỷ lệ (rate / 비율) không phải total.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **2. Derivative là cục bộ (local / 로컬) tuyến tính (linear / 선형) phản hồi (response / 응답)** tiếp nhận điểm tựa từ **1. trạng thái (state / 상태) và thay đổi (change / 변경) trả lời hai câu hỏi khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Accumulation là inverse question** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Derivative là cục bộ (local / 로컬) tuyến tính (linear / 선형) phản hồi (response / 응답)

Instantaneous tỷ lệ (rate / 비율) được formalize bằng limit:

```math
x'(t)=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
```

Nhưng mô hình tư duy (mental model / 사고 모델) tốt hơn “slope formula” là cục bộ (local / 로컬) approximation:

```math
x(t+h)\approx x(t)+x'(t)h.
```

Derivative nói nếu đầu vào (input / 입력) đổi một amount rất nhỏ thì đầu ra (output / 출력) phản ứng first-order ra sao.

Đây là lý do cùng concept xuất hiện dưới nhiều names:

```text
velocity
marginal cost
sensitivity
gradient
Jacobian
growth rate
```

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **3. Accumulation là inverse question** tiếp nhận điểm tựa từ **2. Derivative là cục bộ (local / 로컬) tuyến tính (linear / 선형) phản hồi (response / 응답)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Vì sao dấu quan trọng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Accumulation là inverse question

Nếu biết tỷ lệ (rate / 비율) `r(t)`, accumulated thay đổi (change / 변경) trên `[a,b]` là:

```math
\int_a^b r(t)\,dt.
```

Nếu:

```math
x'(t)=r(t),
```

thì:

```math
x(b)-x(a)=\int_a^b r(t)\,dt.
```

Đây là Fundamental Theorem of Calculus nhìn như accounting law:

> cộng tất cả cục bộ (local / 로컬) changes cho ra net toàn cục (global / 전역) thay đổi (change / 변경).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **4. Vì sao dấu quan trọng?** tiếp nhận điểm tựa từ **3. Accumulation là inverse question** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Discrete analogue: difference và summation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Vì sao dấu quan trọng?

Integral của tỷ lệ (rate / 비율) là **net accumulation**, không luôn là total amount traveled.

Nếu velocity đổi dấu:

```math
\int v(t)dt
```

cho displacement.

Distance traveled cần:

```math
\int |v(t)|dt.
```

Cùng lô-gic (logic / 논리) trong finance: signed cash luồng (flow / 흐름) netting khác gross giao dịch (transaction / 트랜잭션) volume.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **5. Discrete analogue: difference và summation** tiếp nhận điểm tựa từ **4. Vì sao dấu quan trọng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Recurrence là tỷ lệ (rate / 비율) law cho discrete thời gian (time / 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Discrete analogue: difference và summation

Với chuỗi (sequence / 시퀀스) `a_n`:

```math
\Delta a_n=a_{n+1}-a_n.
```

Summing:

```math
\sum_{n=m}^{N-1}\Delta a_n
=a_N-a_m.
```

Middle terms cancel. Đây là telescoping sum — discrete phiên bản (version / 버전) của Fundamental Theorem.

Mental ánh xạ (mapping / 매핑):

```text
derivative ↔ finite difference
integral   ↔ summation
ODE        ↔ recurrence relation
```

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **6. Recurrence là tỷ lệ (rate / 비율) law cho discrete thời gian (time / 시간)** tiếp nhận điểm tựa từ **5. Discrete analogue: difference và summation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Density cũng là tỷ lệ (rate / 비율) of accumulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Recurrence là tỷ lệ (rate / 비율) law cho discrete thời gian (time / 시간)

Nếu:

```math
a_{n+1}=a_n+r,
```

mỗi step cộng constant amount, nên:

```math
a_n=a_0+nr.
```

Nếu:

```math
a_{n+1}=qa_n,
```

mỗi step quy mô (scale / 규모) theo trạng thái hiện tại (current state / 현재 상태):

```math
a_n=a_0q^n.
```

Additive cập nhật (update / 업데이트) sinh tuyến tính (linear / 선형) hành vi (behavior / 동작); multiplicative cập nhật (update / 업데이트) sinh exponential hành vi (behavior / 동작).

Đây là discrete counterpart của:

```math
x'=k
```

và:

```math
x'=kx.
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **7. Density cũng là tỷ lệ (rate / 비율) of accumulation** tiếp nhận điểm tựa từ **6. Recurrence là tỷ lệ (rate / 비율) law cho discrete thời gian (time / 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. thông lượng (throughput / 처리량) và hàng đợi (queue / 큐) length** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Density cũng là tỷ lệ (rate / 비율) of accumulation

Xác suất (probability / 확률) density `f(x)` không phải xác suất (probability / 확률) tại một điểm (point / 지점).

CDF:

```math
F(x)=P(X\le x)
```

là accumulated xác suất (probability / 확률).

Khi differentiable:

```math
F'(x)=f(x).
```

Và:

```math
P(a\le X\le b)=\int_a^b f(x)dx.
```

Mẫu (pattern / 패턴) hoàn toàn giống:

```text
local density
→ integrate
→ accumulated mass
```

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **8. thông lượng (throughput / 처리량) và hàng đợi (queue / 큐) length** tiếp nhận điểm tựa từ **7. Density cũng là tỷ lệ (rate / 비율) of accumulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Finance: balance là accumulated cash luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. thông lượng (throughput / 처리량) và hàng đợi (queue / 큐) length

Trong hệ thống (system / 시스템) kỹ thuật (engineering / 엔지니어링), hàng đợi (queue / 큐) length `Q(t)` là trạng thái (state / 상태).

Arrival tỷ lệ (rate / 비율) `λ(t)` và dịch vụ (service / 서비스) tỷ lệ (rate / 비율) `μ(t)` cho cục bộ (local / 로컬) thay đổi (change / 변경) roughly:

```math
Q'(t)\approx \lambda(t)-\mu(t)
```

khi dùng continuous approximation.

Nếu arrival > dịch vụ (service / 서비스) lâu dài, backlog tích lũy.

Một dashboard chỉ nhìn thông lượng (throughput / 처리량) mà không nhìn accumulated hàng đợi (queue / 큐) có thể bỏ lỡ overload đang tích tụ.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **8. thông lượng (throughput / 처리량) và hàng đợi (queue / 큐) length** xác định đầu vào; **9. Finance: balance là accumulated cash luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. Marginal vs total trong economics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Finance: balance là accumulated cash luồng (flow / 흐름)

Nếu `B(t)` là account balance và `c(t)` là net cash-flow tỷ lệ (rate / 비율):

```math
B'(t)=c(t)
```

thì:

```math
B(T)=B(0)+\int_0^T c(t)dt.
```

Nếu balance tự sinh interest proportional với hiện tại (current / 현재) balance:

```math
B'(t)=rB(t),
```

solution exponential:

```math
B(t)=B_0e^{rt}.
```

Tỷ lệ (rate / 비율) law quyết định accumulation shape.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **9. Finance: balance là accumulated cash luồng (flow / 흐름)** xác định đầu vào; **10. Marginal vs total trong economics** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **11. độ dốc (gradient / 기울기) là véc-tơ (vector / 벡터) của cục bộ (local / 로컬) rates** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Marginal vs total trong economics

Nếu total chi phí (cost / 비용) là `C(q)`, marginal chi phí (cost / 비용):

```math
C'(q)
```

là cục bộ (local / 로컬) chi phí (cost / 비용) của thêm một đơn vị (unit / 단위) môi trường vận hành (production / 운영 환경).

Net total thay đổi (change / 변경) từ `q_1` tới `q_2`:

```math
C(q_2)-C(q_1)
=\int_{q_1}^{q_2}C'(q)dq.
```

Mistake phổ biến là đọc marginal quantity như average hoặc total quantity.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **11. độ dốc (gradient / 기울기) là véc-tơ (vector / 벡터) của cục bộ (local / 로컬) rates** tiếp nhận điểm tựa từ **10. Marginal vs total trong economics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. độ dốc (gradient / 기울기) descent là tích lũy các cục bộ (local / 로컬) decisions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. độ dốc (gradient / 기울기) là véc-tơ (vector / 벡터) của cục bộ (local / 로컬) rates

Với multivariable hàm (function / 함수):

```math
L(\theta_1,\ldots,\theta_n),
```

Độ dốc (gradient / 기울기):

```math
\nabla L=
\begin{bmatrix}
\partial L/\partial\theta_1\\
\vdots\\
\partial L/\partial\theta_n
\end{bmatrix}
```

collect cục bộ (local / 로컬) sensitivities.

Directional derivative:

```math
D_uL=\nabla L\cdot u.
```

nói mất mát (loss / 손실) thay đổi nhanh thế nào nếu parameters move theo direction `u`.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **12. độ dốc (gradient / 기울기) descent là tích lũy các cục bộ (local / 로컬) decisions** tiếp nhận điểm tựa từ **11. độ dốc (gradient / 기울기) là véc-tơ (vector / 벡터) của cục bộ (local / 로컬) rates** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Differential equation: biết law của thay đổi (change / 변경), reconstruct trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. độ dốc (gradient / 기울기) descent là tích lũy các cục bộ (local / 로컬) decisions

Cập nhật (update / 업데이트):

```math
\theta_{k+1}=\theta_k-\eta\nabla L(\theta_k)
```

là discrete trajectory.

Mỗi step dùng cục bộ (local / 로컬) tỷ lệ (rate / 비율) thông tin (information / 정보); toàn bộ huấn luyện (training / 학습) đường dẫn (path / 경로) là accumulated kết quả (result / 결과) của many cục bộ (local / 로컬) updates.

Trong limit step nhỏ, ta gặp độ dốc (gradient / 기울기) luồng (flow / 흐름):

```math
\frac{d\theta}{dt}=-\nabla L(\theta).
```

Tối ưu hóa (optimization / 최적화) nối recurrence với differential equations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **13. Differential equation: biết law của thay đổi (change / 변경), reconstruct trạng thái (state / 상태)** tiếp nhận điểm tựa từ **12. độ dốc (gradient / 기울기) descent là tích lũy các cục bộ (local / 로컬) decisions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Conservation law là accounting ở cấp trường dữ liệu (field / 필드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Differential equation: biết law của thay đổi (change / 변경), reconstruct trạng thái (state / 상태)

ODE:

```math
x'=F(x,t)
```

không cho trạng thái (state / 상태) trực tiếp. Nó cho **law of thay đổi (change / 변경)**.

Solving ODE nghĩa reconstruct trajectory consistent với cục bộ (local / 로컬) law + initial điều kiện (condition / 조건).

PDE mở rộng idea này sang trường dữ liệu (field / 필드):

```text
local law at every point
→ global field evolution
```

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **13. Differential equation: biết law của thay đổi (change / 변경), reconstruct trạng thái (state / 상태)** nêu điều cần giải thích; **14. Conservation law là accounting ở cấp trường dữ liệu (field / 필드)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Local-to-global là mẫu (pattern / 패턴) lớn hơn calculus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Conservation law là accounting ở cấp trường dữ liệu (field / 필드)

Nếu density `ρ(x,t)` và flux `J(x,t)` satisfy:

```math
\frac{\partial \rho}{\partial t}
+\nabla\cdot J=0,
```

thì cục bộ (local / 로컬) density chỉ thay đổi vì luồng (flow / 흐름) đi vào/ra.

Integrate over region `V`:

```math
\frac{d}{dt}\int_V\rho\,dV
=-\int_{\partial V}J\cdot n\,dS.
```

Accumulated amount bên trong thay đổi bằng net ranh giới (boundary / 경계) luồng (flow / 흐름).

Đây là continuous accounting principle nằm dưới mass, charge, xác suất (probability / 확률) và fluid conservation.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **14. Conservation law là accounting ở cấp trường dữ liệu (field / 필드)** nêu điều cần giải thích; **15. Local-to-global là mẫu (pattern / 패턴) lớn hơn calculus** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Units như sanity check** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Local-to-global là mẫu (pattern / 패턴) lớn hơn calculus

Nhiều theorem có cấu trúc (structure / 구조):

```text
local quantity
→ integrate/sum
→ global statement
```

Ví dụ:

```text
derivative → net change
curl → circulation
ndivergence → flux
local loss → empirical risk
per-step cost → total dynamic-programming cost
```

Nhận ra mẫu (pattern / 패턴) này giúp transfer intuition giữa domains.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **16. Units như sanity check** tiếp nhận điểm tựa từ **15. Local-to-global là mẫu (pattern / 패턴) lớn hơn calculus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Continuous mô hình (model / 모델) là approximation của discrete reality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Units như sanity check

Nếu tỷ lệ (rate / 비율) có units:

```text
requests / second
```

integrating over seconds phải cho:

```text
requests
```

Nếu derivative:

```math
\frac{dB}{dt}
```

có units KRW/day thì multiplying by a thời gian (time / 시간) interval cho KRW.

Dimensional phân tích (analysis / 분석) thường bắt được confusion giữa trạng thái (state / 상태) và tỷ lệ (rate / 비율) trước cả algebra.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **17. Continuous mô hình (model / 모델) là approximation của discrete reality** tiếp nhận điểm tựa từ **16. Units như sanity check** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. dùng chung (common / 공통) thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Continuous mô hình (model / 모델) là approximation của discrete reality

People, packets và cơ sở dữ liệu (database / 데이터베이스) rows là discrete.

Derivative mô hình (model / 모델) có thể hữu ích khi quy mô (scale / 규모) lớn và changes smooth enough, nhưng chính xác (exact / 정확한) microscopic tiến trình (process / 프로세스) vẫn discrete.

Ví dụ average yêu cầu (request / 요청) tỷ lệ (rate / 비율) 1000 req/s không nghĩa mỗi millisecond có đúng 1 yêu cầu (request / 요청).

Continuous approximation smooths randomness và granularity.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **18. dùng chung (common / 공통) thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **17. Continuous mô hình (model / 모델) là approximation của discrete reality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. dùng chung (common / 공통) thất bại (failure / 실패) modes

### Endpoint-only thinking

Average tỷ lệ (rate / 비율) giữa hai endpoints không reveal spikes bên trong interval.

### Confusing signed and absolute accumulation

Net thay đổi (change / 변경) có cancellation; total activity có thể không.

### Treating derivative as toàn cục (global / 전역) trend

Cục bộ (local / 로컬) derivative tại một điểm (point / 지점) không đảm bảo same slope far away.

### Ignoring trạng thái (state / 상태) dependence

Tỷ lệ (rate / 비율) có thể depend on trạng thái (state / 상태), tạo nonlinear phản hồi (feedback / 피드백).

### Integrating a wrong mô hình (model / 모델)

Precise accumulation của wrong tỷ lệ (rate / 비율) law vẫn cho wrong kết quả (result / 결과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **Liên kết kiến thức (knowledge connection / 지식 연결)** tiếp nhận điểm tựa từ **18. dùng chung (common / 공통) thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối cho thấy rate và accumulation xuất hiện trong physics, finance, population và software metrics. Cùng một cặp derivative–integral có thể mô tả những hệ khác nhau nếu xác định đúng state và time scale.

```text
Algebra      → finite difference
Calculus     → derivative/integral
Probability  → density/CDF
Optimization → gradient/update trajectory
ODE/PDE      → local law → global state
Finance      → cash flow → balance
Systems      → throughput → queue/backlog
Physics      → velocity/flux → conserved quantity
```

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — tỷ lệ (rate / 비율), thay đổi (change / 변경) và Accumulation: từ difference đến conservation**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Mỗi khi gặp một quantity, hỏi: đây là state, local rate hay accumulated total? Nếu biết state, derivative/difference nói nó đang đổi thế nào. Nếu biết rate, sum/integral reconstruct net accumulation. Rất nhiều công thức khác domain chỉ là cùng accounting structure dưới notation khác nhau.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
