# I/O hiệu năng (performance / 성능), độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량) trên Linux

> **Mạch đọc:** Đọc **I/O hiệu năng (performance / 성능), độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량) trên Linux** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **I/O là gì trong ngữ cảnh Linux?** sang **độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và IOPS**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi ứng dụng chậm, CPU và bộ nhớ (memory / 메모리) thường được kiểm tra trước, nhưng nhiều hệ thống backend thực tế bị giới hạn bởi I/O: disk, mạng (network / 네트워크) lưu trữ (storage / 저장소), cơ sở dữ liệu (database / 데이터베이스) volume hoặc filesystem writeback. “Disk còn trống” không đồng nghĩa lưu trữ (storage / 저장소) đang khỏe. sức chứa (capacity / 용량) và hiệu năng (performance / 성능) là hai câu hỏi khác nhau.

Chương này tập trung vào cách suy luận về I/O trên Linux: dữ liệu đi qua những lớp nào, độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량) khác nhau ra sao, hàng đợi (queue / 큐) hình thành thế nào và dùng `iostat`, `pidstat`, `vmstat` để đọc bằng chứng thay vì đoán.

## I/O là gì trong ngữ cảnh Linux?

I/O (Input/Output) là việc chương trình trao đổi dữ liệu với tài nguyên bên ngoài CPU cốt lõi (core / 핵심), chẳng hạn filesystem, khối (block / 블록) thiết bị (device / 장치), socket hoặc terminal.

Với lưu trữ (storage / 저장소), đường đi đơn giản hóa có thể là:

```text
application
→ system call
→ page cache / filesystem
→ block layer
→ device driver
→ disk / SSD / virtual volume
```

Trong cloud, phía dưới “disk” còn có thể là mạng (network / 네트워크) lưu trữ (storage / 저장소) hoặc hypervisor tầng (layer / 계층).

Vì có nhiều lớp đệm và hàng đợi (queue / 큐), thời gian một `write()` trả về không nhất thiết là thời gian byte đã được ghi bền vững xuống thiết bị vật lý.

## Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và IOPS

Ba khái niệm thường bị trộn lẫn.

**độ trễ (latency / 지연 시간)** là thời gian hoàn thành một thao tác (operation / 연산). Nếu một read mất 5 ms, đó là độ trễ (latency / 지연 시간) của thao tác (operation / 연산) đó.

**thông lượng (throughput / 처리량)** là lượng dữ liệu xử lý theo thời gian, ví dụ 300 MiB/s.

**IOPS** là số I/O operations mỗi giây.

Một tải công việc (workload / 워크로드) đọc tệp (file / 파일) lớn tuần tự có thể cần thông lượng (throughput / 처리량) cao nhưng không cần IOPS cực lớn. cơ sở dữ liệu (database / 데이터베이스) random truy cập (access / 접근) có thể nhạy với độ trễ (latency / 지연 시간) và IOPS hơn.

Không có một chỉ số (metric / 지표) duy nhất đại diện cho “disk nhanh”.

## Sequential và random I/O

Sequential I/O truy cập các khối (block / 블록) gần nhau theo thứ tự, thường tận dụng tốt readahead và đặc tính thiết bị. Random I/O truy cập nhiều vị trí rời rạc, có thể tạo nhiều operations nhỏ.

SSD giảm mạnh penalty random truy cập (access / 접근) so với HDD, nhưng hàng đợi (queue / 큐), controller, mạng (network / 네트워크) lưu trữ (storage / 저장소) và filesystem vẫn tạo độ trễ (latency / 지연 시간).

Khi hiệu năng (performance / 성능) kiểm thử (test / 테스트), cần biết mẫu (pattern / 패턴) thật của tải công việc (workload / 워크로드) thay vì chỉ nhìn benchmark bản sao (copy / 복사) một tệp (file / 파일) lớn.

## Page bộ nhớ đệm (cache / 캐시) làm việc ở đâu?

Linux dùng RAM làm page bộ nhớ đệm (cache / 캐시). Read có thể được phục vụ từ bộ nhớ đệm (cache / 캐시) mà không chạm thiết bị. ghi (write / 쓰기) cũng có thể đi vào page bộ nhớ đệm (cache / 캐시) trước rồi kernel ghi xuống lưu trữ (storage / 저장소) sau.

Do đó một benchmark ngắn có thể đo chủ yếu RAM/bộ nhớ đệm (cache / 캐시) thay vì thiết bị (device / 장치) hiệu năng (performance / 성능).

