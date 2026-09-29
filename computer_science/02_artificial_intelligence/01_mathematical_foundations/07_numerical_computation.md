# Numerical Computation cho Artificial Intelligence

> **Mạch đọc:** Đặt **Numerical Computation cho Artificial Intelligence** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Floating-point numbers không phải real numbers** sang **Precision formats trong AI**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Mathematics trên giấy giả định real numbers có precision vô hạn. Computer thì không. AI chạy trên finite bộ nhớ (memory / 메모리), finite precision và hardware kernels cụ thể. Vì vậy một công thức mathematically correct vẫn có thể overflow, underflow, lose precision hoặc produce NaN khi hiện thực (implementation / 구현).

Numerical Computation (수치 계산 / tính toán số) nghiên cứu cách biến mathematical các mô hình (models / 모델들) thành computation stable và efficient. Với Deep học tập (learning / 학습) hiện đại, đây không phải topic phụ: mixed precision, softmax stability, ma trận (matrix / 행렬) conditioning, quantization và phân tán (distributed / 분산) accumulation ảnh hưởng trực tiếp khả năng train/deploy mô hình (model / 모델).

Xem trước: [Linear Algebra for AI](./01_linear_algebra_for_ai.md) và [Optimization](./06_optimization.md).

## Floating-point numbers không phải real numbers

Computer thường dùng IEEE-754 floating điểm (point / 지점). Một number được represented gần dạng:

\[
(-1)^s\times m\times2^e
\]

với sign, significand/mantissa và exponent.

Chỉ finite set numbers representable. Nhiều decimal như `0.1` không represent chính xác (exact / 정확한) trong nhị phân (binary / 이진) floating điểm (point / 지점).

Do đó:

```python
0.1 + 0.2 == 0.3
```

có thể false trong dùng chung (common / 공통) languages.

Trong normal software, lỗi (error / 오류) này nhỏ. Trong repeated large-scale accumulation hoặc unstable formula, small errors có thể amplify.

## Precision formats trong AI

### FP32

32-bit floating điểm (point / 지점) có khoảng 24 bits significand precision including hidden bit và exponent phạm vi (range / 범위) đủ rộng cho nhiều ML computations. Nó từng là default huấn luyện (training / 학습) format.

### FP16

FP16 dùng ít bộ nhớ (memory / 메모리) và tăng accelerator thông lượng (throughput / 처리량) nhưng exponent/mantissa nhỏ hơn, dễ overflow/underflow hơn.

### BF16

BFloat16 giữ exponent phạm vi (range / 범위) tương tự FP32 nhưng mantissa ngắn hơn. Nó hy sinh precision để giữ động (dynamic / 동적) phạm vi (range / 범위), phù hợp nhiều Deep học tập (learning / 학습) workloads.

### FP8 và lower precision

Hiện đại (modern / 현대적) accelerators hỗ trợ FP8-like formats trong selected huấn luyện (training / 학습)/suy luận (inference / 추론) paths. Lower precision tăng thông lượng (throughput / 처리량) và giảm bộ nhớ (memory / 메모리) nhưng đòi hỏi scaling, calibration và kernel hỗ trợ (support / 지원) cẩn thận.

### Integer quantization

INT8/INT4-like formats thường dùng suy luận (inference / 추론) để giảm bộ nhớ (memory / 메모리) bandwidth và compute. Quantization không chỉ “convert kiểu (type / 타입)”; cần map real values sang discrete levels.

## Machine epsilon

Machine epsilon là khoảng cách relative nhỏ nhất quanh 1 mà floating-point có thể distinguish theo format/convention.

Intuition: khi numbers rất lớn, spacing giữa representable numbers cũng lớn hơn. Precision là relative, không uniform absolute trên toàn phạm vi (range / 범위).

Do đó adding tiny number vào huge number có thể không thay kết quả (result / 결과):

\[
large + tiny \approx large
\]

trong floating điểm (point / 지점).

