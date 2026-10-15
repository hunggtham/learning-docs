# LLM Tokenization: chuỗi (sequence / 시퀀스) length, vocabulary và mô hình (model / 모델) economics

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **LLM tokenization**. Route đi từ Unicode/text normalization → subword segmentation → vocabulary/sequence length → token cost/context window → multilingual and rare-token behavior, để cách cắt chuỗi nối trực tiếp với compute và chất lượng model.

LLM tokenization dùng cùng subword/byte principles của NLP, nhưng ở large-scale mô hình (model / 모델) nó trở thành vấn đề **compute, ngữ cảnh (context / 맥락) economics, multilingual fairness và giao thức (protocol / 프로토콜) tính tương thích (compatibility / 호환성)**. Một tokenizer không chỉ chia văn bản (text / 텍스트); nó quyết định mô hình (model / 모델) phải thực hiện bao nhiêu autoregressive steps để biểu diễn/generate cùng content.

Xem nền: [Text Normalization and Tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md). Chapter này tập trung LLM-specific consequences.

## Đơn vị từ (token / 토큰) là đơn vị compute của LLM

Huấn luyện (training / 학습)/suy luận (inference / 추론) chi phí (cost / 비용) thường quy mô (scale / 규모) theo đơn vị từ (token / 토큰) count. Một câu tokenize 20 tokens thay vì 10 roughly doubles chuỗi (sequence / 시퀀스) positions for many operations.

Autoregressive đầu ra (output / 출력) độ trễ (latency / 지연 시간) cũng proportional generated tokens because generation serial.

Therefore tokenizer efficiency affects:

```text
training FLOPs
context usage
KV cache
inference latency
API/token cost
multilingual UX
```

Token là đơn vị tính toán, còn vocabulary quyết định cách chuỗi được chia thành các token. Mục tiếp theo cho thấy byte-level BPE xây dựng vocabulary đó bằng các phép gộp như thế nào.

## Vocabulary kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)

Large vocabulary:

- shorter sequences;
- larger embedding/đầu ra (output / 출력) ma trận (matrix / 행렬);
- more rare đơn vị từ (token / 토큰) parameters;
- softmax/đầu ra (output / 출력) compute/bộ nhớ (memory / 메모리) bigger.

Small vocabulary:

- more subword reuse;
- longer sequences;
- smaller đơn vị từ (token / 토큰) matrices.

Optimal depends mô hình (model / 모델) kích thước (size / 크기)/dữ liệu (data / 데이터)/languages.

Byte-level BPE giúp tokenizer bao phủ nhiều script, nhưng số token cần cho cùng một nội dung vẫn thay đổi theo ngôn ngữ. Vì vậy, mục tiếp theo đo chi phí thực tế bằng token fertility.

## Byte-Level BPE

Many GPT-like tokenizers start bytes then merge frequent sequences. Any Unicode văn bản (text / 텍스트) can represent, avoiding `<UNK>`.

But scripts using multi-byte UTF-8 may need more cơ sở (base / 기반) units before merges. Underrepresented ngôn ngữ (language / 언어) gets fewer efficient merges.

Token fertility biến khác biệt tokenizer thành chi phí và độ dài ngữ cảnh có thể đo. Tiếp theo, hãy xem các khác biệt đó ảnh hưởng cụ thể ra sao với tiếng Hàn và tiếng Việt.

## Đơn vị từ (token / 토큰) Fertility

**Fertility** = average number tokens per word/character/content đơn vị (unit / 단위).

Higher fertility ngôn ngữ (language / 언어) consumes more ngữ cảnh (context / 맥락) and compute for same ngữ nghĩa (semantic / 의미적) message.

For multilingual triển khai (deployment / 배포), measure fertility separately Korean, Vietnamese, English and lĩnh vực (domain / 도메인) mã (code / 코드)/dữ liệu (data / 데이터).

Tác động ngôn ngữ xác nhận rằng không nên dùng heuristic tiếng Anh cho mọi corpus. Chat template là một lớp khác cũng biến cùng văn bản thành chuỗi token khác nhau, nên được xét ngay sau đây.

## Korean/Vietnamese practical tác động (effect / 효과)

Korean endings create many forms; good subword merges can reuse stem/morpheme patterns but corpus balance matters.

Vietnamese words may span syllables separated spaces; tokenizer may or may not merge dùng chung (common / 공통) multi-syllable expressions.

Do not assume 4 characters/đơn vị từ (token / 토큰) English heuristic across languages.

Chat template quy định role markers và thứ tự serialization mà mô hình đã được huấn luyện để đọc. Những marker này liên quan trực tiếp đến điều kiện bắt đầu, kết thúc và dừng sinh.

