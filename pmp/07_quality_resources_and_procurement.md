# 07 — chất lượng (quality / 품질), resources và procurement

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **07 — Quality, resources và procurement**. Route đi từ fitness-for-purpose → quality criteria/grade → resource capacity → supplier/contract choice → acceptance and control, để chất lượng nối với nguồn lực và cam kết.

## Chất lượng (quality / 품질) là fitness for purpose

Chất lượng (quality / 품질) không đồng nghĩa “nhiều tính năng (feature / 기능)” hoặc “đắt tiền”. chất lượng (quality / 품질) là mức deliverable đáp ứng yêu cầu (requirement / 요구사항) và phù hợp mục đích sử dụng. Grade có thể thấp nhưng chất lượng (quality / 품질) cao nếu đúng specification; một sản phẩm nhiều tính năng (feature / 기능) nhưng lỗi trọng yếu (critical / 중요) vẫn chất lượng (quality / 품질) thấp.

Quản lý chất lượng (quality / 품질) cần ba lớp lập luận (reasoning / 추론): yêu cầu (requirement / 요구사항) chất lượng là gì, tiến trình (process / 프로세스) nào tạo khả năng đạt chúng, và bằng chứng (evidence / 증거) nào xác nhận deliverable thực sự đạt.

Chất lượng (quality / 품질) không phải activity của QA nhóm (team / 팀) ở cuối chuỗi xử lý (pipeline / 파이프라인). Nó là thuộc tính (property / 속성) emergent từ yêu cầu (requirement / 요구사항), thiết kế (design / 설계), tiến trình (process / 프로세스), năng lực (capability / 역량), supplier và vòng phản hồi (feedback loop / 피드백 루프) xuyên vòng đời (lifecycle / 생명주기).

> **Nối mạch:** **Chất lượng (quality / 품질) và grade khác nhau** nối từ **Chất lượng (quality / 품질) là fitness for purpose** sang **Chất lượng (quality / 품질) yêu cầu (requirement / 요구사항) phải operationalizable**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chất lượng (quality / 품질) và grade khác nhau

Grade nói category hoặc tính năng (feature / 기능) mức (level / 수준). chất lượng (quality / 품질) nói mức conformance/fitness trong grade đã chọn.

Một economy sản phẩm (product / 제품) có ít tính năng (feature / 기능) nhưng đạt mọi specification có thể chất lượng (quality / 품질) cao. Một premium sản phẩm (product / 제품) nhiều tính năng (feature / 기능) nhưng unreliable có chất lượng (quality / 품질) thấp. Distinction này giúp tránh gold plating: thêm năng lực (capability / 역량) không tự làm chất lượng (quality / 품질) tốt hơn.

> **Nối mạch:** **Chất lượng (quality / 품질) yêu cầu (requirement / 요구사항) phải operationalizable** nối từ **Chất lượng (quality / 품질) và grade khác nhau** sang **Chất lượng (quality / 품질) planning, assurance và điều khiển (control / 제어)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chất lượng (quality / 품질) yêu cầu (requirement / 요구사항) phải operationalizable

“High chất lượng (quality / 품질)”, “secure”, “easy to use” không đủ để điều khiển (control / 제어). yêu cầu (requirement / 요구사항) cần bằng chứng (evidence / 증거) criterion phù hợp ngữ cảnh (context / 맥락).

Ví dụ availability 99.95%, defect severity-1 bằng 0 trước go-live, tác vụ (task / 작업) completion usability kiểm thử (test / 테스트) trên 90%, hoặc material tolerance ±0.2 mm. Không phải mọi chất lượng (quality / 품질) attribute cần numeric, nhưng phải đủ rõ để reviewer biết pass/thất bại (fail / 실패) hoặc mức acceptable.

Một criterion còn phải gắn đúng ngữ cảnh (context / 맥락) đo. “phản hồi (response / 응답) dưới 300 ms” vô nghĩa nếu tải công việc (workload / 워크로드), percentile, môi trường (environment / 환경) và giao dịch (transaction / 트랜잭션) kiểu (type / 타입) không rõ. chất lượng (quality / 품질) chỉ số (metric / 지표) càng xa usage thực tế càng dễ tạo false confidence.

> **Nối mạch:** **Chất lượng (quality / 품질) planning, assurance và điều khiển (control / 제어)** nối từ **Chất lượng (quality / 품질) yêu cầu (requirement / 요구사항) phải operationalizable** sang **Tiến trình (process / 프로세스) năng lực (capability / 역량) và chất lượng (quality / 품질) at nguồn (source / 소스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chất lượng (quality / 품질) planning, assurance và điều khiển (control / 제어)

Chất lượng (quality / 품질) planning xác định tiêu chuẩn (standard / 표준), chỉ số (metric / 지표), acceptance và tiến trình (process / 프로세스). chất lượng (quality / 품질) assurance tập trung vào tiến trình (process / 프로세스) có khả năng tạo đầu ra (output / 출력) đúng không. chất lượng (quality / 품질) điều khiển (control / 제어) inspect/measure deliverable hoặc tiến trình (process / 프로세스) kết quả (result / 결과).

Ba lớp không thay thế nhau. kiểm thử (test / 테스트) nhiều không cứu yêu cầu (requirement / 요구사항) sai. tiến trình (process / 프로세스) kiểm tra (audit / 감사) tốt không chứng minh từng deliverable pass. chất lượng (quality / 품질) plan tốt không có giá trị nếu thực thi (execution / 실행) không follow và bằng chứng (evidence / 증거) không được thu.

Một cách nhìn sâu hơn là chất lượng (quality / 품질) management cố tạo một tiến trình (process / 프로세스) có năng lực (capability / 역량) đủ cao để đầu ra (output / 출력) đúng trở thành trạng thái bình thường, thay vì dựa vào heroic inspection ở cuối.

> **Nối mạch:** **Chất lượng (quality / 품질) planning, assurance và điều khiển (control / 제어)** đặt vấn đề; **Tiến trình (process / 프로세스) năng lực (capability / 역량) và chất lượng (quality / 품질) at nguồn (source / 소스)** kiểm tra bằng chứng, rồi **Prevention tốt hơn inspection khi thất bại (failure / 실패) chi phí (cost / 비용) cao** mở rộng hệ quả.

## Tiến trình (process / 프로세스) năng lực (capability / 역량) và chất lượng (quality / 품질) at nguồn (source / 소스)

Nếu tiến trình (process / 프로세스) thường xuyên tạo defect rồi QA lọc ở cuối, organization có detection năng lực (capability / 역량) nhưng chưa chắc có môi trường vận hành (production / 운영 환경) năng lực (capability / 역량) tốt. chất lượng (quality / 품질) at nguồn (source / 소스) nghĩa người/tiến trình (process / 프로세스) tạo công việc (work / 작업) cũng có cơ chế (mechanism / 메커니즘) phát hiện lỗi sớm tại nơi lỗi sinh ra: peer rà soát (review / 검토), automated kiểm tra hợp lệ (validation / 검증), poka-yoke/error-proofing, checklist trọng yếu (critical / 중요) step hoặc built-in điều khiển (control / 제어) phù hợp lĩnh vực (domain / 도메인).

Mục tiêu không phải chuyển trách nhiệm sang cá nhân, mà rút vòng phản hồi (feedback loop / 피드백 루프). Defect được phát hiện một giờ sau khi tạo thường rẻ và dễ hiểu hơn defect được phát hiện ba tháng sau khi ngữ cảnh (context / 맥락) đã mất.

Tiến trình (process / 프로세스) năng lực (capability / 역량) không đồng nghĩa zero variation. Nó nghĩa variation đủ ổn định và nằm trong tolerance phù hợp để downstream có thể tin vào đầu ra (output / 출력) mà không cần kiểm tra lại mọi thứ.

> **Nối mạch:** **Tiến trình (process / 프로세스) năng lực (capability / 역량) và chất lượng (quality / 품질) at nguồn (source / 소스)** đặt vấn đề; **Prevention tốt hơn inspection khi thất bại (failure / 실패) chi phí (cost / 비용) cao** kiểm tra bằng chứng, rồi **Chi phí (cost / 비용) of chất lượng (quality / 품질) là economic sự đánh đổi (trade-off / 트레이드오프)** mở rộng hệ quả.

## Prevention tốt hơn inspection khi thất bại (failure / 실패) chi phí (cost / 비용) cao

Inspection cuối chuỗi xử lý (pipeline / 파이프라인) chỉ phát hiện defect sau khi chi phí (cost / 비용) đã xảy ra. Prevention đưa chất lượng (quality / 품질) vào yêu cầu (requirement / 요구사항), thiết kế (design / 설계), working phương thức (method / 메서드) và automated điều khiển (control / 제어) sớm hơn.

Chi phí (cost / 비용) of chất lượng (quality / 품질) thường được nhìn thành prevention + appraisal + thất bại (failure / 실패) chi phí (cost / 비용). nội bộ (internal / 내부) thất bại (failure / 실패) được phát hiện trước customer; bên ngoài (external / 외부) thất bại (failure / 실패) xảy ra sau bản phát hành (release / 릴리스)/delivery và thường đắt hơn vì sự cố (incident / 인시던트), recall, penalty hoặc trust mất mát (loss / 손실).

Tuy nhiên “kiểm thử (test / 테스트) nhiều vô hạn” cũng không tối ưu. điều khiển (control / 제어) phải proportional với rủi ro (risk / 위험). Safety-critical thành phần (component / 컴포넌트) cần bằng chứng (evidence / 증거) mạnh hơn low-impact nội bộ (internal / 내부) công cụ (tool / 도구).

Trong software, xem thêm [Testing, quality và verification strategy](../computer_science/09_software_engineering/02_testing_quality_and_verification_strategy.md) để hiểu sâu kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) và bằng chứng (evidence / 증거) kỹ thuật.

