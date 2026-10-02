# Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Observability: từ telemetry đến suy luận có bằng chứng**. Route đi từ metrics/logs/traces → correlation and context → hypothesis narrowing → evidence-driven debugging → actionable remediation, để quan sát phục vụ chẩn đoán.

## 1. Monitoring và khả năng quan sát (observability / 관측 가능성) không hoàn toàn giống nhau

Monitoring thường trả lời các câu hỏi đã biết trước: CPU có cao không, lỗi (error / 오류) tỷ lệ (rate / 비율) có vượt ngưỡng không. khả năng quan sát (observability / 관측 가능성) rộng hơn: từ dữ liệu hệ thống phát ra, ta có thể đặt câu hỏi mới khi thất bại (failure / 실패) chưa từng biết trước.

Khả năng quan sát (observability / 관측 가능성) không được đo bằng số dashboard. Một hệ thống có hàng nghìn chỉ số (metric / 지표) nhưng thiếu correlation giữa yêu cầu (request / 요청), triển khai (deployment / 배포) và phụ thuộc (dependency / 의존성) vẫn khó gỡ lỗi (debug / 디버그).

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **1. Monitoring và khả năng quan sát (observability / 관측 가능성) không hoàn toàn giống nhau** nêu điều cần giải thích; **2. Telemetry là bằng chứng (evidence / 증거), không phải sự thật trọn vẹn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Metrics dùng cho trend và alert** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Telemetry là bằng chứng (evidence / 증거), không phải sự thật trọn vẹn

Metrics, logs, traces và events đều là phép quan sát có độ lệch (bias / 편향). chỉ số (metric / 지표) aggregate làm mất detail. Log có thể thiếu ngữ cảnh (context / 맥락). dấu vết (trace / 추적) có sampling. sự kiện (event / 이벤트) có thể bị drop. Vì vậy khi hai nguồn mâu thuẫn, không nên chọn nguồn “quen dùng”; phải hiểu ngữ nghĩa (semantics / 의미론) thu thập.

Một chỉ số (metric / 지표) CPU 40% trung bình nút (node / 노드) không phủ định việc một bộ chứa (container / 컨테이너) bị CPU throttling. Average độ trễ (latency / 지연 시간) 100 ms không phủ định p99 là 3 giây. Telemetry luôn cần dimensions và phân phối (distribution / 분포) phù hợp.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **2. Telemetry là bằng chứng (evidence / 증거), không phải sự thật trọn vẹn** nêu điều cần giải thích; **3. Metrics dùng cho trend và alert** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Logs cần cấu trúc (structure / 구조) và ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Metrics dùng cho trend và alert

Chỉ số (metric / 지표) phù hợp để theo dõi quantity theo thời gian. Counter tăng đơn điệu cho sự kiện (event / 이벤트) count; gauge biểu diễn giá trị (value / 값) hiện tại; histogram/phân phối (distribution / 분포) giữ phân bố độ trễ (latency / 지연 시간)/kích thước (size / 크기) tốt hơn chỉ average.

Cardinality là sự đánh đổi (trade-off / 트레이드오프) quan trọng. Label như `status_code`, `region`, `service` hữu ích. Label như `user_id` hoặc yêu cầu (request / 요청) UUID có cardinality cực cao và làm chỉ số (metric / 지표) hệ thống (system / 시스템) tốn tài nguyên (resource / 자원). Detail per-request phù hợp hơn với dấu vết (trace / 추적)/log.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **4. Logs cần cấu trúc (structure / 구조) và ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **3. Metrics dùng cho trend và alert** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. phân tán (distributed / 분산) dấu vết (trace / 추적) nối nhân quả (causal / 인과적) đường dẫn (path / 경로) của yêu cầu (request / 요청)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Logs cần cấu trúc (structure / 구조) và ngữ cảnh (context / 맥락)

Structured log giúp machine truy vấn (query / 쿼리) trường dữ liệu (field / 필드) thay vì parse văn bản (text / 텍스트) tự do. Một log entry hữu ích thường có timestamp chuẩn, dịch vụ (service / 서비스)/phiên bản (version / 버전), severity, yêu cầu (request / 요청)/dấu vết (trace / 추적) correlation và lĩnh vực (domain / 도메인) ngữ cảnh (context / 맥락) phù hợp.

Không log secret/đơn vị từ (token / 토큰)/PII tùy tiện. Logging là dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) có bảo mật (security / 보안)/privacy chi phí (cost / 비용). “Log mọi thứ để gỡ lỗi (debug / 디버그)” có thể tạo rủi ro lớn hơn sự cố (incident / 인시던트) ban đầu.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **4. Logs cần cấu trúc (structure / 구조) và ngữ cảnh (context / 맥락)** xác định đầu vào; **5. phân tán (distributed / 분산) dấu vết (trace / 추적) nối nhân quả (causal / 인과적) đường dẫn (path / 경로) của yêu cầu (request / 요청)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. Events và thay đổi (change / 변경) telemetry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. phân tán (distributed / 분산) dấu vết (trace / 추적) nối nhân quả (causal / 인과적) đường dẫn (path / 경로) của yêu cầu (request / 요청)

Dấu vết (trace / 추적) mô tả yêu cầu (request / 요청) đi qua nhiều span. Nó giúp thấy thời gian nằm ở dịch vụ (service / 서비스) nào, downstream lời gọi (call / 호출) nào và thử lại (retry / 재시도) có xảy ra không. ngữ cảnh dấu vết (trace context / 추적 컨텍스트) phải propagate qua ranh giới (boundary / 경계); nếu proxy/message hàng đợi (queue / 큐) làm mất ngữ cảnh (context / 맥락), đồ thị (graph / 그래프) bị đứt.

Dấu vết (trace / 추적) không thay chỉ số (metric / 지표). Sampling có thể bỏ yêu cầu (request / 요청) hiếm; chỉ số (metric / 지표) vẫn tốt để phát hiện xu hướng. Hai loại tín hiệu (signal / 신호) bổ sung nhau.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **5. phân tán (distributed / 분산) dấu vết (trace / 추적) nối nhân quả (causal / 인과적) đường dẫn (path / 경로) của yêu cầu (request / 요청)** xác định đầu vào; **6. Events và thay đổi (change / 변경) telemetry** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **7. RED và USE như khung hỏi, không phải luật thuộc lòng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Events và thay đổi (change / 변경) telemetry

