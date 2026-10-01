# Dataset độ lệch (bias / 편향)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Dataset độ lệch (bias / 편향)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Selection độ lệch (bias / 편향)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Sampling độ lệch (bias / 편향)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Dataset độ lệch (bias / 편향)** là systematic mismatch giữa dữ liệu (data / 데이터) được quan sát và phenomenon/population mà mô hình (model / 모델) intended serve. độ lệch (bias / 편향) không chỉ là “lớp (class / 클래스) imbalance”; nó có thể đến từ sampling, đo lường (measurement / 측정), labels, historical decisions và triển khai (deployment / 배포) phản hồi (feedback / 피드백) loops.

## Selection độ lệch (bias / 편향)

Examples được include không random relative mục tiêu (target / 대상) population.

Ví dụ hospital dataset chỉ chứa people who sought care. mô hình (model / 모델) trained to estimate disease prevalence từ dataset đó may overestimate relative general population.

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Sampling độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Selection độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đo lường (measurement / 측정) độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sampling độ lệch (bias / 편향)

Some subgroups underrepresented:

```text
camera devices
languages
regions
age groups
rare classes
```

Mô hình (model / 모델) may have high aggregate hiệu năng (performance / 성능) but weak subgroup độ tin cậy (reliability / 신뢰성).

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Sampling độ lệch (bias / 편향)** nêu điều cần giải thích; **Đo lường (measurement / 측정) độ lệch (bias / 편향)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Historical độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đo lường (measurement / 측정) độ lệch (bias / 편향)

Tính năng (feature / 기능)/label đo lường (measurement / 측정) chất lượng (quality / 품질) differs across groups. Example ảnh (image / 이미지) chất lượng (quality / 품질) lower on certain devices, or diagnostic kiểm thử (test / 테스트) sensitivity differs.

Same mô hình (model / 모델) may appear “biased” partly because sensor chất lượng (quality / 품질) differs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, **Đo lường (measurement / 측정) độ lệch (bias / 편향)** nêu điều cần giải thích; **Historical độ lệch (bias / 편향)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Label độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Historical độ lệch (bias / 편향)

Dữ liệu (data / 데이터) reflects historical human/hệ thống (system / 시스템) decisions. Hiring records encode who was hired under previous chính sách (policy / 정책), not mục tiêu (objective / 목표) “true talent”.

Học tập (learning / 학습) historical kết quả (outcome / 결과) can reproduce past inequity.

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Historical độ lệch (bias / 편향)** cho ta quy tắc; **Label độ lệch (bias / 편향)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Biểu diễn (representation / 표현) độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Label độ lệch (bias / 편향)

Human labels may systematically differ by subgroup. Moderation/toxicity judgments can reflect dialect/cultural độ lệch (bias / 편향).

Need kiểm tra (audit / 감사) annotator agreement by subgroup, not only toàn cục (global / 전역).

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Label độ lệch (bias / 편향)** cho ta quy tắc; **Biểu diễn (representation / 표현) độ lệch (bias / 편향)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Aggregation độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn (representation / 표현) độ lệch (bias / 편향)

Dùng chung (common / 공통) groups dominate tính năng (feature / 기능) học tập (learning / 학습). Rare ngôn ngữ (language / 언어)/accent may have poorer embeddings/ASR even if labels themselves correct.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, **Aggregation độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Biểu diễn (representation / 표현) độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Aggregation độ lệch (bias / 편향)

One toàn cục (global / 전역) mô hình (model / 모델) assumes same ánh xạ (mapping / 매핑) for heterogeneous populations. If mechanisms differ, pooled mô hình (model / 모델) can hurt some groups.

Separate các mô hình (models / 모델들) or group-aware features may help, but must consider fairness/privacy/legal các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Evaluation độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Aggregation độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Survivorship độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation độ lệch (bias / 편향)

Benchmark itself unrepresentative. mô hình (model / 모델) optimized to benchmark becomes good at measured slice, not intended world.

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Survivorship độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Evaluation độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phản hồi (feedback / 피드백) Loops** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Survivorship độ lệch (bias / 편향)

