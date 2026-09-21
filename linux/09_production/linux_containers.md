# Các cơ chế Linux phía sau container

Container thường được giới thiệu như "máy ảo nhẹ". Cách so sánh này tiện để hình dung ban đầu nhưng dễ gây hiểu sai. Container Linux thông thường không khởi động một kernel riêng như máy ảo (VM). Các tiến trình trong container vẫn là tiến trình Linux dùng **kernel của host**, nhưng kernel cung cấp cho chúng góc nhìn và ranh giới tài nguyên khác nhau thông qua namespace, cgroup và nhiều cơ chế bảo mật.

## Container muốn giải quyết vấn đề gì?

Ứng dụng cần một môi trường tương đối có thể tái tạo: hệ thống tệp, thư viện, cây tiến trình, giao diện mạng và giới hạn tài nguyên. Nếu mọi ứng dụng đều chạy trực tiếp trên host, dependency và vòng đời của chúng dễ xung đột với nhau.

Container đóng gói một hệ thống tệp không gian người dùng hoặc ảnh (image), sau đó dùng các cơ chế cô lập của kernel để mỗi khối lượng công việc có góc nhìn riêng mà không cần một guest kernel đầy đủ.

## Namespace: cô lập góc nhìn

**Vùng tên (namespace)** của Linux cho tiến trình nhìn một phần hoặc một phiên bản riêng của một số tài nguyên vốn có phạm vi toàn hệ thống. Các loại namespace thường gặp liên quan tới PID, mount, mạng, IPC, UTS, người dùng và cgroup.

Ví dụ, PID namespace làm tiến trình trong container thấy một hệ thống đánh số PID riêng. Một tiến trình có thể nhìn thấy mình là `PID 1` trong namespace của container trong khi host nhìn cùng tiến trình bằng một PID khác.

Network namespace cho container giao diện mạng, bảng định tuyến và không gian socket riêng. Virtual Ethernet, bridge hoặc NAT có thể nối namespace đó với host và mạng bên ngoài.

Mount namespace tạo một góc nhìn mount khác, là nền tảng để container có cây hệ thống tệp gốc riêng.

Mô hình tư duy quan trọng là: namespace không nhất thiết tạo ra một tài nguyên vật lý mới; nó thay **khả năng nhìn thấy và ngữ cảnh** của tiến trình đối với một nhóm tài nguyên.

## Cgroup: thống kê và kiểm soát tài nguyên

**Nhóm điều khiển (control groups / cgroups / 컨트롤 그룹)** tổ chức các tiến trình để thống kê hoặc giới hạn tài nguyên như CPU, bộ nhớ và I/O tùy khả năng của phiên bản kernel.

Giới hạn bộ nhớ của container vì vậy có thể nhỏ hơn RAM của host. Tiến trình có thể bị OOM do cgroup dù `free -h` trên host vẫn cho thấy còn nhiều bộ nhớ.

Giới hạn CPU cũng không có nghĩa container sở hữu CPU vật lý riêng. Bộ lập lịch vẫn phân phối CPU của host theo các quy tắc và giới hạn của cgroup.

## Image và hệ thống tệp nhiều lớp

**Ảnh container (container image)** chứa các tệp không gian người dùng như chương trình, thư viện và cấu hình mặc định. Các lớp image giúp tái sử dụng và phân phối hiệu quả. Khi chạy, runtime thường thêm một lớp có thể ghi phía trên các lớp image chỉ đọc.

Điều này giải thích vì sao sửa tệp trực tiếp trong container đang chạy thường không phải phương pháp triển khai bền vững. Khi container được tạo lại từ image, thay đổi trong lớp ghi cũ có thể biến mất.

**Trạng thái mong muốn (desired state)** nên được mô tả trong image, cấu hình và hệ thống quản lý volume thay vì dựa vào các lần chỉnh sửa thủ công giống SSH trong một container tạm thời.

## Volume và dữ liệu bền vững

Lớp ghi của container thường gắn với vòng đời container. Dữ liệu cần tồn tại lâu hơn nên dùng volume, bind mount hoặc hệ thống lưu trữ bên ngoài theo kiến trúc.

Quyền hệ thống tệp vẫn dựa trên ngữ nghĩa `UID`/`GID`. Tên người dùng hiển thị trong host và container có thể khác, nhưng kernel quan tâm tới ánh xạ danh tính dạng số. User namespace còn có thể ánh xạ lại các danh tính này.

