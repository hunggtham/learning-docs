# Knowledge Connection — Vòng đời dữ liệu: register → RAM → disk → network

“Data” không phải một object đứng yên ở một chỗ. Trong lifetime của một request, cùng logical value có thể tồn tại dưới nhiều representations và copies: CPU register, cache line, heap object, kernel buffer, filesystem page, SSD block, database page, network packet và remote replica.

## Một value trong CPU

Suppose Java field `balance=1000`. Object reference leads to heap memory. CPU load virtual address; TLB translates; cache hierarchy returns line; relevant bytes enter register. Arithmetic updates register value; store marks cache line dirty.

At this point database/disk knows nothing about change.

## Runtime memory

Heap object representation includes fields/header/alignment. GC tracks reachability; object may move during compacting collection while semantic reference remains valid.

Application can serialize `1000` as JSON characters `1 0 0 0`, not same bytes as 64-bit binary integer.

Representation changed while meaning stayed.

## Kernel and socket buffers

`send()` copies or references bytes into kernel/network buffers depending API/zero-copy. TCP adds sequence state; TLS encrypts plaintext into ciphertext records; IP/link add headers. NIC DMA reads buffers and transmits symbols.

Remote machine reverses layers to reconstruct application bytes.

## Database buffer pool

DB parses numeric text/binary protocol into internal type. Row version stored in page in buffer pool. Commit may append WAL record first; data page remains dirty memory and flush later.

Thus logical “saved” can mean transaction durable via log even though table page not yet written.

## Filesystem and device

WAL write passes OS page cache or direct I/O, block layer, controller queue, device cache, flash translation layer. `fsync`/barriers establish ordering/durability assumptions.

SSD stores physical charge states unrelated to source-level integer layout.

## Replication

Primary ships WAL/logical change over network. Replica writes its own log/pages. At one moment primary committed but replica still stale if asynchronous.

Now one logical record has multiple versions/copies with different freshness.

## Cache copies

Application/Redis/CDN may cache derived representation. Invalidation message can lag/fail, so cache returns stale value. Cache consistency is data-lifecycle problem: copies need ownership/freshness rules.

## Copying vs referencing

Every boundary can copy or share. Copy isolates lifetime/mutation but costs bandwidth/memory. Shared memory/zero-copy reduces copy cost but complicates ownership, synchronization and pinning.

Serialization necessarily creates another representation; zero-copy cannot eliminate semantic transformation if protocols differ.

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

A system's “durable” contract chooses required stage(s). Acknowledging at process memory is very different from quorum stable storage.

## Data integrity

Checksums/CRC detect accidental corruption at layers; AEAD/MAC detect adversarial tampering; database constraints validate semantic integrity. Same word “integrity” spans different threat models.

## Data deletion

Deleting logical record may remove index/reference but copies survive in WAL, replica, cache, backup or SSD blocks until retention/GC/secure erase. Privacy/compliance deletion therefore needs full data-flow inventory.

## Mental Model

> Treat data as **a lineage of representations and copies**, not one variable. At every boundary ask: encoding gì, owner ai, lifetime bao lâu, copy hay share, durability/freshness guarantee gì, và ai xóa/invalidate?

## Cross-references

- [Information/encoding](../00_computation_information/01_information_bits_and_encoding.md)
- [Memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md)
- [Virtual memory](../03_operating_systems/03_virtual_memory_and_address_spaces.md)
- [Filesystem durability](../03_operating_systems/04_filesystems_storage_and_io.md)
- [Database WAL](../05_data_databases/04_storage_logs_recovery_and_durability.md)
- [Replication](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md)
