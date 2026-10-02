# Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Ownership, borrowing, linear/affine types và memory safety**. Route đi từ resource/lifetime → unique ownership → borrowing và aliasing → compile-time proof, để quyền sở hữu được nối với use-after-free, double-free và data-race freedom.

Bộ nhớ (memory / 메모리) an toàn (safety / 안전) traditionally được bảo vệ theo nhiều hướng. Garbage-collected languages giữ đối tượng (object / 객체) sống khi còn reachable và thu hồi tự động. các hệ thống (systems / 시스템들) languages như C trao quyền allocation/free trực tiếp cho programmer nhưng dễ tạo use-after-free, double-free hoặc dangling pointer. quyền sở hữu (ownership / 소유권) mở ra một hướng khác: đưa **tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명), aliasing và quyền sử dụng** vào ngữ nghĩa (semantics / 의미론)/hệ kiểu (type system / 타입 시스템) để trình biên dịch (compiler / 컴파일러) loại bỏ một lớp trạng thái nguy hiểm trước thời gian chạy (runtime / 런타임).

Điểm advanced không phải học Rust cú pháp (syntax / 문법). Cần hiểu bất biến (invariant / 불변식): **ai sở hữu tài nguyên (resource / 자원), ai được phép dùng hoặc mutate nó, quyền đó chuyển giao lúc nào, và ranh giới (boundary / 경계) nào làm trình biên dịch (compiler / 컴파일러) không còn tự chứng minh được bất biến (invariant / 불변식).**

## 1. tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) là vấn đề ngữ nghĩa (semantic / 의미적)

Use-after-free xảy ra khi tham chiếu (reference / 참조) còn được dùng sau khi tài nguyên (resource / 자원) đã hết thời gian tồn tại (lifetime / 수명). Double-free xảy ra khi nhiều điều khiển (control / 제어) paths cùng tin rằng chúng chịu trách nhiệm cleanup. Leak xảy ra khi không còn đường dẫn (path / 경로) nào thực hiện responsibility đó.

Nếu quyền sở hữu (ownership / 소유권) chỉ tồn tại trong comment hoặc convention, trình biên dịch (compiler / 컴파일러) không thể bảo đảm bất biến (invariant / 불변식). Ownership-aware ngữ nghĩa (semantics / 의미론) biến responsibility thành thứ có thể được kiểm tra bằng data-flow/kiểu (type / 타입) rules.

Tài nguyên (resource / 자원) không chỉ là bộ nhớ vùng động (heap memory / 힙 메모리). tệp (file / 파일) descriptor, socket, mutex guard, giao dịch (transaction / 트랜잭션) handle, GPU buffer hay cryptographic năng lực (capability / 역량) đều có vòng đời (lifecycle / 생명주기).

> **Chuyển mạch:** Trong **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **1. tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) là vấn đề ngữ nghĩa (semantic / 의미적)** nêu điều cần giải thích; **2. Unique quyền sở hữu (ownership / 소유권) làm responsibility rõ ràng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Borrowing tách quyền sử dụng khỏi quyền sở hữu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Unique quyền sở hữu (ownership / 소유권) làm responsibility rõ ràng

Mô hình tư duy (mental model / 사고 모델) đơn giản là mỗi tài nguyên (resource / 자원) có một đơn vị sở hữu (owner / 오너) chịu trách nhiệm thời gian tồn tại (lifetime / 수명). Khi quyền sở hữu (ownership / 소유권) được **move**, nguồn (source / 소스) cũ không còn quyền sử dụng tài nguyên (resource / 자원) như trước.

```text
owner A --move--> owner B
A mất quyền         B chịu trách nhiệm
```

Move ngữ nghĩa (semantics / 의미론) tránh implicit duplication của resource-sensitive values và giúp cleanup đường dẫn (path / 경로) rõ hơn.

Bất biến (invariant / 불변식) cốt lõi là: **không tồn tại hai đơn vị sở hữu (owner / 오너) độc lập cùng tin rằng mình có quyền hủy cùng một unique tài nguyên (resource / 자원).**

> **Chuyển mạch:** Ở chặng này của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **3. Borrowing tách quyền sử dụng khỏi quyền sở hữu** tiếp nhận điểm tựa từ **2. Unique quyền sở hữu (ownership / 소유권) làm responsibility rõ ràng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. thời gian tồn tại (lifetime / 수명) là quan hệ chứ không phải đồng hồ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Borrowing tách quyền sử dụng khỏi quyền sở hữu

