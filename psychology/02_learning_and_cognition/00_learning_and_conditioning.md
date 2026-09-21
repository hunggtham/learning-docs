# Học tập và điều kiện hóa — Learning & Conditioning / 학습과 조건형성

Learning là thay đổi tương đối bền trong behavior hoặc knowledge do experience. Nếu behavior đổi chỉ vì fatigue, drug hay maturation, ta không nhất thiết gọi đó là learning. tâm lý học (psychology) có nhiều cơ chế learning; conditioning là nền quan trọng nhưng không phải toàn bộ.

## điều kiện hóa cổ điển (classical conditioning): học quan hệ dự báo

Trong **điều kiện hóa cổ điển (điều kiện hóa cổ điển / 고전적 조건형성)**, một cue ban đầu trung tính trở nên có khả năng gợi response sau khi dự báo một event quan trọng. Cách hiểu hiện đại tốt hơn “ghép kích thích” là **predictive learning**. Nếu cue không cung cấp information mới vì event đã được dự báo hoàn hảo bởi cue khác, learning có thể yếu — phenomenon blocking cho thấy association phụ thuộc sai số dự đoán (prediction error).

Extinction không đơn giản xóa association cũ. Organism học một relation mới “cue không còn dẫn tới outcome trong context này”, nên response có thể quay lại qua renewal hoặc spontaneous recovery. Đây là lý do fear phơi nhiễm (exposure) cần generalization across contexts.

## điều kiện hóa thao tác (operant conditioning): hành vi thay đổi theo consequence

**điều kiện hóa thao tác (điều kiện hóa thao tác / 조작적 조건형성)** mô tả cách consequence thay đổi future probability của behavior. **Reinforcement** làm behavior tăng; **punishment** làm behavior giảm. Positive/negative chỉ nghĩa add/remove stimulus, không phải tốt/xấu.

củng cố âm tính (negative reinforcement) thường bị nhầm với punishment. Nếu đóng cửa để tiếng ồn biến mất và lần sau bạn đóng cửa nhanh hơn, removal của tiếng ồn đã reinforce hành vi đóng cửa. Trong avoidance lo âu (anxiety), việc né tình huống làm discomfort giảm ngay, nên avoidance được reinforced dù về dài hạn duy trì fear.

## Schedules và habit persistence

Variable-ratio schedules có thể tạo response bền vì reward unpredictable; slot machines là ví dụ kinh điển. Trong digital products, notification và intermittent social rewards có thể tạo checking behavior tương tự, dù human behavior còn chịu goals, social meaning và design context.

## Observational learning và model-based learning

Con người học bằng quan sát người khác, instruction và mô hình tư duy (mental model), không cần trực tiếp nhận mọi consequence. **Observational learning** phụ thuộc attention, memory, ability và motivation. học tập xã hội (social learning) giải thích vì sao norms lan truyền và vì sao role model có thể thay đổi behavior.

## Connection với học tăng cường (reinforcement learning) trong AI

RL dùng reward signal để update policy/value. Connection với điều kiện hóa thao tác hữu ích ở mức abstract: action–consequence–updating. Nhưng human reward không phải scalar đơn giản; động lực nội tại (intrinsic motivation), social value, model-based planning và language làm hệ thống giàu hơn.


## Learning là thay đổi system do experience

Trong tâm lý học, **learning (học tập / 학습)** rộng hơn classroom study. Nó là relatively persistent change trong behavior, knowledge hoặc response tendency do experience. Fatigue làm performance giảm tạm thời không phải learning; maturation thuần biological cũng khác learning, dù real development often interacts with experience.

## điều kiện hóa cổ điển: học relation giữa events

Pavlovian conditioning không chỉ là “nghe chuông chảy nước bọt”. Organism học predictive relation. **Conditioned stimulus — CS** có information về **unconditioned stimulus — US**. Strength learning phụ thuộc contingency và surprise, không chỉ số lần pair.

Rescorla–Wagner style models formalize sai số dự đoán:

\[
\Delta V = \alpha\beta(\lambda - V)
\]

Learning change lớn khi outcome surprising (`λ - V` lớn), nhỏ khi fully predicted. Đây là connection quan trọng với học tăng cường in AI.

## Extinction không phải erase

Khi CS xuất hiện repeatedly without US, conditioned response giảm. Nhưng spontaneous recovery, renewal và reinstatement cho thấy original association may remain. Extinction thường được understood as new inhibitory/contextual learning.

Điều này explain why fear có thể return after successful phơi nhiễm nếu context changes.

## điều kiện hóa thao tác: consequences shape action

**điều kiện hóa thao tác (조작적 조건형성)** tập trung relation giữa behavior và consequence. **củng cố tích cực (positive reinforcement)** thêm stimulus làm behavior tăng; **củng cố âm tính** remove aversive stimulus làm behavior tăng. “Negative” nghĩa subtract, không nghĩa punishment.

