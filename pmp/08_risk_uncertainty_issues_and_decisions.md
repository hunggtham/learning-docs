# 08 — rủi ro (risk / 위험), bất định (uncertainty / 불확실성), issue và quyết định (decision / 결정) making

> **Mạch đọc:** Đặt **08 — rủi ro (risk / 위험), bất định (uncertainty / 불확실성), issue và quyết định (decision / 결정) making** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **rủi ro (risk / 위험) là bất định (uncertainty / 불확실성) có tác động (effect / 효과) lên mục tiêu (objective / 목표)** sang **bất định (uncertainty / 불확실성) không chỉ là sự kiện (event / 이벤트) rủi ro (risk / 위험)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## Rủi ro (risk / 위험) là bất định (uncertainty / 불확실성) có tác động (effect / 효과) lên mục tiêu (objective / 목표)

Rủi ro (risk / 위험) là một sự kiện hoặc điều kiện chưa chắc chắn có thể ảnh hưởng tích cực hoặc tiêu cực tới mục tiêu (objective / 목표). Issue (vấn đề đang xảy ra / 이슈) là điều kiện (condition / 조건) đã xảy ra hoặc đang tồn tại và cần xử lý. Nhầm rủi ro (risk / 위험) với issue làm phản hồi (response / 응답) sai timing: rủi ro (risk / 위험) cần preparation; issue cần hành động (action / 동작).

“Vendor có thể giao trễ” là rủi ro (risk / 위험). “Vendor vừa xác nhận trễ hai tuần” là issue. Khi trigger xuất hiện, item chuyển từ monitoring/phản hồi (response / 응답) readiness sang thực thi (execution / 실행)/escalation.

Rủi ro (risk / 위험) không tồn tại độc lập với mục tiêu (objective / 목표). Cùng một sự kiện (event / 이벤트) có thể là threat với một mục tiêu (objective / 목표) nhưng gần như irrelevant với mục tiêu (objective / 목표) khác. Vì vậy rủi ro (risk / 위험) statement nên luôn gắn với impact thực tế lên giá trị (value / 값), phạm vi (scope / 범위), schedule, chi phí (cost / 비용), chất lượng (quality / 품질), compliance hoặc reputation.

## Bất định (uncertainty / 불확실성) không chỉ là sự kiện (event / 이벤트) rủi ro (risk / 위험)

Không phải mọi bất định (uncertainty / 불확실성) đều dễ viết thành một sự kiện (event / 이벤트). Ambiguity xuất hiện khi ta chưa hiểu bài toán (problem / 문제) hoặc yêu cầu (requirement / 요구사항). Variability xuất hiện khi duration, demand hoặc defect tỷ lệ (rate / 비율) dao động tự nhiên. độ phức tạp (complexity / 복잡도) xuất hiện khi nhiều phụ thuộc (dependency / 의존성) tương tác khiến hành vi (behavior / 동작) khó dự đoán. Unknown unknown là vùng mà nhóm (team / 팀) chưa biết mình thiếu kiến thức (knowledge / 지식) gì.

Sự kiện (event / 이벤트) rủi ro (risk / 위험) có thể đưa vào register. Variability thường cần phạm vi (range / 범위), reserve hoặc probabilistic mô hình (model / 모델). Ambiguity cần discovery, prototype hoặc expert đầu vào (input / 입력). độ phức tạp (complexity / 복잡도) cần decomposition, giao diện (interface / 인터페이스) management và phản hồi (feedback / 피드백) nhanh. Unknown unknown cần resilience, contingency sức chứa (capacity / 용량) và khả năng phát hiện anomaly sớm.

Gọi tất cả là “rủi ro (risk / 위험)” nhưng dùng cùng một phản hồi (response / 응답) làm mất chất lượng lập luận (reasoning / 추론).

Một cách phân biệt sâu hơn là epistemic bất định (uncertainty / 불확실성) — bất định (uncertainty / 불확실성) vì thiếu kiến thức (knowledge / 지식) và có thể giảm bằng học tập (learning / 학습) — với aleatory variability — variation vốn có không biến mất chỉ vì nghiên cứu thêm. Prototype có thể giảm epistemic bất định (uncertainty / 불확실성) về API tính tương thích (compatibility / 호환성); nó không loại bỏ natural variability của giao dịch (transaction / 트랜잭션) volume. Hai loại bất định (uncertainty / 불확실성) cần intervention khác nhau.

## Rủi ro (risk / 위험) management là làm bất định (uncertainty / 불확실성) có thể hành động

Rủi ro (risk / 위험) identification tốt không phải tạo một danh sách dài “có thể xảy ra”. Mỗi rủi ro (risk / 위험) nên đủ nhân quả (causal / 인과적) để hành động (action / 동작): cause → uncertain sự kiện (event / 이벤트) → tác động (effect / 효과). Ví dụ “do API regulator chưa ổn định, giao diện (interface / 인터페이스) có thể thay trong UAT, dẫn tới rework và delay go-live”. Cấu trúc này gợi phản hồi (response / 응답) tốt hơn từ “tích hợp (integration / 통합) rủi ro (risk / 위험)”.

Rủi ro (risk / 위험) register là working mô hình (model / 모델) gồm đơn vị sở hữu (owner / 오너), xác suất (probability / 확률)/impact, phản hồi (response / 응답), trigger và status. Nó mất giá trị nếu chỉ được cập nhật trước quản trị (governance / 거버넌스) meeting.

