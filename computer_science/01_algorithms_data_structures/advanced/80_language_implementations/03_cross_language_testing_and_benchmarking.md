# Kiểm thử và đo hiệu năng DSA trên C, Java và JavaScript
**DSA Testing & Benchmarking / 자료구조·알고리즘 테스트와 벤치마킹**

Một cách triển khai DSA đáng tin cậy phải trả lời ba câu hỏi khác nhau:

```text
Thuật toán có đúng về mặt lý thuyết không?
Cách triển khai có lỗi không?
Chi phí thực tế trên môi trường chạy và phần cứng có đúng với kỳ vọng không?
```

**Chứng minh (proof)**, **kiểm thử (testing)** và **đo hiệu năng (benchmarking)** giải quyết ba lớp vấn đề khác nhau. Chứng minh giải thích tính đúng đắn và mô hình tăng trưởng. Kiểm thử cố tìm phản ví dụ trong mã nguồn thật. Benchmark đo độ trễ, thông lượng, bộ nhớ và khả năng mở rộng trong một môi trường cụ thể.

Benchmark không chứng minh tính đúng đắn, và một vài unit test cũng không chứng minh được Big-O.

## 1. Đặc tả trước kiểm thử

Trước khi viết test, phải xác định **hợp đồng (contract)**:

```text
đầu vào hợp lệ là gì?
đầu ra chính xác là gì?
có được phép thay đổi đầu vào không?
thứ tự và cách phá hòa được định nghĩa thế nào?
khi lỗi thì hành vi ra sao?
yêu cầu độ phức tạp nào là bắt buộc?
```

Ví dụ `topK(items, k)` có thể trả một tập không thứ tự, một danh sách đã sắp xếp hoặc một thứ tự tùy ý giữa các phần tử bằng nhau. Nếu đặc tả mơ hồ, một kiểm thử “thất bại” có thể chỉ phản ánh hai cách hiểu khác nhau về hợp đồng.

## 2. Hành vi công khai và bất biến nội bộ là hai lớp khác nhau

Hàng đợi phải giữ FIFO dù được cài bằng danh sách liên kết hay bộ đệm vòng. Kiểm thử hành vi công khai không nên phụ thuộc cách biểu diễn bên trong.

Cấu trúc tự cài đặt còn cần kiểm tra **bất biến (invariant)**:

```text
heap: nút cha <= các nút con
BST: duyệt inorder cho thứ tự đã sắp xếp
AVL/RB Tree: thỏa điều kiện cân bằng và màu
Hash Table: size khớp số ô đang chứa phần tử
DSU: các con trỏ cha tạo thành rừng hợp lệ
Segment Tree: nút cha = phép gộp của các nút con
```

Kiểm thử hành vi bảo vệ lớp trừu tượng; kiểm tra bất biến giúp phát hiện hỏng cấu trúc sớm hơn.

## 3. Assertion như một đặc tả có thể thực thi

Trong bản dựng dùng để kiểm thử hoặc gỡ lỗi, có thể đặt assertion:

```java
assert size >= 0 && size <= capacity;
```

hoặc viết các hàm:

```text
validateHeap()
validateBST()
validateFreeList()
```

Assertion không thay cho việc kiểm tra đầu vào ở ranh giới API. Nó dùng để phát hiện giả định của lập trình viên bị phá vỡ.

Một phép kiểm tra bất biến `O(n)` sau mỗi cập nhật có thể quá đắt cho production nhưng hoàn toàn hợp lý trong kiểm thử ngẫu nhiên.

## 4. Unit test nên bắt đầu từ trường hợp biên

Các trường hợp cần ưu tiên:

```text
rỗng
một phần tử
hai phần tử
đầy dung lượng
lần tăng dung lượng đầu tiên
xóa phần tử cuối cùng
khóa trùng
giá trị âm hoặc rất lớn
chỉ số nhỏ nhất/lớn nhất
```

