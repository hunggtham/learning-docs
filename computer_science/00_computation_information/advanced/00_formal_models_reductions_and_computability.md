# Formal các mô hình (models / 모델들), reductions và computability

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Formal các mô hình (models / 모델들), reductions và computability**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình (model / 모델) of computation là một hợp đồng lập luận (reasoning / 추론)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Ánh xạ (mapping / 매핑) reduction như công cụ truyền độ khó** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Ở foundation, computability trả lời câu hỏi “có thuật toán (algorithm / 알고리즘) tổng quát nào luôn giải được bài toán (problem / 문제) này hay không?”. Ở mức advanced, điều quan trọng hơn là **cách chứng minh một giới hạn** và cách chuyển giới hạn đã biết từ bài toán (problem / 문제) này sang bài toán (problem / 문제) khác.

## Mô hình (model / 모델) of computation là một hợp đồng lập luận (reasoning / 추론)

Một computation mô hình (model / 모델) xác định trạng thái (state / 상태) nào tồn tại, thao tác (operation / 연산) nào được phép và một bước computation nghĩa là gì. Turing machine, lambda calculus, register machine và general-purpose programming languages có hình thức khác nhau nhưng nhiều mô hình (model / 모델) có cùng sức biểu đạt computability dưới các giả định chuẩn.

Điều này cho phép ta tách hai tầng: **expressive power** và **chi phí (cost / 비용) mô hình (model / 모델)**. Hai languages đều Turing-complete nhưng có thể khác rất xa về bộ nhớ (memory / 메모리) an toàn (safety / 안전), hiệu năng (performance / 성능) mô hình (model / 모델), tính đồng thời (concurrency / 동시성) ngữ nghĩa (semantics / 의미론) hay khả năng xác minh (verification / 확인). Turing-equivalence không làm các hiện thực (implementation / 구현) trở nên giống nhau.

> **Chuyển mạch:** Computation model đặt contract cho machine và input; mapping reduction truyền độ khó giữa bài toán, còn halting problem là nguồn chuẩn để chứng minh giới hạn đó.

## Ánh xạ (mapping / 매핑) reduction như công cụ truyền độ khó

Giả sử bài toán (problem / 문제) `A` có thể transform thành bài toán (problem / 문제) `B` sao cho answer được bảo toàn. Nếu transformation đủ hiệu quả, solver cho `B` trở thành solver cho `A`. Vì vậy khi `A` đã biết là khó hoặc undecidable, reduction `A → B` có thể chứng minh `B` ít nhất khó tương đương theo loại reduction đó.

Sai lầm phổ biến là nhớ reduction như một “mũi tên độ khó” mà không kiểm tra ngữ nghĩa (semantic / 의미적) preservation. Một reduction đúng phải định nghĩa ánh xạ (mapping / 매핑) trên mọi đầu vào (input / 입력) hợp lệ và chứng minh quan hệ giữa answer của đầu vào (input / 입력) gốc và answer của instance sau transform.

> **Chuyển mạch:** Ở chặng này của **Formal các mô hình (models / 모델들), reductions và computability**, **Ánh xạ (mapping / 매핑) reduction như công cụ truyền độ khó** nêu điều cần giải thích; **Halting bài toán (problem / 문제) là nguồn reduction trung tâm** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Recognizable, decidable và complement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Halting bài toán (problem / 문제) là nguồn reduction trung tâm

Halting bài toán (problem / 문제) hỏi program `P` trên đầu vào (input / 입력) `x` có terminate hay không. Khi muốn chứng minh một thuộc tính (property / 속성) khác undecidable, mẫu (pattern / 패턴) thường là giả sử có decider cho thuộc tính (property / 속성) mới, rồi dùng nó để quyết định halting.

Ví dụ tưởng tượng một công cụ (tool / 도구) `AlwaysTerminatesAfterNetworkRead(program)` quyết định hoàn hảo liệu program sau lần đọc mạng (network / 네트워크) đầu tiên có luôn terminate. Nếu ta có thể encode một arbitrary computation `P(x)` vào phần chương trình sau mạng (network / 네트워크) read, công cụ (tool / 도구) đó có thể bị biến thành halting decider. Chi tiết proof phụ thuộc thuộc tính (property / 속성) cụ thể, nhưng mô hình tư duy (mental model / 사고 모델) là: **nhúng computation chưa biết vào ngữ cảnh (context / 맥락) mà thuộc tính (property / 속성) mới buộc phải tiết lộ answer**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Formal các mô hình (models / 모델들), reductions và computability**, **Halting bài toán (problem / 문제) là nguồn reduction trung tâm** nêu điều cần giải thích; **Recognizable, decidable và complement** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Rice's theorem và static phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Recognizable, decidable và complement

Một ngôn ngữ (language / 언어) decidable nếu có machine luôn halt và trả lời yes/no đúng. Recognizable yếu hơn: với member, machine eventually accept; với non-member, nó có thể reject hoặc chạy mãi.

