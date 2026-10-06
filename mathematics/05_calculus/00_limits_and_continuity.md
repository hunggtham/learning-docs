# Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tại sao “gần” cần definition chính xác?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Một ví dụ quan trọng: hàm (function / 함수) không cần được định nghĩa tại điểm (point / 지점)** để đem mô hình vào tình huống cụ thể. Mạch này nối giới hạn với liên tục và phép tính vi phân, để kiểm tra một kết quả có ổn định khi đầu vào tiến gần hay không.

Giải tích (Calculus / 미적분) bắt đầu khi những câu hỏi đơn giản về thay đổi (change / 변경) và accumulation va vào một vấn đề lô-gic (logic / 논리): nhiều quantities ta muốn biết chỉ xuất hiện khi một interval trở nên **cực nhỏ** hoặc khi một tiến trình (process / 프로세스) được lặp **cực nhiều lần**.

Vận tốc trung bình trên interval `Δt` là

```math
\frac{\Delta x}{\Delta t}.
```

Nhưng vận tốc **tức thời** tại đúng một thời điểm thì sao? Nếu đặt `Δt=0`, ta chia cho 0. Nếu không đặt bằng 0, ta vẫn chỉ có average trên một interval hữu hạn.

Giới hạn (Limit / 극한) giải quyết đúng khoảng trống đó. Nó cho phép ta nói: “ta không cần đặt interval bằng 0; ta nghiên cứu điều xảy ra khi interval có thể được làm nhỏ tùy ý.”

> Limit không phải phép thế `x=a`. Nó là ngôn ngữ để mô tả hành vi (behavior / 동작) khi `x` tiến gần `a` với mức chính xác tùy ý.

## Tại sao “gần” cần definition chính xác?

Trong everyday ngôn ngữ (language / 언어), “gần” là mơ hồ. `0.001` có gần 0 không? Với kỹ thuật (engineering / 엔지니어링) tolerance 1 mm thì có thể gần; với quantum-scale đo lường (measurement / 측정) thì không.

Mathematics cần statement không phụ thuộc cảm giác. Khi viết

```math
\lim_{x\to a}f(x)=L,
```

ý nghĩa không phải “`f(x)` trông gần `L` trên đồ thị (graph / 그래프)”, mà là:

> ta có thể yêu cầu đầu ra (output / 출력) gần `L` đến mức tùy ý, và luôn tìm được một vùng quanh `a` đủ nhỏ để mọi đầu vào (input / 입력) trong vùng đó tạo đầu ra (output / 출력) nằm trong tolerance mong muốn.

Đây là một đặc tả hợp đồng (contract / 계약) giữa **đầu vào (input / 입력) tolerance** và **đầu ra (output / 출력) tolerance**.

> **Nối mạch:** “Gần” chỉ có nghĩa toán học khi được gắn với tolerance của đầu ra; ví dụ hàm không định nghĩa tại điểm cho thấy limit xét lân cận chứ không xét riêng giá trị đó. **Epsilon–delta** tiếp theo biến trực giác này thành hợp đồng định lượng giữa (\varepsilon) và (\delta).

## Một ví dụ quan trọng: hàm (function / 함수) không cần được định nghĩa tại điểm (point / 지점)

Xét

```math
f(x)=\frac{x^2-1}{x-1}.
```

Tại `x=1`, denominator bằng 0 nên `f(1)` không được định nghĩa.

Nhưng với `x≠1`, factor numerator:

```math
x^2-1=(x-1)(x+1),
```

nên

```math
f(x)=x+1.
```

Khi `x` tiến gần `1`, `x+1` tiến gần `2`. Vì vậy

```math
\lim_{x\to1}f(x)=2.
```

Điểm này rất quan trọng: **limit mô tả neighborhood hành vi (behavior / 동작), không nhất thiết hàm (function / 함수) giá trị (value / 값) tại điểm (point / 지점)**.

Ta thậm chí có thể define lại

```math
f(1)=100
```

