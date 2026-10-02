# Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Bắt đầu từ tải công việc (workload / 워크로드), không bắt đầu từ hardware** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Thông lượng (throughput / 처리량) và độ trễ (latency / 지연 시간)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối capacity planning với workload, server sizing và headroom, để quy mô được chọn theo SLO và mô hình tăng trưởng.

Một máy chủ (server / 서버) có thể “chạy được” nhưng vẫn được sizing sai. Nếu sizing quá nhỏ, độ trễ (latency / 지연 시간) và lỗi (error / 오류) tỷ lệ (rate / 비율) tăng khi traffic burst. Nếu sizing quá lớn, chi phí cao và bottleneck thật có thể nằm ở cơ sở dữ liệu (database / 데이터베이스) hoặc phụ thuộc (dependency / 의존성) khác.

**sức chứa (capacity / 용량) planning** là quá trình ước lượng và kiểm chứng lượng tài nguyên cần thiết để tải công việc (workload / 워크로드) đạt mục tiêu về thông lượng (throughput / 처리량), độ trễ (latency / 지연 시간), độ tin cậy (reliability / 신뢰성) và chi phí (cost / 비용).

Đây không phải bài toán chọn “CPU bao nhiêu cốt lõi (core / 핵심), RAM bao nhiêu GB” một lần rồi kết thúc. sức chứa (capacity / 용량) là quan hệ giữa tải công việc (workload / 워크로드) và toàn bộ chuỗi tài nguyên.

## Bắt đầu từ tải công việc (workload / 워크로드), không bắt đầu từ hardware

Nếu chỉ hỏi:

```text
server nên có bao nhiêu CPU?
```

thì chưa đủ thông tin.

Cần biết:

- yêu cầu (request / 요청) tỷ lệ (rate / 비율);
- yêu cầu (request / 요청) chi phí (cost / 비용);
- tính đồng thời (concurrency / 동시성);
- phản hồi (response / 응답) kích thước (size / 크기);
- cơ sở dữ liệu (database / 데이터베이스) calls/yêu cầu (request / 요청);
- bộ nhớ (memory / 메모리) working set;
- traffic burst mẫu (pattern / 패턴);
- độ trễ (latency / 지연 시간) SLO;
- growth tỷ lệ (rate / 비율);
- thất bại (failure / 실패)/redundancy yêu cầu (requirement / 요구사항).

Hai applications cùng 100 requests/second có thể cần tài nguyên khác nhau hàng chục lần.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Thông lượng (throughput / 처리량) và độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Bắt đầu từ tải công việc (workload / 워크로드), không bắt đầu từ hardware** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Utilization không nên luôn ở 100%** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thông lượng (throughput / 처리량) và độ trễ (latency / 지연 시간)

**thông lượng (throughput / 처리량)** là lượng công việc (work / 작업) hoàn thành trên đơn vị thời gian.

Ví dụ:

```text
1000 requests/second
```

**độ trễ (latency / 지연 시간)** là thời gian để một đơn vị (unit / 단위) công việc (work / 작업) hoàn thành.

Ví dụ:

```text
p95 = 120 ms
p99 = 350 ms
```

Sức chứa (capacity / 용량) planning môi trường vận hành (production / 운영 환경) thường phải giữ cả hai trong mục tiêu.

Tăng tính đồng thời (concurrency / 동시성) có thể tăng thông lượng (throughput / 처리량) đến một điểm, sau đó queueing làm độ trễ (latency / 지연 시간) tăng mạnh.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Utilization không nên luôn ở 100%** tiếp nhận điểm tựa từ **Thông lượng (throughput / 처리량) và độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sức chứa (capacity / 용량) khác với utilization snapshot** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Utilization không nên luôn ở 100%

Một batch job có thể tận dụng CPU gần 100% và vẫn ổn.

Một web API cần phản ứng với burst thường cần **headroom**.

Nếu normal traffic đã dùng 95% CPU, một burst nhỏ hoặc GC spike có thể đẩy hệ thống (system / 시스템) vào saturation.

Headroom là phần sức chứa (capacity / 용량) chưa dùng trong trạng thái bình thường để hấp thụ biến động và thất bại (failure / 실패).

Không có một tỷ lệ headroom universal cho mọi hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Sức chứa (capacity / 용량) khác với utilization snapshot** tiếp nhận điểm tựa từ **Utilization không nên luôn ở 100%** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Little's Law** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức chứa (capacity / 용량) khác với utilization snapshot

Một máy chủ (server / 서버) CPU 30% lúc 03:00 không chứng minh máy chủ (server / 서버) dư 70% sức chứa (capacity / 용량).

Cần nhìn:

