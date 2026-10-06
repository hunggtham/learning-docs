# 16 — End-to-end trường hợp (case / 사례) studies: predictive, adaptive và hybrid

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **16 — End-to-end trường hợp (case / 사례) studies: predictive, adaptive và hybrid**. Route đi từ context và quyết định của case predictive → adaptive → hybrid → trade-off, evidence, failure mode và chuyển mạch giữa domain, để người học theo dõi cách quyết định đổi khi trạng thái dự án đổi.

Các trường hợp (case / 사례) dưới đây cố ý đi xuyên nhiều lĩnh vực (domain / 도메인) để tránh thói quen học từng kiến thức (knowledge / 지식) area độc lập. Mỗi trường hợp (case / 사례) bắt đầu bằng ngữ cảnh (context / 맥락), sau đó theo chuỗi quyết định (decision / 결정), sự đánh đổi (trade-off / 트레이드오프), bằng chứng (evidence / 증거) và dạng thất bại (failure mode / 실패 모드). Mục tiêu không phải tìm một “đáp án chuẩn” duy nhất mà luyện cách đổi quyết định (decision / 결정) khi ngữ cảnh (context / 맥락) đổi.

Khi đọc, đừng chỉ hỏi “PM nên làm gì?”. Hãy giữ một trạng thái (state / 상태) mô hình (model / 모델) gồm mục tiêu (objective / 목표), delivery chế độ (mode / 모드), ràng buộc (constraint / 제약조건), authority, giả định (assumption / 가정), hiện tại (current / 현재) bằng chứng (evidence / 증거) và next irreversible quyết định (decision / 결정). Khi một tín hiệu (signal / 신호) mới xuất hiện, quan sát nó lan sang lĩnh vực (domain / 도메인) nào thay vì gắn nhãn ngay là “rủi ro (risk / 위험) question”, “schedule question” hay “stakeholder question”.

## Trường hợp (case / 사례) A — Predictive: mở trung tâm dữ liệu dự phòng

### Ngữ cảnh (context / 맥락)

Một công ty tài chính phải mở disaster-recovery site trước deadline regulatory. Location và sức chứa (capacity / 용량) đã được phê duyệt, construction/equipment có lead thời gian (time / 시간) dài, acceptance cần kiểm thử (test / 테스트) failover. yêu cầu (requirement / 요구사항) phần cứng tương đối ổn định; thay đổi (change / 변경) muộn rất đắt.

### Chọn approach

Predictive là lô-gic (logic / 논리) chính vì vật lý (physical / 물리적) phụ thuộc (dependency / 의존성), procurement lead thời gian (time / 시간) và compliance gate tạo strong sequencing. Điều này không cấm iteration ở subcomponent, nhưng overall milestones và baseline có giá trị coordination cao.

### Từ giá trị (value / 값) tới phạm vi (scope / 범위)

Kết quả (outcome / 결과) không phải “xây xong site” mà là nghiệp vụ (business / 비즈니스) dịch vụ (service / 서비스) có khả năng failover trong RTO/RPO yêu cầu. Vì thế phạm vi (scope / 범위) phải gồm mạng (network / 네트워크), dữ liệu (data / 데이터) replication, runbook, kiểm thử (test / 테스트), huấn luyện (training / 학습) và regulatory bằng chứng (evidence / 증거); nếu chỉ WBS construction thì đầu ra (output / 출력) không đạt kết quả (outcome / 결과).

### Integrated planning

Charter nên làm rõ regulatory mục tiêu (objective / 목표), sponsor, deadline, authority và success criteria. WBS tách facility, power, mạng (network / 네트워크), replication, bảo mật (security / 보안), kiểm thử (test / 테스트) và operational readiness, nhưng integrated schedule phải giữ phụ thuộc (dependency / 의존성) giữa chúng.

Nếu generator tới đúng hạn nhưng mạng (network / 네트워크) circuit chưa được carrier provision, facility completion không tạo usable kết quả (outcome / 결과). Đây là tích hợp (integration / 통합) bài toán (problem / 문제) chứ không chỉ schedule bài toán (problem / 문제).

### Schedule và procurement

Long-lead generator và mạng (network / 네트워크) equipment có thể nằm trên đường găng (critical path / 임계 경로). Procurement chiến lược (strategy / 전략) cần đặc tả hợp đồng (contract / 계약) acceptance, delivery milestone và supplier rủi ro (risk / 위험). Nếu vendor delay, PM kiểm tra critical-path impact, đặc tả hợp đồng (contract / 계약) right, alternative supplier và contingency thay vì chỉ yêu cầu overtime.

Suppose generator có 8 tuần lead thời gian (time / 시간) và float gần zero, còn office furniture có 4 tuần float. Procurement nhóm (team / 팀) không nên ưu tiên hai gói (package / 패키지) theo cùng urgency chỉ vì cả hai “đang trễ”.

### Rủi ro (risk / 위험) và reserve

Rủi ro (risk / 위험) register có thể gồm permit delay, supply-chain disruption, failover defect, power-load issue và regulator scheduling. Contingency reserve nên gắn với identified bất định (uncertainty / 불확실성) thay vì padding ngầm trong từng gói (package / 패키지).

Nếu supply-chain disruption có xác suất (probability / 확률) thấp nhưng impact regulatory rất lớn, threat phản hồi (response / 응답) có thể là second supplier hoặc early thứ tự (order / 순서) dù expected chi phí (cost / 비용) tăng.

### Chất lượng (quality / 품질)/compliance

Chất lượng (quality / 품질) bằng chứng (evidence / 증거) là failover kiểm thử (test / 테스트) và dịch vụ (service / 서비스) criteria, không chỉ visual inspection facility. Compliance gate phải được đưa vào plan sớm; regulator approval không thể “kiểm thử (test / 테스트) cuối rồi sửa”.

Yêu cầu (requirement / 요구사항) traceability nối regulation → thiết kế (design / 설계) điều khiển (control / 제어) → trường hợp kiểm thử (test case / 테스트 케이스) → bằng chứng (evidence / 증거) gói (package / 패키지). Nếu điều khiển (control / 제어) bằng chứng (evidence / 증거) không traceable, dự án (project / 프로젝트) có thể technically ready nhưng chưa governance-ready.

### Thay đổi (change / 변경) scenario

Nghiệp vụ (business / 비즈니스) muốn thêm extra analytics môi trường (environment / 환경) trong site vì “đang xây rồi thì làm luôn”. Technical công việc (work / 작업) có vẻ nhỏ nhưng có thể tăng power, mạng (network / 네트워크), bảo mật (security / 보안) phạm vi (scope / 범위) và delay approval.

Đây là phạm vi (scope / 범위) thay đổi (change / 변경) cần impact phân tích (analysis / 분석). Nếu analytics không liên quan regulatory kết quả (outcome / 결과) và threaten deadline, quyết định (decision / 결정) có thể defer sang dự án (project / 프로젝트) khác thay vì gold plating.

### Closure

Closure chỉ xảy ra khi operations có quyền sở hữu (ownership / 소유권), runbook/truy cập (access / 접근)/monitoring, DR drill được chấp nhận, đặc tả hợp đồng (contract / 계약)/financials đóng và bằng chứng (evidence / 증거) archived. Benefit—resilience/compliance—sống trong operations sau dự án (project / 프로젝트).

### Dạng thất bại (failure mode / 실패 모드) nếu quản lý theo tác vụ (task / 작업)

Mọi construction tác vụ (task / 작업) có thể “green” nhưng failover rehearsal thất bại vì ứng dụng (application / 애플리케이션) phụ thuộc (dependency / 의존성) chưa được map. Đây là ví dụ cục bộ (local / 로컬) completion không bằng hệ thống (system / 시스템) readiness.

