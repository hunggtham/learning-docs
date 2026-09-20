# Selection, k-th Element và Top-K  
**선택 알고리즘과 Top-K**

Nếu chỉ cần phần tử nhỏ thứ `k`, sorting toàn bộ tạo nhiều information hơn yêu cầu. Sort xác định relative order của mọi phần tử; selection chỉ cần biết boundary quanh rank `k`.

## Quickselect

Quickselect dùng partition như quicksort. Sau partition, pivot nằm ở final rank `p`.

Nếu `k == p`, xong. Nếu `k < p`, chỉ tiếp tục bên trái. Nếu `k > p`, chỉ tiếp tục bên phải.

Expected recurrence với reasonably balanced/random pivots dẫn tới expected `O(n)` vì ta chỉ recurse một side. Worst case vẫn `O(n^2)` nếu partitions liên tục cực lệch.

### JavaScript

```js
function quickselect(a, k) {
  let lo = 0, hi = a.length - 1;

  while (lo <= hi) {
    const pivotIndex = lo + Math.floor(Math.random() * (hi - lo + 1));
    [a[pivotIndex], a[hi]] = [a[hi], a[pivotIndex]];
    const pivot = a[hi];

    let p = lo;
    for (let i = lo; i < hi; i++) {
      if (a[i] < pivot) {
        [a[i], a[p]] = [a[p], a[i]];
        p++;
      }
    }
    [a[p], a[hi]] = [a[hi], a[p]];

    if (p === k) return a[p];
    if (k < p) hi = p - 1;
    else lo = p + 1;
  }
}
```

Function mutate array. API production nên document điều đó hoặc copy input.

## Median of medians

Có deterministic selection worst-case `O(n)` bằng cách chọn pivot qua median-of-medians. Nó có proof đẹp nhưng constant factor lớn, nên randomized quickselect thường thực dụng hơn.

Ý nghĩa lý thuyết quan trọng: k-th selection không cần `Omega(n log n)` như sorting; lower information requirement cho phép tuyến tính.

## Top-K với heap

Nếu stream có `n` items và cần `k` largest, giữ min-heap size `k`.

Với mỗi `x`:

```text
heap chưa đủ k -> push
x <= heap.min -> bỏ
x > heap.min -> replace min bằng x
```

Complexity:

\[
O(n\log k)
\]

Memory `O(k)`.

Nếu `k` nhỏ hơn nhiều `n`, đây tốt hơn sort toàn bộ `O(n log n)` cả về memory và work.

## Streaming và bounded memory

Top-K heap không cần giữ toàn bộ data. Đây là distinction quan trọng giữa batch và streaming algorithms. Trong log processing, recommendation candidates hoặc monitoring, bounded-memory property có thể quan trọng hơn một constant-factor speedup.

## Mental Model

> Đừng trả tiền để biết **toàn bộ order** nếu câu hỏi chỉ cần một rank hoặc một boundary nhỏ.

Xem: [Heap](../02_trees/03_heaps.md), [Sorting](./01_sorting.md).
