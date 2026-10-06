# 14 — Artifacts, thông tin (information / 정보) luồng (flow / 흐름) và traceability

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **14 — Artifacts, thông tin (information / 정보) luồng (flow / 흐름) và traceability**. Route đi từ artifact và decision information → temporary organization memory → registers, logs, baselines và plans → traceability, versioning và handoff → auditability, để sản phẩm tạo ra phục vụ quyết định thay vì chỉ là tài liệu.

## Sản phẩm tạo ra (artifact / 산출물) chỉ có giá trị khi nó giữ hoặc truyền thông tin (information / 정보) cần cho quyết định (decision / 결정)

PMP có nhiều tên sản phẩm tạo ra (artifact / 산출물) nên người học dễ biến chúng thành danh sách cần thuộc. Cách hiểu bền hơn là hỏi mỗi sản phẩm tạo ra (artifact / 산출물) giải quyết thông tin (information / 정보) bài toán (problem / 문제) nào. Một register giữ tập item cùng loại qua thời gian; một log ghi các sự kiện (event / 이벤트)/quyết định (decision / 결정) cần theo dõi; một baseline tạo tham chiếu (reference / 참조) để đo variance; một plan định nghĩa cách một loại công việc (work / 작업)/điều khiển (control / 제어) sẽ được thực hiện; một report nén trạng thái (state / 상태) thành thông tin (information / 정보) cho stakeholder; một agreement tạo commitment giữa các party.

Nếu sản phẩm tạo ra (artifact / 산출물) không có bên tiêu thụ (consumer / 소비자) hoặc không thay đổi quyết định (decision / 결정)/điều khiển (control / 제어) nào, nó có nguy cơ trở thành administrative waste. Ngược lại, thiếu sản phẩm tạo ra (artifact / 산출물) ở chỗ thất bại (failure / 실패) chi phí (cost / 비용) cao làm dự án (project / 프로젝트) mất bộ nhớ (memory / 메모리) và accountability.

Một sản phẩm tạo ra (artifact / 산출물) tốt cần answer bốn câu: ai dùng, để quyết điều gì, cập nhật (update / 업데이트) khi nào, và đâu là nguồn chuẩn (source of truth / 정본). Nếu không trả lời được, sản phẩm tạo ra (artifact / 산출물) có thể đang tồn tại vì tradition chứ không vì thông tin (information / 정보) need.

> **Nối mạch:** **Sản phẩm tạo ra (artifact / 산출물) là bên ngoài (external / 외부) bộ nhớ (memory / 메모리) của temporary organization** nối từ **Sản phẩm tạo ra (artifact / 산출물) chỉ có giá trị khi nó giữ hoặc truyền thông tin (information / 정보) cần cho quyết định (decision / 결정)** sang **Dự án (project / 프로젝트) thông tin (information / 정보) kiến trúc (architecture / 아키텍처) có nhiều lớp**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sản phẩm tạo ra (artifact / 산출물) là bên ngoài (external / 외부) bộ nhớ (memory / 메모리) của temporary organization

Dự án (project / 프로젝트) là tổ chức tạm thời. Con người thay đổi, bộ nhớ (memory / 메모리) cá nhân mất đi và quyết định (decision / 결정) diễn ra ở nhiều thời điểm. sản phẩm tạo ra (artifact / 산출물) tồn tại để externalize bộ nhớ (memory / 메모리), làm coordination không phụ thuộc hoàn toàn vào việc “ai đó còn nhớ”.

Điều này đặc biệt quan trọng ở dự án (project / 프로젝트) dài hoặc có nhiều vendor. Một quyết định không ghi rationale có thể bị tranh luận lại vài tháng sau hoặc bị hiểu sai khi người cũ rời nhóm (team / 팀).

Bên ngoài (external / 외부) bộ nhớ (memory / 메모리) còn giúp accountability công bằng hơn. Khi quyết định (decision / 결정) được đánh giá bằng hindsight, sản phẩm tạo ra (artifact / 산출물) cho biết thông tin (information / 정보) và giả định (assumption / 가정) có sẵn tại thời điểm quyết định, thay vì dùng kiến thức (knowledge / 지식) xuất hiện sau đó để phán xét quá khứ.

> **Nối mạch:** **Dự án (project / 프로젝트) thông tin (information / 정보) kiến trúc (architecture / 아키텍처) có nhiều lớp** nối từ **Sản phẩm tạo ra (artifact / 산출물) là bên ngoài (external / 외부) bộ nhớ (memory / 메모리) của temporary organization** sang **Từ giả định (assumption / 가정) tới quyết định (decision / 결정)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dự án (project / 프로젝트) thông tin (information / 정보) kiến trúc (architecture / 아키텍처) có nhiều lớp

Một mô hình tư duy (mental model / 사고 모델) hữu ích là tách thông tin (information / 정보) thành bốn lớp:

```text
source evidence
    ↓
operational state
    ↓
decision / commitment
    ↓
reporting / governance view
```

Nguồn (source / 소스) bằng chứng (evidence / 증거) có thể là kiểm thử (test / 테스트) kết quả (result / 결과), invoice, hệ thống (system / 시스템) log, signed đặc tả hợp đồng (contract / 계약) hoặc stakeholder approval. Operational trạng thái (state / 상태) là rủi ro (risk / 위험) status, công việc (work / 작업) progress, forecast. quyết định (decision / 결정) tầng (layer / 계층) giữ approval, priority, exception và rationale. Reporting tầng (layer / 계층) nén trạng thái (state / 상태) cho steering committee hoặc stakeholder.

Nếu report không dấu vết (trace / 추적) được về nguồn (source / 소스) bằng chứng (evidence / 증거), dispute khó resolve. Nếu nguồn (source / 소스) bằng chứng (evidence / 증거) có nhưng quyết định (decision / 결정) không được bản ghi (record / 레코드), dự án (project / 프로젝트) biết “điều gì xảy ra” nhưng không biết “vì sao trạng thái (state / 상태) đổi”.

> **Nối mạch:** **Từ giả định (assumption / 가정) tới quyết định (decision / 결정)** nối từ **Dự án (project / 프로젝트) thông tin (information / 정보) kiến trúc (architecture / 아키텍처) có nhiều lớp** sang **Thông tin (information / 정보) chuyển tiếp trạng thái (state transition / 상태 전이) cần được mô hình (model / 모델) tường minh (explicit / 명시적)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Từ giả định (assumption / 가정) tới quyết định (decision / 결정)

