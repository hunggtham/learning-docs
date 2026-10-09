# 05 — Schedule, estimation, phụ thuộc (dependency / 의존성) và luồng (flow / 흐름)

## Schedule là mô hình (model / 모델) của phụ thuộc (dependency / 의존성) và bất định (uncertainty / 불확실성)

Lịch trình (schedule / 일정) không phải lời hứa rằng tương lai sẽ diễn ra đúng một tập ngày. Nó là mô hình (model / 모델) cho chuỗi (sequence / 시퀀스), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원), ràng buộc (constraint / 제약조건) và estimate hiện tại. Giá trị của schedule nằm ở việc cho thấy điều gì quyết định finish date và tín hiệu (signal / 신호) nào làm forecast thay đổi.

Nếu một Gantt chart có rất nhiều ngày nhưng không phản ánh phụ thuộc (dependency / 의존성) hoặc bất định (uncertainty / 불확실성), nó tạo false precision.

Schedule tốt phải đủ detailed để coordination nhưng không detailed đến mức maintenance chi phí (cost / 비용) lớn hơn thông tin (information / 정보) giá trị (value / 값). Planning horizon càng xa thì detail thường càng coarse vì bất định (uncertainty / 불확실성) lớn hơn.

Một schedule trưởng thành cần trả lời được ba lớp câu hỏi: lô-gic (logic / 논리) nào buộc công việc (work / 작업) phải đi theo chuỗi (sequence / 시퀀스) này, tài nguyên (resource / 자원)/calendar nào giới hạn thực thi (execution / 실행), và bất định (uncertainty / 불확실성) nào làm finish phân phối (distribution / 분포) thay đổi. Chỉ có ngày bắt đầu/kết thúc mà thiếu ba lớp đó thì schedule chưa phải quyết định (decision / 결정) mô hình (model / 모델).

## Milestone, activity và deliverable

Deliverable là đầu ra (output / 출력) có ý nghĩa. Activity là công việc (work / 작업) để tạo đầu ra (output / 출력). Milestone là điểm sự kiện quan trọng thường có zero duration trong schedule mô hình (model / 모델).

Nhầm ba lớp làm status méo. “Development 80%” là activity progress; “Đặc tả API (API contract / API 계약) accepted” là milestone; “integrated dịch vụ (service / 서비스)” là deliverable. Milestone thường hữu ích hơn percent-complete khi cần quyết định (decision / 결정) hoặc handoff.

Milestone tốt đại diện một chuyển tiếp trạng thái (state transition / 상태 전이) có bằng chứng (evidence / 증거), không chỉ một date đẹp. “Bảo mật (security / 보안) approval obtained” mạnh hơn “Bảo mật (security / 보안) rà soát (review / 검토) milestone” nếu người đọc biết điều kiện (condition / 조건) nào làm milestone complete.

## Từ phạm vi (scope / 범위) tới activity

Sau khi phạm vi (scope / 범위) được decompose, nhóm (team / 팀) xác định activity cần thực hiện, relationship giữa chúng và tài nguyên (resource / 자원)/effort. Phụ thuộc (dependency / 의존성) có thể bắt buộc về lô-gic (logic / 논리), đến từ đặc tả hợp đồng (contract / 계약)/regulation, hoặc chỉ do cách tổ chức chọn.

Finish-to-start là kiểu phổ biến: B chỉ bắt đầu sau A. Nhưng thực tế còn start-to-start, finish-to-finish và lag/lead. Điều quan trọng không phải nhớ tên mà hiểu ràng buộc (constraint / 제약조건) thật: “cái gì phải xảy ra trước khi cái khác có thể tiến?”.

Một phụ thuộc (dependency / 의존성) nên bị challenge nếu chỉ tồn tại vì habit. Nếu testing có thể bắt sớm hơn bằng partial increment, phụ thuộc (dependency / 의존성) “dev hoàn tất toàn bộ rồi mới kiểm thử (test / 테스트)” là organizational choice chứ không phải law tự nhiên.

## Lead và lag: dùng để mô hình reality, không để che thiếu activity

Lag biểu diễn waiting thời gian (time / 시간) giữa hai trạng thái (state / 상태); lead cho phép overlap. Ví dụ concrete curing cần 3 ngày chờ trước activity sau; đó là lag có vật lý (physical / 물리적) meaning. Nhưng nếu “đợi phê duyệt 5 ngày” thực chất là một tiến trình (process / 프로세스) có đơn vị sở hữu (owner / 오너) và công việc (work / 작업), biến nó thành lag có thể che accountability.

Một schedule khỏe ưu tiên mô hình (model / 모델) tường minh (explicit / 명시적) activity khi có công việc (work / 작업)/điều khiển (control / 제어) cần quản lý; lag phù hợp hơn với waiting thời gian (time / 시간) thật sự. Lead cũng không nên dùng để giả vờ parallelism khi downstream chưa có stable thông tin (information / 정보) để bắt đầu.

## Mandatory, discretionary và bên ngoài (external / 외부) phụ thuộc (dependency / 의존성)

Mandatory phụ thuộc (dependency / 의존성) đến từ vật lý (physical / 물리적)/technical lô-gic (logic / 논리). Discretionary phụ thuộc (dependency / 의존성) đến từ preferred chuỗi (sequence / 시퀀스) hoặc best practice. Bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) nằm ngoài direct điều khiển (control / 제어), như regulator approval hoặc vendor shipment.

Classification quan trọng vì khôi phục (recovery / 복구) option khác nhau. Mandatory phụ thuộc (dependency / 의존성) khó loại bỏ; discretionary có thể redesign; bên ngoài (external / 외부) cần lead thời gian (time / 시간), monitoring và escalation giao diện (interface / 인터페이스).

Bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) còn cần confidence và phản hồi (response / 응답) cửa sổ (window / 윈도우). “Regulator phản hồi trong tháng 11” khác “regulator có SLA 10 nghiệp vụ (business / 비즈니스) days”. Schedule cần phân biệt fact, giả định (assumption / 가정) và mục tiêu (target / 대상).

## Mạng (network / 네트워크) diagram như nhân quả (causal / 인과적) đồ thị (graph / 그래프)

Schedule mạng (network / 네트워크) không chỉ là hình để tính CPM. Nó là nhân quả (causal / 인과적) đồ thị (graph / 그래프) của finish-date lô-gic (logic / 논리). Khi một activity delay, đồ thị (graph / 그래프) cho biết impact truyền qua đâu.

