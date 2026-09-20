# Workflow giải bài DSA và thiết kế thuật toán
**Problem-Solving Workflow / 문제 해결 흐름**

Giải một bài DSA tốt không bắt đầu bằng việc nhớ “pattern nào giống LeetCode”, mà bắt đầu bằng cách **mô hình hóa đúng vấn đề**, định lượng constraints, tìm một baseline đúng, rồi từng bước loại bỏ work không cần thiết. Mục tiêu của workflow này là biến một problem statement dài thành một chuỗi câu hỏi có thể kiểm chứng.

Một solution mạnh thường có ba lớp reasoning: representation đúng, invariant đúng và complexity phù hợp. Nếu một trong ba sai, code có thể chạy nhưng solution vẫn không đáng tin cậy.

## 1. Đọc problem như một specification

Đừng code ngay khi vừa đọc ví dụ. Trước tiên cần xác định chính xác input, output, assumptions và semantics.

Nếu đề nói “subarray”, thông thường đó là đoạn **liên tiếp** của array; nếu nói “subsequence”, phần tử không cần liên tiếp nhưng phải giữ relative order. Nếu graph là directed hay undirected, weighted hay unweighted, multi-edge có được phép không, self-loop có tồn tại không, tất cả đều ảnh hưởng algorithm.

Interval `[l,r]` và `[l,r)` khác nhau ở boundary semantics. String có thể chỉ chứa ASCII hay Unicode. Integer có thể vượt 32-bit hay không. Những chi tiết này không phải phần phụ; chúng quyết định correctness.

Một thói quen tốt là tự viết lại bài toán bằng một câu ngắn: “Tôi cần tìm X sao cho Y, dưới constraints Z.” Nếu chưa viết được câu này, model vẫn chưa rõ.

## 2. Từ story sang mathematical/computational model

Problem statement thường kể một câu chuyện domain: thành phố, chuyến bay, nhân viên, server, booking, robot hoặc game. DSA bắt đầu khi ta bỏ lớp câu chuyện và nhận ra cấu trúc bên dưới.

Một hệ thống đường đi giữa thành phố có thể là graph. Quan hệ cha-con là tree. Booking theo thời gian là intervals. Chuỗi thao tác undo là stack. Các truy vấn cộng đoạn là range-query problem. Một bài “chọn hoặc bỏ từng item” có thể là subset state space.

Việc model hóa đúng thường quan trọng hơn implementation. Nếu model sai, thuật toán đúng vẫn giải sai bài toán.

## 3. Constraints chính là complexity budget

Constraints không chỉ là thông tin để tránh overflow; chúng cho biết loại thuật toán nào còn khả thi.

Nếu `n <= 20`, `O(2^n)` có thể hợp lý. Nếu `n ≈ 10^3`, `O(n^2)` đôi khi chấp nhận được. Nếu `n ≈ 10^5` hoặc `10^6`, thường phải hướng tới `O(n log n)` hoặc `O(n)`. Nếu có `10^5` queries trên cùng dataset, preprocessing hoặc data structure index trở nên đáng giá.

Nhưng đây chỉ là heuristic. Constant factor, language runtime và time limit cũng quan trọng. `O(n log n)` với heavy allocation có thể chậm hơn `O(n sqrt(n))` tối ưu tốt ở một miền nhỏ; tuy nhiên asymptotic analysis vẫn là bước lọc đầu tiên.

## 4. Luôn tìm một baseline đúng trước

Brute force không phải “solution tệ để bỏ đi”; nó là specification executable. Baseline cho ta ba thứ: xác nhận hiểu đề đúng, làm reference cho testing, và phơi bày repeated work.

Ví dụ Two Sum brute force kiểm tra mọi cặp `O(n^2)`. Khi nhìn vào repeated work, ta thấy với mỗi phần tử `x` ta chỉ cần biết `target - x` đã xuất hiện chưa. Hash set nén việc tìm kiếm này xuống expected `O(1)` mỗi bước.

Với range sum, brute force cộng lại đoạn mỗi query. Prefix sum nhận ra cùng prefix được tính lặp đi lặp lại và precompute nó một lần.

Với recursive search `O(2^n)`, nếu nhiều nhánh đi tới cùng state, memoization biến search tree thành state graph nhỏ hơn.

Optimization tốt thường có thể mô tả bằng câu: **“Tôi đã loại bỏ loại work lặp lại nào?”**

## 5. Xác định state và information thực sự cần giữ

Nhiều thuật toán trở nên đơn giản khi ta hỏi: để quyết định bước tiếp theo, cần biết tối thiểu những thông tin nào?

