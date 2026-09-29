# Từ dữ liệu AI → evaluation → provenance → production evidence

> **Mạch đọc:** Chapter này là tuyến liên kết (connection route / 연결 경로) cho AI systems. Data quality, labeling và leakage thuộc [Data for AI](../02_artificial_intelligence/14_data_for_ai/README.md); experiment/model lifecycle thuộc [MLOps & LLMOps](../02_artificial_intelligence/16_mlops_and_llmops/); evaluation/calibration/robustness thuộc [Evaluation, Reliability & Interpretability](../02_artificial_intelligence/18_evaluation_reliability_interpretability/README.md); research design thuộc `research_methods/`; production observability thuộc DevOps/SRE. Mục tiêu của route này là trả lời câu hỏi: **một AI result trở thành evidence đáng tin để deploy và tiếp tục vận hành như thế nào?**

Một model có score tốt chưa đủ để nói system tốt. Một benchmark tăng chưa đủ để nói user outcome tăng. Một deployment chạy ổn về CPU/latency chưa đủ để nói model vẫn đúng với population hiện tại.

Chuỗi cần giữ là:

```text
problem definition
→ target / label / measurement
→ dataset + split + provenance
→ experiment configuration
→ evaluation design
→ metric + uncertainty
→ decision threshold / policy
→ artifact/version approval
→ deployment
→ production telemetry
→ delayed outcome / feedback
→ drift / incident / retraining decision
```

Nếu bất kỳ arrow nào mất provenance, ta có thể biết “model hiện tại tốt 87%” nhưng không biết 87% trên dataset nào, label version nào, split nào, metric implementation nào và có còn đại diện production không.

## 1. Bắt đầu từ decision, không bắt đầu từ model

AI system tồn tại để hỗ trợ prediction, ranking, generation hoặc action. Vì vậy trước model phải có **decision context**.

Ví dụ fraud detection:

```text
input: transaction context
model output: estimated fraud risk
policy: review / block / allow
business outcome: fraud loss, false block, review cost, customer friction
```

Nếu chỉ tối ưu AUC mà không biết threshold/policy và cost, evaluation chưa nối tới decision.

Với generative AI cũng tương tự:

```text
user request
→ model/system response
→ downstream user action
→ utility / error / harm / correction cost
```

“Response trông hay” không tự động là outcome tốt.

## 2. Target là một measurement, không phải reality trực tiếp

Label (nhãn / 라벨) thường là proxy cho khái niệm thật.

Ví dụ:

```text
true concept: khách hàng thật sự hài lòng
available label: survey score
```

hoặc:

```text
true concept: giao dịch gian lận
available label: chargeback được ghi nhận
```

Chargeback có delay, missing cases và policy bias. Survey có response bias.

Vì vậy model quality bị giới hạn bởi measurement quality. Nếu label thay đổi definition theo thời gian, model drift có thể xuất hiện dù underlying behavior không đổi.

## 3. Dataset phải có identity và version

Một experiment reproducible cần biết chính xác data nào đã dùng.

Không đủ:

```text
trained on data from August
```

Tốt hơn:

```text
source snapshot/version
query/transformation version
filter policy
label-generation version
time window
row/entity identity
split assignment
```

Data version không nhất thiết là copy toàn bộ dataset; có thể là immutable manifest + source snapshot reference + code version. Nhưng phải reconstruct được input.

## 4. Data lineage của AI dài hơn training table

Một feature có thể đi qua:

```text
operational DB
→ CDC / warehouse
→ feature transformation
→ training dataset
→ online feature serving
→ model prediction
```

Training lineage và serving lineage phải được nối.

Nếu training feature tính `30_day_spend` theo UTC nhưng online feature dùng local timezone, model artifact không đổi nhưng semantics đầu vào đã đổi.

Đây là training-serving skew (훈련-서빙 불일치 / lệch huấn luyện–phục vụ).

## 5. Split design là causal assumption về future use

Random split không luôn đại diện production.

Nếu production predict future users/events, time-based split thường mô phỏng deployment tốt hơn random split khi distribution thay đổi theo thời gian.

Nếu cùng user/entity xuất hiện cả train và test, model có thể exploit entity-specific pattern thay vì generalize.

Evaluation split cần hỏi:

```text
future deployment population là ai?
information nào thực sự có trước prediction time?
entity nào phải được tách?
time leakage có thể xảy ra ở đâu?
```

Data leakage canonical owner: [Data Leakage](../02_artificial_intelligence/14_data_for_ai/05_data_leakage.md).

## 6. Test set cũng là một finite sample

Metric trên test set là estimate, không phải constant tuyệt đối.

