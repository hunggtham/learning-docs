# Nhận thức thời gian và trí nhớ tương lai — Temporal Cognition & Prospective bộ nhớ (memory / 메모리)

> **Mạch đọc:** Đọc **Nhận thức thời gian và trí nhớ tương lai — Temporal Cognition & Prospective bộ nhớ (memory / 메모리)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Subjective thời gian (time / 시간) không giống clock thời gian (time / 시간)** sang **Prospective bộ nhớ (memory / 메모리)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Con người không chỉ nhớ quá khứ; ta còn phải giữ ý định cho tương lai, ước lượng thời gian, chờ reward và phối hợp nhiều deadline. **Nhận thức thời gian (temporal cognition)** là tập hợp tiến trình (process / 프로세스) dùng để represent duration, chuỗi (sequence / 시퀀스), future delay và thời điểm phải hành động.

## Subjective thời gian (time / 시간) không giống clock thời gian (time / 시간)

Một phút trên đồng hồ luôn dài 60 giây, nhưng subjective experience có thể rất khác. Khi attention tập trung vào thời gian, duration thường có vẻ dài hơn; khi bị cuốn vào tác vụ (task / 작업), cùng khoảng thời gian có thể trôi nhanh.

Arousal, boredom, novelty, emotion và attention đều ảnh hưởng thời gian (time / 시간) perception. Vì vậy cảm giác “hôm nay thời gian chạy nhanh” là thuộc tính (property / 속성) của experience chứ không phải clock thay đổi.

## Prospective bộ nhớ (memory / 메모리)

**Trí nhớ tương lai (prospective memory)** là nhớ thực hiện intention sau này, ví dụ gửi email lúc 3 giờ hoặc mang tài liệu khi rời nhà.

Nó khác retrospective bộ nhớ (memory / 메모리) ở chỗ không chỉ nhớ “cần làm gì” mà còn phải tự kích hoạt hành động đúng lúc.

Có hai dạng phổ biến. **Event-based prospective bộ nhớ (memory / 메모리)** được trigger bởi sự kiện (event / 이벤트) như “khi gặp A thì hỏi B”. **Time-based prospective bộ nhớ (memory / 메모리)** cần tự theo dõi thời gian như “đúng 17:00 phải gửi report”. Dạng time-based thường cần self-monitoring nhiều hơn.

## Why we forget intentions

Intentions cạnh tranh với hiện tại (current / 현재) tác vụ (task / 작업). Nếu cue yếu, interruption nhiều hoặc tác vụ (task / 작업) engrossing, hành động (action / 동작) có thể không được triggered dù person vẫn nhớ intention khi được nhắc.

Đây là lý do nói “tôi biết mà, chỉ quên làm” không mâu thuẫn. kiến thức (knowledge / 지식) tồn tại nhưng retrieval đúng thời điểm thất bại.

## Reminder như bên ngoài (external / 외부) trigger

Calendar, alarm và location-based reminder chuyển burden từ nội bộ (internal / 내부) monitoring sang môi trường (environment / 환경). Đây là [[10_cognitive_offloading_external_memory_and_extended_cognition]].

Reminder tốt cần xuất hiện gần ngữ cảnh (context / 맥락) có thể hành động. Reminder lúc 9 giờ sáng về việc chỉ có thể làm lúc tối có thể tạo acknowledgment nhưng không tạo completion.

## Hiện thực (implementation / 구현) intention

**Ý định thực thi (implementation intention)** có dạng `Nếu X xảy ra, tôi sẽ làm Y`. Nó liên kết cue cụ thể với hành động (action / 동작) cụ thể.

Ví dụ “sau khi đánh răng tối, tôi sẽ mở Anki 10 phút” thường mạnh hơn goal mơ hồ “tối nay học”. hiện thực (implementation / 구현) intention không bảo đảm success nếu tải công việc (workload / 워크로드) quá cao, nhưng nó giảm ambiguity ở moment of hành động (action / 동작).

## Planning fallacy

**Ngụy biện lập kế hoạch (planning fallacy)** là xu hướng underestimate thời gian hoàn thành tác vụ (task / 작업), đặc biệt khi dựa quá nhiều vào ideal scenario và bỏ qua cơ sở (base / 기반) tỷ lệ (rate / 비율) của tác vụ (task / 작업) tương tự.

Kỹ thuật hữu ích là **outside view**: trước khi estimate, xem những tác vụ (task / 작업) gần giống trước đây mất bao lâu. Trong software development, historical lead thời gian (time / 시간) thường đáng tin hơn cảm giác “lần này chắc nhanh”.

