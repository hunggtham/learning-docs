# 03 — Stakeholder, communication và kiến thức (knowledge / 지식) transfer

> **Mạch đọc:** Đặt **03 — Stakeholder, communication và kiến thức (knowledge / 지식) transfer** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Stakeholder management không phải danh sách người nhận email** sang **Stakeholder hệ thống (system / 시스템) là mạng (network / 네트워크), không phải danh sách độc lập**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## Stakeholder management không phải danh sách người nhận email

Bên liên quan (stakeholder / 이해관계자) là cá nhân, nhóm hoặc tổ chức có thể ảnh hưởng, bị ảnh hưởng, hoặc nhận thấy mình bị ảnh hưởng bởi dự án (project / 프로젝트). Điều khó không nằm ở việc ghi tên họ, mà ở việc hiểu interest, influence, expectation, thông tin (information / 정보) need và mức độ thay đổi theo thời gian.

Một regulator, sponsor, end người dùng (user / 사용자), operations nhóm (team / 팀) và vendor đều có “success” khác nhau. dự án (project / 프로젝트) manager phải biến các success mô hình (model / 모델) riêng đó thành expectation đủ tương thích với mục tiêu (objective / 목표) chung.

Stakeholder engagement vì vậy là một vòng điều khiển (control loop / 제어 루프) của dự án (project / 프로젝트). dự án (project / 프로젝트) gửi tín hiệu (signal / 신호) về direction và trạng thái hiện tại (current state / 현재 상태); stakeholder gửi phản hồi (feedback / 피드백), ràng buộc (constraint / 제약조건), objection hoặc approval; dự án (project / 프로젝트) cập nhật quyết định (decision / 결정). Nếu vòng lặp (loop / 루프) này chậm hoặc méo, yêu cầu (requirement / 요구사항) và quản trị (governance / 거버넌스) sẽ trễ hơn reality.

## Stakeholder hệ thống (system / 시스템) là mạng (network / 네트워크), không phải danh sách độc lập

Stakeholder ảnh hưởng lẫn nhau. Sponsor có thể bị board pressure; operations có thể liên kết với bảo mật (security / 보안); vendor có thể dựa vào subcontractor; regulator có thể thay expectation sau công khai (public / 공개) sự cố (incident / 인시던트) trong ngành.

Vì vậy phân tích từng người riêng lẻ đôi khi bỏ lỡ coalition, phụ thuộc (dependency / 의존성) và influence đường dẫn (path / 경로). Một stakeholder có formal power thấp nhưng có thể ảnh hưởng mạnh nếu họ cung cấp bằng chứng (evidence / 증거) cho người có quyền quyết định.

Mô hình tư duy (mental model / 사고 모델) tốt hơn là mạng (network / 네트워크):

```text
stakeholder → interest / power / dependency / information
            ↘ ảnh hưởng stakeholder khác
```

Dự án (project / 프로젝트) manager cần hiểu không chỉ “ai có power” mà còn **power đi qua đường nào**.

## Identification là continuous sensing

Stakeholder register không phải sản phẩm tạo ra (artifact / 산출물) tạo một lần. Stakeholder mới xuất hiện khi phạm vi (scope / 범위), organization hoặc bên ngoài (external / 외부) môi trường (environment / 환경) thay đổi. Một nhóm (team / 팀) vận hành có thể chưa quan tâm ở đầu dự án nhưng trở thành stakeholder trọng yếu (critical / 중요) trước handover. Nếu identification chỉ diễn ra lúc initiation, chuyển tiếp (transition / 전이) thường gặp surprise.

Một trigger tốt để rà lại stakeholder là khi có phạm vi (scope / 범위) thay đổi (change / 변경) lớn, organization restructure, vendor mới, compliance thay đổi (change / 변경), bản phát hành (release / 릴리스) tới người dùng (user / 사용자) group mới hoặc benefit đơn vị sở hữu (owner / 오너) thay đổi. Stakeholder map phải sống cùng dự án (project / 프로젝트) hệ thống (system / 시스템).

## Stakeholder vòng đời (lifecycle / 생명주기) khác dự án (project / 프로젝트) vòng đời (lifecycle / 생명주기)

Cùng một stakeholder có thể đổi vai trò theo thời gian. bảo mật (security / 보안) nhóm (team / 팀) có thể chỉ consult trong discovery nhưng trở thành approver trước go-live. Operations từ low-interest trở thành primary đơn vị sở hữu (owner / 오너) ở chuyển tiếp (transition / 전이). Customer hỗ trợ (support / 지원) có thể gần như vắng ở bản dựng (build / 빌드) nhưng trọng yếu (critical / 중요) sau rollout.

Engagement chiến lược (strategy / 전략) nên thay theo **quyết định (decision / 결정) need hiện tại**, không theo classification lúc kickoff.

## Stakeholder không chỉ có power và interest

Các ma trận (matrix / 행렬) như power-interest hữu ích để nghĩ về engagement, nhưng không nên biến con người thành một ô cố định. Một stakeholder “low interest” có thể đột ngột có high power khi sự cố (incident / 인시던트) xảy ra. Salience còn phụ thuộc legitimacy và urgency.

Ngoài power và interest, nên hiểu stance, phụ thuộc (dependency / 의존성) và thông tin (information / 정보) asymmetry. Một stakeholder có power thấp nhưng giữ kiến thức (knowledge / 지식) độc quyền vẫn có leverage cao. Một end người dùng (user / 사용자) có formal power thấp nhưng adoption của họ quyết định benefit realization.

Điều quan trọng là chiến lược (strategy / 전략): ai cần co-create, ai cần approve, ai cần consult, ai chỉ cần informed; và bằng chứng nào cho thấy chiến lược (strategy / 전략) cần đổi.

