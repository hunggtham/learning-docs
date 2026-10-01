# Băm (hash / 해시), MAC, symmetric và public-key cryptography

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Cryptographic băm (hash / 해시)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Password hashing** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Cryptography (암호학 / mật mã học) dùng mathematical constructions để tạo bảo mật (security / 보안) properties trong adversarial môi trường (environment / 환경). Điều quan trọng là phân biệt primitives: băm (hash / 해시), MAC, encryption và digital signature giải các bài toán khác nhau.

## Cryptographic băm (hash / 해시)

Băm (hash / 해시) hàm (function / 함수) nhận message arbitrary length và tạo fixed-length digest. Security-oriented băm (hash / 해시) muốn preimage resistance, second-preimage resistance và collision resistance ở mức computationally infeasible.

Băm (hash / 해시) không có secret key, nên ai cũng có thể băm (hash / 해시). Vì vậy `hash(message)` không chứng minh message đến từ trusted sender. Integrity chống attacker cần MAC/signature hoặc authenticated giao thức (protocol / 프로토콜).

SHA-256 là cryptographic băm (hash / 해시) phổ biến; MD5/SHA-1 không phù hợp collision-sensitive bảo mật (security / 보안) hiện đại (modern / 현대적) dù có thể còn dùng non-security checksums/legacy identifiers.

> **Chuyển mạch:** Cryptographic hash gives integrity primitive; password hashing adds salt/cost for offline resistance, while MAC next authenticates message origin with a shared secret.

## Password hashing

Password không nên lưu bằng fast general băm (hash / 해시). Attacker có cơ sở dữ liệu (database / 데이터베이스) hashes có thể thử billions guesses. Password KDF như Argon2, scrypt, bcrypt hoặc PBKDF2 intentionally expensive và salted.

Salt random unique per password ngăn precomputed rainbow tables và làm identical passwords có hashes khác. Salt không cần secret. Pepper nếu dùng là server-held secret separate from DB.

> **Chuyển mạch:** Ở chặng này của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **MAC** tiếp nhận điểm tựa từ **Password hashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Symmetric encryption** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MAC

Message Authentication mã (code / 코드) dùng dùng chung (shared / 공유) secret key để tạo tag, cung cấp integrity + authenticity giữa parties biết key. HMAC xây MAC từ cryptographic băm (hash / 해시) theo construction an toàn, không phải `hash(key || message)` tự chế.

MAC không cung cấp non-repudiation giữa parties cùng share key vì cả hai có thể forge tag.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Symmetric encryption** tiếp nhận điểm tựa từ **MAC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Public-key cryptography** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Symmetric encryption

Same secret key dùng encrypt/decrypt. AES là khối (block / 블록) cipher; ChaCha20 stream cipher. Nhưng raw cipher không đủ: chế độ (mode / 모드)/construction phải cung cấp nonce/IV rules và integrity.

Authenticated Encryption with Associated dữ liệu (data / 데이터) — AEAD như AES-GCM hoặc ChaCha20-Poly1305 cung cấp confidentiality + integrity, đồng thời authenticate associated headers không encrypt.

Nonce reuse có thể catastrophic tùy construction; “random IV bất kỳ” không phải universal quy tắc (rule / 규칙).

> **Chuyển mạch:** Trong **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Public-key cryptography** tiếp nhận điểm tựa từ **Symmetric encryption** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Digital signature** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Public-key cryptography

Asymmetric hệ thống (system / 시스템) có công khai (public / 공개)/private key. Encryption/key encapsulation cho phép establish secret tới holder private key; digital signature cho verifier dùng công khai (public / 공개) key kiểm tra signature private-key holder tạo.

Public-key operations chậm hơn symmetric, nên protocols thường dùng asymmetric key exchange/authentication để establish symmetric session keys, rồi bulk encrypt symmetric.

> **Chuyển mạch:** Ở chặng này của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Digital signature** tiếp nhận điểm tựa từ **Public-key cryptography** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Key exchange và forward secrecy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Digital signature

Signature binds message to private key thao tác (operation / 연산) under thuật toán (algorithm / 알고리즘) các giả định (assumptions / 가정들). xác minh (verification / 확인) cần trustworthy ánh xạ (mapping / 매핑) công khai (public / 공개) key ↔ định danh (identity / 식별자). Nếu attacker thay cả công khai (public / 공개) key lẫn signature, math vẫn verify nhưng định danh (identity / 식별자) sai.

PKI/certificates giải phân phối (distribution / 분포)/trust ánh xạ (mapping / 매핑) bằng certificate authorities và kiểm tra hợp lệ (validation / 검증) rules.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Key exchange và forward secrecy** tiếp nhận điểm tựa từ **Digital signature** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Randomness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Key exchange và forward secrecy

Ephemeral Diffie–Hellman variants cho parties derive dùng chung (shared / 공유) secret qua công khai (public / 공개) channel. Nếu ephemeral private keys bị discard, later compromise long-term key không necessarily decrypt past captured sessions — forward secrecy.

TLS hiện đại (modern / 현대적) commonly uses ephemeral key exchange + certificates for authentication.

> **Chuyển mạch:** Trong **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Randomness** tiếp nhận điểm tựa từ **Key exchange và forward secrecy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checksums vs hashes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Randomness

Cryptographic keys/nonces cần cryptographically secure random generator. `Math.random()`-style PRNG không thích hợp cho secrets nếu predictable. CSPRNG seed/trạng thái (state / 상태) bảo mật (security / 보안) là foundational.

> **Chuyển mạch:** Ở chặng này của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Checksums vs hashes** tiếp nhận điểm tựa từ **Randomness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Crypto kỹ thuật (engineering / 엔지니어링)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Checksums vs hashes

CRC detects accidental transmission errors efficiently but attacker có thể deliberately alter message và recompute CRC. Cryptographic integrity primitives assume adversary and are computationally stronger.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Crypto kỹ thuật (engineering / 엔지니어링)** tiếp nhận điểm tựa từ **Checksums vs hashes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Crypto kỹ thuật (engineering / 엔지니어링)

“Do not roll your own crypto” không chỉ vì math khó; giao thức (protocol / 프로토콜) composition, nonce management, side channels, key rotation, encoding, lỗi (error / 오류) hành vi (behavior / 동작) đều dễ sai. Use mature libraries/protocols and safe APIs.

> **Chuyển mạch:** Trong **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Crypto kỹ thuật (engineering / 엔지니어링)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> băm (hash / 해시) = fingerprint không key. MAC = integrity/authenticity với dùng chung (shared / 공유) key. Encryption = confidentiality. AEAD = confidentiality + integrity. Signature = authenticity/integrity với asymmetric key. **Key management quyết định bảo mật (security / 보안) thực tế nhiều như thuật toán (algorithm / 알고리즘).**

> **Chuyển mạch:** Ở chặng này của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“băm (hash / 해시) là encryption one-way.”** băm (hash / 해시) không phải encryption; goal/giao diện (interface / 인터페이스) khác và không có decryption key.

**“Base64 là encryption.”** Chỉ encoding reversible không secret.

**“Encrypt rồi là không cần integrity.”** Malleability/tampering có thể nguy hiểm; authenticated encryption preferred.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Băm (hash / 해시), MAC, symmetric và public-key cryptography**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Information/encoding](../00_computation_information/01_information_bits_and_encoding.md) phân biệt biểu diễn (representation / 표현). [TLS web request](../06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) compose these primitives. [Identity](./02_identity_authentication_and_authorization.md) dùng passwords/tokens/certificates nhưng authentication ngữ nghĩa (semantics / 의미론) không đồng nhất cryptography.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