## Temporal discounting

Reward xa thường bị discount. Khi future benefit mờ còn present chi phí (cost / 비용) rõ, ta dễ chọn option immediate.

Technical debt, saving, exercise và study đều có cấu trúc này. `Không refactor hôm nay` cho reward ngay là tiết kiệm thời gian; chi phí (cost / 비용) xuất hiện tháng sau và vì xa nên bị underweight.

Precommitment và môi trường (environment / 환경) thiết kế (design / 설계) giúp bằng cách thay quyết định (decision / 결정) kiến trúc (architecture / 아키텍처) trước khi temptation xuất hiện.

## Procrastination

Procrastination không chỉ là time-management thất bại (failure / 실패). Nó thường là **emotion regulation ngắn hạn**: tác vụ (task / 작업) tạo boredom, bất định (uncertainty / 불확실성), threat hoặc shame; avoidance làm distress giảm ngay, nên avoidance được negative reinforcement.

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

Intervention tốt có thể giảm activation năng lượng (energy / 에너지), chia next hành động (action / 동작) nhỏ, tạo cue rõ và chấp nhận discomfort thay vì đợi motivation hoàn hảo.

## Deadline và Parkinson-like effects

Deadline tạo ràng buộc (constraint / 제약조건) giúp prioritize, nhưng deadline quá gần có thể tăng rushed lỗi (error / 오류); quá xa có thể làm tác vụ (task / 작업) thiếu urgency.

Một dự án (project / 프로젝트) dài thường tốt hơn khi có intermediate milestone tạo phản hồi (feedback / 피드백) thật, không chỉ chia ngày cho đẹp.

## Thời gian (time / 시간) estimation trong kiến thức (knowledge / 지식) công việc (work / 작업)

Kiến thức (knowledge / 지식) công việc (work / 작업) có variance lớn vì hidden phụ thuộc (dependency / 의존성), interruption và rework. điểm (point / 지점) estimate kiểu “3 ngày” dễ tạo false precision.

Phạm vi (range / 범위) estimate và tường minh (explicit / 명시적) giả định (assumption / 가정) tốt hơn: “2–4 ngày nếu API ổn định; thêm 1–2 ngày nếu phải migrate lược đồ (schema / 스키마)”. Điều này kết nối với [[08_decision_under_risk_uncertainty_and_ambiguity]].

## Future self

Con người đôi khi đối xử future self như một người khác: present self hưởng reward, future self trả chi phí (cost / 비용). Tăng psychological continuity với future self có thể làm long-term choice salient hơn, nhưng không thay thế ràng buộc (constraint / 제약조건) vật chất.

## Episodic future thinking

**Mô phỏng tương lai theo tình tiết (episodic future thinking)** là tưởng tượng sự kiện (event / 이벤트) tương lai cụ thể với ngữ cảnh (context / 맥락) chi tiết. Nó có thể làm delayed kết quả (outcome / 결과) bớt abstract và hỗ trợ planning trong một số tình huống.

Nhưng future simulation cũng chịu độ lệch (bias / 편향) từ hiện tại (current / 현재) mood và autobiographical bộ nhớ (memory / 메모리). Xem [[11_emotion_memory_and_affective_cognition]].

## Những hiểu lầm phổ biến

**“Người hay trễ giờ không tôn trọng người khác.”** Có thể đúng trong một số trường hợp (case / 사례), nhưng thời gian (time / 시간) perception, planning fallacy, executive hàm (function / 함수) và tải công việc (workload / 워크로드) cũng ảnh hưởng.

**“Procrastination chỉ là lười.”** Nó thường liên quan avoidance và emotion regulation.

**“Muốn nhớ việc chỉ cần cố nhớ hơn.”** bên ngoài (external / 외부) reminder thường đáng tin hơn pure intention.

**“Estimate tốt là đưa ra một con số chính xác.”** Với bất định (uncertainty / 불확실성) cao, phạm vi (range / 범위) và giả định (assumption / 가정) thường trung thực hơn.

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

> Quản lý thời gian hiệu quả không chỉ là chia lịch; đó là thiết kế cue, future reward, bất định (uncertainty / 불확실성) và emotion quanh hành động.

## Kết nối kiến thức

Xem [[08_decision_under_risk_uncertainty_and_ambiguity]], [[10_cognitive_offloading_external_memory_and_extended_cognition]], [[11_emotion_memory_and_affective_cognition]], [[../06_applied/01_education_learning_and_habit_design]] và [[../06_applied/12_psychology_in_daily_life_and_self_regulation]].

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 learning and conditioning](./00_learning_and_conditioning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
