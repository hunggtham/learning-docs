# Trie và các cấu trúc chỉ mục tiền tố

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Trie và các cấu trúc chỉ mục tiền tố**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Khi nào Trie đáng dùng?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. tìm kiếm (search / 검색) và Insert** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Trie với prefix, search và insert, để chỉ mục chuỗi được chọn theo pattern truy vấn.

**Trie / Prefix cây (tree / 트리) / 트라이·접두사 트리**

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

> bảng băm (hash table / 해시 테이블) quan tâm định danh của toàn khóa. Trie giữ lại cấu trúc bên trong khóa để biến prefix thành một trạng thái có thể truy vấn trực tiếp.

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

Nếu chỉ cần chính xác (exact / 정확한) lookup và không khai thác prefix, băm (hash / 해시) Map thường đơn giản và tiết kiệm bộ nhớ hơn.

Trie đáng dùng khi tiền tố là một phần của truy vấn, không chỉ là chi tiết của khóa đầy đủ. Sau search và insert, prefix query cho phép trả lời trực tiếp các câu hỏi trên một nhánh.

## 2. tìm kiếm (search / 검색) và Insert

Với khóa dài `L`, đi từ gốc qua từng symbol.

Nếu child tương ứng chưa tồn tại khi insert, tạo child mới. Sau symbol cuối, đánh dấu `isEnd` hoặc tăng `endCount`.

Chính xác (exact / 정확한) tìm kiếm (search / 검색) cần hai điều kiện:

```text
đường đi tồn tại
nút cuối là điểm kết thúc khóa
```

Nếu đường đi tồn tại nhưng `isEnd=false`, đầu vào chỉ là prefix của khóa dài hơn.

Nếu lookup child gần `O(1)`, độ phức tạp (complexity / 복잡도) thường:

\[
O(L)
\]

phụ thuộc độ dài khóa hơn là số lượng khóa trong dictionary.

Prefix query tìm node đại diện cho prefix rồi duyệt hoặc đếm subtree phía dưới, nên chi phí tách thành phần tìm prefix và phần kết quả trả về. Để các thao tác này đúng, trie phải giữ một số invariant rõ ràng.

## 3. Prefix truy vấn (query / 쿼리)

Để kiểm tra `startsWith(prefix)`, chỉ cần đi hết prefix. Không cần nút cuối là `isEnd`.

Nếu cần liệt kê mọi kết quả, độ phức tạp (complexity / 복잡도) phải tính cả đầu ra (output / 출력):

\[
O(|prefix| + k + \text{characters emitted})
\]

với `k` là số kết quả.

Một hệ thống autocomplete không thể trả một triệu gợi ý trong `O(|prefix|)` chỉ vì Trie tìm prefix nhanh.

Invariant cốt lõi là mỗi path biểu diễn đúng chuỗi ký tự, terminal flag chỉ đánh dấu khóa đã chèn, và mọi child nối tiếp đúng prefix. Cách biểu diễn children quyết định cả tốc độ duyệt lẫn footprint bộ nhớ.

## 4. Bất biến quan trọng

Một Trie mutable thường cần giữ:

```text
mỗi path từ root tương ứng đúng một prefix
mọi key tồn tại có đúng một terminal marker/count
child mapping không chứa duplicate symbol
passCount/endCount nếu có phải nhất quán với subtree
```

Nếu hỗ trợ duplicate keys, `endCount` tốt hơn `boolean isEnd`.

Nếu lưu `passCount`, insert/delete phải cập nhật mọi nút trên đường dẫn (path / 경로). siêu dữ liệu (metadata / 메타데이터) tăng tốc truy vấn (query / 쿼리) nhưng tạo thêm bất biến (invariant / 불변식) cần bảo trì.

Children có thể là mảng cố định, map, vector cạnh hoặc cấu trúc nén; lựa chọn phụ thuộc alphabet và phân bố prefix. Mảng con đơn giản nhưng dễ lãng phí, khiến memory trở thành điểm yếu lớn của trie ngây thơ.

