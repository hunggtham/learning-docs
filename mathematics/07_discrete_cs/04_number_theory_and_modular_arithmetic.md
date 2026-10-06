# Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Divisibility là structural quan hệ (relation / 관계)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Division thuật toán (algorithm / 알고리즘)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối number theory với modular arithmetic, để nhận ra cấu trúc chia dư đứng sau thuật toán, mật mã và kiểm tra tính chất số.

Lý thuyết số (number theory / 정수론) nghiên cứu integers, divisibility và các structures sinh ra từ arithmetic rời rạc. Đây là một lĩnh vực cho thấy rất rõ cách một concept “thuần toán” có thể trở thành nền của algorithms, hashing, cyclic các hệ thống (systems / 시스템들), lỗi (error / 오류) checking và cryptographic mathematics.

Mục tiêu của chapter này không phải nhớ các theorem riêng lẻ, mà hiểu một mạch học (learning flow / 학습 흐름):

```text
integer structure
→ divisibility
→ gcd / Euclidean algorithm
→ primes
→ congruence classes
→ modular inverses
→ finite algebraic systems
→ efficient computation
```

## 1. Divisibility là structural quan hệ (relation / 관계)

Với integers `a,b`, ta viết

```math
a\mid b
```

nếu tồn tại integer `k` sao cho

```math
b=ak.
```

Definition này mạnh hơn “chia ra được số nguyên” vì nó cho phép proof algebraic trực tiếp.

Ví dụ nếu

```math
a\mid b
\quad\text{và}\quad
a\mid c,
```

thì tồn tại `m,n` với

```math
b=am,\qquad c=an.
```

Do đó với integers `r,s`:

```math
rb+sc=a(rm+sn),
```

nên

```math
a\mid(rb+sc).
```

Đây là nguồn (source / 소스) của rất nhiều arguments về gcd và congruence.

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **2. Division thuật toán (algorithm / 알고리즘)** nối từ **1. Divisibility là structural quan hệ (relation / 관계)** sang **3. GCD là greatest dùng chung (common / 공통) cấu trúc (structure / 구조)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Division thuật toán (algorithm / 알고리즘)

Với integer `a` và positive integer `n`, tồn tại duy nhất integers `q,r` sao cho

```math
a=qn+r,
\qquad 0\le r<n.
```

`q` là quotient, `r` remainder.

Đây là theorem formal hóa intuition “chia lấy phần nguyên và phần dư”.

Nó là nền của Euclidean thuật toán (algorithm / 알고리즘) và modular arithmetic.

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **3. GCD là greatest dùng chung (common / 공통) cấu trúc (structure / 구조)** nối từ **2. Division thuật toán (algorithm / 알고리즘)** sang **4. Euclidean thuật toán (algorithm / 알고리즘): vì sao thay (a,b) bằng (b,r) được?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. GCD là greatest dùng chung (common / 공통) cấu trúc (structure / 구조)

Greatest dùng chung (common / 공통) divisor:

```math
\gcd(a,b)
```

là positive integer lớn nhất chia cả `a` và `b`.

Ví dụ:

```math
\gcd(84,30)=6.
```

