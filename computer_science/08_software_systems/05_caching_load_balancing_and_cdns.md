# Caching, tải (load / 로드) balancing và CDNs

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Caching, load balancing và CDNs**. Route đi từ cache copy/consistency → cache-aside/TTL/eviction → stampede control → L4/L7 balancing/consistent hashing → CDN locality, để freshness và capacity được cân cùng nhau.

Khi hệ thống (system / 시스템) lớn lên, hai câu hỏi lặp lại: làm sao tránh lặp lại công việc (work / 작업)/dữ liệu (data / 데이터) transfer đắt, và làm sao phân phối công việc (work / 작업) qua nhiều resources? Caching trả lời câu đầu; tải (load / 로드) balancing trả lời câu hai; CDN kết hợp cả hai theo geography/mạng (network / 네트워크) topology.

## Bộ nhớ đệm (cache / 캐시) là bản sao có điều kiện

Bộ nhớ đệm (cache / 캐시) giữ bản sao (copy / 복사) của dữ liệu (data / 데이터)/computation gần nơi sử dụng hơn hoặc trên medium nhanh hơn. Nhưng bản sao (copy / 복사) tạo consistency bài toán (problem / 문제): nguồn (source / 소스) thay đổi thì bộ nhớ đệm (cache / 캐시) stale.

Mỗi bộ nhớ đệm (cache / 캐시) thiết kế (design / 설계) phải trả lời key, giá trị (value / 값), eviction, freshness và vô hiệu hóa (invalidation / 무효화). “Thêm Redis” không trả lời các câu đó.

> **Chuyển mạch:** Trong **Caching, tải (load / 로드) balancing và CDNs**, **Cache-aside** tiếp nhận điểm tựa từ **Bộ nhớ đệm (cache / 캐시) là bản sao có điều kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TTL và staleness ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cache-aside

Ứng dụng (application / 애플리케이션) đọc bộ nhớ đệm (cache / 캐시) trước; miss thì đọc nguồn (source / 소스), ghi bộ nhớ đệm (cache / 캐시) rồi trả. ghi (write / 쓰기) thường cập nhật (update / 업데이트) nguồn (source / 소스) và invalidate bộ nhớ đệm (cache / 캐시).

Race có thể xảy ra: yêu cầu (request / 요청) A miss, yêu cầu (request / 요청) B cập nhật (update / 업데이트) nguồn (source / 소스) + invalidate, rồi A ghi old giá trị (value / 값) trở lại bộ nhớ đệm (cache / 캐시). Solutions phụ thuộc versioning, short TTL hoặc coordinated ghi (write / 쓰기) chiến lược (strategy / 전략).

> **Chuyển mạch:** Ở chặng này của **Caching, tải (load / 로드) balancing và CDNs**, **TTL và staleness ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **Cache-aside** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Eviction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TTL và staleness ngân sách (budget / 예산)

Time-to-live đặt upper bound thực dụng cho freshness nhưng không đảm bảo chính xác (exact / 정확한) vô hiệu hóa (invalidation / 무효화) moment. Short TTL tăng nguồn (source / 소스) tải (load / 로드); long TTL tăng stale cửa sổ (window / 윈도우).

Nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항) nên nói “stale tối đa bao lâu chấp nhận được” thay vì “bộ nhớ đệm (cache / 캐시) phải luôn mới”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Caching, tải (load / 로드) balancing và CDNs**, **Eviction** tiếp nhận điểm tựa từ **TTL và staleness ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ đệm (cache / 캐시) stampede** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Eviction

Bộ nhớ đệm (cache / 캐시) sức chứa (capacity / 용량) hữu hạn nên cần eviction chính sách (policy / 정책) như LRU, LFU, CLOCK hoặc adaptive variants. tải công việc (workload / 워크로드) scan có thể phá LRU; skewed popularity làm LFU hữu ích hơn.

Eviction chính sách (policy / 정책) là online thuật toán (algorithm / 알고리즘) vì không biết future accesses.

> **Chuyển mạch:** Trong **Caching, tải (load / 로드) balancing và CDNs**, **Bộ nhớ đệm (cache / 캐시) stampede** tiếp nhận điểm tựa từ **Eviction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tải (load / 로드) balancing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ đệm (cache / 캐시) stampede

Khi hot key hết hạn, hàng nghìn requests cùng miss và cùng hit backend. Single-flight/yêu cầu (request / 요청) coalescing, jittered TTL và stale-while-revalidate là mitigations.

Đây là ví dụ synchronization bài toán (problem / 문제) ở hệ thống (system / 시스템) mức (level / 수준).

