# Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Bộ chứa (container / 컨테이너) muốn giải quyết vấn đề gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Không gian tên (namespace / 네임스페이스): cô lập góc nhìn** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Linux containers với namespaces, cgroups và image lifecycle, để hiểu cô lập tài nguyên nào được đảm bảo và giới hạn nào còn lại.

Bộ chứa (container / 컨테이너) thường được giới thiệu như "máy ảo nhẹ". Cách so sánh này tiện để hình dung ban đầu nhưng dễ gây hiểu sai. bộ chứa (container / 컨테이너) Linux thông thường không khởi động một kernel riêng như máy ảo (VM). Các tiến trình trong bộ chứa (container / 컨테이너) vẫn là tiến trình Linux dùng **kernel của host**, nhưng kernel cung cấp cho chúng góc nhìn và ranh giới tài nguyên khác nhau thông qua không gian tên (namespace / 네임스페이스), cgroup và nhiều cơ chế bảo mật.

## Bộ chứa (container / 컨테이너) muốn giải quyết vấn đề gì?

Ứng dụng cần một môi trường tương đối có thể tái tạo: hệ thống tệp, thư viện, cây tiến trình, giao diện mạng và giới hạn tài nguyên. Nếu mọi ứng dụng đều chạy trực tiếp trên host, phụ thuộc (dependency / 의존성) và vòng đời của chúng dễ xung đột với nhau.

Bộ chứa (container / 컨테이너) đóng gói một hệ thống tệp không gian người dùng hoặc ảnh (image / 이미지), sau đó dùng các cơ chế cô lập của kernel để mỗi khối lượng công việc có góc nhìn riêng mà không cần một guest kernel đầy đủ.

> **Nối mạch:** Trong **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Không gian tên (namespace / 네임스페이스): cô lập góc nhìn** nối từ **Bộ chứa (container / 컨테이너) muốn giải quyết vấn đề gì?** sang **Cgroup: thống kê và kiểm soát tài nguyên**, vì cơ chế trước tạo đầu vào cho bước sau.

## Không gian tên (namespace / 네임스페이스): cô lập góc nhìn

**Vùng tên (namespace)** của Linux cho tiến trình nhìn một phần hoặc một phiên bản riêng của một số tài nguyên vốn có phạm vi toàn hệ thống. Các loại không gian tên (namespace / 네임스페이스) thường gặp liên quan tới PID, mount, mạng, IPC, UTS, người dùng và cgroup.

Ví dụ, PID không gian tên (namespace / 네임스페이스) làm tiến trình trong bộ chứa (container / 컨테이너) thấy một hệ thống đánh số PID riêng. Một tiến trình có thể nhìn thấy mình là `PID 1` trong không gian tên (namespace / 네임스페이스) của bộ chứa (container / 컨테이너) trong khi host nhìn cùng tiến trình bằng một PID khác.

Mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) cho bộ chứa (container / 컨테이너) giao diện mạng, bảng định tuyến và không gian socket riêng. Virtual Ethernet, cầu nối (bridge / 브리지) hoặc NAT có thể nối không gian tên (namespace / 네임스페이스) đó với host và mạng bên ngoài.

Mount không gian tên (namespace / 네임스페이스) tạo một góc nhìn mount khác, là nền tảng để bộ chứa (container / 컨테이너) có cây hệ thống tệp gốc riêng.

Mô hình tư duy quan trọng là: không gian tên (namespace / 네임스페이스) không nhất thiết tạo ra một tài nguyên vật lý mới; nó thay **khả năng nhìn thấy và ngữ cảnh** của tiến trình đối với một nhóm tài nguyên.

> **Nối mạch:** Ở chặng này của **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Cgroup: thống kê và kiểm soát tài nguyên** nối từ **Không gian tên (namespace / 네임스페이스): cô lập góc nhìn** sang **Ảnh (image / 이미지) và hệ thống tệp nhiều lớp**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cgroup: thống kê và kiểm soát tài nguyên

**Nhóm điều khiển (control groups / cgroups / 컨트롤 그룹)** tổ chức các tiến trình để thống kê hoặc giới hạn tài nguyên như CPU, bộ nhớ và I/O tùy khả năng của phiên bản kernel.

Giới hạn bộ nhớ của bộ chứa (container / 컨테이너) vì vậy có thể nhỏ hơn RAM của host. Tiến trình có thể bị OOM do cgroup dù `free -h` trên host vẫn cho thấy còn nhiều bộ nhớ.

