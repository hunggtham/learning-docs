# 06 — phân tán (distributed / 분산) processing: partition, shuffle, skew và spill

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **06 — phân tán (distributed / 분산) processing: partition, shuffle, skew và spill**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. thực thi (execution / 실행) đồ thị (graph / 그래프)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Partition** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của distributed processing, rồi nối partition, coordination, consistency và failure thành một pipeline có thể đo.

Phân tán (distributed / 분산) processing không chỉ là chạy cùng một hàm (function / 함수) trên nhiều máy. Hệ thống phải chia đầu vào (input / 입력), di chuyển dữ liệu giữa worker, giữ thứ tự (ordering / 순서)/aggregation ngữ nghĩa (semantics / 의미론) và phục hồi khi một phần computation thất bại.

## 1. thực thi (execution / 실행) đồ thị (graph / 그래프)

Một job thường có các stage nối bằng ranh giới (boundary / 경계):

```text
read → map/filter → repartition → join/aggregate → write
```

Thao tác (operation / 연산) giữ bản ghi (record / 레코드) ở cùng partition thường rẻ hơn thao tác (operation / 연산) cần đưa các bản ghi (record / 레코드) cùng key về một nơi. ranh giới (boundary / 경계) đó thường là shuffle. Khi rà soát (review / 검토) một job, hãy đánh dấu byte đi qua mạng (network / 네트워크), không chỉ số dòng trong mã (code / 코드).

> **Chuyển mạch:** **Execution graph** xác định dependency và stage; **Partition** chia dữ liệu theo key, rồi **Shuffle** mô tả dữ liệu di chuyển giữa các stage.

## 2. Partition

Partition là đơn vị phân phối công việc (work / 작업) và thường là đơn vị thất bại (failure / 실패)/thử lại (retry / 재시도). Key tốt cần đủ phân tán, ổn định và phù hợp với thao tác (operation / 연산) downstream. Partition theo một key có cardinality thấp tạo hotspot; partition theo key quá ngẫu nhiên làm mất locality và tăng shuffle.

Partition count phải tương xứng với đầu vào (input / 입력) kích thước (size / 크기), worker parallelism và overhead scheduling. Quá ít partition tạo tác vụ (task / 작업) dài; quá nhiều tạo tác vụ (task / 작업) nhỏ, siêu dữ liệu (metadata / 메타데이터) và scheduling overhead.

> **Chuyển mạch:** **Shuffle** tạo network và disk movement từ partition; **Skew** kiểm tra khi phân bố key làm một số task nặng hơn phần còn lại.

## 3. Shuffle

Shuffle xảy ra khi bản ghi (record / 레코드) phải đi tới partition mới theo key/phạm vi (range / 범위). Chi phí gồm serialize, mạng (network / 네트워크) transfer, buffer, disk spill và merge. phép nối (join / 조인), group-by và toàn cục (global / 전역) sort thường là shuffle ranh giới (boundary / 경계).

Một truy vấn (query / 쿼리) có ít đầu ra (output / 출력) vẫn có thể shuffle nhiều TB. Predicate pushdown trước shuffle, pre-aggregation và projection sớm giảm byte di chuyển. Không được đo hiệu năng (performance / 성능) chỉ bằng đầu ra (output / 출력) kích thước (size / 크기).

> **Chuyển mạch:** **Skew** tập trung tải vào một số task; **Spill và memory pressure** giải thích lúc buffer vượt capacity và chuyển xuống disk.

## 4. Skew

Skew là khi phân phối key không đều: một customer lớn, một ngày lỗi, hoặc `null` gom phần lớn bản ghi (record / 레코드) vào một partition. Dấu hiệu là phần lớn tác vụ (task / 작업) hoàn tất nhưng một vài tác vụ (task / 작업) kéo dài, bộ nhớ (memory / 메모리) cao và spill lớn.

Các hướng xử lý tùy ngữ nghĩa (semantics / 의미론):

