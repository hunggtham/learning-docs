# Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô-đun (module / 모듈) là đơn vị (unit / 단위) của responsibility và thay đổi (change / 변경)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Thông tin (information / 정보) hiding** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Software lớn không thể được hiểu toàn bộ cùng lúc. Modularity (모듈성 / tính mô-đun) chia hệ thống (system / 시스템) thành boundaries để mỗi phần có thể lập luận (reasoning / 추론), thay đổi và kiểm thử (test / 테스트) tương đối độc lập. Nhưng ranh giới (boundary / 경계) chỉ hữu ích khi giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약) rõ và thông tin (information / 정보) hiding đúng.

## Mô-đun (module / 모듈) là đơn vị (unit / 단위) của responsibility và thay đổi (change / 변경)

Mô-đun (module / 모듈) có thể là hàm (function / 함수), lớp (class / 클래스), gói (package / 패키지), thư viện (library / 라이브러리), dịch vụ (service / 서비스) hoặc subsystem. Ranh giới tốt thường gom những decisions có lý do thay đổi cùng nhau và che hiện thực (implementation / 구현) details khỏi consumers.

High cohesion nghĩa elements trong mô-đun (module / 모듈) phục vụ purpose liên quan. Low coupling nghĩa mô-đun (module / 모듈) phụ thuộc ít các giả định (assumptions / 가정들) về internals của mô-đun (module / 모듈) khác.

Coupling không thể bằng zero; mục tiêu là dependencies tường minh (explicit / 명시적) và stable.

> **Chuyển mạch:** Module gom responsibility và change boundary; information hiding che detail, còn interface/API contract tiếp theo giữ consumer độc lập với implementation.

## Thông tin (information / 정보) hiding

Parnas' principle: mô-đun (module / 모듈) nên hide thiết kế (design / 설계) decisions likely to thay đổi (change / 변경). Encapsulation không chỉ `private` fields; nó che biểu diễn (representation / 표현) và expose operations theo ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약).

Ví dụ ngăn xếp (stack / 스택) expose push/pop thay vì cho caller sửa nội bộ (internal / 내부) array chỉ mục (index / 인덱스). cơ sở dữ liệu (database / 데이터베이스) repository expose truy vấn (query / 쿼리) intent thay vì leak liên kết (connection / 연결)/cursor vòng đời (lifecycle / 생명주기) nếu caller không cần.

> **Chuyển mạch:** Ở chặng này của **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Giao diện (interface / 인터페이스) vs hiện thực (implementation / 구현)** tiếp nhận điểm tựa từ **Thông tin (information / 정보) hiding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phụ thuộc (dependency / 의존성) inversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giao diện (interface / 인터페이스) vs hiện thực (implementation / 구현)

Giao diện (interface / 인터페이스) mô tả operations/hành vi (behavior / 동작) bên tiêu thụ (consumer / 소비자) có thể dựa; hiện thực (implementation / 구현) có freedom nội bộ. Nhưng giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약) rộng hơn phương thức (method / 메서드) signature: thứ tự (ordering / 순서), nullability, errors, tính đồng thời (concurrency / 동시성), idempotency, độ trễ (latency / 지연 시간) expectations và tính tương thích (compatibility / 호환성) đều có thể observable.

