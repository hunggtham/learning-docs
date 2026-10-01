# Interactive proofs, zero-knowledge và verifiable computation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Interactive proofs, zero-knowledge và verifiable computation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Prover mạnh, verifier rẻ** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Completeness và soundness** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Trong NP-style xác minh (verification / 확인), prover đưa một certificate và verifier kiểm tra. Nhưng tương tác (interaction / 상호작용) tạo thêm khả năng: verifier có thể gửi challenge ngẫu nhiên, prover trả lời, rồi verifier dùng nhiều vòng để kiểm tra một claim mà không tự làm toàn bộ computation.

Từ đây xuất hiện ba ý tưởng lớn:

```text
interactive proof
→ kiểm tra claim bằng interaction + randomness

zero-knowledge
→ chứng minh claim mà không tiết lộ thêm secret witness

verifiable computation
→ outsource computation nhưng vẫn kiểm tra result rẻ hơn việc chạy lại toàn bộ
```

Chapter này không nhằm biến người đọc thành cryptographer. Mục tiêu là xây mô hình tư duy (mental model / 사고 모델) về **completeness, soundness, kiến thức (knowledge / 지식) leakage, commitment, challenge và xác minh (verification / 확인) chi phí (cost / 비용)** để hiểu proof các hệ thống (systems / 시스템들) hiện đại mà không dừng ở buzzword như ZK, SNARK hay STARK.

## 1. Prover mạnh, verifier rẻ

Ta có hai actor:

**Prover (người chứng minh / 증명자)** có thể có computation power lớn hoặc biết secret witness.

**Verifier (người kiểm chứng / 검증자)** muốn kiểm tra claim với ít tài nguyên (resource / 자원) hơn và không tin prover.

Giao thức (protocol / 프로토콜) là máy trạng thái (state machine / 상태 머신):

```text
claim x
→ prover message
→ verifier challenge/randomness
→ prover response
→ ...
→ verifier accept/reject
```

Tương tác (interaction / 상호작용) cho verifier tạo bất định (uncertainty / 불확실성) mà prover không biết trước khi lần ghi nhận (commit / 커밋) một phần trạng thái (state / 상태), làm cheating khó hơn.

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **2. Completeness và soundness** tiếp nhận điểm tựa từ **1. Prover mạnh, verifier rẻ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Tại sao randomness giúp verifier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Completeness và soundness

Một proof giao thức (protocol / 프로토콜) cần ít nhất hai đặc tả hợp đồng (contract / 계약).

**Completeness**: nếu statement đúng và prover honest có witness hợp lệ, verifier accept với xác suất cao.

**Soundness**: nếu statement sai, cheating prover không thể làm verifier accept ngoài xác suất nhỏ.

```text
true statement + honest prover
→ accept

false statement + arbitrary cheating prover
→ reject với xác suất cao
```

Soundness có thể là statistical hoặc computational tùy giao thức (protocol / 프로토콜)/giả định (assumption / 가정).

Một proof “thường pass” nhưng không có soundness argument chỉ là kiểm thử (test / 테스트), không phải proof hệ thống (system / 시스템) theo nghĩa mạnh.

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **3. Tại sao randomness giúp verifier** tiếp nhận điểm tựa từ **2. Completeness và soundness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Interactive proof mở rộng xác minh (verification / 확인) power** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Tại sao randomness giúp verifier

Nếu verifier luôn gửi cùng challenge biết trước, prover có thể chuẩn bị phản hồi (response / 응답) giả chỉ cho challenge đó.

Random challenge buộc prover phải có trạng thái (state / 상태) đủ nhất quán để trả lời nhiều khả năng.

Trực giác giống kiểm tra một đối tượng (object / 객체) lớn bằng spot-checking có cấu trúc. Nếu prover không biết verifier sẽ hỏi vị trí/combination nào, việc giả mạo toàn bộ consistency khó hơn.

