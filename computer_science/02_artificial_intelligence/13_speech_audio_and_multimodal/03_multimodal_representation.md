# Multimodal biểu diễn (representation / 표현)

> **Mạch đọc:** Đặt **Multimodal biểu diễn (representation / 표현)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao multimodal khó?** sang **Alignment**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Multimodal AI (멀티모달 AI)** xử lý và liên kết nhiều modality như văn bản (text / 텍스트), ảnh (image / 이미지), audio, video, sensor dữ liệu (data / 데이터). Thách thức không chỉ là có nhiều đầu vào (input / 입력); mô hình (model / 모델) phải học **biểu diễn (representation / 표현) tương thích** để biết thông tin nào tương ứng, bổ sung hay mâu thuẫn giữa modalities.

```text
text tokens
image patches
speech frames
video frames
sensor values
      ↓
modality encoders
      ↓
aligned / fused representations
      ↓
reasoning / generation / action
```

## Vì sao multimodal khó?

Mỗi modality có cấu trúc (structure / 구조) khác:

- văn bản (text / 텍스트): discrete chuỗi (sequence / 시퀀스), ngữ nghĩa (semantic / 의미적) dense;
- ảnh (image / 이미지): 2D spatial grid;
- audio: time-frequency tín hiệu (signal / 신호);
- video: không gian (space / 공간) + thời gian (time / 시간);
- sensor: continuous irregular streams.

Sampling rates khác nhau rất lớn. Một câu 5 giây có vài chục văn bản (text / 텍스트) tokens nhưng audio có hàng chục nghìn samples và video có hàng trăm frames.

## Alignment

Alignment hỏi: phần nào của modality A tương ứng phần nào của modality B?

Examples:

```text
caption ↔ whole image
word ↔ image region
phoneme ↔ audio frames
subtitle ↔ video segment
gesture ↔ spoken phrase
```

Alignment có thể coarse hoặc fine-grained.

## Dùng chung (shared / 공유) Embedding không gian (space / 공간)

Contrastive huấn luyện (training / 학습) đặt paired modalities gần nhau:

\[
sim(f_{img}(x),f_{văn bản (text / 텍스트)}(y))\uparrow
\]

Matched image-caption pair close, mismatched far.

Dùng chung (shared / 공유) không gian (space / 공간) useful retrieval/zero-shot transfer nhưng toàn cục (global / 전역) embedding có thể lose detailed spatial alignment.

## Modality-Specific Encoders

Dùng chung (common / 공통) kiến trúc (architecture / 아키텍처):

```text
vision encoder → visual tokens
speech encoder → audio tokens
text tokenizer/embedding → text tokens
```

Sau đó fusion tầng (layer / 계층)/projector maps tokens vào compatible hidden dimension.

Encoders preserve modality inductive biases.

## Early, Intermediate, Late Fusion

**Early fusion** combine raw/low-level features early. Có high tương tác (interaction / 상호작용) nhưng khó vì scales/statistics khác.

**Intermediate fusion** encode each modality first then cross-attention/joint layers. dùng chung (common / 공통) in hiện đại (modern / 현대적) các hệ thống (systems / 시스템들).

**Late fusion** combine final scores/embeddings. Simple/robust nhưng limited fine tương tác (interaction / 상호작용).

## Cross-Attention

One modality queries another:

\[
Attention(Q_{text},K_{vision},V_{vision})
\]

Văn bản (text / 텍스트) đơn vị từ (token / 토큰) có thể attend visual patches. Reverse direction cũng possible.

Cross-attention preserves modality separation while enabling tương tác (interaction / 상호작용).

## Unified đơn vị từ (token / 토큰) không gian (space / 공간)

Another approach converts modalities into tokens then tiến trình (process / 프로세스) one Transformer:

```text
[image tokens][audio tokens][text tokens]
```

Unified kiến trúc (architecture / 아키텍처) simplifies scaling but đơn vị từ (token / 토큰) counts and modality statistics require careful thiết kế (design / 설계).

## Modality Projector

Vision encoder dimension `D_v` và LLM hidden `D_l` khác. Projector:

\[
h_{llm}=Wh_v+b
\]

or small MLP maps biểu diễn (representation / 표현). Simple projector can công việc (work / 작업) surprisingly well if pretrained encoders already strong.

## Modality Gap

Even after same dimension, ảnh (image / 이미지)/văn bản (text / 텍스트) tính năng (feature / 기능) distributions differ. Alignment huấn luyện (training / 학습) teaches ngôn ngữ (language / 언어) mô hình (model / 모델) how visual features correspond ngôn ngữ (language / 언어) concepts.

## Paired dữ liệu (data / 데이터)

Multimodal học tập (learning / 학습) often relies paired dữ liệu (data / 데이터):