Giả định (assumption / 가정) log ghi điều đang được coi là đúng nhưng chưa được chứng minh chắc chắn. ràng buộc (constraint / 제약조건) là ranh giới (boundary / 경계) phải tôn trọng. rủi ro (risk / 위험) register quản lý bất định (uncertainty / 불확실성) có tác động (effect / 효과) lên mục tiêu (objective / 목표). Issue log quản lý bài toán (problem / 문제) đã materialize. thay đổi (change / 변경) log theo dõi proposed/approved/rejected thay đổi (change / 변경). quyết định (decision / 결정) log giữ quyết định, rationale, đơn vị sở hữu (owner / 오너) và thời điểm.

Các sản phẩm tạo ra (artifact / 산출물) này không tách biệt hoàn toàn. Ví dụ giả định (assumption / 가정) “vendor API ổn định trước UAT” bị bằng chứng (evidence / 증거) mới bác bỏ. giả định (assumption / 가정) chuyển thành rủi ro (risk / 위험) hoặc issue; rủi ro (risk / 위험) phân tích (analysis / 분석) tạo option; quyết định (decision / 결정) đổi tích hợp (integration / 통합) plan; thay đổi (change / 변경) có thể cập nhật schedule baseline. Traceability tốt cho phép đi ngược chuỗi để hiểu vì sao plan hiện tại khác plan ban đầu.

Một dự án (project / 프로젝트) thông tin (information / 정보) hệ thống (system / 시스템) trưởng thành không chỉ có nhiều document; nó cho phép chuyển tiếp trạng thái (state transition / 상태 전이) giữa các loại thông tin (information / 정보) mà không mất ngữ cảnh (context / 맥락).

> **Nối mạch:** **Thông tin (information / 정보) chuyển tiếp trạng thái (state transition / 상태 전이) cần được mô hình (model / 모델) tường minh (explicit / 명시적)** nối từ **Từ giả định (assumption / 가정) tới quyết định (decision / 결정)** sang **Register, log, plan, baseline, report và agreement khác nhau về purpose**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thông tin (information / 정보) chuyển tiếp trạng thái (state transition / 상태 전이) cần được mô hình (model / 모델) tường minh (explicit / 명시적)

Một tín hiệu (signal / 신호) thường đi qua nhiều trạng thái (state / 상태):

```text
observation → assumption/question → risk/issue → analysis → decision → change/action → evidence → closure
```

Không phải mọi tín hiệu (signal / 신호) đi hết chuỗi, nhưng mô hình tư duy (mental model / 사고 모델) này giúp phát hiện “missing chuyển tiếp (transition / 전이)”. Nếu issue đã resolved nhưng quyết định (decision / 결정)/hành động (action / 동작) bằng chứng (evidence / 증거) không có, status close có thể chỉ là administrative.

Nếu thay đổi (change / 변경) được approved nhưng yêu cầu (requirement / 요구사항)/baseline không cập nhật (update / 업데이트), thông tin (information / 정보) trạng thái (state / 상태) bị split. Nếu rủi ro (risk / 위험) trigger xảy ra mà item vẫn nằm trong rủi ro (risk / 위험) register như “open rủi ro (risk / 위험)” nhưng không thành issue/hành động (action / 동작), công cụ (tool / 도구) đang giữ label cũ hơn reality.

> **Nối mạch:** **Register, log, plan, baseline, report và agreement khác nhau về purpose** nối từ **Thông tin (information / 정보) chuyển tiếp trạng thái (state transition / 상태 전이) cần được mô hình (model / 모델) tường minh (explicit / 명시적)** sang **Ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약): cùng một trường dữ liệu (field / 필드) phải có cùng meaning**, vì cơ chế trước tạo đầu vào cho bước sau.

## Register, log, plan, baseline, report và agreement khác nhau về purpose

Register thường là tập các item cùng loại cần theo dõi qua thời gian, ví dụ rủi ro (risk / 위험) register hoặc stakeholder register. Log nhấn mạnh sự kiện (event / 이벤트)/hành động (action / 동작) lịch sử (history / 이력), ví dụ issue log hoặc quyết định (decision / 결정) log. Plan mô tả cách quản lý một lĩnh vực (domain / 도메인). Baseline là tham chiếu (reference / 참조) được authorize. Report là view nén cho một audience. Agreement ghi commitment giữa party.

Phân biệt theo thông tin (information / 정보) purpose giúp nhớ sản phẩm tạo ra (artifact / 산출물) tự nhiên hơn học tên riêng lẻ.

> **Nối mạch:** **Register, log, plan, baseline, report và agreement khác nhau về purpose** đặt vấn đề; **Ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약): cùng một trường dữ liệu (field / 필드) phải có cùng meaning** kiểm tra bằng chứng, rồi **Dữ liệu (data / 데이터) lineage: con số này đến từ đâu?** mở rộng hệ quả.

## Ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약): cùng một trường dữ liệu (field / 필드) phải có cùng meaning

Một dashboard có thể đúng về arithmetic nhưng sai về ngữ nghĩa (semantics / 의미론). “Completed” ở nhóm (team / 팀) A có thể nghĩa mã (code / 코드) complete; ở nhóm (team / 팀) B nghĩa accepted; ở nhóm (team / 팀) C nghĩa deployed. Tổng 80% completion khi definitions khác nhau không có meaning ổn định.

Trọng yếu (critical / 중요) chỉ số (metric / 지표)/sản phẩm tạo ra (artifact / 산출물) cần ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약): definition, đơn vị (unit / 단위), nguồn (source / 소스), đơn vị sở hữu (owner / 오너), cutoff, inclusion/exclusion và cập nhật (update / 업데이트) quy tắc (rule / 규칙). Khi definition đổi, lịch sử (history / 이력) có thể không còn comparable.

Ngữ nghĩa (semantic / 의미적) drift là dạng thất bại (failure mode / 실패 모드) khi cùng tên chỉ số (metric / 지표) thay meaning theo thời gian nhưng chart vẫn nối thành một line như không có gì đổi.

> **Nối mạch:** **Ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약): cùng một trường dữ liệu (field / 필드) phải có cùng meaning** đặt vấn đề; **Dữ liệu (data / 데이터) lineage: con số này đến từ đâu?** kiểm tra bằng chứng, rồi **Requirements Traceability ma trận (matrix / 행렬) như một đồ thị (graph / 그래프)** mở rộng hệ quả.

## Dữ liệu (data / 데이터) lineage: con số này đến từ đâu?

Lineage trả lời một reported giá trị (value / 값) được tạo từ nguồn (source / 소스) nào, transform ra sao và phiên bản (version / 버전)/cutoff nào. Ví dụ dashboard chi phí (cost / 비용) lấy invoice từ ERP, committed amount từ procurement và forecast từ PM công cụ (tool / 도구).