Nhưng sampling ngẫu nhiên chỉ tạo soundness khi mathematical cấu trúc (structure / 구조) bảo đảm cheating làm nhiều challenge thất bại. “Randomly check vài dòng” không tự động là cryptographic proof.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **4. Interactive proof mở rộng xác minh (verification / 확인) power** tiếp nhận điểm tựa từ **3. Tại sao randomness giúp verifier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Proof of kiến thức (knowledge / 지식) khác proof of statement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Interactive proof mở rộng xác minh (verification / 확인) power

Độ phức tạp (complexity / 복잡도) lý thuyết (theory / 이론) cho thấy tương tác (interaction / 상호작용) + randomness có sức mạnh đáng ngạc nhiên. Kết quả nổi tiếng `IP = PSPACE` nói rằng lớp (class / 클래스) bài toán (problem / 문제) có interactive proof polynomial-time verifier bằng PSPACE.

Điểm cần hiểu không phải thuộc theorem để dùng hàng ngày, mà là insight:

```text
verification power
không chỉ phụ thuộc local compute của verifier
mà còn phụ thuộc protocol interaction + randomness
```

Đọc prerequisite: [Complexity classes beyond P/NP](./06_complexity_classes_conp_pspace_exp_and_randomized_classes.md).

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **5. Proof of kiến thức (knowledge / 지식) khác proof of statement** tiếp nhận điểm tựa từ **4. Interactive proof mở rộng xác minh (verification / 확인) power** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Commitment: khóa lựa chọn trước khi thấy challenge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Proof of kiến thức (knowledge / 지식) khác proof of statement

Một giao thức (protocol / 프로토콜) có thể chứng minh “statement đúng” hoặc mạnh hơn là prover **biết witness** tương ứng theo formal extractor notion.

Ví dụ authentication muốn chứng minh máy khách (client / 클라이언트) biết secret key chứ không chỉ statement “có ai đó tồn tại biết key”.

Proof-of-knowledge lập luận (reasoning / 추론) cần cẩn thận: từ “kiến thức (knowledge / 지식)” trong cryptography có formal meaning qua khả năng extractor lấy witness từ prover đáp ứng giao thức (protocol / 프로토콜), không phải đọc tâm trí actor.

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **6. Commitment: khóa lựa chọn trước khi thấy challenge** tiếp nhận điểm tựa từ **5. Proof of kiến thức (knowledge / 지식) khác proof of statement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Sigma giao thức (protocol / 프로토콜) intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Commitment: khóa lựa chọn trước khi thấy challenge

**Commitment scheme** giống phong bì số:

```text
commit phase:
prover chọn value v + randomness r
→ commitment c

open phase:
prover reveal v,r
→ verifier check c
```

Hai thuộc tính (property / 속성) chính:

**Hiding**: commitment không tiết lộ giá trị (value / 값) trước khi open.

**Binding**: prover không thể dễ dàng mở cùng commitment thành hai giá trị (value / 값) khác nhau.

Commitment tạo temporal bất biến (invariant / 불변식):

```text
prover phải khóa lựa chọn
trước khi biết challenge tiếp theo
```

Nó là thành phần nguyên thủy (primitive / 기본 요소) quan trọng trong zero-knowledge, coin flipping, MPC và nhiều giao thức (protocol / 프로토콜) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **7. Sigma giao thức (protocol / 프로토콜) intuition** tiếp nhận điểm tựa từ **6. Commitment: khóa lựa chọn trước khi thấy challenge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Zero-knowledge: verifier học gì ngoài truth của statement?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Sigma giao thức (protocol / 프로토콜) intuition

Nhiều identification/proof-of-knowledge giao thức (protocol / 프로토콜) có ba bước dạng:

```text
commitment a
→ random challenge e
→ response z
```

thường gọi là **Σ-protocol** vì transcript có ba nhánh message.

Các thuộc tính (property / 속성) như completeness, special soundness và honest-verifier zero-knowledge có thể được chứng minh cho construction cụ thể.

