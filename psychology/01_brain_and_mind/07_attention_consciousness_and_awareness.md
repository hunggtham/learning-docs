# Chú ý, kiểm soát nhận thức và giới hạn xử lý

Môi trường cung cấp nhiều tín hiệu hơn mức hệ thần kinh có thể xử lý sâu cùng lúc. **Chú ý (attention)** là tập hợp các cơ chế ưu tiên một số tín hiệu, mục tiêu hoặc biểu diễn để chúng có ảnh hưởng lớn hơn lên perception, memory và action. Chú ý không phải một “đèn pin” duy nhất và cũng không đồng nhất với ý thức.

> **Trạng thái bằng chứng tổng quát:** selective attention, orienting, sustained attention/vigilance, executive control, attentional capture và switching cost đều có nền thực nghiệm mạnh. Cách phân chia chúng thành network hoặc mechanism cụ thể là **current model**: hữu ích và có converging evidence nhưng không nên biến thành sơ đồ vùng não cố định một–một.

Phần theory of consciousness đã được tách riêng tại [[09_consciousness_theories_and_evidence]].

## 1. Chú ý là sự ưu tiên trong hệ có tài nguyên hữu hạn

Một stimulus có thể được sensory system xử lý sơ bộ mà không trở thành nội dung được ưu tiên đủ lâu cho reasoning hoặc report. Chú ý thay đổi **processing priority**, không đơn giản bật/tắt perception.

Trong công việc lập trình, một notification không chỉ “mất 10 giây”. Nó có thể làm working-memory state bị phân rã: file nào đang theo dõi, hypothesis lỗi nào đang test, invariant nào chưa kiểm tra. Chi phí thực tế vì vậy gồm cả **resumption cost** khi quay lại task.

Xem [[../02_learning_and_cognition/01_memory]].

## 2. Alerting, orienting và executive control

Một taxonomy có ảnh hưởng phân biệt ba function:

**Alerting** duy trì mức readiness để phản ứng. **Orienting** chuyển ưu tiên tới location hoặc source. **Executive control** xử lý conflict giữa response cạnh tranh và giữ behavior phù hợp goal.

Các function này có thể dissociate phần nào trong behavioral/neural studies, nhưng chúng tương tác và network boundaries không tuyệt đối. Meta-analysis và review gần đây vẫn dùng framework này như một cách tổ chức evidence chứ không như “ba module độc lập”.

## 3. Bottom-up, top-down và priority map

Một tín hiệu nổi bật có thể kéo attention **từ dưới lên (bottom-up)**; goal hiện tại tạo bias **từ trên xuống (top-down)**.

Cách nhìn hiện đại thường xem selection là competition giữa salience, task goal, reward history và learned relevance. Vì vậy một notification quen thuộc có thể capture attention không chỉ vì màu sắc mà còn vì history of reward.

Environment design có thể giảm competition bằng cách giảm cue thay vì yêu cầu inhibition lặp đi lặp lại.

## 4. Attentional capture không phải phản xạ bất biến

Stimulus đột ngột hoặc salient thường có khả năng capture attention, nhưng capture phụ thuộc current attentional set, expectation và task.

> **Evidence boundary:** nói “màu đỏ luôn chiếm chú ý” hay “notification chắc chắn phá focus” là quá mạnh. Effect phụ thuộc stimulus, goal, timing, habit và individual difference.

Trong HCI, design tốt không nên dựa vào giả định người dùng sẽ luôn thấy warning chỉ vì warning technically visible.

## 5. Sustained attention và vigilance

**Chú ý duy trì (sustained attention)** là khả năng giữ performance ổn định trong task kéo dài. **Vigilance decrement** mô tả việc detection hoặc response thường suy giảm theo thời gian trong một số monotonous monitoring tasks.

Lý do của decrement vẫn còn tranh luận. Resource-depletion accounts, underload/mind-wandering accounts và các model mới nhấn mạnh **strategic allocation of effort** đều đang được nghiên cứu.

> **Current theory:** không nên nói vigilance giảm chỉ vì “não hết năng lượng chú ý”. Motivation, expected value of effort, task demand, arousal và opportunity cost đều có thể tham gia.

Review 2024 về strategic allocation of vigilance nhấn mạnh việc phân bổ effort theo expected value hơn là một “bình tài nguyên” đơn giản (PMID: 39295156).

## 6. Attention fluctuation quan trọng hơn một score trung bình

