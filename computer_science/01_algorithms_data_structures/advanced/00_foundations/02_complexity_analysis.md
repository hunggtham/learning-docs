# Phân tích độ phức tạp
**Complexity Analysis / 복잡도 분석**

Độ phức tạp mô tả cách lượng tài nguyên cần thiết tăng theo kích thước đầu vào. Hai tài nguyên được nhắc đến nhiều nhất là **độ phức tạp thời gian (time complexity / 시간 복잡도)** và **độ phức tạp không gian (space complexity / 공간 복잡도)**. Trong hệ thống thực tế, ta còn phải quan tâm đến số lần I/O, số lần trượt bộ nhớ đệm (cache miss), số lượt trao đổi qua mạng (network round-trip), số lần cấp phát bộ nhớ, dự đoán sai nhánh và chi phí đồng bộ hóa (synchronization). Vì vậy, phân tích độ phức tạp không phải là một bảng Big-O để học thuộc mà là một **mô hình tăng trưởng** giúp dự đoán một thiết kế sẽ hoạt động ra sao khi dữ liệu lớn dần.

Một phép đo hiệu năng cho kết quả 2 ms ở hiện tại không trả lời được câu hỏi “điều gì xảy ra khi đầu vào tăng 100 lần?”. Phân tích độ phức tạp cố gắng trả lời câu hỏi đó bằng cách tạm bỏ qua nhiều chi tiết phần cứng và tập trung vào cấu trúc của quá trình tính toán.

## 1. Tại sao không chỉ đo thời gian thực thi?

Giả sử hai cách triển khai cùng xử lý `n = 1_000` trong thời gian tương tự. Một cách có chi phí gần tỷ lệ với `n`, cách còn lại gần tỷ lệ với `n²`. Với đầu vào nhỏ, hệ số hằng và hiệu ứng bộ nhớ đệm có thể che khuất khác biệt. Khi `n` tăng 100 lần, thuật toán tuyến tính tăng khoảng 100 lần, còn thuật toán bậc hai có thể tăng khoảng 10.000 lần.

Nếu thời gian chạy có dạng:

\[
T(n)=3n^2+5n+20
\]

thì khi `n` đủ lớn, hạng tử `n²` chi phối. Ta nói `T(n)=O(n²)`. Nếu cận trên và cận dưới có cùng bậc tăng trưởng, ta dùng `Θ(n²)`. Ký hiệu `Ω` diễn tả cận dưới.

Các ký hiệu này không phải ba cách nói cùng một điều:

- `O(f(n))` cho biết chi phí không tăng nhanh hơn một hằng số nhân với `f(n)` sau một ngưỡng nào đó;
- `Ω(f(n))` cho biết chi phí không tăng chậm hơn một hằng số nhân với `f(n)`;
- `Θ(f(n))` cho biết tốc độ tăng trưởng bị kẹp giữa cận trên và cận dưới cùng bậc.

Trong trao đổi kỹ thuật, Big-O đôi khi được dùng tương đối lỏng để chỉ **bậc tăng trưởng (order of growth)**. Khi cần lập luận chặt chẽ, phải phân biệt rõ đang nói về cận trên, cận dưới hay cận chặt.

## 2. Tốc độ tăng trưởng quan trọng hơn độ dài mã nguồn

Một hàm 5 dòng có thể có độ phức tạp `O(n²)`, trong khi một hàm 100 dòng có thể chỉ là `O(n)`. Độ phức tạp không đo số dòng mã nguồn mà đo **số thao tác hoặc lượng trạng thái cần xử lý tăng như thế nào theo đầu vào**.

Các bậc tăng trưởng phổ biến:

| Độ phức tạp | Mô hình tư duy |
|---|---|
| `O(1)` | chi phí không tăng theo `n` |
| `O(log n)` | mỗi bước loại bỏ hoặc gộp một tỷ lệ cố định của không gian tìm kiếm |
| `O(n)` | duyệt qua dữ liệu một số lần cố định |
| `O(n log n)` | có khoảng `log n` tầng và tổng công việc ở mỗi tầng là tuyến tính |
| `O(n²)` | thường xuất hiện khi xét tương tác theo cặp hoặc hai chiều trạng thái |
| `O(2^n)` | mỗi phần tử có thể mở thêm một lựa chọn nhị phân |
| `O(n!)` | phải xét các hoán vị của `n` phần tử |

