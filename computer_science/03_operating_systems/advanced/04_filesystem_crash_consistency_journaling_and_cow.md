# Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán ban đầu: một thao tác (operation / 연산) lô-gic (logic / 논리) gồm nhiều writes vật lý** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Atomicity, visibility và durability là ba thuộc tính (property / 속성) khác nhau** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Filesystem phải biến một chuỗi writes có thể bị ngắt ở **bất kỳ điểm nào** thành trạng thái sau reboot vẫn hợp lệ hoặc ít nhất có thể khôi phục (recovery / 복구) một cách xác định. Vấn đề khó không nằm ở việc “ghi bytes xuống disk”, mà ở việc một thao tác lô-gic (logic / 논리) thường tạo nhiều updates vật lý: directory entry, inode, allocation bitmap/cây (tree / 트리), dữ liệu (data / 데이터) blocks, journal siêu dữ liệu (metadata / 메타데이터) và bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태).

Mô hình tư duy (mental model / 사고 모델) trung tâm của chương này là: **crash consistency là một giao thức (protocol / 프로토콜) thứ tự (ordering / 순서)**. Mỗi tối ưu hóa (optimization / 최적화) được phép đổi timing và batching, nhưng không được làm xuất hiện một on-disk trạng thái (state / 상태) mà khôi phục (recovery / 복구) giao thức (protocol / 프로토콜) không giải thích được.

## 1. Bài toán ban đầu: một thao tác (operation / 연산) lô-gic (logic / 논리) gồm nhiều writes vật lý

Tạo hoặc thay thế một tệp (file / 파일) có thể cần:

```text
allocate inode
allocate data block
write data
link block vào inode
insert directory entry
update free-space metadata
```

Nếu power mất mát (loss / 손실) xảy ra sau bất kỳ bước nào, filesystem phải tránh các trạng thái như directory trỏ tới inode chưa hợp lệ, một khối (block / 블록) vừa được dùng vừa còn nằm trong free danh sách (list / 목록), hoặc siêu dữ liệu (metadata / 메타데이터) nói tệp (file / 파일) dài hơn số dữ liệu (data / 데이터) khối (block / 블록) thực sự tồn tại.

**Crash consistency** hỏi:

> Với mọi crash điểm (point / 지점) nằm trong thất bại (failure / 실패) mô hình (model / 모델), on-disk trạng thái (state / 상태) sau reboot có thuộc tập trạng thái mà khôi phục (recovery / 복구) có thể đưa về một filesystem hợp lệ không?

Đây là bất biến (invariant / 불변식) mạnh hơn “ghi (write / 쓰기) thường hoàn tất”.

> **Chuyển mạch:** Trong **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **2. Atomicity, visibility và durability là ba thuộc tính (property / 속성) khác nhau** tiếp nhận điểm tựa từ **1. Bài toán ban đầu: một thao tác (operation / 연산) lô-gic (logic / 논리) gồm nhiều writes vật lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Page bộ nhớ đệm (cache / 캐시) làm write() chưa đồng nghĩa persistence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Atomicity, visibility và durability là ba thuộc tính (property / 속성) khác nhau

Một rename có thể atomic về **visibility**: observer thấy tên cũ hoặc tên mới, không thấy trạng thái nửa đổi tên. Nhưng điều đó không tự động nghĩa rename đã **durable** qua power mất mát (loss / 손실).

Tương tự, `write()` có thể trả success vì kernel đã bản sao (copy / 복사) bytes vào page bộ nhớ đệm (cache / 캐시). Nó không chứng minh bytes đã tới non-volatile media.

Khi lập luận (reasoning / 추론), luôn tách:

```text
atomicity  : observer có thấy partial logical update không?
visibility : process khác được phép thấy state nào?
durability : state nào sống sót failure đã công bố?
```

Một API có thể mạnh ở một trục và yếu ở trục khác.

> **Chuyển mạch:** Ở chặng này của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **3. Page bộ nhớ đệm (cache / 캐시) làm write() chưa đồng nghĩa persistence** tiếp nhận điểm tựa từ **2. Atomicity, visibility và durability là ba thuộc tính (property / 속성) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. bất biến (invariant / 불변식) ghi (write / 쓰기) thứ tự (ordering / 순서): pointer không được durable trước đối tượng (object / 객체) nó làm reachable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Page bộ nhớ đệm (cache / 캐시) làm `write()` chưa đồng nghĩa persistence

Với buffered I/O, ứng dụng (application / 애플리케이션) thường đi qua:

```text
user buffer
→ write()/pwrite()
→ kernel page cache: page trở thành dirty
→ writeback
→ filesystem/block layer
→ device queue/cache
→ non-volatile media
```

`write()` return thường chỉ chứng minh kernel đã nhận dữ liệu (data / 데이터). Dirty page có thể được flush vài giây sau hoặc sớm hơn vì bộ nhớ (memory / 메모리) pressure.

Thành phần nguyên thủy (primitive / 기본 요소) như `fsync()`/`fdatasync()` yêu cầu durability mạnh hơn, nhưng chính xác (exact / 정확한) đặc tả hợp đồng (contract / 계약) vẫn phụ thuộc filesystem và thiết bị (device / 장치) ngăn xếp (stack / 스택). cơ sở dữ liệu (database / 데이터베이스) WAL dựa mạnh vào ranh giới (boundary / 경계) này, nên “OS sẽ tự flush sớm thôi” không phải tính đúng đắn (correctness / 정확성) argument.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **4. bất biến (invariant / 불변식) ghi (write / 쓰기) thứ tự (ordering / 순서): pointer không được durable trước đối tượng (object / 객체) nó làm reachable** tiếp nhận điểm tựa từ **3. Page bộ nhớ đệm (cache / 캐시) làm write() chưa đồng nghĩa persistence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Journaling biến arbitrary cập nhật (update / 업데이트) thành một log giao thức (protocol / 프로토콜) có ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. bất biến (invariant / 불변식) ghi (write / 쓰기) thứ tự (ordering / 순서): pointer không được durable trước đối tượng (object / 객체) nó làm reachable

Một mẫu (pattern / 패턴) chung của crash-safe cấu trúc (structure / 구조) là tránh làm một đối tượng (object / 객체) mới **reachable** trước khi đối tượng (object / 객체) đó đủ hợp lệ.

Ví dụ simplified:

```text
1. ghi block data mới
2. đảm bảo block đủ persistent theo protocol
3. cập nhật metadata/pointer để file trỏ tới block mới
4. đảm bảo metadata durable
```

Nếu step 3 durable trước step 1, khôi phục (recovery / 복구) có thể thấy pointer tới garbage hoặc incomplete content.

Filesystem journaling, sao chép khi ghi (copy-on-write / 쓰기 시 복사) cây (tree / 트리) và cơ sở dữ liệu (database / 데이터베이스) WAL dùng hiện thực (implementation / 구현) khác nhau nhưng cùng family bất biến (invariant / 불변식): **publication siêu dữ liệu (metadata / 메타데이터) không được vượt quá trạng thái (state / 상태) mà khôi phục (recovery / 복구) dựa vào**.

> **Chuyển mạch:** Trong **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **4. bất biến (invariant / 불변식) ghi (write / 쓰기) thứ tự (ordering / 순서): pointer không được durable trước đối tượng (object / 객체) nó làm reachable** đã nêu tiêu chí phân biệt, còn **5. Journaling biến arbitrary cập nhật (update / 업데이트) thành một log giao thức (protocol / 프로토콜) có ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **6. siêu dữ liệu (metadata / 메타데이터) journaling và dữ liệu (data / 데이터) journaling bảo vệ những thứ khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Journaling biến arbitrary cập nhật (update / 업데이트) thành một log giao thức (protocol / 프로토콜) có ranh giới (boundary / 경계)

Journaling ghi giao dịch (transaction / 트랜잭션) siêu dữ liệu (metadata / 메타데이터) hoặc copies/descriptions của updates vào journal trước khi áp dụng chúng vào home locations. khôi phục (recovery / 복구) sau crash không cần đoán toàn filesystem; nó xác định journal giao dịch (transaction / 트랜잭션) nào đủ lần ghi nhận (commit / 커밋) ranh giới (boundary / 경계) để replay hoặc giao dịch (transaction / 트랜잭션) nào phải bỏ.

Simplified máy trạng thái (state machine / 상태 머신):

```text
prepare journal records
→ write records
→ persist required journal content
→ persist commit marker / transaction boundary
→ checkpoint/apply updates to home locations
→ reclaim journal space
```

Bất biến (invariant / 불변식) không phải “home blocks luôn mới nhất”. bất biến (invariant / 불변식) là **journal + home trạng thái (state / 상태) luôn đủ để khôi phục (recovery / 복구) một lịch sử (history / 이력) hợp lệ**.