Hai model khác nhau 0.2 percentage point có thể không khác meaningful nếu sample nhỏ hoặc metric variance cao.

Cần hiểu:

```text
point estimate
+ uncertainty
+ subgroup variance
+ repeated evaluation risk
```

Nếu team iterate hàng trăm lần và nhìn cùng test set, test set dần trở thành training signal thông qua human selection.

Đây là một dạng benchmark overfitting.

## 7. Metric phải gắn với error geometry

Accuracy có thể vô nghĩa khi class imbalance lớn. AUC đo ranking, không trực tiếp cho biết threshold hiện tại tạo bao nhiêu false positive.

Classification có thể cần:

```text
precision
recall
specificity
FPR/FNR
PR-AUC
ROC-AUC
calibration
expected cost
```

Generation có thể cần kết hợp:

```text
task success
factuality / groundedness
constraint following
latency
cost
safety failures
human preference / correction rate
```

Không có một metric universal cho AI quality.

## 8. Calibration nối probability với policy

Nếu model output được dùng như risk score, calibration quan trọng.

Trong một nhóm prediction khoảng 0.8, nếu outcome xảy ra chỉ 0.5, score không nên được đọc như probability 80%.

Canonical route tổng quát nằm tại [Probability → Calibration → Decision & Risk](../../mathematics/09_connections/07_probability_calibration_decision_and_risk.md).

AI layer cần hỏi thêm:

```text
calibration trên population nào?
subgroup nào miscalibrated?
shift mới có phá calibration không?
threshold policy phụ thuộc consequence nào?
```

## 9. Offline quality ≠ online utility

Một model tốt trên historical dataset có thể kém khi deploy vì:

```text
user behavior thay đổi
feedback loop
latency làm feature cũ
policy/action thay đổi label distribution
UI thay đổi cách user tương tác
model output ảnh hưởng chính data tương lai
```

Ví dụ recommender thay đổi items user nhìn thấy. Dataset tương lai không còn được generate bởi policy cũ.

Do đó online evaluation cần nhìn system feedback, không chỉ model score.

## 10. Shadow, canary và A/B trả lời câu hỏi khác nhau

**Shadow evaluation** chạy model mới trên production traffic nhưng không dùng output để quyết định. Nó đo technical behavior và prediction distribution mà giảm user impact.

**Canary** đưa model mới cho một phần traffic để kiểm tra deployment/system risk.

**A/B test** so outcome giữa policies/treatments trong điều kiện experiment phù hợp.

Không nên gọi mọi partial rollout là A/B test.

Nếu assignment không randomized hoặc user cross-over giữa groups, causal interpretation yếu hơn.

## 11. Evaluation artifact phải có provenance

Một evaluation report cần reference ít nhất:

```text
model artifact/version
prompt/system configuration nếu có
retrieval index/version nếu có
tool configuration nếu có
dataset/eval-suite version
metric implementation version
runtime/dependency version quan trọng
run timestamp
code commit
```

Với LLM system, “model version” đơn lẻ thường không đủ vì output phụ thuộc prompt, retrieval, tools và orchestration.

## 12. Provenance graph nên nối artifact tới evidence

Hãy tưởng tượng graph:

```text
source data
→ dataset version
→ training run
→ model artifact
→ evaluation run
→ approval decision
→ deployment
→ production observations
```

Mỗi edge nên có stable identifier.

Khi incident xảy ra, câu hỏi phải trả lời được:

> Deployment `prod-ai-2026-09-29` đang dùng model nào, model đó đến từ training run nào, training run dùng data nào, evaluation nào đã approve nó, và production evidence nào cho thấy regression bắt đầu khi nào?

Nếu graph này không reconstruct được, postmortem sẽ dựa vào memory của team.

## 13. Model registry không chỉ là file storage

Registry có giá trị khi nó giữ lifecycle state và evidence relationship:

```text
candidate
→ evaluated
→ approved
→ staged
→ production
→ deprecated / rolled back
```

Một artifact “latest.pkl” hoặc “model-final-v7” không đủ semantic.

Canonical owner: [Model Registry](../02_artificial_intelligence/16_mlops_and_llmops/03_model_registry.md).

## 14. Approval nên dựa vào gates rõ, không dựa vào score đẹp nhất

Deployment gate có thể gồm:

```text
offline performance floor
subgroup/slice checks
calibration bound
latency/cost budget
robustness tests
safety/adversarial tests
reproducibility/provenance completeness
rollback readiness
```

Không phải system nào cũng cần mọi gate; nhưng gate phải phản ánh failure cost.

