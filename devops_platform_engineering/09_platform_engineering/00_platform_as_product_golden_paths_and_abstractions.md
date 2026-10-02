# Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Platform engineering: platform as product, golden paths và abstractions**. Route đi từ developer pain points → platform product contract → paved/golden paths → self-service abstractions → adoption and feedback, để platform tạo leverage mà không che mất cơ chế.

## 1. Vì sao nền tảng (platform / 플랫폼) xuất hiện sau DevOps

DevOps khuyến khích nhóm (team / 팀) sở hữu delivery và môi trường vận hành (production / 운영 환경) kết quả (outcome / 결과). Khi tổ chức có nhiều nhóm (team / 팀), mỗi nhóm (team / 팀) tự giải cùng bài toán CI, bộ chứa (container / 컨테이너), khả năng quan sát (observability / 관측 가능성), secrets và cloud thì cognitive tải (load / 로드) tăng. kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) tạo một sản phẩm (product / 제품) nội bộ để tái sử dụng năng lực (capability / 역량) mà không quay lại mô hình ticket hàng đợi (queue / 큐) cũ.

Mục tiêu không phải lấy việc của nhà phát triển (developer / 개발자), mà làm self-service an toàn.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **2. nền tảng (platform / 플랫폼) là sản phẩm (product / 제품) có người dùng (user / 사용자)** tiếp nhận điểm tựa từ **1. Vì sao nền tảng (platform / 플랫폼) xuất hiện sau DevOps** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Golden đường dẫn (path / 경로) là đường tối ưu cho dùng chung (common / 공통) trường hợp (case / 사례)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. nền tảng (platform / 플랫폼) là sản phẩm (product / 제품) có người dùng (user / 사용자)

Một nền tảng (platform / 플랫폼) phải biết người dùng (user / 사용자) persona: backend nhà phát triển (developer / 개발자), dữ liệu (data / 데이터) engineer, mobile backend nhóm (team / 팀) hay operator. Mỗi persona có job-to-be-done khác nhau.

“nhà phát triển (developer / 개발자) cần không gian tên (namespace / 네임스페이스) Kubernetes” có thể chỉ là implementation-level yêu cầu (request / 요청). Job thật có thể là “cần một HTTP dịch vụ (service / 서비스) private có cơ sở dữ liệu (database / 데이터베이스), metrics và deploy chuỗi xử lý (pipeline / 파이프라인)”. nền tảng (platform / 플랫폼) nên thiết kế giao diện (interface / 인터페이스) theo năng lực (capability / 역량) gần job, không theo tài nguyên (resource / 자원) danh mục (catalog / 카탈로그) nội bộ.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **2. nền tảng (platform / 플랫폼) là sản phẩm (product / 제품) có người dùng (user / 사용자)** cho ta quy tắc; **3. Golden đường dẫn (path / 경로) là đường tối ưu cho dùng chung (common / 공통) trường hợp (case / 사례)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **4. lớp trừu tượng (abstraction / 추상화) phải che độ phức tạp (complexity / 복잡도) accidental, không che physics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Golden đường dẫn (path / 경로) là đường tối ưu cho dùng chung (common / 공통) trường hợp (case / 사례)

Golden đường dẫn (path / 경로) bundle quyết định (decision / 결정) đã được tổ chức hiểu rõ. Ví dụ dịch vụ (service / 서비스) chuẩn có repository template, bản dựng (build / 빌드), sản phẩm tạo ra (artifact / 산출물) registry, triển khai (deployment / 배포), định danh (identity / 식별자), secret tích hợp (integration / 통합), SLO dashboard và quyền sở hữu (ownership / 소유권) siêu dữ liệu (metadata / 메타데이터).

Golden đường dẫn (path / 경로) nên opinionated đủ để giảm quyết định (decision / 결정) fatigue. Nếu generator hỏi 80 câu cloud/Kubernetes, nền tảng (platform / 플랫폼) chưa giảm cognitive tải (load / 로드).

Nhưng golden đường dẫn (path / 경로) không nên khóa use trường hợp (case / 사례) đặc biệt. Escape hatch cần có, kèm tường minh (explicit / 명시적) quyền sở hữu (ownership / 소유권) và rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **3. Golden đường dẫn (path / 경로) là đường tối ưu cho dùng chung (common / 공통) trường hợp (case / 사례)** cho ta quy tắc; **4. lớp trừu tượng (abstraction / 추상화) phải che độ phức tạp (complexity / 복잡도) accidental, không che physics** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **5. giao diện (interface / 인터페이스) của nền tảng (platform / 플랫폼) có nhiều dạng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. lớp trừu tượng (abstraction / 추상화) phải che độ phức tạp (complexity / 복잡도) accidental, không che physics

Nhà phát triển (developer / 개발자) không cần biết CNI hiện thực (implementation / 구현) để deploy dịch vụ (service / 서비스) bình thường. Nhưng họ vẫn cần hiểu hết thời gian chờ (timeout / 타임아웃), yêu cầu tài nguyên (resource request / 리소스 요청), thử lại (retry / 재시도) và dữ liệu (data / 데이터) durability vì đó là thuộc tính (property / 속성) của hệ thống (system / 시스템) chứ không phải chi tiết nền tảng (platform / 플랫폼).

Lớp trừu tượng (abstraction / 추상화) tốt ẩn hiện thực (implementation / 구현) nhưng giữ concept quan trọng. “cơ sở dữ liệu (database / 데이터베이스) plan: small/medium/large” có thể che IOPS detail cho dùng chung (common / 공통) trường hợp (case / 사례), nhưng phải expose backup lớp (class / 클래스), HA, RPO/RTO và liên kết (connection / 연결) các ràng buộc (constraints / 제약조건들) nếu chúng ảnh hưởng ứng dụng (application / 애플리케이션).

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **5. giao diện (interface / 인터페이스) của nền tảng (platform / 플랫폼) có nhiều dạng** tiếp nhận điểm tựa từ **4. lớp trừu tượng (abstraction / 추상화) phải che độ phức tạp (complexity / 복잡도) accidental, không che physics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. dịch vụ (service / 서비스) danh mục (catalog / 카탈로그) là quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. giao diện (interface / 인터페이스) của nền tảng (platform / 플랫폼) có nhiều dạng

Nội bộ (internal / 내부) nhà phát triển (developer / 개발자) Portal (IDP portal) chỉ là một giao diện (interface / 인터페이스). nền tảng (platform / 플랫폼) có thể expose CLI, API, Git repository lược đồ (schema / 스키마), CRD, Terraform mô-đun (module / 모듈) và documentation. Portal đẹp không bù được backend năng lực (capability / 역량) yếu.

Giao diện (interface / 인터페이스) nên composable và automation-friendly. Nếu portal là con đường duy nhất và không có API/declarative nguồn (source / 소스), bulk thao tác (operation / 연산) và GitOps tích hợp (integration / 통합) khó.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, sau nội dung của **5. giao diện (interface / 인터페이스) của nền tảng (platform / 플랫폼) có nhiều dạng**, **6. dịch vụ (service / 서비스) danh mục (catalog / 카탈로그) là quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **7. nền tảng (platform / 플랫폼) năng lực (capability / 역량) nên có đặc tả hợp đồng (contract / 계약)/phiên bản (version / 버전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. dịch vụ (service / 서비스) danh mục (catalog / 카탈로그) là quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)

Danh mục (catalog / 카탈로그) có giá trị khi nối dịch vụ (service / 서비스) với đơn vị sở hữu (owner / 오너), repository, thời gian chạy (runtime / 런타임), dependencies, on-call, SLO và docs. Chỉ liệt kê hàng nghìn dịch vụ (service / 서비스) name không giúp sự cố (incident / 인시던트).

Danh mục (catalog / 카탈로그) nên được cập nhật từ nguồn chuẩn (source of truth / 정본) tự động càng nhiều càng tốt. siêu dữ liệu (metadata / 메타데이터) manual thường stale.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **7. nền tảng (platform / 플랫폼) năng lực (capability / 역량) nên có đặc tả hợp đồng (contract / 계약)/phiên bản (version / 버전)** tiếp nhận điểm tựa từ **6. dịch vụ (service / 서비스) danh mục (catalog / 카탈로그) là quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Paved road và escape hatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. nền tảng (platform / 플랫폼) năng lực (capability / 역량) nên có đặc tả hợp đồng (contract / 계약)/phiên bản (version / 버전)

Template và mô-đun (module / 모듈) thay đổi theo thời gian. Nếu nền tảng (platform / 플랫폼) cập nhật (update / 업데이트) Terraform mô-đun (module / 모듈)/Kubernetes lớp trừu tượng (abstraction / 추상화) phá hàng trăm dịch vụ (service / 서비스), nền tảng (platform / 플랫폼) là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경) nên cần ngữ nghĩa (semantic / 의미적)/phiên bản (version / 버전)/evolution chiến lược (strategy / 전략).

