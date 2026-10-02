# Dữ liệu (data / 데이터) Labeling

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Data labeling**. Route đi từ task definition → label ontology → annotation guidelines → agreement/adjudication → noisy-label monitoring, để “ground truth” được xây dựng và kiểm soát thay vì giả định là tuyệt đối.

**dữ liệu (data / 데이터) labeling (데이터 라벨링 / gán nhãn dữ liệu)** biến raw examples thành supervision tín hiệu (signal / 신호) mà mô hình (model / 모델) tối ưu. Label không tự nhiên rơi từ reality xuống dataset; nó được tạo bởi quy tắc (rule / 규칙), human judgment, downstream kết quả (outcome / 결과) hoặc mô hình (model / 모델) khác. Vì vậy label luôn có ngữ nghĩa (semantics / 의미론), bất định (uncertainty / 불확실성) và tiến trình (process / 프로세스) phía sau.

## Ground Truth không luôn tuyệt đối

Một số label gần deterministic:

```text
invoice total = exact numeric field
object class = known catalog ID
```

Nhưng nhiều labels subjective/latent:

```text
toxicity
sentiment
medical diagnosis
fraud intent
helpfulness
image quality
```

Trong các trường hợp (case / 사례) này, disagreement giữa annotators có thể phản ánh ambiguity thật, không chỉ annotator “sai”.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Ground Truth không luôn tuyệt đối** cho ta quy tắc; **Label Definition** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Kết quả (outcome / 결과) Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Label Definition

Trước annotation cần specification:

- label nghĩa là gì;
- positive/negative ranh giới (boundary / 경계);
- edge cases;
- unknown/abstain option;
- temporal cutoff;
- multi-label rules;
- examples/counterexamples.

Không có guideline rõ, mô hình (model / 모델) sẽ học inconsistency.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Label Definition** cho ta quy tắc; **Kết quả (outcome / 결과) Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Proxy Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kết quả (outcome / 결과) Labels

Labels có thể đến từ future sự kiện (event / 이벤트):

```text
customer churned within 30 days
transaction became chargeback
loan defaulted within 12 months
```

Need define observation cửa sổ (window / 윈도우) và label maturity. huấn luyện (training / 학습) too early creates false negatives vì kết quả (outcome / 결과) chưa có đủ thời gian (time / 시간) xuất hiện.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, **Kết quả (outcome / 결과) Labels** cho ta quy tắc; **Proxy Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Human Annotation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proxy Labels

Khi true goal khó measure, ta dùng proxy:

```text
click → interest
watch time → satisfaction
manual review result → fraud truth
```

Proxy mismatch là cốt lõi (core / 핵심) rủi ro (risk / 위험). mô hình (model / 모델) optimize proxy, không intended concept.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Proxy Labels** cho ta quy tắc; **Human Annotation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Inter-Annotator Agreement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human Annotation

Human labeling chuỗi xử lý (pipeline / 파이프라인) cần:

```text
instructions
training/calibration
annotation UI
quality checks
adjudication
feedback loop
```

Công cụ (tool / 도구) UX ảnh hưởng label chất lượng (quality / 품질). Nếu UI crop mất ngữ cảnh (context / 맥락), annotator không thể label đúng.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Inter-Annotator Agreement** tiếp nhận điểm tựa từ **Human Annotation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Majority Vote** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inter-Annotator Agreement

Agreement measures consistency. Simple percent agreement bị inflated khi one lớp (class / 클래스) dominant. Cohen’s kappa cho two annotators:

\[
\kappa=\frac{p_o-p_e}{1-p_e}
\]

trong đó `p_o` observed agreement, `p_e` expected by chance.

Low agreement có thể tín hiệu (signal / 신호) guideline unclear hoặc tác vụ (task / 작업) inherently subjective.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, **Majority Vote** tiếp nhận điểm tựa từ **Inter-Annotator Agreement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Soft Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Majority Vote

Multiple labels có thể aggregate bằng majority vote, nhưng điều này discards bất định (uncertainty / 불확실성) và assumes annotators equally reliable.

Alternative:

