# 09 — quản trị (governance / 거버넌스), compliance và nghiệp vụ (business / 비즈니스) môi trường (environment / 환경)

> **Mạch đọc:** Đặt **09 — quản trị (governance / 거버넌스), compliance và nghiệp vụ (business / 비즈니스) môi trường (environment / 환경)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **quản trị (governance / 거버넌스) là hệ thống quyền quyết định** sang **quản trị (governance / 거버넌스) là quyết định (decision / 결정) kiến trúc (architecture / 아키텍처), không chỉ committee**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## Quản trị (governance / 거버넌스) là hệ thống quyền quyết định

Quản trị (governance / 거버넌스) xác định quyết định (decision / 결정) rights, accountability, chính sách (policy / 정책), reporting, điều khiển (control / 제어) và escalation. Nó trả lời: ai có quyền phê duyệt điều gì, threshold nào cần escalate, bằng chứng (evidence / 증거) nào phải có, và ai chịu trách nhiệm cho kết quả (outcome / 결과).

Management vận hành bên trong ranh giới (boundary / 경계) đó. quản trị (governance / 거버넌스) yếu làm dự án (project / 프로젝트) hoặc tê liệt vì mọi thứ phải xin phép, hoặc nguy hiểm vì không ai rõ authority.

Quản trị (governance / 거버넌스) tốt không cố quyết mọi việc ở cấp cao nhất. Nó phân loại quyết định (decision / 결정) theo impact, reversibility và rủi ro (risk / 위험), rồi đặt quyền quyết định ở mức (level / 수준) thấp nhất vẫn bảo vệ được organization.

## Quản trị (governance / 거버넌스) là quyết định (decision / 결정) kiến trúc (architecture / 아키텍처), không chỉ committee

Một quản trị (governance / 거버넌스) operating mô hình (model / 모델) cần ít nhất quyết định (decision / 결정) kiểu (type / 타입), quyết định (decision / 결정) đơn vị sở hữu (owner / 오너), đầu vào (input / 입력)/bằng chứng (evidence / 증거), threshold, cadence, escalation đường dẫn (path / 경로) và bản ghi (record / 레코드). Committee chỉ là một hiện thực (implementation / 구현) option.

Nếu quyết định (decision / 결정) đơn vị sở hữu (owner / 오너) rõ nhưng bằng chứng (evidence / 증거) tới quá chậm, quản trị (governance / 거버넌스) vẫn thất bại (fail / 실패). Nếu meeting xảy ra đúng lịch nhưng không ai có authority lần ghi nhận (commit / 커밋), quản trị (governance / 거버넌스) chỉ tạo ceremony. Nếu nhóm (team / 팀) có authority nhưng threshold không rõ, quyết định (decision / 결정) dễ bị escalated quá mức hoặc giữ quá lâu.

Một thiết kế (design / 설계) tốt cố tối thiểu hóa tổng chi phí (cost / 비용) gồm rủi ro (risk / 위험) của quyết định (decision / 결정) sai và độ trễ (latency / 지연 시간)/overhead của quyết định (decision / 결정) tiến trình (process / 프로세스). quản trị (governance / 거버넌스) quá nhẹ tăng uncontrolled rủi ro (risk / 위험); quản trị (governance / 거버넌스) quá nặng tạo hàng đợi (queue / 큐), workaround và shadow quyết định (decision / 결정).

## Quản trị (governance / 거버넌스) khác bureaucracy

Một điều khiển (control / 제어) chỉ có ý nghĩa khi nó giảm rủi ro (risk / 위험) hoặc tạo thông tin (information / 정보) cần cho quyết định (decision / 결정). Stage gate có thể phù hợp trước khi bỏ vốn lớn hoặc go-live regulated hệ thống (system / 시스템). Nhưng nếu mỗi thay đổi (change / 변경) nhỏ đều cần board meeting hai tuần một lần, quản trị (governance / 거버넌스) tạo hàng đợi (queue / 큐) và làm phản hồi (response / 응답) chậm.

Tailoring quản trị (governance / 거버넌스) nghĩa giữ điều khiển (control / 제어) mục tiêu (objective / 목표) nhưng điều chỉnh cơ chế (mechanism / 메커니즘). Có thể tự động hóa bằng chứng (evidence / 증거), đặt threshold theo rủi ro (risk / 위험) hoặc delegate approval cho reversible quyết định (decision / 결정).

Một cách kiểm tra (audit / 감사) quản trị (governance / 거버넌스) đơn giản là hỏi mỗi điều khiển (control / 제어) đang bảo vệ dạng thất bại (failure mode / 실패 모드) nào. Nếu không ai trả lời được, điều khiển (control / 제어) có thể đã biến thành ritual. Ngược lại, bỏ một điều khiển (control / 제어) mà không hiểu dạng thất bại (failure mode / 실패 모드) phía sau có thể tạo rủi ro (risk / 위험) lớn hơn overhead đã tiết kiệm.

## Quản trị (governance / 거버넌스) debt

Quản trị (governance / 거버넌스) debt xuất hiện khi temporary shortcut trong authority, approval hoặc bằng chứng (evidence / 증거) không được retire. Ví dụ emergency cho phép nhóm (team / 팀) deploy bằng verbal approval; nếu exception đó tiếp tục thành habit, organization mất traceability và ranh giới (boundary / 경계) chính thức.

Debt cũng xuất hiện khi chính sách (policy / 정책)/threshold không được cập nhật (update / 업데이트) dù operating ngữ cảnh (context / 맥락) đổi. nhóm (team / 팀) khi đó phải workaround quy tắc (rule / 규칙) outdated, làm shadow tiến trình (process / 프로세스) lớn dần.

Giống technical debt, quản trị (governance / 거버넌스) debt có thể hợp lý trong emergency nếu visible, đơn vị sở hữu (owner / 오너) rõ và repayment date có thật. Hidden permanent exception mới nguy hiểm.

## Quyết định (decision / 결정) hàng đợi (queue / 큐) và quản trị (governance / 거버넌스) độ trễ (latency / 지연 시간)

