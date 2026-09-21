# Numerical Computation cho Artificial Intelligence

Mathematics trên giấy giả định real numbers có precision vô hạn. Computer thì không. AI chạy trên finite memory, finite precision và hardware kernels cụ thể. Vì vậy một công thức mathematically correct vẫn có thể overflow, underflow, lose precision hoặc produce NaN khi implementation.

Numerical Computation (수치 계산 / tính toán số) nghiên cứu cách biến mathematical models thành computation stable và efficient. Với Deep Learning hiện đại, đây không phải topic phụ: mixed precision, softmax stability, matrix conditioning, quantization và distributed accumulation ảnh hưởng trực tiếp khả năng train/deploy model.

Xem trước: [Linear Algebra for AI](./01_linear_algebra_for_ai.md) và [Optimization](./06_optimization.md).

## Floating-point numbers không phải real numbers

Computer thường dùng IEEE-754 floating point. Một number được represented gần dạng:

\[
(-1)^s\times m\times2^e
\]

với sign, significand/mantissa và exponent.

Chỉ finite set numbers representable. Nhiều decimal như `0.1` không represent exact trong binary floating point.

Do đó:

```python
0.1 + 0.2 == 0.3
```

có thể false trong common languages.

Trong normal software, error này nhỏ. Trong repeated large-scale accumulation hoặc unstable formula, small errors có thể amplify.

## Precision formats trong AI

### FP32

32-bit floating point có khoảng 24 bits significand precision including hidden bit và exponent range đủ rộng cho nhiều ML computations. Nó từng là default training format.

### FP16

FP16 dùng ít memory và tăng accelerator throughput nhưng exponent/mantissa nhỏ hơn, dễ overflow/underflow hơn.

### BF16

BFloat16 giữ exponent range tương tự FP32 nhưng mantissa ngắn hơn. Nó hy sinh precision để giữ dynamic range, phù hợp nhiều Deep Learning workloads.

### FP8 và lower precision

Modern accelerators hỗ trợ FP8-like formats trong selected training/inference paths. Lower precision tăng throughput và giảm memory nhưng đòi hỏi scaling, calibration và kernel support cẩn thận.

### Integer quantization

INT8/INT4-like formats thường dùng inference để giảm memory bandwidth và compute. Quantization không chỉ “convert type”; cần map real values sang discrete levels.

## Machine epsilon

Machine epsilon là khoảng cách relative nhỏ nhất quanh 1 mà floating-point có thể distinguish theo format/convention.

Intuition: khi numbers rất lớn, spacing giữa representable numbers cũng lớn hơn. Precision là relative, không uniform absolute trên toàn range.

Do đó adding tiny number vào huge number có thể không thay result:

\[
large + tiny \approx large
\]

trong floating point.

## Rounding error

Operation exact `a+b` có thể được stored thành nearest representable floating-point number:

\[
fl(a+b)=(a+b)(1+\delta)
\]

với small `δ` dưới assumptions.

Một operation error nhỏ, nhưng algorithm với millions operations cần consider accumulation and conditioning.

## Catastrophic cancellation

Khi subtract hai gần-equal large numbers:

\[
x-y
\]

leading significant digits cancel, relative error của result có thể rất lớn.

Ví dụ computation variance bằng:

\[
E[X^2]-E[X]^2
\]

có thể unstable nếu hai terms rất gần nhau.

Stable algorithms như Welford's method update mean/variance incrementally để giảm cancellation issues.

## Overflow và underflow

**Overflow** xảy ra khi magnitude vượt representable max → `Inf` hoặc error behavior.

**Underflow** khi magnitude quá nhỏ, thành subnormal hoặc zero.

Exponentials/log probabilities rất dễ gặp vấn đề này.

## Stable softmax

Naive softmax:

