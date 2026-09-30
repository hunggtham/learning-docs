# Synthetic dữ liệu (data / 데이터)

> **Mạch đọc:** Đặt **Synthetic dữ liệu (data / 데이터)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Các nguồn synthetic dữ liệu (data / 데이터)** sang **Simulation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Simulation

Robotics/autonomous driving có thể generate unlimited trajectories/images trong simulator.

Ưu điểm:

- labels chính xác (exact / 정확한) từ simulator trạng thái (state / 상태);
- rare/dangerous cases cheap;
- full điều khiển (control / 제어) conditions.

Nhược điểm: **sim-to-real gap**. Renderer/physics/sensor mô hình (model / 모델) không perfect.

## Lĩnh vực (domain / 도메인) Randomization

Randomize textures, lighting, camera, physics parameters để force mô hình (model / 모델) learn bất biến (invariant / 불변식) cấu trúc (structure / 구조) rather than overfit one simulator look.

Goal không phải make simulation photorealistic nhất, mà cover real lĩnh vực (domain / 도메인) sufficiently.

## Generative Synthetic dữ liệu (data / 데이터)

Diffusion/LLM can produce new examples. Use cases:

- augment rare classes;
- generate instruction-response pairs;
- create paraphrases;
- simulate edge cases;
- anonymized-like samples.

But generated dữ liệu (data / 데이터) reflects generator huấn luyện (training / 학습) phân phối (distribution / 분포).

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

## Teacher–Student Distillation

Strong mô hình (model / 모델) labels/generates dữ liệu huấn luyện (training data / 학습 데이터) for smaller mô hình (model / 모델). Student approximates teacher hành vi (behavior / 동작), not necessarily ground truth.

Chất lượng (quality / 품질) ceiling tied to teacher + filtering.

## Rare sự kiện (event / 이벤트) Generation

Fraud/thất bại (failure / 실패) cases rare. Synthetic generation can balance huấn luyện (training / 학습), but if synthetic rare cases unrealistic mô hình (model / 모델) learns artifacts separating “synthetic” from “real” rather than true phenomenon.

Need realism evaluation and mixed real dữ liệu (data / 데이터).

## Privacy Motivation

Synthetic records may reduce direct exposure of real individuals, but privacy is not automatic.

Generator can memorize and reproduce huấn luyện (training / 학습) records. Privacy needs attacks/tests or formal mechanisms like Differential Privacy.

## Differential Privacy liên kết (connection / 연결)

DP huấn luyện (training / 학습) limits influence of any one huấn luyện (training / 학습) bản ghi (record / 레코드). Synthetic dữ liệu (data / 데이터) generated from DP-trained mô hình (model / 모델) can inherit formal privacy guarantees under các giả định (assumptions / 가정들), unlike ordinary synthetic dữ liệu (data / 데이터).

## Statistical Fidelity

For tabular synthetic dữ liệu (data / 데이터), compare:

- marginals;
- correlations;
- conditional distributions;
- rare category frequency;
- temporal patterns;
- downstream mô hình (model / 모델) utility.

Matching simple histograms does not guarantee joint fidelity.

## Utility Evaluation

Train on synthetic, kiểm thử (test / 테스트) on **real holdout**. This TSTR (Train Synthetic Test Real) style evaluation measures whether synthetic captures task-relevant cấu trúc (structure / 구조).

Also compare mô hình (model / 모델) trained real vs real+synthetic.

## Diversity

Generator chế độ (mode / 모드) collapse/low diversity produces many near-duplicates. Count alone overstates effective cỡ mẫu (sample size / 표본 크기).

Deduplication and diversity metrics needed.

## Synthetic-to-Real Ratio

Too much synthetic dữ liệu (data / 데이터) can shift mô hình (model / 모델) toward generator artifacts. Optimal ratio task-dependent; monitor real kiểm tra hợp lệ (validation / 검증) hiệu năng (performance / 성능).

## Phân phối (distribution / 분포) Steering