- lọc hoặc xử lý `null`/heavy hitter riêng;
- pre-aggregate trước phép nối (join / 조인);
- salting key rồi aggregate lại;
- broadcast phía nhỏ khi thật sự phù hợp;
- thay đổi partition chiến lược (strategy / 전략) hoặc giới hạn đầu vào (input / 입력) theo thời gian (time / 시간) slice.

Tăng worker không chữa được một key vẫn phải đi vào một partition duy nhất.

> **Chuyển mạch:** **Spill và memory pressure** tạo latency và retry risk; **Join semantics** cần nói rõ duplicate, null và ordering khi chạy trong điều kiện đó.

## 5. Spill và bộ nhớ (memory / 메모리) pressure

Khi bảng băm (hash table / 해시 테이블), sort buffer hoặc aggregation trạng thái (state / 상태) vượt bộ nhớ (memory / 메모리), engine spill intermediate dữ liệu (data / 데이터) xuống disk. Spill bảo vệ tính đúng đắn (correctness / 정확성) nhưng tăng I/O, serialization và merge pass. Spill cao có thể là triệu chứng của skew, partition quá lớn, projection dư thừa hoặc tính đồng thời (concurrency / 동시성) quá cao.

Đừng chỉ tăng bộ nhớ (memory / 메모리). Hãy phân biệt:

```text
input bytes → post-filter bytes → shuffle bytes → spill bytes → output bytes
```

Mỗi bước có bottleneck khác nhau và cần bằng chứng (evidence / 증거) riêng.

> **Chuyển mạch:** **Join semantics** khóa correctness của kết quả; **Fault recovery** kiểm tra retry, checkpoint và partial output khi stage thất bại.

## 6. phép nối (join / 조인) ngữ nghĩa (semantics / 의미론)

Băm (hash / 해시) phép nối (join / 조인) thường cần bản dựng (build / 빌드) side vừa bộ nhớ (memory / 메모리); sort-merge phép nối (join / 조인) cần sort và có thể spill; broadcast phép nối (join / 조인) giảm shuffle nhưng tạo pressure trên mọi worker. Chọn thuật toán (algorithm / 알고리즘) phải dựa trên cardinality, phân phối (distribution / 분포), null ngữ nghĩa (semantics / 의미론), freshness và hành vi khi thất bại (failure behavior / 실패 동작).

Nếu duplicate key ở một phía là hợp lệ, phép nối (join / 조인) đầu ra (output / 출력) có thể tăng theo tích cardinality. truy vấn (query / 쿼리) “chạy được” không chứng minh phép nối (join / 조인) đúng nghiệp vụ (business / 비즈니스).

> **Chuyển mạch:** **Fault recovery** bảo đảm output không sai khi retry; **Performance review loop** dùng runtime evidence để tìm bottleneck còn lại.

## 7. Fault khôi phục (recovery / 복구)

Worker thất bại (failure / 실패) buộc engine thử lại (retry / 재시도) tác vụ (task / 작업) hoặc stage. Nếu nguồn (source / 소스) và sink có side tác động (effect / 효과) ngoài giao dịch (transaction / 트랜잭션), thử lại (retry / 재시도) có thể duplicate. Intermediate dữ liệu (data / 데이터) cần được tái tạo hoặc lưu với vòng đời (lifecycle / 생명주기) rõ ràng. đầu ra (output / 출력) lần ghi nhận (commit / 커밋) chỉ nên công khai (public / 공개) sau khi toàn bộ partition cần thiết đã hoàn tất và reconcile đạt.

> **Chuyển mạch:** **Performance review loop** liên hệ failure evidence với metric; **Shuffle cost model** lượng hóa network, disk và compute contribution.

## 8. hiệu năng (performance / 성능) rà soát (review / 검토) vòng lặp (loop / 루프)