Rủi ro (risk / 위험) đơn vị sở hữu (owner / 오너) là người chịu trách nhiệm theo dõi và bảo đảm rủi ro (risk / 위험) được quản lý; hành động (action / 동작) đơn vị sở hữu (owner / 오너) có thể là người thực hiện một phản hồi (response / 응답) cụ thể. Hai vai trò có thể là một hoặc khác nhau. Nếu register chỉ có “đơn vị sở hữu (owner / 오너)” nhưng không ai hiểu trách nhiệm là gì, item dễ bị treo.

## Rủi ro (risk / 위험) mô hình (model / 모델) chất lượng (quality / 품질) quan trọng hơn số lượng rủi ro (risk / 위험)

Một rủi ro (risk / 위험) register 200 dòng có thể kém hơn 30 rủi ro (risk / 위험) có nhân quả (causal / 인과적) lô-gic (logic / 논리) rõ. Chất lượng mô hình (model / 모델) phụ thuộc vào ranh giới (boundary / 경계), phụ thuộc (dependency / 의존성), các giả định (assumptions / 가정들) và ability to cập nhật (update / 업데이트) khi bằng chứng (evidence / 증거) đổi.

Duplicate rủi ro (risk / 위험) làm exposure bị double-count. rủi ro (risk / 위험) quá broad làm đơn vị sở hữu (owner / 오너) không biết phản hồi (response / 응답). rủi ro (risk / 위험) quá granular tạo noise. Một rủi ro (risk / 위험) tốt phải đủ cụ thể để có điều khiển (control / 제어) nhưng đủ rộng để giữ nhân quả (causal / 인과적) consequence quan trọng.

Register cũng phải phân biệt nguồn (source / 소스) rủi ro (risk / 위험) và symptom rủi ro (risk / 위험). “UAT có thể trễ” có thể chỉ là consequence của môi trường (environment / 환경) instability, vendor phản hồi (response / 응답) độ trễ (latency / 지연 시간) và yêu cầu (requirement / 요구사항) churn. Nếu chỉ mitigate symptom bằng overtime, underlying exposure còn nguyên.

## Rủi ro (risk / 위험) identification cần nhìn theo nhiều lớp

Một workshop chỉ hỏi “có rủi ro (risk / 위험) gì?” thường tạo danh sách (list / 목록) nông. Có thể scan theo nguồn: technical, people, vendor, schedule, financial, compliance, bảo mật (security / 보안), thị trường (market / 시장), organization, bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) và chuyển tiếp (transition / 전이). Có thể scan theo vòng đời (lifecycle / 생명주기): discovery, bản dựng (build / 빌드), tích hợp (integration / 통합), kiểm thử (test / 테스트), bản phát hành (release / 릴리스), adoption và operations handover.

Pre-mortem cũng hữu ích: giả sử sáu tháng sau dự án (project / 프로젝트) thất bại, điều gì có thể đã xảy ra? Cách này giúp nhóm (team / 팀) nói ra concern khó nêu khi mọi người đang quá committed với plan.

Near miss và weak tín hiệu (signal / 신호) cũng là nguồn identification. Một môi trường (environment / 환경) outage chỉ kéo dài 10 phút và chưa ảnh hưởng milestone có thể là tín hiệu (signal / 신호) của systemic độ tin cậy (reliability / 신뢰성) rủi ro (risk / 위험). Nếu organization chỉ học từ mất mát (loss / 손실) thật, học tập (learning / 학습) chi phí (cost / 비용) sẽ cao hơn cần thiết.

## Rủi ro (risk / 위험) dimensions ngoài xác suất (probability / 확률) × impact

Xác suất (probability / 확률) và impact là hai dimension phổ biến nhưng không phải toàn bộ. rủi ro (risk / 위험) velocity nói tác động (effect / 효과) xảy ra nhanh tới mức nào sau trigger. Proximity nói rủi ro (risk / 위험) có thể materialize gần hay xa. Detectability nói nhóm (team / 팀) có khả năng thấy tín hiệu (signal / 신호) sớm hay không. Controllability nói nhóm (team / 팀) có influence thực sự lên cause/impact không.

Một rủi ro (risk / 위험) xác suất (probability / 확률) trung bình nhưng velocity cực nhanh và detectability thấp có thể cần stronger prevention hơn rủi ro (risk / 위험) xác suất (probability / 확률) cao nhưng consequence phát triển chậm và dễ contain.

Không nhất thiết phải biến mọi dimension thành score. Mục tiêu là tránh flatten mọi rủi ro (risk / 위험) thành một ô màu.

## Qualitative và quantitative phân tích (analysis / 분석)

Qualitative phân tích (analysis / 분석) dùng relative scales để prioritize. Probability-impact ma trận (matrix / 행렬) hữu ích để tập trung attention nhưng dễ tạo false precision nếu quy mô (scale / 규모) không calibrated.

Expected Monetary giá trị (value / 값) (EMV) cho quyết định (decision / 결정) đơn giản:

```text
EMV = Probability × Impact
```

Nếu 20% khả năng outage gây tổn thất 100 triệu, EMV kỳ vọng là 20 triệu. Nhưng two risks cùng EMV có tail profile rất khác; catastrophic low-probability rủi ro (risk / 위험) có thể cần phản hồi (response / 응답) mạnh hơn rủi ro (risk / 위험) nhỏ lặp lại.

Cây quyết định (decision tree / 의사결정 트리) giúp so option có branch xác suất (probability / 확률)/chi phí (cost / 비용). Monte Carlo simulation có thể mô hình phân phối (distribution / 분포) của schedule/chi phí (cost / 비용) khi nhiều bất định (uncertainty / 불확실성) kết hợp. công cụ (tool / 도구) không thay rủi ro (risk / 위험) judgment; nó làm giả định (assumption / 가정) tường minh (explicit / 명시적) và aggregation tốt hơn.

