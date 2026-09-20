# Công cụ toán học cho cấu trúc dữ liệu và thuật toán
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

Đây là nguồn gốc của `O(log n)` trong binary search, balanced BST, heap, binary lifting và nhiều thuật toán divide-and-conquer.

Cơ số logarithm không quan trọng trong Big-O vì:

\[
\log_a n = \frac{\log_b n}{\log_b a}
\]

hai logarithm khác cơ số chỉ khác một hệ số hằng. Nhưng ở cấp hệ thống, cơ số vẫn có ý nghĩa. B+Tree có chiều cao gần `log_B n` với `B` lớn vì mỗi page chứa nhiều khóa, nên số lần I/O giảm mạnh.

Mô hình tư duy:

> `log n` thường xuất hiện khi mỗi bước loại bỏ hoặc gom lại một tỷ lệ cố định của phần còn lại.

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

Sparse Table lưu block độ dài `2^k`. Binary Lifting lưu tổ tiên cách `2^k` cạnh. Fenwick Tree dùng bit 1 thấp nhất để xác định kích thước block phụ trách. Exponentiation by squaring phân rã số mũ theo bit.

Một insight quan trọng là nhiều kỹ thuật tưởng khác nhau thực ra cùng dùng ý tưởng: **tiền xử lý các bước có kích thước tăng gấp đôi rồi ghép chúng theo biểu diễn nhị phân của một số nguyên**.

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

## Cấp số nhân và phân tích khấu hao

Tổng hình học:

\[
1+2+4+\cdots+2^k=2^{k+1}-1
\]

là nền tảng của nhiều phân tích doubling.

Mảng động tăng capacity gấp đôi. Qua `n` lần append, số phần tử bị copy trong các lần resize xấp xỉ:

\[
1+2+4+\cdots+\frac n2<n
\]

Do đó tổng copy là `O(n)`, dù một lần append riêng lẻ có thể tốn `O(n)`. Chi phí khấu hao mỗi append vẫn là `O(1)`.

Điểm quan trọng: **amortized** không phải “trung bình theo xác suất”. Nó là bảo đảm về tổng chi phí của một chuỗi thao tác hợp lệ.

## Harmonic series

Tổng điều hòa:

\[
H_n=1+\frac12+\frac13+\cdots+\frac1n=\Theta(\log n)
\]

xuất hiện trong randomized algorithms, coupon-collector reasoning, một số phân tích hashing và nhiều quá trình xác suất.

Khi thấy tổng nghịch đảo `1/i`, nên nghĩ tới tăng trưởng logarithmic thay vì tuyến tính.

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

## Công thức truy hồi mô tả cây đệ quy

Merge Sort:

\[
T(n)=2T(n/2)+cn
\]

Mỗi tầng của cây đệ quy có tổng công việc `Θ(n)` và có `Θ(log n)` tầng, nên:

\[
T(n)=\Theta(n\log n)
\]

Binary Search:

\[
T(n)=T(n/2)+c=\Theta(\log n)
\]

Quicksort trường hợp xấu khi partition cực lệch:

\[
T(n)=T(n-1)+cn=\Theta(n^2)
\]

Truy hồi là bản mô tả toán học của hình dạng recursion tree. Nếu không hiểu recursion tree, dùng công thức dễ trở thành thao tác máy móc.

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

hoặc subproblem không đều, recurrence phụ thuộc dữ liệu, hay randomized recurrence thường phù hợp hơn với substitution, recursion tree hoặc probabilistic analysis.

Bài học: theorem là công cụ cho một lớp cấu trúc, không phải phép biến đổi cú pháp tổng quát.

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

với `b` là branching factor và `d` là độ sâu. Pruning làm branching factor hiệu dụng nhỏ hơn, nhưng không tự thay đổi worst-case nếu vẫn tồn tại input buộc duyệt gần toàn cây.

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

## Pigeonhole principle

Nếu đặt nhiều hơn `m` đối tượng vào `m` ngăn, ít nhất một ngăn chứa từ hai đối tượng trở lên.

Trong hashing, miền khóa thường lớn hơn số bucket, nên collision không phải “lỗi hiếm có thể loại bỏ hoàn toàn”; nó là điều toán học không tránh khỏi. Thiết kế đúng phải quản lý collision.

Pigeonhole cũng xuất hiện trong chứng minh duplicate, cycle và nhiều lập luận tồn tại.

## Inclusion–exclusion

Với hai tập:

\[
|A\cup B|=|A|+|B|-|A\cap B|
\]

