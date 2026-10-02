# Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ cộng lặp sang nhân lặp** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Percentage growth là multiplicative** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối exponential/logarithmic models với growth, decay và inverse scale, để chọn mô hình theo cơ chế thay đổi.

Hàm mũ (Exponential Function / 지수함수) xuất hiện khi một hệ thay đổi **theo tỷ lệ của chính lượng hiện có** hoặc khi cùng một multiplicative factor được lặp đi lặp lại. Hàm logarithm (Logarithmic Function / 로그함수) là phép đảo của exponential: thay vì hỏi “sau `n` lần nhân thì lượng thành bao nhiêu?”, logarithm hỏi “cần bao nhiêu lần nhân để đạt tới lượng này?”.

Hai ideas này đi cùng nhau. Exponential mô tả multiplicative growth/decay; logarithm đo multiplicative độ sâu (depth / 깊이), thứ tự (order / 순서) of magnitude hoặc số bước cần thiết để đảo ngược quá trình đó.

## Từ cộng lặp sang nhân lặp

Tuyến tính (linear / 선형) growth có dạng “mỗi bước cộng cùng một amount”. Nếu bắt đầu `A_0` và mỗi period thêm `d`, ta có

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

Điều quan trọng là absolute increment không cố định. Với `r=1.1`, một balance `100` tăng `10` trong period đầu, nhưng khi balance đã là `1000`, cùng 10% tạo increment `100`. Exponential growth tăng tốc vì cơ sở (base / 기반) mà percentage được áp dụng cũng đang tăng.

> **Chuyển mạch:** Trong **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Percentage growth là multiplicative** tiếp nhận điểm tựa từ **Từ cộng lặp sang nhân lặp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exponential decay và half-life** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

trừ khi ta đang mô hình (model / 모델) simple interest hoặc một tuyến tính (linear / 선형) approximation rất ngắn hạn.

Đây là khác biệt cơ bản giữa **percentage thay đổi (change / 변경)** và **absolute thay đổi (change / 변경)**.

> **Chuyển mạch:** Ở chặng này của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Exponential decay và half-life** tiếp nhận điểm tựa từ **Percentage growth là multiplicative** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Continuous exponential: vì sao số e xuất hiện?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exponential decay và half-life

Nếu quantity mất cùng một tỷ lệ sau mỗi period, ta có exponential decay. Giả sử sau mỗi half-life `H`, lượng còn một nửa. Sau thời gian `t`, số half-lives đã trôi qua là `t/H`, nên

```math
A(t)=A_0\left(\frac12\right)^{t/H}.
```

Nếu `t=H`, exponent bằng `1`, quantity còn `A_0/2`. Nếu `t=2H`, còn `A_0/4`.

Half-life mô hình (model / 모델) xuất hiện trong radioactive decay và pharmacokinetics gần đúng. Nhưng thực tế biological elimination có thể multi-compartment hoặc nonlinear; exponential decay là mô hình (model / 모델) dựa trên giả định (assumption / 가정) rằng **fractional removal tỷ lệ (rate / 비율) gần constant**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Continuous exponential: vì sao số e xuất hiện?** tiếp nhận điểm tựa từ **Exponential decay và half-life** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Doubling thời gian (time / 시간) và logarithm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Continuous exponential: vì sao số `e` xuất hiện?

Trong continuous các hệ thống (systems / 시스템들), statement tự nhiên không còn là “mỗi period nhân với `r`” mà là:

> instantaneous tỷ lệ (rate / 비율) of thay đổi (change / 변경) tỷ lệ với hiện tại (current / 현재) amount.

Viết bằng differential equation:

```math
\frac{dA}{dt}=kA.
```

`A(t)` là quantity tại thời gian (time / 시간) `t`; `k` là proportional growth tỷ lệ (rate / 비율) có đơn vị (unit / 단위) `1/time`.

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

Dùng initial điều kiện (condition / 조건) `A(0)=A_0` cho `C=A_0`, nên

```math
A(t)=A_0e^{kt}.
```

Số `e≈2.71828` không xuất hiện vì convention tùy ý. Exponential cơ sở (base / 기반) `e` là hàm (function / 함수) đặc biệt có derivative bằng chính nó:

