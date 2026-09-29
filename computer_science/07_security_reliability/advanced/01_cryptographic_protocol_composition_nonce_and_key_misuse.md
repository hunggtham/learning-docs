# Applied cryptographic giao thức (protocol / 프로토콜) composition, nonce và key misuse

> **Mạch đọc:** Đặt **Applied cryptographic giao thức (protocol / 프로토콜) composition, nonce và key misuse** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Encryption không tự động tạo integrity** sang **Nonce không nhất thiết bí mật**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Cryptographic thành phần nguyên thủy (primitive / 기본 요소) có thể an toàn về mặt toán học nhưng hệ thống (system / 시스템) vẫn không an toàn nếu thành phần nguyên thủy (primitive / 기본 요소) được ghép sai. môi trường vận hành (production / 운영 환경) bảo mật (security / 보안) vì thế tập trung không chỉ vào “AES hay RSA mạnh bao nhiêu bit”, mà vào **giao thức (protocol / 프로토콜) composition**: key được sinh, phân tách, lưu, rotate và dùng trong ngữ cảnh (context / 맥락) nào; nonce có unique không; ciphertext có integrity không; siêu dữ liệu (metadata / 메타데이터) nào được authenticated.

## Encryption không tự động tạo integrity

Mục tiêu confidentiality là che plaintext; integrity/authenticity là phát hiện dữ liệu bị sửa hoặc giả mạo. Một scheme chỉ mã hóa mà không authenticate có thể không bảo vệ được message khỏi manipulation.

Hiện đại (modern / 현대적) ứng dụng (application / 애플리케이션) thường ưu tiên **AEAD — Authenticated Encryption with Associated dữ liệu (data / 데이터)**, nơi encryption và authentication được thiết kế cùng nhau. Associated dữ liệu (data / 데이터) cho phép authenticate siêu dữ liệu (metadata / 메타데이터) cần nhìn thấy nhưng không được phép sửa, như giao thức (protocol / 프로토콜) phiên bản (version / 버전) hoặc routing identifier.


> **Chuyển mạch:** Từ **Encryption không tự động tạo integrity**, ta sang **Nonce không nhất thiết bí mật** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Nonce không nhất thiết bí mật

**Nonce** thường là giá trị “number used once”. Nhiều chế độ (mode / 모드) yêu cầu nonce unique dưới cùng key, không yêu cầu nonce secret. Reuse nonce có thể phá guarantee nghiêm trọng tùy construction.

Sai lầm phổ biến là tập trung bảo vệ nonce như password nhưng lại không đảm bảo uniqueness. yêu cầu (requirement / 요구사항) phải được đọc đúng theo thuật toán (algorithm / 알고리즘)/giao thức (protocol / 프로토콜) cụ thể.


> **Chuyển mạch:** Từ **Nonce không nhất thiết bí mật**, ta sang **Randomness và uniqueness là hai yêu cầu (requirement / 요구사항) khác nhau** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Randomness và uniqueness là hai yêu cầu (requirement / 요구사항) khác nhau

Một nonce random đủ dài có thể đạt uniqueness với xác suất cao, nhưng counter cũng có thể tạo uniqueness nếu vòng đời (lifecycle / 생명주기) được quản lý đúng. Sau restart, counter reset mà key vẫn giữ nguyên có thể tái sử dụng nonce.

Do đó thiết kế (design / 설계) phải lập luận (reasoning / 추론) cả persistence, multi-process coordination, backup/restore và key rotation — không chỉ hàm (function / 함수) `random()`.


> **Chuyển mạch:** Từ **Randomness và uniqueness là hai yêu cầu (requirement / 요구사항) khác nhau**, ta sang **Key separation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Key separation

Dùng cùng key material cho nhiều mục đích có thể tạo tương tác (interaction / 상호작용) không được bảo mật (security / 보안) proof giả định. **Key derivation hàm (function / 함수) (KDF)** có thể tạo subkeys riêng cho encryption, authentication hoặc từng ngữ cảnh (context / 맥락)/dịch vụ (service / 서비스) từ master secret.

