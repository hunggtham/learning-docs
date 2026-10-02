# Eulerian các đường đi và các chu trình

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Eulerian các đường đi và các chu trình**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. sự trừu tượng (abstraction) từ Königsberg** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Trail, đường đi, circuit và terminology** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Eulerian paths với degree, connectivity và traversal, để điều kiện tồn tại đường đi được chứng minh từ graph.

**Đường đi Euler và chu trình Euler / Eulerian đường đi & chu trình / 오일러 경로와 회로**

Eulerian problems hỏi một câu rất cụ thể: **có thể đi qua mỗi cạnh đúng một lần hay không?** Đây là bài toán về cạnh usage, khác hoàn toàn Hamiltonian đường đi/chu trình nơi mỗi **đỉnh** phải được thăm đúng một lần.

Sự khác biệt này quyết định độ khó. Eulerian đường đi có characterization rất đẹp bằng degree/balance và có thể xây trong `O(V+E)`. Hamiltonian đường đi nói chung không có cục bộ criterion đơn giản tương tự và thuộc lớp bài toán khó hơn nhiều.

## 1. sự trừu tượng (abstraction) từ Königsberg

Bài toán các cây cầu Königsberg nổi tiếng vì Euler bỏ hình dạng địa lý cụ thể và chỉ giữ:

```text
land regions -> vertices
bridges      -> edges
```

Question “đi qua mỗi cầu nối (bridge / 브리지) đúng một lần” trở thành đồ thị bài toán (problem / 문제). Đây là một ví dụ lịch sử điển hình của algorithmic mô hình hóa: bỏ detail không ảnh hưởng feasibility và giữ cấu trúc (structure / 구조) quyết định bài toán.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **2. Trail, đường đi, circuit và terminology** tiếp nhận điểm tựa từ **1. sự trừu tượng (abstraction) từ Königsberg** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. đồ thị vô hướng (undirected graph): parity điều kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Trail, đường đi, circuit và terminology

Trong nhiều tài liệu:

- **trail**: không lặp cạnh;
- **đường đi**: thường không lặp đỉnh theo graph-theory strict terminology;
- **Eulerian trail/đường đi**: đi qua mọi cạnh đúng một lần, đỉnh có thể lặp;
- **Eulerian circuit/chu trình**: Eulerian trail có start = end.

Competitive-programming material đôi khi dùng “Euler đường đi” cho trail. Khi đọc tài liệu, hãy nhìn ngữ nghĩa (semantics / 의미론) thay vì chỉ tên.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **3. đồ thị vô hướng (undirected graph): parity điều kiện** tiếp nhận điểm tựa từ **2. Trail, đường đi, circuit và terminology** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Vì sao parity là điều kiện cần?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. đồ thị vô hướng (undirected graph): parity điều kiện

Bỏ qua isolated các đỉnh degree 0, phần đồ thị chứa các cạnh phải connected.

Eulerian chu trình tồn tại khi **mọi đỉnh có degree chẵn**.

Đường đi Euler mở tồn tại khi **đúng hai đỉnh có bậc lẻ**; hai đỉnh đó là hai đầu mút của đường đi.

Nếu số odd-degree các đỉnh khác 0 hoặc 2, không tồn tại Eulerian trail.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **4. Vì sao parity là điều kiện cần?** tiếp nhận điểm tựa từ **3. đồ thị vô hướng (undirected graph): parity điều kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Vì sao parity chưa đủ?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Vì sao parity là điều kiện cần?

Ở một đỉnh trung gian, mỗi lần tuyến (route / 경로) đi vào qua một unused cạnh, nó phải đi ra qua một unused cạnh khác. sự cố (incident / 인시던트) các cạnh được consume theo cặp:

```text
in + out
in + out
...
```

nên degree phải chẵn.

Start của open trail có thể có một outgoing cạnh dư, end có một incoming cạnh dư, tạo đúng hai odd các đỉnh.

Handshaking lemma cũng nói số odd-degree các đỉnh trong đồ thị vô hướng luôn chẵn, nên “1 odd đỉnh” vốn đã bất khả thi.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **5. Vì sao parity chưa đủ?** tiếp nhận điểm tựa từ **4. Vì sao parity là điều kiện cần?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. đồ thị có hướng: cân bằng bậc vào/bậc ra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Vì sao parity chưa đủ?