Correlation là điểm dễ bị bỏ qua. Nếu ba rủi ro (risk / 위험) đều cùng phụ thuộc một vendor hoặc cùng xảy ra khi thị trường (market / 시장) biến động, cộng EMV như các sự kiện (event / 이벤트) độc lập có thể đánh giá thấp tail rủi ro (risk / 위험).

## Risk-adjusted giá trị (value / 값) thay vì expected giá trị (value / 값) đơn thuần

Hai option có cùng expected giá trị (value / 값) nhưng phân phối (distribution / 분포) khác nhau có thể không tương đương với organization. Option A có upside vừa phải và downside bounded; option B có upside lớn nhưng tail có thể gây compliance breach hoặc mất khả năng thanh toán. rủi ro (risk / 위험) appetite/sức chứa (capacity / 용량) làm preference khác nhau.

Vì vậy EMV là đầu vào (input / 입력), không phải quyết định. Risk-adjusted lập luận (reasoning / 추론) phải nhìn downside severity, reversibility, liquidity/sức chứa (capacity / 용량), mandatory ranh giới (boundary / 경계) và concentration exposure.

Một organization không có sức chứa (capacity / 용량) hấp thụ một mất mát (loss / 손실) 1 tỷ không nên hành xử như thể 1% × 1 tỷ chỉ đơn giản là 10 triệu expected chi phí (cost / 비용).

## Scenario phân tích (analysis / 분석): không ép bất định (uncertainty / 불확실성) thành một số duy nhất

Khi xác suất (probability / 확률) chưa đủ tốt để mô hình chi tiết, scenario phân tích (analysis / 분석) có thể hữu ích hơn việc tạo một con số giả chính xác. nhóm (team / 팀) xây một vài future trạng thái (state / 상태) có lô-gic (logic / 논리) nội tại, chẳng hạn cơ sở (base / 기반) trường hợp (case / 사례), downside trường hợp (case / 사례) và severe-but-plausible trường hợp (case / 사례), rồi hỏi dự án (project / 프로젝트) có còn viable trong mỗi trạng thái (state / 상태) không.

Scenario không phải ba con số tùy ý quanh estimate trung bình. Mỗi scenario nên thay đổi một nhóm driver có nhân quả (causal / 인과적) quan hệ (relation / 관계): regulation chậm phê duyệt, vendor sức chứa (capacity / 용량) giảm, adoption thấp hoặc FX biến động. Mục tiêu là kiểm tra robustness của plan và tìm giả định (assumption / 가정) nào làm quyết định (decision / 결정) đảo chiều.

Một dự án (project / 프로젝트) chỉ “tốt” trong best trường hợp (case / 사례) nhưng mất viability ngay khi adoption thấp hơn 10% đang có fragility mà một single-point forecast che mất.

## Kiểm thử sức chịu tải (stress test / 스트레스 테스트) và break điểm (point / 지점)

Scenario phân tích (analysis / 분석) có thể đi thêm một bước: thay vì hỏi kết quả (outcome / 결과) ở vài scenario cố định, hỏi parameter nào làm quyết định (decision / 결정) đổi. Adoption thấp tới mức nào thì NPV không còn dương? Vendor delay bao lâu thì legal deadline không thể recover? Defect tỷ lệ (rate / 비율) nào làm manual fallback vượt sức chứa (capacity / 용량)?

Break điểm (point / 지점) biến discussion từ “rủi ro (risk / 위험) cao hay thấp” thành “hệ thống (system / 시스템) chịu được tới đâu”. Đây là cầu nối (bridge / 브리지) giữa rủi ro (risk / 위험), finance, schedule và operations readiness.

## Monte Carlo: từ một finish date sang phân phối (distribution / 분포)

Monte Carlo simulation không “dự đoán ngày hoàn thành chính xác”. Nó chạy nhiều iteration bằng cách mẫu (sample / 표본) duration/chi phí (cost / 비용) từ phân phối (distribution / 분포) đã định cho các activity/rủi ro (risk / 위험), rồi tạo phân phối (distribution / 분포) của kết quả (outcome / 결과) tổng.

Ví dụ thay vì nói dự án (project / 프로젝트) sẽ hoàn thành ngày 30/11, simulation có thể cho:

```text
P50 finish: 30/11
P80 finish: 12/12
P90 finish: 20/12
```

P80 nghĩa trong mô hình (model / 모델) có khoảng 80% iteration hoàn thành không muộn hơn mốc đó. Nó không phải guarantee 80% ngoài đời; chất lượng phụ thuộc mạng (network / 네트워크), phân phối (distribution / 분포), correlation và các giả định (assumptions / 가정들) đầu vào.

Một lỗi phổ biến là mẫu (sample / 표본) mỗi activity độc lập dù nhiều activity cùng phụ thuộc một tài nguyên (resource / 자원) hoặc vendor. Khi correlation bị bỏ qua, tail thường trông đẹp hơn reality. Một lỗi khác là dùng phân phối (distribution / 분포) quá hẹp chỉ vì nhóm (team / 팀) không muốn forecast xấu.

Monte Carlo hữu ích nhất khi quyết định (decision / 결정) cần xác suất (probability / 확률) ngôn ngữ (language / 언어): cần contingency bao nhiêu để đạt confidence mục tiêu (target / 대상), milestone nào có tail lớn, hoặc rủi ro (risk / 위험) phản hồi (response / 응답) nào làm phân phối (distribution / 분포) thu hẹp đáng kể.

