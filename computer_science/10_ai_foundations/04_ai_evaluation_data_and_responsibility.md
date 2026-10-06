# AI evaluation, dữ liệu (data / 데이터) và responsibility

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **AI evaluation, data và responsibility**. Route đi từ task metrics/class imbalance → calibration/leakage → subgroup/human evaluation → provenance/consent → robustness/reproducibility, để metric, dữ liệu và trách nhiệm được kiểm tra cùng nhau.

Một AI hệ thống (system / 시스템) không thể được đánh giá chỉ bằng một benchmark score. mô hình (model / 모델) hiệu năng (performance / 성능) phụ thuộc dataset, phân phối (distribution / 분포), chỉ số (metric / 지표), threshold, subgroup, độ trễ (latency / 지연 시간), chi phí (cost / 비용) và downstream human workflow. Evaluation phải nối mô hình (model / 모델) đầu ra (output / 출력) với real-world quyết định (decision / 결정) consequences.

## Chỉ số (metric / 지표) theo tác vụ (task / 작업)

Classification có precision, recall, F1, ROC-AUC, PR-AUC, calibration. Regression có MAE, MSE, quantile mất mát (loss / 손실). Ranking có NDCG/MRR. Generative các hệ thống (systems / 시스템들) cần mix automatic metrics, human evaluation và task-specific tests.

Chỉ số (metric / 지표) chọn sai có thể tối ưu hành vi (behavior / 동작) sai.

> **Nối mạch:** Metric phải khớp task và chi phí lỗi; khi lớp lệch, accuracy có thể che failure của lớp hiếm. **Calibration** đi thêm một bước: kiểm tra xác suất dự báo có đúng mức tin cậy quan sát được hay không.

## Lớp (class / 클래스) imbalance

Nếu fraud tỷ lệ (rate / 비율) 0.1%, mô hình (model / 모델) luôn dự đoán “không fraud” đạt 99.9% accuracy nhưng vô dụng.

Precision trả lời trong alerts, bao nhiêu thật; recall trả lời trong positives thật, bắt được bao nhiêu. sự đánh đổi (trade-off / 트레이드오프) threshold phải gắn operational chi phí (cost / 비용).

> **Nối mạch:** Class imbalance buộc ta chọn metric theo alert và cost; **calibration** hỏi các score đó có thể dùng như xác suất cho quyết định hay không. Sau khi đo chất lượng dự báo, **benchmark leakage** kiểm tra liệu điểm số có bị thổi phồng do dùng lại dữ liệu đánh giá hay không.

## Calibration

Mô hình (model / 모델) calibrated nếu predictions 0.8 xảy ra đúng khoảng 80% trong long run theo grouping phù hợp. Calibration quan trọng khi probabilities feed quyết định (decision / 결정)/rủi ro (risk / 위험) các hệ thống (systems / 시스템들).

High ranking accuracy không đảm bảo calibrated probabilities.

> **Nối mạch:** Calibration làm rõ độ tin cậy của score, nhưng score vẫn có thể lạc quan nếu benchmark đã trở thành tín hiệu huấn luyện gián tiếp. **Subgroup evaluation** tiếp theo kiểm tra liệu kết quả còn giữ được trên các nhóm nhỏ và phân phối khác nhau hay không.

## Benchmark leakage và overfitting

Nếu community repeatedly tune trên cùng benchmark, benchmark trở thành huấn luyện (training / 학습) tín hiệu (signal / 신호) xã hội. Dataset contamination có thể làm scores phóng đại generalization.

Evaluation cần held-out/private tests, temporal splits và realistic triển khai (deployment / 배포) tasks.

> **Nối mạch:** Benchmark leakage làm suy yếu khả năng khái quát, còn **subgroup evaluation** tìm failure bị che bởi metric trung bình và cỡ mẫu nhỏ. Khi phát hiện khác biệt nhóm, **human-in-the-loop** phải được đánh giá như một phần của workflow chứ không phải lớp sửa lỗi tự động.

## Subgroup evaluation

Aggregate chỉ số (metric / 지표) có thể che thất bại (failure / 실패) cho subgroup nhỏ. Nhưng subgroup definitions và cỡ mẫu (sample size / 표본 크기) cần cẩn thận; slicing quá nhiều tạo statistical noise.

