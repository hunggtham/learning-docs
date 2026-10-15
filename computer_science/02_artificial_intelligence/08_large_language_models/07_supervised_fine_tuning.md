# Supervised Fine-Tuning (SFT)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Supervised fine-tuning (SFT)**. Route đi từ pretrained checkpoint → labeled demonstrations → loss masking and batching → catastrophic forgetting/overfitting → evaluation and deployment, để SFT được phân biệt với pretraining bằng dữ liệu và mục tiêu tối ưu.

**Supervised Fine-Tuning (SFT / 지도 미세조정 / tinh chỉnh có giám sát)** là giai đoạn tiếp tục train một pretrained mô hình (model / 모델) trên tập examples có đầu vào (input / 입력) và desired đầu ra (output / 출력) rõ ràng. Với chat mô hình (model / 모델), một mẫu (sample / 표본) có thể gồm hệ thống (system / 시스템) message, người dùng (user / 사용자) yêu cầu (request / 요청) và assistant phản hồi (response / 응답) chuẩn.

Nếu pretraining học phân phối (distribution / 분포) rộng của ngôn ngữ (language / 언어), SFT ép độ dốc (gradient / 기울기) tập trung vào **hành vi (behavior / 동작) phân phối (distribution / 분포) mong muốn**.

## Mục tiêu (objective / 목표)

Về mặt toán học, SFT thường vẫn dùng next-token cross-entropy trên mục tiêu (target / 대상) phản hồi (response / 응답):

\[
\mathcal L_{SFT}=-\sum_{t\in phản hồi (response / 응답)}\log P_\theta(y_t\mid x,y_{<t})
\]

`x` là instruction/ngữ cảnh (context / 맥락), còn `y` là desired answer.

Nhiều chuỗi xử lý (pipeline / 파이프라인) mask mất mát (loss / 손실) trên người dùng (user / 사용자)/hệ thống (system / 시스템) tokens và chỉ optimize assistant tokens. Như vậy mô hình (model / 모델) không bị train để “predict người dùng (user / 사용자)” mà tập trung tái tạo phản hồi (response / 응답) hành vi (behavior / 동작).

Mục tiêu loss cho biết tín hiệu nào được tối ưu; sự khác biệt thực tế giữa SFT và pretraining nằm ở phân phối dữ liệu và mức độ giám sát. Vì vậy, trước hết cần đặt hai quy trình cạnh nhau.

## SFT khác pretraining ở đâu?

Cơ chế (mechanism / 메커니즘) optimizer/backprop có thể giống, nhưng **dữ liệu (data / 데이터) phân phối (distribution / 분포) và supervision tín hiệu (signal / 신호)** khác.

Pretraining:

```text
raw corpus → predict next token everywhere
```

SFT:

```text
instruction/context → imitate curated target response
```

SFT vì vậy gần hành vi (behavior / 동작) cloning hơn raw ngôn ngữ (language / 언어) modeling.

Nếu pretraining cung cấp nền năng lực rộng, SFT chọn những hành vi sẽ được bắt chước và củng cố. Chất lượng ví dụ vì thế quyết định trực tiếp chất lượng hành vi, còn loss masking và template quyết định tín hiệu đó đi vào mô hình ra sao.

## Dữ liệu (data / 데이터) chất lượng (quality / 품질) quyết định hành vi (behavior / 동작) chất lượng (quality / 품질)

Một SFT dataset nhỏ nhưng curated có thể thay đổi hành vi (behavior / 동작) mạnh vì pretrained mô hình (model / 모델) đã có năng lực (capability / 역량) nền. Nhưng nếu mục tiêu (target / 대상) responses verbose, evasive, overconfident hoặc inconsistent, mô hình (model / 모델) sẽ bắt chước mẫu (pattern / 패턴) đó.

SFT dữ liệu (data / 데이터) cần represent nhiều dimensions:

- tính đúng đắn (correctness / 정확성);
- instruction adherence;
- style/độ sâu (depth / 깊이);
- refusal hành vi (behavior / 동작);
- công cụ (tool / 도구) format;
- multilingual coverage;
- ambiguity handling.

Ví dụ tốt chỉ có tác dụng khi pipeline gán đúng role và vị trí chịu loss. Sau khi kiểm soát hai điều đó, ta mới có thể cân nhắc cập nhật toàn bộ weights hay chỉ một phần parameters.

## Mất mát (loss / 손실) masking và conversation templates

Chat template quyết định đơn vị từ (token / 토큰) nào đại diện role boundaries. Một mismatch giữa huấn luyện (training / 학습) template và serving template có thể làm mô hình (model / 모델) hành vi (behavior / 동작) giảm dù weights không đổi.

Ví dụ mô hình (model / 모델) được train với special tokens:

```text
<|system|> ...
<|user|> ...
<|assistant|> ...
```

nhưng suy luận (inference / 추론) dùng format khác, mô hình (model / 모델) có thể không recognize role ngữ nghĩa (semantics / 의미론) đúng như huấn luyện (training / 학습).

