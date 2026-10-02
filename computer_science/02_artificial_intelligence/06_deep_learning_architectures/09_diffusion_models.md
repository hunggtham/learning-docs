# Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Diffusion models**. Route đi từ forward noising process → reverse denoising process → score/noise prediction → conditioning/sampling schedule → quality/latency trade-offs, để generation được nối với stochastic dynamics.

Diffusion các mô hình (models / 모델들) học generative phân phối (distribution / 분포) bằng một idea khác GAN: thay vì generator một bước phải tạo mẫu (sample / 표본) hoàn chỉnh ngay, ta định nghĩa một **forward tiến trình (process / 프로세스)** dần phá dữ liệu (data / 데이터) thành noise, rồi train mô hình (model / 모델) học **reverse denoising tiến trình (process / 프로세스)** từng bước để quay từ noise về dữ liệu (data / 데이터).

Điều này biến generation thành một chuỗi bài toán cục bộ (local / 로컬) denoising tương đối ổn định.

## Forward Diffusion tiến trình (process / 프로세스)

Bắt đầu dữ liệu (data / 데이터):

\[
x_0\sim p_{dữ liệu (data / 데이터)}
\]

Mỗi step thêm Gaussian noise:

\[
q(x_t\mid x_{t-1})=
\mathcal N(\sqrt{1-\beta_t}x_{t-1},\beta_t I)
\]

Define:

\[
\alpha_t=1-\beta_t,
\qquad
\bar\alpha_t=\prod_{s=1}^{t}\alpha_s
\]

Ta có closed form mẫu (sample / 표본) trực tiếp bất kỳ timestep:

\[
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,
\qquad \epsilon\sim\mathcal N(0,I)
\]

As `t` large, tín hiệu (signal / 신호) destroyed và `x_t` gần Gaussian noise.

