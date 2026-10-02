# Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Fault tolerance, observability và reliability**. Route đi từ fault/error/failure → redundancy/retry/timeout → circuit breaker/bulkhead → SLI/SLO/availability → graceful degradation và chaos, để reliability được đo bằng hành vi khi hỏng.

Một hệ thống đáng tin cậy (reliable system / 신뢰성 높은 시스템) không phải là hệ thống không bao giờ hỏng. thành phần (component / 컴포넌트), mạng (network / 네트워크), disk, tiến trình (process / 프로세스), phụ thuộc (dependency / 의존성) và con người đều có thể thất bại (fail / 실패). độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) bắt đầu từ giả định đó rồi thiết kế để **thất bại (failure / 실패) được phát hiện, giới hạn phạm vi ảnh hưởng, phục hồi có thể dự đoán và vẫn giữ dịch vụ (service / 서비스) trong mục tiêu đã định lượng**.

Điểm cốt lõi là độ tin cậy (reliability / 신뢰성) không phải một collection mẫu (pattern / 패턴) như thử lại (retry / 재시도), circuit breaker hay multi-zone. Nó là lập luận (reasoning / 추론) về **thất bại (failure / 실패) mô hình (model / 모델) + bất biến (invariant / 불변식) + tài nguyên (resource / 자원) sức chứa (capacity / 용량) + khôi phục (recovery / 복구) bằng chứng (evidence / 증거)**.

## 1. Fault, lỗi (error / 오류) và thất bại (failure / 실패)

Trong dependability, ba từ thường được tách như sau:

```text
fault
→ nguyên nhân bên dưới

error
→ internal state đã sai

failure
→ service bên ngoài lệch contract
```

Ví dụ một bit flip là fault. Nếu bộ nhớ (memory / 메모리) trạng thái (state / 상태) bị corrupt thì đó là lỗi (error / 오류). Nếu checksum phát hiện corruption và yêu cầu (request / 요청) bị thử lại (retry / 재시도) từ replica khỏe, người dùng (user / 사용자) có thể chưa thấy thất bại (failure / 실패).

Phân biệt này quan trọng vì độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cố chặn propagation trước khi nội bộ (internal / 내부) lỗi (error / 오류) trở thành user-visible thất bại (failure / 실패).

> **Chuyển mạch:** Fault là nguyên nhân, error là trạng thái sai và failure là tác động lên người dùng; reliability invariant phải đo được, còn redundancy chỉ giúp khi các failure không cùng nguồn.

## 2. độ tin cậy (reliability / 신뢰성) bất biến (invariant / 불변식) phải nói bằng ngôn ngữ của người dùng

Thành phần (component / 컴포넌트) health không phải mục tiêu cuối. Một dịch vụ (service / 서비스) có thể có tất cả processes `UP` nhưng người dùng (user / 사용자) vẫn hết thời gian chờ (timeout / 타임아웃) vì hàng đợi (queue / 큐) dài hoặc phụ thuộc (dependency / 의존성) chậm.

Bất biến (invariant / 불변식) độ tin cậy (reliability / 신뢰성) nên được diễn đạt bằng kết quả quan sát được, ví dụ:

```text
99.9% request hợp lệ hoàn tất dưới 300 ms trong 30 ngày

payment đã trả success không được mất sau failover thuộc failure model

một tenant quá tải không được làm tenant khác mất toàn bộ capacity
```

Từ bất biến (invariant / 불변식) đó mới chọn SLI, hết thời gian chờ (timeout / 타임아웃), replication, bulkhead hay fallback phù hợp.

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **3. Redundancy chỉ hữu ích khi thất bại (failure / 실패) đủ độc lập** tiếp nhận điểm tựa từ **2. độ tin cậy (reliability / 신뢰성) bất biến (invariant / 불변식) phải nói bằng ngôn ngữ của người dùng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. thử lại (retry / 재시도) là tải (load / 로드) multiplier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Redundancy chỉ hữu ích khi thất bại (failure / 실패) đủ độc lập

