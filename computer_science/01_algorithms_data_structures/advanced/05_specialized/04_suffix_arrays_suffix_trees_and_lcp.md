# Mảng hậu tố, cây hậu tố và LCP

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Mảng hậu tố, cây hậu tố và LCP**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Suffix là gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Suffix Array** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối suffix arrays, suffix trees và LCP, để text indexing được tối ưu theo cấu trúc hậu tố và truy vấn.

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

Suffix của một text là một điểm bắt đầu kèm toàn bộ phần đuôi; so sánh chúng chính là so sánh các suffix lexicographic. Sắp các suffix theo thứ tự đó tạo ra suffix array, một index gọn hơn cây nhưng vẫn giữ thứ tự cần tìm.

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

Suffix array đặt mọi suffix trên một trục đã sắp xếp. Vì các suffix bắt đầu bằng cùng pattern tạo thành một đoạn liên tiếp, truy vấn substring có thể dùng binary search thay vì quét toàn văn bản.

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

Binary search chỉ hữu ích nếu phép so sánh suffix không tạo substring mới ở mỗi bước. So sánh trực tiếp theo offset giữ được memory và time bound, đồng thời dẫn tới prefix-doubling khi xây index.

## 4. So sánh suffix không nên tạo substring mới

Một hiện thực (implementation / 구현) tệ có thể tạo `s.substring(i)` cho từng suffix rồi sort. Điều này dễ tạo tổng dữ liệu `Θ(n²)` và nhiều allocation.

Cách đúng về biểu diễn (representation / 표현) là giữ chỉ mục (index / 인덱스) vào string gốc và so sánh qua chỉ mục (index / 인덱스) hoặc rank.

Đây là một bài học hệ thống quan trọng: cùng một ý tưởng thuật toán nhưng materialization không cần thiết có thể phá cả bộ nhớ (memory / 메모리) lẫn hiệu năng (performance / 성능).

Prefix-doubling xếp các prefix độ dài 1, 2, 4, ... bằng rank của hai nửa. Muốn tin kết quả, cần giữ invariant rằng rank hiện tại phản ánh đúng thứ tự của mọi prefix đã được xét.

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

Invariant của doubling phụ thuộc việc cặp rank và thứ tự tie-break được định nghĩa nhất quán. Sentinel giúp mọi suffix có điểm kết thúc rõ ràng và tránh so sánh vượt biên khi các prefix có độ dài khác nhau.

## 6. Bất biến của Doubling

Sau vòng `k`:

> `rank[i]` biểu diễn đúng lớp thứ tự của prefix dài `2^k` bắt đầu tại `i`.

Khi xây vòng sau, cặp rank của hai nửa đủ quyết định thứ tự prefix dài gấp đôi.

Đây là một ví dụ đẹp của tư duy **nâng cấp tóm lược (summary refinement)**: thay vì so lại chuỗi dài, ta so hai summary đã được xác minh từ vòng trước.

Sentinel nhỏ hơn mọi ký tự làm suffix kết thúc có thứ tự duy nhất và khiến các phép so sánh dễ chứng minh hơn. Khi suffix đã được xếp, rank array cung cấp ánh xạ ngược từ vị trí text sang vị trí trong suffix array.

## 7. Sentinel và ký tự kết thúc

Khi `i + len` vượt chuỗi, rank phần còn lại phải có quy ước rõ, thường dùng `-1` nhỏ hơn mọi rank hợp lệ.

Một cách khác là thêm terminal symbol `$` nhỏ hơn mọi ký tự hợp lệ và chỉ xuất hiện một lần.

Sentinel không phải chi tiết nhỏ. Nó ảnh hưởng trực tiếp lexicographic thứ tự (order / 순서) và tính duy nhất của suffix.

Rank array là inverse permutation của suffix array, nên biết một suffix bắt đầu ở đâu là biết vị trí của nó trong thứ tự lexicographic. Từ rank kề nhau, LCP array đo phần prefix chung giữa các suffix lân cận.

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

LCP array ghi độ dài prefix chung của từng cặp suffix kề nhau, không phải toàn bộ substring. Các giá trị này biến câu hỏi về lặp lại thành bài toán cực đại trên LCP.

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

