# Testing, xác minh (verification / 확인) và debugging

> **Mạch đọc:** Đặt **Testing, xác minh (verification / 확인) và debugging** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **kiểm thử (test / 테스트) là mẫu (sample / 표본), specification là thuộc tính (property / 속성)** sang **đơn vị (unit / 단위), tích hợp (integration / 통합), hệ thống (system / 시스템)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Software tính đúng đắn (correctness / 정확성) không thể dựa vào cảm giác “mã (code / 코드) nhìn đúng”. Ta cần nhiều techniques với strengths khác nhau: kiểu (type / 타입) checking, static phân tích (analysis / 분석), đơn vị (unit / 단위)/thuộc tính (property / 속성)/tích hợp (integration / 통합) tests, formal xác minh (verification / 확인), thời gian chạy (runtime / 런타임) assertions, khả năng quan sát (observability / 관측 가능성) và systematic debugging.

## Kiểm thử (test / 테스트) là mẫu (sample / 표본), specification là thuộc tính (property / 속성)

Example-based kiểm thử (test / 테스트) chọn đầu vào (input / 입력) và expected đầu ra (output / 출력) cụ thể. Nó tốt cho known cases/regressions nhưng không cover infinite lĩnh vực (domain / 도메인).

Property-based testing generate many inputs và check bất biến (invariant / 불변식): sorting đầu ra (output / 출력) ordered + permutation of đầu vào (input / 입력); serializer roundtrip; parser never crash on valid grammar. thuộc tính (property / 속성) buộc ta viết specification rõ hơn.

Fuzzing generate/mutate unexpected inputs để tìm crash/bảo mật (security / 보안) bugs, especially parsers and bản địa (native / 네이티브) mã (code / 코드).


> **Chuyển mạch:** Từ **kiểm thử (test / 테스트) là mẫu (sample / 표본), specification là thuộc tính (property / 속성)**, ta sang **đơn vị (unit / 단위), tích hợp (integration / 통합), hệ thống (system / 시스템)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đơn vị (unit / 단위), tích hợp (integration / 통합), hệ thống (system / 시스템)

Đơn vị (unit / 단위) kiểm thử (test / 테스트) isolate small thành phần (component / 컴포넌트), nhanh và precise diagnosis. kiểm thử tích hợp (integration test / 통합 테스트) kiểm tra boundaries thật như DB/mạng (network / 네트워크)/serialization. End-to-end kiểm thử (test / 테스트) cover whole luồng (flow / 흐름) nhưng chậm/flaky và khó localize thất bại (failure / 실패).

Testing pyramid không phải law; optimal mix phụ thuộc kiến trúc (architecture / 아키텍처)/rủi ro (risk / 위험). đặc tả hợp đồng (contract / 계약) tests hữu ích cho dịch vụ (service / 서비스) APIs.


> **Chuyển mạch:** Từ **đơn vị (unit / 단위), tích hợp (integration / 통합), hệ thống (system / 시스템)**, ta sang **Determinism và flaky tests** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Determinism và flaky tests

Flaky kiểm thử (test / 테스트) thường do hidden inputs: clock, random seed, luồng thực thi (thread / 스레드) scheduling, trạng thái dùng chung (shared state / 공유 상태), mạng (network / 네트워크), eventual consistency. Inject clock/random nguồn (source / 소스), isolate trạng thái (state / 상태), await conditions instead of fixed sleeps, điều khiển (control / 제어) tính đồng thời (concurrency / 동시성) where possible.

A flaky kiểm thử (test / 테스트) is not merely annoyance; it erodes trust in tín hiệu (signal / 신호).


> **Chuyển mạch:** Từ **Determinism và flaky tests**, ta sang **Static phân tích (analysis / 분석)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Static phân tích (analysis / 분석)

Trình biên dịch (compiler / 컴파일러) warnings, linters, dataflow phân tích (analysis / 분석), abstract interpretation và symbolic thực thi (execution / 실행) tìm classes bugs without running all paths concretely. They trade precision vs scalability, potentially false positives/negatives.

Undecidability explains why universal perfect analyzer for arbitrary programs impossible; tools solve restricted properties/các mô hình (models / 모델들).


> **Chuyển mạch:** Từ **Static phân tích (analysis / 분석)**, ta sang **Formal methods** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Formal methods

Hoare lô-gic (logic / 논리) uses `{P} C {Q}` precondition/program/postcondition. mô hình (model / 모델) checking explores finite trạng thái (state / 상태) mô hình (model / 모델). SMT solvers prove các ràng buộc (constraints / 제약조건들). Proof assistants verify machine-checkable proofs.