## Rounding lỗi (error / 오류)

Thao tác (operation / 연산) chính xác (exact / 정확한) `a+b` có thể được stored thành nearest representable floating-point number:

\[
fl(a+b)=(a+b)(1+\delta)
\]

với small `δ` dưới các giả định (assumptions / 가정들).

Một thao tác (operation / 연산) lỗi (error / 오류) nhỏ, nhưng thuật toán (algorithm / 알고리즘) với millions operations cần consider accumulation and conditioning.

## Catastrophic cancellation

Khi subtract hai gần-equal large numbers:

\[
x-y
\]

leading significant digits cancel, relative lỗi (error / 오류) của kết quả (result / 결과) có thể rất lớn.

Ví dụ computation variance bằng:

\[
E[X^2]-E[X]^2
\]

có thể unstable nếu hai terms rất gần nhau.

Stable algorithms như Welford's phương thức (method / 메서드) cập nhật (update / 업데이트) mean/variance incrementally để giảm cancellation issues.

## Overflow và underflow

**Overflow** xảy ra khi magnitude vượt representable max → `Inf` hoặc lỗi (error / 오류) hành vi (behavior / 동작).

**Underflow** khi magnitude quá nhỏ, thành subnormal hoặc zero.

Exponentials/log probabilities rất dễ gặp vấn đề này.

## Stable softmax

Naive softmax:

\[
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

Nếu `z=[1000,1001]`, `e^{1001}` overflow trong nhiều formats.

Softmax bất biến (invariant / 불변식) khi subtract same constant:

\[
softmax(z_i)=\frac{e^{z_i-c}}{\sum_j e^{z_j-c}}
\]

Chọn:

\[
c=\max_j z_j
\]

làm largest exponent bằng `e^0=1`, tránh overflow.

Đây là chuẩn gốc (canonical / 정본) example của numerical stability: mathematically equivalent formulas có radically different computational hành vi (behavior / 동작).

## Log-sum-exp trick

Ta thường cần:

\[
\log\sum_i e^{x_i}
\]

Stable form:

\[
\log\sum_i e^{x_i}=m+\log\sum_i e^{x_i-m}
\]

với:

\[
m=\max_i x_i
\]

Log-sum-exp xuất hiện trong log-likelihood, softmax, CRF, probabilistic các mô hình (models / 모델들).

Frameworks thường cung cấp thành phần nguyên thủy (primitive / 기본 요소) stable; nên dùng thay vì tự compose `log(sum(exp(x)))`.

## Tính xác suất (probability / 확률) trong log không gian (space / 공간)

Sản phẩm (product / 제품) nhiều probabilities nhỏ:

\[
\prod_i p_i
\]

có thể underflow về zero.

Lấy log:

\[
\log\prod_i p_i=\sum_i\log p_i
\]

biến multiplication thành addition và stable hơn.

Đây là lý do chuỗi (sequence / 시퀀스) likelihood thường computed as sum of log-probabilities.

## Conditioning khác stability

**Conditioning** là thuộc tính (property / 속성) của mathematical bài toán (problem / 문제): đầu vào (input / 입력) perturb nhỏ có thể làm đầu ra (output / 출력) đổi bao nhiêu.

**Numerical stability** là thuộc tính (property / 속성) của thuật toán (algorithm / 알고리즘): computation có introduce lỗi (error / 오류) lớn hơn inherent conditioning hay không.

Một bài toán (problem / 문제) ill-conditioned không thể magically fix hoàn toàn bằng thuật toán (algorithm / 알고리즘); stable thuật toán (algorithm / 알고리즘) chỉ tránh thêm unnecessary lỗi (error / 오류).

Ví dụ solving hệ tuyến tính (linear system / 선형 시스템) với nearly singular ma trận (matrix / 행렬) inherently sensitive.

## Điều kiện (condition / 조건) number

Cho invertible ma trận (matrix / 행렬) `A`, điều kiện (condition / 조건) number theo norm:

\[
\kappa(A)=\|A\|\|A^{-1}\|
\]

Large `κ` nghĩa small đầu vào (input / 입력)/rounding errors có thể amplify mạnh trong solution.

Trong tối ưu hóa (optimization / 최적화), ill-conditioned Hessian dẫn độ dốc (gradient / 기울기) descent zig-zag và slow convergence.

Tính năng (feature / 기능) scaling và normalization có thể improve effective conditioning.

## Không nên tính inverse khi không cần

Expression:

\[
x=A^{-1}b
\]

mathematically valid, nhưng numerical tuyến tính (linear / 선형) algebra thường dùng solver/factorization thay vì explicitly compute inverse.

Ví dụ least squares nên dùng QR/SVD hoặc optimized solver thay vì:

\[
(X^TX)^{-1}X^Ty
\]

vì forming `X^TX` có thể square điều kiện (condition / 조건) number và worsen stability.

Quy tắc (rule / 규칙) kỹ thuật (engineering / 엔지니어링):

> Solve the hệ thống (system / 시스템); do not automatically form the inverse.

## Summation lỗi (error / 오류)

Sum millions floating-point values depends thứ tự (order / 순서) vì floating-point addition không associative:

\[
(a+b)+c\neq a+(b+c)
\]

exactly.

Pairwise summation hoặc Kahan summation có thể reduce lỗi (error / 오류).

Parallel GPU reductions thay đổi (change / 변경) thao tác (operation / 연산) thứ tự (order / 순서), nên identical mã (code / 코드)/hardware settings vẫn có slight nondeterminism depending kernels.

## Determinism và reproducibility

Deep học tập (learning / 학습) kết quả (result / 결과) có thể khác do:

- random initialization;
- shuffled batches;
- dropout;
- parallel reduction thứ tự (order / 순서);
- nondeterministic CUDA kernels;
- phân tán (distributed / 분산) communication timing.

Setting seed không guarantee bitwise determinism nếu kernel nondeterministic.

Reproducibility cần bản ghi (record / 레코드) software versions, hardware, seeds, configs, dataset phiên bản (version / 버전) và deterministic settings khi required.

## Mixed-precision huấn luyện (training / 학습)

Mixed precision dùng lower precision cho high-throughput operations nhưng giữ selected quantities ở higher precision.

Typical mẫu (pattern / 패턴):

```text
FP16/BF16 matrix multiply
        ↓
higher-precision accumulation / master weights where needed
        ↓
optimizer update
```

Chính xác (exact / 정확한) hành vi (behavior / 동작) phụ thuộc hardware/khung phần mềm (framework / 프레임워크).

Goal là giảm bộ nhớ (memory / 메모리) + tăng thông lượng (throughput / 처리량) mà không destroy huấn luyện (training / 학습) tín hiệu (signal / 신호).

## Mất mát (loss / 손실) scaling

Với FP16, small gradients có thể underflow. mất mát (loss / 손실) scaling multiply mất mát (loss / 손실) bởi factor `S`:

\[
L'=SL
\]

Độ dốc (gradient / 기울기):

\[
\nabla L'=S\nabla L
\]

sau backward, divide độ dốc (gradient / 기울기) by `S` trước optimizer cập nhật (update / 업데이트).

Động (dynamic / 동적) mất mát (loss / 손실) scaling adjust `S` khi detect overflow.

BF16 exponent phạm vi (range / 범위) rộng hơn nên often less dependent on mất mát (loss / 손실) scaling.

## Độ dốc (gradient / 기울기) overflow và NaN debugging

NaN có thể xuất phát từ:

- divide by zero;
- log of invalid/zero giá trị (value / 값);
- sqrt negative due to numerical noise;
- exploding activation/độ dốc (gradient / 기울기);
- overflow exponential;
- invalid normalization statistics.

Gỡ lỗi (debug / 디버그) luồng (flow / 흐름) useful:

```text
loss finite?
  ↓
activations finite per layer?
  ↓
gradients finite?
  ↓
optimizer states finite?
  ↓
learning rate / scaling / input values
```

Khung phần mềm (framework / 프레임워크) anomaly detection giúp locate first invalid thao tác (operation / 연산), nhưng có hiệu năng (performance / 성능) chi phí (cost / 비용).

## Stable normalization

Variance computation:

\[
\sigma^2=E[x^2]-E[x]^2
\]

có thể suffer cancellation. Implementations dùng stable reductions và add epsilon:

\[
\hat x=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}
\]

