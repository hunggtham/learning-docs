# Caching consistency, vô hiệu hóa (invalidation / 무효화), stampede và hot keys

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Caching consistency, invalidation, stampede và hot keys**. Route đi từ authoritative state → cache-aside/read-write ordering → invalidation/versioning → stampede protection → hot-key locality, để freshness và load reduction không phá correctness.

Bộ nhớ đệm (cache / 캐시) giảm độ trễ (latency / 지연 시간) và tải (load / 로드) bằng cách giữ bản sao trạng thái (state / 상태) gần bên tiêu thụ (consumer / 소비자) hơn. Nhưng ngay khi có thêm một bản sao, hệ thống phải trả lời: **nguồn chuẩn (source of truth / 정본) ở đâu, stale bao lâu được chấp nhận, cập nhật (update / 업데이트)/vô hiệu hóa (invalidation / 무효화) được thứ tự (ordering / 순서) thế nào, và backend sống sót ra sao khi bộ nhớ đệm (cache / 캐시) đồng loạt miss hoặc biến mất.**

Một bộ nhớ đệm (cache / 캐시) vì thế không chỉ là cấu trúc dữ liệu (data structure / 자료구조); nó là một **replication giao thức (protocol / 프로토콜) có eviction chính sách (policy / 정책)**.

## 1. bất biến (invariant / 불변식) đầu tiên: phải biết authoritative trạng thái (state / 상태) nằm ở đâu

Nếu cơ sở dữ liệu (database / 데이터베이스) có `V2` nhưng bộ nhớ đệm (cache / 캐시) còn `V1`, đó không tự động là bug. Nó chỉ là bug nếu freshness đặc tả hợp đồng (contract / 계약) nói reader phải thấy `V2` ở thời điểm đó.

Trước khi thêm bộ nhớ đệm (cache / 캐시), cần định nghĩa đặc tả hợp đồng (contract / 계약) như:

```text
strongly fresh?
bounded stale tối đa N giây?
read-your-writes cần không?
stale-while-revalidate được không?
cache failure có bypass về origin không?
```

Không có đặc tả hợp đồng (contract / 계약), nhóm (team / 팀) chỉ tranh luận “stale thế này có chấp nhận được không?” sau sự cố (incident / 인시던트).

> **Nối mạch:** **2. Cache-aside đơn giản nhưng có race thứ tự (ordering / 순서)** nối từ **1. bất biến (invariant / 불변식) đầu tiên: phải biết authoritative trạng thái (state / 상태) nằm ở đâu** sang **3. TTL là freshness bound thô, không phải consistency proof**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Cache-aside đơn giản nhưng có race thứ tự (ordering / 순서)

Trong cache-aside, reader miss bộ nhớ đệm (cache / 캐시) → đọc DB → populate bộ nhớ đệm (cache / 캐시). Writer thường cập nhật (update / 업데이트) DB rồi invalidate/cập nhật (update / 업데이트) bộ nhớ đệm (cache / 캐시).

Race điển hình:

```text
Reader miss cache → đọc DB V1
Writer ghi DB V2 → invalidate cache
Reader cũ set cache V1
```

Stale giá trị (value / 값) bị resurrect. TTL cuối cùng có thể sửa nhưng cửa sổ (window / 윈도우) stale vẫn tồn tại.

Mitigation có thể là versioned giá trị (value / 값)/key, delayed/double vô hiệu hóa (invalidation / 무효화), write-through hoặc thứ tự (ordering / 순서) đơn vị từ (token / 토큰) tùy yêu cầu (requirement / 요구사항). Không có chiến lược (strategy / 전략) universal.

> **Nối mạch:** **3. TTL là freshness bound thô, không phải consistency proof** nối từ **2. Cache-aside đơn giản nhưng có race thứ tự (ordering / 순서)** sang **4. Write-through và write-behind đổi thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. TTL là freshness bound thô, không phải consistency proof

TTL chỉ định entry được reuse trong bao lâu trước refresh/expiry. TTL dài tăng hit tỷ lệ (rate / 비율) nhưng stale lâu; TTL ngắn tăng origin tải (load / 로드).

