# 10 — Agile, adaptive và hybrid delivery

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **10 — Agile, adaptive và hybrid delivery**. Route đi từ uncertainty → hypothesis/feedback → incremental delivery → evidence-based decisions → hybrid governance, để agile được đọc qua tốc độ học và giá trị tạo ra.

## Agile là phản hồi (feedback / 피드백) economics, không phải ceremony

Agile (애자일) có giá trị khi bất định (uncertainty / 불확실성) cao và phản hồi (feedback / 피드백) sớm có thể thay đổi quyết định (decision / 결정). Bản chất không nằm ở daily meeting hay board, mà ở việc giảm batch kích thước (size / 크기) của học tập (learning / 학습), giao increment có thể kiểm chứng, đưa customer/stakeholder phản hồi (feedback / 피드백) vào planning và cho nhóm (team / 팀) quyền thích ứng trong guardrail.

Nếu tổ chức chạy sprint nhưng mọi phạm vi (scope / 범위) đã khóa một năm, phản hồi (feedback / 피드백) không thể thay priority và bản phát hành (release / 릴리스) vẫn big-bang, ceremony agile không tạo adaptive năng lực (capability / 역량).

Một mô hình tư duy (mental model / 사고 모델) hữu ích là economics của phản hồi (feedback / 피드백): phản hồi (feedback / 피드백) càng đến sớm, chi phí (cost / 비용) sửa giả định (assumption / 가정) càng thấp. Nhưng phản hồi (feedback / 피드백) cũng có chi phí. Vì vậy cadence nên đủ nhanh để giảm rủi ro (risk / 위험) đáng kể nhưng không nhanh đến mức ceremony lớn hơn học tập (learning / 학습) giá trị (value / 값).

> **Nối mạch:** **Agile là phản hồi (feedback / 피드백) economics, không phải ceremony** đặt vấn đề; **Adaptive vòng lặp (loop / 루프): hypothesis → bằng chứng (evidence / 증거) → quyết định (decision / 결정)** kiểm tra bằng chứng, rồi **Empiricism: transparency, inspection, adaptation** mở rộng hệ quả.

## Adaptive vòng lặp (loop / 루프): hypothesis → bằng chứng (evidence / 증거) → quyết định (decision / 결정)

Adaptive delivery chỉ thật sự adaptive khi công việc (work / 작업) nối vào hypothesis. nhóm (team / 팀) đang tin điều gì về người dùng (user / 사용자), solution, kiến trúc (architecture / 아키텍처) hoặc tiến trình (process / 프로세스)? Increment/experiment nào tạo bằng chứng (evidence / 증거)? bằng chứng (evidence / 증거) nào đủ mạnh để giữ, đổi hoặc bỏ hypothesis?

Nếu sprint chỉ biến backlog item thành mã (code / 코드) nhưng không có câu hỏi học tập, nhóm (team / 팀) có thể giao nhanh mà học tập (learning / 학습) chậm. Ngược lại, discovery tạo nhiều insight nhưng không thay backlog cũng chỉ là research theater.

Một vòng adaptive hoàn chỉnh có dạng:

```text
hypothesis → smallest useful test/increment → evidence → interpretation → decision → next hypothesis
```

Điểm quan trọng là quyết định (decision / 결정). phản hồi (feedback / 피드백) không có quyền thay direction thì chỉ là thông tin (information / 정보) collection.

> **Nối mạch:** **Adaptive vòng lặp (loop / 루프): hypothesis → bằng chứng (evidence / 증거) → quyết định (decision / 결정)** đặt vấn đề; **Empiricism: transparency, inspection, adaptation** kiểm tra bằng chứng, rồi **Sản phẩm (product / 제품) goal tạo stable direction cho adaptive phạm vi (scope / 범위)** mở rộng hệ quả.

## Empiricism: transparency, inspection, adaptation

Adaptive delivery dựa trên empiricism: làm cho trạng thái (state / 상태) đủ minh bạch để inspect, sau đó adaptation dựa trên bằng chứng (evidence / 증거). Nếu công việc (work / 작업) status không đáng tin, backlog không phản ánh priority thật hoặc increment không thực sự usable, inspection trở nên giả và adaptation cũng sai.

Transparency không có nghĩa báo cáo thật nhiều. Nó nghĩa những thông tin (information / 정보) quan trọng cho quyết định (decision / 결정) được nhìn thấy đúng lúc: chất lượng (quality / 품질) trạng thái (state / 상태), blocked phụ thuộc (dependency / 의존성), unfinished công việc (work / 작업), forecast và stakeholder phản hồi (feedback / 피드백).

Empiricism còn phụ thuộc chất lượng (quality / 품질) của bằng chứng (evidence / 증거). Một demo cho 5 người dùng (user / 사용자) thân thiện không chứng minh product-market fit. Một chỉ số (metric / 지표) aggregate có thể che segment thất bại (failure / 실패). Inspection tốt phải hiểu mẫu (sample / 표본), đo lường (measurement / 측정) ranh giới (boundary / 경계) và độ lệch (bias / 편향).

> **Nối mạch:** **Sản phẩm (product / 제품) goal tạo stable direction cho adaptive phạm vi (scope / 범위)** nối từ **Empiricism: transparency, inspection, adaptation** sang **Sản phẩm (product / 제품) backlog như một option set**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sản phẩm (product / 제품) goal tạo stable direction cho adaptive phạm vi (scope / 범위)

Adaptive phạm vi (scope / 범위) có thể thay nhưng hệ thống (system / 시스템) vẫn cần direction đủ ổn định. sản phẩm (product / 제품) goal/kết quả (outcome / 결과) tạo ràng buộc (constraint / 제약조건) cho cục bộ (local / 로컬) adaptation: backlog có thể đổi, nhưng mọi đổi phải giải thích vì sao giúp mục tiêu (objective / 목표) tốt hơn.

Nếu backlog thay liên tục theo stakeholder mới nhất mà không có stable kết quả (outcome / 결과), organization đang phản ứng với noise chứ không học tập (learning / 학습). Adaptive không đồng nghĩa direction instability.

Một goal tốt cũng có stop criterion. Nếu bằng chứng (evidence / 증거) liên tục cho thấy hypothesis không tạo giá trị (value / 값), nhóm (team / 팀) phải có permission dừng/pivot thay vì tiếp tục vì roadmap đã công bố.

> **Nối mạch:** **Sản phẩm (product / 제품) backlog như một option set** nối từ **Sản phẩm (product / 제품) goal tạo stable direction cho adaptive phạm vi (scope / 범위)** sang **Backlog aging và option decay**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sản phẩm (product / 제품) backlog như một option set

Backlog không phải một đặc tả hợp đồng (contract / 계약) rằng mọi item sẽ được xây. Nó là ordered set của possibilities theo giá trị (value / 값), rủi ro (risk / 위험), học tập (learning / 학습) và phụ thuộc (dependency / 의존성). Item gần delivery được refine chi tiết hơn; item xa giữ coarse-grained để tránh overplanning.

