# Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. trường hợp kiểm thử (test case / 테스트 케이스) chỉ có giá trị khi có oracle đủ mạnh** đưa mô hình vào một trường hợp đủ cụ thể để quan sát; sau đó sang **2. đơn vị (unit / 단위) kiểm thử (test / 테스트) và hiện thực (implementation / 구현) coupling** để kiểm tra nhận định bằng tiêu chí hoặc phép thử. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Bộ kiểm thử (test suite / 테스트 스위트) tốt không phải suite có nhiều kiểm thử (test / 테스트) nhất. Nó là một **hệ thống bằng chứng** giúp nhóm (team / 팀) phát hiện regression với phản hồi (feedback / 피드백) đủ nhanh và confidence phù hợp rủi ro (risk / 위험). Khi software lớn lên, kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) cần phân bổ bằng chứng (evidence / 증거) theo ranh giới (boundary / 경계): lô-gic (logic / 논리) cục bộ, giao thức (protocol / 프로토콜) giữa components, tính đồng thời (concurrency / 동시성)/timing, hành vi khi thất bại (failure behavior / 실패 동작) và các giả định (assumptions / 가정들) chỉ xuất hiện dưới môi trường vận hành (production / 운영 환경) tải công việc (workload / 워크로드).

Điểm cốt lõi là kiểm thử (test / 테스트) không chứng minh “hệ thống (system / 시스템) đúng trong mọi trường hợp”. kiểm thử (test / 테스트) lấy mẫu thực thi (execution / 실행) không gian (space / 공간). Vì vậy thiết kế kiểm thử (test / 테스트) tốt bắt đầu từ **bất biến (invariant / 불변식), thất bại (failure / 실패) mô hình (model / 모델) và oracle** chứ không bắt đầu từ số lượng trường hợp kiểm thử (test case / 테스트 케이스).

## 1. trường hợp kiểm thử (test case / 테스트 케이스) chỉ có giá trị khi có oracle đủ mạnh

Một kiểm thử (test / 테스트) gồm đầu vào (input / 입력)/hành động (action / 동작) và cách quyết định kết quả có đúng hay không. Phần quyết định đó là **oracle kiểm thử (test oracle / 테스트 오라클)**.

Oracle có thể đơn giản như `expected == actual`, nhưng ở hệ thống phức tạp nó có thể là bất biến (invariant / 불변식):

```text
balance không âm
committed transaction survive crash model đã hứa
consumer xử lý duplicate mà không tạo side effect thứ hai
schema mới vẫn đọc được message cũ
principal không truy cập resource ngoài policy
```

Nếu oracle yếu, kiểm thử (test / 테스트) có thể chạy đúng đường dẫn (path / 경로) nhưng không phát hiện bug. Đây là lý do mã (code / 코드) coverage cao không tự tạo confidence cao.

> **Chuyển mạch:** Test case cần oracle mạnh; unit tests dễ couple implementation, còn contract/property/mutation tests mở rộng bằng chứng tới boundary, behavior và production-like invariants.

## 2. đơn vị (unit / 단위) kiểm thử (test / 테스트) và hiện thực (implementation / 구현) coupling

Đơn vị (unit / 단위) kiểm thử (test / 테스트) nhanh và cục bộ (local / 로컬) nhưng dễ brittle nếu assert private hiện thực (implementation / 구현) details. kiểm thử (test / 테스트) nên ưu tiên observable hành vi (behavior / 동작)/bất biến (invariant / 불변식) thay vì mirror từng phương thức (method / 메서드) lời gọi (call / 호출) nội bộ.

Mock mọi phụ thuộc (dependency / 의존성) có thể tạo “green tests” cho một thế giới giả mà môi trường vận hành (production / 운영 환경) components không thực sự tương thích.

Mock hữu ích khi cần kiểm soát rare lỗi (error / 오류) hoặc tách pure lô-gic (logic / 논리) khỏi expensive phụ thuộc (dependency / 의존성). Nhưng nếu kiểm thử (test / 테스트) bắt đầu mô phỏng giao thức (protocol / 프로토콜), giao dịch (transaction / 트랜잭션) hoặc mạng (network / 네트워크) hành vi (behavior / 동작) bằng hàng chục expectations thủ công, fake world có thể khác môi trường vận hành (production / 운영 환경) world nhiều hơn nhóm (team / 팀) tưởng.

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **2. đơn vị (unit / 단위) kiểm thử (test / 테스트) và hiện thực (implementation / 구현) coupling** đã nêu tiêu chí phân biệt, còn **3. đặc tả hợp đồng (contract / 계약) testing kiểm tra agreement tại ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **4. Property-based testing biến yêu cầu (requirement / 요구사항) thành bất biến (invariant / 불변식) tổng quát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. đặc tả hợp đồng (contract / 계약) testing kiểm tra agreement tại ranh giới (boundary / 경계)

Dịch vụ (service / 서비스)/API tích hợp (integration / 통합) thường hỏng ở các giả định (assumptions / 가정들) về yêu cầu (request / 요청)/phản hồi (response / 응답)/lược đồ (schema / 스키마). **Kiểm thử hợp đồng (contract testing / 계약 테스트)** kiểm tra provider/bên tiêu thụ (consumer / 소비자) có cùng hiểu giao diện (interface / 인터페이스) mà không cần dựng toàn hệ thống (system / 시스템) mỗi lần.

