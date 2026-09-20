# String Algorithms
**Thuật toán chuỗi (String Algorithms / 문자열 알고리즘)**

String là sequence, nhưng không phải sequence “bình thường”. Ngoài vị trí, string còn có **prefix, suffix, border, repetition, alphabet, substring, lexicographic order và encoding**. Những structure này cho phép ta reuse thông tin từ các comparisons trước thay vì quay lại so từng ký tự từ đầu.

Một mental model tốt là:

> String algorithms thắng bằng cách ghi nhớ **điều gì đã biết về sự giống nhau của prefix/suffix** sau mỗi mismatch.

## Đầu tiên phải định nghĩa “character”

Trước cả KMP hay Trie, production code phải biết unit đang xử lý là gì:

```text
byte
UTF-8 code unit
UTF-16 code unit
Unicode code point
grapheme cluster người dùng nhìn thấy
```

Trong C, string thường là byte array kết thúc bằng `\0`; nếu bytes chứa UTF-8 thì một Unicode code point có thể dài nhiều bytes.

Trong Java, `char` là UTF-16 code unit. Một code point ngoài BMP dùng surrogate pair.

Trong JavaScript, indexing string cũng chủ yếu theo UTF-16 code units.

Emoji như `👨‍👩‍👧‍👦` có thể gồm nhiều code points nối bằng zero-width joiner. Vì vậy “reverse từng character” cho UI text không giống reverse code units.

Algorithm phải xác định abstraction level trước khi nói complexity theo `n` characters.

## Naive Pattern Matching

Text length `n`, pattern length `m`. Cách đơn giản là thử pattern tại mọi start position:

```text
for start = 0..n-m:
    compare pattern[0..m-1] với text[start..]
```

Worst case:

\[
O(nm)
\]

Ví dụ text nhiều `a` và pattern `aaaa...ab`: mỗi start match gần hết pattern rồi mới fail, lặp lại nhiều work.

Naive matching không sai; với pattern ngắn hoặc data nhỏ nó có thể đủ tốt. Vấn đề là nó **quên mọi prefix information sau mismatch**.

## Border: khái niệm nối nhiều string algorithms

Một **border** của string là một proper prefix đồng thời là suffix.

Ví dụ `ababab` có border `abab` và `ab`.

Border trả lời câu hỏi:

> Sau khi match một đoạn rồi mismatch, ta có phần suffix nào của đoạn vừa match mà chắc chắn cũng là prefix của pattern không?

KMP và prefix-function xoay quanh chính idea này.

## Prefix Function

Với string `s`, prefix function `pi[i]` là length của longest proper prefix của `s[0..i]` đồng thời là suffix.

Khi tính `pi[i]`, giả sử candidate hiện tại:

```text
j = pi[i - 1]
```

Nếu:

```text
s[i] == s[j]
```

border mở rộng thành `j+1`.

Nếu mismatch, candidate border tiếp theo không cần thử mọi length. Nó phải là border của border hiện tại:

```text
j = pi[j - 1]
```

Ta reuse hierarchy của borders.

### Java implementation

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

## Vì sao prefix function là O(n)?

Có nested `while`, nên nhìn bề ngoài dễ sợ `O(n^2)`. Nhưng `j` chỉ tăng dần qua outer iterations và mỗi fallback làm `j` giảm.

Tổng số lần tăng/giảm của matched-prefix length bị amortize tuyến tính. Ta không reset `j` về một giá trị lớn tùy ý rồi giảm lại vô hạn lần.

Đây là một pattern amortized reasoning tương tự stack monotonic hoặc path compression ở mức nhẹ hơn.

## KMP Matching

KMP preprocess pattern bằng prefix function, rồi scan text một lần.

Khi mismatch sau khi đã match `j` chars, thay vì move text pointer backward, ta fallback:

```text
j = pi[j - 1]
```

Text character hiện tại có thể được thử lại với shorter valid prefix candidate.

Complexity:

\[
O(n+m)
\]

Memory:

\[
O(m)
\]

### JavaScript implementation

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

KMP không phải “magic linear search”; nó chỉ tránh so lại những prefix relations đã biết.

## Prefix Function ngoài pattern matching

`pi` còn dùng để tìm:

- borders của string;
- smallest period;
- prefix occurrences;
- repeated structure.

Nếu full string length `n` và longest border length `b = pi[n-1]`, candidate period có thể là:

\[
p = n-b
\]

Nếu `n % p == 0`, string có thể là repetition của block length `p`.

## Z-Function

**Z-function (Z 함수)** định nghĩa `Z[i]` là length của longest substring bắt đầu tại `i` khớp prefix của whole string.

Ví dụ với:

```text
a a b a a b a
0 1 0 4 1 0 1   (illustrative shape)
```

Z trực tiếp trả lời “prefix match dài bao nhiêu tại mỗi position?”.

Efficient Z algorithm giữ một interval `[L,R)` mà prefix match đã biết. Nếu `i < R`, ta reuse data từ mirrored prefix position trước khi mở rộng thêm.

Đây là cùng philosophy với KMP: không quên comparison information.

## KMP vs Z

Hai structures chứa liên quan prefix-suffix information nhưng layout khác nhau.

```text
KMP / pi -> mỗi prefix kết thúc ở i có border dài nhất bao nhiêu?
Z        -> từ i trở đi match prefix dài bao nhiêu?
```

Nhiều problems giải được bằng cả hai; chọn representation khiến reasoning đơn giản hơn.

## Rabin-Karp và Rolling Hash

Thay vì compare toàn substring, **Rabin-Karp** so hash của pattern với rolling hash của mỗi text window.

Polynomial hash có dạng:

\[
H=s_0b^{m-1}+s_1b^{m-2}+\cdots+s_{m-1}\pmod M
\]

Khi window dịch một position, ta remove contribution cũ và add character mới thay vì tính lại `O(m)`.

Expected/practical matching có thể rất nhanh, nhất là khi cần nhiều substring equality checks.

## Collision là correctness concern

Hai strings khác nhau có thể có cùng hash.

Vì vậy:

```text
hash equal != chắc chắn string equal
```

Các strategy:

```text
hash match -> verify actual substring
use double hashing
use 64-bit overflow hash với risk model rõ ràng
use deterministic suffix/string structure nếu không chấp nhận collision
```

Trong security-sensitive input, hash algorithm còn có adversarial concerns.

## Prefix Hash và O(1) substring hash

Ta precompute:

```text
H[i] = hash của prefix length i
pow[i] = b^i mod M
```

Substring `[l,r)` có thể lấy từ hai prefix hashes sau normalization theo chosen polynomial convention.

Điều này cho phép nhiều algorithms làm binary search trên length, duplicate substring checks hoặc palindrome comparisons.

Nhưng “O(1) substring equality” chỉ deterministic nếu representation không có collision hoặc có verification.

## Trie và Prefix Sharing

Trie index keys bằng path của symbols. Nhiều words chung prefix share nodes.

Trie rất hợp với:

```text
autocomplete
prefix existence
lexicographic traversal
longest prefix match
routing/radix variants
```

Hash table tốt cho exact key identity nhưng không tự nhiên cho prefix semantics.

Xem chapter [Trie](../02_trees/04_tries.md).

## Aho-Corasick: multi-pattern matching

Nếu có hàng nghìn patterns và một text lớn, chạy KMP riêng từng pattern lặp lại scanning work.

**Aho-Corasick (아호-코라식)** kết hợp:

```text
Trie          -> share common pattern prefixes
failure link  -> fallback như KMP khi mismatch
output links  -> report patterns kết thúc tại state
```

Build automaton từ patterns; scan text gần tuyến tính theo text length cộng số matches.

Conceptually:

> KMP reuse prefix knowledge của một pattern; Aho-Corasick reuse prefix knowledge của cả một set patterns.

Ứng dụng gồm keyword filtering, signature scanning, dictionary matching và token detection.

