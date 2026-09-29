# Lũy thừa, căn và logarithm: multiplicative cấu trúc (structure / 구조) và inverse scales

> **Mạch đọc:** Đọc **Lũy thừa, căn và logarithm: multiplicative cấu trúc (structure / 구조) và inverse scales** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Từ repeated addition đến repeated multiplication** sang **2. Vì sao exponent laws tồn tại?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Lũy thừa (power / 거듭제곱), căn (root / 근) và logarithm (로그) không phải ba chủ đề tách rời. Chúng là ba cách đọc cùng một relationship:

```math
b^x=y.
```

Nếu biết `b` và `x`, ta tính `y`: đó là exponentiation. Nếu biết `x` và `y`, ta hỏi giá trị base-like phù hợp: đó dẫn tới roots. Nếu biết `b` và `y`, ta hỏi exponent cần thiết: đó là logarithm.

Điểm sâu hơn là cả ba thuộc **multiplicative cấu trúc (structure / 구조)**. Chúng mô tả các hệ thống (systems / 시스템들) nơi quy mô (scale / 규모) thay đổi bằng factors, không phải fixed differences.

## 1. Từ repeated addition đến repeated multiplication

Multiplication có thể được xem như repeated addition trong integer setting:

```math
5\cdot3=5+5+5.
```

Exponentiation tiếp tục mẫu (pattern / 패턴) bằng repeated multiplication:

```math
b^n=\underbrace{b\cdot b\cdots b}_{n\text{ factors}}.
```

Nếu `b>1`, repeated multiplication tạo growth nhanh hơn tuyến tính (linear / 선형) growth vì mỗi step quy mô (scale / 규모) toàn bộ quantity hiện tại.

Ví dụ doubling:

```text
1, 2, 4, 8, 16, 32, ...
```

sau `n` doublings:

```math
2^n.
```

Đây là cấu trúc (structure / 구조) phía sau compound interest, population các mô hình (models / 모델들), nhị phân (binary / 이진) trees và many divide/multiply processes.

## 2. Vì sao exponent laws tồn tại?

Với positive integers:

```math
b^m b^n
```

chỉ là sản phẩm (product / 제품) có tổng cộng `m+n` factors `b`, nên

```math
b^m b^n=b^{m+n}.
```

Tương tự,

```math
(b^m)^n=b^{mn}
```

vì ta lặp một sản phẩm (product / 제품) có `m` factors tổng cộng `n` lần.

Các exponent laws không nên được học như bảng rules; chúng đến từ counting multiplicative factors.

## 3. Tại sao exponent 0 bằng 1?

Ta muốn law

```math
\frac{b^m}{b^n}=b^{m-n}
```

vẫn nhất quán khi `m=n`.

Left side:

```math
\frac{b^n}{b^n}=1,
```

nên ta cần

```math
b^0=1,\qquad b\ne0.
```

Đây là consistency extension: definition của exponent được mở rộng để giữ algebraic cấu trúc (structure / 구조).

## 4. Negative exponents là inverse scaling

Muốn law

```math
b^m b^n=b^{m+n}
```

vẫn đúng với `n=-m`, ta cần

```math
b^m b^{-m}=b^0=1.
```

Do đó

```math
b^{-m}=\frac1{b^m}.
```

Negative exponent không nghĩa “negative multiplication”; nó nghĩa multiplicative inverse.

Ví dụ:

```math
10^{-3}=\frac1{1000}=0.001.
```

Scientific notation dựa trực tiếp trên idea này.

## 5. Fractional exponents và roots

Ta muốn

```math
(b^{1/n})^n=b.
```

Do exponent multiplication law, điều này gợi ý

```math
b^{1/n}=\sqrt[n]{b}
```

trong lĩnh vực (domain / 도메인) phù hợp.

Do đó

```math
b^{m/n}=\sqrt[n]{b^m}.
```

Với real numbers, lĩnh vực (domain / 도메인) cần cẩn thận: even gốc (root / 루트) của negative real không tồn tại trong `\mathbb R`, nhưng tồn tại trong complex numbers.

Fractional exponents vì vậy nối number các hệ thống (systems / 시스템들) với exponent laws.

## 6. Exponential hàm (function / 함수) khác polynomial growth như thế nào?

So sánh

```math
x^3
```

và

```math
2^x.
```

Trong polynomial, variable nằm ở cơ sở (base / 기반). Trong exponential, variable nằm ở exponent.

Khi `x` lớn, exponential với cơ sở (base / 기반) `>1` cuối cùng vượt mọi fixed-degree polynomial. Đây là lý do exponential-time algorithms trở nên infeasible cực nhanh.

Ví dụ:

```math
2^{100}\approx1.27\times10^{30}.
```