Mọi quản trị (governance / 거버넌스) body có sức chứa (capacity / 용량) hữu hạn. Nếu quá nhiều item phải chờ cùng một sponsor, architect hoặc committee, hàng đợi (queue / 큐) tạo độ trễ (latency / 지연 시간). độ trễ (latency / 지연 시간) có thể lớn hơn thời gian thực hiện công việc (work / 작업) sau approval.

Một hệ thống (system / 시스템) tốt theo dõi không chỉ số quyết định (decision / 결정) mà còn age của pending quyết định (decision / 결정), materiality và chi phí (cost / 비용) of delay. Delegation, standing guardrail hoặc asynchronous approval có thể giảm hàng đợi (queue / 큐) mà không bỏ điều khiển (control / 제어) mục tiêu (objective / 목표).

Nếu nhóm (team / 팀) liên tục bắt đầu công việc (work / 작업) “at rủi ro (risk / 위험)” vì approval đến quá chậm, vấn đề không chỉ là discipline của nhóm (team / 팀); quản trị (governance / 거버넌스) thiết kế (design / 설계) có thể đang không đáp ứng cadence của delivery hệ thống (system / 시스템).

## Sponsor, dự án (project / 프로젝트) manager và quản trị (governance / 거버넌스) body

Sponsor thường sở hữu nghiệp vụ (business / 비즈니스) justification, bảo trợ dự án (project / 프로젝트) ở cấp tổ chức và hỗ trợ quyết định (decision / 결정) vượt authority của dự án (project / 프로젝트) manager. dự án (project / 프로젝트) manager điều phối delivery trong ranh giới (boundary / 경계) được trao. quản trị (governance / 거버넌스) body như steering committee hoặc thay đổi (change / 변경) điều khiển (control / 제어) board xử lý quyết định (decision / 결정) theo threshold đã định.

Điểm quan trọng không phải title mà là quyết định (decision / 결정) right. Nếu sponsor chịu accountability về nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과) nhưng không có thời gian hoặc authority để giải quyết escalated issue, dự án (project / 프로젝트) đang có quản trị (governance / 거버넌스) gap.

Một escalation tốt nên nêu quyết định (decision / 결정) cần đưa ra, option, impact, recommendation và deadline. Chỉ gửi “có vấn đề” làm quản trị (governance / 거버넌스) body phải tự tái tạo toàn bộ phân tích (analysis / 분석).

## Sponsor attention là tài nguyên (resource / 자원) khan hiếm

Sponsor không thể tham gia mọi detail. dự án (project / 프로젝트) manager cần bảo vệ sponsor attention bằng cách escalate material quyết định (decision / 결정), không phải mọi status issue.

Escalation packet tốt giảm cognitive tải (load / 로드): trạng thái hiện tại (current state / 현재 상태), why it matters, options, recommendation, deadline và consequence nếu không quyết. Nếu sponsor phải đọc 40 trang để hiểu câu hỏi, độ trễ (latency / 지연 시간) dễ tăng.

Ngược lại, PM che bad news để “không làm phiền sponsor” có thể làm sponsor chỉ biết bài toán (problem / 문제) khi option đã biến mất. Attention management không phải thông tin (information / 정보) suppression.

## PMO và organizational quản trị (governance / 거버넌스)

Dự án (project / 프로젝트) Management Office (PMO / 프로젝트 관리 조직) có thể cung cấp tiêu chuẩn (standard / 표준), assurance, portfolio alignment, reporting hoặc trực tiếp quản lý dự án (project / 프로젝트) tùy organization. PMO không mặc định là bureaucracy; giá trị của nó nằm ở việc giảm duplicate học tập (learning / 학습), chuẩn hóa điều khiển (control / 제어) cần thiết và tạo visibility xuyên dự án (project / 프로젝트).

PMO yếu có thể tập trung vào template compliance hơn kết quả (outcome / 결과). PMO mạnh giúp organization phân biệt variance bình thường với systemic rủi ro (risk / 위험), dùng historical dữ liệu (data / 데이터) tốt hơn và hỗ trợ dự án (project / 프로젝트) manager khi issue vượt ranh giới (boundary / 경계) một dự án (project / 프로젝트).

## PMO operating mô hình (model / 모델): hỗ trợ (support / 지원), điều khiển (control / 제어) hay delivery

Không có một PMO duy nhất cho mọi organization. Supportive PMO tập trung coaching, template, community of practice và dữ liệu (data / 데이터). Controlling PMO đặt tiêu chuẩn (standard / 표준), assurance, gate và compliance. Directive PMO có thể trực tiếp sở hữu hoặc điều hành dự án (project / 프로젝트)/program.

Ba chế độ (mode / 모드) này không phải maturity ladder. Một regulated bank có thể cần điều khiển (control / 제어) mạnh; một sản phẩm (product / 제품) organization nhỏ có thể cần enablement nhiều hơn. Vấn đề xuất hiện khi authority thực tế và expectation không khớp: PMO bị yêu cầu chịu accountability nhưng không có quyết định (decision / 결정) right, hoặc có quyền gate nhưng không chịu consequence của quyết định (decision / 결정) độ trễ (latency / 지연 시간).

PMO nên đo giá trị (value / 값) của mình bằng organizational outcomes như quyết định (decision / 결정) speed, forecast chất lượng (quality / 품질), delivery predictability, reuse of học tập (learning / 학습) và systemic rủi ro (risk / 위험) visibility hơn là số template được điền đúng hạn.

## Assurance cần đủ độc lập để challenge

Dự án (project / 프로젝트) nhóm (team / 팀) có incentive tự nhiên muốn chứng minh mình on nhánh học (track / 트랙). Vì vậy một số quyết định (decision / 결정) high-consequence cần independent challenge hoặc assurance: bảo mật (security / 보안) rà soát (review / 검토), kiểm tra (audit / 감사), kiến trúc (architecture / 아키텍처) rà soát (review / 검토), commercial rà soát (review / 검토) hoặc health check.

Independence không có nghĩa reviewer không hiểu ngữ cảnh (context / 맥락). Reviewer quá xa reality dễ tạo checkbox điều khiển (control / 제어); reviewer quá embedded có thể mất objectivity. quản trị (governance / 거버넌스) phải cân challenge chất lượng (quality / 품질) với delivery ngữ cảnh (context / 맥락).

