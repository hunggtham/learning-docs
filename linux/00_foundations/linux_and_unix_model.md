# Mô hình hệ thống Linux và Unix

> **Mạch đọc:** Đọc **Mô hình hệ thống Linux và Unix** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Vì sao cần hệ điều hành?** sang **Linux, Unix và GNU**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi mới tiếp xúc máy chủ (server / 서버) qua PuTTY hoặc SSH, Linux dễ tạo cảm giác rằng hệ điều hành chỉ là một màn hình đen với hàng trăm câu lệnh (command) cần nhớ. Cách nhìn đó khiến việc học nhanh trở thành học thuộc. Trên thực tế, số câu lệnh có thể rất lớn nhưng số lớp trừu tượng (abstraction / 추상화) nền tảng của hệ thống lại ít hơn nhiều. Khi hiểu các lớp trừu tượng này, một câu lệnh mới thường chỉ là một giao diện khác để quan sát hoặc điều khiển một đối tượng đã biết.

## Vì sao cần hệ điều hành?

CPU có thể thực thi chỉ thị (instruction), RAM có thể giữ dữ liệu, thiết bị lưu trữ có thể ghi các byte và giao diện mạng có thể truyền khung dữ liệu (frame). Nhưng nếu mỗi chương trình tự điều khiển trực tiếp toàn bộ phần cứng, hai chương trình có thể ghi vào cùng vùng RAM, tranh chấp cùng thiết bị lưu trữ hoặc làm hỏng dữ liệu của nhau. Hệ điều hành (operating system / 운영체제) tồn tại để biến tài nguyên vật lý thành những lớp trừu tượng có thể chia sẻ, cô lập và kiểm soát.

Hạt nhân Linux (Linux kernel / 커널) cung cấp các lớp trừu tượng quan trọng như **tiến trình (process / 프로세스)**, **bộ nhớ ảo (virtual memory)**, **tệp (file / 파일)**, **ổ cắm mạng (socket)**, **danh tính người dùng (user identity)** và **quyền truy cập (permission)**. Chương trình không cần biết sector vật lý nào chứa `application.yml`; nó chỉ yêu cầu mở một đường dẫn thông qua `open()` hoặc lời gọi tương đương. Máy chủ web không cần tự điều khiển card mạng; nó làm việc với socket. Một ứng dụng Java có cảm giác như đang sở hữu một không gian địa chỉ riêng, dù RAM vật lý đang được chia sẻ với hàng trăm tiến trình khác.

Đây là bước chuyển quan trọng trong **mô hình tư duy (mental model / 사고 모델)**: Linux không chủ yếu là một bộ sưu tập câu lệnh. Nó là một hệ thống quản lý tài nguyên (resource management) thông qua các lớp trừu tượng có quy tắc rõ ràng.


> **Chuyển mạch:** Từ **Vì sao cần hệ điều hành?**, ta sang **Linux, Unix và GNU** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Linux, Unix và GNU

**Unix** ban đầu là một họ hệ điều hành và đồng thời tạo ra nhiều quy ước có ảnh hưởng lâu dài: hệ thống tệp phân cấp, mô hình tiến trình, quyền người dùng/nhóm, bộ mô tả tệp (file descriptor) và các tiện ích nhỏ có thể kết hợp bằng đường ống (pipe). **Linux** chính xác hơn là một hạt nhân do Linus Torvalds khởi đầu năm 1991. Một bản phân phối Linux (Linux distribution / 리눅스 배포판) như Ubuntu, Debian hoặc RHEL kết hợp hạt nhân Linux với công cụ không gian người dùng (user-space tools), thư viện, trình quản lý gói, hệ thống khởi tạo và nhiều phần mềm khác.

Nhiều câu lệnh quen thuộc như `ls`, `cp`, `grep` thường đến từ GNU Coreutils hoặc những dự án không gian người dùng khác chứ không phải bản thân kernel. Sự phân biệt này giải thích vì sao hai bản phân phối cùng dùng Linux kernel nhưng tùy chọn câu lệnh, trình quản lý gói hoặc cách bố trí cấu hình có thể khác nhau.

Trong môi trường Hàn Quốc, Linux thường được gọi là **리눅스**, kernel là **커널**, hệ điều hành là **운영체제** và bản phân phối Linux là **리눅스 배포판**.


> **Chuyển mạch:** Từ **Linux, Unix và GNU**, ta sang **Triết lý Unix và khả năng kết hợp** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Triết lý Unix và khả năng kết hợp

Một tư tưởng nổi tiếng của Unix là tạo những chương trình làm một việc tương đối rõ rồi cho phép chúng kết hợp với nhau. Điều quan trọng không phải khẩu hiệu, mà là một giao diện chung dựa trên luồng văn bản và bộ mô tả tệp.

Ví dụ:

```bash
journalctl -u app | grep ERROR | tail -n 20
```

`journalctl` không cần biết `grep` tồn tại. `grep` cũng không cần một API riêng dành cho systemd. Trình vỏ lệnh (shell) nối đầu ra chuẩn (standard output) của chương trình trước với đầu vào chuẩn (standard input) của chương trình sau. Giao diện nhỏ và ổn định làm khả năng kết hợp (composition) trở nên mạnh.

