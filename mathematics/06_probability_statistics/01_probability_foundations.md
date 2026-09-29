# Nền tảng xác suất: mô hình hóa bất định bằng events, thông tin (information / 정보) và các giả định (assumptions / 가정들)

> **Mạch đọc:** Đọc **Nền tảng xác suất: mô hình hóa bất định bằng events, thông tin (information / 정보) và các giả định (assumptions / 가정들)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **mẫu (sample / 표본) không gian (space / 공간): universe của mô hình (model / 모델), không nhất thiết universe của reality** sang **xác suất (probability / 확률) axioms tồn tại để giữ lập luận (reasoning / 추론) nhất quán**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Xác suất (probability / 확률) không phải là cách làm cho thế giới “ít ngẫu nhiên hơn”. Nó là một ngôn ngữ (language / 언어) để mô tả **bất định (uncertainty / 불확실성) có cấu trúc (structure / 구조)**. Trước khi hỏi một xác suất (probability / 확률) bằng bao nhiêu, phải hỏi ba câu:

1. kết quả (outcome / 결과) không gian (space / 공간) nào đang được mô hình (model / 모델)?
2. sự kiện (event / 이벤트) nào ta quan tâm?
3. thông tin (information / 정보) và các giả định (assumptions / 가정들) nào đang được dùng?

Một con số như `70%` không có nghĩa nếu sự kiện (event / 이벤트) và thông tin (information / 정보) set chưa được định nghĩa.

## Mẫu (sample / 표본) không gian (space / 공간): universe của mô hình (model / 모델), không nhất thiết universe của reality

Không gian mẫu (sample space / 표본공간) `\Omega` là set outcomes mà mô hình (model / 모델) cho phép.

Với một coin toss:

```math
\Omega=\{H,T\}.
```

Với hai tosses:

```math
\Omega=\{HH,HT,TH,TT\}.
```

Một sự kiện (event / 이벤트) là subset của `\Omega`. sự kiện (event / 이벤트) “exactly one head” là

```math
\{HT,TH\}.
```

Điểm subtle: mẫu (sample / 표본) không gian (space / 공간) là modeling choice. Nếu ta mô hình (model / 모델) độ trễ (latency / 지연 시간) chỉ bằng categories `{fast, slow}`, ta đã bỏ nhiều detail so với continuous milliseconds. xác suất (probability / 확률) conclusions chỉ đúng trong biểu diễn (representation / 표현) đã chọn.

## Xác suất (probability / 확률) axioms tồn tại để giữ lập luận (reasoning / 추론) nhất quán

Xác suất (probability / 확률) measure `P` phải thỏa:

```math
P(A)\ge0,
```

```math
P(\Omega)=1,
```

và với pairwise-disjoint events `A_i`:

```math
P\left(\bigcup_iA_i\right)
=
\sum_iP(A_i).
```

Từ ba axioms này, nhiều rules quen thuộc được derive thay vì memorize.

Vì `A` và `A^c` disjoint và union thành `\Omega`:

```math
P(A)+P(A^c)=1,
```

nên

```math
P(A^c)=1-P(A).
```

Với two events:

```math
P(A\cup B)
=P(A)+P(B)-P(A\cap B),
```

vì intersection bị double-count nếu chỉ cộng hai probabilities.

## Equally likely formula là special trường hợp (case / 사례)

Nếu finite outcomes equally likely:

```math
P(A)=\frac{|A|}{|\Omega|}.
```

Nhưng đây không phải definition chung của xác suất (probability / 확률). Nó chỉ đúng sau khi giả định (assumption / 가정) “equally likely” được justify.

Một loaded die, thị trường (market / 시장) return hay máy chủ (server / 서버) thất bại (failure / 실패) không có outcomes tự nhiên equally likely. xác suất (probability / 확률) phải đến từ cơ chế (mechanism / 메커니즘), empirical mô hình (model / 모델), symmetry hoặc suy luận (inference / 추론).