Longest repeated substring chính là prefix chung dài nhất của hai suffix khác nhau, nên có thể đọc từ max của LCP. Để xây LCP hiệu quả thay vì so từng cặp từ đầu, ta dùng Kasai với reuse của các match trước.

## 10. Longest Repeated Substring

Nếu một substring xuất hiện ít nhất hai lần, tồn tại ít nhất hai suffix chia sẻ prefix đó.

Trong thứ tự đã sắp xếp, hai suffix có prefix chung dài nhất sẽ có một cặp kề nhau phản ánh độ dài đó.

Do đó:

```text
longest repeated substring length = max(LCP)
```

Nếu cần substring cụ thể, lấy vị trí tương ứng trong SA.

Kasai tận dụng việc suffix kế tiếp thường mất nhiều nhất một ký tự LCP khi dịch vị trí, nhờ đó tổng số bước tăng giảm là tuyến tính. Khi LCP đã có, truy vấn giữa hai suffix bất kỳ trở thành range minimum query.

## 11. Kasai xây LCP trong O(n)

Naive tính LCP lại từ đầu cho từng cặp suffix kề nhau có thể `O(n²)` ở chuỗi lặp nhiều.

Kasai duy trì độ dài `h` của prefix chung đã biết. Khi chuyển từ suffix bắt đầu tại `i` sang suffix `i+1`, ta có thể giảm `h` tối đa một rồi tiếp tục so sánh.

Mỗi ký tự chỉ làm `h` tăng hữu hạn lần, và mỗi bước ngoài cùng làm `h` giảm tối đa một.

Tổng số thao tác so sánh thành công được khấu hao tuyến tính:

\[
O(n)
\]

Đây là một ví dụ rất hay của amortized phân tích (analysis / 분석) trong string algorithms.

Kasai tạo LCP ở không gian suffix array; RMQ trên đoạn LCP giữa hai rank trả về LCP của bất kỳ cặp suffix. Từ primitive này, ta đếm số substring phân biệt bằng cách trừ phần prefix đã xuất hiện.

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

Số substring phân biệt bằng tổng độ dài suffix trừ tổng LCP kề nhau, vì mỗi LCP loại phần prefix trùng. Cùng cách nhìn prefix chung còn mở rộng tự nhiên sang longest common substring của hai chuỗi.

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

Đếm substring phân biệt dùng suffix array để đếm, còn hai chuỗi cần thêm separator và phân biệt nguồn của suffix. LCP lớn nhất giữa suffix thuộc hai chuỗi cho longest common substring.

## 14. Longest dùng chung (common / 공통) Substring giữa hai chuỗi

Ghép:

```text
A + '#' + B + '$'
```

với các separator không xuất hiện trong đầu vào (input / 입력).

Xây SA + LCP, sau đó xét các cặp suffix kề nhau thuộc hai nguồn khác nhau. LCP lớn nhất của các cặp đó là độ dài longest dùng chung (common / 공통) substring.

Nếu có nhiều hơn hai chuỗi, bài toán cần một cửa sổ trên SA chứa đủ nguồn và lấy min-LCP trong cửa sổ, kết hợp two pointers/RMQ tùy formulation.

Longest common substring xác định độ dài chung, nhưng tìm mọi occurrence của pattern cần tìm đoạn suffix có cùng prefix với pattern. Binary search trên suffix array cho khoảng ứng viên, sau đó kiểm tra boundary.

## 15. Tìm tất cả occurrence của mẫu (pattern / 패턴)

Tìm kiếm nhị phân (binary search / 이진 탐색) trên SA tìm đoạn suffix bắt đầu bằng mẫu (pattern / 패턴).

Kích thước đoạn chính là số occurrence theo vị trí bắt đầu.

Nếu cần xuất vị trí theo thứ tự văn bản (text / 텍스트), các vị trí trong SA phạm vi (range / 범위) phải được sort hoặc xử lý bằng cấu trúc phụ vì SA thứ tự (order / 순서) là lexicographic, không phải văn bản (text / 텍스트) thứ tự (order / 순서).

Khi nhiều suffix có prefix dài giống nhau, binary search lặp lại cùng phép so sánh. LCP-accelerated search lưu LCP ở hai biên để bỏ qua phần đã biết và giảm số ký tự phải kiểm tra.