## Sensitivity và tornado thinking

Simulation tạo nhiều đầu ra (output / 출력), nhưng management vẫn cần biết driver nào quan trọng nhất. Sensitivity phân tích (analysis / 분석) đo kết quả (outcome / 결과) thay đổi mạnh ra sao khi đầu vào (input / 입력) thay đổi. Tornado chart thường sắp các driver theo mức ảnh hưởng để attention đi vào leverage điểm (point / 지점) thay vì rủi ro (risk / 위험) có tên đáng sợ nhất.

Nếu finish date nhạy nhất với regulatory approval và kiểm thử tích hợp (integration test / 통합 테스트) duration, thêm buffer vào low-impact documentation tác vụ (task / 작업) không giải quyết bất định (uncertainty / 불확실성) chính. Nếu chi phí (cost / 비용) forecast nhạy với FX nhưng nhóm (team / 팀) chỉ thảo luận overtime, rủi ro (risk / 위험) conversation đang lệch driver.

Sensitivity không chứng minh causation tuyệt đối, nhưng giúp ưu tiên nơi nên mua thêm thông tin (information / 정보) hoặc phản hồi (response / 응답).

## Xác suất (probability / 확률) không phải frequency đơn giản

Trong dự án (project / 프로젝트), xác suất (probability / 확률) thường là judgment dựa trên bằng chứng (evidence / 증거) không đầy đủ. Vì vậy numeric score cần calibration. Nếu nhóm (team / 팀) gọi gần như mọi rủi ro (risk / 위험) là “medium”, ma trận (matrix / 행렬) không tạo priority. Nếu xác suất (probability / 확률) 30% chỉ là cảm giác nhưng dashboard hiển thị 0.30 như số đo khoa học, organization đang tạo false precision.

Điều quan trọng là consistency của quy mô (scale / 규모) và chất lượng (quality / 품질) của bằng chứng (evidence / 증거), không phải số chữ số thập phân.

Calibration có thể học theo thời gian. Nếu một nhóm (team / 팀) liên tục gắn “20%” cho rủi ro (risk / 위험) nhưng gần một nửa rủi ro (risk / 위험) đó xảy ra, quy mô (scale / 규모) hoặc judgment đang miscalibrated. quyết định (decision / 결정) log và historical outcomes giúp cải thiện forecasting skill.

## Threat phản hồi (response / 응답) và opportunity phản hồi (response / 응답)

Threat có thể avoid, mitigate, transfer, accept hoặc escalate. Opportunity có thể exploit, enhance, share, accept hoặc escalate. Chọn phản hồi (response / 응답) dựa trên expected giá trị (value / 값), controllability, chi phí (cost / 비용) và rủi ro (risk / 위험) appetite.

Mitigation làm xác suất (probability / 확률) hoặc impact giảm trước khi sự kiện (event / 이벤트) xảy ra. Contingency plan được kích hoạt khi trigger xảy ra. Workaround thường là phản hồi (response / 응답) cho issue không có planned phản hồi (response / 응답) phù hợp.

Transfer không làm rủi ro (risk / 위험) biến mất khỏi dự án (project / 프로젝트) kết quả (outcome / 결과). Bảo hiểm hoặc đặc tả hợp đồng (contract / 계약) có thể chuyển financial consequence, nhưng schedule hoặc reputation tác động (effect / 효과) vẫn có thể ở lại. Đây là lý do transfer phải được hiểu theo loại exposure cụ thể.

## Điều khiển (control / 제어) taxonomy: preventive, detective, corrective

Preventive điều khiển (control / 제어) cố giảm khả năng sự kiện (event / 이벤트) xảy ra. Detective điều khiển (control / 제어) làm tín hiệu (signal / 신호) xuất hiện nhanh hơn. Corrective điều khiển (control / 제어) giảm consequence sau khi sự kiện (event / 이벤트) xảy ra.

Một dự án (project / 프로젝트) mature không chỉ hỏi “có phản hồi (response / 응답) không?” mà hỏi điều khiển (control / 제어) nằm ở đâu trên chuỗi nhân quả (causal chain / 인과 사슬). Ví dụ duplicate dữ liệu (data / 데이터) kiểm tra hợp lệ (validation / 검증) có thể prevent bad đầu vào (input / 입력), monitoring phát hiện anomaly và quay lui (rollback / 롤백) giảm impact.

Bow-tie lập luận (reasoning / 추론) hữu ích vì nó đặt sự kiện (event / 이벤트) ở giữa: bên trái là cause/preventive barrier; bên phải là consequence/mitigating barrier. Nó giúp thấy dự án (project / 프로젝트) đang dựa quá nhiều vào một điều khiển (control / 제어) duy nhất hay không.

## Điều khiển (control / 제어) effectiveness phải được kiểm chứng

Có điều khiển (control / 제어) trên giấy không có nghĩa điều khiển (control / 제어) hoạt động. Backup là điều khiển (control / 제어) chỉ khi restore đã được kiểm thử (test / 테스트). Vendor fallback là điều khiển (control / 제어) chỉ khi alternate supplier thực sự có sức chứa (capacity / 용량). Escalation đường dẫn (path / 경로) là điều khiển (control / 제어) chỉ khi người nhận có authority và phản hồi (response / 응답) thời gian (time / 시간) phù hợp.

