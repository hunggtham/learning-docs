# Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Polynomial và exponential khác nhau về bản chất tăng trưởng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Đầu vào (input / 입력) length và giá trị số** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Reductions, NP-Completeness & Approximation / 환원, NP-완전, 근사 알고리즘**

DSA không chỉ dạy cách làm một thuật toán nhanh hơn. Một mức trưởng thành quan trọng là nhận ra khi bản chất bài toán đã khó tới mức việc tiếp tục đổi `ArrayList` thành `HashMap`, hoặc tối ưu `O(n²)` thành `O(n log n)`, không còn giải quyết nút thắt chính.

Khi đó câu hỏi chuyển từ:

> “Làm sao tối ưu hiện thực (implementation / 구현) này?”

sang:

> “Bài toán tổng quát có cấu trúc hardness nào? Có special trường hợp (case / 사례) dễ hơn không? Parameter nào nhỏ? Có thể dùng chính xác (exact / 정확한) exponential thuật toán (algorithm / 알고리즘) thông minh, approximation, heuristic hoặc solver chuyên dụng không?”

Mục tiêu chương này là dùng độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) như một **công cụ kỹ thuật (engineering / 엔지니어링)**, không phải danh sách thuật ngữ để học thuộc.

## Polynomial và exponential khác nhau về bản chất tăng trưởng

`O(n³)` có thể chậm, nhưng vẫn polynomial. `O(2^n)` có tốc độ tăng khác hẳn: tăng `n` thêm 1 có thể gần như nhân đôi số trạng thái.

```text
2^20 ≈ 1 triệu
2^30 ≈ 1 tỷ
2^40 ≈ 1 nghìn tỷ
```

Điều này không có nghĩa exponential luôn vô dụng. Nếu parameter thực tế chỉ 20–30, hoặc pruning rất mạnh, chính xác (exact / 정확한) exponential thuật toán (algorithm / 알고리즘) có thể là lựa chọn tốt nhất.

Điều cần nhớ là **đầu vào (input / 입력) kích thước (size / 크기) thực** đôi khi không phải chỉ một biến `n`; độ lớn số được mã hóa bằng bao nhiêu bit cũng quan trọng.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Đầu vào (input / 입력) length và giá trị số** tiếp nhận điểm tựa từ **Polynomial và exponential khác nhau về bản chất tăng trưởng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quyết định (decision / 결정) bài toán (problem / 문제) và tối ưu hóa (optimization / 최적화) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đầu vào (input / 입력) length và giá trị số

Giả sử sức chứa (capacity / 용량) `W = 1,000,000`. Giá trị `W` cần chỉ khoảng `log₂ W` bit để biểu diễn.

Một thuật toán (algorithm / 알고리즘) `O(nW)` là polynomial theo **giá trị số** `W`, nhưng không polynomial theo **độ dài encoding** `log W`.

Đây là nguồn gốc khái niệm **giả đa thức (pseudo-polynomial)**.

Phân biệt này giải thích vì sao một bài NP-hard vẫn có DP rất thực dụng khi numeric parameter nhỏ.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Quyết định (decision / 결정) bài toán (problem / 문제) và tối ưu hóa (optimization / 최적화) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **Đầu vào (input / 입력) length và giá trị số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lớp (class / 클래스) P** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyết định (decision / 결정) bài toán (problem / 문제) và tối ưu hóa (optimization / 최적화) bài toán (problem / 문제)

Độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) thường mô tả **quyết định (decision / 결정) bài toán (problem / 문제)** với đầu ra yes/no.

Tối ưu hóa (optimization / 최적화) TSP:

> Tour ngắn nhất dài bao nhiêu?

Quyết định (decision / 결정) TSP:

> Có tour đi qua mọi đỉnh với tổng chi phí `<= B` không?

Nếu giải tối ưu hóa (optimization / 최적화) được, quyết định (decision / 결정) thường dễ suy ra. Ngược lại, trong nhiều bài, tối ưu hóa (optimization / 최적화) có thể được dựng từ quyết định (decision / 결정) qua repeated queries hoặc tìm kiếm nhị phân (binary search / 이진 탐색) nếu mục tiêu (objective / 목표) có miền thích hợp.

Việc chuyển sang quyết định (decision / 결정) phiên bản (version / 버전) giúp định nghĩa lớp P/NP và reduction rõ ràng hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Lớp (class / 클래스) P** tiếp nhận điểm tựa từ **Quyết định (decision / 결정) bài toán (problem / 문제) và tối ưu hóa (optimization / 최적화) bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lớp (class / 클래스) NP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lớp (class / 클래스) P

**P** là lớp quyết định (decision / 결정) problems có deterministic polynomial-time thuật toán (algorithm / 알고리즘) trong mô hình tính toán chuẩn.

Ví dụ quen thuộc:

```text
shortest path
minimum spanning tree
maximum flow
bipartite matching
2-SAT
```

