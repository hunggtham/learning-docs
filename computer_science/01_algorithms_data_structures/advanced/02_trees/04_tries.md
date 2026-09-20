# Trie
**Cây tiền tố (Trie / 트라이, 접두사 트리)**

Trie tổ chức strings theo prefix. Các từ `car`, `card`, `care`, `cat` chia sẻ path `c -> a`, nên prefix chung trở thành structure chung.

Mỗi node thường có mapping từ symbol sang child và marker `isEnd`.

```text
(root)
  |
  c
  |
  a
 / \
r   t*
|\
d* e*
```

## Complexity

Nếu string length là `L`, insert/search thường `O(L)` giả sử child lookup đủ nhanh. Cost không trực tiếp phụ thuộc số words, nhưng memory có thể lớn vì nhiều nodes/maps.

Java sketch:

```java
class TrieNode {
    Map<Character, TrieNode> next = new HashMap<>();
    boolean end;
}
```

## Prefix queries

Hash map rất tốt cho exact key lookup nhưng không tự nhiên cho “có word nào bắt đầu bằng `app`?” hoặc autocomplete. Trie trả lời prefix bằng việc đi theo path của prefix rồi enumerate descendants.

## Compressed trie / radix tree

Nếu nhiều nodes chỉ có một child, có thể nén chuỗi edges thành một segment dài hơn để giảm overhead. Routing tables và prefix matching thường dùng trie/radix variants.

## Mental Model

> Trie biến key string thành path. Nếu structure bên trong key — đặc biệt prefix — có ý nghĩa, trie có thể khai thác trực tiếp structure đó.

## Dense children array hay map?

Nếu alphabet nhỏ cố định, mỗi node có array children:

```text
children[26]
```

Lookup rất nhanh nhưng memory lãng phí nếu trie sparse. Nếu alphabet lớn/Unicode, hash map/tree map cho children tiết kiệm sparse memory nhưng tăng overhead lookup/allocation.

Representation phụ thuộc alphabet distribution và workload.

## Delete

Xóa word không thể đơn giản xóa path, vì path có thể được word khác dùng chung. Ta bỏ `isEnd`; sau đó chỉ reclaim node từ dưới lên nếu node không còn child và không là end của word khác.

Đây là một case đẹp cho reference/count/shared-prefix reasoning.

## Trie cho integer bits

Trie không chỉ cho characters. Binary trie xem mỗi integer như sequence bits từ high to low. Nó hỗ trợ queries như maximum XOR: tại mỗi bit, ưu tiên đi child có bit đối nghịch để làm XOR bit hiện tại bằng 1.

## Patricia/Radix compression

Nếu nhiều nodes có một child, path compression lưu whole substring/bit segment trên một edge. Điều này giảm node count và pointer overhead. Radix trees được dùng trong networking, routing và key-value systems vì prefix semantics tự nhiên.

## Trie vs hash set

Exact lookup của hash set thường compact và nhanh hơn. Trie đáng trả memory khi prefix sharing/prefix query/lexicographic traversal có giá trị.

> Trie tối ưu cho **structure bên trong key**, hash table tối ưu cho **identity của toàn key**.
