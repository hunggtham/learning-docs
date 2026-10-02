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

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **2. tìm kiếm (search / 검색) và Insert** tiếp nhận điểm tựa từ **1. Khi nào Trie đáng dùng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Prefix truy vấn (query / 쿼리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **3. Prefix truy vấn (query / 쿼리)** tiếp nhận điểm tựa từ **2. tìm kiếm (search / 검색) và Insert** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Bất biến quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Prefix truy vấn (query / 쿼리)

Để kiểm tra `startsWith(prefix)`, chỉ cần đi hết prefix. Không cần nút cuối là `isEnd`.

Nếu cần liệt kê mọi kết quả, độ phức tạp (complexity / 복잡도) phải tính cả đầu ra (output / 출력):

\[
O(|prefix| + k + \text{characters emitted})
\]

với `k` là số kết quả.

Một hệ thống autocomplete không thể trả một triệu gợi ý trong `O(|prefix|)` chỉ vì Trie tìm prefix nhanh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **4. Bất biến quan trọng** tiếp nhận điểm tựa từ **3. Prefix truy vấn (query / 쿼리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Child biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **5. Child biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **4. Bất biến quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Bộ nhớ là điểm yếu lớn của Trie ngây thơ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **6. Bộ nhớ là điểm yếu lớn của Trie ngây thơ** tiếp nhận điểm tựa từ **5. Child biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Delete** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **7. Delete** tiếp nhận điểm tựa từ **6. Bộ nhớ là điểm yếu lớn của Trie ngây thơ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Lexicographic Traversal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Delete

Xóa `car` khi vẫn còn `card` không được giải phóng toàn đường dẫn (path / 경로) `c-a-r`.

Quy trình:

1. đi tới terminal;
2. giảm `endCount` hoặc clear `isEnd`;
3. đi ngược lên;
4. chỉ xóa nút (node / 노드) nếu không còn child, không còn key kết thúc và siêu dữ liệu (metadata / 메타데이터) cho phép.

Nếu có `passCount`, nút (node / 노드) có thể được thu hồi khi count xuống 0.

Delete là nơi shared-prefix quyền sở hữu (ownership / 소유권) trở nên rõ nhất.

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **8. Lexicographic Traversal** tiếp nhận điểm tựa từ **7. Delete** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Radix cây (tree / 트리) / Patricia Trie** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Lexicographic Traversal

Nếu child được duyệt theo symbol thứ tự (order / 순서), DFS xuất key theo thứ tự từ điển.

Nếu child dùng băm (hash / 해시) Map, iteration thứ tự (order / 순서) có thể không tương ứng lexicographic thứ tự (order / 순서); cần sort symbol hoặc dùng ordered biểu diễn (representation / 표현).

Đây là một ví dụ thứ tự (order / 순서) ngữ nghĩa (semantics / 의미론) ảnh hưởng trực tiếp bố cục (layout / 레이아웃).

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **9. Radix cây (tree / 트리) / Patricia Trie** tiếp nhận điểm tựa từ **8. Lexicographic Traversal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Split Edge khi Insert vào Radix cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Radix cây (tree / 트리) / Patricia Trie

Trie ngây thơ có thể có chuỗi dài các nút (node / 노드) chỉ có một child:

```text
c -> o -> m -> p -> u -> t -> e
```

Đường dẫn (path / 경로) compression gộp thành một cạnh nhãn `"compute"`.

**Radix cây (tree / 트리) / Patricia Trie** giảm số nút (node / 노드), pointer và cấp phát. tìm kiếm (search / 검색) phải so nhiều symbol trên mỗi cạnh, nhưng tổng ký tự xử lý vẫn gắn với độ dài khóa.

Đường dẫn (path / 경로) compression đặc biệt hữu ích khi key dài nhưng branching xảy ra ít.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **10. Split Edge khi Insert vào Radix cây (tree / 트리)** tiếp nhận điểm tựa từ **9. Radix cây (tree / 트리) / Patricia Trie** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Patricia Trie và Bit Prefix** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **11. Patricia Trie và Bit Prefix** tiếp nhận điểm tựa từ **10. Split Edge khi Insert vào Radix cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Longest Prefix Match** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **12. Longest Prefix Match** tiếp nhận điểm tựa từ **11. Patricia Trie và Bit Prefix** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. nhị phân (binary / 이진) Trie và Maximum XOR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Longest Prefix Match

Duyệt key từ gốc, đồng thời ghi nhớ terminal nút (node / 노드) gần nhất đã gặp.

Khi không còn edge phù hợp, terminal gần nhất chính là longest matching prefix.

Đây là mẫu (pattern / 패턴) quan trọng trong routing và quy tắc (rule / 규칙) matching.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **13. nhị phân (binary / 이진) Trie và Maximum XOR** tiếp nhận điểm tựa từ **12. Longest Prefix Match** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Count theo Prefix** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. nhị phân (binary / 이진) Trie và Maximum XOR

Một integer có thể xem như chuỗi bit cố định `W` bit.

Muốn maximize `x XOR y`, tại bit hiện tại của `x`, ưu tiên branch có bit đối nghịch nếu tồn tại.

```text
x bit = 0 -> ưu tiên y bit = 1
x bit = 1 -> ưu tiên y bit = 0
```

Với word width cố định, insert/truy vấn (query / 쿼리) là `O(W)`.

Nhị phân (binary / 이진) Trie minh họa rằng Trie không chỉ dành cho văn bản (text / 텍스트); bất kỳ key có cấu trúc tuần tự đều có thể được chỉ mục (index / 인덱스) theo prefix.

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **14. Count theo Prefix** tiếp nhận điểm tựa từ **13. nhị phân (binary / 이진) Trie và Maximum XOR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Autocomplete không chỉ là Trie** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **15. Autocomplete không chỉ là Trie** tiếp nhận điểm tựa từ **14. Count theo Prefix** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Best-First Autocomplete** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **16. Best-First Autocomplete** tiếp nhận điểm tựa từ **15. Autocomplete không chỉ là Trie** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Aho–Corasick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Best-First Autocomplete

Nếu mỗi nút (node / 노드) có `maxScore` của subtree, ta không cần bộ nhớ đệm (cache / 캐시) toàn Top-K tại từng prefix. Sau khi tới prefix nút (node / 노드), có thể dùng priority hàng đợi (queue / 큐) ưu tiên subtree có upper bound lớn nhất.

Đây là một bài branch-and-bound nhỏ:

```text
state = trie node
upper bound = max score dưới node
```

Khi đã tìm đủ K kết quả (result / 결과) và bound còn lại không thể thắng, dừng.

Trie có thể kết hợp vùng nhớ động (heap / 힙) để tạo ranking tìm kiếm (search / 검색) thay vì chỉ DFS toàn subtree.

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **17. Aho–Corasick** tiếp nhận điểm tựa từ **16. Best-First Autocomplete** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. thất bại (failure / 실패) Link như tái sử dụng trạng thái** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Aho–Corasick

Nếu có nhiều mẫu (pattern / 패턴) và cần quét một văn bản (text / 텍스트) một lần, chạy tìm kiếm (search / 검색) riêng cho từng mẫu (pattern / 패턴) hoặc restart Trie từ từng vị trí là tốn kém.

Aho–Corasick thêm **thất bại (failure / 실패) link**.

Khi chuyển tiếp (transition / 전이) thất bại, automaton chuyển tới suffix dài nhất của prefix hiện tại cũng là prefix của một mẫu (pattern / 패턴).

Sau preprocessing dictionary, matching chạy gần:

\[
O(|text| + \text{number of matches})
\]

với các giả định biểu diễn (representation / 표현) phù hợp.

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **18. thất bại (failure / 실패) Link như tái sử dụng trạng thái** tiếp nhận điểm tựa từ **17. Aho–Corasick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Double-Array Trie** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. thất bại (failure / 실패) Link như tái sử dụng trạng thái

Thất bại (failure / 실패) link có cùng tinh thần với KMP prefix hàm (function / 함수) và suffix link:

> Khi ngữ cảnh (context / 맥락) dài không còn hợp lệ, đừng quay về trạng thái rỗng; tái sử dụng suffix dài nhất còn có ý nghĩa.

Đây là motif rất sâu trong string algorithms.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **19. Double-Array Trie** tiếp nhận điểm tựa từ **18. thất bại (failure / 실패) Link như tái sử dụng trạng thái** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Succinct Trie và LOUDS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **20. Succinct Trie và LOUDS** tiếp nhận điểm tựa từ **19. Double-Array Trie** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Finite-State Transducer / Minimal Automaton** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Succinct Trie và LOUDS

Nếu dictionary rất lớn và gần tĩnh, có thể biểu diễn topology bằng bitvector thay vì pointer per nút (node / 노드).

**LOUDS (Level-Order Unary Degree Sequence)** mã hóa bậc nút (node / 노드) theo mức (level / 수준) thứ tự (order / 순서) và dùng rank/select để điều hướng.

Mục tiêu không còn là “mã (code / 코드) dễ nhất” mà là giảm bits per nút (node / 노드) tới gần giới hạn thông tin.

Đây là ví dụ succinct cấu trúc dữ liệu (data structure / 자료구조): vẫn hỗ trợ điều hướng (navigation / 내비게이션) nhưng với bộ nhớ (memory / 메모리) gần tối ưu hơn pointer đồ thị (graph / 그래프).

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **21. Finite-State Transducer / Minimal Automaton** tiếp nhận điểm tựa từ **20. Succinct Trie và LOUDS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Trie vs bảng băm (hash table / 해시 테이블)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Finite-State Transducer / Minimal Automaton

Nếu dictionary tĩnh có nhiều suffix giống nhau, Trie chỉ chia sẻ prefix; các suffix giống nhau ở các nhánh khác vẫn bị lặp.

Minimal acyclic finite-state automaton hoặc FST có thể gộp các trạng thái tương đương phía sau, chia sẻ cả suffix cấu trúc (structure / 구조).

Điều này đặc biệt mạnh trong dictionary/search-engine indexing.

Mô hình tư duy:

```text
Trie       -> chia sẻ prefix
minimal DFA/FST -> chia sẻ các continuation tương đương
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **22. Trie vs bảng băm (hash table / 해시 테이블)** tiếp nhận điểm tựa từ **21. Finite-State Transducer / Minimal Automaton** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Trie vs Sorted Array** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **23. Trie vs Sorted Array** tiếp nhận điểm tựa từ **22. Trie vs bảng băm (hash table / 해시 테이블)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Trie vs TreeMap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **24. Trie vs TreeMap** tiếp nhận điểm tựa từ **23. Trie vs Sorted Array** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Unicode** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Trie vs TreeMap

TreeMap giữ full key thứ tự (order / 순서). Prefix truy vấn (query / 쿼리) có thể chuyển thành phạm vi (range / 범위) trong lexicographic thứ tự (order / 순서).

Nhưng mỗi comparator có thể phải so lại nhiều prefix character ở nhiều cây (tree / 트리) nút (node / 노드).

Trie chia sẻ phần prefix đã duyệt một lần, nhưng trả giá bằng nhiều nút (node / 노드) hơn.

Không có lựa chọn tốt nhất nếu chưa biết key length, cập nhật (update / 업데이트) tỷ lệ (rate / 비율) và truy vấn (query / 쿼리) mix.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **25. Unicode** tiếp nhận điểm tựa từ **24. Trie vs TreeMap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. trường hợp (case / 사례) Folding và Locale** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **25. Unicode** cho ta quy tắc; **26. trường hợp (case / 사례) Folding và Locale** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **27. bộ nhớ (memory / 메모리) Allocation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. trường hợp (case / 사례) Folding và Locale

Autocomplete/tìm kiếm (search / 검색) không phân biệt hoa thường có thể cần trường hợp (case / 사례) folding. Nhưng ánh xạ (mapping / 매핑) chữ thường không luôn là phép một-ký-tự thành một-ký-tự ở mọi ngôn ngữ.

Nếu normalization/trường hợp (case / 사례) folding là một phần của định danh (identity / 식별자), phải thực hiện nhất quán cả lúc insert và truy vấn (query / 쿼리).

Băm (hash / 해시)/equality và Trie đường dẫn (path / 경로) đều phụ thuộc cùng canonicalization đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **26. trường hợp (case / 사례) Folding và Locale** cho ta quy tắc; **27. bộ nhớ (memory / 메모리) Allocation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **28. bộ nhớ đệm (cache / 캐시) Locality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. bộ nhớ (memory / 메모리) Allocation

Trong C, cấp phát từng nút (node / 노드) bằng `malloc` có thể đắt. Arena allocator thường rất phù hợp vì nhiều Trie nút (node / 노드) có cùng vòng đời.

Trong Java/JavaScript, nhiều đối tượng (object / 객체) nhỏ tạo pressure lên GC.

Mảng nút (node / 노드) + integer child chỉ mục (index / 인덱스) có thể giảm đối tượng (object / 객체) overhead, đặc biệt với dictionary lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **28. bộ nhớ đệm (cache / 캐시) Locality** tiếp nhận điểm tựa từ **27. bộ nhớ (memory / 메모리) Allocation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Persistent Trie** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. bộ nhớ đệm (cache / 캐시) Locality

Pointer-heavy Trie có lookup `O(L)` nhưng mỗi bước có thể gây trượt bộ nhớ đệm (cache miss / 캐시 미스).

Radix compression giảm số nút (node / 노드) truy cập. Double-array hoặc compact arrays tăng locality.

Big-O `O(L)` không nói bao nhiêu bộ nhớ đệm (cache / 캐시) line phải chạm.

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **29. Persistent Trie** tiếp nhận điểm tựa từ **28. bộ nhớ đệm (cache / 캐시) Locality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Concurrent Trie** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **30. Concurrent Trie** tiếp nhận điểm tựa từ **29. Persistent Trie** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Trie trong cơ sở dữ liệu (database / 데이터베이스)/tìm kiếm (search / 검색) hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Concurrent Trie

Fine-grained locking hoặc lock-free Trie phức tạp vì insert/delete thay đổi child pointers và thời gian tồn tại (lifetime / 수명) nút (node / 노드).

Radix cây (tree / 트리) còn có split/merge edge, làm atomic cập nhật (update / 업데이트) khó hơn.

Trong read-mostly tải công việc (workload / 워크로드), immutable snapshot + sao chép khi ghi (copy-on-write / 쓰기 시 복사) có thể đơn giản hơn mutable concurrent cây (tree / 트리).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **30. Concurrent Trie** nêu điều cần giải thích; **31. Trie trong cơ sở dữ liệu (database / 데이터베이스)/tìm kiếm (search / 검색) hệ thống (system / 시스템)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **32. Kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **31. Trie trong cơ sở dữ liệu (database / 데이터베이스)/tìm kiếm (search / 검색) hệ thống (system / 시스템)** nêu điều cần giải thích; **32. Kiểm thử** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **33. Validator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trie và các cấu trúc chỉ mục tiền tố**, **33. Validator** tiếp nhận điểm tựa từ **32. Kiểm thử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Validator

Nếu có `passCount/endCount`, có thể kiểm tra:

```text
passCount >= endCount
passCount phù hợp tổng subtree theo convention
không node rác có passCount 0 nếu policy yêu cầu thu hồi
mọi child symbol unique
```

Radix cây (tree / 트리) còn cần kiểm tra không có hai outgoing edge bắt đầu bằng cùng symbol và không có unary nút (node / 노드) nếu biểu diễn (representation / 표현) yêu cầu compression tối đa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trie và các cấu trúc chỉ mục tiền tố**, **34. Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **33. Validator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Những hiểu lầm phổ biến

“Trie lookup O(L) nên luôn nhanh hơn HashMap” — sai; constant factor và bộ nhớ (memory / 메모리) locality rất khác.

“Trie chỉ dùng cho từ tiếng Anh” — sai; key có thể là byte, bit, đơn vị từ (token / 토큰) hoặc mã (code / 코드) điểm (point / 지점).

“Prefix truy vấn (query / 쿼리) luôn cần Trie” — sai; sorted array/static dictionary có thể đơn giản hơn.

“Unicode string có thể chỉ mục (index / 인덱스) theo `char` mà không cần chính sách (policy / 정책)” — sai với nhiều miền người dùng thực tế.

“Compressed Trie chỉ là Trie ít nút (node / 노드) hơn” — đúng ở mức ý tưởng nhưng cập nhật (update / 업데이트)/split invariants phức tạp hơn nhiều.

> **Chuyển mạch:** Trong **Trie và các cấu trúc chỉ mục tiền tố**, **Mô hình tư duy** gom các mảnh từ **34. Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Trie biến **prefix từ một quan hệ ngầm trong khóa thành một trạng thái tường minh trong cấu trúc**. Nhờ đó truy vấn (query / 쿼리) prefix không phải so lại toàn bộ keyspace.

Khi cân nhắc Trie, hãy hỏi: **truy vấn (query / 쿼리) có thực sự cần prefix không, alphabet/normalization là gì, branching factor thế nào, dictionary static hay động (dynamic / 동적), bộ nhớ (memory / 메모리) overhead có chấp nhận được không, và có cần compression/ranking/persistence/tính đồng thời (concurrency / 동시성) không?**

Xem thêm: [String Algorithms](../05_specialized/00_string_algorithms.md), [Suffix Structures](../05_specialized/04_suffix_arrays_suffix_trees_and_lcp.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [B/B+Tree](./05_b_trees_and_external_memory.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
