# Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán ban đầu: hiệu năng (performance / 성능) cần tự do, software cần một hợp đồng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Coherence và consistency trả lời hai câu hỏi khác nhau** để mở câu hỏi trung tâm cho phần kế tiếp. Mạch này nối memory consistency với cache coherence và ordering, để nhiều core cùng nhìn dữ liệu theo quy tắc nào.

Trong single-thread mã (code / 코드), ta thường hình dung read/ghi (write / 쓰기) xảy ra theo đúng thứ tự nguồn (source / 소스). Trên multicore hiện đại, trình biên dịch (compiler / 컴파일러), CPU chuỗi xử lý (pipeline / 파이프라인), store buffer, invalidate hàng đợi (queue / 큐), bộ nhớ đệm (cache / 캐시) hierarchy và interconnect đều được phép trì hoãn hoặc sắp xếp lại một số bộ nhớ (memory / 메모리) operations để che độ trễ (latency / 지연 시간). Vì vậy tính đồng thời (concurrency / 동시성) tính đúng đắn (correctness / 정확성) không thể lập luận (reasoning / 추론) bằng trực giác “dòng nào viết trước”.

Chương này giữ một bất biến (invariant / 불변식) xuyên nhiều tầng: **bộ nhớ đệm (cache / 캐시) coherence giữ lịch sử hợp lệ của từng location; ISA memory-consistency mô hình (model / 모델) giới hạn những quan sát cross-location phần cứng được phép tạo ra; ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) định nghĩa đặc tả hợp đồng (contract / 계약) mà mã nguồn (source code / 소스 코드) có quyền dựa vào; synchronization primitives tạo thứ tự (ordering / 순서) edges đủ để chứng minh bất biến (invariant / 불변식) của chương trình.**

## 1. Bài toán ban đầu: hiệu năng (performance / 성능) cần tự do, software cần một hợp đồng

Nếu mỗi store phải chờ mọi cốt lõi (core / 핵심) khác quan sát được giá trị mới trước khi cốt lõi (core / 핵심) hiện tại chạy tiếp, CPU sẽ lãng phí rất nhiều cycle. Hardware vì thế dùng store buffer, speculative thực thi (execution / 실행), out-of-order thực thi (execution / 실행) và nhiều outstanding bộ nhớ (memory / 메모리) requests để tiếp tục làm việc khi coherence traffic hoặc DRAM truy cập (access / 접근) còn đang chờ.

Software lại cần các thuộc tính (property / 속성) như:

```text
release lock xong
→ thread acquire cùng lock phải thấy state được bảo vệ

publish payload xong bằng release
→ reader acquire publication flag phải được phép dùng payload
```

Thiết kế bộ nhớ (memory / 메모리) mô hình (model / 모델) là một thỏa hiệp: cho trình biên dịch (compiler / 컴파일러)/hardware đủ freedom để tối ưu nhưng vẫn cung cấp thành phần nguyên thủy (primitive / 기본 요소) đủ mạnh để software chứng minh tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Performance cần hardware freedom nhưng software cần contract; coherence giữ một cache line nhất quán, consistency quy định thứ tự quan sát giữa nhiều location, và store buffer tạo độ trễ visibility.

## 2. Coherence và consistency trả lời hai câu hỏi khác nhau

**Nhất quán bộ nhớ đệm (cache / 캐시)** chủ yếu hỏi: với **một bộ nhớ (memory / 메모리) location**, các cores có quan sát writes theo một lịch sử tương thích hay không? giao thức (protocol / 프로토콜) kiểu MESI/MOESI quản lý quyền sở hữu (ownership / 소유권)/trạng thái (state / 상태) của bộ nhớ đệm (cache / 캐시) lines để nhiều bộ nhớ đệm (cache / 캐시) không tự do ghi các phiên bản mâu thuẫn.

**Mô hình nhất quán bộ nhớ (memory consistency model / 메모리 일관성 모델)** hỏi rộng hơn: với nhiều locations và nhiều processors, những thứ tự (ordering / 순서) nào của reads/writes được phép quan sát?

Sequential consistency là mô hình (model / 모델) trực quan: kết quả như thể mọi bộ nhớ (memory / 메모리) operations của mọi threads được xen kẽ trong một toàn cục (global / 전역) thứ tự (order / 순서) trong khi mỗi luồng thực thi (thread / 스레드) giữ program thứ tự (order / 순서). Hardware thực tế thường cho phép mô hình (model / 모델) yếu hơn để đạt hiệu năng (performance / 성능) tốt hơn.

