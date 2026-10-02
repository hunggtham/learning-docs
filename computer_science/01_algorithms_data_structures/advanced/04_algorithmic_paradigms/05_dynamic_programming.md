# quy hoạch động (dynamic programming)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **quy hoạch động (dynamic programming)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ recursion tới DP** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Optimal substructure và overlapping subproblems** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối dynamic programming với state, transition, memoization và optimal substructure, để tránh tính lặp.

**Quy hoạch động (Dynamic Programming, DP / 동적 계획법)**

quy hoạch động không phải một bộ công thức `dp[i][j]`. Bản chất của DP là **trạng thái (state / 상태) compression + reuse**: nếu nhiều histories khác nhau dẫn đến cùng một trạng thái mà từ trạng thái đó tương lai hành vi giống nhau, ta chỉ cần giải trạng thái một lần rồi tái sử dụng kết quả.

Một cách nói chặt hơn:

> trạng thái DP đại diện cho một **equivalence lớp (class / 클래스) của histories**. Những quá khứ khác nhau được gom thành cùng trạng thái vì mọi quyết định tương lai chỉ cần một dữ liệu tóm lược nhỏ của quá khứ.

Đây là mental mô hình quan trọng hơn việc học thuộc công thức truy hồi.

## Từ recursion tới DP

Hãy bắt đầu bằng recursive bài toán (problem / 문제) definition tự nhiên.

Fibonacci naive:

```text
F(n) = F(n-1) + F(n-2)
```

tạo cây lời gọi với nhiều lần tính lại `F(k)`. Nếu bộ nhớ đệm theo `n`, mỗi trạng thái chỉ tính một lần.

```java
long fib(int n, long[] memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
}
```

Nhưng Fibonacci quá đơn giản. Phần khó thật của DP là trả lời:

```text
state cần lưu information gì để future được xác định?
```

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Optimal substructure và overlapping subproblems** tiếp nhận điểm tựa từ **Từ recursion tới DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **trạng thái thiết kế (design / 설계): tương lai cần biết gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Optimal substructure và overlapping subproblems

Hai concepts thường xuất hiện cùng nhau nhưng không giống nhau.

**Optimal substructure**: lời giải tối ưu của bài toán (problem / 문제) lớn có thể xây từ optimal các lời giải của subproblems phù hợp.

**Overlapping subproblems**: cùng subproblem/trạng thái xuất hiện lặp lại từ nhiều histories.

DP đặc biệt hữu ích khi cả hai cùng có mặt.

Nếu subproblems độc lập không overlap nhiều, divide-and-conquer có thể phù hợp hơn.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **trạng thái thiết kế (design / 설계): tương lai cần biết gì?** tiếp nhận điểm tựa từ **Optimal substructure và overlapping subproblems** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **trạng thái quá nhỏ và trạng thái quá lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## trạng thái thiết kế (design / 설계): tương lai cần biết gì?

0/1 Knapsack có trạng thái phổ biến:

```text
dp[i][w] = giá trị tối đa khi xét first i items và capacity w
```

Tại sao full lịch sử items đã chọn không cần giữ? Vì tương lai chỉ quan tâm:

```text
đã đi tới index nào
capacity còn/đã dùng bao nhiêu
```

Hai histories khác nhau nhưng có cùng `(i,w)` là future-equivalent.

Đây là một cách thiết kế trạng thái có hệ thống: **xóa mọi thông tin của quá khứ không ảnh hưởng tương lai choices**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **trạng thái quá nhỏ và trạng thái quá lớn** tiếp nhận điểm tựa từ **trạng thái thiết kế (design / 설계): tương lai cần biết gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển tiếp (transition / 전이) từ “hành động cuối”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## trạng thái quá nhỏ và trạng thái quá lớn

trạng thái quá nhỏ → merge những histories thực ra có tương lai khác nhau → answer sai.

trạng thái quá lớn → đúng nhưng không gian trạng thái explosion, bộ nhớ/thời gian (time / 시간) lãng phí.

Ví dụ grid có các khóa/doors:

```text
(row,col)
```

có thể quá nhỏ; cần `(row,col,keysMask)`.

Ngược lại lưu toàn bộ đường đi tới cell là quá lớn nếu tương lai chỉ cần khóa set.

trạng thái thiết kế (design / 설계) của DP và visited-trạng thái thiết kế (design / 설계) của đồ thị tìm kiếm (search / 검색) là cùng một bài toán (problem / 문제).

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Chuyển tiếp (transition / 전이) từ “hành động cuối”** tiếp nhận điểm tựa từ **trạng thái quá nhỏ và trạng thái quá lớn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Top-down và bottom-up** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển tiếp (transition / 전이) từ “hành động cuối”

Một technique rất mạnh là phân loại lời giải tối ưu theo **last hành động (action / 동작)**.

Edit khoảng cách:

```text
dp[i][j] = minimum edits biến A[0..i) thành B[0..j)
```

thao tác cuối chỉ có thể là:

```text
insert B[j-1]
delete A[i-1]
replace/match A[i-1] với B[j-1]
```

Từ đó công thức truy hồi xuất hiện tự nhiên.

Nếu chars bằng:

\[
dp[i][j] = dp[i-1][j-1]
\]

Nếu khác:

\[
dp[i][j] = 1 + \min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
\]

Đây là “derive công thức truy hồi”, không phải memorize công thức truy hồi.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Top-down và bottom-up** tiếp nhận điểm tựa từ **Chuyển tiếp (transition / 전이) từ “hành động cuối”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DP như DAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Top-down và bottom-up

**Top-down / memoization**:

```text
viết recursion tự nhiên
cache state đã giải
chỉ tính states reachable
```

**Bottom-up / tabulation**:

```text
xác định dependency order
fill table theo thứ tự đó
không cần recursion stack
```

Không có phương án nào luôn tốt hơn.

Sparse có thể tới không gian trạng thái có thể hợp top-down. Dense regular bảng (table / 테이블) thường hợp bottom-up và tính cục bộ bộ nhớ đệm tốt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **DP như DAG** tiếp nhận điểm tựa từ **Top-down và bottom-up** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fibonacci không gian (space / 공간) tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP như DAG

Xem mỗi trạng thái là đỉnh, mỗi phụ thuộc (dependency / 의존성) là directed cạnh.

Nếu trạng thái `A` phụ thuộc trạng thái `B`, có cạnh:

```text
B -> A
```

DP computation đồ thị phải acyclic theo dimension/thứ tự (order / 순서) phù hợp. Bottom-up chỉ đơn giản là evaluate các trạng thái theo một thứ tự tô-pô.

Mental liên kết (connection / 연결):

```text
DP table
≈ DAG of states
≈ reuse repeated subproblems
```

Điều này giúp chuyển đổi giữa đồ thị đường đi ngắn nhất (shortest path) và DP.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Fibonacci không gian (space / 공간) tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **DP như DAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **0/1 Knapsack và vòng lặp (loop / 루프) direction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fibonacci không gian (space / 공간) tối ưu hóa (optimization / 최적화)

Nếu chuyển tiếp (transition / 전이) chỉ cần hai các trạng thái trước:

```text
F(i) depends on F(i-1), F(i-2)
```

không cần mảng `O(n)`; chỉ giữ rolling variables `O(1)`.

Không gian (space / 공간) tối ưu hóa (optimization / 최적화) xuất phát từ phụ thuộc (dependency / 의존성) width, không phải trick riêng.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **0/1 Knapsack và vòng lặp (loop / 루프) direction** tiếp nhận điểm tựa từ **Fibonacci không gian (space / 공간) tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Unbounded knapsack** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 0/1 Knapsack và vòng lặp (loop / 루프) direction

2D công thức truy hồi:

\[
dp[i][w]=\max(dp[i-1][w], dp[i-1][w-weight_i]+value_i)
\]

Nếu compress thành 1D:

```java
for (Item item : items) {
    for (int w = capacity; w >= item.weight; --w) {
        dp[w] = Math.max(dp[w], dp[w - item.weight] + item.value);
    }
}
```