> **Nối mạch:** **Chi phí (cost / 비용) of chất lượng (quality / 품질) là economic sự đánh đổi (trade-off / 트레이드오프)** nối từ **Prevention tốt hơn inspection khi thất bại (failure / 실패) chi phí (cost / 비용) cao** sang **Chất lượng (quality / 품질) debt và escaped defect**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chi phí (cost / 비용) of chất lượng (quality / 품질) là economic sự đánh đổi (trade-off / 트레이드오프)

Prevention có chi phí (cost / 비용), appraisal có chi phí (cost / 비용) và thất bại (failure / 실패) có chi phí (cost / 비용). Mục tiêu không phải zero spending on thất bại (failure / 실패) bằng mọi giá, mà minimize total expected chi phí (cost / 비용) trong ràng buộc (constraint / 제약조건) và rủi ro (risk / 위험) appetite.

Một defect cosmetic hiếm có thể rẻ hơn để accept; một privacy defect low-probability có impact lớn nên prevention mạnh hơn. Economic lập luận (reasoning / 추론) giúp chất lượng (quality / 품질) điều khiển (control / 제어) không trở thành checklist đồng đều.

Chi phí (cost / 비용) of poor chất lượng (quality / 품질) còn gồm những khoản khó thấy: rework làm chậm tính năng (feature / 기능) khác, hỗ trợ (support / 지원) tải (load / 로드), customer churn, warranty, opportunity chi phí (cost / 비용) và management attention. Một defect sửa mất hai giờ có thể gây hệ thống (system / 시스템) chi phí (cost / 비용) lớn hơn nhiều nếu nó làm bản phát hành (release / 릴리스) bị delay hoặc kéo specialist khỏi trọng yếu (critical / 중요) công việc (work / 작업).

> **Nối mạch:** **Chất lượng (quality / 품질) debt và escaped defect** nối từ **Chi phí (cost / 비용) of chất lượng (quality / 품질) là economic sự đánh đổi (trade-off / 트레이드오프)** sang **Nguyên nhân gốc (root cause / 근본 원인) và contributing factors**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chất lượng (quality / 품질) debt và escaped defect

Khi nhóm (team / 팀) chấp nhận known defect, bỏ kiểm thử, nới acceptance hoặc defer corrective hành động (action / 동작) để giữ deadline, họ có thể đang tạo chất lượng (quality / 품질) debt. Debt có thể hợp lý nếu visible, đơn vị sở hữu (owner / 오너) rõ, impact hiểu được và repayment plan có thật. Nó nguy hiểm khi được gọi là “temporary exception” nhưng không bao giờ retire.

Escaped defect là defect vượt qua điều khiển (control / 제어) hiện tại và được phát hiện ở downstream hoặc môi trường vận hành (production / 운영 환경). Trend escaped defect hữu ích vì nó kiểm tra effectiveness của điều khiển (control / 제어) hệ thống (system / 시스템), không chỉ số lượng bug nội bộ.

Nếu nội bộ (internal / 내부) defect count giảm nhưng escaped defect tăng, kết luận “chất lượng (quality / 품질) tốt hơn” có thể sai. chỉ số (metric / 지표) cần được đọc như một hệ thống (system / 시스템), không tách rời.

> **Nối mạch:** **Nguyên nhân gốc (root cause / 근본 원인) và contributing factors** nối từ **Chất lượng (quality / 품질) debt và escaped defect** sang **Corrective, preventive và defect repair**, vì cơ chế trước tạo đầu vào cho bước sau.

## Nguyên nhân gốc (root cause / 근본 원인) và contributing factors

Complex thất bại (failure / 실패) hiếm khi có một nguyên nhân gốc (root cause / 근본 원인) duy nhất. Five Whys hoặc fishbone giúp mở investigation nhưng có thể oversimplify nếu nhóm (team / 팀) ép một tuyến tính (linear / 선형) chuỗi (chain / 사슬).

Một sự cố (incident / 인시던트) môi trường vận hành (production / 운영 환경) có thể đồng thời do yêu cầu (requirement / 요구사항) ambiguity, missing automated kiểm thử (test / 테스트), deadline pressure và kiểm soát truy cập (access control / 접근 제어) yếu. Corrective hành động (action / 동작) nên mục tiêu (target / 대상) leverage điểm (point / 지점), không chỉ người cuối cùng chạm hệ thống (system / 시스템).

Nguyên nhân gốc (root cause / 근본 원인) phân tích (analysis / 분석) tốt còn phân biệt cause có thể kiểm soát và điều kiện (condition / 조건) làm thất bại (failure / 실패) dễ xảy ra. “Engineer nhập sai” có thể là immediate cause, nhưng giao diện (interface / 인터페이스) cho phép thao tác nguy hiểm không confirmation hoặc tải công việc (workload / 워크로드) quá cao có thể là contributing hệ thống (system / 시스템) điều kiện (condition / 조건).

> **Nối mạch:** **Corrective, preventive và defect repair** nối từ **Nguyên nhân gốc (root cause / 근본 원인) và contributing factors** sang **Statistical thinking ở mức cần thiết**, vì cơ chế trước tạo đầu vào cho bước sau.

## Corrective, preventive và defect repair

Defect repair sửa đầu ra (output / 출력) cụ thể. Corrective hành động (action / 동작) xử lý cause của nonconformity đã xảy ra. Preventive hành động (action / 동작) giảm khả năng future bài toán (problem / 문제) dựa trên identified rủi ro (risk / 위험) hoặc weakness.