Lỗi DSA thường xuất hiện ở các điểm chuyển trạng thái:

```text
rỗng -> một phần tử
một phần tử -> rỗng
capacity -> capacity + 1
xoay nút gốc
xóa head/tail
gộp hai thành phần
```

Không nên chỉ kiểm thử trạng thái “bình thường ở giữa”.

## 5. Kiểm thử đối chiếu

**Kiểm thử đối chiếu (differential testing)** chạy cách triển khai cần kiểm tra và một cách làm tham chiếu đơn giản trên cùng đầu vào.

```text
heap tự cài đặt       vs mảng đã sắp xếp
Segment Tree          vs vòng lặp trực tiếp trên mảng
Dijkstra              vs Floyd-Warshall trên đồ thị nhỏ
Kruskal               vs Prim
Hash Set tự cài đặt   vs mô hình tuyến tính đơn giản
Quickselect           vs sắp xếp toàn bộ
```

Bộ tham chiếu không cần nhanh. Với đầu vào nhỏ, một cách làm chậm nhưng đơn giản thường đáng tin hơn một “oracle” tối ưu nhưng phức tạp.

## 6. Kiểm thử dựa trên tính chất

Thay vì mã hóa cứng đầu ra, có thể kiểm tra các tính chất luôn phải đúng.

Sắp xếp:

```text
đầu ra không giảm
multiset(đầu ra) == multiset(đầu vào)
```

MST:

```text
có V-1 cạnh nếu đồ thị liên thông
liên thông
không có chu trình
chi phí bằng cách làm tham chiếu
```

Tìm cận dưới:

```text
mọi vị trí trước đáp án không thỏa điều kiện
đáp án và các vị trí sau thỏa điều kiện đơn điệu tương ứng
```

Kiểm thử dựa trên tính chất thường gần với đặc tả toán học hơn một tập nhỏ các ví dụ viết tay.

## 7. Kiểm thử biến hình

Khi khó tạo một oracle trực tiếp, có thể biến đổi đầu vào theo một quan hệ đã biết và kiểm tra đầu ra biến đổi tương ứng.

Ví dụ:

```text
đổi tên các đỉnh đồ thị -> kết quả phải tương đương sau khi ánh xạ lại
cộng cùng hằng số vào mọi khóa sắp xếp -> thứ tự tương đối không đổi
thêm một đỉnh cô lập -> khoảng cách giữa các đỉnh cũ không đổi
hoán vị đầu vào của thuật toán tập hợp -> tập kết quả không đổi
nhân mọi trọng số MST dương với cùng c -> cấu trúc tối ưu tương ứng nếu quan hệ hòa không đổi
```

Đây được gọi là **kiểm thử biến hình (metamorphic testing)** và đặc biệt hữu ích với đồ thị, tối ưu hóa và thuật toán ngẫu nhiên.

## 8. Kiểm thử dựa trên mô hình cho cấu trúc có trạng thái

Tạo một mô hình đơn giản rồi sinh chuỗi thao tác:

```text
insert
remove
contains
peek
update
```

Sau mỗi thao tác:

```text
so sánh giá trị trả về
so sánh nội dung logic
kiểm tra bất biến
```

Ví dụ, deque tự cài đặt có thể được đối chiếu với deque của thư viện chuẩn. Phương pháp này rất hiệu quả với lỗi chỉ xuất hiện sau một chuỗi thao tác dài.

## 9. Fuzzing có trạng thái

Fuzzer không nhất thiết chỉ sinh một đầu vào độc lập. Nó có thể sinh chuỗi thao tác phụ thuộc trạng thái:

```text
push 5
push 2
pop
push 9
remove index 0
...
```

Cách này có thể phát hiện lỗi thay đổi kích thước, con trỏ cũ, sai lệch siêu dữ liệu hoặc lỗi xóa ở trường hợp góc. Luôn ghi lại hạt giống và chuỗi thao tác để tái hiện lỗi.

## 10. Thu nhỏ trường hợp lỗi

