# Nhận thức thời gian và trí nhớ tương lai — Temporal Cognition & Prospective Memory

Con người không chỉ nhớ quá khứ; ta còn phải giữ ý định cho tương lai, ước lượng thời gian, chờ reward và phối hợp nhiều deadline. **Nhận thức thời gian (temporal cognition)** là tập hợp process dùng để represent duration, sequence, future delay và thời điểm phải hành động.

## Subjective time không giống clock time

Một phút trên đồng hồ luôn dài 60 giây, nhưng subjective experience có thể rất khác. Khi attention tập trung vào thời gian, duration thường có vẻ dài hơn; khi bị cuốn vào task, cùng khoảng thời gian có thể trôi nhanh.

Arousal, boredom, novelty, emotion và attention đều ảnh hưởng time perception. Vì vậy cảm giác “hôm nay thời gian chạy nhanh” là property của experience chứ không phải clock thay đổi.

## Prospective memory

**Trí nhớ tương lai (prospective memory)** là nhớ thực hiện intention sau này, ví dụ gửi email lúc 3 giờ hoặc mang tài liệu khi rời nhà.

Nó khác retrospective memory ở chỗ không chỉ nhớ “cần làm gì” mà còn phải tự kích hoạt hành động đúng lúc.

Có hai dạng phổ biến. **Event-based prospective memory** được trigger bởi event như “khi gặp A thì hỏi B”. **Time-based prospective memory** cần tự theo dõi thời gian như “đúng 17:00 phải gửi report”. Dạng time-based thường cần self-monitoring nhiều hơn.

## Why we forget intentions

Intentions cạnh tranh với current task. Nếu cue yếu, interruption nhiều hoặc task engrossing, action có thể không được triggered dù person vẫn nhớ intention khi được nhắc.

Đây là lý do nói “tôi biết mà, chỉ quên làm” không mâu thuẫn. Knowledge tồn tại nhưng retrieval đúng thời điểm thất bại.

## Reminder như external trigger

Calendar, alarm và location-based reminder chuyển burden từ internal monitoring sang environment. Đây là [[10_cognitive_offloading_external_memory_and_extended_cognition]].

Reminder tốt cần xuất hiện gần context có thể hành động. Reminder lúc 9 giờ sáng về việc chỉ có thể làm lúc tối có thể tạo acknowledgment nhưng không tạo completion.

## Implementation intention

**Ý định thực thi (implementation intention)** có dạng `Nếu X xảy ra, tôi sẽ làm Y`. Nó liên kết cue cụ thể với action cụ thể.

Ví dụ “sau khi đánh răng tối, tôi sẽ mở Anki 10 phút” thường mạnh hơn goal mơ hồ “tối nay học”. Implementation intention không bảo đảm success nếu workload quá cao, nhưng nó giảm ambiguity ở moment of action.

## Planning fallacy

**Ngụy biện lập kế hoạch (planning fallacy)** là xu hướng underestimate thời gian hoàn thành task, đặc biệt khi dựa quá nhiều vào ideal scenario và bỏ qua base rate của task tương tự.

Kỹ thuật hữu ích là **outside view**: trước khi estimate, xem những task gần giống trước đây mất bao lâu. Trong software development, historical lead time thường đáng tin hơn cảm giác “lần này chắc nhanh”.

## Temporal discounting

Reward xa thường bị discount. Khi future benefit mờ còn present cost rõ, ta dễ chọn option immediate.

Technical debt, saving, exercise và study đều có cấu trúc này. `Không refactor hôm nay` cho reward ngay là tiết kiệm thời gian; cost xuất hiện tháng sau và vì xa nên bị underweight.

Precommitment và environment design giúp bằng cách thay decision architecture trước khi temptation xuất hiện.

## Procrastination

Procrastination không chỉ là time-management failure. Nó thường là **emotion regulation ngắn hạn**: task tạo boredom, uncertainty, threat hoặc shame; avoidance làm distress giảm ngay, nên avoidance được negative reinforcement.

```text
task gây khó chịu
   ↓
avoid / scroll / làm việc khác
   ↓
relief ngay lập tức
   ↓
avoidance được củng cố
   ↓
deadline gần hơn → stress tăng
```

Intervention tốt có thể giảm activation energy, chia next action nhỏ, tạo cue rõ và chấp nhận discomfort thay vì đợi motivation hoàn hảo.

## Deadline và Parkinson-like effects

Deadline tạo constraint giúp prioritize, nhưng deadline quá gần có thể tăng rushed error; quá xa có thể làm task thiếu urgency.

Một project dài thường tốt hơn khi có intermediate milestone tạo feedback thật, không chỉ chia ngày cho đẹp.

## Time estimation trong knowledge work

Knowledge work có variance lớn vì hidden dependency, interruption và rework. Point estimate kiểu “3 ngày” dễ tạo false precision.

Range estimate và explicit assumption tốt hơn: “2–4 ngày nếu API ổn định; thêm 1–2 ngày nếu phải migrate schema”. Điều này kết nối với [[08_decision_under_risk_uncertainty_and_ambiguity]].

## Future self

Con người đôi khi đối xử future self như một người khác: present self hưởng reward, future self trả cost. Tăng psychological continuity với future self có thể làm long-term choice salient hơn, nhưng không thay thế constraint vật chất.

## Episodic future thinking

**Mô phỏng tương lai theo tình tiết (episodic future thinking)** là tưởng tượng event tương lai cụ thể với context chi tiết. Nó có thể làm delayed outcome bớt abstract và hỗ trợ planning trong một số tình huống.

Nhưng future simulation cũng chịu bias từ current mood và autobiographical memory. Xem [[11_emotion_memory_and_affective_cognition]].

## Những hiểu lầm phổ biến

**“Người hay trễ giờ không tôn trọng người khác.”** Có thể đúng trong một số case, nhưng time perception, planning fallacy, executive function và workload cũng ảnh hưởng.

**“Procrastination chỉ là lười.”** Nó thường liên quan avoidance và emotion regulation.

**“Muốn nhớ việc chỉ cần cố nhớ hơn.”** External reminder thường đáng tin hơn pure intention.

**“Estimate tốt là đưa ra một con số chính xác.”** Với uncertainty cao, range và assumption thường trung thực hơn.

## Mô hình tư duy

```text
future intention
 + cue strength
 + time monitoring
 + current task load
 + immediate emotion/reward
 + external support
          ↓
   action đúng thời điểm
```

> Quản lý thời gian hiệu quả không chỉ là chia lịch; đó là thiết kế cue, future reward, uncertainty và emotion quanh hành động.

## Kết nối kiến thức

Xem [[08_decision_under_risk_uncertainty_and_ambiguity]], [[10_cognitive_offloading_external_memory_and_extended_cognition]], [[11_emotion_memory_and_affective_cognition]], [[../06_applied/01_education_learning_and_habit_design]] và [[../06_applied/12_psychology_in_daily_life_and_self_regulation]].
