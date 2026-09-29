# 11 — quản trị (governance / 거버넌스), lineage và bảo mật (security / 보안)

> **Mạch đọc:** Đọc **11 — quản trị (governance / 거버넌스), lineage và bảo mật (security / 보안)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약)** sang **2. danh mục (catalog / 카탈로그) và quyền sở hữu (ownership / 소유권)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Quản trị (governance / 거버넌스) là cách hệ thống biết dữ liệu nào tồn tại, ai sở hữu, được dùng cho mục đích nào, thay đổi ra sao và phải xóa khi nào. Đây là điều khiển (control / 제어) plane của dữ liệu (data / 데이터) sản phẩm (product / 제품), không phải tài liệu hành chính nằm ngoài chuỗi xử lý (pipeline / 파이프라인).

## 1. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약)

Đặc tả hợp đồng (contract / 계약) giữa producer và bên tiêu thụ (consumer / 소비자) cần bao gồm lược đồ (schema / 스키마), grain, ngữ nghĩa (semantics / 의미론), chất lượng (quality / 품질) expectation, tính tương thích (compatibility / 호환성), đơn vị sở hữu (owner / 오너), freshness và sự cố (incident / 인시던트) contact. đặc tả hợp đồng (contract / 계약) tốt làm breaking thay đổi (change / 변경) thành một quy trình có thông báo thay vì surprise.

Lược đồ (schema / 스키마) registry không tự tạo ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약). trường dữ liệu (field / 필드) `status` có thể parse được nhưng đổi nghĩa từ “payment trạng thái (state / 상태)” sang “shipment trạng thái (state / 상태)” vẫn là breaking thay đổi (change / 변경).


> **Chuyển mạch:** Từ **1. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약)**, ta sang **2. danh mục (catalog / 카탈로그) và quyền sở hữu (ownership / 소유권)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. danh mục (catalog / 카탈로그) và quyền sở hữu (ownership / 소유권)

Danh mục (catalog / 카탈로그) tối thiểu cần biết dataset đường dẫn (path / 경로), lĩnh vực (domain / 도메인), đơn vị sở hữu (owner / 오너), steward, nguồn (source / 소스), grain, sensitivity, freshness SLO, retention và related assets. Dataset không có đơn vị sở hữu (owner / 오너) không có người quyết định khi chất lượng (quality / 품질) thất bại (fail / 실패) hoặc lược đồ (schema / 스키마) cần evolve.

Quyền sở hữu (ownership / 소유권) phải gắn với hành động (action / 동작): ai approve thay đổi (change / 변경), ai triage sự cố (incident / 인시던트), ai xác nhận delete, ai chịu chi phí (cost / 비용).


> **Chuyển mạch:** Từ **2. danh mục (catalog / 카탈로그) và quyền sở hữu (ownership / 소유권)**, ta sang **3. Lineage** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Lineage

Lineage là bằng chứng (evidence / 증거) đồ thị (graph / 그래프) từ nguồn (source / 소스) → ingestion → transformation → serving → bên tiêu thụ (consumer / 소비자). Static SQL parser có thể bỏ sót động (dynamic / 동적) mã (code / 코드); thời gian chạy (runtime / 런타임) lineage có chi phí instrumentation. Nên kết hợp orchestration siêu dữ liệu (metadata / 메타데이터), truy vấn (query / 쿼리) logs, bảng (table / 테이블) danh mục (catalog / 카탈로그) và triển khai (deployment / 배포) phiên bản (version / 버전).

Lineage không chứng minh dữ liệu (data / 데이터) đúng. Nó giúp khoanh blast radius và lần ngược nguyên nhân nhanh hơn.


> **Chuyển mạch:** Từ **3. Lineage**, ta sang **4. ranh giới bảo mật (security boundary / 보안 경계)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. ranh giới bảo mật (security boundary / 보안 경계)

Least privilege áp dụng cho dịch vụ (service / 서비스) account, engineer và bên tiêu thụ (consumer / 소비자). Tách quyền đọc raw PII khỏi quyền đọc serving aggregate. Encryption at rest/in transit là baseline; cần thêm masking/tokenization, row/column-level truy cập (access / 접근), nhật ký kiểm tra (audit log / 감사 로그) và secret rotation.

Development không nên bản sao (copy / 복사) môi trường vận hành (production / 운영 환경) PII mặc định. Nếu cần mẫu (sample / 표본), dùng synthetic hoặc masked dữ liệu (data / 데이터) có chính sách (policy / 정책) rõ.


> **Chuyển mạch:** Từ **4. ranh giới bảo mật (security boundary / 보안 경계)**, ta sang **5. Retention và deletion** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. Retention và deletion

Retention phải bao phủ raw files, snapshots, backups, caches, derived tables và downstream exports. Xóa row ở serving nhưng giữ tệp (file / 파일) raw hoặc snapshot cũ vẫn có thể vi phạm deletion yêu cầu (requirement / 요구사항).

Replayability và privacy có thể xung đột. Thiết kế cần biết trường dữ liệu (field / 필드) nào immutable, trường dữ liệu (field / 필드) nào có thể redact, và khi deletion xảy ra thì trạng thái (state / 상태)/projection nào phải rebuild.


