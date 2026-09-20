# Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ

Hàm mũ (Exponential Function / 지수함수) xuất hiện khi một hệ thay đổi **theo tỷ lệ của chính lượng hiện có** hoặc khi cùng một multiplicative factor được lặp đi lặp lại. Hàm logarithm (Logarithmic Function / 로그함수) là phép đảo của exponential: thay vì hỏi “sau `n` lần nhân thì lượng thành bao nhiêu?”, logarithm hỏi “cần bao nhiêu lần nhân để đạt tới lượng này?”.

Hai ideas này đi cùng nhau. Exponential mô tả multiplicative growth/decay; logarithm đo multiplicative depth, order of magnitude hoặc số bước cần thiết để đảo ngược quá trình đó.

## Từ cộng lặp sang nhân lặp

Linear growth có dạng “mỗi bước cộng cùng một amount”. Nếu bắt đầu `A_0` và mỗi period thêm `d`, ta có

```math
A_n=A_0+nd.
```

Exponential growth khác ở bản chất. Mỗi bước không cộng fixed amount mà **nhân với cùng factor** `r`:

```math
A_{n+1}=rA_n.
```

Thay recurrence nhiều lần:

```math
A_1=rA_0,
```

```math
A_2=rA_1=r^2A_0,
```

và nói chung

```math
A_n=A_0r^n.
```

Nếu `r>1`, quantity tăng. Nếu `0<r<1`, nó decay. Nếu `r=1`, quantity không đổi.

Điều quan trọng là absolute increment không cố định. Với `r=1.1`, một balance `100` tăng `10` trong period đầu, nhưng khi balance đã là `1000`, cùng 10% tạo increment `100`. Exponential growth tăng tốc vì base mà percentage được áp dụng cũng đang tăng.

## Percentage growth là multiplicative

Nếu quantity tăng `p%` mỗi period, growth factor là

```math
r=1+\frac{p}{100}.
```

Ví dụ tăng 5% mỗi năm nghĩa

```math
A_n=A_0(1.05)^n.
```

Không phải

```math
A_n=A_0+0.05nA_0
```

trừ khi ta đang model simple interest hoặc một linear approximation rất ngắn hạn.

Đây là khác biệt cơ bản giữa **percentage change** và **absolute change**.

## Exponential decay và half-life

Nếu quantity mất cùng một tỷ lệ sau mỗi period, ta có exponential decay. Giả sử sau mỗi half-life `H`, lượng còn một nửa. Sau thời gian `t`, số half-lives đã trôi qua là `t/H`, nên

```math
A(t)=A_0\left(\frac12\right)^{t/H}.
```

Nếu `t=H`, exponent bằng `1`, quantity còn `A_0/2`. Nếu `t=2H`, còn `A_0/4`.

Half-life model xuất hiện trong radioactive decay và pharmacokinetics gần đúng. Nhưng thực tế biological elimination có thể multi-compartment hoặc nonlinear; exponential decay là model dựa trên assumption rằng **fractional removal rate gần constant**.

## Continuous exponential: vì sao số `e` xuất hiện?

Trong continuous systems, statement tự nhiên không còn là “mỗi period nhân với `r`” mà là:

> instantaneous rate of change tỷ lệ với current amount.

Viết bằng differential equation:

```math
\frac{dA}{dt}=kA.
```

`A(t)` là quantity tại time `t`; `k` là proportional growth rate có unit `1/time`.

Nếu `k>0`, quantity growth; nếu `k<0`, decay.

Ta solve equation bằng separation:

```math
\frac{1}{A}\,dA=k\,dt.
```

Integrate hai phía:

```math
\ln|A|=kt+C.
```

Exponentiate:

```math
A=Ce^{kt}.
```

Dùng initial condition `A(0)=A_0` cho `C=A_0`, nên

```math
A(t)=A_0e^{kt}.
```

