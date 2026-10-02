# Robustness và phân phối (distribution / 분포) Shift

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Robustness và distribution shift**. Route đi từ clean-set performance → perturbations/shift types → subgroup and temporal slices → stress tests → mitigation and monitoring, để độ bền được đo ngoài dữ liệu thuận lợi.

**Robustness (강건성 / tính bền vững)** hỏi hệ thống (system / 시스템) còn hoạt động tốt khi đầu vào (input / 입력), môi trường (environment / 환경) hoặc các giả định (assumptions / 가정들) thay đổi trong phạm vi nào. Một mô hình (model / 모델) đạt benchmark cao trên clean dữ liệu (data / 데이터) nhưng sụp khi có typo, sensor noise, unseen ngôn ngữ (language / 언어) hoặc phân phối (distribution / 분포) shift chưa phải robust hệ thống (system / 시스템).

## Clean hiệu năng (performance / 성능) không đủ

Huấn luyện (training / 학습)/kiểm thử (test / 테스트) thường giả định examples từ phân phối (distribution / 분포) tương tự. môi trường vận hành (production / 운영 환경) world tạo perturbations:

- thiết bị (device / 장치)/sensor thay đổi (change / 변경);
- typo/spelling;
- background noise;
- lighting/weather;
- new người dùng (user / 사용자) hành vi (behavior / 동작);
- malicious inputs;
- missing fields;
- downstream API changes.

Robustness evaluation cố đo hiệu năng (performance / 성능) dưới những variations này.

> **Chuyển mạch:** Trong **Robustness và phân phối (distribution / 분포) Shift**, **Phân phối (distribution / 분포) Shift** tiếp nhận điểm tựa từ **Clean hiệu năng (performance / 성능) không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Corruption Robustness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) Shift

Nếu môi trường vận hành (production / 운영 환경) phân phối (distribution / 분포) khác huấn luyện (training / 학습):

\[
P_{prod}(X,Y) \neq P_{train}(X,Y)
\]

Mô hình (model / 모델) generalization các giả định (assumptions / 가정들) bị thử thách.

Shift types include covariate, label/prior và concept shift. Taxonomy useful nhưng diagnosis thực tế cần look at dữ liệu (data / 데이터) + outcomes.

> **Chuyển mạch:** Ở chặng này của **Robustness và phân phối (distribution / 분포) Shift**, **Corruption Robustness** tiếp nhận điểm tựa từ **Phân phối (distribution / 분포) Shift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Perturbation Invariance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Corruption Robustness

Computer Vision có thể kiểm thử (test / 테스트) blur, noise, compression, brightness. NLP kiểm thử (test / 테스트) typo, paraphrase, code-switching. Audio kiểm thử (test / 테스트) background noise, microphone variation.

Goal không phải score trên mọi corruption imaginable mà map degradation curve theo severity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Robustness và phân phối (distribution / 분포) Shift**, **Perturbation Invariance** tiếp nhận điểm tựa từ **Corruption Robustness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adversarial Examples** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Perturbation Invariance

Nếu small meaning-preserving perturbation đổi đầu ra (output / 출력) lớn, mô hình (model / 모델) unstable.

Examples:

```text
paraphrase same question
format whitespace change
image slight crop
reordering irrelevant metadata
```

Metamorphic tests define relationships expected giữa original và transformed inputs.

> **Chuyển mạch:** Trong **Robustness và phân phối (distribution / 분포) Shift**, **Perturbation Invariance** cho ta quy tắc; **Adversarial Examples** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Spurious Correlations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adversarial Examples

Adversarial đầu vào (input / 입력) được optimize để gây lỗi (error / 오류). Small perturbation có thể exploit cục bộ (local / 로컬) quyết định (decision / 결정) ranh giới (boundary / 경계).

Threat mô hình (model / 모델) phải specify attacker năng lực (capability / 역량). Robustness against random noise khác robustness against adaptive attacker.

> **Chuyển mạch:** Ở chặng này của **Robustness và phân phối (distribution / 분포) Shift**, **Adversarial Examples** cho ta quy tắc; **Spurious Correlations** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **OOD Generalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spurious Correlations