1. Xác định grain và predicate cần thiết.
2. Đo đầu vào (input / 입력), filtered, shuffle, spill, đầu ra (output / 출력) bytes.
3. Kiểm tra tác vụ (task / 작업) duration phân phối (distribution / 분포), không chỉ average.
4. Tìm heavy hitter/skew key.
5. Kiểm tra bộ nhớ (memory / 메모리), disk, mạng (network / 네트워크) và tính đồng thời (concurrency / 동시성) saturation.
6. Thay đổi một ranh giới (boundary / 경계), chạy lại cùng đầu vào (input / 입력)/phiên bản (version / 버전) và so sánh tính đúng đắn (correctness / 정확성) trước chi phí (cost / 비용).

Đọc tiếp: [03 — Storage và layout](../03_storage_and_formats.md), [07 — Streaming systems](../07_streaming_systems/README.md), [12 — Cost, performance và capacity](../12_cost_performance_capacity/README.md).

> **Chuyển mạch:** **Shuffle cost model** chỉ ra component đắt nhất; **Skew diagnosis bằng phân phối** kiểm tra cost có đến từ key distribution hay không.

## 9. Shuffle chi phí (cost / 비용) mô hình (model / 모델)

Một approximation hữu ích khi phân tích stage:

```text
wall time ≈ max(task compute + local spill) + network shuffle + barrier wait
```

`max`, không phải average, quyết định long-tail độ trễ (latency / 지연 시간). Nếu một partition có 10 lần bytes trung bình, tăng worker chỉ làm 99 tác vụ (task / 작업) khác rảnh hơn; tác vụ (task / 작업) hotspot vẫn giữ wall thời gian (time / 시간).

Trước shuffle, projection và filter làm giảm payload. Sau shuffle, pre-aggregation làm giảm số row gửi tới phép nối (join / 조인)/aggregate. Nhưng pre-aggregation chỉ hợp lệ nếu thao tác (operation / 연산) associative/commutative hoặc có quy tắc (rule / 규칙) preserve thứ tự (order / 순서).

> **Chuyển mạch:** **Skew diagnosis** gắn histogram với task runtime; **Determinism và retry** kiểm tra cùng input có cho cùng output sau lần chạy lại hay không.

## 10. Skew diagnosis bằng phân phối

Hãy ghi lại p50/p95/p99 tác vụ (task / 작업) duration, đầu vào (input / 입력) bytes mỗi tác vụ (task / 작업), spill bytes, peak bộ nhớ (memory / 메모리) và key frequency. Average duration có thể che khuất một heavy hitter. Một key `NULL`, tenant lớn hoặc ngày dữ liệu lỗi thường là đầu mối.

Salting thay key `k` thành `(k, salt)` để chia heavy hitter, sau đó aggregate lần hai theo `k`. Đây là sự đánh đổi (trade-off / 트레이드오프): thêm stage và trạng thái (state / 상태) nhưng tránh một partition bị quá tải. Không salt nếu bên tiêu thụ (consumer / 소비자) cần thứ tự (ordering / 순서) per key hoặc nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) không cho phép chia key.

> **Chuyển mạch:** **Determinism và retry** khép README bằng correctness, capacity và recovery evidence; chi tiết engine quay về canonical distributed-systems owner.

## 11. Determinism và thử lại (retry / 재시도)

Phân tán (distributed / 분산) reduction không phải lúc nào cũng deterministic do thứ tự merge floating điểm (point / 지점), tie trong sort hoặc non-deterministic UDF. Nếu đầu ra (output / 출력) được dùng cho reconciliation, cần chuẩn gốc (canonical / 정본) thứ tự (ordering / 순서), decimal arithmetic hoặc tolerance rõ ràng.

Thử lại (retry / 재시도) tác vụ (task / 작업) cũng cần tránh side tác động (effect / 효과). ghi (write / 쓰기) temporary đầu ra (output / 출력) theo tác vụ (task / 작업) attempt, rồi lần ghi nhận (commit / 커밋) một attempt thắng; không để mỗi thử lại (retry / 재시도) append trực tiếp vào serving bảng (table / 테이블).

> **Bàn giao:** Sau **11. Determinism và thử lại (retry / 재시도)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
