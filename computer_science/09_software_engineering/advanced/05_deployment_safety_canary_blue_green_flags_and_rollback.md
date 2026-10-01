# Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. triển khai (deployment / 배포) là một phân tán (distributed / 분산) chuyển tiếp trạng thái (state transition / 상태 전이)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. tính tương thích (compatibility / 호환성) là bất biến (invariant / 불변식) đầu tiên của rolling triển khai (deployment / 배포)** để chuyển câu hỏi ấy thành điều kiện phải giữ. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Deploy không chỉ là bản sao (copy / 복사) sản phẩm tạo ra (artifact / 산출물). Nó thay đổi một running socio-technical hệ thống (system / 시스템) có traffic, persistent dữ liệu (data / 데이터), caches, queues và dependencies đang ở nhiều versions. triển khai (deployment / 배포) chiến lược (strategy / 전략) tốt giữ một bất biến (invariant / 불변식) quan trọng: **mỗi bước rollout phải giới hạn blast radius, giữ tính tương thích (compatibility / 호환성) trong coexistence cửa sổ (window / 윈도우) và tạo đủ bằng chứng (evidence / 증거) để quyết định tiếp tục, dừng, quay lui (rollback / 롤백) hay roll-forward.**

## 1. triển khai (deployment / 배포) là một phân tán (distributed / 분산) chuyển tiếp trạng thái (state transition / 상태 전이)

Khi fleet có 100 instances, rollout hiếm khi đổi từ phiên bản (version / 버전) N sang N+1 atomically. Trong nhiều phút hoặc lâu hơn, hệ thống ở trạng thái mixed-version:

```text
clients cũ + mới
servers N + N+1
schema cũ + expanded schema
events/messages của nhiều versions
cache entries cũ
background jobs cũ
```

Tính đúng đắn (correctness / 정확성) phải giữ trong **chuyển tiếp (transition / 전이) trạng thái (state / 상태)**, không chỉ ở trạng thái cuối.

> **Chuyển mạch:** Deployment là distributed state transition; rolling compatibility giữ invariant đầu tiên, còn canary/blue-green/flags giới hạn blast radius trước khi rollback hoặc mở rộng capacity.

## 2. tính tương thích (compatibility / 호환성) là bất biến (invariant / 불변식) đầu tiên của rolling triển khai (deployment / 배포)

Old/new versions coexist nên giao thức (protocol / 프로토콜)/lược đồ (schema / 스키마) cần hỗ trợ overlap cửa sổ (window / 윈도우). Nếu N+1 ghi dữ liệu (data / 데이터) mà N không đọc được, rolling deploy hoặc quay lui (rollback / 롤백) có thể thất bại (fail / 실패) dù từng phiên bản (version / 버전) riêng lẻ kiểm thử (test / 테스트) pass.

Cần lập luận (reasoning / 추론) cả hai hướng khi cần:

```text
new reader đọc old data?
old reader đọc new data?
new writer tạo format old consumer có chịu được?
message/event consumer lag có kéo version cũ tồn tại lâu hơn dự kiến?
```