Nếu steering committee hỏi vì sao EAC tăng 10%, nhóm (team / 팀) nên dấu vết (trace / 추적) được thay đổi (change / 변경) về vendor quote, phạm vi (scope / 범위) quyết định (decision / 결정) hoặc productivity bằng chứng (evidence / 증거). “Dashboard tự tính” không phải explanation.

Lineage đặc biệt quan trọng khi automation aggregate nhiều hệ thống (system / 시스템). Tự động hóa làm calculation nhanh hơn nhưng cũng có thể propagate ngữ nghĩa (semantic / 의미적) lỗi (error / 오류) nhanh hơn.

> **Nối mạch:** **Dữ liệu (data / 데이터) lineage: con số này đến từ đâu?** đặt vấn đề; **Requirements Traceability ma trận (matrix / 행렬) như một đồ thị (graph / 그래프)** kiểm tra bằng chứng, rồi **Traceability là đồ thị (graph / 그래프) hai chiều** mở rộng hệ quả.

## Requirements Traceability ma trận (matrix / 행렬) như một đồ thị (graph / 그래프)

Requirements Traceability ma trận (matrix / 행렬) thường được dạy như một bảng. mô hình tư duy (mental model / 사고 모델) tốt hơn là đồ thị (graph / 그래프):

```text
business need
   ↓
requirement
   ↓
design/deliverable
   ↓
verification / acceptance evidence
   ↓
outcome / benefit metric
```

Không phải mọi dự án (project / 프로젝트) cần một spreadsheet RTM nặng. Nhưng regulated/high-risk dự án (project / 프로젝트) cần khả năng chứng minh yêu cầu (requirement / 요구사항) nào được thực hiện ở đâu và bằng chứng (evidence / 증거) nào xác nhận nó.

Trong software, traceability kỹ thuật có thể nối ticket → lần ghi nhận (commit / 커밋) → bản dựng (build / 빌드) → kiểm thử (test / 테스트) → triển khai (deployment / 배포). PMP quan tâm ranh giới (boundary / 경계) lớn hơn: yêu cầu (requirement / 요구사항) đó đến từ stakeholder/chính sách (policy / 정책) nào và acceptance/giá trị (value / 값) được xác nhận ra sao.

> **Nối mạch:** **Traceability là đồ thị (graph / 그래프) hai chiều** nối từ **Requirements Traceability ma trận (matrix / 행렬) như một đồ thị (graph / 그래프)** sang **Traceability debt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Traceability là đồ thị (graph / 그래프) hai chiều

Forward dấu vết (trace / 추적) trả lời yêu cầu (requirement / 요구사항) này được implement và verify ở đâu. Backward dấu vết (trace / 추적) trả lời tính năng (feature / 기능) hoặc điều khiển (control / 제어) này tồn tại vì yêu cầu (requirement / 요구사항)/nghiệp vụ (business / 비즈니스) need nào. Hai chiều đều quan trọng.

Nếu một tính năng (feature / 기능) không dấu vết (trace / 추적) được tới need nào, nó có thể là phạm vi (scope / 범위) creep. Nếu một yêu cầu (requirement / 요구사항) không dấu vết (trace / 추적) được tới xác minh (verification / 확인) bằng chứng (evidence / 증거), dự án (project / 프로젝트) chưa chứng minh completion. Nếu một kiểm thử (test / 테스트) không dấu vết (trace / 추적) tới yêu cầu (requirement / 요구사항), có thể đang kiểm thứ không cần hoặc yêu cầu (requirement / 요구사항) chưa rõ.

> **Nối mạch:** **Traceability debt** nối từ **Traceability là đồ thị (graph / 그래프) hai chiều** sang **Dự án (project / 프로젝트) management plan và subsidiary plans**, vì cơ chế trước tạo đầu vào cho bước sau.

## Traceability debt

Traceability debt xuất hiện khi công việc (work / 작업) vẫn tiến nhưng link giữa need, thay đổi (change / 변경), hiện thực (implementation / 구현) và bằng chứng (evidence / 증거) không được cập nhật. Debt có thể chưa gây thất bại (failure / 실패) ngay, nhưng chi phí (cost / 비용) xuất hiện khi kiểm tra (audit / 감사), sự cố (incident / 인시던트) hoặc thay đổi (change / 변경) impact phân tích (analysis / 분석) cần reconstruct lịch sử (history / 이력).

Debt tăng nhanh trong môi trường (environment / 환경) nhiều thay đổi (change / 변경). Nếu nhóm (team / 팀) liên tục sửa yêu cầu (requirement / 요구사항) nhưng RTM/kiểm thử (test / 테스트) ánh xạ (mapping / 매핑) chỉ cập nhật (update / 업데이트) cuối bản phát hành (release / 릴리스), họ đang tích thông tin (information / 정보) rework tương tự technical debt.

Không phải mọi dự án (project / 프로젝트) cần zero traceability debt. Low-risk prototype có thể chấp nhận nhẹ; regulated dự án (project / 프로젝트) có tolerance thấp hơn. Mức traceability phải tailor theo consequence.

> **Nối mạch:** **Dự án (project / 프로젝트) management plan và subsidiary plans** nối từ **Traceability debt** sang **Baseline và working document**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dự án (project / 프로젝트) management plan và subsidiary plans

Dự án (project / 프로젝트) management plan là integrated điều khiển (control / 제어) mô hình (model / 모델). Các subsidiary plan như phạm vi (scope / 범위), schedule, chi phí (cost / 비용), chất lượng (quality / 품질), tài nguyên (resource / 자원), communication, rủi ro (risk / 위험), procurement hoặc stakeholder engagement chỉ nên tách khi độ phức tạp (complexity / 복잡도) cần separation. Chúng trả lời “chúng ta sẽ quản lý lĩnh vực (domain / 도메인) này như thế nào?”, không phải “trạng thái (state / 상태) hiện tại là gì?”.

Đây là distinction hữu ích: plan mô tả phương thức (method / 메서드)/điều khiển (control / 제어); document/register thường mô tả hiện tại (current / 현재) thông tin (information / 정보). rủi ro (risk / 위험) management plan định nghĩa rủi ro (risk / 위험) tiến trình (process / 프로세스)/scales/roles; rủi ro (risk / 위험) register chứa rủi ro (risk / 위험) cụ thể.