Assurance tốt hỏi bằng chứng (evidence / 증거) và giả định (assumption / 가정), không chỉ “đã điền template chưa?”.

## Dự án (project / 프로젝트), program và portfolio nối nhau qua phụ thuộc (dependency / 의존성) và capital allocation

Dự án (project / 프로젝트) tạo một thay đổi (change / 변경) cụ thể. Program phối hợp nhiều dự án (project / 프로젝트)/thao tác (operation / 연산) liên quan để tạo benefit mà từng dự án (project / 프로젝트) riêng lẻ khó tối ưu. Portfolio chọn và cân investment để phù hợp chiến lược (strategy / 전략), sức chứa (capacity / 용량) và rủi ro (risk / 위험) appetite.

Ranh giới (boundary / 경계) này quan trọng vì một dự án (project / 프로젝트) có thể “xanh” nhưng program thất bại. Ví dụ app mobile hoàn thành đúng plan nhưng định danh (identity / 식별자) nền tảng (platform / 플랫폼) trong dự án (project / 프로젝트) khác chưa sẵn sàng, nên benefit toàn program chưa xuất hiện. cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화) ở từng dự án (project / 프로젝트) không đảm bảo hệ thống (system / 시스템) kết quả (outcome / 결과).

Portfolio cũng có thể dừng một dự án (project / 프로젝트) khỏe nếu capital cần chuyển sang opportunity có strategic giá trị (value / 값) cao hơn. Với dự án (project / 프로젝트) manager, điều này có thể khó chấp nhận nếu chỉ nhìn delivery metrics. quản trị (governance / 거버넌스) cấp portfolio hỏi một câu khác: đây còn là nơi tốt nhất để đầu tư nguồn lực khan hiếm không?

## Portfolio WIP và sức chứa (capacity / 용량)

Portfolio có thể overcommit giống nhóm (team / 팀). Nếu organization khởi động 30 initiative nhưng chỉ có sức chứa (capacity / 용량) thực cho 15, mỗi dự án (project / 프로젝트) nhận tài nguyên (resource / 자원) không ổn định, quyết định (decision / 결정) body quá tải và thay đổi (change / 변경) saturation tăng.

Portfolio WIP cao làm cycle thời gian (time / 시간) của strategic thay đổi (change / 변경) dài hơn. Giảm số initiative active có thể tăng thông lượng (throughput / 처리량) hoàn thành dù nhìn bề ngoài organization “làm ít thứ hơn”. Đây là same luồng (flow / 흐름) lô-gic (logic / 논리) ở [Schedule & Flow](./05_schedule_estimation_and_flow.md), nhưng áp dụng ở cấp investment.

Portfolio quản trị (governance / 거버넌스) vì vậy không chỉ chọn dự án (project / 프로젝트) tốt; nó quyết định bao nhiêu công việc (work / 작업) có thể được active đồng thời mà hệ thống (system / 시스템) vẫn giữ focus và absorption sức chứa (capacity / 용량).

## Incremental funding và progressive commitment

Một initiative bất định (uncertainty / 불확실성) cao không nhất thiết cần full funding ngay từ đầu. quản trị (governance / 거버넌스) có thể cấp discovery tranche, sau đó tăng commitment khi bằng chứng (evidence / 증거) tốt hơn.

Incremental funding tạo option stop/pivot trước irreversible spend lớn. Nhưng nếu mỗi tranche approval quá nhỏ và chậm, giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) có thể phá luồng (flow / 흐름). Progressive commitment cần threshold phù hợp với kích thước (size / 크기)/rủi ro (risk / 위험), không micro-approve mọi expense.

Đây là portfolio equivalent của stage-gate/real-options thinking ở chapter vòng đời (lifecycle / 생명주기) và rủi ro (risk / 위험).

## Cross-project phụ thuộc (dependency / 의존성) và dùng chung (shared / 공유) ràng buộc (constraint / 제약조건)

Program/portfolio quản trị (governance / 거버넌스) cần thấy phụ thuộc (dependency / 의존성) xuyên dự án (project / 프로젝트): dùng chung (shared / 공유) vendor, môi trường (environment / 환경), dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션), regulatory approval, specialist hoặc nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너). Nếu mỗi dự án (project / 프로젝트) forecast độc lập, cùng một tài nguyên (resource / 자원) có thể bị allocate 200% trên giấy.

Phụ thuộc (dependency / 의존성) cần đơn vị sở hữu (owner / 오너), required-by date, supplying dự án (project / 프로젝트), consuming dự án (project / 프로젝트) và escalation đường dẫn (path / 경로). Một phụ thuộc (dependency / 의존성) “được biết” nhưng không có quyết định (decision / 결정) cơ chế (mechanism / 메커니즘) vẫn là unmanaged rủi ro (risk / 위험).

Dùng chung (shared / 공유) ràng buộc (constraint / 제약조건) cũng làm rủi ro (risk / 위험) correlated. Năm dự án (project / 프로젝트) dùng cùng vendor không phải năm exposure độc lập. Đây là điểm nối với [Risk, uncertainty và decision](./08_risk_uncertainty_issues_and_decisions.md).

## Portfolio quản trị (governance / 거버넌스) và kill/pause/pivot quyết định (decision / 결정)

Quản trị (governance / 거버넌스) trưởng thành không chỉ approve start; nó cũng có khả năng pause, pivot hoặc terminate khi bằng chứng (evidence / 증거) thay đổi. Nếu mọi dự án (project / 프로젝트) chỉ được phép “continue”, portfolio rà soát (review / 검토) trở thành reporting ritual.

Quyết định (decision / 결정) nên xem sunk chi phí (cost / 비용) là lịch sử (history / 이력), không phải lý do tiếp tục. Các câu hỏi quan trọng hơn là remaining investment, expected future giá trị (value / 값), strategic alignment, opportunity chi phí (cost / 비용), rủi ro (risk / 위험) và reversibility.

Một dự án (project / 프로젝트) bị terminate không nhất thiết là thất bại (failure / 실패) của PM. Có thể đó là bằng chứng (evidence / 증거) rằng quản trị (governance / 거버넌스) học sớm trước khi đốt thêm capital.

## Strategic alignment drift

