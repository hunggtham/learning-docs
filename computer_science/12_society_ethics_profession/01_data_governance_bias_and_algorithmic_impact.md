# Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Dữ liệu (data / 데이터) provenance** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Đo lường (measurement / 측정) độ lệch (bias / 편향)** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) không chỉ là technical ETL. Dataset đại diện cho decisions về đo lường (measurement / 측정), inclusion, labels, truy cập (access / 접근) và retention. Những decisions đó ảnh hưởng mô hình (model / 모델)/report/automation downstream, nên quản trị (governance / 거버넌스) là part of hệ thống (system / 시스템) tính đúng đắn (correctness / 정확성).

## Dữ liệu (data / 데이터) provenance

Provenance trả lời dữ liệu (data / 데이터) đến từ đâu, transform qua steps nào, phiên bản (version / 버전) nào và ai chịu quyền sở hữu (ownership / 소유권). Không có provenance, khi chỉ số (metric / 지표) sai rất khó truy nguyên nhân gốc (root cause / 근본 원인).

Lineage tools biến chuỗi xử lý (pipeline / 파이프라인) dependencies thành đồ thị (graph / 그래프) để impact phân tích (analysis / 분석) khi lược đồ (schema / 스키마)/nguồn (source / 소스) thay đổi.

> **Chuyển mạch:** Provenance cho biết dữ liệu đến từ đâu và biến đổi thế nào; bias measurement cần metric/context rõ, còn sampling bias có thể làm sai ngay trước khi mô hình được huấn luyện.

## Đo lường (measurement / 측정) độ lệch (bias / 편향)

Ta thường không observe concept trực tiếp mà đo proxy. “Productivity” có thể proxy bằng tickets closed; “creditworthiness” bằng historical repayment; “engagement” bằng clicks.

Proxy mismatch tạo độ lệch (bias / 편향) ngay trước thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Đo lường (measurement / 측정) độ lệch (bias / 편향)** nêu điều cần giải thích; **Sampling độ lệch (bias / 편향)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Label độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sampling độ lệch (bias / 편향)

Dataset chỉ phản ánh population được quan sát. Nếu dữ liệu huấn luyện (training data / 학습 데이터) thiếu rural users hoặc devices cũ, mô hình (model / 모델) may generalize kém cho nhóm đó.

Random split không sửa biểu diễn (representation / 표현) gap nếu underlying dataset đã biased.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Sampling độ lệch (bias / 편향)** cho ta quy tắc; **Label độ lệch (bias / 편향)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Phản hồi (feedback / 피드백) loops** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Label độ lệch (bias / 편향)

Labels do humans/institutions tạo có inconsistency và historical chính sách (policy / 정책). Arrest records không bằng crime ground truth; customer hỗ trợ (support / 지원) escalation không bằng mục tiêu (objective / 목표) severity.

ML có thể reproduce institutional độ lệch (bias / 편향) encoded trong labels.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Label độ lệch (bias / 편향)** cho ta quy tắc; **Phản hồi (feedback / 피드백) loops** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Fairness metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phản hồi (feedback / 피드백) loops

Prediction ảnh hưởng môi trường (environment / 환경), tạo dữ liệu (data / 데이터) mới rồi reinforce mô hình (model / 모델). Nếu predictive policing gửi nhiều patrol tới khu A, phát hiện nhiều incidents ở A và dữ liệu (data / 데이터) sau càng “chứng minh” A risky.

Closed-loop các hệ thống (systems / 시스템들) cần evaluate nhân quả (causal / 인과적)/behavioral effects, không chỉ offline accuracy.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Fairness metrics** tiếp nhận điểm tựa từ **Phản hồi (feedback / 피드백) loops** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quản trị (governance / 거버넌스) controls** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fairness metrics

Group fairness metrics formalize different goals: parity of positive rates, equalized lỗi (error / 오류) rates, calibration... Chúng có thể xung đột (conflict / 충돌) khi cơ sở (base / 기반) rates khác.

Không có chỉ số (metric / 지표) “fairness universal”. Selection là normative quyết định (decision / 결정) cần lĩnh vực (domain / 도메인)/stakeholder phân tích (analysis / 분석).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Quản trị (governance / 거버넌스) controls** tiếp nhận điểm tựa từ **Fairness metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Right to deletion và derived dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quản trị (governance / 거버넌스) controls

Useful controls gồm dữ liệu (data / 데이터) classification, truy cập (access / 접근) chính sách (policy / 정책), retention, chất lượng (quality / 품질) checks, lược đồ (schema / 스키마) contracts, lineage, stewardship và deletion workflows.

Quản trị (governance / 거버넌스) không nên chỉ là document; chính sách (policy / 정책) cần map thành technical enforcement/monitoring.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Quản trị (governance / 거버넌스) controls** nêu điều cần giải thích; **Right to deletion và derived dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Algorithmic impact assessment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Right to deletion và derived dữ liệu (data / 데이터)

Xóa nguồn (source / 소스) bản ghi (record / 레코드) không luôn đơn giản nếu dữ liệu (data / 데이터) đã bản sao (copy / 복사) vào bộ nhớ đệm (cache / 캐시), backup, analytics và mô hình (model / 모델) huấn luyện (training / 학습) artifacts. hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처) cần know dữ liệu (data / 데이터) propagation.

Legal obligations vary jurisdiction, nhưng kỹ thuật (engineering / 엔지니어링) principle là deletion/retention must be designed, not improvised.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Right to deletion và derived dữ liệu (data / 데이터)** nêu điều cần giải thích; **Algorithmic impact assessment** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Algorithmic impact assessment

Trước high-impact automation, assessment có thể hỏi affected populations, thất bại (failure / 실패) modes, contestability, human oversight, monitoring và redress.

Goal là discover risks before irreversible triển khai (deployment / 배포), tương tự threat modeling cho bảo mật (security / 보안).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Algorithmic impact assessment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“dữ liệu (data / 데이터) là mục tiêu (objective / 목표) facts.”** đo lường (measurement / 측정)/collection luôn có ngữ cảnh (context / 맥락) và missingness.

**“Remove protected attribute thì mô hình (model / 모델) không biased.”** Proxies/correlated features vẫn encode group thông tin (information / 정보).

**“Fairness chỉ số (metric / 지표) giải ethics.”** chỉ số (metric / 지표) làm sự đánh đổi (trade-off / 트레이드오프) tường minh (explicit / 명시적) nhưng không quyết normative priority thay con người.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> dữ liệu (data / 데이터) hệ thống (system / 시스템) là đo lường (measurement / 측정) hệ thống (system / 시스템). Mỗi trường dữ liệu (field / 필드) là claim về world; quản trị (governance / 거버넌스) giữ provenance, purpose và chất lượng (quality / 품질) của claims đó xuyên vòng đời (lifecycle / 생명주기).

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) quản trị (governance / 거버넌스), độ lệch (bias / 편향) và algorithmic impact**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [AI evaluation](../10_ai_foundations/04_ai_evaluation_data_and_responsibility.md), [database data models](../05_data_databases/00_data_models_and_database_systems.md), [privacy/ethics](./00_computing_ethics_privacy_and_professional_responsibility.md) và [data lifecycle](../90_connections/02_data_lifecycle_memory_disk_network.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
