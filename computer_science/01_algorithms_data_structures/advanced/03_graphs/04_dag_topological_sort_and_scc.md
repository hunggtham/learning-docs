# DAG, sắp xếp tô-pô và Strongly Connected các thành phần

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **DAG, sắp xếp tô-pô và Strongly Connected các thành phần**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình tư duy** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **thứ tự tô-pô là gì?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối DAG, topological sort và SCC với dependency, cycle và condensation, để cấu trúc thứ tự được suy ra.

**DAG, sắp xếp tô-pô và thành phần liên thông mạnh / 방향 비순환 그래프, 위상 정렬, 강한 연결 요소**

đồ thị có hướng thường được dùng để biểu diễn phụ thuộc (dependency / 의존성): gói (package / 패키지) A cần B, tác vụ (task / 작업) X phải chạy trước Y, course prerequisite, xây dựng đích, dữ liệu (data / 데이터) chuỗi xử lý, chuyển tiếp trạng thái (state transition / 상태 전이) hoặc workflow. Khi phụ thuộc (dependency / 의존성) có chu trình, câu hỏi “cái nào phải trước cái nào” có thể mất ý nghĩa hoặc cần xử lý đặc biệt.

**Directed Acyclic đồ thị (DAG / 방향 비순환 그래프)** là đồ thị có hướng không có directed chu trình. DAG quan trọng vì nó biến một quan hệ phụ thuộc phức tạp thành một cấu trúc (structure / 구조) có thể xử lý theo thứ tự.

## Mô hình tư duy

> DAG cho ta một **thứ tự bộ phận**: không phải mọi cặp nút đều so sánh được, nhưng mọi phụ thuộc (dependency / 의존성) cạnh đều yêu cầu một hướng trước-sau. sắp xếp tô-pô biến thứ tự bộ phận đó thành một tuyến tính (linear / 선형) thứ tự (order / 순서) hợp lệ.

Nếu đồ thị có chu trình, không có thứ tự tô-pô đầy đủ vì một chu trình tạo contradiction kiểu:

```text
A trước B
B trước C
C trước A
```

Thứ tự tô-pô biến quan hệ phụ thuộc thành một thứ tự tuyến tính hợp lệ, còn mô hình tư duy cho biết khi nào thứ tự đó tồn tại. Cách xây dựng trực tiếp nhất là liên tục lấy đỉnh có indegree bằng không bằng thuật toán Kahn.

## thứ tự tô-pô là gì?

Một thứ tự (ordering / 순서) `v1, v2, ..., vn` là thứ tự tô-pô nếu với mọi cạnh:

\[
u \to v
\]

thì `u` xuất hiện trước `v`.

thứ tự tô-pô **không nhất thiết duy nhất**. Nếu hai tasks không phụ thuộc nhau, chúng có thể đổi chỗ mà vẫn hợp lệ.

Điều này rất quan trọng trong scheduling: đồ thị chỉ encode các ràng buộc bắt buộc, không phải một schedule duy nhất.

Kahn duy trì frontier các đỉnh đã trở nên khả dụng sau khi xóa các cạnh vào, nên mỗi bước đều có thể giải thích bằng indegree. Nếu frontier cạn trước khi xử lý hết đỉnh, chính điều đó là bằng chứng có chu trình.

## Kahn's thuật toán: lập luận (reasoning / 추론) bằng indegree

**Indegree (진입 차수)** của nút là số incoming các cạnh. Trong phụ thuộc (dependency / 의존성) đồ thị, indegree 0 nghĩa nút hiện không còn prerequisite chưa xử lý.

Kahn's thuật toán:

1. tính indegree mọi nút;
2. đưa tất cả nút indegree 0 vào frontier;
3. lấy một nút ra, append vào thứ tự (order / 순서);
4. “xóa lô-gic (logic / 논리)” các outgoing các cạnh bằng cách giảm indegree các đỉnh kề;
5. đỉnh kề nào về 0 thì trở thành eligible;
6. nếu xử lý đủ `V` nút, đồ thị là DAG.

### JavaScript cách triển khai

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

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

Độ phức tạp (complexity / 복잡도):

\[
O(V+E)
\]

vì mỗi đỉnh vào hàng đợi (queue / 큐) tối đa một lần và mỗi cạnh giảm indegree đúng một lần.

