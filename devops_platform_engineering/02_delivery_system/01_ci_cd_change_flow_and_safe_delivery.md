# CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **CI/CD: biến change thành flow có bằng chứng**. Route đi từ small integration → automated checks → staged promotion → deployment guardrails → rollback/feedback, để delivery giảm rủi ro theo từng tầng.

## 1. Continuous tích hợp (integration / 통합) là giảm tích hợp (integration / 통합) rủi ro (risk / 위험)

Continuous tích hợp (integration / 통합) không đồng nghĩa với “có máy chủ (server / 서버) chạy kiểm thử (test / 테스트)”. Bản chất là tích hợp thay đổi nhỏ vào nhánh chính thường xuyên và nhận phản hồi (feedback / 피드백) tự động đủ nhanh để lỗi tích hợp (integration / 통합) không tích tụ.

Nếu branch sống hai tuần rồi mới merge nhưng có Jenkins chạy mỗi lần ghi nhận (commit / 커밋), hệ thống có automation nhưng phản hồi (feedback / 피드백) tích hợp (integration / 통합) vẫn muộn. Nếu kiểm thử (test / 테스트) mất sáu giờ và thường flaky, nhà phát triển (developer / 개발자) có xu hướng bỏ qua tín hiệu (signal / 신호). Do đó CI là thiết kế vòng phản hồi (feedback loop / 피드백 루프), không chỉ YAML chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **1. Continuous tích hợp (integration / 통합) là giảm tích hợp (integration / 통합) rủi ro (risk / 위험)** xác định đầu vào; **2. chuỗi xử lý (pipeline / 파이프라인) phải trả lời câu hỏi theo tầng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. Flaky kiểm thử (test / 테스트) là độ tin cậy (reliability / 신뢰성) debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. chuỗi xử lý (pipeline / 파이프라인) phải trả lời câu hỏi theo tầng

Một chuỗi xử lý (pipeline / 파이프라인) tốt tổ chức check từ rẻ/nhanh đến đắt/chậm, nhưng không biến chuỗi xử lý (pipeline / 파이프라인) thành một chuỗi tuần tự dài vô lý. Lint/static check cho phản hồi (feedback / 피드백) nhanh. đơn vị (unit / 단위) kiểm thử (test / 테스트) kiểm tra lô-gic (logic / 논리) cục bộ. tích hợp (integration / 통합)/đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) kiểm tra ranh giới (boundary / 경계). bảo mật (security / 보안)/supply-chain checks xác minh chính sách (policy / 정책). bản dựng (build / 빌드) tạo sản phẩm tạo ra (artifact / 산출물). Một số stage có thể chạy song song nếu phụ thuộc (dependency / 의존성) cho phép.

Điểm quan trọng là mỗi stage phải có thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) rõ. “chuỗi xử lý (pipeline / 파이프라인) đỏ” nhưng không biết check nào đáng tin, ai sở hữu, có thử lại (retry / 재시도) được không sẽ tạo alert fatigue giống môi trường vận hành (production / 운영 환경) monitoring.

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **2. chuỗi xử lý (pipeline / 파이프라인) phải trả lời câu hỏi theo tầng** xác định đầu vào; **3. Flaky kiểm thử (test / 테스트) là độ tin cậy (reliability / 신뢰성) debt** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Continuous Delivery khác Continuous triển khai (deployment / 배포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Flaky kiểm thử (test / 테스트) là độ tin cậy (reliability / 신뢰성) debt

Kiểm thử (test / 테스트) lúc pass lúc thất bại (fail / 실패) mà nguồn (source / 소스) không đổi làm chuỗi xử lý (pipeline / 파이프라인) mất vai trò oracle. nhóm (team / 팀) bắt đầu rerun đến khi xanh và CI trở thành nghi thức. Flaky kiểm thử (test / 테스트) cần được đo, quarantine có kiểm soát và sửa có đơn vị sở hữu (owner / 오너). Không nên giữ bản dựng (build / 빌드) đỏ vô hạn, nhưng cũng không được coi rerun là remediation.

Một cấp cao (senior / 시니어) practice là theo dõi false positive/false negative của kiểm tra hợp lệ (validation / 검증) hệ thống (system / 시스템). chuỗi xử lý (pipeline / 파이프라인) cũng là môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) phục vụ nhà phát triển (developer / 개발자); nó có SLO về thời gian, availability và tín hiệu (signal / 신호) chất lượng (quality / 품질).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **4. Continuous Delivery khác Continuous triển khai (deployment / 배포)** tiếp nhận điểm tựa từ **3. Flaky kiểm thử (test / 테스트) là độ tin cậy (reliability / 신뢰성) debt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. môi trường (environment / 환경) promotion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Continuous Delivery khác Continuous triển khai (deployment / 배포)

Continuous Delivery nghĩa mainline luôn ở trạng thái có thể phát hành thông qua tiến trình (process / 프로세스) tự động đáng tin. Continuous triển khai (deployment / 배포) đi thêm một bước: thay đổi đạt chính sách (policy / 정책) sẽ tự động vào môi trường vận hành (production / 운영 환경) mà không cần quyết định thủ công cho từng bản phát hành (release / 릴리스).

Tổ chức có thể chọn delivery mà không triển khai (deployment / 배포) tự động vì regulation hoặc rủi ro (risk / 위험) mô hình (model / 모델). Điều quan trọng là approval nếu có phải nằm đúng nơi: xác nhận nghiệp vụ (business / 비즈니스)/rủi ro (risk / 위험) quyết định (decision / 결정), không phải bù cho chuỗi xử lý (pipeline / 파이프라인) thiếu kiểm thử (test / 테스트).

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **5. môi trường (environment / 환경) promotion** tiếp nhận điểm tựa từ **4. Continuous Delivery khác Continuous triển khai (deployment / 배포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. triển khai (deployment / 배포) không kết thúc khi API trả thành công** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. môi trường (environment / 환경) promotion

Một anti-pattern là mỗi môi trường bản dựng (build / 빌드) lại nguồn (source / 소스). Confidence tốt hơn khi bản dựng (build / 빌드) một lần và promote cùng sản phẩm tạo ra (artifact / 산출물). môi trường (environment / 환경) khác nhau chủ yếu qua cấu hình (config / 설정), credential, sức chứa (capacity / 용량) và bên ngoài (external / 외부) tích hợp (integration / 통합).

Promotion cần bằng chứng (evidence / 증거). Ví dụ sản phẩm tạo ra (artifact / 산출물) A qua kiểm thử tích hợp (integration test / 통합 테스트), deploy staging, chạy smoke/e2e, rồi mới đủ điều kiện môi trường vận hành (production / 운영 환경). bằng chứng (evidence / 증거) có thể được lưu cùng bản phát hành (release / 릴리스) siêu dữ liệu (metadata / 메타데이터). Khi môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트), ta cần biết chính xác sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정), di chuyển (migration / 마이그레이션) và triển khai (deployment / 배포) sự kiện (event / 이벤트) nào vừa xảy ra.

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **6. triển khai (deployment / 배포) không kết thúc khi API trả thành công** tiếp nhận điểm tựa từ **5. môi trường (environment / 환경) promotion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. quay lui (rollback / 롤백) không luôn là inverse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. triển khai (deployment / 배포) không kết thúc khi API trả thành công

Một triển khai (deployment / 배포) command thành công chỉ chứng minh điều khiển (control / 제어) plane chấp nhận desired trạng thái (state / 상태). Safe delivery cần xác minh actual hành vi (behavior / 동작) sau rollout. Có thể tải công việc (workload / 워크로드) chưa ready, traffic lỗi (error / 오류) tăng hoặc phụ thuộc (dependency / 의존성) saturation xuất hiện sau vài phút.

