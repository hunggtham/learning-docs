# Mô hình tuyến tính và bậc hai: từ constant tỷ lệ (rate / 비율) đến curvature

> **Mạch đọc:** Đọc **Mô hình tuyến tính và bậc hai: từ constant tỷ lệ (rate / 비율) đến curvature** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. mô hình tuyến tính (linear model / 선형 모델) bắt đầu từ constant tỷ lệ (rate / 비율) of thay đổi (change / 변경)** sang **2. Vì sao constant slope tạo đường thẳng?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tuyến tính (linear / 선형) và quadratic functions là hai families đầu tiên nên học thật sâu vì chúng tạo mô hình tư duy (mental model / 사고 모델) cho phần lớn calculus sau này.

Mô hình tuyến tính (linear model / 선형 모델) trả lời:

> Nếu đầu vào (input / 입력) tăng một lượng cố định, đầu ra (output / 출력) có thay đổi gần như cùng một lượng cố định không?

Quadratic mô hình (model / 모델) trả lời:

> Nếu bản thân tỷ lệ (rate / 비율) of thay đổi (change / 변경) đang thay đổi gần tuyến tính, shape của đầu ra (output / 출력) sẽ ra sao?

Đây không chỉ là hai đồ thị (graph / 그래프) cần nhớ. Chúng là hai mức cấu trúc (structure / 구조) khác nhau của thay đổi (change / 변경).

## 1. mô hình tuyến tính (linear model / 선형 모델) bắt đầu từ constant tỷ lệ (rate / 비율) of thay đổi (change / 변경)

Một affine hàm (function / 함수) một biến có dạng

```math
y=mx+b.
```

Trong school algebra thường gọi đây là tuyến tính (linear / 선형) hàm (function / 함수). Trong tuyến tính (linear / 선형) algebra nghiêm ngặt, `mx+b` với `b\ne0` là affine; tuyến tính (linear / 선형) map phải giữ origin và có dạng `y=mx`.

`m` là slope (기울기 / slope):

```math
m=\frac{\Delta y}{\Delta x}.
```

Điểm quan trọng không phải công thức mà là meaning:

```text
m = output change per input unit
```

Nếu `y` là KRW và `x` là GB:

```text
m unit = KRW/GB
```

Slope vì vậy là tỷ lệ (rate / 비율), không chỉ là “độ nghiêng của line”.

## 2. Vì sao constant slope tạo đường thẳng?

Nếu mọi increment `\Delta x` tạo cùng đầu ra (output / 출력) increment

```math
\Delta y=m\Delta x,
```

thì bắt đầu từ tham chiếu (reference / 참조) điểm (point / 지점) `(x_0,y_0)`:

```math
y-y_0=m(x-x_0).
```

Đó là point-slope equation.

Chọn `x_0=0`, đặt `b=y_0`:

```math
y=mx+b.
```

Vì vậy line equation không phải arbitrary cú pháp (syntax / 문법). Nó là consequence của giả định (assumption / 가정) **constant tỷ lệ (rate / 비율) of thay đổi (change / 변경)**.

## 3. Intercept là baseline, nhưng chỉ khi baseline có meaning

Trong

```math
y=mx+b,
```

`b` là predicted đầu ra (output / 출력) tại `x=0`.

Nhưng mathematical intercept không tự động có real-world meaning.

Ví dụ fit salary theo years of experience trên phạm vi (range / 범위) 3–15 years. Intercept tại 0 years có thể là extrapolation ngoài dữ liệu (data / 데이터) và không nên diễn giải mạnh.

Do đó khi đọc parameter:

```text
coefficient meaning = formula + domain + model assumptions
```

## 4. Worked example: fixed chi phí (cost / 비용) + variable chi phí (cost / 비용)

Cloud dịch vụ (service / 서비스):

```text
fixed fee = 30,000 KRW/month
variable fee = 20 KRW/GB
```

Mô hình (model / 모델):

```math
C(x)=20x+30000.
```

Slope:

```text
20 KRW/GB
```

là marginal tỷ lệ (rate / 비율) trong mô hình (model / 모델).