## 16. LCP-Accelerated tìm kiếm (search / 검색)

Tìm kiếm nhị phân (binary search / 이진 탐색) mẫu (pattern / 패턴) trên SA cơ bản có thể so lại nhiều prefix giống nhau ở nhiều bước.

Có thể giữ LCP của mẫu (pattern / 패턴) với biên trái/phải để bỏ qua phần prefix đã biết chung, giảm lượng ký tự phải so sánh trong một số thiết kế.

Ý tưởng tổng quát:

> Nếu đã biết hai chuỗi cùng prefix dài `k`, đừng so lại `k` ký tự đó ở lần tiếp theo.

Đây là một motif tái sử dụng thông tin rất phổ biến trong string algorithms.

LCP giúp suffix array tìm nhanh nhưng vẫn lưu mảng chỉ số; suffix tree nén các cạnh có prefix chung thành cấu trúc explicit. Đổi lại, tree tăng khả năng truy vấn theo prefix với chi phí node và pointer lớn hơn.

## 17. Suffix cây (tree / 트리)

**Cây hậu tố (Suffix Tree / 접미사 트리)** là compressed trie của mọi suffix.

Suffix Trie naive có thể `Θ(n²)` nút (node / 노드)/ký tự. Suffix cây (tree / 트리) nén các chuỗi nút (node / 노드) một-con thành một cạnh có nhãn là một đoạn của văn bản (text / 텍스트) gốc.

Thay vì sao chép nhãn cạnh, lưu:

```text
(start, end)
```

trỏ vào string gốc.

Với terminal symbol và construction chuẩn, Suffix cây (tree / 트리) có số nút (node / 노드) tuyến tính theo `n`.

Suffix tree trả lời prefix/path query bằng cách đi theo cạnh và có thể báo occurrence ở subtree. Cách tìm này mạnh, nhưng correctness phụ thuộc việc quản lý edge label, leaf và termination chính xác.

## 18. tìm kiếm (search / 검색) trong Suffix cây (tree / 트리)

Mẫu (pattern / 패턴) tìm kiếm (search / 검색) đi theo nhãn cạnh. Nếu biểu diễn (representation / 표현) cạnh dùng chỉ số vào văn bản (text / 텍스트), tổng số ký tự mẫu (pattern / 패턴) cần kiểm tra về lý tưởng là `O(m)`.

Sau khi tới locus của mẫu (pattern / 패턴), mọi leaf bên dưới tương ứng với occurrence.

Do đó độ phức tạp (complexity / 복잡도) tự nhiên là:

\[
O(m+k)
\]

với `k` là số occurrence phải xuất.

Suffix tree có thể xây tuyến tính bằng Ukkonen, nhưng active point, suffix link và extension rule khiến implementation khó kiểm chứng. Hiểu suffix link là chìa khóa để thấy vì sao mỗi phase không phải bắt đầu lại từ root.

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

Suffix link nối node biểu diễn chuỗi `aX` với node biểu diễn `X`, cho phép chuyển nhanh giữa các suffix liên tiếp. Ý tưởng link và end-position equivalence được nén khác đi trong suffix automaton.

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

Suffix automaton biểu diễn mọi substring bằng DAG các state và transition, thường nhỏ hơn suffix tree cho nhiều truy vấn. Để duy trì invariant endpos khi tách state, cần hiểu vai trò của clone.

## 21. Suffix Automaton

**Suffix Automaton (SAM / 접미 자동자)** là DFA tối thiểu đại diện cho tập substring của một chuỗi theo lớp tương đương end-position.

Mỗi trạng thái (state / 상태) thường giữ:

```text
len   -> độ dài substring dài nhất của lớp
link  -> suffix link
next  -> transition theo ký tự
```

Trạng thái (state / 상태) không đại diện một substring duy nhất mà đại diện một lớp substring có cùng tập vị trí kết thúc.

Clone không phải substring mới trong text; nó là state copy để tách hai tập end positions mà vẫn giữ transition đúng. Sai clone sẽ phá invariant và làm hỏng cả count lẫn occurrence query.

## 22. Ý nghĩa của Clone trong SAM

