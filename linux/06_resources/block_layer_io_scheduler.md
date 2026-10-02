# Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ tệp (file / 파일) I/O tới khối (block / 블록) I/O** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Tại sao cần khối (block / 블록) tầng (layer / 계층)?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối block layer với I/O scheduler và queue depth, để phân biệt độ trễ thiết bị với độ trễ do hàng đợi kernel.

Khi một ứng dụng ghi dữ liệu xuống tệp, dữ liệu không đi thẳng từ `write()` tới SSD theo một đường duy nhất. Nó đi qua nhiều lớp: page bộ nhớ đệm (cache / 캐시), filesystem, khối (block / 블록) tầng (layer / 계층), hàng đợi yêu cầu, driver, controller và thiết bị lưu trữ. Vì vậy khi lưu trữ (storage / 저장소) chậm, việc chỉ nhìn `iostat` hoặc `df` là chưa đủ; cần hiểu mỗi lớp đang làm gì.

## Từ tệp (file / 파일) I/O tới khối (block / 블록) I/O

Một đường ghi điển hình:

```text
application
   ↓
write()/pwrite()/fsync()
   ↓
page cache / filesystem
   ↓
block layer
   ↓
request queue
   ↓
device driver
   ↓
controller / storage
```

Filesystem làm việc với tệp (file / 파일), inode và khối (block / 블록) lô-gic (logic / 논리). khối (block / 블록) tầng (layer / 계층) cung cấp lớp trừu tượng (abstraction / 추상화) chung cho các thiết bị lưu trữ khối như HDD, SSD, NVMe hoặc virtual disk.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Tại sao cần khối (block / 블록) tầng (layer / 계층)?** tiếp nhận điểm tựa từ **Từ tệp (file / 파일) I/O tới khối (block / 블록) I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bio và yêu cầu (request / 요청)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao cần khối (block / 블록) tầng (layer / 계층)?

Nếu mỗi filesystem phải tự biết cách nói chuyện với mọi loại lưu trữ (storage / 저장소) controller, hệ thống sẽ rất khó duy trì. khối (block / 블록) tầng (layer / 계층) tách hai phía:

- phía trên: filesystem hoặc thành phần phát sinh khối (block / 블록) I/O;
- phía dưới: driver và thiết bị cụ thể.

Nó còn quản lý hàng đợi, hợp nhất yêu cầu và một số chính sách lập lịch.

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Bio và yêu cầu (request / 요청)** tiếp nhận điểm tựa từ **Tại sao cần khối (block / 블록) tầng (layer / 계층)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàng đợi và độ trễ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bio và yêu cầu (request / 요청)

Trong kernel, I/O có thể được biểu diễn bằng các cấu trúc mô tả vùng khối (block / 블록) cần đọc/ghi. Nhiều thao tác có thể được hợp nhất hoặc xếp thành yêu cầu (request / 요청) trước khi gửi xuống thiết bị.

Mô hình tư duy (mental model / 사고 모델):

```text
nhiều thao tác nhỏ
      ↓
block requests
      ↓
queue / merge / dispatch
      ↓
device
```

Điều này giải thích vì sao số lời gọi hệ thống (system call / 시스템 호출) `write()` không bằng số thao tác (operation / 연산) vật lý mà thiết bị thấy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Hàng đợi và độ trễ** tiếp nhận điểm tựa từ **Bio và yêu cầu (request / 요청)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HDD và SSD khác nhau ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi và độ trễ

Mỗi thiết bị chỉ có khả năng xử lý hữu hạn. Khi tốc độ yêu cầu tới vượt tốc độ phục vụ trong thời gian đủ dài, hàng đợi tăng.

Theo trực giác hàng đợi:

```text
arrival rate tăng
    ↓
queue depth tăng
    ↓
waiting time tăng
    ↓
tail latency tăng
```

Đây là lý do lưu trữ (storage / 저장소) có thể chưa đạt 100% thông lượng (throughput / 처리량) lý thuyết nhưng độ trễ (latency / 지연 시간) đã xấu do queueing.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **HDD và SSD khác nhau ở đâu?** tiếp nhận điểm tựa từ **Hàng đợi và độ trễ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-queue khối (block / 블록) tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HDD và SSD khác nhau ở đâu?

HDD có đầu đọc cơ học, nên thứ tự yêu cầu (request / 요청) ảnh hưởng nhiều tới seek thời gian (time / 시간). SSD không có seek cơ học như HDD, nhưng vẫn có controller, flash translation tầng (layer / 계층), garbage collection và giới hạn song song.