Replication, extra instances, RAID/erasure coding và multi-zone triển khai (deployment / 배포) tạo redundancy. Nhưng hai replicas cùng rack, cùng power nguồn (source / 소스), cùng cơ sở dữ liệu (database / 데이터베이스) hoặc cùng broken triển khai (deployment / 배포) sản phẩm tạo ra (artifact / 산출물) vẫn có thể thất bại (fail / 실패) cùng lúc.

Đây là **correlated thất bại (failure / 실패)**. Vì vậy phải hỏi:

```text
replicas có cùng failure domain không?
control plane có phải shared dependency không?
config/deploy bug có lan tới mọi replica không?
corruption có được replicate không?
```

“Có ba bản sao” không đồng nghĩa ba thất bại (failure / 실패) domains độc lập.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **4. thử lại (retry / 재시도) là tải (load / 로드) multiplier** tiếp nhận điểm tựa từ **3. Redundancy chỉ hữu ích khi thất bại (failure / 실패) đủ độc lập** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. hết thời gian chờ (timeout / 타임아웃) là ngân sách (budget / 예산), không phải magic number** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. thử lại (retry / 재시도) là tải (load / 로드) multiplier

Thử lại (retry / 재시도) có thể biến transient thất bại (failure / 실패) thành success, nhưng mỗi thử lại (retry / 재시도) là một yêu cầu (request / 요청) mới. Nếu phụ thuộc (dependency / 의존성) chậm vì overload, thử lại (retry / 재시도) làm arrival tỷ lệ (rate / 비율) tăng đúng lúc dịch vụ (service / 서비스) tỷ lệ (rate / 비율) đang giảm.

Do đó thử lại (retry / 재시도) cần:

```text
bounded attempts
exponential backoff
jitter
retry budget
idempotency khi có side effect
```

Hết thời gian chờ (timeout / 타임아웃) + thử lại (retry / 재시도) mà thao tác (operation / 연산) không idempotent có thể duplicate payment/thứ tự (order / 순서). thử lại (retry / 재시도) chính sách (policy / 정책) vì vậy vừa là độ tin cậy (reliability / 신뢰성) thiết kế (design / 설계) vừa là sức chứa (capacity / 용량) thiết kế (design / 설계).

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **5. hết thời gian chờ (timeout / 타임아웃) là ngân sách (budget / 예산), không phải magic number** tiếp nhận điểm tựa từ **4. thử lại (retry / 재시도) là tải (load / 로드) multiplier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Circuit breaker không tạo sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. hết thời gian chờ (timeout / 타임아웃) là ngân sách (budget / 예산), không phải magic number

Không có hết thời gian chờ (timeout / 타임아웃), caller có thể giữ luồng thực thi (thread / 스레드)/liên kết (connection / 연결) vô hạn. hết thời gian chờ (timeout / 타임아웃) quá ngắn tạo false thất bại (failure / 실패) và thử lại (retry / 재시도) storm; quá dài giữ tài nguyên (resource / 자원) lâu và làm khôi phục (recovery / 복구) chậm.

Hết thời gian chờ (timeout / 타임아웃) nên xuất phát từ end-to-end độ trễ (latency / 지연 시간) ngân sách (budget / 예산). Nếu yêu cầu (request / 요청) còn 80 ms nhưng downstream lời gọi (call / 호출) được hết thời gian chờ (timeout / 타임아웃) 2 giây, hệ thống (system / 시스템) đã mất deadline bất biến (invariant / 불변식).

**Deadline propagation** truyền remaining ngân sách (budget / 예산) xuống các hop thay vì mỗi tầng (layer / 계층) tự reset một hết thời gian chờ (timeout / 타임아웃) đầy đủ.

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **6. Circuit breaker không tạo sức chứa (capacity / 용량)** tiếp nhận điểm tựa từ **5. hết thời gian chờ (timeout / 타임아웃) là ngân sách (budget / 예산), không phải magic number** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Bulkhead là isolation ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Circuit breaker không tạo sức chứa (capacity / 용량)