> **Chuyển mạch:** Ở chặng này của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **5. Journaling biến arbitrary cập nhật (update / 업데이트) thành một log giao thức (protocol / 프로토콜) có ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **6. siêu dữ liệu (metadata / 메타데이터) journaling và dữ liệu (data / 데이터) journaling bảo vệ những thứ khác nhau** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **7. Barriers, flush và FUA: thứ tự (ordering / 순서) phải sống xuống thiết bị (device / 장치)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. siêu dữ liệu (metadata / 메타데이터) journaling và dữ liệu (data / 데이터) journaling bảo vệ những thứ khác nhau

Siêu dữ liệu (metadata / 메타데이터) journaling chủ yếu bảo vệ filesystem cấu trúc (structure / 구조). người dùng (user / 사용자) dữ liệu (data / 데이터) có thể được ghi (write / 쓰기) theo chính sách (policy / 정책) khác, nên sau crash cấu trúc (structure / 구조) vẫn valid nhưng tệp (file / 파일) content mới nhất chưa chắc đúng như ứng dụng (application / 애플리케이션) tưởng nếu ứng dụng (application / 애플리케이션) không dùng durability giao thức (protocol / 프로토콜) thích hợp.

Dữ liệu (data / 데이터) journaling có thể log cả người dùng (user / 사용자) dữ liệu (data / 데이터), tăng guarantee nhưng cũng tăng ghi (write / 쓰기) amplification và bandwidth chi phí (cost / 비용).

Do đó câu “filesystem có journal nên không mất dữ liệu (data / 데이터)” quá mạnh. Phải hỏi journal chế độ (mode / 모드) và ứng dụng (application / 애플리케이션) đã đặt durability ranh giới (boundary / 경계) ở đâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **6. siêu dữ liệu (metadata / 메타데이터) journaling và dữ liệu (data / 데이터) journaling bảo vệ những thứ khác nhau** nêu điều cần giải thích; **7. Barriers, flush và FUA: thứ tự (ordering / 순서) phải sống xuống thiết bị (device / 장치)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. Torn ghi (write / 쓰기) và atomic ghi (write / 쓰기) granularity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Barriers, flush và FUA: thứ tự (ordering / 순서) phải sống xuống thiết bị (device / 장치)

Filesystem có thể phát writes theo đúng thứ tự lô-gic (logic / 논리) nhưng lưu trữ (storage / 저장소) ngăn xếp (stack / 스택)/thiết bị (device / 장치) vẫn có hàng đợi (queue / 큐) và volatile ghi (write / 쓰기) bộ nhớ đệm (cache / 캐시). Nếu thiết bị (device / 장치) reorder hoặc báo completion trước khi dữ liệu (data / 데이터) an toàn mà không tôn trọng flush/FUA ngữ nghĩa (semantics / 의미론), upper-layer giao thức (protocol / 프로토콜) có thể bị phá.

Chuỗi nhân quả (causal chain / 인과 사슬):

```text
filesystem wants A before B
→ block layer schedules requests
→ controller/device caches them
→ power loss
```

Tính đúng đắn (correctness / 정확성) yêu cầu thứ tự (ordering / 순서) intent phải được truyền đủ qua các tầng (layer / 계층) nằm trong đặc tả hợp đồng (contract / 계약). Một filesystem thuật toán (algorithm / 알고리즘) đúng không cứu được thiết bị (device / 장치)/firmware vi phạm persistence guarantee mà upper tầng (layer / 계층) dựa vào.

> **Chuyển mạch:** Trong **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **8. Torn ghi (write / 쓰기) và atomic ghi (write / 쓰기) granularity** tiếp nhận điểm tựa từ **7. Barriers, flush và FUA: thứ tự (ordering / 순서) phải sống xuống thiết bị (device / 장치)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. sao chép khi ghi (copy-on-write / 쓰기 시 복사): publish gốc (root / 루트) sau khi subtree mới đã tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Torn ghi (write / 쓰기) và atomic ghi (write / 쓰기) granularity

Một filesystem khối (block / 블록) hoặc cơ sở dữ liệu (database / 데이터베이스) page có thể lớn hơn atomic persistence granularity của lưu trữ (storage / 저장소). Power mất mát (loss / 손실) giữa ghi (write / 쓰기) có thể tạo **ghi rách (torn write)**: một phần old, một phần new.

Checksum giúp **detect** corruption nhưng không tự recover. khôi phục (recovery / 복구) cần redundant siêu dữ liệu (metadata / 메타데이터), journal redo, sao chép khi ghi (copy-on-write / 쓰기 시 복사) phiên bản (version / 버전) cũ, mirrored siêu dữ liệu (metadata / 메타데이터) hoặc cơ chế (mechanism / 메커니즘) tương đương tùy filesystem.