Nếu nhóm (team / 팀) chỉ giữ danh sách (list / 목록) tác vụ (task / 작업) và due date mà không có phụ thuộc (dependency / 의존성) mô hình (model / 모델), họ khó biết tác vụ (task / 작업) nào thực sự trọng yếu (critical / 중요) và tác vụ (task / 작업) nào có slack.

Đồ thị (graph / 그래프) còn giúp phát hiện đường dẫn (path / 경로) convergence: nhiều đường dẫn (path / 경로) độc lập cùng đổ vào một milestone. Dù từng đường dẫn (path / 경로) có xác suất hoàn thành đúng hạn cao, milestone tổng có thể rủi ro hơn vì chỉ cần một đường dẫn (path / 경로) muộn là tích hợp (integration / 통합) muộn.

## Đường găng (critical path / 임계 경로)

Đường găng (critical path / 임계 경로) phương thức (method / 메서드) tìm chuỗi activity có total duration dài nhất qua mạng (network / 네트워크) và quyết định thời gian dự án (project / 프로젝트) tối thiểu theo mô hình (model / 모델) hiện tại. Activity trên đường găng (critical path / 임계 경로) có zero hoặc rất ít total float; delay ở đó có khả năng đẩy finish date nếu không có khôi phục (recovery / 복구) elsewhere.

Ví dụ có hai đường: A(3 ngày) → B(5) → D(2) = 10 ngày, và A(3) → C(2) → D(2) = 7 ngày. Đường A-B-D trọng yếu (critical / 중요). C có khoảng slack 3 ngày so với mạng (network / 네트워크) đơn giản này. Việc tăng tốc C không làm dự án (project / 프로젝트) kết thúc sớm hơn; muốn giảm duration cần tác động đường găng (critical path / 임계 경로).

Đường găng (critical path / 임계 경로) có thể thay đổi khi estimate hoặc phụ thuộc (dependency / 의존성) đổi. Vì vậy nó là động (dynamic / 동적) thuộc tính (property / 속성) của schedule mô hình (model / 모델).

## Near-critical đường dẫn (path / 경로) và criticality switching

Đường dẫn (path / 경로) có float rất nhỏ có thể trở thành trọng yếu (critical / 중요) sau một delay nhỏ. Trong dự án (project / 프로젝트) nhiều bất định (uncertainty / 불확실성), chỉ theo dõi một đường găng (critical path / 임계 경로) duy nhất tạo false bảo mật (security / 보안).

Near-critical đường dẫn (path / 경로) cần attention theo mức float và bất định (uncertainty / 불확실성). Một đường dẫn (path / 경로) có 2 ngày float nhưng estimate rất volatile có thể đáng quan tâm hơn đường găng (critical path / 임계 경로) ổn định. Khi simulation được dùng, criticality chỉ mục (index / 인덱스) có thể cho intuition activity/đường dẫn (path / 경로) xuất hiện trên đường găng (critical path / 임계 경로) trong bao nhiêu iteration; mục tiêu không phải học thêm chỉ số (metric / 지표) mà là hiểu criticality có thể thay đổi theo bất định (uncertainty / 불확실성).

## Criticality index và schedule sensitivity

Critical path trong một deterministic schedule chỉ trả lời “với bộ estimate hiện tại, đường nào có zero/lowest float?”. Khi duration là phân phối và nhiều path gần nhau, một path hôm nay không critical vẫn có thể trở thành critical trong nhiều kịch bản. **Criticality index** là trực giác xác suất cho câu hỏi đó: trong bao nhiêu simulated outcomes một activity/path nằm trên critical path?

Điểm quan trọng không phải thuộc một công thức mới mà là hiểu **schedule sensitivity**. Nếu path A critical trong 52% kịch bản và path B trong 44%, việc chỉ quản lý A như “đường găng thật” tạo false certainty. Hệ thống có hai path cạnh tranh; chỉ một biến động nhỏ về vendor, rework hoặc calendar có thể làm criticality switch.

Criticality index cũng không đồng nghĩa impact. Một activity có thể thường xuyên critical nhưng chỉ có variance nhỏ; activity khác ít khi critical nhưng khi nó trượt thì tạo tail rất lớn. Vì vậy khi ưu tiên attention nên đọc cùng ít nhất ba lớp: xác suất trở thành critical, độ lớn của delay nếu xảy ra và mức controllability của nguyên nhân.

Scenario PMP thường không đưa criticality index bằng số, nhưng reasoning vẫn áp dụng: nếu nhiều path “gần găng”, PM không nên chỉ bảo vệ path đang được tô đỏ trên Gantt. Hãy tìm common-cause dependency, convergence point và những activity có thể làm critical path đổi trạng thái.

> **Nối mạch:** Criticality index cho thấy critical path là một trạng thái có thể đổi dưới uncertainty; **Float** tiếp theo giải thích lượng schedule flexibility còn lại và vì sao positive float không đồng nghĩa “không cần quan tâm”.

## Float và việc hiểu đúng “không trọng yếu (critical / 중요)”

Total float là lượng delay một activity có thể chịu trước khi dự án (project / 프로젝트) finish bị ảnh hưởng theo hiện tại (current / 현재) mạng (network / 네트워크). Free float là lượng delay trước khi successor sớm nhất bị ảnh hưởng.

Activity không trọng yếu (critical / 중요) không có nghĩa không quan trọng. Float có thể bị consume dần và đường dẫn (path / 경로) gần trọng yếu (critical / 중요) có thể trở thành trọng yếu (critical / 중요) sau vài thay đổi (change / 변경). PM nên theo dõi near-critical đường dẫn (path / 경로) ở dự án (project / 프로젝트) có bất định (uncertainty / 불확실성) cao.

Float cũng không phải “ngân sách (budget / 예산) của activity đơn vị sở hữu (owner / 오너)”. Nếu nhiều upstream activity cùng tiêu cùng downstream slack, cục bộ (local / 로컬) nhóm (team / 팀) không thể giả định toàn bộ float thuộc riêng mình.

## Negative float

Negative float xuất hiện khi imposed date sớm hơn finish date mà mạng (network / 네트워크) hiện tại có thể đạt. Nó không phải phép thuật để schedule “ép” nhanh hơn; nó là tín hiệu (signal / 신호) rằng ràng buộc (constraint / 제약조건) và lô-gic (logic / 논리) đang xung đột (conflict / 충돌).

Nếu mạng (network / 네트워크) forecast 30/11 nhưng contractual milestone là 20/11, negative float 10 ngày cho biết cần thay phạm vi (scope / 범위), chuỗi (sequence / 시퀀스), tài nguyên (resource / 자원), ràng buộc (constraint / 제약조건) hoặc commitment. Chỉ đổi ngày trên Gantt không giải inconsistency.

