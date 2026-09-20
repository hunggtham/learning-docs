# Greedy các thuật toán
**Thuật toán tham lam (Greedy Algorithms / 그리디 알고리즘)**

thuật toán tham lam chọn một quyết định cục bộ, khóa nó, rồi tiếp tục mà không quay lại reconsider toàn bộ lịch sử. Điểm khó không nằm ở việc “chọn cái tốt nhất trước” mà ở câu hỏi:

> Tại sao decision cục bộ này có thể được khóa mà vẫn còn ít nhất một toàn cục phương án tối ưu tương thích với nó?

Nếu không trả lời được câu đó, greedy chỉ là heuristic.

## Mô hình tư duy

> Greedy đúng khi ta chứng minh rằng một cục bộ choice là **an toàn**: sau khi chọn nó, vẫn tồn tại một lời giải tối ưu chứa lựa chọn đó.

chứng minh thường quan trọng hơn code. Code greedy nhiều khi chỉ vài dòng; phần khó là tìm đúng ordering và chứng minh không có regret về sau.

## Greedy-choice tính chất và optimal substructure

Hai ý thường xuất hiện:

**Greedy-choice tính chất**: có một lời giải tối ưu bắt đầu bằng lựa chọn tham lam hiện tại.

**Optimal substructure**: sau khi cố định choice đó, phần còn lại là một subproblem mà lời giải tối ưu của nó có thể ghép với hiện tại choice để tạo toàn cục phương án tối ưu.

quy hoạch động (dynamic programming) cũng dùng optimal substructure, nhưng DP thường giữ nhiều alternatives. Greedy loại alternatives ngay vì chứng minh nói chúng không cần thiết.

## lập lịch khoảng

Bài toán: chọn số intervals không overlap nhiều nhất.

Một số quy tắc nghe hợp lý nhưng sai:

```text
chọn interval bắt đầu sớm nhất
chọn interval ngắn nhất
chọn interval overlap ít nhất hiện tại
```

quy tắc đúng kinh điển là:

> chọn interval có thời điểm kết thúc sớm nhất trong số interval còn khả dụng.

Sau khi chọn, bỏ các interval overlap và lặp lại.

### Tại sao finish sớm nhất là an toàn?

Gọi `g` là interval finish sớm nhất. Giả sử một lời giải tối ưu `O` bắt đầu bằng interval `o` khác.

Vì:

\[
finish(g) \le finish(o)
\]

thay `o` bằng `g` không làm giảm khoảng thời gian còn lại cho các intervals tiếp theo. Do đó lời giải mới vẫn có ít nhất cùng số intervals.

Vậy tồn tại lời giải tối ưu bắt đầu bằng `g`.

Đây là **exchange argument (교환 논증)**.

## Exchange Argument là gì?

Một chứng minh greedy thường có shape:

1. lấy một lời giải tối ưu bất kỳ;
2. nếu nó đã dùng lựa chọn tham lam, xong;
3. nếu chưa, biến đổi một phần của lời giải tối ưu để đưa lựa chọn tham lam vào;
4. chứng minh phép biến đổi không làm objective tệ hơn;
5. suy ra có lời giải tối ưu tương thích với bước tham lam.

Điểm mạnh của exchange argument là ta không cần chứng minh lời giải tham lam “tốt” trực tiếp; ta chứng minh bất kỳ phương án tối ưu nào cũng có thể được chỉnh thành phương án tối ưu chứa greedy choices.

## Cut tính chất trong MST

Kruskal và Prim là greedy nhưng chứng minh không giống lập lịch khoảng.

Với một cut chia các đỉnh thành hai phía, một minimum-weight cạnh crossing cut là **an toàn** cho một MST theo cut tính chất.

Kruskal lặp lại chọn lightest cạnh nối hai các thành phần khác nhau.

Prim lặp lại chọn lightest cạnh crossing từ hiện tại cây ra ngoài.

Cả hai đều lock cục bộ cạnh vì cut tính chất chứng minh vẫn tồn tại MST chứa cạnh đó.

## Dijkstra cũng có greedy flavor

Dijkstra chọn unsettled nút có tentative khoảng cách nhỏ nhất và finalize nó.

bước tham lam an toàn chỉ vì cạnh các trọng số không âm. Negative cạnh phá chứng minh.

Điều này cho thấy greedy tính đúng đắn thường phụ thuộc giả định rất cụ thể. Nếu giả định thay đổi, cùng cục bộ quy tắc có thể sai hoàn toàn.

