# Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Modular monolith vs services: boundary economics và migration**. Route đi từ module cohesion → service fixed costs/remote failure → ownership/data boundaries → extraction seams → migration evidence, để tách dịch vụ theo coupling thật thay vì theo khẩu hiệu.

“Monolith hay microservices?” thường bị biến thành câu hỏi công nghệ, trong khi vấn đề thật là **ranh giới (boundary / 경계) economics**: ranh giới (boundary / 경계) nào cần enforce, nhóm (team / 팀) nào sở hữu trạng thái (state / 상태), thay đổi (change / 변경) nào thường đi cùng nhau, thất bại (failure / 실패) nào cần cô lập và organization có đủ năng lực vận hành hệ thống phân tán (distributed system / 분산 시스템) hay không.

## Monolith không đồng nghĩa spaghetti

Một **modular monolith** deploy như một ứng dụng (application / 애플리케이션) nhưng bên trong có mô-đun (module / 모듈) boundaries rõ, phụ thuộc (dependency / 의존성) direction và quyền sở hữu (ownership / 소유권) đặc tả hợp đồng (contract / 계약). mô-đun (module / 모듈) có thể có API nội bộ và không cho mã (code / 코드) khác truy cập trực tiếp hiện thực (implementation / 구현)/dữ liệu (data / 데이터) của nó.

Nếu ranh giới (boundary / 경계) lô-gic (logic / 논리) không tồn tại trong monolith, tách tiến trình (process / 프로세스) thường chỉ biến coupling trong bộ nhớ (memory / 메모리) thành coupling qua mạng (network / 네트워크).

> **Chuyển mạch:** Modular monolith giữ boundary trong một deployable; services thêm fixed cost vận hành, nên data ownership là boundary kiểm chứng mạnh hơn endpoint khi cân nhắc migration.

## Dịch vụ (service / 서비스) ranh giới (boundary / 경계) có chi phí cố định

Khi mô-đun (module / 모듈) trở thành dịch vụ (service / 서비스), hàm (function / 함수) lời gọi (call / 호출) biến thành mạng (network / 네트워크) lời gọi (call / 호출). Ta nhận thêm serialization, hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도), authentication, khả năng quan sát (observability / 관측 가능성), triển khai (deployment / 배포), phiên bản (version / 버전) tính tương thích (compatibility / 호환성) và partial thất bại (failure / 실패).

Đổi lại có thể nhận independent triển khai (deployment / 배포), tài nguyên (resource / 자원) scaling, fault isolation và nhóm (team / 팀) autonomy. dịch vụ (service / 서비스) chỉ đáng giá khi lợi ích ranh giới (boundary / 경계) vượt distributed-systems tax.

> **Chuyển mạch:** Ở chặng này của **Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)**, **Dịch vụ (service / 서비스) ranh giới (boundary / 경계) có chi phí cố định** đã nêu tiêu chí phân biệt, còn **Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) là ranh giới (boundary / 경계) mạnh hơn endpoint** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Giao dịch (transaction / 트랜잭션) trở thành workflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) là ranh giới (boundary / 경계) mạnh hơn endpoint

Hai services dùng chung cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) và sửa trực tiếp bảng (table / 테이블) của nhau vẫn coupled mạnh dù có hai triển khai (deployment / 배포). Một dịch vụ (service / 서비스) ranh giới (boundary / 경계) trưởng thành thường đi cùng **dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권)**: dịch vụ (service / 서비스) khác tương tác qua đặc tả hợp đồng (contract / 계약) thay vì bypass đơn vị sở hữu (owner / 오너).

Điều này không bắt buộc “mỗi dịch vụ (service / 서비스) một cơ sở dữ liệu (database / 데이터베이스) máy chủ (server / 서버)”; điểm quan trọng là quyền thay đổi lược đồ (schema / 스키마)/dữ liệu (data / 데이터) thuộc một đơn vị sở hữu (owner / 오너) và truy cập (access / 접근) đường dẫn (path / 경로) được kiểm soát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)**, **Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) là ranh giới (boundary / 경계) mạnh hơn endpoint** đã nêu tiêu chí phân biệt, còn **Giao dịch (transaction / 트랜잭션) trở thành workflow** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Coupling có nhiều chiều** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giao dịch (transaction / 트랜잭션) trở thành workflow

Trong monolith + single cơ sở dữ liệu (database / 데이터베이스), nhiều bất biến (invariant / 불변식) có thể nằm trong ACID giao dịch (transaction / 트랜잭션). Sau khi tách dịch vụ (service / 서비스), giao dịch (transaction / 트랜잭션) xuyên ranh giới (boundary / 경계) trở nên đắt hoặc không khả dụng. nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) phải được modeling thành workflow với message, thử lại (retry / 재시도), idempotency và compensation.

Đây là lý do decomposition không chỉ là cắt gói (package / 패키지) thành REST APIs. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) thay đổi ngữ nghĩa (semantics / 의미론) của hệ thống.

> **Chuyển mạch:** Trong **Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)**, **Giao dịch (transaction / 트랜잭션) trở thành workflow** xác định đầu vào; **Coupling có nhiều chiều** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Khi modular monolith có lợi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coupling có nhiều chiều

