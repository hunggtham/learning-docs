# Dynamic Programming
**Quy hoạch động (Dynamic Programming, DP / 동적 계획법)**

DP không phải tập công thức. Bản chất là: nếu nhiều đường reasoning dẫn tới cùng một state, hãy giải state đó một lần và reuse.

## Overlapping subproblems

Naive Fibonacci tạo call tree chứa cùng `F(k)` nhiều lần. Memoization biến nó thành `O(n)`:

```java
long fib(int n, long[] memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib(n-1, memo) + fib(n-2, memo);
}
```

Nhưng phần khó thật của DP là **state design**.

## State phải giữ đủ future-relevant information

0/1 Knapsack có thể định nghĩa:

```text
dp[i][w] = giá trị tối đa khi xét first i items và capacity w
```

Transition:

\[
dp[i][w]=\max(dp[i-1][w],\ dp[i-1][w-weight_i]+value_i)
\]

nếu item vừa capacity.

Ta không giữ full history vì `(i,w)` đã đủ để future decisions không cần biết chi tiết đường đi trước đó.

## Top-down và bottom-up

Top-down = recursion + memoization, gần recurrence và chỉ tính reachable states. Bottom-up xác định dependency order rồi fill table.

DP state dependencies thường tạo DAG. Nếu state A phụ thuộc B, bottom-up phải đảm bảo B có trước A.

## Space optimization

0/1 knapsack có thể dùng 1D array nếu iterate capacity giảm:

```java
for (Item item : items) {
    for (int w = capacity; w >= item.weight; --w) {
        dp[w] = Math.max(dp[w], dp[w-item.weight] + item.value);
    }
}
```

Đi ngược là essential: nếu đi tăng, value vừa update có thể bị reuse trong cùng item iteration, vô tình đổi bài toán thành unbounded knapsack.

## Các family lớn

Sequence DP gồm LCS, edit distance, LIS; grid DP cho paths; interval DP; tree DP; bitmask DP cho subset state; digit DP cho numeric digit constraints.

## DP như graph

Có thể xem mỗi state là node và transition là edge. Nhiều DP chính là shortest/longest path trên DAG state graph với ordering thuận lợi.

## Mental Model

> DP = state compression + reuse. Câu hỏi then chốt là: hai partial histories nào có thể coi là tương đương vì từ đây future của chúng giống nhau?

## Một quy trình thiết kế DP có thể tái sử dụng

Khi gặp bài toán, trước hết viết recursive definition chưa tối ưu. Mỗi function call phải được mô tả bằng một state tuple. Sau đó hỏi: cùng tuple có được gọi từ nhiều paths không? Nếu có, memoization có thể loại recomputation.

Tiếp theo, xác định transition graph giữa states. Nếu muốn bottom-up, tìm một topological order của graph ngầm này. Cuối cùng, xem state cũ nào còn cần giữ để tối ưu memory.

Quy trình này đáng tin hơn việc “đoán dp[i][j]”.

## Coin change: cùng bài toán nhưng objective khác tạo DP khác

Với coins và amount, có ít nhất ba bài khác nhau:

```text
Có tạo được amount không?
Ít coin nhất là bao nhiêu?
Có bao nhiêu cách tạo amount?
```

State có thể cùng là amount, nhưng value semantics và transition khác.

Minimum coins:

\[
dp[x]=1+\min_{c\le x}dp[x-c]
\]

Count combinations cần cẩn thận loop order. Nếu iterate coins ngoài, amount trong tăng, ta đếm combinations không phân biệt permutation. Nếu đảo loops, có thể đếm ordered sequences.

Loop order ở DP vì thế là một phần của mathematical definition, không chỉ implementation detail.

## Longest Common Subsequence

Cho strings `A`, `B`:

```text
dp[i][j] = LCS length của A[0..i) và B[0..j)
```

Nếu last chars bằng nhau:

\[
dp[i][j]=dp[i-1][j-1]+1
\]

Nếu khác:

\[
dp[i][j]=\max(dp[i-1][j],dp[i][j-1])
\]

Tại sao? Một LCS optimal khi chars cuối khác nhau không thể bắt buộc dùng cả hai chars cuối; ít nhất một char cuối bị bỏ, nên hai candidate subproblems cover possibilities.

## Edit distance

State `dp[i][j]` là minimum edits biến prefix A length i thành prefix B length j.

Transitions tương ứng với operation cuối cùng:

```text
delete A[i-1]
insert B[j-1]
replace/match A[i-1] với B[j-1]
```

Đây là một pattern rất tổng quát: **phân loại optimal solution theo hành động cuối cùng** để derive recurrence.

## LIS: từ O(n²) DP tới O(n log n)

Classic DP:

\[
dp[i]=1+\max(dp[j])\quad j<i, a[j]<a[i]
\]

`O(n^2)`.

Một algorithm nhanh hơn duy trì `tails[len]` = tail nhỏ nhất có thể của increasing subsequence có length `len+1`. Mỗi element binary-search vị trí thay thế trong `tails`, tổng `O(n log n)`.

`tails` không nhất thiết là một subsequence thực hoàn chỉnh tại mọi thời điểm; nó là compressed frontier của possibilities. Đây là ví dụ mạnh của state compression ngoài traditional DP table.

## Tree DP

Tree không có cycles, nên child subproblems tự nhiên độc lập khi condition qua parent được cố định.

Ví dụ maximum independent set trên tree có thể dùng:

```text
dp[u][0] = best ở subtree u khi không chọn u
dp[u][1] = best ở subtree u khi chọn u
```

Nếu chọn u, children không được chọn. Nếu không chọn u, mỗi child chọn trạng thái tốt hơn.

## Reconstruction

DP value thường chưa trả actual solution. Ta có thể lưu choice/parent hoặc backtrack từ table bằng cách xem transition nào tạo giá trị hiện tại.

Trong memory-optimized DP, reconstruction có thể khó hơn vì đã vứt rows cũ. Đây là trade-off giữa memory và information retention.

## Common misconceptions

Không phải bài có recursion là DP. DP cần repeated equivalent states hoặc DAG state computation đáng reuse.

Không phải mọi `dp[i]` đều đại diện “best tới i”. State phải xuất phát từ **information future cần biết**, không từ thói quen đặt index.

Không phải tabulation luôn tốt hơn memoization. Sparse reachable state space có thể khiến top-down chỉ tính phần cần thiết.

## Mental Model mở rộng

> Một state DP là một **equivalence class của histories**: nhiều quá khứ khác nhau được gom lại vì từ thời điểm đó, mọi quyết định tương lai chỉ cần cùng một summary.

Đây là cách nghĩ giúp thiết kế state bền vững hơn học thuộc recurrence.
