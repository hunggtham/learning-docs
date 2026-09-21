# Trie và các cấu trúc chỉ mục tiền tố
**Trie / Prefix Tree / 트라이·접두사 트리**

Trie tổ chức khóa theo **các thành phần cấu tạo nên khóa**, thường là ký tự, byte hoặc bit. Nếu nhiều khóa chia sẻ cùng tiền tố, phần tiền tố chung chỉ được biểu diễn một lần dưới dạng đường đi chung.

Ví dụ `car`, `card`, `care`, `cat`:

```text
(root)
  |
  c
  |
  a
 / \
r*  t*
|\
d* e*
```

Dấu `*` biểu diễn một khóa kết thúc tại nút đó. Một nút trong Trie không nhất thiết là một khóa hoàn chỉnh; nó đại diện cho một **trạng thái tiền tố**.

Mô hình tư duy cốt lõi:

> Hash Table quan tâm định danh của toàn khóa. Trie giữ lại cấu trúc bên trong khóa để biến prefix thành một trạng thái có thể truy vấn trực tiếp.

## 1. Khi nào Trie đáng dùng?

Trie tự nhiên với các truy vấn:

```text
khóa có tồn tại chính xác không?
có khóa nào bắt đầu bằng prefix p không?
có bao nhiêu khóa bắt đầu bằng p?
liệt kê/top-k khóa có prefix p
longest-prefix match
maximum XOR theo bit
multi-pattern matching khi mở rộng thành automaton
```

Nếu chỉ cần exact lookup và không khai thác prefix, Hash Map thường đơn giản và tiết kiệm bộ nhớ hơn.

## 2. Search và Insert

Với khóa dài `L`, đi từ gốc qua từng symbol.

Nếu child tương ứng chưa tồn tại khi insert, tạo child mới. Sau symbol cuối, đánh dấu `isEnd` hoặc tăng `endCount`.

Exact search cần hai điều kiện:

```text
đường đi tồn tại
nút cuối là điểm kết thúc khóa
```

Nếu đường đi tồn tại nhưng `isEnd=false`, đầu vào chỉ là prefix của khóa dài hơn.

Nếu lookup child gần `O(1)`, complexity thường:

\[
O(L)
\]

phụ thuộc độ dài khóa hơn là số lượng khóa trong dictionary.

## 3. Prefix Query

Để kiểm tra `startsWith(prefix)`, chỉ cần đi hết prefix. Không cần nút cuối là `isEnd`.

Nếu cần liệt kê mọi kết quả, complexity phải tính cả output:

\[
O(|prefix| + k + \text{characters emitted})
\]

với `k` là số kết quả.

Một hệ thống autocomplete không thể trả một triệu gợi ý trong `O(|prefix|)` chỉ vì Trie tìm prefix nhanh.

## 4. Bất biến quan trọng

Một Trie mutable thường cần giữ:

```text
mỗi path từ root tương ứng đúng một prefix
mọi key tồn tại có đúng một terminal marker/count
child mapping không chứa duplicate symbol
passCount/endCount nếu có phải nhất quán với subtree
```

Nếu hỗ trợ duplicate keys, `endCount` tốt hơn `boolean isEnd`.

Nếu lưu `passCount`, insert/delete phải cập nhật mọi nút trên path. Metadata tăng tốc query nhưng tạo thêm invariant cần bảo trì.

## 5. Child Representation

Mỗi nút cần ánh xạ:

```text
symbol -> child
```

Các cách phổ biến:

### Mảng cố định

Phù hợp alphabet nhỏ, ví dụ 26 chữ thường.

Ưu điểm:

```text
lookup trực tiếp
layout dễ đoán
không cần hash
```

Nhược điểm: mỗi node trả chi phí cho toàn alphabet dù chỉ có 1–2 child.

### Hash Map

Phù hợp alphabet lớn/thưa. Tiết kiệm slot null nhưng tăng object/hash overhead.

### Sorted small vector

Nếu branching factor thường nhỏ, một vector cặp `(symbol, child)` đã sắp xếp có thể cache-friendly hơn Hash Map. Có thể linear scan với vài child hoặc binary search khi nhiều hơn.

Representation nên dựa trên phân phối branching thực tế.

## 6. Bộ nhớ là điểm yếu lớn của Trie ngây thơ

Số node có thể gần tổng độ dài mọi key:

\[
O\left(\sum |key_i|\right)
\]

Nếu mỗi node là object Java chứa một HashMap riêng, overhead có thể lớn hơn dữ liệu ký tự nhiều lần.