Consumer-driven đặc tả hợp đồng (contract / 계약) hữu ích khi provider cần biết hành vi (behavior / 동작) nào consumers thật sự phụ thuộc. Tuy nhiên đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) không thay end-to-end kiểm thử (test / 테스트) cho mạng (network / 네트워크), auth, triển khai (deployment / 배포), routing hoặc dùng chung (shared / 공유) hạ tầng (infrastructure / 인프라).

Đặc tả hợp đồng (contract / 계약) cũng không chỉ là JSON shape. Behavioral đặc tả hợp đồng (contract / 계약) có thể gồm status ngữ nghĩa (semantics / 의미론), idempotency, thứ tự (ordering / 순서), hết thời gian chờ (timeout / 타임아웃) expectation, pagination, lỗi (error / 오류) ánh xạ (mapping / 매핑) và backward tính tương thích (compatibility / 호환성).

Nếu lược đồ (schema / 스키마) vẫn parse nhưng ngữ nghĩa (semantics / 의미론) đổi từ “missing means zero” thành “missing means unknown”, structural đặc tả hợp đồng (contract / 계약) có thể xanh trong khi nghiệp vụ (business / 비즈니스) đặc tả hợp đồng (contract / 계약) đã vỡ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **3. đặc tả hợp đồng (contract / 계약) testing kiểm tra agreement tại ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **4. Property-based testing biến yêu cầu (requirement / 요구사항) thành bất biến (invariant / 불변식) tổng quát** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **5. Metamorphic testing hữu ích khi không biết chính xác (exact / 정확한) expected đầu ra (output / 출력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Property-based testing biến yêu cầu (requirement / 요구사항) thành bất biến (invariant / 불변식) tổng quát

Thay vì viết vài examples, **kiểm thử dựa trên thuộc tính (property-based testing / 속성 기반 테스트)** sinh nhiều inputs để kiểm tra bất biến (invariant / 불변식) như round-trip encode/decode, sorting preserves multiset hoặc parser không crash với arbitrary valid đầu vào (input / 입력).

Giá trị lớn nhất là buộc ta phát biểu thuộc tính (property / 속성) tổng quát. Shrinking giúp rút failing trường hợp (case / 사례) lớn về counterexample nhỏ dễ hiểu.

Ví dụ serializer có thể được kiểm tra bằng:

```text
decode(encode(x)) ≈ x
```

Dấu `≈` quan trọng: floating điểm (point / 지점), unordered maps hoặc canonicalization có thể làm chính xác (exact / 정확한) byte equality không phải bất biến (invariant / 불변식) đúng. kiểm thử (test / 테스트) tốt phải phát biểu ngữ nghĩa (semantic / 의미적) equivalence đúng với lĩnh vực (domain / 도메인).

> **Chuyển mạch:** Trong **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **5. Metamorphic testing hữu ích khi không biết chính xác (exact / 정확한) expected đầu ra (output / 출력)** tiếp nhận điểm tựa từ **4. Property-based testing biến yêu cầu (requirement / 요구사항) thành bất biến (invariant / 불변식) tổng quát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Mutation testing đo sức mạnh của assertion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Metamorphic testing hữu ích khi không biết chính xác (exact / 정확한) expected đầu ra (output / 출력)

Có bài toán khó có oracle tuyệt đối cho từng đầu vào (input / 입력), ví dụ optimizer, tìm kiếm (search / 검색) ranking hoặc numerical solver. Khi đó có thể kiểm tra **quan hệ biến hình (metamorphic relation)**.

Nếu quy mô (scale / 규모) toàn bộ đơn vị đo theo cùng factor, hoặc biến đổi đầu vào (input / 입력) theo một symmetry mà bài toán (problem / 문제) giữ nguyên, đầu ra (output / 출력) cần biến đổi theo quan hệ (relation / 관계) dự kiến.

Metamorphic testing không thay lĩnh vực (domain / 도메인) oracle, nhưng giúp kiểm tra consistency khi expected answer quá đắt hoặc khó tính trước.

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **6. Mutation testing đo sức mạnh của assertion** tiếp nhận điểm tựa từ **5. Metamorphic testing hữu ích khi không biết chính xác (exact / 정확한) expected đầu ra (output / 출력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. kiểm thử tích hợp (integration test / 통합 테스트) cần real ngữ nghĩa (semantics / 의미론) ở nơi mock nguy hiểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Mutation testing đo sức mạnh của assertion

Mã (code / 코드) coverage chỉ nói line đã chạy, không nói assertion có khả năng bắt lỗi. **Kiểm thử đột biến (mutation testing / 변이 테스트)** cố thay operator/điều kiện (condition / 조건) nhỏ rồi xem tests có thất bại (fail / 실패) không.

Mutation sống sót có thể chỉ ra assertion yếu, unreachable hành vi (behavior / 동작) hoặc mã (code / 코드) không quan trọng. chi phí (cost / 비용) chạy cao nên thường dùng có chọn lọc ở lô-gic (logic / 논리) trọng yếu (critical / 중요) thay vì toàn monorepo mỗi lần ghi nhận (commit / 커밋).

Mutation score cũng không nên thành KPI tuyệt đối. Nếu nhóm (team / 팀) viết assertions vô nghĩa chỉ để “kill mutant”, chỉ số (metric / 지표) bắt đầu bị Goodhart hóa thay vì tăng tính đúng đắn (correctness / 정확성) bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **7. kiểm thử tích hợp (integration test / 통합 테스트) cần real ngữ nghĩa (semantics / 의미론) ở nơi mock nguy hiểm** tiếp nhận điểm tựa từ **6. Mutation testing đo sức mạnh của assertion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. tính đồng thời (concurrency / 동시성) testing không thể thay proof bằng “chạy nhiều lần”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. kiểm thử tích hợp (integration test / 통합 테스트) cần real ngữ nghĩa (semantics / 의미론) ở nơi mock nguy hiểm

Cơ sở dữ liệu (database / 데이터베이스), broker, filesystem, TLS và giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) khó mock chính xác. Containerized/ephemeral dependencies giúp kiểm thử tích hợp (integration test / 통합 테스트) gần môi trường vận hành (production / 운영 환경) hơn nhưng tăng startup/flakiness chi phí (cost / 비용).

Điểm chọn ranh giới (boundary / 경계) dựa vào rủi ro (risk / 위험). Nếu bug nguy hiểm nhất là giao dịch (transaction / 트랜잭션) isolation, cần kiểm thử (test / 테스트) với cơ sở dữ liệu (database / 데이터베이스) engine thật. Nếu bug nằm ở pure calculation, dựng cả cluster chỉ làm phản hồi (feedback / 피드백) chậm hơn.

Kiểm thử (test / 테스트) pyramid vì vậy không nên được hiểu là luật hình học cố định; phân phối (distribution / 분포) phụ thuộc hệ thống (system / 시스템) boundaries, chi phí (cost / 비용) of thất bại (failure / 실패) và tốc độ phản hồi (feedback / 피드백).

> **Chuyển mạch:** Trong **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **8. tính đồng thời (concurrency / 동시성) testing không thể thay proof bằng “chạy nhiều lần”** tiếp nhận điểm tựa từ **7. kiểm thử tích hợp (integration test / 통합 테스트) cần real ngữ nghĩa (semantics / 의미론) ở nơi mock nguy hiểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. thất bại (failure / 실패) injection kiểm tra đặc tả hợp đồng (contract / 계약) khi lower tầng (layer / 계층) không còn happy đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. tính đồng thời (concurrency / 동시성) testing không thể thay proof bằng “chạy nhiều lần”

Race điều kiện (condition / 조건) phụ thuộc interleaving. vòng lặp (loop / 루프) một kiểm thử (test / 테스트) 10,000 lần có thể tăng xác suất lộ bug nhưng không chứng minh giao thức (protocol / 프로토콜) đúng.

Kiểm thử (test / 테스트) tính đồng thời (concurrency / 동시성) nên làm rõ bất biến (invariant / 불변식) và chủ động tạo pressure lên scheduling ranh giới (boundary / 경계): barriers/latches để đồng bộ start, deterministic scheduler khi khung phần mềm (framework / 프레임워크) hỗ trợ, randomized scheduling, stress tải công việc (workload / 워크로드) và sanitizer/race detector.

Nếu bug biến mất khi thêm logging/sleep, đó có thể là Heisenbug vì instrumentation đổi timing. `sleep(100)` không phải synchronization proof.

Tính đúng đắn (correctness / 정확성) lập luận (reasoning / 추론) vẫn phải quay về happens-before/quyền sở hữu (ownership / 소유권). Xem [đường correctness CPU → language memory model](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **8. tính đồng thời (concurrency / 동시성) testing không thể thay proof bằng “chạy nhiều lần”** xác định đầu vào; **9. thất bại (failure / 실패) injection kiểm tra đặc tả hợp đồng (contract / 계약) khi lower tầng (layer / 계층) không còn happy đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. Crash consistency cần kiểm thử (test / 테스트) interruption points, không chỉ restart** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. thất bại (failure / 실패) injection kiểm tra đặc tả hợp đồng (contract / 계약) khi lower tầng (layer / 계층) không còn happy đường dẫn (path / 경로)

Nhiều môi trường vận hành (production / 운영 환경) bất biến (invariant / 불변식) chỉ có ý nghĩa khi thành phần (component / 컴포넌트) thất bại (fail / 실패) giữa chừng. **Tiêm lỗi (fault injection / 장애 주입)** chủ động tạo thất bại (failure / 실패) ở ranh giới (boundary / 경계) để kiểm tra khôi phục (recovery / 복구) hành vi (behavior / 동작).

Ví dụ có thể ngắt mạng (network / 네트워크) giữa yêu cầu (request / 요청) và phản hồi (response / 응답), kill tiến trình (process / 프로세스) trước/sau WAL flush, làm phụ thuộc (dependency / 의존성) hết thời gian chờ (timeout / 타임아웃), trả disk-full, làm replica lag hoặc làm certificate hết hạn trong môi trường (environment / 환경) kiểm soát.

Mỗi injection cần gắn với hypothesis:

```text
failure xảy ra ở đâu?
invariant nào vẫn phải giữ?
caller thấy outcome nào?
retry có an toàn không?
state nào cần recover?
evidence nào chứng minh recovery thành công?
```

Nếu kiểm thử (test / 테스트) chỉ kiểm tra dịch vụ (service / 서비스) “không crash” mà không kiểm tra trạng thái (state / 상태) sau khôi phục (recovery / 복구), oracle vẫn quá yếu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **9. thất bại (failure / 실패) injection kiểm tra đặc tả hợp đồng (contract / 계약) khi lower tầng (layer / 계층) không còn happy đường dẫn (path / 경로)** xác định đầu vào; **10. Crash consistency cần kiểm thử (test / 테스트) interruption points, không chỉ restart** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **11. mạng (network / 네트워크) fault không chỉ là disconnect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Crash consistency cần kiểm thử (test / 테스트) interruption points, không chỉ restart

Durability bug thường nằm giữa hai persistent transitions. kiểm thử (test / 테스트) hữu ích cần inject crash tại các điểm khác nhau:

```text
trước log flush
sau log flush nhưng trước data flush
sau output file nhưng trước metadata publication
sau local persist nhưng trước replica acknowledgement
```

Sau restart phải kiểm tra committed trạng thái (state / 상태), uncommitted trạng thái (state / 상태), idempotent khôi phục (recovery / 복구) và siêu dữ liệu (metadata / 메타데이터) consistency.

Đây là lý do cơ sở dữ liệu (database / 데이터베이스)/filesystem testing cần state-machine lập luận (reasoning / 추론) thay vì chỉ “restart xong app lên được”. Đọc [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Chuyển mạch:** Trong **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **11. mạng (network / 네트워크) fault không chỉ là disconnect** tiếp nhận điểm tựa từ **10. Crash consistency cần kiểm thử (test / 테스트) interruption points, không chỉ restart** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Chaos kỹ thuật (engineering / 엔지니어링) là experiment trên bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. mạng (network / 네트워크) fault không chỉ là disconnect

Phân tán (distributed / 분산) các hệ thống (systems / 시스템들) có asymmetric thất bại (failure / 실패), delay, duplication, reordering và partition. Inject `connection refused` chỉ cover một phần nhỏ.

Máy khách (client / 클라이언트) có thể gửi yêu cầu (request / 요청) thành công nhưng mất phản hồi (response / 응답); từ caller perspective kết quả (outcome / 결과) trở thành ambiguous. thử lại (retry / 재시도) chỉ an toàn nếu thao tác (operation / 연산) idempotent hoặc deduplication key đủ mạnh.

Độ trễ (latency / 지연 시간) injection cũng cần cẩn thận. Fixed 500 ms cho mọi yêu cầu (request / 요청) tạo tải công việc (workload / 워크로드) khác môi trường vận hành (production / 운영 환경) burst/tail phân phối (distribution / 분포). Delay phân phối (distribution / 분포), packet mất mát (loss / 손실) và partial phụ thuộc (dependency / 의존성) slowdown thường cho bằng chứng (evidence / 증거) thực tế hơn.

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **12. Chaos kỹ thuật (engineering / 엔지니어링) là experiment trên bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **11. mạng (network / 네트워크) fault không chỉ là disconnect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. bảo mật (security / 보안) testing cần kiểm tra authorization quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Chaos kỹ thuật (engineering / 엔지니어링) là experiment trên bất biến (invariant / 불변식)

**Kỹ nghệ hỗn loạn (chaos engineering / 카오스 엔지니어링)** thường bị hiểu thành tắt ngẫu nhiên máy chủ (server / 서버). Cách tiếp cận nghiêm túc hơn là controlled experiment:

```text
steady-state hypothesis
→ bounded fault
→ observe invariant/SLO
→ abort condition
→ recovery verification
```

Blast radius phải phù hợp maturity. Early-stage hệ thống (system / 시스템) nên bắt đầu ở cục bộ (local / 로컬)/staging hoặc môi trường vận hành (production / 운영 환경) cohort nhỏ với guardrails. Không cần gây outage toàn fleet nếu cùng hypothesis có thể kiểm chứng ở phạm vi nhỏ.

Chaos kiểm thử (test / 테스트) có giá trị khi nó tìm giả định (assumption / 가정) ẩn: failover chậm hơn ngân sách thời gian chờ (timeout budget / 타임아웃 예산), thử lại (retry / 재시도) storm, certificate issuer là single điểm (point / 지점) of thất bại (failure / 실패), hoặc autoscaler không kịp phản ứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **13. bảo mật (security / 보안) testing cần kiểm tra authorization quyết định (decision / 결정)** tiếp nhận điểm tựa từ **12. Chaos kỹ thuật (engineering / 엔지니어링) là experiment trên bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Differential testing dùng hiện thực (implementation / 구현) khác làm bằng chứng (evidence / 증거) so sánh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. bảo mật (security / 보안) testing cần kiểm tra authorization quyết định (decision / 결정)

Bảo mật (security / 보안) kiểm thử (test / 테스트) thường dừng ở “login đúng/sai”. Nhưng môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) hay nằm ở object-level authorization, delegation, parser differential và credential vòng đời (lifecycle / 생명주기).

Một bộ kiểm thử (test suite / 테스트 스위트) tốt kiểm tra principal A không đọc tài nguyên (resource / 자원) B, stale/revoked credential bị reject, chính sách (policy / 정책) rollout không mở rộng privilege ngoài ý muốn và malformed yêu cầu (request / 요청) không được proxy/backend diễn giải khác nhau.

Fuzzing parser/giao thức (protocol / 프로토콜) đặc biệt có giá trị với đầu vào (input / 입력) untrusted. Tuy nhiên fuzz “không crash” vẫn chưa đủ nếu parser có thể accept semantically dangerous trạng thái (state / 상태).

Đọc [Security boundaries và attack chains](../../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md).

> **Chuyển mạch:** Trong **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **13. bảo mật (security / 보안) testing cần kiểm tra authorization quyết định (decision / 결정)** đã nêu tiêu chí phân biệt, còn **14. Differential testing dùng hiện thực (implementation / 구현) khác làm bằng chứng (evidence / 증거) so sánh** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. môi trường vận hành (production / 운영 환경) xác minh (verification / 확인) kiểm tra các giả định (assumptions / 가정들) chỉ môi trường vận hành (production / 운영 환경) mới có** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Differential testing dùng hiện thực (implementation / 구현) khác làm bằng chứng (evidence / 증거) so sánh

Nếu có hai independent implementations của cùng spec, cùng đầu vào (input / 입력) có thể được chạy qua cả hai để tìm divergence. trình biên dịch (compiler / 컴파일러), parser, cơ sở dữ liệu (database / 데이터베이스) tính tương thích (compatibility / 호환성) tầng (layer / 계층) và crypto hiện thực (implementation / 구현) thường dùng kiểu lập luận (reasoning / 추론) này.

Divergence không tự chứng minh bên nào sai; specification có thể cho phép nhiều outputs. Nhưng nó tạo counterexample để investigation.

Shadow traffic trong di chuyển (migration / 마이그레이션) là một biến thể môi trường vận hành (production / 운영 환경) của differential testing: old/new đường dẫn (path / 경로) nhận cùng logical yêu cầu (request / 요청) rồi ngữ nghĩa (semantic / 의미적) outputs được so sánh có chọn lọc.

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **14. Differential testing dùng hiện thực (implementation / 구현) khác làm bằng chứng (evidence / 증거) so sánh** đã nêu tiêu chí phân biệt, còn **15. môi trường vận hành (production / 운영 환경) xác minh (verification / 확인) kiểm tra các giả định (assumptions / 가정들) chỉ môi trường vận hành (production / 운영 환경) mới có** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. thời gian chạy (runtime / 런타임) bất biến (invariant / 불변식) biến silent corruption thành observable thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. môi trường vận hành (production / 운영 환경) xác minh (verification / 확인) kiểm tra các giả định (assumptions / 가정들) chỉ môi trường vận hành (production / 운영 환경) mới có

Một số thuộc tính (property / 속성) chỉ quan sát được với real traffic/dữ liệu (data / 데이터) phân phối (distribution / 분포). Canary metrics, synthetic probes, shadow comparison và thời gian chạy (runtime / 런타임) invariants bổ sung pre-production tests.

Testing không kết thúc khi deploy; triển khai (deployment / 배포) là một experiment có guardrails.

Môi trường vận hành (production / 운영 환경) xác minh (verification / 확인) cần phân biệt bản phát hành (release / 릴리스) health, nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성), hiệu năng (performance / 성능) regression, bảo mật (security / 보안) chính sách (policy / 정책) regression và dữ liệu (data / 데이터)/lược đồ (schema / 스키마) divergence. Một canary CPU ổn không chứng minh monetary calculation đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **16. thời gian chạy (runtime / 런타임) bất biến (invariant / 불변식) biến silent corruption thành observable thất bại (failure / 실패)** tiếp nhận điểm tựa từ **15. môi trường vận hành (production / 운영 환경) xác minh (verification / 확인) kiểm tra các giả định (assumptions / 가정들) chỉ môi trường vận hành (production / 운영 환경) mới có** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Flaky tests là độ tin cậy (reliability / 신뢰성) thất bại (failure / 실패) của chính kiểm thử (test / 테스트) hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. thời gian chạy (runtime / 런타임) bất biến (invariant / 불변식) biến silent corruption thành observable thất bại (failure / 실패)

Có bất biến (invariant / 불변식) quá đắt để chứng minh statically nhưng rẻ để kiểm tra thời gian chạy (runtime / 런타임) ở mẫu (sample / 표본) hoặc ranh giới (boundary / 경계) quan trọng: chuỗi (sequence / 시퀀스) number không lùi, account balance nằm trong phạm vi (range / 범위) hợp lệ, replicated trạng thái (state / 상태) băm (hash / 해시) khớp, message phiên bản (version / 버전) được hỗ trợ.

Thời gian chạy (runtime / 런타임) assertion có thể fail-fast trong nội bộ (internal / 내부) hệ thống (system / 시스템) hoặc chỉ emit telemetry tùy blast radius. Cần tránh log sensitive dữ liệu (data / 데이터) và tránh assertion quá nặng trở thành hiệu năng (performance / 성능) sự cố (incident / 인시던트).

Ý tưởng cốt lõi là chuyển “hy vọng giả định (assumption / 가정) đúng” thành observable bằng chứng (evidence / 증거).

> **Chuyển mạch:** Trong **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **17. Flaky tests là độ tin cậy (reliability / 신뢰성) thất bại (failure / 실패) của chính kiểm thử (test / 테스트) hệ thống (system / 시스템)** tiếp nhận điểm tựa từ **16. thời gian chạy (runtime / 런타임) bất biến (invariant / 불변식) biến silent corruption thành observable thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. kiểm thử (test / 테스트) dữ liệu (data / 데이터) phải giữ ngữ nghĩa (semantics / 의미론) mà không tạo privacy debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Flaky tests là độ tin cậy (reliability / 신뢰성) thất bại (failure / 실패) của chính kiểm thử (test / 테스트) hệ thống (system / 시스템)

Flakiness phá trust. thử lại (retry / 재시도) kiểm thử (test / 테스트) vô hạn che race/timing bug. Cần classify nguồn nondeterminism: clock, async wait, trạng thái dùng chung (shared state / 공유 상태), random seed, bên ngoài (external / 외부) phụ thuộc (dependency / 의존성), cổng (port / 포트) collision hoặc tài nguyên (resource / 자원) exhaustion.

Deterministic thời gian (time / 시간)/fake clock và tường minh (explicit / 명시적) synchronization tốt hơn sleep cố định.

Nếu kiểm thử (test / 테스트) randomize đầu vào (input / 입력)/schedule, seed phải được lưu để reproduce. Nếu kiểm thử (test / 테스트) phụ thuộc eventual consistency, poll theo điều kiện (condition / 조건) + deadline thường đúng hơn sleep “đủ lâu”.

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **17. Flaky tests là độ tin cậy (reliability / 신뢰성) thất bại (failure / 실패) của chính kiểm thử (test / 테스트) hệ thống (system / 시스템)** nêu điều cần giải thích; **18. kiểm thử (test / 테스트) dữ liệu (data / 데이터) phải giữ ngữ nghĩa (semantics / 의미론) mà không tạo privacy debt** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. hiệu năng (performance / 성능) kiểm thử (test / 테스트) phải đo saturation và khôi phục (recovery / 복구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. kiểm thử (test / 테스트) dữ liệu (data / 데이터) phải giữ ngữ nghĩa (semantics / 의미론) mà không tạo privacy debt

Môi trường vận hành (production / 운영 환경) snapshot có phân phối (distribution / 분포) thực nhưng có thể chứa personal dữ liệu (data / 데이터), secret hoặc identifiers. bản sao (copy / 복사) thẳng môi trường vận hành (production / 운영 환경) DB vào kiểm thử (test / 테스트) làm tăng breach surface và retention độ phức tạp (complexity / 복잡도).

Synthetic/anonymized dữ liệu (data / 데이터) hữu ích nhưng có thể mất skew/rare edge cases. Test-data chiến lược (strategy / 전략) cần cân privacy với representativeness và ghi rõ phân phối (distribution / 분포) nào đã bị mất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **18. kiểm thử (test / 테스트) dữ liệu (data / 데이터) phải giữ ngữ nghĩa (semantics / 의미론) mà không tạo privacy debt** nêu điều cần giải thích; **19. hiệu năng (performance / 성능) kiểm thử (test / 테스트) phải đo saturation và khôi phục (recovery / 복구)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. kiểm thử (test / 테스트) môi trường (environment / 환경) có thể pass vì miền lỗi (failure domain / 장애 도메인) khác môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. hiệu năng (performance / 성능) kiểm thử (test / 테스트) phải đo saturation và khôi phục (recovery / 복구)

Kiểm thử tải (load test / 부하 테스트) tốt tăng tải (load / 로드) qua utilization knee, đo hàng đợi (queue / 큐) wait/dịch vụ (service / 서비스) thời gian (time / 시간) và xem hệ thống (system / 시스템) phục hồi thế nào sau burst. Nếu chỉ báo “max 20k RPS”, ta chưa biết p99 SLO, thử lại (retry / 재시도) amplification hay backlog drain thời gian (time / 시간).

Tải công việc (workload / 워크로드) mix, payload sizes, bộ nhớ đệm (cache / 캐시) warm/cold, downstream điều kiện (condition / 조건) và background tasks phải gần enough môi trường vận hành (production / 운영 환경) để kết quả (result / 결과) có ý nghĩa.

Sức chứa (capacity / 용량) chapter đi sâu hơn tại [Capacity planning và whole-system profiling](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

> **Chuyển mạch:** Trong **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **20. kiểm thử (test / 테스트) môi trường (environment / 환경) có thể pass vì miền lỗi (failure domain / 장애 도메인) khác môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **19. hiệu năng (performance / 성능) kiểm thử (test / 테스트) phải đo saturation và khôi phục (recovery / 복구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. sự cố (incident / 인시던트) phải quay lại kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) dưới dạng bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. kiểm thử (test / 테스트) môi trường (environment / 환경) có thể pass vì miền lỗi (failure domain / 장애 도메인) khác môi trường vận hành (production / 운영 환경)

Staging một nút (node / 노드) không tái hiện multi-zone failover. cục bộ (local / 로컬) filesystem không đại diện remote managed lưu trữ (storage / 저장소). In-memory hàng đợi (queue / 큐) không đại diện broker delivery ngữ nghĩa (semantics / 의미론). Fake clock không tái hiện cross-host clock skew.

Điều này không làm lower-level kiểm thử (test / 테스트) vô dụng. Nó chỉ yêu cầu kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) ghi rõ **giả định (assumption / 가정) nào mỗi môi trường (environment / 환경) cover và không cover**.

Một useful ma trận (matrix / 행렬) là:

```text
invariant
→ failure model
→ test level/environment
→ oracle/evidence
```

Nhờ vậy nhóm (team / 팀) biết gap nào cần môi trường vận hành (production / 운영 환경) canary hoặc fault-injection môi trường (environment / 환경) thay vì vô thức tin một green CI suite.

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **21. sự cố (incident / 인시던트) phải quay lại kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) dưới dạng bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **20. kiểm thử (test / 테스트) môi trường (environment / 환경) có thể pass vì miền lỗi (failure domain / 장애 도메인) khác môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. kiểm thử (test / 테스트) metrics cũng chịu Goodhart's Law** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. sự cố (incident / 인시던트) phải quay lại kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) dưới dạng bất biến (invariant / 불변식)

Sau sự cố (incident / 인시던트), cách đơn giản là thêm kiểm thử (test / 테스트) cho chính xác (exact / 정확한) đầu vào (input / 입력) gây lỗi. Cách tốt hơn là hỏi bug reveal bất biến (invariant / 불변식) nào chưa được encode.

Outage do thử lại (retry / 재시도) storm không chỉ cần kiểm thử (test / 테스트) “endpoint X hết thời gian chờ (timeout / 타임아웃)”. Cần kiểm thử (test / 테스트) thử lại (retry / 재시도) ngân sách (budget / 예산)/backoff/admission hành vi (behavior / 동작) khi phụ thuộc (dependency / 의존성) dịch vụ (service / 서비스) tỷ lệ (rate / 비율) giảm. dữ liệu (data / 데이터) mất mát (loss / 손실) do crash không chỉ cần replay chính xác (exact / 정확한) chuỗi (sequence / 시퀀스); cần crash-point tests quanh durability giao thức (protocol / 프로토콜).

Sự cố (incident / 인시던트) học tập (learning / 학습) hiệu quả biến một môi trường vận hành (production / 운영 환경) surprise thành **family of properties/thất bại (failure / 실패) tests**, giảm xác suất cùng cơ chế (mechanism / 메커니즘) xuất hiện ở hình thức khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **22. kiểm thử (test / 테스트) metrics cũng chịu Goodhart's Law** tiếp nhận điểm tựa từ **21. sự cố (incident / 인시던트) phải quay lại kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) dưới dạng bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Worked example: payment hết thời gian chờ (timeout / 타임아웃) với ambiguous kết quả (outcome / 결과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. kiểm thử (test / 테스트) metrics cũng chịu Goodhart's Law

Coverage %, kiểm thử (test / 테스트) count, pass tỷ lệ (rate / 비율), mutation score và mean CI duration đều hữu ích nhưng trở nên nguy hiểm khi biến thành mục tiêu (target / 대상) độc lập.

100% coverage có thể đạt bằng assertions yếu. Zero flaky tests có thể đạt bằng xóa kiểm thử (test / 테스트) khó. CI rất nhanh có thể vì bỏ tích hợp (integration / 통합) checks quan trọng.

Chỉ số (metric / 지표) nên là bằng chứng (evidence / 증거) hỗ trợ câu hỏi “rủi ro (risk / 위험) nào đang được kiểm soát?”, không phải proxy thay tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Trong **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **22. kiểm thử (test / 테스트) metrics cũng chịu Goodhart's Law** cho ta quy tắc; **23. Worked example: payment hết thời gian chờ (timeout / 타임아웃) với ambiguous kết quả (outcome / 결과)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **24. Worked example: lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) old/new coexist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Worked example: payment hết thời gian chờ (timeout / 타임아웃) với ambiguous kết quả (outcome / 결과)

Giả sử máy khách (client / 클라이언트) gửi payment yêu cầu (request / 요청), máy chủ (server / 서버) lần ghi nhận (commit / 커밋) giao dịch (transaction / 트랜잭션) nhưng phản hồi (response / 응답) bị mất. máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) rồi thử lại (retry / 재시도).

