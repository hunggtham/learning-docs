# Speech, Audio and Multimodal AI — Reading Map

> **Mạch đọc:** Đây là README owner của **Speech, Audio and Multimodal AI**. Route đọc đi từ audio/speech signals → recognition/synthesis → multimodal representations → vision-language models → multimodal agents; mỗi chương nối một loại tín hiệu với model, task và giới hạn đánh giá tương ứng.

Folder này nối perception ngoài văn bản (text / 텍스트) vào AI hệ thống (system / 시스템): waveform/audio biểu diễn (representation / 표현) → ASR/TTS → multimodal alignment → Vision-Language các mô hình (models / 모델들) → multimodal Transformer → multimodal agents.

```mermaid
flowchart TD
    A[00 Audio & Speech Representation] --> ASR[01 Speech Recognition]
    A --> TTS[02 Speech Synthesis]
    ASR --> M[03 Multimodal Representation]
    TTS --> M
    V[Computer Vision] --> M
    M --> VLM[04 Vision-Language Models]
    M --> MT[05 Multimodal Transformers]
    VLM --> MA[06 Multimodal Agents]
    MT --> MA
```

## Chapters

Sơ đồ hoặc danh sách này mô tả thứ tự phụ thuộc của các khái niệm. Hãy đọc theo mũi tên để biết phần nào là prerequisite, phần nào là ứng dụng và khi nào cần quay lại nền tảng.

- [00 — Audio and Speech Representation](./00_audio_and_speech_representation.md)
- [01 — Speech Recognition](./01_speech_recognition.md)
- [02 — Speech Synthesis](./02_speech_synthesis.md)
- [03 — Multimodal Representation](./03_multimodal_representation.md)
- [04 — Vision-Language Models](./04_vision_language_models.md)
- [05 — Multimodal Transformers](./05_multimodal_transformers.md)
- [06 — Multimodal Agents](./06_multimodal_agents.md)

> **Chuyển mạch:** **Chapters** phân biệt waveform, spectrogram, token và modality alignment; **Core distinctions** gom chúng thành mental model cho từng đường biểu diễn.

## Cốt lõi (core / 핵심) distinctions

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

```text
Waveform ≠ Text
Spectrogram ≠ Ordinary Image
ASR ≠ Speaker Recognition
TTS ≠ Just Pronunciation
Shared Embedding ≠ Perfect Grounding
Vision-Language Model ≠ Exact Spatial Understanding
More Modalities ≠ Better Answer
Visual Text ≠ Trusted Instruction
Multimodal Agent ≠ VLM With Click Tool Only
```

> **Chuyển mạch:** Ở chặng này của **Speech, Audio and Multimodal AI — Reading Map**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Cốt lõi (core / 핵심) distinctions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Physical signals / visual scenes
→ modality-specific measurement
→ modality encoders
→ aligned/fused representation
→ language/reasoning
→ tool/action/output
```

The thư viện (library / 라이브러리) treats multimodal AI as an giao diện (interface / 인터페이스) bài toán (problem / 문제) between heterogeneous đo lường (measurement / 측정) spaces, not as a buzzword tầng (layer / 계층) over an LLM.

> **Chuyển mạch:** **Mental model** làm rõ trade-off giữa fidelity, latency và alignment; **Connections** trả trade-off đó về signal processing, NLP và vision owners.

## Connections

Nên đọc cùng:

- [Computer Vision](../12_computer_vision/README.md)
- [Transformer](../06_deep_learning_architectures/05_transformer.md)
- [Large Language Models](../08_large_language_models/README.md)
- [Agents](../10_agents_and_ai_systems/README.md)

Layer tiếp theo `14_data_for_ai/` tập trung vào material mà toàn bộ learning system phụ thuộc: data collection, labeling, quality, leakage, bias, synthetic data và governance.

> **Bàn giao:** Sau **Connections**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