mà limit vẫn là `2`, vì một isolated điểm (point / 지점) không thay hành vi (behavior / 동작) của nearby values.

> **Nối mạch:** Ví dụ khử nhân tử cho thấy một lỗ hổng tại (x=a) không ngăn limit tồn tại; **epsilon–delta** giải thích chính xác vì sao mọi (x) đủ gần nhưng khác (a) đều cho đầu ra gần (L). Ví dụ epsilon–delta đơn giản tiếp theo luyện cách chọn (\delta) từ yêu cầu (\varepsilon).

## Epsilon–delta: biến “gần” thành đặc tả hợp đồng (contract / 계약) định lượng

Definition formal của

```math
\lim_{x\to a}f(x)=L
```

là:

> với mọi `ε>0`, tồn tại `δ>0` sao cho nếu

```math
0<|x-a|<\delta,
```

thì

```math
|f(x)-L|<\varepsilon.
```

`ε` đo tolerance ở đầu ra (output / 출력). `δ` là tolerance ở đầu vào (input / 입력) đủ để guarantee đầu ra (output / 출력) tolerance đó.

Điều kiện `0<|x-a|` loại điểm (point / 지점) `x=a`, vì limit chỉ hỏi hành vi (behavior / 동작) quanh điểm (point / 지점). Nếu hàm (function / 함수) giá trị (value / 값) tại `a` cần tham gia, đó là câu hỏi về continuity.

### Đọc definition như một game

Tưởng tượng một người thách thức chọn bất kỳ `ε>0`, dù cực nhỏ. Nhiệm vụ của ta là đưa ra `δ>0` sao cho mọi `x` thỏa

```math
0<|x-a|<\delta
```

đều buộc `f(x)` nằm trong

```math
(L-\varepsilon,L+\varepsilon).
```

Nếu ta luôn làm được, limit là `L`.

Cách nhìn này giải thích vì sao definition dùng “for every `ε`” trước “there exists `δ`”. Ta không được chọn một tolerance dễ rồi tuyên bố limit tồn tại; phải đáp ứng mọi độ chính xác được yêu cầu.

> **Nối mạch:** Định nghĩa epsilon–delta là tiêu chuẩn tổng quát; ví dụ đơn giản cho thấy cách biến (|f(x)-L|) thành một biểu thức bị chặn bởi (|x-a|). Khi kỹ thuật này rõ, **limit laws** cho phép ghép các giới hạn đã biết thay vì chứng minh lại từ đầu.

## Epsilon–delta example đơn giản

Chứng minh

```math
\lim_{x\to3}(2x+1)=7.
```

Ta muốn

```math
|(2x+1)-7|<\varepsilon.
```

Simplify:

```math
|2x-6|=2|x-3|.
```

Muốn expression này nhỏ hơn `ε`, chỉ cần

```math
|x-3|<\frac{\varepsilon}{2}.
```

Vậy chọn

```math
\delta=\frac{\varepsilon}{2}.
```

Khi đó

```math
0<|x-3|<\delta
```

suy ra

```math
|(2x+1)-7|=2|x-3|<2\delta=\varepsilon.
```

Proof này cho thấy epsilon–delta không phải nghi thức formal vô nghĩa. Nó tường minh (explicit / 명시적) hóa sensitivity giữa đầu vào (input / 입력) và đầu ra (output / 출력).

> **Nối mạch:** Ví dụ epsilon–delta chứng minh một limit cụ thể, còn **limit laws** cung cấp phép cộng, nhân và chia có điều kiện để mở rộng kết quả. Bước kế tiếp hỏi khi nào có thể **direct substitution**, và khi nào mẫu số bằng 0 hoặc gián đoạn buộc phải biến đổi thêm.

## Limit laws: tại sao ta không phải chứng minh từ đầu mọi lần?

Nếu

```math
\lim_{x\to a}f(x)=L
```

và

```math
\lim_{x\to a}g(x)=M,
```

thì dưới conditions phù hợp:

```math
\lim_{x\to a}[f(x)+g(x)]=L+M,
```

