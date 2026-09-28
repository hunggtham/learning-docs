# Mảng hậu tố, cây hậu tố và LCP

> **Mạch đọc:** Đọc **Mảng hậu tố, cây hậu tố và LCP** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Suffix là gì?** sang **2. Suffix Array**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Suffix Array, Suffix cây (tree / 트리) & Longest dùng chung (common / 공통) Prefix / 접미사 배열, 접미사 트리, LCP**

Nhiều bài toán chuỗi không chỉ hỏi prefix của toàn chuỗi mà hỏi về **mọi substring**: mẫu có xuất hiện không, chuỗi con lặp dài nhất là gì, có bao nhiêu chuỗi con phân biệt, hai suffix giống nhau bao lâu, hay longest dùng chung (common / 공통) substring giữa hai văn bản là gì.

Một chuỗi dài `n` có `Θ(n²)` substring nếu đếm theo vị trí. Lưu hoặc lập chỉ mục từng substring trực tiếp là quá đắt. Các cấu trúc hậu tố tận dụng một nhận xét then chốt:

> **Mọi substring đều là prefix của ít nhất một suffix.**

Thay vì quản lý `Θ(n²)` substring, ta tổ chức `n` suffix rồi khai thác thứ tự và các prefix dùng chung giữa chúng.

## 1. Suffix là gì?

Với `banana`:

```text
0  banana
1  anana
2  nana
3  ana
4  na
5  a
```

Có đúng `n` suffix, một suffix bắt đầu tại mỗi vị trí.

Substring `s[l..r]` chính là prefix của suffix bắt đầu tại `l`. Đây là cầu nối từ bài toán substring sang suffix indexing.

## 2. Suffix Array

**Mảng hậu tố (Suffix Array – SA / 접미사 배열)** lưu vị trí bắt đầu của các suffix sau khi sắp xếp theo thứ tự từ điển.

Với `banana`:

```text
5: a
3: ana
1: anana
0: banana
4: na
2: nana
```

nên:

```text
SA = [5, 3, 1, 0, 4, 2]
```

Điểm quan trọng: SA chỉ lưu chỉ số, không lưu lại toàn bộ các suffix. Vì vậy biểu diễn (representation / 표현) gọn hơn rất nhiều so với materialize `n` string con.

## 3. Vì sao substring tìm kiếm (search / 검색) trở thành tìm kiếm nhị phân (binary search / 이진 탐색)?

Trong thứ tự suffix đã sắp xếp, mọi suffix bắt đầu bằng cùng một mẫu (pattern / 패턴) tạo thành một đoạn liên tiếp.

Ví dụ mẫu (pattern / 패턴) `ana` khớp suffix `ana` và `anana`, nằm cạnh nhau trong SA.

Ta có thể dùng tìm kiếm nhị phân (binary search / 이진 탐색) để tìm:

```text
lower bound của pattern
upper bound của pattern
```

Nếu mỗi phép so sánh mẫu (pattern / 패턴)–suffix tốn `O(m)` với mẫu (pattern / 패턴) dài `m`, truy vấn cơ bản là:

\[
O(m\log n)
\]

sau khi SA đã được xây.

## 4. So sánh suffix không nên tạo substring mới

Một hiện thực (implementation / 구현) tệ có thể tạo `s.substring(i)` cho từng suffix rồi sort. Điều này dễ tạo tổng dữ liệu `Θ(n²)` và nhiều allocation.

Cách đúng về biểu diễn (representation / 표현) là giữ chỉ mục (index / 인덱스) vào string gốc và so sánh qua chỉ mục (index / 인덱스) hoặc rank.

Đây là một bài học hệ thống quan trọng: cùng một ý tưởng thuật toán nhưng materialization không cần thiết có thể phá cả bộ nhớ (memory / 메모리) lẫn hiệu năng (performance / 성능).

## 5. Prefix-Doubling

Một cách xây Suffix Array dễ học là **doubling**.

Ban đầu xếp suffix theo ký tự đầu tiên. Sau đó ở vòng `k`, mỗi suffix được đặc trưng bởi cặp rank của hai khối (block / 블록) dài `2^(k-1)`:

```text
(rank[i], rank[i + 2^(k-1)])
```

Mỗi vòng tăng độ dài prefix đã biết thứ tự lên gấp đôi:

```text
1, 2, 4, 8, 16, ...
```