## Salience là động (dynamic / 동적) thuộc tính (property / 속성)

Power, legitimacy và urgency thay đổi theo sự kiện (event / 이벤트). Một legal nhóm (team / 팀) bình thường ít tham gia nhưng trở thành trọng yếu (critical / 중요) khi dữ liệu (data / 데이터) breach xuất hiện. Một người dùng (user / 사용자) group nhỏ có thể trở nên urgent nếu defect ảnh hưởng an toàn (safety / 안전).

Stakeholder prioritization vì vậy phải event-sensitive. Nếu dự án (project / 프로젝트) chỉ dùng stakeholder ma trận (matrix / 행렬) static, tín hiệu (signal / 신호) mới có thể không đổi engagement dù rủi ro (risk / 위험) profile đã đổi hoàn toàn.

## Stakeholder phụ thuộc (dependency / 의존성) quan trọng ngang stakeholder power

Power hỏi “họ có thể ảnh hưởng dự án (project / 프로젝트) tới đâu?”. phụ thuộc (dependency / 의존성) hỏi “dự án (project / 프로젝트) phụ thuộc họ tới đâu?”.

Một bên ngoài (external / 외부) API nhóm (team / 팀) không có quyền formal với dự án (project / 프로젝트) nhưng nếu không giao giao diện (interface / 인터페이스), dự án (project / 프로젝트) không thể proceed. Đây là high phụ thuộc (dependency / 의존성) stakeholder dù organizational power thấp.

Ngược lại một executive power cao nhưng không nằm trên trọng yếu (critical / 중요) quyết định (decision / 결정) đường dẫn (path / 경로) có thể cần exception-level reporting thay vì daily engagement.

## Biểu diễn (representation / 표현) rủi ro (risk / 위험): người lên tiếng không luôn đại diện người chịu tác động

Dự án (project / 프로젝트) thường nghe rõ nhất từ stakeholder có thời gian, authority hoặc kỹ năng diễn đạt tốt. Nhưng nhóm bị ảnh hưởng lớn nhất có thể ít xuất hiện trong workshop: frontline employee bận vận hành, customer bỏ sản phẩm thay vì gửi phản hồi (feedback / 피드백), người dùng (user / 사용자) có khả năng tiếp cận (accessibility / 접근성) need ít được mời, hoặc subcontractor chịu ràng buộc (constraint / 제약조건) nhưng communication đi qua vendor chính.

Đây là **biểu diễn (representation / 표현) rủi ro (risk / 위험)**. Nếu dự án (project / 프로젝트) đồng nhất “phản hồi (feedback / 피드백) thu được” với “nhu cầu của population”, yêu cầu (requirement / 요구사항) và benefit mô hình (model / 모델) có thể bị lệch ngay cả khi workshop diễn ra rất chuyên nghiệp.

Cần hỏi ai đang vắng mặt, ai đang được proxy bởi người khác và proxy đó có incentive/kiến thức (knowledge / 지식) đủ để đại diện không. chủ sản phẩm (product owner / 제품 책임자), manager hoặc customer representative có thể là giao diện (interface / 인터페이스) cần thiết, nhưng high-consequence giả định (assumption / 가정) vẫn nên được kiểm chứng với bằng chứng (evidence / 증거) gần affected population hơn khi khả thi.

Một dấu hiệu nguy hiểm là stakeholder map rất đầy đủ theo org chart nhưng không có người đại diện cho nhóm chịu operational burden sau rollout. Đây là điểm nối stakeholder phân tích (analysis / 분석) với phân phối (distribution / 분포) of giá trị (value / 값)/harm ở chapter Foundations.

## Engagement trạng thái (state / 상태) khác communication frequency

Gửi nhiều thông tin không đồng nghĩa stakeholder được engage tốt. Một stakeholder có thể nhận daily report nhưng vẫn phản đối dự án (project / 프로젝트) vì success criteria của họ chưa được hiểu.

Engagement có thể nhìn như movement giữa unaware, resistant, neutral, supportive và leading, nhưng classification chỉ hữu ích nếu gắn với hành động (action / 동작). Nếu một stakeholder trọng yếu (critical / 중요) vẫn resistant, PM cần hiểu reason: mất mát (loss / 손실) of điều khiển (control / 제어), tải công việc (workload / 워크로드) tăng, compliance concern, trust thấp hay incentive mismatch.

Mục tiêu không phải biến mọi người thành “supportive”. Một regulator đúng vai trò có thể liên tục challenge dự án (project / 프로젝트); engagement tốt ở đây nghĩa concern được surface sớm và bằng chứng (evidence / 증거) được trao đổi đúng cách.

## Resistance không phải luôn là bài toán (problem / 문제) cần “loại bỏ”

Resistance có thể chứa thông tin (information / 정보) mà dự án (project / 프로젝트) chưa thấy. Operations phản đối có thể vì hỗ trợ (support / 지원) sức chứa (capacity / 용량) không đủ. Compliance phản đối có thể vì điều khiển (control / 제어) bằng chứng (evidence / 증거) yếu. người dùng (user / 사용자) phản đối có thể vì workflow làm tăng tải công việc (workload / 워크로드).

Nếu dự án (project / 프로젝트) coi mọi resistance là “change-management issue”, nó có thể cố thuyết phục thay vì sửa thiết kế (design / 설계).

Câu hỏi đầu tiên nên là: resistance đến từ misinformation, incentive xung đột (conflict / 충돌), legitimate rủi ro (risk / 위험), năng lực (capability / 역량) gap hay mất mát (loss / 손실) of status/điều khiển (control / 제어)? phản hồi (response / 응답) khác nhau theo cause.

