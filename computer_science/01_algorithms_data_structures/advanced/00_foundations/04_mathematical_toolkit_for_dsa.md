# Công cụ Toán học cho Data Structures & Algorithms  
**Mathematical Toolkit for DSA / 알고리즘을 위한 수학 도구**

DSA không đòi hỏi toàn bộ Toán cao cấp, nhưng nó sử dụng một số ý tưởng toán học lặp đi lặp lại: logarithm, tổng hữu hạn, recurrence, tổ hợp, xác suất và proof by induction. Mục tiêu của chương này không phải biến DSA thành môn Toán, mà giúp ta nhìn thấy **vì sao complexity có dạng đó** thay vì học thuộc kết quả.

## Logarithm là số lần có thể chia theo một tỷ lệ

Nếu một search space có kích thước `n` và mỗi bước giảm còn một nửa, sau `k` bước ta có:

\[
\frac{n}{2^k}\approx 1
\]

suy ra:

\[
k\approx \log_2 n
\]

Đây là nguồn gốc của `O(log n)` trong binary search, balanced BST, heap height và nhiều divide-and-conquer algorithms. Cơ số của logarithm không quan trọng trong Big-O vì:

\[
\log_a n = \frac{\log_b n}{\log_b a}
\]

khác nhau chỉ bởi một constant factor.

Mental model cần giữ là:

> `log n` xuất hiện khi mỗi bước loại bỏ hoặc gom lại một **tỷ lệ cố định** của trạng thái còn lại.

## Tổng cấp số và nested loops

Nhiều complexity xuất hiện từ tổng:

\[
1+2+\dots+n=\frac{n(n+1)}2=\Theta(n^2)
\]

Vì vậy loop dạng:

```c
for (int i = 0; i < n; ++i)
    for (int j = 0; j <= i; ++j)
        work();
```

không cần đếm từng iteration. Tổng số `work()` là tam giác số học ở trên.

Một tổng khác quan trọng:

\[
1+2+4+\dots+2^k=2^{k+1}-1
\]

Nó giải thích vì sao một binary tree hoàn chỉnh có số node tăng theo lũy thừa của height, và vì sao height của heap chứa `n` phần tử là `Theta(log n)`.

## Geometric series và amortized dynamic array

Khi capacity tăng gấp đôi, tổng lượng dữ liệu từng phải copy là:

\[
1+2+4+8+\dots+\frac n2 < n
\]

hoặc cùng bậc `O(n)` tùy điểm bắt đầu. Vì thế `n` lần append không phải `O(n^2)` dù một vài lần resize có cost tuyến tính. Đây là một ví dụ mà tổng geometric series trực tiếp trở thành proof cho amortized complexity.

## Recurrence

Recurrence mô tả runtime của recursive algorithm bằng runtime của subproblem.

Merge sort:

\[
T(n)=2T(n/2)+cn
\]

Ta có thể nhìn bằng recursion tree. Mỗi level tổng cộng xử lý `cn`; có khoảng `log n` levels; tổng:

\[
T(n)=\Theta(n\log n)
\]

Binary search:

\[
T(n)=T(n/2)+c
\]

Mỗi level chỉ làm constant work, có `log n` levels, nên `Theta(log n)`.

Quicksort worst case:

\[
T(n)=T(n-1)+cn
\]

mở ra thành:

\[
cn+c(n-1)+\dots+c=\Theta(n^2)
\]

Điều quan trọng là recurrence không phải công thức trang trí. Nó ghi lại **shape của quá trình phân rã vấn đề**.

## Master theorem — dùng khi structure phù hợp

Với recurrence dạng:

\[
T(n)=aT(n/b)+f(n)
\]

`a` là số subproblems, `n/b` là kích thước mỗi subproblem và `f(n)` là chi phí divide/combine.

Master theorem so sánh `f(n)` với:

\[
n^{\log_b a}
\]

để xác định phần nào chi phối. Không nên dùng theorem như máy móc nếu recurrence không có form phù hợp hoặc subproblem sizes không đều; recursion tree hoặc substitution thường trực quan hơn.

## Combinatorics và search space

Backtracking thường sinh subsets, permutations hoặc assignments. Nếu mỗi phần tử có hai lựa chọn “chọn/không chọn”, có:

\[
2^n
\]

subsets.

Nếu sắp xếp `n` phần tử khác nhau:

\[
n!
\]

permutations.

Các con số này không chỉ dùng để tính. Chúng giúp quyết định feasibility. `2^20` khoảng một triệu có thể chấp nhận trong nhiều bài; `2^60` thì không.

## Probability trong hashing và randomized algorithms

Expected complexity cần một random model. Ví dụ randomized quicksort không nói một run chắc chắn `O(n log n)`; nó nói expectation theo random pivot có growth đó.

Hash table cũng thường mô tả lookup expected `O(1)` dưới assumption hashing phân phối keys đủ đều. Nếu input adversarial hoặc hash function kém, assumption có thể vỡ.

## Induction và correctness

Mathematical induction khớp rất tự nhiên với recursive data structures.

Để chứng minh một tree algorithm đúng, ta thường làm:

**Base:** leaf/null subtree đúng.

**Inductive step:** giả sử algorithm đúng trên children, chứng minh combine result ở parent đúng.

Đó chính là structural induction.

## Mental Model

> Toán học trong DSA không phải lớp ký hiệu phủ lên code. Nó là ngôn ngữ để nói chính xác **search space lớn bao nhiêu, một bước loại được bao nhiêu, và work được lặp lại theo cấu trúc nào**.

Xem tiếp: [Complexity Analysis](./02_complexity_analysis.md), [Divide and Conquer](../04_algorithmic_paradigms/03_divide_and_conquer.md), [Dynamic Programming](../04_algorithmic_paradigms/05_dynamic_programming.md).