Deprecation cần timeline, di chuyển (migration / 마이그레이션) tooling và visibility ai đang dùng phiên bản (version / 버전) cũ. nền tảng (platform / 플랫폼) không thể nói “nhà phát triển (developer / 개발자) tự cập nhật (update / 업데이트)” nếu lớp trừu tượng (abstraction / 추상화) vốn được tạo để giảm tải công việc (workload / 워크로드) đó.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **8. Paved road và escape hatch** tiếp nhận điểm tựa từ **7. nền tảng (platform / 플랫폼) năng lực (capability / 역량) nên có đặc tả hợp đồng (contract / 계약)/phiên bản (version / 버전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. sản phẩm (product / 제품) discovery cho nền tảng (platform / 플랫폼)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Paved road và escape hatch

Use trường hợp (case / 사례) phổ biến đi paved road với hỗ trợ (support / 지원)/SLO tốt. Use trường hợp (case / 사례) khác có thể tự quản nhưng phải đáp ứng minimum quản trị (governance / 거버넌스). Điều này tránh hai cực: central nền tảng (platform / 플랫폼) kiểm soát mọi thứ, hoặc nền tảng (platform / 플랫폼) bị bỏ qua vì không fit ai.

Escape hatch nên tường minh (explicit / 명시적), không phải undocumented workaround.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **9. sản phẩm (product / 제품) discovery cho nền tảng (platform / 플랫폼)** tiếp nhận điểm tựa từ **8. Paved road và escape hatch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Đo nền tảng (platform / 플랫폼) kết quả (outcome / 결과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. sản phẩm (product / 제품) discovery cho nền tảng (platform / 플랫폼)

Nền tảng (platform / 플랫폼) backlog không nên chỉ đến từ công cụ (tool / 도구) nhóm (team / 팀) muốn thử. Quan sát nhà phát triển (developer / 개발자) journey: thời gian tạo dịch vụ (service / 서비스) mới, bước phải mở ticket, loại sự cố (incident / 인시던트) lặp lại, chuỗi xử lý (pipeline / 파이프라인) wait, secret rotation pain, local-to-prod gap.

Ưu tiên năng lực (capability / 역량) loại bỏ toil/cognitive tải (load / 로드) có tần suất và impact cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **10. Đo nền tảng (platform / 플랫폼) kết quả (outcome / 결과)** tiếp nhận điểm tựa từ **9. sản phẩm (product / 제품) discovery cho nền tảng (platform / 플랫폼)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. nền tảng (platform / 플랫폼) nhóm (team / 팀) không phải ticket nhóm (team / 팀) mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Đo nền tảng (platform / 플랫폼) kết quả (outcome / 결과)

Vanity chỉ số (metric / 지표) như số cluster, số template hoặc số API endpoint không phản ánh giá trị (value / 값). Có thể đo time-to-first-deploy, lead thời gian (time / 시간) cho platform-supported đường dẫn (path / 경로), tỷ lệ adoption tự nguyện, hỗ trợ (support / 지원) ticket theo workflow, thất bại (failure / 실패) tỷ lệ (rate / 비율) do cấu hình (configuration / 구성) và nhà phát triển (developer / 개발자) satisfaction kết hợp độ tin cậy (reliability / 신뢰성).

Chỉ số (metric / 지표) cần chống gaming. Adoption cao vì chính sách (policy / 정책) bắt buộc chưa chắc người dùng (user / 사용자) experience tốt.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **11. nền tảng (platform / 플랫폼) nhóm (team / 팀) không phải ticket nhóm (team / 팀) mới** tiếp nhận điểm tựa từ **10. Đo nền tảng (platform / 플랫폼) kết quả (outcome / 결과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. nhóm (team / 팀) topology và quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. nền tảng (platform / 플랫폼) nhóm (team / 팀) không phải ticket nhóm (team / 팀) mới

Nếu mọi self-service form cuối cùng tạo ticket để nền tảng (platform / 플랫폼) engineer thao tác bằng tay, chỉ thay giao diện. True self-service cần automated provisioning với chính sách (policy / 정책) và asynchronous status rõ.

Human hỗ trợ (support / 지원) vẫn cần cho exception, education và sự cố (incident / 인시던트), nhưng dùng chung (common / 공통) đường dẫn (path / 경로) không nên phụ thuộc hàng đợi (queue / 큐).

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, sau nội dung của **11. nền tảng (platform / 플랫폼) nhóm (team / 팀) không phải ticket nhóm (team / 팀) mới**, **12. nhóm (team / 팀) topology và quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **13. cấp cao (senior / 시니어) ghi chú (note / 노트): nền tảng (platform / 플랫폼) là phụ thuộc (dependency / 의존성) có blast radius lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. nhóm (team / 팀) topology và quyền sở hữu (ownership / 소유권)

Nền tảng (platform / 플랫폼) nhóm (team / 팀) quản dùng chung (shared / 공유) năng lực (capability / 역량); enabling nhóm (team / 팀) có thể giúp sản phẩm (product / 제품) nhóm (team / 팀) học practice mới; complicated subsystem nhóm (team / 팀) sở hữu lĩnh vực (domain / 도메인) chuyên sâu. ranh giới (boundary / 경계) tổ chức nên giảm communication đường dẫn (path / 경로) bắt buộc.

Conway's Law nhắc rằng hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처) phản ánh communication cấu trúc (structure / 구조). nền tảng (platform / 플랫폼) API là cách biến communication lặp lại thành đặc tả hợp đồng (contract / 계약) kỹ thuật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **13. cấp cao (senior / 시니어) ghi chú (note / 노트): nền tảng (platform / 플랫폼) là phụ thuộc (dependency / 의존성) có blast radius lớn** tiếp nhận điểm tựa từ **12. nhóm (team / 팀) topology và quyền sở hữu (ownership / 소유권)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. nền tảng (platform / 플랫폼) có điều khiển (control / 제어) plane và mặt phẳng dữ liệu (data plane / 데이터 플레인) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. cấp cao (senior / 시니어) ghi chú (note / 노트): nền tảng (platform / 플랫폼) là phụ thuộc (dependency / 의존성) có blast radius lớn

Một bug trong dùng chung (shared / 공유) chuỗi xử lý (pipeline / 파이프라인) template, cơ sở (base / 기반) ảnh (image / 이미지) hoặc ingress nền tảng (platform / 플랫폼) có thể ảnh hưởng toàn công ty. Vì vậy nền tảng (platform / 플랫폼) cần chính SLO, canary, tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트), sự cố (incident / 인시던트) phản hồi (response / 응답) và staged rollout như bất kỳ sản phẩm (product / 제품) trọng yếu (critical / 중요) nào.

Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) không phải “DevOps nhóm (team / 팀) đổi tên”. Nó là sản phẩm (product / 제품) discipline áp dụng cho dùng chung (shared / 공유) kỹ thuật (engineering / 엔지니어링) capabilities.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **13. cấp cao (senior / 시니어) ghi chú (note / 노트): nền tảng (platform / 플랫폼) là phụ thuộc (dependency / 의존성) có blast radius lớn** nêu điều cần giải thích; **14. nền tảng (platform / 플랫폼) có điều khiển (control / 제어) plane và mặt phẳng dữ liệu (data plane / 데이터 플레인) riêng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Self-service thao tác (operation / 연산) nên là asynchronous máy trạng thái (state machine / 상태 머신)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. nền tảng (platform / 플랫폼) có điều khiển (control / 제어) plane và mặt phẳng dữ liệu (data plane / 데이터 플레인) riêng

Một nền tảng (platform / 플랫폼) trưởng thành thường có thể nhìn thành hai lớp. **điều khiển (control / 제어) plane** nhận intent, validate chính sách (policy / 정책), tạo workflow, lưu trạng thái và điều phối controller. **mặt phẳng dữ liệu (data plane / 데이터 플레인)** là tải công việc (workload / 워크로드)/tài nguyên (resource / 자원) thực sự phục vụ traffic hoặc chạy job.

Ví dụ nhà phát triển (developer / 개발자) yêu cầu “nội bộ (internal / 내부) HTTP dịch vụ (service / 서비스)”. nền tảng (platform / 플랫폼) điều khiển (control / 제어) plane có thể tạo repository siêu dữ liệu (metadata / 메타데이터), định danh (identity / 식별자), triển khai (deployment / 배포) đối tượng (object / 객체) và khả năng quan sát (observability / 관측 가능성) cấu hình (config / 설정). Sau đó Kubernetes/cloud/thời gian chạy (runtime / 런타임) mặt phẳng dữ liệu (data plane / 데이터 플레인) mới chạy tiến trình (process / 프로세스) và traffic.

Phân biệt này quan trọng khi sự cố (incident / 인시던트). Portal/API nền tảng (platform / 플랫폼) down có thể làm không tạo dịch vụ (service / 서비스) mới được nhưng tải công việc (workload / 워크로드) hiện tại vẫn phục vụ người dùng (user / 사용자). Ngược lại nền tảng (platform / 플랫폼) UI xanh không chứng minh mặt phẳng dữ liệu (data plane / 데이터 플레인) ứng dụng (application / 애플리케이션) khỏe.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **14. nền tảng (platform / 플랫폼) có điều khiển (control / 제어) plane và mặt phẳng dữ liệu (data plane / 데이터 플레인) riêng** nêu điều cần giải thích; **15. Self-service thao tác (operation / 연산) nên là asynchronous máy trạng thái (state machine / 상태 머신)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약) phải nói cả happy đường dẫn (path / 경로) lẫn thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Self-service thao tác (operation / 연산) nên là asynchronous máy trạng thái (state machine / 상태 머신)

