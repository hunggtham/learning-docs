# chia để trị

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **chia để trị**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Ba câu hỏi trước khi dùng chia để trị** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **2. công thức truy hồi là ngôn ngữ tự nhiên của decomposition** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Chia để trị / chia để trị / 분할 정복**

chia để trị là một chiến lược thiết kế thuật toán trong đó một bài toán (problem / 문제) lớn được tách thành các subproblems nhỏ hơn có cấu trúc tương tự, giải các phần đó, rồi ghép kết quả lại. mẫu kinh điển:

```text
Divide → Conquer → Combine
```

Điểm quan trọng không phải “dùng recursion”. Một hàm recursive chưa chắc là divide-and-conquer, và một thuật toán divide-and-conquer có thể được implement iterative. Bản chất nằm ở **decomposition**: bài toán (problem / 문제) được tách thành các phần nhỏ hơn sao cho mỗi phần có thể giải tương đối độc lập và phần kết hợp không phá lợi ích của việc chia nhỏ.

## 1. Ba câu hỏi trước khi dùng chia để trị

Khi nhìn một bài toán (problem / 문제), hãy hỏi:

```text
Có thể chia input/state thành những phần nhỏ hơn cùng loại không?
Các phần có overlap/recompute nhiều không?
Combine result có rẻ hơn giải trực tiếp toàn problem không?
```

Nếu subproblems overlap mạnh, quy hoạch động (dynamic programming) thường tự nhiên hơn. Nếu kết hợp step đắt gần bằng brute force, việc chia không giúp nhiều. Nếu decomposition rất mất cân bằng, recursion độ sâu có thể xấu.

> **Chuyển mạch:** Trong **chia để trị**, **2. công thức truy hồi là ngôn ngữ tự nhiên của decomposition** tiếp nhận điểm tựa từ **1. Ba câu hỏi trước khi dùng chia để trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. cây đệ quy: xem công việc (work / 작업) nằm ở đâu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. công thức truy hồi là ngôn ngữ tự nhiên của decomposition

Nếu mỗi bài toán kích thước `n` tạo `a` bài toán con kích thước khoảng `n/b`, và phần công việc ngoài đệ quy là `f(n)`:

\[
T(n)=aT(n/b)+f(n)
\]

sắp xếp trộn:

\[
T(n)=2T(n/2)+\Theta(n)
\]

tìm kiếm nhị phân:

\[
T(n)=T(n/2)+\Theta(1)
\]

Karatsuba:

\[
T(n)=3T(n/2)+\Theta(n)
\]

công thức truy hồi ghi lại chính **shape của computation cây**.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **3. cây đệ quy: xem công việc (work / 작업) nằm ở đâu** tiếp nhận điểm tựa từ **2. công thức truy hồi là ngôn ngữ tự nhiên của decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Định lý Master: cách rút gọn có điều kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. cây đệ quy: xem công việc (work / 작업) nằm ở đâu

Với sắp xếp trộn, mỗi tầng có tổng kích thước đầu vào `n`, nên kết hợp công việc (work / 작업) mỗi tầng là `Θ(n)`. Có `Θ(log n)` các tầng:

\[
T(n)=\Theta(n\log n)
\]

Với:

\[
T(n)=2T(n/2)+\Theta(1)
\]

nội bộ công việc (work / 작업) mỗi nút constant, nhưng số các nút lá là `Θ(n)`, nên total `Θ(n)`.

Đừng nhìn thấy `2T(n/2)` rồi tự động kết luận `n log n`; hãy hỏi **công việc (work / 작업) phân bố theo tầng thế nào**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **4. Định lý Master: cách rút gọn có điều kiện** tiếp nhận điểm tựa từ **3. cây đệ quy: xem công việc (work / 작업) nằm ở đâu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. sắp xếp trộn: kết hợp step dựa trên điều kiện trước mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Định lý Master: cách rút gọn có điều kiện

Với công thức truy hồi chuẩn:

\[
T(n)=aT(n/b)+f(n)
\]

so sánh `f(n)` với:

\[
n^{\log_b a}
\]

