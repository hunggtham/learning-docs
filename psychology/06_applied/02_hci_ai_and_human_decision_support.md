# HCI, AI và hỗ trợ ra quyết định của con người

Khi xây phần mềm, ta không chỉ thiết kế giao diện. Ta đang thiết kế một **môi trường nhận thức (cognitive environment)**: hệ thống quyết định thông tin nào nổi bật, lúc nào người dùng bị ngắt quãng, error được trình bày ra sao, lựa chọn mặc định là gì và người dùng phải nhớ bao nhiêu thứ trong đầu.

Vì vậy, HCI (Human–Computer Interaction / tương tác người–máy) là điểm gặp tự nhiên giữa psychology, computer science và design.

## Working memory là tài nguyên hữu hạn

Nếu UI yêu cầu người dùng nhớ ID từ màn hình trước, đối chiếu nhiều field và giữ rule nghiệp vụ trong đầu, ta đã chuyển cost từ system sang working memory của user.

Một nguyên tắc hữu ích là **recognition over recall**: khi có thể, hãy để system hiển thị option/context thay vì bắt user nhớ chính xác.

Ví dụ:

- dropdown có label rõ tốt hơn bắt nhớ code;
- inline validation tốt hơn báo lỗi tổng quát ở cuối form;
- breadcrumb tốt hơn bắt user nhớ mình đang ở tầng navigation nào.

Xem thêm: [[../02_learning_and_cognition/01_memory]], [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]].

## Cognitive load không phải cứ “ít element” là tốt

Tải nhận thức (cognitive load) phụ thuộc vào task, expertise và information structure. Một screen nhiều thông tin nhưng được chunk tốt có thể dễ hơn screen tối giản buộc user mở nhiều popup.

Đặc biệt với enterprise software, mục tiêu không phải “trông tối giản” mà là **giảm unnecessary mental transformation**.

## Attention là hệ thống cạnh tranh ưu tiên

Notification, animation, color contrast và motion đều cạnh tranh attention. Nếu mọi thứ đều nổi bật thì không còn hierarchy.

UI nên dùng salience tương ứng với decision importance. Một destructive action cần nổi bật theo cách khác một informational badge.

Attention capture cũng có cost sau khi interruption kết thúc: người dùng phải tái dựng task state. Với developer hoặc analyst, frequent context switching có thể gây mất nhiều thời gian hơn bản thân interruption.

Xem thêm: [[../01_brain_and_mind/07_attention_consciousness_and_awareness]], [[./00_work_organization_and_leadership]].

## Error là interaction giữa người và system

Human error thường bị giải thích bằng “user bất cẩn”. Human factors đặt câu hỏi khác: **system đã tạo điều kiện gì khiến error dễ xảy ra?**

Có thể phân biệt:

- slip: intention đúng nhưng action sai;
- mistake: model/decision sai;
- mode error: user nghĩ system đang ở state khác;
- confirmation error: feedback không đủ để user nhận ra action đã xảy ra.

Thiết kế tốt không chỉ prevent error mà còn hỗ trợ **recovery**: undo, clear status, reversible action và meaningful error message.

## Mental model và system model

Người dùng không nhìn thấy database, state machine hay backend workflow. Họ xây một **mental model** dựa trên những gì UI cho thấy.

Nếu UI hiển thị một button “Save” nhưng thực tế action chỉ lưu draft local, mental model sẽ sai. Bug usability đôi khi không nằm ở chức năng mà nằm ở mapping giữa interface và underlying state.

## Affordance và feedback

**Affordance** liên quan tới việc object gợi ý action nào có thể thực hiện. Trong digital UI, nhiều affordance là learned convention: button trông có thể click, link có style nhất quán.

**Feedback** trả lời “action vừa rồi có tác dụng gì?”. Latency không có feedback khiến user click lặp, submit nhiều lần hoặc nghĩ system treo.

## Default và choice architecture

Default có influence mạnh vì giảm effort và đôi khi được hiểu như recommendation. Vì vậy default không trung tính hoàn toàn.

Trong enterprise workflow, default có thể tăng efficiency nhưng cũng tạo automation-like bias: user ít xem lại field đã được system prefill.

Xem thêm: [[../02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity]], [[../02_learning_and_cognition/02_thinking_language_and_decision]].

## AI thay đổi vai trò của interface

Với AI system, user không chỉ thao tác button; họ phải đánh giá output có đáng tin hay không. Đây là vấn đề **calibration**, không phải chỉ UX.

Hai failure mode đối lập:

- **automation bias**: tin output quá mức vì “máy đã tính”;
- **algorithm aversion**: mất trust hoàn toàn sau một lỗi dù system trung bình vẫn hữu ích.

