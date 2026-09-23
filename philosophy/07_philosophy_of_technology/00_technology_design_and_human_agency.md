# Technology, Design và Human Agency

Technology không chỉ là vật thể trung tính nằm ngoài xã hội. Thiết kế quyết định affordance, default, visibility, cost of action và ai có quyền sửa hệ thống. Tuy vậy, nói “technology tự quyết định mọi thứ” cũng sai: institutions, users, incentives và regulation cùng định hình outcome.

## Các câu hỏi kiểm tra

1. Hệ thống làm cho hành động nào dễ hoặc khó hơn?
2. Data, classification và metric đại diện cho ai, bỏ sót ai?
3. Ai chịu benefit, risk, error và chi phí giám sát?
4. Automation thay thế task hay chuyển quyền quyết định sang một actor khó thấy?
5. Có appeal, contestability, reversibility và human accountability không?

Trong AI, accuracy không đủ để quyết định deployment. Cần xem objective, proxy, distribution shift, uncertainty, human oversight và value trade-off. “Human in the loop” chỉ có ý nghĩa nếu con người có thông tin, quyền can thiệp và thời gian để thực sự sửa quyết định.

Liên hệ với [Computer Science](../../computer_science/README.md), [AI](../../computer_science/02_artificial_intelligence/README.md) và [Psychology về human–AI collaboration](../../psychology/90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading.md).

## Case: recommendation system

Một recommender tối ưu watch time có thể làm tăng engagement nhưng thay đổi attention, exposure diversity và beliefs. Để đánh giá, không chỉ hỏi model có accurate không; cần hỏi objective, feedback loop, population-level externality, user understanding, opt-out, vulnerable users và khả năng audit. Nếu người dùng thích nội dung do hệ thống liên tục cho xem, preference quan sát được vừa là input vừa là sản phẩm của design.

## Agency dưới automation

Human agency không chỉ là còn một nút “approve”. Người duyệt cần thấy uncertainty, alternatives, reason codes và có quyền override mà không bị penalty ngầm. Nếu workload khiến mọi người rubber-stamp output, oversight trên giấy trở thành automation bias. Thiết kế có trách nhiệm phải phân bổ cả quyền quyết định, năng lực hiểu và nghĩa vụ giải trình.

## Depth pass: technology, agency và quyền lực được vật chất hóa

### Question và definitions

Technology vừa là artifact, practice, infrastructure và institution. Agency không chỉ là “có nút override”; nó cần information, competence, time, alternative và freedom from retaliation. Design làm một số action rẻ/dễ, một số action đắt/khó, qua đó phân bổ power trước cả khi có policy.

### Strongest argument và premises

Technological mediation argument nói artifact hình thành perception và habit; social-shaping rival nhấn mạnh procurement, labor, law và user adaptation. Một claim về bias cần nêu construct, population, metric, baseline và feedback loop. Accuracy chỉ là một property; legitimacy còn cần purpose, contestability, privacy, safety và distribution of error.

### Objection, reply và primary-source context

Objection với “technology is political” là thiết kế không tự quyết định outcome: cùng tool có thể có governance khác. Reply: non-determinism không có nghĩa neutrality; defaults và infrastructure tạo switching cost và path dependence. Primary-source context từ Winner và STS tradition hữu ích để đặt câu hỏi về built-in politics, nhưng phải kiểm tra bằng deployment evidence chứ không coi theory là case.

### Empirical boundary và implication

Audit cần test distribution shift, human workload, automation bias, opt-out, appeal và second-order effects. “Human in the loop” chỉ có nghĩa khi override thực tế, reason code và liability rõ. Implication: deploy theo staged/reversible path, log decisions, cho phép independent audit và thiết kế exit; agency cần được đo trong context chứ không suy ra từ giao diện.
