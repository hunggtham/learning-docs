# Trình biên dịch, trình thông dịch, máy ảo và JIT

Mã nguồn phải được biến đổi thành các thao tác mà máy tính có thể thực thi. Thiết kế trình biên dịch cho thấy một chuỗi lớp trừu tượng: văn bản → token → cây cú pháp → biểu diễn ngữ nghĩa → biểu diễn trung gian → mã đã tối ưu → thực thi trên máy hoặc môi trường chạy.

## Phân tách token và phân tích cú pháp

**Bộ tách token (lexer/tokenizer)** nhóm các ký tự thành token như tên định danh, số và toán tử. **Bộ phân tích cú pháp (parser)** dùng ngữ pháp để xây cây phân tích hoặc **cây cú pháp trừu tượng (Abstract Syntax Tree — AST)**.

Các kỹ thuật dựa trên ngôn ngữ chính quy phù hợp với nhiều mẫu token; ngữ pháp phi ngữ cảnh (context-free grammar) mô tả cấu trúc lồng nhau như ngoặc và block. Tuy nhiên ngôn ngữ thực tế còn phải xử lý độ ưu tiên toán tử, sự mơ hồ và các kiểm tra phụ thuộc ngữ cảnh.

AST bỏ bớt dấu câu không cần thiết và giữ cấu trúc có ý nghĩa. Biểu thức `1 + 2 * 3` phải tạo cây thể hiện phép nhân có độ ưu tiên cao hơn phép cộng.

## Phân tích ngữ nghĩa

Trình biên dịch phải phân giải tên, kiểm tra kiểu, xác nhận quy tắc điều khiển và có thể suy luận kiểu hoặc generic tùy ngôn ngữ. Một đoạn mã đúng cú pháp vẫn có thể sai ngữ nghĩa, chẳng hạn dùng biến chưa khai báo hoặc trả về sai kiểu.

**Bảng ký hiệu (symbol table)** ánh xạ tên tới khai báo và siêu dữ liệu theo từng phạm vi.

## Biểu diễn trung gian

**Biểu diễn trung gian (Intermediate Representation — IR)** nằm giữa mã nguồn và mã đích, giúp nhiều bước tối ưu ít phụ thuộc trực tiếp vào ngôn ngữ hoặc phần cứng. **Dạng gán tĩnh đơn (Static Single Assignment — SSA)** tạo phiên bản biến sao cho mỗi phiên bản chỉ được gán một lần, nhờ đó quan hệ luồng dữ liệu và chuỗi định nghĩa–sử dụng rõ ràng hơn.

LLVM IR, bytecode JVM và các IR riêng của từng trình biên dịch nằm ở các mức trừu tượng khác nhau.

## Tối ưu hóa

**Gấp hằng (constant folding)** tính trước biểu thức như `2*3`. **Loại mã chết (dead-code elimination)** bỏ phần tính toán không thể ảnh hưởng kết quả quan sát được. **Nội tuyến (inlining)** thay lời gọi hàm bằng thân hàm để mở thêm cơ hội tối ưu nhưng có thể làm mã máy lớn hơn. Loại biểu thức con chung, tối ưu vòng lặp và vectorization cũng thay đổi cấu trúc tính toán để giảm chi phí.

Trình biên dịch chỉ được tối ưu nếu vẫn giữ ngữ nghĩa mà đặc tả ngôn ngữ cho phép quan sát. Hành vi không xác định (undefined behavior) trong C/C++ tạo thêm tự do tối ưu vì trình biên dịch có thể giả định chương trình hợp lệ không đi vào trường hợp UB.

## Biên dịch trước khi chạy

**Biên dịch trước thời gian chạy (Ahead-of-Time — AOT)** tạo mã máy trước khi chương trình bắt đầu. Cách này giúp thời gian khởi động dễ dự đoán và không cần trình biên dịch trong runtime, nhưng khó tận dụng chính xác dữ liệu hành vi khi chạy nếu không có tối ưu dựa trên hồ sơ (profile-guided optimization).

C, C++ và Rust thường dùng AOT. Một số hệ thống native image áp dụng ý tưởng tương tự cho ngôn ngữ có runtime quản lý, đổi lại phải xử lý cẩn thận reflection và tính năng động.

## Thông dịch

