# Thông tin sai lệch, sửa niềm tin và miễn dịch nhận thức

Thông tin sai lệch (misinformation) không tồn tại chỉ vì người ta “thiếu hiểu biết”. Con người ra quyết định dưới áp lực thời gian, chú ý hữu hạn, trí nhớ nguồn không hoàn hảo, động cơ bản sắc và môi trường truyền thông có incentive riêng. Vì vậy vulnerability với misinformation là kết quả của tương tác giữa nhận thức, xã hội và hệ thống phân phối thông tin.

> **Trạng thái bằng chứng:** repetition/familiarity, source-memory failure và continued influence đều có nền tảng thực nghiệm. Debunking và prebunking/inoculation có thể cải thiện khả năng phân biệt thông tin đáng tin và không đáng tin, nhưng effect không phải vĩnh viễn, không đồng nhất ở mọi context và không thay thế source quality hay platform design.

## 1. Familiarity và illusory truth

**Hiệu ứng chân lý ảo (illusory truth effect)** mô tả việc một câu được lặp lại có thể được đánh giá là đáng tin hơn vì xử lý trở nên trôi chảy hơn.

Điều này không có nghĩa repetition luôn thắng fact-check. Effect phụ thuộc prior knowledge, source cue, task và context. Nhưng nó giải thích vì sao một headline sai được lặp nhiều lần có thể trở nên “quen tai”.

## 2. Source monitoring

Người ta có thể nhớ nội dung nhưng quên nguồn. Đây là lỗi **giám sát nguồn (source monitoring)**.

```text
nhớ claim
+
quên provenance
→ familiarity dễ bị nhầm với credibility
```

Xem [[../02_learning_and_cognition/07_memory_distortion_eyewitness_and_false_memory]].

## 3. Continued influence effect

Ngay cả sau khi correction được chấp nhận, misinformation cũ vẫn có thể ảnh hưởng reasoning nếu nó từng lấp một chỗ trong causal model.

Correction thường hữu ích hơn khi không chỉ nói “điều đó sai”, mà còn cung cấp explanation thay thế đủ để người đọc xây model mới.

## 4. Identity và motivated reasoning

Khi một claim gắn mạnh với political, moral hoặc group identity, evidence có thể được xử lý khác nhau tùy nó bảo vệ hay đe dọa self-concept.

Điểm quan trọng là motivated reasoning không phải đặc điểm của “phe kia”. Nó có thể xuất hiện ở nhiều nhóm và nhiều chủ đề.

## 5. Confirmation bias không chỉ là chọn source mình thích

Thiên kiến xác nhận có thể xuất hiện trong cách chọn nguồn, diễn giải ambiguity, đặt threshold để chấp nhận evidence và nhớ kết quả thuận/không thuận.

Một câu hỏi hữu ích là:

> Bằng chứng nào, nếu xuất hiện, sẽ làm mình hạ confidence?

Nếu answer là “không có gì”, belief gần như đã mất tính falsifiable.

## 6. Debunking

Một correction tốt thường:

```text
fact đúng
→ cảnh báo claim sai
→ giải thích lỗi
→ cung cấp causal alternative nếu cần
→ nhắc lại fact đúng
```

Meta-analytic evidence cho thấy debunking nhìn chung có hiệu quả, nhưng misinformation vẫn có thể để lại ảnh hưởng. Hiệu quả phụ thuộc nội dung, mức người đọc đã đầu tư vào belief, chi tiết correction và bối cảnh truyền thông.

## 7. Prebunking / inoculation

**Miễn dịch nhận thức (inoculation)** hoặc **prebunking** dạy trước tactic thao túng như false dilemma, emotional manipulation, fake expert hoặc cherry-picking.

Meta-analysis tín hiệu–phát hiện công bố 2026 trên 33 thí nghiệm, tổng N khoảng 37.000, cho thấy cả video và gamified inoculation cải thiện discrimination giữa news đáng tin và không đáng tin mà không đơn giản làm người dùng hoài nghi mọi thứ hơn.

> **Bằng chứng tương đối vững:** inoculation có thể tăng discrimination trong điều kiện nghiên cứu đã kiểm tra.

> **Giới hạn:** effect có thể decay, transfer sang tactic/nội dung khác không tuyệt đối và implementation ngoài đời còn phụ thuộc exposure, attention và platform context.

