# Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Self-service, multi-tenancy, governance và FinOps**. Route đi từ delegated control → API intent → tenant isolation → cost attribution/guardrails → policy and accountability, để tự phục vụ không biến thành tự do không kiểm soát.

## 1. Self-service là delegated điều khiển (control / 제어) có ranh giới (boundary / 경계)

Self-service không nghĩa ai cũng có admin. Nó nghĩa người dùng (user / 사용자) có thể hoàn thành dùng chung (common / 공통) tác vụ (task / 작업) trong một permission envelope đã thiết kế: tạo dịch vụ (service / 서비스), cơ sở dữ liệu (database / 데이터베이스) plan, secret binding hoặc môi trường (environment / 환경) mà không chờ operator thao tác.

Nền tảng (platform / 플랫폼) nhận intent mức cao, validate chính sách (policy / 정책), thực hiện provisioning bằng automation định danh (identity / 식별자) và trả status. Đây là delegated điều khiển (control / 제어).

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **1. Self-service là delegated điều khiển (control / 제어) có ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **2. API cần thể hiện intent** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **3. Multi-tenancy là dùng chung (shared / 공유) tài nguyên (resource / 자원) + isolation đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. API cần thể hiện intent

Nếu nhà phát triển (developer / 개발자) muốn “một nội bộ (internal / 내부) HTTP dịch vụ (service / 서비스)” nhưng phải khai VPC ID, subnet, bảo mật (security / 보안) group, nút (node / 노드) selector và IAM ARN, nền tảng (platform / 플랫폼) đang expose hiện thực (implementation / 구현).

Intent-level API giảm coupling. nền tảng (platform / 플랫폼) có thể đổi underlying hiện thực (implementation / 구현) mà bên tiêu thụ (consumer / 소비자) đặc tả hợp đồng (contract / 계약) ít thay hơn.

