# TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Dịch địa chỉ nằm trên đường thực thi quan trọng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Phạm vi bao phủ của TLB** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Bộ nhớ ảo (virtual memory) cho mỗi tiến trình một không gian địa chỉ riêng, nhưng CPU cuối cùng vẫn phải truy cập bộ nhớ vật lý. Nếu mỗi thao tác đọc hoặc ghi đều phải đọc nhiều mục bảng trang từ RAM trước khi lấy dữ liệu thật, chi phí sẽ rất lớn. **Bộ đệm dịch địa chỉ (Translation Lookaside Buffer — TLB / 변환 색인 버퍼)** tồn tại để lưu tạm kết quả ánh xạ từ trang ảo sang khung trang vật lý.

## Dịch địa chỉ nằm trên đường thực thi quan trọng

Một địa chỉ ảo thường được tách thành số trang ảo và độ lệch (offset). Độ lệch giữ nguyên, còn số trang được dịch qua bảng trang. Bảng trang nhiều cấp (multi-level page table) tiết kiệm bộ nhớ cho không gian địa chỉ thưa, nhưng khi TLB bị trượt, CPU có thể phải thực hiện nhiều lần truy cập bộ nhớ để đi qua các cấp bảng trang.

Trên nhiều kiến trúc, phần cứng có **bộ duyệt bảng trang (page walker)** thực hiện quá trình này. Các mục bảng trang mà bộ duyệt đọc lại có thể được lưu trong bộ nhớ đệm (cache / 캐시) CPU, vì vậy hiệu năng dịch địa chỉ liên hệ trực tiếp với phân cấp bộ nhớ đệm (cache / 캐시).

> **Chuyển mạch:** Trong **TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa**, **Phạm vi bao phủ của TLB** tiếp nhận điểm tựa từ **Dịch địa chỉ nằm trên đường thực thi quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trang lớn không miễn phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phạm vi bao phủ của TLB

Nếu TLB có `N` mục và kích thước trang là `P`, lượng bộ nhớ mà nó có thể bao phủ xấp xỉ `N × P`. Khi tập dữ liệu làm việc lớn hơn phạm vi này, số lần trượt TLB tăng ngay cả khi dữ liệu vẫn vừa bộ nhớ đệm (cache / 캐시) cấp cuối.

Đây là lý do cơ sở dữ liệu, vùng nhớ động (heap / 힙) JVM lớn và hệ thống phân tích có thể hưởng lợi từ **trang lớn (huge pages)**. Trang 2 MiB bao phủ vùng nhớ lớn hơn nhiều so với trang 4 KiB khi số mục TLB không đổi.

> **Chuyển mạch:** Ở chặng này của **TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa**, **Trang lớn không miễn phí** tiếp nhận điểm tựa từ **Phạm vi bao phủ của TLB** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vô hiệu hóa TLB giữa nhiều lõi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trang lớn không miễn phí

Trang lớn giảm áp lực lên TLB nhưng tăng phân mảnh nội bộ, khiến cấp phát và dồn bộ nhớ khó hơn, đồng thời làm lượng dữ liệu bị ảnh hưởng lớn hơn khi một trang cần sao chép hoặc di chuyển. Cơ chế **Transparent Huge Pages (THP)** có thể giúp một số loại tải nhưng lại gây đột biến độ trễ ở tải khác do quá trình dồn hoặc hợp nhất trang.

Vì vậy trang lớn là sự đánh đổi giữa hiệu quả dịch địa chỉ và tính linh hoạt của quản lý bộ nhớ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa**, **Vô hiệu hóa TLB giữa nhiều lõi** tiếp nhận điểm tựa từ **Trang lớn không miễn phí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảo hóa bổ sung thêm tầng dịch địa chỉ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vô hiệu hóa TLB giữa nhiều lõi

Khi hệ điều hành thay đổi một ánh xạ có thể đang được lưu trong TLB của nhiều lõi, các mục cũ phải bị vô hiệu hóa. Quá trình **TLB shootdown** thường cần ngắt liên bộ xử lý hoặc cơ chế phối hợp giữa các lõi.

