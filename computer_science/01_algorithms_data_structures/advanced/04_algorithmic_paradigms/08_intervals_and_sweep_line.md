# Interval Algorithms và Sweep Line  
**구간 알고리즘과 스위프 라인**

Nhiều dữ liệu thực tế là intervals: booking time, CPU task duration, genomic ranges, screen rectangles, price validity periods. Khi mỗi interval tương tác với nhiều interval khác, brute-force pairwise comparison dễ thành `O(n^2)`.

## Merge intervals

Sort theo start. Sau đó scan:

```text
nếu next.start <= current.end:
    merge
ngược lại:
    output current và bắt đầu interval mới
```

Sau sorting `O(n log n)`, scan `O(n)`.

Sorting tạo invariant: một interval mới chỉ cần so với merged interval cuối; không cần quay lại mọi interval cũ.

## Meeting rooms và event transformation

Mỗi interval `[start,end)` có thể biến thành hai events:

```text
(start, +1)
(end, -1)
```

Sort events theo time rồi cộng running count. Maximum count là số intervals overlap lớn nhất.

Tie-breaking phụ thuộc semantics `[start,end)` hay closed interval `[start,end]`. Nếu meeting kết thúc đúng lúc meeting khác bắt đầu và room được reuse, `end` event phải được xử lý trước `start` cùng timestamp.

Đây là ví dụ điển hình nơi **domain semantics quyết định comparator**.

## Sweep line

Sweep line tưởng tượng một đường quét qua coordinate/time axis. Ta xử lý events theo order; active set giữ objects hiện đang “cắt” sweep line.

Nếu active set cần ordered queries, balanced BST thường xuất hiện. Nếu chỉ cần count, counter/multiset có thể đủ.

Computational geometry dùng sweep line cho line-segment intersections, rectangle union area và closest structures; scheduling dùng cùng mental model trên time axis.

## Difference coordinates và coordinate compression

Nếu coordinates rất lớn nhưng chỉ một số endpoints thực sự xuất hiện, ta có thể sort unique coordinates và map chúng về indices nhỏ. Đây là **coordinate compression / 좌표 압축**.

Compression giữ order nhưng không giữ raw distance trừ khi ta lưu original coordinates. Segment/Fenwick trees thường kết hợp coordinate compression khi key domain sparse và lớn.

## Mental Model

> Sweep line đổi bài toán “mọi object tương tác với mọi object” thành “xử lý **những thay đổi theo một trục có thứ tự** và duy trì active state”.