```math
\lim_{x\to a}f(x)g(x)=LM,
```

và nếu `M≠0`,

```math
\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{L}{M}.
```

Các laws này follow từ epsilon–delta cấu trúc (structure / 구조). Một khi đã được prove, chúng trở thành reusable building blocks.

Đây là mẫu (pattern / 패턴) chung của mathematics: formal foundation được xây kỹ để later lập luận (reasoning / 추론) có thể dùng theorem thay vì re-prove mọi detail.

> **Nối mạch:** Limit laws cho phép thế trực tiếp khi các phép toán vẫn xác định và liên tục tại điểm; **direct substitution** vì thế là kết luận có điều kiện, không phải mẹo phổ quát. Khi gặp dạng (0/0) hoặc (infty/infty), **indeterminate form** chỉ báo cần phân tích thêm chứ chưa phải đáp án.

## Khi direct substitution đúng?

Nếu `f` continuous tại `a`, thì

```math
\lim_{x\to a}f(x)=f(a).
```

Vì vậy với polynomials, many elementary functions và compositions trong lĩnh vực (domain / 도메인) hợp lệ, direct substitution thường hoạt động.

Ví dụ

```math
\lim_{x\to2}(x^2+3x)=4+6=10.
```

Nhưng direct substitution không phải definition của limit. Nó là shortcut justified bởi continuity.

Khi substitution cho `0/0`, ta không thể conclude limit là `0/0`; đó là **indeterminate form**, tín hiệu (signal / 신호) rằng cần analyze cấu trúc (structure / 구조) sâu hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Indeterminate form không phải answer** nối từ **Khi direct substitution đúng?** sang **One-sided limits: approach direction có thể matter**, vì cơ chế trước tạo đầu vào cho bước sau.

## Indeterminate form không phải answer

Xét

```math
\lim_{x\to1}\frac{x^2-1}{x-1}.
```

Substitution cho

```math
\frac00.
```

Nhưng `0/0` không phải giá trị (value / 값). Nó nói numerator và denominator đều vanish nên relative rates matter.

Factorization cho limit `2`.

Một expression khác,

```math
\frac{(x-1)^2}{x-1}=x-1,
```

cũng cho `0/0` khi substitute `1`, nhưng limit là `0`.

Do đó same indeterminate form có thể dẫn tới different limits. Form cho biết “cần thêm phân tích (analysis / 분석)”, không quyết định kết quả (result / 결과).

> **Nối mạch:** Trong **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Indeterminate form không phải answer** đặt tiêu chí; **One-sided limits: approach direction có thể matter** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Infinite limits: unbounded hành vi (behavior / 동작), không phải “giá trị infinity”** mở rộng hệ quả.

## One-sided limits: approach direction có thể matter

Left-hand limit

```math
\lim_{x\to a^-}f(x)
```

chỉ xét `x<a` tiến tới `a`.

Right-hand limit

```math
\lim_{x\to a^+}f(x)
```

chỉ xét `x>a`.

Two-sided limit tồn tại khi hai one-sided limits tồn tại và bằng nhau.

Xét step hàm (function / 함수)

```math
f(x)=
\begin{cases}
0,&x<0,\\
1,&x\ge0.
\end{cases}
```

Ta có

```math
\lim_{x\to0^-}f(x)=0,
```

nhưng

```math
\lim_{x\to0^+}f(x)=1.
```

Vì hai sides khác nhau,

```math
\lim_{x\to0}f(x)
```

không tồn tại.

Piecewise pricing, tax threshold, activation functions và điều khiển (control / 제어) lô-gic (logic / 논리) đều có thể tạo kiểu hành vi (behavior / 동작) này.

> **Nối mạch:** Ở chặng này của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **One-sided limits: approach direction có thể matter** đặt tiêu chí; **Infinite limits: unbounded hành vi (behavior / 동작), không phải “giá trị infinity”** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Limits at infinity: long-run hành vi (behavior / 동작)** mở rộng hệ quả.

