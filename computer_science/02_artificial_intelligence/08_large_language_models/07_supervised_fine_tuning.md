# Supervised Fine-Tuning (SFT)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Supervised Fine-Tuning (SFT)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mục tiêu (objective / 목표)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **SFT khác pretraining ở đâu?** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Supervised Fine-Tuning (SFT / 지도 미세조정 / tinh chỉnh có giám sát)** là giai đoạn tiếp tục train một pretrained mô hình (model / 모델) trên tập examples có đầu vào (input / 입력) và desired đầu ra (output / 출력) rõ ràng. Với chat mô hình (model / 모델), một mẫu (sample / 표본) có thể gồm hệ thống (system / 시스템) message, người dùng (user / 사용자) yêu cầu (request / 요청) và assistant phản hồi (response / 응답) chuẩn.

Nếu pretraining học phân phối (distribution / 분포) rộng của ngôn ngữ (language / 언어), SFT ép độ dốc (gradient / 기울기) tập trung vào **hành vi (behavior / 동작) phân phối (distribution / 분포) mong muốn**.

## Mục tiêu (objective / 목표)

Về mặt toán học, SFT thường vẫn dùng next-token cross-entropy trên mục tiêu (target / 대상) phản hồi (response / 응답):

\[
\mathcal L_{SFT}=-\sum_{t\in phản hồi (response / 응답)}\log P_\theta(y_t\mid x,y_{<t})
\]

`x` là instruction/ngữ cảnh (context / 맥락), còn `y` là desired answer.

Nhiều chuỗi xử lý (pipeline / 파이프라인) mask mất mát (loss / 손실) trên người dùng (user / 사용자)/hệ thống (system / 시스템) tokens và chỉ optimize assistant tokens. Như vậy mô hình (model / 모델) không bị train để “predict người dùng (user / 사용자)” mà tập trung tái tạo phản hồi (response / 응답) hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **Supervised Fine-Tuning (SFT)**, **SFT khác pretraining ở đâu?** tiếp nhận điểm tựa từ **Mục tiêu (objective / 목표)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) chất lượng (quality / 품질) quyết định hành vi (behavior / 동작) chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Supervised Fine-Tuning (SFT)**, **SFT khác pretraining ở đâu?** nêu điều cần giải thích; **Dữ liệu (data / 데이터) chất lượng (quality / 품질) quyết định hành vi (behavior / 동작) chất lượng (quality / 품질)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mất mát (loss / 손실) masking và conversation templates** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Supervised Fine-Tuning (SFT)**, **Dữ liệu (data / 데이터) chất lượng (quality / 품질) quyết định hành vi (behavior / 동작) chất lượng (quality / 품질)** nêu điều cần giải thích; **Mất mát (loss / 손실) masking và conversation templates** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Full fine-tuning vs parameter-efficient fine-tuning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mất mát (loss / 손실) masking và conversation templates

Chat template quyết định đơn vị từ (token / 토큰) nào đại diện role boundaries. Một mismatch giữa huấn luyện (training / 학습) template và serving template có thể làm mô hình (model / 모델) hành vi (behavior / 동작) giảm dù weights không đổi.

Ví dụ mô hình (model / 모델) được train với special tokens:

```text
<|system|> ...
<|user|> ...
<|assistant|> ...
```

nhưng suy luận (inference / 추론) dùng format khác, mô hình (model / 모델) có thể không recognize role ngữ nghĩa (semantics / 의미론) đúng như huấn luyện (training / 학습).

> **Chuyển mạch:** Trong **Supervised Fine-Tuning (SFT)**, **Full fine-tuning vs parameter-efficient fine-tuning** tiếp nhận điểm tựa từ **Mất mát (loss / 손실) masking và conversation templates** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lĩnh vực (domain / 도메인) fine-tuning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Full fine-tuning vs parameter-efficient fine-tuning

