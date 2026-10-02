# Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Kernel, system calls và OS abstractions**. Route đi từ kernel privilege/protection → system calls/ABI → process, memory và I/O abstractions → isolation và observability, để “OS abstraction” luôn quay về cơ chế kernel thực thi.

**Hệ điều hành (Operating System — OS / 운영체제)** giải quyết một mâu thuẫn cơ bản: nhiều chương trình muốn dùng chung CPU, bộ nhớ, lưu trữ và thiết bị, nhưng nếu mỗi chương trình điều khiển phần cứng trực tiếp thì việc cô lập, chia sẻ và hỗ trợ nhiều loại phần cứng gần như không thể quản lý. Hệ điều hành đặt một **nhân có đặc quyền (privileged kernel)** giữa ứng dụng và phần cứng, sau đó cung cấp các lớp trừu tượng ổn định như tiến trình, bộ nhớ ảo, tệp và socket.

## Nhân hệ điều hành là phần có quyền đặc biệt

**Nhân hệ điều hành (kernel / 커널)** chạy ở mức đặc quyền CPU cao, quản lý bảng trang, ngắt, trình điều khiển thiết bị, lập lịch và các tài nguyên được bảo vệ. Ứng dụng thông thường chạy ở **chế độ người dùng (user mode / 사용자 모드)** với quyền hạn chế.

Ranh giới này được phần cứng cưỡng chế. Nếu một tiến trình bình thường có thể tự sửa bảng trang hoặc đọc tùy ý bộ nhớ vật lý thì sự cô lập giữa các tiến trình sẽ không còn tồn tại.

Thiết kế kernel có nhiều dạng. Kernel nguyên khối như Linux đặt nhiều hệ thống con và trình điều khiển trong không gian kernel. Triết lý **vi nhân (microkernel)** đưa nhiều dịch vụ ra không gian người dùng và giữ kernel nhỏ hơn. Hệ thống lai kết hợp cả hai. Mỗi cách đánh đổi giữa hiệu năng, khả năng cô lập lỗi và độ phức tạp.

> **Chuyển mạch:** Trong **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Lời gọi hệ thống** tiếp nhận điểm tựa từ **Nhân hệ điều hành là phần có quyền đặc biệt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ mô tả tệp và handle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lời gọi hệ thống

**Lời gọi hệ thống (system call / syscall / 시스템 호출)** là lối vào có kiểm soát từ chế độ người dùng sang kernel để yêu cầu thao tác cần đặc quyền, ví dụ `read`, `write`, `open`, `mmap`, `fork` hoặc `socket`. API của ngôn ngữ hoặc thư viện có thể bao bọc syscall; không phải mọi lời gọi thư viện đều tạo syscall.

Ví dụ `printf` có thể định dạng dữ liệu hoàn toàn trong không gian người dùng rồi chỉ gọi `write` khi bộ đệm cần được đẩy ra. Tương tự, `malloc` có thể cấp phát từ vùng vùng nhớ động (heap / 힙) đã có và chỉ thỉnh thoảng xin thêm trang bộ nhớ từ hệ điều hành.

Syscall có chi phí do chuyển mức đặc quyền, kiểm tra đầu vào và thực hiện công việc trong kernel. Các kernel và môi trường thực thi hiện đại giảm chi phí này bằng gom nhóm thao tác (batching), bộ nhớ chia sẻ và giao diện I/O bất đồng bộ.

> **Chuyển mạch:** Ở chặng này của **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Bộ mô tả tệp và handle** tiếp nhận điểm tựa từ **Lời gọi hệ thống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trừu tượng tiến trình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ mô tả tệp và handle

Hệ điều hành kiểu Unix dùng **bộ mô tả tệp (file descriptor)**, tức một số nguyên làm chỉ mục vào bảng tài nguyên đang mở của từng tiến trình. Tệp, socket, pipe và thiết bị có thể cùng sử dụng giao diện gần giống `read`/`write`. Câu “mọi thứ là tệp” không hoàn toàn đúng theo nghĩa đen, nhưng giao diện I/O thống nhất giúp các thành phần dễ kết hợp hơn.

Windows dùng khái niệm **handle** rộng hơn. Nguyên tắc chung là mã ở không gian người dùng giữ một tham chiếu không trong suốt (opaque reference) thay vì trực tiếp nắm đối tượng nội bộ của kernel.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Trừu tượng tiến trình** tiếp nhận điểm tựa từ **Bộ mô tả tệp và handle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảo hóa thời gian và không gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trừu tượng tiến trình

**tiến trình (process / 프로세스)** tạo cảm giác rằng một chương trình có ngữ cảnh thực thi CPU và không gian địa chỉ riêng. Trong thực tế, bộ lập lịch chia thời gian CPU giữa nhiều tác vụ có thể chạy, còn bộ nhớ ảo ánh xạ các địa chỉ trông như riêng tư sang các trang vật lý có thể được chia sẻ hoặc sao chép khi ghi.

Vì vậy có thể xem hệ điều hành như **bộ phân phối tài nguyên và lớp cô lập**.

