# Interface design, accessibility và usability

Usability không phải cảm giác chủ quan hoàn toàn. Ta có thể quan sát task completion, error rate, time, learnability và satisfaction. Accessibility (khả năng tiếp cận / 접근성) mở rộng câu hỏi: interface có usable với người có năng lực giác quan, vận động, nhận thức và thiết bị khác nhau hay không?

## Usability theo task và user

Một interface nhanh cho expert operator có thể khó cho novice. Command line hiệu quả cho repetitive automation nhưng không discoverable như GUI.

Vì vậy “dễ dùng” luôn cần context: ai, làm task gì, tần suất nào, error cost bao nhiêu.

## Information architecture

Navigation tốt phản ánh cách users phân loại goals, không nhất thiết cách database tables hoặc organization departments được chia.

Card sorting, tree testing và search logs có thể giúp kiểm model categories.

## Visual hierarchy

Size, spacing, position, contrast và grouping hướng attention. Gestalt principles như proximity/similarity giúp user nhận groups mà không cần border mọi thứ.

Visual hierarchy không chỉ aesthetic; nó encode priority và relationship.

## Form design

Forms cần labels rõ, input constraints, error message gần field và preserve entered data khi validation fail.

Validation sớm giúp feedback nhưng server-side validation vẫn bắt buộc vì client không trusted.

Good error message nói điều gì sai và cách sửa, không chỉ “Invalid input”.

## Accessibility không phải add-on cuối dự án

Semantic HTML, keyboard navigation, focus order, text alternatives, contrast và scalable text ảnh hưởng architecture/component design từ đầu.

Screen reader dựa accessibility tree/semantics, không “nhìn pixel” như người sighted.

## Keyboard và focus

Interactive controls phải reachable bằng keyboard nếu use case/platform yêu cầu. Focus indicator cho biết current target; modal phải quản lý focus entry/trap/return hợp lý.

Custom clickable `div` thường thiếu keyboard semantics và accessible role nếu developer không thêm đúng behavior.

## Color

Không nên dùng color là channel duy nhất truyền trạng thái vì color-vision differences và monochrome/high-contrast modes.

Error có thể dùng icon/text + color. Contrast cần đủ theo accessibility guidelines tương ứng, nhưng exact threshold phụ thuộc standard/context.

## Responsive design

Responsive không chỉ shrink desktop UI. Small touch screen có target size, thumb reach, virtual keyboard và network constraints khác.

Layout/content priority có thể cần thay đổi, không chỉ CSS scaling.

## User testing

Quan sát representative users làm representative tasks phát hiện mismatches mà team quen sản phẩm không thấy.

5 users không phải magic number cho mọi research. Sample size phụ thuộc goal, variability và statistical vs qualitative method.

## A/B testing

A/B test đo causal effect của interface variant nếu randomization/metrics đúng. Nhưng local metric tăng có thể hại long-term outcome.

Ví dụ tăng notification clicks không đồng nghĩa tăng user well-being. Metric cần guardrails.

## Dark patterns

Dark pattern dùng asymmetry/confusion để steer user chống lợi ích/preferences của họ, như khó cancel hơn subscribe hoặc hidden fees.

Đây là intersection HCI và ethics: design effectiveness không tự đồng nghĩa design responsibility.

## Common Misconceptions

**“Accessibility chỉ dành cho một nhóm nhỏ.”** Temporary injury, aging, bright sunlight, one-handed use và poor network tạo situational accessibility needs rộng.

**“Semantic HTML chỉ tốt cho SEO.”** Nó hỗ trợ accessibility, browser behavior và maintainability.

**“A/B test thắng nghĩa design tốt hơn.”** Chỉ với metric/horizon/population đã chọn; cần interpret broader effects.

## Mental Model

> Interface là một information-and-action architecture. Accessibility tốt làm semantics/actions survive across different bodies, devices và assistive technologies.

## Kết nối

Đọc [HCI/human factors](./00_hci_human_factors_and_interaction_models.md), [web security](../07_security_reliability/06_web_application_security.md) và [computing ethics](../12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md).