“Polynomial” không đồng nghĩa “luôn nhanh”. `O(n^10)` vẫn polynomial nhưng có thể không practical. P là khái niệm về tốc độ tăng lý thuyết, không phải SLA môi trường vận hành (production / 운영 환경).

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Lớp (class / 클래스) NP** tiếp nhận điểm tựa từ **Lớp (class / 클래스) P** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NP-hard và NP-complete** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lớp (class / 클래스) NP

**NP** là lớp quyết định (decision / 결정) problems mà với một instance có đáp án “yes”, tồn tại một **certificate** có thể được verify trong polynomial thời gian (time / 시간).

Ví dụ Hamiltonian Cycle: certificate là một thứ tự các đỉnh. xác minh (verification / 확인) chỉ cần kiểm tra mỗi đỉnh xuất hiện đúng quy tắc và mọi cạnh liên tiếp tồn tại.

NP không có nghĩa “not polynomial” hay “không giải được”. Ta biết:

\[
P\subseteq NP
\]

vì nếu solve được polynomial thì hiển nhiên verify cũng polynomial.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **NP-hard và NP-complete** tiếp nhận điểm tựa từ **Lớp (class / 클래스) NP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NP-complete không có nghĩa mọi instance đều khó** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NP-hard và NP-complete

**NP-hard** nghĩa bài toán ít nhất khó như mọi bài trong NP dưới một notion reduction phù hợp.

**NP-complete** nghĩa:

```text
problem ∈ NP
và
problem là NP-hard
```

Nếu có polynomial-time thuật toán (algorithm / 알고리즘) cho một NP-complete bài toán (problem / 문제), thì suy ra mọi bài toán (problem / 문제) trong NP có polynomial-time thuật toán (algorithm / 알고리즘).

Điểm kỹ thuật (engineering / 엔지니어링) quan trọng không phải tranh luận lý thuyết, mà là: khi nhận ra bài toán tương đương một NP-hard cốt lõi (core / 핵심) quen thuộc, ta phải đổi chiến lược giải.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **NP-complete không có nghĩa mọi instance đều khó** tiếp nhận điểm tựa từ **NP-hard và NP-complete** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reduction: ngôn ngữ để so sánh độ khó** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NP-complete không có nghĩa mọi instance đều khó

Hardness là phát biểu về lớp đầu vào (input / 입력) tổng quát và worst-case.

Instance thực tế có thể dễ vì:

```text
n nhỏ
parameter nhỏ
graph sparse
constraint rất chặt
cấu trúc gần cây
treewidth nhỏ
numeric range nhỏ
dữ liệu có geometry đặc biệt
solver heuristic rất phù hợp
```

Vì vậy “bài này NP-hard” không phải điểm kết thúc. Nó là tín hiệu để hỏi: **cấu trúc (structure / 구조) nào của instance thực tế có thể khai thác?**

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **NP-complete không có nghĩa mọi instance đều khó** đã nêu tiêu chí phân biệt, còn **Reduction: ngôn ngữ để so sánh độ khó** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Reduction cần chứng minh hai chiều ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reduction: ngôn ngữ để so sánh độ khó

Một polynomial-time reduction từ `A` sang `B` biến instance `x` của A thành `f(x)` của B sao cho:

\[
x\in A \iff f(x)\in B
\]

và `f` tính được trong polynomial thời gian (time / 시간).

Ký hiệu:

\[
A\le_p B
\]

Nếu A đã biết hard và `A <=p B`, thì B ít nhất hard như A.

### Direction rất dễ nhầm

Muốn chứng minh `B` hard, phải biến **bài đã biết hard A thành B**.

```text
known hard A  ->  target B
```

Nếu chỉ biết cách biến B thành A, điều đó cho thấy có thể dùng solver A để giải B; nó không chứng minh B hard.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Reduction: ngôn ngữ để so sánh độ khó** đã nêu tiêu chí phân biệt, còn **Reduction cần chứng minh hai chiều ngữ nghĩa (semantics / 의미론)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Reduction không chỉ dùng để chứng minh hardness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reduction cần chứng minh hai chiều ngữ nghĩa (semantics / 의미론)

Một reduction đúng thường cần:

```text
A yes -> B yes
B yes -> A yes
```

Nếu chỉ chứng minh một chiều, transformation có thể tạo thêm lời giải giả hoặc làm mất lời giải hợp lệ.

Ngoài ra cần chứng minh transformation chạy polynomial và kích thước instance mới không phình exponential.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Reduction không chỉ dùng để chứng minh hardness** tiếp nhận điểm tựa từ **Reduction cần chứng minh hai chiều ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SAT như ngôn ngữ ràng buộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reduction không chỉ dùng để chứng minh hardness

Trong thuật toán (algorithm / 알고리즘) thiết kế (design / 설계), reduction là kỹ năng cực kỳ tích cực:

```text
assignment                 -> bipartite matching
2-SAT                      -> implication graph + SCC
subtree query              -> Euler Tour + range query
difference constraints     -> shortest path
circulation                -> flow
interval overlap           -> sweep line
```

Khi reduce được bài mới về một thành phần nguyên thủy (primitive / 기본 요소) đã hiểu, ta tái sử dụng cả thuật toán (algorithm / 알고리즘), proof và hiện thực (implementation / 구현) mẫu (pattern / 패턴).

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **SAT như ngôn ngữ ràng buộc** tiếp nhận điểm tựa từ **Reduction không chỉ dùng để chứng minh hardness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3-SAT và 2-SAT: thay một chi tiết, landscape thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SAT như ngôn ngữ ràng buộc

SAT hỏi liệu có assignment Boolean làm công thức đúng hay không.

CNF là conjunction của nhiều clause; mỗi clause là disjunction của literals.

Ví dụ:

\[
(x\lor \neg y\lor z)\land(\neg x\lor y)
\]

SAT quan trọng vì rất nhiều bài combinatorial có thể encode thành Boolean các ràng buộc (constraints / 제약조건들).

Hiện đại (modern / 현대적) SAT solver dùng nhiều kỹ thuật mạnh như propagation, clause học tập (learning / 학습) và branching heuristics, nên nhiều instance lớn có thể giải rất nhanh dù worst-case vẫn exponential.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **3-SAT và 2-SAT: thay một chi tiết, landscape thay đổi** tiếp nhận điểm tựa từ **SAT như ngôn ngữ ràng buộc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Clique, Independent Set và Vertex Cover** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3-SAT và 2-SAT: thay một chi tiết, landscape thay đổi

3-SAT vẫn NP-complete.

2-SAT lại giải được polynomial bằng implication đồ thị (graph / 그래프).

Clause:

\[
(a\lor b)
\]

suy ra:

```text
¬a -> b
¬b -> a
```

Formula satisfiable khi không biến nào nằm cùng SCC với phủ định của chính nó.

Bài học cực kỳ quan trọng:

> Một restriction nhỏ của bài toán (problem / 문제) có thể biến bài tổng quát hard thành special trường hợp (case / 사례) dễ.

Do đó luôn tìm cấu trúc đặc biệt trước khi áp một solver tổng quát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Clique, Independent Set và Vertex Cover** tiếp nhận điểm tựa từ **3-SAT và 2-SAT: thay một chi tiết, landscape thay đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Knapsack và pseudo-polynomial DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Clique, Independent Set và Vertex Cover

Trong đồ thị vô hướng:

\[
S\văn bản (text / 텍스트){ là independent set}\iff V\setminus S\văn bản (text / 텍스트){ là vertex cover}
\]

Và `S` là clique trong `G` khi và chỉ khi `S` là independent set trong complement đồ thị (graph / 그래프) `\bar G`.

Ba bài tưởng khác nhau nhưng liên kết chặt qua complement và set complement.

Những quan hệ này giúp rèn khả năng nhìn “cùng một ràng buộc dưới biểu diễn khác”.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Knapsack và pseudo-polynomial DP** tiếp nhận điểm tựa từ **Clique, Independent Set và Vertex Cover** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weakly và strongly NP-hard: trực giác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Knapsack và pseudo-polynomial DP

0/1 Knapsack có DP dạng:

```text
dp[capacity]
```

với thời gian chạy (runtime / 런타임) `O(nW)`.

Nếu `W` nhỏ, đây là cách cực kỳ thực dụng. Nếu `W` được biểu diễn bằng nhiều bit và rất lớn, `O(nW)` có thể exponential theo đầu vào (input / 입력) encoding length.

Đây là lý do Knapsack vừa có hardness lý thuyết (theory / 이론) vừa có DP nổi tiếng mà không mâu thuẫn.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Weakly và strongly NP-hard: trực giác** tiếp nhận điểm tựa từ **Knapsack và pseudo-polynomial DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính xác (exact / 정확한) exponential thuật toán (algorithm / 알고리즘) vẫn rất có giá trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weakly và strongly NP-hard: trực giác

Một số bài toán (problem / 문제) hard chủ yếu vì numeric values có thể rất lớn và có pseudo-polynomial thuật toán (algorithm / 알고리즘). Đây là kiểu hardness yếu hơn về mặt cấu trúc.

Strongly NP-hard problems vẫn hard ngay cả khi numeric values được giới hạn polynomial theo đầu vào (input / 입력) kích thước (size / 크기), nên pseudo-polynomial chiến lược (strategy / 전략) không giải quyết bản chất tương tự.

Không cần nhớ toàn bộ taxonomy; điều cần học là **numeric magnitude có thể là một parameter ẩn của độ phức tạp (complexity / 복잡도)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Chính xác (exact / 정확한) exponential thuật toán (algorithm / 알고리즘) vẫn rất có giá trị** tiếp nhận điểm tựa từ **Weakly và strongly NP-hard: trực giác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Meet-in-the-middle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính xác (exact / 정확한) exponential thuật toán (algorithm / 알고리즘) vẫn rất có giá trị