Tìm kiếm nhị phân giảm khoảng tìm kiếm còn một nửa sau mỗi bước:

\[
n,\frac n2,\frac n4,\ldots,1
\]

Sau `k` bước:

\[
\frac{n}{2^k}=1 \Rightarrow k=\log_2 n
\]

`log n` xuất hiện vì mỗi bước thu nhỏ phần còn lại theo một tỷ lệ cố định, chứ không phải vì “tìm kiếm nhị phân mặc nhiên có log”.

## 3. Kích thước đầu vào không phải lúc nào cũng chỉ là `n`

Đồ thị thường cần hai biến `V` và `E`. Ma trận có thể cần `R` và `C`. Thuật toán chuỗi có thể phụ thuộc vào `n + m`. Hiệu năng của bảng băm (Hash Table) còn phụ thuộc vào hệ số tải (load factor). Bài toán Knapsack có `n` vật phẩm và sức chứa `W`.

Ví dụ, BFS dùng danh sách kề có độ phức tạp:

\[
O(V+E)
\]

Không nên tùy tiện rút gọn thành `O(n)` nếu việc đó làm mất thông tin quan trọng về mật độ đồ thị.

Với đồ thị thưa (sparse graph), thường `E≈V`; với đồ thị dày (dense graph), `E` có thể gần `V²`. Cùng một công thức `O(V+E)` nhưng hành vi thực tế có thể rất khác giữa hai trường hợp.

## 4. Trường hợp tốt nhất, trung bình, kỳ vọng và xấu nhất

Các khái niệm này thường bị dùng lẫn lộn nhưng có ý nghĩa khác nhau.

Tìm kiếm tuyến tính có trường hợp tốt nhất `O(1)` nếu phần tử cần tìm nằm ngay đầu mảng, và trường hợp xấu nhất `O(n)` nếu phần tử ở cuối hoặc không tồn tại. Trường hợp trung bình chỉ có ý nghĩa khi ta xác định được phân phối của đầu vào hoặc vị trí phần tử cần tìm.

**Độ phức tạp kỳ vọng (expected complexity)** thường xuất hiện khi thuật toán hoặc cấu trúc dữ liệu sử dụng tính ngẫu nhiên. Quickselect ngẫu nhiên có thời gian kỳ vọng tuyến tính dưới các giả định phân tích chuẩn. Bảng băm có thời gian tra cứu kỳ vọng gần `O(1)` khi hàm băm phân phối khóa đủ tốt.

Giá trị kỳ vọng không có nghĩa là “đa số trường hợp đều bằng đúng giá trị trung bình”. Một phân phối có thể có trung bình tốt nhưng phần đuôi rất xấu. Trong hệ thống nhạy với độ trễ, các phân vị p95/p99 và những đợt tăng đột biến ở trường hợp xấu nhất có thể quan trọng hơn giá trị kỳ vọng.

## 5. Chi phí khấu hao không phải chi phí trung bình

Phép thêm cuối vào mảng động thường được mô tả là có chi phí khấu hao (amortized cost) `O(1)`. Kết quả này không dựa vào phân phối ngẫu nhiên của đầu vào. Nó nói rằng trên một **chuỗi thao tác đủ dài**, tổng chi phí bị chặn tuyến tính theo số thao tác nếu chính sách tăng dung lượng phù hợp.

Nếu dung lượng tăng gấp đôi:

```text
1 -> 2 -> 4 -> 8 -> ...
```

thì tổng số phần tử phải sao chép qua các lần thay đổi kích thước là:

\[
1+2+4+\cdots+\frac n2 < n
\]

Do đó `n` lần thêm cuối có tổng chi phí `O(n)`, tương đương chi phí khấu hao `O(1)` cho mỗi lần thêm.

Một lần thêm riêng lẻ vẫn có thể tốn `O(n)` khi phải thay đổi kích thước mảng. Đây là khác biệt quan trọng trong hệ thống thời gian thực: thông lượng khấu hao tốt không đồng nghĩa với độ trễ đuôi thấp.

## 6. Ba cách phân tích chi phí khấu hao

Có ba phương pháp kinh điển.

**Phương pháp tổng hợp (aggregate method)** tính tổng chi phí của cả chuỗi thao tác rồi chia cho số thao tác.

**Phương pháp hạch toán (accounting method)** gán chi phí quy ước cao hơn cho một số thao tác rẻ để tích lũy “tín dụng”, sau đó dùng phần tín dụng này trả cho thao tác đắt hơn.