Sustained attention không giảm tuyến tính đều. Performance có thể dao động theo từng moment. Reaction-time variability, omission error và neural/network dynamics giúp nghiên cứu lapse.

Điều này giải thích tại sao một người có thể “tập trung được 50 phút” nhưng vẫn có micro-lapse quan trọng trong task safety-critical.

Trong monitoring system, design cần hỗ trợ detection của rare event thay vì giả định operator sẽ giữ vigilance hoàn hảo hàng giờ.

## 7. Nghỉ giải lao và metacognition

Break có thể giúp một số sustained-attention task, nhưng “Pomodoro 25 phút” không phải law tâm lý học universal.

Evidence gần đây cho thấy người dùng đôi khi có thể sử dụng metacognitive signal để self-schedule break và cải thiện vigilance, nhưng optimal timing phụ thuộc task và person (PMID: 39250235).

Ứng dụng hợp lý là theo dõi performance/fatigue signal và điều chỉnh pacing, không thần thánh hóa một con số thời gian duy nhất.

## 8. Executive attention và cognitive control

**Kiểm soát nhận thức (cognitive control)** giúp duy trì goal, inhibit response không phù hợp, update working memory và chuyển rule khi context đổi.

Attention, working memory và executive function có overlap nhưng không phải cùng một construct. Review đa phương pháp cho thấy vừa có shared process vừa có dissociation (PMID: 36967445).

Vì vậy một task “executive function” đơn lẻ không nên được coi là direct meter của một năng lực duy nhất trong não.

## 9. Task switching và switch cost

Khi chuyển từ rule A sang rule B, response thường chậm hoặc error-prone hơn. **Switch cost** phản ánh ít nhất một phần việc reconfigure task set, resolve interference và retrieve rule phù hợp.

Preparation có thể giảm cost nhưng thường không loại hoàn toàn.

Trong software work, switching giữa code review, chat, debugging và documentation có thể tạo cost lớn vì mỗi task chứa context state rộng hơn laboratory task.

## 10. Multitasking: concurrency và switching phải tách nhau

Một số activity có thể song song nếu một component đã automatic hoặc sử dụng resource tương đối khác. Nhưng khi hai task cùng cần language, reasoning hoặc response selection, performance thường chịu interference.

Do đó câu “con người không thể multitask” cũng quá tuyệt đối. Câu chính xác hơn:

> nhiều **attention-demanding tasks** không thể được xử lý sâu hoàn toàn đồng thời mà không có cost; observed performance phụ thuộc automaticity, modality và task demand.

## 11. Interruption và resumption lag

Interruption tạo thêm problem: task chính bị suspend trong khi secondary task chiếm control. Khi quay lại, người dùng phải reconstruct “mình đang ở đâu”.

External cue, bookmark, TODO marker hoặc IDE state có thể đóng vai trò **cognitive offloading** để giảm resumption cost.

Xem [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]].

## 12. Mind wandering

**Mind wandering** là chuyển attention khỏi task hiện tại sang internally generated thought. Nó thường làm comprehension hoặc vigilance giảm khi task đòi external monitoring.

Nhưng mind wandering không phải luôn dysfunctional. Trong safe context, spontaneous thought có thể hỗ trợ future planning hoặc creative incubation.

Điểm quan trọng là task fit: cùng một internal thought hữu ích khi đi bộ có thể nguy hiểm khi lái xe.

## 13. Meta-awareness

**Meta-awareness** là nhận biết rằng trạng thái chú ý đã thay đổi. Một người có regulation tốt không phải người “không bao giờ phân tâm”, mà có thể detect lapse và reorient trước khi cost tăng lớn.

Meta-awareness nối attention với [[../02_learning_and_cognition/04_cognitive_biases_and_metacognition]].

## 14. Attentional blink

Khi hai target xuất hiện rất gần nhau trong rapid serial presentation, target thứ hai có thể bị miss. **Attentional blink** cho thấy selection có temporal bottleneck.

Mechanism chi tiết vẫn được model theo nhiều cách, nên phenomenon established hơn explanation duy nhất của phenomenon.

Ứng dụng HCI: alert quan trọng không nên xuất hiện thành chuỗi dày đặc khiến chúng cạnh tranh cùng temporal window.

## 15. Inattentional blindness và change blindness

