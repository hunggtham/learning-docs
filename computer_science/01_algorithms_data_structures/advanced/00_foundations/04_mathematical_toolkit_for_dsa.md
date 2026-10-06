# Công cụ toán học cho cấu trúc dữ liệu và thuật toán

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Công cụ toán học cho cấu trúc dữ liệu và thuật toán**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Logarithm: số lần thu nhỏ theo tỷ lệ cố định** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Lũy thừa của hai và biểu diễn nhị phân** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối mathematical toolkit với algebra, counting, probability và proof, để DSA có nền tảng suy luận nhất quán.

**Mathematical Toolkit for DSA / 알고리즘을 위한 수학 도구**

DSA không yêu cầu toàn bộ toán cao cấp, nhưng liên tục sử dụng một số ý tưởng toán học: logarithm, tổng hữu hạn, truy hồi, tổ hợp, số học modulo, xác suất, kỳ vọng, quy nạp, đại số của phép gộp, đếm trên đồ thị và cận dưới. Mục tiêu của chương này không phải biến DSA thành môn toán thuần túy, mà giúp nhìn thấy **vì sao độ phức tạp và tính đúng đắn có hình dạng như vậy**.

Khi gặp một công thức, câu hỏi quan trọng nhất là: **công thức này đang mô tả cấu trúc nào của quá trình tính toán?** Nếu ký hiệu không gắn được với hành vi của thuật toán, công thức vẫn chỉ là thứ để học thuộc.

## Logarithm: số lần thu nhỏ theo tỷ lệ cố định

Nếu không gian tìm kiếm kích thước `n` và mỗi bước giữ lại một nửa:

\[
\frac{n}{2^k}\approx 1
\]

suy ra:

\[
k\approx \log_2 n
\]

Đây là nguồn gốc của `O(log n)` trong tìm kiếm nhị phân (binary search / 이진 탐색), balanced BST, vùng nhớ động (heap / 힙), nhị phân (binary / 이진) lifting và nhiều thuật toán divide-and-conquer.

Cơ số logarithm không quan trọng trong Big-O vì:

\[
\log_a n = \frac{\log_b n}{\log_b a}
\]

hai logarithm khác cơ số chỉ khác một hệ số hằng. Nhưng ở cấp hệ thống, cơ số vẫn có ý nghĩa. B+cây (tree / 트리) có chiều cao gần `log_B n` với `B` lớn vì mỗi page chứa nhiều khóa, nên số lần I/O giảm mạnh.

Mô hình tư duy:

> `log n` thường xuất hiện khi mỗi bước loại bỏ hoặc gom lại một tỷ lệ cố định của phần còn lại.

> **Nối mạch:** **Lũy thừa của hai và biểu diễn nhị phân** nối từ **Logarithm: số lần thu nhỏ theo tỷ lệ cố định** sang **Tổng số học và vòng lặp lồng nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lũy thừa của hai và biểu diễn nhị phân

Chuỗi:

```text
1, 2, 4, 8, 16, ...
```

xuất hiện khắp DSA vì doubling/halving và biểu diễn bit rất tự nhiên với máy tính.

Nếu:

\[
2^k \le n < 2^{k+1}
\]

thì:

\[
k=\lfloor \log_2 n \rfloor
\]

Sparse bảng (table / 테이블) lưu khối (block / 블록) độ dài `2^k`. nhị phân (binary / 이진) Lifting lưu tổ tiên cách `2^k` cạnh. Fenwick cây (tree / 트리) dùng bit 1 thấp nhất để xác định kích thước khối (block / 블록) phụ trách. Exponentiation by squaring phân rã số mũ theo bit.

Một insight quan trọng là nhiều kỹ thuật tưởng khác nhau thực ra cùng dùng ý tưởng: **tiền xử lý các bước có kích thước tăng gấp đôi rồi ghép chúng theo biểu diễn nhị phân của một số nguyên**.

> **Nối mạch:** **Tổng số học và vòng lặp lồng nhau** nối từ **Lũy thừa của hai và biểu diễn nhị phân** sang **Cấp số nhân và phân tích khấu hao**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tổng số học và vòng lặp lồng nhau

Tổng:

\[
1+2+\cdots+n=\frac{n(n+1)}2=\Theta(n^2)
\]

mô tả chính xác vòng lặp:

```c
for (int i = 0; i < n; ++i)
    for (int j = 0; j <= i; ++j)
        work();
```

Thay vì đếm số vòng `for`, nên viết số lần thực thi thật dưới dạng tổng:

\[
T(n)=\sum_{i=1}^{n} f(i)
\]

Điều này đặc biệt quan trọng khi giới hạn vòng trong phụ thuộc `i`, vì “hai vòng lặp” không tự động nghĩa là `O(n²)`.