**Phương pháp thế năng (potential method)** định nghĩa hàm thế năng `Φ(state)` đại diện cho lượng công việc đã được “tích trữ” trong trạng thái của cấu trúc. Chi phí khấu hao thường được viết:

\[
\hat c_i = c_i + \Phi(D_i)-\Phi(D_{i-1})
\]

Mảng động, thao tác `multipop` trên ngăn xếp, cây Splay và một số phân tích của cấu trúc hợp nhất–tìm kiếm (Union-Find) đều có thể được hiểu rõ hơn bằng các phương pháp này.

## 7. Phân tích vòng lặp từ quy tắc cập nhật, không từ số tầng thụt lề

Các vòng lặp lồng nhau không tự động có độ phức tạp `O(n²)`.

```java
for (int i = 0; i < n; i++) {
    for (int j = 1; j < n; j *= 2) {
        consume(i, j);
    }
}
```

Vòng ngoài chạy `n` lần, vòng trong chạy khoảng `log n` lần, nên tổng chi phí là:

\[
\Theta(n\log n)
\]

Ngược lại, một vòng lặp đơn cũng có thể chứa thao tác ẩn có chi phí `O(n)`, chẳng hạn xóa phần tử đầu của mảng động, nối chuỗi theo cách phải sao chép toàn bộ tiền tố, hoặc gọi `LinkedList.get(i)` lặp đi lặp lại.

Nguyên tắc đúng là: **phân tích chi phí của từng thao tác nguyên thủy hoặc API được gọi, sau đó cộng hoặc nhân chi phí theo luồng điều khiển (control flow)**.

## 8. Phép tổng là công cụ phân tích quan trọng

Vòng lặp:

```c
for (int i = 0; i < n; ++i)
    for (int j = 0; j <= i; ++j)
        work();
```

thực hiện số thao tác:

\[
1+2+\cdots+n=\frac{n(n+1)}2=\Theta(n^2)
\]

Một mẫu khác:

\[
1+2+4+8+\cdots+n=\Theta(n)
\]

Đây là lý do một số thuật toán có số thao tác ở từng giai đoạn tăng theo lũy thừa của hai nhưng tổng công việc vẫn chỉ tuyến tính.

Phân tích độ phức tạp thường là quá trình nhận ra dãy hoặc phép tổng đang ẩn trong mã nguồn.

## 9. Công thức truy hồi cho thuật toán đệ quy

Sắp xếp trộn (Merge Sort) có công thức:

\[
T(n)=2T(n/2)+\Theta(n)
\]

Mỗi tầng có tổng công việc `Θ(n)` và có `Θ(log n)` tầng, nên:

\[
T(n)=\Theta(n\log n)
\]

Tìm kiếm nhị phân có:

\[
T(n)=T(n/2)+\Theta(1)=\Theta(\log n)
\]

Quicksort trong trường hợp xấu nhất có:

\[
T(n)=T(n-1)+\Theta(n)=\Theta(n^2)
\]

Định lý Master là công cụ rút gọn cho một họ công thức truy hồi. Tuy nhiên, cây đệ quy hoặc phương pháp thế (substitution) thường cho trực giác rõ hơn khi kích thước các bài toán con không đều nhau.

## 10. Độ phức tạp không gian: bộ nhớ sống khác tổng lượng cấp phát

Một thuật toán có thể cấp phát tổng cộng rất nhiều byte trong suốt quá trình chạy nhưng lượng bộ nhớ tồn tại đồng thời ở thời điểm cực đại vẫn nhỏ nếu bộ nhớ được thu hồi dần. Khi nói bộ nhớ phụ trợ là `O(n)`, ta thường quan tâm đến **lượng bộ nhớ phụ trợ còn sống đồng thời**, không phải tổng số byte từng được xin từ bộ cấp phát.

DFS đệ quy trên cây có chiều cao `h` dùng ngăn xếp lời gọi `O(h)`. Merge Sort trên mảng thường cần bộ đệm phụ trợ `O(n)`. Quicksort tại chỗ (in-place) dùng ít dữ liệu phụ trợ, nhưng ngăn xếp đệ quy có độ sâu kỳ vọng `O(log n)` và có thể đạt `O(n)` trong trường hợp xấu nhất.

