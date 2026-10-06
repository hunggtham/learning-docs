# Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tại sao cần bộ nhớ ảo?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Trang nhớ (page)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối virtual memory với page cache, memory pressure và OOM, giúp đọc số liệu `free` theo hành vi thu hồi thay vì chỉ nhìn cột trống.

`free -h` thường làm người mới lo khi cột `free` nhỏ. Linux chủ động dùng phần RAM chưa cần thiết cho ứng dụng làm bộ nhớ đệm để tăng hiệu năng và có thể thu hồi phần bộ nhớ đó khi khối lượng công việc cần. Muốn hiểu **áp lực bộ nhớ (memory pressure)**, cần bỏ mô hình đơn giản "RAM chỉ có đã dùng và còn trống" và chuyển sang cách nhìn gồm **bộ nhớ ảo + trang nhớ + bộ nhớ đệm có thể thu hồi + tập trang đang hoạt động của tiến trình**.

## Tại sao cần bộ nhớ ảo?

Nếu mỗi tiến trình trực tiếp dùng địa chỉ RAM vật lý, việc cô lập và phân bổ bộ nhớ sẽ rất khó. **Bộ nhớ ảo (virtual memory / 가상 메모리)** cung cấp cho mỗi tiến trình một không gian địa chỉ ảo riêng. MMU của CPU và bảng trang (page table / 페이지 테이블) do kernel quản lý ánh xạ các trang ảo tới khung trang vật lý hoặc các trạng thái lưu trữ phía sau khác.

Ứng dụng nhìn thấy một không gian địa chỉ tương đối liên tục và riêng biệt, còn kernel chịu trách nhiệm quản lý ánh xạ thật. Cơ chế này tạo ra sự cô lập, chia sẻ có kiểm soát, tệp ánh xạ bộ nhớ (memory-mapped file) và nạp trang theo nhu cầu (demand paging).

> **Nối mạch:** Trong **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Trang nhớ (page)** nối từ **Tại sao cần bộ nhớ ảo?** sang **free -h và available**, vì cơ chế trước tạo đầu vào cho bước sau.

## Trang nhớ (page)

Trong nhiều cơ chế, bộ nhớ được quản lý theo đơn vị gọi là **trang (page)**. Kích thước trang thường là 4 KiB trên nhiều hệ thống nhưng không nên coi đây là giá trị cố định; hệ thống còn có huge pages.

```bash
getconf PAGESIZE
```

Việc dịch địa chỉ qua bảng trang có chi phí, vì vậy CPU có **TLB (Translation Lookaside Buffer)** để lưu tạm kết quả ánh xạ. Đây là mối liên hệ trực tiếp giữa quản lý bộ nhớ của hệ điều hành và kiến trúc máy tính.

> **Nối mạch:** Ở chặng này của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Trang nhớ (page)** nêu quy tắc; **free -h và available** thử quy tắc trong tình huống, rồi **Page bộ nhớ đệm (cache / 캐시)** mở rộng hệ quả.

