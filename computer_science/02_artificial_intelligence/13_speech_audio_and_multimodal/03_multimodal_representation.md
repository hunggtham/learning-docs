# Multimodal biểu diễn (representation / 표현)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Multimodal representation**. Route đi từ modality-specific encoders → shared/paired spaces → alignment objectives → fusion and missing modalities → cross-modal transfer, để các tín hiệu khác nhau gặp nhau mà không mất cấu trúc riêng.

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

> **Chuyển mạch:** Trong **Multimodal biểu diễn (representation / 표현)**, **Alignment** tiếp nhận điểm tựa từ **Vì sao multimodal khó?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (shared / 공유) Embedding không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Multimodal biểu diễn (representation / 표현)**, **Dùng chung (shared / 공유) Embedding không gian (space / 공간)** tiếp nhận điểm tựa từ **Alignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modality-Specific Encoders** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (shared / 공유) Embedding không gian (space / 공간)

Contrastive huấn luyện (training / 학습) đặt paired modalities gần nhau:

\[
sim(f_{img}(x),f_{văn bản (text / 텍스트)}(y))\uparrow
\]

Matched image-caption pair close, mismatched far.

Dùng chung (shared / 공유) không gian (space / 공간) useful retrieval/zero-shot transfer nhưng toàn cục (global / 전역) embedding có thể lose detailed spatial alignment.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal biểu diễn (representation / 표현)**, **Modality-Specific Encoders** tiếp nhận điểm tựa từ **Dùng chung (shared / 공유) Embedding không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Early, Intermediate, Late Fusion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modality-Specific Encoders

Dùng chung (common / 공통) kiến trúc (architecture / 아키텍처):

```text
vision encoder → visual tokens
speech encoder → audio tokens
text tokenizer/embedding → text tokens
```

Sau đó fusion tầng (layer / 계층)/projector maps tokens vào compatible hidden dimension.

Encoders preserve modality inductive biases.

> **Chuyển mạch:** Trong **Multimodal biểu diễn (representation / 표현)**, **Early, Intermediate, Late Fusion** tiếp nhận điểm tựa từ **Modality-Specific Encoders** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cross-Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Early, Intermediate, Late Fusion

**Early fusion** combine raw/low-level features early. Có high tương tác (interaction / 상호작용) nhưng khó vì scales/statistics khác.

**Intermediate fusion** encode each modality first then cross-attention/joint layers. dùng chung (common / 공통) in hiện đại (modern / 현대적) các hệ thống (systems / 시스템들).

**Late fusion** combine final scores/embeddings. Simple/robust nhưng limited fine tương tác (interaction / 상호작용).

> **Chuyển mạch:** Ở chặng này của **Multimodal biểu diễn (representation / 표현)**, **Cross-Attention** tiếp nhận điểm tựa từ **Early, Intermediate, Late Fusion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Unified đơn vị từ (token / 토큰) không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cross-Attention

One modality queries another:

\[
Attention(Q_{text},K_{vision},V_{vision})
\]

Văn bản (text / 텍스트) đơn vị từ (token / 토큰) có thể attend visual patches. Reverse direction cũng possible.

