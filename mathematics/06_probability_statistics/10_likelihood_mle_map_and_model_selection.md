# Likelihood, MLE, MAP và chọn mô hình từ dữ liệu

> **Mạch đọc:** Đọc **Likelihood, MLE, MAP và chọn mô hình từ dữ liệu** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Ví dụ Bernoulli: từ coin flips tới estimate xác suất** sang **Maximum Likelihood Estimation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Xác suất (probability / 확률) thường được giới thiệu theo hướng: biết mô hình (model / 모델), tính xác suất dữ liệu (data / 데이터). Statistics thường đi chiều ngược lại: đã quan sát dữ liệu (data / 데이터), ta muốn suy ra parameters hoặc so sánh các mô hình (models / 모델들). cầu nối (bridge / 브리지) giữa hai hướng nhìn là **likelihood / 우도**.

Giả sử mô hình (model / 모델) có parameter `\theta` và dữ liệu (data / 데이터) `x`. xác suất (probability / 확률) phân phối (distribution / 분포) viết

```math
p(x\mid\theta)
```

mô tả xác suất (probability / 확률) hoặc density của dữ liệu (data / 데이터) nếu `\theta` đã biết. Khi dữ liệu (data / 데이터) `x` đã fixed và ta xem expression này như hàm (function / 함수) của `\theta`, ta gọi nó là likelihood:

```math
L(\theta;x)=p(x\mid\theta).
```

Cùng một biểu thức số học, nhưng câu hỏi đã đổi: parameter nào làm observed dữ liệu (data / 데이터) trở nên plausible nhất dưới mô hình (model / 모델)?

## Ví dụ Bernoulli: từ coin flips tới estimate xác suất

Giả sử `n` independent trials, mỗi trial success với xác suất (probability / 확률) `p`, và ta quan sát `k` successes. Likelihood là

```math
L(p)
=
p^k(1-p)^{n-k}.
```

Ta muốn tìm `p` maximize expression này. sản phẩm (product / 제품) dễ underflow và derivative của sản phẩm (product / 제품) phức tạp hơn, nên thường dùng **log-likelihood / 로그우도**:

```math
\ell(p)
=
k\log p+(n-k)\log(1-p).
```

Log là monotonic nên maximize `L` tương đương maximize `\ell`. Derivative:

```math
\frac{d\ell}{dp}
=
\frac{k}{p}-\frac{n-k}{1-p}.
```

Đặt bằng zero:

```math
\frac{k}{p}
=
\frac{n-k}{1-p}
```

suy ra

```math
\hat p=\frac{k}{n}.
```

Mẫu (sample / 표본) proportion không phải một formula rơi từ trời xuống; nó là **maximum likelihood estimator** cho Bernoulli xác suất (probability / 확률) dưới independence giả định (assumption / 가정).


> **Chuyển mạch:** Từ **Ví dụ Bernoulli: từ coin flips tới estimate xác suất**, ta sang **Maximum Likelihood Estimation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Maximum Likelihood Estimation

**Ước lượng hợp lý cực đại (Maximum Likelihood Estimation, MLE / 최대우도추정)** chọn

```math
\hat\theta_{MLE}
=
\arg\max_\theta L(\theta;x).
```

hoặc tương đương

```math
\hat\theta_{MLE}
=
\arg\max_\theta \log L(\theta;x).
```

MLE rất phổ biến vì general, nối trực tiếp với tối ưu hóa (optimization / 최적화) và thường có good asymptotic properties dưới regularity các giả định (assumptions / 가정들). Nhưng MLE không phải “truth detector”. Nó chỉ chọn parameter tốt nhất trong mô hình (model / 모델) family đã giả định.

Nếu mô hình (model / 모델) family sai, MLE vẫn trả về một answer — chỉ là answer tốt nhất trong family sai đó.


> **Chuyển mạch:** Từ **Maximum Likelihood Estimation**, ta sang **Negative log-likelihood và hàm mất mát (loss function / 손실 함수) trong machine học tập (learning / 학습)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Negative log-likelihood và hàm mất mát (loss function / 손실 함수) trong machine học tập (learning / 학습)

Machine học tập (learning / 학습) thường minimize mất mát (loss / 손실) thay vì maximize likelihood. Hai cách nhìn nối nhau bằng

```math
\text{NLL}(\theta)
=
-\log L(\theta;x).
```

Với independent observations,

```math
L(\theta)=\prod_i p(x_i\mid\theta),
```

nên

```math
-\log L(\theta)
=
-\sum_i\log p(x_i\mid\theta).
```

Classification với categorical phân phối (distribution / 분포) dẫn tới cross-entropy mất mát (loss / 손실). tuyến tính (linear / 선형) regression với Gaussian noise dẫn tới squared-error mục tiêu (objective / 목표). Vì vậy nhiều “mất mát (loss / 손실) functions” thực ra encode probabilistic các giả định (assumptions / 가정들) về dữ liệu (data / 데이터) noise.