Nếu sort cặp rank bằng comparison sort, độ phức tạp (complexity / 복잡도) thường `O(n log² n)`. Nếu rank là số nguyên và dùng radix/counting sort, có thể đạt `O(n log n)`.

## 6. Bất biến của Doubling

Sau vòng `k`:

> `rank[i]` biểu diễn đúng lớp thứ tự của prefix dài `2^k` bắt đầu tại `i`.

Khi xây vòng sau, cặp rank của hai nửa đủ quyết định thứ tự prefix dài gấp đôi.

Đây là một ví dụ đẹp của tư duy **nâng cấp tóm lược (summary refinement)**: thay vì so lại chuỗi dài, ta so hai summary đã được xác minh từ vòng trước.

## 7. Sentinel và ký tự kết thúc

Khi `i + len` vượt chuỗi, rank phần còn lại phải có quy ước rõ, thường dùng `-1` nhỏ hơn mọi rank hợp lệ.

Một cách khác là thêm terminal symbol `$` nhỏ hơn mọi ký tự hợp lệ và chỉ xuất hiện một lần.

Sentinel không phải chi tiết nhỏ. Nó ảnh hưởng trực tiếp lexicographic thứ tự (order / 순서) và tính duy nhất của suffix.

## 8. Rank Array

Nếu:

```text
SA[pos] = suffixStart
```

thì inverse array:

```text
rank[suffixStart] = pos
```

Rank giúp chuyển từ vị trí trong văn bản (text / 텍스트) sang vị trí trong thứ tự suffix.

Nó đặc biệt quan trọng trong Kasai và các bài cần hỏi quan hệ giữa suffix bắt đầu tại hai chỉ mục (index / 인덱스) gốc.

## 9. LCP Array

**LCP (Longest Common Prefix / 최장 공통 접두사)** thường được định nghĩa:

```text
LCP[i] = lcp(SA[i-1], SA[i])
LCP[0] = 0
```

LCP đo lượng prefix chung giữa hai suffix kề nhau trong lexicographic thứ tự (order / 순서).

Một insight rất quan trọng:

> Các suffix có prefix chung dài sẽ tụ lại thành một vùng liên tiếp trong SA.

Vì vậy LCP biến nhiều bài substring thành bài trên mảng.

## 10. Longest Repeated Substring

Nếu một substring xuất hiện ít nhất hai lần, tồn tại ít nhất hai suffix chia sẻ prefix đó.

Trong thứ tự đã sắp xếp, hai suffix có prefix chung dài nhất sẽ có một cặp kề nhau phản ánh độ dài đó.

Do đó:

```text
longest repeated substring length = max(LCP)
```

Nếu cần substring cụ thể, lấy vị trí tương ứng trong SA.

## 11. Kasai xây LCP trong O(n)

Naive tính LCP lại từ đầu cho từng cặp suffix kề nhau có thể `O(n²)` ở chuỗi lặp nhiều.

Kasai duy trì độ dài `h` của prefix chung đã biết. Khi chuyển từ suffix bắt đầu tại `i` sang suffix `i+1`, ta có thể giảm `h` tối đa một rồi tiếp tục so sánh.

Mỗi ký tự chỉ làm `h` tăng hữu hạn lần, và mỗi bước ngoài cùng làm `h` giảm tối đa một.

Tổng số thao tác so sánh thành công được khấu hao tuyến tính:

\[
O(n)
\]

Đây là một ví dụ rất hay của amortized phân tích (analysis / 분석) trong string algorithms.

## 12. LCP giữa hai suffix bất kỳ trở thành RMQ

Giả sử `rank[a] < rank[b]`. Khi đó:

\[
lcp(a,b)=\min LCP[rank[a]+1..rank[b]]
\]

Lý do: để hai suffix đầu-cuối cùng chia sẻ prefix dài `x`, mọi cặp suffix kề nhau giữa chúng trong lexicographic interval cũng phải chia sẻ ít nhất prefix dài `x`.

Vì vậy sau SA + LCP, bài toán LCP tùy ý trở thành **phạm vi (range / 범위) Minimum truy vấn (query / 쿼리)**.

Có thể dùng:

```text
Sparse Table -> static, O(1) query sau O(n log n) preprocessing
Segment Tree -> O(log n) query
```

