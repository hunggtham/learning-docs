# Computer Science thực sự nghiên cứu gì?

Một người mới thường gặp Computer Science (khoa học máy tính / 컴퓨터 과학, 전산학) qua programming. Điều này dễ tạo ra một hiểu nhầm: tưởng rằng lĩnh vực này chủ yếu nghiên cứu cú pháp ngôn ngữ và framework. Programming rất quan trọng, nhưng nó giống việc dùng ký hiệu đại số trong Toán: là phương tiện biểu đạt một phần của tư duy chứ không phải toàn bộ đối tượng nghiên cứu.

Câu hỏi sâu hơn là: **ta có một trạng thái thông tin hiện tại, muốn biến nó thành trạng thái khác theo một quy tắc; quy tắc đó có thể được mô tả chính xác không, thực thi được không, đúng không, và tốn bao nhiêu tài nguyên?** Từ câu hỏi này xuất hiện algorithm, data structure, programming language, CPU, operating system, database, network và distributed system.

## Computation là sự biến đổi trạng thái theo quy tắc

Computation (tính toán / 계산, 연산) có thể hiểu trước hết là một quá trình biến đổi **state** (trạng thái / 상태). Một state chứa thông tin cần thiết để mô tả hệ tại một thời điểm. Một transition rule xác định state tiếp theo từ state hiện tại.

Ví dụ, với phép cộng 37 + 58, ta có thể coi các chữ số, carry và vị trí đang xử lý là state. Thuật toán cộng theo cột là tập transition rules. CPU cũng hoạt động theo tinh thần tương tự: registers, memory và program counter mô tả state; mỗi instruction làm state thay đổi.

Mô hình này rất mạnh vì nó nối nhiều lĩnh vực tưởng như tách biệt. Một finite-state machine, một parser, một transaction database, một UI component, một network protocol và một workflow nghiệp vụ đều có thể được reasoning bằng state + transition + invariant.

> Mental model: **Computer Science nghiên cứu những cách biểu diễn state và những quy tắc biến đổi state sao cho ta có thể reasoning về correctness, cost và failure.**

## Information không đồng nghĩa với ý nghĩa

Computer xử lý representation chứ không trực tiếp “hiểu” ý nghĩa như con người. Chuỗi bit `01000001` có thể được diễn giải là số 65, ký tự `A`, một phần pixel, một byte trong instruction hoặc đơn giản là tám boolean values. Bit pattern tự nó không mang semantic meaning duy nhất; **interpretation phụ thuộc vào encoding và context**.

Điều này dẫn tới một nguyên tắc nền tảng: dữ liệu luôn tồn tại trong một representation, và representation tạo ra cả khả năng lẫn giới hạn. Integer 32-bit biểu diễn được một miền hữu hạn; floating point đánh đổi độ chính xác để có range rất lớn; UTF-8 dùng số byte biến đổi để tương thích ASCII và vẫn biểu diễn Unicode.

Xem sâu hơn: [Information, bit và encoding](./01_information_bits_and_encoding.md) và [machine representation](./02_numbers_and_machine_representation.md).

## Algorithm khác program ở đâu?

Algorithm (thuật toán / 알고리즘) là một procedure đủ rõ ràng để biến input thành output hoặc đạt một trạng thái đích. Program (chương trình / 프로그램) là một representation cụ thể của một hoặc nhiều algorithm trong một programming language và runtime cụ thể.

Binary search là một algorithm. Một method Java dùng `Arrays.binarySearch`, một function C tự viết bằng pointer hay implementation trong PostgreSQL có thể hiện thực cùng ý tưởng nhưng có memory model, error behavior và interface khác nhau.

Tách hai tầng này giúp reasoning. Ta có thể chứng minh binary search cần `O(log n)` comparisons mà chưa cần chọn Java hay C. Sau đó mới hỏi implementation trên hardware cụ thể có cache locality tốt không, branch prediction ra sao, generic comparator tốn bao nhiêu chi phí.

## Correctness trước performance

Một computation hữu ích phải có specification (đặc tả / 명세): điều gì được coi là input hợp lệ, output mong đợi là gì, và điều kiện nào phải luôn đúng. Correctness (tính đúng đắn / 정확성) là quan hệ giữa program/algorithm và specification đó.

Ví dụ, một function `withdraw(account, amount)` không thể chỉ được đánh giá bằng việc “trừ tiền thành công”. Specification còn có thể yêu cầu `amount > 0`, balance không âm, transaction được ghi log, và trong concurrency hai request không được tiêu cùng một số dư.

Đây là lý do invariants (bất biến / 불변식) xuất hiện ở khắp CS. Invariant là một property phải tiếp tục đúng trước và sau một nhóm state transitions. Loop invariant giúp chứng minh thuật toán; database invariant bảo vệ business rule; filesystem invariant giữ metadata nhất quán; distributed invariant như “một term chỉ có một leader” giúp reasoning về consensus.