Hai các chu trình tách rời có mọi degree chẵn nhưng không thể có một tour duy nhất dùng các cạnh của cả hai các thành phần. Ta không thể teleport.

Vì vậy cần connectivity của **subgraph chứa nonzero-degree các đỉnh**.

Isolated các đỉnh không ảnh hưởng edge-covering trail vì không có cạnh cần dùng ở đó.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **6. đồ thị có hướng: cân bằng bậc vào/bậc ra** tiếp nhận điểm tựa từ **5. Vì sao parity chưa đủ?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Connectivity trong đồ thị có hướng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. đồ thị có hướng: cân bằng bậc vào/bậc ra

Với đồ thị có hướng, parity được thay bằng balance.

Eulerian chu trình:

```text
indegree(v) == outdegree(v)
```

cho mọi relevant đỉnh, kèm connectivity điều kiện thích hợp.

Open trail:

```text
start: out = in + 1
end:   in  = out + 1
others: in == out
```

Trực giác theo luồng rất rõ: ở mỗi đỉnh trung gian, các cạnh đi vào và đi ra phải được sử dụng theo cặp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **7. Connectivity trong đồ thị có hướng** tiếp nhận điểm tựa từ **6. đồ thị có hướng: cân bằng bậc vào/bậc ra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Start đỉnh selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Connectivity trong đồ thị có hướng

Degree balance một mình không đủ. Với Eulerian chu trình, các đỉnh có nonzero degree phải nằm trong một directed connectivity cấu trúc (structure / 구조) đủ mạnh để mọi các cạnh thuộc cùng traversable thành phần.

Một cách lập luận (reasoning / 추론) chuẩn là kiểm tra strongly connected trên relevant các đỉnh sau khi xử lý start/end các điều kiện thích hợp, hoặc dùng theorem tương đương với tính liên thông của đồ thị vô hướng nền cộng degree các ràng buộc cho Eulerian trail trong formulation cụ thể.

Điểm cốt lõi: **balance không nối các thành phần**.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **8. Start đỉnh selection** tiếp nhận điểm tựa từ **7. Connectivity trong đồ thị có hướng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Hierholzer's thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Start đỉnh selection

Undirected:

```text
0 odd vertices -> start bất kỳ vertex degree > 0
2 odd vertices -> start phải là một odd vertex
```

Directed:

```text
open trail -> start có out = in + 1
cycle      -> start bất kỳ vertex có outgoing edge
```

Start sai có thể làm traversal kết thúc sớm dù đồ thị có Eulerian trail hợp lệ.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **9. Hierholzer's thuật toán** tiếp nhận điểm tựa từ **8. Start đỉnh selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Vì sao Hierholzer không bị “greedy dead-end”?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Hierholzer's thuật toán

Hierholzer xây tuyến (route / 경로) bằng cách đi qua unused các cạnh cho tới khi hiện tại đỉnh không còn cạnh unused. Khi dead-end, đỉnh được đưa vào đầu ra và ta backtrack.

Ngăn xếp (stack / 스택) view:

```text
while stack not empty:
    u = top
    if u còn unused edge:
        consume edge (u,v)
        push v
    else:
        path.push(pop stack)
reverse(path)
```

đầu ra được tạo theo reverse finishing thứ tự (order / 순서).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **10. Vì sao Hierholzer không bị “greedy dead-end”?** tiếp nhận điểm tựa từ **9. Hierholzer's thuật toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Splicing view** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Vì sao Hierholzer không bị “greedy dead-end”?

Trong đồ thị thỏa Euler các điều kiện, balance/parity đảm bảo một tuyến (route / 경로) đang đi không thể mắc kẹt ở đỉnh “sai” trừ endpoint hợp lệ. Nếu tour cục bộ đóng lại nhưng vẫn còn unused các cạnh, connectivity đảm bảo unused region gắn vào một đỉnh đã xuất hiện trong tour. Ta có thể bắt đầu sub-tour ở đó và splice vào tuyến (route / 경로) cũ.

Đây là khác biệt với arbitrary đường đi tìm kiếm (search / 검색): đồ thị cấu trúc (structure / 구조) bảo đảm cục bộ cạnh consumption có thể ghép thành toàn cục lời giải.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **11. Splicing view** tiếp nhận điểm tựa từ **10. Vì sao Hierholzer không bị “greedy dead-end”?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. cách biểu diễn (representation / 표현) quyết định độ phức tạp (complexity / 복잡도) thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Splicing view

