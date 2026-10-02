# hợp nhất-tìm kiếm / hợp nhất tập rời nhau

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Hai thao tác cốt lõi** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Mô hình tư duy** để rút ra mô hình chung và giới hạn. Mạch này nối union-find với components, connectivity và amortized complexity, để thao tác hợp nhất được đọc qua cấu trúc rừng.

**Tập hợp rời nhau (Disjoint Set Union / 서로소 집합)**

hợp nhất-tìm kiếm, thường gọi là **hợp nhất tập rời nhau (DSU / 서로소 집합 자료구조)**, được thiết kế cho một câu hỏi rất hẹp nhưng xuất hiện rất nhiều:

> Khi các phần tử liên tục được hợp nhất thành các nhóm, làm sao biết nhanh hai phần tử có đang thuộc cùng một nhóm hay không?

DSU không cố lưu toàn bộ topology của đồ thị. Nó không biết đường đi giữa hai các đỉnh, không biết degree, không biết đường đi ngắn nhất (shortest path). Nó chỉ duy trì **thành phần định danh (identity / 식별자)**.

## Hai thao tác cốt lõi

`find(x)` trả representative của thành phần chứa `x`.

`union(a,b)` hợp nhất hai các thành phần nếu chúng khác nhau.

Nếu:

```text
find(a) == find(b)
```

thì `a` và `b` đã connected theo quan hệ merge hiện tại.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Mô hình tư duy** gom các mảnh từ **Hai thao tác cốt lõi** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **cách biểu diễn (representation / 표현) bằng nút cha forest** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> DSU nén một partition của tập phần tử thành một forest. Mỗi cây đại diện một thành phần; nút gốc chỉ là **identifier nội bộ**, không phải đỉnh “quan trọng nhất”.

Điểm mạnh của DSU đến từ việc nó từ chối lưu thông tin không cần thiết. Nếu bài toán chỉ hỏi connectivity dưới thao tác merge, đường đi chi tiết là overhead.

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **cách biểu diễn (representation / 표현) bằng nút cha forest** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Cách đơn giản union có vấn đề gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cách biểu diễn (representation / 표현) bằng nút cha forest

Ban đầu mỗi phần tử là một set riêng:

```text
parent[x] = x
```

Khi merge hai sets, ta nối nút gốc của một cây vào nút gốc của cây kia.

Ví dụ:

```text
0   1   2   3
```

sau `union(0,1)` và `union(2,3)`:

```text
0      2
|      |
1      3
```

sau `union(0,2)`:

```text
    0
   / \
  1   2
      |
      3
```

Tất cả các nút trong cùng cây có cùng representative nút gốc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Cách đơn giản union có vấn đề gì?** tiếp nhận điểm tựa từ **cách biểu diễn (representation / 표현) bằng nút cha forest** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Union by kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cách đơn giản union có vấn đề gì?

Nếu luôn gắn nút gốc mới vào nút gốc cũ một cách tùy ý, có thể tạo chuỗi (chain / 사슬):

```text
0 <- 1 <- 2 <- 3 <- 4 <- ...
```

Khi đó `find(n-1)` là `O(n)`.

DSU hiệu quả nhờ hai tối ưu hóa (optimization / 최적화) phối hợp:

1. **union by kích thước (size / 크기)/rank (크기/랭크 기준 합치기)**;
2. **đường đi compression (경로 압축)**.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Union by kích thước (size / 크기)** tiếp nhận điểm tựa từ **Cách đơn giản union có vấn đề gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **đường đi compression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Union by kích thước (size / 크기)

Khi merge hai các thành phần, gắn nút gốc của cây nhỏ hơn dưới nút gốc của cây lớn hơn.

```java
boolean union(int a, int b) {
    int ra = find(a);
    int rb = find(b);

    if (ra == rb) return false;

    if (size[ra] < size[rb]) {
        int t = ra;
        ra = rb;
        rb = t;
    }

    parent[rb] = ra;
    size[ra] += size[rb];
    return true;
}
```

