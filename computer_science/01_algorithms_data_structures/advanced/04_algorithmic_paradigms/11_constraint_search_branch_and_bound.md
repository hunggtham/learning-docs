# Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. tìm kiếm (search / 검색) cây (tree / 트리) chỉ là biểu diễn của không gian nghiệm** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. ràng buộc (constraint / 제약조건) Satisfaction bài toán (problem / 문제)** để chuyển câu hỏi ấy thành điều kiện phải giữ. Mạch này nối constraint search với branch-and-bound, pruning và feasibility, để không gian nghiệm được thu hẹp bằng ràng buộc.

**ràng buộc (constraint / 제약조건) tìm kiếm (search / 검색) & Branch-and-Bound / 제약 탐색과 분기 한정법**

Backtracking cơ bản thử một lựa chọn, đi sâu, rồi hoàn tác. Nhưng trong các bài tổ hợp thực tế, khác biệt giữa một bộ giải chạy được và một bộ giải bất khả thi thường nằm ở **mô hình trạng thái, propagation, thứ tự phân nhánh và cận** chứ không phải ở cú pháp đệ quy.

Chương này tập trung vào cách biến cây tìm kiếm thô thành một hệ thống suy luận có chủ đích.

## 1. tìm kiếm (search / 검색) cây (tree / 트리) chỉ là biểu diễn của không gian nghiệm

Mỗi nút (node / 노드) trong cây tìm kiếm đại diện một **trạng thái từng phần (partial state)**. Mỗi cạnh là một quyết định.

Ví dụ trong Sudoku:

```text
state = các ô đã gán + miền giá trị còn lại của các ô chưa gán
branch = chọn một giá trị cho một ô
```

Trong TSP:

```text
state = đường đi từng phần + thành phố chưa thăm
branch = chọn thành phố tiếp theo
```

Điểm quan trọng là cây tìm kiếm không tồn tại sẵn; nó được sinh từ **cách ta chọn biến trạng thái và quyết định**. Một mô hình khác có thể làm branching factor nhỏ đi rất nhiều.

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **2. ràng buộc (constraint / 제약조건) Satisfaction bài toán (problem / 문제)** tiếp nhận điểm tựa từ **1. tìm kiếm (search / 검색) cây (tree / 트리) chỉ là biểu diễn của không gian nghiệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Forward Checking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. ràng buộc (constraint / 제약조건) Satisfaction bài toán (problem / 문제)

Một **bài toán thỏa ràng buộc (constraint Satisfaction Problem – CSP)** thường có:

```text
variables
mỗi variable có domain
constraints giữa các variables
```

Mục tiêu có thể chỉ là tìm một phép gán hợp lệ hoặc tối ưu thêm một mục tiêu (objective / 목표).

Sudoku, đồ thị (graph / 그래프) coloring, scheduling, n-queens và nhiều cấu hình (configuration / 구성) bài toán (problem / 문제) đều có thể nhìn theo mô hình này.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **3. Forward Checking** tiếp nhận điểm tựa từ **2. ràng buộc (constraint / 제약조건) Satisfaction bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. ràng buộc (constraint / 제약조건) Propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Forward Checking

Khi gán một biến, đừng chờ tới khi sâu hơn mới phát hiện xung đột. Hãy cập nhật miền của các biến liên quan ngay lập tức.

Nếu một biến chưa gán bị mất hết lĩnh vực (domain / 도메인), branch hiện tại chắc chắn thất bại và có thể quay lui ngay.

Đây là **forward checking**.

Nó biến kiểm tra từ “đến cuối mới biết sai” thành “phát hiện contradiction sớm”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **4. ràng buộc (constraint / 제약조건) Propagation** tiếp nhận điểm tựa từ **3. Forward Checking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Arc Consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. ràng buộc (constraint / 제약조건) Propagation

Forward checking chỉ là mức đơn giản. **ràng buộc (constraint / 제약조건) propagation** lặp lại việc suy ra hậu quả của các lĩnh vực (domain / 도메인) bị thu hẹp.

Ví dụ nếu một ô Sudoku chỉ còn một ứng viên, ta gán nó; phép gán này lại làm giảm lĩnh vực (domain / 도메인) của các ô cùng hàng/cột/khối; quá trình tiếp tục cho tới khi không còn suy ra mới.