Negative float nên trigger management conversation về feasibility chứ không trở thành lý do tự động ép overtime.

## Forward pass và backward pass

Forward pass tính earliest start/finish từ đầu mạng (network / 네트워크). Backward pass tính latest start/finish từ deadline hoặc finish date. Difference giữa latest và earliest tạo float.

Cơ chế quan trọng hơn arithmetic: forward pass hỏi “sớm nhất có thể xong khi phụ thuộc (dependency / 의존성) giữ nguyên là khi nào?”, backward pass hỏi “muộn nhất có thể làm mà chưa đẩy finish là khi nào?”. Worked example đầy đủ nằm ở [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md).

## Hard ràng buộc (constraint / 제약조건) và soft ràng buộc (constraint / 제약조건)

Không phải mọi ràng buộc (constraint / 제약조건) date đều ngang nhau. “Must finish on” do regulation có thể là hard ranh giới (boundary / 경계); “prefer finish before” để align nội bộ (internal / 내부) campaign là soft mục tiêu (target / 대상).

Hard ràng buộc (constraint / 제약조건) nên được dùng cẩn thận trong schedule công cụ (tool / 도구) vì nó có thể che lô-gic (logic / 논리) nếu planner ép date mà không giải phụ thuộc (dependency / 의존성). Soft ràng buộc (constraint / 제약조건) nên giữ visibility của forecast để management nhìn gap giữa mục tiêu (target / 대상) và khả năng hiện tại.

Ràng buộc (constraint / 제약조건) nguồn (source / 소스) luôn cần traceable: đặc tả hợp đồng (contract / 계약), law, sponsor mục tiêu (target / 대상), thị trường (market / 시장) cửa sổ (window / 윈도우) hay nội bộ (internal / 내부) preference.

## Calendar là một phần của lô-gic (logic / 논리)

Duration phụ thuộc calendar. 5 working days không đồng nghĩa 5 calendar days. Holiday, shift, regional calendar, vendor working hours và specialist availability đều làm earliest finish thay đổi.

Một toàn cục (global / 전역) dự án (project / 프로젝트) có thể mất một ngày ở mỗi handoff vì timezone/cutoff dù effort gần như không đổi. Nếu schedule công cụ (tool / 도구) dùng default calendar cho mọi activity, forecast có thể optimistic giả.

Tài nguyên (resource / 자원) calendar đặc biệt quan trọng với reviewer hoặc expert hiếm. Activity duration 2 giờ nhưng reviewer chỉ available thứ Sáu có thể tạo lead thời gian (time / 시간) gần một tuần.

## Estimate là phân phối (distribution / 분포), không phải số thật tuyệt đối

Estimate luôn dựa trên thông tin (information / 정보) chưa hoàn chỉnh. Một estimate “10 ngày” nên được hiểu như một forecast với confidence, các giả định (assumptions / 가정들) và phạm vi (range / 범위). Three-point estimation dùng optimistic, most likely và pessimistic để buộc ta nghĩ về bất định (uncertainty / 불확실성).

PERT thường dùng expected duration:

```text
E = (O + 4M + P) / 6
```

Nếu O=4, M=7, P=16 thì E=(4+28+16)/6=8 ngày. Formula không biến bất định (uncertainty / 불확실성) thành certainty; nó chỉ tạo một summary có trọng số. Nếu đầu vào (input / 입력) là guess không có lập luận (reasoning / 추론), đầu ra (output / 출력) vẫn là guess có thêm decimal.

Analogous estimation nhanh khi có historical comparable. Parametric estimation dùng tỷ lệ (rate / 비율) như “giờ mỗi di chuyển (migration / 마이그레이션) bản ghi (record / 레코드)”. Bottom-up estimate chi tiết hơn nhưng tốn effort và vẫn bị aggregation lỗi (error / 오류).

## Estimate effort và duration khác nhau

Effort là lượng công việc (work / 작업), ví dụ 40 person-hours. Duration là calendar thời gian (time / 시간) để hoàn tất, có thể dài hơn hoặc ngắn hơn tùy tài nguyên (resource / 자원), parallelism, calendar và phụ thuộc (dependency / 의존성).

40 giờ effort không tự động là 5 ngày duration. Nếu chuyên gia chỉ available 50%, hoặc công việc (work / 작업) phải chờ rà soát (review / 검토), duration tăng. Đây là lỗi phổ biến khi convert estimate cơ học.

Parallelism cũng có giới hạn. Hai người không luôn giảm duration một nửa vì communication, indivisible công việc (work / 작업) hoặc dùng chung (shared / 공유) môi trường (environment / 환경).

## Estimate bất định (uncertainty / 불확실성) có nhiều nguồn

Bất định (uncertainty / 불확실성) không chỉ đến từ “không biết effort”. Nó có thể đến từ yêu cầu (requirement / 요구사항) ambiguity, technical novelty, bên ngoài (external / 외부) approval, tài nguyên (resource / 자원) availability, hàng đợi (queue / 큐) thời gian (time / 시간), defect/rework và sự kiện (event / 이벤트) rủi ro (risk / 위험).

Hai activity cùng điểm (point / 지점) estimate 5 ngày nhưng bất định (uncertainty / 불확실성) profile khác nhau. Một activity routine có phạm vi (range / 범위) 4–6; một tích hợp (integration / 통합) mới có phạm vi (range / 범위) 2–15. Schedule nên attention vào variance/tail, không chỉ mean.

## Historical dữ liệu (data / 데이터) và tham chiếu (reference / 참조) lớp (class / 클래스) forecasting

Estimate nội bộ dễ bị optimism độ lệch (bias / 편향). Tham chiếu (reference / 참조) lớp (class / 클래스) forecasting nhìn các dự án (project / 프로젝트)/công việc (work / 작업) item tương tự trong lịch sử để tạo cơ sở (base / 기반) tỷ lệ (rate / 비율).

Nếu 20 di chuyển (migration / 마이그레이션) tương tự có median 8 ngày và P80 13 ngày, forecast nên bắt đầu từ bằng chứng (evidence / 증거) đó rồi adjust theo difference, thay vì hỏi đơn vị sở hữu (owner / 오너) “bạn nghĩ mấy ngày?”. Historical dữ liệu (data / 데이터) không hoàn hảo nhưng giúp anchor vào reality.

Tham chiếu (reference / 참조) lớp (class / 클래스) cần đủ tương đồng. Dùng lịch sử (history / 이력) của tính năng (feature / 기능) nhỏ để forecast regulatory di chuyển (migration / 마이그레이션) lớn có thể tạo precision giả. Cơ sở (base / 기반) tỷ lệ (rate / 비율) là starting điểm (point / 지점), không phải replacement cho ngữ cảnh (context / 맥락).