Synthetic generator can intentionally rebalance subgroup/category coverage. But forcing uniform phân phối (distribution / 분포) may no longer match triển khai (deployment / 배포) prior. Separate huấn luyện (training / 학습) balancing from xác suất (probability / 확률) calibration.

## Counterfactual dữ liệu (data / 데이터) Augmentation

Modify one attribute while preserving label ngữ nghĩa (semantics / 의미론):

```text
he ↔ she
background color change
style transfer
```

Useful to break shortcuts, but generated counterfactual must remain plausible and not unintentionally alter mục tiêu (target / 대상).

## Adversarial Synthetic dữ liệu (data / 데이터)

Generate hard negatives or red-team prompts near mô hình (model / 모델) quyết định (decision / 결정) ranh giới (boundary / 경계). This can strengthen robustness, but generator may overfocus known thất bại (failure / 실패) modes.

## Synthetic Evaluation Sets

Generated benchmarks quy mô (scale / 규모) scenario creation, but using LLM to both generate and judge can create circularity. Keep human/real anchors.

## Dữ liệu (data / 데이터) Contamination

As web fills with AI-generated content, future foundation-model huấn luyện (training / 학습) may ingest synthetic dữ liệu (data / 데이터) unknowingly. Repeated model-generated distributions can narrow diversity or amplify errors.

Provenance becomes increasingly important.

## Mô hình (model / 모델) Collapse Intuition

If generations replace real dữ liệu (data / 데이터) over repeated generations without fresh real tín hiệu (signal / 신호), phân phối (distribution / 분포) tails may erode. chính xác (exact / 정확한) hành vi (behavior / 동작) depends setup, but principle: synthetic vòng phản hồi (feedback loop / 피드백 루프) can lose thông tin (information / 정보).

## Watermark / siêu dữ liệu (metadata / 메타데이터)

Synthetic media can carry provenance siêu dữ liệu (metadata / 메타데이터)/watermarks. siêu dữ liệu (metadata / 메타데이터) can be stripped; watermark robust detection is probabilistic, not perfect.

## Simulation Labels vs Real Labels

Simulator gives chính xác (exact / 정확한) trạng thái nội bộ (internal state / 내부 상태), but ánh xạ (mapping / 매핑) to real sensor ngữ nghĩa (semantics / 의미론) may differ. Perfect simulated ground truth does not mean perfect real-world relevance.

## Example: Document OCR

Synthetic văn bản (text / 텍스트) rendered with many fonts/backgrounds gives chính xác (exact / 정확한) transcription/bounding boxes. Useful pretraining. But real scans add fold, glare, handwriting, compression; real fine-tuning still needed.

## Example: mã (code / 코드) dữ liệu (data / 데이터)

LLM-generated mã (code / 코드) can create exercises/solutions/tests. But trình biên dịch (compiler / 컴파일러)/kiểm thử (test / 테스트) thực thi (execution / 실행) should verify, because syntactically plausible mã (code / 코드) may be wrong/insecure.

## Mô hình tư duy (mental model / 사고 모델)

> **Synthetic dữ liệu (data / 데이터) là đầu ra (output / 출력) của một mô hình (model / 모델) về world. huấn luyện (training / 학습) trên synthetic nghĩa là học từ các giả định (assumptions / 가정들) của world-model đó; giá trị đến từ controllability, không phải vì synthetic inherently truthful.**

## Dùng chung (common / 공통) Misconceptions

### “Synthetic dữ liệu (data / 데이터) solves privacy”

Not automatically; memorization/re-identification possible.

### “More synthetic samples always increase diversity”

Generator may đầu ra (output / 출력) near-duplicates/chế độ (mode / 모드) độ lệch (bias / 편향).

### “If synthetic looks realistic to human, it is statistically correct”

Visual plausibility does not guarantee task-relevant joint phân phối (distribution / 분포).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Synthetic dữ liệu (data / 데이터) connects Generative AI, Simulation, Privacy, RL environments and dữ liệu (data / 데이터) quản trị (governance / 거버넌스).

Xem tiếp: [Data Governance](./08_data_governance.md).
