# CPU, lập lịch, tải trung bình và hiệu năng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **CPU, lập lịch, tải trung bình và hiệu năng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **CPU là tài nguyên được chia theo thời gian** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Mức sử dụng CPU** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối CPU scheduling với run queue, context switch và latency để đọc hiệu năng từ trạng thái chờ thực tế của tiến trình.

Khi xử lý sự cố CPU, rất dễ rơi vào suy luận quá nhanh: thấy `CPU 90%` rồi kết luận "CPU yếu", hoặc thấy tải trung bình (load average) bằng 20 rồi hiểu thành "CPU 2000%". Các số liệu chỉ có ý nghĩa khi đặt cùng **bộ lập lịch (scheduler)**, số CPU lô-gic (logic / 논리), lượng công việc sẵn sàng chạy, thời gian chờ I/O và mục tiêu của khối lượng công việc.

## CPU là tài nguyên được chia theo thời gian

Nhiều luồng sẵn sàng chạy cùng cạnh tranh một số lượng ngữ cảnh thực thi CPU hữu hạn. **Bộ lập lịch Linux (Linux scheduler)** quyết định luồng nào được chạy trên CPU nào và trong khoảng thời gian nào dựa trên chính sách lập lịch, mức ưu tiên và trạng thái hệ thống.

```bash
nproc
lscpu
```

`nproc` cho biết số đơn vị xử lý khả dụng trong môi trường hiện tại; `lscpu` cho topology CPU chi tiết hơn.

> **Nối mạch:** Trong **CPU, lập lịch, tải trung bình và hiệu năng**, **Mức sử dụng CPU** nối từ **CPU là tài nguyên được chia theo thời gian** sang **Tải (load / 로드) average không phải phần trăm CPU**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức sử dụng CPU

`top` hoặc `mpstat` chia thời gian CPU thành các nhóm như `user`, `system`, `idle`, `iowait` tùy công cụ và nền tảng.

```bash
top
mpstat -P ALL 1
```

`%user` cao thường gợi ý ứng dụng đang tính toán nhiều. `%system` cao cho thấy nhiều thời gian được dùng trong kernel. `iowait` cao có thể liên quan chờ I/O lưu trữ, nhưng không nên dùng một chỉ số đơn lẻ để kết luận nguyên nhân gốc.

> **Nối mạch:** Ở chặng này của **CPU, lập lịch, tải trung bình và hiệu năng**, **Tải (load / 로드) average không phải phần trăm CPU** nối từ **Mức sử dụng CPU** sang **Hàng đợi tác vụ sẵn sàng chạy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tải (load / 로드) average không phải phần trăm CPU

`uptime` hiển thị tải trung bình trong khoảng 1, 5 và 15 phút:

```bash
uptime
```

Trên Linux, tải (load / 로드) phản ánh số tác vụ đang sẵn sàng chạy và một số tác vụ ở trạng thái chờ không thể ngắt. Vì vậy tải (load / 로드) có thể cao do tranh chấp CPU hoặc do nhiều tác vụ ở trạng thái `D` liên quan I/O.

Tải (load / 로드) bằng 8 trên máy có 8 CPU lô-gic (logic / 논리) mang ý nghĩa khác với tải (load / 로드) bằng 8 trên máy chỉ có 2 CPU. Tuy nhiên tỷ lệ này vẫn chỉ là một **quy tắc kinh nghiệm (heuristic)**; độ trễ của tải công việc (workload / 워크로드) và thành phần trạng thái tác vụ vẫn cần được kiểm tra.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CPU, lập lịch, tải trung bình và hiệu năng**, **Hàng đợi tác vụ sẵn sàng chạy** nối từ **Tải (load / 로드) average không phải phần trăm CPU** sang **CPU ở mức tiến trình và mức luồng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hàng đợi tác vụ sẵn sàng chạy

Trường `r` của `vmstat` cho một góc nhìn về số tác vụ đang sẵn sàng chạy:

```bash
vmstat 1 10
```

Nếu `r` liên tục lớn hơn số CPU khả dụng và mức sử dụng CPU cũng cao, giả thuyết tranh chấp CPU trở nên mạnh hơn. Nếu tải (load / 로드) cao nhưng CPU vẫn còn nhàn rỗi đáng kể và có nhiều tác vụ `D`, nên chuyển hướng điều tra sang I/O.

