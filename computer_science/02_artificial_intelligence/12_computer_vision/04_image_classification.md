# Ảnh (image / 이미지) Classification

> **Mạch đọc:** Đặt **ảnh (image / 이미지) Classification** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Single-Label Classification** sang **Multi-Label Classification**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Multi-Label Classification

Một ảnh (image / 이미지) có nhiều labels đồng thời, ví dụ `dog`, `outdoor`, `grass`.

Không dùng softmax competition. Mỗi lớp (class / 클래스) thường có sigmoid independent:

\[
p_k=\sigma(z_k)
\]

và nhị phân (binary / 이진) cross-entropy per label.

## Lớp (class / 클래스) xác suất (probability / 확률) không phải Truth xác suất (probability / 확률)

Softmax score có thể overconfident, đặc biệt under phân phối (distribution / 분포) shift. Calibration cần evaluate riêng.

## Dữ liệu (data / 데이터) Splitting

Random ảnh (image / 이미지) split có thể leak near-duplicate frames từ cùng video/person/sản phẩm (product / 제품) vào train/kiểm thử (test / 테스트). Grouped split theo patient/thiết bị (device / 장치)/scene thường cần để estimate generalization đúng.

## Lớp (class / 클래스) Imbalance

Nếu rare defect 0.1%, accuracy vô nghĩa. Metrics phù hợp:

- precision/recall;
- PR-AUC;
- per-class F1;
- macro average;
- expected chi phí (cost / 비용).

Lớp (class / 클래스) weighting/focal mất mát (loss / 손실) có thể đổi huấn luyện (training / 학습) emphasis nhưng không substitute representative dữ liệu (data / 데이터).

## Top-k Accuracy

Top-1 yêu cầu correct lớp (class / 클래스) highest score. Top-5 tính đúng nếu label nằm trong 5 classes score cao nhất. Top-k hữu ích large-taxonomy tasks nhưng có thể irrelevant cho môi trường vận hành (production / 운영 환경) hành động (action / 동작).

## Confusion ma trận (matrix / 행렬)

Cho biết lớp (class / 클래스) nào mô hình (model / 모델) nhầm với lớp (class / 클래스) nào. Aggregate accuracy không reveal systematic thất bại (failure / 실패) between similar categories.

## Transfer học tập (learning / 학습) chuỗi xử lý (pipeline / 파이프라인)

Practical luồng (flow / 흐름):

```text
pretrained backbone
→ replace classifier head
→ train head
→ optionally unfreeze/fine-tune backbone
```

Học tập (learning / 학습) tỷ lệ (rate / 비율) cho pretrained layers thường nhỏ hơn newly initialized head.

## Freeze vs Fine-Tune

Freeze khi dữ liệu (data / 데이터) ít/compute hạn chế/lĩnh vực (domain / 도메인) close. Fine-tune khi enough dữ liệu (data / 데이터) và lĩnh vực (domain / 도메인) shift meaningful.

Full fine-tuning có rủi ro (risk / 위험) catastrophic forgetting/overfit. Parameter-efficient approaches có thể useful.

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

## Label Smoothing

Replace one-hot mục tiêu (target / 대상) with slightly softened phân phối (distribution / 분포). Can reduce overconfidence but may affect calibration/rare-class học tập (learning / 학습).

## Fine-Grained Classification

Distinguishing bird species/sản phẩm (product / 제품) variants requires subtle cục bộ (local / 로컬) features. High-resolution crops, attention/localization and domain-specific dữ liệu (data / 데이터) become important.

## Hierarchical Taxonomy

Labels may have hierarchy:

```text
animal → bird → eagle
```

Flat classifier ignores ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조). Hierarchical losses/routing can exploit taxonomy, but evaluation must handle parent/child errors meaningfully.

## Open-Set Recognition

Tiêu chuẩn (standard / 표준) classifier assumes đầu vào (input / 입력) belongs to known classes. Real world may contain unknown category. Out-of-distribution/open-set detection attempts identify unfamiliar examples.

High softmax confidence does not guarantee in-distribution.

## Zero-Shot Classification

Vision-language các mô hình (models / 모델들) can compare ảnh (image / 이미지) embedding with văn bản (text / 텍스트) label descriptions, enabling classes not explicitly trained as classifier head.

But hiệu năng (performance / 성능) depends prompt wording, lớp (class / 클래스) ngữ nghĩa (semantics / 의미론) and pretraining coverage.

## Data-Centric lỗi (error / 오류) phân tích (analysis / 분석)

For each lỗi (error / 오류) cluster ask:

- label wrong?
- ảnh (image / 이미지) ambiguous?
- resolution too low?
- background shortcut?
- rare subgroup missing?
- triển khai (deployment / 배포) camera mismatch?

Mô hình (model / 모델) thay đổi (change / 변경) is only one lever.

## Shortcut học tập (learning / 학습)

Mô hình (model / 모델) may classify “cow” from green pasture background rather than animal shape. If triển khai (deployment / 배포) background changes, accuracy collapses.

Counterfactual/background-balanced dữ liệu (data / 데이터) helps detect shortcut reliance.

## Saliency and CAM

Lớp (class / 클래스) Activation Maps highlight regions contributing to lớp (class / 클래스) score. Useful debugging, not definitive nhân quả (causal / 인과적) explanation.

If mô hình (model / 모델) consistently focuses watermark/corner, dataset leakage likely.

## Adversarial / Natural Robustness

Small perturbation or dùng chung (common / 공통) corruptions can degrade mô hình (model / 모델). Robust evaluation should include blur, noise, brightness, compression and viewpoint changes relevant triển khai (deployment / 배포).

## Confidence Threshold and Abstention

Hệ thống (system / 시스템) can abstain/manual-review when max confidence below threshold. This converts mô hình (model / 모델) into quyết định (decision / 결정) hệ thống (system / 시스템) with coverage–rủi ro (risk / 위험) sự đánh đổi (trade-off / 트레이드오프).

Selective rủi ro (risk / 위험):

```text
higher threshold → fewer automated predictions, potentially higher precision
```

## Mô hình tư duy (mental model / 사고 모델)

> **Classification compresses entire ảnh (image / 이미지) into a toàn cục (global / 전역) quyết định (decision / 결정). Vì vậy nó có thể biết “có gì” nhưng không nhất thiết biết “ở đâu”.**

Detection/segmentation add spatial outputs.

## Dùng chung (common / 공통) Misconceptions

### “99% accuracy nghĩa mô hình (model / 모델) production-ready”

Need subgroup, shift, calibration, độ trễ (latency / 지연 시간) and thất bại (failure / 실패) chi phí (cost / 비용) evaluation.

### “Softmax 0.99 nghĩa 99% chắc chắn đúng”

Only if calibrated on mục tiêu (target / 대상) phân phối (distribution / 분포).

### “More augmentation always improves”

Invalid augmentations can destroy label ngữ nghĩa (semantics / 의미론).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Classification is the simplest supervised vision head and a foundation for transfer học tập (learning / 학습). Detection extends the tác vụ (task / 작업) to multiple localized objects.

Xem tiếp: [Object Detection](./05_object_detection.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 images as data](./00_images_as_data.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
