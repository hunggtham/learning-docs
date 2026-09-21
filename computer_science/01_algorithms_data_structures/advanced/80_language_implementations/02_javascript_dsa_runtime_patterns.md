# Các mẫu DSA và môi trường chạy JavaScript
**JavaScript DSA & Runtime Patterns / JavaScript 자료구조와 런타임 패턴**

JavaScript cho phép triển khai thuật toán và cấu trúc dữ liệu rất nhanh, nhưng cùng một thuật toán có thể có những điểm cần lưu ý khác C hoặc Java. Nguyên nhân đến từ kiểu `Number`, mảng động, định danh đối tượng, bộ thu gom rác, chuỗi UTF-16 và hành vi của môi trường JIT.

Mô hình tư duy cần giữ là:

> **Bất biến thuật toán (algorithmic invariant)** không đổi theo ngôn ngữ, nhưng ngữ nghĩa của cách biểu diễn dữ liệu và mô hình chi phí của môi trường chạy có thể thay đổi.

Vì vậy, học DSA bằng JavaScript không chỉ là chuyển cú pháp từ Java hoặc C. Cần hiểu những ranh giới của môi trường chạy có thể làm một giả định vốn đúng ở ngôn ngữ khác trở nên sai.

## `Number` và độ chính xác số nguyên

JavaScript `Number` dùng số dấu phẩy động IEEE-754 dạng double. Số nguyên chỉ được biểu diễn chính xác trong miền an toàn đến:

\[
2^{53}-1
\]

```js
Number.MAX_SAFE_INTEGER
```

Nếu tổng tiền tố, khoảng cách đường đi, số tổ hợp hoặc ID có thể vượt miền số nguyên an toàn, kết quả có thể mất độ chính xác dù không xuất hiện kiểu tràn số cố định như `int32` hoặc `int64`.

```js
Number.MAX_SAFE_INTEGER + 1 === Number.MAX_SAFE_INTEGER + 2
```

Biểu thức trên minh họa việc hai số nguyên toán học khác nhau có thể không còn được phân biệt chính xác bằng `Number`.

## `BigInt`

`BigInt` hỗ trợ số nguyên có độ lớn tùy ý:

```js
const x = 12345678901234567890n;
```

Không được trộn trực tiếp phép toán số học giữa `BigInt` và `Number`:

```js
1n + 1 // TypeError
```

Khi sắp xếp `BigInt`, nên dùng so sánh quan hệ:

```js
(a, b) => a < b ? -1 : a > b ? 1 : 0
```

thay vì dựa vào `a - b`.

## `Infinity` và `BigInt`

`Infinity` là giá trị canh gác thuận tiện cho thuật toán đường đi ngắn nhất dùng `Number`:

```js
const dist = Array(n).fill(Infinity);
```

`BigInt` không có giá trị `Infinity`. Nếu khoảng cách dùng `BigInt`, cần chọn cách biểu diễn rõ ràng như `null`, `undefined`, một cờ `reachable` riêng hoặc một cận trên `BigInt` đã biết chắc là đủ lớn.

Lựa chọn giá trị canh gác là một phần của **cách biểu diễn (representation)**, không chỉ là chi tiết cú pháp.

## Mảng JavaScript không phải mảng C

JavaScript `Array` có độ dài động và có thể chứa nhiều loại giá trị:

```js
const a = [];
a.push(1);
a.push(2);
```

Các engine thường tối ưu tốt mảng dày đặc có kiểu phần tử ổn định, nhưng mảng thưa hoặc trộn nhiều kiểu có thể được biểu diễn khác. Không nên giả định mỗi phần tử luôn nằm trong một ô nhớ liên tiếp giống `double[]` của C.

## Mảng dày đặc, mảng thưa và lỗ trống

```js
const a = [];
a[1_000_000] = 1;
```

`a.length` trở thành `1_000_001` dù chỉ có một phần tử được gán. Engine có thể chuyển sang cách biểu diễn phù hợp với mảng thưa.

Ngoài ra:

```js
const a = new Array(3);                 // có 3 lỗ trống
const b = [undefined, undefined, undefined]; // có 3 phần tử thật
```

