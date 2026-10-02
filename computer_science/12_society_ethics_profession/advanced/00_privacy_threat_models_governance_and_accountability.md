# Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Privacy threat models, governance và accountability**. Route đi từ data-flow threat surface → actors/purposes → minimization architecture constraint → governance controls → accountability evidence, để privacy được đánh giá xuyên vòng đời.

Privacy kỹ thuật (engineering / 엔지니어링) không đồng nhất với bảo mật (security / 보안). Một hệ thống (system / 시스템) có thể không bị hack nhưng vẫn thu thập quá nhiều dữ liệu (data / 데이터), dùng dữ liệu (data / 데이터) ngoài purpose ban đầu hoặc giữ dữ liệu (data / 데이터) lâu hơn cần thiết. Vì vậy privacy cần threat mô hình (model / 모델) riêng về **linkability, identifiability, suy luận (inference / 추론), secondary use và power over dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기)**.

## Bắt đầu từ luồng dữ liệu (data flow / 데이터 흐름), không chỉ cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마)

Vẽ dữ liệu (data / 데이터) nguồn (source / 소스) → collection → transformation → lưu trữ (storage / 저장소) → sharing → analytics → deletion. Cùng một attribute có thể xuất hiện trong logs, bộ nhớ đệm (cache / 캐시), backup, warehouse và third-party telemetry.

“Xóa người dùng (user / 사용자) khỏi main DB” chưa chắc là deletion hoàn chỉnh nếu identifiers còn trong sự kiện (event / 이벤트) stream/backups/tìm kiếm (search / 검색) chỉ mục (index / 인덱스). dữ liệu (data / 데이터) inventory phải theo luồng (flow / 흐름) và copies.

> **Chuyển mạch:** Privacy threat model phải theo data flow qua system, không chỉ schema; minimization là architectural constraint, còn purpose limitation ngăn function creep sau khi dữ liệu đã được thu thập.

## Dữ liệu (data / 데이터) minimization là kiến trúc (architecture / 아키텍처) ràng buộc (constraint / 제약조건)

Cách bảo vệ tốt nhất cho dữ liệu (data / 데이터) không cần thiết là không thu nó. Nếu tính năng (feature / 기능) chỉ cần age band, lưu full birth date tạo thêm sensitivity mà không tăng utility tương ứng.

Minimization có thể áp ở collection, precision, retention và truy cập (access / 접근). Ví dụ location có thể coarse-grain trước khi lưu nếu chính xác (exact / 정확한) coordinate không cần cho lô-gic nghiệp vụ (business logic / 비즈니스 로직).

> **Chuyển mạch:** Ở chặng này của **Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability**, **Dữ liệu (data / 데이터) minimization là kiến trúc (architecture / 아키텍처) ràng buộc (constraint / 제약조건)** đã nêu tiêu chí phân biệt, còn **Purpose limitation và hàm (function / 함수) creep** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Pseudonymization không phải anonymization tuyệt đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Purpose limitation và hàm (function / 함수) creep

Dữ liệu (data / 데이터) thu để chống fraud sau đó dùng cho marketing có thể thay rủi ro (risk / 위험)/expectation. Technical teams cần siêu dữ liệu (metadata / 메타데이터)/chính sách (policy / 정책) để biết dataset được phép dùng vào purpose nào, thay vì giả định “đã có dữ liệu (data / 데이터) thì dùng được”.

