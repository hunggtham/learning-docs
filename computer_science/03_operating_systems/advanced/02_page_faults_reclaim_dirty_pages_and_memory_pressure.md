# Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Free bộ nhớ (memory / 메모리) và available bộ nhớ (memory / 메모리) khác nhau** đưa mô hình vào một trường hợp đủ cụ thể để quan sát; sau đó sang **2. Page fault là điều khiển (control / 제어) transfer, không đồng nghĩa lỗi nghiêm trọng** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Virtual bộ nhớ (memory / 메모리) tạo cảm giác mỗi tiến trình (process / 프로세스) có một address không gian (space / 공간) lớn và liên tục, nhưng vật lý (physical / 물리적) bộ nhớ (memory / 메모리) hữu hạn. Câu hỏi advanced không phải “còn bao nhiêu MB free?” mà là: **working set nào cần ở RAM, page nào reclaim được, reclaim chi phí (cost / 비용) bao nhiêu, và pressure ở tầng kernel biến thành độ trễ (latency / 지연 시간)/OOM ở ứng dụng (application / 애플리케이션) như thế nào?**

Bất biến (invariant / 불변식) cốt lõi là kernel phải tiếp tục cung cấp lớp trừu tượng (abstraction / 추상화) virtual bộ nhớ (memory / 메모리) đúng trong khi tái sử dụng vật lý (physical / 물리적) pages: page bị reclaim chỉ khi dữ liệu (data / 데이터) có thể được bỏ hoặc có backing chiến lược (strategy / 전략) hợp lệ; dirty trạng thái (state / 상태) phải được ghi (write / 쓰기) back đúng; ánh xạ (mapping / 매핑)/permission phải nhất quán với page-table trạng thái (state / 상태).

## 1. Free bộ nhớ (memory / 메모리) và available bộ nhớ (memory / 메모리) khác nhau

Free pages dùng được ngay, nhưng clean page bộ nhớ đệm (cache / 캐시) cũng có thể reclaim tương đối rẻ vì dữ liệu (data / 데이터) vẫn tồn tại trên lưu trữ (storage / 저장소). Vì vậy RAM `used` cao không tự động nghĩa bộ nhớ (memory / 메모리) pressure.

Ngược lại, hệ thống còn một ít free RAM nhưng anonymous working set lớn, dirty pages cao và allocation tăng nhanh có thể đang rất gần pressure.

Mô hình tư duy (mental model / 사고 모델) tốt hơn là:

```text
memory pressure
≈ demand cho physical pages
  so với
  lượng page reclaimable và cost để reclaim chúng
```

> **Chuyển mạch:** Trong **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **1. Free bộ nhớ (memory / 메모리) và available bộ nhớ (memory / 메모리) khác nhau** cho ta quy tắc; **2. Page fault là điều khiển (control / 제어) transfer, không đồng nghĩa lỗi nghiêm trọng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **3. Demand paging đổi startup chi phí (cost / 비용) thành first-touch chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Page fault là điều khiển (control / 제어) transfer, không đồng nghĩa lỗi nghiêm trọng

**Page fault (페이지 폴트)** xảy ra khi CPU không thể hoàn tất bộ nhớ (memory / 메모리) truy cập (access / 접근) bằng page-table trạng thái (state / 상태) hiện tại và chuyển quyền xử lý cho kernel.

**Minor fault** có thể xử lý không cần lưu trữ (storage / 저장소) I/O, ví dụ anonymous page mới, sao chép khi ghi (copy-on-write / 쓰기 시 복사) hoặc page đã nằm trong page bộ nhớ đệm (cache / 캐시) nhưng chưa map vào tiến trình (process / 프로세스). **Major fault** cần I/O để đưa dữ liệu (data / 데이터) vào RAM và thường đắt hơn nhiều.

Page-fault count không đủ. Cần biết loại fault, working-set ngữ cảnh (context / 맥락) và độ trễ (latency / 지연 시간) hậu quả.

> **Chuyển mạch:** Ở chặng này của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **3. Demand paging đổi startup chi phí (cost / 비용) thành first-touch chi phí (cost / 비용)** tiếp nhận điểm tựa từ **2. Page fault là điều khiển (control / 제어) transfer, không đồng nghĩa lỗi nghiêm trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Working set mới quyết định hệ thống (system / 시스템) có khỏe hay không** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Demand paging đổi startup chi phí (cost / 비용) thành first-touch chi phí (cost / 비용)