Điểm phải giữ: **coherence của từng location không tự tạo cross-location thứ tự (ordering / 순서)**. `payload` và `ready` có thể đều coherent nhưng reader không được suy luận `ready == true` kéo theo payload đã visible nếu giao thức (protocol / 프로토콜) thiếu synchronization đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **3. Store buffer giải thích vì sao store chưa chắc visible ngay** tiếp nhận điểm tựa từ **2. Coherence và consistency trả lời hai câu hỏi khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Message-passing kiểm thử (test / 테스트): publication cần một thứ tự (ordering / 순서) edge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Store buffer giải thích vì sao store chưa chắc visible ngay

Khi cốt lõi (core / 핵심) thực hiện store, nó có thể đặt ghi (write / 쓰기) vào store buffer rồi tiếp tục thay vì chờ quyền sở hữu (ownership / 소유권)/bộ nhớ đệm (cache / 캐시) propagation hoàn tất. cốt lõi (core / 핵심) đó thường forward được giá trị (value / 값) từ buffer cho chính nó, nhưng cốt lõi (core / 핵심) khác chưa chắc thấy ghi (write / 쓰기) ngay.

Xét litmus kiểm thử (test / 테스트) Store Buffering:

```text
Initially x = 0, y = 0

Thread A:        Thread B:
x = 1           y = 1
r1 = y           r2 = x
```

Trực giác sequential dễ cho rằng `r1 = 0 && r2 = 0` “không thể”. Nhưng trên mô hình (model / 모델) cho phép store→tải (load / 로드) reordering hoặc delayed visibility, kết quả (outcome / 결과) này có thể hợp lệ khi không có synchronization phù hợp.

Litmus kiểm thử (test / 테스트) không phải mẹo phỏng vấn. Nó là cách cô lập đặc tả hợp đồng (contract / 계약): đưa một thực thi (execution / 실행) rất nhỏ, liệt kê kết quả (outcome / 결과) nào mô hình (model / 모델) cho phép, rồi so sánh ngôn ngữ (language / 언어) → trình biên dịch (compiler / 컴파일러) → ISA. Nếu một kết quả (outcome / 결과) bị cấm ở ngôn ngữ (language / 언어) mức (level / 수준) thì trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) phải phát mã máy (machine code / 기계어) đủ mạnh để cấm nó trên mục tiêu (target / 대상) ISA.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **4. Message-passing kiểm thử (test / 테스트): publication cần một thứ tự (ordering / 순서) edge** tiếp nhận điểm tựa từ **3. Store buffer giải thích vì sao store chưa chắc visible ngay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Invalidate hàng đợi (queue / 큐) và visibility không phải một sự kiện toàn cục tức thì** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Message-passing kiểm thử (test / 테스트): publication cần một thứ tự (ordering / 순서) edge

Xét:

```text
Writer:                 Reader:
payload = 42            if (ready) {
ready = true                use(payload)
                        }
```

Bất biến (invariant / 불변식) mong muốn là: **nếu reader quan sát publication sự kiện (event / 이벤트) `ready`, nó phải quan sát initialization của `payload` tương ứng**.

Plain stores/loads không nhất thiết tạo bất biến (invariant / 불변식) này. Một giao thức (protocol / 프로토콜) đúng thường biểu diễn publication bằng release-store và observation bằng acquire-load, hoặc dùng khóa (lock / 잠금)/monitor/thành phần nguyên thủy (primitive / 기본 요소) có ngữ nghĩa (semantics / 의미론) tương đương ở ngôn ngữ (language / 언어) mức (level / 수준).

Điểm quan trọng là không hỏi “CPU có reorder hai instruction này không?” trước. Hãy hỏi **tầng mã nguồn (source-level / 소스 수준) giao thức (protocol / 프로토콜) có happens-before edge không?** Nếu không, việc mã (code / 코드) “chạy đúng trên máy tôi” không tạo guarantee.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **5. Invalidate hàng đợi (queue / 큐) và visibility không phải một sự kiện toàn cục tức thì** tiếp nhận điểm tựa từ **4. Message-passing kiểm thử (test / 테스트): publication cần một thứ tự (ordering / 순서) edge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Fence không phải lệnh “flush toàn bộ bộ nhớ đệm (cache / 캐시)”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Invalidate hàng đợi (queue / 큐) và visibility không phải một sự kiện toàn cục tức thì