Điều này liên hệ trực tiếp với kỹ nghệ phần mềm (software engineering / 소프트웨어 공학): một thành phần dễ kết hợp khi nó có trách nhiệm và giao diện rõ ràng. Chuỗi xử lý Unix (Unix pipeline) là một ví dụ sớm của tư duy mô-đun (modularity).


> **Chuyển mạch:** Từ **Triết lý Unix và khả năng kết hợp**, ta sang **"Everything is a tệp (file / 파일)" thực sự có nghĩa gì?** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## "Everything is a tệp (file / 파일)" thực sự có nghĩa gì?

Câu "mọi thứ đều là tệp" hữu ích như một mô hình tư duy nhưng sẽ sai nếu hiểu theo nghĩa đen. Tệp thông thường, thư mục, thiết bị, pipe và socket không phải cùng một loại đối tượng. Ý tưởng sâu hơn là Linux cố gắng đưa nhiều loại tài nguyên về một **giao diện vào/ra (I/O interface) tương đối thống nhất**. Tiến trình nhận một số nguyên gọi là **bộ mô tả tệp (file descriptor)** rồi có thể thực hiện các thao tác như đọc và ghi trên nhiều loại tài nguyên.

Ví dụ `/dev/null` không phải tệp dữ liệu thông thường trên đĩa. Nó là một điểm cuối thiết bị: dữ liệu ghi vào đó bị bỏ đi. Pipe cũng không phải tệp lưu trữ lâu dài, nhưng tiến trình vẫn có thể đọc hoặc ghi thông qua bộ mô tả tệp.

Xem sâu hơn tại [Tệp, luồng dữ liệu và bộ mô tả tệp](../01_filesystem/files_streams_descriptors.md).


> **Chuyển mạch:** Từ **"Everything is a tệp (file / 파일)" thực sự có nghĩa gì?**, ta sang **Vùng tên: tên không phải là đối tượng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Vùng tên: tên không phải là đối tượng

Một trong những hiểu biết quan trọng của Linux là phân biệt **tên (name)** với **đối tượng (object / 객체)**. Đường dẫn `/var/log/app.log` là một tên trong vùng tên của hệ thống tệp, dùng để dẫn tới đối tượng dữ liệu. `PID 1234` là mã định danh của một tiến trình tại một thời điểm. Cổng `8080` là một phần của điểm cuối mạng, không phải bản thân ứng dụng.

Sự phân biệt này giải thích nhiều hiện tượng tưởng như lạ. Xóa tên đường dẫn của một tệp đang được tiến trình mở không nhất thiết giải phóng dung lượng ngay: mục thư mục (directory entry) biến mất nhưng đối tượng vẫn còn được tham chiếu bởi một bộ mô tả tệp đang mở. Một `PID` có thể được kernel tái sử dụng sau khi tiến trình cũ kết thúc. Một dịch vụ (service / 서비스) ở trạng thái "đang chạy" chưa chắc đã lắng nghe đúng cổng mà máy khách cần.

Vì vậy khi xử lý sự cố trong môi trường vận hành thực tế (production), cần kiểm tra nhiều lớp thay vì suy luận từ một dấu hiệu duy nhất.


> **Chuyển mạch:** Từ **Vùng tên: tên không phải là đối tượng**, ta sang **Không gian người dùng và không gian hạt nhân** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Không gian người dùng và không gian hạt nhân

Ứng dụng thông thường chạy trong **không gian người dùng (user space / 사용자 공간)** với quyền CPU bị giới hạn. Kernel chạy ở mức đặc quyền cao hơn và quản lý ánh xạ bộ nhớ, bộ lập lịch (scheduler), hệ thống tệp, ngăn xếp mạng và trình điều khiển phần cứng. Khi ứng dụng cần thao tác một tài nguyên do kernel quản lý, nó đi qua ranh giới của **lời gọi hệ thống (system call / 시스템 호출)**.

Ví dụ Java gọi API để đọc tệp. Sau nhiều lớp của môi trường chạy Java và thư viện C, thao tác cuối cùng vẫn cần kernel đọc dữ liệu từ bộ mô tả tệp. Vì vậy các lỗi như `Permission denied`, `No such file or directory` hoặc `Connection refused` thường phản ánh trạng thái hoặc chính sách của các đối tượng do kernel quản lý, dù lỗi xuất hiện ở tầng khung phần mềm (framework / 프레임워크) của ứng dụng.

Xem chi tiết tại [Kernel, không gian người dùng và lời gọi hệ thống](./kernel_userspace_syscalls.md).


> **Chuyển mạch:** Từ **Không gian người dùng và không gian hạt nhân**, ta sang **Trạng thái, quan sát và thay đổi** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trạng thái, quan sát và thay đổi