Circuit breaker tạm dừng gửi traffic tới phụ thuộc (dependency / 의존성) đang thất bại (fail / 실패) để giảm wasted công việc (work / 작업) và cho phụ thuộc (dependency / 의존성) cơ hội hồi phục. Half-open probing kiểm tra khôi phục (recovery / 복구) dần dần.

Nhưng circuit breaker không tự tăng sức chứa (capacity / 용량). Nếu thất bại (failure / 실패) do overload toàn hệ thống, vẫn cần bounded hàng đợi (queue / 큐), admission điều khiển (control / 제어), backpressure hoặc tải (load / 로드) shedding.

Một breaker reopen đồng loạt trên nhiều instances còn có thể tạo spike mới nếu không có jitter/ramp-up.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **6. Circuit breaker không tạo sức chứa (capacity / 용량)** đã nêu tiêu chí phân biệt, còn **7. Bulkhead là isolation ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. tải (load / 로드) shedding và graceful degradation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Bulkhead là isolation ranh giới (boundary / 경계)

Bulkhead tách tài nguyên (resource / 자원) pools hoặc quotas để một tải công việc (workload / 워크로드) không ăn hết tài nguyên (resource / 자원) của tải công việc (workload / 워크로드) khác.

Ví dụ background export dùng pool khác yêu cầu (request / 요청) user-facing. sự đánh đổi (trade-off / 트레이드오프) là có thể lãng phí một phần sức chứa (capacity / 용량) khi pool A rảnh nhưng pool B đầy.

Isolation chỉ có ý nghĩa nếu nó được đặt ở tài nguyên (resource / 자원) thật sự bottleneck. Hai logical queues khác nhau nhưng cùng tranh một exhausted DB pool vẫn không phải isolation đầy đủ.

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **7. Bulkhead là isolation ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **8. tải (load / 로드) shedding và graceful degradation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. khả năng quan sát (observability / 관측 가능성) là khả năng suy ra trạng thái nội bộ (internal state / 내부 상태) từ bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. tải (load / 로드) shedding và graceful degradation

Khi hệ thống (system / 시스템) gần overload, cố nhận 100% requests có thể dẫn tới 100% hết thời gian chờ (timeout / 타임아웃). Reject sớm một phần traffic đôi khi giữ phần còn lại khỏe hơn.

Graceful degradation có thể gồm stale bộ nhớ đệm (cache / 캐시), read-only chế độ (mode / 모드), bỏ optional enrichment hoặc giảm chất lượng đầu ra (output / 출력). Nhưng degradation không được bỏ tính đúng đắn (correctness / 정확성)/bảo mật (security / 보안) bất biến (invariant / 불변식) chỉ để giữ success tỷ lệ (rate / 비율).

Ví dụ phục vụ stale recommendation có thể chấp nhận được; phục vụ stale authorization chính sách (policy / 정책) có thể không chấp nhận được.

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **8. tải (load / 로드) shedding và graceful degradation** nêu điều cần giải thích; **9. khả năng quan sát (observability / 관측 가능성) là khả năng suy ra trạng thái nội bộ (internal state / 내부 상태) từ bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. SLI, SLO và SLA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. khả năng quan sát (observability / 관측 가능성) là khả năng suy ra trạng thái nội bộ (internal state / 내부 상태) từ bằng chứng (evidence / 증거)

Logs, metrics và traces là công cụ. **khả năng quan sát (observability / 관측 가능성)** là khả năng dùng đầu ra (output / 출력)/telemetry để suy ra điều gì đang xảy ra bên trong.

Các nhóm tín hiệu (signal / 신호) thường hữu ích:

```text
latency
traffic / rate
errors
saturation / queue
```