Chủ sản phẩm (product owner / 제품 책임자) chịu trách nhiệm tối ưu giá trị (value / 값) và thứ tự (ordering / 순서) trong Scrum ngữ cảnh (context / 맥락). dự án (project / 프로젝트) manager trong môi trường (environment / 환경) PMP có thể phối hợp quản trị (governance / 거버넌스), phụ thuộc (dependency / 의존성), stakeholder, rủi ro (risk / 위험) và organizational ranh giới (boundary / 경계) mà không giành micro-control của self-managing nhóm (team / 팀).

Backlog item nên đủ nhỏ để tạo học tập (learning / 학습) trong thời gian hợp lý. Một item quá lớn che nhiều giả định (assumption / 가정); một item quá nhỏ lại tạo administrative overhead. Decomposition tốt theo vertical slice thường tạo bằng chứng (evidence / 증거) tốt hơn chia theo technical tầng (layer / 계층) thuần túy.

> **Nối mạch:** **Backlog aging và option decay** nối từ **Sản phẩm (product / 제품) backlog như một option set** sang **Prioritization không chỉ là nghiệp vụ (business / 비즈니스) giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Backlog aging và option decay

Option trong backlog không giữ giá trị (value / 값) mãi. yêu cầu (requirement / 요구사항) có thể hết relevance, phụ thuộc (dependency / 의존성) đổi, thị trường (market / 시장) cửa sổ (window / 윈도우) đóng hoặc giả định (assumption / 가정) ban đầu không còn đúng.

Backlog quá lớn có carrying chi phí (cost / 비용): refinement, duplicate item, tìm kiếm (search / 검색) chi phí (cost / 비용) và cognitive tải (load / 로드). Item không có đơn vị sở hữu (owner / 오너)/rationale hoặc không được rà soát (review / 검토) nhiều tháng có thể trở thành inventory stale.

Vì vậy backlog refinement không chỉ thêm detail; nó còn xóa option không còn đáng giữ. “Không làm” là một đầu ra (output / 출력) hợp lệ của học tập (learning / 학습).

> **Nối mạch:** **Prioritization không chỉ là nghiệp vụ (business / 비즈니스) giá trị (value / 값)** nối từ **Backlog aging và option decay** sang **Chi phí (cost / 비용) of delay và sequencing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Prioritization không chỉ là nghiệp vụ (business / 비즈니스) giá trị (value / 값)

Priority nên phản ánh giá trị (value / 값), rủi ro (risk / 위험), học tập (learning / 학습), phụ thuộc (dependency / 의존성) và chi phí (cost / 비용) of delay. Một technical spike có direct nghiệp vụ (business / 비즈니스) giá trị (value / 값) thấp nhưng có thể rất cao về thông tin (information / 정보) giá trị (value / 값). Một compliance item có customer-visible giá trị (value / 값) thấp nhưng mandatory. Một phụ thuộc (dependency / 의존성) item có thể cần làm sớm để unblock nhiều công việc (work / 작업) sau.

Vì vậy “làm tính năng (feature / 기능) có giá trị (value / 값) cao nhất trước” là quá đơn giản. Adaptive planning cần nhìn toàn bộ hệ thống (system / 시스템) mục tiêu (objective / 목표).

Priority còn phụ thuộc expiry. Một small tính năng (feature / 기능) có giá trị (value / 값) vừa nhưng thị trường (market / 시장) cửa sổ (window / 윈도우) một tuần có thể nên đi trước tính năng (feature / 기능) giá trị (value / 값) lớn hơn nhưng không time-sensitive.

> **Nối mạch:** **Chi phí (cost / 비용) of delay và sequencing** nối từ **Prioritization không chỉ là nghiệp vụ (business / 비즈니스) giá trị (value / 값)** sang **Increment, Definition of Done và chất lượng (quality / 품질) ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chi phí (cost / 비용) of delay và sequencing

Chi phí (cost / 비용) of delay biến “trễ” thành economic consequence. Nhưng nó không nhất thiết tuyến tính. Seasonal launch có cliff; regulatory deadline có penalty step; học tập (learning / 학습) item có giá trị (value / 값) giảm nếu đến sau kiến trúc (architecture / 아키텍처) commitment.

Adaptive sequencing nên nhìn giá trị (value / 값) over thời gian (time / 시간), không chỉ static priority. Điều này nối backlog quyết định (decision / 결정) với finance/schedule lập luận (reasoning / 추론) ở chapter `05–06`.

> **Nối mạch:** **Chi phí (cost / 비용) of delay và sequencing** đặt tiêu chí; **Increment, Definition of Done và chất lượng (quality / 품질) ranh giới (boundary / 경계)** dùng nó để kiểm tra ranh giới, rồi **Done, deployed, released và giá trị (value / 값) realized khác nhau** mở rộng cơ chế.

## Increment, Definition of Done và chất lượng (quality / 품질) ranh giới (boundary / 경계)

Increment có ý nghĩa khi đủ integrated và usable để tạo bằng chứng (evidence / 증거). Definition of Done tạo dùng chung (shared / 공유) chất lượng (quality / 품질) ranh giới (boundary / 경계) cho “done”. Nếu mỗi sprint có nhiều item “90% xong” nhưng kiểm thử (test / 테스트)/tích hợp (integration / 통합) dồn cuối bản phát hành (release / 릴리스), dự án (project / 프로젝트) vẫn tích batch lớn và hidden inventory.

Acceptance criteria áp cho item cụ thể; Definition of Done là chất lượng (quality / 품질) bar chung. Hai thứ bổ sung nhau.

Nếu Definition of Done bỏ tích hợp (integration / 통합), bảo mật (security / 보안) scan hoặc documentation bắt buộc, nhóm (team / 팀) có thể tối ưu sprint completion nhưng tạo bản phát hành (release / 릴리스) debt. “Done” phải phản ánh trạng thái đủ thật để management không bị false progress.

> **Nối mạch:** **Increment, Definition of Done và chất lượng (quality / 품질) ranh giới (boundary / 경계)** đặt tiêu chí; **Done, deployed, released và giá trị (value / 값) realized khác nhau** dùng nó để kiểm tra ranh giới, rồi **MVP, prototype, experiment và increment không phải một thứ** mở rộng cơ chế.

## Done, deployed, released và giá trị (value / 값) realized khác nhau

Một increment có thể Done nhưng chưa deploy. mã (code / 코드) có thể deploy nhưng cờ tính năng (feature flag / 기능 플래그) chưa bản phát hành (release / 릴리스) cho người dùng (user / 사용자). tính năng (feature / 기능) có thể bản phát hành (release / 릴리스) nhưng chưa được adopt. Adoption có thể xảy ra nhưng benefit chưa materialize.

Phân biệt các trạng thái (state / 상태) này ngăn false progress. “Chúng ta bản phát hành (release / 릴리스) mỗi sprint” không đồng nghĩa nghiệp vụ (business / 비즈니스) nhận giá trị (value / 값) mỗi sprint nếu người dùng (user / 사용자) chưa dùng hoặc operational phụ thuộc (dependency / 의존성) chưa sẵn sàng.