Ví dụ:

```c
for (int i = 1; i <= n; i *= 2)
    for (int j = 0; j < n; ++j)
        work();
```

vòng ngoài chạy `O(log n)` lần, nên tổng là `O(n log n)`.

> **Nối mạch:** **Cấp số nhân và phân tích khấu hao** nối từ **Tổng số học và vòng lặp lồng nhau** sang **Harmonic series**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp số nhân và phân tích khấu hao

Tổng hình học:

\[
1+2+4+\cdots+2^k=2^{k+1}-1
\]

là nền tảng của nhiều phân tích doubling.

Mảng động tăng sức chứa (capacity / 용량) gấp đôi. Qua `n` lần append, số phần tử bị bản sao (copy / 복사) trong các lần resize xấp xỉ:

\[
1+2+4+\cdots+\frac n2<n
\]

Do đó tổng bản sao (copy / 복사) là `O(n)`, dù một lần append riêng lẻ có thể tốn `O(n)`. Chi phí khấu hao mỗi append vẫn là `O(1)`.

Điểm quan trọng: **amortized** không phải “trung bình theo xác suất”. Nó là bảo đảm về tổng chi phí của một chuỗi thao tác hợp lệ.

> **Nối mạch:** **Harmonic series** nối từ **Cấp số nhân và phân tích khấu hao** sang **Tích và factorial: nhận diện bùng nổ tổ hợp**, vì cơ chế trước tạo đầu vào cho bước sau.

## Harmonic series

Tổng điều hòa:

\[
H_n=1+\frac12+\frac13+\cdots+\frac1n=\Theta(\log n)
\]

xuất hiện trong randomized algorithms, coupon-collector lập luận (reasoning / 추론), một số phân tích hashing và nhiều quá trình xác suất.

Khi thấy tổng nghịch đảo `1/i`, nên nghĩ tới tăng trưởng logarithmic thay vì tuyến tính.

> **Nối mạch:** **Tích và factorial: nhận diện bùng nổ tổ hợp** nối từ **Harmonic series** sang **Công thức truy hồi mô tả cây đệ quy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tích và factorial: nhận diện bùng nổ tổ hợp

Số hoán vị của `n` phần tử phân biệt là:

\[
n!
\]

Và:

\[
n! = n(n-1)(n-2)\cdots 1
\]

Factorial tăng nhanh hơn mọi `c^n` cố định khi `n` đủ lớn. Một brute force duyệt hoán vị chỉ phù hợp với `n` khá nhỏ.

Stirling approximation cho trực giác:

\[
n! \approx \sqrt{2\pi n}\left(\frac ne\right)^n
\]

và do đó:

\[
\log(n!)=\Theta(n\log n)
\]

Kết quả này xuất hiện trực tiếp trong cận dưới của comparison sorting.

> **Nối mạch:** **Công thức truy hồi mô tả cây đệ quy** nối từ **Tích và factorial: nhận diện bùng nổ tổ hợp** sang **Master Theorem và giới hạn của nó**, vì cơ chế trước tạo đầu vào cho bước sau.

## Công thức truy hồi mô tả cây đệ quy

Merge Sort:

\[
T(n)=2T(n/2)+cn
\]

Mỗi tầng của cây đệ quy có tổng công việc `Θ(n)` và có `Θ(log n)` tầng, nên:

\[
T(n)=\Theta(n\log n)
\]

Tìm kiếm nhị phân (binary search / 이진 탐색):

\[
T(n)=T(n/2)+c=\Theta(\log n)
\]

Quicksort trường hợp xấu khi partition cực lệch:

\[
T(n)=T(n-1)+cn=\Theta(n^2)
\]

Truy hồi là bản mô tả toán học của hình dạng recursion cây (tree / 트리). Nếu không hiểu recursion cây (tree / 트리), dùng công thức dễ trở thành thao tác máy móc.

> **Nối mạch:** **Công thức truy hồi mô tả cây đệ quy** đã nêu tiêu chí phân biệt, còn **Master Theorem và giới hạn của nó** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm; **Nguyên lý cộng và nhân trong tổ hợp** mở rộng hệ quả hoặc giới hạn của cơ chế này.

## Master Theorem và giới hạn của nó

Với:

\[
T(n)=aT(n/b)+f(n)
\]

ta so `f(n)` với:

\[
n^{\log_b a}
\]

để xem chi phí chia nhánh hay chi phí xử lý mỗi tầng chi phối.

Master Theorem rất tiện khi subproblem có kích thước cân bằng, nhưng không nên ép vào mọi recurrence. Các dạng như:

\[
T(n)=T(n-1)+n
\]

hoặc subproblem không đều, recurrence phụ thuộc dữ liệu, hay randomized recurrence thường phù hợp hơn với substitution, recursion cây (tree / 트리) hoặc probabilistic phân tích (analysis / 분석).

Bài học: theorem là công cụ cho một lớp cấu trúc, không phải phép biến đổi cú pháp tổng quát.

> **Nối mạch:** **Master Theorem và giới hạn của nó** đã nêu tiêu chí phân biệt, còn **Nguyên lý cộng và nhân trong tổ hợp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm; **Combination và subset** mở rộng hệ quả hoặc giới hạn của cơ chế này.

## Nguyên lý cộng và nhân trong tổ hợp

Nếu bước một có `a` lựa chọn và sau mỗi lựa chọn đó bước hai có `b` lựa chọn độc lập, tổng số đường là:

\[
ab
\]

Nếu hai nhóm lựa chọn loại trừ nhau có `a` và `b` cách, tổng là:

\[
a+b
\]

Cây backtracking thường được ước lượng thô bằng:

\[
O(b^d)
\]

với `b` là branching factor và `d` là độ sâu. Pruning làm branching factor hiệu dụng nhỏ hơn, nhưng không tự thay đổi worst-case nếu vẫn tồn tại đầu vào (input / 입력) buộc duyệt gần toàn cây.

> **Nối mạch:** **Combination và subset** nối từ **Nguyên lý cộng và nhân trong tổ hợp** sang **Pigeonhole principle**, vì cơ chế trước tạo đầu vào cho bước sau.

## Combination và subset

Số cách chọn `r` phần tử từ `n` phần tử:

\[
\binom nr=\frac{n!}{r!(n-r)!}
\]

Tổng số subset của một tập `n` phần tử là:

\[
\sum_{r=0}^{n}\binom nr=2^n
\]

Đây là lý do bitmask trên `n` phần tử tạo không gian `2^n` trạng thái.

Với `n=20`, khoảng một triệu subset còn có thể xử lý trong nhiều bối cảnh. Với `n=40`, hơn một nghìn tỷ subset thường buộc ta dùng meet-in-the-middle hoặc cấu trúc khác.

> **Nối mạch:** **Pigeonhole principle** nối từ **Combination và subset** sang **Inclusion–exclusion**, vì cơ chế trước tạo đầu vào cho bước sau.

## Pigeonhole principle

Nếu đặt nhiều hơn `m` đối tượng vào `m` ngăn, ít nhất một ngăn chứa từ hai đối tượng trở lên.

Trong hashing, miền khóa thường lớn hơn số bucket, nên collision không phải “lỗi hiếm có thể loại bỏ hoàn toàn”; nó là điều toán học không tránh khỏi. Thiết kế đúng phải quản lý collision.

Pigeonhole cũng xuất hiện trong chứng minh duplicate, cycle và nhiều lập luận tồn tại.

> **Nối mạch:** **Inclusion–exclusion** nối từ **Pigeonhole principle** sang **Prefix Sum và cấu trúc đại số phía sau**, vì cơ chế trước tạo đầu vào cho bước sau.

## Inclusion–exclusion

Với hai tập:

\[
|A\cup B|=|A|+|B|-|A\cap B|
\]

Ta phải trừ phần giao vì nó bị đếm hai lần.

Với nhiều tập, các giao được cộng/trừ luân phiên. Ý tưởng này xuất hiện trong combinatorial counting, bitmask DP, xác suất và một số thuật toán đếm với điều kiện loại trừ.

> **Nối mạch:** **Prefix Sum và cấu trúc đại số phía sau** nối từ **Inclusion–exclusion** sang **Semigroup, monoid và group trong DSA**, vì cơ chế trước tạo đầu vào cho bước sau.

## Prefix Sum và cấu trúc đại số phía sau

Định nghĩa:

\[
P[i]=\sum_{j=0}^{i-1}a_j
\]

thì:

\[
sum(L,R)=P[R+1]-P[L]
\]

Điểm sâu hơn không phải công thức, mà là việc phép cộng có **phép nghịch đảo**: contribution của prefix trước `L` có thể bị loại bằng phép trừ.

Điều này giải thích vì sao Prefix Sum làm phạm vi (range / 범위) sum rất tự nhiên, còn prefix minimum không thể “trừ min cũ” để lấy min của một đoạn bất kỳ.

> **Nối mạch:** **Semigroup, monoid và group trong DSA** nối từ **Prefix Sum và cấu trúc đại số phía sau** sang **Commutativity không giống associativity**, vì cơ chế trước tạo đầu vào cho bước sau.

## Semigroup, monoid và group trong DSA

