# Trình biên dịch, trình thông dịch, máy ảo và JIT

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Compilers, interpreters, VM và JIT**. Route đi từ source/lexing/parsing → semantic analysis/IR → interpretation hoặc compilation → VM execution/JIT speculation, để mỗi tầng biến đổi vẫn truy được semantics ban đầu.

Mã nguồn phải được biến đổi thành các thao tác mà máy tính có thể thực thi. Thiết kế trình biên dịch cho thấy một chuỗi lớp trừu tượng: văn bản → đơn vị từ (token / 토큰) → cây cú pháp → biểu diễn ngữ nghĩa → biểu diễn trung gian → mã đã tối ưu → thực thi trên máy hoặc môi trường chạy.

## Phân tách đơn vị từ (token / 토큰) và phân tích cú pháp

**Bộ tách đơn vị từ (token / 토큰)** nhóm các ký tự thành đơn vị từ (token / 토큰) như tên định danh, số và toán tử. **Bộ phân tích cú pháp (parser)** dùng ngữ pháp để xây cây phân tích hoặc **cây cú pháp trừu tượng (Abstract syntax Tree — AST)**.

Các kỹ thuật dựa trên ngôn ngữ chính quy phù hợp với nhiều mẫu đơn vị từ (token / 토큰); ngữ pháp phi ngữ cảnh (context-free grammar) mô tả cấu trúc lồng nhau như ngoặc và khối (block / 블록). Tuy nhiên ngôn ngữ thực tế còn phải xử lý độ ưu tiên toán tử, sự mơ hồ và các kiểm tra phụ thuộc ngữ cảnh.

AST bỏ bớt dấu câu không cần thiết và giữ cấu trúc có ý nghĩa. Biểu thức `1 + 2 * 3` phải tạo cây thể hiện phép nhân có độ ưu tiên cao hơn phép cộng.

> **Chuyển mạch:** Trong **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Phân tích ngữ nghĩa** tiếp nhận điểm tựa từ **Phân tách đơn vị từ (token / 토큰) và phân tích cú pháp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biểu diễn trung gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân tích ngữ nghĩa

Trình biên dịch phải phân giải tên, kiểm tra kiểu, xác nhận quy tắc điều khiển và có thể suy luận kiểu hoặc generic tùy ngôn ngữ. Một đoạn mã đúng cú pháp vẫn có thể sai ngữ nghĩa, chẳng hạn dùng biến chưa khai báo hoặc trả về sai kiểu.

**Bảng ký hiệu (symbol table)** ánh xạ tên tới khai báo và siêu dữ liệu theo từng phạm vi.

> **Chuyển mạch:** Ở chặng này của **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Biểu diễn trung gian** tiếp nhận điểm tựa từ **Phân tích ngữ nghĩa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tối ưu hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn trung gian

**Biểu diễn trung gian (Intermediate Representation — IR)** nằm giữa mã nguồn và mã đích, giúp nhiều bước tối ưu ít phụ thuộc trực tiếp vào ngôn ngữ hoặc phần cứng. **Dạng gán tĩnh đơn (Static Single Assignment — SSA)** tạo phiên bản biến sao cho mỗi phiên bản chỉ được gán một lần, nhờ đó quan hệ luồng dữ liệu và chuỗi định nghĩa–sử dụng rõ ràng hơn.

LLVM IR, bytecode JVM và các IR riêng của từng trình biên dịch nằm ở các mức trừu tượng khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Tối ưu hóa** tiếp nhận điểm tựa từ **Biểu diễn trung gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biên dịch trước khi chạy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tối ưu hóa

**Gấp hằng (constant folding)** tính trước biểu thức như `2*3`. **Loại mã chết (dead-code elimination)** bỏ phần tính toán không thể ảnh hưởng kết quả quan sát được. **Nội tuyến (inlining)** thay lời gọi hàm bằng thân hàm để mở thêm cơ hội tối ưu nhưng có thể làm mã máy lớn hơn. Loại biểu thức con chung, tối ưu vòng lặp và vectorization cũng thay đổi cấu trúc tính toán để giảm chi phí.

Trình biên dịch chỉ được tối ưu nếu vẫn giữ ngữ nghĩa mà đặc tả ngôn ngữ cho phép quan sát. Hành vi không xác định (undefined behavior) trong C/C++ tạo thêm tự do tối ưu vì trình biên dịch có thể giả định chương trình hợp lệ không đi vào trường hợp UB.

> **Chuyển mạch:** Trong **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Biên dịch trước khi chạy** tiếp nhận điểm tựa từ **Tối ưu hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thông dịch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biên dịch trước khi chạy

**Biên dịch trước thời gian chạy (Ahead-of-Time — AOT)** tạo mã máy trước khi chương trình bắt đầu. Cách này giúp thời gian khởi động dễ dự đoán và không cần trình biên dịch trong thời gian chạy (runtime / 런타임), nhưng khó tận dụng chính xác dữ liệu hành vi khi chạy nếu không có tối ưu dựa trên hồ sơ (profile-guided optimization).

C, C++ và Rust thường dùng AOT. Một số hệ thống bản địa (native / 네이티브) ảnh (image / 이미지) áp dụng ý tưởng tương tự cho ngôn ngữ có thời gian chạy (runtime / 런타임) quản lý, đổi lại phải xử lý cẩn thận reflection và tính năng động.

> **Chuyển mạch:** Ở chặng này của **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Thông dịch** tiếp nhận điểm tựa từ **Biên dịch trước khi chạy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biên dịch đúng lúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thông dịch

Trình thông dịch (interpreter / 인터프리터) có thể đi trực tiếp trên AST hoặc thực thi bytecode trong một vòng lặp điều phối. Cách này giảm chi phí biên dịch ban đầu và thuận lợi cho hành vi động, nhưng chi phí điều phối ở mỗi thao tác có thể lớn.