Adaptive reporting nên nói rõ trạng thái (state / 상태) nào đang được đo.

> **Nối mạch:** **MVP, prototype, experiment và increment không phải một thứ** nối từ **Done, deployed, released và giá trị (value / 값) realized khác nhau** sang **Experiment phải có quyết định (decision / 결정) quy tắc (rule / 규칙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## MVP, prototype, experiment và increment không phải một thứ

Prototype dùng để học về feasibility, tương tác (interaction / 상호작용) hoặc solution shape; nó có thể hoàn toàn không production-ready. Experiment dùng để kiểm tra một hypothesis. Minimum Viable sản phẩm (product / 제품) (MVP) là phiên bản đủ nhỏ để kiểm tra giá trị (value / 값) proposition với người dùng (user / 사용자) thật hoặc thị trường (market / 시장) thật. Increment là phần sản phẩm (product / 제품) tích hợp đáp ứng chất lượng (quality / 품질) ranh giới (boundary / 경계) đã định.

Nhầm bốn khái niệm này tạo quản trị (governance / 거버넌스) sai. Một prototype có thể chấp nhận bảo mật (security / 보안) điều khiển (control / 제어) nhẹ vì chạy trong sandbox; một increment customer-facing thì không. Một MVP không có nghĩa “sản phẩm chất lượng thấp”; nó giảm phạm vi (scope / 범위) giả thuyết nhưng vẫn phải đủ an toàn và usable trong ngữ cảnh (context / 맥락) được phép.

Dự án (project / 프로젝트) manager cần hỏi sản phẩm tạo ra (artifact / 산출물) này được tạo để học điều gì, ai sẽ dùng, exposure là bao nhiêu và exit criterion là gì. “Chúng ta đang làm MVP” không phải lý do để bỏ qua compliance hoặc operational readiness.

> **Nối mạch:** **Experiment phải có quyết định (decision / 결정) quy tắc (rule / 규칙)** nối từ **MVP, prototype, experiment và increment không phải một thứ** sang **Batch kích thước (size / 크기) và queueing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Experiment phải có quyết định (decision / 결정) quy tắc (rule / 규칙)

Experiment không chỉ có chỉ số (metric / 지표); nó cần quy tắc (rule / 규칙): kết quả (result / 결과) nào làm continue, pivot, stop hoặc collect thêm dữ liệu (data / 데이터).

Nếu nhóm (team / 팀) nhìn kết quả (result / 결과) sau rồi mới chọn threshold thuận lợi, confirmation độ lệch (bias / 편향) dễ xảy ra. Pre-defined hypothesis, mẫu (sample / 표본)/segment, chỉ số (metric / 지표) và quyết định (decision / 결정) ranh giới (boundary / 경계) làm học tập (learning / 학습) đáng tin hơn.

Experiment cũng có ethical/quản trị (governance / 거버넌스) ranh giới (boundary / 경계). Không phải mọi hypothesis được phép kiểm thử (test / 테스트) trực tiếp trên customer nếu exposure, consent hoặc an toàn (safety / 안전) consequence quá lớn.

> **Nối mạch:** **Batch kích thước (size / 크기) và queueing** nối từ **Experiment phải có quyết định (decision / 결정) quy tắc (rule / 규칙)** sang **Batch kích thước (size / 크기) có optimum kinh tế, không phải càng nhỏ càng tốt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Batch kích thước (size / 크기) và queueing

Batch nhỏ làm giảm thời gian từ công việc (work / 작업) start tới phản hồi (feedback / 피드백). Nhưng nếu nhóm (team / 팀) bắt quá nhiều công việc (work / 작업) song song, mỗi item vẫn chờ lâu trong hàng đợi (queue / 큐). Đây là lý do WIP quan trọng: utilization cao không đồng nghĩa luồng (flow / 흐름) tốt.

Một hệ thống (system / 시스템) luôn giữ mọi người 100% bận có thể làm cycle thời gian (time / 시간) tăng mạnh vì không còn slack để xử lý variation, rà soát (review / 검토) hoặc urgent defect. Adaptive delivery tối ưu luồng (flow / 흐름) của giá trị (value / 값) hơn utilization của từng cá nhân.

> **Nối mạch:** **Batch kích thước (size / 크기) có optimum kinh tế, không phải càng nhỏ càng tốt** nối từ **Batch kích thước (size / 크기) và queueing** sang **Iteration, luồng (flow / 흐름) và Kanban**, vì cơ chế trước tạo đầu vào cho bước sau.

## Batch kích thước (size / 크기) có optimum kinh tế, không phải càng nhỏ càng tốt

Batch nhỏ giảm rủi ro (risk / 위험) và phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간) nhưng tăng giao dịch (transaction / 트랜잭션) chi phí (cost / 비용): planning, setup, triển khai (deployment / 배포), rà soát (review / 검토), coordination. Nếu mỗi thay đổi cực nhỏ cần manual compliance gate hai giờ, batch quá nhỏ có thể tạo overhead lớn hơn học tập (learning / 학습) giá trị (value / 값).

Automation thường làm optimum batch nhỏ hơn bằng cách giảm giao dịch (transaction / 트랜잭션) chi phí (cost / 비용). Đây là lý do CI/CD hoặc automated bằng chứng (evidence / 증거) có impact quản lý chứ không chỉ kỹ thuật.

Câu hỏi đúng là batch nào tối thiểu hóa tổng chi phí (cost / 비용) của waiting, rework và giao dịch (transaction / 트랜잭션)—not “sprint càng ngắn càng agile”.

> **Nối mạch:** Batch size có optimum kinh tế, nên Iteration, flow và Kanban phải được chọn theo mục tiêu. **Class of service và expedite risk** kiểm tra chi phí của việc ưu tiên.

## Iteration, luồng (flow / 흐름) và Kanban

Iteration-based approach timebox công việc (work / 작업); flow-based approach giới hạn WIP và kéo công việc (work / 작업) theo sức chứa (capacity / 용량). Kanban chú trọng visualize workflow, WIP limit, manage luồng (flow / 흐름) và improve hệ thống (system / 시스템). Scrum tạo role/sự kiện (event / 이벤트)/sản phẩm tạo ra (artifact / 산출물) khung phần mềm (framework / 프레임워크) rõ hơn. Không cần biến đây thành tranh luận brand; chọn cơ chế (mechanism / 메커니즘) theo bài toán (problem / 문제).

WIP limit giúp expose bottleneck. Nếu nhóm (team / 팀) cứ bắt đầu tác vụ (task / 작업) mới khi testing hàng đợi (queue / 큐) đầy, total utilization nhìn cao nhưng cycle thời gian (time / 시간) và phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간) tăng.

Kanban board chỉ có giá trị nếu column phản ánh real workflow trạng thái (state / 상태). Một board đẹp nhưng công việc (work / 작업) thực vẫn chạy ngoài hệ thống không tạo khả năng quan sát (observability / 관측 가능성).

> **Nối mạch:** Iteration, flow và Kanban tạo nhịp quan sát; Class of service và expedite risk điều chỉnh thứ tự. **Scrum events như control loops** kiểm tra phản hồi và giới hạn.