```math
\frac{d}{dx}e^x=e^x.
```

Vì differential equation nói growth tỷ lệ (rate / 비율) proportional hiện tại (current / 현재) amount, `e^x` là biểu diễn (representation / 표현) tự nhiên nhất.

> **Chuyển mạch:** Trong **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Doubling thời gian (time / 시간) và logarithm** tiếp nhận điểm tựa từ **Continuous exponential: vì sao số e xuất hiện?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logarithm là inverse của exponentiation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Doubling thời gian (time / 시간) và logarithm

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

> **Chuyển mạch:** Ở chặng này của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Logarithm là inverse của exponentiation** tiếp nhận điểm tựa từ **Doubling thời gian (time / 시간) và logarithm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các luật logarithm đến từ luật exponent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logarithm là inverse của exponentiation

Definition

```math
\log_b x=y
```

nghĩa là

```math
b^y=x.
```

Vì vậy logarithm trả lời câu hỏi: “cơ sở (base / 기반) `b` phải được raise lên power nào để tạo `x`?”

Ví dụ

```math
\log_{10}1000=3
```

vì

```math
10^3=1000.
```

Natural logarithm `ln x` là logarithm cơ sở (base / 기반) `e`.

Logarithm chỉ nhận positive real đầu vào (input / 입력) khi làm việc trong real numbers:

```math
x>0.
```

Lý do là positive cơ sở (base / 기반) exponential `b^y` luôn positive, nên inverse real của nó chỉ có lĩnh vực (domain / 도메인) `(0,∞)`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Các luật logarithm đến từ luật exponent** tiếp nhận điểm tựa từ **Logarithm là inverse của exponentiation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao logarithm biến multiplication thành addition?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Các laws này không phải rules rời để memorise. Chúng là ảnh (image / 이미지) của exponent laws khi chuyển qua inverse thao tác (operation / 연산).

> **Chuyển mạch:** Trong **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Vì sao logarithm biến multiplication thành addition?** tiếp nhận điểm tựa từ **Các luật logarithm đến từ luật exponent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Compound interest** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao logarithm biến multiplication thành addition?

Đây là một insight quan trọng. Multiplication trong original quy mô (scale / 규모) trở thành addition trong log quy mô (scale / 규모):

```math
xy
\quad\longrightarrow\quad
\log x+\log y.
```

Điều này từng có giá trị computation lớn trước electronic calculators: log tables cho phép thay multiplication phức tạp bằng addition đơn giản hơn.

Trong hiện đại (modern / 현대적) computing, cùng cấu trúc (structure / 구조) vẫn quan trọng trong xác suất (probability / 확률). sản phẩm (product / 제품) của nhiều small probabilities dễ underflow:

```math
P=\prod_i p_i.
```

Lấy log:

```math
\log P=\sum_i\log p_i.
```

Vì vậy machine học tập (learning / 학습) và statistics thường tối ưu **log-likelihood** thay cho likelihood sản phẩm (product / 제품) trực tiếp.

> **Chuyển mạch:** Ở chặng này của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Compound interest** tiếp nhận điểm tựa từ **Vì sao logarithm biến multiplication thành addition?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy tắc (rule / 규칙) of 72 là approximation từ logarithm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compound interest

Với principal `P`, tỷ lệ (rate / 비율) `r` mỗi period và `n` periods:

```math
A=P(1+r)^n.
```

Nếu annual nominal tỷ lệ (rate / 비율) `r` được compounded `m` lần mỗi year trong `t` years:

```math
A=P\left(1+\frac rm\right)^{mt}.
```

Khi compounding frequency tăng vô hạn,

```math
\lim_{m\to\infty}\left(1+\frac rm\right)^{mt}=e^{rt},
```

nên continuous compounding mô hình (model / 모델) là

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Quy tắc (rule / 규칙) of 72 là approximation từ logarithm** tiếp nhận điểm tựa từ **Compound interest** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Semi-log plot: exponential trở thành line** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy tắc (rule / 규칙) of 72 là approximation từ logarithm

