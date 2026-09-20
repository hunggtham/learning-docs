# Trie
**Cây tiền tố / Trie / Prefix Tree / 트라이·접두사 트리**

Trie là cấu trúc tổ chức keys theo **các phần tử cấu thành của key**, thường là characters hoặc bits. Nếu nhiều keys chia sẻ prefix, phần prefix chung đó được lưu một lần dưới dạng path chung.

Ví dụ các từ `car`, `card`, `care`, `cat` chia sẻ prefix `ca`:

```text
(root)
  |
  c
  |
  a
 / \
r   t*
|\
d* e*
```

Dấu `*` biểu diễn vị trí kết thúc một word. Một node trong trie không nhất thiết tự đại diện một word; nó đại diện một prefix. Marker như `isEnd` phân biệt prefix `car` với việc chỉ có các words `card`, `care` đi qua node đó.

## 1. Trie giải quyết vấn đề gì?

Hash table rất mạnh cho exact key lookup: “key này có tồn tại không?”. Nhưng nếu câu hỏi là “có key nào bắt đầu bằng `app` không?”, “liệt kê 10 từ bắt đầu bằng prefix này”, hoặc “tìm longest matching prefix”, hash table không tự nhiên vì nó hash toàn key và làm mất structure bên trong key.

Trie làm ngược lại: key được tách thành sequence symbols và mỗi symbol quyết định một edge. Prefix trở thành một node/path thật trong structure.

Vì vậy trie phù hợp khi **prefix semantics là một phần của workload**.

## 2. Insert và Search

Giả sử key có length `L`. Ta bắt đầu từ root và đi qua từng symbol. Nếu child tương ứng chưa tồn tại khi insert, ta tạo node mới. Sau symbol cuối, đánh dấu `isEnd = true`.

Search exact cũng đi theo path đó. Nếu thiếu child, key không tồn tại. Nếu đi hết string nhưng node cuối `isEnd = false`, input chỉ là prefix của một key dài hơn, chưa phải exact key.

Với child lookup `O(1)` expected qua array/hash map, time thường:

\[
O(L)
\]

Điểm đáng chú ý là runtime phụ thuộc key length nhiều hơn số keys toàn trie.

## 3. Prefix Search

Để kiểm tra có word nào bắt đầu bằng prefix `p`, ta chỉ cần đi theo path `p`. Nếu path tồn tại, prefix tồn tại trong trie, bất kể node cuối có `isEnd` hay không.

Autocomplete có thể tiếp tục DFS/BFS từ node prefix để enumerate descendants.

Nếu chỉ enumerate mọi descendant, output có thể rất lớn. Complexity phải tính cả số kết quả; không có algorithm nào output một triệu suggestions trong `O(1)`.

Production autocomplete thường giới hạn top-N và cache ranking metadata tại nodes để tránh traverse toàn subtree mỗi query.

## 4. Representation của children

Một trie node cần mapping:

```text
symbol -> child node
```

Representation phụ thuộc alphabet.

Nếu alphabet nhỏ, cố định như lowercase English `a-z`, có thể dùng array size 26. Lookup rất nhanh và predictable nhưng mỗi node trả memory cho 26 child slots dù hầu hết null.

Nếu alphabet sparse/lớn, `HashMap<Character, Node>` hoặc map theo code point tiết kiệm empty slots nhưng thêm hash/object overhead.

Một sorted small vector/list children có thể tốt khi branching factor nhỏ vì locality tốt hơn hash map.

Không có representation tốt nhất độc lập workload.

## 5. Memory là nhược điểm lớn của naive trie

Trie có thể có số nodes xấp xỉ tổng length của all keys nếu sharing ít. Nếu mỗi node là một Java object chứa HashMap riêng, overhead có thể lớn hơn text data rất nhiều.

Trong JavaScript, object/Map per node cũng tốn metadata và GC pressure. Trong C, pointer arrays lớn cho mỗi node có thể lãng phí mạnh nếu alphabet sparse.

Do đó production tries thường dùng path compression, compact arrays, arena allocation, double-array trie hoặc finite-state compression tùy workload.

## 6. Delete đúng cách

Xóa word không thể đơn giản delete toàn path vì path có thể được key khác dùng chung.

Ví dụ có `car` và `card`. Xóa `car` chỉ cần clear `isEnd` tại node `r`; path `c-a-r-d` vẫn cần cho `card`.

Sau khi clear end marker, ta có thể đi ngược từ dưới lên và reclaim node chỉ khi:

```text
node không còn child
và node không phải end của key khác
```

Nếu trie lưu frequency/reference count, deletion/reclamation có thể dựa trên count.

Đây là một case điển hình của shared-prefix ownership.

## 7. Lexicographic Traversal

Nếu children được iterate theo symbol order, DFS trên trie output keys theo lexicographic order.

Hash-map children không tự bảo đảm order; cần sorted keys hoặc ordered map nếu lexical traversal là requirement thường xuyên.