Tính tương thích (compatibility / 호환성) ranh giới (boundary / 경계) có thể là API, DB lược đồ (schema / 스키마), sự kiện (event / 이벤트) lược đồ (schema / 스키마), bộ nhớ đệm (cache / 캐시) encoding hoặc dùng chung (shared / 공유) tệp (file / 파일) format.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **3. Rolling triển khai (deployment / 배포) giữ sức chứa (capacity / 용량) nhưng làm trạng thái (state / 상태) không gian (space / 공간) lớn hơn** tiếp nhận điểm tựa từ **2. tính tương thích (compatibility / 호환성) là bất biến (invariant / 불변식) đầu tiên của rolling triển khai (deployment / 배포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Blue-green giảm traffic-switch chi phí (cost / 비용) nhưng không tách trạng thái (state / 상태) tự động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Rolling triển khai (deployment / 배포) giữ sức chứa (capacity / 용량) nhưng làm trạng thái (state / 상태) không gian (space / 공간) lớn hơn

Thay instances dần giúp dịch vụ (service / 서비스) tiếp tục phục vụ và giảm blast radius, nhưng mixed-version trạng thái (state / 상태) tăng độ phức tạp (complexity / 복잡도).

Nếu readiness sai, triển khai (deployment / 배포) controller có thể đưa instance chưa warm vào traffic. Nếu terminate quá nhanh, in-flight công việc (work / 작업) bị cắt. Nếu rollout đồng thời quá nhiều nodes, remaining sức chứa (capacity / 용량) có thể đi qua utilization knee.

Triển khai (deployment / 배포) chính sách (policy / 정책) vì thế liên quan trực tiếp sức chứa (capacity / 용량) kỹ thuật (engineering / 엔지니어링).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **4. Blue-green giảm traffic-switch chi phí (cost / 비용) nhưng không tách trạng thái (state / 상태) tự động** tiếp nhận điểm tựa từ **3. Rolling triển khai (deployment / 배포) giữ sức chứa (capacity / 용량) nhưng làm trạng thái (state / 상태) không gian (space / 공간) lớn hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Canary là experiment dưới traffic thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Blue-green giảm traffic-switch chi phí (cost / 비용) nhưng không tách trạng thái (state / 상태) tự động

Blue-green duy trì hai environments và chuyển traffic. nhị phân (binary / 이진) quay lui (rollback / 롤백) routing có thể rất nhanh nếu trạng thái (state / 상태)/giao thức (protocol / 프로토콜) tương thích.

Nhưng cơ sở dữ liệu (database / 데이터베이스), message broker, third-party side effects thường vẫn dùng chung (shared / 공유). Nếu green đã chạy destructive di chuyển (migration / 마이그레이션) hoặc phát bên ngoài (external / 외부) side tác động (effect / 효과), chuyển traffic về blue không đưa world quay lại trạng thái trước.

“Blue-green quay lui (rollback / 롤백)” chỉ mạnh tới ranh giới (boundary / 경계) trạng thái (state / 상태) mà hai environments thực sự tách được.

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **5. Canary là experiment dưới traffic thật** tiếp nhận điểm tựa từ **4. Blue-green giảm traffic-switch chi phí (cost / 비용) nhưng không tách trạng thái (state / 상태) tự động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Guardrail phải gắn với bất biến (invariant / 불변식), không chỉ CPU/lỗi (error / 오류) tỷ lệ (rate / 비율)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Canary là experiment dưới traffic thật

Canary gửi một phần traffic tới phiên bản (version / 버전) mới rồi đo lỗi (error / 오류), độ trễ (latency / 지연 시간), saturation và nghiệp vụ (business / 비즈니스) invariants.

Canary giảm blast radius nhưng chỉ có giá trị nếu traffic mẫu (sample / 표본) chạm dạng thất bại (failure mode / 실패 모드) cần phát hiện. 1% random traffic có thể bỏ sót rare workflow, large tenant, specific region hoặc high-cost yêu cầu (request / 요청) lớp (class / 클래스).

Canary thiết kế (design / 설계) nên chọn cohort theo rủi ro (risk / 위험), không chỉ percentage.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **6. Guardrail phải gắn với bất biến (invariant / 불변식), không chỉ CPU/lỗi (error / 오류) tỷ lệ (rate / 비율)** tiếp nhận điểm tựa từ **5. Canary là experiment dưới traffic thật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. cờ tính năng (feature flag / 기능 플래그) tách mã (code / 코드) triển khai (deployment / 배포) khỏi tính năng (feature / 기능) exposure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Guardrail phải gắn với bất biến (invariant / 불변식), không chỉ CPU/lỗi (error / 오류) tỷ lệ (rate / 비율)

Một bản phát hành (release / 릴리스) có thể trả HTTP 200 nhưng phá nghiệp vụ (business / 비즈니스) trạng thái (state / 상태). Guardrail tốt có thể gồm:

```text
error/latency SLO burn
resource saturation
queue/DB wait
business invariant violations
payment duplicate/reconciliation mismatch
authorization-denied anomaly
schema compatibility errors
```

Chỉ số (metric / 지표) noisy hoặc label cardinality sai có thể làm auto quay lui (rollback / 롤백) giả. Guardrail cần threshold, cửa sổ (window / 윈도우) và baseline hợp lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **7. cờ tính năng (feature flag / 기능 플래그) tách mã (code / 코드) triển khai (deployment / 배포) khỏi tính năng (feature / 기능) exposure** tiếp nhận điểm tựa từ **6. Guardrail phải gắn với bất biến (invariant / 불변식), không chỉ CPU/lỗi (error / 오류) tỷ lệ (rate / 비율)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. quay lui (rollback / 롤백) không phải thời gian (time / 시간) machine** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. cờ tính năng (feature flag / 기능 플래그) tách mã (code / 코드) triển khai (deployment / 배포) khỏi tính năng (feature / 기능) exposure

Flag cho phép deploy dormant mã (code / 코드) rồi bật dần theo cohort.

Nhưng mỗi flag tạo thêm trạng thái (state / 상태) dimension. N flags có thể tạo nhiều combinations khó kiểm thử (test / 테스트). Flag lâu ngày trở thành permanent branching độ phức tạp (complexity / 복잡도).

Flag cần đơn vị sở hữu (owner / 오너), purpose, expiry/cleanup điều kiện (condition / 조건) và safe default. Security-critical điều khiển (control / 제어) không nên biến thành “flag có thể vô tình off” nếu bất biến (invariant / 불변식) yêu cầu luôn enforce.

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **8. quay lui (rollback / 롤백) không phải thời gian (time / 시간) machine** tiếp nhận điểm tựa từ **7. cờ tính năng (feature flag / 기능 플래그) tách mã (code / 코드) triển khai (deployment / 배포) khỏi tính năng (feature / 기능) exposure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) là phần triển khai (deployment / 배포) khó đảo nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. quay lui (rollback / 롤백) không phải thời gian (time / 시간) machine

