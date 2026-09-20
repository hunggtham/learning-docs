# LSM tree, compaction, Bloom filters và write amplification

B+Tree tối ưu cho in-place page-oriented indexing, nhưng random writes có thể gây nhiều small I/O. **LSM Tree — Log-Structured Merge Tree** đổi bài toán: ghi mới trước vào cấu trúc tuần tự nhanh, rồi merge/compact dữ liệu nền theo thời gian.

## Write path

Write thường vào **memtable** trong memory và được bảo vệ bởi WAL. Khi memtable đầy, nó được freeze rồi flush thành immutable sorted file, thường gọi SSTable.

Sequential flush thân thiện với storage hơn random page updates. Đổi lại một key có thể tồn tại ở nhiều files/levels, nên read path và background maintenance phức tạp hơn.

## Read amplification

Để tìm key, engine có thể phải kiểm tra memtable và nhiều SSTables. Index metadata và **Bloom filter** giúp loại nhanh files chắc chắn không chứa key.

Bloom filter có false positive nhưng không false negative: nó có thể nói “có thể có” khi thực tế không có, nhưng nếu nói “không có” thì engine bỏ file an toàn.

## Compaction

Compaction đọc nhiều sorted runs và merge thành runs mới, đồng thời loại overwritten versions/tombstones khi safe. Đây là quá trình trả “nợ tổ chức” phát sinh từ fast writes.

Nếu compaction không theo kịp ingest rate, số files tăng, read amplification và space amplification tăng. Vì vậy throughput write bền vững bị giới hạn bởi background compaction bandwidth chứ không chỉ tốc độ append ban đầu.

## Leveled và tiered compaction

Leveled compaction giữ overlap thấp ở các levels, tốt cho reads nhưng rewrite data nhiều hơn. Tiered/size-tiered gom nhiều runs cùng cỡ, giảm write amplification nhưng có thể tăng read/space amplification.

Không có strategy tốt tuyệt đối; read/write ratio, storage type và latency SLO quyết định.

## Write amplification

Một logical byte user ghi có thể được WAL append, flush rồi rewrite nhiều lần qua compactions. Tỷ lệ physical bytes/logical bytes là **write amplification**.

Trên SSD, amplification ảnh hưởng bandwidth và device endurance. Vì vậy storage-engine policy liên hệ trực tiếp hardware lifecycle.

## Tombstone

Delete trong LSM thường ghi tombstone thay vì tìm và xóa mọi old copy ngay. Tombstone phải sống đủ lâu để che versions cũ, rồi mới được compaction loại bỏ khi engine biết không còn cần.

Range tombstone và distributed replication làm lifecycle này phức tạp hơn.

## LSM và B+Tree

B+Tree trả cost ngay khi update page; LSM trì hoãn organization sang background. Có thể xem đây là khác biệt giữa eager maintenance và deferred batch maintenance.

Xem thêm: [B+Tree internals](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md).

## Mental Model

> LSM Tree biến random mutation thành append + merge. Fast foreground write không miễn phí; chi phí được chuyển sang read amplification, space và compaction. Muốn đánh giá engine phải tính toàn lifecycle của byte dữ liệu, không chỉ latency của lệnh PUT.