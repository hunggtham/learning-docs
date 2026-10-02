# Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Cloud primitives: identity, network, compute, storage và shared responsibility**. Route đi từ trust boundary → identity/access → network placement → compute/storage primitives → provider/customer controls, để cloud được đọc qua ranh giới trách nhiệm.

## 1. Cloud không xóa hạ tầng, nó chuyển ranh giới (boundary / 경계) điều khiển

Công khai (public / 공개) cloud biến nhiều năng lực (capability / 역량) hạ tầng thành API. Thay vì mua máy chủ (server / 서버), cắm switch và cấu hình lưu trữ (storage / 저장소) bằng ticket, engineer gọi điều khiển (control / 제어) plane để yêu cầu compute, mạng (network / 네트워크), cơ sở dữ liệu (database / 데이터베이스) hoặc hàng đợi (queue / 큐). Điều thay đổi lớn nhất không chỉ là location của máy chủ mà là **hạ tầng (infrastructure / 인프라) trở thành programmable tài nguyên (resource / 자원) có vòng đời (lifecycle / 생명주기) nhanh hơn**.

Điều này làm IaC, định danh (identity / 식별자) và chính sách (policy / 정책) quan trọng hơn. Khi một API lời gọi (call / 호출) có thể tạo hàng trăm tài nguyên (resource / 자원) hoặc mở mạng (network / 네트워크) ra Internet, automation cần guardrail tương xứng.

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **1. Cloud không xóa hạ tầng, nó chuyển ranh giới (boundary / 경계) điều khiển** đã nêu tiêu chí phân biệt, còn **2. dùng chung (shared / 공유) responsibility là ranh giới (boundary / 경계), không phải khẩu hiệu** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **3. định danh (identity / 식별자) là perimeter mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. dùng chung (shared / 공유) responsibility là ranh giới (boundary / 경계), không phải khẩu hiệu

Cloud provider sở hữu một phần ngăn xếp (stack / 스택); customer sở hữu phần còn lại. ranh giới (boundary / 경계) thay đổi theo dịch vụ (service / 서비스) mô hình (model / 모델). Với VM, customer thường chịu OS patch, tiến trình (process / 프로세스) và nhiều mạng (network / 네트워크) cấu hình (configuration / 구성). Với managed cơ sở dữ liệu (database / 데이터베이스), provider quản nhiều phần OS/cơ sở dữ liệu (database / 데이터베이스) engine nhưng customer vẫn sở hữu lược đồ (schema / 스키마), truy cập (access / 접근), backup chính sách (policy / 정책), truy vấn (query / 쿼리) tải (load / 로드) và dữ liệu (data / 데이터) classification.

Một lỗi phổ biến là nghe từ “managed” rồi giả định provider chịu luôn availability/dữ liệu (data / 데이터) khôi phục (recovery / 복구) theo nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항). Managed dịch vụ (service / 서비스) chỉ thay responsibility ma trận (matrix / 행렬); không loại bỏ responsibility.