Một plan stale nguy hiểm nếu nhóm (team / 팀) vẫn tưởng đó là operating quy tắc (rule / 규칙) hiện hành. Plan thay đổi (change / 변경) cần quản trị (governance / 거버넌스) phù hợp với impact.

> **Nối mạch:** **Baseline và working document** nối từ **Dự án (project / 프로젝트) management plan và subsidiary plans** sang **Sản phẩm tạo ra (artifact / 산출물) vòng đời (lifecycle / 생명주기): draft → reviewed → approved → effective → superseded → archived**, vì cơ chế trước tạo đầu vào cho bước sau.

## Baseline và working document

Baseline là authorized tham chiếu (reference / 참조). Working forecast/document có thể thay đổi thường xuyên. Nhầm hai lớp tạo confusion: nếu mọi cập nhật (update / 업데이트) forecast tự động rewrite baseline thì variance biến mất; nếu baseline không bao giờ được rebaseline dù mục tiêu (objective / 목표) đã formally đổi, chỉ số (metric / 지표) mất ý nghĩa.

Rebaseline phải là quản trị (governance / 거버넌스) quyết định (decision / 결정) khi planning basis thay đổi đủ lớn, không phải cách che hiệu năng (performance / 성능) xấu.

Một useful mẫu (pattern / 패턴) là giữ baseline, actual và forecast tách rõ. Khi một stakeholder hỏi “plan là gì?”, cần biết họ đang hỏi commitment đã approve hay hiện tại (current / 현재) expected kết quả (outcome / 결과).

> **Nối mạch:** Baseline và working document cung cấp trạng thái cần quản lý; **Artifact lifecycle** giải thích cách tài liệu đi từ draft tới archived. **Immutable history và audit trail** kiểm tra hệ quả của từng chuyển trạng thái.

## Sản phẩm tạo ra (artifact / 산출물) vòng đời (lifecycle / 생명주기): draft → reviewed → approved → effective → superseded → archived

Không phải tệp (file / 파일) mới nhất luôn là tệp (file / 파일) có hiệu lực. đặc tả hợp đồng (contract / 계약) amendment có thể signed nhưng effective từ tháng sau; chính sách (policy / 정책) draft mới hơn vẫn chưa replace approved phiên bản (version / 버전).

Trọng yếu (critical / 중요) sản phẩm tạo ra (artifact / 산출물) nên có vòng đời (lifecycle / 생명주기) trạng thái (state / 상태) và effective date rõ. “Latest modified” khác “authorized hiện tại (current / 현재)”.

Superseded sản phẩm tạo ra (artifact / 산출물) vẫn có historical giá trị (value / 값). Xóa phiên bản (version / 버전) cũ làm mất kiểm tra (audit / 감사) trail và khiến quyết định (decision / 결정) cũ khó hiểu.

> **Nối mạch:** Artifact lifecycle tạo lịch sử có thể truy nguyên; **Immutable history và audit trail** giữ bằng chứng. **Change request như information packet** kiểm tra ai đổi gì, vì sao và với tác động nào.

## Immutable lịch sử (history / 이력) và kiểm tra (audit / 감사) trail

Một số bằng chứng (evidence / 증거) cần append-only hoặc immutable lịch sử (history / 이력): approval, financial giao dịch (transaction / 트랜잭션), kiểm thử (test / 테스트) kết quả (result / 결과), quyết định (decision / 결정) bản ghi (record / 레코드). Không nhất thiết dùng blockchain; principle là không overwrite lịch sử (history / 이력) tới mức không biết trạng thái (state / 상태) trước.

Version-control hệ thống (system / 시스템), signed document repository hoặc nhật ký kiểm tra (audit log / 감사 로그) có thể cung cấp cơ chế (mechanism / 메커니즘). Mục tiêu là reconstruct được ai thay gì, khi nào, vì sao và authority nào.

Kiểm tra (audit / 감사) trail mạnh đặc biệt quan trọng khi exception/compliance quyết định (decision / 결정) có consequence cao.

> **Nối mạch:** **Thay đổi (change / 변경) yêu cầu (request / 요청) như một thông tin (information / 정보) packet** nối từ **Immutable lịch sử (history / 이력) và kiểm tra (audit / 감사) trail** sang **Bằng chứng (evidence / 증거) gói (package / 패키지) cho gate**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thay đổi (change / 변경) yêu cầu (request / 요청) như một thông tin (information / 정보) packet

Thay đổi (change / 변경) yêu cầu (request / 요청) không chỉ là câu “hãy đổi phạm vi (scope / 범위)”. Một yêu cầu (request / 요청) tốt nên đủ ngữ cảnh (context / 맥락) để authority ra quyết định (decision / 결정): reason, affected mục tiêu (objective / 목표), impact lên schedule/chi phí (cost / 비용)/rủi ro (risk / 위험)/chất lượng (quality / 품질), option và urgency.

Nếu quản trị (governance / 거버넌스) body phải tự tìm lại toàn bộ impact, quyết định (decision / 결정) độ trễ (latency / 지연 시간) tăng. sản phẩm tạo ra (artifact / 산출물) tốt giảm giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) của quản trị (governance / 거버넌스).

Quyết định (decision / 결정) packet càng high-impact càng cần bằng chứng (evidence / 증거) về alternative và recommendation, không chỉ one-option yêu cầu (request / 요청). Nếu yêu cầu (request / 요청) chỉ trình bày solution mong muốn, quản trị (governance / 거버넌스) khó biết sự đánh đổi (trade-off / 트레이드오프) thật.

> **Nối mạch:** **Thay đổi (change / 변경) yêu cầu (request / 요청) như một thông tin (information / 정보) packet** đặt vấn đề; **Bằng chứng (evidence / 증거) gói (package / 패키지) cho gate** kiểm tra bằng chứng, rồi **Quyết định (decision / 결정) log và giả định (assumption / 가정) expiration** mở rộng hệ quả.

## Bằng chứng (evidence / 증거) gói (package / 패키지) cho gate

Stage gate, go/no-go hoặc regulatory approval thường cần nhiều bằng chứng (evidence / 증거): yêu cầu (requirement / 요구사항) status, kiểm thử (test / 테스트) kết quả (result / 결과), unresolved rủi ro (risk / 위험), operational readiness, đặc tả hợp đồng (contract / 계약) status và approval.

Một gate gói (package / 패키지) tốt không phải folder chứa mọi tệp (file / 파일). Nó là curated proof rằng exit criteria đã được đáp ứng hoặc exception đã được authority accept.