> **Chuyển mạch:** Trong **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Forward Diffusion tiến trình (process / 프로세스)** xác định đầu vào; **Reverse tiến trình (process / 프로세스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Tại sao predict noise giúp generation?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reverse tiến trình (process / 프로세스)

Goal learn:

\[
p_\theta(x_{t-1}\mid x_t)
\]

Nếu biết noise/dữ liệu (data / 데이터) score, có thể gradually denoise.

DDPM parameterization phổ biến train neural mạng (network / 네트워크) predict added noise:

\[
\epsilon_\theta(x_t,t)
\]

Mất mát (loss / 손실) simplified:

\[
L=\mathbb E_{x_0,\epsilon,t}
\left[
\|\epsilon-\epsilon_\theta(x_t,t)\|^2
\right]
\]

Mạng (network / 네트워크) receives noisy mẫu (sample / 표본) + timestep and learns noise thành phần (component / 컴포넌트).

> **Chuyển mạch:** Ở chặng này của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Reverse tiến trình (process / 프로세스)** xác định đầu vào; **Tại sao predict noise giúp generation?** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Timestep Encoding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao predict noise giúp generation?

From:

\[
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
\]

if mô hình (model / 모델) estimates `ε`, one can estimate clean `x_0` or reverse mean. Repeating reverse steps gradually reconstructs cấu trúc dữ liệu (data structure / 자료구조).

Mô hình (model / 모델) is học tập (learning / 학습) denoising véc-tơ (vector / 벡터) trường dữ liệu (field / 필드) across noise levels, not memorizing one deterministic ánh xạ (mapping / 매핑) noise→ảnh (image / 이미지) in single jump.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Timestep Encoding** tiếp nhận điểm tựa từ **Tại sao predict noise giúp generation?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **U-Net kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Timestep Encoding

Same noisy ảnh (image / 이미지) at low vs high noise requires different denoising hành vi (behavior / 동작). mô hình (model / 모델) therefore receives timestep/noise mức (level / 수준) embedding.

Sinusoidal/Fourier-like embeddings map scalar `t` into véc-tơ (vector / 벡터) processed alongside features.

> **Chuyển mạch:** Trong **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **U-Net kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Timestep Encoding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conditional Diffusion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## U-Net kiến trúc (architecture / 아키텍처)

Ảnh (image / 이미지) diffusion historically uses U-Net:

```text
high resolution
→ downsample encoder
→ bottleneck
→ upsample decoder
```

Skip connections pass fine spatial details from down đường dẫn (path / 경로) to up đường dẫn (path / 경로).

Hiện đại (modern / 현대적) diffusion U-Nets include residual blocks, attention/cross-attention and normalization.

Transformer-based diffusion architectures (DiT-like) increasingly replace/augment U-Net at quy mô (scale / 규모).

> **Chuyển mạch:** Ở chặng này của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Conditional Diffusion** tiếp nhận điểm tựa từ **U-Net kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Classifier Guidance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conditional Diffusion

Want generate `x` conditioned on văn bản (text / 텍스트)/lớp (class / 클래스) `c`:

\[
\epsilon_\theta(x_t,t,c)
\]

Văn bản (text / 텍스트) encoder creates embeddings; cross-attention injects văn bản (text / 텍스트) điều kiện (condition / 조건) into ảnh (image / 이미지) denoiser.

Thus text-to-image is multimodal encoder + conditional generative denoising hệ thống (system / 시스템).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Classifier Guidance** tiếp nhận điểm tựa từ **Conditional Diffusion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Classifier-Free Guidance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Classifier Guidance

An bên ngoài (external / 외부) classifier estimates:

\[
\nabla_{x_t}\log p(c\mid x_t)
\]

and modifies reverse score toward desired lớp (class / 클래스).

This improved conditional chất lượng (quality / 품질) but requires classifier trained on noisy dữ liệu (data / 데이터).

> **Chuyển mạch:** Trong **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Classifier-Free Guidance** tiếp nhận điểm tựa từ **Classifier Guidance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Score-Based View** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Classifier-Free Guidance

Train same mô hình (model / 모델) sometimes with điều kiện (condition / 조건) dropped. At suy luận (inference / 추론) combine conditional and unconditional predictions:

\[
\epsilon_{guided}
=\epsilon_{uncond}
+w(\epsilon_{cond}-\epsilon_{uncond})
\]

`w` guidance quy mô (scale / 규모).

Higher guidance often increases prompt adherence but can reduce diversity/oversaturate artifacts. sự đánh đổi (trade-off / 트레이드오프), not “higher better”.

> **Chuyển mạch:** Ở chặng này của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Score-Based View** tiếp nhận điểm tựa từ **Classifier-Free Guidance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sampling Speed** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Score-Based View

Score hàm (function / 함수):

\[
\nabla_x\log p_t(x)
\]

points toward directions increasing dữ liệu (data / 데이터) density at noise mức (level / 수준) `t`.

Denoising-score matching and diffusion are closely connected. Continuous-time formulation uses stochastic differential equations (SDEs).

This provides deeper probabilistic interpretation beyond “predict noise”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Sampling Speed** tiếp nhận điểm tựa từ **Score-Based View** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DDIM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sampling Speed

Original DDPM uses many reverse steps (hundreds/thousands), slower than one-pass GAN.

Accelerations:

- DDIM;
- higher-order samplers;
- DPM-Solver-like methods;
- distillation/consistency các mô hình (models / 모델들);
- fewer-step schedules.

Sampler changes numerical tích hợp (integration / 통합)/đường dẫn (path / 경로), often trading speed vs chất lượng (quality / 품질)/diversity.

> **Chuyển mạch:** Trong **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **DDIM** tiếp nhận điểm tựa từ **Sampling Speed** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Latent Diffusion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DDIM

DDIM constructs non-Markovian/deterministic-like sampling paths sharing huấn luyện (training / 학습) mục tiêu (objective / 목표), enabling fewer steps and latent interpolation hành vi (behavior / 동작).

`η`-style settings can điều khiển (control / 제어) stochasticity depending formulation.

> **Chuyển mạch:** Ở chặng này của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Latent Diffusion** tiếp nhận điểm tựa từ **DDIM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Image-to-Image và Inpainting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Latent Diffusion

Raw điểm ảnh (pixel / 픽셀) diffusion expensive. Latent diffusion first compress ảnh (image / 이미지):

\[
x\xrightarrow{VAE\ encoder}z
\]

run diffusion on `z`, then:

\[
z_0\xrightarrow{VAE\ decoder}\hat x
\]

Latent spatial resolution smaller → attention/U-Net computation drastically cheaper.

This is why understanding VAE matters for text-to-image các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Image-to-Image và Inpainting** tiếp nhận điểm tựa từ **Latent Diffusion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ControlNet-like Conditioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Image-to-Image và Inpainting

Image-to-image starts from encoded đầu vào (input / 입력) plus controlled noise then denoises under văn bản (text / 텍스트) điều kiện (condition / 조건). Noise strength controls how far đầu ra (output / 출력) may deviate.

Inpainting keeps known pixels/latent regions constrained and denoises masked region using surrounding ngữ cảnh (context / 맥락) + prompt.

Outpainting extends canvas similarly.

These are conditioning/điều khiển (control / 제어) variations, not completely different mô hình (model / 모델) classes.

> **Chuyển mạch:** Trong **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **ControlNet-like Conditioning** tiếp nhận điểm tựa từ **Image-to-Image và Inpainting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Diffusion vs VAE vs GAN** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ControlNet-like Conditioning

Additional structural điều kiện (condition / 조건) such as edge map, pose, độ sâu (depth / 깊이) can feed parallel/điều khiển (control / 제어) branch while preserving pretrained diffusion mô hình (model / 모델).

This separates ngữ nghĩa (semantic / 의미적) văn bản (text / 텍스트) điều khiển (control / 제어) from geometric/spatial điều khiển (control / 제어).

> **Chuyển mạch:** Ở chặng này của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Diffusion vs VAE vs GAN** tiếp nhận điểm tựa từ **ControlNet-like Conditioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Diffusion for non-image dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Diffusion vs VAE vs GAN

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Family | Training signal | Sampling | Typical trade-off |
|---|---|---|---|
| VAE | ELBO / reconstruction + KL | one decoder pass | smooth latent, likelihood khung phần mềm (framework / 프레임워크), sometimes softer samples |
| GAN | adversarial critic | one generator pass | sharp/fast, unstable/chế độ (mode / 모드) collapse rủi ro (risk / 위험) |
| Diffusion | denoising/score mục tiêu (objective / 목표) | iterative | stable/high chất lượng (quality / 품질), traditionally slower |

Hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) hybridize, so taxonomy describes mechanisms, not sản phẩm (product / 제품) boundaries.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Diffusion vs VAE vs GAN** nêu điều cần giải thích; **Diffusion for non-image dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dữ liệu (data / 데이터) and Copyright/an toàn (safety / 안전) liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Diffusion for non-image dữ liệu (data / 데이터)