Term này đại diện quy mô công việc (work / 작업) của cây đệ quy nếu nội bộ kết hợp nhỏ.

Định lý Master rất tiện nhưng không áp dụng cho mọi công thức truy hồi. Ví dụ:

\[
T(n)=T(n/3)+T(2n/3)+\Theta(n)
\]

không đúng dạng equal-size subproblems. cây đệ quy/Akra–Bazzi lập luận (reasoning / 추론) phù hợp hơn.

> **Chuyển mạch:** Trong **chia để trị**, **5. sắp xếp trộn: kết hợp step dựa trên điều kiện trước mạnh** tiếp nhận điểm tựa từ **4. Định lý Master: cách rút gọn có điều kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. tìm kiếm nhị phân: chia để trị một nhánh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. sắp xếp trộn: kết hợp step dựa trên điều kiện trước mạnh

Hai halves đã sorted, nên merge tuyến tính (linear / 선형) bằng hai con trỏ (two pointers):

```text
left smallest vs right smallest
chọn nhỏ hơn
advance pointer tương ứng
```

Bất biến (invariant / 불변식):

> Prefix đầu ra luôn là các phần tử nhỏ nhất đã được quyết định đúng thứ tự từ hai halves.

Nếu halves chưa sorted, kết hợp `O(n)` này không tồn tại. Divide-and-conquer hiệu quả vì recursive công việc (work / 작업) đã tạo ra **cấu trúc (structure / 구조) thuận lợi cho kết hợp**.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **6. tìm kiếm nhị phân: chia để trị một nhánh** tiếp nhận điểm tựa từ **5. sắp xếp trộn: kết hợp step dựa trên điều kiện trước mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Quicksort: chất lượng divide quyết định môi trường chạy (runtime)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. tìm kiếm nhị phân: chia để trị một nhánh

tìm kiếm nhị phân chia interval nhưng chỉ tiếp tục một half.

điều kiện trước là monotonic/sorted thông tin đủ mạnh để chứng minh half còn lại không thể chứa answer.

Mỗi bước giảm không gian tìm kiếm theo tỷ lệ:

\[
T(n)=T(n/2)+O(1)=O(\log n)
\]

Không phải cứ lấy midpoint là tìm kiếm nhị phân; phần cốt lõi là chứng minh loại được nửa các ứng viên.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **7. Quicksort: chất lượng divide quyết định môi trường chạy (runtime)** tiếp nhận điểm tựa từ **6. tìm kiếm nhị phân: chia để trị một nhánh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Quickselect: mục tiêu (objective / 목표) quyết định số subproblems cần giải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Quicksort: chất lượng divide quyết định môi trường chạy (runtime)

Partition quanh pivot tạo hai subarrays. Nếu gần cân bằng:

\[
T(n)=2T(n/2)+O(n)=O(n\log n)
\]

Nếu liên tục lệch `0` và `n-1`:

\[
T(n)=T(n-1)+O(n)=O(n^2)
\]

Đây là ví dụ rõ rằng cùng khung làm việc chia để trị nhưng **chất lượng phân hoạch** thay đổi toàn bộ cây đệ quy.

ngẫu nhiên hóa pivot giúp kỳ vọng hành vi tốt hơn, nhưng trường hợp xấu nhất vẫn khác kỳ vọng-case.

> **Chuyển mạch:** Trong **chia để trị**, **8. Quickselect: mục tiêu (objective / 목표) quyết định số subproblems cần giải** tiếp nhận điểm tựa từ **7. Quicksort: chất lượng divide quyết định môi trường chạy (runtime)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Closest Pair: kết hợp được cứu bởi hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Quickselect: mục tiêu (objective / 목표) quyết định số subproblems cần giải

Selection chỉ cần rank `k`, nên sau partition chỉ recurse vào side chứa `k`.

kỳ vọng công thức truy hồi gần:

\[
T(n)=T(n/2)+O(n)=O(n)
\]

Sắp xếp toàn bộ sẽ tạo nhiều thông tin thứ tự hơn mức đầu ra yêu cầu.