High-stakes decision cần evidence mạnh hơn low-risk personalization.

## 15. Slice evaluation thường quan trọng hơn global average

Global accuracy có thể tăng trong khi một important subgroup giảm mạnh.

Slice có thể theo:

```text
country / language
new vs returning user
rare class
device / channel
product category
traffic source
time period
```

Slice không chỉ để fairness; nó còn giúp tìm distribution boundary nơi model generalize kém.

Nhưng chia quá nhiều slice tạo multiple-comparison/noise problem. Slice nên gắn hypothesis hoặc operational importance.

## 16. Robustness test hỏi “nếu input thay đổi hợp lý thì behavior có ổn không?”

Robustness không chỉ adversarial attack.

Có thể test:

```text
missing fields
format variation
small measurement noise
language variation
long-tail categories
stale context
retrieval failure
tool timeout
```

Với LLM/RAG, model-only eval bỏ sót nhiều system failure.

## 17. LLM evaluation phải đánh giá system, không chỉ base model

Một RAG answer có thể sai do:

```text
retrieval không tìm đúng document
chunking làm mất context
ranker chọn sai evidence
prompt hướng model sai
model hallucinate ngoài context
citation mapper trỏ sai source
```

Do đó eval nên tách stage:

```text
retrieval recall
ranking quality
context sufficiency
answer correctness
citation support
task success
```

Nếu chỉ chấm final answer, root cause khó tìm.

## 18. Human evaluation cần rubric và inter-rater reasoning

Human judge không phải ground truth tự động.

Một rubric cần operationalize tiêu chí:

```text
correctness
relevance
completeness
clarity
safety
```

Judge cần example/reference cho ambiguous cases. Nếu nhiều reviewer disagree cao, vấn đề có thể nằm ở rubric/construct chứ không chỉ reviewer quality.

LLM-as-judge cũng cần được validated cho task đó; không nên coi judge model là oracle.

## 19. Production monitoring có ít nhất ba lớp

AI monitoring nên tách:

```text
system health
model/input behavior
business/user outcome
```

System health:

```text
latency
error rate
timeout
resource saturation
cost
```

Model/input behavior:

```text
feature distribution
prediction distribution
confidence/calibration proxy
retrieval/tool success
output length / refusal / safety pattern
```

Outcome:

```text
conversion
fraud loss
manual correction
customer complaint
human escalation
delayed label performance
```

CPU green không chứng minh AI quality green.

## 20. Drift detection không tự nói model đã hỏng

Input distribution thay đổi không nhất thiết làm performance giảm; performance giảm có thể xảy ra mà marginal feature drift nhỏ.

Phân biệt:

```text
covariate shift
label shift
concept drift
policy shift
measurement drift
```

Drift alert là signal cần investigation, không tự động là retraining command.

Canonical owner: [Drift & Retraining](../02_artificial_intelligence/16_mlops_and_llmops/07_drift_and_retraining.md).

## 21. Delayed labels tạo khoảng mù production

Nhiều outcome chỉ biết sau vài ngày/tuần. Fraud chargeback, default, retention hoặc medical outcome đều có delay.

Khi label chưa đến, team chỉ có leading indicators:

```text
input shift
prediction distribution
policy action rate
human review rate
complaint/escalation
```

Khi delayed label đến, phải backfill performance theo prediction cohort/time, không chỉ theo label-arrival date.

Nếu không, metric temporal attribution bị sai.

## 22. Feedback loop có thể làm evaluation tự thay đổi population

Nếu model chặn high-risk transaction, future dataset chỉ chứa labels cho transaction được allow/review theo policy. Một phần counterfactual outcome không quan sát được.

Model/policy đã can thiệp vào data-generating process.

Đây là lý do online AI system đôi khi cần exploration, randomized holdout hoặc causal design phù hợp để estimate policy effect.

Không thể luôn train/evaluate bằng dữ liệu “tự nhiên” vì policy đã tạo dữ liệu đó.

## 23. Production incident phải có model/data/config timeline

Một AI regression timeline nên có:

```text
source data/schema change
feature pipeline change
prompt/retrieval config change
model artifact deploy
threshold/policy change
first distribution anomaly
first user-visible error
first delayed-label degradation
rollback/recovery
```

Nhiều incident không do model weights.

Nếu prompt hoặc feature pipeline thay đổi cùng ngày với model deploy nhưng telemetry chỉ log model version, root cause attribution gần như không thể.

## 24. Rollback AI có thể không đưa system về trạng thái cũ

Rollback model binary không đủ nếu:

```text
feature schema đã migrate
retrieval index đã rebuild
prompt contract đã đổi
downstream policy đã đổi
cache/state đã được ghi bởi version mới
```

