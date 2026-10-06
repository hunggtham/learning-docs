# 11 — đo lường (measurement / 측정), status, closure và continuous improvement

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **11 — Measurement, status, closure và continuous improvement**. Route đi từ decision-oriented metrics → status/evidence → acceptance/closure → lessons learned → improvement loops, để đo lường nối với hành động và giá trị bền vững.

## Đo lường (measurement / 측정) phục vụ quyết định (decision / 결정)

Chỉ số (metric / 지표) có giá trị khi giúp phát hiện trạng thái (state / 상태), trend hoặc rủi ro (risk / 위험) để ai đó ra quyết định (decision / 결정). Số liệu được thu chỉ vì “dashboard phải có” tạo reporting tải (load / 로드) nhưng không tăng điều khiển (control / 제어).

Một chỉ số (metric / 지표) tốt cần definition, dữ liệu (data / 데이터) nguồn (source / 소스), cadence, đơn vị sở hữu (owner / 오너), threshold và hành động (action / 동작) interpretation. Nếu hai nhóm (team / 팀) hiểu “completed” khác nhau, tổng percent complete không có meaning.

Điểm quan trọng là đo lường (measurement / 측정) không phải mục tiêu (objective / 목표). chỉ số (metric / 지표) là proxy cho một phần reality. Khi proxy trở thành mục tiêu (target / 대상) tuyệt đối, hành vi (behavior / 동작) có thể bị méo để tối ưu số thay vì kết quả (outcome / 결과).

> **Nối mạch:** **Đo lường (measurement / 측정) phục vụ quyết định (decision / 결정)** đặt vấn đề; **Đo lường (measurement / 측정) kiến trúc (architecture / 아키텍처): chỉ số (metric / 지표) cũng là một thông tin (information / 정보) hệ thống (system / 시스템)** kiểm tra bằng chứng, rồi **Sai số đo lường (measurement error / 측정 오차) và mô hình (model / 모델) lỗi (error / 오류)** mở rộng hệ quả.

## Đo lường (measurement / 측정) kiến trúc (architecture / 아키텍처): chỉ số (metric / 지표) cũng là một thông tin (information / 정보) hệ thống (system / 시스템)

Khi dự án (project / 프로젝트) phụ thuộc nhiều dashboard, chỉ số (metric / 지표) không nên được xem như con số xuất hiện tự nhiên. Nó có một chuỗi xử lý (pipeline / 파이프라인):

```text
real event → capture → transform → aggregate → display → interpretation → decision
```

Lỗi ở bất kỳ bước nào đều có thể tạo false confidence. Ticket được đóng nhưng reopen sau đó, timestamp dùng timezone khác, duplicate bản ghi (record / 레코드) hoặc denominator thay đổi đều có thể làm dashboard đúng về truy vấn (query / 쿼리) nhưng sai về meaning.

Vì vậy chỉ số (metric / 지표) quan trọng cần ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약): chính xác đang đo sự kiện (event / 이벤트) nào, inclusion/exclusion quy tắc (rule / 규칙), nguồn chuẩn (source of truth / 정본), độ trễ (latency / 지연 시간) và cách xử lý missing dữ liệu (data / 데이터). Đây là dữ liệu (data / 데이터) quản trị (governance / 거버넌스) ở mức dự án (project / 프로젝트), không chỉ chuyện BI nhóm (team / 팀).

> **Nối mạch:** **Đo lường (measurement / 측정) kiến trúc (architecture / 아키텍처): chỉ số (metric / 지표) cũng là một thông tin (information / 정보) hệ thống (system / 시스템)** đặt vấn đề; **Sai số đo lường (measurement error / 측정 오차) và mô hình (model / 모델) lỗi (error / 오류)** kiểm tra bằng chứng, rồi **Từ mục tiêu (objective / 목표) tới chỉ số (metric / 지표)** mở rộng hệ quả.

## Sai số đo lường (measurement error / 측정 오차) và mô hình (model / 모델) lỗi (error / 오류)

Hai loại sai khác nhau cần tách. sai số đo lường (measurement error / 측정 오차) xảy ra khi dữ liệu (data / 데이터) capture/truy vấn (query / 쿼리) không phản ánh sự kiện (event / 이벤트) thật. mô hình (model / 모델) lỗi (error / 오류) xảy ra khi dữ liệu (data / 데이터) đúng nhưng chỉ số (metric / 지표) được dùng như proxy sai cho mục tiêu (objective / 목표).

Ví dụ velocity được tính hoàn toàn chính xác nhưng dùng để kết luận productivity giữa hai nhóm (team / 팀) là mô hình (model / 모델) lỗi (error / 오류). UAT pass tỷ lệ (rate / 비율) đúng nhưng trường hợp kiểm thử (test case / 테스트 케이스) không đại diện customer journey cũng là mô hình (model / 모델) weakness.

Fix dashboard truy vấn (query / 쿼리) không sửa chỉ số (metric / 지표) mô hình (model / 모델); thêm chỉ số (metric / 지표) mới không sửa nguồn (source / 소스) dữ liệu (data / 데이터) sai. Diagnosis phải đúng tầng.

> **Nối mạch:** **Sai số đo lường (measurement error / 측정 오차) và mô hình (model / 모델) lỗi (error / 오류)** đặt vấn đề; **Từ mục tiêu (objective / 목표) tới chỉ số (metric / 지표)** kiểm tra bằng chứng, rồi **Proxy distance** mở rộng hệ quả.

## Từ mục tiêu (objective / 목표) tới chỉ số (metric / 지표)

Một chuỗi lập luận (reasoning / 추론) tốt là:

```text
objective → observable outcome → indicator → threshold → decision/action
```

Nếu mục tiêu (objective / 목표) là giảm thời gian onboarding, chỉ số (metric / 지표) phù hợp có thể là median time-to-complete hoặc abandonment tỷ lệ (rate / 비율). Số story điểm (point / 지점) hoàn thành không trực tiếp chứng minh mục tiêu (objective / 목표) này.

Chỉ số (metric / 지표) nên được chọn từ câu hỏi quản trị. “Ta cần biết điều gì để quyết định?” tốt hơn “dashboard thường có chỉ số nào?”.

> **Nối mạch:** **Proxy distance** nối từ **Từ mục tiêu (objective / 목표) tới chỉ số (metric / 지표)** sang **Leading và lagging indicators**, vì cơ chế trước tạo đầu vào cho bước sau.

## Proxy distance

Chỉ số (metric / 지표) càng xa mục tiêu (objective / 목표), càng dễ bị misinterpreted. Ticket closed là proxy xa customer kết quả (outcome / 결과) hơn resolution accepted; huấn luyện (training / 학습) attendance xa adoption hơn actual tiến trình (process / 프로세스) usage.

