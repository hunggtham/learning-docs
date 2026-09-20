# hợp nhất-tìm kiếm / hợp nhất tập rời nhau
**Tập hợp rời nhau (Disjoint Set Union / 서로소 집합)**

hợp nhất-tìm kiếm, thường gọi là **hợp nhất tập rời nhau (DSU / 서로소 집합 자료구조)**, được thiết kế cho một câu hỏi rất hẹp nhưng xuất hiện rất nhiều:

> Khi các phần tử liên tục được hợp nhất thành các nhóm, làm sao biết nhanh hai phần tử có đang thuộc cùng một nhóm hay không?

DSU không cố lưu toàn bộ topology của đồ thị. Nó không biết đường đi giữa hai các đỉnh, không biết degree, không biết đường đi ngắn nhất (shortest path). Nó chỉ duy trì **thành phần identity**.

## Hai thao tác cốt lõi

`find(x)` trả representative của thành phần chứa `x`.

`union(a,b)` hợp nhất hai các thành phần nếu chúng khác nhau.

Nếu:

```text
find(a) == find(b)
```

thì `a` và `b` đã connected theo quan hệ merge hiện tại.

## Mô hình tư duy

> DSU nén một partition của tập phần tử thành một forest. Mỗi cây đại diện một thành phần; nút gốc chỉ là **identifier nội bộ**, không phải đỉnh “quan trọng nhất”.

Điểm mạnh của DSU đến từ việc nó từ chối lưu thông tin không cần thiết. Nếu bài toán chỉ hỏi connectivity dưới thao tác merge, đường đi chi tiết là overhead.

## cách biểu diễn (representation) bằng nút cha forest

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

## Cách đơn giản union có vấn đề gì?

Nếu luôn gắn nút gốc mới vào nút gốc cũ một cách tùy ý, có thể tạo chain:

```text
0 <- 1 <- 2 <- 3 <- 4 <- ...
```

Khi đó `find(n-1)` là `O(n)`.

DSU hiệu quả nhờ hai optimization phối hợp:

1. **union by size/rank (크기/랭크 기준 합치기)**;
2. **đường đi compression (경로 압축)**.

## Union by size

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

### Tại sao size heuristic giúp chiều cao nhỏ?

Mỗi khi độ sâu của một nút tăng 1 do cây của nó bị gắn dưới cây khác, thành phần mới ít nhất gấp đôi thành phần cũ nếu luôn gắn smaller vào larger.

Một nút không thể trải qua quá `log2 n` lần mà “kích thước thành phần ít nhất tăng gấp đôi”. Vì vậy chỉ riêng union-by-size đã chặn chiều cao cây ở `O(log n)`.

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

Pass đầu tìm nút gốc; pass sau compress đường đi. Iterative form tránh recursion độ sâu concern và làm sự thay đổi dữ liệu flow rõ ràng.

## `O(alpha(n))` thực sự nghĩa là gì?

Kết hợp union-by-size/rank với đường đi compression cho độ phức tạp khấu hao:

\[
O(\alpha(n))
\]

mỗi thao tác, trong đó `\alpha` là **inverse Ackermann hàm**.

Không cần học chi tiết Ackermann hàm để dùng DSU. Điều cần hiểu là `alpha(n)` tăng cực chậm; với mọi `n` thực tế, nó là một hằng số rất nhỏ.

Nhưng nói “DSU là O(1)” về mặt lý thuyết là không chính xác. Cách nói tốt hơn:

> amortized gần constant trong mọi kích thước đầu vào thực tế, với bound `O(alpha(n))`.

## phân tích khấu hao ở đây đến từ đâu?

Một `find` riêng lẻ vẫn có thể đi qua nhiều các nút. Nhưng mỗi lần đi qua đường đi dài, compression làm structure phẳng hơn. Ta không thể liên tục trả chi phí lớn trên cùng các nút mà không thay đổi tương lai shape.

Đây là cùng family reasoning với mảng động resize: một thao tác đắt được “trả” bởi việc làm nhiều thao tác tương lai rẻ hơn.

## DSU trong Kruskal MST

Kruskal sort các cạnh theo trọng số rồi xét từng cạnh `(u,v)`.

Nếu:

```text
find(u) != find(v)
```

cạnh nối hai các thành phần khác nhau nên không tạo chu trình; ta nhận cạnh và `union(u,v)`.

Nếu representatives giống nhau, cạnh đóng chu trình và bỏ qua.