> **Chuyển mạch:** Ở chặng này của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **2. dùng chung (shared / 공유) responsibility là ranh giới (boundary / 경계), không phải khẩu hiệu** đã nêu tiêu chí phân biệt, còn **3. định danh (identity / 식별자) là perimeter mới** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **4. Region, zone và miền lỗi (failure domain / 장애 도메인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. định danh (identity / 식별자) là perimeter mới

Trong cloud, IAM chính sách (policy / 정책) thường quyết định tài nguyên (resource / 자원) nào có thể gọi API nào. mạng (network / 네트워크) private không đủ nếu credential bị lộ có quyền rộng. Human định danh (identity / 식별자), tải công việc (workload / 워크로드) định danh (identity / 식별자) và automation định danh (identity / 식별자) nên tách nhau.

Least privilege không có nghĩa viết chính sách (policy / 정책) nhỏ nhất ngay từ ngày đầu bằng phỏng đoán. Nó là vòng đời (lifecycle / 생명주기): bắt đầu permission theo use trường hợp (case / 사례), quan sát hành động (action / 동작) thật, giảm wildcard, rà soát (review / 검토) unused privilege và dùng short-lived credential khi có thể.

Tải công việc (workload / 워크로드) nên ưu tiên định danh (identity / 식별자) federation/role thay vì static truy cập (access / 접근) key bake vào tệp (file / 파일)/ảnh (image / 이미지). Nếu secret dài hạn bị bản sao (copy / 복사) qua nhiều CI runner và laptop, rotation trở thành rất khó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **4. Region, zone và miền lỗi (failure domain / 장애 도메인)** tiếp nhận điểm tựa từ **3. định danh (identity / 식별자) là perimeter mới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Virtual mạng (network / 네트워크) là topology + chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Region, zone và miền lỗi (failure domain / 장애 도메인)

Region thường gồm nhiều availability zone/miền lỗi (failure domain / 장애 도메인) riêng hơn. Triển khai replica ở nhiều zone giảm rủi ro nút (node / 노드)/zone, nhưng không tự động chịu region outage. Multi-region tăng resilience nhưng thêm consistency, dữ liệu (data / 데이터) replication, routing và operational độ phức tạp (complexity / 복잡도).

Đừng chọn multi-region chỉ vì nghe “enterprise”. Bắt đầu từ SLO, RPO/RTO và nghiệp vụ (business / 비즈니스) impact rồi mới chọn miền lỗi (failure domain / 장애 도메인) cần chịu.

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **5. Virtual mạng (network / 네트워크) là topology + chính sách (policy / 정책)** tiếp nhận điểm tựa từ **4. Region, zone và miền lỗi (failure domain / 장애 도메인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Compute: VM, bộ chứa (container / 컨테이너) và serverless là lớp trừu tượng (abstraction / 추상화) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Virtual mạng (network / 네트워크) là topology + chính sách (policy / 정책)

Cloud virtual mạng (network / 네트워크) thường có subnet, tuyến (route / 경로) bảng (table / 테이블), bảo mật (security / 보안) group/firewall, NAT, gateway và bộ cân bằng tải (load balancer / 로드 밸런서). mô hình tư duy (mental model / 사고 모델) vẫn là packet đường dẫn (path / 경로). “Private subnet” thường nghĩa không có direct inbound tuyến (route / 경로) từ Internet theo topology hiện tại, không phải tài nguyên (resource / 자원) tự động an toàn trước mọi dữ liệu (data / 데이터) exfiltration hoặc credential misuse.

Troubleshooting nên vẽ nguồn (source / 소스) → DNS → tuyến (route / 경로) → bảo mật (security / 보안) chính sách (policy / 정책) → bộ cân bằng tải (load balancer / 로드 밸런서) → mục tiêu (target / 대상). Chapter [network request path](../01_runtime_foundations/01_network_dns_tls_and_request_path.md) cung cấp chuỗi nhân quả (causal chain / 인과 사슬) chung.

> **Chuyển mạch:** Ở chặng này của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **6. Compute: VM, bộ chứa (container / 컨테이너) và serverless là lớp trừu tượng (abstraction / 추상화) khác nhau** tiếp nhận điểm tựa từ **5. Virtual mạng (network / 네트워크) là topology + chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. đối tượng (object / 객체), khối (block / 블록) và tệp (file / 파일) lưu trữ (storage / 저장소) có ngữ nghĩa (semantics / 의미론) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Compute: VM, bộ chứa (container / 컨테이너) và serverless là lớp trừu tượng (abstraction / 추상화) khác nhau

VM cho điều khiển (control / 제어) lớn và ranh giới (boundary / 경계) kernel riêng. bộ chứa (container / 컨테이너) tăng density/packaging consistency nhưng chia kernel host. Serverless/hàm (function / 함수)/managed thời gian chạy (runtime / 런타임) đẩy vòng đời (lifecycle / 생명주기)/scheduling xuống provider và tính tiền theo mô hình (model / 모델) khác.

Không có lớp trừu tượng (abstraction / 추상화) luôn tốt hơn. tải công việc (workload / 워크로드) lâu dài, latency-sensitive, GPU, stateful hoặc cần kernel điều khiển (control / 제어) có yêu cầu (requirement / 요구사항) khác event-driven hàm (function / 함수) ngắn. nền tảng (platform / 플랫폼) nên offer một số paved road theo tải công việc (workload / 워크로드) lớp (class / 클래스) thay vì buộc tất cả vào Kubernetes.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **7. đối tượng (object / 객체), khối (block / 블록) và tệp (file / 파일) lưu trữ (storage / 저장소) có ngữ nghĩa (semantics / 의미론) khác** tiếp nhận điểm tựa từ **6. Compute: VM, bộ chứa (container / 컨테이너) và serverless là lớp trừu tượng (abstraction / 추상화) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Managed cơ sở dữ liệu (database / 데이터베이스) là phụ thuộc (dependency / 의존성) có quota và maintenance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. đối tượng (object / 객체), khối (block / 블록) và tệp (file / 파일) lưu trữ (storage / 저장소) có ngữ nghĩa (semantics / 의미론) khác

Đối tượng (object / 객체) lưu trữ (storage / 저장소) cung cấp đối tượng (object / 객체)/key API, phù hợp sản phẩm tạo ra (artifact / 산출물), backup, static asset và dữ liệu (data / 데이터) lake mẫu (pattern / 패턴). khối (block / 블록) lưu trữ (storage / 저장소) giống thiết bị (device / 장치)/volume cho filesystem/cơ sở dữ liệu (database / 데이터베이스). tệp (file / 파일) lưu trữ (storage / 저장소) cung cấp dùng chung (shared / 공유) filesystem ngữ nghĩa (semantics / 의미론).

Chọn lưu trữ (storage / 저장소) theo consistency, truy cập (access / 접근) mẫu (pattern / 패턴), độ trễ (latency / 지연 시간), durability, sharing và vòng đời (lifecycle / 생명주기). Không chọn chỉ theo “rẻ hơn mỗi GB”. yêu cầu (request / 요청) chi phí (cost / 비용), egress, IOPS và dữ liệu (data / 데이터) retrieval có thể chi phối tổng chi phí.

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **7. đối tượng (object / 객체), khối (block / 블록) và tệp (file / 파일) lưu trữ (storage / 저장소) có ngữ nghĩa (semantics / 의미론) khác** nêu điều cần giải thích; **8. Managed cơ sở dữ liệu (database / 데이터베이스) là phụ thuộc (dependency / 의존성) có quota và maintenance** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Quota là một phần sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Managed cơ sở dữ liệu (database / 데이터베이스) là phụ thuộc (dependency / 의존성) có quota và maintenance

Managed DB vẫn có liên kết (connection / 연결) limit, IOPS, failover hành vi (behavior / 동작), maintenance cửa sổ (window / 윈도우) và phiên bản (version / 버전) vòng đời (lifecycle / 생명주기). ứng dụng (application / 애플리케이션) liên kết (connection / 연결) pool phải phù hợp sức chứa (capacity / 용량). Nếu autoscale ứng dụng (application / 애플리케이션) từ 10 lên 100 replica, tổng liên kết (connection / 연결) có thể tăng 10 lần và làm cơ sở dữ liệu (database / 데이터베이스) collapse.

Nền tảng (platform / 플랫폼) cần expose quota/ngân sách (budget / 예산) và tích hợp (integration / 통합) mẫu (pattern / 패턴) chứ không chỉ nút “Create cơ sở dữ liệu (database / 데이터베이스)”.

> **Chuyển mạch:** Ở chặng này của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **8. Managed cơ sở dữ liệu (database / 데이터베이스) là phụ thuộc (dependency / 의존성) có quota và maintenance** nêu điều cần giải thích; **9. Quota là một phần sức chứa (capacity / 용량)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Egress và locality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Quota là một phần sức chứa (capacity / 용량)

Cloud account/dự án (project / 프로젝트) có quota theo region/dịch vụ (service / 서비스). Autoscaler không thể tạo nút (node / 노드) mới nếu quota hết. DR failover cũng có thể thất bại nếu region dự phòng chưa có quota/sức chứa (capacity / 용량) reservation.

Quota nên được monitor trước khi sự cố (incident / 인시던트), giống disk không gian (space / 공간). Đây là phụ thuộc (dependency / 의존성) control-plane chứ không hiện trên ứng dụng (application / 애플리케이션) CPU chart.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **10. Egress và locality** tiếp nhận điểm tựa từ **9. Quota là một phần sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. điều khiển (control / 제어) plane thất bại (failure / 실패) và cached mặt phẳng dữ liệu (data plane / 데이터 플레인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Egress và locality

Dữ liệu (data / 데이터) transfer giữa zone/region/Internet vừa ảnh hưởng độ trễ (latency / 지연 시간) vừa chi phí (cost / 비용). Kiến trúc microservice chatty xuyên zone/region có thể tạo bill lớn. chi phí (cost / 비용) telemetry cần nối topology với traffic volume.

“Cloud chi phí (cost / 비용)” thường là architectural tín hiệu (signal / 신호). High egress có thể cho thấy dữ liệu (data / 데이터)/dịch vụ (service / 서비스) ranh giới (boundary / 경계) chưa hợp lý, không chỉ là vấn đề mua discount.

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **10. Egress và locality** nêu điều cần giải thích; **11. điều khiển (control / 제어) plane thất bại (failure / 실패) và cached mặt phẳng dữ liệu (data plane / 데이터 플레인)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. cấp cao (senior / 시니어) ghi chú (note / 노트): thiết kế cloud theo năng lực (capability / 역량), không theo danh mục (catalog / 카탈로그)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. điều khiển (control / 제어) plane thất bại (failure / 실패) và cached mặt phẳng dữ liệu (data plane / 데이터 플레인)

Nhiều managed dịch vụ (service / 서비스) có điều khiển (control / 제어) plane riêng với mặt phẳng dữ liệu (data plane / 데이터 플레인). điều khiển (control / 제어) plane tạm lỗi không luôn làm traffic hiện tại dừng; nhưng quy mô (scale / 규모), cấu hình (config / 설정) thay đổi (change / 변경) hoặc failover có thể không thực hiện được.

Sự cố (incident / 인시던트) runbook phải phân biệt “dịch vụ (service / 서비스) dữ liệu (data / 데이터) đường dẫn (path / 경로) down” với “provider điều khiển (control / 제어) API degraded”. Trong trường hợp điều khiển (control / 제어) plane lỗi, liên tục thử lại (retry / 재시도) provisioning có thể làm hàng đợi (queue / 큐)/hành động (action / 동작) storm khi provider hồi phục.

> **Chuyển mạch:** Ở chặng này của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **11. điều khiển (control / 제어) plane thất bại (failure / 실패) và cached mặt phẳng dữ liệu (data plane / 데이터 플레인)** nêu điều cần giải thích; **12. cấp cao (senior / 시니어) ghi chú (note / 노트): thiết kế cloud theo năng lực (capability / 역량), không theo danh mục (catalog / 카탈로그)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. API success không luôn đồng nghĩa tài nguyên (resource / 자원) đã usable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. cấp cao (senior / 시니어) ghi chú (note / 노트): thiết kế cloud theo năng lực (capability / 역량), không theo danh mục (catalog / 카탈로그)

Cloud provider có hàng trăm dịch vụ (service / 서비스), nhưng nền tảng (platform / 플랫폼) không nên expose danh mục (catalog / 카탈로그) nguyên xi. Hãy gom theo năng lực (capability / 역량): chạy HTTP dịch vụ (service / 서비스), chạy batch, lưu relational dữ liệu (data / 데이터), publish sự kiện (event / 이벤트), lưu đối tượng (object / 객체), expose công khai (public / 공개) endpoint. Sau đó nền tảng (platform / 플랫폼) chọn hiện thực (implementation / 구현)/default dựa trên tổ chức.

Cách này giảm vendor-specific cognitive tải (load / 로드) và cho phép evolution mà không bắt sản phẩm (product / 제품) nhóm (team / 팀) học lại toàn bộ provider.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **12. cấp cao (senior / 시니어) ghi chú (note / 노트): thiết kế cloud theo năng lực (capability / 역량), không theo danh mục (catalog / 카탈로그)** nêu điều cần giải thích; **13. API success không luôn đồng nghĩa tài nguyên (resource / 자원) đã usable** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. Durability, availability và backup là ba thuộc tính (property / 속성) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. API success không luôn đồng nghĩa tài nguyên (resource / 자원) đã usable

Cloud điều khiển (control / 제어) plane thường có hành vi bất đồng bộ và nhất quán cuối cùng (eventual consistency). API tạo role, tuyến (route / 경로), DNS bản ghi (record / 레코드) hoặc cơ sở dữ liệu (database / 데이터베이스) có thể trả thành công trước khi mọi subsystem nhìn thấy trạng thái (state / 상태) mới.

Vì vậy automation không nên giả định `create` thành công là bước sau có thể dùng ngay. Cần waiter/thử lại (retry / 재시도) có backoff cho điều kiện (condition / 조건) cụ thể, nhưng thử lại (retry / 재시도) phải phân biệt trạng thái “chưa hội tụ” với lỗi permission/cấu hình (config / 설정) không thể tự hết.

Một chuỗi xử lý (pipeline / 파이프라인) tạo IAM role rồi ngay lập tức assume role có thể thỉnh thoảng thất bại (fail / 실패) dù mã (code / 코드) không đổi. Nếu chỉ rerun đến khi pass, ta che mất propagation đặc tả hợp đồng (contract / 계약). nền tảng (platform / 플랫폼) nên encode stabilization ngữ nghĩa (semantics / 의미론) để bên tiêu thụ (consumer / 소비자) không phải tự đoán sleep bao nhiêu giây.

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **13. API success không luôn đồng nghĩa tài nguyên (resource / 자원) đã usable** cho ta quy tắc; **14. Durability, availability và backup là ba thuộc tính (property / 속성) khác nhau** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **15. Multi-zone không có nghĩa phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) đã multi-zone** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Durability, availability và backup là ba thuộc tính (property / 속성) khác nhau

Một lưu trữ (storage / 저장소) dịch vụ (service / 서비스) có durability rất cao nghĩa xác suất mất bytes lâu dài thấp, nhưng vẫn có thể tạm unavailable do mạng (network / 네트워크), định danh (identity / 식별자), điều khiển (control / 제어) plane hoặc regional issue. Ngược lại dịch vụ (service / 서비스) highly available không thay thế backup nếu dữ liệu bị xóa/corrupt hợp lệ rồi replication lan truyền thay đổi đó.

Do đó “provider quảng cáo nhiều số 9” phải hỏi đang nói về durability hay availability và phạm vi (scope / 범위) nào. nghiệp vụ (business / 비즈니스) RPO/RTO vẫn cần khôi phục (recovery / 복구) thiết kế (design / 설계) riêng.

Đối tượng (object / 객체) versioning, cross-region replication và backup vault có thể cung cấp các thất bại (failure / 실패) ranh giới (boundary / 경계) khác nhau; không nên coi chúng là cùng một điều khiển (control / 제어).

> **Chuyển mạch:** Ở chặng này của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **14. Durability, availability và backup là ba thuộc tính (property / 속성) khác nhau** cho ta quy tắc; **15. Multi-zone không có nghĩa phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) đã multi-zone** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **16. Autoscaling bị giới hạn bởi provisioning độ trễ (latency / 지연 시간) và downstream ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Multi-zone không có nghĩa phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) đã multi-zone