- weighted annotators;
- probabilistic label các mô hình (models / 모델들);
- adjudicator;
- soft mục tiêu (target / 대상) phân phối (distribution / 분포).

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Majority Vote** cho ta quy tắc; **Soft Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Expert vs Crowd Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Soft Labels

Nếu 7/10 annotators chọn A, 3/10 chọn B, mục tiêu (target / 대상) phân phối (distribution / 분포):

\[
y=[0.7,0.3]
\]

có thể preserve ambiguity tốt hơn hard majority `[1,0]`.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Soft Labels** cho ta quy tắc; **Expert vs Crowd Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Annotation độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Expert vs Crowd Labels

Lĩnh vực (domain / 도메인) tasks như radiology/legal rà soát (review / 검토) cần expert kiến thức (knowledge / 지식). Crowd labels cheaper nhưng may lack lĩnh vực (domain / 도메인) competence.

Hybrid chuỗi xử lý (pipeline / 파이프라인) có thể crowd easy cases, expert adjudicate difficult cases.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, **Expert vs Crowd Labels** cho ta quy tắc; **Annotation độ lệch (bias / 편향)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Blind Annotation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Annotation độ lệch (bias / 편향)

Annotators bring cultural/contextual priors. Guideline designer cũng encode values. Diverse annotator pool + subgroup phân tích (analysis / 분석) helps expose disagreements.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Blind Annotation** tiếp nhận điểm tựa từ **Annotation độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Active học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Blind Annotation

Nếu annotator biết mô hình (model / 모델) prediction, anchoring độ lệch (bias / 편향) có thể xảy ra. Human rà soát (review / 검토) UI nên cân nhắc hide mô hình (model / 모델) đầu ra (output / 출력) khi collecting independent ground truth.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Active học tập (learning / 학습)** tiếp nhận điểm tựa từ **Blind Annotation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weak Supervision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Active học tập (learning / 학습)

Mô hình (model / 모델) chọn examples uncertain/high-value để label. This reduces chi phí (cost / 비용) but mẫu (sample / 표본) becomes model-dependent.

Need include exploration/random kiểm tra (audit / 감사) samples để không miss systematic blind spots.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, **Weak Supervision** tiếp nhận điểm tựa từ **Active học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pseudo-Labeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weak Supervision

Labels generated by heuristics/rules/kiến thức (knowledge / 지식) bases:

```text
keyword rule
regex
existing classifier
business rule
```

Multiple noisy labeling functions có thể combine probabilistically.

Weak supervision scales but inherits quy tắc (rule / 규칙) độ lệch (bias / 편향).

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Weak Supervision** cho ta quy tắc; **Pseudo-Labeling** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **LLM-Generated Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pseudo-Labeling

Train mô hình (model / 모델) on labeled dữ liệu (data / 데이터), predict unlabeled dữ liệu (data / 데이터), use confident predictions as pseudo-labels.

Rủi ro (risk / 위험): self-reinforcing mistakes. Thresholding, teacher các mô hình (models / 모델들) và consistency methods reduce but not eliminate.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Pseudo-Labeling** cho ta quy tắc; **LLM-Generated Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Label Leakage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM-Generated Labels

LLMs can label văn bản (text / 텍스트)/ảnh (image / 이미지) at quy mô (scale / 규모). Need treat as noisy annotator:

- benchmark against human gold set;
- inspect subgroup độ lệch (bias / 편향);
- bản ghi (record / 레코드) mô hình (model / 모델)/phiên bản (version / 버전)/prompt;
- avoid circular evaluation where same mô hình (model / 모델) family generates and judges labels.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, **LLM-Generated Labels** cho ta quy tắc; **Label Leakage** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Label Noise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Label Leakage

Annotation tiến trình (process / 프로세스) may use thông tin (information / 정보) unavailable at suy luận (inference / 추론). Example fraud analyst sees final chargeback status while labeling suspiciousness at giao dịch (transaction / 트랜잭션) thời gian (time / 시간).

Need ask: **labeler được phép biết gì tương ứng prediction thời gian (time / 시간)?**

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Label Leakage** cho ta quy tắc; **Label Noise** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Positive-Unlabeled học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Label Noise