Một chương trình thay đổi ánh xạ thường xuyên có thể tạo chi phí không chỉ trên lõi gọi lời gọi hệ thống (system call / 시스템 호출) mà còn trên nhiều lõi khác. Đây là ví dụ điển hình cho việc một thao tác có vẻ “cục bộ” ở mức API lại có chi phí phối hợp trên toàn máy.

> **Chuyển mạch:** Trong **TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa**, **Ảo hóa bổ sung thêm tầng dịch địa chỉ** tiếp nhận điểm tựa từ **Vô hiệu hóa TLB giữa nhiều lõi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IOMMU và thiết bị I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảo hóa bổ sung thêm tầng dịch địa chỉ

Trong máy ảo, hệ điều hành khách quản lý địa chỉ vật lý khách, nhưng trình giám sát ảo hóa (hypervisor) phải ánh xạ chúng tới địa chỉ vật lý của máy chủ. Phần cứng hiện đại hỗ trợ dịch lồng nhau bằng các cơ chế như Intel EPT hoặc AMD NPT.

Nếu thực hiện ngây thơ, quá trình duyệt bảng trang của hệ điều hành khách kết hợp với dịch địa chỉ của máy chủ có thể tạo rất nhiều lần truy cập bộ nhớ. CPU hiện đại bổ sung bộ nhớ đệm (cache / 캐시) dịch địa chỉ và tối ưu bộ duyệt bảng trang để giảm chi phí, nhưng hệ thống ảo hóa vẫn có phân cấp dịch phức tạp hơn chạy trực tiếp trên phần cứng.

> **Chuyển mạch:** Ở chặng này của **TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa**, **IOMMU và thiết bị I/O** tiếp nhận điểm tựa từ **Ảo hóa bổ sung thêm tầng dịch địa chỉ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chẩn đoán trong hệ thống thực tế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## IOMMU và thiết bị I/O

DMA của thiết bị cũng cần được cô lập. **Đơn vị quản lý bộ nhớ I/O (I/O Memory Management Unit — IOMMU)** dịch địa chỉ mà thiết bị nhìn thấy và ngăn thiết bị tùy ý đọc hoặc ghi toàn bộ bộ nhớ vật lý. Vai trò của nó tương tự MMU nhưng áp dụng cho thiết bị I/O, đặc biệt quan trọng trong ảo hóa, PCI passthrough và ranh giới bảo mật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa**, **Chẩn đoán trong hệ thống thực tế** tiếp nhận điểm tựa từ **IOMMU và thiết bị I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chẩn đoán trong hệ thống thực tế

Nếu ứng dụng sử dụng CPU cao nhưng số lần trượt bộ nhớ đệm (cache / 캐시) không lớn, trượt TLB có thể là nguyên nhân bị bỏ sót. Truy cập ngẫu nhiên trên vùng nhớ động (heap / 힙) lớn, cấu trúc dữ liệu thưa và tải phụ thuộc nhiều vào con trỏ dễ tạo áp lực dịch địa chỉ.

Khi đo lường cần phân biệt lỗi trang nhỏ/lớn (minor/major page fault) ở tầng hệ điều hành với trượt TLB ở tầng phần cứng. Chúng đều liên quan tới “trang”, nhưng là các hiện tượng khác nhau.

> **Chuyển mạch:** Trong **TLB, quá trình duyệt bảng trang, trang lớn và hỗ trợ ảo hóa**, các dấu vết trong **Chẩn đoán trong hệ thống thực tế** được đọc cùng nhau ở **Mô hình tư duy** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Bộ nhớ ảo tạo ra lớp trừu tượng; TLB làm lớp trừu tượng đó đủ nhanh. Khi tập dữ liệu làm việc, số lõi hoặc mức ảo hóa tăng, dịch địa chỉ trở thành một hệ thống phân cấp riêng với bộ nhớ đệm (cache / 캐시), trượt, vô hiệu hóa và tính cục bộ.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