Dự án (project / 프로젝트) có thể vẫn đúng charter ban đầu nhưng chiến lược (strategy / 전략) đã đổi. Merger, regulation, thị trường (market / 시장) shock hoặc new nền tảng (platform / 플랫폼) có thể làm initiative ít giá trị (value / 값) hơn mà delivery metrics không phản ánh.

Alignment vì vậy cần được reassess ở material trigger, không chỉ annual planning. Nếu dự án (project / 프로젝트) purpose không còn nối chiến lược (strategy / 전략), “on phạm vi (scope / 범위)/on ngân sách (budget / 예산)” không phải lý do đủ để tiếp tục.

Strategic drift cũng có thể theo hướng ngược: một dự án (project / 프로젝트) từng optional trở thành trọng yếu (critical / 중요) vì regulation hoặc competitor sự kiện (event / 이벤트). quản trị (governance / 거버넌스) cần có ability reprioritize, không khóa toàn portfolio theo ranking cũ.

## Compliance là ràng buộc (constraint / 제약조건) không thể “sự đánh đổi (trade-off / 트레이드오프) tùy ý”

Tuân thủ (compliance / 컴플라이언스) đến từ law, regulation, industry tiêu chuẩn (standard / 표준), đặc tả hợp đồng (contract / 계약), chính sách (policy / 정책) hoặc nội bộ (internal / 내부) điều khiển (control / 제어). dự án (project / 프로젝트) phải xác định yêu cầu (requirement / 요구사항), đơn vị sở hữu (owner / 오너), bằng chứng (evidence / 증거), timing và consequence của noncompliance.

Bảo mật (security / 보안), privacy, health & an toàn (safety / 안전) và sustainability có thể tạo yêu cầu (requirement / 요구사항) xuyên suốt vòng đời (lifecycle / 생명주기). Nếu compliance rà soát (review / 검토) chỉ được gọi ở cuối, rework thường rất đắt. “Shift left” trong dự án (project / 프로젝트) ngữ cảnh (context / 맥락) nghĩa đưa ràng buộc (constraint / 제약조건) vào yêu cầu (requirement / 요구사항)/thiết kế (design / 설계)/planning đủ sớm.

Compliance yêu cầu (requirement / 요구사항) cần được chuyển thành testable bằng chứng (evidence / 증거). “Đảm bảo privacy” quá mơ hồ; “PII được mã hóa at rest, retention theo chính sách (policy / 정책) X và truy cập (access / 접근) được log” tạo ranh giới (boundary / 경계) có thể verify. Đây là điểm nối giữa quản trị (governance / 거버넌스) và chất lượng (quality / 품질).

## Chính sách (policy / 정책) hierarchy và xung đột (conflict / 충돌)

Dự án (project / 프로젝트) có thể chịu nhiều quy tắc (rule / 규칙): law, regulation, đặc tả hợp đồng (contract / 계약), corporate chính sách (policy / 정책), kiến trúc (architecture / 아키텍처) tiêu chuẩn (standard / 표준), dự án (project / 프로젝트) working agreement. Chúng không có cùng authority.

Khi hai yêu cầu (requirement / 요구사항) xung đột (conflict / 충돌), nhóm (team / 팀) không nên tự chọn quy tắc (rule / 규칙) dễ hơn. Cần biết hierarchy, interpretation đơn vị sở hữu (owner / 오너) và exception cơ chế (mechanism / 메커니즘). nội bộ (internal / 내부) chính sách (policy / 정책) có thể có exception; law thường không thể được override bằng sponsor approval.

Làm rõ nguồn (source / 소스)/authority của ràng buộc (constraint / 제약조건) giúp scenario lập luận (reasoning / 추론) tránh lỗi “manager đã approve nên được phép”.

## Compliance by thiết kế (design / 설계) thay vì compliance at gate

Nếu mandatory điều khiển (control / 제어) chỉ được kiểm tra ở cuối, dự án (project / 프로젝트) đang biến compliance thành inspection. Compliance by thiết kế (design / 설계) đưa yêu cầu (requirement / 요구사항), bằng chứng (evidence / 증거) capture và rà soát (review / 검토) vào vòng đời (lifecycle / 생명주기) sớm.

Ví dụ dữ liệu (data / 데이터) retention yêu cầu (requirement / 요구사항) ảnh hưởng kiến trúc (architecture / 아키텍처), cơ sở dữ liệu (database / 데이터베이스) vòng đời (lifecycle / 생명주기), vendor đặc tả hợp đồng (contract / 계약) và kiểm thử (test / 테스트) bằng chứng (evidence / 증거). Nếu chỉ hỏi privacy nhóm (team / 팀) hai ngày trước go-live, cost-of-change rất cao.

Gate cuối vẫn cần, nhưng role của nó nên xác nhận accumulated bằng chứng (evidence / 증거) chứ không khám phá lần đầu yêu cầu (requirement / 요구사항) trọng yếu (critical / 중요).

## Bằng chứng (evidence / 증거) chuỗi (chain / 사슬) và auditability

Một điều khiển (control / 제어) chỉ đáng tin khi có bằng chứng (evidence / 증거) chuỗi (chain / 사슬). yêu cầu (requirement / 요구사항) nào áp dụng? Ai phê duyệt interpretation? điều khiển (control / 제어) nào được implement? kiểm thử (test / 테스트) nào chứng minh điều khiển (control / 제어) hoạt động? Exception nào đã được chấp nhận và bởi ai?

Traceability không nhất thiết phải là spreadsheet lớn. Trong software dự án (project / 프로젝트), chuỗi (chain / 사슬) có thể đi từ regulatory yêu cầu (requirement / 요구사항) → backlog/điều khiển (control / 제어) → mã (code / 코드)/cấu hình (configuration / 구성) → kiểm thử (test / 테스트) bằng chứng (evidence / 증거) → bản phát hành (release / 릴리스) approval. Mục tiêu là reconstruct lập luận (reasoning / 추론) khi kiểm tra (audit / 감사) hoặc sự cố (incident / 인시던트) xảy ra.

## Materiality và proportional điều khiển (control / 제어)

Không phải mọi deviation có cùng materiality. Một typo trong nội bộ (internal / 내부) ghi chú (note / 노트) khác với privacy điều khiển (control / 제어) missing. quản trị (governance / 거버넌스) cần threshold dựa trên consequence, exposure và reversibility.

