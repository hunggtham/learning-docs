# String algorithms và văn bản (text / 텍스트) indexing

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **String algorithms và văn bản (text / 텍스트) indexing**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Biểu diễn (representation / 표현) đến trước thuật toán (algorithm / 알고리즘)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Naive substring tìm kiếm (search / 검색) và thông tin bị lãng phí** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

String (chuỗi / 문자열) trông giống một array ký tự, nhưng nhiều bài toán trên văn bản (text / 텍스트) không thể giải thích tốt chỉ bằng array operations. Ta thường cần tìm một mẫu (pattern / 패턴) trong văn bản lớn, so sánh prefixes, phát hiện lặp, autocomplete, xử lý DNA chuỗi (sequence / 시퀀스), tokenize mã nguồn (source code / 소스 코드) hoặc tìm hàng triệu documents. Điểm cốt lõi là **cấu trúc thứ tự trong chuỗi tạo ra thông tin có thể tái sử dụng**, nếu ta không bắt đầu so sánh lại từ đầu mỗi lần.

## Biểu diễn (representation / 표현) đến trước thuật toán (algorithm / 알고리즘)

Trước khi nói về tìm kiếm chuỗi, cần phân biệt character, mã (code / 코드) điểm (point / 지점), byte và grapheme cluster. Với ASCII, một ký tự thường tương ứng một byte nên ta dễ quên rằng đây chỉ là trường hợp đơn giản. UTF-8 dùng số byte biến đổi; một ký tự người dùng nhìn thấy có thể gồm nhiều Unicode mã (code / 코드) points. Vì vậy `length`, slicing và indexing có ngữ nghĩa (semantics / 의미론) khác nhau tùy thời gian chạy (runtime / 런타임).

Xem nền tảng biểu diễn (representation / 표현) tại [Information, bit và encoding](../00_computation_information/01_information_bits_and_encoding.md).

Nếu thuật toán (algorithm / 알고리즘) nói “O(n) theo số ký tự”, ta phải hỏi `n` là bytes, mã (code / 코드) points hay grapheme clusters. Đây không phải chi tiết ngôn ngữ: nó thay đổi chi phí (cost / 비용) mô hình (model / 모델) và tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Trong **String algorithms và văn bản (text / 텍스트) indexing**, **Naive substring tìm kiếm (search / 검색) và thông tin bị lãng phí** tiếp nhận điểm tựa từ **Biểu diễn (representation / 표현) đến trước thuật toán (algorithm / 알고리즘)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rabin–Karp: so sánh fingerprint trước, nội dung sau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Naive substring tìm kiếm (search / 검색) và thông tin bị lãng phí

Giả sử cần tìm mẫu (pattern / 패턴) `ABABAC` trong một văn bản (text / 텍스트) dài. Cách trực tiếp đặt mẫu (pattern / 패턴) tại từng vị trí rồi so sánh cho tới khi mismatch. Worst trường hợp (case / 사례) có thể gần `O(nm)` với `n` là độ dài văn bản (text / 텍스트) và `m` là mẫu (pattern / 패턴).

Điều lãng phí nằm ở chỗ một mismatch sau nhiều ký tự match đã cho ta thông tin về cấu trúc prefix của mẫu (pattern / 패턴), nhưng naive thuật toán (algorithm / 알고리즘) bỏ thông tin đó.

### KMP: prefix cũng có thể là suffix

Knuth–Morris–Pratt (KMP / KMP 문자열 검색) preprocess mẫu (pattern / 패턴) thành bảng prefix hàm (function / 함수) hoặc thất bại (failure / 실패) hàm (function / 함수). Bảng này trả lời: khi mismatch tại vị trí hiện tại, prefix dài nhất nào của mẫu (pattern / 패턴) cũng là suffix của phần vừa match?

Nhờ đó pointer của văn bản (text / 텍스트) không cần quay lại. Preprocessing tốn `O(m)`, scanning tốn `O(n)`, tổng `O(n+m)`.

Mô hình tư duy (mental model / 사고 모델) không phải “học bảng KMP”, mà là:

> Khi computation thất bại sau khi đã học được một phần cấu trúc, đừng vứt thông tin đó đi; dùng nó để quyết định trạng thái tiếp theo.

Ý tưởng này giống automaton, parser trạng thái (state / 상태) và incremental computation.

