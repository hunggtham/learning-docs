# SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **SLI, SLO, error budget và capacity**. Route đi từ user journey → SLI → SLO target → error-budget policy → capacity and delivery trade-offs, để reliability trở thành mục tiêu điều hành.

## 1. độ tin cậy (reliability / 신뢰성) không thể chỉ là “càng cao càng tốt”

Nếu mục tiêu mơ hồ là 100% uptime, mọi thay đổi đều có thể bị coi là nguy hiểm và chi phí (cost / 비용) sẽ tăng vô hạn. SRE đưa độ tin cậy (reliability / 신뢰성) về bài toán có đặc tả hợp đồng (contract / 계약) đo được: dịch vụ (service / 서비스) nào quan trọng, người dùng (user / 사용자) nhìn thấy hành vi (behavior / 동작) nào, mức không hoàn hảo nào chấp nhận được và trong cửa sổ nào.

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **2. SLI phải gần người dùng (user / 사용자) experience** tiếp nhận điểm tựa từ **1. độ tin cậy (reliability / 신뢰성) không thể chỉ là “càng cao càng tốt”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. SLO là mục tiêu trong cửa sổ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. SLI phải gần người dùng (user / 사용자) experience

Chỉ báo mức dịch vụ (service Level Indicator — SLI) là phép đo. Ví dụ availability SLI không nên đơn giản là tiến trình (process / 프로세스) uptime; tiến trình (process / 프로세스) sống nhưng trả 500 vẫn không phục vụ người dùng (user / 사용자).

Một request-based SLI có thể là:

```text
good events / valid events
```

