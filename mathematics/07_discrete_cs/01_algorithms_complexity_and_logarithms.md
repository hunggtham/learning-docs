# Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Trước Big-O phải chọn chi phí (cost / 비용) mô hình (model / 모델)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Big-O là asymptotic upper bound** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối algorithms với complexity và logarithms, để chọn phương pháp theo tốc độ tăng chứ không chỉ theo ví dụ nhỏ.

Phân tích độ phức tạp (algorithmic complexity / 알고리즘 복잡도) không nhằm dự đoán chính xác chương trình chạy bao nhiêu milliseconds. Nó trả lời câu hỏi cấu trúc hơn:

> Khi đầu vào (input / 입력) kích thước (size / 크기) tăng, lượng tài nguyên (resource / 자원) cần thiết tăng theo **shape** nào?

Đây là câu hỏi về scalability. Một hiện thực (implementation / 구현) rất nhanh ở `n=100` có thể trở nên vô dụng ở `n=10^9` nếu growth tỷ lệ (rate / 비율) xấu. Ngược lại, thuật toán (algorithm / 알고리즘) có constant overhead lớn nhưng asymptotic tốt có thể thắng ở quy mô (scale / 규모) lớn.

## Trước Big-O phải chọn chi phí (cost / 비용) mô hình (model / 모델)

Độ phức tạp (complexity / 복잡도) luôn phụ thuộc điều ta đang count.

Ta có thể count:

- arithmetic operations;
- comparisons;
- bộ nhớ (memory / 메모리) usage;
- disk I/O;
- mạng (network / 네트워크) round trips;
- bộ nhớ đệm (cache / 캐시) misses;
- parallel độ sâu (depth / 깊이).

Statement `O(n)` không có nghĩa universal “nhanh”. Một scan `O(n)` trên RAM và `O(n)` remote API calls có độ trễ (latency / 지연 시간) hoàn toàn khác.

Vì vậy phân tích (analysis / 분석) bắt đầu bằng input-size definition và chi phí (cost / 비용) mô hình (model / 모델).

> **Nối mạch:** Trong **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Big-O là asymptotic upper bound** nối từ **Trước Big-O phải chọn chi phí (cost / 비용) mô hình (model / 모델)** sang **Vì sao constants và lower-order terms thường bị bỏ?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Big-O là asymptotic upper bound

`f(n)=O(g(n))` nếu tồn tại constants `c>0` và `n_0` sao cho

```math
0\le f(n)\le c g(n)
```

với mọi `n\ge n_0`.

Big-O nói rằng sau một quy mô (scale / 규모) đủ lớn, `f` không grow nhanh hơn `g` hơn constant factor.

Tight bound dùng `\Theta`:

```math
f(n)=\Theta(g(n))
```

nếu `f` vừa upper-bounded vừa lower-bounded bởi constant multiples của `g` asymptotically.

`\Omega` biểu diễn lower asymptotic bound.

> **Nối mạch:** Ở chặng này của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Vì sao constants và lower-order terms thường bị bỏ?** nối từ **Big-O là asymptotic upper bound** sang **O(1) không nghĩa “một instruction”**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao constants và lower-order terms thường bị bỏ?

Giả sử

```math
T(n)=3n^2+10n+500.
```

Chia cho `n^2`:

```math
\frac{T(n)}{n^2}
=
3+\frac{10}{n}+\frac{500}{n^2}.
```

Khi `n\to\infty`, lower-order terms vanish và ratio tiến về 3. Growth cấu trúc (structure / 구조) dominant là quadratic:

```math
T(n)=\Theta(n^2).
```

Nhưng constants vẫn matter trong kỹ thuật (engineering / 엔지니어링). phân tích độ phức tạp (complexity analysis / 복잡도 분석) và benchmarking trả lời hai câu hỏi khác nhau:

```text
complexity: scaling shape là gì?
benchmark: implementation này nhanh bao nhiêu trên workload/hardware cụ thể?
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **O(1) không nghĩa “một instruction”** nối từ **Vì sao constants và lower-order terms thường bị bỏ?** sang **Tuyến tính (linear / 선형) và quadratic growth**, vì cơ chế trước tạo đầu vào cho bước sau.

## `O(1)` không nghĩa “một instruction”

Constant độ phức tạp (complexity / 복잡도) nghĩa chi phí (cost / 비용) không grow với chosen đầu vào (input / 입력) kích thước (size / 크기) `n`.

Hash-table lookup average-case có thể được gọi expected `O(1)` under các giả định (assumptions / 가정들), nhưng vẫn có hashing, bộ nhớ (memory / 메모리) truy cập (access / 접근) và collision handling.

Cơ sở dữ liệu (database / 데이터베이스) indexed lookup có thể look constant ở ứng dụng (application / 애플리케이션) lớp trừu tượng (abstraction / 추상화) nhưng lưu trữ (storage / 저장소) engine thực tế dùng cây (tree / 트리)/page I/O. độ phức tạp (complexity / 복잡도) label chỉ meaningful khi mô hình (model / 모델) rõ.

> **Nối mạch:** Trong **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Tuyến tính (linear / 선형) và quadratic growth** nối từ **O(1) không nghĩa “một instruction”** sang **Logarithm xuất hiện khi progress là multiplicative**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tuyến tính (linear / 선형) và quadratic growth

Tuyến tính (linear / 선형) scan:

```math
T(n)=an+b
```

Quy mô (scale / 규모) proportionally với `n`.

All-pairs comparison thường:

```math
\binom n2
=
\frac{n(n-1)}2
=
\Theta(n^2).
```

Nếu `n` tăng 10×, tuyến tính (linear / 선형) công việc (work / 작업) tăng khoảng 10×, quadratic tăng khoảng 100×.

Đây là practical meaning của growth lớp (class / 클래스).

> **Nối mạch:** Ở chặng này của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Logarithm xuất hiện khi progress là multiplicative** nối từ **Tuyến tính (linear / 선형) và quadratic growth** sang **Worked example — tìm kiếm nhị phân (binary search / 이진 탐색)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Logarithm xuất hiện khi progress là multiplicative

Nếu mỗi step giảm bài toán (problem / 문제) kích thước (size / 크기) bởi factor `b>1`:

```math
n,
\frac nb,
\frac n{b^2},
\ldots
```

Sau `k` steps muốn còn khoảng 1:

```math
\frac n{b^k}\approx1.
```

Nên

```math
b^k\approx n,
```

và

```math
k\approx\log_b n.
```

Vì vậy logarithmic độ phức tạp (complexity / 복잡도) không đến từ việc mã (code / 코드) gọi hàm `log`. Nó xuất hiện từ repeated multiplicative shrinkage.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Logarithm xuất hiện khi progress là multiplicative** nêu quy tắc; **Worked example — tìm kiếm nhị phân (binary search / 이진 탐색)** thử quy tắc trong tình huống, rồi **Balanced trees và logarithmic height** mở rộng hệ quả.

## Worked example — tìm kiếm nhị phân (binary search / 이진 탐색)

Sorted array kích thước (size / 크기) `n`. Mỗi comparison loại khoảng half candidates.

Recurrence:

```math
T(n)=T(n/2)+O(1).
```

Unroll:

```math
T(n)=T(n/2^k)+kO(1).
```

Stop khi

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

Log cơ sở (base / 기반) không matter trong Big-O vì

```math
\log_a n
=
\frac{\log_b n}{\log_b a},
```

chỉ khác constant factor.

> **Nối mạch:** Trong **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Worked example — tìm kiếm nhị phân (binary search / 이진 탐색)** nêu quy tắc; **Balanced trees và logarithmic height** thử quy tắc trong tình huống, rồi **Divide and conquer: vì sao n log n xuất hiện?** mở rộng hệ quả.

## Balanced trees và logarithmic height

Balanced nhị phân (binary / 이진) cây (tree / 트리) với branching factor roughly 2 có number nodes tăng exponential theo độ sâu (depth / 깊이):

```math
1+2+4+\cdots+2^h\approx2^{h+1}.
```

Do đó storing `n` nodes cần height

```math
h=O(\log n).
```

Tìm kiếm (search / 검색)/cập nhật (update / 업데이트) độ phức tạp (complexity / 복잡도) xuất hiện từ same multiplicative hình học (geometry / 기하학) như tìm kiếm nhị phân (binary search / 이진 탐색).

> **Nối mạch:** Ở chặng này của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Divide and conquer: vì sao n log n xuất hiện?** nối từ **Balanced trees và logarithmic height** sang **Master theorem là mẫu (pattern / 패턴) recognition, không phải spell**, vì cơ chế trước tạo đầu vào cho bước sau.

## Divide and conquer: vì sao `n log n` xuất hiện?

Merge sort recurrence:

```math
T(n)=2T(n/2)+O(n).
```

Recursion cây (tree / 트리) có `\log_2n` levels. Ở mỗi mức (level / 수준), total merge công việc (work / 작업) across subproblems là `O(n)`.

Do đó

```math
T(n)=O(n\log n).
```

Meaning: ta trả tuyến tính (linear / 선형) công việc (work / 작업) ở mỗi logarithmic mức (level / 수준) of decomposition.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Master theorem là mẫu (pattern / 패턴) recognition, không phải spell** nối từ **Divide and conquer: vì sao n log n xuất hiện?** sang **Exponential explosion: khi micro-optimization không cứu được mô hình (model / 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Master theorem là mẫu (pattern / 패턴) recognition, không phải spell

Recurrence dạng

```math
T(n)=aT(n/b)+f(n)
```

so sánh công việc (work / 작업) trong recursive subproblems với nonrecursive công việc (work / 작업) `f(n)`.

Master theorem useful khi cấu trúc (structure / 구조) match, nhưng không thay thế việc hiểu recursion cây (tree / 트리). Nếu recurrence không đúng form hoặc subproblem sizes irregular, theorem có thể không áp dụng.

> **Nối mạch:** Trong **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Exponential explosion: khi micro-optimization không cứu được mô hình (model / 모델)** nối từ **Master theorem là mẫu (pattern / 패턴) recognition, không phải spell** sang **Worst-case, average-case và expected độ phức tạp (complexity / 복잡도)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Exponential explosion: khi micro-optimization không cứu được mô hình (model / 모델)

Enumerate all subsets:

```math
2^n.
```

Enumerate all permutations:

```math
n!.
```

Ví dụ

```math
2^{100}\approx1.27\times10^{30}.
```

Dù xử lý one billion states mỗi second, exhaustive enumeration vẫn infeasible.

Khi growth lớp (class / 클래스) exponential/factorial, solution thường cần **algorithmic insight**: động (dynamic / 동적) programming, pruning, approximation, relaxations hoặc exploit bài toán (problem / 문제) cấu trúc (structure / 구조).

> **Nối mạch:** Ở chặng này của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Exponential explosion: khi micro-optimization không cứu được mô hình (model / 모델)** nêu quy tắc; **Worst-case, average-case và expected độ phức tạp (complexity / 복잡도)** thử quy tắc trong tình huống, rồi **Amortized phân tích (analysis / 분석): expensive thao tác (operation / 연산) nhưng cheap chuỗi (sequence / 시퀀스)** mở rộng hệ quả.

## Worst-case, average-case và expected độ phức tạp (complexity / 복잡도)

Độ phức tạp (complexity / 복잡도) statement phải nói trường hợp (case / 사례) nào.

Quicksort có average/expected `O(n\log n)` under dùng chung (common / 공통) pivot các giả định (assumptions / 가정들) nhưng worst-case `O(n^2)`.

Băm (hash / 해시) tables often expected `O(1)` lookup, nhưng adversarial collisions có thể degrade.

Worst-case useful cho guarantees; expected/average useful khi probabilistic tải công việc (workload / 워크로드) các giả định (assumptions / 가정들) justified.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Worst-case, average-case và expected độ phức tạp (complexity / 복잡도)** nêu quy tắc; **Amortized phân tích (analysis / 분석): expensive thao tác (operation / 연산) nhưng cheap chuỗi (sequence / 시퀀스)** thử quy tắc trong tình huống, rồi **Không gian (space / 공간) độ phức tạp (complexity / 복잡도) và time-space sự đánh đổi (trade-off / 트레이드오프)** mở rộng hệ quả.

## Amortized phân tích (analysis / 분석): expensive thao tác (operation / 연산) nhưng cheap chuỗi (sequence / 시퀀스)

Động (dynamic / 동적) array append thường `O(1)`, nhưng occasionally resize costs `O(n)`.

Nếu sức chứa (capacity / 용량) doubles, total copied elements over many appends is geometric series:

```math
1+2+4+\cdots+n<2n.
```

Across `n` appends, total resize công việc (work / 작업) `O(n)`, nên amortized chi phí (cost / 비용) per append là `O(1)`.

Amortized không phải probabilistic average; nó là deterministic accounting over thao tác (operation / 연산) chuỗi (sequence / 시퀀스).

> **Nối mạch:** Trong **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Amortized phân tích (analysis / 분석): expensive thao tác (operation / 연산) nhưng cheap chuỗi (sequence / 시퀀스)** đặt đầu vào cho **Không gian (space / 공간) độ phức tạp (complexity / 복잡도) và time-space sự đánh đổi (trade-off / 트레이드오프)**, rồi **Lower bounds: có những giới hạn không thể vượt bằng clever coding** mở rộng hệ quả hoặc giới hạn liên quan.

## Không gian (space / 공간) độ phức tạp (complexity / 복잡도) và time-space sự đánh đổi (trade-off / 트레이드오프)

Memoization lưu previous results để tránh recomputation. động (dynamic / 동적) programming thường đổi extra bộ nhớ (memory / 메모리) lấy lower thời gian (time / 시간).

BFS giữ frontier có thể lớn; DFS dùng ngăn xếp (stack / 스택) độ sâu (depth / 깊이) khác. External-memory algorithms optimize I/O vì disk truy cập (access / 접근) dominates arithmetic.

Thuật toán (algorithm / 알고리즘) thiết kế (design / 설계) luôn là multi-resource bài toán (problem / 문제), không chỉ thời gian (time / 시간).

> **Nối mạch:** Ở chặng này của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Không gian (space / 공간) độ phức tạp (complexity / 복잡도) và time-space sự đánh đổi (trade-off / 트레이드오프)** đặt tiêu chí; **Lower bounds: có những giới hạn không thể vượt bằng clever coding** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Độ phức tạp (complexity / 복잡도) classes và tractability intuition** mở rộng hệ quả.

## Lower bounds: có những giới hạn không thể vượt bằng clever coding

Comparison sorting có lower bound

```math
\Omega(n\log n)
```

trong comparison mô hình (model / 모델).

Proof idea: `n!` possible đầu vào (input / 입력) orders cần được distinguish. cây quyết định (decision tree / 의사결정 트리) với nhị phân (binary / 이진) comparisons độ sâu (depth / 깊이) `h` có tối đa `2^h` leaves, nên

```math
2^h\ge n!,
```

suy ra

```math
h\ge\log_2(n!)=\Omega(n\log n).
```

Meaning: merge sort/heapsort are asymptotically optimal among comparison-based sorts. Muốn beat bound phải thay đổi (change / 변경) mô hình (model / 모델)/các giả định (assumptions / 가정들), như counting sort exploiting bounded integer keys.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Lower bounds: có những giới hạn không thể vượt bằng clever coding** đặt tiêu chí; **Độ phức tạp (complexity / 복잡도) classes và tractability intuition** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Động (dynamic / 동적) programming: reduce trạng thái (state / 상태) explosion bằng overlapping cấu trúc (structure / 구조)** mở rộng hệ quả.

## Độ phức tạp (complexity / 복잡도) classes và tractability intuition

Polynomial-time algorithms thường được xem là tractable baseline trong theoretical CS, nhưng degree/constant vẫn matter. `O(n^{100})` không practical; `O(2^n)` có thể practical nếu `n=20`.

Độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) nói asymptotic cấu trúc (structure / 구조), kỹ thuật (engineering / 엔지니어링) feasibility cần actual quy mô (scale / 규모).

> **Nối mạch:** Trong **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Động (dynamic / 동적) programming: reduce trạng thái (state / 상태) explosion bằng overlapping cấu trúc (structure / 구조)** nối từ **Độ phức tạp (complexity / 복잡도) classes và tractability intuition** sang **Đồ thị (graph / 그래프) algorithms: độ phức tạp (complexity / 복잡도) phụ thuộc biểu diễn (representation / 표현)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Động (dynamic / 동적) programming: reduce trạng thái (state / 상태) explosion bằng overlapping cấu trúc (structure / 구조)

Naive Fibonacci recursion:

```math
F(n)=F(n-1)+F(n-2)
```

recomputes same subproblems exponentially nhiều lần.

Memoization stores each `F(k)` once, reducing thời gian (time / 시간) to `O(n)`.

DP không làm mọi exponential bài toán (problem / 문제) polynomial. It works when trạng thái (state / 상태) không gian (space / 공간) nhỏ enough và subproblems overlap with optimal substructure.

> **Nối mạch:** Ở chặng này của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Đồ thị (graph / 그래프) algorithms: độ phức tạp (complexity / 복잡도) phụ thuộc biểu diễn (representation / 표현)** nối từ **Động (dynamic / 동적) programming: reduce trạng thái (state / 상태) explosion bằng overlapping cấu trúc (structure / 구조)** sang **AI liên kết (connection / 연결) — huấn luyện (training / 학습) độ phức tạp (complexity / 복잡도)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đồ thị (graph / 그래프) algorithms: độ phức tạp (complexity / 복잡도) phụ thuộc biểu diễn (representation / 표현)

BFS/DFS với adjacency danh sách (list / 목록):

```math
O(|V|+|E|).
```

Adjacency ma trận (matrix / 행렬) traversal có thể chi phí (cost / 비용) `O(|V|^2)` even when đồ thị (graph / 그래프) sparse.

Same thuật toán (algorithm / 알고리즘) idea có độ phức tạp (complexity / 복잡도) khác theo dữ liệu (data / 데이터) biểu diễn (representation / 표현). phân tích độ phức tạp (complexity analysis / 복잡도 분석) phải include biểu diễn (representation / 표현) choice.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, sau nội dung của **Đồ thị (graph / 그래프) algorithms: độ phức tạp (complexity / 복잡도) phụ thuộc biểu diễn (representation / 표현)**, **AI liên kết (connection / 연결) — huấn luyện (training / 학습) độ phức tạp (complexity / 복잡도)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Finance liên kết (connection / 연결) — Monte Carlo và scenario explosion** mở rộng hệ quả hoặc giới hạn liên quan.

## AI liên kết (connection / 연결) — huấn luyện (training / 학습) độ phức tạp (complexity / 복잡도)

Huấn luyện (training / 학습) chi phí (cost / 비용) depends on samples, mô hình (model / 모델) dimension, chuỗi (sequence / 시퀀스) length, batch kích thước (size / 크기) và hardware parallelism. Một thao tác (operation / 연산) theoretically `O(n^2)` như full attention becomes major bottleneck khi chuỗi (sequence / 시퀀스) length tăng.

Nhưng FLOP độ phức tạp (complexity / 복잡도) alone chưa đủ: bộ nhớ (memory / 메모리) bandwidth, communication và kernel utilization có thể dominate wall-clock.

> **Nối mạch:** Trong **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Finance liên kết (connection / 연결) — Monte Carlo và scenario explosion** nối từ **AI liên kết (connection / 연결) — huấn luyện (training / 학습) độ phức tạp (complexity / 복잡도)** sang **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes**, vì cơ chế trước tạo đầu vào cho bước sau.

## Finance liên kết (connection / 연결) — Monte Carlo và scenario explosion

Rủi ro (risk / 위험) engines may simulate `N` scenarios across `M` instruments, roughly `O(NM)` valuation công việc (work / 작업) if no sharing. Path-dependent derivatives add thời gian (time / 시간) steps. Variance reduction can reduce scenarios needed for same accuracy, effectively improving cost-to-error quan hệ (relation / 관계) even if per-scenario độ phức tạp (complexity / 복잡도) same.

> **Nối mạch:** Ở chặng này của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** nối từ **Finance liên kết (connection / 연결) — Monte Carlo và scenario explosion** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Asymptotic phân tích (analysis / 분석) can mislead when `n` small, constants huge, bộ nhớ (memory / 메모리) hierarchy dominates hoặc mạng (network / 네트워크) độ trễ (latency / 지연 시간) matters.

Input-size definition itself can be subtle. Integer arithmetic on very large numbers is not constant-time if bit length grows.

Parallel speedup limited by serial fractions and communication; công việc (work / 작업) độ phức tạp (complexity / 복잡도) và span/độ sâu (depth / 깊이) both matter.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> phân tích độ phức tạp (complexity analysis / 복잡도 분석) is growth accounting. Ask what trạng thái (state / 상태) shrinks or expands each step, what tài nguyên (resource / 자원) is counted, and how many structurally distinct steps are needed as đầu vào (input / 입력) quy mô (scale / 규모) grows. Logarithms appear when progress is multiplicative; polynomial/exponential distinctions tell when tối ưu hóa (optimization / 최적화) should mục tiêu (target / 대상) mã (code / 코드) constants versus algorithmic cấu trúc (structure / 구조).

> **Nối mạch:** Trong **Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting công việc (work / 작업) đến scalability**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“Big-O is chính xác (exact / 정확한) thời gian chạy (runtime / 런타임).”** Không; nó là asymptotic bound under a chi phí (cost / 비용) mô hình (model / 모델).

**“`O(1)` means instant.”** Không; constant with respect to `n` can still be expensive.

**“Nested loops always mean `O(n^2)`.”** Need analyze iteration ranges and trạng thái (state / 상태) changes.

**“`O(log n)` means mã (code / 코드) computes logarithm.”** Log often comes from repeated halving or multiplicative branching.

**“Asymptotically better always faster.”** Not at every practical đầu vào (input / 입력) kích thước (size / 크기); constants, bộ nhớ đệm (cache / 캐시) and hardware matter.

**“tối ưu hóa (optimization / 최적화) can rescue `2^n` by making mã (code / 코드) 10× faster.”** Growth-rate problems often require changing algorithmic cấu trúc (structure / 구조).

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
