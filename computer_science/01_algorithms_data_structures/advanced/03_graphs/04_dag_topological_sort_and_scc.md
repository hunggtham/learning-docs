# DAG, sắp xếp tô-pô và Strongly Connected các thành phần
**DAG, sắp xếp tô-pô và thành phần liên thông mạnh / 방향 비순환 그래프, 위상 정렬, 강한 연결 요소**

đồ thị có hướng thường được dùng để biểu diễn dependency: package A cần B, task X phải chạy trước Y, course prerequisite, xây dựng đích, data chuỗi xử lý, trạng thái (state) transition hoặc workflow. Khi dependency có chu trình, câu hỏi “cái nào phải trước cái nào” có thể mất ý nghĩa hoặc cần xử lý đặc biệt.

**Directed Acyclic đồ thị (DAG / 방향 비순환 그래프)** là đồ thị có hướng không có directed chu trình. DAG quan trọng vì nó biến một quan hệ phụ thuộc phức tạp thành một structure có thể xử lý theo thứ tự.

## Mô hình tư duy

> DAG cho ta một **thứ tự bộ phận**: không phải mọi cặp nút đều so sánh được, nhưng mọi dependency cạnh đều yêu cầu một hướng trước-sau. sắp xếp tô-pô biến thứ tự bộ phận đó thành một linear order hợp lệ.

Nếu đồ thị có chu trình, không có thứ tự tô-pô đầy đủ vì một chu trình tạo contradiction kiểu:

```text
A trước B
B trước C
C trước A
```

## thứ tự tô-pô là gì?

Một ordering `v1, v2, ..., vn` là thứ tự tô-pô nếu với mọi cạnh:

\[
u \to v
\]

thì `u` xuất hiện trước `v`.

thứ tự tô-pô **không nhất thiết duy nhất**. Nếu hai tasks không phụ thuộc nhau, chúng có thể đổi chỗ mà vẫn hợp lệ.

Điều này rất quan trọng trong scheduling: đồ thị chỉ encode các ràng buộc bắt buộc, không phải một schedule duy nhất.

## Kahn's thuật toán: reasoning bằng indegree

**Indegree (진입 차수)** của nút là số incoming các cạnh. Trong dependency đồ thị, indegree 0 nghĩa nút hiện không còn prerequisite chưa xử lý.

Kahn's thuật toán:

1. tính indegree mọi nút;
2. đưa tất cả nút indegree 0 vào frontier;
3. lấy một nút ra, append vào order;
4. “xóa logic” các outgoing các cạnh bằng cách giảm indegree các đỉnh kề;
5. đỉnh kề nào về 0 thì trở thành eligible;
6. nếu xử lý đủ `V` nút, đồ thị là DAG.

### JavaScript cách triển khai

```js
function topoSort(n, g) {
  const indeg = Array(n).fill(0);
  for (let u = 0; u < n; u++) {
    for (const v of g[u]) indeg[v]++;
  }

  const q = [];
  let head = 0;
  for (let v = 0; v < n; v++) {
    if (indeg[v] === 0) q.push(v);
  }

  const order = [];

  while (head < q.length) {
    const u = q[head++];
    order.push(u);

    for (const v of g[u]) {
      if (--indeg[v] === 0) q.push(v);
    }
  }

  return order.length === n ? order : null;
}
```

Complexity:

\[
O(V+E)
\]

vì mỗi đỉnh vào queue tối đa một lần và mỗi cạnh giảm indegree đúng một lần.

## Tại sao Kahn phát hiện chu trình?

Nếu còn các nút chưa xử lý nhưng không còn indegree-0 nút, mỗi nút còn lại có ít nhất một incoming cạnh từ region còn lại. Theo finite đồ thị, follow incoming các cạnh mãi cuối cùng phải lặp lại một đỉnh, tạo chu trình.

Do đó:

```text
processedCount < V
```

là certificate rằng đồ thị có directed chu trình.

## Frontier cấu trúc dữ liệu quyết định secondary objective

Nếu chỉ cần một thứ tự tô-pô bất kỳ, hàng đợi là đủ. Nếu muốn thứ tự nhỏ nhất theo từ điển, dùng đống nhỏ nhất thay cho hàng đợi:

```text
frontier = all indegree-0 nodes
always choose smallest eligible node
```

tính đúng đắn vẫn giống nhau; cấu trúc dữ liệu chỉ thêm secondary objective.

