# Memory safety, mitigations và sandbox boundaries

Memory corruption xảy ra khi chương trình đọc/ghi ngoài lifetime hoặc bounds được phép. Chapter này tập trung defensive reasoning: vì sao bug cấp thấp có thể vượt abstraction boundary và các lớp mitigation giảm exploitability như thế nào.

## Spatial và temporal safety

**Spatial memory safety** yêu cầu access nằm trong bounds của object. **Temporal memory safety** yêu cầu object vẫn còn sống khi access. Buffer overflow vi phạm spatial safety; use-after-free vi phạm temporal safety.

Ngôn ngữ managed hoặc ownership-based có thể loại nhiều class lỗi trước runtime, nhưng native code, FFI và unsafe blocks vẫn là boundary cần chú ý.

## Từ bug tới exploitability

Không phải mọi crash đều exploitable. Attacker cần influence input/state đủ để biến corruption thành primitive hữu ích như control-flow/data corruption. Modern mitigations làm chuỗi này khó hơn.

Defensive review nên hỏi input nào attacker control, object lifetime ra sao, corrupted data có ảnh hưởng authority/control flow không và sandbox giới hạn hậu quả tới đâu.

## DEP/NX

Non-executable memory ngăn data pages được execute như code theo mặc định. Điều này chặn kiểu attack cổ điển ghi shellcode vào stack rồi jump tới đó, nhưng không sửa underlying memory bug.

## ASLR

Address Space Layout Randomization làm vị trí code/libraries/stack khó đoán. Information leak có thể làm giảm hiệu quả ASLR, nên mitigation cần defense-in-depth.

## Stack canary và control-flow protection

Stack canary phát hiện overwrite quanh return metadata trước khi function return. Control-Flow Integrity và hardware features như shadow stack/CET cố hạn chế indirect control transfers.

Mỗi mitigation bảo vệ một class transition, không phải “bật security là xong”.

## Memory-safe languages

Rust ownership/borrowing đưa nhiều lifetime/bounds invariants vào compile-time; Java/C# dùng managed memory và runtime checks. Chúng giảm attack surface nhưng logic bug, unsafe/native libraries và deserialization vẫn tồn tại.

Security gain lớn nhất thường đến từ giảm lượng code cần manual memory management.

## Sandbox

Sandbox giả định component có thể bị compromise và giới hạn quyền của nó: filesystem, network, syscalls, devices hoặc credentials. Browser renderer sandbox là ví dụ: memory bug trong renderer không nên tự động cho quyền toàn OS.

Sandbox escape cần thêm vulnerability ở boundary có quyền cao hơn, tăng số điều kiện attacker phải thỏa.

## Seccomp, capabilities và process isolation

Linux seccomp lọc syscalls; capabilities tách root privileges; namespaces cô lập resource views. Container kết hợp nhiều primitives nhưng không phải security boundary tuyệt đối nếu cấu hình privileged hoặc kernel shared bị khai thác.

## Patch và hardening

Mitigation giảm probability/impact nhưng patch root bug vẫn cần thiết. Compiler hardening, fuzzing, sanitizers và memory-safe migration bổ sung nhau ở các lifecycle khác nhau.

## Mental Model

> Memory security là defense-in-depth quanh một invariant: code chỉ được truy cập memory nó có quyền trong lifetime hợp lệ. Khi invariant có thể vỡ, mitigations làm exploit chain dài hơn và sandbox giảm blast radius.