## Coin Change: ví dụ greedy thất bại

Coin set:

```text
[1, 3, 4]
```

đích `6`.

Greedy “lấy coin lớn nhất không vượt đích”:

```text
4 + 1 + 1 = 3 coins
```

Optimal:

```text
3 + 3 = 2 coins
```

cục bộ choice `4` nhìn tốt nhưng làm tương lai trạng thái (state) xấu hơn.

Với một số currency các hệ thống chuẩn, greedy coin change có thể đúng, nhưng tính đúng đắn đến từ structure của hệ tiền xu, không từ intuition “coin lớn hơn luôn tốt”.

## Fractional Knapsack vs 0/1 Knapsack

Đây là cặp problem rất hữu ích để thấy ràng buộc nhỏ có thể đổi paradigm.

### Fractional Knapsack

Cho phép lấy fraction của item. Sort theo:

\[
\frac{giá trị}{trọng số}
\]

và lấy ratio cao trước là optimal.

Trong chứng minh trao đổi (exchange argument), nếu lời giải dành một phần sức chứa cho vật có tỷ lệ giá trị thấp trong khi vật có tỷ lệ cao vẫn chưa được lấy hết, ta có thể chuyển một phần sức chứa sang vật có tỷ lệ cao để làm tổng giá trị tăng.

### 0/1 Knapsack

Không được chia item. Exchange “một lượng nhỏ” không còn hợp lệ. Greedy theo ratio có thể sai; DP thường cần giữ multiple combinations.

Một chữ “fractional” thay đổi mathematical structure của problem.

## Huffman Coding

Huffman coding lặp lại merge hai các tần suất nhỏ nhất bằng đống nhỏ nhất.

thuật toán:

```text
đưa tất cả frequencies vào min-heap
while còn hơn một tree:
    lấy hai tree nhẹ nhất a,b
    tạo parent weight a+b
    push parent lại heap
```

Tổng chi phí liên hệ với weighted đường đi length của các nút lá.

### Tại sao merge hai nhỏ nhất là an toàn?

Trong một optimal prefix-code cây, hai các nút lá sâu nhất có thể được chọn làm siblings; ta có thể exchange labels để hai các tần suất nhỏ nhất nằm ở các vị trí deepest đó mà không tăng chi phí.

Sau khi merge chúng thành pseudo-symbol có tần suất sum, problem co lại thành một instance nhỏ hơn cùng dạng.

Đây là greedy + cây + hàng đợi ưu tiên cùng lúc.

## Scheduling theo deadline

Nhiều bài toán lập lịch có lời giải tham lam nhưng **quy tắc lựa chọn khác nhau** tùy mục tiêu tối ưu.

Ví dụ single-machine jobs với deadline/profit, minimize lateness, maximize số jobs đúng hạn, lập lịch có trọng số... không thể dùng một quy tắc chung.

Một problem có thể sort theo:

```text
earliest deadline
shortest processing time
highest ratio
finish time
```

nhưng mỗi ordering chỉ đúng cho objective/các ràng buộc cụ thể.

Đây là lý do nhận diện “đây là scheduling nên greedy” là chưa đủ.

## Earliest Deadline First

Trong một số scheduling các mô hình, Earliest Deadline First (EDF) có optimality tính chất. Nhưng thêm non-preemptive các ràng buộc, release time, multiple machines hoặc các trọng số có thể thay đổi hoàn toàn kết quả.

Greedy chứng minh luôn gắn với chính xác mô hình.

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

Trong code thật, ranh giới ngữ nghĩa (semantics) phải rõ: intervals là `[start,end)` hay closed `[start,end]`? Nếu end đúng bằng next start thì có overlap không? Domain quyết định comparator/điều kiện.

## Sorting thường là bước tạo greedy bất biến (invariant)

Nhiều greedy các thuật toán bắt đầu bằng sort. Sort không chỉ để code đẹp; nó tạo một order cho phép cục bộ choice có meaning.

Ví dụ:

```text
interval scheduling -> sort by finish time
Kruskal             -> sort edges by weight
fractional knapsack -> sort by value/weight ratio
```

chi phí tổng thường bị sort chi phối:

\[
O(n\log n)
\]

sau đó greedy quét chỉ `O(n)`.

## Greedy với hàng đợi ưu tiên