Nếu mọi deviation được xử lý bằng cùng escalation, hệ thống (system / 시스템) quá tải. Nếu materiality bị hiểu là “issue nhỏ nên bỏ qua” mà không có quy tắc (rule / 규칙), hidden rủi ro (risk / 위험) tích tụ. Proportionality cần tường minh (explicit / 명시적) ranh giới (boundary / 경계).

## Exception management

Thực tế có lúc dự án (project / 프로젝트) không thể đáp ứng một nội bộ (internal / 내부) tiêu chuẩn (standard / 표준) đúng thời điểm. Khi đó exception không nên được “nói miệng cho qua”. Cần document phạm vi (scope / 범위), rationale, compensating điều khiển (control / 제어), đơn vị sở hữu (owner / 오너), expiry date và authority chấp nhận residual rủi ro (risk / 위험).

Nếu exception không có expiry hoặc rà soát (review / 검토), temporary deviation dễ trở thành permanent hidden debt.

Exception register cũng nên theo dõi concentration. Mười exception nhỏ trên cùng điều khiển (control / 제어) area có thể tạo systemic weakness dù từng exception riêng nằm dưới threshold.

## Organizational tiến trình (process / 프로세스) Assets và Enterprise Environmental Factors

Organizational tiến trình (process / 프로세스) Assets (OPA) gồm template, chính sách (policy / 정책), historical dữ liệu (data / 데이터), lessons learned và tiến trình (process / 프로세스) nội bộ mà dự án (project / 프로젝트) có thể dùng. Enterprise Environmental Factors (EEF) là môi trường (environment / 환경) dự án (project / 프로젝트) phải hoạt động trong đó: culture, cấu trúc (structure / 구조), thị trường (market / 시장), regulation, technology, tài nguyên (resource / 자원) availability.

Không cần học thuộc category nếu mô hình tư duy (mental model / 사고 모델) rõ: OPA phần lớn là kiến thức (knowledge / 지식)/tiến trình (process / 프로세스) asset có thể tận dụng; EEF là ngữ cảnh (context / 맥락) tạo ràng buộc (constraint / 제약조건)/opportunity và thường không do dự án (project / 프로젝트) tự kiểm soát.

OPA chỉ có giá trị nếu được cập nhật từ học tập (learning / 학습) thực tế. Template cũ không phản ánh sự cố (incident / 인시던트) hoặc technology mới có thể gây false confidence. dự án (project / 프로젝트) manager nên reuse kiến thức (knowledge / 지식) nhưng vẫn kiểm tra relevance.

## Organizational cấu trúc (structure / 구조) và authority

Functional organization giữ authority chủ yếu ở functional managers. Projectized organization trao authority mạnh hơn cho dự án (project / 프로젝트) manager. ma trận (matrix / 행렬) nằm giữa và có weak/balanced/strong variants.

Cấu trúc ảnh hưởng tốc độ tài nguyên (resource / 자원) allocation, escalation và xung đột (conflict / 충돌). Một PM trong weak ma trận (matrix / 행렬) không thể hành xử như có full authority; influence và sponsor hỗ trợ (support / 지원) trở nên quan trọng hơn.

Trong ma trận (matrix / 행렬), xung đột (conflict / 충돌) tài nguyên (resource / 자원) thường không giải được chỉ bằng “ưu tiên dự án (project / 프로젝트)”. Functional manager tối ưu năng lực (capability / 역량) dài hạn, dự án (project / 프로젝트) manager tối ưu temporary delivery. quản trị (governance / 거버넌스) phải cung cấp cơ chế (mechanism / 메커니즘) để giải sự đánh đổi (trade-off / 트레이드오프) thay vì để hai phía tranh quyền không chính thức.

## Nghiệp vụ (business / 비즈니스) môi trường (environment / 환경) là moving mục tiêu (target / 대상)

Bên ngoài (external / 외부) môi trường (environment / 환경) gồm regulation, thị trường (market / 시장), technology, competition, geopolitics, supply chuỗi (chain / 사슬) và xã hội (social / 사회적) expectation. PMP 2026 tăng trọng số nghiệp vụ (business / 비즈니스) môi trường (environment / 환경) vì dự án (project / 프로젝트) manager ngày càng phải nối delivery với nghiệp vụ (business / 비즈니스) ngữ cảnh (context / 맥락) chứ không chỉ nội bộ (internal / 내부) tiến trình (process / 프로세스).

Environmental scanning không có nghĩa PM dự đoán mọi trend. Nó nghĩa có cơ chế (mechanism / 메커니즘) để phát hiện thay đổi (change / 변경) có thể làm nghiệp vụ (business / 비즈니스) trường hợp (case / 사례), phạm vi (scope / 범위)/backlog hoặc rủi ro (risk / 위험) profile thay đổi.

Trigger có thể là regulation draft mới, competitor bản phát hành (release / 릴리스), FX movement, vendor acquisition hoặc strategic priority thay đổi (change / 변경). Một dự án (project / 프로젝트) khỏe phải có khả năng hỏi lại “nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) còn đúng không?” thay vì coi charter ban đầu là chân lý bất biến.

## Environmental tín hiệu (signal / 신호), trigger và phản hồi (response / 응답) horizon

Không phải mọi bên ngoài (external / 외부) tín hiệu (signal / 신호) cần thay đổi (change / 변경) ngay. nhóm (team / 팀) cần phân biệt weak tín hiệu (signal / 신호), confirmed trigger và material tác động (effect / 효과).

Một regulation draft có thể cần scenario phân tích (analysis / 분석); regulation finalized có thể trigger yêu cầu (requirement / 요구사항) thay đổi (change / 변경); enforcement date quyết phản hồi (response / 응답) horizon. Phản ứng quá sớm với noise tạo churn, phản ứng quá muộn với tín hiệu (signal / 신호) rõ tạo surprise.

Environmental scanning tốt nối tín hiệu (signal / 신호) → possible impact → đơn vị sở hữu (owner / 오너) → quyết định (decision / 결정) trigger. “Theo dõi thị trường” mà không có threshold không tạo actionability.

## Nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) cần sống trong suốt dự án (project / 프로젝트)

Nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) không chỉ dùng để xin ngân sách (budget / 예산). Khi chi phí (cost / 비용) tăng mạnh, thị trường (market / 시장) thay đổi hoặc expected benefit giảm, dự án (project / 프로젝트) cần reassess viability. Continuing chỉ vì đã đầu tư nhiều là sunk-cost trap.

Dự án (project / 프로젝트) manager có thể không có authority hủy dự án (project / 프로젝트), nhưng phải surface bằng chứng (evidence / 증거) khi expected giá trị (value / 값) thay đổi đáng kể. quản trị (governance / 거버넌스) body cần quyết định continue, pivot, pause hoặc terminate.

## Benefits quyền sở hữu (ownership / 소유권)

Dự án (project / 프로젝트) tạo năng lực (capability / 역량) nhưng benefit thường xuất hiện sau delivery. Vì vậy cần nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너) chịu trách nhiệm cho adoption và benefit realization. Nếu không có đơn vị sở hữu (owner / 오너) sau closure, organization có thể hoàn thành đầu ra (output / 출력) nhưng không ai theo dõi kết quả (outcome / 결과).

Một benefit map nối đầu ra (output / 출력) → năng lực (capability / 역량) → hành vi (behavior / 동작) thay đổi (change / 변경) → measurable kết quả (outcome / 결과) giúp xác định giả định (assumption / 가정) nào nằm ngoài điều khiển (control / 제어) trực tiếp của dự án (project / 프로젝트) nhưng vẫn phải được quản lý như phụ thuộc (dependency / 의존성).

## Benefit phụ thuộc (dependency / 의존성) mạng (network / 네트워크)

Benefit hiếm khi đến từ một đầu ra (output / 출력) duy nhất. Revenue uplift có thể cần hệ thống (system / 시스템) năng lực (capability / 역량), sales huấn luyện (training / 학습), pricing thay đổi (change / 변경), marketing và operations sức chứa (capacity / 용량). Nếu một phụ thuộc (dependency / 의존성) không thuộc dự án (project / 프로젝트) nhưng không có đơn vị sở hữu (owner / 오너), benefit mô hình (model / 모델) có hidden gap.

Benefit mạng (network / 네트워크) nên cho thấy phụ thuộc (dependency / 의존성), đơn vị sở hữu (owner / 오너) và giả định (assumption / 가정). Điều này giúp quản trị (governance / 거버넌스) phân biệt “dự án (project / 프로젝트) delivered” với “investment giá trị (value / 값) realized”.

Nếu multiple projects cùng claim một benefit, portfolio cần tránh double-count. Attribution lô-gic (logic / 논리) phải consistent với nghiệp vụ (business / 비즈니스) trường hợp (case / 사례).

## Benefits realization không kết thúc ở dự án (project / 프로젝트) closure

Closure chỉ xác nhận dự án (project / 프로젝트) công việc (work / 작업) đã hoàn thành và chuyển tiếp (transition / 전이) đã xảy ra. Benefit có thể cần nhiều tháng hoặc năm mới materialize. Vì vậy benefits realization plan cần đơn vị sở hữu (owner / 오너), chỉ số (metric / 지표), baseline, mục tiêu (target / 대상), đo lường (measurement / 측정) cadence và trigger rà soát (review / 검토) sau dự án (project / 프로젝트).

Nếu benefit phụ thuộc adoption, tiến trình (process / 프로세스) redesign hoặc sales hành vi (behavior / 동작), các activity đó phải được nối vào operating mô hình (model / 모델) sau handover. Một dự án (project / 프로젝트) đóng đúng quy trình nhưng không có post-project đo lường (measurement / 측정) đang bỏ mất vòng phản hồi (feedback loop / 피드백 루프) cuối cùng của investment.

Quản trị (governance / 거버넌스) cũng cần phân biệt benefit không xuất hiện vì dự án (project / 프로젝트) đầu ra (output / 출력) kém với benefit không xuất hiện vì giả định (assumption / 가정) nghiệp vụ (business / 비즈니스) sai. Hai nguyên nhân dẫn tới học tập (learning / 학습) khác nhau.

## Organizational thay đổi (change / 변경)

Dự án (project / 프로젝트) tạo đầu ra (output / 출력), nhưng organization cần hấp thụ thay đổi. thay đổi (change / 변경) management quan tâm readiness, sponsor coalition, communication, huấn luyện (training / 학습), resistance và reinforcement. Một hệ thống (system / 시스템) mới không tạo kết quả (outcome / 결과) nếu người dùng (user / 사용자) tiếp tục dùng workaround cũ.

Dự án (project / 프로젝트) manager không nhất thiết sở hữu toàn bộ organizational thay đổi (change / 변경) management, nhưng phải tích hợp phụ thuộc (dependency / 의존성) đó vào success mô hình (model / 모델) và chuyển tiếp (transition / 전이).

Resistance không phải lúc nào cũng “người dùng chống thay đổi”. Nó có thể là tín hiệu (signal / 신호) rằng tiến trình (process / 프로세스) mới tăng tải công việc (workload / 워크로드), incentive không phù hợp hoặc stakeholder không tin dữ liệu (data / 데이터). Treat resistance như thông tin (information / 정보) giúp thiết kế (design / 설계) intervention tốt hơn.

## Thay đổi (change / 변경) readiness: ability, willingness và môi trường (environment / 환경)

Readiness không chỉ là “đã huấn luyện (training / 학습)”. Người dùng có thể biết cách dùng hệ thống nhưng không muốn dùng vì incentive cũ vẫn thưởng hành vi (behavior / 동작) cũ. Hoặc họ muốn dùng nhưng tiến trình (process / 프로세스), permission hay manager expectation không cho phép.

Có thể lập luận (reasoning / 추론) readiness qua ba lớp: ability—người dùng có skill/năng lực (capability / 역량) không; willingness—họ hiểu purpose, tin thay đổi (change / 변경) và thấy incentive hợp lý không; môi trường (environment / 환경)—công cụ (tool / 도구), chính sách (policy / 정책), tải công việc (workload / 워크로드) và management reinforcement có hỗ trợ hành vi (behavior / 동작) mới không.

Nếu một trong ba lớp thất bại (fail / 실패), communication campaign mạnh hơn chưa chắc sửa được adoption.