Provision cơ sở dữ liệu (database / 데이터베이스), cluster tài nguyên (resource / 자원) hoặc môi trường (environment / 환경) thường không hoàn thành trong một HTTP yêu cầu (request / 요청) ngắn. nền tảng (platform / 플랫폼) API tốt không giả vờ mọi thao tác (operation / 연산) là synchronous. Nó nhận intent, tạo thao tác (operation / 연산)/tài nguyên (resource / 자원) định danh (identity / 식별자) rồi expose status/điều kiện (condition / 조건) cho người dùng (user / 사용자) theo dõi.

Mô hình tư duy (mental model / 사고 모델):

```text
request intent
→ accepted + resource/operation ID
→ validation/policy
→ provisioning/reconciliation
→ ready | failed | degraded
```

Điều này cho phép thử lại (retry / 재시도), hết thời gian chờ (timeout / 타임아웃) và partial thất bại (failure / 실패) có ngữ nghĩa (semantics / 의미론) rõ. Nếu người dùng (user / 사용자) bấm nút lần hai vì trang web hết thời gian chờ (timeout / 타임아웃) mà backend không có idempotency key/tài nguyên (resource / 자원) định danh (identity / 식별자), nền tảng (platform / 플랫폼) có thể tạo duplicate hạ tầng (infrastructure / 인프라).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **15. Self-service thao tác (operation / 연산) nên là asynchronous máy trạng thái (state machine / 상태 머신)** xác định đầu vào; **16. nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약) phải nói cả happy đường dẫn (path / 경로) lẫn thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **17. phiên bản (version / 버전) evolution cần tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약) phải nói cả happy đường dẫn (path / 경로) lẫn thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)

API “CreateDatabase(plan=medium)” chưa đủ. bên tiêu thụ (consumer / 소비자) còn cần biết create mất bao lâu, thất bại (failure / 실패) có thử lại (retry / 재시도) được không, delete có giữ backup không, phiên bản (version / 버전) upgrade có downtime không, credential rotate thế nào và SLO/hỗ trợ (support / 지원) ranh giới (boundary / 경계) là gì.

Lớp trừu tượng (abstraction / 추상화) mạnh không chỉ giảm số trường dữ liệu (field / 필드); nó nén nhiều quyết định (decision / 결정) vào một đặc tả hợp đồng (contract / 계약) ổn định. Nếu đặc tả hợp đồng (contract / 계약) chỉ mô tả provisioning mà bỏ Day 2 thao tác (operation / 연산), nhà phát triển (developer / 개발자) vẫn phải học hiện thực (implementation / 구현) khi upgrade/sự cố (incident / 인시던트).

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **16. nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약) phải nói cả happy đường dẫn (path / 경로) lẫn thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)** xác định đầu vào; **17. phiên bản (version / 버전) evolution cần tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **18. Golden đường dẫn (path / 경로) phải encode escape hatch chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. phiên bản (version / 버전) evolution cần tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)

Nền tảng (platform / 플랫폼) giao diện (interface / 인터페이스) thay đổi có thể ảnh hưởng hàng trăm nhóm (team / 팀). Một breaking di chuyển (migration / 마이그레이션) “mọi dịch vụ (service / 서비스) đổi manifest trong tuần này” chuyển toil từ nền tảng (platform / 플랫폼) nhóm (team / 팀) sang toàn tổ chức.

Evolution tốt thường cần coexistence cửa sổ (window / 윈도우): phiên bản (version / 버전) cũ tiếp tục được hỗ trợ (support / 지원) trong thời gian xác định; phiên bản (version / 버전) mới có di chuyển (migration / 마이그레이션) công cụ (tool / 도구)/preview; nền tảng (platform / 플랫폼) biết bên tiêu thụ (consumer / 소비자) nào còn ở old phiên bản (version / 버전); deprecation có telemetry và deadline.

Nếu có thể tự động migrate nguồn (source / 소스)/cấu hình (config / 설정) an toàn, nền tảng (platform / 플랫폼) nên làm automation thay vì phát documentation dài yêu cầu từng nhóm (team / 팀) sửa tay.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **17. phiên bản (version / 버전) evolution cần tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** xác định đầu vào; **18. Golden đường dẫn (path / 경로) phải encode escape hatch chi phí (cost / 비용)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **19. nền tảng (platform / 플랫폼) SLO nên theo nhà phát triển (developer / 개발자) journey** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Golden đường dẫn (path / 경로) phải encode escape hatch chi phí (cost / 비용)

Escape hatch không chỉ là boolean “được phép custom”. Nó cần quyền sở hữu (ownership / 소유권) mô hình (model / 모델). nhóm (team / 팀) rời paved road có thể mất một phần hỗ trợ (support / 지원)/SLO, tự chịu upgrade của custom thành phần (component / 컴포넌트) hoặc phải đáp ứng chính sách (policy / 정책) bổ sung.

Nếu custom đường dẫn (path / 경로) miễn mọi chi phí (cost / 비용) nhưng vẫn được nền tảng (platform / 플랫폼) nhóm (team / 팀) hỗ trợ (support / 지원) đầy đủ, golden đường dẫn (path / 경로) khó duy trì. Ngược lại nếu escape hatch bị phạt quá nặng, nhóm (team / 팀) sẽ giấu workaround. đặc tả hợp đồng (contract / 계약) minh bạch giúp lựa chọn sự đánh đổi (trade-off / 트레이드오프) có chủ đích.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **18. Golden đường dẫn (path / 경로) phải encode escape hatch chi phí (cost / 비용)** xác định đầu vào; **19. nền tảng (platform / 플랫폼) SLO nên theo nhà phát triển (developer / 개발자) journey** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **20. sản phẩm (product / 제품) discovery phải phân biệt cognitive tải (load / 로드) thiết yếu và accidental** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. nền tảng (platform / 플랫폼) SLO nên theo nhà phát triển (developer / 개발자) journey

Một nền tảng (platform / 플랫폼) có nhiều nội bộ (internal / 내부) thành phần (component / 컴포넌트) nhưng người dùng (user / 사용자) quan tâm journey end-to-end: tạo dịch vụ (service / 서비스), merge thay đổi (change / 변경), deploy, provision môi trường (environment / 환경), rotate secret, gỡ lỗi (debug / 디버그) sự cố (incident / 인시던트). SLI chỉ đo API uptime của portal có thể xanh trong khi provisioning hàng đợi (queue / 큐) treo hàng giờ.

Ví dụ SLI nền tảng (platform / 플랫폼) có thể đo tỷ lệ provisioning hoàn tất trong 15 phút, tỷ lệ deploy chuỗi xử lý (pipeline / 파이프라인) thành công không do nền tảng (platform / 플랫폼) fault, hoặc time-to-first-production trên paved road. Khi SLO cháy, nền tảng (platform / 플랫폼) nhóm (team / 팀) có bằng chứng (evidence / 증거) để ưu tiên độ tin cậy (reliability / 신뢰성) thay vì chỉ nhìn hỗ trợ (support / 지원) ticket.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **20. sản phẩm (product / 제품) discovery phải phân biệt cognitive tải (load / 로드) thiết yếu và accidental** tiếp nhận điểm tựa từ **19. nền tảng (platform / 플랫폼) SLO nên theo nhà phát triển (developer / 개발자) journey** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. cấp cao (senior / 시니어) walkthrough: nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) gây blast radius toàn công ty** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. sản phẩm (product / 제품) discovery phải phân biệt cognitive tải (load / 로드) thiết yếu và accidental

Không phải mọi độ phức tạp (complexity / 복잡도) đều nên giấu. nhà phát triển (developer / 개발자) cần hiểu consistency, hết thời gian chờ (timeout / 타임아웃), idempotency, tài nguyên (resource / 자원) demand và dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) vì đó là physics của phân tán (distributed / 분산) ứng dụng (application / 애플리케이션). Nhưng họ không nhất thiết phải biết account ID, subnet naming, ingress annotation hay secret-store wiring của tổ chức.

Nền tảng (platform / 플랫폼) tốt giảm **accidental độ phức tạp (complexity / 복잡도)** nhưng giữ **essential độ phức tạp (complexity / 복잡도)** đủ visible để người dùng (user / 사용자) đưa quyết định đúng. Nếu lớp trừu tượng (abstraction / 추상화) biến mọi cơ sở dữ liệu (database / 데이터베이스) thành một nút “Create” mà che RPO, liên kết (connection / 연결) limit và chi phí (cost / 비용) tier, cognitive tải (load / 로드) giảm ngắn hạn nhưng sự cố (incident / 인시던트)/rủi ro (risk / 위험) tăng dài hạn.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **21. cấp cao (senior / 시니어) walkthrough: nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) gây blast radius toàn công ty** tiếp nhận điểm tựa từ **20. sản phẩm (product / 제품) discovery phải phân biệt cognitive tải (load / 로드) thiết yếu và accidental** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Declarative nền tảng (platform / 플랫폼) tài nguyên (resource / 자원) cần bất biến (invariant / 불변식) rõ hơn trạng thái Ready** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. cấp cao (senior / 시니어) walkthrough: nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) gây blast radius toàn công ty

Giả sử dùng chung (shared / 공유) cơ sở (base / 기반) ảnh (image / 이미지) mới nâng thời gian chạy (runtime / 런타임)/CA bundle và nền tảng (platform / 플랫폼) cập nhật template để mọi bản dựng (build / 빌드) dùng ngay phiên bản (version / 버전) mới. Nếu rollout đồng loạt, một tính tương thích (compatibility / 호환성) bug có thể làm hàng trăm dịch vụ (service / 서비스) thất bại (fail / 실패) cùng lúc.

