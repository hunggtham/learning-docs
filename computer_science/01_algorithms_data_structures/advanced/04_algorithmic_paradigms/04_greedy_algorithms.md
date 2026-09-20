# Greedy Algorithms
**Thuật toán tham lam (Greedy Algorithms / 그리디 알고리즘)**

Greedy algorithm chọn một quyết định local, khóa nó, rồi tiếp tục mà không quay lại reconsider toàn bộ lịch sử. Điểm khó không nằm ở việc “chọn cái tốt nhất trước” mà ở câu hỏi:

> Tại sao decision local này có thể được khóa mà vẫn còn ít nhất một global optimum tương thích với nó?

Nếu không trả lời được câu đó, greedy chỉ là heuristic.

## Mental Model

> Greedy đúng khi ta chứng minh rằng một local choice là **safe**: sau khi chọn nó, vẫn tồn tại một optimal solution chứa lựa chọn đó.

Proof thường quan trọng hơn code. Code greedy nhiều khi chỉ vài dòng; phần khó là tìm đúng ordering và chứng minh không có regret về sau.

## Greedy-choice property và optimal substructure

Hai ý thường xuất hiện:

**Greedy-choice property**: có một optimal solution bắt đầu bằng greedy choice hiện tại.

**Optimal substructure**: sau khi cố định choice đó, phần còn lại là một subproblem mà optimal solution của nó có thể ghép với current choice để tạo global optimum.

Dynamic programming cũng dùng optimal substructure, nhưng DP thường giữ nhiều alternatives. Greedy loại alternatives ngay vì proof nói chúng không cần thiết.

## Interval Scheduling

Bài toán: chọn số intervals không overlap nhiều nhất.

Một số rule nghe hợp lý nhưng sai:

```text
chọn interval bắt đầu sớm nhất
chọn interval ngắn nhất
chọn interval overlap ít nhất hiện tại
```

Rule đúng kinh điển là:

> chọn interval có finish time sớm nhất trong số interval còn khả dụng.

Sau khi chọn, bỏ các interval overlap và lặp lại.

### Tại sao finish sớm nhất là safe?

Gọi `g` là interval finish sớm nhất. Giả sử một optimal solution `O` bắt đầu bằng interval `o` khác.

Vì:

\[
finish(g) \le finish(o)
\]

thay `o` bằng `g` không làm giảm khoảng thời gian còn lại cho các intervals tiếp theo. Do đó solution mới vẫn có ít nhất cùng số intervals.

Vậy tồn tại optimal solution bắt đầu bằng `g`.

Đây là **exchange argument (교환 논증)**.

## Exchange Argument là gì?

Một proof greedy thường có shape:

1. lấy một optimal solution bất kỳ;
2. nếu nó đã dùng greedy choice, xong;
3. nếu chưa, biến đổi một phần của optimal solution để đưa greedy choice vào;
4. chứng minh transformation không làm objective tệ hơn;
5. suy ra có optimal solution tương thích với greedy step.

Điểm mạnh của exchange argument là ta không cần chứng minh greedy solution “tốt” trực tiếp; ta chứng minh bất kỳ optimum nào cũng có thể được chỉnh thành optimum chứa greedy choices.

## Cut Property trong MST

Kruskal và Prim là greedy nhưng proof không giống interval scheduling.

Với một cut chia vertices thành hai phía, một minimum-weight edge crossing cut là **safe** cho một MST theo cut property.

Kruskal repeatedly chọn lightest edge nối hai components khác nhau.

Prim repeatedly chọn lightest edge crossing từ current tree ra ngoài.

Cả hai đều lock local edge vì cut property chứng minh vẫn tồn tại MST chứa edge đó.

## Dijkstra cũng có greedy flavor

Dijkstra chọn unsettled node có tentative distance nhỏ nhất và finalize nó.

Greedy step safe chỉ vì edge weights không âm. Negative edge phá proof.