### Tại sao kích thước (size / 크기) heuristic giúp chiều cao nhỏ?

Mỗi khi độ sâu của một nút tăng 1 do cây của nó bị gắn dưới cây khác, thành phần mới ít nhất gấp đôi thành phần cũ nếu luôn gắn smaller vào larger.

Một nút không thể trải qua quá `log2 n` lần mà “kích thước thành phần ít nhất tăng gấp đôi”. Vì vậy chỉ riêng union-by-size đã chặn chiều cao cây ở `O(log n)`.

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **đường đi compression** tiếp nhận điểm tựa từ **Union by kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Iterative find trong C** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## đường đi compression

`find(x)` không chỉ đi lên nút gốc; nó còn sửa nút cha của các nút trên đường đi để những lần tìm sau ngắn hơn.

Recursive Java:

```java
int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]);
    }
    return parent[x];
}
```

Nếu đường đi ban đầu:

```text
7 -> 5 -> 3 -> 0
```

sau `find(7)` có thể thành:

```text
7 -> 0
5 -> 0
3 -> 0
```

Một thao tác hiện tại trả thêm maintenance chi phí để tương lai các thao tác rẻ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Iterative find trong C** tiếp nhận điểm tựa từ **đường đi compression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **O(alpha(n)) thực sự nghĩa là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Iterative find trong C

Recursion không bắt buộc:

```c
int dsu_find(DSU *d, int x) {
    int root = x;

    while (d->parent[root] != root) {
        root = d->parent[root];
    }

    while (d->parent[x] != x) {
        int p = d->parent[x];
        d->parent[x] = root;
        x = p;
    }

    return root;
}
```

Pass đầu tìm nút gốc; pass sau compress đường đi. Iterative form tránh recursion độ sâu concern và làm sự thay đổi dữ liệu luồng (flow / 흐름) rõ ràng.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **O(alpha(n)) thực sự nghĩa là gì?** tiếp nhận điểm tựa từ **Iterative find trong C** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **phân tích khấu hao ở đây đến từ đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `O(alpha(n))` thực sự nghĩa là gì?

Kết hợp union-by-size/rank với đường đi compression cho độ phức tạp khấu hao:

\[
O(\alpha(n))
\]

mỗi thao tác, trong đó `\alpha` là **inverse Ackermann hàm**.

Không cần học chi tiết Ackermann hàm để dùng DSU. Điều cần hiểu là `alpha(n)` tăng cực chậm; với mọi `n` thực tế, nó là một hằng số rất nhỏ.

Nhưng nói “DSU là O(1)” về mặt lý thuyết là không chính xác. Cách nói tốt hơn:

> amortized gần constant trong mọi kích thước đầu vào thực tế, với bound `O(alpha(n))`.

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **phân tích khấu hao ở đây đến từ đâu?** tiếp nhận điểm tựa từ **O(alpha(n)) thực sự nghĩa là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DSU trong Kruskal MST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## phân tích khấu hao ở đây đến từ đâu?

Một `find` riêng lẻ vẫn có thể đi qua nhiều các nút. Nhưng mỗi lần đi qua đường đi dài, compression làm cấu trúc (structure / 구조) phẳng hơn. Ta không thể liên tục trả chi phí lớn trên cùng các nút mà không thay đổi tương lai shape.

Đây là cùng family lập luận (reasoning / 추론) với mảng động resize: một thao tác đắt được “trả” bởi việc làm nhiều thao tác tương lai rẻ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **DSU trong Kruskal MST** tiếp nhận điểm tựa từ **phân tích khấu hao ở đây đến từ đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **phát hiện chu trình khi add undirected các cạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DSU trong Kruskal MST

Kruskal sort các cạnh theo trọng số rồi xét từng cạnh `(u,v)`.

Nếu:

```text
find(u) != find(v)
```

cạnh nối hai các thành phần khác nhau nên không tạo chu trình; ta nhận cạnh và `union(u,v)`.