Coherence yêu cầu (request / 요청) đi qua interconnect, directories và queues. Một cốt lõi (core / 핵심) có thể nhận vô hiệu hóa (invalidation / 무효화)/quyền sở hữu (ownership / 소유권) traffic ở thời điểm khác cốt lõi (core / 핵심) khác, miễn hành vi cuối vẫn nằm trong ISA bộ nhớ (memory / 메모리) mô hình (model / 모델).

Vì vậy câu “ghi (write / 쓰기) đã tới L1 nên mọi cốt lõi (core / 핵심) phải thấy ngay” không phải lập luận (reasoning / 추론) hợp lệ. Software không có đặc tả hợp đồng (contract / 계약) trực tiếp với thời điểm nội bộ của coherence messages; software có đặc tả hợp đồng (contract / 계약) với thứ tự (ordering / 순서) primitives của ISA và ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델).

Tương tự, “bộ nhớ đệm (cache / 캐시) coherent” không nghĩa “tất cả cores có cùng snapshot tại cùng nanosecond”. Coherence là giao thức (protocol / 프로토콜) về thứ tự/quyền sở hữu (ownership / 소유권), không phải barrier toàn hệ thống sau mọi store.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **6. Fence không phải lệnh “flush toàn bộ bộ nhớ đệm (cache / 캐시)”** tiếp nhận điểm tựa từ **5. Invalidate hàng đợi (queue / 큐) và visibility không phải một sự kiện toàn cục tức thì** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. trình biên dịch (compiler / 컴파일러) reordering và CPU reordering là hai tầng khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Fence không phải lệnh “flush toàn bộ bộ nhớ đệm (cache / 캐시)”

Bộ nhớ (memory / 메모리) fence áp thứ tự (ordering / 순서) các ràng buộc (constraints / 제약조건들) lên classes bộ nhớ (memory / 메모리) operations theo ngữ nghĩa (semantics / 의미론) của ISA. Acquire thường ngăn operations sau acquire vượt qua synchronization điểm (point / 지점) theo đặc tả hợp đồng (contract / 계약) cần thiết; bản phát hành (release / 릴리스) giữ effects trước bản phát hành (release / 릴리스) không bị đẩy qua publication điểm (point / 지점) theo cách phá giao thức (protocol / 프로토콜); full fence mạnh hơn và thường hạn chế tối ưu hóa (optimization / 최적화) nhiều hơn.

Lập luận (reasoning / 추론) đúng phải bắt đầu bằng:

```text
operation A phải precede operation B trong quan sát nào?
writer và reader liên hệ qua primitive nào?
ordering tối thiểu nào đủ để giữ invariant?
```

Dùng fence “cho chắc” có thể che giao thức (protocol / 프로토콜) yếu và tạo chi phí (cost / 비용) không cần thiết. Dùng fence quá yếu có thể giữ benchmark nhanh nhưng làm proof sai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **7. trình biên dịch (compiler / 컴파일러) reordering và CPU reordering là hai tầng khác nhau** tiếp nhận điểm tựa từ **6. Fence không phải lệnh “flush toàn bộ bộ nhớ đệm (cache / 캐시)”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Happens-before là lớp trừu tượng (abstraction / 추상화) software nên dùng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. trình biên dịch (compiler / 컴파일러) reordering và CPU reordering là hai tầng khác nhau

Trình biên dịch (compiler / 컴파일러) có thể hoist/sink load-store, giữ giá trị (value / 값) trong register, eliminate redundant truy cập (access / 접근) hoặc transform điều khiển (control / 제어) luồng (flow / 흐름) nếu ngôn ngữ (language / 언어) specification cho phép. CPU lại có freedom riêng theo ISA bộ nhớ (memory / 메모리) mô hình (model / 모델).

Do đó cùng một tầng mã nguồn (source-level / 소스 수준) acquire/bản phát hành (release / 릴리스) có thể compile thành machine chuỗi (sequence / 시퀀스) khác nhau trên x86-64 và ARM64. Một ISA có baseline thứ tự (ordering / 순서) mạnh hơn có thể cần ít tường minh (explicit / 명시적) fence hơn; ISA yếu hơn có thể cần instruction/thứ tự (order / 순서) thành phần nguyên thủy (primitive / 기본 요소) rõ hơn.