Nền tảng (platform / 플랫폼) bản phát hành (release / 릴리스) nên được xử lý như môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스): canary một nhóm bên tiêu thụ (consumer / 소비자), tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트) trên representative tải công việc (workload / 워크로드), đo thất bại (failure / 실패) tín hiệu (signal / 신호), sau đó staged adoption. Có thể giữ old/new phiên bản (version / 버전) song song và auto-open di chuyển (migration / 마이그레이션) PR thay vì force-update instant.

Điểm cốt lõi là nền tảng (platform / 플랫폼) có **fan-out blast radius** lớn. Mức discipline cần cao hơn, không thấp hơn, ứng dụng (application / 애플리케이션) nhóm (team / 팀) bình thường.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **21. cấp cao (senior / 시니어) walkthrough: nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) gây blast radius toàn công ty** nêu điều cần giải thích; **22. Declarative nền tảng (platform / 플랫폼) tài nguyên (resource / 자원) cần bất biến (invariant / 불변식) rõ hơn trạng thái Ready** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **23. Idempotency cần đi qua toàn workflow, không chỉ API front door** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Declarative nền tảng (platform / 플랫폼) tài nguyên (resource / 자원) cần bất biến (invariant / 불변식) rõ hơn trạng thái `Ready`

Một tài nguyên (resource / 자원) self-service như `Database`, `Service` hoặc `Environment` thường là aggregate của nhiều đối tượng (object / 객체) thật. `Ready=true` chỉ có ý nghĩa nếu nền tảng (platform / 플랫폼) định nghĩa bất biến (invariant / 불변식) đứng sau nó: mạng (network / 네트워크) reachable, định danh (identity / 식별자) bound, credential issued, backup chính sách (policy / 정책) active, monitoring registered và phụ thuộc (dependency / 의존성) required đã usable.

Nếu controller set Ready ngay sau khi cloud API trả “accepted” nhưng endpoint còn chưa routable, lớp trừu tượng (abstraction / 추상화) đang báo trạng thái quá sớm. Ngược lại nếu một năng lực (capability / 역량) optional như dashboard lỗi mà toàn tài nguyên (resource / 자원) bị `Failed`, đặc tả hợp đồng (contract / 계약) có thể quá chặt.

Nền tảng (platform / 플랫폼) cần phân biệt điều kiện (condition / 조건) theo năng lực (capability / 역량) và severity, ví dụ `Provisioned`, `Reachable`, `BackupConfigured`, `Degraded`. Status là API cho automation và operator, không phải văn bản (text / 텍스트) trang trí UI.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, biết phải giữ gì trong **22. Declarative nền tảng (platform / 플랫폼) tài nguyên (resource / 자원) cần bất biến (invariant / 불변식) rõ hơn trạng thái Ready**, ta theo dõi trong **23. Idempotency cần đi qua toàn workflow, không chỉ API front door** cách hệ thống thực hiện và phản hồi qua từng bước. Từ đây, **24. Delete là máy trạng thái (state machine / 상태 머신) có data-retention ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Idempotency cần đi qua toàn workflow, không chỉ API front door

Một `POST` có idempotency key chưa đủ nếu backend workflow tạo tài nguyên (resource / 자원) A thành công, hết thời gian chờ (timeout / 타임아웃), rồi thử lại (retry / 재시도) tạo tài nguyên (resource / 자원) B lần nữa. Mỗi side tác động (effect / 효과) cần được bind vào stable tài nguyên (resource / 자원) định danh (identity / 식별자) và controller phải có cách discover/adopt trạng thái (state / 상태) đã tồn tại.

Mô hình tư duy (mental model / 사고 모델) tốt là:

```text
stable intent identity
→ deterministic/external resource identity
→ observe existing state
→ create only what is missing
→ record progress
→ retry safely
```

Nếu bên ngoài (external / 외부) provider không hỗ trợ idempotent create, nền tảng (platform / 플랫폼) có thể cần naming deterministic, máy khách (client / 클라이언트) đơn vị từ (token / 토큰) hoặc reconciliation/adoption lô-gic (logic / 논리). Partial thất bại (failure / 실패) là normal trạng thái (state / 상태) của phân tán (distributed / 분산) workflow, không phải trường hợp biên (edge case / 경계 사례) hiếm.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, cơ chế trong **23. Idempotency cần đi qua toàn workflow, không chỉ API front door** cần được kiểm chứng bằng dấu vết cụ thể; **24. Delete là máy trạng thái (state machine / 상태 머신) có data-retention ngữ nghĩa (semantics / 의미론)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **25. nền tảng (platform / 플랫폼) nên chia fault-containment cell thay vì một toàn cục (global / 전역) điều khiển (control / 제어) plane vô hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Delete là máy trạng thái (state machine / 상태 머신) có data-retention ngữ nghĩa (semantics / 의미론)

Delete thường nguy hiểm hơn create vì có thể irreversible. Một nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약) cần trả lời: xóa logical tài nguyên (resource / 자원) có xóa dữ liệu (data / 데이터) ngay không; backup giữ bao lâu; phụ thuộc (dependency / 의존성) nào chặn delete; finalizer/cleanup thất bại (fail / 실패) thì tài nguyên (resource / 자원) ở trạng thái gì; force-delete có bỏ lại orphan không.

Một mẫu (pattern / 패턴) an toàn là tách `DeletionRequested` khỏi `Deleted`, thực hiện phụ thuộc (dependency / 의존성) check, snapshot/retention theo chính sách (policy / 정책), revoke định danh (identity / 식별자)/traffic rồi mới destroy tài nguyên (resource / 자원). Với dữ liệu (data / 데이터) trọng yếu (critical / 중요), nền tảng (platform / 플랫폼) có thể thêm grace period hoặc khôi phục (recovery / 복구) cửa sổ (window / 윈도우).

Nếu người dùng (user / 사용자) phải biết hiện thực (implementation / 구현) để đoán dữ liệu (data / 데이터) còn hay mất sau nút Delete, lớp trừu tượng (abstraction / 추상화) đã thất bại ở thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) quan trọng nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **25. nền tảng (platform / 플랫폼) nên chia fault-containment cell thay vì một toàn cục (global / 전역) điều khiển (control / 제어) plane vô hạn** tiếp nhận điểm tựa từ **24. Delete là máy trạng thái (state machine / 상태 머신) có data-retention ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. nền tảng (platform / 플랫폼) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) cần được quản như API phụ thuộc (dependency / 의존성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. nền tảng (platform / 플랫폼) nên chia fault-containment cell thay vì một toàn cục (global / 전역) điều khiển (control / 제어) plane vô hạn

Dùng chung (shared / 공유) nền tảng (platform / 플랫폼) tạo leverage nhưng cũng tạo blast radius. Một controller/toàn cục (global / 전역) hàng đợi (queue / 큐)/toàn cục (global / 전역) registry phụ thuộc (dependency / 의존성) có thể trở thành common-mode thất bại (failure / 실패) cho toàn tổ chức. Khi quy mô (scale / 규모) lớn, có thể cần chia cell theo region, nghiệp vụ (business / 비즈니스) criticality, tenant group hoặc tải công việc (workload / 워크로드) lớp (class / 클래스).

Cell không nhất thiết nghĩa mỗi nhóm (team / 팀) một nền tảng (platform / 플랫폼) riêng. Nó nghĩa thất bại (failure / 실패) trong một partition không được mặc định lan tới tất cả bên tiêu thụ (consumer / 소비자). điều khiển (control / 제어) plane có thể federation chung về chính sách (policy / 정책)/danh mục (catalog / 카탈로그) nhưng thực thi (execution / 실행) hàng đợi (queue / 큐), cluster/account hoặc bản phát hành (release / 릴리스) ring được partition.

Sự đánh đổi (trade-off / 트레이드오프) là duplication/chi phí (cost / 비용) tăng và toàn cục (global / 전역) thao tác (operation / 연산) phức tạp hơn. Vì vậy cell ranh giới (boundary / 경계) nên xuất phát từ SLO, miền lỗi (failure domain / 장애 도메인) và operational blast radius, không phải organizational chart đơn thuần.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **26. nền tảng (platform / 플랫폼) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) cần được quản như API phụ thuộc (dependency / 의존성)** tiếp nhận điểm tựa từ **25. nền tảng (platform / 플랫폼) nên chia fault-containment cell thay vì một toàn cục (global / 전역) điều khiển (control / 제어) plane vô hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. lớp trừu tượng (abstraction / 추상화) leakage là tín hiệu (signal / 신호) để cải tiến đặc tả hợp đồng (contract / 계약), không phải luôn là lỗi người dùng (user / 사용자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. nền tảng (platform / 플랫폼) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) cần được quản như API phụ thuộc (dependency / 의존성)

Golden đường dẫn (path / 경로) thường kéo theo cơ sở (base / 기반) ảnh (image / 이미지), thời gian chạy (runtime / 런타임), CI hành động (action / 동작), chính sách (policy / 정책) bundle, ingress lớp (class / 클래스), khả năng quan sát (observability / 관측 가능성) tác nhân (agent / 에이전트) và cloud mô-đun (module / 모듈). Nếu mỗi phụ thuộc (dependency / 의존성) tự upgrade độc lập, bên tiêu thụ (consumer / 소비자) có thể nhận breaking thay đổi (change / 변경) gián tiếp mà nền tảng (platform / 플랫폼) phiên bản (version / 버전) không đổi.