Triển khai (deployment / 배포) xác minh (verification / 확인) nên dùng môi trường vận hành (production / 운영 환경) tín hiệu (signal / 신호) liên quan người dùng (user / 사용자) impact. Canary, blue-green, rolling cập nhật (update / 업데이트) và cờ tính năng (feature flag / 기능 플래그) là các cơ chế (mechanism / 메커니즘) giảm blast radius. lý thuyết (theory / 이론) và sự đánh đổi (trade-off / 트레이드오프) đã có chuẩn gốc (canonical / 정본) chapter [deployment safety, canary, blue-green, flags và rollback](../../computer_science/09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md).

DevOps tầng (layer / 계층) phải nối cơ chế (mechanism / 메커니즘) đó vào chuỗi xử lý (pipeline / 파이프라인)/controller để promotion dựa trên bằng chứng (evidence / 증거) chứ không dựa vào “deploy command exited 0”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **7. quay lui (rollback / 롤백) không luôn là inverse** tiếp nhận điểm tựa từ **6. triển khai (deployment / 배포) không kết thúc khi API trả thành công** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. cờ tính năng (feature flag / 기능 플래그) tách deploy khỏi bản phát hành (release / 릴리스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. quay lui (rollback / 롤백) không luôn là inverse

Nếu bản phát hành (release / 릴리스) chỉ thay stateless mã (code / 코드) tương thích, quay lui (rollback / 롤백) ảnh (image / 이미지) có thể dễ. Nhưng nếu bản phát hành (release / 릴리스) đã migrate cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마), publish sự kiện (event / 이벤트) theo lược đồ (schema / 스키마) mới hoặc gọi bên ngoài (external / 외부) side tác động (effect / 효과), quay lui (rollback / 롤백) mã (code / 코드) có thể làm tình hình tệ hơn.

Safe thay đổi (change / 변경) cần backward/forward tính tương thích (compatibility / 호환성). cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) thường nên theo expand-and-contract: thêm năng lực (capability / 역량) tương thích trước, chuyển traffic/mã (code / 코드), sau đó mới bỏ cấu trúc cũ khi chắc chắn không còn bên tiêu thụ (consumer / 소비자). Khi trạng thái (state / 상태) đã biến đổi không thể đảo, roll-forward có thể an toàn hơn quay lui (rollback / 롤백).

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **8. cờ tính năng (feature flag / 기능 플래그) tách deploy khỏi bản phát hành (release / 릴리스)** tiếp nhận điểm tựa từ **7. quay lui (rollback / 롤백) không luôn là inverse** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. thay đổi (change / 변경) siêu dữ liệu (metadata / 메타데이터) là telemetry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. cờ tính năng (feature flag / 기능 플래그) tách deploy khỏi bản phát hành (release / 릴리스)

Deploy là đưa mã (code / 코드) vào môi trường (environment / 환경). bản phát hành (release / 릴리스) là làm hành vi (behavior / 동작) mới có hiệu lực với người dùng (user / 사용자). cờ tính năng (feature flag / 기능 플래그) cho phép hai thời điểm khác nhau. Điều này giảm blast radius và cho progressive exposure, nhưng flag tạo trạng thái (state / 상태) và độ phức tạp (complexity / 복잡도) riêng.