Nhiều cấu trúc phạm vi (range / 범위) truy vấn (query / 쿼리) có thể hiểu bằng đại số.

### Tính kết hợp

Một phép toán `*` có tính kết hợp nếu:

\[
(a*b)*c=a*(b*c)
\]

Khi đó ta có thể chia đoạn thành nhiều khối (block / 블록) rồi ghép kết quả theo bất kỳ cách đặt ngoặc nào. Segment cây (tree / 트리) cần tính chất này.

Một tập cùng phép toán kết hợp tạo thành **semigroup**.

### Phần tử đơn vị

Nếu tồn tại `e` sao cho:

\[
a*e=e*a=a
\]

thì ta có **monoid**.

Ví dụ:

```text
sum -> identity 0
product -> identity 1
min -> identity +∞
max -> identity -∞
```

Định danh (identity / 식별자) rất hữu ích cho đoạn rỗng và accumulator ban đầu.

### Phép nghịch đảo

Nếu mỗi phần tử có inverse phù hợp, monoid trở thành group. Prefix Sum hưởng lợi từ inverse của phép cộng:

\[
a+(-a)=0
\]

Fenwick cây (tree / 트리) cho phạm vi (range / 범위) sum rất tự nhiên vì prefix aggregate có thể “trừ” nhau.

### Idempotence

Một phép toán idempotent nếu:

\[
f(x,x)=x
\]

`min`, `max`, `gcd`, bitwise AND/OR có tính chất này. Classic Sparse bảng (table / 테이블) có thể trả RMQ bằng hai khối (block / 블록) chồng lấn vì phần giao bị tính hai lần nhưng không thay kết quả.

Nhìn bằng đại số giúp trả lời câu hỏi “cấu trúc này có tổng quát sang thao tác (operation / 연산) khác không?” chính xác hơn việc học thuộc danh sách.

> **Nối mạch:** **Commutativity không giống associativity** nối từ **Semigroup, monoid và group trong DSA** sang **Số học modulo**, vì cơ chế trước tạo đầu vào cho bước sau.

## Commutativity không giống associativity

**Giao hoán (commutativity)**:

\[
a*b=b*a
\]

không bắt buộc cho mọi cấu trúc. Segment cây (tree / 트리) có thể làm việc với phép kết hợp không giao hoán, miễn ta giữ đúng thứ tự trái–phải.

Ví dụ nối chuỗi là associative nhưng không commutative:

```text
"ab" + "cd" != "cd" + "ab"
```

Phân biệt hai tính chất này tránh nhiều lỗi khi tổng quát hóa phạm vi (range / 범위) cấu trúc (structure / 구조).

> **Nối mạch:** **Số học modulo** nối từ **Commutativity không giống associativity** sang **GCD, coprime và modular inverse**, vì cơ chế trước tạo đầu vào cho bước sau.

## Số học modulo

Các đồng nhất thức cơ bản:

\[
(a+b)\bmod m=((a\bmod m)+(b\bmod m))\bmod m
\]

\[
(ab)\bmod m=((a\bmod m)(b\bmod m))\bmod m
\]

Modulo xuất hiện trong hashing, cyclic buffer, rolling băm (hash / 해시) và counting lớn.

Phép chia không thể thay bằng chia số nguyên rồi `% m`. Muốn “chia” trong modulo cần **nghịch đảo modulo (modular inverse)** và inverse chỉ tồn tại khi điều kiện phù hợp được thỏa.

> **Nối mạch:** **GCD, coprime và modular inverse** nối từ **Số học modulo** sang **Modulo âm trong ngôn ngữ lập trình**, vì cơ chế trước tạo đầu vào cho bước sau.

## GCD, coprime và modular inverse

Euclid:

\[
gcd(a,b)=gcd(b,a\bmod b)
\]

Mỗi bước làm đối số giảm mạnh nên số bước là logarithmic theo độ lớn số.

Hai số coprime khi:

\[
gcd(a,m)=1
\]

Khi đó `a` có modular inverse modulo `m`.

Extended Euclidean thuật toán (algorithm / 알고리즘) tìm `x,y` sao cho:

\[
ax+by=gcd(a,b)
\]

Nếu `gcd(a,m)=1`, từ đó suy ra một inverse của `a (mod m)`.

> **Nối mạch:** **Modulo âm trong ngôn ngữ lập trình** nối từ **GCD, coprime và modular inverse** sang **Bit và lũy thừa của hai**, vì cơ chế trước tạo đầu vào cho bước sau.

## Modulo âm trong ngôn ngữ lập trình

Toán học thường chọn phần dư chuẩn không âm, nhưng `%` trong C, Java và JavaScript hoạt động theo quy tắc remainder của ngôn ngữ và có thể trả số âm với toán hạng âm.

