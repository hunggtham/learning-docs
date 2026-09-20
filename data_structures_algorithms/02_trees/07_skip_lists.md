# Skip List  
**스킵 리스트**

Skip list cung cấp ordered-set/map operations expected `O(log n)` nhưng dùng linked lists nhiều tầng và randomness thay vì rotations.

## Từ linked list tới express lanes

Một sorted linked list search `O(n)` vì chỉ đi từng node. Nếu thêm một tầng chứa khoảng một nửa nodes, ta có thể nhảy xa hơn; tầng trên nữa chứa khoảng một phần tư, tiếp tục như vậy.

```text
L2: 1 -------- 9 -------- 20
L1: 1 --- 4 -- 9 --- 15 - 20
L0: 1 2 3 4 5  9 10 15 18 20
```

Search đi right khi next <= target; nếu không, đi xuống level. Đây giống binary-search spirit nhưng trên linked representation.

## Random level

Khi insert, node được promote lên tầng cao hơn với probability, thường gần 1/2 mỗi level. Expected số nodes giảm exponentially theo level, tạo expected logarithmic height/search.

Không có deterministic balance rotations; randomness giữ distribution tốt trong expectation.

## Insert/delete

Search lưu `update[level]`: node trước insertion position ở mỗi tầng. Tạo node với random height rồi splice links ở các tầng nó tham gia.

Delete dùng cùng predecessor path và unlink node ở mọi level.

## So với balanced BST

Skip list implementation thường đơn giản hơn rotations và dễ hỗ trợ certain concurrent designs. Balanced tree cho deterministic worst-case logarithmic guarantees; skip list cho expected guarantees và pointer-rich representation.

Redis sorted sets historically use skip-list-like structure kết hợp hash map trong một số implementations/versions, minh họa composition theo workload.

## Mental Model

> Skip list tạo **nhiều độ phân giải của cùng sorted sequence**. Tầng cao bỏ qua nhiều nodes; tầng thấp hoàn thiện search chính xác.