> **Nối mạch:** **Trường hợp (case / 사례) A — Predictive: mở trung tâm dữ liệu dự phòng** nêu quy tắc; **Trường hợp (case / 사례) B — Adaptive: xây sản phẩm mobile mới trong thị trường chưa chắc chắn** thử quy tắc trong tình huống, rồi **Trường hợp (case / 사례) C — Hybrid: ngân hàng triển khai eKYC với bên ngoài (external / 외부) vendor** mở rộng hệ quả.

## Trường hợp (case / 사례) B — Adaptive: xây sản phẩm mobile mới trong thị trường chưa chắc chắn

### Ngữ cảnh (context / 맥락)

Startup biết customer bài toán (problem / 문제) nhưng chưa biết tính năng (feature / 기능) set nào tạo retention. Technical nền tảng (platform / 플랫폼) đủ linh hoạt để ship increment hàng tuần. Deadline không regulatory; runway là ràng buộc (constraint / 제약조건) chính.

### Chọn approach

Adaptive delivery tối ưu học tập (learning / 학습). Roadmap nên định nghĩa kết quả (outcome / 결과)/hypothesis, còn backlog giữ option. Việc lập một WBS chi tiết 12 tháng sẽ tạo false precision.

### Nghiệp vụ (business / 비즈니스) hypothesis

Giả thuyết ban đầu là người dùng (user / 사용자) bỏ dịch vụ (service / 서비스) vì onboarding quá khó. kết quả (outcome / 결과) mục tiêu (target / 대상) không phải “ship 20 tính năng (feature / 기능)” mà là tăng activation và retention với runway hữu hạn.

Điều này ảnh hưởng priority: analytics instrumentation có thể được làm sớm dù customer không thấy vì nó tạo bằng chứng (evidence / 증거) cho hypothesis.

### Value-based delivery

Nhóm (team / 팀) bắt đầu với onboarding + cốt lõi (core / 핵심) hành động (action / 동작) nhỏ nhất để đo activation. Mỗi increment có Definition of Done và telemetry. tính năng (feature / 기능) yêu cầu (request / 요청) được ưu tiên theo customer bằng chứng (evidence / 증거), strategic fit, rủi ro (risk / 위험), phụ thuộc (dependency / 의존성) và học tập (learning / 학습) giá trị (value / 값) chứ không theo người nói to nhất.

### Discovery thất bại (failure / 실패)

Customer interview nói họ muốn xã hội (social / 사회적) tính năng (feature / 기능), nhưng prototype cho thấy tính năng (feature / 기능) gần như không ảnh hưởng retention. nhóm (team / 팀) không nên tiếp tục chỉ vì đã đưa xã hội (social / 사회적) tính năng (feature / 기능) vào roadmap slide.

Adaptive quản trị (governance / 거버넌스) cho phép bỏ option khi bằng chứng (evidence / 증거) thay đổi. Sunk effort trong discovery không phải lý do bản dựng (build / 빌드) full tính năng (feature / 기능).

### Chỉ số (metric / 지표) trap

Nếu nhóm (team / 팀) chỉ tối ưu velocity, story điểm (point / 지점) có thể tăng nhưng retention không đổi. dự án (project / 프로젝트)/sản phẩm (product / 제품) leadership phải nối delivery chỉ số (metric / 지표) với kết quả (outcome / 결과) chỉ số (metric / 지표). luồng (flow / 흐름) chỉ số (metric / 지표) giúp delivery; sản phẩm (product / 제품) chỉ số (metric / 지표) giúp nghiệp vụ (business / 비즈니스) học tập (learning / 학습).

Nếu activation tăng nhưng hỗ trợ (support / 지원) ticket và refund cũng tăng, nhóm (team / 팀) cần mở ranh giới (boundary / 경계) đo lường (measurement / 측정) thay vì tuyên bố success từ một chỉ số (metric / 지표).

### Schedule và forecasting

Bản phát hành (release / 릴리스) forecast có thể dựa trên thông lượng (throughput / 처리량)/cycle-time phân phối (distribution / 분포) thay vì detailed long-range tác vụ (task / 작업) estimate. Khi WIP tăng, cycle thời gian (time / 시간) tăng dù velocity gần như giữ nguyên, nhóm (team / 팀) cần inspect luồng (flow / 흐름) trước khi thêm người.

### Rủi ro (risk / 위험)

Rủi ro (risk / 위험) lớn nhất có thể là thị trường (market / 시장) rủi ro (risk / 위험) chứ không technical rủi ro (risk / 위험). phản hồi (response / 응답) tốt là experiment sớm, không phải thêm buffer schedule. Một prototype có thể “thất bại” về tính năng (feature / 기능) nhưng thành công vì loại bỏ giả định (assumption / 가정) sai.

Technical rủi ro (risk / 위험) vẫn tồn tại. Nếu payment tích hợp (integration / 통합) chưa được thử với production-like tải (load / 로드), spike sớm có thông tin (information / 정보) giá trị (value / 값) cao hơn polish UI.

### Quản trị (governance / 거버넌스)

Adaptive không nghĩa không quản trị (governance / 거버넌스). Runway/ngân sách (budget / 예산) threshold, privacy/bảo mật (security / 보안) và brand rủi ro (risk / 위험) vẫn có guardrail. quyết định (decision / 결정) reversible được nhóm (team / 팀) tự chủ; high-impact chính sách (policy / 정책) quyết định (decision / 결정) escalate.

### Closure hoặc chuyển tiếp (transition / 전이)

Nếu initiative chứng minh product-market tín hiệu (signal / 신호), temporary dự án (project / 프로젝트) chế độ (mode / 모드) có thể chuyển sang long-lived sản phẩm (product / 제품) nhóm (team / 팀). Nếu hypothesis thất bại (fail / 실패), closure có thể là stop investment và preserve học tập (learning / 학습) thay vì “ship cho xong vì đã làm nhiều”.

### Dạng thất bại (failure mode / 실패 모드) nếu hiểu Agile như ceremony

Nhóm (team / 팀) chạy sprint, daily và retrospective nhưng founder khóa roadmap sáu tháng và mọi yêu cầu (request / 요청) đều “must-have”. phản hồi (feedback / 피드백) không thay quyết định (decision / 결정); hệ thống (system / 시스템) chỉ có ceremony, không có adaptation.

> **Nối mạch:** **Trường hợp (case / 사례) B — Adaptive: xây sản phẩm mobile mới trong thị trường chưa chắc chắn** nêu quy tắc; **Trường hợp (case / 사례) C — Hybrid: ngân hàng triển khai eKYC với bên ngoài (external / 외부) vendor** thử quy tắc trong tình huống, rồi **Trường hợp (case / 사례) D — Troubled dự án (project / 프로젝트) khôi phục (recovery / 복구): ERP rollout đang đỏ** mở rộng hệ quả.

## Trường hợp (case / 사례) C — Hybrid: ngân hàng triển khai eKYC với bên ngoài (external / 외부) vendor

### Ngữ cảnh (context / 맥락)

Ngân hàng có deadline nghiệp vụ (business / 비즈니스), privacy/bảo mật (security / 보안) chính sách (policy / 정책), vendor OCR/face matching, tích hợp (integration / 통합) với backend cũ và UX cần được kiểm thử (test / 테스트) với người dùng (user / 사용자). Một số bên ngoài (external / 외부) giao diện (interface / 인터페이스) và UAT gate cố định; UX/luồng (flow / 흐름) còn bất định (uncertainty / 불확실성).

### Decompose theo bất định (uncertainty / 불확실성)