Chu trình không có đỉnh bắt đầu hợp lệ vì mọi đỉnh trong chu trình đều còn một cạnh vào từ chu trình. Sau khi hiểu invariant này, ta có thể chọn cấu trúc frontier theo mục tiêu phụ như thứ tự từ điển hoặc tính ổn định.

## Tại sao Kahn phát hiện chu trình?

Nếu còn các nút chưa xử lý nhưng không còn indegree-0 nút, mỗi nút còn lại có ít nhất một incoming cạnh từ region còn lại. Theo finite đồ thị, follow incoming các cạnh mãi cuối cùng phải lặp lại một đỉnh, tạo chu trình.

Do đó:

```text
processedCount < V
```

là certificate rằng đồ thị có directed chu trình.

Queue, stack hoặc priority queue đều có thể làm frontier; chúng tạo ra các thứ tự tô-pô khác nhau nhưng cùng hợp lệ, trừ khi bài toán yêu cầu tie-break cụ thể. Một cách xây dựng khác là DFS và thứ tự hoàn tất của nó.

## Frontier cấu trúc dữ liệu quyết định secondary mục tiêu (objective / 목표)

Nếu chỉ cần một thứ tự tô-pô bất kỳ, hàng đợi là đủ. Nếu muốn thứ tự nhỏ nhất theo từ điển, dùng đống nhỏ nhất thay cho hàng đợi:

```text
frontier = all indegree-0 nodes
always choose smallest eligible node
```

tính đúng đắn vẫn giống nhau; cấu trúc dữ liệu chỉ thêm secondary mục tiêu (objective / 목표).

Nếu muốn maximize parallelism, thay vì lấy một nút, có thể lấy toàn bộ hiện tại frontier như một thực thi (execution / 실행) wave. Đây là basis cho xây dựng các hệ thống và workflow bộ lập lịchs.

DFS đẩy một đỉnh vào thứ tự khi đã duyệt hết các successor của nó, rồi đảo danh sách hoàn tất để có thứ tự tô-pô. Cách này làm rõ vì sao thứ tự tô-pô không đồng nghĩa với sắp xếp nhãn đỉnh.

## DFS sắp xếp tô-pô

Một cách khác dùng DFS. nút được append sau khi tất cả các hậu duệ đã được xử lý, sau đó reverse finish thứ tự (order / 순서).

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

DFS cung cấp thứ tự thỏa quan hệ cạnh, còn label chỉ là dữ liệu phụ để phá hòa nếu được yêu cầu. Khi đã có thứ tự hợp lệ, mọi recurrence phụ thuộc acyclic có thể chạy bằng dynamic programming một lượt.

## thứ tự tô-pô không phải “sort theo label”

Tên “sort” dễ gây hiểu nhầm. sắp xếp tô-pô không so sánh khóa như quicksort/mergesort. Nó linearize phụ thuộc (dependency / 의존성) các ràng buộc.

Nếu đồ thị có nhiều hợp lệ orders, thuật toán được phép trả bất kỳ thứ tự (order / 순서) nào trừ khi bài toán (problem / 문제) thêm quy tắc phân xử khi bằng nhau quy tắc.

DP trên DAG thay cho việc lặp vô hạn vì mỗi cạnh đi theo thứ tự đã biết; ví dụ điển hình là longest path trong đồ thị công việc. Mô hình đó dẫn tự nhiên đến scheduling và critical path.

## DP trên DAG

DAG đặc biệt mạnh vì thứ tự tô-pô chính là evaluation thứ tự (order / 순서) của quy hoạch động (dynamic programming).

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

Critical path là một ứng dụng của longest-path DP khi phụ thuộc không có chu trình. Khi phụ thuộc có chu trình, cần gom các đỉnh mutually reachable thành strongly connected components trước.

## Scheduling và trọng yếu (critical / 중요) đường đi phương thức (method / 메서드)

Trong dự án (project / 프로젝트) scheduling, đỉnh/cạnh có thể biểu diễn tác vụ (task / 작업) và phụ thuộc (dependency / 의존성). Earliest completion thời gian (time / 시간) có thể được tính bằng longest đường đi trong DAG nếu durations không âm theo mô hình phù hợp.

Ví dụ:

\[
finish[v] = duration[v] + \max_{u \to v} finish[u]
\]