Nếu muốn maximize parallelism, thay vì lấy một nút, có thể lấy toàn bộ hiện tại frontier như một execution wave. Đây là basis cho xây dựng các hệ thống và workflow bộ lập lịchs.

## DFS sắp xếp tô-pô

Một cách khác dùng DFS. nút được append sau khi tất cả các hậu duệ đã được xử lý, sau đó reverse finish order.

```java
void dfs(int u) {
    state[u] = 1; // visiting

    for (int v : g.get(u)) {
        if (state[v] == 1) throw new CycleDetected();
        if (state[v] == 0) dfs(v);
    }

    state[u] = 2; // done
    order.add(u);
}
```

Ba trạng thái thường là:

```text
0 = unseen
1 = active / gray
2 = finished / black
```

cạnh tới nút đang `active` là back cạnh và chứng minh có directed chu trình.

DFS topo và Kahn đều `O(V+E)`, nhưng mental mô hình khác nhau:

```text
Kahn -> repeatedly remove prerequisites-free nodes
DFS  -> output node only after all descendants finish
```

## thứ tự tô-pô không phải “sort theo label”

Tên “sort” dễ gây hiểu nhầm. sắp xếp tô-pô không so sánh khóa như quicksort/mergesort. Nó linearize dependency các ràng buộc.

Nếu đồ thị có nhiều hợp lệ orders, thuật toán được phép trả bất kỳ order nào trừ khi problem thêm quy tắc phân xử khi bằng nhau quy tắc.

## DP trên DAG

DAG đặc biệt mạnh vì thứ tự tô-pô chính là evaluation order của quy hoạch động (dynamic programming).

Giả sử `dp[v]` phụ thuộc các predecessor `u -> v`. Sau sắp xếp tô-pô, khi tới `v`, mọi predecessor đã được xử lý.

### Longest đường đi trên DAG

Longest đường đi trên general đồ thị rất khó vì chu trình cho phép bùng nổ tổ hợp. Trên DAG:

\[
dp[v] = \max_{u \to v}(dp[u] + w(u,v))
\]

chỉ cần một pass theo thứ tự tô-pô:

\[
O(V+E)
\]

### đường đi counting

Nếu muốn số các đường đi từ nguồn tới mỗi nút:

```text
ways[source] = 1
for u in topo:
    for v in g[u]:
        ways[v] += ways[u]
```

Không chu trình nghĩa là contribution chỉ chảy theo một chiều và không cần lặp lại relaxation.

## Scheduling và Critical đường đi Method

Trong project scheduling, đỉnh/cạnh có thể biểu diễn task và dependency. Earliest completion time có thể được tính bằng longest đường đi trong DAG nếu durations không âm theo mô hình phù hợp.

Ví dụ:

\[
finish[v] = duration[v] + \max_{u \to v} finish[u]
\]

Task trên longest dependency chain tạo **critical đường đi**: delay ở đó trực tiếp kéo dài project thời điểm kết thúc nếu không có slack.

Đây là connection trực tiếp giữa DAG thuật toán và project/xây dựng scheduling.

## thành phần liên thông mạnh là gì?

Trong đồ thị có hướng, một **thành phần liên thông mạnh (SCC / 강한 연결 요소)** là một maximal set các đỉnh sao cho với mọi `u,v` trong thành phần:

```text
u reaches v
v reaches u
```

Từ “maximal” quan trọng: không thể thêm đỉnh ngoài vào mà vẫn giữ mutual reachability.

SCC là cách nén những region mà directed reachability đã trở thành “hai chiều”.

## Condensation đồ thị

Co mỗi SCC thành một siêu nút (super-node). Nếu có cạnh nối hai SCC khác nhau, tạo cạnh tương ứng giữa hai siêu nút.

đồ thị kết quả gọi là **condensation DAG (축약 DAG)** và luôn là DAG.

chứng minh rất trực tiếp: nếu condensation đồ thị có chu trình giữa nhiều các thành phần, từ thành phần nào cũng có thể đi vòng về thành phần khác và quay lại; như vậy chúng thực ra mutually có thể tới và phải là cùng một SCC, contradiction.

Mental chuỗi xử lý rất mạnh:

```text
graph directed phức tạp
        ↓
find SCCs
        ↓
collapse mutually-reachable regions
        ↓
solve easier problem on DAG
```

