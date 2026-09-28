# Limitations của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)

> **Mạch đọc:** Đặt **Limitations của Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **kiến thức (knowledge / 지식) không có provenance bản địa (native / 네이티브)** sang **kiến thức (knowledge / 지식) có cutoff và staleness**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


LLM rất mạnh vì học broad statistical regularities từ lượng dữ liệu (data / 데이터) và compute lớn, nhưng kiến trúc (architecture / 아키텍처)/mục tiêu (objective / 목표) của chúng tạo ra limitations mang tính cấu trúc. Hiểu limitations giúp chọn đúng kiến trúc (architecture / 아키텍처) hệ thống (system / 시스템) thay vì cố “prompt harder” mọi vấn đề.

## Kiến thức (knowledge / 지식) không có provenance bản địa (native / 네이티브)

Weights không lưu nguồn (source / 소스) citation theo dạng cơ sở dữ liệu (database / 데이터베이스). mô hình (model / 모델) có thể generate fact nhưng không tự biết chính xác (exact / 정확한) document nào hỗ trợ (support / 지원) fact đó.

Nếu provenance là yêu cầu (requirement / 요구사항), cần retrieval/nguồn (source / 소스) tracking.

## Kiến thức (knowledge / 지식) có cutoff và staleness

Pretraining xảy ra tại một thời điểm. Facts sau cutoff hoặc trạng thái (state / 상태) động (dynamic / 동적) không nằm trong weights trừ khi continued huấn luyện (training / 학습)/cập nhật (update / 업데이트).

Hiện tại (current / 현재) dữ liệu (data / 데이터) nên đến từ tools/APIs/RAG.

## Hallucination

Autoregressive mục tiêu (objective / 목표) yêu cầu tiếp tục chuỗi (sequence / 시퀀스), không guarantee truth. mô hình (model / 모델) có thể tạo confident falsehood.

Xem: [Hallucination and Grounding](./13_hallucination_and_grounding.md).

## Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) hữu hạn

Mô hình (model / 모델) chỉ điều kiện (condition / 조건) trên tokens trong hiện tại (current / 현재) ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우). Long conversations cần truncation, summarization hoặc bộ nhớ (memory / 메모리) retrieval.

Ngay cả khi đơn vị từ (token / 토큰) technically fits, **effective use** của thông tin (information / 정보) ở đầu/giữa ngữ cảnh (context / 맥락) có thể không đồng đều.

## Lập luận (reasoning / 추론) không guaranteed

LLM có thể solve many lập luận (reasoning / 추론) tasks nhưng vẫn thất bại (fail / 실패) logically simple variants, especially adversarial or distribution-shifted prompts.

Bên ngoài (external / 외부) xác minh (verification / 확인) nên dùng khi exactness important.

## Chính xác (exact / 정확한) computation yếu hơn algorithmic tools

Large-number arithmetic, exhaustive tìm kiếm (search / 검색), cơ sở dữ liệu (database / 데이터베이스) aggregation và formal proof thường phù hợp với specialized tools hơn đơn vị từ (token / 토큰) generation.

Hệ thống (system / 시스템) tốt dispatch thao tác (operation / 연산) tới right computational substrate.

## Calibration hạn chế

Ngôn ngữ (language / 언어) confidence không phải xác suất (probability / 확률) of tính đúng đắn (correctness / 정확성). Phrases như “chắc chắn” có thể chỉ là learned style.

Risk-sensitive decisions cần calibrated scores hoặc bên ngoài (external / 외부) checks.

## Prompt sensitivity

Small wording differences có thể alter đầu ra (output / 출력). Post-training reduces but does not eliminate sensitivity.

Môi trường vận hành (production / 운영 환경) prompts cần regression tests.

## Susceptibility to prompt injection

Mô hình (model / 모델) naturally follows patterns/instructions in ngữ cảnh (context / 맥락). Khi untrusted documents nằm cùng ngữ cảnh (context / 맥락) với privileged instructions, attacker có thể attempt steer mô hình (model / 모델).

Bảo mật (security / 보안) requires privilege boundaries outside mô hình (model / 모델).

## Non-determinism

Sampling làm outputs vary. Even deterministic decoding can thay đổi (change / 변경) across mô hình (model / 모델)/provider versions, kernels or hệ thống (system / 시스템) updates.

If ứng dụng (application / 애플리케이션) requires strict repeatability, isolate deterministic components and bản ghi (record / 레코드) mô hình (model / 모델)/cấu hình (config / 설정)/phiên bản (version / 버전).

## Độ lệch (bias / 편향) từ dữ liệu (data / 데이터)

Huấn luyện (training / 학습) corpus reflects xã hội (social / 사회적), linguistic và geographic imbalance. mô hình (model / 모델) can underperform on low-resource languages/domains or reproduce stereotypes.

Evaluation must include mục tiêu (target / 대상) population, not only average benchmark.

## Long-tail failures

Mô hình (model / 모델) may perform 99% on dùng chung (common / 공통) cases but thất bại (fail / 실패) rare edge cases unpredictably. For large-scale triển khai (deployment / 배포), 1% can be many incidents.

Guardrails/fallback human rà soát (review / 검토) should mục tiêu (target / 대상) high-cost tail failures.