Sức chứa (capacity / 용량) phải iterate giảm. Nếu đi tăng, `dp[w-item.weight]` có thể đã dùng chính item hiện tại và ta vô tình đổi bài thành unbounded knapsack.

Vòng lặp (loop / 루프) direction là part của mathematical ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Unbounded knapsack** tiếp nhận điểm tựa từ **0/1 Knapsack và vòng lặp (loop / 루프) direction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Coin thay đổi (change / 변경) và ngữ nghĩa của “cách”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Unbounded knapsack

Nếu mỗi item được dùng unlimited times, sức chứa (capacity / 용량) vòng lặp (loop / 루프) tăng là đúng:

```text
for item:
    for w = weight .. capacity:
        dp[w] = max(dp[w], dp[w-weight] + value)
```

Hai problems khác nhau chỉ bởi reuse chính sách, nhưng cách triển khai thứ tự (order / 순서) phản ánh difference đó.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Coin thay đổi (change / 변경) và ngữ nghĩa của “cách”** tiếp nhận điểm tựa từ **Unbounded knapsack** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Longest Phổ biến Subsequence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coin thay đổi (change / 변경) và ngữ nghĩa của “cách”

Có nhiều bài coin thay đổi (change / 변경):

```text
có tạo được amount không?
ít coin nhất?
số combinations?
số permutations/orderings?
```

Cùng trạng thái dimension có thể cho giá trị ngữ nghĩa khác.

Đếm combinations thường dùng coins vòng lặp bên ngoài:

```text
for coin:
    for amount increasing:
        ways[x] += ways[x-coin]
```

Nếu amount outer, coin inner, ta có thể đếm ordered sequences.

Vòng lặp (loop / 루프) thứ tự (order / 순서) chính là cách ta định nghĩa combinatorial đối tượng được đếm.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Longest Phổ biến Subsequence** tiếp nhận điểm tựa từ **Coin thay đổi (change / 변경) và ngữ nghĩa của “cách”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LCS reconstruction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Longest Phổ biến Subsequence

trạng thái:

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

trực giác chứng minh: nếu chars cuối khác nhau, một LCS optimal không thể cần dùng cả hai chars đó cùng vị trí matching; ít nhất một bên bị bỏ, nên hai subproblems cover possibilities.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **LCS reconstruction** tiếp nhận điểm tựa từ **Longest Phổ biến Subsequence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Longest Increasing Subsequence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LCS reconstruction

Bảng giá trị chỉ trả về độ dài. Muốn khôi phục dãy con thực tế, cần lần ngược lại các lựa chọn:

```text
nếu chars equal -> take char, move diagonal
else move về neighbor có dp lớn hơn
```

Nếu đã compress bộ nhớ xuống hai rows, reconstruction khó hơn vì lịch sử bị bỏ. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa bộ nhớ và thông tin retention.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Longest Increasing Subsequence** tiếp nhận điểm tựa từ **LCS reconstruction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Grid DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Longest Increasing Subsequence

Kinh điển DP:

\[
dp[i]=1+\max(dp[j]) \quad j<i, a[j]<a[i]
\]

Thời gian (time / 시간) `O(n^2)`.

thuật toán `O(n log n)` giữ:

```text
tails[len] = smallest possible tail của increasing subsequence length len+1
```

Mỗi giá trị binary-search vị trí trong `tails`.

`tails` không nhất thiết là actual LIS ở mọi thời điểm; nó là **compressed frontier** của possibilities. Đây là một ví dụ sâu về trạng thái compression vượt khỏi bảng (table / 테이블) DP truyền thống.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Grid DP** tiếp nhận điểm tựa từ **Longest Increasing Subsequence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interval DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Grid DP

Grid đường đi problems thường có natural phụ thuộc (dependency / 의존성):

```text
dp[r][c] depends on top/left/diagonal
```

Nếu movement chỉ đi xuống/phải, đồ thị trạng thái là DAG theo row+column thứ tự (order / 순서).

