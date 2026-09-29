# Phân tích khấu hao, ngẫu nhiên hóa và tư duy xác suất

> **Mạch đọc:** Đọc **Phân tích khấu hao, ngẫu nhiên hóa và tư duy xác suất** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Amortized không phải average trường hợp (case / 사례)** sang **2. Phương pháp tổng hợp**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Amortized phân tích (analysis / 분석), Randomization & Probabilistic lập luận (reasoning / 추론) / 상환 분석, 무작위화, 확률적 사고**

Không phải mọi bảo đảm trong DSA đều có dạng “mỗi thao tác luôn mất `O(f(n))`”. Có cấu trúc thỉnh thoảng thực hiện một thao tác rất đắt nhưng cả chuỗi thao tác vẫn rẻ. Có thuật toán chủ động dùng tính ngẫu nhiên để tránh đầu vào xấu. Có cấu trúc dữ liệu chấp nhận sai số xác suất để đổi lấy bộ nhớ nhỏ và khả năng xử lý quy mô lớn.

Ba nhóm này thường bị trộn lẫn nhưng trả lời ba câu hỏi khác nhau:

```text
phân tích khấu hao    -> chi phí được phân bố ra sao trên một chuỗi thao tác?
ngẫu nhiên hóa         -> randomness giúp tránh hoặc phân tán trường hợp xấu thế nào?
cấu trúc xác suất      -> cho phép sai số nào để tiết kiệm tài nguyên?
```

Điểm chung là ta không còn nhìn một thao tác hoặc một lần chạy riêng lẻ; ta nhìn **phân phối chi phí, chuỗi trạng thái hoặc phân phối xác suất của quá trình tính toán**.

## 1. Amortized không phải average trường hợp (case / 사례)

**Phân tích khấu hao (amortized analysis)** không cần giả sử đầu vào ngẫu nhiên. Nó cho một cận trên đối với **mọi chuỗi thao tác hợp lệ** trong mô hình.

Ngược lại, average-case phân tích (analysis / 분석) cần một phân phối đầu vào hoặc mô hình xác suất cụ thể.

Mảng động là ví dụ điển hình. Một lần `append` có thể phải sao chép toàn bộ `n` phần tử khi resize, nhưng nếu sức chứa (capacity / 용량) tăng theo cấp số nhân thì `m` lần append có tổng chi phí tuyến tính. Vì vậy chi phí khấu hao mỗi append là `O(1)`.

Điều này không có nghĩa từng append là `O(1)` trong trường hợp xấu nhất.

## 2. Phương pháp tổng hợp

**Phương pháp tổng hợp (aggregate method)** tính tổng chi phí của cả chuỗi rồi chia cho số thao tác.

Với mảng tăng dung lượng gấp đôi:

\[
1+2+4+\cdots < 2m
\]

Tổng số phần tử phải sao chép qua `m` lần append là `O(m)`. Cộng thêm `m` lần ghi phần tử mới, tổng vẫn `O(m)`.

Do đó:

\[
\frac{O(m)}{m}=O(1)
\]

Điểm cốt lõi là thao tác đắt ngày càng thưa nhờ tăng trưởng hình học.

## 3. Phương pháp hạch toán

**Phương pháp hạch toán (accounting method)** gán một chi phí quy ước cho mỗi thao tác. Một thao tác rẻ có thể bị “thu phí” cao hơn chi phí thật; phần dư trở thành tín dụng dùng để trả cho thao tác đắt trong tương lai.

Nếu luôn giữ tổng tín dụng không âm, tổng chi phí thật không thể vượt tổng chi phí quy ước đã thu.

Đây là một mô hình rất thực dụng:

> thao tác rẻ hiện tại có thể đang trả trước cho công việc mà cấu trúc chắc chắn phải làm sau này.

## 4. Phương pháp thế năng

Phương pháp tổng quát hơn gán cho trạng thái `D` một hàm thế năng:

\[
\Phi(D)\ge 0
\]

Chi phí khấu hao của thao tác `i`:

\[
\hat c_i=c_i+\Phi(D_i)-\Phi(D_{i-1})
\]

Khi thao tác rẻ làm tích lũy “công việc tiềm năng”, thế năng tăng. Khi thao tác đắt tiêu thụ phần tích lũy đó, thế năng giảm.

Cộng qua cả chuỗi cho hiệu ứng telescoping:

\[
\sum_i \hat c_i
=
\sum_i c_i + \Phi(D_m)-\Phi(D_0)
\]

Nếu `Φ(D_0)=0` và thế năng không âm, tổng chi phí khấu hao tạo cận trên cho tổng chi phí thật.