Bất biến (invariant / 불변식) cần giữ không phải “assembly trên mọi CPU phải giống nhau”, mà là:

> mã máy (machine code / 기계어) trên mỗi mục tiêu (target / 대상) phải thực hiện cùng đặc tả hợp đồng (contract / 계약) mà ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) đã hứa.

Đây là lý do mã (code / 코드) tự chế dựa vào hành vi (behavior / 동작) accidental của một kiến trúc (architecture / 아키텍처) có thể thất bại (fail / 실패) sau khi cổng (port / 포트), đổi trình biên dịch (compiler / 컴파일러) hoặc bật tối ưu hóa (optimization / 최적화) khác.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **8. Happens-before là lớp trừu tượng (abstraction / 추상화) software nên dùng** tiếp nhận điểm tựa từ **7. trình biên dịch (compiler / 컴파일러) reordering và CPU reordering là hai tầng khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Atomicity, visibility và thứ tự (ordering / 순서) phải được tách riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Happens-before là lớp trừu tượng (abstraction / 추상화) software nên dùng

Ở ứng dụng (application / 애플리케이션)/thời gian chạy (runtime / 런타임) tầng (layer / 계층), ta hiếm khi lập luận (reasoning / 추론) trực tiếp bằng MESI states. Ta dùng **xảy-ra-trước (happens-before)**: program thứ tự (order / 순서), synchronization edges và transitivity tạo ra visibility/thứ tự (order / 순서) guarantees hợp lệ.

```text
write data
   ↓ program order
release / unlock
   ↓ synchronization edge
acquire / lock
   ↓ program order
read data
```

“Xảy ra sớm hơn theo wall clock” không đồng nghĩa happens-before. Một ghi (write / 쓰기) có thể vật lý xảy ra trước nhưng reader vẫn không có quyền suy luận visibility nếu thiếu synchronization edge.

Lower tầng (layer / 계층) giải thích vì sao stale/reordered observation có thể xuất hiện; ngôn ngữ (language / 언어) mô hình (model / 모델) quyết định chương trình **được phép dựa vào điều gì**.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **9. Atomicity, visibility và thứ tự (ordering / 순서) phải được tách riêng** tiếp nhận điểm tựa từ **8. Happens-before là lớp trừu tượng (abstraction / 추상화) software nên dùng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Atomic RMW tạo serialization điểm (point / 지점) vật lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Atomicity, visibility và thứ tự (ordering / 순서) phải được tách riêng

Một atomic tải (load / 로드)/store bảo vệ một loại thuộc tính (property / 속성), nhưng giao thức (protocol / 프로토콜) có thể còn cần thứ tự (ordering / 순서). Một fence tạo thứ tự (ordering / 순서) nhưng không tự biến chuỗi read→modify→ghi (write / 쓰기) thành atomic giao dịch (transaction / 트랜잭션).

Khi rà soát (review / 검토) mã (code / 코드), tách ba câu hỏi:

```text
Atomicity   : operation có thể bị interleave thành lost update không?
Visibility  : write nào reader được bảo đảm nhìn thấy?
Ordering    : reader được phép suy luận operation nào đứng trước/sau?
```

Rất nhiều bug xuất phát từ việc lấy thành phần nguyên thủy (primitive / 기본 요소) giải một câu hỏi rồi giả định hai câu còn lại cũng được giải tự động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **10. Atomic RMW tạo serialization điểm (point / 지점) vật lý** tiếp nhận điểm tựa từ **9. Atomicity, visibility và thứ tự (ordering / 순서) phải được tách riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. False sharing: lô-gic (logic / 논리) độc lập nhưng vật lý vẫn tranh một bộ nhớ đệm (cache / 캐시) line** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Atomic RMW tạo serialization điểm (point / 지점) vật lý

Compare-and-swap, fetch-add và các atomic read-modify-write thường cần exclusive quyền sở hữu (ownership / 소유권) của bộ nhớ đệm (cache / 캐시) line. Khi nhiều cores cùng cập nhật một toàn cục (global / 전역) counter, tính đúng đắn (correctness / 정확성) có thể hoàn hảo nhưng bộ nhớ đệm (cache / 캐시) line phải ping-pong qua interconnect.

Nhân quả (causal / 인과적) đường dẫn (path / 경로):

