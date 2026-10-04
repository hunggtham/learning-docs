# Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Modular monolith vs services: boundary economics và migration**. Route đi từ module cohesion → service fixed costs/remote failure → ownership/data boundaries → extraction seams → migration evidence, để tách dịch vụ theo coupling thật thay vì theo khẩu hiệu.

“Monolith hay microservices?” thường bị biến thành câu hỏi công nghệ, trong khi vấn đề thật là **ranh giới (boundary / 경계) economics**: ranh giới (boundary / 경계) nào cần enforce, nhóm (team / 팀) nào sở hữu trạng thái (state / 상태), thay đổi (change / 변경) nào thường đi cùng nhau, thất bại (failure / 실패) nào cần cô lập và organization có đủ năng lực vận hành hệ thống phân tán (distributed system / 분산 시스템) hay không.

## Monolith không đồng nghĩa spaghetti

Một **modular monolith** deploy như một ứng dụng (application / 애플리케이션) nhưng bên trong có mô-đun (module / 모듈) boundaries rõ, phụ thuộc (dependency / 의존성) direction và quyền sở hữu (ownership / 소유권) đặc tả hợp đồng (contract / 계약). mô-đun (module / 모듈) có thể có API nội bộ và không cho mã (code / 코드) khác truy cập trực tiếp hiện thực (implementation / 구현)/dữ liệu (data / 데이터) của nó.

Nếu ranh giới (boundary / 경계) lô-gic (logic / 논리) không tồn tại trong monolith, tách tiến trình (process / 프로세스) thường chỉ biến coupling trong bộ nhớ (memory / 메모리) thành coupling qua mạng (network / 네트워크).

> **Nối mạch:** Modular monolith giữ boundary trong một deployable; services thêm fixed cost vận hành, nên data ownership là boundary kiểm chứng mạnh hơn endpoint khi cân nhắc migration.

## Dịch vụ (service / 서비스) ranh giới (boundary / 경계) có chi phí cố định

Khi mô-đun (module / 모듈) trở thành dịch vụ (service / 서비스), hàm (function / 함수) lời gọi (call / 호출) biến thành mạng (network / 네트워크) lời gọi (call / 호출). Ta nhận thêm serialization, hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도), authentication, khả năng quan sát (observability / 관측 가능성), triển khai (deployment / 배포), phiên bản (version / 버전) tính tương thích (compatibility / 호환성) và partial thất bại (failure / 실패).

Đổi lại có thể nhận independent triển khai (deployment / 배포), tài nguyên (resource / 자원) scaling, fault isolation và nhóm (team / 팀) autonomy. dịch vụ (service / 서비스) chỉ đáng giá khi lợi ích ranh giới (boundary / 경계) vượt distributed-systems tax.

> **Nối mạch:** **Dịch vụ (service / 서비스) ranh giới (boundary / 경계) có chi phí cố định** đặt tiêu chí; **Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) là ranh giới (boundary / 경계) mạnh hơn endpoint** dùng nó để kiểm tra ranh giới, rồi **Giao dịch (transaction / 트랜잭션) trở thành workflow** mở rộng hệ quả.

## Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) là ranh giới (boundary / 경계) mạnh hơn endpoint

Hai services dùng chung cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) và sửa trực tiếp bảng (table / 테이블) của nhau vẫn coupled mạnh dù có hai triển khai (deployment / 배포). Một dịch vụ (service / 서비스) ranh giới (boundary / 경계) trưởng thành thường đi cùng **dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권)**: dịch vụ (service / 서비스) khác tương tác qua đặc tả hợp đồng (contract / 계약) thay vì bypass đơn vị sở hữu (owner / 오너).

Điều này không bắt buộc “mỗi dịch vụ (service / 서비스) một cơ sở dữ liệu (database / 데이터베이스) máy chủ (server / 서버)”; điểm quan trọng là quyền thay đổi lược đồ (schema / 스키마)/dữ liệu (data / 데이터) thuộc một đơn vị sở hữu (owner / 오너) và truy cập (access / 접근) đường dẫn (path / 경로) được kiểm soát.

> **Nối mạch:** **Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) là ranh giới (boundary / 경계) mạnh hơn endpoint** đặt tiêu chí; **Giao dịch (transaction / 트랜잭션) trở thành workflow** dùng nó để kiểm tra ranh giới, rồi **Coupling có nhiều chiều** mở rộng hệ quả.

## Giao dịch (transaction / 트랜잭션) trở thành workflow

Trong monolith + single cơ sở dữ liệu (database / 데이터베이스), nhiều bất biến (invariant / 불변식) có thể nằm trong ACID giao dịch (transaction / 트랜잭션). Sau khi tách dịch vụ (service / 서비스), giao dịch (transaction / 트랜잭션) xuyên ranh giới (boundary / 경계) trở nên đắt hoặc không khả dụng. nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) phải được modeling thành workflow với message, thử lại (retry / 재시도), idempotency và compensation.

Đây là lý do decomposition không chỉ là cắt gói (package / 패키지) thành REST APIs. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) thay đổi ngữ nghĩa (semantics / 의미론) của hệ thống.