## Phản hồi (feedback / 피드백) sampling độ lệch (bias / 편향)

Vòng phản hồi (feedback loop / 피드백 루프) chỉ tốt khi mẫu (sample / 표본) đủ đại diện cho quyết định (decision / 결정) cần đưa ra. Nếu pilot chỉ gồm power người dùng (user / 사용자) nhiệt tình, adoption tín hiệu (signal / 신호) có thể quá optimistic. Nếu survey chỉ nhận phản hồi (response / 응답) từ người rất hài lòng hoặc rất bất mãn, average không phản ánh silent majority. Nếu UAT chủ yếu do dự án (project / 프로젝트) nhóm (team / 팀) chạy, operational friction có thể bị bỏ qua.

Vì vậy PM cần phân biệt **phản hồi (feedback / 피드백) volume** với **phản hồi (feedback / 피드백) validity**. Câu hỏi nên là: ai được quan sát, trong ngữ cảnh (context / 맥락) nào, ai không xuất hiện và bằng chứng (evidence / 증거) này có đủ gần môi trường vận hành (production / 운영 환경) reality không?

Sampling độ lệch (bias / 편향) đặc biệt nguy hiểm vì dashboard có thể rất nhiều dữ liệu (data / 데이터) nhưng vẫn sai mô hình (model / 모델). Cách giảm không phải luôn “thu thập nhiều hơn”, mà là chọn segment, scenario và observation cửa sổ (window / 윈도우) phù hợp với bất định (uncertainty / 불확실성) đang cần giảm.

## Expectation alignment trước expectation management

Không thể “manage expectation” tốt nếu expectation chưa được surface. Nhiều dự án (project / 프로젝트) xung đột (conflict / 충돌) đến từ hidden các giả định (assumptions / 가정들): sponsor nghĩ MVP gồm reporting, nhóm (team / 팀) nghĩ không; vendor nghĩ phản hồi (response / 응답) SLA là nghiệp vụ (business / 비즈니스) hours, customer nghĩ 24/7.

Alignment là quá trình làm giả định (assumption / 가정) tường minh (explicit / 명시적), tìm gap, thương lượng priority và ghi nhận quyết định (decision / 결정). Sau đó expectation management mới là việc liên tục so sánh hiện tại (current / 현재) reality với agreed expectation và cập nhật khi ngữ cảnh (context / 맥락) thay đổi.

Expectation càng quan trọng càng cần bằng chứng (evidence / 증거) cụ thể. “Nhanh”, “ổn định”, “dễ dùng” hoặc “xong trước cuối quý” đều có thể được hiểu khác nhau nếu không chuyển thành acceptance criterion, milestone hoặc measurable kết quả (outcome / 결과).

## Expectation debt

Nếu dự án (project / 프로젝트) biết expectation đang khác reality nhưng trì hoãn conversation vì sợ xung đột (conflict / 충돌), gap đó tích lại thành **expectation debt**.

Ví dụ sponsor vẫn tin go-live tháng 10 dù nhóm (team / 팀) đã biết từ tháng 8 rằng trọng yếu (critical / 중요) vendor phụ thuộc (dependency / 의존성) có khả năng đẩy sang tháng 12. Mỗi tuần không cập nhật làm correction sau này khó hơn vì quyết định (decision / 결정) khác đã dựa trên expectation cũ.

Expectation debt giống technical debt ở chỗ short-term silence giảm discomfort nhưng tăng future correction chi phí (cost / 비용).

## Promise, forecast và aspiration phải tách nhau

Stakeholder thường nghe một date nhưng không biết đó là commitment, forecast hay mục tiêu (target / 대상). Communication tốt phải làm rõ ngữ nghĩa (semantic / 의미적) mức (level / 수준).

“Chúng tôi mục tiêu (target / 대상) 30/10 với confidence hiện tại 60%” khác hoàn toàn “30/10 là contractual commitment”. Nếu ba loại date bị trộn, trust bị phá dù nhóm (team / 팀) technically “đã nói trước”.

## Communication là transfer of meaning

Gửi message không đồng nghĩa communication thành công. Communication có sender, encoding, channel, noise, receiver, interpretation và phản hồi (feedback / 피드백). Vì vậy “đã gửi email” không chứng minh stakeholder hiểu quyết định (decision / 결정).

Channel nên match với purpose. Một xung đột (conflict / 충돌) phức tạp thường cần synchronous conversation; một quyết định (decision / 결정) cần traceability nên được documented; urgent sự cố (incident / 인시던트) cần fast broadcast và acknowledgement; kiến thức (knowledge / 지식) bền vững cần repository có quyền sở hữu (ownership / 소유권).

Communication plan hữu ích khi nó trả lời ai cần thông tin gì, tại sao, khi nào, qua channel nào, format nào, ai chịu trách nhiệm và vòng phản hồi (feedback loop / 피드백 루프) nào xác nhận understanding.

## Closed-loop communication

Với thông tin (information / 정보) trọng yếu (critical / 중요), communication nên có acknowledgement và confirmation of meaning. Sender truyền message, receiver xác nhận nhận/hiểu, hành động (action / 동작) hoặc next trạng thái (state / 상태) được ghi rõ.

Trong sự cố (incident / 인시던트), “đã post Slack” không đủ nếu đơn vị sở hữu (owner / 오너) chưa acknowledge. Trong handover, “đã gửi tài liệu” không đủ nếu operations chưa chứng minh năng lực (capability / 역량).

Closed-loop communication đặc biệt quan trọng khi consequence của misunderstanding cao.