Một chuỗi 100.000 thao tác gây lỗi ít hữu ích hơn một chuỗi 7 thao tác tối thiểu vẫn gây cùng lỗi. **Thu nhỏ (shrinking/minimization)** cố loại bớt thao tác hoặc giảm giá trị trong khi vẫn giữ lỗi.

Một cách đơn giản theo kiểu delta debugging:

```text
thử bỏ một nửa chuỗi
nếu vẫn lỗi -> giữ phiên bản nhỏ hơn
lặp lại
```

Phản ví dụ nhỏ thường làm nguyên nhân phá bất biến trở nên rõ ràng.

## 11. Bộ sinh dữ liệu phải biết các dạng lỗi

Sinh số ngẫu nhiên đồng đều là chưa đủ.

Sắp xếp nên thử:

```text
đã sắp xếp
giảm dần
gần sắp xếp
tất cả bằng nhau
rất nhiều phần tử trùng
mẫu organ-pipe
```

Bảng băm nên thử va chạm nhiều, chèn/xóa liên tục, ngưỡng hệ số tải và ranh giới băm lại. Đồ thị nên thử đường thẳng, hình sao, chu trình, DAG, clique, đồ thị rời rạc, cạnh song song và self-loop.

Bộ sinh tốt tạo **trường hợp đối nghịch có cấu trúc**, không chỉ tạo nhiễu ngẫu nhiên.

## 12. Hạt giống phải tái hiện được

Mọi kiểm thử ngẫu nhiên và benchmark có sinh dữ liệu nên cho phép cấu hình hạt giống. Báo cáo lỗi nên chứa:

```text
seed
kích thước đầu vào
tham số
phiên bản môi trường chạy
chuỗi thao tác hoặc trường hợp đã sinh
```

Không tái hiện được lỗi sẽ làm chi phí gỡ lỗi tăng mạnh.

## 13. Kiểm thử thuật toán ngẫu nhiên mà không làm test chập chờn

Không nên kiểm tra kiểu “Quickselect luôn dùng ít hơn X phép so sánh” trong một lần chạy ngẫu nhiên. Thay vào đó:

```text
kiểm tra tính đúng đắn ở mọi lần chạy
cố định seed cho trường hợp hồi quy
kiểm tra thống kê về hiệu năng/xác suất ở một bài test riêng nếu cần
```

Cấu trúc xác suất cần kiểm tra thống kê trên nhiều lần thử với dung sai và mức tin cậy phù hợp.

## 14. Kiểm thử cấu trúc dữ liệu xác suất

Bloom Filter:

```text
không có âm tính giả với phần tử đã chèn trong mô hình chuẩn
tỷ lệ dương tính giả gần mức kỳ vọng trên mẫu độc lập đủ lớn
```

HyperLogLog:

```text
phân phối sai số tương đối trên nhiều tập dữ liệu
kết quả sau gộp tương thích với kết quả xử lý một lượt trong dung sai
```

Count-Min Sketch:

```text
estimate >= true count trong mô hình cập nhật không âm
thống kê sai số phù hợp với tham số cấu hình
```

Bảo đảm thống kê phải được kiểm thử bằng tiêu chí thống kê, không phải bằng so sánh bằng tuyệt đối.

## 15. Mutation testing

Một cách đánh giá chất lượng test suite là cố tình đưa vào các lỗi nhỏ:

```text
< thành <=
quên size--
đảo comparator
bỏ một bước cập nhật
sai biên +1
```

Nếu toàn bộ test vẫn vượt qua, bộ kiểm thử đang thiếu khả năng phát hiện hành vi đó. **Mutation testing** đặc biệt hữu ích với DSA vì nhiều lỗi chỉ là một dòng nhưng phá bất biến sâu bên trong.

## 16. Benchmark khác kiểm thử ở mục tiêu

Kiểm thử hỏi đúng hay sai. Benchmark hỏi chi phí bao nhiêu.