Nếu nhóm (team / 팀) fix cùng loại bug mỗi bản phát hành (release / 릴리스) nhưng không đổi tiến trình (process / 프로세스), họ chỉ repair symptom. Nếu thêm lint/kiểm thử (test / 테스트) quy tắc (rule / 규칙) để ngăn lớp (class / 클래스) bug đó, hệ thống (system / 시스템) năng lực (capability / 역량) tăng.

> **Nối mạch:** **Statistical thinking ở mức cần thiết** nối từ **Corrective, preventive và defect repair** sang **Continuous improvement**, vì cơ chế trước tạo đầu vào cho bước sau.

## Statistical thinking ở mức cần thiết

Variation luôn tồn tại. điều khiển (control / 제어) chart hoặc trend phân tích (analysis / 분석) giúp phân biệt tiến trình (process / 프로세스) variation bình thường với special tín hiệu (signal / 신호). React mạnh với từng dữ liệu (data / 데이터) điểm (point / 지점) random có thể làm tiến trình (process / 프로세스) bất ổn hơn.

PMP learner không cần trở thành statistician, nhưng cần hiểu chất lượng (quality / 품질) quyết định (decision / 결정) dựa trên mẫu (pattern / 패턴) và threshold, không anecdote đơn lẻ.

Một điểm quan trọng là specification limit và tiến trình (process / 프로세스) hành vi (behavior / 동작) khác nhau. Deliverable có thể vẫn pass specification nhưng tiến trình (process / 프로세스) đang drift dần về ranh giới (boundary / 경계); nếu chỉ nhìn pass/thất bại (fail / 실패) cuối cùng, early tín hiệu (signal / 신호) bị bỏ lỡ.

> **Nối mạch:** **Continuous improvement** nối từ **Statistical thinking ở mức cần thiết** sang **Tài nguyên (resource / 자원) management là năng lực (capability / 역량) + availability**, vì cơ chế trước tạo đầu vào cho bước sau.

## Continuous improvement

Các vòng như Plan-Do-Check-Act (PDCA) hay retrospective đều dựa trên phản hồi (feedback / 피드백). Improvement tốt cần phân biệt symptom và nguyên nhân gốc (root cause / 근본 원인). Nếu defect tăng vì yêu cầu (requirement / 요구사항) ambiguity, tăng số tester có thể chỉ xử lý symptom.

Improvement cần hypothesis và measure. “Thêm rà soát mã (code review / 코드 리뷰) checklist có giảm escaped defect loại X mà không tăng lead thời gian (time / 시간) quá mức không?” rõ hơn “hãy rà soát (review / 검토) kỹ hơn”.

Improvement cũng cần guardrail. Giảm defect bằng cách làm rà soát (review / 검토) chậm gấp ba có thể không tối ưu nếu nghiệp vụ (business / 비즈니스) cần fast phản hồi (feedback / 피드백). chất lượng (quality / 품질) improvement là multi-objective tối ưu hóa (optimization / 최적화), không phải tối đa một chỉ số (metric / 지표).

> **Nối mạch:** **Continuous improvement** nêu quy tắc; **Tài nguyên (resource / 자원) management là năng lực (capability / 역량) + availability** thử quy tắc trong tình huống, rồi **Sức chứa (capacity / 용량) không bằng calendar availability** mở rộng hệ quả.

## Tài nguyên (resource / 자원) management là năng lực (capability / 역량) + availability

Tài nguyên (resources / 자원) gồm people, equipment, facilities, material và dịch vụ (service / 서비스) sức chứa (capacity / 용량). Với kiến thức (knowledge / 지식) công việc (work / 작업), một người “rảnh 50%” không tương đương mọi người khác “rảnh 50%”; năng lực (capability / 역량), ngữ cảnh (context / 맥락) switching và lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) matters.

Tài nguyên (resource / 자원) planning cần nhìn role, skill, sức chứa (capacity / 용량), timing và phụ thuộc (dependency / 의존성). tài nguyên (resource / 자원) histogram hoặc sức chứa (capacity / 용량) view chỉ hữu ích nếu phản ánh ràng buộc (constraint / 제약조건) thật.

> **Nối mạch:** **Tài nguyên (resource / 자원) management là năng lực (capability / 역량) + availability** nêu quy tắc; **Sức chứa (capacity / 용량) không bằng calendar availability** thử quy tắc trong tình huống, rồi **Utilization paradox và hàng đợi (queue / 큐)** mở rộng hệ quả.

## Sức chứa (capacity / 용량) không bằng calendar availability

Một engineer có 8 giờ calendar không có 8 giờ productive sức chứa (capacity / 용량) cho dự án (project / 프로젝트) nếu có hỗ trợ (support / 지원) duty, meeting và ngữ cảnh (context / 맥락) switching.

Planning dựa trên nominal availability thường gây overcommit. Sustainable sức chứa (capacity / 용량) cần reserve cho variability và unplanned công việc (work / 작업), nhất là operational môi trường (environment / 환경).

Sức chứa (capacity / 용량) nên được nhìn theo effective thông lượng (throughput / 처리량), không chỉ giờ phân bổ. Hai người mỗi người 50% trên hai dự án (project / 프로젝트) có thể tạo ít đầu ra (output / 출력) hơn một người full-time trên một dự án (project / 프로젝트) vì switching chi phí (cost / 비용), meeting duplication và bộ nhớ (memory / 메모리) reload.

> **Nối mạch:** **Sức chứa (capacity / 용량) không bằng calendar availability** nêu quy tắc; **Utilization paradox và hàng đợi (queue / 큐)** thử quy tắc trong tình huống, rồi **Skill ma trận (matrix / 행렬) và single điểm (point / 지점) of thất bại (failure / 실패)** mở rộng hệ quả.

## Utilization paradox và hàng đợi (queue / 큐)

Đẩy specialist lên gần 100% utilization thường làm hàng đợi (queue / 큐) tăng mạnh. Khi mọi minute đã được booked, một yêu cầu (request / 요청) bất ngờ không có slack để hấp thụ và chờ đợi lan sang nhiều nhóm (team / 팀).

Vì vậy tài nguyên (resource / 자원) “nhàn một chút” ở bottleneck có thể là sức chứa (capacity / 용량) bảo hiểm cho variability, không phải waste. Đây là cùng lô-gic (logic / 논리) luồng (flow / 흐름) đã được giải thích ở [Schedule & Flow](./05_schedule_estimation_and_flow.md): cục bộ (local / 로컬) utilization cao không đảm bảo hệ thống (system / 시스템) thông lượng (throughput / 처리량) cao.

> **Nối mạch:** **Skill ma trận (matrix / 행렬) và single điểm (point / 지점) of thất bại (failure / 실패)** nối từ **Utilization paradox và hàng đợi (queue / 큐)** sang **Học tập (learning / 학습) curve và onboarding chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Skill ma trận (matrix / 행렬) và single điểm (point / 지점) of thất bại (failure / 실패)

Tài nguyên (resource / 자원) rủi ro (risk / 위험) không chỉ thiếu headcount. Có thể đủ 10 người nhưng chỉ một người biết legacy cơ sở dữ liệu (database / 데이터베이스) hoặc đặc tả hợp đồng (contract / 계약) negotiation.

Skill ma trận (matrix / 행렬) giúp nhìn năng lực (capability / 역량) concentration. Cross-training, pairing và documentation giảm bus factor. trọng yếu (critical / 중요) kiến thức (knowledge / 지식) transfer nên được plan trước khi người đó rời dự án (project / 프로젝트), không chờ notice period.

