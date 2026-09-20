# Formal models, reductions và computability

Ở foundation, computability trả lời câu hỏi “có algorithm tổng quát nào luôn giải được problem này hay không?”. Ở mức advanced, điều quan trọng hơn là **cách chứng minh một giới hạn** và cách chuyển giới hạn đã biết từ problem này sang problem khác.

## Model of computation là một hợp đồng reasoning

Một computation model xác định state nào tồn tại, operation nào được phép và một bước computation nghĩa là gì. Turing machine, lambda calculus, register machine và general-purpose programming languages có hình thức khác nhau nhưng nhiều model có cùng sức biểu đạt computability dưới các giả định chuẩn.

Điều này cho phép ta tách hai tầng: **expressive power** và **cost model**. Hai languages đều Turing-complete nhưng có thể khác rất xa về memory safety, performance model, concurrency semantics hay khả năng verification. Turing-equivalence không làm các implementation trở nên giống nhau.

## Mapping reduction như công cụ truyền độ khó

Giả sử problem `A` có thể transform thành problem `B` sao cho answer được bảo toàn. Nếu transformation đủ hiệu quả, solver cho `B` trở thành solver cho `A`. Vì vậy khi `A` đã biết là khó hoặc undecidable, reduction `A → B` có thể chứng minh `B` ít nhất khó tương đương theo loại reduction đó.

Sai lầm phổ biến là nhớ reduction như một “mũi tên độ khó” mà không kiểm tra semantic preservation. Một reduction đúng phải định nghĩa mapping trên mọi input hợp lệ và chứng minh quan hệ giữa answer của input gốc và answer của instance sau transform.

## Halting problem là nguồn reduction trung tâm

Halting Problem hỏi program `P` trên input `x` có terminate hay không. Khi muốn chứng minh một property khác undecidable, pattern thường là giả sử có decider cho property mới, rồi dùng nó để quyết định halting.

Ví dụ tưởng tượng một tool `AlwaysTerminatesAfterNetworkRead(program)` quyết định hoàn hảo liệu program sau lần đọc network đầu tiên có luôn terminate. Nếu ta có thể encode một arbitrary computation `P(x)` vào phần chương trình sau network read, tool đó có thể bị biến thành halting decider. Chi tiết proof phụ thuộc property cụ thể, nhưng mental model là: **nhúng computation chưa biết vào context mà property mới buộc phải tiết lộ answer**.

## Recognizable, decidable và complement

Một language decidable nếu có machine luôn halt và trả lời yes/no đúng. Recognizable yếu hơn: với member, machine eventually accept; với non-member, nó có thể reject hoặc chạy mãi.

Nếu một language và complement của nó đều recognizable, ta có thể chạy hai recognizers song song theo dovetailing; một bên cuối cùng accept, tạo decider. Đây là một bridge quan trọng giữa existence proof và execution strategy.

## Rice's theorem và static analysis

Rice's theorem nói, ở mức khái quát, mọi non-trivial semantic property của partial functions được tính bởi programs trong model đủ mạnh đều undecidable. Điều này không khiến static analysis “vô ích”. Nó giải thích tại sao analyzers thực tế phải chọn một trong các chiến lược: giới hạn language, giới hạn property, chấp nhận approximation, dùng annotations/contracts, hoặc cho phép false positive/false negative.

Abstract interpretation là ví dụ điển hình: thay vì execute trên state space thật vô hạn, analyzer chạy trên abstract domain nhỏ hơn và thiết kế transfer functions để bảo toàn guarantee cần thiết. Precision tăng thường kéo theo cost tăng; termination của analysis lại trở thành một engineering constraint.

## Computability khác complexity

Một problem decidable vẫn có thể không practical. Sau khi biết algorithm tồn tại, câu hỏi tiếp theo là lượng time/space cần thiết. Đây là nơi reductions tiếp tục được dùng trong complexity theory, nhưng loại reduction và resource bound trở nên quan trọng hơn.

Một proof undecidability nói không có algorithm tổng quát theo model. Một NP-hardness proof không nói problem “không giải được”; nó đặt problem vào quan hệ worst-case complexity với các problem khác.

## Khi nào formal limit hữu ích trong công việc?

Formal limits giúp tránh mục tiêu bất khả thi. Một “perfect bug detector cho mọi program”, “tool luôn biết request nào sẽ deadlock”, hay “analyzer luôn suy ra chính xác mọi runtime behavior” có thể đụng undecidability. Thiết kế tốt chuyển câu hỏi sang subset có cấu trúc: finite-state protocol, bounded model, restricted type/effect system, symbolic execution với cutoff, hoặc runtime monitoring.

## Mental Model

> Advanced computability không phải học thêm tên theorem. Nó là kỹ năng chọn model, định nghĩa property, xây reduction và phân biệt ba câu hỏi: **có giải được không, giải với resource nào, và implementation thực tế có đáng dùng không**.

## Kết nối

Đọc lại [Computability foundation](../../basic/00_computation_information/04_computability_and_limits.md), rồi nối sang [Complexity & reductions](../../basic/01_algorithms_data_structures/11_complexity_reductions_and_np.md) và phần advanced về language/runtime khi nghiên cứu static analysis hoặc verification.