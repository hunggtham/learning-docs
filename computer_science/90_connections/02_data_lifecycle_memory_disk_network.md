# Liên kết kiến thức (knowledge connection / 지식 연결) — Vòng đời dữ liệu: register → RAM → disk → mạng (network / 네트워크)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Vòng đời dữ liệu: register → RAM → disk → network**. Route theo representation và copy: CPU/register → runtime/heap → socket/kernel buffer → database/WAL → filesystem/device → replica/cache; ở mỗi boundary cần hỏi ownership, freshness và durability guarantee.


“dữ liệu (data / 데이터)” không phải một đối tượng (object / 객체) đứng yên ở một chỗ. Trong thời gian tồn tại (lifetime / 수명) của một yêu cầu (request / 요청), cùng logical giá trị (value / 값) có thể tồn tại dưới nhiều representations và copies: CPU register, bộ nhớ đệm (cache / 캐시) line, vùng nhớ động (heap / 힙) đối tượng (object / 객체), kernel buffer, filesystem page, SSD khối (block / 블록), cơ sở dữ liệu (database / 데이터베이스) page, mạng (network / 네트워크) packet và remote replica.

## Một giá trị (value / 값) trong CPU

Suppose Java trường dữ liệu (field / 필드) `balance=1000`. đối tượng (object / 객체) tham chiếu (reference / 참조) leads to bộ nhớ vùng động (heap memory / 힙 메모리). CPU tải (load / 로드) virtual address; TLB translates; bộ nhớ đệm (cache / 캐시) hierarchy returns line; relevant bytes enter register. Arithmetic updates register giá trị (value / 값); store marks bộ nhớ đệm (cache / 캐시) line dirty.

At this điểm (point / 지점) cơ sở dữ liệu (database / 데이터베이스)/disk knows nothing about thay đổi (change / 변경).

## Thời gian chạy (runtime / 런타임) bộ nhớ (memory / 메모리)

Vùng nhớ vùng nhớ động (heap / 힙) biểu diễn đối tượng (object representation / 객체 표현) includes fields/header/alignment. GC tracks reachability; đối tượng (object / 객체) may move during compacting collection while ngữ nghĩa (semantic / 의미적) tham chiếu (reference / 참조) remains valid.

Ứng dụng (application / 애플리케이션) can serialize `1000` as JSON characters `1 0 0 0`, not same bytes as 64-bit nhị phân (binary / 이진) integer.

Biểu diễn (representation / 표현) changed while meaning stayed.

> **Chuyển mạch:** Runtime đã đổi logical value thành object/bytes nhưng chưa tạo durability. **Kernel and socket buffers** tiếp nhận cùng bytes qua một boundary mới, nơi copy/zero-copy, framing và encryption quyết định representation nào thực sự rời process.

## Kernel and socket buffers

`send()` copies or references bytes into kernel/mạng (network / 네트워크) buffers depending API/zero-copy. TCP adds chuỗi (sequence / 시퀀스) trạng thái (state / 상태); TLS encrypts plaintext into ciphertext records; IP/link add headers. NIC DMA reads buffers and transmits symbols.

Remote machine reverses layers to reconstruct ứng dụng (application / 애플리케이션) bytes.

> **Chuyển mạch:** Socket path mô tả transport, còn durability bắt đầu khi database nhận và ghi lại bytes. **Cơ sở dữ liệu (database / 데이터베이스) buffer pool** tách page đang dirty khỏi WAL đã commit, nên “đã lưu” phải được đọc theo guarantee cụ thể.

## Cơ sở dữ liệu (database / 데이터베이스) buffer pool

DB parses numeric văn bản (text / 텍스트)/nhị phân (binary / 이진) giao thức (protocol / 프로토콜) into nội bộ (internal / 내부) kiểu (type / 타입). Row phiên bản (version / 버전) stored in page in buffer pool. lần ghi nhận (commit / 커밋) may append WAL bản ghi (record / 레코드) first; dữ liệu (data / 데이터) page remains dirty bộ nhớ (memory / 메모리) and flush later.

Thus logical “saved” can mean giao dịch (transaction / 트랜잭션) durable via log even though bảng (table / 테이블) page not yet written.

## Filesystem and thiết bị (device / 장치)

WAL ghi (write / 쓰기) passes OS page bộ nhớ đệm (cache / 캐시) or direct I/O, khối (block / 블록) tầng (layer / 계층), controller hàng đợi (queue / 큐), thiết bị (device / 장치) bộ nhớ đệm (cache / 캐시), flash translation tầng (layer / 계층). `fsync`/barriers establish thứ tự (ordering / 순서)/durability các giả định (assumptions / 가정들).