Rollback plan phải xác định compatibility boundary giữa artifact, feature, schema, index, prompt và policy.

## 25. Retraining không nên là phản xạ đầu tiên

Khi performance giảm, nguyên nhân có thể là:

```text
bad input pipeline
label delay/change
threshold policy sai
serving bug
feature skew
distribution shift thật
model aging
```

Nếu pipeline bug nhưng team retrain, model mới học trên bad data và làm problem khó hơn.

Runbook đúng là locate first divergent boundary trước khi chọn retraining.

## 26. Reproducibility có nhiều cấp độ

Phân biệt:

```text
code reproducibility
input-data reproducibility
training-run reproducibility
metric reproducibility
behavioral reproducibility
```

Deep learning có thể có hardware/nondeterminism khiến weights không byte-identical dù setup tương đương. Mục tiêu thực tế thường là reproduce evidence và behavior envelope, không nhất thiết bit-for-bit artifact.

## 27. Research reproducibility và production reproducibility khác trọng tâm

Research hỏi liệu finding có tái tạo dưới method đã mô tả. Production hỏi liệu artifact/evidence/deployment có trace được và recovery được.

Hai hướng gặp nhau ở provenance:

```text
claim
↔ method
↔ data
↔ code/config
↔ result
```

Research Methods giúp giữ distinction giữa exploratory finding, confirmatory test và evidence strength.

## 28. Benchmark improvement ≠ product improvement

Một model mạnh hơn trên benchmark có thể:

```text
chậm hơn quá nhiều
đắt hơn quá nhiều
khó calibrate hơn
failure tail nguy hiểm hơn
không cải thiện user task
```

Product decision phải combine model quality với system constraint và user/business utility.

Do đó model selection là multi-objective decision.

## 29. Cost và latency là một phần của quality envelope

Nếu model tốt hơn 1% nhưng latency tăng 3×, timeout/dropout có thể làm end-to-end success giảm.

Quality envelope:

```text
correctness
reliability
latency
cost
safety
operability
```

Không tối ưu một dimension rồi giả định system tốt hơn.

## 30. Decision log cho AI release

Một release decision nên ghi:

```text
candidate artifact/config
intended population/use case
baseline
key metrics + uncertainty
known weak slices
safety/reliability findings
latency/cost delta
approval threshold
rollback trigger
monitoring plan
owner
```

Sau release, review decision quality chứ không chỉ outcome.

Nếu release có evidence hợp lý nhưng random outcome xấu, process có thể vẫn tốt. Nếu release thành công nhờ may mắn dù evidence yếu, process cần sửa.

## 31. Worked case: fraud model offline tốt hơn nhưng production loss tăng

Giả sử model B có PR-AUC cao hơn model A và được deploy. Hai tuần sau fraud loss tăng.

Không kết luận ngay “model B tệ”. Vẽ path:

```text
source events
→ feature pipeline
→ model B score
→ threshold policy
→ review/block action
→ user/adversary response
→ delayed fraud labels
→ loss metric
```

Kiểm tra:

**Data provenance:** training/eval có dùng label definition giống production không?

**Feature parity:** online features có cùng semantics với offline features không?

**Calibration:** model B ranking tốt hơn nhưng calibration khác có làm threshold cũ không còn phù hợp?

**Policy:** review capacity cố định có bị overload vì action rate tăng?

**Adversarial adaptation:** fraud pattern đã đổi sau policy deployment?

**Delayed outcome:** loss cohort có được attribute theo prediction date không?

**Operational issue:** timeout có fallback sang allow không?

Chỉ sau khi tìm first divergence mới quyết định rollback model, đổi threshold, fix feature pipeline hay retrain.

## 32. Failure mode: metric leakage

Eval dataset chứa information chỉ xuất hiện sau prediction time. Score rất cao nhưng production collapse.

Guardrail:

```text
prediction-time data contract
feature availability timestamp
entity/time-aware split
lineage audit
```

## 33. Failure mode: benchmark contamination

Training/pretraining/fine-tuning data chứa eval items hoặc near-duplicates. Benchmark score tăng nhưng không phản ánh generalization.

Cần dataset provenance/dedup và benchmark governance. Với foundation models, contamination có thể khó chứng minh hoàn toàn; uncertainty này phải được ghi rõ.

## 34. Failure mode: metric gaming

Team tối ưu một metric đến mức system behavior lệch goal thật.

Ví dụ support bot giảm escalation rate bằng cách không offer human handoff, nhưng user frustration tăng.

Goodhart-like failure xảy ra khi proxy biến thành target mà không có balancing metrics.

