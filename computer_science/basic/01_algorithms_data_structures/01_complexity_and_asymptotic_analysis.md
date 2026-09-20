# Độ phức tạp thời gian, không gian và phân tích tiệm cận

Nếu hai thuật toán đều đúng, câu hỏi tiếp theo là chi phí của chúng tăng như thế nào khi đầu vào lớn dần. **Độ phức tạp tính toán (computational complexity / 계산 복잡도)** xây một mô hình đủ đơn giản để bỏ qua chi tiết của từng máy cụ thể nhưng vẫn giữ được tốc độ tăng chi phí theo kích thước đầu vào.

## Kích thước đầu vào là gì?

Trước khi nói `O(n)`, phải định nghĩa `n`. Với mảng, `n` thường là số phần tử. Với một số nguyên `N`, trong lý thuyết độ phức tạp kích thước đầu vào thường là số bit cần để biểu diễn `N`, xấp xỉ `log₂N`, chứ không phải chính giá trị `N`. Vì vậy một vòng lặp từ 1 tới `N` có thể là hàm mũ theo độ dài bit nếu `N` được nhập ở dạng nhị phân.

Chi tiết này dễ bị bỏ qua nhưng có thể làm phân loại độ phức tạp sai hoàn toàn.

## Mô hình chi phí

Mô hình RAM thường giả định các thao tác cơ bản như đọc hoặc ghi một từ máy và phép số học đơn giản có chi phí hằng số. Đây là một phép xấp xỉ. Số nguyên lớn, trượt cache, I/O đĩa và vòng khứ hồi mạng không thật sự có chi phí hằng số.

Mô hình không “sai”; nó chỉ có phạm vi áp dụng. Khi tốc độ tăng của thuật toán là yếu tố chính, mô hình RAM rất hữu ích. Khi hiệu năng phụ thuộc mạnh vào phân cấp bộ nhớ hoặc I/O, cần mô hình giàu chi tiết hơn.

## Big O, Big Theta và Big Omega

Big O mô tả **cận trên tiệm cận (asymptotic upper bound)**. `T(n) ∈ O(f(n))` nếu tồn tại các hằng số `c, n₀` sao cho `T(n) ≤ c f(n)` với mọi `n ≥ n₀`.

Big Ω mô tả cận dưới; Big Θ mô tả cận chặt khi cận trên và cận dưới cùng bậc. Vì vậy nói merge sort ở trường hợp xấu nhất có `Θ(n log n)` chính xác hơn chỉ nói `O(n log n)`, dù trong kỹ thuật thực tế Big O thường được dùng rộng để nói về bậc tăng trưởng.

Các hệ số và hạng bậc thấp bị bỏ qua vì phân tích tiệm cận quan tâm hình dạng khi `n` lớn. `3n² + 10n + 100` thuộc `Θ(n²)`.

## Các tốc độ tăng thường gặp

`O(1)` không có nghĩa là “một lệnh”; nó nghĩa chi phí không tăng theo `n` trong mô hình đang dùng. `O(log n)` thường xuất hiện khi mỗi bước giảm không gian tìm kiếm theo một tỷ lệ cố định. `O(n)` thường là quét đầu vào một lần. `O(n log n)` phổ biến ở sắp xếp dựa trên so sánh tối ưu. `O(n²)` xuất hiện khi xét mọi cặp. Hàm mũ `O(2^n)` và giai thừa tăng cực nhanh.

Logarithm xuất hiện tự nhiên khi liên tục chia đôi. Nếu sau `k` bước còn `n/2^k = 1`, thì `k = log₂n`.

Xem toán sâu hơn tại [Algorithms, Complexity và Logarithms](../../mathematics/07_discrete_cs/01_algorithms_complexity_and_logarithms.md).

## Trường hợp xấu nhất, trung bình và tốt nhất

Bảo đảm trường hợp xấu nhất quan trọng trong hệ thống nhạy độ trễ hoặc có đầu vào đối kháng. Trường hợp trung bình cần một phân bố xác suất của đầu vào; nếu giả định về phân bố sai, kết luận có thể không còn ý nghĩa. Trường hợp tốt nhất ít hữu ích cho bảo đảm nhưng vẫn giúp hiểu hành vi.

Tra cứu bảng băm có chi phí kỳ vọng hoặc khấu hao gần `O(1)` khi hàm băm tốt và hệ số tải hợp lý, nhưng trường hợp xấu nhất có thể là `O(n)`. Cây tìm kiếm cân bằng có thể bảo đảm tra cứu `O(log n)`. Lựa chọn phụ thuộc loại bảo đảm mà hệ thống cần.

