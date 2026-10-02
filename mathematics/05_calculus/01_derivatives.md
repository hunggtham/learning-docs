# Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Ba cách nhìn cần giữ cùng lúc** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Derive x^2 từ nguyên lý nền tảng (first principles / 제일 원리)** để chuyển câu hỏi ấy thành điều kiện phải giữ. Mạch này nối đạo hàm với tốc độ thay đổi, tuyến tính hóa và tối ưu, giúp đọc hình học của hàm qua thông tin cục bộ.

Đạo hàm (derivative / 미분계수, 도함수) không nên được học như một bảng công thức differentiation. Nó xuất hiện vì ta cần mô tả **tốc độ thay đổi tại một trạng thái cụ thể**, trong khi phép chia hữu hạn chỉ cho average thay đổi (change / 변경) trên một interval.

Nếu position của một đối tượng (object / 객체) là `s(t)`, average velocity từ `t` đến `t+h` là

```math
\frac{s(t+h)-s(t)}{h}.
```

Nhưng câu hỏi vật lý “velocity ngay tại thời điểm `t` là bao nhiêu?” không thể được trả lời bằng cách đơn giản đặt `h=0`, vì khi đó mẫu số bằng zero. Calculus giải quyết bằng limit:

```math
s'(t)=\lim_{h\to0}\frac{s(t+h)-s(t)}{h}.
```

Ta không chia cho zero. Ta nghiên cứu hành vi (behavior / 동작) của average tỷ lệ (rate / 비율) khi interval trở nên arbitrarily small.

## Ba cách nhìn cần giữ cùng lúc

Derivative có ba interpretation tương đương nhưng hữu ích trong các ngữ cảnh (context / 맥락) khác nhau.

**Slope viewpoint:** derivative là slope của tangent line.

**tỷ lệ (rate / 비율) viewpoint:** derivative là đầu ra (output / 출력) thay đổi (change / 변경) trên một đơn vị (unit / 단위) đầu vào (input / 입력) thay đổi (change / 변경), ở cục bộ (local / 로컬) quy mô (scale / 규모).

**Linearization viewpoint:** derivative là coefficient của best first-order tuyến tính (linear / 선형) approximation:

```math
f(x+\Delta x)
\approx
f(x)+f'(x)\Delta x.
```

Cách nhìn thứ ba là sâu nhất để nối sang multivariable calculus, tối ưu hóa (optimization / 최적화), numerical methods và machine học tập (learning / 학습).

> **Chuyển mạch:** Trong **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Derive x^2 từ nguyên lý nền tảng (first principles / 제일 원리)** tiếp nhận điểm tựa từ **Ba cách nhìn cần giữ cùng lúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao power quy tắc (rule / 규칙) có dạng nx^{n-1}?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Derive `x^2` từ nguyên lý nền tảng (first principles / 제일 원리)

Với

```math
f(x)=x^2,
```

ta có

```math
f'(x)
=
\lim_{h\to0}\frac{(x+h)^2-x^2}{h}.
```

Khai triển:

```math
=
\lim_{h\to0}\frac{2xh+h^2}{h}.
```

Trong quá trình limit, `h\neq0`, nên có thể factor/cancel:

```math
=
\lim_{h\to0}(2x+h)=2x.
```

Formula `2x` không phải magic quy tắc (rule / 규칙). Nó nói parabola có cục bộ (local / 로컬) slope tăng tuyến tính theo position.