Kiểm tra bộ nhớ (memory / 메모리) và writeback ngữ cảnh (context / 맥락) bằng:

```bash
free -h
vmstat 1
```

Không nên “drop bộ nhớ đệm (cache / 캐시)” trên môi trường vận hành (production / 운영 환경) chỉ để benchmark nếu chưa hiểu tác động.

## `iostat`

Công cụ (tool / 도구) `iostat` thường nằm trong gói (package / 패키지) `sysstat`:

```bash
iostat -xz 1 10
```

`-x` hiển thị extended statistics, `-z` bỏ thiết bị (device / 장치) không hoạt động, còn `1 10` lấy mẫu mỗi giây trong 10 lần.

Các trường dữ liệu (field / 필드) thay đổi theo phiên bản nhưng thường có các nhóm ý nghĩa như số read/ghi (write / 쓰기) thao tác (operation / 연산), thông lượng (throughput / 처리량), average yêu cầu (request / 요청) kích thước (size / 크기), hàng đợi (queue / 큐) độ sâu (depth / 깊이), độ trễ (latency / 지연 시간) và utilization.

Điều quan trọng không phải học thuộc threshold. Một NVMe có thể xử lý tính đồng thời (concurrency / 동시성) rất khác một mạng (network / 네트워크) volume. Hãy so với baseline của chính tải công việc (workload / 워크로드).

## `await`

Trên nhiều phiên bản `iostat`, `await` biểu thị thời gian trung bình I/O yêu cầu (request / 요청) trải qua trong hệ thống khối (block / 블록) thiết bị (device / 장치), thường gồm cả hàng đợi (queue / 큐) và dịch vụ (service / 서비스) thời gian (time / 시간).

Nếu `await` tăng mạnh đồng thời ứng dụng (application / 애플리케이션) độ trễ (latency / 지연 시간) tăng, lưu trữ (storage / 저장소) trở thành hypothesis đáng kiểm tra hơn.

Tuy nhiên average có thể che tail độ trễ (latency / 지연 시간). Một vài yêu cầu (request / 요청) cực chậm có thể gây hết thời gian chờ (timeout / 타임아웃) dù trung bình nhìn vẫn ổn.

## `%util` không luôn có nghĩa “100% là hết khả năng”

Với HDD truyền thống, utilization cao thường là tín hiệu saturation hữu ích. Với hiện đại (modern / 현대적) devices có parallel queues, NVMe hoặc virtual lưu trữ (storage / 저장소), diễn giải `%util` đơn giản như “phần trăm công suất” có thể sai.

Hãy kết hợp hàng đợi (queue / 큐), độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và tải công việc (workload / 워크로드) hành vi (behavior / 동작) thay vì kết luận từ `%util` duy nhất.

## Queueing

Khi yêu cầu (request / 요청) tới nhanh hơn tốc độ dịch vụ (service / 서비스) trong đủ lâu, hàng đợi (queue / 큐) tăng. Khi hàng đợi (queue / 큐) tăng, độ trễ (latency / 지연 시간) tăng dù thiết bị vẫn xử lý cùng thông lượng (throughput / 처리량).

Đây là cùng mô hình với luồng thực thi (thread / 스레드) pool, cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool và CPU runnable hàng đợi (queue / 큐).

```text
arrival rate > service capacity
→ queue tăng
→ waiting time tăng
→ latency tăng
→ timeout/retry
→ có thể tạo thêm load
```

Thử lại (retry / 재시도) không kiểm soát có thể làm I/O bottleneck tệ hơn bằng cách tạo thêm công việc (work / 작업).

