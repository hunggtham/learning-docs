# 04 — tích hợp (integration / 통합), phạm vi (scope / 범위), requirements và thay đổi (change / 변경)

> **Mạch đọc:** Đặt **04 — tích hợp (integration / 통합), phạm vi (scope / 범위), requirements và thay đổi (change / 변경)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **tích hợp (integration / 통합) là quản lý tương tác (interaction / 상호작용) giữa các quyết định** sang **tích hợp (integration / 통합) là operating hệ thống (system / 시스템) của dự án (project / 프로젝트)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## Tích hợp (integration / 통합) là quản lý tương tác (interaction / 상호작용) giữa các quyết định

Tích hợp dự án (project integration management / 프로젝트 통합 관리) không đơn giản là gom nhiều plan vào một tệp (file / 파일). phạm vi (scope / 범위) thay đổi có thể làm schedule, chi phí (cost / 비용), procurement, rủi ro (risk / 위험) và stakeholder expectation thay đổi cùng lúc. tích hợp (integration / 통합) là năng lực nhìn dự án (project / 프로젝트) như một hệ thống (system / 시스템) và giữ các quyết định (decision / 결정) nhất quán với nhau.

Integrated dự án (project / 프로젝트) management plan vì vậy là một coherent quyết định (decision / 결정) mô hình (model / 모델): delivery approach, baselines khi cần, quản trị (governance / 거버넌스), subsidiary plans, thresholds và cách kiểm soát thay đổi (change / 변경). Giá trị của nó nằm ở consistency chứ không ở độ dày.

Tích hợp (integration / 통합) đặc biệt quan trọng ở ranh giới (boundary / 경계). Một cục bộ (local / 로컬) quyết định (decision / 결정) có thể tối ưu subsystem nhưng làm toàn dự án (project / 프로젝트) tệ hơn. nhóm (team / 팀) technical có thể chọn solution tốt nhất về hiệu năng (performance / 성능) nhưng phá vendor đặc tả hợp đồng (contract / 계약); nghiệp vụ (business / 비즈니스) có thể thêm tính năng (feature / 기능) high-value nhưng làm compliance rà soát (review / 검토) trễ. dự án (project / 프로젝트) manager phải nhìn tác động (effect / 효과) lan truyền trước khi quyết định (decision / 결정) được lần ghi nhận (commit / 커밋).

## Tích hợp (integration / 통합) là operating hệ thống (system / 시스템) của dự án (project / 프로젝트)

Một cách hiểu sâu hơn là xem tích hợp (integration / 통합) như operating hệ thống (system / 시스템) của dự án (project / 프로젝트). Mỗi lĩnh vực (domain / 도메인) tạo cục bộ (local / 로컬) trạng thái (state / 상태): phạm vi (scope / 범위) có yêu cầu (requirement / 요구사항) và baseline; schedule có phụ thuộc (dependency / 의존성) và forecast; finance có ngân sách (budget / 예산) và actual; rủi ro (risk / 위험) có exposure; procurement có obligation; stakeholder có expectation. Nếu các cục bộ (local / 로컬) trạng thái (state / 상태) này không được đồng bộ, dự án (project / 프로젝트) có nhiều “sự thật” cùng tồn tại.

Tích hợp (integration / 통합) tạo giao thức (protocol / 프로토콜) để một thay đổi ở một lĩnh vực (domain / 도메인) được nhận diện, phân tích, quyết định và phản ánh vào các lĩnh vực (domain / 도메인) liên quan. Nếu vendor delivery date đổi nhưng schedule, rủi ro (risk / 위험) register, cash forecast và stakeholder commitment vẫn giữ trạng thái (state / 상태) cũ, dự án (project / 프로젝트) đã mất coherence dù từng sản phẩm tạo ra (artifact / 산출물) riêng lẻ vẫn nhìn hợp lệ.

Vì vậy maturity của tích hợp (integration / 통합) không nằm ở số meeting coordination mà ở tốc độ và độ chính xác của trạng thái (state / 상태) propagation.

## Tích hợp (integration / 통합) là quản lý ràng buộc (constraint / 제약조건) coupling

Phạm vi (scope / 범위), schedule, chi phí (cost / 비용), chất lượng (quality / 품질) và rủi ro (risk / 위험) không phải các thanh trượt độc lập. Chúng coupling với nhau. Rút schedule có thể làm chi phí (cost / 비용) hoặc rủi ro (risk / 위험) tăng. Giảm chi phí (cost / 비용) có thể giảm redundancy và chất lượng (quality / 품질) margin. Tăng phạm vi (scope / 범위) có thể làm tài nguyên (resource / 자원) contention xuất hiện.

Vì vậy câu hỏi đúng không phải “thay đổi (change / 변경) này ảnh hưởng schedule bao nhiêu?” mà là “thay đổi (change / 변경) này làm mục tiêu (objective / 목표) và ràng buộc (constraint / 제약조건) hệ thống (system / 시스템) thay đổi ra sao?”. Impact phân tích (analysis / 분석) tốt luôn multidimensional.

Coupling còn có thể phi tuyến. Thêm 5% phạm vi (scope / 범위) không nhất thiết tăng 5% duration. Nếu phần thêm chạm một regulatory rà soát (review / 검토) hoặc vendor giao diện (interface / 인터페이스), nó có thể mở một phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬) mới và kéo finish date nhiều tuần. dự án (project / 프로젝트) manager cần tìm discontinuity như gate, dùng chung (shared / 공유) tài nguyên (resource / 자원), license threshold hoặc kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계), không chỉ dùng tỷ lệ tuyến tính.

## Dự án (project / 프로젝트) charter và integrated direction

Charter thiết lập dự án (project / 프로젝트) purpose, high-level mục tiêu (objective / 목표), sponsor, authority và ranh giới (boundary / 경계). Nó giúp tránh dự án (project / 프로젝트) bắt đầu thực thi (execution / 실행) khi chưa có agreement tối thiểu về vì sao investment tồn tại.

Dự án (project / 프로젝트) management plan phát triển direction đó thành operating mô hình (model / 모델). Charter không cần mô tả cách quản lý mọi lĩnh vực (domain / 도메인); plan không nên thay nghiệp vụ (business / 비즈니스) justification. Hai sản phẩm tạo ra (artifact / 산출물) ở hai lớp trừu tượng (abstraction / 추상화) mức (level / 수준) khác nhau.

