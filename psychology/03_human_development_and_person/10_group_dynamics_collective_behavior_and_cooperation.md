# Động lực nhóm, hành vi tập thể và hợp tác

Con người hiếm khi ra quyết định hoàn toàn một mình. Nhóm, gia đình, công ty, cộng đồng trực tuyến và tổ chức đều tạo ra **động lực nhóm (group dynamics)**: các mẫu hành vi xuất hiện từ tương tác giữa thành viên, chuẩn mực, vai trò, địa vị và dòng thông tin.

Một nhóm không đơn giản là tổng tính cách của các thành viên. Khi vào nhóm, hành vi có thể thay đổi vì trách nhiệm, bản sắc, khán giả, cạnh tranh và yêu cầu phối hợp.

> **Trạng thái bằng chứng:** nhiều hiện tượng như social facilitation, social loafing, conformity, information pooling và coordination loss có nền tảng nghiên cứu lâu dài. Các khái niệm như groupthink hay deindividuation hữu ích nhưng không nên được dùng như nhãn giải thích mọi thất bại của nhóm.

## 1. Vì sao nhóm tồn tại?

Nhóm giúp chia sẻ nguồn lực, thông tin và rủi ro. Hợp tác cho phép con người hoàn thành nhiệm vụ vượt quá khả năng cá nhân.

Nhưng nhóm cũng tạo chi phí: phối hợp, xung đột, free-riding, cạnh tranh địa vị và méo thông tin. Một team tốt không phải team không có chi phí, mà là team có cấu trúc làm lợi ích hợp tác lớn hơn chi phí phối hợp.

## 2. Social facilitation và yêu cầu nhiệm vụ

Sự hiện diện của người khác có thể làm hiệu suất tăng ở nhiệm vụ quen thuộc nhưng giảm ở nhiệm vụ mới hoặc khó. Các giải thích bao gồm tăng mức kích hoạt, lo bị đánh giá và xung đột chú ý.

Vì vậy open office, pair programming hay trình bày trước nhóm không tự động tốt hoặc xấu; effect phụ thuộc độ khó nhiệm vụ và mức thành thạo.

## 3. Social loafing và visibility của đóng góp

Khi đóng góp cá nhân khó quan sát, nỗ lực đôi khi giảm — **social loafing**.

Cơ chế có thể gồm trách nhiệm bị phân tán, niềm tin rằng người khác sẽ bù, contribution ít được nhìn thấy hoặc mục tiêu nhóm thiếu ý nghĩa.

Giải pháp không chỉ là giám sát mạnh hơn. Role clarity, task identity, feedback và quy mô nhóm hợp lý cũng quan trọng.

## 4. Coordination loss

Ngay cả khi mọi người đều cố gắng, team vẫn có thể hoạt động kém do **mất mát phối hợp (coordination loss)**.

Nhiều developer cùng sửa một module nhưng ownership không rõ có thể tạo conflict và duplicated work. Khả năng tổng của nhóm cao nhưng hệ thống không chuyển được thành output tương ứng.

Điểm này nối trực tiếp với architecture ownership, incident response và project management.

## 5. Vai trò và chuẩn mực

**Vai trò (role)** tạo kỳ vọng về trách nhiệm; vai trò rõ giúp phối hợp nhưng quá cứng có thể làm thông tin bị mắc kẹt. Một junior có thể thấy risk nhưng nghĩ “không phải phần của mình”.

**Chuẩn mực (norm)** thường được học từ hành vi được thưởng/phạt hơn là từ policy. Nếu công ty nói “quality first” nhưng chỉ thưởng tốc độ giao hàng, chuẩn mực thực sẽ nghiêng về speed.

## 6. Status và information pooling

Địa vị ảnh hưởng ai được nghe, ai nói trước và ý kiến của ai trở thành mốc neo. Người status cao có thể ảnh hưởng discussion dù expertise không cao nhất.

Một kỹ thuật tốt là lấy đánh giá độc lập trước khi thảo luận chung để giảm anchoring theo senior.

Nhóm chỉ có lợi từ đa dạng thông tin nếu unique information thực sự được đưa vào discussion. Nhiều nhóm nói nhiều về **shared information** vì nó dễ xác nhận lẫn nhau, còn dữ liệu độc nhất của từng người bị bỏ qua.

Xem [[15_power_status_hierarchy_and_inequality]].

## 7. Groupthink nên được hiểu như pattern, không phải nhãn ma thuật

**Groupthink** mô tả tình huống áp lực đồng thuận làm giảm đánh giá phản biện. Risk tăng khi leader nêu preference quá sớm, dissent có social cost, nhóm bị cô lập hoặc stress cao.

Các guardrail hữu ích gồm pre-mortem, independent review, red team và kênh nêu concern không bị trừng phạt.

> **Giới hạn:** không nên nhìn một quyết định sai rồi retroactively gắn nhãn groupthink mà không kiểm tra process thực tế.

## 8. Group polarization và môi trường số

Sau thảo luận, nhóm đôi khi đi mạnh hơn theo hướng ban đầu — **group polarization**. Các cơ chế gồm tiếp xúc với argument cùng hướng, social comparison, identity signaling và selective information.

Thuật toán mạng xã hội có thể làm một số process này mạnh hơn khi feed tối ưu engagement, nhưng không nên nói thuật toán tự động tạo cực đoan ở mọi người.