Nhị phân (binary / 이진) quay lui (rollback / 롤백) không undo:

```text
DB migration đã mất data
message/event đã publish
email đã gửi
money đã movement
external API side effect
cache/state đã đổi format
```

Do đó cần tách **reversible mã (code / 코드) trạng thái (state / 상태)** khỏi **irreversible world trạng thái (state / 상태)**.

Nhiều sự cố (incident / 인시던트) an toàn hơn khi roll-forward bằng tính tương thích (compatibility / 호환성) fix thay vì cố chạy old nhị phân (binary / 이진) trên trạng thái (state / 상태) mới.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **8. quay lui (rollback / 롤백) không phải thời gian (time / 시간) machine** nêu điều cần giải thích; **9. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) là phần triển khai (deployment / 배포) khó đảo nhất** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. hàng đợi (queue / 큐)/sự kiện (event / 이벤트) làm coexistence cửa sổ (window / 윈도우) dài hơn rollout cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) là phần triển khai (deployment / 배포) khó đảo nhất

Expand-contract mẫu (pattern / 패턴):

```text
1. add compatible structure
2. deploy code hiểu old + new
3. backfill/throttle
4. switch reads/writes
5. verify
6. remove old structure sau safe window
```

Destructive drop/rename sớm phá quay lui (rollback / 롤백) và mixed-version fleet.

Backfill cũng là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경). Nó có thể saturate DB/lưu trữ (storage / 저장소) và làm người dùng (user / 사용자) traffic chậm, nên di chuyển (migration / 마이그레이션) cần tỷ lệ (rate / 비율) limit và khả năng quan sát (observability / 관측 가능성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **9. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) là phần triển khai (deployment / 배포) khó đảo nhất** nêu điều cần giải thích; **10. hàng đợi (queue / 큐)/sự kiện (event / 이벤트) làm coexistence cửa sổ (window / 윈도우) dài hơn rollout cửa sổ (window / 윈도우)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Readiness, liveness và health là control-loop inputs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. hàng đợi (queue / 큐)/sự kiện (event / 이벤트) làm coexistence cửa sổ (window / 윈도우) dài hơn rollout cửa sổ (window / 윈도우)

