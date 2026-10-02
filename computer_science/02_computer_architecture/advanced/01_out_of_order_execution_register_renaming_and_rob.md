# Out-of-order thực thi (execution / 실행), register renaming và reorder buffer

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Program thứ tự (order / 순서), thực thi (execution / 실행) thứ tự (order / 순서) và retirement thứ tự (order / 순서) là ba thứ khác nhau** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Instruction được biến thành micro-operation như thế nào?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối out-of-order execution với register renaming, ROB và recovery, để pipeline chạy song song mà vẫn giữ semantics.

Một CPU hiện đại không đơn giản lấy một instruction, chạy xong rồi mới lấy instruction tiếp theo. Nếu instruction đang chờ bộ nhớ đệm (cache / 캐시), phép nhân hoặc branch kết quả (result / 결과) mà các instruction độc lập phía sau đã sẵn sàng, việc để chuỗi xử lý (pipeline / 파이프라인) đứng yên sẽ lãng phí thực thi (execution / 실행) units. **Thực thi ngoài thứ tự (out-of-order execution, OoO / 비순차 실행)** giải quyết vấn đề đó bằng cách cho CPU thực thi micro-operations theo phụ thuộc (dependency / 의존성) và tài nguyên (resource / 자원) readiness, trong khi vẫn giữ một bất biến (invariant / 불변식) quan trọng: trạng thái kiến trúc mà software quan sát phải tương thích với đặc tả hợp đồng (contract / 계약) của ISA.

Chương này cần được đọc như một bài toán giữ bất biến (invariant / 불변식) dưới hiệu năng (performance / 성능) pressure: **thực thi (execution / 실행) được phép reorder để che độ trễ (latency / 지연 시간); retirement, exception và quay lui (rollback / 롤백) phải khôi phục một architectural lịch sử (history / 이력) hợp lệ.**

## 1. Program thứ tự (order / 순서), thực thi (execution / 실행) thứ tự (order / 순서) và retirement thứ tự (order / 순서) là ba thứ khác nhau

Cần tách ba khái niệm:

```text
program order
= thứ tự instruction trong machine-code stream

execution order
= thứ tự µop thật sự sử dụng execution units

retirement/commit order
= thứ tự kết quả trở thành architectural state chính thức
```

CPU có thể execute instruction trẻ hơn trước instruction già hơn nếu phụ thuộc (dependency / 의존성) cho phép, nhưng thường retire theo program thứ tự (order / 순서). bất biến (invariant / 불변식) này giúp giữ **precise exception**: nếu instruction 15 page fault, OS phải thấy trạng thái (state / 상태) như thể các instruction sau 15 chưa lần ghi nhận (commit / 커밋).

> **Chuyển mạch:** Trong **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **2. Instruction được biến thành micro-operation như thế nào?** tiếp nhận điểm tựa từ **1. Program thứ tự (order / 순서), thực thi (execution / 실행) thứ tự (order / 순서) và retirement thứ tự (order / 순서) là ba thứ khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. True phụ thuộc (dependency / 의존성) mới là ràng buộc (constraint / 제약조건) dữ liệu thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Instruction được biến thành micro-operation như thế nào?

ISA instruction là đặc tả hợp đồng (contract / 계약) với software. Bên trong processor, một instruction có thể được decode thành một hoặc nhiều **micro-operation (µop)**. Front-end fetch/decode tạo stream; rename/scheduler/back-end quyết định µop nào có đủ operand và thực thi (execution / 실행) cổng (port / 포트) phù hợp để chạy.

Mô hình tư duy (mental model / 사고 모델):

```text
fetch → decode → rename → dispatch
                         ↓
                issue / scheduling window
                    ↓       ↓       ↓
                   ALU     load    vector ...
                    \       |       /
                     complete
                        ↓
                       ROB
                        ↓
                     retire
```

Đây gần như một data-flow machine speculative nằm bên trong vỏ architectural-order.

> **Chuyển mạch:** Ở chặng này của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **2. Instruction được biến thành micro-operation như thế nào?** nêu điều cần giải thích; **3. True phụ thuộc (dependency / 의존성) mới là ràng buộc (constraint / 제약조건) dữ liệu thật** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Vì sao register renaming tồn tại?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. True phụ thuộc (dependency / 의존성) mới là ràng buộc (constraint / 제약조건) dữ liệu thật

Ví dụ:

```text
1: r1 = load [A]
2: r2 = r1 + 1
3: r3 = r4 * r5
4: r6 = r3 + 2
```

