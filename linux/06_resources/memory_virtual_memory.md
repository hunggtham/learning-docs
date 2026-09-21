# Bộ nhớ, bộ nhớ ảo, page cache và OOM

`free -h` thường làm người mới lo khi cột `free` nhỏ. Linux chủ động dùng phần RAM chưa cần thiết cho ứng dụng làm bộ nhớ đệm để tăng hiệu năng và có thể thu hồi phần bộ nhớ đó khi khối lượng công việc cần. Muốn hiểu **áp lực bộ nhớ (memory pressure)**, cần bỏ mô hình đơn giản "RAM chỉ có đã dùng và còn trống" và chuyển sang cách nhìn gồm **bộ nhớ ảo + trang nhớ + bộ nhớ đệm có thể thu hồi + tập trang đang hoạt động của tiến trình**.

## Tại sao cần bộ nhớ ảo?

Nếu mỗi tiến trình trực tiếp dùng địa chỉ RAM vật lý, việc cô lập và phân bổ bộ nhớ sẽ rất khó. **Bộ nhớ ảo (virtual memory / 가상 메모리)** cung cấp cho mỗi tiến trình một không gian địa chỉ ảo riêng. MMU của CPU và bảng trang (page table) do kernel quản lý ánh xạ các trang ảo tới khung trang vật lý hoặc các trạng thái lưu trữ phía sau khác.

Ứng dụng nhìn thấy một không gian địa chỉ tương đối liên tục và riêng biệt, còn kernel chịu trách nhiệm quản lý ánh xạ thật. Cơ chế này tạo ra sự cô lập, chia sẻ có kiểm soát, tệp ánh xạ bộ nhớ (memory-mapped file) và nạp trang theo nhu cầu (demand paging).

## Trang nhớ (page)

Trong nhiều cơ chế, bộ nhớ được quản lý theo đơn vị gọi là **trang (page)**. Kích thước trang thường là 4 KiB trên nhiều hệ thống nhưng không nên coi đây là giá trị cố định; hệ thống còn có huge pages.

```bash
getconf PAGESIZE
```

Việc dịch địa chỉ qua bảng trang có chi phí, vì vậy CPU có **TLB (Translation Lookaside Buffer)** để lưu tạm kết quả ánh xạ. Đây là mối liên hệ trực tiếp giữa quản lý bộ nhớ của hệ điều hành và kiến trúc máy tính.

## `free -h` và `available`

```bash
free -h
```

Linux dùng RAM cho page cache và nhiều vùng đệm. Cột `free` thấp không tự động có nghĩa hệ thống thiếu bộ nhớ. `available` cố ước lượng lượng bộ nhớ có thể cấp cho khối lượng công việc mới mà không cần phải swap đáng kể, trong đó có tính tới phần bộ nhớ có thể thu hồi.

Vì vậy khi đánh giá áp lực bộ nhớ, `available` thường có ý nghĩa hơn việc chỉ nhìn `free`.

## Page cache

Dữ liệu tệp đã đọc có thể được giữ trong **bộ nhớ đệm trang (page cache)**. Lần đọc sau có thể tránh I/O tới thiết bị lưu trữ nếu trang vẫn còn trong cache. Khi ứng dụng cần RAM, kernel có thể thu hồi các trang cache sạch.

Điều này giải thích vì sao sau khi đọc một tệp lớn, lượng RAM "đã dùng" tăng. Cache không phải rò rỉ bộ nhớ chỉ vì nó chiếm RAM.

Không nên thường xuyên xóa cache trên production chỉ để làm con số `free` đẹp hơn; việc đó có thể làm giảm hiệu năng và che khuất cách hệ thống thực sự quản lý bộ nhớ.

## RSS và VSZ

`ps` thường hiển thị `RSS` và `VSZ`/`VIRT`.

**Kích thước ảo (virtual size)** phản ánh các vùng địa chỉ ảo đã ánh xạ và có thể rất lớn do vùng địa chỉ được đặt trước, tệp ánh xạ hoặc vùng chia sẻ. **RSS (Resident Set Size)** phản ánh lượng trang đang hiện diện trong bộ nhớ vật lý theo cách thống kê của công cụ. Do có bộ nhớ chia sẻ, cộng RSS của nhiều tiến trình không đơn giản bằng tổng RAM vật lý đang sử dụng.

```bash
ps -p <PID> -o pid,%mem,rss,vsz,cmd
```

Một JVM có `VSZ` lớn không đồng nghĩa nó đang chiếm lượng RAM vật lý tương ứng.

## Heap không phải toàn bộ bộ nhớ của tiến trình

Trong Java, `-Xmx` giới hạn heap nhưng tiến trình còn dùng metaspace, code cache, stack của các thread, direct buffer, thư viện native, cấu trúc nội bộ JVM và các tệp ánh xạ bộ nhớ. Vì vậy giới hạn bộ nhớ của host hoặc container phải tính toàn bộ bộ nhớ tiến trình chứ không chỉ heap.

Đây là lý do JVM có heap 3 GiB trong container giới hạn 4 GiB vẫn có thể gặp OOM với một số khối lượng công việc.

## Swap