Lỗ trống (hole) và phần tử có giá trị `undefined` không hoàn toàn giống nhau đối với mọi phương thức mảng. Nếu cần vùng lưu trữ số đã khởi tạo, dùng:

```js
Array(n).fill(0)
```

hoặc một `TypedArray` phù hợp.

## Dùng mảng làm ngăn xếp

Mảng rất tự nhiên khi dùng làm ngăn xếp:

```js
stack.push(x);
stack.pop();
```

Các thao tác ở cuối mảng thường phù hợp với mô hình này.

## Hàng đợi và `shift()`

Gọi `shift()` lặp lại trên hàng đợi lớn có thể phát sinh chi phí di chuyển, đánh lại chỉ số hoặc xử lý nội bộ tùy engine. Với BFS, mẫu dùng chỉ số đầu thường dễ dự đoán hơn:

```js
const q = [];
let head = 0;

q.push(start);
while (head < q.length) {
  const u = q[head++];
}
```

Nếu hàng đợi tồn tại lâu và phần tiền tố đã xử lý giữ nhiều tham chiếu không cần thiết, có thể nén theo một ngưỡng hợp lý:

```js
if (head > 4096 && head * 2 > q.length) {
  q.splice(0, head);
  head = 0;
}
```

Không cần nén sau mỗi lần lấy phần tử khỏi hàng đợi.

## Deque tự cài đặt

Nếu thường xuyên thêm và lấy ở cả hai đầu, nên cân nhắc bộ đệm vòng (ring buffer) thay vì dựa vào `shift()` và `unshift()`.

Một deque dạng vòng thường duy trì:

```text
buffer
head
tail
size
capacity
```

Khi đầy, có thể tăng dung lượng tương tự mảng động rồi sao chép theo thứ tự logic.

## `Object` và `Map`

Đối tượng thông thường:

```js
const obj = {};
```

có ngữ nghĩa thuộc tính, chuỗi prototype và quy tắc chuyển đổi khóa riêng. `Map` hỗ trợ khóa với nhiều kiểu và so sánh khóa theo ngữ nghĩa phù hợp hơn cho ánh xạ tổng quát:

```js
const map = new Map();
map.set(objectKey, value);
```

Với bài toán DSA cần từ điển hoặc bảng ánh xạ tổng quát, `Map` thường thể hiện ý định rõ hơn.

## Chuyển đổi khóa của `Object`

```js
const o = {};
o[1] = 'a';
o['1'] = 'b';
```

Hai phép truy cập trên cùng liên quan đến khóa chuỗi `"1"`. Nếu miền bài toán cần phân biệt kiểu khóa, `Map` an toàn và rõ nghĩa hơn.

Đối tượng thông thường còn có chuỗi prototype. Có thể tạo từ điển không prototype bằng:

```js
const dict = Object.create(null);
```

nhưng `Map` vẫn thường là lựa chọn dễ hiểu hơn cho cấu trúc ánh xạ thuật toán.

## Định danh đối tượng trong `Map`

```js
const m = new Map();
m.set({x: 1}, 'value');
console.log(m.get({x: 1})); // undefined
```

Hai object literal có cùng trường và giá trị vẫn là hai đối tượng khác nhau. `Map` không tự so sánh sâu theo nội dung.

Với trạng thái `(x, y, mask)`, có thể:

```text
mã hóa thành số nguyên
mã hóa thành chuỗi
dùng Map lồng nhau
chuẩn hóa thành một đối tượng dùng chung
```

Không nên tạo một object mới rồi kỳ vọng nó bằng một object cũ chỉ vì các trường giống nhau.

## Mã hóa trạng thái chuẩn

Nếu miền giá trị nhỏ và chắc chắn không vượt giới hạn toán tử bit:

```js
const key = ((x * width + y) << bits) | mask;
```

Tuy nhiên, toán tử bit của `Number` dùng ngữ nghĩa 32 bit. Với miền tổng quát hơn, có thể dùng:

```js
const key = `${x},${y},${mask}`;
```

Khóa chuỗi đơn giản nhưng phát sinh cấp phát và chi phí băm. Nếu các cận kích thước đã biết, mảng nhiều chiều hoặc `TypedArray` có thể hiệu quả hơn.

## `Set` và mảng đánh dấu

`Set` là lựa chọn mặc định tốt cho tập đã thăm khi khóa không phải ID số nguyên dày đặc:

```js
const seen = new Set();
seen.add(key);
if (seen.has(key)) { /* ... */ }
```

Nếu đỉnh là các số nguyên liên tiếp `0..n-1`, một mảng đánh dấu thường gọn hơn:

```js
const seen = new Uint8Array(n);
seen[v] = 1;
```

Đây là ví dụ điển hình về việc chọn cấu trúc theo **miền khóa**, không chỉ theo tên thao tác “membership”.

## `TypedArray`

Các kiểu thường dùng:

```text
Int32Array
Uint32Array
Float64Array
BigInt64Array
BigUint64Array
```

Ưu điểm chính là độ dài cố định, vùng lưu trữ số gọn, quy tắc chuyển đổi dễ dự đoán hơn và khả năng làm việc với dữ liệu nhị phân. Đổi lại, chúng không hỗ trợ `push/pop` như mảng động và mỗi kiểu có miền giá trị cố định.

## Tràn số và chuyển đổi trong `TypedArray`

Gán một `Number` lớn vào `Int32Array` sẽ chuyển giá trị theo ngữ nghĩa số nguyên 32 bit. Nếu khoảng cách của Dijkstra có thể vượt `2^31-1`, `Int32Array` có thể làm sai kết quả dù phép toán bằng `Number` ban đầu vẫn chính xác.

Khi cần miền số của `Number`, có thể dùng `Float64Array`:

```js
const dist = new Float64Array(n);
dist.fill(Infinity);
```

`Uint8Array` rất phù hợp với cờ hoặc trạng thái nhỏ:

```js
const state = new Uint8Array(n);
// 0 = chưa thăm, 1 = đang thăm, 2 = hoàn tất
```

`BigInt64Array` và `BigUint64Array` chứa số nguyên 64 bit; chúng không có miền vô hạn như `BigInt` độc lập.

## Toán tử bit dùng 32 bit

Các toán tử bit trên `Number` chuyển toán hạng sang số nguyên 32 bit. Vì vậy:

```js
1 << 31
```

có hành vi số có dấu 32 bit. Một mặt nạ cần hơn khoảng 31 bit hữu dụng phải được thiết kế cẩn thận. `BigInt` có toán tử bit riêng:

```js
1n << 60n
```

nhưng toàn bộ phép toán và cấu trúc liên quan phải nhất quán với `BigInt`.

Mẫu:

```js
x >>> 0
```

chuyển về `Number` không dấu 32 bit. Nó hữu ích trong một số thao tác băm hoặc bit, nhưng sẽ cắt bỏ các bit cao và không phải cách tổng quát để “biến số thành số dương”.

## Sắp xếp số

`Array.prototype.sort()` mặc định không nên được dùng để suy ra thứ tự số tăng dần:

```js
[2, 10, 3].sort()
```

Với `Number`, dùng:

```js
arr.sort((a, b) => a - b);
```

Với `BigInt`, dùng so sánh quan hệ:

```js
arr.sort((a, b) => a < b ? -1 : a > b ? 1 : 0);
```

ECMAScript hiện đại quy định `Array.prototype.sort()` là ổn định (stable). Nếu phải hỗ trợ môi trường cũ hoặc không chuẩn, cần kiểm tra môi trường đích thay vì giả định.

## Hàng đợi ưu tiên

Thư viện chuẩn JavaScript không cung cấp một `PriorityQueue` tổng quát giống Java. Mã DSA thường tự cài đặt heap nhị phân:

```js
class MinHeap {
  constructor(compare = (a, b) => a - b) {
    this.a = [];
    this.compare = compare;
  }

  push(x) { /* sift up */ }
  pop() { /* đổi root với phần tử cuối rồi sift down */ }
  peek() { return this.a[0]; }
}
```

Hàm so sánh phải nhất quán và có tính bắc cầu.

## Cấp phát đối tượng trong heap

Dijkstra viết theo kiểu:

```js
heap.push({ node: v, dist: nd });
```

rất dễ đọc nhưng có thể tạo nhiều đối tượng tạm thời. Nếu đo đạc cho thấy cấp phát hoặc GC là nút thắt, có thể cân nhắc mảng song song, tuple nhỏ, trạng thái mã hóa hoặc heap theo kiểu **struct-of-arrays**.