Flag cần đơn vị sở hữu (owner / 오너), expiry và cleanup. Flag tồn tại nhiều tháng có thể tạo combinatorial hành vi (behavior / 동작) mà kiểm thử (test / 테스트) không bao phủ. nền tảng (platform / 플랫폼) nên hỗ trợ vòng đời (lifecycle / 생명주기) chứ không chỉ cung cấp SDK.

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **8. cờ tính năng (feature flag / 기능 플래그) tách deploy khỏi bản phát hành (release / 릴리스)** nêu điều cần giải thích; **9. thay đổi (change / 변경) siêu dữ liệu (metadata / 메타데이터) là telemetry** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. chuỗi xử lý (pipeline / 파이프라인) ranh giới bảo mật (security boundary / 보안 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. thay đổi (change / 변경) siêu dữ liệu (metadata / 메타데이터) là telemetry

Mỗi triển khai (deployment / 배포) nên phát sự kiện (event / 이벤트) có dịch vụ (service / 서비스), sản phẩm tạo ra (artifact / 산출물) phiên bản (version / 버전), lần ghi nhận (commit / 커밋), môi trường (environment / 환경), actor/automation, thời gian và kết quả (result / 결과). Khi dashboard độ trễ (latency / 지연 시간) tăng lúc 14:03, operator phải dễ overlay triển khai (deployment / 배포) sự kiện (event / 이벤트) để thấy correlation. Không có thay đổi (change / 변경) telemetry, investigation thường bắt đầu bằng câu “có ai vừa deploy gì không?”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **9. thay đổi (change / 변경) siêu dữ liệu (metadata / 메타데이터) là telemetry** đã nêu tiêu chí phân biệt, còn **10. chuỗi xử lý (pipeline / 파이프라인) ranh giới bảo mật (security boundary / 보안 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **11. Ví dụ lập luận (reasoning / 추론) một bản phát hành (release / 릴리스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. chuỗi xử lý (pipeline / 파이프라인) ranh giới bảo mật (security boundary / 보안 경계)

CI thường có quyền đọc nguồn (source / 소스), đơn vị từ (token / 토큰) registry, cloud credential hoặc deploy permission. Vì vậy runner và workflow là ranh giới bảo mật (security boundary / 보안 경계). Pull yêu cầu (request / 요청) từ mã (code / 코드) chưa tin cậy không nên tự động nhận môi trường vận hành (production / 운영 환경) secret. phụ thuộc (dependency / 의존성) hành động (action / 동작)/plugin phải được pin và kiểm soát. Least privilege nên áp dụng cho job định danh (identity / 식별자) theo stage.

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, sau khi thấy quy trình trong **10. chuỗi xử lý (pipeline / 파이프라인) ranh giới bảo mật (security boundary / 보안 경계)**, **11. Ví dụ lập luận (reasoning / 추론) một bản phát hành (release / 릴리스)** đặt nó vào một trường hợp đủ cụ thể để nhận ra điều kiện thành công và chỗ dễ sai. Từ đây, **12. cấp cao (senior / 시니어) ghi chú (note / 노트): tối ưu lead thời gian (time / 시간) bằng giảm hàng đợi (queue / 큐), không bỏ bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Ví dụ lập luận (reasoning / 추론) một bản phát hành (release / 릴리스)

Giả sử `orders-api` thay lô-gic (logic / 논리) tính phí. CI xác minh đơn vị (unit / 단위)/đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) rồi bản dựng (build / 빌드) ảnh (image / 이미지) digest D. D được scan và publish một lần. Staging deploy D với cấu hình (config / 설정) staging. Smoke kiểm thử (test / 테스트) và đặc tả hợp đồng (contract / 계약) với phụ thuộc (dependency / 의존성) pass. môi trường vận hành (production / 운영 환경) rollout bắt đầu 5% traffic, theo dõi lỗi (error / 오류) tỷ lệ (rate / 비율), độ trễ (latency / 지연 시간) và nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식). Nếu tín hiệu (signal / 신호) xấu, controller dừng promotion; quay lui (rollback / 롤백) hoặc disable tính năng (feature / 기능) tùy trạng thái (state / 상태) tính tương thích (compatibility / 호환성).

Điểm cốt lõi không nằm ở Jenkins/GitHub Actions/Argo Rollouts. Nó nằm ở định danh (identity / 식별자) của sản phẩm tạo ra (artifact / 산출물), staged bằng chứng (evidence / 증거), blast-radius điều khiển (control / 제어) và khôi phục (recovery / 복구) đường dẫn (path / 경로).

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **11. Ví dụ lập luận (reasoning / 추론) một bản phát hành (release / 릴리스)** cho ta quy tắc; **12. cấp cao (senior / 시니어) ghi chú (note / 노트): tối ưu lead thời gian (time / 시간) bằng giảm hàng đợi (queue / 큐), không bỏ bằng chứng (evidence / 증거)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **13. chuỗi xử lý (pipeline / 파이프라인) là DAG có đường găng (critical path / 임계 경로), không phải một danh sách stage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. cấp cao (senior / 시니어) ghi chú (note / 노트): tối ưu lead thời gian (time / 시간) bằng giảm hàng đợi (queue / 큐), không bỏ bằng chứng (evidence / 증거)

Khi chuỗi xử lý (pipeline / 파이프라인) chậm, phản xạ nguy hiểm là bỏ kiểm thử (test / 테스트). Trước tiên tìm đường găng (critical path / 임계 경로): setup phụ thuộc (dependency / 의존성), duplicate bản dựng (build / 빌드), serialized job, scarce runner, flaky rerun hay bộ kiểm thử (test suite / 테스트 스위트) không partition. Tối ưu phản hồi (feedback / 피드백) thời gian (time / 시간) bằng bộ nhớ đệm (cache / 캐시) đúng, parallelism, kiểm thử (test / 테스트) selection và kiến trúc (architecture / 아키텍처) tốt hơn.

Delivery hiệu năng (performance / 성능) cao và độ tin cậy (reliability / 신뢰성) không phải hai mục tiêu đối nghịch nếu hệ thống được thiết kế để thay đổi nhỏ, phản hồi (feedback / 피드백) nhanh và quay lui (rollback / 롤백)/rủi ro (risk / 위험) ranh giới (boundary / 경계) rõ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **12. cấp cao (senior / 시니어) ghi chú (note / 노트): tối ưu lead thời gian (time / 시간) bằng giảm hàng đợi (queue / 큐), không bỏ bằng chứng (evidence / 증거)** nêu điều cần giải thích; **13. chuỗi xử lý (pipeline / 파이프라인) là DAG có đường găng (critical path / 임계 경로), không phải một danh sách stage** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. kiểm tra hợp lệ (validation / 검증) có thể stale khi cơ sở (base / 기반) thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. chuỗi xử lý (pipeline / 파이프라인) là DAG có đường găng (critical path / 임계 경로), không phải một danh sách stage

Một chuỗi xử lý (pipeline / 파이프라인) có thể có 30 job nhưng lead thời gian (time / 시간) chủ yếu do chuỗi phụ thuộc (dependency / 의존성) dài nhất quyết định. Hai job 20 phút chạy song song chỉ thêm khoảng 20 phút vào đường găng (critical path / 임계 경로), còn chạy tuần tự thành 40 phút.

Vì vậy tối ưu chuỗi xử lý (pipeline / 파이프라인) nên vẽ phụ thuộc (dependency / 의존성) DAG: job nào thật sự cần đầu ra (output / 출력) của job trước, job nào có thể chạy song song, job nào rebuild cùng sản phẩm tạo ra (artifact / 산출물) và job nào chỉ chờ scarce runner. Việc đổi tên stage hoặc tăng runner không giúp nếu đường găng (critical path / 임계 경로) nằm ở tích hợp (integration / 통합) môi trường (environment / 환경) mất 40 phút provision.

Chuỗi xử lý (pipeline / 파이프라인) thiết kế (design / 설계) tốt tách **phản hồi (feedback / 피드백) fast đường dẫn (path / 경로)** cho nhà phát triển (developer / 개발자) khỏi **bằng chứng (evidence / 증거) deep đường dẫn (path / 경로)** nhưng vẫn giữ chính sách (policy / 정책) bản phát hành (release / 릴리스). Ví dụ lint/đơn vị (unit / 단위)/bảo mật (security / 보안) static chạy sớm; tích hợp (integration / 통합) suite nặng có thể parallel và promotion chỉ chờ đúng bằng chứng (evidence / 증거) cần thiết.

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **13. chuỗi xử lý (pipeline / 파이프라인) là DAG có đường găng (critical path / 임계 경로), không phải một danh sách stage** xác định đầu vào; **14. kiểm tra hợp lệ (validation / 검증) có thể stale khi cơ sở (base / 기반) thay đổi** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **15. Deploy tính đồng thời (concurrency / 동시성) phải có quyền sở hữu (ownership / 소유권) theo môi trường (environment / 환경)/dịch vụ (service / 서비스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. kiểm tra hợp lệ (validation / 검증) có thể stale khi cơ sở (base / 기반) thay đổi

Một pull yêu cầu (request / 요청) pass toàn bộ kiểm thử (test / 테스트) trên lần ghi nhận (commit / 커밋) X + cơ sở (base / 기반) B. Trong lúc chờ merge, cơ sở (base / 기반) có thêm thay đổi (change / 변경) C. Nếu merge tạo trạng thái (state / 상태) X+C nhưng chuỗi xử lý (pipeline / 파이프라인) không revalidate combination đó, “PR xanh” không chứng minh mainline mới xanh.

Đây là tích hợp (integration / 통합) race. Cách xử lý có thể là merge hàng đợi (queue / 큐), rebase/merge-latest-base rồi kiểm thử (test / 테스트) lại, hoặc post-merge xác minh (verification / 확인) nhanh tùy repository rủi ro (risk / 위험). mô hình tư duy (mental model / 사고 모델) quan trọng: **bằng chứng (evidence / 증거) phải gắn với chính xác (exact / 정확한) revision/composition được bản phát hành (release / 릴리스)**, không chỉ với branch từng xanh.

IaC/GitOps cũng có stale-plan bài toán (problem / 문제) tương tự; đây là mẫu (pattern / 패턴) chung của concurrent thay đổi (change / 변경).

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, sau nội dung của **14. kiểm tra hợp lệ (validation / 검증) có thể stale khi cơ sở (base / 기반) thay đổi**, **15. Deploy tính đồng thời (concurrency / 동시성) phải có quyền sở hữu (ownership / 소유권) theo môi trường (environment / 환경)/dịch vụ (service / 서비스)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **16. di chuyển (migration / 마이그레이션) nên được coi là một bản phát hành (release / 릴리스) đặc tả hợp đồng (contract / 계약) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Deploy tính đồng thời (concurrency / 동시성) phải có quyền sở hữu (ownership / 소유권) theo môi trường (environment / 환경)/dịch vụ (service / 서비스)

Hai chuỗi xử lý (pipeline / 파이프라인) cùng deploy một dịch vụ (service / 서비스)/môi trường (environment / 환경) có thể race. bản phát hành (release / 릴리스) A bắt đầu canary, bản phát hành (release / 릴리스) B tới sau thay desired trạng thái (state / 상태); chỉ số (metric / 지표) của A và B trộn lẫn làm xác minh (verification / 확인) không còn nghĩa.

Nền tảng (platform / 플랫폼) nên có tính đồng thời (concurrency / 동시성) chính sách (policy / 정책): serialize môi trường vận hành (production / 운영 환경) rollout theo dịch vụ (service / 서비스), cancel superseded run khi safe, hoặc dùng bản phát hành (release / 릴리스) controller có máy trạng thái (state machine / 상태 머신) rõ. “chuỗi xử lý (pipeline / 파이프라인) job chạy song song nhanh hơn” không áp dụng cho mutation cùng một quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계).

Nếu bản phát hành (release / 릴리스) B phụ thuộc A, tường minh (explicit / 명시적) phụ thuộc (dependency / 의존성)/phiên bản (version / 버전) tốt hơn để race ngẫu nhiên quyết định thứ tự (order / 순서).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **16. di chuyển (migration / 마이그레이션) nên được coi là một bản phát hành (release / 릴리스) đặc tả hợp đồng (contract / 계약) riêng** tiếp nhận điểm tựa từ **15. Deploy tính đồng thời (concurrency / 동시성) phải có quyền sở hữu (ownership / 소유권) theo môi trường (environment / 환경)/dịch vụ (service / 서비스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Canary cần guardrail chống false confidence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. di chuyển (migration / 마이그레이션) nên được coi là một bản phát hành (release / 릴리스) đặc tả hợp đồng (contract / 계약) riêng

Cơ sở dữ liệu (database / 데이터베이스)/lược đồ (schema / 스키마)/message di chuyển (migration / 마이그레이션) có vòng đời (lifecycle / 생명주기) dài hơn tiến trình (process / 프로세스) deploy. Expand-and-contract thường gồm ít nhất: thêm lược đồ (schema / 스키마) mới tương thích, deploy producer/bên tiêu thụ (consumer / 소비자) hiểu cả hai, migrate/backfill dữ liệu (data / 데이터) nếu cần, verify usage, rồi mới remove old đường dẫn (path / 경로).

Chuỗi xử lý (pipeline / 파이프라인) không nên coi di chuyển (migration / 마이그레이션) thành một shell command chạy trước deploy mà không có idempotency, khóa (lock / 잠금)/quyền sở hữu (ownership / 소유권) và resume ngữ nghĩa (semantics / 의미론). di chuyển (migration / 마이그레이션) thất bại (failure / 실패) giữa chừng có thể để trạng thái (state / 상태) partial; rerun phải an toàn hoặc có khôi phục (recovery / 복구) plan.

Thay đổi (change / 변경) siêu dữ liệu (metadata / 메타데이터) nên lưu di chuyển (migration / 마이그레이션) phiên bản (version / 버전)/trạng thái cùng sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정) để sự cố (incident / 인시던트) biết mã (code / 코드) nào tương thích dữ liệu (data / 데이터) trạng thái (state / 상태) nào.

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **17. Canary cần guardrail chống false confidence** tiếp nhận điểm tựa từ **16. di chuyển (migration / 마이그레이션) nên được coi là một bản phát hành (release / 릴리스) đặc tả hợp đồng (contract / 계약) riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. quay lui (rollback / 롤백) quyết định (decision / 결정) cần tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Canary cần guardrail chống false confidence

Canary 1% traffic chỉ có giá trị nếu mẫu (sample / 표본) chạm tải công việc (workload / 워크로드) đại diện. Rare tenant, ghi (write / 쓰기) đường dẫn (path / 경로), batch job hoặc region nhỏ có thể không xuất hiện. chỉ số (metric / 지표) aggregate toàn fleet cũng có thể che canary thất bại (failure / 실패) vì 1% tín hiệu (signal / 신호) bị 99% stable traffic pha loãng.

Xác minh (verification / 확인) nên dimension theo phiên bản (version / 버전)/canary cohort và chọn nghiệp vụ (business / 비즈니스)/technical bất biến (invariant / 불변식) phù hợp. Một canary healthy 10 phút không chứng minh bộ nhớ (memory / 메모리) leak xảy ra sau 6 giờ; observation cửa sổ (window / 윈도우) phải phù hợp thất bại (failure / 실패) lớp (class / 클래스).

Canary là cách giảm blast radius và tăng bằng chứng (evidence / 증거), không phải chứng minh tuyệt đối bản phát hành (release / 릴리스) an toàn.

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **18. quay lui (rollback / 롤백) quyết định (decision / 결정) cần tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **17. Canary cần guardrail chống false confidence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. chuỗi xử lý (pipeline / 파이프라인) SLO và lỗi (error / 오류) ngân sách (budget / 예산) cũng áp dụng cho nhà phát triển (developer / 개발자) experience** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. quay lui (rollback / 롤백) quyết định (decision / 결정) cần tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)