Hàm (function / 함수) thường chỉ cần dùng tài nguyên (resource / 자원) tạm thời, không cần trở thành đơn vị sở hữu (owner / 오너). **Borrowing (대여/차용)** cho phép mã (code / 코드) giữ tham chiếu (reference / 참조) trong một thời gian tồn tại (lifetime / 수명) có kiểm soát mà không nhận trách nhiệm destroy tài nguyên (resource / 자원).

Một discipline điển hình là:

```text
nhiều shared/immutable borrows
        hoặc
một mutable borrow độc quyền
```

Mục tiêu là ngăn unrestricted mutable aliasing — nguồn gốc của nhiều dữ liệu (data / 데이터) race, iterator vô hiệu hóa (invalidation / 무효화) và temporal bugs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **4. thời gian tồn tại (lifetime / 수명) là quan hệ chứ không phải đồng hồ** tiếp nhận điểm tựa từ **3. Borrowing tách quyền sử dụng khỏi quyền sở hữu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. tuyến tính (linear / 선형) và affine types theo dõi quyền sử dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. thời gian tồn tại (lifetime / 수명) là quan hệ chứ không phải đồng hồ

Trình biên dịch (compiler / 컴파일러) không cần biết tham chiếu (reference / 참조) tồn tại “3 ms”. Nó cần chứng minh tham chiếu (reference / 참조) không sống lâu hơn referent.

Nếu hàm (function / 함수) trả tham chiếu (reference / 참조) tới cục bộ (local / 로컬) ngăn xếp (stack / 스택) giá trị (value / 값) đã bị destroy, quan hệ (relation / 관계) không thể thỏa. Nếu đầu ra (output / 출력) tham chiếu (reference / 참조) được lấy từ đầu vào (input / 입력), trình biên dịch (compiler / 컴파일러) cần biết đầu ra (output / 출력) thời gian tồn tại (lifetime / 수명) bị ràng buộc bởi đầu vào (input / 입력) nào.

Thời gian tồn tại (lifetime / 수명) vì thế là thuộc tính (property / 속성) của phạm vi (scope / 범위)/data-flow/quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프), không phải timestamp thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Trong **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **5. tuyến tính (linear / 선형) và affine types theo dõi quyền sử dụng** tiếp nhận điểm tựa từ **4. thời gian tồn tại (lifetime / 수명) là quan hệ chứ không phải đồng hồ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Typestate: kiểu (type / 타입) có thể biểu diễn giao thức (protocol / 프로토콜) quyền sở hữu trạng thái (state ownership / 상태 소유권) thinking mở rộng tự nhiên sang typestate. Một giao dịch (transaction / 트랜잭션) đối tượng (object / 객체) có thể chuyển trạng thái:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. tuyến tính (linear / 선형) và affine types theo dõi quyền sử dụng

**tuyến tính (linear / 선형) kiểu (type / 타입)** yêu cầu một tài nguyên (resource / 자원) được sử dụng đúng một lần theo discipline lý thuyết. **Affine kiểu (type / 타입)** thường cho phép sử dụng tối đa một lần: có thể bỏ nhưng không arbitrary duplicate.

Hệ thống thực tế có thể không tuân một calculus thuần túy, nhưng mô hình tư duy (mental model / 사고 모델) quan trọng là hệ kiểu (type system / 타입 시스템) theo dõi **usage/năng lực (capability / 역량)**, không chỉ shape của dữ liệu (data / 데이터).

Một integer có thể bản sao (copy / 복사) tự do; một unique tệp (file / 파일) handle, khóa (lock / 잠금) guard hay signing năng lực (capability / 역량) có thể cần ngữ nghĩa (semantics / 의미론) khác.

> **Chuyển mạch:** Ở chặng này của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, sau nội dung của **5. tuyến tính (linear / 선형) và affine types theo dõi quyền sử dụng**, **6. Typestate: kiểu (type / 타입) có thể biểu diễn giao thức (protocol / 프로토콜) quyền sở hữu trạng thái (state ownership / 상태 소유권) thinking mở rộng tự nhiên sang typestate. Một giao dịch (transaction / 트랜잭션) đối tượng (object / 객체) có thể chuyển trạng thái:** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **7. RAII và deterministic cleanup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Typestate: kiểu (type / 타입) có thể biểu diễn giao thức (protocol / 프로토콜) quyền sở hữu trạng thái (state ownership / 상태 소유권) thinking mở rộng tự nhiên sang **typestate**. Một giao dịch (transaction / 트랜잭션) đối tượng (object / 객체) có thể chuyển trạng thái:

```text
OpenTransaction
   ├─ commit()   → Committed
   └─ rollback() → RolledBack
```

Nếu API encode chuyển tiếp trạng thái (state transition / 상태 전이) vào kiểu (type / 타입), thao tác (operation / 연산) như “lần ghi nhận (commit / 커밋) lần hai” có thể trở thành trạng thái không biểu diễn được hoặc khó biểu diễn hơn.

Đây là cách hệ kiểu (type system / 타입 시스템) giữ bất biến (invariant / 불변식) của một giao thức (protocol / 프로토콜), không chỉ thời gian tồn tại (lifetime / 수명) bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **7. RAII và deterministic cleanup** tiếp nhận điểm tựa từ **6. Typestate: kiểu (type / 타입) có thể biểu diễn giao thức (protocol / 프로토콜) quyền sở hữu trạng thái (state ownership / 상태 소유권) thinking mở rộng tự nhiên sang typestate. Một giao dịch (transaction / 트랜잭션) đối tượng (object / 객체) có thể chuyển trạng thái:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. dùng chung (shared / 공유) quyền sở hữu (ownership / 소유권) có chi phí (cost / 비용) mô hình (model / 모델) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. RAII và deterministic cleanup

C++ và Rust dùng mẫu (pattern / 패턴) **RAII — tài nguyên (resource / 자원) Acquisition Is Initialization**: thời gian tồn tại (lifetime / 수명) của tài nguyên (resource / 자원) gắn với thời gian tồn tại (lifetime / 수명) đơn vị sở hữu (owner / 오너) đối tượng (object / 객체). Khi đơn vị sở hữu (owner / 오너) rời phạm vi (scope / 범위), destructor/drop chạy deterministic.

Khóa (lock / 잠금) guard là ví dụ rõ: acquire khóa (lock / 잠금) tạo guard; phạm vi (scope / 범위) kết thúc thì guard bản phát hành (release / 릴리스) khóa (lock / 잠금) ngay cả khi return sớm hoặc exception/unwind xảy ra theo ngữ nghĩa (semantics / 의미론) tương ứng.

Java dùng GC cho bộ nhớ (memory / 메모리) nhưng vẫn cần `try-with-resources` cho tệp (file / 파일)/socket vì reachability thời gian tồn tại (lifetime / 수명) không đồng nghĩa external-resource thời gian tồn tại (lifetime / 수명).

> **Chuyển mạch:** Trong **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, sau nội dung của **7. RAII và deterministic cleanup**, **8. dùng chung (shared / 공유) quyền sở hữu (ownership / 소유권) có chi phí (cost / 비용) mô hình (model / 모델) riêng** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **9. Interior mutability: dùng chung (shared / 공유) tham chiếu (reference / 참조) không đồng nghĩa bits bất biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. dùng chung (shared / 공유) quyền sở hữu (ownership / 소유권) có chi phí (cost / 비용) mô hình (model / 모델) riêng

Khi nhiều owners thực sự cần share thời gian tồn tại (lifetime / 수명), tham chiếu (reference / 참조) counting là một chiến lược (strategy / 전략): clone handle tăng count, bản phát hành (release / 릴리스) giảm count, count về zero thì cleanup.

Nhưng chi phí (cost / 비용) không miễn phí. Atomic tham chiếu (reference / 참조) counting trong multi-threaded ngữ cảnh (context / 맥락) tạo synchronization traffic. Cycle `A → B → A` có thể giữ count > 0 mãi nếu không có weak tham chiếu (reference / 참조) hoặc tracing cơ chế (mechanism / 메커니즘).