JavaScript `Map` per node cũng tạo áp lực GC. Trong C, mảng 256 pointer trên mỗi node cực lãng phí nếu branching thưa.

Do đó production Trie thường dùng:

```text
path compression
compact node layout
arena/pool allocation
double-array trie
LOUDS / succinct representation
FST/automaton compression
```

## 7. Delete

Xóa `car` khi vẫn còn `card` không được giải phóng toàn path `c-a-r`.

Quy trình:

1. đi tới terminal;
2. giảm `endCount` hoặc clear `isEnd`;
3. đi ngược lên;
4. chỉ xóa node nếu không còn child, không còn key kết thúc và metadata cho phép.

Nếu có `passCount`, node có thể được thu hồi khi count xuống 0.

Delete là nơi shared-prefix ownership trở nên rõ nhất.

## 8. Lexicographic Traversal

Nếu child được duyệt theo symbol order, DFS xuất key theo thứ tự từ điển.

Nếu child dùng Hash Map, iteration order có thể không tương ứng lexicographic order; cần sort symbol hoặc dùng ordered representation.

Đây là một ví dụ order semantics ảnh hưởng trực tiếp layout.

## 9. Radix Tree / Patricia Trie

Trie ngây thơ có thể có chuỗi dài các node chỉ có một child:

```text
c -> o -> m -> p -> u -> t -> e
```

Path compression gộp thành một cạnh nhãn `"compute"`.

**Radix Tree / Patricia Trie** giảm số node, pointer và cấp phát. Search phải so nhiều symbol trên mỗi cạnh, nhưng tổng ký tự xử lý vẫn gắn với độ dài khóa.

Path compression đặc biệt hữu ích khi key dài nhưng branching xảy ra ít.

## 10. Split Edge khi Insert vào Radix Tree

Giả sử cạnh hiện có nhãn `computer`, nhưng chèn `compact`.

Hai chuỗi chia sẻ `com`, sau đó khác nhau. Cạnh phải được tách:

```text
com
├── puter
└── pact
```

Insert Radix Tree vì thế phải tìm longest common prefix giữa edge label và phần key còn lại rồi xử lý các trường hợp:

```text
match toàn edge
key kết thúc giữa edge
mismatch giữa edge
```

Đây là lý do compressed trie tiết kiệm memory nhưng implementation phức tạp hơn Trie một ký tự mỗi cạnh.

## 11. Patricia Trie và Bit Prefix

Patricia Trie thường được dùng cho bit strings hoặc IP prefixes. Nó chỉ giữ các bit/position phân nhánh quan trọng thay vì mọi bit trung gian.

Trong routing:

```text
10.0.0.0/8
10.10.0.0/16
10.10.20.0/24
```

khi lookup destination, cần chọn route có **prefix dài nhất khớp**.

Trie/Radix Tree mã hóa requirement này tự nhiên hơn Hash Table exact-match.

## 12. Longest Prefix Match

Duyệt key từ gốc, đồng thời ghi nhớ terminal node gần nhất đã gặp.

Khi không còn edge phù hợp, terminal gần nhất chính là longest matching prefix.

Đây là pattern quan trọng trong routing và rule matching.

## 13. Binary Trie và Maximum XOR

Một integer có thể xem như chuỗi bit cố định `W` bit.

Muốn maximize `x XOR y`, tại bit hiện tại của `x`, ưu tiên branch có bit đối nghịch nếu tồn tại.

```text
x bit = 0 -> ưu tiên y bit = 1
x bit = 1 -> ưu tiên y bit = 0
```

Với word width cố định, insert/query là `O(W)`.

Binary Trie minh họa rằng Trie không chỉ dành cho text; bất kỳ key có cấu trúc tuần tự đều có thể được index theo prefix.

## 14. Count theo Prefix

Nếu node lưu:

```text
passCount = số key đi qua node
endCount  = số key kết thúc tại node
```

thì:

```text
countPrefix(p) = passCount(node(p))
countExact(k)  = endCount(node(k))
```

Metadata này rất hữu ích cho dictionary frequency nhưng insert/delete phải cập nhật toàn path đúng thứ tự.

## 15. Autocomplete không chỉ là Trie

Trie giải quyết candidate retrieval theo prefix, nhưng production autocomplete còn cần ranking.

Có thể lưu ở mỗi node:

```text
top-K suggestions
max score trong subtree
frequency/time-decay metadata
```

Khi đó query prefix có thể trả top results rất nhanh.

Trade-off:

```text
read nhanh hơn
nhưng update ranking phải propagate lên nhiều prefix node
```

