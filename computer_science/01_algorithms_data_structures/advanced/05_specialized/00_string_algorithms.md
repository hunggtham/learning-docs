# String các thuật toán

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **String các thuật toán**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Đầu tiên phải định nghĩa “character”** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Cách đơn giản mẫu Matching** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối string algorithms với pattern, prefix và suffix, để tìm kiếm văn bản được chọn theo cấu trúc đầu vào.

**Thuật toán chuỗi (String Algorithms / 문자열 알고리즘)**

String là chuỗi (sequence / 시퀀스), nhưng không phải chuỗi (sequence / 시퀀스) “bình thường”. Ngoài vị trí, string còn có **prefix, suffix, border, repetition, alphabet, substring, thứ tự từ điển và encoding**. Những cấu trúc (structure / 구조) này cho phép ta reuse thông tin từ các phép so sánh trước thay vì quay lại so từng ký tự từ đầu.

Một mental mô hình tốt là:

> String các thuật toán thắng bằng cách ghi nhớ **điều gì đã biết về sự giống nhau của prefix/suffix** sau mỗi mismatch.

## Đầu tiên phải định nghĩa “character”

Trước cả KMP hay Trie, mã dùng trong hệ thống thực tế phải biết đơn vị (unit / 단위) đang xử lý là gì:

```text
byte
UTF-8 code unit
UTF-16 code unit
Unicode code point
grapheme cluster người dùng nhìn thấy
```

Trong C, string thường là byte mảng kết thúc bằng `\0`; nếu byte chứa UTF-8 thì một Unicode điểm mã có thể dài nhiều byte.

Trong Java, `char` là UTF-16 đơn vị mã. Một điểm mã ngoài BMP dùng cặp thay thế UTF-16.

Trong JavaScript, lập chỉ mục string cũng chủ yếu theo UTF-16 các đơn vị mã.

Emoji như `👨‍👩‍👧‍👦` có thể gồm nhiều các điểm mã nối bằng zero-width joiner. Vì vậy “reverse từng character” cho UI văn bản (text / 텍스트) không giống reverse các đơn vị mã.

thuật toán phải xác định sự trừu tượng (abstraction) tầng trước khi nói độ phức tạp (complexity / 복잡도) theo `n` characters.

> **Chuyển mạch:** Trong **String các thuật toán**, **Cách đơn giản mẫu Matching** tiếp nhận điểm tựa từ **Đầu tiên phải định nghĩa “character”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Border: khái niệm nối nhiều string các thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cách đơn giản mẫu Matching

Văn bản có độ dài `n`, mẫu có độ dài `m`. Cách đơn giản là thử đặt mẫu tại mọi vị trí bắt đầu:

```text
for start = 0..n-m:
    compare pattern[0..m-1] với text[start..]
```

trường hợp xấu nhất:

\[
O(nm)
\]

Ví dụ văn bản (text / 텍스트) nhiều `a` và mẫu `aaaa...ab`: mỗi start match gần hết mẫu rồi mới thất bại (fail / 실패), lặp lại nhiều công việc (work / 작업).

Cách đơn giản matching không sai; với mẫu ngắn hoặc dữ liệu (data / 데이터) nhỏ nó có thể đủ tốt. Vấn đề là nó **quên mọi prefix thông tin sau mismatch**.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **Border: khái niệm nối nhiều string các thuật toán** tiếp nhận điểm tựa từ **Cách đơn giản mẫu Matching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **hàm tiền tố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Border: khái niệm nối nhiều string các thuật toán

Một **border** của string là một proper prefix đồng thời là suffix.

Ví dụ `ababab` có border `abab` và `ab`.

Border trả lời câu hỏi:

> Sau khi match một đoạn rồi mismatch, ta có phần suffix nào của đoạn vừa match mà chắc chắn cũng là prefix của mẫu không?

KMP và prefix-function xoay quanh chính idea này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **hàm tiền tố** tiếp nhận điểm tựa từ **Border: khái niệm nối nhiều string các thuật toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao hàm tiền tố là O(n)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## hàm tiền tố