Ví dụ nếu

```math
y_i=f_\theta(x_i)+\varepsilon_i,
\qquad
\varepsilon_i\sim\mathcal N(0,\sigma^2),
```

thì maximizing Gaussian likelihood tương đương minimizing

```math
\sum_i(y_i-f_\theta(x_i))^2.
```

Mean squared lỗi (error / 오류) do đó không chỉ là convenient chỉ số (metric / 지표); nó tương ứng một noise mô hình (model / 모델) cụ thể.


> **Chuyển mạch:** Từ **Negative log-likelihood và hàm mất mát (loss function / 손실 함수) trong machine học tập (learning / 학습)**, ta sang **Bayesian cập nhật (update / 업데이트) và MAP** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bayesian cập nhật (update / 업데이트) và MAP

Bayes theorem cho

```math
p(\theta\mid x)
\propto
p(x\mid\theta)p(\theta).
```

Trong đó `p(\theta)` là **prior / 사전분포**, `p(x|\theta)` là likelihood và `p(\theta|x)` là **posterior / 사후분포**.

**Maximum A Posteriori (MAP / 최대사후추정)** chọn

```math
\hat\theta_{MAP}
=
\arg\max_\theta p(\theta\mid x).
```

Dùng log:

```math
\hat\theta_{MAP}
=
\arg\max_\theta
\left[
\log p(x\mid\theta)+\log p(\theta)
\right].
```

So với MLE, MAP thêm prior. Nếu dữ liệu (data / 데이터) rất nhiều và likelihood dominate, MLE và MAP có thể gần nhau. Khi dữ liệu (data / 데이터) ít, prior có ảnh hưởng mạnh hơn.


> **Chuyển mạch:** Từ **Bayesian cập nhật (update / 업데이트) và MAP**, ta sang **Regularization như prior** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Regularization như prior

Một liên kết (connection / 연결) quan trọng: regularization trong tối ưu hóa (optimization / 최적화) thường tương đương MAP với một prior cụ thể.

Nếu prior Gaussian

```math
p(\theta)\propto e^{-\lambda\|\theta\|_2^2},
```

negative log posterior chứa term

```math
\lambda\|\theta\|_2^2,
```

đó là L2 regularization.

Nếu prior Laplace, ta nhận L1-like penalty. Vì vậy regularization không chỉ là trick chống overfitting; nó có thể được hiểu là preference về parameter cấu trúc (structure / 구조).


> **Chuyển mạch:** Từ **Regularization như prior**, ta sang **độ lệch (bias / 편향)–variance và overfitting** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ lệch (bias / 편향)–variance và overfitting

Một mô hình (model / 모델) quá simple có thể **underfit / 과소적합**: không đủ flexibility để capture cấu trúc (structure / 구조). mô hình (model / 모델) quá flexible có thể **overfit / 과적합**: fit cả noise trong dữ liệu huấn luyện (training data / 학습 데이터).

Generalization lỗi (error / 오류) thường được conceptualize qua **độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프) / 편향-분산 절충**. High-bias mô hình (model / 모델) có systematic lỗi (error / 오류); high-variance mô hình (model / 모델) thay đổi mạnh khi huấn luyện (training / 학습) mẫu (sample / 표본) thay đổi.

Đây không phải law nói “mô hình (model / 모델) độ phức tạp (complexity / 복잡도) luôn có một sweet spot đơn giản”. hiện đại (modern / 현대적) high-dimensional các mô hình (models / 모델들) có hành vi (behavior / 동작) phức tạp hơn classical picture. Nhưng mô hình tư duy (mental model / 사고 모델) vẫn hữu ích: fit dữ liệu huấn luyện (training data / 학습 데이터) tốt chưa đủ; ta quan tâm hiệu năng (performance / 성능) trên unseen dữ liệu (data / 데이터).


> **Chuyển mạch:** Từ **độ lệch (bias / 편향)–variance và overfitting**, ta sang **Train, kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Train, kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트)

Nếu ta dùng cùng dữ liệu (data / 데이터) để fit mô hình (model / 모델) và evaluate mô hình (model / 모델), estimate hiệu năng (performance / 성능) bị optimistic. Thực hành phổ biến tách dữ liệu (data / 데이터) thành huấn luyện (training / 학습), kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트) sets.

Dữ liệu huấn luyện (training data / 학습 데이터) dùng để estimate parameters. kiểm tra hợp lệ (validation / 검증) dữ liệu (data / 데이터) dùng để chọn hyperparameters hoặc mô hình (model / 모델) variants. kiểm thử (test / 테스트) dữ liệu (data / 데이터) nên được dùng như final held-out evaluation; nếu ta xem kiểm thử (test / 테스트) repeatedly rồi điều chỉnh mô hình (model / 모델), kiểm thử (test / 테스트) đã trở thành kiểm tra hợp lệ (validation / 검증) dữ liệu (data / 데이터) về mặt thực chất.