Không nên làm mã nguồn phức tạp trước khi có số liệu đo cho thấy điều đó cần thiết.

## Dijkstra với phần tử cũ trong heap

Heap tự cài đặt thường không có `decrease-key`. Một mẫu đơn giản là chèn khoảng cách mới:

```js
heap.push([newDist, v]);
```

và khi lấy ra, bỏ qua phần tử đã cũ:

```js
if (d !== dist[v]) continue;
```

Mẫu này đơn giản, dễ kiểm chứng và thường đủ tốt.

## Độ sâu đệ quy

DFS hoặc quay lui (backtracking) đệ quy có thể vượt ngăn xếp lời gọi. Giới hạn cụ thể không phải một hằng số di động giữa các trình duyệt, phiên bản Node.js hoặc engine.

Với cây hoặc đồ thị có thể rất sâu, nên chuyển sang ngăn xếp tường minh:

```js
const stack = [start];
while (stack.length) {
  const u = stack.pop();
  // xử lý u
}
```

Không nên dựa vào tối ưu lời gọi đuôi như một bảo đảm an toàn ngăn xếp cho mã DSA phổ thông.

## `async` không thay thế thuật toán dạng lặp

Chuyển một DFS sâu sang `Promise` hoặc `async` làm thay đổi cách lập lịch và tạo thêm chi phí cấp phát. Đây không phải giải pháp tổng quát thay cho việc dùng ngăn xếp tường minh.

Tương tự, `await Promise.resolve()` chỉ chuyển việc tiếp tục sang hàng đợi microtask; nếu lặp không hợp lý, nó vẫn có thể làm các giai đoạn khác của event loop bị đói.

**Lập lịch bất đồng bộ không sửa được lựa chọn thuật toán sai.**

## Event loop và thuật toán chạy lâu

Trong trình duyệt và trong nhiều ngữ cảnh Node.js, mã JavaScript của người dùng chạy trên luồng gắn với event loop. Một vòng lặp `O(n²)` dài có thể làm giao diện hoặc xử lý sự kiện bị chặn.

Khi công việc CPU lớn, có thể cân nhắc:

```text
chia nhỏ công việc và chủ động nhường quyền thực thi
Web Worker
worker_threads
native code / WebAssembly
```

Thiết kế xử lý đồng thời là một vấn đề riêng; nó không thay đổi độ phức tạp cơ bản của thuật toán.

## Bộ thu gom rác và vòng đời dữ liệu

GC thu hồi đối tượng không còn đạt tới được, nhưng `Map`, `Set`, bộ nhớ đệm, closure, listener và timer có thể giữ tham chiếu sống lâu hơn dự kiến.

```js
const cache = new Map();
```

Nếu bộ nhớ đệm trên không có chính sách giới hạn hoặc loại bỏ, nó có thể trở thành rò rỉ bộ nhớ ở cấp logic.

GC tự động không có nghĩa là vòng đời bộ nhớ không cần được thiết kế.

## `WeakMap` và `WeakSet`

`WeakMap` hữu ích khi cần gắn siêu dữ liệu với vòng đời của một đối tượng mà không muốn ánh xạ mạnh giữ đối tượng đó sống. Tuy nhiên, nó không hỗ trợ duyệt như `Map`, nên không phù hợp với bảng trạng thái thuật toán cần liệt kê toàn bộ phần tử.

## Closure và giữ tham chiếu

Closure có thể giữ tham chiếu tới mảng hoặc cây lớn ngay cả khi hàm bên ngoài đã trả về. Listener và timer cũng giữ callback cùng trạng thái được bắt giữ.

Nhiều rò rỉ bộ nhớ JavaScript là **rò rỉ do khả năng đạt tới (reachability leak)** chứ không phải lỗi quên `free()` như trong C.

## Hình dạng đối tượng và JIT

Các engine JIT thường có tối ưu nội bộ dựa trên **hình dạng đối tượng (object shape)**. Những đối tượng được tạo với cùng trường và cùng thứ tự thường dễ tối ưu hơn các đối tượng liên tục thêm/xóa trường theo nhiều kiểu khác nhau.

Với bản ghi cố định, nên khởi tạo các trường từ đầu:

```js
const node = { key, left: null, right: null, size: 1 };
```

Chi tiết về hidden class là đặc thù engine; không nên viết mã phụ thuộc vào các ngưỡng nội bộ không được đặc tả.

## `class` và object literal

`class Node` và object literal cuối cùng đều tạo đối tượng JavaScript. `class` giúp thống nhất cách xây dựng và API, nhưng không tự tạo bố trí bộ nhớ gọn giống `struct` của C.

Khi có hàng triệu nút, quyết định dùng mảng, `TypedArray` hay đối tượng thường quan trọng hơn việc chọn cú pháp `class` hay object literal.

## Đồ thị CSR trong JavaScript

Với đồ thị tĩnh có ID đỉnh dày đặc, có thể dùng **CSR (Compressed Sparse Row)** bằng `TypedArray`:

```text
Uint32Array offsets
Uint32Array edges
```

Quá trình xây dựng thường gồm hai lượt:

```text
đếm bậc
prefix sum để tạo offsets
điền danh sách cạnh
```

Cách này giảm chi phí của nhiều object/mảng con và đưa cách biểu diễn JavaScript gần hơn với bố trí dữ liệu kiểu hệ thống.

Với đồ thị vừa phải, danh sách kề vẫn là mặc định dễ đọc:

```js
const g = Array.from({length: n}, () => []);
g[u].push(v);
```

Khi có hàng triệu cạnh, nên đo chi phí của các mảng lồng nhau thay vì mặc định rằng chúng đủ gọn.

## Chuỗi JavaScript dùng UTF-16

Các thao tác:

```js
s.length
s[i]
s.charCodeAt(i)
```

chủ yếu làm việc trên **đơn vị mã UTF-16 (UTF-16 code unit)**. Một ký tự Unicode ngoài BMP có thể chiếm hai code unit:

```js
'😀'.length === 2
```

Thuật toán chuỗi phải xác định rõ đơn vị đang xử lý:

```text
UTF-16 code unit
Unicode code point
cụm tự vị (grapheme cluster)
```

Vòng lặp:

```js
for (const ch of s) {
  // duyệt theo code point theo ngữ nghĩa iterator của chuỗi
}
```

xử lý cặp thay thế tốt hơn truy cập từng code unit, nhưng một ký tự mà người dùng nhìn thấy vẫn có thể gồm nhiều code point. Khi cần phân đoạn theo ký tự hiển thị, có thể dùng `Intl.Segmenter`.

## Chuỗi là bất biến

Chuỗi JavaScript không thay đổi tại chỗ. Engine có thể tối ưu phép nối trong nhiều trường hợp, nhưng khi xây chuỗi lớn, việc gom các đoạn vào mảng rồi `join()` thường là lựa chọn dễ kiểm soát hơn.

Nếu đây là đường chạy nóng, cần đo trên tải công việc thực tế thay vì dựa vào giả định chung.

## Thứ tự duyệt của `Map` và `Object`

`Map` giữ **thứ tự chèn**, nhưng đó không phải thứ tự khóa đã sắp xếp. Nếu thuật toán cần ánh xạ có thứ tự giống `TreeMap`, JavaScript chuẩn không cung cấp sẵn một cây cân bằng tổng quát; có thể cần tự cài đặt hoặc dùng thư viện.

Quy tắc duyệt thuộc tính của `Object` có các nhóm thứ tự được đặc tả, trong đó khóa dạng số nguyên có quy tắc riêng. Không nên dùng object thông thường như một ánh xạ có thứ tự tổng quát chỉ vì một ví dụ nhỏ cho ra thứ tự mong muốn.

Về ngữ nghĩa, `Map` thường rõ ràng hơn khi mục tiêu thực sự là một ánh xạ.

## Trạng thái dày đặc và trạng thái thưa

Khóa chuỗi:

```js
const key = `${r}|${c}|${mask}`;
```

đơn giản nhưng tạo chuỗi mới. Nếu các cận nhỏ và biết trước, có thể cấp phát trạng thái dày đặc:

```js
const seen = Array.from({length: rows}, () =>
  Array.from({length: cols}, () => new Uint8Array(1 << k))
);
```