- peak hour;
- daily/weekly mẫu (pattern / 패턴);
- p95/p99 utilization;
- burst duration;
- seasonal traffic;
- triển khai (deployment / 배포)/backup jobs;
- nút (node / 노드) thất bại (failure / 실패) scenarios.

Sức chứa (capacity / 용량) planning dựa thời gian (time / 시간) series, không dựa một snapshot.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Little's Law** tiếp nhận điểm tựa từ **Sức chứa (capacity / 용량) khác với utilization snapshot** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dịch vụ (service / 서비스) thời gian (time / 시간) và queueing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Little's Law

Trong hệ thống tương đối ổn định:

\[
L = \lambda W
\]

trong đó:

- `L`: số requests/công việc (work / 작업) items trung bình đang ở trong hệ thống (system / 시스템);
- `λ`: thông lượng (throughput / 처리량)/arrival tỷ lệ (rate / 비율);
- `W`: thời gian trung bình trong hệ thống (system / 시스템).

Ví dụ nếu dịch vụ (service / 서비스) xử lý 1000 yêu cầu (request / 요청)/s và average độ trễ (latency / 지연 시간) 100 ms:

\[
L = 1000 \times 0.1 = 100
\]

nghĩa trung bình có khoảng 100 requests đang in-flight.

Nếu độ trễ (latency / 지연 시간) tăng lên 1 giây mà thông lượng (throughput / 처리량) vẫn 1000/s, số in-flight công việc (work / 작업) tăng lên khoảng 1000.

Điều này giải thích tại sao độ trễ (latency / 지연 시간) degradation kéo theo luồng thực thi (thread / 스레드)/socket/bộ nhớ (memory / 메모리) pressure.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Dịch vụ (service / 서비스) thời gian (time / 시간) và queueing** tiếp nhận điểm tựa từ **Little's Law** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CPU sizing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dịch vụ (service / 서비스) thời gian (time / 시간) và queueing

Độ trễ (latency / 지연 시간) có thể tách gần đúng thành:

\[
W = W_q + S
\]

trong đó:

- `Wq`: thời gian chờ hàng đợi (queue / 큐);
- `S`: thời gian thực sự được phục vụ.

Khi tài nguyên (resource / 자원) utilization gần saturation, hàng đợi (queue / 큐) wait có thể tăng nhanh dù dịch vụ (service / 서비스) thời gian (time / 시간) không thay đổi nhiều.

Đó là lý do tail độ trễ (latency / 지연 시간) thường xấu đi mạnh trước khi hệ thống (system / 시스템) hoàn toàn thất bại (fail / 실패).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **CPU sizing** tiếp nhận điểm tựa từ **Dịch vụ (service / 서비스) thời gian (time / 시간) và queueing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **vCPU không phải đơn vị (unit / 단위) hiệu năng (performance / 성능) tuyệt đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CPU sizing

CPU sizing cần biết CPU thời gian (time / 시간)/yêu cầu (request / 요청).

Giả sử benchmark cho thấy mỗi yêu cầu (request / 요청) cần trung bình:

```text
2 ms CPU
```

và mục tiêu (target / 대상):

```text
2000 requests/s
```

CPU demand gần đúng:

\[
2000 \times 0.002 = 4 CPU-seconds/second
\]

nghĩa tải công việc (workload / 워크로드) cần khoảng 4 CPU cores ở 100% utilization lý tưởng.

Nhưng môi trường vận hành (production / 운영 환경) cần thêm headroom, kernel overhead, GC, uneven traffic và tail hành vi (behavior / 동작).

Có thể mục tiêu (target / 대상) 6–8 vCPU tùy benchmark/kiến trúc (architecture / 아키텍처) thay vì đúng 4.

Đây chỉ là mô hình (model / 모델) khởi đầu. CPU kiến trúc (architecture / 아키텍처) và cloud vCPU hiệu năng (performance / 성능) khác nhau.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **vCPU không phải đơn vị (unit / 단위) hiệu năng (performance / 성능) tuyệt đối** tiếp nhận điểm tựa từ **CPU sizing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CPU saturation signals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## vCPU không phải đơn vị (unit / 단위) hiệu năng (performance / 성능) tuyệt đối

Một vCPU ở cloud instance A không chắc bằng vCPU ở instance B.

Khác biệt có thể đến từ:

- CPU generation;
- clock frequency;
- SMT topology;
- noisy neighbor;
- burst credit mô hình (model / 모델);
- virtualization overhead.

Sức chứa (capacity / 용량) phải benchmark trên instance family thật nếu hiệu năng (performance / 성능) quan trọng.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **CPU saturation signals** tiếp nhận điểm tựa từ **vCPU không phải đơn vị (unit / 단위) hiệu năng (performance / 성능) tuyệt đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) sizing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CPU saturation signals

Các dấu hiệu:

```bash
mpstat -P ALL 1
vmstat 1
pidstat -u 1
```

