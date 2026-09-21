# AI ký hiệu và AI Neuro-Symbolic

Lịch sử AI đôi khi bị kể quá đơn giản theo kiểu: **AI ký hiệu thất bại → Machine Learning chiến thắng → Deep Learning thay thế mọi thứ trước đó**. Cách kể này không chính xác. Hệ ký hiệu và hệ neural có những điểm mạnh khác nhau; nhiều hệ thống đáng tin cậy hiện nay kết hợp mô hình học được với công cụ, ràng buộc, tìm kiếm, cơ sở dữ liệu và cơ chế kiểm chứng hình thức.

**AI ký hiệu (Symbolic AI / 기호주의 인공지능)** biểu diễn tri thức bằng ký hiệu, quy tắc và quan hệ có cấu trúc. **AI neural** học biểu diễn phân tán và hàm từ dữ liệu. **AI neuro-symbolic (Neuro-Symbolic AI / 신경-기호 인공지능)** là tên chung cho các hướng cố gắng kết hợp hai họ phương pháp này; nó không chỉ một kiến trúc duy nhất.

Xem trước: [Biểu diễn tri thức](./00_knowledge_representation.md), [Suy luận và lập luận](./03_inference_and_reasoning.md), và [Knowledge Graph](./06_knowledge_graphs.md).

## AI ký hiệu bắt đầu từ đâu?

Các hệ ký hiệu giả định rằng nhiều khía cạnh của trí tuệ có thể được mô hình hóa bằng:

```text
ký hiệu
+ quy tắc
+ tìm kiếm / suy luận
```

Ví dụ gồm bộ chứng minh định lý, expert system, planner kiểu STRIPS, SAT/SMT solver, rule engine và ontology reasoner.

Một ký hiệu như `Patient42`, vị từ `HasSymptom(x,Fever)` hoặc quy tắc `A∧B→C` có ý nghĩa được xác định rõ bởi người thiết kế và tri thức miền.

## Điểm mạnh của hệ ký hiệu

### Tính tường minh

Một quy tắc có thể đọc trực tiếp:

```text
HighRisk(x) ∧ MissingKYC(x) → ManualReview(x)
```

Người thiết kế biết rõ điều kiện nào dẫn tới kết luận nào.

### Khả năng kiểm chứng

Bộ chứng minh hình thức hoặc solver có thể xác nhận một ứng viên có thỏa các ràng buộc đã mô hình hóa hay không.

### Khả năng kết hợp cấu trúc

Ký hiệu và quan hệ có thể kết hợp theo quy tắc rõ ràng. Khi xuất hiện thực thể mới nhưng vẫn phù hợp schema, hệ thống có thể áp dụng quy tắc mà không cần huấn luyện lại.

### Hiệu quả dữ liệu

Nếu quy tắc miền đã biết, không cần hàng nghìn ví dụ để hệ thống tự phát hiện lại cùng quy tắc bằng thống kê.

## Điểm yếu của hệ ký hiệu

Một vấn đề kinh điển là **nút thắt thu thập tri thức (knowledge acquisition bottleneck)**: chuyên gia phải tự mã hóa số lượng rất lớn quy tắc và sự kiện.

Hệ ký hiệu cũng dễ giòn khi dữ liệu đầu vào không sạch. Ảnh, âm thanh và ngôn ngữ tự nhiên không xuất hiện sẵn dưới dạng ký hiệu hoàn hảo.

Ngoài ra, tri thức đời thường có quá nhiều ngoại lệ và phụ thuộc ngữ cảnh để có thể mã hóa toàn bộ bằng tay.

Những hạn chế này là một trong các động lực thúc đẩy Machine Learning và Deep Learning.

## Hệ neural bắt đầu từ việc học

Một mô hình neural có dạng:

\[
f_\theta(x)
\]

và học các tham số `θ` từ dữ liệu thông qua tối ưu hóa.

Thay vì thiết kế toàn bộ feature hoặc rule thủ công, mô hình có thể học biểu diễn trực tiếp từ dữ liệu.

Điểm mạnh của neural network là xử lý perception, ngôn ngữ, similarity, dữ liệu nhiều chiều và khả năng khái quát hóa từ lượng dữ liệu lớn.

