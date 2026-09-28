# Red Teaming và Adversarial Evaluation

> **Mạch đọc:** Đặt **Red Teaming và Adversarial Evaluation** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Threat mô hình (model / 모델) trước Attack danh sách (list / 목록)** sang **Attack Surfaces**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Red teaming (레드팀 평가)** là quá trình chủ động tìm cách làm AI hệ thống (system / 시스템) thất bại, vi phạm chính sách (policy / 정책) hoặc hành xử nguy hiểm trước khi attacker/người dùng (user / 사용자)/môi trường (environment / 환경) vô tình tìm ra. Khác robustness testing thông thường, red teaming thường giả định đầu vào (input / 입력) hoặc chiến lược (strategy / 전략) có tính đối kháng và thích nghi với hệ thống (system / 시스템).

## Threat mô hình (model / 모델) trước Attack danh sách (list / 목록)

Không bắt đầu bằng danh sách prompt tricks. Xác định:

```text
asset cần bảo vệ là gì?
attacker có capability gì?
attacker biết gì về system?
entry points nào?
impact nào đáng lo?
```

Threat mô hình (model / 모델) cho RAG assistant khác autonomous payment tác nhân (agent / 에이전트).

## Attack Surfaces

AI ứng dụng (application / 애플리케이션) có nhiều surfaces:

- người dùng (user / 사용자) prompt;
- uploaded files;
- retrieved documents;
- tools/APIs;
- bộ nhớ (memory / 메모리);
- mô hình (model / 모델) endpoint;
- dữ liệu huấn luyện (training data / 학습 데이터);
- logs/caches;
- orchestration trạng thái (state / 상태).

Chỉ red-team prompt tầng (layer / 계층) là chưa đủ.

## Prompt Injection

Malicious instruction cố override intended hành vi (behavior / 동작).

Direct injection đến từ người dùng (user / 사용자). Indirect injection có thể nằm trong webpage/document/công cụ (tool / 도구) kết quả (result / 결과) mà hệ thống (system / 시스템) retrieve.

Important principle:

> Untrusted content phải được coi là dữ liệu (data / 데이터), không phải authority.

Hệ thống (system / 시스템) prompt không phải ranh giới bảo mật (security boundary / 보안 경계).

## Dữ liệu (data / 데이터) Exfiltration Tests

Try to extract:

- secrets;
- hidden prompts;
- other tenant dữ liệu (data / 데이터);
- retrieved unauthorized documents;
- công cụ (tool / 도구) credentials.

Strong defense dựa auth/permissions/dữ liệu (data / 데이터) isolation, không dựa mô hình (model / 모델) “biết không nên nói”.

## Công cụ (tool / 도구) Abuse

Tác nhân (agent / 에이전트) có tools tạo side tác động (effect / 효과) cần kiểm thử (test / 테스트):

- unauthorized hành động (action / 동작);
- parameter manipulation;
- duplicate hành động (action / 동작);
- confused-deputy attack;
- injected công cụ (tool / 도구) kết quả (result / 결과);
- privilege escalation.

Authorization phải enforced outside mô hình (model / 모델).

## Jailbreak Evaluation

Jailbreaks thử vượt an toàn (safety / 안전) hành vi (behavior / 동작) qua roleplay, encoding, instruction xung đột (conflict / 충돌) hoặc multi-turn setup.

Red nhóm (team / 팀) nên measure thất bại (failure / 실패) categories/impact, không chỉ collect clever prompts.

## Adversarial Examples

Vision/classification có optimized perturbations. Threat mô hình (model / 모델) cần specify norm/vật lý (physical / 물리적) realism/truy vấn (query / 쿼리) truy cập (access / 접근).

Robustness against white-box độ dốc (gradient / 기울기) attack khác black-box real-world attack.

## RAG Poisoning

Attacker chèn malicious document vào corpus hoặc manipulate ranking.

Tests:

```text
poisoned document ranks high?
model follows hidden instruction?
citation makes attack look legitimate?
metadata filters bypassed?
```

## Bộ nhớ (memory / 메모리) Poisoning