## Reinforcement và regression về hành vi (behavior / 동작) cũ

Ngay sau go-live, novelty và project-team hỗ trợ (support / 지원) có thể làm adoption cao tạm thời. Khi hypercare kết thúc, người dùng (user / 사용자) có thể quay lại workaround cũ nếu incentive, manager hành vi (behavior / 동작) hoặc tiến trình (process / 프로세스) không reinforce thay đổi (change / 변경).

Vì vậy adoption cần theo dõi sau chuyển tiếp (transition / 전이), không chỉ launch week. Sustainable thay đổi (change / 변경) cần cục bộ (local / 로컬) manager reinforcement, removal of old đường dẫn (path / 경로) khi phù hợp và vòng phản hồi (feedback loop / 피드백 루프) để friction được sửa.

Không phải lúc nào cũng nên tắt old tiến trình (process / 프로세스) ngay; nếu new hệ thống (system / 시스템) chưa stable, parallel run có thể là rủi ro (risk / 위험) điều khiển (control / 제어). Nhưng old đường dẫn (path / 경로) không có retirement plan sẽ làm dual tiến trình (process / 프로세스) thành permanent độ phức tạp (complexity / 복잡도).

## Thay đổi (change / 변경) saturation và portfolio tác động (effect / 효과)

Một nhóm (team / 팀) có thể chịu nhiều initiative cùng lúc: ERP mới, org restructure, compliance huấn luyện (training / 학습) và office relocation. Mỗi dự án (project / 프로젝트) riêng lẻ nhìn thay đổi (change / 변경) impact “vừa phải”, nhưng tổng tải thay đổi lên cùng population có thể vượt absorption sức chứa (capacity / 용량).

Đây là thay đổi (change / 변경) saturation. Portfolio quản trị (governance / 거버넌스) cần nhìn dùng chung (shared / 공유) stakeholder tải (load / 로드), huấn luyện (training / 학습) calendar, blackout period và operational peak. Nếu không, dự án (project / 프로젝트) manager có thể đổ lỗi cho “resistance” trong khi organization đơn giản là không còn bandwidth để hấp thụ thêm thay đổi (change / 변경).

Thay đổi (change / 변경) saturation là ví dụ điển hình cho hệ thống (system / 시스템) tác động (effect / 효과) không nhìn thấy khi quản lý từng dự án (project / 프로젝트) riêng lẻ.

## Adoption chỉ số (metric / 지표) phải đo hành vi (behavior / 동작), không chỉ activity

Huấn luyện (training / 학습) attendance, email open tỷ lệ (rate / 비율) hoặc số guide được gửi là activity chỉ số (metric / 지표). Adoption cần measure hành vi (behavior / 동작) hoặc kết quả (outcome / 결과): tỷ lệ giao dịch (transaction / 트랜잭션) đi qua tiến trình (process / 프로세스) mới, active users, workaround tỷ lệ (rate / 비율), lỗi (error / 오류) tỷ lệ (rate / 비율), cycle thời gian (time / 시간) hoặc benefit indicator.

Một rollout có 100% huấn luyện (training / 학습) completion nhưng 40% người dùng (user / 사용자) quay lại spreadsheet cũ chưa thể coi là successful adoption.

Đo lường (measurement / 측정) nên segment theo role, location hoặc cohort để tìm nơi intervention cần khác nhau.

## Chuyển tiếp (transition / 전이) và operating mô hình (model / 모델)

Handover tốt không chỉ chuyển document. thao tác (operation / 연산) cần role, hỗ trợ (support / 지원) mô hình (model / 모델), sự cố (incident / 인시던트) đường dẫn (path / 경로), truy cập (access / 접근), monitoring, ngân sách (budget / 예산), vendor contact, SLA, quyền sở hữu (ownership / 소유권) và improvement backlog.

Nếu dự án (project / 프로젝트) nhóm (team / 팀) rời đi nhưng không ai có authority/sức chứa (capacity / 용량) vận hành năng lực (capability / 역량) mới, dự án (project / 프로젝트) chỉ chuyển rủi ro (risk / 위험) sang operations.

Chuyển tiếp (transition / 전이) readiness vì vậy là acceptance criterion của hệ thống (system / 시스템) vận hành, không phải administrative checklist cuối dự án (project / 프로젝트).

## Ethics và professional responsibility

Ethics không phải chỉ tránh hành vi trái luật. dự án (project / 프로젝트) manager thường đứng giữa pressure giao hàng và obligation về an toàn (safety / 안전), truthfulness, fairness hoặc confidentiality. Reporting một forecast xấu trung thực có thể khó về chính trị nhưng che giấu dữ liệu làm quản trị (governance / 거버넌스) mất chức năng.

Khi xung đột (conflict / 충돌) of interest hoặc pressure vượt authority, escalate qua channel phù hợp và giữ bằng chứng (evidence / 증거). “Sponsor muốn vậy” không tự động biến hành động thành acceptable.

Professional judgment cũng yêu cầu phân biệt confidentiality với concealment. Không chia sẻ sensitive dữ liệu (data / 데이터) bừa bãi là đúng; giấu rủi ro (risk / 위험) material khỏi người có quyền quyết định là quản trị (governance / 거버넌스) thất bại (failure / 실패).

## Speaking truth to power là điều khiển (control / 제어) cơ chế (mechanism / 메커니즘)

Quản trị (governance / 거버넌스) chỉ hoạt động nếu bad news có thể đi lên. Nếu incentive trừng phạt người báo variance nhưng thưởng dashboard xanh, thông tin (information / 정보) hệ thống (system / 시스템) sẽ tự làm đẹp số liệu.

PM cần trình bày material fact, bất định (uncertainty / 불확실성) và recommendation rõ ràng, ngay cả khi message không thuận political expectation. Điều này không có nghĩa confrontational; có thể communicate bằng bằng chứng (evidence / 증거), option và consequence.

Một organization trưởng thành phân biệt messenger khỏi bài toán (problem / 문제). Nếu không, silence trở thành rational hành vi (behavior / 동작) của nhóm (team / 팀) và quản trị (governance / 거버넌스) mất sensor.

## Quản trị (governance / 거버넌스) thất bại (failure / 실패) modes