Đổi lại, biểu diễn bên trong khó giải thích trực tiếp, việc bảo đảm ràng buộc cứng khó hơn, hành vi ngoài phân phối có thể không ổn định và tri thức cụ thể khó cập nhật chọn lọc trong trọng số.

## Không nên xem symbolic và neural như hai lựa chọn loại trừ nhau

Rất nhiều hệ thống hiện đại đã là hệ lai dù không tự gọi là “neuro-symbolic”.

Ví dụ search engine:

```text
neural embedding retrieval
+ bộ lọc Boolean
+ chỉ mục cơ sở dữ liệu
+ quy tắc xếp hạng
```

Ví dụ coding agent:

```text
LLM đề xuất code
+ compiler / type checker
+ test
+ shell / git tool
```

Compiler chính là một thành phần hình thức cung cấp phản hồi chính xác mà LLM không cần tự mô phỏng.

## Chọn cơ chế theo yêu cầu của từng thành phần

Thay vì hỏi “symbolic hay neural tốt hơn?”, nên hỏi thành phần nào cần tính chất nào.

| Nhu cầu | Cơ chế thường phù hợp |
|---|---|
| Hiểu pixel hoặc âm thanh thô | neural model |
| Tìm tương đồng ngữ nghĩa | embedding |
| Ràng buộc nghiệp vụ cứng | rule / solver |
| Tính toán số chính xác | calculator / runtime |
| Lưu trữ quan hệ tường minh | database / Knowledge Graph |
| Giao tiếp ngôn ngữ linh hoạt | LLM |
| Chứng minh hình thức | theorem prover |
| Lập kế hoạch tổ hợp | search / solver + heuristic học được |

Một kiến trúc tốt có thể kết hợp nhiều cơ chế thay vì buộc một mô hình duy nhất làm mọi việc.

## Neural perception rồi suy luận ký hiệu

Một mẫu kiến trúc cổ điển:

```text
ảnh
 ↓ neural detector
đối tượng + thuộc tính
 ↓ symbolic rules / planner
suy luận / hành động
```

Điểm yếu là lỗi perception sẽ trở thành ký hiệu sai. Bộ suy luận phía sau có thể hoàn toàn hợp logic nhưng đang suy luận trên dữ liệu đầu vào sai.

Vì vậy ranh giới giữa neural và symbolic nên truyền cả độ tin cậy hoặc mức bất định khi phù hợp.

## Cấu trúc ký hiệu hướng dẫn việc học neural

Quy tắc hoặc ràng buộc có thể được đưa vào hàm mất mát.

Ví dụ biết rằng:

\[
A(x)\rightarrow B(x)
\]

có thể thêm penalty khi dự đoán neural vi phạm quan hệ này.

Đây là **ràng buộc mềm (soft constraint)**. Nó làm vi phạm trở nên tốn kém nhưng không tạo bảo đảm tuyệt đối, trừ khi kết quả cuối cùng còn được kiểm tra bằng một cơ chế cứng khác.

## Logic khả vi

Một số phương pháp thay chân trị Boolean bằng giá trị liên tục `[0,1]` và thay toán tử logic bằng các hàm khả vi.

Ví dụ phép hội kiểu fuzzy có thể dùng:

\[
T(a,b)=ab
\]

hoặc một t-norm khác.

Khi đó mức thỏa logic có thể trở thành một phần của loss và huấn luyện bằng gradient.

Lợi ích là tích hợp trực tiếp với Deep Learning. Hạn chế là ngữ nghĩa chân trị đã trở thành xấp xỉ liên tục, không còn tương đương hoàn toàn với chứng minh logic cổ điển.

## Logic Tensor Network

Các hướng kiểu **Logic Tensor Network** ánh xạ vị từ thành hàm neural rồi biến công thức logic thành mục tiêu thỏa mãn khả vi.

Có thể hình dung:

```text
công thức ký hiệu
   ↓ relaxation khả vi
hàm mất mát
   ↓
tham số neural
```

Cách này đưa tri thức có cấu trúc vào quá trình học, nhưng không tự động kế thừa toàn bộ bảo đảm của theorem proving cổ điển.