Nếu một ngôn ngữ (language / 언어) và complement của nó đều recognizable, ta có thể chạy hai recognizers song song theo dovetailing; một bên cuối cùng accept, tạo decider. Đây là một cầu nối (bridge / 브리지) quan trọng giữa existence proof và thực thi (execution / 실행) chiến lược (strategy / 전략).

> **Chuyển mạch:** Trong **Formal các mô hình (models / 모델들), reductions và computability**, **Rice's theorem và static phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **Recognizable, decidable và complement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Computability khác độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rice's theorem và static phân tích (analysis / 분석)

Rice's theorem nói, ở mức khái quát, mọi non-trivial ngữ nghĩa (semantic / 의미적) thuộc tính (property / 속성) của partial functions được tính bởi programs trong mô hình (model / 모델) đủ mạnh đều undecidable. Điều này không khiến static phân tích (analysis / 분석) “vô ích”. Nó giải thích tại sao analyzers thực tế phải chọn một trong các chiến lược: giới hạn ngôn ngữ (language / 언어), giới hạn thuộc tính (property / 속성), chấp nhận approximation, dùng annotations/contracts, hoặc cho phép false positive/false negative.

Abstract interpretation là ví dụ điển hình: thay vì execute trên trạng thái (state / 상태) không gian (space / 공간) thật vô hạn, analyzer chạy trên abstract lĩnh vực (domain / 도메인) nhỏ hơn và thiết kế transfer functions để bảo toàn guarantee cần thiết. Precision tăng thường kéo theo chi phí (cost / 비용) tăng; termination của phân tích (analysis / 분석) lại trở thành một kỹ thuật (engineering / 엔지니어링) ràng buộc (constraint / 제약조건).

> **Chuyển mạch:** Ở chặng này của **Formal các mô hình (models / 모델들), reductions và computability**, **Computability khác độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **Rice's theorem và static phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi nào formal limit hữu ích trong công việc?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Computability khác độ phức tạp (complexity / 복잡도)

Một bài toán (problem / 문제) decidable vẫn có thể không practical. Sau khi biết thuật toán (algorithm / 알고리즘) tồn tại, câu hỏi tiếp theo là lượng thời gian (time / 시간)/không gian (space / 공간) cần thiết. Đây là nơi reductions tiếp tục được dùng trong độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론), nhưng loại reduction và tài nguyên (resource / 자원) bound trở nên quan trọng hơn.

Một proof undecidability nói không có thuật toán (algorithm / 알고리즘) tổng quát theo mô hình (model / 모델). Một NP-hardness proof không nói bài toán (problem / 문제) “không giải được”; nó đặt bài toán (problem / 문제) vào quan hệ worst-case độ phức tạp (complexity / 복잡도) với các bài toán (problem / 문제) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Formal các mô hình (models / 모델들), reductions và computability**, **Computability khác độ phức tạp (complexity / 복잡도)** đã nêu tiêu chí phân biệt, còn **Khi nào formal limit hữu ích trong công việc?** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi nào formal limit hữu ích trong công việc?

Formal limits giúp tránh mục tiêu bất khả thi. Một “perfect bug detector cho mọi program”, “công cụ (tool / 도구) luôn biết yêu cầu (request / 요청) nào sẽ deadlock”, hay “analyzer luôn suy ra chính xác mọi hành vi thời gian chạy (runtime behavior / 런타임 동작)” có thể đụng undecidability. Thiết kế tốt chuyển câu hỏi sang subset có cấu trúc: finite-state giao thức (protocol / 프로토콜), bounded mô hình (model / 모델), restricted kiểu (type / 타입)/tác động (effect / 효과) hệ thống (system / 시스템), symbolic thực thi (execution / 실행) với cutoff, hoặc thời gian chạy (runtime / 런타임) monitoring.

> **Chuyển mạch:** Trong **Formal các mô hình (models / 모델들), reductions và computability**, **Khi nào formal limit hữu ích trong công việc?** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Advanced computability không phải học thêm tên theorem. Nó là kỹ năng chọn mô hình (model / 모델), định nghĩa thuộc tính (property / 속성), xây reduction và phân biệt ba câu hỏi: **có giải được không, giải với tài nguyên (resource / 자원) nào, và hiện thực (implementation / 구현) thực tế có đáng dùng không**.

> **Chuyển mạch:** Ở chặng này của **Formal các mô hình (models / 모델들), reductions và computability**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc lại [Computability foundation](../../basic/00_computation_information/04_computability_and_limits.md), rồi nối sang [Complexity & reductions](../../basic/01_algorithms_data_structures/11_complexity_reductions_and_np.md) và phần advanced về ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) khi nghiên cứu static phân tích (analysis / 분석) hoặc xác minh (verification / 확인).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