Compliance yêu cầu (requirement / 요구사항), dữ liệu (data / 데이터) retention, vendor đặc tả hợp đồng (contract / 계약) và môi trường vận hành (production / 운영 환경) cutover cần điều khiển (control / 제어) mạnh. UX và error-flow có thể iterative. Hybrid được thiết kế từ ranh giới (boundary / 경계) này thay vì trộn ceremony tùy ý.

### Stakeholder map

Sponsor quan tâm deadline/adoption; compliance quan tâm lawful processing; bảo mật (security / 보안) quan tâm attack/dữ liệu (data / 데이터) exposure; operations quan tâm supportability; vendor quan tâm đặc tả hợp đồng (contract / 계약) ranh giới (boundary / 경계); người dùng (user / 사용자) quan tâm friction/privacy. Communication phải tailor theo quyết định (decision / 결정) need.

### Early rủi ro (risk / 위험) reduction

Thay vì chờ full tích hợp (integration / 통합) rồi UAT, nhóm (team / 팀) prototype API, kiểm thử (test / 테스트) representative ID-card images, đo accuracy theo segment và xác nhận thất bại (failure / 실패) fallback. Đây là mua thông tin (information / 정보) sớm để giảm rework.

### Procurement giao diện (interface / 인터페이스)

Vendor đặc tả hợp đồng (contract / 계약) fixed một số SLA/API obligation, nhưng UX backlog adaptive. Nếu UX thay đổi (change / 변경) làm API volume tăng gấp ba, sản phẩm (product / 제품) quyết định (decision / 결정) có thể chạm commercial term dù “chỉ đổi luồng (flow / 흐름)”. Hybrid giao diện (interface / 인터페이스) phải nối backlog thay đổi (change / 변경) với vendor impact phân tích (analysis / 분석).

### Schedule giao diện (interface / 인터페이스)

Nhóm (team / 팀) có sprint hai tuần nhưng bank UAT cửa sổ (window / 윈도우) chỉ mở hàng tháng. nội bộ (internal / 내부) Definition of Done không đồng nghĩa bên ngoài (external / 외부) acceptance. Plan cần trạng thái (state / 상태) rõ: mã (code / 코드) complete, integrated, UAT accepted và môi trường vận hành (production / 운영 환경) ready là các trạng thái khác nhau.

### Thay đổi (change / 변경) scenario

Giữa UAT, regulator yêu cầu thêm consent wording và retention bằng chứng (evidence / 증거). Đây không chỉ là “UI văn bản (text / 텍스트) thay đổi (change / 변경)”. PM đánh giá yêu cầu (requirement / 요구사항)/compliance impact, vendor/dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기), kiểm thử (test / 테스트) bằng chứng (evidence / 증거), schedule và approval. Mandatory compliance phạm vi (scope / 범위) được ưu tiên; optional tính năng (feature / 기능) có thể bị đẩy sau go-live để bảo vệ deadline.

### Sự cố (incident / 인시던트) trước go-live

Kiểm thử tải (load test / 부하 테스트) phát hiện face-matching hết thời gian chờ (timeout / 타임아웃) ở peak. PM không nên chỉ yêu cầu “optimize mã (code / 코드)”. nhóm (team / 팀) cần xác định bottleneck phía vendor/mạng (network / 네트워크)/ứng dụng (application / 애플리케이션), nghiệp vụ (business / 비즈니스) impact, SLA, sức chứa (capacity / 용량) option, degradation/fallback và go-live threshold. Nếu thất bại (failure / 실패) vượt rủi ro (risk / 위험) tolerance, quản trị (governance / 거버넌스) quyết định go/no-go dựa bằng chứng (evidence / 증거).

### AI/model-quality scenario

OCR accuracy trung bình 98% nhưng giấy tờ cũ của một nhóm customer chỉ 85%. Average chỉ số (metric / 지표) che segment rủi ro (risk / 위험). nhóm (team / 팀) cần phân loại impact, manual fallback, nghiệp vụ (business / 비즈니스) volume và fairness/customer friction trước khi quyết rollout.

Nếu nhóm đó chỉ 1% volume và manual fallback xử lý được, phản hồi (response / 응답) khác trường hợp nhóm đó chiếm 30% người dùng (user / 사용자) hoặc regulation yêu cầu equal treatment.

### Chuyển tiếp (transition / 전이)

Operations cần dashboard, alert, vendor escalation, manual fallback, privacy sự cố (incident / 인시던트) procedure và kiến thức (knowledge / 지식) transfer. dự án (project / 프로젝트) closure không thể chỉ dựa vào UAT sign-off nếu hỗ trợ (support / 지원) mô hình (model / 모델) chưa sẵn sàng.

### Dạng thất bại (failure mode / 실패 모드) nếu hybrid chỉ là tên

Nếu nhóm (team / 팀) vừa giữ full upfront specification, vừa có sprint ceremony, vừa phải submit mọi backlog reorder cho CCB, overhead tăng mà phản hồi (feedback / 피드백) không nhanh hơn. Hybrid tốt chọn cơ chế (mechanism / 메커니즘) theo ràng buộc (constraint / 제약조건); hybrid xấu cộng tất cả ceremony.

> **Nối mạch:** **Trường hợp (case / 사례) C — Hybrid: ngân hàng triển khai eKYC với bên ngoài (external / 외부) vendor** nêu quy tắc; **Trường hợp (case / 사례) D — Troubled dự án (project / 프로젝트) khôi phục (recovery / 복구): ERP rollout đang đỏ** thử quy tắc trong tình huống, rồi **Trường hợp (case / 사례) E — AI-assisted claims processing với sustainability và quản trị (governance / 거버넌스)** mở rộng hệ quả.

## Trường hợp (case / 사례) D — Troubled dự án (project / 프로젝트) khôi phục (recovery / 복구): ERP rollout đang đỏ

### Ngữ cảnh (context / 맥락)

Một ERP transformation 18 tháng đã dùng 70% ngân sách (budget / 예산). kiểm thử tích hợp (integration test / 통합 테스트) trễ hai tháng, nghiệp vụ (business / 비즈니스) đơn vị (unit / 단위) liên tục thêm yêu cầu (requirement / 요구사항), vendor blame nội bộ (internal / 내부) dữ liệu (data / 데이터) chất lượng (quality / 품질), sponsor vẫn yêu cầu original go-live vì đã công bố với board.

### Bước đầu không phải lập khôi phục (recovery / 복구) plan ngay

PM mới vào không nên lập tức yêu cầu overtime hoặc rebaseline. Trước hết cần reconstruct trạng thái (state / 상태): approved phạm vi (scope / 범위), actual completion bằng chứng (evidence / 증거), open defect, dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) readiness, đặc tả hợp đồng (contract / 계약) obligation, trọng yếu (critical / 중요) phụ thuộc (dependency / 의존성), chi phí (cost / 비용) forecast và quyết định (decision / 결정) authority.

Nếu status lịch sử dùng percent complete chủ quan, dashboard cũ không đủ làm bằng chứng (evidence / 증거).

### Sunk chi phí (cost / 비용)

70% spend đã xảy ra không chứng minh dự án (project / 프로젝트) nên tiếp tục original plan. quản trị (governance / 거버넌스) cần future-cost/future-value phân tích (analysis / 분석).

Nếu remaining investment vẫn tạo strategic năng lực (capability / 역량) nhưng original go-live không realistic, khôi phục (recovery / 복구) có thể hợp lý. Nếu nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) đã mất giá trị (value / 값), stop/pivot cũng là option hợp lệ.

### Phạm vi (scope / 범위) stabilization