Tìm kiếm (search / 검색) và propagation tạo hai pha:

```text
propagate đến điểm cố định
nếu contradiction -> backtrack
nếu hoàn tất -> solution
nếu chưa -> branch
```

Bộ giải mạnh thường dành nhiều công sức cho propagation để giảm tìm kiếm (search / 검색) cây (tree / 트리).

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **5. Arc Consistency** tiếp nhận điểm tựa từ **4. ràng buộc (constraint / 제약조건) Propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. MRV: chọn biến khó nhất trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Arc Consistency

Với ràng buộc nhị phân giữa hai biến `X` và `Y`, một giá trị `x` trong lĩnh vực (domain / 도메인) của `X` có **hỗ trợ (support / 지원)** nếu tồn tại ít nhất một `y` trong lĩnh vực (domain / 도메인) của `Y` sao cho `(x,y)` thỏa ràng buộc (constraint / 제약조건).

Nếu không có hỗ trợ (support / 지원), `x` có thể bị loại.

Các thuật toán như AC-3 liên tục xử lý các cung bị ảnh hưởng cho tới khi đạt arc consistency hoặc một lĩnh vực (domain / 도메인) rỗng.

Propagation mạnh hơn tốn nhiều chi phí mỗi nút (node / 노드) nhưng có thể giảm mạnh số nút (node / 노드) phải tìm kiếm (search / 검색). Đây là sự đánh đổi (trade-off / 트레이드오프) giống nhiều cấu trúc DSA khác: trả thêm tiền cục bộ để giảm không gian tương lai.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **6. MRV: chọn biến khó nhất trước** tiếp nhận điểm tựa từ **5. Arc Consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Degree Heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. MRV: chọn biến khó nhất trước

**Minimum Remaining Values (MRV)** chọn biến có lĩnh vực (domain / 도메인) nhỏ nhất chưa được gán.

Trực giác là **thất bại (fail / 실패) first**: nếu một branch sắp mâu thuẫn, hãy tìm ra càng sớm càng tốt thay vì xây một cây con lớn rồi mới thất bại.

Trong đồ thị (graph / 그래프) coloring, có thể ưu tiên vertex còn ít màu hợp lệ. Trong Sudoku, chọn ô có ít ứng viên nhất.

MRV không thay đổi tập lời giải; nó chỉ đổi shape của cây tìm kiếm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **7. Degree Heuristic** tiếp nhận điểm tựa từ **6. MRV: chọn biến khó nhất trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Least Constraining giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Degree Heuristic

Nếu nhiều biến có cùng MRV, có thể ưu tiên biến liên quan tới nhiều ràng buộc (constraint / 제약조건) chưa giải quyết nhất.

Biến “ảnh hưởng rộng” có khả năng tạo propagation mạnh hơn.

Một heuristic chọn biến tốt thường cân bằng:

```text
constrained nhất hiện tại
và
có khả năng ràng buộc phần còn lại nhiều nhất
```

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **8. Least Constraining giá trị (value / 값)** tiếp nhận điểm tựa từ **7. Degree Heuristic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Symmetry Breaking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Least Constraining giá trị (value / 값)

Sau khi chọn biến, thứ tự thử giá trị cũng quan trọng.

**Least Constraining giá trị (value / 값) (LCV)** thử giá trị loại ít lựa chọn của các biến khác nhất trước. Ý tưởng là giữ tương lai linh hoạt nếu đang tìm một nghiệm.

Tuy nhiên, nếu mục tiêu là chứng minh không có nghiệm, đôi khi giá trị gây contradiction sớm có thể hữu ích hơn. Heuristic phải phù hợp mục tiêu (objective / 목표).

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **9. Symmetry Breaking** tiếp nhận điểm tựa từ **8. Least Constraining giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. chuẩn gốc (canonical / 정본) trạng thái (state / 상태) và Memoization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Symmetry Breaking

Nhiều cây tìm kiếm chứa các branch khác nhau về biểu diễn nhưng tương đương về ngữ nghĩa.

Ví dụ đồ thị (graph / 그래프) coloring với màu `{red, green, blue}`: đổi tên toàn bộ màu có thể tạo một nghiệm tương đương.

Nếu không phá đối xứng, solver có thể tìm cùng cấu trúc nghiệm nhiều lần dưới các nhãn khác nhau.