## Confidence và probabilistic forecast

Một deterministic date dễ bị hiểu thành guarantee. Khi bất định (uncertainty / 불확실성) material, forecast có thể dùng confidence như P50 hoặc P80.

P80 date nghĩa theo mô hình (model / 모델) và giả định (assumption / 가정) hiện tại có khoảng 80% simulated kết quả (outcome / 결과) hoàn tất trước hoặc tại date đó, không phải “80% dự án (project / 프로젝트) đã xong”. Confidence phải đi kèm mô hình (model / 모델) caveat.

Monte Carlo schedule simulation có thể aggregate duration phân phối (distribution / 분포) và phụ thuộc (dependency / 의존성) để nhìn finish-date phân phối (distribution / 분포). PMP learner không cần mã (code / 코드) simulation để hiểu mô hình tư duy (mental model / 사고 모델): đầu ra (output / 출력) nên là phạm vi (range / 범위)/xác suất (probability / 확률), không phải một ngày thần kỳ.

## Đường dẫn (path / 경로) convergence và merge độ lệch (bias / 편향)

Khi nhiều parallel đường dẫn (path / 경로) hội tụ, milestone chỉ hoàn thành khi tất cả đầu vào (input / 입력) sẵn sàng. Nếu mỗi đường dẫn (path / 경로) “thường đúng hạn”, tích hợp (integration / 통합) milestone vẫn có tail rủi ro (risk / 위험) cao hơn từng đường dẫn (path / 경로) riêng.

Đây là merge độ lệch (bias / 편향) intuition: bất định (uncertainty / 불확실성) không average đơn giản ở điểm hội tụ; late tail của bất kỳ đường dẫn (path / 경로) nào có thể kéo milestone. Vì vậy tích hợp (integration / 통합)/kiểm thử (test / 테스트) milestone thường cần attention đặc biệt, nhất là khi nhiều vendor/workstream hội tụ gần deadline.

Một schedule quá optimistic thường xuất hiện khi planner cộng average duration nhưng bỏ correlation và convergence.

## Correlation trong schedule rủi ro (risk / 위험)

Activity không luôn độc lập. Nhiều tác vụ (task / 작업) cùng phụ thuộc một vendor, một môi trường (environment / 환경) hoặc một expert. Nếu dùng chung (shared / 공유) phụ thuộc (dependency / 의존성) chậm, nhiều duration cùng tăng.

Simulation giả độc lập có thể đánh giá thấp tail. Ánh xạ (mapping / 매핑) common-cause phụ thuộc (dependency / 의존성) giúp forecast thực tế hơn và cũng gợi ý phản hồi (response / 응답): thêm buffer vào từng tác vụ (task / 작업) không bằng giảm dùng chung (shared / 공유) miền lỗi (failure domain / 장애 도메인).

## Tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건) và trọng yếu (critical / 중요) chuỗi (chain / 사슬) intuition

Mạng (network / 네트워크) lô-gic (logic / 논리) không phải ràng buộc (constraint / 제약조건) duy nhất. Hai activity có thể độc lập nhưng dùng cùng một chuyên gia. Nếu tài nguyên (resource / 자원) chỉ làm được một việc tại một thời điểm, schedule phải phản ánh tài nguyên (resource / 자원) leveling/smoothing. Đây là lý do đường găng (critical path / 임계 경로) trên lô-gic (logic / 논리) đồ thị (graph / 그래프) có thể chưa đủ để dự đoán thực tế.

Tài nguyên (resource / 자원) leveling có thể đổi đường găng (critical path / 임계 경로) và finish date. Tài nguyên (resource / 자원) smoothing cố dùng float để cân tài nguyên (resource / 자원) mà không đổi đường găng (critical path / 임계 경로)/finish nếu có thể.

Trọng yếu (critical / 중요) chuỗi (chain / 사슬) intuition nhấn mạnh tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건) và buffer. Điểm đáng hiểu là bảo vệ luồng (flow / 흐름) ở hệ thống (system / 시스템) mức (level / 수준) thay vì nhét an toàn (safety / 안전) margin bí mật vào từng tác vụ (task / 작업).

## Tài nguyên (resource / 자원) contention và multitasking chi phí (cost / 비용)

Một specialist chạy ba dự án (project / 프로젝트) song song không tạo 300% sức chứa (capacity / 용량). Ngữ cảnh (context / 맥락) switching, hàng đợi (queue / 큐) và priority xung đột (conflict / 충돌) làm elapsed duration tăng.

Schedule nên phản ánh allocation thực tế thay vì giả mỗi dự án (project / 프로젝트) có full tài nguyên (resource / 자원). Nếu portfolio không resolve contention, từng PM có thể có schedule “feasible” riêng nhưng toàn organization thì không feasible.

Tài nguyên (resource / 자원) contention là điểm nối trực tiếp giữa dự án (project / 프로젝트) schedule và portfolio quản trị (governance / 거버넌스).

## Student syndrome và Parkinson-like hành vi (behavior / 동작)

Khi mỗi tác vụ (task / 작업) có buffer riêng nhưng deadline được coi như mục tiêu (target / 대상), công việc (work / 작업) có xu hướng bắt đầu muộn hoặc expand tới available thời gian (time / 시간). Buffer bị tiêu thụ mà không bảo vệ dự án (project / 프로젝트) finish.

Hệ thống (system / 시스템) buffer rõ và early-finish handoff có thể tạo visibility tốt hơn hidden padding, dù hiện thực (implementation / 구현) cụ thể tùy methodology.

## Crashing và fast tracking

Crashing thêm tài nguyên (resource / 자원) hoặc chi phí để giảm duration của trọng yếu (critical / 중요) activities khi có thể. Fast tracking chạy overlap các việc vốn chuỗi (sequence / 시퀀스) để rút thời gian nhưng tăng coordination/rework rủi ro (risk / 위험). Không phải activity nào cũng compress được; chín phụ nữ không thể tạo một em bé trong một tháng là intuition kinh điển cho non-parallelizable công việc (work / 작업).

Crashing chỉ có giá trị (value / 값) khi activity nằm trên đường găng (critical path / 임계 경로) hoặc đường dẫn (path / 경로) có khả năng trở thành trọng yếu (critical / 중요). Thêm người vào noncritical tác vụ (task / 작업) không rút dự án (project / 프로젝트) finish.

Fast tracking hiệu quả khi downstream có thể bắt với partial stable thông tin (information / 정보). Nếu upstream bất định (uncertainty / 불확실성) cao, overlap có thể tạo rework lớn hơn thời gian (time / 시간) saved.

