# Cơ chế bên trong của bộ nhớ ảo: bảng trang, TLB shootdown và trang lớn

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Cơ chế bên trong của bộ nhớ ảo: bảng trang, TLB shootdown và trang lớn**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Không gian địa chỉ là một hợp đồng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Bảng trang nhiều cấp** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối virtual memory với page tables, TLB shootdown và huge pages, để đọc chi phí dịch địa chỉ theo cả phần cứng và kernel.

Ở mức API, một tiến trình nhìn thấy dải địa chỉ ảo gần như riêng tư. Ở mức nhân hệ điều hành (kernel), lớp trừu tượng này phải được duy trì bằng bảng trang, bit quyền truy cập, xử lý lỗi trang và phối hợp với TLB của CPU. Vì vậy bộ nhớ ảo (virtual memory) không chỉ là “dùng đĩa thay RAM”; nó là cơ chế cốt lõi cho cô lập, di chuyển địa chỉ và cấp phát theo nhu cầu.

## Không gian địa chỉ là một hợp đồng

Hai tiến trình có thể sử dụng cùng một địa chỉ ảo nhưng ánh xạ tới các khung trang vật lý khác nhau. Kernel kiểm soát ánh xạ và các quyền đọc, ghi, thực thi cũng như ranh giới người dùng (user / 사용자)/kernel. Sự cô lập này là nền tảng của bảo mật tiến trình.

`mmap`, mở rộng vùng nhớ động (heap / 힙), thư viện dùng chung và ánh xạ tệp (file / 파일) đều là các cách xây dựng không gian địa chỉ. Nhiều ánh xạ ban đầu chỉ tạo siêu dữ liệu; trang vật lý có thể chưa được cấp cho tới khi lần truy cập đầu tiên gây lỗi trang.

> **Nối mạch:** Address space là contract giữa process và OS; multi-level page tables map it, TLB caches the mapping, còn page faults và huge pages đổi chi phí translation với memory footprint.

## Bảng trang nhiều cấp

Một bảng trang phẳng cho không gian địa chỉ lớn sẽ lãng phí rất nhiều bộ nhớ. **Bảng trang nhiều cấp (multi-level page table)** chỉ tạo các nhánh thực sự cần thiết. Đổi lại, dịch địa chỉ phải đi qua nhiều cấp và cần TLB để tránh lặp lại quá trình duyệt bảng trang liên tục.

Kernel phải quản lý vòng đời của các trang chứa bảng trang, thay đổi quyền và đồng bộ khi nhiều luồng của cùng một tiến trình chạy trên nhiều lõi.

> **Nối mạch:** **Lỗi trang nhỏ và lỗi trang lớn** nối từ **Bảng trang nhiều cấp** sang **Sao chép khi ghi**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lỗi trang nhỏ và lỗi trang lớn

**Lỗi trang nhỏ (minor page fault)** không cần đọc dữ liệu từ thiết bị lưu trữ; ví dụ dữ liệu đã có trong page bộ nhớ đệm (cache / 캐시) nhưng chưa được ánh xạ vào tiến trình, hoặc một trang ẩn danh mới cần được cấp. **Lỗi trang lớn (major page fault)** cần I/O từ thiết bị lưu trữ nên có độ trễ lớn hơn nhiều.

Lỗi trang không tự động có nghĩa là hệ thống có lỗi. Phân trang theo nhu cầu (demand paging) cố ý dùng page fault như một cơ chế điều khiển. Điều cần quan tâm là tần suất và chi phí của nó trong ngữ cảnh tải thực tế.

> **Nối mạch:** **Sao chép khi ghi** nối từ **Lỗi trang nhỏ và lỗi trang lớn** sang **TLB shootdown từ góc nhìn hệ điều hành**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sao chép khi ghi

Sau `fork`, tiến trình cha và con có thể tạm thời dùng chung các trang vật lý ở chế độ chỉ đọc. Khi một bên ghi, lỗi ghi khiến kernel sao chép trang. **Sao chép khi ghi (copy-on-write — COW)** tránh phải sao chép toàn bộ không gian địa chỉ ngay lập tức.