Không nên đặt các hàm xác minh nặng vào bên trong vòng đo đường chạy nóng nếu chúng không thuộc tải công việc thật. Khâu chuẩn bị dữ liệu cũng cần tách ra nếu câu hỏi chỉ là chi phí của một thao tác cụ thể.

Ví dụ, nếu đo `HashMap.get`, nên tạo sẵn map trước khi bắt đầu tính giờ, trừ khi mục tiêu thật sự là đo cả quá trình xây dựng và tra cứu.

## 17. Đo ở nhiều quy mô

Nên tăng `n` theo cấp số nhân:

```text
1K, 2K, 4K, 8K, ...
```

Quan sát tỷ lệ thời gian khi tăng gấp đôi đầu vào:

```text
xấp xỉ 2 lần -> tín hiệu gần tuyến tính
xấp xỉ 4 lần -> tín hiệu gần bậc hai
hơn 2 lần một chút -> có thể là n log n hoặc hiệu ứng bộ nhớ
```

Đây không phải chứng minh Big-O, nhưng rất hữu ích để phát hiện suy giảm độ phức tạp ngoài ý muốn.

## 18. Hình dạng đầu vào là một chiều của benchmark

Hiệu năng Quicksort phụ thuộc cách chọn pivot và thứ tự đầu vào. Bảng băm phụ thuộc phân phối khóa. Thuật toán đồ thị phụ thuộc mật độ. DP phụ thuộc mật độ trạng thái đạt tới được.

Một bảng benchmark nên mô tả:

```text
kích thước
hình dạng / phân phối
hỗn hợp thao tác
tỷ lệ đọc/ghi
bộ nhớ đệm nóng/lạnh
```

Một tập dữ liệu ngẫu nhiên đồng đều duy nhất không đại diện cho mọi tải công việc.

## 19. Thông lượng và độ trễ

**Thông lượng (throughput)** thường đo số thao tác mỗi giây. **Độ trễ (latency)** đo thời gian cho một thao tác hoặc yêu cầu.

Một cấu trúc có thông lượng trung bình tốt vẫn có thể có p99 xấu do thay đổi kích thước hoặc GC. Chi phí khấu hao `O(1)` không bảo đảm mỗi thao tác đều có độ trễ hằng số.

Khi độ trễ đuôi quan trọng, nên đo:

```text
p50
p95
p99
max
```

## 20. Bộ nhớ đệm nóng và lạnh

Quét lặp lại cùng một mảng có thể chủ yếu đo trường hợp dữ liệu đã nằm trong cache. Điều này khác với lần truy cập đầu tiên hoặc tải công việc có tập dữ liệu lớn hơn LLC.

Cần xác định rõ đang đo:

```text
vòng lặp ổn định với cache nóng?
lần truy cập đầu tiên?
tập làm việc lớn hơn cache?
```

## 21. C: tối ưu hóa của trình biên dịch

Benchmark C với `-O0` không đại diện cho bản dựng production đã tối ưu. Cần ghi lại cờ biên dịch, phiên bản compiler và kiến trúc đích.

Compiler còn có thể loại bỏ phép tính nếu kết quả không quan sát được. Benchmark phải sử dụng kết quả hoặc dùng harness phù hợp để tránh đo “công việc đã bị tối ưu mất”.

Nếu chương trình có hành vi không xác định (undefined behavior), kết luận hiệu năng có thể hoàn toàn vô nghĩa vì optimizer được phép giả định UB không xảy ra.

## 22. C: bộ cấp phát là một phần của tải công việc

Danh sách liên kết gọi `malloc` cho từng nút đang đo cả thuật toán lẫn bộ cấp phát. Điều đó đúng nếu hệ thống thật cũng cấp phát như vậy.

Nếu muốn tách riêng chi phí duyệt, có thể cấp phát trước các nút. Nếu muốn so arena với `malloc`, thao tác cấp phát phải nằm trong vùng đo.

