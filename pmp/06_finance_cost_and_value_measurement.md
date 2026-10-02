# 06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **06 — Finance, cost, reserves và value measurement**. Route đi từ decision/value target → estimate → budget/funding → reserves and variance → value realization, để chi phí nối với lựa chọn và outcome.

## Chi phí (cost / 비용) management bắt đầu từ quyết định (decision / 결정), không từ spreadsheet

Quản lý chi phí (cost management / 비용 관리) trả lời dự án (project / 프로젝트) cần bao nhiêu tài nguyên (resource / 자원) tài chính, khi nào cần, confidence ra sao, và deviation có ý nghĩa gì đối với giá trị (value / 값)/nghiệp vụ (business / 비즈니스) trường hợp (case / 사례). ngân sách (budget / 예산) không chỉ là trần chi tiêu; nó là một ràng buộc (constraint / 제약조건) gắn với phạm vi (scope / 범위), schedule, chất lượng (quality / 품질) và rủi ro (risk / 위험).

Một dự án (project / 프로젝트) under ngân sách (budget / 예산) vẫn có thể thất bại nếu không tạo kết quả (outcome / 결과). Một dự án (project / 프로젝트) over initial estimate vẫn có thể hợp lý nếu expected giá trị (value / 값) tăng nhiều hơn và quản trị (governance / 거버넌스) chấp nhận sự đánh đổi (trade-off / 트레이드오프). Vì vậy chi phí (cost / 비용) phải luôn được đọc trong hệ thống giá trị (value / 값)–rủi ro (risk / 위험)–phạm vi (scope / 범위) chứ không riêng lẻ.

Finance ở dự án (project / 프로젝트) mức (level / 수준) không nhằm biến PM thành accountant. Mục tiêu là hiểu economic trạng thái (state / 상태) đủ tốt để phân biệt “đã chi”, “đã cam kết sẽ chi”, “sắp cần cash”, “forecast sẽ vượt”, và “investment còn đáng tiếp tục hay không”. Những trạng thái này khác nhau nhưng thường bị trộn trên dashboard.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Estimate, ngân sách (budget / 예산) và funding** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) management bắt đầu từ quyết định (decision / 결정), không từ spreadsheet** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Estimate, commitment, accrual, actual và cash là năm trạng thái (state / 상태) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Estimate, ngân sách (budget / 예산) và funding

Chi phí (cost / 비용) estimate dự đoán chi phí công việc (work / 작업). chi phí (cost / 비용) baseline là time-phased authorized ngân sách (budget / 예산) dùng để đo hiệu năng (performance / 성능), thường không gồm management reserve. dự án (project / 프로젝트) ngân sách (budget / 예산) rộng hơn có thể gồm management reserve. Funding yêu cầu (requirement / 요구사항) còn quan tâm thời điểm dòng tiền cần được cấp.

Nếu PM chỉ biết “tổng ngân sách (budget / 예산) 1 tỷ” nhưng không biết khi nào đặc tả hợp đồng (contract / 계약) milestone phải thanh toán, dự án (project / 프로젝트) vẫn có liquidity/timing bài toán (problem / 문제).

Time-phasing quan trọng vì hai dự án (project / 프로젝트) cùng total chi phí (cost / 비용) có cash-flow profile khác nhau. Procurement deposit lớn ở đầu, construction payment theo milestone và cloud spend tăng dần theo quy mô (scale / 규모) cần funding chiến lược (strategy / 전략) khác nhau.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Estimate, commitment, accrual, actual và cash là năm trạng thái (state / 상태) khác nhau** tiếp nhận điểm tựa từ **Estimate, ngân sách (budget / 예산) và funding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Committed chi phí (cost / 비용) là early-warning tín hiệu (signal / 신호)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Estimate, commitment, accrual, actual và cash là năm trạng thái (state / 상태) khác nhau

Estimate là kỳ vọng future chi phí (cost / 비용). Commitment là obligation đã được tạo, ví dụ purchase thứ tự (order / 순서) hoặc signed đặc tả hợp đồng (contract / 계약), dù cash chưa trả. Accrual/expense recognition phản ánh chi phí (cost / 비용) đã phát sinh theo accounting quy tắc (rule / 규칙) dù invoice/cash có thể chưa đi qua. Actual chi phí (cost / 비용) trong project-control hệ thống (system / 시스템) cần ngữ nghĩa (semantic / 의미적) definition rõ. Cash luồng (flow / 흐름) nói tiền thực sự vào/ra khi nào.

Ví dụ vendor hoàn thành milestone cuối tháng 9 nhưng invoice trả tháng 10. Operationally dự án (project / 프로젝트) đã incur chi phí (cost / 비용) tháng 9; cash ra tháng 10. Nếu dashboard chỉ nhìn bank payment, September có thể trông under ngân sách (budget / 예산) giả.

Ngược lại dự án (project / 프로젝트) có thể trả deposit lớn trước delivery; cash đã ra nhưng earned progress chưa tương ứng. PM phải biết chỉ số (metric / 지표) mình đang nhìn thuộc economic trạng thái (state / 상태) nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Committed chi phí (cost / 비용) là early-warning tín hiệu (signal / 신호)** tiếp nhận điểm tựa từ **Estimate, commitment, accrual, actual và cash là năm trạng thái (state / 상태) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Direct, indirect, fixed và variable chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Committed chi phí (cost / 비용) là early-warning tín hiệu (signal / 신호)

Actual chi phí (cost / 비용) chỉ nhìn quá khứ. Committed chi phí (cost / 비용) cho thấy một phần future chi phí (cost / 비용) đã khó đảo ngược. Nếu dự án (project / 프로젝트) đã ký đặc tả hợp đồng (contract / 계약) 80% ngân sách (budget / 예산) dù mới chi 30%, “còn 70% ngân sách (budget / 예산) chưa dùng” là statement gây hiểu lầm.