Kinh điển chứng minh thường hình dung:

1. xây một chu trình;
2. tìm đỉnh trên chu trình còn unused cạnh;
3. xây chu trình khác từ đỉnh đó;
4. splice chu trình mới vào chu trình cũ;
5. lặp tới khi hết các cạnh.

Ngăn xếp (stack / 스택) cách triển khai chính là cách thực hiện việc splice này implicit và gọn hơn.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **12. cách biểu diễn (representation / 표현) quyết định độ phức tạp (complexity / 복잡도) thật** tiếp nhận điểm tựa từ **11. Splicing view** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. đồ thị vô hướng cần cạnh ID** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. cách biểu diễn (representation / 표현) quyết định độ phức tạp (complexity / 복잡도) thật

Nếu mỗi lần ở `u` ta quét danh sách kề từ đầu để tìm cạnh unused, cùng cạnh có thể bị xem lại nhiều lần.

Một cách triển khai tuyến tính (linear / 선형) nên giữ:

```text
ptr[u] = vị trí adjacency tiếp theo cần xét
```

hoặc destructively pop các cạnh khỏi cuối danh sách (list / 목록).

Mỗi adjacency mục được advance constant number of times, nên total `O(V+E)`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **13. đồ thị vô hướng cần cạnh ID** tiếp nhận điểm tựa từ **12. cách biểu diễn (representation / 표현) quyết định độ phức tạp (complexity / 복잡도) thật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. JavaScript cách triển khai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. đồ thị vô hướng cần cạnh ID

Mỗi undirected lô-gic (logic / 논리) cạnh thường xuất hiện hai adjacency các mục. Nếu chỉ mark `(u,v)` theo endpoints, các cạnh song song bị nhầm.

Dùng:

```text
edge id
used[id]
```

để đảm bảo mỗi vật lý cạnh consume đúng một lần.

Self-loop cũng cần cạnh ID; trong đồ thị vô hướng nó góp 2 vào degree.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **14. JavaScript cách triển khai** tiếp nhận điểm tựa từ **13. đồ thị vô hướng cần cạnh ID** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Validate đầu ra thay vì chỉ tin thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. JavaScript cách triển khai

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```js
function eulerUndirected(n, edges, start) {
  const g = Array.from({ length: n }, () => []);

  edges.forEach(([u, v], id) => {
    g[u].push([v, id]);
    g[v].push([u, id]);
  });

  const used = Array(edges.length).fill(false);
  const ptr = Array(n).fill(0);
  const stack = [start];
  const path = [];

  while (stack.length) {
    const u = stack[stack.length - 1];

    while (ptr[u] < g[u].length && used[g[u][ptr[u]][1]]) {
      ptr[u]++;
    }

    if (ptr[u] === g[u].length) {
      path.push(stack.pop());
    } else {
      const [v, id] = g[u][ptr[u]++];
      if (used[id]) continue;
      used[id] = true;
      stack.push(v);
    }
  }

  path.reverse();
  return path;
}
```

điều kiện sau mạnh:

```text
path.length == E + 1
```

nếu một Eulerian trail hợp lệ đã dùng hết `E` các cạnh.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **15. Validate đầu ra thay vì chỉ tin thuật toán** tiếp nhận điểm tựa từ **14. JavaScript cách triển khai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Fleury's thuật toán và vì sao Hierholzer tốt hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Validate đầu ra thay vì chỉ tin thuật toán

Một bộ xác minh có thể kiểm tra:

```text
route có E+1 vertices
mỗi bước route tương ứng một edge thật
mỗi edge id dùng đúng một lần
start/end đúng degree conditions
```

Với các cạnh song song, bộ xác minh cũng phải match cạnh identities, không chỉ endpoint pairs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **16. Fleury's thuật toán và vì sao Hierholzer tốt hơn** tiếp nhận điểm tựa từ **15. Validate đầu ra thay vì chỉ tin thuật toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Eulerian đồ thị và Bridges** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Fleury's thuật toán và vì sao Hierholzer tốt hơn

Fleury chọn cạnh không phải cầu nối (bridge / 브리지) nếu còn lựa chọn khác. Conceptually đẹp vì cố tránh làm phần đồ thị còn lại disconnect.