Nếu representatives giống nhau, cạnh đóng chu trình và bỏ qua.

DSU ở đây không tìm chu trình bằng traversal. Nó chỉ trả lời “hai endpoints đã connected bởi các cạnh trước chưa?”.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **phát hiện chu trình khi add undirected các cạnh** tiếp nhận điểm tựa từ **DSU trong Kruskal MST** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Connected các thành phần dưới merge-only các cập nhật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## phát hiện chu trình khi add undirected các cạnh

Trong đồ thị ban đầu rỗng, xử lý các cạnh trực tuyến:

```text
for edge (u,v):
    if find(u) == find(v):
        adding edge creates a cycle
    else:
        union(u,v)
```

Lưu ý đây là lập luận (reasoning / 추론) cho **undirected** connectivity. Directed phát hiện chu trình không thể dùng DSU theo cách này vì directed reachability không phải quan hệ tương đương đơn giản.

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Connected các thành phần dưới merge-only các cập nhật** tiếp nhận điểm tựa từ **phát hiện chu trình khi add undirected các cạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **thành phần siêu dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Connected các thành phần dưới merge-only các cập nhật

Nếu các đỉnh ban đầu tách rời và các cạnh chỉ được thêm, DSU là cấu trúc (structure / 구조) rất tự nhiên.

Maintain thêm:

```text
componentCount = n
```

mỗi successful union:

```text
componentCount--
```

Ta có thể truy vấn số các thành phần `O(1)`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Connected các thành phần dưới merge-only các cập nhật** nêu điều cần giải thích; **thành phần siêu dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **ngoại tuyến threshold các truy vấn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## thành phần siêu dữ liệu

nút gốc có thể lưu siêu dữ liệu của toàn thành phần:

```text
size
sum
minimum id
maximum value
aggregate statistics
```

Khi merge two các nút gốc, kết hợp siêu dữ liệu.

Ví dụ:

```java
size[ra] += size[rb];
sum[ra] += sum[rb];
```

Nguyên tắc là siêu dữ liệu phải thuộc representative hiện tại; không nên đọc `size[x]` cho non-root nếu cách triển khai không giữ nó cập nhật.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **thành phần siêu dữ liệu** nêu điều cần giải thích; **ngoại tuyến threshold các truy vấn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kruskal Reconstruction cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ngoại tuyến threshold các truy vấn

Một mẫu cực mạnh là sort các sự kiện theo threshold.

Ví dụ: có roads `(u,v,w)` và các truy vấn:

> Với chỉ roads có chi phí `<= X`, `a` và `b` có connected không?

Ta sắp xếp các cạnh theo `w`, sắp xếp các truy vấn theo `X`, rồi tăng dần ngưỡng:

```text
while nextRoad.weight <= query.X:
    union(nextRoad.u, nextRoad.v)

answer = find(a) == find(b)
```

Mỗi cạnh chỉ được add một lần. Đây là ví dụ của **ngoại tuyến thuật toán**: biết trước toàn bộ các truy vấn cho phép reorder xử lý để dùng DSU hiệu quả.

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Kruskal Reconstruction cây** tiếp nhận điểm tựa từ **ngoại tuyến threshold các truy vấn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DSU với parity / bipartite các ràng buộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kruskal Reconstruction cây

Một extension thú vị: mỗi successful union có thể tạo một nội bộ nút mới đại diện thời điểm/trọng số mà hai các thành phần hợp nhất. các nút lá là original các đỉnh; nội bộ nút trọng số là cạnh threshold.

Sau khi xây dựng, các truy vấn như “minimum threshold để u và v connected” có thể biến thành LCA trên reconstruction cây.

Insight này cho thấy DSU không chỉ là endpoint thuật toán; nó còn có thể xây một hierarchy từ merge lịch sử.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **DSU với parity / bipartite các ràng buộc** tiếp nhận điểm tựa từ **Kruskal Reconstruction cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weighted / Potential DSU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DSU với parity / bipartite các ràng buộc