## Compression có diminishing return

Khi schedule bị compress dần, option rẻ thường được dùng trước. Sau đó mỗi ngày rút thêm có thể đắt hơn và riskier hơn.

Crashing một activity có thể làm đường dẫn (path / 경로) khác trở thành trọng yếu (critical / 중요); fast tracking có thể tăng defect/rework. Vì vậy schedule compression cần re-run mạng (network / 네트워크)/rủi ro (risk / 위험) lập luận (reasoning / 추론) sau mỗi significant thay đổi (change / 변경), không giả benefit tuyến tính.

## Deadline, mục tiêu (target / 대상) date và ràng buộc (constraint / 제약조건) khác nhau

Một date có thể là aspirational mục tiêu (target / 대상), contractual milestone, regulatory deadline hoặc technical phụ thuộc (dependency / 의존성). Chúng không có cùng flexibility.

Nếu nhóm (team / 팀) đối xử mục tiêu (target / 대상) nội bộ như legal deadline, họ có thể nhận rủi ro (risk / 위험) không cần thiết. Ngược lại, coi regulatory deadline như estimate có thể gây compliance thất bại (failure / 실패). Schedule lập luận (reasoning / 추론) phải hiểu nguồn (source / 소스) của ràng buộc (constraint / 제약조건).

## Forecast date, target date và committed date

Một nguồn conflict lớn trong schedule là dùng cùng một ngày để biểu diễn ba ý nghĩa khác nhau. **Forecast date** là ngày mô hình hiện tại dự đoán có thể hoàn thành dựa trên evidence và uncertainty. **Target date** là ngày organization muốn đạt để tối ưu value hoặc alignment. **Committed date** là ngày đã trở thành promise/obligation với stakeholder, contract, regulator hoặc downstream operation.

Ba ngày có thể trùng nhau, nhưng không nên giả định chúng luôn giống nhau. Nếu P80 forecast là 30/6 nhưng management đặt target 20/6, khoảng cách đó là một **management challenge**, không phải bằng chứng dự án sẽ xong 20/6. Nếu sales đã cam kết 20/6 với khách hàng, challenge đã biến thành commitment risk; PM cần làm visible probability, recovery options và consequence thay vì sửa estimate để “khớp ngày đã hứa”.

Ngược lại, forecast trễ hơn target không tự động yêu cầu escalation nếu target chỉ là stretch goal và tolerance cho phép. Câu hỏi đúng là: ngày nào thuộc model, ngày nào thuộc preference, ngày nào thuộc obligation; authority nào có thể đổi từng loại ngày; và consequence khi miss là gì.

Phân biệt semantic này giúp tránh **date laundering**: target được trình bày như forecast, rồi forecast lại bị đối xử như guarantee. Một schedule governance tốt giữ provenance của từng date và cập nhật stakeholder khi confidence thay đổi material.

> **Nối mạch:** Forecast/target/commitment tách prediction khỏi preference và obligation; **external window** tiếp theo cho thấy một số commitment còn bị khóa bởi calendar bên ngoài nên cost của miss có thể phi tuyến.

## Bên ngoài (external / 외부) cửa sổ (window / 윈도우) và cadence mismatch

Một dự án (project / 프로젝트) có thể nội bộ (internal / 내부) cadence nhanh nhưng phụ thuộc cửa sổ (window / 윈도우) hiếm: regulator kiểm thử (test / 테스트) mỗi tháng, vendor cutover mỗi quý, dữ liệu (data / 데이터) center maintenance mỗi cuối tuần.

Nếu miss một 2-hour cửa sổ (window / 윈도우), effective delay có thể là cả tháng. Schedule nên mô hình (model / 모델) calendar/cửa sổ (window / 윈도우) như real ràng buộc (constraint / 제약조건), không chỉ activity duration.

Đây là lý do “tác vụ (task / 작업) chỉ trễ một ngày” đôi khi gây impact rất lớn khi nó bỏ lỡ fixed tích hợp (integration / 통합) cửa sổ (window / 윈도우).

## Schedule reserve và buffer

Bất định (uncertainty / 불확실성) nên được visible ở hệ thống (system / 시스템) mức (level / 수준). Buffer có thể bảo vệ milestone, tích hợp (integration / 통합) cửa sổ (window / 윈도우) hoặc bản phát hành (release / 릴리스).

Buffer không phải lý do để slack công việc (work / 작업) vô hạn. Nó là rủi ro (risk / 위험) sức chứa (capacity / 용량) có trigger và đơn vị sở hữu (owner / 오너). Khi buffer burn nhanh hơn progress, đó là early warning tín hiệu (signal / 신호).

Buffer consumption nên được đọc cùng bất định (uncertainty / 불확실성) retired. Dùng 50% buffer nhưng đã retire 90% major rủi ro (risk / 위험) khác với dùng 50% buffer khi mới hoàn thành 20% uncertain công việc (work / 작업).

## Buffer consumption phải được đọc cùng progress

Reserve hoặc project buffer không nên được đọc như “số ngày còn dư”. Ý nghĩa của buffer chỉ rõ khi so **buffer consumption** với mức progress của chuỗi công việc mà buffer đang bảo vệ. Nếu 20% công việc bảo vệ đã hoàn tất nhưng 70% buffer đã bị consume, hệ thống đang đốt protection nhanh hơn tốc độ tạo progress; đây là tín hiệu sớm mạnh hơn việc chỉ nhìn finish date hiện tại.

Ngược lại, buffer đã dùng nhiều không nhất thiết xấu nếu phần uncertainty lớn nhất đã được retired. Ví dụ integration spike khó nhất đã qua, remaining work routine hơn và estimate distribution đã hẹp lại. Vì vậy buffer burn cần nối với **risk retirement**, không chỉ elapsed time.

Một cách đọc trực giác là đặt hai tỷ lệ cạnh nhau:

```text
work/protection progress  vs  buffer consumed
```

Nếu buffer consumption tăng nhanh hơn progress qua nhiều review cycle, PM cần tìm cơ chế: estimate bias, rework, resource contention, hidden queue hay common-cause risk. Phản ứng đúng có thể là giảm WIP, xử lý bottleneck hoặc thay sequencing; “cắt thêm buffer” chỉ làm dashboard đẹp hơn.

Trong predictive context, buffer giúp bảo vệ milestone/system-level date. Trong adaptive flow, cùng mental model xuất hiện dưới dạng service-level expectation, cycle-time percentile hoặc capacity slack. Tên công cụ khác nhau nhưng invariant giống nhau: uncertainty cần protection ở cấp hệ thống, và protection phải được quản lý bằng evidence.