Không có benchmark “thuần cấu trúc dữ liệu” tách hoàn toàn khỏi cách biểu diễn nếu cấp phát chính là một phần của cách triển khai.

## 23. C: sanitizer và benchmark phải tách riêng

AddressSanitizer và UBSan rất hữu ích để tìm lỗi nhưng làm tăng chi phí đáng kể. Không nên dùng bản dựng có sanitizer để kết luận hiệu năng production.

Quy trình hợp lý:

```text
kiểm thử/fuzzing với sanitizer
benchmark bằng bản dựng tối ưu riêng
```

Tính đúng đắn trước, hiệu năng sau.

## 24. Java: làm nóng JIT

Java có biên dịch nhiều tầng và JIT. Những lần chạy đầu có thể đo nhiều chi phí khởi động, thông dịch và biên dịch hơn là trạng thái ổn định.

JMH hỗ trợ các khái niệm như:

```text
warmup iterations
measurement iterations
forks
blackholes
state scopes
```

Tự viết một vòng `System.nanoTime()` rất dễ gặp tối ưu loại mã chết, gộp hằng hoặc làm nóng không đủ.

## 25. Java: GC và tốc độ cấp phát

Hai thuật toán có độ trễ trung bình giống nhau có thể có tốc độ cấp phát rất khác. Cấp phát nhiều làm GC hoạt động nhiều hơn và có thể ảnh hưởng độ trễ đuôi.

Các chỉ số nên quan sát:

```text
bytes/op
allocations/op
GC count/time
peak/live heap
```

Mảng kiểu nguyên thủy và collection chứa object đóng hộp có thể tạo khác biệt lớn về bộ nhớ và GC.

## 26. Java: escape analysis và scalar replacement

JIT có thể loại bỏ một số cấp phát ngắn hạn nếu đối tượng không thoát khỏi phạm vi phân tích. Một microbenchmark quá nhân tạo có thể được tối ưu khác xa hệ thống thật, nơi object thoát qua collection hoặc API.

Benchmark nên mô phỏng vòng đời dữ liệu thật; không nên suy rộng quá xa từ một ví dụ nhỏ sang toàn bộ dịch vụ.

## 27. JavaScript: JIT và hình dạng dữ liệu

Engine JavaScript tối ưu dựa trên phản hồi khi chạy. Kiểu dữ liệu trộn lẫn, hình dạng object thay đổi, mảng thưa hoặc truy cập đa hình có thể làm mã nóng mất tối ưu.

Dữ liệu benchmark phải có hình dạng gần tải công việc thật. Một phép đo chỉ dùng mảng số dày đặc không đại diện cho hệ thống chứa object và chuỗi.

## 28. JavaScript: event loop và nhiễu bất đồng bộ

Nếu đo DSA thuần CPU trong Node.js hoặc trình duyệt, nên tách mạng, file, timer và các nguồn nhiễu khác càng nhiều càng tốt.

`async` không làm một thuật toán CPU-bound nhanh hơn; nó thay đổi cách lập lịch. Chỉ đưa thời gian chờ event loop vào benchmark nếu đó thực sự là một phần của tải công việc cần nghiên cứu.

## 29. JavaScript: độ phân giải thời gian

Thao tác quá nhanh cần được lặp theo lô để thời gian đo vượt nhiễu và độ phân giải của đồng hồ. Tuy nhiên, lặp quá nhiều có thể chuyển chương trình sang chế độ JIT hoặc GC khác.

Nên đo nhiều lần, bỏ giai đoạn làm nóng và xem phân phối kết quả thay vì chỉ lấy một lần chạy.

## 30. Benchmark đa ngôn ngữ phải định nghĩa câu hỏi trước

So C, Java và JavaScript có thể phục vụ hai mục tiêu khác nhau.

**So sánh thuật toán:** nên giữ cùng ngôn ngữ và môi trường để giảm nhiễu, tập trung vào khác biệt thuật toán.