Với string `s`, hàm tiền tố `pi[i]` là length của longest proper prefix của `s[0..i]` đồng thời là suffix.

Khi tính `pi[i]`, giả sử ứng viên hiện tại:

```text
j = pi[i - 1]
```

Nếu:

```text
s[i] == s[j]
```

border mở rộng thành `j+1`.

Nếu mismatch, ứng viên border tiếp theo không cần thử mọi length. Nó phải là border của border hiện tại:

```text
j = pi[j - 1]
```

Ta reuse hierarchy của borders.

### Java cách triển khai

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```java
static int[] prefixFunction(String s) {
    int n = s.length();
    int[] pi = new int[n];

    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];

        while (j > 0 && s.charAt(i) != s.charAt(j)) {
            j = pi[j - 1];
        }

        if (s.charAt(i) == s.charAt(j)) {
            j++;
        }

        pi[i] = j;
    }
    return pi;
}
```

> **Chuyển mạch:** Trong **String các thuật toán**, **Vì sao hàm tiền tố là O(n)?** tiếp nhận điểm tựa từ **hàm tiền tố** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KMP Matching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao hàm tiền tố là O(n)?

Có nested `while`, nên nhìn bề ngoài dễ sợ `O(n^2)`. Nhưng `j` chỉ tăng dần qua outer iterations và mỗi fallback làm `j` giảm.

Tổng số lần tăng/giảm của matched-prefix length bị amortize tuyến tính. Ta không reset `j` về một giá trị lớn tùy ý rồi giảm lại vô hạn lần.

Đây là một mẫu amortized lập luận (reasoning / 추론) tương tự ngăn xếp (stack / 스택) monotonic hoặc đường đi compression ở mức nhẹ hơn.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **KMP Matching** tiếp nhận điểm tựa từ **Vì sao hàm tiền tố là O(n)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **hàm tiền tố ngoài mẫu matching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KMP Matching

KMP preprocess mẫu bằng hàm tiền tố, rồi quét văn bản (text / 텍스트) một lần.

Khi xảy ra không khớp sau khi đã khớp `j` ký tự, thay vì di chuyển con trỏ văn bản lùi lại, ta lùi trạng thái mẫu theo thông tin tiền tố:

```text
j = pi[j - 1]
```

Văn bản (text / 텍스트) character hiện tại có thể được thử lại với shorter hợp lệ prefix ứng viên.

Độ phức tạp (complexity / 복잡도):

\[
O(n+m)
\]

bộ nhớ:

\[
O(m)
\]

### JavaScript cách triển khai

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```js
function prefixFunction(s) {
  const pi = Array(s.length).fill(0);

  for (let i = 1; i < s.length; i++) {
    let j = pi[i - 1];
    while (j > 0 && s[i] !== s[j]) j = pi[j - 1];
    if (s[i] === s[j]) j++;
    pi[i] = j;
  }
  return pi;
}

function kmpSearch(text, pattern) {
  if (pattern.length === 0) return 0;

  const pi = prefixFunction(pattern);
  let j = 0;

  for (let i = 0; i < text.length; i++) {
    while (j > 0 && text[i] !== pattern[j]) {
      j = pi[j - 1];
    }

    if (text[i] === pattern[j]) j++;

    if (j === pattern.length) {
      return i - pattern.length + 1;
    }
  }
  return -1;
}
```

KMP không phải “magic tìm kiếm tuyến tính”; nó chỉ tránh so lại những prefix relations đã biết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **hàm tiền tố ngoài mẫu matching** tiếp nhận điểm tựa từ **KMP Matching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Z-Function** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## hàm tiền tố ngoài mẫu matching

`pi` còn dùng để tìm:

- borders của string;
- smallest period;
- prefix occurrences;
- lặp lại cấu trúc (structure / 구조).