Yêu cầu (requirement / 요구사항) churn cần phân loại mandatory, committed, optional và future enhancement. Freeze toàn bộ phạm vi (scope / 범위) có thể sai nếu compliance need mới xuất hiện; tiếp tục nhận mọi yêu cầu (request / 요청) cũng sai.

Thay đổi (change / 변경) quản trị (governance / 거버넌스) cần được reset với tường minh (explicit / 명시적) threshold và sản phẩm (product / 제품)/nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너).

### Vendor xung đột (conflict / 충돌)

Không bắt đầu bằng blame. rà soát (review / 검토) đặc tả hợp đồng (contract / 계약), acceptance criterion, responsibility ma trận (matrix / 행렬) và bằng chứng (evidence / 증거) về dữ liệu (data / 데이터) chất lượng (quality / 품질). Có thể nguyên nhân gốc (root cause / 근본 원인) dùng chung (shared / 공유): buyer dữ liệu (data / 데이터) cleansing trễ và vendor tooling yếu.

Khôi phục (recovery / 복구) plan cần hành động (action / 동작) đơn vị sở hữu (owner / 오너) hai bên, milestone bằng chứng (evidence / 증거) và escalation đường dẫn (path / 경로). Claim/legal handling tách khỏi technical khôi phục (recovery / 복구) khi cần.

### Forecast và rebaseline

Chỉ rebaseline sau khi planning basis mới đủ credible và authority approve. Rebaseline không xóa lịch sử (history / 이력); original variance và rationale phải được giữ để học tập (learning / 학습)/quản trị (governance / 거버넌스).

### Nhóm (team / 팀) health

Nếu nhóm (team / 팀) đã overtime nhiều tháng, thêm pressure có thể tăng defect. khôi phục (recovery / 복구) cần sức chứa (capacity / 용량) realism và psychological an toàn (safety / 안전) để bad news được nói ra.

### Quyết định (decision / 결정)

Một khôi phục (recovery / 복구) proposal tốt có option: phased rollout, reduced phạm vi (scope / 범위), delayed full rollout hoặc terminate mô-đun (module / 모듈). Mỗi option cần giá trị (value / 값), chi phí (cost / 비용), rủi ro (risk / 위험) và chuyển tiếp (transition / 전이) impact.

### Dạng thất bại (failure mode / 실패 모드)

“Red dự án (project / 프로젝트)” thường bị cứu bằng kế hoạch đẹp hơn mà không sửa thông tin (information / 정보) chất lượng (quality / 품질), quản trị (governance / 거버넌스) hoặc phạm vi (scope / 범위) coupling. Khi sensor vẫn sai, khôi phục (recovery / 복구) plan cũng chỉ là fiction mới.

> **Nối mạch:** **Trường hợp (case / 사례) D — Troubled dự án (project / 프로젝트) khôi phục (recovery / 복구): ERP rollout đang đỏ** nêu quy tắc; **Trường hợp (case / 사례) E — AI-assisted claims processing với sustainability và quản trị (governance / 거버넌스)** thử quy tắc trong tình huống, rồi **Trường hợp (case / 사례) F — Portfolio/PMO: nhiều initiative cùng tranh một thay đổi (change / 변경) sức chứa (capacity / 용량)** mở rộng hệ quả.

## Trường hợp (case / 사례) E — AI-assisted claims processing với sustainability và quản trị (governance / 거버넌스)

### Ngữ cảnh (context / 맥락)

Một insurer muốn dùng generative AI để hỗ trợ claim assessor, giảm handling thời gian (time / 시간) 30%. Vendor mô hình (model / 모델) là cloud dịch vụ (service / 서비스). dữ liệu (data / 데이터) chứa personal/medical thông tin (information / 정보). Management muốn pilot nhanh vì competitor đã công bố AI năng lực (capability / 역량).

### Bài toán (problem / 문제) framing

Mục tiêu (objective / 목표) là giảm processing thời gian (time / 시간) mà không tăng incorrect claim quyết định (decision / 결정) hoặc privacy rủi ro (risk / 위험). “Dùng GenAI” là solution hypothesis, không phải mục tiêu (objective / 목표).

### Delivery approach

Pilot/adaptive học tập (learning / 학습) phù hợp vì mô hình (model / 모델) hành vi (behavior / 동작) và người dùng (user / 사용자) workflow bất định (uncertainty / 불확실성) cao. Nhưng privacy, bảo mật (security / 보안), legal approval và data-location ràng buộc (constraint / 제약조건) cần quản trị (governance / 거버넌스) cứng. Đây là hybrid dự án (project / 프로젝트) ngay từ nature của ràng buộc (constraint / 제약조건).

### Dữ liệu (data / 데이터) và chất lượng (quality / 품질)

Evaluation không chỉ dùng average accuracy. nhóm (team / 팀) cần segment claim kiểu (type / 타입), severity của lỗi (error / 오류), hallucination/factual inconsistency và human override.

Một 2% lỗi (error / 오류) tỷ lệ (rate / 비율) có thể acceptable cho draft summarization nhưng unacceptable nếu hệ thống (system / 시스템) auto-deny claim. Same mô hình (model / 모델), different quyết định (decision / 결정) consequence, different quản trị (governance / 거버넌스).

### Human-in-the-loop

Assessor phải rà soát (review / 검토) recommendation trước final quyết định (decision / 결정). Nhưng điều khiển (control / 제어) chỉ thật nếu tải công việc (workload / 워크로드) cho phép rà soát (review / 검토) meaningful. Nếu mục tiêu (target / 대상) productivity ép reviewer approve 100 trường hợp (case / 사례)/giờ, human-in-the-loop có thể thành theater.

### Vendor/procurement

Đặc tả hợp đồng (contract / 계약) cần dữ liệu (data / 데이터) handling, mô hình (model / 모델)/phiên bản (version / 버전) thay đổi (change / 변경) notification, sự cố (incident / 인시던트), availability, IP và exit/export. Cheap API price không phản ánh switching chi phí (cost / 비용) hoặc regulatory exposure.

### Sustainability

AI suy luận (inference / 추론) tăng compute spend. dự án (project / 프로젝트) có thể đo chi phí (cost / 비용)/năng lượng (energy / 에너지) proxy per claim và total volume. Nếu automation làm claim volume processed tăng mạnh, đơn vị (unit / 단위) efficiency không đủ để kết luận total footprint giảm.

### Go/no-go

Pilot giảm handling 28%, serious lỗi (error / 오류) dưới threshold ở low-risk claim nhưng high-risk medical claim vẫn không ổn. Option hợp lý có thể limited rollout cho low-risk segment với mandatory human rà soát (review / 검토), còn high-risk giữ manual tiến trình (process / 프로세스) và tiếp tục evaluation.

Đây là rủi ro (risk / 위험) segmentation, không nhị phân (binary / 이진) “AI rollout” hay “AI thất bại (fail / 실패)”.

### Benefits realization

Sau rollout cần đo actual handling thời gian (time / 시간), assessor adoption, override tỷ lệ (rate / 비율), complaint, lỗi (error / 오류), vendor spend và sự cố (incident / 인시던트). Pilot success không chứng minh môi trường vận hành (production / 운영 환경) benefit nếu hành vi (behavior / 동작) thay đổi ở quy mô (scale / 규모).

> **Nối mạch:** Case E cho thấy AI-assisted claims processing phải nối sustainability với governance; **Case F** thử cùng logic khi nhiều initiative tranh một change capacity. **Cross-case synthesis** rút ra invariant và variable làm quyết định đổi.

## Trường hợp (case / 사례) F — Portfolio/PMO: nhiều initiative cùng tranh một thay đổi (change / 변경) sức chứa (capacity / 용량)