Trước môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스), nhóm (team / 팀) nên biết ít nhất bốn lớp có thể quay lui (rollback / 롤백) độc lập đến đâu: ứng dụng (application / 애플리케이션) sản phẩm tạo ra (artifact / 산출물), cấu hình (configuration / 구성), cơ sở dữ liệu (database / 데이터베이스)/lược đồ (schema / 스키마)/dữ liệu (data / 데이터) và bên ngoài (external / 외부) giao thức (protocol / 프로토콜)/sự kiện (event / 이벤트) đặc tả hợp đồng (contract / 계약).

Có thể biểu diễn mô hình tư duy (mental model / 사고 모델):

```text
code N+1 ↔ config C2 ↔ schema S2 ↔ event/API E2
```

Quay lui (rollback / 롤백) mã (code / 코드) về N chỉ an toàn nếu N còn hiểu C2/S2/E2 hoặc các lớp kia cũng có khôi phục (recovery / 복구) đường dẫn (path / 경로) tương thích. Nếu lược đồ (schema / 스키마) S2 đã drop column N cần, quay lui (rollback / 롤백) ảnh (image / 이미지) nhanh sẽ thất bại (fail / 실패) ngay.

Cấp cao (senior / 시니어) delivery rà soát (review / 검토) không chỉ hỏi “có nút quay lui (rollback / 롤백) không?” mà hỏi “quay lui (rollback / 롤백) mục tiêu (target / 대상) có còn compatible với actual trạng thái (state / 상태) sau bản phát hành (release / 릴리스) không?”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **18. quay lui (rollback / 롤백) quyết định (decision / 결정) cần tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** xác định đầu vào; **19. chuỗi xử lý (pipeline / 파이프라인) SLO và lỗi (error / 오류) ngân sách (budget / 예산) cũng áp dụng cho nhà phát triển (developer / 개발자) experience** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **20. Superseded công việc (work / 작업) nên được hủy khi bằng chứng (evidence / 증거) của nó không còn giá trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. chuỗi xử lý (pipeline / 파이프라인) SLO và lỗi (error / 오류) ngân sách (budget / 예산) cũng áp dụng cho nhà phát triển (developer / 개발자) experience

Nếu CI availability thấp hoặc p95 phản hồi (feedback / 피드백) 50 phút, nhà phát triển (developer / 개발자) batch thay đổi (change / 변경) lớn hơn và rerun nhiều hơn, làm tích hợp (integration / 통합) rủi ro (risk / 위험) tăng. chuỗi xử lý (pipeline / 파이프라인) là dùng chung (shared / 공유) môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) có downstream impact lên delivery hành vi (behavior / 동작).

Nền tảng (platform / 플랫폼) nhóm (team / 팀) có thể đo hàng đợi (queue / 큐) thời gian (time / 시간), thực thi (execution / 실행) thời gian (time / 시간), flaky rerun tỷ lệ (rate / 비율), runner saturation và thất bại (failure / 실패) do nền tảng (platform / 플랫폼) vs nguồn (source / 소스). Mục tiêu không phải chuỗi xử lý (pipeline / 파이프라인) luôn xanh; nguồn (source / 소스) bug phải làm đỏ. Mục tiêu là **tín hiệu (signal / 신호) đúng, nhanh và đáng tin** để nhà phát triển (developer / 개발자) không học thói quen bypass.

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, cơ chế trong **19. chuỗi xử lý (pipeline / 파이프라인) SLO và lỗi (error / 오류) ngân sách (budget / 예산) cũng áp dụng cho nhà phát triển (developer / 개발자) experience** cần được kiểm chứng bằng dấu vết cụ thể; **20. Superseded công việc (work / 작업) nên được hủy khi bằng chứng (evidence / 증거) của nó không còn giá trị** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **21. Approval cũng có thể stale** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Superseded công việc (work / 작업) nên được hủy khi bằng chứng (evidence / 증거) của nó không còn giá trị

Nhà phát triển (developer / 개발자) push lần ghi nhận (commit / 커밋) B sau lần ghi nhận (commit / 커밋) A nhưng chuỗi xử lý (pipeline / 파이프라인) A vẫn chiếm runner 40 phút. Nếu kết quả A không còn được dùng để merge/bản phát hành (release / 릴리스), tiếp tục chạy chỉ làm tăng hàng đợi (queue / 큐) cho bằng chứng (evidence / 증거) mới hơn. Tuy nhiên không phải job nào cũng cancel an toàn; di chuyển (migration / 마이그레이션)/kiểm thử (test / 테스트) môi trường (environment / 환경) có side tác động (effect / 효과) cần cleanup.