## Communication độ tin cậy (reliability / 신뢰성) có thể thiết kế như dịch vụ (service / 서비스)

Một dự án (project / 프로젝트) lớn có thể coi communication đường dẫn (path / 경로) như dịch vụ (service / 서비스) với expectation rõ: sự cố (incident / 인시던트) severity-1 acknowledgement trong 10 phút, phụ thuộc (dependency / 의존성) yêu cầu (request / 요청) phản hồi trong hai ngày, thay đổi (change / 변경) quyết định (decision / 결정) trong năm ngày.

Đây không phải để biến con người thành SLA máy móc, mà để làm độ trễ (latency / 지연 시간) visible. Nếu dự án (project / 프로젝트) phụ thuộc quyết định (decision / 결정) nhưng không có phản hồi (response / 응답) expectation, hàng đợi (queue / 큐) có thể bị coi là “communication bài toán (problem / 문제)” thay vì quản trị (governance / 거버넌스) bottleneck.

## Thông tin (information / 정보) có half-life

Một message có thể hoàn toàn đúng lúc gửi nhưng nhanh chóng stale. Forecast, stakeholder stance, vendor ETA, rủi ro (risk / 위험) exposure và operating procedure đều có **thông tin (information / 정보) half-life** khác nhau. Vì vậy traceability không chỉ hỏi “nguồn ở đâu?” mà còn “nguồn này còn fresh không?”.

Thông tin (information / 정보) high-volatility cần timestamp, đơn vị sở hữu (owner / 오너) và refresh trigger rõ hơn thông tin (information / 정보) ổn định. Một contact danh sách (list / 목록) có thể rà soát (review / 검토) hàng quý; sự cố (incident / 인시던트) status có thể stale sau 15 phút. Dùng cùng một cadence cho mọi thông tin (information / 정보) tạo hoặc overhead hoặc stale quyết định (decision / 결정) đầu vào (input / 입력).

Quyết định (decision / 결정) dựa trên stale thông tin (information / 정보) có thể hợp lý tại thời điểm cũ nhưng sai ở hiện tại. Vì vậy sản phẩm tạo ra (artifact / 산출물) quan trọng nên cho người đọc biết effective thời gian (time / 시간), confidence và điều kiện (condition / 조건) làm nó hết hiệu lực. Đây là liên kết (connection / 연결) trực tiếp với freshness SLO và lineage ở chapter Artifacts.

## Push, pull và interactive communication

Push communication đưa thông tin (information / 정보) trực tiếp tới audience, ví dụ email hoặc notification. Pull communication để stakeholder tự truy cập repository, dashboard hoặc portal khi cần. Interactive communication cho phép trao đổi hai chiều như workshop, lời gọi (call / 호출) hoặc negotiation.

Chọn chế độ (mode / 모드) theo bất định (uncertainty / 불확실성). thông tin (information / 정보) ổn định và self-service phù hợp pull. Announcement rõ có thể push. Ambiguous yêu cầu (requirement / 요구사항) hoặc xung đột (conflict / 충돌) cần interactive vì meaning phải được đồng tạo, không chỉ truyền đi.

## Communication chế độ (mode / 모드) nên dựa trên chi phí (cost / 비용) of misunderstanding

Một routine chỉ số (metric / 지표) có thể pull qua dashboard. Một material rủi ro (risk / 위험) cần push tới đơn vị sở hữu (owner / 오너). Một ambiguous contractual interpretation cần interactive discussion rồi formal bản ghi (record / 레코드).

Càng khó sửa misunderstanding, càng cần richer channel và confirmation mạnh hơn.

## Richness của communication channel

Channel có độ giàu thông tin khác nhau. văn bản (text / 텍스트) ngắn tốt cho fact đơn giản nhưng kém cho xung đột (conflict / 충돌) nhiều cảm xúc. Video/lời gọi (call / 호출) hoặc face-to-face cung cấp phản hồi (feedback / 피드백) tức thời và nhiều contextual cue hơn, nhưng khó dấu vết (trace / 추적) nếu không document quyết định (decision / 결정) sau đó.

Một mẫu (pattern / 패턴) tốt là discuss rich, bản ghi (record / 레코드) lean: dùng synchronous channel để giải ambiguity rồi ghi quyết định (decision / 결정)/hành động (action / 동작) trong sản phẩm tạo ra (artifact / 산출물) bền vững.

## Synchronous và asynchronous communication là sự đánh đổi (trade-off / 트레이드오프)

Synchronous communication giảm phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간) nhưng tốn calendar alignment và dễ mất traceability. Asynchronous communication quy mô (scale / 규모) tốt hơn và tạo bản ghi (record / 레코드) nhưng cần ngữ cảnh (context / 맥락) rõ, có thể làm clarification chậm.

Dự án (project / 프로젝트) phân tán (distributed / 분산) nên thiết kế loại quyết định (decision / 결정) nào cần sync, loại nào async và hết thời gian chờ (timeout / 타임아웃) bao lâu trước escalation.

## Transparency không phải thông tin (information / 정보) overload

Transparency nghĩa thông tin (information / 정보) cần thiết cho quyết định (decision / 결정) được nhìn thấy đúng thời điểm. Dump mọi log/report cho sponsor không tăng transparency nếu họ không nhận ra tín hiệu (signal / 신호) quan trọng. Reporting tốt phải tailor theo quyết định (decision / 결정) mức (level / 수준).

Nhóm (team / 팀) có thể cần blocker, WIP, defect và phụ thuộc (dependency / 의존성) detail. Sponsor cần kết quả (outcome / 결과), trend, forecast, major rủi ro (risk / 위험), quyết định (decision / 결정) yêu cầu (request / 요청) và tolerance breach. quản trị (governance / 거버넌스) body cần compliance/bằng chứng (evidence / 증거) và escalation.