Rủi ro (risk / 위험) rà soát (review / 검토) nên hỏi bằng chứng (evidence / 증거) về điều khiển (control / 제어) effectiveness, không chỉ status “implemented”. điều khiển (control / 제어) có thể degrade theo thời gian, đặc biệt khi cấu hình (configuration / 구성), people hoặc vendor phiên bản (version / 버전) thay đổi.

## Residual và secondary rủi ro (risk / 위험)

Phản hồi (response / 응답) có thể không loại bỏ rủi ro (risk / 위험) hoàn toàn; phần còn lại là residual rủi ro (risk / 위험). phản hồi (response / 응답) cũng có thể tạo secondary rủi ro (risk / 위험). Ví dụ duplicate vendor để giảm supply rủi ro (risk / 위험) làm tăng tích hợp (integration / 통합)/coordination rủi ro (risk / 위험). rủi ro (risk / 위험) management trưởng thành luôn hỏi “phản hồi (response / 응답) này tạo dạng thất bại (failure mode / 실패 모드) mới nào?”.

Một phản hồi (response / 응답) chỉ hợp lý khi tổng exposure sau phản hồi (response / 응답), gồm residual và secondary rủi ro (risk / 위험), tốt hơn trạng thái trước đó so với chi phí (cost / 비용) bỏ ra.

## Rủi ro (risk / 위험) sức chứa (capacity / 용량), appetite, threshold và tolerance

Rủi ro (risk / 위험) sức chứa (capacity / 용량) là mức mất mát (loss / 손실)/exposure tối đa hệ thống (system / 시스템) thực tế có thể chịu trước khi viability bị đe dọa. rủi ro (risk / 위험) appetite nói mức rủi ro (risk / 위험) organization sẵn sàng nhận để theo đuổi mục tiêu (objective / 목표). Threshold/tolerance chuyển preference thành ranh giới (boundary / 경계) hành động cụ thể.

Sức chứa (capacity / 용량) và appetite không giống nhau. Organization có thể có sức chứa (capacity / 용량) chịu delay một tháng nhưng appetite chỉ chấp nhận một tuần vì strategic timing. Ngược lại, leadership có thể muốn nhận rủi ro (risk / 위험) lớn hơn sức chứa (capacity / 용량) thực tế; quản trị (governance / 거버넌스) tốt phải surface inconsistency đó.

Ví dụ organization có thể chấp nhận schedule variance vài ngày nhưng zero tolerance với privacy breach. Hai rủi ro (risk / 위험) cùng xác suất (probability / 확률) không thể được xử lý bằng cùng priority quy tắc (rule / 규칙).

## Reserve và buffer: bảo vệ plan khỏi bất định (uncertainty / 불확실성)

Contingency reserve thường dành cho known-unknowns đã được nhận diện; management reserve bao quát unknown-unknowns hoặc bất định (uncertainty / 불확실성) ở mức cao hơn tùy quản trị (governance / 거버넌스) của tổ chức. Schedule buffer cũng có vai trò tương tự: nó hấp thụ variability thay vì giả định mọi estimate xảy ra đúng giá trị trung bình.

Reserve không phải “padding bí mật”. Nếu buffer bị giấu trong từng estimate, nhóm (team / 팀) khó biết true forecast và rủi ro (risk / 위험) exposure. Reserve nên có purpose, đơn vị sở hữu (owner / 오너) và quy tắc (rule / 규칙) sử dụng rõ.

Reserve cũng không nên được tính bằng cách cộng mechanical mọi EMV rồi coi tổng đó là đủ. Correlation, tail rủi ro (risk / 위험), non-monetary impact và confidence mục tiêu (target / 대상) có thể làm required reserve khác đáng kể expected giá trị (value / 값) trung bình.

Reserve consumption cần liên hệ rủi ro (risk / 위험) retirement. Nếu contingency đã tiêu nhưng exposure chưa giảm, dự án (project / 프로젝트) đang mất protection. Nếu rủi ro (risk / 위험) đã retire mà reserve vẫn bị giữ không cần thiết, forecast có thể quá conservative.

## Rủi ro (risk / 위험) exposure trend và rủi ro (risk / 위험) burndown

Một snapshot rủi ro (risk / 위험) register không cho biết hệ thống (system / 시스템) đang khỏe lên hay xấu đi. Có thể theo dõi exposure trend theo thời gian: tổng weighted exposure, số rủi ro (risk / 위험) vượt threshold, expected mất mát (loss / 손실) hoặc phân phối (distribution / 분포) percentile tùy ngữ cảnh (context / 맥락).

Rủi ro (risk / 위험) burndown không có nghĩa số rủi ro (risk / 위험) phải luôn giảm. Trong discovery tốt, số rủi ro (risk / 위험) có thể tăng vì nhóm (team / 팀) nhìn thấy reality rõ hơn. tín hiệu (signal / 신호) tích cực là bất định (uncertainty / 불확실성) quan trọng được retire, phản hồi (response / 응답) effectiveness tăng và residual exposure phù hợp appetite.

Nếu nhóm (team / 팀) “đóng rủi ro (risk / 위험)” để dashboard đẹp trong khi giả định (assumption / 가정) chưa được kiểm chứng, chỉ số (metric / 지표) trở thành gaming.

## Rủi ro (risk / 위험) tương tác (interaction / 상호작용) và rủi ro (risk / 위험) cascade

Rủi ro (risk / 위험) có thể gây rủi ro (risk / 위험) khác. Vendor delay có thể ép compression schedule; compression lại tăng defect rủi ro (risk / 위험); defect tăng khả năng failed UAT; failed UAT ảnh hưởng regulatory deadline. Nếu register tách từng rủi ro (risk / 위험) nhưng không thấy chuỗi nhân quả (causal chain / 인과 사슬), phản hồi (response / 응답) dễ cục bộ (local / 로컬).