COW hiệu quả khi phần lớn trang không bị sửa. Nếu tiến trình con ghi gần như toàn bộ vùng nhớ, các bản sao trì hoãn vẫn phải được tạo và có thể gây đột biến độ trễ hoặc mức sử dụng bộ nhớ.

> **Nối mạch:** **TLB shootdown từ góc nhìn hệ điều hành** nối từ **Sao chép khi ghi** sang **Trang lớn và THP**, vì cơ chế trước tạo đầu vào cho bước sau.

## TLB shootdown từ góc nhìn hệ điều hành

Khi kernel bỏ ánh xạ một trang hoặc giảm quyền truy cập, CPU khác có thể vẫn giữ mục TLB cũ. Kernel phải gửi yêu cầu vô hiệu hóa và chờ mức đồng bộ cần thiết. Trên máy nhiều lõi, thay đổi ánh xạ quá thường xuyên có thể tạo chi phí mở rộng đáng kể.

Đây là kết nối trực tiếp với [TLB và ảo hóa ở tầng kiến trúc](../../02_computer_architecture/advanced/05_tlb_page_walkers_huge_pages_and_virtualization.md).

> **Nối mạch:** **Trang lớn và THP** nối từ **TLB shootdown từ góc nhìn hệ điều hành** sang **Cấp phát vượt mức và OOM**, vì cơ chế trước tạo đầu vào cho bước sau.

## Trang lớn và THP

Trang lớn tăng phạm vi bao phủ của TLB nhưng làm cấp phát bộ nhớ vật lý khó hơn. **Transparent Huge Pages (THP)** trên Linux cố tự động hợp nhất các trang nhỏ, nhưng quá trình dồn bộ nhớ có thể gây đột biến độ trễ. Cơ sở dữ liệu đôi khi chọn trang lớn tường minh để kiểm soát hành vi tốt hơn.

Không có chính sách đúng cho mọi tải. Phân mảnh bộ nhớ, độ nhạy với độ trễ và kiểu truy cập quyết định sự đánh đổi.

> **Nối mạch:** **Cấp phát vượt mức và OOM** nối từ **Trang lớn và THP** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp phát vượt mức và OOM

Hệ điều hành có thể cho tiến trình đặt trước không gian bộ nhớ ảo lớn hơn lượng RAM vật lý hiện có, với giả định không phải mọi vùng đặt trước đều được sử dụng thật. Khi giả định này sai và cơ chế thu hồi không đủ, hệ thống có thể rơi vào áp lực bộ nhớ hoặc xử lý hết bộ nhớ (Out Of memory — OOM).

Vì vậy câu “ứng dụng đã cấp phát X GB” có thể mang nhiều nghĩa khác nhau: vùng địa chỉ ảo đặt trước, bộ nhớ ẩn danh đã cam kết, tập trang đang cư trú trong RAM hoặc tập dữ liệu thực sự được dùng thường xuyên.

> **Nối mạch:** **Mô hình tư duy** tổng hợp từ **Cấp phát vượt mức và OOM**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> Bộ nhớ ảo là một hệ thống ánh xạ có quyền truy cập và vòng đời, không phải một vùng RAM giả. Hiệu năng phụ thuộc vào tính cục bộ của dịch địa chỉ, hành vi lỗi trang, cơ chế thu hồi và chi phí phối hợp giữa các lõi.

> **Bàn giao:** Giữ lại bốn boundary trước khi rời chapter: address mapping, TLB coherence, page-fault/reclaim cost và overcommit/OOM semantics. Sang [Filesystem crash consistency](./04_filesystem_crash_consistency_journaling_and_cow.md) nếu cần theo dõi page dirty đi xuống storage; sang [Memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md) nếu cần quay lại reclaim/working-set; quay về [README](./README.md) để xác nhận owner.