Cross-attention preserves modality separation while enabling tương tác (interaction / 상호작용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal biểu diễn (representation / 표현)**, **Unified đơn vị từ (token / 토큰) không gian (space / 공간)** tiếp nhận điểm tựa từ **Cross-Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modality Projector** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Unified đơn vị từ (token / 토큰) không gian (space / 공간)

Another approach converts modalities into tokens then tiến trình (process / 프로세스) one Transformer:

```text
[image tokens][audio tokens][text tokens]
```

Unified kiến trúc (architecture / 아키텍처) simplifies scaling but đơn vị từ (token / 토큰) counts and modality statistics require careful thiết kế (design / 설계).

> **Chuyển mạch:** Trong **Multimodal biểu diễn (representation / 표현)**, **Modality Projector** tiếp nhận điểm tựa từ **Unified đơn vị từ (token / 토큰) không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modality Gap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modality Projector

Vision encoder dimension `D_v` và LLM hidden `D_l` khác. Projector:

\[
h_{llm}=Wh_v+b
\]

or small MLP maps biểu diễn (representation / 표현). Simple projector can công việc (work / 작업) surprisingly well if pretrained encoders already strong.

> **Chuyển mạch:** Ở chặng này của **Multimodal biểu diễn (representation / 표현)**, **Modality Gap** tiếp nhận điểm tựa từ **Modality Projector** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Paired dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modality Gap

Even after same dimension, ảnh (image / 이미지)/văn bản (text / 텍스트) tính năng (feature / 기능) distributions differ. Alignment huấn luyện (training / 학습) teaches ngôn ngữ (language / 언어) mô hình (model / 모델) how visual features correspond ngôn ngữ (language / 언어) concepts.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal biểu diễn (representation / 표현)**, **Modality Gap** nêu điều cần giải thích; **Paired dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Missing Modalities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Paired dữ liệu (data / 데이터)

Multimodal học tập (learning / 학습) often relies paired dữ liệu (data / 데이터):

- image-caption;
- video-subtitle;
- speech-transcript;
- instruction + ảnh (image / 이미지) + phản hồi (response / 응답).

Pair chất lượng (quality / 품질) determines alignment. Web captions may describe only salient đối tượng (object / 객체), not every visual detail.

> **Chuyển mạch:** Trong **Multimodal biểu diễn (representation / 표현)**, **Paired dữ liệu (data / 데이터)** nêu điều cần giải thích; **Missing Modalities** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Complementary vs Redundant thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Missing Modalities

Real các hệ thống (systems / 시스템들) may lack one modality. kiến trúc (architecture / 아키텍처) should handle:

```text
text only
image + text
image only
speech + text
```

Huấn luyện (training / 학습) only always-complete pairs may make mô hình (model / 모델) brittle.

> **Chuyển mạch:** Ở chặng này của **Multimodal biểu diễn (representation / 표현)**, **Complementary vs Redundant thông tin (information / 정보)** tiếp nhận điểm tựa từ **Missing Modalities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conflicting Modalities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Complementary vs Redundant thông tin (information / 정보)

Audio and video may both reveal speech; ảnh (image / 이미지) and văn bản (text / 텍스트) may repeat same fact. Fusion should exploit complementarity without double-counting noisy correlated bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal biểu diễn (representation / 표현)**, **Conflicting Modalities** tiếp nhận điểm tựa từ **Complementary vs Redundant thông tin (information / 정보)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Grounding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conflicting Modalities

Ảnh (image / 이미지) says red light, văn bản (text / 텍스트) siêu dữ liệu (metadata / 메타데이터) says green. Which nguồn (source / 소스) trusted? mô hình (model / 모델) needs độ tin cậy (reliability / 신뢰성)/authority priors and ứng dụng (application / 애플리케이션) may need tường minh (explicit / 명시적) nguồn (source / 소스) chính sách (policy / 정책).

> **Chuyển mạch:** Trong **Multimodal biểu diễn (representation / 표현)**, **Grounding** tiếp nhận điểm tựa từ **Conflicting Modalities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Temporal Alignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Grounding

**Grounding (그라운딩 / neo nghĩa vào dữ liệu nguồn)** means connect ngôn ngữ (language / 언어) claim to specific perceptual bằng chứng (evidence / 증거).

Examples:

- phrase “red cup” ↔ pixels/box;
- word timestamp ↔ audio frames;
- hành động (action / 동작) “person opens door” ↔ video segment.

Toàn cục (global / 전역) ngữ nghĩa (semantic / 의미적) alignment is not enough for precise grounding.

> **Chuyển mạch:** Ở chặng này của **Multimodal biểu diễn (representation / 표현)**, **Temporal Alignment** tiếp nhận điểm tựa từ **Grounding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multimodal đơn vị từ (token / 토큰) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Temporal Alignment

Video/audio tương tác (interaction / 상호작용) requires sync. Millisecond/second shifts can break lip-reading or sự kiện (event / 이벤트) understanding.

Timestamp normalization and sampling chuỗi xử lý (pipeline / 파이프라인) become part of mô hình (model / 모델) chất lượng (quality / 품질).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal biểu diễn (representation / 표현)**, **Multimodal đơn vị từ (token / 토큰) ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **Temporal Alignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modality Compression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multimodal đơn vị từ (token / 토큰) ngân sách (budget / 예산)

Images/video can create thousands tokens. ngữ cảnh (context / 맥락) ngân sách (budget / 예산) sự đánh đổi (trade-off / 트레이드오프):

```text
higher visual resolution / more frames
→ more detail
→ more compute/context usage
```

Adaptive đơn vị từ (token / 토큰) selection/compression is important.

> **Chuyển mạch:** Trong **Multimodal biểu diễn (representation / 표현)**, **Modality Compression** tiếp nhận điểm tựa từ **Multimodal đơn vị từ (token / 토큰) ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biểu diễn (representation / 표현) Bottleneck** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modality Compression

Perceiver/resampler modules compress many visual/audio tokens into smaller latent set before LLM. Compression must preserve task-relevant thông tin (information / 정보).

> **Chuyển mạch:** Ở chặng này của **Multimodal biểu diễn (representation / 표현)**, **Biểu diễn (representation / 표현) Bottleneck** tiếp nhận điểm tựa từ **Modality Compression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pretraining Objectives** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn (representation / 표현) Bottleneck

If projector compresses ảnh (image / 이미지) into few tokens, OCR/small-detail info may disappear. Bigger LLM cannot recover thông tin (information / 정보) never passed through bottleneck.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal biểu diễn (representation / 표현)**, **Pretraining Objectives** tiếp nhận điểm tựa từ **Biểu diễn (representation / 표현) Bottleneck** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multimodal Hallucination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pretraining Objectives

Possible objectives:

- contrastive alignment;
- image-text matching;
- caption generation;
- masked multimodal modeling;
- next-token prediction conditioned on visual/audio tokens;
- instruction following.

Mục tiêu (objective / 목표) shapes năng lực (capability / 역량).

> **Chuyển mạch:** Trong **Multimodal biểu diễn (representation / 표현)**, **Multimodal Hallucination** tiếp nhận điểm tựa từ **Pretraining Objectives** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multimodal Hallucination

Mô hình (model / 모델) may generate đối tượng (object / 객체) not present because ngôn ngữ (language / 언어) prior overwhelms visual bằng chứng (evidence / 증거). Evaluation needs distinguish perception thất bại (failure / 실패) vs lập luận (reasoning / 추론)/generation thất bại (failure / 실패).

> **Chuyển mạch:** Ở chặng này của **Multimodal biểu diễn (representation / 표현)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Multimodal Hallucination** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Multimodal biểu diễn (representation / 표현) is the bài toán (problem / 문제) of building interfaces between different đo lường (measurement / 측정) spaces so that corresponding thông tin (information / 정보) can interact without erasing modality-specific cấu trúc (structure / 구조).**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal biểu diễn (representation / 표현)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Put ảnh (image / 이미지) embedding into LLM = true multimodal understanding”

It enables giao diện (interface / 인터페이스), but grounding/detail năng lực (capability / 역량) depends alignment dữ liệu (data / 데이터), projector and huấn luyện (training / 학습).

### “dùng chung (shared / 공유) embedding means all modalities have same meaning hình học (geometry / 기하학)”

Only to extent huấn luyện (training / 학습) mục tiêu (objective / 목표) aligns them.

### “More modalities always improve kết quả (result / 결과)”

Noisy/conflicting modalities can degrade đầu ra (output / 출력).

> **Chuyển mạch:** Trong **Multimodal biểu diễn (representation / 표현)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Multimodal biểu diễn (representation / 표현) connects [Modern Visual Representation](../12_computer_vision/08_modern_visual_representation.md), speech encoders, embeddings and attention.

Xem tiếp: [Vision-Language Models](./04_vision_language_models.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