## Lớp (class / 클래스) of dịch vụ (service / 서비스) và expedite rủi ro (risk / 위험)

Không phải mọi công việc (work / 작업) có cùng urgency. Một môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트), fixed-date regulatory item và normal tính năng (feature / 기능) có thể cần dịch vụ (service / 서비스) chính sách (policy / 정책) khác.

Nhưng expedite lane không miễn phí. Nếu quá nhiều item được gọi urgent, luồng bố cục thông thường (normal flow / 일반 흐름) bị phá và priority hệ thống (system / 시스템) mất meaning. nhóm (team / 팀) nên định nghĩa tiêu chí expedite và theo dõi chi phí (cost / 비용) mà urgent công việc (work / 작업) gây cho hàng đợi (queue / 큐) khác.

> **Nối mạch:** **Scrum events như điều khiển (control / 제어) loops** nối từ **Lớp (class / 클래스) of dịch vụ (service / 서비스) và expedite rủi ro (risk / 위험)** sang **Estimation và forecasting trong adaptive ngữ cảnh (context / 맥락)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Scrum events như điều khiển (control / 제어) loops

Sprint Planning tạo near-term commitment dựa trên mục tiêu (objective / 목표) và sức chứa (capacity / 용량). Daily Scrum giúp nhóm (team / 팀) inspect progress toward Sprint Goal và điều chỉnh coordination. Sprint rà soát (review / 검토) lấy stakeholder phản hồi (feedback / 피드백) trên increment. Retrospective inspect cách làm việc và chọn improvement.

Nếu biến Daily Scrum thành status report cho manager, hoặc Sprint rà soát (review / 검토) thành demo ceremonial không ảnh hưởng backlog, sự kiện (event / 이벤트) mất control-loop hàm (function / 함수). Khi học khung phần mềm (framework / 프레임워크), nên luôn hỏi sự kiện (event / 이벤트) này làm giảm loại bất định (uncertainty / 불확실성) nào.

> **Nối mạch:** **Estimation và forecasting trong adaptive ngữ cảnh (context / 맥락)** nối từ **Scrum events như điều khiển (control / 제어) loops** sang **Story điểm (point / 지점) là relative mô hình (model / 모델), không phải giờ được mã hóa**, vì cơ chế trước tạo đầu vào cho bước sau.

## Estimation và forecasting trong adaptive ngữ cảnh (context / 맥락)

Velocity là empirical planning tín hiệu (signal / 신호) của một nhóm (team / 팀), không phải hiệu năng (performance / 성능) KPI. thông lượng (throughput / 처리량) và cycle-time phân phối (distribution / 분포) có thể tạo probabilistic forecast, ví dụ “85% item tương tự hoàn thành trong 8 ngày”. Forecast nên dùng historical bằng chứng (evidence / 증거) và được cập nhật (update / 업데이트) khi hệ thống (system / 시스템) thay đổi.

So sánh velocity giữa hai nhóm (team / 팀) dễ gây gaming vì story điểm (point / 지점) không có đơn vị (unit / 단위) chuẩn xuyên nhóm (team / 팀). Khi chỉ số (metric / 지표) trở thành mục tiêu (target / 대상), hành vi (behavior / 동작) thường thay đổi để tối ưu chỉ số (metric / 지표) thay vì kết quả (outcome / 결과).

Forecast tốt nên nói bằng phạm vi (range / 범위) và confidence thay vì một ngày duy nhất khi bất định (uncertainty / 불확실성) cao.

> **Nối mạch:** **Story điểm (point / 지점) là relative mô hình (model / 모델), không phải giờ được mã hóa** nối từ **Estimation và forecasting trong adaptive ngữ cảnh (context / 맥락)** sang **Probabilistic forecast và bằng chứng (evidence / 증거) từ luồng (flow / 흐름)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Story điểm (point / 지점) là relative mô hình (model / 모델), không phải giờ được mã hóa

Story điểm (point / 지점) thường được dùng để biểu diễn tương đối kích thước (size / 크기)/độ phức tạp (complexity / 복잡도)/bất định (uncertainty / 불확실성) trong một nhóm (team / 팀). Nếu organization quy định “1 điểm (point / 지점) = 8 giờ”, điểm (point / 지점) mất vai trò relative tín hiệu (signal / 신호) và trở thành thời gian (time / 시간) estimate vòng vo.

Story điểm (point / 지점) cũng không phải measure productivity. nhóm (team / 팀) có thể đổi quy mô (scale / 규모) mà năng lực (capability / 역량) không đổi. Nếu management thưởng nhóm (team / 팀) tăng velocity, incentive tự nhiên là điểm (point / 지점) inflation.

Khi công việc (work / 작업) tương đối đồng nhất và historical dữ liệu (data / 데이터) đủ tốt, thông lượng (throughput / 처리량)/cycle thời gian (time / 시간) có thể forecast mà không cần điểm (point / 지점). Khi item kích thước (size / 크기) thay đổi lớn, decomposition hoặc class-of-service có thể quan trọng hơn cố tìm một conversion factor thần kỳ.

> **Nối mạch:** **Story điểm (point / 지점) là relative mô hình (model / 모델), không phải giờ được mã hóa** đặt vấn đề; **Probabilistic forecast và bằng chứng (evidence / 증거) từ luồng (flow / 흐름)** kiểm tra bằng chứng, rồi **Forecast calibration** mở rộng hệ quả.

## Probabilistic forecast và bằng chứng (evidence / 증거) từ luồng (flow / 흐름)

Một bản phát hành (release / 릴리스) gồm 40 item còn lại không nên được forecast chỉ bằng `40 / average velocity` nếu thông lượng (throughput / 처리량) biến động mạnh. Historical thông lượng (throughput / 처리량) phân phối (distribution / 분포) có thể được mẫu (sample / 표본) nhiều lần để tạo phạm vi (range / 범위) finish hoặc xác suất hoàn thành trước mục tiêu (target / 대상) date. Đây là cùng mô hình tư duy (mental model / 사고 모델) probabilistic lập luận (reasoning / 추론) đã dùng ở [Risk & Uncertainty](./08_risk_uncertainty_issues_and_decisions.md) và [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md).

Forecast chỉ đáng tin khi công việc (work / 작업) hệ thống (system / 시스템) đủ tương đồng với historical cửa sổ (window / 윈도우). Nếu nhóm (team / 팀) vừa thay kiến trúc (architecture / 아키텍처), thêm ba người mới hoặc đổi Definition of Done, dữ liệu cũ cần được discount hoặc phân đoạn.

Điểm quan trọng không phải dùng công cụ (tool / 도구) Monte Carlo cho mọi sprint; điểm quan trọng là tránh biến average thành certainty.

> **Nối mạch:** **Probabilistic forecast và bằng chứng (evidence / 증거) từ luồng (flow / 흐름)** đặt vấn đề; **Forecast calibration** kiểm tra bằng chứng, rồi **Adaptive planning across horizons** mở rộng hệ quả.

## Forecast calibration