Nền tảng (platform / 플랫폼) bản phát hành (release / 릴리스) nên có một notion về tested tính tương thích (compatibility / 호환성) set. Không nhất thiết khóa (lock / 잠금) mọi thành phần (component / 컴포넌트) mãi mãi, nhưng cần biết phiên bản (version / 버전) nào đã được verify cùng nhau và rollout phụ thuộc (dependency / 의존성) nào có fan-out lớn.

Khi một dùng chung (shared / 공유) CA bundle hoặc tác nhân (agent / 에이전트) mới gây lỗi, danh mục (catalog / 카탈로그)/telemetry phải cho biết bên tiêu thụ (consumer / 소비자) nào đang ở bản phát hành (release / 릴리스) ring/phiên bản (version / 버전) nào. Đây là ứng dụng (application / 애플리케이션) của sản phẩm tạo ra (artifact / 산출물)/phiên bản (version / 버전) lập luận (reasoning / 추론) vào chính nền tảng (platform / 플랫폼) sản phẩm (product / 제품).

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **27. lớp trừu tượng (abstraction / 추상화) leakage là tín hiệu (signal / 신호) để cải tiến đặc tả hợp đồng (contract / 계약), không phải luôn là lỗi người dùng (user / 사용자)** tiếp nhận điểm tựa từ **26. nền tảng (platform / 플랫폼) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) cần được quản như API phụ thuộc (dependency / 의존성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Long-running thao tác (operation / 연산) cần cancellation ngữ nghĩa (semantics / 의미론) rõ ràng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. lớp trừu tượng (abstraction / 추상화) leakage là tín hiệu (signal / 신호) để cải tiến đặc tả hợp đồng (contract / 계약), không phải luôn là lỗi người dùng (user / 사용자)

Mọi lớp trừu tượng (abstraction / 추상화) đều có lúc rò: cơ sở dữ liệu (database / 데이터베이스) plan không đủ mô tả IOPS, ingress lớp trừu tượng (abstraction / 추상화) thiếu hết thời gian chờ (timeout / 타임아웃) chế độ (mode / 모드), dịch vụ (service / 서비스) tier không biểu diễn failover yêu cầu (requirement / 요구사항). Khi nhiều nhóm (team / 팀) cùng cần escape hatch ở cùng điểm, đó là bằng chứng (evidence / 증거) đặc tả hợp đồng (contract / 계약) thiếu dimension quan trọng.

Nền tảng (platform / 플랫폼) nhóm (team / 팀) nên phân loại escape hatch: one-off exceptional yêu cầu (requirement / 요구사항) hay repeated missing năng lực (capability / 역량). Nếu repeated, hãy đưa concept thật sự cần thiết lên API ở mức lĩnh vực (domain / 도메인) — ví dụ `durabilityClass`, `trafficProfile`, `recoveryTier` — thay vì expose raw provider trường dữ liệu (field / 필드) hàng loạt.

Mục tiêu của lớp trừu tượng (abstraction / 추상화) không phải che mọi chi tiết mãi mãi; nó là giữ **quyết định (decision / 결정) surface nhỏ nhưng đúng với physics và bất biến (invariant / 불변식) mà bên tiêu thụ (consumer / 소비자) cần kiểm soát**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **28. Long-running thao tác (operation / 연산) cần cancellation ngữ nghĩa (semantics / 의미론) rõ ràng** tiếp nhận điểm tựa từ **27. lớp trừu tượng (abstraction / 추상화) leakage là tín hiệu (signal / 신호) để cải tiến đặc tả hợp đồng (contract / 계약), không phải luôn là lỗi người dùng (user / 사용자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Compensation khác quay lui (rollback / 롤백) thật sự** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Long-running thao tác (operation / 연산) cần cancellation ngữ nghĩa (semantics / 의미론) rõ ràng

Một thao tác (operation / 연산) provisioning kéo dài 20 phút có thể bị người dùng (user / 사용자) cancel ở phút thứ 8, nhưng bên ngoài (external / 외부) API đã tạo mạng (network / 네트워크), cơ sở dữ liệu (database / 데이터베이스) hoặc reservation. “Cancel yêu cầu (request / 요청)” không tự động đồng nghĩa mọi side tác động (effect / 효과) biến mất.

Nền tảng (platform / 플랫폼) API cần nói cancellation là best-effort hay guaranteed trước một checkpoint nào đó; thao tác (operation / 연산) đang ở phase nào; tài nguyên (resource / 자원) nào đã materialize; cleanup có tự động không; và khi cleanup thất bại (fail / 실패) thì trạng thái cuối là `Cancelled`, `CancelRequested` hay `Degraded`.

Nếu cancel chỉ dừng worker cục bộ (local / 로컬) nhưng bên ngoài (external / 외부) side tác động (effect / 효과) vẫn tiếp tục, controller sau đó phải reconcile/adopt hoặc cleanup. Cancellation vì vậy là một chuyển tiếp trạng thái (state transition / 상태 전이) có quyền sở hữu (ownership / 소유권), không phải nút UI đơn giản.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **29. Compensation khác quay lui (rollback / 롤백) thật sự** tiếp nhận điểm tựa từ **28. Long-running thao tác (operation / 연산) cần cancellation ngữ nghĩa (semantics / 의미론) rõ ràng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Orphan và adoption là vòng đời (lifecycle / 생명주기) bình thường của controller mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Compensation khác quay lui (rollback / 롤백) thật sự

Trong workflow phân tán, nhiều hành động (action / 동작) không có inverse hoàn hảo. Tạo cơ sở dữ liệu (database / 데이터베이스) rồi xóa lại có thể để backup, kiểm tra (audit / 감사) bản ghi (record / 레코드), chi phí (cost / 비용) hoặc bên ngoài (external / 외부) identifier; gửi notification không thể “unsend”; rotate credential có thể làm liên kết (connection / 연결) cũ chết.

Khi giao dịch (transaction / 트랜잭션) atomic không tồn tại, nền tảng (platform / 플랫폼) thường dùng compensating hành động (action / 동작): tạo bước mới để đưa hệ thống (system / 시스템) về bất biến (invariant / 불변식) chấp nhận được thay vì giả vờ quay ngược thời gian. đặc tả hợp đồng (contract / 계약) cần phân biệt quay lui (rollback / 롤백) có thể đảo chính xác (exact / 정확한) trạng thái (state / 상태) với compensation chỉ phục hồi nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식).

Điều này quan trọng cho UX và runbook. Nếu nền tảng (platform / 플랫폼) nói “quay lui (rollback / 롤백) succeeded”, operator phải biết đó là sản phẩm tạo ra (artifact / 산출물) revert, traffic revert hay workflow compensation sau partial side tác động (effect / 효과).

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **29. Compensation khác quay lui (rollback / 롤백) thật sự** xác định đầu vào; **30. Orphan và adoption là vòng đời (lifecycle / 생명주기) bình thường của controller mạnh** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. “Ai vận hành nền tảng (platform / 플랫폼) khi nền tảng (platform / 플랫폼) hỏng?” là bootstrap bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Orphan và adoption là vòng đời (lifecycle / 생명주기) bình thường của controller mạnh

Bên ngoài (external / 외부) tài nguyên (resource / 자원) có thể tồn tại mà nền tảng (platform / 플랫폼) trạng thái (state / 상태) mất bản ghi (record / 레코드) do crash/trạng thái (state / 상태) corruption, hoặc tài nguyên (resource / 자원) được tạo thủ công rồi cần đưa vào quyền sở hữu (ownership / 소유권). Xóa ngay mọi đối tượng (object / 객체) “không nhận ra” là nguy hiểm; bỏ mặc chúng lại tạo drift, chi phí (cost / 비용) và bảo mật (security / 보안) debt.

Nền tảng (platform / 플랫폼) nên có ngữ nghĩa (semantics / 의미론) discover/adopt/quarantine. Adoption cần verify định danh (identity / 식별자), quyền sở hữu (ownership / 소유권), chính sách (policy / 정책) tính tương thích (compatibility / 호환성) và trạng thái (state / 상태) ánh xạ (mapping / 매핑) trước khi controller bắt đầu mutate. Orphan cleanup cần grace period và bằng chứng (evidence / 증거) đủ mạnh rằng tài nguyên (resource / 자원) không còn đơn vị sở hữu (owner / 오너) hợp lệ.

Mô hình tư duy (mental model / 사고 모델) là **quyền sở hữu (ownership / 소유권) cũng là trạng thái (state / 상태) cần reconcile**. tài nguyên (resource / 자원) tồn tại không nói ai có quyền sửa/xóa nó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **30. Orphan và adoption là vòng đời (lifecycle / 생명주기) bình thường của controller mạnh** xác định đầu vào; **31. “Ai vận hành nền tảng (platform / 플랫폼) khi nền tảng (platform / 플랫폼) hỏng?” là bootstrap bài toán (problem / 문제)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **32. Deprecation thành công phải đo di chuyển (migration / 마이그레이션) trạng thái (state / 상태), không chỉ gửi thông báo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. “Ai vận hành nền tảng (platform / 플랫폼) khi nền tảng (platform / 플랫폼) hỏng?” là bootstrap bài toán (problem / 문제)

Nền tảng (platform / 플랫폼) có thể phụ thuộc vào chính Kubernetes cluster, GitOps, secret store, DNS, định danh (identity / 식별자) hoặc CI mà nó cung cấp cho người dùng (user / 사용자). Nếu điều khiển (control / 제어) plane nền tảng (platform / 플랫폼) down và khôi phục (recovery / 복구) công cụ (tool / 도구) cũng nằm hoàn toàn bên trong cùng miền lỗi (failure domain / 장애 도메인), nhóm (team / 팀) có circular phụ thuộc (dependency / 의존성).

Khôi phục (recovery / 복구) thiết kế (design / 설계) phải có bootstrap đường dẫn (path / 경로) tối thiểu: nguồn (source / 소스)/cấu hình (config / 설정) nào còn truy cập được, credential break-glass nào tồn tại độc lập, sản phẩm tạo ra (artifact / 산출물)/controller ảnh (image / 이미지) lấy từ đâu, trạng thái (state / 상태) backend restore thế nào và thành phần (component / 컴포넌트) nào phải lên trước. Có thể cần một management plane/cell nhỏ hơn hoặc documented manual khôi phục (recovery / 복구) step được drill định kỳ.

Nền tảng (platform / 플랫폼) SLO vì vậy không chỉ đo normal self-service. Nó phải có khôi phục (recovery / 복구) đặc tả hợp đồng (contract / 계약) cho chính điều khiển (control / 제어) plane — một dạng “operator của operator”.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **32. Deprecation thành công phải đo di chuyển (migration / 마이그레이션) trạng thái (state / 상태), không chỉ gửi thông báo** tiếp nhận điểm tựa từ **31. “Ai vận hành nền tảng (platform / 플랫폼) khi nền tảng (platform / 플랫폼) hỏng?” là bootstrap bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Cell kiến trúc (architecture / 아키텍처) cần toàn cục (global / 전역) siêu dữ liệu (metadata / 메타데이터) nhưng tránh toàn cục (global / 전역) thực thi (execution / 실행) phụ thuộc (dependency / 의존성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Deprecation thành công phải đo di chuyển (migration / 마이그레이션) trạng thái (state / 상태), không chỉ gửi thông báo

Một nền tảng (platform / 플랫폼) phiên bản (version / 버전) cũ được tuyên bố deprecated nhưng không biết bên tiêu thụ (consumer / 소비자) nào còn dùng thì deadline chỉ là hy vọng. di chuyển (migration / 마이그레이션) program cần inventory theo chính xác (exact / 정확한) phiên bản (version / 버전)/năng lực (capability / 역량), đơn vị sở hữu (owner / 오너), blocker và rủi ro (risk / 위험) nếu quá hạn.

Telemetry nên phân biệt `supported`, `deprecated`, `migration-in-progress`, `exception`, `unsupported`. Auto-remediation có thể mở PR hoặc mutate nguồn (source / 소스) khi safe, nhưng breaking ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경) vẫn cần bằng chứng (evidence / 증거) từ bên tiêu thụ (consumer / 소비자) hành vi (behavior / 동작).

Deprecation hoàn tất khi old đường dẫn (path / 경로) không còn môi trường vận hành (production / 운영 환경) phụ thuộc (dependency / 의존성) và hỗ trợ (support / 지원) burden được gỡ bỏ có kiểm soát, không phải khi announcement đã gửi ba lần.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **32. Deprecation thành công phải đo di chuyển (migration / 마이그레이션) trạng thái (state / 상태), không chỉ gửi thông báo** nêu điều cần giải thích; **33. Cell kiến trúc (architecture / 아키텍처) cần toàn cục (global / 전역) siêu dữ liệu (metadata / 메타데이터) nhưng tránh toàn cục (global / 전역) thực thi (execution / 실행) phụ thuộc (dependency / 의존성)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **34. Supportability là một phần của nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Cell kiến trúc (architecture / 아키텍처) cần toàn cục (global / 전역) siêu dữ liệu (metadata / 메타데이터) nhưng tránh toàn cục (global / 전역) thực thi (execution / 실행) phụ thuộc (dependency / 의존성)

Khi nền tảng (platform / 플랫폼) chia nhiều cell để giảm blast radius, vẫn thường cần danh mục (catalog / 카탈로그), định danh (identity / 식별자) ánh xạ (mapping / 매핑), chính sách (policy / 정책) phiên bản (version / 버전) hoặc routing siêu dữ liệu (metadata / 메타데이터) chung. Nếu mọi yêu cầu (request / 요청) thời gian chạy (runtime / 런타임) phải đồng bộ gọi một toàn cục (global / 전역) điều khiển (control / 제어) plane, cell isolation có thể bị phá bởi toàn cục (global / 전역) outage.

Một thiết kế tốt phân biệt siêu dữ liệu (metadata / 메타데이터) cần phân phối với thực thi (execution / 실행) quyết định (decision / 결정) cần cục bộ (local / 로컬) autonomy. toàn cục (global / 전역) trạng thái (state / 상태) có thể replicate/bộ nhớ đệm (cache / 캐시)/phiên bản (version / 버전); cell dùng revision đã biết để tiếp tục phục vụ trong một khoảng, rồi degrade có chủ đích nếu trạng thái (state / 상태) quá cũ.

Sự đánh đổi (trade-off / 트레이드오프) chuyển từ “một toàn cục (global / 전역) điều khiển (control / 제어) plane đơn giản” sang bài toán consistency và phiên bản (version / 버전) skew. Nhưng mục tiêu là giữ miền lỗi (failure domain / 장애 도메인) thật sự bounded, không chỉ chia cluster trên sơ đồ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **33. Cell kiến trúc (architecture / 아키텍처) cần toàn cục (global / 전역) siêu dữ liệu (metadata / 메타데이터) nhưng tránh toàn cục (global / 전역) thực thi (execution / 실행) phụ thuộc (dependency / 의존성)** nêu điều cần giải thích; **34. Supportability là một phần của nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **35. Control-plane trạng thái (state / 상태) phải có durability đặc tả hợp đồng (contract / 계약) riêng với tài nguyên (resource / 자원) bên ngoài** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Supportability là một phần của nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약)