Proxy xa vẫn hữu ích nếu leading và cheap, nhưng cần biết nhân quả (causal / 인과적) link nào đang được giả định. Khi link yếu, chỉ số (metric / 지표) phải được kết hợp với bằng chứng (evidence / 증거) khác.

Một dashboard tốt không chỉ chứa nhiều number; nó giữ chuỗi (chain / 사슬) từ operational tín hiệu (signal / 신호) tới kết quả (outcome / 결과) đủ rõ để reader không nhầm activity với giá trị (value / 값).

> **Nối mạch:** **Leading và lagging indicators** nối từ **Proxy distance** sang **False positive và false negative**, vì cơ chế trước tạo đầu vào cho bước sau.

## Leading và lagging indicators

Lagging indicator phản ánh kết quả (outcome / 결과) đã xảy ra, như defect escaped môi trường vận hành (production / 운영 환경) hoặc ngân sách (budget / 예산) variance. Leading indicator báo trước rủi ro (risk / 위험), như kiểm thử (test / 테스트) hàng đợi (queue / 큐) tăng, trọng yếu (critical / 중요) phụ thuộc (dependency / 의존성) chưa resolved hoặc yêu cầu (requirement / 요구사항) churn cao.

Không có leading chỉ số (metric / 지표) hoàn hảo. Mục tiêu là tạo early tín hiệu (signal / 신호) đủ tốt để kiểm tra thêm trước khi lagging thất bại (failure / 실패) xảy ra.

Một chỉ số (metric / 지표) có thể leading cho mục tiêu (objective / 목표) này nhưng lagging cho mục tiêu (objective / 목표) khác. Cycle thời gian (time / 시간) tăng là lagging tín hiệu (signal / 신호) của workflow congestion đã xảy ra, nhưng có thể là leading tín hiệu (signal / 신호) cho missed bản phát hành (release / 릴리스) date.

> **Nối mạch:** **False positive và false negative** nối từ **Leading và lagging indicators** sang **Baseline, actual và forecast**, vì cơ chế trước tạo đầu vào cho bước sau.

## False positive và false negative

Leading indicator tạo sự đánh đổi (trade-off / 트레이드오프). Threshold quá nhạy tạo nhiều false alarm, làm nhóm (team / 팀) mệt và mất trust. Threshold quá rộng bỏ lỡ bài toán (problem / 문제) cho tới khi lagging kết quả (outcome / 결과) xấu xuất hiện.

Đo lường (measurement / 측정) thiết kế (design / 설계) phải cân chi phí (cost / 비용) của false positive và false negative. Privacy/bảo mật (security / 보안) điều khiển (control / 제어) có thể chấp nhận nhiều alert dư hơn low-impact nội bộ (internal / 내부) workflow vì chi phí (cost / 비용) bỏ sót cao hơn.

Threshold vì vậy là rủi ro (risk / 위험) quyết định (decision / 결정), không chỉ statistical tuning.

> **Nối mạch:** **Baseline, actual và forecast** nối từ **False positive và false negative** sang **Forecast calibration: dự báo tốt không chỉ là “gần đúng một lần”**, vì cơ chế trước tạo đầu vào cho bước sau.

## Baseline, actual và forecast

Baseline là tham chiếu (reference / 참조) đã được phê duyệt. Actual cho biết điều đã xảy ra. Forecast ước lượng điều có khả năng xảy ra tiếp theo dựa trên hiện tại (current / 현재) bằng chứng (evidence / 증거).

Ba lớp này không nên trộn. Nếu forecast xấu, không được sửa baseline chỉ để dashboard đẹp. Nếu phạm vi (scope / 범위) hoặc chiến lược (strategy / 전략) đã formally đổi, giữ baseline cũ mãi cũng mất ý nghĩa. Rebaseline phải là quản trị (governance / 거버넌스) quyết định (decision / 결정) có rationale, không phải cosmetic hành động (action / 동작).

> **Nối mạch:** **Forecast calibration: dự báo tốt không chỉ là “gần đúng một lần”** nối từ **Baseline, actual và forecast** sang **Forecast stability và forecast responsiveness**, vì cơ chế trước tạo đầu vào cho bước sau.

## Forecast calibration: dự báo tốt không chỉ là “gần đúng một lần”

Một forecast có thể nhìn chính xác do may mắn. Calibration hỏi prediction có đáng tin qua nhiều lần hay không. Nếu nhóm (team / 팀) thường nói “80% confidence” nhưng chỉ đúng khoảng một nửa số lần, confidence ngôn ngữ (language / 언어) đang overconfident.

Không cần hệ thống thống kê phức tạp để bắt đầu. Có thể lưu forecast theo status date, phạm vi (range / 범위)/confidence, actual kết quả (outcome / 결과) và reason variance. Sau vài milestone, nhóm (team / 팀) sẽ thấy estimate nào thường độ lệch (bias / 편향), phụ thuộc (dependency / 의존성) nào gây tail và ngữ cảnh (context / 맥락) nào làm historical mô hình (model / 모델) mất hiệu lực.

Forecast nên được versioned thay vì overwrite. Nếu mỗi tuần chỉ giữ con số forecast mới nhất, organization mất bằng chứng (evidence / 증거) về forecast chất lượng (quality / 품질) và không học được từ độ lệch (bias / 편향).

> **Nối mạch:** **Forecast stability và forecast responsiveness** nối từ **Forecast calibration: dự báo tốt không chỉ là “gần đúng một lần”** sang **Status không phải màu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Forecast stability và forecast responsiveness

Forecast quá ổn định có thể là dấu hiệu không absorb bằng chứng (evidence / 증거); forecast thay mỗi ngày có thể là noise chasing. Một mô hình (model / 모델) tốt đủ responsive với material tín hiệu (signal / 신호) nhưng không react quá mạnh với random fluctuation.

Đây là sự đánh đổi (trade-off / 트레이드오프) giống điều khiển (control / 제어) hệ thống (system / 시스템): cập nhật (update / 업데이트) quá chậm tạo lag; cập nhật (update / 업데이트) quá nhanh với noise tạo oscillation. Cadence nên match tốc độ hệ thống (system / 시스템) thay đổi và chi phí (cost / 비용) của quyết định (decision / 결정).

> **Nối mạch:** **Status không phải màu** nối từ **Forecast stability và forecast responsiveness** sang **Status narrative phải giải thích nhân quả (causal / 인과적) story**, vì cơ chế trước tạo đầu vào cho bước sau.

## Status không phải màu