Diffusion/score methods apply audio, video, 3D, molecule, continuous actions. Discrete diffusion variants adapt tiến trình (process / 프로세스) to categorical/đơn vị từ (token / 토큰) spaces.

However discrete ngôn ngữ (language / 언어) generation remains dominated autoregressive Transformers because corruption/reverse tiến trình (process / 프로세스) and decoding trade-offs differ.

> **Chuyển mạch:** Trong **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Diffusion for non-image dữ liệu (data / 데이터)** nêu điều cần giải thích; **Dữ liệu (data / 데이터) and Copyright/an toàn (safety / 안전) liên kết (connection / 연결)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) and Copyright/an toàn (safety / 안전) liên kết (connection / 연결)

Generative mô hình (model / 모델) hành vi (behavior / 동작) reflects huấn luyện (training / 학습) phân phối (distribution / 분포). Memorization can occur; mô hình (model / 모델) may reproduce styles/concepts/biases. Dataset provenance and deduplication matter.

An toàn (safety / 안전) filters can operate dữ liệu huấn luyện (training data / 학습 데이터), prompt, latent/generation and đầu ra (output / 출력) — hệ thống (system / 시스템) bài toán (problem / 문제) beyond diffusion math.

> **Chuyển mạch:** Ở chặng này của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, các dấu vết trong **Dữ liệu (data / 데이터) and Copyright/an toàn (safety / 안전) liên kết (connection / 연결)** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Training:
real data → add known noise level → model predicts how to remove noise

Generation:
random noise → denoise a little → denoise a little → ... → structured sample
```

At every noise mức (level / 수준), mô hình (model / 모델) learns cục bộ (local / 로컬) direction toward plausible dữ liệu (data / 데이터).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Diffusion stores images then retrieves nearest one”

Generation runs learned denoising dynamics. Memorization is separate rủi ro (risk / 위험), not cốt lõi (core / 핵심) cơ chế (mechanism / 메커니즘).

### “Noise prediction is arbitrary trick”

It arises from parameterization of reverse probabilistic/score tiến trình (process / 프로세스) and yields simple stable mục tiêu (objective / 목표).

### “More diffusion steps always better”

Sampler/thứ tự (order / 순서)/huấn luyện (training / 학습) determine sự đánh đổi (trade-off / 트레이드오프); advanced samplers achieve chất lượng (quality / 품질) with fewer steps.

### “Guidance quy mô (scale / 규모) controls ảnh (image / 이미지) chất lượng (quality / 품질) only”

It trades conditioning strength against diversity/artifacts.

### “Stable Diffusion means diffusion is done directly in pixels”

Latent diffusion operates in VAE-compressed latent không gian (space / 공간), then decodes to pixels.

> **Chuyển mạch:** Trong **Diffusion các mô hình (models / 모델들): tạo dữ liệu bằng quá trình khử nhiễu có điều kiện**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Diffusion synthesizes [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [Numerical Methods](../01_mathematical_foundations/07_numerical_computation.md), [Autoencoder/VAE](./06_autoencoders.md), [Attention](./04_attention.md) and multimodal văn bản (text / 텍스트) conditioning.

Later `13_speech_audio_and_multimodal/` will connect diffusion with text/image/audio/video foundation systems.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