Charter cũng tạo anchor khi dự án (project / 프로젝트) bị kéo theo cục bộ (local / 로컬) pressure. Nếu một yêu cầu (request / 요청) mới hấp dẫn nhưng không còn phục vụ mục tiêu (objective / 목표) được authorize, nhóm (team / 팀) cần đưa nó trở lại business-case/thay đổi (change / 변경) lập luận (reasoning / 추론) thay vì mặc định hấp thụ.

## Phạm vi (scope / 범위): ranh giới (boundary / 경계) của commitment

Phạm vi (scope / 범위) mô tả những gì dự án (project / 프로젝트)/sản phẩm (product / 제품) cam kết tạo ra và ranh giới (boundary / 경계) của công việc cần thiết. sản phẩm (product / 제품) phạm vi (scope / 범위) nói về tính năng (feature / 기능)/năng lực (capability / 역량); dự án (project / 프로젝트) phạm vi (scope / 범위) nói về công việc (work / 작업) để tạo ra kết quả (result / 결과) đó.

Phạm vi (scope / 범위) cần đủ rõ để stakeholder có thể đồng ý và nhóm (team / 팀) có thể decompose. Nhưng “rõ” không nhất thiết nghĩa mọi chi tiết cố định từ đầu. Trong adaptive dự án (project / 프로젝트), sản phẩm (product / 제품) backlog là một phạm vi (scope / 범위) mô hình (model / 모델) động; trong predictive dự án (project / 프로젝트), phạm vi (scope / 범위) baseline thường ổn định hơn và thay đổi (change / 변경) được formalized.

Phạm vi (scope / 범위) ranh giới (boundary / 경계) còn cần nói rõ exclusion. “Không bao gồm di chuyển (migration / 마이그레이션) historical dữ liệu (data / 데이터) trước 2020” có thể quan trọng ngang “bao gồm customer profile di chuyển (migration / 마이그레이션)”. Exclusion làm hidden giả định (assumption / 가정) visible.

Một ranh giới (boundary / 경계) tốt còn nêu giao diện (interface / 인터페이스). Nếu dự án (project / 프로젝트) tạo API nhưng downstream di chuyển (migration / 마이그레이션) do chương trình khác làm, giao diện (interface / 인터페이스) acceptance và handoff điều kiện (condition / 조건) phải rõ; nếu không, mỗi bên có thể hoàn thành “phạm vi (scope / 범위) của mình” nhưng hệ thống (system / 시스템) kết quả (outcome / 결과) vẫn thiếu.

## Yêu cầu (requirement / 요구사항) không phải solution statement

Yêu cầu (requirement / 요구사항) mô tả need, điều kiện (condition / 조건) hoặc năng lực (capability / 역량) cần đạt. Solution thiết kế (design / 설계) mô tả cách đạt nó. Nhầm hai lớp làm solution không gian (space / 공간) bị khóa sớm.

Ví dụ “người dùng (user / 사용자) phải đăng nhập bằng OTP SMS” nghe như yêu cầu (requirement / 요구사항) nhưng có thể thực chất need là “xác thực possession factor”. Nếu regulation không bắt SMS, passkey hoặc app-based OTP có thể tốt hơn. Tách need khỏi hiện thực (implementation / 구현) giúp option phân tích (analysis / 분석).

Một kỹ thuật lập luận (reasoning / 추론) hữu ích là hỏi nhiều lần “tại sao cần điều này?”. Nếu answer quay về nghiệp vụ (business / 비즈니스) need, rủi ro (risk / 위험)/điều khiển (control / 제어) mục tiêu (objective / 목표) hoặc stakeholder kết quả (outcome / 결과), yêu cầu (requirement / 요구사항) đang tiến gần bài toán (problem / 문제) tầng (layer / 계층). Nếu answer chỉ lặp hiện thực (implementation / 구현), có thể solution đã bị masquerade thành yêu cầu (requirement / 요구사항).

## Yêu cầu (requirement / 요구사항) xung đột (conflict / 충돌) không thể giải bằng cách giữ tất cả

Stakeholder có thể đưa yêu cầu (requirement / 요구사항) mâu thuẫn. bảo mật (security / 보안) muốn session hết thời gian chờ (timeout / 타임아웃) ngắn; người dùng (user / 사용자) experience muốn không bị logout. Finance muốn giảm vendor chi phí (cost / 비용); operations muốn premium hỗ trợ (support / 지원). Ghi cả hai vào backlog không giải xung đột (conflict / 충돌).

Dự án (project / 프로젝트) cần tường minh (explicit / 명시적) priority và sự đánh đổi (trade-off / 트레이드오프) authority. xung đột (conflict / 충돌) nên được đưa về mục tiêu (objective / 목표), rủi ro (risk / 위험) appetite, compliance và giá trị (value / 값). yêu cầu (requirement / 요구사항) kỹ thuật (engineering / 엔지니어링) trưởng thành không chỉ capture nhu cầu mà còn resolve inconsistency trước khi nó trở thành thiết kế (design / 설계) rework.

Nếu xung đột (conflict / 충돌) được trì hoãn quá lâu, nhóm (team / 팀) thường tự quyết ngầm ở hiện thực (implementation / 구현). Khi đó một technical quyết định (decision / 결정) vô tình trở thành nghiệp vụ (business / 비즈니스) quyết định (decision / 결정) mà không có đúng authority.

## Giả định (assumption / 가정) là phụ thuộc (dependency / 의존성) vô hình

Nhiều plan nhìn nhất quán chỉ vì một giả định (assumption / 가정) chưa bị kiểm tra: “vendor sẽ hỗ trợ API này”, “regulator chấp nhận điều khiển (control / 제어) tương đương”, “người dùng (user / 사용자) có smartphone mới”, “dữ liệu (data / 데이터) chất lượng (quality / 품질) đủ tốt” hoặc “operations có sức chứa (capacity / 용량) nhận thêm tải công việc (workload / 워크로드)”. giả định (assumption / 가정) chưa được chứng minh nhưng thường được dùng như fact trong schedule, ngân sách (budget / 예산) và thiết kế (design / 설계).