Tác nhân (agent / 에이전트) persistent bộ nhớ (memory / 메모리) có thể store malicious false instruction/trạng thái (state / 상태), causing future sessions thất bại (fail / 실패).

Need ghi (write / 쓰기) kiểm tra hợp lệ (validation / 검증), provenance, phạm vi (scope / 범위) và deletion.

## Multi-Turn Attacks

Single-turn an toàn (safety / 안전) tests miss gradual ngữ cảnh (context / 맥락) manipulation. Stateful agents need multi-turn adversarial scenarios.

## Tài nguyên (resource / 자원) Exhaustion

Bảo mật (security / 보안) includes availability:

- huge prompts/files;
- recursive tác nhân (agent / 에이전트) loops;
- expensive công cụ (tool / 도구) calls;
- adversarial inputs maximizing đầu ra (output / 출력) length.

Enforce quotas, budgets, kích thước (size / 크기) limits, cancellation.

## Mô hình (model / 모델) Extraction / Abuse

Công khai (public / 공개) endpoint có thể be queried for imitation or exploit. tỷ lệ (rate / 비율) limits, abuse detection và terms may reduce rủi ro (risk / 위험), though complete prevention difficult.

## Automated Red Teaming

Attacker các mô hình (models / 모델들)/generators can create variants at quy mô (scale / 규모). Useful for breadth but can overfit to generator style.

Human red teams bring creativity/lĩnh vực (domain / 도메인) ngữ cảnh (context / 맥락). Best approach combines automation + human expertise.

## Adaptive Evaluation

Once hệ thống (system / 시스템) patched, attackers adapt. Red teaming is recurring vòng đời (lifecycle / 생명주기), not one pre-launch exercise.

## Scoring

Nhánh học (track / 트랙) more than attack success tỷ lệ (rate / 비율):

```text
severity
reproducibility
required attacker capability
time/cost to exploit
blast radius
detectability
```

A rare catastrophic exploit can matter more than dùng chung (common / 공통) harmless chính sách (policy / 정책) deviation.

## Defense-in-Depth kiểm tra hợp lệ (validation / 검증)

Kiểm thử (test / 테스트) layers independently:

```text
model refuses?
permission layer blocks?
schema validator rejects?
rate limit triggers?
audit alert fires?
```

If mô hình (model / 모델) defense fails but authorization still prevents harm, blast radius bounded.

## Red nhóm (team / 팀) to Regression

Confirmed vulnerability should become:

- regression kiểm thử (test / 테스트);
- monitoring tín hiệu (signal / 신호);
- kiến trúc (architecture / 아키텍처) fix where possible;
- sự cố (incident / 인시던트)/runbook kiến thức (knowledge / 지식).

Do not depend solely on prompt patch that attacker can rephrase around.

## Safe Evaluation môi trường (environment / 환경)

High-impact tools/actions should be red-teamed in sandbox/simulation or with harmless kiểm thử (test / 테스트) credentials.

Do not perform destructive real-world actions just to kiểm thử (test / 테스트) tác nhân (agent / 에이전트).

## Mô hình tư duy (mental model / 사고 모델)

```text
Red teaming = adversarial search over the whole AI system, guided by a threat model and impact.
```

## Dùng chung (common / 공통) Misconceptions

### “Prompt injection là mô hình (model / 모델) bài toán (problem / 문제)”

Nó là hệ thống (system / 시스템) bảo mật (security / 보안) bài toán (problem / 문제); mô hình (model / 모델) robustness helps but permission ranh giới (boundary / 경계) is essential.

### “Pass jailbreak benchmark nghĩa secure”

Attackers adapt and other surfaces remain.

### “Red nhóm (team / 팀) xong trước launch là đủ”

Các mô hình (models / 모델들), prompts, tools và attackers thay đổi (change / 변경) continuously.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Robustness](./03_robustness_and_distribution_shift.md), [AI Testing](./05_ai_testing_and_behavioral_evaluation.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md) và [AI Safety/Security](../19_ai_safety_security_alignment/README.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 evaluation foundations](./00_evaluation_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