OS không cần materialize toàn bộ virtual address không gian (space / 공간) khi tiến trình (process / 프로세스) start. vật lý (physical / 물리적) page có thể chỉ được cấp/map khi address thật sự được truy cập.

Demand paging giảm startup bộ nhớ (memory / 메모리) footprint nhưng đưa chi phí (cost / 비용) vào first touch. Đây là cùng mô hình tư duy (mental model / 사고 모델) lazy công việc (work / 작업) ở nhiều tầng: chi phí (cost / 비용) không biến mất, nó được dời thời điểm.

Nếu latency-sensitive đường dẫn (path / 경로) first-touch một vùng bộ nhớ (memory / 메모리) lớn, page faults có thể xuất hiện đúng lúc yêu cầu (request / 요청) đang chạy dù startup đồ thị (graph / 그래프) nhìn rất nhanh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **4. Working set mới quyết định hệ thống (system / 시스템) có khỏe hay không** tiếp nhận điểm tựa từ **3. Demand paging đổi startup chi phí (cost / 비용) thành first-touch chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. File-backed và anonymous bộ nhớ (memory / 메모리) có reclaim chi phí (cost / 비용) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Working set mới quyết định hệ thống (system / 시스템) có khỏe hay không

**Working set** là tập pages tải công việc (workload / 워크로드) đang truy cập trong cửa sổ (window / 윈도우) hiện tại. Virtual bộ nhớ (memory / 메모리) hoạt động tốt khi active working sets phù hợp với vật lý (physical / 물리적) bộ nhớ (memory / 메모리) và locality đủ ổn định.

Nếu working set vượt sức chứa (capacity / 용량), kernel evict page rồi tải công việc (workload / 워크로드) lại fault page đó trở vào. Khi hệ thống dành phần lớn thời gian cho paging/reclaim thay vì useful công việc (work / 작업), ta có **thrashing**.

Thrashing là dạng thất bại (failure mode / 실패 모드) của một bộ nhớ đệm (cache / 캐시) có sức chứa (capacity / 용량) nhỏ hơn active demand, không phải chỉ là “swap chậm”.

> **Chuyển mạch:** Trong **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **5. File-backed và anonymous bộ nhớ (memory / 메모리) có reclaim chi phí (cost / 비용) khác nhau** tiếp nhận điểm tựa từ **4. Working set mới quyết định hệ thống (system / 시스템) có khỏe hay không** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. sao chép khi ghi (copy-on-write / 쓰기 시 복사): tối ưu hóa (optimization / 최적화) có dạng thất bại (failure mode / 실패 모드) khi ghi (write / 쓰기) mẫu (pattern / 패턴) thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. File-backed và anonymous bộ nhớ (memory / 메모리) có reclaim chi phí (cost / 비용) khác nhau

Clean file-backed page có thể drop và đọc lại từ tệp (file / 파일). Dirty file-backed page phải ghi (write / 쓰기) back trước khi reclaim nếu thay đổi cần được giữ. Anonymous pages như vùng nhớ động (heap / 힙)/ngăn xếp (stack / 스택) không có tệp (file / 파일) origin trực tiếp; để reclaim mà giữ dữ liệu (data / 데이터), hệ thống cần swap hoặc cơ chế (mechanism / 메커니즘) backing tương đương.

Vì vậy cùng 1 GB bộ nhớ (memory / 메모리) nhưng vật lý (physical / 물리적) pressure khác nhau rất nhiều tùy loại page và dirty trạng thái (state / 상태).

Điều này cũng giải thích vì sao JVM vùng nhớ động (heap / 힙), bản địa (native / 네이티브)/direct buffer và mmap/page bộ nhớ đệm (cache / 캐시) không thể gom thành một con số “tiến trình (process / 프로세스) dùng RAM” đơn giản.

> **Chuyển mạch:** Ở chặng này của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **6. sao chép khi ghi (copy-on-write / 쓰기 시 복사): tối ưu hóa (optimization / 최적화) có dạng thất bại (failure mode / 실패 모드) khi ghi (write / 쓰기) mẫu (pattern / 패턴) thay đổi** tiếp nhận điểm tựa từ **5. File-backed và anonymous bộ nhớ (memory / 메모리) có reclaim chi phí (cost / 비용) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Reclaim là eviction bài toán (problem / 문제) của OS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. sao chép khi ghi (copy-on-write / 쓰기 시 복사): tối ưu hóa (optimization / 최적화) có dạng thất bại (failure mode / 실패 모드) khi ghi (write / 쓰기) mẫu (pattern / 패턴) thay đổi