Đây là ví dụ cross-domain rất đẹp giữa string indexing và range-query dữ liệu (data / 데이터) structures.

## 13. Số substring phân biệt

Tổng số substring tính theo vị trí:

\[
\frac{n(n+1)}2
\]

Xét suffix theo thứ tự SA. Suffix `SA[i]` có `n-SA[i]` prefix, nhưng `LCP[i]` prefix đầu đã xuất hiện trong suffix trước.

Do đó số substring phân biệt:

\[
\sum_i (n-SA[i]-LCP[i])
\]

hay tương đương:

\[
\frac{n(n+1)}2-\sum_i LCP[i]
\]

LCP có thể được hiểu như lượng “trùng lặp thông tin” giữa suffix hiện tại và phần đã thấy trước đó.

## 14. Longest dùng chung (common / 공통) Substring giữa hai chuỗi

Ghép:

```text
A + '#' + B + '$'
```

với các separator không xuất hiện trong đầu vào (input / 입력).

Xây SA + LCP, sau đó xét các cặp suffix kề nhau thuộc hai nguồn khác nhau. LCP lớn nhất của các cặp đó là độ dài longest dùng chung (common / 공통) substring.

Nếu có nhiều hơn hai chuỗi, bài toán cần một cửa sổ trên SA chứa đủ nguồn và lấy min-LCP trong cửa sổ, kết hợp two pointers/RMQ tùy formulation.

## 15. Tìm tất cả occurrence của mẫu (pattern / 패턴)

Tìm kiếm nhị phân (binary search / 이진 탐색) trên SA tìm đoạn suffix bắt đầu bằng mẫu (pattern / 패턴).

Kích thước đoạn chính là số occurrence theo vị trí bắt đầu.

Nếu cần xuất vị trí theo thứ tự văn bản (text / 텍스트), các vị trí trong SA phạm vi (range / 범위) phải được sort hoặc xử lý bằng cấu trúc phụ vì SA thứ tự (order / 순서) là lexicographic, không phải văn bản (text / 텍스트) thứ tự (order / 순서).

## 16. LCP-Accelerated tìm kiếm (search / 검색)

Tìm kiếm nhị phân (binary search / 이진 탐색) mẫu (pattern / 패턴) trên SA cơ bản có thể so lại nhiều prefix giống nhau ở nhiều bước.

Có thể giữ LCP của mẫu (pattern / 패턴) với biên trái/phải để bỏ qua phần prefix đã biết chung, giảm lượng ký tự phải so sánh trong một số thiết kế.

Ý tưởng tổng quát:

> Nếu đã biết hai chuỗi cùng prefix dài `k`, đừng so lại `k` ký tự đó ở lần tiếp theo.

Đây là một motif tái sử dụng thông tin rất phổ biến trong string algorithms.

## 17. Suffix cây (tree / 트리)

**Cây hậu tố (Suffix Tree / 접미사 트리)** là compressed trie của mọi suffix.

Suffix Trie naive có thể `Θ(n²)` nút (node / 노드)/ký tự. Suffix cây (tree / 트리) nén các chuỗi nút (node / 노드) một-con thành một cạnh có nhãn là một đoạn của văn bản (text / 텍스트) gốc.

Thay vì sao chép nhãn cạnh, lưu:

```text
(start, end)
```

trỏ vào string gốc.

Với terminal symbol và construction chuẩn, Suffix cây (tree / 트리) có số nút (node / 노드) tuyến tính theo `n`.

## 18. tìm kiếm (search / 검색) trong Suffix cây (tree / 트리)

Mẫu (pattern / 패턴) tìm kiếm (search / 검색) đi theo nhãn cạnh. Nếu biểu diễn (representation / 표현) cạnh dùng chỉ số vào văn bản (text / 텍스트), tổng số ký tự mẫu (pattern / 패턴) cần kiểm tra về lý tưởng là `O(m)`.

Sau khi tới locus của mẫu (pattern / 패턴), mọi leaf bên dưới tương ứng với occurrence.

Do đó độ phức tạp (complexity / 복잡도) tự nhiên là:

\[
O(m+k)
\]

với `k` là số occurrence phải xuất.

## 19. Ukkonen và vì sao Suffix cây (tree / 트리) khó cài

Xây Suffix cây (tree / 트리) naive bằng cách chèn từng suffix là `O(n²)`.