Ứng dụng (application / 애플리케이션) replica có thể nằm ba zone nhưng NAT gateway, cơ sở dữ liệu (database / 데이터베이스) writer, secret endpoint hoặc bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) vẫn tạo single miền lỗi (failure domain / 장애 도메인). Availability phải được lập luận (reasoning / 추론) theo **đường yêu cầu (request / 요청) và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)**, không theo số zone của riêng compute.

Một rà soát (review / 검토) hữu ích là chọn một zone rồi giả định zone đó biến mất: traffic tuyến (route / 경로) lại ra sao, tải công việc (workload / 워크로드) còn sức chứa (capacity / 용량) không, lưu trữ (storage / 저장소) attach/failover mất bao lâu, DNS/định danh (identity / 식별자)/điều khiển (control / 제어) plane có phụ thuộc tài nguyên (resource / 자원) trong zone đó không.

Nếu hệ thống chỉ sống được khi autoscaler thêm nút (node / 노드) sau thất bại (failure / 실패) nhưng nút (node / 노드) provisioning mất 15 phút còn SLO không chịu được 15 phút degraded sức chứa (capacity / 용량), topology trên giấy chưa đủ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **15. Multi-zone không có nghĩa phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) đã multi-zone** đã nêu tiêu chí phân biệt, còn **16. Autoscaling bị giới hạn bởi provisioning độ trễ (latency / 지연 시간) và downstream ngân sách (budget / 예산)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. Managed dịch vụ (service / 서비스) phiên bản (version / 버전) vòng đời (lifecycle / 생명주기) vẫn là trách nhiệm của bên tiêu thụ (consumer / 소비자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Autoscaling bị giới hạn bởi provisioning độ trễ (latency / 지연 시간) và downstream ngân sách (budget / 예산)

Cloud API giúp quy mô (scale / 규모) nhanh hơn datacenter truyền thống nhưng không tức thời. VM/nút (node / 노드) có thể mất phút để provision, ảnh (image / 이미지) pull thêm thời gian, ứng dụng (application / 애플리케이션) warm-up thêm thời gian nữa. Serverless có lớp trừu tượng (abstraction / 추상화) khác nhưng vẫn có tính đồng thời (concurrency / 동시성) limit, cold-start hoặc downstream quota.

Sức chứa (capacity / 용량) planning cần so **time-to-capacity** với tốc độ demand tăng. Nếu traffic có thể tăng gấp bốn trong 30 giây còn thêm sức chứa (capacity / 용량) cần 8 phút, phải giữ headroom, pre-scale theo sự kiện (event / 이벤트) hoặc shed tải (load / 로드).

Quy mô (scale / 규모) compute cũng không tạo thêm cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) ngân sách (budget / 예산), third-party API quota hay NAT sức chứa (capacity / 용량). Autoscaling là một actuator, không phải nguồn sức chứa (capacity / 용량) vô hạn.

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **16. Autoscaling bị giới hạn bởi provisioning độ trễ (latency / 지연 시간) và downstream ngân sách (budget / 예산)** đã nêu tiêu chí phân biệt, còn **17. Managed dịch vụ (service / 서비스) phiên bản (version / 버전) vòng đời (lifecycle / 생명주기) vẫn là trách nhiệm của bên tiêu thụ (consumer / 소비자)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **18. IAM chính sách (policy / 정책) phải xét tài nguyên (resource / 자원), hành động (action / 동작) và ngữ cảnh (context / 맥락) cùng lúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Managed dịch vụ (service / 서비스) phiên bản (version / 버전) vòng đời (lifecycle / 생명주기) vẫn là trách nhiệm của bên tiêu thụ (consumer / 소비자)

