# Liên kết kiến thức (knowledge connection / 지식 연결) — lớp trừu tượng (abstraction / 추상화) layers và leaky abstractions

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Abstraction layers và leaky abstractions**. Route bắt đầu từ contract/encapsulation, đi qua leakage, cross-layer debugging và performance, rồi kết thúc bằng câu hỏi layer nào thực sự sở hữu invariant khi abstraction không còn che được failure.


Computer các hệ thống (systems / 시스템들) are possible because no one thinks about all layers simultaneously. trình duyệt (browser / 브라우저) nhà phát triển (developer / 개발자) sees DOM/HTTP; backend sees objects/transactions; cơ sở dữ liệu (database / 데이터베이스) sees pages/logs; kernel sees processes/pages/sockets; CPU sees instructions/bộ nhớ đệm (cache / 캐시) lines. Each tầng (layer / 계층) offers an lớp trừu tượng (abstraction / 추상화) đặc tả hợp đồng (contract / 계약).

## Why lớp trừu tượng (abstraction / 추상화) is essential

Without lớp trừu tượng (abstraction / 추상화), to append văn bản (text / 텍스트) to tệp (file / 파일) nhà phát triển (developer / 개발자) would need điều khiển (control / 제어) SSD voltage cells. Filesystem turns blocks into files; thời gian chạy (runtime / 런타임) turns bộ nhớ (memory / 메모리) into objects; TCP turns packets into byte stream; SQL turns pages/indexes into relations/truy vấn (query / 쿼리) results.

Lớp trừu tượng (abstraction / 추상화) creates **cục bộ (local / 로컬) lập luận (reasoning / 추론)**: solve bài toán (problem / 문제) using mô hình (model / 모델) without reproducing lower-layer mechanics.


> **Nối mạch:** Abstraction giảm chi phí nhận thức bằng contract; khi latency, failure hoặc resource detail xuyên qua contract, đó là leaky abstraction cần được đo ở đúng tầng.

## Leaky lớp trừu tượng (abstraction / 추상화)

Joel Spolsky popularized “Law of Leaky Abstractions”: non-trivial abstractions leak to some degree. Meaning: hidden details can become observable when hiệu năng (performance / 성능), thất bại (failure / 실패) or edge cases matter.

Examples:

- SQL/ORM leaks chỉ mục (index / 인덱스)/cardinality because truy vấn (query / 쿼리) độ trễ (latency / 지연 시간) depends vật lý (physical / 물리적) plan.
- TCP byte stream leaks mạng (network / 네트워크) mất mát (loss / 손실)/RTT through độ trễ (latency / 지연 시간)/timeouts.
- GC leaks allocation/thời gian tồn tại (lifetime / 수명) via pauses/vùng nhớ động (heap / 힙) pressure.
- Virtual bộ nhớ (memory / 메모리) leaks page/TLB locality via hiệu năng (performance / 성능).
- Cloud đối tượng (object / 객체) lưu trữ (storage / 저장소) mounted as filesystem leaks different rename/consistency ngữ nghĩa (semantics / 의미론).

Leak does not make lớp trừu tượng (abstraction / 추상화) useless. It defines when engineer must descend a tầng (layer / 계층).


> **Nối mạch:** **Leaky lớp trừu tượng (abstraction / 추상화)** cung cấp điều kiện cho **tầng (layer / 계층) đặc tả hợp đồng (contract / 계약) and khả năng quan sát (observability / 관측 가능성)**; mục sau mở rộng cơ chế và chỉ ra giới hạn.

## Tầng (layer / 계층) đặc tả hợp đồng (contract / 계약) and khả năng quan sát (observability / 관측 가능성)

Each tầng (layer / 계층) transforms guarantees:

```text
Application semantics
↓
Language/runtime semantics
↓
OS abstractions
↓
ISA/memory model
↓
Microarchitecture
↓
Hardware physics
```

Across mạng (network / 네트워크):

```text
Application protocol
↓
TLS
↓
Transport
↓
IP
↓
Link
↓
Physical medium
```

A bug can be reasoned at highest tầng (layer / 계층) where bằng chứng (evidence / 증거) explains hành vi (behavior / 동작). Descend only when đặc tả hợp đồng (contract / 계약) no longer explains observation.


> **Nối mạch:** **tầng (layer / 계층) đặc tả hợp đồng (contract / 계약) and khả năng quan sát (observability / 관측 가능성)** cung cấp điều kiện cho **ranh giới (boundary / 경계) mismatch examples**; mục sau mở rộng cơ chế và chỉ ra giới hạn.

## Ranh giới (boundary / 경계) mismatch examples

### ORM N+1

Ứng dụng (application / 애플리케이션) thinks `order.customer` thuộc tính (property / 속성) truy cập (access / 접근) is cục bộ (local / 로컬); ORM lazily issues truy vấn (query / 쿼리) per thứ tự (order / 순서). đối tượng (object / 객체) lớp trừu tượng (abstraction / 추상화) hides remote/cơ sở dữ liệu (database / 데이터베이스) chi phí (cost / 비용). Fix requires understanding ranh giới (boundary / 경계) chi phí (cost / 비용) and batching/phép nối (join / 조인).

### Thread-per-request