Skill substitution cũng không tuyến tính. Hai junior không tự động thay một specialist ở quyết định (decision / 결정) trọng yếu (critical / 중요). tài nguyên (resource / 자원) mô hình (model / 모델) phải hiểu minimum năng lực (capability / 역량) threshold và học tập (learning / 학습) curve, không coi mọi FTE là fungible đơn vị (unit / 단위).

> **Nối mạch:** **Học tập (learning / 학습) curve và onboarding chi phí (cost / 비용)** nối từ **Skill ma trận (matrix / 행렬) và single điểm (point / 지점) of thất bại (failure / 실패)** sang **Tài nguyên (resource / 자원) leveling và smoothing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Học tập (learning / 학습) curve và onboarding chi phí (cost / 비용)

Tài nguyên (resource / 자원) mới không tạo full sức chứa (capacity / 용량) ngay ngày đầu. Họ cần lĩnh vực (domain / 도메인) ngữ cảnh (context / 맥락), môi trường (environment / 환경) truy cập (access / 접근), working agreement và kiến thức (knowledge / 지식) transfer; đồng thời người cũ phải dành thời gian onboarding.

Vì vậy “thêm người” vào dự án (project / 프로젝트) trễ có thể tạm thời giảm net thông lượng (throughput / 처리량). Càng nhiều coordination phụ thuộc (dependency / 의존성), ramp-up chi phí (cost / 비용) càng lớn. tài nguyên (resource / 자원) quyết định (decision / 결정) phải nhìn time-to-effective-capacity, không chỉ headcount.

> **Nối mạch:** **Học tập (learning / 학습) curve và onboarding chi phí (cost / 비용)** đặt vấn đề; **Tài nguyên (resource / 자원) leveling và smoothing** kiểm tra bằng chứng, rồi **Dùng chung (shared / 공유) tài nguyên (resource / 자원) và portfolio contention** mở rộng hệ quả.

## Tài nguyên (resource / 자원) leveling và smoothing

Khi demand vượt availability, tài nguyên (resource / 자원) leveling thay schedule để phù hợp ràng buộc (constraint / 제약조건) và có thể đổi đường găng (critical path / 임계 경로)/finish date. tài nguyên (resource / 자원) smoothing dùng available float để cân allocation nhưng cố giữ finish date.

Điểm cốt lõi là schedule phải phản ánh sức chứa (capacity / 용량) thật. Một plan giả định cùng người làm ba activity song song không trở nên khả thi chỉ vì Gantt đẹp.

> **Nối mạch:** **Tài nguyên (resource / 자원) leveling và smoothing** đặt vấn đề; **Dùng chung (shared / 공유) tài nguyên (resource / 자원) và portfolio contention** kiểm tra bằng chứng, rồi **Nhóm (team / 팀) acquisition và bản phát hành (release / 릴리스)** mở rộng hệ quả.

## Dùng chung (shared / 공유) tài nguyên (resource / 자원) và portfolio contention

Dự án (project / 프로젝트) có thể plan đúng nội bộ nhưng vẫn thất bại (fail / 실패) khi nhiều dự án (project / 프로젝트) cùng tranh một dùng chung (shared / 공유) specialist, môi trường (environment / 환경) hoặc approval body. Đây là tài nguyên (resource / 자원) rủi ro (risk / 위험) ở portfolio/hệ thống (system / 시스템) mức (level / 수준).

Nếu tất cả dự án (project / 프로젝트) đều được plan như thể dùng chung (shared / 공유) tài nguyên (resource / 자원) luôn available, tổng portfolio plan là impossible dù từng plan riêng trông feasible. PM cần surface contention và đưa priority quyết định (decision / 결정) tới mức (level / 수준) có authority phân bổ sức chứa (capacity / 용량).

> **Nối mạch:** **Dùng chung (shared / 공유) tài nguyên (resource / 자원) và portfolio contention** đặt vấn đề; **Nhóm (team / 팀) acquisition và bản phát hành (release / 릴리스)** kiểm tra bằng chứng, rồi **RACI và giới hạn** mở rộng hệ quả.

## Nhóm (team / 팀) acquisition và bản phát hành (release / 릴리스)

Dự án (project / 프로젝트) cần tài nguyên (resource / 자원) đúng thời điểm. Onboarding quá muộn có học tập (learning / 학습) curve; giữ specialist quá lâu tăng chi phí (cost / 비용)/opportunity chi phí (cost / 비용).

Tài nguyên (resource / 자원) bản phát hành (release / 릴리스) cũng cần chuyển tiếp (transition / 전이) kiến thức (knowledge / 지식). Một chuyên gia rời dự án (project / 프로젝트) ngay sau bản dựng (build / 빌드) nhưng trước UAT có thể tạo rủi ro (risk / 위험) lớn dù planned tác vụ (task / 작업) của họ đã complete.

Bản phát hành (release / 릴리스) quyết định (decision / 결정) nên nhìn remaining bất định (uncertainty / 불확실성) và kiến thức (knowledge / 지식) phụ thuộc (dependency / 의존성), không chỉ số tác vụ (task / 작업) còn lại. Specialist có thể không còn nhiều công việc (work / 작업) nhưng vẫn là trọng yếu (critical / 중요) fallback trong tích hợp (integration / 통합) cửa sổ (window / 윈도우).

> **Nối mạch:** **Nhóm (team / 팀) acquisition và bản phát hành (release / 릴리스)** đặt tiêu chí; **RACI và giới hạn** dùng nó để kiểm tra ranh giới, rồi **Procurement là chuyển một phần delivery qua ranh giới (boundary / 경계) tổ chức** mở rộng cơ chế.

## RACI và giới hạn

RACI làm rõ Responsible, Accountable, Consulted, Informed. Nhưng ma trận (matrix / 행렬) không sửa được quản trị (governance / 거버넌스) mơ hồ nếu authority thực tế khác trên giấy.

Một công việc (work / 작업) item nên có accountability rõ. Nếu ba người đều “A”, thường quyết định (decision / 결정) quyền sở hữu (ownership / 소유권) chưa rõ. Nếu người “A” không có authority/tài nguyên (resource / 자원) để quyết, RACI chỉ là documentation theater.

RACI cũng không mô tả phụ thuộc (dependency / 의존성) timing, quyết định (decision / 결정) threshold hoặc escalation. Nó là role map, không phải operating mô hình (model / 모델) hoàn chỉnh.

> **Nối mạch:** **RACI và giới hạn** đặt tiêu chí; **Procurement là chuyển một phần delivery qua ranh giới (boundary / 경계) tổ chức** dùng nó để kiểm tra ranh giới, rồi **Principal–tác nhân (agent / 에이전트) bài toán (problem / 문제) và thông tin (information / 정보) asymmetry** mở rộng cơ chế.

## Procurement là chuyển một phần delivery qua ranh giới (boundary / 경계) tổ chức

Thu mua (procurement / 조달) tạo một giao diện (interface / 인터페이스) giữa buyer và seller. đặc tả hợp đồng (contract / 계약) phân phối phạm vi (scope / 범위), price, schedule và rủi ro (risk / 위험) giữa hai bên. Vì incentive hai bên không hoàn toàn giống nhau, đặc tả hợp đồng (contract / 계약) thiết kế (design / 설계) ảnh hưởng hành vi (behavior / 동작).

Procurement không chỉ là purchasing. Nó gồm make-or-buy, solicitation, selection, contracting, hiệu năng (performance / 성능) điều khiển (control / 제어), thay đổi (change / 변경)/claim và closure.

> **Nối mạch:** **Procurement là chuyển một phần delivery qua ranh giới (boundary / 경계) tổ chức** đặt tiêu chí; **Principal–tác nhân (agent / 에이전트) bài toán (problem / 문제) và thông tin (information / 정보) asymmetry** dùng nó để kiểm tra ranh giới, rồi **Make-or-buy và total chi phí (cost / 비용)** mở rộng cơ chế.