Một mẫu normalize thường gặp:

```text
((x % m) + m) % m
```

Nhưng hiện thực (implementation / 구현) vẫn phải xét overflow trước khi cộng nếu kiểu số hữu hạn.

> **Nối mạch:** **Bit và lũy thừa của hai** nối từ **Modulo âm trong ngôn ngữ lập trình** sang **Xác suất và biến cố**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bit và lũy thừa của hai

Với số nguyên dương `x`, nếu `x` là lũy thừa của hai thì biểu diễn nhị phân có đúng một bit 1.

Một định danh (identity / 식별자) phổ biến:

```text
x & (x - 1)
```

xóa bit 1 thấp nhất. Vì vậy:

```text
x > 0 && (x & (x - 1)) == 0
```

kiểm tra lũy thừa của hai trong mô hình integer phù hợp.

Fenwick cây (tree / 트리) dùng:

```text
x & -x
```

để lấy lowbit, tức giá trị của bit 1 thấp nhất. Đây không phải mẹo thần bí; nó là hệ quả của biểu diễn bù hai.

> **Nối mạch:** **Xác suất và biến cố** nối từ **Bit và lũy thừa của hai** sang **Kỳ vọng và tính tuyến tính của kỳ vọng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Xác suất và biến cố

Với hai biến cố độc lập:

\[
P(A\cap B)=P(A)P(B)
\]

Nhưng không được giả định độc lập chỉ vì hai sự kiện “trông khác nhau”. băm (hash / 해시) functions tương quan hoặc randomness dùng lại có thể phá giả định này.

Xác suất có điều kiện:

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
\]

là công cụ nền tảng khi phân tích sampling, collision và quá trình ngẫu nhiên phụ thuộc trạng thái trước đó.

> **Nối mạch:** **Kỳ vọng và tính tuyến tính của kỳ vọng** nối từ **Xác suất và biến cố** sang **Indicator variable**, vì cơ chế trước tạo đầu vào cho bước sau.

## Kỳ vọng và tính tuyến tính của kỳ vọng

Kỳ vọng:

\[
E[X]=\sum_x xP(X=x)
\]

Tính chất cực mạnh:

\[
E[X+Y]=E[X]+E[Y]
\]

không đòi hỏi `X` và `Y` độc lập.

Nếu tổng chi phí là tổng contribution của nhiều sự kiện, ta có thể phân tích từng contribution rồi cộng expectation.

Đây là một trong những lý do probabilistic phân tích (analysis / 분석) thường trở nên đơn giản hơn sau khi định nghĩa đúng biến ngẫu nhiên.

> **Nối mạch:** **Indicator variable** nối từ **Kỳ vọng và tính tuyến tính của kỳ vọng** sang **Variance và tail hành vi (behavior / 동작)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Indicator variable

Định nghĩa:

\[
I_i=\begin{cases}
1 & \văn bản (text / 텍스트){nếu sự kiện i xảy ra}\\
0 & \văn bản (text / 텍스트){nếu không}
\end{cases}
\]

thì:

\[
E[I_i]=P(i\text{ xảy ra})
\]

Nếu:

\[
X=\sum_i I_i
\]

thì:

\[
E[X]=\sum_i P(i\text{ xảy ra})
\]

Cách này rất hữu ích để đếm kỳ vọng số collision, số phần tử được chọn hoặc số lần một sự kiện (event / 이벤트) xảy ra.

> **Nối mạch:** **Variance và tail hành vi (behavior / 동작)** nối từ **Indicator variable** sang **Union bound**, vì cơ chế trước tạo đầu vào cho bước sau.

## Variance và tail hành vi (behavior / 동작)

Kỳ vọng chỉ nói trung bình, không nói mức độ phân tán.

\[
Var(X)=E[(X-E[X])^2]
\]

Hai thuật toán có cùng expected thời gian chạy (runtime / 런타임) nhưng một thuật toán có tail độ trễ (latency / 지연 시간) lớn hơn rất nhiều có thể khác hẳn trong môi trường vận hành (production / 운영 환경).

Markov, Chebyshev, Chernoff và Hoeffding là các lớp công cụ để đưa ra cận xác suất vượt quá ngưỡng. Không cần thuộc toàn bộ công thức ngay, nhưng phải nhớ:

> Expected giá trị (value / 값) tốt không tự động chứng minh bad trường hợp (case / 사례) hiếm.

> **Nối mạch:** **Union bound** nối từ **Variance và tail hành vi (behavior / 동작)** sang **Randomized thuật toán (algorithm / 알고리즘) và probabilistic cấu trúc dữ liệu (data structure / 자료구조)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Union bound

