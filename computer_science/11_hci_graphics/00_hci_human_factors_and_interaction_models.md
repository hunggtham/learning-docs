# Human-Computer Interaction, human factors và interaction models

Human-Computer Interaction (HCI / 인간-컴퓨터 상호작용) nghiên cứu cách con người hiểu, điều khiển và hình thành mental model về computer systems. Một interface technically correct vẫn có thể gây lỗi nếu user không biết system state, action consequences hoặc recovery path.

## User là một phần của system

Trong interactive software, output không kết thúc computation; nó thay đổi perception của user, user chọn action mới rồi system tiếp tục. Đây là feedback loop.

Vì vậy usability bug có thể trở thành correctness/safety bug. Nếu banking UI làm user nhầm beneficiary hoặc medical UI che warning quan trọng, problem không còn là “mỹ thuật”.

## Mental model

User xây mental model từ labels, layout, feedback và prior experience. Interface dễ dùng khi model user hình thành gần với behavior thực đủ để dự đoán kết quả actions.

Nếu button “Save” đôi lúc lưu cloud, đôi lúc local draft, mental model không ổn định. Consistency giảm learning cost vì cùng cue → cùng expectation.

## Affordance và signifier

Affordance là action possibilities của object; signifier là cue cho user biết action đó có thể thực hiện.

Một icon không label có thể có affordance click nhưng signifier meaning kém. HCI quan tâm cả khả năng thao tác lẫn khả năng nhận biết.

## Feedback

Action cần feedback tương xứng latency. Nếu save mất 2 giây nhưng UI im lặng, user có thể click lại và tạo duplicate.

Loading indicator, disabled button hoặc optimistic UI là các strategies khác nhau. Feedback phải phản ánh uncertainty/state thật, không chỉ animation.

## Gulf of execution và evaluation

Gulf of execution là khoảng cách giữa goal user và actions interface cung cấp. Gulf of evaluation là khoảng cách giữa system state và khả năng user hiểu state đó.

Good design giảm cả hai: action discoverable, result interpretable.

## Human attention và working memory

Working memory hữu hạn. Interface buộc nhớ mã từ màn hình trước hoặc compare nhiều values không visible tăng cognitive load.

Recognition thường dễ hơn recall. Dropdown/history/autocomplete có thể giảm need nhớ chính xác.

Nhưng quá nhiều choices visible lại tăng visual/search load; design phải balance.

## Fitts's Law

Fitts's Law mô hình thời gian trỏ tới target phụ thuộc distance và target size gần theo:

\[
T = a + b\log_2(1 + D/W)
\]

với `D` là khoảng cách và `W` effective target width.

Insight: target quan trọng nên đủ lớn và placement thuận tiện. Screen edges/corners có effective targeting advantage trong pointer interfaces vì cursor không overshoot boundary.

## Hick–Hyman intuition

Decision time thường tăng khi number/uncertainty của choices tăng. Nhưng không có nghĩa luôn giảm menu items; grouping, hierarchy và familiarity thay đổi effective decision complexity.

## Errors: slips và mistakes

Slip xảy ra khi goal đúng nhưng action sai, như click nhầm delete. Mistake xảy ra khi mental model/goal selection sai.

Prevention khác nhau: slip giảm bằng spacing, undo, confirmation cho irreversible action; mistake giảm bằng clearer model, explanation và constraints.

## Direct manipulation

Dragging object, resizing visual item và immediate feedback tạo cảm giác thao tác trực tiếp trên domain object. Nó mạnh cho spatial tasks nhưng không luôn phù hợp automation/batch operations.

Command interfaces có learning cost cao hơn nhưng composability/efficiency tốt cho experts. UI design phải xem user/task distribution.

## Common Misconceptions

**“UX là làm giao diện đẹp.”** HCI quan tâm cognition, error, learnability, efficiency và feedback, không chỉ aesthetics.

**“User error là lỗi user.”** Repeated predictable error pattern thường cho thấy system design không phù hợp human constraints.

**“Ít click hơn luôn tốt.”** Một click nguy hiểm/khó hiểu có thể tệ hơn flow nhiều bước nhưng rõ ràng.

## Mental Model

> Interactive system là closed feedback loop giữa machine state và human perception/action. Design tốt làm state, available actions và consequences legible.

## Kết nối

Đọc [interface/accessibility/usability](./01_interface_design_accessibility_and_usability.md), [requirements](../09_software_engineering/00_requirements_specification_and_engineering_process.md) và [AI human-in-the-loop](../10_ai_foundations/04_ai_evaluation_data_and_responsibility.md).