> **Nối mạch:** Buffer burn nối uncertainty với risk retirement; **Adaptive flow** tiếp theo chuyển cùng logic bảo vệ hệ thống từ network schedule sang throughput, WIP và cycle time.

## Adaptive luồng (flow / 흐름): velocity không phải productivity tuyệt đối

Trong adaptive delivery, planning thường dùng backlog, story points, thông lượng (throughput / 처리량), cycle thời gian (time / 시간) và velocity. Story điểm (point / 지점) là relative sizing trong một nhóm (team / 팀)/ngữ cảnh (context / 맥락); không nên dùng để so hiệu suất giữa nhóm (team / 팀) hoặc ép “tăng productivity”. Khi biến điểm (point / 지점) thành KPI thưởng/phạt, Goodhart's Law khiến chỉ số (metric / 지표) bị game.

Luồng (flow / 흐름) metrics giúp nhìn hệ thống (system / 시스템): công việc (work / 작업) in progress cao thường kéo cycle thời gian (time / 시간) dài. Little's Law trong steady-state cho intuition:

```text
WIP ≈ Throughput × Cycle Time
```

Nếu trung bình 20 item đang mở và hoàn thành 5 item/tuần, cycle thời gian (time / 시간) trung bình xấp xỉ 4 tuần. Giảm WIP có thể cải thiện phản hồi (feedback / 피드백) nhanh hơn mà không cần “làm nhanh hơn” từng người.

## Little's Law các giả định (assumptions / 가정들)

Little's Law là relationship dài hạn trong stable luồng (flow / 흐름), không phải magic formula cho mọi snapshot. Arrival/completion hệ thống (system / 시스템) cần đủ ổn định trong period đo và đơn vị (unit / 단위) phải consistent.

Nếu phạm vi (scope / 범위) inflow tăng đột biến hoặc backlog không bounded, dùng formula từ một tuần dữ liệu có thể gây kết luận sai. Mô hình tư duy (mental model / 사고 모델) là WIP, thông lượng (throughput / 처리량) và cycle thời gian (time / 시간) ràng buộc nhau trong luồng (flow / 흐름) hệ thống (system / 시스템).

## Queueing và utilization

Khi tài nguyên (resource / 자원) utilization tiến gần 100%, hàng đợi (queue / 큐) thường tăng mạnh vì không còn slack hấp thụ variation. Đây là lý do “mọi người phải luôn bận” có thể làm lead thời gian (time / 시간) tệ hơn.

Một reviewer có 100% calendar booked tạo hàng đợi (queue / 큐) cho mọi approval. Hệ thống (system / 시스템) cần sức chứa (capacity / 용량) margin ở bottleneck để luồng (flow / 흐름) ổn định.

Hàng đợi (queue / 큐) thời gian (time / 시간) thường lớn hơn touch thời gian (time / 시간). Một thay đổi (change / 변경) yêu cầu (request / 요청) có 2 giờ phân tích (analysis / 분석) nhưng chờ 8 ngày approval; tối ưu analyst 10% không cải thiện lead thời gian (time / 시간) đáng kể.

## Bottleneck và Lý thuyết (theory / 이론) of Các ràng buộc (constraints / 제약조건들) intuition

Thông lượng (throughput / 처리량) toàn hệ thống (system / 시스템) bị giới hạn bởi ràng buộc (constraint / 제약조건)/bottleneck. Tối ưu non-bottleneck có thể chỉ tạo inventory trước bottleneck.

Nếu QA là bottleneck, tăng coding thông lượng (throughput / 처리량) có thể làm WIP và cycle thời gian (time / 시간) tăng. Cần exploit/elevate bottleneck hoặc giảm demand trước nó.

Bottleneck có thể di chuyển sau khi được cải thiện. Vì vậy tối ưu hóa (optimization / 최적화) là vòng lặp (loop / 루프), không phải one-time fix.

## Schedule, finance và rủi ro (risk / 위험) là ba projection của cùng một future trạng thái (state / 상태)

Schedule delay hiếm khi chỉ là vấn đề ngày tháng. Một milestone trượt có thể làm payment milestone trượt, kéo cash inflow sang kỳ sau, tăng burn, kéo dài thuê vendor/tài nguyên (resource / 자원) và làm rủi ro (risk / 위험) exposure tồn tại lâu hơn. Ngược lại, funding bị cắt có thể làm tài nguyên (resource / 자원) giảm, hàng đợi (queue / 큐) tăng và đường găng (critical path / 임계 경로) đổi. Vì vậy schedule, finance và rủi ro (risk / 위험) phải được đọc như các projection liên kết của cùng dự án (project / 프로젝트) trạng thái (state / 상태).

Ví dụ một cutover trễ ba ngày nhưng bỏ lỡ monthly regulatory cửa sổ (window / 윈도우) có thể tạo delay thực tế bốn tuần. Bốn tuần đó không chỉ làm finish date đổi: nhóm (team / 팀) phải duy trì môi trường (environment / 환경) thêm một tháng, vendor hỗ trợ (support / 지원) kéo dài, benefit realization lùi, contingency exposure tăng và có thể chạm contractual penalty. Cục bộ (local / 로컬) schedule variance nhỏ đã trở thành economic/rủi ro (risk / 위험) discontinuity lớn.

Khi forecast date đổi material, PM nên hỏi ít nhất ba propagation question: cash/funding trạng thái (state / 상태) nào đổi, rủi ro (risk / 위험) nào tồn tại lâu hơn hoặc mới xuất hiện, và commitment nào với stakeholder/vendor phải được cập nhật. Đây là điểm nối trực tiếp với [Finance & Value](./06_finance_cost_and_value_measurement.md), [Risk & Decisions](./08_risk_uncertainty_issues_and_decisions.md) và [Integration & Scope](./04_integration_scope_requirements_and_change.md).

## Forecast divergence: khi nhiều chỉ số (metric / 지표) kể các câu chuyện khác nhau

Một schedule có thể báo finish date ổn định trong khi SPI xấu; velocity có thể tăng nhưng milestone forecast vẫn trượt; percent complete có thể cao trong khi acceptance bằng chứng (evidence / 증거) thấp. Không nên ép các chỉ số (metric / 지표) phải “khớp” bằng cách chọn một con số làm sự thật duy nhất. Trước hết phải xác định chúng đo trạng thái (state / 상태) nào.

