# Suffix Array, Suffix Tree và LCP
**Suffix Array, Suffix Tree, LCP / 접미사 배열, 접미사 트리, LCP**

Nhiều bài string không hỏi về prefix của toàn string mà hỏi về **mọi substring**: pattern có xuất hiện không, substring lặp dài nhất là gì, hai suffix giống nhau bao lâu, có bao nhiêu distinct substrings, hay longest common substring giữa hai strings là gì.

Nếu index từng substring trực tiếp, số substring của string length `n` là `O(n^2)`. Suffix structures tránh lưu toàn bộ set này bằng một observation quan trọng: **mọi substring là prefix của một suffix nào đó**.

Vì vậy thay vì index tất cả substrings, ta tổ chức các suffixes và khai thác shared prefixes.

## 1. Suffix là gì?

Với string `banana`:

```text
index  suffix
0      banana
1      anana
2      nana
3      ana
4      na
5      a
```

Có đúng `n` suffixes, một suffix bắt đầu tại mỗi position.

Mọi substring `s[l..r]` là prefix của suffix bắt đầu tại `l`. Đây là lý do suffix indexing đủ để answer substring queries.

## 2. Suffix Array

**Suffix Array (SA / 접미사 배열)** là array các starting indices của suffixes theo lexicographic order.

Với `banana`:

```text
5: a
3: ana
1: anana
0: banana
4: na
2: nana
```

Suffix Array là:

```text
[5, 3, 1, 0, 4, 2]
```

SA không lưu suffix strings riêng biệt. Nó chỉ lưu indices vào original text, nên compact hơn suffix trie/tree ở mức constant factors và locality thường tốt hơn.

## 3. Vì sao substring search trở thành binary search?

Trong lexicographically sorted suffixes, tất cả suffixes bắt đầu bằng cùng pattern tạo một contiguous interval.

Ví dụ pattern `ana` trong `banana` match suffixes `ana` và `anana`, nằm cạnh nhau trong suffix order.

Ta có thể binary search lower bound và upper bound của pattern trên SA. Nếu mỗi comparison pattern-với-suffix mất `O(m)` cho pattern length `m`, query đơn giản là:

\[
O(m\log n)
\]

với preprocessing SA tách riêng.

Điểm quan trọng là sorting suffixes biến substring search thành ordered search.

## 4. Naive suffix construction quá đắt

Nếu tạo mọi suffix string rồi sort, ta có `n` strings với total character storage `O(n^2)`. Comparison giữa suffixes cũng có thể tốn `O(n)`.

Naive approach vì thế có thể lên tới `O(n^2 log n)` hoặc tệ hơn tùy implementation.

Suffix-array algorithms tốt hơn tránh materialize mọi suffix, thay vào đó sort suffixes bằng **ranks** đại diện cho prefixes ngày càng dài.

## 5. Prefix-doubling construction

Một cách học rất thực dụng để xây SA là doubling.

Ban đầu sort suffixes theo ký tự đầu tiên, tức prefix length 1. Mỗi suffix có một rank.

Sau đó để sort theo first 2 characters, suffix tại `i` được đại diện bởi pair:

```text
(rank[i], rank[i + 1])
```

Tiếp theo prefix length 4 dùng:

```text
(rank[i], rank[i + 2])
```

rồi 8, 16, ...

Ở step với length `2^k`, pair ranks của hai halves size `2^{k-1}` đủ mô tả order của prefix đó.

Nếu mỗi round sort `n` pairs bằng comparison sort, complexity thường:

\[
O(n\log^2 n)
\]

Có thể giảm còn `O(n log n)` bằng counting/radix sort trên integer ranks.

## 6. Sentinel và boundary handling

Khi `i + len` vượt string, rank của phần ngoài thường dùng một sentinel nhỏ hơn mọi valid rank, ví dụ `-1`.

Nếu append một terminal character `$` nhỏ hơn mọi alphabet character, suffix order đôi khi dễ reason hơn. Nhưng sentinel phải thực sự unique và ordering phải rõ.

Boundary semantics nhỏ này ảnh hưởng trực tiếp correctness của construction.

## 7. Rank array

Nếu `SA[pos] = suffixStart`, rank array là inverse:

```text
rank[suffixStart] = pos
```

Rank cho biết suffix bắt đầu tại index `i` đứng ở vị trí nào trong suffix order.

Nó là bridge giữa original text order và suffix-array order, đặc biệt quan trọng cho Kasai LCP algorithm.

## 8. LCP Array

**LCP (Longest Common Prefix / 최장 공통 접두사)** array lưu độ dài common prefix giữa hai suffixes kề nhau trong suffix order.

Nếu:

```text
SA = [5, 3, 1, 0, 4, 2]
```

thì một convention phổ biến là:

```text
LCP[i] = lcp(SA[i-1], SA[i])
```

với `LCP[0] = 0`.