Hầu hết câu lệnh quản trị có thể nhìn theo hai vai trò. Một nhóm dùng để **quan sát trạng thái**, ví dụ `ps`, `ss`, `df`, `free`, `ip`, `journalctl`. Nhóm còn lại dùng để **thay đổi trạng thái**, ví dụ `kill`, `rm`, `chmod`, `systemctl restart`, `ip route add`.

Trong vận hành hệ thống ở mức nâng cao, nguyên tắc quan trọng là ưu tiên quan sát trước khi can thiệp. Nếu ứng dụng lỗi và ta khởi động lại ngay, triệu chứng có thể biến mất nhưng bằng chứng như trạng thái tiến trình, trạng thái luồng hoặc áp lực tài nguyên tạm thời cũng có thể mất theo. Quy trình tốt hơn là thu thập đủ bằng chứng để hình thành giả thuyết, sau đó mới thay đổi trạng thái.

Đây chính là phương pháp khoa học (scientific method) ở quy mô vận hành hệ thống: **quan sát → giả thuyết → kiểm tra → can thiệp → xác minh**.


> **Chuyển mạch:** Từ **Trạng thái, quan sát và thay đổi**, ta sang **Các bản phân phối khác nhau ở đâu?** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Các bản phân phối khác nhau ở đâu?

Giao diện cốt lõi của kernel tương đối ổn định, nhưng bản phân phối quyết định nhiều chính sách ở không gian người dùng. Ubuntu/Debian dùng `apt` và gói `.deb`; họ RHEL dùng `dnf` và RPM. Cách đặt tệp cấu hình của cùng một phần mềm cũng có thể khác. Một máy chủ tối giản có thể không cài sẵn `vim`, `tree`, `netstat` hoặc `lsof`.

Do đó khi gặp một câu lệnh "không tồn tại", không nên lập tức kết luận Linux không hỗ trợ chức năng đó. Hãy đặt ba câu hỏi: chức năng thuộc kernel hay công cụ không gian người dùng? Công cụ nằm trong gói nào? Bản phân phối và phiên bản hiện tại là gì?

```bash
cat /etc/os-release
uname -a
command -v lsof
```


> **Chuyển mạch:** Từ **Các bản phân phối khác nhau ở đâu?**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

Có thể hình dung Linux như một thành phố có nhiều lớp quản lý. Phần cứng là hạ tầng vật lý. Kernel là lớp điều phối tài nguyên và thực thi ranh giới bảo vệ. Tiến trình là các hoạt động đang diễn ra. Hệ thống tệp cung cấp vùng tên để tìm dữ liệu và tài nguyên. Người dùng, nhóm và quyền truy cập quyết định ai được phép làm gì. Shell là công cụ để yêu cầu các chương trình quan sát hoặc thay đổi hệ thống.

Phép so sánh này chỉ hữu ích nếu nhớ rằng kernel không phải một "tiến trình quản trị" thông thường; nó hoạt động trong miền đặc quyền khác với tiến trình người dùng.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Những hiểu lầm phổ biến (Common Misconceptions)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Linux là dòng lệnh."** Linux có thể chạy giao diện đồ họa. Dòng lệnh chỉ là một giao diện; máy chủ thường ưu tiên shell vì dễ tự động hóa, truyền qua mạng nhẹ và có khả năng kết hợp cao.

**"Câu lệnh là chức năng của kernel."** Phần lớn câu lệnh là chương trình thực thi trong không gian người dùng. Chúng sử dụng giao diện của kernel để thực hiện công việc.

**"Tiến trình đang chạy nghĩa là dịch vụ hoạt động bình thường."** Tiến trình có thể vẫn tồn tại nhưng bị deadlock, chưa gắn cổng, kiểm tra sức khỏe (health check) thất bại hoặc phụ thuộc bên ngoài bị lỗi. Sức khỏe của hệ thống môi trường vận hành (production / 운영 환경) là kết quả của nhiều lớp.

**"gốc (root / 루트) có nghĩa là không còn giới hạn."** `root` có đặc quyền rất lớn trong host nhưng vẫn chịu các quy tắc của kernel, trạng thái hệ thống tệp, giới hạn tài nguyên, không gian tên (namespace / 네임스페이스) của bộ chứa (container / 컨테이너), cơ chế kiểm soát truy cập bắt buộc và nhiều ranh giới khác.


> **Chuyển mạch:** Từ **Những hiểu lầm phổ biến (Common Misconceptions)**, ta sang **Kết nối sang chương tiếp theo** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối sang chương tiếp theo

Chương này cung cấp từ vựng chung. Để hiểu điều gì xảy ra khi một câu lệnh hoặc ứng dụng yêu cầu hệ điều hành thực hiện công việc, tiếp tục với [Kernel, không gian người dùng và lời gọi hệ thống](./kernel_userspace_syscalls.md). Sau đó, hệ thống tệp và bộ mô tả tệp sẽ cho thấy vì sao đường dẫn, pipe, socket và chuyển hướng có thể ghép thành một mô hình thống nhất.

> **Bàn giao:** Sau **Kết nối sang chương tiếp theo**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [cpu privilege exceptions syscall path](./cpu_privilege_exceptions_syscall_path.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