Điểm lập luận (reasoning / 추론) quan trọng: cùng commitment mà trả lời đúng hai challenge khác nhau đôi khi cho phép extractor recover witness. Vì vậy prover không biết witness khó chuẩn bị trạng thái (state / 상태) chịu được challenge ngẫu nhiên.

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **8. Zero-knowledge: verifier học gì ngoài truth của statement?** tiếp nhận điểm tựa từ **7. Sigma giao thức (protocol / 프로토콜) intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Ví dụ trực giác: chứng minh biết password mà không gửi password** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Zero-knowledge: verifier học gì ngoài truth của statement?

Một proof có thể sound nhưng leak witness. **Zero-knowledge (ZK / 영지식 증명)** thêm privacy thuộc tính (property / 속성): verifier không học thêm thông tin đáng kể ngoài việc statement đúng.

Formal intuition dùng **simulator**. Nếu có thuật toán (algorithm / 알고리즘) tạo transcript không phân biệt được với tương tác (interaction / 상호작용) thật mà không biết witness, transcript thật không mang extra kiến thức (knowledge / 지식) mà verifier có thể khai thác.

Mô hình tư duy (mental model / 사고 모델):

```text
real interaction with witness
≈
simulated view without witness
```

Dấu `≈` có thể là perfect, statistical hoặc computational indistinguishability tùy definition.

Zero-knowledge không có nghĩa “không có dữ liệu (data / 데이터) nào được gửi”. Có transcript, commitment, proof bytes; thuộc tính (property / 속성) là transcript không tiết lộ kiến thức (knowledge / 지식) ngoài statement theo mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **8. Zero-knowledge: verifier học gì ngoài truth của statement?** cho ta quy tắc; **9. Ví dụ trực giác: chứng minh biết password mà không gửi password** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **10. Fiat–Shamir: biến challenge interactive thành deterministic băm (hash / 해시) challenge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Ví dụ trực giác: chứng minh biết password mà không gửi password

Authentication cổ điển gửi password qua secure channel rồi máy chủ (server / 서버) so băm (hash / 해시). ZK-style identification hướng tới proof rằng máy khách (client / 클라이언트) biết secret tương ứng công khai (public / 공개) quan hệ (relation / 관계) mà không truyền secret itself.

Nhưng zero-knowledge không tự động giải quyết phishing, compromised endpoint hoặc stolen session đơn vị từ (token / 토큰). Nếu malware đọc witness trước proof hoặc hijack authenticated session sau proof, privacy của transcript không cứu được hệ thống (system / 시스템).

Ranh giới bảo mật (security boundary / 보안 경계) vẫn phải đi end-to-end.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **9. Ví dụ trực giác: chứng minh biết password mà không gửi password** cho ta quy tắc; **10. Fiat–Shamir: biến challenge interactive thành deterministic băm (hash / 해시) challenge** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **11. Non-interactive proof cần setup/giả định (assumption / 가정) gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Fiat–Shamir: biến challenge interactive thành deterministic băm (hash / 해시) challenge

Một số public-coin interactive protocols có thể được chuyển thành non-interactive proof/signature-like construction bằng **Fiat–Shamir heuristic**:

```text
challenge = H(statement, commitment, context...)
```

Thay vì verifier gửi random challenge, prover tính challenge từ băm (hash / 해시) transcript/ngữ cảnh (context / 맥락).

Bảo mật (security / 보안) lập luận (reasoning / 추론) thường dựa trên random-oracle mô hình (model / 모델) hoặc các giả định (assumptions / 가정들)/construction cụ thể. Không được hiểu đơn giản “băm (hash / 해시) là random nên tương tác (interaction / 상호작용) biến mất miễn phí”. lĩnh vực (domain / 도메인) separation, transcript binding và ngữ cảnh (context / 맥락) phải đúng để tránh replay/cross-protocol issue.

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **11. Non-interactive proof cần setup/giả định (assumption / 가정) gì?** tiếp nhận điểm tựa từ **10. Fiat–Shamir: biến challenge interactive thành deterministic băm (hash / 해시) challenge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Succinct proof: verifier rẻ nhưng prover thường đắt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Non-interactive proof cần setup/giả định (assumption / 가정) gì?

Khi không có live verifier challenge, hệ thống (system / 시스템) cần nguồn công khai (public / 공개) parameters hoặc cryptographic giả định (assumption / 가정) tạo unpredictability/binding tương đương.