Nếu employee avoid difficult meeting và lo âu giảm ngay, avoidance được negatively reinforced. Đây là central mechanism trong lo âu maintenance.

## Punishment và side effects

Punishment decreases behavior but may not teach desired alternative. It can also create avoidance of punisher/context. Effective thay đổi hành vi (behavior change) often reinforces replacement behavior Thay vì only suppressing error.

## Reinforcement schedules

Củng cố liên tục thường hữu ích khi mới hình thành hành vi, còn lịch củng cố gián đoạn có thể duy trì hành vi bền hơn trước dập tắt. Lịch tỷ lệ biến đổi (variable-ratio schedule) liên quan đến phản ứng dai dẳng trong các hệ thống giống cờ bạc, dù cờ bạc thực tế còn có nhận thức và sự không chắc chắn của phần thưởng ngoài mô hình sách giáo khoa.

## Shaping và chaining

Hành vi phức tạp có thể được xây dựng bằng cách củng cố dần các xấp xỉ liên tiếp (**shaping**) hoặc nối nhiều hành vi thành chuỗi (**chaining**). Huấn luyện kỹ năng trong thể thao hay lập trình cũng dựa vào phân rã nhiệm vụ và phản hồi, dù nhận thức có ý thức của con người tạo thêm nhiều tầng phức tạp.

## Observational learning

Bandura showed people learn from models without direct reinforcement. Attention, retention, reproduction và motivation affect imitation. mạng xã hội (social media) massively expands models people observe, including rewarded risky behavior.

## Latent learning và cognitive maps

Công trình của Tolman thách thức quan điểm kích thích–phản ứng đơn giản bằng cách cho thấy sinh vật có thể hình thành biểu diễn mà chưa cần củng cố tức thời. Việc học có thể đã xảy ra trước khi thành tích quan sát được bộc lộ nó.

Điều này báo trước sự phân biệt giữa **học tập (learning)** và **thành tích biểu hiện (performance)** được dùng trong khoa học giáo dục.

## học tăng cường in AI: similarity và difference

Học tăng cường trong AI dùng các thành phần như tác nhân, trạng thái, hành động, phần thưởng và cập nhật giá trị. Mô hình học tăng cường trong tâm lý học cũng dùng tín hiệu sai số dự đoán, nhưng hàm phần thưởng nhân tạo được thiết kế rõ ràng còn hệ phần thưởng của con người chứa giá trị sinh học, xã hội và biểu diễn phong phú hơn. Phép tương tự hữu ích nhưng không đồng nghĩa hai hệ có cơ chế giống hệt.

## những hiểu lầm phổ biến (common misconceptions)

### “củng cố âm tính = punishment”

No. củng cố âm tính increases behavior by removing something aversive.

### “Reward always improves motivation”

Tác động của phần thưởng phụ thuộc vào nhiệm vụ, kỳ vọng, quan hệ điều kiện và mức kiểm soát mà người thực hiện cảm nhận.

### “Conditioning means mindless reflex”

Kỳ vọng, biểu diễn nhận thức và bối cảnh đều ảnh hưởng đến quá trình điều kiện hóa ở con người.

## kết nối kiến thức (knowledge connection)

Learning mechanisms support [[01_memory]], [[../04_mental_health/02_anxiety_ocd_and_trauma]], [[../05_intervention/01_cbt_behavioral_and_third_wave]] và [[../06_applied/01_education_learning_and_habit_design]].

## sai số dự đoán: trái tim của learning hiện đại

điều kiện hóa cổ điển không chỉ là “ghép chuông với thức ăn”. Modern learning theory nhấn mạnh **sai số dự đoán (sai số dự đoán / 예측오차)**: learning mạnh khi outcome khác expectation. Nếu tone luôn đã được fully predicted bởi một cue khác, thêm tone mới có thể tạo ít learning—phenomenon gọi là **blocking**.

Rescorla–Wagner model formalize intuition này:

\[
\Delta V = \alpha\beta(\lambda - V)
\]

`V` là associative strength hiện tại; `λ - V` là sai số dự đoán; `α` và `β` phản ánh salience/learning-rate parameters. Formula không phải truth cuối cùng, nhưng nó giải thích tại sao surprise drives updating.

Connection với machine learning rất trực tiếp: model update parameters theo error giữa prediction và target. Brain reward learning cũng thường được mô hình bằng temporal-difference prediction errors.

## Extinction không phải xóa ký ức

Khi conditioned cue xuất hiện nhiều lần mà outcome không còn, response giảm. **Extinction** từng được hiểu như unlearning, nhưng phenomena như spontaneous recovery, renewal và reinstatement cho thấy original association có thể còn. Extinction tạo new learning `cue → no outcome` cạnh tranh với old memory.