`ε` không chỉ tránh divide by zero; nó ảnh hưởng hành vi (behavior / 동작) khi variance rất nhỏ.

Different normalization layers choose axes differently, affecting both statistics and numerical hành vi (behavior / 동작).

## Quantization

Quantization map continuous/floating values thành discrete integer levels.

Simple affine quantization:

\[
q=round(x/s)+z
\]

với quy mô (scale / 규모) `s` và zero-point `z`.

Dequantize approximate:

\[
x\approx s(q-z)
\]

Quantization lỗi (error / 오류) là difference giữa original và reconstructed giá trị (value / 값).

## Symmetric vs asymmetric quantization

Symmetric quantization thường set zero-point near 0 và phạm vi (range / 범위) symmetric quanh zero. Simpler/faster trên some hardware.

Asymmetric quantization dùng zero-point để fit non-symmetric phạm vi (range / 범위) tốt hơn.

Choice depends weights/activations phân phối (distribution / 분포) và hardware kernels.

## Per-tensor vs per-channel quantization

**Per-tensor**: một quy mô (scale / 규모) cho toàn tensor.

**Per-channel**: mỗi đầu ra (output / 출력)/đầu vào (input / 입력) channel có quy mô (scale / 규모) riêng, thường giảm lỗi (error / 오류) khi ranges khác nhau nhưng siêu dữ liệu (metadata / 메타데이터)/hiện thực (implementation / 구현) phức tạp hơn.

LLM weight quantization còn dùng group-wise schemes: một quy mô (scale / 규모) per group of weights.

## Post-training quantization và quantization-aware huấn luyện (training / 학습)

**Post-Training Quantization (PTQ)** quantize trained mô hình (model / 모델) sau huấn luyện (training / 학습), dùng calibration dữ liệu (data / 데이터) khi cần.

**Quantization-Aware huấn luyện (training / 학습) (QAT)** simulate quantization effects trong huấn luyện (training / 학습) để mô hình (model / 모델) thích nghi.

PTQ dễ hơn; QAT có thể preserve chất lượng (quality / 품질) tốt hơn ở aggressive low precision nhưng tốn huấn luyện (training / 학습) effort.

## LLM quantization

LLM parameters chiếm bộ nhớ (memory / 메모리) lớn. Approx bộ nhớ (memory / 메모리) chỉ tính raw weights:

\[
bộ nhớ (memory / 메모리)\approx N_{params}\times bits/parameter
\]

Ví dụ 7B parameters:

- FP16 ≈ 14 GB raw weights;
- INT8 ≈ 7 GB;
- 4-bit ≈ 3.5 GB;

Actual thời gian chạy (runtime / 런타임) cần thêm siêu dữ liệu (metadata / 메타데이터), KV bộ nhớ đệm (cache / 캐시), activations, workspace và allocator overhead.

Chất lượng (quality / 품질) impact phụ thuộc quantization thuật toán (algorithm / 알고리즘), outlier handling, group kích thước (size / 크기) và mô hình (model / 모델) kiến trúc (architecture / 아키텍처).

## KV bộ nhớ đệm (cache / 캐시) và precision

Autoregressive Transformer suy luận (inference / 추론) bộ nhớ đệm (cache / 캐시) Key/giá trị (value / 값) của previous tokens để không recompute toàn chuỗi (sequence / 시퀀스).