Sliding window thường chỉ cần hai pointers và một summary của window. Dijkstra cần best known distance và frontier priority. DP cần state đủ để đại diện mọi thông tin từ quá khứ có thể ảnh hưởng tương lai.

State quá nhỏ làm solution sai vì mất thông tin. State quá lớn làm complexity bùng nổ. Đây là lý do thiết kế state là trung tâm của DP, graph search và many online algorithms.

Một test hữu ích là: nếu hai partial histories tạo cùng state, tương lai của chúng có thực sự tương đương không? Nếu có, ta có thể merge hai histories thành một DP/memo state.

## 6. Chọn representation trước khi chọn algorithm cụ thể

Cùng một graph có thể biểu diễn bằng adjacency matrix hoặc adjacency list. Matrix cho edge lookup `O(1)` nhưng memory `O(V^2)`. List phù hợp sparse graph và traversal `O(V+E)`.

Một frequency problem có thể dùng array nếu key domain nhỏ và dense, hoặc hash map nếu sparse. Một set các intervals có thể sort theo start để tạo ordering invariant trước khi sweep.

Representation quyết định cost của operation sau đó. Vì thế “algorithm” và “data structure” không nên được suy nghĩ tách rời.

## 7. Viết invariant trước khi viết loop phức tạp

**Invariant / 불변식** là điều phải luôn đúng tại một điểm cụ thể của algorithm. Nó là cầu nối giữa intuition và proof.

Với binary search, invariant có thể là “nếu answer tồn tại thì nó vẫn nằm trong interval `[lo, hi]`”. Với sliding window, invariant có thể là “window hiện tại luôn có tổng không vượt `K`”. Với heap, parent-child order phải luôn đúng sau mỗi update. Với DSU, mỗi component phải có một representative root nhất quán.

Nếu không nói được invariant, debug thường trở thành thử-sai. Nếu invariant rõ, ta biết mỗi line update phải bảo toàn điều gì.

## 8. Tách correctness khỏi complexity

Một thuật toán có thể nhanh nhưng sai; hoặc đúng nhưng quá chậm. Hai câu hỏi cần được chứng minh riêng.

Correctness thường dựa trên induction, exchange argument, cut property, loop invariant hoặc contradiction. Complexity dựa trên counting operations, recurrence, amortized analysis hoặc expected analysis.

Ví dụ greedy interval scheduling không đúng chỉ vì code chọn interval kết thúc sớm nhất “có vẻ hợp lý”. Ta cần exchange argument cho thấy bất kỳ optimal solution nào cũng có thể đổi first chosen interval thành interval kết thúc sớm nhất mà không làm giảm số lượng interval còn chọn được.

## 9. Nhận diện các hướng tối ưu hóa phổ biến

Khi baseline quá chậm, có vài câu hỏi rất hữu ích.

Nếu đang có nested loop `O(n^2)`, hãy hỏi liệu sorting có tạo monotonic structure cho two pointers hay binary search không; liệu hash table có thay inner scan bằng lookup không; liệu prefix/difference array có tránh recompute aggregate không; liệu sweep line có biến pairwise interaction thành ordered events không.

Nếu search tree exponential, hãy hỏi liệu có overlapping states để memoize, có pruning bound để loại branch, có symmetry để tránh xét trạng thái tương đương, hoặc có greedy property để không cần search toàn bộ hay không.

Nếu query lặp lại trên dữ liệu giống nhau, hãy hỏi preprocessing/index có đáng không. Nếu update và query đều nhiều, hãy cân nhắc Fenwick/Segment Tree, balanced tree hoặc specialized structure phù hợp.

## 10. Dry-run bằng một input nhỏ nhưng “khó chịu”

Ví dụ đẹp trong đề thường không đủ. Hãy tự tạo input phá assumptions: empty, one element, duplicates, all equal, reverse order, negative values, disconnected graph, cycle, multiple shortest paths, zero-weight edge, duplicate edges hoặc extremely skewed tree.

Dry-run nên theo state thật của algorithm: pointers, queue, stack, distances, parent links, DP table, heap content. Nếu state transition không giải thích được bằng invariant, đó là dấu hiệu design chưa ổn.

## 11. Edge cases phải sinh từ model

Một checklist chung hữu ích, nhưng edge cases mạnh nhất xuất phát từ assumption của chính algorithm.