Người tập trung vào task có thể bỏ qua stimulus rất rõ nhưng unexpected. **Inattentional blindness** không có nghĩa mắt không nhận photon; nó cho thấy conscious report phụ thuộc selection/task set.

**Change blindness** cho thấy visual representation không giữ mọi detail của scene ở mức có thể compare liên tục.

Hai phenomenon cảnh báo rằng “nó nằm trên màn hình” không đủ chứng minh user đã nhận biết.

## 16. Attention và consciousness không đồng nhất

Attention có thể modulate processing mà stimulus không nhất thiết đạt report có ý thức; ngược lại conscious content có thể được trải nghiệm với mức focal attention khác nhau.

No-report paradigms cố giảm confound do report, nhưng chính interpretation của chúng vẫn là active methodological debate.

Theory landscape được trình bày riêng tại [[09_consciousness_theories_and_evidence]].

## 17. Attention và neuroscience

Attention liên quan distributed systems hơn là một “attention center”. Dorsal/ventral frontoparietal systems, thalamic mechanisms, salience/default-mode interactions và neuromodulation đều được nghiên cứu.

> **Evidence boundary:** activation network là correlate/mechanism evidence ở một level; nó không tự giải thích subjective experience, motivation hoặc task context.

Review và meta-analytic work 2024 tiếp tục hỗ trợ việc phân biệt alerting/orienting/executive networks theo developmental và neural evidence (PMID: 38392175), đồng thời cho thấy network interaction thay đổi theo tuổi.

## 18. ADHD không phải “thiếu chú ý” đơn giản

ADHD liên quan heterogeneous differences trong attention regulation, executive function, arousal, motivation và development. Không có một single attention deficit hoặc một brain marker dùng như diagnostic test.

Review 2024 về ADHD neurobiology nhấn mạnh heterogeneity và multi-level mechanisms thay vì một deficit duy nhất.

Xem [[../04_mental_health/05_neurodevelopmental_adhd_autism]].

## 19. Meditation và attention training

Focused-attention meditation thường luyện cycle `focus → detect distraction → return`; open-monitoring nhấn nhận biết experience mà không giữ một target duy nhất.

Một số intervention cho effect trên attention/stress, nhưng effect size phụ thuộc population, control group, practice duration và expectation.

> **Boundary:** meditation không phải evidence cho claim “rewire não vĩnh viễn” hoặc universal productivity boost.

## 20. Everyday/work design

Thay vì chỉ dạy “hãy tập trung”, có thể thiết kế hệ thống:

```text
reduce unnecessary capture
→ preserve task context
→ batch interruptible work
→ externalize resumption cue
→ place breaks where performance actually drops
```

Đây là human-factors logic, không phải self-help slogan.

Xem [[../06_applied/02_hci_ai_and_human_decision_support]], [[../06_applied/00_work_organization_and_leadership]] và [[../06_applied/12_psychology_in_daily_life_and_self_regulation]].

## 21. Những hiểu lầm phổ biến

**“Attention là một tài nguyên đơn duy nhất.”** Quá đơn giản. Có nhiều function và model cạnh tranh về giới hạn của chúng.

**“Multitasking luôn bất khả thi.”** Quá tuyệt đối. Interference phụ thuộc task/resource/automaticity, nhưng concurrent demanding cognition thường có cost.

**“Vigilance giảm vì hết năng lượng tinh thần.”** Đây chỉ là một class theory; motivation/opportunity-cost models cũng có evidence.

**“ADHD = không thể chú ý.”** Sai. Attention regulation và task/context sensitivity phức tạp hơn.

**“Thấy stimulus = đã nhận biết stimulus.”** Không. Inattentional/change blindness cho thấy visibility không đảm bảo report/awareness.

## 22. Mô hình tư duy

```text
salience + goal + reward history + state
                    ↓
              priority selection
                    ↓
 perception / working memory / action
                    ↓
      performance + feedback + fatigue
                    ↓
          reallocation of attention
```

Chú ý là một hệ thống phân bổ ưu tiên động, không phải nút bật/tắt “focus”.

## Kết nối kiến thức

Đọc cùng [[01_sensation_and_perception]], [[09_consciousness_theories_and_evidence]], [[../02_learning_and_cognition/01_memory]], [[../02_learning_and_cognition/04_cognitive_biases_and_metacognition]], [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]], [[../06_applied/02_hci_ai_and_human_decision_support]] và [[../06_applied/00_work_organization_and_leadership]].