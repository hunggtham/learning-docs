# Tính đúng đắn và bất biến của thuật toán
**Algorithm Correctness & Invariants / 알고리즘 정확성과 불변식**

Thuật toán nhanh nhưng sai không có giá trị. Test cho thấy chương trình đúng trên các case đã chạy, nhưng không tự chứng minh rằng algorithm đúng với mọi input hợp lệ. DSA vì vậy cần một lớp reasoning khác: precondition, postcondition, invariant và induction.

## Precondition và postcondition

**Điều kiện trước (Precondition / 사전 조건)** là giả định phải đúng trước khi algorithm chạy. **Điều kiện sau (Postcondition / 사후 조건)** là điều algorithm cam kết sau khi kết thúc.

Binary search có precondition quan trọng: array đã sorted. Postcondition: nếu target tồn tại thì trả về một index hợp lệ, nếu không thì báo không tìm thấy. Nếu array chưa sorted, binary search không chỉ “chậm hơn”; nền tảng suy luận của nó bị phá.

## Loop invariant

**Bất biến vòng lặp (Loop Invariant / 루프 불변식)** là mệnh đề luôn đúng tại một điểm xác định của mỗi iteration.

Với binary search, invariant có thể là:

> Nếu target còn khả năng tồn tại, nó nằm trong đoạn `[lo, hi]`.

Nếu `a[mid] < target`, sorted order chứng minh mọi index `<= mid` không thể chứa target; vì vậy cập nhật `lo = mid + 1` vẫn giữ invariant.

```c
int binary_search(const int *a, int n, int target) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}
```

Cấu trúc chứng minh loop invariant thường gồm initialization, maintenance và termination. Khi loop kết thúc, invariant kết hợp với điều kiện dừng phải dẫn tới postcondition.

## Recursion và induction

Tree algorithms thường được chứng minh bằng **quy nạp (Induction / 수학적 귀납법)**. Với merge sort: array 0 hoặc 1 phần tử đã sorted; giả sử hai nửa nhỏ hơn được sort đúng; nếu procedure merge hai sorted halves là đúng thì toàn array sorted.

Đây không phải mẹo học thuật. Khi viết recursive code, induction chính là cách kiểm tra logic của recursive contract.

## Greedy và exchange argument

Greedy cần một kiểu chứng minh khác. Ta thường giả sử có optimal solution chưa dùng greedy choice, rồi chỉ ra có thể “exchange” một phần của solution đó thành greedy choice mà không làm tệ hơn. Khi làm được, greedy choice được chứng minh safe.

## Assertions như executable invariants

Invariant có thể biến thành assertion trong code nội bộ:

```java
assert size >= 0 && size <= capacity;
```

hoặc trong C:

```c
assert(list->size == counted_nodes);
```

Assertion không thay input validation cho dữ liệu bên ngoài; nó phù hợp để phát hiện programmer assumption bị phá.

## Mental Model

> Correctness là chuỗi reasoning: giả định gì trước khi chạy → điều gì luôn được giữ trong quá trình chạy → tại sao khi dừng điều cần tìm bắt buộc phải đúng.

Khi một algorithm khó hiểu, đừng chỉ đọc code line-by-line. Hãy tìm invariant mà code đang bảo vệ.
