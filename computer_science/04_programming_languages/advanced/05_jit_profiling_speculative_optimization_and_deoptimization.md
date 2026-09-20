# JIT profiling, speculative optimization và deoptimization

Ahead-of-time compiler phải tối ưu khi chưa biết workload runtime cụ thể. **JIT — Just-In-Time compilation (적시 컴파일)** có lợi thế quan sát program đang chạy: type nào xuất hiện, branch nào thường đi, method nào hot. Nó dùng profile này để tạo machine code chuyên biệt hơn.

## Interpreter, baseline và optimizing tier

Runtime như JVM thường không compile mọi method tối đa ngay lập tức vì optimization tốn CPU và startup time. Code có thể bắt đầu interpreted hoặc baseline-compiled. Khi counters cho thấy method hot, optimizing compiler mới đầu tư nhiều hơn.

Đây là **tiered compilation**: đổi compile cost lấy runtime benefit dựa trên hotness.

## Profile-guided specialization

Giả sử call site gần như luôn nhận cùng concrete class. JIT có thể inline target và loại virtual dispatch, sau đó optimize xuyên function boundary.

Nếu array bounds đã được chứng minh trong loop, bounds checks có thể bị hoist/eliminate. Nếu branch gần như luôn true, code layout có thể ưu tiên hot path.

## Speculation dựa trên assumption

Runtime optimization thường đúng dưới assumption hiện tại, không phải theorem vĩnh viễn. Ví dụ “call site chỉ có class A” có thể đúng trong 10 phút đầu rồi plugin load class B.

JIT gắn **guard** để kiểm tra assumption. Nếu guard fail, runtime chuyển sang **deoptimization**: bỏ optimized frame/code và khôi phục state phù hợp với representation ít specialized hơn.

## On-stack replacement

Một loop dài có thể bắt đầu chạy trong interpreted code rồi trở thành hot trước khi function return. **On-Stack Replacement (OSR)** cho phép chuyển execution giữa tiers ngay giữa active frame/loop.

Điều này đòi hỏi metadata để map locals, stack state và program point giữa representations.

## Escape analysis

Nếu object không escape khỏi method/thread, JIT có thể scalar-replace fields hoặc tránh heap allocation. Source code có `new` nhưng runtime không nhất thiết tạo object vật lý.

Đây là ví dụ vì sao allocation cost không thể suy ra chỉ từ syntax; optimization phụ thuộc escape graph và profile.

## Warm-up và benchmark trap

Microbenchmark JVM chạy quá ngắn có thể đo interpreter/baseline compile thay vì steady-state optimized code. Ngược lại benchmark lặp vô nghĩa có thể bị dead-code elimination.

Framework benchmark cần warm-up, consume results và kiểm soát environment. “Chạy vòng lặp 1 triệu lần rồi đo” dễ cho kết quả sai.

## Deoptimization và latency

JIT tăng throughput nhưng compilation, safepoint và deoptimization có thể ảnh hưởng latency. Production service cần phân biệt startup latency, warm-up, steady-state và tail behavior.

AOT/native image giảm warm-up ở một số trường hợp nhưng mất một phần adaptive profile information. Đây là trade-off, không phải một bên luôn tốt hơn.

## Mental Model

> JIT là optimizer có quyền đặt cược vào behavior runtime. Profile cho bằng chứng, guards bảo vệ assumption, deoptimization là đường thoát khi thế giới thay đổi. Performance cao đến từ specialization có khả năng rollback.