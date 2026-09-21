# Đường đi của tính đúng đắn: mô hình bộ nhớ ngôn ngữ → hệ điều hành → thứ tự CPU

Lỗi đồng thời thường bị giải thích quá đơn giản bằng câu “CPU sắp xếp lại lệnh”. Thực tế hợp đồng về tính đúng đắn đi qua nhiều tầng: mô hình bộ nhớ của ngôn ngữ nguồn, biến đổi của trình biên dịch, primitive của runtime, lập lịch hệ điều hành và thứ tự bộ nhớ của phần cứng. Muốn suy luận đúng phải biết mỗi tầng được phép thay đổi điều gì.

## Thứ tự trong mã nguồn không phải hợp đồng thực thi tuyệt đối

Trình biên dịch có thể đổi thứ tự hoặc loại bỏ thao tác nếu hành vi quan sát được theo mô hình ngôn ngữ không thay đổi. CPU cũng có thể thực thi và dự đoán ngoài thứ tự. Tuy nhiên cả hai đều bị ràng buộc bởi ngữ nghĩa đồng bộ mà ngôn ngữ và ISA định nghĩa.

Vì vậy chỉ nhìn thứ tự lệnh assembly không đủ để kết luận chương trình nguồn không có tranh chấp dữ liệu.

## Tranh chấp dữ liệu

Trong nhiều mô hình ngôn ngữ, **tranh chấp dữ liệu (data race)** xuất hiện khi hai luồng truy cập cùng một vị trí có thể thay đổi, ít nhất một bên ghi và không có đồng bộ phù hợp. Hậu quả có thể vượt xa việc “đọc giá trị cũ”, vì trình biên dịch có thể tối ưu dựa trên giả định chương trình hợp lệ không có race.

Mô hình bộ nhớ Java định nghĩa quan hệ **xảy-ra-trước (happens-before)** qua khóa monitor, `volatile`, `thread start/join` và các quy tắc khác. Nếu một lần ghi xảy-ra-trước lần đọc, khả năng quan sát và thứ tự được bảo đảm theo mô hình.

## Volatile và thao tác nguyên tử

Trong Java, `volatile` cung cấp ngữ nghĩa về khả năng quan sát và thứ tự mạnh hơn trường thông thường, nhưng không biến thao tác ghép như `count++` thành một giao dịch nguyên tử.

Các lớp atomic dùng compare-and-set hoặc primitive tương đương để xây thao tác đọc–sửa–ghi nguyên tử. Khóa cung cấp loại trừ lẫn nhau và thứ tự, nhưng phải trả chi phí lập lịch và tranh chấp.

## Rào cản trình biên dịch và hàng rào phần cứng

**Rào cản trình biên dịch (compiler barrier)** ngăn compiler đổi thứ tự qua một ranh giới theo các quy tắc nhất định; **hàng rào bộ nhớ (memory fence)** điều khiển thứ tự quan sát của thao tác bộ nhớ ở CPU. Một primitive đồng bộ cấp cao có thể được biên dịch thành fence hoặc lệnh nguyên tử khác nhau tùy kiến trúc.

x86 có thứ tự tương đối mạnh trong nhiều trường hợp; ARM và RISC-V cho phép nhiều kiểu đổi thứ tự hơn. Runtime đa nền tảng phải ánh xạ cùng một hợp đồng cấp cao xuống từng ISA sao cho vẫn đúng.

## Nhất quán cache

Nhất quán cache bảo đảm các lõi không giữ vô hạn các phiên bản có thể ghi mâu thuẫn của cùng một dòng cache, nhưng riêng coherence không định nghĩa thứ tự giữa nhiều vị trí bộ nhớ khác nhau. Vì vậy “cache coherent” không thay thế mô hình bộ nhớ.

Xem thêm: [Memory consistency, cache coherence và ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md).

## Bộ lập lịch hệ điều hành

Luồng có thể bị tạm dừng hoặc di chuyển giữa các lõi gần như bất kỳ lúc nào. Đồng bộ đúng không được dựa vào giả định “luồng A chắc chạy xong trước vì bình thường nó nhanh hơn”. `sleep` hoặc canh thời gian không tạo quan hệ happens-before đáng tin cậy.

## Double-checked locking

Mẫu khởi tạo lười kiểu double-checked locking từng có các biến thể sai khi việc công bố đối tượng và thứ tự ghi không được bảo đảm. Tham chiếu đối tượng có thể trở nên nhìn thấy trước khi luồng khác quan sát đầy đủ các hiệu ứng khởi tạo theo mô hình bộ nhớ yếu.

Các mẫu hiện đại dùng `volatile`, `synchronized` hoặc ngữ nghĩa khởi tạo tĩnh để tạo **công bố an toàn (safe publication)**.

## Gỡ lỗi

Race có thể biến mất khi thêm log vì thời điểm chạy, hàng rào hoặc hiệu ứng cache thay đổi. Loại lỗi này thường được gọi là **Heisenbug**. Công cụ phát hiện race, kiểm thử áp lực và suy luận theo mô hình đáng tin hơn việc cố tái hiện bằng `sleep`.

## Mô hình tư duy

> Tính đúng đắn của chương trình đồng thời là một hợp đồng xuyên nhiều tầng. Ngôn ngữ định nghĩa happens-before; compiler và runtime phải giữ hợp đồng; ISA cung cấp thao tác nguyên tử và fence; cache/coherence thực hiện việc lan truyền giá trị; hệ điều hành quyết định cách các luồng xen kẽ. Đừng sửa race bằng thời gian — hãy tạo cạnh đồng bộ rõ ràng.