Triển khai (deployment / 배포), cấu hình (config / 설정) cập nhật (update / 업데이트), nút (node / 노드) drain, autoscaler hành động (action / 동작) và certificate rotation là sự kiện (event / 이벤트) có giá trị cao. Overlay thay đổi (change / 변경) sự kiện (event / 이벤트) lên độ trễ (latency / 지연 시간)/lỗi (error / 오류) chart thường rút ngắn điều tra.

Một nền tảng (platform / 플랫폼) nên làm thay đổi (change / 변경) sự kiện (event / 이벤트) tự động thay vì dựa vào người deploy nhớ ghi chú.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **7. RED và USE như khung hỏi, không phải luật thuộc lòng** tiếp nhận điểm tựa từ **6. Events và thay đổi (change / 변경) telemetry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Alert phải gắn với hành động (action / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. RED và USE như khung hỏi, không phải luật thuộc lòng

Với request-serving dịch vụ (service / 서비스), tỷ lệ (rate / 비율), Errors, Duration giúp bắt đầu từ user-facing hành vi (behavior / 동작). Với tài nguyên (resource / 자원), Utilization, Saturation, Errors giúp tìm bottleneck. Nhưng khung phần mềm (framework / 프레임워크) chỉ là câu hỏi mở đầu.

Ví dụ CPU utilization thấp nhưng run hàng đợi (queue / 큐) cao do quota/throttling cần bằng chứng (evidence / 증거) khác. cơ sở dữ liệu (database / 데이터베이스) độ trễ (latency / 지연 시간) cao có thể đến từ tranh chấp khóa (lock contention / 잠금 경합) dù CPU/lưu trữ (storage / 저장소) chỉ số (metric / 지표) bình thường.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **8. Alert phải gắn với hành động (action / 동작)** tiếp nhận điểm tựa từ **7. RED và USE như khung hỏi, không phải luật thuộc lòng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Dashboard là map, không phải investigation engine duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Alert phải gắn với hành động (action / 동작)

Alert tốt nói có người dùng (user / 사용자)/độ tin cậy (reliability / 신뢰성) rủi ro (risk / 위험) và người nhận có hành động (action / 동작) hợp lý. Alert “CPU > 80% 5 phút” có thể không actionable nếu dịch vụ (service / 서비스) vẫn khỏe và autoscaler đang làm việc.

Alert nên ưu tiên symptom gần SLO/người dùng (user / 사용자) impact, sau đó dùng lower-level telemetry để chẩn đoán. Cause-based alert vẫn hữu ích với điều kiện (condition / 조건) chắc chắn cần hành động (action / 동작) như disk sắp đầy hoặc certificate sắp hết hạn.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **9. Dashboard là map, không phải investigation engine duy nhất** tiếp nhận điểm tựa từ **8. Alert phải gắn với hành động (action / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Evidence-driven debugging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Dashboard là map, không phải investigation engine duy nhất

Dashboard chuẩn giúp dùng chung (shared / 공유) ngữ cảnh (context / 맥락): traffic, errors, độ trễ (latency / 지연 시간), saturation, triển khai (deployment / 배포) marker. Nhưng sự cố (incident / 인시던트) mới có thể cần truy vấn (query / 쿼리) ad-hoc. nền tảng (platform / 플랫폼) khả năng quan sát (observability / 관측 가능성) nên cho phép đi từ overview → dịch vụ (service / 서비스) → dấu vết (trace / 추적)/log/tài nguyên (resource / 자원) bằng dùng chung (shared / 공유) identifiers.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **9. Dashboard là map, không phải investigation engine duy nhất** nêu điều cần giải thích; **10. Evidence-driven debugging** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Instrumentation có chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Evidence-driven debugging

Quy trình tốt bắt đầu bằng câu hỏi có thể bác bỏ. “Có phải rollout mới gây lỗi không?” kiểm tra triển khai (deployment / 배포) thời gian (time / 시간) và phiên bản (version / 버전) dimension. “Có phải downstream DB chậm?” xem dấu vết (trace / 추적) span, DB độ trễ (latency / 지연 시간)/pool saturation. “Có phải nút (node / 노드) pressure?” xem pod phân phối (distribution / 분포), throttling, bộ nhớ (memory / 메모리) pressure.

Mỗi bước nên giảm tìm kiếm (search / 검색) không gian (space / 공간). Tránh nhảy sang restart/quy mô (scale / 규모) nếu chưa có bằng chứng, trừ khi khôi phục (recovery / 복구) priority buộc phải hành động ngay.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **10. Evidence-driven debugging** nêu điều cần giải thích; **11. Instrumentation có chi phí (cost / 비용)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. OpenTelemetry như ngữ nghĩa (semantic / 의미적) tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Instrumentation có chi phí (cost / 비용)

Telemetry tiêu CPU/mạng (network / 네트워크)/lưu trữ (storage / 저장소) và chi phí (cost / 비용) tài chính. High-cardinality logs/traces có thể đắt hơn ứng dụng (application / 애플리케이션). Sampling và retention cần dựa trên mục tiêu điều tra/compliance.

Đừng tối ưu chi phí (cost / 비용) bằng cách xóa tín hiệu (signal / 신호) quan trọng nhất cho sự cố (incident / 인시던트) hiếm. Tốt hơn là phân tier retention, động (dynamic / 동적) sampling và giữ exemplar/correlation.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **12. OpenTelemetry như ngữ nghĩa (semantic / 의미적) tầng (layer / 계층)** tiếp nhận điểm tựa từ **11. Instrumentation có chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. cấp cao (senior / 시니어) ghi chú (note / 노트): khả năng quan sát (observability / 관측 가능성) là thiết kế giao diện (interface / 인터페이스) cho thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. OpenTelemetry như ngữ nghĩa (semantic / 의미적) tầng (layer / 계층)

OpenTelemetry cung cấp chuẩn instrumentation/telemetry chuỗi xử lý (pipeline / 파이프라인) cho traces, metrics và logs trong nhiều hệ sinh thái. Giá trị lớn nằm ở portability và ngữ nghĩa (semantic / 의미적) convention, không phải “cài collector là có khả năng quan sát (observability / 관측 가능성)”. ứng dụng (application / 애플리케이션) vẫn phải tạo span/chỉ số (metric / 지표) có meaning đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **13. cấp cao (senior / 시니어) ghi chú (note / 노트): khả năng quan sát (observability / 관측 가능성) là thiết kế giao diện (interface / 인터페이스) cho thất bại (failure / 실패)** tiếp nhận điểm tựa từ **12. OpenTelemetry như ngữ nghĩa (semantic / 의미적) tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Telemetry chuỗi xử lý (pipeline / 파이프라인) cũng là một hệ thống phân tán (distributed system / 분산 시스템) có thể thất bại (fail / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. cấp cao (senior / 시니어) ghi chú (note / 노트): khả năng quan sát (observability / 관측 가능성) là thiết kế giao diện (interface / 인터페이스) cho thất bại (failure / 실패)

Khi thiết kế dịch vụ (service / 서비스), hãy hỏi trước: nếu yêu cầu (request / 요청) chậm, bằng chứng (evidence / 증거) nào phân biệt app CPU, DB, mạng (network / 네트워크) và thử lại (retry / 재시도)? Nếu triển khai (deployment / 배포) xấu, phiên bản (version / 버전) có dimension trong chỉ số (metric / 지표) không? Nếu hàng đợi (queue / 큐) backlog, có chỉ số (metric / 지표) age/độ sâu (depth / 깊이) không? Nếu customer báo một yêu cầu (request / 요청) lỗi, có correlation identifier nào truy ra không?

Khả năng quan sát (observability / 관측 가능성) tốt được thiết kế cùng hệ thống (system / 시스템), không phải gắn dashboard sau khi môi trường vận hành (production / 운영 환경) đã khó hiểu.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **13. cấp cao (senior / 시니어) ghi chú (note / 노트): khả năng quan sát (observability / 관측 가능성) là thiết kế giao diện (interface / 인터페이스) cho thất bại (failure / 실패)** xác định đầu vào; **14. Telemetry chuỗi xử lý (pipeline / 파이프라인) cũng là một hệ thống phân tán (distributed system / 분산 시스템) có thể thất bại (fail / 실패)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **15. Sampling phải biết câu hỏi cần trả lời** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Telemetry chuỗi xử lý (pipeline / 파이프라인) cũng là một hệ thống phân tán (distributed system / 분산 시스템) có thể thất bại (fail / 실패)

Ứng dụng (application / 애플리케이션) phát chỉ số (metric / 지표)/log/dấu vết (trace / 추적) nhưng tín hiệu (signal / 신호) thường còn đi qua tác nhân (agent / 에이전트), collector, hàng đợi (queue / 큐), mạng (network / 네트워크) và backend lưu trữ. Vì vậy “không thấy log” có ít nhất hai khả năng: sự kiện (event / 이벤트) không xảy ra hoặc telemetry đường dẫn (path / 경로) làm mất sự kiện (event / 이벤트).

Nền tảng (platform / 플랫폼) cần quan sát chính khả năng quan sát (observability / 관측 가능성) chuỗi xử lý (pipeline / 파이프라인): hàng đợi (queue / 큐)/backpressure, dropped spans/logs, export lỗi (error / 오류), backend ingestion độ trễ (latency / 지연 시간) và sampling chính sách (policy / 정책). Nếu collector quá tải trong đúng lúc sự cố (incident / 인시던트) traffic spike, bằng chứng (evidence / 증거) quý giá nhất có thể bị mất.

Đây là lý do telemetry chuỗi xử lý (pipeline / 파이프라인) cần sức chứa (capacity / 용량) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론), không nên được coi là hệ thống phụ “không thể lỗi”.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **14. Telemetry chuỗi xử lý (pipeline / 파이프라인) cũng là một hệ thống phân tán (distributed system / 분산 시스템) có thể thất bại (fail / 실패)** xác định đầu vào; **15. Sampling phải biết câu hỏi cần trả lời** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. Percentile không cộng và không average đơn giản qua dịch vụ (service / 서비스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Sampling phải biết câu hỏi cần trả lời

Head sampling quyết định giữ dấu vết (trace / 추적) từ đầu yêu cầu (request / 요청), rẻ và đơn giản nhưng có thể bỏ rare lỗi (error / 오류) trước khi biết yêu cầu (request / 요청) sẽ lỗi. Tail sampling quyết định sau khi thấy nhiều span/kết quả, có thể ưu tiên lỗi (error / 오류)/slow dấu vết (trace / 추적) nhưng cần buffering/trạng thái (state / 상태) và tăng độ phức tạp (complexity / 복잡도).

Không có một tỷ lệ sampling tốt cho mọi dịch vụ (service / 서비스). High-volume healthy traffic có thể mẫu (sample / 표본) thấp; lỗi (error / 오류)/bảo mật (security / 보안)/trọng yếu (critical / 중요) giao dịch (transaction / 트랜잭션) có thể giữ nhiều hơn. Quan trọng là biết tín hiệu (signal / 신호) nào vẫn đầy đủ — thường chỉ số (metric / 지표) aggregate — và tín hiệu (signal / 신호) nào chỉ đại diện mẫu (sample / 표본).

Khi điều tra “không có dấu vết (trace / 추적) của yêu cầu (request / 요청) lỗi”, trước hết kiểm tra sampling/propagation trước khi kết luận yêu cầu (request / 요청) chưa vào dịch vụ (service / 서비스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **16. Percentile không cộng và không average đơn giản qua dịch vụ (service / 서비스)** tiếp nhận điểm tựa từ **15. Sampling phải biết câu hỏi cần trả lời** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Clock và timestamp có thể làm nhân quả (causal / 인과적) thứ tự (order / 순서) khó đọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Percentile không cộng và không average đơn giản qua dịch vụ (service / 서비스)

Nếu dịch vụ (service / 서비스) A p99 = 200 ms và B p99 = 300 ms, không thể kết luận end-to-end p99 = 500 ms. Hai percentile có thể đến từ các yêu cầu (request / 요청) khác nhau. Tương tự average của p99 giữa nhiều instance không tạo p99 toàn fleet.

Histogram/phân phối (distribution / 분포) giữ count theo bucket cho phép aggregate đúng hơn trong nhiều hệ thống. Khi dashboard hiển thị percentile, operator cần biết percentile được tính từ raw events, histogram merge hay average của precomputed percentile.

Đây là giả định (assumption / 가정) quan trọng vì tail độ trễ (latency / 지연 시간) thường quyết định SLO.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **17. Clock và timestamp có thể làm nhân quả (causal / 인과적) thứ tự (order / 순서) khó đọc** tiếp nhận điểm tựa từ **16. Percentile không cộng và không average đơn giản qua dịch vụ (service / 서비스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Correlation ID không thay ngữ cảnh dấu vết (trace context / 추적 컨텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Clock và timestamp có thể làm nhân quả (causal / 인과적) thứ tự (order / 순서) khó đọc

Phân tán (distributed / 분산) dấu vết (trace / 추적)/log dựa vào timestamp từ nhiều host/tiến trình (process / 프로세스). Clock skew nhỏ có thể làm span trông như child bắt đầu trước parent hoặc log thứ tự (order / 순서) lộn xộn. giao thức (protocol / 프로토콜) tracing thường có parent/child quan hệ (relation / 관계) giúp lập luận (reasoning / 추론) tốt hơn chỉ sort timestamp.

Thời gian (time / 시간) synchronization vẫn quan trọng cho sự cố (incident / 인시던트) timeline, certificate và kiểm tra (audit / 감사). Nhưng khi hai log lệch vài trăm mili giây, đừng suy luận causality chỉ từ timestamp tuyệt đối nếu có dấu vết (trace / 추적)/sự kiện (event / 이벤트) quan hệ (relation / 관계) mạnh hơn.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **18. Correlation ID không thay ngữ cảnh dấu vết (trace context / 추적 컨텍스트)** tiếp nhận điểm tựa từ **17. Clock và timestamp có thể làm nhân quả (causal / 인과적) thứ tự (order / 순서) khó đọc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Cardinality explosion thường đến từ dimension tưởng như vô hại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Correlation ID không thay ngữ cảnh dấu vết (trace context / 추적 컨텍스트)

Một yêu cầu (request / 요청) ID tự tạo giúp tìm kiếm (search / 검색) log nhưng thường chỉ là opaque label. ngữ cảnh dấu vết (trace context / 추적 컨텍스트) còn mang dấu vết (trace / 추적)/span relationship và sampling trạng thái (state / 상태) qua hop. Hai thứ có thể cùng tồn tại; nền tảng (platform / 플랫폼) nên chuẩn hóa propagation qua HTTP, messaging và background tác vụ (task / 작업).

Đặc biệt với asynchronous hàng đợi (queue / 큐), vòng đời yêu cầu (request lifecycle / 요청 생명주기) không còn một ngăn xếp lời gọi (call stack / 호출 스택) đồng bộ. Message ID, dấu vết (trace / 추적)/link và nghiệp vụ (business / 비즈니스) thực thể (entity / 엔터티) ID có vai trò khác nhau. Không nên nhét tất cả vào một `correlation_id` rồi kỳ vọng truy vấn (query / 쿼리) nào cũng dễ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **19. Cardinality explosion thường đến từ dimension tưởng như vô hại** tiếp nhận điểm tựa từ **18. Correlation ID không thay ngữ cảnh dấu vết (trace context / 추적 컨텍스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Exemplars nối aggregate chỉ số (metric / 지표) với yêu cầu (request / 요청) cụ thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Cardinality explosion thường đến từ dimension tưởng như vô hại

Label `endpoint` có thể an toàn nếu chỉ vài tuyến (route / 경로) template như `/orders/{id}`. Nhưng nếu instrumentation dùng raw URL `/orders/12345`, mỗi ID tạo series mới. Tương tự lỗi (error / 오류) message nguyên văn, SQL văn bản (text / 텍스트) hoặc người dùng (user / 사용자) ID.

Cardinality cao làm bộ nhớ (memory / 메모리)/chỉ mục (index / 인덱스)/truy vấn (query / 쿼리) chi phí (cost / 비용) tăng và có thể khiến backend drop dữ liệu (data / 데이터) hoặc rate-limit đúng lúc sự cố (incident / 인시던트). Instrumentation nên normalize dimension và để detail high-cardinality sang dấu vết (trace / 추적)/log.

Nền tảng (platform / 플랫폼) khả năng quan sát (observability / 관측 가능성) cần lint/convention để ngăn lỗi này sớm thay vì chữa bill/backend outage sau đó.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **20. Exemplars nối aggregate chỉ số (metric / 지표) với yêu cầu (request / 요청) cụ thể** tiếp nhận điểm tựa từ **19. Cardinality explosion thường đến từ dimension tưởng như vô hại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. cấp cao (senior / 시니어) walkthrough: dashboard im lặng trong lúc người dùng (user / 사용자) báo lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Exemplars nối aggregate chỉ số (metric / 지표) với yêu cầu (request / 요청) cụ thể

Chỉ số (metric / 지표) histogram cho thấy p99/slow bucket nhưng không nói yêu cầu (request / 요청) nào. Exemplar có thể gắn một mẫu (sample / 표본) dấu vết (trace / 추적) ID vào bucket/điểm (point / 지점), cho phép drill-down từ aggregate anomaly sang dấu vết (trace / 추적) cụ thể mà không biến chỉ số (metric / 지표) label thành high-cardinality.

Đây là mẫu (pattern / 패턴) hữu ích cho nhà phát triển (developer / 개발자) experience: dashboard độ trễ (latency / 지연 시간) tăng → click exemplar → dấu vết (trace / 추적) → downstream span → log tương ứng. Correlation tốt giảm thời gian chuyển công cụ (tool / 도구) và giữ nhân quả (causal / 인과적) ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **21. cấp cao (senior / 시니어) walkthrough: dashboard im lặng trong lúc người dùng (user / 사용자) báo lỗi** tiếp nhận điểm tựa từ **20. Exemplars nối aggregate chỉ số (metric / 지표) với yêu cầu (request / 요청) cụ thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Missing dữ liệu (data / 데이터) khác zero và khác healthy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. cấp cao (senior / 시니어) walkthrough: dashboard im lặng trong lúc người dùng (user / 사용자) báo lỗi

Giả sử hỗ trợ (support / 지원) nhận nhiều complaint nhưng lỗi (error / 오류) dashboard không tăng. Có ba nhóm hypothesis: SLI/chỉ số (metric / 지표) không bao phủ thất bại (failure / 실패) nghiệp vụ (business / 비즈니스); telemetry chuỗi xử lý (pipeline / 파이프라인)/drop lỗi; hoặc complaint nằm ở subset dimension bị aggregate che.

Kiểm tra raw edge/truy cập (access / 접근) bằng chứng (evidence / 증거), telemetry exporter/collector drop chỉ số (metric / 지표), phiên bản (version / 버전)/region/tenant dimension và nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과). Nếu HTTP 200 nhưng payload chứa nghiệp vụ (business / 비즈니스) thất bại (failure / 실패), vận chuyển (transport / 전송) lỗi (error / 오류) chỉ số (metric / 지표) sẽ vẫn xanh.

Bài học là khả năng quan sát (observability / 관측 가능성) chỉ tốt bằng ngữ nghĩa (semantics / 의미론) đã instrument. “Dashboard xanh” không phải bằng chứng người dùng (user / 사용자) experience xanh nếu sensor đo sai đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **21. cấp cao (senior / 시니어) walkthrough: dashboard im lặng trong lúc người dùng (user / 사용자) báo lỗi** nêu điều cần giải thích; **22. Missing dữ liệu (data / 데이터) khác zero và khác healthy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **23. Counter reset và tiến trình (process / 프로세스) restart làm tỷ lệ (rate / 비율) truy vấn (query / 쿼리) dễ sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Missing dữ liệu (data / 데이터) khác zero và khác healthy

Một dashboard trả `0 errors` có thể nghĩa thật sự không có lỗi, nhưng cũng có thể vì exporter chết, mục tiêu (target / 대상) không scrape được hoặc truy vấn (query / 쿼리) vô tình loại bỏ series mất dữ liệu. Đây là khác biệt giữa **absence of bad events** và **absence of observations**.

Monitoring thiết kế (design / 설계) nên làm missing-data ngữ nghĩa (semantics / 의미론) tường minh (explicit / 명시적). Với chỉ số (metric / 지표) trọng yếu (critical / 중요), mất mát (loss / 손실) of tín hiệu (signal / 신호) có thể cần alert riêng. Một SLI chuỗi xử lý (pipeline / 파이프라인) không được mặc định coi missing mẫu (sample / 표본) là success nếu điều đó làm outage telemetry biến thành availability 100%.

Khi dịch vụ (service / 서비스) biến mất khỏi dashboard đúng lúc sự cố (incident / 인시던트), hãy hỏi mục tiêu (target / 대상) có còn emit không, collector có nhận không, backend có ingest không và truy vấn (query / 쿼리) có còn match label mới không trước khi kết luận dịch vụ (service / 서비스) idle.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **22. Missing dữ liệu (data / 데이터) khác zero và khác healthy** nêu điều cần giải thích; **23. Counter reset và tiến trình (process / 프로세스) restart làm tỷ lệ (rate / 비율) truy vấn (query / 쿼리) dễ sai** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. Log delivery thường không có exactly-once ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Counter reset và tiến trình (process / 프로세스) restart làm tỷ lệ (rate / 비율) truy vấn (query / 쿼리) dễ sai

Counter thường tăng đơn điệu trong thời gian tồn tại (lifetime / 수명) của tiến trình (process / 프로세스), nhưng tiến trình (process / 프로세스) restart đưa counter về 0. truy vấn (query / 쿼리) tính tỷ lệ (rate / 비율) cần hiểu reset ngữ nghĩa (semantics / 의미론); lấy chênh lệch hai mẫu (sample / 표본) thủ công có thể tạo tỷ lệ (rate / 비율) âm hoặc spike giả.

Tương tự, một fleet scale-out tạo nhiều thời gian (time / 시간) series mới. Nếu dashboard cộng raw counter không chuẩn hóa theo thời gian hoặc instance thời gian tồn tại (lifetime / 수명), số nhìn có thể thay đổi chỉ vì topology thay đổi chứ nghiệp vụ (business / 비즈니스) traffic không đổi.

Operational lesson là biết chỉ số (metric / 지표) kiểu (type / 타입) và vòng đời (lifecycle / 생명주기). Dashboard formula là mã (code / 코드); nó cần rà soát (review / 검토), kiểm thử (test / 테스트) với restart/gap và phiên bản (version / 버전) cùng ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약) giống ứng dụng (application / 애플리케이션) lô-gic (logic / 논리) quan trọng khác.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **23. Counter reset và tiến trình (process / 프로세스) restart làm tỷ lệ (rate / 비율) truy vấn (query / 쿼리) dễ sai** xác định đầu vào; **24. Log delivery thường không có exactly-once ngữ nghĩa (semantics / 의미론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **25. Telemetry lược đồ (schema / 스키마) cũng tiến hóa như API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Log delivery thường không có exactly-once ngữ nghĩa (semantics / 의미론)

Tác nhân (agent / 에이전트)/collector có thể buffer rồi thử lại (retry / 재시도) khi backend tạm lỗi. Điều này tốt cho durability nhưng có thể tạo duplicate log. mạng (network / 네트워크)/thử lại (retry / 재시도)/batching cũng có thể làm sự kiện (event / 이벤트) tới backend khác thứ tự timestamp hoặc ingestion thứ tự (order / 순서).

Vì vậy đếm nghiệp vụ (business / 비즈니스) sự kiện (event / 이벤트) bằng log line cần cẩn thận. Nếu một payment success log bị gửi lại hai lần, truy vấn (query / 쿼리) `count()` không nhất thiết bằng số payment thật. Với kiểm tra (audit / 감사)/nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) quan trọng, sự kiện (event / 이벤트) cần stable định danh (identity / 식별자)/deduplication ngữ nghĩa (semantics / 의미론) hoặc nguồn (source / 소스) dữ liệu authoritative hơn.

Log là bằng chứng (evidence / 증거) tuyệt vời nhưng không nên vô thức biến thành giao dịch (transaction / 트랜잭션) ledger nếu chuỗi xử lý (pipeline / 파이프라인) không có đặc tả hợp đồng (contract / 계약) tương ứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **25. Telemetry lược đồ (schema / 스키마) cũng tiến hóa như API** tiếp nhận điểm tựa từ **24. Log delivery thường không có exactly-once ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Observer tác động (effect / 효과): instrumentation có thể làm tải công việc (workload / 워크로드) thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Telemetry lược đồ (schema / 스키마) cũng tiến hóa như API

Đổi tên chỉ số (metric / 지표), label, log trường dữ liệu (field / 필드) hoặc span attribute có thể làm dashboard/alert/truy vấn (query / 쿼리) im lặng mà ứng dụng (application / 애플리케이션) vẫn chạy. Nếu rollout ứng dụng (application / 애플리케이션) và dashboard không coordinated, một phần fleet dùng lược đồ (schema / 스키마) cũ, phần khác lược đồ (schema / 스키마) mới, aggregate có thể double-count hoặc bỏ sót.

Dùng chung (shared / 공유) ngữ nghĩa (semantic / 의미적) convention cần phiên bản (version / 버전)/di chuyển (migration / 마이그레이션) cửa sổ (window / 윈도우). Có thể emit old+new trường dữ liệu (field / 필드) tạm thời, cập nhật (update / 업데이트) truy vấn (query / 쿼리) trước rồi mới remove old, hoặc dùng recording/translation tầng (layer / 계층) tùy hệ thống (system / 시스템).

Đây là một tính tương thích (compatibility / 호환성) bài toán (problem / 문제): khả năng quan sát (observability / 관측 가능성) bên tiêu thụ (consumer / 소비자) cũng là bên tiêu thụ (consumer / 소비자) của telemetry API.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **26. Observer tác động (effect / 효과): instrumentation có thể làm tải công việc (workload / 워크로드) thay đổi** tiếp nhận điểm tựa từ **25. Telemetry lược đồ (schema / 스키마) cũng tiến hóa như API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Sampling chính sách (policy / 정책) có thể độ lệch (bias / 편향) chính thất bại (failure / 실패) muốn tìm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Observer tác động (effect / 효과): instrumentation có thể làm tải công việc (workload / 워크로드) thay đổi

Tracing mọi yêu cầu (request / 요청) với payload lớn, synchronous log flush hoặc stack-profile quá nặng có thể tăng CPU, I/O và độ trễ (latency / 지연 시간). Trong sự cố (incident / 인시던트), bật gỡ lỗi (debug / 디버그) log toàn fleet đôi khi làm disk/mạng (network / 네트워크) pressure nặng thêm và che nguyên nhân gốc (root cause / 근본 원인) ban đầu.

Instrumentation cần ngân sách (budget / 예산) và activation phạm vi (scope / 범위). gỡ lỗi (debug / 디버그) chế độ (mode / 모드) nên có TTL, sampling hoặc targeted cohort khi có thể. Một diagnostic hành động (action / 동작) tốt luôn hỏi thêm: bằng chứng (evidence / 증거) mới tạo ra có làm thay đổi hệ thống (system / 시스템) đủ lớn để invalidate observation không?

Điều này đặc biệt quan trọng với profiling, packet capture và verbose logging trên đường dẫn (path / 경로) latency-sensitive.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **27. Sampling chính sách (policy / 정책) có thể độ lệch (bias / 편향) chính thất bại (failure / 실패) muốn tìm** tiếp nhận điểm tựa từ **26. Observer tác động (effect / 효과): instrumentation có thể làm tải công việc (workload / 워크로드) thay đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Black-box và white-box telemetry trả lời hai phía khác nhau của đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Sampling chính sách (policy / 정책) có thể độ lệch (bias / 편향) chính thất bại (failure / 실패) muốn tìm

Nếu sampling quyết định dựa trên độ trễ (latency / 지연 시간) threshold, lỗi (error / 오류) mã (code / 코드) hoặc tenant, dataset giữ lại không còn đại diện traffic tổng thể. Điều đó không xấu nếu mục tiêu là debugging rare thất bại (failure / 실패), nhưng không được dùng mẫu (sample / 표본) đó để ước lượng tỷ lệ toàn bộ người dùng (user / 사용자) mà không biết selection độ lệch (bias / 편향).

Tail sampling còn phụ thuộc việc dấu vết (trace / 추적) hoàn thành và collector có đủ buffer. Trong overload, slow dấu vết (trace / 추적) có thể bị drop do bộ nhớ (memory / 메모리) pressure đúng lúc ta muốn giữ chúng nhất.

Một khả năng quan sát (observability / 관측 가능성) nền tảng (platform / 플랫폼) trưởng thành tách use trường hợp (case / 사례): chỉ số (metric / 지표) đầy đủ cho population-level tỷ lệ (rate / 비율)/SLO, sampled traces cho nhân quả (causal / 인과적) detail, và chính sách (policy / 정책) rõ về độ lệch (bias / 편향) của mẫu (sample / 표본).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **28. Black-box và white-box telemetry trả lời hai phía khác nhau của đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **27. Sampling chính sách (policy / 정책) có thể độ lệch (bias / 편향) chính thất bại (failure / 실패) muốn tìm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Stale telemetry có thể nguy hiểm hơn missing telemetry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Black-box và white-box telemetry trả lời hai phía khác nhau của đặc tả hợp đồng (contract / 계약)

White-box chỉ số (metric / 지표) nhìn từ bên trong dịch vụ (service / 서비스): hàng đợi (queue / 큐), luồng thực thi (thread / 스레드) pool, GC, DB pool. Black-box probe nhìn như bên tiêu thụ (consumer / 소비자): DNS resolve được không, TLS/HTTP có trả đúng không, synthetic giao dịch (transaction / 트랜잭션) có hoàn thành không.

Một dịch vụ (service / 서비스) có nội bộ (internal / 내부) dashboard xanh nhưng edge tuyến (route / 경로) hỏng; ngược lại synthetic probe thất bại (fail / 실패) từ một region trong khi dịch vụ (service / 서비스) tiến trình (process / 프로세스) khỏe. Hai perspective không cạnh tranh mà giúp xác định ranh giới (boundary / 경계) thất bại (failure / 실패).

Với năng lực (capability / 역량) trọng yếu (critical / 중요), một số bên ngoài (external / 외부)/synthetic check giúp phát hiện lớp (class / 클래스) thất bại (failure / 실패) mà self-reported telemetry không thể thấy — đặc biệt khi chính dịch vụ (service / 서비스) hoặc telemetry tác nhân (agent / 에이전트) đã chết.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **29. Stale telemetry có thể nguy hiểm hơn missing telemetry** tiếp nhận điểm tựa từ **28. Black-box và white-box telemetry trả lời hai phía khác nhau của đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Telemetry cần priority khi chính khả năng quan sát (observability / 관측 가능성) chuỗi xử lý (pipeline / 파이프라인) quá tải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Stale telemetry có thể nguy hiểm hơn missing telemetry

Missing tín hiệu (signal / 신호) thường dễ nhận ra. Stale tín hiệu (signal / 신호) khó hơn vì dashboard vẫn có giá trị cuối cùng và người xem tưởng nó mới. bộ nhớ đệm (cache / 캐시), exporter stuck, delayed ingestion hoặc truy vấn (query / 쿼리) cửa sổ (window / 윈도우) có thể giữ “CPU 40%, replicas 10” dù actual trạng thái (state / 상태) đã đổi.

Mọi trọng yếu (critical / 중요) tín hiệu (signal / 신호) nên có freshness ngữ cảnh (context / 맥락): mẫu (sample / 표본) timestamp, scrape age, ingestion lag hoặc heartbeat phù hợp. Khi sự cố (incident / 인시던트), một bằng chứng (evidence / 증거) item không chỉ cần hỏi “giá trị là gì?” mà còn “được quan sát khi nào và từ trạng thái (state / 상태) phiên bản (version / 버전) nào?”.

Cấp cao (senior / 시니어) lập luận (reasoning / 추론) coi freshness như một dimension của bằng chứng (evidence / 증거). Dữ liệu chính xác nhưng quá cũ có thể dẫn tới hành động (action / 동작) sai giống dữ liệu sai.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **29. Stale telemetry có thể nguy hiểm hơn missing telemetry** xác định đầu vào; **30. Telemetry cần priority khi chính khả năng quan sát (observability / 관측 가능성) chuỗi xử lý (pipeline / 파이프라인) quá tải** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. khả năng quan sát (observability / 관측 가능성) backend cũng có noisy-neighbor và truy vấn (query / 쿼리) blast radius** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Telemetry cần priority khi chính khả năng quan sát (observability / 관측 가능성) chuỗi xử lý (pipeline / 파이프라인) quá tải

Khi ingestion vượt sức chứa (capacity / 용량), drop ngẫu nhiên mọi tín hiệu (signal / 신호) có thể làm mất đúng lỗi (error / 오류)/bảo mật (security / 보안) sự kiện (event / 이벤트) quan trọng trong khi giữ hàng triệu gỡ lỗi (debug / 디버그) log ít giá trị. Vì vậy overload chính sách (policy / 정책) nên phản ánh giá trị bằng chứng (evidence / 증거): SLO chỉ số (metric / 지표), kiểm tra (audit / 감사)/bảo mật (security / 보안) sự kiện (event / 이벤트) và trọng yếu (critical / 중요) lỗi (error / 오류) có thể cần durability/priority cao hơn verbose dấu vết (trace / 추적) hoặc gỡ lỗi (debug / 디버그) log.

Priority không có nghĩa mọi trọng yếu (critical / 중요) tín hiệu (signal / 신호) được giữ vô hạn. Nếu buffer không bound, khả năng quan sát (observability / 관측 가능성) tác nhân (agent / 에이전트) có thể làm ứng dụng (application / 애플리케이션)/nút (node / 노드) OOM. Cần tường minh (explicit / 명시적) hàng đợi (queue / 큐) limit, spill/durable đường dẫn (path / 경로) khi phù hợp, drop counter và degradation chính sách (policy / 정책). Điều quan trọng là khi mất dữ liệu, ta biết **loại nào bị mất, bao nhiêu và vì sao**.

Đây là admission điều khiển (control / 제어) áp dụng cho telemetry: hệ thống (system / 시스템) bảo vệ năng lực (capability / 역량) chẩn đoán cốt lõi thay vì để overload biến toàn bộ bằng chứng (evidence / 증거) thành ngẫu nhiên.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **30. Telemetry cần priority khi chính khả năng quan sát (observability / 관측 가능성) chuỗi xử lý (pipeline / 파이프라인) quá tải** xác định đầu vào; **31. khả năng quan sát (observability / 관측 가능성) backend cũng có noisy-neighbor và truy vấn (query / 쿼리) blast radius** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **32. Retention nên đi từ câu hỏi điều tra và nghĩa vụ, không từ một con số chung** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. khả năng quan sát (observability / 관측 가능성) backend cũng có noisy-neighbor và truy vấn (query / 쿼리) blast radius

Một truy vấn regex rộng trên log nhiều tháng, dashboard fan-out hàng nghìn series hoặc tenant có cardinality bùng nổ có thể làm truy vấn (query / 쿼리)/ingestion backend chậm cho người khác. Multi-tenancy của khả năng quan sát (observability / 관측 가능성) vì vậy cần quota không chỉ ở ingestion mà cả retained dữ liệu (data / 데이터), concurrent truy vấn (query / 쿼리), scan volume và cardinality.

Trong sự cố (incident / 인시던트), operator cần truy vấn (query / 쿼리) nhanh nhất đúng lúc toàn tổ chức cùng mở dashboard. sức chứa (capacity / 용량) mô hình (model / 모델) phải xét **sự cố (incident / 인시던트) tính đồng thời (concurrency / 동시성)**, không chỉ traffic ngày thường. Có thể cần precomputed/recording dữ liệu (data / 데이터) cho SLO, truy vấn (query / 쿼리) priority, per-tenant limit và isolation cho kiểm tra (audit / 감사)/trọng yếu (critical / 중요) telemetry.

Nếu khả năng quan sát (observability / 관측 가능성) backend là dùng chung (shared / 공유) phụ thuộc (dependency / 의존성) toàn công ty, một truy vấn (query / 쿼리) xấu không nên có blast radius tương đương outage monitoring toàn bộ fleet.

> **Chuyển mạch:** Trong **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **32. Retention nên đi từ câu hỏi điều tra và nghĩa vụ, không từ một con số chung** tiếp nhận điểm tựa từ **31. khả năng quan sát (observability / 관측 가능성) backend cũng có noisy-neighbor và truy vấn (query / 쿼리) blast radius** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Telemetry chi phí (cost / 비용) cần attribution theo tín hiệu (signal / 신호) driver** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Retention nên đi từ câu hỏi điều tra và nghĩa vụ, không từ một con số chung

Không phải mọi telemetry cần giữ 90 ngày ở cùng độ chi tiết. High-resolution chỉ số (metric / 지표) hữu ích cho sự cố (incident / 인시던트) gần; aggregate dài hạn hữu ích cho sức chứa (capacity / 용량)/trend. Full dấu vết (trace / 추적) có thể chỉ cần giữ ngắn, trong khi bảo mật (security / 보안)/kiểm tra (audit / 감사) bằng chứng (evidence / 증거) có retention dài hơn vì forensic/compliance.

Một retention thiết kế (design / 설계) tốt hỏi: thất bại (failure / 실패) thường được phát hiện sau bao lâu; sức chứa (capacity / 용량) cần seasonality dài bao nhiêu; kiểm tra (audit / 감사) yêu cầu gì; replay/gỡ lỗi (debug / 디버그) cần raw detail hay aggregate. Sau đó mới chọn tier hot/warm/archive hoặc downsampling. Xóa detail quá sớm làm forensic bất khả thi; giữ mọi thứ mãi mãi tăng chi phí (cost / 비용), privacy exposure và truy vấn (query / 쿼리) surface.

Retention vì vậy là sản phẩm (product / 제품)/bảo mật (security / 보안)/độ tin cậy (reliability / 신뢰성) đặc tả hợp đồng (contract / 계약), không chỉ lưu trữ (storage / 저장소) setting.

> **Chuyển mạch:** Ở chặng này của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **33. Telemetry chi phí (cost / 비용) cần attribution theo tín hiệu (signal / 신호) driver** tiếp nhận điểm tựa từ **32. Retention nên đi từ câu hỏi điều tra và nghĩa vụ, không từ một con số chung** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. cấp cao (senior / 시니어) walkthrough: sự cố (incident / 인시던트) làm khả năng quan sát (observability / 관측 가능성) chết trước ứng dụng (application / 애플리케이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Telemetry chi phí (cost / 비용) cần attribution theo tín hiệu (signal / 신호) driver

Bill khả năng quan sát (observability / 관측 가능성) thường tăng vì một số driver cụ thể: log volume, retained bytes, high-cardinality series, dấu vết (trace / 추적) span count, egress hoặc truy vấn (query / 쿼리) scan. Nếu chỉ phân bổ theo số dịch vụ (service / 서비스), nhóm (team / 팀) ít có phản hồi (feedback / 피드백) để sửa instrumentation gây chi phí (cost / 비용).

Nền tảng (platform / 플랫폼) nên expose chi phí (cost / 비용)/usage theo dịch vụ (service / 서비스) hoặc tenant ở mức đủ gần nhân quả (causal / 인과적) driver: `GB ingested`, `GB-day retained`, active series/cardinality, sampled span volume, expensive truy vấn (query / 쿼리) lớp (class / 클래스). Nhưng chi phí (cost / 비용) guardrail phải đi cùng độ tin cậy (reliability / 신뢰성) guardrail; cắt dấu vết (trace / 추적) sampling xuống gần zero để đạt ngân sách (budget / 예산) có thể phá diagnosability.

Mô hình tư duy (mental model / 사고 모델) FinOps ở đây là `question/evidence value → signal design → ingestion/retention/query cost → feedback cho owner`. Mục tiêu không phải telemetry rẻ nhất mà là **chi phí thấp nhất vẫn giữ được quyết định môi trường vận hành (production / 운영 환경) cần thiết**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khả năng quan sát (observability / 관측 가능성): từ telemetry đến suy luận có bằng chứng**, **34. cấp cao (senior / 시니어) walkthrough: sự cố (incident / 인시던트) làm khả năng quan sát (observability / 관측 가능성) chết trước ứng dụng (application / 애플리케이션)** tiếp nhận điểm tựa từ **33. Telemetry chi phí (cost / 비용) cần attribution theo tín hiệu (signal / 신호) driver** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 34. cấp cao (senior / 시니어) walkthrough: sự cố (incident / 인시던트) làm khả năng quan sát (observability / 관측 가능성) chết trước ứng dụng (application / 애플리케이션)

Giả sử bản phát hành (release / 릴리스) lỗi tạo exception vòng lặp (loop / 루프), mỗi yêu cầu (request / 요청) phát hàng trăm log line. ứng dụng (application / 애플리케이션) vẫn còn phục vụ một phần traffic nhưng log ingestion tăng 50 lần, collector hàng đợi (queue / 큐) đầy, backend truy vấn (query / 쿼리) hết thời gian chờ (timeout / 타임아웃) và on-call mất visibility. Tăng log backend vô hạn không phải fix bền vững vì chính thất bại (failure / 실패) đường dẫn (path / 경로) có amplification factor không bound.

Chuỗi nhân quả (causal chain / 인과 사슬) là `application fault → telemetry amplification → collector/backend saturation → evidence loss → recovery chậm`. Mitigation có thể rate-limit/sampling log lặp, ưu tiên lỗi (error / 오류) summary/SLO tín hiệu (signal / 신호), bảo vệ backend bằng tenant/truy vấn (query / 쿼리) quota và giữ drop counter. Sau sự cố (incident / 인시던트), instrumentation phải được sửa để một lỗi ứng dụng (application / 애플리케이션) không thể biến thành khả năng quan sát (observability / 관측 가능성) outage có blast radius lớn hơn lỗi gốc.

Đây là ví dụ rõ rằng khả năng quan sát (observability / 관측 가능성) nằm trong môi trường vận hành (production / 운영 환경) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và cần overload/thất bại (failure / 실패) thiết kế (design / 설계) giống mọi dùng chung (shared / 공유) nền tảng (platform / 플랫폼) khác.

> **Bàn giao:** Sau **34. cấp cao (senior / 시니어) walkthrough: sự cố (incident / 인시던트) làm khả năng quan sát (observability / 관측 가능성) chết trước ứng dụng (application / 애플리케이션)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