## 8. Accuracy prompts

Một số thí nghiệm cho thấy đưa attention về accuracy trước khi share có thể giảm willingness to share misinformation trong một số context.

Điều này gợi ý rằng sharing không phải lúc nào cũng đi sau full truth evaluation; social signaling, speed và emotion có thể cạnh tranh với accuracy goal.

Không nên nâng accuracy prompt thành universal solution.

## 9. Empathy và correction

Correction có thể thất bại về social communication dù fact đúng. Nếu người nghe cảm thấy bị humiliation hoặc status threat, họ có thể bảo vệ identity thay vì cập nhật belief.

Điều này không có nghĩa “phải đồng ý với misinformation để giữ hòa khí”; nó nghĩa communication design là một phần của intervention.

## 10. Platform incentive

Misinformation không chỉ là cognitive problem. Platform có thể thưởng tốc độ, outrage, novelty và identity signal.

Nếu content sensational nhận engagement cao, creator và recommender system đều có incentive khuếch đại nó.

Xem [[05_digital_psychology_social_media_and_online_behavior]].

## 11. Health misinformation

Health misinformation có thể làm người dùng trì hoãn chăm sóc, thay đổi medication hoặc hiểu sai vaccine/treatment risk.

Vì consequence cao, verification depth nên lớn hơn các claim ít quan trọng.

```text
mức hậu quả cao
→ yêu cầu provenance cao hơn
→ cần source gốc + independent confirmation
```

## 12. AI-generated information

Generative AI làm chi phí tạo plausible text giảm mạnh. Fluency và specificity có thể bị người dùng nhầm với accuracy.

```text
trôi chảy ≠ bằng chứng
cụ thể ≠ đúng
confidence của câu chữ ≠ calibration
```

Xem [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]].

## 13. Verification workflow

Một workflow thực dụng:

1. xác định claim cụ thể;
2. tách fact, interpretation và prediction;
3. tìm nguồn gốc;
4. kiểm tra date/context;
5. tìm source độc lập;
6. xem counterevidence;
7. cập nhật confidence theo evidence.

Depth nên match consequence; không phải mọi claim cần investigation như một paper review.

## 14. Signal Detection Theory

Khi classify thông tin “đúng/sai”, threshold quá nghiêm làm reject cả truth; threshold quá lỏng làm accept misinformation.

Mục tiêu vì vậy không phải “nghi ngờ mọi thứ”, mà là **calibration** với cost của false positive và false negative.

## 15. Ranh giới bằng chứng

**Bằng chứng tương đối vững:** repetition có thể tăng perceived truth; source memory có thể thất bại; debunking và prebunking có positive average effects; alternative explanation giúp correction trong nhiều tình huống.

**Lý thuyết/construct hiện đại:** motivated reasoning, identity-protective cognition, accuracy-attention accounts và inoculation mechanisms.

**Còn tranh luận:** persistence dài hạn, transfer giữa topic/platform/culture, effect ngoài laboratory và interaction với recommender systems.

**Không được nói:** người thông minh miễn nhiễm misinformation, fact-check một lần xóa belief, hoặc prebunking là “vaccine vĩnh viễn”.

## 16. Những hiểu lầm phổ biến

**“Critical thinking là đủ.”** Không; incentive và source environment cũng quan trọng.

**“Debunk càng mạnh càng tốt.”** Communication failure có thể làm correction kém hiệu quả.

**“Dạy manipulation tactic làm người ta hoài nghi mọi thứ.”** Meta-analysis gần đây cho thấy inoculation có thể tăng discrimination mà không nhất thiết tăng generalized skepticism.

## Mô hình tư duy

```text
memory + familiarity + identity
 + source cue + social reward
 + platform distribution
           ↓
      belief update
```

> Belief không nằm một mình trong đầu; nó nằm trong một mạng source–memory–identity–incentive.

## Kết nối kiến thức

Xem [[../02_learning_and_cognition/07_memory_distortion_eyewitness_and_false_memory]], [[05_digital_psychology_social_media_and_online_behavior]], [[../00_foundations/06_open_science_and_evidence_evaluation]], [[../00_foundations/08_causal_inference_and_psychological_evidence]], [[../90_connections/03_risk_uncertainty_and_science_communication]] và [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]].