Lesson:

> Decomposition không có nghĩa phải solve tất cả branches. Solve đúng những subproblems mà mục tiêu (objective / 목표) thật sự cần.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **9. Closest Pair: kết hợp được cứu bởi hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **8. Quickselect: mục tiêu (objective / 목표) quyết định số subproblems cần giải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Karatsuba: giảm hệ số phân nhánh bằng đại số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Closest Pair: kết hợp được cứu bởi hình học (geometry / 기하학)

Cách đơn giản xét mọi cặp có độ phức tạp `O(n²)`. Cách chia để trị chia các điểm theo trục x, giải hai nửa rồi lấy khoảng cách tốt nhất `d`.

Các ứng viên đi qua đường chia chỉ cần xét trong một dải rộng `2d`. Nếu các điểm trong dải được sắp theo y, lập luận đóng gói cho thấy mỗi điểm chỉ cần so với một số hằng ứng viên tiếp theo.

kết hợp giữ `O(n)` mỗi tầng, total `O(n log n)`.

Đây là mẫu quan trọng: **domain-specific theorem làm kết hợp rẻ**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **10. Karatsuba: giảm hệ số phân nhánh bằng đại số** tiếp nhận điểm tựa từ **9. Closest Pair: kết hợp được cứu bởi hình học (geometry / 기하학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Fast Exponentiation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Karatsuba: giảm hệ số phân nhánh bằng đại số

Cách đơn giản multiplication hai số split high/low cần 4 multiplications recursive. Karatsuba biến đổi để chỉ cần 3:

\[
T(n)=3T(n/2)+O(n)
\]

nên:

\[
T(n)=O(n^{\log_2 3})\approx O(n^{1.585})
\]

Tối ưu hóa (optimization / 최적화) ở đây không giảm kích thước đầu vào nhiều hơn; nó giảm số branches `a`.

> **Chuyển mạch:** Trong **chia để trị**, **11. Fast Exponentiation** tiếp nhận điểm tựa từ **10. Karatsuba: giảm hệ số phân nhánh bằng đại số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. phép nhân ma trận (matrix multiplication / 행렬 곱셈) và khối (block / 블록) decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Fast Exponentiation

Tính `a^n` bằng n multiplications là `O(n)`. Nhưng:

\[
a^n=(a^{n/2})^2
\]

với n chẵn, và thêm một factor `a` nếu n lẻ.

Mỗi bước halve exponent:

\[
O(\log n)
\]

mẫu này xuất hiện trong modular exponentiation, ma trận (matrix / 행렬) exponentiation và nhảy nhị phân.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **12. phép nhân ma trận (matrix multiplication / 행렬 곱셈) và khối (block / 블록) decomposition** tiếp nhận điểm tựa từ **11. Fast Exponentiation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. chia để trị vs quy hoạch động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. phép nhân ma trận (matrix multiplication / 행렬 곱셈) và khối (block / 블록) decomposition

Cách đơn giản phép nhân ma trận (matrix multiplication / 행렬 곱셈) `O(n³)`. Divide ma trận (matrix / 행렬) thành quadrants giúp tính cục bộ bộ nhớ đệm và mở đường cho các thuật toán giảm số recursive multiplications như Strassen.

Strassen giảm 8 recursive products xuống 7:

\[
T(n)=7T(n/2)+O(n^2)
\]

nên exponent nhỏ hơn 3.

Nhưng constants, numeric tính ổn định và bộ nhớ hành vi quyết định khi nào nó thực dụng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **13. chia để trị vs quy hoạch động** tiếp nhận điểm tựa từ **12. phép nhân ma trận (matrix multiplication / 행렬 곱셈) và khối (block / 블록) decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. chia để trị vs quay lui (backtracking)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. chia để trị vs quy hoạch động

Fibonacci recursion chia thành `F(n-1)` và `F(n-2)` nhưng sự chồng lặp bài toán con rất mạnh. Pure divide-and-conquer recompute cùng các trạng thái nhiều lần.

DP thêm memoization/tabulation để reuse:

```text
Divide-and-conquer: branches mostly independent
Dynamic Programming: many branches converge to same state
```

Question hữu ích:

> Hai histories khác nhau có dẫn tới cùng chính xác tương lai trạng thái (state / 상태) không?

Nếu có nhiều convergence, nghĩ tới DP.

> **Chuyển mạch:** Trong **chia để trị**, **14. chia để trị vs quay lui (backtracking)** tiếp nhận điểm tựa từ **13. chia để trị vs quy hoạch động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Unbalanced các công thức truy hồi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. chia để trị vs quay lui (backtracking)

Quay lui cũng tạo cây đệ quy nhưng mục tiêu khác. Chia để trị chia bài toán thành các bài toán con cần giải rồi ghép kết quả; quay lui liệt kê các lựa chọn trong không gian tìm kiếm và cắt tỉa những nhánh không hợp lệ hoặc không hứa hẹn.

Quicksort recursion không phải “thử choices”; N-Queens không phải “kết hợp independent halves”.

Nhìn cùng hình cây recursion không có nghĩa cùng paradigm.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **15. Unbalanced các công thức truy hồi** tiếp nhận điểm tựa từ **14. chia để trị vs quay lui (backtracking)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Base-case threshold và hybrid các thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Unbalanced các công thức truy hồi

Một công thức truy hồi:

\[
T(n)=T(n/10)+T(9n/10)+O(n)
\]

vẫn có thể `O(n log n)` dù split không 50/50, vì độ sâu vẫn logarithmic theo constant ratio và total tầng công việc (work / 작업) tuyến tính (linear / 선형) theo lập luận (reasoning / 추론) phù hợp.

Nhưng:

\[
T(n)=T(1)+T(n-1)+O(n)
\]

có độ sâu tuyến tính (linear / 선형) và total quadratic.

Balance không cần hoàn hảo; quan trọng là **mỗi branch giảm theo tỷ lệ đủ mạnh hay không**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **15. Unbalanced các công thức truy hồi** cho ta quy tắc; **16. Base-case threshold và hybrid các thuật toán** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **17. Tail-recursion elimination cho Quicksort ngăn xếp (stack / 스택) độ sâu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Base-case threshold và hybrid các thuật toán

các lời gọi đệ quy có overhead. Với subarray rất nhỏ, insertion sort có thể nhanh hơn quick/sắp xếp trộn.

Trong hệ thống thực tế, sort thường:

```text
large partitions -> divide-and-conquer
small partitions -> insertion-like strategy
pathological depth -> fallback heapsort/introsort
```

Hybrid thuật toán giữ asymptotic bảo đảm nhưng tối ưu constants theo regime.

> **Chuyển mạch:** Trong **chia để trị**, **16. Base-case threshold và hybrid các thuật toán** cho ta quy tắc; **17. Tail-recursion elimination cho Quicksort ngăn xếp (stack / 스택) độ sâu** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **18. Parallel chia để trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Tail-recursion elimination cho Quicksort ngăn xếp (stack / 스택) độ sâu

Nếu always recurse vào phân vùng nhỏ hơn trước và xử lý phân vùng lớn hơn bằng vòng lặp (loop / 루프), ngăn xếp lời gọi độ sâu có thể giữ `O(log n)` ngay cả khi partitions không đẹp theo một phía.

mẫu:

```text
partition
recurse smaller side
loop on larger side
```

Ta đang dùng tường minh (explicit / 명시적) control-flow phép biến đổi để giảm ngăn xếp (stack / 스택) usage mà không đổi lô-gic (logic / 논리) partitioning.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **18. Parallel chia để trị** tiếp nhận điểm tựa từ **17. Tail-recursion elimination cho Quicksort ngăn xếp (stack / 스택) độ sâu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Grain kích thước (size / 크기) trong parallel recursion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Parallel chia để trị

Nếu subproblems độc lập, có thể fork tasks song song.

sắp xếp trộn:

```text
sort left  || sort right
then merge
```

Nhưng parallel speedup bị giới hạn bởi:

```text
task creation overhead
synchronization
memory bandwidth
combine bottleneck
load imbalance
```

Amdahl's Law nhắc rằng phần serial còn lại giới hạn speedup tổng thể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **19. Grain kích thước (size / 크기) trong parallel recursion** tiếp nhận điểm tựa từ **18. Parallel chia để trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. công việc (work / 작업) và Span** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Grain kích thước (size / 크기) trong parallel recursion

Nếu spawn tác vụ (task / 작업) tới từng subproblem rất nhỏ, bộ lập lịch overhead có thể lớn hơn actual công việc (work / 작업).

Trong hệ thống thực tế, fork-join thường có threshold:

```text
if size <= threshold:
    solve sequentially
else:
    split and parallelize
```

Threshold là kỹ thuật (engineering / 엔지니어링) parameter cần benchmark.

> **Chuyển mạch:** Trong **chia để trị**, **20. công việc (work / 작업) và Span** tiếp nhận điểm tựa từ **19. Grain kích thước (size / 크기) trong parallel recursion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Cache-oblivious các thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. công việc (work / 작업) và Span

Trong parallel thuật toán phân tích (analysis / 분석):

- **công việc (work / 작업)** = tổng các thao tác nếu chạy sequential;
- **Span / trọng yếu (critical / 중요) đường đi** = longest phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬).