Tuy nhiên kích thước có thể tăng rất nhanh. Với không gian trạng thái thưa, `Map` hoặc `Set` dùng khóa chuẩn hóa bằng chuỗi hay `BigInt` có thể tiết kiệm bộ nhớ hơn.

Đây chính là sự đánh đổi **thưa–dày (sparse–dense)** quen thuộc trong quy hoạch động và biểu diễn đồ thị.

## `NaN`, `-0` và số dấu phẩy động

`NaN` có ngữ nghĩa đặc biệt:

```js
NaN === NaN // false
```

`Map` và `Set` dùng ngữ nghĩa kiểu SameValueZero, nên cách `NaN` làm khóa không hoàn toàn giống trực giác dựa trên `===`. Thuật toán số nên tránh để `NaN` xuất hiện nếu miền bài toán không định nghĩa rõ ý nghĩa của nó.

JavaScript cũng có `0` và `-0`. Phần lớn phép so sánh và cấu trúc ánh xạ coi chúng tương đương cho mục đích DSA, nhưng đây vẫn là trường hợp biên cần biết trong tính toán số mức thấp.

Tổng số dấu phẩy động có thể tích lũy sai số làm tròn:

```js
0.1 + 0.2 !== 0.3
```

Với tiền tệ, thường nên lưu số nguyên theo đơn vị nhỏ nhất hoặc dùng thư viện số thập phân phù hợp. Tính đúng đắn của thuật toán phụ thuộc vào cách biểu diễn số, không chỉ vào công thức toán học.

## Sắp xếp đối tượng và hàm so sánh

Một hàm so sánh nhiều trường có thể viết:

```js
items.sort((a, b) =>
  a.score !== b.score ? a.score - b.score : a.id - b.id
);
```

Nếu trường có thể vượt miền số nguyên an toàn, nên dùng so sánh quan hệ thay cho phép trừ. Hàm so sánh phải nhất quán và có tính bắc cầu; nếu không, kết quả sắp xếp có thể khó dự đoán.

## Đo hiệu năng trong môi trường JIT

JavaScript JIT có giai đoạn làm nóng, tối ưu theo tầng và có thể mất tối ưu. Một phép đo vi mô nên:

```text
chạy làm nóng trước khi đo
sử dụng hình dạng dữ liệu gần thực tế
thực sự tiêu thụ kết quả để tránh đo công việc vô nghĩa
đo nhiều lần
quan sát cả bộ nhớ và GC
không chỉ so sánh lần chạy lạnh đầu tiên
```

Có thể dùng `performance.now()` hoặc `process.hrtime.bigint()`, nhưng phương pháp đo quan trọng hơn độ phân giải của đồng hồ.

Một benchmark chỉ dùng mảng toàn số có thể không phản ánh hệ thống thực tế nơi dữ liệu trộn số, object và chuỗi. Dữ liệu đo phải gần với tải công việc thật.

## Trình duyệt và Node.js

Ngữ nghĩa ECMAScript cơ bản có thể giống nhau, nhưng phiên bản engine, giới hạn bộ nhớ, cấu hình GC và môi trường thực thi có thể khác. Không nên đưa ra một con số hiệu năng phổ quát cho “JavaScript” mà không nêu rõ môi trường chạy.

## Web Worker và `worker_threads`

Công việc CPU lớn có thể được chuyển sang worker để tránh chặn luồng chính. Tuy nhiên truyền dữ liệu, tuần tự hóa và bộ nhớ dùng chung đều có chi phí.

Xử lý song song chỉ hữu ích khi công việc có thể chia được và phần công việc đủ lớn để bù chi phí phối hợp.

## `SharedArrayBuffer` và `Atomics`

JavaScript có cơ chế đồng thời mức thấp trên bộ nhớ dùng chung. Tuy nhiên, viết cấu trúc dữ liệu không khóa (lock-free) đúng đắn đòi hỏi hiểu thứ tự bộ nhớ và giao thức phối hợp.

Chỉ thêm `Atomics` vào một cấu trúc dữ liệu tùy ý không tự biến nó thành cấu trúc an toàn khi truy cập đồng thời.

## Liên hệ với WebAssembly