Vì vậy giả định (assumption / 가정) material nên có đơn vị sở hữu (owner / 오너), bằng chứng (evidence / 증거) plan, expiry/kiểm tra hợp lệ (validation / 검증) date và consequence nếu sai. Khi giả định (assumption / 가정) đổi trạng thái (state / 상태), tích hợp (integration / 통합) cơ chế (mechanism / 메커니즘) phải biết sản phẩm tạo ra (artifact / 산출물)/quyết định (decision / 결정) nào phụ thuộc nó. Đây là **giả định (assumption / 가정) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)**.

Một giả định (assumption / 가정) có blast radius lớn đáng được validate sớm ngay cả khi xác suất (probability / 확률) sai không cao. Nếu toàn bộ kiến trúc (architecture / 아키텍처) và đặc tả hợp đồng (contract / 계약) phụ thuộc một interpretation pháp lý, giá trị (value / 값) of thông tin (information / 정보) của việc xác minh sớm có thể rất lớn.

Giả định (assumption / 가정) debt xuất hiện khi dự án (project / 프로젝트) tiếp tục bản dựng (build / 빌드) nhiều tầng (layer / 계층) trên giả định (assumption / 가정) chưa kiểm chứng. Mỗi tầng (layer / 계층) mới làm reversal chi phí (cost / 비용) tăng. Đây là lý do discovery, spike, pilot hoặc early bên ngoài (external / 외부) rà soát (review / 검토) có thể là tích hợp (integration / 통합) điều khiển (control / 제어) chứ không chỉ technical activity.

## Yêu cầu (requirement / 요구사항) và acceptance

Yêu cầu (requirement / 요구사항) là need/điều kiện (condition / 조건)/năng lực (capability / 역량) cần được đáp ứng. Một yêu cầu (requirement / 요구사항) chưa testable thường còn ambiguity. Acceptance criteria biến intent thành điều kiện kiểm chứng.

Trong software, một câu “hệ thống phải nhanh” không đủ. “95% API yêu cầu (request / 요청) dưới 300 ms ở tải công việc (workload / 워크로드) X” tạo bằng chứng (evidence / 증거). Chiều kỹ thuật sâu hơn đã có ở chuẩn gốc (canonical / 정본) [Requirements Engineering](../computer_science/09_software_engineering/00_requirements_specification_and_engineering_process.md); chapter này tập trung vào tác động cấp dự án (project / 프로젝트).

Acceptance criterion tốt phải đủ cụ thể để hai bên có cùng answer khi kiểm tra. Nếu acceptance phụ thuộc cảm nhận chủ quan nhưng không có user-test giao thức (protocol / 프로토콜), dispute rất dễ xảy ra ở cuối.

Acceptance criteria cũng cần phản ánh operating ngữ cảnh (context / 맥락). hiệu năng (performance / 성능) kiểm thử (test / 테스트) ở 100 người dùng (user / 사용자) không chứng minh yêu cầu (requirement / 요구사항) nếu môi trường vận hành (production / 운영 환경) expected 10.000 concurrent người dùng (user / 사용자). bằng chứng (evidence / 증거) chỉ mạnh khi kiểm thử (test / 테스트) điều kiện (condition / 조건) tương thích với claim cần chứng minh.

## Xác minh (verification / 확인) và kiểm tra hợp lệ (validation / 검증) là hai câu hỏi khác nhau

Xác minh (verification / 확인) hỏi deliverable được xây đúng specification chưa. kiểm tra hợp lệ (validation / 검증) hỏi deliverable có giải đúng need trong ngữ cảnh (context / 맥락) sử dụng không. Một hệ thống (system / 시스템) có thể pass toàn bộ kiểm thử (test / 테스트) kỹ thuật nhưng người dùng (user / 사용자) vẫn không thể hoàn thành nghiệp vụ (business / 비즈니스) luồng (flow / 흐름).

Ở dự án (project / 프로젝트) mức (level / 수준), distinction này ngăn nhóm (team / 팀) đồng nhất “kiểm thử (test / 테스트) pass” với “giá trị (value / 값) achieved”. Acceptance thường cần bằng chứng (evidence / 증거) về conformance; benefit realization cần bằng chứng (evidence / 증거) về kết quả (outcome / 결과) sau khi năng lực (capability / 역량) được dùng.

## Functional và non-functional yêu cầu (requirement / 요구사항)

Functional yêu cầu (requirement / 요구사항) nói hệ thống (system / 시스템) cần làm gì. Non-functional yêu cầu (requirement / 요구사항) mô tả chất lượng (quality / 품질) hoặc ràng buộc (constraint / 제약조건) như hiệu năng (performance / 성능), bảo mật (security / 보안), availability, usability, portability hoặc compliance.

Dự án (project / 프로젝트) thường under-plan non-functional yêu cầu (requirement / 요구사항) vì chúng ít visible trong demo nhưng có thể quyết định go-live. Một tính năng (feature / 기능) đủ chức năng nhưng không đạt bảo mật (security / 보안) rà soát (review / 검토) vẫn chưa usable trong ngữ cảnh (context / 맥락) thật.

Non-functional yêu cầu (requirement / 요구사항) thường tạo cross-cutting công việc (work / 작업). bảo mật (security / 보안) hoặc availability không nằm gọn trong một tính năng (feature / 기능); nó ảnh hưởng kiến trúc (architecture / 아키텍처), kiểm thử (test / 테스트), monitoring, vendor và operations. Vì vậy chúng cần được đưa vào tích hợp (integration / 통합) lập luận (reasoning / 추론) sớm.

## Yêu cầu (requirement / 요구사항) vòng đời (lifecycle / 생명주기) và traceability

Yêu cầu (requirement / 요구사항) không chỉ được “thu thập” rồi đóng. Nó cần nguồn (source / 소스), đơn vị sở hữu (owner / 오너), priority, rationale, status, acceptance bằng chứng (evidence / 증거) và impact khi thay đổi.

Traceability nối nghiệp vụ (business / 비즈니스) need → yêu cầu (requirement / 요구사항) → deliverable/thiết kế (design / 설계) → xác minh (verification / 확인) → kết quả (outcome / 결과). Điều này giúp phát hiện orphan tính năng (feature / 기능) và uncovered yêu cầu (requirement / 요구사항). Chi tiết hơn xem [Artifacts, information flow và traceability](./14_artifacts_information_and_traceability.md).