Đây là read/write trade-off điển hình của materialized metadata.

## 16. Best-First Autocomplete

Nếu mỗi node có `maxScore` của subtree, ta không cần cache toàn Top-K tại từng prefix. Sau khi tới prefix node, có thể dùng priority queue ưu tiên subtree có upper bound lớn nhất.

Đây là một bài branch-and-bound nhỏ:

```text
state = trie node
upper bound = max score dưới node
```

Khi đã tìm đủ K result và bound còn lại không thể thắng, dừng.

Trie có thể kết hợp heap để tạo ranking search thay vì chỉ DFS toàn subtree.

## 17. Aho–Corasick

Nếu có nhiều pattern và cần quét một text một lần, chạy search riêng cho từng pattern hoặc restart Trie từ từng vị trí là tốn kém.

Aho–Corasick thêm **failure link**.

Khi transition thất bại, automaton chuyển tới suffix dài nhất của prefix hiện tại cũng là prefix của một pattern.

Sau preprocessing dictionary, matching chạy gần:

\[
O(|text| + \text{number of matches})
\]

với các giả định representation phù hợp.

## 18. Failure Link như tái sử dụng trạng thái

Failure link có cùng tinh thần với KMP prefix function và suffix link:

> Khi context dài không còn hợp lệ, đừng quay về trạng thái rỗng; tái sử dụng suffix dài nhất còn có ý nghĩa.

Đây là motif rất sâu trong string algorithms.

## 19. Double-Array Trie

Double-Array Trie biểu diễn transitions bằng hai mảng, thường gọi `base` và `check`, nhằm giảm pointer/object overhead và tăng locality.

Ý tưởng là ánh xạ child position bằng công thức từ `base[parent] + code(symbol)`, còn `check` xác nhận parent thật sự của slot.

Ưu điểm:

```text
compact hơn object-trie
array locality tốt
lookup nhanh
```

Nhược điểm là construction/update phức tạp và quản lý slot trống khó hơn.

## 20. Succinct Trie và LOUDS

Nếu dictionary rất lớn và gần tĩnh, có thể biểu diễn topology bằng bitvector thay vì pointer per node.

**LOUDS (Level-Order Unary Degree Sequence)** mã hóa bậc node theo level order và dùng rank/select để điều hướng.

Mục tiêu không còn là “code dễ nhất” mà là giảm bits per node tới gần giới hạn thông tin.

Đây là ví dụ succinct data structure: vẫn hỗ trợ navigation nhưng với memory gần tối ưu hơn pointer graph.

## 21. Finite-State Transducer / Minimal Automaton

Nếu dictionary tĩnh có nhiều suffix giống nhau, Trie chỉ chia sẻ prefix; các suffix giống nhau ở các nhánh khác vẫn bị lặp.

Minimal acyclic finite-state automaton hoặc FST có thể gộp các trạng thái tương đương phía sau, chia sẻ cả suffix structure.

Điều này đặc biệt mạnh trong dictionary/search-engine indexing.

Mô hình tư duy:

```text
Trie       -> chia sẻ prefix
minimal DFA/FST -> chia sẻ các continuation tương đương
```

## 22. Trie vs Hash Table

Hash Table tốt hơn khi chỉ cần exact lookup và memory overhead Trie không đáng.

Trie tốt khi query quan tâm:

```text
prefix
longest-prefix
lexicographic traversal
prefix count
structure bên trong key
```

Không nên chọn Trie chỉ vì key là string.

## 23. Trie vs Sorted Array

Dictionary tĩnh có thể dùng sorted array + binary search để tìm prefix range.

Ưu điểm:

```text
memory gọn
cache-friendly
simple serialization
```

Trie mạnh hơn khi dynamic update, prefix metadata hoặc character-by-character traversal là trung tâm.

Đối với workload static, sorted array đôi khi thực dụng hơn Trie.

## 24. Trie vs TreeMap

TreeMap giữ full key order. Prefix query có thể chuyển thành range trong lexicographic order.

Nhưng mỗi comparator có thể phải so lại nhiều prefix character ở nhiều tree node.

Trie chia sẻ phần prefix đã duyệt một lần, nhưng trả giá bằng nhiều node hơn.

Không có lựa chọn tốt nhất nếu chưa biết key length, update rate và query mix.

## 25. Unicode

“Character” không phải đơn vị duy nhất.

Có thể có:

```text
byte
UTF-16 code unit
Unicode code point
grapheme cluster
normalized form
```

`é` có thể được biểu diễn trực tiếp hoặc bằng `e + combining mark`. Nếu không normalize, hai string người dùng nhìn giống nhau có thể đi theo hai path khác nhau.

