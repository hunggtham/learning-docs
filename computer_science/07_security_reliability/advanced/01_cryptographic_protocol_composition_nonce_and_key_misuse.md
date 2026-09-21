# Applied cryptographic protocol composition, nonce và key misuse

Cryptographic primitive có thể an toàn về mặt toán học nhưng system vẫn không an toàn nếu primitive được ghép sai. Production security vì thế tập trung không chỉ vào “AES hay RSA mạnh bao nhiêu bit”, mà vào **protocol composition**: key được sinh, phân tách, lưu, rotate và dùng trong context nào; nonce có unique không; ciphertext có integrity không; metadata nào được authenticated.

## Encryption không tự động tạo integrity

Mục tiêu confidentiality là che plaintext; integrity/authenticity là phát hiện dữ liệu bị sửa hoặc giả mạo. Một scheme chỉ mã hóa mà không authenticate có thể không bảo vệ được message khỏi manipulation.

Modern application thường ưu tiên **AEAD — Authenticated Encryption with Associated Data**, nơi encryption và authentication được thiết kế cùng nhau. Associated data cho phép authenticate metadata cần nhìn thấy nhưng không được phép sửa, như protocol version hoặc routing identifier.

## Nonce không nhất thiết bí mật

**Nonce** thường là giá trị “number used once”. Nhiều mode yêu cầu nonce unique dưới cùng key, không yêu cầu nonce secret. Reuse nonce có thể phá guarantee nghiêm trọng tùy construction.

Sai lầm phổ biến là tập trung bảo vệ nonce như password nhưng lại không đảm bảo uniqueness. Requirement phải được đọc đúng theo algorithm/protocol cụ thể.

## Randomness và uniqueness là hai requirement khác nhau

Một nonce random đủ dài có thể đạt uniqueness với xác suất cao, nhưng counter cũng có thể tạo uniqueness nếu lifecycle được quản lý đúng. Sau restart, counter reset mà key vẫn giữ nguyên có thể tái sử dụng nonce.

Do đó design phải reasoning cả persistence, multi-process coordination, backup/restore và key rotation — không chỉ function `random()`.

## Key separation

Dùng cùng key material cho nhiều mục đích có thể tạo interaction không được security proof giả định. **Key derivation function (KDF)** có thể tạo subkeys riêng cho encryption, authentication hoặc từng context/service từ master secret.

Context label/domain separation giúp đảm bảo output dùng cho mục đích A không bị nhầm với mục đích B. Đây là một ví dụ security boundary được encode vào key schedule.

## Password không phải encryption key trực tiếp

Human password có entropy thấp và distribution dễ đoán. Khi password cần dẫn xuất key, protocol dùng password KDF có salt và work factor phù hợp để tăng cost brute-force. Salt không cần secret; nó ngăn precomputation dùng chung giữa nhiều password hashes.

Key encryption key, data encryption key và password-derived key nên được phân biệt theo role thay vì gọi tất cả là “secret key”.

## Rotation không đơn giản là thay một biến

Nếu key mới xuất hiện, dữ liệu cũ vẫn có thể được mã hóa bằng key cũ. Hệ thống cần key identifier/version để biết key nào decrypt object nào, policy giữ old keys bao lâu và migration/re-encryption diễn ra thế nào.

Rotation tốt tách **write key hiện tại** khỏi **read keys còn hợp lệ**. Xóa key cũ quá sớm biến rotation thành data loss; giữ vô hạn làm giảm giá trị của rotation.

## Protocol transcript và downgrade

Handshake thường thương lượng version/algorithm. Nếu negotiation không được authenticated đúng, attacker có thể cố ép hai bên dùng option yếu hơn. Secure protocol cần bind các lựa chọn quan trọng vào authenticated transcript.

Bài học tổng quát: security property của từng message phụ thuộc context của toàn conversation, không chỉ payload hiện tại.

## “Encrypt everything” vẫn cần threat model

Encryption at rest không giúp nếu attacker đã chiếm application process và process có quyền lấy plaintext/key. TLS không bảo vệ dữ liệu sau khi endpoint giải mã. HSM/KMS giảm exposure của key material nhưng không tự giải quyết authorization sai.

Cryptography phải được đặt đúng boundary trong threat model.

## Mental model

> Primitive an toàn là nguyên liệu, protocol an toàn là hệ thống. Nonce uniqueness, key separation, authenticated metadata, rotation và lifecycle đều là một phần của security proof thực tế. Tránh tự thiết kế cryptographic protocol mới khi standard protocol/library đã giải quyết đúng use case; phần khó thường nằm ở composition và key management chứ không phải gọi hàm encrypt.