Traceability còn giúp đánh giá blast radius khi thay đổi (change / 변경). Nếu yêu cầu (requirement / 요구사항) A đổi, đồ thị (graph / 그래프) cho biết thiết kế (design / 설계), kiểm thử (test / 테스트), vendor obligation, huấn luyện (training / 학습) và operational điều khiển (control / 제어) nào cần rà soát (review / 검토). Traceability vì vậy vừa phục vụ compliance vừa phục vụ thay đổi (change / 변경) economics.

## Decomposition và WBS

Công việc (work / 작업) Breakdown cấu trúc (structure / 구조) decompose dự án (project / 프로젝트) phạm vi (scope / 범위) thành các phần quản lý được. WBS tốt là sản phẩm (product / 제품)/deliverable-oriented trước khi biến thành activity danh sách (list / 목록). Điều này giúp giữ liên kết (connection / 연결) giữa công việc (work / 작업) và đầu ra (output / 출력).

Decomposition phải đủ chi tiết để estimate, assign và điều khiển (control / 제어), nhưng quá chi tiết tạo maintenance overhead. công việc (work / 작업) gói (package / 패키지) là mức (level / 수준) đủ nhỏ để có đơn vị sở hữu (owner / 오너)/estimate/điều khiển (control / 제어) hợp lý trong ngữ cảnh (context / 맥락).

Trong adaptive delivery, backlog decomposition thực hiện chức năng tương tự nhưng theo rolling horizon: epic/năng lực (capability / 역량) được chia dần thành item nhỏ khi gần delivery.

Decomposition cũng expose giao diện (interface / 인터페이스). Nếu hai công việc (work / 작업) gói (package / 패키지) cần cùng một mô hình dữ liệu (data model / 데이터 모델) hoặc cùng một expert, phụ thuộc (dependency / 의존성) nên được nhìn thấy trước khi activity scheduling.

## 100% quy tắc (rule / 규칙) và ranh giới (boundary / 경계) discipline

Một WBS thường dùng mô hình tư duy (mental model / 사고 모델) 100% quy tắc (rule / 규칙): parent phạm vi (scope / 범위) được bao phủ đầy đủ bởi child elements mà không cố ý thêm công việc (work / 작업) ngoài ranh giới (boundary / 경계).

Điểm quan trọng không phải thuộc quy tắc (rule / 규칙) để thi mà là tránh hai lỗi: missing công việc (work / 작업) và duplicate công việc (work / 작업). Nếu testing hoặc di chuyển (migration / 마이그레이션) không nằm trong WBS vì “đó không phải tính năng (feature / 기능)”, estimate sẽ thiếu dù hiện thực (implementation / 구현) phạm vi (scope / 범위) đúng.

100% quy tắc (rule / 규칙) không yêu cầu mô tả mọi micro-task. Nó yêu cầu không để trọng yếu (critical / 중요) deliverable/công việc (work / 작업) biến mất giữa lớp trừu tượng (abstraction / 추상화) mức (level / 수준).

## Phạm vi (scope / 범위) kiểm tra hợp lệ (validation / 검증) và chất lượng (quality / 품질) điều khiển (control / 제어) khác nhau

Chất lượng (quality / 품질) điều khiển (control / 제어) hỏi deliverable có đáp ứng specification hay không. Validate phạm vi (scope / 범위) hỏi customer/sponsor có formally accept deliverable phù hợp hay không.

Một thành phần (component / 컴포넌트) có thể pass nội bộ (internal / 내부) QA nhưng chưa được customer accept. Ngược lại, stakeholder có thể accept deliverable với agreed exception dù một noncritical defect còn tồn tại. Hai tiến trình (process / 프로세스) dùng bằng chứng (evidence / 증거) liên quan nhưng purpose khác.

## Acceptance debt

Acceptance debt xuất hiện khi nhóm (team / 팀) hoàn thành technical công việc (work / 작업) nhưng trì hoãn acceptance bằng chứng (evidence / 증거) hoặc stakeholder kiểm tra hợp lệ (validation / 검증). Dashboard có thể báo nhiều item “done”, trong khi nghiệp vụ (business / 비즈니스) chưa xác nhận deliverable thực sự usable.

Debt này nguy hiểm vì defect hoặc expectation gap được phát hiện muộn, khi chi phí (cost / 비용) of thay đổi (change / 변경) cao hơn. Early acceptance slice hoặc progressive kiểm tra hợp lệ (validation / 검증) làm giảm batch kích thước (size / 크기) của bất định (uncertainty / 불확실성).

## Phạm vi (scope / 범위) creep và gold plating

Phạm vi (scope / 범위) creep là expansion không được kiểm soát của phạm vi (scope / 범위). Gold plating là thêm tính năng (feature / 기능)/chất lượng (quality / 품질) không được yêu cầu chỉ vì nhóm (team / 팀) nghĩ nó tốt. Cả hai đều nguy hiểm vì dùng tài nguyên (resource / 자원) và thay rủi ro (risk / 위험) profile mà không có tường minh (explicit / 명시적) quyết định (decision / 결정).

Đây không có nghĩa mọi idea mới phải bị từ chối. Idea có giá trị (value / 값) nên đi qua thay đổi (change / 변경)/prioritization cơ chế (mechanism / 메커니즘) để sự đánh đổi (trade-off / 트레이드오프) được nhìn thấy.

Gold plating còn tạo hỗ trợ (support / 지원) obligation. Một tính năng (feature / 기능) không được yêu cầu nhưng đã bản phát hành (release / 릴리스) có thể trở thành permanent sản phẩm (product / 제품) expectation và tăng maintenance chi phí (cost / 비용).

## Thay đổi (change / 변경) là normal; uncontrolled thay đổi (change / 변경) mới là bài toán (problem / 문제)

Dự án (project / 프로젝트) tồn tại trong môi trường thay đổi. Mục tiêu không phải giữ plan bất biến mà là đảm bảo thay đổi (change / 변경) được đưa vào quyết định (decision / 결정) hệ thống (system / 시스템) phù hợp.