Điều này cho thấy greedy correctness thường phụ thuộc assumption rất cụ thể. Nếu assumption thay đổi, cùng local rule có thể sai hoàn toàn.

## Coin Change: ví dụ greedy thất bại

Coin set:

```text
[1, 3, 4]
```

target `6`.

Greedy “lấy coin lớn nhất không vượt target”:

```text
4 + 1 + 1 = 3 coins
```

Optimal:

```text
3 + 3 = 2 coins
```

Local choice `4` nhìn tốt nhưng làm future state xấu hơn.

Với một số currency systems chuẩn, greedy coin change có thể đúng, nhưng correctness đến từ structure của coin system, không từ intuition “coin lớn hơn luôn tốt”.

## Fractional Knapsack vs 0/1 Knapsack

Đây là cặp problem rất hữu ích để thấy constraint nhỏ có thể đổi paradigm.

### Fractional Knapsack

Cho phép lấy fraction của item. Sort theo:

\[
\frac{value}{weight}
\]

và lấy ratio cao trước là optimal.

Proof exchange: nếu solution dùng một lượng capacity cho item ratio thấp trong khi item ratio cao còn chưa lấy hết, chuyển một lượng nhỏ capacity sang item ratio cao làm value tăng.

### 0/1 Knapsack

Không được chia item. Exchange “một lượng nhỏ” không còn hợp lệ. Greedy theo ratio có thể sai; DP thường cần giữ multiple combinations.

Một chữ “fractional” thay đổi mathematical structure của problem.

## Huffman Coding

Huffman coding repeatedly merge hai frequencies nhỏ nhất bằng min-heap.

Algorithm:

```text
đưa tất cả frequencies vào min-heap
while còn hơn một tree:
    lấy hai tree nhẹ nhất a,b
    tạo parent weight a+b
    push parent lại heap
```

Tổng cost liên hệ với weighted path length của leaves.

### Tại sao merge hai nhỏ nhất là safe?

Trong một optimal prefix-code tree, hai leaves sâu nhất có thể được chọn làm siblings; ta có thể exchange labels để hai frequencies nhỏ nhất nằm ở các vị trí deepest đó mà không tăng cost.

Sau khi merge chúng thành pseudo-symbol có frequency sum, problem co lại thành một instance nhỏ hơn cùng dạng.

Đây là greedy + tree + priority queue cùng lúc.

## Scheduling theo deadline

Nhiều scheduling problems có greedy solution nhưng **rule khác nhau** tùy objective.

Ví dụ single-machine jobs với deadline/profit, minimize lateness, maximize số jobs đúng hạn, weighted scheduling... không thể dùng một rule chung.

Một problem có thể sort theo:

```text
earliest deadline
shortest processing time
highest ratio
finish time
```

nhưng mỗi ordering chỉ đúng cho objective/constraints cụ thể.

Đây là lý do nhận diện “đây là scheduling nên greedy” là chưa đủ.

## Earliest Deadline First

Trong một số scheduling models, Earliest Deadline First (EDF) có optimality property. Nhưng thêm non-preemptive constraints, release time, multiple machines hoặc weights có thể thay đổi hoàn toàn result.

Greedy proof luôn gắn với exact model.

## Activity Selection bằng Java

```java
record Interval(int start, int end) {}

static List<Interval> selectMaxNonOverlapping(List<Interval> xs) {
    xs.sort(Comparator.comparingInt(Interval::end));

    List<Interval> ans = new ArrayList<>();
    int lastEnd = Integer.MIN_VALUE;

    for (Interval x : xs) {
        if (x.start() >= lastEnd) {
            ans.add(x);
            lastEnd = x.end();
        }
    }
    return ans;
}
```

Trong code thật, boundary semantics phải rõ: intervals là `[start,end)` hay closed `[start,end]`? Nếu end đúng bằng next start thì có overlap không? Domain quyết định comparator/condition.

## Sorting thường là bước tạo greedy invariant