## Principal–tác nhân (agent / 에이전트) bài toán (problem / 문제) và thông tin (information / 정보) asymmetry

Buyer thường không quan sát trực tiếp toàn bộ effort, chất lượng (quality / 품질) hay nội bộ (internal / 내부) ràng buộc (constraint / 제약조건) của seller; seller cũng không hiểu đầy đủ nghiệp vụ (business / 비즈니스) consequence phía buyer. Đây là thông tin (information / 정보) asymmetry.

Đặc tả hợp đồng (contract / 계약) và quản trị (governance / 거버넌스) cố align hành vi (behavior / 동작) bằng acceptance, milestone, reporting, kiểm tra (audit / 감사) right, incentive và liability. Nhưng không đặc tả hợp đồng (contract / 계약) nào mô tả hết mọi future trạng thái (state / 상태). Vì vậy procurement luôn là combination của formal agreement và relationship/quản trị (governance / 거버넌스) cơ chế (mechanism / 메커니즘).

Nếu buyer chỉ dựa vào trust, material issue có thể bị che. Nếu buyer cố đặc tả hợp đồng (contract / 계약) hóa mọi micro-action, giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và adversarial hành vi (behavior / 동작) tăng. thiết kế (design / 설계) tốt cân bằng chứng (evidence / 증거), autonomy và consequence.

> **Nối mạch:** **Make-or-buy và total chi phí (cost / 비용)** nối từ **Principal–tác nhân (agent / 에이전트) bài toán (problem / 문제) và thông tin (information / 정보) asymmetry** sang **Rủi ro (risk / 위험) allocation: giao rủi ro (risk / 위험) cho bên có khả năng quản lý**, vì cơ chế trước tạo đầu vào cho bước sau.

## Make-or-buy và total chi phí (cost / 비용)

Make-or-buy không chỉ so hourly tỷ lệ (rate / 비율). Outsourcing có giao dịch (transaction / 트랜잭션) chi phí (cost / 비용): vendor selection, đặc tả hợp đồng (contract / 계약), tích hợp (integration / 통합), kiến thức (knowledge / 지식) transfer, bảo mật (security / 보안), oversight và exit chi phí (cost / 비용). nội bộ (internal / 내부) development có opportunity chi phí (cost / 비용) và sức chứa (capacity / 용량) ràng buộc (constraint / 제약조건).

Một vendor rẻ hơn 20% nhưng lock-in cao, SLA yếu và kiến thức (knowledge / 지식) transfer kém có thể đắt hơn trong vòng đời (lifecycle / 생명주기).

Quyết định (decision / 결정) cũng cần strategic năng lực (capability / 역량). Outsource một commodity khác outsource cốt lõi (core / 핵심) kiến thức (knowledge / 지식) tạo competitive advantage.

Make-or-buy còn thay đổi future option. Nếu nội bộ (internal / 내부) năng lực (capability / 역량) bị mất sau nhiều năm outsource, switching back không miễn phí. Total chi phí (cost / 비용) phải nhìn cả năng lực (capability / 역량) erosion và phụ thuộc (dependency / 의존성) concentration.

> **Nối mạch:** **Rủi ro (risk / 위험) allocation: giao rủi ro (risk / 위험) cho bên có khả năng quản lý** nối từ **Make-or-buy và total chi phí (cost / 비용)** sang **Đặc tả hợp đồng (contract / 계약) kiểu (type / 타입) là incentive kiến trúc (architecture / 아키텍처)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Rủi ro (risk / 위험) allocation: giao rủi ro (risk / 위험) cho bên có khả năng quản lý

Đặc tả hợp đồng (contract / 계약) không nên chỉ “đẩy càng nhiều rủi ro (risk / 위험) sang seller càng tốt”. Seller sẽ price rủi ro (risk / 위험) họ không kiểm soát được hoặc phản ứng bằng exclusion/thay đổi (change / 변경) claim. rủi ro (risk / 위험) allocation hiệu quả giao exposure cho party có năng lực (capability / 역량) kiểm soát cause tốt nhất và có incentive phù hợp.

Ví dụ buyer kiểm soát yêu cầu (requirement / 요구사항) approval thì delay do buyer approval khó hợp lý nếu hoàn toàn chuyển sang seller. Seller kiểm soát staffing thì sức chứa (capacity / 용량) thất bại (failure / 실패) nên nằm nhiều hơn ở seller. dùng chung (shared / 공유) rủi ro (risk / 위험) cần giao diện (interface / 인터페이스), trigger và quyết định (decision / 결정) quy tắc (rule / 규칙) rõ.

Poor rủi ro (risk / 위험) allocation tạo rủi ro (risk / 위험) premium, dispute và defensive hành vi (behavior / 동작); nó không làm bất định (uncertainty / 불확실성) biến mất.