Không có micro-optimization thông thường nào cứu được việc enumerate tất cả `2^100` possibilities.

## 7. Logarithm là inverse của exponential

Definition:

```math
\log_b y=x
\iff
b^x=y,
```

với real logarithm yêu cầu

```math
b>0,\qquad b\ne1,\qquad y>0.
```

Logarithm trả lời câu hỏi:

> Cần bao nhiêu multiplicative steps ở cơ sở (base / 기반) `b` để đi từ quy mô (scale / 규모) 1 tới quy mô (scale / 규모) `y`?

Ví dụ:

```math
\log_2 8=3
```

vì ba doublings đưa 1 thành 8.

## 8. Vì sao log biến sản phẩm (product / 제품) thành sum?

Giả sử

```math
x=b^m,\qquad y=b^n.
```

Khi đó

```math
xy=b^{m+n}.
```

Lấy log cơ sở (base / 기반) `b`:

```math
\log_b(xy)=m+n
```

và vì

```math
m=\log_bx,\qquad n=\log_by,
```

nên

```math
\log_b(xy)=\log_bx+\log_by.
```

Log law xuất phát trực tiếp từ exponent law. sản phẩm (product / 제품) trở thành sum vì logarithm đo exponent độ sâu (depth / 깊이).

Tương tự:

```math
\log_b(x^k)=k\log_bx.
```

## 9. thay đổi (change / 변경) of cơ sở (base / 기반): vì sao cơ sở (base / 기반) chỉ thay quy mô (scale / 규모)

Từ

```math
b^x=y
```

lấy natural log:

```math
x\ln b=\ln y,
```

nên

```math
\log_b y=\frac{\ln y}{\ln b}.
```

Các log bases khác nhau chỉ khác nhau bởi constant quy mô (scale / 규모) factor. Đây là lý do trong Big-O,

```math
\log_2 n
```

và

```math
\ln n
```

cùng asymptotic thứ tự (order / 순서).

## 10. cơ sở (base / 기반) `e` xuất hiện từ continuous thay đổi (change / 변경)

Natural exponential

```math
e^x
```

đặc biệt vì

```math
\frac{d}{dx}e^x=e^x.
```

Nếu quantity có instantaneous growth tỷ lệ (rate / 비율) proportional với chính nó,

```math
\frac{dA}{dt}=kA,
```

solution có dạng

```math
A(t)=A_0e^{kt}.
```

Do đó `e` không chỉ là một constant lạ. Nó là cơ sở (base / 기반) tự nhiên khi multiplicative thay đổi (change / 변경) xảy ra continuously.

## 11. Compound growth và solving time-to-target

Nếu growth mỗi period là `r`,

```math
A_n=A_0(1+r)^n.
```

Muốn tìm `n` để đạt mục tiêu (target / 대상) `A`:

```math
A=A_0(1+r)^n.
```

Chia cho `A_0`:

```math
\frac A{A_0}=(1+r)^n.
```

Lấy log:

```math
n=\frac{\ln(A/A_0)}{\ln(1+r)}.
```

Unknown nằm trong exponent nên logarithm là inverse thao tác (operation / 연산) tự nhiên.

### Worked example

Một khoản đầu tư tăng 8% mỗi năm. Cần bao lâu để tăng gấp đôi?

```math
2=(1.08)^n.
```

Suy ra

```math
n=\frac{\ln2}{\ln1.08}\approx9.0.
```

Đây là nguồn gốc định lượng của quy tắc (rule / 규칙) of 72 approximation.

## 12. Half-life và exponential decay

Nếu quantity giảm theo

```math
A(t)=A_0e^{-kt},
```

half-life `T_{1/2}` thỏa

```math
\frac{A_0}{2}=A_0e^{-kT_{1/2}}.
```

Do đó

```math
T_{1/2}=\frac{\ln2}{k}.
```

Cùng algebra áp dụng cho radioactive decay, pharmacokinetics, capacitor discharge và nhiều relaxation processes.

## 13. `O(log n)` đến từ repeated shrinking

Nếu mỗi step giảm bài toán (problem / 문제) kích thước (size / 크기) bởi factor `b>1`:

```math
n,\frac nb,\frac n{b^2},\ldots
```

sau `k` steps còn khoảng 1:

```math
\frac{n}{b^k}\approx1.
```

Suy ra

```math
k\approx\log_b n.
```

Tìm kiếm nhị phân (binary search / 이진 탐색) là example điển hình. `O(log n)` không có nghĩa mã (code / 코드) phải gọi một `log()` hàm (function / 함수); logarithm xuất hiện từ **number of multiplicative reductions**.

## 14. Log scales trong đo lường (measurement / 측정)