Vì vậy bất biến (invariant / 불변식) thường không phải “khối (block / 블록) ghi (write / 쓰기) là atomic”; bất biến (invariant / 불변식) là **partial vật lý (physical / 물리적) cập nhật (update / 업데이트) không được âm thầm trở thành logical trạng thái (state / 상태) được tin là hoàn chỉnh**.

> **Chuyển mạch:** Ở chặng này của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **9. sao chép khi ghi (copy-on-write / 쓰기 시 복사): publish gốc (root / 루트) sau khi subtree mới đã tồn tại** tiếp nhận điểm tựa từ **8. Torn ghi (write / 쓰기) và atomic ghi (write / 쓰기) granularity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Rename-based replace: atomic không gian tên (namespace / 네임스페이스) thay đổi (change / 변경) chưa đủ cho durable replace** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. sao chép khi ghi (copy-on-write / 쓰기 시 복사): publish gốc (root / 루트) sau khi subtree mới đã tồn tại

Sao chép khi ghi (copy-on-write / 쓰기 시 복사) filesystem không overwrite cấu trúc (structure / 구조) đang live. Nó tạo blocks/nodes mới, cập nhật ancestors mới, rồi cuối cùng chuyển gốc (root / 루트)/tham chiếu (reference / 참조) tới phiên bản (version / 버전) mới.

Simplified:

```text
old root -> old subtree

write new leaf
→ write new parent
→ ...
→ atomically/safely publish new root
```

Nếu crash trước gốc (root / 루트) publication, old cây (tree / 트리) vẫn authoritative. Nếu crash sau publication ranh giới (boundary / 경계), new cây (tree / 트리) phải đủ complete theo giao thức (protocol / 프로토콜).

COW làm snapshot tự nhiên vì old blocks vẫn còn reachable từ old roots, nhưng trả chi phí (cost / 비용) bằng fragmentation, siêu dữ liệu (metadata / 메타데이터) churn và ghi (write / 쓰기) amplification.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **10. Rename-based replace: atomic không gian tên (namespace / 네임스페이스) thay đổi (change / 변경) chưa đủ cho durable replace** tiếp nhận điểm tựa từ **9. sao chép khi ghi (copy-on-write / 쓰기 시 복사): publish gốc (root / 루트) sau khi subtree mới đã tồn tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Writeback lan truyền lỗi (error propagation / 오류 전파) cũng là một tính đúng đắn (correctness / 정확성) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Rename-based replace: atomic không gian tên (namespace / 네임스페이스) thay đổi (change / 변경) chưa đủ cho durable replace

Mẫu (pattern / 패턴) phổ biến:

```text
write temp file
→ fsync(temp)
→ rename(temp, target)
→ fsync(parent directory)   // khi contract/filesystem yêu cầu để persist directory entry
```

Chi tiết chính xác (exact / 정확한) phụ thuộc nền tảng (platform / 플랫폼)/filesystem, nhưng mô hình tư duy (mental model / 사고 모델) phải nhận ra **tệp (file / 파일) dữ liệu (data / 데이터)** và **directory siêu dữ liệu (metadata / 메타데이터)** là hai durability objects khác nhau.

Nếu chỉ fsync tệp (file / 파일) rồi rename nhưng crash trước directory cập nhật (update / 업데이트) durable, sau reboot tên mới có thể không tồn tại theo đặc tả hợp đồng (contract / 계약). “Rename atomic” chỉ trả lời visibility của không gian tên (namespace / 네임스페이스) chuyển tiếp (transition / 전이), không tự trả lời toàn bộ power-failure durability.

> **Chuyển mạch:** Trong **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **11. Writeback lan truyền lỗi (error propagation / 오류 전파) cũng là một tính đúng đắn (correctness / 정확성) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **10. Rename-based replace: atomic không gian tên (namespace / 네임스페이스) thay đổi (change / 변경) chưa đủ cho durable replace** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Dirty-page pressure làm timing thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Writeback lan truyền lỗi (error propagation / 오류 전파) cũng là một tính đúng đắn (correctness / 정확성) bài toán (problem / 문제)