Nếu movement cho phép chu trình, naive grid DP không còn trực tiếp; có thể cần đồ thị đường đi ngắn nhất hoặc detect another monotonic dimension.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Interval DP** tiếp nhận điểm tựa từ **Grid DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ma trận (matrix / 행렬) chuỗi (chain / 사슬) Multiplication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interval DP

Interval DP dùng trạng thái:

```text
dp[l][r] = answer cho subarray/subsequence interval [l,r]
```

Transitions thường split interval tại `k` hoặc quyết định endpoints.

Examples:

```text
matrix-chain multiplication
optimal BST
burst balloons
palindrome interval problems
```

Thứ tự tính từ dưới lên thường đi theo độ dài khoảng tăng dần:

```text
for len = 1..n:
    for l:
        r = l + len - 1
```

Vì smaller intervals phải có trước larger intervals.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Interval DP** xác định đầu vào; **Ma trận (matrix / 행렬) chuỗi (chain / 사슬) Multiplication** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **cây DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ma trận (matrix / 행렬) chuỗi (chain / 사슬) Multiplication

Dimensions `p0,p1,...,pn`. trạng thái:

```text
dp[i][j] = minimum scalar multiplications để nhân matrices i..j
```

Try last split `k`:

\[
dp[i][j] = \min_k dp[i][k] + dp[k+1][j] + p_{i-1}p_kp_j
\]

Đây là classic “choose partition điểm (point / 지점)” interval DP.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Ma trận (matrix / 행렬) chuỗi (chain / 사슬) Multiplication** xác định đầu vào; **cây DP** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Rerooting DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây DP

Fix nút cha để nút con các cây con độc lập.

Maximum independent set:

```text
dp[u][0] = best nếu không chọn u
dp[u][1] = best nếu chọn u
```

Nếu chọn `u`, các nút con không được chọn.

Nếu không chọn `u`, mỗi nút con chọn tốt nhất giữa two các trạng thái.

cây DP mạnh vì cây itself cung cấp acyclic phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Rerooting DP** tiếp nhận điểm tựa từ **cây DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bitmask DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rerooting DP

Nếu cần answer cho mọi nút khi coi nút đó là nút gốc, tính lại từ đầu là `O(n^2)`.

Rerooting reuse:

```text
child contribution
+ contribution từ phần ngoài child subtree
```

Pass 1 bottom-up, pass 2 top-down.

Đây là message-passing DP trên cây.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Bitmask DP** tiếp nhận điểm tựa từ **Rerooting DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Subset DP và SOS DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bitmask DP

Nếu `n` nhỏ, subset có thể encode bằng bitmask.

Travelling Salesman DP:

```text
dp[mask][u] = minimum cost visit set mask và kết thúc tại u
```

Chuyển tiếp (transition / 전이) add new đỉnh.

Số trạng thái có thể là `O(2^n n)`. Bitmask không làm biến mất độ phức tạp hàm mũ; nó tổ chức không gian tìm kiếm hàm mũ để tái sử dụng các trạng thái chồng lặp.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Subset DP và SOS DP** tiếp nhận điểm tựa từ **Bitmask DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Digit DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Subset DP và SOS DP

Nếu cần tổng hợp trên mọi mặt nạ con hoặc mặt nạ bao, Sum Over Subsets DP (SOS DP) có thể biến các vòng lặp đơn giản `O(3^n)` thành khoảng `O(n2^n)`.

Đây là quy hoạch động trên lattice của subsets.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Digit DP** tiếp nhận điểm tựa từ **Subset DP và SOS DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Profile DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Digit DP

Digit DP đếm numbers thỏa ràng buộc trong phạm vi (range / 범위) bằng trạng thái như:

```text
position
tight?        // prefix có đang bằng bound không
started?      // đã bắt đầu số chưa
additional property: sum/mod/count/etc
```

trạng thái `tight` là ví dụ rõ về future-relevant thông tin: nếu prefix đã nhỏ hơn cận trên (upper bound), tương lai digits không còn bị bound digit hiện tại giới hạn.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Profile DP** tiếp nhận điểm tựa từ **Digit DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DP on DAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Profile DP