```text
threads tăng
→ nhiều RMW cùng một line
→ ownership transfer/invalidation tăng
→ retries hoặc serialization tăng
→ stalled cycles tăng
→ throughput dừng tăng hoặc giảm
```

Ở đây lower lớp trừu tượng (abstraction / 추상화) thực sự quyết định scalability là **coherence granularity + topology**, không phải ALU speed. Sharded/per-core counters, batching hoặc partitioned quyền sở hữu (ownership / 소유권) có thể tốt hơn một atomic toàn cục (global / 전역) counter tùy bất biến (invariant / 불변식).

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **11. False sharing: lô-gic (logic / 논리) độc lập nhưng vật lý vẫn tranh một bộ nhớ đệm (cache / 캐시) line** tiếp nhận điểm tựa từ **10. Atomic RMW tạo serialization điểm (point / 지점) vật lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Lock-free không đồng nghĩa “không còn thời gian tồn tại (lifetime / 수명) bài toán (problem / 문제)”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. False sharing: lô-gic (logic / 논리) độc lập nhưng vật lý vẫn tranh một bộ nhớ đệm (cache / 캐시) line

Hai threads sửa hai fields khác nhau nhưng nằm cùng bộ nhớ đệm (cache / 캐시) line có thể làm line ping-pong giữa cores. Đây là **chia sẻ giả (false sharing)**: nguồn (source / 소스) không có logical sharing nhưng hardware có vật lý (physical / 물리적) sharing ở coherence granularity.

Padding/alignment hoặc thay dữ liệu (data / 데이터) bố cục (layout / 레이아웃) có thể sửa vì lớp trừu tượng (abstraction / 추상화) quyết định hành vi (behavior / 동작) là cache-line placement. Đây cũng là lời nhắc rằng hiệu năng (performance / 성능) bug có thể nằm dưới lớp trừu tượng (abstraction / 추상화) mà tính đúng đắn (correctness / 정확성) hoàn toàn đúng.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **12. Lock-free không đồng nghĩa “không còn thời gian tồn tại (lifetime / 수명) bài toán (problem / 문제)”** tiếp nhận điểm tựa từ **11. False sharing: lô-gic (logic / 논리) độc lập nhưng vật lý vẫn tranh một bộ nhớ đệm (cache / 캐시) line** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. NUMA làm “bộ nhớ (memory / 메모리)” không còn có một độ trễ (latency / 지연 시간) duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Lock-free không đồng nghĩa “không còn thời gian tồn tại (lifetime / 수명) bài toán (problem / 문제)”

CAS cho phép xây lock-free cấu trúc (structure / 구조), nhưng proof phải bao gồm linearization điểm (point / 지점), bộ nhớ (memory / 메모리) thứ tự (ordering / 순서), ABA, đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) và reclamation.

ABA minh họa leaky lớp trừu tượng (abstraction / 추상화):

```text
thread A đọc pointer P
thread B remove P, free/reuse memory, rồi một pointer có cùng bit pattern P xuất hiện lại
thread A CAS thấy bit pattern vẫn giống
```

CAS chỉ so sánh giá trị (value / 값) theo đặc tả hợp đồng (contract / 계약) của nó; nó không chứng minh đối tượng (object / 객체) định danh (identity / 식별자)/thời gian tồn tại (lifetime / 수명) vẫn là đối tượng (object / 객체) cũ. Hazard pointer, epoch-based reclamation, tham chiếu (reference / 참조) counting hoặc tagged/versioned pointer là các family giải pháp khác nhau vì chúng bổ sung **thời gian tồn tại (lifetime / 수명) bất biến (invariant / 불변식)** mà atomic thành phần nguyên thủy (primitive / 기본 요소) đơn lẻ không cung cấp.

Lock-free chỉ hứa system-wide progress theo định nghĩa; một luồng thực thi (thread / 스레드) cụ thể vẫn có thể starve. Wait-free mạnh hơn nhưng proof burden cũng cao hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **13. NUMA làm “bộ nhớ (memory / 메모리)” không còn có một độ trễ (latency / 지연 시간) duy nhất** tiếp nhận điểm tựa từ **12. Lock-free không đồng nghĩa “không còn thời gian tồn tại (lifetime / 수명) bài toán (problem / 문제)”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. hiệu năng (performance / 성능) pressure làm hành vi (behavior / 동작) thay đổi theo phase** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. NUMA làm “bộ nhớ (memory / 메모리)” không còn có một độ trễ (latency / 지연 시간) duy nhất

