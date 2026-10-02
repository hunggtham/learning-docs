# Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Errors, exceptions, resources và runtime safety**. Route đi từ failure classification → result/exception propagation → resource acquisition/release → contracts và recovery, để lỗi, tài nguyên và tính an toàn được đánh giá trong cùng một đường chạy.

Thất bại (failure / 실패) là một phần của computation đặc tả hợp đồng (contract / 계약). Invalid đầu vào (input / 입력), unavailable mạng (network / 네트워크), exhausted bộ nhớ (memory / 메모리), violated bất biến (invariant / 불변식) và programmer bug không nên bị gộp thành một “lỗi (error / 오류)” mơ hồ. lỗi (error / 오류) mô hình (model / 모델) tốt giúp caller biết điều gì recoverable, tài nguyên (resource / 자원) nào cần cleanup và trạng thái (state / 상태) nào còn valid.

## Lỗi (error / 오류) categories

Có thể phân biệt rough categories: lĩnh vực (domain / 도메인) kiểm tra hợp lệ (validation / 검증) thất bại (failure / 실패); environmental/transient thất bại (failure / 실패) như hết thời gian chờ (timeout / 타임아웃); tài nguyên (resource / 자원) exhaustion; programmer bất biến (invariant / 불변식) violation; hardware/hệ thống (system / 시스템) thất bại (failure / 실패). ranh giới (boundary / 경계) không tuyệt đối nhưng khôi phục (recovery / 복구) chính sách (policy / 정책) khác nhau.

Thử lại (retry / 재시도) invalid password vô hạn không giúp; thử lại (retry / 재시도) transient 503 có thể hợp lý với backoff; thử lại (retry / 재시도) non-idempotent payment yêu cầu (request / 요청) mù quáng có thể duplicate charge.

> **Chuyển mạch:** Trong **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Return values, kết quả (result / 결과) types và exceptions** tiếp nhận điểm tựa từ **Lỗi (error / 오류) categories** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checked vs unchecked** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Return values, kết quả (result / 결과) types và exceptions

C-style lỗi (error / 오류) codes buộc caller check manually. Exceptions tách lan truyền lỗi (error propagation / 오류 전파) khỏi normal return nhưng tạo non-local điều khiển (control / 제어) luồng (flow / 흐름). kết quả (result / 결과)/Either types làm success/lỗi (error / 오류) tường minh (explicit / 명시적) trong hệ kiểu (type system / 타입 시스템) và compose transformations.

Không có cơ chế (mechanism / 메커니즘) nào tự đảm bảo good thiết kế (design / 설계). Quan trọng là encode ngữ cảnh (context / 맥락), preserve cause và tránh swallowing failures.

> **Chuyển mạch:** Ở chặng này của **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Checked vs unchecked** tiếp nhận điểm tựa từ **Return values, kết quả (result / 결과) types và exceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tài nguyên (resource / 자원) an toàn (safety / 안전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Checked vs unchecked

Checked exceptions buộc declaration/handling một số failures compile-time; unchecked giảm signature noise nhưng dễ bỏ sót. Ecosystems có trade-offs khác. Thay vì tranh luận tuyệt đối, hãy hỏi caller có meaningful khôi phục (recovery / 복구) không và đặc tả hợp đồng (contract / 계약) API cần expose gì.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Checked vs unchecked** nêu điều cần giải thích; **Tài nguyên (resource / 자원) an toàn (safety / 안전)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Exception an toàn (safety / 안전) và invariants** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tài nguyên (resource / 자원) an toàn (safety / 안전)

Bộ nhớ (memory / 메모리) GC không tự close socket/tệp (file / 파일)/DB liên kết (connection / 연결) đúng lúc. tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) cần deterministic cleanup. RAII, `try/finally`, `try-with-resources`, `defer`, ngữ cảnh (context / 맥락) manager đảm bảo cleanup cả normal và exceptional paths.

Cancellation cũng là error-like điều khiển (control / 제어) đường dẫn (path / 경로). Async tác vụ (task / 작업) cancelled phải bản phát hành (release / 릴리스) locks/connections/buffers và không để partial trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Tài nguyên (resource / 자원) an toàn (safety / 안전)** nêu điều cần giải thích; **Exception an toàn (safety / 안전) và invariants** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Panic/abort vs recoverable lỗi (error / 오류)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exception an toàn (safety / 안전) và invariants

Một thao tác (operation / 연산) có thể thất bại (fail / 실패) giữa chừng. Strong exception-safety style cố giữ trạng thái (state / 상태) unchanged nếu thất bại (fail / 실패); basic guarantee giữ invariants/no leaks dù trạng thái (state / 상태) thay đổi. cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) quay lui (rollback / 롤백) là analogous cơ chế (mechanism / 메커니즘) ở persistent trạng thái (state / 상태) tầng (layer / 계층).