Ta có thể lưu thêm quan hệ (relation / 관계) từ nút tới nút cha. Ví dụ `parity[x]` biểu diễn màu của `x` XOR màu nút cha.

Khi `find(x)` compress đường đi, phải compose parity dọc đường đi.

Cấu trúc (structure / 구조) này có thể hỗ trợ (support / 지원) các ràng buộc kiểu:

```text
u và v phải khác màu
```

và detect contradiction khi thêm các cạnh trong trực tuyến bipartiteness variants.

Nguyên tắc tổng quát: DSU có thể duy trì **relative potential** giữa nút và representative nếu quan hệ (relation / 관계) compose được.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Weighted / Potential DSU** tiếp nhận điểm tựa từ **DSU với parity / bipartite các ràng buộc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tại sao DSU chuẩn không hỗ trợ xóa/tách tốt?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weighted / Potential DSU

Một biến thể lưu:

\[
potential[x] = giá trị(x) - giá trị(nút cha(x))
\]

hoặc một group-like quan hệ (relation / 관계) tương tự. Khi union hai các thành phần với ràng buộc giữa `a` và `b`, ta tính potential của nút gốc mới sao cho quan hệ (relation / 관계) vẫn đúng.

Ứng dụng gồm difference các ràng buộc đơn giản, coordinate quan hệ (relation / 관계) và parity.

Đây là bước nâng cao: đường đi compression không chỉ đổi nút cha; mọi siêu dữ liệu relative-to-parent phải được cập nhật tương ứng.

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Tại sao DSU chuẩn không hỗ trợ xóa/tách tốt?** tiếp nhận điểm tựa từ **Weighted / Potential DSU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quay lui (rollback / 롤백) DSU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao DSU chuẩn không hỗ trợ xóa/tách tốt?

DSU được tối ưu cho **monotonic merge**. Sau đường đi compression, nhiều các nút có thể trỏ thẳng tới nút gốc; original cây cấu trúc (structure / 구조) gần như bị mất.

Nếu xóa một cạnh đã từng làm các thành phần merge, DSU không biết thành phần phải split thành những phần nào vì nó chưa bao giờ lưu đủ đồ thị topology.

Đây không phải thiếu tính năng (feature / 기능) nhỏ; đó là consequence trực tiếp của thông tin compression.

> DSU nhanh vì nó quên đường đi cấu trúc (structure / 구조). Muốn hỗ trợ (support / 지원) deletion, bạn cần giữ thêm thông tin hoặc đổi thuật toán.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Quay lui (rollback / 롤백) DSU** tiếp nhận điểm tựa từ **Tại sao DSU chuẩn không hỗ trợ xóa/tách tốt?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **động connectivity ngoại tuyến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quay lui (rollback / 롤백) DSU

Nếu cần undo unions trong ngoại tuyến thuật toán, tiêu chuẩn (standard / 표준) đường đi compression gây khó vì một `find` có thể mutate nhiều các nút cha.

**quay lui (rollback / 롤백) DSU (롤백 DSU)** thường:

- dùng union-by-size;
- không path-compress;
- mỗi union ghi thay đổi vào ngăn xếp (stack / 스택);
- quay lui (rollback / 롤백) pop ngăn xếp (stack / 스택) để restore nút cha/kích thước (size / 크기).

Union/find khi đó thường `O(log n)` trường hợp xấu nhất do union-by-size chiều cao bound, nhưng undo trở nên đơn giản.

### Thay đổi (change / 변경) ngăn xếp (stack / 스택) idea

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
union(ra, rb):
    record (rb, oldParent, ra, oldSizeRa)
    parent[rb] = ra
    size[ra] += size[rb]

rollback():
    restore recorded values