KV bộ nhớ đệm (cache / 캐시) bộ nhớ (memory / 메모리) grows roughly với:

```text
batch × sequence length × layers × KV heads × head dimension × bytes
```

Long ngữ cảnh (context / 맥락) có thể khiến KV bộ nhớ đệm (cache / 캐시) dominate bộ nhớ (memory / 메모리). Quantizing KV bộ nhớ đệm (cache / 캐시) hoặc using grouped-query/multi-query attention giảm bộ nhớ (memory / 메모리) pressure, nhưng may affect chất lượng (quality / 품질).

## Accumulation precision trong phép nhân ma trận (matrix multiplication / 행렬 곱셈)

Inputs có thể FP16/BF16 nhưng accumulation nhiều products ở FP32-like precision tùy hardware/kernel.

Dot sản phẩm (product / 제품):

\[
s=\sum_i a_ib_i
\]

nếu accumulate hoàn toàn low precision, rounding lỗi (error / 오류) tăng theo many terms.

Accelerator thiết kế (design / 설계) thường separate đầu vào (input / 입력) format và accumulation format.

## Fused kernels

Một expression như:

```text
linear → bias → activation
```

nếu thực hiện từng thao tác (operation / 연산) riêng cần ghi (write / 쓰기)/read intermediate tensors từ bộ nhớ (memory / 메모리).

Kernel fusion combine operations để giảm bộ nhớ (memory / 메모리) traffic và sometimes improve numerical hành vi (behavior / 동작) by avoiding rounding between intermediates.

FlashAttention là example sâu hơn: restructure attention computation để reduce HBM bộ nhớ (memory / 메모리) traffic và compute chính xác (exact / 정확한) attention up to floating-point hành vi (behavior / 동작) without materializing full attention ma trận (matrix / 행렬) in naive way.

Numerical thuật toán (algorithm / 알고리즘) và hardware efficiency có thể cùng được cải thiện bằng reformulation.

## Bộ nhớ (memory / 메모리) bandwidth vs FLOPs

AI hiệu năng (performance / 성능) không chỉ phụ thuộc số floating-point operations. thao tác (operation / 연산) có thể **compute-bound** hoặc **memory-bound**.

Arithmetic intensity roughly:

\[
\frac{FLOPs}{bytes\ moved}
\]

Phép nhân ma trận (matrix multiplication / 행렬 곱셈) lớn có high arithmetic intensity và phù hợp GPU. Elementwise thao tác (operation / 연산) có thể memory-bound.

Đây là lý do vectorization/fusion quan trọng, và tại sao kiến trúc (architecture / 아키텍처) AI co-evolve với hardware.

## Sparse computation

Nếu tensor có nhiều zeros, sparse biểu diễn (representation / 표현) có thể tiết kiệm compute/bộ nhớ (memory / 메모리). Nhưng sparsity chỉ có lợi nếu hardware/software exploit mẫu (pattern / 패턴).

Unstructured random sparsity có overhead indexing cao; structured sparsity dễ accelerate hơn.

“90% weights zero” không tự động nghĩa suy luận (inference / 추론) nhanh 10×.

## Approximation lỗi (error / 오류) và mô hình (model / 모델) lỗi (error / 오류)

Cần tách:

```text
modeling error
+ statistical error
+ optimization error
+ numerical error
```

Mô hình (model / 모델) prediction sai có thể do mô hình (model / 모델) lớp (class / 클래스) không đủ, dữ liệu (data / 데이터) thiếu, optimizer chưa converge hoặc numerical precision.

Không nên blame floating điểm (point / 지점) trước khi kiểm tra larger sources, nhưng ở quy mô (scale / 규모) lớn numerical issues là real dạng thất bại (failure mode / 실패 모드).

## Stable sigmoid và nhị phân (binary / 이진) cross-entropy

Naively computing:

\[
\sigma(z)=1/(1+e^{-z})
\]

rồi:

\[
-y\log\sigma(z)-(1-y)\log(1-\sigma(z))
\]