- image-caption;
- video-subtitle;
- speech-transcript;
- instruction + ảnh (image / 이미지) + phản hồi (response / 응답).

Pair chất lượng (quality / 품질) determines alignment. Web captions may describe only salient đối tượng (object / 객체), not every visual detail.

## Missing Modalities

Real các hệ thống (systems / 시스템들) may lack one modality. kiến trúc (architecture / 아키텍처) should handle:

```text
text only
image + text
image only
speech + text
```

Huấn luyện (training / 학습) only always-complete pairs may make mô hình (model / 모델) brittle.

## Complementary vs Redundant thông tin (information / 정보)

Audio and video may both reveal speech; ảnh (image / 이미지) and văn bản (text / 텍스트) may repeat same fact. Fusion should exploit complementarity without double-counting noisy correlated bằng chứng (evidence / 증거).

## Conflicting Modalities

Ảnh (image / 이미지) says red light, văn bản (text / 텍스트) siêu dữ liệu (metadata / 메타데이터) says green. Which nguồn (source / 소스) trusted? mô hình (model / 모델) needs độ tin cậy (reliability / 신뢰성)/authority priors and ứng dụng (application / 애플리케이션) may need tường minh (explicit / 명시적) nguồn (source / 소스) chính sách (policy / 정책).

## Grounding

**Grounding (그라운딩 / neo nghĩa vào dữ liệu nguồn)** means connect ngôn ngữ (language / 언어) claim to specific perceptual bằng chứng (evidence / 증거).

Examples:

- phrase “red cup” ↔ pixels/box;
- word timestamp ↔ audio frames;
- hành động (action / 동작) “person opens door” ↔ video segment.

Toàn cục (global / 전역) ngữ nghĩa (semantic / 의미적) alignment is not enough for precise grounding.

## Temporal Alignment

Video/audio tương tác (interaction / 상호작용) requires sync. Millisecond/second shifts can break lip-reading or sự kiện (event / 이벤트) understanding.

Timestamp normalization and sampling chuỗi xử lý (pipeline / 파이프라인) become part of mô hình (model / 모델) chất lượng (quality / 품질).

## Multimodal đơn vị từ (token / 토큰) ngân sách (budget / 예산)

Images/video can create thousands tokens. ngữ cảnh (context / 맥락) ngân sách (budget / 예산) sự đánh đổi (trade-off / 트레이드오프):

```text
higher visual resolution / more frames
→ more detail
→ more compute/context usage
```

Adaptive đơn vị từ (token / 토큰) selection/compression is important.

## Modality Compression

Perceiver/resampler modules compress many visual/audio tokens into smaller latent set before LLM. Compression must preserve task-relevant thông tin (information / 정보).

## Biểu diễn (representation / 표현) Bottleneck

If projector compresses ảnh (image / 이미지) into few tokens, OCR/small-detail info may disappear. Bigger LLM cannot recover thông tin (information / 정보) never passed through bottleneck.

## Pretraining Objectives

Possible objectives:

- contrastive alignment;
- image-text matching;
- caption generation;
- masked multimodal modeling;
- next-token prediction conditioned on visual/audio tokens;
- instruction following.

Mục tiêu (objective / 목표) shapes năng lực (capability / 역량).

## Multimodal Hallucination

Mô hình (model / 모델) may generate đối tượng (object / 객체) not present because ngôn ngữ (language / 언어) prior overwhelms visual bằng chứng (evidence / 증거). Evaluation needs distinguish perception thất bại (failure / 실패) vs lập luận (reasoning / 추론)/generation thất bại (failure / 실패).

## Mô hình tư duy (mental model / 사고 모델)

> **Multimodal biểu diễn (representation / 표현) is the bài toán (problem / 문제) of building interfaces between different đo lường (measurement / 측정) spaces so that corresponding thông tin (information / 정보) can interact without erasing modality-specific cấu trúc (structure / 구조).**

## Dùng chung (common / 공통) Misconceptions

### “Put ảnh (image / 이미지) embedding into LLM = true multimodal understanding”

It enables giao diện (interface / 인터페이스), but grounding/detail năng lực (capability / 역량) depends alignment dữ liệu (data / 데이터), projector and huấn luyện (training / 학습).

### “dùng chung (shared / 공유) embedding means all modalities have same meaning hình học (geometry / 기하학)”

Only to extent huấn luyện (training / 학습) mục tiêu (objective / 목표) aligns them.

### “More modalities always improve kết quả (result / 결과)”

Noisy/conflicting modalities can degrade đầu ra (output / 출력).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Multimodal biểu diễn (representation / 표현) connects [Modern Visual Representation](../12_computer_vision/08_modern_visual_representation.md), speech encoders, embeddings and attention.

Xem tiếp: [Vision-Language Models](./04_vision_language_models.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 audio and speech representation](./00_audio_and_speech_representation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