SSD stores vật lý (physical / 물리적) charge states unrelated to tầng mã nguồn (source-level / 소스 수준) integer bố cục (layout / 레이아웃).

> **Chuyển mạch:** Filesystem/device quyết định thứ tự và độ bền của local media; logical record vẫn có thể có bản sao khác ở replica. **Replication** tiếp tục bằng freshness và acknowledgment, không mặc định rằng primary commit đồng nghĩa mọi copy đã bền.

## Replication

Primary ships WAL/logical thay đổi (change / 변경) over mạng (network / 네트워크). Replica writes its own log/pages. At one moment primary committed but replica still stale if asynchronous.

Now one logical bản ghi (record / 레코드) has multiple versions/copies with different freshness.

> **Chuyển mạch:** Replication làm rõ nhiều bản copy, còn **Bộ nhớ đệm (cache / 캐시) copies** thêm các representation dẫn xuất có invalidation riêng. Từ đây cần phân biệt copy với reference để biết ai sở hữu mutation và freshness guarantee.

## Bộ nhớ đệm (cache / 캐시) copies

Ứng dụng (application / 애플리케이션)/Redis/CDN may bộ nhớ đệm (cache / 캐시) derived biểu diễn (representation / 표현). vô hiệu hóa (invalidation / 무효화) message can lag/thất bại (fail / 실패), so bộ nhớ đệm (cache / 캐시) returns stale giá trị (value / 값). bộ nhớ đệm (cache / 캐시) consistency is data-lifecycle bài toán (problem / 문제): copies need quyền sở hữu (ownership / 소유권)/freshness rules.

## Copying vs referencing

Every ranh giới (boundary / 경계) can bản sao (copy / 복사) or share. bản sao (copy / 복사) isolates thời gian tồn tại (lifetime / 수명)/mutation but costs bandwidth/bộ nhớ (memory / 메모리). dùng chung (shared / 공유) bộ nhớ (memory / 메모리)/zero-copy reduces bản sao (copy / 복사) chi phí (cost / 비용) but complicates quyền sở hữu (ownership / 소유권), synchronization and pinning.

Serialization necessarily creates another biểu diễn (representation / 표현); zero-copy cannot eliminate ngữ nghĩa (semantic / 의미적) transformation if protocols differ.

## Durability levels

Think in stages:

```text
CPU register/cache
→ process heap
→ kernel/buffer cache
→ device volatile cache
→ stable local media
→ remote replica memory
→ remote stable media
→ backup/archive
```

A hệ thống (system / 시스템)'s “durable” đặc tả hợp đồng (contract / 계약) chooses required stage(s). Acknowledging at tiến trình (process / 프로세스) bộ nhớ (memory / 메모리) is very different from quorum stable lưu trữ (storage / 저장소).

## Dữ liệu (data / 데이터) integrity

Checksums/CRC detect accidental corruption at layers; AEAD/MAC detect adversarial tampering; cơ sở dữ liệu (database / 데이터베이스) các ràng buộc (constraints / 제약조건들) validate ngữ nghĩa (semantic / 의미적) integrity. Same word “integrity” spans different threat các mô hình (models / 모델들).

## Dữ liệu (data / 데이터) deletion

Deleting logical bản ghi (record / 레코드) may remove chỉ mục (index / 인덱스)/tham chiếu (reference / 참조) but copies survive in WAL, replica, bộ nhớ đệm (cache / 캐시), backup or SSD blocks until retention/GC/secure erase. Privacy/compliance deletion therefore needs full data-flow inventory.

## Mô hình tư duy (mental model / 사고 모델)

> Treat dữ liệu (data / 데이터) as **a lineage of representations and copies**, not one variable. At every ranh giới (boundary / 경계) ask: encoding gì, đơn vị sở hữu (owner / 오너) ai, thời gian tồn tại (lifetime / 수명) bao lâu, bản sao (copy / 복사) hay share, durability/freshness guarantee gì, và ai xóa/invalidate?

## Cross-references

Mục này bàn giao kiến thức sang các domain liên quan. Hãy theo từng liên kết để biết prerequisite nào đang được dùng, ứng dụng nào được mở rộng và ranh giới nào vẫn cần giữ.

- [Information/encoding](../00_computation_information/01_information_bits_and_encoding.md)
- [Memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md)
- [Virtual memory](../03_operating_systems/03_virtual_memory_and_address_spaces.md)
- [Filesystem durability](../03_operating_systems/04_filesystems_storage_and_io.md)
- [Database WAL](../05_data_databases/04_storage_logs_recovery_and_durability.md)
- [Replication](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md)

> **Bàn giao:** Sau **Cross-references**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 source code to cpu](./00_source_code_to_cpu.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