> **Chuyển mạch:** Ở chặng này của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Vì sao power quy tắc (rule / 규칙) có dạng nx^{n-1}?** tiếp nhận điểm tựa từ **Derive x^2 từ nguyên lý nền tảng (first principles / 제일 원리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Units: derivative luôn là một tỷ lệ (rate / 비율)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao power quy tắc (rule / 규칙) có dạng `nx^{n-1}`?

Với positive integer `n`, binomial expansion cho

```math
(x+h)^n
=
x^n+n x^{n-1}h+\text{terms chứa }h^2,h^3,\ldots
```

Difference quotient:

```math
\frac{(x+h)^n-x^n}{h}
=
nx^{n-1}+\text{terms vẫn chứa }h.
```

Khi `h\to0`, các higher-order terms vanish, còn lại

```math
\frac{d}{dx}x^n=nx^{n-1}.
```

Đây cũng preview một idea lớn: derivative giữ lại **first-order term** và bỏ những effects nhỏ hơn theo thứ tự (order / 순서) của `h`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Units: derivative luôn là một tỷ lệ (rate / 비율)** tiếp nhận điểm tựa từ **Vì sao power quy tắc (rule / 규칙) có dạng nx^{n-1}?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sản phẩm (product / 제품) quy tắc (rule / 규칙): khi hai factors cùng thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Units: derivative luôn là một tỷ lệ (rate / 비율)

Nếu distance đo bằng meters và thời gian (time / 시간) bằng seconds:

```math
\frac{ds}{dt}
```

có đơn vị (unit / 단위) m/s.

Nếu revenue `R(q)` đo bằng dollars và quantity `q` là units sold:

```math
R'(q)
```

có đơn vị (unit / 단위) dollars per additional đơn vị (unit / 단위) quanh hiện tại (current / 현재) operating điểm (point / 지점).

Units là sanity check mạnh. Nếu derivative có đơn vị (unit / 단위) vô lý, mô hình (model / 모델) hoặc manipulation có thể sai.

> **Chuyển mạch:** Trong **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Sản phẩm (product / 제품) quy tắc (rule / 규칙): khi hai factors cùng thay đổi** tiếp nhận điểm tựa từ **Units: derivative luôn là một tỷ lệ (rate / 비율)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi (chain / 사슬) quy tắc (rule / 규칙): sensitivity đi qua một chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sản phẩm (product / 제품) quy tắc (rule / 규칙): khi hai factors cùng thay đổi

Cho

```math
y=u(x)v(x).
```

Nếu cả hai thay đổi một chút:

```math
(u+\Delta u)(v+\Delta v)-uv
=u\Delta v+v\Delta u+\Delta u\Delta v.
```

Chia cho `\Delta x`. Trong limit, term cuối là second thứ tự (order / 순서) và vanish dưới smoothness phù hợp. Ta nhận

```math
(uv)'=u'v+uv'.
```

Meaning: total first-order thay đổi (change / 변경) là contribution từ `u` thay đổi khi `v` tạm fixed, cộng contribution từ `v` thay đổi khi `u` tạm fixed.

> **Chuyển mạch:** Ở chặng này của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Sản phẩm (product / 제품) quy tắc (rule / 규칙): khi hai factors cùng thay đổi** xác định đầu vào; **Chuỗi (chain / 사슬) quy tắc (rule / 규칙): sensitivity đi qua một chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Worked example — sensitivity qua một composed mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (chain / 사슬) quy tắc (rule / 규칙): sensitivity đi qua một chuỗi xử lý (pipeline / 파이프라인)

Nếu

```math
y=f(g(x)),
```

thì

```math
\frac{dy}{dx}
=
\frac{dy}{dg}\frac{dg}{dx}
=
f'(g(x))g'(x).
```

Interpretation bằng units rất tự nhiên:

```text
output per g-unit × g-unit per x-unit = output per x-unit.
```

Nếu temperature ảnh hưởng pressure, pressure ảnh hưởng sensor voltage, chuỗi (chain / 사슬) quy tắc (rule / 규칙) đo sensitivity của voltage đối với temperature bằng cách multiply cục bộ (local / 로컬) sensitivities qua chuỗi xử lý (pipeline / 파이프라인).

Backpropagation trong neural networks chính là chuỗi (chain / 사슬) quy tắc (rule / 규칙) được tổ chức efficient trên computational đồ thị (graph / 그래프).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, sau khi thấy quy trình trong **Chuỗi (chain / 사슬) quy tắc (rule / 규칙): sensitivity đi qua một chuỗi xử lý (pipeline / 파이프라인)**, **Worked example — sensitivity qua một composed mô hình (model / 모델)** đặt nó vào một trường hợp đủ cụ thể để nhận ra điều kiện thành công và chỗ dễ sai. Từ đây, **Exponential và logarithm: những derivatives có cấu trúc (structure / 구조) đặc biệt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Worked example — sensitivity qua một composed mô hình (model / 모델)

Giả sử

```math
g(x)=x^2+1,
```

và

```math
f(u)=\ln u.
```

Then

```math
y=\ln(x^2+1).
```

Ta có

```math
\frac{dy}{du}=\frac1u,
\qquad
\frac{du}{dx}=2x.
```

Nên

```math
y'(x)=\frac{2x}{x^2+1}.
```

Tại `x=2`:

```math
y'(2)=\frac45.
```

Nếu `x` tăng khoảng `0.01`, đầu ra (output / 출력) tăng xấp xỉ

```math
\Delta y\approx \frac45\cdot0.01=0.008.
```

Derivative đã trở thành cục bộ (local / 로컬) prediction công cụ (tool / 도구).

> **Chuyển mạch:** Trong **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Worked example — sensitivity qua một composed mô hình (model / 모델)** cho ta quy tắc; **Exponential và logarithm: những derivatives có cấu trúc (structure / 구조) đặc biệt** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trigonometric derivatives và vì sao radians quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exponential và logarithm: những derivatives có cấu trúc (structure / 구조) đặc biệt

Hàm (function / 함수) `e^x` thỏa

```math
\frac{d}{dx}e^x=e^x.
```

Nó là eigenfunction của differentiation operator: derivative không đổi shape, chỉ quy mô (scale / 규모) factor bằng 1. Đây là lý do exponential xuất hiện tự nhiên trong các hệ thống (systems / 시스템들) nơi growth tỷ lệ (rate / 비율) proportional trạng thái hiện tại (current state / 현재 상태).

Logarithm có

```math
\frac{d}{dx}\ln x=\frac1x,
```

nên equal relative changes có cấu trúc (structure / 구조) đơn giản trong log coordinates.

> **Chuyển mạch:** Ở chặng này của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Trigonometric derivatives và vì sao radians quan trọng** tiếp nhận điểm tựa từ **Exponential và logarithm: những derivatives có cấu trúc (structure / 구조) đặc biệt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Implicit differentiation: relationship không cần solve tường minh (explicit / 명시적) trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trigonometric derivatives và vì sao radians quan trọng

Với radians:

```math
\frac{d}{dx}\sin x=\cos x,
```

```math
\frac{d}{dx}\cos x=-\sin x.
```

Nếu đo bằng degrees, extra conversion factor xuất hiện. Radian không chỉ là convention; nó làm angle bằng arc-length/radius, khiến cục bộ (local / 로컬) hình học (geometry / 기하학) của circle phù hợp tự nhiên với calculus.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Implicit differentiation: relationship không cần solve tường minh (explicit / 명시적) trước** tiếp nhận điểm tựa từ **Trigonometric derivatives và vì sao radians quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Derivative như lan truyền lỗi (error propagation / 오류 전파)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Implicit differentiation: relationship không cần solve tường minh (explicit / 명시적) trước

Circle

```math
x^2+y^2=r^2
```

không phải toàn cục (global / 전역) hàm (function / 함수) `y=f(x)` nếu giữ cả hai halves, nhưng locally ta vẫn tìm slope.

Differentiate theo `x`:

```math
2x+2y\frac{dy}{dx}=0,
```

nên

```math
\frac{dy}{dx}=-\frac{x}{y}.
```

Term `dy/dx` xuất hiện vì `y` itself changes with `x` along the ràng buộc (constraint / 제약조건) curve.

> **Chuyển mạch:** Trong **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Derivative như lan truyền lỗi (error propagation / 오류 전파)** tiếp nhận điểm tựa từ **Implicit differentiation: relationship không cần solve tường minh (explicit / 명시적) trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Relative sensitivity và elasticity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Derivative như lan truyền lỗi (error propagation / 오류 전파)

Nếu đo lường (measurement / 측정) `x` có small lỗi (error / 오류) `\Delta x`, thì

```math
\Delta y
\approx
f'(x)\Delta x.
```

Derivative magnitude cho cục bộ (local / 로컬) lỗi (error / 오류) amplification.

Ví dụ `y=x^2`, tại `x=100`, derivative là 200. lỗi (error / 오류) `0.01` trong `x` tạo khoảng `2` units lỗi (error / 오류) trong `y`. Same đầu vào (input / 입력) lỗi (error / 오류) ở `x=1` chỉ tạo khoảng `0.02`.

Sensitivity phụ thuộc operating điểm (point / 지점).

> **Chuyển mạch:** Ở chặng này của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Relative sensitivity và elasticity** tiếp nhận điểm tựa từ **Derivative như lan truyền lỗi (error propagation / 오류 전파)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differentiability mạnh hơn continuity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Relative sensitivity và elasticity

Absolute derivative phụ thuộc units. Dimensionless sensitivity thường dùng elasticity:

```math
E(x)=\frac{x}{f(x)}f'(x).
```

Nó xấp xỉ percentage đầu ra (output / 출력) thay đổi (change / 변경) trên percentage đầu vào (input / 입력) thay đổi (change / 변경).

Nếu

```math
f(x)=x^k,
```

thì

```math
E(x)=k.
```

Power-law exponent chính là elasticity constant.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Differentiability mạnh hơn continuity** tiếp nhận điểm tựa từ **Relative sensitivity và elasticity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi derivative không tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differentiability mạnh hơn continuity

Nếu hàm (function / 함수) differentiable tại `a`, nó continuous tại `a`. Nhưng converse sai.

`|x|` continuous tại 0 nhưng left derivative là `-1`, right derivative là `1`; không có single cục bộ (local / 로컬) tuyến tính (linear / 선형) approximation nên derivative không tồn tại.

Điều này cho thấy derivative không chỉ hỏi “đồ thị (graph / 그래프) có đứt không?” mà hỏi “zoom đủ gần có thấy một line duy nhất không?”.

> **Chuyển mạch:** Trong **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Khi derivative không tồn tại** tiếp nhận điểm tựa từ **Differentiability mạnh hơn continuity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Numerical differentiation khác symbolic derivative** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi derivative không tồn tại

Các dùng chung (common / 공통) reasons:

- jump/discontinuity;
- corner như `|x|`;
- cusp;
- vertical tangent;
- highly oscillatory hành vi (behavior / 동작).

Không nên force symbolic rules ở điểm (point / 지점) nơi các giả định (assumptions / 가정들) của differentiability thất bại (fail / 실패).

> **Chuyển mạch:** Ở chặng này của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Numerical differentiation khác symbolic derivative** tiếp nhận điểm tựa từ **Khi derivative không tồn tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Physics, AI và Finance connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Numerical differentiation khác symbolic derivative

Máy tính có thể approximate

```math
f'(x)\approx \frac{f(x+h)-f(x)}{h}.
```

Nhưng `h` quá lớn gây truncation lỗi (error / 오류); `h` quá nhỏ gây cancellation/rounding lỗi (error / 오류). Mathematical derivative là limit ideal; finite-difference hiện thực (implementation / 구현) là numerical approximation.

Automatic differentiation lại khác cả hai: nó áp dụng chuỗi (chain / 사슬) quy tắc (rule / 규칙) chính xác ở machine arithmetic lên computation đồ thị (graph / 그래프), không xấp xỉ derivative bằng finite differences.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Physics, AI và Finance connections** tiếp nhận điểm tựa từ **Numerical differentiation khác symbolic derivative** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Physics, AI và Finance connections

Trong physics, derivative tạo velocity, acceleration, force laws và trường dữ liệu (field / 필드) gradients. Trong AI, gradients đo cục bộ (local / 로컬) sensitivity của mất mát (loss / 손실) đối với parameters. Trong finance, delta của option là derivative của price theo underlying; duration/convexity là related sensitivity concepts. Trong software các hệ thống (systems / 시스템들), derivative-like lập luận (reasoning / 추론) giúp hiểu cục bộ (local / 로컬) sức chứa (capacity / 용량) sensitivity dù measurements thường noisy và discrete.

Điểm chung là cùng một mathematical cấu trúc (structure / 구조): **cục bộ (local / 로컬) phản hồi (response / 응답) to perturbation**.

> **Chuyển mạch:** Trong **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **Physics, AI và Finance connections** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Derivative là cục bộ (local / 로컬) đối tượng (object / 객체). Extrapolate một tangent line quá xa có thể sai mạnh nếu curvature lớn.

Small derivative không luôn nghĩa đầu vào (input / 입력) “không quan trọng” globally; tác động (effect / 효과) có thể nonlinear hoặc derivative bằng zero đúng tại một special điểm (point / 지점).

A derivative computed from a mô hình (model / 모델) reflects mô hình (model / 모델) sensitivity, not automatically real-world nhân quả (causal / 인과적) sensitivity.

> **Chuyển mạch:** Ở chặng này của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Đạo hàm là cục bộ (local / 로컬) gain của một hệ thống (system / 시스템). Ta perturb đầu vào (input / 입력) một lượng rất nhỏ và hỏi đầu ra (output / 출력) phản ứng first-order ra sao. Slope, velocity, marginal chi phí (cost / 비용), độ dốc (gradient / 기울기) và backpropagation đều là các biểu hiện của cùng idea: cục bộ (local / 로컬) tuyến tính (linear / 선형) phản hồi (response / 응답).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đạo hàm: cục bộ (local / 로컬) thay đổi (change / 변경), sensitivity và tuyến tính (linear / 선형) approximation**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Derivative là slope của đồ thị (graph / 그래프) nên chỉ dùng cho hình học (geometry / 기하학).”** Slope là một biểu diễn (representation / 표현); derivative tổng quát là cục bộ (local / 로컬) sensitivity.

**“`dy/dx` chỉ là fraction.”** Notation có nhiều manipulations giống fraction vì chuỗi (chain / 사슬) quy tắc (rule / 규칙)/differentials, nhưng derivative được định nghĩa bằng limit/cục bộ (local / 로컬) tuyến tính (linear / 선형) map.

**“Derivative bằng 0 nghĩa hàm (function / 함수) không thay đổi.”** Chỉ nói first-order thay đổi (change / 변경) bằng zero tại điểm (point / 지점) đó; higher-order thay đổi (change / 변경) vẫn có thể lớn.

**“Có formula differentiable thì áp dụng ở mọi điểm (point / 지점).”** lĩnh vực (domain / 도메인), corners, discontinuities và denominator restrictions vẫn phải kiểm tra.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