## Failure links là gì?

Ở trie state đại diện prefix `P`, nếu next character không có child, failure link dẫn tới longest proper suffix của `P` cũng là prefix của một pattern trong trie.

Đây chính là border idea được nâng từ một pattern lên automaton nhiều patterns.

## Manacher's Algorithm cho palindrome

Palindrome substring có symmetry. Naive expand-around-center là `O(n^2)` worst-case.

**Manacher's algorithm (매내처 알고리즘)** giữ rightmost palindrome đã biết. Với center mới nằm trong current right boundary, radius có thể khởi tạo từ mirror center trước khi cần expand thêm.

Result là `O(n)` để tìm palindrome radii cho mọi center.

Mental connection với Z algorithm rất mạnh:

```text
cả hai giữ một interval match xa nhất
và reuse thông tin mirror/relative position bên trong interval đó
```

## Longest Palindromic Substring: chọn algorithm theo need

Nếu chỉ cần longest palindrome một lần và input vừa, center expansion `O(n^2)` có thể đủ, rất đơn giản.

Nếu `n` lớn hoặc cần radii cho mọi centers, Manacher `O(n)` hợp lý.

Nếu cần dynamic palindrome queries, structure khác có thể cần.

Không nên dùng advanced algorithm chỉ vì tồn tại.

## Suffix Structures

Substring queries trên static text thường dẫn tới suffix array, suffix tree hoặc suffix automaton.

Key transformation:

> Mọi substring là prefix của một suffix.

Thay vì index mọi `O(n^2)` substrings trực tiếp, ta tổ chức `n` suffixes rồi khai thác shared prefixes/order.

Xem [Suffix Array, Suffix Tree và LCP](./04_suffix_arrays_suffix_trees_and_lcp.md).

## Lexicographic Order

String comparison dừng tại first differing symbol. Vì vậy sorted strings có useful prefix locality: strings có prefix chung thường nằm gần nhau.

Trie và suffix array khai thác property này theo hai cách khác nhau:

```text
Trie        -> explicit prefix tree
SuffixArray -> sorted order của suffix starting positions
```

## Longest Common Prefix

Cho hai strings, naive LCP compare từ đầu cho tới mismatch.

Trong suffix-array context, LCP array lưu LCP của adjacent sorted suffixes. Sau đó LCP giữa arbitrary suffixes có thể biến thành Range Minimum Query trên LCP interval.

Đây là composition rất hay:

```text
suffix array -> lexicographic order
LCP array    -> adjacent similarity
RMQ          -> arbitrary suffix LCP
```

String algorithm thường mạnh khi ghép structures thay vì dùng một thuật toán cô lập.

## String Periodicity

String có period `p` nếu:

```text
s[i] == s[i-p]
```

cho mọi index phù hợp.

Borders và periods có relation sâu: nếu prefix length `n-p` cũng là suffix, `p` là candidate period.

Periodicity xuất hiện trong compression, pattern repetition, synchronization và combinatorics on words.

## Fine-Wilf intuition

Nếu string có hai periods đủ “dài overlap”, gcd của hai periods cũng trở thành period dưới điều kiện Fine-Wilf. Không cần dùng theorem này hằng ngày, nhưng nó cho thấy periodic structure không phải collection mẹo; có algebra/combinatorics rõ ràng phía sau.

## Minimal Rotation

Một problem khác là tìm lexicographically smallest rotation của cyclic string. Naive generate all rotations tốn `O(n^2)` memory/time.

Booth's algorithm có thể làm tuyến tính bằng cách loại whole ranges of candidate starts sau mismatch.

Pattern reasoning giống nhiều string algorithms: một comparison thất bại không chỉ loại một candidate, mà loại cả một vùng dựa trên order information.

## String Matching trong streaming

KMP/Aho-Corasick có thể process text streaming vì state hiện tại chỉ cần matched-prefix/automaton state, không cần giữ toàn text.

Điều này quan trọng trong logs/network streams. Algorithm complexity giống nhau nhưng memory model tốt hơn batch substring search.