Doubling thời gian (time / 시간) discrete với tỷ lệ (rate / 비율) `r` mỗi period thỏa

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

Nếu tỷ lệ (rate / 비율) được viết bằng percent `p=100r`,

```math
T\approx\frac{69.3}{p}.
```

“quy tắc (rule / 규칙) of 72” thay `69.3` bằng `72` vì dễ chia và khá chính xác quanh nhiều rates thực tế. Đây là ví dụ một financial heuristic có nguồn gốc từ logarithmic approximation.

> **Chuyển mạch:** Trong **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Semi-log plot: exponential trở thành line** tiếp nhận điểm tựa từ **Quy tắc (rule / 규칙) of 72 là approximation từ logarithm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logarithmic scales và orders of magnitude** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Semi-log plot: exponential trở thành line

Nếu

```math
A=A_0e^{kt},
```

lấy natural log:

```math
\ln A=\ln A_0+kt.
```

Đây là tuyến tính (linear / 선형) quan hệ (relation / 관계) giữa `ln A` và `t`. Vì vậy exponential mẫu (pattern / 패턴) trở thành straight line trên semi-log plot.

Nhưng cần thận trọng: log-transform thay đổi lỗi (error / 오류) cấu trúc (structure / 구조). Nếu original đo lường (measurement / 측정) có additive Gaussian-like noise,

```math
Y=A_0e^{kt}+\varepsilon,
```

thì fitting `ln Y` bằng straight line không còn tương đương chính xác (exact / 정확한) với fitting original mô hình (model / 모델). Nếu noise là multiplicative,

```math
Y=A_0e^{kt}\eta,
```

log-transform lại tự nhiên hơn vì

```math
\ln Y=\ln A_0+kt+\ln\eta.
```

Modeling choice phải dựa trên data-generating cơ chế (mechanism / 메커니즘), không chỉ vì đồ thị (graph / 그래프) nhìn thẳng đẹp hơn.

> **Chuyển mạch:** Ở chặng này của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Logarithmic scales và orders of magnitude** tiếp nhận điểm tựa từ **Semi-log plot: exponential trở thành line** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **pH: logarithm biến concentration quy mô (scale / 규모) thành manageable numbers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logarithmic scales và orders of magnitude

Khi quantities trải qua nhiều powers of ten, tuyến tính (linear / 선형) axis khó đọc. Log quy mô (scale / 규모) compress magnitude theo ratio.

Trên base-10 log quy mô (scale / 규모), khoảng cách từ `1` đến `10` bằng khoảng cách từ `10` đến `100`, vì cả hai đều là multiplication by 10.

Đây là lý do logarithmic quy mô (scale / 규모) xuất hiện trong:

- decibel cho intensity ratio;
- pH cho hydrogen ion concentration;
- earthquake magnitude scales trong historical/dùng chung (common / 공통) formulations;
- thông tin (information / 정보) lý thuyết (theory / 이론) với logarithm của probabilities;
- thuật toán (algorithm / 알고리즘) độ phức tạp (complexity / 복잡도) như `O(log n)`.

Điểm chung không phải “các lĩnh vực này đều thích log”, mà là underlying cấu trúc (structure / 구조) có **multiplicative ratios hoặc repeated scaling**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **pH: logarithm biến concentration quy mô (scale / 규모) thành manageable numbers** tiếp nhận điểm tựa từ **Logarithmic scales và orders of magnitude** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decibel: measuring ratios chứ không phải absolute amount** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## pH: logarithm biến concentration quy mô (scale / 규모) thành manageable numbers

pH được định nghĩa gần dạng

```math
\mathrm{pH}=-\log_{10}[H^+].
```

Nếu hydrogen ion concentration giảm factor 10, pH tăng 1 đơn vị (unit / 단위).

Ví dụ:

```math
[H^+]=10^{-3}
```

cho pH khoảng `3`; còn

```math
[H^+]=10^{-5}
```

cho pH khoảng `5`.

Hai units pH tương ứng factor `100` concentration, không phải additive difference nhỏ. Log quy mô (scale / 규모) làm một phạm vi (range / 범위) cực rộng trở thành quy mô (scale / 규모) dễ thao tác.

