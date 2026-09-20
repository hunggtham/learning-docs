# Testing và Benchmarking DSA trên C, Java, JavaScript
**자료구조 테스트와 벤치마킹**

Một implementation DSA cần được kiểm tra ở ba lớp: examples, invariants và comparative/property tests.

## Test invariant thay vì chỉ output

Với heap, sau random sequences push/pop, kiểm tra mỗi parent thỏa heap property.

Với BST, inorder traversal phải sorted và size metadata phải khớp node count.

Với DSU, `find(x)` phải ổn định theo component partition.

Invariant tests phát hiện corruption sớm hơn test một query cuối.

## Differential testing

Tạo random operations và so sánh custom structure với trusted reference implementation.

Ví dụ custom hash set C có thể được so semantic output với một simple sorted-array model trên datasets nhỏ. Custom JS heap có thể so `pop` sequence với `array.sort` reference.

Reference chậm nhưng đơn giản thường tốt cho test.

## Property-based thinking

Sort output phải:

```text
nondecreasing
same multiset as input
```

Shortest path result phải thỏa triangle-style relaxation condition sau algorithm và parent path cost phải bằng reported distance.

Không cần framework property testing chuyên dụng để dùng mental model này.

## Benchmark pitfalls

Không benchmark chỉ một input shape. Sorting cần random, sorted, reverse, duplicate-heavy. Hashing cần realistic keys. Graph algorithms cần sparse/dense, path-like và clustered graphs tùy domain.

Java cần warm-up JIT; JavaScript engine cũng có tiering/JIT effects. C compiler flags ảnh hưởng lớn. So sánh cross-language microbenchmark mà không kiểm soát environment thường không nói nhiều về algorithm.

## Scale test

Một technique tốt là đo runtime theo nhiều `n` tăng dần và nhìn growth trend. Nếu runtime nhân khoảng 4 khi `n` nhân 2, có tín hiệu `n^2`; nếu gần nhân 2, có thể tuyến tính trong regime đo được.

Benchmark không thay thế complexity proof, nhưng nó có thể phát hiện implementation overhead hoặc assumption sai.

## Mental Model

> Proof nói algorithm nên đúng và tăng trưởng thế nào. Tests tìm implementation bugs. Benchmark đo cost thật trên workload/runtime. Ba công cụ trả lời ba câu hỏi khác nhau.
