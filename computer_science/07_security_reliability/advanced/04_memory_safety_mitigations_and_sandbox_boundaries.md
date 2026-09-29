# Bộ nhớ (memory / 메모리) an toàn (safety / 안전), mitigations và sandbox boundaries

> **Mạch đọc:** Đặt **bộ nhớ (memory / 메모리) an toàn (safety / 안전), mitigations và sandbox boundaries** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Spatial và temporal an toàn (safety / 안전)** sang **Từ bug tới exploitability**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Bộ nhớ (memory / 메모리) corruption xảy ra khi chương trình đọc/ghi ngoài thời gian tồn tại (lifetime / 수명) hoặc bounds được phép. Chapter này tập trung defensive lập luận (reasoning / 추론): vì sao bug cấp thấp có thể vượt lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) và các lớp mitigation giảm exploitability như thế nào.

## Spatial và temporal an toàn (safety / 안전)

**Spatial bộ nhớ (memory / 메모리) an toàn (safety / 안전)** yêu cầu truy cập (access / 접근) nằm trong bounds của đối tượng (object / 객체). **Temporal bộ nhớ (memory / 메모리) an toàn (safety / 안전)** yêu cầu đối tượng (object / 객체) vẫn còn sống khi truy cập (access / 접근). Buffer overflow vi phạm spatial an toàn (safety / 안전); use-after-free vi phạm temporal an toàn (safety / 안전).

Ngôn ngữ managed hoặc ownership-based có thể loại nhiều lớp (class / 클래스) lỗi trước thời gian chạy (runtime / 런타임), nhưng bản địa (native / 네이티브) mã (code / 코드), FFI và unsafe blocks vẫn là ranh giới (boundary / 경계) cần chú ý.


> **Chuyển mạch:** Từ **Spatial và temporal an toàn (safety / 안전)**, ta sang **Từ bug tới exploitability** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Từ bug tới exploitability

Không phải mọi crash đều exploitable. Attacker cần influence đầu vào (input / 입력)/trạng thái (state / 상태) đủ để biến corruption thành thành phần nguyên thủy (primitive / 기본 요소) hữu ích như control-flow/dữ liệu (data / 데이터) corruption. hiện đại (modern / 현대적) mitigations làm chuỗi này khó hơn.

Defensive rà soát (review / 검토) nên hỏi đầu vào (input / 입력) nào attacker điều khiển (control / 제어), đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) ra sao, corrupted dữ liệu (data / 데이터) có ảnh hưởng authority/điều khiển (control / 제어) luồng (flow / 흐름) không và sandbox giới hạn hậu quả tới đâu.


> **Chuyển mạch:** Từ **Từ bug tới exploitability**, ta sang **DEP/NX** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## DEP/NX

Non-executable bộ nhớ (memory / 메모리) ngăn dữ liệu (data / 데이터) pages được execute như mã (code / 코드) theo mặc định. Điều này chặn kiểu attack cổ điển ghi shellcode vào ngăn xếp (stack / 스택) rồi jump tới đó, nhưng không sửa underlying bộ nhớ (memory / 메모리) bug.


> **Chuyển mạch:** Từ **DEP/NX**, ta sang **ASLR** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## ASLR

Address không gian (space / 공간) bố cục (layout / 레이아웃) Randomization làm vị trí mã (code / 코드)/libraries/ngăn xếp (stack / 스택) khó đoán. thông tin (information / 정보) leak có thể làm giảm hiệu quả ASLR, nên mitigation cần defense-in-depth.


> **Chuyển mạch:** Từ **ASLR**, ta sang **ngăn xếp (stack / 스택) canary và control-flow protection** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ngăn xếp (stack / 스택) canary và control-flow protection

Ngăn xếp (stack / 스택) canary phát hiện overwrite quanh return siêu dữ liệu (metadata / 메타데이터) trước khi hàm (function / 함수) return. Control-Flow Integrity và hardware features như shadow ngăn xếp (stack / 스택)/CET cố hạn chế indirect điều khiển (control / 제어) transfers.

Mỗi mitigation bảo vệ một lớp (class / 클래스) chuyển tiếp (transition / 전이), không phải “bật bảo mật (security / 보안) là xong”.


> **Chuyển mạch:** Từ **ngăn xếp (stack / 스택) canary và control-flow protection**, ta sang **Memory-safe languages** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Memory-safe languages

Rust quyền sở hữu (ownership / 소유권)/borrowing đưa nhiều thời gian tồn tại (lifetime / 수명)/bounds invariants vào compile-time; Java/C# dùng managed bộ nhớ (memory / 메모리) và thời gian chạy (runtime / 런타임) checks. Chúng giảm attack surface nhưng lô-gic (logic / 논리) bug, unsafe/bản địa (native / 네이티브) libraries và deserialization vẫn tồn tại.

Bảo mật (security / 보안) gain lớn nhất thường đến từ giảm lượng mã (code / 코드) cần manual bộ nhớ (memory / 메모리) management.


> **Chuyển mạch:** Từ **Memory-safe languages**, ta sang **Sandbox** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sandbox

Sandbox giả định thành phần (component / 컴포넌트) có thể bị compromise và giới hạn quyền của nó: filesystem, mạng (network / 네트워크), syscalls, devices hoặc credentials. trình duyệt (browser / 브라우저) renderer sandbox là ví dụ: bộ nhớ (memory / 메모리) bug trong renderer không nên tự động cho quyền toàn OS.

Sandbox escape cần thêm vulnerability ở ranh giới (boundary / 경계) có quyền cao hơn, tăng số điều kiện attacker phải thỏa.


> **Chuyển mạch:** Từ **Sandbox**, ta sang **Seccomp, capabilities và tiến trình (process / 프로세스) isolation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Seccomp, capabilities và tiến trình (process / 프로세스) isolation

Linux seccomp lọc syscalls; capabilities tách gốc (root / 루트) privileges; namespaces cô lập tài nguyên (resource / 자원) views. bộ chứa (container / 컨테이너) kết hợp nhiều primitives nhưng không phải ranh giới bảo mật (security boundary / 보안 경계) tuyệt đối nếu cấu hình privileged hoặc kernel dùng chung (shared / 공유) bị khai thác.


> **Chuyển mạch:** Từ **Seccomp, capabilities và tiến trình (process / 프로세스) isolation**, ta sang **Patch và hardening** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Patch và hardening

Mitigation giảm xác suất (probability / 확률)/impact nhưng patch gốc (root / 루트) bug vẫn cần thiết. trình biên dịch (compiler / 컴파일러) hardening, fuzzing, sanitizers và memory-safe di chuyển (migration / 마이그레이션) bổ sung nhau ở các vòng đời (lifecycle / 생명주기) khác nhau.


> **Chuyển mạch:** Từ **Patch và hardening**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> bộ nhớ (memory / 메모리) bảo mật (security / 보안) là defense-in-depth quanh một bất biến (invariant / 불변식): mã (code / 코드) chỉ được truy cập bộ nhớ (memory / 메모리) nó có quyền trong thời gian tồn tại (lifetime / 수명) hợp lệ. Khi bất biến (invariant / 불변식) có thể vỡ, mitigations làm exploit chuỗi (chain / 사슬) dài hơn và sandbox giảm blast radius.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 security boundaries attack chains and exploitability](./00_security_boundaries_attack_chains_and_exploitability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