Trong môi trường có bộ thu gom rác (GC), **tốc độ cấp phát (allocation rate)** và **lượng bộ nhớ được giữ lại (retained memory)** là hai chỉ số khác nhau. Nhiều đối tượng tạm thời có thể gây áp lực lên GC dù kích thước cấu trúc dữ liệu sống tại một thời điểm không lớn.

## 11. Độ phức tạp nhạy theo kích thước đầu ra

Nếu bản thân đầu ra có `k` phần tử, thuật toán phải tốn ít nhất `Ω(k)` chỉ để tạo hoặc xuất các phần tử đó. Vì vậy, truy vấn khoảng (range query) hoặc một số thuật toán hình học thường có độ phức tạp dạng:

\[
O(f(n)+k)
\]

Cây tìm kiếm nhị phân cân bằng có thể trả lời truy vấn khoảng trong `O(log n + k)`. Một phép duyệt đồ thị cần liệt kê mọi cạnh phải tốn ít nhất `Ω(E)`.

Góc nhìn này giúp tránh những mục tiêu bất khả thi như “liệt kê một triệu kết quả trong `O(log n)`”.

## 12. Độ phức tạp phụ thuộc đặc điểm đầu vào

Một số thuật toán chạy nhanh hơn đáng kể khi đầu vào có cấu trúc thuận lợi. Insertion Sort có thể gần `O(n)` khi dữ liệu gần như đã được sắp xếp. Timsort khai thác các đoạn đã có thứ tự (runs) trong dữ liệu. Hiệu năng của Union-Find phụ thuộc chuỗi thao tác nhưng vẫn có cận khấu hao rất mạnh.

Nếu hiệu năng phụ thuộc vào các tham số như **mức độ mất trật tự**, **số nghịch thế (number of inversions)**, chiều cao cây hoặc số khóa phân biệt, nên giữ các tham số đó trong phân tích thay vì ép mọi thứ về một biến `n`.

## 13. Độ phức tạp giả đa thức và độ dài biểu diễn

Quy hoạch động cho Knapsack có độ phức tạp `O(nW)` với sức chứa `W`. Công thức này trông giống đa thức, nhưng chỉ cần `O(log W)` bit để biểu diễn giá trị `W`. Vì vậy, nếu đo theo độ dài biểu diễn của đầu vào, `O(nW)` có thể tăng theo hàm mũ. Loại độ phức tạp này được gọi là **thời gian giả đa thức (pseudopolynomial time / 의사 다항 시간)**.

Sự phân biệt này quan trọng khi chuyển từ thiết kế thuật toán sang lý thuyết độ phức tạp: “đa thức theo giá trị số” không đồng nghĩa với “đa thức theo độ dài mã hóa của đầu vào”.

## 14. Mô hình so sánh và cận dưới

Thuật toán sắp xếp dựa trên so sánh phải phân biệt `n!` hoán vị có thể có của đầu vào. Mỗi phép so sánh chỉ cho một số hữu hạn kết quả, vì vậy cây quyết định (decision tree) phải có độ sâu ít nhất:

\[
\Omega(\log(n!))=\Omega(n\log n)
\]

Đây là lý do không thể có thuật toán sắp xếp tổng quát chỉ dựa trên so sánh với độ phức tạp `o(n log n)` trong trường hợp xấu nhất.

Counting Sort và Radix Sort không vi phạm cận này vì chúng khai thác thông tin khác ngoài phép so sánh từng cặp, chẳng hạn cách biểu diễn khóa và miền giá trị của khóa.

Cận dưới giúp ta nhận ra khi nào phải thay đổi mô hình bài toán thay vì tiếp tục cố tối ưu mã nguồn trong một mô hình vốn đã đạt giới hạn lý thuyết.

## 15. Độ phức tạp là một phần của hợp đồng API

Lớp trừu tượng của thư viện (library abstraction) không làm biến mất mô hình chi phí.

Trong Java, `ArrayList.get(i)` gần `O(1)` còn `LinkedList.get(i)` là `O(n)`. Trong JavaScript, `Array.shift()` có thể phát sinh chi phí đánh lại chỉ số hoặc nén mảng; `push()` và `pop()` ở cuối thường phù hợp hơn khi dùng mảng làm ngăn xếp. `HashMap` có thời gian tra cứu kỳ vọng nhanh, còn `TreeMap` duy trì thứ tự với chi phí `O(log n)`.

Một lần tái cấu trúc chỉ thay cách triển khai tập hợp dữ liệu cũng có thể làm thay đổi bậc độ phức tạp của toàn hàm dù logic nghiệp vụ không đổi.