Forecast tốt nên reconcile actual + committed + uncommitted estimate. Khi phạm vi (scope / 범위) thay đổi (change / 변경), cần biết phần nào còn flexible và phần nào đã khóa (lock / 잠금) bởi đặc tả hợp đồng (contract / 계약)/cancellation clause.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Direct, indirect, fixed và variable chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Committed chi phí (cost / 비용) là early-warning tín hiệu (signal / 신호)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Opportunity chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Direct, indirect, fixed và variable chi phí (cost / 비용)

Direct chi phí (cost / 비용) có thể gắn trực tiếp với dự án (project / 프로젝트) như vendor fee hoặc dự án (project / 프로젝트) labor. Indirect chi phí (cost / 비용) được chia sẻ như office, dùng chung (shared / 공유) nền tảng (platform / 플랫폼) hoặc corporate overhead. Fixed chi phí (cost / 비용) không đổi đáng kể theo volume trong phạm vi (range / 범위) nhất định; variable chi phí (cost / 비용) thay theo usage hoặc đầu ra (output / 출력).

Classification giúp estimate và nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) nhưng không nên học máy móc. Cloud subscription có phần fixed và variable; nội bộ (internal / 내부) employee chi phí (cost / 비용) có thể là sunk payroll ở organization nhưng vẫn có opportunity chi phí (cost / 비용) vì họ không làm việc khác.

Một chi phí (cost / 비용) cũng có thể behave khác theo quyết định (decision / 결정) horizon. Annual license đã trả có thể là sunk trong short-term continuation quyết định (decision / 결정) nhưng trở thành avoidable chi phí (cost / 비용) ở renewal quyết định (decision / 결정).

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Opportunity chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Direct, indirect, fixed và variable chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Avoidable, unavoidable và incremental chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Opportunity chi phí (cost / 비용)

Opportunity chi phí (cost / 비용) là giá trị (value / 값) của alternative tốt nhất bị bỏ khi chọn một option. Nếu một nhóm (team / 팀) cấp cao (senior / 시니어) làm dự án (project / 프로젝트) A, họ không thể đồng thời làm dự án (project / 프로젝트) B.

Dự án (project / 프로젝트) selection vì vậy không chỉ hỏi “A có positive ROI không?” mà còn “A có tốt hơn cách dùng tài nguyên (resource / 자원) khác không?”. Portfolio tầng (layer / 계층) quản lý sự đánh đổi (trade-off / 트레이드오프) này rõ hơn dự án (project / 프로젝트) tầng (layer / 계층), nhưng PM cần hiểu khi tài nguyên (resource / 자원) scarcity ảnh hưởng priority.

Opportunity chi phí (cost / 비용) thường vô hình trong accounting report nhưng rất thật trong portfolio. dùng chung (shared / 공유) architect 3 tháng dành cho low-value dự án (project / 프로젝트) có thể làm high-value initiative chậm dù payroll total không đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Avoidable, unavoidable và incremental chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Opportunity chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Contingency reserve và management reserve** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Avoidable, unavoidable và incremental chi phí (cost / 비용)

Khi đánh giá option, useful question là chi phí (cost / 비용) nào thực sự thay đổi nếu quyết định (decision / 결정) thay đổi. Một sunk or unavoidable corporate overhead không nên được dùng như incremental penalty nếu nó vẫn tồn tại ở mọi option.

Incremental chi phí (cost / 비용) là phần thêm do option/thay đổi (change / 변경) tạo ra. thay đổi (change / 변경) yêu cầu (request / 요청) “chỉ tốn 20 triệu vendor fee” có thể còn incremental kiểm thử (test / 테스트), huấn luyện (training / 학습), hỗ trợ (support / 지원) và schedule cost-of-delay. Impact phân tích (analysis / 분석) cần total incremental economics, không chỉ invoice trực tiếp.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Contingency reserve và management reserve** tiếp nhận điểm tựa từ **Avoidable, unavoidable và incremental chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reserve consumption phải nối với rủi ro (risk / 위험) retirement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contingency reserve và management reserve

Contingency reserve dùng cho known-unknowns: rủi ro (risk / 위험) đã được nhận diện nhưng kết quả (outcome / 결과) chưa chắc. Nó thường nằm trong chi phí (cost / 비용) baseline tùy quản trị (governance / 거버넌스). Management reserve dùng cho unknown-unknowns hoặc công việc (work / 작업) ngoài planning basis trong ranh giới (boundary / 경계) được quản trị, và thường do management điều khiển (control / 제어).

Sự phân biệt quan trọng vì reserve không phải “tiền dư”. Nó biểu diễn bất định (uncertainty / 불확실성) được chủ động price vào plan.

Reserve cần quy tắc (rule / 규칙) sử dụng. Nếu nhóm (team / 팀) coi contingency là ngân sách (budget / 예산) có thể spend tự do, bất định (uncertainty / 불확실성) buffer bị consume bởi optional phạm vi (scope / 범위). Nếu reserve quá khó truy cập (access / 접근), nó không giúp phản hồi (response / 응답) khi rủi ro (risk / 위험) materialize.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Reserve consumption phải nối với rủi ro (risk / 위험) retirement** tiếp nhận điểm tựa từ **Contingency reserve và management reserve** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) estimate cũng là phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reserve consumption phải nối với rủi ro (risk / 위험) retirement

Dùng reserve không tự động là bad hiệu năng (performance / 성능). Nếu identified rủi ro (risk / 위험) materialize và contingency được dùng đúng purpose, reserve đang làm công việc của nó.

Câu hỏi quản trị là exposure còn lại so với reserve còn lại. Nếu 70% reserve đã dùng nhưng 80% major bất định (uncertainty / 불확실성) đã retired, trạng thái (state / 상태) có thể hợp lý. Nếu 70% reserve đã dùng khi dự án (project / 프로젝트) mới đi qua 20% uncertain công việc (work / 작업), forecast cần attention.

Reserve phân tích (analysis / 분석) nên theo trend của rủi ro (risk / 위험) exposure, không chỉ balance tài khoản.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Chi phí (cost / 비용) estimate cũng là phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **Reserve consumption phải nối với rủi ro (risk / 위험) retirement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Estimate phạm vi (range / 범위) phải phản ánh nguồn (source / 소스) of bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) estimate cũng là phân phối (distribution / 분포)