## Chứng minh định lý có neural hỗ trợ

Mô hình học có thể giúp xếp hạng lemma hoặc tactic:

```text
trạng thái chứng minh hiện tại
 ↓ neural model xếp hạng bước tiếp theo
formal prover thực thi
 ↓
trạng thái chứng minh hợp lệ hoặc thất bại
```

Tính đúng đắn cuối cùng đến từ kernel hình thức; neural network chủ yếu cải thiện hiệu quả tìm kiếm.

Đây là một trong những kiến trúc neuro-symbolic rõ ràng nhất vì vai trò của hai phần được tách rất sạch.

## Heuristic học được kết hợp tìm kiếm ký hiệu

Thuật toán tìm kiếm có thể cần heuristic `h(s)` hoặc policy để ưu tiên hành động. Neural network dự đoán hành động hoặc giá trị có triển vọng, trong khi quy tắc chuyển trạng thái vẫn được kiểm tra chính xác.

Các hệ thống kiểu AlphaZero có thể nhìn như:

```text
neural policy / value
+ Monte Carlo Tree Search
+ luật trò chơi chính xác
```

Machine Learning không thay thế search; nó giúp search tập trung vào nhánh hứa hẹn hơn.

## LLM kết hợp SAT/SMT solver

Giả sử yêu cầu tự nhiên:

> Xếp lịch cho 5 nhân viên, không được trùng ca, Alice không làm thứ Ba...

Kiến trúc đáng tin cậy hơn là:

```text
ngôn ngữ tự nhiên
 ↓ LLM trích xuất biến / ràng buộc
SMT / CP-SAT model
 ↓ solver
assignment hợp lệ hoặc UNSAT
 ↓ LLM giải thích
```

Solver chỉ bảo đảm các ràng buộc đã được mã hóa. Điểm yếu nhất vẫn là bước chuyển từ ý định người dùng sang mô hình ràng buộc, vì vậy hệ thống nên hiển thị hoặc kiểm tra mô hình trung gian khi bài toán quan trọng.

## LLM kết hợp code execution

Với số học hoặc phân tích dữ liệu:

```text
câu hỏi
 ↓ LLM viết code / query
runtime thực thi
 ↓ kết quả thật
LLM diễn giải
```

Đây là một kiến trúc lai rất thực dụng. Khi có một executor xác định và chính xác, không cần yêu cầu LLM “tự đóng vai máy tính” trong trọng số.

## LLM kết hợp Knowledge Graph

LLM có thể phụ trách nhận diện thực thể, tạo query và diễn đạt kết quả; Knowledge Graph lưu tri thức quan hệ tường minh.

```text
câu hỏi người dùng
 ↓ phân tích ngữ nghĩa / entity linking
truy vấn graph có cấu trúc
 ↓ Knowledge Graph
facts + provenance
 ↓ LLM
câu trả lời
```

Cách này giúp tri thức có thể cập nhật độc lập khỏi model weights và dễ kiểm toán hơn.

Tuy nhiên graph có thể không đầy đủ; không được tự suy rằng “không có cạnh” nghĩa là “sai” nếu hệ thống không dùng closed-world semantics.

## RAG có phải Neuro-Symbolic AI không?

RAG kết hợp retrieval với generative model, nhưng gọi mọi hệ RAG là “neuro-symbolic” sẽ làm khái niệm trở nên quá rộng.

Vector RAG thông thường có thể không có suy luận ký hiệu nào. KG-RAG, solver-backed RAG hoặc RAG có rule engine rõ ràng mang tính lai hơn.

Nên mô tả chính xác kiến trúc thay vì chỉ dùng nhãn.

## Program synthesis kết hợp verification

Mô hình neural đề xuất chương trình, còn test, static analysis hoặc formal verifier kiểm tra.

```text
đề xuất
 ↓
thực thi / kiểm chứng
 ↓ lỗi hoặc phản ví dụ
sửa lại
 ↺
```

Phản ví dụ mang thông tin rất cao vì nó chỉ ra một điều kiện cụ thể khiến lời giải sai. Mẫu này rất quan trọng trong coding agent đáng tin cậy.

## Constraint decoding

