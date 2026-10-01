# Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Computation là sự biến đổi trạng thái theo quy tắc** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Thông tin (information / 정보) không đồng nghĩa với ý nghĩa** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một người mới thường gặp khoa học máy tính (computer science / 컴퓨터 과학) qua programming. Điều này dễ tạo ra một hiểu nhầm: tưởng rằng lĩnh vực này chủ yếu nghiên cứu cú pháp ngôn ngữ và khung phần mềm (framework / 프레임워크). Programming rất quan trọng, nhưng nó giống việc dùng ký hiệu đại số trong Toán: là phương tiện biểu đạt một phần của tư duy chứ không phải toàn bộ đối tượng nghiên cứu.

Câu hỏi sâu hơn là: **ta có một trạng thái thông tin hiện tại, muốn biến nó thành trạng thái khác theo một quy tắc; quy tắc đó có thể được mô tả chính xác không, thực thi được không, đúng không, và tốn bao nhiêu tài nguyên?** Từ câu hỏi này xuất hiện thuật toán (algorithm / 알고리즘), cấu trúc dữ liệu (data structure / 자료구조), programming ngôn ngữ (language / 언어), CPU, operating hệ thống (system / 시스템), cơ sở dữ liệu (database / 데이터베이스), mạng (network / 네트워크) và hệ thống phân tán (distributed system / 분산 시스템).

## Computation là sự biến đổi trạng thái theo quy tắc

Computation (tính toán / 계산, 연산) có thể hiểu trước hết là một quá trình biến đổi **trạng thái (state / 상태)** (trạng thái / 상태). Một trạng thái (state / 상태) chứa thông tin cần thiết để mô tả hệ tại một thời điểm. Một chuyển tiếp (transition / 전이) quy tắc (rule / 규칙) xác định trạng thái (state / 상태) tiếp theo từ trạng thái (state / 상태) hiện tại.

Ví dụ, với phép cộng 37 + 58, ta có thể coi các chữ số, carry và vị trí đang xử lý là trạng thái (state / 상태). Thuật toán cộng theo cột là tập chuyển tiếp (transition / 전이) rules. CPU cũng hoạt động theo tinh thần tương tự: registers, bộ nhớ (memory / 메모리) và program counter mô tả trạng thái (state / 상태); mỗi instruction làm trạng thái (state / 상태) thay đổi.

Mô hình này rất mạnh vì nó nối nhiều lĩnh vực tưởng như tách biệt. Một finite-state machine, một parser, một giao dịch (transaction / 트랜잭션) cơ sở dữ liệu (database / 데이터베이스), một UI thành phần (component / 컴포넌트), một mạng (network / 네트워크) giao thức (protocol / 프로토콜) và một workflow nghiệp vụ đều có thể được lập luận (reasoning / 추론) bằng trạng thái (state / 상태) + chuyển tiếp (transition / 전이) + bất biến (invariant / 불변식).

> mô hình tư duy (mental model / 사고 모델): **Khoa học máy tính (computer science / 컴퓨터 과학) nghiên cứu những cách biểu diễn trạng thái (state / 상태) và những quy tắc biến đổi trạng thái (state / 상태) sao cho ta có thể lập luận (reasoning / 추론) về tính đúng đắn (correctness / 정확성), chi phí (cost / 비용) và thất bại (failure / 실패).**

> **Chuyển mạch:** Trong **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Thông tin (information / 정보) không đồng nghĩa với ý nghĩa** tiếp nhận điểm tựa từ **Computation là sự biến đổi trạng thái theo quy tắc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thuật toán (algorithm / 알고리즘) khác program ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thông tin (information / 정보) không đồng nghĩa với ý nghĩa

Computer xử lý biểu diễn (representation / 표현) chứ không trực tiếp “hiểu” ý nghĩa như con người. Chuỗi bit `01000001` có thể được diễn giải là số 65, ký tự `A`, một phần điểm ảnh (pixel / 픽셀), một byte trong instruction hoặc đơn giản là tám boolean values. Bit mẫu (pattern / 패턴) tự nó không mang ý nghĩa (semantic meaning / 의미적 뜻) duy nhất; **interpretation phụ thuộc vào encoding và ngữ cảnh (context / 맥락)**.

Điều này dẫn tới một nguyên tắc nền tảng: dữ liệu luôn tồn tại trong một biểu diễn (representation / 표현), và biểu diễn (representation / 표현) tạo ra cả khả năng lẫn giới hạn. Integer 32-bit biểu diễn được một miền hữu hạn; floating điểm (point / 지점) đánh đổi độ chính xác để có phạm vi (range / 범위) rất lớn; UTF-8 dùng số byte biến đổi để tương thích ASCII và vẫn biểu diễn Unicode.