Instruction 2 có **RAW phụ thuộc (dependency / 의존성) (Read After Write)** với 1 nên phải chờ. Instruction 3 độc lập với tải (load / 로드) ở 1 và có thể chạy trong lúc trượt bộ nhớ đệm (cache miss / 캐시 미스) đang được xử lý. Instruction 4 chỉ cần chờ 3.

OoO engine tìm independent công việc (work / 작업) trong một instruction cửa sổ (window / 윈도우) để overlap độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **3. True phụ thuộc (dependency / 의존성) mới là ràng buộc (constraint / 제약조건) dữ liệu thật** nêu điều cần giải thích; **4. Vì sao register renaming tồn tại?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Rename bảng (table / 테이블), vật lý (physical / 물리적) registers và thời gian tồn tại (lifetime / 수명)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Vì sao register renaming tồn tại?

Architectural register names có thể tạo phụ thuộc (dependency / 의존성) giả.

```text
1: r1 = r2 + r3
2: r4 = r1 + 1
3: r1 = r5 + r6
```

Instruction 3 ghi lại tên `r1`, nhưng không phụ thuộc giá trị (value / 값) của instruction 1. Đây là **WAW (Write After Write)** về tên. Tương tự, WAR (Write After Read) có thể xuất hiện khi instruction trẻ ghi một tên mà instruction già còn cần đọc.

**Đổi tên thanh ghi (register renaming / 레지스터 리네이밍)** ánh xạ architectural registers sang vật lý (physical / 물리적) registers lớn hơn:

```text
architectural r1 version A → physical P17
architectural r1 version B → physical P42
```

Renaming loại false phụ thuộc (dependency / 의존성), để scheduler chỉ bị giới hạn bởi true dữ liệu (data / 데이터) phụ thuộc (dependency / 의존성) và tài nguyên (resource / 자원) các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Trong **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **5. Rename bảng (table / 테이블), vật lý (physical / 물리적) registers và thời gian tồn tại (lifetime / 수명)** tiếp nhận điểm tựa từ **4. Vì sao register renaming tồn tại?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Reservation station / issue hàng đợi (queue / 큐) và wakeup-select** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Rename bảng (table / 테이블), vật lý (physical / 물리적) registers và thời gian tồn tại (lifetime / 수명)

Rename stage giữ ánh xạ (mapping / 매핑) từ architectural register tới vật lý (physical / 물리적) register chứa phiên bản (version / 버전) mới nhất. Khi instruction tạo giá trị (value / 값) mới, CPU cấp vật lý (physical / 물리적) register mới và cập nhật ánh xạ (mapping / 매핑) cho instruction sau.

Vật lý (physical / 물리적) register cũ không thể tái sử dụng ngay vì instruction speculative hoặc instruction chưa retire có thể vẫn tham chiếu nó. Free-list/thời gian tồn tại (lifetime / 수명) management vì vậy gắn trực tiếp với retirement trạng thái (state / 상태).

Đây là một bất biến (invariant / 불변식) nội bộ: **vật lý (physical / 물리적) lưu trữ (storage / 저장소) không được tái sử dụng khi vẫn còn architectural/speculative phụ thuộc (dependency / 의존성) hợp lệ tới phiên bản (version / 버전) cũ**.

> **Chuyển mạch:** Ở chặng này của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **6. Reservation station / issue hàng đợi (queue / 큐) và wakeup-select** tiếp nhận điểm tựa từ **5. Rename bảng (table / 테이블), vật lý (physical / 물리적) registers và thời gian tồn tại (lifetime / 수명)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Reorder Buffer giữ architectural bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Reservation station / issue hàng đợi (queue / 큐) và wakeup-select

Sau rename, µops đi vào scheduling structures. Entry giữ thao tác (operation / 연산), nguồn (source / 소스) tags/readiness và destination. Khi producer complete, dependent entries được wake up; scheduler chọn ready µops cho thực thi (execution / 실행) ports.

Đây không phải FIFO. Wakeup/select phải chạy cực nhanh mỗi cycle, nên scheduler width, issue-window kích thước (size / 크기) và bypass mạng (network / 네트워크) tạo sự đánh đổi (trade-off / 트레이드오프) area/power/frequency.