## Chat Templates

Instruction/chat các mô hình (models / 모델들) are trained with chính xác (exact / 정확한) serialization scheme. Example abstractly:

```text
<|system|>...
<|user|>...
<|assistant|>...
```

Special tokens delimit roles/turns.

If ứng dụng (application / 애플리케이션) manually builds prompt with wrong template, mô hình (model / 모델) sees phân phối (distribution / 분포) unlike post-training and may leak role văn bản (text / 텍스트)/behave poorly.

Always use official tokenizer/chat-template hiện thực (implementation / 구현) when possible.

BOS/EOS và stop condition là ranh giới giao thức, không chỉ là chuỗi ký tự tùy ý. Khi ranh giới token và ranh giới chuỗi lệch nhau, token healing có thể làm thay đổi kết quả tiếp nối.

## BOS/EOS and Stop Conditions

Beginning/end tokens affect generation boundaries. Chat turn may use special end-of-turn đơn vị từ (token / 토큰) distinct document EOS.

Suy luận (inference / 추론) máy chủ (server / 서버) stop lô-gic (logic / 논리) must align tokens/strings. Stopping by substring can truncate legitimate văn bản (text / 텍스트) or thất bại (fail / 실패) with đơn vị từ (token / 토큰) ranh giới (boundary / 경계) differences.

Token healing làm rõ vì sao cùng một prefix có thể được phân đoạn khác nhau khi autocomplete. Với số và dữ liệu có cấu trúc, ta cần kiểm tra thêm các quy tắc biểu diễn thay vì dựa vào trực giác token.

## Đơn vị từ (token / 토큰) Healing / ranh giới (boundary / 경계) Effects

Prompt ending inside a tokenizable word or with awkward whitespace can create tokenization phân phối (distribution / 분포) unlike huấn luyện (training / 학습). Some các hệ thống (systems / 시스템들) implement đơn vị từ (token / 토큰) healing/re-tokenization around ranh giới (boundary / 경계).

This matters autocomplete/mã (code / 코드) completion more than normal chat.

Số học và tokenization có thể không đồng nhất: một số được tạo từ nhiều mảnh token không mang giá trị số trực tiếp. Vì vậy, structured data cần schema và validation rõ ràng khi đi qua mô hình.

## Tokenization and Numbers

Numbers split into digit chunks unpredictably. This partly explains weak chính xác (exact / 정확한) arithmetic/counting: mô hình (model / 모델) operates statistical đơn vị từ (token / 토큰) patterns rather than bản địa (native / 네이티브) numeric datatype.

Tools/mã (code / 코드)/calculators should handle chính xác (exact / 정확한) arithmetic when độ tin cậy (reliability / 신뢰성) required.

Structured output giữ tính đúng của dữ liệu bằng quy tắc bên ngoài chuỗi token tự do. Khi tokenizer và embedding matrix không cùng vocabulary hoặc kích thước, pipeline sẽ hỏng trước cả bước sinh.

## Structured dữ liệu (data / 데이터)

JSON/XML/mã (code / 코드) punctuation can consume many tokens. Minified format saves tokens but may reduce readability/mô hình (model / 모델) độ tin cậy (reliability / 신뢰성); pretty format uses more ngữ cảnh (context / 맥락).

Lược đồ (schema / 스키마) thiết kế (design / 설계) can optimize both validity and đơn vị từ (token / 토큰) chi phí (cost / 비용). Repeated long trường dữ liệu (field / 필드) names increase đầu ra (output / 출력) tokens.

Tokenizer và embedding matrix là một cặp phiên bản: token ID chỉ có nghĩa trong vocabulary mà embedding đã học. Special tokens mở rộng giao thức và tạo thêm ranh giới cần bảo vệ.

## Tokenizer and Embedding ma trận (matrix / 행렬) tính tương thích (compatibility / 호환성)

Mô hình (model / 모델) checkpoint assumes chính xác (exact / 정확한) ánh xạ (mapping / 매핑):

\[
đơn vị từ (token / 토큰)\ string\leftrightarrow đơn vị từ (token / 토큰)\ id\leftrightarrow embedding\ row
\]

Swap tokenizer destroys ngữ nghĩa (semantics / 의미론) even if vocab kích thước (size / 크기) same.

Adding new tokens requires resize embedding/đầu ra (output / 출력) matrices and huấn luyện (training / 학습) those rows; naive addition does not teach meaning.

Special token có thể thay đổi role, stop behavior hoặc cấu trúc output, nên phải được coi như một phần của attack surface. Sau khi xác định ranh giới giao thức, ta lập kế hoạch ngân sách context.

## Special Tokens as Attack Surface