Trên NUMA machine, page có home nút (node / 노드); cốt lõi (core / 핵심) truy cập remote bộ nhớ (memory / 메모리) phải đi qua interconnect. dùng chung (shared / 공유) bộ nhớ đệm (cache / 캐시) line bị ghi xuyên socket có thể đắt hơn nhiều so với cùng socket.

Một toàn cục (global / 전역) khóa (lock / 잠금)/counter đúng về lô-gic (logic / 논리) có thể trở thành bottleneck vật lý do remote cache-line bouncing. luồng thực thi (thread / 스레드) placement, page placement và quyền sở hữu (ownership / 소유권) topology vì vậy thuộc hiệu năng (performance / 성능) lập luận (reasoning / 추론) của tính đồng thời (concurrency / 동시성).

Đọc tiếp [NUMA, interconnects và scalable coherence](./04_numa_interconnects_and_scalable_coherence.md).

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **14. hiệu năng (performance / 성능) pressure làm hành vi (behavior / 동작) thay đổi theo phase** tiếp nhận điểm tựa từ **13. NUMA làm “bộ nhớ (memory / 메모리)” không còn có một độ trễ (latency / 지연 시간) duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Vì sao bug có thể “chỉ xảy ra trên ARM” hoặc “chỉ khi tải cao”?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. hiệu năng (performance / 성능) pressure làm hành vi (behavior / 동작) thay đổi theo phase

Ở low contention, một atomic hoặc mutex có thể gần như miễn phí so với nghiệp vụ (business / 비즈니스) công việc (work / 작업). Khi contention tăng, chi phí (cost / 비용) không còn tuyến tính vì quyền sở hữu (ownership / 소유권) transfer, spinning, parking/unparking, scheduler tương tác (interaction / 상호작용) và trượt bộ nhớ đệm (cache miss / 캐시 미스) bắt đầu dominate.

Thứ tự (ordering / 순서) mạnh hơn có thể hạn chế trình biên dịch (compiler / 컴파일러)/hardware reordering; thứ tự (ordering / 순서) yếu hơn cho nhiều hiệu năng (performance / 성능) latitude nhưng tăng proof burden. tối ưu hóa (optimization / 최적화) đúng phải giữ bất biến (invariant / 불변식) và đo tải công việc (workload / 워크로드) thật, không chọn `relaxed` chỉ vì microbenchmark ngắn hơn.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **15. Vì sao bug có thể “chỉ xảy ra trên ARM” hoặc “chỉ khi tải cao”?** tiếp nhận điểm tựa từ **14. hiệu năng (performance / 성능) pressure làm hành vi (behavior / 동작) thay đổi theo phase** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. bằng chứng vận hành (production evidence / 운영 증거): chọn bằng chứng (evidence / 증거) theo tầng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Vì sao bug có thể “chỉ xảy ra trên ARM” hoặc “chỉ khi tải cao”?

Hai trường hợp cần tách:

```text
Architecture-sensitive correctness:
program vô tình dựa vào ordering mạnh hơn của platform cũ
→ target ISA/compiler mới lộ execution vốn đã không được language guarantee

Load-sensitive correctness/performance:
contention/interleaving window mở rộng
→ race xuất hiện thường hơn hoặc coherence bottleneck tăng mạnh
```

Không nên kết luận “ARM có bug” hay “CPU quá tải làm sai dữ liệu”. Hãy kiểm tra đặc tả hợp đồng (contract / 계약) tầng mã nguồn (source-level / 소스 수준) trước, rồi dùng ISA/microarchitecture để giải thích tại sao symptom lộ ở môi trường đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **15. Vì sao bug có thể “chỉ xảy ra trên ARM” hoặc “chỉ khi tải cao”?** nêu điều cần giải thích; **16. bằng chứng vận hành (production evidence / 운영 증거): chọn bằng chứng (evidence / 증거) theo tầng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. thất bại (failure / 실패) lập luận (reasoning / 추론) theo lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. bằng chứng vận hành (production evidence / 운영 증거): chọn bằng chứng (evidence / 증거) theo tầng

Ở ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) tầng (layer / 계층), tìm race detector hoặc tính đồng thời (concurrency / 동시성) sanitizer khi ecosystem hỗ trợ, khóa (lock / 잠금)/park/contention profile, luồng thực thi (thread / 스레드)/tác vụ (task / 작업) dump và kiểm thử sức chịu tải (stress test / 스트레스 테스트) có bất biến (invariant / 불변식) check.