Do đó một I/O scheduler được thiết kế tốt cho HDD chưa chắc tối ưu cho NVMe hiện đại.

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Multi-queue khối (block / 블록) tầng (layer / 계층)** tiếp nhận điểm tựa từ **HDD và SSD khác nhau ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **I/O scheduler** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-queue khối (block / 블록) tầng (layer / 계층)

Linux hiện đại dùng **blk-mq (multi-queue block layer)** để khai thác lưu trữ (storage / 저장소) có khả năng song song cao.

Thay vì một hàng đợi (queue / 큐) chung duy nhất, hệ thống có thể có nhiều software hàng đợi (queue / 큐) gắn với CPU và hardware hàng đợi (queue / 큐) phía thiết bị.

```text
CPU0 -> software queue 0 ┐
CPU1 -> software queue 1 ├-> hardware queues -> device
CPU2 -> software queue 2 ┤
CPU3 -> software queue 3 ┘
```

Mục tiêu là giảm contention và tăng khả năng song song trên SSD/NVMe.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **I/O scheduler** tiếp nhận điểm tựa từ **Multi-queue khối (block / 블록) tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **none** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## I/O scheduler

Có thể kiểm tra scheduler:

```bash
cat /sys/block/<device>/queue/scheduler
```

Ví dụ:

```text
[mq-deadline] kyber none
```

Tên và scheduler có sẵn phụ thuộc kernel, phân phối (distribution / 분포) và thiết bị.

Các scheduler thường cố cân bằng một số mục tiêu như:

- thông lượng (throughput / 처리량);
- fairness;
- độ trễ (latency / 지연 시간);
- starvation avoidance;
- tối ưu mẫu (pattern / 패턴) yêu cầu (request / 요청).

Không nên đổi scheduler chỉ vì benchmark của tải công việc (workload / 워크로드) khác.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **none** tiếp nhận điểm tựa từ **I/O scheduler** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **mq-deadline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `none`

Với một số NVMe hiện đại, `none` để khối (block / 블록) tầng (layer / 계층) can thiệp tối thiểu và dựa nhiều vào khả năng queueing của thiết bị. Điều này không có nghĩa “không có hàng đợi (queue / 큐)”; thiết bị vẫn có hardware queues.

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **mq-deadline** tiếp nhận điểm tựa từ **none** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kyber** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `mq-deadline`

`mq-deadline` cố hạn chế starvation bằng deadline và vẫn sắp xếp yêu cầu (request / 요청) ở mức phù hợp. Nó có thể hữu ích khi cần độ trễ (latency / 지연 시간) tương đối ổn định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **kyber** tiếp nhận điểm tựa từ **mq-deadline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàng đợi (queue / 큐) độ sâu (depth / 깊이)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `kyber`

Kyber tập trung kiểm soát độ trễ (latency / 지연 시간) bằng cách điều tiết số yêu cầu (request / 요청) đang đi qua một số lớp hàng đợi (queue / 큐). Tính phù hợp phụ thuộc tải công việc (workload / 워크로드) và kernel.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Hàng đợi (queue / 큐) độ sâu (depth / 깊이)** tiếp nhận điểm tựa từ **kyber** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đọc iostat đúng hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) độ sâu (depth / 깊이)

Hàng đợi (queue / 큐) độ sâu (depth / 깊이) cho biết bao nhiêu thao tác (operation / 연산) có thể đang chờ hoặc xử lý đồng thời. NVMe thường hỗ trợ hàng đợi (queue / 큐) độ sâu (depth / 깊이) lớn, nhưng “càng lớn càng tốt” là hiểu lầm.

Hàng đợi (queue / 큐) sâu có thể tăng thông lượng (throughput / 처리량) tới một mức, nhưng cũng tăng thời gian chờ của từng yêu cầu (request / 요청).