### Ngữ cảnh (context / 맥락)

Một ngân hàng đang chạy đồng thời core-banking modernization, CRM replacement, eKYC upgrade, mobile redesign và regulatory reporting. Mỗi dự án (project / 프로젝트) riêng lẻ đều có nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) hợp lý. Tuy nhiên ba initiative cùng cần một tích hợp (integration / 통합) nhóm (team / 팀), hai dự án (project / 프로젝트) cùng yêu cầu branch staff huấn luyện (training / 학습) trong quý IV và nhiều bản phát hành (release / 릴리스) cùng nhắm một môi trường vận hành (production / 운영 환경) cửa sổ (window / 윈도우).

Đây là bài toán (problem / 문제) mà project-level tối ưu hóa (optimization / 최적화) không giải được. Nếu từng PM chỉ bảo vệ milestone của mình, organization có thể tạo tài nguyên (resource / 자원) contention, bản phát hành (release / 릴리스) collision và thay đổi (change / 변경) saturation dù từng plan nhìn hợp lý độc lập.

### Portfolio view

Portfolio quản trị (governance / 거버넌스) hỏi investment nào tạo strategic giá trị (value / 값) cao hơn trong ràng buộc (constraint / 제약조건) chung, phụ thuộc (dependency / 의존성) nào cần chuỗi (sequence / 시퀀스) và initiative nào nên defer, phase hoặc stop. quyết định (decision / 결정) không dựa vào ai escalate mạnh nhất mà vào chiến lược (strategy / 전략), mandatory obligation, expected giá trị (value / 값), rủi ro (risk / 위험), sức chứa (capacity / 용량) và timing.

Một regulatory reporting dự án (project / 프로젝트) có ROI trực tiếp thấp nhưng deadline pháp lý cứng. Mobile redesign có customer giá trị (value / 값) cao nhưng flexible timing hơn. Portfolio priority vì vậy không đồng nghĩa xếp dự án (project / 프로젝트) theo financial ROI đơn giản.

### PMO như thông tin (information / 정보)/điều khiển (control / 제어) năng lực (capability / 역량)

PMO không chỉ thu status slide. Một PMO hữu ích làm cross-project phụ thuộc (dependency / 의존성), shared-resource demand, quyết định (decision / 결정) độ trễ (latency / 지연 시간), dùng chung (common / 공통) rủi ro (risk / 위험) và benefit visibility trở nên comparable.

Nếu mỗi dự án (project / 프로젝트) định nghĩa “green”, “complete” và “trọng yếu (critical / 중요)” khác nhau, portfolio dashboard chỉ cộng nhiều ngữ nghĩa (semantic / 의미적) không tương thích. PMO cần minimum thông tin (information / 정보) đặc tả hợp đồng (contract / 계약) đủ để leadership nhìn hệ thống (system / 시스템) trạng thái (state / 상태) mà không ép mọi nhóm (team / 팀) dùng cùng delivery phương thức (method / 메서드).

### Cross-project phụ thuộc (dependency / 의존성)

eKYC cần định danh (identity / 식별자) nền tảng (platform / 플랫폼) từ cốt lõi (core / 핵심) modernization; mobile redesign cũng cần định danh (identity / 식별자) API đó. Nếu định danh (identity / 식별자) công việc (work / 작업) slip, hai dự án (project / 프로젝트) cùng bị tác động. Tách rủi ro (risk / 위험) thành hai register không làm exposure độc lập hơn.

Portfolio/PMO nên nhìn dùng chung (shared / 공유) phụ thuộc (dependency / 의존성) như một miền lỗi (failure domain / 장애 도메인), xác định đơn vị sở hữu (owner / 오너) ở mức (level / 수준) phù hợp và tránh hai PM cùng “đòi ưu tiên” tài nguyên (resource / 자원) theo cách cục bộ.

### Thay đổi (change / 변경) saturation

CRM và cốt lõi (core / 핵심) dự án (project / 프로젝트) đều lập huấn luyện (training / 학습) plan tốt nếu xét riêng. Nhưng cùng branch employee phải học hai tiến trình (process / 프로세스) mới trong ba tuần trước year-end peak. Adoption rủi ro (risk / 위험) đến từ tổng tải thay đổi, không phải chất lượng một huấn luyện (training / 학습) deck.

Phản hồi (response / 응답) có thể là chuỗi (sequence / 시퀀스) rollout, segment population, giảm simultaneous thay đổi (change / 변경) hoặc thêm chuyển tiếp (transition / 전이) hỗ trợ (support / 지원). “Mỗi dự án (project / 프로젝트) đã có thay đổi (change / 변경) plan” không chứng minh organization có sức chứa (capacity / 용량) hấp thụ tổng thay đổi (change / 변경).

### Sức chứa (capacity / 용량) xung đột (conflict / 충돌)

Tích hợp (integration / 통합) nhóm (team / 팀) chỉ có 8 người nhưng demand từ năm initiative tương đương 15 người trong cùng tháng. Yêu cầu từng dự án (project / 프로젝트) “làm nhanh hơn” không tạo sức chứa (capacity / 용량) mới.

Portfolio option gồm resequence, reduce phạm vi (scope / 범위), thuê thêm năng lực (capability / 역량) nếu onboarding economics hợp lý, hoặc protect mandatory công việc (work / 작업) trước. quyết định (decision / 결정) phải nhìn opportunity chi phí (cost / 비용): ưu tiên dự án (project / 프로젝트) A nghĩa dự án (project / 프로젝트) B bị chậm bao nhiêu giá trị (value / 값) hoặc rủi ro (risk / 위험).

### Benefits và continuation

Sau sáu tháng, CRM dự án (project / 프로젝트) vẫn on-budget nhưng adoption thấp; mobile dự án (project / 프로젝트) tạo benefit cao hơn dự kiến. Portfolio rà soát (review / 검토) không nên giữ funding chỉ vì annual plan đã approve. nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) là living quyết định (decision / 결정) đối tượng (object / 객체).

Tuy nhiên stop một initiative cũng có chuyển tiếp (transition / 전이) chi phí (cost / 비용), đặc tả hợp đồng (contract / 계약) obligation và phụ thuộc (dependency / 의존성) tác động (effect / 효과). “giá trị (value / 값) thấp hơn plan” là tín hiệu (signal / 신호) để reassess, không tự động là lệnh terminate.

### Dạng thất bại (failure mode / 실패 모드)

PMO thất bại khi trở thành reporting bureaucracy mà không cải thiện quyết định (decision / 결정) chất lượng (quality / 품질). Portfolio thất bại khi chỉ rank dự án (project / 프로젝트) một lần đầu năm rồi bỏ qua phụ thuộc (dependency / 의존성)/sức chứa (capacity / 용량)/thay đổi (change / 변경) trong thực thi (execution / 실행). dự án (project / 프로젝트) manager thất bại khi cục bộ (local / 로컬) success chỉ số (metric / 지표) khiến system-level mục tiêu (objective / 목표) xấu đi.

Trường hợp (case / 사례) này nối [Governance & Business Environment](./09_governance_compliance_and_business_environment.md), [Stakeholders](./03_stakeholders_communication_and_knowledge.md), [Schedule & Flow](./05_schedule_estimation_and_flow.md), [Risk](./08_risk_uncertainty_issues_and_decisions.md) và [Measurement](./11_measurement_status_closure_and_continuous_improvement.md).

> **Nối mạch:** **Trường hợp (case / 사례) F — Portfolio/PMO: nhiều initiative cùng tranh một thay đổi (change / 변경) sức chứa (capacity / 용량)** nêu quy tắc; **Cross-case synthesis: bất biến (invariant / 불변식) nào giữ nguyên, variable nào làm quyết định (decision / 결정) đổi** thử quy tắc trong tình huống, rồi **Cross-case synthesis: bottleneck di chuyển** mở rộng hệ quả.