## 5. Chọn hàm thế năng thế nào?

Đây thường là phần khó nhất. Một hàm thế năng tốt đo “mức công việc bị trì hoãn” hoặc “độ căng” của cấu trúc.

Ví dụ:

```text
mảng động       -> mức lấp đầy/capacity chưa sử dụng
stack multipop  -> số phần tử còn nằm trong stack
Splay Tree      -> tổng log kích thước subtree theo một rank phù hợp
```

Không có công thức chung để đo thế năng. Cần hiểu điều gì khiến thao tác tương lai trở nên đắt, rồi đo lượng “nợ” đó trong trạng thái hiện tại.

## 6. ngăn xếp (stack / 스택) với multipop

Giả sử ngăn xếp (stack / 스택) hỗ trợ `push`, `pop`, `multipop(k)`. Một lần `multipop` có thể pop `O(n)` phần tử.

Nhưng mỗi phần tử chỉ được push một lần và pop tối đa một lần. Vì vậy qua `m` thao tác, tổng số lần pop bị chặn bởi tổng số lần push.

Total công việc (work / 작업) là `O(m)`, nên chi phí khấu hao mỗi thao tác là `O(1)`.

Mẫu quan trọng:

> nếu một vòng lặp bên trong tiêu thụ đối tượng mà đối tượng đó không quay trở lại, tổng số lần lặp có thể tuyến tính dù nhìn bề ngoài giống vòng lặp lồng nhau.

## 7. Monotonic ngăn xếp (stack / 스택) và Deque

Trong Next Greater Element, mỗi phần tử vào ngăn xếp (stack / 스택) đúng một lần và rời ngăn xếp (stack / 스택) tối đa một lần. Trong sliding-window maximum với deque đơn điệu, mỗi chỉ số cũng được push một lần và pop tối đa một lần.

Vì vậy các vòng `while` bên trong không tạo `O(n²)`; tổng số lần pop trên toàn bộ thuật toán vẫn `O(n)`.

Đây là một trong những mẫu (pattern / 패턴) khấu hao quan trọng nhất khi đọc mã (code / 코드).

## 8. DSU và “thao tác đắt làm tương lai rẻ hơn”

Union-Find với union-by-rank/kích thước (size / 크기) và đường dẫn (path / 경로) compression có chi phí khấu hao:

\[
O(\alpha(n))
\]

với `α` là hàm Ackermann nghịch đảo, tăng cực chậm.

Một lần `find` có thể đi qua nhiều nút, nhưng đồng thời nén đường và cải thiện cấu trúc cho các lần `find` sau. Chi phí hiện tại tạo lợi ích cho tương lai.

Đây là dạng phân tích khấu hao khác động (dynamic / 동적) array: thao tác đắt không chỉ hiếm mà còn **tự làm cấu trúc tốt hơn**.

## 9. Splay cây (tree / 트리)

Splay cây (tree / 트리) không giữ cân bằng cứng sau mỗi thao tác. Một truy cập có thể tốn `O(n)`, nhưng một chuỗi thao tác có chi phí khấu hao `O(log n)` mỗi thao tác dưới phân tích chuẩn.

Ngoài ra, các phần tử được truy cập gần đây có xu hướng được đưa gần gốc, tạo tính thích nghi với locality của tải công việc (workload / 워크로드).

Bài học:

> bảo đảm khấu hao cho phép thiết kế cấu trúc đơn giản hơn hoặc thích nghi tốt hơn, nhưng phải chấp nhận một thao tác đơn lẻ có thể đắt.

## 10. Amortized guarantee và tail độ trễ (latency / 지연 시간)

Trong hệ thống latency-sensitive, “`O(1)` amortized” có thể chưa đủ. Resize của động (dynamic / 동적) array hoặc rehash của bảng băm (hash table / 해시 테이블) vẫn tạo một lần dừng lớn.

Các kỹ thuật hệ thống gồm:

```text
preallocation
incremental resizing
incremental rehashing
bounded ring buffer
real-time queue
```

Chúng cố biến một thao tác rất đắt thành nhiều phần việc nhỏ hơn để giảm tail độ trễ (latency / 지연 시간).

Thông lượng tốt và độ trễ đuôi thấp là hai mục tiêu khác nhau.

## 11. Deamortization

**Khử khấu hao (deamortization)** là quá trình biến một cấu trúc có bảo đảm tốt trên chuỗi thành cấu trúc có cận tốt hơn cho từng thao tác riêng lẻ.

Ví dụ, thay vì rehash toàn bảng trong một lần, ta di chuyển vài bucket sau mỗi thao tác. Trong thời gian chuyển đổi, tra cứu có thể phải kiểm tra cả bảng cũ và bảng mới.