Nếu tải công việc (workload / 워크로드) nhạy độ trễ (latency / 지연 시간), hàng đợi (queue / 큐) quá sâu có thể làm p99 xấu.

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Đọc iostat đúng hơn** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) độ sâu (depth / 깊이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **await và dịch vụ (service / 서비스) thời gian (time / 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đọc `iostat` đúng hơn

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
iostat -x 1
```

Các trường cụ thể thay đổi theo phiên bản, nhưng thường cần quan tâm:

- `r/s`, `w/s`: số yêu cầu (request / 요청) đọc/ghi mỗi giây;
- thông lượng (throughput / 처리량) đọc/ghi;
- `await`: thời gian trung bình yêu cầu (request / 요청) chờ + xử lý;
- hàng đợi (queue / 큐) kích thước (size / 크기) trung bình;
- `%util`: mức bận của thiết bị theo ngữ nghĩa (semantics / 의미론) của công cụ.

Không nên diễn giải `%util=100` trên NVMe giống hệt HDD. Thiết bị đa hàng đợi (queue / 큐) có thể xử lý song song nhiều thao tác (operation / 연산).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **await và dịch vụ (service / 서비스) thời gian (time / 시간)** tiếp nhận điểm tựa từ **Đọc iostat đúng hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **I/O kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `await` và dịch vụ (service / 서비스) thời gian (time / 시간)

Một yêu cầu (request / 요청) thấy tổng độ trễ (latency / 지연 시간) gồm thời gian đợi trong hàng đợi (queue / 큐) và thời gian thiết bị thực sự xử lý.

```text
request latency
   = queue wait
   + service time
```

Nếu `await` tăng khi thông lượng (throughput / 처리량) chưa tăng nhiều, có thể hàng đợi (queue / 큐) hoặc lưu trữ (storage / 저장소) backend đang có vấn đề.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **I/O kích thước (size / 크기)** tiếp nhận điểm tựa từ **await và dịch vụ (service / 서비스) thời gian (time / 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Random và sequential I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## I/O kích thước (size / 크기)

Hai tải công việc (workload / 워크로드) đều 1000 IOPS nhưng hoàn toàn khác nếu một bên dùng 4 KiB và bên kia 1 MiB.

Thông lượng (throughput / 처리량) gần đúng:

```text
throughput ≈ IOPS × average I/O size
```

Ví dụ:

```text
10,000 IOPS × 4 KiB ≈ 39 MiB/s
```

Trong khi:

```text
1,000 IOPS × 1 MiB ≈ 1 GiB/s
```

Vì vậy không thể đánh giá lưu trữ (storage / 저장소) chỉ bằng IOPS.

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Random và sequential I/O** tiếp nhận điểm tựa từ **I/O kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Read-ahead** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Random và sequential I/O

Sequential I/O thường dễ tối ưu hơn vì có tính liên tục. Random I/O tạo mẫu (pattern / 패턴) truy cập phân tán.

Với HDD, khác biệt này rất lớn do seek. Với SSD vẫn có khác biệt vì nội bộ (internal / 내부) parallelism, ghi (write / 쓰기) amplification và bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작).

Cơ sở dữ liệu (database / 데이터베이스) thường tạo tải công việc (workload / 워크로드) có nhiều random truy cập (access / 접근) hơn log append tuần tự.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Read-ahead** tiếp nhận điểm tựa từ **Random và sequential I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Writeback và dirty throttling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Read-ahead

Kernel có thể đọc trước dữ liệu dự đoán ứng dụng sắp cần.

```bash
blockdev --getra /dev/<device>
```

Read-ahead tốt cho truy cập tuần tự nhưng có thể lãng phí I/O và bộ nhớ đệm (cache / 캐시) nếu tải công việc (workload / 워크로드) ngẫu nhiên.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Writeback và dirty throttling** tiếp nhận điểm tựa từ **Read-ahead** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **fsync() và độ trễ (latency / 지연 시간) spike** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Writeback và dirty throttling

Ứng dụng có thể ghi nhanh vào page bộ nhớ đệm (cache / 캐시) trong một thời gian. Nếu lượng trang bẩn (dirty pages) tăng quá nhiều, kernel phải tăng tốc writeback hoặc throttle tiến trình tạo dirty dữ liệu (data / 데이터).

Do đó một ứng dụng có thể đột nhiên thấy `write()` chậm dù trước đó rất nhanh. Lý do không nhất thiết thiết bị vừa hỏng; có thể ứng dụng đã chạm ngưỡng dirty throttling.

Quan sát:

```bash
grep -E 'Dirty|Writeback' /proc/meminfo
```

Các tham số liên quan:

```bash
sysctl vm.dirty_background_ratio
sysctl vm.dirty_ratio
```

Trên một số hệ thống có thể dùng các biến dạng byte thay vì ratio.

Không nên chỉnh các tham số này nếu chưa hiểu tải công việc (workload / 워크로드).

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **fsync() và độ trễ (latency / 지연 시간) spike** tiếp nhận điểm tựa từ **Writeback và dirty throttling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **I/O scheduler không thay thế ứng dụng (application / 애플리케이션) thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `fsync()` và độ trễ (latency / 지연 시간) spike

Một hệ thống ghi log có thể thấy thông lượng (throughput / 처리량) cao vì ghi (write / 쓰기) đi vào page bộ nhớ đệm (cache / 캐시), nhưng khi cơ sở dữ liệu (database / 데이터베이스) hoặc ứng dụng (application / 애플리케이션) gọi `fsync()`, nó phải chờ durability đặc tả hợp đồng (contract / 계약) mạnh hơn.

Nếu lưu trữ (storage / 저장소) backend có tail độ trễ (latency / 지연 시간) cao, `fsync` độ trễ (latency / 지연 시간) có thể trực tiếp xuất hiện thành giao dịch (transaction / 트랜잭션) độ trễ (latency / 지연 시간).

Đây là lý do cơ sở dữ liệu (database / 데이터베이스) benchmark cần quan tâm durability chế độ (mode / 모드), không chỉ số giao dịch (transaction / 트랜잭션) mỗi giây.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **I/O scheduler không thay thế ứng dụng (application / 애플리케이션) thiết kế (design / 설계)** tiếp nhận điểm tựa từ **fsync() và độ trễ (latency / 지연 시간) spike** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Direct I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## I/O scheduler không thay thế ứng dụng (application / 애플리케이션) thiết kế (design / 설계)

Nếu ứng dụng (application / 애플리케이션) phát hàng nghìn synchronous small writes, scheduler không thể biến tải công việc (workload / 워크로드) đó thành một tải công việc (workload / 워크로드) lý tưởng hoàn toàn. Batch, buffering và write-ahead log ở tầng ứng dụng có thể có ảnh hưởng lớn hơn.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Direct I/O** tiếp nhận điểm tựa từ **I/O scheduler không thay thế ứng dụng (application / 애플리케이션) thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Async I/O và iouring** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Direct I/O

Một số cơ sở dữ liệu (database / 데이터베이스) dùng **direct I/O** để giảm hoặc tránh page bộ nhớ đệm (cache / 캐시) của kernel cho dữ liệu chính, vì cơ sở dữ liệu (database / 데이터베이스) tự quản lý bộ nhớ đệm (cache / 캐시) riêng.

Điều này tránh double caching nhưng làm ứng dụng (application / 애플리케이션) chịu trách nhiệm nhiều hơn về I/O mẫu (pattern / 패턴) và alignment.

Không nên suy ra rằng direct I/O luôn nhanh hơn buffered I/O.

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Async I/O và iouring** tiếp nhận điểm tựa từ **Direct I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NVMe** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Async I/O và io_uring

Synchronous I/O khiến luồng thực thi (thread / 스레드) có thể chờ thao tác (operation / 연산) hoàn thành. Linux cung cấp nhiều mô hình bất đồng bộ. `io_uring` là một giao diện (interface / 인터페이스) hiện đại giúp submit/completion I/O với overhead thấp hơn trong nhiều use trường hợp (case / 사례).

Mô hình tư duy (mental model / 사고 모델):

```text
submit nhiều operation
       ↓
kernel/device xử lý song song
       ↓
completion events
       ↓
application nhận kết quả
```

Điều này đặc biệt hữu ích khi tải công việc (workload / 워크로드) cần tính đồng thời (concurrency / 동시성) cao mà không muốn một luồng thực thi (thread / 스레드) blocking cho mỗi thao tác (operation / 연산).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **NVMe** tiếp nhận điểm tựa từ **Async I/O và iouring** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Virtual disk và cloud lưu trữ (storage / 저장소)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NVMe

NVMe được thiết kế cho lưu trữ (storage / 저장소) flash tốc độ cao với nhiều hàng đợi (queue / 큐) và hàng đợi (queue / 큐) độ sâu (depth / 깊이) lớn. Nó giảm nhiều giới hạn từ giao thức lưu trữ (storage / 저장소) cũ hơn.

Kiểm tra thiết bị:

```bash
lsblk -o NAME,TYPE,SIZE,ROTA,MODEL
```

`ROTA=0` thường gợi ý thiết bị không quay cơ học.

Nếu có công cụ NVMe:

```bash
nvme list
```

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Virtual disk và cloud lưu trữ (storage / 저장소)** tiếp nhận điểm tựa từ **NVMe** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cgroup I/O điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Virtual disk và cloud lưu trữ (storage / 저장소)

Trong VM/cloud, `/dev/vda` hay `/dev/nvme...` không cho bạn toàn bộ sự thật về phần cứng cuối cùng. Phía dưới có thể là network-attached lưu trữ (storage / 저장소), phân tán (distributed / 분산) khối (block / 블록) lưu trữ (storage / 저장소) hoặc lớp giới hạn IOPS của cloud provider.

Do đó guest OS có thể thấy queueing mà nguyên nhân thật nằm ngoài VM.

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Cgroup I/O điều khiển (control / 제어)** tiếp nhận điểm tựa từ **Virtual disk và cloud lưu trữ (storage / 저장소)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi iowait cao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cgroup I/O điều khiển (control / 제어)

Cgroup v2 có thể giới hạn hoặc ưu tiên I/O cho tải công việc (workload / 워크로드).

Các tệp (file / 파일) có thể gồm:

```text
io.stat
io.max
io.weight
```

Nếu bộ chứa (container / 컨테이너) chậm lưu trữ (storage / 저장소) dù host còn khả năng, cần kiểm tra chính sách (policy / 정책) cgroup.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Khi iowait cao** tiếp nhận điểm tựa từ **Cgroup I/O điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy trình điều tra lưu trữ (storage / 저장소) độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi `iowait` cao

`iowait` không phải phần trăm thời gian “ổ đĩa bận”. Nó là cách accounting CPU idle trong một số tình huống có outstanding I/O.

Một hệ thống có lưu trữ (storage / 저장소) bottleneck vẫn có thể có iowait không quá cao nếu CPU bận làm việc khác. Ngược lại iowait cao không tự động chỉ ra thiết bị nào có vấn đề.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Khi iowait cao** xác định đầu vào; **Quy trình điều tra lưu trữ (storage / 저장소) độ trễ (latency / 지연 시간)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy trình điều tra lưu trữ (storage / 저장소) độ trễ (latency / 지연 시간)

Một trình tự hữu ích:

```text
1. xác nhận symptom ở ứng dụng
2. kiểm tra latency/throughput I/O ở host
3. xác định device/mount thực tế
4. kiểm tra queue và error kernel
5. đối chiếu workload khác trên cùng device
6. kiểm tra cgroup/VM/cloud limit
7. kiểm tra filesystem và durability pattern
```

Câu lệnh thường dùng:

```bash
iostat -x 1
pidstat -d 1
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
findmnt
journalctl -k | grep -i -E 'error|timeout|reset|nvme|blk'
```

> **Chuyển mạch:** Ở chặng này của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Mô hình tư duy** gom các mảnh từ **Quy trình điều tra lưu trữ (storage / 저장소) độ trễ (latency / 지연 시간)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Lưu trữ (storage / 저장소) hiệu năng (performance / 성능) là bài toán chuỗi xử lý (pipeline / 파이프라인) và hàng đợi (queue / 큐):

```text
application rate
    ↓
page cache / filesystem
    ↓
block queue
    ↓
device queue
    ↓
storage service rate
```

Bottleneck xuất hiện khi tốc độ đưa việc vào vượt khả năng phục vụ hoặc khi tail độ trễ (latency / 지연 시간) phía dưới tăng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“SSD không cần I/O scheduler.”** khối (block / 블록) tầng (layer / 계층) và queueing vẫn tồn tại; scheduler phù hợp tùy thiết bị và tải công việc (workload / 워크로드).

**“hàng đợi (queue / 큐) độ sâu (depth / 깊이) lớn luôn tốt.”** Nó có thể tăng thông lượng (throughput / 처리량) nhưng cũng tăng độ trễ (latency / 지연 시간).

**“`%util=100` luôn nghĩa ổ đĩa đã hết khả năng.”** Cách diễn giải phụ thuộc thiết bị, đặc biệt với multi-queue NVMe.

**“`write()` nhanh nghĩa dữ liệu đã xuống disk.”** Buffered I/O có thể chỉ mới vào page bộ nhớ đệm (cache / 캐시).

**“iowait cao chính là phần trăm disk utilization.”** Hai chỉ số (metric / 지표) mô tả khái niệm khác nhau.

> **Chuyển mạch:** Trong **Khối (block / 블록) tầng (layer / 계층), hàng đợi I/O và bộ lập lịch lưu trữ**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Đọc cùng [VFS, page cache và writeback](../01_filesystem/vfs_page_cache_writeback.md), [I/O performance](./io_performance.md) và [journaling/consistency](../01_filesystem/journaling_consistency_mounts.md). Với database, các cơ chế này quyết định trực tiếp latency của WAL, checkpoint và transaction commit.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