Potential parallelism xấp xỉ:

\[
công việc (work / 작업)/Span
\]

Divide-and-conquer tự nhiên cho mô hình này vì cây đệ quy thể hiện phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조) rõ ràng.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **21. Cache-oblivious các thuật toán** tiếp nhận điểm tựa từ **20. công việc (work / 작업) và Span** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. In-place chia để trị vs extra bộ đệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Cache-oblivious các thuật toán

Recursive decomposition thường xử lý smaller contiguous regions. Khi region đủ nhỏ để fit bộ nhớ đệm, tính cục bộ (locality) tự cải thiện dù thuật toán không biết bộ nhớ đệm kích thước (size / 크기) cụ thể.

Cache-oblivious ma trận (matrix / 행렬) các thuật toán, recursive transpose/bố trí và divide-based searching tận dụng tính chất này.

Đây là cầu nối (bridge / 브리지) giữa asymptotic decomposition và phân cấp bộ nhớ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **22. In-place chia để trị vs extra bộ đệm** tiếp nhận điểm tựa từ **21. Cache-oblivious các thuật toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. ổn định Partition khó hơn unstable partition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. In-place chia để trị vs extra bộ đệm

sắp xếp trộn mảng thường cần bộ đệm `O(n)`. Quicksort có thể partition in-place với bộ nhớ phụ trợ chủ yếu ngăn xếp đệ quy.