Chuỗi xử lý (pipeline / 파이프라인) nên phân biệt công việc (work / 작업) **pure xác minh (verification / 확인)** có thể cancel với công việc (work / 작업) **mutation** cần máy trạng thái (state machine / 상태 머신)/cleanup. Cancel-on-new-commit cho lint/đơn vị (unit / 단위) thường hợp lý; cancel một môi trường vận hành (production / 운영 환경) triển khai (deployment / 배포) giữa di chuyển (migration / 마이그레이션) cần ngữ nghĩa (semantics / 의미론) rõ.

Đây là hàng đợi (queue / 큐) discipline: giảm WIP không phải bằng bỏ kiểm thử (test / 테스트) mà bằng ngừng tiêu sức chứa (capacity / 용량) cho bằng chứng (evidence / 증거) đã stale.

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **20. Superseded công việc (work / 작업) nên được hủy khi bằng chứng (evidence / 증거) của nó không còn giá trị** nêu điều cần giải thích; **21. Approval cũng có thể stale** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. dùng chung (shared / 공유) tích hợp (integration / 통합) môi trường (environment / 환경) là nguồn nondeterminism và coupling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Approval cũng có thể stale

Một người approve bản phát hành (release / 릴리스) khi bằng chứng (evidence / 증거) gắn với sản phẩm tạo ra (artifact / 산출물) D và cấu hình (config / 설정) C. Sau đó chuỗi xử lý (pipeline / 파이프라인) rerun bản dựng (build / 빌드) tạo D2 hoặc cấu hình (config / 설정) thay C2 nhưng approval cũ vẫn được reuse. Khi đó approval không còn xác nhận subject thực sự được deploy.

Manual gate chỉ có ý nghĩa nếu nó bind tới chính xác (exact / 정확한) bản phát hành (release / 릴리스) subject: sản phẩm tạo ra (artifact / 산출물) digest, cấu hình (config / 설정)/revision, di chuyển (migration / 마이그레이션) trạng thái (state / 상태) và rủi ro (risk / 위험) ngữ cảnh (context / 맥락) liên quan. Nếu subject đổi đáng kể, approval/bằng chứng (evidence / 증거) cần được đánh giá lại theo chính sách (policy / 정책).

Điều này giống cryptographic attestation ở cấp quy trình: statement “tôi chấp nhận rủi ro (risk / 위험)” phải nói rõ chấp nhận **cái gì**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **21. Approval cũng có thể stale** nêu điều cần giải thích; **22. dùng chung (shared / 공유) tích hợp (integration / 통합) môi trường (environment / 환경) là nguồn nondeterminism và coupling** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **23. bản phát hành (release / 릴리스) controller cần trạng thái paused, không chỉ pass/thất bại (fail / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. dùng chung (shared / 공유) tích hợp (integration / 통합) môi trường (environment / 환경) là nguồn nondeterminism và coupling

Hai chuỗi xử lý (pipeline / 파이프라인) dùng cùng cơ sở dữ liệu (database / 데이터베이스)/kiểm thử (test / 테스트) tenant có thể ảnh hưởng nhau: kiểm thử (test / 테스트) A xóa dữ liệu (data / 데이터) kiểm thử (test / 테스트) B, lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) race, tỷ lệ (rate / 비율) limit chung hoặc background job chạy chéo. Kết quả flaky không nhất thiết do kiểm thử (test / 테스트) mã (code / 코드) mà do môi trường (environment / 환경) không có isolation đặc tả hợp đồng (contract / 계약).

Có ba chiến lược chính: môi trường (environment / 환경) per thay đổi (change / 변경), dùng chung (shared / 공유) môi trường (environment / 환경) nhưng không gian tên (namespace / 네임스페이스)/dữ liệu (data / 데이터) isolation mạnh, hoặc serialize lớp (class / 클래스) kiểm thử (test / 테스트) có xung đột (conflict / 충돌). Mỗi lựa chọn đổi chi phí (cost / 비용), fidelity và phản hồi (feedback / 피드백) thời gian (time / 시간).

Không cần mọi PR có full môi trường vận hành (production / 운영 환경) clone. Nhưng kiểm thử (test / 테스트) tín hiệu (signal / 신호) phải biết phụ thuộc (dependency / 의존성) nào dùng chung (shared / 공유) và thất bại (failure / 실패) do môi trường (environment / 환경) phải được phân biệt với thất bại (failure / 실패) của nguồn (source / 소스) thay đổi (change / 변경).

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **22. dùng chung (shared / 공유) tích hợp (integration / 통합) môi trường (environment / 환경) là nguồn nondeterminism và coupling** nêu điều cần giải thích; **23. bản phát hành (release / 릴리스) controller cần trạng thái paused, không chỉ pass/thất bại (fail / 실패)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. Health xác minh (verification / 확인) cần phân biệt bản phát hành (release / 릴리스) fault với nền tảng (platform / 플랫폼)/phụ thuộc (dependency / 의존성) fault** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. bản phát hành (release / 릴리스) controller cần trạng thái `paused`, không chỉ pass/thất bại (fail / 실패)

Trong progressive delivery, tín hiệu (signal / 신호) có thể chưa đủ rõ để promote cũng chưa đủ xấu để quay lui (rollback / 롤백). Nếu máy trạng thái (state machine / 상태 머신) chỉ có “continue” hoặc “thất bại (fail / 실패)”, operator dễ chọn hành động (action / 동작) vội.

`Paused` cho phép giữ cohort hiện tại, thu thêm bằng chứng (evidence / 증거) hoặc điều tra phụ thuộc (dependency / 의존성) mà không tăng blast radius. Tuy nhiên pause có chi phí (cost / 비용): hai phiên bản (version / 버전) cùng tồn tại lâu hơn, lược đồ (schema / 스키마)/cấu hình (config / 설정) tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) kéo dài và sức chứa (capacity / 용량) surge tiếp tục bị giữ.

