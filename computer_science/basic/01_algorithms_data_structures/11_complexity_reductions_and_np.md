# Độ phức tạp (complexity / 복잡도), reductions và NP

> **Mạch đọc:** Đọc **độ phức tạp (complexity / 복잡도), reductions và NP** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **bài toán (problem / 문제) khác thuật toán (algorithm / 알고리즘)** sang **quyết định (decision / 결정) problems như dạng chuẩn để lập luận (reasoning / 추론)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Big-O trả lời “thời gian chạy (runtime / 런타임) tăng thế nào với đầu vào (input / 입력) kích thước (size / 크기)”, nhưng độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) hỏi sâu hơn: **một bài toán (problem / 문제) về bản chất cần bao nhiêu tài nguyên để giải, và các problems liên hệ với nhau qua khả năng chuyển đổi như thế nào?** Đây là nơi xuất hiện P, NP, NP-hard, reductions và lower bounds.

## Bài toán (problem / 문제) khác thuật toán (algorithm / 알고리즘)

Một thuật toán (algorithm / 알고리즘) là một procedure cụ thể. Một computational bài toán (problem / 문제) là tập mọi instances và đầu ra (output / 출력) hợp lệ tương ứng. Sorting là bài toán (problem / 문제); merge sort và quicksort là algorithms.

Độ phức tạp (complexity / 복잡도) lớp (class / 클래스) phân loại problems, không phân loại một đoạn mã (code / 코드) cụ thể. Khi nói SAT thuộc NP, ta đang nói về quyết định (decision / 결정) bài toán (problem / 문제) Boolean satisfiability, không phải hiệu năng (performance / 성능) của một hiện thực (implementation / 구현) SAT solver cụ thể.


> **Chuyển mạch:** Từ **bài toán (problem / 문제) khác thuật toán (algorithm / 알고리즘)**, ta sang **quyết định (decision / 결정) problems như dạng chuẩn để lập luận (reasoning / 추론)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Quyết định (decision / 결정) problems như dạng chuẩn để lập luận (reasoning / 추론)

Nhiều tối ưu hóa (optimization / 최적화) problems có thể chuyển sang quyết định (decision / 결정) form. Thay vì “tìm tuyến (route / 경로) ngắn nhất”, hỏi “có tuyến (route / 경로) dài không quá K hay không?”. quyết định (decision / 결정) form giúp định nghĩa classes và reductions sạch hơn.

Điều này không có nghĩa practical software chỉ dùng yes/no. Nó là lớp trừu tượng (abstraction / 추상화) lý thuyết để so sánh difficulty.


> **Chuyển mạch:** Từ **quyết định (decision / 결정) problems như dạng chuẩn để lập luận (reasoning / 추론)**, ta sang **P: giải được trong polynomial thời gian (time / 시간)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## P: giải được trong polynomial thời gian (time / 시간)

P chứa quyết định (decision / 결정) problems có deterministic thuật toán (algorithm / 알고리즘) chạy polynomial thời gian (time / 시간) theo đầu vào (input / 입력) kích thước (size / 크기), ví dụ `O(n)`, `O(n²)`, `O(n^5)`.

Polynomial không đồng nghĩa “nhanh trong thực tế”. `n^100` là polynomial nhưng vô dụng cho đầu vào (input / 입력) vừa phải. P chủ yếu biểu thị một ranh giới (boundary / 경계) lý thuyết giữa growth polynomial và nhiều dạng combinatorial explosion.


> **Chuyển mạch:** Từ **P: giải được trong polynomial thời gian (time / 시간)**, ta sang **NP: solution có thể verify nhanh** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## NP: solution có thể verify nhanh

NP chứa quyết định (decision / 결정) problems mà nếu ai đó đưa một certificate cho answer YES, ta có thể verify certificate trong polynomial thời gian (time / 시간).

Ví dụ với Hamiltonian cycle, certificate là một thứ tự vertices. Verifier kiểm tra mỗi vertex xuất hiện đúng một lần và consecutive vertices có edges phù hợp.

> NP không có nghĩa “non-polynomial”. Tên lịch sử là nondeterministic polynomial thời gian (time / 시간).

Mọi bài toán (problem / 문제) trong P cũng thuộc NP vì nếu tự giải nhanh được thì tất nhiên có thể verify nhanh.


> **Chuyển mạch:** Từ **NP: solution có thể verify nhanh**, ta sang **Reduction: dùng bài toán (problem / 문제) A để biểu diễn bài toán (problem / 문제) B** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Reduction: dùng bài toán (problem / 문제) A để biểu diễn bài toán (problem / 문제) B

Polynomial-time reduction từ A sang B nghĩa là có transformation polynomial thời gian (time / 시간) biến instance của A thành instance của B sao cho answer được bảo toàn.

Nếu A reduce sang B, ta có thể dùng solver cho B để giải A sau bước transform. Vì vậy B ít nhất “khó như” A theo reduction đó.

Reduction là một trong những ideas xuyên suốt CS: trình biên dịch (compiler / 컴파일러) lowering, serialization, truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리) rewriting và giao thức (protocol / 프로토콜) translation đều có bóng dáng “đổi biểu diễn (representation / 표현) nhưng bảo toàn meaning”, dù formal reduction trong độ phức tạp (complexity / 복잡도) có definition chặt hơn.


