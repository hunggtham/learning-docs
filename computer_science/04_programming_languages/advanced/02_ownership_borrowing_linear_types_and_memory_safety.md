# Ownership, borrowing, linear/affine types và memory safety

Memory safety traditionally được bảo vệ theo hai hướng lớn. Garbage-collected languages giữ object sống khi còn reachable và thu hồi tự động. Systems languages kiểu C trao quyền allocation/free trực tiếp cho programmer nhưng dễ tạo use-after-free, double-free hoặc dangling pointer. **Ownership** mở ra hướng thứ ba: đưa lifetime và quyền truy cập vào static rules để compiler loại bỏ nhiều lỗi trước runtime mà không cần tracing GC cho mọi object.

## Ownership là câu hỏi “ai chịu trách nhiệm cho resource?”

Resource không chỉ là heap memory. File descriptor, socket, mutex guard, transaction handle hay GPU buffer đều có lifecycle. Nếu nhiều nơi cùng tin rằng mình phải cleanup, double-close có thể xảy ra; nếu không nơi nào chịu trách nhiệm, leak xuất hiện.

Ownership model gán responsibility rõ ràng cho value. Khi ownership được **move**, source cũ không còn quyền sử dụng resource theo cùng cách. Compiler biến một convention thường được ghi trong documentation thành rule có thể kiểm tra.

## Borrowing tách quyền dùng khỏi quyền sở hữu

Không phải function nào nhận object cũng cần trở thành owner. **Borrowing (대여/차용)** cho phép code tạm thời tham chiếu resource mà không nhận trách nhiệm destroy nó.

Một immutable/shared borrow có thể tồn tại đồng thời nếu không ai mutate state theo cách gây race. Mutable borrow thường yêu cầu exclusivity trong khoảng lifetime của borrow. Rule “nhiều reader hoặc một writer” liên hệ trực tiếp với synchronization invariant.

## Lifetime là quan hệ, không chỉ thời lượng

Compiler không nhất thiết cần biết một reference sống “3 ms”. Nó cần chứng minh reference không sống lâu hơn referent. **Lifetime** mô tả quan hệ scope/data-flow đó.

Nếu function trả reference tới local stack variable đã bị destroy, relation không thể thỏa. Nếu reference được trả từ input, compiler cần biết output lifetime bị ràng buộc bởi input nào.

## Linear và affine type

**Linear type** yêu cầu resource được dùng chính xác một lần theo nghĩa type-theoretic; **affine type** thường cho phép dùng tối đa một lần. Ownership systems thực tế có thể kết hợp move semantics, destructor và borrowing thay vì tuân một calculus thuần túy.

Ý tưởng chung là không cho phép arbitrary duplication của value mang resource-sensitive semantics. Một integer có thể copy tự do; một unique file handle hoặc capability có thể cần quy tắc khác.

## RAII và deterministic cleanup

C++ và Rust dùng pattern **RAII — Resource Acquisition Is Initialization**: lifetime của resource gắn với lifetime của owner object. Khi owner rời scope, destructor/drop chạy deterministic.

Điều này đặc biệt hữu ích cho lock guard: acquire lock tạo guard; scope kết thúc thì guard release lock kể cả khi control flow return sớm. Resource protocol được gắn vào language lifetime thay vì dựa vào programmer nhớ gọi cleanup ở mọi branch.

## GC và ownership không phải hai phe đối lập

Garbage collection rất mạnh khi object graph phức tạp, ownership chia sẻ tự nhiên và pause/throughput trade-off chấp nhận được. Ownership mạnh khi cần deterministic destruction, predictable memory footprint, FFI hoặc low-level control.

Nhiều hệ thống kết hợp: Java heap dùng GC nhưng `try-with-resources` quản lý file/socket deterministic; Swift dùng ARC; C++ có `unique_ptr` và `shared_ptr`; Rust có `Rc/Arc` cho shared ownership khi unique ownership không đủ.

## Shared ownership có cost model riêng

Reference counting cần tăng/giảm counter. Atomic reference counting trong multi-threaded context còn có synchronization cost. Cycle cũng có thể khiến pure reference counting không reclaim được nếu không có cơ chế bổ sung.

Vì vậy “không có GC” không có nghĩa memory management miễn phí. Cost chỉ chuyển sang compile-time restriction, refcount operation, allocator behavior hoặc explicit architecture.

## Concurrency safety

Ownership giúp reasoning data race vì quyền mutation có thể bị giới hạn. Nếu object không thể được mutable-access đồng thời từ nhiều thread mà không qua synchronization-safe abstraction, một lớp race condition bị loại bỏ structurally.

Tuy nhiên ownership không chứng minh toàn bộ concurrent program đúng. Deadlock, logical race, starvation và distributed consistency vẫn tồn tại.

## FFI boundary

Khi đi qua Foreign Function Interface, compiler có thể mất khả năng kiểm chứng lifetime/aliasing của external code. Đây là lý do `unsafe` boundary cần nhỏ và có contract rõ: pointer validity, ownership transfer, allocation/deallocation pair và thread-safety phải được xác định.

`unsafe` không có nghĩa “tắt mọi safety”; nó nghĩa programmer nhận trách nhiệm chứng minh invariant mà compiler không thể tự chứng minh.

## Mental model

> Ownership biến resource lifecycle thành một phần của type/data-flow. Move chuyển responsibility; borrow cho phép sử dụng tạm; lifetime chứng minh reference không vượt resource; linear/affine restriction kiểm soát duplication. Mục tiêu không phải loại bỏ mọi runtime bug mà thu hẹp mạnh tập trạng thái memory-unsafe có thể biểu diễn.