Toolbox chính xác (exact / 정확한) gồm:

```text
backtracking
branch and bound
bitmask DP
meet-in-the-middle
subset DP
SAT/SMT/ILP/CP-SAT
parameterized algorithm
```

Nếu `n=25`, một `2^n` thuật toán (algorithm / 알고리즘) tốt có thể hoàn toàn hợp lý. Nếu nghiệp vụ (business / 비즈니스) yêu cầu chính xác (exact / 정확한) kết quả (result / 결과), approximation có thể không chấp nhận được.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Meet-in-the-middle** tiếp nhận điểm tựa từ **Chính xác (exact / 정확한) exponential thuật toán (algorithm / 알고리즘) vẫn rất có giá trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bitmask DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Meet-in-the-middle

Tách `n` phần tử thành hai nửa.

Thay vì duyệt:

\[
2^n
\]

ta duyệt khoảng:

\[
2^{n/2}+2^{n/2}
\]

rồi kết hợp bằng sort, băm (hash / 해시) hoặc tìm kiếm nhị phân (binary search / 이진 탐색).

Subset Sum với `n≈40` là ví dụ kinh điển.

Meet-in-the-middle đổi thêm bộ nhớ (memory / 메모리) để giảm exponent của thời gian (time / 시간).

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Bitmask DP** tiếp nhận điểm tựa từ **Meet-in-the-middle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Branch and Bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bitmask DP

TSP Held–Karp:

```text
dp[mask][v] = chi phí nhỏ nhất đi qua tập mask và kết thúc tại v
```

Số trạng thái (state / 상태):

\[
O(n2^n)
\]

và chuyển tiếp (transition / 전이) thường dẫn tới:

\[
O(n^2 2^n)
\]

Nó vẫn exponential, nhưng tốt hơn `n!` brute force rất nhiều.

Điểm sâu hơn là trạng thái (state / 상태) compression: nhiều thứ tự lịch sử khác nhau được gộp nếu chúng có cùng `(mask,v)` và tương lai chỉ phụ thuộc hai thông tin đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Branch and Bound** tiếp nhận điểm tựa từ **Bitmask DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tìm kiếm (search / 검색) thứ tự (ordering / 순서) và incumbent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Branch and Bound

Backtracking loại nhánh khi biết nó infeasible. **Branch and Bound** còn dùng một bound lạc quan về mục tiêu (objective / 목표) tốt nhất có thể đạt từ nhánh.

Với minimization:

```text
if lowerBound(state) >= bestKnown:
    prune
```

Bound phải **an toàn**. Nếu bound quá lạc quan, prune ít. Nếu bound sai theo hướng quá mạnh, có thể cắt mất optimum và phá tính đúng đắn (correctness / 정확성).

Thiết kế bound thường là phần khó nhất.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Tìm kiếm (search / 검색) thứ tự (ordering / 순서) và incumbent** tiếp nhận điểm tựa từ **Branch and Bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ràng buộc (constraint / 제약조건) propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm (search / 검색) thứ tự (ordering / 순서) và incumbent

Branch-and-bound vẫn đúng nếu duyệt nhánh theo thứ tự bất kỳ, nhưng tìm được một lời giải tốt sớm sẽ làm `bestKnown` mạnh hơn và prune được nhiều hơn.

Do đó heuristic thứ tự (ordering / 순서) có thể thay thời gian chạy (runtime / 런타임) thực tế hàng bậc độ lớn mà không thay worst-case độ phức tạp (complexity / 복잡도).

Đây là khác biệt giữa:

```text
correctness guarantee
và
practical search engineering
```

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Ràng buộc (constraint / 제약조건) propagation** tiếp nhận điểm tựa từ **Tìm kiếm (search / 검색) thứ tự (ordering / 순서) và incumbent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Memoization trong tìm kiếm (search / 검색) khó** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ràng buộc (constraint / 제약조건) propagation

Trong CSP/SAT, trước khi branch có thể suy ra các hậu quả bắt buộc.

Nếu một biến chỉ còn một giá trị hợp lệ, gán nó ngay. Nếu assignment khiến clause/đơn vị (unit / 단위)/ràng buộc (constraint / 제약조건) khác bị ép, tiếp tục propagate.

Propagation giúp phát hiện contradiction sớm, làm cây tìm kiếm (search / 검색) nhỏ hơn rất nhiều.

Backtracking “thô” và solver hiện đại khác nhau chủ yếu ở lượng thông tin được suy ra trước khi phải đoán tiếp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Memoization trong tìm kiếm (search / 검색) khó** tiếp nhận điểm tựa từ **Ràng buộc (constraint / 제약조건) propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parameterized độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memoization trong tìm kiếm (search / 검색) khó

