# Suy luận và lập luận trong Trí tuệ nhân tạo

Biểu diễn tri thức chỉ thật sự hữu ích khi hệ thống có thể tạo ra kết luận mới hoặc đưa ra quyết định dựa trên tri thức đã có. **Suy luận (inference / 추론)** là quá trình dẫn xuất thông tin từ các tiền đề theo một cơ chế xác định. **Lập luận (reasoning)** là khái niệm rộng hơn, bao gồm việc lựa chọn giả định, kết hợp bằng chứng, xử lý bất định, tìm kiếm chứng minh, suy luận về nguyên nhân và hành động, đồng thời đôi khi phải sửa lại niềm tin khi có thông tin mới.

Không tồn tại một “thuật toán lập luận” duy nhất dùng cho mọi bài toán. Diễn dịch (deduction), quy nạp (induction), suy đoán lời giải thích (abduction), suy luận mặc định (default reasoning) và suy luận xác suất (probabilistic inference) trả lời những câu hỏi khác nhau và có mức bảo đảm khác nhau.

Xem trước: [Logic mệnh đề](./01_propositional_logic.md) và [Logic vị từ bậc nhất](./02_first_order_logic.md).

## Suy luận diễn dịch

Suy luận diễn dịch (deduction) có dạng:

```text
Quy tắc tổng quát + sự kiện
        ↓
kết luận tất yếu
```

Ví dụ:

\[
\forall x\;Human(x)\rightarrow Mortal(x)
\]

\[
Human(Socrates)
\]

suy ra:

\[
Mortal(Socrates)
\]

Nếu tiền đề đúng và phép suy luận hợp lệ thì kết luận bắt buộc phải đúng. Đây là đặc điểm **bảo toàn chân lý (truth-preserving)** của suy luận diễn dịch so với ngữ nghĩa hình thức đã chọn.

## Suy luận quy nạp

Suy luận quy nạp (induction) đi theo hướng:

```text
các ví dụ đã quan sát
        ↓
mẫu hoặc giả thuyết tổng quát
```

Ví dụ, hệ thống quan sát nhiều giao dịch rồi học một bộ phân loại để dự đoán gian lận.

Kết luận quy nạp không được bảo đảm tuyệt đối. Một dữ liệu mới hoàn toàn có thể làm giả thuyết cũ trở nên sai. Phần lớn Machine Learning là quá trình quy nạp: từ một tập dữ liệu hữu hạn, hệ thống học một mô hình được kỳ vọng có khả năng khái quát hóa (generalization) sang dữ liệu chưa thấy.

Thống kê cung cấp khung lý thuyết để đánh giá mức bất định của quá trình này.

## Suy luận abduction

**Abduction** tìm một lời giải thích có khả năng hợp lý cho quan sát hiện tại.

```text
Quy tắc: Fire → Smoke
Quan sát: Smoke
Giả thuyết có thể: Fire
```

Kết luận “có lửa” không phải là diễn dịch hợp lệ vì khói có thể đến từ nhiều nguyên nhân khác.

Chẩn đoán y khoa thường mang tính abduction: từ triệu chứng suy ra một tập nguyên nhân có thể xảy ra. Sau đó xác suất, kiến thức nhân quả hoặc kiểm tra bổ sung được dùng để xếp hạng các giả thuyết.

## Diễn dịch, quy nạp và abduction phối hợp với nhau

Một chu trình nghiên cứu hoặc AI có thể diễn ra như sau:

```text
Abduction  → đề xuất lời giải thích hoặc mô hình
Induction  → học và khái quát hóa từ dữ liệu
Deduction  → suy ra hệ quả có thể kiểm tra
Quan sát   → so sánh với thực tế
```

Ba cơ chế này bổ sung cho nhau thay vì loại trừ nhau.

## Tính đúng đắn của hệ suy luận

Một thủ tục suy luận là **đúng đắn (soundness / 건전성)** nếu:

\[
KB\vdash\alpha\Rightarrow KB\models\alpha
\]