Vì vậy, độ phức tạp nên được xem là một phần của **hợp đồng kỹ thuật của API**.

## 16. Phân cấp bộ nhớ và ảnh hưởng của bộ nhớ đệm

Hai thuật toán cùng có độ phức tạp `O(n)` vẫn có thể chênh lệch hiệu năng lớn nếu một thuật toán quét vùng nhớ liên tiếp còn thuật toán kia phải lần theo các con trỏ nằm rải rác.

```text
array scan       -> spatial locality, prefetch-friendly
linked traversal -> random-ish addresses, cache-miss prone
```

Trong **mô hình bộ nhớ ngoài (external-memory model)**, đôi khi ta đếm số lần truyền các khối dữ liệu thay vì số thao tác CPU. B-Tree tối ưu chiều cao theo hệ số phân nhánh của trang vì I/O theo đĩa hoặc trang thường đắt hơn nhiều so với một phép so sánh.

Mô hình RAM tiệm cận vẫn rất hữu ích, nhưng khi phân tích hệ thống thực tế cần xét thêm tính cục bộ (locality) và chi phí di chuyển dữ liệu giữa các tầng bộ nhớ.

## 17. CPU, dự đoán nhánh và vector hóa

Một thuật toán có nhiều nhánh phụ thuộc dữ liệu khó dự đoán có thể chậm hơn một phép quét tuyến tính đơn giản dù số lượng thao tác tương đương. Các mảng số nằm liên tiếp trong bộ nhớ còn có thể tận dụng **vector hóa (vectorization)** hoặc SIMD.

Điều này giải thích vì sao tìm kiếm nhị phân với ít phép so sánh chưa chắc nhanh hơn quét tuyến tính trên mảng rất nhỏ: chi phí phụ của dự đoán nhánh và bộ nhớ đệm có thể chi phối các hệ số hằng.

Big-O mô tả hình dạng tăng trưởng khi quy mô thay đổi; **vi kiến trúc (microarchitecture)** quyết định nhiều hệ số hằng trong thực tế.

## 18. Độ trễ đuôi và các loại bảo đảm

Trong xử lý theo lô, thông lượng trung bình thường quan trọng. Trong bộ lập lịch, giao dịch, âm thanh hoặc hệ thống phục vụ yêu cầu, chỉ một đợt tăng độ trễ cũng có thể làm lỡ thời hạn.

Mảng động có phép thêm cuối với chi phí khấu hao `O(1)` nhưng một lần thay đổi kích thước có thể tốn `O(n)`. Bảng băm có thể thực hiện băm lại theo từng bước để phân tán chi phí thay vì dồn toàn bộ vào một lần. Hàng đợi thời gian thực có thể ưu tiên bộ đệm vòng với dung lượng cố định để tránh các đợt cấp phát đột biến.

Khi yêu cầu liên quan đến độ trễ trong trường hợp xấu nhất, cần phân biệt:

```text
expected bound          -> cận kỳ vọng
amortized bound         -> cận khấu hao
worst-case bound        -> cận trường hợp xấu nhất
high-probability bound  -> cận đúng với xác suất cao
```

Các loại bảo đảm này không thể thay thế lẫn nhau.

## 19. Đồng thời làm thay đổi mô hình chi phí

Một ánh xạ dùng đồng thời (concurrent map) không chỉ có chi phí `get/put` phụ thuộc số phần tử. Tranh chấp tài nguyên, việc một dòng bộ nhớ đệm liên tục chuyển giữa các lõi (cache-line bouncing), đoàn khóa (lock convoy), số lần thử lại và hàng rào bộ nhớ (memory fence) có thể trở thành nút thắt hiệu năng.

Một vòng lặp nguyên tử có độ phức tạp lý thuyết `O(1)` vẫn có thể chậm khi nhiều luồng cùng tranh chấp một trạng thái. Vì vậy, độ phức tạp của thuật toán tuần tự chỉ là đường cơ sở, không phải toàn bộ mô hình hiệu năng khi chạy đồng thời.

## 20. Độ phức tạp trong hệ thống phân tán

Trong hệ thống phân tán, một lượt trao đổi qua mạng có thể đắt hơn hàng triệu lệnh CPU. Một thuật toán `O(log n)` nhưng cần nhiều RPC nối tiếp có thể chậm hơn một thao tác theo lô `O(n)` được xử lý cục bộ.