Do đó bản phát hành (release / 릴리스) trạng thái (state / 상태) cần hết thời gian chờ (timeout / 타임아웃)/đơn vị sở hữu (owner / 오너): ai quyết định tiếp, bằng chứng (evidence / 증거) nào cần thêm và sau bao lâu phải quay lui (rollback / 롤백)/roll-forward. “Để canary treo” không phải chiến lược (strategy / 전략).

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **24. Health xác minh (verification / 확인) cần phân biệt bản phát hành (release / 릴리스) fault với nền tảng (platform / 플랫폼)/phụ thuộc (dependency / 의존성) fault** tiếp nhận điểm tựa từ **23. bản phát hành (release / 릴리스) controller cần trạng thái paused, không chỉ pass/thất bại (fail / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Merge hàng đợi (queue / 큐) là một controller cho tích hợp (integration / 통합) tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Health xác minh (verification / 확인) cần phân biệt bản phát hành (release / 릴리스) fault với nền tảng (platform / 플랫폼)/phụ thuộc (dependency / 의존성) fault

Nếu canary lỗi (error / 오류) tăng đúng lúc bên ngoài (external / 외부) payment provider outage toàn fleet, tự động quay lui (rollback / 롤백) canary có thể không cải thiện gì và còn tạo thêm churn. Ngược lại aggregate fleet lỗi (error / 오류) có thể che lỗi chỉ ở canary.

Xác minh (verification / 확인) tốt dùng comparative/cohort lập luận (reasoning / 추론): canary vs baseline trong cùng region/tenant/phụ thuộc (dependency / 의존성) cửa sổ (window / 윈도우), kết hợp absolute SLO guardrail. Nếu cả old và new cùng xấu, suspect dùng chung (shared / 공유) phụ thuộc (dependency / 의존성)/nền tảng (platform / 플랫폼); nếu new xấu riêng, bằng chứng (evidence / 증거) cho bản phát hành (release / 릴리스) fault mạnh hơn.

Automation vẫn có thể chọn conservative stop, nhưng reason phải observable để operator biết quay lui (rollback / 롤백) dự kiến tác động gì.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **25. Merge hàng đợi (queue / 큐) là một controller cho tích hợp (integration / 통합) tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **24. Health xác minh (verification / 확인) cần phân biệt bản phát hành (release / 릴리스) fault với nền tảng (platform / 플랫폼)/phụ thuộc (dependency / 의존성) fault** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. cấp cao (senior / 시니어) walkthrough: bản phát hành (release / 릴리스) được approve nhưng deploy sản phẩm tạo ra (artifact / 산출물) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Merge hàng đợi (queue / 큐) là một controller cho tích hợp (integration / 통합) tính đồng thời (concurrency / 동시성)

Khi nhiều PR cùng xanh trên cơ sở (base / 기반) cũ, merge hàng đợi (queue / 큐) tạo candidate composition gần trạng thái (state / 상태) sẽ vào main rồi verify theo thứ tự. Nó không “làm kiểm thử (test / 테스트) tốt hơn”; nó quản tính đồng thời (concurrency / 동시성) và freshness của bằng chứng (evidence / 증거).

Hàng đợi (queue / 큐) cũng có thông lượng (throughput / 처리량)/sức chứa (capacity / 용량). Nếu kiểm thử (test / 테스트) lâu và arrival tỷ lệ (rate / 비율) PR cao hơn merge dịch vụ (service / 서비스) tỷ lệ (rate / 비율), wait thời gian (time / 시간) tăng. Tối ưu cần giảm đường găng (critical path / 임계 경로), tăng parallelism an toàn hoặc giảm batch kích thước (size / 크기); bypass hàng đợi (queue / 큐) khi đông chỉ chuyển hàng đợi (queue / 큐) từ CI sang broken mainline.

Đây là cùng mô hình tư duy (mental model / 사고 모델) với môi trường vận hành (production / 운영 환경) admission điều khiển (control / 제어): khi tài nguyên (resource / 자원) xác minh (verification / 확인) hữu hạn, cần chính sách (policy / 정책) chọn công việc (work / 작업) nào được vào và bằng chứng nào còn fresh.

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **26. cấp cao (senior / 시니어) walkthrough: bản phát hành (release / 릴리스) được approve nhưng deploy sản phẩm tạo ra (artifact / 산출물) khác** tiếp nhận điểm tựa từ **25. Merge hàng đợi (queue / 큐) là một controller cho tích hợp (integration / 통합) tính đồng thời (concurrency / 동시성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Online lược đồ (schema / 스키마) thay đổi (change / 변경) phải xét khóa (lock / 잠금), rewrite và thời gian chạy (runtime / 런타임) chi phí (cost / 비용) chứ không chỉ DDL hợp lệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. cấp cao (senior / 시니어) walkthrough: bản phát hành (release / 릴리스) được approve nhưng deploy sản phẩm tạo ra (artifact / 산출물) khác

Giả sử sản phẩm tạo ra (artifact / 산출물) D1 pass staging và được approve. Sau approval, chuỗi xử lý (pipeline / 파이프라인) dùng lệnh bản dựng (build / 빌드) lại trước môi trường vận hành (production / 운영 환경), tạo D2 vì cơ sở (base / 기반) ảnh (image / 이미지) đã đổi. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) xảy ra và nhật ký kiểm tra (audit log / 감사 로그) chỉ ghi lần ghi nhận (commit / 커밋) giống nhau.

Lỗi cấu trúc là gate bind tới nguồn (source / 소스) lần ghi nhận (commit / 커밋) thay vì immutable sản phẩm tạo ra (artifact / 산출물) subject. Correct luồng (flow / 흐름) là bản dựng (build / 빌드)/publish D1 một lần, gắn bằng chứng (evidence / 증거)/approval vào D1 rồi promote chính digest đó. Nếu buộc rebuild, D2 phải được coi bản phát hành (release / 릴리스) subject mới và kiểm tra hợp lệ (validation / 검증) tương ứng phải chạy lại.

Bài học là CI/CD maturity phụ thuộc **bằng chứng (evidence / 증거) định danh (identity / 식별자) + freshness + quyền sở hữu (ownership / 소유권)**, không phụ thuộc số stage hay số nút approval.

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **27. Online lược đồ (schema / 스키마) thay đổi (change / 변경) phải xét khóa (lock / 잠금), rewrite và thời gian chạy (runtime / 런타임) chi phí (cost / 비용) chứ không chỉ DDL hợp lệ** tiếp nhận điểm tựa từ **26. cấp cao (senior / 시니어) walkthrough: bản phát hành (release / 릴리스) được approve nhưng deploy sản phẩm tạo ra (artifact / 산출물) khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Backfill là một tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) cần throttle, checkpoint và bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Online lược đồ (schema / 스키마) thay đổi (change / 변경) phải xét khóa (lock / 잠금), rewrite và thời gian chạy (runtime / 런타임) chi phí (cost / 비용) chứ không chỉ DDL hợp lệ

Một di chuyển (migration / 마이그레이션) có thể đúng về cú pháp nhưng nguy hiểm về vận hành. `ALTER TABLE` tùy cơ sở dữ liệu (database / 데이터베이스)/phiên bản (version / 버전) có thể lấy khóa (lock / 잠금) mạnh, rewrite lượng dữ liệu lớn, tăng WAL/replication lag hoặc giữ giao dịch (transaction / 트랜잭션) lâu. Vì vậy câu hỏi môi trường vận hành (production / 운영 환경) không phải chỉ là “di chuyển (migration / 마이그레이션) chạy được không?” mà là “nó tranh tài nguyên (resource / 자원) gì, trong bao lâu và thất bại (failure / 실패) giữa chừng để lại trạng thái (state / 상태) nào?”.

Chuỗi xử lý (pipeline / 파이프라인) nên tách kiểm tra hợp lệ (validation / 검증) lược đồ (schema / 스키마) khỏi thực thi (execution / 실행) rủi ro (risk / 위험). Với bảng lớn, cần estimate row/dữ liệu (data / 데이터) volume, khóa (lock / 잠금) hành vi (behavior / 동작), replication headroom và maintenance/thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론); có thể dùng online di chuyển (migration / 마이그레이션) cơ chế (mechanism / 메커니즘) hoặc chia thay đổi thành nhiều phase. cơ sở dữ liệu (database / 데이터베이스) internals cụ thể thuộc chuẩn gốc (canonical / 정본) dữ liệu (data / 데이터) & Databases, nhưng delivery đặc tả hợp đồng (contract / 계약) phải nhìn thấy operational consequence.

Một di chuyển (migration / 마이그레이션) chạy tốt trên staging nhỏ không chứng minh môi trường vận hành (production / 운영 환경) an toàn nếu chi phí (cost / 비용) tăng theo dữ liệu (data / 데이터) kích thước (size / 크기). bằng chứng (evidence / 증거) phải đại diện volume và tính đồng thời (concurrency / 동시성) thực tế hoặc có mô hình (model / 모델) đủ bảo thủ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **28. Backfill là một tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) cần throttle, checkpoint và bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **27. Online lược đồ (schema / 스키마) thay đổi (change / 변경) phải xét khóa (lock / 잠금), rewrite và thời gian chạy (runtime / 런타임) chi phí (cost / 비용) chứ không chỉ DDL hợp lệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Dual-write tạo cửa sổ inconsistency cần reconciliation chứ không chỉ kiểm thử (test / 테스트) happy đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Backfill là một tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) cần throttle, checkpoint và bất biến (invariant / 불변식)