> **Chuyển mạch:** Ở chặng này của **Caching, tải (load / 로드) balancing và CDNs**, **Tải (load / 로드) balancing** tiếp nhận điểm tựa từ **Bộ nhớ đệm (cache / 캐시) stampede** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tầng (layer / 계층) 4 và tầng (layer / 계층) 7** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tải (load / 로드) balancing

Bộ cân bằng tải (load balancer / 로드 밸런서) chọn backend cho yêu cầu (request / 요청). Strategies gồm round robin, least connections, weighted variants, consistent hashing hoặc locality-aware routing.

Nếu backends heterogeneous hoặc requests chi phí (cost / 비용) khác nhau, simple round robin có thể tạo imbalance.

Health check phải phân biệt tiến trình (process / 프로세스) alive với dịch vụ (service / 서비스) capable of useful công việc (work / 작업). Một máy chủ (server / 서버) overloaded có thể technically return health 200 nhưng không nên nhận thêm tải (load / 로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Caching, tải (load / 로드) balancing và CDNs**, **Tầng (layer / 계층) 4 và tầng (layer / 계층) 7** tiếp nhận điểm tựa từ **Tải (load / 로드) balancing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Consistent hashing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tầng (layer / 계층) 4 và tầng (layer / 계층) 7

L4 bộ cân bằng tải (load balancer / 로드 밸런서) tuyến (route / 경로) theo vận chuyển (transport / 전송) liên kết (connection / 연결)/IP/cổng (port / 포트). L7 hiểu HTTP-level dữ liệu (data / 데이터) như host/đường dẫn (path / 경로)/header để tuyến (route / 경로) richer chính sách (policy / 정책).

L7 flexibility có CPU/parsing/TLS overhead và larger attack surface.

> **Chuyển mạch:** Trong **Caching, tải (load / 로드) balancing và CDNs**, **Consistent hashing** tiếp nhận điểm tựa từ **Tầng (layer / 계층) 4 và tầng (layer / 계층) 7** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CDN** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Consistent hashing

Hashing key lên ring/không gian (space / 공간) giúp remap fraction nhỏ keys khi nodes add/remove, hữu ích cho caches/shards.

Virtual nodes cải thiện balance. Tuy nhiên consistent hashing không tự xử lý hot keys hoặc heterogeneous sức chứa (capacity / 용량) nếu không weighting.

> **Chuyển mạch:** Ở chặng này của **Caching, tải (load / 로드) balancing và CDNs**, **CDN** tiếp nhận điểm tựa từ **Consistent hashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CDN

Content Delivery mạng (network / 네트워크) đặt edge caches gần users/mạng (network / 네트워크) peering points. Static assets rất phù hợp; động (dynamic / 동적) content có thể use edge compute, origin shielding hoặc cacheable APIs.

Bộ nhớ đệm (cache / 캐시) key phải bao gồm dimensions làm phản hồi (response / 응답) khác nhau. Bỏ `Accept-Encoding`, auth trạng thái (state / 상태) hoặc locale khỏi key có thể trả sai dữ liệu (data / 데이터); include quá nhiều dimensions lại phá hit tỷ lệ (rate / 비율).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Caching, tải (load / 로드) balancing và CDNs**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **CDN** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“bộ nhớ đệm (cache / 캐시) luôn làm nhanh hơn.”** Cold miss, serialization, mạng (network / 네트워크) hop và vô hiệu hóa (invalidation / 무효화) độ phức tạp (complexity / 복잡도) có thể khiến bộ nhớ đệm (cache / 캐시) không đáng cho cheap dữ liệu (data / 데이터).

**“bộ cân bằng tải (load balancer / 로드 밸런서) giải scaling.”** Backend bottleneck chung như cơ sở dữ liệu (database / 데이터베이스) vẫn có thể choke toàn hệ thống (system / 시스템).

**“CDN chỉ là mirror static files.”** hiện đại (modern / 현대적) CDNs còn TLS termination, routing, DDoS absorption và edge computation, nhưng cốt lõi (core / 핵심) mô hình tư duy (mental model / 사고 모델) vẫn là placement/caching gần máy khách (client / 클라이언트).

> **Chuyển mạch:** Trong **Caching, tải (load / 로드) balancing và CDNs**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Caching đổi freshness/độ phức tạp (complexity / 복잡도) lấy độ trễ (latency / 지연 시간)/tải (load / 로드); tải (load / 로드) balancing đổi single-resource simplicity lấy coordination. Cả hai chỉ đúng khi key, health và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) rõ.

> **Chuyển mạch:** Ở chặng này của **Caching, tải (load / 로드) balancing và CDNs**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Xem [online algorithms](../01_algorithms_data_structures/10_randomized_approximation_and_online_algorithms.md), [performance/capacity](./02_performance_capacity_and_scalability.md), [Internet routing](../06_networks_distributed_systems/07_routing_protocols_and_the_internet.md) và [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
