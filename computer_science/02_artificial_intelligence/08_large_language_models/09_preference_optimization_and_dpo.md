# Preference tối ưu hóa (optimization / 최적화) và Direct Preference tối ưu hóa (optimization / 최적화) (DPO)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Preference optimization và direct preference optimization (DPO)**. Route đi từ preference pairs → reward/preference model assumptions → DPO objective → policy/reference comparison → distribution shift and alignment limits, để DPO được hiểu như một lựa chọn tối ưu hóa có điều kiện.

Sau RLHF cổ điển, một câu hỏi tự nhiên xuất hiện: nếu ta đã có preference pairs `chosen > rejected`, có nhất thiết phải train reward mô hình (model / 모델) riêng rồi chạy reinforcement học tập (learning / 학습) như PPO không? **Direct Preference tối ưu hóa (optimization / 최적화) (DPO)** là một family phương thức (method / 메서드) cho phép cập nhật (update / 업데이트) ngôn ngữ (language / 언어) mô hình (model / 모델) trực tiếp từ preference dữ liệu (data / 데이터) bằng mục tiêu (objective / 목표) supervised-like, giảm độ phức tạp chuỗi xử lý (pipeline / 파이프라인).

## Preference pair

Một mẫu (sample / 표본) thường có dạng:

```text
prompt x
chosen response y_w
rejected response y_l
```

Ta muốn chính sách (policy / 정책) gán relative preference lớn hơn cho `y_w` so với `y_l`, nhưng vẫn giữ chính sách (policy / 정책) không drift quá xa tham chiếu (reference / 참조) mô hình (model / 모델).

Preference pair cho biết tín hiệu cần tối ưu; bước tiếp theo giải thích vì sao DPO vẫn cần một mô hình tham chiếu để giữ cập nhật trong vùng hợp lý.

## Intuition của DPO

DPO xuất phát từ relationship giữa optimal KL-regularized reward chính sách (policy / 정책) và implicit reward. Thay vì explicitly fit `r(x,y)` rồi optimize it, mục tiêu (objective / 목표) có thể viết trực tiếp bằng log-probability ratios giữa chính sách (policy / 정책) hiện tại và tham chiếu (reference / 참조) chính sách (policy / 정책).

Một form phổ biến:

\[
\mathcal L_{DPO}
=-\log\sigma\left(
\beta
\left[
\log\frac{\pi_\theta(y_w\mid x)}{\pi_{ref}(y_w\mid x)}
-
\log\frac{\pi_\theta(y_l\mid x)}{\pi_{ref}(y_l\mid x)}
\right]
\right)
\]

Không cần học thuộc formula ngay. Ý chính là mô hình (model / 모델) được khuyến khích **increase chosen relative to rejected**, sau khi accounting cho hành vi (behavior / 동작) ban đầu của tham chiếu (reference / 참조) mô hình (model / 모델).

Reference tạo điểm neo cho log-probability ratio; `β` sau đó điều chỉnh mức đánh đổi giữa điểm neo này và tín hiệu preference.

## Tại sao cần tham chiếu (reference / 참조) mô hình (model / 모델)?

Nếu chỉ maximize chosen phản hồi (response / 응답) xác suất (probability / 확률), mô hình (model / 모델) có thể overfit preference set và drift khỏi ngôn ngữ (language / 언어) phân phối (distribution / 분포) tốt đã học.

Tham chiếu (reference / 참조) mô hình (model / 모델) tạo anchor. Preference cập nhật (update / 업데이트) đo “thay đổi so với chính sách (policy / 정책) ban đầu”, không chỉ raw likelihood.

Reference giữ mô hình không drift tùy ý; tiếp theo ta xem `β` điều chỉnh mức đánh đổi giữa neo này và tín hiệu preference như thế nào.

## Vai trò của beta

`β` điều khiển strength của preference tối ưu hóa (optimization / 최적화)/regularization relationship.

Trực giác:

```text
β nhỏ/lớn tùy convention implementation
→ trade-off giữa staying near reference và fitting preference strongly
```

Khi dùng thư viện (library / 라이브러리) cụ thể cần kiểm tra chính xác (exact / 정확한) parameterization; không nên chuyển meaning của `β` giữa implementations một cách máy móc.

`β` kiểm soát một trade-off chứ không biến DPO thành phương án thay thế tuyệt đối cho RLHF; lựa chọn phương pháp còn phụ thuộc dữ liệu và yêu cầu triển khai.

## DPO không phải magic replacement cho RLHF

DPO đơn giản hóa kỹ thuật (engineering / 엔지니어링) vì bỏ tường minh (explicit / 명시적) reward mô hình (model / 모델) + on-policy RL vòng lặp (loop / 루프). Nhưng nó vẫn phụ thuộc mạnh vào preference dữ liệu (data / 데이터) chất lượng (quality / 품질) và coverage.

Nếu preference dataset được thu từ chính sách (policy / 정책) cũ và mô hình (model / 모델) mới drift sang phân phối (distribution / 분포) khác, offline labels có thể không cover thất bại (failure / 실패) modes mới.

RL methods có advantage khi muốn online exploration hoặc reward tín hiệu (signal / 신호) phức tạp.

DPO đơn giản hóa pipeline, nhưng tín hiệu chosen vẫn chỉ là so sánh tương đối; vì vậy cần kiểm tra nó có phản ánh chất lượng tuyệt đối hay không.

## Chosen phản hồi (response / 응답) không phải absolute truth

Preference pair chỉ nói `A` được chọn hơn `B` theo guideline/annotator. Nếu cả hai đều sai, DPO vẫn có thể reinforce answer “ít tệ hơn”.