If untrusted văn bản (text / 텍스트) can inject role delimiters/special-control strings and ứng dụng (application / 애플리케이션) serializes poorly, instruction hierarchy may be confused.

Robust chat APIs should separate roles structurally and escape/encode người dùng (user / 사용자) dữ liệu (data / 데이터) according giao thức (protocol / 프로토콜) rather than concatenate raw pseudo-role markup.

Tokenizer/giao thức (protocol / 프로토콜) bảo mật (security / 보안) connects prompt injection.

Context budget phân bổ giới hạn giữa instruction, dữ liệu truy hồi và output. Những phần ổn định có thể được cache, nhưng chỉ khi serialization và semantics vẫn giữ nguyên.

## Ngữ cảnh (context / 맥락) ngân sách (budget / 예산) Planning

For ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) `C`:

```text
system instructions
+ conversation history
+ retrieved documents
+ tool results
+ user input
+ reserved output
≤ C tokens
```

If ngân sách (budget / 예산) exceeded, hệ thống (system / 시스템) needs truncate/summarize/retrieve selectively. Silent truncation may remove hệ thống (system / 시스템) instruction or crucial bằng chứng (evidence / 증거) depending hiện thực (implementation / 구현).

Prompt caching biến phần input lặp lại thành yếu tố economics có thể tối ưu. Để đánh giá đúng, cần tách token input khỏi token output vì hai loại có hành vi và chi phí khác nhau.

## Prompt Caching

Repeated prefix tokens can be cached by suy luận (inference / 추론) providers/servers, reducing prefill compute. bộ nhớ đệm (cache / 캐시) usually depends chính xác (exact / 정확한) đơn vị từ (token / 토큰) prefix, so tiny văn bản (text / 텍스트)/template thay đổi (change / 변경) invalidates hit.

Stable hệ thống (system / 시스템) prompt/lược đồ (schema / 스키마) organization can improve economics.

Phân biệt input và output token giúp nối tokenization với latency, context window và chi phí. Mental model sau đây tóm tắt các ranh giới đó thành một cách suy luận có thể tái dùng.

## Đầu vào (input / 입력) vs đầu ra (output / 출력) đơn vị từ (token / 토큰) chi phí (cost / 비용)

Transformer **prefill** processes đầu vào (input / 입력) tokens parallel-ish; **decode** generates đầu ra (output / 출력) one by one. Same đơn vị từ (token / 토큰) count has different độ trễ (latency / 지연 시간) characteristics.

Long đầu vào (input / 입력) increases prefill and KV bộ nhớ đệm (cache / 캐시); long đầu ra (output / 출력) increases serial decode độ trễ (latency / 지연 시간) strongly.

Hệ thống (system / 시스템) tối ưu hóa (optimization / 최적화) distinguishes both.

Mental model coi tokenizer như ABI giữa chuỗi người dùng và tensor computation. Các ngộ nhận chung sẽ kiểm tra những suy luận sai về ID, chi phí và tính tương thích.

## Mô hình tư duy (mental model / 사고 모델)

> Tokenizer is the ABI between human strings and LLM tensor computation. It defines chuỗi (sequence / 시퀀스) granularity, chi phí (cost / 비용) and giao thức (protocol / 프로토콜) boundaries; changing it is closer to changing mô hình (model / 모델) giao diện (interface / 인터페이스) than changing a văn bản (text / 텍스트) preprocessing option.

Các ngộ nhận đã tách bạch token ID, embedding, protocol và economics. Phần liên kết kiến thức tiếp theo chỉ rõ tài liệu owner để kiểm tra sâu hơn từng lớp.

## Dùng chung (common / 공통) Misconceptions

### “đơn vị từ (token / 토큰) count is roughly word count”

Varies ngôn ngữ (language / 언어)/content/tokenizer dramatically.

### “Tokenizer chất lượng (quality / 품질) only changes chi phí (cost / 비용)”

It affects chuỗi (sequence / 시퀀스) length, morphology sharing and mô hình (model / 모델) học tập (learning / 학습)/generation difficulty.

### “Chat roles are just văn bản (text / 텍스트) labels”

They are serialized through model-specific special đơn vị từ (token / 토큰)/template learned during post-training.

### “Add a đơn vị từ (token / 토큰) and mô hình (model / 모델) immediately understands it”

New embedding must be trained; ID alone has no ý nghĩa (semantic meaning / 의미적 뜻).

Các liên kết cuối cùng nối tokenization với language modeling, chat protocol và retrieval. Hãy quay về README để chọn bài tiếp theo theo mục tiêu học tập.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [NLP Tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md), [Transformer](../06_deep_learning_architectures/05_transformer.md) và later [Context Engineering](./11_prompting_and_context_engineering.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
