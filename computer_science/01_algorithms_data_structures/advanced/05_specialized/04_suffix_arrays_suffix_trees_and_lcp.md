# Suffix Array, Suffix Tree và LCP
**접미사 배열, 접미사 트리, LCP**

Nhiều string queries hỏi về substrings: pattern có xuất hiện không, longest repeated substring là gì, hai suffix giống nhau bao lâu? Một cách mạnh là tổ chức **tất cả suffixes** của string.

Với `banana`:

```text
banana
anana
nana
ana
na
a
```

Sort suffixes lexicographically tạo suffix array.

## Suffix Array

Suffix Array (SA / 접미사 배열) lưu starting indices của suffixes theo lexicographic order.

Với `banana`:

```text
5: a
3: ana
1: anana
0: banana
4: na
2: nana
```

SA là:

```text
[5, 3, 1, 0, 4, 2]
```

## Pattern search

Mọi suffix bắt đầu bằng pattern tạo một contiguous interval trong suffix order. Vì vậy ta có thể binary search lower/upper boundary của pattern trên suffix array.

Nếu comparison pattern-suffix tốn `O(m)`, query khoảng `O(m log n)` theo cách đơn giản. Các structure bổ sung có thể cải thiện hơn.

## LCP array

LCP (Longest Common Prefix / 최장 공통 접두사) giữa adjacent suffixes trong SA ghi độ dài prefix chung.

Longest repeated substring length chính là maximum LCP giữa adjacent suffixes: nếu một substring lặp lại, ít nhất hai suffixes chia sẻ prefix đó; trong sorted suffix order, các suffixes gần nhau nhất về lexicographic structure sẽ lộ ra overlap.

Kasai algorithm xây LCP từ SA trong `O(n)` sau khi có rank array, bằng cách reuse `h-1` lower bound khi chuyển sang suffix kế tiếp.

## Suffix Tree

Suffix tree là compressed trie của tất cả suffixes. Naive suffix trie có `O(n^2)` nodes; compression gom chains thành edge labels là substrings, và algorithms như Ukkonen xây suffix tree tuyến tính với alphabet assumptions thích hợp.

Suffix tree hỗ trợ nhiều queries mạnh nhưng implementation phức tạp và memory overhead lớn. Suffix array thường compact và cache-friendly hơn.

## Suffix Automaton

Suffix automaton là minimal DFA nhận mọi substrings của một string. Nó có `O(n)` states/transitions theo bounded alphabet assumptions và rất mạnh cho distinct-substring count, occurrence/state analysis và longest common substring variants.

Mental model khác suffix tree nhưng cùng mục tiêu: compress enormous substring set bằng cách chia sẻ equivalent future behavior.

## Khi dùng gì?

Nếu chỉ cần single-pattern search, KMP/Z có thể đơn giản nhất.

Nếu nhiều prefix words, Trie/Aho–Corasick.

Nếu nhiều substring/order queries trên một static text, suffix array + LCP thường thực dụng.

Nếu cần advanced substring automaton properties, suffix automaton đáng học.

## Mental Model

> Suffix structures biến “mọi substring” thành vấn đề trên **prefixes của suffixes**. Thay vì index từng substring trực tiếp, ta index các starting positions và khai thác shared prefixes.

Xem: [String Algorithms](./00_string_algorithms.md), [Searching](../04_algorithmic_paradigms/00_searching.md).