RED phù hợp service-oriented view: tỷ lệ (rate / 비율), Errors, Duration. USE phù hợp tài nguyên (resource / 자원) view: Utilization, Saturation, Errors.

Điểm quan trọng là correlation: yêu cầu (request / 요청) chậm phải nối được với hàng đợi (queue / 큐)/pool/tài nguyên (resource / 자원)/phụ thuộc (dependency / 의존성) nào thay vì chỉ nhìn từng dashboard rời rạc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **9. khả năng quan sát (observability / 관측 가능성) là khả năng suy ra trạng thái nội bộ (internal state / 내부 상태) từ bằng chứng (evidence / 증거)** nêu điều cần giải thích; **10. SLI, SLO và SLA** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. lỗi (error / 오류) ngân sách (budget / 예산) biến độ tin cậy (reliability / 신뢰성) thành một sự đánh đổi (trade-off / 트레이드오프) định lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. SLI, SLO và SLA

**SLI (service Level Indicator)** là chỉ số đo, ví dụ tỷ lệ yêu cầu (request / 요청) hợp lệ hoàn tất dưới 300 ms.

**SLO (service Level Objective)** là mục tiêu nội bộ, ví dụ 99.9% trong rolling 30-day cửa sổ (window / 윈도우).

**SLA (service Level Agreement)** là cam kết nghiệp vụ (business / 비즈니스)/bên ngoài (external / 외부) có consequence, không phải synonym của SLO.

SLO nên đo thứ người dùng (user / 사용자) thực sự quan tâm, không chỉ thành phần (component / 컴포넌트) uptime.

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **11. lỗi (error / 오류) ngân sách (budget / 예산) biến độ tin cậy (reliability / 신뢰성) thành một sự đánh đổi (trade-off / 트레이드오프) định lượng** tiếp nhận điểm tựa từ **10. SLI, SLO và SLA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Burn tỷ lệ (rate / 비율) cho biết ngân sách (budget / 예산) đang bị tiêu nhanh đến mức nào** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. lỗi (error / 오류) ngân sách (budget / 예산) biến độ tin cậy (reliability / 신뢰성) thành một sự đánh đổi (trade-off / 트레이드오프) định lượng

Nếu SLO là 99.9%, phần unreliability được phép trong cửa sổ (window / 윈도우) là **lỗi (error / 오류) ngân sách (budget / 예산)**.

Ví dụ đơn giản:

```text
30 ngày × 24 giờ × 60 phút = 43,200 phút
0.1% budget ≈ 43.2 phút tương đương full outage
```

Thực tế ngân sách (budget / 예산) có thể được tiêu bởi partial errors/độ trễ (latency / 지연 시간) chứ không chỉ full outage.

Lỗi (error / 오류) ngân sách (budget / 예산) giúp trả lời câu hỏi: hiện tại nhóm (team / 팀) còn đủ margin để tăng triển khai (deployment / 배포) rủi ro (risk / 위험) hay cần ưu tiên độ tin cậy (reliability / 신뢰성) công việc (work / 작업)?

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **12. Burn tỷ lệ (rate / 비율) cho biết ngân sách (budget / 예산) đang bị tiêu nhanh đến mức nào** tiếp nhận điểm tựa từ **11. lỗi (error / 오류) ngân sách (budget / 예산) biến độ tin cậy (reliability / 신뢰성) thành một sự đánh đổi (trade-off / 트레이드오프) định lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Availability math và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Burn tỷ lệ (rate / 비율) cho biết ngân sách (budget / 예산) đang bị tiêu nhanh đến mức nào

Nếu dịch vụ (service / 서비스) chỉ mới đi qua 10% của cửa sổ (window / 윈도우) nhưng đã tiêu 50% lỗi (error / 오류) ngân sách (budget / 예산), tốc độ tiêu ngân sách (budget / 예산) đang quá cao.

