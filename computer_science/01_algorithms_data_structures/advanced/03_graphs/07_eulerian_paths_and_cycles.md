# Eulerian Paths và Cycles  
**Đường đi Euler và chu trình Euler / 오일러 경로와 회로**

Eulerian problem hỏi về **edges**, không phải vertices: có thể đi qua mỗi edge đúng một lần không?

Đây khác Hamiltonian path, nơi mỗi vertex được thăm đúng một lần. Hai bài có độ khó tính toán rất khác; đừng nhầm vì hình thức giống nhau.

## Undirected graph condition

Bỏ qua isolated vertices, graph cần connected trong phần có edge.

Eulerian cycle tồn tại khi mọi vertex có degree chẵn.

Eulerian path nhưng không cycle tồn tại khi đúng hai vertices có degree lẻ; chúng sẽ là endpoints.

Intuition: mỗi lần đi vào một vertex trung gian qua một edge, ta cần một edge khác để đi ra. Edges tại intermediate vertex ghép thành pairs, nên degree phải chẵn. Endpoints được phép thiếu một pair nên degree lẻ.

## Directed graph condition

Eulerian cycle cần mỗi relevant vertex có:

```text
indegree == outdegree
```

và connectivity phù hợp.

Eulerian path có thể có một start với `outdegree = indegree + 1` và một end với `indegree = outdegree + 1`; các vertex khác cân bằng.

## Hierholzer's algorithm

Bắt đầu đi theo unused edges cho tới khi mắc kẹt. Nếu graph thỏa Euler condition, ta tạo cycle/path cục bộ. Nếu còn unused edges gắn với vertex đã có trong route, tiếp tục một tour mới từ đó rồi splice vào route.

Implementation thường dùng stack và remove/mark edges; complexity tuyến tính:

\[
O(V+E)
\]

nếu edge access được tổ chức đúng.

### JavaScript sketch

```js
function euler(start, g) {
  const stack = [start];
  const path = [];

  while (stack.length) {
    const u = stack[stack.length - 1];

    while (g[u].length && g[u][g[u].length - 1].used) {
      g[u].pop();
    }

    if (!g[u].length) {
      path.push(stack.pop());
    } else {
      const e = g[u].pop();
      if (e.used) continue;
      e.used = true;
      e.rev.used = true;
      stack.push(e.to);
    }
  }

  return path.reverse();
}
```

Thực tế nên dùng edge ids thay vì mutual object references nếu muốn representation đơn giản hơn.

## Connection thực tế

Euler tours xuất hiện trong route planning với requirement dùng mỗi road/edge một lần, DNA assembly historical models, de Bruijn graphs và một số transformations của tree/graph problems.

## Mental Model

> Eulerian reasoning là về **pairing edge entrances và exits** tại mỗi vertex. Degree parity/balance xuất hiện vì flow qua vertex phải vào-ra thành cặp, trừ endpoints.