```

Tối ưu hóa (optimization / 최적화) không tồn tại trong chân không: đường đi compression tốt cho forward các truy vấn nhưng xung đột với reversibility.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **động connectivity ngoại tuyến** tiếp nhận điểm tựa từ **Quay lui (rollback / 롤백) DSU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Persistent / Partially Persistent DSU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## động connectivity ngoại tuyến

Nếu các cạnh có cả add và remove theo thời gian (time / 시간), có thể xử lý ngoại tuyến bằng cây đoạn (Segment Tree) over thời gian (time / 시간) + quay lui (rollback / 롤백) DSU.

Mỗi cạnh tồn tại trên một interval thời gian `[l,r)`. Ta add cạnh vào các segment-tree các nút phủ interval đó. DFS cây đoạn:

```text
enter node -> apply unions
process children / answer queries
exit node -> rollback
```

Mỗi truy vấn sees đúng tập các cạnh active tại timestamp của nó.

Đây là một example nâng cao của việc kết hợp các cấu trúc dữ liệu: cây đoạn quản thời gian (time / 시간) intervals, quay lui (rollback / 롤백) DSU quản connectivity trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Persistent / Partially Persistent DSU** tiếp nhận điểm tựa từ **động connectivity ngoại tuyến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **gộp nhỏ vào lớn khác DSU thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Persistent / Partially Persistent DSU

Một hướng khác là giữ lịch sử để truy vấn connectivity ở phiên bản (version / 버전) cũ. Có nhiều designs: union cây với timestamps, persistent các mảng, or versioned nút cha relations. Không phải mọi variant hỗ trợ (support / 지원) arbitrary branching các cập nhật; cần xác định persistence mô hình.

Điểm conceptual là DSU có thể được mở rộng theo trục **thời gian (time / 시간)**, nhưng tiêu chuẩn (standard / 표준) cách triển khai chỉ đại diện trạng thái hiện tại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **gộp nhỏ vào lớn khác DSU thế nào?** tiếp nhận điểm tựa từ **Persistent / Partially Persistent DSU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java cách triển khai đầy đủ cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## gộp nhỏ vào lớn khác DSU thế nào?

Một technique khác cũng gọi “merge smaller into larger” là gộp nhỏ vào lớn của sets/maps trên cây. Ví dụ merge color-frequency maps của các nút con vào largest map.

Kỹ thuật này dùng cùng lập luận nhân đôi để chặn số lần một phần tử bị di chuyển ở `O(log n)`, nhưng nó không phải DSU. DSU duy trì định danh của các phân hoạch, còn gộp nhỏ vào lớn có thể duy trì các tập hợp dữ liệu giàu thông tin hơn.

Cùng chứng minh mẫu không đồng nghĩa cùng cấu trúc dữ liệu.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Java cách triển khai đầy đủ cơ bản** tiếp nhận điểm tựa từ **gộp nhỏ vào lớn khác DSU thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **JavaScript cách triển khai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java cách triển khai đầy đủ cơ bản

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```java
final class DSU {
    private final int[] parent;
    private final int[] size;
    private int components;

    DSU(int n) {
        parent = new int[n];
        size = new int[n];
        components = n;

        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int find(int x) {
        int root = x;
        while (parent[root] != root) {
            root = parent[root];
        }

        while (parent[x] != x) {
            int p = parent[x];
            parent[x] = root;
            x = p;
        }
        return root;
    }

    boolean union(int a, int b) {
        int ra = find(a);
        int rb = find(b);
        if (ra == rb) return false;

        if (size[ra] < size[rb]) {
            int t = ra;
            ra = rb;
            rb = t;
        }

        parent[rb] = ra;
        size[ra] += size[rb];
        components--;
        return true;
    }

    boolean connected(int a, int b) {
        return find(a) == find(b);
    }

    int componentSize(int x) {
        return size[find(x)];
    }

    int componentCount() {
        return components;
    }
}
```

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **JavaScript cách triển khai** tiếp nhận điểm tựa từ **Java cách triển khai đầy đủ cơ bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## JavaScript cách triển khai

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```js
class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.size = Array(n).fill(1);
    this.components = n;
  }

  find(x) {
    let root = x;
    while (this.parent[root] !== root) {
      root = this.parent[root];
    }

    while (this.parent[x] !== x) {
      const p = this.parent[x];
      this.parent[x] = root;
      x = p;
    }
    return root;
  }

  union(a, b) {
    let ra = this.find(a);
    let rb = this.find(b);
    if (ra === rb) return false;

    if (this.size[ra] < this.size[rb]) [ra, rb] = [rb, ra];

    this.parent[rb] = ra;
    this.size[ra] += this.size[rb];
    this.components--;
    return true;
  }
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **JavaScript cách triển khai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử DSU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“Representative là smallest phần tử.”** Không trừ khi bạn chủ động giữ quy tắc đó. nút gốc chỉ là cách triển khai định danh (identity / 식별자).

