# Từ dữ liệu AI → đánh giá → nguồn gốc → bằng chứng production

> **Mạch đọc:** Chapter này là tuyến liên kết cho hệ thống AI (AI system / AI 시스템). Chất lượng dữ liệu, gắn nhãn và rò rỉ dữ liệu thuộc [Data for AI](../02_artificial_intelligence/14_data_for_ai/README.md); vòng đời thử nghiệm/mô hình thuộc [MLOps & LLMOps](../02_artificial_intelligence/16_mlops_and_llmops/); hiệu chuẩn, độ bền và khả năng diễn giải thuộc [Evaluation, Reliability & Interpretability](../02_artificial_intelligence/18_evaluation_reliability_interpretability/README.md); thiết kế nghiên cứu thuộc [Research Methods](../../research_methods/README.md); quan sát production thuộc DevOps/SRE. Câu hỏi trung tâm ở đây là: **một kết quả AI trở thành bằng chứng đủ đáng tin để triển khai, theo dõi và quyết định huấn luyện lại bằng cách nào?**

Một mô hình có điểm benchmark cao chưa đủ để nói hệ thống tốt. Một deployment chạy ổn về CPU/latency chưa đủ để nói dự đoán vẫn đúng với population hiện tại. Cần giữ toàn bộ chuỗi bằng chứng:

```text
định nghĩa vấn đề
→ mục tiêu / nhãn / phép đo
→ dataset + split + provenance
→ cấu hình thử nghiệm
→ thiết kế đánh giá
→ metric + bất định
→ threshold / policy
→ artifact + version approval
→ deployment
→ telemetry production
→ outcome trễ / feedback
→ drift / incident / quyết định retrain
```

Nếu mất provenance ở bất kỳ mũi tên nào, con số “87%” gần như vô nghĩa vì ta không biết 87% trên dataset nào, label version nào, split nào, metric implementation nào và có còn đại diện production hay không.

## 1. Bắt đầu từ quyết định, không bắt đầu từ mô hình

Một hệ thống AI tồn tại để hỗ trợ **dự đoán (prediction / 예측)**, **xếp hạng (ranking / 순위화)**, **sinh nội dung (generation / 생성)** hoặc **hành động (action / 행동)**. Vì vậy trước model phải có decision context.

Ví dụ phát hiện gian lận:

```text
input: bối cảnh giao dịch
→ model: xác suất gian lận ước lượng
→ policy: cho qua / review / chặn
→ outcome: fraud loss / false block / review cost / customer friction
```

Nếu chỉ tối ưu AUC mà không biết threshold, cost hoặc policy, đánh giá chưa nối tới quyết định.

Với AI sinh (generative AI / 생성형 AI) cũng tương tự:

```text
yêu cầu người dùng
→ phản hồi hệ thống
→ hành động downstream
→ lợi ích / lỗi / tác hại / chi phí sửa
```

Một câu trả lời “trông hay” chưa phải outcome tốt.

## 2. Nhãn là phép đo, không phải thực tại trực tiếp

**Nhãn (label / 라벨)** thường chỉ là proxy cho khái niệm thật.

Ví dụ:

```text
khái niệm thật: khách hàng thực sự hài lòng
nhãn có sẵn: survey score
```

hoặc:

```text
khái niệm thật: giao dịch gian lận
nhãn có sẵn: chargeback đã được ghi nhận
```

Chargeback có delay, missing case và policy bias. Survey có response bias. Vì vậy chất lượng model bị giới hạn bởi chất lượng measurement.

Nếu định nghĩa label thay đổi theo thời gian, apparent model drift có thể xuất hiện dù hành vi nền không đổi. Do đó model monitoring phải theo dõi cả **measurement process**, không chỉ prediction distribution.

## 3. Dataset phải có identity và version

Một thử nghiệm tái tạo được cần xác định chính xác dữ liệu nào đã dùng.

“Dữ liệu tháng 8” là chưa đủ. Cần truy được:

```text
source snapshot/version
query/transformation version
filter policy
label-generation version
time window
entity/row identity
split assignment
```

Không nhất thiết phải copy cả dataset; một manifest bất biến trỏ tới source snapshot + transform code + version cũng đủ nếu có thể dựng lại input.