Nếu binary search dùng `mid = (lo + hi) / 2`, hãy nghĩ overflow trong C/Java integer. Nếu recursion depth có thể bằng `n = 10^5`, stack overflow là risk. Nếu Dijkstra được dùng, hãy hỏi edge có negative không. Nếu interval comparator xử lý ties, hãy hỏi domain dùng closed hay half-open intervals.

Trong C phải kiểm tra bounds, allocation, lifetime và ownership. Trong Java cần chú ý boxing, comparator contract, `equals/hashCode`, recursion depth và mutable keys. Trong JavaScript phải để ý `Number` precision, default `.sort()`, `Array.shift()` cost, recursion limit, `Map` vs plain object và UTF-16 string semantics.

## 12. Complexity review phải đi theo toàn pipeline

Đừng chỉ phân tích core loop. Nếu solution sort `O(n log n)` rồi chạy binary search cho mỗi query, total phải gồm cả preprocessing và queries. Nếu mỗi iteration gọi một helper `O(n)`, outer loop nhìn `O(n)` nhưng total có thể `O(n^2)`.

Memory cũng phải tính cả auxiliary arrays, recursion stack, graph edges, hash-table overhead và duplicated representation.

Một solution production còn cần nhìn allocation rate, cache locality và I/O, nhưng Big-O vẫn là lớp reasoning nền tảng.

## 13. Testing: so với oracle nhỏ

Khi implementation phức tạp, hãy giữ một brute-force reference cho small random inputs. Sinh nhiều input nhỏ, chạy cả optimized và brute solution, rồi so output. Đây là **differential testing**.

Ví dụ Segment Tree có thể được so với simple array update + linear range sum. Custom heap có thể được so với sorting reference. Shortest-path implementation có thể được đối chiếu với Floyd–Warshall trên graph nhỏ.

Cách này đặc biệt hiệu quả vì brute force dễ viết đúng hơn optimized structure.

## 14. Khi nào nên dừng tối ưu?

Một solution `O(n log n)` rõ ràng, dễ chứng minh và chạy tốt thường đáng chọn hơn một solution `O(n)` cực kỳ phức tạp nếu constraints không cần mức tối ưu đó. Engineering không chỉ tối thiểu hóa runtime mà còn tối thiểu hóa bug risk và maintenance cost.

Trong phỏng vấn hoặc competitive programming, giới hạn thời gian có thể đẩy ta tới asymptotic tối ưu hơn. Trong production, readability, observability và resilience cũng là constraints thật.

## 15. Ví dụ đầy đủ: Longest subarray có tổng không vượt K với số dương

Brute force thử mọi `l`, mở rộng `r` và tính tổng có thể `O(n^2)`. Nhưng vì tất cả số dương, khi mở rộng `r`, tổng chỉ tăng. Nếu tổng vượt `K`, tăng `l` sẽ chỉ làm tổng giảm. Tính monotonic này cho phép sliding window.

Invariant là: sau khi shrink xong, window `[l,r]` luôn có sum `<= K`. Mỗi index chỉ đi qua `l` hoặc `r` tối đa một lần, nên total `O(n)`.

Nếu array có số âm, monotonicity biến mất và cùng sliding-window proof không còn đúng. Đây là ví dụ điển hình cho việc constraint nhỏ trong đề có thể là lý do toàn bộ algorithm hoạt động.

## 16. Một template reasoning có thể dùng cho mọi bài

Khi tự học hoặc review solution, hãy ép mình trả lời tuần tự:

**Problem model là gì?** Sequence, set, graph, tree, intervals hay state space?

**Operation trọng tâm là gì?** Lookup, range query, shortest path, connectivity, optimization hay enumeration?

**Constraints cho phép complexity nào?**

**Baseline đúng đơn giản nhất là gì?**

**Baseline đang lặp lại work nào?**

**Representation/invariant nào loại được work đó?**

**Tại sao solution đúng?**

**Time/space complexity của toàn pipeline là gì?**

**Assumption nào có thể vỡ ở edge case?**

Nếu trả lời được tám câu này, solution thường đã vượt khỏi mức “nhớ pattern” và trở thành reasoning có thể tái sử dụng.

## Mental Model

> Giải DSA là quá trình **nén search space và repeated work** bằng representation, ordering, invariants và reuse. Một optimization có giá trị khi bạn chỉ ra chính xác phần work nào đã biến mất và vì sao correctness vẫn được giữ.

Xem thêm: [Chọn cấu trúc dữ liệu phù hợp](./00_choose_the_right_data_structure.md), [Correctness & Invariants](../00_foundations/01_algorithm_correctness_and_invariants.md), [Complexity Analysis](../00_foundations/02_complexity_analysis.md).