Cần xem:

- CPU utilization;
- runnable hàng đợi (queue / 큐);
- steal thời gian (time / 시간);
- per-core imbalance;
- cgroup throttling.

CPU 80% không tự động nghĩa chỉ còn 20% sức chứa (capacity / 용량) vì tail độ trễ (latency / 지연 시간) có thể bắt đầu tăng trước 100%.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Bộ nhớ (memory / 메모리) sizing** tiếp nhận điểm tựa từ **CPU saturation signals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vùng nhớ vùng nhớ động (heap / 힙) headroom** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) sizing

RAM không nên sizing chỉ bằng vùng nhớ động (heap / 힙) kích thước (size / 크기).

Với Java dịch vụ (service / 서비스), tổng bộ nhớ (memory / 메모리) có thể gồm:

```text
Java heap
+ metaspace
+ thread stacks
+ code cache
+ direct buffers
+ native libraries
+ JVM internal structures
+ page cache
+ OS/kernel memory
```

Nếu bộ chứa (container / 컨테이너) limit 4 GiB và `-Xmx4g`, gần như không còn headroom cho bản địa (native / 네이티브) bộ nhớ (memory / 메모리).

Đây là cấu hình dễ OOMKill.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Vùng nhớ vùng nhớ động (heap / 힙) headroom** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) sizing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Page bộ nhớ đệm (cache / 캐시) là sức chứa (capacity / 용량) hữu ích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vùng nhớ vùng nhớ động (heap / 힙) headroom

Giả sử bộ chứa (container / 컨테이너) giới hạn bộ nhớ (memory limit / 메모리 제한):

```text
8 GiB
```

Không nhất thiết set:

```text
-Xmx8g
```

Có thể cần để một phần cho bản địa (native / 네이티브) bộ nhớ (memory / 메모리) và page bộ nhớ đệm (cache / 캐시). Tỷ lệ phù hợp phụ thuộc JVM/tải công việc (workload / 워크로드).

Theo dõi RSS, bản địa (native / 네이티브) bộ nhớ (memory / 메모리) tracking và cgroup bộ nhớ (memory / 메모리) thay vì chỉ vùng nhớ động (heap / 힙) metrics.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Page bộ nhớ đệm (cache / 캐시) là sức chứa (capacity / 용량) hữu ích** tiếp nhận điểm tựa từ **Vùng nhớ vùng nhớ động (heap / 힙) headroom** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Swap trong sức chứa (capacity / 용량) planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Page bộ nhớ đệm (cache / 캐시) là sức chứa (capacity / 용량) hữu ích

Linux sử dụng RAM dư cho page bộ nhớ đệm (cache / 캐시).

Một dịch vụ (service / 서비스) đọc nhiều files hoặc cơ sở dữ liệu (database / 데이터베이스) cục bộ (local / 로컬) có thể hưởng lợi từ bộ nhớ đệm (cache / 캐시).

Sizing RAM quá sát tiến trình (process / 프로세스) RSS có thể làm bộ nhớ đệm (cache / 캐시) bị reclaim liên tục, tăng disk I/O và độ trễ (latency / 지연 시간).

Vì vậy RAM headroom không nhất thiết là “lãng phí”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Swap trong sức chứa (capacity / 용량) planning** tiếp nhận điểm tựa từ **Page bộ nhớ đệm (cache / 캐시) là sức chứa (capacity / 용량) hữu ích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lưu trữ (storage / 저장소) sức chứa (capacity / 용량) có nhiều dimensions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Swap trong sức chứa (capacity / 용량) planning

Swap có thể giúp tránh immediate OOM trong một số workloads, nhưng heavy swap thường gây độ trễ (latency / 지연 시간) lớn.

Dịch vụ (service / 서비스) latency-sensitive không nên dựa swap như normal sức chứa (capacity / 용량).

Quan sát:

```bash
vmstat 1
```

Sustained swap in/out (`si/so`) là tín hiệu (signal / 신호) pressure.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Lưu trữ (storage / 저장소) sức chứa (capacity / 용량) có nhiều dimensions** tiếp nhận điểm tựa từ **Swap trong sức chứa (capacity / 용량) planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IOPS sizing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lưu trữ (storage / 저장소) sức chứa (capacity / 용량) có nhiều dimensions

Disk sizing không chỉ là GB.

Các dimensions:

- sức chứa (capacity / 용량);
- IOPS;
- thông lượng (throughput / 처리량) MB/s;
- độ trễ (latency / 지연 시간);
- hàng đợi (queue / 큐) độ sâu (depth / 깊이);
- inode count;
- durability;
- burst credits ở cloud disks.

