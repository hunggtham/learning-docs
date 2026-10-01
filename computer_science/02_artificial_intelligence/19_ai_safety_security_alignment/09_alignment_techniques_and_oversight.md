# Kỹ thuật căn chỉnh và cơ chế giám sát

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Kỹ thuật căn chỉnh và cơ chế giám sát**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiến thức cần có trước** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Vì sao pretraining chưa đủ** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Không có một thuật toán duy nhất giải quyết toàn bộ bài toán căn chỉnh. Hệ thống môi trường vận hành (production / 운영 환경) thường kết hợp **hậu huấn luyện (post-training)**, dữ liệu preference, chính sách (policy / 정책)/quy tắc (rule / 규칙), verifier, phân quyền, human approval và đánh giá liên tục. Mục tiêu của chapter này là đặt các kỹ thuật đó vào một kiến trúc chung, để phân biệt rõ thứ gì định hình hành vi mô hình và thứ gì thực sự kiểm soát authority của hệ thống.

## Kiến thức cần có trước

Nên đọc [Căn chỉnh AI và đặc tả mục tiêu](./01_alignment_and_objective_specification.md), [Reward Misspecification](./02_reward_misspecification_and_goal_misgeneralization.md), [SFT](../08_large_language_models/07_supervised_fine_tuning.md), [RLHF](../08_large_language_models/08_rlhf.md), [DPO](../08_large_language_models/09_preference_optimization_and_dpo.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

> **Chuyển mạch:** Trong **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Vì sao pretraining chưa đủ** tiếp nhận điểm tựa từ **Kiến thức cần có trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Supervised Fine-Tuning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao pretraining chưa đủ

Mô hình ngôn ngữ tiền huấn luyện tối ưu xác suất đơn vị từ (token / 토큰) tiếp theo:

\[
\min_\theta\; -\sum_t \log P_\theta(x_t\mid x_{<t})
\]

Mục tiêu (objective / 목표) này giúp mô hình học cấu trúc ngôn ngữ và nhiều mẫu (pattern / 패턴) về thế giới, nhưng không trực tiếp yêu cầu nó:

```text
làm đúng instruction
ưu tiên nguồn đáng tin
thừa nhận bất định
tránh hành động nguy hiểm
xuất JSON hợp lệ
dùng tool đúng quyền
```

Post-training biến khả năng nền thành hành vi trợ lý hoặc hành vi tác vụ cụ thể.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Supervised Fine-Tuning** tiếp nhận điểm tựa từ **Vì sao pretraining chưa đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu preference** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Supervised Fine-Tuning

**Tinh chỉnh có giám sát (Supervised Fine-Tuning — SFT)** học từ cặp instruction–phản hồi (response / 응답) mẫu:

\[
L_{SFT}=-\sum_t\log P_\theta(y_t\mid x,y_{<t})
\]

SFT hiệu quả khi có demonstration rõ và nhất quán. Nó dạy trực tiếp mẫu (pattern / 패턴) như:

```text
câu hỏi → câu trả lời phù hợp
input có cấu trúc → output đúng schema
case mơ hồ → hỏi lại
```

Nhưng SFT bị giới hạn bởi coverage và chất lượng demonstration. Những hành vi (behavior / 동작) không xuất hiện hoặc xuất hiện sai trong dữ liệu (data / 데이터) khó được học đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Supervised Fine-Tuning** nêu điều cần giải thích; **Dữ liệu preference** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **RLHF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu preference

Khi có nhiều đầu ra (output / 출력) hợp lệ, người đánh giá có thể chọn:

```text
A tốt hơn B
```

Từ đó hệ thống học preference tương đối thay vì một đáp án duy nhất. Tuy nhiên preference dữ liệu (data / 데이터) phản ánh rubric, annotator population và phân phối (distribution / 분포) của prompt được thu thập.

Các độ lệch (bias / 편향) thường gặp:

- thích câu dài hơn dù không chính xác hơn;
- ưu tiên phong cách lịch sự hơn nội dung;
- thiên lệch văn hóa/ngôn ngữ;
- chấm theo độ tự tin thay vì bằng chứng.

> **Chuyển mạch:** Trong **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Dữ liệu preference** nêu điều cần giải thích; **RLHF** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **DPO và tối ưu preference trực tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RLHF

Chuỗi xử lý (pipeline / 파이프라인) khái niệm phổ biến:

```text
SFT model
→ thu thập cặp preference
→ huấn luyện reward model
→ tối ưu policy theo reward
→ kiểm soát độ lệch khỏi reference model
```

Một mục tiêu (objective / 목표) đơn giản hóa có thể gồm reward và penalty KL:

\[
J(\pi)=\mathbb{E}[r(x,y)]-\beta D_{KL}(\pi\|\pi_{ref})
\]

`β` kiểm soát mức chính sách (policy / 정책) được phép đi xa khỏi tham chiếu (reference / 참조). Nếu tối ưu hóa (optimization / 최적화) quá mạnh trong khi reward mô hình (model / 모델) không hoàn hảo, reward có thể tăng nhưng chất lượng thật giảm.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật căn chỉnh và cơ chế giám sát**, sau nội dung của **RLHF**, **DPO và tối ưu preference trực tiếp** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Best-of-N và rejection sampling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DPO và tối ưu preference trực tiếp

Các phương pháp kiểu **Direct Preference tối ưu hóa (optimization / 최적화) (DPO)** dùng cặp chosen/rejected để tối ưu chính sách (policy / 정책) trực tiếp, tránh một số độ phức tạp (complexity / 복잡도) của online RL. Operationally, DPO có thể đơn giản hơn nhưng không làm biến mất các vấn đề về chất lượng preference dữ liệu (data / 데이터), phân phối (distribution / 분포) shift hay specification.

Vì vậy “không có reward mô hình (model / 모델) riêng” không đồng nghĩa “không còn proxy mục tiêu (objective / 목표)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Best-of-N và rejection sampling** tiếp nhận điểm tựa từ **DPO và tối ưu preference trực tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Critique và revision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Best-of-N và rejection sampling

Một cách cải thiện suy luận (inference / 추론) mà không cập nhật weights:

```text
sinh N candidate
→ chấm bằng verifier / reward model
→ chọn candidate tốt nhất
```

Xác suất tìm được đầu ra (output / 출력) tốt có thể tăng khi `N` tăng, nhưng chi phí suy luận (inference / 추론) cũng tăng gần tương ứng. Nếu verifier có blind spot, tìm kiếm (search / 검색) pressure sẽ khai thác chính blind spot đó.

> **Chuyển mạch:** Trong **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Critique và revision** tiếp nhận điểm tựa từ **Best-of-N và rejection sampling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rule-based và constitutional-style guidance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Critique và revision

Mẫu (pattern / 패턴) phổ biến:

```text
sinh bản nháp
→ critique theo rubric
→ sửa lại
```

Self-critique có thể giúp khi lỗi dễ nhận diện sau khi đã có candidate. Tuy nhiên cùng một mô hình có thể không phát hiện được lỗi do chính nó tạo ra. Verifier độc lập, công cụ xác định hoặc human rà soát (review / 검토) cung cấp tín hiệu độc lập hơn.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Rule-based và constitutional-style guidance** tiếp nhận điểm tựa từ **Critique và revision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết quả (outcome / 결과) supervision và tiến trình (process / 프로세스) supervision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rule-based và constitutional-style guidance

Có thể biểu diễn principle cấp cao rồi yêu cầu mô hình (model / 모델) tự critique/revise theo principle đó. Cách này giúp quy mô (scale / 규모) phản hồi (feedback / 피드백) và làm chính sách (policy / 정책) dễ đọc hơn.

Nhưng principle bằng ngôn ngữ tự nhiên vẫn được mô hình (model / 모델) diễn giải. Nó không thay thế:

```text
authorization
schema validation
rate limit
financial limit
network policy
sandbox
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Rule-based và constitutional-style guidance** xác định đầu vào; **Kết quả (outcome / 결과) supervision và tiến trình (process / 프로세스) supervision** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Verifier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kết quả (outcome / 결과) supervision và tiến trình (process / 프로세스) supervision

**Giám sát kết quả (outcome supervision)** đánh giá đầu ra (output / 출력) cuối. **Giám sát quá trình (process supervision)** đánh giá các bước trung gian hoặc hành động.

Với tác nhân (agent / 에이전트), process-level check đặc biệt quan trọng vì một trajectory có thể chứa bước nguy hiểm dù final answer trông đúng.

Nên ưu tiên trạng thái và hành động có thể quan sát:

```text
tool call
state transition
permission result
external side effect
verifier outcome
```

thay vì giả định rằng textual chain-of-thought phản ánh chính xác cơ chế bên trong.

> **Chuyển mạch:** Trong **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Kết quả (outcome / 결과) supervision và tiến trình (process / 프로세스) supervision** xác định đầu vào; **Verifier** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Scalable oversight** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Verifier

Verifier mạnh khi tính đúng đắn (correctness / 정확성) có cấu trúc kiểm tra được:

- đơn vị (unit / 단위) kiểm thử (test / 테스트);
- kiểu (type / 타입) checker;
- theorem prover;
- calculator;
- citation hỗ trợ (support / 지원);
- lược đồ (schema / 스키마) validator;
- nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙);
- chính sách (policy / 정책) engine.

Mẫu (pattern / 패턴) môi trường vận hành (production / 운영 환경):

```text
mô hình đề xuất
→ verifier kiểm tra
→ policy/authorization xác nhận
→ executor thực thi
→ outcome được kiểm lại
```

Verifier không nhất thiết là AI. Nhiều verifier tốt nhất là deterministic.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Verifier** cho ta quy tắc; **Scalable oversight** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Human-in-the-Loop không tự động tạo an toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scalable oversight

Khi số lượng đầu ra (output / 출력) vượt khả năng rà soát (review / 검토) thủ công, oversight phải được phân tầng:

```text
automated validator cho tất cả request
→ sample audit
→ model-based judge cho case trung bình
→ human escalation cho case rủi ro cao
```

Thiết kế này cần đo cả false negative lẫn false positive của từng tầng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Scalable oversight** cho ta quy tắc; **Human-in-the-Loop không tự động tạo an toàn** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Confidence-based escalation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human-in-the-Loop không tự động tạo an toàn

Human rà soát (review / 검토) có thể thất bại vì:

- alert quá nhiều;
- reviewer thiếu ngữ cảnh (context / 맥락);
- automation độ lệch (bias / 편향);
- deadline quá ngắn;
- UI chỉ hiển thị summary do mô hình (model / 모델) tạo;
- người duyệt không có quyền thật để chặn hành động (action / 동작).

Một approval tốt nên hiển thị structured hành động (action / 동작) và dữ liệu nguồn quan trọng, sau đó backend re-authorize trước khi thực thi.

> **Chuyển mạch:** Trong **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Confidence-based escalation** tiếp nhận điểm tựa từ **Human-in-the-Loop không tự động tạo an toàn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Over-refusal và harmful compliance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Confidence-based escalation

Có thể tuyến (route / 경로) trường hợp (case / 사례) khó sang mô hình (model / 모델) mạnh hơn hoặc con người dựa trên bất định (uncertainty / 불확실성)/rủi ro (risk / 위험) tín hiệu (signal / 신호). Tuy nhiên xác suất đơn vị từ (token / 토큰) thô của LLM không phải thước đo confidence đáng tin cho mọi tác vụ (task / 작업).

Escalation tín hiệu (signal / 신호) có thể kết hợp:

- verifier thất bại (failure / 실패);
- retrieval chất lượng (quality / 품질);
- chính sách (policy / 정책) rủi ro (risk / 위험);
- mô hình (model / 모델) disagreement;
- calibrated classifier;
- domain-specific bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Over-refusal và harmful compliance** tiếp nhận điểm tựa từ **Confidence-based escalation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân phối (distribution / 분포) shift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Over-refusal và harmful compliance

Alignment evaluation phải đo đồng thời hai phía:

```text
harmful compliance thấp
và
over-refusal thấp
```

Nếu chỉ tối ưu refusal tỷ lệ (rate / 비율), hệ thống có thể trở nên vô dụng. Nếu chỉ tối ưu helpfulness, nó có thể thực hiện yêu cầu (request / 요청) không phù hợp.

Đây là bài toán precision–recall dưới chính sách (policy / 정책) phân phối (distribution / 분포), không phải chỉ “càng từ chối nhiều càng an toàn”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Phân phối (distribution / 분포) shift** tiếp nhận điểm tựa từ **Over-refusal và harmful compliance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Căn chỉnh mô hình và căn chỉnh hệ thống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) shift

Hành vi (behavior / 동작) được học từ preference dữ liệu (data / 데이터) có thể suy giảm khi gặp:

- ngôn ngữ mới;
- lĩnh vực (domain / 도메인) mới;
- prompt dài hoặc lạ;
- adversarial wording;
- công cụ (tool / 도구) mới;
- workflow dài hạn.

Vì vậy alignment cần regression suite và red-team set theo môi trường vận hành (production / 운영 환경) phân phối (distribution / 분포) thật.

> **Chuyển mạch:** Trong **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Căn chỉnh mô hình và căn chỉnh hệ thống** tiếp nhận điểm tựa từ **Phân phối (distribution / 분포) shift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Oversight cho tác nhân (agent / 에이전트) dài hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Căn chỉnh mô hình và căn chỉnh hệ thống

Cần phân biệt rõ:

```text
model alignment
→ định hình output và preference của mô hình

system alignment
→ giới hạn quyền, trạng thái, workflow, verifier và human approval
```

Mô hình (model / 모델) alignment cải thiện xác suất hành vi đúng. hệ thống (system / 시스템) alignment quyết định mức hậu quả tối đa nếu mô hình vẫn sai.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Oversight cho tác nhân (agent / 에이전트) dài hạn** tiếp nhận điểm tựa từ **Căn chỉnh mô hình và căn chỉnh hệ thống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Oversight cho tác nhân (agent / 에이전트) dài hạn

Một tác nhân (agent / 에이전트) có quyền hành động nên có checkpoint rõ:

```text
mục tiêu
→ kế hoạch
→ validation
→ tool call
→ authorization
→ side-effect approval
→ execution
→ outcome verification
→ state update
```

Không nên chỉ dựa vào câu cuối “tôi đã hoàn thành nhiệm vụ”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **Oversight cho tác nhân (agent / 에이전트) dài hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation và bản phát hành (release / 릴리스) gate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình triển khai môi trường vận hành (production / 운영 환경)

Một ngăn xếp (stack / 스택) căn chỉnh thực dụng có thể gồm:

```text
base model
→ SFT / preference tuning
→ system/developer policy
→ retrieval grounding
→ tool scope hẹp
→ validator / verifier
→ human approval theo risk
→ monitoring / red-team feedback
→ release gate
```

Mỗi tầng (layer / 계층) giải một loại thất bại (failure / 실패) khác nhau; không có tầng (layer / 계층) nào thay thế hoàn toàn các tầng (layer / 계층) còn lại.

> **Chuyển mạch:** Trong **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Evaluation và bản phát hành (release / 릴리스) gate** tiếp nhận điểm tựa từ **Mô hình triển khai môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation và bản phát hành (release / 릴리스) gate

Bộ đánh giá nên bao gồm:

- helpfulness;
- factuality;
- instruction hierarchy;
- harmful compliance;
- over-refusal;
- jailbreak resistance;
- multilingual/lĩnh vực (domain / 도메인) slice;
- công cụ (tool / 도구) misuse;
- long-horizon tác nhân (agent / 에이전트) scenario;
- chi phí (cost / 비용)/độ trễ (latency / 지연 시간) regression;
- ranh giới bảo mật (security boundary / 보안 경계) regression.

Một thay đổi alignment không nên được promote chỉ vì một tổng điểm duy nhất tăng.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Evaluation và bản phát hành (release / 릴리스) gate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프)

Các kỹ thuật alignment có thể làm tăng độ trễ (latency / 지연 시간), chi phí, refusal, độ phức tạp (complexity / 복잡도) và operational burden. Verifier nhiều tầng làm hệ thống chậm hơn nhưng tăng khả năng phát hiện lỗi. Human approval giảm autonomy nhưng phù hợp cho hành động (action / 동작) có impact lớn.

Sự đánh đổi (trade-off / 트레이드오프) phải gắn với rủi ro (risk / 위험) lớp (class / 클래스), không áp một cấu hình cho mọi tác vụ (task / 작업).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Dạng thất bại (failure mode / 실패 모드) thường gặp** tiếp nhận điểm tựa từ **Sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) thường gặp

**Reward overoptimization.** Reward mô hình (model / 모델) tăng nhưng human chất lượng (quality / 품질) giảm.

**Preference độ lệch (bias / 편향).** Dataset preference ưu tiên style hơn tính đúng đắn (correctness / 정확성).

**Over-refusal.** chính sách (policy / 정책) quá rộng chặn nhiều yêu cầu (request / 요청) hợp lệ.

**Verifier đồng sai.** mô hình (model / 모델) và judge cùng chia sẻ blind spot.

**Human rubber-stamp.** Người duyệt không đủ ngữ cảnh (context / 맥락) hoặc thời gian.

**mô hình (model / 모델) alignment bị nhầm với kiểm soát truy cập (access control / 접근 제어).** mô hình (model / 모델) vẫn có công cụ (tool / 도구) permission quá rộng.

**Regression ngoài phân phối (distribution / 분포).** Alignment tốt ở tiếng Anh nhưng kém ở ngôn ngữ/lĩnh vực (domain / 도메인) khác.

> **Chuyển mạch:** Trong **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Mô hình tư duy** gom các mảnh từ **Dạng thất bại (failure mode / 실패 모드) thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Alignment techniques định hình hành vi; oversight kiểm tra hành vi; bảo mật (security / 보안) kiến trúc (architecture / 아키텍처) kiểm soát quyền và hậu quả.**

Ba lớp này liên quan nhưng không thể thay thế lẫn nhau.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “RLHF căn chỉnh mô hình với toàn bộ giá trị con người”

Không. RLHF tối ưu theo preference dữ liệu (data / 데이터) và reward mô hình (model / 모델) trong một phân phối (distribution / 분포) hữu hạn.

### “Constitutional quy tắc (rule / 규칙) là hard ràng buộc (constraint / 제약조건)”

Không nếu quy tắc (rule / 규칙) chỉ được mô hình (model / 모델) diễn giải bằng ngôn ngữ tự nhiên.

### “Có human approval là chắc chắn an toàn”

Không. Chất lượng approval phụ thuộc tải công việc (workload / 워크로드), UI, ngữ cảnh (context / 맥락) và authority của reviewer.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật căn chỉnh và cơ chế giám sát**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Căn chỉnh AI](./01_alignment_and_objective_specification.md), [Reward Misspecification](./02_reward_misspecification_and_goal_misgeneralization.md), [SFT](../08_large_language_models/07_supervised_fine_tuning.md), [RLHF](../08_large_language_models/08_rlhf.md), [DPO](../08_large_language_models/09_preference_optimization_and_dpo.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [Prompt Injection](./03_prompt_injection_and_jailbreaks.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