## 5. Child biểu diễn (representation / 표현)

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

Nhược điểm: mỗi nút (node / 노드) trả chi phí cho toàn alphabet dù chỉ có 1–2 child.

### Băm (hash / 해시) Map

Phù hợp alphabet lớn/thưa. Tiết kiệm slot null nhưng tăng đối tượng (object / 객체)/băm (hash / 해시) overhead.

### Sorted small véc-tơ (vector / 벡터)

Nếu branching factor thường nhỏ, một véc-tơ (vector / 벡터) cặp `(symbol, child)` đã sắp xếp có thể cache-friendly hơn băm (hash / 해시) Map. Có thể tuyến tính (linear / 선형) scan với vài child hoặc tìm kiếm nhị phân (binary search / 이진 탐색) khi nhiều hơn.

Biểu diễn (representation / 표현) nên dựa trên phân phối branching thực tế.

Trie naïve có thể tạo nhiều node ít nhánh và nhiều slot rỗng, nên tổng footprint vượt xa tổng độ dài key. Delete cần thu hồi các node không còn terminal và không còn child mà không làm hỏng prefix của key khác.

## 6. Bộ nhớ là điểm yếu lớn của Trie ngây thơ

Số nút (node / 노드) có thể gần tổng độ dài mọi key:

\[
O\left(\sum |key_i|\right)
\]

Nếu mỗi nút (node / 노드) là đối tượng (object / 객체) Java chứa một HashMap riêng, overhead có thể lớn hơn dữ liệu ký tự nhiều lần.

JavaScript `Map` per nút (node / 노드) cũng tạo áp lực GC. Trong C, mảng 256 pointer trên mỗi nút (node / 노드) cực lãng phí nếu branching thưa.

Do đó môi trường vận hành (production / 운영 환경) Trie thường dùng:

```text
path compression
compact node layout
arena/pool allocation
double-array trie
LOUDS / succinct representation
FST/automaton compression
```

Delete đi ngược path, chỉ xóa suffix không còn được key nào dùng; terminal của một key prefix phải được giữ lại. Khi children được duyệt theo thứ tự, cùng cấu trúc đó tạo ra lexicographic traversal.

## 7. Delete

Xóa `car` khi vẫn còn `card` không được giải phóng toàn đường dẫn (path / 경로) `c-a-r`.

Quy trình:

1. đi tới terminal;
2. giảm `endCount` hoặc clear `isEnd`;
3. đi ngược lên;
4. chỉ xóa nút (node / 노드) nếu không còn child, không còn key kết thúc và siêu dữ liệu (metadata / 메타데이터) cho phép.

Nếu có `passCount`, nút (node / 노드) có thể được thu hồi khi count xuống 0.

Delete là nơi shared-prefix quyền sở hữu (ownership / 소유권) trở nên rõ nhất.

Lexicographic traversal DFS children theo thứ tự, phát output ở terminal node, nên thứ tự kết quả phản ánh thứ tự alphabet đã chọn. Radix tree giảm node bằng cách gộp các đoạn path không phân nhánh.

## 8. Lexicographic Traversal

Nếu child được duyệt theo symbol thứ tự (order / 순서), DFS xuất key theo thứ tự từ điển.

Nếu child dùng băm (hash / 해시) Map, iteration thứ tự (order / 순서) có thể không tương ứng lexicographic thứ tự (order / 순서); cần sort symbol hoặc dùng ordered biểu diễn (representation / 표현).

Đây là một ví dụ thứ tự (order / 순서) ngữ nghĩa (semantics / 의미론) ảnh hưởng trực tiếp bố cục (layout / 레이아웃).

Radix/Patricia trie lưu edge label là một chuỗi hoặc bit string thay vì một ký tự, giảm overhead trên các nhánh dài. Khi insert key chia sẻ một phần edge nhưng rẽ giữa chừng, phải split edge trước khi gắn suffix mới.