Adaptive forecast nên được đánh giá bằng calibration theo thời gian. Nếu nhóm (team / 팀) nói “85% confidence” nhưng chỉ đạt mục tiêu (target / 대상) khoảng 50% số lần, mô hình (model / 모델) hoặc đầu vào (input / 입력) chưa calibrated.

Calibration tốt hơn việc ép nhóm (team / 팀) cho một date “chắc chắn”. Nó khuyến khích phạm vi (range / 범위) honest và học tập (learning / 학습) từ forecast miss.

Forecast miss cũng cần phân loại: phạm vi (scope / 범위) inflow, blocked phụ thuộc (dependency / 의존성), thông lượng (throughput / 처리량) shift hay mô hình (model / 모델) giả định (assumption / 가정) sai. Chỉ cập nhật average mà không hiểu cause dễ lặp lại lỗi (error / 오류).

> **Nối mạch:** **Adaptive planning across horizons** nối từ **Forecast calibration** sang **Quyết định (decision / 결정) horizon khác delivery horizon**, vì cơ chế trước tạo đầu vào cho bước sau.

## Adaptive planning across horizons

Vision/roadmap định hướng kết quả (outcome / 결과) dài hơn. bản phát hành (release / 릴리스) planning nối kết quả (outcome / 결과) với increment/milestone. Iteration planning chọn công việc (work / 작업) gần. Daily coordination xử lý luồng (flow / 흐름). Retrospective cải thiện hệ thống (system / 시스템). Mỗi horizon có mức detail khác nhau.

Đây là rolling-wave planning dưới dạng adaptive: commitment gần mạnh hơn; option xa linh hoạt hơn.

Roadmap không nên bị biến thành fixed phạm vi (scope / 범위) schedule dài hạn nếu môi trường còn nhiều bất định (uncertainty / 불확실성). Nó có thể giữ kết quả (outcome / 결과), strategic chuỗi (sequence / 시퀀스) và major ràng buộc (constraint / 제약조건) trong khi detail thay đổi theo bằng chứng (evidence / 증거).

> **Nối mạch:** **Quyết định (decision / 결정) horizon khác delivery horizon** nối từ **Adaptive planning across horizons** sang **Thay đổi (change / 변경) trong adaptive môi trường (environment / 환경) không có nghĩa “không cần điều khiển (control / 제어)”**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quyết định (decision / 결정) horizon khác delivery horizon

Nhóm (team / 팀) có thể chỉ plan tác vụ (task / 작업) chi tiết hai tuần nhưng vẫn phải quyết kiến trúc (architecture / 아키텍처), vendor hoặc regulatory đường dẫn (path / 경로) nhiều tháng trước. Không phải mọi quyết định (decision / 결정) có thể postpone tới sprint gần nhất.

Adaptive planning cần identify quyết định (decision / 결정) có long lead thời gian (time / 시간) hoặc high irreversibility và tạo bằng chứng (evidence / 증거) sớm. “Không plan xa” là hiểu sai agility; đúng hơn là không lần ghi nhận (commit / 커밋) detail xa hơn thông tin (information / 정보) chất lượng (quality / 품질) cho phép, trong khi vẫn quản lý future ràng buộc (constraint / 제약조건).

> **Nối mạch:** **Thay đổi (change / 변경) trong adaptive môi trường (environment / 환경) không có nghĩa “không cần điều khiển (control / 제어)”** nối từ **Quyết định (decision / 결정) horizon khác delivery horizon** sang **Adaptive thay đổi (change / 변경) điều khiển (control / 제어) là continuous reprioritization có guardrail**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thay đổi (change / 변경) trong adaptive môi trường (environment / 환경) không có nghĩa “không cần điều khiển (control / 제어)”

Backlog reprioritization trong authority của chủ sản phẩm (product owner / 제품 책임자) có thể không cần formal thay đổi (change / 변경) yêu cầu (request / 요청) cho từng item. Nhưng thay ngân sách (budget / 예산), regulatory commitment, đặc tả hợp đồng (contract / 계약) phạm vi (scope / 범위), kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계) hoặc milestone đã được quản trị (governance / 거버넌스) phê duyệt có thể vẫn cần thay đổi (change / 변경) cơ chế (mechanism / 메커니즘) chính thức.

Vì vậy câu “Agile không có thay đổi (change / 변경) điều khiển (control / 제어)” là sai. Adaptive delivery chuyển một phần thay đổi (change / 변경) quyết định (decision / 결정) vào frequent planning vòng lặp (loop / 루프), nhưng quản trị (governance / 거버넌스) ranh giới (boundary / 경계) vẫn tồn tại. Tailoring tốt định nghĩa rõ thay đổi (change / 변경) nào là normal backlog management và thay đổi (change / 변경) nào vượt authority/tolerance.

Điều này đặc biệt quan trọng trong hybrid dự án (project / 프로젝트): nhóm (team / 팀) có thể đổi chuỗi (sequence / 시퀀스) hàng ngày nhưng không thể tự thay contractual acceptance hoặc regulatory bằng chứng (evidence / 증거) yêu cầu (requirement / 요구사항).

> **Nối mạch:** **Adaptive thay đổi (change / 변경) điều khiển (control / 제어) là continuous reprioritization có guardrail** nối từ **Thay đổi (change / 변경) trong adaptive môi trường (environment / 환경) không có nghĩa “không cần điều khiển (control / 제어)”** sang **Discovery và delivery không nên tách tuyệt đối**, vì cơ chế trước tạo đầu vào cho bước sau.

## Adaptive thay đổi (change / 변경) điều khiển (control / 제어) là continuous reprioritization có guardrail

Traditional thay đổi (change / 변경) điều khiển (control / 제어) thường tạo tường minh (explicit / 명시적) yêu cầu (request / 요청)/approval vì baseline phạm vi (scope / 범위) ổn định hơn. Adaptive điều khiển (control / 제어) dùng backlog thứ tự (ordering / 순서), WIP chính sách (policy / 정책), sản phẩm (product / 제품) goal và rà soát (review / 검토) cadence để absorb small thay đổi (change / 변경) liên tục.

Nhưng thay đổi (change / 변경) vẫn có chi phí (cost / 비용). Nếu stakeholder thêm công việc (work / 작업) nhanh hơn thông lượng (throughput / 처리량), backlog inflow tăng và lead thời gian (time / 시간) dài. Adaptive hệ thống (system / 시스템) cần sức chứa (capacity / 용량) quy tắc (rule / 규칙): new item vào có thể đẩy item khác ra hoặc làm forecast thay đổi; không có free phạm vi (scope / 범위).

> **Nối mạch:** **Discovery và delivery không nên tách tuyệt đối** nối từ **Adaptive thay đổi (change / 변경) điều khiển (control / 제어) là continuous reprioritization có guardrail** sang **Technical practice ảnh hưởng trực tiếp khả năng adaptive**, vì cơ chế trước tạo đầu vào cho bước sau.

## Discovery và delivery không nên tách tuyệt đối