Provider có thể patch OS hoặc vận hành failover, nhưng ứng dụng (application / 애플리케이션) vẫn phụ thuộc engine/API phiên bản (version / 버전), parameter tính tương thích (compatibility / 호환성) và maintenance hành vi (behavior / 동작). Major cơ sở dữ liệu (database / 데이터베이스)/bộ nhớ đệm (cache / 캐시)/thời gian chạy (runtime / 런타임) upgrade có thể đổi kế hoạch truy vấn (query plan / 쿼리 계획), giao thức (protocol / 프로토콜) default hoặc extension tính tương thích (compatibility / 호환성).

Môi trường vận hành (production / 운영 환경) cần inventory phiên bản (version / 버전), deprecation timeline, kiểm thử (test / 테스트) đường dẫn (path / 경로) và staged upgrade. “Managed” không biến phiên bản (version / 버전) evolution thành zero-work; nó chuyển một phần thực thi (execution / 실행) cho provider nhưng tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약) vẫn thuộc hệ thống (system / 시스템) đơn vị sở hữu (owner / 오너).

Maintenance cửa sổ (window / 윈도우) cũng là môi trường vận hành (production / 운영 환경) sự kiện (event / 이벤트). Nếu provider failover/reboot trong cửa sổ (window / 윈도우), ứng dụng (application / 애플리케이션) phải có reconnect/thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론) phù hợp; liên kết (connection / 연결) pool giữ liên kết (connection / 연결) chết quá lâu có thể làm người dùng (user / 사용자) impact kéo dài hơn hạ tầng (infrastructure / 인프라) sự kiện (event / 이벤트).