**So sánh stack hệ thống:** chi phí runtime, GC, JIT và cách biểu diễn chính là một phần của câu trả lời.

Không nên từ một microbenchmark kết luận rằng “ngôn ngữ X nhanh hơn ngôn ngữ Y nói chung”. Kết luận hợp lệ phải gắn với:

```text
khối lượng công việc
cách triển khai
phiên bản runtime
phần cứng
cờ compiler
giới hạn bộ nhớ
```

## 31. Công bằng không có nghĩa là mã nguồn giống hệt

Java dùng `int[]`, JavaScript dùng `TypedArray` và C dùng mảng phẳng có thể là một so sánh công bằng hơn việc ép cả ba dùng cấu trúc object-heavy giống nhau về hình thức.

Phải nói rõ đang so **cách triển khai hợp lý nhất cho cùng ngữ nghĩa** hay **cùng một cấu trúc cấp cao được mô phỏng giống nhau**. Đây là hai câu hỏi nghiên cứu khác nhau.

## 32. Tính đúng đắn phải tương đương trước khi so hiệu năng

Trước khi đo thời gian giữa các ngôn ngữ, phải xác nhận đầu ra và miền số tương đương. Nếu C dùng số nguyên 64 bit còn JavaScript dùng `Number` đã mất độ chính xác, hai chương trình không còn giải cùng một bài toán về mặt ngữ nghĩa.

Tương tự, nếu quy tắc phá hòa hoặc tính ổn định khi sắp xếp khác nhau, hợp đồng đầu ra cũng khác.

## 33. Ngữ nghĩa số giữa các ngôn ngữ

C có thể có hành vi không xác định khi số nguyên có dấu tràn trong nhiều trường hợp. Java cho số nguyên tràn theo ngữ nghĩa two's complement. JavaScript `Number` là IEEE-754 double với giới hạn số nguyên an toàn.

Thuật toán đếm hoặc cộng khoảng cách phải dùng cách biểu diễn tương đương, hoặc tài liệu phải ghi rõ khác biệt ngữ nghĩa.

`BigInt` trong JavaScript và `BigInteger` trong Java cũng có chi phí khác đáng kể so với kiểu số nguyên nguyên thủy.

## 34. Dung lượng bộ nhớ thực tế giữa các ngôn ngữ

Một nút logic giống nhau có thể có chi phí khác:

```text
C    -> các trường struct + alignment + siêu dữ liệu allocator
Java -> object header + reference + ảnh hưởng GC
JS   -> object shape + vùng lưu thuộc tính của engine
```

Không thể chỉ đếm “một triệu nút” rồi kết luận bộ nhớ giống nhau. Nên đo lượng bộ nhớ thực tế. Mảng phẳng, `TypedArray` và mảng kiểu nguyên thủy thường cho cách so sánh bố trí dữ liệu rõ hơn đồ thị object.

## 35. CPU profiling

Khi benchmark cho kết quả bất ngờ, profiler giúp phân biệt thời gian đang nằm ở:

```text
công việc thuật toán
comparator
cấp phát
GC
hàm băm
cache miss
runtime helper
```

Tối ưu mà không profile rất dễ tập trung sai chỗ.

## 36. Bộ đếm phần cứng

Trong môi trường native hoặc nhạy về hiệu năng, các chỉ số như:

```text
cycles
instructions
cache misses
branch misses
```

có thể giải thích vì sao hai cách triển khai cùng `O(n)` lại chênh lệch mạnh. Mảng và danh sách liên kết là ví dụ điển hình do tính cục bộ bộ nhớ khác nhau.

## 37. Benchmark bộ nhớ

Biết rằng cấu trúc là `O(n)` chưa đủ vì hệ số hằng có thể rất lớn. Nên đo:

```text
peak RSS
live heap
allocation rate
bytes per element
spare capacity
fragmentation
```

Bảng băm có ô dự phòng, cây có con trỏ hoặc object header, còn danh sách kề bằng object có thể tốn nhiều hơn CSR dùng mảng phẳng.