## 35. Failure mode: hidden configuration drift

Weights giữ nguyên nhưng prompt, retrieval index, feature lookup hoặc tool schema đổi. Performance thay đổi nhưng registry vẫn nói “same model”.

Với AI systems, deployable unit nên được định nghĩa rộng hơn weight file.

Có thể là:

```text
model + prompt + retrieval/index + tools + policy + feature contract
```

## 36. Failure mode: retraining loop tự củng cố bias

Model ảnh hưởng action; action ảnh hưởng labels; labels mới lại train model. Nếu policy systematically suppresses observation của một subgroup, data mới có thể củng cố blind spot.

Cần monitor coverage/selection mechanism, không chỉ label accuracy.

## 37. Production evidence packet

Một AI system mature nên có thể tạo một “evidence packet” cho release/version:

```text
problem/use-case definition
data + label provenance
eval suite/version
metric results + uncertainty
slice/robustness/safety findings
artifact/config identity
approval record
deployment identity
monitoring dashboard/runbook
known limitations
rollback/recovery plan
```

Đây không nhất thiết là một PDF; có thể là linked metadata/artifacts. Quan trọng là traceable.

## 38. Canonical owner map

Đọc sâu tại:

- [Data for AI](../02_artificial_intelligence/14_data_for_ai/README.md)
- [Data Leakage](../02_artificial_intelligence/14_data_for_ai/05_data_leakage.md)
- [Data Governance](../02_artificial_intelligence/14_data_for_ai/08_data_governance.md)
- [MLOps & LLMOps](../02_artificial_intelligence/16_mlops_and_llmops/00_mlops_and_llmops.md)
- [Experiment Tracking & Reproducibility](../02_artificial_intelligence/16_mlops_and_llmops/01_experiment_tracking_and_reproducibility.md)
- [Data & Model Versioning](../02_artificial_intelligence/16_mlops_and_llmops/02_data_and_model_versioning.md)
- [Model Registry](../02_artificial_intelligence/16_mlops_and_llmops/03_model_registry.md)
- [Feature Pipelines & Training-Serving Consistency](../02_artificial_intelligence/16_mlops_and_llmops/05_feature_pipelines_and_training_serving_consistency.md)
- [Monitoring & Observability](../02_artificial_intelligence/16_mlops_and_llmops/06_monitoring_and_observability.md)
- [Drift & Retraining](../02_artificial_intelligence/16_mlops_and_llmops/07_drift_and_retraining.md)
- [AI Evaluation Foundations](../02_artificial_intelligence/18_evaluation_reliability_interpretability/00_evaluation_foundations.md)
- [Metrics, Benchmarks & Test Design](../02_artificial_intelligence/18_evaluation_reliability_interpretability/01_metrics_benchmarks_and_test_design.md)
- [Uncertainty & Calibration](../02_artificial_intelligence/18_evaluation_reliability_interpretability/02_uncertainty_and_calibration.md)
- [Robustness & Distribution Shift](../02_artificial_intelligence/18_evaluation_reliability_interpretability/03_robustness_and_distribution_shift.md)
- [AI Testing & Behavioral Evaluation](../02_artificial_intelligence/18_evaluation_reliability_interpretability/05_ai_testing_and_behavioral_evaluation.md)
- [AI Reliability Engineering](../02_artificial_intelligence/18_evaluation_reliability_interpretability/07_reliability_engineering.md)
- [Research Methods](../../research_methods/README.md)
- [Probability → Calibration → Decision & Risk](../../mathematics/09_connections/07_probability_calibration_decision_and_risk.md)

## 39. Mô hình tư duy cuối

Hãy giữ distinction:

```text
model score
≠ system quality
≠ user utility
≠ business outcome
```

Và giữ chuỗi evidence:

```text
measurement
→ dataset provenance
→ experiment provenance
→ evaluation with uncertainty
→ deployment decision
→ artifact/config provenance
→ production telemetry
→ delayed outcome
→ review / recalibration / retraining
```

Nếu không trace được từ production behavior ngược về data/evaluation đã approve release, AI lifecycle chưa thật sự reproducible. Nếu metric tốt nhưng decision context không rõ, evaluation chưa hoàn chỉnh. Nếu drift alert có nhưng không biết first divergent boundary, monitoring chưa đủ để hành động.

> **Bàn giao:** Sau chapter này, người đọc nên có thể lấy một AI feature/model/LLM system thực tế và tạo evidence map từ data source tới production outcome, xác định version/provenance cần ghi, metric và slice cần theo dõi, rollback trigger và điều kiện nào thực sự justify retraining.