Red/amber/green có thể hữu ích nhưng dễ che bất định (uncertainty / 불확실성). Một status report mạnh thường nối mục tiêu (objective / 목표)/milestone với hiện tại (current / 현재) bằng chứng (evidence / 증거), trend, forecast, key rủi ro (risk / 위험)/issue, quyết định (decision / 결정) needed và confidence.

Dự án (project / 프로젝트) “green” nhưng không có bằng chứng (evidence / 증거) cho adoption hoặc tích hợp (integration / 통합) readiness có thể chỉ đang đo tác vụ (task / 작업) completion. Status phải phản ánh success mô hình (model / 모델), không chỉ activity.

Một report hữu ích thường trả lời bốn câu: ta đang ở đâu so với mục tiêu (objective / 목표), điều gì thay đổi từ lần trước, nếu không làm gì thì forecast là gì, và quyết định (decision / 결정) nào cần ai đưa ra khi nào.

> **Nối mạch:** **Status narrative phải giải thích nhân quả (causal / 인과적) story** nối từ **Status không phải màu** sang **Confidence và bất định (uncertainty / 불확실성) trong reporting**, vì cơ chế trước tạo đầu vào cho bước sau.

## Status narrative phải giải thích nhân quả (causal / 인과적) story

Hai dự án (project / 프로젝트) cùng `amber` có thể cần quyết định (decision / 결정) hoàn toàn khác. Một dự án (project / 프로젝트) amber vì known vendor delay có contingency; dự án (project / 프로젝트) khác amber vì yêu cầu (requirement / 요구사항) ambiguity chưa có đơn vị sở hữu (owner / 오너).

Status nên giải thích driver, not just label. Trend và nhân quả (causal / 인과적) story giúp quản trị (governance / 거버넌스) biết liệu cần thêm tài nguyên (resource / 자원), quyết định (decision / 결정), rủi ro (risk / 위험) acceptance hay chỉ tiếp tục monitor.

Color without story dễ biến quản trị (governance / 거버넌스) thành reaction to formatting.

> **Nối mạch:** **Confidence và bất định (uncertainty / 불확실성) trong reporting** nối từ **Status narrative phải giải thích nhân quả (causal / 인과적) story** sang **Percent complete đặc biệt dễ gây ảo giác**, vì cơ chế trước tạo đầu vào cho bước sau.

## Confidence và bất định (uncertainty / 불확실성) trong reporting

Một ngày forecast duy nhất dễ tạo false precision. Khi bất định (uncertainty / 불확실성) cao, phạm vi (range / 범위) hoặc confidence statement trung thực hơn. Ví dụ “P80 hoàn thành trước 30/11” chứa thông tin (information / 정보) khác hoàn toàn “deadline 30/11”.

PM không cần biến mọi report thành thống kê nâng cao, nhưng nên tránh trình bày estimate như fact. Confidence phải thay đổi khi bằng chứng (evidence / 증거) thay đổi.

Nếu bất định (uncertainty / 불확실성) tăng nhưng report vẫn giữ cùng một màu xanh chỉ vì mục tiêu (target / 대상) date chưa chính thức trượt, status hệ thống (system / 시스템) đang phản ứng quá muộn.

> **Nối mạch:** **Percent complete đặc biệt dễ gây ảo giác** nối từ **Confidence và bất định (uncertainty / 불확실성) trong reporting** sang **Chỉ số (metric / 지표) portfolio thay vì single chỉ số (metric / 지표)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Percent complete đặc biệt dễ gây ảo giác

Một tác vụ (task / 작업) “90% complete” không nói rõ 10% còn lại là documentation dễ làm hay tích hợp (integration / 통합) unknown có thể kéo dài ba tuần. Percent complete càng chủ quan khi công việc (work / 작업) chưa có mục tiêu (objective / 목표) completion criterion.

Deliverable-based bằng chứng (evidence / 증거) thường tốt hơn subjective completion percentage: yêu cầu (requirement / 요구사항) accepted, môi trường (environment / 환경) ready, giao diện (interface / 인터페이스) integrated, kiểm thử (test / 테스트) passed, regulatory bằng chứng (evidence / 증거) approved. Với adaptive công việc (work / 작업), usable increment hoặc luồng (flow / 흐름) trạng thái (state / 상태) có thể informative hơn phần trăm.

Nếu bắt buộc dùng percent complete, definition và earning quy tắc (rule / 규칙) phải nhất quán; nếu không chỉ số (metric / 지표) dễ tăng đều cho đến 90% rồi đứng yên rất lâu.

> **Nối mạch:** **Chỉ số (metric / 지표) portfolio thay vì single chỉ số (metric / 지표)** nối từ **Percent complete đặc biệt dễ gây ảo giác** sang **Variance → diagnosis → phản hồi (response / 응답)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chỉ số (metric / 지표) portfolio thay vì single chỉ số (metric / 지표)

Một chỉ số (metric / 지표) duy nhất dễ bị tối ưu cục bộ. thông lượng (throughput / 처리량) nên đi với cycle thời gian (time / 시간)/chất lượng (quality / 품질); adoption nên đi với hỗ trợ (support / 지원)/lỗi (error / 오류); chi phí (cost / 비용) efficiency nên đi với kết quả (outcome / 결과)/rủi ro (risk / 위험).

Chỉ số (metric / 지표) portfolio không có nghĩa dashboard 50 KPI. Chỉ cần đủ counter-signal để chỉ số (metric / 지표) chính không che side tác động (effect / 효과).

Một mẫu (pattern / 패턴) tốt là kết quả (outcome / 결과) chỉ số (metric / 지표) + luồng (flow / 흐름)/leading chỉ số (metric / 지표) + rủi ro (risk / 위험)/chất lượng (quality / 품질) guardrail. Cấu trúc cụ thể tùy mục tiêu (objective / 목표).

> **Nối mạch:** **Variance → diagnosis → phản hồi (response / 응답)** nối từ **Chỉ số (metric / 지표) portfolio thay vì single chỉ số (metric / 지표)** sang **Threshold và hành động (action / 동작) quy tắc (rule / 규칙) phải tồn tại trước crisis**, vì cơ chế trước tạo đầu vào cho bước sau.

## Variance → diagnosis → phản hồi (response / 응답)

Khi variance xuất hiện, trình tự tốt là xác nhận dữ liệu (data / 데이터), tìm cause, đánh giá impact, xem threshold/authority, chọn phản hồi (response / 응답), cập nhật (update / 업데이트) forecast và communicate. Jump ngay từ “delay” sang “overtime” có thể giải quyết symptom và tăng chất lượng (quality / 품질) rủi ro (risk / 위험).