> **Chuyển mạch:** Từ **Reduction: dùng bài toán (problem / 문제) A để biểu diễn bài toán (problem / 문제) B**, ta sang **NP-hard và NP-complete** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## NP-hard và NP-complete

Một bài toán (problem / 문제) là NP-hard nếu mọi bài toán (problem / 문제) trong NP có thể polynomial-time reduce sang nó. Nó không nhất thiết thuộc NP hoặc thậm chí là quyết định (decision / 결정) bài toán (problem / 문제).

Một bài toán (problem / 문제) là NP-complete nếu vừa thuộc NP vừa NP-hard. SAT là bài toán (problem / 문제) NP-complete lịch sử đầu tiên qua Cook–Levin theorem.

Để chứng minh bài toán (problem / 문제) X NP-complete, mẫu (pattern / 패턴) điển hình là: chứng minh X ∈ NP, rồi chọn một bài toán (problem / 문제) Y đã biết NP-complete và reduce **Y → X**.

Hướng reduction thường bị nhầm. Nếu reduce X → Y, điều đó chỉ cho thấy Y ít nhất khó như X, không chứng minh X khó.


> **Chuyển mạch:** Từ **NP-hard và NP-complete**, ta sang **P versus NP** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## P versus NP

Câu hỏi P = NP hay không vẫn chưa được giải quyết. Nếu P = NP, mọi bài toán (problem / 문제) có certificate verify polynomial cũng có thể solve polynomial về mặt asymptotic. Nếu P ≠ NP, tồn tại problems verify nhanh nhưng solve không có polynomial thuật toán (algorithm / 알고리즘).

Không nên suy diễn rằng “NP-complete nghĩa là không thể giải”. Instances nhỏ, cấu trúc (structure / 구조) đặc biệt, parameterization, approximation, heuristics và exponential algorithms tối ưu hóa vẫn có thể cực kỳ hữu ích.

SAT solvers hiện đại giải nhiều industrial instances rất lớn vì real-world cấu trúc (structure / 구조) khác worst-case adversarial instances.


> **Chuyển mạch:** Từ **P versus NP**, ta sang **Lower bounds và comparison sorting** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Lower bounds và comparison sorting

Một lower bound nói không thuật toán (algorithm / 알고리즘) nào trong mô hình (model / 모델) nhất định có thể vượt một chi phí (cost / 비용) asymptotic nào đó.

Comparison-based sorting có lower bound `Ω(n log n)` comparisons vì có `n!` permutations và mỗi comparison phân nhánh tối đa hai outcomes. cây quyết định (decision tree / 의사결정 트리) phải có ít nhất `n!` leaves, nên height ít nhất `log₂(n!) = Ω(n log n)`.

Counting sort có thể `O(n+k)` vì nó không bị giới hạn trong comparison mô hình (model / 모델); nó khai thác cấu trúc (structure / 구조) của keys. Vì vậy lower bound luôn phụ thuộc computational mô hình (model / 모델) và các giả định (assumptions / 가정들).


> **Chuyển mạch:** Từ **Lower bounds và comparison sorting**, ta sang **Parameterized độ phức tạp (complexity / 복잡도)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Parameterized độ phức tạp (complexity / 복잡도)

Có bài toán (problem / 문제) exponential theo `n` nhưng practical nếu một parameter `k` nhỏ. Fixed-parameter tractable (FPT) algorithms có form như `f(k) * poly(n)`.

Cách nhìn này quan trọng trong practice: difficulty không chỉ phụ thuộc raw đầu vào (input / 입력) kích thước (size / 크기) mà còn cấu trúc instance.


> **Chuyển mạch:** Từ **Parameterized độ phức tạp (complexity / 복잡도)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“NP là các bài toán cần exponential thời gian (time / 시간).”** Chưa biết điều đó cho mọi NP-complete bài toán (problem / 문제); chính P vs NP hỏi liệu polynomial algorithms có tồn tại hay không.

**“NP-hard nghĩa là không giải được.”** Nó nói về worst-case độ phức tạp (complexity / 복잡도) dưới reductions, không cấm practical solvers, approximation hay special cases.

**“Một thuật toán (algorithm / 알고리즘) O(n²) luôn tốt hơn O(2^n).”** Với đầu vào (input / 입력) nhỏ và constants khác nhau, không nhất thiết. độ phức tạp (complexity / 복잡도) mô tả scaling, không thay benchmark.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) không chỉ hỏi “thuật toán (algorithm / 알고리즘) này tốn bao lâu”, mà xây bản đồ giữa problems: bài toán (problem / 문제) nào biến được thành bài toán (problem / 문제) nào, ranh giới (boundary / 경계) tài nguyên nằm ở đâu, và limitation nào đến từ bản chất chứ không phải hiện thực (implementation / 구현) yếu.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc cùng [asymptotic analysis](./01_complexity_and_asymptotic_analysis.md), [algorithmic strategies](./08_algorithmic_strategies.md) và [randomized/approximation algorithms](./10_randomized_approximation_and_online_algorithms.md). Nền lô-gic (logic / 논리)/computability nằm tại [Computability](../00_computation_information/04_computability_and_limits.md) và [Automata/Formal Languages](../../../mathematics/07_discrete_cs/07_automata_formal_languages_and_computability.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 algorithmic thinking and correctness](./00_algorithmic_thinking_and_correctness.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