## Kosaraju's thuật toán

Kosaraju dùng hai DFS passes.

### Pass 1: finish order trên đồ thị gốc

DFS đồ thị và record các đỉnh theo finishing time.

### Pass 2: DFS transpose theo reverse finish order

**Transpose đồ thị** đảo mọi cạnh `u -> v` thành `v -> u`.

xử lý các đỉnh theo decreasing thời điểm kết thúc. Mỗi DFS trong transpose thu được một SCC.

### Intuition

Trong DAG co SCC, thứ tự hoàn tất của DFS giúp chọn một thành phần sao cho trên đồ thị chuyển vị nó không đi sang thành phần chưa nên được gom. Đảo cạnh làm đổi vai trò nguồn–đích, còn việc duyệt theo thứ tự hoàn tất đảo ngược giúp cô lập từng SCC đúng thời điểm.

Complexity:

\[
O(V+E)
\]

nhưng cần transpose đồ thị hoặc cách iterate reverse các cạnh.

## Tarjan's SCC thuật toán

Tarjan tìm các thành phần liên thông mạnh trong một lượt DFS bằng chỉ số khám phá và một ngăn xếp đang hoạt động.

Mỗi nút có:

```text
index[u] = thời điểm discover
low[u]   = smallest discovery index reachable
           trong active DFS region theo rule của SCC
```

nút được push lên stack khi active. Khi:

\[
low[u] = index[u]
\]

`u` là nút gốc của một SCC; pop stack cho tới `u`.

### Vì sao cần `onStack`?

Không phải mọi đã thăm đỉnh kề đều được phép kéo `low[u]` xuống. cạnh tới nút thuộc SCC đã hoàn tất không biểu diễn một chu trình nằm trong active region hiện tại.

Vì vậy khi gặp cạnh tới đã thăm nút `v`, chỉ dùng `index[v]` để cập nhật low nếu `v` vẫn `onStack`.

Đây là một bug kinh điển khi implement Tarjan.

## Low-link trong Tarjan khác bridge low-link

Cùng tên `low` nhưng ngữ nghĩa (semantics) không hoàn toàn giống nhau.

Bridge/articulation trong đồ thị vô hướng (undirected graph) hỏi cây con có thể đi ngược tới tổ tiên nào mà không dùng nút cha cạnh.

Trong Tarjan SCC, giá trị low-link biểu diễn chỉ số khám phá nhỏ nhất mà vùng DFS có hướng đang hoạt động có thể đi tới trong phạm vi các đỉnh vẫn còn trên ngăn xếp.

Không nên copy công thức giữa hai các thuật toán mà không hiểu bất biến (invariant).

## Java skeleton cho Tarjan SCC

```java
int timer = 0;
int[] index, low, comp;
boolean[] onStack;
Deque<Integer> stack = new ArrayDeque<>();

void dfs(int u) {
    index[u] = low[u] = timer++;
    stack.push(u);
    onStack[u] = true;

    for (int v : g.get(u)) {
        if (index[v] == -1) {
            dfs(v);
            low[u] = Math.min(low[u], low[v]);
        } else if (onStack[v]) {
            low[u] = Math.min(low[u], index[v]);
        }
    }

    if (low[u] == index[u]) {
        while (true) {
            int v = stack.pop();
            onStack[v] = false;
            comp[v] = componentCount;
            if (v == u) break;
        }
        componentCount++;
    }
}
```

Recursive DFS có thể stack-overflow trên đồ thị cực sâu. Trong hệ thống thực tế, cách triển khai có thể cần iterative traversal hoặc tăng stack có chủ đích tùy môi trường chạy (runtime).

## SCC và phát hiện chu trình

Một SCC có nhiều hơn một đỉnh chắc chắn chứa directed chu trình. SCC một đỉnh cũng có chu trình nếu có self-loop.

Do đó SCC decomposition không chỉ nói “có chu trình không”, mà còn cho biết **chu trình clusters ở đâu** và cách chúng liên hệ với phần acyclic còn lại.

## ứng dụng: dependency các hệ thống

### xây dựng đồ thị

Nếu modules A, B, C tạo SCC, chúng có circular dependency. xây dựng hệ thống có thể reject, bundle chúng thành một unit hoặc yêu cầu refactor ranh giới.

### Package managers