Xem [[../06_applied/05_digital_psychology_social_media_and_online_behavior]].

## 9. Deindividuation và accountability

Trong crowd hoặc môi trường ẩn danh, self-awareness và accountability có thể thay đổi. Tuy nhiên ẩn danh không tự động tạo hành vi xấu; chuẩn mực của nhóm quyết định hướng.

Anonymous community có thể toxic nếu aggression được reward, nhưng cũng có thể hỗ trợ disclosure an toàn nếu norm prosocial.

## 10. Information cascade

**Thác thông tin (information cascade)** xảy ra khi người sau dựa nhiều vào hành động của người trước hơn thông tin riêng của mình.

```text
quan sát người khác
→ suy ra “họ biết điều gì đó”
→ làm theo
→ hành vi tập thể trở thành bằng chứng mới
```

Một cascade có thể đúng hoặc sai. Khi evidence gốc yếu nhưng visibility cao, sai lệch có thể khuếch đại.

## 11. Cooperation dilemma

Hợp tác thường có tension giữa lợi ích cá nhân ngắn hạn và lợi ích nhóm dài hạn. Public-goods problem minh họa việc mọi người cùng hưởng lợi từ resource chung nhưng từng người có incentive free-ride.

Hợp tác bền vững thường cần repeated interaction, reputation, monitoring, sanction công bằng và shared identity.

## 12. Trust phải được hiệu chỉnh

Trust giảm transaction cost. Nếu mọi hành động đều phải kiểm tra chi tiết, team trở nên chậm.

Nhưng blind trust tạo vulnerability. Team lành mạnh cần **niềm tin được hiệu chỉnh (calibrated trust)**: autonomy tăng khi evidence về độ tin cậy tăng, còn review mạnh hơn khi uncertainty hoặc risk cao.

## 13. Psychological safety và accountability

**An toàn tâm lý (psychological safety)** là niềm tin rằng team tương đối an toàn cho interpersonal risk như hỏi, thừa nhận lỗi hoặc nêu concern.

Safety không phải comfort và không loại bỏ accountability. Team có safety cao nhưng standard thấp vẫn có thể hoạt động kém.

Xem [[../06_applied/16_psychological_safety_team_learning_and_speaking_up]].

## 14. Task, process và relationship conflict

Có thể phân biệt:

- **xung đột nhiệm vụ (task conflict)**: khác nhau về nội dung công việc;
- **xung đột quy trình (process conflict)**: ai làm gì, khi nào;
- **xung đột quan hệ (relationship conflict)**: threat cá nhân, disrespect hoặc resentment.

Task disagreement có thể hữu ích nếu không trượt thành relationship threat.

Xem [[../06_applied/03_interpersonal_communication_and_conflict]].

## 15. Minority influence và dissent

Majority influence mạnh, nhưng minority nhất quán có thể buộc nhóm kiểm tra assumption sâu hơn. Dissent có giá trị ngay cả khi minority cuối cùng sai, vì nó tạo pressure phải giải thích reasoning.

Một team không có disagreement chưa chắc đồng thuận thật; có thể chỉ thiếu psychological safety.

## 16. Leadership tạo norm qua attention và reward

Leader ảnh hưởng nhóm không chỉ bằng lời nói mà qua thứ họ hỏi, lỗi nào bị phạt, ai được nói và metric nào được thưởng.

Behavior của leader thường là tín hiệu mạnh hơn poster giá trị.

Xem [[../06_applied/00_work_organization_and_leadership]].

## 17. Shared mental model và transactive memory

**Mô hình tinh thần chung (shared mental model)** là phần hiểu biết chồng lấp đủ để thành viên dự đoán mục tiêu, vai trò và hành động của nhau.

**Trí nhớ giao dịch (transactive memory)** là việc team biết “ai biết gì” thay vì mọi người phải nhớ tất cả.

Documentation, ownership map và knowledge sharing giúp hai hệ thống này hoạt động tốt hơn và giảm bus factor.

## 18. Ranh giới bằng chứng

**Bằng chứng tương đối vững:** social facilitation, coordination cost, social loafing, conformity/status effects và information-pooling problems có hỗ trợ thực nghiệm ở nhiều bối cảnh.

**Lý thuyết/construct hữu ích nhưng cần context:** groupthink, deindividuation, shared mental model và transactive memory.

**Không được nói:** nhóm luôn kém cá nhân, consensus nghĩa là quyết định đúng, hoặc anonymous setting tự động làm con người mất đạo đức.

## Mô hình tư duy

```text
member ability + information diversity
            ↓
 norm + role + status + coordination
            ↓
 information flow + trust + dissent
            ↓
      group performance
```

> Hiệu suất nhóm không chỉ phụ thuộc “ai giỏi”, mà phụ thuộc hệ thống biến năng lực và thông tin của họ thành quyết định chung như thế nào.

## Kết nối kiến thức

Đọc cùng [[15_power_status_hierarchy_and_inequality]], [[04_social_and_cultural_psychology]], [[../06_applied/00_work_organization_and_leadership]], [[../06_applied/16_psychological_safety_team_learning_and_speaking_up]], [[../06_applied/03_interpersonal_communication_and_conflict]] và [[../90_connections/03_risk_uncertainty_and_science_communication]].