# Đếm và tổ hợp: cấu trúc của không gian khả năng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Đếm và tổ hợp: cấu trúc của không gian khả năng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. quy tắc (rule / 규칙) of sum và quy tắc (rule / 규칙) of sản phẩm (product / 제품)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Khi nào sản phẩm (product / 제품) quy tắc (rule / 규칙) sai?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối counting với combinatorics và probability, để không gian mẫu được dựng trước khi tính xác suất.

Tổ hợp (combinatorics / 조합론) nghiên cứu cách đếm số cấu hình có thể có mà không cần liệt kê từng trường hợp. Đây là nền của xác suất rời rạc, độ phức tạp (complexity / 복잡도), tìm kiếm (search / 검색) không gian (space / 공간), hashing, coding và nhiều bài toán tối ưu.

Mô hình tư duy (mental model / 사고 모델) quan trọng:

```text
object space
→ decompose choices
→ remove symmetry / double counting
→ count configurations
→ infer probability or computational cost
```

Combinatorics không chỉ là nhớ `n!` hay `C(n,k)`. Nó là kỹ năng nhìn một cấu hình (configuration / 구성) như kết quả của nhiều quyết định nhỏ hơn.

## 1. quy tắc (rule / 규칙) of sum và quy tắc (rule / 규칙) of sản phẩm (product / 제품)

Nếu một tác vụ (task / 작업) có hai nhóm cases **rời nhau**, với `m` và `n` possibilities, total:

```math
m+n.
```

Nếu một tiến trình (process / 프로세스) có hai stages, stage 1 có `m` choices và với mỗi choice stage 2 có `n` choices, total:

```math
mn.
```

Sản phẩm (product / 제품) quy tắc (rule / 규칙) là nền của rất nhiều công thức đếm.

Ví dụ password gồm 8 lowercase letters:

```math
26^8
```

possible strings, nếu repetition được phép.

> **Chuyển mạch:** Trong **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **2. Khi nào sản phẩm (product / 제품) quy tắc (rule / 규칙) sai?** tiếp nhận điểm tựa từ **1. quy tắc (rule / 규칙) of sum và quy tắc (rule / 규칙) of sản phẩm (product / 제품)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Permutation: thứ tự (order / 순서) tạo cấu hình (configuration / 구성) mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Khi nào sản phẩm (product / 제품) quy tắc (rule / 규칙) sai?

Sản phẩm (product / 제품) quy tắc (rule / 규칙) không yêu cầu xác suất (probability / 확률) independence, nhưng yêu cầu cấu trúc choice count ở mỗi stage được biết rõ.

Nếu number of choices stage sau phụ thuộc vào stage trước, ta phải cộng theo branches:

```math
\sum_i \text{choices after branch }i.
```

Ví dụ chọn two distinct digits: digit đầu có 10 choices, digit sau chỉ còn 9:

```math
10\cdot9.
```

Không thể dùng `10^2` nếu repetition bị cấm.

> **Chuyển mạch:** Ở chặng này của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **3. Permutation: thứ tự (order / 순서) tạo cấu hình (configuration / 구성) mới** tiếp nhận điểm tựa từ **2. Khi nào sản phẩm (product / 제품) quy tắc (rule / 규칙) sai?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Combination: quotient out thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Permutation: thứ tự (order / 순서) tạo cấu hình (configuration / 구성) mới

Sắp `n` distinct objects:

```math
n!=n(n-1)\cdots1.
```

Chọn và sắp `k` từ `n`:

```math
P(n,k)=\frac{n!}{(n-k)!}.
```

Key question luôn là:

> Đổi thứ tự có tạo kết quả (outcome / 결과) khác không?

Nếu có, permutation-like counting phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **4. Combination: quotient out thứ tự (order / 순서)** tiếp nhận điểm tựa từ **3. Permutation: thứ tự (order / 순서) tạo cấu hình (configuration / 구성) mới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Binomial coefficient như nhiều thứ cùng lúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Combination: quotient out thứ tự (order / 순서)