Số `e≈2.71828` không xuất hiện vì convention tùy ý. Exponential base `e` là function đặc biệt có derivative bằng chính nó:

```math
\frac{d}{dx}e^x=e^x.
```

Vì differential equation nói growth rate proportional current amount, `e^x` là representation tự nhiên nhất.

## Doubling time và logarithm

Giả sử

```math
A(t)=A_0e^{kt}.
```

Ta muốn biết cần bao lâu để lượng gấp đôi. Set

```math
A(T)=2A_0.
```

Suy ra

```math
e^{kT}=2.
```

Ta cần undo exponential. Đây chính là vai trò của logarithm:

```math
kT=\ln 2,
```

nên

```math
T=\frac{\ln 2}{k}.
```

Logarithm xuất hiện không phải vì “đề bài logarithm”, mà vì unknown đang nằm trong exponent.

Với decay `A=A_0e^{-\lambda t}`, half-life là

```math
T_{1/2}=\frac{\ln2}{\lambda}.
```

## Logarithm là inverse của exponentiation

Definition

```math
\log_b x=y
```

nghĩa là

```math
b^y=x.
```

Vì vậy logarithm trả lời câu hỏi: “base `b` phải được raise lên power nào để tạo `x`?”

Ví dụ

```math
\log_{10}1000=3
```

vì

```math
10^3=1000.
```

Natural logarithm `ln x` là logarithm base `e`.

Logarithm chỉ nhận positive real input khi làm việc trong real numbers:

```math
x>0.
```

Lý do là positive base exponential `b^y` luôn positive, nên inverse real của nó chỉ có domain `(0,∞)`.

## Các luật logarithm đến từ luật exponent

Vì

```math
b^m b^n=b^{m+n},
```

apply log hai phía cho ta

```math
\log_b(xy)=\log_bx+\log_by.
```

Tương tự,

```math
\log_b\frac{x}{y}=\log_bx-\log_by,
```

và

```math
\log_b(x^p)=p\log_bx.
```

Các laws này không phải rules rời để memorise. Chúng là image của exponent laws khi chuyển qua inverse operation.

## Vì sao logarithm biến multiplication thành addition?

Đây là một insight quan trọng. Multiplication trong original scale trở thành addition trong log scale:

```math
xy
\quad\longrightarrow\quad
\log x+\log y.
```

Điều này từng có giá trị computation lớn trước electronic calculators: log tables cho phép thay multiplication phức tạp bằng addition đơn giản hơn.

Trong modern computing, cùng structure vẫn quan trọng trong probability. Product của nhiều small probabilities dễ underflow:

```math
P=\prod_i p_i.
```

Lấy log:

```math
\log P=\sum_i\log p_i.
```

Vì vậy machine learning và statistics thường tối ưu **log-likelihood** thay cho likelihood product trực tiếp.

## Compound interest

Với principal `P`, rate `r` mỗi period và `n` periods:

```math
A=P(1+r)^n.
```

Nếu annual nominal rate `r` được compounded `m` lần mỗi year trong `t` years:

```math
A=P\left(1+\frac rm\right)^{mt}.
```

Khi compounding frequency tăng vô hạn,

```math
\lim_{m\to\infty}\left(1+\frac rm\right)^{mt}=e^{rt},
```

nên continuous compounding model là

```math
A=Pe^{rt}.
```

### Một numeric example

Giả sử đầu tư `P=10,000,000` VND với effective annual growth 8% trong 10 years:

```math
A=10{,}000{,}000(1.08)^{10}.
```

Vì

```math
(1.08)^{10}\approx2.159,
```

amount khoảng

```math
21{,}590{,}000\text{ VND}.
```

Lợi nhuận không phải `8%×10=80%` theo simple addition; compounding tạo khoảng 115.9% total growth.

## Rule of 72 là approximation từ logarithm

Doubling time discrete với rate `r` mỗi period thỏa

```math
(1+r)^T=2.
```

Do đó