Một số problems không có toàn bộ các ứng viên available từ đầu. Ta sort các sự kiện theo một dimension, rồi dùng heap để chọn best trong active set.

Ví dụ scheduling jobs với deadlines có thể xử lý deadlines tăng dần và giữ selected durations/profits trong heap để loại ứng viên tệ nhất khi ràng buộc bị vi phạm.

Đây là mẫu:

```text
sort theo thời gian / boundary
maintain feasible active solution
nếu violation -> remove worst local contributor bằng heap
```

Chứng minh tính đúng đắn vẫn cần lập luận trao đổi (exchange argument); heap chỉ giúp thao tác lựa chọn tham lam chạy nhanh hơn.

## Greedy với monotonicity

Nếu decision làm feasible region co lại theo một chiều monotonic, greedy có thể xuất hiện tự nhiên.

Ví dụ khi chọn earliest finish, mọi interval bắt đầu trước finish mới bị loại; phần còn lại vẫn là cùng problem trên suffix timeline.

Monotonicity giúp chứng minh subproblem không cần nhớ chi tiết lịch sử ngoài một ranh giới trạng thái.

## Matroid intuition

Một khung làm việc lý thuyết giải thích nhiều greedy các thuật toán là **matroid**. Không cần học formal theory ngay, nhưng intuition hữu ích:

Có một họ các tập độc lập thỏa tính chất di truyền và tính chất trao đổi. Khi cấu trúc là matroid, thuật toán tham lam chọn phần tử tốt nhất theo trọng số có thể tạo tập độc lập có tổng trọng số lớn nhất.

Graphic matroid của đồ thị là ví dụ nền cho Kruskal: cạnh sets không tạo chu trình là independent sets.

Điểm quan trọng không phải thuật ngữ, mà là nhận ra greedy tính đúng đắn thường đến từ một **exchange structure sâu hơn**.

## Greedy Stays Ahead chứng minh

Một chứng minh style khác là chứng minh sau mỗi bước, lời giải tham lam không thua bất kỳ optimal ứng viên prefix nào theo một metric.

Ví dụ, có thể chứng minh thời điểm kết thúc do thuật toán tham lam tạo ra luôn không muộn hơn thời điểm kết thúc tương ứng trong một lịch khoảng tối ưu.

Nếu lời giải tham lam luôn “đi trước” ở mọi tiền tố, tính tối ưu của mục tiêu toàn cục có thể được suy ra từ đó.

## Contradiction chứng minh

Một số greedy tính đúng đắn các chứng minh giả sử greedy đầu tiên khác optimal tại vị trí đầu tiên, rồi chỉ ra việc thay optimal choice bằng lựa chọn tham lam không làm tệ hơn, contradiction với việc cần khác nhau.

Dù presentation khác exchange argument, core idea vẫn là cục bộ choice có thể được đưa vào phương án tối ưu an toàn.

## Khi Greedy và DP gần nhau

Có problems mà DP trạng thái có transition:

\[
dp[i] = \min_j(...)
\]

nhưng một structural theorem cho thấy ứng viên tối ưu luôn theo một monotonic/cục bộ quy tắc. Khi đó greedy có thể được xem như DP đã “collapse” nhờ chứng minh mạnh hơn.

Ngược lại, nếu không thể prove một choice an toàn, DP giữ nhiều alternatives vì tương lai có thể làm thay đổi best decision.

Mental contrast:

```text
Greedy -> commit một state frontier
DP     -> giữ nhiều state alternatives
```

## Greedy và approximation

Đôi khi greedy không chính xác nhưng vẫn có approximation bảo đảm.

Set Cover greedy chọn set cover nhiều uncovered các phần tử nhất mỗi bước. Nó không luôn optimal, nhưng có logarithmic approximation bảo đảm.

Trong Maximum Coverage với budget `k`, greedy có bảo đảm kinh điển liên quan `1 - 1/e` dưới mô hình chuẩn.

Điều này nhắc rằng “greedy sai chính xác” không có nghĩa vô dụng. Có thể nó có provable bound gần optimal.

## Greedy và heuristic khác nhau

**thuật toán tham lam có chứng minh chính xác**: cục bộ choices tạo optimal answer.

**Approximation greedy**: có chứng minh answer không quá xa phương án tối ưu theo ratio/additive bound.

**Heuristic**: có empirical intuition nhưng không có bảo đảm cần thiết.

Ba loại này nên được nói rõ, đặc biệt trong hệ thống thực tế optimization.

