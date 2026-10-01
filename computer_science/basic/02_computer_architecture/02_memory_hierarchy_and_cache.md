# Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Không có loại bộ nhớ hoàn hảo** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Dòng bộ nhớ đệm (cache / 캐시)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

CPU có thể thực hiện phép tính trong vài chu kỳ, trong khi truy cập DRAM có thể tốn hàng chục tới hàng trăm chu kỳ. Thiết bị lưu trữ và mạng còn chậm hơn nhiều. Nếu mọi thao tác đều phải chờ tầng chậm nhất, CPU sẽ dành phần lớn thời gian để chờ. **Phân cấp bộ nhớ (memory hierarchy)** giải quyết vấn đề này bằng nhiều tầng có dung lượng, độ trễ và chi phí khác nhau.

## Không có loại bộ nhớ hoàn hảo

Ta muốn bộ nhớ vừa rất nhanh, rất lớn, rẻ, tiết kiệm điện và không mất dữ liệu khi mất nguồn. Giới hạn vật lý và kinh tế khiến không một công nghệ nào đáp ứng đồng thời tất cả yêu cầu. Vì vậy hệ thống sử dụng chuỗi thanh ghi (register) → bộ nhớ đệm (cache / 캐시) L1/L2/L3 → DRAM → SSD/HDD → lưu trữ từ xa.

Tầng càng gần CPU thường càng nhỏ nhưng càng nhanh. Cơ chế này hiệu quả vì phần lớn chương trình có **tính cục bộ theo thời gian (temporal locality)** và **tính cục bộ theo không gian (spatial locality)**.

> **Chuyển mạch:** Trong **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Dòng bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Không có loại bộ nhớ hoàn hảo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thẻ, tập và độ kết hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dòng bộ nhớ đệm (cache / 캐시)

Bộ nhớ đệm (cache / 캐시) CPU thường di chuyển dữ liệu theo **dòng bộ nhớ đệm (cache / 캐시) (cache line)**, chẳng hạn 64 byte trên nhiều hệ thống, chứ không theo từng biến. Khi đọc một số nguyên 4 byte, các byte lân cận cũng có thể được đưa vào bộ nhớ đệm (cache / 캐시). Duyệt mảng tuần tự tận dụng tốt đặc điểm này, còn truy lần theo con trỏ ngẫu nhiên có thể chỉ sử dụng vài byte trong mỗi dòng.

Đây là một lý do hai thuật toán có cùng độ phức tạp Big-O nhưng tốc độ thực tế khác nhau đáng kể.

> **Chuyển mạch:** Ở chặng này của **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Thẻ, tập và độ kết hợp** tiếp nhận điểm tựa từ **Dòng bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trúng bộ nhớ đệm (cache / 캐시) và trượt bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thẻ, tập và độ kết hợp

Bộ nhớ đệm (cache / 캐시) cần biết khối bộ nhớ nào đang nằm ở vị trí nào. Địa chỉ thường được tách thành độ lệch (offset), chỉ số tập (set index) và thẻ (tag). bộ nhớ đệm (cache / 캐시) ánh xạ trực tiếp chỉ cho mỗi khối một vị trí; bộ nhớ đệm (cache / 캐시) kết hợp theo tập cho một số vị trí ứng viên; bộ nhớ đệm (cache / 캐시) kết hợp hoàn toàn cho phép đặt ở bất kỳ vị trí nào nhưng phần cứng tra cứu phức tạp hơn.

**Trượt do xung đột (conflict miss)** xảy ra khi nhiều khối dữ liệu nóng ánh xạ vào cùng một tập dù tổng bộ nhớ đệm (cache / 캐시) vẫn còn dung lượng. Chính sách thay thế (replacement policy), thường là các biến thể xấp xỉ LRU, quyết định dòng nào bị loại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Trúng bộ nhớ đệm (cache / 캐시) và trượt bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Thẻ, tập và độ kết hợp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính sách ghi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trúng bộ nhớ đệm (cache / 캐시) và trượt bộ nhớ đệm (cache / 캐시)

**Trúng bộ nhớ đệm (cache / 캐시) (cache hit)** cho phép phục vụ dữ liệu ở tầng nhanh. **Trượt bộ nhớ đệm (cache / 캐시) (cache miss)** buộc hệ thống lấy dữ liệu từ tầng thấp hơn. Mô hình đơn giản cho thời gian truy cập bộ nhớ trung bình là:

\[
AMAT = hit\ thời gian (time / 시간) + miss\ tỷ lệ (rate / 비율) \times miss\ penalty
\]

Nghĩa là thời gian trung bình bằng chi phí khi trúng bộ nhớ đệm (cache / 캐시) cộng với tỷ lệ trượt nhân chi phí bổ sung của mỗi lần trượt. Khi có nhiều tầng bộ nhớ đệm (cache / 캐시), công thức chi tiết hơn, nhưng ý chính không đổi: tỷ lệ trượt nhỏ vẫn có thể gây ảnh hưởng lớn nếu chi phí của một lần trượt rất cao.

> **Chuyển mạch:** Trong **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Chính sách ghi** tiếp nhận điểm tựa từ **Trúng bộ nhớ đệm (cache / 캐시) và trượt bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhất quán bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách ghi

**Ghi xuyên (write-through)** gửi thay đổi xuống tầng thấp hơn ngay lập tức, giúp trạng thái dễ theo dõi nhưng tăng lưu lượng. **Ghi trả sau (write-back)** chỉ cập nhật dòng bộ nhớ đệm (cache / 캐시) và đánh dấu bẩn, sau đó ghi xuống khi dòng bị loại; cách này giảm băng thông nhưng quản lý phức tạp hơn. Chính sách cấp phát khi ghi (write-allocate/no-write-allocate) quyết định một lần ghi bị trượt có kéo dòng dữ liệu vào bộ nhớ đệm (cache / 캐시) hay không.