Một số proof hệ thống (system / 시스템) dùng **trusted setup** để tạo structured tham chiếu (reference / 참조) string. Nếu toxic waste bị giữ và attacker khai thác được, soundness có thể bị phá tùy scheme.

Các scheme khác dùng transparent setup hoặc công khai (public / 공개) randomness nhưng trả chi phí (cost / 비용) khác về proof kích thước (size / 크기), xác minh (verification / 확인) thời gian (time / 시간) hoặc prover công việc (work / 작업).

Không có câu “trusted setup luôn xấu” hoặc “transparent luôn tốt”. Phải so threat mô hình (model / 모델) và operational vòng đời (lifecycle / 생명주기).

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **12. Succinct proof: verifier rẻ nhưng prover thường đắt** tiếp nhận điểm tựa từ **11. Non-interactive proof cần setup/giả định (assumption / 가정) gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Arithmetic circuit và ràng buộc (constraint / 제약조건) biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Succinct proof: verifier rẻ nhưng prover thường đắt

Một mục tiêu của verifiable computation là:

```text
computation C(x) = y
→ prover chạy computation + tạo proof π
→ verifier kiểm tra (x,y,π)
```

Xác minh (verification / 확인) có thể nhỏ hơn nhiều so với chạy lại `C`.

Nhưng prover phải encode computation thành ràng buộc (constraint / 제약조건) hệ thống (system / 시스템)/circuit/dấu vết (trace / 추적) và tạo proof. Prover chi phí (cost / 비용) có thể lớn hơn bản địa (native / 네이티브) computation đáng kể.

Do đó “xác minh (verification / 확인) rẻ” không đồng nghĩa “hệ thống (system / 시스템) tổng thể rẻ”. Cần chi phí (cost / 비용) mô hình (model / 모델):

```text
prover CPU/GPU/memory
proof generation latency
proof size
network/storage
verifier cost
setup/key lifecycle
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **13. Arithmetic circuit và ràng buộc (constraint / 제약조건) biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **12. Succinct proof: verifier rẻ nhưng prover thường đắt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. SNARK là family thuộc tính (property / 속성), không phải một thuật toán (algorithm / 알고리즘) duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Arithmetic circuit và ràng buộc (constraint / 제약조건) biểu diễn (representation / 표현)

Proof hệ thống (system / 시스템) không hiểu mã nguồn (source code / 소스 코드) như nhà phát triển (developer / 개발자). Computation thường được hạ xuống biểu diễn (representation / 표현) toán học: arithmetic circuit, rank-1 ràng buộc (constraint / 제약조건) hệ thống (system / 시스템), polynomial quan hệ (relation / 관계) hoặc thực thi (execution / 실행) dấu vết (trace / 추적) tùy family.

Trình biên dịch (compiler / 컴파일러)/prover chuỗi xử lý (pipeline / 파이프라인):

```text
program / relation
→ circuit/constraints/trace
→ witness assignment
→ polynomial/commitment machinery
→ proof
```

Một thao tác (operation / 연산) rẻ trên CPU chưa chắc rẻ trong circuit. Bitwise thao tác (operation / 연산), phạm vi (range / 범위) check, băm (hash / 해시) hàm (function / 함수) hoặc bộ nhớ (memory / 메모리) truy cập (access / 접근) có chi phí (cost / 비용) profile khác tùy proof hệ thống (system / 시스템).

Đây là lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) quan trọng khi thiết kế ZK ứng dụng (application / 애플리케이션).

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **14. SNARK là family thuộc tính (property / 속성), không phải một thuật toán (algorithm / 알고리즘) duy nhất** tiếp nhận điểm tựa từ **13. Arithmetic circuit và ràng buộc (constraint / 제약조건) biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. STARK intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. SNARK là family thuộc tính (property / 속성), không phải một thuật toán (algorithm / 알고리즘) duy nhất

**SNARK** thường mở rộng thành *Succinct Non-interactive Argument of kiến thức (knowledge / 지식)*. Các construction khác nhau có giả định (assumption / 가정), setup, proof kích thước (size / 크기) và prover/verifier chi phí (cost / 비용) khác nhau.

Từ **argument** thường ngụ ý soundness chống prover computationally bounded thay vì information-theoretic prover vô hạn.

Không nên nói “SNARK dùng elliptic curve” như universal truth; nhiều construction dùng thành phần nguyên thủy (primitive / 기본 요소) khác nhau. Hãy đọc theo thuộc tính (property / 속성) đặc tả hợp đồng (contract / 계약), không theo brand name.

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **15. STARK intuition** tiếp nhận điểm tựa từ **14. SNARK là family thuộc tính (property / 속성), không phải một thuật toán (algorithm / 알고리즘) duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Soundness lỗi (error / 오류) và amplification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. STARK intuition

**STARK** thường nhấn mạnh scalable transparent argument of kiến thức (knowledge / 지식), dùng băm (hash / 해시)/polynomial commitment techniques thay vì trusted setup kiểu một số SNARK cổ điển và hướng tới post-quantum-friendly các giả định (assumptions / 가정들) ở thành phần nguyên thủy (primitive / 기본 요소) nhất định.

Sự đánh đổi (trade-off / 트레이드오프) thường khác về proof kích thước (size / 크기), prover chi phí (cost / 비용) và hiện thực (implementation / 구현) độ phức tạp (complexity / 복잡도).

Điểm cần giữ: SNARK/STARK label không đủ để chọn hệ thống (system / 시스템). Phải so:

```text
statement/circuit shape
prover resources
verification budget
proof size/network
setup trust
cryptographic assumptions
recursion needs
implementation maturity
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **16. Soundness lỗi (error / 오류) và amplification** tiếp nhận điểm tựa từ **15. STARK intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. công khai (public / 공개) verifiability vs designated verifier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Soundness lỗi (error / 오류) và amplification