Gate theater xảy ra khi meeting vẫn “approve” dù bằng chứng (evidence / 증거) gói (package / 패키지) incomplete vì deadline pressure. Khi đó sản phẩm tạo ra (artifact / 산출물) tồn tại nhưng điều khiển (control / 제어) mục tiêu (objective / 목표) đã thất bại (fail / 실패).

> **Nối mạch:** **Bằng chứng (evidence / 증거) gói (package / 패키지) cho gate** đặt vấn đề; **Quyết định (decision / 결정) log và giả định (assumption / 가정) expiration** kiểm tra bằng chứng, rồi **Quyết định (decision / 결정) provenance** mở rộng hệ quả.

## Quyết định (decision / 결정) log và giả định (assumption / 가정) expiration

Quyết định (decision / 결정) log nên ghi không chỉ quyết định (decision / 결정) mà còn key giả định (assumption / 가정). Nếu giả định (assumption / 가정) thay đổi, quyết định (decision / 결정) có thể cần rà soát (review / 검토).

Ví dụ “chọn vendor A vì chi phí (cost / 비용) thấp nhất và API đáp ứng thông lượng (throughput / 처리량) 1.000 req/s”. Nếu forecast traffic tăng lên 5.000 req/s, quyết định (decision / 결정) cũ không sai tại thời điểm đó nhưng basis đã hết hạn.

Điều này giúp organization tránh hai cực: giữ quyết định (decision / 결정) cũ quá lâu hoặc blame người cũ bằng thông tin (information / 정보) mới.

Một quyết định (decision / 결정) bản ghi (record / 레코드) mạnh nên gồm ngữ cảnh (context / 맥락), options considered, đơn vị sở hữu (owner / 오너)/authority, rationale, effective date, affected artifacts và rà soát (review / 검토) trigger.

> **Nối mạch:** **Quyết định (decision / 결정) provenance** nối từ **Quyết định (decision / 결정) log và giả định (assumption / 가정) expiration** sang **Thông tin (information / 정보) radiator và dashboard**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quyết định (decision / 결정) provenance

Provenance nối quyết định (decision / 결정) với bằng chứng (evidence / 증거) và authority. Nếu một phạm vi (scope / 범위) exception được approve, cần biết yêu cầu (request / 요청) nào, phân tích (analysis / 분석) nào, ai approve và điều kiện nào đi kèm.

Provenance khác mere lịch sử (history / 이력). lịch sử (history / 이력) nói sự kiện (event / 이벤트) đã xảy ra; provenance giải thích chuỗi (chain / 사슬) tạo ra trạng thái (state / 상태) hiện tại.

Trong sự cố (incident / 인시던트) hoặc kiểm tra (audit / 감사), provenance giúp phân biệt unauthorized drift với tường minh (explicit / 명시적) accepted exception.

> **Nối mạch:** **Thông tin (information / 정보) radiator và dashboard** nối từ **Quyết định (decision / 결정) provenance** sang **Thông tin (information / 정보) compression luôn làm mất detail**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thông tin (information / 정보) radiator và dashboard

Adaptive nhóm (team / 팀) thường dùng visual board, burnup/burndown, cumulative luồng (flow / 흐름) hoặc bản phát hành (release / 릴리스) forecast như thông tin (information / 정보) radiator. Predictive dự án (project / 프로젝트) dùng milestone/Gantt/EVM/dashboard. công cụ (tool / 도구) khác nhau nhưng bài toán (problem / 문제) giống nhau: làm trạng thái (state / 상태) và deviation visible đủ nhanh.

Burnup cho thấy completed phạm vi (scope / 범위) và total phạm vi (scope / 범위) nên nhìn được phạm vi (scope / 범위) thay đổi (change / 변경) tốt hơn burndown chỉ hiển thị remaining công việc (work / 작업). Cumulative luồng (flow / 흐름) cho thấy WIP theo trạng thái (state / 상태) và bottleneck. chỉ số (metric / 지표) nên chọn theo question, không theo template.

Dashboard tốt không thay nguồn (source / 소스) hệ thống (system / 시스템). Nó là projection của nguồn (source / 소스) dữ liệu (data / 데이터) cho một quyết định (decision / 결정) audience. Nếu dashboard có số nhưng không thể truy ngược dữ liệu (data / 데이터) nguồn (source / 소스), trust giảm khi có dispute.

> **Nối mạch:** **Thông tin (information / 정보) compression luôn làm mất detail** nối từ **Thông tin (information / 정보) radiator và dashboard** sang **Dashboard là view, không phải reality**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thông tin (information / 정보) compression luôn làm mất detail

Status report nén hàng nghìn sự kiện (event / 이벤트) thành vài tín hiệu (signal / 신호). Compression là cần thiết, nhưng người thiết kế report phải biết detail nào bị mất.

Một green milestone có thể che trọng yếu (critical / 중요) rủi ro (risk / 위험) nếu chỉ nhìn completion. Vì vậy report cần surface exception và confidence, không chỉ aggregate average.

Compression cũng tạo aggregation độ lệch (bias / 편향). Average defect tỷ lệ (rate / 비율) 2% có thể che một segment high-risk 20%. Report designer cần biết khi nào aggregate cần drill-down.