Nhưng in-place không luôn nhanh hơn: bộ đệm bản sao (copy / 복사) có thể sequential/thân thiện với bộ nhớ đệm hơn phức tạp swapping.

độ phức tạp bộ nhớ và bộ nhớ bandwidth phải được xét cùng nhau.

> **Chuyển mạch:** Trong **chia để trị**, **23. ổn định Partition khó hơn unstable partition** tiếp nhận điểm tựa từ **22. In-place chia để trị vs extra bộ đệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. CDQ chia để trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. ổn định Partition khó hơn unstable partition

Quicksort-style in-place partition thường không ổn định. Nếu hợp đồng đầu ra yêu cầu tính ổn định, kết hợp/partition chiến lược (strategy / 전략) phức tạp hơn hoặc cần extra bộ nhớ.

Một yêu cầu như “giữ thứ tự (order / 순서) của equal các khóa” có thể thay đổi cách triển khai landscape dù asymptotic thời gian (time / 시간) tương tự.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **24. CDQ chia để trị** tiếp nhận điểm tựa từ **23. ổn định Partition khó hơn unstable partition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Divide-and-Conquer DP tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. CDQ chia để trị

Trong các bài toán ngoại tuyến, đệ quy có thể chia theo một chiều hoặc theo thứ tự thời gian, còn Fenwick cây (tree / 트리) hoặc Segment cây (tree / 트리) xử lý một chiều khác.