Có thể thêm ràng buộc (constraint / 제약조건) như:

```text
vertex đầu tiên luôn dùng màu 0
màu mới chỉ được mở theo thứ tự 0,1,2,...
```

Symmetry breaking không loại nghiệm theo lớp tương đương; nó chọn một đại diện chuẩn gốc (canonical / 정본) cho mỗi lớp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, sau nội dung của **9. Symmetry Breaking**, **10. chuẩn gốc (canonical / 정본) trạng thái (state / 상태) và Memoization** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **11. Branch-and-Bound khác Backtracking thuần túy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. chuẩn gốc (canonical / 정본) trạng thái (state / 상태) và Memoization

Nếu hai lịch sử khác nhau dẫn đến trạng thái tương đương cho tương lai, có thể memoize theo một dạng chuẩn gốc (canonical / 정본).

Ví dụ trong game tìm kiếm (search / 검색), trạng thái bàn cờ có thể canonicalize dưới các phép quay/đối xứng nếu luật chơi đối xứng.

Nhưng canonicalization bản thân có chi phí. Chỉ đáng dùng khi giảm đủ nhiều trạng thái trùng lặp.

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **11. Branch-and-Bound khác Backtracking thuần túy** tiếp nhận điểm tựa từ **10. chuẩn gốc (canonical / 정본) trạng thái (state / 상태) và Memoization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Cận phải optimistic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Branch-and-Bound khác Backtracking thuần túy

Backtracking thường cắt branch khi **không còn khả thi**.

Branch-and-Bound còn cắt khi branch **vẫn khả thi nhưng không thể đánh bại nghiệm tốt nhất đã biết**.

Ta duy trì:

```text
incumbent = nghiệm tốt nhất đã tìm thấy
bound(state) = cận tốt nhất có thể đạt từ state
```

Nếu bài maximize và:

```text
bound(state) <= incumbent
```

thì không cần mở rộng trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **12. Cận phải optimistic** tiếp nhận điểm tựa từ **11. Branch-and-Bound khác Backtracking thuần túy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Knapsack Branch-and-Bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Cận phải optimistic

Một cận dùng để prune phải “lạc quan” theo đúng hướng.

Với bài maximize, upper bound phải ít nhất bằng mọi kết quả thật có thể đạt từ branch. Nếu bound đánh giá thấp, ta có thể cắt nhầm branch chứa optimum.

Với bài minimize, cần lower bound không lớn hơn optimum còn có thể đạt.

Độ chặt của bound quyết định sức mạnh pruning; tính hợp lệ của bound quyết định tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **13. Knapsack Branch-and-Bound** tiếp nhận điểm tựa từ **12. Cận phải optimistic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Relaxation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Knapsack Branch-and-Bound

Trong 0/1 Knapsack, một upper bound phổ biến là cho phép lấy phân số các vật còn lại giống Fractional Knapsack.

Vì phiên bản fractional nới lỏng ràng buộc (constraint / 제약조건) 0/1, giá trị của nó không nhỏ hơn optimum 0/1 thật. Do đó nó là upper bound hợp lệ cho bài maximize.

Nếu upper bound này đã không vượt incumbent, toàn bộ branch có thể bỏ.

Đây là mẫu (pattern / 패턴) rất quan trọng:

> **Giải một bài toán nới lỏng dễ hơn để tạo cận cho bài toán khó hơn.**

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **14. Relaxation** tiếp nhận điểm tựa từ **13. Knapsack Branch-and-Bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Best-First Branch-and-Bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Relaxation

Một **relaxation** bỏ bớt một số ràng buộc (constraint / 제약조건) để tạo bài dễ hơn.

Ví dụ:

```text
0/1 variable -> cho phép liên tục [0,1]
integer program -> linear programming relaxation
TSP -> minimum spanning tree / 1-tree lower bound
```

Vì feasible region của bài nới lỏng lớn hơn, optimum của relaxation tạo cận cho bài gốc theo hướng phù hợp.

Relaxation là cầu nối giữa Branch-and-Bound, LP/ILP và approximation.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **15. Best-First Branch-and-Bound** tiếp nhận điểm tựa từ **14. Relaxation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. DFS, BFS hay Best-First?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Best-First Branch-and-Bound