## 9. Radix cây (tree / 트리) / Patricia Trie

Trie ngây thơ có thể có chuỗi dài các nút (node / 노드) chỉ có một child:

```text
c -> o -> m -> p -> u -> t -> e
```

Đường dẫn (path / 경로) compression gộp thành một cạnh nhãn `"compute"`.

**Radix cây (tree / 트리) / Patricia Trie** giảm số nút (node / 노드), pointer và cấp phát. tìm kiếm (search / 검색) phải so nhiều symbol trên mỗi cạnh, nhưng tổng ký tự xử lý vẫn gắn với độ dài khóa.

Đường dẫn (path / 경로) compression đặc biệt hữu ích khi key dài nhưng branching xảy ra ít.

Split edge tạo node trung gian cho common prefix, rồi giữ hai suffix như các child riêng; terminal có thể nằm ngay tại node mới. Với bit string và địa chỉ nhị phân, Patricia trie áp dụng cùng ý tưởng trên bit prefix.

## 10. Split Edge khi Insert vào Radix cây (tree / 트리)

Giả sử cạnh hiện có nhãn `computer`, nhưng chèn `compact`.

Hai chuỗi chia sẻ `com`, sau đó khác nhau. Cạnh phải được tách:

```text
com
├── puter
└── pact
```

Insert Radix cây (tree / 트리) vì thế phải tìm longest dùng chung (common / 공통) prefix giữa edge label và phần key còn lại rồi xử lý các trường hợp:

```text
match toàn edge
key kết thúc giữa edge
mismatch giữa edge
```

Đây là lý do compressed trie tiết kiệm bộ nhớ (memory / 메모리) nhưng hiện thực (implementation / 구현) phức tạp hơn Trie một ký tự mỗi cạnh.

Patricia trie chọn bit khác biệt để phân nhánh, rất phù hợp với routing prefix hoặc các khóa nhị phân dài. Từ path representation đó, longest-prefix match có thể ghi nhận ứng viên cuối cùng còn khớp khi đi xuống.

## 11. Patricia Trie và Bit Prefix

Patricia Trie thường được dùng cho bit strings hoặc IP prefixes. Nó chỉ giữ các bit/position phân nhánh quan trọng thay vì mọi bit trung gian.

Trong routing:

```text
10.0.0.0/8
10.10.0.0/16
10.10.20.0/24
```

khi lookup destination, cần chọn tuyến (route / 경로) có **prefix dài nhất khớp**.

Trie/Radix cây (tree / 트리) mã hóa yêu cầu (requirement / 요구사항) này tự nhiên hơn bảng băm (hash table / 해시 테이블) exact-match.

Longest-prefix match lưu lại node terminal gần nhất trên đường đi, rồi trả kết quả đó nếu phần còn lại của query không khớp. Binary trie dùng quyết định theo từng bit cho một mục tiêu khác: chọn số tạo XOR lớn nhất.

## 12. Longest Prefix Match

Duyệt key từ gốc, đồng thời ghi nhớ terminal nút (node / 노드) gần nhất đã gặp.

Khi không còn edge phù hợp, terminal gần nhất chính là longest matching prefix.

Đây là mẫu (pattern / 패턴) quan trọng trong routing và quy tắc (rule / 규칙) matching.

Binary trie ưu tiên bit đối nghịch với query ở mỗi level khi có thể, nhờ đó tối đa hóa XOR. Nếu mỗi node giữ thêm subtree count, cùng invariant prefix có thể trả lời số lượng key dưới một prefix.

## 13. nhị phân (binary / 이진) Trie và Maximum XOR

Một integer có thể xem như chuỗi bit cố định `W` bit.

Muốn maximize `x XOR y`, tại bit hiện tại của `x`, ưu tiên branch có bit đối nghịch nếu tồn tại.