Nếu thứ tự (order / 순서) không matter, mỗi subset kích thước (size / 크기) `k` bị permutation count lặp `k!` lần, nên:

```math
\binom nk=\frac{n!}{k!(n-k)!}.
```

Combination có symmetry:

```math
\binom nk=\binom n{n-k}.
```

Lý do: chọn `k` phần tử để giữ tương đương chọn `n-k` phần tử để bỏ.

> **Chuyển mạch:** Trong **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **5. Binomial coefficient như nhiều thứ cùng lúc** tiếp nhận điểm tựa từ **4. Combination: quotient out thứ tự (order / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Binomial theorem từ counting choices** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Binomial coefficient như nhiều thứ cùng lúc

`\binom nk` không chỉ là “công thức chọn”. Nó đồng thời là:

```text
number of k-subsets
coefficient trong (a+b)^n
number of binary strings length n có exactly k ones
number of paths với k moves theo một direction
```

Connections này rất quan trọng vì cùng một cấu trúc (structure / 구조) xuất hiện dưới nhiều representations.

> **Chuyển mạch:** Ở chặng này của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **6. Binomial theorem từ counting choices** tiếp nhận điểm tựa từ **5. Binomial coefficient như nhiều thứ cùng lúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Pascal định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Binomial theorem từ counting choices

Trong:

```math
(a+b)^n,
```

mỗi factor đóng góp `a` hoặc `b`.

Muốn term chứa `b^k`, ta chọn `k` trong `n` factors lấy `b`:

```math
(a+b)^n=
\sum_{k=0}^n
\binom nk a^{n-k}b^k.
```

Coefficient không xuất hiện magic; nó đếm số ways tạo cùng monomial.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **7. Pascal định danh (identity / 식별자)** tiếp nhận điểm tựa từ **6. Binomial theorem từ counting choices** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Stars and bars** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Pascal định danh (identity / 식별자)

Pascal identity cho thấy tổ hợp có thể được xây đệ quy từ hai trường hợp nhỏ hơn. Nó là cầu nối giữa counting, recurrence và hệ số trong khai triển nhị thức.

```math
\binom nk
=
\binom{n-1}{k}
+
\binom{n-1}{k-1}.
```

Proof idea: chọn `k` từ `n` objects. Fix một đối tượng (object / 객체) đặc biệt.

Cases:

```text
không chọn object đó → C(n-1,k)
chọn object đó → C(n-1,k-1)
```

Hai cases rời nhau và cover toàn bộ possibilities.

Đây là classic combinatorial proof: chứng minh định danh (identity / 식별자) bằng cách đếm cùng một set theo hai cách.

> **Chuyển mạch:** Trong **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **8. Stars and bars** tiếp nhận điểm tựa từ **7. Pascal định danh (identity / 식별자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Inclusion–exclusion: sửa double counting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Stars and bars

Số nonnegative integer solutions của:

```math
x_1+\cdots+x_k=n
```

là:

```math
\binom{n+k-1}{k-1}.
```

Ta encode `n` identical items bằng stars và `k-1` separators bằng bars.

Ví dụ:

```text
***|*||**
```

có thể encode phân phối (distribution / 분포) `(3,1,0,2)`.

Giả định (assumption / 가정) quan trọng: items identical, boxes distinguishable, values nonnegative.

Nếu các ràng buộc (constraints / 제약조건들) đổi, formula cũng đổi.

> **Chuyển mạch:** Ở chặng này của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **9. Inclusion–exclusion: sửa double counting** tiếp nhận điểm tựa từ **8. Stars and bars** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Complement counting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Inclusion–exclusion: sửa double counting

Hai sets:

```math
|A\cup B|
=|A|+|B|-|A\cap B|.
```

Ba sets:

```math
|A\cup B\cup C|
=
|A|+|B|+|C|
-|A\cap B|-|A\cap C|-|B\cap C|
+|A\cap B\cap C|.
```

Mẫu (pattern / 패턴) alternating signs vì intersections bị đếm thừa nhiều lần.

Inclusion–exclusion là một thành phần nguyên thủy (primitive / 기본 요소) rất quan trọng trong xác suất (probability / 확률) và discrete mathematics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **10. Complement counting** tiếp nhận điểm tựa từ **9. Inclusion–exclusion: sửa double counting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Pigeonhole principle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Complement counting

Nhiều bài dễ hơn nếu đếm complement trước.

Birthday collision:

```math
P(\text{at least one collision})
=1-P(\text{no collision}).
```

Với `n` people, idealized 365 equally likely birthdays:

```math
P(\text{no collision})
=
\frac{365}{365}
\frac{364}{365}
\cdots
\frac{365-n+1}{365}.
```

Complement chiến lược (strategy / 전략) là mẫu (pattern / 패턴) general: “at least one” thường dễ xử lý qua “none”.

> **Chuyển mạch:** Trong **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **11. Pigeonhole principle** tiếp nhận điểm tựa từ **10. Complement counting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Bijection proof** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Pigeonhole principle

Nếu nhiều hơn `n` objects được map vào `n` boxes, ít nhất một box nhận ≥2 objects.

Generalized form: `N` objects vào `k` boxes ⇒ có box chứa ít nhất

```math
\left\lceil\frac Nk\right\rceil
```

objects.

Trong hashing, collision là unavoidable nếu key không gian (space / 공간) lớn hơn bucket không gian (space / 공간). Good băm (hash / 해시) chỉ phân bố collisions tốt hơn; không loại được định lý.

> **Chuyển mạch:** Ở chặng này của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **12. Bijection proof** tiếp nhận điểm tựa từ **11. Pigeonhole principle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Recurrence trong counting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Bijection proof

Một technique mạnh là tìm bijection giữa hai sets để chứng minh chúng có cùng cardinality.

Ví dụ `k`-subsets của `n` objects biject với `(n-k)`-subsets bằng complement map.

Bijection không chỉ chứng minh count; nó giải thích **vì sao** hai quantities giống nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **13. Recurrence trong counting** tiếp nhận điểm tựa từ **12. Bijection proof** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Generating functions intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Recurrence trong counting

Nhiều counting sequences thỏa recurrence.

Ví dụ nhị phân (binary / 이진) strings length `n` không chứa consecutive `1` có count liên hệ Fibonacci.

Lập luận (reasoning / 추론): split theo last bit.

```text
ends in 0 → previous n-1 bits valid
ends in 1 → previous bit phải 0 → reduce về n-2
```

Do đó:

```math
a_n=a_{n-1}+a_{n-2}.
```

Combinatorics và recurrence/DP gặp nhau ở đây.

> **Chuyển mạch:** Trong **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **14. Generating functions intuition** tiếp nhận điểm tựa từ **13. Recurrence trong counting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Asymptotic counting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Generating functions intuition

Nếu chuỗi (sequence / 시퀀스) counts là `a_n`, generating hàm (function / 함수):

```math
A(x)=\sum_{n\ge0}a_nx^n.
```

Nó encode whole count chuỗi (sequence / 시퀀스) vào một algebraic đối tượng (object / 객체).

Operations trên generating functions có thể transform recurrence thành algebra. Đây là advanced cầu nối (bridge / 브리지) giữa combinatorics, power series và thuật toán (algorithm / 알고리즘) phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **15. Asymptotic counting** tiếp nhận điểm tựa từ **14. Generating functions intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Search-space explosion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Asymptotic counting

Chính xác (exact / 정확한) count không phải lúc nào cần thiết. Với large `n`, growth lớp (class / 클래스) thường quan trọng hơn.

Ví dụ:

```math
n!\gg c^n\gg n^k
```

cho fixed `c>1`, `k`.

Stirling approximation:

```math
n!\approx\sqrt{2\pi n}\left(\frac ne\right)^n.
```

Nó cho logarithm của factorial gần:

```math
\log n!\approx n\log n-n.
```

Điều này xuất hiện trong entropy, counting states và độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **16. Search-space explosion** tiếp nhận điểm tựa từ **15. Asymptotic counting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Counting và xác suất (probability / 확률)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Search-space explosion

`n` independent nhị phân (binary / 이진) decisions tạo:

```math
2^n
```

subsets.

Permutation tìm kiếm (search / 검색) tạo:

```math
n!
```

possibilities.

Đây là lý do brute force nhanh chóng bất khả thi. độ phức tạp (complexity / 복잡도) thường bắt đầu từ combinatorial count của tìm kiếm (search / 검색) không gian (space / 공간).

> **Chuyển mạch:** Trong **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **17. Counting và xác suất (probability / 확률)** tiếp nhận điểm tựa từ **16. Search-space explosion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Hypergeometric vs binomial liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Counting và xác suất (probability / 확률)

Khi outcomes equally likely:

```math
P(A)=\frac{|A|}{|\Omega|}.
```

Nhưng combinatorics chỉ cung cấp counts. giả định (assumption / 가정) equally likely phải đến từ xác suất (probability / 확률) mô hình (model / 모델).

Sai lầm phổ biến là đếm đúng nhưng mô hình (model / 모델) xác suất sai.

> **Chuyển mạch:** Ở chặng này của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, sau nội dung của **17. Counting và xác suất (probability / 확률)**, **18. Hypergeometric vs binomial liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **19. Worked example: committee ràng buộc (constraint / 제약조건)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Hypergeometric vs binomial liên kết (connection / 연결)

Sampling **without replacement** tạo dependence.

Nếu population có `K` successes trong `N`, draw `n` without replacement, số successes `X` có hypergeometric xác suất (probability / 확률):

```math
P(X=k)
=
\frac{\binom Kk\binom{N-K}{n-k}}
{\binom Nn}.
```

Binomial phù hợp hơn khi trials independent với constant success xác suất (probability / 확률).

Combinatorial cấu trúc (structure / 구조) giúp thấy giả định (assumption / 가정) difference ngay lập tức.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **18. Hypergeometric vs binomial liên kết (connection / 연결)** cho ta quy tắc; **19. Worked example: committee ràng buộc (constraint / 제약조건)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **20. AI, coding và combinatorics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Worked example: committee ràng buộc (constraint / 제약조건)

Có 6 engineers và 4 designers. Chọn committee 4 người có ít nhất 1 designer.

Total committees:

```math
\binom{10}{4}=210.
```

Committees không có designer:

```math
\binom64=15.
```

Vậy valid:

```math
210-15=195.
```

Complement counting đơn giản hơn sum cases theo number designers.

> **Chuyển mạch:** Trong **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **19. Worked example: committee ràng buộc (constraint / 제약조건)** cho ta quy tắc; **20. AI, coding và combinatorics** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. AI, coding và combinatorics

Tính năng (feature / 기능) subset selection có `2^d` subsets. chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) có vocabulary `V` và length `n` tạo raw string không gian (space / 공간) kích thước (size / 크기) `V^n`. Error-correcting codes chọn codewords trong Hamming không gian (space / 공간) với distance các ràng buộc (constraints / 제약조건들).

Trong AI, combinatorial explosion giải thích vì sao tìm kiếm (search / 검색) cần heuristics, động (dynamic / 동적) programming, branch-and-bound hoặc approximation.

> **Chuyển mạch:** Ở chặng này của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **20. AI, coding và combinatorics** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Combinatorics là algebra của finite possibility spaces. sản phẩm (product / 제품) quy tắc (rule / 규칙) tạo choices; symmetry loại overcount; inclusion–exclusion sửa overlap; bijection giải thích equal counts; asymptotics cho biết không gian (space / 공간) lớn nhanh đến mức nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đếm và tổ hợp: cấu trúc của không gian khả năng**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

Permutation và combination khác ở việc thứ tự (order / 순서) có meaning hay không. Counting sản phẩm (product / 제품) quy tắc (rule / 규칙) không phải xác suất (probability / 확률) independence. `n!` và `2^n` đều “lớn” nhưng growth rất khác. Đếm favorable/total chỉ cho xác suất (probability / 확률) khi outcomes thực sự equiprobable theo mô hình (model / 모델).

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