Sau `fork`, parent/child có thể cùng map pages read-only. Khi một bên ghi (write / 쓰기), page fault tạo private bản sao (copy / 복사). **sao chép khi ghi (copy-on-write / 쓰기 시 복사) (COW)** làm `fork` rẻ nếu child sớm `exec`, nhưng tải công việc (workload / 워크로드) ghi nhiều sau fork có thể tạo bộ nhớ (memory / 메모리) spike.

Tối ưu hóa (optimization / 최적화) dựa trên giả định (assumption / 가정) “chia sẻ chủ yếu read”. Khi pressure/tải công việc (workload / 워크로드) đổi, hành vi (behavior / 동작) cũng đổi. Đây là mẫu (pattern / 패턴) lặp lại xuyên Khoa học máy tính (computer science / 컴퓨터 과학): tối ưu hóa (optimization / 최적화) trì hoãn tài nguyên (resource / 자원) chi phí (cost / 비용) dựa trên expected truy cập (access / 접근) mẫu (pattern / 패턴).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **7. Reclaim là eviction bài toán (problem / 문제) của OS** tiếp nhận điểm tựa từ **6. sao chép khi ghi (copy-on-write / 쓰기 시 복사): tối ưu hóa (optimization / 최적화) có dạng thất bại (failure mode / 실패 모드) khi ghi (write / 쓰기) mẫu (pattern / 패턴) thay đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Background reclaim và direct reclaim khác impact** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Reclaim là eviction bài toán (problem / 문제) của OS

Khi available bộ nhớ (memory / 메모리) giảm, kernel chọn candidate pages để reclaim. OS không biết tương lai nên phải dùng truy cập (access / 접근)/tham chiếu (reference / 참조) thông tin (information / 정보) và replacement heuristics.

Bài toán cùng family với bộ nhớ đệm (cache / 캐시) replacement:

```text
page nào có reuse probability thấp?
miss/reload cost của nó là bao nhiêu?
page có dirty không?
reclaim nó có tạo I/O không?
```

Khác biệt là miss chi phí (cost / 비용) có thể từ microseconds tới milliseconds và có thể nằm trực tiếp trên yêu cầu (request / 요청) đường găng (critical path / 임계 경로).

> **Chuyển mạch:** Trong **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **8. Background reclaim và direct reclaim khác impact** tiếp nhận điểm tựa từ **7. Reclaim là eviction bài toán (problem / 문제) của OS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Dirty pages biến bộ nhớ (memory / 메모리) pressure thành lưu trữ (storage / 저장소) pressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Background reclaim và direct reclaim khác impact

Kernel thường cố reclaim trước khi free bộ nhớ (memory / 메모리) bằng 0, dựa trên watermarks/pressure thresholds. Background reclaim làm việc ngoài allocation đường dẫn (path / 경로). Khi không đủ, allocating luồng thực thi (thread / 스레드) có thể bị kéo vào **direct reclaim**.

Direct reclaim rất quan trọng cho môi trường vận hành (production / 운영 환경) độ trễ (latency / 지연 시간): ứng dụng (application / 애플리케이션) luồng thực thi (thread / 스레드) tưởng đang allocate bộ nhớ (memory / 메모리) nhưng thực tế phải scan/reclaim/writeback trước khi allocation tiến tiếp.

Do đó tail độ trễ (latency / 지연 시간) có thể tăng trước OOM rất lâu.

> **Chuyển mạch:** Ở chặng này của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **9. Dirty pages biến bộ nhớ (memory / 메모리) pressure thành lưu trữ (storage / 저장소) pressure** tiếp nhận điểm tựa từ **8. Background reclaim và direct reclaim khác impact** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. fsync thay đổi đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Dirty pages biến bộ nhớ (memory / 메모리) pressure thành lưu trữ (storage / 저장소) pressure

Buffered tệp (file / 파일) ghi (write / 쓰기) thường cập nhật page bộ nhớ đệm (cache / 캐시) rồi return trước khi bytes bền trên lưu trữ (storage / 저장소). Dirty pages tích tụ nếu producer ghi nhanh hơn writeback thông lượng (throughput / 처리량).

Khi dirty threshold/pressure tăng, kernel có thể throttle writer hoặc foreground allocation bị ảnh hưởng bởi writeback.

Chuỗi nhân quả (causal chain / 인과 사슬):

```text
write burst
→ dirty page growth
→ background writeback / throttling
→ storage queue depth tăng
→ allocation/write latency tăng
→ application tail latency tăng
```