Dependency SCC có thể biểu diễn nhóm packages phụ thuộc vòng nhau. Condensation DAG cho thứ tự xử lý giữa groups.

### trạng thái machines

SCC là region mà các trạng thái có thể quay lại lẫn nhau. Một SCC không có outgoing cạnh trong condensation DAG là vùng lặp lại cuối cùng theo xác định/nondeterministic mô hình phù hợp.

### Web/link đồ thị

SCC có thể biểu diễn communities với mutual reachability, dù đồ thị analytics hệ thống thực tế thường dùng thêm metrics khác.

## 2-SAT connection

Trong implication đồ thị của 2-SAT, mỗi literal Boolean có nút và clause tạo implications. Công thức unsatisfiable nếu một variable `x` và `¬x` nằm trong cùng SCC.

Sau SCC decomposition, condensation order còn giúp derive assignment.

Đây là một example mạnh nơi logic problem được biến thành directed reachability structure.

## DAG transitive reduction và transitive closure

Hai concepts thường bị nhầm.

**Transitive closure** thêm thông tin reachability: cạnh logic `u -> v` tồn tại nếu `v` có thể tới từ `u`.

**Transitive reduction** cố bỏ các cạnh dư mà vẫn giữ cùng reachability relation. Với DAG, transitive reduction là unique theo điều kiện chuẩn.

Ví dụ nếu có:

```text
A -> B
B -> C
A -> C
```

cạnh `A -> C` là redundant về reachability.

Trong dependency visualization, reduction giúp đồ thị dễ đọc hơn; closure giúp truy vấn reachability nhanh hơn nhưng có thể tốn `O(V^2)` space.

## Uniqueness của thứ tự tô-pô

thứ tự tô-pô unique khi tại mỗi bước Kahn chỉ có đúng một eligible indegree-0 nút. Nếu có hai choices, ít nhất hai hợp lệ orders có thể tồn tại.

Góc nhìn tương đương: trong một thứ tự tô-pô unique, mỗi cặp consecutive các đỉnh phải có dependency structure buộc thứ tự phù hợp.

Đây là useful tính chất khi problem hỏi “schedule có duy nhất không?”.

## Những hiểu lầm phổ biến

**“Có sắp xếp tô-pô cho mọi đồ thị có hướng.”** Sai. Chỉ DAG mới có full thứ tự tô-pô.

**“Kahn không đầu ra đủ nút nghĩa là thuật toán bug.”** Có thể đồ thị có chu trình; đó chính là detection mechanism.

**“thứ tự tô-pô là unique.”** Thường không.

**“SCC giống thành phần liên thông của đồ thị vô hướng.”** Không. Directed reachability phải đúng cả hai chiều.

**“Tarjan low giống bridge low nên dùng cùng formula.”** Không nên; các bất biến khác nhau.

**“Collapse SCC có thể vẫn còn chu trình.”** Không. Nếu còn chu trình, các thành phần trên chu trình phải là một SCC lớn hơn.

## kiểm thử

Cho sắp xếp tô-pô, sau khi có `pos[v]`, kiểm mọi cạnh:

\[
pos[u] < pos[v]
\]

Nếu thuật toán report chu trình, có thể differential-test với DFS color-trạng thái trên đồ thị nhỏ.

Cho SCC, kiểm:

- các đỉnh cùng thành phần mutually có thể tới trên small tham chiếu đồ thị;
- các đỉnh khác thành phần không mutually có thể tới cả hai chiều;
- condensation đồ thị acyclic;
- self-loop và isolated đỉnh;
- các cạnh song song;
- một chuỗi dài, một chu trình lớn, hoặc nhiều SCC nhỏ.

Property-based tests đặc biệt hữu ích với Tarjan vì bug `onStack` và low-link thường chỉ xuất hiện ở đồ thị shape cụ thể.

## Mô hình tư duy mở rộng

> sắp xếp tô-pô là cách **tháo một dependency đồ thị từ ngoài vào**. SCC là cách **nén các vùng không thể áp một thứ tự một chiều bên trong**. Sau khi nén mọi mutual-reachability region, phần còn lại bắt buộc trở thành DAG.

Khi gặp đồ thị có hướng có các chu trình, thay vì cố áp dụng DAG thuật toán trực tiếp, hãy hỏi liệu chu trình có semantic meaning gì và liệu SCC condensation có biến problem thành DAG problem dễ hơn không.