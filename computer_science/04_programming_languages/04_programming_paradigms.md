# Imperative, object-oriented, functional và declarative paradigms

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Imperative, object-oriented, functional và declarative paradigms**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Imperative programming** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Object-oriented programming** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Programming paradigm (프로그래밍 패러다임 / mô hình lập trình) là một cách tổ chức trạng thái (state / 상태), computation và lớp trừu tượng (abstraction / 추상화). Languages hiện đại thường multi-paradigm; điều có giá trị không phải gắn nhãn ngôn ngữ (language / 언어) mà hiểu mô hình tư duy (mental model / 사고 모델) nào phù hợp bài toán (problem / 문제).

## Imperative programming

Imperative style mô tả chuỗi (sequence / 시퀀스) commands thay đổi trạng thái (state / 상태): assign, vòng lặp (loop / 루프), branch. Nó map khá tự nhiên tới machine trạng thái (state / 상태) transitions và dễ kiểm soát step-by-step.

Điểm yếu xuất hiện khi mutable trạng thái (state / 상태) lan rộng: muốn hiểu hiện tại (current / 현재) giá trị (value / 값) phải biết lịch sử (history / 이력) of writes. cục bộ (local / 로컬) mutation có thể rõ và efficient; toàn cục (global / 전역) dùng chung (shared / 공유) mutation khó reason.

> **Chuyển mạch:** Imperative code mô tả bước và state; object-oriented gom state với behavior, functional ưu tiên pure transformation, còn declarative mô tả kết quả cần đạt thay vì chuỗi thao tác.

## Object-oriented programming

OOP nhóm trạng thái (state / 상태) + hành vi (behavior / 동작) quanh objects, encapsulation và interfaces. Polymorphism cho caller depend lớp trừu tượng (abstraction / 추상화) thay concrete hiện thực (implementation / 구현).

Inheritance là một cơ chế (mechanism / 메커니즘), không phải essence duy nhất. Composition thường giảm coupling khi “has-a” relationship phù hợp hơn “is-a”. Liskov Substitution Principle yêu cầu subtype preserve behavioral expectations, không chỉ phương thức (method / 메서드) signatures.

Lĩnh vực (domain / 도메인) mô hình (model / 모델) tốt không đồng nghĩa tạo lớp (class / 클래스) cho mọi noun. giá trị (value / 값) objects, services, modules và data-oriented structures đều có chỗ.

> **Chuyển mạch:** Ở chặng này của **Imperative, object-oriented, functional và declarative paradigms**, **Functional programming** tiếp nhận điểm tựa từ **Object-oriented programming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Declarative programming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Functional programming

Functional style nhấn mạnh functions as values, immutability, expression composition và pure functions. Referential transparency cho phép thay expression bằng giá trị (value / 값) mà không đổi hành vi (behavior / 동작), làm equational lập luận (reasoning / 추론) và testing dễ.

Real programs vẫn cần I/O/trạng thái (state / 상태). Functional các hệ thống (systems / 시스템들) isolate effects qua controlled boundaries, tường minh (explicit / 명시적) trạng thái (state / 상태) passing, monadic/tác động (effect / 효과) các hệ thống (systems / 시스템들) hoặc thời gian chạy (runtime / 런타임) constructs tùy ngôn ngữ (language / 언어).

Persistent immutable dữ liệu (data / 데이터) structures dùng structural sharing để tránh full bản sao (copy / 복사).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Imperative, object-oriented, functional và declarative paradigms**, **Declarative programming** tiếp nhận điểm tựa từ **Functional programming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lô-gic (logic / 논리) programming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Declarative programming

Declarative style mô tả **what** desired kết quả (result / 결과)/thuộc tính (property / 속성) hơn **how** chuỗi (sequence / 시퀀스) steps. SQL nói rows cần thỏa điều kiện (condition / 조건); truy vấn (query / 쿼리) optimizer chọn scan/chỉ mục (index / 인덱스)/phép nối (join / 조인) plan. CSS mô tả các ràng buộc (constraints / 제약조건들)/rules; bản dựng (build / 빌드) các hệ thống (systems / 시스템들) mô tả dependencies.

Declarative lớp trừu tượng (abstraction / 추상화) mạnh khi engine có thể optimize chiến lược (strategy / 전략), nhưng hiệu năng (performance / 성능) debugging đòi hiểu engine mô hình thực thi (execution model / 실행 모델).