## Infinite limits: unbounded hành vi (behavior / 동작), không phải “giá trị infinity”

Khi viết

```math
\lim_{x\to0^+}\frac1x=+\infty,
```

`∞` không phải real number mà hàm (function / 함수) chạm tới. Statement nói:

> với bất kỳ bound `M` lớn đến đâu, ta có thể chọn `x>0` đủ gần 0 để `1/x>M`.

Tương tự,

```math
\lim_{x\to0^-}\frac1x=-\infty.
```

Vì hành vi (behavior / 동작) hai sides khác sign, không có single two-sided infinite hành vi (behavior / 동작).

Vertical asymptote thường liên quan kiểu unbounded cục bộ (local / 로컬) hành vi (behavior / 동작) này.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Infinite limits: unbounded hành vi (behavior / 동작), không phải “giá trị infinity”** đặt tiêu chí; **Limits at infinity: long-run hành vi (behavior / 동작)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Rates of growth và dominant terms** mở rộng hệ quả.

## Limits at infinity: long-run hành vi (behavior / 동작)

Ký hiệu

```math
\lim_{x\to\infty}f(x)=L
```

không nói `x` “đạt infinity”. Nó nói khi `x` vượt mọi threshold đủ lớn, `f(x)` có thể được ép gần `L` tùy ý.

Ví dụ

```math
\lim_{x\to\infty}\frac{3x^2+1}{x^2-5}=3.
```

Chia numerator và denominator cho `x^2`:

```math
\frac{3+1/x^2}{1-5/x^2}.
```

Khi `x→∞`, terms `1/x^2` và `5/x^2` tiến về 0, để lại ratio `3`.

Điều này phản ánh principle “highest-order terms dominate” cho rational functions ở large magnitude.

> **Nối mạch:** Trong **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Limits at infinity: long-run hành vi (behavior / 동작)** đặt tiêu chí; **Rates of growth và dominant terms** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Continuity: khi hàm (function / 함수) giá trị (value / 값) khớp với cục bộ (local / 로컬) hành vi (behavior / 동작)** mở rộng hệ quả.

## Rates of growth và dominant terms

Limits at infinity cho phép compare growth.

Ví dụ polynomial thấp hơn bị polynomial cao hơn dominate:

```math
\lim_{x\to\infty}\frac{x^2}{x^3}=0.
```

Exponential dominate polynomial:

```math
\lim_{x\to\infty}\frac{x^k}{e^x}=0
```

cho fixed positive integer `k`.

Logarithm grow chậm hơn powers:

```math
\lim_{x\to\infty}\frac{\ln x}{x^a}=0
```

với `a>0`.

Hierarchy này rất quan trọng trong thuật toán (algorithm / 알고리즘) độ phức tạp (complexity / 복잡도) và asymptotic phân tích (analysis / 분석).

> **Nối mạch:** Ở chặng này của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Continuity: khi hàm (function / 함수) giá trị (value / 값) khớp với cục bộ (local / 로컬) hành vi (behavior / 동작)** nối từ **Rates of growth và dominant terms** sang **Continuity trên interval**, vì cơ chế trước tạo đầu vào cho bước sau.

## Continuity: khi hàm (function / 함수) giá trị (value / 값) khớp với cục bộ (local / 로컬) hành vi (behavior / 동작)

Hàm (function / 함수) `f` continuous tại `a` nếu

```math
\lim_{x\to a}f(x)=f(a).
```

Viết đầy đủ, điều này ngầm yêu cầu:

- `f(a)` được định nghĩa;
- limit tồn tại;
- limit bằng hàm (function / 함수) giá trị (value / 값).

Trực giác “vẽ đồ thị (graph / 그래프) không nhấc bút” hữu ích trong `R→R`, nhưng không đủ general. Definition sâu hơn là **small đầu vào (input / 입력) perturbation tạo arbitrarily small đầu ra (output / 출력) perturbation** cục bộ (local / 로컬) quanh điểm (point / 지점).