## `free -h` và `available`

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
free -h
```

Linux dùng RAM cho page bộ nhớ đệm (cache / 캐시) và nhiều vùng đệm. Cột `free` thấp không tự động có nghĩa hệ thống thiếu bộ nhớ. `available` cố ước lượng lượng bộ nhớ có thể cấp cho khối lượng công việc mới mà không cần phải swap đáng kể, trong đó có tính tới phần bộ nhớ có thể thu hồi.

Vì vậy khi đánh giá áp lực bộ nhớ, `available` thường có ý nghĩa hơn việc chỉ nhìn `free`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **free -h và available** nêu quy tắc; **Page bộ nhớ đệm (cache / 캐시)** thử quy tắc trong tình huống, rồi **RSS và VSZ** mở rộng hệ quả.

## Page bộ nhớ đệm (cache / 캐시)

Dữ liệu tệp đã đọc có thể được giữ trong **bộ nhớ đệm trang (page cache)**. Lần đọc sau có thể tránh I/O tới thiết bị lưu trữ nếu trang vẫn còn trong bộ nhớ đệm (cache / 캐시). Khi ứng dụng cần RAM, kernel có thể thu hồi các trang bộ nhớ đệm (cache / 캐시) sạch.

Điều này giải thích vì sao sau khi đọc một tệp lớn, lượng RAM "đã dùng" tăng. bộ nhớ đệm (cache / 캐시) không phải rò rỉ bộ nhớ chỉ vì nó chiếm RAM.

Không nên thường xuyên xóa bộ nhớ đệm (cache / 캐시) trên môi trường vận hành (production / 운영 환경) chỉ để làm con số `free` đẹp hơn; việc đó có thể làm giảm hiệu năng và che khuất cách hệ thống thực sự quản lý bộ nhớ.

> **Nối mạch:** Trong **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **RSS và VSZ** nối từ **Page bộ nhớ đệm (cache / 캐시)** sang **Vùng nhớ vùng nhớ động (heap / 힙) không phải toàn bộ bộ nhớ của tiến trình**, vì cơ chế trước tạo đầu vào cho bước sau.

## RSS và VSZ

`ps` thường hiển thị `RSS` và `VSZ`/`VIRT`.

**Kích thước ảo (virtual size)** phản ánh các vùng địa chỉ ảo đã ánh xạ và có thể rất lớn do vùng địa chỉ được đặt trước, tệp ánh xạ hoặc vùng chia sẻ. **RSS (Resident Set Size)** phản ánh lượng trang đang hiện diện trong bộ nhớ vật lý theo cách thống kê của công cụ. Do có bộ nhớ chia sẻ, cộng RSS của nhiều tiến trình không đơn giản bằng tổng RAM vật lý đang sử dụng.

```bash
ps -p <PID> -o pid,%mem,rss,vsz,cmd
```

Một JVM có `VSZ` lớn không đồng nghĩa nó đang chiếm lượng RAM vật lý tương ứng.

> **Nối mạch:** Ở chặng này của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Vùng nhớ vùng nhớ động (heap / 힙) không phải toàn bộ bộ nhớ của tiến trình** nối từ **RSS và VSZ** sang **Swap**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vùng nhớ vùng nhớ động (heap / 힙) không phải toàn bộ bộ nhớ của tiến trình

Trong Java, `-Xmx` giới hạn vùng nhớ động (heap / 힙) nhưng tiến trình còn dùng metaspace, mã (code / 코드) bộ nhớ đệm (cache / 캐시), ngăn xếp (stack / 스택) của các luồng thực thi (thread / 스레드), direct buffer, thư viện bản địa (native / 네이티브), cấu trúc nội bộ JVM và các tệp ánh xạ bộ nhớ. Vì vậy giới hạn bộ nhớ của host hoặc bộ chứa (container / 컨테이너) phải tính toàn bộ bộ nhớ tiến trình chứ không chỉ vùng nhớ động (heap / 힙).

Đây là lý do JVM có vùng nhớ động (heap / 힙) 3 GiB trong bộ chứa (container / 컨테이너) giới hạn 4 GiB vẫn có thể gặp OOM với một số khối lượng công việc.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Swap** nối từ **Vùng nhớ vùng nhớ động (heap / 힙) không phải toàn bộ bộ nhớ của tiến trình** sang **Áp lực bộ nhớ và thu hồi**, vì cơ chế trước tạo đầu vào cho bước sau.

## Swap

Swap cung cấp vùng lưu trữ phía sau cho các trang bộ nhớ ẩn danh khi kernel cần giải phóng RAM. Swap chậm hơn RAM rất nhiều, nhưng việc có một lượng dữ liệu nằm trong swap không tự động có nghĩa hệ thống đang lỗi.

```bash
swapon --show
free -h
vmstat 1
```

Trong `vmstat`, `si`/`so` duy trì ở mức đáng kể có thể cho thấy hệ thống đang tích cực đưa trang vào và ra swap. Cần đối chiếu hiện tượng này với độ trễ và khối lượng công việc.

> **Nối mạch:** Trong **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Áp lực bộ nhớ và thu hồi** nối từ **Swap** sang **OOM trong bộ chứa (container / 컨테이너) và trên host**, vì cơ chế trước tạo đầu vào cho bước sau.

## Áp lực bộ nhớ và thu hồi

Khi bộ nhớ `free`/`available` giảm, kernel cố thu hồi bộ nhớ đệm (cache / 캐시) và có thể dùng swap tùy chính sách. Nếu không thể đáp ứng yêu cầu cấp phát, Linux có thể kích hoạt **OOM killer (Out Of memory)** để kết thúc một tiến trình nhằm bảo vệ hệ thống.

Kiểm tra bằng chứng từ kernel:

```bash
journalctl -k | grep -i -E 'oom|out of memory|killed process'
```

Nếu tiến trình Java biến mất và nhật ký ứng dụng dừng đột ngột, đây là một trong những kiểm tra quan trọng nhất.

> **Nối mạch:** Ở chặng này của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **OOM trong bộ chứa (container / 컨테이너) và trên host** nối từ **Áp lực bộ nhớ và thu hồi** sang **Rò rỉ bộ nhớ**, vì cơ chế trước tạo đầu vào cho bước sau.

## OOM trong bộ chứa (container / 컨테이너) và trên host

Giới hạn bộ nhớ của cgroup có thể nhỏ hơn nhiều so với RAM của host. Tiến trình trong bộ chứa (container / 컨테이너) có thể bị OOM do chạm giới hạn cgroup dù `free -h` trên host vẫn cho thấy còn nhiều bộ nhớ. Vì vậy phải biết khối lượng công việc đang chạy trong miền tài nguyên nào.

Xem [Linux và container](../09_production/linux_containers.md) để hiểu mối liên hệ với cgroup.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Rò rỉ bộ nhớ** nối từ **OOM trong bộ chứa (container / 컨테이너) và trên host** sang **vmstat**, vì cơ chế trước tạo đầu vào cho bước sau.

## Rò rỉ bộ nhớ

**Rò rỉ bộ nhớ (memory leak)** là tình huống bộ nhớ đã cấp phát không còn hữu ích nhưng vẫn bị giữ lại hoặc không được giải phóng theo vòng đời mong muốn. Không nên kết luận có leak chỉ từ một ảnh chụp cho thấy bộ nhớ cao. Cần xem xu hướng: bộ nhớ có tăng theo thời gian hoặc tải, có giảm sau vòng đời dự kiến không, và bằng chứng ở vùng nhớ động (heap / 힙)/bản địa (native / 네이티브) cho thấy gì.

Với JVM, có thể cần vùng nhớ động (heap / 힙) dump, histogram đối tượng hoặc metrics GC. `RSS` ở tầng Linux chỉ cho thấy triệu chứng bộ nhớ của tiến trình, không chỉ ra đối tượng Java nào đang giữ bộ nhớ.

> **Nối mạch:** Trong **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **vmstat** nối từ **Rò rỉ bộ nhớ** sang **NUMA và huge pages**, vì cơ chế trước tạo đầu vào cho bước sau.

## `vmstat`

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
vmstat 1 10
```