> **Nối mạch:** Trong **CPU, lập lịch, tải trung bình và hiệu năng**, **CPU ở mức tiến trình và mức luồng** nối từ **Hàng đợi tác vụ sẵn sàng chạy** sang **Chuyển ngữ cảnh**, vì cơ chế trước tạo đầu vào cho bước sau.

## CPU ở mức tiến trình và mức luồng

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
ps aux --sort=-%cpu | head -20
```

cho góc nhìn theo tiến trình. Với ứng dụng Java nhiều luồng, cần quan sát từng luồng thực thi (thread / 스레드):

```bash
pidstat -t -p <PID> 1
```

Sau đó có thể lấy luồng thực thi (thread / 스레드) dump:

```bash
jcmd <PID> Thread.print > /tmp/thread.txt
```

Việc đối chiếu ID luồng của hệ điều hành với luồng thực thi (thread / 스레드) dump JVM đôi khi cần chuyển đổi giữa số thập phân và thập lục phân tùy JVM và công cụ. Điểm quan trọng là CPU cao thường thuộc về **một hoặc nhiều luồng/đường thực thi mã**, không chỉ đơn giản là tên tiến trình.

> **Nối mạch:** Ở chặng này của **CPU, lập lịch, tải trung bình và hiệu năng**, **Chuyển ngữ cảnh** nối từ **CPU ở mức tiến trình và mức luồng** sang **Khối lượng công việc thiên về CPU và thiên về I/O**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chuyển ngữ cảnh

Khi scheduler chuyển giữa các luồng, hệ thống phải lưu và phục hồi trạng thái thực thi, đồng thời có thể ảnh hưởng bộ nhớ đệm CPU và TLB. Nhiều luồng hơn không luôn nhanh hơn. Nếu số luồng sẵn sàng chạy vượt xa năng lực CPU, tranh chấp và số lần chuyển ngữ cảnh có thể tăng trong khi thông lượng không tăng tương ứng.

```bash
vmstat 1
pidstat -w 1
```

Các bộ đếm chuyển ngữ cảnh cần được so với mức bình thường của chính hệ thống; không tồn tại một ngưỡng "cao" phù hợp cho mọi tải công việc (workload / 워크로드).

> **Nối mạch:** Đặt trong câu hỏi lớn của **CPU, lập lịch, tải trung bình và hiệu năng**, **Khối lượng công việc thiên về CPU và thiên về I/O** nối từ **Chuyển ngữ cảnh** sang **Độ trễ và thông lượng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khối lượng công việc thiên về CPU và thiên về I/O

**CPU-bound tải công việc (workload / 워크로드)** dành phần lớn thời gian để tính toán; thêm CPU có thể tăng thông lượng nếu công việc có thể chạy song song. **I/O-bound tải công việc (workload / 워크로드)** thường chờ ổ đĩa, mạng hoặc cơ sở dữ liệu; thêm CPU có thể gần như không giúp gì.

Đây là một cách áp dụng tư duy gần với định luật Amdahl: tối ưu chỉ có giá trị lớn khi nhắm đúng phần đang giới hạn toàn hệ thống.

Nếu API có độ trễ cao nhưng CPU chỉ dùng 20%, nút thắt có thể nằm ở liên kết (connection / 연결) pool của cơ sở dữ liệu, khóa, API phía sau, thiết bị lưu trữ hoặc luồng thực thi (thread / 스레드) pool.

> **Nối mạch:** Trong **CPU, lập lịch, tải trung bình và hiệu năng**, **Độ trễ và thông lượng** nối từ **Khối lượng công việc thiên về CPU và thiên về I/O** sang **nice và mức ưu tiên lập lịch**, vì cơ chế trước tạo đầu vào cho bước sau.

## Độ trễ và thông lượng

**thông lượng (throughput / 처리량)** là lượng công việc hoàn thành trong một đơn vị thời gian; **độ trễ (latency / 지연 시간)** là thời gian cần để hoàn thành một đơn vị công việc. Hệ thống có thể tăng thông lượng (throughput / 처리량) bằng cách gom lô (batching) nhưng làm độ trễ (latency / 지연 시간) của từng yêu cầu tăng.

Mức sử dụng CPU gần 100% có thể hợp lý với một batch job nhưng nguy hiểm với dịch vụ tương tác cần khoảng dự phòng để giữ độ trễ ổn định. Không tồn tại một mức sử dụng CPU "tốt nhất" cho mọi loại tải công việc (workload / 워크로드).

> **Nối mạch:** Ở chặng này của **CPU, lập lịch, tải trung bình và hiệu năng**, **nice và mức ưu tiên lập lịch** nối từ **Độ trễ và thông lượng** sang **CPU affinity**, vì cơ chế trước tạo đầu vào cho bước sau.

## `nice` và mức ưu tiên lập lịch

`nice` và `renice` ảnh hưởng mức ưu tiên tương đối của các tác vụ trong lớp lập lịch thông thường:

```bash
nice -n 10 long-job
renice 10 -p <PID>
```

Giá trị nice không phải giới hạn CPU cứng. Nó ảnh hưởng trọng số hoặc mức ưu tiên tương đối. Khi cần cô lập tài nguyên rõ ràng hơn, thường phải dùng cgroup hoặc cơ chế kiểm soát CPU của systemd.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CPU, lập lịch, tải trung bình và hiệu năng**, **CPU affinity** nối từ **nice và mức ưu tiên lập lịch** sang **Phương pháp tối ưu hiệu năng**, vì cơ chế trước tạo đầu vào cho bước sau.

## CPU affinity

Tiến trình hoặc luồng có thể bị giới hạn vào một tập CPU cụ thể:

```bash
taskset -pc <PID>
```

**CPU affinity** hữu ích trong một số tình huống tối ưu chuyên biệt nhưng cũng có thể làm hiệu năng xấu đi nếu ghim CPU sai và làm giảm khả năng linh hoạt của scheduler.

> **Nối mạch:** Trong **CPU, lập lịch, tải trung bình và hiệu năng**, **Phương pháp tối ưu hiệu năng** nối từ **CPU affinity** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phương pháp tối ưu hiệu năng

Tối ưu hiệu năng tốt bắt đầu bằng mục tiêu rõ ràng: độ trễ (latency / 지연 시간) p95, thông lượng (throughput / 처리량), hay chi phí CPU trên mỗi yêu cầu? Sau đó đo đường cơ sở (baseline), xác định nút thắt, thay đổi một yếu tố rồi đo lại.

Tăng luồng thực thi (thread / 스레드) pool, tăng vùng nhớ động (heap / 힙), ghim CPU hoặc đổi tham số kernel mà không có giả thuyết thường chỉ làm nút thắt di chuyển sang nơi khác.

> **Nối mạch:** Ở chặng này của **CPU, lập lịch, tải trung bình và hiệu năng**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Phương pháp tối ưu hiệu năng** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Bộ lập lịch CPU phân phối **thời gian thực thi** giữa những thực thể sẵn sàng chạy. CPU cao chỉ nói bộ xử lý đang bận; tải (load / 로드) cho biết áp lực rộng hơn; hiệu năng ứng dụng phụ thuộc cả thời gian chạy lẫn thời gian chờ.

Hãy luôn hỏi:

```text
công việc đang chạy hay đang chờ?
đang chờ CPU, khóa, đĩa, mạng hay phụ thuộc bên ngoài?
chỉ số nào chứng minh giả thuyết đó?
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **CPU, lập lịch, tải trung bình và hiệu năng**, **Những hiểu lầm phổ biến (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến (Common Misconceptions)

**"tải (load / 로드) 10 = CPU 1000%."** tải (load / 로드) average không phải phần trăm CPU.

**"CPU 100% luôn xấu."** Batch tải công việc (workload / 워크로드) có thể tận dụng CPU tối đa; dịch vụ nhạy với độ trễ (latency / 지연 시간) cần cách đánh giá khác.

**"Nhiều luồng thực thi (thread / 스레드) luôn tăng hiệu năng."** luồng thực thi (thread / 스레드) tạo thêm tranh chấp, chuyển ngữ cảnh và có thể đụng các nút thắt khác.

**"CPU thấp nghĩa là máy chủ (server / 서버) khỏe."** Ứng dụng có thể deadlock hoặc đang chờ phụ thuộc với CPU gần 0.

**"Tăng CPU sẽ sửa được độ trễ (latency / 지연 시간)."** Chỉ đúng khi CPU thực sự là nút thắt đáng kể.

> **Nối mạch:** Trong **CPU, lập lịch, tải trung bình và hiệu năng**, **Kết nối kiến thức** nối từ **Những hiểu lầm phổ biến (Common Misconceptions)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết nối kiến thức

Hành vi CPU gắn với mô hình tiến trình/luồng, bộ nhớ qua TLB và page fault, và thời gian chờ từ lưu trữ hoặc mạng. [Xử lý sự cố production](../09_production/production_troubleshooting.md) kết hợp nhiều tín hiệu tài nguyên để tránh chẩn đoán chỉ dựa trên một chỉ số.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