“Không dùng GC” không có nghĩa bộ nhớ (memory / 메모리) management không có thời gian chạy (runtime / 런타임) chi phí (cost / 비용); chi phí (cost / 비용) được chuyển sang refcount, allocator, static các ràng buộc (constraints / 제약조건들) hoặc tường minh (explicit / 명시적) kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Ở chặng này của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **9. Interior mutability: dùng chung (shared / 공유) tham chiếu (reference / 참조) không đồng nghĩa bits bất biến** tiếp nhận điểm tựa từ **8. dùng chung (shared / 공유) quyền sở hữu (ownership / 소유권) có chi phí (cost / 비용) mô hình (model / 모델) riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. quyền sở hữu (ownership / 소유권) và tính đồng thời (concurrency / 동시성) an toàn (safety / 안전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Interior mutability: dùng chung (shared / 공유) tham chiếu (reference / 참조) không đồng nghĩa bits bất biến

Đôi khi outer API muốn dùng chung (shared / 공유) tham chiếu (reference / 참조) nhưng trạng thái (state / 상태) bên trong vẫn thay đổi qua thành phần nguyên thủy (primitive / 기본 요소) có kiểm soát như mutex, atomic cell hoặc thời gian chạy (runtime / 런타임) borrow check.

Mô hình tư duy (mental model / 사고 모델) đúng là: dùng chung (shared / 공유)/immutable tham chiếu (reference / 참조) không cho phép **unrestricted mutation qua tham chiếu (reference / 참조) đó**. Mutation vẫn có thể xảy ra nếu lớp trừu tượng (abstraction / 추상화) bên trong giữ bất biến (invariant / 불변식) bằng synchronization/thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증).

Điều này rất quan trọng khi lập luận (reasoning / 추론) tính đồng thời (concurrency / 동시성): “API nhìn immutable” không có nghĩa đối tượng (object / 객체) physically không đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **10. quyền sở hữu (ownership / 소유권) và tính đồng thời (concurrency / 동시성) an toàn (safety / 안전)** tiếp nhận điểm tựa từ **9. Interior mutability: dùng chung (shared / 공유) tham chiếu (reference / 참조) không đồng nghĩa bits bất biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. hiệu năng (performance / 성능) pressure thay đổi sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. quyền sở hữu (ownership / 소유권) và tính đồng thời (concurrency / 동시성) an toàn (safety / 안전)

Nếu hệ kiểu (type system / 타입 시스템) chứng minh mutable truy cập (access / 접근) không bị alias đồng thời giữa threads trừ qua synchronization-safe lớp trừu tượng (abstraction / 추상화), một lớp dữ liệu (data / 데이터) race bị loại structurally.

Tuy nhiên quyền sở hữu (ownership / 소유권) không chứng minh toàn bộ concurrent program đúng. Deadlock, starvation, logical race, thứ tự (ordering / 순서) giữa phân tán (distributed / 분산) messages và state-machine bug vẫn tồn tại.

Static quyền sở hữu (ownership / 소유권) chỉ sở hữu một số bất biến (invariant / 불변식): thời gian tồn tại (lifetime / 수명), aliasing và transfer discipline. Đừng mở rộng guarantee vượt quá ranh giới (boundary / 경계) đó.

> **Chuyển mạch:** Trong **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **11. hiệu năng (performance / 성능) pressure thay đổi sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **10. quyền sở hữu (ownership / 소유권) và tính đồng thời (concurrency / 동시성) an toàn (safety / 안전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. FFI là nơi static proof dừng lại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. hiệu năng (performance / 성능) pressure thay đổi sự đánh đổi (trade-off / 트레이드오프)

Static quyền sở hữu (ownership / 소유권) có thể loại thời gian chạy (runtime / 런타임) checks và giúp trình biên dịch (compiler / 컴파일러) lập luận (reasoning / 추론) aliasing tốt hơn, nhưng program cấu trúc (structure / 구조) đôi khi phải dùng arena, indirection, copying hoặc tham chiếu (reference / 참조) counting để biểu diễn đồ thị (graph / 그래프) phức tạp.

Dùng chung (shared / 공유) atomic refcount có thể tạo cache-line contention. Deterministic destruction có thể đẩy cleanup chi phí (cost / 비용) vào latency-sensitive đường dẫn (path / 경로). Arena giảm per-object allocation nhưng đổi thời gian tồn tại (lifetime / 수명) granularity.

Vì vậy “quyền sở hữu (ownership / 소유권) = nhanh” không phải bất biến (invariant / 불변식). hiệu năng (performance / 성능) phụ thuộc bố cục (layout / 레이아웃), allocation chiến lược (strategy / 전략), sharing mẫu (pattern / 패턴) và thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계).

> **Chuyển mạch:** Ở chặng này của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **12. FFI là nơi static proof dừng lại** tiếp nhận điểm tựa từ **11. hiệu năng (performance / 성능) pressure thay đổi sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. thất bại (failure / 실패) modes cần phân biệt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. FFI là nơi static proof dừng lại