Ta phải trừ phần giao vì nó bị đếm hai lần.

Với nhiều tập, các giao được cộng/trừ luân phiên. Ý tưởng này xuất hiện trong combinatorial counting, bitmask DP, xác suất và một số thuật toán đếm với điều kiện loại trừ.

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

Điều này giải thích vì sao Prefix Sum làm range sum rất tự nhiên, còn prefix minimum không thể “trừ min cũ” để lấy min của một đoạn bất kỳ.

## Semigroup, monoid và group trong DSA

Nhiều cấu trúc range query có thể hiểu bằng đại số.

### Tính kết hợp

Một phép toán `*` có tính kết hợp nếu:

\[
(a*b)*c=a*(b*c)
\]

Khi đó ta có thể chia đoạn thành nhiều block rồi ghép kết quả theo bất kỳ cách đặt ngoặc nào. Segment Tree cần tính chất này.

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

Identity rất hữu ích cho đoạn rỗng và accumulator ban đầu.

### Phép nghịch đảo

Nếu mỗi phần tử có inverse phù hợp, monoid trở thành group. Prefix Sum hưởng lợi từ inverse của phép cộng:

\[
a+(-a)=0
\]

Fenwick Tree cho range sum rất tự nhiên vì prefix aggregate có thể “trừ” nhau.

### Idempotence

Một phép toán idempotent nếu:

\[
f(x,x)=x
\]

`min`, `max`, `gcd`, bitwise AND/OR có tính chất này. Classic Sparse Table có thể trả RMQ bằng hai block chồng lấn vì phần giao bị tính hai lần nhưng không thay kết quả.

Nhìn bằng đại số giúp trả lời câu hỏi “cấu trúc này có tổng quát sang operation khác không?” chính xác hơn việc học thuộc danh sách.

## Commutativity không giống associativity

**Giao hoán (commutativity)**:

\[
a*b=b*a
\]

không bắt buộc cho mọi cấu trúc. Segment Tree có thể làm việc với phép kết hợp không giao hoán, miễn ta giữ đúng thứ tự trái–phải.

Ví dụ nối chuỗi là associative nhưng không commutative:

```text
"ab" + "cd" != "cd" + "ab"
```

Phân biệt hai tính chất này tránh nhiều lỗi khi tổng quát hóa range structure.

## Số học modulo

Các đồng nhất thức cơ bản:

\[
(a+b)\bmod m=((a\bmod m)+(b\bmod m))\bmod m
\]

\[
(ab)\bmod m=((a\bmod m)(b\bmod m))\bmod m
\]

Modulo xuất hiện trong hashing, cyclic buffer, rolling hash và counting lớn.

Phép chia không thể thay bằng chia số nguyên rồi `% m`. Muốn “chia” trong modulo cần **nghịch đảo modulo (modular inverse)** và inverse chỉ tồn tại khi điều kiện phù hợp được thỏa.

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

Extended Euclidean Algorithm tìm `x,y` sao cho:

\[
ax+by=gcd(a,b)
\]

Nếu `gcd(a,m)=1`, từ đó suy ra một inverse của `a (mod m)`.

## Modulo âm trong ngôn ngữ lập trình

Toán học thường chọn phần dư chuẩn không âm, nhưng `%` trong C, Java và JavaScript hoạt động theo quy tắc remainder của ngôn ngữ và có thể trả số âm với toán hạng âm.

Một mẫu normalize thường gặp:

```text
((x % m) + m) % m
```

Nhưng implementation vẫn phải xét overflow trước khi cộng nếu kiểu số hữu hạn.

## Bit và lũy thừa của hai

Với số nguyên dương `x`, nếu `x` là lũy thừa của hai thì biểu diễn nhị phân có đúng một bit 1.

Một identity phổ biến:

```text
x & (x - 1)
```

xóa bit 1 thấp nhất. Vì vậy:

```text
x > 0 && (x & (x - 1)) == 0
```

kiểm tra lũy thừa của hai trong mô hình integer phù hợp.

Fenwick Tree dùng:

```text
x & -x
```

để lấy lowbit, tức giá trị của bit 1 thấp nhất. Đây không phải mẹo thần bí; nó là hệ quả của biểu diễn bù hai.

## Xác suất và biến cố

Với hai biến cố độc lập:

\[
P(A\cap B)=P(A)P(B)
\]

Nhưng không được giả định độc lập chỉ vì hai sự kiện “trông khác nhau”. Hash functions tương quan hoặc randomness dùng lại có thể phá giả định này.