```text
x bit = 0 -> ưu tiên y bit = 1
x bit = 1 -> ưu tiên y bit = 0
```

Với word width cố định, insert/truy vấn (query / 쿼리) là `O(W)`.

Nhị phân (binary / 이진) Trie minh họa rằng Trie không chỉ dành cho văn bản (text / 텍스트); bất kỳ key có cấu trúc tuần tự đều có thể được chỉ mục (index / 인덱스) theo prefix.

Prefix count cập nhật counter trên mọi node của path khi insert/delete, nên query chỉ cần tìm node prefix. Autocomplete thêm yêu cầu xếp hạng và giới hạn kết quả, không thể chỉ trả toàn bộ subtree.

## 14. Count theo Prefix

Nếu nút (node / 노드) lưu:

```text
passCount = số key đi qua node
endCount  = số key kết thúc tại node
```

thì:

```text
countPrefix(p) = passCount(node(p))
countExact(k)  = endCount(node(k))
```

Siêu dữ liệu (metadata / 메타데이터) này rất hữu ích cho dictionary frequency nhưng insert/delete phải cập nhật toàn đường dẫn (path / 경로) đúng thứ tự.

Autocomplete thực tế cần score, tần suất, freshness hoặc personalization bên cạnh prefix matching. Best-first traversal dùng priority queue để mở rộng node hứa hẹn nhất và dừng khi đã đủ K kết quả.

## 15. Autocomplete không chỉ là Trie

Trie giải quyết candidate retrieval theo prefix, nhưng môi trường vận hành (production / 운영 환경) autocomplete còn cần ranking.

Có thể lưu ở mỗi nút (node / 노드):

```text
top-K suggestions
max score trong subtree
frequency/time-decay metadata
```

Khi đó truy vấn (query / 쿼리) prefix có thể trả top results rất nhanh.

Sự đánh đổi (trade-off / 트레이드오프):

```text
read nhanh hơn
nhưng update ranking phải propagate lên nhiều prefix node
```

Đây là read/ghi (write / 쓰기) sự đánh đổi (trade-off / 트레이드오프) điển hình của materialized siêu dữ liệu (metadata / 메타데이터).

Best-first autocomplete tránh duyệt toàn bộ subtree bằng upper bound score trên mỗi node, nhưng quality phụ thuộc bound và dữ liệu score. Nếu mục tiêu là tìm nhiều pattern trong một văn bản, trie cần failure links như Aho–Corasick.

## 16. Best-First Autocomplete

Nếu mỗi nút (node / 노드) có `maxScore` của subtree, ta không cần bộ nhớ đệm (cache / 캐시) toàn Top-K tại từng prefix. Sau khi tới prefix nút (node / 노드), có thể dùng priority hàng đợi (queue / 큐) ưu tiên subtree có upper bound lớn nhất.

Đây là một bài branch-and-bound nhỏ:

```text
state = trie node
upper bound = max score dưới node
```

Khi đã tìm đủ K kết quả (result / 결과) và bound còn lại không thể thắng, dừng.

Trie có thể kết hợp vùng nhớ động (heap / 힙) để tạo ranking tìm kiếm (search / 검색) thay vì chỉ DFS toàn subtree.

Aho–Corasick xây trie của các pattern rồi duyệt text một lần để báo mọi match kết thúc tại mỗi vị trí. Failure link tái sử dụng suffix state thay vì quay lại root sau từng mismatch.

## 17. Aho–Corasick

Nếu có nhiều mẫu (pattern / 패턴) và cần quét một văn bản (text / 텍스트) một lần, chạy tìm kiếm (search / 검색) riêng cho từng mẫu (pattern / 패턴) hoặc restart Trie từ từng vị trí là tốn kém.

Aho–Corasick thêm **thất bại (failure / 실패) link**.

Khi chuyển tiếp (transition / 전이) thất bại, automaton chuyển tới suffix dài nhất của prefix hiện tại cũng là prefix của một mẫu (pattern / 패턴).