Variance phân tích (analysis / 분석) nên tách common-cause variation khỏi special-cause tín hiệu (signal / 신호) khi phù hợp. Một nhóm (team / 팀) có cycle thời gian (time / 시간) dao động tự nhiên 3–5 ngày không nên bị escalated vì một item mất 5 ngày. Nhưng hàng đợi (queue / 큐) tăng liên tục ba tuần có thể là hệ thống (system / 시스템) thay đổi (change / 변경) cần investigation.

> **Nối mạch:** **Threshold và hành động (action / 동작) quy tắc (rule / 규칙) phải tồn tại trước crisis** nối từ **Variance → diagnosis → phản hồi (response / 응답)** sang **Threshold hysteresis và alert flapping**, vì cơ chế trước tạo đầu vào cho bước sau.

## Threshold và hành động (action / 동작) quy tắc (rule / 규칙) phải tồn tại trước crisis

Chỉ số (metric / 지표) không tạo điều khiển (control / 제어) nếu không ai biết khi nào phải hành động (action / 동작). Threshold có thể là hard ranh giới (boundary / 경계) như regulatory tolerance hoặc soft trigger như “cycle thời gian (time / 시간) P85 tăng hơn 20% trong ba tuần”.

Threshold tốt không tự động hóa mọi quyết định (decision / 결정); nó kích hoạt rà soát (review / 검토) thích hợp. Nếu threshold bị vượt nhưng phản hồi (response / 응답) phụ thuộc ngữ cảnh (context / 맥락), playbook có thể nói ai rà soát (review / 검토), bằng chứng (evidence / 증거) nào cần và authority nào quyết.

Nếu threshold chỉ được định nghĩa sau khi bài toán (problem / 문제) xảy ra, organization dễ chọn quy tắc (rule / 규칙) thuận tiện để giải thích kết quả (outcome / 결과) thay vì quy tắc (rule / 규칙) giúp kiểm soát trước đó.

> **Nối mạch:** **Threshold hysteresis và alert flapping** nối từ **Threshold và hành động (action / 동작) quy tắc (rule / 규칙) phải tồn tại trước crisis** sang **Vanity chỉ số (metric / 지표) và Goodhart tác động (effect / 효과)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Threshold hysteresis và alert flapping

Nếu chỉ số (metric / 지표) dao động quanh một threshold, status có thể nhảy green/amber liên tục. Điều này tạo noise và overreaction.

Một số hệ thống (system / 시스템) cần hysteresis: trigger hành động (action / 동작) khi vượt ranh giới (boundary / 경계) đủ lâu hoặc quay về normal khi bằng chứng (evidence / 증거) phục hồi đủ rõ. Không phải mọi chỉ số (metric / 지표) cần kỹ thuật này, nhưng mô hình tư duy (mental model / 사고 모델) hữu ích: điều khiển (control / 제어) trạng thái (state / 상태) không nên flip vì một dữ liệu (data / 데이터) điểm (point / 지점) random.

> **Nối mạch:** **Vanity chỉ số (metric / 지표) và Goodhart tác động (effect / 효과)** nối từ **Threshold hysteresis và alert flapping** sang **Đo lường (measurement / 측정) cần denominator và ngữ cảnh (context / 맥락)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vanity chỉ số (metric / 지표) và Goodhart tác động (effect / 효과)

Vanity chỉ số (metric / 지표) trông tích cực nhưng không hỗ trợ quyết định (decision / 결정), như số meeting, số page tài liệu hoặc số ticket đóng mà không có ngữ cảnh (context / 맥락). Goodhart tác động (effect / 효과) xuất hiện khi chỉ số (metric / 지표) trở thành mục tiêu (target / 대상) và người ta tối ưu cách tính chỉ số (metric / 지표).

Nếu velocity trở thành KPI cá nhân/nhóm (team / 팀), story điểm (point / 지점) có thể phình ra. Nếu defect count thấp được thưởng, nhóm (team / 팀) có incentive redefine defect. điều khiển (control / 제어) tốt cần chỉ số (metric / 지표) portfolio thay vì một số đơn lẻ và cần kiểm tra (audit / 감사) ngữ nghĩa (semantic / 의미적) definition.

> **Nối mạch:** **Vanity chỉ số (metric / 지표) và Goodhart tác động (effect / 효과)** đặt vấn đề; **Đo lường (measurement / 측정) cần denominator và ngữ cảnh (context / 맥락)** kiểm tra bằng chứng, rồi **Aggregation mất mát (loss / 손실)** mở rộng hệ quả.

## Đo lường (measurement / 측정) cần denominator và ngữ cảnh (context / 맥락)

“Có 20 defect” ít thông tin (information / 정보) nếu không biết bản phát hành (release / 릴리스) kích thước (size / 크기), severity, detection stage hoặc trend. “chi phí (cost / 비용) tăng 10%” cần biết baseline chất lượng (quality / 품질) và phạm vi (scope / 범위) thay đổi (change / 변경). Relative measure thường cần denominator để tránh kết luận sai.

Chỉ số (metric / 지표) cũng cần segmentation. Average có thể che tail. người dùng (user / 사용자) onboarding trung bình 3 phút nhưng 10% người dùng (user / 사용자) mất 20 phút có thể là bài toán (problem / 문제) lớn nếu nhóm đó là customer chiến lược.

> **Nối mạch:** **Đo lường (measurement / 측정) cần denominator và ngữ cảnh (context / 맥락)** đặt vấn đề; **Aggregation mất mát (loss / 손실)** kiểm tra bằng chứng, rồi **Quyết định (decision / 결정) độ trễ (latency / 지연 시간) như một chỉ số (metric / 지표) hệ thống** mở rộng hệ quả.

## Aggregation mất mát (loss / 손실)

Khi chỉ số (metric / 지표) được aggregate từ nhóm (team / 팀) → program → executive, detail bị mất. Average schedule status có thể che một phụ thuộc (dependency / 의존성) red quyết định toàn kết quả (outcome / 결과).

Aggregation nên preserve exception material. Executive không cần mọi tác vụ (task / 작업), nhưng cần biết tail/threshold breach và bất định (uncertainty / 불확실성) quan trọng.

Nếu summary luôn làm dữ liệu (data / 데이터) “mượt hơn”, quản trị (governance / 거버넌스) có compression độ lệch (bias / 편향).