Một happy-path E2E kiểm thử (test / 테스트) không cover tình huống này. kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) cần inject thất bại (failure / 실패) sau lần ghi nhận (commit / 커밋) trước phản hồi (response / 응답), rồi kiểm tra:

```text
retry cùng idempotency key
→ không tạo charge thứ hai
→ client nhận outcome consistent
→ audit trail reconstruct được attempts
```

Oracle không phải “HTTP 200”. Oracle là **một logical payment tạo tối đa một irreversible charge theo đặc tả hợp đồng (contract / 계약)**.

Ví dụ này nối fault injection, idempotency, giao dịch (transaction / 트랜잭션) durability và môi trường vận hành (production / 운영 환경) tracing trong một bất biến (invariant / 불변식) duy nhất.

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **23. Worked example: payment hết thời gian chờ (timeout / 타임아웃) với ambiguous kết quả (outcome / 결과)** cho ta quy tắc; **24. Worked example: lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) old/new coexist** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **25. bằng chứng vận hành (production evidence / 운영 증거) và forensic usefulness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Worked example: lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) old/new coexist

Trong rolling deploy, old producer và new bên tiêu thụ (consumer / 소비자) có thể coexist. kiểm thử (test / 테스트) chỉ chạy new→new bỏ sót tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우).

Đặc tả hợp đồng (contract / 계약) ma trận (matrix / 행렬) nên cover supported pairs:

```text
old producer → old consumer
old producer → new consumer
new producer → old consumer   nếu rollout contract yêu cầu
new producer → new consumer
```

Sau khi old phiên bản (version / 버전) retire, đặc tả hợp đồng (contract / 계약) ma trận (matrix / 행렬) có thể thu hẹp. Testing phải phản ánh triển khai (deployment / 배포) máy trạng thái (state machine / 상태 머신), không giả định fleet upgrade atomically.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **24. Worked example: lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) old/new coexist** cho ta quy tắc; **25. bằng chứng vận hành (production evidence / 운영 증거) và forensic usefulness** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. bằng chứng vận hành (production evidence / 운영 증거) và forensic usefulness

Khi kiểm thử (test / 테스트) thất bại (fail / 실패) hoặc sự cố (incident / 인시던트) xảy ra, bằng chứng (evidence / 증거) nên đủ để reconstruct ranh giới (boundary / 경계) trạng thái (state / 상태): yêu cầu (request / 요청)/dấu vết (trace / 추적) ID, phiên bản (version / 버전)/bản dựng (build / 빌드), đầu vào (input / 입력) lớp (class / 클래스), principal/chính sách (policy / 정책) phiên bản (version / 버전), phụ thuộc (dependency / 의존성) kết quả (outcome / 결과), thử lại (retry / 재시도) attempt, giao dịch (transaction / 트랜잭션)/sự kiện (event / 이벤트) ID và relevant timing.