Đây là liên kết (connection / 연결) trực tiếp giữa bộ nhớ (memory / 메모리) subsystem và durability/lưu trữ (storage / 저장소) hành vi (behavior / 동작).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **10. fsync thay đổi đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **9. Dirty pages biến bộ nhớ (memory / 메모리) pressure thành lưu trữ (storage / 저장소) pressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Swap: flexibility tốt, thrashing mới là thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. `fsync` thay đổi đặc tả hợp đồng (contract / 계약)

Buffered ghi (write / 쓰기) chỉ nói kernel đã nhận dữ liệu (data / 데이터); `fsync`/equivalent yêu cầu persistence mạnh hơn theo filesystem/thiết bị (device / 장치) đặc tả hợp đồng (contract / 계약). Khi cơ sở dữ liệu (database / 데이터베이스) WAL gọi durability thành phần nguyên thủy (primitive / 기본 요소), dirty/writeback trạng thái (state / 상태) và lưu trữ (storage / 저장소) hàng đợi (queue / 큐) có thể quyết định lần ghi nhận (commit / 커밋) độ trễ (latency / 지연 시간).

Bộ nhớ (memory / 메모리) pressure và durability vì vậy không độc lập. Xem [đường durability xuyên tầng](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Chuyển mạch:** Trong **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **11. Swap: flexibility tốt, thrashing mới là thất bại (failure / 실패)** tiếp nhận điểm tựa từ **10. fsync thay đổi đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Huge pages: giảm translation chi phí (cost / 비용), tăng allocation/fragmentation pressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Swap: flexibility tốt, thrashing mới là thất bại (failure / 실패)

Swap có thể giúp giữ infrequently used anonymous pages ngoài RAM để active working set dùng bộ nhớ (memory / 메모리) tốt hơn. Vấn đề xảy ra khi tải công việc (workload / 워크로드) liên tục cần lại pages vừa swap out.

Nếu lưu trữ (storage / 저장소)/page-fault vòng lặp (loop / 루프) chiếm phần lớn thời gian, CPU có thể không full nhưng hệ thống (system / 시스템) gần như không tiến triển. Chỉ nhìn CPU utilization dễ bỏ sót thất bại (failure / 실패) này.

> **Chuyển mạch:** Ở chặng này của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **12. Huge pages: giảm translation chi phí (cost / 비용), tăng allocation/fragmentation pressure** tiếp nhận điểm tựa từ **11. Swap: flexibility tốt, thrashing mới là thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. cgroup tạo bộ nhớ (memory / 메모리) ranh giới (boundary / 경계) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Huge pages: giảm translation chi phí (cost / 비용), tăng allocation/fragmentation pressure

Huge pages giảm số page-table entries và TLB pressure cho large-memory tải công việc (workload / 워크로드). Đổi lại allocation/compaction khó hơn, nội bộ (internal / 내부) fragmentation có thể tăng và chính sách (policy / 정책) như transparent huge pages có thể tạo độ trễ (latency / 지연 시간) spikes tùy tải công việc (workload / 워크로드)/kernel.

Không có bất biến (invariant / 불변식) “page lớn luôn nhanh hơn”. Cần đo TLB benefit so với compaction/allocation chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **12. Huge pages: giảm translation chi phí (cost / 비용), tăng allocation/fragmentation pressure** đã nêu tiêu chí phân biệt, còn **13. cgroup tạo bộ nhớ (memory / 메모리) ranh giới (boundary / 경계) riêng** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. OOM là thất bại (failure / 실패) cuối, không phải tín hiệu đầu tiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. cgroup tạo bộ nhớ (memory / 메모리) ranh giới (boundary / 경계) riêng

Bộ chứa (container / 컨테이너) giới hạn bộ nhớ (memory limit / 메모리 제한) có thể gây OOM trong cgroup dù host còn RAM. Điều này làm câu hỏi “máy còn bộ nhớ (memory / 메모리) không?” sai lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층).

Ví dụ JVM vùng nhớ động (heap / 힙) 6 GB trong bộ chứa (container / 컨테이너) limit 8 GB vẫn có thể OOM vì ngoài vùng nhớ động (heap / 힙) còn direct buffers, luồng thực thi (thread / 스레드) stacks, JIT/thời gian chạy (runtime / 런타임) siêu dữ liệu (metadata / 메타데이터), bản địa (native / 네이티브) libraries và mapped/file-backed trạng thái (state / 상태).

Sức chứa (capacity / 용량) phải lập luận (reasoning / 추론) trên **total resident/tài nguyên (resource / 자원) footprint tại ranh giới (boundary / 경계) bị limit**, không chỉ managed vùng nhớ động (heap / 힙).