> **Nối mạch:** **Dashboard là view, không phải reality** nối từ **Thông tin (information / 정보) compression luôn làm mất detail** sang **Thông tin (information / 정보) độ trễ (latency / 지연 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dashboard là view, không phải reality

Dashboard thường dùng cutoff thời gian (time / 시간) và transform. Một dashboard 09:00 có thể stale sau sự cố (incident / 인시던트) 10:00. “Green” nghĩa green theo dữ liệu (data / 데이터) captured và quy tắc (rule / 규칙) hiện tại, không phải metaphysical truth.

Trọng yếu (critical / 중요) quyết định (decision / 결정) nên kiểm tra freshness và underlying bằng chứng (evidence / 증거), đặc biệt khi trạng thái (state / 상태) đang thay đổi nhanh.

> **Nối mạch:** **Thông tin (information / 정보) độ trễ (latency / 지연 시간)** nối từ **Dashboard là view, không phải reality** sang **Communication channels formula và giới hạn của nó**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thông tin (information / 정보) độ trễ (latency / 지연 시간)

Thông tin (information / 정보) độ trễ (latency / 지연 시간) là thời gian từ sự kiện (event / 이벤트) xảy ra tới khi người có authority nhìn thấy tín hiệu (signal / 신호) usable. độ trễ (latency / 지연 시간) dài làm điều khiển (control / 제어) phản ứng muộn.

Ví dụ defect môi trường vận hành (production / 운영 환경) xuất hiện hôm nay nhưng chất lượng (quality / 품질) dashboard cập nhật (update / 업데이트) weekly; management có thể tiếp tục rollout sáu ngày dựa trên stale trạng thái (state / 상태).

Automation có thể giảm độ trễ (latency / 지연 시간), nhưng only if alert threshold và quyền sở hữu (ownership / 소유권) rõ. Alert không ai đọc chỉ chuyển độ trễ (latency / 지연 시간) từ dữ liệu (data / 데이터) tầng (layer / 계층) sang human hàng đợi (queue / 큐).

> **Nối mạch:** **Thông tin (information / 정보) độ trễ (latency / 지연 시간)** đặt tiêu chí; **Communication channels formula và giới hạn của nó** dùng nó để kiểm tra ranh giới, rồi **Single nguồn chuẩn (source of truth / 정본) không có nghĩa một công cụ (tool / 도구) duy nhất** mở rộng cơ chế.

## Communication channels formula và giới hạn của nó

Với `n` người nếu mọi cặp có thể giao tiếp trực tiếp, số channel lý thuyết là:

```text
channels = n(n - 1) / 2
```

5 người tạo 10 channel; 10 người tạo 45. Formula giải thích vì sao coordination độ phức tạp (complexity / 복잡도) tăng nhanh khi nhóm (team / 팀) lớn. Nhưng nó không có nghĩa mọi channel hoạt động đều như nhau hoặc một dự án (project / 프로젝트) 10 người “phức tạp 4.5 lần” dự án (project / 프로젝트) 5 người. cấu trúc (structure / 구조), role và communication thiết kế (design / 설계) làm giảm tương tác (interaction / 상호작용) cần thiết.

Sản phẩm tạo ra (artifact / 산출물) và giao thức (protocol / 프로토콜) chính là cách giảm coordination tải (load / 로드). dùng chung (shared / 공유) Đặc tả API (API contract / API 계약), kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) hoặc acceptance criterion có thể thay hàng chục conversation lặp lại.

> **Nối mạch:** **Communication channels formula và giới hạn của nó** đặt tiêu chí; **Single nguồn chuẩn (source of truth / 정본) không có nghĩa một công cụ (tool / 도구) duy nhất** dùng nó để kiểm tra ranh giới, rồi **Versioning và cấu hình (configuration / 구성) điều khiển (control / 제어)** mở rộng cơ chế.

## Single nguồn chuẩn (source of truth / 정본) không có nghĩa một công cụ (tool / 도구) duy nhất

Một dự án (project / 프로젝트) lớn có thể dùng Jira cho công việc (work / 작업), Git cho mã (code / 코드), CI cho kiểm thử (test / 테스트) bằng chứng (evidence / 증거) và ERP cho actual chi phí (cost / 비용). Không cần ép mọi thông tin (information / 정보) vào một công cụ (tool / 도구).

“Single nguồn chuẩn (source of truth / 정본)” nên hiểu là mỗi loại fact có authoritative nguồn (source / 소스) rõ. Dashboard có thể aggregate nhiều nguồn (source / 소스) nhưng không nên tạo competing truth.

Nguồn (source / 소스) quyền sở hữu (ownership / 소유권) cũng cần conflict-resolution quy tắc (rule / 규칙). Nếu ERP và procurement công cụ (tool / 도구) khác nhau về committed chi phí (cost / 비용), organization phải biết hệ thống (system / 시스템) nào authoritative cho từng trường dữ liệu (field / 필드) hoặc cách reconcile.

> **Nối mạch:** **Single nguồn chuẩn (source of truth / 정본) không có nghĩa một công cụ (tool / 도구) duy nhất** đặt vấn đề; **Versioning và cấu hình (configuration / 구성) điều khiển (control / 제어)** kiểm tra bằng chứng, rồi **Sản phẩm tạo ra (artifact / 산출물) quyền sở hữu (ownership / 소유권) và freshness** mở rộng hệ quả.

## Versioning và cấu hình (configuration / 구성) điều khiển (control / 제어)

Sản phẩm tạo ra (artifact / 산출물) quan trọng cần biết phiên bản (version / 버전) nào đang có hiệu lực. Điều này đặc biệt quan trọng với yêu cầu (requirement / 요구사항), đặc tả hợp đồng (contract / 계약), thiết kế (design / 설계), baseline và kiểm thử (test / 테스트) bằng chứng (evidence / 증거).

Nếu nhóm (team / 팀) rà soát (review / 검토) yêu cầu (requirement / 요구사항) v3 nhưng vendor implement v2, communication frequency cao cũng không cứu được cấu hình (configuration / 구성) thất bại (failure / 실패). cấu hình (configuration / 구성) management tạo định danh (identity / 식별자) và phiên bản (version / 버전) điều khiển (control / 제어) cho sản phẩm tạo ra (artifact / 산출물)/deliverable để mọi party làm việc trên cùng trạng thái (state / 상태).

Phiên bản (version / 버전) string chỉ có giá trị nếu ánh xạ (mapping / 매핑) tới effective cấu hình (configuration / 구성). “v3-final-final2” không phải cấu hình (configuration / 구성) management.

> **Nối mạch:** Versioning và configuration control xác định bản nào có hiệu lực; **Artifact ownership và freshness** gắn bản đó với owner trong README. **Freshness SLO cho information** kiểm tra khi nào dữ liệu đã quá cũ.

## Sản phẩm tạo ra (artifact / 산출물) quyền sở hữu (ownership / 소유권) và freshness

Sản phẩm tạo ra (artifact / 산출물) stale nguy hiểm hơn sản phẩm tạo ra (artifact / 산출물) thiếu vì nó tạo confidence giả. Mỗi trọng yếu (critical / 중요) sản phẩm tạo ra (artifact / 산출물) cần nguồn chuẩn (source of truth / 정본), đơn vị sở hữu (owner / 오너), cập nhật (update / 업데이트) trigger và archive/phiên bản (version / 버전) chính sách (policy / 정책). Nếu rủi ro (risk / 위험) register chỉ cập nhật trước kiểm tra (audit / 감사), nó không phải risk-control instrument.

Automation có thể giảm maintenance: CI tạo kiểm thử (test / 테스트) bằng chứng (evidence / 증거), issue tracker sinh status, financial hệ thống (system / 시스템) cập nhật actual chi phí (cost / 비용). Nhưng automation chỉ tốt nếu ngữ nghĩa (semantic / 의미적) definition đúng.

Freshness yêu cầu (requirement / 요구사항) nên phụ thuộc quyết định (decision / 결정) cadence. Daily luồng (flow / 흐름) board cần cập nhật gần real thời gian (time / 시간); benefits report có thể monthly/quarterly. Không phải sản phẩm tạo ra (artifact / 산출물) nào cũng cần cùng cập nhật (update / 업데이트) frequency.