Tác vụ (task / 작업) trên longest phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬) tạo **trọng yếu (critical / 중요) đường đi**: delay ở đó trực tiếp kéo dài dự án (project / 프로젝트) thời điểm kết thúc nếu không có slack.

Đây là liên kết (connection / 연결) trực tiếp giữa DAG thuật toán và dự án (project / 프로젝트)/xây dựng scheduling.

SCC là tập cực đại trong đó mọi cặp đỉnh đi đến được nhau theo hướng. Co mỗi SCC thành một siêu đỉnh sẽ loại chu trình nội bộ và tạo ra condensation graph dạng DAG.

## thành phần liên thông mạnh là gì?

Trong đồ thị có hướng, một **thành phần liên thông mạnh (SCC / 강한 연결 요소)** là một maximal set các đỉnh sao cho với mọi `u,v` trong thành phần:

```text
u reaches v
v reaches u
```

Từ “maximal” quan trọng: không thể thêm đỉnh ngoài vào mà vẫn giữ mutual reachability.

SCC là cách nén những region mà directed reachability đã trở thành “hai chiều”.

Condensation graph giữ các cạnh giữa SCC khác nhau và luôn acyclic, nên các bài toán thứ tự và DP quay trở lại trên đồ thị rút gọn. Kosaraju tìm SCC bằng hai lượt DFS và transpose graph.

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

Kosaraju dùng thứ tự hoàn tất của DFS trên graph gốc để quyết định thứ tự duyệt trên graph đảo. Tarjan đạt cùng mục tiêu trong một DFS bằng stack và low-link, phù hợp khi muốn tránh tạo graph transpose.

## Kosaraju's thuật toán

Kosaraju dùng hai DFS passes.

### Pass 1: finish thứ tự (order / 순서) trên đồ thị gốc

DFS đồ thị và bản ghi (record / 레코드) các đỉnh theo finishing thời gian (time / 시간).

### Pass 2: DFS transpose theo reverse finish thứ tự (order / 순서)

**Transpose đồ thị** đảo mọi cạnh `u -> v` thành `v -> u`.

xử lý các đỉnh theo decreasing thời điểm kết thúc. Mỗi DFS trong transpose thu được một SCC.

### Intuition

Trong DAG co SCC, thứ tự hoàn tất của DFS giúp chọn một thành phần sao cho trên đồ thị chuyển vị nó không đi sang thành phần chưa nên được gom. Đảo cạnh làm đổi vai trò nguồn–đích, còn việc duyệt theo thứ tự hoàn tất đảo ngược giúp cô lập từng SCC đúng thời điểm.

Độ phức tạp (complexity / 복잡도):

\[
O(V+E)
\]

nhưng cần transpose đồ thị hoặc cách iterate reverse các cạnh.

Tarjan đánh dấu thời điểm vào stack và giá trị low-link để biết một subtree còn quay lại ancestor nào. Công thức này tương tự bridge-finding ở bề mặt, nhưng điều kiện tách SCC có ý nghĩa riêng trong đồ thị có hướng.

## Tarjan's SCC thuật toán

Tarjan tìm các thành phần liên thông mạnh trong một lượt DFS bằng chỉ số khám phá và một ngăn xếp đang hoạt động.

Mỗi nút có:

```text
index[u] = thời điểm discover
low[u]   = smallest discovery index reachable
           trong active DFS region theo rule của SCC
```

nút được push lên ngăn xếp (stack / 스택) khi active. Khi:

\[
low[u] = chỉ mục (index / 인덱스)[u]
\]

`u` là nút gốc của một SCC; pop ngăn xếp (stack / 스택) cho tới `u`.

### Vì sao cần `onStack`?

Không phải mọi đã thăm đỉnh kề đều được phép kéo `low[u]` xuống. cạnh tới nút thuộc SCC đã hoàn tất không biểu diễn một chu trình nằm trong active region hiện tại.

Vì vậy khi gặp cạnh tới đã thăm nút `v`, chỉ dùng `index[v]` để cập nhật low nếu `v` vẫn `onStack`.

Đây là một bug kinh điển khi implement Tarjan.

Trong Tarjan SCC, low-link phản ánh khả năng quay về một vertex đang ở stack; không được bê nguyên điều kiện của bridge trong đồ thị vô hướng. Skeleton Java tiếp theo hiện thực đúng các trạng thái này.