Với các biến cố `A_1,...,A_k`:

\[
P\left(\bigcup_i A_i\right)\le\sum_i P(A_i)
\]

Không cần các biến cố độc lập.

Union bound rất hữu ích khi muốn chứng minh “xác suất có ít nhất một lỗi trong nhiều vị trí” nhỏ bằng cách cộng các xác suất lỗi riêng lẻ.

> **Nối mạch:** **Union bound** đặt vấn đề; **Randomized thuật toán (algorithm / 알고리즘) và probabilistic cấu trúc dữ liệu (data structure / 자료구조)** kiểm tra bằng chứng, rồi **Quy nạp cấu trúc** mở rộng hệ quả.

## Randomized thuật toán (algorithm / 알고리즘) và probabilistic cấu trúc dữ liệu (data structure / 자료구조)

Cần phân biệt hai khái niệm.

Randomized Quicksort luôn trả kết quả sort chính xác nhưng thời gian chạy (runtime / 런타임) phụ thuộc randomness.

Bloom Filter có thể trả false positive; randomness ảnh hưởng cả biểu diễn (representation / 표현) và xác suất lỗi.

Một thuật toán có thể ngẫu nhiên nhưng chính xác (exact / 정확한), hoặc deterministic nhưng approximate, hoặc vừa randomized vừa approximate. Không nên trộn các loại guarantee này.

> **Nối mạch:** **Randomized thuật toán (algorithm / 알고리즘) và probabilistic cấu trúc dữ liệu (data structure / 자료구조)** đặt vấn đề; **Quy nạp cấu trúc** kiểm tra bằng chứng, rồi **Quy nạp mạnh và động (dynamic / 동적) Programming** mở rộng hệ quả.

## Quy nạp cấu trúc

Cây (tree / 트리), linked cấu trúc (structure / 구조) và recursive grammar tự nhiên với structural induction.

```text
base: cấu trúc rỗng hoặc lá đúng
step: giả sử các substructure đúng, chứng minh cách ghép ở node hiện tại đúng
```

Đây là phiên bản toán học của đặc tả hợp đồng (contract / 계약) đệ quy.

> **Nối mạch:** **Quy nạp mạnh và động (dynamic / 동적) Programming** nối từ **Quy nạp cấu trúc** sang **Một số đẳng thức đồ thị cơ bản**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quy nạp mạnh và động (dynamic / 동적) Programming

Một trạng thái DP có thể phụ thuộc nhiều trạng thái nhỏ hơn. Strong induction giả sử tất cả trạng thái nhỏ hơn đã đúng rồi chứng minh trạng thái hiện tại.

Bottom-up DP thực hiện chính thứ tự chứng minh đó: prerequisite được tính trước khi trạng thái (state / 상태) mới sử dụng chúng.

> **Nối mạch:** **Một số đẳng thức đồ thị cơ bản** nối từ **Quy nạp mạnh và động (dynamic / 동적) Programming** sang **Đếm cạnh của đồ thị dày đặc**, vì cơ chế trước tạo đầu vào cho bước sau.

## Một số đẳng thức đồ thị cơ bản

Với đồ thị vô hướng:

\[
\sum_{v\in V}degree(v)=2|E|
\]

vì mỗi cạnh đóng góp hai đầu mút. Hệ quả: số đỉnh có bậc lẻ luôn chẵn.

Với đồ thị có hướng:

\[
\sum indegree(v)=\sum outdegree(v)=|E|
\]

Với cây có `n` đỉnh:

\[
|E|=n-1
\]

Nếu một đồ thị vô hướng liên thông có `n-1` cạnh thì nó là cây. Nếu một đồ thị vô hướng không chu trình có `n-1` cạnh thì nó cũng phải liên thông.

Các định danh (identity / 식별자) này vừa hỗ trợ chứng minh vừa hỗ trợ validator.