Công cụ này cung cấp góc nhìn gọn về tác vụ có thể chạy, bộ nhớ, swap, I/O và CPU. Các trường cần được đọc cùng nhau. Ví dụ RAM trống thấp nhưng không có hoạt động swap và `available` vẫn khỏe có thể hoàn toàn bình thường; ngược lại swap vào/ra liên tục cùng độ trễ tăng là bằng chứng mạnh hơn về áp lực bộ nhớ.

> **Nối mạch:** Ở chặng này của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **NUMA và huge pages** nối từ **vmstat** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## NUMA và huge pages

Trên máy chủ lớn, độ trễ truy cập RAM có thể khác nhau giữa các socket CPU, tạo mô hình **NUMA (Non-Uniform memory Access)**. Huge pages giảm chi phí bảng trang và TLB trong một số khối lượng công việc. Đây là các chủ đề quan trọng với cơ sở dữ liệu, JVM và tối ưu hiệu năng, nhưng không nên bật hoặc tắt theo khuyến nghị chung chung; quyết định phải dựa vào nền tảng và tải công việc (workload / 워크로드) thực tế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **NUMA và huge pages** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Đừng coi RAM là một chiếc hộp chia thành "ứng dụng" và "còn trống". Hãy coi nó là một tập hợp các trang mà kernel liên tục phân bổ giữa vùng làm việc của tiến trình, page bộ nhớ đệm (cache / 캐시) và nhu cầu của kernel. Không gian địa chỉ ảo của tiến trình là góc nhìn lô-gic (logic / 논리); việc trang nào đang thực sự nằm trong RAM vật lý là trạng thái động.

> **Nối mạch:** Trong **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Những hiểu lầm phổ biến (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"RAM `free` thấp nghĩa là sắp hết RAM."** bộ nhớ đệm (cache / 캐시) có thể được thu hồi; cần nhìn `available` và các bằng chứng về áp lực bộ nhớ.

**"VSZ là lượng RAM tiến trình đang chiếm."** Ánh xạ ảo khác với lượng trang hiện diện trong RAM vật lý.

**"`Xmx` bằng tổng bộ nhớ Java sử dụng."** JVM còn nhiều thành phần bản địa (native / 네이티브) và ngoài vùng nhớ động (heap / 힙).

**"Có dữ liệu trong swap nghĩa là máy chủ (server / 서버) đang swap liên tục."** Lượng swap đang chứa dữ liệu khác với hoạt động swap vào/ra đang diễn ra.

**"Tiến trình biến mất chắc chắn do ứng dụng crash."** Kernel hoặc cgroup OOM có thể đã kết thúc nó.

**"Xóa bộ nhớ đệm (cache / 캐시) giúp máy chủ (server / 서버) nhanh hơn."** Thường ngược lại vì làm mất dữ liệu bộ nhớ đệm (cache / 캐시) hữu ích; chỉ thực hiện khi có lý do cụ thể.

> **Nối mạch:** Ở chặng này của **Bộ nhớ, bộ nhớ ảo, page bộ nhớ đệm (cache / 캐시) và OOM**, **Kết nối kiến thức** nối từ **Những hiểu lầm phổ biến (Common Misconceptions)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết nối kiến thức

Bộ nhớ nối với hệ thống tệp thông qua page cache, với CPU thông qua page fault và TLB, và với container thông qua giới hạn cgroup. [CPU, lập lịch và hiệu năng](./cpu_scheduling_performance.md) tiếp tục cách đọc các chỉ số tài nguyên như một hệ thống thống nhất thay vì những con số rời rạc.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