Again, order semantics ảnh hưởng representation.

## 8. Compressed Trie / Radix Tree

Naive trie có nhiều chains mà mỗi node chỉ có một child. Ta có thể compress chain thành một edge label dài hơn.

Thay vì:

```text
c -> o -> m -> p -> u -> t -> e
```

có thể lưu một edge label `"compute"` nếu không có branching bên trong.

**Radix Tree / Patricia Trie / 압축 트라이** giảm node count và pointer overhead. Search phải so sánh nhiều symbols trên mỗi edge label, nhưng total character work vẫn gắn với key length.

Path compression đặc biệt hiệu quả khi keys dài và branching chỉ xảy ra ở ít positions.

## 9. Patricia Trie cho bit strings

Patricia trie là compressed binary radix trie, thường bỏ các unary internal nodes và chỉ giữ branching positions quan trọng.

Routing tables, IP prefixes và some key-value indexes có thể dùng radix/patricia variants vì prefix bits có semantic trực tiếp.

Nếu IPv4 address là 32 bits, route như `10.0.0.0/8` đại diện prefix 8 bits. Longest-prefix match tìm route matching destination với prefix dài nhất.

## 10. Binary Trie và Maximum XOR

Trie không chỉ dành cho text. Một integer có thể được xem như bit string từ most significant bit xuống least significant bit.

Để maximize `x XOR y`, tại mỗi bit của `x`, ta muốn chọn bit đối nghịch của `y` nếu branch đó tồn tại, vì XOR bit khi khác nhau là 1.

Ví dụ với fixed 31/32/64-bit width, insert numbers vào binary trie rồi query greedy theo bits có thể tìm maximum XOR partner trong `O(W)` với `W` là bit width.

Đây là ví dụ trie khai thác internal structure của numeric key.

## 11. Prefix Count và Metadata Augmentation

Node có thể lưu số words đi qua (`passCount`) và số words kết thúc (`endCount`).

Khi đó query “bao nhiêu words có prefix `pre`?” chỉ cần đi tới node prefix rồi trả `passCount`.

Nếu duplicate keys được phép, `endCount` tốt hơn boolean `isEnd`.

Ta có thể augment thêm top suggestions, frequency, timestamp hoặc subtree statistics. Nhưng metadata làm insert/delete đắt hơn và tăng memory; chỉ lưu summary phục vụ query thật sự cần.

## 12. Autocomplete ranking

Trie chỉ giải quyết candidate retrieval theo prefix, không tự giải quyết ranking.

Một production autocomplete có thể lưu top-K suggestions tại mỗi popular prefix node. Query prefix dài `L` đi `O(L)`, sau đó trả cached top-K nhanh.

Nhưng update popularity trở nên phức tạp vì score change có thể phải propagate qua nhiều prefix nodes. Đây là read/write trade-off: precompute để query nhanh, trả update cost và memory.

## 13. Trie và Aho–Corasick

Nếu có nhiều patterns và cần scan một text để tìm tất cả matches, chạy trie search từ mọi text position vẫn đắt.

Aho–Corasick thêm **failure links** vào trie. Khi mismatch, automaton chuyển tới longest suffix hiện tại cũng là prefix của một pattern, thay vì restart từ root.

Kết quả là multi-pattern matching gần tuyến tính theo text length + matches sau preprocessing dictionary.

Aho–Corasick cho thấy trie có thể được nâng thành automaton bằng cách thêm cross-links giữa prefix states.

## 14. Trie vs Hash Table

Hash table thường tốt hơn cho exact lookup nếu không cần prefix semantics. Nó có ít logical nodes hơn và implementation/library có sẵn rất tối ưu.

Trie đáng giá khi query khai thác structure trong key: prefix existence, longest prefix, lexicographic traversal, prefix counts, routing hoặc autocomplete.

Có thể tóm lại:

> Hash table tối ưu cho **identity của toàn key**; trie tối ưu cho **structure bên trong key**.

## 15. Trie vs Sorted Array

Nếu dictionary static, sorted array + binary search cũng xử lý prefix query khá tốt.

Ta binary search lower bound của prefix rồi scan forward trong range matching prefix. Memory thường compact hơn trie và locality tốt.

Trie mạnh hơn khi updates nhiều, character-by-character traversal quan trọng hoặc cần prefix metadata. Sorted array có thể đơn giản hơn cho static dictionary.

Vì vậy “prefix query” chưa đủ để mặc định chọn trie; mutation pattern và memory vẫn quan trọng.

## 16. Trie vs BST/TreeMap

Ordered map lưu full keys theo comparator. Prefix range có thể được chuyển thành lower/upper bounds trong lexicographic keyspace, nhưng mỗi comparison có thể inspect nhiều characters.

Trie chia sẻ prefixes và không compare lại prefix từ đầu mỗi tree comparison. Tuy nhiên tree node count theo keys thay vì total characters, nên memory trade-off khác.