> **Chuyển mạch:** Trong **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Ảo hóa thời gian và không gian** tiếp nhận điểm tựa từ **Trừu tượng tiến trình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Không gian người dùng và không gian kernel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảo hóa thời gian và không gian

Ảo hóa CPU: bộ lập lịch làm nhiều tiến trình cùng có cảm giác đang tiến triển.

Ảo hóa bộ nhớ: mỗi tiến trình nhìn thấy không gian địa chỉ ảo riêng.

Ảo hóa lưu trữ: hệ thống tệp biến các khối thô thành cây tệp có tên.

Ảo hóa mạng: socket cung cấp điểm cuối giao tiếp trên các gói tin của card mạng.

Lớp trừu tượng biến chi tiết phần cứng thành hợp đồng dễ sử dụng nhưng không xóa giới hạn vật lý. CPU, RAM, đĩa và mạng vẫn có dung lượng hữu hạn và độ trễ thực tế.

> **Chuyển mạch:** Ở chặng này của **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Không gian người dùng và không gian kernel** tiếp nhận điểm tựa từ **Ảo hóa thời gian và không gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngắt, ngoại lệ và syscall** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Không gian người dùng và không gian kernel

**Không gian kernel (kernel space)** thường chỉ vùng địa chỉ hoặc ngữ cảnh thực thi có đặc quyền; **không gian người dùng (user space)** là môi trường của các tiến trình thông thường. Dữ liệu đi qua ranh giới này thường cần được kiểm tra, sao chép hoặc chia sẻ thông qua ánh xạ bộ nhớ được kiểm soát.

Các kỹ thuật **không sao chép hoặc giảm sao chép (zero-copy)** như `mmap`, `sendfile`, bộ đệm DMA hoặc scatter/gather cố tránh những lần sao chép dư thừa, nhưng hệ thống vẫn phải kiểm soát quyền sở hữu và vòng đời dữ liệu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Ngắt, ngoại lệ và syscall** tiếp nhận điểm tựa từ **Không gian người dùng và không gian kernel** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khởi động hệ điều hành ở mức mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngắt, ngoại lệ và syscall

Cả ba đều có thể chuyển quyền điều khiển vào kernel nhưng nguyên nhân khác nhau. **Ngắt phần cứng (interrupt)** đến từ thiết bị hoặc bộ định thời. **Ngoại lệ CPU (exception)** phát sinh từ lệnh hiện tại, ví dụ lỗi trang. **Syscall** là yêu cầu có chủ đích của chương trình người dùng theo quy ước đã định.

Phân biệt này hữu ích khi gỡ lỗi. Lỗi trang có thể là một phần bình thường của cơ chế phân trang theo nhu cầu; segmentation fault thường là phản ứng khi truy cập địa chỉ không hợp lệ; còn syscall thất bại thường trả về mã lỗi.

> **Chuyển mạch:** Trong **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Khởi động hệ điều hành ở mức mô hình tư duy** gom các mảnh từ **Ngắt, ngoại lệ và syscall** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khởi động hệ điều hành ở mức mô hình tư duy

Firmware khởi tạo phần cứng cơ bản, bootloader nạp kernel, kernel thiết lập bộ nhớ, ngắt và trình điều khiển rồi khởi chạy tiến trình `init` hoặc trình quản lý dịch vụ ở không gian người dùng. Điểm quan trọng là bản thân hệ điều hành cũng là phần mềm cần được nạp và trao quyền điều khiển trước khi ứng dụng chạy.

> **Chuyển mạch:** Ở chặng này của **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Mô hình tư duy** gom các mảnh từ **Khởi động hệ điều hành ở mức mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> Hệ điều hành là **bộ trung gian có đặc quyền**. Nó phân phối tài nguyên hữu hạn, cưỡng chế sự cô lập và cung cấp các lớp trừu tượng ổn định. Syscall là cánh cửa có kiểm soát qua ranh giới người dùng ↔ kernel.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Những hiểu lầm thường gặp** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm thường gặp

**“Mọi hàm I/O đều là syscall.”** Bộ đệm của thư viện hoặc thời gian chạy (runtime / 런타임) có thể gom nhiều thao tác trước khi gọi syscall.

**“Mỗi tiến trình có CPU riêng.”** Đó là lớp trừu tượng; bộ lập lịch chia các lõi CPU theo thời gian và chính sách.

**“Kernel là toàn bộ hệ điều hành.”** Một hệ điều hành hoàn chỉnh còn có thư viện không gian người dùng, daemon, shell, GUI và công cụ; kernel là lõi có đặc quyền.

> **Chuyển mạch:** Trong **Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS**, **Kết nối** tiếp nhận điểm tựa từ **Những hiểu lầm thường gặp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Cơ chế đặc quyền CPU trong [CPU/ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) cho kernel khả năng cưỡng chế ranh giới. [Lập lịch tiến trình/luồng](./01_processes_threads_and_scheduling.md), [bộ nhớ ảo](./03_virtual_memory_and_address_spaces.md) và [hệ thống tệp](./04_filesystems_storage_and_io.md) là ba lớp trừu tượng lớn tiếp theo.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