Xem sâu hơn: [Information, bit và encoding](./01_information_bits_and_encoding.md) và [machine representation](./02_numbers_and_machine_representation.md).

> **Chuyển mạch:** Ở chặng này của **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Thuật toán (algorithm / 알고리즘) khác program ở đâu?** tiếp nhận điểm tựa từ **Thông tin (information / 정보) không đồng nghĩa với ý nghĩa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đúng đắn (correctness / 정확성) trước hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thuật toán (algorithm / 알고리즘) khác program ở đâu?

Thuật toán (algorithm / 알고리즘) là một procedure đủ rõ ràng để biến đầu vào (input / 입력) thành đầu ra (output / 출력) hoặc đạt một trạng thái đích. Program (chương trình / 프로그램) là một biểu diễn (representation / 표현) cụ thể của một hoặc nhiều thuật toán (algorithm / 알고리즘) trong một programming ngôn ngữ (language / 언어) và thời gian chạy (runtime / 런타임) cụ thể.

Tìm kiếm nhị phân (binary search / 이진 탐색) là một thuật toán (algorithm / 알고리즘). Một phương thức (method / 메서드) Java dùng `Arrays.binarySearch`, một hàm (function / 함수) C tự viết bằng pointer hay hiện thực (implementation / 구현) trong PostgreSQL có thể hiện thực cùng ý tưởng nhưng có bộ nhớ (memory / 메모리) mô hình (model / 모델), lỗi (error / 오류) hành vi (behavior / 동작) và giao diện (interface / 인터페이스) khác nhau.

Tách hai tầng này giúp lập luận (reasoning / 추론). Ta có thể chứng minh tìm kiếm nhị phân (binary search / 이진 탐색) cần `O(log n)` comparisons mà chưa cần chọn Java hay C. Sau đó mới hỏi hiện thực (implementation / 구현) trên hardware cụ thể có bộ nhớ đệm (cache / 캐시) locality tốt không, branch prediction ra sao, generic comparator tốn bao nhiêu chi phí.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Tính đúng đắn (correctness / 정확성) trước hiệu năng (performance / 성능)** tiếp nhận điểm tựa từ **Thuật toán (algorithm / 알고리즘) khác program ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tài nguyên (resource / 자원): thời gian, không gian và những thứ khó nhìn thấy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đúng đắn (correctness / 정확성) trước hiệu năng (performance / 성능)

Một computation hữu ích phải có specification (đặc tả / 명세): điều gì được coi là đầu vào (input / 입력) hợp lệ, đầu ra (output / 출력) mong đợi là gì, và điều kiện nào phải luôn đúng. tính đúng đắn (correctness / 정확성) là quan hệ giữa program/thuật toán (algorithm / 알고리즘) và specification đó.

Ví dụ, một hàm (function / 함수) `withdraw(account, amount)` không thể chỉ được đánh giá bằng việc “trừ tiền thành công”. Specification còn có thể yêu cầu `amount > 0`, balance không âm, giao dịch (transaction / 트랜잭션) được ghi log, và trong tính đồng thời (concurrency / 동시성) hai yêu cầu (request / 요청) không được tiêu cùng một số dư.

Đây là lý do invariants (bất biến / 불변식) xuất hiện ở khắp CS. bất biến (invariant / 불변식) là một thuộc tính (property / 속성) phải tiếp tục đúng trước và sau một nhóm trạng thái (state / 상태) transitions. vòng lặp (loop / 루프) bất biến (invariant / 불변식) giúp chứng minh thuật toán; cơ sở dữ liệu (database / 데이터베이스) bất biến (invariant / 불변식) bảo vệ nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙); filesystem bất biến (invariant / 불변식) giữ siêu dữ liệu (metadata / 메타데이터) nhất quán; phân tán (distributed / 분산) bất biến (invariant / 불변식) như “một term chỉ có một leader” giúp lập luận (reasoning / 추론) về consensus.

Xem thêm: [Logic, state, abstraction và invariants](./03_logic_state_abstraction_and_invariants.md).

> **Chuyển mạch:** Trong **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Tính đúng đắn (correctness / 정확성) trước hiệu năng (performance / 성능)** nêu điều cần giải thích; **Tài nguyên (resource / 자원): thời gian, không gian và những thứ khó nhìn thấy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Lớp trừu tượng (abstraction / 추상화): lý do hệ thống lớn có thể tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tài nguyên (resource / 자원): thời gian, không gian và những thứ khó nhìn thấy