Ta trả thêm độ phức tạp hiện thực (implementation / 구현) để đổi lấy độ trễ (latency / 지연 시간) ổn định hơn.

## 12. Randomized thuật toán (algorithm / 알고리즘) là gì?

Thuật toán ngẫu nhiên dùng randomness như một phần của lô-gic (logic / 논리). Với cùng đầu vào, hai lần chạy có thể đi qua các trạng thái khác nhau.

Mục tiêu thường là:

```text
tránh đầu vào bệnh lý cố định
đơn giản hóa cấu trúc
đạt expected bound tốt
phân tán tải hoặc collision
```

Randomized Quicksort là ví dụ kinh điển: pivot ngẫu nhiên làm một thứ tự đầu vào cố định không còn dễ ép thuật toán luôn chọn pivot tệ.

## 13. Expected thời gian (time / 시간) phải nói expectation lấy trên cái gì

Nói `O(n log n)` kỳ vọng là chưa đủ nếu không rõ expectation đến từ đâu.

Có thể là:

```text
randomness của thuật toán
phân phối của đầu vào
random hash function
random priority của cấu trúc
```

Hai phân tích có cùng chữ “expected” nhưng giả định khác nhau có thể cho mức bảo đảm rất khác.

## 14. Las Vegas và Monte Carlo

**Las Vegas:** kết quả luôn đúng; randomness ảnh hưởng thời gian chạy hoặc cấu trúc nội bộ.

Ví dụ: Randomized Quicksort vẫn trả mảng đã sắp xếp đúng.

**Monte Carlo:** thời gian được kiểm soát tốt nhưng kết quả có xác suất sai.

Ví dụ: fingerprint để kiểm tra bằng nhau hoặc một số primality kiểm thử (test / 테스트) xác suất.

Distinction này rất quan trọng vì một hệ thống có thể chấp nhận thời gian không xác định nhưng không được phép trả kết quả sai, hoặc ngược lại.

## 15. Amplification để giảm xác suất sai

Nếu một phép kiểm tra Monte Carlo độc lập có xác suất sai `p<1`, lặp lại `k` lần và chỉ chấp nhận khi tất cả đồng ý có thể làm xác suất sai giảm theo hàm mũ, tùy cấu trúc phép thử:

\[
p^k
\]

Ý tưởng **khuếch đại xác suất (probability amplification)** cho thấy có thể đổi thêm CPU lấy mức tin cậy cao hơn.

Điều kiện quan trọng là các lần thử phải đủ độc lập theo mô hình phân tích.

## 16. Universal Hashing

Nếu adversary biết hàm băm (hash / 해시) cố định, họ có thể chọn khóa gây va chạm. Universal hashing chọn hàm từ một họ ngẫu nhiên sao cho với hai khóa khác nhau, xác suất collision bị chặn.

Mục tiêu không phải “không bao giờ collision”, mà là làm một tập khóa cố định khó kiểm soát phân phối collision trước khi hàm băm (hash / 해시) được chọn.

Trong hệ thống nhận đầu vào (input / 입력) không tin cậy, threat mô hình (model / 모델) này quan trọng hơn average-case trên dữ liệu ngẫu nhiên.

## 17. Treap

Treap giữ hai bất biến:

```text
BST order theo key
heap order theo priority ngẫu nhiên
```

Nếu priorities độc lập ngẫu nhiên, chiều cao kỳ vọng là `O(log n)`.

Treap cho thấy randomness có thể được mã hóa trong **siêu dữ liệu (metadata / 메타데이터) của cấu trúc**, không nhất thiết là một nhánh random trong thuật toán.

Các thao tác split/merge còn làm Treap rất hữu ích cho chuỗi (sequence / 시퀀스) động và implicit cây (tree / 트리).

## 18. Skip danh sách (list / 목록)

Skip danh sách (list / 목록) tạo các tầng “đường cao tốc” ngẫu nhiên. Mỗi nút (node / 노드) được promote lên tầng tiếp theo với xác suất `p`.

Kỳ vọng chiều cao `O(log n)`, tìm kiếm/chèn/xóa kỳ vọng `O(log n)`.

Không cần rotation hoặc balance factor cứng. Balance đến từ phân phối ngẫu nhiên của chiều cao nút (node / 노드).

## 19. Randomized Selection

Quickselect với pivot ngẫu nhiên có thời gian kỳ vọng `O(n)`. Trực giác: pivot không cần luôn gần median; chỉ cần đủ thường xuyên tạo partition làm giảm đáng kể bài toán còn lại.

