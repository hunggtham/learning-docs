# Băm (hash / 해시), MAC, symmetric và public-key cryptography

> **Mạch đọc:** Đặt **băm (hash / 해시), MAC, symmetric và public-key cryptography** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Cryptographic băm (hash / 해시)** sang **Password hashing**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Cryptography (암호학 / mật mã học) dùng mathematical constructions để tạo bảo mật (security / 보안) properties trong adversarial môi trường (environment / 환경). Điều quan trọng là phân biệt primitives: băm (hash / 해시), MAC, encryption và digital signature giải các bài toán khác nhau.

## Cryptographic băm (hash / 해시)

Băm (hash / 해시) hàm (function / 함수) nhận message arbitrary length và tạo fixed-length digest. Security-oriented băm (hash / 해시) muốn preimage resistance, second-preimage resistance và collision resistance ở mức computationally infeasible.

Băm (hash / 해시) không có secret key, nên ai cũng có thể băm (hash / 해시). Vì vậy `hash(message)` không chứng minh message đến từ trusted sender. Integrity chống attacker cần MAC/signature hoặc authenticated giao thức (protocol / 프로토콜).

SHA-256 là cryptographic băm (hash / 해시) phổ biến; MD5/SHA-1 không phù hợp collision-sensitive bảo mật (security / 보안) hiện đại (modern / 현대적) dù có thể còn dùng non-security checksums/legacy identifiers.

## Password hashing

Password không nên lưu bằng fast general băm (hash / 해시). Attacker có cơ sở dữ liệu (database / 데이터베이스) hashes có thể thử billions guesses. Password KDF như Argon2, scrypt, bcrypt hoặc PBKDF2 intentionally expensive và salted.

Salt random unique per password ngăn precomputed rainbow tables và làm identical passwords có hashes khác. Salt không cần secret. Pepper nếu dùng là server-held secret separate from DB.

## MAC

Message Authentication mã (code / 코드) dùng dùng chung (shared / 공유) secret key để tạo tag, cung cấp integrity + authenticity giữa parties biết key. HMAC xây MAC từ cryptographic băm (hash / 해시) theo construction an toàn, không phải `hash(key || message)` tự chế.

MAC không cung cấp non-repudiation giữa parties cùng share key vì cả hai có thể forge tag.

## Symmetric encryption

Same secret key dùng encrypt/decrypt. AES là khối (block / 블록) cipher; ChaCha20 stream cipher. Nhưng raw cipher không đủ: chế độ (mode / 모드)/construction phải cung cấp nonce/IV rules và integrity.

Authenticated Encryption with Associated dữ liệu (data / 데이터) — AEAD như AES-GCM hoặc ChaCha20-Poly1305 cung cấp confidentiality + integrity, đồng thời authenticate associated headers không encrypt.

Nonce reuse có thể catastrophic tùy construction; “random IV bất kỳ” không phải universal quy tắc (rule / 규칙).

## Public-key cryptography

Asymmetric hệ thống (system / 시스템) có công khai (public / 공개)/private key. Encryption/key encapsulation cho phép establish secret tới holder private key; digital signature cho verifier dùng công khai (public / 공개) key kiểm tra signature private-key holder tạo.

Public-key operations chậm hơn symmetric, nên protocols thường dùng asymmetric key exchange/authentication để establish symmetric session keys, rồi bulk encrypt symmetric.

## Digital signature

Signature binds message to private key thao tác (operation / 연산) under thuật toán (algorithm / 알고리즘) các giả định (assumptions / 가정들). xác minh (verification / 확인) cần trustworthy ánh xạ (mapping / 매핑) công khai (public / 공개) key ↔ định danh (identity / 식별자). Nếu attacker thay cả công khai (public / 공개) key lẫn signature, math vẫn verify nhưng định danh (identity / 식별자) sai.

PKI/certificates giải phân phối (distribution / 분포)/trust ánh xạ (mapping / 매핑) bằng certificate authorities và kiểm tra hợp lệ (validation / 검증) rules.

## Key exchange và forward secrecy

Ephemeral Diffie–Hellman variants cho parties derive dùng chung (shared / 공유) secret qua công khai (public / 공개) channel. Nếu ephemeral private keys bị discard, later compromise long-term key không necessarily decrypt past captured sessions — forward secrecy.

TLS hiện đại (modern / 현대적) commonly uses ephemeral key exchange + certificates for authentication.

## Randomness

Cryptographic keys/nonces cần cryptographically secure random generator. `Math.random()`-style PRNG không thích hợp cho secrets nếu predictable. CSPRNG seed/trạng thái (state / 상태) bảo mật (security / 보안) là foundational.

## Checksums vs hashes

CRC detects accidental transmission errors efficiently but attacker có thể deliberately alter message và recompute CRC. Cryptographic integrity primitives assume adversary and are computationally stronger.

## Crypto kỹ thuật (engineering / 엔지니어링)

“Do not roll your own crypto” không chỉ vì math khó; giao thức (protocol / 프로토콜) composition, nonce management, side channels, key rotation, encoding, lỗi (error / 오류) hành vi (behavior / 동작) đều dễ sai. Use mature libraries/protocols and safe APIs.

## Mô hình tư duy (mental model / 사고 모델)

> băm (hash / 해시) = fingerprint không key. MAC = integrity/authenticity với dùng chung (shared / 공유) key. Encryption = confidentiality. AEAD = confidentiality + integrity. Signature = authenticity/integrity với asymmetric key. **Key management quyết định bảo mật (security / 보안) thực tế nhiều như thuật toán (algorithm / 알고리즘).**

## Dùng chung (common / 공통) Misconceptions

**“băm (hash / 해시) là encryption one-way.”** băm (hash / 해시) không phải encryption; goal/giao diện (interface / 인터페이스) khác và không có decryption key.

**“Base64 là encryption.”** Chỉ encoding reversible không secret.

**“Encrypt rồi là không cần integrity.”** Malleability/tampering có thể nguy hiểm; authenticated encryption preferred.

## Kết nối

[Information/encoding](../00_computation_information/01_information_bits_and_encoding.md) phân biệt biểu diễn (representation / 표현). [TLS web request](../06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) compose these primitives. [Identity](./02_identity_authentication_and_authorization.md) dùng passwords/tokens/certificates nhưng authentication ngữ nghĩa (semantics / 의미론) không đồng nhất cryptography.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 threat models and security principles](./00_threat_models_and_security_principles.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