Khi thêm ký tự mới, đôi lúc một trạng thái (state / 상태) cũ phải được tách về mặt ngữ nghĩa để giữ đúng automaton tối thiểu. Ta tạo **clone trạng thái (state / 상태)** có chuyển tiếp (transition / 전이)/link giống trạng thái (state / 상태) cũ nhưng `len` ngắn hơn.

Clone không tương ứng với một prefix mới của văn bản (text / 텍스트). Nó là một trạng thái kỹ thuật cần thiết để chia lớp tương đương end-position.

Đây là phần quan trọng để hiểu SAM không phải “một trie tối ưu hóa”.

SAM đếm substring phân biệt bằng tổng `len[v] - len[link[v]]` trên các state. Công thức này đếm các độ dài mới mà mỗi state đại diện, không cần liệt kê substring.

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

Distinct-substring count kiểm tra phạm vi độ dài mà state đại diện; occurrence count lại cần propagate số lần kết thúc theo thứ tự topo của suffix links. Hai phép đếm dùng cùng SAM nhưng khác invariant.

## 24. Occurrence Count trong SAM

Nếu mỗi prefix-end trạng thái (state / 상태) được khởi tạo count 1, rồi propagate count theo thứ tự `len` giảm dần qua suffix link, ta thu được số end positions của mỗi trạng thái (state / 상태).

Khi đó có thể trả lời số lần xuất hiện của substring sau khi đi chuyển tiếp (transition / 전이) tới trạng thái (state / 상태) tương ứng, với caveat về cách substring được ánh xạ vào trạng thái (state / 상태).

Occurrence count trong SAM cho biết một substring xuất hiện bao nhiêu lần; để tìm longest common substring với chuỗi khác, ta duyệt chuỗi đó qua transition và giữ độ dài match tốt nhất.

## 25. Longest dùng chung (common / 공통) Substring với SAM

Xây SAM cho `A`, rồi quét `B`. Duy trì trạng thái (state / 상태) hiện tại và độ dài match; khi chuyển tiếp (transition / 전이) thất bại, đi suffix link để tìm ngữ cảnh (context / 맥락) ngắn hơn có thể tiếp tục.

Độ dài match lớn nhất là longest dùng chung (common / 공통) substring.

Đây là counterpart automaton của cách làm SA + LCP.

Longest common substring với SAM cho thấy mỗi cấu trúc phục vụ một workload khác. Chọn SA, suffix tree hay SAM cần cân query, thời gian xây, memory và khả năng cập nhật thay vì chọn theo tên thuật toán.

## 26. SA, Suffix cây (tree / 트리) hay SAM?

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Nhu cầu | Cấu trúc thường phù hợp |
|---|---|
| văn bản (text / 텍스트) tĩnh, bộ nhớ (memory / 메모리) gọn, tìm kiếm nhị phân (binary search / 이진 탐색)/RMQ | Suffix Array + LCP |
| traversal theo substring prefix và truy vấn (query / 쿼리) giàu cấu trúc | Suffix cây (tree / 트리) |
| online xây một chuỗi, substring-state queries | Suffix Automaton |

Không có cấu trúc “mạnh nhất”. biểu diễn (representation / 표현) phù hợp phụ thuộc truy vấn (query / 쿼리) set, bộ nhớ (memory / 메모리) ngân sách (budget / 예산) và độ phức tạp hiện thực (implementation / 구현) chấp nhận được.

Suffix array gọn và thuận lợi cho binary search, suffix tree mạnh ở path query nhưng nặng pointer, còn SAM gọn cho substring/language queries. FM-index thêm một lựa chọn nén dựa trên BWT cho pattern search.

## 27. FM-Index và Burrows–Wheeler Transform

Ở quy mô văn bản (text / 텍스트) lớn, suffix thứ tự (ordering / 순서) còn dẫn tới **Burrows–Wheeler Transform (BWT)** và FM-index.

FM-index dùng BWT + rank/select-like structures để hỗ trợ **backward tìm kiếm (search / 검색)** cho mẫu (pattern / 패턴) trong bộ nhớ nén hơn nhiều so với lưu suffix cây (tree / 트리) đầy đủ.

Đây là nền tảng quan trọng của compressed full-text indexing và bioinformatics.

Mô hình tư duy mở rộng:

> Suffix thứ tự (order / 순서) không chỉ hỗ trợ tìm kiếm nhị phân (binary search / 이진 탐색); nó còn làm lộ cấu trúc lặp của văn bản (text / 텍스트) để vừa nén vừa tìm kiếm.

FM-index dùng BWT và LF-mapping để đi ngược pattern trong không gian nhỏ, thường phù hợp text lớn. Nếu chưa có suffix array, SA-IS cung cấp một đường xây tuyến tính theo các lớp suffix.

## 28. SA-IS và Linear-Time Construction

Có các thuật toán xây SA tuyến tính như SA-IS, dựa trên phân loại suffix và induced sorting.

Chúng quan trọng về lý thuyết và trong hiện thực (implementation / 구현) chuyên dụng, nhưng prefix-doubling thường dễ học, dễ gỡ lỗi (debug / 디버그) và đủ tốt cho nhiều tải công việc (workload / 워크로드).

Không nên dùng thuật toán construction phức tạp hơn chỉ vì asymptotic tốt hơn nếu `n` và hệ số thực tế không yêu cầu.

SA-IS đạt linear-time dưới mô hình chi phí phù hợp bằng cách phân loại LMS và induce sort. Nhưng alphabet và cách mã hóa ký tự ảnh hưởng trực tiếp đến bucket, thứ tự và correctness.

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

Alphabet không chỉ là số lượng ký tự; Unicode cần normalization, code point và comparator nhất quán. Những lựa chọn đó quyết định kích thước rank/bucket và kéo theo memory footprint.

## 30. Bộ nhớ

SA cơ bản cần vài mảng số nguyên kích thước `O(n)`. Doubling có thể cần SA, rank, tmp và buffers sort.

Suffix cây (tree / 트리)/SAM dùng nhiều nút (node / 노드)/trạng thái (state / 상태) và chuyển tiếp (transition / 전이). Nếu alphabet lớn, map/băm (hash / 해시) chuyển tiếp (transition / 전이) tăng overhead; nếu alphabet nhỏ cố định, array chuyển tiếp (transition / 전이) nhanh hơn nhưng tốn chỗ trống.

Cùng `O(n)` nhưng hệ số bộ nhớ có thể chênh rất lớn.

Suffix structures thường dùng nhiều mảng `O(n)` và có thể thêm LCP/RMQ hoặc transition. Sau khi tính đủ dung lượng, cần xem layout và cache locality để tránh tốc độ thực tế kém hơn bound lý thuyết.

## 31. bộ nhớ đệm (cache / 캐시) Locality

SA và LCP là các mảng liên tiếp nên rất thân thiện với bộ nhớ đệm (cache / 캐시) và serialization.

Suffix cây (tree / 트리) nhiều nút (node / 노드)/con trỏ dễ tạo pointer chasing. SAM có thể nằm giữa hai thái cực tùy biểu diễn (representation / 표현) transitions.

Đây là lý do SA thường rất thực dụng dù cây hậu tố có truy vấn (query / 쿼리) độ phức tạp (complexity / 복잡도) lý thuyết đẹp.

Cache locality phụ thuộc việc mảng liên tục hay node/pointer phân tán. Với static text, có thể tối ưu layout mạnh; dynamic text lại buộc cân nhắc chi phí cập nhật và invalidation index.

## 32. Static vs động (dynamic / 동적) văn bản (text / 텍스트)

Suffix Array/cây (tree / 트리) cổ điển được tối ưu cho văn bản (text / 텍스트) tương đối tĩnh. Nếu văn bản (text / 텍스트) thay đổi giữa chuỗi, một edit có thể làm thay đổi rất nhiều suffix thứ tự (order / 순서).

Động (dynamic / 동적) full-text indexing cần cấu trúc phức tạp hơn hoặc chiến lược rebuild/batching.

Nếu tải công việc (workload / 워크로드) là append-only stream, SAM có lợi thế vì construction online tự nhiên hơn.

Static index cho query nhanh sau một lần build, còn dynamic text cần rebuild, append strategy hoặc cấu trúc khác. Khi trả nhiều vị trí, complexity phải gắn với số output thay vì chỉ n và query time.

## 33. Output-Sensitive Bound