> **Nối mạch:** **Freshness SLO cho thông tin (information / 정보)** nối từ **Sản phẩm tạo ra (artifact / 산출물) quyền sở hữu (ownership / 소유권) và freshness** sang **Automation ranh giới (boundary / 경계) và human kiểm tra hợp lệ (validation / 검증)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Freshness SLO cho thông tin (information / 정보)

Có thể nghĩ freshness như dịch vụ (service / 서비스) mức (level / 수준) cho thông tin (information / 정보). trọng yếu (critical / 중요) sự cố (incident / 인시던트) status có thể cần dưới 15 phút; schedule forecast weekly; benefit realization monthly.

Nếu quyết định (decision / 결정) cadence nhanh hơn freshness, quản trị (governance / 거버넌스) đang lái bằng rear-view mirror. Nếu cập nhật (update / 업데이트) cadence quá cao so với quyết định (decision / 결정) need, nhóm (team / 팀) tạo reporting waste.

Tailoring sản phẩm tạo ra (artifact / 산출물) cadence là matching thông tin (information / 정보) half-life với quyết định (decision / 결정) cadence.

> **Nối mạch:** **Freshness SLO cho thông tin (information / 정보)** đặt tiêu chí; **Automation ranh giới (boundary / 경계) và human kiểm tra hợp lệ (validation / 검증)** dùng nó để kiểm tra ranh giới, rồi **Kiểm soát truy cập (access control / 접근 제어) và thông tin (information / 정보) bảo mật (security / 보안)** mở rộng cơ chế.

## Automation ranh giới (boundary / 경계) và human kiểm tra hợp lệ (validation / 검증)

Automation tốt cho deterministic transform: aggregate actual chi phí (cost / 비용), link build-test bằng chứng (evidence / 증거), calculate chỉ số (metric / 지표). Nhưng ngữ nghĩa (semantic / 의미적) exception cần human judgment.

Ví dụ công cụ (tool / 도구) có thể auto-close rủi ro (risk / 위험) khi due date qua là dangerous; due date không chứng minh rủi ro (risk / 위험) retired. Automation nên reduce clerical công việc (work / 작업) mà không encode false nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙).

Automated sản phẩm tạo ra (artifact / 산출물) cần observable thất bại (failure / 실패). Nếu tích hợp (integration / 통합) từ ERP sang dashboard thất bại (fail / 실패) silently, report có thể stale mà người dùng không biết.

> **Nối mạch:** **Automation ranh giới (boundary / 경계) và human kiểm tra hợp lệ (validation / 검증)** đặt tiêu chí; **Kiểm soát truy cập (access control / 접근 제어) và thông tin (information / 정보) bảo mật (security / 보안)** dùng nó để kiểm tra ranh giới, rồi **Kiến thức (knowledge / 지식) transfer: sản phẩm tạo ra (artifact / 산출물) không thay conversation hoàn toàn** mở rộng cơ chế.

## Kiểm soát truy cập (access control / 접근 제어) và thông tin (information / 정보) bảo mật (security / 보안)

Không phải mọi sản phẩm tạo ra (artifact / 산출물) nên mở cho toàn dự án (project / 프로젝트). Procurement bid, personal dữ liệu (data / 데이터), legal advice hoặc bảo mật (security / 보안) finding có thể cần truy cập (access / 접근) ranh giới (boundary / 경계).

Transparency không có nghĩa phá confidentiality. dự án (project / 프로젝트) thông tin (information / 정보) kiến trúc (architecture / 아키텍처) phải cân bằng need-to-know, auditability và collaboration.

Truy cập (access / 접근) mô hình (model / 모델) cũng ảnh hưởng continuity. Nếu trọng yếu (critical / 중요) sản phẩm tạo ra (artifact / 산출물) nằm trong private account của một contractor, offboarding có thể làm dự án (project / 프로젝트) mất bộ nhớ (memory / 메모리). quyền sở hữu (ownership / 소유권) nên thuộc organizational hệ thống (system / 시스템) khi appropriate.

> **Nối mạch:** **Kiến thức (knowledge / 지식) transfer: sản phẩm tạo ra (artifact / 산출물) không thay conversation hoàn toàn** nối từ **Kiểm soát truy cập (access control / 접근 제어) và thông tin (information / 정보) bảo mật (security / 보안)** sang **Sản phẩm tạo ra (artifact / 산출물) minimization heuristic**, vì cơ chế trước tạo đầu vào cho bước sau.

## Kiến thức (knowledge / 지식) transfer: sản phẩm tạo ra (artifact / 산출물) không thay conversation hoàn toàn

Tacit kiến thức (knowledge / 지식) khó capture hoàn toàn bằng document. Handover tốt thường kết hợp sản phẩm tạo ra (artifact / 산출물) với walkthrough, shadowing hoặc joint thao tác (operation / 연산) period.

Runbook có thể ghi step, nhưng operator vẫn cần hiểu thất bại (failure / 실패) tín hiệu (signal / 신호) và escalation ngữ cảnh (context / 맥락). Vì vậy kiến thức (knowledge / 지식) transfer là combination của tường minh (explicit / 명시적) kiến thức (knowledge / 지식) và experience transfer.

Teach-back hoặc simulation giúp verify kiến thức (knowledge / 지식) transfer thay vì chỉ ghi “huấn luyện (training / 학습) completed”.

> **Nối mạch:** **Sản phẩm tạo ra (artifact / 산출물) minimization heuristic** nối từ **Kiến thức (knowledge / 지식) transfer: sản phẩm tạo ra (artifact / 산출물) không thay conversation hoàn toàn** sang **Sản phẩm tạo ra (artifact / 산출물) anti-patterns**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sản phẩm tạo ra (artifact / 산출물) minimization heuristic

Mỗi sản phẩm tạo ra (artifact / 산출물) có carrying chi phí (cost / 비용): create, cập nhật (update / 업데이트), rà soát (review / 검토), reconcile, archive. Vì vậy “có thêm document cho chắc” không luôn tốt.

Trước khi tạo sản phẩm tạo ra (artifact / 산출물) mới, hỏi: thông tin (information / 정보) này đã có authoritative nguồn (source / 소스) chưa, bên tiêu thụ (consumer / 소비자)/quyết định (decision / 결정) nào cần view khác, rủi ro (risk / 위험) của không ghi là gì, và automation/view có đủ thay document mới không.