Discovery tìm hiểu bài toán (problem / 문제), người dùng (user / 사용자) và solution hypothesis; delivery biến hypothesis đủ tốt thành working increment. Nếu discovery đi trước delivery nhiều tháng, nhóm (team / 팀) dễ quay lại big-batch specification. Nếu không có discovery nào, nhóm (team / 팀) có thể bản dựng (build / 빌드) rất nhanh thứ không có giá trị (value / 값).

Dual-track hoặc continuous discovery chỉ có ý nghĩa khi học tập (learning / 학습) được nối vào backlog quyết định (decision / 결정). Discovery sản phẩm tạo ra (artifact / 산출물) không phải mục tiêu; quyết định (decision / 결정) chất lượng (quality / 품질) mới là mục tiêu.

> **Nối mạch:** **Technical practice ảnh hưởng trực tiếp khả năng adaptive** nối từ **Discovery và delivery không nên tách tuyệt đối** sang **Technical option giá trị (value / 값) và reversibility**, vì cơ chế trước tạo đầu vào cho bước sau.

## Technical practice ảnh hưởng trực tiếp khả năng adaptive

Agile về management không đủ nếu technical hệ thống (system / 시스템) làm thay đổi (change / 변경) rất đắt. Automated kiểm thử (test / 테스트), continuous tích hợp (integration / 통합), modular kiến trúc (architecture / 아키텍처), cờ tính năng (feature flag / 기능 플래그) và triển khai (deployment / 배포) automation thường giảm chi phí (cost / 비용) of thay đổi (change / 변경) và phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간).

PMP không cần đi sâu hiện thực (implementation / 구현), nhưng dự án (project / 프로젝트) manager phải hiểu một phụ thuộc (dependency / 의존성) quan trọng: technical debt có thể làm organization “muốn agile” nhưng không thể thay đổi nhanh. Nội dung kỹ thuật sâu hơn nằm ở [Delivery, configuration và operations](../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md) và [Maintenance, evolution và technical debt](../computer_science/09_software_engineering/04_maintenance_evolution_and_technical_debt.md).

> **Nối mạch:** **Technical option giá trị (value / 값) và reversibility** nối từ **Technical practice ảnh hưởng trực tiếp khả năng adaptive** sang **Hybrid giao diện (interface / 인터페이스) là nơi rủi ro tích tụ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Technical option giá trị (value / 값) và reversibility

Modularity, tính năng (feature / 기능) flags, backward-compatible giao diện (interface / 인터페이스) và automated quay lui (rollback / 롤백) không chỉ là kỹ thuật (engineering / 엔지니어링) elegance. Chúng giữ option đổi hướng với chi phí (cost / 비용) thấp hơn.

Khi hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처) làm mọi thay đổi (change / 변경) cross-cutting, management adaptation bị giới hạn dù tiến trình (process / 프로세스) rất agile. Technical reversibility là một phần của dự án (project / 프로젝트) flexibility.

> **Nối mạch:** **Hybrid giao diện (interface / 인터페이스) là nơi rủi ro tích tụ** nối từ **Technical option giá trị (value / 값) và reversibility** sang **Cadence mismatch và synchronization chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hybrid giao diện (interface / 인터페이스) là nơi rủi ro tích tụ

Khi adaptive nhóm (team / 팀) phụ thuộc predictive vendor hoặc quản trị (governance / 거버넌스) gate, giao diện (interface / 인터페이스) cần được tường minh (explicit / 명시적). Ví dụ sprint nhóm (team / 팀) bản phát hành (release / 릴리스) tính năng (feature / 기능) liên tục nhưng regulator chỉ approve theo quarterly batch. Khi đó “done” nội bộ khác “released to customer”. Schedule và status phải phân biệt hai trạng thái (state / 상태) để không tạo false progress.

Một hybrid thiết kế (design / 설계) tốt xác định cadence, đặc tả hợp đồng (contract / 계약), acceptance, phụ thuộc (dependency / 의존성), thay đổi (change / 변경) cơ chế (mechanism / 메커니즘) và tích hợp (integration / 통합) điểm (point / 지점) giữa các chế độ (mode / 모드).

Nếu nội bộ (internal / 내부) nhóm (team / 팀) dùng backlog linh hoạt nhưng vendor đặc tả hợp đồng (contract / 계약) fixed phạm vi (scope / 범위)/fixed date, thay đổi (change / 변경) economics cần được tường minh (explicit / 명시적). Mỗi backlog reorder có thể không chi phí (cost / 비용) nhiều bên trong nhưng có đặc tả hợp đồng (contract / 계약) implication bên ngoài.

> **Nối mạch:** **Cadence mismatch và synchronization chi phí (cost / 비용)** nối từ **Hybrid giao diện (interface / 인터페이스) là nơi rủi ro tích tụ** sang **Đặc tả hợp đồng (contract / 계약) và procurement trong adaptive ngữ cảnh (context / 맥락)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cadence mismatch và synchronization chi phí (cost / 비용)

Hai subsystem có cadence khác nhau tạo waiting. nhóm (team / 팀) A integrate daily, vendor B deliver monthly, regulator kiểm thử (test / 테스트) quarterly. luồng (flow / 흐름) toàn hệ thống (system / 시스템) bị giới hạn bởi giao diện (interface / 인터페이스) chậm nhất nếu công việc (work / 작업) cần qua gate đó.

Giải pháp không nhất thiết làm mọi cadence giống nhau. Có thể dùng stable giao diện (interface / 인터페이스), mock/sandbox, decouple phụ thuộc (dependency / 의존성) hoặc create pre-validation để giảm waiting.

Hybrid thiết kế (design / 설계) tốt tối ưu synchronization chi phí (cost / 비용), không chỉ chọn methodology riêng cho từng nhóm (team / 팀).

> **Nối mạch:** **Đặc tả hợp đồng (contract / 계약) và procurement trong adaptive ngữ cảnh (context / 맥락)** nối từ **Cadence mismatch và synchronization chi phí (cost / 비용)** sang **Adaptive quản trị (governance / 거버넌스) và funding guardrail**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đặc tả hợp đồng (contract / 계약) và procurement trong adaptive ngữ cảnh (context / 맥락)

Adaptive delivery phù hợp hơn với đặc tả hợp đồng (contract / 계약) cho phép collaboration, incremental acceptance hoặc capacity-based arrangement khi yêu cầu (requirement / 요구사항) còn thay đổi. Fixed-price fixed-scope có thể hợp khi phạm vi (scope / 범위) đủ ổn định, nhưng nếu bất định (uncertainty / 불확실성) cao nó thường chuyển bất định (uncertainty / 불확실성) thành negotiation friction hoặc change-order chi phí (cost / 비용).

Không có đặc tả hợp đồng (contract / 계약) kiểu (type / 타입) “agile” tự động. Câu hỏi là incentive có hỗ trợ dùng chung (shared / 공유) kết quả (outcome / 결과) và adaptation hay không.

> **Nối mạch:** **Adaptive quản trị (governance / 거버넌스) và funding guardrail** nối từ **Đặc tả hợp đồng (contract / 계약) và procurement trong adaptive ngữ cảnh (context / 맥락)** sang **Adaptive funding và option-based investment**, vì cơ chế trước tạo đầu vào cho bước sau.