Một 1 TB disk có thể không đủ hiệu năng (performance / 성능) nếu tải công việc (workload / 워크로드) cần nhiều random IOPS.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **IOPS sizing** tiếp nhận điểm tựa từ **Lưu trữ (storage / 저장소) sức chứa (capacity / 용량) có nhiều dimensions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sequential và random I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## IOPS sizing

Nếu một yêu cầu (request / 요청) gây trung bình 5 random lưu trữ (storage / 저장소) operations và dịch vụ (service / 서비스) cần 1000 requests/s:

```text
~5000 IOPS
```

chưa tính background writes, logs, compaction, backups.

Nếu provisioned disk chỉ 3000 IOPS, lưu trữ (storage / 저장소) có thể thành bottleneck dù còn rất nhiều free không gian (space / 공간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Sequential và random I/O** tiếp nhận điểm tựa từ **IOPS sizing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mạng (network / 네트워크) sizing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sequential và random I/O

Sequential tải công việc (workload / 워크로드) thường tối ưu thông lượng (throughput / 처리량) MB/s.

Random small-block tải công việc (workload / 워크로드) thường bị giới hạn IOPS/độ trễ (latency / 지연 시간).

Sức chứa (capacity / 용량) kiểm thử (test / 테스트) phải giống tải công việc (workload / 워크로드) mẫu (pattern / 패턴) thật.

`dd` sequential benchmark không đại diện cơ sở dữ liệu (database / 데이터베이스) random I/O đầy đủ.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Mạng (network / 네트워크) sizing** tiếp nhận điểm tựa từ **Sequential và random I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Packet tỷ lệ (rate / 비율) cũng quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạng (network / 네트워크) sizing

Mạng (network / 네트워크) sức chứa (capacity / 용량) cần xem:

- requests/s;
- yêu cầu (request / 요청) bytes;
- phản hồi (response / 응답) bytes;
- giao thức (protocol / 프로토콜) overhead;
- replication traffic;
- backup traffic;
- TLS overhead;
- peak burst.

Ví dụ phản hồi (response / 응답) trung bình 100 KB với 1000 requests/s:

```text
100 MB/s application payload
≈ 800 Mbps trước overhead
```

Một giao diện (interface / 인터페이스) 1 Gbps có thể đã gần saturation sau overhead và traffic khác.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Packet tỷ lệ (rate / 비율) cũng quan trọng** tiếp nhận điểm tựa từ **Mạng (network / 네트워크) sizing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết (connection / 연결) sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Packet tỷ lệ (rate / 비율) cũng quan trọng

Mạng (network / 네트워크) không chỉ giới hạn bandwidth Mbps/Gbps.

Rất nhiều small packets có thể giới hạn packets per second, interrupt/softirq CPU hoặc conntrack.

Một API trả 1 KB ở 100k req/s có bandwidth không quá lớn nhưng packet tỷ lệ (rate / 비율) và liên kết (connection / 연결) handling rất cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, sau nội dung của **Packet tỷ lệ (rate / 비율) cũng quan trọng**, **Liên kết (connection / 연결) sức chứa (capacity / 용량)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Tệp (file / 파일) descriptor sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) sức chứa (capacity / 용량)

Mỗi TCP liên kết (connection / 연결) dùng:

- kernel socket structures;
- send/receive buffers;
- tệp (file / 파일) descriptors;
- ứng dụng (application / 애플리케이션) trạng thái (state / 상태).

Một máy chủ (server / 서버) có 100k idle connections có tài nguyên (resource / 자원) profile khác 100 active requests.

Cần xem:

```bash
ss -s
cat /proc/sys/fs/file-nr
```

và tiến trình (process / 프로세스) limits.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Tệp (file / 파일) descriptor sức chứa (capacity / 용량)** tiếp nhận điểm tựa từ **Liên kết (connection / 연결) sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Luồng thực thi (thread / 스레드) sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tệp (file / 파일) descriptor sức chứa (capacity / 용량)

Nếu dịch vụ (service / 서비스) cần nhiều sockets/files đồng thời, `nofile` limit phải đủ.

```bash
cat /proc/<PID>/limits
```

Nhưng tăng FD limit không giải quyết leak. Nếu descriptors tăng vô hạn, nguyên nhân gốc (root cause / 근본 원인) là vòng đời (lifecycle / 생명주기) bug.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Luồng thực thi (thread / 스레드) sức chứa (capacity / 용량)** tiếp nhận điểm tựa từ **Tệp (file / 파일) descriptor sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng thực thi (thread / 스레드) sức chứa (capacity / 용량)

Luồng thực thi (thread / 스레드) count ảnh hưởng:

- bộ nhớ (memory / 메모리) ngăn xếp (stack / 스택);
- scheduling;
- ngữ cảnh (context / 맥락) switches;
- tranh chấp khóa (lock contention / 잠금 경합).