Epsilon–delta form của continuity là:

```math
|x-a|<\delta\Rightarrow |f(x)-f(a)|<\varepsilon.
```

Khác limit definition ở chỗ `x=a` không cần bị exclude và mục tiêu (target / 대상) đầu ra (output / 출력) là chính `f(a)`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Continuity trên interval** nối từ **Continuity: khi hàm (function / 함수) giá trị (value / 값) khớp với cục bộ (local / 로컬) hành vi (behavior / 동작)** sang **Intermediate giá trị (value / 값) Theorem và gốc (root / 루트) existence**, vì cơ chế trước tạo đầu vào cho bước sau.

## Continuity trên interval

Một hàm (function / 함수) continuous trên interval nếu continuous tại mọi interior điểm (point / 지점) và appropriate one-sided continuity tại endpoints.

Continuous functions có nhiều stability properties. Hai theorem đặc biệt quan trọng trên closed bounded interval `[a,b]` là:

**Extreme giá trị (value / 값) Theorem:** continuous hàm (function / 함수) đạt minimum và maximum.

**Intermediate giá trị (value / 값) Theorem:** hàm (function / 함수) nhận mọi giá trị (value / 값) giữa `f(a)` và `f(b)`.

Continuity vì thế không chỉ là “đồ thị (graph / 그래프) mượt”. Nó guarantee existence của values/extrema dưới conditions cụ thể.

> **Nối mạch:** Trong **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Intermediate giá trị (value / 값) Theorem và gốc (root / 루트) existence** nối từ **Continuity trên interval** sang **Types of discontinuity**, vì cơ chế trước tạo đầu vào cho bước sau.

## Intermediate giá trị (value / 값) Theorem và gốc (root / 루트) existence

Nếu `f` continuous trên `[a,b]` và

```math
f(a)f(b)<0,
```

thì `0` nằm giữa `f(a)` và `f(b)`. Intermediate giá trị (value / 값) Theorem bảo đảm tồn tại ít nhất một `c∈(a,b)` sao cho

```math
f(c)=0.
```

Đây là theoretical foundation của bisection.

Lưu ý theorem chỉ guarantee **existence**, không uniqueness. hàm (function / 함수) có thể cross zero nhiều lần trong interval.

> **Nối mạch:** Ở chặng này của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Types of discontinuity** nối từ **Intermediate giá trị (value / 값) Theorem và gốc (root / 루트) existence** sang **Continuous không có nghĩa differentiable**, vì cơ chế trước tạo đầu vào cho bước sau.

## Types of discontinuity

### Removable discontinuity

Ví dụ

```math
f(x)=\frac{x^2-1}{x-1}
```

at `x=1` có finite limit `2` nhưng hàm (function / 함수) undefined. Ta có thể “repair” continuity bằng cách define

```math
f(1)=2.
```

### Jump discontinuity

Left và right limits finite nhưng khác nhau. Step functions thường có jumps.

### Infinite discontinuity

Hàm (function / 함수) unbounded quanh điểm (point / 지점), như `1/x` tại 0.

### Oscillatory thất bại (failure / 실패)

Hàm (function / 함수)

```math
f(x)=\sin\frac1x
```

khi `x→0` oscillate ngày càng nhanh giữa `-1` và `1`, nên không approach một giá trị (value / 값) duy nhất.

Ví dụ này quan trọng vì limit có thể thất bại (fail / 실패) mà không jump và không blow up.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Continuous không có nghĩa differentiable** nối từ **Types of discontinuity** sang **Differentiability như cục bộ (local / 로컬) linearity**, vì cơ chế trước tạo đầu vào cho bước sau.

## Continuous không có nghĩa differentiable

Absolute giá trị (value / 값)

```math
f(x)=|x|
```

continuous tại `0`, nhưng derivative không tồn tại ở đó vì left slope `-1` và right slope `1`.

Differentiability stronger hơn continuity.

Nếu hàm (function / 함수) differentiable tại `a`, nó continuous tại `a`. Converse sai.