SPI nhìn hiệu năng (performance / 성능) so với baseline trong phần công việc (work / 작업) được đo; critical-path forecast nhìn lô-gic (logic / 논리) còn lại; thông lượng (throughput / 처리량)/cycle thời gian (time / 시간) nhìn luồng (flow / 흐름); milestone bằng chứng (evidence / 증거) nhìn chuyển tiếp trạng thái (state transition / 상태 전이). Nếu SPI thấp vì công việc (work / 작업) noncritical bị chậm nhưng đường găng (critical path / 임계 경로) vẫn ổn, finish forecast có thể chưa đổi. Ngược lại SPI gần 1 vẫn có thể che một regulatory phụ thuộc (dependency / 의존성) mới chưa được baseline/mô hình (model / 모델) phản ánh.

Divergence là diagnostic tín hiệu (signal / 신호). PM cần giải thích nhân quả (causal / 인과적) cầu nối (bridge / 브리지) giữa chỉ số (metric / 지표) và forecast: chỉ số (metric / 지표) nào là leading tín hiệu (signal / 신호), chỉ số (metric / 지표) nào lagging, ranh giới (boundary / 경계) nào không được mô hình (model / 모델) hóa, và bằng chứng (evidence / 증거) nào đủ mạnh để cập nhật (update / 업데이트) remaining duration. Cross-metric consistency được đào sâu thêm ở [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md).

## Khôi phục (recovery / 복구) option phải được đánh giá theo marginal economics và reversibility

Khi forecast trượt, câu hỏi không phải luôn là “làm sao lấy lại ngày cũ?”. Khôi phục (recovery / 복구) chỉ có lý khi giá trị (value / 값) của việc giữ date lớn hơn marginal chi phí (cost / 비용) và rủi ro (risk / 위험) của khôi phục (recovery / 복구). Crashing có thể mua thêm sức chứa (capacity / 용량); fast tracking có thể mua thời gian (time / 시간) bằng rework rủi ro (risk / 위험); de-scope có thể giữ date bằng cách giảm giá trị (value / 값); đổi chuỗi (sequence / 시퀀스) có thể giữ option nhưng tăng coordination.

Quyết định (decision / 결정) ranh giới (boundary / 경계) thay đổi theo loại date. Với regulatory deadline không thể dời, organization có thể chấp nhận khôi phục (recovery / 복구) chi phí (cost / 비용) cao hơn nhưng vẫn không được phá an toàn (safety / 안전)/compliance ranh giới (boundary / 경계). Với nội bộ (internal / 내부) mục tiêu (target / 대상) có flexibility, overtime kéo dài hoặc chất lượng (quality / 품질) compromise để giữ một ngày tượng trưng có thể là cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화). Với thị trường (market / 시장) cửa sổ (window / 윈도우), giá trị (value / 값) của một ngày có thể phi tuyến nếu miss cửa sổ (window / 윈도우) làm mất cả mùa bán hàng.

Một khôi phục (recovery / 복구) quyết định (decision / 결정) tốt vì vậy so sánh ít nhất `time saved`, `marginal cost`, `new risk`, `quality/rework consequence`, `resource sustainability` và `value protected`. Sau khôi phục (recovery / 복구), mạng (network / 네트워크) phải được tính lại vì bottleneck/đường găng (critical path / 임계 경로) có thể đã chuyển sang nơi khác.

## Thất bại (failure / 실패) cascade: delay có thể tự khuếch đại

Schedule thất bại (failure / 실패) thường lan qua vòng phản hồi (feedback loop / 피드백 루프) thay vì dừng ở một tác vụ (task / 작업). Một vendor trễ làm tích hợp (integration / 통합) trễ; tích hợp (integration / 통합) trễ bỏ lỡ kiểm thử (test / 테스트) cửa sổ (window / 윈도우); kiểm thử (test / 테스트) cửa sổ (window / 윈도우) trễ làm acceptance/payment trễ; cash pressure khiến organization trì hoãn bên ngoài (external / 외부) specialist; specialist thiếu lại làm remediation chậm hơn. Đây là reinforcing vòng lặp (loop / 루프) khiến một variance ban đầu nhỏ trở thành dự án (project / 프로젝트) khôi phục (recovery / 복구) bài toán (problem / 문제).

Cách ngắt cascade không nhất thiết là tăng tốc activity đầu tiên. Có thể cần giữ kiểm thử (test / 테스트) cửa sổ (window / 윈도우) bằng partial phạm vi (scope / 범위), thay payment cấu trúc (structure / 구조), mua temporary sức chứa (capacity / 용량), đổi chuỗi (sequence / 시퀀스) hoặc negotiate giao diện (interface / 인터페이스). Gốc (root / 루트) hành động (action / 동작) phải đánh vào propagation cơ chế (mechanism / 메커니즘) đang khuếch đại delay.

Một dấu hiệu quan trọng là **schedule consequence đã vượt ranh giới (boundary / 경계) của schedule**: finance forecast đổi, reserve bị consume, đặc tả hợp đồng (contract / 계약) exposure tăng, benefit date đổi hoặc quản trị (governance / 거버넌스) tolerance bị breach. Khi đó issue phải được xử lý bằng integrated quyết định (decision / 결정), không còn là việc planner chỉnh Gantt.

## Schedule health: lô-gic (logic / 논리) trước màu status

Một schedule “green” có thể unhealthy nếu thiếu predecessor/successor, dùng quá nhiều hard ràng buộc (constraint / 제약조건), có activity dài hàng tháng không milestone, hoặc không phản ánh tài nguyên (resource / 자원) calendar.

Health kiểm tra (audit / 감사) nên hỏi: công việc (work / 작업) có lô-gic (logic / 논리) link đủ không, ràng buộc (constraint / 제약조건) có nguồn (source / 소스) rõ không, negative float có được hiểu không, near-critical đường dẫn (path / 경로) nào tồn tại, bên ngoài (external / 외부) cửa sổ (window / 윈도우) nào quyết định, estimate nào stale, tài nguyên (resource / 자원) nào overallocated và actual progress có bằng chứng (evidence / 증거) không.

Một Gantt chart đẹp không chứng minh schedule mô hình (model / 모델) tốt.

## Open ends và dangling activities

Activity không có predecessor hoặc successor ngoài start/finish lô-gic (logic / 논리) có thể là intentional, nhưng cũng có thể là broken mạng (network / 네트워크). Nếu một tác vụ (task / 작업) có due date nhưng không link tới dự án (project / 프로젝트) finish, delay của nó không propagate trong mô hình (model / 모델).

Schedule kiểm tra (audit / 감사) cần phân biệt genuine independent công việc (work / 작업) với missing phụ thuộc (dependency / 의존성). Broken lô-gic (logic / 논리) tạo false float và false đường găng (critical path / 임계 경로).