Một điểm (point / 지점) estimate như 500 triệu che bất định (uncertainty / 불확실성). phạm vi (range / 범위) 450–650 triệu với các giả định (assumptions / 가정들) rõ cung cấp thông tin (information / 정보) tốt hơn.

Estimate confidence phụ thuộc maturity của phạm vi (scope / 범위), thị trường (market / 시장) price, exchange tỷ lệ (rate / 비율), technical bất định (uncertainty / 불확실성) và vendor quote. Progressive elaboration thường làm phạm vi (range / 범위) hẹp dần khi bằng chứng (evidence / 증거) tăng.

Management nên tránh ép estimate sớm thành fixed commitment mà không price rủi ro (risk / 위험), vì bất định (uncertainty / 불확실성) không biến mất chỉ vì đặc tả hợp đồng (contract / 계약) hoặc slide có một con số.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Chi phí (cost / 비용) estimate cũng là phân phối (distribution / 분포)** nêu điều cần giải thích; **Estimate phạm vi (range / 범위) phải phản ánh nguồn (source / 소스) of bất định (uncertainty / 불확실성)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Chi phí (cost / 비용) aggregation và baseline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Estimate phạm vi (range / 범위) phải phản ánh nguồn (source / 소스) of bất định (uncertainty / 불확실성)

Phạm vi (range / 범위) rộng không phải luôn do nhóm (team / 팀) estimate kém. Early concept dự án (project / 프로젝트) có thể legitimately có phạm vi (range / 범위) lớn vì phạm vi (scope / 범위) và thị trường (market / 시장) chưa ổn định. Ngược lại phạm vi (range / 범위) rất hẹp khi dữ liệu (data / 데이터) còn yếu có thể là false precision.

Estimate nên kèm basis: quantity, tỷ lệ (rate / 비율), vendor quote, historical tham chiếu (reference / 참조), inflation/FX giả định (assumption / 가정), productivity, exclusions và validity period. Một con số không có basis rất khó cập nhật (update / 업데이트) khi world thay đổi.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Estimate phạm vi (range / 범위) phải phản ánh nguồn (source / 소스) of bất định (uncertainty / 불확실성)** nêu điều cần giải thích; **Chi phí (cost / 비용) aggregation và baseline** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Funding-limit reconciliation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) aggregation và baseline

Work-package estimates được aggregate thành control-account/dự án (project / 프로젝트) ngân sách (budget / 예산). Nhưng aggregation không tự loại bất định (uncertainty / 불확실성). Correlated rủi ro (risk / 위험) có thể làm total variance lớn.

Baseline là tham chiếu (reference / 참조) được approve để đo hiệu năng (performance / 성능). Nếu phạm vi (scope / 범위) thay đổi (change / 변경) được approve, baseline có thể cần thay đổi (change / 변경) theo quản trị (governance / 거버넌스). Baseline không phải original estimate bất biến cũng không phải rolling forecast.

Aggregation cũng cần tránh double count. dùng chung (shared / 공유) môi trường (environment / 환경) chi phí (cost / 비용) được allocate ở hạ tầng (infrastructure / 인프라) gói (package / 패키지) rồi lại cộng vào từng workstream sẽ inflate ngân sách (budget / 예산); dùng chung (common / 공통) tài nguyên (resource / 자원) bị bỏ khỏi mọi gói (package / 패키지) lại làm underestimate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Chi phí (cost / 비용) aggregation và baseline** đã nêu tiêu chí phân biệt, còn **Funding-limit reconciliation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Payment terms và working-capital tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Funding-limit reconciliation

Một plan có thể economically hợp lý nhưng funding cadence không match. Organization có thể chỉ cấp tối đa 300 triệu/quý trong khi procurement cần deposit 500 triệu tháng đầu.

Funding-limit reconciliation điều chỉnh timing, đặc tả hợp đồng (contract / 계약) term, phasing hoặc financing plan để cash need phù hợp funding availability. Đây là liên kết (connection / 연결) giữa schedule và finance: dời procurement milestone có thể giải cash ràng buộc (constraint / 제약조건) nhưng làm đường găng (critical path / 임계 경로) trễ.

PM cần surface xung đột (conflict / 충돌) này sớm thay vì tới ngày invoice mới phát hiện “ngân sách (budget / 예산) có nhưng cash chưa được bản phát hành (release / 릴리스)”.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Funding-limit reconciliation** đã nêu tiêu chí phân biệt, còn **Payment terms và working-capital tác động (effect / 효과)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Inflation, escalation và FX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Payment terms và working-capital tác động (effect / 효과)

Hai vendor có cùng total price nhưng payment term khác nhau: 50% upfront so với payment after acceptance. Điều này thay cash exposure, leverage và rủi ro (risk / 위험).