Mục tiêu là **sự phụ thuộc phù hợp (appropriate reliance)**: dùng AI khi comparative advantage của nó cao và kiểm tra mạnh hơn khi uncertainty/risk cao.

## Explainability không tự động tạo trust tốt

Một explanation trông hợp lý có thể làm user overtrust system ngay cả khi explanation không phản ánh actual computation. Vì vậy cần phân biệt:

- explanation để giúp debugging;
- explanation để support decision;
- confidence/uncertainty communication;
- provenance/source visibility.

“AI giải thích được” không đồng nghĩa “AI đúng”.

## Verification debt

Khi AI giúp tạo code, text hoặc analysis rất nhanh, output volume có thể tăng nhanh hơn capacity để review. Khoảng chênh này có thể gọi là **nợ kiểm chứng (verification debt)**.

Ví dụ developer generate 500 dòng code trong vài phút nhưng không hiểu invariant, dependency và failure mode. Productivity tức thời tăng nhưng future debugging cost cũng tăng.

Cách giảm verification debt:

- chia generation thành unit nhỏ;
- yêu cầu test/assumption rõ;
- review diff thay vì chỉ nhìn final output;
- tự giải thích lại logic;
- giữ human checkpoint cho high-risk action.

## Cognitive offloading: AI là công cụ hay phần thay thế kỹ năng?

Cognitive offloading có thể hữu ích. Calculator giúp ta không cần giữ arithmetic intermediate state; IDE autocomplete giảm recall burden; AI có thể giảm search/synthesis cost.

Vấn đề xuất hiện khi **performance goal** và **learning goal** bị nhầm.

Nếu mục tiêu là ship một task đã hiểu rõ, offloading có thể tốt. Nếu mục tiêu là học Java Streams, để AI viết toàn bộ pipeline mà không reconstruct logic có thể làm giảm encoding và retrieval practice.

Mental model:

> Offload storage/computation khi phù hợp, nhưng đừng offload phần reasoning mà bạn đang cố học.

## Human-in-the-loop thực sự nghĩa gì?

Chỉ có một người bấm “Approve” cuối pipeline không đảm bảo meaningful oversight. Human-in-the-loop cần:

- người review có đủ information;
- có authority để reject;
- workload không quá lớn;
- failure consequence được hiểu;
- system không tạo pressure khiến approve trở thành default.

Nếu 99.9% suggestion đúng, vigilance của reviewer có thể giảm; đây là automation complacency problem.

## AI anthropomorphism

Ngôn ngữ tự nhiên khiến con người dễ gán intention, understanding hoặc confidence cho model. Một câu trả lời trôi chảy có thể tạo **fluency heuristic**: dễ đọc → có vẻ đúng.

Cần tách:

- linguistic fluency;
- factual accuracy;
- reasoning validity;
- source quality;
- uncertainty.

Xem thêm: [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]], [[./17_misinformation_belief_revision_and_inoculation]].

## Ví dụ: AI code assistant

Một workflow tốt hơn “prompt rồi copy”:

```text
1. Người dùng xác định requirement và invariant.
2. AI đề xuất implementation nhỏ.
3. Người dùng đọc diff và giải thích logic.
4. Test tự động kiểm tra behavior.
5. Người dùng review edge case/security.
6. Chỉ sau đó mới mở rộng sang phần tiếp theo.
```

Ở đây AI làm giảm production cost nhưng human vẫn giữ model của system.

## Common Misconceptions

**“UX chỉ là làm đẹp.”** UX bao gồm cognitive load, error, decision, navigation, accessibility và feedback.

**“AI càng chính xác thì con người càng ít cần review.”** Review strategy phụ thuộc cả accuracy, uncertainty, consequence và detectability của error.

**“Có confidence score là giải quyết trust.”** User cần hiểu score đại diện gì và có calibrated hay không.

**“Dùng AI sẽ chắc chắn làm con người ngu đi.”** Quá đơn giản. Outcome phụ thuộc phần nào được offload, task goal và cách người dùng vẫn thực hành retrieval/reasoning.

## Mental Model

Một interactive system tốt không cố làm user “ghi nhớ cách dùng”. Nó **phân bố cognition** hợp lý giữa người, interface, automation và environment.

Câu hỏi thiết kế trung tâm:

> Phần nào con người nên quyết định, phần nào máy nên tính, và thông tin nào cần hiện ra để hai bên phối hợp đúng?

## Connections

Xem thêm:

- [[../02_learning_and_cognition/01_memory]];
- [[../02_learning_and_cognition/04_cognitive_biases_and_metacognition]];
- [[../02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity]];
- [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]];
- [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]];
- [[../90_connections/03_risk_uncertainty_and_science_communication]].