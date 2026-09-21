# Tư duy thuật toán, đặc tả và tính đúng đắn

**Thuật toán (algorithm / 알고리즘)** không đơn thuần là một đoạn mã có vẻ chạy được. Nó là một thủ tục hữu hạn và rõ nghĩa, biến đầu vào thành đầu ra theo một **đặc tả (specification / 명세)**. Tư duy thuật toán bắt đầu trước khi viết mã: cần xác định trạng thái nào quan trọng, thao tác nào được phép, bất biến nào phải được giữ và bằng chứng nào cho thấy thủ tục thực sự giải đúng bài toán.

## Từ mô tả bài toán tới đặc tả

Một yêu cầu như “tìm phần tử lớn nhất” vẫn còn thiếu nhiều điều. Đầu vào có thể rỗng không? Có phần tử trùng lặp không? Dữ liệu được so sánh theo thứ tự nào? Kết quả cần trả giá trị hay vị trí? Nếu hàm so sánh không có tính bắc cầu thì điều gì xảy ra?

Đặc tả biến các giả định ngầm thành điều kiện rõ ràng. Với mảng không rỗng `A[0..n-1]`, đặc tả của hàm `max` có thể là: kết quả `m` thuộc mảng và với mọi `i`, `m >= A[i]`.

Một cách triển khai đơn giản:

```text
m = A[0]
for i = 1 .. n-1:
    if A[i] > m:
        m = A[i]
return m
```

Điểm cần học không phải cú pháp mà là cách suy luận. Sau khi xử lý đoạn đầu `A[0..i]`, **bất biến vòng lặp (loop invariant)** là `m` bằng phần tử lớn nhất của đoạn đó. Ban đầu bất biến đúng với một phần tử. Mỗi vòng lặp hoặc giữ `m`, hoặc thay nó bằng phần tử lớn hơn, nên bất biến tiếp tục đúng. Khi vòng lặp kết thúc, đoạn đã xét chính là toàn bộ mảng và đặc tả được thỏa mãn.

## Tính đúng đắn từng phần và khả năng kết thúc

Một thuật toán có thể “nếu kết thúc thì cho kết quả đúng” nhưng chưa chắc luôn kết thúc. **Tính đúng đắn từng phần (partial correctness)** nói rằng đầu ra đúng nếu quá trình tính toán kết thúc. **Tính đúng đắn toàn phần (total correctness)** yêu cầu cả kết quả đúng lẫn việc thuật toán chắc chắn kết thúc.

Với vòng lặp, khả năng kết thúc thường được chứng minh bằng một đại lượng giảm dần theo một thứ tự không thể giảm mãi. Tìm kiếm nhị phân làm khoảng tìm kiếm nhỏ dần; thuật toán Euclid làm số dư nhỏ dần; đệ quy phải tiến dần tới trường hợp cơ sở.

Trong hệ thống thực tế, khả năng kết thúc còn có ý nghĩa vận hành: lời gọi mạng cần thời gian chờ tối đa (timeout), cơ chế thử lại cần giới hạn hoặc thời gian chờ tăng dần (backoff), còn bộ xử lý hàng đợi phải tránh lặp vô hạn với thông điệp lỗi. Lý thuyết về kết thúc vì vậy liên hệ trực tiếp với kỹ thuật độ tin cậy.

## Phân rã bài toán và bài toán con

Tư duy thuật toán thường biến một bài toán thành các **bài toán con (subproblem)** dễ xử lý hơn. Merge sort chia mảng thành hai nửa, sắp xếp từng nửa rồi trộn lại. Quy hoạch động nhận ra các bài toán con chồng lặp và lưu kết quả. Tìm kiếm trên đồ thị biến câu hỏi “có thể đi tới đâu?” thành quá trình liên tục mở rộng biên tìm kiếm.

Phân rã phải bảo toàn cấu trúc của bài toán. Với chia để trị (divide and conquer), cần biết cách kết hợp kết quả. Với thuật toán tham lam (greedy), cần chứng minh lựa chọn cục bộ không phá nghiệm tối ưu toàn cục. Với quy hoạch động (dynamic programming), trạng thái phải chứa đủ thông tin từ quá khứ có ảnh hưởng tới tương lai.

## Tư duy chứng minh gắn trực tiếp với mã nguồn

Chứng minh hình thức có thể phức tạp, nhưng tư duy chứng minh tạo ra những câu hỏi rất thực tế:

- Điều kiện tiên quyết (precondition) nào đang bị giả định ngầm?
- Bất biến vòng lặp là gì?
- Bất biến của cấu trúc dữ liệu nào phải được mỗi phương thức bảo toàn?
- Nếu có dữ liệu trùng, đầu vào rỗng hoặc tràn số thì lập luận còn đúng không?
- Nếu hàm so sánh không nhất quán thì giả định về thứ tự có còn đúng không?