Fairness không reducible thành một chỉ số (metric / 지표) duy nhất; definitions như demographic parity, equalized odds có thể xung đột (conflict / 충돌) tùy cơ sở (base / 기반) rates/ngữ cảnh (context / 맥락).

> **Nối mạch:** Subgroup evaluation chỉ ra ai chịu lỗi nhiều hơn; **human-in-the-loop** kiểm tra cách người dùng tiếp nhận, bỏ qua hoặc lạm dụng output trong quyết định thật. Muốn diễn giải kết quả và quyền sử dụng, cần truy tiếp **data provenance và consent**.

## Human-in-the-loop

AI đầu ra (output / 출력) thường đi qua human quyết định (decision / 결정). Automation có thể tạo automation độ lệch (bias / 편향): người dùng quá tin suggestion. Ngược lại alert fatigue khiến humans bỏ qua hệ thống (system / 시스템).

Evaluation phải đo combined human+AI workflow, không chỉ standalone mô hình (model / 모델).

> **Nối mạch:** **Human-in-the-loop** đặt vấn đề; **Dữ liệu (data / 데이터) provenance và consent** kiểm tra bằng chứng, rồi **Robustness và adversarial hành vi (behavior / 동작)** mở rộng hệ quả.

## Dữ liệu (data / 데이터) provenance và consent

Dataset cần biết nguồn (source / 소스), license, consent/usage các ràng buộc (constraints / 제약조건들), labeling tiến trình (process / 프로세스) và retention. dữ liệu (data / 데이터) chất lượng (quality / 품질) issue không chỉ missing values mà còn representativeness và provenance.

Datasheets/mô hình (model / 모델) cards là documentation patterns để làm các giả định (assumptions / 가정들)/limitations tường minh (explicit / 명시적).

> **Nối mạch:** **Dữ liệu (data / 데이터) provenance và consent** đặt vấn đề; **Robustness và adversarial hành vi (behavior / 동작)** kiểm tra bằng chứng, rồi **Reproducibility** mở rộng hệ quả.

## Robustness và adversarial hành vi (behavior / 동작)

Phân phối (distribution / 분포) shift, noisy inputs và malicious manipulation có thể degrade mô hình (model / 모델). Adversarial examples/mô hình (model / 모델) extraction/prompt injection là security-style threats tùy mô hình (model / 모델) lớp (class / 클래스).

AI bảo mật (security / 보안) cần threat mô hình (model / 모델) như software bảo mật (security / 보안), không chỉ accuracy testing.

> **Nối mạch:** **Reproducibility** nối từ **Robustness và adversarial hành vi (behavior / 동작)** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Reproducibility

Random seeds, dữ liệu (data / 데이터) versions, preprocessing, thư viện (library / 라이브러리)/hardware kernels và nondeterminism ảnh hưởng huấn luyện (training / 학습). Reproducibility cần capture experiment siêu dữ liệu (metadata / 메타데이터) và sản phẩm tạo ra (artifact / 산출물) provenance.

Chính xác (exact / 정확한) bitwise reproducibility không luôn possible/necessary; phải định nghĩa mức (level / 수준) cần.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Reproducibility** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Benchmark SOTA nghĩa môi trường vận hành (production / 운영 환경) tốt nhất.”** triển khai (deployment / 배포) các ràng buộc (constraints / 제약조건들) và phân phối (distribution / 분포) khác benchmark.

**“Fairness có một công thức đúng.”** Metrics encode normative choices và có thể incompatibility; ngữ cảnh (context / 맥락)/impact matter.

**“Human rà soát (review / 검토) tự giải quyết AI rủi ro (risk / 위험).”** Human reviewers cũng có tải công việc (workload / 워크로드), độ lệch (bias / 편향) và thông tin (information / 정보) các ràng buộc (constraints / 제약조건들).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> AI evaluation là hệ thống (system / 시스템) evaluation dưới bất định (uncertainty / 불확실성). mô hình (model / 모델) chỉ số (metric / 지표) chỉ là một tầng (layer / 계층); cần nối dữ liệu (data / 데이터) provenance, subgroup hành vi (behavior / 동작), human workflow và downstream chi phí (cost / 비용).

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc [ML foundations](./02_machine_learning_foundations.md), [computing ethics/privacy](../12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md), [data governance/bias](../12_society_ethics_profession/01_data_governance_bias_and_algorithmic_impact.md) và [security threat modeling](../07_security_reliability/00_threat_models_and_security_principles.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