> **Nối mạch:** **Đặc tả hợp đồng (contract / 계약) kiểu (type / 타입) là incentive kiến trúc (architecture / 아키텍처)** nối từ **Rủi ro (risk / 위험) allocation: giao rủi ro (risk / 위험) cho bên có khả năng quản lý** sang **Fixed-price trong high bất định (uncertainty / 불확실성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đặc tả hợp đồng (contract / 계약) kiểu (type / 타입) là incentive kiến trúc (architecture / 아키텍처)

Fixed-price chuyển nhiều chi phí (cost / 비용) rủi ro (risk / 위험) sang seller khi phạm vi (scope / 범위) rõ, nhưng seller sẽ price bất định (uncertainty / 불확실성) hoặc resist thay đổi (change / 변경). Cost-reimbursable phù hợp khi phạm vi (scope / 범위) uncertain hơn nhưng buyer giữ nhiều chi phí (cost / 비용) rủi ro (risk / 위험) và cần oversight. Time-and-materials linh hoạt nhưng cần cap/điều khiển (control / 제어) để tránh spend không kiểm soát.

Không có đặc tả hợp đồng (contract / 계약) kiểu (type / 타입) “tốt nhất” độc lập ngữ cảnh (context / 맥락). Cần hỏi ai kiểm soát rủi ro (risk / 위험) tốt hơn và đo lường (measurement / 측정) nào có thể enforce.

Rủi ro (risk / 위험) không thật sự biến mất khi “transfer” qua đặc tả hợp đồng (contract / 계약). Seller có thể chịu financial penalty nhưng buyer vẫn chịu nghiệp vụ (business / 비즈니스) delay, reputation hoặc tích hợp (integration / 통합) consequence.

> **Nối mạch:** **Fixed-price trong high bất định (uncertainty / 불확실성)** nối từ **Đặc tả hợp đồng (contract / 계약) kiểu (type / 타입) là incentive kiến trúc (architecture / 아키텍처)** sang **Statement of công việc (work / 작업) và acceptance ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Fixed-price trong high bất định (uncertainty / 불확실성)

Fixed-price/fixed-scope ở môi trường (environment / 환경) bất định (uncertainty / 불확실성) cao có thể tạo adversarial hành vi (behavior / 동작). Seller phải price rủi ro (risk / 위험) hoặc kiếm margin qua thay đổi (change / 변경) yêu cầu (request / 요청); buyer cố chứng minh item nằm trong phạm vi (scope / 범위).

Nếu yêu cầu (requirement / 요구사항) chưa ổn định, đặc tả hợp đồng (contract / 계약) theo increment, sức chứa (capacity / 용량) hoặc kết quả (outcome / 결과) có thể align collaboration tốt hơn tùy procurement rules. Nhưng flexibility cần quản trị (governance / 거버넌스) để không biến thành uncontrolled spend.

Một đặc tả hợp đồng (contract / 계약) “fixed” vẫn cần thay đổi (change / 변경) cơ chế (mechanism / 메커니즘) vì reality thay đổi. Không có cơ chế (mechanism / 메커니즘) không làm thay đổi (change / 변경) biến mất; nó chỉ đẩy negotiation sang informal channel hoặc dispute.

> **Nối mạch:** **Fixed-price trong high bất định (uncertainty / 불확실성)** đặt tiêu chí; **Statement of công việc (work / 작업) và acceptance ranh giới (boundary / 경계)** dùng nó để kiểm tra ranh giới, rồi **Seller selection không chỉ nhìn price** mở rộng cơ chế.

## Statement of công việc (work / 작업) và acceptance ranh giới (boundary / 경계)

Statement of công việc (work / 작업) hoặc procurement specification cần đủ rõ về deliverable, ranh giới (boundary / 경계), acceptance, schedule, responsibility và ràng buộc (constraint / 제약조건).

Ambiguity bị trì hoãn không biến mất; nó thường quay lại thành claim. Acceptance criterion càng mục tiêu (objective / 목표) càng giảm dispute.

SOW nên nói rõ giao diện (interface / 인터페이스) và buyer-provided phụ thuộc (dependency / 의존성). Nếu seller deliver đúng phần mình nhưng buyer không cung cấp môi trường (environment / 환경)/dữ liệu (data / 데이터) đúng hạn, dự án (project / 프로젝트) vẫn thất bại (fail / 실패) dù đặc tả hợp đồng (contract / 계약) phạm vi (scope / 범위) phía seller có vẻ clear.

> **Nối mạch:** **Statement of công việc (work / 작업) và acceptance ranh giới (boundary / 경계)** đặt tiêu chí; **Seller selection không chỉ nhìn price** dùng nó để kiểm tra ranh giới, rồi **SLA, KPI và kết quả (outcome / 결과)** mở rộng cơ chế.

## Seller selection không chỉ nhìn price

Selection có thể cân năng lực (capability / 역량), technical approach, financial stability, bảo mật (security / 보안), delivery bản ghi (record / 레코드), hỗ trợ (support / 지원) mô hình (model / 모델), total chi phí (cost / 비용) và strategic fit.

Weighted scoring giúp cấu trúc (structure / 구조) quyết định (decision / 결정) nhưng weight vẫn là judgment. Một ma trận (matrix / 행렬) đẹp không cứu đầu vào (input / 입력) độ lệch (bias / 편향) hoặc vendor tham chiếu (reference / 참조) không được verify.

Selection còn phải hỏi dạng thất bại (failure mode / 실패 모드): supplier này yếu nhất ở đâu, concentration rủi ro (risk / 위험) nào tồn tại, exit có khả thi không và bằng chứng (evidence / 증거) nào chứng minh claim marketing của vendor.

> **Nối mạch:** **SLA, KPI và kết quả (outcome / 결과)** nối từ **Seller selection không chỉ nhìn price** sang **Vendor hiệu năng (performance / 성능) và relationship**, vì cơ chế trước tạo đầu vào cho bước sau.

## SLA, KPI và kết quả (outcome / 결과)

Dịch vụ (service / 서비스) mức (level / 수준) Agreement định nghĩa dịch vụ (service / 서비스) expectation như availability, phản hồi (response / 응답) thời gian (time / 시간) hoặc khôi phục (recovery / 복구). KPI theo dõi hiệu năng (performance / 성능). Nhưng chỉ số (metric / 지표) cần liên hệ nghiệp vụ (business / 비즈니스) impact.

Vendor đáp SLA 99.9% nhưng outage luôn rơi đúng peak payment cửa sổ (window / 윈도우) có thể vẫn gây nghiệp vụ (business / 비즈니스) pain lớn. đặc tả hợp đồng (contract / 계약) chỉ số (metric / 지표) không thay operational lập luận (reasoning / 추론).

SLA cũng có thể bị cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화). Seller đạt response-time KPI bằng cách acknowledgement nhanh nhưng resolution chậm; buyer cần chỉ số (metric / 지표) ngữ nghĩa (semantic / 의미적) rõ và counter-metric cho hành vi (behavior / 동작) không mong muốn.

> **Nối mạch:** **Vendor hiệu năng (performance / 성능) và relationship** nối từ **SLA, KPI và kết quả (outcome / 결과)** sang **Supplier financial/sức chứa (capacity / 용량) health**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vendor hiệu năng (performance / 성능) và relationship

Vendor management cần mục tiêu (objective / 목표) metrics, acceptance criteria, rà soát (review / 검토) cadence và escalation đường dẫn (path / 경로). Payment milestone nên liên kết với deliverable/bằng chứng (evidence / 증거) có nghĩa, không chỉ “đã làm x% effort”.

Relationship tốt không có nghĩa bỏ đặc tả hợp đồng (contract / 계약). đặc tả hợp đồng (contract / 계약) cung cấp ranh giới (boundary / 경계); collaboration giúp solve bài toán (problem / 문제) bên trong ranh giới (boundary / 경계). Dùng penalty quá sớm có thể phá cooperation; không enforce khi material breach lại làm điều khiển (control / 제어) vô nghĩa.

Rà soát (review / 검토) cadence nên khác nhau theo phase và rủi ro (risk / 위험). Weekly deep rà soát (review / 검토) trong stabilization có thể hợp lý nhưng thành overhead trong steady phase. Procurement quản trị (governance / 거버넌스) cũng cần tailoring.

> **Nối mạch:** **Supplier financial/sức chứa (capacity / 용량) health** nối từ **Vendor hiệu năng (performance / 성능) và relationship** sang **Procurement thay đổi (change / 변경) và claim**, vì cơ chế trước tạo đầu vào cho bước sau.

## Supplier financial/sức chứa (capacity / 용량) health

Technical delivery tốt hôm nay không bảo đảm supplier còn sức chứa (capacity / 용량) hoặc financial health sáu tháng sau. trọng yếu (critical / 중요) procurement nên theo dõi tín hiệu (signal / 신호) như key-person turnover, subcontractor phụ thuộc (dependency / 의존성), cash-flow stress, backlog overload hoặc repeated missed commitment.

Mục tiêu không phải quản trị nội bộ vendor thay họ, mà phát hiện early warning trước khi thất bại (failure / 실패) thành delivery issue.

> **Nối mạch:** **Procurement thay đổi (change / 변경) và claim** nối từ **Supplier financial/sức chứa (capacity / 용량) health** sang **Claim anatomy: entitlement, causation và quantum**, vì cơ chế trước tạo đầu vào cho bước sau.

## Procurement thay đổi (change / 변경) và claim

Đặc tả hợp đồng (contract / 계약) thay đổi (change / 변경) cần formal cơ chế (mechanism / 메커니즘). Verbal yêu cầu (request / 요청) có thể tạo disputed phạm vi (scope / 범위). Claim xuất hiện khi party bất đồng về compensation, thời gian (time / 시간) hoặc obligation.

PM nên giữ records, correspondence, approved thay đổi (change / 변경) và acceptance bằng chứng (evidence / 증거) đủ tốt để dispute không phụ thuộc bộ nhớ (memory / 메모리). Legal/procurement specialist cần được involve khi issue vượt authority.

> **Nối mạch:** **Claim anatomy: entitlement, causation và quantum** nối từ **Procurement thay đổi (change / 변경) và claim** sang **Delay phân tích (analysis / 분석) và concurrent cause**, vì cơ chế trước tạo đầu vào cho bước sau.

## Claim anatomy: entitlement, causation và quantum