Predictive ngữ cảnh (context / 맥락) thường cần formal impact phân tích (analysis / 분석) và approval khi baseline bị ảnh hưởng. Adaptive ngữ cảnh (context / 맥락) absorb nhiều sản phẩm (product / 제품) thay đổi (change / 변경) qua backlog reprioritization, nhưng ngân sách (budget / 예산), regulatory phạm vi (scope / 범위), đặc tả hợp đồng (contract / 계약) và bản phát hành (release / 릴리스) commitment vẫn có guardrail.

Không có một thay đổi (change / 변경) tiến trình (process / 프로세스) duy nhất cho mọi mức (level / 수준). Typo trong document và thay authentication kiến trúc (architecture / 아키텍처) không cần cùng quản trị (governance / 거버넌스).

## Chi phí (cost / 비용) of thay đổi (change / 변경) và timing của quyết định (decision / 결정)

Một thay đổi (change / 변경) giống nhau có chi phí (cost / 비용) khác nhau tùy thời điểm. Đổi yêu cầu (requirement / 요구사항) trước thiết kế (design / 설계) rẻ hơn sau procurement, kiểm thử tích hợp (integration test / 통합 테스트) hoặc regulatory submission. Đây là lý do early phản hồi (feedback / 피드백) có economic giá trị (value / 값).

Tuy nhiên quyết định quá sớm khi thông tin (information / 정보) chưa đủ cũng có chi phí (cost / 비용). tích hợp (integration / 통합) cần cân bằng hai áp lực: delay quyết định (decision / 결정) có thể làm thay đổi (change / 변경) chi phí (cost / 비용) tăng; lần ghi nhận (commit / 커밋) sớm có thể khóa option sai. Reversible quyết định (decision / 결정) nên giữ linh hoạt lâu hơn; irreversible/long-lead quyết định (decision / 결정) cần bằng chứng (evidence / 증거) sớm hơn.

## Thay đổi (change / 변경) điều khiển (control / 제어): bảo vệ coherence, không bảo vệ status quo

Thay đổi (change / 변경) điều khiển (control / 제어) tồn tại vì một thay đổi (change / 변경) có second-order tác động (effect / 효과). Quy trình hợp lý thường bắt đầu bằng mô tả thay đổi (change / 변경) và reason, sau đó impact phân tích (analysis / 분석), authority quyết định (decision / 결정), hiện thực (implementation / 구현), cập nhật (update / 업데이트) artifacts/baselines và communication.

Trong predictive ngữ cảnh (context / 맥락), thay đổi (change / 변경) điều khiển (control / 제어) Board có thể phê duyệt thay đổi (change / 변경) lớn. Trong adaptive ngữ cảnh (context / 맥락), chủ sản phẩm (product owner / 제품 책임자)/backlog prioritization có thể hấp thụ yêu cầu (requirement / 요구사항) thay đổi (change / 변경) mà không cần ceremony giống predictive, miễn guardrail về ngân sách (budget / 예산), bản phát hành (release / 릴리스), compliance và kiến trúc (architecture / 아키텍처) được giữ.

Điểm chung là không làm “silent thay đổi (change / 변경)”. quyết định (decision / 결정) phải có đơn vị sở hữu (owner / 오너), impact và traceability phù hợp.

## Thay đổi (change / 변경) authority và threshold

Không phải thay đổi (change / 변경) nào cũng cần sponsor. quản trị (governance / 거버넌스) nên định nghĩa threshold để reversible/low-impact thay đổi (change / 변경) được xử lý gần nhóm (team / 팀), còn thay đổi (change / 변경) vượt tolerance mới escalate.

Nếu mọi thay đổi (change / 변경) đều lên CCB, hàng đợi (queue / 큐) và delay tăng. Nếu không thay đổi (change / 변경) nào lên quản trị (governance / 거버넌스), organization mất điều khiển (control / 제어). Tailoring đúng là đặt quyết định (decision / 결정) đúng mức (level / 수준).

Threshold nên gắn với materiality: ngân sách (budget / 예산) tolerance, regulatory tác động (effect / 효과), customer commitment, kiến trúc (architecture / 아키텍처) rủi ro (risk / 위험) hoặc đặc tả hợp đồng (contract / 계약) impact. “Mọi thay đổi (change / 변경) trên 3 ngày” có thể quá thô nếu một thay đổi 1 ngày chạm privacy điều khiển (control / 제어) còn một thay đổi 5 ngày chỉ đổi nội bộ.

## Thay đổi (change / 변경) độ trễ (latency / 지연 시간) là một biến quản trị

Thay đổi (change / 변경) độ trễ (latency / 지연 시간) là thời gian từ khi nhu cầu thay đổi được nhận diện tới khi quyết định (decision / 결정) đủ rõ để thực thi (execution / 실행) điều chỉnh. độ trễ (latency / 지연 시간) quá cao làm nhóm (team / 팀) tiếp tục bản dựng (build / 빌드) theo giả định (assumption / 가정) cũ; độ trễ (latency / 지연 시간) quá thấp nhưng thiếu phân tích (analysis / 분석) tạo quyết định hấp tấp.

Hàng đợi (queue / 큐) ở approval body là một nguồn (source / 소스) phổ biến. Nếu CCB họp mỗi tháng trong dự án (project / 프로젝트) có weekly thị trường (market / 시장) phản hồi (feedback / 피드백), quản trị (governance / 거버넌스) cadence không phù hợp với bất định (uncertainty / 불확실성) cadence.

Một điều khiển (control / 제어) tốt không chỉ hỏi “ai approve?” mà còn “quyết định (decision / 결정) phải xảy ra nhanh tới mức nào để còn tạo giá trị (value / 값)?”.

## Impact phân tích (analysis / 분석) cần xem second-order tác động (effect / 효과)

Một yêu cầu (request / 요청) “chỉ thêm một trường dữ liệu (field / 필드)” có thể chạm mô hình dữ liệu (data model / 데이터 모델), Đặc tả API (API contract / API 계약), di chuyển (migration / 마이그레이션), privacy classification, report, analytics, kiểm thử (test / 테스트) và huấn luyện (training / 학습).

Impact phân tích (analysis / 분석) nên đi qua phạm vi (scope / 범위), schedule, chi phí (cost / 비용), chất lượng (quality / 품질), rủi ro (risk / 위험), tài nguyên (resource / 자원), procurement, compliance, thao tác (operation / 연산) và stakeholder. Không phải mọi dimension đều bị ảnh hưởng, nhưng checklist mental này ngăn cục bộ (local / 로컬) estimate bị coi là total impact.