## 38. Benchmark đầu-cuối

Một phép `heap.poll()` nhanh hơn 20% không chắc làm dịch vụ nhanh hơn nếu heap chỉ chiếm 1% thời gian xử lý yêu cầu.

Quyết định kiến trúc cần benchmark gần hệ thống thật, bao gồm khi phù hợp:

```text
tuần tự hóa
cơ sở dữ liệu / mạng
cấp phát
thuật toán
bộ nhớ đệm
tranh chấp tài nguyên
```

Profile trước khi tối ưu.

## 39. Benchmark xử lý đồng thời

Chi phí tuần tự không dự đoán trực tiếp thông lượng khi nhiều luồng cùng truy cập. Nên thay đổi:

```text
số luồng
tỷ lệ đọc/ghi
mức tranh chấp khóa
vị trí NUMA/lõi
kích thước vùng tới hạn
```

Một concurrent map có thể mở rộng tốt khi khóa phân tán nhưng sụp giảm hiệu năng khi mọi luồng cùng cập nhật một khóa hoặc một dòng cache.

Nên báo cáo đường cong thông lượng theo số luồng, không chỉ một kết quả ở 8 luồng.

## 40. Chia sẻ giả và tranh chấp dòng cache

Hai bộ đếm logic khác nhau nhưng nằm trên cùng một dòng cache có thể khiến các lõi liên tục chuyển quyền sở hữu dòng cache cho nhau. Đây là **chia sẻ giả (false sharing)**.

Khi benchmark mảng hoặc hàng đợi dùng đồng thời, cần cân nhắc padding và alignment nếu kết quả có dấu hiệu bất thường. Đây là hiệu ứng phần cứng nằm ngoài Big-O tuần tự nhưng có tác động thực tế lớn.

## 41. Kỷ luật thống kê trong benchmark

Không nên chỉ lấy một giá trị trung bình. Tùy mức độ quan trọng, có thể dùng:

```text
nhiều process/fork
nhiều mẫu
median và percentile
confidence interval
phân tích outlier
```

Bộ lập lịch hệ điều hành, giới hạn nhiệt, tiến trình nền và thay đổi tần số CPU đều tạo nhiễu. Không cần biến mọi benchmark thành nghiên cứu khoa học, nhưng phải đủ kỷ luật để tránh tự kết luận từ nhiễu.

## 42. Benchmark hồi quy

Benchmark hữu ích khi được chạy lặp lại qua commit hoặc release với ngưỡng hợp lý.

Ví dụ:

```text
thông lượng heap push không giảm quá 10%
bộ nhớ cực đại của graph parser không tăng quá 15%
```

Ngưỡng phải chừa khoảng cho nhiễu. Một microbenchmark quá chập chờn sẽ làm CI mất giá trị.

## 43. Kiểm tra hồi quy độ phức tạp

Có thể kiểm tra tỷ lệ tăng theo quy mô thay vì chỉ dùng số mili giây tuyệt đối.

Với thuật toán kỳ vọng gần tuyến tính:

```text
time(2n) / time(n)
```

không nên liên tục tiến gần 4 trong một miền `n` đủ lớn và ổn định. Cách này không chứng minh độ phức tạp nhưng có thể phát hiện vòng lặp lồng nhau ngoài ý muốn hoặc sao chép ẩn.

## 44. Benchmark đầu vào đối nghịch

Ngoài tải công việc trung bình, nên thử:

```text
tấn công va chạm băm
thứ tự bệnh lý cho Quicksort
cây/đồ thị rất sâu
rất nhiều phần tử trùng
ranh giới thay đổi dung lượng cực đại
```

Nếu API công khai hoặc hệ thống nhạy với độ trễ, hành vi trường hợp xấu nhất có thể trở thành vấn đề bảo mật hoặc độ tin cậy.

## 45. Báo cáo benchmark có thể tái hiện