Quản trị (governance / 거버넌스) tốt nối nghiệp vụ (business / 비즈니스) purpose với lược đồ (schema / 스키마)/danh mục (catalog / 카탈로그)/truy cập (access / 접근) chính sách (policy / 정책) và rà soát (review / 검토) tiến trình (process / 프로세스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability**, **Purpose limitation và hàm (function / 함수) creep** đã nêu tiêu chí phân biệt, còn **Pseudonymization không phải anonymization tuyệt đối** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kiểm soát truy cập (access control / 접근 제어) và accountability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pseudonymization không phải anonymization tuyệt đối

Thay name bằng random ID giảm direct identification nhưng các quasi-identifiers hoặc linkage với dataset khác vẫn có thể re-identify. Timestamp, location mẫu (pattern / 패턴), rare attributes có thể đủ đặc trưng.

Privacy rủi ro (risk / 위험) vì vậy phụ thuộc adversary auxiliary thông tin (information / 정보), không chỉ việc xóa cột `name`.

> **Chuyển mạch:** Trong **Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability**, **Kiểm soát truy cập (access control / 접근 제어) và accountability** tiếp nhận điểm tựa từ **Pseudonymization không phải anonymization tuyệt đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Retention là máy trạng thái (state machine / 상태 머신)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm soát truy cập (access control / 접근 제어) và accountability

Least privilege giới hạn ai đọc dữ liệu (data / 데이터); auditability cho biết ai đã đọc gì và vì sao. High-risk truy cập (access / 접근) thường cần purpose/approval ngữ cảnh (context / 맥락), not only role.

Nhật ký kiểm tra (audit log / 감사 로그) phải chống tampering đủ mức, nhưng log cũng chứa personal dữ liệu (data / 데이터) nên cần retention/truy cập (access / 접근) chính sách (policy / 정책) của chính nó.

> **Chuyển mạch:** Ở chặng này của **Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability**, **Retention là máy trạng thái (state machine / 상태 머신)** tiếp nhận điểm tựa từ **Kiểm soát truy cập (access control / 접근 제어) và accountability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Accountability cần dấu vết (trace / 추적) quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Retention là máy trạng thái (state machine / 상태 머신)

“Giữ 30 ngày” nghe đơn giản nhưng cần định nghĩa sự kiện (event / 이벤트) bắt đầu, legal/nghiệp vụ (business / 비즈니스) exception, backups, delayed jobs và derived dữ liệu (data / 데이터). Retention hiện thực (implementation / 구현) thường là workflow:

```text
active → expired → deletion queued → deleted from primary → aged out from backups
```

Nếu hệ thống (system / 시스템) không biết dữ liệu (data / 데이터) ở đâu, không thể thực thi retention đáng tin.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability**, **Accountability cần dấu vết (trace / 추적) quyết định (decision / 결정)** tiếp nhận điểm tựa từ **Retention là máy trạng thái (state machine / 상태 머신)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Privacy chỉ số (metric / 지표) không thay normative quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Accountability cần dấu vết (trace / 추적) quyết định (decision / 결정)

Khi automated hệ thống (system / 시스템) ảnh hưởng người dùng (user / 사용자), cần tái dựng đầu vào (input / 입력)/phiên bản (version / 버전)/chính sách (policy / 정책)/mô hình (model / 모델)/đầu ra (output / 출력) liên quan. Provenance hỗ trợ debugging, kiểm tra (audit / 감사) và contestability.

Nhưng logging mọi tính năng (feature / 기능)/đầu vào (input / 입력) cũng tăng privacy surface. Accountability và minimization phải được thiết kế cùng nhau: lưu bằng chứng (evidence / 증거) cần thiết, không bản sao (copy / 복사) toàn payload vô hạn.

> **Chuyển mạch:** Trong **Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability**, **Privacy chỉ số (metric / 지표) không thay normative quyết định (decision / 결정)** tiếp nhận điểm tựa từ **Accountability cần dấu vết (trace / 추적) quyết định (decision / 결정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Privacy chỉ số (metric / 지표) không thay normative quyết định (decision / 결정)

Differential privacy cung cấp formal khung phần mềm (framework / 프레임워크) cho leakage qua statistical bản phát hành (release / 릴리스), nhưng parameter choice và applicability vẫn gắn với sản phẩm (product / 제품) ngữ cảnh (context / 맥락). K-anonymity-like heuristics có limitations trước linkage attacks.

Technical chỉ số (metric / 지표) không tự quyết định “acceptable use”; quản trị (governance / 거버넌스) cần stakeholders, law/chính sách (policy / 정책) ngữ cảnh (context / 맥락) và impact phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Privacy chỉ số (metric / 지표) không thay normative quyết định (decision / 결정)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Privacy kỹ thuật (engineering / 엔지니어링) là quản lý **dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기) + allowed purpose + suy luận (inference / 추론)/linkage rủi ro (risk / 위험) + accountability**. bảo mật (security / 보안) bảo vệ khỏi unauthorized truy cập (access / 접근); privacy còn hỏi authorized hệ thống (system / 시스템) có nên thu, dùng và giữ dữ liệu (data / 데이터) đó theo cách này hay không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Privacy threat các mô hình (models / 모델들), quản trị (governance / 거버넌스) và accountability**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ôn [privacy/professional foundation](../../basic/12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md), [data governance](../../basic/12_society_ethics_profession/01_data_governance_bias_and_algorithmic_impact.md) và [security threat models](../../basic/07_security_reliability/00_threat_models_and_security_principles.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