Swap cung cấp vùng lưu trữ phía sau cho các trang bộ nhớ ẩn danh khi kernel cần giải phóng RAM. Swap chậm hơn RAM rất nhiều, nhưng việc có một lượng dữ liệu nằm trong swap không tự động có nghĩa hệ thống đang lỗi.

```bash
swapon --show
free -h
vmstat 1
```

Trong `vmstat`, `si`/`so` duy trì ở mức đáng kể có thể cho thấy hệ thống đang tích cực đưa trang vào và ra swap. Cần đối chiếu hiện tượng này với độ trễ và khối lượng công việc.

## Áp lực bộ nhớ và thu hồi

Khi bộ nhớ `free`/`available` giảm, kernel cố thu hồi cache và có thể dùng swap tùy chính sách. Nếu không thể đáp ứng yêu cầu cấp phát, Linux có thể kích hoạt **OOM killer (Out Of Memory)** để kết thúc một tiến trình nhằm bảo vệ hệ thống.

Kiểm tra bằng chứng từ kernel:

```bash
journalctl -k | grep -i -E 'oom|out of memory|killed process'
```

Nếu tiến trình Java biến mất và nhật ký ứng dụng dừng đột ngột, đây là một trong những kiểm tra quan trọng nhất.

## OOM trong container và trên host

Giới hạn bộ nhớ của cgroup có thể nhỏ hơn nhiều so với RAM của host. Tiến trình trong container có thể bị OOM do chạm giới hạn cgroup dù `free -h` trên host vẫn cho thấy còn nhiều bộ nhớ. Vì vậy phải biết khối lượng công việc đang chạy trong miền tài nguyên nào.

Xem [Linux và container](../09_production/linux_containers.md) để hiểu mối liên hệ với cgroup.

## Rò rỉ bộ nhớ

**Rò rỉ bộ nhớ (memory leak)** là tình huống bộ nhớ đã cấp phát không còn hữu ích nhưng vẫn bị giữ lại hoặc không được giải phóng theo vòng đời mong muốn. Không nên kết luận có leak chỉ từ một ảnh chụp cho thấy bộ nhớ cao. Cần xem xu hướng: bộ nhớ có tăng theo thời gian hoặc tải, có giảm sau vòng đời dự kiến không, và bằng chứng ở heap/native cho thấy gì.

Với JVM, có thể cần heap dump, histogram đối tượng hoặc metrics GC. `RSS` ở tầng Linux chỉ cho thấy triệu chứng bộ nhớ của tiến trình, không chỉ ra đối tượng Java nào đang giữ bộ nhớ.

## `vmstat`

```bash
vmstat 1 10
```

Công cụ này cung cấp góc nhìn gọn về tác vụ có thể chạy, bộ nhớ, swap, I/O và CPU. Các trường cần được đọc cùng nhau. Ví dụ RAM trống thấp nhưng không có hoạt động swap và `available` vẫn khỏe có thể hoàn toàn bình thường; ngược lại swap vào/ra liên tục cùng độ trễ tăng là bằng chứng mạnh hơn về áp lực bộ nhớ.

## NUMA và huge pages

Trên máy chủ lớn, độ trễ truy cập RAM có thể khác nhau giữa các socket CPU, tạo mô hình **NUMA (Non-Uniform Memory Access)**. Huge pages giảm chi phí bảng trang và TLB trong một số khối lượng công việc. Đây là các chủ đề quan trọng với cơ sở dữ liệu, JVM và tối ưu hiệu năng, nhưng không nên bật hoặc tắt theo khuyến nghị chung chung; quyết định phải dựa vào nền tảng và workload thực tế.

## Mô hình tư duy (Mental Model)

Đừng coi RAM là một chiếc hộp chia thành "ứng dụng" và "còn trống". Hãy coi nó là một tập hợp các trang mà kernel liên tục phân bổ giữa vùng làm việc của tiến trình, page cache và nhu cầu của kernel. Không gian địa chỉ ảo của tiến trình là góc nhìn logic; việc trang nào đang thực sự nằm trong RAM vật lý là trạng thái động.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"RAM `free` thấp nghĩa là sắp hết RAM."** Cache có thể được thu hồi; cần nhìn `available` và các bằng chứng về áp lực bộ nhớ.

**"VSZ là lượng RAM tiến trình đang chiếm."** Ánh xạ ảo khác với lượng trang hiện diện trong RAM vật lý.

**"`Xmx` bằng tổng bộ nhớ Java sử dụng."** JVM còn nhiều thành phần native và ngoài heap.

**"Có dữ liệu trong swap nghĩa là server đang swap liên tục."** Lượng swap đang chứa dữ liệu khác với hoạt động swap vào/ra đang diễn ra.

**"Tiến trình biến mất chắc chắn do ứng dụng crash."** Kernel hoặc cgroup OOM có thể đã kết thúc nó.

**"Xóa cache giúp server nhanh hơn."** Thường ngược lại vì làm mất dữ liệu cache hữu ích; chỉ thực hiện khi có lý do cụ thể.

## Kết nối kiến thức

Bộ nhớ nối với hệ thống tệp thông qua page cache, với CPU thông qua page fault và TLB, và với container thông qua giới hạn cgroup. [CPU, lập lịch và hiệu năng](./cpu_scheduling_performance.md) tiếp tục cách đọc các chỉ số tài nguyên như một hệ thống thống nhất thay vì những con số rời rạc.