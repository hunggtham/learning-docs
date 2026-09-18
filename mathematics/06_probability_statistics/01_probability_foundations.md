# Nền tảng xác suất: mô hình hóa bất định

Xác suất (Probability / 확률) không loại bỏ bất định; nó gán structure định lượng cho những outcomes chưa biết. Một probability model bắt đầu bằng sample space, events và rule gán probability.

## Sample space và event

Không gian mẫu (Sample space / 표본공간) `Ω` là set all outcomes trong model. Event (사건) là subset của `Ω`.

Với coin toss:

```math
\Omega=\{H,T\}
```

Event “heads” là `{H}`.

Với hai tosses:

```math
\Omega=\{HH,HT,TH,TT\}
```

Event “exactly one head” là `{HT,TH}`.

## Probability axioms

Probability measure `P` thỏa:

```math
P(A)\ge0
```

```math
P(\Omega)=1
```

và với disjoint events `A_i`:

```math
P\left(\bigcup_i A_i\right)=\sum_iP(A_i)
```

Từ đó derive complement:

```math
P(A^c)=1-P(A)
```

và union:

```math
P(A\cup B)=P(A)+P(B)-P(A\cap B)
```

## Equally likely outcomes

Nếu finite outcomes equally likely:

```math
P(A)=\frac{|A|}{|\Omega|}
```

Nhưng formula này không phải definition universal của probability. Real-world outcomes hiếm khi tự nhiên equally likely. Ta cần model/data để gán probabilities.

## Frequency interpretation

Trong repeated trials under stable conditions, relative frequency thường tiến gần probability theo law of large numbers. Nếu coin fair, fraction heads quanh 0.5 khi number trials lớn.

Điều này không nghĩa sequence phải “bù” ngắn hạn. Sau 10 tails liên tiếp, next fair toss vẫn probability heads 0.5.

## Probability as degree of belief

Bayesian interpretation xem probability là quantified uncertainty given information. Probability có thể update khi evidence mới đến. Frequentist và Bayesian frameworks khác nhau trong interpretation và inference, dù dùng nhiều mathematics chung.

## Independence

Events `A` và `B` independent nếu

```math
P(A\cap B)=P(A)P(B)
```

Điều này nghĩa biết A xảy ra không thay probability của B trong model.

Independence không giống mutual exclusivity. Nếu events mutually exclusive và đều có positive probability, chúng không independent vì occurrence của one làm probability other thành zero.

## Expected count

Nếu event probability `p` lặp `n` independent trials, expected number occurrences là `np`. Nhưng expectation không guarantee actual count exactly `np`; nó là long-run/average property.

## Risk interpretation

Một forecast “30% rain” không có nghĩa trời sẽ mưa 30% thời gian hôm đó. Tùy forecasting definition, nó thường biểu diễn probability precipitation cho area/time event specified. Probability phải đi kèm event definition.

## Mental Model

> Probability là measure trên tập các outcomes. Nó chỉ có nghĩa sau khi ta xác định rõ “event nào?”, “information nào đang có?” và “model nào tạo ra con số đó?”.

## Common Misconceptions

Mutually exclusive không phải independent. 70% probability không nghĩa event chắc chắn xảy ra 70 lần trong mỗi block 100 trials. Past streak không buộc random process “cân bằng ngay” nếu trials independent.

## Worked Example: union và overlap

Trong 100 users, 40 dùng feature A, 30 dùng B, 15 dùng cả hai. Fraction dùng ít nhất một:

```math
\frac{40+30-15}{100}=0.55
```

Nếu chỉ cộng 40%+30%=70%, 15 users overlap bị đếm hai lần. Inclusion-exclusion trong set theory trở thành probability union rule.

## Independence phải được model hóa, không suy từ “không liên quan trực giác”

Hai events có thể phụ thuộc qua hidden variable. Ví dụ server errors và slow responses có thể nhìn như hai metrics khác nhau nhưng cùng phụ thuộc load. Nếu model nhân probabilities như independent mà dependency mạnh, risk estimates sai.

Trong reliability engineering, component failures đôi khi share power/network/environment; common-cause failures phá assumption độc lập và làm system risk cao hơn calculation naive.