Nếu ở mỗi bước đều phải tính lại cầu, cách làm đơn giản sẽ có độ phức tạp cao. Hierholzer đạt thời gian tuyến tính mà không cần phát hiện cầu động.

Bài học: một quy tắc tham lam trực quan chưa chắc là cách triển khai tốt nhất dù tính đúng đắn dễ hình dung.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **17. Eulerian đồ thị và Bridges** tiếp nhận điểm tựa từ **16. Fleury's thuật toán và vì sao Hierholzer tốt hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Eulerization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Eulerian đồ thị và Bridges

Trong một connected Eulerian đồ thị có các cạnh, mọi cạnh nằm trên một chu trình của Euler tour, nên không cạnh nào là cầu nối (bridge / 브리지).

Nếu đồ thị có cầu nối (bridge / 브리지), đi qua cầu nối (bridge / 브리지) sang một region rồi muốn quay lại sẽ cần dùng cầu nối (bridge / 브리지) lần hai, trừ open trail endpoint cấu trúc (structure / 구조) rất đặc biệt. Parity/chu trình perspective giải thích mối liên hệ này.

đồ thị các tính chất không tồn tại độc lập; cầu nối (bridge / 브리지)/chu trình/degree các ràng buộc tương tác với nhau.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **18. Eulerization** tiếp nhận điểm tựa từ **17. Eulerian đồ thị và Bridges** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Chinese Postman bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Eulerization

Nếu đồ thị chưa Eulerian nhưng muốn tuyến (route / 경로) qua mọi cạnh, ta có thể thêm/phần tử trùng các cạnh để làm odd-degree các đỉnh trở thành even.

Trong đồ thị vô hướng, số odd các đỉnh luôn chẵn. Bài toán chọn pairs odd các đỉnh để phần tử trùng các đường đi ngắn nhất tối ưu dẫn tới **Chinese Postman bài toán (problem / 문제)**.

Eulerian tour là building khối (block / 블록) sau khi đồ thị được Eulerize.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **19. Chinese Postman bài toán (problem / 문제)** tiếp nhận điểm tựa từ **18. Eulerization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. De Bruijn đồ thị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Chinese Postman bài toán (problem / 문제)

Mục tiêu (objective / 목표):

> Đi qua mọi cạnh ít nhất một lần với tổng chi phí nhỏ nhất.

Nếu đồ thị Eulerian, answer là Euler tour trực tiếp.

Nếu không, phải phần tử trùng một số routes sao cho mọi degree trở thành chẵn với extra chi phí nhỏ nhất. Weighted phiên bản (version / 버전) liên quan các đường đi ngắn nhất + minimum-weight matching trên odd các đỉnh.