Formal methods are especially valuable for protocols, crypto, kernels, safety-critical mã (code / 코드), but chi phí (cost / 비용)/mô hình (model / 모델) fidelity matter. Proving wrong mô hình (model / 모델) perfectly still leaves real hệ thống (system / 시스템) bugs.


> **Chuyển mạch:** Từ **Formal methods**, ta sang **Debugging as hypothesis testing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Debugging as hypothesis testing

Good debugging vòng lặp (loop / 루프):

1. make thất bại (failure / 실패) reproducible/observable;
2. bound where divergence from expected first occurs;
3. form hypothesis tied to cơ chế (mechanism / 메커니즘);
4. gather discriminating bằng chứng (evidence / 증거);
5. thay đổi (change / 변경) one relevant variable or inspect trạng thái (state / 상태);
6. fix nguyên nhân gốc (root cause / 근본 원인) and add regression guard.

Random mã (code / 코드) changes are tìm kiếm (search / 검색) without mô hình (model / 모델).


> **Chuyển mạch:** Từ **Debugging as hypothesis testing**, ta sang **Logs, traces, metrics and debuggers** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Logs, traces, metrics and debuggers

Logs bản ghi (record / 레코드) discrete events/ngữ cảnh (context / 맥락); metrics aggregate numeric thời gian (time / 시간) series; traces connect nhân quả (causal / 인과적) đường đi của yêu cầu (request path / 요청 경로) across components; debugger inspects thực thi (execution / 실행) trạng thái (state / 상태). cốt lõi (core / 핵심) dumps/profile captures freeze bằng chứng (evidence / 증거) after thất bại (failure / 실패)/hiệu năng (performance / 성능) issue.

Each view loses different thông tin (information / 정보). High-cardinality IDs belong naturally in traces/logs more than naive chỉ số (metric / 지표) labels.


> **Chuyển mạch:** Từ **Logs, traces, metrics and debuggers**, ta sang **Reproduction and minimization** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Reproduction and minimization

Reduce failing đầu vào (input / 입력)/môi trường (environment / 환경) to smallest trường hợp (case / 사례). Delta debugging/minimal reproducer removes irrelevant variables and often exposes violated bất biến (invariant / 불변식).

For tính đồng thời (concurrency / 동시성), deterministic bản ghi (record / 레코드)/replay or stress scheduling can help; for phân tán (distributed / 분산) failures, fault injection/mạng (network / 네트워크) simulation reveals các giả định (assumptions / 가정들).


> **Chuyển mạch:** Từ **Reproduction and minimization**, ta sang **Tests and refactoring** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tests and refactoring

Tests provide behavioral đặc tả hợp đồng (contract / 계약) during refactor. But over-mocking hiện thực (implementation / 구현) details makes tests brittle and blocks nội bộ (internal / 내부) changes. kiểm thử (test / 테스트) observable đặc tả hợp đồng (contract / 계약)/invariants, use mocks at meaningful boundaries.


> **Chuyển mạch:** Từ **Tests and refactoring**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Confidence comes from **overlapping bằng chứng (evidence / 증거)**. Types prove one lớp (class / 클래스), tests mẫu (sample / 표본) behaviors, static phân tích (analysis / 분석) approximates paths, formal proof covers modeled properties, môi trường vận hành (production / 운영 환경) khả năng quan sát (observability / 관측 가능성) checks reality.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“100% mã (code / 코드) coverage = correct.”** Coverage only says mã (code / 코드) executed, not assertions meaningful or trạng thái (state / 상태) không gian (space / 공간) covered.

**“đơn vị (unit / 단위) tests should mock everything bên ngoài (external / 외부).”** Excessive mocks kiểm thử (test / 테스트) hiện thực (implementation / 구현) choreography, not tích hợp (integration / 통합) contracts.

**“Debugger is first công cụ (tool / 도구) for every issue.”** Logs/traces/profiles/reproducers may locate phân tán (distributed / 분산)/hiệu năng (performance / 성능) bugs better.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

[Computability limits](../00_computation_information/04_computability_and_limits.md) explain phân tích (analysis / 분석) boundaries. [Algorithm invariants](../01_algorithms_data_structures/00_algorithmic_thinking_and_correctness.md) inspire properties. [Observability/reliability](./05_fault_tolerance_observability_and_reliability.md) extends bằng chứng (evidence / 증거) to môi trường vận hành (production / 운영 환경).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 threat models and security principles](./00_threat_models_and_security_principles.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