Golden đường dẫn (path / 경로) không chỉ cần create nhanh mà còn phải giúp người dùng hiểu thất bại (failure / 실패) khi lớp trừu tượng (abstraction / 추상화) rò. nền tảng (platform / 플랫폼) nên expose thao tác (operation / 연산) ID, hiện tại (current / 현재) phase, owning controller, relevant revision, phụ thuộc (dependency / 의존성) status và đường drill-down đủ để hỗ trợ (support / 지원)/operator giảm tìm kiếm (search / 검색) không gian (space / 공간).

Nếu portal chỉ báo `Provisioning failed` còn nguyên nhân nằm trong ba hệ thống nội bộ không có correlation ID, self-service đã chuyển ticket từ “hãy tạo giúp” thành “hãy gỡ lỗi (debug / 디버그) giúp”. Cognitive tải (load / 로드) không biến mất mà chỉ đổi thời điểm.

Một lớp trừu tượng (abstraction / 추상화) trưởng thành tối ưu cả **happy-path simplicity** lẫn **failure-path diagnosability**. Đường đi chuẩn thật sự tốt là đường dễ dùng khi bình thường và vẫn giữ chuỗi nhân quả (causal chain / 인과 사슬) khi bất thường.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **34. Supportability là một phần của nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **35. Control-plane trạng thái (state / 상태) phải có durability đặc tả hợp đồng (contract / 계약) riêng với tài nguyên (resource / 자원) bên ngoài** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **36. Safe chế độ (mode / 모드)/read-only chế độ (mode / 모드) là degraded năng lực (capability / 역량) có chủ đích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Control-plane trạng thái (state / 상태) phải có durability đặc tả hợp đồng (contract / 계약) riêng với tài nguyên (resource / 자원) bên ngoài

Nền tảng (platform / 플랫폼) thường lưu intent, quyền sở hữu (ownership / 소유권), thao tác (operation / 연산) progress và ánh xạ (mapping / 매핑) tới cloud/Kubernetes tài nguyên (resource / 자원). Nếu trạng thái (state / 상태) store mất nhưng tài nguyên (resource / 자원) thật vẫn tồn tại, restore một backup cũ có thể khiến controller tin tài nguyên (resource / 자원) chưa được tạo rồi tạo duplicate, hoặc coi tài nguyên (resource / 자원) hợp lệ là orphan.

Vì vậy backup control-plane trạng thái (state / 상태) không đủ nếu không có reconciliation sau restore. khôi phục (recovery / 복구) cần biết checkpoint nào được restore, bên ngoài (external / 외부) side tác động (effect / 효과) nào có thể đã xảy ra sau checkpoint, rồi discover/adopt/reconcile trước khi mở lại mutation bình thường. Đây là cùng thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) với cơ sở dữ liệu (database / 데이터베이스) + hệ thống bên ngoài (external system / 외부 시스템), nhưng blast radius lớn hơn vì nền tảng (platform / 플랫폼) sở hữu nhiều tenant.

