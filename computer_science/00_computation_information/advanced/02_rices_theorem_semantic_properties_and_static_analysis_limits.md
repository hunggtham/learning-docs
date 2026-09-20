# Rice's theorem, semantic properties và giới hạn static analysis

Developer thường muốn tool trả lời những câu như “program này có bao giờ crash không?”, “function này có luôn trả đúng result không?” hoặc “code này có leak secret không?”. Static analysis có thể trả lời rất nhiều câu hữu ích, nhưng với general programs tồn tại giới hạn lý thuyết sâu hơn vấn đề performance của tool.

## Syntax và semantics

Syntactic property nhìn hình dạng chương trình: có dùng API X không, AST có pattern Y không. Semantic property nói về behavior mà program computes: có terminate không, có thể trả value cụ thể không, hai programs có cùng function không.

Semantic reasoning mạnh hơn nhưng cũng khó hơn vì phải xét potentially unbounded execution.

## Rice's theorem

Trực giác của **Rice's theorem**: mọi non-trivial semantic property của partial computable functions đều undecidable trong general case. “Non-trivial” nghĩa property đúng với một số computable functions và sai với một số khác.

Điều này không nói analyzer vô dụng. Nó nói không thể có algorithm luôn terminate và luôn trả lời chính xác cho mọi program về mọi property semantic kiểu đó.

## Halting problem connection

Nhiều impossibility proof dùng reduction từ halting problem. Nếu ta có perfect analyzer cho property P, ta có thể xây program đặc biệt để dùng analyzer đó quyết định halting, mâu thuẫn với undecidability.

Reduction vì vậy là kỹ thuật biến “nếu giải được B thì giải được A” để chuyển lower bound/impossibility.

## Soundness và completeness

Static analyzer thường phải trade-off. **Sound** analyzer cố không bỏ sót lỗi thuộc model nhưng có false positives. **Complete** theo một setting có thể tránh false positive nhưng bỏ sót hoặc chỉ áp dụng restricted language.

Security tooling thường ưu tiên soundness hơn ở critical property; IDE lint có thể ưu tiên signal/noise để developer không bỏ qua cảnh báo.

## Abstract interpretation

Analyzer thay concrete states vô hạn bằng abstract domain hữu hạn/compact hơn, rồi compute fixed point. Ví dụ thay mọi integer bằng sign `{negative, zero, positive}`.

Abstraction mất thông tin nhưng làm analysis tractable. False positive thường xuất hiện vì nhiều concrete states bị gộp.

## Restriction tạo decidability

Finite-state protocol, bounded model checking, total language hoặc restricted query language có thể cho stronger guarantees chính vì expressive power bị giới hạn.

Đây là recurring principle: model yếu hơn đôi khi hữu ích hơn vì có thể prove nhiều hơn.

## AI code analysis không xóa giới hạn

ML/LLM có thể dự đoán bug dựa trên patterns nhưng không biến undecidable property thành decidable proof. Prediction và formal guarantee là hai loại evidence khác nhau.

## Mental Model

> Static analysis luôn đứng giữa expressive power, precision và termination cost. Undecidability không bảo ta ngừng phân tích; nó bảo ta phải chọn abstraction, restriction và loại guarantee một cách rõ ràng.