CDQ thường xuất hiện trong dominance counting hoặc ngoại tuyến các truy vấn. Mô hình tư duy:

```text
recursion cố định order ở dimension A
combine đếm cross-half contributions bằng data structure trên dimension B
```

Divide-and-conquer ở đây không còn là “split mảng rồi sắp xếp trộn” đơn giản, mà là khung làm việc để xử lý cross interactions có cấu trúc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **25. Divide-and-Conquer DP tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **24. CDQ chia để trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Parallel prefix và quét liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Divide-and-Conquer DP tối ưu hóa (optimization / 최적화)

công thức truy hồi dạng:

\[
dp[k][i]=\min_{j<i}(dp[k-1][j]+C(j,i))
\]

naive có thể `O(KN²)`.

Nếu optimal split indices có monotonicity:

\[
opt[i]\le opt[i+1]
\]

ta có thể compute midpoint `i`, tìm best `j` trong narrowed interval, rồi recurse trái/phải với ứng viên bounds tương ứng.

Kỹ thuật này dùng chia để trị để giảm **miền tìm kiếm của bước chuyển**, không phải để tách bài toán gốc thành hai nửa độc lập.

> **Chuyển mạch:** Trong **chia để trị**, sau nội dung của **25. Divide-and-Conquer DP tối ưu hóa (optimization / 최적화)**, **26. Parallel prefix và quét liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **27. cây contraction và recursive separators** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Parallel prefix và quét liên kết (connection / 연결)

Một số prefix các thao tác có thể được xây bằng upsweep/downsweep cây, nhìn như divide-and-conquer reduction rồi distribute các kết quả.

Tính kết hợp của phép toán cho phép ghép các kết quả tổng hợp từng phần. Đây là mối liên hệ giữa tính chất đại số và khả năng phân rã để xử lý song song.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **27. cây contraction và recursive separators** tiếp nhận điểm tựa từ **26. Parallel prefix và quét liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. hình học (geometry / 기하학) và spatial partitioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. cây contraction và recursive separators

đồ thị/cây các thuật toán nâng cao đôi khi dùng separators: loại một small separator chia bài toán (problem / 문제) thành regions nhỏ hơn, solve regions rồi kết hợp.

Centroid decomposition trên cây là ví dụ: chọn centroid chia cây thành các thành phần không lớn hơn n/2, recurse từng thành phần. độ sâu `O(log n)` nhờ kích thước (size / 크기) giảm theo tỷ lệ.

Đây là chia để trị trên topology thay vì mảng interval.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **28. hình học (geometry / 기하학) và spatial partitioning** tiếp nhận điểm tựa từ **27. cây contraction và recursive separators** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. dạng lỗi: kết hợp quá đắt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. hình học (geometry / 기하학) và spatial partitioning

Việc xây dựng KD-tree, quadtree/octree và BSP cũng mang tinh thần chia để trị: chia không gian thành các vùng rồi đệ quy theo từng vùng.

Hiệu quả phụ thuộc vào mức cân bằng của phép phân hoạch và hình học của truy vấn. Một “điểm giữa” tốt trong không gian tọa độ không nhất thiết chia các điểm thành hai nhóm có số lượng bằng nhau.

> **Chuyển mạch:** Trong **chia để trị**, **29. dạng lỗi: kết hợp quá đắt** tiếp nhận điểm tựa từ **28. hình học (geometry / 기하학) và spatial partitioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. dạng lỗi: hidden overlap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. dạng lỗi: kết hợp quá đắt

Nếu có 2 halves nhưng kết hợp `O(n²)` mỗi tầng:

\[
T(n)=2T(n/2)+O(n^2)=O(n^2)
\]

Divide không tự cứu độ phức tạp (complexity / 복잡도). Đôi khi kết hợp term dominate hoàn toàn.

Khi thiết kế, hãy tính kết hợp ngay từ đầu thay vì chỉ vui vì “đã chia bài toán (problem / 문제) làm đôi”.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **30. dạng lỗi: hidden overlap** tiếp nhận điểm tựa từ **29. dạng lỗi: kết hợp quá đắt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. dạng lỗi: bad partition adversarially** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. dạng lỗi: hidden overlap