Intercept:

```text
30,000 KRW
```

là baseline tại zero usage nếu pricing quy tắc (rule / 규칙) thực sự áp dụng ở zero.

Nếu pricing có tiers, hàm (function / 함수) trở thành piecewise tuyến tính (linear / 선형) chứ không còn một line duy nhất.

## 5. Proportionality là special trường hợp (case / 사례) của tuyến tính (linear / 선형)/affine hành vi (behavior / 동작)

Direct proportionality:

```math
y=kx
```

đi qua origin.

Nếu `x=0` thì `y=0`. Đây là stronger giả định (assumption / 가정) so với affine mô hình (model / 모델) `mx+b`.

Ví dụ chi phí (cost / 비용) proportional với quantity chỉ hợp lý nếu không có fixed fee.

Rất nhiều lỗi modeling đến từ việc dùng proportionality khi thực tế có baseline.

## 6. Interpolation và extrapolation khác nhau về giả định (assumption / 가정) rủi ro (risk / 위험)

Interpolation dự đoán trong observed phạm vi (range / 범위).

Extrapolation dự đoán ngoài phạm vi (range / 범위).

Nếu dữ liệu (data / 데이터) từ `x=10` đến `x=20`, prediction tại `x=15` dựa vào giả định (assumption / 가정) cục bộ (local / 로컬). Prediction tại `x=1000` yêu cầu giả định (assumption / 가정) constant slope tồn tại xa ngoài bằng chứng (evidence / 증거).

Một line có thể fit tốt trong narrow region của một nonlinear tiến trình (process / 프로세스).

Đây là cầu nối (bridge / 브리지) sang Taylor approximation: nonlinear functions thường gần tuyến tính (linear / 선형) locally dù toàn cục (global / 전역) hành vi (behavior / 동작) khác hẳn.

## 7. Residual cho biết mô hình (model / 모델) bỏ sót cấu trúc (structure / 구조) nào

Observed giá trị (value / 값) `y_i`, prediction `\hat y_i`:

```math
r_i=y_i-\hat y_i.
```

Nếu residuals random quanh zero, line có thể capture mean cấu trúc (structure / 구조) khá tốt.

Nếu residuals tạo curve:

```text
positive → negative → positive
```

đó là dấu hiệu mô hình tuyến tính (linear model / 선형 모델) đang bỏ sót curvature.

Residual không chỉ là “lỗi (error / 오류) cần nhỏ”; mẫu (pattern / 패턴) của residual là diagnostic tín hiệu (signal / 신호).

## 8. Quadratic mô hình (model / 모델) xuất hiện khi first-order tỷ lệ (rate / 비율) không constant

Quadratic hàm (function / 함수):

```math
y=ax^2+bx+c,
\qquad a\ne0.
```

Derivative:

```math
y'=2ax+b.
```

Slope thay đổi tuyến tính theo `x`.

Second derivative:

```math
y''=2a
```

constant.

Vì vậy một mô hình tư duy (mental model / 사고 모델) rất mạnh là:

```text
linear function       → constant first derivative
quadratic function    → constant second derivative
```

Đây là lý do quadratic xuất hiện trong constant acceleration, cục bộ (local / 로컬) curvature và second-order tối ưu hóa (optimization / 최적화).

## 9. Physics derivation: constant acceleration tạo quadratic position

Nếu acceleration constant `a`:

```math
v(t)=v_0+at.
```

Position accumulation:

```math
x(t)=x_0+\int_0^t v(s)\,ds
```

nên

```math
x(t)=x_0+v_0t+\frac12at^2.
```

Quadratic không xuất hiện vì “projectile formula phải nhớ”. Nó xuất hiện vì tích phân của tuyến tính (linear / 선형) velocity là quadratic position.

## 10. Ba representations của quadratic trả lời ba câu hỏi khác nhau

Expanded form:

```math
f(x)=ax^2+bx+c
```

làm coefficients rõ.

Factored form:

```math
f(x)=a(x-r_1)(x-r_2)
```