Services có thể loosely coupled về mã (code / 코드) nhưng tightly coupled về triển khai (deployment / 배포) nếu mọi bản phát hành (release / 릴리스) phải phối hợp. Có thể độc lập triển khai (deployment / 배포) nhưng coupled về thời gian chạy (runtime / 런타임) nếu synchronous lời gọi (call / 호출) chuỗi (chain / 사슬) dài. Có thể tách thời gian chạy (runtime / 런타임) nhưng coupled về dữ liệu (data / 데이터) lược đồ (schema / 스키마).

Đánh giá ranh giới (boundary / 경계) cần nhìn **thay đổi (change / 변경) coupling, temporal coupling, dữ liệu (data / 데이터) coupling và organizational coupling**.

> **Chuyển mạch:** Ở chặng này của **Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)**, **Khi modular monolith có lợi** tiếp nhận điểm tựa từ **Coupling có nhiều chiều** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi dịch vụ (service / 서비스) extraction có tín hiệu tốt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi modular monolith có lợi

Nhóm (team / 팀) nhỏ, lĩnh vực (domain / 도메인) còn thay đổi nhanh, giao dịch (transaction / 트랜잭션) cross-domain nhiều và operational nền tảng (platform / 플랫폼) chưa trưởng thành thường hưởng lợi từ modular monolith. Debugging cục bộ (local / 로컬) đơn giản, refactor cross-module rẻ hơn và consistency dễ giữ.

Điều kiện là kiến trúc (architecture / 아키텍처) phải thực sự enforce mô-đun (module / 모듈) boundaries; nếu không, technical debt tích tụ và extraction sau này khó hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)**, **Khi dịch vụ (service / 서비스) extraction có tín hiệu tốt** tiếp nhận điểm tựa từ **Khi modular monolith có lợi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Di chuyển (migration / 마이그레이션) theo seam** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi dịch vụ (service / 서비스) extraction có tín hiệu tốt

Một mô-đun (module / 모듈) có scaling profile khác biệt, ranh giới bảo mật (security boundary / 보안 경계) riêng, bản phát hành (release / 릴리스) cadence độc lập hoặc nhóm (team / 팀) quyền sở hữu (ownership / 소유권) ổn định có thể là candidate tốt. Đường xử lý nóng (hot path / 핫 패스) cần tài nguyên (resource / 자원) đặc biệt cũng có thể justify extraction.

“Codebase lớn” một mình chưa đủ; repository có thể lớn nhưng mô-đun (module / 모듈) boundaries vẫn quản lý tốt.

> **Chuyển mạch:** Trong **Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)**, **Di chuyển (migration / 마이그레이션) theo seam** tiếp nhận điểm tựa từ **Khi dịch vụ (service / 서비스) extraction có tín hiệu tốt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reverse di chuyển (migration / 마이그레이션) cũng hợp lệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Di chuyển (migration / 마이그레이션) theo seam

Extraction an toàn thường bắt đầu từ seam rõ: define giao diện (interface / 인터페이스), ngăn direct cơ sở dữ liệu (database / 데이터베이스) truy cập (access / 접근), đưa phụ thuộc (dependency / 의존성) qua lớp trừu tượng (abstraction / 추상화), quan sát traffic, sau đó mới move hiện thực (implementation / 구현) ra tiến trình (process / 프로세스) riêng.

Mẫu (pattern / 패턴) strangler cho phép tuyến (route / 경로) từng năng lực (capability / 역량) sang dịch vụ (service / 서비스) mới thay vì rewrite toàn hệ thống. Branch-by-abstraction giúp mã (code / 코드) cũ và mới cùng tồn tại trong di chuyển (migration / 마이그레이션) mà không cần long-lived branch khổng lồ.

> **Chuyển mạch:** Ở chặng này của **Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)**, **Reverse di chuyển (migration / 마이그레이션) cũng hợp lệ** tiếp nhận điểm tựa từ **Di chuyển (migration / 마이그레이션) theo seam** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reverse di chuyển (migration / 마이그레이션) cũng hợp lệ

Nếu dịch vụ (service / 서비스) ranh giới (boundary / 경계) tạo nhiều operational chi phí (cost / 비용) nhưng không mang autonomy/isolation thực, merge services trở lại modular monolith có thể là quyết định đúng. kiến trúc (architecture / 아키텍처) evolution không phải con đường một chiều từ monolith → microservices.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Modular monolith vs services: ranh giới (boundary / 경계) economics và di chuyển (migration / 마이그레이션)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Reverse di chuyển (migration / 마이그레이션) cũng hợp lệ** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> tiến trình (process / 프로세스) ranh giới (boundary / 경계) là công cụ kinh tế-kỹ thuật. Modular monolith tối ưu cục bộ (local / 로컬) lập luận (reasoning / 추론) và giao dịch (transaction / 트랜잭션) simplicity; services mua autonomy/isolation bằng phân tán (distributed / 분산) độ phức tạp (complexity / 복잡도). ranh giới (boundary / 경계) tốt là nơi quyền sở hữu (ownership / 소유권), thay đổi (change / 변경) mẫu (pattern / 패턴), dữ liệu (data / 데이터) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) cùng có lý do tách — không phải nơi sơ đồ trông đẹp.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