**Full fine-tuning** cập nhật gần như toàn bộ mô hình (model / 모델) weights. Nó linh hoạt nhưng tốn bộ nhớ (memory / 메모리)/compute và có rủi ro (risk / 위험) catastrophic forgetting.

**Parameter-Efficient Fine-Tuning (PEFT)** chỉ train một subset parameters hoặc adapters. LoRA là ví dụ nổi tiếng:

\[
W' = W + BA
\]

với rank nhỏ `r`, nên số trainable parameters giảm mạnh.

LoRA không “compress toàn bộ mô hình (model / 모델)”; nó học một low-rank cập nhật (update / 업데이트) trên một số matrices được chọn.

> **Chuyển mạch:** Ở chặng này của **Supervised Fine-Tuning (SFT)**, **Lĩnh vực (domain / 도메인) fine-tuning** tiếp nhận điểm tựa từ **Full fine-tuning vs parameter-efficient fine-tuning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Curriculum và mixture** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lĩnh vực (domain / 도메인) fine-tuning

Nếu tác vụ (task / 작업) yêu cầu terminology và đầu ra (output / 출력) style đặc thù, SFT lĩnh vực (domain / 도메인) có thể rất hữu ích. Ví dụ financial hỗ trợ (support / 지원) assistant cần phản hồi (response / 응답) format, tone và escalation lô-gic (logic / 논리) ổn định.

Nhưng facts thường xuyên thay đổi vẫn nên đến từ cơ sở dữ liệu (database / 데이터베이스)/RAG, không nên hard-code qua weights nếu provenance quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Supervised Fine-Tuning (SFT)**, **Curriculum và mixture** tiếp nhận điểm tựa từ **Lĩnh vực (domain / 도메인) fine-tuning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Response-only mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Curriculum và mixture

SFT dataset thường là mixture của general instruction, lĩnh vực (domain / 도메인) tasks, an toàn (safety / 안전) dữ liệu (data / 데이터) và công cụ (tool / 도구) use. Weighting ảnh hưởng độ dốc (gradient / 기울기).

Nếu an toàn (safety / 안전) examples quá nhiều và simplistic, over-refusal tăng. Nếu lĩnh vực (domain / 도메인) dữ liệu (data / 데이터) quá mạnh, general năng lực (capability / 역량) có thể giảm.

> **Chuyển mạch:** Trong **Supervised Fine-Tuning (SFT)**, **Response-only mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Curriculum và mixture** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi (sequence / 시퀀스) packing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Response-only mất mát (loss / 손실)

Trong chat SFT, một practice phổ biến là tính mất mát (loss / 손실) chỉ trên assistant phản hồi (response / 응답). Điều này tránh mô hình (model / 모델) học reproduce người dùng (user / 사용자) văn bản (text / 텍스트).

Tuy nhiên hệ thống (system / 시스템) prompt cấu trúc (structure / 구조) vẫn ảnh hưởng hidden biểu diễn (representation / 표현) vì nó nằm trong ngữ cảnh (context / 맥락) dù không chịu mất mát (loss / 손실) trực tiếp.

> **Chuyển mạch:** Ở chặng này của **Supervised Fine-Tuning (SFT)**, **Response-only mất mát (loss / 손실)** xác định đầu vào; **Chuỗi (sequence / 시퀀스) packing** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Overfitting trong SFT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) packing

Nhiều short SFT samples có thể pack vào một huấn luyện (training / 학습) chuỗi (sequence / 시퀀스) để tăng utilization. Attention/mất mát (loss / 손실) masks phải đảm bảo samples không leak ngữ cảnh (context / 맥락) lẫn nhau ngoài intended packing ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Supervised Fine-Tuning (SFT)**, **Chuỗi (sequence / 시퀀스) packing** xác định đầu vào; **Overfitting trong SFT** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **SFT và lập luận (reasoning / 추론) traces** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Supervised Fine-Tuning (SFT)**, **SFT và lập luận (reasoning / 추론) traces** tiếp nhận điểm tựa từ **Overfitting trong SFT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Distillation bằng SFT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SFT và lập luận (reasoning / 추론) traces

