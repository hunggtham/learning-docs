# Dữ liệu (data / 데이터) Collection

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Data collection**. Route đi từ decision/use case → population and sampling frame → source types → collection protocol → coverage, consent, and drift, để dữ liệu thu được phù hợp với quyết định cần hỗ trợ.

**dữ liệu (data / 데이터) collection (데이터 수집 / thu thập dữ liệu)** là quá trình quyết định cái gì được quan sát, từ đâu, với tần suất nào, dưới permission nào và bằng instrumentation gì. Đây là nơi nhiều độ lệch (bias / 편향) bắt đầu trước khi mô hình (model / 모델) tồn tại.

## Collection Goal phải xuất phát từ quyết định (decision / 결정) Goal

Không thu dữ liệu (data / 데이터) chỉ vì “có thể”. Hãy bắt đầu:

```text
business / scientific decision
→ target outcome
→ prediction time
→ required signals
→ collection mechanism
```

Nếu mục tiêu (target / 대상) là fraud quyết định (decision / 결정) trong 200 ms, tính năng (feature / 기능) chỉ available sau 1 ngày không hữu ích online.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Collection**, **Collection Goal phải xuất phát từ quyết định (decision / 결정) Goal** nêu điều cần giải thích; **Nguồn (source / 소스) Types** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Instrumentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguồn (source / 소스) Types

Nguồn dữ liệu (data / 데이터) có thể:

- transactional databases;
- ứng dụng (application / 애플리케이션) logs;
- sensors;
- third-party APIs;
- user-generated content;
- surveys;
- web/công khai (public / 공개) corpora;
- human annotation;
- synthetic/simulation.

Mỗi nguồn (source / 소스) có độ tin cậy (reliability / 신뢰성) và legal/privacy các ràng buộc (constraints / 제약조건들) khác.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Collection**, **Nguồn (source / 소스) Types** nêu điều cần giải thích; **Instrumentation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Observation độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Instrumentation

Logging sự kiện (event / 이벤트) phải có ngữ nghĩa (semantics / 의미론) rõ:

```text
event_name
entity_id
event_time
properties
producer_version
```

Lược đồ (schema / 스키마) drift hoặc sự kiện (event / 이벤트) rename silently có thể phá tính năng (feature / 기능) chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Collection**, **Observation độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Instrumentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sampling chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Observation độ lệch (bias / 편향)

Bạn chỉ collect những gì hệ thống (system / 시스템) hiện tại expose. Recommendation logs không chứa reactions với items chưa từng show.

Đây là exposure độ lệch (bias / 편향).

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Collection**, **Sampling chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **Observation độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Temporal Coverage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sampling chiến lược (strategy / 전략)

Nếu collect mọi sự kiện (event / 이벤트) quá đắt, sampling cần preserve relevant phân phối (distribution / 분포).

Uniform sampling simple nhưng rare events biến mất. Stratified sampling giữ biểu diễn (representation / 표현) của subgroups/classes.

Sampling xác suất (probability / 확률) nên được recorded nếu later weighting needed.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Collection**, **Temporal Coverage** tiếp nhận điểm tựa từ **Sampling chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sensor Calibration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Temporal Coverage

Dữ liệu (data / 데이터) cần cover seasonality:

- weekday/weekend;
- holidays;
- campaigns;
- economic cycles;
- software phiên bản (version / 버전) changes.

Train trên một tuần bình thường có thể thất bại (fail / 실패) Black Friday.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Collection**, **Sensor Calibration** tiếp nhận điểm tựa từ **Temporal Coverage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Người dùng (user / 사용자) Consent và Purpose Limitation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sensor Calibration

Vật lý (physical / 물리적) sensor dữ liệu (data / 데이터) phụ thuộc calibration. Drift sensor tạo phân phối (distribution / 분포) shift mà mô hình (model / 모델) có thể interpret như real-world thay đổi (change / 변경).

Calibration siêu dữ liệu (metadata / 메타데이터) cần lineage.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Collection**, **Sensor Calibration** đã nêu tiêu chí phân biệt, còn **Người dùng (user / 사용자) Consent và Purpose Limitation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Dữ liệu (data / 데이터) Minimization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Người dùng (user / 사용자) Consent và Purpose Limitation

Dữ liệu (data / 데이터) collection phải phù hợp consent/legal basis và intended purpose. “Đã collect được” không tự động nghĩa được phép dùng để train mọi mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Collection**, **Người dùng (user / 사용자) Consent và Purpose Limitation** đã nêu tiêu chí phân biệt, còn **Dữ liệu (data / 데이터) Minimization** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Identifiers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Minimization

Collect minimum necessary sensitive dữ liệu (data / 데이터). Extra fields increase bảo mật (security / 보안)/compliance burden và shortcut rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Collection**, **Dữ liệu (data / 데이터) Minimization** nêu điều cần giải thích; **Identifiers** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Web dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Identifiers