Mô hình (model / 모델) có thể dựa shortcut tính năng (feature / 기능) correlated trong huấn luyện (training / 학습) nhưng không nhân quả (causal / 인과적)/reliable.

Ví dụ ảnh (image / 이미지) classifier học background thay vì đối tượng (object / 객체).

Kiểm thử sức chịu tải (stress test / 스트레스 테스트) thay đổi (change / 변경) background/ngữ cảnh (context / 맥락) để reveal shortcut.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Robustness và phân phối (distribution / 분포) Shift**, **OOD Generalization** tiếp nhận điểm tựa từ **Spurious Correlations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Robustness vs Invariance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OOD Generalization

OOD kiểm thử (test / 테스트) should be intentionally separated by lĩnh vực (domain / 도메인)/thời gian (time / 시간)/nguồn (source / 소스). Random split thường underestimate challenge.

Examples:

- train hospitals A/B, kiểm thử (test / 테스트) hospital C;
- train past months, kiểm thử (test / 테스트) future;
- train English, kiểm thử (test / 테스트) code-switch;
- train known sản phẩm (product / 제품) categories, kiểm thử (test / 테스트) new category.

> **Chuyển mạch:** Trong **Robustness và phân phối (distribution / 분포) Shift**, **Robustness vs Invariance** tiếp nhận điểm tựa từ **OOD Generalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Augmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Robustness vs Invariance

Không phải mọi changes nên ignored. Nếu tính năng (feature / 기능) thay đổi (change / 변경) thực sự alters mục tiêu (target / 대상), forcing invariance harmful.

Lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) quyết định which transformations preserve label.

> **Chuyển mạch:** Ở chặng này của **Robustness và phân phối (distribution / 분포) Shift**, **Robustness vs Invariance** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Augmentation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Regularization và Robustness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Augmentation

Augmentation injects expected variations during huấn luyện (training / 학습):

```text
image crop/flip/color
text noise/paraphrase
audio noise/time shift
```

Augmentation defines inductive độ lệch (bias / 편향) about invariance. Wrong augmentation can distort ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Robustness và phân phối (distribution / 분포) Shift**, **Dữ liệu (data / 데이터) Augmentation** nêu điều cần giải thích; **Regularization và Robustness** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Robustness Curves** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Regularization và Robustness

Regularization may improve average generalization but does not guarantee adversarial or OOD robustness.

Need direct stress testing.

> **Chuyển mạch:** Trong **Robustness và phân phối (distribution / 분포) Shift**, **Robustness Curves** tiếp nhận điểm tựa từ **Regularization và Robustness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM Robustness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Robustness Curves

Instead of single score, measure chỉ số (metric / 지표) vs perturbation severity:

```text
noise level 0 → accuracy 95%
noise level 1 → 93%
noise level 2 → 88%
noise level 3 → 60%
```

Curve shows degradation onset.

> **Chuyển mạch:** Ở chặng này của **Robustness và phân phối (distribution / 분포) Shift**, **LLM Robustness** tiếp nhận điểm tựa từ **Robustness Curves** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) Robustness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM Robustness

Kiểm thử (test / 테스트):

- prompt paraphrases;
- irrelevant ngữ cảnh (context / 맥락);
- conflicting instructions;
- long ngữ cảnh (context / 맥락);
- multilingual inputs;
- format variation;
- retrieval noise;
- misleading premises.

LLM hành vi (behavior / 동작) can be highly sensitive to prompt wording/thứ tự (order / 순서).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Robustness và phân phối (distribution / 분포) Shift**, **Ngữ cảnh (context / 맥락) Robustness** tiếp nhận điểm tựa từ **LLM Robustness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tác nhân (agent / 에이전트) Robustness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) Robustness

Longer ngữ cảnh (context / 맥락) can introduce distractors. A robust QA hệ thống (system / 시스템) should focus relevant bằng chứng (evidence / 증거) and ignore irrelevant chunks.

Need kiểm thử (test / 테스트) retrieval with mix relevant/irrelevant/contradictory sources.