Giới hạn CPU cũng không có nghĩa bộ chứa (container / 컨테이너) sở hữu CPU vật lý riêng. Bộ lập lịch vẫn phân phối CPU của host theo các quy tắc và giới hạn của cgroup.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Ảnh (image / 이미지) và hệ thống tệp nhiều lớp** nối từ **Cgroup: thống kê và kiểm soát tài nguyên** sang **Volume và dữ liệu bền vững**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ảnh (image / 이미지) và hệ thống tệp nhiều lớp

**Ảnh bộ chứa (container / 컨테이너) (container image)** chứa các tệp không gian người dùng như chương trình, thư viện và cấu hình mặc định. Các lớp ảnh (image / 이미지) giúp tái sử dụng và phân phối hiệu quả. Khi chạy, thời gian chạy (runtime / 런타임) thường thêm một lớp có thể ghi phía trên các lớp ảnh (image / 이미지) chỉ đọc.

Điều này giải thích vì sao sửa tệp trực tiếp trong bộ chứa (container / 컨테이너) đang chạy thường không phải phương pháp triển khai bền vững. Khi bộ chứa (container / 컨테이너) được tạo lại từ ảnh (image / 이미지), thay đổi trong lớp ghi cũ có thể biến mất.

**Trạng thái mong muốn (desired state)** nên được mô tả trong ảnh (image / 이미지), cấu hình và hệ thống quản lý volume thay vì dựa vào các lần chỉnh sửa thủ công giống SSH trong một bộ chứa (container / 컨테이너) tạm thời.

> **Nối mạch:** Trong **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Ảnh (image / 이미지) và hệ thống tệp nhiều lớp** đặt vấn đề; **Volume và dữ liệu bền vững** đối chiếu bằng chứng, rồi **PID 1 trong bộ chứa (container / 컨테이너)** mở rộng hệ quả hoặc giới hạn liên quan.

## Volume và dữ liệu bền vững

Lớp ghi của bộ chứa (container / 컨테이너) thường gắn với vòng đời bộ chứa (container / 컨테이너). Dữ liệu cần tồn tại lâu hơn nên dùng volume, bind mount hoặc hệ thống lưu trữ bên ngoài theo kiến trúc.

Quyền hệ thống tệp vẫn dựa trên ngữ nghĩa `UID`/`GID`. Tên người dùng hiển thị trong host và bộ chứa (container / 컨테이너) có thể khác, nhưng kernel quan tâm tới ánh xạ danh tính dạng số. người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) còn có thể ánh xạ lại các danh tính này.

> **Nối mạch:** Ở chặng này của **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Volume và dữ liệu bền vững** đặt vấn đề; **PID 1 trong bộ chứa (container / 컨테이너)** đối chiếu bằng chứng, rồi **Bộ chứa (container / 컨테이너) không phải ranh giới bảo mật tuyệt đối** mở rộng hệ quả hoặc giới hạn liên quan.

## `PID 1` trong bộ chứa (container / 컨테이너)

Tiến trình mang `PID 1` trong không gian tên (namespace / 네임스페이스) có trách nhiệm và ngữ nghĩa tín hiệu (signal / 신호) đáng chú ý. Nếu ứng dụng không xử lý tín hiệu (signal / 신호) hoặc thu nhận trạng thái tiến trình con đúng cách, bộ chứa (container / 컨테이너) có thể dừng chậm hoặc tích lũy zombie. thời gian chạy (runtime / 런타임) hoặc một init wrapper có thể hỗ trợ, nhưng vòng đời tiến trình của ứng dụng vẫn cần được thiết kế đúng.

Đây là mối liên hệ trực tiếp với [Tiến trình, luồng, tín hiệu và tác vụ](../04_process/processes_threads_signals_jobs.md).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Bộ chứa (container / 컨테이너) không phải ranh giới bảo mật tuyệt đối** nối từ **PID 1 trong bộ chứa (container / 컨테이너)** sang **Gỡ lỗi mạng trong bộ chứa (container / 컨테이너)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bộ chứa (container / 컨테이너) không phải ranh giới bảo mật tuyệt đối

Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량), seccomp và MAC tạo ra nhiều lớp cô lập. Tuy nhiên bộ chứa (container / 컨테이너) vẫn chia sẻ kernel với host, vì vậy lỗ hổng kernel hoặc quyền quá rộng có thể làm tăng rủi ro.

Chạy bộ chứa (container / 컨테이너) với `--privileged`, gắn socket hoặc hệ thống tệp nhạy cảm của host, hay cấp năng lực (capability / 역량) quá rộng đều làm mức cô lập yếu đi đáng kể.

Bảo mật bộ chứa (container / 컨테이너) cần nguồn gốc ảnh (image / 이미지) đáng tin cậy, đặc quyền tối thiểu, hệ thống tệp chỉ đọc khi phù hợp, giảm capabilities, vá lỗi và gia cố host.