Một claim có chất lượng thường phải trả lời ba câu hỏi tách biệt. Entitlement hỏi đặc tả hợp đồng (contract / 계약) có cho bên yêu cầu quyền được thêm tiền/thời gian hoặc relief hay không. Causation hỏi sự kiện (event / 이벤트) được nêu có thật sự gây ra delay/chi phí (cost / 비용) đó không. Quantum hỏi nếu có entitlement và causation thì mức compensation/thời gian (time / 시간) extension hợp lý là bao nhiêu.

Nếu chỉ chứng minh “vendor đã gặp khó” nhưng không nối khó khăn đó với obligation cụ thể và impact đã đo được, claim yếu. Ngược lại, buyer cũng không nên từ chối claim chỉ vì kết quả (outcome / 결과) xấu nếu chính buyer đã thay yêu cầu (requirement / 요구사항), trì hoãn approval hoặc không cung cấp phụ thuộc (dependency / 의존성) đúng cam kết.

Mô hình tư duy (mental model / 사고 모델) này giúp dự án (project / 프로젝트) manager tránh biến claim thành tranh luận cảm tính. đặc tả hợp đồng (contract / 계약) ngôn ngữ (language / 언어), sự kiện (event / 이벤트) chronology, baseline, approved changes, contemporaneous records và impact phân tích (analysis / 분석) phải nối được với nhau.

> **Nối mạch:** **Delay phân tích (analysis / 분석) và concurrent cause** nối từ **Claim anatomy: entitlement, causation và quantum** sang **Negotiation: position khác interest**, vì cơ chế trước tạo đầu vào cho bước sau.

## Delay phân tích (analysis / 분석) và concurrent cause

Delay không phải lúc nào cũng có một nguyên nhân. Buyer có thể chậm dữ liệu (data / 데이터) truy cập (access / 접근) trong khi seller cũng chậm staffing. Nếu hai cause overlap, câu hỏi responsibility phức tạp hơn việc “ai trễ trước”.

Dự án (project / 프로젝트) manager không nên tự đóng vai legal expert, nhưng cần giữ schedule lô-gic (logic / 논리) và bằng chứng (evidence / 증거) đủ tốt để specialist phân tích. Nếu baseline không đáng tin, actual dates không được ghi, hoặc thay đổi (change / 변경) được thực hiện trước rồi mới document, dispute resolution trở nên đắt hơn nhiều.

Điểm quản lý quan trọng là preserve bằng chứng (evidence / 증거) khi sự kiện (event / 이벤트) xảy ra, không reconstruct bộ nhớ (memory / 메모리) nhiều tháng sau.

> **Nối mạch:** **Negotiation: position khác interest** nối từ **Delay phân tích (analysis / 분석) và concurrent cause** sang **Dispute ladder và escalation proportionality**, vì cơ chế trước tạo đầu vào cho bước sau.

## Negotiation: position khác interest

Position là điều một bên nói muốn, ví dụ “thêm 200 triệu” hoặc “không trả thêm”. Interest là concern phía sau: cash luồng (flow / 흐름), margin protection, deadline, reputation, sức chứa (capacity / 용량) hoặc future relationship.

Nếu chỉ bargaining trên position, negotiation dễ thành chia đôi con số. Nếu hiểu interest, có thể mở solution không gian (space / 공간): đổi milestone payment, giảm low-value phạm vi (scope / 범위), kéo dài schedule, tăng buyer-provided tài nguyên (resource / 자원), chia sẻ rủi ro (risk / 위험) hoặc đổi acceptance chuỗi (sequence / 시퀀스).

Một negotiation tốt cần biết BATNA — phương án tốt nhất nếu không đạt agreement. BATNA yếu làm một bên dễ chấp nhận deal tệ; BATNA mạnh nhưng được đánh giá sai có thể dẫn tới bluff nguy hiểm. dự án (project / 프로젝트) manager nên chuẩn bị mục tiêu (objective / 목표), authority limit, tradeable variables, bằng chứng (evidence / 증거) và walk-away điều kiện (condition / 조건) trước meeting.

> **Nối mạch:** **Dispute ladder và escalation proportionality** nối từ **Negotiation: position khác interest** sang **Incentive gaming và chỉ số (metric / 지표) thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dispute ladder và escalation proportionality

Không phải mọi disagreement cần legal escalation ngay. Một dispute ladder có thể đi từ working-level clarification → project-manager negotiation → commercial/procurement rà soát (review / 검토) → executive mediation → formal dispute cơ chế (mechanism / 메커니즘) theo đặc tả hợp đồng (contract / 계약).

Mục tiêu là giải ở mức (level / 수준) thấp nhất có đủ authority và expertise, nhưng không kéo dài informal discussion tới mức mất contractual notice deadline hoặc bằng chứng (evidence / 증거). Collaboration và rights preservation phải song song.

Nếu đặc tả hợp đồng (contract / 계약) yêu cầu notice trong 7 ngày, “giữ quan hệ nên chưa gửi notice” có thể vô tình làm mất quyền. Notice không nhất thiết là hành động thù địch; nó có thể là quản trị (governance / 거버넌스) cơ chế (mechanism / 메커니즘) để hai bên cùng nhìn thấy issue sớm.

> **Nối mạch:** **Incentive gaming và chỉ số (metric / 지표) thiết kế (design / 설계)** nối từ **Dispute ladder và escalation proportionality** sang **Procurement ethics và xung đột (conflict / 충돌) of interest**, vì cơ chế trước tạo đầu vào cho bước sau.

## Incentive gaming và chỉ số (metric / 지표) thiết kế (design / 설계)

Đặc tả hợp đồng (contract / 계약) chỉ số (metric / 지표) tạo hành vi (behavior / 동작). Nếu vendor được thưởng theo số ticket đóng, họ có incentive chia ticket nhỏ hoặc đóng sớm. Nếu payment chỉ theo milestone date, chất lượng (quality / 품질) debt có thể bị đẩy sang giai đoạn sau.

Chỉ số (metric / 지표) tốt phải gần kết quả (outcome / 결과), khó game và có counter-metric cho side tác động (effect / 효과). Ví dụ velocity không nên là commercial KPI nếu nó khuyến khích inflate story điểm (point / 지점). SLA availability có thể cần đi cùng severity, business-hour impact và khôi phục (recovery / 복구) chất lượng (quality / 품질).

Mọi incentive đều tạo tối ưu hóa (optimization / 최적화) pressure; procurement thiết kế (design / 설계) cần hỏi “nếu supplier tối ưu đúng chỉ số (metric / 지표) này, hệ thống (system / 시스템) hành vi (behavior / 동작) tệ nhất có thể là gì?”.

> **Nối mạch:** **Procurement ethics và xung đột (conflict / 충돌) of interest** nối từ **Incentive gaming và chỉ số (metric / 지표) thiết kế (design / 설계)** sang **Procurement rủi ro (risk / 위험) và supply chuỗi (chain / 사슬)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Procurement ethics và xung đột (conflict / 충돌) of interest

Vendor selection và negotiation dễ phát sinh xung đột (conflict / 충돌) of interest, gift, confidential thông tin (information / 정보) leak hoặc favoritism. Ethics không phải lớp phụ bên ngoài commercial quyết định (decision / 결정); nó bảo vệ tính legitimacy của quyết định (decision / 결정) và giảm legal/reputational rủi ro (risk / 위험).

Dự án (project / 프로젝트) manager nên disclose xung đột (conflict / 충돌), tách người đánh giá khi cần, giữ scoring bằng chứng (evidence / 증거) và không chia sẻ bid thông tin (information / 정보) không được phép. Một supplier tốt không nên được chọn bằng tiến trình (process / 프로세스) yếu, vì tiến trình (process / 프로세스) yếu làm quyết định (decision / 결정) khó defend khi kiểm tra (audit / 감사) hoặc dispute.