“Good” phải định nghĩa theo đặc tả hợp đồng (contract / 계약): status mã (code / 코드), độ trễ (latency / 지연 시간) threshold và loại yêu cầu (request / 요청). Một số 4xx do máy khách (client / 클라이언트) sai có thể không tính là dịch vụ (service / 서비스) thất bại (failure / 실패); một số nghiệp vụ (business / 비즈니스) phản hồi (response / 응답) HTTP 200 nhưng nội dung thất bại vẫn phải tính xấu.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **3. SLO là mục tiêu trong cửa sổ** tiếp nhận điểm tựa từ **2. SLI phải gần người dùng (user / 사용자) experience** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. lỗi (error / 오류) ngân sách (budget / 예산) biến độ tin cậy (reliability / 신뢰성) thành ràng buộc (constraint / 제약조건) cho thay đổi (change / 변경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. SLO là mục tiêu trong cửa sổ

Mục tiêu mức dịch vụ (service Level Objective — SLO) nói SLI cần đạt bao nhiêu trong khoảng thời gian. Ví dụ 99.9% yêu cầu (request / 요청) hợp lệ thành công trong 30 ngày.

99.9% không phải “chỉ khác 99% một chút”. lỗi (error / 오류) ngân sách (budget / 예산) giảm khoảng mười lần. Vì vậy số SLO phải gắn với người dùng (user / 사용자)/nghiệp vụ (business / 비즈니스) need, kiến trúc (architecture / 아키텍처) và chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **3. SLO là mục tiêu trong cửa sổ** đặt câu hỏi cần giải quyết; **4. lỗi (error / 오류) ngân sách (budget / 예산) biến độ tin cậy (reliability / 신뢰성) thành ràng buộc (constraint / 제약조건) cho thay đổi (change / 변경)** biến câu hỏi đó thành những điều kiện không được phá vỡ khi đi vào thực hành. Từ đây, **5. Burn tỷ lệ (rate / 비율) tốt hơn alert theo snapshot** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. lỗi (error / 오류) ngân sách (budget / 예산) biến độ tin cậy (reliability / 신뢰성) thành ràng buộc (constraint / 제약조건) cho thay đổi (change / 변경)

Nếu SLO là 99.9%, phần 0.1% còn lại là lỗi (error / 오류) ngân sách (budget / 예산). ngân sách (budget / 예산) không phải quota để cố tình gây lỗi; nó là ngôn ngữ cân bằng innovation và stability.

Khi dịch vụ (service / 서비스) tiêu ngân sách (budget / 예산) nhanh, nhóm (team / 팀) có bằng chứng (evidence / 증거) để ưu tiên độ tin cậy (reliability / 신뢰성) công việc (work / 작업) hoặc giảm thay đổi (change / 변경) rủi ro (risk / 위험). Khi ngân sách (budget / 예산) còn nhiều, không nên dùng “sợ downtime” làm lý do chặn mọi cải tiến.

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **5. Burn tỷ lệ (rate / 비율) tốt hơn alert theo snapshot** tiếp nhận điểm tựa từ **4. lỗi (error / 오류) ngân sách (budget / 예산) biến độ tin cậy (reliability / 신뢰성) thành ràng buộc (constraint / 제약조건) cho thay đổi (change / 변경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. độ trễ (latency / 지연 시간) SLO cần phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Burn tỷ lệ (rate / 비율) tốt hơn alert theo snapshot

Alert “lỗi (error / 오류) tỷ lệ (rate / 비율) > 1% 5 phút” không tự hiểu SLO. Burn tỷ lệ (rate / 비율) hỏi dịch vụ (service / 서비스) đang tiêu lỗi (error / 오류) ngân sách (budget / 예산) nhanh hơn tốc độ cho phép bao nhiêu lần. Kết hợp cửa sổ ngắn và dài giúp bắt outage lớn nhanh nhưng giảm noise do spike nhỏ.

Mô hình tư duy (mental model / 사고 모델) là: nếu tiếp tục với tốc độ lỗi hiện tại, ngân sách (budget / 예산) sẽ hết khi nào.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **6. độ trễ (latency / 지연 시간) SLO cần phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **5. Burn tỷ lệ (rate / 비율) tốt hơn alert theo snapshot** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. phụ thuộc (dependency / 의존성) và composite SLO** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. độ trễ (latency / 지연 시간) SLO cần phân phối (distribution / 분포)

Average độ trễ (latency / 지연 시간) che tail. người dùng (user / 사용자) thường cảm nhận p95/p99 hoặc threshold-based good sự kiện (event / 이벤트). Một SLI “99% yêu cầu (request / 요청) dưới 500 ms” trực tiếp hơn average 200 ms nếu 1% yêu cầu (request / 요청) treo 20 giây.

Tuy nhiên percentile aggregation giữa dịch vụ (service / 서비스)/cửa sổ (window / 윈도우) có caveat; histogram bucket và event-based SLI thường dễ lập luận (reasoning / 추론) hơn khi xây SLO chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **7. phụ thuộc (dependency / 의존성) và composite SLO** tiếp nhận điểm tựa từ **6. độ trễ (latency / 지연 시간) SLO cần phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. sức chứa (capacity / 용량) là ability giữ SLO dưới tải (load / 로드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. phụ thuộc (dependency / 의존성) và composite SLO

Một dịch vụ (service / 서비스) phụ thuộc DB, bộ nhớ đệm (cache / 캐시) và payment provider. Availability end-to-end không thể cao tùy ý nếu phụ thuộc (dependency / 의존성) yếu và không có redundancy/degradation.

SLO kiến trúc (architecture / 아키텍처) phải hỏi phụ thuộc (dependency / 의존성) thất bại (failure / 실패) nào có thể degrade gracefully. Ví dụ recommendation dịch vụ (service / 서비스) down có thể bỏ recommendation thay vì thất bại (fail / 실패) checkout. Đây là thiết kế (design / 설계) quyết định (decision / 결정), không phải monitoring cấu hình (config / 설정).

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **8. sức chứa (capacity / 용량) là ability giữ SLO dưới tải (load / 로드)** tiếp nhận điểm tựa từ **7. phụ thuộc (dependency / 의존성) và composite SLO** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Autoscaling không thay thế sức chứa (capacity / 용량) planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. sức chứa (capacity / 용량) là ability giữ SLO dưới tải (load / 로드)

Sức chứa (capacity / 용량) planning không phải dự báo chính xác tương lai. Nó là giữ đủ headroom để demand variation, nút (node / 노드) thất bại (failure / 실패) và rollout không đẩy hệ thống qua saturation cliff.

Ba khái niệm cần tách: utilization cho biết tài nguyên (resource / 자원) đang dùng bao nhiêu; saturation cho biết demand đang chờ; thông lượng (throughput / 처리량) cho biết hệ thống hoàn thành bao nhiêu công việc (work / 작업). Khi utilization gần 100%, độ trễ (latency / 지연 시간) thường tăng phi tuyến do queueing.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **9. Autoscaling không thay thế sức chứa (capacity / 용량) planning** tiếp nhận điểm tựa từ **8. sức chứa (capacity / 용량) là ability giữ SLO dưới tải (load / 로드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. yêu cầu tài nguyên (resource request / 리소스 요청) là sức chứa (capacity / 용량) reservation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Autoscaling không thay thế sức chứa (capacity / 용량) planning

Autoscaler có delay và có thể quy mô (scale / 규모) đúng tài nguyên (resource / 자원) nhưng bottleneck nằm ở phụ thuộc (dependency / 의존성) khác. Thêm ứng dụng (application / 애플리케이션) replicas có thể làm cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) storm nặng hơn.

Sức chứa (capacity / 용량) mô hình (model / 모델) cần tìm bottleneck chuỗi (chain / 사슬): ingress, app CPU/bộ nhớ (memory / 메모리), liên kết (connection / 연결) pool, DB, hàng đợi (queue / 큐) bên tiêu thụ (consumer / 소비자), bên ngoài (external / 외부) API. kiểm thử tải (load test / 부하 테스트) phải tái tạo traffic shape và dữ liệu (data / 데이터) hành vi (behavior / 동작) đủ thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **9. Autoscaling không thay thế sức chứa (capacity / 용량) planning** nêu điều cần giải thích; **10. yêu cầu tài nguyên (resource request / 리소스 요청) là sức chứa (capacity / 용량) reservation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Queueing và backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. yêu cầu tài nguyên (resource request / 리소스 요청) là sức chứa (capacity / 용량) reservation

Trong Kubernetes, yêu cầu (request / 요청) ảnh hưởng scheduling. Tổng yêu cầu (request / 요청) là một cách biểu diễn demand reserved trên cluster. Nếu nhóm (team / 팀) cố hạ yêu cầu (request / 요청) để “tiết kiệm”, scheduler có thể overpack và độ tin cậy (reliability / 신뢰성) giảm.

FinOps tốt không tối ưu con số bill độc lập; nó tối ưu chi phí (cost / 비용) trên mỗi năng lực (capability / 역량)/SLO với headroom hợp lý.

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **10. yêu cầu tài nguyên (resource request / 리소스 요청) là sức chứa (capacity / 용량) reservation** nêu điều cần giải thích; **11. Queueing và backpressure** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. tải (load / 로드) shedding và graceful degradation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Queueing và backpressure

Khi arrival tỷ lệ (rate / 비율) vượt dịch vụ (service / 서비스) tỷ lệ (rate / 비율), hàng đợi (queue / 큐) tăng. hàng đợi (queue / 큐) giúp hấp thụ burst nhưng không tạo sức chứa (capacity / 용량). Nếu backlog tăng lâu, độ trễ (latency / 지연 시간) theo hàng đợi (queue / 큐) age tăng và cuối cùng hệ thống phải reject/drop/degrade.

Backpressure truyền tín hiệu ngược để producer giảm tốc. Nếu không có, upstream có thể tiếp tục đẩy công việc (work / 작업) vào downstream đã saturation.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **12. tải (load / 로드) shedding và graceful degradation** tiếp nhận điểm tựa từ **11. Queueing và backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. SLO cho nền tảng (platform / 플랫폼)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. tải (load / 로드) shedding và graceful degradation

Khi không thể phục vụ tất cả, chọn bỏ công việc (work / 작업) ít quan trọng có kiểm soát tốt hơn để toàn hệ thống collapse. tỷ lệ (rate / 비율) limit, admission điều khiển (control / 제어), hàng đợi (queue / 큐) limit và priority là các cơ chế.

Ví dụ checkout giữ cốt lõi (core / 핵심) thao tác (operation / 연산) nhưng tắt recommendation/analytics sync. Đây là độ tin cậy (reliability / 신뢰성) kiến trúc (architecture / 아키텍처) được quyết định trước sự cố (incident / 인시던트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **13. SLO cho nền tảng (platform / 플랫폼)** tiếp nhận điểm tựa từ **12. tải (load / 로드) shedding và graceful degradation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. cấp cao (senior / 시니어) ghi chú (note / 노트): độ tin cậy (reliability / 신뢰성) là ngân sách (budget / 예산) allocation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. SLO cho nền tảng (platform / 플랫폼)

Nền tảng (platform / 플랫폼) nhóm (team / 팀) cũng có người dùng (user / 사용자) là nhà phát triển (developer / 개발자)/sản phẩm (product / 제품) nhóm (team / 팀). SLI có thể gồm time-to-create dịch vụ (service / 서비스), chuỗi xử lý (pipeline / 파이프라인) availability, triển khai (deployment / 배포) success tín hiệu (signal / 신호), môi trường (environment / 환경) provisioning độ trễ (latency / 지연 시간) hoặc hỗ trợ (support / 지원) phản hồi (response / 응답) cho đường găng (critical path / 임계 경로).

Không nên chọn vanity chỉ số (metric / 지표) như “số cluster được quản”. nền tảng (platform / 플랫폼) SLO phải phản ánh người dùng (user / 사용자) journey.

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **14. cấp cao (senior / 시니어) ghi chú (note / 노트): độ tin cậy (reliability / 신뢰성) là ngân sách (budget / 예산) allocation** tiếp nhận điểm tựa từ **13. SLO cho nền tảng (platform / 플랫폼)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Worked example: 99.9% thực sự cho phép bao nhiêu thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. cấp cao (senior / 시니어) ghi chú (note / 노트): độ tin cậy (reliability / 신뢰성) là ngân sách (budget / 예산) allocation

CPU headroom, replica, multi-zone, kiểm thử (test / 테스트) thời gian (time / 시간), rà soát (review / 검토) effort và kỹ thuật (engineering / 엔지니어링) attention đều là ngân sách (budget / 예산). SLO cung cấp mục tiêu (objective / 목표) để phân bổ chúng. Nếu dịch vụ (service / 서비스) vượt xa SLO với chi phí (cost / 비용) cao, có thể đang over-engineer. Nếu ngân sách (budget / 예산) luôn cháy, kiến trúc (architecture / 아키텍처)/thay đổi (change / 변경) tiến trình (process / 프로세스) có debt.

SRE trưởng thành không phải làm mọi dịch vụ (service / 서비스) cực kỳ redundant; nó làm mức độ tin cậy (reliability / 신뢰성) **có chủ đích, đo được và phù hợp giá trị**.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **14. cấp cao (senior / 시니어) ghi chú (note / 노트): độ tin cậy (reliability / 신뢰성) là ngân sách (budget / 예산) allocation** cho ta quy tắc; **15. Worked example: 99.9% thực sự cho phép bao nhiêu thất bại (failure / 실패)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **16. Burn tỷ lệ (rate / 비율) là tốc độ tiêu ngân sách (budget / 예산) tương đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Worked example: 99.9% thực sự cho phép bao nhiêu thất bại (failure / 실패)

Với SLO time-based 99.9% trong 30 ngày, tổng cửa sổ có 43.200 phút. Phần 0,1% tương ứng khoảng 43,2 phút không đáp ứng SLO. Con số này chỉ đúng nếu SLI thực sự là time-based availability; request-based SLI phải tính theo sự kiện (event / 이벤트).

Nếu có 1.000.000 yêu cầu (request / 요청) hợp lệ trong cửa sổ và SLO là 99.9% good events, lỗi (error / 오류) ngân sách (budget / 예산) là 1.000 bad events. Một outage 5 phút ở giờ thấp điểm và một outage 5 phút ở giờ cao điểm có thể tiêu ngân sách (budget / 예산) request-based rất khác nhau. Đây là lý do phải định nghĩa SLI trước rồi mới diễn giải “bao nhiêu downtime”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **15. Worked example: 99.9% thực sự cho phép bao nhiêu thất bại (failure / 실패)** cho ta quy tắc; **16. Burn tỷ lệ (rate / 비율) là tốc độ tiêu ngân sách (budget / 예산) tương đối** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **17. Little's Law nối hàng đợi (queue / 큐) với độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Burn tỷ lệ (rate / 비율) là tốc độ tiêu ngân sách (budget / 예산) tương đối

Giả sử SLO cho phép bad-event ratio 0,1%. Nếu trong một cửa sổ (window / 윈도우) dịch vụ (service / 서비스) đang có 1% bad sự kiện (event / 이벤트), nó đang burn nhanh khoảng 10 lần tốc độ bền vững. Nếu giữ nguyên, lỗi (error / 오류) ngân sách (budget / 예산) của cả cửa sổ dài sẽ bị tiêu nhanh hơn nhiều so với thiết kế.

Burn tỷ lệ (rate / 비율) giúp thống nhất severity theo SLO. Một spike 5% kéo dài vài phút có thể đáng page ngay vì burn cực nhanh; 0,12% kéo dài ngắn có thể chưa cần đánh thức người trực nếu ngân sách (budget / 예산)/cửa sổ (window / 윈도우) còn khỏe. Alert chính sách (policy / 정책) thực tế thường kết hợp nhiều cửa sổ (window / 윈도우) để vừa nhạy với outage lớn vừa tránh noise.

Điều quan trọng không phải thuộc một bộ threshold cố định, mà hiểu ratio:

```text
burn rate = observed bad-event rate / allowed bad-event rate
```

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **17. Little's Law nối hàng đợi (queue / 큐) với độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **16. Burn tỷ lệ (rate / 비율) là tốc độ tiêu ngân sách (budget / 예산) tương đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Khi arrival tỷ lệ (rate / 비율) lớn hơn dịch vụ (service / 서비스) tỷ lệ (rate / 비율), backlog tăng theo thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Little's Law nối hàng đợi (queue / 큐) với độ trễ (latency / 지연 시간)

Trong một hệ thống ổn định, Little's Law cho một mô hình tư duy (mental model / 사고 모델) rất mạnh:

```text
L = λ × W
```

`L` là lượng công việc (work / 작업) trung bình đang ở trong hệ thống, `λ` là thông lượng (throughput / 처리량)/arrival tỷ lệ (rate / 비율) trung bình, `W` là thời gian trung bình một công việc (work / 작업) item ở trong hệ thống. Đây không phải công thức để dự đoán mọi spike, mà là sanity check cho hàng đợi (queue / 큐)/sức chứa (capacity / 용량).

Ví dụ dịch vụ (service / 서비스) xử lý trung bình 100 yêu cầu (request / 요청)/s và mỗi yêu cầu (request / 요청) ở trong hệ thống (system / 시스템) 0,2 giây thì tính đồng thời (concurrency / 동시성) trung bình xấp xỉ 20. Nếu độ trễ (latency / 지연 시간) tăng lên 1 giây trong khi thông lượng (throughput / 처리량) tương tự, số yêu cầu (request / 요청) in-flight trung bình tăng lên khoảng 100. liên kết (connection / 연결) pool, luồng thực thi (thread / 스레드) pool và bộ nhớ (memory / 메모리) pressure có thể tăng theo dù traffic không đổi.

Đây là lý do độ trễ (latency / 지연 시간) degradation tự nó có thể tạo thêm tài nguyên (resource / 자원) pressure.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **18. Khi arrival tỷ lệ (rate / 비율) lớn hơn dịch vụ (service / 서비스) tỷ lệ (rate / 비율), backlog tăng theo thời gian** tiếp nhận điểm tựa từ **17. Little's Law nối hàng đợi (queue / 큐) với độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. thử lại (retry / 재시도) cần một ngân sách (budget / 예산) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Khi arrival tỷ lệ (rate / 비율) lớn hơn dịch vụ (service / 서비스) tỷ lệ (rate / 비율), backlog tăng theo thời gian

Nếu producer đưa vào `λ` công việc (work / 작업)/giây nhưng bên tiêu thụ (consumer / 소비자) chỉ xử lý `μ` công việc (work / 작업)/giây và `λ > μ`, hàng đợi (queue / 큐) sẽ tăng gần theo chênh lệch `λ - μ` trong giai đoạn đó. Autoscaling chỉ cứu được nếu cuối cùng làm `μ` vượt `λ` trước khi hàng đợi (queue / 큐) age vi phạm SLO hoặc lưu trữ (storage / 저장소)/TTL bị chạm.

Ví dụ hàng đợi (queue / 큐) nhận 1.200 message/s nhưng bên tiêu thụ (consumer / 소비자) chỉ hoàn thành 1.000 message/s. Backlog tăng khoảng 200 message mỗi giây. Sau 10 phút đã có khoảng 120.000 message tích thêm, chưa tính traffic biến động. “hàng đợi (queue / 큐) vẫn hoạt động” không có nghĩa hệ thống (system / 시스템) healthy; message age mới phản ánh người dùng (user / 사용자) delay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **19. thử lại (retry / 재시도) cần một ngân sách (budget / 예산) riêng** tiếp nhận điểm tựa từ **18. Khi arrival tỷ lệ (rate / 비율) lớn hơn dịch vụ (service / 서비스) tỷ lệ (rate / 비율), backlog tăng theo thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. phụ thuộc (dependency / 의존성) ngân sách (budget / 예산) phải được phân bổ có chủ đích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. thử lại (retry / 재시도) cần một ngân sách (budget / 예산) riêng

Thử lại (retry / 재시도) làm arrival tỷ lệ (rate / 비율) mà downstream nhìn thấy lớn hơn người dùng (user / 사용자) traffic. Nếu mỗi yêu cầu (request / 요청) có tối đa ba attempt, outage downstream có thể khiến yêu cầu (request / 요청) tỷ lệ (rate / 비율) thực tế tiến gần nhiều lần traffic gốc. Nhiều tầng (layer / 계층) cùng thử lại (retry / 재시도) — SDK, dịch vụ (service / 서비스) mesh, bộ cân bằng tải (load balancer / 로드 밸런서), ứng dụng (application / 애플리케이션) — còn có thể nhân lên mạnh hơn.

Một độ tin cậy (reliability / 신뢰성) thiết kế (design / 설계) tốt xác định thử lại (retry / 재시도) ngân sách (budget / 예산): thao tác (operation / 연산) nào thử lại (retry / 재시도) được, tổng deadline, attempt tối đa, backoff/jitter và tầng (layer / 계층) nào sở hữu thử lại (retry / 재시도). Khi downstream saturation, tải (load / 로드) shedding/circuit breaking có thể quan trọng hơn cố tăng success bằng thử lại (retry / 재시도).

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **20. phụ thuộc (dependency / 의존성) ngân sách (budget / 예산) phải được phân bổ có chủ đích** tiếp nhận điểm tựa từ **19. thử lại (retry / 재시도) cần một ngân sách (budget / 예산) riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. sức chứa (capacity / 용량) kiểm thử (test / 테스트) phải đo saturation cliff, không chỉ peak thông lượng (throughput / 처리량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. phụ thuộc (dependency / 의존성) ngân sách (budget / 예산) phải được phân bổ có chủ đích

Một checkout dịch vụ (service / 서비스) có SLO 99.9% nhưng gọi tuần tự nhiều phụ thuộc (dependency / 의존성) trọng yếu (critical / 중요) thì end-to-end độ tin cậy (reliability / 신뢰성) chịu ảnh hưởng của tất cả phụ thuộc (dependency / 의존성). Không thể chỉ đặt cho mỗi phụ thuộc (dependency / 의존성) cùng 99.9% rồi kỳ vọng composition vẫn đạt 99.9%.

Có ba cách xử lý chính: phụ thuộc (dependency / 의존성) phải mạnh hơn SLO end-to-end; hệ thống (system / 시스템) thêm redundancy/fallback/bộ nhớ đệm (cache / 캐시); hoặc luồng (flow / 흐름) được thiết kế để phụ thuộc (dependency / 의존성) không trọng yếu (critical / 중요), ví dụ recommendation thất bại (fail / 실패) thì checkout vẫn tiếp tục.

Đây là nơi SLO trở thành đầu vào (input / 입력) cho kiến trúc (architecture / 아키텍처). SLO không phải dashboard decoration; nó quyết định chỗ nào cần redundancy, chỗ nào có thể degrade và chỗ nào chi phí (cost / 비용) thêm không tạo giá trị.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **21. sức chứa (capacity / 용량) kiểm thử (test / 테스트) phải đo saturation cliff, không chỉ peak thông lượng (throughput / 처리량)** tiếp nhận điểm tựa từ **20. phụ thuộc (dependency / 의존성) ngân sách (budget / 예산) phải được phân bổ có chủ đích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Admission điều khiển (control / 제어) giữ hệ thống trong vùng có thể phục vụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. sức chứa (capacity / 용량) kiểm thử (test / 테스트) phải đo saturation cliff, không chỉ peak thông lượng (throughput / 처리량)

Một kiểm thử tải (load test / 부하 테스트) chỉ hỏi “tối đa bao nhiêu yêu cầu (request / 요청)/s” dễ bỏ qua hành vi (behavior / 동작) khi vượt ngưỡng. Điều quan trọng hơn là khi tải (load / 로드) tăng, độ trễ (latency / 지연 시간), lỗi (error / 오류), hàng đợi (queue / 큐), GC, liên kết (connection / 연결) pool và downstream pressure thay đổi theo curve nào; khi tải (load / 로드) giảm lại hệ thống (system / 시스템) có hồi phục hay không.

Một dịch vụ (service / 서비스) có thể đạt 5.000 yêu cầu (request / 요청)/s trong kiểm thử (test / 테스트) ngắn nhưng sau vài phút liên kết (connection / 연결) hàng đợi (queue / 큐) tích tụ, tail độ trễ (latency / 지연 시간) tăng và thử lại (retry / 재시도) đẩy cơ sở dữ liệu (database / 데이터베이스) vào collapse. sức chứa (capacity / 용량) usable phải là vùng hệ thống giữ SLO ổn định với headroom cho rollout/thất bại (failure / 실패), không phải con số thông lượng (throughput / 처리량) lớn nhất từng thấy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **22. Admission điều khiển (control / 제어) giữ hệ thống trong vùng có thể phục vụ** tiếp nhận điểm tựa từ **21. sức chứa (capacity / 용량) kiểm thử (test / 테스트) phải đo saturation cliff, không chỉ peak thông lượng (throughput / 처리량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. tính đồng thời (concurrency / 동시성) limit nên dựa trên độ trễ (latency / 지연 시간) và tài nguyên (resource / 자원) ngân sách (budget / 예산), không chỉ CPU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Admission điều khiển (control / 제어) giữ hệ thống trong vùng có thể phục vụ

Khi một dịch vụ (service / 서비스) đã ở gần saturation, nhận thêm mọi yêu cầu (request / 요청) không phải lúc nào cũng tăng useful thông lượng (throughput / 처리량). công việc (work / 작업) mới có thể chỉ làm hàng đợi (queue / 큐) dài hơn, hết thời gian chờ (timeout / 타임아웃) nhiều hơn và giữ tài nguyên (resource / 자원) lâu hơn. Admission điều khiển (control / 제어) đặt một giới hạn trước khi công việc (work / 작업) đi sâu vào hệ thống: concurrent yêu cầu (request / 요청) limit, hàng đợi (queue / 큐) bound, tỷ lệ (rate / 비율) limit hoặc per-tenant ngân sách (budget / 예산).

Mô hình tư duy (mental model / 사고 모델) quan trọng là **protect useful công việc (work / 작업), không maximize accepted công việc (work / 작업)**. Nếu dịch vụ (service / 서비스) xử lý ổn định 800 yêu cầu (request / 요청)/s nhưng nhận 1.500 yêu cầu (request / 요청)/s rồi để tất cả chờ 20 giây trước khi hết thời gian chờ (timeout / 타임아웃), người dùng (user / 사용자) experience và tài nguyên (resource / 자원) usage đều tệ hơn việc reject nhanh phần vượt khả năng với tín hiệu (signal / 신호) thử lại (retry / 재시도) rõ.

Admission điểm (point / 지점) nên đặt gần tài nguyên (resource / 자원) khan hiếm mà nó bảo vệ. Limit ở edge có thể bảo vệ toàn dịch vụ (service / 서비스); semaphore ở ứng dụng (application / 애플리케이션) có thể bảo vệ luồng thực thi (thread / 스레드)/liên kết (connection / 연결) pool; quota ở downstream bảo vệ cơ sở dữ liệu (database / 데이터베이스) hoặc bên ngoài (external / 외부) API. Một limit quá xa bottleneck có thể không kiểm soát đúng tài nguyên (resource / 자원) pressure.

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **22. Admission điều khiển (control / 제어) giữ hệ thống trong vùng có thể phục vụ** đã nêu tiêu chí phân biệt, còn **23. tính đồng thời (concurrency / 동시성) limit nên dựa trên độ trễ (latency / 지연 시간) và tài nguyên (resource / 자원) ngân sách (budget / 예산), không chỉ CPU** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **24. Failover sức chứa (capacity / 용량) phải được reserve trước thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. tính đồng thời (concurrency / 동시성) limit nên dựa trên độ trễ (latency / 지연 시간) và tài nguyên (resource / 자원) ngân sách (budget / 예산), không chỉ CPU

Một dịch vụ (service / 서비스) I/O-bound có thể CPU thấp nhưng liên kết (connection / 연결) pool hoặc downstream tính đồng thời (concurrency / 동시성) đã đầy. Vì vậy autoscaling chỉ theo CPU và admission chỉ theo yêu cầu (request / 요청) tỷ lệ (rate / 비율) đều có thể miss bottleneck.

Nếu mỗi yêu cầu (request / 요청) giữ một DB liên kết (connection / 연결) trung bình 200 ms và DB chỉ dành 400 liên kết (connection / 연결) hữu ích cho dịch vụ (service / 서비스), tính đồng thời (concurrency / 동시성) vượt xa 400 sẽ chủ yếu tạo wait. Giới hạn ứng dụng (application / 애플리케이션) tính đồng thời (concurrency / 동시성) quanh downstream ngân sách (budget / 예산) thường ổn định hơn việc mở pool vô hạn.

Adaptive tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) có thể điều chỉnh limit theo độ trễ (latency / 지연 시간)/saturation tín hiệu (signal / 신호), nhưng controller phải phản ứng chậm hơn noise và có floor/ceiling. Nếu limit controller, autoscaler và thử lại (retry / 재시도) cùng phản ứng mạnh trên cùng tín hiệu (signal / 신호), hệ thống có thể oscillate.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **23. tính đồng thời (concurrency / 동시성) limit nên dựa trên độ trễ (latency / 지연 시간) và tài nguyên (resource / 자원) ngân sách (budget / 예산), không chỉ CPU** đã nêu tiêu chí phân biệt, còn **24. Failover sức chứa (capacity / 용량) phải được reserve trước thất bại (failure / 실패)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **25. Correlated thất bại (failure / 실패) phá giả định (assumption / 가정) độc lập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Failover sức chứa (capacity / 용량) phải được reserve trước thất bại (failure / 실패)

Một hệ thống chạy bình thường ở 70–80% utilization mỗi zone có thể nhìn “hiệu quả”, nhưng nếu một zone mất và traffic dồn sang phần còn lại, sức chứa (capacity / 용량) có thể lập tức vượt saturation cliff. Headroom cần được tính theo thất bại (failure / 실패) mô hình (model / 모델), không chỉ daily peak.

Ví dụ ba zone mỗi zone phục vụ 1/3 traffic. Nếu thiết kế chịu mất một zone mà vẫn giữ SLO, hai zone còn lại phải hấp thụ khoảng 1,5 lần tải (load / 로드) bình thường, cộng thêm rollout/autoscaling delay. sức chứa (capacity / 용량) mục tiêu (target / 대상) vì vậy thường thấp hơn mức utilization tối đa kỹ thuật.

Điều tương tự áp dụng cho cơ sở dữ liệu (database / 데이터베이스) replica, hàng đợi (queue / 큐) bên tiêu thụ (consumer / 소비자), NAT gateway, bên ngoài (external / 외부) API quota và CI runner. “Có redundancy” nhưng không có **spare sức chứa (capacity / 용량) under failover** chỉ tạo redundancy hình thức.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **25. Correlated thất bại (failure / 실패) phá giả định (assumption / 가정) độc lập** tiếp nhận điểm tựa từ **24. Failover sức chứa (capacity / 용량) phải được reserve trước thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Brownout là intentional degradation để bảo vệ cốt lõi (core / 핵심) SLO** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Correlated thất bại (failure / 실패) phá giả định (assumption / 가정) độc lập

Nhiều mô hình độ tin cậy (reliability / 신뢰성) ngầm giả định replica hoặc zone thất bại (fail / 실패) độc lập. Thực tế phụ thuộc (dependency / 의존성) chung như DNS, định danh (identity / 식별자) provider, registry, certificate authority, điều khiển (control / 제어) plane, dùng chung (shared / 공유) mạng (network / 네트워크) hoặc bad rollout có thể làm nhiều replica thất bại (fail / 실패) cùng lúc.

Vì vậy redundancy phải hỏi **common-mode phụ thuộc (dependency / 의존성) nào còn dùng chung**. Hai region cùng dùng một toàn cục (global / 전역) cấu hình (configuration / 구성) rollout hoặc cùng một bên ngoài (external / 외부) API chưa chắc tạo independence thực sự.

Kiểm thử tải (load test / 부하 테스트)/thất bại (failure / 실패) exercise nên bao gồm correlated sự kiện (event / 이벤트): secret rotation sai toàn fleet, DNS degradation, chính sách (policy / 정책) rollout chặn deploy hoặc regional phụ thuộc (dependency / 의존성) thất bại (failure / 실패). Đây là cách kiểm tra blast radius của dùng chung (shared / 공유) điều khiển (control / 제어) plane, không chỉ tiến trình (process / 프로세스) crash đơn lẻ.

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **26. Brownout là intentional degradation để bảo vệ cốt lõi (core / 핵심) SLO** tiếp nhận điểm tựa từ **25. Correlated thất bại (failure / 실패) phá giả định (assumption / 가정) độc lập** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. lỗi (error / 오류) ngân sách (budget / 예산) chính sách (policy / 정책) phải điều khiển quyết định (decision / 결정), không chỉ tạo dashboard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Brownout là intentional degradation để bảo vệ cốt lõi (core / 핵심) SLO

Trong overload, một dịch vụ (service / 서비스) có thể tạm tắt tính năng (feature / 기능) không thiết yếu thay vì để toàn đường đi của yêu cầu (request path / 요청 경로) chậm. Ví dụ bỏ recommendation, giảm ảnh (image / 이미지) transformation chất lượng cao, defer analytics hoặc trả stale-but-safe bộ nhớ đệm (cache / 캐시) cho một số read đường dẫn (path / 경로).

Brownout khác outage ngẫu nhiên ở chỗ degradation được thiết kế trước, observable và reversible. tính năng (feature / 기능) nào được bỏ phải dựa trên nghiệp vụ (business / 비즈니스) criticality và dữ liệu (data / 데이터) tính đúng đắn (correctness / 정확성); không phải mọi thao tác (operation / 연산) đều có thể stale hoặc async.

Một nền tảng (platform / 플랫폼) tốt cho phép declare priority lớp (class / 클래스) hoặc degradation chế độ (mode / 모드) đủ rõ để sự cố (incident / 인시던트) phản hồi (response / 응답) không phải phát minh lô-gic (logic / 논리) mới giữa lúc hệ thống đang cháy.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **27. lỗi (error / 오류) ngân sách (budget / 예산) chính sách (policy / 정책) phải điều khiển quyết định (decision / 결정), không chỉ tạo dashboard** tiếp nhận điểm tựa từ **26. Brownout là intentional degradation để bảo vệ cốt lõi (core / 핵심) SLO** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. SLO traffic thấp cần ngữ nghĩa (semantics / 의미론) khác dịch vụ (service / 서비스) nhiều yêu cầu (request / 요청)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. lỗi (error / 오류) ngân sách (budget / 예산) chính sách (policy / 정책) phải điều khiển quyết định (decision / 결정), không chỉ tạo dashboard

Một SLO chỉ có giá trị tổ chức khi ngân sách (budget / 예산) trạng thái (state / 상태) thay đổi hành vi. Nếu ngân sách (budget / 예산) cháy nhưng bản phát hành (release / 릴리스) cadence, rà soát (review / 검토) độ sâu (depth / 깊이) và độ tin cậy (reliability / 신뢰성) backlog không thay đổi, SLO chỉ là reporting.

Chính sách (policy / 정책) có thể nói khi burn kéo dài thì giảm risky rollout, bắt buộc canary, ưu tiên độ tin cậy (reliability / 신뢰성) công việc (work / 작업) hoặc yêu cầu đơn vị sở hữu (owner / 오너) rà soát (review / 검토). Nhưng chính sách (policy / 정책) không nên cơ học đến mức mọi ngân sách (budget / 예산) dip nhỏ đều đóng băng delivery; cần phân biệt transient sự kiện (event / 이벤트), known sự cố (incident / 인시던트) và structural unreliability.

Cấp cao (senior / 시니어) SRE xem lỗi (error / 오류) ngân sách (budget / 예산) như **phản hồi (feedback / 피드백) controller cho kỹ thuật (engineering / 엔지니어링) quyết định (decision / 결정)**. tín hiệu (signal / 신호) phải gần người dùng (user / 사용자) impact, hành động (action / 동작) phải proportional và sau khi độ tin cậy (reliability / 신뢰성) hồi phục, ràng buộc (constraint / 제약조건) cũng phải được nới lại thay vì trở thành permanent bureaucracy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **28. SLO traffic thấp cần ngữ nghĩa (semantics / 의미론) khác dịch vụ (service / 서비스) nhiều yêu cầu (request / 요청)** tiếp nhận điểm tựa từ **27. lỗi (error / 오류) ngân sách (budget / 예산) chính sách (policy / 정책) phải điều khiển quyết định (decision / 결정), không chỉ tạo dashboard** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Valid-event denominator là một phần của tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. SLO traffic thấp cần ngữ nghĩa (semantics / 의미론) khác dịch vụ (service / 서비스) nhiều yêu cầu (request / 요청)

Với dịch vụ (service / 서비스) xử lý hàng triệu yêu cầu (request / 요청) mỗi giờ, một tỷ lệ bad-event có mẫu (sample / 표본) đủ lớn để burn-rate ổn định. Nhưng một admin API chỉ có vài chục yêu cầu (request / 요청) mỗi ngày có thể bị một lỗi duy nhất làm tỷ lệ lỗi nhảy rất mạnh. Alert theo phần trăm lúc này dễ vừa noisy vừa chậm.

Low-traffic SLO nên hỏi người dùng (user / 사용자) journey thực sự là gì. Có thể synthetic giao dịch (transaction / 트랜잭션) định kỳ phù hợp hơn yêu cầu (request / 요청) ratio; hoặc đo lường (measurement / 측정) cửa sổ (window / 윈도우) cần dài hơn; hoặc cần kết hợp sự kiện (event / 이벤트) count tối thiểu trước khi diễn giải một tỷ lệ. Không nên giả định cùng một công thức alert phù hợp cho checkout 50.000 yêu cầu (request / 요청)/s và backup-restore API 20 lần/ngày.

Điểm quan trọng là **mẫu quan sát (sample) quyết định độ ổn định của phép đo**. SLO là đặc tả hợp đồng (contract / 계약) sản phẩm, nhưng tín hiệu (signal / 신호) dùng để đánh giá đặc tả hợp đồng (contract / 계약) vẫn chịu giới hạn thống kê.

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **29. Valid-event denominator là một phần của tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **28. SLO traffic thấp cần ngữ nghĩa (semantics / 의미론) khác dịch vụ (service / 서비스) nhiều yêu cầu (request / 요청)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. cửa sổ (window / 윈도우) ngữ nghĩa (semantics / 의미론) thay đổi hành vi của lỗi (error / 오류) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Valid-event denominator là một phần của tính đúng đắn (correctness / 정확성)

Trong công thức `good / valid`, denominator quyết định SLO đang nói về population nào. Nếu chuỗi xử lý (pipeline / 파이프라인) vô tình loại yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) trước khi chúng tới ứng dụng (application / 애플리케이션) log, hoặc bỏ tenant/region lỗi vì label missing, SLI có thể đẹp lên chính vì bad sự kiện (event / 이벤트) biến mất khỏi denominator.

Do đó cần định nghĩa nơi đo và điều kiện eligibility. Edge/bộ cân bằng tải (load balancer / 로드 밸런서) thường nhìn được cả yêu cầu (request / 요청) không tới ứng dụng (application / 애플리케이션); ứng dụng (application / 애플리케이션) nhìn được nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과) sâu hơn. Với trọng yếu (critical / 중요) journey, đôi khi cần kết hợp nhiều sensor để tránh survivorship độ lệch (bias / 편향).

Một SLI rà soát (review / 검토) tốt không chỉ hỏi “good sự kiện (event / 이벤트) là gì?” mà hỏi thêm **sự kiện (event / 이벤트) nào có quyền biến mất khỏi phép tính và tại sao**.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **30. cửa sổ (window / 윈도우) ngữ nghĩa (semantics / 의미론) thay đổi hành vi của lỗi (error / 오류) ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **29. Valid-event denominator là một phần của tính đúng đắn (correctness / 정확성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. SLO cho asynchronous công việc (work / 작업) nên đo age và completion ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. cửa sổ (window / 윈도우) ngữ nghĩa (semantics / 의미론) thay đổi hành vi của lỗi (error / 오류) ngân sách (budget / 예산)

Rolling cửa sổ (window / 윈도우) 30 ngày, calendar month và fixed bản phát hành (release / 릴리스) cửa sổ (window / 윈도우) không tương đương. Rolling cửa sổ (window / 윈도우) luôn trượt theo thời gian nên một sự cố (incident / 인시던트) lớn dần rời khỏi cửa sổ (window / 윈도우); calendar cửa sổ (window / 윈도우) reset ở mốc lịch; bản phát hành (release / 릴리스) cửa sổ (window / 윈도우) gắn độ tin cậy (reliability / 신뢰성) với một cohort/phiên bản (version / 버전) cụ thể.

Không có một loại cửa sổ (window / 윈도우) luôn đúng. Rolling cửa sổ (window / 윈도우) phù hợp vận hành liên tục; calendar cửa sổ (window / 윈도우) dễ align reporting; cohort/bản phát hành (release / 릴리스) cửa sổ (window / 윈도우) hữu ích khi muốn so rollout. Điều quan trọng là chính sách (policy / 정책) phải biết cửa sổ (window / 윈도우) nào đang điều khiển quyết định (decision / 결정), nếu không nhóm (team / 팀) có thể thấy “ngân sách (budget / 예산) hồi phục” chỉ vì đồng hồ reset chứ hệ thống (system / 시스템) chưa đáng tin hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **31. SLO cho asynchronous công việc (work / 작업) nên đo age và completion ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **30. cửa sổ (window / 윈도우) ngữ nghĩa (semantics / 의미론) thay đổi hành vi của lỗi (error / 오류) ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Composite journey cần phân biệt serial phụ thuộc (dependency / 의존성) và fallback đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. SLO cho asynchronous công việc (work / 작업) nên đo age và completion ngữ nghĩa (semantics / 의미론)

Hàng đợi (queue / 큐) bên tiêu thụ (consumer / 소비자) hoặc batch chuỗi xử lý (pipeline / 파이프라인) không có “yêu cầu (request / 요청) độ trễ (latency / 지연 시간)” giống HTTP. người dùng (user / 사용자) có thể quan tâm việc message được xử lý trong 5 phút, report hoàn tất trước 08:00 hoặc dữ liệu (data / 데이터) freshness không quá 15 phút.

SLI phù hợp có thể là tỷ lệ công việc (work / 작업) item hoàn tất trước deadline hoặc age của oldest valid item. hàng đợi (queue / 큐) độ sâu (depth / 깊이) đơn thuần không đủ: 100.000 item mới có thể ít nghiêm trọng hơn 1.000 item đã chờ 6 giờ.

Với thử lại (retry / 재시도), cần quyết định success sau thử lại (retry / 재시도) còn là good sự kiện (event / 이벤트) không và deadline tính từ attempt đầu hay cuối. Đây là nơi lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론) phải đi trước chỉ số (metric / 지표) cú pháp (syntax / 문법).

> **Chuyển mạch:** Trong **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **31. SLO cho asynchronous công việc (work / 작업) nên đo age và completion ngữ nghĩa (semantics / 의미론)** xác định đầu vào; **32. Composite journey cần phân biệt serial phụ thuộc (dependency / 의존성) và fallback đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **33. Multi-SLI dịch vụ (service / 서비스) cần biết sự đánh đổi (trade-off / 트레이드오프) giữa availability, độ trễ (latency / 지연 시간) và tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Composite journey cần phân biệt serial phụ thuộc (dependency / 의존성) và fallback đường dẫn (path / 경로)

Nếu một người dùng (user / 사용자) journey bắt buộc đi qua A rồi B rồi C và thất bại (failure / 실패) tương đối độc lập, end-to-end success không thể tốt hơn các thành phần và thường thấp hơn từng thành phần riêng. Nhưng nếu B có bộ nhớ đệm (cache / 캐시)/fallback hoặc C chỉ chạy cho 10% yêu cầu (request / 요청), cách composition thay đổi.

Vì vậy không nên nhân các số availability một cách máy móc nếu topology có conditional đường dẫn (path / 경로), thử lại (retry / 재시도), quorum hoặc graceful degradation. Trước hết vẽ journey đồ thị (graph / 그래프): phụ thuộc (dependency / 의존성) nào mandatory, phụ thuộc (dependency / 의존성) nào optional, branch nào chiếm bao nhiêu traffic và thất bại (failure / 실패) nào được che bởi fallback.

SLO decomposition là bài toán kiến trúc (architecture / 아키텍처) trước khi là bài toán số học.

> **Chuyển mạch:** Ở chặng này của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **32. Composite journey cần phân biệt serial phụ thuộc (dependency / 의존성) và fallback đường dẫn (path / 경로)** cho ta quy tắc; **33. Multi-SLI dịch vụ (service / 서비스) cần biết sự đánh đổi (trade-off / 트레이드오프) giữa availability, độ trễ (latency / 지연 시간) và tính đúng đắn (correctness / 정확성)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **34. SLO đo lường (measurement / 측정) chuỗi xử lý (pipeline / 파이프라인) cũng cần phiên bản (version / 버전) và kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Multi-SLI dịch vụ (service / 서비스) cần biết sự đánh đổi (trade-off / 트레이드오프) giữa availability, độ trễ (latency / 지연 시간) và tính đúng đắn (correctness / 정확성)

Một dịch vụ (service / 서비스) có thể tăng availability bằng cách trả stale bộ nhớ đệm (cache / 캐시), nhưng freshness/tính đúng đắn (correctness / 정확성) giảm. Có thể giữ độ trễ (latency / 지연 시간) thấp bằng fail-fast, nhưng tỷ lệ yêu cầu (request / 요청) thành công giảm. Vì vậy chỉ một SLO có thể tạo incentive lệch.

Trọng yếu (critical / 중요) năng lực (capability / 역량) thường cần một tập nhỏ SLI bổ sung nhau: success/tính đúng đắn (correctness / 정확성), độ trễ (latency / 지연 시간)/freshness và đôi khi durability. Các SLI này không nên biến thành dashboard hàng chục mục tiêu; mỗi cái phải đại diện một thất bại (failure / 실패) dimension người dùng (user / 사용자) thực sự quan tâm.

Brownout càng làm điều này rõ: cốt lõi (core / 핵심) availability có thể đạt trong khi chất lượng (quality / 품질) tier đang giảm có chủ đích. độ tin cậy (reliability / 신뢰성) đặc tả hợp đồng (contract / 계약) phải cho phép nói chính xác **điều gì đang được giữ và điều gì đang được hy sinh**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SLI, SLO, lỗi (error / 오류) ngân sách (budget / 예산) và sức chứa (capacity / 용량): độ tin cậy (reliability / 신뢰성) có mục tiêu**, **33. Multi-SLI dịch vụ (service / 서비스) cần biết sự đánh đổi (trade-off / 트레이드오프) giữa availability, độ trễ (latency / 지연 시간) và tính đúng đắn (correctness / 정확성)** cho ta quy tắc; **34. SLO đo lường (measurement / 측정) chuỗi xử lý (pipeline / 파이프라인) cũng cần phiên bản (version / 버전) và kiểm tra (audit / 감사)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 34. SLO đo lường (measurement / 측정) chuỗi xử lý (pipeline / 파이프라인) cũng cần phiên bản (version / 버전) và kiểm tra (audit / 감사)

Đổi truy vấn (query / 쿼리), bucket, denominator, label ánh xạ (mapping / 매핑) hoặc dữ liệu (data / 데이터) nguồn (source / 소스) có thể làm SLO nhảy mà dịch vụ (service / 서비스) hành vi (behavior / 동작) không đổi. Đây là thay đổi (change / 변경) môi trường vận hành (production / 운영 환경) vì lỗi (error / 오류) ngân sách (budget / 예산) trạng thái (state / 상태) có thể điều khiển bản phát hành (release / 릴리스) chính sách (policy / 정책) và paging.

Đo lường (measurement / 측정) definition nên được versioned/reviewed; khi di chuyển (migration / 마이그레이션) lớn có thể chạy old/new song song để so difference trước khi đổi nguồn chuẩn (source of truth / 정본). Dashboard nên cho biết SLO definition revision hoặc thay đổi (change / 변경) sự kiện (event / 이벤트) để operator phân biệt độ tin cậy (reliability / 신뢰성) regression với đo lường (measurement / 측정) thay đổi (change / 변경).

Cấp cao (senior / 시니어) lập luận (reasoning / 추론) coi SLO chuỗi xử lý (pipeline / 파이프라인) là một điều khiển (control / 제어) hệ thống (system / 시스템): **sensor definition sai có thể làm actuator kỹ thuật (engineering / 엔지니어링) ra quyết định sai**, dù ứng dụng (application / 애플리케이션) hoàn toàn không thay đổi.

> **Bàn giao:** Sau **34. SLO đo lường (measurement / 측정) chuỗi xử lý (pipeline / 파이프라인) cũng cần phiên bản (version / 버전) và kiểm tra (audit / 감사)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