Dataset có thể chứa rationale hoặc chain-like solution steps. mô hình (model / 모델) có thể học mẫu (pattern / 패턴) giải từng bước, nhưng chất lượng (quality / 품질) phụ thuộc tính đúng đắn (correctness / 정확성) của traces.

Nếu traces chứa plausible nhưng incorrect lập luận (reasoning / 추론), mô hình (model / 모델) cũng bắt chước.

Không nên assume dài hơn = lập luận (reasoning / 추론) tốt hơn.

> **Chuyển mạch:** Ở chặng này của **Supervised Fine-Tuning (SFT)**, **Distillation bằng SFT** tiếp nhận điểm tựa từ **SFT và lập luận (reasoning / 추론) traces** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tool-use SFT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Distillation bằng SFT

Một teacher mô hình (model / 모델) mạnh có thể generate responses, sau đó student train bằng SFT. Đây là một dạng kiến thức (knowledge / 지식) distillation ở hành vi (behavior / 동작) mức (level / 수준).

Student học phân phối (distribution / 분포) đầu ra (output / 출력) của teacher, nhưng không nhất thiết bản sao (copy / 복사) nội bộ (internal / 내부) cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Supervised Fine-Tuning (SFT)**, **Tool-use SFT** tiếp nhận điểm tựa từ **Distillation bằng SFT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SFT và calibration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tool-use SFT

Để mô hình (model / 모델) gọi tools, dataset có thể chứa examples:

```text
user request
→ tool call JSON
→ tool result
→ final answer
```

SFT giúp mô hình (model / 모델) học cú pháp (syntax / 문법) và quyết định (decision / 결정) patterns. Nhưng môi trường vận hành (production / 운영 환경) vẫn cần lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증), permissions và thời gian chạy (runtime / 런타임) lỗi (error / 오류) handling.

> **Chuyển mạch:** Trong **Supervised Fine-Tuning (SFT)**, **SFT và calibration** tiếp nhận điểm tựa từ **Tool-use SFT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SFT và calibration

SFT có thể làm mô hình (model / 모델) answers trông tự tin hơn mà không cải thiện factual calibration tương ứng. Vì vậy preference về “confident helpful style” có thể tạo overconfidence.

Evaluation phải tách style và tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Ở chặng này của **Supervised Fine-Tuning (SFT)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **SFT và calibration** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> SFT là **hành vi (behavior / 동작) imitation trên top của pretrained năng lực (capability / 역량)**.

Nó không thay thế pretraining, retrieval hay thời gian chạy (runtime / 런타임) xác minh (verification / 확인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Supervised Fine-Tuning (SFT)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “SFT train mô hình (model / 모델) từ đầu cho tác vụ (task / 작업)”

Không. Với LLM, SFT thường là small post-training phase trên pretrained mô hình (model / 모델).

### “LoRA luôn cho kết quả giống full fine-tuning”

Không. Hiệu quả phụ thuộc rank, mục tiêu (target / 대상) modules, dữ liệu (data / 데이터) và mức thay đổi hành vi (behavior / 동작) cần thiết.

### “SFT dataset càng lớn càng tốt”

Bad/inconsistent examples có thể degrade hành vi (behavior / 동작). Curated chất lượng (quality / 품질) và coverage quan trọng hơn raw count.

> **Chuyển mạch:** Trong **Supervised Fine-Tuning (SFT)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

SFT là cầu giữa [Instruction Tuning](./06_instruction_tuning.md) và preference tối ưu hóa (optimization / 최적화). Khi multiple acceptable answers tồn tại, imitation một mục tiêu (target / 대상) không đủ để encode preference thứ tự (ordering / 순서). Đó là lý do RLHF/DPO xuất hiện.

Xem tiếp: [RLHF](./08_rlhf.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