\[
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

Nếu `z=[1000,1001]`, `e^{1001}` overflow trong nhiều formats.

Softmax invariant khi subtract same constant:

\[
softmax(z_i)=\frac{e^{z_i-c}}{\sum_j e^{z_j-c}}
\]

Chọn:

\[
c=\max_j z_j
\]

làm largest exponent bằng `e^0=1`, tránh overflow.

Đây là canonical example của numerical stability: mathematically equivalent formulas có radically different computational behavior.

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

Log-sum-exp xuất hiện trong log-likelihood, softmax, CRF, probabilistic models.

Frameworks thường cung cấp primitive stable; nên dùng thay vì tự compose `log(sum(exp(x)))`.

## Tính probability trong log space

Product nhiều probabilities nhỏ:

\[
\prod_i p_i
\]

có thể underflow về zero.

Lấy log:

\[
\log\prod_i p_i=\sum_i\log p_i
\]

biến multiplication thành addition và stable hơn.

Đây là lý do sequence likelihood thường computed as sum of log-probabilities.

## Conditioning khác stability

**Conditioning** là property của mathematical problem: input perturb nhỏ có thể làm output đổi bao nhiêu.

**Numerical stability** là property của algorithm: computation có introduce error lớn hơn inherent conditioning hay không.

Một problem ill-conditioned không thể magically fix hoàn toàn bằng algorithm; stable algorithm chỉ tránh thêm unnecessary error.

Ví dụ solving linear system với nearly singular matrix inherently sensitive.

## Condition number

Cho invertible matrix `A`, condition number theo norm:

\[
\kappa(A)=\|A\|\|A^{-1}\|
\]

Large `κ` nghĩa small input/rounding errors có thể amplify mạnh trong solution.

Trong optimization, ill-conditioned Hessian dẫn gradient descent zig-zag và slow convergence.

Feature scaling và normalization có thể improve effective conditioning.

## Không nên tính inverse khi không cần

Expression:

\[
x=A^{-1}b
\]

mathematically valid, nhưng numerical linear algebra thường dùng solver/factorization thay vì explicitly compute inverse.

Ví dụ least squares nên dùng QR/SVD hoặc optimized solver thay vì:

\[
(X^TX)^{-1}X^Ty
\]

vì forming `X^TX` có thể square condition number và worsen stability.

Rule engineering:

> Solve the system; do not automatically form the inverse.

## Summation error

Sum millions floating-point values depends order vì floating-point addition không associative:

\[
(a+b)+c\neq a+(b+c)
\]

exactly.

Pairwise summation hoặc Kahan summation có thể reduce error.

Parallel GPU reductions change operation order, nên identical code/hardware settings vẫn có slight nondeterminism depending kernels.

## Determinism và reproducibility

Deep Learning result có thể khác do:

- random initialization;
- shuffled batches;
- dropout;
- parallel reduction order;
- nondeterministic CUDA kernels;
- distributed communication timing.

Setting seed không guarantee bitwise determinism nếu kernel nondeterministic.

Reproducibility cần record software versions, hardware, seeds, configs, dataset version và deterministic settings khi required.

## Mixed-precision training

Mixed precision dùng lower precision cho high-throughput operations nhưng giữ selected quantities ở higher precision.

Typical pattern:

```text
FP16/BF16 matrix multiply
        ↓
higher-precision accumulation / master weights where needed
        ↓
optimizer update
```

Exact behavior phụ thuộc hardware/framework.

Goal là giảm memory + tăng throughput mà không destroy training signal.

## Loss scaling

Với FP16, small gradients có thể underflow. Loss scaling multiply loss bởi factor `S`:

\[
L'=SL
\]

Gradient:

\[
\nabla L'=S\nabla L
\]

sau backward, divide gradient by `S` trước optimizer update.

Dynamic loss scaling adjust `S` khi detect overflow.

BF16 exponent range rộng hơn nên often less dependent on loss scaling.

## Gradient overflow và NaN debugging

NaN có thể xuất phát từ:

- divide by zero;
- log of invalid/zero value;
- sqrt negative due to numerical noise;
- exploding activation/gradient;
- overflow exponential;
- invalid normalization statistics.

Debug flow useful:

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

Framework anomaly detection giúp locate first invalid operation, nhưng có performance cost.

## Stable normalization

Variance computation:

\[
\sigma^2=E[x^2]-E[x]^2
\]

có thể suffer cancellation. Implementations dùng stable reductions và add epsilon:

\[
\hat x=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}
\]

`ε` không chỉ tránh divide by zero; nó ảnh hưởng behavior khi variance rất nhỏ.

Different normalization layers choose axes differently, affecting both statistics and numerical behavior.

## Quantization

Quantization map continuous/floating values thành discrete integer levels.

Simple affine quantization:

\[
q=round(x/s)+z
\]

với scale `s` và zero-point `z`.

Dequantize approximate:

\[
x\approx s(q-z)
\]

Quantization error là difference giữa original và reconstructed value.

## Symmetric vs asymmetric quantization

Symmetric quantization thường set zero-point near 0 và range symmetric quanh zero. Simpler/faster trên some hardware.

Asymmetric quantization dùng zero-point để fit non-symmetric range tốt hơn.

Choice depends weights/activations distribution và hardware kernels.

## Per-tensor vs per-channel quantization

**Per-tensor**: một scale cho toàn tensor.

**Per-channel**: mỗi output/input channel có scale riêng, thường giảm error khi ranges khác nhau nhưng metadata/implementation phức tạp hơn.

LLM weight quantization còn dùng group-wise schemes: một scale per group of weights.

## Post-training quantization và quantization-aware training

**Post-Training Quantization (PTQ)** quantize trained model sau training, dùng calibration data khi cần.

**Quantization-Aware Training (QAT)** simulate quantization effects trong training để model thích nghi.

PTQ dễ hơn; QAT có thể preserve quality tốt hơn ở aggressive low precision nhưng tốn training effort.

## LLM quantization

LLM parameters chiếm memory lớn. Approx memory chỉ tính raw weights:

\[
Memory\approx N_{params}\times bits/parameter
\]

Ví dụ 7B parameters:

- FP16 ≈ 14 GB raw weights;
- INT8 ≈ 7 GB;
- 4-bit ≈ 3.5 GB;

Actual runtime cần thêm metadata, KV cache, activations, workspace và allocator overhead.

