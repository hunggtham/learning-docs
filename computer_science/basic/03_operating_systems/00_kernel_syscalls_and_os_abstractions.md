# Nhân hệ điều hành, lời gọi hệ thống và các lớp trừu tượng OS

**Hệ điều hành (Operating System — OS / 운영체제)** giải quyết một mâu thuẫn cơ bản: nhiều chương trình muốn dùng chung CPU, bộ nhớ, lưu trữ và thiết bị, nhưng nếu mỗi chương trình điều khiển phần cứng trực tiếp thì việc cô lập, chia sẻ và hỗ trợ nhiều loại phần cứng gần như không thể quản lý. Hệ điều hành đặt một **nhân có đặc quyền (privileged kernel)** giữa ứng dụng và phần cứng, sau đó cung cấp các lớp trừu tượng ổn định như tiến trình, bộ nhớ ảo, tệp và socket.

## Nhân hệ điều hành là phần có quyền đặc biệt

**Nhân hệ điều hành (kernel / 커널)** chạy ở mức đặc quyền CPU cao, quản lý bảng trang, ngắt, trình điều khiển thiết bị, lập lịch và các tài nguyên được bảo vệ. Ứng dụng thông thường chạy ở **chế độ người dùng (user mode)** với quyền hạn chế.

Ranh giới này được phần cứng cưỡng chế. Nếu một tiến trình bình thường có thể tự sửa bảng trang hoặc đọc tùy ý bộ nhớ vật lý thì sự cô lập giữa các tiến trình sẽ không còn tồn tại.

Thiết kế kernel có nhiều dạng. Kernel nguyên khối như Linux đặt nhiều hệ thống con và trình điều khiển trong không gian kernel. Triết lý **vi nhân (microkernel)** đưa nhiều dịch vụ ra không gian người dùng và giữ kernel nhỏ hơn. Hệ thống lai kết hợp cả hai. Mỗi cách đánh đổi giữa hiệu năng, khả năng cô lập lỗi và độ phức tạp.

## Lời gọi hệ thống

**Lời gọi hệ thống (system call / syscall / 시스템 호출)** là lối vào có kiểm soát từ chế độ người dùng sang kernel để yêu cầu thao tác cần đặc quyền, ví dụ `read`, `write`, `open`, `mmap`, `fork` hoặc `socket`. API của ngôn ngữ hoặc thư viện có thể bao bọc syscall; không phải mọi lời gọi thư viện đều tạo syscall.

Ví dụ `printf` có thể định dạng dữ liệu hoàn toàn trong không gian người dùng rồi chỉ gọi `write` khi bộ đệm cần được đẩy ra. Tương tự, `malloc` có thể cấp phát từ vùng heap đã có và chỉ thỉnh thoảng xin thêm trang bộ nhớ từ hệ điều hành.

Syscall có chi phí do chuyển mức đặc quyền, kiểm tra đầu vào và thực hiện công việc trong kernel. Các kernel và môi trường thực thi hiện đại giảm chi phí này bằng gom nhóm thao tác (batching), bộ nhớ chia sẻ và giao diện I/O bất đồng bộ.

## Bộ mô tả tệp và handle

Hệ điều hành kiểu Unix dùng **bộ mô tả tệp (file descriptor)**, tức một số nguyên làm chỉ mục vào bảng tài nguyên đang mở của từng tiến trình. Tệp, socket, pipe và thiết bị có thể cùng sử dụng giao diện gần giống `read`/`write`. Câu “mọi thứ là tệp” không hoàn toàn đúng theo nghĩa đen, nhưng giao diện I/O thống nhất giúp các thành phần dễ kết hợp hơn.

Windows dùng khái niệm **handle** rộng hơn. Nguyên tắc chung là mã ở không gian người dùng giữ một tham chiếu không trong suốt (opaque reference) thay vì trực tiếp nắm đối tượng nội bộ của kernel.

## Trừu tượng tiến trình

**Tiến trình (process)** tạo cảm giác rằng một chương trình có ngữ cảnh thực thi CPU và không gian địa chỉ riêng. Trong thực tế, bộ lập lịch chia thời gian CPU giữa nhiều tác vụ có thể chạy, còn bộ nhớ ảo ánh xạ các địa chỉ trông như riêng tư sang các trang vật lý có thể được chia sẻ hoặc sao chép khi ghi.