Sau preprocessing dictionary, matching chạy gần:

\[
O(|text| + \text{number of matches})
\]

với các giả định biểu diễn (representation / 표현) phù hợp.

Failure link trỏ tới suffix dài nhất vẫn là prefix của một pattern và được tính theo BFS trên trie. Khi cần layout gọn và cache-friendly hơn, double-array trie mã hóa transitions bằng hai mảng base/check.

## 18. thất bại (failure / 실패) Link như tái sử dụng trạng thái

Thất bại (failure / 실패) link có cùng tinh thần với KMP prefix hàm (function / 함수) và suffix link:

> Khi ngữ cảnh (context / 맥락) dài không còn hợp lệ, đừng quay về trạng thái rỗng; tái sử dụng suffix dài nhất còn có ý nghĩa.

Đây là motif rất sâu trong string algorithms.

Double-array trie giảm pointer overhead nhưng cần quản lý collision khi chọn base và có thể phải di chuyển vùng transition. Succinct trie/LOUDS nén topology bằng bitvector, đổi một phần tốc độ và khả năng cập nhật lấy memory efficiency.

## 19. Double-Array Trie

Double-Array Trie biểu diễn transitions bằng hai mảng, thường gọi `base` và `check`, nhằm giảm pointer/đối tượng (object / 객체) overhead và tăng locality.

Ý tưởng là ánh xạ child position bằng công thức từ `base[parent] + code(symbol)`, còn `check` xác nhận parent thật sự của slot.

Ưu điểm:

```text
compact hơn object-trie
array locality tốt
lookup nhanh
```

Nhược điểm là construction/cập nhật (update / 업데이트) phức tạp và quản lý slot trống khó hơn.

LOUDS biểu diễn cây theo level-order bằng bitvector và rank/select, nên child navigation không cần pointer cho từng node. Nếu các suffix/outputs có thể chia sẻ, finite-state transducer hoặc minimal automaton còn nén cả ngôn ngữ được nhận.

## 20. Succinct Trie và LOUDS

Nếu dictionary rất lớn và gần tĩnh, có thể biểu diễn topology bằng bitvector thay vì pointer per nút (node / 노드).

**LOUDS (Level-Order Unary Degree Sequence)** mã hóa bậc nút (node / 노드) theo mức (level / 수준) thứ tự (order / 순서) và dùng rank/select để điều hướng.

Mục tiêu không còn là “mã (code / 코드) dễ nhất” mà là giảm bits per nút (node / 노드) tới gần giới hạn thông tin.

Đây là ví dụ succinct cấu trúc dữ liệu (data structure / 자료구조): vẫn hỗ trợ điều hướng (navigation / 내비게이션) nhưng với bộ nhớ (memory / 메모리) gần tối ưu hơn pointer đồ thị (graph / 그래프).

Minimal automaton hợp nhất các suffix-equivalent states, còn FST có thể ánh xạ key sang output như trọng số hoặc ID. So sánh với hash table giúp xác định khi prefix và thứ tự có thực sự cần thiết.

## 21. Finite-State Transducer / Minimal Automaton

Nếu dictionary tĩnh có nhiều suffix giống nhau, Trie chỉ chia sẻ prefix; các suffix giống nhau ở các nhánh khác vẫn bị lặp.

Minimal acyclic finite-state automaton hoặc FST có thể gộp các trạng thái tương đương phía sau, chia sẻ cả suffix cấu trúc (structure / 구조).

Điều này đặc biệt mạnh trong dictionary/search-engine indexing.

Mô hình tư duy:

```text
Trie       -> chia sẻ prefix
minimal DFA/FST -> chia sẻ các continuation tương đương
```

Hash table thường tốt cho exact lookup với footprint hợp lý, nhưng không tự hỗ trợ prefix enumeration hay lexicographic order. Sorted array có locality và binary search tốt, nhưng insert và prefix range có thể tốn chi phí di chuyển.