Một phụ thuộc (dependency / 의존성) map hoặc bow-tie lập luận (reasoning / 추론) giúp nhìn nguyên nhân gốc (root cause / 근본 원인), preventive điều khiển (control / 제어), sự kiện (event / 이벤트) và consequence. Mục tiêu là chọn điều khiển (control / 제어) ở nơi có leverage lớn nhất.

## Systemic rủi ro (risk / 위험) và common-cause thất bại (failure / 실패)

Một portfolio dự án có thể tưởng đang diversified vì dùng nhiều nhóm (team / 팀) khác nhau nhưng thực tế cùng phụ thuộc một cloud region, một vendor định danh (identity / 식별자) provider, một key architect hoặc một regulatory approval hàng đợi (queue / 큐). Đây là common-cause rủi ro (risk / 위험).

Ở dự án (project / 프로젝트) mức (level / 수준) cũng vậy: nhiều workstream có thể trông độc lập nhưng cùng tranh một môi trường (environment / 환경) hoặc specialist. Nếu dùng chung (shared / 공유) phụ thuộc (dependency / 의존성) thất bại (fail / 실패), nhiều đường dẫn (path / 경로) cùng thất bại (fail / 실패). Register theo workstream riêng có thể che systemic exposure.

Cách xử lý là map dùng chung (shared / 공유) phụ thuộc (dependency / 의존성) và miền lỗi (failure domain / 장애 도메인), không chỉ tăng số item trong rủi ro (risk / 위험) register.

Concentration rủi ro (risk / 위험) còn có thể nằm ở giả định (assumption / 가정). Nhiều benefit trường hợp (case / 사례) có vẻ khác nhau nhưng cùng phụ thuộc adoption growth. Nếu adoption giả định (assumption / 가정) sai, nhiều benefit cùng collapse.

## Robustness, resilience và recoverability

Prediction không thể loại bỏ surprise. Robustness là khả năng hệ thống (system / 시스템) vẫn hoạt động khi đầu vào (input / 입력) thay đổi trong một phạm vi (range / 범위). Resilience là khả năng hấp thụ shock và phục hồi. Recoverability là tốc độ/năng lực (capability / 역량) quay về trạng thái acceptable sau thất bại (failure / 실패).

Redundancy, slack, modularity, fallback, cross-training và quay lui (rollback / 롤백) đều có thể là resilience investment. Chúng nhìn giống “inefficiency” nếu chỉ tối ưu utilization/chi phí (cost / 비용) bình thường, nhưng tạo option khi bất định (uncertainty / 불확실성) materialize.

Rủi ro (risk / 위험) management trưởng thành cân preventive efficiency với khôi phục (recovery / 복구) năng lực (capability / 역량). Một hệ thống (system / 시스템) không bao giờ thất bại (fail / 실패) là mục tiêu không thực tế; một hệ thống (system / 시스템) thất bại (fail / 실패) nhưng recover nhanh có thể tạo nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과) tốt hơn.

## Issue management và impediment

Issue log theo dõi đơn vị sở hữu (owner / 오너), priority, due date, impact và resolution. Impediment/blocker là trở ngại làm nhóm (team / 팀) không thể hoặc khó tiến. dự án (project / 프로젝트) manager nên ưu tiên remove hệ thống (system / 시스템) impediment hơn thúc từng người “làm nhanh hơn”.

Một issue recurring thường chỉ ra systemic cause. Nếu mỗi sprint môi trường (environment / 환경) lại hỏng, workaround liên tục không đủ; cần đầu tư vào môi trường (environment / 환경) độ tin cậy (reliability / 신뢰성).

Khi rủi ro (risk / 위험) trở thành issue, register không nên chỉ chuyển status sang “occurred” rồi bỏ. nhóm (team / 팀) cần execute phản hồi (response / 응답), cập nhật forecast, reassess secondary rủi ro (risk / 위험) và communicate impact tới người có quyết định (decision / 결정) right.

## Triage: contain trước, diagnose sau khi harm đang lan

Khi issue gây active harm, thứ tự có thể khác rủi ro (risk / 위험) phân tích (analysis / 분석) bình thường. Containment giảm blast radius trước khi root-cause phân tích (analysis / 분석) hoàn tất. bảo mật (security / 보안) sự cố (incident / 인시던트) có thể cần revoke truy cập (access / 접근) trước khi biết chính xác attacker đường dẫn (path / 경로); failed bản phát hành (release / 릴리스) có thể cần quay lui (rollback / 롤백) trước post-mortem.

Triage nên dựa trên severity, velocity, reversibility và stakeholder exposure. Không phải mọi issue cần war room; nhưng slow phân tích (analysis / 분석) trong fast-moving thất bại (failure / 실패) cũng là rủi ro (risk / 위험).

Sau containment, nhóm (team / 팀) vẫn phải diagnose và sửa hệ thống (system / 시스템). Nếu chỉ dập lửa rồi quay lại business-as-usual, recurring issue trở thành normalized thất bại (failure / 실패).

## Crisis và quyết định (decision / 결정) compression

Trong crisis, thông tin (information / 정보) không đầy đủ nhưng quyết định (decision / 결정) deadline ngắn. quản trị (governance / 거버넌스) cần pre-defined authority, communication channel và safe default để tránh mọi hành động (action / 동작) chờ escalation chuỗi (chain / 사슬) bình thường.