Hai tài nguyên (resource / 자원) quen thuộc là thời gian (time / 시간) và không gian (space / 공간), nhưng hệ thống thực còn bị giới hạn bởi bandwidth, I/O operations, mạng (network / 네트워크) round trips, năng lượng (energy / 에너지), tranh chấp khóa (lock contention / 잠금 경합), bộ nhớ đệm (cache / 캐시) sức chứa (capacity / 용량), tệp (file / 파일) descriptors, liên kết (connection / 연결) pools và human độ phức tạp (complexity / 복잡도).

Một thuật toán (algorithm / 알고리즘) có độ phức tạp (complexity / 복잡도) tốt về lý thuyết chưa chắc nhanh hơn trên tải công việc (workload / 워크로드) nhỏ nếu constant factor lớn hoặc dữ liệu (data / 데이터) bố cục (layout / 레이아웃) phá bộ nhớ đệm (cache / 캐시) locality. Một phân tán (distributed / 분산) thiết kế (design / 설계) tăng availability có thể tăng độ phức tạp (complexity / 복잡도) vận hành và làm consistency yếu hơn. Vì vậy Khoa học máy tính (computer science / 컴퓨터 과학) không phải tìm “giải pháp tối ưu tuyệt đối”; rất nhiều bài toán là **sự đánh đổi (trade-off / 트레이드오프) dưới các ràng buộc (constraints / 제약조건들)**.

Điều này sẽ quay lại trong [complexity analysis](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md), [memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md) và [cross-cutting trade-offs](../90_connections/03_cross_cutting_tradeoffs.md).

> **Chuyển mạch:** Ở chặng này của **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Tài nguyên (resource / 자원): thời gian, không gian và những thứ khó nhìn thấy** nêu điều cần giải thích; **Lớp trừu tượng (abstraction / 추상화): lý do hệ thống lớn có thể tồn tại** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Ba lớp câu hỏi nên hỏi khi học một concept CS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lớp trừu tượng (abstraction / 추상화): lý do hệ thống lớn có thể tồn tại

Nếu mỗi nhà phát triển (developer / 개발자) phải nhớ voltage của transistor khi viết SQL, software hiện đại gần như không thể xây dựng. lớp trừu tượng (abstraction / 추상화) che các chi tiết phía dưới sau một mô hình (model / 모델) ổn định đủ để tầng trên lập luận (reasoning / 추론).

Tệp (file / 파일) là lớp trừu tượng (abstraction / 추상화) trên blocks của lưu trữ (storage / 저장소) thiết bị (device / 장치). tiến trình (process / 프로세스) là lớp trừu tượng (abstraction / 추상화) của một executing program trên CPU và bộ nhớ (memory / 메모리). Socket là lớp trừu tượng (abstraction / 추상화) cho communication endpoint. bảng (table / 테이블) là lớp trừu tượng (abstraction / 추상화) trên pages, indexes và logs. HTTP yêu cầu (request / 요청) là lớp trừu tượng (abstraction / 추상화) trên TCP/TLS/IP/Ethernet.

Lớp trừu tượng (abstraction / 추상화) không có nghĩa chi tiết phía dưới biến mất. Nó chỉ tạo một ranh giới (boundary / 경계). Khi hiệu năng hoặc thất bại (failure / 실패) vượt qua ranh giới (boundary / 경계), lớp trừu tượng (abstraction / 추상화) có thể “leak”: truy vấn (query / 쿼리) chậm buộc ta hiểu chỉ mục (index / 인덱스); bộ nhớ (memory / 메모리) pressure buộc ta hiểu GC và virtual bộ nhớ (memory / 메모리); hết thời gian chờ (timeout / 타임아웃) buộc ta hiểu mạng (network / 네트워크) và queueing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Ba lớp câu hỏi nên hỏi khi học một concept CS** tiếp nhận điểm tựa từ **Lớp trừu tượng (abstraction / 추상화): lý do hệ thống lớn có thể tồn tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khoa học máy tính (computer science / 컴퓨터 과학) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ba lớp câu hỏi nên hỏi khi học một concept CS

Khi gặp một thuật ngữ mới, thay vì chỉ học definition, hãy thử hỏi ba lớp câu hỏi. Thứ nhất là **mô hình (model / 모델)**: hệ thống đang coi cái gì là trạng thái (state / 상태), thao tác (operation / 연산) và bất biến (invariant / 불변식)? Thứ hai là **cơ chế (mechanism / 메커니즘)**: bên dưới nó thực sự thực hiện bằng cấu trúc dữ liệu, instruction, message hay giao thức (protocol / 프로토콜) nào? Thứ ba là **sự đánh đổi (trade-off / 트레이드오프)**: nó đánh đổi điều gì để đạt thuộc tính (property / 속성) mong muốn?