Milestone payment có thể align incentive với verified progress. Upfront payment có thể cần khi equipment custom nhưng tăng buyer exposure nếu vendor thất bại (fail / 실패). Commercial quyết định (decision / 결정) vì vậy không chỉ so headline price.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Inflation, escalation và FX** tiếp nhận điểm tựa từ **Payment terms và working-capital tác động (effect / 효과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tax, duty và regulatory chi phí (cost / 비용) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inflation, escalation và FX

Long dự án (project / 프로젝트) chịu price escalation. Material, labor tỷ lệ (rate / 비율) hoặc cloud/vendor price có thể tăng theo thời gian. Multi-currency đặc tả hợp đồng (contract / 계약) còn có FX rủi ro (risk / 위험).

Một vendor quote 1 triệu USD không phải fixed chi phí (cost / 비용) bằng nội tệ nếu exchange tỷ lệ (rate / 비율) chưa hedge/fix. PM không cần trade FX, nhưng phải biết giả định (assumption / 가정) tỷ lệ (rate / 비율), exposure đơn vị sở hữu (owner / 오너) và trigger cập nhật (update / 업데이트) forecast.

Delay cũng có finance tác động (effect / 효과): cùng phạm vi (scope / 범위) nhưng mua một năm sau có thể đắt hơn vì inflation/escalation. Schedule variance vì vậy có thể biến thành chi phí (cost / 비용) variance ngay cả khi productivity không đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Inflation, escalation và FX** đã nêu tiêu chí phân biệt, còn **Tax, duty và regulatory chi phí (cost / 비용) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Earned giá trị (value / 값) Management như một mô hình (model / 모델) tích hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tax, duty và regulatory chi phí (cost / 비용) ranh giới (boundary / 경계)

Dự án (project / 프로젝트) estimate cần rõ giá đã gồm tax, import duty, license, insurance hay chưa. Một quote “100” từ vendor có thể không phải landed/dự án (project / 프로젝트) chi phí (cost / 비용) 100.

Điểm quan trọng không phải học luật thuế mà là xác định chi phí (cost / 비용) ranh giới (boundary / 경계). Missing non-work chi phí (cost / 비용) thường xuất hiện ở procurement-heavy dự án (project / 프로젝트) khi nhóm (team / 팀) chỉ estimate technical price.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Tax, duty và regulatory chi phí (cost / 비용) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **Earned giá trị (value / 값) Management như một mô hình (model / 모델) tích hợp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **EV không phải revenue hay nghiệp vụ (business / 비즈니스) giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Earned giá trị (value / 값) Management như một mô hình (model / 모델) tích hợp

Earned giá trị (value / 값) Management (EVM / 획득가치관리) kết nối phạm vi (scope / 범위), schedule và chi phí (cost / 비용) trong predictive điều khiển (control / 제어). Ba quantity cơ bản là Planned giá trị (value / 값) (PV), Earned giá trị (value / 값) (EV) và Actual chi phí (cost / 비용) (AC).

Nếu tới hôm nay ta dự kiến hoàn thành công việc (work / 작업) trị giá 100 (PV=100), thực tế hoàn thành lượng công việc (work / 작업) tương đương 80 theo baseline (EV=80), và đã chi 90 (AC=90), thì:

```text
Schedule Variance: SV = EV - PV = 80 - 100 = -20
Cost Variance:     CV = EV - AC = 80 - 90  = -10
Schedule Index:    SPI = EV / PV = 0.80
Cost Index:        CPI = EV / AC ≈ 0.89
```

Negative SV nói ta hoàn thành ít planned công việc (work / 작업) hơn mức dự kiến tại thời điểm đo. CPI dưới 1 nói mỗi đơn vị chi phí tạo ít earned giá trị (value / 값) hơn plan. Nhưng EVM không tự giải thích nguyên nhân gốc (root cause / 근본 원인) và không đo customer giá trị (value / 값); nó đo hiệu năng (performance / 성능) so với baseline.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **EV không phải revenue hay nghiệp vụ (business / 비즈니스) giá trị (value / 값)** tiếp nhận điểm tựa từ **Earned giá trị (value / 값) Management như một mô hình (model / 모델) tích hợp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **EV đo lường (measurement / 측정) technique quyết định tín hiệu (signal / 신호) chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## EV không phải revenue hay nghiệp vụ (business / 비즈니스) giá trị (value / 값)

Tên “earned giá trị (value / 값)” dễ gây hiểu nhầm. EV là budgeted giá trị (value / 값) của công việc (work / 작업) đã hoàn thành theo baseline, không phải revenue, profit hoặc customer benefit.

Một tính năng (feature / 기능) không ai dùng vẫn có EV nếu phạm vi (scope / 범위) đã hoàn thành. Vì vậy EVM mạnh về thực thi (execution / 실행) điều khiển (control / 제어) nhưng cần benefit chỉ số (metric / 지표) để đánh giá kết quả (outcome / 결과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **EV không phải revenue hay nghiệp vụ (business / 비즈니스) giá trị (value / 값)** nêu điều cần giải thích; **EV đo lường (measurement / 측정) technique quyết định tín hiệu (signal / 신호) chất lượng (quality / 품질)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **BAC, ETC, EAC và VAC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## EV đo lường (measurement / 측정) technique quyết định tín hiệu (signal / 신호) chất lượng (quality / 품질)

EV chỉ đáng tin khi quy tắc (rule / 규칙) đo completion phù hợp. 0/100, 50/50, weighted milestone hoặc percent complete tạo hành vi (behavior / 동작) khác nhau.

Nếu một công việc (work / 작업) gói (package / 패키지) trị giá lớn được cho 90% EV dựa trên subjective progress nhưng phần acceptance khó nhất chưa xong, CPI/SPI sẽ đẹp giả. Discrete deliverable nên ưu tiên mục tiêu (objective / 목표) completion bằng chứng (evidence / 증거) khi feasible.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **EV đo lường (measurement / 측정) technique quyết định tín hiệu (signal / 신호) chất lượng (quality / 품질)** nêu điều cần giải thích; **BAC, ETC, EAC và VAC** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Forecast với EAC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BAC, ETC, EAC và VAC

Ngân sách (budget / 예산) at Completion (BAC) là authorized baseline ngân sách (budget / 예산) cho phạm vi (scope / 범위). Estimate to Complete (ETC) là forecast chi phí (cost / 비용) còn lại. Estimate at Completion (EAC) là total forecast chi phí (cost / 비용). Variance at Completion (VAC) là difference giữa BAC và EAC.

Định danh (identity / 식별자) cơ bản:

```text
EAC = AC + ETC
VAC = BAC - EAC
```

Các formula khác nhau chủ yếu là cách estimate ETC dưới giả định (assumption / 가정) khác nhau.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Forecast với EAC** tiếp nhận điểm tựa từ **BAC, ETC, EAC và VAC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bottom-up ETC khi cấu trúc (structure / 구조) đã thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Forecast với EAC

Nếu hiện tại (current / 현재) chi phí (cost / 비용) efficiency dự kiến tiếp tục, có thể dùng:

```text
EAC = BAC / CPI
```

Nếu variance hiện tại được xem là one-off và phần còn lại theo plan, có thể dùng:

```text
EAC = AC + (BAC - EV)
```

Nếu cả chi phí (cost / 비용) và schedule efficiency được giả định ảnh hưởng phần còn lại, một mô hình (model / 모델) thường gặp dùng:

```text
EAC = AC + (BAC - EV) / (CPI × SPI)
```

Không nên học formula mà quên giả định (assumption / 가정). Chọn formula trước khi hiểu nguyên nhân variance là biến arithmetic thành ritual.

Worked examples chi tiết hơn nằm ở [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Bottom-up ETC khi cấu trúc (structure / 구조) đã thay đổi** tiếp nhận điểm tựa từ **Forecast với EAC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TCPI như câu hỏi về feasibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bottom-up ETC khi cấu trúc (structure / 구조) đã thay đổi

Formula extrapolation hữu ích khi future công việc (work / 작업) giống hiệu năng (performance / 성능) mẫu (pattern / 패턴) hiện tại. Nhưng nếu phạm vi (scope / 범위), vendor, nhóm (team / 팀) hoặc approach đã thay đổi, bottom-up ETC có thể tốt hơn.

Ví dụ CPI thấp do one-time failed di chuyển (migration / 마이그레이션) và remaining công việc (work / 작업) là routine rollout. `BAC/CPI` có thể quá pessimistic. Ngược lại nếu nguyên nhân gốc (root cause / 근본 원인) là structural productivity bài toán (problem / 문제), “remaining công việc (work / 작업) theo plan” quá optimistic.

Forecast chất lượng (quality / 품질) phụ thuộc nhân quả (causal / 인과적) mô hình (model / 모델) của remaining công việc (work / 작업).

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **TCPI như câu hỏi về feasibility** tiếp nhận điểm tựa từ **Bottom-up ETC khi cấu trúc (structure / 구조) đã thay đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SPI và SV có giới hạn gần cuối dự án (project / 프로젝트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TCPI như câu hỏi về feasibility

To-Complete hiệu năng (performance / 성능) chỉ mục (index / 인덱스) (TCPI) hỏi efficiency cần đạt trên công việc (work / 작업) còn lại để chạm một mục tiêu (target / 대상) ngân sách (budget / 예산).

Nếu hiệu năng (performance / 성능) lịch sử CPI khoảng 0.8 nhưng TCPI cần 1.25 để đạt BAC, mục tiêu (target / 대상) có thể không realistic nếu không có major thay đổi (change / 변경). TCPI giúp chuyển conversation từ “hãy cố lên” sang “required improvement có feasible không?”.

TCPI cao không phải mệnh lệnh làm việc nhanh hơn. Nó là tín hiệu (signal / 신호) để reassess mục tiêu (target / 대상), phạm vi (scope / 범위), tiến trình (process / 프로세스) hoặc forecast.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **TCPI như câu hỏi về feasibility** đã nêu tiêu chí phân biệt, còn **SPI và SV có giới hạn gần cuối dự án (project / 프로젝트)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **EVM thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SPI và SV có giới hạn gần cuối dự án (project / 프로젝트)

Khi dự án (project / 프로젝트) gần completion, EV và PV đều tiến về BAC nên SPI có xu hướng quay về 1 và SV về 0, kể cả dự án (project / 프로젝트) đã finish muộn. Đây là giới hạn của schedule interpretation bằng EVM monetary dimension.

Vì vậy actual/forecast finish date, milestone lô-gic (logic / 논리) và đường găng (critical path / 임계 경로) vẫn cần được quản lý bằng schedule mô hình (model / 모델). EVM không thay mạng (network / 네트워크) scheduling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **SPI và SV có giới hạn gần cuối dự án (project / 프로젝트)** đã nêu tiêu chí phân biệt, còn **EVM thất bại (failure / 실패) modes** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Variance attribution: price, quantity, productivity, mix và timing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## EVM thất bại (failure / 실패) modes

EVM chỉ tốt khi phạm vi (scope / 범위)/baseline và completion đo lường (measurement / 측정) đáng tin. Nếu nhóm (team / 팀) declare công việc (work / 작업) 90% complete quá dễ, EV bị inflated. Nếu baseline đã outdated nhưng không rebaseline sau approved major thay đổi (change / 변경), variance mất meaning.

EVM cũng ít phù hợp khi phạm vi (scope / 범위) adaptive liên tục và giá trị (value / 값) không map ổn định vào baseline công việc (work / 작업) gói (package / 패키지). Có thể vẫn dùng financial điều khiển (control / 제어) khác mà không ép khung phần mềm (framework / 프레임워크) không phù hợp.

Một thất bại (failure / 실패) khác là “variance hunting”: management hỏi vì sao CPI 0.97 thay vì tập trung material driver. Threshold nên phản ánh quyết định (decision / 결정) significance, không biến mọi decimal thành sự cố (incident / 인시던트).

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Variance attribution: price, quantity, productivity, mix và timing** tiếp nhận điểm tựa từ **EVM thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fixed ngân sách (budget / 예산) không có nghĩa fixed phạm vi (scope / 범위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variance attribution: price, quantity, productivity, mix và timing

Chi phí (cost / 비용) variance tổng không đủ để hành động (action / 동작). Cần biết driver. Vendor tỷ lệ (rate / 비율) tăng là price tác động (effect / 효과); rework tăng hours là quantity/productivity tác động (effect / 효과); cấp cao (senior / 시니어)/junior ratio khác plan là mix tác động (effect / 효과); invoice timing lệch là timing tác động (effect / 효과).

Hai dự án (project / 프로젝트) đều over 10% nhưng phản hồi (response / 응답) khác nhau. Price escalation cần commercial/forecast hành động (action / 동작); productivity issue cần tiến trình (process / 프로세스)/technical hành động (action / 동작); timing tác động (effect / 효과) có thể không thay EAC.

Variance phân tích (analysis / 분석) tốt phân biệt symptom tài chính với nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Fixed ngân sách (budget / 예산) không có nghĩa fixed phạm vi (scope / 범위)** tiếp nhận điểm tựa từ **Variance attribution: price, quantity, productivity, mix và timing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Burn tỷ lệ (rate / 비율) và runway** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fixed ngân sách (budget / 예산) không có nghĩa fixed phạm vi (scope / 범위)

Nhiều dự án (project / 프로젝트) có ngân sách (budget / 예산) cap nhưng phạm vi (scope / 범위) có thể prioritize. Adaptive sản phẩm (product / 제품) delivery thường giữ nhóm (team / 팀)/chi phí (cost / 비용) tương đối stable và optimize phạm vi (scope / 범위) theo giá trị (value / 값).

Ngược lại fixed phạm vi (scope / 범위) + fixed ngân sách (budget / 예산) + fixed date trong high bất định (uncertainty / 불확실성) môi trường (environment / 환경) thường đẩy rủi ro (risk / 위험) sang chất lượng (quality / 품질), hidden overtime hoặc đặc tả hợp đồng (contract / 계약) dispute. Triple ràng buộc (constraint / 제약조건) không thể bị “ra lệnh” để bất định (uncertainty / 불확실성) biến mất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Burn tỷ lệ (rate / 비율) và runway** tiếp nhận điểm tựa từ **Fixed ngân sách (budget / 예산) không có nghĩa fixed phạm vi (scope / 범위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sunk chi phí (cost / 비용) và continuation quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Burn tỷ lệ (rate / 비율) và runway

Burn tỷ lệ (rate / 비율) là tốc độ tiêu cash/ngân sách (budget / 예산) trong period. Runway ước lượng thời gian còn lại nếu burn hiện tại tiếp tục.

Startup/sản phẩm (product / 제품) ngữ cảnh (context / 맥락) dùng khái niệm này rõ, nhưng dự án (project / 프로젝트) cũng có thể dùng để phát hiện funding timing rủi ro (risk / 위험). Burn tỷ lệ (rate / 비율) cao không nhất thiết xấu nếu dự án (project / 프로젝트) đang ở phase procurement lớn; cần so với plan và đầu ra (output / 출력).

Runway dựa trên burn hiện tại chỉ meaningful nếu chi phí (cost / 비용) profile tương đối stable. Construction/procurement dự án (project / 프로젝트) có lumpy payment nên tuyến tính (linear / 선형) extrapolation dễ sai.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Sunk chi phí (cost / 비용) và continuation quyết định (decision / 결정)** tiếp nhận điểm tựa từ **Burn tỷ lệ (rate / 비율) và runway** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cancellation chi phí (cost / 비용) và switching chi phí (cost / 비용) vẫn là future chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sunk chi phí (cost / 비용) và continuation quyết định (decision / 결정)

Sunk chi phí (cost / 비용) là chi phí đã xảy ra và không thể thu hồi. Quyết định tiếp tục dự án (project / 프로젝트) nên dựa trên future chi phí (cost / 비용), future benefit, rủi ro (risk / 위험) và alternatives, không dựa trên “đã đầu tư quá nhiều để dừng”.

Ví dụ đã chi 70% ngân sách (budget / 예산) nhưng bằng chứng (evidence / 증거) mới cho thấy sản phẩm (product / 제품) không có thị trường (market / 시장) fit. Nếu remaining 30% không tạo expected giá trị (value / 값), tiếp tục chỉ để “không phí 70%” làm tổn thất lớn hơn.

Quản trị (governance / 거버넌스) cần exit criteria đủ rõ để sunk-cost psychology không khóa organization vào dự án (project / 프로젝트) mất giá trị (value / 값).

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Cancellation chi phí (cost / 비용) và switching chi phí (cost / 비용) vẫn là future chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Sunk chi phí (cost / 비용) và continuation quyết định (decision / 결정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Marginal phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cancellation chi phí (cost / 비용) và switching chi phí (cost / 비용) vẫn là future chi phí (cost / 비용)

Tránh sunk-cost fallacy không có nghĩa dừng là miễn phí. Termination fee, dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션), decommission, employee chuyển tiếp (transition / 전이) hoặc regulatory obligation là future chi phí (cost / 비용) và phải được tính vào stop option.

Quyết định (decision / 결정) đúng so future states: continue, pause, pivot, phase hoặc terminate. “Đã chi bao nhiêu” không quyết định; “mỗi option từ hôm nay tạo chi phí (cost / 비용)/giá trị (value / 값)/rủi ro (risk / 위험) gì” mới quyết định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Marginal phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **Cancellation chi phí (cost / 비용) và switching chi phí (cost / 비용) vẫn là future chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ROI, payback và NPV** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Marginal phân tích (analysis / 분석)

Khi dự án (project / 프로젝트) gần hoàn thành, câu hỏi có thể là thêm 10% chi phí (cost / 비용) có tạo enough incremental benefit/rủi ro (risk / 위험) reduction không. Đây là marginal lập luận (reasoning / 추론).

Không nên dùng average ROI của toàn dự án (project / 프로젝트) để quyết một optional enhancement cuối kỳ. Hãy so incremental chi phí (cost / 비용) với incremental giá trị (value / 값) và tác động (effect / 효과) lên deadline/rủi ro (risk / 위험).

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **ROI, payback và NPV** tiếp nhận điểm tựa từ **Marginal phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Benefit-cost ratio và break-even intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ROI, payback và NPV

Return on Investment (ROI) so return với investment theo definition tổ chức. Payback period hỏi mất bao lâu để recover investment. Net Present giá trị (value / 값) (NPV) discount future cash luồng (flow / 흐름) về present giá trị (value / 값).

Mỗi chỉ số (metric / 지표) trả lời câu khác. Payback ưu tiên liquidity/tốc độ thu hồi nhưng bỏ qua nhiều benefit sau payback. ROI có thể che timing. NPV phản ánh thời gian (time / 시간) giá trị (value / 값) of money nhưng phụ thuộc discount tỷ lệ (rate / 비율) và cash-flow các giả định (assumptions / 가정들).

Dự án (project / 프로젝트) selection không nên dùng một chỉ số (metric / 지표) như truth tuyệt đối.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Benefit-cost ratio và break-even intuition** tiếp nhận điểm tựa từ **ROI, payback và NPV** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NPV và thời gian (time / 시간) giá trị (value / 값) intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Benefit-cost ratio và break-even intuition

Benefit-cost ratio so present/expected benefit với chi phí (cost / 비용) theo convention tổ chức. Break-even hỏi khi nào cumulative benefit bù cumulative chi phí (cost / 비용) hoặc mức volume nào làm economics đổi dấu.

Hai chỉ số (metric / 지표) này hữu ích để reason nhưng vẫn phụ thuộc các giả định (assumptions / 가정들). A dự án (project / 프로젝트) có BCR tốt ở adoption 80% có thể không viable ở adoption 30%.

Sensitivity phân tích (analysis / 분석) nên tìm driver làm quyết định (decision / 결정) đổi, không chỉ produce one base-case number.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **NPV và thời gian (time / 시간) giá trị (value / 값) intuition** tiếp nhận điểm tựa từ **Benefit-cost ratio và break-even intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Financial benefit và non-financial benefit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NPV và thời gian (time / 시간) giá trị (value / 값) intuition

Tiền nhận hôm nay thường có giá trị hơn cùng số tiền nhận sau nhiều năm vì opportunity chi phí (cost / 비용) và rủi ro (risk / 위험). NPV có dạng khái quát:

```text
NPV = Σ CF_t / (1 + r)^t - Initial Investment
```

Trong đó `r` là discount tỷ lệ (rate / 비율) và `CF_t` là cash luồng (flow / 흐름) theo period.

Thư viện này không biến PMP thành môn corporate finance; mô hình tư duy (mental model / 사고 모델) cần nhớ là investment quyết định (decision / 결정) phải so benefit theo thời gian (time / 시간)/rủi ro (risk / 위험), không chỉ tổng nominal money.

Delay có thể giảm NPV ngay cả khi total nominal benefit không đổi vì cash inflow đến muộn hơn và chi phí (cost / 비용) kéo dài.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Financial benefit và non-financial benefit** tiếp nhận điểm tựa từ **NPV và thời gian (time / 시간) giá trị (value / 값) intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) of delay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Financial benefit và non-financial benefit

Compliance, an toàn (safety / 안전), năng lực (capability / 역량), reputation hoặc strategic option có thể có benefit khó quy tiền chính xác. Không nên ép mọi giá trị (value / 값) thành dollar nếu mô hình (model / 모델) quá giả tạo.

Nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) có thể kết hợp financial chỉ số (metric / 지표) với mandatory ràng buộc (constraint / 제약조건) và strategic rationale. “NPV thấp” không tự động loại dự án (project / 프로젝트) pháp lý bắt buộc; quyết định (decision / 결정) ngữ cảnh (context / 맥락) khác nhau.

Non-financial benefit vẫn cần bằng chứng (evidence / 증거). “Tăng uy tín” quá mơ hồ; có thể dùng proxy như kiểm tra (audit / 감사) finding giảm, dịch vụ (service / 서비스) availability, employee adoption hoặc rủi ro (risk / 위험) exposure reduction.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Chi phí (cost / 비용) of delay** tiếp nhận điểm tựa từ **Financial benefit và non-financial benefit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) of chất lượng (quality / 품질) nối chất lượng (quality / 품질) với finance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) of delay

Chi phí (cost / 비용) of delay cố lượng hóa giá trị (value / 값) mất khi delivery trễ. Một tính năng (feature / 기능) seasonal hoặc regulatory deadline có chi phí (cost / 비용) of delay cao; enhancement nội bộ có thể thấp hơn.

Chi phí (cost / 비용) of delay giúp priority khi nhiều item cạnh tranh tài nguyên (resource / 자원). Nó cũng cho thấy schedule và finance nối nhau: delay là economic tác động (effect / 효과) chứ không chỉ màu đỏ trên Gantt.

Chi phí (cost / 비용) of delay có thể nonlinear. Miss Black Friday một ngày có thể mất phần lớn seasonal giá trị (value / 값); delay một ngày ở nội bộ (internal / 내부) refactor có thể gần zero. Vì vậy “chi phí (cost / 비용) per day” constant chỉ là approximation trong một số ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Chi phí (cost / 비용) of chất lượng (quality / 품질) nối chất lượng (quality / 품질) với finance** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) of delay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giá trị (value / 값) đo lường (measurement / 측정) vượt ra ngoài ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) of chất lượng (quality / 품질) nối chất lượng (quality / 품질) với finance