## Phân phối (distribution / 분포) shift

Người dùng (user / 사용자) hành vi (behavior / 동작) changes, new jargon appears, malicious strategies evolve. Static offline eval decays over thời gian (time / 시간).

Monitoring and continual evaluation are necessary.

## Công cụ (tool / 도구) errors compound

Agentic LLM can lời gọi (call / 호출) tools, but wrong công cụ (tool / 도구) argument may thay đổi (change / 변경) bên ngoài (external / 외부) trạng thái (state / 상태). mô hình (model / 모델) ngôn ngữ (language / 언어) năng lực (capability / 역량) does not guarantee giao dịch (transaction / 트랜잭션) an toàn (safety / 안전).

Use permissions, idempotency, kiểm tra hợp lệ (validation / 검증), confirmation and kiểm tra (audit / 감사) logs.

## Bộ nhớ (memory / 메모리) is not human-like

Conversation bộ nhớ (memory / 메모리) usually comes from tường minh (explicit / 명시적) ngữ cảnh (context / 맥락), retrieval or ứng dụng (application / 애플리케이션) cơ sở dữ liệu (database / 데이터베이스). LLM does not automatically maintain persistent episodic bộ nhớ (memory / 메모리) across sessions unless hệ thống (system / 시스템) provides it.

## Interpretability is incomplete

Attention weights or generated rationales do not provide full explanation of nội bộ (internal / 내부) computation. Mechanistic interpretability can reveal circuits/patterns but does not yet make large mô hình (model / 모델) decisions fully transparent.

## Training-data bất định (uncertainty / 불확실성)

For many các mô hình (models / 모델들), chính xác (exact / 정확한) corpus composition may be partially unknown. This complicates copyright, contamination and provenance phân tích (analysis / 분석).

## Ngôn ngữ (language / 언어) understanding vs world tương tác (interaction / 상호작용)

Text-only mô hình (model / 모델) learns world patterns through văn bản (text / 텍스트). vật lý (physical / 물리적) grounding, sensing and real-time hành động (action / 동작) require multimodal/robotic/công cụ (tool / 도구) interfaces.

Ngôn ngữ (language / 언어) competence should not be confused with direct embodied experience.

## Tối ưu hóa (optimization / 최적화) mục tiêu (target / 대상) mismatch

Pretraining optimizes đơn vị từ (token / 토큰) prediction; post-training optimizes preference/chính sách (policy / 정책) signals. người dùng (user / 사용자)'s true mục tiêu (objective / 목표) may differ.

This is Goodhart-like bài toán (problem / 문제): proxy chỉ số (metric / 지표) can be optimized while real goal suffers.

## Mô hình (model / 모델) vs hệ thống (system / 시스템) limitation

Nhiều “LLM limitations” có thể mitigated ở hệ thống (system / 시스템) mức (level / 수준):

```text
stale knowledge → RAG/API
arithmetic      → calculator
factuality      → grounding/verifier
long workflow   → agent state + tools
format          → constrained decoding/schema
security        → permissions/sandbox
```

Nhưng mitigation adds độ phức tạp (complexity / 복잡도) and new thất bại (failure / 실패) modes.

## When LLM is the wrong công cụ (tool / 도구)

Nếu bài toán (problem / 문제) có chính xác (exact / 정확한) deterministic rules, low ambiguity và high xác minh (verification / 확인) yêu cầu (requirement / 요구사항), normal software may be better.

Examples:

```text
interest calculation
permission check
schema validation
unique ID generation
cryptographic verification
```

LLM có thể explain/giao diện (interface / 인터페이스) quanh quy tắc (rule / 규칙) engine nhưng không nên replace deterministic cốt lõi (core / 핵심).

## Mô hình tư duy (mental model / 사고 모델)

> LLM là **probabilistic language-and-representation engine**, không phải cơ sở dữ liệu (database / 데이터베이스), calculator, theorem prover, chính sách (policy / 정책) engine hay operating hệ thống (system / 시스템). môi trường vận hành (production / 운영 환경) AI mạnh bằng cách kết hợp LLM với đúng components khác.

## Dùng chung (common / 공통) Misconceptions

### “mô hình (model / 모델) thế hệ sau sẽ làm mọi limitation biến mất”

Some limitations improve, but truth guarantees, provenance, authorization và deterministic thực thi (execution / 실행) remain hệ thống (system / 시스템) concerns.

### “Nếu prompt đủ tốt thì không cần kiến trúc (architecture / 아키텍처) khác”

Prompt không thay bên ngoài (external / 외부) kiến thức (knowledge / 지식), tools hoặc kiểm tra hợp lệ (validation / 검증).

### “LLM thất bại (failure / 실패) nghĩa AI không hữu ích”

Không. Giá trị đến từ matching năng lực (capability / 역량) với tác vụ (task / 작업) và kỹ thuật (engineering / 엔지니어링) around thất bại (failure / 실패) modes.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Limitations dẫn trực tiếp tới các tầng (layer / 계층) tiếp theo: [Retrieval & RAG](../09_retrieval_and_rag/00_information_retrieval_foundations.md), Agents, Evaluation, an toàn (safety / 안전) và AI kỹ thuật (engineering / 엔지니어링).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from language models to llms](./00_from_language_models_to_llms.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