Máy ảo bytecode đưa chương trình về một tập lệnh gọn và có tính di động. Bytecode JVM, chẳng hạn, có thể chạy trên nhiều triển khai JVM ở các nền tảng khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Biên dịch đúng lúc** tiếp nhận điểm tựa từ **Thông dịch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thu gom rác và dịch vụ của thời gian chạy (runtime / 런타임)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biên dịch đúng lúc

**Biên dịch đúng lúc (Just-In-Time — JIT)** quan sát chương trình đang chạy rồi biên dịch các hàm hoặc vòng lặp nóng thành mã máy tối ưu. Hồ sơ khi chạy cho biết kiểu đối tượng thực tế, tần suất nhánh và đường chạy nóng. JIT có thể tối ưu theo giả định rồi **hoàn nguyên tối ưu (deoptimization)** nếu giả định không còn đúng.

Java HotSpot với biên dịch nhiều tầng và các engine JavaScript hiện đại đều dùng biến thể của ý tưởng này. Vì vậy khi đo hiệu năng cần chú ý giai đoạn làm nóng (warm-up): hành vi lúc mới chạy và trạng thái ổn định có thể khác nhau.

> **Chuyển mạch:** Trong **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Thu gom rác và dịch vụ của thời gian chạy (runtime / 런타임)** tiếp nhận điểm tựa từ **Biên dịch đúng lúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trình liên kết và trình nạp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thu gom rác và dịch vụ của thời gian chạy (runtime / 런타임)

Môi trường thực thi được quản lý thường cung cấp thu gom rác (GC), nạp lớp, ngoại lệ, đồng bộ, reflection và profiling. Hiệu năng vì thế không chỉ phụ thuộc mã do trình biên dịch (compiler / 컴파일러) sinh ra mà còn phụ thuộc hành vi của thời gian chạy (runtime / 런타임).

**Điểm an toàn (safepoint)** là vị trí thời gian chạy (runtime / 런타임) có thể dừng hoặc phối hợp các luồng cho GC và deoptimization. Tạm dừng toàn bộ chương trình (stop-the-world) không phải toàn bộ quá trình GC; bộ thu gom đồng thời thực hiện nhiều giai đoạn song song với ứng dụng nhưng vẫn cần những điểm phối hợp nhất định.

> **Chuyển mạch:** Ở chặng này của **Trình biên dịch, trình thông dịch, máy ảo và JIT**, sau nội dung của **Thu gom rác và dịch vụ của thời gian chạy (runtime / 런타임)**, **Trình liên kết và trình nạp** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Khả năng tái lập và bẫy khi đo hiệu năng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trình liên kết và trình nạp

Trình biên dịch mã máy thường tạo tệp (file / 파일) đối tượng; **trình liên kết (linker)** phân giải ký hiệu và relocation. **Trình nạp (loader)** ánh xạ tệp (file / 파일) thực thi và thư viện dùng chung vào tiến trình. Trình liên kết động có thể phân giải ký hiệu theo nhu cầu. Đây là phần tiếp nối của [assembly và ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Trình liên kết và trình nạp** đã nêu tiêu chí phân biệt, còn **Khả năng tái lập và bẫy khi đo hiệu năng** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng tái lập và bẫy khi đo hiệu năng

Đo vi mô (microbenchmark) dễ bị ảnh hưởng bởi loại mã chết, gấp hằng, thời gian làm nóng JIT, GC và thay đổi tần số CPU. Công cụ như JMH giúp tránh nhiều bẫy phổ biến, nhưng tải đo vẫn phải đại diện cho cách chương trình thực sự được sử dụng.

> **Chuyển mạch:** Trong **Trình biên dịch, trình thông dịch, máy ảo và JIT**, các dấu vết trong **Khả năng tái lập và bẫy khi đo hiệu năng** được đọc cùng nhau ở **Mô hình tư duy** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> trình biên dịch (compiler / 컴파일러) và thời gian chạy (runtime / 런타임) tạo thành một **chuỗi biến đổi giữ nguyên ngữ nghĩa quan sát được**. Mỗi giai đoạn thay đổi cách biểu diễn để việc phân tích hoặc thực thi thuận lợi hơn, nhưng không được tùy ý thay đổi ý nghĩa chương trình.

> **Chuyển mạch:** Ở chặng này của **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“Trình thông dịch không biên dịch gì.”** Không luôn đúng. Nhiều trình thông dịch (interpreter / 인터프리터) chuyển mã nguồn thành bytecode hoặc IR trước khi thực thi.

**“JIT luôn nhanh hơn AOT.”** Không đúng. Thời gian khởi động, chất lượng hồ sơ, bộ nhớ mã, thời lượng tải và AOT có PGO đều có thể thay đổi kết quả.

**“Bộ tối ưu chỉ làm mã nhanh hơn mà không thay đổi gì khác.”** Nó giữ ngữ nghĩa quan sát được theo đặc tả, nhưng thời gian, bố trí mã và hình dạng mã máy có thể thay đổi; UB và dữ liệu (data / 데이터) race còn làm các giả định phức tạp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trình biên dịch, trình thông dịch, máy ảo và JIT**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Kết nối** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ngôn ngữ hình thức và giới hạn tính toán nằm ở [Computability](../00_computation_information/04_computability_and_limits.md), đích máy ở [CPU/ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md), bộ nhớ thời gian chạy (runtime / 런타임) ở [kiểu và bộ nhớ](./01_types_values_references_and_memory.md), còn chuỗi bản dựng (build / 빌드) được nối tại [build, link và package](../08_software_systems/01_version_control_build_link_and_packages.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
