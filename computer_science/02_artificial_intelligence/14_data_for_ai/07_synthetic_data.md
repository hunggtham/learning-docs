# Synthetic dữ liệu (data / 데이터)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Synthetic dữ liệu (data / 데이터)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Các nguồn synthetic dữ liệu (data / 데이터)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Simulation** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Synthetic dữ liệu (data / 데이터)** là dữ liệu (data / 데이터) được tạo bởi simulator, rules hoặc generative mô hình (model / 모델) thay vì thu trực tiếp từ phenomenon thật. Nó hữu ích để tăng coverage, bảo vệ privacy, tạo rare scenarios hoặc bootstrap labels, nhưng không phải “dữ liệu (data / 데이터) miễn phí” vì synthetic dữ liệu (data / 데이터) luôn kế thừa các giả định (assumptions / 가정들) của generator.

## Các nguồn synthetic dữ liệu (data / 데이터)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
rule-based generation
simulation / digital twin
generative models
LLM-generated text
rendered images
procedural environments
counterfactual transformations
```

Mỗi nguồn (source / 소스) có fidelity và thất bại (failure / 실패) modes khác.

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, **Các nguồn synthetic dữ liệu (data / 데이터)** nêu điều cần giải thích; **Simulation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Lĩnh vực (domain / 도메인) Randomization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Simulation

Robotics/autonomous driving có thể generate unlimited trajectories/images trong simulator.

Ưu điểm:

- labels chính xác (exact / 정확한) từ simulator trạng thái (state / 상태);
- rare/dangerous cases cheap;
- full điều khiển (control / 제어) conditions.

Nhược điểm: **sim-to-real gap**. Renderer/physics/sensor mô hình (model / 모델) không perfect.

> **Chuyển mạch:** Ở chặng này của **Synthetic dữ liệu (data / 데이터)**, **Lĩnh vực (domain / 도메인) Randomization** tiếp nhận điểm tựa từ **Simulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Generative Synthetic dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lĩnh vực (domain / 도메인) Randomization

Randomize textures, lighting, camera, physics parameters để force mô hình (model / 모델) learn bất biến (invariant / 불변식) cấu trúc (structure / 구조) rather than overfit one simulator look.

Goal không phải make simulation photorealistic nhất, mà cover real lĩnh vực (domain / 도메인) sufficiently.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Synthetic dữ liệu (data / 데이터)**, **Lĩnh vực (domain / 도메인) Randomization** nêu điều cần giải thích; **Generative Synthetic dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Self-Instruct / Synthetic Instructions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Generative Synthetic dữ liệu (data / 데이터)

Diffusion/LLM can produce new examples. Use cases:

- augment rare classes;
- generate instruction-response pairs;
- create paraphrases;
- simulate edge cases;
- anonymized-like samples.

But generated dữ liệu (data / 데이터) reflects generator huấn luyện (training / 학습) phân phối (distribution / 분포).

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, **Generative Synthetic dữ liệu (data / 데이터)** nêu điều cần giải thích; **Self-Instruct / Synthetic Instructions** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Teacher–Student Distillation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Self-Instruct / Synthetic Instructions

LLM can generate tasks then answers, scaling instruction-tuning dữ liệu (data / 데이터).

Chuỗi xử lý (pipeline / 파이프라인):

```text
seed tasks
→ generate candidate instructions
→ filter/deduplicate
→ generate responses
→ quality judge/human sample audit
```

Rủi ro (risk / 위험): errors compound and mô hình (model / 모델) family may teach its own blind spots.

> **Chuyển mạch:** Ở chặng này của **Synthetic dữ liệu (data / 데이터)**, **Teacher–Student Distillation** tiếp nhận điểm tựa từ **Self-Instruct / Synthetic Instructions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rare sự kiện (event / 이벤트) Generation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Teacher–Student Distillation

Strong mô hình (model / 모델) labels/generates dữ liệu huấn luyện (training data / 학습 데이터) for smaller mô hình (model / 모델). Student approximates teacher hành vi (behavior / 동작), not necessarily ground truth.

Chất lượng (quality / 품질) ceiling tied to teacher + filtering.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Synthetic dữ liệu (data / 데이터)**, **Rare sự kiện (event / 이벤트) Generation** tiếp nhận điểm tựa từ **Teacher–Student Distillation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Privacy Motivation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rare sự kiện (event / 이벤트) Generation

Fraud/thất bại (failure / 실패) cases rare. Synthetic generation can balance huấn luyện (training / 학습), but if synthetic rare cases unrealistic mô hình (model / 모델) learns artifacts separating “synthetic” from “real” rather than true phenomenon.

Need realism evaluation and mixed real dữ liệu (data / 데이터).

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, **Privacy Motivation** tiếp nhận điểm tựa từ **Rare sự kiện (event / 이벤트) Generation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differential Privacy liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Privacy Motivation

Synthetic records may reduce direct exposure of real individuals, but privacy is not automatic.

Generator can memorize and reproduce huấn luyện (training / 학습) records. Privacy needs attacks/tests or formal mechanisms like Differential Privacy.

> **Chuyển mạch:** Ở chặng này của **Synthetic dữ liệu (data / 데이터)**, sau nội dung của **Privacy Motivation**, **Differential Privacy liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Statistical Fidelity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential Privacy liên kết (connection / 연결)

DP huấn luyện (training / 학습) limits influence of any one huấn luyện (training / 학습) bản ghi (record / 레코드). Synthetic dữ liệu (data / 데이터) generated from DP-trained mô hình (model / 모델) can inherit formal privacy guarantees under các giả định (assumptions / 가정들), unlike ordinary synthetic dữ liệu (data / 데이터).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Synthetic dữ liệu (data / 데이터)**, **Statistical Fidelity** tiếp nhận điểm tựa từ **Differential Privacy liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Utility Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Statistical Fidelity

For tabular synthetic dữ liệu (data / 데이터), compare:

- marginals;
- correlations;
- conditional distributions;
- rare category frequency;
- temporal patterns;
- downstream mô hình (model / 모델) utility.

Matching simple histograms does not guarantee joint fidelity.

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, **Utility Evaluation** tiếp nhận điểm tựa từ **Statistical Fidelity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Diversity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Utility Evaluation

Train on synthetic, kiểm thử (test / 테스트) on **real holdout**. This TSTR (Train Synthetic Test Real) style evaluation measures whether synthetic captures task-relevant cấu trúc (structure / 구조).

Also compare mô hình (model / 모델) trained real vs real+synthetic.

> **Chuyển mạch:** Ở chặng này của **Synthetic dữ liệu (data / 데이터)**, **Diversity** tiếp nhận điểm tựa từ **Utility Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Synthetic-to-Real Ratio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Diversity

Generator chế độ (mode / 모드) collapse/low diversity produces many near-duplicates. Count alone overstates effective cỡ mẫu (sample size / 표본 크기).

Deduplication and diversity metrics needed.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Synthetic dữ liệu (data / 데이터)**, **Synthetic-to-Real Ratio** tiếp nhận điểm tựa từ **Diversity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân phối (distribution / 분포) Steering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Synthetic-to-Real Ratio

Too much synthetic dữ liệu (data / 데이터) can shift mô hình (model / 모델) toward generator artifacts. Optimal ratio task-dependent; monitor real kiểm tra hợp lệ (validation / 검증) hiệu năng (performance / 성능).

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, **Phân phối (distribution / 분포) Steering** tiếp nhận điểm tựa từ **Synthetic-to-Real Ratio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Counterfactual dữ liệu (data / 데이터) Augmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) Steering

Synthetic generator can intentionally rebalance subgroup/category coverage. But forcing uniform phân phối (distribution / 분포) may no longer match triển khai (deployment / 배포) prior. Separate huấn luyện (training / 학습) balancing from xác suất (probability / 확률) calibration.

> **Chuyển mạch:** Ở chặng này của **Synthetic dữ liệu (data / 데이터)**, **Phân phối (distribution / 분포) Steering** nêu điều cần giải thích; **Counterfactual dữ liệu (data / 데이터) Augmentation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Adversarial Synthetic dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Counterfactual dữ liệu (data / 데이터) Augmentation

Modify one attribute while preserving label ngữ nghĩa (semantics / 의미론):

```text
he ↔ she
background color change
style transfer
```

Useful to break shortcuts, but generated counterfactual must remain plausible and not unintentionally alter mục tiêu (target / 대상).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Synthetic dữ liệu (data / 데이터)**, **Counterfactual dữ liệu (data / 데이터) Augmentation** nêu điều cần giải thích; **Adversarial Synthetic dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Synthetic Evaluation Sets** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adversarial Synthetic dữ liệu (data / 데이터)

Generate hard negatives or red-team prompts near mô hình (model / 모델) quyết định (decision / 결정) ranh giới (boundary / 경계). This can strengthen robustness, but generator may overfocus known thất bại (failure / 실패) modes.

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, **Adversarial Synthetic dữ liệu (data / 데이터)** nêu điều cần giải thích; **Synthetic Evaluation Sets** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dữ liệu (data / 데이터) Contamination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Synthetic Evaluation Sets

Generated benchmarks quy mô (scale / 규모) scenario creation, but using LLM to both generate and judge can create circularity. Keep human/real anchors.

> **Chuyển mạch:** Ở chặng này của **Synthetic dữ liệu (data / 데이터)**, **Synthetic Evaluation Sets** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Contamination** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình (model / 모델) Collapse Intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Contamination

As web fills with AI-generated content, future foundation-model huấn luyện (training / 학습) may ingest synthetic dữ liệu (data / 데이터) unknowingly. Repeated model-generated distributions can narrow diversity or amplify errors.

Provenance becomes increasingly important.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Synthetic dữ liệu (data / 데이터)**, **Dữ liệu (data / 데이터) Contamination** nêu điều cần giải thích; **Mô hình (model / 모델) Collapse Intuition** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Watermark / siêu dữ liệu (metadata / 메타데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) Collapse Intuition

If generations replace real dữ liệu (data / 데이터) over repeated generations without fresh real tín hiệu (signal / 신호), phân phối (distribution / 분포) tails may erode. chính xác (exact / 정확한) hành vi (behavior / 동작) depends setup, but principle: synthetic vòng phản hồi (feedback loop / 피드백 루프) can lose thông tin (information / 정보).

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, **Mô hình (model / 모델) Collapse Intuition** nêu điều cần giải thích; **Watermark / siêu dữ liệu (metadata / 메타데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Simulation Labels vs Real Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Watermark / siêu dữ liệu (metadata / 메타데이터)

Synthetic media can carry provenance siêu dữ liệu (metadata / 메타데이터)/watermarks. siêu dữ liệu (metadata / 메타데이터) can be stripped; watermark robust detection is probabilistic, not perfect.

> **Chuyển mạch:** Ở chặng này của **Synthetic dữ liệu (data / 데이터)**, **Watermark / siêu dữ liệu (metadata / 메타데이터)** cho ta quy tắc; **Simulation Labels vs Real Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Example: Document OCR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Simulation Labels vs Real Labels

Simulator gives chính xác (exact / 정확한) trạng thái nội bộ (internal state / 내부 상태), but ánh xạ (mapping / 매핑) to real sensor ngữ nghĩa (semantics / 의미론) may differ. Perfect simulated ground truth does not mean perfect real-world relevance.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Synthetic dữ liệu (data / 데이터)**, **Simulation Labels vs Real Labels** cho ta quy tắc; **Example: Document OCR** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Example: mã (code / 코드) dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example: Document OCR

Synthetic văn bản (text / 텍스트) rendered with many fonts/backgrounds gives chính xác (exact / 정확한) transcription/bounding boxes. Useful pretraining. But real scans add fold, glare, handwriting, compression; real fine-tuning still needed.

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, **Example: Document OCR** cho ta quy tắc; **Example: mã (code / 코드) dữ liệu (data / 데이터)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example: mã (code / 코드) dữ liệu (data / 데이터)

LLM-generated mã (code / 코드) can create exercises/solutions/tests. But trình biên dịch (compiler / 컴파일러)/kiểm thử (test / 테스트) thực thi (execution / 실행) should verify, because syntactically plausible mã (code / 코드) may be wrong/insecure.

> **Chuyển mạch:** Ở chặng này của **Synthetic dữ liệu (data / 데이터)**, các dấu vết trong **Example: mã (code / 코드) dữ liệu (data / 데이터)** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Synthetic dữ liệu (data / 데이터) là đầu ra (output / 출력) của một mô hình (model / 모델) về world. huấn luyện (training / 학습) trên synthetic nghĩa là học từ các giả định (assumptions / 가정들) của world-model đó; giá trị đến từ controllability, không phải vì synthetic inherently truthful.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Synthetic dữ liệu (data / 데이터)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Synthetic dữ liệu (data / 데이터) solves privacy”

Not automatically; memorization/re-identification possible.

### “More synthetic samples always increase diversity”

Generator may đầu ra (output / 출력) near-duplicates/chế độ (mode / 모드) độ lệch (bias / 편향).

### “If synthetic looks realistic to human, it is statistically correct”

Visual plausibility does not guarantee task-relevant joint phân phối (distribution / 분포).

> **Chuyển mạch:** Trong **Synthetic dữ liệu (data / 데이터)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Synthetic dữ liệu (data / 데이터) connects Generative AI, Simulation, Privacy, RL environments and dữ liệu (data / 데이터) quản trị (governance / 거버넌스).

Xem tiếp: [Data Governance](./08_data_governance.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