**Cross-validation / 교차검증** chia dữ liệu (data / 데이터) thành folds và luân phiên train/validate để estimate out-of-sample hiệu năng (performance / 성능) ổn định hơn, đặc biệt khi dataset không lớn.


> **Chuyển mạch:** Từ **Train, kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트)**, ta sang **thông tin (information / 정보) criteria: fit tốt nhưng trả giá cho độ phức tạp (complexity / 복잡도)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thông tin (information / 정보) criteria: fit tốt nhưng trả giá cho độ phức tạp (complexity / 복잡도)

Criteria như AIC và BIC cân bằng likelihood với mô hình (model / 모델) độ phức tạp (complexity / 복잡도). AIC có form điển hình

```math
AIC=2k-2\log\hat L,
```

với `k` là number of parameters và `\hat L` là maximized likelihood. Lower AIC được ưu tiên trong khung phần mềm (framework / 프레임워크) của nó.

BIC có penalty tăng theo cỡ mẫu (sample size / 표본 크기):

```math
BIC=k\log n-2\log\hat L.
```

Không nên dùng AIC/BIC như universal score cho mọi bài toán (problem / 문제); các giả định (assumptions / 가정들) và modeling goal quan trọng. Nhưng chúng minh họa principle: higher in-sample likelihood không free — độ phức tạp (complexity / 복잡도) cần được account.


> **Chuyển mạch:** Từ **thông tin (information / 정보) criteria: fit tốt nhưng trả giá cho độ phức tạp (complexity / 복잡도)**, ta sang **Identifiability** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Identifiability

Một parameter **identifiable / 식별가능** nếu different parameter values tạo distributions phân biệt được theo mô hình (model / 모델). Nếu hai parameter settings tạo exactly same observable phân phối (distribution / 분포), dữ liệu (data / 데이터) không thể quyết định giữa chúng dù mẫu (sample / 표본) lớn đến đâu.

Trong neural networks, parameter symmetries khiến many weight configurations represent same hàm (function / 함수). Trong mixture các mô hình (models / 모델들), label switching là một dạng non-identifiability. Đây là reminder rằng “tối ưu được một parameter véc-tơ (vector / 벡터)” không có nghĩa parameter đó có unique interpretation.


> **Chuyển mạch:** Từ **Identifiability**, ta sang **liên kết kiến thức (knowledge connection / 지식 연결)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Likelihood nối xác suất (probability / 확률) với tối ưu hóa (optimization / 최적화). Log-likelihood dùng logarithm để biến products thành sums. Hessian của log-likelihood liên hệ bất định (uncertainty / 불확실성) của estimators. Bayesian posterior nối likelihood với prior. Cross-entropy trong classification, least squares trong regression và many losses trong ML đều có probabilistic interpretations.

Thông tin (information / 정보) lý thuyết (theory / 이론) cũng gặp likelihood qua coding: mô hình (model / 모델) gán high xác suất (probability / 확률) cho observed dữ liệu (data / 데이터) tương ứng shorter ideal mã (code / 코드) length `-\log p(x)`. Vì vậy minimizing negative log-likelihood đồng thời có thể hiểu là minimizing description length dưới mô hình (model / 모델).


> **Chuyển mạch:** Từ **liên kết kiến thức (knowledge connection / 지식 연결)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> xác suất (probability / 확률) hỏi “nếu parameter là thế này, dữ liệu (data / 데이터) có thể trông như thế nào?”. Likelihood quay cùng biểu thức lại và hỏi “dữ liệu (data / 데이터) đã trông như thế này, parameter nào giải thích nó tốt nhất trong mô hình (model / 모델) family?”. MLE chọn theo dữ liệu (data / 데이터); MAP thêm prior; mô hình (model / 모델) selection hỏi liệu phần fit thêm có thực sự generalize hay chỉ đang mua bằng độ phức tạp (complexity / 복잡도).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

Likelihood không phải xác suất (probability / 확률) phân phối (distribution / 분포) của parameter trừ khi được normalize cùng prior thành posterior trong Bayesian khung phần mềm (framework / 프레임워크). Vì vậy không nên nói `L(\theta)` là “xác suất parameter đúng”.

MLE cũng không tự động unbiased, robust hay unique. Properties phụ thuộc mô hình (model / 모델) và cỡ mẫu (sample size / 표본 크기).

Cross-validation không chữa được dữ liệu (data / 데이터) leakage. Nếu preprocessing sử dụng toàn dataset trước khi split — ví dụ standardization bằng toàn cục (global / 전역) mean hoặc tính năng (feature / 기능) selection nhìn labels của kiểm thử (test / 테스트) fold — kiểm tra hợp lệ (validation / 검증) estimate vẫn bị nhiễm thông tin (information / 정보).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 counting and combinatorics](./00_counting_and_combinatorics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