Ukkonen đạt tuyến tính (linear / 선형) thời gian (time / 시간) về lý thuyết bằng các khái niệm:

```text
implicit tree
active point
suffix links
end index dùng chung cho leaf edges
rule extensions
```

Hiện thực (implementation / 구현) rất tinh tế. Đây là ví dụ nơi thuật toán lý thuyết đẹp nhưng kỹ thuật (engineering / 엔지니어링) độ phức tạp (complexity / 복잡도) lớn.

Trong nhiều tải công việc (workload / 워크로드) văn bản (text / 텍스트) tĩnh, SA gọn hơn, dễ serialize hơn và cache-friendly hơn.

## 20. Suffix Link

Suffix link thường nối trạng thái biểu diễn `xα` tới trạng thái biểu diễn `α`.

Nó cho phép “bỏ ký tự đầu” của ngữ cảnh (context / 맥락) mà không quay về gốc và tìm lại từ đầu.

Motif này xuất hiện ở nhiều string structures:

```text
KMP failure link
Aho–Corasick failure link
Suffix Tree suffix link
Suffix Automaton suffix link
```

Đây đều là cách tái sử dụng trạng thái của các prefix/suffix chồng lấn.

## 21. Suffix Automaton

**Suffix Automaton (SAM / 접미 자동자)** là DFA tối thiểu đại diện cho tập substring của một chuỗi theo lớp tương đương end-position.

Mỗi trạng thái (state / 상태) thường giữ:

```text
len   -> độ dài substring dài nhất của lớp
link  -> suffix link
next  -> transition theo ký tự
```

Trạng thái (state / 상태) không đại diện một substring duy nhất mà đại diện một lớp substring có cùng tập vị trí kết thúc.

## 22. Ý nghĩa của Clone trong SAM

Khi thêm ký tự mới, đôi lúc một trạng thái (state / 상태) cũ phải được tách về mặt ngữ nghĩa để giữ đúng automaton tối thiểu. Ta tạo **clone trạng thái (state / 상태)** có chuyển tiếp (transition / 전이)/link giống trạng thái (state / 상태) cũ nhưng `len` ngắn hơn.

Clone không tương ứng với một prefix mới của văn bản (text / 텍스트). Nó là một trạng thái kỹ thuật cần thiết để chia lớp tương đương end-position.

Đây là phần quan trọng để hiểu SAM không phải “một trie tối ưu hóa”.

## 23. Số substring phân biệt bằng SAM

Mỗi trạng thái (state / 상태) `v` đóng góp số substring mới:

\[
len[v]-len[link[v]]
\]

Tổng trên các trạng thái (state / 상태) cho số substring phân biệt.

Trực giác: trạng thái (state / 상태) đại diện tất cả độ dài trong interval:

```text
(len[link[v]] + 1) ... len[v]
```

và các substring này thuộc cùng lớp end-position.

## 24. Occurrence Count trong SAM

Nếu mỗi prefix-end trạng thái (state / 상태) được khởi tạo count 1, rồi propagate count theo thứ tự `len` giảm dần qua suffix link, ta thu được số end positions của mỗi trạng thái (state / 상태).

Khi đó có thể trả lời số lần xuất hiện của substring sau khi đi chuyển tiếp (transition / 전이) tới trạng thái (state / 상태) tương ứng, với caveat về cách substring được ánh xạ vào trạng thái (state / 상태).

## 25. Longest dùng chung (common / 공통) Substring với SAM

Xây SAM cho `A`, rồi quét `B`. Duy trì trạng thái (state / 상태) hiện tại và độ dài match; khi chuyển tiếp (transition / 전이) thất bại, đi suffix link để tìm ngữ cảnh (context / 맥락) ngắn hơn có thể tiếp tục.

Độ dài match lớn nhất là longest dùng chung (common / 공통) substring.

Đây là counterpart automaton của cách làm SA + LCP.

## 26. SA, Suffix cây (tree / 트리) hay SAM?

| Nhu cầu | Cấu trúc thường phù hợp |
|---|---|
| văn bản (text / 텍스트) tĩnh, bộ nhớ (memory / 메모리) gọn, tìm kiếm nhị phân (binary search / 이진 탐색)/RMQ | Suffix Array + LCP |
| traversal theo substring prefix và truy vấn (query / 쿼리) giàu cấu trúc | Suffix cây (tree / 트리) |
| online xây một chuỗi, substring-state queries | Suffix Automaton |