Nếu hàng nghìn keys cùng TTL và cùng populate lúc deploy, expiry đồng loạt tạo traffic spike. Jitter TTL giúp phân tán expiry.

TTL giải cleanup và bounded staleness thô, nhưng không giải read-your-writes hay race thứ tự (ordering / 순서) tự động.

> **Nối mạch:** **4. Write-through và write-behind đổi thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)** nối từ **3. TTL là freshness bound thô, không phải consistency proof** sang **5. Multi-layer bộ nhớ đệm (cache / 캐시) làm vô hiệu hóa (invalidation / 무효화) đường dẫn (path / 경로) dài hơn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Write-through và write-behind đổi thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)

Write-through đặt bộ nhớ đệm (cache / 캐시) trong ghi (write / 쓰기) đường dẫn (path / 경로); read freshness tốt hơn nhưng ghi (write / 쓰기) độ trễ (latency / 지연 시간)/coupling tăng.

Write-behind ghi bộ nhớ đệm (cache / 캐시)/buffer rồi flush nguồn (source / 소스) async; thông lượng (throughput / 처리량) có thể tốt nhưng durability, thứ tự (ordering / 순서) và khôi phục (recovery / 복구) trở nên khó hơn. Khi bộ nhớ đệm (cache / 캐시) nút (node / 노드) chết trước flush, logical ghi (write / 쓰기) có thể mất nếu bộ nhớ đệm (cache / 캐시) đang đóng vai trò hàng đợi (queue / 큐) bền mà thực tế không durable.

Do đó bộ nhớ đệm (cache / 캐시) mẫu (pattern / 패턴) phải được đánh giá cùng durability đặc tả hợp đồng (contract / 계약), không chỉ hit tỷ lệ (rate / 비율).

> **Nối mạch:** **4. Write-through và write-behind đổi thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)** đặt đầu vào cho **5. Multi-layer bộ nhớ đệm (cache / 캐시) làm vô hiệu hóa (invalidation / 무효화) đường dẫn (path / 경로) dài hơn**, rồi **6. Read-your-writes là guarantee riêng** mở rộng hệ quả.

## 5. Multi-layer bộ nhớ đệm (cache / 캐시) làm vô hiệu hóa (invalidation / 무효화) đường dẫn (path / 경로) dài hơn

Trình duyệt (browser / 브라우저), CDN, reverse proxy, service-local bộ nhớ đệm (cache / 캐시), phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시) và DB buffer pool có thể cùng giữ trạng thái (state / 상태).

```text
origin DB
→ distributed cache
→ service local cache
→ CDN/proxy
→ browser
```

Fix Redis vô hiệu hóa (invalidation / 무효화) không giúp nếu CDN vẫn giữ stale phản hồi (response / 응답). Debugging cần biết key/phiên bản (version / 버전)/header ngữ nghĩa (semantics / 의미론) ở từng tầng (layer / 계층).

Bộ nhớ đệm (cache / 캐시) càng nhiều tầng, consistency đặc tả hợp đồng (contract / 계약) càng cần rõ về nơi nào được phép stale bao lâu.

> **Nối mạch:** **5. Multi-layer bộ nhớ đệm (cache / 캐시) làm vô hiệu hóa (invalidation / 무효화) đường dẫn (path / 경로) dài hơn** đặt đầu vào cho **6. Read-your-writes là guarantee riêng**, rồi **7. bộ nhớ đệm (cache / 캐시) stampede là synchronized miss thất bại (failure / 실패)** mở rộng hệ quả.

## 6. Read-your-writes là guarantee riêng

Người dùng (user / 사용자) vừa cập nhật (update / 업데이트) profile rồi GET ngay có thể đọc bộ nhớ đệm (cache / 캐시) cũ. toàn cục (global / 전역) strong consistency có thể quá đắt, nhưng session-scoped read-your-writes đôi khi đủ.

Ghi (write / 쓰기) đường dẫn (path / 경로) có thể cập nhật (update / 업데이트)/invalidate đồng bộ, phản hồi (response / 응답) trả phiên bản (version / 버전) đơn vị từ (token / 토큰), hoặc subsequent read tạm bypass stale tầng (layer / 계층).