có thể unstable cho extreme logits.

Frameworks cung cấp `binary_cross_entropy_with_logits`-like fused stable formulation. kỹ thuật (engineering / 엔지니어링) quy tắc (rule / 규칙): use numerically stable mất mát (loss / 손실) primitives từ khung phần mềm (framework / 프레임워크) thay vì manually compose probabilities nếu possible.

## Độ dốc (gradient / 기울기) accumulation

Nếu GPU bộ nhớ (memory / 메모리) không đủ batch lớn, có thể accumulate gradients qua micro-batches:

```text
microbatch 1 → gradient
microbatch 2 → add gradient
...
optimizer.step()
```

Nếu mất mát (loss / 손실) scaling/normalization đúng, effective batch có thể approximate large batch.

Nhưng BatchNorm-like layers và stochastic trạng thái (state / 상태) có thể làm ngữ nghĩa (semantics / 의미론) khác true large batch.

## Phân tán (distributed / 분산) numerical hành vi (behavior / 동작)

Phân tán (distributed / 분산) huấn luyện (training / 학습) aggregate gradients qua all-reduce. thứ tự (order / 순서) và precision communication ảnh hưởng rounding.

Độ dốc (gradient / 기울기) compression, reduced-precision communication và sharding tiết kiệm bandwidth/bộ nhớ (memory / 메모리) nhưng introduce trade-offs.

At quy mô (scale / 규모), numerical phân tích (analysis / 분석) merge với distributed-systems kỹ thuật (engineering / 엔지니어링).

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Real-number formula ≠ floating-point computation
Stable formula       = same mathematics, safer numerical path
Conditioning         = problem sensitive đến input error mức nào
Precision            = represent values chi tiết đến đâu
Dynamic range        = represent magnitude lớn/nhỏ đến đâu
Mixed precision      = dùng format phù hợp cho từng operation
Quantization         = trade numerical fidelity for memory/throughput
Kernel design        = reformulate computation for hardware + stability
```

## Dùng chung (common / 공통) Misconceptions

### “FP16 chỉ kém chính xác hơn FP32 một chút”

Nó có cả lower precision và much smaller exponent phạm vi (range / 범위) than FP32; overflow/underflow hành vi (behavior / 동작) khác đáng kể. BF16 sự đánh đổi (trade-off / 트레이드오프) lại khác.

### “Quantization 4-bit làm mô hình (model / 모델) nhỏ chính xác 4× và nhanh 4×”

Raw weight lưu trữ (storage / 저장소) có thể giảm ~4× so với FP16, nhưng thời gian chạy (runtime / 런타임) bộ nhớ (memory / 메모리) còn KV bộ nhớ đệm (cache / 캐시)/siêu dữ liệu (metadata / 메타데이터) và speed phụ thuộc kernel/hardware.

### “NaN là bug khung phần mềm (framework / 프레임워크)”

Có thể là bug, nhưng thường cũng có thể do unstable mục tiêu (objective / 목표), overflow, huge học tập (learning / 학습) tỷ lệ (rate / 비율), invalid đầu vào (input / 입력) hoặc scaling.

### “Công thức mathematically equivalent sẽ chạy giống nhau”

Không trong floating điểm (point / 지점). Softmax và log-sum-exp là examples điển hình.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Numerical Computation nối Mathematics với [AI System Architecture](../00_foundations/04_ai_system_architecture.md), tối ưu hóa (optimization / 최적화) và Compute hạ tầng (infrastructure / 인프라). Những concepts này sẽ quay lại khi học mixed-precision huấn luyện (training / 학습), quantization, Transformer kernels, phân tán (distributed / 분산) huấn luyện (training / 학습) và efficient suy luận (inference / 추론).

Khi model gặp instability hoặc deployment cost cao, hãy nhìn cả equation, precision format, tensor range, reduction order, memory movement và hardware kernel — không chỉ nhìn architecture trên paper.