Nhưng definition “largest dùng chung (shared / 공유) factor” chưa cho thuật toán (algorithm / 알고리즘) hiệu quả. Euclid tìm cấu trúc (structure / 구조) sâu hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **4. Euclidean thuật toán (algorithm / 알고리즘): vì sao thay (a,b) bằng (b,r) được?** nối từ **3. GCD là greatest dùng chung (common / 공통) cấu trúc (structure / 구조)** sang **5. Termination và algorithmic lập luận (reasoning / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Euclidean thuật toán (algorithm / 알고리즘): vì sao thay `(a,b)` bằng `(b,r)` được?

Viết

```math
a=qb+r.
```

Một number `d` chia cả `a,b` iff nó chia cả `b,r` vì

```math
r=a-qb.
```

Do đó:

```math
\gcd(a,b)=\gcd(b,r).
```

Lặp tiến trình (process / 프로세스) làm second argument giảm:

```text
252 = 105·2 + 42
105 = 42·2 + 21
42  = 21·2 + 0
```

nên

```math
\gcd(252,105)=21.
```

Điểm quan trọng là mỗi step không “đoán” gcd; nó thay bài toán (problem / 문제) bằng equivalent smaller bài toán (problem / 문제).

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **5. Termination và algorithmic lập luận (reasoning / 추론)** nối từ **4. Euclidean thuật toán (algorithm / 알고리즘): vì sao thay (a,b) bằng (b,r) được?** sang **6. Bézout định danh (identity / 식별자)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Termination và algorithmic lập luận (reasoning / 추론)

Remainder luôn thỏa

```math
0\le r<b.
```

nên chuỗi (sequence / 시퀀스) remainders là decreasing nonnegative integers. Nó không thể giảm vô hạn, nên thuật toán (algorithm / 알고리즘) terminate.

Đây là ví dụ number lý thuyết (theory / 이론) nối trực tiếp với proof of termination trong algorithms.

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **6. Bézout định danh (identity / 식별자)** nối từ **5. Termination và algorithmic lập luận (reasoning / 추론)** sang **7. Prime numbers là atoms của multiplication**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Bézout định danh (identity / 식별자)

Có integers `x,y` sao cho

```math
ax+by=\gcd(a,b).
```

Extended Euclidean thuật toán (algorithm / 알고리즘) không chỉ tìm gcd; nó tìm luôn coefficients `x,y`.

Ví dụ với `30,18`:

```math
\gcd(30,18)=6.
```

Ta có thể tìm:

```math
6=2(18)-1(30).
```

Bézout định danh (identity / 식별자) là cầu nối (bridge / 브리지) trực tiếp tới modular inverse.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **7. Prime numbers là atoms của multiplication** nối từ **6. Bézout định danh (identity / 식별자)** sang **8. GCD/LCM từ prime exponents**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Prime numbers là atoms của multiplication

Prime (số nguyên tố / 소수) là integer >1 chỉ có positive divisors `1` và chính nó.

Composite numbers có factorization thành smaller integers.

Fundamental Theorem of Arithmetic nói mọi integer `n>1` có prime factorization duy nhất up to thứ tự (order / 순서):

```math
n=p_1^{a_1}\cdots p_k^{a_k}.
```

Prime factorization đóng vai trò như “coordinate hệ thống (system / 시스템)” cho multiplicative cấu trúc (structure / 구조) của positive integers.

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **8. GCD/LCM từ prime exponents** nối từ **7. Prime numbers là atoms của multiplication** sang **9. Infinitely many primes: proof idea**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. GCD/LCM từ prime exponents

Nếu

```math
n=\prod p_i^{a_i},
\qquad
m=\prod p_i^{b_i},
```

thì

```math
\gcd(n,m)=\prod p_i^{\min(a_i,b_i)}
```

và

```math
\operatorname{lcm}(n,m)=\prod p_i^{\max(a_i,b_i)}.
```

Điều này giải thích vì sao:

```math
\gcd(n,m)\operatorname{lcm}(n,m)=|nm|.
```

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **9. Infinitely many primes: proof idea** nối từ **8. GCD/LCM từ prime exponents** sang **10. Congruence modulo n**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Infinitely many primes: proof idea

Giả sử chỉ có finitely many primes:

```text
p1,p2,...,pk.
```

Xét

```math
N=p_1p_2\cdots p_k+1.
```

Không `p_i` nào chia `N` vì remainder là 1. Nhưng `N>1` phải có prime divisor. Contradiction.

Điểm đáng học không chỉ theorem mà là proof chiến lược (strategy / 전략): bản dựng (build / 빌드) đối tượng (object / 객체) cố tình nằm ngoài assumed complete danh sách (list / 목록).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **10. Congruence modulo n** nối từ **9. Infinitely many primes: proof idea** sang **11. Modular arithmetic không chỉ là %**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Congruence modulo n

Ta viết

```math
a\equiv b\pmod n
```

nếu

```math
n\mid(a-b).
```

Equivalent interpretation: `a` và `b` cùng remainder khi chia cho `n`.

Ví dụ:

```math
17\equiv5\pmod{12}.
```

Congruence là một equivalence quan hệ (relation / 관계) trên integers.

Nó partition `\mathbb Z` thành remainder classes:

```math
[0],[1],\ldots,[n-1].
```

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **11. Modular arithmetic không chỉ là %** nối từ **10. Congruence modulo n** sang **12. Addition và multiplication descend xuống residue classes**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Modular arithmetic không chỉ là `%`

Operator `%` trong programming trả remainder theo language-specific convention.

Mathematical modulo arithmetic nói về equivalence classes.

Hai statements khác nhau:

```text
-1 % 5  // implementation/language semantics
```

và

```math
-1\equiv4\pmod5.
```

Trong mathematics, lớp (class / 클래스) của `-1` và `4` là cùng lớp (class / 클래스) modulo 5.

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **12. Addition và multiplication descend xuống residue classes** nối từ **11. Modular arithmetic không chỉ là %** sang **13. Modular inverse**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Addition và multiplication descend xuống residue classes

Nếu

```math
a\equiv b\pmod n
```

và

```math
c\equiv d\pmod n,
```

thì

```math
a+c\equiv b+d\pmod n
```

và

```math
ac\equiv bd\pmod n.
```

Proof đến từ divisibility của differences.

Điều này làm arithmetic trên residue classes well-defined.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **13. Modular inverse** nối từ **12. Addition và multiplication descend xuống residue classes** sang **14. Worked Example: inverse của 7 modulo 26**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Modular inverse

Ta muốn `x` sao cho

```math
ax\equiv1\pmod n.
```

Điều này equivalent tồn tại integer `k`:

```math
ax-kn=1.
```

Theo Bézout, solution tồn tại iff

```math
\gcd(a,n)=1.
```

Vì vậy coprimality là điều kiện (condition / 조건) chính xác cho invertibility modulo `n`.

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **13. Modular inverse** nêu quy tắc; **14. Worked Example: inverse của 7 modulo 26** thử quy tắc trong tình huống, rồi **15. Modular division không giống ordinary division** mở rộng hệ quả.

## 14. Worked Example: inverse của 7 modulo 26

Euclidean thuật toán (algorithm / 알고리즘):

```text
26 = 7·3 + 5
7  = 5·1 + 2
5  = 2·2 + 1
```

Back substitute:

```math
1=5-2\cdot2
```

```math
=5-2(7-5)
=3\cdot5-2\cdot7
```

```math
=3(26-3\cdot7)-2\cdot7
=3\cdot26-11\cdot7.
```

Do đó:

```math
-11\cdot7\equiv1\pmod{26}
```

nên inverse của 7 modulo 26 là

```math
15
```

vì `-11≡15 mod 26`.

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **14. Worked Example: inverse của 7 modulo 26** nêu quy tắc; **15. Modular division không giống ordinary division** thử quy tắc trong tình huống, rồi **16. Fermat's little theorem** mở rộng hệ quả.

## 15. Modular division không giống ordinary division

Expression

```math
\frac ab\pmod n
```

chỉ meaningful nếu `b` có inverse modulo `n`.

Ví dụ modulo 6, `2` không invertible vì

```math
\gcd(2,6)=2\ne1.
```

Không thể “chia hai vế cho 2” modulo 6 như trên real numbers mà không kiểm tra cấu trúc (structure / 구조).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **16. Fermat's little theorem** nối từ **15. Modular division không giống ordinary division** sang **17. Euler's theorem**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Fermat's little theorem

Nếu `p` prime và

```math
p\nmid a,
```

thì

```math
a^{p-1}\equiv1\pmod p.
```

Một proof idea xem multiplication by `a` permute nonzero residue classes modulo `p` vì `a` invertible.

Sản phẩm (product / 제품) của classes `1,...,p-1` sau permutation vẫn same modulo `p`, dẫn tới theorem.

Điểm sâu là theorem đến từ symmetry/permutation cấu trúc (structure / 구조) của invertible residues.

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **17. Euler's theorem** nối từ **16. Fermat's little theorem** sang **18. Fast modular exponentiation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Euler's theorem

Nếu

```math
\gcd(a,n)=1,
```

thì

```math
a^{\varphi(n)}\equiv1\pmod n,
```

trong đó `\varphi(n)` là Euler totient: số residue classes modulo `n` coprime với `n`.

Fermat là special trường hợp (case / 사례) khi `n=p` prime, vì

```math
\varphi(p)=p-1.
```

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **18. Fast modular exponentiation** nối từ **17. Euler's theorem** sang **19. Chinese Remainder Theorem intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Fast modular exponentiation

Muốn tính

```math
a^k\bmod n
```

không cần compute giant integer `a^k` trước.

Repeated squaring dùng nhị phân (binary / 이진) decomposition của exponent.

Ví dụ `k=13=8+4+1`:

```text
a^1
→ square: a^2
→ square: a^4
→ square: a^8
```

combine needed powers, reducing modulo `n` mỗi step.

Độ phức tạp (complexity / 복잡도) theo number of exponent bits, roughly `O(log k)` multiplications.

Đây là liên kết (connection / 연결) trực tiếp number lý thuyết (theory / 이론) ↔ thuật toán (algorithm / 알고리즘) độ phức tạp (complexity / 복잡도).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **19. Chinese Remainder Theorem intuition** nối từ **18. Fast modular exponentiation** sang **20. Cyclic các hệ thống (systems / 시스템들) trong software**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Chinese Remainder Theorem intuition

Nếu moduli `m,n` coprime, pair of remainders:

```math
x\bmod m,
\qquad x\bmod n
```

xác định unique residue modulo `mn`.

Conceptually, một large cyclic trạng thái (state / 상태) có thể decomposed thành independent smaller cyclic coordinates khi moduli coprime.

CRT là một “thay đổi (change / 변경) of coordinates” cho modular arithmetic.

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **20. Cyclic các hệ thống (systems / 시스템들) trong software** nối từ **19. Chinese Remainder Theorem intuition** sang **21. bảng băm (hash table / 해시 테이블) liên kết (connection / 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Cyclic các hệ thống (systems / 시스템들) trong software

Modulo xuất hiện tự nhiên khi trạng thái (state / 상태) wraps around:

```text
clock hours
weekdays
ring buffers
circular array index
sequence counters
sharding buckets
```

Nhưng wraparound integer trong hardware không luôn equivalent với intended mathematical modulo, đặc biệt khi signed overflow ngữ nghĩa (semantics / 의미론) khác ngôn ngữ (language / 언어).

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, sau nội dung của **20. Cyclic các hệ thống (systems / 시스템들) trong software**, **21. bảng băm (hash table / 해시 테이블) liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **22. lỗi (error / 오류) detection và check digits** mở rộng hệ quả hoặc giới hạn liên quan.

## 21. bảng băm (hash table / 해시 테이블) liên kết (connection / 연결)

Bảng băm (hash table / 해시 테이블) thường dùng ánh xạ (mapping / 매핑):

```math
bucket=h(key)\bmod m.
```

Modulo chỉ compress phạm vi (range / 범위). Nó không tự tạo good phân phối (distribution / 분포).

Nếu upstream băm (hash / 해시) có patterns align với `m`, collisions có thể cao.

Do đó number-theoretic cấu trúc (structure / 구조) của bảng (table / 테이블) kích thước (size / 크기) đôi khi matter, nhưng hiện đại (modern / 현대적) hash-table thiết kế (design / 설계) còn phụ thuộc tải (load / 로드) factor, mixing hàm (function / 함수) và collision chiến lược (strategy / 전략).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **22. lỗi (error / 오류) detection và check digits** nối từ **21. bảng băm (hash table / 해시 테이블) liên kết (connection / 연결)** sang **23. Finite fields: khi residue arithmetic trở thành trường dữ liệu (field / 필드)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. lỗi (error / 오류) detection và check digits

Checksum/check-digit các hệ thống (systems / 시스템들) thường dùng modular các ràng buộc (constraints / 제약조건들).

Ví dụ simple digit sum modulo 10 có thể detect một số errors nhưng không phải tất cả transpositions.

Thiết kế (design / 설계) tốt cần analyze lỗi (error / 오류) mô hình (model / 모델) và algebraic mã (code / 코드) cấu trúc (structure / 구조).

Number lý thuyết (theory / 이론) cung cấp bất biến (invariant / 불변식); độ tin cậy (reliability / 신뢰성) phụ thuộc bất biến (invariant / 불변식) detect được loại perturbation nào.

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **22. lỗi (error / 오류) detection và check digits** đặt vấn đề; **23. Finite fields: khi residue arithmetic trở thành trường dữ liệu (field / 필드)** đối chiếu bằng chứng, rồi **24. liên kết (connection / 연결) với cryptographic mathematics** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. Finite fields: khi residue arithmetic trở thành trường dữ liệu (field / 필드)

Modulo prime `p`, nonzero residue classes đều invertible. Vì vậy

```math
\mathbb F_p
```

là trường dữ liệu (field / 필드).

Modulo composite `n`, zero divisors có thể xuất hiện. Ví dụ modulo 6:

```math
2\cdot3\equiv0\pmod6
```

mặc dù neither factor congruent 0.

Do đó `\mathbb Z/6\mathbb Z` không phải trường dữ liệu (field / 필드).

Đây là cầu nối (bridge / 브리지) sang algebraic structures.

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **23. Finite fields: khi residue arithmetic trở thành trường dữ liệu (field / 필드)** đặt vấn đề; **24. liên kết (connection / 연결) với cryptographic mathematics** đối chiếu bằng chứng, rồi **25. liên kết (connection / 연결) với Fourier và cyclic cấu trúc (structure / 구조)** mở rộng hệ quả hoặc giới hạn liên quan.

## 24. liên kết (connection / 연결) với cryptographic mathematics

Modular exponentiation, finite groups và finite fields xuất hiện trong nhiều cryptographic constructions.

Nhưng một theorem number lý thuyết (theory / 이론) đúng không tự đảm bảo hệ thống (system / 시스템) secure. Practical thiết kế (design / 설계) còn phụ thuộc giao thức (protocol / 프로토콜), parameter kích thước (size / 크기), randomness, hiện thực (implementation / 구현), side-channel resistance và threat mô hình (model / 모델).

Ở đây mục tiêu chỉ là hiểu mathematical substrate, không đồng nhất “có prime/modulo” với bảo mật (security / 보안).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **25. liên kết (connection / 연결) với Fourier và cyclic cấu trúc (structure / 구조)** nối từ **24. liên kết (connection / 연결) với cryptographic mathematics** sang **26. Worked Example: weekday arithmetic**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. liên kết (connection / 연결) với Fourier và cyclic cấu trúc (structure / 구조)

Discrete Fourier Transform làm việc với periodic/cyclic indexing. Roots of unity là solutions của

```math
z^n=1
```

trong complex numbers.

Finite cyclic structures và modular indexing vì vậy xuất hiện song song trong tín hiệu (signal / 신호) processing và number-theoretic transforms.

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **25. liên kết (connection / 연결) với Fourier và cyclic cấu trúc (structure / 구조)** nêu quy tắc; **26. Worked Example: weekday arithmetic** thử quy tắc trong tình huống, rồi **27. Proof chiến lược (strategy / 전략): công việc (work / 작업) modulo small cơ sở (base / 기반) để tìm impossibility** mở rộng hệ quả.

## 26. Worked Example: weekday arithmetic

Nếu Monday encode `0`, Tuesday `1`, ..., Sunday `6`, thì 100 days after Monday:

```math
100\equiv2\pmod7.
```

nên day là Wednesday.

Ta không cần enumerate 100 steps; modulo giữ lại đúng thông tin (information / 정보) relevant cho periodic trạng thái (state / 상태).

> **Nối mạch:** Ở chặng này của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **26. Worked Example: weekday arithmetic** nêu quy tắc; **27. Proof chiến lược (strategy / 전략): công việc (work / 작업) modulo small cơ sở (base / 기반) để tìm impossibility** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## 27. Proof chiến lược (strategy / 전략): công việc (work / 작업) modulo small cơ sở (base / 기반) để tìm impossibility

Suppose muốn chứng minh square integer không thể congruent 2 modulo 4.

Mọi integer là even hoặc odd.

Nếu `n=2k`:

```math
n^2=4k^2\equiv0\pmod4.
```

Nếu `n=2k+1`:

```math
n^2=4k^2+4k+1\equiv1\pmod4.
```

Vậy square chỉ remainder 0 hoặc 1 modulo 4, không thể 2.

Đây là proof technique rất mạnh: quotient infinite integer bài toán (problem / 문제) xuống finite residue classes.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **27. Proof chiến lược (strategy / 전략): công việc (work / 작업) modulo small cơ sở (base / 기반) để tìm impossibility** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Number lý thuyết (theory / 이론) nghiên cứu cấu trúc (structure / 구조) của integers dưới divisibility và multiplication. Modular arithmetic quotient infinite integers thành finite equivalence classes nhưng giữ đủ arithmetic cấu trúc (structure / 구조) để tính toán. GCD, inverse, prime factorization và congruence không phải tricks riêng lẻ; chúng là các mặt của cùng cấu trúc divisibility.

> **Nối mạch:** Trong **Lý thuyết số và số học modulo: cấu trúc của integers và computation rời rạc**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“Modulo chỉ là remainder operator `%`.”** Không; mathematical modulo là equivalence quan hệ (relation / 관계)/lớp (class / 클래스) cấu trúc (structure / 구조).

**“Có thể chia modulo như ordinary arithmetic.”** Chỉ khi divisor invertible.

**“Prime factorization dễ vì theorem bảo tồn tại.”** Existence/uniqueness không nói factoring computationally cheap.

**“Fermat theorem áp cho mọi `a,p`.”** Cần conditions.

**“Modulo tự tạo băm (hash / 해시) phân phối (distribution / 분포) tốt.”** Không; upstream hashing và bảng (table / 테이블) thiết kế (design / 설계) vẫn quyết định.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
