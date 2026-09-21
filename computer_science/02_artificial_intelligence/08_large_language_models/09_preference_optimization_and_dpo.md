# Tối ưu sở thích và Direct Preference Optimization (DPO)

Sau RLHF cổ điển, một câu hỏi tự nhiên xuất hiện: nếu đã có các cặp sở thích `chosen > rejected`, có nhất thiết phải huấn luyện reward model riêng rồi chạy reinforcement learning như PPO không? **Direct Preference Optimization (DPO)** là một nhóm phương pháp cho phép cập nhật mô hình ngôn ngữ trực tiếp từ dữ liệu preference bằng objective gần với supervised learning hơn, nhờ đó đơn giản hóa pipeline.

## Cặp preference

Một sample thường có dạng:

```text
prompt x
phản hồi được chọn y_w
phản hồi bị loại y_l
```

Ta muốn policy ưu tiên tương đối `y_w` hơn `y_l`, nhưng vẫn không để policy trôi quá xa mô hình tham chiếu.

## Trực giác của DPO

DPO xuất phát từ quan hệ giữa policy tối ưu có regularization KL và phần thưởng ngầm. Thay vì học riêng `r(x,y)` rồi tối ưu reward đó, objective có thể viết trực tiếp bằng tỷ lệ log-probability giữa policy hiện tại và policy tham chiếu.

Một dạng phổ biến:

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

Không cần học thuộc công thức. Ý chính là mô hình được khuyến khích **tăng xác suất tương đối của phản hồi được chọn so với phản hồi bị loại**, sau khi tính tới hành vi ban đầu của reference model.

## Vì sao cần mô hình tham chiếu?

Nếu chỉ tăng xác suất của chosen response, mô hình có thể overfit tập preference và trôi khỏi phân bố ngôn ngữ tốt đã học.

Reference model đóng vai trò mỏ neo. Update được đánh giá theo “mức thay đổi so với policy ban đầu” chứ không chỉ raw likelihood.

## Vai trò của beta

`β` kiểm soát quan hệ giữa độ mạnh của tối ưu preference và regularization.

Ý nghĩa chính xác của việc `β` lớn hay nhỏ phụ thuộc cách thư viện tham số hóa objective. Vì vậy không nên chuyển cách hiểu của `β` giữa các implementation một cách máy móc; cần đọc đúng công thức được dùng.

## DPO không phải sự thay thế thần kỳ cho RLHF

DPO đơn giản hóa engineering vì loại bỏ reward model tách riêng và vòng RL on-policy. Tuy nhiên nó vẫn phụ thuộc rất mạnh vào chất lượng và độ bao phủ của dữ liệu preference.

Nếu dataset được thu từ policy cũ còn policy mới trôi sang một phân bố khác, nhãn offline có thể không bao phủ failure mode mới.

Phương pháp RL vẫn có lợi thế khi cần exploration online hoặc reward signal phức tạp.

## Phản hồi được chọn không phải chân lý tuyệt đối

Một preference pair chỉ cho biết `A` được chọn hơn `B` theo guideline hoặc người đánh giá. Nếu cả hai đều sai, DPO vẫn có thể tăng xác suất cho câu trả lời “ít tệ hơn”.

Do đó preference optimization không thay thế factual verification.

## Thiên lệch theo độ dài

Người đánh giá hoặc reward signal có thể vô tình ưu tiên câu trả lời dài. Nếu chosen response thường dài hơn, mô hình có thể học preference về verbosity thay vì chất lượng thật.

Nên phân tích dataset theo:

- phân bố độ dài;
- dấu hiệu phong cách;
- mất cân bằng chủ đề;
- mức bất đồng của annotator;
- hiệu ứng vị trí hoặc thứ tự hiển thị.

## Độ khó của cặp so sánh

Nếu chosen và rejected khác chất lượng quá rõ, tín hiệu dễ nhưng ít tinh tế. Nếu quá giống nhau, nhãn có thể nhiễu.

Dataset preference tốt thường cần nhiều mức độ khó để mô hình học những khác biệt có ý nghĩa.

## DPO và dữ liệu SFT

Pipeline thường là:

```text
mô hình đã pretrain
→ SFT
→ preference optimization
```

SFT tạo baseline làm theo chỉ dẫn ổn định; DPO tiếp tục tinh chỉnh thứ tự ưu tiên giữa các hành vi thay thế.

DPO trực tiếp từ base model yếu có thể khó vì chosen sample quá xa phân bố policy hiện tại.

## Các objective preference khác

DPO không phải phương pháp duy nhất. Có nhiều biến thể và hướng thay thế để xử lý nhiễu, thiết lập không cần reference, margin phần thưởng hoặc cập nhật online.

Tên thuật toán thay đổi nhanh; mô hình tư duy bền vững hơn là:

```text
dữ liệu preference
+ likelihood của policy / reference
→ objective làm đầu ra được ưu tiên có xác suất tương đối cao hơn
```

## Preference optimization và an toàn

Preference pair có thể mã hóa hành vi an toàn, nhưng safety policy thường đa chiều và mang tính đối kháng. Mô hình tối ưu trên các cặp tĩnh vẫn có thể thất bại trước prompt injection hoặc jailbreak.

Safety cần evaluation và defense-in-depth ở cấp hệ thống.

## Vấn đề phân bố của dữ liệu offline

Dataset preference phản ánh prompt và candidate đã từng được lấy mẫu. Nếu traffic production khác mạnh, mô hình có thể được tối ưu cho sai vùng của input space.

Đây chính là một dạng **distribution shift** trong statistical learning.

## Mô hình tư duy

> DPO biến “con người thích A hơn B” thành **cập nhật likelihood tương đối** trực tiếp trên policy, thay vì bắt buộc xây reward model rồi chạy một RL optimizer riêng.

## Những hiểu lầm thường gặp

### “DPO không phải RL nên không cần hiểu reward hoặc preference”

DPO vẫn bắt nguồn từ bài toán preference optimization có regularization KL; hiểu framing reward/preference giúp hiểu đúng objective.

### “DPO luôn tốt hơn PPO”

Không. Lựa chọn phụ thuộc dữ liệu, nhu cầu feedback online, độ ổn định và ràng buộc engineering.

### “DPO bảo đảm mô hình aligned”

DPO tối ưu preference quan sát được. Alignment rộng hơn rất nhiều so với một dataset và một objective.

## Liên kết kiến thức

DPO nối [RLHF](./08_rlhf.md), [SFT](./07_supervised_fine_tuning.md), [Probability](../01_mathematical_foundations/02_probability_for_ai.md) và [Distribution Shift](../04_machine_learning/14_bias_variance_and_generalization.md).

Xem tiếp: [In-Context Learning](./10_in_context_learning.md).