Expected tuyến tính (linear / 선형) thời gian (time / 시간) không có nghĩa mỗi lần chạy tuyến tính (linear / 선형). Nếu cần worst-case tuyến tính (linear / 선형) thời gian (time / 시간), Median-of-Medians cung cấp bảo đảm mạnh hơn với constant factor và hiện thực (implementation / 구현) phức tạp hơn.

Đây là ví dụ rõ của sự đánh đổi (trade-off / 트레이드오프):

```text
đơn giản + expected guarantee
vs
phức tạp hơn + deterministic worst-case guarantee
```

## 20. Indicator Variables

Một kỹ thuật phân tích rất mạnh là định nghĩa biến chỉ báo:

\[
I_i = 1 \văn bản (text / 텍스트){ nếu sự kiện i xảy ra, ngược lại 0}
\]

Khi đó:

\[
E[I_i]=P(i)
\]

Nếu `X=ΣI_i`:

\[
E[X]=\sum E[I_i]
\]

Không cần các `I_i` độc lập để dùng tính tuyến tính của kỳ vọng.

Đây là công cụ tiêu chuẩn để đếm expected number of collisions, comparisons hoặc selected events.

## 21. Linearity of Expectation

Tính chất:

\[
E[X+Y]=E[X]+E[Y]
\]

đúng ngay cả khi `X` và `Y` phụ thuộc nhau.

Điều này cực kỳ hữu ích vì phân tích trực tiếp toàn bộ random tiến trình (process / 프로세스) thường khó, nhưng expected contribution của từng sự kiện riêng lẻ có thể dễ tính.

## 22. Kỳ vọng không mô tả tail

Một thuật toán có expected thời gian (time / 시간) tốt vẫn có thể có phân phối đuôi xấu. Trong hệ thống, p99/p999 độ trễ (latency / 지연 시간) hoặc xác suất chạy quá deadline có thể quan trọng hơn mean.

Để nói mạnh hơn, cần các công cụ như:

```text
variance
Markov bound
Chebyshev bound
Chernoff/Hoeffding bounds
high-probability guarantees
```

Không nhất thiết phải dùng các công thức nâng cao ở mọi bài, nhưng phải nhớ rằng **mean không đủ mô tả rủi ro**.

## 23. Markov Inequality như một cận thô

Với biến ngẫu nhiên không âm `X`:

\[
P(X\ge a)\le \frac{E[X]}a
\]

Cận Markov thường lỏng nhưng cho thấy từ kỳ vọng có thể suy ra một cận xác suất cơ bản mà không cần biết phân phối đầy đủ.

## 24. Union Bound

Với các sự kiện `A_i`:

\[
P(\cup_i A_i)\le \sum_i P(A_i)
\]

Không cần độc lập.

Union bound rất hữu ích khi cần chứng minh “xác suất bất kỳ trong số nhiều lỗi xảy ra vẫn nhỏ”. Ví dụ nếu mỗi một trong `n` sự kiện lỗi có xác suất ≤ `1/n³`, tổng xác suất có ít nhất một lỗi ≤ `1/n²`.

## 25. High-Probability Guarantee

Một kết quả có thể được mô tả là đúng hoặc nhanh **với xác suất cao (with high probability)**, thường nghĩa xác suất thất bại giảm đa thức theo `n`, ví dụ `1/n^c`.

Đây là bảo đảm mạnh hơn chỉ nói expectation tốt vì nó kiểm soát tail theo kích thước đầu vào.

Khi đọc paper hoặc tài liệu nâng cao, phải phân biệt:

```text
expected O(f(n))
O(f(n)) with high probability
worst-case O(f(n))
```

## 26. Probabilistic cấu trúc dữ liệu (data structure / 자료구조) khác Randomized thuật toán (algorithm / 알고리즘)

Bloom Filter có thể trả dương tính giả. HyperLogLog ước lượng cardinality. Count-Min Sketch ước lượng frequency.

Ở đây randomness không chỉ ảnh hưởng thời gian chạy (runtime / 런타임); **đầu ra (output / 출력) itself có bất định (uncertainty / 불확실성) có kiểm soát**.

Mô hình thiết kế cần xác định:

```text
loại sai số
biên sai số
xác suất thất bại
khả năng merge
khả năng delete/update
```

## 27. One-sided và two-sided lỗi (error / 오류)

Bloom Filter chuẩn có false positive nhưng không false negative trong mô hình chỉ chèn. Đây là **sai số một phía (one-sided error)**.

Một estimator khác có thể cao hoặc thấp hơn giá trị thật, tạo **sai số hai phía (two-sided error)**.