Hai nhánh tìm kiếm (search / 검색) khác nhau có thể dẫn tới cùng trạng thái (state / 상태) lô-gic (logic / 논리). Nếu tương lai chỉ phụ thuộc trạng thái (state / 상태), có thể memoize để tránh giải lại.

Đây là cầu nối giữa backtracking và DP.

Một cách nhìn:

```text
backtracking = duyệt cây lịch sử
DP/memoization = gom các lịch sử tương đương thành cùng node trạng thái
```

Nếu số trạng thái (state / 상태) duy nhất nhỏ hơn rất nhiều số đường đi lịch sử, memoization tạo khác biệt lớn.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Parameterized độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **Memoization trong tìm kiếm (search / 검색) khó** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parameter đúng quan trọng hơn label NP-hard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parameterized độ phức tạp (complexity / 복잡도)

Thay vì chỉ hỏi thời gian chạy (runtime / 런타임) theo `n`, ta chọn một parameter `k` phản ánh phần khó.

Một thuật toán (algorithm / 알고리즘) **fixed-parameter tractable (FPT)** có dạng:

\[
f(k)\cdot n^{O(1)}
\]

`f(k)` có thể exponential theo `k`, nhưng nếu `k` nhỏ thì toàn bộ thuật toán (algorithm / 알고리즘) vẫn practical.

Ví dụ mindset:

```text
n rất lớn
nhưng số vertex cần xóa chỉ k=10
```

thì exponential theo `k` có thể tốt hơn exponential theo `n`.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Parameterized độ phức tạp (complexity / 복잡도)** cho ta quy tắc; **Parameter đúng quan trọng hơn label NP-hard** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Kernelization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parameter đúng quan trọng hơn label NP-hard

Một bài toán (problem / 문제) NP-hard theo `n` vẫn có thể dễ khi parameter thực tế nhỏ.

Các parameter thường có ý nghĩa:

```text
solution size
number of conflicts
treewidth
number of machines
number of colors
edit distance
feedback vertex count
```

Kỹ thuật (engineering / 엔지니어링) question nên là:

> Hardness nằm ở chiều nào của instance, và chiều đó trong dữ liệu thật có nhỏ không?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Parameter đúng quan trọng hơn label NP-hard** cho ta quy tắc; **Kernelization** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Treewidth: đồ thị (graph / 그래프) gần cây có thể dễ hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kernelization

Kernelization là preprocessing polynomial-time biến `(instance,k)` thành một instance nhỏ hơn có kích thước bị chặn theo hàm của `k`, đồng thời bảo toàn đáp án.

Mục tiêu là loại bỏ phần dữ liệu chắc chắn không ảnh hưởng bản chất combinatorial khó.

Có thể xem kernelization như **bài toán (problem / 문제) reduction theo parameter** trước khi chạy chính xác (exact / 정확한) tìm kiếm (search / 검색) đắt tiền.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Treewidth: đồ thị (graph / 그래프) gần cây có thể dễ hơn** tiếp nhận điểm tựa từ **Kernelization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Approximation thuật toán (algorithm / 알고리즘)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Treewidth: đồ thị (graph / 그래프) gần cây có thể dễ hơn

Nhiều bài NP-hard trên general đồ thị (graph / 그래프) trở nên dễ hơn trên cây (tree / 트리) hoặc đồ thị (graph / 그래프) có treewidth nhỏ.

Cây (tree / 트리) decomposition cho phép DP trên các “bag” kích thước nhỏ, với exponential factor phụ thuộc treewidth thay vì toàn bộ số đỉnh.

Trực giác:

> Nếu đồ thị (graph / 그래프) có thể được ghép từ các phần nhỏ liên kết với nhau qua ranh giới (boundary / 경계) nhỏ, ta có thể giữ trạng thái (state / 상태) chỉ trên ranh giới (boundary / 경계) đó.

Đây là một ví dụ sâu về việc cấu trúc (structure / 구조) của instance quan trọng hơn tên bài toán tổng quát.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Approximation thuật toán (algorithm / 알고리즘)** tiếp nhận điểm tựa từ **Treewidth: đồ thị (graph / 그래프) gần cây có thể dễ hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vertex Cover 2-approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Approximation thuật toán (algorithm / 알고리즘)

Khi chính xác (exact / 정확한) optimum quá đắt, có thể chấp nhận solution gần optimum với guarantee định lượng.

Với minimization, một `ρ`-approximation thường bảo đảm:

\[
ALG(I)\le \rho\cdot OPT(I)
\]

Với maximization, convention được viết theo hướng phù hợp để đảm bảo giá trị không quá xa optimum.

Điểm quan trọng là approximation thuật toán (algorithm / 알고리즘) có **guarantee trên mọi instance thuộc mô hình**, khác với heuristic chỉ “thường chạy tốt”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Vertex Cover 2-approximation** tiếp nhận điểm tựa từ **Approximation thuật toán (algorithm / 알고리즘)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Set Cover và greedy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vertex Cover 2-approximation