**Burn tỷ lệ (rate / 비율)** so sánh tốc độ lỗi hiện tại với tốc độ lỗi cho phép để vừa hết ngân sách (budget / 예산) đúng cuối cửa sổ (window / 윈도우).

Mô hình tư duy (mental model / 사고 모델):

```text
burn rate = 1
→ đang tiêu budget đúng tốc độ cho phép

burn rate > 1
→ nếu kéo dài sẽ hết budget sớm
```

Alert theo burn tỷ lệ (rate / 비율) thường tốt hơn alert chỉ theo lỗi (error / 오류) tỷ lệ (rate / 비율) tức thời vì nó nối symptom với SLO impact.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **12. Burn tỷ lệ (rate / 비율) cho biết ngân sách (budget / 예산) đang bị tiêu nhanh đến mức nào** cho ta quy tắc; **13. Availability math và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **14. Correlated thất bại (failure / 실패) quan trọng hơn công thức độc lập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Availability math và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)

Nếu hai independent components bắt buộc đều available và mỗi cái có availability 99.9%, combined availability gần:

```text
0.999 × 0.999 = 0.998001 ≈ 99.8001%
```

Series dependencies làm availability tổng giảm. Parallel redundancy có thể tăng availability nếu failover thật sự hoạt động và thất bại (failure / 실패) đủ độc lập.

Vì vậy độ tin cậy (reliability / 신뢰성) kiến trúc (architecture / 아키텍처) phải nhìn **phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)**, không nhìn từng thành phần (component / 컴포넌트) score riêng.

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **13. Availability math và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** cho ta quy tắc; **14. Correlated thất bại (failure / 실패) quan trọng hơn công thức độc lập** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **15. Fault containment và blast radius** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Correlated thất bại (failure / 실패) quan trọng hơn công thức độc lập

Availability multiplication chỉ đúng dưới các giả định (assumptions / 가정들) phù hợp. dùng chung (shared / 공유) DNS, dùng chung (shared / 공유) KMS, same triển khai (deployment / 배포), same region hoặc same operator mistake làm failures correlated.

Một phụ thuộc (dependency / 의존성) “99.99%” nhưng nằm trên đường găng (critical path / 임계 경로) của mọi yêu cầu (request / 요청) có thể quyết định toàn dịch vụ (service / 서비스). Một điều khiển (control / 제어) plane hiếm dùng nhưng khi thất bại (fail / 실패) lại chặn certificate renewal cho toàn fleet cũng là độ tin cậy (reliability / 신뢰성) phụ thuộc (dependency / 의존성).

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **15. Fault containment và blast radius** tiếp nhận điểm tựa từ **14. Correlated thất bại (failure / 실패) quan trọng hơn công thức độc lập** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. khôi phục (recovery / 복구) phải có trạng thái (state / 상태) mô hình (model / 모델) rõ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Fault containment và blast radius

Độ tin cậy (reliability / 신뢰성) tốt không chỉ phục hồi nhanh mà còn ngăn thất bại (failure / 실패) lan rộng.

Các ranh giới (boundary / 경계) thường dùng:

```text
zone / region
process / container
thread or worker pool
connection pool
queue
tenant quota
service ownership boundary
```

Blast radius cần được thiết kế trước sự cố (incident / 인시던트). Nếu mọi tải công việc (workload / 워크로드) dùng cùng pool/credential/điều khiển (control / 제어) plane, một lỗi nhỏ có thể trở thành systemic thất bại (failure / 실패).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **16. khôi phục (recovery / 복구) phải có trạng thái (state / 상태) mô hình (model / 모델) rõ** tiếp nhận điểm tựa từ **15. Fault containment và blast radius** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Chaos/fault injection là kiểm thử hypothesis** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. khôi phục (recovery / 복구) phải có trạng thái (state / 상태) mô hình (model / 모델) rõ