RPO của siêu dữ liệu (metadata / 메타데이터) nền tảng (platform / 플랫폼) và RPO của tải công việc (workload / 워크로드) dữ liệu (data / 데이터) có thể khác nhau, nhưng cả hai phải được tường minh (explicit / 명시적). “Có backup cơ sở dữ liệu (database / 데이터베이스) nền tảng (platform / 플랫폼)” không tự chứng minh restore sẽ hội tụ đúng với world trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **35. Control-plane trạng thái (state / 상태) phải có durability đặc tả hợp đồng (contract / 계약) riêng với tài nguyên (resource / 자원) bên ngoài** nêu điều cần giải thích; **36. Safe chế độ (mode / 모드)/read-only chế độ (mode / 모드) là degraded năng lực (capability / 역량) có chủ đích** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **37. Control-plane admission phải bảo vệ reconciliation công việc (work / 작업) quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Safe chế độ (mode / 모드)/read-only chế độ (mode / 모드) là degraded năng lực (capability / 역량) có chủ đích

Khi chính sách (policy / 정책) dịch vụ (service / 서비스), trạng thái (state / 상태) backend hoặc một toàn cục (global / 전역) phụ thuộc (dependency / 의존성) có vấn đề, lựa chọn không chỉ là “nền tảng (platform / 플랫폼) hoạt động đầy đủ” hoặc “tắt toàn bộ”. Một điều khiển (control / 제어) plane có thể chuyển sang chế độ (mode / 모드) hạn chế: cho phép đọc status/danh mục (catalog / 카탈로그), giữ tải công việc (workload / 워크로드) hiện tại, chặn create/delete nguy hiểm hoặc chỉ cho thao tác (operation / 연산) đã xác minh an toàn.

Safe chế độ (mode / 모드) cần đặc tả hợp đồng (contract / 계약) rõ về hành động (action / 동작) nào được phép và stale trạng thái (state / 상태) tối đa bao lâu. Nếu người dùng (user / 사용자) không biết yêu cầu (request / 요청) bị từ chối vì an toàn (safety / 안전) chế độ (mode / 모드) hay vì chính sách (policy / 정책) nghiệp vụ (business / 비즈니스), họ sẽ thử lại (retry / 재시도)/tạo workaround và tăng sự cố (incident / 인시던트) tải (load / 로드).

Thiết kế degraded chế độ (mode / 모드) trước sự cố (incident / 인시던트) giúp tránh operator tự chế fail-open bằng cách disable hàng loạt guardrail. Đây là brownout ở nền tảng (platform / 플랫폼) điều khiển (control / 제어) plane: giữ năng lực (capability / 역량) cốt lõi và giảm mutation surface để bảo vệ bất biến (invariant / 불변식).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **37. Control-plane admission phải bảo vệ reconciliation công việc (work / 작업) quan trọng** tiếp nhận điểm tựa từ **36. Safe chế độ (mode / 모드)/read-only chế độ (mode / 모드) là degraded năng lực (capability / 역량) có chủ đích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. nền tảng (platform / 플랫폼) DR phải kiểm tra phụ thuộc (dependency / 의존성) thứ tự (ordering / 순서) chứ không chỉ restore từng thành phần (component / 컴포넌트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Control-plane admission phải bảo vệ reconciliation công việc (work / 작업) quan trọng

Self-service API có thể nhận create hàng loạt đúng lúc controller đang xử lý khôi phục (recovery / 복구) của tài nguyên (resource / 자원) hiện có. Nếu tất cả thao tác (operation / 연산) vào chung hàng đợi (queue / 큐) FIFO, burst provisioning mới có thể làm health reconciliation, secret rotation hoặc failover chậm tới mức vi phạm SLO.

Nền tảng (platform / 플랫폼) cần phân loại công việc (work / 작업) theo urgency/quyền sở hữu (ownership / 소유권): steady-state reconciliation, khôi phục (recovery / 복구), người dùng (user / 사용자) provisioning, bulk di chuyển (migration / 마이그레이션), background cleanup. Priority không nên biến thành starvation; cần tính đồng thời (concurrency / 동시성)/reservation/fairness phù hợp. Một số công việc (work / 작업) có thể bị shed hoặc pause khi điều khiển (control / 제어) plane saturation, trong khi khôi phục (recovery / 복구) công việc (work / 작업) giữ reserved sức chứa (capacity / 용량).

Đây là liên kết (connection / 연결) giữa nền tảng (platform / 플랫폼) sản phẩm (product / 제품) và SRE overload điều khiển (control / 제어): điều khiển (control / 제어) plane cũng cần admission, hàng đợi (queue / 큐) discipline và khôi phục (recovery / 복구) headroom như mặt phẳng dữ liệu (data plane / 데이터 플레인).

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **38. nền tảng (platform / 플랫폼) DR phải kiểm tra phụ thuộc (dependency / 의존성) thứ tự (ordering / 순서) chứ không chỉ restore từng thành phần (component / 컴포넌트)** tiếp nhận điểm tựa từ **37. Control-plane admission phải bảo vệ reconciliation công việc (work / 작업) quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. API tính tương thích (compatibility / 호환성) phải xét cả stored trạng thái (state / 상태), máy khách (client / 클라이언트) và controller phiên bản (version / 버전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. nền tảng (platform / 플랫폼) DR phải kiểm tra phụ thuộc (dependency / 의존성) thứ tự (ordering / 순서) chứ không chỉ restore từng thành phần (component / 컴포넌트)

Một runbook liệt kê “restore cơ sở dữ liệu (database / 데이터베이스), start controller, start portal” có thể sai nếu controller cần định danh (identity / 식별자) issuer, DNS, KMS, registry hoặc chính sách (policy / 정책) bundle chưa sẵn sàng. khôi phục (recovery / 복구) đồ thị (graph / 그래프) nên biểu diễn prerequisite và năng lực (capability / 역량) tối thiểu cần cho bước tiếp theo.

```text
break-glass identity + artifact access
→ state/KMS/DNS tối thiểu
→ core controller
→ reconcile/adopt external resources
→ policy/catalog/observability
→ mở mutation dần
→ full self-service
```

Game day phải chứng minh operator thực sự có thể đi từ miền lỗi (failure domain / 장애 도메인) bị mất tới trạng thái hội tụ, bao gồm credential độc lập, sản phẩm tạo ra (artifact / 산출물) khả dụng và bên ngoài (external / 외부) tài nguyên (resource / 자원) discovery. Nếu drill chỉ restart thành phần (component / 컴포넌트) trong môi trường (environment / 환경) đang khỏe, bootstrap đường dẫn (path / 경로) chưa được kiểm thử (test / 테스트).

Nền tảng (platform / 플랫폼) khôi phục (recovery / 복구) hoàn tất khi điều khiển (control / 제어) plane và bên ngoài (external / 외부) world đồng thuận đủ về quyền sở hữu (ownership / 소유권)/trạng thái (state / 상태) để mutation trở lại an toàn, không phải khi portal HTTP 200.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **39. API tính tương thích (compatibility / 호환성) phải xét cả stored trạng thái (state / 상태), máy khách (client / 클라이언트) và controller phiên bản (version / 버전)** tiếp nhận điểm tựa từ **38. nền tảng (platform / 플랫폼) DR phải kiểm tra phụ thuộc (dependency / 의존성) thứ tự (ordering / 순서) chứ không chỉ restore từng thành phần (component / 컴포넌트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Defaulting là hành vi (behavior / 동작) và có thể trở thành breaking thay đổi (change / 변경) âm thầm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. API tính tương thích (compatibility / 호환성) phải xét cả stored trạng thái (state / 상태), máy khách (client / 클라이언트) và controller phiên bản (version / 버전)

Nền tảng (platform / 플랫폼) API declarative thường sống lâu hơn một lần deploy controller. tài nguyên (resource / 자원) đã lưu từ phiên bản (version / 버전) cũ có thể tiếp tục tồn tại khi API máy chủ (server / 서버)/controller đã nâng phiên bản (version / 버전); CLI, portal, GitOps tác nhân (agent / 에이전트) và automation của bên tiêu thụ (consumer / 소비자) cũng không nâng cùng lúc. Vì vậy tính tương thích (compatibility / 호환성) không chỉ là “yêu cầu (request / 요청) mới có parse được không?” mà là **phiên bản (version / 버전) skew trên toàn vòng đời tài nguyên (resource / 자원)**.

Một trường dữ liệu (field / 필드) bị đổi nghĩa nhưng giữ cùng tên đặc biệt nguy hiểm: manifest cũ vẫn hợp lệ về lược đồ (schema / 스키마) nhưng controller mới diễn giải khác. Breaking ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경) nên được phiên bản (version / 버전) hóa hoặc di chuyển (migration / 마이그레이션) rõ, thay vì dựa vào kiểm tra hợp lệ (validation / 검증) cú pháp (syntax / 문법). bằng chứng (evidence / 증거) cần biết tài nguyên (resource / 자원) được tạo/last-converted theo revision nào và controller nào đang reconcile nó.

Nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약) tốt định nghĩa skew được hỗ trợ (support / 지원): máy khách (client / 클라이언트) N-1 có nói chuyện với điều khiển (control / 제어) plane N không, tài nguyên (resource / 자원) lược đồ (schema / 스키마) cũ được đọc bao lâu, controller quay lui (rollback / 롤백) có hiểu trạng thái (state / 상태) đã được controller mới ghi không. Đây là tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) của chính nền tảng (platform / 플랫폼).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **40. Defaulting là hành vi (behavior / 동작) và có thể trở thành breaking thay đổi (change / 변경) âm thầm** tiếp nhận điểm tựa từ **39. API tính tương thích (compatibility / 호환성) phải xét cả stored trạng thái (state / 상태), máy khách (client / 클라이언트) và controller phiên bản (version / 버전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Conversion phải bảo toàn intent, không chỉ chuyển được JSON** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Defaulting là hành vi (behavior / 동작) và có thể trở thành breaking thay đổi (change / 변경) âm thầm

Khi người dùng (user / 사용자) bỏ trống một trường dữ liệu (field / 필드), nền tảng (platform / 플랫폼) thường áp default. Nếu default thay từ `single-zone` sang `multi-zone`, `small` sang `medium` hoặc retention 7 ngày sang 30 ngày, manifest nguồn (source / 소스) không đổi nhưng effective hạ tầng (infrastructure / 인프라), chi phí (cost / 비용) và hành vi khi thất bại (failure behavior / 실패 동작) đổi.

Vì vậy default phải được coi là versioned chính sách (policy / 정책). Với tài nguyên (resource / 자원) đã tồn tại, cần quyết định default được materialize/freeze lúc create hay được recompute mỗi reconciliation. Hai lựa chọn có ngữ nghĩa (semantics / 의미론) rất khác: recompute giúp chính sách (policy / 정책) mới lan nhanh nhưng có thể mutate hàng nghìn tài nguyên (resource / 자원) chỉ vì controller upgrade.

Status/effective-state nên cho operator thấy default nào đã được resolve. “Không có trường dữ liệu (field / 필드) trong YAML” không đồng nghĩa “không có quyết định”. Default ẩn là một phần của API surface.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **41. Conversion phải bảo toàn intent, không chỉ chuyển được JSON** tiếp nhận điểm tựa từ **40. Defaulting là hành vi (behavior / 동작) và có thể trở thành breaking thay đổi (change / 변경) âm thầm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. năng lực (capability / 역량) negotiation tốt hơn giả định (assumption / 가정) khi nhiều cell/phiên bản (version / 버전) cùng tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Conversion phải bảo toàn intent, không chỉ chuyển được JSON

Khi lược đồ (schema / 스키마) có `v1alpha1 → v1beta1 → v1`, conversion có thể map trường dữ liệu (field / 필드) cũ sang biểu diễn (representation / 표현) mới. Nhưng nếu mô hình (model / 모델) mới biểu diễn concept khác, conversion cú pháp có thể làm mất intent. Ví dụ trường dữ liệu (field / 필드) `replicas: 3` trước đây ngầm nghĩa cùng zone, còn phiên bản (version / 버전) mới tách `capacity` và `failureDomainSpread`.

Một conversion an toàn cần bất biến (invariant / 불변식) về round-trip hoặc lossiness được tường minh (explicit / 명시적). Nếu `old → new → old` làm mất thông tin, quay lui (rollback / 롤백) điều khiển (control / 제어) plane có thể không an toàn. Một số di chuyển (migration / 마이그레이션) cần materialize trường dữ liệu (field / 필드) mới hoặc yêu cầu người dùng (user / 사용자) quyết định thay vì tự đoán.

Conversion webhook/controller cũng là phụ thuộc (dependency / 의존성) thời gian chạy (runtime / 런타임). Nếu API máy chủ (server / 서버) cần conversion dịch vụ (service / 서비스) để đọc đối tượng (object / 객체) cũ mà dịch vụ (service / 서비스) đó down trong control-plane sự cố (incident / 인시던트), chính tài nguyên (resource / 자원) cần cho khôi phục (recovery / 복구) có thể không đọc được. Upgrade thiết kế (design / 설계) phải xét bootstrap đường dẫn (path / 경로) của conversion.

> **Chuyển mạch:** Ở chặng này của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **42. năng lực (capability / 역량) negotiation tốt hơn giả định (assumption / 가정) khi nhiều cell/phiên bản (version / 버전) cùng tồn tại** tiếp nhận điểm tựa từ **41. Conversion phải bảo toàn intent, không chỉ chuyển được JSON** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Controller upgrade phải giữ reconciliation monotonic theo bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. năng lực (capability / 역량) negotiation tốt hơn giả định (assumption / 가정) khi nhiều cell/phiên bản (version / 버전) cùng tồn tại

Trong rollout nền tảng (platform / 플랫폼) nhiều cell/region, không nên giả định mọi nơi hỗ trợ năng lực (capability / 역량) mới cùng lúc. bên tiêu thụ (consumer / 소비자) hoặc orchestrator có thể cần biết cell nào hỗ trợ lưu trữ (storage / 저장소) lớp (class / 클래스) mới, chính sách (policy / 정책) revision nào hoặc thao tác (operation / 연산) ngữ nghĩa (semantic / 의미적) nào trước khi gửi intent.

Năng lực (capability / 역량) có thể được expose qua phiên bản (version / 버전)/status/danh mục (catalog / 카탈로그) thay vì để yêu cầu (request / 요청) thất bại (fail / 실패) ngẫu nhiên. Tuy nhiên negotiation không nên biến thành hàng trăm tính năng (feature / 기능) bit không có vòng đời (lifecycle / 생명주기). năng lực (capability / 역량) cần ngữ nghĩa (semantic / 의미적) ổn định, đơn vị sở hữu (owner / 오너) và deprecation giống API trường dữ liệu (field / 필드).

Mô hình tư duy (mental model / 사고 모델) là `intent requirement → advertised capability → admission → execution`. Nếu năng lực (capability / 역량) không đủ, reject sớm với reason rõ tốt hơn accept rồi thất bại (fail / 실패) sâu sau 20 phút provisioning.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **43. Controller upgrade phải giữ reconciliation monotonic theo bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **42. năng lực (capability / 역량) negotiation tốt hơn giả định (assumption / 가정) khi nhiều cell/phiên bản (version / 버전) cùng tồn tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Status lược đồ (schema / 스키마) cũng là API và cần evolution discipline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Controller upgrade phải giữ reconciliation monotonic theo bất biến (invariant / 불변식)

Hai controller phiên bản (version / 버전) có thể chạy chồng trong rolling upgrade hoặc old phiên bản (version / 버전) có thể quay lại sau quay lui (rollback / 롤백). Nếu chúng sở hữu cùng trường dữ liệu (field / 필드) nhưng dùng lô-gic (logic / 논리) khác, desired trạng thái (state / 상태) có thể oscillate: phiên bản (version / 버전) mới thêm cấu hình (config / 설정), phiên bản (version / 버전) cũ xóa nó, rồi phiên bản (version / 버전) mới thêm lại.

Upgrade chiến lược (strategy / 전략) cần trường dữ liệu (field / 필드) quyền sở hữu (ownership / 소유권) và tính tương thích (compatibility / 호환성) rõ. Có thể cần leader/phiên bản (version / 버전) gate, staged controller rollout, lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) trước hành vi (behavior / 동작) activation hoặc chỉ cho một phiên bản (version / 버전) mutate tài nguyên (resource / 자원) lớp (class / 클래스) nhất định. Quan trọng là mỗi reconciliation trong supported skew phải đưa hệ thống (system / 시스템) gần bất biến (invariant / 불변식) hơn, không tạo tug-of-war.