Nếu mẫu (pattern / 패턴) xuất hiện `k` lần và API yêu cầu liệt kê mọi vị trí, độ phức tạp (complexity / 복잡도) không thể nhỏ hơn `Ω(k)`.

Một cấu trúc cho tìm kiếm (search / 검색) `O(m)` vẫn cần thêm `O(k)` để đầu ra (output / 출력) occurrences.

Đừng nhầm chi phí tìm vùng kết quả với chi phí materialize kết quả.

Output-sensitive bound mô tả chi phí `O(search + output)` khi kết quả nhiều hay ít. Kiểm thử suffix array cần chứng minh ordering và boundary trước khi tin vào benchmark.

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

Suffix array test nên so với danh sách suffix đã sort trực tiếp trên text nhỏ và kiểm tra permutation. Sau đó Kasai cần được kiểm chứng bằng LCP brute force để tách lỗi index khỏi lỗi construction.

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

Kasai test xác nhận LCP từng rank và invariant giảm khi dịch suffix; SAM test lại cần kiểm tra transition, suffix link, clone và count trên mọi substring của text nhỏ.

## 36. Kiểm thử SAM

Có thể generate mọi substring của chuỗi nhỏ bằng brute force và so:

```text
SAM accepts đúng mọi substring
SAM rejects các string không phải substring
số distinct substrings khớp brute force set
occurrence count khớp oracle
```

Clone-related bug thường lộ rõ qua random differential testing.

Kiểm thử SAM theo oracle brute force bắt được lỗi clone và end-position propagation. Những hiểu lầm phổ biến thường đến từ việc đánh đồng suffix array, suffix tree và SAM như cùng một cấu trúc.

## 37. Những hiểu lầm phổ biến

“Suffix Array lưu mọi suffix string” — sai; nó chỉ cần lưu chỉ mục (index / 인덱스).

“Có SA thì mọi substring truy vấn (query / 쿼리) là O(log n)” — còn phụ thuộc chi phí so mẫu (pattern / 패턴), LCP acceleration và đầu ra (output / 출력) kích thước (size / 크기).

“Suffix cây (tree / 트리) luôn tốt hơn SA vì truy vấn (query / 쿼리) O(m)” — bỏ qua bộ nhớ (memory / 메모리), bộ nhớ đệm (cache / 캐시) locality và hiện thực (implementation / 구현) độ phức tạp (complexity / 복잡도).

“SAM trạng thái (state / 상태) tương ứng đúng một substring” — sai; trạng thái (state / 상태) là lớp tương đương của nhiều substring.

“Coordinate của string luôn là ký tự Unicode thực” — sai nếu thời gian chạy (runtime / 런타임) chỉ mục (index / 인덱스) theo mã (code / 코드) đơn vị (unit / 단위)/byte.

Ba cấu trúc chia sẻ mục tiêu substring nhưng khác invariant, memory layout và query boundary. Mô hình tư duy cuối cùng nên bắt đầu từ workload rồi chọn representation, proof invariant và test oracle tương ứng.

## Mô hình tư duy

> Các cấu trúc hậu tố biến không gian `Θ(n²)` substring thành một biểu diễn (representation / 표현) tuyến tính bằng cách tổ chức `n` suffix và chia sẻ thông tin prefix giữa chúng.

Suffix Array khai thác **thứ tự**. LCP khai thác **mức giống nhau giữa hàng xóm trong thứ tự**. Suffix cây (tree / 트리) khai thác **nén đường đi prefix**. Suffix Automaton khai thác **lớp tương đương theo vị trí kết thúc**.

Khi gặp bài substring lớn, hãy hỏi: **văn bản (text / 텍스트) tĩnh hay append-only, cần tìm kiếm (search / 검색) hay counting/rank/RMQ, cần đầu ra (output / 출력) mọi occurrence không, bộ nhớ (memory / 메모리) có quan trọng không, alphabet là gì, và có cần construction đủ đơn giản để kiểm chứng không?**

Xem thêm: [String Algorithms](./00_string_algorithms.md), [Sparse Table](./05_sparse_table_and_static_range_queries.md), [Range Queries](./01_range_queries_fenwick_segment_tree.md), [Amortized & Probabilistic Thinking](./03_amortized_randomized_and_probabilistic_thinking.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