## Adaptive quản trị (governance / 거버넌스) và funding guardrail

Adaptive nhóm (team / 팀) cần autonomy bên trong ranh giới (boundary / 경계), nhưng autonomy không đồng nghĩa không có ngân sách (budget / 예산), rủi ro (risk / 위험) appetite hay quyết định (decision / 결정) threshold. Organization có thể tài trợ theo sản phẩm (product / 제품)/năng lực (capability / 역량) horizon, rà soát (review / 검토) kết quả (outcome / 결과) theo cadence và giữ stop/pivot quyết định (decision / 결정) ở portfolio hoặc sponsor mức (level / 수준).

Một quản trị (governance / 거버넌스) thiết kế (design / 설계) tốt tách reversible sản phẩm (product / 제품) quyết định (decision / 결정) khỏi irreversible investment quyết định (decision / 결정). nhóm (team / 팀) nên tự quyết UI bản sao (copy / 복사) hay chuỗi (sequence / 시퀀스) của backlog item nếu nằm trong guardrail; nhưng tăng funding 40%, thay regulated dữ liệu (data / 데이터) processor hoặc bỏ committed thị trường (market / 시장) launch có thể cần authority khác.

Nếu steering committee approve từng người dùng (user / 사용자) story, vòng phản hồi (feedback loop / 피드백 루프) bị nghẹt. Nếu nhóm (team / 팀) tự thay strategic commitment mà không quản trị (governance / 거버넌스), organization mất điều khiển (control / 제어). Adaptive quản trị (governance / 거버넌스) là đặt quyết định (decision / 결정) ở mức (level / 수준) thấp nhất vẫn giữ được accountability.

> **Nối mạch:** **Adaptive funding và option-based investment** nối từ **Adaptive quản trị (governance / 거버넌스) và funding guardrail** sang **Servant leadership và impediment removal**, vì cơ chế trước tạo đầu vào cho bước sau.

## Adaptive funding và option-based investment

Funding toàn năm cho một hypothesis chưa kiểm chứng có thể khóa (lock / 잠금) capital quá sớm. Incremental funding theo kết quả (outcome / 결과)/học tập (learning / 학습) milestone giữ option stop/pivot.

Nhưng funding rà soát (review / 검토) quá dày làm nhóm (team / 팀) mất continuity và tạo pitch theater. Cadence cần match material bất định (uncertainty / 불확실성) và investment kích thước (size / 크기).

Adaptive portfolio lô-gic (logic / 논리) không có nghĩa “mỗi sprint xin tiền”; nó nghĩa commitment tăng cùng bằng chứng (evidence / 증거).

> **Nối mạch:** **Servant leadership và impediment removal** nối từ **Adaptive funding và option-based investment** sang **Autonomy ranh giới (boundary / 경계) phải đi cùng visibility**, vì cơ chế trước tạo đầu vào cho bước sau.

## Servant leadership và impediment removal

Adaptive nhóm (team / 팀) cần autonomy nhưng organization vẫn có impediment: slow procurement, dùng chung (shared / 공유) môi trường (environment / 환경), chính sách (policy / 정책), cross-team phụ thuộc (dependency / 의존성). Leader tạo giá trị (value / 값) bằng cách remove hệ thống (system / 시스템) ràng buộc (constraint / 제약조건), facilitate xung đột (conflict / 충돌) và bảo vệ vòng phản hồi (feedback loop / 피드백 루프) hơn là phân tác vụ (task / 작업) từng người.

Nếu cùng một blocker xuất hiện nhiều sprint, xử lý từng lần chỉ là workaround. Retrospective nên chuyển issue thành hệ thống (system / 시스템) improvement có đơn vị sở hữu (owner / 오너).

> **Nối mạch:** **Servant leadership và impediment removal** đặt tiêu chí; **Autonomy ranh giới (boundary / 경계) phải đi cùng visibility** dùng nó để kiểm tra ranh giới, rồi **Agile không loại bỏ documentation hoặc quản trị (governance / 거버넌스)** mở rộng cơ chế.

## Autonomy ranh giới (boundary / 경계) phải đi cùng visibility

Self-management không có nghĩa cục bộ (local / 로컬) nhóm (team / 팀) được tối ưu mà downstream không biết. Autonomy có hiệu quả khi mục tiêu (objective / 목표), ràng buộc (constraint / 제약조건), giao diện (interface / 인터페이스) và bằng chứng (evidence / 증거) visible.

Nhóm (team / 팀) có thể tự quyết hiện thực (implementation / 구현) nhưng nếu quyết định (decision / 결정) làm Đặc tả API (API contract / API 계약) đổi, blast radius vượt cục bộ (local / 로컬) ranh giới (boundary / 경계). quyết định (decision / 결정) right cần match consequence radius.

> **Nối mạch:** **Autonomy ranh giới (boundary / 경계) phải đi cùng visibility** đặt tiêu chí; **Agile không loại bỏ documentation hoặc quản trị (governance / 거버넌스)** dùng nó để kiểm tra ranh giới, rồi **Scaling không chỉ là thêm ceremony** mở rộng cơ chế.

## Agile không loại bỏ documentation hoặc quản trị (governance / 거버넌스)

Regulated agile dự án (project / 프로젝트) vẫn cần bằng chứng (evidence / 증거). Difference là documentation được tạo đúng thời điểm và tự động hóa nếu có thể. Traceability có thể nối backlog item → mã (code / 코드) thay đổi (change / 변경) → kiểm thử (test / 테스트) → bản phát hành (release / 릴리스) approval. quản trị (governance / 거버넌스) mục tiêu (objective / 목표) được giữ, ceremony có thể khác.

Trong software dự án (project / 프로젝트), cơ chế delivery kỹ thuật sâu hơn nằm ở [Delivery, configuration và operations](../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md). PMP chapter giữ focus ở coordination/giá trị (value / 값)/quản trị (governance / 거버넌스) ranh giới (boundary / 경계).

> **Nối mạch:** **Scaling không chỉ là thêm ceremony** nối từ **Agile không loại bỏ documentation hoặc quản trị (governance / 거버넌스)** sang **Scaling law: phụ thuộc (dependency / 의존성) tăng nhanh hơn nhóm (team / 팀) count**, vì cơ chế trước tạo đầu vào cho bước sau.

## Scaling không chỉ là thêm ceremony

Khi nhiều nhóm (team / 팀) cùng làm một sản phẩm (product / 제품) hoặc program, vấn đề chính là phụ thuộc (dependency / 의존성), kiến trúc (architecture / 아키텍처), tích hợp (integration / 통합), quyết định (decision / 결정) rights và dùng chung (shared / 공유) kết quả (outcome / 결과). Thêm nhiều tầng (layer / 계층) meeting có thể làm coordination chi phí (cost / 비용) tăng mà không giảm coupling.