## 22. Trie vs bảng băm (hash table / 해시 테이블)

Bảng băm (hash table / 해시 테이블) tốt hơn khi chỉ cần chính xác (exact / 정확한) lookup và bộ nhớ (memory / 메모리) overhead Trie không đáng.

Trie tốt khi truy vấn (query / 쿼리) quan tâm:

```text
prefix
longest-prefix
lexicographic traversal
prefix count
structure bên trong key
```

Không nên chọn Trie chỉ vì key là string.

Sorted array phù hợp dữ liệu tĩnh và scan theo range nhờ cache locality; trie phù hợp khi prefix navigation là thao tác chính và key biến động. TreeMap cung cấp thứ tự động bằng balanced search tree, với trade-off khác về node và comparator.

## 23. Trie vs Sorted Array

Dictionary tĩnh có thể dùng sorted array + tìm kiếm nhị phân (binary search / 이진 탐색) để tìm prefix phạm vi (range / 범위).

Ưu điểm:

```text
memory gọn
cache-friendly
simple serialization
```

Trie mạnh hơn khi động (dynamic / 동적) cập nhật (update / 업데이트), prefix siêu dữ liệu (metadata / 메타데이터) hoặc character-by-character traversal là trung tâm.

Đối với tải công việc (workload / 워크로드) static, sorted array đôi khi thực dụng hơn Trie.

TreeMap so sánh toàn bộ key tại mỗi level của cây và hỗ trợ ordered map tổng quát, còn trie phân rã key theo ký tự hoặc token. Với text thực, đơn vị ký tự và chuẩn hóa Unicode có thể thay đổi hoàn toàn path.

## 24. Trie vs TreeMap

TreeMap giữ full key thứ tự (order / 순서). Prefix truy vấn (query / 쿼리) có thể chuyển thành phạm vi (range / 범위) trong lexicographic thứ tự (order / 순서).

Nhưng mỗi comparator có thể phải so lại nhiều prefix character ở nhiều cây (tree / 트리) nút (node / 노드).

Trie chia sẻ phần prefix đã duyệt một lần, nhưng trả giá bằng nhiều nút (node / 노드) hơn.

Không có lựa chọn tốt nhất nếu chưa biết key length, cập nhật (update / 업데이트) tỷ lệ (rate / 비율) và truy vấn (query / 쿼리) mix.

Unicode không đồng nhất với byte hay code point; grapheme cluster và normalization có thể khiến hai chuỗi nhìn giống nhau nhưng có path khác. Case folding cũng phải được định nghĩa theo locale hoặc theo chuẩn bất biến trước khi insert/search.

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

`é` có thể được biểu diễn trực tiếp hoặc bằng `e + combining mark`. Nếu không normalize, hai string người dùng nhìn giống nhau có thể đi theo hai đường dẫn (path / 경로) khác nhau.

String chỉ mục (index / 인덱스) môi trường vận hành (production / 운영 환경) phải xác định normalization chính sách (policy / 정책) trước khi xây Trie.

Case folding theo locale có thể không bảo toàn một ánh xạ đơn giản giữa ký tự và ký tự, nên pipeline phải thống nhất quy tắc cho cả ghi và đọc. Sau khi chốt representation, allocation trở thành yếu tố quyết định footprint và tốc độ.

## 26. trường hợp (case / 사례) Folding và Locale

Autocomplete/tìm kiếm (search / 검색) không phân biệt hoa thường có thể cần trường hợp (case / 사례) folding. Nhưng ánh xạ (mapping / 매핑) chữ thường không luôn là phép một-ký-tự thành một-ký-tự ở mọi ngôn ngữ.

Nếu normalization/trường hợp (case / 사례) folding là một phần của định danh (identity / 식별자), phải thực hiện nhất quán cả lúc insert và truy vấn (query / 쿼리).

