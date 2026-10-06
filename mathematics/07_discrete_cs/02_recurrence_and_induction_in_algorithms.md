# Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Recursion cần một well-founded descent** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Vì sao recursive lời gọi (call / 호출) phải tiến về cơ sở (base / 기반) trường hợp (case / 사례)?** để đem mô hình vào tình huống cụ thể. Mạch này nối recurrence với induction và algorithms, để chứng minh đúng không chỉ cho một input mà cho cả họ bài toán.

Đệ quy (recursion / 재귀), quan hệ truy hồi (recurrence / 점화식) và quy nạp (induction / 수학적 귀납법) thường được học ở ba nơi khác nhau: programming, discrete mathematics và proof. Nhưng chúng là ba mặt của cùng một idea:

> một đối tượng (object / 객체)/bài toán (problem / 문제) lớn được xây từ versions nhỏ hơn của chính nó.

Recursion mô tả **computation**. Recurrence mô tả **quantity thay đổi theo kích thước (size / 크기)/trạng thái (state / 상태)**. Induction mô tả **proof rằng cấu trúc (structure / 구조) đó đúng ở mọi kích thước (size / 크기)**.

Khi nhìn chúng cùng nhau, divide-and-conquer, động (dynamic / 동적) programming, cây (tree / 트리) algorithms và vòng lặp (loop / 루프) invariants trở nên thống nhất hơn rất nhiều.

## 1. Recursion cần một well-founded descent

Một recursive definition phải có:

```text
base case
+
rule giảm problem về case nhỏ hơn
```

Ví dụ factorial:

```math
n!=n(n-1)!,
```

với

```math
0!=1.
```

Mã (code / 코드) tương ứng:

```text
factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

Cơ sở (base / 기반) trường hợp (case / 사례) không chỉ để tránh ngăn xếp (stack / 스택) overflow. Nó neo cả definition và tính đúng đắn (correctness / 정확성) proof vào một trạng thái (state / 상태) đã biết.

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **1. Recursion cần một well-founded descent** nêu quy tắc; **2. Vì sao recursive lời gọi (call / 호출) phải tiến về cơ sở (base / 기반) trường hợp (case / 사례)?** thử quy tắc trong tình huống, rồi **3. Mathematical induction mirror recursive construction** mở rộng hệ quả.

## 2. Vì sao recursive lời gọi (call / 호출) phải tiến về cơ sở (base / 기반) trường hợp (case / 사례)?

Ta cần một measure `m(state)` giảm theo một well-founded thứ tự (order / 순서).

Với factorial:

```math
m(n)=n.
```

Mỗi lời gọi (call / 호출) giảm `n` một đơn vị và natural numbers không thể giảm vô hạn dưới 0.

Đây là termination proof.

Nếu recursive hàm (function / 함수) gọi chính nó với cùng hoặc larger measure, termination không được guarantee.

> **Nối mạch:** Ở chặng này của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **2. Vì sao recursive lời gọi (call / 호출) phải tiến về cơ sở (base / 기반) trường hợp (case / 사례)?** nêu quy tắc; **3. Mathematical induction mirror recursive construction** thử quy tắc trong tình huống, rồi **4. Strong induction cho divide-and-conquer** mở rộng hệ quả.

## 3. Mathematical induction mirror recursive construction

Muốn prove thuộc tính (property / 속성) `P(n)` cho mọi natural number:

### Cơ sở (base / 기반) trường hợp (case / 사례)

Prove `P(0)` hoặc starting trường hợp (case / 사례).

### Inductive step

Assume

```math
P(n)
```

và prove

```math
P(n+1).
```

Lô-gic (logic / 논리) là: nếu thuộc tính (property / 속성) được truyền từ mỗi trạng thái (state / 상태) sang next trạng thái (state / 상태), và chuỗi (chain / 사슬) bắt đầu đúng, thì toàn chuỗi (chain / 사슬) đúng.

Induction vì vậy không phải một proof trick kỳ lạ; nó là proof form matching recursive cấu trúc (structure / 구조) của natural numbers.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **4. Strong induction cho divide-and-conquer** nối từ **3. Mathematical induction mirror recursive construction** sang **5. Recurrence mô tả chi phí (cost / 비용), count hoặc trạng thái (state / 상태) quan hệ (relation / 관계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Strong induction cho divide-and-conquer

Strong induction assume thuộc tính (property / 속성) đúng cho **mọi** smaller sizes:

```math
P(0),P(1),\ldots,P(n-1)
```

để prove `P(n)`.

Điều này natural khi thuật toán (algorithm / 알고리즘) chia đầu vào (input / 입력) kích thước (size / 크기) `n` thành subproblems như `n/2`, `n/3`, hoặc varying sizes.

Ví dụ merge sort tính đúng đắn (correctness / 정확성) có thể assume recursive calls sort correctly mọi smaller arrays, rồi prove merge step tạo sorted kết quả (result / 결과) kích thước (size / 크기) `n`.

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **5. Recurrence mô tả chi phí (cost / 비용), count hoặc trạng thái (state / 상태) quan hệ (relation / 관계)** nối từ **4. Strong induction cho divide-and-conquer** sang **6. Solve recurrence bằng unrolling**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Recurrence mô tả chi phí (cost / 비용), count hoặc trạng thái (state / 상태) quan hệ (relation / 관계)

Nếu thời gian chạy (runtime / 런타임) của thuật toán (algorithm / 알고리즘) kích thước (size / 크기) `n` phụ thuộc thời gian chạy (runtime / 런타임) smaller inputs, ta viết recurrence.

Tìm kiếm nhị phân (binary search / 이진 탐색):

```math
T(n)=T(n/2)+c.
```

Merge sort:

```math
T(n)=2T(n/2)+cn.
```

Fibonacci:

```math
F_n=F_{n-1}+F_{n-2}.
```

Cùng notation “hiện tại (current / 현재) quantity từ smaller quantities”, nhưng ngữ nghĩa (semantics / 의미론) khác nhau: thời gian chạy (runtime / 런타임), chuỗi (sequence / 시퀀스) giá trị (value / 값) hoặc number of configurations.

> **Nối mạch:** Ở chặng này của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **6. Solve recurrence bằng unrolling** nối từ **5. Recurrence mô tả chi phí (cost / 비용), count hoặc trạng thái (state / 상태) quan hệ (relation / 관계)** sang **7. Recursion cây (tree / 트리) cho merge sort**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Solve recurrence bằng unrolling

Tìm kiếm nhị phân (binary search / 이진 탐색):

```math
T(n)=T(n/2)+c.
```

Substitute repeatedly:

```math
T(n)=T(n/4)+2c
```

```math
=T(n/8)+3c
```

sau `k` levels:

```math
T(n)=T(n/2^k)+kc.
```

Cơ sở (base / 기반) khi

```math
n/2^k\approx1,
```

nên

```math
k\approx\log_2n.
```

Do đó

```math
T(n)=O(\log n).
```

Logarithm xuất hiện từ recursion độ sâu (depth / 깊이) của repeated halving.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **7. Recursion cây (tree / 트리) cho merge sort** nối từ **6. Solve recurrence bằng unrolling** sang **8. Master Theorem là compressed mẫu (pattern / 패턴) recognition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Recursion cây (tree / 트리) cho merge sort

Merge sort:

```math
T(n)=2T(n/2)+cn.
```

Mức (level / 수준) 0 công việc (work / 작업) outside recursion: `cn`.

Mức (level / 수준) 1 có 2 subproblems kích thước (size / 크기) `n/2`; total merge công việc (work / 작업):

```math
2\cdot c(n/2)=cn.
```

Mức (level / 수준) 2:

```math
4\cdot c(n/4)=cn.
```

Có roughly `\log_2n` levels, mỗi mức (level / 수준) `O(n)`, nên

```math
T(n)=O(n\log n).
```

Recursion cây (tree / 트리) là geometric visualization của recurrence.

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **8. Master Theorem là compressed mẫu (pattern / 패턴) recognition** nối từ **7. Recursion cây (tree / 트리) cho merge sort** sang **9. Substitution phương thức (method / 메서드): guess rồi prove bằng induction**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Master Theorem là compressed mẫu (pattern / 패턴) recognition

Recurrences dạng

```math
T(n)=aT(n/b)+f(n)
```

so sánh:

- number subproblems `a`;
- shrink factor `b`;
- combine công việc (work / 작업) `f(n)`.

Quantity

```math
n^{\log_b a}
```

mô tả total leaf-growth quy mô (scale / 규모) của recursion cây (tree / 트리).

Master Theorem chỉ đóng gói comparison giữa recursive expansion và per-level combine công việc (work / 작업). Học recursion cây (tree / 트리) trước giúp theorem không trở thành bảng cases phải thuộc.

> **Nối mạch:** Ở chặng này của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **9. Substitution phương thức (method / 메서드): guess rồi prove bằng induction** nối từ **8. Master Theorem là compressed mẫu (pattern / 패턴) recognition** sang **10. Naive Fibonacci và overlapping subproblems**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Substitution phương thức (method / 메서드): guess rồi prove bằng induction

Giả sử recurrence

```math
T(n)=2T(n/2)+n
```

và ta đoán

```math
T(n)=O(n\log n).
```

Ta có thể assume inductively

```math
T(n/2)\le c\frac n2\log(n/2)
```

rồi substitute để bound `T(n)`.

Đây là liên kết (connection / 연결) trực tiếp recurrence ↔ induction: solve asymptotic recurrence bằng proof trên đầu vào (input / 입력) kích thước (size / 크기).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **10. Naive Fibonacci và overlapping subproblems** nối từ **9. Substitution phương thức (method / 메서드): guess rồi prove bằng induction** sang **11. động (dynamic / 동적) programming = recurrence + trạng thái (state / 상태) thiết kế (design / 설계) + reuse**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Naive Fibonacci và overlapping subproblems

Recurrence mathematical:

```math
F_n=F_{n-1}+F_{n-2}.
```

Naive recursive hiện thực (implementation / 구현) recomputes same states many times.

Lời gọi (call / 호출) cây (tree / 트리) của `F_n` chứa repeated `F_{n-2}`, `F_{n-3}`, ...

Thời gian chạy (runtime / 런타임) recurrence roughly:

```math
T(n)=T(n-1)+T(n-2)+O(1),
```

leading to exponential growth.

Memoization changes computation đồ thị (graph / 그래프): mỗi distinct trạng thái (state / 상태) solved once.

Then number states `O(n)`, so thời gian (time / 시간) can become `O(n)`.

Same mathematical recurrence, radically different algorithmic thực thi (execution / 실행).

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **11. động (dynamic / 동적) programming = recurrence + trạng thái (state / 상태) thiết kế (design / 설계) + reuse** nối từ **10. Naive Fibonacci và overlapping subproblems** sang **12. trạng thái (state / 상태) definition quyết định độ phức tạp (complexity / 복잡도)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. động (dynamic / 동적) programming = recurrence + trạng thái (state / 상태) thiết kế (design / 설계) + reuse

Động (dynamic / 동적) programming không chỉ là “recursion có bộ nhớ đệm (cache / 캐시)”. Nó cần:

1. define trạng thái (state / 상태);
2. derive recurrence/chuyển tiếp (transition / 전이);
3. identify cơ sở (base / 기반) states;
4. choose evaluation thứ tự (order / 순서) or memoization;
5. sometimes reconstruct choices.

For shortest đường dẫn (path / 경로) in DAG:

```math
D(v)=\min_{u\to v}[D(u)+w(u,v)].
```

Recurrence expresses Bellman optimality: best solution to trạng thái (state / 상태) uses best solutions to predecessor states.

> **Nối mạch:** Ở chặng này của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **12. trạng thái (state / 상태) definition quyết định độ phức tạp (complexity / 복잡도)** nối từ **11. động (dynamic / 동적) programming = recurrence + trạng thái (state / 상태) thiết kế (design / 설계) + reuse** sang **13. vòng lặp (loop / 루프) invariants là induction trên thời gian (time / 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. trạng thái (state / 상태) definition quyết định độ phức tạp (complexity / 복잡도)

Một DP có thể chậm không phải vì recurrence sai mà vì trạng thái (state / 상태) không gian (space / 공간) quá lớn.

If trạng thái (state / 상태) uses `(i,j,k)`, number states may quy mô (scale / 규모)

```math
O(nmk).
```

If a dimension is redundant and can be removed, độ phức tạp (complexity / 복잡도) drops dramatically.

Mathematics of recurrence và modeling of trạng thái (state / 상태) must be analyzed together.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **13. vòng lặp (loop / 루프) invariants là induction trên thời gian (time / 시간)** nối từ **12. trạng thái (state / 상태) definition quyết định độ phức tạp (complexity / 복잡도)** sang **14. Worked proof: tìm kiếm nhị phân (binary search / 이진 탐색) tính đúng đắn (correctness / 정확성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. vòng lặp (loop / 루프) invariants là induction trên thời gian (time / 시간)

Vòng lặp (loop / 루프):

```text
for k = 0,1,2,...
```

can be proved with bất biến (invariant / 불변식) `I(k)`.

### Initialization

Bất biến (invariant / 불변식) true before first iteration.

### Maintenance

If bất biến (invariant / 불변식) true before iteration, executing body preserves it.

### Termination

Bất biến (invariant / 불변식) + vòng lặp (loop / 루프) exit điều kiện (condition / 조건) imply postcondition.

This is induction on iteration count disguised as program proof.

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **13. vòng lặp (loop / 루프) invariants là induction trên thời gian (time / 시간)** nêu quy tắc; **14. Worked proof: tìm kiếm nhị phân (binary search / 이진 탐색) tính đúng đắn (correctness / 정확성)** thử quy tắc trong tình huống, rồi **15. Structural induction cho recursive dữ liệu (data / 데이터) structures** mở rộng hệ quả.

## 14. Worked proof: tìm kiếm nhị phân (binary search / 이진 탐색) tính đúng đắn (correctness / 정확성)

Bất biến (invariant / 불변식):

> nếu mục tiêu (target / 대상) tồn tại, nó nằm trong hiện tại (current / 현재) interval `[low, high]`.

Initialization: interval starts as entire sorted array.

Maintenance: if `a[mid]<target`, sorted thứ tự (order / 순서) proves positions `≤mid` cannot contain mục tiêu (target / 대상), so setting

```text
low = mid + 1
```

preserves bất biến (invariant / 불변식).

Symmetric trường hợp (case / 사례) for `a[mid]>target`.

Termination: if `low>high`, interval empty. bất biến (invariant / 불변식) implies mục tiêu (target / 대상) does not exist.

Thời gian chạy (runtime / 런타임) `O(log n)` proof và tính đúng đắn (correctness / 정확성) proof are different arguments.

> **Nối mạch:** Ở chặng này của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **14. Worked proof: tìm kiếm nhị phân (binary search / 이진 탐색) tính đúng đắn (correctness / 정확성)** nêu quy tắc; **15. Structural induction cho recursive dữ liệu (data / 데이터) structures** thử quy tắc trong tình huống, rồi **16. Induction trên đồ thị (graph / 그래프) DAG thứ tự (order / 순서)** mở rộng hệ quả.

## 15. Structural induction cho recursive dữ liệu (data / 데이터) structures

Trees are not naturally indexed only by integer kích thước (size / 크기). Structural induction mirrors constructors.

For nhị phân (binary / 이진) cây (tree / 트리):

- cơ sở (base / 기반): empty/leaf cây (tree / 트리);
- inductive step: assume thuộc tính (property / 속성) for left and right subtrees, prove for parent cây (tree / 트리).

Use cases:

- AST evaluation;
- trình biên dịch (compiler / 컴파일러) transformations;
- JSON/XML trees;
- expression simplification;
- recursive kiểu (type / 타입) tính đúng đắn (correctness / 정확성).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **15. Structural induction cho recursive dữ liệu (data / 데이터) structures** đặt vấn đề; **16. Induction trên đồ thị (graph / 그래프) DAG thứ tự (order / 순서)** đối chiếu bằng chứng, rồi **17. Termination via ranking functions** mở rộng hệ quả hoặc giới hạn liên quan.

## 16. Induction trên đồ thị (graph / 그래프) DAG thứ tự (order / 순서)

DAG permits topological thứ tự (order / 순서). Many proofs/algorithms can proceed according to that thứ tự (order / 순서):

```text
all predecessors solved
→ solve current node
```

This is generalized induction over a partial thứ tự (order / 순서) rather than simple integer chuỗi (sequence / 시퀀스).

Động (dynamic / 동적) programming on DAGs follows exactly this cấu trúc (structure / 구조).

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **17. Termination via ranking functions** nối từ **16. Induction trên đồ thị (graph / 그래프) DAG thứ tự (order / 순서)** sang **18. Mutual recursion**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Termination via ranking functions

To prove vòng lặp (loop / 루프)/recursion terminates, define ranking hàm (function / 함수) into a well-founded set.

Euclidean thuật toán (algorithm / 알고리즘):

```math
\gcd(a,b)=\gcd(b,a\bmod b).
```

For `b>0`:

```math
0\le a\bmod b<b.
```

Second argument strictly decreases among nonnegative integers, so thuật toán (algorithm / 알고리즘) must reach zero.

Termination is a mathematical thuộc tính (property / 속성), not just “seems to get smaller”.

> **Nối mạch:** Ở chặng này của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **18. Mutual recursion** nối từ **17. Termination via ranking functions** sang **19. Tail recursion và ngăn xếp (stack / 스택) ngữ nghĩa (semantics / 의미론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Mutual recursion

Functions can recurse through each other:

```text
A → B → A
```

Termination/tính đúng đắn (correctness / 정확성) may need a dùng chung (shared / 공유) measure across combined states.

Parsers for grammar nonterminals often use mutual recursion.

This illustrates why lời gọi (call / 호출) đồ thị (graph / 그래프) cấu trúc (structure / 구조) matters beyond single-function view.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **19. Tail recursion và ngăn xếp (stack / 스택) ngữ nghĩa (semantics / 의미론)** nối từ **18. Mutual recursion** sang **20. Recurrence quan hệ (relation / 관계) as tuyến tính (linear / 선형) dynamical hệ thống (system / 시스템)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Tail recursion và ngăn xếp (stack / 스택) ngữ nghĩa (semantics / 의미론)

Tail-recursive lời gọi (call / 호출) is final thao tác (operation / 연산) of hàm (function / 함수). Languages/runtimes with tail-call tối ưu hóa (optimization / 최적화) can reuse ngăn xếp (stack / 스택) frame.

But not every thời gian chạy (runtime / 런타임) guarantees tối ưu hóa (optimization / 최적화).

Therefore algorithmic không gian (space / 공간) phân tích (analysis / 분석) should consider actual ngôn ngữ (language / 언어) hiện thực (implementation / 구현), not mathematical recurrence alone.

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **20. Recurrence quan hệ (relation / 관계) as tuyến tính (linear / 선형) dynamical hệ thống (system / 시스템)** nối từ **19. Tail recursion và ngăn xếp (stack / 스택) ngữ nghĩa (semantics / 의미론)** sang **21. Generating-function viewpoint**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Recurrence quan hệ (relation / 관계) as tuyến tính (linear / 선형) dynamical hệ thống (system / 시스템)

Some recurrences can be written ma trận (matrix / 행렬) form.

Fibonacci:

```math
\begin{bmatrix}
F_{n+1}\\F_n
\end{bmatrix}
=
\begin{bmatrix}
1&1\\1&0
\end{bmatrix}
\begin{bmatrix}
F_n\\F_{n-1}
\end{bmatrix}.
```

Then

```math
v_n=A^nv_0.
```

Eigenvalues explain growth tỷ lệ (rate / 비율); fast exponentiation computes `A^n` in `O(log n)` ma trận (matrix / 행렬) multiplications.

This connects discrete recurrence to tuyến tính (linear / 선형) algebra and động (dynamic / 동적) các hệ thống (systems / 시스템들).

> **Nối mạch:** Ở chặng này của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **21. Generating-function viewpoint** nối từ **20. Recurrence quan hệ (relation / 관계) as tuyến tính (linear / 선형) dynamical hệ thống (system / 시스템)** sang **22. Physics liên kết (connection / 연결): discrete thời gian (time / 시간) evolution**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Generating-function viewpoint

Chuỗi (sequence / 시퀀스) recurrence can be encoded into power series

```math
G(x)=\sum_{n\ge0}a_nx^n.
```

Recurrence relations become algebraic equations on `G(x)`.

This transforms a discrete recursive quan hệ (relation / 관계) into hàm (function / 함수) algebra — another example of changing biểu diễn (representation / 표현) to solve cấu trúc (structure / 구조).

Full generating-function lý thuyết (theory / 이론) is optional in hiện tại (current / 현재) phạm vi (scope / 범위), but the liên kết (connection / 연결) explains why recurrence phân tích (analysis / 분석) touches algebra and complex phân tích (analysis / 분석).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, sau nội dung của **21. Generating-function viewpoint**, **22. Physics liên kết (connection / 연결): discrete thời gian (time / 시간) evolution** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **23. Finance liên kết (connection / 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## 22. Physics liên kết (connection / 연결): discrete thời gian (time / 시간) evolution

A recurrence like

```math
x_{k+1}=Ax_k
```

is a discrete dynamical hệ thống (system / 시스템).

Stability depends on eigenvalues of `A`:

```math
|\lambda|<1
```

for modes that decay.

Numerical ODE solvers also create recurrences from continuous equations. Thus recursion/recurrence is not only CS; it is a ngôn ngữ (language / 언어) for discrete dynamics.

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **23. Finance liên kết (connection / 연결)** nối từ **22. Physics liên kết (connection / 연결): discrete thời gian (time / 시간) evolution** sang **24. dùng chung (common / 공통) thất bại (failure / 실패) modes**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Finance liên kết (connection / 연결)

Compound growth:

```math
V_{t+1}=(1+r_t)V_t+C_t
```

is recurrence.

Loan amortization, portfolio wealth updates and động (dynamic / 동적) programming for investment decisions all use trạng thái (state / 상태) transitions over thời gian (time / 시간).

Bellman equations generalize recurrence to optimal sequential decision-making.

> **Nối mạch:** Ở chặng này của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **24. dùng chung (common / 공통) thất bại (failure / 실패) modes** nối từ **23. Finance liên kết (connection / 연결)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. dùng chung (common / 공통) thất bại (failure / 실패) modes

### Missing cơ sở (base / 기반) trường hợp (case / 사례)

Definition/computation has no anchor.

### Cơ sở (base / 기반) exists but measure does not decrease

Still may not terminate.

### Correct recurrence, inefficient evaluation

Naive Fibonacci demonstrates exponential recomputation.

### Correct asymptotic recurrence, wrong tính đúng đắn (correctness / 정확성) lập luận (reasoning / 추론)

Thời gian chạy (runtime / 런타임) phân tích (analysis / 분석) does not prove returned answer is correct.

### Trạng thái (state / 상태) too large

Động (dynamic / 동적) programming can still be infeasible due to curse of dimensionality.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **24. dùng chung (common / 공통) thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Recursion decomposes computation, recurrence records the phụ thuộc (dependency / 의존성) between sizes/states, and induction proves that phụ thuộc (dependency / 의존성) is valid everywhere. động (dynamic / 동적) programming adds one more idea: if many paths reach the same trạng thái (state / 상태), solve that trạng thái (state / 상태) once and reuse it.

> **Nối mạch:** Trong **Recurrence, induction và recursion: một cấu trúc (structure / 구조) chung của algorithmic lập luận (reasoning / 추론)**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**Recursive mã (code / 코드) is inherently slow.** No; repeated công việc (work / 작업) and ngăn xếp (stack / 스택)/hành vi thời gian chạy (runtime behavior / 런타임 동작) determine chi phí (cost / 비용).

**Memoization changes the mathematical recurrence.** Usually no; it changes evaluation chiến lược (strategy / 전략) and computation đồ thị (graph / 그래프).

**cơ sở (base / 기반) trường hợp (case / 사례) is only a programming detail.** It is also the logical anchor of definition/proof.

**Finding a recurrence automatically gives độ phức tạp (complexity / 복잡도).** No; recurrence still needs solution/bounds and actual chi phí (cost / 비용) mô hình (model / 모델).

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