Nhiều probabilistic proof có non-zero soundness lỗi (error / 오류). Repetition hoặc larger challenge trường dữ liệu (field / 필드) có thể giảm lỗi (error / 오류), nhưng chi phí (cost / 비용) tăng.

Bảo mật (security / 보안) parameter phải được chọn theo threat mô hình (model / 모델) và số proof toàn hệ thống, không chỉ một lần verify.

Nếu một proof có thất bại (failure / 실패) xác suất (probability / 확률) cực nhỏ mỗi instance nhưng hệ thống (system / 시스템) verify hàng tỷ instance, aggregate rủi ro (risk / 위험) vẫn cần lập luận (reasoning / 추론).

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **17. công khai (public / 공개) verifiability vs designated verifier** tiếp nhận điểm tựa từ **16. Soundness lỗi (error / 오류) và amplification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Recursive proofs và aggregation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. công khai (public / 공개) verifiability vs designated verifier

Một proof có thể được bất kỳ ai verify bằng công khai (public / 공개) dữ liệu (data / 데이터) hoặc chỉ verifier có secret mới verify.

Công khai (public / 공개) verifiability hữu ích cho kiểm tra (audit / 감사), blockchain hoặc sản phẩm tạo ra (artifact / 산출물) provenance, nhưng transcript dễ được lưu/chia sẻ hơn. Designated-verifier giao thức (protocol / 프로토콜) có privacy/trust thuộc tính (property / 속성) khác.

Yêu cầu (requirement / 요구사항) “ai cần verify?” phải được xác định trước khi chọn proof thành phần nguyên thủy (primitive / 기본 요소).

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **18. Recursive proofs và aggregation** tiếp nhận điểm tựa từ **17. công khai (public / 공개) verifiability vs designated verifier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Verifiable computation không thay thế availability và authorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Recursive proofs và aggregation

Một proof hệ thống (system / 시스템) có thể chứng minh statement “proof khác đã verify đúng”. Từ đó có recursion/aggregation:

```text
proof_1 + proof_2 + ...
→ aggregate/recursive proof
→ verifier check compact result
```