Ngữ cảnh (context / 맥락) label/lĩnh vực (domain / 도메인) separation giúp đảm bảo đầu ra (output / 출력) dùng cho mục đích A không bị nhầm với mục đích B. Đây là một ví dụ ranh giới bảo mật (security boundary / 보안 경계) được encode vào key schedule.


> **Chuyển mạch:** Từ **Key separation**, ta sang **Password không phải encryption key trực tiếp** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Password không phải encryption key trực tiếp

Human password có entropy thấp và phân phối (distribution / 분포) dễ đoán. Khi password cần dẫn xuất key, giao thức (protocol / 프로토콜) dùng password KDF có salt và công việc (work / 작업) factor phù hợp để tăng chi phí (cost / 비용) brute-force. Salt không cần secret; nó ngăn precomputation dùng chung giữa nhiều password hashes.

Key encryption key, dữ liệu (data / 데이터) encryption key và password-derived key nên được phân biệt theo role thay vì gọi tất cả là “secret key”.


> **Chuyển mạch:** Từ **Password không phải encryption key trực tiếp**, ta sang **Rotation không đơn giản là thay một biến** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Rotation không đơn giản là thay một biến

Nếu key mới xuất hiện, dữ liệu cũ vẫn có thể được mã hóa bằng key cũ. Hệ thống cần key identifier/phiên bản (version / 버전) để biết key nào decrypt đối tượng (object / 객체) nào, chính sách (policy / 정책) giữ old keys bao lâu và di chuyển (migration / 마이그레이션)/re-encryption diễn ra thế nào.

Rotation tốt tách **ghi (write / 쓰기) key hiện tại** khỏi **read keys còn hợp lệ**. Xóa key cũ quá sớm biến rotation thành dữ liệu (data / 데이터) mất mát (loss / 손실); giữ vô hạn làm giảm giá trị của rotation.


> **Chuyển mạch:** Từ **Rotation không đơn giản là thay một biến**, ta sang **giao thức (protocol / 프로토콜) transcript và downgrade** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Giao thức (protocol / 프로토콜) transcript và downgrade

Handshake thường thương lượng phiên bản (version / 버전)/thuật toán (algorithm / 알고리즘). Nếu negotiation không được authenticated đúng, attacker có thể cố ép hai bên dùng option yếu hơn. Secure giao thức (protocol / 프로토콜) cần bind các lựa chọn quan trọng vào authenticated transcript.

Bài học tổng quát: bảo mật (security / 보안) thuộc tính (property / 속성) của từng message phụ thuộc ngữ cảnh (context / 맥락) của toàn conversation, không chỉ payload hiện tại.


> **Chuyển mạch:** Từ **giao thức (protocol / 프로토콜) transcript và downgrade**, ta sang **“Encrypt everything” vẫn cần threat mô hình (model / 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## “Encrypt everything” vẫn cần threat mô hình (model / 모델)

Encryption at rest không giúp nếu attacker đã chiếm ứng dụng (application / 애플리케이션) tiến trình (process / 프로세스) và tiến trình (process / 프로세스) có quyền lấy plaintext/key. TLS không bảo vệ dữ liệu sau khi endpoint giải mã. HSM/KMS giảm exposure của key material nhưng không tự giải quyết authorization sai.

Cryptography phải được đặt đúng ranh giới (boundary / 경계) trong threat mô hình (model / 모델).


> **Chuyển mạch:** Từ **“Encrypt everything” vẫn cần threat mô hình (model / 모델)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> thành phần nguyên thủy (primitive / 기본 요소) an toàn là nguyên liệu, giao thức (protocol / 프로토콜) an toàn là hệ thống. Nonce uniqueness, key separation, authenticated siêu dữ liệu (metadata / 메타데이터), rotation và vòng đời (lifecycle / 생명주기) đều là một phần của bảo mật (security / 보안) proof thực tế. Tránh tự thiết kế cryptographic giao thức (protocol / 프로토콜) mới khi tiêu chuẩn (standard / 표준) giao thức (protocol / 프로토콜)/thư viện (library / 라이브러리) đã giải quyết đúng use trường hợp (case / 사례); phần khó thường nằm ở composition và key management chứ không phải gọi hàm encrypt.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 security boundaries attack chains and exploitability](./00_security_boundaries_attack_chains_and_exploitability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