> **Chuyển mạch:** Ở chặng này của **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Nhất quán bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Chính sách ghi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chia sẻ giả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhất quán bộ nhớ đệm (cache / 캐시)

CPU nhiều lõi có thể có bộ nhớ đệm (cache / 캐시) riêng cho từng lõi. Nếu lõi A ghi biến `x` còn lõi B giữ bản sao cũ, hệ thống cần **giao thức nhất quán bộ nhớ đệm (cache / 캐시) (cache coherence protocol)** để quản lý các bản sao. Các giao thức kiểu MESI theo dõi trạng thái và vô hiệu hóa hoặc chia sẻ dòng bộ nhớ đệm (cache / 캐시) khi cần.

Nhất quán bộ nhớ đệm (cache / 캐시) không tự giải quyết toàn bộ ngữ nghĩa đồng thời. Mô hình bộ nhớ của ngôn ngữ và ISA còn quy định thứ tự và khả năng quan sát; các cơ chế đồng bộ tạo quan hệ xảy-ra-trước (happens-before).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Chia sẻ giả** tiếp nhận điểm tựa từ **Nhất quán bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TLB và bộ nhớ đệm (cache / 캐시) dịch địa chỉ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chia sẻ giả

Hai luồng cập nhật hai biến khác nhau nhưng nằm chung một dòng bộ nhớ đệm (cache / 캐시) có thể khiến dòng đó liên tục đổi quyền sở hữu giữa các lõi. Về lô-gic (logic / 논리) chúng không chia sẻ dữ liệu, nhưng về vật lý lại chia sẻ dòng bộ nhớ đệm (cache / 캐시); hiện tượng này gọi là **chia sẻ giả (false sharing)**. Căn chỉnh hoặc chèn khoảng đệm có thể giảm vấn đề trong các đường chạy nóng.

Đây là ví dụ rõ về việc lớp trừu tượng ở mức biến bị “rò” xuống đặc tính phần cứng ở mức dòng bộ nhớ đệm (cache / 캐시).

> **Chuyển mạch:** Trong **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **TLB và bộ nhớ đệm (cache / 캐시) dịch địa chỉ** tiếp nhận điểm tựa từ **Chia sẻ giả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nạp trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TLB và bộ nhớ đệm (cache / 캐시) dịch địa chỉ

Địa chỉ ảo phải được dịch qua bảng trang. **Bộ đệm dịch địa chỉ (Translation Lookaside Buffer — TLB)** lưu các ánh xạ ảo → vật lý gần đây. Khi TLB bị trượt, CPU phải duyệt bảng trang, vì vậy tập dữ liệu lớn hoặc truy cập ngẫu nhiên có thêm chi phí ngoài trượt bộ nhớ đệm (cache / 캐시) dữ liệu.

Trang lớn (huge pages) giảm số mục TLB cần thiết nhưng đổi lại làm cấp phát và phân mảnh nội bộ khó kiểm soát hơn.

> **Chuyển mạch:** Ở chặng này của **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Nạp trước** tiếp nhận điểm tựa từ **TLB và bộ nhớ đệm (cache / 캐시) dịch địa chỉ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nạp trước

Phần cứng hoặc phần mềm có thể **nạp trước (prefetching)** dữ liệu được dự đoán sẽ sớm dùng. Kiểu truy cập tuần tự dễ dự đoán; cấu trúc liên kết khó hơn vì địa chỉ tiếp theo phụ thuộc vào dữ liệu vừa đọc. Dự đoán sai làm lãng phí băng thông và dung lượng bộ nhớ đệm (cache / 캐시).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Mô hình tư duy** gom các mảnh từ **Nạp trước** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> Hiệu năng bộ nhớ phụ thuộc vào **tập dữ liệu làm việc (working set) và kiểu truy cập (access pattern)**, không chỉ kích thước dữ liệu. Hãy hỏi dữ liệu vừa với tầng nào, mỗi lần truy cập sử dụng bao nhiêu phần của dòng bộ nhớ đệm (cache / 캐시), dữ liệu có được tái sử dụng không và các lõi có tranh chấp cùng dòng hay không.

> **Chuyển mạch:** Trong **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“RAM chỉ có một tốc độ.”** Không đúng. bộ nhớ đệm (cache / 캐시), TLB và NUMA khiến chi phí truy cập phụ thuộc vị trí và lịch sử truy cập.

**“bộ nhớ đệm (cache / 캐시) chỉ là bộ nhớ đệm (cache / 캐시) phần mềm như Redis.”** Không đúng. bộ nhớ đệm (cache / 캐시) CPU là tầng bộ nhớ do phần cứng quản lý; nó chia sẻ nguyên lý tính cục bộ với bộ nhớ đệm (cache / 캐시) phần mềm nhưng cơ chế rất khác.

**“Coherence làm mã đồng thời tự động an toàn.”** Không đúng. Coherence giữ các bản sao nhất quán theo giao thức; chương trình không có race vẫn cần quy tắc đồng bộ và thứ tự bộ nhớ phù hợp.

> **Chuyển mạch:** Ở chặng này của **Phân cấp bộ nhớ, bộ nhớ đệm (cache / 캐시) và tính cục bộ**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Kết nối** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Bố trí dữ liệu và tính cục bộ](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) là phía phần mềm; [bộ nhớ ảo](../03_operating_systems/03_virtual_memory_and_address_spaces.md) bổ sung tầng dịch địa chỉ; [đồng thời](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) giải thích thứ tự bộ nhớ; [hiệu năng hệ thống](../08_software_systems/02_performance_capacity_and_scalability.md) mở rộng suy luận tới các nút thắt cổ chai của toàn hệ thống.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