Use trường hợp (case / 사례) gồm rollup, long computation folding hoặc proof chuỗi (chain / 사슬). Nhưng recursion đòi proof-friendly xác minh (verification / 확인) circuit và tạo độ phức tạp (complexity / 복잡도) mới về trạng thái (state / 상태)/công khai (public / 공개) đầu vào (input / 입력).

Aggregation không tự động bảo đảm dữ liệu (data / 데이터) availability. Có thể chứng minh chuyển tiếp trạng thái (state transition / 상태 전이) hợp lệ nhưng người dùng (user / 사용자) vẫn không có dữ liệu (data / 데이터) cần để reconstruct trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **18. Recursive proofs và aggregation** cho ta quy tắc; **19. Verifiable computation không thay thế availability và authorization** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **20. Zero-knowledge và privacy siêu dữ liệu (metadata / 메타데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Verifiable computation không thay thế availability và authorization

Proof trả lời câu “computation/kết quả (result / 결과) có thỏa quan hệ (relation / 관계) không?”. Nó không tự động trả lời:

- đầu vào (input / 입력) có được authorized không;
- dữ liệu (data / 데이터) có sẵn để người dùng (user / 사용자) dùng không;
- timestamp/thứ tự (order / 순서) có đúng nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) không;
- bên ngoài (external / 외부) oracle có nói thật không;
- endpoint tạo witness có bị compromise không.

Proof hệ thống (system / 시스템) chỉ bảo vệ bất biến (invariant / 불변식) được encode vào statement.

```text
what is not constrained
is not proven
```

Đây là quy tắc (rule / 규칙) quan trọng nhất khi rà soát (review / 검토) ZK/verifiable thiết kế (design / 설계).

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **19. Verifiable computation không thay thế availability và authorization** cho ta quy tắc; **20. Zero-knowledge và privacy siêu dữ liệu (metadata / 메타데이터)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **21. Trusted setup vòng đời (lifecycle / 생명주기) và ceremony** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Zero-knowledge và privacy siêu dữ liệu (metadata / 메타데이터)

Ngay cả khi proof body zero-knowledge, siêu dữ liệu (metadata / 메타데이터) vẫn có thể leak:

- ai gửi proof;
- thời điểm;
- proof frequency;
- công khai (public / 공개) đầu vào (input / 입력);
- mạng (network / 네트워크) đường dẫn (path / 경로);
- giao dịch (transaction / 트랜잭션) đồ thị (graph / 그래프);
- proof kích thước (size / 크기) nếu variable.

Privacy phải lập luận (reasoning / 추론) end-to-end, không dừng ở cryptographic thành phần nguyên thủy (primitive / 기본 요소).

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **20. Zero-knowledge và privacy siêu dữ liệu (metadata / 메타데이터)** nêu điều cần giải thích; **21. Trusted setup vòng đời (lifecycle / 생명주기) và ceremony** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. Side channel ở prover/verifier hiện thực (implementation / 구현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Trusted setup vòng đời (lifecycle / 생명주기) và ceremony

Nếu scheme cần setup, operational questions gồm:

```text
ai tham gia setup?
bao nhiêu participant cần honest?
transcript có public audit không?
toxic waste có thể bị recover không?
parameter có circuit-specific hay universal/updatable?
rotation/migration diễn ra thế nào?
```

Multi-party ceremony có thể giảm trust bằng giả định (assumption / 가정) “ít nhất một participant xóa secret contribution đúng cách”, nhưng hiện thực (implementation / 구현)/ceremony bằng chứng (evidence / 증거) vẫn quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **21. Trusted setup vòng đời (lifecycle / 생명주기) và ceremony** xác định đầu vào; **22. Side channel ở prover/verifier hiện thực (implementation / 구현)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **23. Example: outsourced truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Side channel ở prover/verifier hiện thực (implementation / 구현)

Mathematical zero-knowledge không bảo đảm hiện thực (implementation / 구현) không leak witness qua timing, bộ nhớ (memory / 메모리) truy cập (access / 접근), logs hoặc crash dump.

Nếu witness là secret key, prover mã (code / 코드) vẫn là security-critical mã (code / 코드). Constant-time thành phần nguyên thủy (primitive / 기본 요소), secret bộ nhớ (memory / 메모리) handling và telemetry redaction có thể cần thiết.

Cross-link:

- [Security boundaries, attack chains và exploitability](../../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md)
- [Secret, KMS, HSM, rotation và envelope encryption](../../07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md)

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **22. Side channel ở prover/verifier hiện thực (implementation / 구현)** cho ta quy tắc; **23. Example: outsourced truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **24. Example: private membership proof** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Example: outsourced truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리)