> **Chuyển mạch:** Ở chặng này của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, cơ chế trong **17. Managed dịch vụ (service / 서비스) phiên bản (version / 버전) vòng đời (lifecycle / 생명주기) vẫn là trách nhiệm của bên tiêu thụ (consumer / 소비자)** cần được kiểm chứng bằng dấu vết cụ thể; **18. IAM chính sách (policy / 정책) phải xét tài nguyên (resource / 자원), hành động (action / 동작) và ngữ cảnh (context / 맥락) cùng lúc** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **19. Egress chi phí (cost / 비용) và độ trễ (latency / 지연 시간) có thể phát hiện ranh giới (boundary / 경계) kiến trúc sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. IAM chính sách (policy / 정책) phải xét tài nguyên (resource / 자원), hành động (action / 동작) và ngữ cảnh (context / 맥락) cùng lúc

Permission rộng không chỉ đến từ `Action: *`. Một hành động (action / 동작) hẹp trên mọi tài nguyên (resource / 자원) hoặc trust chính sách (policy / 정책) cho phép principal quá rộng cũng có blast radius lớn. Điều kiện theo môi trường (environment / 환경), nguồn (source / 소스) định danh (identity / 식별자), audience, mạng (network / 네트워크) ngữ cảnh (context / 맥락) hoặc tag có thể thu hẹp năng lực (capability / 역량) khi ngữ nghĩa (semantics / 의미론) đáng tin.