Nghĩa là bất kỳ kết luận nào hệ thống chứng minh được cũng phải thật sự được suy ra về mặt ngữ nghĩa từ cơ sở tri thức.

Một bộ chứng minh đúng đắn không tự tạo ra kết luận logic không hợp lệ so với hệ hình thức mà nó đang làm việc.

## Tính đầy đủ

Một thủ tục là **đầy đủ (completeness / 완전성)** nếu:

\[
KB\models\alpha\Rightarrow KB\vdash\alpha
\]

Tức là mọi hệ quả ngữ nghĩa đều có thể được chứng minh về nguyên tắc.

Tuy nhiên đúng đắn và đầy đủ không đồng nghĩa với nhanh. Việc tìm một chứng minh có thể cần không gian tìm kiếm khổng lồ hoặc thậm chí không kết thúc trong các hệ logic có tính biểu đạt cao.

## Tính đúng đắn và khả năng xử lý thực tế

Khi thiết kế hệ suy luận, cần cân bằng:

```text
tính biểu đạt
đúng đắn / đầy đủ
thời gian chạy
bộ nhớ
khả năng bảo trì
```

Một ngôn ngữ quy tắc bị giới hạn nhưng có hành vi suy luận dễ dự đoán đôi khi phù hợp với hệ thống sản xuất hơn FOL đầy đủ.

## Suy diễn tiến

Suy diễn tiến (forward chaining) là cách suy luận dựa trên dữ liệu:

```text
các sự kiện đã biết
    ↓
tìm quy tắc có tiền đề phù hợp
    ↓
thêm kết luận mới
    ↓
lặp lại
```

Ví dụ:

```text
Employee(Alice)
Employee(x) → HasBadge(x)
HasBadge(x) → CanEnterLobby(x)
```

Hệ thống có thể suy ra Alice có thẻ và được vào sảnh.

Suy diễn tiến phù hợp khi dữ liệu liên tục được bổ sung và hệ thống có nhiều loại truy vấn cần phục vụ.

## Suy diễn lùi

Suy diễn lùi (backward chaining) bắt đầu từ mục tiêu:

```text
truy vấn
 ↓
quy tắc nào có thể sinh kết luận này?
 ↓
chứng minh các tiền đề
 ↓
lặp đệ quy
```

Muốn chứng minh `CanEnterLobby(Alice)`, hệ thống có thể chuyển thành yêu cầu chứng minh `HasBadge(Alice)`, rồi tiếp tục chuyển thành `Employee(Alice)`.

Cách này hiệu quả khi truy vấn hẹp so với toàn bộ tập hệ quả có thể tạo ra.

## Ghi nhớ kết quả suy luận

Suy diễn lùi có thể phải giải lại cùng một mục tiêu con nhiều lần. Ta có thể lưu:

```text
mục tiêu con → đã chứng minh / thất bại / các câu trả lời
```

Kỹ thuật **tabling** trong lập trình logic tránh vòng lặp và lặp tính toán, đồng thời cải thiện tính đầy đủ trong một số loại chương trình.

Đây cũng chính là ý tưởng của lập trình động (dynamic programming): lưu lại bài toán con đã giải.

## Suy luận theo điểm cố định

Các hệ kiểu Datalog có thể áp dụng quy tắc cho tới khi không còn sự kiện mới.

Gọi phép biến đổi tri thức là:

\[
T(K)=K\cup\{\text{các hệ quả mới}\}
\]

Ta lặp:

\[
K_{i+1}=T(K_i)
\]

cho tới khi:

\[
K_{i+1}=K_i
\]

Trạng thái này được gọi là điểm cố định (fixed point). Điểm cố định nhỏ nhất là cơ sở ngữ nghĩa cho nhiều chương trình quy tắc dương và đệ quy.

## Xung đột giữa các quy tắc

Cơ sở quy tắc thực tế có thể sinh ra kết luận mâu thuẫn.

Ví dụ:

```text
PremiumCustomer(x) → Approve(x)
FraudFlag(x) → Reject(x)
```

Nếu Alice thỏa cả hai điều kiện, hệ thống cần chính sách xử lý xung đột, chẳng hạn ưu tiên quy tắc, ưu tiên quy tắc cụ thể hơn, chính sách từ chối có độ ưu tiên cao hơn, xét nguồn gốc tri thức hoặc dùng logic phi đơn điệu.

Chính sách này phải được mô tả rõ trong ngữ nghĩa hệ thống thay vì để hành vi phụ thuộc tình cờ vào thứ tự chạy.

## Suy luận đơn điệu

Trong logic đơn điệu (monotonic logic), nếu:

\[
KB\models\alpha
\]

thì khi thêm tiền đề mới, kết luận cũ vẫn giữ nguyên:

\[
KB\cup\{\beta\}\models\alpha
\]

Logic cổ điển là đơn điệu.

Tuy nhiên tri thức đời thực thường không như vậy.

## Suy luận phi đơn điệu

Giả sử:

```text
Bird(Tweety)
Normally Bird(x) → Flies(x)
```

Ta tạm suy ra `Flies(Tweety)`.

Sau đó có thêm:

```text
Penguin(Tweety)
Penguin(x) → ¬Flies(x)
```

Hệ thống phải rút lại kết luận mặc định trước đó.

Suy luận phi đơn điệu (non-monotonic reasoning) cho phép các kết luận được sửa đổi khi xuất hiện bằng chứng mới.

## Logic mặc định

Một quy tắc mặc định có ý nghĩa gần như:

```text
Nếu Bird(x), và chưa có bằng chứng cho thấy đây là trường hợp bất thường,
thì tạm giả định Flies(x).
```

Cơ chế này khác hoàn toàn với một phép kéo theo nghiêm ngặt trong FOL.

Nhiều quy tắc nghiệp vụ thực tế có bản chất mặc định; nếu mô hình hóa chúng như chân lý tuyệt đối sẽ tạo ra rất nhiều ngoại lệ khó quản lý.

## Circumscription

Circumscription là một cách hình thức hóa ý tưởng “chỉ coi những gì thật sự cần thiết là bất thường”.

Ví dụ:

```text
Bird(x) ∧ ¬Abnormal(x) → Flies(x)
```

Hệ thống cố giữ tập `Abnormal` nhỏ nhất nhưng vẫn nhất quán với tri thức hiện có.

Đây là một cách hình thức hóa trực giác “mọi thứ bình thường trừ khi có bằng chứng ngược lại”.

## Suy luận theo giả định thế giới đóng

Các hệ giống cơ sở dữ liệu đôi khi sử dụng quy tắc:

```text
không chứng minh được P → tạm coi ¬P
```

Cách này chỉ an toàn khi cơ sở tri thức được xem là đầy đủ đối với vị từ đang xét.

Ví dụ trong hồ sơ y tế, không có chẩn đoán không có nghĩa bệnh nhân chắc chắn không mắc bệnh. Vì vậy giả định thế giới đóng nên được áp dụng có chủ đích theo từng miền, không phải như một mặc định chung.

## Hệ duy trì chân lý

Khi dữ liệu hoặc quy tắc thay đổi, các kết luận đã dẫn xuất có thể phải bị thu hồi.

**Hệ duy trì chân lý (Truth Maintenance System)** lưu lại quan hệ phụ thuộc:

```text
Sự kiện A + Quy tắc R → Kết luận C
```

Nếu A bị xóa, C cũng có thể phải xóa nếu không còn một đường chứng minh khác.

Ý tưởng này rất gần với lineage và tính toán gia tăng trong các pipeline dữ liệu hiện đại.

## Giải thích kết luận

Suy luận ký hiệu có thể tạo ra một vết chứng minh thật sự:

```text
Alice được vào sảnh vì:
Employee(Alice)
Employee → HasBadge
HasBadge → CanEnterLobby
```