Giả sử máy khách (client / 클라이언트) gửi truy vấn (query / 쿼리) cho untrusted worker và nhận kết quả (result / 결과) aggregate. máy khách (client / 클라이언트) muốn biết worker đã chạy đúng trên committed dataset.

Một verifiable thiết kế (design / 설계) cần bind:

```text
dataset commitment/version
query semantics
execution relation
result
proof
```

Nếu proof chỉ chứng minh “kết quả (result / 결과) là sum của witness rows” nhưng không bind witness rows vào chuẩn gốc (canonical / 정본) dataset phiên bản (version / 버전), worker có thể chọn dataset khác mà vẫn tạo proof hợp lệ.

Bất biến (invariant / 불변식) phải encode **dữ liệu (data / 데이터) provenance**, không chỉ arithmetic tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **23. Example: outsourced truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리)** cho ta quy tắc; **24. Example: private membership proof** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **25. Proof generation dưới pressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Example: private membership proof

Người dùng (user / 사용자) muốn chứng minh mình thuộc một allowlist mà không reveal định danh (identity / 식별자) cụ thể.

Possible quan hệ (relation / 관계):

```text
public: Merkle root R
private witness: leaf + authentication path
statement: witness opens to a member under R
```

Zero-knowledge proof có thể che leaf/đường dẫn (path / 경로) trong construction phù hợp.

Nhưng nếu gốc (root / 루트) cũ vẫn được accept sau revocation, người dùng (user / 사용자) đã bị remove vẫn có thể chứng minh membership theo stale trạng thái (state / 상태). Vì vậy freshness/phiên bản (version / 버전)/epoch phải nằm trong công khai (public / 공개) statement hoặc giao thức (protocol / 프로토콜) ngữ cảnh (context / 맥락).

Cryptographic tính đúng đắn (correctness / 정확성) không thay thế vòng đời (lifecycle / 생명주기) tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **24. Example: private membership proof** cho ta quy tắc; **25. Proof generation dưới pressure** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **26. bằng chứng (evidence / 증거) và khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Proof generation dưới pressure

Môi trường vận hành (production / 운영 환경) prover có thể là heavy compute dịch vụ (service / 서비스). Khi traffic tăng:

```text
proof jobs
→ queue
→ memory/accelerator pressure
→ longer proving latency
→ retries/timeouts
→ overload
```

Proof hệ thống (system / 시스템) vì vậy cũng cần sức chứa (capacity / 용량) planning, batching, admission điều khiển (control / 제어) và thất bại (failure / 실패) khôi phục (recovery / 복구) như software hệ thống (system / 시스템) khác.