Nhưng chính sách (policy / 정책) càng phức tạp càng khó lập luận (reasoning / 추론). nền tảng (platform / 플랫폼) nên cung cấp role theo năng lực (capability / 역량) đã thiết kế thay vì bắt mỗi nhóm (team / 팀) tự viết hàng trăm dòng IAM. Exception cần rà soát (review / 검토) theo năng lực (capability / 역량) thực sự được mở, không chỉ diff JSON.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **18. IAM chính sách (policy / 정책) phải xét tài nguyên (resource / 자원), hành động (action / 동작) và ngữ cảnh (context / 맥락) cùng lúc** đã nêu tiêu chí phân biệt, còn **19. Egress chi phí (cost / 비용) và độ trễ (latency / 지연 시간) có thể phát hiện ranh giới (boundary / 경계) kiến trúc sai** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **20. cấp cao (senior / 시니어) walkthrough: failover cơ sở dữ liệu (database / 데이터베이스) thành công nhưng ứng dụng (application / 애플리케이션) vẫn outage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Egress chi phí (cost / 비용) và độ trễ (latency / 지연 시간) có thể phát hiện ranh giới (boundary / 경계) kiến trúc sai

Giả sử dịch vụ (service / 서비스) A ở region Seoul gọi dịch vụ (service / 서비스) B ở region Tokyo cho mỗi yêu cầu (request / 요청) chỉ để lấy siêu dữ liệu (metadata / 메타데이터) nhỏ nhưng thường xuyên. Hệ thống trả cả độ trễ (latency / 지연 시간) xuyên region lẫn egress chi phí (cost / 비용) cho một phụ thuộc (dependency / 의존성) chatty.

Thay vì chỉ mua discount, hãy hỏi dữ liệu (data / 데이터) có thể bộ nhớ đệm (cache / 캐시)/replicate gần bên tiêu thụ (consumer / 소비자), API có quá fine-grained hay dịch vụ (service / 서비스) ranh giới (boundary / 경계) có đặt sai không. chi phí (cost / 비용) ở đây là telemetry về kiến trúc (architecture / 아키텍처).

Tương tự, log ingestion tăng 5 lần sau một bản phát hành (release / 릴리스) có thể là gỡ lỗi (debug / 디버그) verbosity bị bật hoặc thử lại (retry / 재시도) vòng lặp (loop / 루프); FinOps tín hiệu (signal / 신호) nên có đường quay lại môi trường vận hành (production / 운영 환경) investigation.

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **19. Egress chi phí (cost / 비용) và độ trễ (latency / 지연 시간) có thể phát hiện ranh giới (boundary / 경계) kiến trúc sai** đã nêu tiêu chí phân biệt, còn **20. cấp cao (senior / 시니어) walkthrough: failover cơ sở dữ liệu (database / 데이터베이스) thành công nhưng ứng dụng (application / 애플리케이션) vẫn outage** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **21. API tỷ lệ (rate / 비율) limit là sức chứa (capacity / 용량) của điều khiển (control / 제어) plane** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. cấp cao (senior / 시니어) walkthrough: failover cơ sở dữ liệu (database / 데이터베이스) thành công nhưng ứng dụng (application / 애플리케이션) vẫn outage

Giả sử managed DB tự failover trong 45 giây và endpoint DNS trỏ writer mới. Dashboard provider báo healthy nhưng ứng dụng (application / 애플리케이션) lỗi thêm 8 phút.

Bằng chứng (evidence / 증거) cho thấy liên kết (connection / 연결) pool giữ các TCP liên kết (connection / 연결) cũ; máy khách (client / 클라이언트) driver không refresh DNS/reconnect nhanh; thử lại (retry / 재시도) hết thời gian chờ (timeout / 타임아웃) dài làm worker bị giữ. hạ tầng (infrastructure / 인프라) failover đã hoàn thành, nhưng ứng dụng (application / 애플리케이션) khôi phục (recovery / 복구) đặc tả hợp đồng (contract / 계약) chưa hoàn thành.

Fix nằm ở liên kết (connection / 연결) kiểm tra hợp lệ (validation / 검증)/reconnect, hết thời gian chờ (timeout / 타임아웃)/backoff và kiểm thử (test / 테스트) failover end-to-end. Đây là bài học cốt lõi của managed dịch vụ (service / 서비스): provider chỉ sở hữu một phần chuỗi nhân quả (causal chain / 인과 사슬); user-visible khôi phục (recovery / 복구) phải được kiểm chứng ở bên tiêu thụ (consumer / 소비자).

> **Chuyển mạch:** Ở chặng này của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **20. cấp cao (senior / 시니어) walkthrough: failover cơ sở dữ liệu (database / 데이터베이스) thành công nhưng ứng dụng (application / 애플리케이션) vẫn outage** đã nêu tiêu chí phân biệt, còn **21. API tỷ lệ (rate / 비율) limit là sức chứa (capacity / 용량) của điều khiển (control / 제어) plane** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **22. Zonal sức chứa (capacity / 용량) scarcity khác quota** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. API tỷ lệ (rate / 비율) limit là sức chứa (capacity / 용량) của điều khiển (control / 제어) plane