Buffered ghi (write / 쓰기) có thể return trước khi actual thiết bị (device / 장치) ghi (write / 쓰기) xảy ra. Lỗi I/O có thể xuất hiện ở writeback sau đó. ứng dụng (application / 애플리케이션) cần hiểu API nào báo asynchronous writeback errors và điểm nào nó kiểm tra/propagate thất bại (failure / 실패).

Nếu hệ thống (system / 시스템) log “save successful” trước durability ranh giới (boundary / 경계), nghiệp vụ (business / 비즈니스) acknowledgement có thể mạnh hơn lưu trữ (storage / 저장소) trạng thái (state / 상태) thật. Đây là cùng bất biến (invariant / 불변식) với cơ sở dữ liệu (database / 데이터베이스) lần ghi nhận (commit / 커밋): **acknowledgement không được mạnh hơn bằng chứng (evidence / 증거) đã đạt**.

> **Chuyển mạch:** Ở chặng này của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **12. Dirty-page pressure làm timing thay đổi** tiếp nhận điểm tựa từ **11. Writeback lan truyền lỗi (error propagation / 오류 전파) cũng là một tính đúng đắn (correctness / 정확성) bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Journaling/COW có background công việc (work / 작업) và amplification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Dirty-page pressure làm timing thay đổi

Ở low tải (load / 로드), dirty pages có thể flush nền trơn tru. Khi ghi (write / 쓰기) tỷ lệ (rate / 비율) tăng, dirty set lớn dần, background writer và reclaim bắt đầu cạnh tranh bandwidth. Tới một threshold, foreground writer có thể bị throttle hoặc chờ writeback.

Nhân quả (causal / 인과적) vòng lặp (loop / 루프):

```text
write rate ↑
→ dirty pages ↑
→ writeback queue ↑
→ device utilization/latency ↑
→ foreground fsync latency ↑
→ request queue ↑
```

Vì vậy lưu trữ (storage / 저장소) sự cố (incident / 인시던트) có thể xuất hiện ở API p99 dù CPU thấp. Lower tầng (layer / 계층) thực sự quyết định hành vi (behavior / 동작) là dirty writeback + thiết bị (device / 장치) hàng đợi (queue / 큐), không phải ứng dụng (application / 애플리케이션) handler.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **13. Journaling/COW có background công việc (work / 작업) và amplification** tiếp nhận điểm tựa từ **12. Dirty-page pressure làm timing thay đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. cơ sở dữ liệu (database / 데이터베이스) WAL và filesystem journal là hai protocols xếp chồng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Journaling/COW có background công việc (work / 작업) và amplification

Journal checkpointing, COW siêu dữ liệu (metadata / 메타데이터) rewrite, snapshot retention, filesystem cleaning/defragmentation hoặc thiết bị (device / 장치) garbage collection có thể cạnh tranh với foreground I/O.

Tối ưu hóa (optimization / 최적화) tạo thông lượng (throughput / 처리량) tốt ở steady trạng thái (state / 상태) có thể tạo độ trễ (latency / 지연 시간) burst khi background debt được trả. môi trường vận hành (production / 운영 환경) benchmark cần chạy đủ lâu để quan sát maintenance cycle, không chỉ đo vài giây warm bộ nhớ đệm (cache / 캐시).

> **Chuyển mạch:** Trong **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **13. Journaling/COW có background công việc (work / 작업) và amplification** nêu điều cần giải thích; **14. cơ sở dữ liệu (database / 데이터베이스) WAL và filesystem journal là hai protocols xếp chồng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. thất bại (failure / 실패) injection là cách kiểm tra crash bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. cơ sở dữ liệu (database / 데이터베이스) WAL và filesystem journal là hai protocols xếp chồng

Cơ sở dữ liệu (database / 데이터베이스) WAL bảo vệ giao dịch (transaction / 트랜잭션)/khôi phục (recovery / 복구) ngữ nghĩa (semantics / 의미론) của cơ sở dữ liệu (database / 데이터베이스). Filesystem journal/COW bảo vệ filesystem siêu dữ liệu (metadata / 메타데이터)/data-structure consistency.

```text
application transaction
→ database WAL/buffer pool
→ file I/O durability primitive
→ filesystem journal/COW
→ block/device persistence
```

Hai logs không duplicate cùng bất biến (invariant / 불변식). DB vẫn cần WAL vì filesystem không biết giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) của nhiều cơ sở dữ liệu (database / 데이터베이스) pages; filesystem vẫn cần crash-consistency vì DB tệp (file / 파일) blocks tồn tại trong filesystem không gian tên (namespace / 네임스페이스)/siêu dữ liệu (metadata / 메타데이터) của nó.