Thông tin (information / 정보) overload cũng là rủi ro (risk / 위험) vì tín hiệu (signal / 신호) quan trọng bị chìm. PM phải thiết kế thông tin (information / 정보) kiến trúc (architecture / 아키텍처), không chỉ tăng volume.

## Executive reporting là compression có chủ đích

Một executive dashboard luôn mất detail. Vì vậy người thiết kế phải bảo vệ các tín hiệu (signal / 신호) không được phép bị average hóa: an toàn (safety / 안전) breach, legal exposure, trọng yếu (critical / 중요) phụ thuộc (dependency / 의존성), major forecast shift.

Green overall status không được phép che một red non-negotiable ràng buộc (constraint / 제약조건). Aggregation quy tắc (rule / 규칙) phải phản ánh consequence chứ không chỉ arithmetic average.

## Communication noise và distortion

Noise có thể là technical jargon, ngôn ngữ (language / 언어) barrier, timezone, organizational politics, dữ liệu (data / 데이터) inconsistency hoặc quá nhiều intermediary. Mỗi handoff có khả năng làm message mất fidelity.

Một dự án (project / 프로젝트) nhiều tầng (layer / 계층) reporting có thể thấy “red rủi ro (risk / 위험)” biến thành “amber concern” rồi cuối cùng thành “on nhánh học (track / 트랙)” ở executive deck. Đây là distortion do incentive và compression, không chỉ lỗi wording.

Điều khiển (control / 제어) tốt gồm source-of-truth, direct escalation đường dẫn (path / 경로) cho material rủi ro (risk / 위험) và traceable quyết định (decision / 결정) yêu cầu (request / 요청).

## Incentive tạo distortion

Nếu messenger bị phạt khi mang bad news, tín hiệu (signal / 신호) sẽ bị soften. Nếu department KPI phụ thuộc status xanh, report có độ lệch (bias / 편향) cấu trúc.

Dự án (project / 프로젝트) manager phải hiểu communication độ tin cậy (reliability / 신뢰성) không chỉ là kỹ năng viết; nó phụ thuộc incentive và psychological an toàn (safety / 안전). Đây là điểm nối trực tiếp với chapter People.

## Active listening và diagnostic question

Stakeholder conversation tốt không chỉ là thuyết phục. Active listening dùng paraphrase, clarification và bằng chứng (evidence / 증거) check để xác nhận meaning.

Khi stakeholder nói “dự án (project / 프로젝트) chậm”, PM nên tìm statement cụ thể: milestone nào, expectation nào, dữ liệu (data / 데이터) nào? Khi người dùng (user / 사용자) nói “khó dùng”, cần scenario và friction cụ thể. Diagnostic question biến emotion hoặc general statement thành actionable thông tin (information / 정보) mà không dismiss concern.

## Listening phải phân biệt position, interest và ràng buộc (constraint / 제약조건)

Position là điều stakeholder nói họ muốn. Interest là lý do họ muốn. ràng buộc (constraint / 제약조건) là ranh giới (boundary / 경계) họ không thể thay.

“Phải go-live ngày 1/11” có thể là position. Interest có thể là marketing campaign; ràng buộc (constraint / 제약조건) thực có thể chỉ là regulatory reporting trước cuối năm. Nếu không tách ba lớp, dự án (project / 프로젝트) dễ coi mọi yêu cầu (request / 요청) là hard ràng buộc (constraint / 제약조건).

## Negotiation là quản lý sự đánh đổi (trade-off / 트레이드오프)

Dự án (project / 프로젝트) thường có nhiều mục tiêu (objective / 목표) không thể tối ưu đồng thời. Negotiation tốt tách interest khỏi position và làm sự đánh đổi (trade-off / 트레이드오프) tường minh (explicit / 명시적).

Ví dụ sponsor yêu cầu thêm phạm vi (scope / 범위) nhưng không đổi deadline. PM không nên chỉ nói “không thể” hoặc âm thầm ép nhóm (team / 팀) overtime. Cần đưa option: bỏ phạm vi (scope / 범위) khác, tăng sức chứa (capacity / 용량) nếu có leverage, chấp nhận rủi ro (risk / 위험), đổi milestone hoặc defer tính năng (feature / 기능). Negotiation làm ràng buộc (constraint / 제약조건) visible để authority chọn.

## BATNA và ZOPA

BATNA (Best Alternative to a Negotiated Agreement) là alternative tốt nhất nếu không đạt agreement. ZOPA (Zone of Possible Agreement) là vùng hai bên có thể cùng chấp nhận.

Hiểu BATNA giúp negotiation bớt cảm tính. Nếu vendor không giảm giá nhưng buyer có alternative vendor credible, bargaining position khác hoàn toàn trường hợp switching chi phí (cost / 비용) rất cao.

ZOPA không phải lúc nào tồn tại. Nếu customer yêu cầu deadline không thể đạt mà không phá legal/an toàn (safety / 안전) ràng buộc (constraint / 제약조건), “compromise ở giữa” không phải answer hợp lý. Khi đó cần đổi phạm vi (scope / 범위)/tài nguyên (resource / 자원) hoặc escalate quyết định (decision / 결정).

## Negotiation power đến từ option, thông tin (information / 정보) và timing

Formal authority chỉ là một nguồn power. Có alternative tốt, bằng chứng (evidence / 증거) tốt và thời gian chuẩn bị có thể tăng leverage. Bị khóa vào một vendor ngay trước deadline làm BATNA yếu dù đặc tả hợp đồng (contract / 계약) manager có chức danh cao.