> **Nối mạch:** **Đếm cạnh của đồ thị dày đặc** nối từ **Một số đẳng thức đồ thị cơ bản** sang **Sparse ma trận (matrix / 행렬) và đồ thị (graph / 그래프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đếm cạnh của đồ thị dày đặc

Đồ thị vô hướng đơn với `n` đỉnh có tối đa:

\[
\frac{n(n-1)}2
\]

cạnh. Đồ thị có hướng đơn không self-loop có tối đa:

\[
n(n-1)
\]

cạnh.

Khi `m` gần `n²`, adjacency ma trận (matrix / 행렬) có thể hợp lý hơn. Khi `m` gần tuyến tính theo `n`, adjacency danh sách (list / 목록)/CSR thường tiết kiệm hơn.

Toán đếm giúp chọn biểu diễn (representation / 표현) trước cả khi benchmark.

> **Nối mạch:** **Sparse ma trận (matrix / 행렬) và đồ thị (graph / 그래프)** nối từ **Đếm cạnh của đồ thị dày đặc** sang **Phân tích khấu hao: phương pháp tổng hợp**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sparse ma trận (matrix / 행렬) và đồ thị (graph / 그래프)

Adjacency ma trận (matrix / 행렬) của đồ thị (graph / 그래프) là một ma trận. Với đồ thị (graph / 그래프) thưa, phần lớn entry bằng 0. CSR và các sparse biểu diễn (representation / 표현) về bản chất là cách lưu chỉ các phần tử khác 0.

Nhiều phép toán đồ thị (graph / 그래프) có thể được nhìn dưới dạng tuyến tính (linear / 선형) algebra. Ví dụ số walk độ dài `k` liên hệ với lũy thừa ma trận kề. Tuy nhiên, cách nhìn ma trận không luôn là hiện thực (implementation / 구현) tốt nhất cho đồ thị (graph / 그래프) traversal thông thường; nó cung cấp một mô hình toán học khác để thấy cấu trúc.

> **Nối mạch:** **Phân tích khấu hao: phương pháp tổng hợp** tổng hợp từ **Sparse ma trận (matrix / 행렬) và đồ thị (graph / 그래프)**; **Phương pháp hạch toán** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Phân tích khấu hao: phương pháp tổng hợp

Nếu `n` thao tác có tổng chi phí `T(n)`, chi phí khấu hao là:

\[
\frac{T(n)}n
\]

Động (dynamic / 동적) Array doubling là ví dụ điển hình: một số append đắt nhưng tổng chi phí vẫn tuyến tính.

> **Nối mạch:** **Phương pháp hạch toán** tổng hợp từ **Phân tích khấu hao: phương pháp tổng hợp**; **Phương pháp thế năng** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Phương pháp hạch toán

Ta gán cho mỗi thao tác (operation / 연산) một “giá” có thể lớn hơn chi phí thực tế. Phần dư được coi như credit dành cho thao tác đắt trong tương lai.

Nếu chứng minh credit không bao giờ âm và tổng charge là `O(n)`, tổng actual chi phí (cost / 비용) cũng bị chặn bởi `O(n)`.

Đây là cách suy nghĩ trực quan về việc các thao tác rẻ “trả trước” cho resize sau này.

> **Nối mạch:** **Phương pháp thế năng** nối từ **Phương pháp hạch toán** sang **Lower bound theo lý thuyết thông tin**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phương pháp thế năng

Định nghĩa potential `Φ(D)` cho trạng thái cấu trúc `D`.

Chi phí khấu hao:

\[
\hat c_i=c_i+\Phi(D_i)-\Phi(D_{i-1})
\]

Nếu một thao tác (operation / 연산) rẻ làm potential tăng, nó tích trữ “năng lượng”. Một thao tác (operation / 연산) đắt có thể làm potential giảm và phần giảm đó bù vào actual chi phí (cost / 비용).

Potential phương thức (method / 메서드) rất mạnh vì không cần gắn credit vào từng đối tượng (object / 객체) cụ thể; chỉ cần một hàm đo toàn trạng thái.

> **Nối mạch:** **Lower bound theo lý thuyết thông tin** nối từ **Phương pháp thế năng** sang **Tìm kiếm (search / 검색) lower bound**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lower bound theo lý thuyết thông tin

Comparison sorting phải phân biệt `n!` thứ tự đầu vào (input / 입력) có thể có. Mỗi comparison nhị phân chỉ tạo tối đa hai nhánh trong cây quyết định (decision tree / 의사결정 트리).

Chiều cao cây quyết định ít nhất:

\[
\log_2(n!)=\Omega(n\log n)
\]

Do đó không thể có general comparison sort worst-case `O(n)`.

Counting Sort/Radix Sort không mâu thuẫn với cận này vì chúng khai thác thông tin khác ngoài pairwise comparison, chẳng hạn miền khóa hữu hạn hoặc biểu diễn (representation / 표현) chữ số.

> **Nối mạch:** **Tìm kiếm (search / 검색) lower bound** nối từ **Lower bound theo lý thuyết thông tin** sang **Big-O, Omega và Theta**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tìm kiếm (search / 검색) lower bound

Trên mảng chưa sắp xếp, để khẳng định mục tiêu (target / 대상) không tồn tại, trường hợp xấu nhất phải kiểm tra mọi phần tử:

\[
\Omega(n)
\]

Sau khi sắp xếp, mỗi comparison có thể loại gần nửa candidate, dẫn tới logarithmic tìm kiếm (search / 검색).

Lower bound thường bắt đầu từ câu hỏi:

> Mỗi observation cung cấp tối đa bao nhiêu thông tin về đáp án?

> **Nối mạch:** **Big-O, Omega và Theta** nối từ **Tìm kiếm (search / 검색) lower bound** sang **Worst-case, average-case, expected-case và amortized**, vì cơ chế trước tạo đầu vào cho bước sau.

## Big-O, Omega và Theta

`O(g(n))` là cận trên tiệm cận. `Ω(g(n))` là cận dưới. `Θ(g(n))` nói tốc độ tăng bị kẹp cả trên lẫn dưới bởi cùng bậc.

Nếu một thuật toán chạy đúng `3n² + 5n + 7`, có thể nói:

```text
O(n²)
Ω(n²)
Θ(n²)
```

Việc chỉ nói `O(n³)` cũng đúng về mặt cận trên nhưng quá lỏng và ít thông tin.

> **Nối mạch:** **Big-O, Omega và Theta** nêu quy tắc; **Worst-case, average-case, expected-case và amortized** thử quy tắc trong tình huống, rồi **Sai số số học và miền giá trị** mở rộng hệ quả.

## Worst-case, average-case, expected-case và amortized

Bốn khái niệm này không giống nhau.

**Worst-case**: đầu vào (input / 입력) tệ nhất trong miền hợp lệ.

**Average-case**: trung bình theo một phân phối đầu vào (input / 입력) xác định.

**Expected-case**: kỳ vọng, thường do randomness của thuật toán hoặc cấu trúc.

**Amortized**: trung bình trên chuỗi thao tác nhưng không cần giả định xác suất.

Trộn các khái niệm này dễ dẫn tới tuyên bố hiệu năng sai.

> **Nối mạch:** **Worst-case, average-case, expected-case và amortized** nêu quy tắc; **Sai số số học và miền giá trị** thử quy tắc trong tình huống, rồi **Một checklist toán học cho DSA** mở rộng hệ quả.

## Sai số số học và miền giá trị

Toán học thường dùng số nguyên vô hạn, nhưng mã (code / 코드) dùng kiểu hữu hạn.

Nếu cộng `n` giá trị mỗi giá trị tối đa `M`, tổng có thể tới khoảng `nM`. Trước khi chọn `int` hay `long`, nên ước lượng upper bound.

Với multiplication, overflow có thể xảy ra trước modulo:

```text
(a * b) % m
```

nếu `a*b` vượt miền kiểu. tính đúng đắn (correctness / 정확성) phải xét cả bước trung gian.

JavaScript `Number` chỉ biểu diễn chính xác mọi số nguyên tới `2^53-1`; các bài counting lớn có thể cần `BigInt`.

> **Nối mạch:** **Một checklist toán học cho DSA** nối từ **Sai số số học và miền giá trị** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Một checklist toán học cho DSA

Khi gặp bài mới, có thể hỏi:

```text
Không gian trạng thái có bao nhiêu phần tử?
Một bước giảm kích thước theo cộng hay theo tỷ lệ?
Có tổng hoặc recurrence nào mô tả runtime không?
Operation range có associative không?
Có identity hoặc inverse không?
Có idempotent không?
Có thể dùng bit representation không?
Có lower bound tự nhiên nào không?
Có randomness không, và guarantee là expected hay probabilistic?
Kiểu số có đủ miền giá trị không?
```

Những câu hỏi này giúp toán học trở thành công cụ thiết kế thay vì phần phụ lý thuyết.

> **Nối mạch:** **Mô hình tư duy** tổng hợp từ **Một checklist toán học cho DSA**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> Toán học trong DSA không phải một tập công thức rời rạc. Nó là ngôn ngữ mô tả **số trạng thái, tốc độ thu nhỏ, cách ghép kết quả, lượng thông tin thu được và giới hạn của điều có thể tối ưu**.

Khi hiểu vì sao một cấu trúc cần associativity, vì sao `log n` xuất hiện khi chia đôi, vì sao `2^n` xuất hiện với subset, hoặc vì sao comparison sorting có cận `n log n`, ta có thể tự suy ra nhiều thuật toán thay vì ghi nhớ từng công thức riêng lẻ.

Xem tiếp: [Problem Modeling](./00_dsa_as_problem_modeling.md), [Correctness & Invariants](./01_algorithm_correctness_and_invariants.md), [Complexity Analysis](./02_complexity_analysis.md), [Bit Manipulation](../05_specialized/02_bit_manipulation_and_bitsets.md), [Sparse Table](../05_specialized/05_sparse_table_and_static_range_queries.md) và [Amortized & Randomized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