DFS branch-and-bound dùng ít bộ nhớ và nhanh tìm một nghiệm sâu. Nhưng có thể mở rộng nút (node / 노드) theo cận tốt nhất trước bằng priority hàng đợi (queue / 큐).

```text
frontier ordered by bound
pop state có triển vọng nhất
```

Cách này gần A*: frontier là các partial solutions và key phản ánh tiềm năng tối ưu.

Đổi lại, bộ nhớ có thể rất lớn vì giữ nhiều nút (node / 노드) đang chờ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **16. DFS, BFS hay Best-First?** tiếp nhận điểm tựa từ **15. Best-First Branch-and-Bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Incumbent chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. DFS, BFS hay Best-First?

Không có chiến lược mở rộng duy nhất tốt nhất.

```text
DFS        -> ít memory, incumbent có thể tìm sớm nếu order tốt
BFS        -> hiếm khi phù hợp search tổ hợp lớn
Best-first -> ưu tiên bound tốt, memory cao
```

Nếu incumbent tốt rất quan trọng để prune, ta thường muốn heuristic branch thứ tự (order / 순서) giúp tìm nghiệm chất lượng cao sớm.

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **17. Incumbent chất lượng (quality / 품질)** tiếp nhận điểm tựa từ **16. DFS, BFS hay Best-First?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. TSP: lower bound bằng MST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Incumbent chất lượng (quality / 품질)

Branch-and-bound mạnh khi có nghiệm khả thi tốt từ sớm. Một heuristic greedy có thể tạo incumbent ban đầu rất nhanh.

Sau đó chính xác (exact / 정확한) tìm kiếm (search / 검색) dùng incumbent đó để cắt branch.

Đây là composition hữu ích:

```text
heuristic nhanh -> upper/lower feasible solution
exact search    -> chứng minh không còn nghiệm tốt hơn
```

Heuristic và chính xác (exact / 정확한) thuật toán (algorithm / 알고리즘) không đối lập; chúng có thể hỗ trợ nhau.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **18. TSP: lower bound bằng MST** tiếp nhận điểm tựa từ **17. Incumbent chất lượng (quality / 품질)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Alpha-Beta Pruning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. TSP: lower bound bằng MST

Trong một partial tour, phần còn lại vẫn phải nối các thành phố chưa thăm. Một lower bound đơn giản có thể gồm:

```text
cost đã đi
+ MST của các node chưa thăm
+ chi phí kết nối hiện tại vào phần còn lại
+ chi phí quay về đích
```

Bound càng chặt, tìm kiếm (search / 검색) càng ít. Nhưng tính MST ở mọi nút (node / 노드) cũng đắt.

Ta phải tối ưu cả **bound chất lượng (quality / 품질)** lẫn **bound evaluation chi phí (cost / 비용)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **19. Alpha-Beta Pruning** tiếp nhận điểm tựa từ **18. TSP: lower bound bằng MST** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Move thứ tự (ordering / 순서) trong Alpha-Beta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Alpha-Beta Pruning

Trong minimax game cây (tree / 트리), alpha-beta pruning dùng cận từ các lựa chọn đã xem để loại branch không thể ảnh hưởng kết quả cuối.

`alpha` là giá trị tốt nhất phía maximizing đã bảo đảm; `beta` là giá trị tốt nhất phía minimizing đã bảo đảm.

Khi:

```text
alpha >= beta
```

branch hiện tại không thể thay đổi quyết định của tổ tiên tương ứng.

Đây là branch-and-bound trong game tìm kiếm (search / 검색) dưới dạng hai phía đối kháng.

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **20. Move thứ tự (ordering / 순서) trong Alpha-Beta** tiếp nhận điểm tựa từ **19. Alpha-Beta Pruning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Transposition bảng (table / 테이블)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Move thứ tự (ordering / 순서) trong Alpha-Beta

Alpha-beta cho cùng kết quả minimax bất kể thứ tự move, nhưng hiệu năng phụ thuộc mạnh vào thứ tự.

Nếu xét move tốt trước, alpha/beta chặt sớm và prune nhiều hơn. Iterative deepening, killer move, lịch sử (history / 이력) heuristic hoặc transposition bảng (table / 테이블) giúp cải thiện thứ tự (ordering / 순서).

