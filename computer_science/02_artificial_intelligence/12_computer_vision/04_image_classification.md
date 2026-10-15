# Ảnh (image / 이미지) Classification

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Image classification**. Route đi từ image/label contract → single-label logits → multi-label independence → class imbalance/calibration → error analysis, để mục tiêu nhãn quyết định cách huấn luyện và đánh giá.

**ảnh (image / 이미지) classification (이미지 분류)** gán một hoặc nhiều labels cho toàn ảnh (image / 이미지). Đây là tác vụ (task / 작업) đơn giản hơn detection/segmentation vì đầu ra (output / 출력) không cần vị trí chính xác của đối tượng (object / 객체).

```text
image → encoder/backbone → global representation → classification head → class probabilities
```

## Single-Label Classification

Mỗi ảnh (image / 이미지) có đúng một lớp (class / 클래스) trong `K` classes. mô hình (model / 모델) đầu ra (output / 출력) logits:

\[
z\in\mathbb{R}^K
\]

Softmax:

\[
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Huấn luyện (training / 학습) thường dùng cross-entropy:

\[
L=-\log p_y
\]

Single-label buộc mỗi ảnh chọn một target class, còn multi-label cho phép nhiều nhãn đồng thời. Vì vậy, xác suất lớp cần được hiểu là niềm tin của mô hình và phải được calibration, không phải xác suất chân lý của thế giới.

## Multi-Label Classification

Một ảnh (image / 이미지) có nhiều labels đồng thời, ví dụ `dog`, `outdoor`, `grass`.

Không dùng softmax competition. Mỗi lớp (class / 클래스) thường có sigmoid independent:

\[
p_k=\sigma(z_k)
\]

và nhị phân (binary / 이진) cross-entropy per label.

Multi-label chỉ mô tả cách gán nhãn; điểm xác suất vẫn có thể lệch khỏi tần suất đúng thực tế. Vì thế, trước khi đánh giá calibration, cần chia dữ liệu sao cho các tập train và kiểm thử đại diện cho tình huống triển khai.

## Lớp (class / 클래스) xác suất (probability / 확률) không phải Truth xác suất (probability / 확률)

Softmax score có thể overconfident, đặc biệt under phân phối (distribution / 분포) shift. Calibration cần evaluate riêng.

Calibration chỉ đáng tin khi phép đo không bị rò rỉ hoặc lệch phân phối; data splitting cung cấp điều kiện kiểm chứng đó. Sau khi chia đúng, class imbalance cho thấy vì sao accuracy tổng thể vẫn có thể đánh lạc hướng.

## Dữ liệu (data / 데이터) Splitting

Random ảnh (image / 이미지) split có thể leak near-duplicate frames từ cùng video/person/sản phẩm (product / 제품) vào train/kiểm thử (test / 테스트). Grouped split theo patient/thiết bị (device / 장치)/scene thường cần để estimate generalization đúng.

Data splitting giúp ước lượng generalization, nhưng phân bố lớp trong mỗi split vẫn quyết định metric có ý nghĩa hay không. Khi mất cân bằng lớp đã được nhận diện, top-k accuracy là một metric bổ sung cho các metric theo lớp.

## Lớp (class / 클래스) Imbalance

Nếu rare defect 0.1%, accuracy vô nghĩa. Metrics phù hợp:

- precision/recall;
- PR-AUC;
- per-class F1;
- macro average;
- expected chi phí (cost / 비용).

Lớp (class / 클래스) weighting/focal mất mát (loss / 손실) có thể đổi huấn luyện (training / 학습) emphasis nhưng không substitute representative dữ liệu (data / 데이터).

Class imbalance nhắc ta không nên chỉ nhìn một con số; top-k cho biết nhãn đúng có nằm trong nhóm dự đoán cao nhất hay không. Confusion matrix sẽ đi sâu hơn, chỉ ra những cặp lớp cụ thể mà mô hình thường nhầm.

## Top-k Accuracy

Top-1 yêu cầu correct lớp (class / 클래스) highest score. Top-5 tính đúng nếu label nằm trong 5 classes score cao nhất. Top-k hữu ích large-taxonomy tasks nhưng có thể irrelevant cho môi trường vận hành (production / 운영 환경) hành động (action / 동작).

Top-k chỉ kiểm tra thứ hạng của nhãn đúng, còn confusion matrix giải thích cấu trúc của lỗi. Những lỗi có hệ thống này là tín hiệu để thiết kế transfer-learning pipeline phù hợp với miền dữ liệu.

## Confusion ma trận (matrix / 행렬)

Cho biết lớp (class / 클래스) nào mô hình (model / 모델) nhầm với lớp (class / 클래스) nào. Aggregate accuracy không reveal systematic thất bại (failure / 실패) between similar categories.

Confusion matrix cho biết mô hình đang nhầm ở đâu; transfer-learning pipeline cung cấp cách bắt đầu từ backbone đã học và thay classifier head. Tiếp theo, freeze hay fine-tune quyết định mức độ cập nhật backbone.

## Transfer học tập (learning / 학습) chuỗi xử lý (pipeline / 파이프라인)

Practical luồng (flow / 흐름):

```text
pretrained backbone
→ replace classifier head
→ train head
→ optionally unfreeze/fine-tune backbone
```

Học tập (learning / 학습) tỷ lệ (rate / 비율) cho pretrained layers thường nhỏ hơn newly initialized head.

Transfer learning đặt backbone pretrained làm điểm xuất phát; freeze hoặc fine-tune kiểm soát mức thích nghi với miền mới. Augmentation sau đó tác động lên chính dữ liệu huấn luyện để cải thiện khả năng khái quát.

## Freeze vs Fine-Tune

Freeze khi dữ liệu (data / 데이터) ít/compute hạn chế/lĩnh vực (domain / 도메인) close. Fine-tune khi enough dữ liệu (data / 데이터) và lĩnh vực (domain / 도메인) shift meaningful.

Full fine-tuning có rủi ro (risk / 위험) catastrophic forgetting/overfit. Parameter-efficient approaches có thể useful.

Freeze/fine-tune quyết định tham số nào được học lại, còn augmentation thay đổi các quan sát mà mô hình phải chịu. Label smoothing điều chỉnh mục tiêu huấn luyện để giảm việc bám quá mức vào nhãn one-hot.

## Augmentation

Dùng chung (common / 공통) transformations:

- random crop/resize;
- horizontal flip;
- color jitter;
- mixup;
- CutMix;
- random erasing.

Mixup creates interpolation:

\[
\tilde x=\lambda x_i+(1-\lambda)x_j
\]

\[
\tilde y=\lambda y_i+(1-\lambda)y_j
\]

encouraging smoother quyết định (decision / 결정) boundaries.

CutMix replaces region from another ảnh (image / 이미지) and mixes labels proportional area, preserving cục bộ (local / 로컬) visual statistics better than pure điểm ảnh (pixel / 픽셀) interpolation.

Augmentation tạo ra các biến thể hợp lệ của ảnh; label smoothing làm mềm tín hiệu mục tiêu thay vì ép mô hình vào xác suất one-hot. Fine-grained classification tiếp tục đặt ra bài toán khó hơn: phân biệt những khác biệt thị giác rất nhỏ.

## Label Smoothing

Replace one-hot mục tiêu (target / 대상) with slightly softened phân phối (distribution / 분포). Can reduce overconfidence but may affect calibration/rare-class học tập (learning / 학습).

Label smoothing có thể giảm overconfidence, nhưng không tự tạo ra đặc trưng cần thiết cho các lớp gần nhau. Fine-grained classification thường cần crop, độ phân giải và dữ liệu chuyên biệt; hierarchical taxonomy bổ sung cấu trúc quan hệ giữa các nhãn.

## Fine-Grained Classification

Distinguishing bird species/sản phẩm (product / 제품) variants requires subtle cục bộ (local / 로컬) features. High-resolution crops, attention/localization and domain-specific dữ liệu (data / 데이터) become important.

Fine-grained classification cần phân biệt các biến thể gần nhau; taxonomy phân cấp cho phép mô hình và metric biểu diễn quan hệ cha–con giữa chúng. Open-set recognition mở rộng câu hỏi: điều gì xảy ra khi ảnh không thuộc bất kỳ lớp đã biết nào?

## Hierarchical Taxonomy

Labels may have hierarchy:

```text
animal → bird → eagle
```

Flat classifier ignores ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조). Hierarchical losses/routing can exploit taxonomy, but evaluation must handle parent/child errors meaningfully.