## `PID 1` trong container

Tiến trình mang `PID 1` trong namespace có trách nhiệm và ngữ nghĩa signal đáng chú ý. Nếu ứng dụng không xử lý signal hoặc thu nhận trạng thái tiến trình con đúng cách, container có thể dừng chậm hoặc tích lũy zombie. Runtime hoặc một init wrapper có thể hỗ trợ, nhưng vòng đời tiến trình của ứng dụng vẫn cần được thiết kế đúng.

Đây là mối liên hệ trực tiếp với [Tiến trình, luồng, tín hiệu và tác vụ](../04_process/processes_threads_signals_jobs.md).

## Container không phải ranh giới bảo mật tuyệt đối

Namespace, cgroup, capability, seccomp và MAC tạo ra nhiều lớp cô lập. Tuy nhiên container vẫn chia sẻ kernel với host, vì vậy lỗ hổng kernel hoặc quyền quá rộng có thể làm tăng rủi ro.

Chạy container với `--privileged`, gắn socket hoặc hệ thống tệp nhạy cảm của host, hay cấp capability quá rộng đều làm mức cô lập yếu đi đáng kể.

Bảo mật container cần nguồn gốc image đáng tin cậy, đặc quyền tối thiểu, hệ thống tệp chỉ đọc khi phù hợp, giảm capabilities, vá lỗi và gia cố host.

## Gỡ lỗi mạng trong container

`localhost` trong network namespace của container thường là loopback của chính namespace đó, không phải host. Nếu ứng dụng trong container gọi `localhost:5432`, nó đang tìm dịch vụ trong cùng ngữ cảnh mạng, trừ khi dùng một chế độ mạng đặc biệt.

Khi gỡ lỗi cần biết câu lệnh đang chạy trong namespace của host hay của container. Đây là ví dụ cho thấy cùng một địa chỉ có thể mang ý nghĩa khác nhau tùy ngữ cảnh namespace.

## Liên hệ với Docker và Kubernetes

Docker, containerd và các runtime theo CRI điều phối các cơ chế kernel, quản lý image và vòng đời container. Kubernetes bổ sung lập lịch, trạng thái mong muốn, khám phá dịch vụ và các lớp trừu tượng mạng/lưu trữ trên nhiều node.

Hiểu mô hình tiến trình, mạng và hệ thống tệp của Linux làm việc gỡ lỗi Kubernetes bớt "ma thuật": pod crash vẫn liên quan vòng đời tiến trình; quyền volume vẫn liên quan danh tính của hệ thống tệp; kết nối service cuối cùng vẫn đi qua DNS, IP và socket.

## Mô hình tư duy (Mental Model)

Container có thể được hiểu là **các tiến trình + góc nhìn bị giới hạn + kiểm soát tài nguyên + hệ thống tệp được đóng gói**, chứ không phải một máy tính thu nhỏ hoàn toàn độc lập.

```text
kernel của host
├── namespace/view A + cgroup A + filesystem A
└── namespace/view B + cgroup B + filesystem B
```

Máy ảo khác ở chỗ hệ điều hành khách thường có kernel riêng chạy trên ranh giới phần cứng được ảo hóa.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"Container có kernel riêng."** Container Linux thông thường dùng chung kernel của host.

**"Host còn RAM thì container không thể OOM."** Giới hạn bộ nhớ của cgroup có thể thấp hơn nhiều so với lượng RAM host còn khả dụng.

**"Sửa tệp trong container chính là deploy."** Khi container được tạo lại, thay đổi trong lớp ghi có thể mất.

**"`localhost` trong container là host."** Thông thường đó là loopback của network namespace hiện tại.

**"Container mặc định là sandbox bảo mật tuyệt đối."** Mức cô lập phụ thuộc các cơ chế kernel và cấu hình đặc quyền của runtime.

## Kết nối kiến thức

Container là nơi gần như toàn bộ khái niệm Linux trong thư viện hội tụ: tiến trình, namespace, hệ thống tệp, `UID`/`GID`, giới hạn CPU/bộ nhớ bằng cgroup, socket, mạng và signal. Vì vậy học Linux từ nguyên lý nền tảng giúp các công cụ container dễ hiểu hơn rất nhiều.