Only successful/remaining entities observed. Churned or failed cases disappear from later dữ liệu (data / 데이터), distorting conclusions.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, **Phản hồi (feedback / 피드백) Loops** tiếp nhận điểm tựa từ **Survivorship độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Proxy Variables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phản hồi (feedback / 피드백) Loops

Mô hình (model / 모델) decisions affect future dữ liệu (data / 데이터):

```text
rank popular item higher
→ gets more clicks
→ appears even more popular
```

Popularity reinforcement can reduce exposure diversity.

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Proxy Variables** tiếp nhận điểm tựa từ **Phản hồi (feedback / 피드백) Loops** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Simpson’s Paradox** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proxy Variables

Even if protected attribute removed, other features (postcode, school, language) may strongly proxy it.

“Fairness through unawareness” is insufficient.

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Simpson’s Paradox** tiếp nhận điểm tựa từ **Proxy Variables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fairness Metrics Trade-offs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Simpson’s Paradox

Aggregate relationship can reverse within subgroups. Always inspect relevant conditional slices before nhân quả (causal / 인과적)/fairness conclusions.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, **Fairness Metrics Trade-offs** tiếp nhận điểm tựa từ **Simpson’s Paradox** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ lệch (bias / 편향) vs Variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fairness Metrics Trade-offs

Different fairness definitions can xung đột (conflict / 충돌) when cơ sở (base / 기반) rates differ:

- demographic parity;
- equal opportunity/TPR parity;
- equalized odds;
- calibration.

No chỉ số (metric / 지표) universally correct; choice depends xã hội (social / 사회적)/legal quyết định (decision / 결정) ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Độ lệch (bias / 편향) vs Variance** tiếp nhận điểm tựa từ **Fairness Metrics Trade-offs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reweighting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ lệch (bias / 편향) vs Variance

Dataset độ lệch (bias / 편향) here is xã hội (social / 사회적)/statistical sampling concept, distinct from ML **độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프)**. Same word, different meanings.

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Reweighting** tiếp nhận điểm tựa từ **Độ lệch (bias / 편향) vs Variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Resampling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reweighting

If mục tiêu (target / 대상) population phân phối (distribution / 분포) known, importance weights:

\[
w(x)=\frac{P_{mục tiêu (target / 대상)}(x)}{P_{train}(x)}
\]

can adjust huấn luyện (training / 학습)/evaluation under covariate shift các giả định (assumptions / 가정들).

But high weights increase variance and cannot fix missing hỗ trợ (support / 지원) where `P_train(x)=0`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, **Resampling** tiếp nhận điểm tựa từ **Reweighting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Targeted dữ liệu (data / 데이터) Collection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Resampling

Oversampling minority groups/classes increases huấn luyện (training / 학습) exposure. Undersampling majority reduces imbalance but discards dữ liệu (data / 데이터).

Synthetic oversampling may interpolate examples but can amplify artifacts.

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Resampling** nêu điều cần giải thích; **Targeted dữ liệu (data / 데이터) Collection** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Slice-Based Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Targeted dữ liệu (data / 데이터) Collection

Often best fix is collect more real dữ liệu (data / 데이터) in weak slices rather than complex reweighting.

Mô hình (model / 모델) lỗi (error / 오류) phân tích (analysis / 분석) should drive collection priorities.

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Targeted dữ liệu (data / 데이터) Collection** nêu điều cần giải thích; **Slice-Based Evaluation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Intersectionality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Slice-Based Evaluation

Define metrics per subgroup/ngữ cảnh (context / 맥락):

```text
language
region
skin tone (when ethically/legally appropriate)
device
lighting
transaction amount band
new vs existing users
```

Slices should correspond real rủi ro (risk / 위험), not endless arbitrary combinations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, **Intersectionality** tiếp nhận điểm tựa từ **Slice-Based Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Counterfactual Fairness Intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Intersectionality

Độ lệch (bias / 편향) can appear only at intersection of groups, e.g. ngôn ngữ (language / 언어) + age + thiết bị (device / 장치). dữ liệu (data / 데이터) sparsity makes intersection phân tích (analysis / 분석) statistically hard.

Need confidence intervals/minimum mẫu (sample / 표본) rules.

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Counterfactual Fairness Intuition** tiếp nhận điểm tựa từ **Intersectionality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ lệch (bias / 편향) in Foundation các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Counterfactual Fairness Intuition

