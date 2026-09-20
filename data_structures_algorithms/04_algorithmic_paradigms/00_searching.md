# Searching
**Tìm kiếm (Searching / 탐색)**

Searching là quá trình thu hẹp tập candidates cho tới khi xác định target hoặc chứng minh nó không tồn tại. Điểm khác nhau giữa các search algorithms là **information nào cho phép loại candidates**.

## Linear search

Nếu dữ liệu không có order/index phụ trợ và chỉ search một lần, linear search có thể là lựa chọn hợp lý:

```c
for (int i = 0; i < n; ++i) {
    if (a[i] == target) return i;
}
```

Worst `O(n)`. Không có structure bổ sung thì ta có thể phải xem mọi phần tử.

## Binary search

Sorted order tạo monotonic information. So sánh midpoint với target cho phép bỏ nửa search space.

```java
int binarySearch(int[] a, int target) {
    int lo = 0, hi = a.length - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}
```

Dùng `lo + (hi-lo)/2` tránh overflow kiểu `(lo+hi)/2` trong integer domains lớn.

## Lower bound và upper bound

Lower bound là vị trí đầu tiên `>= target`; upper bound là vị trí đầu tiên `> target`. Chúng cho phép tìm insertion point và đếm duplicates trong sorted array bằng hiệu hai indices.

## Binary search on answer

Binary search không cần array. Nếu predicate `P(x)` monotonic:

```text
false false false true true true
```

ta tìm `x` đầu tiên khiến `P(x)` true. Ví dụ tìm capacity nhỏ nhất để vận chuyển packages trong `D` ngày: `canShip(capacity)` trở thành predicate.

Đây là bước chuyển mental model quan trọng: binary search hoạt động trên **ordered solution space**.

## Những kiểu search khác

Hash lookup dùng hash function để gần-direct address; BST dùng order theo tree; trie dùng prefix path; BFS/DFS search implicit state graph. “Searching” là family problem chứ không đồng nghĩa binary search.

## Mental Model

> Search nhanh khi một observation cho phép loại bỏ một vùng candidates lớn. Hãy tìm invariant hoặc index làm cho việc loại bỏ đó hợp lệ.

## Half-open interval binary search

Một implementation robust thường dùng `[lo, hi)` thay vì closed interval:

```java
int lowerBound(int[] a, int target) {
    int lo = 0, hi = a.length;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
```

Invariant:

```text
mọi index < lo có value < target
mọi index >= hi có value >= target
answer nằm trong [lo, hi]
```

Khi `lo == hi`, interval candidate rỗng nhưng boundary chính là answer.

## Binary search on real numbers

Nếu predicate/monotonic function trên continuous domain, ta có thể iterate fixed number lần hoặc tới epsilon. Đây là numeric approximation chứ không phải exact discrete search; floating-point error và stopping criterion phải được định nghĩa.

## Exponential search

Nếu upper bound chưa biết, tăng bound theo powers of two:

```text
1,2,4,8,...
```

cho tới khi vượt target condition, rồi binary search interval cuối. Cost vẫn logarithmic theo answer position. Pattern này dùng cho unbounded search spaces hoặc APIs không biết size trước.

## Search và information theory intuition

Binary comparison có hai outcomes chính; mỗi comparison cung cấp khoảng một bit thông tin. Để phân biệt `n` sorted positions cần khoảng `log2 n` bits, nên logarithmic comparisons là natural lower scale.

## Common bug: predicate orientation

Trong binary-search-on-answer, trước khi code hãy viết predicate sequence:

```text
F F F F T T T
```

và xác định tìm first T hay last F. Rất nhiều off-by-one bugs đến từ việc không cố định orientation này.