## 4. Dòng dõi dữ liệu dài hơn bảng huấn luyện

**Dòng dõi dữ liệu (data lineage / 데이터 계보)** của một feature có thể đi qua:

```text
source system
→ extraction
→ cleaning
→ join
→ aggregation
→ feature transform
→ training snapshot
```

Một lỗi ở upstream join hoặc timestamp semantics có thể tạo model issue nhưng không xuất hiện trong code huấn luyện.

Vì vậy provenance phải bao gồm transform logic và source boundary, không chỉ final CSV/table.

## 5. Chia dữ liệu là một giả định về tương lai

Train/validation/test split không phải thao tác kỹ thuật trung lập. Nó mã hóa giả định về việc production sẽ khác training như thế nào.

Random split có thể phù hợp nếu các sample độc lập và cùng distribution. Nhưng với dữ liệu theo thời gian, entity hoặc user, random split có thể làm leakage.

Cần hỏi:

```text
future production khác training theo time?
entity/user có lặp giữa split?
label có dùng thông tin tương lai?
feature có aggregate qua boundary?
```

Một test set “sạch” về code nhưng sai về causal/time boundary vẫn cho điểm ảo.

## 6. Rò rỉ dữ liệu là vi phạm boundary thông tin

**Rò rỉ dữ liệu (data leakage / 데이터 누수)** xảy ra khi model nhận thông tin mà tại thời điểm dự đoán production không thể biết.

Leakage có thể đến từ:

- feature dùng tương lai;
- preprocessing fit trên toàn dataset;
- duplicate/entity overlap;
- target-derived feature;
- label generation vô tình dùng downstream outcome;
- human annotation đã nhìn thông tin không có ở production.

Điểm nguy hiểm là benchmark có thể tăng rất đẹp. Vì vậy score cao không tự chứng minh pipeline đúng.

## 7. Thử nghiệm phải có cấu hình tái tạo được

Một experiment cần truy được:

```text
data version
code revision
model architecture/version
hyperparameters
random seed khi relevant
training environment
prompt/template/tool config nếu là LLM system
metric implementation
```

Nếu chỉ lưu final model file, rất khó trả lời vì sao hai lần train khác nhau hoặc vì sao model rollback không tái tạo cùng behavior.

## 8. Metric phải nối với loại lỗi thật

Không có metric duy nhất đúng cho mọi hệ thống.

Accuracy có thể vô nghĩa khi class imbalance lớn. AUC đo ranking tốt nhưng không quyết định threshold. Precision/recall trade-off phụ thuộc cost. Calibration cần thiết nếu probability được dùng cho decision. Với generation, aggregate score có thể che lỗi ở nhóm task quan trọng.

Do đó metric selection phải đi từ failure/cost:

```text
loại lỗi nào gây hậu quả?
→ cần metric nào quan sát được lỗi đó?
→ metric nào có thể bị game?
→ metric nào còn thiếu outcome thực tế?
```

## 9. Hiệu chuẩn quan trọng khi probability đi vào policy

**Hiệu chuẩn (calibration / 보정)** hỏi: dự báo 70% có xảy ra gần 70% trong các case tương tự hay không.

Một model rank tốt nhưng overconfident có thể tạo threshold decision tệ. Nếu output probability được dùng để tính expected loss, price risk hoặc chọn action, calibration không phải “nice to have”.

Đọc sâu hơn tại [Xác suất → hiệu chuẩn → quyết định và rủi ro](../../mathematics/09_connections/07_probability_calibration_decision_and_risk.md).

## 10. Aggregate metric có thể che slice failure

Một score chung có thể tốt trong khi model thất bại ở subgroup, geography, device, language, time window hoặc rare case.

**Đánh giá theo lát cắt (slice evaluation / 슬라이스 평가)** cần được chọn dựa trên risk và mechanism, không phải tạo hàng trăm dashboard slice vô nghĩa.

Câu hỏi là:

```text
population nào có failure cost cao?
segment nào có distribution khác?
segment nào ít data?
segment nào đang tăng nhanh trong production?
```

## 11. Benchmark overfitting là một loại selection bias