Sau khi thêm trường dữ liệu (field / 필드)/lược đồ (schema / 스키마) mới, backfill hàng triệu bản ghi (record / 레코드) thường kéo dài lâu hơn deploy ứng dụng (application / 애플리케이션). Nếu chạy tối đa tốc độ, backfill có thể chiếm I/O, liên kết (connection / 연결) và khóa (lock / 잠금) ngân sách (budget / 예산) của traffic người dùng (user / 사용자). Nếu dừng giữa chừng mà không có checkpoint, rerun có thể làm duplicate side tác động (effect / 효과) hoặc phải quét lại toàn bộ.

Backfill trưởng thành có stable progress định danh (identity / 식별자), chunk/checkpoint, tỷ lệ (rate / 비율)/tính đồng thời (concurrency / 동시성) limit, resume ngữ nghĩa (semantics / 의미론) và chỉ số (metric / 지표) về remaining công việc (work / 작업)/lỗi (error / 오류). Quan trọng hơn, phải định nghĩa bất biến (invariant / 불변식) trong giai đoạn mixed trạng thái (state / 상태): bản ghi (record / 레코드) cũ chưa migrate được đọc thế nào, bản ghi (record / 레코드) mới được ghi theo lược đồ (schema / 스키마) nào, và khi nào có thể tuyên bố old biểu diễn (representation / 표현) không còn cần.

Triển khai (deployment / 배포) controller không nhất thiết chạy backfill trực tiếp, nhưng bản phát hành (release / 릴리스) trạng thái (state / 상태) phải biết phụ thuộc (dependency / 의존성) này. Không được đặc tả hợp đồng (contract / 계약)/drop old trường dữ liệu (field / 필드) chỉ vì ứng dụng (application / 애플리케이션) N+1 đã deploy 100% nếu dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) vẫn chưa converge.

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **28. Backfill là một tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) cần throttle, checkpoint và bất biến (invariant / 불변식)** xác định đầu vào; **29. Dual-write tạo cửa sổ inconsistency cần reconciliation chứ không chỉ kiểm thử (test / 테스트) happy đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **30. đặc tả hợp đồng (contract / 계약) evolution phải theo bên tiêu thụ (consumer / 소비자) lag, không theo producer deploy success** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Dual-write tạo cửa sổ inconsistency cần reconciliation chứ không chỉ kiểm thử (test / 테스트) happy đường dẫn (path / 경로)

Một di chuyển (migration / 마이그레이션) có thể tạm thời ghi cả old store và new store. Hai ghi (write / 쓰기) không atomic qua hai hệ thống nên có thể xảy ra `old success/new fail`, `new success/old fail`, hết thời gian chờ (timeout / 타임아웃) không biết side tác động (effect / 효과) nào đã lần ghi nhận (commit / 커밋) hoặc thử lại (retry / 재시도) tạo duplicate. Vì vậy dual-write là phân tán (distributed / 분산) consistency bài toán (problem / 문제), không phải shortcut miễn phí.

Nếu buộc dùng dual-write, cần xác định nguồn chuẩn (source of truth / 정본) trong từng phase, idempotency key, thử lại (retry / 재시도)/compensation, discrepancy detector và reconciliation job. Read đường dẫn (path / 경로) cũng cần chiến lược (strategy / 전략): đọc old, đọc new, shadow compare hay fallback; mỗi lựa chọn tạo bằng chứng (evidence / 증거) khác nhau.

Cutover chỉ nên xảy ra khi mismatch tỷ lệ (rate / 비율), lag và unresolved discrepancy nằm trong threshold đã định nghĩa. Sau cutover vẫn nên giữ tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) trước khi xóa old đường dẫn (path / 경로) để quay lui (rollback / 롤백)/forensic còn khả thi.

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **29. Dual-write tạo cửa sổ inconsistency cần reconciliation chứ không chỉ kiểm thử (test / 테스트) happy đường dẫn (path / 경로)** xác định đầu vào; **30. đặc tả hợp đồng (contract / 계약) evolution phải theo bên tiêu thụ (consumer / 소비자) lag, không theo producer deploy success** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. thời gian chạy (runtime / 런타임) cấu hình (configuration / 구성) là một bản phát hành (release / 릴리스) surface độc lập với sản phẩm tạo ra (artifact / 산출물)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. đặc tả hợp đồng (contract / 계약) evolution phải theo bên tiêu thụ (consumer / 소비자) lag, không theo producer deploy success

API/sự kiện (event / 이벤트)/lược đồ (schema / 스키마) producer có thể deploy phiên bản (version / 버전) mới trong vài phút nhưng bên tiêu thụ (consumer / 소비자) nâng chậm hàng tuần. Nếu producer ngừng phát trường dữ liệu (field / 필드)/sự kiện (event / 이벤트) cũ ngay sau khi chính nó xanh, hidden bên tiêu thụ (consumer / 소비자) có thể vỡ mà bản phát hành (release / 릴리스) dashboard producer vẫn healthy.

Tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) cần dựa trên inventory/telemetry của bên tiêu thụ (consumer / 소비자) thực: phiên bản (version / 버전) nào đang đọc, bên tiêu thụ (consumer / 소비자) nào offline/batch theo lịch, replay có thể đọc sự kiện (event / 이벤트) cũ bao lâu và retention kéo dài thế nào. Với sự kiện (event / 이벤트) log, một bên tiêu thụ (consumer / 소비자) mới restart từ offset cũ có thể gặp lược đồ (schema / 스키마) lịch sử dù live traffic đã chuyển hết.

Mô hình tư duy (mental model / 사고 모델) bản phát hành (release / 릴리스) vì vậy là `producer capability → coexistence → consumer adoption → evidence không còn old dependency → contract removal`. “Deploy xong producer” chỉ là đầu di chuyển (migration / 마이그레이션), không phải điểm kết thúc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **31. thời gian chạy (runtime / 런타임) cấu hình (configuration / 구성) là một bản phát hành (release / 릴리스) surface độc lập với sản phẩm tạo ra (artifact / 산출물)** tiếp nhận điểm tựa từ **30. đặc tả hợp đồng (contract / 계약) evolution phải theo bên tiêu thụ (consumer / 소비자) lag, không theo producer deploy success** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. cờ tính năng (feature flag / 기능 플래그) là máy trạng thái (state machine / 상태 머신) có cohort và cleanup bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. thời gian chạy (runtime / 런타임) cấu hình (configuration / 구성) là một bản phát hành (release / 릴리스) surface độc lập với sản phẩm tạo ra (artifact / 산출물)

Một nhị phân (binary / 이진)/ảnh (image / 이미지) không đổi nhưng thay hết thời gian chờ (timeout / 타임아웃), pool kích thước (size / 크기), routing weight, bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) hoặc nghiệp vụ (business / 비즈니스) threshold vẫn có thể tạo sự cố (incident / 인시던트) lớn. Vì vậy cấu hình (configuration / 구성) phải được coi là một bản phát hành (release / 릴리스) subject có định danh (identity / 식별자), lịch sử (history / 이력), kiểm tra hợp lệ (validation / 검증) và rollout ngữ nghĩa (semantics / 의미론) riêng, không phải “văn bản (text / 텍스트) tệp (file / 파일) nhỏ nên ít rủi ro”.

Bất biến (invariant / 불변식) quan trọng là operator phải trả lời được `artifact nào + config revision nào + flag state nào` đang tạo hành vi (behavior / 동작) quan sát được. Nếu cấu hình (config / 설정) được mutate trực tiếp mà không có revision/effective-state bằng chứng (evidence / 증거), quay lui (rollback / 롤백) mã (code / 코드) có thể không thay đổi hành vi (behavior / 동작) vì nguyên nhân thực nằm ở cấu hình (config / 설정) mới.