Vì vậy preference tối ưu hóa (optimization / 최적화) không thay factual xác minh (verification / 확인).

Ngay cả khi ranking là hợp lệ, độ dài và các dấu hiệu bề mặt có thể làm lệch tín hiệu; phần kế tiếp xem xét cách phát hiện những lệch đó.

## Length độ lệch (bias / 편향)

Annotators hoặc reward signals thường có độ lệch (bias / 편향) theo phản hồi (response / 응답) length. Nếu chosen responses thường dài hơn, mô hình (model / 모델) có thể learn verbosity preference ngoài intended chất lượng (quality / 품질).

Dataset phân tích (analysis / 분석) nên kiểm tra:

- length phân phối (distribution / 분포);
- style artifacts;
- topic imbalance;
- annotator disagreement;
- position/thứ tự (order / 순서) effects.

Kiểm soát các bias chưa đủ; cặp preference cũng cần độ khó phù hợp để tín hiệu học có đủ phân giải.

## Pair difficulty

Nếu chosen và rejected quá khác chất lượng (quality / 품질), tín hiệu (signal / 신호) dễ nhưng ít fine-grained. Nếu quá giống, labels có thể noisy.

Một good preference dataset thường cần mixture difficulty để mô hình (model / 모델) học distinctions meaningful.

Một pipeline thường dùng SFT để tạo baseline ổn định rồi mới áp dụng preference optimization; từ đó có thể so sánh DPO với các objective khác.

## DPO và SFT dữ liệu (data / 데이터)

Thường chuỗi xử lý (pipeline / 파이프라인):

```text
pretrained model
→ SFT
→ preference optimization
```

SFT tạo stable instruction-following baseline. DPO sau đó refine ranking giữa alternative behaviors.

DPO trực tiếp từ weak cơ sở (base / 기반) mô hình (model / 모델) có thể khó vì chosen samples quá xa hiện tại (current / 현재) chính sách (policy / 정책) phân phối (distribution / 분포).

SFT cung cấp điểm xuất phát, còn DPO chỉ là một trong nhiều cách tối ưu preference; lựa chọn objective tiếp theo cần xét cả an toàn.

## Other preference objectives

DPO không phải only phương thức (method / 메서드). Có nhiều variants/alternatives nhằm xử lý noise, reference-free setup, reward margins hoặc online updates. Tên algorithms thay đổi nhanh; mô hình tư duy (mental model / 사고 모델) bền vững hơn là:

```text
preference data
+ policy/reference likelihood
→ objective làm preferred output tương đối có xác suất cao hơn
```

Các objective khác nhau đều phải được kiểm tra trong bối cảnh an toàn; đặc biệt, dữ liệu offline có thể không đại diện cho traffic khi triển khai.

## Preference tối ưu hóa (optimization / 최적화) và an toàn (safety / 안전)

Preference pairs có thể encode safe hành vi (behavior / 동작), nhưng an toàn (safety / 안전) chính sách (policy / 정책) thường multi-dimensional và adversarial. Một mô hình (model / 모델) optimized trên static pairs vẫn có thể thất bại (fail / 실패) prompt injection/jailbreak.

An toàn (safety / 안전) cần evaluation và defense-in-depth ở hệ thống (system / 시스템) tầng (layer / 계층).

Khi phân phối triển khai khác phân phối preference, kết quả tối ưu có thể suy giảm; mental model tiếp theo giúp giữ rõ ranh giới này.

## Offline phân phối (distribution / 분포) bài toán (problem / 문제)

Preference dataset phản ánh prompts và candidates đã sampled. Nếu triển khai (deployment / 배포) traffic khác mạnh, mô hình (model / 모델) may be optimized cho wrong region of đầu vào (input / 입력) không gian (space / 공간).

Đây là liên kết (connection / 연결) với statistical phân phối (distribution / 분포) shift.

Mental model này tóm tắt DPO như một cập nhật likelihood tương đối có tham chiếu, rồi mở đường cho việc kiểm tra các ngộ nhận.

## Mô hình tư duy (mental model / 사고 모델)

> DPO biến “human thích A hơn B” thành **relative likelihood cập nhật (update / 업데이트)** trực tiếp trên chính sách (policy / 정책), thay vì bắt buộc xây reward mô hình (model / 모델) rồi chạy RL optimizer.

Các ngộ nhận sau đây thường xuất hiện khi bỏ qua reference, chất lượng dữ liệu hoặc khác biệt giữa alignment và preference fitting.

## Dùng chung (common / 공통) Misconceptions

### “DPO không phải reinforcement-learning-related nên không cần hiểu preference/reward”

DPO vẫn bắt nguồn từ KL-regularized preference tối ưu hóa (optimization / 최적화); hiểu reward/preference framing giúp hiểu mục tiêu (objective / 목표).

### “DPO luôn tốt hơn PPO”

Không. Choice phụ thuộc dữ liệu (data / 데이터), online phản hồi (feedback / 피드백) needs, stability và kỹ thuật (engineering / 엔지니어링) các ràng buộc (constraints / 제약조건들).

### “DPO đảm bảo mô hình (model / 모델) aligned”

Nó optimize observed preferences. Alignment rộng hơn dataset và mục tiêu (objective / 목표).

## Liên kết kiến thức (knowledge connection / 지식 연결)

DPO nối [RLHF](./08_rlhf.md), [SFT](./07_supervised_fine_tuning.md), [Probability](../01_mathematical_foundations/02_probability_for_ai.md) và [Distribution Shift](../04_machine_learning/14_bias_variance_and_generalization.md).

Xem tiếp: [In-Context Learning](./10_in_context_learning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
