# Phân cấp bộ nhớ, cache và tính cục bộ

CPU có thể thực hiện phép tính trong vài chu kỳ, trong khi truy cập DRAM có thể tốn hàng chục tới hàng trăm chu kỳ. Thiết bị lưu trữ và mạng còn chậm hơn nhiều. Nếu mọi thao tác đều phải chờ tầng chậm nhất, CPU sẽ dành phần lớn thời gian để chờ. **Phân cấp bộ nhớ (memory hierarchy)** giải quyết vấn đề này bằng nhiều tầng có dung lượng, độ trễ và chi phí khác nhau.

## Không có loại bộ nhớ hoàn hảo

Ta muốn bộ nhớ vừa rất nhanh, rất lớn, rẻ, tiết kiệm điện và không mất dữ liệu khi mất nguồn. Giới hạn vật lý và kinh tế khiến không một công nghệ nào đáp ứng đồng thời tất cả yêu cầu. Vì vậy hệ thống sử dụng chuỗi thanh ghi (register) → cache L1/L2/L3 → DRAM → SSD/HDD → lưu trữ từ xa.

Tầng càng gần CPU thường càng nhỏ nhưng càng nhanh. Cơ chế này hiệu quả vì phần lớn chương trình có **tính cục bộ theo thời gian (temporal locality)** và **tính cục bộ theo không gian (spatial locality)**.

## Dòng cache

Cache CPU thường di chuyển dữ liệu theo **dòng cache (cache line)**, chẳng hạn 64 byte trên nhiều hệ thống, chứ không theo từng biến. Khi đọc một số nguyên 4 byte, các byte lân cận cũng có thể được đưa vào cache. Duyệt mảng tuần tự tận dụng tốt đặc điểm này, còn truy lần theo con trỏ ngẫu nhiên có thể chỉ sử dụng vài byte trong mỗi dòng.

Đây là một lý do hai thuật toán có cùng độ phức tạp Big-O nhưng tốc độ thực tế khác nhau đáng kể.

## Thẻ, tập và độ kết hợp

Cache cần biết khối bộ nhớ nào đang nằm ở vị trí nào. Địa chỉ thường được tách thành độ lệch (offset), chỉ số tập (set index) và thẻ (tag). Cache ánh xạ trực tiếp chỉ cho mỗi khối một vị trí; cache kết hợp theo tập cho một số vị trí ứng viên; cache kết hợp hoàn toàn cho phép đặt ở bất kỳ vị trí nào nhưng phần cứng tra cứu phức tạp hơn.

**Trượt do xung đột (conflict miss)** xảy ra khi nhiều khối dữ liệu nóng ánh xạ vào cùng một tập dù tổng cache vẫn còn dung lượng. Chính sách thay thế (replacement policy), thường là các biến thể xấp xỉ LRU, quyết định dòng nào bị loại.

## Trúng cache và trượt cache

**Trúng cache (cache hit)** cho phép phục vụ dữ liệu ở tầng nhanh. **Trượt cache (cache miss)** buộc hệ thống lấy dữ liệu từ tầng thấp hơn. Mô hình đơn giản cho thời gian truy cập bộ nhớ trung bình là:

\[
AMAT = hit\ time + miss\ rate \times miss\ penalty
\]

Nghĩa là thời gian trung bình bằng chi phí khi trúng cache cộng với tỷ lệ trượt nhân chi phí bổ sung của mỗi lần trượt. Khi có nhiều tầng cache, công thức chi tiết hơn, nhưng ý chính không đổi: tỷ lệ trượt nhỏ vẫn có thể gây ảnh hưởng lớn nếu chi phí của một lần trượt rất cao.

## Chính sách ghi

**Ghi xuyên (write-through)** gửi thay đổi xuống tầng thấp hơn ngay lập tức, giúp trạng thái dễ theo dõi nhưng tăng lưu lượng. **Ghi trả sau (write-back)** chỉ cập nhật dòng cache và đánh dấu bẩn, sau đó ghi xuống khi dòng bị loại; cách này giảm băng thông nhưng quản lý phức tạp hơn. Chính sách cấp phát khi ghi (write-allocate/no-write-allocate) quyết định một lần ghi bị trượt có kéo dòng dữ liệu vào cache hay không.

