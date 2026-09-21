# AI evaluation, data và responsibility

Một AI system không thể được đánh giá chỉ bằng một benchmark score. Model performance phụ thuộc dataset, distribution, metric, threshold, subgroup, latency, cost và downstream human workflow. Evaluation phải nối model output với real-world decision consequences.

## Metric theo task

Classification có precision, recall, F1, ROC-AUC, PR-AUC, calibration. Regression có MAE, MSE, quantile loss. Ranking có NDCG/MRR. Generative systems cần mix automatic metrics, human evaluation và task-specific tests.

Metric chọn sai có thể tối ưu behavior sai.

## Class imbalance

Nếu fraud rate 0.1%, model luôn dự đoán “không fraud” đạt 99.9% accuracy nhưng vô dụng.

Precision trả lời trong alerts, bao nhiêu thật; recall trả lời trong positives thật, bắt được bao nhiêu. Trade-off threshold phải gắn operational cost.

## Calibration

Model calibrated nếu predictions 0.8 xảy ra đúng khoảng 80% trong long run theo grouping phù hợp. Calibration quan trọng khi probabilities feed decision/risk systems.

High ranking accuracy không đảm bảo calibrated probabilities.

## Benchmark leakage và overfitting

Nếu community repeatedly tune trên cùng benchmark, benchmark trở thành training signal xã hội. Dataset contamination có thể làm scores phóng đại generalization.

Evaluation cần held-out/private tests, temporal splits và realistic deployment tasks.

## Subgroup evaluation

Aggregate metric có thể che failure cho subgroup nhỏ. Nhưng subgroup definitions và sample size cần cẩn thận; slicing quá nhiều tạo statistical noise.

Fairness không reducible thành một metric duy nhất; definitions như demographic parity, equalized odds có thể conflict tùy base rates/context.

## Human-in-the-loop

AI output thường đi qua human decision. Automation có thể tạo automation bias: người dùng quá tin suggestion. Ngược lại alert fatigue khiến humans bỏ qua system.

Evaluation phải đo combined human+AI workflow, không chỉ standalone model.

## Data provenance và consent

Dataset cần biết source, license, consent/usage constraints, labeling process và retention. Data quality issue không chỉ missing values mà còn representativeness và provenance.

Datasheets/model cards là documentation patterns để làm assumptions/limitations explicit.

## Robustness và adversarial behavior

Distribution shift, noisy inputs và malicious manipulation có thể degrade model. Adversarial examples/model extraction/prompt injection là security-style threats tùy model class.

AI security cần threat model như software security, không chỉ accuracy testing.

## Reproducibility

Random seeds, data versions, preprocessing, library/hardware kernels và nondeterminism ảnh hưởng training. Reproducibility cần capture experiment metadata và artifact provenance.

Exact bitwise reproducibility không luôn possible/necessary; phải định nghĩa level cần.

## Common Misconceptions

**“Benchmark SOTA nghĩa production tốt nhất.”** Deployment constraints và distribution khác benchmark.

**“Fairness có một công thức đúng.”** Metrics encode normative choices và có thể incompatibility; context/impact matter.

**“Human review tự giải quyết AI risk.”** Human reviewers cũng có workload, bias và information constraints.

## Mental Model

> AI evaluation là system evaluation dưới uncertainty. Model metric chỉ là một layer; cần nối data provenance, subgroup behavior, human workflow và downstream cost.

## Kết nối

Đọc [ML foundations](./02_machine_learning_foundations.md), [computing ethics/privacy](../12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md), [data governance/bias](../12_society_ethics_profession/01_data_governance_bias_and_algorithmic_impact.md) và [security threat modeling](../07_security_reliability/00_threat_models_and_security_principles.md).