String index production phải xác định normalization policy trước khi xây Trie.

## 26. Case Folding và Locale

Autocomplete/search không phân biệt hoa thường có thể cần case folding. Nhưng mapping chữ thường không luôn là phép một-ký-tự thành một-ký-tự ở mọi ngôn ngữ.

Nếu normalization/case folding là một phần của identity, phải thực hiện nhất quán cả lúc insert và query.

Hash/equality và Trie path đều phụ thuộc cùng canonicalization contract.

## 27. Memory Allocation

Trong C, cấp phát từng node bằng `malloc` có thể đắt. Arena allocator thường rất phù hợp vì nhiều Trie node có cùng vòng đời.

Trong Java/JavaScript, nhiều object nhỏ tạo pressure lên GC.

Mảng node + integer child index có thể giảm object overhead, đặc biệt với dictionary lớn.

## 28. Cache Locality

Pointer-heavy Trie có lookup `O(L)` nhưng mỗi bước có thể gây cache miss.

Radix compression giảm số node truy cập. Double-array hoặc compact arrays tăng locality.

Big-O `O(L)` không nói bao nhiêu cache line phải chạm.

## 29. Persistent Trie

Nếu cần nhiều version, update một key chỉ thay các node trên path của key. Có thể sao chép path rồi chia sẻ toàn bộ phần còn lại.

Persistent Trie hữu ích cho:

```text
versioned dictionary
XOR query theo prefix phiên bản
functional maps
snapshot
```

Chi phí update thường tỷ lệ độ dài key hoặc số bit.

## 30. Concurrent Trie

Fine-grained locking hoặc lock-free Trie phức tạp vì insert/delete thay đổi child pointers và lifetime node.

Radix Tree còn có split/merge edge, làm atomic update khó hơn.

Trong read-mostly workload, immutable snapshot + copy-on-write có thể đơn giản hơn mutable concurrent tree.

## 31. Trie trong Database/Search System

Trie/Radix Tree có thể dùng cho:

```text
term dictionary
autocomplete
routing
prefix-compressed index key
in-memory ordered key index
```

B+Tree page cũng có thể dùng prefix compression giữa các key gần nhau để giảm storage. Ý tưởng chia sẻ prefix xuất hiện ngoài Trie thuần túy.

## 32. Kiểm thử

Các case quan trọng:

```text
empty string nếu hợp lệ
key là prefix của key khác
nhiều duplicate key
xóa key có shared prefix
alphabet ngoài dự kiến
Unicode normalized/non-normalized
very long key
single-child chains
high branching node
```

Với Trie tự cài, có thể differential-test exact lookup với Hash Set và prefix query với brute-force filter trên tập string nhỏ.

## 33. Validator

Nếu có `passCount/endCount`, có thể kiểm tra:

```text
passCount >= endCount
passCount phù hợp tổng subtree theo convention
không node rác có passCount 0 nếu policy yêu cầu thu hồi
mọi child symbol unique
```

Radix Tree còn cần kiểm tra không có hai outgoing edge bắt đầu bằng cùng symbol và không có unary node nếu representation yêu cầu compression tối đa.

## 34. Những hiểu lầm phổ biến

“Trie lookup O(L) nên luôn nhanh hơn HashMap” — sai; constant factor và memory locality rất khác.

“Trie chỉ dùng cho từ tiếng Anh” — sai; key có thể là byte, bit, token hoặc code point.

“Prefix query luôn cần Trie” — sai; sorted array/static dictionary có thể đơn giản hơn.

“Unicode string có thể index theo `char` mà không cần policy” — sai với nhiều miền người dùng thực tế.

“Compressed Trie chỉ là Trie ít node hơn” — đúng ở mức ý tưởng nhưng update/split invariants phức tạp hơn nhiều.

## Mô hình tư duy

> Trie biến **prefix từ một quan hệ ngầm trong khóa thành một trạng thái tường minh trong cấu trúc**. Nhờ đó query prefix không phải so lại toàn bộ keyspace.

Khi cân nhắc Trie, hãy hỏi: **query có thực sự cần prefix không, alphabet/normalization là gì, branching factor thế nào, dictionary static hay dynamic, memory overhead có chấp nhận được không, và có cần compression/ranking/persistence/concurrency không?**

Xem thêm: [String Algorithms](../05_specialized/00_string_algorithms.md), [Suffix Structures](../05_specialized/04_suffix_arrays_suffix_trees_and_lcp.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [B/B+Tree](./05_b_trees_and_external_memory.md).