## Low-link trong Tarjan khác cầu nối (bridge / 브리지) low-link

Cùng tên `low` nhưng ngữ nghĩa (semantics / 의미론) không hoàn toàn giống nhau.

Cầu nối (bridge / 브리지)/articulation trong đồ thị vô hướng (undirected graph) hỏi cây con có thể đi ngược tới tổ tiên nào mà không dùng nút cha cạnh.

Trong Tarjan SCC, giá trị low-link biểu diễn chỉ số khám phá nhỏ nhất mà vùng DFS có hướng đang hoạt động có thể đi tới trong phạm vi các đỉnh vẫn còn trên ngăn xếp.

Không nên bản sao (copy / 복사) công thức giữa hai các thuật toán mà không hiểu bất biến (invariant / 불변식).

Skeleton chỉ an toàn khi cập nhật index, low-link, membership trong stack và thao tác pop theo đúng thứ tự. Sau khi có SCC, phát hiện chu trình trở thành kiểm tra kích thước SCC hoặc self-loop.

## Java skeleton cho Tarjan SCC

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

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

Recursive DFS có thể stack-overflow trên đồ thị cực sâu. Trong hệ thống thực tế, cách triển khai có thể cần iterative traversal hoặc tăng ngăn xếp (stack / 스택) có chủ đích tùy môi trường chạy (runtime).

Một SCC có từ hai đỉnh hoặc một self-loop biểu thị chu trình có hướng; SCC đơn đỉnh không có self-loop là acyclic. Phép phân tích này hữu ích trực tiếp khi kiểm tra dependency của hệ thống.

## SCC và phát hiện chu trình

Một SCC có nhiều hơn một đỉnh chắc chắn chứa directed chu trình. SCC một đỉnh cũng có chu trình nếu có self-loop.

Do đó SCC decomposition không chỉ nói “có chu trình không”, mà còn cho biết **chu trình clusters ở đâu** và cách chúng liên hệ với phần acyclic còn lại.

Dependency graph dùng SCC để chỉ ra các module hoặc package tạo thành vòng phụ thuộc, sau đó condensation graph cho thứ tự xử lý phần còn lại. Cấu trúc SCC cũng là nền tảng của phép giải 2-SAT.

## ứng dụng: phụ thuộc (dependency / 의존성) các hệ thống

### xây dựng đồ thị

Nếu modules A, B, C tạo SCC, chúng có circular phụ thuộc (dependency / 의존성). xây dựng hệ thống có thể reject, bundle chúng thành một đơn vị (unit / 단위) hoặc yêu cầu refactor ranh giới.

### Gói (package / 패키지) managers

Phụ thuộc (dependency / 의존성) SCC có thể biểu diễn nhóm packages phụ thuộc vòng nhau. Condensation DAG cho thứ tự xử lý giữa groups.

### trạng thái machines

SCC là region mà các trạng thái có thể quay lại lẫn nhau. Một SCC không có outgoing cạnh trong condensation DAG là vùng lặp lại cuối cùng theo xác định/nondeterministic mô hình phù hợp.

### Web/link đồ thị

SCC có thể biểu diễn communities với mutual reachability, dù đồ thị analytics hệ thống thực tế thường dùng thêm metrics khác.

Trong 2-SAT, SCC trên implication graph cho biết một biến và phủ định của nó có xung đột hay không, đồng thời quyết định thứ tự gán. Với quan hệ DAG, các phép closure và reduction trả lời một câu hỏi khác: cạnh nào là trực tiếp và cạnh nào là suy ra.

## 2-SAT liên kết (connection / 연결)

Trong implication đồ thị của 2-SAT, mỗi literal Boolean có nút và clause tạo implications. Công thức unsatisfiable nếu một variable `x` và `¬x` nằm trong cùng SCC.

Sau SCC decomposition, condensation thứ tự (order / 순서) còn giúp derive assignment.

Đây là một example mạnh nơi lô-gic (logic / 논리) bài toán (problem / 문제) được biến thành directed reachability cấu trúc (structure / 구조).

Transitive closure lưu mọi quan hệ có thể đi tới, còn transitive reduction giữ một tập cạnh tối thiểu nhưng vẫn bảo toàn reachability trong DAG. Khi nhìn vào reachability và indegree, ta có thể xác định thứ tự tô-pô có duy nhất hay không.

