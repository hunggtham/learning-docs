# String algorithms và text indexing

String (chuỗi / 문자열) trông giống một array ký tự, nhưng nhiều bài toán trên text không thể giải thích tốt chỉ bằng array operations. Ta thường cần tìm một pattern trong văn bản lớn, so sánh prefixes, phát hiện lặp, autocomplete, xử lý DNA sequence, tokenize source code hoặc tìm hàng triệu documents. Điểm cốt lõi là **cấu trúc thứ tự trong chuỗi tạo ra thông tin có thể tái sử dụng**, nếu ta không bắt đầu so sánh lại từ đầu mỗi lần.

## Representation đến trước algorithm

Trước khi nói về tìm kiếm chuỗi, cần phân biệt character, code point, byte và grapheme cluster. Với ASCII, một ký tự thường tương ứng một byte nên ta dễ quên rằng đây chỉ là trường hợp đơn giản. UTF-8 dùng số byte biến đổi; một ký tự người dùng nhìn thấy có thể gồm nhiều Unicode code points. Vì vậy `length`, slicing và indexing có semantics khác nhau tùy runtime.

Xem nền tảng representation tại [Information, bit và encoding](../00_computation_information/01_information_bits_and_encoding.md).

Nếu algorithm nói “O(n) theo số ký tự”, ta phải hỏi `n` là bytes, code points hay grapheme clusters. Đây không phải chi tiết ngôn ngữ: nó thay đổi cost model và correctness.

## Naive substring search và thông tin bị lãng phí

Giả sử cần tìm pattern `ABABAC` trong một text dài. Cách trực tiếp đặt pattern tại từng vị trí rồi so sánh cho tới khi mismatch. Worst case có thể gần `O(nm)` với `n` là độ dài text và `m` là pattern.

Điều lãng phí nằm ở chỗ một mismatch sau nhiều ký tự match đã cho ta thông tin về cấu trúc prefix của pattern, nhưng naive algorithm bỏ thông tin đó.

### KMP: prefix cũng có thể là suffix

Knuth–Morris–Pratt (KMP / KMP 문자열 검색) preprocess pattern thành bảng prefix function hoặc failure function. Bảng này trả lời: khi mismatch tại vị trí hiện tại, prefix dài nhất nào của pattern cũng là suffix của phần vừa match?

Nhờ đó pointer của text không cần quay lại. Preprocessing tốn `O(m)`, scanning tốn `O(n)`, tổng `O(n+m)`.

Mental model không phải “học bảng KMP”, mà là:

> Khi computation thất bại sau khi đã học được một phần cấu trúc, đừng vứt thông tin đó đi; dùng nó để quyết định trạng thái tiếp theo.

Ý tưởng này giống automaton, parser state và incremental computation.

## Rabin–Karp: so sánh fingerprint trước, nội dung sau

Rabin–Karp dùng rolling hash (해시 이동 / rolling hash) cho windows có cùng độ dài pattern. Thay vì so sánh toàn bộ mỗi window, ta cập nhật hash khi bỏ ký tự đầu và thêm ký tự cuối.

Nếu hash khác, chắc chắn strings khác. Nếu hash giống, vẫn phải verify vì collision có thể xảy ra. Vì vậy hashing biến một phép so sánh đắt thành filter rẻ, nhưng không biến hash thành bằng chứng equality tuyệt đối.

Pattern này xuất hiện rộng hơn trong checksum, content-addressable storage, deduplication và database hash join.

## Trie: index theo prefix thay vì toàn key

Trie (prefix tree / 트라이) lưu mỗi edge như một ký hiệu của key. Các keys có cùng prefix chia sẻ đường đi. Điều này phù hợp autocomplete, dictionary lookup, routing prefix và lexical analysis.

Nếu alphabet và key length phù hợp, lookup phụ thuộc chủ yếu vào độ dài key hơn là số keys. Đổi lại trie có thể tốn memory lớn do nodes/edges overhead. Compressed trie hoặc radix tree nén chuỗi các node một con thành edge dài hơn.

Routing table IP thường dùng longest-prefix matching, một bài toán có mental model gần trie/radix tree.

## Suffix structures: index mọi suffix để hỏi về substring

Nếu cần nhiều substring queries trên cùng một text, preprocessing mạnh hơn có thể đáng giá. Suffix array (접미 배열) sắp xếp mọi suffix theo lexicographic order. Khi đó tìm pattern có thể dùng binary search trên ordered suffixes.

Suffix tree cung cấp query rất nhanh nhưng cấu trúc và constant factor phức tạp hơn. Suffix automaton nén tập substrings theo equivalence classes của suffix states và rất hữu ích cho các bài toán như longest common substring.

Điểm quan trọng không phải ghi nhớ ba cấu trúc này, mà hiểu trade-off **preprocessing time + index memory ↔ query speed**. Đây cũng là trade-off cốt lõi của database indexes.

## Prefix function, Z-function và pattern preprocessing

Nhiều string algorithms xây một mảng phụ biểu diễn self-similarity của chuỗi. Prefix function hỏi prefix dài nhất kết thúc tại từng vị trí; Z-function hỏi prefix dài nhất bắt đầu tại từng vị trí.

Hai cách nhìn khác nhau nhưng cùng khai thác repeated structure. Đây là ví dụ tốt cho việc một data representation phù hợp có thể làm algorithm trở nên rõ hơn.

## Edit distance: khi “giống nhau” không còn là equality

Levenshtein edit distance đo số insert/delete/replace tối thiểu để biến string A thành B. Đây là dynamic programming với state thường là `dp[i][j]`: cost tối thiểu để biến prefix đầu tiên độ dài `i` thành prefix thứ hai độ dài `j`.

Nó được dùng trong spell checking, fuzzy matching, sequence alignment và record linkage. Nhưng metric này không hiểu semantics; hai từ nghĩa gần nhau vẫn có thể có edit distance lớn. Vì vậy algorithm đo một loại similarity cụ thể, không phải “độ giống” tuyệt đối.

## Text search trong hệ thống thật

Search engine không scan mọi document bằng KMP. Nó thường xây inverted index (역색인): term → danh sách documents/positions chứa term. Đây là inversion của mapping document → terms.

Khi query đến, system intersect/union posting lists, tính ranking và có thể dùng positional information cho phrase queries. Tư duy này nối string processing với database indexing và information retrieval.

## Common Misconceptions

**“String chỉ là array char.”** Chỉ đúng trong một số representation đơn giản. Unicode khiến character-level semantics phức tạp hơn byte-level storage.

**“Hash giống nhau nghĩa là string giống nhau.”** Hash collision luôn là khả năng trong miền hữu hạn, trừ khi context có cơ chế verify hoặc dùng construction đặc biệt.

**“Suffix tree luôn tốt hơn suffix array vì query nhanh.”** Memory layout, implementation complexity và cache locality có thể khiến suffix array thực tế phù hợp hơn.

## Kết nối

String algorithms nối trực tiếp với [hashing](./04_hashing_and_hash_tables.md), [dynamic programming](./08_algorithmic_strategies.md), [compiler front-end](../04_programming_languages/07_parsing_ast_and_language_frontends.md), [database indexing](../05_data_databases/03_indexes_and_query_execution.md) và [information representation](../00_computation_information/01_information_bits_and_encoding.md).