## Cross-case synthesis: bất biến (invariant / 불변식) nào giữ nguyên, variable nào làm quyết định (decision / 결정) đổi

Trường hợp (case / 사례) khác nhau về lĩnh vực (domain / 도메인) nhưng có một số bất biến (invariant / 불변식). Thứ nhất, mục tiêu (objective / 목표) phải được giữ tách khỏi solution. DR site tồn tại để tạo resilience, mobile sản phẩm (product / 제품) để tạo customer/nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과), AI để giảm handling mà không tăng harm. Khi solution trở thành mục tiêu (objective / 목표), cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화) bắt đầu.

Thứ hai, bằng chứng (evidence / 증거) phải đi trước irreversible commitment khi thông tin (information / 정보) còn yếu. Trong trường hợp (case / 사례) A, vật lý (physical / 물리적) procurement cần bằng chứng (evidence / 증거)/plan đủ trước thứ tự (order / 순서) lớn. trường hợp (case / 사례) B dùng prototype/experiment. trường hợp (case / 사례) C kiểm thử (test / 테스트) API và representative documents sớm. trường hợp (case / 사례) D reconstruct trạng thái (state / 상태) trước khôi phục (recovery / 복구) commitment. Cơ chế khác nhau nhưng bất biến (invariant / 불변식) là thông tin (information / 정보) chất lượng (quality / 품질) phải tương xứng irreversibility.

Thứ ba, authority phải match consequence. sản phẩm (product / 제품) nhóm (team / 팀) có thể reorder backlog nhưng không tự waive regulation. PM có thể facilitate vendor khôi phục (recovery / 복구) nhưng không tự quyết legal claim ngoài authority. Portfolio xung đột (conflict / 충돌) không thể được giải bằng từng PM tự tối ưu.

Thứ tư, chuyển tiếp (transition / 전이) không phải phụ lục. Mọi trường hợp (case / 사례) đều chỉ tạo giá trị (value / 값) khi quyền sở hữu (ownership / 소유권) sau dự án (project / 프로젝트) tồn tại: DR operations, sản phẩm (product / 제품) nhóm (team / 팀), bank hỗ trợ (support / 지원), ERP nghiệp vụ (business / 비즈니스) thao tác (operation / 연산), claim assessor workflow hoặc portfolio benefit đơn vị sở hữu (owner / 오너).

Nhưng nhiều variable làm next hành động (action / 동작) đổi mạnh. ràng buộc (constraint / 제약조건) nguồn (source / 소스) là một variable: legal deadline khác thị trường (market / 시장) mục tiêu (target / 대상). Delivery chế độ (mode / 모드) là một variable: predictive baseline thay đổi (change / 변경) khác backlog reprioritization. Harm velocity là một variable: active privacy sự cố (incident / 인시던트) cần contain sớm hơn normal phân tích (analysis / 분석). Reversibility là một variable: prototype dễ quay lui (rollback / 롤백) khác long-term đặc tả hợp đồng (contract / 계약). thông tin (information / 정보) gap là một variable: vendor breach đã có bằng chứng (evidence / 증거) khác suspicion chưa verified.

Mô hình tư duy (mental model / 사고 모델) tốt giữ bất biến (invariant / 불변식) nhưng thay hành động (action / 동작) theo variable. Đây là cách tránh slogan kiểu “luôn assess trước”, “luôn nhóm (team / 팀) first” hoặc “luôn follow thay đổi (change / 변경) điều khiển (control / 제어)”.

> **Nối mạch:** **Cross-case synthesis: bất biến (invariant / 불변식) nào giữ nguyên, variable nào làm quyết định (decision / 결정) đổi** nêu quy tắc; **Cross-case synthesis: bottleneck di chuyển** thử quy tắc trong tình huống, rồi **Cross-case synthesis: rủi ro (risk / 위험) chuyển hình khi dự án (project / 프로젝트) tiến triển** mở rộng hệ quả.

## Cross-case synthesis: bottleneck di chuyển

Một dự án (project / 프로젝트) không có một bottleneck cố định suốt vòng đời (lifecycle / 생명주기). trường hợp (case / 사례) A có thể bắt đầu với permit/procurement bottleneck rồi chuyển sang tích hợp (integration / 통합)/testing. trường hợp (case / 사례) B có thể từ học tập (learning / 학습) bottleneck chuyển sang kỹ thuật (engineering / 엔지니어링) thông lượng (throughput / 처리량) rồi adoption. trường hợp (case / 사례) C có thể từ vendor API sang UAT cửa sổ (window / 윈도우) rồi operational readiness.

Khi nhóm (team / 팀) tiếp tục optimize bottleneck cũ, effort mất leverage. Thêm nhà phát triển (developer / 개발자) khi approval hàng đợi (queue / 큐) là ràng buộc (constraint / 제약조건) không giúp. Tăng huấn luyện (training / 학습) khi permission chưa mở không giúp. Tăng kiểm thử (test / 테스트) khi yêu cầu (requirement / 요구사항) ambiguity tiếp tục tạo defect chỉ xử lý symptom.

Vì vậy mỗi status cycle nên hỏi: ràng buộc (constraint / 제약조건) hiện tại của hệ thống (system / 시스템) là gì, bằng chứng (evidence / 증거) nào chứng minh, và nếu ràng buộc (constraint / 제약조건) được giải thì ràng buộc (constraint / 제약조건) kế tiếp có khả năng ở đâu?

> **Nối mạch:** **Cross-case synthesis: bottleneck di chuyển** nêu quy tắc; **Cross-case synthesis: rủi ro (risk / 위험) chuyển hình khi dự án (project / 프로젝트) tiến triển** thử quy tắc trong tình huống, rồi **Cross-case synthesis: cục bộ (local / 로컬) success có thể tạo toàn cục (global / 전역) thất bại (failure / 실패)** mở rộng hệ quả.

## Cross-case synthesis: rủi ro (risk / 위험) chuyển hình khi dự án (project / 프로젝트) tiến triển

Bất định (uncertainty / 불확실성) ở discovery có thể là ambiguity; sau thiết kế (design / 설계) nó thành thực thi (execution / 실행) variability; gần bản phát hành (release / 릴리스) nó thành readiness/operational rủi ro (risk / 위험). Một rủi ro (risk / 위험) item không nên sống nguyên wording suốt 12 tháng nếu underlying trạng thái (state / 상태) đã đổi.

Trường hợp (case / 사례) E minh họa rõ: ban đầu bất định (uncertainty / 불확실성) là mô hình (model / 모델) chất lượng (quality / 품질); pilot xong, rủi ro (risk / 위험) chuyển sang human sức chứa (capacity / 용량), vendor thay đổi (change / 변경) và môi trường vận hành (production / 운영 환경) drift. trường hợp (case / 사례) D: ban đầu dashboard bất định (uncertainty / 불확실성); sau reconstruct trạng thái (state / 상태), rủi ro (risk / 위험) có thể chuyển thành commercial/phạm vi (scope / 범위)/khôi phục (recovery / 복구) thực thi (execution / 실행).

Rủi ro (risk / 위험) management tốt theo chuyển tiếp trạng thái (state transition / 상태 전이), không chỉ giữ register lịch sử (history / 이력).