Prevention/appraisal chi phí (cost / 비용) tăng có thể giảm nội bộ (internal / 내부)/bên ngoài (external / 외부) thất bại (failure / 실패) chi phí (cost / 비용). Cắt testing để “tiết kiệm ngân sách (budget / 예산)” có thể làm total vòng đời (lifecycle / 생명주기) chi phí (cost / 비용) tăng nếu defect escape môi trường vận hành (production / 운영 환경).

Financial lập luận (reasoning / 추론) tốt nhìn total chi phí (cost / 비용) of kết quả (outcome / 결과), không chỉ dự án (project / 프로젝트) spend ngắn hạn. Tuy vậy vòng đời (lifecycle / 생명주기) chi phí (cost / 비용) thuộc ranh giới (boundary / 경계) rộng hơn dự án (project / 프로젝트) baseline và cần tường minh (explicit / 명시적) business-case giả định (assumption / 가정).

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Chi phí (cost / 비용) of chất lượng (quality / 품질) nối chất lượng (quality / 품질) với finance** nêu điều cần giải thích; **Giá trị (value / 값) đo lường (measurement / 측정) vượt ra ngoài ngân sách (budget / 예산)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Benefit attribution và counterfactual** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giá trị (value / 값) đo lường (measurement / 측정) vượt ra ngoài ngân sách (budget / 예산)