Dự án (project / 프로젝트) chiến lược (strategy / 전략) nên tạo option sớm thay vì đợi negotiation crisis mới tìm leverage.

## Negotiation tốt đôi khi tạo option mới thay vì chia phần cũ

Nếu hai bên chỉ tranh một biến như price hoặc deadline, negotiation dễ thành zero-sum. Nhưng dự án (project / 프로젝트) thường có nhiều dimension: phạm vi (scope / 범위), timing, payment profile, dịch vụ (service / 서비스) mức (level / 수준), rủi ro (risk / 위험) allocation, chuỗi (sequence / 시퀀스), pilot kích thước (size / 크기) hoặc acceptance cơ chế (mechanism / 메커니즘). Mở thêm dimension có thể tạo trade mà cả hai bên coi là tốt hơn.

Ví dụ vendor không thể giảm total price nhưng có thể chấp nhận milestone payment muộn hơn; customer không thể đổi regulatory date nhưng có thể tách optional phạm vi (scope / 범위) sang phase sau. Đây là **option creation**, khác với compromise cơ học “mỗi bên nhường một nửa”.

Tuy nhiên option mới chỉ có giá trị nếu obligation và consequence được làm rõ. Một creative deal mơ hồ có thể chỉ chuyển xung đột (conflict / 충돌) sang acceptance/claim ở cuối dự án (project / 프로젝트).

## Trust là tài sản của thông tin (information / 정보) hệ thống (system / 시스템)

Influence không chỉ đến từ authority. Credibility, consistency, reciprocity và understanding stakeholder interest đều tạo trust. Khi PM liên tục che bad news để “giữ hình ảnh”, short-term xung đột (conflict / 충돌) có thể giảm nhưng thông tin (information / 정보) độ tin cậy (reliability / 신뢰성) bị phá. Khi crisis xảy ra, stakeholder sẽ discount mọi report sau đó.

Trust giúp giảm xác minh (verification / 확인) chi phí (cost / 비용). Khi report đáng tin, stakeholder không phải kiểm lại mọi detail. Nhưng trust không thay bằng chứng (evidence / 증거) ở quyết định (decision / 결정) có compliance hoặc financial impact cao.

## Trust repair cần bằng chứng (evidence / 증거), không chỉ apology

Khi trust bị phá bởi missed commitment hoặc hidden issue, nói “sẽ communicate tốt hơn” thường không đủ. Cần thay cơ chế (mechanism / 메커니즘): forecast confidence rõ hơn, earlier escalation trigger, transparent nguồn (source / 소스) dữ liệu (data / 데이터) hoặc checkpoint mới.

Trust được rebuild khi stakeholder thấy prediction/reality dần align và bad news đến sớm hơn.

## Stakeholder rủi ro (risk / 위험) propagation

Một stakeholder issue có thể lan thành phạm vi (scope / 범위), schedule, finance hoặc adoption rủi ro (risk / 위험). Operations resistance có thể delay chuyển tiếp (transition / 전이); vendor dispute có thể thành schedule/chi phí (cost / 비용) rủi ro (risk / 위험); regulator concern có thể khối (block / 블록) go-live.

Stakeholder register không nên đứng tách biệt rủi ro (risk / 위험) register. Khi engagement bài toán (problem / 문제) có xác suất (probability / 확률)/impact lên mục tiêu (objective / 목표), nó đã trở thành dự án (project / 프로젝트) rủi ro (risk / 위험) cần đơn vị sở hữu (owner / 오너)/phản hồi (response / 응답).

## Coalition và stakeholder alignment

Một dự án (project / 프로젝트) transformation có thể gặp nhiều stakeholder riêng lẻ neutral nhưng khi họ hình thành coalition phản đối, influence tăng mạnh. Ngược lại sponsor có thể tạo coalition hỗ trợ bằng cách align nghiệp vụ (business / 비즈니스) owners quanh dùng chung (shared / 공유) kết quả (outcome / 결과).

PM không nên “chính trị hóa” mọi tương tác (interaction / 상호작용), nhưng phải nhận ra organizational thay đổi (change / 변경) diễn ra qua mạng (network / 네트워크). Engagement chiến lược (strategy / 전략) chỉ theo từng cá nhân có thể bỏ lỡ group dynamics.

## Kiến thức (knowledge / 지식) transfer và bus factor

Kiến thức (knowledge / 지식) transfer (chuyển giao tri thức / 지식 이전) giải quyết rủi ro tri thức nằm trong đầu một vài người. tường minh (explicit / 명시적) kiến thức (knowledge / 지식) có thể document; tacit kiến thức (knowledge / 지식) thường cần pairing, shadowing, walkthrough, rehearsal và thực hành.

Một handover document 100 trang không đảm bảo operations có thể vận hành hệ thống (system / 시스템). Readiness tốt hơn được chứng minh bằng việc operations tự chạy scenario, xử lý sự cố (incident / 인시던트) mẫu hoặc thực hiện quay lui (rollback / 롤백) dưới supervision.

Bus factor thấp nghĩa một vài cá nhân là single điểm (point / 지점) of kiến thức (knowledge / 지식) thất bại (failure / 실패). PM nên phát hiện sớm qua phụ thuộc (dependency / 의존성) map, vacation rủi ro (risk / 위험), rà soát (review / 검토) quyền sở hữu (ownership / 소유권) và handover need.

## Kiến thức (knowledge / 지식) decay

Kiến thức (knowledge / 지식) không chỉ có nguy cơ mất khi người rời nhóm (team / 팀); nó còn stale khi hệ thống (system / 시스템) thay đổi. Runbook viết đúng sáu tháng trước có thể sai sau kiến trúc (architecture / 아키텍처) thay đổi (change / 변경).