Một API trả danh sách (list / 목록) nhưng không nói thứ tự (ordering / 순서) có stable không; máy khách (client / 클라이언트) vô tình dựa hiện tại (current / 현재) thứ tự (order / 순서); hiện thực (implementation / 구현) đổi kế hoạch truy vấn (query plan / 쿼리 계획) làm thứ tự (order / 순서) khác — đó là hidden đặc tả hợp đồng (contract / 계약) phụ thuộc (dependency / 의존성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Phụ thuộc (dependency / 의존성) inversion** tiếp nhận điểm tựa từ **Giao diện (interface / 인터페이스) vs hiện thực (implementation / 구현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **API thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성) inversion

High-level chính sách (policy / 정책) không nên phụ thuộc trực tiếp low-level volatile details nếu ranh giới (boundary / 경계) lớp trừu tượng (abstraction / 추상화) hợp lý. phụ thuộc (dependency / 의존성) inversion đưa giao diện (interface / 인터페이스) theo needs của high-level mô-đun (module / 모듈), hiện thực (implementation / 구현) adapters implement.

Nhưng tạo giao diện (interface / 인터페이스) cho mọi lớp (class / 클래스) không tự động decouple; lớp trừu tượng (abstraction / 추상화) vô nghĩa chỉ tăng indirection. giao diện (interface / 인터페이스) đáng có khi có genuine ranh giới (boundary / 경계)/variation/testing quyền sở hữu (ownership / 소유권).

> **Chuyển mạch:** Trong **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **API thiết kế (design / 설계)** tiếp nhận điểm tựa từ **Phụ thuộc (dependency / 의존성) inversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## API thiết kế (design / 설계)

Good API làm correct use dễ và misuse khó. Types encode valid states; names match lĩnh vực (domain / 도메인); default safe; errors tường minh (explicit / 명시적); operations composable.

Backward tính tương thích (compatibility / 호환성) là đặc tả hợp đồng (contract / 계약) evolution bài toán (problem / 문제). Adding optional phản hồi (response / 응답) trường dữ liệu (field / 필드) usually easier than removing/renaming required trường dữ liệu (field / 필드). ngữ nghĩa (semantic / 의미적) hành vi (behavior / 동작) changes can break clients even if lược đồ (schema / 스키마) unchanged.

> **Chuyển mạch:** Ở chặng này của **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Versioning** tiếp nhận điểm tựa từ **API thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cục bộ (local / 로컬) vs remote giao diện (interface / 인터페이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Versioning

Ngữ nghĩa (semantic / 의미적) Versioning convention major/minor/patch chỉ hữu ích nếu dự án (project / 프로젝트) defines API công khai (public API / 공개 API) and follows ngữ nghĩa (semantics / 의미론). phân tán (distributed / 분산) HTTP APIs may use URL/header versions, additive evolution or năng lực (capability / 역량) negotiation.

Phiên bản (version / 버전) proliferation creates maintenance burden; prefer compatible evolution when possible.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Cục bộ (local / 로컬) vs remote giao diện (interface / 인터페이스)** tiếp nhận điểm tựa từ **Versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đặc tả hợp đồng (contract / 계약) testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cục bộ (local / 로컬) vs remote giao diện (interface / 인터페이스)

Remote Procedure lời gọi (call / 호출) can look like cục bộ (local / 로컬) hàm (function / 함수) but ngữ nghĩa (semantics / 의미론) differ: độ trễ (latency / 지연 시간) orders of magnitude, hết thời gian chờ (timeout / 타임아웃), partial thất bại (failure / 실패), retries, serialization and phiên bản (version / 버전) skew. Treating remote API exactly like cục bộ (local / 로컬) phương thức (method / 메서드) is a classic leaky lớp trừu tượng (abstraction / 추상화).

A remote lời gọi (call / 호출) needs hết thời gian chờ (timeout / 타임아웃), cancellation, idempotency/thử lại (retry / 재시도) chính sách (policy / 정책) and khả năng quan sát (observability / 관측 가능성). Chatty object-style APIs that are fine in-process may be terrible over mạng (network / 네트워크).

> **Chuyển mạch:** Trong **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Đặc tả hợp đồng (contract / 계약) testing** tiếp nhận điểm tựa từ **Cục bộ (local / 로컬) vs remote giao diện (interface / 인터페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conway's Law intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đặc tả hợp đồng (contract / 계약) testing

Bên tiêu thụ (consumer / 소비자)/provider đặc tả hợp đồng (contract / 계약) tests verify tương tác (interaction / 상호작용) các giả định (assumptions / 가정들) without full E2E môi trường (environment / 환경). But đặc tả hợp đồng (contract / 계약) should focus observable hành vi (behavior / 동작), not freeze nội bộ (internal / 내부) hiện thực (implementation / 구현).

Schemas like OpenAPI/Protobuf capture structural đặc tả hợp đồng (contract / 계약); ngữ nghĩa (semantic / 의미적) các ràng buộc (constraints / 제약조건들) still need documentation/tests.

> **Chuyển mạch:** Ở chặng này của **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Conway's Law intuition** tiếp nhận điểm tựa từ **Đặc tả hợp đồng (contract / 계약) testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conway's Law intuition

Hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처) often mirrors communication cấu trúc (structure / 구조) of organization. nhóm (team / 팀) boundaries influence dịch vụ (service / 서비스)/mô-đun (module / 모듈) boundaries because coordination chi phí (cost / 비용) is real. Modular thiết kế (design / 설계) is technical + organizational.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Conway's Law intuition** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> A ranh giới (boundary / 경계) is valuable when it **contains thay đổi (change / 변경) and preserves a small stable đặc tả hợp đồng (contract / 계약)**. Ask what các giả định (assumptions / 가정들) cross ranh giới (boundary / 경계), not how many interfaces/classes exist.

> **Chuyển mạch:** Trong **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“More layers = better kiến trúc (architecture / 아키텍처).”** Layers without distinct responsibility add độ trễ (latency / 지연 시간)/indirection.

**“giao diện (interface / 인터페이스) means lớp trừu tượng (abstraction / 추상화).”** giao diện (interface / 인터페이스) with one hiện thực (implementation / 구현) mirroring every nội bộ (internal / 내부) phương thức (method / 메서드) may reveal rather than hide thiết kế (design / 설계).

**“RPC is just hàm (function / 함수) lời gọi (call / 호출) across mạng (network / 네트워크).”** Remote calls have fundamentally different thất bại (failure / 실패)/độ trễ (latency / 지연 시간) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Ở chặng này của **Lớp trừu tượng (abstraction / 추상화), modularity, giao diện (interface / 인터페이스) và API contracts**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Abstraction/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) is foundation. [Distributed failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) explains remote boundaries. [Version control/build](./01_version_control_build_link_and_packages.md) manages mô-đun (module / 모듈) evolution physically.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