Symmetric random noise and class-dependent noise affect algorithms differently. Deep networks can eventually memorize noisy labels.

Early stopping, robust losses, mẫu (sample / 표본) reweighting and relabeling may help, but fixing nguồn (source / 소스) tiến trình (process / 프로세스) preferable.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Label Noise** cho ta quy tắc; **Positive-Unlabeled học tập (learning / 학습)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Multi-Label Annotation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Positive-Unlabeled học tập (learning / 학습)

Sometimes positives known but unlabeled pool mixes negatives + undiscovered positives. Treating unlabeled as negative creates độ lệch (bias / 편향). PU học tập (learning / 학습) các mô hình (models / 모델들) this explicitly.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, **Positive-Unlabeled học tập (learning / 학습)** cho ta quy tắc; **Multi-Label Annotation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Hierarchical Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Label Annotation

Objects/documents may belong multiple classes. giao diện (interface / 인터페이스) should allow all applicable labels, not force artificial single lớp (class / 클래스).

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Multi-Label Annotation** cho ta quy tắc; **Hierarchical Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Span/Box/Mask Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hierarchical Labels

Taxonomy:

```text
vehicle
├── car
└── truck
```

Annotators may know parent but not leaf. Store label granularity instead of guessing fine lớp (class / 클래스).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Hierarchical Labels** cho ta quy tắc; **Span/Box/Mask Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Label Versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Span/Box/Mask Labels

Structured labels have hình học (geometry / 기하학)/alignment chất lượng (quality / 품질). Bounding box guidelines (tight vs loose), văn bản (text / 텍스트) span ranh giới (boundary / 경계), segmentation contour all need tường minh (explicit / 명시적) policies.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, **Span/Box/Mask Labels** cho ta quy tắc; **Label Versioning** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Gold Set** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Label Versioning

Taxonomy changes:

```text
v1: fraud / not fraud
v2: account takeover / card theft / friendly fraud / clean
```

Historical các mô hình (models / 모델들)/datasets must know label lược đồ (schema / 스키마) phiên bản (version / 버전). di chuyển (migration / 마이그레이션) may require relabeling.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Label Versioning** cho ta quy tắc; **Gold Set** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Annotation QA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gold Set

Maintain high-quality carefully reviewed evaluation set separate from routine annotation. Do not repeatedly tune annotator guidelines against hidden kiểm thử (test / 테스트) examples until it becomes huấn luyện (training / 학습) by proxy.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Annotation QA** tiếp nhận điểm tựa từ **Gold Set** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) vs chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Annotation QA

Methods:

- hidden known-answer tasks;
- overlap between annotators;
- consistency checks;
- impossible-label các ràng buộc (constraints / 제약조건들);
- rà soát (review / 검토) of high-disagreement examples;
- drift monitoring.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, **Chi phí (cost / 비용) vs chất lượng (quality / 품질)** tiếp nhận điểm tựa từ **Annotation QA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) vs chất lượng (quality / 품질)

Annotation ngân sách (budget / 예산) should prioritize uncertain/high-impact regions. 1 million weak labels may be less valuable than 50k consistent domain-relevant labels.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Labeling**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Chi phí (cost / 비용) vs chất lượng (quality / 품질)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Label là đo lường (measurement / 측정) của mục tiêu (target / 대상) concept, không phải concept itself. Chất lượng mô hình (model / 모델) bị giới hạn bởi cách mục tiêu (target / 대상) được operationalize và đo.**

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Labeling**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Human label = ground truth”

Human can disagree, miss ngữ cảnh (context / 맥락) or follow flawed guideline.

### “Majority vote always creates truth”

It can erase valid minority interpretation.

### “LLM labels are free quy mô (scale / 규모)”

They shift annotation lỗi (error / 오류) into mô hình (model / 모델)/prompt độ lệch (bias / 편향) and require kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Labeling**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Labeling connects đo lường (measurement / 측정) lý thuyết (theory / 이론), HCI, statistics, weak supervision and evaluation.

Xem tiếp: [Data Quality](./04_data_quality.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
