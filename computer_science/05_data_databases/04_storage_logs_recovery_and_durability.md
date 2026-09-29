# Lưu trữ (storage / 저장소) engine, WAL, khôi phục (recovery / 복구) và durability

> **Mạch đọc:** Đặt **lưu trữ (storage / 저장소) engine, WAL, khôi phục (recovery / 복구) và durability** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Pages là đơn vị quản lý** sang **Buffer pool**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một giao dịch (transaction / 트랜잭션) lần ghi nhận (commit / 커밋) cần biến logical thay đổi (change / 변경) thành bytes trên lưu trữ (storage / 저장소) sao cho crash ở bất kỳ thời điểm nào vẫn recover được trạng thái (state / 상태) hợp lệ. lưu trữ (storage / 저장소) engine giải vấn đề bằng pages, buffers, logs, checksums và khôi phục (recovery / 복구) protocols.

## Pages là đơn vị quản lý

Cơ sở dữ liệu (database / 데이터베이스) thường quản lý fixed-size pages/blocks chứa rows/chỉ mục (index / 인덱스) nodes/siêu dữ liệu (metadata / 메타데이터). Buffer pool bộ nhớ đệm (cache / 캐시) pages trong RAM. truy vấn (query / 쿼리) operator yêu cầu logical row; lưu trữ (storage / 저장소) tầng (layer / 계층) pin/fetch page, parse slots/records.

Page kích thước (size / 크기) cân bằng siêu dữ liệu (metadata / 메타데이터), I/O granularity và fragmentation. Large sequential scans khác random OLTP lookups.


> **Chuyển mạch:** Từ **Pages là đơn vị quản lý**, ta sang **Buffer pool** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Buffer pool

Buffer pool giảm thiết bị (device / 장치) I/O bằng caching pages. Dirty page đã modified nhưng chưa flushed. Eviction chính sách (policy / 정책) approximates working-set giá trị (value / 값), nhưng DB còn phải cân nhắc dirty flush và scan pollution.

Cơ sở dữ liệu (database / 데이터베이스) bộ nhớ đệm (cache / 캐시) và OS page bộ nhớ đệm (cache / 캐시) có thể double-cache tùy I/O chế độ (mode / 모드).


> **Chuyển mạch:** Từ **Buffer pool**, ta sang **Write-Ahead Logging** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Write-Ahead Logging

WAL (Write-Ahead Log / 미리 쓰기 로그, 선행 기록 로그) principle: log bản ghi (record / 레코드) mô tả thay đổi (change / 변경) phải đạt durable lưu trữ (storage / 저장소) trước dữ liệu (data / 데이터) page chứa thay đổi (change / 변경) được coi durable/allowed flush theo giao thức (protocol / 프로토콜).

Tại lần ghi nhận (commit / 커밋), hệ thống (system / 시스템) thường cần ensure relevant log records + lần ghi nhận (commit / 커밋) marker durable, không nhất thiết flush all dữ liệu (data / 데이터) pages. Sequential log ghi (write / 쓰기) rẻ hơn random page flush; background checkpoint sau đó ghi (write / 쓰기) dirty pages.


> **Chuyển mạch:** Từ **Write-Ahead Logging**, ta sang **REDO và UNDO** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## REDO và UNDO

Khôi phục (recovery / 복구) sau crash phân tích log để redo committed changes chưa lên dữ liệu (data / 데이터) pages và/hoặc undo uncommitted changes tùy thuật toán (algorithm / 알고리즘). ARIES-style khôi phục (recovery / 복구) dùng WAL + LSN + physiological logging, nhưng engines vary.

MVCC engines có additional phiên bản (version / 버전)/undo mechanisms. mô hình tư duy (mental model / 사고 모델) quan trọng hơn sản phẩm (product / 제품) details: log cung cấp lịch sử (history / 이력) đủ để reconstruct consistent durable trạng thái (state / 상태).


> **Chuyển mạch:** Từ **REDO và UNDO**, ta sang **Checkpoint** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Checkpoint

Không thể replay log từ ngày đầu. Checkpoint ghi siêu dữ liệu (metadata / 메타데이터)/flush trạng thái (state / 상태) để giới hạn khôi phục (recovery / 복구) công việc (work / 작업), nhưng checkpoint quá aggressive tăng I/O. It is not necessarily “bản sao (copy / 복사) whole DB”.