Không cần log toàn payload hoặc secret. **Khả năng điều tra (forensic usefulness / 포렌식 유용성)** đến từ nhân quả (causal / 인과적) định danh (identity / 식별자) và quyết định (decision / 결정) siêu dữ liệu (metadata / 메타데이터), không phải lưu mọi byte.

Kiểm thử (test / 테스트) harness cũng nên export artifacts hữu ích: minimized thuộc tính (property / 속성) counterexample, random seed, fault timeline, nút (node / 노드)/replica trạng thái (state / 상태) và relevant logs/metrics. Một flaky CI thất bại (failure / 실패) không reproduce được là bằng chứng (evidence / 증거) rất yếu.

> **Chuyển mạch:** Trong **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **25. bằng chứng vận hành (production evidence / 운영 증거) và forensic usefulness** nêu điều cần giải thích; **Dùng chung (common / 공통) Misconceptions** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Nhiều kiểm thử (test / 테스트) hơn nghĩa confidence cao hơn.”** kiểm thử (test / 테스트) trùng nhau với oracle yếu có thể tăng maintenance mà không tăng bằng chứng (evidence / 증거) đáng kể.

**“100% coverage nghĩa mã (code / 코드) đúng.”** Coverage chỉ nói mã (code / 코드) đã chạy dưới kiểm thử (test / 테스트), không chứng minh assertions đủ mạnh hay thất bại (failure / 실패) không gian (space / 공간) đã được cover.