Đây là ví dụ tính đúng đắn (correctness / 정확성) không đổi nhưng traversal thứ tự (order / 순서) thay đổi độ phức tạp (complexity / 복잡도) thực tế rất lớn.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **21. Transposition bảng (table / 테이블)** tiếp nhận điểm tựa từ **20. Move thứ tự (ordering / 순서) trong Alpha-Beta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Zobrist Hashing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Transposition bảng (table / 테이블)

Trong game cây (tree / 트리), nhiều chuỗi (sequence / 시퀀스) move khác nhau có thể dẫn tới cùng board trạng thái (state / 상태). Nếu coi cấu trúc là cây (tree / 트리), ta tính lại trạng thái (state / 상태) nhiều lần; thực ra không gian là đồ thị (graph / 그래프).

**Transposition bảng (table / 테이블)** dùng bảng băm (hash table / 해시 테이블) lưu kết quả/cận đã biết cho trạng thái (state / 상태).

Entry thường cần:

```text
hash key
depth
evaluation
bound type: exact/lower/upper
best move
```

Không nên bộ nhớ đệm (cache / 캐시) một evaluation nông rồi dùng như kết quả chính xác cho tìm kiếm (search / 검색) sâu hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **22. Zobrist Hashing** tiếp nhận điểm tựa từ **21. Transposition bảng (table / 테이블)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. SAT: tìm kiếm (search / 검색) + Propagation ở quy mô công nghiệp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Zobrist Hashing

Board trạng thái (state / 상태) lớn cần băm (hash / 해시) cập nhật nhanh. Zobrist hashing gán số ngẫu nhiên cho mỗi `(piece, position)` và XOR các giá trị đang hiện diện.

Khi move một quân, băm (hash / 해시) có thể cập nhật bằng vài phép XOR thay vì băm lại toàn board.

Đây là một ví dụ tuyệt vời của **incremental biểu diễn (representation / 표현)**: trạng thái (state / 상태) thay đổi ít thì fingerprint cũng cập nhật ít.

Collision vẫn có xác suất; hệ thống yêu cầu tuyệt đối có thể lưu thêm xác minh (verification / 확인) dữ liệu (data / 데이터).

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **23. SAT: tìm kiếm (search / 검색) + Propagation ở quy mô công nghiệp** tiếp nhận điểm tựa từ **22. Zobrist Hashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Clause học tập (learning / 학습) như Memoization của xung đột (conflict / 충돌)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. SAT: tìm kiếm (search / 검색) + Propagation ở quy mô công nghiệp

SAT solver hiện đại không chỉ là thử True/False đơn giản. Các kỹ thuật quan trọng gồm:

```text
unit propagation
conflict analysis
clause learning
non-chronological backtracking
variable activity heuristic
restart
```

Điểm đáng học cho DSA là tìm kiếm (search / 검색) mạnh thường biến thất bại (failure / 실패) thành **kiến thức mới** để tránh lặp lại cùng vùng sai.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **24. Clause học tập (learning / 학습) như Memoization của xung đột (conflict / 충돌)** tiếp nhận điểm tựa từ **23. SAT: tìm kiếm (search / 검색) + Propagation ở quy mô công nghiệp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Non-Chronological Backtracking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Clause học tập (learning / 학습) như Memoization của xung đột (conflict / 충돌)

Khi một tập quyết định dẫn tới contradiction, solver phân tích xung đột (conflict / 충돌) và học một clause mới biểu diễn “tổ hợp này không được phép lặp lại”.

Đây là dạng tổng quát hơn của memoizing một trạng thái thất bại (fail / 실패). Thay vì nhớ nguyên trạng thái (state / 상태), ta rút ra một ràng buộc (constraint / 제약조건) có thể prune nhiều trạng thái (state / 상태) tương lai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **25. Non-Chronological Backtracking** tiếp nhận điểm tựa từ **24. Clause học tập (learning / 학습) như Memoization của xung đột (conflict / 충돌)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Restart không có nghĩa là mất toàn bộ công việc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Non-Chronological Backtracking

Backtracking cổ điển quay lại đúng một mức. Nhưng nếu xung đột (conflict / 충돌) thực sự do quyết định ở xa hơn, quay từng mức là lãng phí.

Xung đột (conflict / 충돌) phân tích (analysis / 분석) có thể xác định **backjump mức (level / 수준)** và quay thẳng tới quyết định liên quan.

