# Học bền vững, quên và chuyển giao — Durable Learning, Forgetting & Transfer

Học tốt không chỉ là làm đúng ngay sau khi vừa đọc. Một hệ thống học đáng tin cần giữ được knowledge sau khoảng thời gian dài, truy xuất được khi không có cue giống hệt lúc học và **chuyển giao (transfer)** được sang problem mới.

## Performance hiện tại không bằng learning lâu dài

Một learner có thể làm bài rất tốt ngay sau khi xem đáp án vì thông tin còn active trong working memory. Performance cao tại thời điểm đó chưa chứng minh long-term learning.

Điều này tạo một nghịch lý: phương pháp khiến buổi học “dễ” và trôi chảy có thể cho cảm giác tiến bộ mạnh nhưng retention kém; ngược lại, một số difficulty hợp lý làm practice chậm hơn nhưng giúp retrieval lâu dài.

## Forgetting không chỉ là failure

Quên xảy ra vì memory trace thay đổi, retrieval cue yếu, interference và context mismatch. Nhưng forgetting cũng có vai trò adaptive: hệ thống memory không cần giữ mọi detail với priority bằng nhau.

Mục tiêu học không phải ngăn quên hoàn toàn mà thiết kế repeated retrieval để những representation quan trọng trở nên accessible qua nhiều context.

## Retrieval practice

**Luyện truy xuất (retrieval practice)** là cố gọi lại information từ memory thay vì chỉ reread. Khi tự trả lời câu hỏi rồi mới check answer, learner không chỉ test memory mà còn tạo thêm retrieval route.

Retrieval practice hiệu quả nhất khi có feedback. Nếu answer sai nhưng không được correction, learner có thể củng cố error hoặc giữ uncertainty.

Trong programming, tự implement API từ requirement rồi so sánh với reference thường tạo learning sâu hơn chỉ đọc solution nhiều lần.

## Spacing

**Lặp lại giãn cách (spacing)** phân bố practice qua thời gian. Nếu tất cả repetition diễn ra cùng session, learner hưởng lợi từ short-term accessibility và dễ overestimate mastery.

Spacing tạo partial forgetting giữa các lần học, buộc retrieval phải hoạt động lại. Khoảng cách tối ưu phụ thuộc retention interval: nếu cần nhớ nhiều tháng, lịch ôn thường nên giãn dần thay vì cram trước deadline.

## Interleaving

**Học xen kẽ (interleaving)** trộn các dạng problem hoặc category. Nó có thể làm accuracy trong practice thấp hơn blocked practice nhưng tăng khả năng nhận ra “đây là loại problem nào?” khi gặp case mới.

Ví dụ, làm 20 bài chỉ về JOIN giúp execution trơn tru nhưng không luyện lựa chọn giữa JOIN, subquery, window function hay aggregation. Interleaving thêm bước classification trước execution.

## Desirable difficulties

**Khó khăn có lợi (desirable difficulties)** là difficulty làm encoding/retrieval effortful hơn nhưng cải thiện long-term learning trong điều kiện phù hợp. Không phải difficulty nào cũng desirable.

Nếu task quá khó khiến learner không có representation nền để reason, difficulty chỉ tạo noise. Vì vậy challenge cần nằm trên nền knowledge đủ để feedback có ý nghĩa.

## Transfer

**Chuyển giao (transfer)** là dùng knowledge ở situation khác với lúc học. Near transfer xảy ra khi context tương tự; far transfer đòi hỏi nhận ra deep structure dưới surface khác.

Transfer khó vì learner thường encode cả solution cùng context. Nếu chỉ học formula trong một template, họ có thể không nhận ra formula đó khi wording thay đổi.

Muốn tăng transfer, nên học nhiều example có surface khác nhưng deep principle giống, đồng thời giải thích rõ `vì sao` chứ không chỉ `làm thế nào`.

## Analogical learning