> **Nối mạch:** **Quyết định (decision / 결정) độ trễ (latency / 지연 시간) như một chỉ số (metric / 지표) hệ thống** nối từ **Aggregation mất mát (loss / 손실)** sang **Thông tin (information / 정보) độ trễ (latency / 지연 시간) và hành động (action / 동작) độ trễ (latency / 지연 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quyết định (decision / 결정) độ trễ (latency / 지연 시간) như một chỉ số (metric / 지표) hệ thống

Dự án (project / 프로젝트) có thể delivery chậm không phải vì nhóm (team / 팀) làm chậm mà vì quyết định (decision / 결정) chậm. Thời gian từ khi issue được nêu đến khi authority ra quyết định là quyết định (decision / 결정) độ trễ (latency / 지연 시간).

Đo quyết định (decision / 결정) độ trễ (latency / 지연 시간) đặc biệt hữu ích trong ma trận (matrix / 행렬)/hybrid organization. Nếu mọi blocker chờ steering committee hai tuần, thêm nhà phát triển (developer / 개발자) không giải quyết thông lượng (throughput / 처리량).

Có thể tách quyết định (decision / 결정) độ trễ (latency / 지연 시간) thành waiting-for-information, waiting-for-authority và rework-after-decision. Ba phần này dẫn đến intervention khác nhau.

> **Nối mạch:** **Thông tin (information / 정보) độ trễ (latency / 지연 시간) và hành động (action / 동작) độ trễ (latency / 지연 시간)** nối từ **Quyết định (decision / 결정) độ trễ (latency / 지연 시간) như một chỉ số (metric / 지표) hệ thống** sang **Benefit đo lường (measurement / 측정) và vấn đề attribution**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thông tin (information / 정보) độ trễ (latency / 지연 시간) và hành động (action / 동작) độ trễ (latency / 지연 시간)

Đo lường (measurement / 측정) có thể đúng nhưng đến quá muộn. thông tin (information / 정보) độ trễ (latency / 지연 시간) là thời gian từ sự kiện (event / 이벤트) xảy ra đến bằng chứng (evidence / 증거) available. hành động (action / 동작) độ trễ (latency / 지연 시간) là thời gian từ bằng chứng (evidence / 증거) tới intervention.

End-to-end điều khiển (control / 제어) độ trễ (latency / 지연 시간) = thông tin (information / 정보) độ trễ (latency / 지연 시간) + quyết định (decision / 결정) độ trễ (latency / 지연 시간) + hành động (action / 동작) độ trễ (latency / 지연 시간). Đây là chỉ số (metric / 지표) mạnh để hiểu vì sao organization “biết vấn đề nhưng vẫn phản ứng chậm”.

Automation có thể giảm capture độ trễ (latency / 지연 시간); delegation giảm quyết định (decision / 결정) độ trễ (latency / 지연 시간); pre-approved playbook giảm hành động (action / 동작) độ trễ (latency / 지연 시간).

> **Nối mạch:** **Thông tin (information / 정보) độ trễ (latency / 지연 시간) và hành động (action / 동작) độ trễ (latency / 지연 시간)** đặt vấn đề; **Benefit đo lường (measurement / 측정) và vấn đề attribution** kiểm tra bằng chứng, rồi **Benefit decay và unintended consequence** mở rộng hệ quả.

## Benefit đo lường (measurement / 측정) và vấn đề attribution

Sau go-live, kết quả (outcome / 결과) cải thiện không tự động chứng minh dự án (project / 프로젝트) gây ra toàn bộ improvement. thị trường (market / 시장) thay đổi, seasonal tác động (effect / 효과), chính sách (policy / 정책) khác hoặc campaign marketing có thể cùng tác động. Đây là vấn đề attribution.

Trong nhiều dự án (project / 프로젝트) không thể làm experiment hoàn hảo, nhưng vẫn có thể lập luận (reasoning / 추론) tốt hơn bằng baseline, comparison cohort nếu có, pre/post trend và giả định (assumption / 가정) rõ. Claim “automation giảm chi phí (cost / 비용) 30%” mạnh hơn nếu biết volume, staffing chính sách (policy / 정책) và demand không đổi đáng kể; nếu tất cả cùng thay, conclusion cần thận trọng hơn.

Benefit đơn vị sở hữu (owner / 오너) nên phân biệt đo lường (measurement / 측정) với nhân quả (causal / 인과적) claim. Đo được KPI tăng là một chuyện; chứng minh investment tạo phần tăng đó là chuyện khác.

> **Nối mạch:** **Benefit đo lường (measurement / 측정) và vấn đề attribution** đặt vấn đề; **Benefit decay và unintended consequence** kiểm tra bằng chứng, rồi **Lessons learned như kiến thức (knowledge / 지식) vòng lặp (loop / 루프)** mở rộng hệ quả.

## Benefit decay và unintended consequence

Benefit có thể giảm theo thời gian vì người dùng (user / 사용자) hành vi (behavior / 동작), competitor phản hồi (response / 응답), maintenance chi phí (cost / 비용) hoặc tiến trình (process / 프로세스) drift. Vì vậy đo lường (measurement / 측정) chỉ tại go-live + 1 tháng có thể quá sớm.

Kết quả (outcome / 결과) tốt cũng có side tác động (effect / 효과): automation giảm handling thời gian (time / 시간) nhưng complaint tăng; self-service giảm contact center volume nhưng chuyển complex trường hợp (case / 사례) sang specialist, làm average handling thời gian (time / 시간) phần còn lại tăng.

Benefit đo lường (measurement / 측정) cần guardrail và thời gian (time / 시간) horizon, không chỉ headline KPI.

> **Nối mạch:** **Lessons learned như kiến thức (knowledge / 지식) vòng lặp (loop / 루프)** nối từ **Benefit decay và unintended consequence** sang **Kiến thức (knowledge / 지식) retention và retrieval**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lessons learned như kiến thức (knowledge / 지식) vòng lặp (loop / 루프)

Lessons learned không nên chỉ viết lúc close. Nếu insight có thể giúp dự án (project / 프로젝트) hiện tại, nên capture và áp dụng ngay. Retrospective, sự cố (incident / 인시던트) rà soát (review / 검토) và milestone rà soát (review / 검토) đều là học tập (learning / 학습) vòng lặp (loop / 루프).

Một “lesson” hữu ích không chỉ kể chuyện; nó nêu ngữ cảnh (context / 맥락), tín hiệu (signal / 신호), cause/contributing factor, hành động (action / 동작) và điều kiện áp dụng. Organizational tiến trình (process / 프로세스) Assets chỉ có giá trị nếu người sau tìm và dùng được.

“Vendor communication cần tốt hơn” không phải lesson đủ actionable. “API lược đồ (schema / 스키마) thay đổi (change / 변경) không có versioning làm UAT rework; dự án (project / 프로젝트) sau cần đặc tả hợp đồng (contract / 계약) yêu cầu notice period và backward tính tương thích (compatibility / 호환성)” có ngữ cảnh (context / 맥락) và cơ chế (mechanism / 메커니즘) rõ hơn.

> **Nối mạch:** **Kiến thức (knowledge / 지식) retention và retrieval** nối từ **Lessons learned như kiến thức (knowledge / 지식) vòng lặp (loop / 루프)** sang **Retrospective và post-mortem khác blame session**, vì cơ chế trước tạo đầu vào cho bước sau.

## Kiến thức (knowledge / 지식) retention và retrieval

Lesson tồn tại nhưng không được tìm thấy thì organizational học tập (learning / 학습) bằng zero. học tập (learning / 학습) hệ thống (system / 시스템) cần taxonomy/tìm kiếm (search / 검색), đơn vị sở hữu (owner / 오너) hoặc tích hợp (integration / 통합) vào template/checklist nơi relevant.

Một lesson có expiry/ngữ cảnh (context / 맥락). Practice tốt cho monolith 2018 có thể không phù hợp cloud-native 2026. Reuse cần relevance check, không bản sao (copy / 복사) blind.

Kiến thức (knowledge / 지식) vòng lặp (loop / 루프) hoàn chỉnh là capture → abstract cơ chế (mechanism / 메커니즘) → store → retrieve → apply → cập nhật (update / 업데이트).

> **Nối mạch:** **Retrospective và post-mortem khác blame session** nối từ **Kiến thức (knowledge / 지식) retention và retrieval** sang **Hành động (action / 동작) item closure phải kiểm tra effectiveness**, vì cơ chế trước tạo đầu vào cho bước sau.

## Retrospective và post-mortem khác blame session

Mục tiêu của rà soát (review / 검토) là tăng hệ thống (system / 시스템) năng lực (capability / 역량), không tìm người để quy trách nhiệm. Accountability vẫn cần, nhưng blame làm thông tin (information / 정보) bị che ở lần sau.

Một rà soát (review / 검토) trưởng thành tách sự kiện (event / 이벤트) timeline, contributing điều kiện (condition / 조건), điều khiển (control / 제어) đã thất bại (fail / 실패), quyết định (decision / 결정) ngữ cảnh (context / 맥락) và corrective hành động (action / 동작). hành động (action / 동작) nên có đơn vị sở hữu (owner / 오너) và xác minh (verification / 확인), nếu không lesson chỉ là narrative.

> **Nối mạch:** **Hành động (action / 동작) item closure phải kiểm tra effectiveness** nối từ **Retrospective và post-mortem khác blame session** sang **Closure là chuyển responsibility, không chỉ đóng ticket**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hành động (action / 동작) item closure phải kiểm tra effectiveness

Post-mortem hành động (action / 동작) “thêm checklist” không nên được coi là done chỉ vì checklist đã publish. Cần bằng chứng (evidence / 증거) rằng điều khiển (control / 제어) mới được dùng và thất bại (failure / 실패) mẫu (pattern / 패턴) giảm.

Otherwise organization tích corrective-action inventory nhưng hệ thống (system / 시스템) năng lực (capability / 역량) không thay đổi.

> **Nối mạch:** **Closure là chuyển responsibility, không chỉ đóng ticket** nối từ **Hành động (action / 동작) item closure phải kiểm tra effectiveness** sang **Closure là rủi ro (risk / 위험) transfer sự kiện (event / 이벤트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Closure là chuyển responsibility, không chỉ đóng ticket

Dự án (project / 프로젝트) closure (đóng dự án / 프로젝트 종료) xác nhận acceptance, xử lý obligation, chuyển giao deliverable/kiến thức (knowledge / 지식), đóng đặc tả hợp đồng (contract / 계약)/finance, bản phát hành (release / 릴리스) tài nguyên (resource / 자원), archive bằng chứng (evidence / 증거) và ghi học tập (learning / 학습). Với dự án (project / 프로젝트) bị terminate sớm, closure vẫn cần diễn ra để bảo toàn kiến thức (knowledge / 지식), legal/financial obligation và asset.

Chuyển tiếp (transition / 전이) readiness quan trọng hơn một chữ ký hình thức. Operations phải có monitoring, runbook, truy cập (access / 접근), huấn luyện (training / 학습), hỗ trợ (support / 지원) mô hình (model / 모델), quay lui (rollback / 롤백)/khôi phục (recovery / 복구) và quyền sở hữu (ownership / 소유권) phù hợp với kiểu (type / 타입) of deliverable.

Closure nên xác định rõ open item nào được chuyển sang thao tác (operation / 연산), sản phẩm (product / 제품) backlog hoặc separate dự án (project / 프로젝트). “Đóng dự án (project / 프로젝트)” không được biến unfinished responsibility thành orphan công việc (work / 작업).

> **Nối mạch:** **Closure là rủi ro (risk / 위험) transfer sự kiện (event / 이벤트)** nối từ **Closure là chuyển responsibility, không chỉ đóng ticket** sang **Operational readiness phải được chứng minh bằng bằng chứng (evidence / 증거)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Closure là rủi ro (risk / 위험) transfer sự kiện (event / 이벤트)

Khi dự án (project / 프로젝트) nhóm (team / 팀) giải tán, residual rủi ro (risk / 위험) không biến mất; nó chuyển sang sản phẩm (product / 제품)/operations/nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너). Transfer chỉ thật khi receiving đơn vị sở hữu (owner / 오너) hiểu exposure, có authority/sức chứa (capacity / 용량) và chấp nhận nó.

Một open defect danh sách (list / 목록) được gửi email không phải rủi ro (risk / 위험) transfer nếu operations không biết severity hoặc không có ngân sách (budget / 예산) xử lý.

Closure gói (package / 패키지) nên làm residual rủi ro (risk / 위험), warranty/hỗ trợ (support / 지원) cửa sổ (window / 윈도우), unresolved claim và phụ thuộc (dependency / 의존성) visible.

> **Nối mạch:** **Closure là rủi ro (risk / 위험) transfer sự kiện (event / 이벤트)** đặt vấn đề; **Operational readiness phải được chứng minh bằng bằng chứng (evidence / 증거)** kiểm tra bằng chứng, rồi **Legacy decommission cũng là một phần của chuyển tiếp (transition / 전이)** mở rộng hệ quả.

## Operational readiness phải được chứng minh bằng bằng chứng (evidence / 증거)

Một handover meeting không chứng minh thao tác (operation / 연산) sẵn sàng. Readiness có thể cần bằng chứng (evidence / 증거) như hỗ trợ (support / 지원) quyền sở hữu (ownership / 소유권) đã nhận, truy cập (access / 접근) được kiểm thử (test / 테스트), monitoring alert tới đúng người, backup/restore hoặc quay lui (rollback / 롤백) được diễn tập, unresolved defect được risk-accepted và supplier hỗ trợ (support / 지원) channel hoạt động.

Các tiêu chí này nên được định nghĩa trước go-live, không phải sáng tạo vào ngày closure. Khi readiness là gate, cần phân biệt mandatory criterion với desirable criterion để tránh vừa khối (block / 블록) vô lý vừa waive mọi thứ dưới áp lực deadline.

Nếu thao tác (operation / 연산) chỉ ký acceptance vì dự án (project / 프로젝트) nhóm (team / 팀) sắp giải tán, administrative closure đã lấn át rủi ro (risk / 위험) transfer.

> **Nối mạch:** **Operational readiness phải được chứng minh bằng bằng chứng (evidence / 증거)** đặt vấn đề; **Legacy decommission cũng là một phần của chuyển tiếp (transition / 전이)** kiểm tra bằng chứng, rồi **Acceptance không đồng nghĩa benefit realization** mở rộng hệ quả.

## Legacy decommission cũng là một phần của chuyển tiếp (transition / 전이)

New hệ thống (system / 시스템) go-live nhưng old hệ thống (system / 시스템) sống vô hạn tạo duplicate tiến trình (process / 프로세스), chi phí (cost / 비용), dữ liệu (data / 데이터) inconsistency và bảo mật (security / 보안) exposure.

Decommission cần retention/archive, dữ liệu (data / 데이터) reconciliation, người dùng (user / 사용자) di chuyển (migration / 마이그레이션), đặc tả hợp đồng (contract / 계약)/license closure, truy cập (access / 접근) revoke và fallback quyết định (decision / 결정). Có thể giữ parallel run có chủ đích trong stabilization, nhưng phải có exit criterion.

Dự án (project / 프로젝트) phạm vi (scope / 범위) bỏ decommission thường chỉ chuyển hidden chi phí (cost / 비용) sang operations.

> **Nối mạch:** **Acceptance không đồng nghĩa benefit realization** nối từ **Legacy decommission cũng là một phần của chuyển tiếp (transition / 전이)** sang **Benefit realization có thể sống sau dự án (project / 프로젝트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Acceptance không đồng nghĩa benefit realization

Customer hoặc sponsor có thể accept deliverable vì nó đáp ứng agreed criteria, nhưng benefit vẫn chưa xuất hiện. Một hệ thống có thể pass UAT nhưng adoption thấp. Vì vậy acceptance chứng minh đầu ra (output / 출력) đủ chuẩn; benefits tracking chứng minh kết quả (outcome / 결과)/giá trị (value / 값).

Hai khái niệm này cần đơn vị sở hữu (owner / 오너) khác nhau trong nhiều organization.

> **Nối mạch:** **Benefit realization có thể sống sau dự án (project / 프로젝트)** nối từ **Acceptance không đồng nghĩa benefit realization** sang **Premature closure và endless dự án (project / 프로젝트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Benefit realization có thể sống sau dự án (project / 프로젝트)

Một dự án (project / 프로젝트) kết thúc không đồng nghĩa benefit đã xuất hiện. Ví dụ hệ thống tự động hóa go-live tháng 12 nhưng chi phí (cost / 비용) saving chỉ đo rõ sau sáu tháng. Benefit đơn vị sở hữu (owner / 오너) và đo lường (measurement / 측정) plan phải tiếp tục sau closure nếu cần.

Điều này nối dự án (project / 프로젝트) management với sản phẩm (product / 제품)/operations/portfolio quản trị (governance / 거버넌스): dự án (project / 프로젝트) bàn giao năng lực (capability / 역량), organization tiếp tục khai thác giá trị (value / 값).

Benefit chỉ số (metric / 지표) nên có baseline trước dự án (project / 프로젝트) nếu có thể. Nếu không biết trạng thái trước, rất khó chứng minh thay đổi (change / 변경) sau dự án (project / 프로젝트) thực sự đến từ investment.

> **Nối mạch:** **Premature closure và endless dự án (project / 프로젝트)** nối từ **Benefit realization có thể sống sau dự án (project / 프로젝트)** sang **Continuous improvement**, vì cơ chế trước tạo đầu vào cho bước sau.

## Premature closure và endless dự án (project / 프로젝트)

Premature closure xảy ra khi administrative deadline quan trọng hơn readiness, khiến thao tác (operation / 연산) nhận hệ thống (system / 시스템) chưa ổn. Ngược lại, dự án (project / 프로젝트) kéo dài vô tận khi mọi enhancement sau go-live đều được giữ trong dự án (project / 프로젝트) thay vì chuyển sản phẩm (product / 제품)/operations quyền sở hữu (ownership / 소유권).

Closure ranh giới (boundary / 경계) cần được định nghĩa từ charter/vòng đời (lifecycle / 생명주기): deliverable nào thuộc temporary dự án (project / 프로젝트), ongoing improvement nào thuộc thao tác (operation / 연산) hoặc sản phẩm (product / 제품) vòng đời (lifecycle / 생명주기).

> **Nối mạch:** **Continuous improvement** nối từ **Premature closure và endless dự án (project / 프로젝트)** sang **Improvement WIP và thay đổi (change / 변경) fatigue**, vì cơ chế trước tạo đầu vào cho bước sau.

## Continuous improvement

Continuous improvement (cải tiến liên tục / 지속적 개선) dùng phản hồi (feedback / 피드백) để thay tiến trình (process / 프로세스), năng lực (capability / 역량) hoặc môi trường (environment / 환경). Cải tiến không nhất thiết là dự án (project / 프로젝트) lớn; nhiều thay đổi nhỏ có compounding tác động (effect / 효과).

Tuy nhiên thay tiến trình (process / 프로세스) liên tục cũng có chi phí (cost / 비용). Một experiment cải tiến nên có hypothesis và tín hiệu (signal / 신호): “giới hạn WIP từ 10 xuống 6 có giảm cycle thời gian (time / 시간) mà không làm thông lượng (throughput / 처리량) giảm đáng kể không?”. Như vậy retrospective trở thành học tập (learning / 학습) hệ thống (system / 시스템) thay vì meeting cảm tính.

Improvement cần ổn định đủ lâu để đo. Nếu nhóm (team / 팀) đổi tiến trình (process / 프로세스) mỗi tuần, khó phân biệt tác động (effect / 효과) của thay đổi nào.

> **Nối mạch:** **Improvement WIP và thay đổi (change / 변경) fatigue** nối từ **Continuous improvement** sang **Điều khiển (control / 제어) chart và tiến trình (process / 프로세스) stability ở mức mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Improvement WIP và thay đổi (change / 변경) fatigue

Nhóm (team / 팀) cũng có thể overcommit improvement. Mười hành động (action / 동작) từ retrospective nhưng không ai có sức chứa (capacity / 용량) chỉ tạo guilt và stale backlog.

Giới hạn số improvement active giúp học tập (learning / 학습) vòng lặp (loop / 루프) hoàn tất. Chọn leverage điểm (point / 지점) cao, verify tác động (effect / 효과), rồi mới thêm thay đổi (change / 변경) khác.

Continuous improvement không có nghĩa continuous disturbance.

> **Nối mạch:** Control chart và process stability cung cấp khung đọc; **Improvement WIP và change fatigue** cho thấy giới hạn của cải tiến liên tục. **Metric cũng cần lifecycle và retirement** để tránh đo mãi một điều đã hết giá trị.

## Điều khiển (control / 제어) chart và tiến trình (process / 프로세스) stability ở mức mô hình tư duy (mental model / 사고 모델)

Không cần biến PMP thành khóa statistics, nhưng nên hiểu distinction giữa variation bình thường và tín hiệu (signal / 신호) bất thường. Nếu tiến trình (process / 프로세스) stable, phản ứng mạnh với từng fluctuation có thể làm hệ thống (system / 시스템) tệ hơn. Nếu mẫu (pattern / 패턴) thay đổi rõ, cần investigate special cause.

Mô hình tư duy (mental model / 사고 모델) này giúp tránh management by anecdote: một sự cố (incident / 인시던트) đơn lẻ không luôn chứng minh tiến trình (process / 프로세스) hỏng, nhưng trend và repeated tín hiệu (signal / 신호) cần hành động (action / 동작).

> **Nối mạch:** Metric lifecycle và retirement kết hợp với control chart để phân biệt tín hiệu thật với số liệu lỗi thời. **Software operations liên kết** đưa nguyên tắc đó vào vận hành.

## Chỉ số (metric / 지표) cũng cần vòng đời (lifecycle / 생명주기) và retirement

Một chỉ số (metric / 지표) hữu ích ở discovery có thể vô nghĩa ở operations. rủi ro (risk / 위험) count quan trọng lúc bất định (uncertainty / 불확실성) cao nhưng sau stabilization có thể nhường chỗ cho dịch vụ (service / 서비스) độ tin cậy (reliability / 신뢰성). Nếu dashboard chỉ thêm chỉ số (metric / 지표) mà không retire chỉ số (metric / 지표) cũ, attention bị phân tán và reporting chi phí (cost / 비용) tăng.

Mỗi chỉ số (metric / 지표) quan trọng nên có rà soát (review / 검토) điểm (point / 지점): nó còn giúp quyết định (decision / 결정) nào, đơn vị sở hữu (owner / 오너) còn dùng không, definition còn phù hợp không và collection chi phí (cost / 비용) có xứng đáng không. đo lường (measurement / 측정) hệ thống (system / 시스템) cũng cần continuous improvement.

> **Nối mạch:** Metric lifecycle cung cấp đầu vào; Software operations liên kết giải thích cách metric được dùng trong hệ thống. **Ví dụ lập luận** kiểm tra hệ quả.

## Software operations liên kết (connection / 연결)

Khi deliverable là software, go-live chỉ bắt đầu một vòng đời (lifecycle / 생명주기) mới. Xem [Delivery, configuration và operations](../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md) và [Maintenance, evolution và technical debt](../computer_science/09_software_engineering/04_maintenance_evolution_and_technical_debt.md) để hiểu sâu môi trường vận hành (production / 운영 환경) chuyển tiếp (transition / 전이) và long-term evolution.

> **Nối mạch:** **Software operations liên kết (connection / 연결)** nêu quy tắc; **Ví dụ lập luận (reasoning / 추론)** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Ví dụ lập luận (reasoning / 추론)

Một dự án (project / 프로젝트) báo 95% tác vụ (task / 작업) complete nhưng UAT pass tỷ lệ (rate / 비율) chỉ 55% và defect reopen tăng. Nếu chỉ nhìn percent complete, status có vẻ gần xong. Nhưng bằng chứng (evidence / 증거) về usable kết quả (outcome / 결과) cho thấy dự án (project / 프로젝트) còn bất định (uncertainty / 불확실성) lớn. PM nên chuyển focus sang chất lượng (quality / 품질)/tích hợp (integration / 통합) bottleneck, cập nhật (update / 업데이트) forecast và tránh tuyên bố gần hoàn tất chỉ vì planned tasks đã được bắt đầu hoặc code-complete.

Một dự án (project / 프로젝트) khác hoàn thành đúng ngân sách (budget / 예산) nhưng adoption sau ba tháng chỉ 20%. dự án (project / 프로젝트) delivery có thể đã đạt ràng buộc (constraint / 제약조건) nhưng nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과) chưa đạt. Benefits đơn vị sở hữu (owner / 오너) cần investigate huấn luyện (training / 학습), tiến trình (process / 프로세스) fit, incentive hoặc sản phẩm (product / 제품) usability thay vì coi closure administrative là success cuối cùng.

Một forecast bản phát hành (release / 릴리스) được báo “P80 trước 15/12” suốt bốn lần nhưng actual liên tục muộn hơn P80. Vấn đề không chỉ là lần dự báo hiện tại sai; forecasting mô hình (model / 모델) hoặc giả định (assumption / 가정) đang understate bất định (uncertainty / 불확실성). nhóm (team / 팀) cần rà soát (review / 검토) calibration, dùng chung (shared / 공유) phụ thuộc (dependency / 의존성)/correlation và historical cửa sổ (window / 윈도우) trước khi tiếp tục dùng cùng confidence label.

Một scenario đo lường (measurement / 측정): thông lượng (throughput / 처리량) tăng 20% sau automation nhưng escaped defect cũng tăng 40%. Nếu management chỉ nhìn thông lượng (throughput / 처리량), improvement có vẻ thành công. chỉ số (metric / 지표) portfolio cho thấy hệ thống (system / 시스템) đang đổi chất lượng (quality / 품질) lấy speed; nhóm (team / 팀) cần tìm optimum chứ không tiếp tục tối đa một proxy.

> **Nối mạch:** Ví dụ lập luận nêu quy tắc; **Mô hình tư duy** thử quy tắc trong tình huống cụ thể để khép mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> đo lường (measurement / 측정) là sensor hệ thống (system / 시스템): nó phải đo đúng reality đủ sớm, giữ ngữ nghĩa (semantic / 의미적) ổn định và kích hoạt hành động (action / 동작) phù hợp. Closure là sự kiện (event / 이벤트) chuyển quyền sở hữu (ownership / 소유권) và residual rủi ro (risk / 위험); continuous improvement chỉ hoàn tất khi hành động (action / 동작) được kiểm chứng thành năng lực (capability / 역량) mới, không phải khi retrospective kết thúc.

Tiếp theo: [AI, sustainability và bối cảnh dự án hiện đại](./12_ai_sustainability_and_modern_project_context.md).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