> **Chuyển mạch:** Ở chặng này của **String algorithms và văn bản (text / 텍스트) indexing**, **Naive substring tìm kiếm (search / 검색) và thông tin bị lãng phí** đã nêu tiêu chí phân biệt, còn **Rabin–Karp: so sánh fingerprint trước, nội dung sau** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Trie: chỉ mục (index / 인덱스) theo prefix thay vì toàn key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rabin–Karp: so sánh fingerprint trước, nội dung sau

Rabin–Karp dùng rolling băm (hash / 해시) cho windows có cùng độ dài mẫu (pattern / 패턴). Thay vì so sánh toàn bộ mỗi cửa sổ (window / 윈도우), ta cập nhật băm (hash / 해시) khi bỏ ký tự đầu và thêm ký tự cuối.

Nếu băm (hash / 해시) khác, chắc chắn strings khác. Nếu băm (hash / 해시) giống, vẫn phải verify vì collision có thể xảy ra. Vì vậy hashing biến một phép so sánh đắt thành filter rẻ, nhưng không biến băm (hash / 해시) thành bằng chứng equality tuyệt đối.

Mẫu (pattern / 패턴) này xuất hiện rộng hơn trong checksum, content-addressable lưu trữ (storage / 저장소), deduplication và cơ sở dữ liệu (database / 데이터베이스) băm (hash / 해시) phép nối (join / 조인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String algorithms và văn bản (text / 텍스트) indexing**, **Rabin–Karp: so sánh fingerprint trước, nội dung sau** đã nêu tiêu chí phân biệt, còn **Trie: chỉ mục (index / 인덱스) theo prefix thay vì toàn key** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Suffix structures: chỉ mục (index / 인덱스) mọi suffix để hỏi về substring** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trie: chỉ mục (index / 인덱스) theo prefix thay vì toàn key

Trie (prefix tree / 트라이) lưu mỗi edge như một ký hiệu của key. Các keys có cùng prefix chia sẻ đường đi. Điều này phù hợp autocomplete, dictionary lookup, routing prefix và lexical phân tích (analysis / 분석).

Nếu alphabet và key length phù hợp, lookup phụ thuộc chủ yếu vào độ dài key hơn là số keys. Đổi lại trie có thể tốn bộ nhớ (memory / 메모리) lớn do nodes/edges overhead. Compressed trie hoặc radix cây (tree / 트리) nén chuỗi các nút (node / 노드) một con thành edge dài hơn.

Routing bảng (table / 테이블) IP thường dùng longest-prefix matching, một bài toán có mô hình tư duy (mental model / 사고 모델) gần trie/radix cây (tree / 트리).

> **Chuyển mạch:** Trong **String algorithms và văn bản (text / 텍스트) indexing**, **Suffix structures: chỉ mục (index / 인덱스) mọi suffix để hỏi về substring** tiếp nhận điểm tựa từ **Trie: chỉ mục (index / 인덱스) theo prefix thay vì toàn key** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prefix hàm (function / 함수), Z-function và mẫu (pattern / 패턴) preprocessing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suffix structures: chỉ mục (index / 인덱스) mọi suffix để hỏi về substring

Nếu cần nhiều substring queries trên cùng một văn bản (text / 텍스트), preprocessing mạnh hơn có thể đáng giá. Suffix array (접미 배열) sắp xếp mọi suffix theo lexicographic thứ tự (order / 순서). Khi đó tìm mẫu (pattern / 패턴) có thể dùng tìm kiếm nhị phân (binary search / 이진 탐색) trên ordered suffixes.

Suffix cây (tree / 트리) cung cấp truy vấn (query / 쿼리) rất nhanh nhưng cấu trúc và constant factor phức tạp hơn. Suffix automaton nén tập substrings theo equivalence classes của suffix states và rất hữu ích cho các bài toán như longest dùng chung (common / 공통) substring.

Điểm quan trọng không phải ghi nhớ ba cấu trúc này, mà hiểu sự đánh đổi (trade-off / 트레이드오프) **preprocessing thời gian (time / 시간) + chỉ mục (index / 인덱스) bộ nhớ (memory / 메모리) ↔ truy vấn (query / 쿼리) speed**. Đây cũng là sự đánh đổi (trade-off / 트레이드오프) cốt lõi của cơ sở dữ liệu (database / 데이터베이스) indexes.

> **Chuyển mạch:** Ở chặng này của **String algorithms và văn bản (text / 텍스트) indexing**, **Suffix structures: chỉ mục (index / 인덱스) mọi suffix để hỏi về substring** xác định đầu vào; **Prefix hàm (function / 함수), Z-function và mẫu (pattern / 패턴) preprocessing** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Edit distance: khi “giống nhau” không còn là equality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prefix hàm (function / 함수), Z-function và mẫu (pattern / 패턴) preprocessing

Nhiều string algorithms xây một mảng phụ biểu diễn self-similarity của chuỗi. Prefix hàm (function / 함수) hỏi prefix dài nhất kết thúc tại từng vị trí; Z-function hỏi prefix dài nhất bắt đầu tại từng vị trí.

Hai cách nhìn khác nhau nhưng cùng khai thác repeated cấu trúc (structure / 구조). Đây là ví dụ tốt cho việc một dữ liệu (data / 데이터) biểu diễn (representation / 표현) phù hợp có thể làm thuật toán (algorithm / 알고리즘) trở nên rõ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String algorithms và văn bản (text / 텍스트) indexing**, **Prefix hàm (function / 함수), Z-function và mẫu (pattern / 패턴) preprocessing** xác định đầu vào; **Edit distance: khi “giống nhau” không còn là equality** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Văn bản (text / 텍스트) tìm kiếm (search / 검색) trong hệ thống thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Edit distance: khi “giống nhau” không còn là equality

Levenshtein edit distance đo số insert/delete/replace tối thiểu để biến string A thành B. Đây là động (dynamic / 동적) programming với trạng thái (state / 상태) thường là `dp[i][j]`: chi phí (cost / 비용) tối thiểu để biến prefix đầu tiên độ dài `i` thành prefix thứ hai độ dài `j`.

Nó được dùng trong spell checking, fuzzy matching, chuỗi (sequence / 시퀀스) alignment và bản ghi (record / 레코드) linkage. Nhưng chỉ số (metric / 지표) này không hiểu ngữ nghĩa (semantics / 의미론); hai từ nghĩa gần nhau vẫn có thể có edit distance lớn. Vì vậy thuật toán (algorithm / 알고리즘) đo một loại similarity cụ thể, không phải “độ giống” tuyệt đối.

> **Chuyển mạch:** Trong **String algorithms và văn bản (text / 텍스트) indexing**, **Văn bản (text / 텍스트) tìm kiếm (search / 검색) trong hệ thống thật** tiếp nhận điểm tựa từ **Edit distance: khi “giống nhau” không còn là equality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Văn bản (text / 텍스트) tìm kiếm (search / 검색) trong hệ thống thật

Tìm kiếm (search / 검색) engine không scan mọi document bằng KMP. Nó thường xây inverted chỉ mục (index / 인덱스): term → danh sách documents/positions chứa term. Đây là inversion của ánh xạ (mapping / 매핑) document → terms.

Khi truy vấn (query / 쿼리) đến, hệ thống (system / 시스템) intersect/union posting lists, tính ranking và có thể dùng positional thông tin (information / 정보) cho phrase queries. Tư duy này nối string processing với cơ sở dữ liệu (database / 데이터베이스) indexing và thông tin (information / 정보) retrieval.

> **Chuyển mạch:** Ở chặng này của **String algorithms và văn bản (text / 텍스트) indexing**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Văn bản (text / 텍스트) tìm kiếm (search / 검색) trong hệ thống thật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“String chỉ là array char.”** Chỉ đúng trong một số biểu diễn (representation / 표현) đơn giản. Unicode khiến character-level ngữ nghĩa (semantics / 의미론) phức tạp hơn byte-level lưu trữ (storage / 저장소).

**“băm (hash / 해시) giống nhau nghĩa là string giống nhau.”** băm (hash / 해시) collision luôn là khả năng trong miền hữu hạn, trừ khi ngữ cảnh (context / 맥락) có cơ chế verify hoặc dùng construction đặc biệt.

**“Suffix cây (tree / 트리) luôn tốt hơn suffix array vì truy vấn (query / 쿼리) nhanh.”** bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃), hiện thực (implementation / 구현) độ phức tạp (complexity / 복잡도) và bộ nhớ đệm (cache / 캐시) locality có thể khiến suffix array thực tế phù hợp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String algorithms và văn bản (text / 텍스트) indexing**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

String algorithms nối trực tiếp với [hashing](./04_hashing_and_hash_tables.md), [dynamic programming](./08_algorithmic_strategies.md), [compiler front-end](../04_programming_languages/07_parsing_ast_and_language_frontends.md), [database indexing](../05_data_databases/03_indexes_and_query_execution.md) và [information representation](../00_computation_information/01_information_bits_and_encoding.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