Kiến thức (knowledge / 지식) sản phẩm tạo ra (artifact / 산출물) cần đơn vị sở hữu (owner / 오너), cập nhật (update / 업데이트) trigger và kiểm tra hợp lệ (validation / 검증). Một rehearsal định kỳ có thể phát hiện document stale tốt hơn việc chỉ rà soát (review / 검토) văn bản (text / 텍스트).

## Kiến thức (knowledge / 지식) transfer cần acceptance criterion

“Đã huấn luyện (training / 학습)” là activity, không phải bằng chứng (evidence / 증거) của transfer. Có thể dùng teach-back, simulation, runbook thực thi (execution / 실행) hoặc hỗ trợ (support / 지원) handoff drill để kiểm chứng.

Ví dụ operations nhóm (team / 팀) chỉ được coi là ready khi họ tự deploy bản kiểm thử (test / 테스트), restore backup và xử lý ba sự cố (incident / 인시던트) scenario mà không phụ thuộc nhà phát triển (developer / 개발자) chính. Điều này biến kiến thức (knowledge / 지식) transfer từ attendance thành năng lực (capability / 역량) bằng chứng (evidence / 증거).

## Kiến thức (knowledge / 지식) transfer là chuyển khả năng tái tạo lập luận (reasoning / 추론)

Một người có thể nhớ procedure nhưng không biết tại sao procedure tồn tại. Khi ngữ cảnh (context / 맥락) thay đổi, họ không biết phần nào được phép adapt. Vì vậy transfer sâu cần cả **what**, **why**, ranh giới (boundary / 경계) và thất bại (failure / 실패) tín hiệu (signal / 신호).

Ví dụ runbook nói “restart dịch vụ (service / 서비스) B trước dịch vụ (service / 서비스) A” nhưng không giải phụ thuộc (dependency / 의존성). Khi kiến trúc (architecture / 아키텍처) đổi, operator có thể tiếp tục procedure cũ dù bất biến (invariant / 불변식) đã thay. Một handover tốt phải giúp receiving nhóm (team / 팀) tái tạo lập luận (reasoning / 추론) đủ để nhận ra khi document không còn đúng.

Teach-back vì thế mạnh hơn attendance: người nhận giải thích lại mô hình tư duy (mental model / 사고 모델), thực hiện scenario bình thường và xử lý một exception. Nếu chỉ làm được happy đường dẫn (path / 경로) khi người cũ đứng cạnh, năng lực (capability / 역량) chưa thực sự được transfer.

## Kiến thức (knowledge / 지식) quyền sở hữu (ownership / 소유권) sau chuyển tiếp (transition / 전이)

Ai giữ kiến thức (knowledge / 지식) sau dự án (project / 프로젝트) closure phải được xác định. Nếu temporary dự án (project / 프로젝트) nhóm (team / 팀) giải tán nhưng không có đơn vị sở hữu (owner / 오너) cho runbook, kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) hoặc vendor ngữ cảnh (context / 맥락), kiến thức (knowledge / 지식) decay gần như chắc chắn.

Chuyển tiếp (transition / 전이) cần chuyển cả **sản phẩm tạo ra (artifact / 산출물) quyền sở hữu (ownership / 소유권)** và **responsibility to maintain kiến thức (knowledge / 지식)**, không chỉ bản sao (copy / 복사) tệp (file / 파일) sang folder operations.

## Cross-cultural và multilingual communication

Ngôn ngữ chung không đảm bảo dùng chung (shared / 공유) interpretation. Culture khác nhau về hierarchy, directness, silence, disagreement và meaning của commitment.

PM không nên stereotype theo nationality. Cách thực tế hơn là tường minh (explicit / 명시적) working norms: “yes” nghĩa acknowledgement hay commitment? Khi chưa đồng ý có được nói trực tiếp trong meeting không? quyết định (decision / 결정) được xác nhận ở đâu? Deadline timezone nào?

Khi translation cần thiết, trọng yếu (critical / 중요) yêu cầu (requirement / 요구사항) hoặc đặc tả hợp đồng (contract / 계약) term phải được verify hai chiều, không dựa hoàn toàn vào machine translation hoặc một cá nhân trung gian.

## Translation rủi ro (risk / 위험) là ngữ nghĩa (semantic / 의미적) rủi ro (risk / 위험)

Một từ legal/technical dịch gần đúng có thể thay obligation. trọng yếu (critical / 중요) term nên giữ original wording cùng translation, có glossary hoặc back-translation khi cần.

Nếu một bilingual coordinator trở thành single nguồn (source / 소스) cho mọi meaning, họ cũng trở thành kiến thức (knowledge / 지식) bottleneck. Important quyết định (decision / 결정) cần sản phẩm tạo ra (artifact / 산출물) song ngữ hoặc xác minh (verification / 확인) independent khi consequence cao.

## Stakeholder fatigue

Engagement quá nhiều cũng có chi phí (cost / 비용). Mời stakeholder vào mọi meeting làm họ disengage khi thật sự cần quyết định (decision / 결정).

Engagement cadence nên match quyết định (decision / 결정) need. Executive sponsor có thể cần milestone/exception rà soát (review / 검토); sản phẩm (product / 제품) người dùng (user / 사용자) cần frequent phản hồi (feedback / 피드백) trên increment; compliance cần gate ở những điểm (point / 지점) material. Tailoring communication giúp bảo vệ attention như một tài nguyên (resource / 자원) hữu hạn.

## Attention là scarce tài nguyên (resource / 자원)