DSU ở đây không tìm chu trình bằng traversal. Nó chỉ trả lời “hai endpoints đã connected bởi các cạnh trước chưa?”.

## phát hiện chu trình khi add undirected các cạnh

Trong đồ thị ban đầu rỗng, xử lý các cạnh trực tuyến:

```text
for edge (u,v):
    if find(u) == find(v):
        adding edge creates a cycle
    else:
        union(u,v)
```

Lưu ý đây là reasoning cho **undirected** connectivity. Directed phát hiện chu trình không thể dùng DSU theo cách này vì directed reachability không phải quan hệ tương đương đơn giản.

## Connected các thành phần dưới merge-only các cập nhật

Nếu các đỉnh ban đầu tách rời và các cạnh chỉ được thêm, DSU là structure rất tự nhiên.

Maintain thêm:

```text
componentCount = n
```

mỗi successful union:

```text
componentCount--
```

Ta có thể truy vấn số các thành phần `O(1)`.

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

## Kruskal Reconstruction cây

Một extension thú vị: mỗi successful union có thể tạo một nội bộ nút mới đại diện thời điểm/trọng số mà hai các thành phần hợp nhất. các nút lá là original các đỉnh; nội bộ nút trọng số là cạnh threshold.

Sau khi xây dựng, các truy vấn như “minimum threshold để u và v connected” có thể biến thành LCA trên reconstruction cây.

Insight này cho thấy DSU không chỉ là endpoint thuật toán; nó còn có thể xây một hierarchy từ merge lịch sử.

## DSU với parity / bipartite các ràng buộc

Ta có thể lưu thêm relation từ nút tới nút cha. Ví dụ `parity[x]` biểu diễn màu của `x` XOR màu nút cha.

Khi `find(x)` compress đường đi, phải compose parity dọc đường đi.

Structure này có thể support các ràng buộc kiểu:

```text
u và v phải khác màu
```

và detect contradiction khi thêm các cạnh trong trực tuyến bipartiteness variants.

Nguyên tắc tổng quát: DSU có thể duy trì **relative potential** giữa nút và representative nếu relation compose được.

## Weighted / Potential DSU

Một biến thể lưu:

\[
potential[x] = giá trị(x) - giá trị(nút cha(x))
\]

hoặc một group-like relation tương tự. Khi union hai các thành phần với ràng buộc giữa `a` và `b`, ta tính potential của nút gốc mới sao cho relation vẫn đúng.

Ứng dụng gồm difference các ràng buộc đơn giản, coordinate relation và parity.

Đây là bước nâng cao: đường đi compression không chỉ đổi nút cha; mọi siêu dữ liệu relative-to-parent phải được cập nhật tương ứng.

## Tại sao DSU chuẩn không hỗ trợ xóa/tách tốt?

DSU được tối ưu cho **monotonic merge**. Sau đường đi compression, nhiều các nút có thể trỏ thẳng tới nút gốc; original cây structure gần như bị mất.

Nếu xóa một cạnh đã từng làm các thành phần merge, DSU không biết thành phần phải split thành những phần nào vì nó chưa bao giờ lưu đủ đồ thị topology.

Đây không phải thiếu feature nhỏ; đó là consequence trực tiếp của thông tin compression.

> DSU nhanh vì nó quên đường đi structure. Muốn support deletion, bạn cần giữ thêm thông tin hoặc đổi thuật toán.

## Rollback DSU

Nếu cần undo unions trong ngoại tuyến thuật toán, standard đường đi compression gây khó vì một `find` có thể mutate nhiều các nút cha.

**Rollback DSU (롤백 DSU)** thường:

- dùng union-by-size;
- không path-compress;
- mỗi union ghi thay đổi vào stack;
- rollback pop stack để restore nút cha/size.

Union/find khi đó thường `O(log n)` trường hợp xấu nhất do union-by-size chiều cao bound, nhưng undo trở nên đơn giản.

### Change stack idea

```text
union(ra, rb):
    record (rb, oldParent, ra, oldSizeRa)
    parent[rb] = ra
    size[ra] += size[rb]

rollback():
    restore recorded values
```

Optimization không tồn tại trong chân không: đường đi compression tốt cho forward các truy vấn nhưng xung đột với reversibility.

## động connectivity ngoại tuyến

Nếu các cạnh có cả add và remove theo time, có thể xử lý ngoại tuyến bằng cây đoạn (Segment Tree) over time + rollback DSU.