Vì vậy có thể xem hệ điều hành như **bộ phân phối tài nguyên và lớp cô lập**.

## Ảo hóa thời gian và không gian

Ảo hóa CPU: bộ lập lịch làm nhiều tiến trình cùng có cảm giác đang tiến triển.

Ảo hóa bộ nhớ: mỗi tiến trình nhìn thấy không gian địa chỉ ảo riêng.

Ảo hóa lưu trữ: hệ thống tệp biến các khối thô thành cây tệp có tên.

Ảo hóa mạng: socket cung cấp điểm cuối giao tiếp trên các gói tin của card mạng.

Lớp trừu tượng biến chi tiết phần cứng thành hợp đồng dễ sử dụng nhưng không xóa giới hạn vật lý. CPU, RAM, đĩa và mạng vẫn có dung lượng hữu hạn và độ trễ thực tế.

## Không gian người dùng và không gian kernel

**Không gian kernel (kernel space)** thường chỉ vùng địa chỉ hoặc ngữ cảnh thực thi có đặc quyền; **không gian người dùng (user space)** là môi trường của các tiến trình thông thường. Dữ liệu đi qua ranh giới này thường cần được kiểm tra, sao chép hoặc chia sẻ thông qua ánh xạ bộ nhớ được kiểm soát.

Các kỹ thuật **không sao chép hoặc giảm sao chép (zero-copy)** như `mmap`, `sendfile`, bộ đệm DMA hoặc scatter/gather cố tránh những lần sao chép dư thừa, nhưng hệ thống vẫn phải kiểm soát quyền sở hữu và vòng đời dữ liệu.

## Ngắt, ngoại lệ và syscall

Cả ba đều có thể chuyển quyền điều khiển vào kernel nhưng nguyên nhân khác nhau. **Ngắt phần cứng (interrupt)** đến từ thiết bị hoặc bộ định thời. **Ngoại lệ CPU (exception)** phát sinh từ lệnh hiện tại, ví dụ lỗi trang. **Syscall** là yêu cầu có chủ đích của chương trình người dùng theo quy ước đã định.

Phân biệt này hữu ích khi gỡ lỗi. Lỗi trang có thể là một phần bình thường của cơ chế phân trang theo nhu cầu; segmentation fault thường là phản ứng khi truy cập địa chỉ không hợp lệ; còn syscall thất bại thường trả về mã lỗi.

## Khởi động hệ điều hành ở mức mô hình tư duy

Firmware khởi tạo phần cứng cơ bản, bootloader nạp kernel, kernel thiết lập bộ nhớ, ngắt và trình điều khiển rồi khởi chạy tiến trình `init` hoặc trình quản lý dịch vụ ở không gian người dùng. Điểm quan trọng là bản thân hệ điều hành cũng là phần mềm cần được nạp và trao quyền điều khiển trước khi ứng dụng chạy.

## Mô hình tư duy

> Hệ điều hành là **bộ trung gian có đặc quyền**. Nó phân phối tài nguyên hữu hạn, cưỡng chế sự cô lập và cung cấp các lớp trừu tượng ổn định. Syscall là cánh cửa có kiểm soát qua ranh giới người dùng ↔ kernel.

## Những hiểu lầm thường gặp

**“Mọi hàm I/O đều là syscall.”** Bộ đệm của thư viện hoặc runtime có thể gom nhiều thao tác trước khi gọi syscall.

**“Mỗi tiến trình có CPU riêng.”** Đó là lớp trừu tượng; bộ lập lịch chia các lõi CPU theo thời gian và chính sách.

**“Kernel là toàn bộ hệ điều hành.”** Một hệ điều hành hoàn chỉnh còn có thư viện không gian người dùng, daemon, shell, GUI và công cụ; kernel là lõi có đặc quyền.

## Kết nối

Cơ chế đặc quyền CPU trong [CPU/ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) cho kernel khả năng cưỡng chế ranh giới. [Lập lịch tiến trình/luồng](./01_processes_threads_and_scheduling.md), [bộ nhớ ảo](./03_virtual_memory_and_address_spaces.md) và [hệ thống tệp](./04_filesystems_storage_and_io.md) là ba lớp trừu tượng lớn tiếp theo.