So sánh hai case giúp trích xuất cấu trúc chung. Một developer hiểu transaction tốt hơn khi so sánh banking transfer, inventory reservation và distributed saga: surface khác nhưng đều xoay quanh consistency, partial failure và rollback/compensation.

Analogy hữu ích khi mapping đúng relation. Analogy sai có thể che mất boundary condition, vì vậy cần hỏi thêm: “điểm nào của hai case không tương ứng?”.

## Feedback

Feedback tốt trả lời ít nhất ba câu: hiện tại đang ở đâu, mục tiêu là gì, và bước tiếp theo nào có leverage cao nhất.

Feedback quá sớm có thể biến task thành copy. Feedback quá muộn có thể cho phép error pattern được lặp nhiều lần. Tần suất hợp lý phụ thuộc complexity và skill level.

## Metacognitive calibration

Learner thường dùng **cảm giác trôi chảy (fluency)** làm proxy cho mastery. Reread quen mắt tạo fluency nhưng không đảm bảo recall.

Calibration tốt hơn khi dùng prediction trước test: “nếu mai không nhìn note, mình trả lời được bao nhiêu?”. Sau đó so prediction với performance thật. Gap giữa hai số là dữ liệu để cải thiện metacognition.

Xem [[04_cognitive_biases_and_metacognition]].

## Sleep và consolidation

Sleep hỗ trợ nhiều quá trình consolidation, nhưng không nên biến thành claim đơn giản “ngủ là tự học”. Nếu encoding ban đầu yếu, sleep không thay thế practice.

Học gần bedtime cũng không tự động tốt hơn mọi schedule. Quan trọng là đủ sleep, tránh sleep deprivation và phân phối learning hợp lý.

Xem [[../01_brain_and_mind/08_sleep_circadian_and_recovery]].

## Knowledge graph và schema

Durable knowledge không phải tập fact độc lập. Khi concept được nối vào schema, retrieval có nhiều route hơn và reasoning linh hoạt hơn.

Đây là lý do một knowledge library nên có cross-reference thật sự theo mechanism, không chỉ link vì hai chapter dùng cùng keyword.

## Học với AI

AI có thể giảm search cost, tạo example và feedback nhanh. Nhưng nếu mọi generation, explanation và retrieval đều được outsource, learner có thể đạt task performance mà internal model vẫn yếu.

Một workflow tốt phân biệt hai mode: **production mode** dùng tool để làm việc nhanh; **learning mode** yêu cầu learner dự đoán, tự giải thích hoặc tự viết trước khi xem answer.

Xem [[10_cognitive_offloading_external_memory_and_extended_cognition]] và [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]].

## Những hiểu lầm phổ biến

**“Đọc lại nhiều lần là học.”** Rereading có thể hữu ích để exposure nhưng không thay retrieval.

**“Interleaving luôn tốt hơn blocked practice.”** Beginner đôi khi cần block ngắn để hình thành procedure trước khi trộn category.

**“Nếu practice khó thì chắc đang học tốt.”** Difficulty chỉ có lợi khi nó kích hoạt processing hữu ích.

**“Hiểu concept một lần là transfer được.”** Transfer thường cần nhiều context và explicit comparison.

## Mô hình tư duy

```text
encoding có ý nghĩa
      ↓
retrieval + feedback
      ↓
spacing qua thời gian
      ↓
variation / interleaving
      ↓
schema mạnh hơn
      ↓
transfer sang context mới
```

> Học bền vững được đo bằng khả năng truy xuất và vận dụng sau khi cue quen thuộc đã biến mất.

## Kết nối kiến thức

Xem [[00_learning_and_conditioning]], [[01_memory]], [[04_cognitive_biases_and_metacognition]], [[06_expertise_creativity_and_problem_solving]], [[10_cognitive_offloading_external_memory_and_extended_cognition]], [[../06_applied/01_education_learning_and_habit_design]] và [[../01_brain_and_mind/05_neuroplasticity_brain_change_and_learning]].