Khi mã (code / 코드) ownership-safe gọi C API bằng raw pointer, trình biên dịch (compiler / 컴파일러) không tự biết:

```text
ai allocate?
ai free?
pointer valid tới khi nào?
callee giữ pointer sau return không?
callback chạy thread nào?
resource có được share/mutate đồng thời không?
```

`unsafe`/FFI ranh giới (boundary / 경계) nghĩa programmer phải chứng minh bất biến (invariant / 불변식) mà trình biên dịch (compiler / 컴파일러) không thể kiểm tra trực tiếp. Safe wrapper chỉ mạnh bằng đặc tả hợp đồng (contract / 계약) của ranh giới (boundary / 경계) không-safe phía dưới.

Đây là leaky lớp trừu tượng (abstraction / 추상화) điển hình giữa ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và ABI/bản địa (native / 네이티브) thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **13. thất bại (failure / 실패) modes cần phân biệt** tiếp nhận điểm tựa từ **12. FFI là nơi static proof dừng lại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. bằng chứng vận hành (production evidence / 운영 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. thất bại (failure / 실패) modes cần phân biệt

Quyền sở hữu (ownership / 소유권) discipline nhắm vào một số lớp (class / 클래스) thất bại (failure / 실패):

```text
use-after-free
dangling reference
double free
uncontrolled mutable aliasing
resource leak do ownership không rõ
```

Nhưng vẫn có thể có:

```text
logical race
deadlock
starvation
protocol misuse qua unsafe/FFI
OOM
resource exhaustion
```

Một type-safe program không đồng nghĩa system-level correct.

> **Chuyển mạch:** Trong **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **13. thất bại (failure / 실패) modes cần phân biệt** nêu điều cần giải thích; **14. bằng chứng vận hành (production evidence / 운영 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. bằng chứng vận hành (production evidence / 운영 증거)

Static checker/trình biên dịch (compiler / 컴파일러) diagnostic là bằng chứng (evidence / 증거) chính cho proof ở compile thời gian (time / 시간). thời gian chạy (runtime / 런타임) sanitizer, vùng nhớ động (heap / 힙) profiler, leak detector, crash dump và FFI ranh giới (boundary / 경계) tests giúp tìm violation ở vùng unsafe/bản địa (native / 네이티브) mã (code / 코드).

Với tham chiếu (reference / 참조) counting, contention/profile có thể chỉ ra atomic refcount đường xử lý nóng (hot path / 핫 패스). Với deterministic cleanup, tracing/profiling có thể cho thấy destructor/drop đang nằm trên đường găng (critical path / 임계 경로).

Bằng chứng (evidence / 증거) nên gắn đúng hypothesis: thời gian tồn tại (lifetime / 수명) bug, leak, allocator pressure hay contention không phải cùng một vấn đề.

> **Chuyển mạch:** Ở chặng này của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, các dấu vết trong **14. bằng chứng vận hành (production evidence / 운영 증거)** được đọc cùng nhau ở **15. Mô hình tư duy** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Mô hình tư duy

> quyền sở hữu (ownership / 소유권) biến câu hỏi “ai chịu trách nhiệm thời gian tồn tại (lifetime / 수명) và ai được phép mutate/use?” thành một phần của program ngữ nghĩa (semantics / 의미론). **Move chuyển responsibility; borrow cấp quyền tạm thời; thời gian tồn tại (lifetime / 수명) chứng minh tham chiếu (reference / 참조) không vượt tài nguyên (resource / 자원); tuyến tính (linear / 선형)/affine discipline giới hạn duplication; typestate có thể encode tài nguyên (resource / 자원) giao thức (protocol / 프로토콜).** Static proof kết thúc ở ranh giới (boundary / 경계) như FFI/unsafe, nơi programmer phải tái lập bất biến (invariant / 불변식) bằng đặc tả hợp đồng (contract / 계약) rõ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quyền sở hữu (ownership / 소유권), borrowing, tuyến tính (linear / 선형)/affine types và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **Kết nối** gom các mảnh từ **15. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc tiếp [Effect systems và capabilities](./03_effect_systems_capabilities_and_controlled_side_effects.md), [Coroutine/structured concurrency](./07_coroutines_continuations_async_runtimes_and_structured_concurrency.md), [OS resources/handles](../../03_operating_systems/advanced/00_kernel_execution_contexts_and_syscall_path.md) và [Security boundaries](../../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