Các bài toán lát bảng hoặc bài toán theo biên có thể mã hóa trạng thái của một “biên” nhỏ bằng bitmask rồi quét qua từng hàng hoặc cột.

Thay vì lưu trạng thái của toàn bộ bảng với kích thước hàm mũ, ta chỉ giữ phần biên cục bộ còn ảnh hưởng đến các bước tiếp theo.

Đây là một form sophisticated của trạng thái compression.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **DP on DAG** tiếp nhận điểm tựa từ **Profile DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **đường đi ngắn nhất và DP khác nhau ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP on DAG

Nếu đồ thị là DAG, shortest/longest đường đi có thể giải bằng thứ tự tô-pô.

trạng thái:

```text
dp[v] = best value tới v
```

Relax outgoing các cạnh một lần theo topo thứ tự (order / 순서).

Negative cạnh vẫn okay vì không có chu trình.

Đây là cầu nối (bridge / 브리지) trực tiếp giữa các thuật toán đồ thị và DP.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **đường đi ngắn nhất và DP khác nhau ở đâu?** tiếp nhận điểm tựa từ **DP on DAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DP với monotone hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## đường đi ngắn nhất và DP khác nhau ở đâu?

Bellman-Ford có thể được nhìn như lặp lại relaxation DP theo số các cạnh used:

```text
dp[k][v] = shortest path tới v dùng <= k edges
```

Nhưng các thuật toán đồ thị thường khai thác cấu trúc (structure / 구조)/frontier để tránh tường minh (explicit / 명시적) dimension.

Nhiều distinctions giữa “DP” và “thuật toán đồ thị” là cách triển khai/cấu trúc (structure / 구조) emphasis hơn là mathematical wall.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **DP với monotone hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **đường đi ngắn nhất và DP khác nhau ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prefix minima/maxima tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP với monotone hàng đợi (queue / 큐)

Một chuyển tiếp (transition / 전이) dạng:

\[
dp[i]=\min_{j \in cửa sổ (window / 윈도우)(i)}(dp[j]+cost)
\]

có thể được optimize bằng deque nếu ứng viên giá trị có monotonic cấu trúc (structure / 구조).

DP tối ưu hóa (optimization / 최적화) thường là tìm cách tăng tốc chuyển tiếp (transition / 전이), không chỉ giảm number các trạng thái.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Prefix minima/maxima tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **DP với monotone hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Divide-and-conquer tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prefix minima/maxima tối ưu hóa (optimization / 최적화)

Nếu chuyển tiếp (transition / 전이) cần:

```text
min(dp[0..i-1])
```

đừng quét lại mỗi trạng thái; giữ prefix minimum.

Đây là reuse ở tầng chuyển tiếp (transition / 전이) computation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Divide-and-conquer tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **Prefix minima/maxima tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Knuth tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Divide-and-conquer tối ưu hóa (optimization / 최적화)

Một số DP dạng partition:

\[
dp[k][i] = \min_{j<i}(dp[k-1][j]+C(j,i))
\]

có monotonic optimal split các tính chất cho phép divide-and-conquer tối ưu hóa (optimization / 최적화).

Điều kiện chứng minh không trivial; không áp dụng chỉ vì công thức truy hồi “trông giống”. Nhưng nó cho thấy advanced DP thường dựa vào cấu trúc (structure / 구조) của argmin/chuyển tiếp (transition / 전이) ma trận (matrix / 행렬).

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Knuth tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **Divide-and-conquer tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Convex Hull Trick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Knuth tối ưu hóa (optimization / 최적화)

Một số interval DP thỏa quadrangle inequality/monotonicity có thể giảm cubic xuống quadratic.

Không cần học thuộc mọi theorem ngay, nhưng mental mô hình là:

> Sau khi thiết kế đúng trạng thái/chuyển tiếp (transition / 전이), bước tiếp theo là khai thác additional cấu trúc (structure / 구조) để giảm chuyển tiếp (transition / 전이) tìm kiếm (search / 검색).

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Convex Hull Trick** tiếp nhận điểm tựa từ **Knuth tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **xác suất DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Convex Hull Trick

DP chuyển tiếp (transition / 전이) dạng tuyến tính:

\[
dp[i] = \min_j(m_j x_i + b_j)
\]

có thể được tối ưu bằng cấu trúc dữ liệu giữ lines và truy vấn min/max.

Li Chao cây (tree / 트리) hoặc Convex Hull Trick biến bước “duyệt mọi j” thành một truy vấn hình học.

Đây là nơi DP kết nối với computational hình học (geometry / 기하학)/các cấu trúc dữ liệu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **xác suất DP** tiếp nhận điểm tựa từ **Convex Hull Trick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DP modulo arithmetic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## xác suất DP

trạng thái giá trị không nhất thiết min/max/count; có thể là xác suất/kỳ vọng giá trị.

kỳ vọng steps thường dùng law of total expectation:

\[
E[s] = 1 + \sum_t P(s\to t)E[t]
\]

Nhưng nếu transitions chu trình, equations có thể không có đơn giản topological DP; đôi khi cần solve tuyến tính (linear / 선형) các hệ thống hoặc transform các trạng thái.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **DP modulo arithmetic** tiếp nhận điểm tựa từ **xác suất DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Infinity giá trị canh gác (sentinel) và tràn số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP modulo arithmetic

Combinatorial count có thể rất lớn. Problems thường yêu cầu mod `M`.

Cần chú ý tràn số trước modulo trong C/Java, và Number an toàn phạm vi (range / 범위) trong JavaScript.

Modulo changes numeric cách biểu diễn (representation / 표현), không thay combinatorial công thức truy hồi.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Infinity giá trị canh gác (sentinel) và tràn số** tiếp nhận điểm tựa từ **DP modulo arithmetic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Memo khóa thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Infinity giá trị canh gác (sentinel) và tràn số

Minimum DP thường initialize `INF`.

Đừng dùng maximum integer rồi cộng chi phí:

```text
INF + cost -> overflow
```

Use sufficiently an toàn giá trị canh gác (sentinel) hoặc guard:

```java
if (dp[prev] < INF) {
    dp[cur] = Math.min(dp[cur], dp[prev] + cost);
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Memo khóa thiết kế (design / 설계)** tiếp nhận điểm tựa từ **Infinity giá trị canh gác (sentinel) và tràn số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sparse trạng thái DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memo khóa thiết kế (design / 설계)

Top-down DP với compound trạng thái cần chuẩn gốc (canonical / 정본) khóa.

Java có thể dùng các mảng indexed dimensions hoặc bất biến sau khi tạo bản ghi (record / 레코드).

JavaScript `Map` đối tượng các khóa dùng định danh (identity / 식별자), nên `{i:1,j:2}` mới mỗi lần không match trước đó đối tượng. Cần encode khóa string/int hoặc nested maps.

C phải quản bảng băm (hash table / 해시 테이블)/mảng quyền sở hữu (ownership / 소유권) rõ.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Sparse trạng thái DP** tiếp nhận điểm tựa từ **Memo khóa thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DP và bộ nhớ tính cục bộ (locality)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sparse trạng thái DP

Nếu theoretical không gian trạng thái rất lớn nhưng có thể tới các trạng thái ít, hash-map memoization có thể tốt hơn dense mảng.

Examples:

```text
DP theo large coordinate values
state machine với many impossible combinations
search + memo hybrid
```

sự đánh đổi: băm (hash / 해시) overhead vs skipping unreachable các trạng thái.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **DP và bộ nhớ tính cục bộ (locality)** tiếp nhận điểm tựa từ **Sparse trạng thái DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reconstruction strategies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP và bộ nhớ tính cục bộ (locality)

2D `dp[i][j]` theo thứ tự hàng traversal thường thân thiện với bộ nhớ đệm nếu vòng lặp bên trong đi contiguous.

Changing vòng lặp (loop / 루프) thứ tự (order / 순서) có thể ảnh hưởng môi trường chạy (runtime) rất mạnh dù Big-O giống nhau.

Rolling mảng vừa giảm bộ nhớ vừa cải thiện bộ nhớ đệm, nhưng có thể làm reconstruction khó hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Reconstruction strategies** tiếp nhận điểm tựa từ **DP và bộ nhớ tính cục bộ (locality)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Counting vs optimizing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reconstruction strategies

Có ba cách phổ biến:

```text
1. store parent/choice trực tiếp
2. backtrack bằng cách so dp values
3. recompute một phần nếu memory optimized
```

Store choices tăng bộ nhớ nhưng đơn giản.

Recomputation tiết kiệm bộ nhớ nhưng tăng CPU.

Thiết kế (design / 설계) phụ thuộc đầu ra yêu cầu.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Counting vs optimizing** tiếp nhận điểm tựa từ **Reconstruction strategies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **trạng thái explosion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Counting vs optimizing

Một công thức truy hồi có thể cần:

```text
best value
number of best ways
lexicographically smallest optimal solution
```

Nếu tie ngữ nghĩa quan trọng, trạng thái giá trị có thể phải lưu tuple hoặc extra siêu dữ liệu.

“DP đúng giá trị” chưa chắc đủ cho requested đầu ra.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **trạng thái explosion** tiếp nhận điểm tựa từ **Counting vs optimizing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Meet-in-the-middle vs DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## trạng thái explosion

Nếu trạng thái dimensions:

```text
n * capacity * mask * last * flag
```

Sản phẩm (product / 제품) có thể quá lớn.

Trước khi mã (code / 코드), estimate:

```text
#states * transition cost * bytes/state

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.
```

DP feasibility là kỹ thuật (engineering / 엔지니어링) calculation, không chỉ asymptotic label.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Meet-in-the-middle vs DP** tiếp nhận điểm tựa từ **trạng thái explosion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **giả đa thức độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Meet-in-the-middle vs DP

Subset problems với `n≈40` có thể quá lớn cho `2^n`, nhưng split thành hai halves khoảng `2^(n/2)` rồi kết hợp có thể hiệu quả.

Nếu numeric sum dimension nhỏ, giả đa thức DP có thể tốt hơn.

thuật toán choice phụ thuộc both `n` và giá trị ranges.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **giả đa thức độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **Meet-in-the-middle vs DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DP vs Greedy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## giả đa thức độ phức tạp (complexity / 복잡도)

Knapsack `O(nW)` là đa thức theo giá trị số `W`, nhưng không phải đa thức theo độ dài biểu diễn đầu vào `log W`.

Đây gọi là giả đa thức.

Hiểu distinction này quan trọng khi nối DSA với computational độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **DP vs Greedy** tiếp nhận điểm tựa từ **giả đa thức độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dominance pruning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP vs Greedy

Greedy giữ một frontier nhỏ vì prove cục bộ choice an toàn.

DP giữ nhiều các trạng thái vì chưa thể loại alternatives sớm.

Nếu tìm được dominance/exchange tính chất mạnh, một DP có thể collapse thành greedy.

Ngược lại nếu lựa chọn tham lam có regret, DP giữ competing possibilities.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Dominance pruning** tiếp nhận điểm tựa từ **DP vs Greedy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DP tính đúng đắn chứng minh template** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dominance pruning

Trong một số bài quy hoạch động hoặc tìm kiếm, trạng thái A lấn át B nếu A không tệ hơn B trên mọi chiều còn ảnh hưởng tới tương lai.

Ta có thể discard dominated các trạng thái.

Ví dụ resource-constrained đường đi giữ Pareto frontier giữa chi phí/thời gian (time / 시간). Đây là trạng thái pruning thay vì chính xác khóa equality reuse.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **DP tính đúng đắn chứng minh template** tiếp nhận điểm tựa từ **Dominance pruning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP tính đúng đắn chứng minh template

Một chứng minh tốt thường gồm:

```text
1. định nghĩa state chính xác
2. chứng minh base cases
3. chứng minh transition cover mọi valid solution
4. chứng minh không bỏ candidate optimal
5. chứng minh evaluation order thỏa dependencies
```

Nếu tối ưu hóa (optimization / 최적화) không gian (space / 공간), còn phải chứng minh overwrite thứ tự (order / 순서) không làm dùng trạng thái mới sai ngữ nghĩa.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **kiểm thử DP** tiếp nhận điểm tựa từ **DP tính đúng đắn chứng minh template** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử DP

Brute force trên small n là oracle rất mạnh.

Workflow:

```text
generate random small instance
solve brute-force exhaustive
solve DP
compare
```

Đây là cách bắt trạng thái/loop-order bugs tốt hơn nhiều examples thủ công.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **quy hoạch động (dynamic programming)**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **kiểm thử DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một workflow thiết kế DP có thể tái sử dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

“Có recursion là DP” — sai. DP cần lặp lại equivalent các trạng thái hoặc structured đồ thị trạng thái đáng reuse.

“Có `dp[]` mảng là DP” — naming không quan trọng; trạng thái ngữ nghĩa mới quan trọng.

“Bottom-up luôn nhanh hơn” — sparse các trạng thái có thể hợp memoization.

“không gian (space / 공간) tối ưu hóa (optimization / 최적화) luôn tốt” — có thể mất reconstruction/debuggability.

“DP độ phức tạp (complexity / 복잡도) = số các trạng thái” — còn phải nhân chuyển tiếp (transition / 전이) chi phí.

“Thứ tự vòng lặp chỉ là chi tiết triển khai” — sai; trong nhiều bài quy hoạch động, thứ tự vòng lặp quyết định ngữ nghĩa tái sử dụng trạng thái và cả tính đúng đắn.

> **Chuyển mạch:** Trong **quy hoạch động (dynamic programming)**, **Những hiểu lầm phổ biến** xác định đầu vào; **Một workflow thiết kế DP có thể tái sử dụng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một workflow thiết kế DP có thể tái sử dụng

Khi gặp bài toán (problem / 문제):

```text
1. Viết brute-force recursion tự nhiên.
2. Xác định arguments nào quyết định future -> đó là candidate state.
3. Tìm repeated states.
4. Định nghĩa chính xác dp[state] nghĩa gì.
5. Derive transition từ last/first decision.
6. Xác định base cases.
7. Estimate #states và cost/transition.
8. Chọn top-down hay bottom-up.
9. Nếu cần, optimize memory/transition.
10. Thiết kế reconstruction và test với brute force.
```

Nếu bước 4 không thể nói bằng một câu rõ ràng, mã (code / 코드) DP thường rất dễ sai.

> **Chuyển mạch:** Ở chặng này của **quy hoạch động (dynamic programming)**, **Mô hình tư duy** gom các mảnh từ **Một workflow thiết kế DP có thể tái sử dụng** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> DP là nghệ thuật tìm **dữ liệu tóm lược nhỏ nhất của quá khứ mà tương lai cần biết**. Khi dữ liệu tóm lược đúng, nhiều histories collapse thành một trạng thái; khi trạng thái được reuse, exponential tìm kiếm (search / 검색) có thể biến thành polynomial hoặc giả đa thức computation. Sau đó tối ưu hóa (optimization / 최적화) nâng cao tập trung vào giảm số các trạng thái, giảm chuyển tiếp (transition / 전이) chi phí hoặc giảm bộ nhớ.

Câu hỏi cốt lõi luôn là:

```text
Hai histories nào có future giống nhau?
State tối thiểu để phân biệt future là gì?
Transition cover mọi possibility chưa?
Dependency graph có order nào?
Có dominance/monotonicity/convexity để optimize không?
```

Xem thêm: [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Greedy](./04_greedy_algorithms.md), [DAG/SCC](../03_graphs/04_dag_topological_sort_and_scc.md), [Bit Manipulation](../05_specialized/02_bit_manipulation_and_bitsets.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
