# Workflow giải bài DSA và thiết kế thuật toán
**Problem-Solving Workflow / 문제 해결 흐름**

Mục tiêu của DSA là biết bắt đầu reasoning từ đâu khi gặp problem mới.

## Từ story sang model

Trước khi code, xác định input là sequence, set, mapping, tree, graph, intervals hay state-transition system. Nếu model sai, thuật toán đúng cũng giải sai bài toán.

## Constraints là complexity budget

`n <= 20` có thể cho phép `2^n`. `n = 10^5` thường loại `O(n²)`. `10^5` queries gợi ý preprocessing hoặc index/range structure.

## Tìm brute force

Brute force làm lộ search space. Từ `O(n²)`, hỏi có sorted invariant cho two pointers không, có hash table để nhớ previous values không, có prefix aggregate để tránh tính lại không.

Từ `O(2^n)`, hỏi các branches có dẫn tới cùng state không; nếu có, memoization/DP có thể nén repeated work.

## Viết invariant trước code phức tạp

Sliding window cần biết window đang luôn thỏa điều kiện gì. Binary search cần biết answer còn nằm trong interval nào. Greedy cần proof rằng choice là safe. DSU cần parent forest invariant.

## Edge cases phải sinh từ model

Empty input, one element, duplicates, all equal, already/reverse sorted, disconnected graph, cycles, negative edges, integer overflow, recursion depth và mutation aliasing không phải một checklist vô nghĩa; chúng là boundary nơi assumptions dễ vỡ.

## Language-specific review

C: ownership, bounds, allocation failure, pointer lifetime, integer overflow.

Java: boxing, comparator overflow, recursion depth, correct collection type, equality/hashCode contract.

JavaScript: number precision, default `.sort()`, `Array.shift()` cost, recursion limit, `Map` vs object, UTF-16 string semantics.

## Mental Model

> Giải DSA là quá trình nén search space bằng representation, invariant và reuse. Nếu một solution nhanh hơn brute force, hãy chỉ ra chính xác candidates hoặc repeated work nào nó đã loại bỏ.