Mỗi cạnh tồn tại trên một interval thời gian `[l,r)`. Ta add cạnh vào các segment-tree các nút phủ interval đó. DFS cây đoạn:

```text
enter node -> apply unions
process children / answer queries
exit node -> rollback
```

Mỗi truy vấn sees đúng tập các cạnh active tại timestamp của nó.

Đây là một example nâng cao của việc kết hợp các cấu trúc dữ liệu: cây đoạn quản time intervals, rollback DSU quản connectivity trạng thái (state).

## Persistent / Partially Persistent DSU

Một hướng khác là giữ lịch sử để truy vấn connectivity ở version cũ. Có nhiều designs: union cây với timestamps, persistent các mảng, or versioned nút cha relations. Không phải mọi variant support arbitrary branching các cập nhật; cần xác định persistence mô hình.

Điểm conceptual là DSU có thể được mở rộng theo trục **time**, nhưng standard cách triển khai chỉ đại diện trạng thái hiện tại.

## gộp nhỏ vào lớn khác DSU thế nào?

Một technique khác cũng gọi “merge smaller into larger” là gộp nhỏ vào lớn của sets/maps trên cây. Ví dụ merge color-frequency maps của các nút con vào largest map.

Kỹ thuật này dùng cùng lập luận nhân đôi để chặn số lần một phần tử bị di chuyển ở `O(log n)`, nhưng nó không phải DSU. DSU duy trì định danh của các phân hoạch, còn gộp nhỏ vào lớn có thể duy trì các tập hợp dữ liệu giàu thông tin hơn.

Cùng chứng minh mẫu không đồng nghĩa cùng cấu trúc dữ liệu.

## Java cách triển khai đầy đủ cơ bản

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

## JavaScript cách triển khai

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

## Những hiểu lầm phổ biến

**“Representative là smallest phần tử.”** Không trừ khi bạn chủ động giữ quy tắc đó. nút gốc chỉ là cách triển khai identity.

**“DSU cho biết đường đi giữa hai các đỉnh.”** Không. Nó chỉ biết cùng thành phần hay không.

**“DSU dùng được cho directed reachability.”** Không theo standard formulation; directed connectivity không phải quan hệ tương đương đơn giản.

**“đường đi compression luôn nên bật.”** Không nếu cần rollback/undo hoặc một persistence design cụ thể.

**“`size[x]` luôn là thành phần size.”** Thường chỉ đúng ở nút gốc. Hãy dùng `size[find(x)]`.

**“Gần O(1) nghĩa là trường hợp xấu nhất O(1).”** Không. Bound chuẩn là amortized `O(alpha(n))` với hai optimizations.

## kiểm thử DSU

Một test tốt nên tạo ngẫu nhiên union/truy vấn sequence và so sánh với tham chiếu đồ thị connectivity trên `n` nhỏ.

các bất biến nên kiểm:

```text
parent[root] == root
size[root] bằng số elements thực trong component
find(x) idempotent: find(find(x)) == find(x)
components giảm đúng một khi union successful
connected là equivalence relation
```

quan hệ tương đương nghĩa là reflexive, symmetric và transitive. Đây cũng là lý do DSU hợp với partition problems.

## Connection với các lớp tương đương

Nếu relation “cùng nhóm” thực sự là quan hệ tương đương, DSU là cách biểu diễn tự nhiên:

```text
x ~ x                     reflexive
x ~ y => y ~ x            symmetric
x ~ y và y ~ z => x ~ z   transitive
```

Connected các thành phần của đồ thị vô hướng (undirected graph), account merging theo định danh dùng chung, synonym groups, clustering dưới merge các quy tắc đều có thể được nhìn như các lớp tương đương.

## Mô hình tư duy mở rộng

> DSU là một structure tối ưu cho **monotonic equivalence merging**. Nó đổi đường đi/topology detail lấy thành phần identity cực rẻ.

Khi gặp bài toán connectivity, hãy hỏi: các cạnh chỉ được thêm hay còn bị xóa? truy vấn cần đường đi hay chỉ yes/no cùng thành phần? Có threshold ngoại tuyến không? Có siêu dữ liệu per thành phần không? Có cần rollback không?

Nếu câu trả lời là “chỉ merge và hỏi cùng nhóm”, DSU thường là sự trừu tượng (abstraction) đúng hơn BFS/DFS lặp lại.