Điều này cho thấy call-stack thứ tự (order / 순서) không nhất thiết phải là lô-gic (logic / 논리) phụ thuộc (dependency / 의존성) thứ tự (order / 순서).

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **26. Restart không có nghĩa là mất toàn bộ công việc** tiếp nhận điểm tựa từ **25. Non-Chronological Backtracking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Iterative Deepening** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Restart không có nghĩa là mất toàn bộ công việc

SAT solver có thể restart tìm kiếm (search / 검색) định kỳ nhưng giữ lại learned clauses. Restart thay đổi đường exploration trong khi tri thức về các vùng thất bại vẫn được bảo toàn.

Đây là ví dụ tìm kiếm (search / 검색) không nhất thiết tiến tuyến tính “đi sâu rồi quay lại”; nó có thể chủ động reset trajectory khi trạng thái (state / 상태) học được đã thay đổi landscape.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **27. Iterative Deepening** tiếp nhận điểm tựa từ **26. Restart không có nghĩa là mất toàn bộ công việc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. IDA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Iterative Deepening

Nếu solution độ sâu (depth / 깊이) chưa biết, DFS giới hạn độ sâu có thể chạy lần lượt với limit tăng dần.

```text
limit 0
limit 1
limit 2
...
```

Dù các tầng nông được duyệt lại, trong cây có branching factor lớn phần lớn nút (node / 노드) nằm ở tầng sâu nhất, nên chi phí lặp lại thường chấp nhận được.

Iterative deepening kết hợp bộ nhớ (memory / 메모리) của DFS với khả năng tìm solution nông giống BFS.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **28. IDA** tiếp nhận điểm tựa từ **27. Iterative Deepening** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Dominance Pruning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. IDA*

IDA* dùng ngưỡng trên `f = g + h` thay vì độ sâu (depth / 깊이). Mỗi iteration DFS chỉ đi qua nút (node / 노드) có `f <= threshold`; ngưỡng sau tăng tới giá trị nhỏ nhất vượt ngưỡng cũ.

Nó giảm bộ nhớ (memory / 메모리) so với A* nhưng có thể lặp lại nhiều công việc.

Heuristic admissible giữ optimality tương tự A* trong mô hình chuẩn.

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **29. Dominance Pruning** tiếp nhận điểm tựa từ **28. IDA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Pareto Frontier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Dominance Pruning

Nếu hai partial states có cùng future-relevant trạng thái (state / 상태) nhưng một trạng thái (state / 상태) không tốt hơn trạng thái (state / 상태) kia về mọi tiêu chí, trạng thái (state / 상태) bị trội có thể bỏ.

Ví dụ cùng `(position, usedResources)` nhưng một đường dẫn (path / 경로) có chi phí (cost / 비용) lớn hơn; trạng thái (state / 상태) chi phí (cost / 비용) lớn hơn không cần tiếp tục.

Đây là nguyên lý **dominance**. DP thường giữ trạng thái tốt nhất; branch-and-bound dùng dominance để prune tìm kiếm (search / 검색) trực tiếp.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **30. Pareto Frontier** tiếp nhận điểm tựa từ **29. Dominance Pruning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Bitmask DP và tìm kiếm (search / 검색): ranh giới không tuyệt đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Pareto Frontier

Nếu có nhiều mục tiêu (objective / 목표)/tài nguyên (resource / 자원), không thể chỉ giữ một trạng thái (state / 상태) tốt nhất bằng scalar.

Ta giữ các trạng thái (state / 상태) không bị trạng thái (state / 상태) nào khác trội trên mọi chiều, tạo **Pareto frontier**.

Ví dụ tuyến (route / 경로) theo `(time, cost)`: tuyến (route / 경로) A nhanh hơn nhưng đắt hơn tuyến (route / 경로) B; cả hai có thể cần giữ.

Frontier có thể tăng lớn, vì vậy multi-objective tìm kiếm (search / 검색) khó hơn đáng kể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **31. Bitmask DP và tìm kiếm (search / 검색): ranh giới không tuyệt đối** tiếp nhận điểm tựa từ **30. Pareto Frontier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Meet-in-the-Middle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Bitmask DP và tìm kiếm (search / 검색): ranh giới không tuyệt đối