## DAG transitive reduction và transitive closure

Hai concepts thường bị nhầm.

**Transitive closure** thêm thông tin reachability: cạnh lô-gic (logic / 논리) `u -> v` tồn tại nếu `v` có thể tới từ `u`.

**Transitive reduction** cố bỏ các cạnh dư mà vẫn giữ cùng reachability quan hệ (relation / 관계). Với DAG, transitive reduction là unique theo điều kiện chuẩn.

Ví dụ nếu có:

```text
A -> B
B -> C
A -> C
```

cạnh `A -> C` là redundant về reachability.

Trong phụ thuộc (dependency / 의존성) visualization, reduction giúp đồ thị dễ đọc hơn; closure giúp truy vấn reachability nhanh hơn nhưng có thể tốn `O(V^2)` không gian (space / 공간).

Thứ tự tô-pô duy nhất khi tại mỗi bước chỉ có một đỉnh indegree bằng không trong đồ thị còn lại, tương đương với việc các ràng buộc xác định hoàn toàn thứ tự. Các ngộ nhận phổ biến thường xuất phát từ việc nhầm tính duy nhất với việc nhãn đã được sắp xếp.

## Uniqueness của thứ tự tô-pô

thứ tự tô-pô unique khi tại mỗi bước Kahn chỉ có đúng một eligible indegree-0 nút. Nếu có hai choices, ít nhất hai hợp lệ orders có thể tồn tại.

Góc nhìn tương đương: trong một thứ tự tô-pô unique, mỗi cặp consecutive các đỉnh phải có phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조) buộc thứ tự phù hợp.

Đây là useful tính chất khi bài toán (problem / 문제) hỏi “schedule có duy nhất không?”.

Các lỗi thường gặp gồm coi mọi graph là DAG, dùng DFS mà quên phát hiện back edge, hoặc dùng label để thay cho constraint. Kiểm thử cần tạo cả graph hợp lệ, graph có chu trình và trường hợp nhiều thứ tự hợp lệ.

## Những hiểu lầm phổ biến

**“Có sắp xếp tô-pô cho mọi đồ thị có hướng.”** Sai. Chỉ DAG mới có full thứ tự tô-pô.

**“Kahn không đầu ra đủ nút nghĩa là thuật toán bug.”** Có thể đồ thị có chu trình; đó chính là detection cơ chế (mechanism / 메커니즘).

**“thứ tự tô-pô là unique.”** Thường không.

**“SCC giống thành phần liên thông của đồ thị vô hướng.”** Không. Directed reachability phải đúng cả hai chiều.

**“Tarjan low giống cầu nối (bridge / 브리지) low nên dùng cùng formula.”** Không nên; các bất biến khác nhau.

**“Collapse SCC có thể vẫn còn chu trình.”** Không. Nếu còn chu trình, các thành phần trên chu trình phải là một SCC lớn hơn.

Kiểm thử nên đối chiếu mọi cạnh với vị trí trong output, kiểm tra đủ đỉnh và xác nhận chu trình được báo đúng. Mô hình tư duy mở rộng sau đây nối topological order, SCC và các ứng dụng vào cùng một chuỗi quyết định.

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

Mô hình tư duy mở rộng là: xác định hướng cạnh, kiểm tra chu trình, chọn Kahn hoặc DFS, rồi co SCC nếu graph có các vòng liên thông mạnh. Các liên kết cuối bài đưa những nguyên tắc này về tài liệu nền và bài toán ứng dụng.

## Mô hình tư duy mở rộng

> sắp xếp tô-pô là cách **tháo một phụ thuộc (dependency / 의존성) đồ thị từ ngoài vào**. SCC là cách **nén các vùng không thể áp một thứ tự một chiều bên trong**. Sau khi nén mọi mutual-reachability region, phần còn lại bắt buộc trở thành DAG.

Khi gặp đồ thị có hướng có các chu trình, thay vì cố áp dụng DAG thuật toán trực tiếp, hãy hỏi liệu chu trình có semantic meaning gì và liệu SCC condensation có biến problem thành DAG problem dễ hơn không.

> **Bàn giao:** Sau **Mô hình tư duy mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