## C strings và buffer safety

Trong C, `strlen` là `O(n)` nếu không cache length. Gọi `strlen` trong loop condition có thể vô tình tạo quadratic behavior tùy compiler/library context.

String buffers phải có capacity và null-termination discipline rõ. `memcpy`/`memcmp` làm việc trên bytes, không Unicode characters.

Nếu data có thể chứa zero byte, C string abstraction không phù hợp; dùng `(pointer,length)` byte slice.

## Java String specifics

`String` immutable. `substring` semantics/layout đã thay đổi qua Java versions; không nên assume substring share backing array trong modern Java.

Repeated concatenation trong loop:

```java
s = s + piece;
```

có thể tạo nhiều allocations/copies. `StringBuilder` phù hợp hơn khi build result incrementally.

`charAt()` trả UTF-16 code unit. Muốn iterate Unicode code points, dùng APIs như `codePoints()` hoặc `codePointAt` cẩn thận với indexing.

## JavaScript String specifics

`String.length` là số UTF-16 code units, không phải số Unicode code points/graphemes.

`for...of` iterate code points tốt hơn direct indexing cho surrogate pairs, nhưng vẫn không tự động group grapheme clusters.

`Intl.Segmenter` có thể hữu ích cho user-perceived segmentation trong UI/domain cần graphemes; đó là layer khác với classic DSA string matching.

## Choosing the right string technique

| Nhu cầu | Structure/algorithm tự nhiên |
|---|---|
| một pattern trong một text | KMP / Z / library search |
| nhiều exact patterns trong stream | Aho-Corasick |
| prefix dictionary/autocomplete | Trie / radix tree |
| many substring queries trên static text | suffix array + LCP |
| substring-state analytics | suffix automaton |
| palindrome radii | Manacher |
| probabilistic substring equality | rolling hash |
| Unicode user-visible segmentation | Unicode/grapheme-aware layer |

Đây không phải bảng học thuộc; mỗi lựa chọn phản ánh information cần reuse.

## Common misconceptions

**“KMP nhanh vì không bao giờ compare lại character.”** Không chính xác. Một text character có thể tham gia nhiều comparisons, nhưng tổng comparisons bị bound tuyến tính nhờ fallback structure.

**“Hash equal nghĩa là substring equal.”** Không nếu hash có collision.

**“Java/JS character = Unicode character.”** `char`/index thường là UTF-16 code unit.

**“Trie luôn nhanh hơn HashMap cho strings.”** Trie trả prefix capability nhưng memory overhead có thể rất lớn.

**“Advanced string algorithm luôn tốt hơn built-in search.”** Library implementation có thể dùng native/vectorized optimizations rất mạnh. DSA knowledge giúp chọn model, không buộc reimplement mọi thứ.

**“Suffix array index mọi substring trực tiếp.”** Không; nó sort starting positions của suffixes, rồi substring query trở thành prefix search trên suffix order.

## Testing string algorithms

Pattern matching tests nên cover:

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

Một differential test tốt là compare KMP output với simple naive matcher trên random small strings.

Rolling hash nên test collision-handling path nếu implementation verify matches.

Aho-Corasick cần test một pattern là suffix của pattern khác, vì output/failure links dễ sai ở case này.

## Mental Model mở rộng

> String algorithms là nghệ thuật **không quên structure đã khám phá**. Prefix-function nhớ borders, Z nhớ prefix-match intervals, rolling hash nhớ algebraic summary, Trie nhớ shared prefixes, Aho-Corasick nhớ fallback giữa prefixes, suffix structures nhớ order/share của suffixes.

Khi gặp string problem, đừng bắt đầu bằng tên thuật toán. Hãy hỏi: query dựa trên prefix, suffix, substring, repetition, order hay many-pattern sharing? Dữ liệu static hay streaming? Cần deterministic exactness hay probabilistic hash chấp nhận được? Và “character” trong domain thực sự là byte, code point hay grapheme?