Cửa sổ (window / 윈도우) lớn hơn có thể tìm nhiều independent công việc (work / 작업) hơn, nhưng độ phức tạp (complexity / 복잡도) tăng nhanh. hiệu năng (performance / 성능) không tăng miễn phí chỉ bằng cách “cho nhiều instruction in-flight”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **7. Reorder Buffer giữ architectural bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **6. Reservation station / issue hàng đợi (queue / 큐) và wakeup-select** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Precise exception giải thích vì sao retirement thứ tự (order / 순서) quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Reorder Buffer giữ architectural bất biến (invariant / 불변식)

**Reorder Buffer (ROB / 재정렬 버퍼)** theo dõi instructions theo program thứ tự (order / 순서) sau khi chúng vào speculative back-end. thực thi (execution / 실행) có thể complete out of thứ tự (order / 순서), nhưng ROB cho phép retire theo thứ tự.

ROB entry cần siêu dữ liệu (metadata / 메타데이터) đủ để biết instruction complete chưa, exception có xảy ra không, branch speculation có hợp lệ không và tài nguyên (resource / 자원) nào được bản phát hành (release / 릴리스) khi retire.

Bất biến (invariant / 불변식) cốt lõi:

> Speculative thực thi (execution / 실행) được phép tạo intermediate trạng thái (state / 상태), nhưng software chỉ được quan sát architectural trạng thái (state / 상태) tương ứng với một prefix hợp lệ của instruction stream.

> **Chuyển mạch:** Trong **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **8. Precise exception giải thích vì sao retirement thứ tự (order / 순서) quan trọng** tiếp nhận điểm tựa từ **7. Reorder Buffer giữ architectural bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. bộ nhớ (memory / 메모리) thao tác (operation / 연산) khó hơn register phụ thuộc (dependency / 의존성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Precise exception giải thích vì sao retirement thứ tự (order / 순서) quan trọng

Giả sử instruction 10 page fault nhưng 11–20 đã execute. Nếu side effects của 11–20 trở thành architectural trạng thái (state / 상태) không thể quay lui (rollback / 롤백), OS không thể xử lý exception như thể fault xảy ra chính xác tại instruction 10.

ROB dừng retirement tại faulting instruction, squash công việc (work / 작업) trẻ hơn và chuyển điều khiển (control / 제어) sang handler với trạng thái (state / 상태) chính xác.

Đây là liên kết (connection / 연결) trực tiếp giữa microarchitecture và OS lớp trừu tượng (abstraction / 추상화): page fault/tín hiệu (signal / 신호)/debugger chỉ hoạt động hợp lý vì processor giữ precise-state đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Ở chặng này của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **9. bộ nhớ (memory / 메모리) thao tác (operation / 연산) khó hơn register phụ thuộc (dependency / 의존성)** tiếp nhận điểm tựa từ **8. Precise exception giải thích vì sao retirement thứ tự (order / 순서) quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Store buffer nối OoO với bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. bộ nhớ (memory / 메모리) thao tác (operation / 연산) khó hơn register phụ thuộc (dependency / 의존성)

Register phụ thuộc (dependency / 의존성) biết từ operand names sau rename. bộ nhớ (memory / 메모리) phụ thuộc (dependency / 의존성) chỉ rõ khi addresses được tính.

```text
store [p] = 10
load  [q]
```

Nếu chưa biết `p == q`, CPU phải quyết định có cho tải (load / 로드) chạy sớm không. **tải (load / 로드)/Store hàng đợi (queue / 큐) (LSQ)**, bộ nhớ (memory / 메모리) disambiguation và phụ thuộc (dependency / 의존성) prediction giúp khai thác parallelism.

Nếu prediction sai và tải (load / 로드) đã đọc giá trị (value / 값) không hợp lệ, dependent công việc (work / 작업) phải replay hoặc squash. hiệu năng (performance / 성능) pressure vì thế tạo speculation thêm một tầng ngoài branch prediction.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **10. Store buffer nối OoO với bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)** tiếp nhận điểm tựa từ **9. bộ nhớ (memory / 메모리) thao tác (operation / 연산) khó hơn register phụ thuộc (dependency / 의존성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Branch speculation và quay lui (rollback / 롤백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Store buffer nối OoO với bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)

Store có thể complete trong chuỗi xử lý (pipeline / 파이프라인) nhưng chưa globally visible. Store buffer giữ ghi (write / 쓰기) trong khi coherence/quyền sở hữu (ownership / 소유권) được xử lý. CPU có thể forward store cho tải (load / 로드) cùng cốt lõi (core / 핵심) trước khi cốt lõi (core / 핵심) khác thấy giá trị (value / 값).

Điều này nối trực tiếp tới [memory consistency và ordering](./00_memory_consistency_cache_coherence_and_ordering.md). OoO thực thi (execution / 실행) và bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) liên quan nhưng không phải cùng khái niệm: retirement thứ tự (order / 순서) giữ architectural register/exception trạng thái (state / 상태), còn cross-core bộ nhớ (memory / 메모리) visibility tuân ISA bộ nhớ (memory / 메모리) mô hình (model / 모델).