Cấu hình (config / 설정) rollout cũng cần staged exposure khi blast radius lớn. Một thay đổi pool từ 20 lên 200 có thể làm dịch vụ (service / 서비스) cục bộ (local / 로컬) khỏe hơn nhưng đẩy cơ sở dữ liệu (database / 데이터베이스) vào saturation; một hết thời gian chờ (timeout / 타임아웃) dài hơn có thể giảm lỗi (error / 오류) bề mặt nhưng giữ tài nguyên (resource / 자원) lâu hơn. kiểm tra hợp lệ (validation / 검증) phải xét hệ thống (system / 시스템) tác động (effect / 효과), không chỉ lược đồ (schema / 스키마)/kiểu (type / 타입) của cấu hình (config / 설정).

> **Chuyển mạch:** Trong **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **32. cờ tính năng (feature flag / 기능 플래그) là máy trạng thái (state machine / 상태 머신) có cohort và cleanup bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **31. thời gian chạy (runtime / 런타임) cấu hình (configuration / 구성) là một bản phát hành (release / 릴리스) surface độc lập với sản phẩm tạo ra (artifact / 산출물)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Shadow traffic và dark launch tạo bằng chứng (evidence / 증거) nhưng không chứng minh side tác động (effect / 효과) an toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. cờ tính năng (feature flag / 기능 플래그) là máy trạng thái (state machine / 상태 머신) có cohort và cleanup bất biến (invariant / 불변식)

Flag không chỉ là boolean. Progressive bản phát hành (release / 릴리스) thường có quy tắc (rule / 규칙) theo tenant, region, percentage, account lớp (class / 클래스) hoặc prerequisite flag khác. Vì vậy effective hành vi (behavior / 동작) là kết quả của `code revision + flag definition + targeting rule + evaluation context`.

Một flag vòng đời (lifecycle / 생명주기) trưởng thành có ít nhất các trạng thái (state / 상태): tạo ở trạng thái an toàn, enable cho cohort nhỏ, mở rộng theo bằng chứng (evidence / 증거), đạt default mới, rồi **xóa cả old branch lẫn flag definition**. Nếu chỉ để flag ở 100% mãi mãi, codebase vẫn mang hai hành vi (behavior / 동작) đường dẫn (path / 경로) và operator vẫn phải lập luận (reasoning / 추론) về một điều khiển (control / 제어) surface không còn giá trị.

Quay lui (rollback / 롤백) bằng flag cũng có giới hạn. Nếu hành vi (behavior / 동작) mới đã ghi dữ liệu (data / 데이터) theo biểu diễn (representation / 표현) mới, phát bên ngoài (external / 외부) side tác động (effect / 효과) hoặc bên tiêu thụ (consumer / 소비자) khác đã phụ thuộc đầu ra (output / 출력) mới, tắt flag không đảo trạng thái (state / 상태) đã tạo. Vì vậy flag giảm exposure nhưng không thay thế tính tương thích (compatibility / 호환성)/khôi phục (recovery / 복구) thiết kế (design / 설계).

> **Chuyển mạch:** Ở chặng này của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **32. cờ tính năng (feature flag / 기능 플래그) là máy trạng thái (state machine / 상태 머신) có cohort và cleanup bất biến (invariant / 불변식)** nêu điều cần giải thích; **33. Shadow traffic và dark launch tạo bằng chứng (evidence / 증거) nhưng không chứng minh side tác động (effect / 효과) an toàn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **34. bản phát hành (release / 릴리스) định danh (identity / 식별자) phải bao phủ sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정), flag và di chuyển (migration / 마이그레이션) trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Shadow traffic và dark launch tạo bằng chứng (evidence / 증거) nhưng không chứng minh side tác động (effect / 효과) an toàn

Một cách kiểm tra phiên bản (version / 버전) mới là bản sao (copy / 복사) yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) sang candidate nhưng không dùng phản hồi (response / 응답) của candidate cho người dùng (user / 사용자). Cách này cho tải công việc (workload / 워크로드) phân phối (distribution / 분포) thực tế tốt hơn synthetic kiểm thử (test / 테스트), đặc biệt cho parsing, truy vấn (query / 쿼리) planning hoặc read đường dẫn (path / 경로). Tuy nhiên traffic shadow làm tăng downstream tải (load / 로드) và có thể vô tình tạo side tác động (effect / 효과) nếu yêu cầu (request / 요청) không được biến thành read-only/dry-run ngữ nghĩa (semantics / 의미론).

Candidate cũng có thể nhận yêu cầu (request / 요청) trễ hơn original, thiếu session trạng thái (state / 상태) hoặc dùng phụ thuộc (dependency / 의존성) khác nên kết quả mismatch chưa chắc là bug. bằng chứng (evidence / 증거) cần phân biệt đầu vào (input / 입력) equivalence, phụ thuộc (dependency / 의존성) revision và comparison ngữ nghĩa (semantics / 의미론). Với nondeterministic đầu ra (output / 출력), so byte-for-byte có thể tạo false alarm.

Dark launch vì vậy là **đo lường (measurement / 측정) experiment**: phải định nghĩa cái gì được phép thực thi, tải công việc (workload / 워크로드) overhead ngân sách (budget / 예산), mismatch nào có nghĩa và cách dừng experiment nếu candidate gây pressure. Nó không phải cách miễn phí để “kiểm thử (test / 테스트) môi trường vận hành (production / 운영 환경) trước khi bản phát hành (release / 릴리스)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CI/CD: biến thay đổi thành luồng (flow / 흐름) có bằng chứng**, **33. Shadow traffic và dark launch tạo bằng chứng (evidence / 증거) nhưng không chứng minh side tác động (effect / 효과) an toàn** nêu điều cần giải thích; **34. bản phát hành (release / 릴리스) định danh (identity / 식별자) phải bao phủ sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정), flag và di chuyển (migration / 마이그레이션) trạng thái (state / 상태)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 34. bản phát hành (release / 릴리스) định danh (identity / 식별자) phải bao phủ sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정), flag và di chuyển (migration / 마이그레이션) trạng thái (state / 상태)

Nhiều sự cố (incident / 인시던트) khó điều tra vì dashboard chỉ dimension theo ứng dụng (application / 애플리케이션) phiên bản (version / 버전) trong khi hành vi (behavior / 동작) thực phụ thuộc nhiều điều khiển (control / 제어) surface. Một bản phát hành (release / 릴리스) định danh (identity / 식별자) hữu ích nên liên kết immutable sản phẩm tạo ra (artifact / 산출물) digest với cấu hình (config / 설정) revision, relevant flag snapshot/quy tắc (rule / 규칙) revision, lược đồ (schema / 스키마)/di chuyển (migration / 마이그레이션) phase và môi trường (environment / 환경)/region.

Điều này không có nghĩa đóng băng mọi động (dynamic / 동적) cấu hình (config / 설정). Nó có nghĩa mọi mutation quan trọng phải có sự kiện (event / 이벤트)/revision để reconstruct effective trạng thái (state / 상태) tại thời điểm T. Khi operator hỏi “vì sao cùng phiên bản (version / 버전) nhưng chỉ tenant A lỗi?”, cohort/flag/cấu hình (config / 설정) bằng chứng (evidence / 증거) phải cho phép giải thích khác biệt đó.

Mô hình tư duy (mental model / 사고 모델) cuối cùng là:

```text
source change
→ artifact identity
→ config + flag + migration composition
→ staged exposure
→ runtime evidence theo cohort
→ promote / pause / compensate / rollback-compatible action
→ cleanup old compatibility state
```

Safe delivery chỉ hoàn tất khi temporary tính tương thích (compatibility / 호환성)/flag/di chuyển (migration / 마이그레이션) trạng thái (state / 상태) đã được thu hồi và hệ thống trở lại một steady trạng thái (state / 상태) dễ lập luận (reasoning / 추론), không phải ngay khi 100% traffic chạy nhị phân (binary / 이진) mới.

> **Bàn giao:** Sau **34. bản phát hành (release / 릴리스) định danh (identity / 식별자) phải bao phủ sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정), flag và di chuyển (migration / 마이그레이션) trạng thái (state / 상태)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