Một máy chủ (server / 서버) “còn RAM” không nghĩa có thể tăng luồng thực thi (thread / 스레드) pool vô hạn.

Luồng thực thi (thread / 스레드) pool sizing phải dựa CPU/wait ratio và downstream sức chứa (capacity / 용량).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Luồng thực thi (thread / 스레드) sức chứa (capacity / 용량)** nêu điều cần giải thích; **Cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phụ thuộc (dependency / 의존성) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool

Backend sức chứa (capacity / 용량) thường bị giới hạn bởi DB connections trước CPU.

Giả sử 10 ứng dụng (application / 애플리케이션) instances, mỗi instance pool 100:

```text
10 × 100 = 1000 DB connections
```

Nếu cơ sở dữ liệu (database / 데이터베이스) chỉ chịu tốt 300 active connections, quy mô (scale / 규모) app horizontal có thể làm DB tệ hơn.

Sức chứa (capacity / 용량) planning phải end-to-end.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool** nêu điều cần giải thích; **Phụ thuộc (dependency / 의존성) ngân sách (budget / 예산)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Horizontal scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성) ngân sách (budget / 예산)

Mỗi phụ thuộc (dependency / 의존성) có sức chứa (capacity / 용량) riêng:

```text
API instance
 → database
 → Redis
 → downstream API
 → message broker
```

Quy mô (scale / 규모) tầng (layer / 계층) A không tự quy mô (scale / 규모) B.

Đây là lý do kiểm thử tải (load test / 부하 테스트) phải quan sát toàn đồ thị (graph / 그래프) chứ không chỉ dịch vụ (service / 서비스) đang kiểm thử (test / 테스트).

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Horizontal scaling** tiếp nhận điểm tựa từ **Phụ thuộc (dependency / 의존성) ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vertical scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Horizontal scaling

Thêm instances tăng tổng sức chứa (capacity / 용량) khi tải công việc (workload / 워크로드) có thể phân phối.

Ví dụ:

```text
1 instance = 500 req/s
4 instances ≠ chắc chắn 2000 req/s
```

Có thể bị giới hạn bởi:

- DB;
- dùng chung (shared / 공유) bộ nhớ đệm (cache / 캐시);
- mạng (network / 네트워크);
- bộ cân bằng tải (load balancer / 로드 밸런서);
- khóa (lock / 잠금)/toàn cục (global / 전역) trạng thái (state / 상태).

Scale-out efficiency cần đo.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Vertical scaling** tiếp nhận điểm tựa từ **Horizontal scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **N+1 sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vertical scaling

Thêm CPU/RAM cho một máy chủ (server / 서버) đơn giản hơn về kiến trúc (architecture / 아키텍처), nhưng có giới hạn hardware và tăng blast radius khi nút (node / 노드) thất bại (fail / 실패).

Một JVM vùng nhớ động (heap / 힙) quá lớn cũng làm GC hành vi (behavior / 동작) khác.

Vertical và horizontal scaling là sự đánh đổi (trade-off / 트레이드오프), không phải “cloud luôn quy mô (scale / 규모) horizontal”.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **N+1 sức chứa (capacity / 용량)** tiếp nhận điểm tựa từ **Vertical scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Availability Zone thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## N+1 sức chứa (capacity / 용량)

Nếu cluster có 4 nodes và cần chịu mất 1 nút (node / 노드) mà không vi phạm SLO, normal traffic không nên cần 100% tổng sức chứa (capacity / 용량) 4 nodes.

N+1 planning:

```text
capacity của 3 nodes >= peak required capacity
```

Điều này tạo redundancy headroom.

Nếu normal tải (load / 로드) mỗi nút (node / 노드) đã 90%, mất một nút (node / 노드) sẽ làm ba nút (node / 노드) còn lại quá tải.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **N+1 sức chứa (capacity / 용량)** cho ta quy tắc; **Availability Zone thất bại (failure / 실패)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Autoscaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Availability Zone thất bại (failure / 실패)

Multi-AZ kiến trúc (architecture / 아키텍처) cần cân sức chứa (capacity / 용량) theo miền lỗi (failure domain / 장애 도메인).

Nếu có 3 AZ và yêu cầu (requirement / 요구사항) chịu mất 1 AZ, hai AZ còn lại phải đủ sức chứa (capacity / 용량).

Không chỉ có instance count; cơ sở dữ liệu (database / 데이터베이스)/mạng (network / 네트워크) phụ thuộc (dependency / 의존성) cũng cần redundancy tương ứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Availability Zone thất bại (failure / 실패)** cho ta quy tắc; **Autoscaling** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Quy mô (scale / 규모) chỉ số (metric / 지표)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Autoscaling

Autoscaling thêm/bớt instances dựa metrics.