Đây là ví dụ rõ về cách một theorem structural trở thành thành phần nguyên thủy (primitive / 기본 요소) của tối ưu hóa (optimization / 최적화) bài toán (problem / 문제) lớn hơn.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **20. De Bruijn đồ thị** tiếp nhận điểm tựa từ **19. Chinese Postman bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. De Bruijn chuỗi (sequence / 시퀀스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. De Bruijn đồ thị

K-mers/string fragments có thể được mô hình:

```text
vertex = prefix/suffix length k-1
edge   = k-mer
```

Một Eulerian đường đi qua mọi fragment cạnh reconstruct chuỗi (sequence / 시퀀스) sử dụng mọi k-mer đúng một lần theo mô hình.

Liên kết (connection / 연결) này xuất hiện trong lắp ráp bộ gen intuition và de Bruijn xây dựng chuỗi.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **20. De Bruijn đồ thị** xác định đầu vào; **21. De Bruijn chuỗi (sequence / 시퀀스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **22. Itinerary Reconstruction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. De Bruijn chuỗi (sequence / 시퀀스)

Muốn chuỗi (sequence / 시퀀스) chứa mọi string length `k` trên alphabet đúng một lần theo cyclic cửa sổ (window / 윈도우), xây đồ thị:

```text
vertices = strings length k-1
edges = strings length k
```

Chu trình Euler đi qua mỗi cạnh đúng một lần; nếu đọc nhãn theo đường đi, ta có thể xây dựng dãy de Bruijn.

Một bài toán (problem / 문제) string tưởng rất khác lại trở thành edge-covering đồ thị bài toán (problem / 문제).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **21. De Bruijn chuỗi (sequence / 시퀀스)** xác định đầu vào; **22. Itinerary Reconstruction** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **23. Lexicographically smallest Eulerian trail** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Itinerary Reconstruction

Một family bài phổ biến: tickets là directed các cạnh, cần dùng tất cả tickets một lần và đôi khi chọn lexical-smallest hợp lệ itinerary.

đồ thị có thể có các cạnh song song. Hierholzer vẫn là cốt lõi (core / 핵심), nhưng adjacency cần thứ tự (ordering / 순서) phù hợp — thường sort reverse rồi pop cuối hoặc dùng hàng đợi ưu tiên.

Độ phức tạp (complexity / 복잡도) lúc này thêm sorting:

\[
O(E\log E)
\]

hoặc sum per-vertex sort các chi phí.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **23. Lexicographically smallest Eulerian trail** tiếp nhận điểm tựa từ **22. Itinerary Reconstruction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Euler Tour trên cây là khái niệm khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Lexicographically smallest Eulerian trail

Nếu nhiều hợp lệ trails, muốn lexical-smallest tuyến (route / 경로) cần định nghĩa thứ tự (order / 순서) của outgoing các cạnh.

Một cách là sort adjacency và Hierholzer luôn consume smallest cạnh. Nhưng phải lập luận (reasoning / 추론) cẩn thận về đầu ra reversal; cách triển khai thường sort descending và pop smallest-from-end hoặc dùng đống nhỏ nhất.

quy tắc phân xử khi bằng nhau là thêm đầu ra ràng buộc, nên mô hình chi phí khác pure Eulerian existence.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **24. Euler Tour trên cây là khái niệm khác** tiếp nhận điểm tựa từ **23. Lexicographically smallest Eulerian trail** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Directed cạnh labels và phần tử trùng tickets** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Euler Tour trên cây là khái niệm khác

Trong các thuật toán trên cây, “Euler tour” thường là dãy DFS ghi lại thời điểm vào/ra mỗi nút để làm phẳng cây con hoặc giải bài toán LCA/RMQ.

Nó không nhất thiết là Eulerian trail “mỗi cạnh đúng một lần”. Một cây DFS đi xuống và quay lên thường traverse vật lý cạnh hai lần.

Tên giống nhau nhưng sự trừu tượng khác; hãy nhìn definition.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **24. Euler Tour trên cây là khái niệm khác** cho ta quy tắc; **25. Directed cạnh labels và phần tử trùng tickets** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **26. rỗng đồ thị và degenerate cases** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Directed cạnh labels và phần tử trùng tickets

Nếu two các cạnh có cùng `(u,v)` nhưng đại diện hai tickets/items khác nhau, dùng endpoint pair làm khóa có thể gộp nhầm. cạnh ID hoặc multiset count là bắt buộc.

Nếu chỉ cần tuyến (route / 경로) các đỉnh, count cách biểu diễn có thể gọn hơn tường minh (explicit / 명시적) cạnh đối tượng khi rất nhiều phần tử trùng các cạnh.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **25. Directed cạnh labels và phần tử trùng tickets** cho ta quy tắc; **26. rỗng đồ thị và degenerate cases** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **27. độ phức tạp (complexity / 복잡도) theo đầu ra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. rỗng đồ thị và degenerate cases

đồ thị không có cạnh có thể được coi là Eulerian một cách trivial tùy definition/API. tuyến (route / 경로) có thể là rỗng hoặc một chosen đỉnh.

Một khuyên đơn tự nó đã tạo thành chu trình Euler. Hai cạnh song song giữa hai đỉnh tạo một chu trình độ dài 2 theo ngữ nghĩa của đa đồ thị.

các trường hợp góc (corner cases) cần được định nghĩa trước, không để cách triển khai vô tình quyết định ngữ nghĩa.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **26. rỗng đồ thị và degenerate cases** cho ta quy tắc; **27. độ phức tạp (complexity / 복잡도) theo đầu ra** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **28. bộ nhớ bố trí và destructive traversal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. độ phức tạp (complexity / 복잡도) theo đầu ra

Euler trail đầu ra có `E+1` các đỉnh/cạnh identifiers, nên riêng việc emit lời giải đã cần `Ω(E)`.

Hierholzer `O(V+E)` vì thế asymptotically optimal theo đầu vào/kích thước đầu ra trong adjacency cách biểu diễn thông thường.

Đây là ví dụ đẹp của nhạy theo kích thước đầu ra cận dưới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **28. bộ nhớ bố trí và destructive traversal** tiếp nhận điểm tựa từ **27. độ phức tạp (complexity / 복잡도) theo đầu ra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. xử lý luồng/trực tuyến limitation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. bộ nhớ bố trí và destructive traversal

Nếu thuật toán được phép phá adjacency lists, có thể `pop()` các cạnh để giảm extra `ptr[]`. Nhưng hàm gọi sẽ mất đồ thị original.

Non-destructive cách triển khai giữ `ptr`/used trạng thái (state / 상태). Đây là sự đánh đổi (trade-off / 트레이드오프) sự thay đổi dữ liệu đặc tả hợp đồng (contract / 계약) vs extra bộ nhớ.

Trong C/JavaScript, destructive pop cuối thường thân thiện với bộ nhớ đệm và đơn giản; trong dùng chung (shared / 공유) đồ thị cấu trúc (structure / 구조), bản sao (copy / 복사) toàn đồ thị có thể đắt hơn một con trỏ mảng.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **28. bộ nhớ bố trí và destructive traversal** đã nêu tiêu chí phân biệt, còn **29. xử lý luồng/trực tuyến limitation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **30. kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. xử lý luồng/trực tuyến limitation

Eulerian trail là toàn cục tính chất. Nếu các cạnh arrive trực tuyến và ta phải đầu ra tuyến (route / 경로) ngay mà không biết tương lai các cạnh, cục bộ choice có thể không đủ vì tương lai degree/connectivity chưa biết.

tĩnh Hierholzer giả định đồ thị đã biết. động Eulerian maintenance là bài toán (problem / 문제) khác, thường cần maintain degree parity/connectivity và chưa chắc cho phép emit final tuyến (route / 경로) incrementally đơn giản.

> **Chuyển mạch:** Ở chặng này của **Eulerian các đường đi và các chu trình**, **29. xử lý luồng/trực tuyến limitation** đã nêu tiêu chí phân biệt, còn **30. kiểm thử** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **31. Phổ biến cách triển khai failures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. kiểm thử

Kiểm thử (test / 테스트) families:

```text
simple cycle
path graph with exactly 2 odd vertices
star with >2 odd vertices -> impossible
disconnected even-degree components -> impossible
parallel edges
self-loops
directed balanced cycle
directed open trail
duplicate tickets
empty graph
```

Trên đồ thị nhỏ, brute-force quay lui (backtracking) over cạnh IDs có thể làm oracle để verify existence/đường đi của Hierholzer.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Eulerian các đường đi và các chu trình**, **31. Phổ biến cách triển khai failures** tiếp nhận điểm tựa từ **30. kiểm thử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Phổ biến cách triển khai failures

Các lỗi điển hình:

```text
quên connectivity check
start sai
mark adjacency entry thay vì physical edge
không hỗ trợ parallel edges
shift() đầu JS array gây cost xấu
output không reverse
không verify E edges đã dùng
nhầm Eulerian với Hamiltonian
```

Một cách triển khai trả tuyến (route / 경로) ngắn hơn `E+1` thường là dấu hiệu đồ thị không thỏa các giả định hoặc traversal bỏ sót thành phần/cạnh.

> **Chuyển mạch:** Trong **Eulerian các đường đi và các chu trình**, **Mô hình tư duy** gom các mảnh từ **31. Phổ biến cách triển khai failures** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Eulerian lập luận (reasoning / 추론) là **luồng (flow / 흐름) balance của các cạnh qua các đỉnh**. Intermediate đỉnh cần ghép cạnh vào với cạnh ra; đồ thị vô hướng biểu hiện bằng parity, đồ thị có hướng biểu hiện bằng cân bằng bậc vào/bậc ra.

Khi balance + connectivity đúng, Hierholzer biến cục bộ cạnh consumption thành toàn cục tuyến (route / 경로) bằng reverse finishing/splicing. Đây là lý do Eulerian problems có linear-time cấu trúc (structure / 구조) đẹp trong khi các bài Hamilton đi qua đỉnh không có cùng tính chất.

Xem thêm: [Graph Modeling](./00_graph_modeling_and_representation.md), [Bridges](./06_bridges_articulation_and_biconnectivity.md), [Network Flow](./08_network_flow_and_matching.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