## Nhất quán cache

CPU nhiều lõi có thể có cache riêng cho từng lõi. Nếu lõi A ghi biến `x` còn lõi B giữ bản sao cũ, hệ thống cần **giao thức nhất quán cache (cache coherence protocol)** để quản lý các bản sao. Các giao thức kiểu MESI theo dõi trạng thái và vô hiệu hóa hoặc chia sẻ dòng cache khi cần.

Nhất quán cache không tự giải quyết toàn bộ ngữ nghĩa đồng thời. Mô hình bộ nhớ của ngôn ngữ và ISA còn quy định thứ tự và khả năng quan sát; các cơ chế đồng bộ tạo quan hệ xảy-ra-trước (happens-before).

## Chia sẻ giả

Hai luồng cập nhật hai biến khác nhau nhưng nằm chung một dòng cache có thể khiến dòng đó liên tục đổi quyền sở hữu giữa các lõi. Về logic chúng không chia sẻ dữ liệu, nhưng về vật lý lại chia sẻ dòng cache; hiện tượng này gọi là **chia sẻ giả (false sharing)**. Căn chỉnh hoặc chèn khoảng đệm có thể giảm vấn đề trong các đường chạy nóng.

Đây là ví dụ rõ về việc lớp trừu tượng ở mức biến bị “rò” xuống đặc tính phần cứng ở mức dòng cache.

## TLB và cache dịch địa chỉ

Địa chỉ ảo phải được dịch qua bảng trang. **Bộ đệm dịch địa chỉ (Translation Lookaside Buffer — TLB)** lưu các ánh xạ ảo → vật lý gần đây. Khi TLB bị trượt, CPU phải duyệt bảng trang, vì vậy tập dữ liệu lớn hoặc truy cập ngẫu nhiên có thêm chi phí ngoài trượt cache dữ liệu.

Trang lớn (huge pages) giảm số mục TLB cần thiết nhưng đổi lại làm cấp phát và phân mảnh nội bộ khó kiểm soát hơn.

## Nạp trước

Phần cứng hoặc phần mềm có thể **nạp trước (prefetching)** dữ liệu được dự đoán sẽ sớm dùng. Kiểu truy cập tuần tự dễ dự đoán; cấu trúc liên kết khó hơn vì địa chỉ tiếp theo phụ thuộc vào dữ liệu vừa đọc. Dự đoán sai làm lãng phí băng thông và dung lượng cache.

## Mô hình tư duy

> Hiệu năng bộ nhớ phụ thuộc vào **tập dữ liệu làm việc (working set) và kiểu truy cập (access pattern)**, không chỉ kích thước dữ liệu. Hãy hỏi dữ liệu vừa với tầng nào, mỗi lần truy cập sử dụng bao nhiêu phần của dòng cache, dữ liệu có được tái sử dụng không và các lõi có tranh chấp cùng dòng hay không.

## Những hiểu nhầm thường gặp

**“RAM chỉ có một tốc độ.”** Không đúng. Cache, TLB và NUMA khiến chi phí truy cập phụ thuộc vị trí và lịch sử truy cập.

**“Cache chỉ là cache phần mềm như Redis.”** Không đúng. Cache CPU là tầng bộ nhớ do phần cứng quản lý; nó chia sẻ nguyên lý tính cục bộ với cache phần mềm nhưng cơ chế rất khác.

**“Coherence làm mã đồng thời tự động an toàn.”** Không đúng. Coherence giữ các bản sao nhất quán theo giao thức; chương trình không có race vẫn cần quy tắc đồng bộ và thứ tự bộ nhớ phù hợp.

## Kết nối

[Bố trí dữ liệu và tính cục bộ](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) là phía phần mềm; [bộ nhớ ảo](../03_operating_systems/03_virtual_memory_and_address_spaces.md) bổ sung tầng dịch địa chỉ; [đồng thời](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) giải thích thứ tự bộ nhớ; [hiệu năng hệ thống](../08_software_systems/02_performance_capacity_and_scalability.md) mở rộng suy luận tới các nút thắt cổ chai của toàn hệ thống.