Taxonomy giúp diễn tả mức độ gần nhau của các lớp đã biết, còn open-set recognition phải phát hiện cả trường hợp không có nhãn phù hợp. Zero-shot classification tiếp cận lớp chưa thấy bằng mô tả văn bản và biểu diễn đa phương thức.

## Open-Set Recognition

Tiêu chuẩn (standard / 표준) classifier assumes đầu vào (input / 입력) belongs to known classes. Real world may contain unknown category. Out-of-distribution/open-set detection attempts identify unfamiliar examples.

High softmax confidence does not guarantee in-distribution.

Open-set recognition hỏi mô hình có biết nói “không biết” hay không; zero-shot thay classifier cố định bằng đối sánh ảnh–văn bản. Khi kết quả zero-shot không như mong đợi, data-centric error analysis giúp phân biệt lỗi nhãn, dữ liệu và prompt.

## Zero-Shot Classification

Vision-language các mô hình (models / 모델들) can compare ảnh (image / 이미지) embedding with văn bản (text / 텍스트) label descriptions, enabling classes not explicitly trained as classifier head.

But hiệu năng (performance / 성능) depends prompt wording, lớp (class / 클래스) ngữ nghĩa (semantics / 의미론) and pretraining coverage.

Zero-shot phụ thuộc vào mô tả lớp và độ phủ của pretraining; error analysis cần kiểm tra cả những yếu tố đó thay vì chỉ đổi kiến trúc. Một dạng lỗi đặc biệt là shortcut learning, khi mô hình dùng tín hiệu phụ thay cho đối tượng cần nhận biết.