Điểm quan trọng là guarantee phải được thiết kế, không xuất hiện tự nhiên từ TTL.

> **Nối mạch:** **7. bộ nhớ đệm (cache / 캐시) stampede là synchronized miss thất bại (failure / 실패)** nối từ **6. Read-your-writes là guarantee riêng** sang **8. Hot key là skew bài toán (problem / 문제), không phải average-capacity bài toán (problem / 문제)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. bộ nhớ đệm (cache / 캐시) stampede là synchronized miss thất bại (failure / 실패)

Hot key hết hạn và hàng nghìn requests cùng miss có thể cùng gọi origin. bộ nhớ đệm (cache / 캐시) được thêm để giảm tải (load / 로드) nhưng lại biến thành trigger cho thundering herd.

Mitigation gồm:

```text
single-flight/request coalescing
stale-while-revalidate
probabilistic early refresh
per-key refresh ownership
bounded regeneration concurrency
```

Bất biến (invariant / 불변식) hiệu năng (performance / 성능) cần là: một miss wave không được biến thành N expensive origin calls nếu regeneration có thể share.

> **Nối mạch:** **8. Hot key là skew bài toán (problem / 문제), không phải average-capacity bài toán (problem / 문제)** nối từ **7. bộ nhớ đệm (cache / 캐시) stampede là synchronized miss thất bại (failure / 실패)** sang **9. Negative caching cũng có consistency chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Hot key là skew bài toán (problem / 문제), không phải average-capacity bài toán (problem / 문제)

Consistent hashing phân keys giữa shards nhưng không chia được một key duy nhất nếu mỗi key chỉ có một đơn vị sở hữu (owner / 오너) shard.

Một key cực nóng có thể saturate shard dù cluster trung bình còn rảnh. Giải pháp có thể dùng near-cache, replication của hot giá trị (value / 값), yêu cầu (request / 요청) coalescing hoặc thay đổi mô hình dữ liệu (data model / 데이터 모델).

Average QPS/shard che mất phân phối (distribution / 분포) skew. bằng chứng vận hành (production evidence / 운영 증거) cần per-key/per-shard tail.

> **Nối mạch:** **9. Negative caching cũng có consistency chi phí (cost / 비용)** nối từ **8. Hot key là skew bài toán (problem / 문제), không phải average-capacity bài toán (problem / 문제)** sang **10. Versioned key giảm vô hiệu hóa (invalidation / 무효화) race bằng immutable naming**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Negative caching cũng có consistency chi phí (cost / 비용)

Lưu `not found` giúp ngăn repeated lookup cho đối tượng (object / 객체) không tồn tại hoặc attack probing. Nhưng đối tượng (object / 객체) vừa được tạo có thể bị che bởi negative entry cho tới TTL.

Negative TTL thường cần ngắn hơn và creation đường dẫn (path / 경로) có thể cần vô hiệu hóa (invalidation / 무효화). Absence cũng là trạng thái (state / 상태) cần phiên bản (version / 버전)/freshness chính sách (policy / 정책).

> **Nối mạch:** **10. Versioned key giảm vô hiệu hóa (invalidation / 무효화) race bằng immutable naming** nối từ **9. Negative caching cũng có consistency chi phí (cost / 비용)** sang **11. bộ nhớ đệm (cache / 캐시) key tính đúng đắn (correctness / 정확성) là bảo mật (security / 보안) bất biến (invariant / 불변식)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Versioned key giảm vô hiệu hóa (invalidation / 무효화) race bằng immutable naming

Thay vì mutate `profile:123`, hệ thống (system / 시스템) có thể dùng `profile:123:v42`. cập nhật (update / 업데이트) tạo phiên bản (version / 버전) mới; old key tự expire.

Điều này biến vô hiệu hóa (invalidation / 무효화) thành pointer/phiên bản (version / 버전) cập nhật (update / 업데이트), giảm một số race. Đổi lại key churn/bộ nhớ (memory / 메모리) footprint tăng và vẫn cần nơi authoritative để biết hiện tại (current / 현재) phiên bản (version / 버전).

Versioned key là ví dụ đổi mutable-state coordination lấy immutable-state indirection.

