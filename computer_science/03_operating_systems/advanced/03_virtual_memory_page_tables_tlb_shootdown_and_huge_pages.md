# Cơ chế bên trong của bộ nhớ ảo: bảng trang, TLB shootdown và trang lớn

> **Mạch đọc:** Đặt **Cơ chế bên trong của bộ nhớ ảo: bảng trang, TLB shootdown và trang lớn** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Không gian địa chỉ là một hợp đồng** sang **Bảng trang nhiều cấp**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Ở mức API, một tiến trình nhìn thấy dải địa chỉ ảo gần như riêng tư. Ở mức nhân hệ điều hành (kernel), lớp trừu tượng này phải được duy trì bằng bảng trang, bit quyền truy cập, xử lý lỗi trang và phối hợp với TLB của CPU. Vì vậy bộ nhớ ảo (virtual memory) không chỉ là “dùng đĩa thay RAM”; nó là cơ chế cốt lõi cho cô lập, di chuyển địa chỉ và cấp phát theo nhu cầu.

## Không gian địa chỉ là một hợp đồng

Hai tiến trình có thể sử dụng cùng một địa chỉ ảo nhưng ánh xạ tới các khung trang vật lý khác nhau. Kernel kiểm soát ánh xạ và các quyền đọc, ghi, thực thi cũng như ranh giới người dùng (user / 사용자)/kernel. Sự cô lập này là nền tảng của bảo mật tiến trình.

`mmap`, mở rộng vùng nhớ động (heap / 힙), thư viện dùng chung và ánh xạ tệp (file / 파일) đều là các cách xây dựng không gian địa chỉ. Nhiều ánh xạ ban đầu chỉ tạo siêu dữ liệu; trang vật lý có thể chưa được cấp cho tới khi lần truy cập đầu tiên gây lỗi trang.


> **Chuyển mạch:** Từ **Không gian địa chỉ là một hợp đồng**, ta sang **Bảng trang nhiều cấp** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bảng trang nhiều cấp

Một bảng trang phẳng cho không gian địa chỉ lớn sẽ lãng phí rất nhiều bộ nhớ. **Bảng trang nhiều cấp (multi-level page table)** chỉ tạo các nhánh thực sự cần thiết. Đổi lại, dịch địa chỉ phải đi qua nhiều cấp và cần TLB để tránh lặp lại quá trình duyệt bảng trang liên tục.

Kernel phải quản lý vòng đời của các trang chứa bảng trang, thay đổi quyền và đồng bộ khi nhiều luồng của cùng một tiến trình chạy trên nhiều lõi.


> **Chuyển mạch:** Từ **Bảng trang nhiều cấp**, ta sang **Lỗi trang nhỏ và lỗi trang lớn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Lỗi trang nhỏ và lỗi trang lớn

**Lỗi trang nhỏ (minor page fault)** không cần đọc dữ liệu từ thiết bị lưu trữ; ví dụ dữ liệu đã có trong page bộ nhớ đệm (cache / 캐시) nhưng chưa được ánh xạ vào tiến trình, hoặc một trang ẩn danh mới cần được cấp. **Lỗi trang lớn (major page fault)** cần I/O từ thiết bị lưu trữ nên có độ trễ lớn hơn nhiều.

Lỗi trang không tự động có nghĩa là hệ thống có lỗi. Phân trang theo nhu cầu (demand paging) cố ý dùng page fault như một cơ chế điều khiển. Điều cần quan tâm là tần suất và chi phí của nó trong ngữ cảnh tải thực tế.


> **Chuyển mạch:** Từ **Lỗi trang nhỏ và lỗi trang lớn**, ta sang **Sao chép khi ghi** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sao chép khi ghi

Sau `fork`, tiến trình cha và con có thể tạm thời dùng chung các trang vật lý ở chế độ chỉ đọc. Khi một bên ghi, lỗi ghi khiến kernel sao chép trang. **Sao chép khi ghi (copy-on-write — COW)** tránh phải sao chép toàn bộ không gian địa chỉ ngay lập tức.

COW hiệu quả khi phần lớn trang không bị sửa. Nếu tiến trình con ghi gần như toàn bộ vùng nhớ, các bản sao trì hoãn vẫn phải được tạo và có thể gây đột biến độ trễ hoặc mức sử dụng bộ nhớ.


> **Chuyển mạch:** Từ **Sao chép khi ghi**, ta sang **TLB shootdown từ góc nhìn hệ điều hành** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## TLB shootdown từ góc nhìn hệ điều hành

Khi kernel bỏ ánh xạ một trang hoặc giảm quyền truy cập, CPU khác có thể vẫn giữ mục TLB cũ. Kernel phải gửi yêu cầu vô hiệu hóa và chờ mức đồng bộ cần thiết. Trên máy nhiều lõi, thay đổi ánh xạ quá thường xuyên có thể tạo chi phí mở rộng đáng kể.

Đây là kết nối trực tiếp với [TLB và ảo hóa ở tầng kiến trúc](../../02_computer_architecture/advanced/05_tlb_page_walkers_huge_pages_and_virtualization.md).


> **Chuyển mạch:** Từ **TLB shootdown từ góc nhìn hệ điều hành**, ta sang **Trang lớn và THP** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trang lớn và THP

Trang lớn tăng phạm vi bao phủ của TLB nhưng làm cấp phát bộ nhớ vật lý khó hơn. **Transparent Huge Pages (THP)** trên Linux cố tự động hợp nhất các trang nhỏ, nhưng quá trình dồn bộ nhớ có thể gây đột biến độ trễ. Cơ sở dữ liệu đôi khi chọn trang lớn tường minh để kiểm soát hành vi tốt hơn.

Không có chính sách đúng cho mọi tải. Phân mảnh bộ nhớ, độ nhạy với độ trễ và kiểu truy cập quyết định sự đánh đổi.


> **Chuyển mạch:** Từ **Trang lớn và THP**, ta sang **Cấp phát vượt mức và OOM** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cấp phát vượt mức và OOM

Hệ điều hành có thể cho tiến trình đặt trước không gian bộ nhớ ảo lớn hơn lượng RAM vật lý hiện có, với giả định không phải mọi vùng đặt trước đều được sử dụng thật. Khi giả định này sai và cơ chế thu hồi không đủ, hệ thống có thể rơi vào áp lực bộ nhớ hoặc xử lý hết bộ nhớ (Out Of memory — OOM).

Vì vậy câu “ứng dụng đã cấp phát X GB” có thể mang nhiều nghĩa khác nhau: vùng địa chỉ ảo đặt trước, bộ nhớ ẩn danh đã cam kết, tập trang đang cư trú trong RAM hoặc tập dữ liệu thực sự được dùng thường xuyên.


> **Chuyển mạch:** Từ **Cấp phát vượt mức và OOM**, ta sang **Mô hình tư duy** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy

> Bộ nhớ ảo là một hệ thống ánh xạ có quyền truy cập và vòng đời, không phải một vùng RAM giả. Hiệu năng phụ thuộc vào tính cục bộ của dịch địa chỉ, hành vi lỗi trang, cơ chế thu hồi và chi phí phối hợp giữa các lõi.

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 kernel execution contexts and syscall path](./00_kernel_execution_contexts_and_syscall_path.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