> **Chuyển mạch:** Trong **Imperative, object-oriented, functional và declarative paradigms**, **Lô-gic (logic / 논리) programming** tiếp nhận điểm tựa từ **Declarative programming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Event-driven và reactive** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lô-gic (logic / 논리) programming

Lô-gic (logic / 논리) programming biểu diễn facts/rules và truy vấn (query / 쿼리); engine tìm kiếm (search / 검색)/suy luận (inference / 추론) tìm substitutions. Prolog là example kinh điển. Dù ít dùng mainstream backend, ideas unification, các ràng buộc (constraints / 제약조건들) và quy tắc (rule / 규칙) engines xuất hiện trong solvers/static phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **Imperative, object-oriented, functional và declarative paradigms**, **Event-driven và reactive** tiếp nhận điểm tựa từ **Lô-gic (logic / 논리) programming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Paradigm là sự đánh đổi (trade-off / 트레이드오프) về trạng thái (state / 상태) và điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Event-driven và reactive

Event-driven các hệ thống (systems / 시스템들) react events/callbacks/messages thay central sequential luồng (flow / 흐름). Reactive streams thêm propagation + backpressure concepts. UI, mạng (network / 네트워크) servers và streaming pipelines dùng các mô hình (models / 모델들) này.

Hidden temporal dependencies có thể khó gỡ lỗi (debug / 디버그); tường minh (explicit / 명시적) trạng thái (state / 상태) machines/observable streams giúp cấu trúc (structure / 구조).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Imperative, object-oriented, functional và declarative paradigms**, **Paradigm là sự đánh đổi (trade-off / 트레이드오프) về trạng thái (state / 상태) và điều khiển (control / 제어)** tiếp nhận điểm tựa từ **Event-driven và reactive** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Paradigm là sự đánh đổi (trade-off / 트레이드오프) về trạng thái (state / 상태) và điều khiển (control / 제어)

Imperative: điều khiển (control / 제어) tường minh (explicit / 명시적), trạng thái (state / 상태) mutation direct.
OOP: trạng thái (state / 상태) encapsulated theo identities/interfaces.
Functional: minimize mutation, compose transformations.
Declarative: specify relations/goals, engine điều khiển (control / 제어) thực thi (execution / 실행).

Không có paradigm universal winner. truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리) bằng SQL declarative hợp hơn manual page vòng lặp (loop / 루프); low-level driver imperative điều khiển (control / 제어) cần thiết; nghiệp vụ (business / 비즈니스) lĩnh vực (domain / 도메인) có thể dùng OOP + functional giá trị (value / 값) transformations.

> **Chuyển mạch:** Trong **Imperative, object-oriented, functional và declarative paradigms**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Paradigm là sự đánh đổi (trade-off / 트레이드오프) về trạng thái (state / 상태) và điều khiển (control / 제어)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Paradigms khác nhau chủ yếu ở **trạng thái (state / 상태) nằm đâu, điều khiển (control / 제어) nằm đâu, và contracts được biểu đạt thế nào**. Hãy chọn mô hình (model / 모델) làm invariants và thay đổi (change / 변경) boundaries rõ nhất.

> **Chuyển mạch:** Ở chặng này của **Imperative, object-oriented, functional và declarative paradigms**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“OOP = inheritance.”** Encapsulation, lớp trừu tượng (abstraction / 추상화), message/giao diện (interface / 인터페이스) polymorphism quan trọng hơn inheritance hierarchy.

**“Functional = không có trạng thái (state / 상태).”** trạng thái (state / 상태)/effects vẫn tồn tại nhưng được isolate/mô hình (model / 모델) khác.

**“Declarative mã (code / 코드) không có thuật toán (algorithm / 알고리즘).”** Engine vẫn execute algorithms; declarative tầng (layer / 계층) chuyển thuật toán (algorithm / 알고리즘) choice sang optimizer/thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Imperative, object-oriented, functional và declarative paradigms**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[State/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) là dùng chung (common / 공통) foundation; SQL được đào sâu ở [Relational Model](../05_data_databases/01_relational_model_keys_and_normalization.md); sự kiện (event / 이벤트)/async ở [scope/control flow](./02_scope_closures_functions_and_control_flow.md) và [queues/backpressure](../08_software_systems/03_state_queues_backpressure_and_boundaries.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