Băm (hash / 해시)/equality và Trie đường dẫn (path / 경로) đều phụ thuộc cùng canonicalization đặc tả hợp đồng (contract / 계약).

Trie allocation tạo nhiều object nhỏ có thể gây fragmentation và pointer overhead; arena hoặc packed arrays thường cải thiện locality. Layout allocation tốt chỉ phát huy khi truy cập cũng đi theo cache-friendly pattern.

## 27. bộ nhớ (memory / 메모리) Allocation

Trong C, cấp phát từng nút (node / 노드) bằng `malloc` có thể đắt. Arena allocator thường rất phù hợp vì nhiều Trie nút (node / 노드) có cùng vòng đời.

Trong Java/JavaScript, nhiều đối tượng (object / 객체) nhỏ tạo pressure lên GC.

Mảng nút (node / 노드) + integer child chỉ mục (index / 인덱스) có thể giảm đối tượng (object / 객체) overhead, đặc biệt với dictionary lớn.

Cache locality phụ thuộc children layout, độ rộng node và thứ tự duyệt; pointer-rich trie có thể chậm dù số phép so sánh nhỏ. Persistent trie đổi mục tiêu sang chia sẻ các path cũ giữa nhiều phiên bản.

## 28. bộ nhớ đệm (cache / 캐시) Locality

Pointer-heavy Trie có lookup `O(L)` nhưng mỗi bước có thể gây trượt bộ nhớ đệm (cache miss / 캐시 미스).

Radix compression giảm số nút (node / 노드) truy cập. Double-array hoặc compact arrays tăng locality.

Big-O `O(L)` không nói bao nhiêu bộ nhớ đệm (cache / 캐시) line phải chạm.

Persistent trie copy-on-write các node trên path thay đổi và dùng chung phần còn lại, nên mỗi version có thể được truy cập như snapshot. Khi nhiều thread cùng đọc/ghi một phiên bản, cần thêm concurrency protocol.

## 29. Persistent Trie

Nếu cần nhiều phiên bản (version / 버전), cập nhật (update / 업데이트) một key chỉ thay các nút (node / 노드) trên đường dẫn (path / 경로) của key. Có thể sao chép đường dẫn (path / 경로) rồi chia sẻ toàn bộ phần còn lại.

Persistent Trie hữu ích cho:

```text
versioned dictionary
XOR query theo prefix phiên bản
functional maps
snapshot
```

Chi phí cập nhật (update / 업데이트) thường tỷ lệ độ dài key hoặc số bit.

Concurrent trie cần bảo vệ split, delete và cập nhật terminal/count mà không làm reader thấy path dở dang; immutable hoặc copy-on-write có thể giảm lock contention. Trong database/search system, durability, refresh và query ranking còn quan trọng không kém cấu trúc trie.

## 30. Concurrent Trie

Fine-grained locking hoặc lock-free Trie phức tạp vì insert/delete thay đổi child pointers và thời gian tồn tại (lifetime / 수명) nút (node / 노드).

Radix cây (tree / 트리) còn có split/merge edge, làm atomic cập nhật (update / 업데이트) khó hơn.

Trong read-mostly tải công việc (workload / 워크로드), immutable snapshot + sao chép khi ghi (copy-on-write / 쓰기 시 복사) có thể đơn giản hơn mutable concurrent cây (tree / 트리).

Trong hệ thống tìm kiếm, trie có thể làm dictionary, autocomplete index hoặc lớp tiền lọc, nhưng phải nối với storage và ranking có provenance rõ. Kiểm thử cần bao phủ cả semantics của query lẫn lifecycle cập nhật.

## 31. Trie trong cơ sở dữ liệu (database / 데이터베이스)/tìm kiếm (search / 검색) hệ thống (system / 시스템)

Trie/Radix cây (tree / 트리) có thể dùng cho:

```text
term dictionary
autocomplete
routing
prefix-compressed index key
in-memory ordered key index
```