Đọc [MVCC, WAL và recovery internals](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md) và [durability path xuyên tầng](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Chuyển mạch:** Ở chặng này của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **14. cơ sở dữ liệu (database / 데이터베이스) WAL và filesystem journal là hai protocols xếp chồng** nêu điều cần giải thích; **15. thất bại (failure / 실패) injection là cách kiểm tra crash bất biến (invariant / 불변식)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. thất bại (failure / 실패) injection là cách kiểm tra crash bất biến (invariant / 불변식)

Happy-path tests không chứng minh crash consistency. kiểm thử (test / 테스트) tốt cần cắt thực thi (execution / 실행) ở các ranh giới (boundary / 경계) có ý nghĩa:

```text
crash trước journal commit
crash sau commit marker nhưng trước home write
crash giữa COW subtree và root publication
kill process trước/sau fsync
inject write error / short write khi harness cho phép
replay recovery nhiều lần
```

Sau mỗi thất bại (failure / 실패), kiểm tra filesystem mount/khôi phục (recovery / 복구) thành công, không gian tên (namespace / 네임스페이스) không chứa impossible trạng thái (state / 상태), dữ liệu (data / 데이터) được giữ đúng theo durability đặc tả hợp đồng (contract / 계약), và khôi phục (recovery / 복구) idempotent.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **15. thất bại (failure / 실패) injection là cách kiểm tra crash bất biến (invariant / 불변식)** nêu điều cần giải thích; **16. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) hữu ích gồm:

```text
application: fsync/fdatasync latency, write error/ack timing
OS: dirty pages, writeback rate, reclaim/throttling, I/O wait
filesystem: journal/checkpoint activity, filesystem errors, free-space/fragmentation pressure
block/device: latency distribution, queue depth, utilization, flush latency, error counters
```

Một đồ thị (graph / 그래프) “disk utilization 70%” không đủ. Cần nối yêu cầu (request / 요청)/giao dịch (transaction / 트랜잭션) độ trễ (latency / 지연 시간) với writeback/flush hàng đợi (queue / 큐) và background công việc (work / 작업) để chứng minh cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Trong **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **16. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **17. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?

Nếu symptom là tệp (file / 파일) biến mất sau reboot, bắt đầu từ ứng dụng (application / 애플리케이션) durability giao thức (protocol / 프로토콜) rồi xuống rename/directory/fsync ngữ nghĩa (semantics / 의미론). Nếu filesystem cấu trúc (structure / 구조) corrupt, kiểm tra journal/COW khôi phục (recovery / 복구) đường dẫn (path / 경로) và lưu trữ (storage / 저장소) errors. Nếu tính đúng đắn (correctness / 정확성) ổn nhưng p99 spike, kiểm tra dirty/writeback/hàng đợi (queue / 큐)/background maintenance.

Không cần học mọi filesystem hiện thực (implementation / 구현) để lập luận (reasoning / 추론). Cần xác định **publication điểm (point / 지점), persistence ranh giới (boundary / 경계), khôi phục (recovery / 복구) siêu dữ liệu (metadata / 메타데이터) và thất bại (failure / 실패) mô hình (model / 모델)** của hiện thực (implementation / 구현) đang dùng.

> **Chuyển mạch:** Ở chặng này của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **18. Mô hình tư duy** gom các mảnh từ **17. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Mô hình tư duy

> Filesystem crash consistency là một state-transition giao thức (protocol / 프로토콜) dưới khả năng interruption tùy ý. `write()` tạo dirty trạng thái (state / 상태); journaling/COW tạo khôi phục (recovery / 복구) cấu trúc (structure / 구조); barriers/flush đưa thứ tự (ordering / 순서) intent xuống lưu trữ (storage / 저장소); khôi phục (recovery / 복구) chọn lịch sử (history / 이력) hợp lệ sau crash. **Atomic visibility không tự bằng durability, và acknowledgement chỉ an toàn khi tầng dưới đã đạt persistence đặc tả hợp đồng (contract / 계약) mà tầng trên đang hứa.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Filesystem crash consistency, journaling và sao chép khi ghi (copy-on-write / 쓰기 시 복사)**, **Kết nối** gom các mảnh từ **18. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ôn [filesystem foundation](../../basic/03_operating_systems/04_filesystems_storage_and_io.md), [storage hardware](../../basic/02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md), [MVCC/WAL](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md), [buffer pool](../../05_data_databases/advanced/04_buffer_pool_replacement_and_dirty_page_management.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