**“DSU cho biết đường đi giữa hai các đỉnh.”** Không. Nó chỉ biết cùng thành phần hay không.

**“DSU dùng được cho directed reachability.”** Không theo tiêu chuẩn (standard / 표준) formulation; directed connectivity không phải quan hệ tương đương đơn giản.

**“đường đi compression luôn nên bật.”** Không nếu cần quay lui (rollback / 롤백)/undo hoặc một persistence thiết kế (design / 설계) cụ thể.

**“`size[x]` luôn là thành phần kích thước (size / 크기).”** Thường chỉ đúng ở nút gốc. Hãy dùng `size[find(x)]`.

**“Gần O(1) nghĩa là trường hợp xấu nhất O(1).”** Không. Bound chuẩn là amortized `O(alpha(n))` với hai optimizations.

> **Chuyển mạch:** Trong **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **kiểm thử DSU** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết (connection / 연결) với các lớp tương đương** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử DSU

Một kiểm thử (test / 테스트) tốt nên tạo ngẫu nhiên union/truy vấn chuỗi (sequence / 시퀀스) và so sánh với tham chiếu đồ thị connectivity trên `n` nhỏ.

các bất biến nên kiểm:

```text
parent[root] == root
size[root] bằng số elements thực trong component
find(x) idempotent: find(find(x)) == find(x)
components giảm đúng một khi union successful
connected là equivalence relation
```

quan hệ tương đương nghĩa là reflexive, symmetric và transitive. Đây cũng là lý do DSU hợp với partition problems.

> **Chuyển mạch:** Ở chặng này của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Liên kết (connection / 연결) với các lớp tương đương** tiếp nhận điểm tựa từ **kiểm thử DSU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy mở rộng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) với các lớp tương đương

Nếu quan hệ (relation / 관계) “cùng nhóm” thực sự là quan hệ tương đương, DSU là cách biểu diễn tự nhiên:

```text
x ~ x                     reflexive
x ~ y => y ~ x            symmetric
x ~ y và y ~ z => x ~ z   transitive
```

Connected các thành phần của đồ thị vô hướng (undirected graph), account merging theo định danh dùng chung, synonym groups, clustering dưới merge các quy tắc đều có thể được nhìn như các lớp tương đương.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **hợp nhất-tìm kiếm / hợp nhất tập rời nhau**, **Mô hình tư duy mở rộng** gom các mảnh từ **Liên kết (connection / 연결) với các lớp tương đương** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy mở rộng

> DSU là một cấu trúc (structure / 구조) tối ưu cho **monotonic equivalence merging**. Nó đổi đường đi/topology detail lấy thành phần định danh (identity / 식별자) cực rẻ.

Khi gặp bài toán connectivity, hãy hỏi: các cạnh chỉ được thêm hay còn bị xóa? truy vấn cần đường đi hay chỉ yes/no cùng thành phần? Có threshold ngoại tuyến không? Có siêu dữ liệu per thành phần không? Có cần quay lui (rollback / 롤백) không?

Nếu câu trả lời là “chỉ merge và hỏi cùng nhóm”, DSU thường là sự trừu tượng (abstraction) đúng hơn BFS/DFS lặp lại.

> **Bàn giao:** Sau **Mô hình tư duy mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