Ví dụ với bộ nhớ đệm (cache / 캐시): mô hình (model / 모델) là một lớp nhớ nhỏ nhưng nhanh giữ bản sao dữ liệu; cơ chế (mechanism / 메커니즘) là bộ nhớ đệm (cache / 캐시) line, tag, replacement và coherence; sự đánh đổi (trade-off / 트레이드오프) là sức chứa (capacity / 용량) nhỏ, consistency phức tạp và nguy cơ trượt bộ nhớ đệm (cache miss / 캐시 미스). Với cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션): mô hình (model / 모델) là một nhóm thao tác như một đơn vị lô-gic (logic / 논리); cơ chế (mechanism / 메커니즘) có khóa (lock / 잠금)/MVCC/WAL; sự đánh đổi (trade-off / 트레이드오프) là thông lượng (throughput / 처리량), độ trễ (latency / 지연 시간), isolation và contention.

> **Chuyển mạch:** Trong **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Khoa học máy tính (computer science / 컴퓨터 과학) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)** tiếp nhận điểm tựa từ **Ba lớp câu hỏi nên hỏi khi học một concept CS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khoa học máy tính (computer science / 컴퓨터 과학) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)

Khoa học máy tính (computer science / 컴퓨터 과학) tập trung nhiều vào các mô hình (models / 모델들), algorithms, limits và principles. Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) tập trung vào xây dựng và duy trì software các hệ thống (systems / 시스템들) trong các ràng buộc (constraints / 제약조건들) tổ chức, con người và môi trường vận hành (production / 운영 환경). Hai lĩnh vực chồng lấn mạnh nhưng không đồng nhất.

Hiểu độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) không tự động khiến codebase dễ maintain. Ngược lại, biết clean kiến trúc (architecture / 아키텍처) mà không hiểu tính đồng thời (concurrency / 동시성), bộ nhớ (memory / 메모리), giao dịch (transaction / 트랜잭션) hoặc mạng (network / 네트워크) thất bại (failure / 실패) sẽ tạo ra những lớp trừu tượng (abstraction / 추상화) đẹp nhưng sai về hành vi (behavior / 동작). Thư viện này cố tình nối hai phía thay vì tách chúng.

> **Chuyển mạch:** Ở chặng này của **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Khoa học máy tính (computer science / 컴퓨터 과학) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết nối tiếp theo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Khoa học máy tính (computer science / 컴퓨터 과학) = coding.”** Coding là kỹ năng biểu đạt và triển khai. CS còn nghiên cứu computation, biểu diễn (representation / 표현), algorithmic độ phức tạp (complexity / 복잡도), kiến trúc (architecture / 아키텍처), OS, ngôn ngữ (language / 언어) lý thuyết (theory / 이론), networking, thông tin (information / 정보), bảo mật (security / 보안) và giới hạn của những gì máy có thể tính.

**“Máy tính làm chính xác những gì ta bảo nên nếu bug thì chỉ là typo.”** Bug thường nằm ở specification thiếu, các giả định (assumptions / 가정들) sai, race điều kiện (condition / 조건), overflow, partial thất bại (failure / 실패) hoặc mismatch giữa lớp trừu tượng (abstraction / 추상화) và cơ chế (mechanism / 메커니즘).

**“Hardware không còn quan trọng với ứng dụng (application / 애플리케이션) nhà phát triển (developer / 개발자).”** Hardware được che tốt hơn, nhưng bộ nhớ đệm (cache / 캐시) locality, CPU cores, bộ nhớ (memory / 메모리) bandwidth, SSD hành vi (behavior / 동작) và mạng (network / 네트워크) vẫn ảnh hưởng trực tiếp tới độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량) của software.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học máy tính (computer science / 컴퓨터 과학) thực sự nghiên cứu gì?**, **Kết nối tiếp theo** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối tiếp theo

Chapter này cung cấp vocabulary cho toàn thư viện (library / 라이브러리). Bước tiếp theo hợp lý là hiểu [information được mã hóa thành bit như thế nào](./01_information_bits_and_encoding.md), rồi [machine representation của số và dữ liệu](./02_numbers_and_machine_representation.md). Sau đó [logic, state và invariants](./03_logic_state_abstraction_and_invariants.md) tạo nền để học algorithms, digital circuits và operating các hệ thống (systems / 시스템들).

> **Bàn giao:** Sau **Kết nối tiếp theo**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