> **Nối mạch:** **Giao dịch (transaction / 트랜잭션) trở thành workflow** đặt đầu vào cho **Coupling có nhiều chiều**, rồi **Khi modular monolith có lợi** mở rộng hệ quả.

## Coupling có nhiều chiều

Services có thể loosely coupled về mã (code / 코드) nhưng tightly coupled về triển khai (deployment / 배포) nếu mọi bản phát hành (release / 릴리스) phải phối hợp. Có thể độc lập triển khai (deployment / 배포) nhưng coupled về thời gian chạy (runtime / 런타임) nếu synchronous lời gọi (call / 호출) chuỗi (chain / 사슬) dài. Có thể tách thời gian chạy (runtime / 런타임) nhưng coupled về dữ liệu (data / 데이터) lược đồ (schema / 스키마).

Đánh giá ranh giới (boundary / 경계) cần nhìn **thay đổi (change / 변경) coupling, temporal coupling, dữ liệu (data / 데이터) coupling và organizational coupling**.

> **Nối mạch:** **Khi modular monolith có lợi** nối từ **Coupling có nhiều chiều** sang **Khi dịch vụ (service / 서비스) extraction có tín hiệu tốt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khi modular monolith có lợi

Nhóm (team / 팀) nhỏ, lĩnh vực (domain / 도메인) còn thay đổi nhanh, giao dịch (transaction / 트랜잭션) cross-domain nhiều và operational nền tảng (platform / 플랫폼) chưa trưởng thành thường hưởng lợi từ modular monolith. Debugging cục bộ (local / 로컬) đơn giản, refactor cross-module rẻ hơn và consistency dễ giữ.

Điều kiện là kiến trúc (architecture / 아키텍처) phải thực sự enforce mô-đun (module / 모듈) boundaries; nếu không, technical debt tích tụ và extraction sau này khó hơn.

> **Nối mạch:** **Khi dịch vụ (service / 서비스) extraction có tín hiệu tốt** nối từ **Khi modular monolith có lợi** sang **Di chuyển (migration / 마이그레이션) theo seam**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khi dịch vụ (service / 서비스) extraction có tín hiệu tốt

Một mô-đun (module / 모듈) có scaling profile khác biệt, ranh giới bảo mật (security boundary / 보안 경계) riêng, bản phát hành (release / 릴리스) cadence độc lập hoặc nhóm (team / 팀) quyền sở hữu (ownership / 소유권) ổn định có thể là candidate tốt. Đường xử lý nóng (hot path / 핫 패스) cần tài nguyên (resource / 자원) đặc biệt cũng có thể justify extraction.

“Codebase lớn” một mình chưa đủ; repository có thể lớn nhưng mô-đun (module / 모듈) boundaries vẫn quản lý tốt.

> **Nối mạch:** **Di chuyển (migration / 마이그레이션) theo seam** nối từ **Khi dịch vụ (service / 서비스) extraction có tín hiệu tốt** sang **Reverse di chuyển (migration / 마이그레이션) cũng hợp lệ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Di chuyển (migration / 마이그레이션) theo seam

Extraction an toàn thường bắt đầu từ seam rõ: define giao diện (interface / 인터페이스), ngăn direct cơ sở dữ liệu (database / 데이터베이스) truy cập (access / 접근), đưa phụ thuộc (dependency / 의존성) qua lớp trừu tượng (abstraction / 추상화), quan sát traffic, sau đó mới move hiện thực (implementation / 구현) ra tiến trình (process / 프로세스) riêng.

Mẫu (pattern / 패턴) strangler cho phép tuyến (route / 경로) từng năng lực (capability / 역량) sang dịch vụ (service / 서비스) mới thay vì rewrite toàn hệ thống. Branch-by-abstraction giúp mã (code / 코드) cũ và mới cùng tồn tại trong di chuyển (migration / 마이그레이션) mà không cần long-lived branch khổng lồ.

> **Nối mạch:** **Reverse di chuyển (migration / 마이그레이션) cũng hợp lệ** nối từ **Di chuyển (migration / 마이그레이션) theo seam** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Reverse di chuyển (migration / 마이그레이션) cũng hợp lệ

Nếu dịch vụ (service / 서비스) ranh giới (boundary / 경계) tạo nhiều operational chi phí (cost / 비용) nhưng không mang autonomy/isolation thực, merge services trở lại modular monolith có thể là quyết định đúng. kiến trúc (architecture / 아키텍처) evolution không phải con đường một chiều từ monolith → microservices.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Reverse di chuyển (migration / 마이그레이션) cũng hợp lệ**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy (mental model / 사고 모델)

> tiến trình (process / 프로세스) ranh giới (boundary / 경계) là công cụ kinh tế-kỹ thuật. Modular monolith tối ưu cục bộ (local / 로컬) lập luận (reasoning / 추론) và giao dịch (transaction / 트랜잭션) simplicity; services mua autonomy/isolation bằng phân tán (distributed / 분산) độ phức tạp (complexity / 복잡도). ranh giới (boundary / 경계) tốt là nơi quyền sở hữu (ownership / 소유권), thay đổi (change / 변경) mẫu (pattern / 패턴), dữ liệu (data / 데이터) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) cùng có lý do tách — không phải nơi sơ đồ trông đẹp.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