Nhưng scaling có delay:

```text
metric detects load
 → policy triggers
 → VM/container starts
 → application warms up
 → health check passes
 → receives traffic
```

Nếu traffic spike nhanh hơn startup thời gian (time / 시간), autoscaling phản ứng quá chậm.

Cần baseline sức chứa (capacity / 용량)/headroom trước khi autoscaling cứu được hệ thống.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Quy mô (scale / 규모) chỉ số (metric / 지표)** tiếp nhận điểm tựa từ **Autoscaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tải (load / 로드) testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy mô (scale / 규모) chỉ số (metric / 지표)

CPU là chỉ số (metric / 지표) phổ biến nhưng không luôn đúng.

Một dịch vụ (service / 서비스) I/O-bound có CPU 20% nhưng luồng thực thi (thread / 스레드) pool/DB connections exhausted.

Alternative metrics:

- yêu cầu (request / 요청) hàng đợi (queue / 큐) length;
- tính đồng thời (concurrency / 동시성);
- độ trễ (latency / 지연 시간);
- custom công việc (work / 작업) backlog;
- messages in hàng đợi (queue / 큐).

Scaling chỉ số (metric / 지표) nên phản ánh bottleneck/tài nguyên (resource / 자원) demand thật.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Tải (load / 로드) testing** tiếp nhận điểm tựa từ **Quy mô (scale / 규모) chỉ số (metric / 지표)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Warm-up** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tải (load / 로드) testing

Sức chứa (capacity / 용량) plan chỉ là hypothesis cho tới khi được kiểm thử (test / 테스트).

Kiểm thử tải (load test / 부하 테스트) nên mô phỏng:

- realistic yêu cầu (request / 요청) mix;
- realistic dữ liệu (data / 데이터) sizes;
- authentication;
- think thời gian (time / 시간) nếu có;
- phụ thuộc (dependency / 의존성) hành vi (behavior / 동작);
- warm-up;
- bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태);
- ramp-up và burst.

Một benchmark endpoint `/health` không đại diện nghiệp vụ (business / 비즈니스) API.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Warm-up** tiếp nhận điểm tựa từ **Tải (load / 로드) testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Coordinated omission** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Warm-up

JVM cần thời gian JIT compile, bộ nhớ đệm (cache / 캐시) warm-up, liên kết (connection / 연결) pools và filesystem bộ nhớ đệm (cache / 캐시).

Kiểm thử tải (load test / 부하 테스트) ngay từ cold start có thể đo startup hành vi (behavior / 동작) thay vì steady-state sức chứa (capacity / 용량).

Nhưng môi trường vận hành (production / 운영 환경) có rolling deploy/cold start, nên cả hai scenarios đều cần kiểm thử (test / 테스트) tùy yêu cầu (requirement / 요구사항).

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Coordinated omission** tiếp nhận điểm tựa từ **Warm-up** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Percentile thay vì average** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coordinated omission

Load-testing tools có thể báo độ trễ (latency / 지연 시간) quá đẹp nếu khi máy chủ (server / 서버) chậm, công cụ (tool / 도구) cũng giảm yêu cầu (request / 요청) generation và bỏ qua requests lẽ ra đã đến.

Hiện tượng này gọi là **coordinated omission**.

Một kiểm thử (test / 테스트) tốt phải hiểu traffic mô hình (model / 모델) và đo lường (measurement / 측정) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Percentile thay vì average** tiếp nhận điểm tựa từ **Coordinated omission** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SLO và lỗi (error / 오류) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Percentile thay vì average

Average độ trễ (latency / 지연 시간) che tail.

Ví dụ:

```text
99 requests = 10 ms
1 request   = 5 s
```

Average vẫn có thể trông không quá lớn, nhưng người dùng (user / 사용자) bị yêu cầu (request / 요청) 5 giây rất rõ.

Theo dõi p95/p99/p99.9 khi SLO cần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **SLO và lỗi (error / 오류) ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **Percentile thay vì average** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Growth planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SLO và lỗi (error / 오류) ngân sách (budget / 예산)

Sức chứa (capacity / 용량) không chỉ để “không crash”, mà để đạt dịch vụ (service / 서비스) mức (level / 수준) mục tiêu (objective / 목표).

Ví dụ:

```text
99.9% requests < 500 ms
availability 99.95%
```

Máy chủ (server / 서버) có thể vẫn trả phản hồi (response / 응답) nhưng p99 3s — theo SLO vẫn là sức chứa (capacity / 용량) bài toán (problem / 문제).

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Growth planning** tiếp nhận điểm tựa từ **SLO và lỗi (error / 오류) ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sức chứa (capacity / 용량) trend** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Growth planning

Nếu traffic tăng 10% mỗi tháng, máy chủ (server / 서버) đủ hôm nay có thể thiếu sau vài tháng.