Nếu chuỗi đầy đủ có độ dài `n` và border dài nhất có độ dài `b = pi[n-1]`, một chu kỳ ứng viên có thể là:

\[
p = n-b
\]

Nếu `n % p == 0`, string có thể là repetition của khối (block / 블록) length `p`.

> **Chuyển mạch:** Trong **String các thuật toán**, **Z-Function** tiếp nhận điểm tựa từ **hàm tiền tố ngoài mẫu matching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KMP vs Z** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Z-Function

**Z-function (Z 함수)** định nghĩa `Z[i]` là length của longest substring bắt đầu tại `i` khớp prefix của whole string.

Ví dụ với:

```text
a a b a a b a
0 1 0 4 1 0 1   (illustrative shape)
```

Z trực tiếp trả lời “prefix match dài bao nhiêu tại mỗi position?”.

Efficient Z thuật toán giữ một interval `[L,R)` mà prefix match đã biết. Nếu `i < R`, ta reuse dữ liệu (data / 데이터) từ mirrored prefix position trước khi mở rộng thêm.

Đây là cùng philosophy với KMP: không quên phép so sánh thông tin.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **KMP vs Z** tiếp nhận điểm tựa từ **Z-Function** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rabin-Karp và băm trượt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KMP vs Z

Hai structures chứa liên quan prefix-suffix thông tin nhưng bố trí khác nhau.

```text
KMP / pi -> mỗi prefix kết thúc ở i có border dài nhất bao nhiêu?
Z        -> từ i trở đi match prefix dài bao nhiêu?
```

Nhiều problems giải được bằng cả hai; chọn cách biểu diễn (representation / 표현) khiến lập luận (reasoning / 추론) đơn giản hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **Rabin-Karp và băm trượt** tiếp nhận điểm tựa từ **KMP vs Z** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Collision là tính đúng đắn concern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rabin-Karp và băm trượt

Thay vì so sánh toàn substring, **Rabin-Karp** so băm (hash / 해시) của mẫu với băm trượt của mỗi văn bản (text / 텍스트) cửa sổ (window / 윈도우).

Polynomial băm (hash / 해시) có dạng:

\[
H=s_0b^{m-1}+s_1b^{m-2}+\cdots+s_{m-1}\pmod M
\]

Khi cửa sổ dịch một vị trí, ta loại đóng góp của ký tự cũ và thêm ký tự mới thay vì tính lại toàn bộ trong `O(m)`.

kỳ vọng/practical matching có thể rất nhanh, nhất là khi cần nhiều tính bằng nhau của chuỗi con checks.