> **Chuyển mạch:** Từ **5. Retention và deletion**, ta sang **6. chất lượng (quality / 품질) và sự cố (incident / 인시던트)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. chất lượng (quality / 품질) và sự cố (incident / 인시던트)

Quản trị (governance / 거버넌스) nên liên kết đặc tả hợp đồng (contract / 계약) với chất lượng (quality / 품질) checks, lineage-aware alert và runbook. Alert về lược đồ (schema / 스키마) drift phải cho biết bên tiêu thụ (consumer / 소비자) bị ảnh hưởng; alert về PII truy cập (access / 접근) phải giữ kiểm tra (audit / 감사) bằng chứng (evidence / 증거); quarantine phải có đơn vị sở hữu (owner / 오너) và replay procedure.


> **Chuyển mạch:** Từ **6. chất lượng (quality / 품질) và sự cố (incident / 인시던트)**, ta sang **7. rà soát (review / 검토) checklist** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. rà soát (review / 검토) checklist

1. Dataset có đơn vị sở hữu (owner / 오너), grain, sensitivity và retention không?
2. Producer/bên tiêu thụ (consumer / 소비자) đặc tả hợp đồng (contract / 계약) và tính tương thích (compatibility / 호환성) chính sách (policy / 정책) ở đâu?
3. Có thể lần ngược từ chỉ số (metric / 지표) sai về nguồn (source / 소스) snapshot không?
4. Quyền raw/mô hình (model / 모델)/serving có tách không?
5. Delete/rectification có lan qua snapshot, backup và derived đầu ra (output / 출력) không?

Đọc tiếp: [04 — Reliability](../04_reliability_and_production.md), [09 — Warehouse/lakehouse](../09_warehouse_lake_lakehouse/README.md), [10 — Serving](../10_serving_semantic_layer/README.md).


> **Chuyển mạch:** Từ **7. rà soát (review / 검토) checklist**, ta sang **8. Classification và chính sách (policy / 정책) enforcement** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 8. Classification và chính sách (policy / 정책) enforcement

Sensitivity classification nên gắn với column/trường dữ liệu (field / 필드) và purpose, không chỉ gắn với cơ sở dữ liệu (database / 데이터베이스). Một dataset có thể chứa PII ở một column, aggregate an toàn ở column khác và secret ở payload nested.

Chính sách (policy / 정책) enforcement cần xảy ra cả lúc đọc và lúc bản sao (copy / 복사)/export. Masking trong UI không đủ nếu người dùng (user / 사용자) vẫn có quyền đọc raw tệp (file / 파일) hoặc download bộ nhớ đệm (cache / 캐시). chính sách (policy / 정책) kiểm thử (test / 테스트) nên kiểm tra role, purpose, môi trường (environment / 환경), region và kiểm tra (audit / 감사) sự kiện (event / 이벤트).


> **Chuyển mạch:** Từ **8. Classification và chính sách (policy / 정책) enforcement**, ta sang **9. Lineage confidence** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 9. Lineage confidence

Không phải edge lineage nào cũng có cùng độ tin cậy:

```text
declared contract > runtime observed > static parser > naming convention
```

Danh mục (catalog / 카탈로그) nên lưu nguồn (source / 소스) của edge và timestamp quan sát. Khi lineage thiếu, hiển thị “unknown” tốt hơn tạo đồ thị (graph / 그래프) giả chắc chắn khiến sự cố (incident / 인시던트) triage đi sai.


> **Chuyển mạch:** Từ **9. Lineage confidence**, ta sang **10. thay đổi (change / 변경) management** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 10. thay đổi (change / 변경) management

Một lược đồ (schema / 스키마)/ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경) cần blast-radius truy vấn (query / 쿼리): downstream tables, dashboards, ML features, exports, truy cập (access / 접근) policies và chi phí (cost / 비용) centers. đơn vị sở hữu (owner / 오너) phê duyệt thay đổi (change / 변경) phải khác với người chỉ sửa tệp (file / 파일) nếu rủi ro (risk / 위험) cao.

Deprecation cửa sổ (window / 윈도우) cần có telemetry bên tiêu thụ (consumer / 소비자). Không xóa trường dữ liệu (field / 필드) chỉ vì danh mục (catalog / 카탈로그) không liệt kê bên tiêu thụ (consumer / 소비자); absence of bằng chứng (evidence / 증거) không phải bằng chứng (evidence / 증거) of absence.


> **Chuyển mạch:** Từ **10. thay đổi (change / 변경) management**, ta sang **11. dữ liệu (data / 데이터) deletion kiểm tra (audit / 감사)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 11. dữ liệu (data / 데이터) deletion kiểm tra (audit / 감사)

Deletion yêu cầu (request / 요청) nên tạo manifest gồm subject key, nguồn (source / 소스) tables, snapshots, derived outputs, backups và completion bằng chứng (evidence / 증거). Reconciliation sau delete phải chứng minh subject không còn trong các serving đường dẫn (path / 경로) được phạm vi (scope / 범위), hoặc ghi rõ retention exception được phê duyệt.

> **Bàn giao:** Sau **11. dữ liệu (data / 데이터) deletion kiểm tra (audit / 감사)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