Stable IDs giúp group/split/lineage nhưng cũng sensitive. Hashing không automatically anonymize nếu lĩnh vực (domain / 도메인) small hoặc linkage possible.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Collection**, **Identifiers** nêu điều cần giải thích; **Web dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Human-Generated phản hồi (feedback / 피드백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Web dữ liệu (data / 데이터)

Web crawling cần quan tâm:

- robots/policies;
- licensing/copyright;
- duplicate mirrors;
- ngôn ngữ (language / 언어) imbalance;
- spam/SEO content;
- personal dữ liệu (data / 데이터);
- temporal freshness.

Curation often harder than crawling itself.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Collection**, **Web dữ liệu (data / 데이터)** nêu điều cần giải thích; **Human-Generated phản hồi (feedback / 피드백)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Counterfactual Blindness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human-Generated phản hồi (feedback / 피드백)

Ratings/clicks are noisy proxies. Click can mean curiosity, not satisfaction. Absence of click can mean item never seen.

Need understand hành vi (behavior / 동작) cơ chế (mechanism / 메커니즘) before use as label.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Collection**, **Counterfactual Blindness** tiếp nhận điểm tựa từ **Human-Generated phản hồi (feedback / 피드백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Experimentation dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Counterfactual Blindness

Hệ thống (system / 시스템) logs chosen hành động (action / 동작) kết quả (outcome / 결과), not kết quả (outcome / 결과) of alternatives. Bandit/RL/nhân quả (causal / 인과적) methods may be needed to learn optimal quyết định (decision / 결정), not just prediction.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Collection**, **Counterfactual Blindness** nêu điều cần giải thích; **Experimentation dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dữ liệu (data / 데이터) Contracts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Experimentation dữ liệu (data / 데이터)

Randomized experiments produce stronger nhân quả (causal / 인과적) bằng chứng (evidence / 증거). Logging treatment assignment and eligibility is essential.

Do not train later without preserving experiment ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Collection**, **Experimentation dữ liệu (data / 데이터)** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Contracts** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Late-Arriving dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Contracts

Producer-consumer đặc tả hợp đồng (contract / 계약) should specify:

```text
schema
semantic definition
freshness SLA
nullability
units
ownership
breaking-change policy
```

Dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) is API between teams.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Collection**, **Dữ liệu (data / 데이터) Contracts** nêu điều cần giải thích; **Late-Arriving dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Offline vs Online tính năng (feature / 기능) Availability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Late-Arriving dữ liệu (data / 데이터)

Events may arrive delayed/out-of-order. Features based on sự kiện (event / 이벤트) thời gian (time / 시간) need watermarks/cửa sổ (window / 윈도우) chính sách (policy / 정책).

Ignoring late events can độ lệch (bias / 편향) historical aggregates.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Collection**, **Late-Arriving dữ liệu (data / 데이터)** cho ta quy tắc; **Offline vs Online tính năng (feature / 기능) Availability** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dữ liệu (data / 데이터) Retention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Offline vs Online tính năng (feature / 기능) Availability

A tính năng (feature / 기능) easily computed in warehouse may not be available at suy luận (inference / 추론) độ trễ (latency / 지연 시간). Collection kiến trúc (architecture / 아키텍처) should reflect serving requirements.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Collection**, **Offline vs Online tính năng (feature / 기능) Availability** cho ta quy tắc; **Dữ liệu (data / 데이터) Retention** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Chất lượng (quality / 품질) at nguồn (source / 소스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Retention

Keep raw dữ liệu (data / 데이터) forever is costly/risky. Define retention by purpose, legal yêu cầu (requirement / 요구사항) and reproducibility needs.

Sometimes store aggregate/derived sản phẩm tạo ra (artifact / 산출물) instead of raw sensitive nguồn (source / 소스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Collection**, **Dữ liệu (data / 데이터) Retention** nêu điều cần giải thích; **Chất lượng (quality / 품질) at nguồn (source / 소스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Monitoring Collection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chất lượng (quality / 품질) at nguồn (source / 소스)

Best cleaning is preventing bad dữ liệu (data / 데이터) generation. UI kiểm tra hợp lệ (validation / 검증), typed APIs, sensor checks and transactional các ràng buộc (constraints / 제약조건들) reduce downstream repair.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Collection**, **Chất lượng (quality / 품질) at nguồn (source / 소스)** nêu điều cần giải thích; **Monitoring Collection** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Example: eKYC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monitoring Collection

Nhánh học (track / 트랙):

- volume;
- missing tỷ lệ (rate / 비율);
- lược đồ (schema / 스키마) changes;
- độ trễ (latency / 지연 시간);
- duplicate tỷ lệ (rate / 비율);
- category phân phối (distribution / 분포);
- nguồn (source / 소스) outages.

Sudden 90% drop in sự kiện (event / 이벤트) volume should alert before next retraining.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Collection**, **Monitoring Collection** cho ta quy tắc; **Example: eKYC** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example: eKYC

For định danh (identity / 식별자) xác minh (verification / 확인), collection may include document images, selfie video, siêu dữ liệu (metadata / 메타데이터) and quyết định (decision / 결정) kết quả (outcome / 결과).

Important issues:

- camera/thiết bị (device / 장치) diversity;
- glare/blur;
- document-country coverage;
- fraud attack samples;
- PII/bảo mật (security / 보안);
- whether manual-review kết quả (outcome / 결과) is reliable label.

Môi trường vận hành (production / 운영 환경) coverage often matters more than adding another mô hình (model / 모델) tầng (layer / 계층).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Collection**, **Example: eKYC** cho ta quy tắc; **Mô hình tư duy (mental model / 사고 모델)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Collection defines the cửa sổ (window / 윈도우) through which mô hình (model / 모델) sees the world. A blind spot in instrumentation becomes a blind spot in học tập (learning / 학습).**

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Collection**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Collect everything now, decide later”

Creates privacy/chi phí (cost / 비용) and ambiguous ngữ nghĩa (semantics / 의미론); not a free option.

### “Logs are mục tiêu (objective / 목표) ground truth”

Logs reflect software hành vi (behavior / 동작) and người dùng (user / 사용자) exposure.

### “Third-party dữ liệu (data / 데이터) can be trusted as-is”

Need provenance, license, lược đồ (schema / 스키마) and chất lượng (quality / 품질) kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Collection**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Collection connects software instrumentation, databases, privacy and experimental thiết kế (design / 설계).

Xem tiếp: [Data Cleaning](./02_data_cleaning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