Loại giải thích này mạnh hơn một giải thích hậu nghiệm kiểu “feature importance”, vì nó chính là đường dẫn suy luận đã được dùng để tạo kết luận.

Tuy nhiên chất lượng giải thích vẫn phụ thuộc vào tính đúng đắn của các quy tắc và tiền đề ban đầu.

## Suy luận khi tri thức mâu thuẫn

Trong logic cổ điển, mâu thuẫn có thể dẫn tới hiện tượng “bùng nổ”, tức từ mâu thuẫn có thể suy ra bất kỳ mệnh đề nào.

**Logic cận nhất quán (paraconsistent logic)** cho phép tồn tại mâu thuẫn mà không làm toàn bộ hệ suy luận sụp đổ.

Trong hệ thống sản xuất, một cách thực dụng khác là giữ rõ nguồn gốc của từng sự kiện và không hợp nhất các nguồn xung đột thành một “sự thật duy nhất” không có provenance.

## Suy luận dưới bất định

Quy tắc nghiêm ngặt:

\[
Symptom(x)\rightarrow Disease(x)
\]

thường không phù hợp với y tế hoặc thế giới thực.

Suy luận xác suất sử dụng:

\[
P(Disease\mid Symptom)
\]

hoặc các mô hình như Bayesian Network và factor graph.

Khi đó bài toán chuyển từ “chứng minh đúng/sai” sang “tính mức tin cậy hậu nghiệm”.

Xem: [Suy luận xác suất](./04_probabilistic_reasoning.md).

## Suy luận nhân quả

Quan hệ thống kê thường được viết:

\[
P(Y\mid X)
\]

Suy luận nhân quả lại quan tâm tới can thiệp:

\[
P(Y\mid do(X=x))
\]

Quan sát rằng `X` và `Y` đi cùng nhau không giống với việc chủ động thay đổi `X` rồi xem `Y` thay đổi ra sao.

Một quy tắc `Rain→WetRoad` có thể mang hàm ý nhân quả trong mô hình, nhưng phép kéo theo logic tự nó không tạo ra ngữ nghĩa nhân quả. Mô hình nhân quả cấu trúc (Structural Causal Model) biểu diễn cơ chế này rõ hơn.

## Suy luận phản thực

Một câu hỏi phản thực (counterfactual) có dạng:

> Điều gì sẽ xảy ra nếu hành động A đã không được thực hiện?

Trả lời câu hỏi này cần một mô hình của thế giới thay thế nhưng vẫn chia sẻ các yếu tố nền với thế giới thực, chứ không chỉ cần xác suất có điều kiện thông thường.

Suy luận phản thực quan trọng trong giải thích, phân tích chính sách và gán công lao cho hành động (credit assignment).

## Lập luận dựa trên trường hợp

Thay vì học một bộ quy tắc tổng quát, hệ thống có thể truy xuất các trường hợp quá khứ tương tự rồi điều chỉnh lời giải:

```text
truy xuất trường hợp tương tự
→ tái sử dụng lời giải
→ điều chỉnh theo ngữ cảnh mới
→ lưu lại kinh nghiệm mới
```

Đây là tư tưởng của **Case-Based Reasoning**. Nó có nét gần với hệ truy xuất hiện đại, dù RAG thường truy xuất văn bản hoặc ngữ cảnh thay vì thực hiện đầy đủ cơ chế thích nghi trường hợp.

## Lập luận tương tự

Lập luận tương tự (analogical reasoning) ánh xạ cấu trúc quan hệ từ một miền nguồn sang miền đích.

Ví dụ có thể dùng dòng nước để giải thích dòng điện. Cách này hữu ích cho học tập và giải thích, nhưng sẽ gây sai nếu cấu trúc tương đồng chỉ đúng ở một số điểm rồi bị kéo quá xa.

LLM có khả năng sinh phép tương tự rất tốt về ngôn ngữ, nhưng các phép tương tự kỹ thuật vẫn cần kiểm chứng.