## Data-Centric lỗi (error / 오류) phân tích (analysis / 분석)

For each lỗi (error / 오류) cluster ask:

- label wrong?
- ảnh (image / 이미지) ambiguous?
- resolution too low?
- background shortcut?
- rare subgroup missing?
- triển khai (deployment / 배포) camera mismatch?

Mô hình (model / 모델) thay đổi (change / 변경) is only one lever.

Error analysis có thể phát hiện mô hình dựa vào nền, watermark hoặc thiết bị thay vì vật thể; đó là shortcut learning. Saliency và CAM cung cấp một cách quan sát vùng ảnh đang góp phần vào điểm lớp, dù không phải bằng chứng nhân quả.

## Shortcut học tập (learning / 학습)

Mô hình (model / 모델) may classify “cow” from green pasture background rather than animal shape. If triển khai (deployment / 배포) background changes, accuracy collapses.

Counterfactual/background-balanced dữ liệu (data / 데이터) helps detect shortcut reliance.

Shortcut learning cho thấy mô hình có thể dựa vào tín hiệu sai; saliency và CAM giúp kiểm tra giả thuyết đó trên từng dự đoán. Robustness evaluation tiếp tục hỏi liệu dự đoán có giữ được khi ảnh bị nhiễu hoặc thay đổi điều kiện tự nhiên hay không.

## Saliency and CAM

Lớp (class / 클래스) Activation Maps highlight regions contributing to lớp (class / 클래스) score. Useful debugging, not definitive nhân quả (causal / 인과적) explanation.

If mô hình (model / 모델) consistently focuses watermark/corner, dataset leakage likely.

Saliency cho biết vùng mô hình sử dụng, còn robustness cho biết quyết định có bền trước perturbation và corruption hay không. Khi độ tin cậy không đủ, confidence threshold và abstention chuyển phần rủi ro còn lại thành một chính sách vận hành.

## Adversarial / Natural Robustness

Small perturbation or dùng chung (common / 공통) corruptions can degrade mô hình (model / 모델). Robust evaluation should include blur, noise, brightness, compression and viewpoint changes relevant triển khai (deployment / 배포).

Robustness không loại bỏ mọi dự đoán không chắc chắn; threshold và abstention cho phép hệ thống chuyển các trường hợp rủi ro sang người hoặc quy trình khác. Mô hình tư duy dưới đây tóm tắt classification như một quyết định toàn cục có giới hạn không gian.

## Confidence Threshold and Abstention

Hệ thống (system / 시스템) can abstain/manual-review when max confidence below threshold. This converts mô hình (model / 모델) into quyết định (decision / 결정) hệ thống (system / 시스템) with coverage–rủi ro (risk / 위험) sự đánh đổi (trade-off / 트레이드오프).

Selective rủi ro (risk / 위험):

```text
higher threshold → fewer automated predictions, potentially higher precision
```

Abstention bổ sung một lớp quyết định cho classifier: mô hình không chỉ chọn nhãn mà còn có thể từ chối khi rủi ro cao. Các ngộ nhận tiếp theo kiểm tra những giả định thường bị bỏ qua trong chuỗi quyết định đó.

## Mô hình tư duy (mental model / 사고 모델)

> **Classification compresses entire ảnh (image / 이미지) into a toàn cục (global / 전역) quyết định (decision / 결정). Vì vậy nó có thể biết “có gì” nhưng không nhất thiết biết “ở đâu”.**

Detection/segmentation add spatial outputs.

Mô hình tư duy đặt classification trong ranh giới “biết có gì” thay vì “biết ở đâu”; các ngộ nhận cho thấy vì sao metric và confidence không thể tách khỏi bối cảnh vận hành. Phần liên kết kiến thức sẽ nối ranh giới này sang detection.

## Dùng chung (common / 공통) Misconceptions

### “99% accuracy nghĩa mô hình (model / 모델) production-ready”

Need subgroup, shift, calibration, độ trễ (latency / 지연 시간) and thất bại (failure / 실패) chi phí (cost / 비용) evaluation.

### “Softmax 0.99 nghĩa 99% chắc chắn đúng”

Only if calibrated on mục tiêu (target / 대상) phân phối (distribution / 분포).

### “More augmentation always improves”

Invalid augmentations can destroy label ngữ nghĩa (semantics / 의미론).

Các ngộ nhận đã làm rõ giới hạn của accuracy, calibration và augmentation; phần liên kết kiến thức đặt classification cạnh transfer learning và detection để chọn nhánh học tiếp theo.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Classification is the simplest supervised vision head and a foundation for transfer học tập (learning / 학습). Detection extends the tác vụ (task / 작업) to multiple localized objects.

Xem tiếp: [Object Detection](./05_object_detection.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