Geometrically, derivative cần cục bộ (local / 로컬) tuyến tính (linear / 선형) approximation; continuity chỉ yêu cầu no đầu ra (output / 출력) jump under arbitrarily small đầu vào (input / 입력) perturbation.

> **Nối mạch:** Trong **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Differentiability như cục bộ (local / 로컬) linearity** nối từ **Continuous không có nghĩa differentiable** sang **Chuỗi (sequence / 시퀀스) viewpoint của limits**, vì cơ chế trước tạo đầu vào cho bước sau.

## Differentiability như cục bộ (local / 로컬) linearity

Limit mở đường cho derivative:

```math
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}.
```

Expression bên trong là average slope trên interval kích thước (size / 크기) `h`. Limit hỏi liệu slopes có stabilize về một giá trị (value / 값) khi interval shrink không.

Vì vậy derivative không phải “đặt `h=0`”. Ta không bao giờ divide by zero. Ta analyze ratio cho nonzero `h` rồi lấy limit.

Đây là conceptual reason limits nằm trước derivatives trong calculus.

> **Nối mạch:** Ở chặng này của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Differentiability như cục bộ (local / 로컬) linearity** đặt tiêu chí; **Chuỗi (sequence / 시퀀스) viewpoint của limits** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Limits và infinite series** mở rộng hệ quả.

## Chuỗi (sequence / 시퀀스) viewpoint của limits

Một cách hiểu khác: nếu mọi chuỗi (sequence / 시퀀스) `x_n` với

```math
x_n\to a,
```

và `x_n≠a` cuối cùng, đều cho

```math
f(x_n)\to L,
```

thì hàm (function / 함수) limit là `L` trong tiêu chuẩn (standard / 표준) real setting.

Viewpoint này rất hữu ích để prove nonexistence. Nếu ta tìm hai sequences cùng tiến tới `a` nhưng hàm (function / 함수) values tiến tới two different limits, toàn cục (global / 전역) limit không tồn tại.

Ví dụ với

```math
f(x)=\sin\frac1x,
```

ta chọn sequences làm `1/x` rơi vào peaks `π/2+2πn` và troughs `3π/2+2πn`; hàm (function / 함수) values lần lượt tiến theo subsequences `1` và `-1`. Vì vậy không có single limit tại 0.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Chuỗi (sequence / 시퀀스) viewpoint của limits** đặt tiêu chí; **Limits và infinite series** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Uniform continuity: cùng một δ cho cả region** mở rộng hệ quả.

## Limits và infinite series

Series

```math
\sum_{n=1}^{\infty}a_n
```

không có nghĩa “thực hiện phép cộng vô hạn xong”. Ta define partial sums

```math
S_N=\sum_{n=1}^N a_n
```

rồi hỏi limit

```math
\lim_{N\to\infty}S_N.
```

Infinite sum tồn tại khi chuỗi (sequence / 시퀀스) partial sums converge.

Limit vì thế là cơ chế (mechanism / 메커니즘) biến “infinite tiến trình (process / 프로세스)” thành finite mathematical đối tượng (object / 객체) thông qua convergence.

> **Nối mạch:** Trong **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Limits và infinite series** đặt tiêu chí; **Uniform continuity: cùng một δ cho cả region** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Continuity trong nhiều dimensions** mở rộng hệ quả.

## Uniform continuity: cùng một `δ` cho cả region

Ordinary continuity cho phép `δ` phụ thuộc cả `ε` và điểm (point / 지점) `a`.

Uniform continuity yêu cầu với mỗi `ε`, một single `δ` hoạt động cho mọi pair points trong lĩnh vực (domain / 도메인):

```math
|x-y|<\delta\Rightarrow |f(x)-f(y)|<\varepsilon.
```

Continuous hàm (function / 함수) trên closed bounded interval `[a,b]` luôn uniformly continuous.

Distinction này quan trọng trong phân tích (analysis / 분석) vì nó kiểm soát sensitivity globally hơn cục bộ (local / 로컬) pointwise continuity.