Projection đơn giản:

\[
C_{future} = C_{now}(1+g)^n
\]

với `g` là growth tỷ lệ (rate / 비율) theo kỳ.

Đây chỉ là mô hình (model / 모델) nếu growth tương đối ổn định. sản phẩm (product / 제품) launch/sự kiện (event / 이벤트) có thể tạo step thay đổi (change / 변경).

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Sức chứa (capacity / 용량) trend** tiếp nhận điểm tựa từ **Growth planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Saturation chỉ số (metric / 지표)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức chứa (capacity / 용량) trend

Theo dõi:

```text
peak CPU
peak memory
request rate
p99 latency
DB connections
IOPS
network bandwidth
error rate
```

theo tuần/tháng giúp phát hiện approaching limit trước sự cố (incident / 인시던트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Saturation chỉ số (metric / 지표)** tiếp nhận điểm tựa từ **Sức chứa (capacity / 용량) trend** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RED phương thức (method / 메서드) ở dịch vụ (service / 서비스) tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Saturation chỉ số (metric / 지표)

USE phương thức (method / 메서드) thường gợi ý xem mỗi tài nguyên (resource / 자원) theo:

- Utilization;
- Saturation;
- Errors.

Ví dụ CPU:

```text
utilization → % busy
saturation  → run queue
errors      → hiếm theo nghĩa hardware/system
```

Disk:

```text
utilization → busy time
saturation  → queue/await
errors      → I/O errors
```

Mô hình tư duy (mental model / 사고 모델) này tốt hơn chỉ một chỉ số (metric / 지표) utilization.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **RED phương thức (method / 메서드) ở dịch vụ (service / 서비스) tầng (layer / 계층)** tiếp nhận điểm tựa từ **Saturation chỉ số (metric / 지표)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sức chứa (capacity / 용량) worksheet thực tế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RED phương thức (method / 메서드) ở dịch vụ (service / 서비스) tầng (layer / 계층)

Với request-driven dịch vụ (service / 서비스), RED thường nhìn:

- tỷ lệ (rate / 비율);
- Errors;
- Duration.

Kết hợp RED ở dịch vụ (service / 서비스) tầng (layer / 계층) với USE ở tài nguyên (resource / 자원) tầng (layer / 계층) giúp nối symptom nghiệp vụ (business / 비즈니스) với bottleneck Linux.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Sức chứa (capacity / 용량) worksheet thực tế** tiếp nhận điểm tựa từ **RED phương thức (method / 메서드) ở dịch vụ (service / 서비스) tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trường hợp (case / 사례): Java API CPU 70%, p99 tăng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức chứa (capacity / 용량) worksheet thực tế

Một worksheet có thể gồm:

```text
Peak request rate:
Average / p95 request CPU time:
Average response bytes:
Peak concurrency:
DB queries/request:
DB connection pool:
Heap steady-state:
RSS peak:
Disk IOPS peak:
Network peak:
Required failure tolerance:
Growth 6 months:
Target headroom:
```

Sau đó kiểm chứng bằng kiểm thử tải (load test / 부하 테스트) và môi trường vận hành (production / 운영 환경) metrics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Sức chứa (capacity / 용량) worksheet thực tế** cho ta quy tắc; **Trường hợp (case / 사례): Java API CPU 70%, p99 tăng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례): RAM luôn 90%** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): Java API CPU 70%, p99 tăng

Không nên kết luận ngay cần thêm CPU.

Kiểm tra:

```bash
vmstat 1
mpstat -P ALL 1
pidstat -t -p <PID> 1
```

Nếu runnable hàng đợi (queue / 큐) cao và CPUs đều busy, CPU contention mạnh.

Nếu CPU 70% nhưng luồng thực thi (thread / 스레드) dump cho thấy nhiều threads chờ DB, bottleneck có thể là liên kết (connection / 연결) pool/cơ sở dữ liệu (database / 데이터베이스).

Sức chứa (capacity / 용량) planning cần đúng tài nguyên (resource / 자원).

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Trường hợp (case / 사례): Java API CPU 70%, p99 tăng** cho ta quy tắc; **Trường hợp (case / 사례): RAM luôn 90%** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례): quy mô (scale / 규모) từ 2 lên 8 app instances nhưng thông lượng (throughput / 처리량) không tăng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): RAM luôn 90%

Nếu 90% bao gồm page bộ nhớ đệm (cache / 캐시) và `MemAvailable` còn tốt, chưa chắc bộ nhớ (memory / 메모리) pressure.

Nếu cgroup bộ nhớ (memory / 메모리) gần limit, swap/reclaim mạnh hoặc OOM events xuất hiện, sức chứa (capacity / 용량) mới thực sự nguy hiểm.