> **Chuyển mạch:** Trong **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Decibel: measuring ratios chứ không phải absolute amount** tiếp nhận điểm tựa từ **pH: logarithm biến concentration quy mô (scale / 규모) thành manageable numbers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exponential và algorithmic growth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decibel: measuring ratios chứ không phải absolute amount

Một dùng chung (common / 공통) power-ratio form là

```math
L=10\log_{10}\left(\frac{P}{P_0}\right)\text{ dB}.
```

Nếu power ratio tăng factor 10, mức (level / 수준) tăng 10 dB. Logarithm biến multiplicative ratio thành additive mức (level / 수준) difference.

Cần chú ý công thức coefficient có thể khác với amplitude quantities vì power thường proportional amplitude squared. ngữ cảnh (context / 맥락) quyết định formula cụ thể.

> **Chuyển mạch:** Ở chặng này của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Exponential và algorithmic growth** tiếp nhận điểm tựa từ **Decibel: measuring ratios chứ không phải absolute amount** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logistic growth: khi exponential bị giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exponential và algorithmic growth

Không chỉ vật lý (physical / 물리적) quantities mới exponential. Nếu một thuật toán (algorithm / 알고리즘) enumerate tất cả nhị phân (binary / 이진) assignments của `n` Boolean variables, số possibilities là

```math
2^n.
```

Tăng `n` thêm 1 làm tìm kiếm (search / 검색) không gian (space / 공간) nhân đôi.

Ngược lại, nếu thuật toán (algorithm / 알고리즘) mỗi step chia bài toán (problem / 문제) kích thước (size / 크기) đôi,

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

Tìm kiếm nhị phân (binary search / 이진 탐색) có logarithmic độ sâu (depth / 깊이) vì mỗi comparison loại bỏ một fraction lớn của tìm kiếm (search / 검색) không gian (space / 공간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Exponential và algorithmic growth** đã nêu tiêu chí phân biệt, còn **Logistic growth: khi exponential bị giới hạn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Exponential as eigenfunction of differentiation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logistic growth: khi exponential bị giới hạn

Pure exponential mô hình (model / 모델) ngầm giả định growth factor không suy giảm khi quantity lớn. Trong population các hệ thống (systems / 시스템들) hoặc resource-limited processes, giả định (assumption / 가정) đó thường sai.

Một simple correction là logistic differential equation:

```math
\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right).
```

`r` là intrinsic growth tỷ lệ (rate / 비율); `K` là carrying sức chứa (capacity / 용량).

Khi `P≪K`, factor

```math
1-\frac{P}{K}\approx1,
```

nên hệ thống (system / 시스템) gần exponential:

```math
\frac{dP}{dt}\approx rP.
```

Khi `P→K`, factor tiến về `0`, growth slow và equilibrium xuất hiện.

Đây là ví dụ quan trọng về mô hình (model / 모델) refinement: exponential không “sai”, nhưng chỉ đúng trong regime nơi tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건) chưa đáng kể.

> **Chuyển mạch:** Trong **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Logistic growth: khi exponential bị giới hạn** đã nêu tiêu chí phân biệt, còn **Exponential as eigenfunction of differentiation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Exponential family không có nghĩa mọi rapid growth là exponential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exponential as eigenfunction of differentiation

Một thuộc tính (property / 속성) sâu hơn là exponential giữ nguyên shape dưới differentiation:

```math
\frac{d}{dx}e^{kx}=ke^{kx}.
```

Differentiation chỉ quy mô (scale / 규모) hàm (function / 함수) bởi `k`. Vì thế exponential đóng vai trò tương tự eigenvector nhưng trong hàm (function / 함수) không gian (space / 공간): nó là một eigenfunction của derivative operator.

Liên kết (connection / 연결) này giải thích tại sao exponentials xuất hiện tự nhiên khi solve tuyến tính (linear / 선형) differential equations, Fourier/Laplace methods, điều khiển (control / 제어) các hệ thống (systems / 시스템들) và tín hiệu (signal / 신호) processing.