> **Nối mạch:** Ở chặng này của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Continuity trong nhiều dimensions** nối từ **Uniform continuity: cùng một δ cho cả region** sang **Limit và numerical computing là hai tầng khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## Continuity trong nhiều dimensions

Với hàm (function / 함수)

```math
f:\mathbb R^n\to\mathbb R^m,
```

continuity generalize bằng distance/norm:

```math
\|x-a\|<\delta
\Rightarrow
\|f(x)-f(a)\|<\varepsilon.
```

Ta thấy essence không phụ thuộc one-dimensional đồ thị (graph / 그래프). Continuity là preservation của nearness.

Topology sau này abstract hóa idea này hơn nữa, thậm chí bỏ tường minh (explicit / 명시적) chỉ số (metric / 지표) trong nhiều contexts.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Continuity trong nhiều dimensions** đặt tiêu chí; **Limit và numerical computing là hai tầng khác nhau** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Limits trong asymptotic độ phức tạp (complexity / 복잡도)** mở rộng hệ quả.

## Limit và numerical computing là hai tầng khác nhau

Mathematical statement

```math
h\to0
```

không bảo computer nên chọn `h` cực nhỏ nhất có thể.

Finite-difference derivative

```math
\frac{f(x+h)-f(x)}{h}
```

có truncation lỗi (error / 오류) khi `h` lớn nhưng cancellation/rounding lỗi (error / 오류) khi `h` quá nhỏ.

Limit là ideal mathematical đối tượng (object / 객체); numerical thuật toán (algorithm / 알고리즘) phải chọn finite step trong finite precision.

Nhầm hai tầng này dẫn đến misconception kiểu “đặt `h=10^{-100}` sẽ gần derivative hơn”. Trên floating điểm (point / 지점), `x+h` thậm chí có thể round thành đúng `x`.

> **Nối mạch:** Trong **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Limit và numerical computing là hai tầng khác nhau** đặt tiêu chí; **Limits trong asymptotic độ phức tạp (complexity / 복잡도)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Liên kết kiến thức (knowledge connection / 지식 연결) — continuity và robust các hệ thống (systems / 시스템들)** mở rộng hệ quả.

## Limits trong asymptotic độ phức tạp (complexity / 복잡도)

Big-O notation cũng nói về long-run growth hành vi (behavior / 동작).

Statement

```math
T(n)=O(g(n))
```

có nghĩa tồn tại constants `C,n_0` sao cho

```math
|T(n)|\le C|g(n)|
```

cho mọi `n≥n_0`.

Limit ratio thường giúp compare growth:

```math
\lim_{n\to\infty}\frac{T(n)}{g(n)}.
```

Nếu ratio tiến tới positive finite constant, hai functions có cùng asymptotic thứ tự (order / 순서) theo strong intuitive sense.

Vì vậy limit không chỉ là calculus technique; nó là ngôn ngữ (language / 언어) của asymptotics trong algorithms.

> **Nối mạch:** Ở chặng này của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Limits trong asymptotic độ phức tạp (complexity / 복잡도)** đặt tiêu chí; **Liên kết kiến thức (knowledge connection / 지식 연결) — continuity và robust các hệ thống (systems / 시스템들)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Liên kết kiến thức (knowledge connection / 지식 연결) — continuity và tối ưu hóa (optimization / 최적화)** mở rộng hệ quả.

## Liên kết kiến thức (knowledge connection / 지식 연결) — continuity và robust các hệ thống (systems / 시스템들)

Trong kỹ thuật (engineering / 엔지니어링), continuity là thành phần nguyên thủy (primitive / 기본 요소) form của robustness: small thay đổi (change / 변경) đầu vào (input / 입력) không tạo arbitrary large jump đầu ra (output / 출력).

Nhưng continuity không guarantee practical robustness đủ mạnh. hàm (function / 함수) có thể continuous nhưng derivative cực lớn, nghĩa tiny đầu vào (input / 입력) noise vẫn tạo large đầu ra (output / 출력) thay đổi (change / 변경).