## `vmstat` và I/O

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
vmstat 1 10
```

Các trường dữ liệu (field / 필드) `bi` và `bo` phản ánh khối (block / 블록) đầu vào (input / 입력)/đầu ra (output / 출력) theo đơn vị phụ thuộc hiện thực (implementation / 구현). `wa` thường biểu diễn CPU idle thời gian (time / 시간) trong khi chờ I/O theo accounting của Linux.

`wa` cao là dấu hiệu cần điều tra I/O, nhưng `wa` thấp không chứng minh lưu trữ (storage / 저장소) luôn khỏe. ứng dụng (application / 애플리케이션) có thể blocked theo cách không hiện rõ trong chỉ số (metric / 지표) này hoặc bottleneck nằm ở remote mạng (network / 네트워크) lưu trữ (storage / 저장소)/cơ sở dữ liệu (database / 데이터베이스).

## Tìm tiến trình (process / 프로세스) tạo I/O

`pidstat` có thể xem I/O theo tiến trình (process / 프로세스):

```bash
pidstat -d 1
```

Hoặc theo PID:

```bash
pidstat -d -p 1234 1
```

Điều này trả lời câu hỏi “thiết bị (device / 장치) đang bận” từ góc tiến trình (process / 프로세스) nào đang tạo read/ghi (write / 쓰기).

`iotop` cũng hữu ích nếu có:

```bash
sudo iotop
```

Nhưng công cụ (tool / 도구) availability và permission phụ thuộc distro/kernel.

## Tệp (file / 파일) descriptor và I/O đường dẫn (path / 경로)

Nếu cần biết tiến trình (process / 프로세스) đang mở tệp (file / 파일) nào:

```bash
sudo lsof -p 1234
```

Hoặc:

```bash
ls -l /proc/1234/fd
```

Kết hợp tiến trình (process / 프로세스) I/O tỷ lệ (rate / 비율) với tệp (file / 파일) descriptors giúp nối “PID nào ghi nhiều” với “nó đang ghi vào tệp (file / 파일)/thiết bị (device / 장치) nào”.

## Sync, flush và durability

Ứng dụng (application / 애플리케이션) có thể ghi vào bộ nhớ đệm (cache / 캐시) nhưng chưa chắc dữ liệu đã durable. `fsync()` yêu cầu kernel đồng bộ dữ liệu cần thiết xuống lưu trữ (storage / 저장소) theo ngữ nghĩa (semantics / 의미론) của filesystem/thiết bị (device / 장치).

Cơ sở dữ liệu (database / 데이터베이스) engine rất quan tâm vấn đề này vì giao dịch (transaction / 트랜잭션) lần ghi nhận (commit / 커밋) cần durability. lưu trữ (storage / 저장소) có bộ nhớ đệm (cache / 캐시) hoặc virtual tầng (layer / 계층) không honoring flush đúng cách có thể phá giả định của cơ sở dữ liệu (database / 데이터베이스).

Không nên dùng `sync` như một “tối ưu hiệu năng (performance / 성능)”; nó là thao tác (operation / 연산) thúc đẩy writeback và có thể tạo I/O burst.

## Direct I/O

Một số cơ sở dữ liệu (database / 데이터베이스) hoặc tải công việc (workload / 워크로드) dùng direct I/O để giảm hoặc tránh page bộ nhớ đệm (cache / 캐시) cho dữ liệu cụ thể. Điều này không tự động nhanh hơn. Nó chuyển trách nhiệm caching/alignment sang ứng dụng (application / 애플리케이션) và phù hợp với tải công việc (workload / 워크로드) có buffer manager riêng.

Cơ sở dữ liệu (database / 데이터베이스) thường là ví dụ điển hình vì engine đã có bộ nhớ đệm (cache / 캐시) pages riêng.

## Read-ahead

Kernel có thể đọc trước khối (block / 블록) tiếp theo khi phát hiện sequential truy cập (access / 접근). Điều này cải thiện thông lượng (throughput / 처리량) cho scan tuần tự nhưng không giúp nhiều với random truy cập (access / 접근).

Đây là một lý do cùng lưu trữ (storage / 저장소) có thể cho hiệu năng (performance / 성능) rất khác giữa backup tệp (file / 파일) lớn và cơ sở dữ liệu (database / 데이터베이스) random truy vấn (query / 쿼리).

## I/O scheduler

Linux khối (block / 블록) tầng (layer / 계층) có I/O schedulers khác nhau tùy kernel/thiết bị (device / 장치). Với hiện đại (modern / 현대적) SSD/NVMe, lựa chọn mặc định của distro thường đã được tối ưu hợp lý.

Không đổi scheduler môi trường vận hành (production / 운영 환경) theo một bài blog chung chung. Trước tiên cần benchmark đúng tải công việc (workload / 워크로드), hiểu thiết bị (device / 장치) kiểu (type / 타입) và có quay lui (rollback / 롤백) plan.

## Mạng (network / 네트워크) lưu trữ (storage / 저장소)

NFS, EBS-like volumes, SAN hoặc phân tán (distributed / 분산) filesystem thêm mạng (network / 네트워크) và remote dịch vụ (service / 서비스) vào I/O đường dẫn (path / 경로).

Khi cục bộ (local / 로컬) `iostat` không giải thích đủ, cần kiểm tra mạng (network / 네트워크) độ trễ (latency / 지연 시간), provider limits, burst credits, thông lượng (throughput / 처리량) caps hoặc server-side lưu trữ (storage / 저장소) metrics.

Một đường dẫn (path / 경로) `/data` nhìn như cục bộ (local / 로컬) filesystem không có nghĩa dữ liệu nằm trên cục bộ (local / 로컬) disk.

```bash
findmnt /data
```

luôn hữu ích để biết nguồn (source / 소스)/fstype.

## Java backend và I/O

Java API có thể high độ trễ (latency / 지연 시간) với CPU thấp nếu threads đang khối (block / 블록) ở JDBC, tệp (file / 파일) I/O hoặc mạng (network / 네트워크).

Luồng thực thi (thread / 스레드) dump có thể cho thấy nhiều threads ở bản địa (native / 네이티브)/socket/tệp (file / 파일) read. Linux tools sau đó giúp phân biệt cục bộ (local / 로컬) lưu trữ (storage / 저장소), TCP phụ thuộc (dependency / 의존성) hay tài nguyên (resource / 자원) limit.

Một luồng (flow / 흐름) thực tế:

```bash
jcmd <PID> Thread.print > /tmp/thread.txt
pidstat -d -p <PID> 1
iostat -xz 1 10
ss -antp
```

Không nên nhìn từng công cụ (tool / 도구) riêng; cần nối luồng thực thi (thread / 스레드) trạng thái (state / 상태) với OS tài nguyên (resource / 자원) trạng thái (state / 상태).

## Benchmark bằng `fio`

`fio` là công cụ mạnh để benchmark lưu trữ (storage / 저장소) với mẫu (pattern / 패턴) kiểm soát. Nhưng benchmark sai có thể gây tải lớn hoặc làm đầy disk.

Không chạy destructive `fio` job trên môi trường vận hành (production / 운영 환경) volume khi chưa hiểu tệp (file / 파일)/thiết bị (device / 장치) mục tiêu (target / 대상). Benchmark nên dùng kiểm thử (test / 테스트) tệp (file / 파일)/dedicated môi trường (environment / 환경) và tải công việc (workload / 워크로드) mẫu (pattern / 패턴) gần thực tế.

## Phân biệt sức chứa (capacity / 용량) sự cố (incident / 인시던트) và hiệu năng (performance / 성능) sự cố (incident / 인시던트)

Sức chứa (capacity / 용량) sự cố (incident / 인시던트):

```bash
df -h
df -i
du -xhd1 /var
```

Hiệu năng (performance / 성능) sự cố (incident / 인시던트):

```bash
iostat -xz 1 10
pidstat -d 1
vmstat 1 10
```

Hai nhóm liên quan nhưng không giống nhau. Disk 40% dung lượng vẫn có thể độ trễ (latency / 지연 시간) rất cao.

## Mô hình tư duy (mental model / 사고 모델)

Khi nghi I/O bottleneck, hãy hỏi theo chuỗi:

```text
application đang chờ gì?
→ process nào tạo I/O?
→ file/mount/device nào?
→ queue và latency trên device ra sao?
→ device local hay remote?
→ workload là random hay sequential?
→ bottleneck là capacity, latency, IOPS hay throughput?
```

Mỗi câu hỏi thu hẹp một tầng (layer / 계층).

## Những hiểu lầm phổ biến

**“Disk chưa đầy thì disk không phải bottleneck.”** sức chứa (capacity / 용량) không phản ánh độ trễ (latency / 지연 시간)/IOPS.

**“`%util=100` luôn có nghĩa thiết bị (device / 장치) đạt 100% công suất.”** Với hiện đại (modern / 현대적) parallel devices, cách hiểu này có thể quá đơn giản.

**“CPU iowait cao nghĩa CPU bị lỗi.”** CPU đang có thời gian chờ liên quan I/O; cần tìm nguồn I/O.

**“ghi (write / 쓰기) xong là dữ liệu đã nằm bền vững trên disk.”** Buffering và bộ nhớ đệm (cache / 캐시) có nhiều lớp; durability cần ngữ nghĩa (semantics / 의미론) như `fsync`.

**“Benchmark bản sao (copy / 복사) tệp (file / 파일) là đại diện cơ sở dữ liệu (database / 데이터베이스) tải công việc (workload / 워크로드).”** truy cập (access / 접근) mẫu (pattern / 패턴) có thể hoàn toàn khác.

## Kết nối kiến thức

Chương này mở rộng [Storage và Filesystems](./storage_filesystems.md), liên kết với [Memory](./memory_virtual_memory.md) qua page cache, [CPU và Scheduling](./cpu_scheduling_performance.md) qua waiting/queueing, và [Production Troubleshooting](../09_production/production_troubleshooting.md).