> **Chuyển mạch:** Ở chặng này của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Exponential family không có nghĩa mọi rapid growth là exponential** tiếp nhận điểm tựa từ **Exponential as eigenfunction of differentiation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결) — logarithm và thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exponential family không có nghĩa mọi rapid growth là exponential

Một curve tăng nhanh chưa đủ chứng minh exponential. Polynomial `x^10` có thể trông rất steep trên một interval nhỏ. Super-exponential processes như `e^{t^2}` còn tăng nhanh hơn.

Để gọi một tiến trình (process / 프로세스) exponential, ta cần structural reason hoặc dữ liệu (data / 데이터) bằng chứng (evidence / 증거) cho roughly constant relative growth tỷ lệ (rate / 비율):

```math
\frac{1}{A}\frac{dA}{dt}\approx k.
```

Đây là diagnostic bản chất: relative tỷ lệ (rate / 비율) constant tạo exponential.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, sau nội dung của **Exponential family không có nghĩa mọi rapid growth là exponential**, **Liên kết kiến thức (knowledge connection / 지식 연결) — logarithm và thông tin (information / 정보)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결) — logarithm và thông tin (information / 정보)

Nếu một sự kiện (event / 이벤트) có xác suất (probability / 확률) `p`, thông tin (information / 정보) content thường mô hình (model / 모델) bằng

```math
I=-\log p.
```

Rare sự kiện (event / 이벤트) (`p` nhỏ) mang nhiều surprise/thông tin (information / 정보) hơn. Logarithm được dùng vì independent probabilities multiply:

```math
p(A,B)=p(A)p(B),
```

trong khi thông tin (information / 정보) ta muốn add:

```math
I(A,B)=I(A)+I(B).
```

Logarithm chính là hàm (function / 함수) biến sản phẩm (product / 제품) thành sum. Đây là reason structural, không phải convention ngẫu nhiên.

> **Chuyển mạch:** Trong **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결) — logarithm và thông tin (information / 정보)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Exponential là toán học của repeated proportional thay đổi (change / 변경): cùng một **tỷ lệ**, không phải cùng một **lượng**, được áp dụng liên tục hoặc lặp lại. Logarithm quay ngược quá trình đó để đo số lần scaling, thời gian cần đạt threshold hoặc thứ tự (order / 순서) of magnitude. Khi thấy multiplication lặp, percentage compounding, constant relative tỷ lệ (rate / 비율) hoặc tìm kiếm (search / 검색) không gian (space / 공간) co theo ratio, hãy nghĩ đến exponential/logarithm như một cặp inverse.

> **Chuyển mạch:** Ở chặng này của **Hàm mũ và logarithm: toán học của tăng trưởng theo tỷ lệ**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Exponential chỉ nghĩa là tăng rất nhanh.”** Không. Exponential là một specific structural law. Rapid polynomial growth vẫn không phải exponential.

**“Tăng 10% trong hai năm nghĩa tăng 20%.”** Chỉ đúng gần đúng với small rates/short horizon. chính xác (exact / 정확한) compounding là `1.1²=1.21`, tức 21%.

**“Logarithm chỉ là một nút trên calculator.”** Logarithm đo exponent/multiplicative độ sâu (depth / 깊이) và biến products thành sums. Đây là reason nó xuất hiện trong độ phức tạp (complexity / 복잡도), thông tin (information / 정보) lý thuyết (theory / 이론), likelihood và scientific scales.

**“Log-transform luôn làm dữ liệu (data / 데이터) tuyến tính.”** Chỉ một số functional forms như exponential hoặc power laws trở thành tuyến tính (linear / 선형) trong coordinates thích hợp. Arbitrary nonlinear quan hệ (relation / 관계) không tự biến thành tuyến tính (linear / 선형).

**“Exponential growth có thể tiếp tục vô hạn trong vật lý (physical / 물리적) hệ thống (system / 시스템).”** Mathematical mô hình (model / 모델) cho phép, nhưng vật lý (physical / 물리적) resources thường tạo saturation, phản hồi (feedback / 피드백) hoặc regime thay đổi (change / 변경). mô hình (model / 모델) validity phải được kiểm tra, không extrapolate vô hạn chỉ vì curve fit ban đầu tốt.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