Để quantify sensitivity ta cần derivatives, Lipschitz constants hoặc điều kiện (condition / 조건) numbers.

Continuity trả lời “có catastrophic jump do infinitesimal perturbation không?”; conditioning trả lời “amplification mạnh đến mức nào?”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Liên kết kiến thức (knowledge connection / 지식 연결) — continuity và tối ưu hóa (optimization / 최적화)** nối từ **Liên kết kiến thức (knowledge connection / 지식 연결) — continuity và robust các hệ thống (systems / 시스템들)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Liên kết kiến thức (knowledge connection / 지식 연결) — continuity và tối ưu hóa (optimization / 최적화)

Continuous mục tiêu (objective / 목표) trên compact feasible set đạt toàn cục (global / 전역) min/max theo Extreme giá trị (value / 값) Theorem. Đây là existence guarantee trước khi bàn thuật toán (algorithm / 알고리즘) nào tìm optimum.

Differentiability cho gradient-based methods thêm cục bộ (local / 로컬) hình học (geometry / 기하학), nhưng existence của optimum và computability của optimum là different questions.

Mathematical tối ưu hóa (optimization / 최적화) tốt cần phân biệt rõ các tầng guarantee này.

> **Nối mạch:** Trong **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên kết kiến thức (knowledge connection / 지식 연결) — continuity và tối ưu hóa (optimization / 최적화)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Limit là một **tolerance đặc tả hợp đồng (contract / 계약)**: nếu ta yêu cầu đầu ra (output / 출력) gần mục tiêu (target / 대상) đến bất kỳ mức nào, liệu có thể ép đầu vào (input / 입력) đủ gần điểm (point / 지점) để guarantee điều đó không? Continuity nói hàm (function / 함수) giá trị (value / 값) tại điểm (point / 지점) đồng ý với cục bộ (local / 로컬) limit. Derivative dùng limit để biến shrinking interval thành instantaneous tỷ lệ (rate / 비율); integral và infinite series dùng limit để biến increasingly fine/long finite approximations thành mathematical đối tượng (object / 객체). Limit là cây cầu giữa finite lập luận (reasoning / 추론) và idealized infinitesimal/infinite hành vi (behavior / 동작).

> **Nối mạch:** Ở chặng này của **Giới hạn và tính liên tục: làm chính xác ý tưởng “tiến gần”**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“`x→a` nghĩa cuối cùng `x=a`.”** Không. Limit nghiên cứu arbitrarily close values; `x=a` có thể bị exclude.

**“Limit luôn bằng hàm (function / 함수) giá trị (value / 값).”** Chỉ khi hàm (function / 함수) continuous tại điểm (point / 지점). Hole hoặc intentionally redefined điểm (point / 지점) có thể khác limit.

**“`0/0` là limit bằng 0.”** `0/0` là indeterminate form, không phải answer. Different expressions cho same form có thể có different limits.

**“`∞` là một số real rất lớn.”** Trong tiêu chuẩn (standard / 표준) real calculus, infinity biểu diễn unbounded hành vi (behavior / 동작) hoặc extended concept, không phải ordinary real number để algebra tùy ý.

**“Continuous nghĩa smooth.”** Continuous hàm (function / 함수) có thể có corner, nowhere-differentiable hành vi (behavior / 동작) hoặc rất irregular shape. Differentiability/smoothness là stronger properties.

**“Muốn numerical derivative tốt chỉ cần lấy `h` càng nhỏ.”** Mathematical limit và floating-point approximation khác nhau. Quá nhỏ có thể làm rounding/cancellation dominate.

**“đồ thị (graph / 그래프) nhìn có vẻ tiến tới giá trị (value / 값) là đủ chứng minh limit.”** đồ thị (graph / 그래프) tạo intuition nhưng finite-resolution picture không phải proof; oscillation hoặc narrow hành vi (behavior / 동작) có thể bị hình vẽ che mất.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