> **Nối mạch:** **11. bộ nhớ đệm (cache / 캐시) key tính đúng đắn (correctness / 정확성) là bảo mật (security / 보안) bất biến (invariant / 불변식)** nối từ **10. Versioned key giảm vô hiệu hóa (invalidation / 무효화) race bằng immutable naming** sang **12. bộ nhớ đệm (cache / 캐시) outage có thể làm origin collapse**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. bộ nhớ đệm (cache / 캐시) key tính đúng đắn (correctness / 정확성) là bảo mật (security / 보안) bất biến (invariant / 불변식)

Nếu phản hồi (response / 응답) ngữ nghĩa (semantic / 의미적) phụ thuộc tenant, người dùng (user / 사용자), locale, permission hoặc tính năng (feature / 기능) trạng thái (state / 상태) nhưng bộ nhớ đệm (cache / 캐시) key thiếu dimension tương ứng, hệ thống (system / 시스템) có thể trả dữ liệu (data / 데이터) của principal khác.

Đây là dữ liệu (data / 데이터) leak, không chỉ stale bug.

Bất biến (invariant / 불변식) cần là:

> Mọi đầu vào (input / 입력) ảnh hưởng tới authorization/ngữ nghĩa (semantic / 의미적) phản hồi (response / 응답) phải được phản ánh trong bộ nhớ đệm (cache / 캐시) partition/key hoặc phản hồi (response / 응답) phải thật sự share-safe.

Caching vì vậy giao trực tiếp với ranh giới bảo mật (security boundary / 보안 경계).

> **Nối mạch:** **12. bộ nhớ đệm (cache / 캐시) outage có thể làm origin collapse** nối từ **11. bộ nhớ đệm (cache / 캐시) key tính đúng đắn (correctness / 정확성) là bảo mật (security / 보안) bất biến (invariant / 불변식)** sang **13. bộ nhớ đệm (cache / 캐시) nút (node / 노드) thất bại (failure / 실패) và remapping tạo cold-start burst**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. bộ nhớ đệm (cache / 캐시) outage có thể làm origin collapse

Nếu backend được provision với steady-state miss tỷ lệ (rate / 비율) 5%, bộ nhớ đệm (cache / 캐시) outage/cold start có thể đưa 100% traffic về origin. Một phụ thuộc (dependency / 의존성) được gọi là “optional tối ưu hóa (optimization / 최적화)” trên kiến trúc (architecture / 아키텍처) diagram có thể là hard sức chứa (capacity / 용량) phụ thuộc (dependency / 의존성) trong thực tế.

Thất bại (failure / 실패) chuỗi (chain / 사슬):

```text
cache node/cluster fail
→ miss rate tăng
→ DB/origin queue tăng
→ latency + timeout tăng
→ retry tăng
→ origin overload
```

Resilience cần tỷ lệ (rate / 비율) limit, circuit breaker, stale/degraded fallback hoặc origin headroom phù hợp.

> **Nối mạch:** **13. bộ nhớ đệm (cache / 캐시) nút (node / 노드) thất bại (failure / 실패) và remapping tạo cold-start burst** nối từ **12. bộ nhớ đệm (cache / 캐시) outage có thể làm origin collapse** sang **14. hiệu năng (performance / 성능) pressure và eviction tương tác (interaction / 상호작용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. bộ nhớ đệm (cache / 캐시) nút (node / 노드) thất bại (failure / 실패) và remapping tạo cold-start burst

Phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시) partition bằng consistent hashing giảm lượng keys phải remap khi nút (node / 노드) thay đổi, nhưng remapped keys vẫn cold. bộ nhớ đệm (cache / 캐시) cluster sự kiện (event / 이벤트) có thể tạo miss burst không đồng đều theo shard/key popularity.

Sức chứa (capacity / 용량) kiểm thử (test / 테스트) cần simulate cold bộ nhớ đệm (cache / 캐시), không chỉ benchmark steady-state warm bộ nhớ đệm (cache / 캐시).