## trực tuyến greedy decisions

Trong trực tuyến các thuật toán, tương lai đầu vào chưa biết. Greedy có thể là lựa chọn bắt buộc vì decision phải đưa ra ngay.

Lúc này metric không nhất thiết là chính xác phương án tối ưu ngoại tuyến mà là **competitive ratio** so với phương án tối ưu biết trước tương lai.

Caching eviction, trực tuyến matching và scheduling có các variants theo mô hình này.

Greedy ngoại tuyến và trực tuyến nhìn giống nhau ở cục bộ decision, nhưng bảo đảm khung làm việc khác nhau.

## Phổ biến failure các mẫu

### Chọn giá trị lớn nhất trước

Không đủ. tương lai compatibility mới quan trọng.

### Chọn ratio lớn nhất

Chỉ đúng trong một số divisible/resource các mô hình.

### Chọn shortest/earliest task

Objective khác nhau cần chứng minh khác nhau.

### Sort rồi quét nên chắc là greedy đúng

Không. Sorting chỉ tạo ordering; cục bộ choice vẫn cần safe-choice chứng minh.

### Sample tests pass nên greedy đúng

Greedy phản ví dụ thường nhỏ nhưng không obvious. Cần chứng minh hoặc systematic brute-force phép so sánh trên small `n`.

## Cách tìm phản ví dụ

Khi nghi ngờ một quy tắc tham lam, hãy thử tạo phản ví dụ nơi thước đo cục bộ xung đột với mức linh hoạt cần thiết cho tương lai.

Ví dụ với coin greedy, muốn coin lớn nhất để lại remainder xấu.

Với heuristic “khoảng ngắn nhất”, có thể tạo một khoảng rất ngắn nằm giữa dòng thời gian nhưng chặn hai khoảng ở hai phía.

Với quy tắc “lợi nhuận cao nhất trước”, có thể tạo một công việc lợi nhuận cao chiếm tài nguyên và làm mất nhiều công việc lợi nhuận trung bình nhưng tương thích với nhau.

phản ví dụ construction là skill quan trọng để tránh tin intuition.

## Differential kiểm thử greedy vs brute force

Với `n` nhỏ, enumerate mọi feasible subset/order để tìm phương án tối ưu, rồi so sánh greedy kết quả.

Nếu tìm thấy mismatch, greedy hypothesis sai.

Nếu không tìm thấy mismatch trên nhiều ngẫu nhiên small các đầu vào, đó chưa phải chứng minh, nhưng là cách rất tốt để tìm bug hoặc phản ví dụ trước khi cố prove.

Workflow:

```text
propose greedy rule
implement brute-force oracle cho n nhỏ
random/exhaustive compare
tìm counterexample hoặc xây proof
```

## Khi nào nên nghĩ greedy?

Một số dấu hiệu hữu ích nhưng không phải chứng minh:

- objective có thể optimize qua ordered choices;
- sau một choice, problem còn lại giữ cùng structure;
- có natural exchange argument;
- feasible sets có matroid-like exchange tính chất;
- một ranh giới như earliest finish/minimum cạnh tạo an toàn cut;
- decisions có thể được locked vì tương lai không làm chúng regret.

Nếu cục bộ choice có thể bị tương lai thông tin đảo ngược, DP/quay lui (backtracking)/flow có thể phù hợp hơn.

## Connections với các chapter khác

Kruskal/Prim: [Minimum Spanning Tree](../03_graphs/03_minimum_spanning_trees.md).

Dijkstra: [Shortest Paths](../03_graphs/02_shortest_paths.md).

Huffman cần: [Heap](../02_trees/03_heaps.md).

Khi greedy không chính xác và problem computationally hard, xem [Hard Problems, Reductions & Approximation](./09_hard_problems_reductions_and_approximation.md).

## Mô hình tư duy mở rộng

> Greedy không có nghĩa “tham lam chọn cái có vẻ tốt nhất”. Nó nghĩa là **có theorem cho phép khóa một quyết định mà không cần giữ alternatives**.

Khi thiết kế greedy, hãy viết cục bộ choice bằng một câu chính xác, sau đó hỏi: tôi có thể lấy một phương án tối ưu bất kỳ và exchange choice đầu tiên của nó thành lựa chọn tham lam mà không làm tệ hơn không? Nếu không làm được, hãy tìm phản ví dụ trước khi viết code dài.