Quality impact phụ thuộc quantization algorithm, outlier handling, group size và model architecture.

## KV cache và precision

Autoregressive Transformer inference cache Key/Value của previous tokens để không recompute toàn sequence.

KV cache memory grows roughly với:

```text
batch × sequence length × layers × KV heads × head dimension × bytes
```

Long context có thể khiến KV cache dominate memory. Quantizing KV cache hoặc using grouped-query/multi-query attention giảm memory pressure, nhưng may affect quality.

## Accumulation precision trong matrix multiplication

Inputs có thể FP16/BF16 nhưng accumulation nhiều products ở FP32-like precision tùy hardware/kernel.

Dot product:

\[
s=\sum_i a_ib_i
\]

nếu accumulate hoàn toàn low precision, rounding error tăng theo many terms.

Accelerator design thường separate input format và accumulation format.

## Fused kernels

Một expression như:

```text
linear → bias → activation
```

nếu thực hiện từng operation riêng cần write/read intermediate tensors từ memory.

Kernel fusion combine operations để giảm memory traffic và sometimes improve numerical behavior by avoiding rounding between intermediates.

FlashAttention là example sâu hơn: restructure attention computation để reduce HBM memory traffic và compute exact attention up to floating-point behavior without materializing full attention matrix in naive way.

Numerical algorithm và hardware efficiency có thể cùng được cải thiện bằng reformulation.

## Memory bandwidth vs FLOPs

AI performance không chỉ phụ thuộc số floating-point operations. Operation có thể **compute-bound** hoặc **memory-bound**.

Arithmetic intensity roughly:

\[
\frac{FLOPs}{bytes\ moved}
\]

Matrix multiplication lớn có high arithmetic intensity và phù hợp GPU. Elementwise operation có thể memory-bound.

Đây là lý do vectorization/fusion quan trọng, và tại sao architecture AI co-evolve với hardware.

## Sparse computation

Nếu tensor có nhiều zeros, sparse representation có thể tiết kiệm compute/memory. Nhưng sparsity chỉ có lợi nếu hardware/software exploit pattern.

Unstructured random sparsity có overhead indexing cao; structured sparsity dễ accelerate hơn.

“90% weights zero” không tự động nghĩa inference nhanh 10×.

## Approximation error và model error

Cần tách:

```text
modeling error
+ statistical error
+ optimization error
+ numerical error
```

Model prediction sai có thể do model class không đủ, data thiếu, optimizer chưa converge hoặc numerical precision.

Không nên blame floating point trước khi kiểm tra larger sources, nhưng ở scale lớn numerical issues là real failure mode.

## Stable sigmoid và binary cross-entropy

Naively computing:

\[
\sigma(z)=1/(1+e^{-z})
\]

rồi:

\[
-y\log\sigma(z)-(1-y)\log(1-\sigma(z))
\]

có thể unstable cho extreme logits.

Frameworks cung cấp `binary_cross_entropy_with_logits`-like fused stable formulation. Engineering rule: use numerically stable loss primitives từ framework thay vì manually compose probabilities nếu possible.

## Gradient accumulation

Nếu GPU memory không đủ batch lớn, có thể accumulate gradients qua micro-batches:

```text
microbatch 1 → gradient
microbatch 2 → add gradient
...
optimizer.step()
```

Nếu loss scaling/normalization đúng, effective batch có thể approximate large batch.

Nhưng BatchNorm-like layers và stochastic state có thể làm semantics khác true large batch.

## Distributed numerical behavior

Distributed training aggregate gradients qua all-reduce. Order và precision communication ảnh hưởng rounding.

Gradient compression, reduced-precision communication và sharding tiết kiệm bandwidth/memory nhưng introduce trade-offs.

At scale, numerical analysis merge với distributed-systems engineering.

## Mental Model

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

## Common Misconceptions

### “FP16 chỉ kém chính xác hơn FP32 một chút”

Nó có cả lower precision và much smaller exponent range than FP32; overflow/underflow behavior khác đáng kể. BF16 trade-off lại khác.

### “Quantization 4-bit làm model nhỏ chính xác 4× và nhanh 4×”

Raw weight storage có thể giảm ~4× so với FP16, nhưng runtime memory còn KV cache/metadata và speed phụ thuộc kernel/hardware.

### “NaN là bug framework”

Có thể là bug, nhưng thường cũng có thể do unstable objective, overflow, huge learning rate, invalid input hoặc scaling.

### “Công thức mathematically equivalent sẽ chạy giống nhau”

Không trong floating point. Softmax và log-sum-exp là examples điển hình.

## Knowledge Connection

Numerical Computation nối Mathematics với [AI System Architecture](../00_foundations/04_ai_system_architecture.md), Optimization và Compute Infrastructure. Những concepts này sẽ quay lại khi học mixed-precision training, quantization, Transformer kernels, distributed training và efficient inference.

Khi model gặp instability hoặc deployment cost cao, hãy nhìn cả equation, precision format, tensor range, reduction order, memory movement và hardware kernel — không chỉ nhìn architecture trên paper.