> **Chuyển mạch:** Trong **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **13. cgroup tạo bộ nhớ (memory / 메모리) ranh giới (boundary / 경계) riêng** đã nêu tiêu chí phân biệt, còn **14. OOM là thất bại (failure / 실패) cuối, không phải tín hiệu đầu tiên** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. OOM là thất bại (failure / 실패) cuối, không phải tín hiệu đầu tiên

Trước OOM, hệ thống (system / 시스템) thường đã có bằng chứng (evidence / 증거):

```text
reclaim scan tăng
allocation/direct-reclaim stalls
major faults tăng
swap I/O tăng
memory pressure tăng
writeback/dirty pressure tăng
latency p95/p99 xấu đi
```

Nếu alert chỉ đợi tiến trình (process / 프로세스) bị OOM-killed thì khả năng quan sát (observability / 관측 가능성) bắt thất bại (failure / 실패) quá muộn.

> **Chuyển mạch:** Ở chặng này của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **14. OOM là thất bại (failure / 실패) cuối, không phải tín hiệu đầu tiên** nêu điều cần giải thích; **15. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) nên nối symptom ứng dụng (application / 애플리케이션) với kernel bộ nhớ (memory / 메모리) trạng thái (state / 상태):

```text
Application/runtime:
- RSS/native/direct memory, heap/GC state nếu managed runtime
- allocation rate và request latency

Kernel:
- available memory thay vì chỉ free
- minor/major faults
- reclaim scan/stall, direct reclaim
- dirty/writeback pages
- swap in/out
- memory pressure/PSI-like signals khi OS hỗ trợ
- cgroup memory current/limit/events

Storage correlation:
- device latency/queue depth trong thời điểm writeback/fault storm
```

Một vùng nhớ động (heap / 힙) đồ thị (graph / 그래프) đẹp không loại trừ host/cgroup pressure; một `free` snapshot cũng không chứng minh working set khỏe.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **15. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?

Nếu symptom là major-fault độ trễ (latency / 지연 시간), tầng lưu trữ (storage / 저장소) quyết định miss chi phí (cost / 비용). Nếu symptom là COW spike, page ánh xạ (mapping / 매핑) và ghi (write / 쓰기) mẫu (pattern / 패턴) quyết định allocation. Nếu bộ chứa (container / 컨테이너) OOM trong khi host khỏe, cgroup ranh giới (boundary / 경계) quyết định thất bại (failure / 실패). Nếu dirty reclaim chậm, filesystem/khối (block / 블록) thiết bị (device / 장치) thông lượng (throughput / 처리량) quyết định pressure propagation.

Advanced debugging phải theo đặc tả hợp đồng (contract / 계약) tới đúng lower tầng (layer / 계층) thay vì gắn nhãn chung “bộ nhớ (memory / 메모리) leak”.

> **Chuyển mạch:** Trong **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **17. Mô hình tư duy** gom các mảnh từ **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Mô hình tư duy

> RAM trong OS là **working-set bộ nhớ đệm (cache / 캐시) + backing chiến lược (strategy / 전략) + allocation hệ thống (system / 시스템)**. Page fault là cơ chế (mechanism / 메커니즘) đưa ánh xạ (mapping / 매핑)/dữ liệu (data / 데이터) vào trạng thái dùng được; reclaim chọn page để tái sử dụng; dirty trạng thái (state / 상태) biến reclaim thành I/O; cgroup tạo tài nguyên (resource / 자원) ranh giới (boundary / 경계); hiệu năng (performance / 성능) pressure xuất hiện thành stall/tail độ trễ (latency / 지연 시간) trước khi OOM. Câu hỏi đúng không phải “RAM dùng bao nhiêu?” mà là **tài nguyên (resource / 자원) nào reclaim được với chi phí (cost / 비용) nào, và yêu cầu (request / 요청) đang trả chi phí (cost / 비용) đó ở đâu?**

> **Chuyển mạch:** Ở chặng này của **Page faults, reclaim, dirty pages và bộ nhớ (memory / 메모리) pressure**, **Kết nối** gom các mảnh từ **17. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc tiếp [Virtual memory, page table và TLB shootdown](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md), [Filesystem crash consistency](./04_filesystem_crash_consistency_journaling_and_cow.md), [Runtime GC](../../04_programming_languages/advanced/06_garbage_collection_generational_concurrent_compacting_and_barriers.md), [Database buffer pool](../../05_data_databases/advanced/04_buffer_pool_replacement_and_dirty_page_management.md) và [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