One-sided guarantee rất mạnh khi cấu trúc được dùng làm bộ lọc trước một bước chính xác: false positive chỉ tạo thêm công việc (work / 작업), còn false negative có thể phá tính đúng đắn.

## 28. Random Seed là một phần của khả năng tái hiện

Randomized mã (code / 코드) khó gỡ lỗi (debug / 디버그) nếu seed không được ghi lại. Trong kiểm thử (test / 테스트) và benchmark nên cho phép cố định seed.

Trong môi trường vận hành (production / 운영 환경), seed có thể được chọn ngẫu nhiên hoặc bí mật để giảm khả năng adversary đoán cấu trúc băm (hash / 해시). Đây là hai mục tiêu khác nhau:

```text
reproducibility trong test
unpredictability trong production
```

## 29. Adaptive Adversary

Một số phân tích giả định adversary chọn đầu vào (input / 입력) trước khi randomness được lộ. Nếu attacker có thể quan sát đầu ra (output / 출력) hoặc timing rồi thích nghi đầu vào (input / 입력) tiếp theo, bảo đảm có thể yếu hơn.

Trong hệ thống bảo mật hoặc online thuật toán (algorithm / 알고리즘), cần biết threat mô hình (model / 모델) là **oblivious adversary** hay **adaptive adversary**.

Randomization không tự động chống được mọi đối thủ.

## 30. Pseudorandomness trong triển khai

Thuật toán lý thuyết thường giả định random bits độc lập lý tưởng. thời gian chạy (runtime / 런타임) thực tế dùng PRNG.

Với DSA phổ thông, PRNG chất lượng tốt thường đủ. Với bảo mật (security / 보안), cần CSPRNG. Không nên dùng một bộ sinh yếu rồi giả định mọi theorem ngẫu nhiên vẫn giữ nguyên dưới đầu vào đối nghịch.

## 31. Testing Randomized Algorithms

Không nên viết kiểm thử (test / 테스트) kiểu “thời gian chạy (runtime / 런타임) luôn dưới X” cho một thuật toán expected-time.

Cách tốt hơn:

```text
kiểm tra correctness ở mọi run
cố định seed cho regression
chạy nhiều seed cho statistical behavior
kiểm tra invariants sau random operations
```

Với cấu trúc xác suất, cần đo phân phối (distribution / 분포) của lỗi (error / 오류) qua nhiều dataset/seed chứ không chỉ một lần chạy.

## 32. Khi nào nên chọn deterministic guarantee?

Deterministic worst-case bound phù hợp khi:

```text
hard real-time / deadline
input có thể đối nghịch
security-sensitive path
latency tail cực quan trọng
reproducibility là yêu cầu mạnh
```

Expected/amortized/randomized thiết kế (design / 설계) phù hợp khi thông lượng (throughput / 처리량) và simplicity quan trọng hơn worst-case từng thao tác.

Không có một loại guarantee luôn tốt nhất; phải khớp với SLA và threat mô hình (model / 모델).

## 33. Bảng phân biệt nhanh

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Loại bảo đảm | Câu hỏi chính |
|---|---|
| Worst-case | một thao tác/lần chạy tệ nhất có thể đắt tới đâu? |
| Amortized | tổng chi phí của mọi chuỗi thao tác bị chặn thế nào? |
| Average-case | dưới phân phối đầu vào (input / 입력) đã chọn, chi phí trung bình là gì? |
| Expected randomized | expectation trên random choices của thuật toán là gì? |
| High-probability | tail xác suất (probability / 확률) giảm mạnh tới mức nào? |
| Probabilistic đầu ra (output / 출력) | đầu ra (output / 출력) có thể sai bao nhiêu và với xác suất nào? |

## Mô hình tư duy

> Phân tích khấu hao nói về **phân phối chi phí theo thời gian**. Ngẫu nhiên hóa nói về **phân phối hành vi theo lựa chọn random**. Cấu trúc xác suất nói về **phân phối sai số của câu trả lời**.

Khi thấy một bảo đảm không phải worst-case đơn giản, hãy hỏi: **đang lấy trung bình trên cái gì, adversary được phép làm gì, một thao tác riêng lẻ có thể đắt tới đâu, tail xác suất (probability / 확률) ra sao, đầu ra (output / 출력) có được phép sai không, và hệ thống cần thông lượng (throughput / 처리량) hay độ trễ (latency / 지연 시간) guarantee?**

Xem thêm: [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [Mathematical Toolkit](../00_foundations/04_mathematical_toolkit_for_dsa.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [Skip Lists](../02_trees/07_skip_lists.md), [Probabilistic Data Structures](./06_probabilistic_data_structures.md).
