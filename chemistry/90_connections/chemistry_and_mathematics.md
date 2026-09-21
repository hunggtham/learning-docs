# Hóa học và Toán học — toán học là ngôn ngữ của quan hệ hóa học

> Toán học không chỉ xuất hiện sau khi ta đã “hiểu Hóa học” để thay số vào công thức. Nhiều khái niệm hóa học thực chất chính là **các quan hệ toán học giữa những đại lượng đo được**. Hiểu được cấu trúc toán học thường giúp ta suy luận lại công thức thay vì học thuộc.

## Đại số và phân tích thứ nguyên

Hóa lượng, nồng độ và định luật khí dựa mạnh vào tỉ lệ, đại số và đơn vị.

**Phân tích thứ nguyên (dimensional analysis)** có thể xem như đại số trong đó mỗi đại lượng mang theo kiểu dữ liệu vật lý. Nếu đơn vị cuối cùng không khớp với đại lượng cần tìm, quá trình suy luận gần như chắc chắn có lỗi.

Phương trình hóa học cân bằng cũng có thể được viết thành hệ ràng buộc tuyến tính dựa trên bảo toàn nguyên tố. Khi số chất tăng, bài toán cân bằng có thể được giải như bài toán tìm vector trong không gian nghiệm của ma trận thành phần.

## Logarithm

`pH`, `pKa`, hằng số cân bằng và nhiều đại lượng hóa học trải qua nhiều bậc độ lớn nên logarithm là công cụ tự nhiên để nén thang giá trị.

\[
pH=-\log_{10}a_{H^+}
\]

\[
\Delta G^\circ=-RT\ln K
\]

Logarithm biến phép nhân thành phép cộng. Vì hằng số cân bằng của các phản ứng ghép nhau được nhân, năng lượng tự do chuẩn của chúng lại cộng trực tiếp.

Đây là ví dụ đẹp cho việc toán học không chỉ làm tính toán thuận tiện hơn mà còn làm lộ cấu trúc của Hóa học.

## Giải tích

Tốc độ phản ứng là đạo hàm theo thời gian:

\[
rate=-\frac{d[A]}{dt}
\]

Phương trình tốc độ tích phân là nghiệm của phương trình vi phân với điều kiện đầu.

Nhiệt động lực học cũng dùng đạo hàm để định nghĩa nhiệt dung, thế hóa học và nhiều đại lượng đáp ứng. Khi gặp một đạo hàm trong Hóa học, nên đọc nó như câu hỏi: “đại lượng này thay đổi nhạy tới mức nào khi ta thay đổi một biến khác?”.

## Phương trình vi phân

Cơ chế phản ứng phức tạp tạo thành hệ phương trình vi phân thường:

\[
\frac{d\mathbf c}{dt}=\mathbf f(\mathbf c,T)
\]

Hóa học khí quyển, cháy và chuyển hóa sinh học có thể chứa hàng trăm hoặc hàng nghìn chất và phản ứng, nên không thể giải bằng công thức đóng đơn giản.

Khi các tốc độ khác nhau qua nhiều thang thời gian, hệ trở thành **hệ cứng (stiff system)** và cần bộ giải số phù hợp.

## Đại số tuyến tính

Cân bằng phương trình hóa học có thể xem như bài toán không gian nghiệm của ma trận.

Trong cơ học lượng tử, operator và hàm sóng được biểu diễn trên một cơ sở hữu hạn rồi chuyển thành bài toán trị riêng của ma trận:

\[
A\mathbf v=\lambda\mathbf v
\]

Phân tích phổ, hóa lượng đa biến và xử lý dữ liệu cũng dùng mạnh các công cụ như phân rã ma trận, bình phương tối thiểu và phân tích thành phần chính.

## Xác suất và thống kê

Cơ học lượng tử có bản chất xác suất; cơ học thống kê mô tả phân bố của số lượng lớn vi trạng thái; hóa phân tích cần ước lượng sai số và độ không đảm bảo; động học ở quy mô nhỏ có thể được mô tả bằng quá trình ngẫu nhiên.

Ở cấp một phân tử đơn, thời điểm phản ứng có thể dao động mạnh. Ở cấp quần thể lớn, phương trình tốc độ liên tục lại mô tả rất tốt giá trị trung bình.

Đây là mối liên hệ giữa mô hình ngẫu nhiên vi mô và hành vi gần như xác định ở cấp vĩ mô.

## Tối ưu hóa

Cân bằng có thể được tìm bằng cách cực tiểu hóa năng lượng tự do Gibbs dưới các ràng buộc bảo toàn.

Thiết kế quy trình phải tối ưu nhiều mục tiêu như hiệu suất, năng lượng, chi phí và an toàn. Tối ưu hình học phân tử tìm các điểm dừng trên bề mặt thế năng.

Trong mọi trường hợp, việc đặt đúng hàm mục tiêu và ràng buộc quan trọng không kém thuật toán tối ưu.

## Phương pháp số

Phần lớn bài toán hóa học thực tế không có nghiệm giải tích đóng.

Tìm nghiệm số được dùng cho cân bằng phi tuyến; tích phân số được dùng cho động học và vận chuyển; Monte Carlo lấy mẫu cấu hình; động lực học phân tử tích phân phương trình chuyển động; phương pháp phần tử hữu hạn hoặc sai phân hữu hạn giải các bài toán khuếch tán và truyền nhiệt.

Vì vậy năng lực tính toán số ngày càng trở thành một phần tự nhiên của Hóa học hiện đại.

## Mô hình tư duy

Toán học trong Hóa học là **cách nén cấu trúc mà vẫn giữ nguyên quan hệ**. Công thức tốt không chỉ cho đáp án; nó chỉ ra đại lượng nào phụ thuộc đại lượng nào, mức phụ thuộc ra sao và những ràng buộc nào không thể bị phá vỡ.