Ask whether quyết định (decision / 결정) would thay đổi (change / 변경) if protected characteristic changed while relevant underlying factors held appropriately constant. Formal nhân quả (causal / 인과적) definitions require nhân quả (causal / 인과적) mô hình (model / 모델) and strong các giả định (assumptions / 가정들).

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Độ lệch (bias / 편향) in Foundation các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Counterfactual Fairness Intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Synthetic dữ liệu (data / 데이터) and độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ lệch (bias / 편향) in Foundation các mô hình (models / 모델들)

Web-scale văn bản (text / 텍스트)/ảnh (image / 이미지) dữ liệu (data / 데이터) reflects societal stereotypes and uneven ngôn ngữ (language / 언어)/geographic biểu diễn (representation / 표현).

Filtering can reduce harmful content but also erase minority dialects/topics if classifiers biased.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, **Độ lệch (bias / 편향) in Foundation các mô hình (models / 모델들)** nêu điều cần giải thích; **Synthetic dữ liệu (data / 데이터) and độ lệch (bias / 편향)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Label chính sách (policy / 정책) as giá trị (value / 값) Choice** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Synthetic dữ liệu (data / 데이터) and độ lệch (bias / 편향)

Generating synthetic dữ liệu (data / 데이터) from biased mô hình (model / 모델) can reproduce or amplify độ lệch (bias / 편향). Synthetic balancing only helps if generator accurately represents mục tiêu (target / 대상) subgroup.

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Synthetic dữ liệu (data / 데이터) and độ lệch (bias / 편향)** cho ta quy tắc; **Label chính sách (policy / 정책) as giá trị (value / 값) Choice** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dataset Documentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Label chính sách (policy / 정책) as giá trị (value / 값) Choice

Moderation/helpfulness/an toàn (safety / 안전) labels encode normative choices. Dataset documentation should make these policies tường minh (explicit / 명시적).

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Label chính sách (policy / 정책) as giá trị (value / 값) Choice** cho ta quy tắc; **Dataset Documentation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Độ lệch (bias / 편향) Mitigation Layers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dataset Documentation

Datasheets/mô hình (model / 모델) cards style documentation can include:

- motivation;
- composition;
- collection tiến trình (process / 프로세스);
- preprocessing;
- uses/limitations;
- demographic/geographic coverage;
- licensing;
- known biases.

Documentation does not remove độ lệch (bias / 편향) but makes các giả định (assumptions / 가정들) inspectable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, **Độ lệch (bias / 편향) Mitigation Layers** tiếp nhận điểm tựa từ **Dataset Documentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ lệch (bias / 편향) Mitigation Layers

Mitigation can happen:

```text
pre-processing → data collection/reweighting
in-processing  → constraints/loss
post-processing→ thresholds/calibration/policy
```

Fixing dataset/tiến trình (process / 프로세스) nguồn (source / 소스) is often more durable than post-hoc threshold hacks.

> **Chuyển mạch:** Trong **Dataset độ lệch (bias / 편향)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Độ lệch (bias / 편향) Mitigation Layers** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **độ lệch (bias / 편향) asks whose reality dataset represents, whose it misses, và cơ chế selection/đo lường (measurement / 측정) nào tạo ra mismatch đó.**

> **Chuyển mạch:** Ở chặng này của **Dataset độ lệch (bias / 편향)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Balanced lớp (class / 클래스) counts = unbiased dataset”

Độ lệch (bias / 편향) can remain in subgroup coverage, đo lường (measurement / 측정) and labels.

### “Remove protected attribute = fair mô hình (model / 모델)”

Proxy features and historical outcomes still encode it.

### “Fairness has one correct mathematical chỉ số (metric / 지표)”

Metrics encode different normative criteria and can xung đột (conflict / 충돌).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dataset độ lệch (bias / 편향)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Dataset độ lệch (bias / 편향) connects sampling lý thuyết (theory / 이론), nhân quả (causal / 인과적) suy luận (inference / 추론), fairness, xã hội (social / 사회적) các hệ thống (systems / 시스템들) and triển khai (deployment / 배포) phản hồi (feedback / 피드백).

Xem tiếp: [Synthetic Data](./07_synthetic_data.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