Khi values trải nhiều orders of magnitude, tuyến tính (linear / 선형) quy mô (scale / 규모) có thể khó đọc. Logarithmic scales chuyển ratios thành differences.

### Decibel

Với power ratio:

```math
L=10\log_{10}\left(\frac{P}{P_0}\right)\text{ dB}.
```

Một factor `10` về power tương ứng +10 dB.

### pH

pH là ví dụ cho logarithm biến một range nồng độ rất rộng thành thang đo dễ đọc. Hãy giữ dấu âm, base và ý nghĩa hóa học của đại lượng trước khi áp dụng công thức.

```math
pH=-\log_{10}[H^+].
```

Concentration tăng factor 10 làm pH giảm 1.

Log scales rất hữu ích, nhưng interpretation phải giữ quan hệ (relation / 관계) với original multiplicative quy mô (scale / 규모).

## 15. thông tin (information / 정보) lý thuyết (theory / 이론): surprise là logarithmic

Thông tin (information / 정보) content thường được viết

```math
I(x)=-\log_2P(x).
```

Nếu hai independent events có probabilities multiply,

```math
P(A\cap B)=P(A)P(B),
```

thì thông tin (information / 정보) adds:

```math
I(A,B)=I(A)+I(B).
```

Logarithm là hàm (function / 함수) tự nhiên vì nó biến multiplicative xác suất (probability / 확률) cấu trúc (structure / 구조) thành additive thông tin (information / 정보).

## 16. Numerical computing: tại sao dùng log-probability?

Trong statistics/AI, likelihood của many independent observations thường là sản phẩm (product / 제품):

```math
L(\theta)=\prod_i p(x_i\mid\theta).
```

Sản phẩm (product / 제품) của nhiều số nhỏ có thể underflow floating điểm (point / 지점). Lấy log:

```math
\log L(\theta)=\sum_i\log p(x_i\mid\theta).
```

Ta vừa biến sản phẩm (product / 제품) thành sum, vừa cải thiện numerical hành vi (behavior / 동작).

Đây là example rõ của algebraic định danh (identity / 식별자) trở thành kỹ thuật (engineering / 엔지니어링) technique.

## 17. dùng chung (common / 공통) thất bại (failure / 실패) modes

### `\log(a+b)` không phân phối qua addition

Không có quy tắc (rule / 규칙)

```math
\log(a+b)=\log a+\log b.
```

Log laws đến từ multiplication/exponent cấu trúc (structure / 구조), không phải arbitrary algebraic simplification.

### Gốc (root / 루트) và exponent có lĩnh vực (domain / 도메인) subtleties

Ví dụ

```math
\sqrt{x^2}=|x|,
```

không phải luôn `x`. Square gốc (root / 루트) convention trả nonnegative principal gốc (root / 루트) trong real numbers.

### Exponential mô hình (model / 모델) không thể dùng vô hạn

Một hệ thống (system / 시스템) có finite resources thường không thể grow exponential mãi. Logistic các mô hình (models / 모델들) hoặc saturation mechanisms có thể cần thiết.

## Applications và connections

**Khoa học máy tính (computer science / 컴퓨터 과학):** tìm kiếm nhị phân (binary search / 이진 탐색), cây (tree / 트리) height, exponential trạng thái (state / 상태) spaces, logarithmic dữ liệu (data / 데이터) structures.

**Physics:** radioactive decay, oscillation envelopes, thermodynamics/statistical mechanics scales.

**AI:** log-likelihood, cross-entropy, softmax stabilization, exponential families.

**Finance:** compound returns, discounting, continuously compounded rates, time-to-target calculations.

## Mô hình tư duy (mental model / 사고 모델)

> Powers describe multiplicative accumulation. Roots undo a known power. Logarithms measure multiplicative độ sâu (depth / 깊이). Whenever a hệ thống (system / 시스템) changes by ratios, factors, repeated halving/doubling or compounding, exponentials and logarithms are the natural ngôn ngữ (language / 언어).

## Dùng chung (common / 공통) Misconceptions

**Exponent rules là arbitrary formulas.** Không; chúng encode how multiplicative factors combine.

**Negative exponent là negative giá trị (value / 값).** Không; nó means reciprocal scaling.

**Logarithm chỉ dùng để solve equations.** Không; nó là coordinate hệ thống (system / 시스템) tự nhiên cho multiplicative processes và thông tin (information / 정보).

**`O(log n)` nghĩa “rất nhanh” trong mọi setting.** Không; nó mô tả asymptotic scaling trong một chi phí (cost / 비용) mô hình (model / 모델). Constants, bộ nhớ (memory / 메모리) truy cập (access / 접근) và I/O vẫn matter.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 algebraic language](./00_algebraic_language.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