Một bài TSP nhỏ có thể giải bằng Held–Karp DP `O(n^2 2^n)` hoặc branch-and-bound.

DP trả chi phí dự đoán được theo trạng thái (state / 상태) không gian (space / 공간). Branch-and-bound có trường hợp xấu rất lớn nhưng có thể chạy nhanh trên instance dễ nhờ pruning.

Lựa chọn phụ thuộc:

```text
n
memory
instance structure
cần worst-case predictability hay average practical speed
```

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **32. Meet-in-the-Middle** tiếp nhận điểm tựa từ **31. Bitmask DP và tìm kiếm (search / 검색): ranh giới không tuyệt đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Branching Factor và Effective tìm kiếm (search / 검색) cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Meet-in-the-Middle

Khi brute force có `2^n`, chia biến thành hai nửa có thể tạo khoảng `2^{n/2}` states mỗi phía rồi ghép.

Subset Sum là ví dụ điển hình.

Đây không phải backtracking thuần túy mà là thay shape của không gian tìm kiếm: đổi một cây sâu thành hai tập trạng thái (state / 상태) vừa phải + bước matching/tìm kiếm (search / 검색).

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **33. Branching Factor và Effective tìm kiếm (search / 검색) cây (tree / 트리)** tiếp nhận điểm tựa từ **32. Meet-in-the-Middle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Kiểm thử tìm kiếm (search / 검색) Solver** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Branching Factor và Effective tìm kiếm (search / 검색) cây (tree / 트리)

Độ phức tạp (complexity / 복잡도) thô thường viết:

\[
O(b^d)
\]

với branching factor `b`, độ sâu (depth / 깊이) `d`. Nhưng propagation và pruning làm `b` hiệu dụng thay đổi theo tầng.

Một heuristic tốt có thể không thay worst-case asymptotic nhưng giảm số nút (node / 노드) thực tế hàng triệu lần.

Vì vậy benchmark tìm kiếm (search / 검색) nên đo:

```text
nodes expanded
prune ratio
propagation operations
bound evaluations
maximum depth
incumbent improvement timeline
```