Không dùng “RAM used %” đơn lẻ.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Trường hợp (case / 사례): RAM luôn 90%** cho ta quy tắc; **Trường hợp (case / 사례): quy mô (scale / 규모) từ 2 lên 8 app instances nhưng thông lượng (throughput / 처리량) không tăng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cost-performance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): quy mô (scale / 규모) từ 2 lên 8 app instances nhưng thông lượng (throughput / 처리량) không tăng

Potential dùng chung (shared / 공유) bottleneck:

- cơ sở dữ liệu (database / 데이터베이스) CPU/locks;
- DB max connections;
- Redis single-thread hotspot;
- downstream API tỷ lệ (rate / 비율) limit;
- bộ cân bằng tải (load balancer / 로드 밸런서) limit;
- lưu trữ (storage / 저장소) IOPS.

Quy mô (scale / 규모) ứng dụng (application / 애플리케이션) chỉ tăng tải (load / 로드) xuống bottleneck chung.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Trường hợp (case / 사례): quy mô (scale / 규모) từ 2 lên 8 app instances nhưng thông lượng (throughput / 처리량) không tăng** cho ta quy tắc; **Cost-performance** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cost-performance

Sức chứa (capacity / 용량) tốt không đồng nghĩa tài nguyên (resource / 자원) tối đa.

Mục tiêu có thể là:

```text
cost per 1000 requests
```

hoặc:

```text
throughput per vCPU
```

Profiling/tuning ứng dụng (application / 애플리케이션) có thể rẻ hơn tăng instance count.

Nhưng tối ưu hóa (optimization / 최적화) kỹ thuật (engineering / 엔지니어링) cũng có chi phí (cost / 비용). Cần balance.

> **Chuyển mạch:** Trong **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Cost-performance** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Sức chứa (capacity / 용량) planning là bài toán dòng chảy:

```text
workload arrival
      ↓
queues
      ↓
CPU / memory / I/O / network
      ↓
dependencies
      ↓
completed work
```

Mỗi tài nguyên (resource / 자원) có sức chứa (capacity / 용량) và saturation điểm (point / 지점).

Khi một tài nguyên (resource / 자원) đạt giới hạn, hàng đợi (queue / 큐)/độ trễ (latency / 지연 시간)/lỗi (error / 오류) thường tăng trước khi toàn hệ thống “down”.

> **Chuyển mạch:** Ở chặng này của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Xem thêm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“CPU trung bình 50% nghĩa máy chủ (server / 서버) dư một nửa.”** Peak, tail độ trễ (latency / 지연 시간) và single-core bottleneck có thể khác.

**“RAM dùng cao là thiếu RAM.”** Page bộ nhớ đệm (cache / 캐시) và reclaimable bộ nhớ (memory / 메모리) phải được tính.

**“quy mô (scale / 규모) app instances luôn tăng thông lượng (throughput / 처리량) tuyến tính.”** dùng chung (shared / 공유) dependencies có thể trở thành bottleneck.

**“Autoscaling loại bỏ nhu cầu sức chứa (capacity / 용량) planning.”** Scaling có delay và vẫn phụ thuộc upstream limits.

**“Disk đủ GB nghĩa lưu trữ (storage / 저장소) đủ sức chứa (capacity / 용량).”** IOPS, thông lượng (throughput / 처리량) và độ trễ (latency / 지연 시간) cũng là sức chứa (capacity / 용량) dimensions.

**“kiểm thử tải (load test / 부하 테스트) một endpoint là đủ.”** yêu cầu (request / 요청) mix và phụ thuộc (dependency / 의존성) hành vi (behavior / 동작) phải đại diện môi trường vận hành (production / 운영 환경).

**“máy chủ (server / 서버) không crash nghĩa sizing đúng.”** SLO về độ trễ (latency / 지연 시간)/lỗi (error / 오류) có thể đã bị vi phạm từ lâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sức chứa (capacity / 용량) Planning, máy chủ (server / 서버) Sizing và Headroom trong môi trường vận hành (production / 운영 환경)**, **Xem thêm** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Xem thêm

Các liên kết này là bước bàn giao sang cơ chế liên quan. Hãy mở chúng theo câu hỏi còn bỏ ngỏ, không coi danh sách link là phần kết luận tự thân.

- [Kernel scheduler deep dive](../06_resources/kernel_scheduler_deep_dive.md)
- [Memory và virtual memory](../06_resources/memory_virtual_memory.md)
- [I/O performance](../06_resources/io_performance.md)
- [Reverse proxy và load balancing](../07_networking/reverse_proxy_load_balancing.md)
- [Java backend incident playbook](./java_backend_incident_playbook.md)
- [Production troubleshooting](./production_troubleshooting.md)

> **Bàn giao:** Sau **Xem thêm**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
