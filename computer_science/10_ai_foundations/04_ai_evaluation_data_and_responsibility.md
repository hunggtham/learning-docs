# AI evaluation, dữ liệu (data / 데이터) và responsibility

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **AI evaluation, dữ liệu (data / 데이터) và responsibility**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Chỉ số (metric / 지표) theo tác vụ (task / 작업)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Lớp (class / 클래스) imbalance** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một AI hệ thống (system / 시스템) không thể được đánh giá chỉ bằng một benchmark score. mô hình (model / 모델) hiệu năng (performance / 성능) phụ thuộc dataset, phân phối (distribution / 분포), chỉ số (metric / 지표), threshold, subgroup, độ trễ (latency / 지연 시간), chi phí (cost / 비용) và downstream human workflow. Evaluation phải nối mô hình (model / 모델) đầu ra (output / 출력) với real-world quyết định (decision / 결정) consequences.

## Chỉ số (metric / 지표) theo tác vụ (task / 작업)

Classification có precision, recall, F1, ROC-AUC, PR-AUC, calibration. Regression có MAE, MSE, quantile mất mát (loss / 손실). Ranking có NDCG/MRR. Generative các hệ thống (systems / 시스템들) cần mix automatic metrics, human evaluation và task-specific tests.

Chỉ số (metric / 지표) chọn sai có thể tối ưu hành vi (behavior / 동작) sai.

> **Chuyển mạch:** Metric phải khớp task và cost of error; class imbalance làm accuracy gây hiểu nhầm, còn calibration hỏi xác suất dự báo có đúng mức tin cậy thực tế không.

## Lớp (class / 클래스) imbalance

Nếu fraud tỷ lệ (rate / 비율) 0.1%, mô hình (model / 모델) luôn dự đoán “không fraud” đạt 99.9% accuracy nhưng vô dụng.

Precision trả lời trong alerts, bao nhiêu thật; recall trả lời trong positives thật, bắt được bao nhiêu. sự đánh đổi (trade-off / 트레이드오프) threshold phải gắn operational chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Calibration** tiếp nhận điểm tựa từ **Lớp (class / 클래스) imbalance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Benchmark leakage và overfitting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Calibration

Mô hình (model / 모델) calibrated nếu predictions 0.8 xảy ra đúng khoảng 80% trong long run theo grouping phù hợp. Calibration quan trọng khi probabilities feed quyết định (decision / 결정)/rủi ro (risk / 위험) các hệ thống (systems / 시스템들).

High ranking accuracy không đảm bảo calibrated probabilities.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Benchmark leakage và overfitting** tiếp nhận điểm tựa từ **Calibration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Subgroup evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Benchmark leakage và overfitting

Nếu community repeatedly tune trên cùng benchmark, benchmark trở thành huấn luyện (training / 학습) tín hiệu (signal / 신호) xã hội. Dataset contamination có thể làm scores phóng đại generalization.

Evaluation cần held-out/private tests, temporal splits và realistic triển khai (deployment / 배포) tasks.

> **Chuyển mạch:** Trong **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Subgroup evaluation** tiếp nhận điểm tựa từ **Benchmark leakage và overfitting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human-in-the-loop** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Subgroup evaluation

Aggregate chỉ số (metric / 지표) có thể che thất bại (failure / 실패) cho subgroup nhỏ. Nhưng subgroup definitions và cỡ mẫu (sample size / 표본 크기) cần cẩn thận; slicing quá nhiều tạo statistical noise.

Fairness không reducible thành một chỉ số (metric / 지표) duy nhất; definitions như demographic parity, equalized odds có thể xung đột (conflict / 충돌) tùy cơ sở (base / 기반) rates/ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Ở chặng này của **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Human-in-the-loop** tiếp nhận điểm tựa từ **Subgroup evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) provenance và consent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human-in-the-loop

AI đầu ra (output / 출력) thường đi qua human quyết định (decision / 결정). Automation có thể tạo automation độ lệch (bias / 편향): người dùng quá tin suggestion. Ngược lại alert fatigue khiến humans bỏ qua hệ thống (system / 시스템).

Evaluation phải đo combined human+AI workflow, không chỉ standalone mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Human-in-the-loop** nêu điều cần giải thích; **Dữ liệu (data / 데이터) provenance và consent** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Robustness và adversarial hành vi (behavior / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) provenance và consent

Dataset cần biết nguồn (source / 소스), license, consent/usage các ràng buộc (constraints / 제약조건들), labeling tiến trình (process / 프로세스) và retention. dữ liệu (data / 데이터) chất lượng (quality / 품질) issue không chỉ missing values mà còn representativeness và provenance.

Datasheets/mô hình (model / 모델) cards là documentation patterns để làm các giả định (assumptions / 가정들)/limitations tường minh (explicit / 명시적).

> **Chuyển mạch:** Trong **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Dữ liệu (data / 데이터) provenance và consent** nêu điều cần giải thích; **Robustness và adversarial hành vi (behavior / 동작)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Robustness và adversarial hành vi (behavior / 동작)

Phân phối (distribution / 분포) shift, noisy inputs và malicious manipulation có thể degrade mô hình (model / 모델). Adversarial examples/mô hình (model / 모델) extraction/prompt injection là security-style threats tùy mô hình (model / 모델) lớp (class / 클래스).

AI bảo mật (security / 보안) cần threat mô hình (model / 모델) như software bảo mật (security / 보안), không chỉ accuracy testing.

> **Chuyển mạch:** Ở chặng này của **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Reproducibility** tiếp nhận điểm tựa từ **Robustness và adversarial hành vi (behavior / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reproducibility

Random seeds, dữ liệu (data / 데이터) versions, preprocessing, thư viện (library / 라이브러리)/hardware kernels và nondeterminism ảnh hưởng huấn luyện (training / 학습). Reproducibility cần capture experiment siêu dữ liệu (metadata / 메타데이터) và sản phẩm tạo ra (artifact / 산출물) provenance.

Chính xác (exact / 정확한) bitwise reproducibility không luôn possible/necessary; phải định nghĩa mức (level / 수준) cần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Reproducibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Benchmark SOTA nghĩa môi trường vận hành (production / 운영 환경) tốt nhất.”** triển khai (deployment / 배포) các ràng buộc (constraints / 제약조건들) và phân phối (distribution / 분포) khác benchmark.

**“Fairness có một công thức đúng.”** Metrics encode normative choices và có thể incompatibility; ngữ cảnh (context / 맥락)/impact matter.

**“Human rà soát (review / 검토) tự giải quyết AI rủi ro (risk / 위험).”** Human reviewers cũng có tải công việc (workload / 워크로드), độ lệch (bias / 편향) và thông tin (information / 정보) các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Trong **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> AI evaluation là hệ thống (system / 시스템) evaluation dưới bất định (uncertainty / 불확실성). mô hình (model / 모델) chỉ số (metric / 지표) chỉ là một tầng (layer / 계층); cần nối dữ liệu (data / 데이터) provenance, subgroup hành vi (behavior / 동작), human workflow và downstream chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **AI evaluation, dữ liệu (data / 데이터) và responsibility**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [ML foundations](./02_machine_learning_foundations.md), [computing ethics/privacy](../12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md), [data governance/bias](../12_society_ethics_profession/01_data_governance_bias_and_algorithmic_impact.md) và [security threat modeling](../07_security_reliability/00_threat_models_and_security_principles.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
