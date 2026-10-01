# Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ bài toán (problem / 문제) statement tới specification** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Partial tính đúng đắn (correctness / 정확성) và termination** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Thuật toán (algorithm / 알고리즘) không phải một đoạn mã (code / 코드) có vẻ chạy được. Nó là một procedure hữu hạn, rõ nghĩa, biến đầu vào (input / 입력) thành đầu ra (output / 출력) theo một specification. Tư duy thuật toán bắt đầu trước mã (code / 코드): xác định trạng thái (state / 상태) nào quan trọng, thao tác (operation / 연산) nào được phép, bất biến (invariant / 불변식) nào phải giữ, và bằng chứng nào cho thấy procedure thực sự giải đúng bài toán.

## Từ bài toán (problem / 문제) statement tới specification

Một câu như “tìm phần tử lớn nhất” còn thiếu nhiều điều. đầu vào (input / 입력) có thể rỗng không? Có duplicate không? Dữ liệu so sánh được bằng thứ tự (ordering / 순서) nào? Ta trả giá trị (value / 값) hay chỉ mục (index / 인덱스)? Nếu comparator không transitive thì chuyện gì xảy ra?

Specification (명세 / đặc tả) làm những các giả định (assumptions / 가정들) này tường minh (explicit / 명시적). Với array không rỗng `A[0..n-1]`, specification của `max` có thể là: đầu ra (output / 출력) `m` thuộc array và với mọi `i`, `m >= A[i]`.

Một hiện thực (implementation / 구현) đơn giản:

```text
m = A[0]
for i = 1 .. n-1:
    if A[i] > m:
        m = A[i]
return m
```

Điểm đáng học không phải cú pháp (syntax / 문법) mà là lập luận (reasoning / 추론). Sau khi đã xử lý prefix `A[0..i]`, bất biến (invariant / 불변식) là `m` bằng maximum của prefix đó. Ban đầu bất biến (invariant / 불변식) đúng với prefix một phần tử. Mỗi iteration hoặc giữ `m`, hoặc thay bằng phần tử lớn hơn, nên bất biến (invariant / 불변식) được bảo toàn. Khi vòng lặp (loop / 루프) kết thúc, prefix chính là toàn array; specification được thỏa.

> **Chuyển mạch:** Problem statement phải trở thành specification có pre/postcondition; partial correctness kết hợp termination mới thành total correctness, rồi decomposition chia proof obligation.

## Partial tính đúng đắn (correctness / 정확성) và termination

Một thuật toán (algorithm / 알고리즘) có thể “nếu kết thúc thì đúng” nhưng không bảo đảm kết thúc. Partial tính đúng đắn (correctness / 정확성) nói đầu ra (output / 출력) đúng nếu computation terminates. Total tính đúng đắn (correctness / 정확성) cần cả partial tính đúng đắn (correctness / 정확성) lẫn termination.

Với vòng lặp (loop / 루프), termination thường chứng minh bằng một **variant** giảm theo well-founded thứ tự (order / 순서). tìm kiếm nhị phân (binary search / 이진 탐색) làm interval giảm; Euclidean thuật toán (algorithm / 알고리즘) làm remainder giảm; recursion cần tiến gần cơ sở (base / 기반) trường hợp (case / 사례).

Trong môi trường vận hành (production / 운영 환경), termination còn có nghĩa thực dụng hơn: mạng (network / 네트워크) lời gọi (call / 호출) cần hết thời gian chờ (timeout / 타임아웃); thử lại (retry / 재시도) cần bound/backoff; hàng đợi (queue / 큐) bên tiêu thụ (consumer / 소비자) phải tránh poison message vòng lặp (loop / 루프). Lý thuyết termination gặp trực tiếp độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링).

> **Chuyển mạch:** Ở chặng này của **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**, **Decomposition và subproblem** tiếp nhận điểm tựa từ **Partial tính đúng đắn (correctness / 정확성) và termination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đúng đắn (correctness / 정확성) proof không phải hình thức xa rời mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decomposition và subproblem