Cloud API không có thông lượng (throughput / 처리량) vô hạn. Một autoscaler, IaC vòng lặp (loop / 루프) hoặc controller fan-out quá mạnh có thể chạm tỷ lệ (rate / 비율) limit/throttle dù data-plane tải công việc (workload / 워크로드) vẫn khỏe. Khi đó reconcile chậm, scale-out bị trì hoãn hoặc automation bắt đầu thử lại (retry / 재시도) và tự tạo thêm áp lực.

Vì vậy control-plane máy khách (client / 클라이언트) cần bounded tính đồng thời (concurrency / 동시성), exponential backoff với jitter và ưu tiên hành động (action / 동작) quan trọng. Nếu 10.000 tài nguyên (resource / 자원) cùng cần refresh sau outage, “thử lại (retry / 재시도) càng nhanh càng tốt” có thể biến provider khôi phục (recovery / 복구) thành thundering herd.

Nền tảng (platform / 플랫폼) nên quan sát API yêu cầu (request / 요청) tỷ lệ (rate / 비율), throttling, hàng đợi (queue / 큐)/reconcile độ trễ (latency / 지연 시간) và actor định danh (identity / 식별자). Đây là sức chứa (capacity / 용량) dimension riêng với CPU/bộ nhớ (memory / 메모리) của tải công việc (workload / 워크로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **21. API tỷ lệ (rate / 비율) limit là sức chứa (capacity / 용량) của điều khiển (control / 제어) plane** đã nêu tiêu chí phân biệt, còn **22. Zonal sức chứa (capacity / 용량) scarcity khác quota** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **23. khôi phục (recovery / 복구) cần sức chứa (capacity / 용량) ở thất bại (failure / 실패) trạng thái (state / 상태), không chỉ steady trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Zonal sức chứa (capacity / 용량) scarcity khác quota

Có quota không đồng nghĩa provider chắc chắn có vật lý (physical / 물리적) sức chứa (capacity / 용량) ngay tại zone/instance lớp (class / 클래스) mong muốn. Một loại VM/GPU có thể tạm thiếu sức chứa (capacity / 용량) trong một zone dù account quota còn. Autoscaler lúc đó có thể thử lại (retry / 재시도) mãi trên một option không thể cấp phát trong thời gian cần thiết.

Thiết kế resilient có thể cần nhiều instance kiểu (type / 타입) tương đương, nhiều zone hoặc reserved sức chứa (capacity / 용량) cho tải công việc (workload / 워크로드) trọng yếu (critical / 중요). Nhưng diversity cũng tăng độ phức tạp (complexity / 복잡도) về kiến trúc (architecture / 아키텍처)/hiệu năng (performance / 성능). Quyết định phải quay về SLO và tải công việc (workload / 워크로드) ràng buộc (constraint / 제약조건).

Runbook quy mô (scale / 규모) thất bại (failure / 실패) nên phân biệt `quota exceeded`, `rate limited`, `capacity unavailable`, `permission denied` và `invalid configuration`; cùng biểu hiện “nút (node / 노드) không lên” nhưng khôi phục (recovery / 복구) đường dẫn (path / 경로) khác nhau.

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **23. khôi phục (recovery / 복구) cần sức chứa (capacity / 용량) ở thất bại (failure / 실패) trạng thái (state / 상태), không chỉ steady trạng thái (state / 상태)** tiếp nhận điểm tựa từ **22. Zonal sức chứa (capacity / 용량) scarcity khác quota** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Cross-zone/region replication có consistency và bandwidth ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. khôi phục (recovery / 복구) cần sức chứa (capacity / 용량) ở thất bại (failure / 실패) trạng thái (state / 상태), không chỉ steady trạng thái (state / 상태)

Hệ thống chạy bình thường với 50% utilization trên hai zone có vẻ có headroom. Nhưng nếu mất một zone chứa 50% sức chứa (capacity / 용량), zone còn lại lập tức lên gần 100% trước khi autoscaling kịp tạo tài nguyên (resource / 자원). Nếu provider không còn sức chứa (capacity / 용량) hoặc quota cho failover, redundancy trên sơ đồ không chuyển thành người dùng (user / 사용자) availability.

Sức chứa (capacity / 용량) planning vì vậy phải tính N-1 hoặc thất bại (failure / 실패) scenario phù hợp: sau khi mất miền lỗi (failure domain / 장애 도메인) lớn nhất, còn bao nhiêu sức chứa (capacity / 용량) phục vụ traffic trong suốt `time-to-recover-capacity`? Headroom có thể cố ý “idle” ở steady trạng thái (state / 상태) nhưng là insurance cho SLO.

FinOps cần hiểu reserve này để không tối ưu nhầm độ tin cậy (reliability / 신뢰성) headroom thành waste.

> **Chuyển mạch:** Ở chặng này của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **24. Cross-zone/region replication có consistency và bandwidth ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **23. khôi phục (recovery / 복구) cần sức chứa (capacity / 용량) ở thất bại (failure / 실패) trạng thái (state / 상태), không chỉ steady trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Private endpoint vẫn cần DNS, IAM và tuyến (route / 경로) cùng hội tụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Cross-zone/region replication có consistency và bandwidth ngân sách (budget / 예산)

Replication không phải phép nhân bản miễn phí. Synchronous replication thường tăng ghi (write / 쓰기) độ trễ (latency / 지연 시간) và availability phụ thuộc quorum/đường dẫn (path / 경로); asynchronous replication giảm coupling trên ghi (write / 쓰기) đường dẫn (path / 경로) nhưng có replication lag và RPO khác 0 khi failover.

DevOps/nền tảng (platform / 플랫폼) tầng (layer / 계층) không cần viết lại distributed-consistency lý thuyết (theory / 이론), nhưng phải expose consequence: chỉ số (metric / 지표) lag nào cần theo dõi, failover ở lag bao nhiêu chấp nhận được, egress/bandwidth có đủ khi backfill/khôi phục (recovery / 복구) không, và failback có xung đột (conflict / 충돌)/dữ liệu (data / 데이터) divergence ngữ nghĩa (semantics / 의미론) gì.

Nếu replication thường ngày chỉ dùng 20% mạng (network / 네트워크) nhưng khôi phục (recovery / 복구)/backfill cần gấp 10 lần thông lượng (throughput / 처리량), đường truyền có thể trở thành bottleneck đúng lúc DR cần nhất. khôi phục (recovery / 복구) sức chứa (capacity / 용량) phải được kiểm thử (test / 테스트) ở quy mô (scale / 규모) thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **25. Private endpoint vẫn cần DNS, IAM và tuyến (route / 경로) cùng hội tụ** tiếp nhận điểm tựa từ **24. Cross-zone/region replication có consistency và bandwidth ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. cấp cao (senior / 시니어) walkthrough: autoscaler muốn thêm nút (node / 노드) nhưng khôi phục (recovery / 복구) vẫn không tới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Private endpoint vẫn cần DNS, IAM và tuyến (route / 경로) cùng hội tụ

Dịch vụ dùng private endpoint thường được xem “an toàn và đơn giản hơn Internet”, nhưng đường đi của yêu cầu (request path / 요청 경로) vẫn phụ thuộc nhiều lớp: private DNS resolve đúng address, tuyến (route / 경로) tới subnet/endpoint tồn tại, bảo mật (security / 보안) chính sách (policy / 정책) cho phép luồng (flow / 흐름) và IAM/dịch vụ (service / 서비스) chính sách (policy / 정책) cho phép thao tác (operation / 연산).

Một di chuyển (migration / 마이그레이션) từ công khai (public / 공개) sang private endpoint có thể tạo partial thất bại (failure / 실패) nếu một VPC dùng DNS mới còn VPC khác bộ nhớ đệm (cache / 캐시) bản ghi (record / 레코드) cũ, hoặc định danh (identity / 식별자) chính sách (policy / 정책) chỉ cho nguồn (source / 소스) endpoint mới. Vì vậy mạng (network / 네트워크) privacy là một composition của name, topology và authorization, không phải một checkbox.

Troubleshooting vẫn theo nguyên tắc cũ: name → tuyến (route / 경로) → vận chuyển (transport / 전송) → định danh (identity / 식별자) → dịch vụ (service / 서비스) phản hồi (response / 응답).

> **Chuyển mạch:** Trong **Cloud primitives: định danh (identity / 식별자), mạng (network / 네트워크), compute, lưu trữ (storage / 저장소) và dùng chung (shared / 공유) responsibility**, **26. cấp cao (senior / 시니어) walkthrough: autoscaler muốn thêm nút (node / 노드) nhưng khôi phục (recovery / 복구) vẫn không tới** tiếp nhận điểm tựa từ **25. Private endpoint vẫn cần DNS, IAM và tuyến (route / 경로) cùng hội tụ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 26. cấp cao (senior / 시니어) walkthrough: autoscaler muốn thêm nút (node / 노드) nhưng khôi phục (recovery / 복구) vẫn không tới

Giả sử sau khi một zone mất, tải công việc (workload / 워크로드) Pending tăng và cluster autoscaler yêu cầu 30 nút (node / 노드) mới ở zone còn lại. Cloud quota đủ, nhưng API trả `capacity unavailable` cho instance kiểu (type / 타입) chính; controller thử lại (retry / 재시도) nhanh và bắt đầu bị rate-limit. Mười phút sau provider sức chứa (capacity / 용량) mới xuất hiện nhưng thử lại (retry / 재시도) storm làm provisioning vẫn chậm.

Chuỗi nhân quả (causal chain / 인과 사슬) có ba ranh giới (boundary / 경계): vật lý (physical / 물리적) sức chứa (capacity / 용량) scarcity, control-plane tỷ lệ (rate / 비율) limit và autoscaler thử lại (retry / 재시도) chính sách (policy / 정책). Chỉ tăng quota không giải quyết. Mitigation có thể mở thêm instance lớp (class / 클래스)/zone đã kiểm thử (test / 테스트), giảm thử lại (retry / 재시도) tính đồng thời (concurrency / 동시성) và dùng reserved/warm sức chứa (capacity / 용량) cho tier trọng yếu (critical / 중요).

Bài học là “cloud elastic” luôn có **thời gian (time / 시간), quota, API và physical-capacity các ràng buộc (constraints / 제약조건들)**. Elasticity là năng lực (capability / 역량) có độ trễ (latency / 지연 시간) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론), không phải định luật rằng sức chứa (capacity / 용량) luôn xuất hiện khi gọi API.

> **Bàn giao:** Sau **26. cấp cao (senior / 시니어) walkthrough: autoscaler muốn thêm nút (node / 노드) nhưng khôi phục (recovery / 복구) vẫn không tới**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