> **Nối mạch:** **14. hiệu năng (performance / 성능) pressure và eviction tương tác (interaction / 상호작용)** nối từ **13. bộ nhớ đệm (cache / 캐시) nút (node / 노드) thất bại (failure / 실패) và remapping tạo cold-start burst** sang **15. bằng chứng vận hành (production evidence / 운영 증거)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. hiệu năng (performance / 성능) pressure và eviction tương tác (interaction / 상호작용)

Khi working set lớn hơn bộ nhớ đệm (cache / 캐시) sức chứa (capacity / 용량), churn/eviction tăng. Hit tỷ lệ (rate / 비율) có thể giảm dần hoặc collapse nếu truy cập (access / 접근) mẫu (pattern / 패턴) không phù hợp replacement chính sách (policy / 정책).

Large entries giảm effective key sức chứa (capacity / 용량). Hot/cold mix, TTL và admission chính sách (policy / 정책) có thể quyết định bộ nhớ đệm (cache / 캐시) pollution.

Một hit-rate aggregate 99% chưa đủ nếu 1% misses chính là những keys đắt nhất.

> **Nối mạch:** **14. hiệu năng (performance / 성능) pressure và eviction tương tác (interaction / 상호작용)** đặt vấn đề; **15. bằng chứng vận hành (production evidence / 운영 증거)** kiểm tra bằng chứng, rồi **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** mở rộng hệ quả.

## 15. bằng chứng vận hành (production evidence / 운영 증거)

Cần quan sát:

```text
hit/miss rate theo key class/shard
origin QPS do misses
stale/version mismatch events nếu đo được
refresh/coalescing contention
expiry rate
per-key hotness/skew
cache memory/eviction rate
cold-start behavior
backend latency khi cache degraded
```

Dấu vết (trace / 추적) nên cho biết yêu cầu (request / 요청) hit tầng (layer / 계층) nào, miss ở đâu và có regeneration/thử lại (retry / 재시도) hay không.

> **Nối mạch:** **15. bằng chứng vận hành (production evidence / 운영 증거)** đặt vấn đề; **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** kiểm tra bằng chứng, rồi **17. Mô hình tư duy** mở rộng hệ quả.

## 16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?

Nếu stale do propagation race, thứ tự (ordering / 순서)/phiên bản (version / 버전) giao thức (protocol / 프로토콜) quyết định. Nếu p99 tăng vì hot shard, partition/key phân phối (distribution / 분포) quyết định. Nếu bộ nhớ đệm (cache / 캐시) outage kéo DB chết, origin sức chứa (capacity / 용량)/backpressure quyết định. Nếu dữ liệu (data / 데이터) leak qua bộ nhớ đệm (cache / 캐시), authorization/key derivation ranh giới (boundary / 경계) quyết định.

“Redis chậm” thường chỉ là symptom-level label.

> **Nối mạch:** **17. Mô hình tư duy** tổng hợp từ **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## 17. Mô hình tư duy

> bộ nhớ đệm (cache / 캐시) là **replicated, disposable trạng thái (state / 상태) với freshness và eviction chính sách (policy / 정책)**. Mọi bộ nhớ đệm (cache / 캐시) thiết kế (design / 설계) phải lập luận (reasoning / 추론) authority, staleness, vô hiệu hóa (invalidation / 무효화) thứ tự (ordering / 순서), miss amplification, key tính đúng đắn (correctness / 정확성) và origin sức chứa (capacity / 용량) khi bộ nhớ đệm (cache / 캐시) biến mất. Tối ưu hit tỷ lệ (rate / 비율) mà không giữ các bất biến (invariant / 불변식) đó chỉ dời thất bại (failure / 실패) sang một tầng (layer / 계층) khó quan sát hơn.

> **Nối mạch:** **Kết nối** tổng hợp từ **17. Mô hình tư duy**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc cùng [Capacity/admission control](./01_capacity_planning_utilization_knee_and_admission_control.md), [Load balancing và locality](./03_load_balancing_connection_pools_and_locality.md), [Distributed consistency](../../06_networks_distributed_systems/advanced/04_crdts_causal_consistency_and_conflict_resolution.md), [Authorization foundation](../../basic/07_security_reliability/02_identity_authentication_and_authorization.md) và [End-to-end overload path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