Một quyết định (decision / 결정) yêu cầu (request / 요청) gửi cùng 30 informational email dễ bị bỏ qua. Communication thiết kế (design / 설계) nên phân biệt action-needed, approval-needed, rủi ro (risk / 위험) alert và FYI.

Nếu mọi message đều marked urgent, organization mất ability phân biệt urgency. Đây là information-system thất bại (failure / 실패), không chỉ etiquette.

## Stakeholder quyết định (decision / 결정) debt

Khi dự án (project / 프로젝트) liên tục trì hoãn những conversation hoặc approval khó, quyết định (decision / 결정) không biến mất; nó tích thành hàng đợi (queue / 큐). phạm vi (scope / 범위) option khác có thể tiếp tục được xây trên giả định (assumption / 가정) chưa được sponsor xác nhận, vendor có thể tiếp tục công việc (work / 작업) trước khi commercial term rõ, hoặc operations có thể chuẩn bị theo hỗ trợ (support / 지원) mô hình (model / 모델) chưa thống nhất.

Đây là **stakeholder quyết định (decision / 결정) debt**: số quyết định (decision / 결정) material đã đến lúc cần authority/phản hồi (feedback / 피드백) nhưng vẫn bị giữ ở trạng thái implicit. Debt này làm rework potential tăng theo thời gian vì nhiều downstream hành động (action / 동작) phụ thuộc trạng thái (state / 상태) chưa được chốt.

Một dashboard tốt không chỉ báo “awaiting sponsor”; nó cho thấy age, blocked giá trị (value / 값), latest-needed date và consequence nếu không quyết. Điều đó biến engagement từ activity mềm thành decision-flow management.

## Ví dụ scenario

Sponsor yêu cầu báo cáo mỗi ngày vì “không thấy tiến độ”. Thay vì chỉ tăng tần suất report, PM nên tìm thông tin (information / 정보) gap thực sự. Có thể sponsor không cần danh sách tác vụ (task / 작업) mà cần forecast ngày UAT và phụ thuộc (dependency / 의존성) với vendor. Một dashboard nhỏ có milestone confidence, trọng yếu (critical / 중요) blocker và quyết định (decision / 결정) needed có thể giải quyết bài toán (problem / 문제) tốt hơn 20 trang status.

Một scenario khác: operations liên tục từ chối nhận handover vì “tài liệu chưa đủ”, trong khi dự án (project / 프로젝트) đã viết nhiều document. nguyên nhân gốc (root cause / 근본 원인) có thể là họ chưa được tham gia thiết kế (design / 설계) hỗ trợ (support / 지원) mô hình (model / 모델) và không tin mình có năng lực (capability / 역량) xử lý sự cố (incident / 인시던트). Giải pháp cần joint readiness rehearsal và quyền sở hữu (ownership / 소유권) alignment, không chỉ viết thêm tài liệu.

Một scenario thứ ba: vendor liên tục trả lời “đang xem xét” nhưng không lần ghi nhận (commit / 커밋) resolution date. PM gửi thêm email mỗi ngày nhưng phụ thuộc (dependency / 의존성) vẫn trễ. bài toán (problem / 문제) không còn là message frequency; communication đường dẫn (path / 경로) thiếu phản hồi (response / 응답) expectation, escalation threshold và commercial leverage. Cần chuyển từ informal follow-up sang phụ thuộc (dependency / 의존성)/quản trị (governance / 거버넌스) cơ chế (mechanism / 메커니즘) phù hợp.

## Stakeholder anti-patterns

Broadcast management là giả định gửi nhiều cập nhật (update / 업데이트) sẽ tạo alignment. Executive shielding là che bad news khỏi sponsor để “không làm họ lo”. Stakeholder appeasement là hứa phạm vi (scope / 범위)/date không realistic chỉ để tránh xung đột (conflict / 충돌). Engagement theater là workshop nhiều nhưng quyết định (decision / 결정) right không đổi. Translation bottleneck là để một người giữ toàn bộ ngữ nghĩa (semantic / 의미적) cầu nối (bridge / 브리지). Handover dump là chuyển hàng trăm tệp (file / 파일) nhưng không chuyển năng lực (capability / 역량).

Các anti-pattern này đều có điểm chung: activity communication có vẻ cao nhưng thông tin (information / 정보)/quyết định (decision / 결정) chất lượng (quality / 품질) thấp.

## Kết nối với software requirements

Stakeholder need là đầu vào quan trọng của yêu cầu (requirement / 요구사항) nhưng không đồng nghĩa yêu cầu (requirement / 요구사항) cuối cùng. Trong software dự án (project / 프로젝트), xem thêm [Requirements Engineering](../computer_science/09_software_engineering/00_requirements_specification_and_engineering_process.md) để hiểu cách intent được biến thành acceptance criteria và traceable hành vi (behavior / 동작).

## Mô hình tư duy (mental model / 사고 모델)

> Stakeholder engagement là thiết kế phản hồi (feedback / 피드백) và influence mạng (network / 네트워크) giữa dự án (project / 프로젝트) với những người định nghĩa, cung cấp, sử dụng hoặc chịu hệ quả của giá trị (value / 값). Communication tốt phải bảo toàn meaning, độ trễ (latency / 지연 시간) và accountability; kiến thức (knowledge / 지식) transfer tốt phải biến thông tin (information / 정보) thành năng lực (capability / 역량) có đơn vị sở hữu (owner / 오너) sau chuyển tiếp (transition / 전이).

Tiếp theo: [Integration, scope, requirements và change](./04_integration_scope_requirements_and_change.md).

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 foundations value and project system](./00_foundations_value_and_project_system.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