> **Chuyển mạch:** Từ **Checkpoint**, ta sang **Torn writes và checksums** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Torn writes và checksums

Power mất mát (loss / 손실) có thể leave partial page writes tùy thiết bị (device / 장치) guarantees. Page checksums detect corruption. Doublewrite buffer, full-page images, sao chép khi ghi (copy-on-write / 쓰기 시 복사) hoặc atomic-sector các giả định (assumptions / 가정들) mitigate torn pages.

Durability chuỗi (chain / 사슬) đi qua DB → filesystem → kernel bộ nhớ đệm (cache / 캐시) → thiết bị (device / 장치) controller → flash media. Mỗi tầng (layer / 계층) phải respect flush/barrier ngữ nghĩa (semantics / 의미론).


> **Chuyển mạch:** Từ **Torn writes và checksums**, ta sang **WAL khác replication log** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## WAL khác replication log

Cục bộ (local / 로컬) WAL phục vụ crash khôi phục (recovery / 복구)/durability. Replication có thể stream WAL/binlog/oplog tới replicas. Nhưng replication acknowledgements chính sách (policy / 정책) quyết định lần ghi nhận (commit / 커밋) durability across nút (node / 노드) mất mát (loss / 손실).

Async replica có lag; synchronous quorum tăng độ trễ (latency / 지연 시간) nhưng durability/consistency mạnh hơn tùy giao thức (protocol / 프로토콜).


> **Chuyển mạch:** Từ **WAL khác replication log**, ta sang **LSM cây (tree / 트리) intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## LSM cây (tree / 트리) intuition

Log-Structured Merge cây (tree / 트리) tối ưu ghi (write / 쓰기) thông lượng (throughput / 처리량) bằng append/memtable rồi flush sorted SSTables, background compaction merge levels. Reads có thể cần consult multiple files nhưng Bloom filters/indexes giúp.

B-tree cập nhật (update / 업데이트) in-place pages; LSM chuyển random writes thành sequential writes nhưng chịu compaction/ghi (write / 쓰기) amplification. lưu trữ (storage / 저장소) tải công việc (workload / 워크로드) quyết định.


> **Chuyển mạch:** Từ **LSM cây (tree / 트리) intuition**, ta sang **Backup khác replication** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Backup khác replication

Replica có thể faithfully replicate accidental DELETE; nó không thay backup. Backup needs point-in-time/lịch sử (history / 이력)/independent miền lỗi (failure domain / 장애 도메인). WAL archiving + cơ sở (base / 기반) backup có thể hỗ trợ (support / 지원) point-in-time khôi phục (recovery / 복구).


> **Chuyển mạch:** Từ **Backup khác replication**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Durability không phải “ghi tệp (file / 파일)”. Nó là **giao thức (protocol / 프로토콜) về thứ tự (ordering / 순서)**: log lịch sử (history / 이력) phải bền trước khi dữ liệu (data / 데이터) pages được phép lag; khôi phục (recovery / 복구) dùng lịch sử (history / 이력) đó để biến crash-time partial writes thành committed trạng thái (state / 상태).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“lần ghi nhận (commit / 커밋) phải flush mọi changed page.”** WAL cho phép lần ghi nhận (commit / 커밋) bằng durable log trước, dữ liệu (data / 데이터) pages flush sau.

**“Replica = backup.”** Replica bảo availability/read scaling; logical corruption có thể replicate ngay.

**“SSD không cần WAL vì nhanh.”** WAL là tính đúng đắn (correctness / 정확성)/khôi phục (recovery / 복구) cơ chế (mechanism / 메커니즘), không chỉ hiệu năng (performance / 성능) workaround.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

[Filesystem durability](../03_operating_systems/04_filesystems_storage_and_io.md) là lower tầng (layer / 계층); [transactions](./02_transactions_acid_and_concurrency_control.md) là user-visible đặc tả hợp đồng (contract / 계약); [replication/consensus](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) mở durability từ một machine sang cluster.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 data models and database systems](./00_data_models_and_database_systems.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