## Suy luận đời thường

Tri thức đời thường bao gồm mặc định, quy luật vật lý, kỳ vọng xã hội và tri thức theo thời gian.

Các thách thức chính là phạm vi cực rộng, nhiều ngoại lệ, phụ thuộc ngữ cảnh, rất nhiều giả định không được nói ra và tri thức luôn không đầy đủ.

Mã hóa toàn bộ bằng ký hiệu rất khó; mô hình thống kê thuần túy lại có thể thiếu nhất quán. Đây là lý do các hướng tiếp cận lai vẫn là một chủ đề nghiên cứu quan trọng.

## Suy luận nhiều bước như một bài toán tìm kiếm

Tìm chứng minh có thể được nhìn như tìm kiếm trên không gian trạng thái:

```text
trạng thái = các sự kiện hoặc mục tiêu hiện tại
toán tử    = quy tắc suy luận
trạng thái kế = kết luận hoặc mục tiêu con mới
mục tiêu   = chứng minh hoặc phản ví dụ
```

Các bộ chứng minh hiện đại thường sử dụng heuristic để ưu tiên mệnh đề hoặc nhánh có triển vọng.

Điều này nối biểu diễn tri thức quay lại với [Tìm kiếm heuristic](../02_search_reasoning_and_planning/02_heuristic_search.md).

## Độ phức tạp của tìm kiếm chứng minh

Ngay cả khi từng quy tắc suy luận rất đơn giản, số đường dẫn suy luận có thể tăng bùng nổ.

Một hệ suy luận thực tế thường cần chỉ mục, thứ tự quy tắc, loại bỏ mệnh đề dư thừa, ghi nhớ kết quả, cắt nhánh và heuristic.

Đúng về mặt hình thức không đồng nghĩa với khả thi về mặt tính toán.

## Cơ sở dữ liệu suy diễn

Datalog kết hợp sự kiện quan hệ với quy tắc cho phép truy vấn đệ quy.

Ví dụ tính quan hệ có thể đi tới:

```text
Reach(x,y) :- Edge(x,y).
Reach(x,z) :- Edge(x,y), Reach(y,z).
```

Các quy tắc này tính bao đóng bắc cầu (transitive closure) của đồ thị.

Cơ sở dữ liệu và logic có quan hệ rất sâu; ngay cả bộ tối ưu truy vấn cũng có thể được xem như một hệ lập kế hoạch trên nhiều phương án thực thi.

## Suy luận trong Knowledge Graph

Ví dụ quy tắc:

```text
parentOf(x,y) ∧ parentOf(y,z)
→ grandparentOf(x,z)
```

Hoặc suy luận ontology:

```text
Doctor subClassOf MedicalProfessional
Alice type Doctor
→ Alice type MedicalProfessional
```

Trong khi đó, mô hình embedding cho Knowledge Graph thường dự đoán cạnh còn thiếu bằng một điểm số thống kê. Một cơ chế tạo **hệ quả logic**, cơ chế kia tạo **mức khả tín dự đoán**. Hai kết quả không nên bị nhầm lẫn.

## Chứng minh định lý có hỗ trợ neural

Một mô hình neural có thể xếp hạng hoặc chọn bước chứng minh, trong khi kernel ký hiệu kiểm tra từng bước.

Kiến trúc này chia vai trò rõ ràng:

```text
neural  → heuristic linh hoạt trên không gian tìm kiếm lớn
symbolic → bảo đảm tính hợp lệ của bước chứng minh được chấp nhận
```

Đây là một mẫu thiết kế điển hình của AI neuro-symbolic.

## Lập luận LLM và kiểm chứng

Chuỗi lập luận do LLM sinh ra có thể trôi chảy nhưng vẫn sai.

Một kiến trúc đáng tin cậy hơn là tạo ra hiện vật trung gian có thể kiểm tra:

```text
LLM đề xuất SQL / code / proof / plan
      ↓
parser / type checker / solver kiểm tra hoặc thực thi
      ↓
phản hồi kết quả cho mô hình
      ↓
sửa lại nếu cần
```