Không có cấu trúc “mạnh nhất”. biểu diễn (representation / 표현) phù hợp phụ thuộc truy vấn (query / 쿼리) set, bộ nhớ (memory / 메모리) ngân sách (budget / 예산) và độ phức tạp hiện thực (implementation / 구현) chấp nhận được.

## 27. FM-Index và Burrows–Wheeler Transform

Ở quy mô văn bản (text / 텍스트) lớn, suffix thứ tự (ordering / 순서) còn dẫn tới **Burrows–Wheeler Transform (BWT)** và FM-index.

FM-index dùng BWT + rank/select-like structures để hỗ trợ **backward tìm kiếm (search / 검색)** cho mẫu (pattern / 패턴) trong bộ nhớ nén hơn nhiều so với lưu suffix cây (tree / 트리) đầy đủ.

Đây là nền tảng quan trọng của compressed full-text indexing và bioinformatics.

Mô hình tư duy mở rộng:

> Suffix thứ tự (order / 순서) không chỉ hỗ trợ tìm kiếm nhị phân (binary search / 이진 탐색); nó còn làm lộ cấu trúc lặp của văn bản (text / 텍스트) để vừa nén vừa tìm kiếm.

## 28. SA-IS và Linear-Time Construction

Có các thuật toán xây SA tuyến tính như SA-IS, dựa trên phân loại suffix và induced sorting.

Chúng quan trọng về lý thuyết và trong hiện thực (implementation / 구현) chuyên dụng, nhưng prefix-doubling thường dễ học, dễ gỡ lỗi (debug / 디버그) và đủ tốt cho nhiều tải công việc (workload / 워크로드).

Không nên dùng thuật toán construction phức tạp hơn chỉ vì asymptotic tốt hơn nếu `n` và hệ số thực tế không yêu cầu.

## 29. Alphabet và Unicode

String thuật toán (algorithm / 알고리즘) phải xác định đơn vị ký tự:

```text
byte
UTF-16 code unit
Unicode code point
grapheme cluster
```

Suffix cấu trúc (structure / 구조) chỉ đúng theo alphabet mà comparator sử dụng.

Trong Java, `char` là UTF-16 mã (code / 코드) đơn vị (unit / 단위). Trong JavaScript, chỉ mục (index / 인덱스) chuỗi cũng chủ yếu theo UTF-16 mã (code / 코드) đơn vị (unit / 단위). Nếu miền bài toán nói “ký tự người dùng nhìn thấy”, biểu diễn (representation / 표현) có thể phải khác.

## 30. Bộ nhớ

SA cơ bản cần vài mảng số nguyên kích thước `O(n)`. Doubling có thể cần SA, rank, tmp và buffers sort.

Suffix cây (tree / 트리)/SAM dùng nhiều nút (node / 노드)/trạng thái (state / 상태) và chuyển tiếp (transition / 전이). Nếu alphabet lớn, map/băm (hash / 해시) chuyển tiếp (transition / 전이) tăng overhead; nếu alphabet nhỏ cố định, array chuyển tiếp (transition / 전이) nhanh hơn nhưng tốn chỗ trống.

Cùng `O(n)` nhưng hệ số bộ nhớ có thể chênh rất lớn.

## 31. bộ nhớ đệm (cache / 캐시) Locality

SA và LCP là các mảng liên tiếp nên rất thân thiện với bộ nhớ đệm (cache / 캐시) và serialization.

Suffix cây (tree / 트리) nhiều nút (node / 노드)/con trỏ dễ tạo pointer chasing. SAM có thể nằm giữa hai thái cực tùy biểu diễn (representation / 표현) transitions.

Đây là lý do SA thường rất thực dụng dù cây hậu tố có truy vấn (query / 쿼리) độ phức tạp (complexity / 복잡도) lý thuyết đẹp.

## 32. Static vs động (dynamic / 동적) văn bản (text / 텍스트)

Suffix Array/cây (tree / 트리) cổ điển được tối ưu cho văn bản (text / 텍스트) tương đối tĩnh. Nếu văn bản (text / 텍스트) thay đổi giữa chuỗi, một edit có thể làm thay đổi rất nhiều suffix thứ tự (order / 순서).