Xem thêm: [Logic, state, abstraction và invariants](./03_logic_state_abstraction_and_invariants.md).

## Resource: thời gian, không gian và những thứ khó nhìn thấy

Hai resource quen thuộc là time và space, nhưng hệ thống thực còn bị giới hạn bởi bandwidth, I/O operations, network round trips, energy, lock contention, cache capacity, file descriptors, connection pools và human complexity.

Một algorithm có complexity tốt về lý thuyết chưa chắc nhanh hơn trên workload nhỏ nếu constant factor lớn hoặc data layout phá cache locality. Một distributed design tăng availability có thể tăng complexity vận hành và làm consistency yếu hơn. Vì vậy Computer Science không phải tìm “giải pháp tối ưu tuyệt đối”; rất nhiều bài toán là **trade-off dưới constraints**.

Điều này sẽ quay lại trong [complexity analysis](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md), [memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md) và [cross-cutting trade-offs](../90_connections/03_cross_cutting_tradeoffs.md).

## Abstraction: lý do hệ thống lớn có thể tồn tại

Nếu mỗi developer phải nhớ voltage của transistor khi viết SQL, software hiện đại gần như không thể xây dựng. Abstraction (trừu tượng hóa / 추상화) che các chi tiết phía dưới sau một model ổn định đủ để tầng trên reasoning.

File là abstraction trên blocks của storage device. Process là abstraction của một executing program trên CPU và memory. Socket là abstraction cho communication endpoint. Table là abstraction trên pages, indexes và logs. HTTP request là abstraction trên TCP/TLS/IP/Ethernet.

Abstraction không có nghĩa chi tiết phía dưới biến mất. Nó chỉ tạo một boundary. Khi hiệu năng hoặc failure vượt qua boundary, abstraction có thể “leak”: query chậm buộc ta hiểu index; memory pressure buộc ta hiểu GC và virtual memory; timeout buộc ta hiểu network và queueing.

## Ba lớp câu hỏi nên hỏi khi học một concept CS

Khi gặp một thuật ngữ mới, thay vì chỉ học definition, hãy thử hỏi ba lớp câu hỏi. Thứ nhất là **model**: hệ thống đang coi cái gì là state, operation và invariant? Thứ hai là **mechanism**: bên dưới nó thực sự thực hiện bằng cấu trúc dữ liệu, instruction, message hay protocol nào? Thứ ba là **trade-off**: nó đánh đổi điều gì để đạt property mong muốn?

Ví dụ với cache: model là một lớp nhớ nhỏ nhưng nhanh giữ bản sao dữ liệu; mechanism là cache line, tag, replacement và coherence; trade-off là capacity nhỏ, consistency phức tạp và nguy cơ cache miss. Với database transaction: model là một nhóm thao tác như một đơn vị logic; mechanism có lock/MVCC/WAL; trade-off là throughput, latency, isolation và contention.

## Computer Science và Software Engineering

Computer Science tập trung nhiều vào models, algorithms, limits và principles. Software Engineering (kỹ nghệ phần mềm / 소프트웨어 공학) tập trung vào xây dựng và duy trì software systems trong constraints tổ chức, con người và production. Hai lĩnh vực chồng lấn mạnh nhưng không đồng nhất.

Hiểu complexity theory không tự động khiến codebase dễ maintain. Ngược lại, biết clean architecture mà không hiểu concurrency, memory, transaction hoặc network failure sẽ tạo ra những abstraction đẹp nhưng sai về behavior. Thư viện này cố tình nối hai phía thay vì tách chúng.

## Common Misconceptions

**“Computer Science = coding.”** Coding là kỹ năng biểu đạt và triển khai. CS còn nghiên cứu computation, representation, algorithmic complexity, architecture, OS, language theory, networking, information, security và giới hạn của những gì máy có thể tính.

**“Máy tính làm chính xác những gì ta bảo nên nếu bug thì chỉ là typo.”** Bug thường nằm ở specification thiếu, assumptions sai, race condition, overflow, partial failure hoặc mismatch giữa abstraction và mechanism.

**“Hardware không còn quan trọng với application developer.”** Hardware được che tốt hơn, nhưng cache locality, CPU cores, memory bandwidth, SSD behavior và network vẫn ảnh hưởng trực tiếp tới latency và throughput của software.

## Kết nối tiếp theo

Chapter này cung cấp vocabulary cho toàn library. Bước tiếp theo hợp lý là hiểu [information được mã hóa thành bit như thế nào](./01_information_bits_and_encoding.md), rồi [machine representation của số và dữ liệu](./02_numbers_and_machine_representation.md). Sau đó [logic, state và invariants](./03_logic_state_abstraction_and_invariants.md) tạo nền để học algorithms, digital circuits và operating systems.