## Phân tích khấu hao

Một thao tác có thể đôi lúc rất đắt nhưng xảy ra hiếm. Thêm phần tử vào mảng động thường có chi phí hằng số; khi hết dung lượng phải cấp mảng lớn hơn và sao chép nhiều phần tử. Nếu dung lượng tăng theo một hệ số cố định, tổng số phần tử được sao chép qua `n` lần thêm vẫn là `O(n)`, nên chi phí khấu hao cho mỗi lần thêm là `O(1)`.

**Phân tích khấu hao (amortized analysis)** không phải trung bình theo đầu vào ngẫu nhiên. Nó là bảo đảm trung bình trên một chuỗi thao tác và thường không cần giả định xác suất.

## Độ phức tạp không gian và đánh đổi thời gian–bộ nhớ

Ghi nhớ kết quả (memoization) dùng thêm bộ nhớ để tránh tính lại. Chỉ mục băm dùng dung lượng lưu trữ để giảm thời gian truy vấn. Cache dùng RAM để giảm I/O. Bloom filter chấp nhận xác suất dương tính giả để tiết kiệm không gian.

Vì vậy thời gian và không gian không độc lập. Nhiều thiết kế thực tế chỉ là chuyển chi phí từ tài nguyên này sang tài nguyên khác.

## Cận dưới

Không phải cứ viết mã thông minh hơn là vượt được mọi giới hạn. Sắp xếp dựa trên so sánh có cận dưới `Ω(n log n)` trong mô hình so sánh vì phải phân biệt `n!` thứ tự có thể có, trong khi mỗi phép so sánh nhị phân chỉ cung cấp lượng thông tin hữu hạn.

Counting sort có thể đạt `O(n+k)` vì nó không bị giới hạn bởi mô hình so sánh; nó khai thác việc khóa nằm trong một miền hữu hạn. Vì vậy cận dưới luôn gắn với giả định và mô hình cụ thể.

## Độ phức tạp và hiệu năng thực tế

Chèn vào danh sách liên kết có thể là `O(1)` nếu đã có con trỏ đúng vị trí, nhưng việc duyệt và tính cục bộ kém có thể khiến nó chậm hơn cấu trúc dựa trên mảng. Quét liên tục `O(n)` có thể rất nhanh nhờ cache và nạp trước. Tra cứu B-tree `O(log n)` trong cơ sở dữ liệu có thể bị độ trễ đĩa hoặc mạng chi phối.

Phân tích tiệm cận trả lời “chi phí tăng theo quy mô thế nào”. Đo hiệu năng trả lời “trên cách triển khai, tải và phần cứng này nhanh đến đâu”. Cả hai đều cần thiết.

## Độ phức tạp của thuật toán đệ quy

Quan hệ truy hồi mô tả chi phí qua các bài toán con. Với merge sort:

\[
T(n)=2T(n/2)+\Theta(n)
\]

Hai bài toán con kích thước `n/2` và bước trộn tuyến tính dẫn tới `Θ(n log n)`. Có thể hình dung bằng cây đệ quy: mỗi tầng có tổng lượng công việc xấp xỉ `n`, và có khoảng `log n` tầng.

## Mô hình tư duy

> Độ phức tạp mô tả **hình dạng của chi phí khi quy mô tăng**, không phải đồng hồ bấm giờ. Luôn hỏi: `n` là gì, mô hình chi phí là gì, đang nói trường hợp nào và giả định nào làm cận đó đúng?

## Những hiểu nhầm thường gặp

**“O(1) luôn nhanh hơn O(n).”** Không nhất thiết khi `n` nhỏ hoặc hệ số và phần cứng khác nhau. Big O nói về tốc độ tăng tiệm cận.

**“O(n) nghĩa chính xác n thao tác.”** Không đúng. Nó mô tả lớp tăng trưởng bậc tuyến tính.

**“Tra cứu hash trung bình O(1) nghĩa trường hợp xấu nhất cũng O(1).”** Không đúng. Va chạm và đầu vào đối kháng có thể làm chuỗi hoặc quá trình dò dài.

## Kết nối

[Phân bố bộ nhớ](./02_memory_models_and_data_layout.md) giải thích hệ số thực tế và tính cục bộ; [hiệu năng và năng lực xử lý](../08_software_systems/02_performance_capacity_and_scalability.md) mở rộng từ một thuật toán sang hệ thống đầu-cuối có hàng đợi, I/O và đồng thời.