Clinical implication rất quan trọng cho liệu pháp phơi nhiễm (exposure therapy): fear giảm trong clinic không guarantee fear memory bị xóa. Treatment cần generalize extinction across contexts và tolerate occasional return of fear without interpreting it as total failure.

## Generalization và discrimination

Learning thường generalize từ cue đã học sang stimuli tương tự. Nếu chó sợ một loại tiếng nổ sau traumatic event, fear có thể spread sang fireworks, motorcycle backfire hoặc door slam. **Stimulus discrimination** là học phân biệt cues nào thật sự predict outcome.

Overgeneralization có thể contribute lo âu. Nhưng generalization cũng adaptive: nếu learning chỉ apply exact stimulus đã gặp, organism phải học lại từ đầu mọi situation.

## Reinforcement schedules

Operant behavior phụ thuộc schedule. **Fixed ratio** reinforce sau số responses cố định; **variable ratio** sau số responses biến thiên; **fixed interval** và **variable interval** phụ thuộc time. Variable-ratio schedules thường tạo persistent responding vì mỗi response có possibility reward—một reason gambling mechanics mạnh.

Digital products có thể mimic intermittent reinforcement: notification hoặc social reward xuất hiện unpredictable. Tuy nhiên không nên claim mọi app “gây nghiện dopamine” chỉ vì variable reward; addiction diagnosis và mechanism phức tạp hơn.

## củng cố âm tính khác punishment

Đây là confusion kinh điển. **củng cố âm tính** tăng behavior vì remove aversive state. Uống thuốc giảm đau rồi lần sau dùng thuốc sớm hơn là behavior được reinforce bởi pain removal. **Punishment** giảm behavior.

Trong avoidance lo âu, leaving feared situation làm lo âu giảm ngay, vì vậy avoidance được negatively reinforced. Short-term relief maintain long-term fear vì person không học được rằng feared outcome có thể không xảy ra hoặc distress có thể giảm tự nhiên.

## Shaping và chaining

**Shaping** reinforce successive approximations toward complex behavior. **Chaining** liên kết sequence behaviors, mỗi step cue cho step tiếp. Hai techniques useful trong education, rehabilitation và skill training.

Nếu goal là gym 1 giờ nhưng person hiện không exercise, reinforcement plan có thể start 10-minute routine. Đây không phải “hạ tiêu chuẩn”; nó thay transition probability của behavior chain.

## Observational learning

Bandura cho thấy learning có thể xảy ra qua observing model, không cần direct reinforcement. Attention, retention, reproduction và motivation đều matter. Vicarious reward/punishment ảnh hưởng likelihood perform behavior.

mạng xã hội làm observational environment massive: users thấy curated outcomes của others, học norms và expectations. Nhưng observing success không reveal unseen failure tỷ lệ nền (base rate).

## bất lực học được (learned helplessness) và controllability

Classic animal studies gợi ý uncontrollable aversive events có thể impair later attempts escape. Human theory evolved toward beliefs về control và attribution. Modern interpretation thận trọng hơn simple `bị stress → helpless` story; controllability, predictability và individual history matter.

Sense of control là biến trung gian (mediator) quan trọng trong stress và trầm cảm (depression) but not sole cause.

## Habit và goal-directed behavior

Không phải mọi hành vi lặp lại đều là thói quen. **Hành động hướng mục tiêu (goal-directed action)** nhạy với giá trị hiện tại của kết quả, còn **thói quen (habit)** bị kích hoạt mạnh hơn bởi tín hiệu và bối cảnh, đồng thời ít nhạy hơn với việc giá trị kết quả thay đổi ngay lập tức. Khi lặp lại đủ nhiều, quyền kiểm soát có thể dịch chuyển từ hướng mục tiêu sang thói quen.

Habit change vì vậy cần modify cue và friction, không chỉ motivation. Move phone out of reach changes stimulus environment; deleting app adds response cost.

## Reinforcement không đồng nghĩa bribery

Reinforcement là functional relation: consequence làm behavior future tăng. Một reward intended để reinforce có thể fail nếu recipient không value it. Praise có thể reinforce one child nhưng embarrass another.

Extrinsic reward còn có thể alter động lực nội tại depending on perceived control và task meaning. Đây là reason applied behavior design phải test actual behavior, không assume consequence function.

## mô hình tư duy mở rộng

Learning có thể nén thành cycle:

```text
Prediction → action → outcome → prediction error
                     ↓
               update association/policy
                     ↓
          behavior under future cues
```

Conditioning không phải theory về “sinh vật máy móc”; nó là family mechanisms cho cách experience thay future behavior.