Hai subproblems nhìn khác đầu vào chỉ mục (index / 인덱스) nhưng thực chất tính lại cùng trạng thái nội bộ. Nếu overlap lớn, cây đệ quy phình exponential.

Memoization có thể biến cây thành DAG computation.

Đây là lý do phân biệt **subproblem định danh (identity / 식별자)** chứ không chỉ argument cú pháp (syntax / 문법).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **31. dạng lỗi: bad partition adversarially** tiếp nhận điểm tựa từ **30. dạng lỗi: hidden overlap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. kiểm thử chia để trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. dạng lỗi: bad partition adversarially

Quicksort pivot đầu tiên trên already-mảng đã sắp xếp có thể tạo trường hợp xấu nhất nếu không có randomization/hybrid fallback.

Trong hệ thống thực tế, thuật toán phải xét đối kháng đầu vào nếu API công khai (public / 공개). Randomization, median sampling hoặc introspective fallback giúp kiểm soát tail.

> **Chuyển mạch:** Trong **chia để trị**, **32. kiểm thử chia để trị** tiếp nhận điểm tựa từ **31. dạng lỗi: bad partition adversarially** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. tính đúng đắn chứng minh mẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. kiểm thử chia để trị

Các kiểm thử (test / 테스트) nên nhắm vào các ranh giới nơi recursion chia:

```text
n = 0,1,2
odd/even lengths
power-of-two và không power-of-two
all equal
already sorted/reverse
extreme imbalance
large duplicate groups
```

Kiểm thử vi sai (kiểm thử vi sai) với thuật toán vét cạn hoặc thuật toán tham chiếu trên đầu vào nhỏ rất hiệu quả cho closest pair, selection hoặc recursive transforms.

> **Chuyển mạch:** Ở chặng này của **chia để trị**, **33. tính đúng đắn chứng minh mẫu** tiếp nhận điểm tựa từ **32. kiểm thử chia để trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Trong hệ thống thực tế, checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. tính đúng đắn chứng minh mẫu

Một chứng minh điển hình dùng quy nạp mạnh theo kích thước đầu vào:

1. trường hợp cơ sở đúng;
2. assume thuật toán đúng cho mọi kích thước (size / 크기) nhỏ hơn `n`;
3. prove divide tạo hợp lệ subproblems nhỏ hơn;
4. recursive các kết quả đúng theo quy nạp hypothesis;
5. prove kết hợp biến correct subresults thành correct whole kết quả.

Phần khó nhất thường là step 5 — kết hợp bất biến/theorem.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **chia để trị**, **34. Trong hệ thống thực tế, checklist** tiếp nhận điểm tựa từ **33. tính đúng đắn chứng minh mẫu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Trong hệ thống thực tế, checklist

Khi dùng chia để trị, hãy hỏi:

```text
split có balanced đủ không?
subproblems có overlap không?
combine cost bao nhiêu?
recursion depth bao nhiêu?
input mutation có cho phép không?
stability có cần không?
parallelization có đủ coarse-grained không?
cache locality tốt hay xấu?
pathological input có fallback không?
```

> **Chuyển mạch:** Trong **chia để trị**, **Mô hình tư duy** gom các mảnh từ **34. Trong hệ thống thực tế, checklist** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> chia để trị biến một toàn cục bài toán (problem / 문제) thành một **cây đệ quy of smaller obligations**. hiệu năng được quyết định bởi ba thứ: hệ số phân nhánh, tốc độ giảm kích thước (size / 크기) và kết hợp chi phí.

Nếu subproblems độc lập, decomposition mở đường cho recursion, parallelism và tính cục bộ bộ nhớ đệm. Nếu overlap mạnh, nghĩ DP. Nếu kết hợp hoặc partition xấu, khung làm việc không tự mang lại speedup.

Xem thêm: [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Selection/Top-K](./06_selection_and_top_k.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