> **Nối mạch:** Trong **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Gỡ lỗi mạng trong bộ chứa (container / 컨테이너)** nối từ **Bộ chứa (container / 컨테이너) không phải ranh giới bảo mật tuyệt đối** sang **Liên hệ với Docker và Kubernetes**, vì cơ chế trước tạo đầu vào cho bước sau.

## Gỡ lỗi mạng trong bộ chứa (container / 컨테이너)

`localhost` trong mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) của bộ chứa (container / 컨테이너) thường là loopback của chính không gian tên (namespace / 네임스페이스) đó, không phải host. Nếu ứng dụng trong bộ chứa (container / 컨테이너) gọi `localhost:5432`, nó đang tìm dịch vụ trong cùng ngữ cảnh mạng, trừ khi dùng một chế độ mạng đặc biệt.

Khi gỡ lỗi cần biết câu lệnh đang chạy trong không gian tên (namespace / 네임스페이스) của host hay của bộ chứa (container / 컨테이너). Đây là ví dụ cho thấy cùng một địa chỉ có thể mang ý nghĩa khác nhau tùy ngữ cảnh không gian tên (namespace / 네임스페이스).

> **Nối mạch:** Ở chặng này của **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Liên hệ với Docker và Kubernetes** nối từ **Gỡ lỗi mạng trong bộ chứa (container / 컨테이너)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Liên hệ với Docker và Kubernetes

Docker, containerd và các thời gian chạy (runtime / 런타임) theo CRI điều phối các cơ chế kernel, quản lý ảnh (image / 이미지) và vòng đời bộ chứa (container / 컨테이너). Kubernetes bổ sung lập lịch, trạng thái mong muốn, khám phá dịch vụ và các lớp trừu tượng mạng/lưu trữ trên nhiều nút (node / 노드).

Hiểu mô hình tiến trình, mạng và hệ thống tệp của Linux làm việc gỡ lỗi Kubernetes bớt "ma thuật": pod crash vẫn liên quan vòng đời tiến trình; quyền volume vẫn liên quan danh tính của hệ thống tệp; kết nối dịch vụ (service / 서비스) cuối cùng vẫn đi qua DNS, IP và socket.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên hệ với Docker và Kubernetes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Bộ chứa (container / 컨테이너) có thể được hiểu là **các tiến trình + góc nhìn bị giới hạn + kiểm soát tài nguyên + hệ thống tệp được đóng gói**, chứ không phải một máy tính thu nhỏ hoàn toàn độc lập.

```text
kernel của host
├── namespace/view A + cgroup A + filesystem A
└── namespace/view B + cgroup B + filesystem B
```

Máy ảo khác ở chỗ hệ điều hành khách thường có kernel riêng chạy trên ranh giới phần cứng được ảo hóa.

> **Nối mạch:** Trong **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Những hiểu lầm phổ biến (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"bộ chứa (container / 컨테이너) có kernel riêng."** bộ chứa (container / 컨테이너) Linux thông thường dùng chung kernel của host.

**"Host còn RAM thì bộ chứa (container / 컨테이너) không thể OOM."** Giới hạn bộ nhớ của cgroup có thể thấp hơn nhiều so với lượng RAM host còn khả dụng.

**"Sửa tệp trong bộ chứa (container / 컨테이너) chính là deploy."** Khi bộ chứa (container / 컨테이너) được tạo lại, thay đổi trong lớp ghi có thể mất.

**"`localhost` trong bộ chứa (container / 컨테이너) là host."** Thông thường đó là loopback của mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) hiện tại.

**"bộ chứa (container / 컨테이너) mặc định là sandbox bảo mật tuyệt đối."** Mức cô lập phụ thuộc các cơ chế kernel và cấu hình đặc quyền của thời gian chạy (runtime / 런타임).

> **Nối mạch:** Ở chặng này của **Các cơ chế Linux phía sau bộ chứa (container / 컨테이너)**, **Kết nối kiến thức** nối từ **Những hiểu lầm phổ biến (Common Misconceptions)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết nối kiến thức

Bộ chứa (container / 컨테이너) là nơi gần như toàn bộ khái niệm Linux trong thư viện hội tụ: tiến trình, không gian tên (namespace / 네임스페이스), hệ thống tệp, `UID`/`GID`, giới hạn CPU/bộ nhớ bằng cgroup, socket, mạng và tín hiệu (signal / 신호). Vì vậy học Linux từ nguyên lý nền tảng giúp các công cụ bộ chứa (container / 컨테이너) dễ hiểu hơn rất nhiều.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