Trình thông dịch (interpreter) có thể đi trực tiếp trên AST hoặc thực thi bytecode trong một vòng lặp điều phối. Cách này giảm chi phí biên dịch ban đầu và thuận lợi cho hành vi động, nhưng chi phí điều phối ở mỗi thao tác có thể lớn.

Máy ảo bytecode đưa chương trình về một tập lệnh gọn và có tính di động. Bytecode JVM, chẳng hạn, có thể chạy trên nhiều triển khai JVM ở các nền tảng khác nhau.

## Biên dịch đúng lúc

**Biên dịch đúng lúc (Just-In-Time — JIT)** quan sát chương trình đang chạy rồi biên dịch các hàm hoặc vòng lặp nóng thành mã máy tối ưu. Hồ sơ khi chạy cho biết kiểu đối tượng thực tế, tần suất nhánh và đường chạy nóng. JIT có thể tối ưu theo giả định rồi **hoàn nguyên tối ưu (deoptimization)** nếu giả định không còn đúng.

Java HotSpot với biên dịch nhiều tầng và các engine JavaScript hiện đại đều dùng biến thể của ý tưởng này. Vì vậy khi đo hiệu năng cần chú ý giai đoạn làm nóng (warm-up): hành vi lúc mới chạy và trạng thái ổn định có thể khác nhau.

## Thu gom rác và dịch vụ của runtime

Môi trường thực thi được quản lý thường cung cấp thu gom rác (GC), nạp lớp, ngoại lệ, đồng bộ, reflection và profiling. Hiệu năng vì thế không chỉ phụ thuộc mã do compiler sinh ra mà còn phụ thuộc hành vi của runtime.

**Điểm an toàn (safepoint)** là vị trí runtime có thể dừng hoặc phối hợp các luồng cho GC và deoptimization. Tạm dừng toàn bộ chương trình (stop-the-world) không phải toàn bộ quá trình GC; bộ thu gom đồng thời thực hiện nhiều giai đoạn song song với ứng dụng nhưng vẫn cần những điểm phối hợp nhất định.

## Trình liên kết và trình nạp

Trình biên dịch mã máy thường tạo file đối tượng; **trình liên kết (linker)** phân giải ký hiệu và relocation. **Trình nạp (loader)** ánh xạ file thực thi và thư viện dùng chung vào tiến trình. Trình liên kết động có thể phân giải ký hiệu theo nhu cầu. Đây là phần tiếp nối của [assembly và ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md).

## Khả năng tái lập và bẫy khi đo hiệu năng

Đo vi mô (microbenchmark) dễ bị ảnh hưởng bởi loại mã chết, gấp hằng, thời gian làm nóng JIT, GC và thay đổi tần số CPU. Công cụ như JMH giúp tránh nhiều bẫy phổ biến, nhưng tải đo vẫn phải đại diện cho cách chương trình thực sự được sử dụng.

## Mô hình tư duy

> Compiler và runtime tạo thành một **chuỗi biến đổi giữ nguyên ngữ nghĩa quan sát được**. Mỗi giai đoạn thay đổi cách biểu diễn để việc phân tích hoặc thực thi thuận lợi hơn, nhưng không được tùy ý thay đổi ý nghĩa chương trình.

## Những hiểu nhầm thường gặp

**“Trình thông dịch không biên dịch gì.”** Không luôn đúng. Nhiều interpreter chuyển mã nguồn thành bytecode hoặc IR trước khi thực thi.

**“JIT luôn nhanh hơn AOT.”** Không đúng. Thời gian khởi động, chất lượng hồ sơ, bộ nhớ mã, thời lượng tải và AOT có PGO đều có thể thay đổi kết quả.

**“Bộ tối ưu chỉ làm mã nhanh hơn mà không thay đổi gì khác.”** Nó giữ ngữ nghĩa quan sát được theo đặc tả, nhưng thời gian, bố trí mã và hình dạng mã máy có thể thay đổi; UB và data race còn làm các giả định phức tạp hơn.

## Kết nối

Ngôn ngữ hình thức và giới hạn tính toán nằm ở [Computability](../00_computation_information/04_computability_and_limits.md), đích máy ở [CPU/ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md), bộ nhớ runtime ở [kiểu và bộ nhớ](./01_types_values_references_and_memory.md), còn chuỗi build được nối tại [build, link và package](../08_software_systems/01_version_control_build_link_and_packages.md).