Bằng chứng (evidence / 증거) cần dimension theo controller phiên bản (version / 버전), tài nguyên (resource / 자원) generation và mutation reason. Nếu bên ngoài (external / 외부) tài nguyên (resource / 자원) đổi qua lại mà nguồn (source / 소스) intent không đổi, hãy nghi reconciliation xung đột (conflict / 충돌)/phiên bản (version / 버전) skew trước khi đổ lỗi provider.

> **Chuyển mạch:** Trong **Kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링): nền tảng (platform / 플랫폼) as sản phẩm (product / 제품), golden đường dẫn (path / 경로) và lớp trừu tượng (abstraction / 추상화)**, **44. Status lược đồ (schema / 스키마) cũng là API và cần evolution discipline** tiếp nhận điểm tựa từ **43. Controller upgrade phải giữ reconciliation monotonic theo bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 44. Status lược đồ (schema / 스키마) cũng là API và cần evolution discipline

Automation thường đọc `Ready`, điều kiện (condition / 조건) reason, endpoint, thao tác (operation / 연산) phase hoặc observed generation từ status. Đổi tên reason, bỏ điều kiện (condition / 조건) hoặc thay nghĩa `Ready` có thể phá chuỗi xử lý (pipeline / 파이프라인) dù spec vẫn tương thích.

Status nên tách machine-stable trường dữ liệu (field / 필드) khỏi human message. bên tiêu thụ (consumer / 소비자) automation không nên parse chuỗi lỗi tự do. điều kiện (condition / 조건) cần quyền sở hữu (ownership / 소유권), observed revision/generation và chuyển tiếp (transition / 전이) ngữ nghĩa (semantics / 의미론) đủ rõ để biết tín hiệu (signal / 신호) mới hay stale.

Nền tảng (platform / 플랫폼) API trưởng thành phiên bản (version / 버전) cả **intent surface** lẫn **bằng chứng (evidence / 증거) surface**. bên tiêu thụ (consumer / 소비자) cần gửi desired trạng thái (state / 상태) ổn định, nhưng cũng cần đọc actual trạng thái (state / 상태) đáng tin để quyết định tiếp theo; tính tương thích (compatibility / 호환성) chỉ bảo vệ một phía là chưa đủ.

> **Bàn giao:** Sau **44. Status lược đồ (schema / 스키마) cũng là API và cần evolution discipline**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