> **Chuyển mạch:** Trong **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **11. Branch speculation và quay lui (rollback / 롤백)** tiếp nhận điểm tựa từ **10. Store buffer nối OoO với bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Pointer chasing: khi OoO không tìm được việc độc lập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Branch speculation và quay lui (rollback / 롤백)

OoO gần như luôn đi cùng branch prediction. Nếu processor chờ biết chắc mọi branch mới fetch tiếp, chuỗi xử lý (pipeline / 파이프라인) sẽ thường xuyên rỗng.

Speculative đường dẫn (path / 경로) có thể decode/execute sâu phía sau unresolved branch. Khi prediction đúng, độ trễ (latency / 지연 시간) bị che. Khi sai, processor phải khôi phục rename/checkpoint trạng thái (state / 상태) và squash younger công việc (work / 작업).

Mispredict chi phí (cost / 비용) tăng khi chuỗi xử lý (pipeline / 파이프라인) sâu và lượng in-flight công việc (work / 작업) lớn. Vì vậy prediction accuracy có tác động phi tuyến tới IPC trong nhiều tải công việc (workload / 워크로드).

> **Chuyển mạch:** Ở chặng này của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **12. Pointer chasing: khi OoO không tìm được việc độc lập** tiếp nhận điểm tựa từ **11. Branch speculation và quay lui (rollback / 롤백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. hiệu năng (performance / 성능) pressure và giới hạn thực tế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Pointer chasing: khi OoO không tìm được việc độc lập

Ví dụ linked-list traversal:

```text
node = node.next
node = node.next
node = node.next
```

Address tải (load / 로드) tiếp theo chỉ biết sau khi tải (load / 로드) trước hoàn thành. Đây là phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬) dài. ROB lớn hay nhiều ALU không tạo parallelism nếu tải công việc (workload / 워크로드) không có independent công việc (work / 작업).

Ngược lại, xử lý nhiều array elements độc lập có thể tạo memory-level parallelism và vectorization tốt hơn.

Đây là liên kết (connection / 연결) quan trọng giữa cấu trúc dữ liệu (data structure / 자료구조)/bố cục (layout / 레이아웃) và microarchitecture: hai thuật toán cùng Big-O có thể khác đáng kể về bộ nhớ đệm (cache / 캐시) locality và available parallelism.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **12. Pointer chasing: khi OoO không tìm được việc độc lập** đã nêu tiêu chí phân biệt, còn **13. hiệu năng (performance / 성능) pressure và giới hạn thực tế** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. hiệu năng (performance / 성능) pressure và giới hạn thực tế

Các tài nguyên (resource / 자원) hữu hạn gồm:

```text
ROB entries
issue/scheduling queue
physical registers
load/store queue
execution ports
memory-level parallelism slots
branch checkpoints
```

Khi một tài nguyên (resource / 자원) đầy, front-end/back-end có thể stall dù tài nguyên (resource / 자원) khác còn rảnh. Vì vậy câu “CPU utilization 100%” chưa giải thích bottleneck microarchitecture.

Power/thermal limits cũng quan trọng: cửa sổ (window / 윈도우) rộng và wakeup/select lớn tiêu tốn năng lượng; mobile/máy chủ (server / 서버) cores chọn điểm cân bằng khác nhau.

> **Chuyển mạch:** Trong **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **13. hiệu năng (performance / 성능) pressure và giới hạn thực tế** đã nêu tiêu chí phân biệt, còn **14. bằng chứng vận hành (production evidence / 운영 증거)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. dạng thất bại (failure mode / 실패 모드): tính đúng đắn (correctness / 정확성) và bảo mật (security / 보안) khác hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. bằng chứng vận hành (production evidence / 운영 증거)

Khi nghi OoO/back-end bottleneck, bằng chứng (evidence / 증거) hữu ích gồm sampling profiler + hardware hiệu năng (performance / 성능) counters: retired instructions, cycles, IPC, branch miss, bộ nhớ đệm (cache / 캐시)/TLB miss, backend/frontend stalled cycles và memory-bandwidth pressure tùy CPU/công cụ (tool / 도구).