**“Chaos kỹ thuật (engineering / 엔지니어링) là tắt máy chủ (server / 서버) ngẫu nhiên.”** Nó phải là controlled experiment gắn với steady-state hypothesis, bounded blast radius và khôi phục (recovery / 복구) oracle.

**“Mock càng nhiều thì đơn vị (unit / 단위) kiểm thử (test / 테스트) càng tốt.”** Mocking giao thức (protocol / 프로토콜) ngữ nghĩa (semantics / 의미론) có thể tạo fake world khác môi trường vận hành (production / 운영 환경).

**“thử lại (retry / 재시도) flaky kiểm thử (test / 테스트) là fix.”** thử lại (retry / 재시도) có thể che race, clock hoặc tài nguyên (resource / 자원) bug và làm kiểm thử (test / 테스트) hệ thống (system / 시스템) mất trust.

> **Chuyển mạch:** Ở chặng này của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) là **portfolio bằng chứng về bất biến (invariant / 불변식) dưới nhiều thực thi (execution / 실행) và thất bại (failure / 실패) các mô hình (models / 모델들)**. đơn vị (unit / 단위) tests kiểm tra cục bộ (local / 로컬) lô-gic (logic / 논리); contracts kiểm tra ranh giới (boundary / 경계) agreement; properties/mutation kiểm tra độ rộng và sức mạnh oracle; tích hợp (integration / 통합)/fault injection kiểm tra ngữ nghĩa (semantics / 의미론) của phụ thuộc (dependency / 의존성) thật; môi trường vận hành (production / 운영 환경) xác minh (verification / 확인) kiểm tra các giả định (assumptions / 가정들) chỉ tải công việc (workload / 워크로드) thật mới làm lộ. Một bộ kiểm thử (test suite / 테스트 스위트) mạnh biết rủi ro (risk / 위험) nào được chứng minh ở đâu và gap nào vẫn còn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처): đặc tả hợp đồng (contract / 계약), mutation, property-based và môi trường vận hành (production / 운영 환경) xác minh (verification / 확인)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [Deployment safety](./05_deployment_safety_canary_blue_green_flags_and_rollback.md), [Large-scale migration](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md), [Security boundaries](../../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md), [Capacity/whole-system profiling](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [Correctness path](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md), [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md) và [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