Dự án có thể under ngân sách (budget / 예산) nhưng không tạo nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과). Vì vậy chỉ số (metric / 지표) nên nối tới benefit: adoption, revenue uplift, rủi ro (risk / 위험) reduction, thời gian (time / 시간) saved, compliance achieved, customer kết quả (outcome / 결과). Một benefit đơn vị sở hữu (owner / 오너) có thể tiếp tục theo dõi sau dự án (project / 프로젝트) closure khi benefit realization xảy ra muộn.

Giá trị (value / 값) nên được nhìn theo numerator lẫn denominator. Tăng revenue 5% nhưng tăng hỗ trợ (support / 지원) chi phí (cost / 비용) 20% có thể không tạo net benefit mong muốn.

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Giá trị (value / 값) đo lường (measurement / 측정) vượt ra ngoài ngân sách (budget / 예산)** nêu điều cần giải thích; **Benefit attribution và counterfactual** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Living nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) và continuation threshold** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Benefit attribution và counterfactual

Nếu revenue tăng sau go-live, không tự động chứng minh dự án (project / 프로젝트) tạo toàn bộ increase. thị trường (market / 시장) growth, promotion hoặc seasonality có thể cùng tác động.

Benefit plan nên có baseline và, khi khả thi, counterfactual/comparison. dự án (project / 프로젝트) management không cần causal-inference textbook, nhưng cần tránh claim benefit chỉ vì chỉ số (metric / 지표) thay cùng thời điểm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Benefit attribution và counterfactual** cho ta quy tắc; **Living nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) và continuation threshold** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Forecast phải được cập nhật (update / 업데이트) khi giả định (assumption / 가정) đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Living nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) và continuation threshold

Nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) là hypothesis về future giá trị (value / 값) dựa trên các giả định (assumptions / 가정들). Khi chi phí (cost / 비용), timing, adoption, regulation hoặc strategic priority đổi đủ lớn, hypothesis cần được cập nhật.

Quản trị (governance / 거버넌스) nên có threshold để reassess: forecast chi phí (cost / 비용) vượt X, benefit giảm Y, deadline miss làm giá trị (value / 값) cửa sổ (window / 윈도우) mất, hoặc mandatory rủi ro (risk / 위험) xuất hiện. Không cần reopen nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) vì every small variance, nhưng cũng không nên chờ closure mới phát hiện investment đã mất lô-gic (logic / 논리).

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Living nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) và continuation threshold** cho ta quy tắc; **Forecast phải được cập nhật (update / 업데이트) khi giả định (assumption / 가정) đổi** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Ví dụ lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Forecast phải được cập nhật (update / 업데이트) khi giả định (assumption / 가정) đổi

Financial forecast không nên chỉ cập nhật (update / 업데이트) vì actual chi phí (cost / 비용). FX, vendor price, schedule delay, demand, adoption hoặc regulation có thể đổi expected giá trị (value / 값) và future chi phí (cost / 비용).

Nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) sống cần phản ánh thông tin (information / 정보) mới đủ material. Nếu expected benefit giảm mạnh, PM cần surface tới quản trị (governance / 거버넌스) thay vì chỉ cố “giữ ngân sách (budget / 예산)”.