Masking và template ảnh hưởng tín hiệu học, còn lựa chọn full fine-tuning hay PEFT quyết định phạm vi tham số được phép thay đổi. Khi nhu cầu chỉ nằm trong một lĩnh vực, câu hỏi tiếp theo là mức thay đổi đó có cần được giới hạn theo domain hay không.

## Full fine-tuning vs parameter-efficient fine-tuning

**Full fine-tuning** cập nhật gần như toàn bộ mô hình (model / 모델) weights. Nó linh hoạt nhưng tốn bộ nhớ (memory / 메모리)/compute và có rủi ro (risk / 위험) catastrophic forgetting.

**Parameter-Efficient Fine-Tuning (PEFT)** chỉ train một subset parameters hoặc adapters. LoRA là ví dụ nổi tiếng:

\[
W' = W + BA
\]

với rank nhỏ `r`, nên số trainable parameters giảm mạnh.

LoRA không “compress toàn bộ mô hình (model / 모델)”; nó học một low-rank cập nhật (update / 업데이트) trên một số matrices được chọn.

Domain fine-tuning thay đổi vocabulary và format cần thiết, nhưng không nên dùng weights để thay thế dữ liệu luôn biến động. Cách trộn domain examples với general và safety examples sẽ quyết định sự cân bằng đó.

## Lĩnh vực (domain / 도메인) fine-tuning

Nếu tác vụ (task / 작업) yêu cầu terminology và đầu ra (output / 출력) style đặc thù, SFT lĩnh vực (domain / 도메인) có thể rất hữu ích. Ví dụ financial hỗ trợ (support / 지원) assistant cần phản hồi (response / 응답) format, tone và escalation lô-gic (logic / 논리) ổn định.

Nhưng facts thường xuyên thay đổi vẫn nên đến từ cơ sở dữ liệu (database / 데이터베이스)/RAG, không nên hard-code qua weights nếu provenance quan trọng.

Mixture quyết định hành vi nào được ưu tiên khi các mục tiêu cạnh tranh nhau. Trong chat SFT, ưu tiên đó còn được thể hiện bằng việc chỉ tính loss trên response hay trên toàn chuỗi.

## Curriculum và mixture

SFT dataset thường là mixture của general instruction, lĩnh vực (domain / 도메인) tasks, an toàn (safety / 안전) dữ liệu (data / 데이터) và công cụ (tool / 도구) use. Weighting ảnh hưởng độ dốc (gradient / 기울기).

Nếu an toàn (safety / 안전) examples quá nhiều và simplistic, over-refusal tăng. Nếu lĩnh vực (domain / 도메인) dữ liệu (data / 데이터) quá mạnh, general năng lực (capability / 역량) có thể giảm.

Response-only loss tập trung tín hiệu vào câu trả lời, nhưng system và user context vẫn điều kiện hóa biểu diễn. Khi nhiều mẫu được đưa vào một batch, sequence packing phải giữ nguyên các ranh giới ngữ nghĩa ấy.

## Response-only mất mát (loss / 손실)

Trong chat SFT, một practice phổ biến là tính mất mát (loss / 손실) chỉ trên assistant phản hồi (response / 응답). Điều này tránh mô hình (model / 모델) học reproduce người dùng (user / 사용자) văn bản (text / 텍스트).

Tuy nhiên hệ thống (system / 시스템) prompt cấu trúc (structure / 구조) vẫn ảnh hưởng hidden biểu diễn (representation / 표현) vì nó nằm trong ngữ cảnh (context / 맥락) dù không chịu mất mát (loss / 손실) trực tiếp.

Response-only loss xác định vị trí tạo gradient; packing xác định cách các mẫu chia sẻ hạ tầng mà không nhìn lẫn nhau. Nếu dataset vẫn nhỏ so với model, cần kiểm tra tiếp nguy cơ mô hình ghi nhớ format hoặc câu trả lời.

## Chuỗi (sequence / 시퀀스) packing

Nhiều short SFT samples có thể pack vào một huấn luyện (training / 학습) chuỗi (sequence / 시퀀스) để tăng utilization. Attention/mất mát (loss / 손실) masks phải đảm bảo samples không leak ngữ cảnh (context / 맥락) lẫn nhau ngoài intended packing ngữ nghĩa (semantics / 의미론).

Packing đúng giúp sử dụng compute hiệu quả nhưng không làm giảm nguy cơ overfit. Sau khi đánh giá nguy cơ đó, cần xem các traces được đưa vào dataset có làm mô hình học được lập luận đáng tin hay chỉ học một mẫu trình bày.

## Overfitting trong SFT

SFT dataset thường nhỏ hơn pretraining corpus rất nhiều. mô hình (model / 모델) lớn có thể memorize formatting hoặc chính xác (exact / 정확한) answers nhanh.

Kiểm tra hợp lệ (validation / 검증) cần đo:

```text
training loss
validation loss
behavior evals
out-of-template generalization
```

SFT mất mát (loss / 손실) thấp không đồng nghĩa assistant tốt.

Overfitting có thể nằm ở câu trả lời, format hoặc cả rationale. Vì thế, traces phải được kiểm tra về tính đúng đắn trước khi dùng SFT để distill hành vi từ một teacher mạnh hơn.

## SFT và lập luận (reasoning / 추론) traces

Dataset có thể chứa rationale hoặc chain-like solution steps. mô hình (model / 모델) có thể học mẫu (pattern / 패턴) giải từng bước, nhưng chất lượng (quality / 품질) phụ thuộc tính đúng đắn (correctness / 정확성) của traces.

Nếu traces chứa plausible nhưng incorrect lập luận (reasoning / 추론), mô hình (model / 모델) cũng bắt chước.

Không nên assume dài hơn = lập luận (reasoning / 추론) tốt hơn.

Teacher traces có thể truyền cách giải và style, nhưng student chỉ học những gì xuất hiện trong responses. Khi hành vi cần tương tác với hệ thống bên ngoài, dataset phải mô tả cả tool call và kết quả tool.

## Distillation bằng SFT

Một teacher mô hình (model / 모델) mạnh có thể generate responses, sau đó student train bằng SFT. Đây là một dạng kiến thức (knowledge / 지식) distillation ở hành vi (behavior / 동작) mức (level / 수준).

Student học phân phối (distribution / 분포) đầu ra (output / 출력) của teacher, nhưng không nhất thiết bản sao (copy / 복사) nội bộ (internal / 내부) cơ chế (mechanism / 메커니즘).

Tool-use SFT dạy cú pháp và lựa chọn hành động, còn runtime vẫn phải kiểm tra schema, quyền và lỗi. Vì vậy, sau hành vi tool-use cần đánh giá mô hình có diễn đạt mức chắc chắn phù hợp với bằng chứng hay không.

## Tool-use SFT

Để mô hình (model / 모델) gọi tools, dataset có thể chứa examples:

```text
user request
→ tool call JSON
→ tool result
→ final answer
```

SFT giúp mô hình (model / 모델) học cú pháp (syntax / 문법) và quyết định (decision / 결정) patterns. Nhưng môi trường vận hành (production / 운영 환경) vẫn cần lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증), permissions và thời gian chạy (runtime / 런타임) lỗi (error / 오류) handling.

Tool-use đúng cú pháp chưa đồng nghĩa với câu trả lời đúng hoặc được calibration tốt. Mental model dưới đây gom mục tiêu, dữ liệu, gradient và runtime boundary thành một cách đọc thống nhất.

## SFT và calibration

SFT có thể làm mô hình (model / 모델) answers trông tự tin hơn mà không cải thiện factual calibration tương ứng. Vì vậy preference về “confident helpful style” có thể tạo overconfidence.

Evaluation phải tách style và tính đúng đắn (correctness / 정확성).

Hãy nhớ SFT là lớp điều chỉnh hành vi trên nền năng lực pretrained; nó có thể thay đổi cách trả lời mà không đảm bảo thêm sự thật mới. Các ngộ nhận sau đây thường xuất hiện khi quên ranh giới đó.

## Mô hình tư duy (mental model / 사고 모델)

> SFT là **hành vi (behavior / 동작) imitation trên top của pretrained năng lực (capability / 역량)**.

Nó không thay thế pretraining, retrieval hay thời gian chạy (runtime / 런타임) xác minh (verification / 확인).

Các ngộ nhận đều nhầm lẫn giữa việc bắt chước target response và việc huấn luyện lại toàn bộ tri thức hay khả năng của mô hình. Phần liên kết kiến thức đặt SFT vào chuỗi instruction tuning → preference optimization để giữ đúng owner.

## Dùng chung (common / 공통) Misconceptions

### “SFT train mô hình (model / 모델) từ đầu cho tác vụ (task / 작업)”

Không. Với LLM, SFT thường là small post-training phase trên pretrained mô hình (model / 모델).

### “LoRA luôn cho kết quả giống full fine-tuning”

Không. Hiệu quả phụ thuộc rank, mục tiêu (target / 대상) modules, dữ liệu (data / 데이터) và mức thay đổi hành vi (behavior / 동작) cần thiết.

### “SFT dataset càng lớn càng tốt”

Bad/inconsistent examples có thể degrade hành vi (behavior / 동작). Curated chất lượng (quality / 품질) và coverage quan trọng hơn raw count.

## Liên kết kiến thức (knowledge connection / 지식 연결)

SFT là cầu giữa [Instruction Tuning](./06_instruction_tuning.md) và preference tối ưu hóa (optimization / 최적화). Khi multiple acceptable answers tồn tại, imitation một mục tiêu (target / 대상) không đủ để encode preference thứ tự (ordering / 순서). Đó là lý do RLHF/DPO xuất hiện.

Xem tiếp: [RLHF](./08_rlhf.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