Second-order tác động (effect / 효과) còn có vòng phản hồi (feedback loop / 피드백 루프). Thêm tính năng (feature / 기능) làm schedule trễ; trễ làm đặc tả hợp đồng (contract / 계약) milestone bị miss; miss milestone làm cash receipt chậm; cash pressure lại giảm ability thêm tài nguyên (resource / 자원). tích hợp (integration / 통합) lập luận (reasoning / 추론) cần nhìn vòng lặp (loop / 루프), không chỉ one-hop phụ thuộc (dependency / 의존성).

## Thay đổi (change / 변경) propagation và blast radius

Khi thay đổi (change / 변경) được approve, câu hỏi tiếp theo là “trạng thái (state / 상태) nào phải đổi?”. Có thể phải cập nhật (update / 업데이트) yêu cầu (requirement / 요구사항), WBS/backlog, schedule, chi phí (cost / 비용) forecast, rủi ro (risk / 위험) phản hồi (response / 응답), vendor SOW, kiểm thử (test / 테스트) bằng chứng (evidence / 증거), huấn luyện (training / 학습) và operational runbook.

Blast radius càng rộng, coordination chi phí (cost / 비용) càng cao. Modular kiến trúc (architecture / 아키텍처), clear giao diện (interface / 인터페이스) và decoupled đặc tả hợp đồng (contract / 계약) ranh giới (boundary / 경계) làm blast radius nhỏ hơn. Vì thế tích hợp (integration / 통합) chất lượng (quality / 품질) chịu ảnh hưởng trực tiếp bởi hệ thống (system / 시스템) thiết kế (design / 설계) và organizational thiết kế (design / 설계).

## Concurrent thay đổi (change / 변경) và collision rủi ro (risk / 위험)

Hai thay đổi (change / 변경) riêng lẻ có thể đều hợp lý nhưng xung đột khi diễn ra đồng thời. nhóm (team / 팀) A đổi lược đồ (schema / 스키마) để hỗ trợ tính năng (feature / 기능) mới; nhóm (team / 팀) B tối ưu di chuyển (migration / 마이그레이션) dựa trên lược đồ (schema / 스키마) cũ. bảo mật (security / 보안) đổi authentication luồng (flow / 흐름) trong khi vendor đang certify tích hợp (integration / 통합). Mỗi thay đổi (change / 변경) có impact phân tích (analysis / 분석) cục bộ (local / 로컬) đúng nhưng combined trạng thái (state / 상태) lại không hợp lệ.

Vì vậy tích hợp (integration / 통합) cần nhìn **thay đổi (change / 변경) tính đồng thời (concurrency / 동시성)**, không chỉ từng ticket độc lập. Khi nhiều thay đổi (change / 변경) chạm cùng giao diện (interface / 인터페이스), dùng chung (shared / 공유) tài nguyên (resource / 자원), baseline hoặc bản phát hành (release / 릴리스) cửa sổ (window / 윈도우), cần chuỗi (sequence / 시퀀스), tính tương thích (compatibility / 호환성) quy tắc (rule / 규칙) hoặc synchronization điểm (point / 지점).

Collision rủi ro (risk / 위험) tăng khi thay đổi (change / 변경) thông lượng (throughput / 처리량) cao nhưng cấu hình (configuration / 구성) visibility thấp. Adaptive delivery không loại bỏ vấn đề này; cadence nhanh thậm chí làm collision xảy ra nhanh hơn nếu giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약) và automated tích hợp (integration / 통합) bằng chứng (evidence / 증거) yếu.

Một useful question là: “Nếu thay đổi (change / 변경) A và B đều được approve, trạng thái (state / 상태) cuối có còn coherent không?”. Đây là mức (level / 수준) lập luận (reasoning / 추론) cao hơn “A có approve được không?” và “B có approve được không?”.

## Cấu hình (configuration / 구성) management và phiên bản (version / 버전) truth

Khi nhiều phiên bản (version / 버전) của yêu cầu (requirement / 요구사항), thiết kế (design / 설계) hoặc deliverable tồn tại, nhóm (team / 팀) cần biết cái nào là authorized trạng thái (state / 상태). cấu hình (configuration / 구성) management giải quyết identification, versioning, status accounting và điều khiển (control / 제어). Trong software, Git/CI/CD là một phần technical cơ chế (mechanism / 메커니즘); ở dự án (project / 프로젝트) mức (level / 수준) còn có phiên bản (version / 버전) của đặc tả hợp đồng (contract / 계약), phạm vi (scope / 범위) baseline, kiểm thử (test / 테스트) bằng chứng (evidence / 증거) và bản phát hành (release / 릴리스) gói (package / 패키지).

Cấu hình (configuration / 구성) management khác thay đổi (change / 변경) điều khiển (control / 제어) nhưng liên quan chặt. thay đổi (change / 변경) điều khiển (control / 제어) quyết định trạng thái (state / 상태) có được đổi không; cấu hình (configuration / 구성) điều khiển (control / 제어) đảm bảo mọi người biết authorized trạng thái (state / 상태) nào đang có hiệu lực.

Nếu thay đổi (change / 변경) được approve nhưng vendor vẫn implement specification cũ, thất bại (failure / 실패) không nằm ở approval mà ở cấu hình (configuration / 구성) propagation.

## Tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) và di chuyển (migration / 마이그레이션) trạng thái (state / 상태)

Trong dự án (project / 프로젝트) có nhiều nhóm (team / 팀)/vendor, không phải mọi thành phần (component / 컴포넌트) có thể đổi atomically. Một thời gian có thể phải hỗ trợ old và new trạng thái (state / 상태) cùng tồn tại: API v1/v2, old/new tiến trình (process / 프로세스), legacy/new dữ liệu (data / 데이터) format hoặc hai chính sách (policy / 정책) phiên bản (version / 버전) trong chuyển tiếp (transition / 전이).

Đây là **tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)**. Nó cần start/end điều kiện (condition / 조건), đơn vị sở hữu (owner / 오너) và retirement plan. Nếu chỉ thêm backward tính tương thích (compatibility / 호환성) mà không có exit criterion, temporary độ phức tạp (complexity / 복잡도) dễ trở thành permanent chi phí (cost / 비용).