Bộ kiểm chứng phải kiểm tra thuộc tính thực sự của miền bài toán, không chỉ kiểm tra câu chữ có vẻ hợp lý.

## Tự nhất quán

Một chiến lược ở thời điểm suy luận là sinh nhiều đường lập luận rồi chọn câu trả lời theo đa số hoặc theo một bộ chấm điểm.

Cách này có thể cải thiện một số nhiệm vụ về mặt thống kê, nhưng sự đồng thuận không phải là chứng minh. Nhiều mẫu có thể cùng mắc một lỗi hệ thống.

Tự nhất quán (self-consistency) là một chiến lược lấy mẫu, không phải bảo đảm nhất quán logic.

## Chain-of-thought và dẫn xuất hình thức

Lập luận bằng ngôn ngữ tự nhiên linh hoạt, dễ đọc nhưng mơ hồ và có thể bỏ qua bước.

Dẫn xuất hình thức có cú pháp chính xác và kiểm tra được, nhưng bị giới hạn trong miền đã mô hình hóa và có thể tốn chi phí xây dựng.

Một hệ thống hiện đại có thể dùng ngôn ngữ tự nhiên để đề xuất và biểu diễn hình thức để kiểm chứng.

## Nguồn gốc của vết suy luận

Trong AI doanh nghiệp, đầu ra có thể cần kèm theo:

```text
câu trả lời
nguồn hỗ trợ
quy tắc đã sử dụng
kết quả tính toán / công cụ
mức bất định
```

Cách này dễ kiểm toán hơn một câu trả lời cuối cùng không có dấu vết.

Thông tin nguồn gốc phải phản ánh quá trình thật sự, không phải một lời giải thích được tạo ra sau đó nhưng không liên quan tới cách kết luận được sinh ra.

## Mô hình tư duy

```text
Deduction     = tiền đề bảo đảm kết luận
Induction     = ví dụ gợi ra mẫu tổng quát
Abduction     = quan sát gợi ra lời giải thích
Default       = tạm giả định bình thường cho tới khi có ngoại lệ
Probabilistic = xếp hạng niềm tin dưới bất định
Causal        = suy luận về can thiệp
Search        = khám phá các đường dẫn chứng minh hoặc kế hoạch
Verification  = kiểm tra ứng viên bằng quy tắc rõ ràng
```

## Các hiểu lầm thường gặp

### “Lập luận chỉ là diễn dịch”

Không. AI thực tế còn dùng quy nạp, abduction, xác suất, nhân quả và lý thuyết quyết định.

### “Có chứng minh hình thức nghĩa là tiền đề cũng đúng”

Không. Chứng minh chỉ bảo đảm kết luận theo từ tiền đề; tính đúng của nguồn dữ liệu và mô hình hóa là vấn đề riêng.

### “Giải thích do LLM tạo ra là bằng chứng câu trả lời đúng”

Không. Lời giải thích có thể sai hoặc được tạo hậu nghiệm. Kiểm chứng độc lập vẫn cần thiết.

### “Càng nhiều quy tắc thì bộ suy luận càng mạnh”

Không nhất thiết. Thêm quy tắc có thể tạo mâu thuẫn, vòng lặp và bùng nổ không gian tìm kiếm. Chất lượng kỹ thuật tri thức quan trọng hơn số lượng.

## Liên kết kiến thức

Suy luận là nơi biểu diễn tri thức trở thành một hệ thống hoạt động. Nó nối Logic với Search, Xác suất, Suy luận nhân quả và các hệ LLM có công cụ hỗ trợ. Phần Agent sau này sẽ sử dụng lại đúng mẫu kiến trúc này: đề xuất → kiểm tra qua môi trường hoặc công cụ → cập nhật trạng thái → lập kế hoạch lại.

Xem tiếp: [Suy luận xác suất](./04_probabilistic_reasoning.md).