## Worked example — inclusion-exclusion từ set lập luận (reasoning / 추론)

Trong 1,000 users:

- 420 dùng tính năng (feature / 기능) A;
- 350 dùng tính năng (feature / 기능) B;
- 120 dùng cả hai.

Xác suất (probability / 확률) một randomly sampled người dùng (user / 사용자) dùng ít nhất một tính năng (feature / 기능):

```math
P(A\cup B)
=
0.42+0.35-0.12
=0.65.
```

Nếu chỉ cộng 0.42 và 0.35, overlap bị count twice. xác suất (probability / 확률) union quy tắc (rule / 규칙) chính là set inclusion-exclusion được normalize thành measure.

## Conditional xác suất (probability / 확률): xác suất (probability / 확률) luôn phụ thuộc thông tin (information / 정보)

Xác suất có điều kiện (conditional probability / 조건부확률) của `A` khi biết `B` xảy ra:

```math
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)},
\qquad P(B)>0.
```

Interpretation: khi biết `B`, universe relevant thu hẹp từ `\Omega` xuống `B`; ta renormalize xác suất (probability / 확률) mass trong `B` về total 1.

Từ definition:

```math
P(A\cap B)=P(A\mid B)P(B).
```

Và đối xứng:

```math
P(A\cap B)=P(B\mid A)P(A).
```

Equate hai expressions để derive Bayes:

```math
P(A\mid B)
=
\frac{P(B\mid A)P(A)}{P(B)}.
```

Bayes không phải magic inversion; nó chỉ là intersection được factor theo hai directions khác nhau.

## Worked Bayes example — cơ sở (base / 기반) tỷ lệ (rate / 비율) matters

Suppose disease prevalence là 1%. kiểm thử (test / 테스트) có sensitivity 95% và false-positive tỷ lệ (rate / 비율) 5%.

Trong 10,000 people, expected counts:

```text
Disease:        100
Positive among disease: 95
No disease:   9,900
False positives: 495
```

Among positive tests, disease cases khoảng

```math
\frac{95}{95+495}\approx0.161.
```

Positive kiểm thử (test / 테스트) không imply 95% chance disease. Sensitivity `P(+|D)` khác posterior `P(D|+)`. cơ sở (base / 기반) tỷ lệ (rate / 비율) quyết định denominator.

## Independence: một structural giả định (assumption / 가정), không phải cảm giác “không liên quan”

Events `A,B` independent nếu

```math
P(A\cap B)=P(A)P(B).
```

Equivalent khi probabilities positive:

```math
P(A\mid B)=P(A).
```

Nghĩa là biết `B` không thay xác suất (probability / 확률) của `A` trong mô hình (model / 모델).

Independence khác mutual exclusivity. Nếu `A` và `B` mutually exclusive với positive probabilities, occurrence của `B` làm xác suất (probability / 확률) `A` thành zero, nên chúng strongly dependent.

## Pairwise independence chưa chắc mutual independence

Nhiều events có thể pairwise independent nhưng không jointly independent. Vì vậy trong high-dimensional các mô hình (models / 모델들), statement “independent” phải rõ mức (level / 수준) và conditioning ngữ cảnh (context / 맥락).

Conditional independence đặc biệt quan trọng trong Bayesian networks, graphical các mô hình (models / 모델들) và nhân quả (causal / 인과적) suy luận (inference / 추론):

```math
X\perp Y\mid Z.
```

Nó nói sau khi biết `Z`, `X` không cung cấp thêm thông tin (information / 정보) về `Y` trong mô hình (model / 모델).

## Why multiplication appears in repeated trials

Nếu trials independent với success xác suất (probability / 확률) `p`, xác suất (probability / 확률) của specific chuỗi (sequence / 시퀀스) có `k` successes và `n-k` failures là

```math
p^k(1-p)^{n-k}.
```

Multiplication đến từ repeated conditional factorization under independence.