Một báo cáo đáng tin nên ghi:

```text
CPU / số lõi
RAM
hệ điều hành
phiên bản compiler/runtime
các cờ biên dịch
chế độ GC nếu liên quan
commit SHA
bộ sinh đầu vào + seed
cấu hình warmup và measurement
```

Không có siêu dữ liệu, kết quả vài tháng sau gần như không thể kiểm tra lại.

## 46. Quy trình hoàn chỉnh

**Bước 1 — Đặc tả:** viết hợp đồng và giả định.

**Bước 2 — Chứng minh và suy luận:** xác định bất biến, tính đúng đắn và độ phức tạp.

**Bước 3 — Unit test:** kiểm tra trường hợp biên và ví dụ đã biết.

**Bước 4 — Kiểm thử đối chiếu/tính chất:** sinh nhiều trường hợp nhỏ và so với oracle.

**Bước 5 — Fuzzing/đối nghịch:** thử chuỗi thao tác dài và hình dạng khó.

**Bước 6 — Công cụ kiểm tra runtime:** sanitizer cho C, assertion, công cụ phát hiện race khi phù hợp.

**Bước 7 — Microbenchmark:** cô lập thao tác nguyên thủy cần đo.

**Bước 8 — Profiling:** tìm nút thắt thật.

**Bước 9 — Benchmark đầu-cuối:** dùng tải công việc gần hệ thống thực tế.

**Bước 10 — Tự động hóa hồi quy:** giữ tính đúng đắn và hiệu năng qua các thay đổi.

## 47. Ví dụ: hàng đợi ưu tiên tự cài đặt trên ba ngôn ngữ

Giả sử cùng cài heap nhị phân ở C, Java và JavaScript.

Kiểm thử tính đúng đắn:

```text
push/pop ngẫu nhiên và đối chiếu với danh sách đã sắp xếp
kiểm tra bất biến heap sau mỗi cập nhật
thử phần tử trùng
thử biên số và quy tắc phá hòa của comparator
```

Các chiều benchmark:

```text
n
tỷ lệ push:pop
payload kiểu nguyên thủy hay object
dữ liệu đã có thứ tự hay ngẫu nhiên
```

C cần xét chiến lược cấp phát, bố trí `struct` và cờ compiler. Java cần xét boxing, mảng kiểu nguyên thủy, JIT và GC. JavaScript cần xét `Number`/`BigInt`, `Array`/`TypedArray`, cấp phát tuple/object và độ ổn định hình dạng dữ liệu.

Đó mới là một so sánh có ý nghĩa; chạy một heap 1.000 phần tử đúng một lần là chưa đủ.

## 48. Các lỗi benchmark phổ biến

```text
đo bản dựng debug rồi suy ra production
vô tình đo cả bước chuẩn bị dữ liệu
không làm nóng JIT
để compiler loại bỏ công việc không quan sát được
mẫu đo quá ngắn
chỉ thử một kích thước đầu vào
không kiểm tra tính đúng đắn của kết quả
so các chương trình có ngữ nghĩa số khác nhau
kết luận từ một giá trị trung bình duy nhất
lấy microbenchmark để suy ra toàn bộ ứng dụng
```

## Mô hình tư duy

> **Chứng minh** giải thích vì sao thuật toán đúng và tăng trưởng ra sao. **Kiểm thử** cố phá cách triển khai. **Benchmark** đo chi phí thật dưới một tải công việc và môi trường cụ thể.

Ba lớp này phải liên kết với nhau nhưng không thay thế nhau. Một cách triển khai DSA tốt là nơi **hợp đồng toán học, kiểm thử có thể thực thi và số liệu hiệu năng thực nghiệm** cùng mô tả nhất quán một hệ thống.

Xem thêm: [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [C Implementation](./00_c_dsa_implementation_patterns.md), [Java Collections](./01_java_collections_and_dsa.md), [JavaScript Runtime](./02_javascript_dsa_runtime_patterns.md).