Sau failover/restart, câu hỏi không chỉ là “dịch vụ (service / 서비스) đã lên chưa?”. Cần biết trạng thái (state / 상태) nào authoritative, yêu cầu (request / 요청) nào đang in-flight, side tác động (effect / 효과) nào đã xảy ra và thử lại (retry / 재시도) có tạo duplicate không.

Độ tin cậy (reliability / 신뢰성) của stateful hệ thống (system / 시스템) vì thế nối trực tiếp với idempotency, giao dịch (transaction / 트랜잭션) durability, replication và consistency.

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **17. Chaos/fault injection là kiểm thử hypothesis** tiếp nhận điểm tựa từ **16. khôi phục (recovery / 복구) phải có trạng thái (state / 상태) mô hình (model / 모델) rõ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Chaos/fault injection là kiểm thử hypothesis

Fault injection không phải “randomly phá môi trường vận hành (production / 운영 환경)”. Một experiment tốt có:

```text
hypothesis rõ
blast-radius limit
abort condition
observability đủ
recovery expectation
```

Ví dụ: “mất một replica không làm p99 vượt X và không mất committed ghi (write / 쓰기)”. Ta inject thất bại (failure / 실패) rồi kiểm tra bất biến (invariant / 불변식) bằng bằng chứng (evidence / 증거).

Chaos không có hypothesis hoặc telemetry chỉ là tạo sự cố (incident / 인시던트) có chủ đích mà không học được gì.

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **17. Chaos/fault injection là kiểm thử hypothesis** nêu điều cần giải thích; **18. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. thất bại (failure / 실패) modes cần phân biệt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. bằng chứng vận hành (production evidence / 운영 증거)

Độ tin cậy (reliability / 신뢰성) diagnosis nên nối nhiều tầng:

```text
SLI/SLO và burn rate
request error/latency percentiles
queue depth/wait
retry attempts
rejection/load shedding
resource saturation
failover/leader/replica state
dependency health
recovery timeline
```

Một thành phần (component / 컴포넌트) “healthy” nhưng hàng đợi (queue / 큐) debt tăng vẫn có thể đang tiến tới thất bại (failure / 실패). Một outage đã hồi phục nhưng replica chưa catch up cũng chưa chắc độ tin cậy (reliability / 신뢰성) trạng thái (state / 상태) đã bình thường.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **18. bằng chứng vận hành (production evidence / 운영 증거)** nêu điều cần giải thích; **19. thất bại (failure / 실패) modes cần phân biệt** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. thất bại (failure / 실패) modes cần phân biệt

Các thất bại (failure / 실패) khác nhau cần mitigation khác nhau:

```text
transient network failure
→ retry có kiểm soát

overload
→ backpressure/admission/load shedding

correlated dependency failure
→ isolation/redundancy khác failure domain

bad deploy/config
→ staged rollout/rollback/roll-forward

state corruption
→ validation, backup/PITR, recovery
```

Dùng một mẫu (pattern / 패턴) cho mọi thất bại (failure / 실패) thường làm hệ thống khó đoán hơn.

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **20. Mô hình tư duy** gom các mảnh từ **19. thất bại (failure / 실패) modes cần phân biệt** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Mô hình tư duy

> độ tin cậy (reliability / 신뢰성) = **định nghĩa user-visible mục tiêu (objective / 목표), giả định thất bại (failure / 실패) sẽ xảy ra, giới hạn blast radius, giữ tài nguyên (resource / 자원) trong vùng an toàn, phát hiện deviation bằng bằng chứng (evidence / 증거) và phục hồi trạng thái (state / 상태) theo đặc tả hợp đồng (contract / 계약) có thể kiểm chứng.** thử lại (retry / 재시도), redundancy hay circuit breaker chỉ là mechanisms phục vụ bất biến (invariant / 불변식) đó.

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Kết nối** gom các mảnh từ **20. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [Distributed partial failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [Idempotency](../08_software_systems/04_time_serialization_and_idempotency.md), [Performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md), [Advanced capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [Request path và retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [Debugging/containment xuyên tầng](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