Algorithmic thinking thường tìm cách biến bài toán (problem / 문제) thành subproblems dễ hơn. Merge sort chia array thành hai halves, sort từng nửa rồi merge. động (dynamic / 동적) programming nhận ra overlapping subproblems và lưu kết quả. đồ thị (graph / 그래프) tìm kiếm (search / 검색) biến câu hỏi “đi tới đâu được?” thành việc lặp lại expand frontier.

Điểm quan trọng là decomposition phải preserve cấu trúc (structure / 구조). Chia bừa một bài toán (problem / 문제) không tự động tạo thuật toán (algorithm / 알고리즘) tốt. Với divide-and-conquer, ta cần xác định cách combine; với greedy, phải chứng minh cục bộ (local / 로컬) choice không phá toàn cục (global / 전역) optimum; với DP, cần trạng thái (state / 상태) đủ để mô tả phần quá khứ ảnh hưởng tương lai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**, **Tính đúng đắn (correctness / 정확성) proof không phải hình thức xa rời mã (code / 코드)** tiếp nhận điểm tựa từ **Decomposition và subproblem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deterministic, randomized và nondeterministic hành vi (behavior / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đúng đắn (correctness / 정확성) proof không phải hình thức xa rời mã (code / 코드)

Formal proof có thể nặng, nhưng tư duy proof mang lại câu hỏi thiết thực:

- Precondition nào đang bị giả định (assumption / 가정) ngầm?
- vòng lặp (loop / 루프) bất biến (invariant / 불변식) là gì?
- cấu trúc dữ liệu (data structure / 자료구조) bất biến (invariant / 불변식) nào phương thức (method / 메서드) phải bảo toàn?
- Nếu duplicate/empty/overflow xảy ra thì proof còn đúng không?
- Nếu comparator không nhất quán thì thứ tự (ordering / 순서) các giả định (assumptions / 가정들) có vỡ không?

Property-based testing cũng xuất phát từ tinh thần tương tự: thay vì chỉ kiểm tra vài expected outputs, encode properties như “sort đầu ra (output / 출력) là ordered và là permutation của đầu vào (input / 입력)”. Testing không thay proof, nhưng thuộc tính (property / 속성) thinking nâng chất lượng kiểm thử (test / 테스트).

> **Chuyển mạch:** Trong **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**, **Deterministic, randomized và nondeterministic hành vi (behavior / 동작)** tiếp nhận điểm tựa từ **Tính đúng đắn (correctness / 정확성) proof không phải hình thức xa rời mã (code / 코드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Online và offline algorithms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deterministic, randomized và nondeterministic hành vi (behavior / 동작)

Deterministic thuật toán (algorithm / 알고리즘) với cùng trạng thái (state / 상태)/đầu vào (input / 입력) cho cùng chuyển tiếp (transition / 전이)/đầu ra (output / 출력). Randomized thuật toán (algorithm / 알고리즘) dùng random choices, nên tính đúng đắn (correctness / 정확성)/hiệu năng (performance / 성능) có thể được mô tả theo xác suất (probability / 확률). QuickSort chọn random pivot có expected `O(n log n)` dù worst trường hợp (case / 사례) vẫn `O(n²)`.

Tính đồng thời (concurrency / 동시성) tạo hành vi (behavior / 동작) có vẻ nondeterministic vì scheduling khác nhau, dù mỗi luồng thực thi (thread / 스레드) có mã (code / 코드) deterministic. Đây là lý do tính đúng đắn (correctness / 정확성) concurrent các hệ thống (systems / 시스템들) cần lập luận (reasoning / 추론) về interleavings hoặc higher-level bộ nhớ (memory / 메모리) các mô hình (models / 모델들).

> **Chuyển mạch:** Ở chặng này của **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**, **Online và offline algorithms** tiếp nhận điểm tựa từ **Deterministic, randomized và nondeterministic hành vi (behavior / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính xác (exact / 정확한), approximation và heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Online và offline algorithms

Offline thuật toán (algorithm / 알고리즘) thấy toàn đầu vào (input / 입력) trước khi xử lý. Online thuật toán (algorithm / 알고리즘) nhận đầu vào (input / 입력) dần và phải quyết định khi chưa biết tương lai. bộ nhớ đệm (cache / 캐시) replacement, streaming, scheduling và tỷ lệ (rate / 비율) limiting thường có tính online.

Sự khác biệt này thay đổi specification và benchmark. Một thuật toán (algorithm / 알고리즘) optimal khi biết toàn future có thể không implementable trong real-time hệ thống (system / 시스템).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**, **Chính xác (exact / 정확한), approximation và heuristic** tiếp nhận điểm tựa từ **Online và offline algorithms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính xác (exact / 정확한), approximation và heuristic

Không phải bài toán (problem / 문제) nào cũng cần chính xác (exact / 정확한) optimum. Approximation thuật toán (algorithm / 알고리즘) có guarantee về độ gần optimal; heuristic ưu tiên hiệu quả thực nghiệm nhưng thường không có guarantee mạnh. tìm kiếm (search / 검색) engine ranking, trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) và tuyến (route / 경로) planning có thể dùng heuristics vì trạng thái (state / 상태) không gian (space / 공간) khổng lồ.

Điều quan trọng là đừng gọi heuristic là “thuật toán (algorithm / 알고리즘) sai”. Nếu specification chấp nhận approximate solution, nó vẫn có thể đúng theo đặc tả hợp đồng (contract / 계약). Sai là khi guarantees bị hiểu quá mức.

> **Chuyển mạch:** Trong **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Chính xác (exact / 정확한), approximation và heuristic** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Một thuật toán (algorithm / 알고리즘) tốt không bắt đầu từ mã (code / 코드). Hãy xác định **đầu vào (input / 입력) lĩnh vực (domain / 도메인) → trạng thái (state / 상태) → Allowed transitions → bất biến (invariant / 불변식) → Termination → đầu ra (output / 출력) thuộc tính (property / 속성) → tài nguyên (resource / 자원) chi phí (cost / 비용)**. mã (code / 코드) chỉ là một biểu diễn (representation / 표현) của chuỗi lập luận (reasoning / 추론) đó.

> **Chuyển mạch:** Ở chặng này của **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Chạy qua kiểm thử (test / 테스트) cases là chứng minh đúng.”** kiểm thử (test / 테스트) chỉ cover sampled executions. Nó có thể cho confidence nhưng không chứng minh universal thuộc tính (property / 속성) trừ khi lĩnh vực (domain / 도메인) hữu hạn và được exhaust.

**“Nếu độ phức tạp (complexity / 복잡도) tốt thì thuật toán (algorithm / 알고리즘) tốt.”** thuật toán (algorithm / 알고리즘) sai specification với `O(1)` vẫn vô dụng. tính đúng đắn (correctness / 정확성), các ràng buộc (constraints / 제약조건들) và maintainability đến trước micro-optimization.

**“Recursion luôn chậm.”** Recursion là cách mô tả decomposition. hiệu năng (performance / 성능) phụ thuộc lời gọi (call / 호출) overhead, tối ưu hóa (optimization / 최적화), dữ liệu (data / 데이터) truy cập (access / 접근) và algorithmic cấu trúc (structure / 구조); iterative form không tự động đổi độ phức tạp (complexity / 복잡도) lớp (class / 클래스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Algorithmic thinking, specification và tính đúng đắn (correctness / 정확성)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Tính đúng đắn (correctness / 정확성) dựa trên [logic, state và invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md). Sau khi biết procedure đúng, bước tiếp theo là hỏi [nó tốn bao nhiêu time/space](./01_complexity_and_asymptotic_analysis.md), rồi cách [data layout](./02_memory_models_and_data_layout.md) làm chi phí lý thuyết gặp hardware thật.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