làm roots rõ.

Vertex form:

```math
f(x)=a(x-h)^2+k
```

làm extremum và symmetry rõ.

Không có biểu diễn (representation / 표현) “tốt nhất” universal. Good algebra thường là chọn biểu diễn (representation / 표현) phù hợp question.

## 11. Completing the square là đổi biểu diễn (representation / 표현), không phải trick

Từ

```math
ax^2+bx+c,
```

factor `a` khỏi quadratic terms:

```math
=a\left(x^2+\frac ba x\right)+c.
```

Thêm/bớt square:

```math
x^2+\frac ba x
=
\left(x+\frac{b}{2a}\right)^2
-
\frac{b^2}{4a^2}.
```

Do đó

```math
f(x)=
a\left(x+\frac{b}{2a}\right)^2
+
\left(c-\frac{b^2}{4a}\right).
```

Vertex:

```math
h=-\frac{b}{2a}.
```

Điểm này cũng là nơi derivative bằng zero:

```math
2ax+b=0.
```

Algebra và calculus đang nói cùng một cấu trúc (structure / 구조) bằng hai ngôn ngữ.

## 12. Discriminant encode gốc (root / 루트) hình học (geometry / 기하학)

Quadratic equation:

```math
ax^2+bx+c=0.
```

Discriminant:

```math
\Delta=b^2-4ac.
```

Nếu `\Delta>0`: hai real roots.

Nếu `\Delta=0`: tangent touch, repeated gốc (root / 루트).

Nếu `\Delta<0`: no real roots, nhưng có complex conjugate roots.

Discriminant vì vậy không chỉ là symbol trong formula; nó tóm tắt intersection hình học (geometry / 기하학) của parabola với x-axis.

## 13. Quadratic as cục bộ (local / 로컬) approximation

Gần `x_0`, smooth hàm (function / 함수) có Taylor approximation:

```math
f(x_0+h)
\approx
f(x_0)
+f'(x_0)h
+\frac12f''(x_0)h^2.
```

Tuyến tính (linear / 선형) term mô tả slope; quadratic term mô tả curvature.

Tối ưu hóa (optimization / 최적화) methods như Newton's phương thức (method / 메서드) và second-order các mô hình (models / 모델들) dùng đúng viewpoint này.

Một quadratic mô hình (model / 모델) không chỉ là school hàm (function / 함수) family; nó là universal cục bộ (local / 로컬) mô hình (model / 모델) cấp hai cho smooth functions.

## 14. Multivariable quadratic form

Trong nhiều dimensions, quadratic cấu trúc (structure / 구조) viết:

```math
q(x)=x^TAx+b^Tx+c.
```

Ma trận (matrix / 행렬) `A` encode curvature.

Nếu `A` positive definite, bowl shape có unique minimum.

Đây là cầu nối (bridge / 브리지) sang Hessian, least squares, tối ưu hóa (optimization / 최적화) và Gaussian các mô hình (models / 모델들).

## 15. tuyến tính (linear / 선형) regression vs chính xác (exact / 정확한) line through points

Hai points với different x xác định một chính xác (exact / 정확한) line.

Nhưng noisy dữ liệu (data / 데이터) nhiều points thường không nằm trên một line. Khi đó regression solve:

```math
\min_{m,b}
\sum_i
(y_i-(mx_i+b))^2.
```

Đây là projection bài toán (problem / 문제), không phải interpolation.

Distinction:

```text
interpolation → pass through selected data exactly
regression → estimate underlying relationship under noise
```

## 16. Quadratic fitting và overfitting intuition

Thêm degree cho polynomial làm mô hình (model / 모델) flexible hơn. huấn luyện (training / 학습) residual có thể giảm, nhưng generalization không chắc tốt hơn.

Với few noisy samples, quadratic có thể fit apparent curvature chỉ do noise.

Mô hình (model / 모델) choice cần:

```text
structure + data + validation
```

không chỉ “higher degree fits better”.

## 17. Worked example: braking distance

Nếu reaction distance quy mô (scale / 규모) roughly tuyến tính (linear / 선형) với speed `v`:

```math
d_r\propto v,
```

còn braking distance dưới simplified constant deceleration mô hình (model / 모델) quy mô (scale / 규모) như

```math
d_b\propto v^2,
```

thì total stopping distance có form gần

```math
d(v)=av+bv^2.
```

Doubling speed không chỉ double stopping distance vì quadratic term tăng factor 4.

Đây là example tốt cho việc hiểu mô hình (model / 모델) terms bằng scaling.

## 18. Finance liên kết (connection / 연결): cục bộ (local / 로컬) tuyến tính (linear / 선형) vs convex exposure

Một portfolio giá trị (value / 값) có thể cục bộ (local / 로컬) approximate theo price thay đổi (change / 변경):

```math
\Delta V\approx \Delta\,\Delta S
```

(first-order sensitivity).

Với nonlinear instruments, second-order term:

```math
\Delta V
\approx
\Delta\,\Delta S
+
\frac12\Gamma(\Delta S)^2
```

cho curvature exposure.

Không cần học option pricing ở chapter này; important liên kết (connection / 연결) là tuyến tính (linear / 선형) + quadratic terms tạo cục bộ (local / 로컬) sensitivity mô hình (model / 모델).

## 19. AI liên kết (connection / 연결): tuyến tính (linear / 선형) tầng (layer / 계층) nhưng nonlinear mô hình (model / 모델)

Một tầng (layer / 계층) thường viết:

```math
z=Wx+b.
```

đây là affine transformation.

Nếu chỉ compose affine layers mà không activation nonlinear, toàn mạng (network / 네트워크) vẫn collapse thành một affine transformation.

Nonlinearity là thứ tạo richer hàm (function / 함수) family.

Điều này cho thấy mô hình tuyến tính (linear model / 선형 모델) là building khối (block / 블록) nhưng không đủ cho arbitrary nonlinear cấu trúc (structure / 구조).

## 20. các giả định (assumptions / 가정들) checklist

Khi dùng mô hình tuyến tính (linear model / 선형 모델), hỏi:

```text
rate có thực sự gần constant không?
intercept có meaning không?
range nào model valid?
residual có pattern không?
extrapolation có hợp lý không?
```

Khi dùng quadratic mô hình (model / 모델), hỏi thêm:

```text
curvature có gần constant không?
quadratic behavior là global hay chỉ local?
vertex/root có nằm trong domain meaningful không?
```

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tuyến tính (linear / 선형)/quadratic các mô hình (models / 모델들) nối:

```text
ratio/rate
→ functions
→ derivatives
→ Taylor approximation
→ least squares
→ optimization
→ physics motion
→ AI affine layers
→ Finance sensitivity
```

## Mô hình tư duy (mental model / 사고 모델)

> mô hình tuyến tính (linear model / 선형 모델) là **constant first-order thay đổi (change / 변경)**. Quadratic mô hình (model / 모델) là **constant second-order thay đổi (change / 변경)** hoặc **first-order tỷ lệ (rate / 비율) thay đổi tuyến tính**. Đừng bắt đầu từ đồ thị (graph / 그래프) shape; bắt đầu từ cấu trúc (structure / 구조) của thay đổi (change / 변경) mà mô hình (model / 모델) đang giả định.

## Dùng chung (common / 공통) Misconceptions

`y=mx+b` không phải tuyến tính (linear / 선형) map theo definition tuyến tính (linear / 선형) algebra nếu `b\ne0`. High `R^2` không chứng minh relationship truly tuyến tính (linear / 선형) hoặc nhân quả (causal / 인과적). Vertex formula không phải mẹo; nó là nơi first derivative bằng zero. Quadratic fit tốt trong mẫu (sample / 표본) không có nghĩa tiến trình (process / 프로세스) thật sự quadratic ngoài phạm vi (range / 범위). Một đồ thị (graph / 그래프) nhìn thẳng trên narrow interval có thể chỉ là cục bộ (local / 로컬) linearization của nonlinear hàm (function / 함수).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 function concept](./00_function_concept.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