> **Chuyển mạch:** Trong **String các thuật toán**, **Collision là tính đúng đắn concern** tiếp nhận điểm tựa từ **Rabin-Karp và băm trượt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prefix băm (hash / 해시) và O(1) substring băm (hash / 해시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Collision là tính đúng đắn concern

Hai strings khác nhau có thể có cùng băm (hash / 해시).

Vì vậy:

```text
hash equal != chắc chắn string equal
```

Các chiến lược (strategy / 전략):

```text
hash match -> verify actual substring
use double hashing
use 64-bit overflow hash với risk model rõ ràng
use deterministic suffix/string structure nếu không chấp nhận collision
```

Trong security-sensitive đầu vào, băm (hash / 해시) thuật toán còn có đối kháng concerns.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **Prefix băm (hash / 해시) và O(1) substring băm (hash / 해시)** tiếp nhận điểm tựa từ **Collision là tính đúng đắn concern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trie và Prefix Sharing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prefix băm (hash / 해시) và O(1) substring băm (hash / 해시)

Ta precompute:

```text
H[i] = hash của prefix length i
pow[i] = b^i mod M
```

Giá trị băm của chuỗi con `[l,r)` có thể được suy ra từ hai giá trị băm tiền tố sau khi chuẩn hóa theo quy ước đa thức đã chọn.

Điều này cho phép nhiều các thuật toán làm tìm kiếm nhị phân trên length, phần tử trùng substring checks hoặc palindrome các phép so sánh.

Nhưng “O(1) tính bằng nhau của chuỗi con” chỉ xác định nếu cách biểu diễn không có collision hoặc có xác minh (verification / 확인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **Trie và Prefix Sharing** tiếp nhận điểm tựa từ **Prefix băm (hash / 해시) và O(1) substring băm (hash / 해시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Aho-Corasick: khớp nhiều mẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trie và Prefix Sharing

Trie lập chỉ mục khóa bằng đường đi của các ký hiệu. Nhiều từ có chung tiền tố sẽ dùng chung các nút.

Trie rất hợp với:

```text
autocomplete
prefix existence
lexicographic traversal
longest prefix match
routing/radix variants
```

Bảng băm (hash table / 해시 테이블) tốt cho chính xác khóa định danh (identity / 식별자) nhưng không tự nhiên cho prefix ngữ nghĩa (semantics / 의미론).

Xem chapter [Trie](../02_trees/04_tries.md).

> **Chuyển mạch:** Trong **String các thuật toán**, **Aho-Corasick: khớp nhiều mẫu** tiếp nhận điểm tựa từ **Trie và Prefix Sharing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **các liên kết thất bại là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Aho-Corasick: khớp nhiều mẫu

Nếu có hàng nghìn các mẫu và một văn bản (text / 텍스트) lớn, chạy KMP riêng từng mẫu lặp lại scanning công việc (work / 작업).

**Aho-Corasick (아호-코라식)** kết hợp:

```text
Trie          -> share common pattern prefixes
failure link  -> fallback như KMP khi mismatch
output links  -> report patterns kết thúc tại state
```

xây dựng automaton từ các mẫu; quét văn bản (text / 텍스트) gần tuyến tính theo văn bản (text / 텍스트) length cộng số matches.

Conceptually:

> KMP reuse prefix kiến thức (knowledge / 지식) của một mẫu; Aho-Corasick reuse prefix kiến thức (knowledge / 지식) của cả một set các mẫu.

Ứng dụng gồm từ khóa (keyword / 키워드) filtering, signature scanning, khớp từ điển và phát hiện đơn vị từ (token / 토큰).

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, sau nội dung của **Aho-Corasick: khớp nhiều mẫu**, **các liên kết thất bại là gì?** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Manacher's thuật toán cho palindrome** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## các liên kết thất bại là gì?

Ở trie trạng thái (state / 상태) đại diện prefix `P`, nếu next character không có nút con, liên kết thất bại dẫn tới longest hậu tố đúng của `P` cũng là prefix của một mẫu trong trie.

Đây chính là border idea được nâng từ một mẫu lên automaton nhiều các mẫu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **Manacher's thuật toán cho palindrome** tiếp nhận điểm tựa từ **các liên kết thất bại là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Longest Palindromic Substring: chọn thuật toán theo need** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Manacher's thuật toán cho palindrome

Palindrome substring có symmetry. Cách đơn giản expand-around-center là `O(n^2)` trường hợp xấu nhất.

**Manacher's thuật toán (매내처 알고리즘)** giữ rightmost palindrome đã biết. Với center mới nằm trong hiện tại right ranh giới, radius có thể khởi tạo từ mirror center trước khi cần expand thêm.

kết quả là `O(n)` để tìm palindrome radii cho mọi center.

Mental liên kết (connection / 연결) với Z thuật toán rất mạnh:

```text
cả hai giữ một interval match xa nhất
và reuse thông tin mirror/relative position bên trong interval đó
```

> **Chuyển mạch:** Trong **String các thuật toán**, **Longest Palindromic Substring: chọn thuật toán theo need** tiếp nhận điểm tựa từ **Manacher's thuật toán cho palindrome** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Suffix Structures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Longest Palindromic Substring: chọn thuật toán theo need

Nếu chỉ cần longest palindrome một lần và đầu vào vừa, center expansion `O(n^2)` có thể đủ, rất đơn giản.

Nếu `n` lớn hoặc cần radii cho mọi centers, Manacher `O(n)` hợp lý.

Nếu cần động palindrome các truy vấn, cấu trúc (structure / 구조) khác có thể cần.

Không nên dùng advanced thuật toán chỉ vì tồn tại.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **Suffix Structures** tiếp nhận điểm tựa từ **Longest Palindromic Substring: chọn thuật toán theo need** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **thứ tự từ điển** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suffix Structures

Substring các truy vấn trên tĩnh văn bản (text / 텍스트) thường dẫn tới mảng hậu tố, cây hậu tố hoặc suffix automaton.

khóa phép biến đổi:

> Mọi substring là prefix của một suffix.

Thay vì lập chỉ mục trực tiếp cho mọi `O(n^2)` chuỗi con, ta tổ chức `n` hậu tố rồi khai thác các tiền tố dùng chung và thứ tự giữa chúng.

Xem [Suffix Array, Suffix Tree và LCP](./04_suffix_arrays_suffix_trees_and_lcp.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **thứ tự từ điển** tiếp nhận điểm tựa từ **Suffix Structures** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Longest Phổ biến Prefix** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## thứ tự từ điển

So sánh chuỗi dừng tại ký hiệu khác nhau đầu tiên. Vì vậy các chuỗi đã sắp xếp có tính cục bộ theo tiền tố hữu ích: các chuỗi có chung tiền tố thường nằm gần nhau.

Trie và mảng hậu tố khai thác tính chất này theo hai cách khác nhau:

```text
Trie        -> explicit prefix tree
SuffixArray -> sorted order của suffix starting positions
```

> **Chuyển mạch:** Trong **String các thuật toán**, **Longest Phổ biến Prefix** tiếp nhận điểm tựa từ **thứ tự từ điển** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **String tính chu kỳ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Longest Phổ biến Prefix

Với hai chuỗi, cách tính LCP đơn giản là so sánh từ đầu cho tới vị trí đầu tiên không khớp.

Trong ngữ cảnh suffix array, mảng LCP lưu LCP của các hậu tố kề nhau trong thứ tự đã sắp xếp. Sau đó LCP giữa hai hậu tố bất kỳ có thể chuyển thành truy vấn cực tiểu trên một đoạn của mảng LCP.

Đây là composition rất hay:

```text
suffix array -> lexicographic order
LCP array    -> adjacent similarity
RMQ          -> arbitrary suffix LCP
```

String thuật toán thường mạnh khi ghép structures thay vì dùng một thuật toán cô lập.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **String tính chu kỳ** tiếp nhận điểm tựa từ **Longest Phổ biến Prefix** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fine-Wilf intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## String tính chu kỳ

String có period `p` nếu:

```text
s[i] == s[i-p]
```

cho mọi chỉ mục (index / 인덱스) phù hợp.

Border và chu kỳ có quan hệ chặt chẽ: nếu tiền tố độ dài `n-p` đồng thời là hậu tố, thì `p` là một chu kỳ ứng viên.

tính chu kỳ xuất hiện trong compression, mẫu repetition, synchronization và tổ hợp (combinatorics) on words.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **Fine-Wilf intuition** tiếp nhận điểm tựa từ **String tính chu kỳ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Minimal Rotation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fine-Wilf intuition

Nếu string có hai periods đủ “dài overlap”, gcd của hai periods cũng trở thành period dưới điều kiện Fine-Wilf. Không cần dùng theorem này hằng ngày, nhưng nó cho thấy periodic cấu trúc (structure / 구조) không phải collection mẹo; có algebra/tổ hợp (combinatorics) rõ ràng phía sau.

> **Chuyển mạch:** Trong **String các thuật toán**, **Minimal Rotation** tiếp nhận điểm tựa từ **Fine-Wilf intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **String Matching trong xử lý luồng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Minimal Rotation

Một bài toán (problem / 문제) khác là tìm lexicographically smallest rotation của chuỗi vòng. Cách đơn giản generate all rotations tốn `O(n^2)` bộ nhớ/thời gian (time / 시간).

Booth's thuật toán có thể làm tuyến tính bằng cách loại whole ranges of ứng viên starts sau mismatch.

mẫu lập luận (reasoning / 추론) giống nhiều string các thuật toán: một phép so sánh thất bại không chỉ loại một ứng viên, mà loại cả một vùng dựa trên thứ tự (order / 순서) thông tin.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **String Matching trong xử lý luồng** tiếp nhận điểm tựa từ **Minimal Rotation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **C strings và bộ đệm an toàn (safety / 안전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## String Matching trong xử lý luồng

KMP/Aho-Corasick có thể xử lý văn bản (text / 텍스트) xử lý luồng vì trạng thái hiện tại chỉ cần matched-prefix/automaton trạng thái, không cần giữ toàn văn bản (text / 텍스트).

Điều này quan trọng trong logs/mạng streams. thuật toán độ phức tạp (complexity / 복잡도) giống nhau nhưng mô hình bộ nhớ (memory model) tốt hơn batch substring tìm kiếm (search / 검색).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **C strings và bộ đệm an toàn (safety / 안전)** tiếp nhận điểm tựa từ **String Matching trong xử lý luồng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java String specifics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## C strings và bộ đệm an toàn (safety / 안전)

Trong C, `strlen` là `O(n)` nếu không bộ nhớ đệm length. Gọi `strlen` trong vòng lặp (loop / 루프) điều kiện có thể vô tình tạo quadratic hành vi tùy trình biên dịch/thư viện (library / 라이브러리) ngữ cảnh (context / 맥락).

String các bộ đệm phải có sức chứa (capacity / 용량) và null-termination discipline rõ. `memcpy`/`memcmp` làm việc trên byte, không Unicode characters.

Nếu dữ liệu (data / 데이터) có thể chứa zero byte, C string sự trừu tượng không phù hợp; dùng `(pointer,length)` byte slice.

> **Chuyển mạch:** Trong **String các thuật toán**, **Java String specifics** tiếp nhận điểm tựa từ **C strings và bộ đệm an toàn (safety / 안전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **JavaScript String specifics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java String specifics

`String` là bất biến sau khi tạo. Ngữ nghĩa và cách bố trí của `substring` đã thay đổi qua các phiên bản Java; không nên giả định rằng chuỗi con chia sẻ mảng nền trong Java hiện đại.

lặp lại concatenation trong vòng lặp (loop / 루프):

```java
s = s + piece;
```

có thể tạo nhiều các lần cấp phát/copies. `StringBuilder` phù hợp hơn khi xây dựng kết quả incrementally.

`charAt()` trả UTF-16 đơn vị mã. Muốn iterate Unicode các điểm mã, dùng APIs như `codePoints()` hoặc `codePointAt` cẩn thận với lập chỉ mục.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **JavaScript String specifics** tiếp nhận điểm tựa từ **Java String specifics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Choosing the right string technique** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## JavaScript String specifics

`String.length` là số UTF-16 các đơn vị mã, không phải số Unicode các điểm mã/graphemes.

`for...of` iterate các điểm mã tốt hơn direct lập chỉ mục cho các cặp thay thế UTF-16, nhưng vẫn không tự động group các cụm ký tự hiển thị.

`Intl.Segmenter` có thể hữu ích cho phân đoạn theo cách người dùng nhìn thấy trong UI/lĩnh vực (domain / 도메인) cần graphemes; đó là tầng khác với classic DSA string matching.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **Choosing the right string technique** tiếp nhận điểm tựa từ **JavaScript String specifics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Choosing the right string technique

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Nhu cầu | Structure/thuật toán tự nhiên |
|---|---|
| một mẫu trong một văn bản (text / 텍스트) | KMP / Z / thư viện (library / 라이브러리) tìm kiếm (search / 검색) |
| nhiều chính xác các mẫu trong stream | Aho-Corasick |
| prefix dictionary/tự động hoàn thành | Trie / radix cây |
| many substring các truy vấn trên tĩnh văn bản (text / 텍스트) | mảng hậu tố + LCP |
| substring-trạng thái analytics | suffix automaton |
| palindrome radii | Manacher |
| probabilistic tính bằng nhau của chuỗi con | băm trượt |
| Unicode user-visible segmentation | Unicode/grapheme-aware tầng |

Đây không phải bảng học thuộc; mỗi lựa chọn phản ánh thông tin cần reuse.

> **Chuyển mạch:** Trong **String các thuật toán**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Choosing the right string technique** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử string các thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“KMP nhanh vì không bao giờ so sánh lại character.”** Không chính xác. Một văn bản (text / 텍스트) character có thể tham gia nhiều các phép so sánh, nhưng tổng các phép so sánh bị bound tuyến tính nhờ fallback cấu trúc (structure / 구조).

**“băm (hash / 해시) equal nghĩa là substring equal.”** Không nếu băm (hash / 해시) có collision.

**“Java/JS character = Unicode character.”** `char`/chỉ mục (index / 인덱스) thường là UTF-16 đơn vị mã.

**“Trie luôn nhanh hơn HashMap cho strings.”** Trie trả prefix năng lực (capability / 역량) nhưng bộ nhớ overhead có thể rất lớn.

**“Advanced string thuật toán luôn tốt hơn built-in tìm kiếm (search / 검색).”** thư viện (library / 라이브러리) cách triển khai có thể dùng bản địa (native / 네이티브)/vectorized optimizations rất mạnh. DSA kiến thức (knowledge / 지식) giúp chọn mô hình, không buộc reimplement mọi thứ.

**“Suffix Array lập chỉ mục trực tiếp mọi chuỗi con.”** Không; nó sắp xếp các vị trí bắt đầu của hậu tố, rồi truy vấn chuỗi con trở thành tìm kiếm theo tiền tố trên thứ tự hậu tố.

> **Chuyển mạch:** Ở chặng này của **String các thuật toán**, **kiểm thử string các thuật toán** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy mở rộng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử string các thuật toán

mẫu matching tests nên cover:

```text
empty pattern semantics
pattern longer than text
all characters equal
match at start/end
multiple overlapping matches
no match
duplicate patterns
Unicode surrogate pairs / multibyte encoding theo chosen model
```

Một differential kiểm thử (test / 테스트) tốt là so sánh KMP đầu ra với đơn giản naive matcher trên ngẫu nhiên small strings.

băm trượt nên kiểm thử (test / 테스트) collision-handling đường đi nếu cách triển khai verify matches.

Aho-Corasick cần kiểm thử (test / 테스트) một mẫu là suffix của mẫu khác, vì đầu ra/các liên kết thất bại dễ sai ở trường hợp (case / 사례) này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **String các thuật toán**, **Mô hình tư duy mở rộng** gom các mảnh từ **kiểm thử string các thuật toán** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy mở rộng

> String các thuật toán là nghệ thuật **không quên cấu trúc (structure / 구조) đã khám phá**. Prefix-function nhớ borders, Z nhớ prefix-match intervals, băm trượt nhớ algebraic dữ liệu tóm lược, Trie nhớ các tiền tố dùng chung, Aho-Corasick nhớ fallback giữa prefixes, suffix structures nhớ thứ tự (order / 순서)/share của suffixes.

Khi gặp bài toán chuỗi, đừng bắt đầu bằng tên thuật toán. Hãy hỏi: truy vấn dựa trên tiền tố, hậu tố, chuỗi con, tính lặp, thứ tự hay việc chia sẻ giữa nhiều mẫu? Dữ liệu tĩnh hay được xử lý theo luồng? Cần kết quả chính xác tuyệt đối hay chấp nhận băm xác suất? Và “ký tự” trong miền bài toán thực sự là byte, điểm mã hay cụm tự vị (grapheme)?

> **Bàn giao:** Sau **Mô hình tư duy mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