Nếu team thử nhiều model/prompt trên cùng benchmark rồi chọn cái cao nhất, benchmark dần trở thành một phần của training loop dù không backprop trực tiếp.

Đây là **quá khớp benchmark (benchmark overfitting / 벤치마크 과적합)**.

Cần giữ:

- holdout thật sự ít chạm tới;
- nhiều loại test;
- external/temporal evaluation khi phù hợp;
- error analysis thay vì chỉ chasing score.

## 12. Bất định của metric phải được giữ

Một metric trên sample hữu hạn là estimate. Nếu model A = 0,812 và B = 0,816 nhưng confidence interval overlap mạnh, “B tốt hơn” có thể chưa đủ evidence.

Cần quan tâm:

- sample size;
- variance;
- confidence interval/bootstrap;
- multiple comparison khi thử nhiều model;
- practical significance.

Điều này ngăn team tối ưu noise trong benchmark.

## 13. Artifact không chỉ là weights

Một deployment artifact có thể gồm:

```text
model weights
preprocessor/tokenizer
feature schema
prompt/system instruction
tool configuration
threshold/policy
runtime dependency
model-serving code
```

Nếu rollback chỉ version weights nhưng giữ preprocessor hoặc threshold mới, behavior có thể không quay về thật sự.

Do đó registry cần quản lý **gói behavior**, không chỉ file model.

## 14. Model registry là bản đồ provenance và approval

**Kho mô hình (model registry / 모델 레지스트리)** hữu ích khi trả lời được:

```text
artifact này đến từ experiment nào?
data version nào?
evaluation packet nào?
ai/phần nào approve?
đang deploy ở đâu?
previous stable version là gì?
rollback path là gì?
```

Registry chỉ là danh sách file nếu không có các liên kết này.

## 15. Training–serving skew phá giả định “production giống evaluation”

**Lệch giữa huấn luyện và phục vụ (training-serving skew / 학습·서빙 불일치)** xảy ra khi feature/preprocessing/data availability khác giữa training và production.

Ví dụ:

```text
training dùng batch-computed feature cập nhật mỗi ngày
production cần real-time feature nhưng data đến trễ
```

Model có thể tốt offline nhưng input production mang semantics khác.

Cần monitor cả feature availability, schema, missingness, timestamp freshness và transform parity.

## 16. Deployment cần tách software health khỏi model quality

Một service có thể healthy về HTTP, CPU và latency nhưng model quality đã giảm.

Ngược lại model vẫn đúng về prediction nhưng service latency quá cao làm user abandon.

Vì vậy production evidence cần ít nhất hai lớp:

```text
software/system health
→ availability, latency, error, saturation

model/decision health
→ feature distribution, score distribution, calibration proxy,
   slice behavior, delayed outcome
```

Hai lớp liên quan nhưng không thay thế nhau.

## 17. Shadow, canary và A/B trả lời các câu hỏi khác nhau

**Chạy bóng (shadow deployment / 섀도 배포)** cho model mới nhận traffic copy nhưng không ảnh hưởng user; dùng để kiểm compatibility, latency và output distribution.

**Triển khai canary (canary deployment / 카나리 배포)** cho một phần traffic thật nhận behavior mới; dùng để giới hạn blast radius.

**Thử nghiệm A/B (A/B test / A/B 테스트)** so sánh outcome giữa treatment/control khi thiết kế thử nghiệm cho phép.

Không dùng ba từ này như synonym. Mỗi cơ chế cho loại evidence khác nhau.

## 18. Delayed outcome làm monitoring khó hơn

Nhiều label chỉ xuất hiện sau ngày/tuần/tháng. Fraud chargeback, churn, medical outcome hoặc loan default đều có delay.

Do đó online monitoring thường phải dùng proxy trước:

```text
input drift
score distribution
human-review rate
policy action rate
complaint/correction signal
```

Sau đó mới backfill ground-truth outcome khi label đến.

Proxy giúp cảnh báo nhưng không thay final outcome.

## 19. Drift cần phân loại theo cơ chế

Không phải mọi drift đều giống nhau.