Tuy nhiên intent phải đủ rõ cho độ tin cậy (reliability / 신뢰성)/chi phí (cost / 비용). người dùng (user / 사용자) vẫn có thể cần chọn tier, region, dữ liệu (data / 데이터) classification, expected traffic hoặc RPO/RTO.

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **2. API cần thể hiện intent** nêu điều cần giải thích; **3. Multi-tenancy là dùng chung (shared / 공유) tài nguyên (resource / 자원) + isolation đặc tả hợp đồng (contract / 계약)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Quota là sản phẩm (product / 제품) tính năng (feature / 기능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Multi-tenancy là dùng chung (shared / 공유) tài nguyên (resource / 자원) + isolation đặc tả hợp đồng (contract / 계약)

Nhiều nhóm (team / 팀) có thể dùng chung cluster, CI runner, registry hoặc khả năng quan sát (observability / 관측 가능성) backend. Multi-tenancy tiết kiệm và chuẩn hóa nhưng tạo noisy neighbor/bảo mật (security / 보안) rủi ro (risk / 위험).

Isolation có nhiều chiều: định danh (identity / 식별자)/RBAC, mạng (network / 네트워크), compute quota, lưu trữ (storage / 저장소), secret, khả năng quan sát (observability / 관측 가능성) dữ liệu (data / 데이터) và billing attribution. không gian tên (namespace / 네임스페이스) chỉ giải một phần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **3. Multi-tenancy là dùng chung (shared / 공유) tài nguyên (resource / 자원) + isolation đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **4. Quota là sản phẩm (product / 제품) tính năng (feature / 기능)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. tài nguyên (resource / 자원) fairness và noisy neighbor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Quota là sản phẩm (product / 제품) tính năng (feature / 기능)

Quota ngăn một tenant tiêu hết dùng chung (shared / 공유) sức chứa (capacity / 용량), nhưng quota quá thấp tạo hỗ trợ (support / 지원) ticket. nền tảng (platform / 플랫폼) cần default theo tải công việc (workload / 워크로드) lớp (class / 클래스) và cách yêu cầu (request / 요청) increase có reason/approval tự động phù hợp.

Quota usage phải visible cho tenant trước khi chạm limit. lỗi (error / 오류) “quota exceeded” chỉ khi deploy là phản hồi (feedback / 피드백) quá muộn.

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **4. Quota là sản phẩm (product / 제품) tính năng (feature / 기능)** nêu điều cần giải thích; **5. tài nguyên (resource / 자원) fairness và noisy neighbor** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. môi trường (environment / 환경) chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. tài nguyên (resource / 자원) fairness và noisy neighbor

Dùng chung (shared / 공유) cluster có thể gặp CPU, bộ nhớ (memory / 메모리), I/O, mạng (network / 네트워크) hoặc API-server contention. yêu cầu (request / 요청)/limit, priority, tỷ lệ (rate / 비율) limit và dedicated pool là các công cụ.

Không phải tenant nào cũng cần isolation vật lý. Chọn ranh giới (boundary / 경계) dựa trên rủi ro (risk / 위험)/compliance/hiệu năng (performance / 성능). Dedicated cluster per nhóm (team / 팀) có isolation nhưng tăng chi phí (cost / 비용)/operational surface.

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **5. tài nguyên (resource / 자원) fairness và noisy neighbor** nêu điều cần giải thích; **6. môi trường (environment / 환경) chiến lược (strategy / 전략)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. quản trị (governance / 거버넌스) bằng siêu dữ liệu (metadata / 메타데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. môi trường (environment / 환경) chiến lược (strategy / 전략)

Dev/staging/prod có thể tách account/dự án (project / 프로젝트)/cluster hoặc chia không gian tên (namespace / 네임스페이스) tùy rủi ro (risk / 위험). môi trường vận hành (production / 운영 환경) thường cần stronger ranh giới (boundary / 경계). Nhưng càng nhiều môi trường (environment / 환경) giống hệt môi trường vận hành (production / 운영 환경) càng tốn chi phí (cost / 비용) và drift rủi ro (risk / 위험).

Mục tiêu của pre-production là tạo confidence cho thay đổi (change / 변경), không phải sao chép mọi thứ vô điều kiện. Ephemeral môi trường (environment / 환경) có thể phù hợp tính năng (feature / 기능)/kiểm thử tích hợp (integration test / 통합 테스트); long-lived staging phù hợp dùng chung (shared / 공유) phụ thuộc (dependency / 의존성) kiểm thử (test / 테스트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **6. môi trường (environment / 환경) chiến lược (strategy / 전략)** nêu điều cần giải thích; **7. quản trị (governance / 거버넌스) bằng siêu dữ liệu (metadata / 메타데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. FinOps là vòng phản hồi (feedback loop / 피드백 루프) về chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. quản trị (governance / 거버넌스) bằng siêu dữ liệu (metadata / 메타데이터)

Mọi tài nguyên (resource / 자원) nên có đơn vị sở hữu (owner / 오너), môi trường (environment / 환경), dịch vụ (service / 서비스)/sản phẩm (product / 제품), chi phí (cost / 비용) center/nhóm (team / 팀), dữ liệu (data / 데이터) classification và vòng đời (lifecycle / 생명주기)/expiry khi phù hợp. siêu dữ liệu (metadata / 메타데이터) cho phép chính sách (policy / 정책), chi phí (cost / 비용) allocation và cleanup.

Nếu tài nguyên (resource / 자원) không có đơn vị sở hữu (owner / 오너), sự cố (incident / 인시던트)/bảo mật (security / 보안)/chi phí (cost / 비용) question đều khó. nền tảng (platform / 플랫폼) nên inject/require siêu dữ liệu (metadata / 메타데이터) thay vì mong người dùng (user / 사용자) nhớ tag bằng tay.

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **7. quản trị (governance / 거버넌스) bằng siêu dữ liệu (metadata / 메타데이터)** nêu điều cần giải thích; **8. FinOps là vòng phản hồi (feedback loop / 피드백 루프) về chi phí (cost / 비용)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. đơn vị (unit / 단위) economics kỹ thuật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. FinOps là vòng phản hồi (feedback loop / 피드백 루프) về chi phí (cost / 비용)

Cloud bill chỉ hữu ích khi chi phí (cost / 비용) được gắn với đơn vị sở hữu (owner / 오너) và driver. “nhóm (team / 팀) A tốn 20 triệu” chưa đủ; cần biết compute idle, dữ liệu (data / 데이터) egress, cơ sở dữ liệu (database / 데이터베이스) tier, log ingestion hay lưu trữ (storage / 저장소) retention nào gây chi phí (cost / 비용).

FinOps không phải chỉ cắt chi phí. Nó tối ưu sự đánh đổi (trade-off / 트레이드오프) chi phí (cost / 비용)–độ tin cậy (reliability / 신뢰성)–hiệu năng (performance / 성능)–velocity. Giảm replica làm bill thấp nhưng vi phạm SLO không phải tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **9. đơn vị (unit / 단위) economics kỹ thuật** tiếp nhận điểm tựa từ **8. FinOps là vòng phản hồi (feedback loop / 피드백 루프) về chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Rightsizing có bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. đơn vị (unit / 단위) economics kỹ thuật

Chỉ số (metric / 지표) chi phí (cost / 비용) trên yêu cầu (request / 요청), tenant, bản dựng (build / 빌드) minute, GB processed hoặc active người dùng (user / 사용자) giúp thấy efficiency khi quy mô (scale / 규모). Tổng bill tăng có thể là hợp lý nếu nghiệp vụ (business / 비즈니스) volume tăng nhanh hơn.

Nền tảng (platform / 플랫폼) có thể cung cấp chi phí (cost / 비용) estimate trước provisioning và actual chi phí (cost / 비용) sau sử dụng để close vòng lặp (loop / 루프).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **9. đơn vị (unit / 단위) economics kỹ thuật** nêu điều cần giải thích; **10. Rightsizing có bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Cleanup và ephemeral tài nguyên (resource / 자원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Rightsizing có bằng chứng (evidence / 증거)

CPU yêu cầu (request / 요청) lớn hơn nhiều usage có thể là waste, nhưng p99/peak và failover headroom quan trọng. Rightsizing nên dùng historical phân phối (distribution / 분포), SLO, startup thời gian (time / 시간) và autoscaling delay.

Tự động giảm tài nguyên (resource / 자원) ngay theo average có thể tạo sự cố (incident / 인시던트). Recommendation nên có confidence và staged ứng dụng (application / 애플리케이션).

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **10. Rightsizing có bằng chứng (evidence / 증거)** nêu điều cần giải thích; **11. Cleanup và ephemeral tài nguyên (resource / 자원)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. chính sách (policy / 정책) hierarchy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Cleanup và ephemeral tài nguyên (resource / 자원)

Preview môi trường (environment / 환경), temporary cơ sở dữ liệu (database / 데이터베이스) và old ảnh (image / 이미지) tạo chi phí (cost / 비용)/leak. tài nguyên (resource / 자원) tạm nên có TTL/đơn vị sở hữu (owner / 오너) mặc định. Cleanup automation phải bảo vệ môi trường vận hành (production / 운영 환경) bằng classification và tường minh (explicit / 명시적) retention chính sách (policy / 정책).

“Không ai biết tài nguyên (resource / 자원) này là gì nên không dám xóa” là dấu hiệu siêu dữ liệu (metadata / 메타데이터)/vòng đời (lifecycle / 생명주기) thiết kế (design / 설계) yếu.

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **11. Cleanup và ephemeral tài nguyên (resource / 자원)** nêu điều cần giải thích; **12. chính sách (policy / 정책) hierarchy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. nhà phát triển (developer / 개발자) autonomy và guardrail** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. chính sách (policy / 정책) hierarchy

Organization có toàn cục (global / 전역) chính sách (policy / 정책); nền tảng (platform / 플랫폼) có default; nhóm (team / 팀) có cấu hình (config / 설정) trong allowed phạm vi (range / 범위); tải công việc (workload / 워크로드) có thời gian chạy (runtime / 런타임) trạng thái (state / 상태). giải quyết xung đột (conflict resolution / 충돌 해결) phải rõ.

Nếu central chính sách (policy / 정책) thay đổi breaking hành vi (behavior / 동작), rollout cần staged/canary. chính sách (policy / 정책) cũng là môi trường vận hành (production / 운영 환경) mã (code / 코드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **13. nhà phát triển (developer / 개발자) autonomy và guardrail** tiếp nhận điểm tựa từ **12. chính sách (policy / 정책) hierarchy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. cấp cao (senior / 시니어) ghi chú (note / 노트): dùng chung (shared / 공유) nền tảng (platform / 플랫폼) cần economics và độ tin cậy (reliability / 신뢰성) cùng lúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. nhà phát triển (developer / 개발자) autonomy và guardrail

Autonomy tốt không phải cho mọi người toàn quyền, mà là cho quyền quyết định gần ngữ cảnh (context / 맥락) trong ranh giới (boundary / 경계) an toàn. nền tảng (platform / 플랫폼) encode dùng chung (common / 공통) ràng buộc (constraint / 제약조건); nhóm (team / 팀) quyết định business-specific choice.

Khi exception cần nhiều lần, có thể golden đường dẫn (path / 경로) đang thiếu use trường hợp (case / 사례) chứ không phải người dùng (user / 사용자) “không tuân thủ”. nền tảng (platform / 플랫폼) sản phẩm (product / 제품) discovery phải học từ exception.

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **14. cấp cao (senior / 시니어) ghi chú (note / 노트): dùng chung (shared / 공유) nền tảng (platform / 플랫폼) cần economics và độ tin cậy (reliability / 신뢰성) cùng lúc** tiếp nhận điểm tựa từ **13. nhà phát triển (developer / 개발자) autonomy và guardrail** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Isolation phải được mô tả theo thất bại (failure / 실패) và threat mô hình (model / 모델), không theo tên tài nguyên (resource / 자원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. cấp cao (senior / 시니어) ghi chú (note / 노트): dùng chung (shared / 공유) nền tảng (platform / 플랫폼) cần economics và độ tin cậy (reliability / 신뢰성) cùng lúc

Multi-tenancy tăng utilization nhưng blast radius tăng. Dedicated tài nguyên (resource / 자원) giảm coupling nhưng chi phí (cost / 비용)/toil tăng. Quyết định tenancy phải xem tải công việc (workload / 워크로드) criticality, compliance, scaling mẫu (pattern / 패턴) và nhóm (team / 팀) maturity.

Không có topology “chuẩn cho mọi công ty”. Có đặc tả hợp đồng (contract / 계약) rõ và bằng chứng (evidence / 증거) để điều chỉnh mới là maturity.

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **14. cấp cao (senior / 시니어) ghi chú (note / 노트): dùng chung (shared / 공유) nền tảng (platform / 플랫폼) cần economics và độ tin cậy (reliability / 신뢰성) cùng lúc** nêu điều cần giải thích; **15. Isolation phải được mô tả theo thất bại (failure / 실패) và threat mô hình (model / 모델), không theo tên tài nguyên (resource / 자원)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. dùng chung (shared / 공유) điều khiển (control / 제어) plane là một tài nguyên cần quota riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Isolation phải được mô tả theo thất bại (failure / 실패) và threat mô hình (model / 모델), không theo tên tài nguyên (resource / 자원)

Hai tenant ở hai không gian tên (namespace / 네임스페이스) có thể vẫn chia nút (node / 노드) kernel, CNI mặt phẳng dữ liệu (data plane / 데이터 플레인), ingress controller, DNS, API máy chủ (server / 서버), registry và khả năng quan sát (observability / 관측 가능성) backend. Vì vậy câu “đã tách không gian tên (namespace / 네임스페이스)” chưa trả lời được tenant A có thể ảnh hưởng tenant B ra sao.

Hãy hỏi theo từng thất bại (failure / 실패) lớp (class / 클래스): A có thể ăn hết CPU/bộ nhớ (memory / 메모리)/I/O không; tạo quá nhiều đối tượng (object / 객체) có làm API máy chủ (server / 서버) chậm không; log cardinality có làm khả năng quan sát (observability / 관측 가능성) backend quá tải không; chính sách mạng (network policy / 네트워크 정책) có ngăn dữ liệu (data / 데이터) đường dẫn (path / 경로) không; secret/kiểm tra (audit / 감사)/log truy vấn (query / 쿼리) có bị đọc chéo tenant không.

Nếu một tải công việc (workload / 워크로드) có compliance hoặc hostile-code rủi ro (risk / 위험) cao, logical isolation có thể không đủ; dedicated nút (node / 노드)/account/cluster hoặc sandbox ranh giới (boundary / 경계) mạnh hơn có thể hợp lý dù chi phí (cost / 비용) cao hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **15. Isolation phải được mô tả theo thất bại (failure / 실패) và threat mô hình (model / 모델), không theo tên tài nguyên (resource / 자원)** nêu điều cần giải thích; **16. dùng chung (shared / 공유) điều khiển (control / 제어) plane là một tài nguyên cần quota riêng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Quota cần phân biệt hard ceiling và planning tín hiệu (signal / 신호)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. dùng chung (shared / 공유) điều khiển (control / 제어) plane là một tài nguyên cần quota riêng

Nhóm (team / 팀) thường nhìn CPU/bộ nhớ (memory / 메모리) tải công việc (workload / 워크로드) nhưng quên control-plane tài nguyên (resource / 자원). Một tenant tạo hàng trăm nghìn đối tượng (object / 객체), sự kiện (event / 이벤트), watch hoặc GitOps reconciliation có thể làm API máy chủ (server / 서버)/controller/etcd pressure tăng dù ứng dụng (application / 애플리케이션) yêu cầu (request / 요청) vẫn ít.

Nền tảng (platform / 플랫폼) nên đặt ranh giới (boundary / 경계) cho đối tượng (object / 객체) count, API tỷ lệ (rate / 비율), concurrent reconciliation và automation fan-out khi cần. Multi-tenancy fairness phải bảo vệ cả **điều khiển (control / 제어) plane** lẫn mặt phẳng dữ liệu (data plane / 데이터 플레인).

Đây cũng là lý do “mỗi nhóm (team / 팀) tự chạy controller tùy ý trong dùng chung (shared / 공유) cluster” cần quản trị (governance / 거버넌스) về permission và tải (load / 로드), không chỉ bảo mật (security / 보안).

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **17. Quota cần phân biệt hard ceiling và planning tín hiệu (signal / 신호)** tiếp nhận điểm tựa từ **16. dùng chung (shared / 공유) điều khiển (control / 제어) plane là một tài nguyên cần quota riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Showback và chargeback tạo incentive khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Quota cần phân biệt hard ceiling và planning tín hiệu (signal / 신호)

Một hard quota bảo vệ dùng chung (shared / 공유) tài nguyên (resource / 자원) bằng cách từ chối công việc (work / 작업) mới khi chạm giới hạn. Nhưng sức chứa (capacity / 용량) planning còn cần soft threshold để cảnh báo trước. Nếu tenant chỉ biết vấn đề khi triển khai (deployment / 배포) bị reject, phản hồi (feedback / 피드백) đã quá muộn.

Self-service tốt hiển thị hiện tại (current / 현재) usage, forecast và headroom ngay lúc người dùng (user / 사용자) chọn tier hoặc quy mô (scale / 규모). Quota increase có thể tự động khi nằm trong chính sách (policy / 정책) và sức chứa (capacity / 용량) còn đủ; chỉ exception lớn mới cần human quyết định (decision / 결정).

Quota cũng phải xét dạng thất bại (failure mode / 실패 모드). Nếu môi trường vận hành (production / 운영 환경) chạy bình thường ở 80% quota nhưng failover cần gấp đôi replica, quota hiện tại có thể chặn chính khôi phục (recovery / 복구) đường dẫn (path / 경로).

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **18. Showback và chargeback tạo incentive khác nhau** tiếp nhận điểm tựa từ **17. Quota cần phân biệt hard ceiling và planning tín hiệu (signal / 신호)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. đơn vị (unit / 단위) chi phí (cost / 비용) chỉ hữu ích khi denominator có nghĩa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Showback và chargeback tạo incentive khác nhau

Showback cho nhóm (team / 팀) thấy chi phí họ tạo nhưng chưa chuyển chi phí đó vào ngân sách trực tiếp. Chargeback phân bổ chi phí (cost / 비용) thật về đơn vị sử dụng. Cả hai đều là phản hồi (feedback / 피드백) cơ chế (mechanism / 메커니즘); không phải tổ chức nào cũng cần chargeback cứng.

Nếu chi phí (cost / 비용) allocation thiếu shared-cost mô hình (model / 모델), nhóm (team / 팀) có thể tối ưu cục bộ nhưng nền tảng (platform / 플랫폼) bill vẫn lớn. dùng chung (shared / 공유) ingress, khả năng quan sát (observability / 관측 가능성), cluster điều khiển (control / 제어) plane và mạng (network / 네트워크) backbone cần cách phân bổ minh bạch: theo usage driver, tỷ lệ cố định hoặc coi là central investment tùy mục tiêu.

Mục tiêu là tạo quyết định tốt hơn, không phải làm hóa đơn nội bộ đẹp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **19. đơn vị (unit / 단위) chi phí (cost / 비용) chỉ hữu ích khi denominator có nghĩa** tiếp nhận điểm tựa từ **18. Showback và chargeback tạo incentive khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Commitment/discount không sửa được tài nguyên (resource / 자원) waste** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. đơn vị (unit / 단위) chi phí (cost / 비용) chỉ hữu ích khi denominator có nghĩa

`cost/request` giảm có thể vì tải công việc (workload / 워크로드) hiệu quả hơn, nhưng cũng có thể vì traffic bot/cache-hit rẻ tăng mạnh. `cost/user` có thể méo nếu người dùng (user / 사용자) activity rất khác nhau.

Do đó đơn vị (unit / 단위) economics cần chọn denominator gần giá trị (value / 값)/công việc (work / 작업) thực: completed thứ tự (order / 순서), GB processed, successful bản dựng (build / 빌드), active tenant hoặc nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션). Phải giữ chất lượng (quality / 품질) guardrail như SLO/lỗi (error / 오류) tỷ lệ (rate / 비율); nếu giảm chi phí (cost / 비용) bằng cách reject nhiều yêu cầu (request / 요청), đơn vị (unit / 단위) chi phí (cost / 비용) của yêu cầu (request / 요청) thành công có thể nhìn đẹp giả tạo.

Cấp cao (senior / 시니어) FinOps luôn hỏi numerator và denominator đã thay đổi vì kiến trúc (architecture / 아키텍처), price hay traffic mix.

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **19. đơn vị (unit / 단위) chi phí (cost / 비용) chỉ hữu ích khi denominator có nghĩa** nêu điều cần giải thích; **20. Commitment/discount không sửa được tài nguyên (resource / 자원) waste** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. chi phí (cost / 비용) anomaly phải nối lại thay đổi (change / 변경) telemetry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Commitment/discount không sửa được tài nguyên (resource / 자원) waste

Reserved sức chứa (capacity / 용량), savings plan hoặc volume discount có thể giảm đơn giá nhưng không loại bỏ idle kiến trúc (architecture / 아키텍처). Nếu lần ghi nhận (commit / 커밋) dựa trên peak ngắn hạn rồi demand giảm, tổ chức chỉ chuyển waste thành hợp đồng dài hạn.

Thứ tự lập luận (reasoning / 추론) tốt là hiểu baseline/seasonality, rightsizing và kiến trúc (architecture / 아키텍처) trước, sau đó mới quyết định phần usage ổn định nào đáng lần ghi nhận (commit / 커밋). Discount chiến lược (strategy / 전략) là financial tối ưu hóa (optimization / 최적화) trên tải công việc (workload / 워크로드) đã hiểu, không thay thế kỹ thuật (engineering / 엔지니어링) tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **20. Commitment/discount không sửa được tài nguyên (resource / 자원) waste** nêu điều cần giải thích; **21. chi phí (cost / 비용) anomaly phải nối lại thay đổi (change / 변경) telemetry** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. Self-service deletion cần mạnh như self-service creation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. chi phí (cost / 비용) anomaly phải nối lại thay đổi (change / 변경) telemetry

Một bill tăng đột ngột thường có nhân quả (causal / 인과적) sự kiện (event / 이벤트): bản phát hành (release / 릴리스) bật gỡ lỗi (debug / 디버그) log, thử lại (retry / 재시도) storm tăng egress, retention chính sách (policy / 정책) đổi, preview môi trường (environment / 환경) không cleanup hoặc autoscaler stuck.

Chi phí (cost / 비용) monitoring có giá trị hơn khi có dimension đơn vị sở hữu (owner / 오너)/dịch vụ (service / 서비스)/môi trường (environment / 환경) và triển khai (deployment / 배포)/cấu hình (config / 설정) sự kiện (event / 이벤트). Khi daily log chi phí (cost / 비용) tăng 4 lần sau bản phát hành (release / 릴리스) R, operator có thể drill từ FinOps tín hiệu (signal / 신호) sang telemetry/bản phát hành (release / 릴리스) thay vì chờ cuối tháng.

Chi phí (cost / 비용) vì vậy cũng là khả năng quan sát (observability / 관측 가능성) tín hiệu (signal / 신호) của nền tảng (platform / 플랫폼).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **22. Self-service deletion cần mạnh như self-service creation** tiếp nhận điểm tựa từ **21. chi phí (cost / 비용) anomaly phải nối lại thay đổi (change / 변경) telemetry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. cấp cao (senior / 시니어) walkthrough: dùng chung (shared / 공유) cluster rẻ hơn nhưng một nhóm (team / 팀) làm toàn nền tảng (platform / 플랫폼) chậm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Self-service deletion cần mạnh như self-service creation

Nền tảng (platform / 플랫폼) thường tối ưu “Create” nhưng vòng đời (lifecycle / 생명주기) thật còn resize, rotate, migrate, suspend và delete. Nếu tạo cơ sở dữ liệu (database / 데이터베이스) mất 5 phút nhưng xóa cần ticket hai tuần, tài nguyên (resource / 자원) leak là hệ quả thiết kế chứ không phải người dùng (user / 사용자) lười.

Deletion cần an toàn (safety / 안전): phụ thuộc (dependency / 의존성) discovery, retention/backup chính sách (policy / 정책), grace period hoặc approval theo criticality. Nhưng dùng chung (common / 공통) ephemeral tài nguyên (resource / 자원) nên có TTL và cleanup đường dẫn (path / 경로) mặc định.

Day-2 thao tác (operation / 연산) mới quyết định nền tảng (platform / 플랫폼) có thật sự self-service hay chỉ là provisioning portal.

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **23. cấp cao (senior / 시니어) walkthrough: dùng chung (shared / 공유) cluster rẻ hơn nhưng một nhóm (team / 팀) làm toàn nền tảng (platform / 플랫폼) chậm** tiếp nhận điểm tựa từ **22. Self-service deletion cần mạnh như self-service creation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Fairness khác với quota: ai được phục vụ khi tài nguyên (resource / 자원) khan hiếm?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. cấp cao (senior / 시니어) walkthrough: dùng chung (shared / 공유) cluster rẻ hơn nhưng một nhóm (team / 팀) làm toàn nền tảng (platform / 플랫폼) chậm

Giả sử nhóm (team / 팀) analytics tạo hàng chục nghìn short-lived Job mỗi giờ. CPU ứng dụng (application / 애플리케이션) vẫn còn headroom nhưng API máy chủ (server / 서버) độ trễ (latency / 지연 시간), scheduler hàng đợi (queue / 큐) và sự kiện (event / 이벤트) volume tăng; các nhóm (team / 팀) khác thấy triển khai (deployment / 배포) chậm và HPA cập nhật (update / 업데이트) trễ.

Nếu chỉ nhìn không gian tên (namespace / 네임스페이스) CPU quota, tenant analytics “không vi phạm”. thất bại (failure / 실패) nằm ở dùng chung (shared / 공유) control-plane tài nguyên (resource / 자원) chưa được accounting.

Mitigation có thể rate-limit creation, batch công việc (work / 작업), tách tải công việc (workload / 워크로드) lớp (class / 클래스) sang cluster/pool riêng hoặc tăng control-plane sức chứa (capacity / 용량). Long-term đặc tả hợp đồng (contract / 계약) cần quota theo đối tượng (object / 객체)/API hành vi (behavior / 동작) và SLO nền tảng (platform / 플랫폼). Đây là lý do multi-tenancy economics phải tính externality, không chỉ utilization compute.

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **23. cấp cao (senior / 시니어) walkthrough: dùng chung (shared / 공유) cluster rẻ hơn nhưng một nhóm (team / 팀) làm toàn nền tảng (platform / 플랫폼) chậm** nêu điều cần giải thích; **24. Fairness khác với quota: ai được phục vụ khi tài nguyên (resource / 자원) khan hiếm?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. Isolation mức (level / 수준) nên được chọn theo blast-radius ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Fairness khác với quota: ai được phục vụ khi tài nguyên (resource / 자원) khan hiếm?

Quota trả lời tenant có thể sở hữu tối đa bao nhiêu tài nguyên (resource / 자원); fairness trả lời khi nhiều tenant cùng tranh tài nguyên (resource / 자원) tại một thời điểm thì scheduler/hàng đợi (queue / 큐) phân phối ra sao. Hai tenant đều ở dưới quota vẫn có thể gây starvation nếu một tenant luôn submit công việc (work / 작업) trước hoặc giữ liên kết (connection / 연결) lâu.

Dùng chung (shared / 공유) CI runner, triển khai (deployment / 배포) hàng đợi (queue / 큐), API máy chủ (server / 서버) và cơ sở dữ liệu (database / 데이터베이스) proxy đều cần fairness mô hình (model / 모델). Có thể dùng weighted hàng đợi (queue / 큐), priority lớp (class / 클래스), per-tenant tính đồng thời (concurrency / 동시성) hoặc reservation. Không có một thuật toán universal; đặc tả hợp đồng (contract / 계약) phải phản ánh nghiệp vụ (business / 비즈니스) criticality mà vẫn tránh tenant priority cao chiếm mọi sức chứa (capacity / 용량) vô thời hạn.

Fairness chỉ số (metric / 지표) nên nhìn wait thời gian (time / 시간)/dịch vụ (service / 서비스) tỷ lệ (rate / 비율) theo tenant hoặc tải công việc (workload / 워크로드) lớp (class / 클래스), không chỉ aggregate thông lượng (throughput / 처리량). Aggregate 10.000 job/giờ có thể che việc một nhóm (team / 팀) chờ 40 phút còn nhóm (team / 팀) khác gần như không chờ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **24. Fairness khác với quota: ai được phục vụ khi tài nguyên (resource / 자원) khan hiếm?** nêu điều cần giải thích; **25. Isolation mức (level / 수준) nên được chọn theo blast-radius ngân sách (budget / 예산)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **26. Tenant-aware SLO ngăn aggregate chỉ số (metric / 지표) che unfairness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Isolation mức (level / 수준) nên được chọn theo blast-radius ngân sách (budget / 예산)

Thay vì hỏi “dùng chung (shared / 공유) hay dedicated?”, hãy hỏi organization chấp nhận một thất bại (failure / 실패) ảnh hưởng tối đa bao nhiêu tải công việc (workload / 워크로드)/tenant. Từ đó mới chọn cell, account, cluster, nút (node / 노드) pool, ingress hay khả năng quan sát (observability / 관측 가능성) partition phù hợp.

Ví dụ tải công việc (workload / 워크로드) Tier-0 có thể cần cell riêng vì một chính sách (policy / 정책) rollout hoặc noisy tenant không được ảnh hưởng nó; tải công việc (workload / 워크로드) nội bộ (internal / 내부) low-criticality có thể share mạnh hơn để tăng utilization. Isolation là một độ tin cậy (reliability / 신뢰성)/economic tier, không chỉ bảo mật (security / 보안) option.

Nền tảng (platform / 플랫폼) danh mục (catalog / 카탈로그) có thể encode `isolationClass` hoặc `criticalityTier` ở mức intent. người dùng (user / 사용자) không cần chọn raw topology, nhưng đặc tả hợp đồng (contract / 계약) phải nói blast radius và hỗ trợ (support / 지원) expectation tương ứng.

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **26. Tenant-aware SLO ngăn aggregate chỉ số (metric / 지표) che unfairness** tiếp nhận điểm tựa từ **25. Isolation mức (level / 수준) nên được chọn theo blast-radius ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. khôi phục (recovery / 복구) sức chứa (capacity / 용량) là một dùng chung (shared / 공유) tài nguyên (resource / 자원) cần reservation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Tenant-aware SLO ngăn aggregate chỉ số (metric / 지표) che unfairness

Một dùng chung (shared / 공유) nền tảng (platform / 플랫폼) có thể đạt 99.9% aggregate success nhưng một tenant nhỏ bị lỗi 20% nếu traffic tenant lớn thống trị denominator. Vì vậy ngoài toàn cục (global / 전역) SLO, cần slice theo tenant lớp (class / 클래스), region hoặc trọng yếu (critical / 중요) journey khi đó là ranh giới (boundary / 경계) sản phẩm (product / 제품) quan trọng.

Không nên tạo SLO riêng cho hàng nghìn tenant nếu operational chi phí (cost / 비용) quá lớn; có thể dùng cohort/tier hoặc fairness guardrail. Mục tiêu là phát hiện systematic isolation thất bại (failure / 실패) mà aggregate chỉ số (metric / 지표) che mất.

Đây cũng áp dụng cho provisioning độ trễ (latency / 지연 시간): median toàn nền tảng (platform / 플랫폼) thấp không có ý nghĩa nếu một account/region luôn bị hàng đợi (queue / 큐) starvation.

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **26. Tenant-aware SLO ngăn aggregate chỉ số (metric / 지표) che unfairness** nêu điều cần giải thích; **27. khôi phục (recovery / 복구) sức chứa (capacity / 용량) là một dùng chung (shared / 공유) tài nguyên (resource / 자원) cần reservation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **28. chi phí (cost / 비용) allocation phải tính externality chứ không chỉ tài nguyên (resource / 자원) sở hữu trực tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. khôi phục (recovery / 복구) sức chứa (capacity / 용량) là một dùng chung (shared / 공유) tài nguyên (resource / 자원) cần reservation

Trong sự cố (incident / 인시던트), nhiều tenant có thể cùng cần quy mô (scale / 규모), recreate pod, restore cơ sở dữ liệu (database / 데이터베이스) hoặc pull ảnh (image / 이미지). Nếu nền tảng (platform / 플랫폼) chỉ sức chứa (capacity / 용량) cho steady trạng thái (state / 상태), khôi phục (recovery / 복구) fan-out có thể làm registry, API máy chủ (server / 서버), nút (node / 노드) provisioning hoặc backup dịch vụ (service / 서비스) saturation đúng lúc cần nhất.

Sức chứa (capacity / 용량) planning multi-tenant nên có **khôi phục (recovery / 복구) tính đồng thời (concurrency / 동시성) ngân sách (budget / 예산)**: bao nhiêu tải công việc (workload / 워크로드) có thể restart/reconcile/restore đồng thời mà điều khiển (control / 제어) plane và phụ thuộc (dependency / 의존성) vẫn giữ SLO. Game day nên kiểm thử (test / 테스트) burst khôi phục (recovery / 복구), không chỉ normal traffic.

Điều này giải thích vì sao overcommit quá mạnh hoặc quota “vừa đủ ngày thường” có thể biến một thất bại (failure / 실패) nhỏ thành khôi phục (recovery / 복구) storm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **27. khôi phục (recovery / 복구) sức chứa (capacity / 용량) là một dùng chung (shared / 공유) tài nguyên (resource / 자원) cần reservation** nêu điều cần giải thích; **28. chi phí (cost / 비용) allocation phải tính externality chứ không chỉ tài nguyên (resource / 자원) sở hữu trực tiếp** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **29. Idle sức chứa (capacity / 용량) không luôn là waste nếu nó mua được option giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. chi phí (cost / 비용) allocation phải tính externality chứ không chỉ tài nguyên (resource / 자원) sở hữu trực tiếp

Một tenant có thể dùng ít CPU nhưng tạo log cardinality cực cao, egress lớn, API yêu cầu (request / 요청) storm hoặc nhiều short-lived đối tượng (object / 객체) khiến dùng chung (shared / 공유) dịch vụ (service / 서비스) phải quy mô (scale / 규모). Nếu chargeback chỉ dựa trên CPU/RAM, incentive bị lệch.

Không nhất thiết billing phải chính xác tuyệt đối từng byte. Quan trọng là chọn driver đủ gần nhân quả (causal / 인과적) chi phí (cost / 비용): ingestion GB, retained GB-day, egress, bản dựng (build / 빌드) minute, đối tượng (object / 객체)/API volume hoặc dedicated sức chứa (capacity / 용량) reservation.

Khi externality không được visible, nhóm (team / 팀) gây chi phí (cost / 비용) có ít phản hồi (feedback / 피드백) để tối ưu còn central nền tảng (platform / 플랫폼) phải hấp thụ bill và toil.

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **28. chi phí (cost / 비용) allocation phải tính externality chứ không chỉ tài nguyên (resource / 자원) sở hữu trực tiếp** nêu điều cần giải thích; **29. Idle sức chứa (capacity / 용량) không luôn là waste nếu nó mua được option giá trị (value / 값)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **30. quản trị (governance / 거버넌스) tốt cần vòng đời (lifecycle / 생명주기) cho chính chính sách (policy / 정책) và exception** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Idle sức chứa (capacity / 용량) không luôn là waste nếu nó mua được option giá trị (value / 값)

Sức chứa (capacity / 용량) chưa dùng có thể là headroom cho failover, rollout, sự cố (incident / 인시던트) khôi phục (recovery / 복구) hoặc seasonal spike. FinOps nhìn utilization thấp rồi cắt toàn bộ spare sức chứa (capacity / 용량) có thể phá độ tin cậy (reliability / 신뢰성) đặc tả hợp đồng (contract / 계약).

Cần phân biệt **unowned idle** — tài nguyên (resource / 자원) thừa do yêu cầu (request / 요청) sai hoặc vòng đời (lifecycle / 생명주기) leak — với **intentional reserve** — sức chứa (capacity / 용량) được giữ vì thất bại (failure / 실패) mô hình (model / 모델)/SLO. siêu dữ liệu (metadata / 메타데이터) và sức chứa (capacity / 용량) mô hình (model / 모델) nên làm reserve tường minh (explicit / 명시적) để chi phí (cost / 비용) rà soát (review / 검토) không nhầm nó với waste.

Cấp cao (senior / 시니어) discussion về chi phí (cost / 비용) nên hỏi “tài nguyên (resource / 자원) này mua năng lực (capability / 역량) gì?” thay vì “tại sao utilization không 90%?”.

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **29. Idle sức chứa (capacity / 용량) không luôn là waste nếu nó mua được option giá trị (value / 값)** xác định đầu vào; **30. quản trị (governance / 거버넌스) tốt cần vòng đời (lifecycle / 생명주기) cho chính chính sách (policy / 정책) và exception** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. Reservation và borrowing cần reclamation ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. quản trị (governance / 거버넌스) tốt cần vòng đời (lifecycle / 생명주기) cho chính chính sách (policy / 정책) và exception

Chính sách (policy / 정책) có đơn vị sở hữu (owner / 오너), phiên bản (version / 버전), rollout ring, telemetry, deprecation và quay lui (rollback / 롤백) giống software. Exception cũng là tài nguyên (resource / 자원): có requester, reason, phạm vi (scope / 범위), expiry, reviewer và bằng chứng (evidence / 증거) cho việc gia hạn.

Nếu exception không bao giờ hết hạn, chính sách (policy / 정책) dần trở thành nominal. Nếu chính sách (policy / 정책) không có di chuyển (migration / 마이그레이션) đường dẫn (path / 경로), nền tảng (platform / 플랫폼) tạo shadow workflow và bypass. quản trị (governance / 거버넌스) trưởng thành tối ưu **rủi ro (risk / 위험) reduction trên luồng (flow / 흐름)**, không tối đa số quy tắc (rule / 규칙).

Một tín hiệu (signal / 신호) tốt là exception tỷ lệ (rate / 비율) theo chính sách (policy / 정책). Nếu một quy tắc (rule / 규칙) liên tục cần exception hợp lệ, quy tắc (rule / 규칙) hoặc golden đường dẫn (path / 경로) có thể đang mô hình (model / 모델) sai thực tế và cần sản phẩm (product / 제품) discovery lại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **30. quản trị (governance / 거버넌스) tốt cần vòng đời (lifecycle / 생명주기) cho chính chính sách (policy / 정책) và exception** xác định đầu vào; **31. Reservation và borrowing cần reclamation ngữ nghĩa (semantics / 의미론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **32. Preemption là chính sách (policy / 정책) về ai chịu thiệt khi scarcity xảy ra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Reservation và borrowing cần reclamation ngữ nghĩa (semantics / 의미론)

Dùng chung (shared / 공유) nền tảng (platform / 플랫폼) thường muốn vừa bảo đảm sức chứa (capacity / 용량) cho tải công việc (workload / 워크로드) trọng yếu (critical / 중요) vừa cho tải công việc (workload / 워크로드) khác mượn phần đang rảnh để tăng utilization. Borrowing có ích, nhưng nếu không có reclamation đặc tả hợp đồng (contract / 계약) thì “sức chứa (capacity / 용량) dự phòng” chỉ tồn tại trên giấy: khi Tier-0 cần quy mô (scale / 규모), batch job đang mượn tài nguyên (resource / 자원) có thể không nhả đủ nhanh.

Đặc tả hợp đồng (contract / 계약) cần nói tài nguyên (resource / 자원) nào reserved, ai được borrow, khi nào bị reclaim, tải công việc (workload / 워크로드) bị preempt có checkpoint/resume được không và thời gian thu hồi có phù hợp RTO không. Một batch job mất 20 phút để shutdown không phải spare sức chứa (capacity / 용량) hữu ích cho failover cần 2 phút.

Vì vậy headroom phải đo ở **recoverable sức chứa (capacity / 용량)**, không chỉ free sức chứa (capacity / 용량). Game day nên chứng minh borrowed tài nguyên (resource / 자원) thực sự có thể được reclaim trong deadline.

> **Chuyển mạch:** Trong **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **32. Preemption là chính sách (policy / 정책) về ai chịu thiệt khi scarcity xảy ra** tiếp nhận điểm tựa từ **31. Reservation và borrowing cần reclamation ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Isolation mạnh hơn làm giảm pooling efficiency và tăng fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Preemption là chính sách (policy / 정책) về ai chịu thiệt khi scarcity xảy ra

Priority lớp (class / 클래스) chỉ có ý nghĩa khi organization chấp nhận tải công việc (workload / 워크로드) thấp hơn bị delay/evict để bảo vệ tải công việc (workload / 워크로드) cao hơn. Nếu mọi tải công việc (workload / 워크로드) đều gắn priority cao nhất, chính sách (policy / 정책) mất tác dụng. Nếu preemption giết stateful/batch công việc (work / 작업) không checkpoint, khôi phục (recovery / 복구) chi phí (cost / 비용) có thể lớn hơn lợi ích.

Thiết kế priority cần nối nghiệp vụ (business / 비즈니스) criticality với thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론): request-serving Tier-0 có thể giữ reserved tính đồng thời (concurrency / 동시성); batch low-priority có thể pause; background cleanup có thể shed; bảo mật (security / 보안)/khôi phục (recovery / 복구) điều khiển (control / 제어) công việc (work / 작업) có thể cần lane riêng. Sau preemption phải có thử lại (retry / 재시도)/backoff để tránh tất cả tải công việc (workload / 워크로드) thấp cùng quay lại tạo thundering herd.

Scarcity chính sách (policy / 정책) tốt trả lời trước sự cố (incident / 인시던트): **ai được phục vụ, ai chờ, ai bị hủy, và trạng thái của công việc (work / 작업) bị hủy được phục hồi thế nào**.

> **Chuyển mạch:** Ở chặng này của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **33. Isolation mạnh hơn làm giảm pooling efficiency và tăng fragmentation** tiếp nhận điểm tựa từ **32. Preemption là chính sách (policy / 정책) về ai chịu thiệt khi scarcity xảy ra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Tenant isolation cần kiểm tra cả khôi phục (recovery / 복구) đường dẫn (path / 경로) và operator đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Isolation mạnh hơn làm giảm pooling efficiency và tăng fragmentation

Tách tenant thành nhiều cluster/cell/account giảm blast radius nhưng sức chứa (capacity / 용량) không còn pooling hoàn toàn. Mỗi cell phải giữ headroom riêng, tải công việc (workload / 워크로드) nhỏ có thể không tận dụng hết nút (node / 노드)/cơ sở dữ liệu (database / 데이터베이스) tier và operator phải duy trì nhiều điều khiển (control / 제어) plane hơn.

Đây là sự đánh đổi (trade-off / 트레이드오프) cấu trúc, không phải lý do tránh isolation. Quyết định đúng cần so `blast-radius reduction + compliance + predictable performance` với `fragmentation + duplicated reserve + operational surface`. Một Tier-0 có thể đáng trả chi phí (cost / 비용) đó; hàng trăm tải công việc (workload / 워크로드) dev nhỏ có thể không.

FinOps vì vậy phải hiểu topology. So đơn giá CPU giữa dùng chung (shared / 공유) và dedicated mà bỏ qua thất bại (failure / 실패) ngân sách (budget / 예산)/hỗ trợ (support / 지원) burden sẽ cho kết luận sai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Self-service, multi-tenancy, quản trị (governance / 거버넌스) và FinOps**, **33. Isolation mạnh hơn làm giảm pooling efficiency và tăng fragmentation** xác định đầu vào; **34. Tenant isolation cần kiểm tra cả khôi phục (recovery / 복구) đường dẫn (path / 경로) và operator đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 34. Tenant isolation cần kiểm tra cả khôi phục (recovery / 복구) đường dẫn (path / 경로) và operator đường dẫn (path / 경로)

Hai tenant có thể được tách tốt ở steady trạng thái (state / 상태) nhưng dùng chung break-glass admin, restore bucket, registry mirror hoặc khôi phục (recovery / 복구) hàng đợi (queue / 큐). Khi sự cố (incident / 인시던트), operator dùng quyền rộng hoặc restore nhiều tenant qua cùng chuỗi xử lý (pipeline / 파이프라인) có thể phá ranh giới (boundary / 경계) vốn tồn tại lúc bình thường.

Threat/thất bại (failure / 실패) mô hình (model / 모델) nên hỏi cả Day-2: backup của tenant A có thể restore nhầm sang tenant B không; hỗ trợ (support / 지원) engineer có thể truy vấn (query / 쿼리) log chéo tenant không; emergency công cụ (tool / 도구) có kiểm tra (audit / 감사)/mục tiêu (target / 대상) confirmation không; bulk khôi phục (recovery / 복구) của A có starve B không.

Isolation trưởng thành là thuộc tính (property / 속성) của toàn vòng đời (lifecycle / 생명주기) `create → run → observe → recover → delete`, không chỉ không gian tên (namespace / 네임스페이스)/chính sách mạng (network policy / 네트워크 정책) lúc tải công việc (workload / 워크로드) đang khỏe.

> **Bàn giao:** Sau **34. Tenant isolation cần kiểm tra cả khôi phục (recovery / 복구) đường dẫn (path / 경로) và operator đường dẫn (path / 경로)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