Ở OS tầng (layer / 계층), quan sát run hàng đợi (queue / 큐), ngữ cảnh (context / 맥락) switch, CPU di chuyển (migration / 마이그레이션), off-CPU wait, affinity và NUMA placement.

Ở hardware tầng (layer / 계층), dùng hiệu năng (performance / 성능) counters phù hợp CPU/công cụ (tool / 도구) để tìm trượt bộ nhớ đệm (cache miss / 캐시 미스), cache-to-cache transfer, stalled cycles, bộ nhớ (memory / 메모리) bandwidth và cục bộ (local / 로컬)/remote NUMA truy cập (access / 접근). PMU sự kiện (event / 이벤트) names khác theo vendor/mô hình (model / 모델); mô hình tư duy (mental model / 사고 모델) là tìm bằng chứng (evidence / 증거) cho **cache-line movement + thứ tự (ordering / 순서)/contention chi phí (cost / 비용) + chuỗi xử lý (pipeline / 파이프라인) stalls**, không học thuộc một counter name.

Bằng chứng (evidence / 증거) không thay proof. PMU cho biết line đang ping-pong nhưng không chứng minh happens-before; race detector có thể bỏ sót thực thi (execution / 실행). tính đúng đắn (correctness / 정확성) cần kết hợp:

```text
invariant/proof
+
reproducible stress/litmus execution
+
runtime/OS/hardware evidence
```

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **16. bằng chứng vận hành (production evidence / 운영 증거): chọn bằng chứng (evidence / 증거) theo tầng** nêu điều cần giải thích; **17. thất bại (failure / 실패) lập luận (reasoning / 추론) theo lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. thất bại (failure / 실패) lập luận (reasoning / 추론) theo lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층)

Nếu symptom là wrong giá trị (value / 값)/dữ liệu (data / 데이터) race, bắt đầu từ language-level quyền sở hữu (ownership / 소유권) và happens-before. Nếu program đúng nhưng scaling xấu, kiểm tra khóa (lock / 잠금)/RMW contention, false sharing, NUMA placement và bandwidth. Nếu chỉ một kiến trúc (architecture / 아키텍처) thất bại (fail / 실패), kiểm tra mã (code / 코드) có dựa vào accidental ISA thuộc tính (property / 속성) hay undefined/data-race hành vi (behavior / 동작) không.

Không xuống microarchitecture chỉ vì nó thú vị; xuống khi bằng chứng (evidence / 증거) cho thấy lớp trừu tượng (abstraction / 추상화) trên không đủ giải thích symptom.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **18. Mô hình tư duy** gom các mảnh từ **17. thất bại (failure / 실패) lập luận (reasoning / 추론) theo lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Mô hình tư duy

> Coherence giữ lịch sử của một location không tự mâu thuẫn; ISA bộ nhớ (memory / 메모리) mô hình (model / 모델) giới hạn những observation phần cứng được phép; ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) biến chúng thành đặc tả hợp đồng (contract / 계약) tầng mã nguồn (source-level / 소스 수준); synchronization tạo happens-before; cache-line quyền sở hữu (ownership / 소유권) và NUMA quyết định nhiều chi phí (cost / 비용) vật lý. **Program tính đúng đắn (correctness / 정확성) phải được chứng minh ở lớp trừu tượng (abstraction / 추상화) sở hữu bất biến (invariant / 불변식), còn lower tầng (layer / 계층) giải thích vì sao bug hoặc bottleneck có thể xuất hiện.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리) consistency, bộ nhớ đệm (cache / 캐시) coherence và thứ tự (ordering / 순서)**, **Kết nối** gom các mảnh từ **18. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Nền tảng: [Cache hierarchy](../../basic/02_computer_architecture/02_memory_hierarchy_and_cache.md), [OS concurrency](../../basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md) và [Programming Languages concurrency](../../basic/04_programming_languages/08_concurrency_models_and_memory_safety.md). Đường xuyên tầng hoàn chỉnh: [CPU cache → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md). Đọc tiếp [OoO/ROB](./01_out_of_order_execution_register_renaming_and_rob.md), [NUMA](./04_numa_interconnects_and_scalable_coherence.md) và [Runtime concurrency](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