- **Dịch chuyển hiệp biến (covariate shift / 공변량 이동):** input distribution đổi.
- **Dịch chuyển nhãn (label shift / 라벨 이동):** prevalence đổi.
- **Dịch chuyển khái niệm (concept drift / 개념 이동):** quan hệ giữa input và outcome đổi.
- **Measurement drift:** cách tạo feature/label đổi.
- **Policy drift:** downstream action thay đổi và quay lại làm data đổi.

Nếu chỉ đo một distance trên feature distribution, team có thể bỏ sót loại drift quan trọng hơn.

## 20. Retraining không phải phản xạ mặc định

Khi metric giảm, retrain chỉ là một giả thuyết hành động.

Trước hết cần hỏi:

```text
data pipeline có lỗi?
label definition đổi?
production policy đổi?
population đổi?
model thực sự lỗi?
metric proxy có còn đại diện outcome?
```

Nếu root cause là feature bug, retrain trên data hỏng có thể làm tình hình tệ hơn.

## 21. Rollback phải định nghĩa “quay về cái gì”

Rollback cần chỉ rõ:

```text
model artifact
+ preprocessing
+ threshold/policy
+ runtime config
+ feature version
```

Ngoài ra phải xác minh rollback có tương thích với schema/data hiện tại hay không. Previous model không nhất thiết chạy được nếu upstream contract đã thay đổi.

## 22. Incident AI cần evidence chain xuyên nhiều owner

Một incident “prediction xấu” có thể do:

```text
source data
→ feature pipeline
→ schema
→ model artifact
→ serving
→ threshold/policy
→ downstream integration
→ delayed label
```

Runbook cần biết mỗi node do team/domain nào sở hữu và evidence nào kiểm tra node đó. Đây là điểm nối giữa AI, Data Engineering, Backend và DevOps.

## 23. Decision log giúp tránh outcome bias

Trước deployment, nên ghi:

```text
vì sao model này được chọn?
metric nào quyết định?
known weakness?
slice nào rủi ro?
expected production effect?
rollback trigger?
retrain trigger?
```

Sau outcome, quay lại xem assumption nào đúng/sai. Điều này tách decision quality khỏi may mắn của một lần rollout.

## 24. Gói bằng chứng trước khi triển khai

Một **gói bằng chứng (evidence packet / 증거 패킷)** thực dụng có thể gồm:

```text
problem + decision context
data/label provenance
split/leakage checks
metric + uncertainty
slice evaluation
calibration nếu cần
known limitations
artifact/config identity
approval
rollout plan
telemetry plan
rollback trigger
owner
```

Mục tiêu không phải bureaucracy. Mục tiêu là để sáu tháng sau vẫn trả lời được “vì sao model này được deploy?”.

## 25. Mô hình tổng hợp

```text
khái niệm cần dự đoán
→ cách đo bằng label
→ dữ liệu và provenance
→ experiment có thể tái tạo
→ evaluation gắn với cost/outcome
→ artifact + policy có version
→ rollout có giới hạn blast radius
→ system telemetry + model telemetry
→ delayed ground truth
→ drift/root-cause reasoning
→ retrain / rollback / giữ nguyên
```

Bằng chứng production không phải một dashboard. Nó là chuỗi truy nguyên từ outcome ngược về data, model, policy và deployment.

## 26. Bàn giao

Nếu câu hỏi chuyển sang pipeline, grain, CDC hoặc semantic metric, đọc [Query → transaction → pipeline → analytical serving](./06_query_transaction_pipeline_and_analytical_serving.md). Nếu câu hỏi là threat/authority/audit evidence, đọc [Threat model → control → evidence](./05_threat_model_to_control_and_evidence.md). Nếu câu hỏi là delivery, SLO, incident hoặc rollback ở platform, bàn giao sang [DevOps / Platform Engineering](../../devops_platform_engineering/README.md).

> **Bàn giao:** Sau chapter này, người đọc không nên hỏi đơn giản “model score bao nhiêu?” mà phải hỏi **score này đến từ dữ liệu nào, đo cái gì, có uncertainty nào, artifact/policy nào đang chạy, production outcome nào xác nhận nó và trigger nào sẽ làm ta thay đổi quyết định?**