Nhiều greedy algorithms bắt đầu bằng sort. Sort không chỉ để code đẹp; nó tạo một order cho phép local choice có meaning.

Ví dụ:

```text
interval scheduling -> sort by finish time
Kruskal             -> sort edges by weight
fractional knapsack -> sort by value/weight ratio
```

Cost tổng thường bị sort chi phối:

\[
O(n\log n)
\]

sau đó greedy scan chỉ `O(n)`.

## Greedy với priority queue

Một số problems không có toàn bộ candidates available từ đầu. Ta sort events theo một dimension, rồi dùng heap để chọn best trong active set.

Ví dụ scheduling jobs với deadlines có thể process deadlines tăng dần và giữ selected durations/profits trong heap để loại candidate tệ nhất khi constraint bị vi phạm.

Đây là pattern:

```text
sort theo thời gian / boundary
maintain feasible active solution
nếu violation -> remove worst local contributor bằng heap
```

Proof vẫn cần exchange argument; heap chỉ làm greedy operation nhanh.

## Greedy với monotonicity

Nếu decision làm feasible region co lại theo một chiều monotonic, greedy có thể xuất hiện tự nhiên.

Ví dụ khi chọn earliest finish, mọi interval bắt đầu trước finish mới bị loại; phần còn lại vẫn là cùng problem trên suffix timeline.

Monotonicity giúp chứng minh subproblem không cần nhớ chi tiết history ngoài một boundary state.

## Matroid intuition

Một framework lý thuyết giải thích nhiều greedy algorithms là **matroid**. Không cần học formal theory ngay, nhưng intuition hữu ích:

Có một family các independent sets thỏa hereditary property và exchange property. Khi structure là matroid, greedy chọn element tốt nhất theo weight có thể tạo maximum-weight independent set.

Graphic matroid của graph là ví dụ nền cho Kruskal: edge sets không tạo cycle là independent sets.

Điểm quan trọng không phải thuật ngữ, mà là nhận ra greedy correctness thường đến từ một **exchange structure sâu hơn**.

## Greedy Stays Ahead proof

Một proof style khác là chứng minh sau mỗi bước, greedy solution không thua bất kỳ optimal candidate prefix nào theo một metric.

Ví dụ có thể chứng minh greedy finish times luôn không muộn hơn corresponding finish times trong một optimal interval schedule.

Nếu greedy “stays ahead” ở mọi prefix, global objective theo sau.

## Contradiction proof

Một số greedy correctness proofs giả sử greedy đầu tiên khác optimal tại vị trí đầu tiên, rồi chỉ ra việc thay optimal choice bằng greedy choice không làm tệ hơn, contradiction với việc cần khác nhau.

Dù presentation khác exchange argument, core idea vẫn là local choice có thể được đưa vào optimum an toàn.

## Khi Greedy và DP gần nhau

Có problems mà DP state có transition:

\[
dp[i] = \min_j(...)
\]

nhưng một structural theorem cho thấy candidate tối ưu luôn theo một monotonic/local rule. Khi đó greedy có thể được xem như DP đã “collapse” nhờ proof mạnh hơn.

Ngược lại, nếu không thể prove một choice safe, DP giữ nhiều alternatives vì future có thể làm thay đổi best decision.

Mental contrast:

```text
Greedy -> commit một state frontier
DP     -> giữ nhiều state alternatives
```

## Greedy và approximation

Đôi khi greedy không exact nhưng vẫn có approximation guarantee.

Set Cover greedy chọn set cover nhiều uncovered elements nhất mỗi bước. Nó không luôn optimal, nhưng có logarithmic approximation guarantee.

Trong Maximum Coverage với budget `k`, greedy có guarantee kinh điển liên quan `1 - 1/e` dưới model chuẩn.

Điều này nhắc rằng “greedy sai exact” không có nghĩa vô dụng. Có thể nó có provable bound gần optimal.

## Greedy và heuristic khác nhau

