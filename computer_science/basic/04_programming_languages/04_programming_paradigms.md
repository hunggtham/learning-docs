# Imperative, object-oriented, functional và declarative paradigms

Programming paradigm (프로그래밍 패러다임 / mô hình lập trình) là một cách tổ chức state, computation và abstraction. Languages hiện đại thường multi-paradigm; điều có giá trị không phải gắn nhãn language mà hiểu mental model nào phù hợp problem.

## Imperative programming

Imperative style mô tả sequence commands thay đổi state: assign, loop, branch. Nó map khá tự nhiên tới machine state transitions và dễ kiểm soát step-by-step.

Điểm yếu xuất hiện khi mutable state lan rộng: muốn hiểu current value phải biết history of writes. Local mutation có thể rõ và efficient; global shared mutation khó reason.

## Object-oriented programming

OOP nhóm state + behavior quanh objects, encapsulation và interfaces. Polymorphism cho caller depend abstraction thay concrete implementation.

Inheritance là một mechanism, không phải essence duy nhất. Composition thường giảm coupling khi “has-a” relationship phù hợp hơn “is-a”. Liskov Substitution Principle yêu cầu subtype preserve behavioral expectations, không chỉ method signatures.

Domain model tốt không đồng nghĩa tạo class cho mọi noun. Value objects, services, modules và data-oriented structures đều có chỗ.

## Functional programming

Functional style nhấn mạnh functions as values, immutability, expression composition và pure functions. Referential transparency cho phép thay expression bằng value mà không đổi behavior, làm equational reasoning và testing dễ.

Real programs vẫn cần I/O/state. Functional systems isolate effects qua controlled boundaries, explicit state passing, monadic/effect systems hoặc runtime constructs tùy language.

Persistent immutable data structures dùng structural sharing để tránh full copy.

## Declarative programming

Declarative style mô tả **what** desired result/property hơn **how** sequence steps. SQL nói rows cần thỏa condition; query optimizer chọn scan/index/join plan. CSS mô tả constraints/rules; build systems mô tả dependencies.

Declarative abstraction mạnh khi engine có thể optimize strategy, nhưng performance debugging đòi hiểu engine execution model.

## Logic programming

Logic programming biểu diễn facts/rules và query; engine search/inference tìm substitutions. Prolog là example kinh điển. Dù ít dùng mainstream backend, ideas unification, constraints và rule engines xuất hiện trong solvers/static analysis.

## Event-driven và reactive

Event-driven systems react events/callbacks/messages thay central sequential flow. Reactive streams thêm propagation + backpressure concepts. UI, network servers và streaming pipelines dùng models này.

Hidden temporal dependencies có thể khó debug; explicit state machines/observable streams giúp structure.

## Paradigm là trade-off về state và control

Imperative: control explicit, state mutation direct.
OOP: state encapsulated theo identities/interfaces.
Functional: minimize mutation, compose transformations.
Declarative: specify relations/goals, engine control execution.

Không có paradigm universal winner. Database query bằng SQL declarative hợp hơn manual page loop; low-level driver imperative control cần thiết; business domain có thể dùng OOP + functional value transformations.

## Mental Model

> Paradigms khác nhau chủ yếu ở **state nằm đâu, control nằm đâu, và contracts được biểu đạt thế nào**. Hãy chọn model làm invariants và change boundaries rõ nhất.

## Common Misconceptions

**“OOP = inheritance.”** Encapsulation, abstraction, message/interface polymorphism quan trọng hơn inheritance hierarchy.

**“Functional = không có state.”** State/effects vẫn tồn tại nhưng được isolate/model khác.

**“Declarative code không có algorithm.”** Engine vẫn execute algorithms; declarative layer chuyển algorithm choice sang optimizer/runtime.

## Kết nối

[State/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) là common foundation; SQL được đào sâu ở [Relational Model](../05_data_databases/01_relational_model_keys_and_normalization.md); event/async ở [scope/control flow](./02_scope_closures_functions_and_control_flow.md) và [queues/backpressure](../08_software_systems/03_state_queues_backpressure_and_boundaries.md).