Forecast thay đổi (change / 변경) nên preserve lịch sử (history / 이력). Original forecast, revised forecast và reason giúp organization học calibration; overwrite số cũ làm mất bằng chứng (evidence / 증거).

> **Chuyển mạch:** Ở chặng này của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Forecast phải được cập nhật (update / 업데이트) khi giả định (assumption / 가정) đổi** cho ta quy tắc; **Ví dụ lập luận (reasoning / 추론)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ lập luận (reasoning / 추론)

Dự án (project / 프로젝트) có BAC 1 tỷ, CPI 0.8 sau 40% công việc (work / 작업). Nếu inefficiency có systemic cause chưa sửa, dùng `BAC/CPI` tạo forecast khoảng 1.25 tỷ hợp lý hơn giả định phần còn lại tự quay về plan. Nếu nguyên nhân gốc (root cause / 근본 원인) là one-time di chuyển (migration / 마이그레이션) sự cố (incident / 인시던트) đã giải quyết, formula one-off có thể phù hợp hơn.

Một dự án (project / 프로젝트) khác có NPV dương nhưng deadline thị trường (market / 시장) bị delay một năm, khiến benefit tới muộn và competitor chiếm share. nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) cần recompute thay vì giữ quyết định dựa trên NPV cũ.

Một vendor đặc tả hợp đồng (contract / 계약) 600 triệu đã signed nhưng dự án (project / 프로젝트) mới thanh toán 150 triệu. Dashboard “actual spend 150/1000” có thể khiến management nghĩ 850 triệu còn flexible; thực tế committed spend đã 600 và cancellation fee có thể làm phần lớn obligation khó tránh. quyết định (decision / 결정) cần nhìn commitment, không chỉ cash paid.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Ví dụ lập luận (reasoning / 추론)** cho ta quy tắc; **Thất bại (failure / 실패) modes** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) modes

Ngân sách (budget / 예산) tunnel vision xảy ra khi dự án (project / 프로젝트) tối ưu under-budget nhưng mất kết quả (outcome / 결과). Cash/expense confusion xảy ra khi payment timing bị đọc như hiệu năng (performance / 성능). Commitment blindness bỏ qua obligation chưa invoiced. Reserve raiding dùng contingency cho optional phạm vi (scope / 범위). EVM theater xuất hiện khi EV quy tắc (rule / 규칙) chủ quan làm chỉ số (metric / 지표) đẹp. Sunk-cost lock-in giữ dự án (project / 프로젝트) chỉ vì đã chi nhiều. Forecast overwrite xóa lịch sử calibration. FX/inflation blindness giả định nominal quote bất biến qua thời gian.

Financial maturity là khả năng nối accounting trạng thái (state / 상태), project-control trạng thái (state / 상태) và giá trị (value / 값) hypothesis thành một quyết định (decision / 결정) mô hình (model / 모델) nhất quán.

> **Chuyển mạch:** Trong **06 — Finance, chi phí (cost / 비용), reserves và giá trị (value / 값) đo lường (measurement / 측정)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> chi phí (cost / 비용) điều khiển (control / 제어) hỏi tài nguyên (resource / 자원) đã được cam kết, tiêu và forecast như thế nào; funding hỏi cash cần khi nào; giá trị (value / 값) management hỏi từ hôm nay investment còn đáng tiếp tục hay không. Reserve làm bất định (uncertainty / 불확실성) visible, còn mọi forecast chỉ có ý nghĩa khi basis, commitment và giả định (assumption / 가정) phía sau được nói rõ.

Tiếp theo: [Quality, resources và procurement](./07_quality_resources_and_procurement.md).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