Crisis không phải lúc thích hợp để invent toàn bộ operating mô hình (model / 모델). Tabletop exercise và pre-agreed threshold giúp organization biết ai chỉ huy, ai communicate và điều kiện (condition / 조건) nào trigger fallback.

Sau crisis, temporary emergency authority phải được retire; nếu không, exception dễ biến thành permanent shadow quản trị (governance / 거버넌스).

## Quyết định (decision / 결정) under bất định (uncertainty / 불확실성)

Khi thiếu thông tin (information / 정보), câu hỏi không phải “làm sao biết chắc?” mà là “thông tin (information / 정보) nào đáng mua thêm?”. Prototype, spike, pilot, expert rà soát (review / 검토) hoặc experiment đều có thông tin (information / 정보) giá trị (value / 값). Một kiểm thử (test / 테스트) hai ngày có thể đáng làm nếu tránh commitment sáu tháng.

Reversible quyết định (decision / 결정) nên được decentralize và thực hiện nhanh hơn. Irreversible/high-impact quyết định (decision / 결정) cần bằng chứng (evidence / 증거) và rà soát (review / 검토) mạnh hơn. Đây là cách liên kết quyết định (decision / 결정) chi phí (cost / 비용) với quản trị (governance / 거버넌스).

Giá trị (value / 값) of thông tin (information / 정보) có thể lập luận (reasoning / 추론) định tính: nếu một thử nghiệm rẻ có khả năng thay đổi một quyết định (decision / 결정) rất đắt, kiểm thử (test / 테스트) thường đáng làm. Nếu dù kết quả nào quyết định (decision / 결정) cũng không đổi, thu thêm dữ liệu (data / 데이터) chỉ trì hoãn hành động (action / 동작).

## Quyết định (decision / 결정) regret và chi phí (cost / 비용) of waiting

“Thu thêm thông tin (information / 정보)” cũng là một quyết định (decision / 결정) có chi phí (cost / 비용). Trong thị trường (market / 시장) cửa sổ (window / 윈도우) ngắn, chờ certainty có thể làm option hết hạn. Trong an toàn (safety / 안전) issue, delay để phân tích thêm có thể tăng harm.

Quyết định (decision / 결정) lập luận (reasoning / 추론) cần cân expected regret hai phía: regret vì lần ghi nhận (commit / 커밋) sai quá sớm và regret vì chờ quá lâu. Reversibility, thông tin (information / 정보) giá trị (value / 값) và chi phí (cost / 비용) of delay quyết định balance.

Không tồn tại quy tắc (rule / 규칙) “luôn phân tích trước” hoặc “luôn hành động nhanh”. ngữ cảnh (context / 맥락) quyết định thông tin (information / 정보) threshold phù hợp.

## Real options: giữ quyền lựa chọn có thể có giá trị

Trong bất định (uncertainty / 불확실성) cao, giá trị (value / 값) không chỉ đến từ chọn option “tốt nhất” hôm nay mà còn từ giữ khả năng đổi hướng khi có thêm thông tin (information / 정보). Pilot nhỏ, kiến trúc (architecture / 아키텍처) modular, đặc tả hợp đồng (contract / 계약) có exit clause hoặc phased investment đều có thể tạo option giá trị (value / 값).

Một commitment lớn không đảo ngược có thể rẻ hơn nominally nhưng làm mất flexibility. Một approach đắt hơn chút nhưng cho phép stop/pivot sau milestone có thể tốt hơn nếu bất định (uncertainty / 불확실성) lớn.

Real-options thinking không có nghĩa trì hoãn mọi quyết định (decision / 결정). Option cũng có chi phí (cost / 비용) và expiry. Câu hỏi là flexibility có đáng giá hơn chi phí (cost / 비용) giữ option không.

## Quyết định (decision / 결정) chất lượng (quality / 품질) khác kết quả (outcome / 결과) chất lượng (quality / 품질)

Một quyết định tốt vẫn có thể cho kết quả (outcome / 결과) xấu vì bất định (uncertainty / 불확실성); một quyết định tệ đôi khi may mắn cho kết quả (outcome / 결과) tốt. Nếu nhóm (team / 팀) chỉ đánh giá quyết định (decision / 결정) theo kết quả cuối, họ dễ học sai.

Post-decision rà soát (review / 검토) nên hỏi: thông tin (information / 정보) lúc đó là gì, giả định (assumption / 가정) nào hợp lý, alternative nào được cân nhắc, rủi ro (risk / 위험) threshold nào áp dụng và điều gì mới xuất hiện sau quyết định (decision / 결정). Đây là nền tảng của organizational học tập (learning / 학습).

Quyết định (decision / 결정) log giúp chống hindsight độ lệch (bias / 편향). Sau khi biết kết quả (outcome / 결과), con người dễ tin rằng kết quả (result / 결과) “rõ ràng từ đầu”. Ghi prediction, confidence và rationale tại thời điểm quyết định (decision / 결정) tạo bằng chứng (evidence / 증거) để học calibration thật.

## Cognitive độ lệch (bias / 편향) trong rủi ro (risk / 위험) quyết định (decision / 결정)

Optimism độ lệch (bias / 편향) làm estimate quá đẹp. Anchoring khiến nhóm (team / 팀) bám con số đầu tiên. Availability độ lệch (bias / 편향) làm sự kiện (event / 이벤트) mới xảy ra được đánh giá quá cao. Sunk-cost tác động (effect / 효과) khiến organization tiếp tục investment chỉ vì đã chi nhiều. Confirmation độ lệch (bias / 편향) khiến nhóm (team / 팀) tìm bằng chứng (evidence / 증거) ủng hộ plan đã chọn.