> **Nối mạch:** Procurement ethics và conflict of interest đặt ranh giới; Procurement risk và supply chain mô tả phụ thuộc. **Exit strategy và lock-in** kiểm tra khả năng rời nhà cung cấp.

## Procurement rủi ro (risk / 위험) và supply chuỗi (chain / 사슬)

Vendor có own vendor, geography, currency, regulation và sức chứa (capacity / 용량) rủi ro (risk / 위험). Buyer không nên dừng phân tích (analysis / 분석) ở tier-1 supplier nếu trọng yếu (critical / 중요) thành phần (component / 컴포넌트) phụ thuộc single nguồn (source / 소스).

Supply-chain ánh xạ (mapping / 매핑), alternate supplier hoặc buffer có thể giảm rủi ro (risk / 위험) nhưng tạo chi phí (cost / 비용). Procurement chiến lược (strategy / 전략) là rủi ro (risk / 위험) chiến lược (strategy / 전략).

Cần phân biệt redundancy thật với redundancy giả. Hai supplier khác tên nhưng cùng dùng một subcontractor hoặc cloud region không tạo independent fallback.

> **Nối mạch:** Procurement risk và supply chain làm lộ phụ thuộc; Exit strategy và lock-in cho biết chi phí rời đi. **Procurement closure** kiểm tra việc kết thúc có giữ được bằng chứng và quyền sở hữu hay không.

## Exit chiến lược (strategy / 전략) và lock-in

Đặc tả hợp đồng (contract / 계약) nên nghĩ về kết thúc từ đầu: dữ liệu (data / 데이터) export, IP quyền sở hữu (ownership / 소유권), chuyển tiếp (transition / 전이) assistance, documentation, mã nguồn (source code / 소스 코드)/escrow nếu relevant, account/truy cập (access / 접근) revocation và asset return.

Vendor lock-in không luôn xấu nếu benefit lớn, nhưng phải là quyết định (decision / 결정) có visibility. Hidden switching chi phí (cost / 비용) làm future organization mất option.

Exit chiến lược (strategy / 전략) tốt phải được kiểm thử (test / 테스트) ở mức phù hợp. “Có quyền export dữ liệu (data / 데이터)” không đủ nếu format proprietary và chưa ai thử restore sang hệ thống (system / 시스템) khác.

> **Nối mạch:** **Procurement closure** nối từ **Exit chiến lược (strategy / 전략) và lock-in** sang **Chất lượng (quality / 품질) và procurement nối nhau tại acceptance**, vì cơ chế trước tạo đầu vào cho bước sau.

## Procurement closure

Closure cần verify obligation, final acceptance, payment, claim resolution, asset/IP/dữ liệu (data / 데이터) transfer và bản ghi (record / 레코드) retention.

Closed đặc tả hợp đồng (contract / 계약) không đồng nghĩa vendor kiến thức (knowledge / 지식) đã chuyển. chuyển tiếp (transition / 전이) năng lực (capability / 역량) cần acceptance riêng nếu thao tác (operation / 연산) phụ thuộc nó.

> **Nối mạch:** **Chất lượng (quality / 품질) và procurement nối nhau tại acceptance** nối từ **Procurement closure** sang **Ví dụ scenario**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chất lượng (quality / 품질) và procurement nối nhau tại acceptance

Outsourced deliverable vẫn phải đáp dự án (project / 프로젝트) chất lượng (quality / 품질) yêu cầu (requirement / 요구사항). đặc tả hợp đồng (contract / 계약) acceptance criterion là cầu nối (bridge / 브리지) giữa procurement và chất lượng (quality / 품질).

Nếu buyer chỉ specify schedule/price mà chất lượng (quality / 품질) vague, xung đột (conflict / 충돌) gần như được thiết kế vào đặc tả hợp đồng (contract / 계약). Nếu chất lượng (quality / 품질) yêu cầu (requirement / 요구사항) unrealistic hoặc không testable, seller cũng không thể price rủi ro (risk / 위험) đúng.

Acceptance còn phải phân biệt conditional acceptance và final acceptance. Chấp nhận deliverable với open defect có thể hợp lý nếu rủi ro (risk / 위험) được hiểu và đơn vị sở hữu (owner / 오너) rõ, nhưng nếu exception biến thành default thì buyer tích chất lượng (quality / 품질) debt và mất leverage commercial.

> **Nối mạch:** **Chất lượng (quality / 품질) và procurement nối nhau tại acceptance** nêu quy tắc; **Ví dụ scenario** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Ví dụ scenario

Vendor thông báo delay hai tuần vì third-party API. PM không nên lập tức “ép vendor tăng người”. Trước hết cần kiểm tra đặc tả hợp đồng (contract / 계약) responsibility, phụ thuộc (dependency / 의존성), đường găng (critical path / 임계 경로), alternative/workaround, nguyên nhân gốc (root cause / 근본 원인), dịch vụ (service / 서비스) credit/claim nếu relevant và collaborative khôi phục (recovery / 복구) plan. đặc tả hợp đồng (contract / 계약) cho quyền; relationship và hệ thống (system / 시스템) lập luận (reasoning / 추론) quyết định cách dùng quyền đó.

Nếu vendor cho rằng buyer thay API specification muộn và yêu cầu extension 10 ngày cùng 80 triệu chi phí, PM không nên tranh luận ngay về con số 80. Cần tách entitlement, causation và quantum: thay đổi (change / 변경) nào được yêu cầu, ai authorize, thay đổi (change / 변경) nằm ngoài SOW không, nó tác động đường găng (critical path / 임계 경로) thế nào, chi phí (cost / 비용) bằng chứng (evidence / 증거) là gì, và có concurrent seller delay hay không. Khi bằng chứng (evidence / 증거) rõ, negotiation mới có solution không gian (space / 공간) thực.

Một scenario chất lượng (quality / 품질): UAT phát hiện nhiều defect nhưng tất cả tập trung ở yêu cầu (requirement / 요구사항) thay đổi muộn. Chỉ yêu cầu QA tăng regression kiểm thử (test / 테스트) không đủ. nhóm (team / 팀) cần inspect thay đổi (change / 변경) tiến trình (process / 프로세스), acceptance clarity và tích hợp (integration / 통합) timing, vì chất lượng (quality / 품질) thất bại (failure / 실패) có upstream cause.

Một scenario tài nguyên (resource / 자원): ba dự án (project / 프로젝트) cùng lập plan dùng một bảo mật (security / 보안) architect 50% trong cùng tháng. Mỗi plan riêng đều “đủ tài nguyên (resource / 자원)”, nhưng tổng demand là 150%. dự án (project / 프로젝트) manager không thể giải bằng motivational talk; organization cần portfolio priority, schedule shift hoặc năng lực (capability / 역량) redundancy.

> **Nối mạch:** Ví dụ scenario nêu quy tắc; **Mô hình tư duy** thử quy tắc trong tình huống cụ thể để khép mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> chất lượng (quality / 품질) bảo vệ fitness for purpose bằng tiến trình (process / 프로세스) năng lực (capability / 역량) và bằng chứng (evidence / 증거); tài nguyên (resource / 자원) management bảo vệ effective sức chứa (capacity / 용량) thay vì headcount danh nghĩa; procurement mở rộng dự án (project / 프로젝트) hệ thống (system / 시스템) qua organizational ranh giới (boundary / 경계) và vì thế phải thiết kế rủi ro (risk / 위험) allocation, incentive, bằng chứng (evidence / 증거), negotiation cơ chế (mechanism / 메커니즘) và exit đường dẫn (path / 경로) rõ ràng.

Tiếp theo: [Risk, uncertainty, issue và decision making](./08_risk_uncertainty_issues_and_decisions.md).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