Với công việc số học hoặc đồ thị rất nhạy về hiệu năng, C/Rust/WASM có thể cho bố trí bộ nhớ gọn hơn và quyền kiểm soát lớn hơn. Tuy nhiên, chi phí qua ranh giới JavaScript–WebAssembly và chuyển đổi dữ liệu có thể chi phối nếu lời gọi quá nhỏ hoặc quá thường xuyên.

Khi dùng WASM, thường nên gom đủ công việc thành lô trước khi chuyển qua ranh giới môi trường.

## Kiểm thử đối chiếu

JavaScript là ngôn ngữ động, vì vậy kiểm thử dựa trên tính chất và đối chiếu với cách làm đơn giản đặc biệt hữu ích.

Heap:

```text
đưa nhiều giá trị vào heap
lấy lần lượt ra
so sánh với [...values].sort((a, b) => a - b)
```

Đường đi ngắn nhất:

```text
dùng đồ thị nhỏ
so sánh Dijkstra hoặc BFS với Floyd-Warshall làm tham chiếu
```

Thuật toán chuỗi:

```text
so sánh vị trí KMP tìm được với cách kiểm tra ngây thơ
thêm trường hợp Unicode phù hợp với đơn vị chuỗi đã chọn
```

## Kiểm thử dựa trên tính chất

Với tìm kiếm nhị phân tìm cận dưới, kết quả `ans` phải thỏa:

```text
mọi i < ans  : a[i] < target
mọi i >= ans : a[i] >= target
```

Với DSU, phân hoạch liên thông phải tương đương với các thành phần liên thông của đồ thị tham chiếu. Với Segment Tree, có thể sinh ngẫu nhiên cập nhật và truy vấn rồi đối chiếu với mảng xử lý trực tiếp.

Kiểm thử kiểu này thường bắt được lỗi ở ranh giới biểu diễn tốt hơn một vài ví dụ viết tay.

## Phân tích bộ nhớ

Heap snapshot trong Chrome DevTools hoặc công cụ của Node.js có thể cho thấy `Map` còn giữ tham chiếu, cấu trúc nút dùng quá nhiều object hoặc listener/closure giữ dữ liệu ngoài dự kiến.

CPU profile giúp tìm vòng lặp nóng, hàm so sánh tốn kém, thao tác băm hoặc mã hóa chuỗi chiếm nhiều thời gian. Tối ưu nên dựa trên bằng chứng đo được.

## Danh sách kiểm tra cách biểu diễn

```text
ID số nguyên dày đặc?        -> Array / TypedArray
Khóa thưa và tùy ý?          -> Map / Set
Cần hàng đợi?                -> mảng + head index / deque tự cài đặt
Cần hàng đợi ưu tiên?        -> heap tự cài đặt / thư viện phù hợp
Cần bitmask > 32 bit?        -> BigInt hoặc cách biểu diễn khác
Cần số nguyên chính xác >2^53? -> BigInt
Đồ thị tĩnh rất lớn?         -> cân nhắc CSR bằng TypedArray
DFS có thể rất sâu?          -> ngăn xếp dạng lặp
Xử lý Unicode?               -> xác định code unit / code point / grapheme
```

## Mô hình tư duy

> DSA trong JavaScript mạnh nhất khi ta giữ rõ **bất biến thuật toán**, nhưng không giả định môi trường chạy giống C hoặc Java. `Array`, `Map`, `Number`, `BigInt`, `TypedArray` và object đều có ranh giới ngữ nghĩa riêng. Tính đúng đắn trước hết đòi hỏi chọn đúng ngữ nghĩa số, so sánh và chuỗi; hiệu năng sau đó phụ thuộc cách biểu diễn dữ liệu, lượng cấp phát và hành vi của môi trường chạy thực tế.

Khi cách triển khai bắt đầu lớn, hãy tự hỏi:

```text
Miền Number có còn chính xác không?
Toán tử bit có bị ép về 32 bit không?
Khóa trạng thái cần so sánh theo giá trị hay định danh?
Mảng có thực sự dày đặc không?
Đường chạy nóng của hàng đợi có tránh shift/unshift không?
Độ sâu đệ quy có bị chặn không?
Cấp phát object hoặc GC có trở thành nút thắt không?
Kiểu TypedArray có đủ miền giá trị không?
Đơn vị Unicode có đúng với miền bài toán không?
```

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Cross-language Testing](./03_cross_language_testing_and_benchmarking.md).