Di chuyển (migration / 마이그레이션) trạng thái (state / 상태) cũng tạo rủi ro (risk / 위험) riêng: dữ liệu (data / 데이터) có thể nằm ở hai nguồn (source / 소스), người dùng (user / 사용자) được chia cohort, hỗ trợ (support / 지원) phải hiểu hai workflow. tích hợp (integration / 통합) plan phải quản lý intermediate trạng thái (state / 상태) chứ không chỉ trạng thái hiện tại (current state / 현재 상태) và mục tiêu (target / 대상) trạng thái (state / 상태).

## Baseline topology: phạm vi (scope / 범위), schedule và chi phí (cost / 비용) liên kết nhau

Phạm vi (scope / 범위), schedule và chi phí (cost / 비용) baseline không nên được xem là ba tệp (file / 파일) rời. Chúng là ba projection của cùng commitment. phạm vi (scope / 범위) nói “cái gì”, schedule nói “khi nào”, chi phí (cost / 비용) nói “bao nhiêu tài nguyên (resource / 자원)”.

Một approved thay đổi (change / 변경) có thể chỉ tác động một baseline, nhưng nếu phạm vi (scope / 범위) tăng mà schedule/chi phí (cost / 비용) không đổi, cần giải thích cơ chế (mechanism / 메커니즘) nào hấp thụ thay đổi (change / 변경). Nếu không có cơ chế (mechanism / 메커니즘), baseline set đã trở nên internally inconsistent.

Rebaseline chỉ nên xảy ra khi authorized planning basis thay đổi, không phải để xóa lịch sử hiệu năng (performance / 성능). Original baseline, approved changes và hiện tại (current / 현재) baseline cần dấu vết (trace / 추적) được.

## Integrated thay đổi (change / 변경) điều khiển (control / 제어) và vòng phản hồi (feedback loop / 피드백 루프)

Sau khi thay đổi (change / 변경) được approve, công việc (work / 작업) chưa kết thúc. Plan, baseline, rủi ro (risk / 위험), yêu cầu (requirement / 요구사항), procurement và communication cần được cập nhật (update / 업데이트). Nếu quyết định (decision / 결정) được approve nhưng downstream sản phẩm tạo ra (artifact / 산출물) không đổi, dự án (project / 프로젝트) có inconsistent truth.

Một good thay đổi (change / 변경) vòng lặp (loop / 루프) là proposed → analyzed → decided → implemented → verified → reflected in source-of-truth. Mất một chuyển tiếp (transition / 전이) tạo hidden debt.

Xác minh (verification / 확인) của thay đổi (change / 변경) cũng quan trọng. “Implemented” không đồng nghĩa intended tác động (effect / 효과) đã đạt. Một new điều khiển (control / 제어) cần bằng chứng (evidence / 증거) rằng rủi ro (risk / 위험) giảm; một phạm vi (scope / 범위) reduction cần bằng chứng (evidence / 증거) rằng phụ thuộc (dependency / 의존성) cũ thực sự được remove.

## Tích hợp (integration / 통합) debt

Tích hợp (integration / 통합) debt là khoảng cách giữa cục bộ (local / 로컬) states đã thay đổi và project-wide trạng thái (state / 상태) chưa được reconcile. Ví dụ backlog đã bỏ tính năng (feature / 기능) nhưng đặc tả hợp đồng (contract / 계약) chưa sửa; bản phát hành (release / 릴리스) đã đổi kiến trúc (architecture / 아키텍처) nhưng runbook/huấn luyện (training / 학습) vẫn mô tả luồng (flow / 흐름) cũ; sponsor đã đổi benefit mục tiêu (target / 대상) nhưng chỉ số (metric / 지표) plan chưa đổi.

Debt này thường không visible như defect. Mỗi sản phẩm tạo ra (artifact / 산출물) riêng có thể “đúng theo lần cập nhật cuối của nó”, nhưng chúng không còn đúng **cùng nhau**. Khi dự án (project / 프로젝트) gần gate hoặc handover, debt bùng ra thành reconciliation công việc (work / 작업), dispute hoặc rework.

Một cách kiểm soát là dùng tích hợp (integration / 통합) checkpoint dựa trên sự kiện (event / 이벤트): approved material thay đổi (change / 변경), bản phát hành (release / 릴리스) candidate, vendor milestone, regulatory submission hoặc chuyển tiếp (transition / 전이) gate. Checkpoint không cần rà soát (review / 검토) mọi tệp (file / 파일); nó cần xác nhận những trạng thái (state / 상태) có coupling cao đã converged về cùng authorized quyết định (decision / 결정).

## Phụ thuộc (dependency / 의존성) management

Tích hợp (integration / 통합) cũng là quản lý phụ thuộc (dependency / 의존성). phụ thuộc (dependency / 의존성) có thể technical, tài nguyên (resource / 자원), bên ngoài (external / 외부) approval, đặc tả hợp đồng (contract / 계약) hoặc organizational.

Một phụ thuộc (dependency / 의존성) tốt cần đơn vị sở hữu (owner / 오너), needed-by date, hiện tại (current / 현재) confidence và fallback/escalation. “nhóm (team / 팀) B đang làm” không phải đủ thông tin (information / 정보) nếu milestone của nhóm (team / 팀) A phụ thuộc đầu ra (output / 출력) đó.

Phụ thuộc (dependency / 의존성) nên được giảm khi có thể, không chỉ theo dõi. kiến trúc (architecture / 아키텍처) decoupling, đặc tả hợp đồng (contract / 계약) giao diện (interface / 인터페이스) rõ hoặc nhóm (team / 팀) topology tốt có thể xóa coordination công việc (work / 작업) khỏi dự án (project / 프로젝트).

## Giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약) và handoff chất lượng (quality / 품질)

Nhiều thất bại (failure / 실패) không xảy ra bên trong nhóm (team / 팀) mà ở handoff. giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약) nên làm rõ đầu vào (input / 입력), đầu ra (output / 출력), format, acceptance, timing và lỗi (error / 오류) handling giữa hai workstream/party.

Nếu nhóm (team / 팀) A “hoàn thành API” nhưng nhóm (team / 팀) B không biết phiên bản (version / 버전), tỷ lệ (rate / 비율) limit hoặc kiểm thử (test / 테스트) môi trường (environment / 환경), cục bộ (local / 로컬) completion không tạo integrated progress. Handoff cần bằng chứng (evidence / 증거) rằng receiving side có thể sử dụng đầu ra (output / 출력), không chỉ sender tuyên bố done.