LCP biến nhiều substring questions thành array/range questions.

## 9. Longest Repeated Substring

Nếu một substring xuất hiện ít nhất hai lần, có ít nhất hai suffixes chia sẻ prefix đó.

Trong sorted suffix order, những suffixes có common prefix lớn sẽ nằm gần nhau. Vì vậy length của longest repeated substring chính là:

```text
max(LCP)
```

Nếu cần substring thật, lấy starting index từ suffix pair tương ứng.

Đây là một kết quả đẹp: một problem trên `O(n^2)` substrings biến thành maximum trên array size `O(n)` sau preprocessing.

## 10. Kasai Algorithm xây LCP trong O(n)

Naive tính LCP cho mỗi pair adjacent suffixes từ đầu có thể tốn `O(n^2)` trong strings có nhiều prefix lặp.

Kasai tận dụng property rằng nếu suffix `i` và một neighbor trong suffix order có LCP length `h`, thì khi chuyển sang suffix `i+1`, common prefix candidate thường ít nhất `h-1` trước khi tiếp tục compare.

Algorithm duy trì `h`, decrement tối đa 1 mỗi step của original index, còn mỗi character comparison làm `h` tăng. Tổng số tăng/giảm bị bounded tuyến tính, nên total `O(n)`.

Đây là một dạng amortized reasoning rất hay trong string algorithms.

## 11. LCP giữa hai suffix bất kỳ

Nếu muốn LCP của suffixes đứng tại positions `i` và `j` trong suffix order, answer là minimum LCP trên interval giữa chúng:

\[
LCP(SA[i], SA[j]) = \min LCP[i+1..j]
\]

Do đó sau khi có LCP array, ta có thể xây RMQ structure như Sparse Table hoặc Segment Tree.

Với static text và nhiều LCP queries, Sparse Table cho preprocessing `O(n log n)` và query `O(1)`.

Suffix structure vì thế kết nối trực tiếp với range-query structures.

## 12. Count Distinct Substrings

Tổng số substrings của string length `n` là:

\[
\frac{n(n+1)}{2}
\]

Nếu xét suffixes theo lexicographic order, suffix tại SA position `i` đóng góp length của nó trừ phần prefix đã xuất hiện trong suffix trước, tức trừ `LCP[i]`.

Số distinct substrings:

\[
\frac{n(n+1)}{2} - \sum LCP[i]
\]

Đây là một ứng dụng rất trực tiếp của LCP như “amount of duplicate prefix information”.

## 13. Longest Common Substring giữa hai strings

Ghép hai strings bằng separator unique:

```text
A + '#' + B
```

xây SA và LCP. Longest common substring phải xuất hiện như common prefix giữa một suffix từ A và một suffix từ B.

Ta scan adjacent suffixes thuộc hai source khác nhau và lấy maximum LCP phù hợp.

Separator phải không xuất hiện trong inputs và ordering semantics phải rõ.

## 14. Pattern occurrences

Binary search trên SA có thể tìm range suffixes bắt đầu bằng pattern. Kích thước interval đó chính là số occurrences nếu overlapping occurrences được tính theo starting positions.

Nếu cần list positions, các SA entries trong interval là starting positions. Nếu cần output theo text order, có thể sort positions hoặc dùng structure phụ.

## 15. Suffix Tree

**Suffix Tree / 접미사 트리** là compressed trie của tất cả suffixes.

Naive suffix trie có thể có `O(n^2)` nodes/characters. Path compression gộp chains một-child thành một edge label đại diện substring của original text, thường lưu bằng `(start,end)` indices thay vì copy string.

Suffix tree có `O(n)` nodes trong construction chuẩn với terminal symbol và assumptions thích hợp.

Mỗi path từ root biểu diễn một substring. Vì thế pattern search đi theo edge labels theo `O(m)` về mặt character work trong ideal representation.

## 16. Tại sao Suffix Tree khó implement?

Một naive build insert từng suffix vẫn `O(n^2)`. Algorithms như Ukkonen xây online trong linear time nhưng cần suffix links, active point, implicit/explicit nodes và careful edge handling.

Implementation complexity và object/pointer overhead lớn khiến suffix array thường thực dụng hơn cho many static-text workloads.

Suffix tree vẫn rất quan trọng để hiểu compressed suffix structure và nhiều theoretical algorithms.

## 17. Suffix Links

Trong suffix tree construction, suffix link thường nối node đại diện string `xα` tới node đại diện `α`. Nó cho phép chuyển nhanh từ context hiện tại sang suffix context ngắn hơn mà không quay lại root.

Concept này phản ánh recurring idea trong string algorithms: reuse information giữa overlapping suffix/prefix states, tương tự failure links trong KMP/Aho–Corasick ở một abstraction khác.

## 18. Suffix Automaton

**Suffix Automaton (SAM / 접미 자동자)** là minimal DFA nhận tất cả substrings của một string theo một characterization tương ứng.