> **Chuyển mạch:** Ở chặng này của **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Panic/abort vs recoverable lỗi (error / 오류)** tiếp nhận điểm tựa từ **Exception an toàn (safety / 안전) và invariants** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) an toàn (safety / 안전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Panic/abort vs recoverable lỗi (error / 오류)

Bất biến (invariant / 불변식) corruption đôi khi không nên tiếp tục cục bộ (local / 로컬) khôi phục (recovery / 복구) vì trạng thái (state / 상태) không trustworthy. Fail-fast có thể an toàn hơn silently continuing. Nhưng crash whole tiến trình (process / 프로세스) có blast radius; supervision/restart kiến trúc (architecture / 아키텍처) có thể isolate failures.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Bộ nhớ (memory / 메모리) an toàn (safety / 안전)** tiếp nhận điểm tựa từ **Panic/abort vs recoverable lỗi (error / 오류)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểu (type / 타입) an toàn (safety / 안전) và thời gian chạy (runtime / 런타임) an toàn (safety / 안전) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) an toàn (safety / 안전)

Memory-safe môi trường (environment / 환경) ngăn classes lỗi như use-after-free, out-of-bounds hoặc dangling references ở safe subset/thời gian chạy (runtime / 런타임). C/C++ đòi discipline/tooling; Rust quyền sở hữu (ownership / 소유권) enforces many properties statically; Java/.NET checks + GC. bộ nhớ (memory / 메모리) an toàn (safety / 안전) không ngăn lô-gic (logic / 논리) bugs, injection hay authorization errors.

> **Chuyển mạch:** Trong **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Kiểu (type / 타입) an toàn (safety / 안전) và thời gian chạy (runtime / 런타임) an toàn (safety / 안전) khác nhau** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) an toàn (safety / 안전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Defensive programming vs contracts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểu (type / 타입) an toàn (safety / 안전) và thời gian chạy (runtime / 런타임) an toàn (safety / 안전) khác nhau

Type-safe program có thể divide by zero, hết thời gian chờ (timeout / 타임아웃), OOM hoặc deadlock. hệ kiểu (type system / 타입 시스템) chỉ cover properties được mô hình (model / 모델). Richer types/tác động (effect / 효과) các hệ thống (systems / 시스템들) có thể encode thêm states, nhưng real world luôn có bên ngoài (external / 외부) failures.

> **Chuyển mạch:** Ở chặng này của **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Defensive programming vs contracts** tiếp nhận điểm tựa từ **Kiểu (type / 타입) an toàn (safety / 안전) và thời gian chạy (runtime / 런타임) an toàn (safety / 안전) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Defensive programming vs contracts

Checking everything everywhere có thể hide programming bugs hoặc duplicate kiểm tra hợp lệ (validation / 검증). Validate at trust boundaries, assert nội bộ (internal / 내부) invariants, encode impossible states in types khi hợp lý, và document đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Defensive programming vs contracts** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> lỗi (error / 오류) handling là **state-transition thiết kế (design / 설계) dưới thất bại (failure / 실패)**. Hỏi thất bại (failure / 실패) xảy ra ở đâu, trạng thái (state / 상태) còn valid không, thao tác (operation / 연산) có retry-safe không, resources nào đang held, và ranh giới (boundary / 경계) nào chịu trách nhiệm khôi phục (recovery / 복구).

> **Chuyển mạch:** Trong **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Catch Exception rồi log là xử lý lỗi.”** Nếu caller cần biết thất bại (failure / 실패) hoặc giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) chưa khôi phục (recovery / 복구), swallowing exception làm hệ thống khó đúng hơn.

**“GC xử lý mọi tài nguyên (resource / 자원) cleanup.”** bên ngoài (external / 외부) resources cần tường minh (explicit / 명시적)/deterministic thời gian tồn tại (lifetime / 수명).

**“thử lại (retry / 재시도) làm hệ thống reliable.”** thử lại (retry / 재시도) có thể khuếch đại overload hoặc duplicate side effects nếu thiếu backoff/idempotency.

> **Chuyển mạch:** Ở chặng này của **Errors, exceptions, resources và thời gian chạy (runtime / 런타임) an toàn (safety / 안전)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Transactions](../05_data_databases/02_transactions_acid_and_concurrency_control.md) cung cấp atomic khôi phục (recovery / 복구) cho DB trạng thái (state / 상태); [idempotency](../08_software_systems/04_time_serialization_and_idempotency.md) làm retries an toàn hơn; [fault tolerance](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) mở rộng lỗi (error / 오류) handling lên dịch vụ (service / 서비스)/hệ thống (system / 시스템) mức (level / 수준).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