## Progress đo lường (measurement / 측정) và remaining duration

Percent complete không tự động suy ra remaining duration. Một tác vụ (task / 작업) “90% done” có thể còn phần tích hợp (integration / 통합) khó nhất.

Forecast nên cập nhật (update / 업데이트) remaining duration dựa trên bằng chứng (evidence / 증거), không tính cơ học `original duration × (1 - %complete)`. Khi kiến thức (knowledge / 지식) tăng, remaining estimate có thể tăng dù percent complete cao.

## Schedule variance và forecast

Một deviation không tự nói nguyên nhân. PM cần hỏi: đây là random variation hay systematic bài toán (problem / 문제), tác vụ (task / 작업) có trọng yếu (critical / 중요) không, downstream phụ thuộc (dependency / 의존성) nào bị tác động, khôi phục (recovery / 복구) option nào tồn tại, và bất định (uncertainty / 불확실성) mới làm forecast đổi bao nhiêu.

Schedule report tốt nên cập nhật (update / 업데이트) forecast, không chỉ báo variance quá khứ. Stakeholder cần biết “nếu hiện tại (current / 현재) trend tiếp tục thì sao?”.

## Progress đo lường (measurement / 측정) pitfalls

Percent complete dễ subjective. “90% done” có thể tồn tại nhiều tuần. Deliverable-based milestone hoặc mục tiêu (objective / 목표) acceptance bằng chứng (evidence / 증거) thường đáng tin hơn effort-consumed percentage.

Mức (level / 수준) of effort công việc (work / 작업) như management/hỗ trợ (support / 지원) không nên tạo earned progress giống discrete deliverable nếu không có lô-gic (logic / 논리) phù hợp.

## Ví dụ lập luận (reasoning / 추론)

Một dự án (project / 프로젝트) có tác vụ (task / 작업) coding trễ 3 ngày nhưng activity có float 7 ngày. PM không nên ngay lập tức crash. Trước hết xem float, near-critical đường dẫn (path / 경로) và downstream tài nguyên (resource / 자원). Nếu testing đường dẫn (path / 경로) khác đã trọng yếu (critical / 중요), thêm tài nguyên (resource / 자원) vào coding có thể không thay finish date.

Một adaptive nhóm (team / 팀) có thông lượng (throughput / 처리량) ổn 8 item/tuần nhưng cycle thời gian (time / 시간) tăng từ 5 lên 12 ngày. Nếu WIP tăng mạnh, issue có thể là quá nhiều công việc (work / 작업) started. Hành động (action / 동작) hợp lý là giảm WIP và inspect hàng đợi (queue / 큐) trước khi kết luận nhóm (team / 팀) “làm chậm”.

Một dự án (project / 프로젝트) khác có ba parallel workstream cùng cần bảo mật (security / 보안) approval trước go-live. Mỗi workstream riêng lẻ có P80 đúng hạn, nhưng tất cả hội tụ vào một approval cửa sổ (window / 윈도우) duy nhất. PM cần nhìn convergence/common-cause reviewer sức chứa (capacity / 용량) thay vì cộng confidence từng đường dẫn (path / 경로) như độc lập.

Một scenario khác có finish forecast trượt năm ngày. Sponsor yêu cầu overtime để “lấy lại schedule”, nhưng date chỉ là nội bộ (internal / 내부) mục tiêu (target / 대상); khôi phục (recovery / 복구) cần thêm 40 triệu, tăng defect rủi ro (risk / 위험) và không bảo vệ revenue cửa sổ (window / 윈도우) nào. Trong trường hợp này, câu hỏi đúng không phải nhóm (team / 팀) có thể ép năm ngày hay không mà là năm ngày đó đáng giá bao nhiêu và consequence của khôi phục (recovery / 복구) là gì. Nếu ngược lại năm ngày làm miss annual regulatory cửa sổ (window / 윈도우), quyết định (decision / 결정) ranh giới (boundary / 경계) thay đổi hoàn toàn.

## Thất bại (failure / 실패) modes

Date-driven scheduling xảy ra khi planner đặt ngày trước rồi ép lô-gic (logic / 논리) theo. Ràng buộc (constraint / 제약조건) masking xảy ra khi hard ràng buộc (constraint / 제약조건) che infeasible mạng (network / 네트워크). Tài nguyên (resource / 자원) fantasy xảy ra khi cùng specialist được booking full-time ở nhiều activity. Merge blindness bỏ qua tail ở convergence điểm (point / 지점). Open-end mạng (network / 네트워크) tạo false float. Percent-complete theater báo tiến độ mà không cập nhật (update / 업데이트) remaining duration.

Chỉ số (metric / 지표) isolation xảy ra khi SPI, velocity hoặc percent complete được dùng tách khỏi mạng (network / 네트워크)/bằng chứng (evidence / 증거). Khôi phục (recovery / 복구) reflex xảy ra khi mọi variance đều bị crash/fast-track mà không so marginal giá trị (value / 값) với chi phí (cost / 비용)/rủi ro (risk / 위험). Schedule silo xảy ra khi date đổi nhưng finance, rủi ro (risk / 위험), đặc tả hợp đồng (contract / 계약) và benefit forecast không đổi theo. Cascade blindness xảy ra khi management nhìn delay one-hop mà bỏ vòng phản hồi (feedback loop / 피드백 루프) làm consequence tự khuếch đại.

Schedule management trưởng thành không cố làm mọi activity “đúng ngày”; nó giữ mô hình (model / 모델) nhân quả (causal / 인과적) đủ thật để forecast và sự đánh đổi (trade-off / 트레이드오프) còn đáng tin.

## Mô hình tư duy (mental model / 사고 모델)

> Schedule là nhân quả (causal / 인과적) mô hình (model / 모델) của phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원), calendar, hàng đợi (queue / 큐) và bất định (uncertainty / 불확실성). Quản lý schedule tốt là biết đường dẫn (path / 경로)/cửa sổ (window / 윈도우)/tài nguyên (resource / 자원) nào thật sự quyết định kết quả (outcome / 결과), nhận ra khi ràng buộc (constraint / 제약조건) làm mô hình (model / 모델) infeasible, đọc schedule cùng finance/rủi ro (risk / 위험) trạng thái (state / 상태), và chỉ mua khôi phục (recovery / 복구) khi giá trị (value / 값) được bảo vệ lớn hơn chi phí (cost / 비용)/rủi ro (risk / 위험) mới tạo ra.

Tiếp theo: [Finance, cost, reserves và value measurement](./06_finance_cost_and_value_measurement.md).