Dù tên là “suffix”, states của SAM represent equivalence classes của substrings có cùng end-position behavior. Number of states tối đa khoảng `2n-1` cho non-empty string construction chuẩn.

Mỗi state có `len` là maximum substring length trong class, suffix link và transitions.

## 19. Count distinct substrings bằng Suffix Automaton

Mỗi SAM state `v` (trừ initial state) đóng góp số substring lengths mới:

\[
len[v] - len[link[v]]
\]

Tổng qua states cho số distinct substrings.

Đây là một cách khác suffix-array/LCP formula, cho thấy cùng combinatorial object có thể được nén theo two very different representations.

## 20. Longest Common Substring với Suffix Automaton

Xây SAM cho string A. Sau đó scan B, duy trì current automaton state và current matched length. Khi transition không có, follow suffix links để giảm context.

Maximum matched length trong scan cho longest common substring length.

Cách này có thể đạt linear-time behavior theo alphabet transition assumptions và là một ứng dụng kinh điển của SAM.

## 21. Suffix Array vs Suffix Tree vs Suffix Automaton

Suffix Array compact, cache-friendly, dễ serialize và phù hợp static text + lexicographic/range queries. LCP bổ sung rất nhiều sức mạnh.

Suffix Tree hỗ trợ direct path navigation mạnh nhưng implementation/memory overhead lớn.

Suffix Automaton rất mạnh cho substring-language questions, occurrence equivalence và online extension, nhưng mental model automaton khác lexicographic order.

Không có structure “master” tốt nhất. Chọn theo query family.

## 22. Khi chỉ cần single-pattern search, đừng over-engineer

Nếu chỉ có một pattern và một text, KMP hoặc Z algorithm thường đơn giản hơn nhiều với `O(n+m)`.

Nếu có dictionary nhiều patterns và cần scan text, Aho–Corasick có thể phù hợp.

Nếu nhiều substring/order queries trên một static text, SA + LCP đáng giá.

Nếu cần prefix dictionary/autocomplete, Trie là model tự nhiên hơn.

Specialized suffix structures nên được dùng khi workload justify preprocessing/complexity.

## 23. Unicode và alphabet semantics

String algorithms thường trình bày trên alphabet symbols đơn giản. Trong Java, `char` là UTF-16 code unit; một Unicode code point có thể dùng surrogate pair. JavaScript string indexing cũng theo UTF-16 code units.

Nếu domain yêu cầu Unicode code points hoặc grapheme clusters, “character” trong algorithm phải được định nghĩa chính xác trước preprocessing.

Suffix order cũng phụ thuộc comparator/collation. Lexicographic order theo code units khác locale-aware collation.

## 24. Memory considerations

Suffix Array cần integer array size `n`, rank arrays và temporary buffers trong construction. Với text rất lớn, memory constants vẫn quan trọng.

Suffix Tree có many nodes/edges và pointer/object overhead, đặc biệt đắt trong Java/JavaScript nếu mỗi node là object/hash map.

Compressed arrays/primitive buffers thường có locality tốt hơn.

## 25. Testing suffix structures

Với small random strings, naive suffix list có thể làm oracle: tạo tất cả suffixes thật, sort strings rồi so starting indices với SA.

LCP có thể được so với naive pairwise prefix comparison cho adjacent SA entries.

Distinct substring count có thể được kiểm tra bằng brute-force HashSet trên n nhỏ.

Các test quan trọng gồm all-equal string như `aaaaa`, all-distinct, periodic strings như `abababab`, empty/single-character và Unicode semantics nếu supported.

## 26. Connection với Burrows–Wheeler Transform và FM-index

Suffix ordering liên quan sâu tới **Burrows–Wheeler Transform (BWT)**. BWT reorder text dựa trên sorted rotations/suffix-like order để tạo runs thuận lợi cho compression.

FM-index kết hợp BWT với rank/select-like structures để làm compressed full-text index, hỗ trợ pattern search trong space gần compressed text.

Đây là bước từ textbook suffix array sang search/indexing systems quy mô lớn và bioinformatics.

## Mental Model

> Suffix structures tránh index `O(n^2)` substrings trực tiếp bằng cách nhận ra rằng **mọi substring là prefix của một suffix**.

Suffix Array tổ chức suffixes theo lexicographic order; LCP đo mức shared prefix giữa neighbors; Suffix Tree compress prefix trie của suffixes; Suffix Automaton compress substrings theo future/end-position equivalence. Mỗi structure là một cách khác nhau để tái sử dụng overlap information trong string.

Xem thêm: [String Algorithms](./00_string_algorithms.md), [Sparse Table & RMQ](./05_sparse_table_and_static_range_queries.md), [Trie](../02_trees/04_tries.md), [Searching](../04_algorithmic_paradigms/00_searching.md).