Dù toàn fleet đã lên N+1, hàng đợi (queue / 큐) có thể còn message được producer N tạo từ trước. bên tiêu thụ (consumer / 소비자) phải hỗ trợ format cũ tới khi backlog drain hoặc retention cửa sổ (window / 윈도우) hết.

Do đó giao thức (protocol / 프로토콜) deprecation cần dựa **dữ liệu (data / 데이터)/message thời gian tồn tại (lifetime / 수명)**, không chỉ “triển khai (deployment / 배포) đã hoàn tất”.

Đây là reason lược đồ (schema / 스키마) evolution là phân tán (distributed / 분산) giao thức (protocol / 프로토콜) theo thời gian.

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **11. Readiness, liveness và health là control-loop inputs** tiếp nhận điểm tựa từ **10. hàng đợi (queue / 큐)/sự kiện (event / 이벤트) làm coexistence cửa sổ (window / 윈도우) dài hơn rollout cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. liên kết (connection / 연결) draining giữ in-flight bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Readiness, liveness và health là control-loop inputs

Tiến trình (process / 프로세스) start không nghĩa ready nhận traffic. Readiness nên phản ánh cục bộ (local / 로컬) ability phục vụ yêu cầu (request / 요청) cần thiết.

Nhưng nếu readiness phụ thuộc mọi downstream dịch vụ (service / 서비스), một phụ thuộc (dependency / 의존성) sự cố (incident / 인시던트) có thể làm toàn fleet tự rút khỏi bộ cân bằng tải (load balancer / 로드 밸런서), tạo outage lớn hơn.

Health tín hiệu (signal / 신호) phải được thiết kế theo khôi phục (recovery / 복구) hành động (action / 동작) tương ứng:

```text
restart process giải được không?
rút khỏi traffic có giảm blast radius không?
dependency failure là local hay shared?
```

Health check sai là phản hồi (feedback / 피드백) controller sai.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **12. liên kết (connection / 연결) draining giữ in-flight bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **11. Readiness, liveness và health là control-loop inputs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. bộ nhớ đệm (cache / 캐시) warm-up và cold-start là phase khác steady trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. liên kết (connection / 연결) draining giữ in-flight bất biến (invariant / 불변식)

Khi instance bị terminate/rút traffic, existing requests/connections cần thời gian hoàn tất hoặc cancellation ngữ nghĩa (semantics / 의미론) rõ.

HTTP/2, WebSocket, long polling hoặc background tác vụ (task / 작업) có thời gian tồn tại (lifetime / 수명) dài hơn yêu cầu (request / 요청) đơn giản. Drain hết thời gian chờ (timeout / 타임아웃) quá ngắn làm user-visible errors; quá dài làm rollout chậm và giữ old phiên bản (version / 버전) lâu.