Tên counter khác theo microarchitecture; mục tiêu không phải học thuộc sự kiện (event / 이벤트) name mà là phân biệt các hypothesis:

```text
ít instruction parallelism?
branch speculation thất bại?
cache miss/pointer chasing?
execution-port pressure?
front-end không cấp đủ µop?
```

Static assembly inspection hữu ích nhưng không thay thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) vì trượt bộ nhớ đệm (cache miss / 캐시 미스) và branch hành vi (behavior / 동작) phụ thuộc tải công việc (workload / 워크로드).

> **Chuyển mạch:** Ở chặng này của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **14. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **15. dạng thất bại (failure mode / 실패 모드): tính đúng đắn (correctness / 정확성) và bảo mật (security / 보안) khác hiệu năng (performance / 성능)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. dạng thất bại (failure mode / 실패 모드): tính đúng đắn (correctness / 정확성) và bảo mật (security / 보안) khác hiệu năng (performance / 성능)

OoO engine bình thường phải giữ architectural tính đúng đắn (correctness / 정확성) qua ROB/quay lui (rollback / 롤백). Nhưng speculative microarchitectural trạng thái (state / 상태) như bộ nhớ đệm (cache / 캐시) có thể để lại side tác động (effect / 효과) dù speculative instruction không retire. Đây là nền tảng lập luận (reasoning / 추론) cho Spectre-class side channels.

Điểm quan trọng là tách hai đặc tả hợp đồng (contract / 계약):

```text
architectural correctness:
wrong-path result không được commit thành architectural state

microarchitectural confidentiality:
wrong-path execution không được làm lộ secret qua timing side channel
```

Đặc tả hợp đồng (contract / 계약) thứ nhất có thể đúng trong khi đặc tả hợp đồng (contract / 계약) thứ hai bị khai thác. Không cần tạo chapter công nghệ riêng để thấy mô hình tư duy (mental model / 사고 모델) này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **16. dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **15. dạng thất bại (failure mode / 실패 모드): tính đúng đắn (correctness / 정확성) và bảo mật (security / 보안) khác hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. dùng chung (common / 공통) Misconceptions

**“Out-of-order nghĩa CPU thay đổi lô-gic (logic / 논리) chương trình.”** Không. CPU reorder nội bộ nhưng phải giữ architectural đặc tả hợp đồng (contract / 계약).

**“Register renaming là trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화).”** trình biên dịch (compiler / 컴파일러) cũng có register allocation/renaming, nhưng hardware renaming diễn ra động để loại false phụ thuộc (dependency / 의존성) giữa in-flight instructions.

**“Instruction complete nghĩa đã lần ghi nhận (commit / 커밋).”** Không. Instruction có thể complete nhưng vẫn speculative và chưa retire.

**“ROB càng lớn thì luôn càng nhanh.”** Không. Nếu tải công việc (workload / 워크로드) là phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬) hoặc bộ nhớ (memory / 메모리) bandwidth đã saturated, cửa sổ (window / 윈도우) lớn hơn có thể không tạo speedup tương xứng.

> **Chuyển mạch:** Trong **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **17. Mô hình tư duy** gom các mảnh từ **16. dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Mô hình tư duy

> OoO CPU là speculative data-flow engine nằm sau một architectural-order đặc tả hợp đồng (contract / 계약). **Renaming loại false phụ thuộc (dependency / 의존성); scheduler tìm ready công việc (work / 작업); LSQ suy luận bộ nhớ (memory / 메모리) phụ thuộc (dependency / 의존성); ROB giữ precise retirement; quay lui (rollback / 롤백) xóa speculative đường dẫn (path / 경로) sai.** hiệu năng (performance / 성능) phụ thuộc lượng independent công việc (work / 작업) thật sự và khả năng che độ trễ (latency / 지연 시간), không chỉ GHz hay số thực thi (execution / 실행) units.

> **Chuyển mạch:** Ở chặng này của **Out-of-order thực thi (execution / 실행), register renaming và reorder buffer**, **Kết nối** gom các mảnh từ **17. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [Memory consistency và ordering](./00_memory_consistency_cache_coherence_and_ordering.md), [Branch prediction và speculation](./02_branch_prediction_speculation_and_pipeline_recovery.md), [Cache hierarchy](./03_advanced_cache_hierarchy_prefetching_and_replacement.md) và OS advanced về page fault/syscall. Khi gỡ lỗi (debug / 디버그) hiệu năng (performance / 성능) xuyên tầng, nối tiếp [Debugging across abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