Programmer thinks blocked luồng thực thi (thread / 스레드) cheap; OS luồng thực thi (thread / 스레드) has ngăn xếp (stack / 스택)/scheduler overhead. At 100k idle connections, thời gian chạy (runtime / 런타임) mô hình (model / 모델) leaks. Async/virtual threads thay đổi (change / 변경) biểu diễn (representation / 표현).

### Tệp (file / 파일) ghi (write / 쓰기) durability

App thinks `write()` “saved”; OS buffers; thiết bị (device / 장치) bộ nhớ đệm (cache / 캐시) not stable. Durability yêu cầu (requirement / 요구사항) leaks through tệp (file / 파일) lớp trừu tượng (abstraction / 추상화), requiring fsync/WAL.

### `HashMap` O(1)

Thuật toán (algorithm / 알고리즘) tầng (layer / 계층) says expected constant; microarchitecture sees bộ nhớ đệm (cache / 캐시) misses/đối tượng (object / 객체) allocations; adversarial collisions see O(n). hiệu năng (performance / 성능)/bảo mật (security / 보안) leak các giả định (assumptions / 가정들).


> **Nối mạch:** **ranh giới (boundary / 경계) mismatch examples** cung cấp điều kiện cho **Choosing lớp trừu tượng (abstraction / 추상화) mức (level / 수준) for debugging**; mục sau mở rộng cơ chế và chỉ ra giới hạn.

## Choosing lớp trừu tượng (abstraction / 추상화) mức (level / 수준) for debugging

Start with symptom and observable đặc tả hợp đồng (contract / 계약):

- Wrong nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) → ứng dụng (application / 애플리케이션)/giao dịch (transaction / 트랜잭션) invariants.
- truy vấn (query / 쿼리) slow → plan/chỉ mục (index / 인덱스)/cardinality then lưu trữ (storage / 저장소)/bộ nhớ đệm (cache / 캐시).
- CPU hot → profile nguồn (source / 소스)/JIT then bộ nhớ đệm (cache / 캐시)/branch if needed.
- yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) → traces/queues/downstream/mạng (network / 네트워크).
- bộ nhớ (memory / 메모리) growth → allocation/retention/GC then OS RSS/page bộ nhớ đệm (cache / 캐시).

Avoid descending to assembly for every bài toán (problem / 문제); avoid refusing to descend when high-level mô hình (model / 모델) fails.


> **Nối mạch:** **Choosing lớp trừu tượng (abstraction / 추상화) mức (level / 수준) for debugging** cung cấp điều kiện cho **Encapsulation and escape hatches**; mục sau mở rộng cơ chế và chỉ ra giới hạn.

## Encapsulation and escape hatches

Good lớp trừu tượng (abstraction / 추상화) offers safe dùng chung (common / 공통) đường dẫn (path / 경로) plus measured escape hatch: SQL hints/raw SQL, memory-mapped I/O, bản địa (native / 네이티브) interop, custom allocator, vận chuyển (transport / 전송) cấu hình (configuration / 구성). Escape hatch should be tường minh (explicit / 명시적) because caller now inherits lower-level các ràng buộc (constraints / 제약조건들).


> **Nối mạch:** **Encapsulation and escape hatches** cung cấp điều kiện cho **tầng (layer / 계층) inversion hazards**; mục sau mở rộng cơ chế và chỉ ra giới hạn.

## Tầng (layer / 계층) inversion hazards

If nghiệp vụ (business / 비즈니스) tầng (layer / 계층) depends on storage-page details, coupling makes thay đổi (change / 변경) hard. Conversely hạ tầng (infrastructure / 인프라) mã (code / 코드) cannot ignore lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론) like idempotency/giao dịch (transaction / 트랜잭션) boundaries. kiến trúc (architecture / 아키텍처) should điểm (point / 지점) dependencies toward stable chính sách (policy / 정책) while adapters know mechanisms.


> **Nối mạch:** **tầng (layer / 계층) inversion hazards** cung cấp điều kiện cho **mô hình tư duy (mental model / 사고 모델)**; mục sau mở rộng cơ chế và chỉ ra giới hạn.

## Mô hình tư duy (mental model / 사고 모델)

> lớp trừu tượng (abstraction / 추상화) is a **lossy compression of lower-layer reality**: it preserves properties most users need and hides the rest. When hidden variables become relevant, descend deliberately, learn the leaked cơ chế (mechanism / 메커니즘), then return to the highest useful mô hình (model / 모델).


> **Nối mạch:** **mô hình tư duy (mental model / 사고 모델)** cung cấp điều kiện cho **Cross-references**; mục sau mở rộng cơ chế và chỉ ra giới hạn.

## Cross-references

Mục này bàn giao kiến thức sang các domain liên quan. Hãy theo từng liên kết để biết prerequisite nào đang được dùng, ứng dụng nào được mở rộng và ranh giới nào vẫn cần giữ.

- [What Computer Science studies](../00_computation_information/00_what_computer_science_studies.md)
- [Abstraction/modularity/API](../08_software_systems/00_abstraction_modularity_interfaces_and_apis.md)
- [Source code → CPU](./00_source_code_to_cpu.md)
- [Browser → database](./01_browser_to_database_request.md)
- [Cross-cutting trade-offs](./03_cross_cutting_tradeoffs.md)

> **Bàn giao:** Sau **Cross-references**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 source code to cpu](./00_source_code_to_cpu.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