## 17. Unicode: Character không luôn là “một ký tự người dùng nhìn thấy”

Trong Java, `char` là UTF-16 code unit. Emoji hoặc nhiều Unicode code points cần surrogate pairs. JavaScript string indexing cũng theo UTF-16 code units.

Nếu trie semantics cần Unicode code points, nên iterate code points thay vì raw `char`/code unit. Nếu cần grapheme clusters như một ký tự hiển thị, vấn đề còn phức tạp hơn.

Alphabet definition phải được quyết định trước khi nói complexity theo `L`, vì `L` có thể là bytes, code units, code points hoặc grapheme clusters.

## 18. Case normalization và locale

Autocomplete/search thường cần case-insensitive behavior hoặc accent normalization. Nếu keys được normalize trước insert nhưng query không normalize cùng rule, lookup sai.

Unicode normalization forms như NFC/NFD cũng có thể làm hai strings visually giống nhưng sequence code points khác.

Normalization không thuộc trie algorithm cốt lõi, nhưng là correctness condition của text-key system.

## 19. Double-Array Trie

Object-node trie có nhiều pointer overhead. **Double-Array Trie** dùng arrays như `base` và `check` để encode transitions compact hơn và locality tốt hơn.

Implementation/construction phức tạp nhưng rất hữu ích cho static/mostly-static dictionaries và morphological/text systems nơi memory efficiency quan trọng.

Điểm lớn hơn là một abstract trie có nhiều physical encodings khác nhau.

## 20. Ternary Search Tree

Ternary Search Tree lưu mỗi node một character và ba directions: `<`, `=`, `>` so với character hiện tại.

Nó cân bằng giữa trie branching array lớn và BST-like character comparison. Memory có thể nhỏ hơn dense trie khi alphabet lớn, nhưng lookup characteristics khác.

Đây là một alternative đáng biết, không phải default replacement.

## 21. Persistent Trie

Trong một số bài versioned queries, ta có thể tạo **persistent trie** bằng path copying: mỗi update chỉ copy nodes trên path thay đổi, còn phần còn lại share với version cũ.

Binary persistent trie có thể dùng cho XOR/rank queries theo prefix versions. Complexity và memory thường `O(W)` nodes per update với bit width `W`.

Persistent data structures cho thấy prefix sharing không chỉ giữa keys mà còn giữa versions.

## 22. Longest Prefix Match

Given query string/key, ta đi theo trie và nhớ node sâu nhất có `isEnd`. Khi path không thể tiếp tục, deepest end marker là longest stored prefix matching query.

Operation này xuất hiện trong routing, dictionary segmentation và configuration inheritance.

Hash table phải thử nhiều prefix lengths; trie giải tự nhiên trong một traversal.

## 23. Word segmentation connection

Bài Word Break hỏi string có thể chia thành dictionary words không. Trie có thể giảm repeated substring lookup khi DP/backtracking thử các end positions: từ mỗi start, walk trie theo characters cho tới khi branch chết, và mỗi `isEnd` tạo transition DP.

Trie không tự giải DP, nhưng representation dictionary làm candidate generation hiệu quả hơn.

## 24. Testing Trie

Test exact search phải phân biệt word và prefix: insert `apple`, search `app` phải false nếu `app` chưa insert, nhưng `startsWith("app")` true.

Delete cần test shared prefixes như `car`, `card`, `care`; xóa một key không được phá keys còn lại.

Duplicate semantics phải rõ nếu structure hỗ trợ counts. Unicode normalization/case behavior cũng cần test theo API contract.

Differential testing có thể so set of full keys với HashSet cho exact membership, và brute-force `startsWith` scan cho prefix queries trên datasets nhỏ.

## 25. Complexity nhìn đúng cách

Trie search thường viết `O(L)`, nhưng child lookup constant chỉ là abstraction. Dense array child lookup thật sự `O(1)` với memory lớn; hash map expected `O(1)`; tree map `O(log σ)` với alphabet size `σ`; compressed edges cần compare multiple symbols.

Memory thường proportional tổng số distinct prefix nodes, không chỉ number of keys.

Một trie có thể rất nhanh nhưng không compact. Vì vậy complexity discussion phải đi cùng representation.

## Mental Model

> Trie biến **key thành path**. Khi prefix hoặc bit-prefix của key có semantic thật, trie lưu trực tiếp semantic đó trong structure thay vì coi key là một atom như hash table.

Sức mạnh của trie đến từ prefix sharing; nhược điểm cũng đến từ việc representation có thể tạo rất nhiều nodes. Radix compression, compact encodings và metadata augmentation là các cách điều chỉnh trade-off cho workload thật.

Xem thêm: [String Algorithms](../05_specialized/00_string_algorithms.md), [Suffix Structures](../05_specialized/04_suffix_arrays_suffix_trees_and_lcp.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [DSA trong Systems](../90_connections/01_dsa_in_databases_networks_and_systems.md).