Một dạng thất bại (failure mode / 실패 모드) là quyết định (decision / 결정) độ trễ (latency / 지연 시간): authority tồn tại nhưng approval quá chậm nên nhóm (team / 팀) tạo workaround. dạng thất bại (failure mode / 실패 모드) khác là shadow quản trị (governance / 거버넌스): quyết định (decision / 결정) thật xảy ra trong chat riêng còn meeting chỉ hợp thức hóa. Một dạng khác là chỉ số (metric / 지표) gaming: report được tối ưu để trông xanh thay vì phản ánh trạng thái (state / 상태) thật.

Khi quản trị (governance / 거버넌스) tạo incentive che bad news, organization mất early warning. quản trị (governance / 거버넌스) tốt phải thưởng transparency đủ để bài toán (problem / 문제) được thấy trước khi trở thành crisis.

Ở mức (level / 수준) portfolio, dạng thất bại (failure mode / 실패 모드) còn là zombie dự án (project / 프로젝트): initiative không còn giá trị (value / 값) rõ nhưng không ai muốn terminate vì political chi phí (cost / 비용). Một dạng khác là tài nguyên (resource / 자원) illusion: cùng specialist được allocate cho nhiều dự án (project / 프로젝트) mà mỗi plan đều giả định 100% availability. PMO/portfolio quản trị (governance / 거버넌스) phải surface những xung đột (conflict / 충돌) này thay vì chỉ consolidate dashboard.

Quản trị (governance / 거버넌스) cũng có thể thất bại (fail / 실패) vì chính sách (policy / 정책) collision, assurance theater, exception accumulation hoặc committee without authority. Những thất bại (failure / 실패) này khác nhau nhưng đều phá link giữa bằng chứng (evidence / 증거) và hành động (action / 동작).

## Ví dụ scenario

Một sản phẩm (product / 제품) sắp go-live nhưng privacy rà soát (review / 검토) chưa hoàn tất. nghiệp vụ (business / 비즈니스) nói delay sẽ mất campaign. PM không nên tự bỏ điều khiển (control / 제어) hoặc chỉ “để bảo mật (security / 보안) quyết”. Cần xác định chính sách (policy / 정책)/regulatory yêu cầu (requirement / 요구사항), rủi ro (risk / 위험)/authority, available compensating điều khiển (control / 제어), deadline, approver hợp lệ và escalation. Nếu compliance là mandatory gate, nghiệp vụ (business / 비즈니스) pressure không thay đổi yêu cầu (requirement / 요구사항); nó chỉ thay urgency của resolution.

Giả sử rà soát (review / 검토) phát hiện một điều khiển (control / 제어) nội bộ (internal / 내부) chưa đủ nhưng law vẫn được đáp ứng. Khi đó quản trị (governance / 거버넌스) có thể cho phép exception có thời hạn với compensating monitoring nếu authority phù hợp chấp nhận residual rủi ro (risk / 위험). Nhưng nếu legal yêu cầu (requirement / 요구사항) bị vi phạm, cùng cơ chế exception nội bộ không thể hợp pháp hóa bản phát hành (release / 릴리스).

Một scenario portfolio: dự án (project / 프로젝트) A và B đều cần cùng specialist cơ sở dữ liệu (database / 데이터베이스) trong tháng 11 và cả hai report “on nhánh học (track / 트랙)”. PMO phát hiện sức chứa (capacity / 용량) chỉ đủ cho một. Câu hỏi không phải ép specialist overtime để giữ hai dashboard xanh; portfolio quản trị (governance / 거버넌스) phải xem strategic priority, phụ thuộc (dependency / 의존성), delay chi phí (cost / 비용), alternative tài nguyên (resource / 자원) và sequencing rồi đưa sự đánh đổi (trade-off / 트레이드오프) lên đúng quyết định (decision / 결정) mức (level / 수준).

Một scenario thay đổi (change / 변경): rollout mới đạt 100% huấn luyện (training / 학습) completion nhưng adoption chỉ 55%. Thay vì tổ chức thêm cùng một khóa huấn luyện (training / 학습) cho toàn bộ người dùng (user / 사용자), nhóm (team / 팀) cần segment dữ liệu (data / 데이터) và tìm thất bại (failure / 실패) tầng (layer / 계층). Nếu một nhóm không có permission, đây là môi trường (environment / 환경) bài toán (problem / 문제); nếu manager vẫn yêu cầu spreadsheet cũ, đây là reinforcement/incentive bài toán (problem / 문제); nếu người dùng (user / 사용자) không hiểu workflow, mới là năng lực (capability / 역량)/huấn luyện (training / 학습) bài toán (problem / 문제).

Một scenario quản trị (governance / 거버넌스): kiến trúc (architecture / 아키텍처) board họp hai tuần một lần, nhưng sprint cần quyết định (decision / 결정) giao diện (interface / 인터페이스) trong ba ngày. nhóm (team / 팀) liên tục implement trước rồi xin approve sau. Chỉ nhắc nhóm (team / 팀) “tuân thủ quy trình” không sửa nguyên nhân gốc (root cause / 근본 원인). quản trị (governance / 거버넌스) cần threshold/delegation hoặc faster rà soát (review / 검토) đường dẫn (path / 경로) để điều khiển (control / 제어) cadence match delivery cadence.

## Mô hình tư duy (mental model / 사고 모델)

> quản trị (governance / 거버넌스) là kiến trúc biến bằng chứng (evidence / 증거) thành quyết định có authority; portfolio quản trị (governance / 거버넌스) phân bổ capital, sức chứa (capacity / 용량) và attention; compliance bảo vệ non-negotiable ranh giới (boundary / 경계); organizational thay đổi (change / 변경) biến năng lực (capability / 역량) thành hành vi (behavior / 동작) bền vững. quản trị (governance / 거버넌스) tốt không tối đa điều khiển (control / 제어)—nó tối ưu điều khiển (control / 제어) chất lượng (quality / 품질), quyết định (decision / 결정) độ trễ (latency / 지연 시간) và accountability cùng lúc.

Tiếp theo: [Agile, adaptive và hybrid delivery](./10_agile_hybrid_and_adaptive_delivery.md).

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 foundations value and project system](./00_foundations_value_and_project_system.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