Thay vì sinh token tự do rồi mới từ chối, decoder có thể ép đầu ra tuân theo grammar hoặc schema ngay trong quá trình sinh.

Ví dụ:

- JSON grammar;
- SQL grammar;
- finite-state constraint;
- regex hoặc CFG-guided decoding.

Cách này có thể bảo đảm **cú pháp**, nhưng không bảo đảm **ngữ nghĩa**.

Ví dụ `{"age": -500}` vẫn là JSON hợp lệ nhưng là giá trị sai về mặt miền dữ liệu.

## Tool có kiểu dữ liệu rõ ràng

Schema của function calling tạo ra một giao diện gần với biểu diễn ký hiệu:

```text
search(query: string, top_k: int)
transfer(amount: decimal, account_id: string)
```

Kiểu và schema làm giảm không gian hành động và cho phép kiểm tra đầu vào.

LLM lựa chọn công cụ và tham số; chính implementation của công cụ phải chịu trách nhiệm về permission, validation và side effect.

## Tách người đề xuất và bộ kiểm chứng

Một mẫu kiến trúc mạnh:

```text
Proposer
  linh hoạt / học được / sáng tạo
        ↓
Verifier
  nghiêm ngặt / xác định / hình thức
        ↓
Executor
        ↓
Feedback
```

Ví dụ:

- LLM ↔ compiler;
- planner ↔ constraint validator;
- theorem model ↔ proof kernel;
- code model ↔ test;
- extraction model ↔ schema validator.

Cách này tránh yêu cầu một mô hình duy nhất vừa sáng tạo vừa hoàn toàn chính xác.

## Kiểm chứng chỉ đúng so với specification

Một solver có thể chứng nhận:

```text
lịch thỏa toàn bộ ràng buộc đã mã hóa
```

nhưng không thể tự chứng nhận:

```text
các ràng buộc đã mã hóa phản ánh hoàn hảo ý định của con người
```

Khoảng cách này gọi là **specification gap**.

Formal verification chuyển phần lớn rủi ro từ “thực thi có đúng không?” sang “ta đã mô hình hóa đúng thứ cần kiểm tra chưa?”, chứ không làm biến mất mọi bất định.

## Ràng buộc mềm và ràng buộc cứng

Nếu thêm penalty vào loss:

\[
L=L_{task}+\lambda L_{constraint}
\]

thì hệ thống chỉ làm vi phạm trở nên tốn kém hơn.

Nếu dùng solver với ràng buộc:

\[
g(x)\le0
\]

thì lời giải vi phạm sẽ bị loại hoàn toàn.

Với invariant an toàn quan trọng, nếu có thể kiểm tra xác định thì không nên chỉ dựa vào penalty mềm trong quá trình huấn luyện.

## Representation learning theo hướng neuro-symbolic

Một số phương pháp học embedding nhưng vẫn tận dụng cấu trúc quan hệ đã biết.

Knowledge Graph embedding học vector từ triple; GNN truyền thông tin qua topology của graph.

Những hệ như vậy có thể được xem là lai theo nghĩa rộng, nhưng không nhất thiết đang thực hiện suy luận ký hiệu hình thức.

Vì vậy cần dùng thuật ngữ “neuro-symbolic” cẩn thận.

## Ẩn dụ System 1 / System 2

Đôi khi người ta ví neural model là “System 1” nhanh và trực giác, còn symbolic search là “System 2” chậm và có cấu trúc.

Ẩn dụ này có thể hữu ích để giải thích, nhưng không nên hiểu như một sự tương đương sinh học thật sự.

Trong kỹ thuật, nên mô tả cụ thể hơn: proposal network, search, verifier, memory và tool execution.

## Khi symbolic không phù hợp

Không nên ép mọi bài toán vào rule nếu ranh giới khái niệm mơ hồ, đầu vào nhiều chiều, quy tắc không thể liệt kê hết hoặc môi trường thay đổi nhanh.

Nhận diện vật thể từ pixel là ví dụ điển hình nơi Deep Learning hiệu quả hơn rất nhiều so với pipeline symbolic thủ công.

## Khi neural model không phù hợp

Không nên yêu cầu neural network một mình xử lý những việc đã có thuật toán xác định rõ như:

- tính thuế chính xác;
- kiểm tra quyền truy cập cứng;
- join cơ sở dữ liệu;
- kiểm tra chữ ký mật mã;
- proof checking;
- bảo đảm thỏa ràng buộc.

Nên dùng công cụ xác định cho phần đó và chỉ dùng LLM ở chỗ cần giao tiếp hoặc điều phối linh hoạt.

## Lỗi của hệ lai có thể cộng dồn

Một hệ lai có nhiều nguồn lỗi:

```text
lỗi semantic parsing
+ lỗi retrieval
+ lỗi giả định của solver / model
+ lỗi thực thi tool
+ lỗi diễn giải kết quả
```

Thêm verifier không bảo đảm toàn bộ pipeline đúng nếu upstream hoặc downstream xử lý sai thông tin.

Đánh giá cần có cả mức component và end-to-end.

## Thiết kế giao diện giữa neural và symbolic

Nếu có thể, nên truyền trạng thái có cấu trúc thay vì văn bản tự do.

Ví dụ tốt:

```json
{
  "customer_id": "C123",
  "risk_score": 0.82,
  "kyc_status": "MISSING"
}
```

Rule engine có thể xử lý dạng này ổn định hơn một câu mô tả tự nhiên phải phân tích lại ở mỗi bước.

## Confidence và khả năng từ chối

Nếu neural parser không chắc chắn, hệ thống có thể yêu cầu làm rõ thay vì đưa một biểu diễn đáng ngờ vào solver.

Một solver hoàn hảo vẫn có thể cho ra kết quả “rất chắc chắn nhưng sai” nếu input symbolic ban đầu được parse sai.

Vì vậy giao diện giữa hai phần phải nhận biết bất định.

## Cách đọc một nghiên cứu Neuro-Symbolic

Khi một bài nghiên cứu tuyên bố dùng neuro-symbolic, nên hỏi:

- tri thức ký hiệu nào được cung cấp;
- thành phần nào được học;
- phần nào có bảo đảm hình thức;
- logic là ràng buộc cứng hay relaxation khả vi;
- nhiễu được xử lý thế nào;
- khả năng compositional generalization có thật hay chỉ khớp benchmark.

Tên kiến trúc tự nó không nói lên chất lượng.

## Mô hình tư duy

```text
Symbolic AI
  fact / rule / constraint tường minh
  + search / inference chính xác

Neural AI
  biểu diễn phân tán học được
  + khái quát hóa thống kê

Hybrid / Neuro-Symbolic
  dùng từng cơ chế ở nơi phù hợp

Learned proposer → formal verifier → executor → feedback
```

## Các hiểu lầm thường gặp

### “AI ký hiệu đã chết”

Không. Solver, rule engine, database, planner, compiler và proof checker vẫn là những thành phần cốt lõi của nhiều hệ AI hiện đại.

### “Neuro-symbolic tự động có cả sự linh hoạt neural và bảo đảm symbolic”

Không. Chỉ có bảo đảm khi kiến trúc thật sự có lớp kiểm chứng hoặc cưỡng chế đúng đắn. Penalty logic khả vi không tương đương chứng minh cứng.

### “RAG chính là neuro-symbolic AI”

Không nhất thiết. Vector RAG chỉ là retrieval kết hợp generation và có thể không dùng biểu diễn hay suy luận ký hiệu.

### “Có formal verifier là toàn hệ thống đúng”

Verifier chỉ bảo đảm thuộc tính đã được đặc tả. Nó không đảm bảo bước hiểu ngôn ngữ tự nhiên hoặc các giả định thế giới thực ban đầu đúng.

## Liên kết kiến thức

AI neuro-symbolic khép lại lớp Biểu diễn tri thức và chuẩn bị chuyển sang Machine Learning. Bài học chính mang tính kiến trúc: mô hình học mạnh ở perception, ngôn ngữ và đề xuất heuristic; hệ ký hiệu hoặc deterministic system mạnh ở trạng thái tường minh, ràng buộc, tính toán chính xác và verification.

Các phần RAG, Agent và AI Engineering phía sau sẽ sử dụng lại mẫu kết hợp này nhiều lần.