Binomial xác suất (probability / 확률) thêm combinatorial factor `\binom nk` vì có nhiều sequences tạo cùng count `k`.

Xác suất (probability / 확률) và combinatorics gặp nhau ở đây: counting tells how many paths, xác suất (probability / 확률) tells weight mỗi đường dẫn (path / 경로).

## Frequency interpretation và law of large numbers

Nếu repeat một stable random experiment nhiều lần, mẫu (sample / 표본) average/frequency thường converge về expectation/xác suất (probability / 확률) dưới suitable các giả định (assumptions / 가정들).

Điều này giải thích vì sao xác suất (probability / 확률) có empirical meaning. Nhưng convergence không nghĩa short-term balancing.

Sau 10 tails liên tiếp của fair coin, next toss vẫn

```math
P(H)=0.5.
```

Belief “heads is now due” là gambler's fallacy: nó nhầm long-run frequency convergence với short-run compensating force.

## Bayesian viewpoint: bất định (uncertainty / 불확실성) given hiện tại (current / 현재) thông tin (information / 정보)

Bayesian xác suất (probability / 확률) dùng xác suất (probability / 확률) để encode bất định (uncertainty / 불확실성) về unknown states/parameters. Khi bằng chứng (evidence / 증거) mới đến:

```math
posterior
\propto
likelihood\times prior.
```

Frequentist khung phần mềm (framework / 프레임워크) khác về interpretation của parameters và xác suất (probability / 확률) statements, nhưng share axioms và much of the same xác suất (probability / 확률) calculus.

Không nên biến hai frameworks thành slogans. Mỗi one answers suy luận (inference / 추론) questions với các giả định (assumptions / 가정들) và procedures khác nhau.

## Expected giá trị (value / 값): probability-weighted balance điểm (point / 지점)

Cho discrete random variable `X`:

```math
E[X]=\sum_x xP(X=x).
```

Expectation không nhất thiết là possible kết quả (outcome / 결과). Fair die có expectation 3.5 dù không bao giờ roll 3.5.

Expectation là tuyến tính (linear / 선형):

```math
E[aX+bY]=aE[X]+bE[Y]
```

không cần independence.

Đây là reason expected chi phí (cost / 비용)/revenue often easy to decompose.

## Worked Finance example — expected return không đủ mô tả rủi ro (risk / 위험)

Investment A returns `+10%` chắc chắn. Investment B returns `+30%` với xác suất (probability / 확률) 0.5 và `-10%` với xác suất (probability / 확률) 0.5.

Both have expected return 10%:

```math
E[R_B]=0.5(0.30)+0.5(-0.10)=0.10.
```

Nhưng distributions khác hoàn toàn. Expected giá trị (value / 값) alone loses variance, tail and đường dẫn (path / 경로) thông tin (information / 정보).

Xác suất (probability / 확률) mô hình (model / 모델) phải match quyết định (decision / 결정) question; một scalar expectation hiếm khi đủ cho rủi ro (risk / 위험) management.

## Calibration: xác suất (probability / 확률) forecast nên được kiểm tra thế nào?

Nếu mô hình (model / 모델) đưa xác suất (probability / 확률) khoảng 0.7 cho nhiều comparable cases, một calibrated mô hình (model / 모델) sẽ thấy sự kiện (event / 이벤트) xảy ra roughly 70% trong nhóm đó over repeated samples.

Calibration khác discrimination. mô hình (model / 모델) có thể rank risks tốt nhưng probabilities badly calibrated.

Trong AI classification, medical rủi ro (risk / 위험), weather forecast và credit rủi ro (risk / 위험), distinction này quan trọng.

## Common-cause dependence trong kỹ thuật (engineering / 엔지니어링)

Suppose two servers each thất bại (failure / 실패) xác suất (probability / 확률) 1%. Nếu independent, xác suất (probability / 확률) cả hai thất bại (fail / 실패) là

```math
0.01^2=0.0001.
```