Một thuật toán đơn giản:

```text
while còn cạnh chưa cover:
    chọn một cạnh (u,v)
    đưa cả u và v vào cover
    xóa mọi cạnh incident với u hoặc v
```

Các cạnh được chọn tạo một matching. Mọi vertex cover tối ưu phải lấy ít nhất một endpoint của mỗi cạnh matching, nên nếu matching có `k` cạnh thì optimum ít nhất `k` đỉnh.

Thuật toán (algorithm / 알고리즘) lấy `2k` đỉnh, nên kích thước không quá `2*OPT`.

Ví dụ này cho thấy approximation proof thường cần một **lower bound lên optimum** để so solution của thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Set Cover và greedy** tiếp nhận điểm tựa từ **Vertex Cover 2-approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chỉ số (metric / 지표) TSP và vai trò của triangle inequality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Set Cover và greedy

Greedy Set Cover liên tục chọn tập cover nhiều phần tử chưa được cover nhất trên mỗi đơn vị chi phí theo variant phù hợp.

Nó có logarithmic approximation guarantee trong mô hình chuẩn.

Điểm cần học không phải chỉ công thức guarantee, mà là kỹ thuật proof: mỗi bước phân bổ “giá” cho các phần tử mới được cover và so tổng charge với optimum.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Chỉ số (metric / 지표) TSP và vai trò của triangle inequality** tiếp nhận điểm tựa từ **Set Cover và greedy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PTAS và FPTAS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chỉ số (metric / 지표) TSP và vai trò của triangle inequality

General TSP rất khó approximation tốt, nhưng **chỉ số (metric / 지표) TSP** có thêm triangle inequality:

\[
d(a,c)\le d(a,b)+d(b,c)
\]

Cấu trúc này cho phép dùng MST như lower bound và xây các approximation có guarantee hằng số.

Một restriction toán học nhỏ có thể thay approximation landscape rất mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **PTAS và FPTAS** tiếp nhận điểm tựa từ **Chỉ số (metric / 지표) TSP và vai trò của triangle inequality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Approximation khác heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PTAS và FPTAS

**PTAS**: với mọi `ε>0` cố định, có thuật toán (algorithm / 알고리즘) polynomial theo `n` cho solution trong factor `(1+ε)` thích hợp, nhưng exponent theo `n` có thể phụ thuộc `1/ε`.

**FPTAS** mạnh hơn: thời gian chạy (runtime / 런타임) polynomial cả theo `n` và `1/ε`.

Knapsack có FPTAS nổi tiếng dựa trên scaling DP values.

Tư duy kỹ thuật (engineering / 엔지니어링): `ε` là một knob đổi thời gian chạy (runtime / 런타임) lấy chất lượng solution.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Approximation khác heuristic** tiếp nhận điểm tựa từ **PTAS và FPTAS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cục bộ (local / 로컬) tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Approximation khác heuristic

**Approximation thuật toán (algorithm / 알고리즘)** có worst-case chất lượng (quality / 품질) guarantee.

**Heuristic** có thể rất tốt thực tế nhưng không có guarantee tương tự.

Ví dụ heuristic:

```text
local search
simulated annealing
genetic algorithm
greedy without proof
problem-specific neighborhood search
```

Không nên coi heuristic là “sai”. Chỉ cần gọi đúng bản chất guarantee của nó.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Cục bộ (local / 로컬) tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Approximation khác heuristic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Randomized heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cục bộ (local / 로컬) tìm kiếm (search / 검색)

Bắt đầu từ một solution hợp lệ, liên tục chuyển sang solution hàng xóm tốt hơn.

Câu hỏi thiết kế:

```text
neighborhood là gì?
move cost tính nhanh thế nào?
local optimum có tệ không?
làm sao thoát local optimum?
```

2-opt cho TSP là ví dụ kinh điển: thay hai cạnh bằng hai cạnh khác nếu tour ngắn hơn.

Cục bộ (local / 로컬) tìm kiếm (search / 검색) thường rất mạnh khi cần good solution nhanh trên instance lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Randomized heuristic** tiếp nhận điểm tựa từ **Cục bộ (local / 로컬) tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ILP/MILP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Randomized heuristic

Random restart hoặc randomized neighborhood giúp tránh bị kẹt cùng cục bộ (local / 로컬) optimum.

Khi dùng randomness, nên đo phân phối (distribution / 분포) của solution chất lượng (quality / 품질) và thời gian chạy (runtime / 런타임) thay vì chỉ báo một lần chạy tốt.

Trong môi trường vận hành (production / 운영 환경), reproducibility có thể cần seed được quản lý rõ.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **ILP/MILP** tiếp nhận điểm tựa từ **Randomized heuristic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SAT, SMT và CP-SAT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ILP/MILP