Triển khai (deployment / 배포) controller phải hiểu liên kết (connection / 연결)/công việc (work / 작업) vòng đời (lifecycle / 생명주기) thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **13. bộ nhớ đệm (cache / 캐시) warm-up và cold-start là phase khác steady trạng thái (state / 상태)** tiếp nhận điểm tựa từ **12. liên kết (connection / 연결) draining giữ in-flight bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. sức chứa (capacity / 용량) headroom là điều kiện triển khai (deployment / 배포) an toàn (safety / 안전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. bộ nhớ đệm (cache / 캐시) warm-up và cold-start là phase khác steady trạng thái (state / 상태)

New instance có empty cục bộ (local / 로컬) bộ nhớ đệm (cache / 캐시), cold JIT, unloaded mã (code / 코드)/dữ liệu (data / 데이터) pages và empty liên kết (connection / 연결) pools. Canary độ trễ (latency / 지연 시간) ban đầu có thể xấu vì warm-up, hoặc ngược lại canary nhẹ tải (load / 로드) nên trông tốt hơn full rollout.

Rollout bằng chứng (evidence / 증거) cần phân biệt warm-up tác động (effect / 효과) với regression thật.

Một triển khai (deployment / 배포) có thể pass canary nhưng thất bại (fail / 실패) ở 50% traffic khi dùng chung (shared / 공유) DB/bộ nhớ đệm (cache / 캐시) pressure tăng phi tuyến.

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **14. sức chứa (capacity / 용량) headroom là điều kiện triển khai (deployment / 배포) an toàn (safety / 안전)** tiếp nhận điểm tựa từ **13. bộ nhớ đệm (cache / 캐시) warm-up và cold-start là phase khác steady trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. dạng thất bại (failure mode / 실패 모드): thử lại (retry / 재시도) storm trong rollout** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. sức chứa (capacity / 용량) headroom là điều kiện triển khai (deployment / 배포) an toàn (safety / 안전)

Rolling cập nhật (update / 업데이트) làm một phần sức chứa (capacity / 용량) unavailable. Nếu steady trạng thái (state / 상태) đã chạy gần utilization knee, rollout itself có thể tạo overload.

Safe deploy cần headroom cho:

```text
instances terminating/startup
warm-up
canary duplication/shadow traffic
schema backfill
cache cold miss
rollback overlap
```

Triển khai (deployment / 배포) và sức chứa (capacity / 용량) planning không thể tách rời.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **15. dạng thất bại (failure mode / 실패 모드): thử lại (retry / 재시도) storm trong rollout** tiếp nhận điểm tựa từ **14. sức chứa (capacity / 용량) headroom là điều kiện triển khai (deployment / 배포) an toàn (safety / 안전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. bảo mật (security / 보안) rollout cũng có tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. dạng thất bại (failure mode / 실패 모드): thử lại (retry / 재시도) storm trong rollout

Nếu new phiên bản (version / 버전) chậm, máy khách (client / 클라이언트)/proxy thử lại (retry / 재시도) có thể tăng tải (load / 로드) lên cả old và new fleet. Auto quay lui (rollback / 롤백) cũng tạo liên kết (connection / 연결) churn/cold bộ nhớ đệm (cache / 캐시), làm khôi phục (recovery / 복구) khó hơn.

Guardrail cần nhìn attempt/thử lại (retry / 재시도) tỷ lệ (rate / 비율) và hàng đợi (queue / 큐) độ sâu (depth / 깊이), không chỉ lỗi (error / 오류) tỷ lệ (rate / 비율). quay lui (rollback / 롤백) hành động (action / 동작) bản thân cũng là một tải (load / 로드) sự kiện (event / 이벤트) cần sức chứa (capacity / 용량).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **16. bảo mật (security / 보안) rollout cũng có tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **15. dạng thất bại (failure mode / 실패 모드): thử lại (retry / 재시도) storm trong rollout** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. bằng chứng vận hành (production evidence / 운영 증거) trước khi tăng rollout** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. bảo mật (security / 보안) rollout cũng có tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)

Certificate/trust bundle, authorization chính sách (policy / 정책), signing key hoặc đơn vị từ (token / 토큰) issuer rotation đều là deployment-like phân tán (distributed / 분산) trạng thái (state / 상태) changes.

Publish verifier trust trước khi issuer chuyển key thường an toàn hơn đổi issuer trước rồi hy vọng consumers cập nhật (update / 업데이트) kịp.

Bảo mật (security / 보안) cấu hình (config / 설정) nên có canary/kiểm tra (audit / 감사)/quay lui (rollback / 롤백) discipline tương tự mã (code / 코드), nhưng không được quay lui (rollback / 롤백) theo cách resurrect credential đã revoke vì compromise.

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **16. bảo mật (security / 보안) rollout cũng có tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** nêu điều cần giải thích; **17. bằng chứng vận hành (production evidence / 운영 증거) trước khi tăng rollout** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. triển khai (deployment / 배포) sự cố (incident / 인시던트) timeline phải giữ phiên bản (version / 버전) định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. bằng chứng vận hành (production evidence / 운영 증거) trước khi tăng rollout

Một promotion quyết định (decision / 결정) nên dựa trên cohort-aware bằng chứng (evidence / 증거):

```text
request success/error by version
latency percentiles by version/workload class
CPU/memory/GC/queue saturation
DB pool/lock/I/O waits
retry/timeout rate
business invariant checks
schema/protocol decode errors
log/trace anomalies
```

So sánh canary với điều khiển (control / 제어) cùng traffic/thời gian (time / 시간) cửa sổ (window / 윈도우) tốt hơn nhìn chỉ số (metric / 지표) tuyệt đối đơn lẻ.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **17. bằng chứng vận hành (production evidence / 운영 증거) trước khi tăng rollout** nêu điều cần giải thích; **18. triển khai (deployment / 배포) sự cố (incident / 인시던트) timeline phải giữ phiên bản (version / 버전) định danh (identity / 식별자)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. Reversibility phải được kiểm thử (test / 테스트), không chỉ viết trong runbook** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. triển khai (deployment / 배포) sự cố (incident / 인시던트) timeline phải giữ phiên bản (version / 버전) định danh (identity / 식별자)

Dấu vết (trace / 추적)/log/chỉ số (metric / 지표) cần biết instance/phiên bản (version / 버전)/bản dựng (build / 빌드)/cấu hình (config / 설정)/flag trạng thái (state / 상태). Nếu không, mixed-version sự cố (incident / 인시던트) khó reconstruct.

Useful siêu dữ liệu (metadata / 메타데이터):

```text
artifact digest/version
schema/config version
feature flags relevant
deployment wave/cohort
instance/zone/region
```

Khả năng quan sát (observability / 관측 가능성) không version-aware sẽ biến triển khai (deployment / 배포) regression thành “random errors across fleet”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **19. Reversibility phải được kiểm thử (test / 테스트), không chỉ viết trong runbook** tiếp nhận điểm tựa từ **18. triển khai (deployment / 배포) sự cố (incident / 인시던트) timeline phải giữ phiên bản (version / 버전) định danh (identity / 식별자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Reversibility phải được kiểm thử (test / 테스트), không chỉ viết trong runbook

Quay lui (rollback / 롤백) đường dẫn (path / 경로) có thể thối theo thời gian. kiểm thử (test / 테스트) cần bao gồm:

```text
deploy N+1 → rollback N
mixed-version traffic
schema expanded nhưng code cũ chạy lại
queue còn old/new messages
failure giữa migration steps
```

Nếu quay lui (rollback / 롤백) chưa được kiểm thử (test / 테스트) với production-like trạng thái (state / 상태), nó là hypothesis chứ chưa phải năng lực (capability / 역량).

> **Chuyển mạch:** Trong **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **20. Mô hình tư duy** gom các mảnh từ **19. Reversibility phải được kiểm thử (test / 테스트), không chỉ viết trong runbook** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Mô hình tư duy

> Safe triển khai (deployment / 배포) là **controlled exposure dưới bất định (uncertainty / 불확실성)**. Rolling/canary/blue-green/flags chỉ là mechanisms. bất biến (invariant / 불변식) thật là tính tương thích (compatibility / 호환성) trong chuyển tiếp (transition / 전이), bounded blast radius, sufficient sức chứa (capacity / 용량) và bằng chứng (evidence / 증거) để quyết định bước tiếp theo. quay lui (rollback / 롤백) chỉ tồn tại trong phạm vi mã (code / 코드)/dữ liệu (data / 데이터)/giao thức (protocol / 프로토콜) còn reversible; ngoài phạm vi đó phải thiết kế roll-forward và reconciliation.

> **Chuyển mạch:** Ở chặng này của **Triển khai (deployment / 배포) an toàn (safety / 안전): canary, blue-green, tính năng (feature / 기능) flags và quay lui (rollback / 롤백) limits**, **Kết nối** gom các mảnh từ **20. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [Architecture decisions/System Design](./00_architecture_decisions_evolution_and_socio_technical_constraints.md), [Schema/protocol evolution](../../08_software_systems/advanced/06_schema_protocol_evolution_and_compatibility_contracts.md), [Capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md) và [Security identity rotation](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
