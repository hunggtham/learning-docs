# Phân tích độ phức tạp
**Complexity Analysis / 복잡도 분석**

Độ phức tạp mô tả cách tài nguyên tăng theo kích thước input. Hai tài nguyên cơ bản là **thời gian (Time Complexity / 시간 복잡도)** và **bộ nhớ (Space Complexity / 공간 복잡도)**.

## Tại sao không chỉ đo milliseconds?

Benchmark phụ thuộc CPU, compiler/JIT, cache, runtime và dataset. Asymptotic analysis hỏi một câu ổn định hơn: khi `n` tăng rất lớn, cost tăng theo dạng nào?

Nếu:

\[
T(n)=3n^2+5n+20
\]

thì `n²` chi phối về dài hạn. Ta nói `T(n)` thuộc `O(n²)`. Khi bound chặt cùng bậc, dùng `Θ(n²)`; `Ω` mô tả lower bound.

## Các growth rate quan trọng

| Complexity | Mental model |
|---|---|
| `O(1)` | cost không tăng theo n |
| `O(log n)` | mỗi bước loại một tỷ lệ lớn search space |
| `O(n)` | nhìn qua dữ liệu một lần |
| `O(n log n)` | nhiều tầng chia đôi, mỗi tầng xử lý tổng tuyến tính |
| `O(n²)` | xét nhiều cặp |
| `O(2^n)` | mỗi quyết định nhân số state |
| `O(n!)` | xét permutation |

Binary search giảm search space một nửa:

\[
n,\frac n2,\frac n4,\ldots,1
\]

Nếu sau `k` bước còn 1 phần tử:

\[
\frac{n}{2^k}=1\Rightarrow k=\log_2n
\]

Logarithm xuất hiện vì structure của quá trình, không phải vì ta “gán” công thức.

## Best, average, worst

Linear search tìm phần tử đầu tiên có best case `O(1)`, nhưng worst case `O(n)`. Average case chỉ có nghĩa khi distribution của input được xác định hợp lý.

Hash table thường nói expected/average `O(1)` cho lookup, nhưng worst case có thể `O(n)` nếu collisions xấu.

## Amortized analysis

Dynamic array push đôi khi phải resize và copy toàn bộ dữ liệu. Nếu capacity nhân đôi `1→2→4→8...`, tổng số phần tử từng bị copy tới size `n` nhỏ hơn một hằng số nhân `n`. Vì vậy sequence `n` appends có tổng `O(n)`, tức amortized `O(1)` mỗi append.

Điểm quan trọng: amortized `O(1)` không nói mỗi operation đều `O(1)`.

## Space complexity

Recursive DFS trên tree height `h` dùng call stack `O(h)`. Merge sort thường cần auxiliary array `O(n)`. Quicksort in-place vẫn cần recursion stack expected `O(log n)`, worst `O(n)` nếu partition lệch.

## Complexity và ngôn ngữ

Cùng `O(n)` nhưng constant factor có thể khác. `int[]` trong C/Java có data primitive liên tiếp và locality tốt. `ArrayList<Integer>` Java có boxing/reference overhead. JavaScript Array có runtime representation động; packed dense array thường tối ưu tốt hơn sparse/holey array.

## Common misconception

Hai nested loops không tự động là `O(n²)`. Nếu outer loop nhân `i *= 2`, nó chạy `O(log n)` lần. Ngược lại, một loop có thể ẩn `O(n)` bên trong API như `Array.shift()` hoặc linked-list traversal.

## Mental Model

> Complexity đo cách amount of work hoặc state space tăng theo input. Nó không đo code dài bao nhiêu.

Big-O và benchmark bổ sung nhau: Big-O cho growth model; benchmark cho cost thật trên runtime thật.

## Phân tích một đoạn code từ first principles

Giả sử:

```java
for (int i = 0; i < n; i++) {
    for (int j = 1; j < n; j *= 2) {
        consume(i, j);
    }
}
```

Loop ngoài chạy `n` lần. Loop trong tạo sequence `1, 2, 4, 8, ...` cho tới khi vượt `n`, nên số lần lặp là `floor(log2 n)+1`. Tổng số calls xấp xỉ:

\[
n(\log_2 n + 1)=\Theta(n\log n)
\]

Điểm cần học không phải “nested loops có thể là `n log n`”. Ta phải nhìn **rule cập nhật biến loop** để biết search space giảm hay tăng theo kiểu tuyến tính, logarithmic hay khác.

## Output-sensitive complexity

Đôi khi output tự nó đã lớn. Nếu phải liệt kê mọi edge của một dense graph, output có thể `Theta(V^2)`. Không thể đòi algorithm `O(V)` nếu chỉ việc ghi output đã lớn hơn.

Vì vậy một complexity hữu ích đôi khi có dạng:

\[
O(n+k)
\]

với `k` là số kết quả thực tế. Đây gọi là output-sensitive analysis.

## Pseudopolynomial complexity

Một DP có complexity `O(nW)` với `W` là numeric capacity của knapsack trông như polynomial, nhưng input để biểu diễn `W` chỉ cần `O(log W)` bits. Vì vậy theo input bit-length, `O(nW)` không phải polynomial thực sự; nó là **pseudopolynomial / 의사 다항 시간**.

Distinction này quan trọng khi học knapsack, subset sum và complexity theory.

## Cache complexity và locality

Asymptotic complexity cố tình bỏ qua memory hierarchy. Nhưng hai `O(n)` algorithms có thể khác nhau lớn:

```text
contiguous scan  -> predictable, cache-friendly
pointer chasing  -> frequent cache misses
```

Khi performance thật sự quan trọng, quy trình đúng là:

1. dùng asymptotic analysis để loại design tăng trưởng xấu;
2. dùng representation reasoning để dự đoán constants;
3. benchmark workload thực.

Không nên đảo thứ tự và benchmark một design `O(n^2)` trên input nhỏ rồi kết luận nó tốt.

## Complexity contract của API

Khi dùng library collection, complexity là một phần của contract engineering. Ví dụ Java `ArrayList.get(i)` và `LinkedList.get(i)` cùng trả phần tử theo index nhưng cost model khác hoàn toàn. Code gọi `get(i)` trong loop có thể biến từ tuyến tính thành bậc hai chỉ vì implementation collection thay đổi.

Vì vậy DSA không chỉ nằm trong function bạn tự viết; nó nằm trong **assumption về operation cost của dependency**.