Xác suất có điều kiện:

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
\]

là công cụ nền tảng khi phân tích sampling, collision và quá trình ngẫu nhiên phụ thuộc trạng thái trước đó.

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

Đây là một trong những lý do probabilistic analysis thường trở nên đơn giản hơn sau khi định nghĩa đúng biến ngẫu nhiên.

## Indicator variable

Định nghĩa:

\[
I_i=\begin{cases}
1 & \text{nếu sự kiện i xảy ra}\\
0 & \text{nếu không}
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

Cách này rất hữu ích để đếm kỳ vọng số collision, số phần tử được chọn hoặc số lần một event xảy ra.

## Variance và tail behavior

Kỳ vọng chỉ nói trung bình, không nói mức độ phân tán.

\[
Var(X)=E[(X-E[X])^2]
\]

Hai thuật toán có cùng expected runtime nhưng một thuật toán có tail latency lớn hơn rất nhiều có thể khác hẳn trong production.

Markov, Chebyshev, Chernoff và Hoeffding là các lớp công cụ để đưa ra cận xác suất vượt quá ngưỡng. Không cần thuộc toàn bộ công thức ngay, nhưng phải nhớ:

> Expected value tốt không tự động chứng minh bad case hiếm.

## Union bound

Với các biến cố `A_1,...,A_k`:

\[
P\left(\bigcup_i A_i\right)\le\sum_i P(A_i)
\]

Không cần các biến cố độc lập.

Union bound rất hữu ích khi muốn chứng minh “xác suất có ít nhất một lỗi trong nhiều vị trí” nhỏ bằng cách cộng các xác suất lỗi riêng lẻ.

## Randomized algorithm và probabilistic data structure

Cần phân biệt hai khái niệm.

Randomized Quicksort luôn trả kết quả sort chính xác nhưng runtime phụ thuộc randomness.

Bloom Filter có thể trả false positive; randomness ảnh hưởng cả representation và xác suất lỗi.

Một thuật toán có thể ngẫu nhiên nhưng exact, hoặc deterministic nhưng approximate, hoặc vừa randomized vừa approximate. Không nên trộn các loại guarantee này.

## Quy nạp cấu trúc

Tree, linked structure và recursive grammar tự nhiên với structural induction.

```text
base: cấu trúc rỗng hoặc lá đúng
step: giả sử các substructure đúng, chứng minh cách ghép ở node hiện tại đúng
```

Đây là phiên bản toán học của contract đệ quy.

## Quy nạp mạnh và Dynamic Programming

Một trạng thái DP có thể phụ thuộc nhiều trạng thái nhỏ hơn. Strong induction giả sử tất cả trạng thái nhỏ hơn đã đúng rồi chứng minh trạng thái hiện tại.

Bottom-up DP thực hiện chính thứ tự chứng minh đó: prerequisite được tính trước khi state mới sử dụng chúng.

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

Các identity này vừa hỗ trợ chứng minh vừa hỗ trợ validator.

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

Khi `m` gần `n²`, adjacency matrix có thể hợp lý hơn. Khi `m` gần tuyến tính theo `n`, adjacency list/CSR thường tiết kiệm hơn.

Toán đếm giúp chọn representation trước cả khi benchmark.

## Sparse matrix và graph

Adjacency matrix của graph là một ma trận. Với graph thưa, phần lớn entry bằng 0. CSR và các sparse representation về bản chất là cách lưu chỉ các phần tử khác 0.

Nhiều phép toán graph có thể được nhìn dưới dạng linear algebra. Ví dụ số walk độ dài `k` liên hệ với lũy thừa ma trận kề. Tuy nhiên, cách nhìn ma trận không luôn là implementation tốt nhất cho graph traversal thông thường; nó cung cấp một mô hình toán học khác để thấy cấu trúc.

## Phân tích khấu hao: phương pháp tổng hợp

Nếu `n` thao tác có tổng chi phí `T(n)`, chi phí khấu hao là:

\[
\frac{T(n)}n
\]

Dynamic Array doubling là ví dụ điển hình: một số append đắt nhưng tổng chi phí vẫn tuyến tính.

## Phương pháp hạch toán

Ta gán cho mỗi operation một “giá” có thể lớn hơn chi phí thực tế. Phần dư được coi như credit dành cho thao tác đắt trong tương lai.

Nếu chứng minh credit không bao giờ âm và tổng charge là `O(n)`, tổng actual cost cũng bị chặn bởi `O(n)`.

Đây là cách suy nghĩ trực quan về việc các thao tác rẻ “trả trước” cho resize sau này.

## Phương pháp thế năng

Định nghĩa potential `Φ(D)` cho trạng thái cấu trúc `D`.

Chi phí khấu hao:

\[
\hat c_i=c_i+\Phi(D_i)-\Phi(D_{i-1})
\]

Nếu một operation rẻ làm potential tăng, nó tích trữ “năng lượng”. Một operation đắt có thể làm potential giảm và phần giảm đó bù vào actual cost.

Potential method rất mạnh vì không cần gắn credit vào từng object cụ thể; chỉ cần một hàm đo toàn trạng thái.

## Lower bound theo lý thuyết thông tin

Comparison sorting phải phân biệt `n!` thứ tự input có thể có. Mỗi comparison nhị phân chỉ tạo tối đa hai nhánh trong decision tree.

Chiều cao cây quyết định ít nhất:

\[
\log_2(n!)=\Omega(n\log n)
\]

Do đó không thể có general comparison sort worst-case `O(n)`.

Counting Sort/Radix Sort không mâu thuẫn với cận này vì chúng khai thác thông tin khác ngoài pairwise comparison, chẳng hạn miền khóa hữu hạn hoặc representation chữ số.

## Search lower bound

Trên mảng chưa sắp xếp, để khẳng định target không tồn tại, trường hợp xấu nhất phải kiểm tra mọi phần tử:

\[
\Omega(n)
\]

Sau khi sắp xếp, mỗi comparison có thể loại gần nửa candidate, dẫn tới logarithmic search.

Lower bound thường bắt đầu từ câu hỏi:

> Mỗi observation cung cấp tối đa bao nhiêu thông tin về đáp án?

## Big-O, Omega và Theta

`O(g(n))` là cận trên tiệm cận. `Ω(g(n))` là cận dưới. `Θ(g(n))` nói tốc độ tăng bị kẹp cả trên lẫn dưới bởi cùng bậc.

Nếu một thuật toán chạy đúng `3n² + 5n + 7`, có thể nói:

```text
O(n²)
Ω(n²)
Θ(n²)
```

Việc chỉ nói `O(n³)` cũng đúng về mặt cận trên nhưng quá lỏng và ít thông tin.

## Worst-case, average-case, expected-case và amortized

Bốn khái niệm này không giống nhau.

**Worst-case**: input tệ nhất trong miền hợp lệ.

**Average-case**: trung bình theo một phân phối input xác định.

**Expected-case**: kỳ vọng, thường do randomness của thuật toán hoặc cấu trúc.

**Amortized**: trung bình trên chuỗi thao tác nhưng không cần giả định xác suất.

Trộn các khái niệm này dễ dẫn tới tuyên bố hiệu năng sai.

## Sai số số học và miền giá trị

Toán học thường dùng số nguyên vô hạn, nhưng code dùng kiểu hữu hạn.

Nếu cộng `n` giá trị mỗi giá trị tối đa `M`, tổng có thể tới khoảng `nM`. Trước khi chọn `int` hay `long`, nên ước lượng upper bound.

Với multiplication, overflow có thể xảy ra trước modulo:

```text
(a * b) % m
```

nếu `a*b` vượt miền kiểu. Correctness phải xét cả bước trung gian.

JavaScript `Number` chỉ biểu diễn chính xác mọi số nguyên tới `2^53-1`; các bài counting lớn có thể cần `BigInt`.

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

## Mô hình tư duy

> Toán học trong DSA không phải một tập công thức rời rạc. Nó là ngôn ngữ mô tả **số trạng thái, tốc độ thu nhỏ, cách ghép kết quả, lượng thông tin thu được và giới hạn của điều có thể tối ưu**.

Khi hiểu vì sao một cấu trúc cần associativity, vì sao `log n` xuất hiện khi chia đôi, vì sao `2^n` xuất hiện với subset, hoặc vì sao comparison sorting có cận `n log n`, ta có thể tự suy ra nhiều thuật toán thay vì ghi nhớ từng công thức riêng lẻ.

Xem tiếp: [Problem Modeling](./00_dsa_as_problem_modeling.md), [Correctness & Invariants](./01_algorithm_correctness_and_invariants.md), [Complexity Analysis](./02_complexity_analysis.md), [Bit Manipulation](../05_specialized/02_bit_manipulation_and_bitsets.md), [Sparse Table](../05_specialized/05_sparse_table_and_static_range_queries.md) và [Amortized & Randomized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md).