**Greedy algorithm có proof exact**: local choices tạo optimal answer.

**Approximation greedy**: có proof answer không quá xa optimum theo ratio/additive bound.

**Heuristic**: có empirical intuition nhưng không có guarantee cần thiết.

Ba loại này nên được nói rõ, đặc biệt trong production optimization.

## Online greedy decisions

Trong online algorithms, future input chưa biết. Greedy có thể là lựa chọn bắt buộc vì decision phải đưa ra ngay.

Lúc này metric không nhất thiết là exact optimum offline mà là **competitive ratio** so với optimum biết trước future.

Caching eviction, online matching và scheduling có các variants theo model này.

Greedy offline và online nhìn giống nhau ở local decision, nhưng guarantee framework khác nhau.

## Common failure patterns

### Chọn value lớn nhất trước

Không đủ. Future compatibility mới quan trọng.

### Chọn ratio lớn nhất

Chỉ đúng trong một số divisible/resource models.

### Chọn shortest/earliest task

Objective khác nhau cần proof khác nhau.

### Sort rồi scan nên chắc là greedy đúng

Không. Sorting chỉ tạo ordering; local choice vẫn cần safe-choice proof.

### Sample tests pass nên greedy đúng

Greedy counterexample thường nhỏ nhưng không obvious. Cần proof hoặc systematic brute-force comparison trên small `n`.

## Cách tìm counterexample

Khi nghi ngờ một greedy rule, thử tạo case nơi local metric và future flexibility xung đột.

Ví dụ với coin greedy, muốn coin lớn nhất để lại remainder xấu.

Với interval heuristic “shortest duration”, tạo interval rất ngắn nằm giữa timeline nhưng block hai intervals ngoài.

Với “highest profit first”, tạo high-profit job chiếm resource làm mất nhiều medium-profit compatible jobs.

Counterexample construction là skill quan trọng để tránh tin intuition.

## Differential testing greedy vs brute force

Với `n` nhỏ, enumerate mọi feasible subset/order để tìm optimum, rồi compare greedy result.

Nếu tìm thấy mismatch, greedy hypothesis sai.

Nếu không tìm thấy mismatch trên nhiều random small inputs, đó chưa phải proof, nhưng là cách rất tốt để tìm bug hoặc counterexample trước khi cố prove.

Workflow:

```text
propose greedy rule
implement brute-force oracle cho n nhỏ
random/exhaustive compare
tìm counterexample hoặc xây proof
```

## Khi nào nên nghĩ greedy?

Một số dấu hiệu hữu ích nhưng không phải proof:

- objective có thể optimize qua ordered choices;
- sau một choice, problem còn lại giữ cùng structure;
- có natural exchange argument;
- feasible sets có matroid-like exchange property;
- một boundary như earliest finish/minimum edge tạo safe cut;
- decisions có thể được locked vì future không làm chúng regret.

Nếu local choice có thể bị future information đảo ngược, DP/backtracking/flow có thể phù hợp hơn.

## Connections với các chapter khác

Kruskal/Prim: [Minimum Spanning Tree](../03_graphs/03_minimum_spanning_trees.md).

Dijkstra: [Shortest Paths](../03_graphs/02_shortest_paths.md).

Huffman cần: [Heap](../02_trees/03_heaps.md).

Khi greedy không exact và problem computationally hard, xem [Hard Problems, Reductions & Approximation](./09_hard_problems_reductions_and_approximation.md).

## Mental Model mở rộng

> Greedy không có nghĩa “tham lam chọn cái có vẻ tốt nhất”. Nó nghĩa là **có theorem cho phép khóa một quyết định mà không cần giữ alternatives**.

Khi thiết kế greedy, hãy viết local choice bằng một câu chính xác, sau đó hỏi: tôi có thể lấy một optimum bất kỳ và exchange choice đầu tiên của nó thành greedy choice mà không làm tệ hơn không? Nếu không làm được, hãy tìm counterexample trước khi viết code dài.