Trước khi chọn scaling khung phần mềm (framework / 프레임워크), nên hỏi phụ thuộc (dependency / 의존성) nào thực sự bắt buộc, phụ thuộc (dependency / 의존성) nào có thể loại bỏ bằng kiến trúc (architecture / 아키텍처)/nhóm (team / 팀) ranh giới (boundary / 경계), và quyết định (decision / 결정) nào cần synchronize. Organization thiết kế (design / 설계) và hệ thống (system / 시스템) thiết kế (design / 설계) thường liên quan chặt.

Tích hợp (integration / 통합) cadence thường quan trọng hơn reporting cadence. Hai nhóm (team / 팀) demo tốt riêng lẻ nhưng chỉ integrate cuối quý vẫn mang batch rủi ro (risk / 위험) lớn. dùng chung (shared / 공유) môi trường (environment / 환경), giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약), phiên bản (version / 버전) tính tương thích (compatibility / 호환성) và cross-team Definition of Done có thể là điều khiển (control / 제어) mạnh hơn thêm một coordination meeting.

> **Nối mạch:** **Scaling law: phụ thuộc (dependency / 의존성) tăng nhanh hơn nhóm (team / 팀) count** nối từ **Scaling không chỉ là thêm ceremony** sang **Adaptive anti-patterns**, vì cơ chế trước tạo đầu vào cho bước sau.

## Scaling law: phụ thuộc (dependency / 의존성) tăng nhanh hơn nhóm (team / 팀) count

Thêm nhóm (team / 팀) có thể tăng sức chứa (capacity / 용량) nhưng cũng tăng giao diện (interface / 인터페이스). Nếu kiến trúc (architecture / 아키텍처) và quyền sở hữu (ownership / 소유권) không rõ, coordination đường dẫn (path / 경로) tăng nhanh và marginal thông lượng (throughput / 처리량) giảm.

Scaling tốt cố giảm phụ thuộc (dependency / 의존성) trước khi tăng coordination ceremony. nhóm (team / 팀) ranh giới (boundary / 경계) nên align với giá trị (value / 값) stream/năng lực (capability / 역량) đủ độc lập để cục bộ (local / 로컬) quyết định (decision / 결정) không liên tục chờ cross-team agreement.

> **Nối mạch:** **Adaptive anti-patterns** nối từ **Scaling law: phụ thuộc (dependency / 의존성) tăng nhanh hơn nhóm (team / 팀) count** sang **Ví dụ scenario**, vì cơ chế trước tạo đầu vào cho bước sau.

## Adaptive anti-patterns

Sprint waterfall xảy ra khi phân tích (analysis / 분석), dev và kiểm thử (test / 테스트) vẫn chạy tuần tự trong cùng sprint. Fake agility xảy ra khi nhóm (team / 팀) có ceremony nhưng priority không thể thay. Velocity pressure biến estimate thành hiệu năng (performance / 성능) mục tiêu (target / 대상). Backlog hoarding tạo hàng nghìn item không còn relevance. “Self-managing” bị dùng như lý do manager không remove organizational blocker.

Một anti-pattern khác là bản phát hành (release / 릴리스) every sprint nhưng không đo kết quả (outcome / 결과). Delivery nhanh không tự động tạo giá trị (value / 값) nhanh. Một anti-pattern tinh vi hơn là backlog thay đổi liên tục nhưng không có stable sản phẩm (product / 제품) goal; lúc đó nhóm (team / 팀) “adaptive” nhưng chỉ phản ứng với noise.

Experiment theater xảy ra khi mọi công việc (work / 작업) được gọi là experiment nhưng kết quả (result / 결과) không bao giờ làm roadmap đổi. Hybrid theater xảy ra khi organization cộng tất cả gate và ceremony của cả hai chế độ (mode / 모드) mà không bỏ điều khiển (control / 제어) trùng lặp.

> **Nối mạch:** **Adaptive anti-patterns** nêu quy tắc; **Ví dụ scenario** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Ví dụ scenario

Customer liên tục đổi priority nhưng deadline compliance cố định. Câu trả lời không phải “agile nên chấp nhận mọi thay đổi (change / 변경)” hoặc “deadline cố định nên khóa toàn bộ phạm vi (scope / 범위)”. Ta giữ compliance kết quả (outcome / 결과)/deadline như ràng buộc (constraint / 제약조건), ưu tiên backlog theo giá trị (value / 값) và mandatory phạm vi (scope / 범위), giảm optional phạm vi (scope / 범위) khi cần, validate increment thường xuyên và quản lý phụ thuộc (dependency / 의존성)/gate rõ.

Giả sử tích hợp (integration / 통합) với regulator chỉ có kiểm thử (test / 테스트) cửa sổ (window / 윈도우) mỗi tháng. nhóm (team / 팀) vẫn có thể làm adaptive bên trong, nhưng tích hợp (integration / 통합) cửa sổ (window / 윈도우) là bên ngoài (external / 외부) cadence phải đưa vào planning. tính năng (feature / 기능) nên được integrated/prototyped sớm trước cửa sổ (window / 윈도우) thay vì chờ sprint cuối. Hybrid ở đây là thiết kế vòng phản hồi (feedback loop / 피드백 루프) quanh một ràng buộc (constraint / 제약조건) không adaptive.

Một scenario khác: velocity tăng 25% sau khi management đặt KPI “tăng điểm (point / 지점) mỗi sprint”, nhưng escaped defect và cycle thời gian (time / 시간) cũng tăng. Kết luận không nên là nhóm (team / 팀) productivity tăng. chỉ số (metric / 지표) đã trở thành mục tiêu (target / 대상) và hành vi (behavior / 동작) thay đổi. PM nên quay lại kết quả (outcome / 결과)/luồng (flow / 흐름)/chất lượng (quality / 품질) bằng chứng (evidence / 증거), bỏ incentive gây gaming và dùng velocity đúng vai trò cục bộ (local / 로컬) planning tín hiệu (signal / 신호).

Một scenario experimentation: onboarding experiment tăng activation 8% nhưng churn tháng đầu không đổi. nhóm (team / 팀) không nên tự động rollout full tính năng (feature / 기능) chỉ vì primary chỉ số (metric / 지표) tăng. Cần xem hypothesis ban đầu là activation có dẫn tới retention hay không, guardrail chỉ số (metric / 지표) có xấu đi không và thêm bằng chứng (evidence / 증거) có khả năng đổi quyết định (decision / 결정) không.

> **Nối mạch:** Ví dụ scenario nêu quy tắc; **Mô hình tư duy** thử quy tắc trong tình huống cụ thể để khép mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Adaptive delivery tối ưu tốc độ học bằng cách giảm batch, rút phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간) và giữ option; predictive delivery tối ưu coordination/predictability khi commitment sớm có giá trị; hybrid tối ưu giao diện (interface / 인터페이스) giữa các lô-gic (logic / 논리) khác cadence. Agility thật được đo bằng việc bằng chứng (evidence / 증거) có thể thay quyết định (decision / 결정) mà không phá quản trị (governance / 거버넌스) ranh giới (boundary / 경계).

Tiếp theo: [Measurement, status, closure và continuous improvement](./11_measurement_status_closure_and_continuous_improvement.md).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