## Quyết định (decision / 결정) log và consistency

Nhiều tích hợp (integration / 통합) thất bại (failure / 실패) xuất hiện vì quyết định (decision / 결정) được đưa ra riêng lẻ trong các meeting khác nhau. quyết định (decision / 결정) log giữ ngữ cảnh (context / 맥락) và rationale giúp tránh contradiction.

Ví dụ bảo mật (security / 보안) nhóm (team / 팀) approve thiết kế (design / 설계) A với giả định (assumption / 가정) dữ liệu (data / 데이터) không lưu lâu dài, nhưng nghiệp vụ (business / 비즈니스) sau đó quyết định retention 7 năm. tích hợp (integration / 통합) cơ chế (mechanism / 메커니즘) phải detect giả định (assumption / 가정) xung đột (conflict / 충돌) và trigger rà soát (review / 검토).

Quyết định (decision / 결정) log mạnh hơn khi ghi quyết định (decision / 결정) đơn vị sở hữu (owner / 오너), effective date, affected artifacts và giả định (assumption / 가정) expiry. Nó trở thành nút (node / 노드) trong thay đổi (change / 변경) đồ thị (graph / 그래프) thay vì meeting minutes.

## Ví dụ impact phân tích (analysis / 분석)

Customer yêu cầu thêm biometric fallback trước go-live. Thay vì hỏi “mất bao nhiêu ngày?”, PM cần kiểm tra ít nhất: yêu cầu (requirement / 요구사항)/bảo mật (security / 보안) implication, vendor/API phụ thuộc (dependency / 의존성), privacy rà soát (review / 검토), kiểm thử (test / 테스트) phạm vi (scope / 범위), schedule đường găng (critical path / 임계 경로), ngân sách (budget / 예산), operations huấn luyện (training / 학습) và nghiệp vụ (business / 비즈니스) giá trị (value / 값). Có thể tính năng (feature / 기능) chỉ mã (code / 코드) ba ngày nhưng kéo thêm bảo mật (security / 보안) approval hai tuần. tích hợp (integration / 통합) lập luận (reasoning / 추론) tìm total hệ thống (system / 시스템) impact chứ không chỉ coding effort.

Nếu fallback là mandatory regulatory yêu cầu (requirement / 요구사항) mới, priority khác hoàn toàn một optional UX enhancement. Nếu deadline legal không đổi, dự án (project / 프로젝트) có thể phải de-scope optional tính năng (feature / 기능) khác hoặc tăng sức chứa (capacity / 용량). thay đổi (change / 변경) quyết định (decision / 결정) là sự đánh đổi (trade-off / 트레이드오프) hệ thống (system / 시스템), không phải estimate exercise.

Một scenario khác: sponsor approve phạm vi (scope / 범위) reduction để giữ deadline nhưng procurement đặc tả hợp đồng (contract / 계약) vẫn yêu cầu deliverable cũ. Nếu nhóm (team / 팀) chỉ cập nhật (update / 업데이트) backlog, vendor vẫn có contractual obligation và invoice basis khác. tích hợp (integration / 통합) thất bại (failure / 실패) xuất hiện vì thay đổi (change / 변경) chưa propagate qua commercial ranh giới (boundary / 경계).

## Thất bại (failure / 실패) modes

Cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화) xảy ra khi từng lĩnh vực (domain / 도메인) tối ưu riêng. Silent phạm vi (scope / 범위) creep xảy ra khi nhóm (team / 팀) làm thay đổi (change / 변경) trước approval. Baseline theater xảy ra khi baseline liên tục rewrite để không có variance. yêu cầu (requirement / 요구사항) dumping xảy ra khi mọi stakeholder yêu cầu (request / 요청) đều được ghi nhưng không resolve xung đột (conflict / 충돌). Approval theater xảy ra khi CCB approve nhưng không ai cập nhật (update / 업데이트) thực thi (execution / 실행) sản phẩm tạo ra (artifact / 산출물).

Quyết định (decision / 결정) độ trễ (latency / 지연 시간) mismatch xảy ra khi quản trị (governance / 거버넌스) cadence chậm hơn cadence của bất định (uncertainty / 불확실성). cấu hình (configuration / 구성) drift xảy ra khi các party dùng phiên bản (version / 버전) khác nhau. Acceptance debt xảy ra khi technical completion đi trước formal/nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증). giao diện (interface / 인터페이스) blindness xảy ra khi mỗi nhóm (team / 팀) đúng cục bộ (local / 로컬) phạm vi (scope / 범위) nhưng handoff không usable. giả định (assumption / 가정) debt làm nhiều commitment phụ thuộc fact chưa được chứng minh. thay đổi (change / 변경) collision xảy ra khi các thay đổi (change / 변경) cục bộ (local / 로컬) hợp lệ tạo combined trạng thái (state / 상태) không coherent. tích hợp (integration / 통합) debt tích khi sản phẩm tạo ra (artifact / 산출물) đúng riêng lẻ nhưng sai với nhau.

Tích hợp (integration / 통합) maturity được đo bằng consistency giữa quyết định (decision / 결정) và actual dự án (project / 프로젝트) trạng thái (state / 상태).

## Mô hình tư duy (mental model / 사고 모델)

> phạm vi (scope / 범위) tạo ranh giới (boundary / 경계) cho commitment; thay đổi (change / 변경) điều khiển (control / 제어) giữ các commitment liên quan vẫn nhất quán khi ranh giới (boundary / 경계) thay đổi. tích hợp (integration / 통합) là khả năng làm một quyết định (decision / 결정) propagate đúng qua yêu cầu (requirement / 요구사항), giả định (assumption / 가정), baseline, phụ thuộc (dependency / 의존성), đặc tả hợp đồng (contract / 계약), bằng chứng (evidence / 증거) và stakeholder trước khi các cục bộ (local / 로컬) trạng thái (state / 상태) tách thành nhiều “sự thật”.

Tiếp theo: [Schedule, estimation, dependency và flow](./05_schedule_estimation_and_flow.md).

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 foundations value and project system](./00_foundations_value_and_project_system.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