không chỉ wall-clock thời gian (time / 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **34. Kiểm thử tìm kiếm (search / 검색) Solver** tiếp nhận điểm tựa từ **33. Branching Factor và Effective tìm kiếm (search / 검색) cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Reversible trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Kiểm thử tìm kiếm (search / 검색) Solver

Cần tách ba lớp:

```text
feasibility checker đúng không?
search có bỏ sót solution không?
objective có tối ưu đúng không?
```

Với đầu vào (input / 입력) nhỏ, exhaustive enumeration là oracle rất mạnh.

Có thể sinh random instance nhỏ rồi so:

```text
optimized solver
vs
brute-force solver
```

Nếu solver dùng bound, nên thêm kiểm thử (test / 테스트) kiểm tra bound luôn hợp lệ trên trạng thái (state / 상태) nhỏ bằng cách tính optimum thật của subtree.

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **35. Reversible trạng thái (state / 상태)** tiếp nhận điểm tựa từ **34. Kiểm thử tìm kiếm (search / 검색) Solver** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Persistent trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Reversible trạng thái (state / 상태)

Mutable + undo thường nhanh nhưng dễ bug. Một mẫu (pattern / 패턴) an toàn là ghi log thay đổi:

```text
checkpoint = changeStack.size()
apply changes and push old values
recurse
rollback until checkpoint
```

Quay lui (rollback / 롤백) DSU dùng đúng tư duy này. ràng buộc (constraint / 제약조건) solver cũng có thể quản lĩnh vực (domain / 도메인) updates bằng trail ngăn xếp (stack / 스택).

Điểm mạnh là undo không cần viết lô-gic (logic / 논리) ngược riêng cho từng thao tác (operation / 연산); chỉ restore các giá trị đã ghi.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **36. Persistent trạng thái (state / 상태)** tiếp nhận điểm tựa từ **35. Reversible trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Parallel tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Persistent trạng thái (state / 상태)

Cấu trúc persistent tạo phiên bản mới bằng structural sharing. Nó giảm rủi ro quên undo và phù hợp tìm kiếm (search / 검색) phân nhánh, nhưng có thêm allocation và siêu dữ liệu (metadata / 메타데이터).

Trong functional programming hoặc tìm kiếm (search / 검색) cần giữ nhiều frontier states đồng thời, persistent structures có thể rất tự nhiên.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **37. Parallel tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **36. Persistent trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Anytime thuật toán (algorithm / 알고리즘)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Parallel tìm kiếm (search / 검색)

Các branch độc lập có thể chạy song song, nhưng cần xử lý:

```text
chia work
cập nhật incumbent dùng chung
hủy branch khi bound mới mạnh hơn
tránh duplicate search
reproducibility
```

Công việc (work / 작업) stealing phù hợp khi kích thước subtree khó dự đoán.

Một incumbent tốt tìm được bởi một worker có thể giúp mọi worker khác prune mạnh hơn, vì vậy communication có giá trị.

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **38. Anytime thuật toán (algorithm / 알고리즘)** tiếp nhận điểm tựa từ **37. Parallel tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Khi nào dùng DP, khi nào dùng tìm kiếm (search / 검색)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Anytime thuật toán (algorithm / 알고리즘)

Một số branch-and-bound có thể trả nghiệm khả thi sớm và tiếp tục cải thiện, đồng thời duy trì gap giữa incumbent và bound tốt nhất còn lại.

Nếu bị dừng giữa chừng, hệ thống vẫn có:

```text
một nghiệm khả thi
và
một chứng nhận khoảng cách tới tối ưu
```

Đây là đặc tính cực hữu ích trong scheduling và tối ưu hóa (optimization / 최적화) môi trường vận hành (production / 운영 환경) có thời gian (time / 시간) ngân sách (budget / 예산).

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **39. Khi nào dùng DP, khi nào dùng tìm kiếm (search / 검색)?** tiếp nhận điểm tựa từ **38. Anytime thuật toán (algorithm / 알고리즘)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. quyết định (decision / 결정) Checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Khi nào dùng DP, khi nào dùng tìm kiếm (search / 검색)?

DP phù hợp khi trạng thái (state / 상태) không gian (space / 공간) có thể liệt kê tương đối gọn và nhiều lịch sử hội tụ về cùng trạng thái (state / 상태).

Tìm kiếm (search / 검색) phù hợp khi:

```text
state space lý thuyết lớn
nhưng constraint/bound có thể prune mạnh
cần một solution sớm
instance thực tế có structure thuận lợi
```

Hybrid rất phổ biến: tìm kiếm (search / 검색) bên ngoài, memoization/DP cho subproblem lặp lại bên trong.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **40. quyết định (decision / 결정) Checklist** tiếp nhận điểm tựa từ **39. Khi nào dùng DP, khi nào dùng tìm kiếm (search / 검색)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. quyết định (decision / 결정) Checklist

Trước một bài tổ hợp khó, hãy hỏi:

```text
State tối thiểu là gì?
Có propagation nào làm domain nhỏ trước khi branch không?
Biến nào nên chọn trước để fail sớm?
Có symmetry để canonicalize không?
Có relaxation tạo bound không?
Có incumbent heuristic tốt không?
Có state dominance/memoization không?
Có cần optimality proof hay chỉ feasible solution tốt?
Có time budget để dùng anytime search không?
```

> **Chuyển mạch:** Trong **Tìm kiếm ràng buộc, Branch-and-Bound và chiến lược cắt tỉa**, **Mô hình tư duy** gom các mảnh từ **40. quyết định (decision / 결정) Checklist** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> tìm kiếm (search / 검색) hiệu quả không phải “đệ quy nhanh hơn”. Nó là **quản lý thông tin để càng nhiều nhánh bị chứng minh là không cần mở càng sớm càng tốt**.

Bốn đòn bẩy chính là:

```text
mô hình trạng thái tốt
propagation mạnh
branch ordering tốt
bound/certificate chặt
```

Nếu tìm kiếm (search / 검색) cây (tree / 트리) vẫn quá lớn, đừng chỉ tối ưu mã (code / 코드); hãy hỏi thông tin nào chưa được khai thác để loại cả một vùng trạng thái.

Xem thêm: [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Hard Problems & Approximation](./09_hard_problems_reductions_and_approximation.md), [Greedy nâng cao](./10_greedy_matroids_primal_dual_and_approximation.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [Amortized/Randomized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