Vì vậy, đôi khi cần mô tả chi phí theo nhiều chiều:

```text
CPU work                 -> lượng công việc CPU
memory                   -> bộ nhớ
number of disk I/Os      -> số lần I/O đĩa
number of network rounds -> số vòng trao đổi mạng
bytes transferred        -> số byte được truyền
```

MapReduce, sắp xếp phân tán, lập kế hoạch truy vấn cơ sở dữ liệu và xử lý đồ thị thường phải tối ưu chi phí truyền thông không kém chi phí CPU.

## 21. Đo hiệu năng để kiểm chứng, không thay thế phân tích

Một quy trình tốt thường gồm:

1. phân tích tốc độ tăng trưởng tiệm cận;
2. xác định các tham số ẩn và giả định;
3. đo trên nhiều kích thước đầu vào;
4. kiểm tra bộ nhớ, cấp phát và tính cục bộ;
5. dùng công cụ định hình hiệu năng (profiler) để tìm đường chạy nóng;
6. đo trên khối lượng công việc gần với hệ thống thực tế.

Nếu đường cong thời gian chạy không giống dự đoán lý thuyết, hãy kiểm tra hệ số hằng, JIT/GC, bộ nhớ đệm, tối ưu hóa của trình biên dịch, miền kích thước đầu vào hoặc lỗi trong phép đo trước khi kết luận rằng phân tích độ phức tạp sai.

## 22. Ví dụ: chọn cấu trúc cho dịch vụ tra cứu

Giả sử hệ thống có 10 triệu bản ghi với khối lượng công việc:

```text
95% exact lookup by id -> tra cứu chính xác theo id
4% insert/update       -> chèn hoặc cập nhật
1% range scan          -> quét theo khoảng
```

Bảng băm có thời gian tra cứu kỳ vọng tốt nhưng không hỗ trợ quét theo thứ tự trên một khoảng. Cây cân bằng có tra cứu `O(log n)` nhưng hỗ trợ thao tác theo khoảng tốt hơn. Trong thực tế, có thể dùng bảng băm cho các tra cứu chính xác thường xuyên và một chỉ mục có thứ tự riêng cho truy vấn khoảng, hoặc để hệ quản trị cơ sở dữ liệu quản lý cả hai đường truy cập.

Phân tích độ phức tạp không tự chọn cấu trúc thay ta; nó giúp định lượng **sự đánh đổi (trade-off)** theo khối lượng công việc.

## 23. Danh sách kiểm tra khi phân tích độ phức tạp

Khi nhìn một thuật toán, hãy lần lượt hỏi:

```text
Kích thước đầu vào được đo bằng những biến nào?
Thao tác nguyên thủy nào thực sự tạo ra chi phí?
Biến vòng lặp tăng theo +1, nhân 2 hay phụ thuộc dữ liệu?
Các bài toán con đệ quy có kích thước và số lượng ra sao?
Kích thước đầu ra có tạo thành một cận dưới không?
Có bảo đảm khấu hao, kỳ vọng hoặc ngẫu nhiên hóa nào không?
Bộ nhớ cực đại hay tốc độ cấp phát quan trọng hơn?
Cách biểu diễn dữ liệu ảnh hưởng đến tính cục bộ như thế nào?
Lời gọi API/thư viện có ẩn thao tác duyệt hoặc sao chép không?
Hệ thống thực tế cần thông lượng trung bình hay độ trễ trường hợp xấu nhất?
```

## Mô hình tư duy

> Phân tích độ phức tạp là nghệ thuật xây dựng **một mô hình chi phí đủ đơn giản để suy luận nhưng đủ sát thực tế để hướng dẫn thiết kế**.

Big-O cho biết hình dạng tăng trưởng. Phân tích khấu hao, kỳ vọng và trường hợp xấu nhất cho biết loại bảo đảm. Bộ nhớ đệm, cấp phát, I/O và tranh chấp tài nguyên bổ sung lớp mô hình thực tế hơn. Cuối cùng, phép đo hiệu năng xác nhận cách triển khai trên khối lượng công việc thật.

Xem thêm: [Mathematical Toolkit](./04_mathematical_toolkit_for_dsa.md), [Memory Models](./03_memory_models_c_java_javascript.md), [Testing & Benchmarking](../80_language_implementations/03_cross_language_testing_and_benchmarking.md).