B+cây (tree / 트리) page cũng có thể dùng prefix compression giữa các key gần nhau để giảm lưu trữ (storage / 저장소). Ý tưởng chia sẻ prefix xuất hiện ngoài Trie thuần túy.

Test trie nên kiểm tra insert/search/delete, prefix enumeration, Unicode normalization, duplicate key và phiên bản concurrent/persistent nếu có. Validator tự động hóa các invariant để phát hiện lỗi cấu trúc trước khi đo hiệu năng.

## 32. Kiểm thử

Các trường hợp (case / 사례) quan trọng:

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

Với Trie tự cài, có thể differential-test chính xác (exact / 정확한) lookup với băm (hash / 해시) Set và prefix truy vấn (query / 쿼리) với brute-force filter trên tập string nhỏ.

Validator có thể kiểm tra mọi output tìm được thật sự mang prefix, terminal/count không âm, children không trùng nhãn và round-trip serialization. Những lỗi còn lại thường đến từ việc suy diễn quá mức complexity hoặc xem trie là lựa chọn mặc định.

## 33. Validator

Nếu có `passCount/endCount`, có thể kiểm tra:

```text
passCount >= endCount
passCount phù hợp tổng subtree theo convention
không node rác có passCount 0 nếu policy yêu cầu thu hồi
mọi child symbol unique
```

Radix cây (tree / 트리) còn cần kiểm tra không có hai outgoing edge bắt đầu bằng cùng symbol và không có unary nút (node / 노드) nếu biểu diễn (representation / 표현) yêu cầu compression tối đa.

Trie không luôn tiết kiệm hơn hash table, không tự giải quyết Unicode, và prefix query vẫn phải trả chi phí theo số kết quả. Mô hình tư duy cuối bài sẽ đặt các trade-off này cạnh workload và invariant cụ thể.

## 34. Những hiểu lầm phổ biến

“Trie lookup O(L) nên luôn nhanh hơn HashMap” — sai; constant factor và bộ nhớ (memory / 메모리) locality rất khác.

“Trie chỉ dùng cho từ tiếng Anh” — sai; key có thể là byte, bit, đơn vị từ (token / 토큰) hoặc mã (code / 코드) điểm (point / 지점).

“Prefix truy vấn (query / 쿼리) luôn cần Trie” — sai; sorted array/static dictionary có thể đơn giản hơn.

“Unicode string có thể chỉ mục (index / 인덱스) theo `char` mà không cần chính sách (policy / 정책)” — sai với nhiều miền người dùng thực tế.

“Compressed Trie chỉ là Trie ít nút (node / 노드) hơn” — đúng ở mức ý tưởng nhưng cập nhật (update / 업데이트)/split invariants phức tạp hơn nhiều.

Mô hình tư duy của trie là: chọn đơn vị key, giữ path invariant, chọn layout children, rồi tối ưu memory, locality và concurrency theo query. Các liên kết cuối bài giúp so sánh trie với hash, sorted structures và automata.

## Mô hình tư duy

> Trie biến **prefix từ một quan hệ ngầm trong khóa thành một trạng thái tường minh trong cấu trúc**. Nhờ đó truy vấn (query / 쿼리) prefix không phải so lại toàn bộ keyspace.

Khi cân nhắc Trie, hãy hỏi: **truy vấn (query / 쿼리) có thực sự cần prefix không, alphabet/normalization là gì, branching factor thế nào, dictionary static hay động (dynamic / 동적), bộ nhớ (memory / 메모리) overhead có chấp nhận được không, và có cần compression/ranking/persistence/tính đồng thời (concurrency / 동시성) không?**

Xem thêm: [String Algorithms](../05_specialized/00_string_algorithms.md), [Suffix Structures](../05_specialized/04_suffix_arrays_suffix_trees_and_lcp.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [B/B+Tree](./05_b_trees_and_external_memory.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