> **Chuyển mạch:** Trong **Robustness và phân phối (distribution / 분포) Shift**, **Tác nhân (agent / 에이전트) Robustness** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) Robustness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Robustness vs độ tin cậy (reliability / 신뢰성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tác nhân (agent / 에이전트) Robustness

Tác nhân (agent / 에이전트) operates in changing môi trường (environment / 환경):

- công cụ (tool / 도구) hết thời gian chờ (timeout / 타임아웃);
- stale trạng thái (state / 상태);
- partial thất bại (failure / 실패);
- unexpected lược đồ (schema / 스키마);
- human interruption;
- duplicate thử lại (retry / 재시도).

Robust thiết kế (design / 설계) requires khôi phục (recovery / 복구), replanning, idempotency and bounded loops.

> **Chuyển mạch:** Ở chặng này của **Robustness và phân phối (distribution / 분포) Shift**, **Robustness vs độ tin cậy (reliability / 신뢰성)** tiếp nhận điểm tựa từ **Tác nhân (agent / 에이전트) Robustness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Distributionally Robust tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Robustness vs độ tin cậy (reliability / 신뢰성)

Robustness concerns hành vi (behavior / 동작) under variation/perturbation. độ tin cậy (reliability / 신뢰성) broader: availability, khôi phục (recovery / 복구), operational consistency and verified outcomes.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Robustness và phân phối (distribution / 분포) Shift**, **Distributionally Robust tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **Robustness vs độ tin cậy (reliability / 신뢰성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lĩnh vực (domain / 도메인) Generalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Distributionally Robust tối ưu hóa (optimization / 최적화)

Some methods optimize worst-case or neighborhood distributions rather than empirical average. Conceptually:

\[
\min_\theta \max_{Q\in\mathcal U(P)} E_Q[L_\theta]
\]

Useful intuition but bất định (uncertainty / 불확실성) set choice crucial.

> **Chuyển mạch:** Trong **Robustness và phân phối (distribution / 분포) Shift**, **Lĩnh vực (domain / 도메인) Generalization** tiếp nhận điểm tựa từ **Distributionally Robust tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhân quả (causal / 인과적) Perspective** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lĩnh vực (domain / 도메인) Generalization

Train across multiple domains to learn features stable across environments. Success depends diversity and cấu trúc (structure / 구조); no guarantee for arbitrary unseen lĩnh vực (domain / 도메인).

> **Chuyển mạch:** Ở chặng này của **Robustness và phân phối (distribution / 분포) Shift**, **Nhân quả (causal / 인과적) Perspective** tiếp nhận điểm tựa từ **Lĩnh vực (domain / 도메인) Generalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Robustness ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhân quả (causal / 인과적) Perspective

Nhân quả (causal / 인과적) features may transfer better across interventions than spurious correlations, but học tập (learning / 학습) nhân quả (causal / 인과적) cấu trúc (structure / 구조) itself is hard. Causality is not automatic fix.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Robustness và phân phối (distribution / 분포) Shift**, **Robustness ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **Nhân quả (causal / 인과적) Perspective** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Robustness ngân sách (budget / 예산)

Môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) can tầng (layer / 계층) defenses:

```text
input validation
OOD detection
model robustness
retrieval verification
fallback
human escalation
```

Do not demand mô hình (model / 모델) alone handle all bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Trong **Robustness và phân phối (distribution / 분포) Shift**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Robustness ngân sách (budget / 예산)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Robustness = how gracefully behavior degrades when reality differs from the clean assumptions used to build the model.
```

> **Chuyển mạch:** Ở chặng này của **Robustness và phân phối (distribution / 분포) Shift**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “dữ liệu (data / 데이터) augmentation làm mô hình (model / 모델) robust”

Chỉ với variation augmentation actually represents; unknown/adaptive shifts remain.

### “OOD detector biết mọi unknown”

OOD is open-world bài toán (problem / 문제); detectors have blind spots.

### “Robustness score là một con số universal”

Robustness depends threat/shift mô hình (model / 모델) and severity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Robustness và phân phối (distribution / 분포) Shift**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Drift](../16_mlops_and_llmops/07_drift_and_retraining.md), [Uncertainty](./02_uncertainty_and_calibration.md), [Red Teaming](./06_red_teaming_and_adversarial_evaluation.md) và [Safety/Security](../19_ai_safety_security_alignment/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