```math
T=\frac{\ln2}{\ln(1+r)}.
```

Với `r` nhỏ,

```math
\ln(1+r)\approx r,
```

nên

```math
T\approx\frac{0.693}{r}.
```

Nếu rate được viết bằng percent `p=100r`,

```math
T\approx\frac{69.3}{p}.
```

“Rule of 72” thay `69.3` bằng `72` vì dễ chia và khá chính xác quanh nhiều rates thực tế. Đây là ví dụ một financial heuristic có nguồn gốc từ logarithmic approximation.

## Semi-log plot: exponential trở thành line

Nếu

```math
A=A_0e^{kt},
```

lấy natural log:

```math
\ln A=\ln A_0+kt.
```

Đây là linear relation giữa `ln A` và `t`. Vì vậy exponential pattern trở thành straight line trên semi-log plot.

Nhưng cần thận trọng: log-transform thay đổi error structure. Nếu original measurement có additive Gaussian-like noise,

```math
Y=A_0e^{kt}+\varepsilon,
```

thì fitting `ln Y` bằng straight line không còn tương đương exact với fitting original model. Nếu noise là multiplicative,

```math
Y=A_0e^{kt}\eta,
```

log-transform lại tự nhiên hơn vì

```math
\ln Y=\ln A_0+kt+\ln\eta.
```

Modeling choice phải dựa trên data-generating mechanism, không chỉ vì graph nhìn thẳng đẹp hơn.

## Logarithmic scales và orders of magnitude

Khi quantities trải qua nhiều powers of ten, linear axis khó đọc. Log scale compress magnitude theo ratio.

Trên base-10 log scale, khoảng cách từ `1` đến `10` bằng khoảng cách từ `10` đến `100`, vì cả hai đều là multiplication by 10.

Đây là lý do logarithmic scale xuất hiện trong:

- decibel cho intensity ratio;
- pH cho hydrogen ion concentration;
- earthquake magnitude scales trong historical/common formulations;
- information theory với logarithm của probabilities;
- algorithm complexity như `O(log n)`.

Điểm chung không phải “các lĩnh vực này đều thích log”, mà là underlying structure có **multiplicative ratios hoặc repeated scaling**.

## pH: logarithm biến concentration scale thành manageable numbers

pH được định nghĩa gần dạng

```math
\mathrm{pH}=-\log_{10}[H^+].
```

Nếu hydrogen ion concentration giảm factor 10, pH tăng 1 unit.

Ví dụ:

```math
[H^+]=10^{-3}
```

cho pH khoảng `3`; còn

```math
[H^+]=10^{-5}
```

cho pH khoảng `5`.

Hai units pH tương ứng factor `100` concentration, không phải additive difference nhỏ. Log scale làm một range cực rộng trở thành scale dễ thao tác.

## Decibel: measuring ratios chứ không phải absolute amount

Một common power-ratio form là

```math
L=10\log_{10}\left(\frac{P}{P_0}\right)\text{ dB}.
```

Nếu power ratio tăng factor 10, level tăng 10 dB. Logarithm biến multiplicative ratio thành additive level difference.

Cần chú ý công thức coefficient có thể khác với amplitude quantities vì power thường proportional amplitude squared. Context quyết định formula cụ thể.

## Exponential và algorithmic growth

Không chỉ physical quantities mới exponential. Nếu một algorithm enumerate tất cả binary assignments của `n` Boolean variables, số possibilities là

```math
2^n.
```

Tăng `n` thêm 1 làm search space nhân đôi.

Ngược lại, nếu algorithm mỗi step chia problem size đôi,

```text
n → n/2 → n/4 → n/8 → ...
```

số steps cần để xuống 1 thỏa

```math
\frac{n}{2^k}\approx1.
```

Do đó

```math
k\approx\log_2 n.
```

Binary search có logarithmic depth vì mỗi comparison loại bỏ một fraction lớn của search space.