> **Nối mạch:** **Cross-case synthesis: rủi ro (risk / 위험) chuyển hình khi dự án (project / 프로젝트) tiến triển** nêu quy tắc; **Cross-case synthesis: cục bộ (local / 로컬) success có thể tạo toàn cục (global / 전역) thất bại (failure / 실패)** thử quy tắc trong tình huống, rồi **Cross-case synthesis: quyết định (decision / 결정) chất lượng (quality / 품질) và kết quả (outcome / 결과) chất lượng (quality / 품질)** mở rộng hệ quả.

## Cross-case synthesis: cục bộ (local / 로컬) success có thể tạo toàn cục (global / 전역) thất bại (failure / 실패)

Trường hợp (case / 사례) A: facility complete nhưng failover unusable. trường hợp (case / 사례) B: velocity cao nhưng retention không đổi. trường hợp (case / 사례) C: sprint complete nhưng UAT chưa accepted. trường hợp (case / 사례) D: mô-đun (module / 모듈) on schedule nhưng program nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) không viable. trường hợp (case / 사례) F: từng dự án (project / 프로젝트) green nhưng dùng chung (shared / 공유) sức chứa (capacity / 용량) impossible.

Đây là mẫu (pattern / 패턴) quan trọng nhất của hệ thống (system / 시스템) thinking: chỉ số (metric / 지표)/cục bộ (local / 로컬) deliverable chỉ là proxy. Mỗi thời gian (time / 시간) bạn thấy một cục bộ (local / 로컬) success, hỏi downstream kết quả (outcome / 결과) và dùng chung (shared / 공유) ràng buộc (constraint / 제약조건) có còn healthy không.

> **Nối mạch:** **Cross-case synthesis: cục bộ (local / 로컬) success có thể tạo toàn cục (global / 전역) thất bại (failure / 실패)** nêu quy tắc; **Cross-case synthesis: quyết định (decision / 결정) chất lượng (quality / 품질) và kết quả (outcome / 결과) chất lượng (quality / 품질)** thử quy tắc trong tình huống, rồi **Cách dùng trường hợp (case / 사례) study để tự luyện** mở rộng hệ quả.

## Cross-case synthesis: quyết định (decision / 결정) chất lượng (quality / 품질) và kết quả (outcome / 결과) chất lượng (quality / 품질)

Một quyết định (decision / 결정) đúng vẫn có thể kết quả (outcome / 결과) xấu vì bất định (uncertainty / 불확실성). trường hợp (case / 사례) B có experiment hợp lý nhưng người dùng (user / 사용자) vẫn không thích tính năng (feature / 기능). trường hợp (case / 사례) A chọn supplier tốt nhưng geopolitical disruption vẫn xảy ra. trường hợp (case / 사례) E rollout segment low-risk hợp lý nhưng vendor sự cố (incident / 인시던트) vẫn có thể xảy ra.

Rà soát (review / 검토) sau kết quả (outcome / 결과) phải hỏi thông tin (information / 정보) available lúc quyết định (decision / 결정), giả định (assumption / 가정), authority, option và threshold—not hindsight “đã thất bại thì quyết định (decision / 결정) sai”. Ngược lại, may mắn không chứng minh tiến trình (process / 프로세스) tốt.

Trường hợp (case / 사례) study nên được dùng để luyện chất lượng (quality / 품질) của lập luận (reasoning / 추론), không đo khả năng đoán kết quả.

> **Nối mạch:** **Cross-case synthesis: quyết định (decision / 결정) chất lượng (quality / 품질) và kết quả (outcome / 결과) chất lượng (quality / 품질)** nêu quy tắc; **Cách dùng trường hợp (case / 사례) study để tự luyện** thử quy tắc trong tình huống, rồi **Coverage của các trường hợp (case / 사례)** mở rộng hệ quả.

## Cách dùng trường hợp (case / 사례) study để tự luyện

### Pass 1 — Không mở chapter khác

Đọc ngữ cảnh (context / 맥락) rồi tự viết ngắn: mục tiêu (objective / 목표), delivery chế độ (mode / 모드), strongest ràng buộc (constraint / 제약조건), hiện tại (current / 현재) tín hiệu (signal / 신호), authority, bằng chứng (evidence / 증거) còn thiếu và next hành động (action / 동작). Mục tiêu là kiểm thử (test / 테스트) mô hình tư duy (mental model / 사고 모델) đang có, không phải tra cứu.

### Pass 2 — dấu vết (trace / 추적) lập luận (reasoning / 추론) về chuẩn gốc (canonical / 정본) chapter

Sau khi trả lời, map mỗi quyết định (decision / 결정) về cơ chế (mechanism / 메커니즘). Nếu không giải thích được vì sao vendor issue cần đặc tả hợp đồng (contract / 계약) bằng chứng (evidence / 증거), quay lại [Quality, Resources & Procurement](./07_quality_resources_and_procurement.md). Nếu không giải thích được vì sao dự án (project / 프로젝트) green nhưng portfolio vẫn unhealthy, quay lại [Governance](./09_governance_compliance_and_business_environment.md).

Không đọc lại toàn bộ thư viện (library / 라이브러리). Chỉ sửa đúng conceptual gap.

### Pass 3 — Counterfactual

Đổi một biến và quan sát quyết định (decision / 결정) có đổi không. Với trường hợp (case / 사례) C, giả sử vendor giao diện (interface / 인터페이스) ổn định nhưng deadline không còn cố định; hoặc accuracy issue chỉ ảnh hưởng 0.01% người dùng (user / 사용자); hoặc regulator yêu cầu (requirement / 요구사항) trở thành recommendation. Với trường hợp (case / 사례) D, giả sử dự án (project / 프로젝트) mới chi 10% thay vì 70%; sunk chi phí (cost / 비용) không nên thay future-value quyết định (decision / 결정), nhưng option khôi phục (recovery / 복구) và termination chi phí (cost / 비용) có thể khác.

Với trường hợp (case / 사례) F, đổi regulatory dự án (project / 프로젝트) thành optional efficiency initiative. Priority có thể đổi vì ràng buộc (constraint / 제약조건) nguồn (source / 소스) đổi. Hoặc tăng tích hợp (integration / 통합) sức chứa (capacity / 용량) từ 8 lên 20 người nhưng giữ huấn luyện (training / 학습) saturation; bottleneck chuyển từ technical sức chứa (capacity / 용량) sang adoption sức chứa (capacity / 용량).

### Pass 4 — sản phẩm tạo ra (artifact / 산출물)/dữ liệu (data / 데이터) injection

Tự thêm một sản phẩm tạo ra (artifact / 산출물): rủi ro (risk / 위험) register, EVM dashboard, defect trend, đặc tả hợp đồng (contract / 계약) clause, stakeholder engagement assessment hoặc benefits dashboard. Hỏi bằng chứng (evidence / 증거) mới có làm trạng thái (state / 상태) mô hình (model / 모델) hoặc next hành động (action / 동작) thay đổi không.

Ví dụ thêm vào trường hợp (case / 사례) D một dashboard có `CPI = 0.78`, `SPI = 0.93` nhưng dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) readiness chỉ 35%. Nếu chỉ focus EVM, bạn có thể bỏ readiness driver lớn hơn. Thêm vào trường hợp (case / 사례) F một portfolio heatmap cho thấy ba dự án (project / 프로젝트) cùng phụ thuộc một vendor; systemic rủi ro (risk / 위험) trở nên visible hơn.

### Pass 5 — Explain the rejected alternative

Đừng chỉ nói option nào tốt hơn. Giải thích vì sao alternative hấp dẫn nhưng sai trạng thái (state / 상태), authority, chuỗi (sequence / 시퀀스) hoặc hệ thống (system / 시스템) tác động (effect / 효과). Kỹ năng này trực tiếp giúp loại distractor trong exam.

Một answer có chất lượng thường có dạng:

```text
Signal → Impact → Information → Authority → Option → Next action → Evidence cần theo dõi
```

Nếu lập luận (reasoning / 추론) tự điều chỉnh theo giá trị (value / 값)/rủi ro (risk / 위험)/authority thay vì lặp câu thuộc lòng, mô hình tư duy (mental model / 사고 모델) đã hoạt động.

### Pass 6 — thay đổi (change / 변경) the bottleneck

Sau khi chọn next hành động (action / 동작), giả sử hành động (action / 동작) thành công rồi hỏi bottleneck kế tiếp là gì. Đây là cách tránh giải một vấn đề rồi tiếp tục dùng cùng intervention khi hệ thống (system / 시스템) đã chuyển trạng thái (state / 상태).

Ví dụ trường hợp (case / 사례) C fix vendor hết thời gian chờ (timeout / 타임아웃) xong nhưng UAT cửa sổ (window / 윈도우) vẫn là monthly bên ngoài (external / 외부) ràng buộc (constraint / 제약조건). trường hợp (case / 사례) F tăng tích hợp (integration / 통합) sức chứa (capacity / 용량) nhưng branch huấn luyện (training / 학습) vẫn saturated. quyết định (decision / 결정) chất lượng (quality / 품질) phải theo hệ thống (system / 시스템) trạng thái (state / 상태) mới.

### Pass 7 — Separate quyết định (decision / 결정) chất lượng (quality / 품질) from kết quả (outcome / 결과)

Tự tạo hai ending: một ending tốt sau quyết định (decision / 결정) xấu nhờ may mắn và một ending xấu sau quyết định (decision / 결정) hợp lý do tail sự kiện (event / 이벤트). Sau đó đánh giá tiến trình (process / 프로세스) bằng bằng chứng (evidence / 증거) available tại quyết định (decision / 결정) thời gian (time / 시간).

Bài tập này chống hindsight độ lệch (bias / 편향) và giúp lập luận (reasoning / 추론) giống dự án (project / 프로젝트) manager hơn người kể chuyện sau sự kiện.

> **Nối mạch:** **Cách dùng trường hợp (case / 사례) study để tự luyện** nêu quy tắc; **Coverage của các trường hợp (case / 사례)** thử quy tắc trong tình huống, rồi **Một micro-case về contractual claim** mở rộng hệ quả.

## Coverage của các trường hợp (case / 사례)

Trường hợp (case / 사례) A chủ yếu ép bạn nối predictive planning, procurement, compliance, schedule, chất lượng (quality / 품질) và closure. trường hợp (case / 사례) B nối adaptive học tập (learning / 학습), sản phẩm (product / 제품) giá trị (value / 값), luồng (flow / 흐름), chỉ số (metric / 지표) và quản trị (governance / 거버넌스). trường hợp (case / 사례) C tập trung hybrid giao diện (interface / 인터페이스), vendor, privacy, AI chất lượng (quality / 품질) và operational chuyển tiếp (transition / 전이). trường hợp (case / 사례) D luyện khôi phục (recovery / 복구), sunk chi phí (cost / 비용), rebaseline, thông tin (information / 정보) chất lượng (quality / 품질) và vendor xung đột (conflict / 충돌). trường hợp (case / 사례) E nối AI quản trị (governance / 거버넌스), human oversight, sustainability và benefit đo lường (measurement / 측정). trường hợp (case / 사례) F đưa lập luận (reasoning / 추론) lên program/portfolio mức (level / 수준) với dùng chung (shared / 공유) phụ thuộc (dependency / 의존성), PMO, sức chứa (capacity / 용량) và thay đổi (change / 변경) saturation.

Không trường hợp (case / 사례) nào chỉ thuộc một chapter. Đó chính là mục đích của tầng (layer / 계층) consolidation này.

> **Nối mạch:** **Coverage của các trường hợp (case / 사례)** nêu quy tắc; **Một micro-case về contractual claim** thử quy tắc trong tình huống, rồi **Cross-domain liên kết (connection / 연결)** mở rộng hệ quả.

## Một micro-case về contractual claim

Construction vendor báo delay 20 ngày và yêu cầu extension + compensation vì buyer thay thiết kế (design / 설계). Buyer cho rằng vendor vốn đã chậm 10 ngày trước thay đổi (change / 변경).

Không nên nhảy thẳng sang “approve claim” hoặc “reject claim”. Tách lập luận (reasoning / 추론) thành entitlement: đặc tả hợp đồng (contract / 계약)/thay đổi (change / 변경) có trao quyền không; causation: buyer thay đổi (change / 변경) thực sự gây bao nhiêu delay; concurrent delay: phần nào overlap với delay do vendor; quantum: thời gian (time / 시간)/chi phí (cost / 비용) relief nào có bằng chứng (evidence / 증거). Song song đó, dự án (project / 프로젝트) vẫn cần technical khôi phục (recovery / 복구) và forecast cập nhật (update / 업데이트); dispute tiến trình (process / 프로세스) không nên làm khôi phục (recovery / 복구) đứng yên.

Micro-case này giúp nối đặc tả hợp đồng (contract / 계약) mechanics trong [07](./07_quality_resources_and_procurement.md) với schedule bằng chứng (evidence / 증거) trong [05](./05_schedule_estimation_and_flow.md) và quản trị (governance / 거버넌스) trong [09](./09_governance_compliance_and_business_environment.md).

> **Nối mạch:** **Một micro-case về contractual claim** nêu quy tắc; **Cross-domain liên kết (connection / 연결)** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Cross-domain liên kết (connection / 연결)

Software-specific yêu cầu (requirement / 요구사항), kiểm thử (test / 테스트) và môi trường vận hành (production / 운영 환경) mechanics nên đọc tiếp ở [Software Engineering](../computer_science/09_software_engineering/README.md). PMP giữ focus ở hệ thống (system / 시스템) of decisions quanh delivery chứ không duplicate hiện thực (implementation / 구현) detail.

AI hiện thực (implementation / 구현) detail không được duplicate trong PMP; chapter [AI, sustainability và bối cảnh dự án hiện đại](./12_ai_sustainability_and_modern_project_context.md) chỉ giữ quản trị (governance / 거버넌스)/giá trị (value / 값)/rủi ro (risk / 위험) ranh giới (boundary / 경계) cần cho dự án (project / 프로젝트) lập luận (reasoning / 추론).

Finance chuyên sâu như corporate valuation/portfolio lý thuyết (theory / 이론) tiếp tục thuộc [Investing Knowledge Library](../investing/README.md); PMP chỉ lấy phần cần cho dự án (project / 프로젝트)/portfolio quyết định (decision / 결정).

> **Nối mạch:** **Cross-domain liên kết** gom các ràng buộc và trade-off của từng miền; **Mô hình tư duy** biến chúng thành tiêu chí chọn predictive, adaptive hoặc hybrid trong case end-to-end.

## Mô hình tư duy (mental model / 사고 모델)

> Một dự án thật không phát sinh “câu hỏi chất lượng (quality / 품질)” hoặc “câu hỏi stakeholder” riêng rẽ. Một tín hiệu (signal / 신호) thường lan qua nhiều lĩnh vực (domain / 도메인); kỹ năng PMP là giữ một trạng thái (state / 상태) mô hình (model / 모델) đủ đúng, nhận ra bất biến (invariant / 불변식) và ngữ cảnh (context / 맥락) variable, theo dõi bottleneck/rủi ro (risk / 위험) khi chúng chuyển hình, rồi chọn next hành động (action / 동작) phù hợp mà không tối ưu cục bộ một chỉ số (metric / 지표) hay một dự án (project / 프로젝트).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