Nhưng nếu cả hai share same power supply hoặc mạng (network / 네트워크), failures correlated. Multiplying 1%×1% underestimates systemic rủi ro (risk / 위험).

Independence là giả định (assumption / 가정) phải justify, không phải default convenience.

## Xác suất (probability / 확률) zero không luôn nghĩa impossible

Với continuous phân phối (distribution / 분포):

```math
P(X=x)=0
```

cho every chính xác (exact / 정확한) điểm (point / 지점), nhưng một realized `X` vẫn nhận một chính xác (exact / 정확한) giá trị (value / 값). xác suất (probability / 확률) zero sự kiện (event / 이벤트) trong continuous mathematics không đồng nghĩa logical impossibility.

Đây là cầu nối (bridge / 브리지) tới measure-theoretic xác suất (probability / 확률).

## Khoa học máy tính (computer science / 컴퓨터 과학), AI và thông tin (information / 정보) lý thuyết (theory / 이론) connections

Randomized algorithms analyze expected thời gian chạy (runtime / 런타임) và thất bại (failure / 실패) xác suất (probability / 확률). băm (hash / 해시) collisions, Bloom filters, phân tán (distributed / 분산) retries và sampling đều dựa xác suất (probability / 확률) các giả định (assumptions / 가정들).

Machine học tập (learning / 학습) dùng conditional distributions like

```math
P(Y\mid X).
```

Thông tin (information / 정보) lý thuyết (theory / 이론) dùng

```math
-\log P(x)
```

để đo surprisal. Rare outcomes carry more thông tin (information / 정보) under the mô hình (model / 모델).

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Xác suất (probability / 확률) statements depend on sự kiện (event / 이벤트) definition, conditioning thông tin (information / 정보) và mô hình (model / 모델) stability. phân phối (distribution / 분포) shift phá historical probabilities. Selection độ lệch (bias / 편향) làm observed frequencies không represent mục tiêu (target / 대상) population. Hidden variables phá independence. Small samples tạo high bất định (uncertainty / 불확실성) ngay cả khi điểm (point / 지점) estimate nhìn precise.

Một xác suất (probability / 확률) mô hình (model / 모델) tốt phải nói cả number **và** các giả định (assumptions / 가정들) đã tạo number đó.

## Mô hình tư duy (mental model / 사고 모델)

> xác suất (probability / 확률) là bookkeeping nhất quán cho bất định (uncertainty / 불확실성). mẫu (sample / 표본) không gian (space / 공간) nói những outcomes nào mô hình (model / 모델) cho phép; events gom outcomes thành câu hỏi; conditioning thay đổi thông tin (information / 정보) set; independence là structural simplification; Bayes chỉ re-express cùng joint xác suất (probability / 확률) khi bằng chứng (evidence / 증거) thay đổi. xác suất (probability / 확률) không tồn tại trong vacuum — nó luôn gắn với mô hình (model / 모델) và thông tin (information / 정보).

## Dùng chung (common / 공통) Misconceptions

**“xác suất (probability / 확률) 70% nghĩa sự kiện (event / 이벤트) sẽ xảy ra 70 lần trong đúng 100 trials.”** Không; đó là long-run/calibration statement under repeated comparable conditions, không guarantee một khối (block / 블록) cụ thể.

**“Mutually exclusive nghĩa independent.”** Ngược lại, positive-probability mutually exclusive events are dependent.

**“Sau một streak, random tiến trình (process / 프로세스) phải bù.”** Không nếu trials independent.

**“Positive kiểm thử (test / 테스트) 95% accurate nghĩa 95% chance disease.”** Posterior còn phụ thuộc cơ sở (base / 기반) tỷ lệ (rate / 비율) và false positives.

**“Hai các hệ thống (systems / 시스템들) trông unrelated nên failures independent.”** dùng chung (shared / 공유) hidden causes có thể tạo dependence mạnh.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 counting and combinatorics](./00_counting_and_combinatorics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