Nhiều bài tối ưu hóa (optimization / 최적화) có thể encode bằng biến và ràng buộc tuyến tính nguyên.

Ví dụ chọn item:

```text
x_i ∈ {0,1}
```

với mục tiêu (objective / 목표) và các ràng buộc (constraints / 제약조건들) tuyến tính.

MILP solver dùng LP relaxation, cutting planes, branch-and-bound/branch-and-cut và nhiều heuristic.

Lợi thế kỹ thuật (engineering / 엔지니어링):

```text
mô hình hóa nhanh
solver trưởng thành
có bound và optimality gap
xử lý nhiều constraint business phức tạp
```

Nhược điểm là hiệu năng (performance / 성능) khó dự đoán theo worst-case và cần solver/tooling phù hợp.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **SAT, SMT và CP-SAT** tiếp nhận điểm tựa từ **ILP/MILP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Solver không loại bỏ nhu cầu mô hình hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SAT, SMT và CP-SAT

SAT phù hợp Boolean lô-gic (logic / 논리). SMT thêm lý thuyết (theory / 이론) như integer arithmetic, bit-vectors hoặc arrays. ràng buộc (constraint / 제약조건) Programming/CP-SAT phù hợp scheduling và combinatorial các ràng buộc (constraints / 제약조건들) với propagation mạnh.

Thay vì tự viết backtracking khổng lồ, đôi khi encoding bài toán (problem / 문제) vào solver là cách kỹ thuật (engineering / 엔지니어링) tốt hơn.

Câu hỏi là mô hình (model / 모델) nào diễn đạt ràng buộc (constraint / 제약조건) tự nhiên nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Solver không loại bỏ nhu cầu mô hình hóa** tiếp nhận điểm tựa từ **SAT, SMT và CP-SAT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Symmetry breaking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Solver không loại bỏ nhu cầu mô hình hóa

Một mô hình (model / 모델) solver tệ vẫn có thể chạy rất chậm.

Các quyết định quan trọng:

```text
biến nào thực sự cần?
constraint nào redundant nhưng giúp propagation?
symmetry có thể phá bớt không?
bound ban đầu có tốt không?
miền biến có thể thu hẹp trước không?
```

Hardness không biến mất khi dùng solver; solver cung cấp một bộ tìm kiếm (search / 검색)/pruning engine rất mạnh.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Symmetry breaking** tiếp nhận điểm tựa từ **Solver không loại bỏ nhu cầu mô hình hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lower bound, upper bound và optimality gap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symmetry breaking

Nếu nhiều assignment khác nhau thực chất biểu diễn cùng một solution, solver có thể tốn thời gian khám phá các bản sao đối xứng.

Ví dụ gán màu cho đồ thị (graph / 그래프): hoán đổi tên màu có thể tạo solution lô-gic (logic / 논리) giống nhau.

Thêm ràng buộc (constraint / 제약조건) cố định một số lựa chọn đại diện có thể giảm tìm kiếm (search / 검색) mà không mất solution thực sự khác biệt.

Đây là một dạng state-space reduction.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Lower bound, upper bound và optimality gap** tiếp nhận điểm tựa từ **Symmetry breaking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Anytime thuật toán (algorithm / 알고리즘)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lower bound, upper bound và optimality gap

Trong minimization:

```text
upper bound = chi phí solution khả thi đã tìm được
lower bound = cận dưới chứng minh optimum không thể thấp hơn
```

Nếu hai bound gặp nhau, optimum được chứng minh.

Nếu chưa gặp, gap cho biết mức độ chưa chắc chắn.

Solver tối ưu hóa (optimization / 최적화) hiện đại thường báo cả incumbent solution và best bound; đây là thông tin rất hữu ích để quyết định dừng sớm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Anytime thuật toán (algorithm / 알고리즘)** tiếp nhận điểm tựa từ **Lower bound, upper bound và optimality gap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi nào nên bỏ exactness?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Anytime thuật toán (algorithm / 알고리즘)

Một **anytime thuật toán (algorithm / 알고리즘)** có thể trả solution hiện tại bất cứ lúc nào và cải thiện dần nếu được cho thêm thời gian.

Branch-and-bound, cục bộ (local / 로컬) tìm kiếm (search / 검색) và nhiều solver có thể dùng theo cách này.

Trong hệ thống deadline-driven, đôi khi “solution tốt trong 2 giây” có giá trị hơn “optimum sau thời gian không biết trước”.

Đây là sự đánh đổi (trade-off / 트레이드오프) trực tiếp giữa chất lượng (quality / 품질) và compute ngân sách (budget / 예산).

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Khi nào nên bỏ exactness?** tiếp nhận điểm tựa từ **Anytime thuật toán (algorithm / 알고리즘)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi nào nên dùng brute force?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi nào nên bỏ exactness?

Một quy trình thực dụng:

```text
1. Xác định exactness có thật sự là requirement không.
2. Tìm special case polynomial.
3. Tìm parameter nhỏ cho FPT/exponential method.
4. Ước lượng state-space và memory.
5. Thử exact solver nếu instance vừa phải.
6. Nếu quá lớn, tìm approximation guarantee phù hợp.
7. Nếu guarantee vẫn quá đắt, dùng heuristic và đo quality thực tế.
```

Không nên nhảy thẳng sang heuristic chỉ vì thấy từ “NP-hard”.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Khi nào nên dùng brute force?** tiếp nhận điểm tựa từ **Khi nào nên bỏ exactness?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hardness và sản phẩm (product / 제품) requirements** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi nào nên dùng brute force?

Brute force đúng khi:

```text
input rất nhỏ
cần oracle để test algorithm tối ưu hơn
chỉ chạy offline một lần
search space thực tế bị constraint thu nhỏ
implementation đơn giản quan trọng hơn runtime
```

Một brute-force solver nhỏ, rõ và đúng còn là tham chiếu (reference / 참조) mô hình (model / 모델) rất tốt cho differential testing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Hardness và sản phẩm (product / 제품) requirements** tiếp nhận điểm tựa từ **Khi nào nên dùng brute force?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một workflow nhận diện bài khó** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hardness và sản phẩm (product / 제품) requirements

Một sản phẩm (product / 제품) có thể thay specification để làm bài dễ hơn.

Ví dụ:

```text
exact optimal route -> route <= 5% so với optimum
solve 1 triệu item -> solve theo từng region
arbitrary graph -> graph được giới hạn gần tree
real-time answer -> offline preprocessing
```

Thay yêu cầu (requirement / 요구사항) không phải “né thuật toán”; đôi khi đó là cách duy nhất biến một tối ưu hóa (optimization / 최적화) không khả thi thành hệ thống có SLA rõ.

> **Chuyển mạch:** Trong **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Hardness và sản phẩm (product / 제품) requirements** xác định đầu vào; **Một workflow nhận diện bài khó** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một workflow nhận diện bài khó

Khi gặp combinatorial bài toán (problem / 문제), có thể hỏi:

```text
Có đang chọn subset/permutation/partition không?
Có constraint pairwise hoặc global khiến greedy khó không?
State space là 2^n, n!, k^n hay gì khác?
Có special case graph/tree/interval không?
Numeric parameter có nhỏ không?
Có thể reduce về flow/matching/2-SAT không?
Có parameter k nhỏ cho FPT không?
Có approximation guarantee đã biết theo structure không?
Solver SAT/ILP/CP có phù hợp không?
```

Mục tiêu là nhận ra cấu trúc trước khi lao vào micro-optimization.

> **Chuyển mạch:** Ở chặng này của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Một workflow nhận diện bài khó** xác định đầu vào; **Những hiểu lầm phổ biến** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

“NP nghĩa là non-polynomial” — sai.

“NP-complete nghĩa là không giải được” — sai; nhiều instance cụ thể giải rất tốt.

“Bài NP-hard thì DP polynomial không thể tồn tại” — pseudo-polynomial hoặc special-case DP vẫn có thể tồn tại.

“Reduction B -> SAT chứng minh SAT hard” — sai direction; nó cho thấy SAT có thể giải B nếu encoding đúng.

“Approximation là heuristic” — không nhất thiết; approximation thuật toán (algorithm / 알고리즘) có guarantee định lượng.

“Solver tự động giải quyết modeling” — sai; mô hình (model / 모델) chất lượng (quality / 품질) ảnh hưởng tìm kiếm (search / 검색) cực mạnh.

“Exponential thuật toán (algorithm / 알고리즘) luôn tệ” — sai nếu parameter nhỏ hoặc exactness bắt buộc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khi bài toán chính xác trở nên khó: Reduction, NP-Complete và Approximation**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Khi một bài toán khó, đừng chỉ hỏi “thuật toán nào nhanh hơn?”. Hãy hỏi **hardness nằm ở dimension nào, cấu trúc (structure / 구조) nào của instance làm bài dễ hơn, exactness có thật sự cần không, và ta có thể đổi thời gian–bộ nhớ–độ chính xác như thế nào?**

Reduction giúp đổi góc nhìn. Parameterization đổi biến mà exponential phụ thuộc. Approximation đổi exactness lấy guarantee. Solver đổi công sức hiện thực (implementation / 구현) lấy một tìm kiếm (search / 검색) engine trưởng thành. Heuristic đổi guarantee lấy tốc độ thực tế.

Đó là toolbox đầy đủ hơn cho những bài toán mà “chọn đúng cấu trúc dữ liệu (data structure / 자료구조)” vẫn chưa đủ.

Xem tiếp: [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Greedy Algorithms](./04_greedy_algorithms.md), [Graph Algorithms](../03_graphs/_index.md), [Probabilistic Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md) và [Problem Modeling](../00_foundations/00_dsa_as_problem_modeling.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