Động (dynamic / 동적) full-text indexing cần cấu trúc phức tạp hơn hoặc chiến lược rebuild/batching.

Nếu tải công việc (workload / 워크로드) là append-only stream, SAM có lợi thế vì construction online tự nhiên hơn.

## 33. Output-Sensitive Bound

Nếu mẫu (pattern / 패턴) xuất hiện `k` lần và API yêu cầu liệt kê mọi vị trí, độ phức tạp (complexity / 복잡도) không thể nhỏ hơn `Ω(k)`.

Một cấu trúc cho tìm kiếm (search / 검색) `O(m)` vẫn cần thêm `O(k)` để đầu ra (output / 출력) occurrences.

Đừng nhầm chi phí tìm vùng kết quả với chi phí materialize kết quả.

## 34. Kiểm thử Suffix Array

Với chuỗi nhỏ, có thể tạo oracle:

```text
suffixes = [(s[i:], i) for i]
sort trực tiếp
so index với SA
```

Các bất biến (invariant / 불변식):

```text
SA là permutation của 0..n-1
suffixes theo SA tăng lexicographically
rank[SA[i]] == i
LCP[i] đúng với cặp kề
```

## 35. Kiểm thử Kasai

Với chuỗi nhỏ, tính LCP naive cho từng cặp suffix kề rồi so với Kasai.

Trường hợp (case / 사례) quan trọng:

```text
all same chars: aaaaa
all distinct
periodic string: ababab...
empty/single char
Unicode theo đúng unit đã định nghĩa
```

Chuỗi `aaaaa` đặc biệt tốt để bắt bug vì LCP rất dài và overlapping mạnh.

## 36. Kiểm thử SAM

Có thể generate mọi substring của chuỗi nhỏ bằng brute force và so:

```text
SAM accepts đúng mọi substring
SAM rejects các string không phải substring
số distinct substrings khớp brute force set
occurrence count khớp oracle
```

Clone-related bug thường lộ rõ qua random differential testing.

## 37. Những hiểu lầm phổ biến

“Suffix Array lưu mọi suffix string” — sai; nó chỉ cần lưu chỉ mục (index / 인덱스).

“Có SA thì mọi substring truy vấn (query / 쿼리) là O(log n)” — còn phụ thuộc chi phí so mẫu (pattern / 패턴), LCP acceleration và đầu ra (output / 출력) kích thước (size / 크기).

“Suffix cây (tree / 트리) luôn tốt hơn SA vì truy vấn (query / 쿼리) O(m)” — bỏ qua bộ nhớ (memory / 메모리), bộ nhớ đệm (cache / 캐시) locality và hiện thực (implementation / 구현) độ phức tạp (complexity / 복잡도).

“SAM trạng thái (state / 상태) tương ứng đúng một substring” — sai; trạng thái (state / 상태) là lớp tương đương của nhiều substring.

“Coordinate của string luôn là ký tự Unicode thực” — sai nếu thời gian chạy (runtime / 런타임) chỉ mục (index / 인덱스) theo mã (code / 코드) đơn vị (unit / 단위)/byte.

## Mô hình tư duy

> Các cấu trúc hậu tố biến không gian `Θ(n²)` substring thành một biểu diễn (representation / 표현) tuyến tính bằng cách tổ chức `n` suffix và chia sẻ thông tin prefix giữa chúng.

Suffix Array khai thác **thứ tự**. LCP khai thác **mức giống nhau giữa hàng xóm trong thứ tự**. Suffix cây (tree / 트리) khai thác **nén đường đi prefix**. Suffix Automaton khai thác **lớp tương đương theo vị trí kết thúc**.

Khi gặp bài substring lớn, hãy hỏi: **văn bản (text / 텍스트) tĩnh hay append-only, cần tìm kiếm (search / 검색) hay counting/rank/RMQ, cần đầu ra (output / 출력) mọi occurrence không, bộ nhớ (memory / 메모리) có quan trọng không, alphabet là gì, và có cần construction đủ đơn giản để kiểm chứng không?**

Xem thêm: [String Algorithms](./00_string_algorithms.md), [Sparse Table](./05_sparse_table_and_static_range_queries.md), [Range Queries](./01_range_queries_fenwick_segment_tree.md), [Amortized & Probabilistic Thinking](./03_amortized_randomized_and_probabilistic_thinking.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 string algorithms](./00_string_algorithms.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