## Logistic growth: khi exponential bị giới hạn

Pure exponential model ngầm giả định growth factor không suy giảm khi quantity lớn. Trong population systems hoặc resource-limited processes, assumption đó thường sai.

Một simple correction là logistic differential equation:

```math
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right).
```

`r` là intrinsic growth rate; `K` là carrying capacity.

Khi `P≪K`, factor

```math
1-\frac{P}{K}\approx1,
```

nên system gần exponential:

```math
\frac{dP}{dt}\approx rP.
```

Khi `P→K`, factor tiến về `0`, growth slow và equilibrium xuất hiện.

Đây là ví dụ quan trọng về model refinement: exponential không “sai”, nhưng chỉ đúng trong regime nơi resource constraint chưa đáng kể.

## Exponential as eigenfunction of differentiation

Một property sâu hơn là exponential giữ nguyên shape dưới differentiation:

```math
\frac{d}{dx}e^{kx}=ke^{kx}.
```

Differentiation chỉ scale function bởi `k`. Vì thế exponential đóng vai trò tương tự eigenvector nhưng trong function space: nó là một eigenfunction của derivative operator.

Connection này giải thích tại sao exponentials xuất hiện tự nhiên khi solve linear differential equations, Fourier/Laplace methods, control systems và signal processing.

## Exponential family không có nghĩa mọi rapid growth là exponential

Một curve tăng nhanh chưa đủ chứng minh exponential. Polynomial `x^10` có thể trông rất steep trên một interval nhỏ. Super-exponential processes như `e^{t^2}` còn tăng nhanh hơn.

Để gọi một process exponential, ta cần structural reason hoặc data evidence cho roughly constant relative growth rate:

```math
\frac{1}{A}\frac{dA}{dt}\approx k.
```

Đây là diagnostic bản chất: relative rate constant tạo exponential.

## Knowledge Connection — logarithm và information

Nếu một event có probability `p`, information content thường model bằng

```math
I=-\log p.
```

Rare event (`p` nhỏ) mang nhiều surprise/information hơn. Logarithm được dùng vì independent probabilities multiply:

```math
p(A,B)=p(A)p(B),
```

trong khi information ta muốn add:

```math
I(A,B)=I(A)+I(B).
```

Logarithm chính là function biến product thành sum. Đây là reason structural, không phải convention ngẫu nhiên.

## Mental Model

> Exponential là toán học của repeated proportional change: cùng một **tỷ lệ**, không phải cùng một **lượng**, được áp dụng liên tục hoặc lặp lại. Logarithm quay ngược quá trình đó để đo số lần scaling, thời gian cần đạt threshold hoặc order of magnitude. Khi thấy multiplication lặp, percentage compounding, constant relative rate hoặc search space co theo ratio, hãy nghĩ đến exponential/logarithm như một cặp inverse.

## Common Misconceptions

**“Exponential chỉ nghĩa là tăng rất nhanh.”** Không. Exponential là một specific structural law. Rapid polynomial growth vẫn không phải exponential.

**“Tăng 10% trong hai năm nghĩa tăng 20%.”** Chỉ đúng gần đúng với small rates/short horizon. Exact compounding là `1.1²=1.21`, tức 21%.

**“Logarithm chỉ là một nút trên calculator.”** Logarithm đo exponent/multiplicative depth và biến products thành sums. Đây là reason nó xuất hiện trong complexity, information theory, likelihood và scientific scales.

**“Log-transform luôn làm data tuyến tính.”** Chỉ một số functional forms như exponential hoặc power laws trở thành linear trong coordinates thích hợp. Arbitrary nonlinear relation không tự biến thành linear.

**“Exponential growth có thể tiếp tục vô hạn trong physical system.”** Mathematical model cho phép, nhưng physical resources thường tạo saturation, feedback hoặc regime change. Model validity phải được kiểm tra, không extrapolate vô hạn chỉ vì curve fit ban đầu tốt.