Nếu hai sản phẩm tạo ra (artifact / 산출물) luôn phải cập nhật (update / 업데이트) cùng nhau và không có audience/điều khiển (control / 제어) khác nhau, chúng có thể đang duplicate truth.

> **Nối mạch:** **Sản phẩm tạo ra (artifact / 산출물) anti-patterns** nối từ **Sản phẩm tạo ra (artifact / 산출물) minimization heuristic** sang **Ví dụ lập luận (reasoning / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sản phẩm tạo ra (artifact / 산출물) anti-patterns

Document theater là tạo sản phẩm tạo ra (artifact / 산출물) để pass kiểm tra (audit / 감사) nhưng không dùng trong công việc (work / 작업). Duplicate truth xảy ra khi nhiều spreadsheet chứa cùng fact nhưng cập nhật (update / 업데이트) khác nhau. Zombie document là tệp (file / 파일) vẫn được link nhưng không còn đơn vị sở hữu (owner / 오너). Dashboard theater là chỉ số (metric / 지표) đẹp không nối quyết định (decision / 결정). Traceability theater là RTM đầy đủ về hình thức nhưng link không được verify.

Một anti-pattern khác là over-documentation: thông tin (information / 정보) được ghi ở quá nhiều nơi đến mức cập nhật (update / 업데이트) chi phí (cost / 비용) cao hơn giá trị (value / 값) và freshness giảm.

Ngữ nghĩa (semantic / 의미적) drift làm cùng chỉ số (metric / 지표) đổi meaning nhưng report không nói. Lineage break khiến number không dấu vết (trace / 추적) về nguồn (source / 소스). Gate theater approve dù bằng chứng (evidence / 증거) thiếu. lịch sử (history / 이력) overwrite xóa trạng thái (state / 상태) cũ. Automation blindness tin chuỗi xử lý (pipeline / 파이프라인) dù tích hợp (integration / 통합) đã thất bại (fail / 실패).

> **Nối mạch:** **Sản phẩm tạo ra (artifact / 산출물) anti-patterns** nêu quy tắc; **Ví dụ lập luận (reasoning / 추론)** thử quy tắc trong tình huống, rồi **Thất bại (failure / 실패) modes theo thông tin (information / 정보) hệ thống (system / 시스템)** mở rộng hệ quả.

## Ví dụ lập luận (reasoning / 추론)

Một thay đổi (change / 변경) yêu cầu (request / 요청) thêm biometric xác minh (verification / 확인) được sponsor nói miệng trong meeting. nhóm (team / 팀) dev bắt đầu làm, procurement chưa biết vendor license thay đổi, privacy rà soát (review / 검토) chưa được cập nhật và schedule vẫn dùng baseline cũ. bài toán (problem / 문제) không chỉ là “communication kém”. dự án (project / 프로젝트) đã thiếu sản phẩm tạo ra (artifact / 산출물) chuyển tiếp (transition / 전이) từ yêu cầu (request / 요청) → impact phân tích (analysis / 분석) → approval → baseline/backlog cập nhật (update / 업데이트) → compliance bằng chứng (evidence / 증거).

Một luồng (flow / 흐름) tốt làm quyết định (decision / 결정) visible và traceable, nhờ đó mỗi lĩnh vực (domain / 도메인) nhận đúng thông tin (information / 정보) tại đúng thời điểm.

Một scenario khác: steering dashboard báo EAC 1.1 tỷ nhưng finance ERP chỉ có actual 600 triệu. Procurement công cụ (tool / 도구) cho biết 400 triệu PO đã committed; PM forecast thêm 200 triệu remaining. Nếu dashboard không có lineage, stakeholder có thể tranh luận vì “số không khớp”. Khi ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약) rõ, ta hiểu EAC = actual/commitment/remaining forecast theo quy tắc (rule / 규칙), còn ERP actual chỉ là một thành phần (component / 컴포넌트).

> **Nối mạch:** **Ví dụ lập luận (reasoning / 추론)** nêu quy tắc; **Thất bại (failure / 실패) modes theo thông tin (information / 정보) hệ thống (system / 시스템)** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Thất bại (failure / 실패) modes theo thông tin (information / 정보) hệ thống (system / 시스템)

Thất bại (failure / 실패) ở capture: sự kiện (event / 이벤트) không được ghi. thất bại (failure / 실패) ở ngữ nghĩa (semantics / 의미론): trường dữ liệu (field / 필드) có meaning khác nhau. thất bại (failure / 실패) ở propagation: nguồn (source / 소스) đổi nhưng downstream view không đổi. thất bại (failure / 실패) ở authority: người không có quyền sửa baseline. thất bại (failure / 실패) ở lineage: report không dấu vết (trace / 추적) về bằng chứng (evidence / 증거). thất bại (failure / 실패) ở freshness: dữ liệu (data / 데이터) đúng nhưng quá cũ. thất bại (failure / 실패) ở truy cập (access / 접근): đúng người không xem được hoặc sai người xem được. thất bại (failure / 실패) ở retention: lịch sử (history / 이력) bị xóa trước khi kiểm tra (audit / 감사)/học tập (learning / 학습) cần.

Nhìn sản phẩm tạo ra (artifact / 산출물) theo dạng thất bại (failure mode / 실패 모드) giúp dự án (project / 프로젝트) manager thiết kế điều khiển (control / 제어) thực dụng hơn memorizing template.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp kết quả từ **Thất bại (failure / 실패) modes theo thông tin (information / 정보) hệ thống (system / 시스템)** để khép mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> sản phẩm tạo ra (artifact / 산출물) là bên ngoài (external / 외부) bộ nhớ (memory / 메모리) và bằng chứng (evidence / 증거) kiến trúc (architecture / 아키텍처) của dự án (project / 프로젝트). Mục tiêu không phải tạo nhiều document mà là giữ được lineage từ nguồn (source / 소스) → trạng thái (state / 상태) → quyết định (decision / 결정) → commitment → bằng chứng (evidence / 증거), với ngữ nghĩa (semantics / 의미론), phiên bản (version / 버전), freshness và authority đủ rõ để dự án (project / 프로젝트) có một reality có thể kiểm chứng.

Tiếp theo nên đọc [Quantitative reasoning](./15_quantitative_reasoning_worked_examples.md) để nối dữ liệu (data / 데이터)/sản phẩm tạo ra (artifact / 산출물) với các phép tính PMP, hoặc [Case studies](./16_end_to_end_case_studies.md) để thấy nhiều sản phẩm tạo ra (artifact / 산출물) tương tác trong một dự án (project / 프로젝트).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
