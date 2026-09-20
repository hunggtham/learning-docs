# Branch prediction, speculation và pipeline recovery

Pipeline chỉ đạt throughput cao khi front-end liên tục biết instruction tiếp theo nằm ở đâu. Conditional branch phá tính liên tục đó: trước khi điều kiện được tính xong, CPU chưa chắc nên fetch từ nhánh taken hay fall-through. Nếu chờ kết quả thật rồi mới fetch, pipeline sâu sẽ tạo nhiều bubble. **Branch prediction (분기 예측)** biến uncertainty này thành speculation có kiểm soát.

## Prediction gồm nhiều câu hỏi khác nhau

Một branch predictor không chỉ đoán “taken hay not taken”. Front-end còn phải biết branch instruction nằm ở đâu, target address là gì và với indirect branch/call/return thì control flow sẽ chuyển tới target nào.

Các cấu trúc như **Branch Target Buffer (BTB)** lưu thông tin target đã thấy; direction predictor học pattern taken/not-taken; **Return Address Stack (RAS)** chuyên dự đoán return target. Processor thực tế phối hợp nhiều predictor thay vì dựa vào một bảng duy nhất.

## Vì sao history hữu ích?

Branch thường có pattern. Loop branch có thể taken hàng nghìn lần rồi not-taken một lần. Một condition có thể tương quan với branch trước đó. Predictor vì thế dùng **local history**, **global history** hoặc tổ hợp nhiều history để dự đoán.

Hai-bit saturating counter là mental model cơ bản: thay vì đổi prediction ngay sau một lần sai, predictor cần đủ evidence để chuyển giữa strongly/weakly taken và not-taken. Predictor hiện đại phức tạp hơn nhiều, nhưng nguyên lý vẫn là khai thác correlation trong control-flow history.

## Speculative execution bắt đầu ngay sau prediction

Khi predictor chọn một path, CPU fetch, decode, rename và có thể execute các instruction trên path đó trước khi branch được resolve. Các kết quả vẫn speculative và chưa được retire. Nếu prediction đúng, processor đã che được phần lớn branch latency.

Nếu sai, các instruction trẻ hơn trên wrong path phải bị **squash**. Rename map được khôi phục từ checkpoint, front-end chuyển sang correct target và pipeline phải được refill. Chi phí này là **misprediction penalty**.

Pipeline càng sâu và front-end càng rộng, một prediction sai càng có thể lãng phí nhiều work. Vì thế predictor accuracy là thành phần kiến trúc rất quan trọng.

## Branch predictability liên hệ với code và data

Một condition có distribution 50/50 không đồng nghĩa luôn khó predict. Nếu kết quả có pattern lặp hoặc tương quan với history, predictor vẫn có thể học. Ngược lại, branch phụ thuộc dữ liệu gần-random có thể gây misprediction cao.

Ví dụ, xử lý một mảng đã sort theo threshold thường tạo một vùng false rồi một vùng true, dễ dự đoán. Cùng condition trên dữ liệu trộn ngẫu nhiên có thể khó hơn. Đây là một trong các lý do benchmark micro-level phải kiểm soát data distribution.

## Branchless code không tự động nhanh hơn

Thay branch bằng conditional move, masking hoặc vector operation có thể tránh misprediction, nhưng lại có thể buộc CPU thực hiện work ở cả hai phía hoặc kéo dài dependency chain. Nếu branch vốn rất predictable, branchless transformation có thể không mang lợi ích.

Optimization đúng phải dựa trên profile và cost model: misprediction rate, instruction count, dependency, vectorization và cache behavior.

## Indirect branch và polymorphism

Virtual dispatch, function pointer, interpreter dispatch và dynamic-language runtime thường tạo indirect branches. Khi một call site chỉ gặp một target, prediction khá dễ; khi target thay đổi nhiều, front-end khó giữ instruction stream ổn định.

JIT compiler có thể dùng profiling để specialization: nếu một call site gần như luôn nhận cùng type, runtime sinh fast path cho type đó và guard assumption. Nếu assumption không còn đúng, deoptimization đưa execution về generic path. Đây là ví dụ trực tiếp về cùng mental model speculation ở hardware và runtime.

## Security consequence của speculation

Speculative instruction bị squash không được commit architectural state, nhưng nó có thể để lại dấu vết **microarchitectural state** như cache occupancy. Các vulnerability thuộc lớp Spectre khai thác khoảng cách giữa architectural rollback và microarchitectural side effect.

Bài học kiến trúc quan trọng không phải kỹ thuật khai thác, mà là: “không retire” không đồng nghĩa “không có observable effect”. Security boundary phải xem xét cả transient execution và shared microarchitectural resources.

## Đo lường

Khi performance counter cho thấy branch-miss cao, cần liên hệ với workload thay vì sửa code mù quáng. Hãy xác định hot branch, distribution của input, compiler transformation và liệu stall thực sự bị branch hay memory latency chi phối. Một tỷ lệ miss nhỏ trong đoạn code chạy cực nhiều lần có thể quan trọng hơn tỷ lệ miss lớn trong cold path.

## Mental model

> Branch prediction là cơ chế biến control-flow uncertainty thành một giả thuyết có thể rollback. Prediction tốt giữ front-end bận; prediction sai tiêu tốn speculative work và pipeline refill. Tối ưu branch vì thế là bài toán xác suất + workload + pipeline, không phải quy tắc “if là chậm”.