**Kiểm thử dựa trên thuộc tính (property-based testing)** cũng xuất phát từ tinh thần này. Thay vì chỉ kiểm tra vài đầu ra cụ thể, ta kiểm tra thuộc tính như “kết quả sắp xếp phải có thứ tự và chứa đúng các phần tử của đầu vào”. Kiểm thử không thay thế chứng minh, nhưng tư duy theo thuộc tính giúp thiết kế kiểm thử tốt hơn.

## Hành vi xác định, ngẫu nhiên và không xác định

**Thuật toán xác định (deterministic algorithm)** với cùng trạng thái và đầu vào sẽ tạo cùng quá trình chuyển trạng thái và đầu ra. **Thuật toán ngẫu nhiên (randomized algorithm)** sử dụng lựa chọn ngẫu nhiên, vì vậy tính đúng đắn hoặc hiệu năng có thể được mô tả theo xác suất. QuickSort chọn pivot ngẫu nhiên có thời gian kỳ vọng `O(n log n)` dù trường hợp xấu nhất vẫn là `O(n²)`.

Tính đồng thời có thể tạo hành vi trông như không xác định vì lịch chạy giữa các luồng thay đổi, dù mã của từng luồng riêng lẻ là xác định. Do đó hệ thống đồng thời cần suy luận về các cách xen kẽ thực thi hoặc mô hình bộ nhớ ở tầng cao hơn.

## Thuật toán trực tuyến và ngoại tuyến

**Thuật toán ngoại tuyến (offline algorithm)** nhìn thấy toàn bộ đầu vào trước khi xử lý. **Thuật toán trực tuyến (online algorithm)** nhận đầu vào dần dần và phải ra quyết định khi chưa biết tương lai. Thay thế bộ nhớ đệm, xử lý luồng, lập lịch và giới hạn tốc độ thường mang tính trực tuyến.

Sự khác biệt này làm thay đổi cả đặc tả lẫn cách đánh giá. Một thuật toán tối ưu khi biết toàn bộ tương lai có thể không triển khai được trong hệ thống thời gian thực.

## Nghiệm chính xác, xấp xỉ và heuristic

Không phải bài toán nào cũng cần nghiệm tối ưu tuyệt đối. **Thuật toán xấp xỉ (approximation algorithm)** có bảo đảm về mức độ gần nghiệm tối ưu. **Heuristic** ưu tiên hiệu quả thực nghiệm nhưng thường không có bảo đảm mạnh. Xếp hạng tìm kiếm, tối ưu trình biên dịch và lập tuyến đường có thể dùng heuristic vì không gian trạng thái quá lớn.

Heuristic không đồng nghĩa với “thuật toán sai”. Nếu đặc tả chấp nhận nghiệm gần đúng thì nó vẫn có thể đúng theo hợp đồng đã định. Vấn đề xuất hiện khi ta diễn giải bảo đảm của nó mạnh hơn thực tế.

## Mô hình tư duy

> Một thuật toán tốt không bắt đầu từ mã nguồn. Hãy xác định **miền đầu vào → trạng thái → phép chuyển hợp lệ → bất biến → điều kiện kết thúc → thuộc tính đầu ra → chi phí tài nguyên**. Mã nguồn chỉ là một cách biểu diễn chuỗi suy luận đó.

## Những hiểu lầm thường gặp

**“Chạy qua các ca kiểm thử là chứng minh đúng.”** Kiểm thử chỉ bao phủ một tập mẫu các lần thực thi. Nó tăng độ tin cậy nhưng không chứng minh một thuộc tính phổ quát, trừ khi miền đầu vào hữu hạn và được kiểm tra đầy đủ.

**“Độ phức tạp tốt thì thuật toán tốt.”** Một thuật toán sai đặc tả với `O(1)` vẫn vô dụng. Tính đúng đắn, ràng buộc và khả năng bảo trì phải được xem xét trước tối ưu vi mô.

**“Đệ quy luôn chậm.”** Đệ quy là cách mô tả phân rã bài toán. Hiệu năng phụ thuộc chi phí gọi hàm, tối ưu hóa, truy cập dữ liệu và cấu trúc thuật toán; chuyển sang vòng lặp không tự động thay đổi lớp độ phức tạp.

## Kết nối

Tính đúng đắn dựa trên [logic, trạng thái và bất biến](../00_computation_information/03_logic_state_abstraction_and_invariants.md). Sau khi biết thủ tục đúng, bước tiếp theo là hỏi [nó tốn bao nhiêu thời gian và không gian](./01_complexity_and_asymptotic_analysis.md), rồi xem [bố trí dữ liệu](./02_memory_models_and_data_layout.md) khiến chi phí lý thuyết tương tác với phần cứng thực tế như thế nào.