Cross-link: [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **25. Proof generation dưới pressure** nêu điều cần giải thích; **26. bằng chứng (evidence / 증거) và khả năng quan sát (observability / 관측 가능성)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **27. Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. bằng chứng (evidence / 증거) và khả năng quan sát (observability / 관측 가능성)

Bằng chứng vận hành (production evidence / 운영 증거) nên gồm:

```text
circuit/relation version
public input hash/version
proving key / verification key version
proof generation latency
prover memory/accelerator utilization
proof size
verification latency
verification failure reason
soundness/security parameter configuration
setup/ceremony provenance
```

Không log private witness chỉ để gỡ lỗi (debug / 디버그). Nếu cần reproduce, dùng synthetic fixture hoặc encrypted controlled capture với chính sách (policy / 정책) phù hợp.

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **26. bằng chứng (evidence / 증거) và khả năng quan sát (observability / 관측 가능성)** đã nêu tiêu chí phân biệt, còn **27. Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **28. liên kết (connection / 연결) map** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Những nhầm lẫn thường gặp

**“Zero-knowledge nghĩa không gửi dữ liệu.”** Sai; thuộc tính (property / 속성) là không leak kiến thức (knowledge / 지식) ngoài statement theo definition.

**“Proof đúng nghĩa đầu vào (input / 입력) nghiệp vụ (business / 비즈니스) hợp lệ.”** Chỉ nếu authorization/provenance/freshness đã được encode.

**“SNARK luôn cần trusted setup.”** Không phải mọi construction.

**“STARK luôn tốt hơn SNARK.”** Không; sự đánh đổi (trade-off / 트레이드오프) khác nhau.

**“Verifier rẻ nghĩa prover cũng rẻ.”** Thường sai.

**“Blockchain cần ZK thì ZK chỉ dùng cho blockchain.”** Sai; verifiable computation, privacy-preserving định danh (identity / 식별자) và outsourced computation đều là use trường hợp (case / 사례) rộng hơn.

**“Cryptographic proof thay thế monitoring.”** Không. hiện thực (implementation / 구현), key vòng đời (lifecycle / 생명주기), queueing và phiên bản (version / 버전) mismatch vẫn cần bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interactive proofs, zero-knowledge và verifiable computation**, **27. Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **28. liên kết (connection / 연결) map** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **29. Checklist lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. liên kết (connection / 연결) map

```text
Complexity theory
→ certificate / verifier / interaction

Randomness
→ unpredictable challenge / soundness

Commitment
→ bind before challenge

Zero-knowledge
→ truth without extra witness leakage

Polynomial/circuit representation
→ encode computation as constraints

Cryptography
→ computational binding/hiding/soundness assumptions

Distributed systems
→ state/version/data availability remain separate invariants

Software systems
→ prover capacity, queueing, rollout and observability
```

> **Chuyển mạch:** Trong **Interactive proofs, zero-knowledge và verifiable computation**, **29. Checklist lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **28. liên kết (connection / 연결) map** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Checklist lập luận (reasoning / 추론)

```text
Statement chính xác đang được chứng minh là gì?
Public input và private witness là gì?
Completeness/soundness contract nào được dùng?
Soundness statistical hay computational?
Verifier học gì ngoài truth của statement?
Challenge/randomness đến từ đâu?
Setup/key/parameter lifecycle thế nào?
Computation được encode thành circuit/trace ra sao?
Prover cost, proof size và verifier cost bao nhiêu?
Freshness, authorization, provenance và data availability có nằm ngoài proof không?
Metadata/implementation có leak witness không?
Evidence nào cho phép audit version và verification failure?
```

> **Chuyển mạch:** Ở chặng này của **Interactive proofs, zero-knowledge và verifiable computation**, **Kết luận** gom các mảnh từ **29. Checklist lập luận (reasoning / 추론)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết luận

Interactive proofs thay đổi cách ta nghĩ về xác minh (verification / 확인): verifier không nhất thiết phải tự làm toàn bộ công việc (work / 작업) để có confidence mạnh về một claim. Zero-knowledge thêm privacy đặc tả hợp đồng (contract / 계약); succinct/verifiable computation thêm mục tiêu giảm xác minh (verification / 확인) chi phí (cost / 비용).

Mô hình tư duy (mental model / 사고 모델) cần giữ:

```text
claim
→ relation/invariant
→ witness
→ commitment/challenge/proof mechanism
→ completeness + soundness
→ optional zero-knowledge
→ verification
```

Proof hệ thống (system / 시스템) chỉ mạnh bằng statement được encode, các giả định (assumptions / 가정들) được giữ và hiện thực (implementation / 구현)/vòng đời (lifecycle / 생명주기) xung quanh nó. Khi ba phần đó được tách rõ, các thuật ngữ ZK, SNARK, STARK hay verifiable computation trở thành những kỹ thuật (engineering / 엔지니어링) sự đánh đổi (trade-off / 트레이드오프) có thể lập luận (reasoning / 추론) thay vì một danh sách công nghệ bí ẩn.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
