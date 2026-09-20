# String Algorithms
**Thuật toán chuỗi (String Algorithms / 문자열 알고리즘)**

String là sequence nhưng có structure đặc biệt: alphabet, prefix, suffix, repetitions và patterns. Algorithms chuyên dụng tăng tốc bằng cách reuse information từ các comparisons trước.

## Naive matching

Pattern length `m`, text length `n`. Thử pattern ở mọi vị trí có worst `O(nm)` vì characters có thể bị so sánh lại nhiều lần.

## KMP và prefix function

KMP tránh quay text pointer lùi lại. Khi mismatch sau khi đã match một prefix dài, nếu suffix của đoạn đã match cũng là prefix của pattern, phần đó có thể reuse.

Prefix function `pi[i]` lưu length của longest proper prefix của `pattern[0..i]` đồng thời là suffix. Preprocess `O(m)`, matching `O(n)`, tổng `O(n+m)`.

## Z-function

`Z[i]` là length của longest prefix của string trùng substring bắt đầu ở `i`. Nó cung cấp một representation khác của prefix-match information và giải nhiều bài pattern/prefix trong tuyến tính.

## Rolling hash

Rabin-Karp dùng rolling hash để update hash của sliding substring nhanh. Polynomial hash dạng:

\[
H=s_0b^{k-1}+s_1b^{k-2}+\cdots+s_{k-1}\pmod M
\]

Hash collision có thể xảy ra, nên hash equality không phải string equality tuyệt đối nếu không verify hoặc dùng multiple hashes với risk đã đánh giá.

## Trie và multi-pattern

Trie phù hợp prefix/many-word queries. Aho-Corasick mở rộng trie với failure links để match nhiều patterns trong text cùng lúc.

## Unicode caveat

Java `char` và JavaScript string indexing chủ yếu dựa trên UTF-16 code units. Một Unicode code point có thể dùng surrogate pair; một grapheme người dùng nhìn thấy còn có thể gồm nhiều code points. Trong C, strings thường là byte sequences trừ khi library/encoding layer quy định khác.

Vì vậy “character” phải được định nghĩa rõ: byte, code unit, code point hay grapheme cluster.

## Mental Model

> String algorithms nhanh vì chúng không quên những gì đã biết về prefix/suffix sau một mismatch.

## KMP prefix function được xây như thế nào?

Khi tính `pi[i]`, ta muốn longest border của prefix kết thúc tại `i`. Giả sử border candidate dài `j = pi[i-1]`. Nếu `s[i] == s[j]`, border mở rộng được thành `j+1`.

Nếu mismatch, thay vì thử lại mọi độ dài nhỏ hơn, ta nhảy tới border của border:

```text
j = pi[j-1]
```

vì bất kỳ candidate border hợp lệ tiếp theo cũng phải là suffix của border hiện tại. Tổng số back-jumps trên toàn quá trình bị amortize tuyến tính, nên prefix-function `O(n)`.

### Java implementation

```java
int[] prefixFunction(String s) {
    int n = s.length();
    int[] pi = new int[n];

    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && s.charAt(i) != s.charAt(j)) {
            j = pi[j - 1];
        }
        if (s.charAt(i) == s.charAt(j)) j++;
        pi[i] = j;
    }
    return pi;
}
```

## Aho–Corasick

Nếu cần tìm hàng nghìn patterns trong cùng text, chạy KMP riêng từng pattern lặp lại work. Aho–Corasick xây trie của patterns và thêm failure links tương tự KMP border fallback.

Traversal text trở thành automaton walk gần `O(text length + matches + automaton size)`.

Mental connection:

```text
Trie          = prefix sharing giữa patterns
KMP fallback  = reuse suffix/prefix knowledge khi mismatch
Aho-Corasick  = kết hợp hai idea
```

## Rolling hash và substring equality

Với prefix hashes, substring hash có thể lấy `O(1)` sau preprocessing. Điều này hữu ích cho binary-search-on-length problems, duplicate substring candidates và palindrome variants.

Nhưng hash collision là correctness issue. Nếu algorithm phải deterministic exact, cần verify substring, dùng multiple moduli với risk được định lượng, hoặc dùng suffix/string structures deterministic.

## Unicode: code point chưa phải user-perceived character

Emoji như `👨‍👩‍👧‍👦` có thể gồm nhiều code points nối bằng zero-width joiners. Vì vậy “reverse string by character” cho UI text khác hoàn toàn “reverse UTF-16 code units”.

DSA trên text production phải xác định unit của algorithm: byte, UTF-16 unit, code point hay grapheme cluster.