Không thể loại bỏ độ lệch (bias / 편향) hoàn toàn, nhưng có thể thiết kế countermeasure: independent rà soát (review / 검토), phạm vi (range / 범위) estimate, pre-mortem, tường minh (explicit / 명시적) exit criteria và quyết định (decision / 결정) log.

Groupthink và authority độ lệch (bias / 편향) cũng quan trọng. Nếu cấp cao (senior / 시니어) leader nói “vendor này chắc chắn ổn”, nhóm (team / 팀) có thể ngừng surface weak tín hiệu (signal / 신호). Psychological an toàn (safety / 안전) ở chapter People vì vậy là một risk-control cơ chế (mechanism / 메커니즘) thực sự.

## Opportunity management không chỉ là “rủi ro (risk / 위험) tích cực” trên giấy

Opportunity có thể là supplier sẵn sức chứa (capacity / 용량) sớm, thị trường (market / 시장) demand tăng, reusable nền tảng (platform / 플랫폼) hoặc regulation mở option mới. Nếu opportunity chỉ được ghi vào register nhưng không có trigger/sức chứa (capacity / 용량) để exploit, nó không tạo giá trị (value / 값).

Opportunity phản hồi (response / 응답) cũng cạnh tranh tài nguyên (resource / 자원) với threat mitigation. Organization cần nhìn expected upside, strategic fit và option expiry. Một opportunity có thể biến thành threat nếu quy mô (scale / 규모) quá nhanh làm operations quá tải.

## Ví dụ scenario

Nhóm (team / 팀) phát hiện vendor OCR có accuracy thấp với giấy tờ cũ, nhưng chưa biết mức độ. Thay vì ngay lập tức đổi vendor hoặc chấp nhận rủi ro (risk / 위험), PM có thể thiết kế mẫu (sample / 표본) kiểm thử (test / 테스트) đại diện, đo accuracy theo segment, estimate nghiệp vụ (business / 비즈니스) impact, tìm fallback manual rà soát (review / 검토) và xác định threshold go/no-go. Đây là rủi ro (risk / 위험) reduction bằng thông tin (information / 정보).

Nếu kết quả cho thấy chỉ 2% document bị ảnh hưởng và manual rà soát (review / 검토) đủ sức chứa (capacity / 용량), mitigation có thể rẻ hơn đổi vendor. Nếu thất bại (failure / 실패) tập trung ở một loại giấy tờ bắt buộc và compliance không cho manual exception, rủi ro (risk / 위험) profile thay đổi hoàn toàn. Cùng một technical symptom nhưng quyết định (decision / 결정) phụ thuộc impact mô hình (model / 모델).

Một scenario schedule khác: deterministic plan nói go-live 30/11, nhưng simulation cho P50 là 30/11 và P80 là 12/12. Nếu đặc tả hợp đồng (contract / 계약) penalty bắt đầu 5/12, quản lý không nên báo “on nhánh học (track / 트랙) 30/11” như một fact duy nhất. Cần surface confidence phân phối (distribution / 분포), driver chính và option giảm tail—ví dụ early tích hợp (integration / 통합) hoặc giảm shared-resource contention.

Một scenario resilience: payment API phụ thuộc một vendor đạt SLA 99.99%, nhưng không có degraded chế độ (mode / 모드). Expected outage thấp, song mỗi outage chặn toàn bộ sales. Một fallback manual/queued processing có thể tạo nhiều giá trị (value / 값) hơn việc mua thêm 0.005% SLA vì nó giảm consequence thay vì chỉ xác suất (probability / 확률).

## Anti-patterns

Rủi ro (risk / 위험) register dài nhưng không có đơn vị sở hữu (owner / 오너) là documentation theater. Chỉ theo dõi red rủi ro (risk / 위험) nhưng bỏ correlation là nhìn từng cây mà mất rừng. Chỉ nói “monitor” mà không có trigger là trì hoãn quyết định (decision / 결정). Escalate mọi rủi ro (risk / 위험) làm quản trị (governance / 거버넌스) overload; không escalate rủi ro (risk / 위험) vượt tolerance lại là quản trị (governance / 거버넌스) thất bại (failure / 실패).

Dùng Monte Carlo với đầu vào (input / 입력) giả chính xác cũng chỉ tạo false precision đẹp hơn. Dùng EMV như luật quyết định duy nhất bỏ qua tail, sức chứa (capacity / 용량), appetite và ethics. điều khiển (control / 제어) “implemented” nhưng chưa kiểm thử (test / 테스트) là paper điều khiển (control / 제어). Reserve bị tiêu mà exposure không giảm là protection erosion.

Mục tiêu không phải có nhiều rủi ro (risk / 위험) item hay nhiều chart mà là tạo preparedness, option, resilience và timely quyết định (decision / 결정).

## Mô hình tư duy (mental model / 사고 모델)

> rủi ro (risk / 위험) management không nhằm dự đoán đúng tương lai; nó xây một nhân quả (causal / 인과적) mô hình (model / 모델) đủ tốt để biết bất định (uncertainty / 불확실성) nào cần học, điều khiển (control / 제어) nào cần kiểm chứng, exposure nào hệ thống (system / 시스템) có thể chịu, option nào nên giữ và cách phục hồi khi surprise vượt prediction.

Tiếp theo: [Governance, compliance và business environment](./09_governance_compliance_and_business_environment.md).

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 foundations value and project system](./00_foundations_value_and_project_system.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
