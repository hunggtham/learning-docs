# Hash, MAC, symmetric và public-key cryptography

Cryptography (암호학 / mật mã học) dùng mathematical constructions để tạo security properties trong adversarial environment. Điều quan trọng là phân biệt primitives: hash, MAC, encryption và digital signature giải các bài toán khác nhau.

## Cryptographic hash

Hash function nhận message arbitrary length và tạo fixed-length digest. Security-oriented hash muốn preimage resistance, second-preimage resistance và collision resistance ở mức computationally infeasible.

Hash không có secret key, nên ai cũng có thể hash. Vì vậy `hash(message)` không chứng minh message đến từ trusted sender. Integrity chống attacker cần MAC/signature hoặc authenticated protocol.

SHA-256 là cryptographic hash phổ biến; MD5/SHA-1 không phù hợp collision-sensitive security modern dù có thể còn dùng non-security checksums/legacy identifiers.

## Password hashing

Password không nên lưu bằng fast general hash. Attacker có database hashes có thể thử billions guesses. Password KDF như Argon2, scrypt, bcrypt hoặc PBKDF2 intentionally expensive và salted.

Salt random unique per password ngăn precomputed rainbow tables và làm identical passwords có hashes khác. Salt không cần secret. Pepper nếu dùng là server-held secret separate from DB.

## MAC

Message Authentication Code dùng shared secret key để tạo tag, cung cấp integrity + authenticity giữa parties biết key. HMAC xây MAC từ cryptographic hash theo construction an toàn, không phải `hash(key || message)` tự chế.

MAC không cung cấp non-repudiation giữa parties cùng share key vì cả hai có thể forge tag.

## Symmetric encryption

Same secret key dùng encrypt/decrypt. AES là block cipher; ChaCha20 stream cipher. Nhưng raw cipher không đủ: mode/construction phải cung cấp nonce/IV rules và integrity.

Authenticated Encryption with Associated Data — AEAD như AES-GCM hoặc ChaCha20-Poly1305 cung cấp confidentiality + integrity, đồng thời authenticate associated headers không encrypt.

Nonce reuse có thể catastrophic tùy construction; “random IV bất kỳ” không phải universal rule.

## Public-key cryptography

Asymmetric system có public/private key. Encryption/key encapsulation cho phép establish secret tới holder private key; digital signature cho verifier dùng public key kiểm tra signature private-key holder tạo.

Public-key operations chậm hơn symmetric, nên protocols thường dùng asymmetric key exchange/authentication để establish symmetric session keys, rồi bulk encrypt symmetric.

## Digital signature

Signature binds message to private key operation under algorithm assumptions. Verification cần trustworthy mapping public key ↔ identity. Nếu attacker thay cả public key lẫn signature, math vẫn verify nhưng identity sai.

PKI/certificates giải distribution/trust mapping bằng certificate authorities và validation rules.

## Key exchange và forward secrecy

Ephemeral Diffie–Hellman variants cho parties derive shared secret qua public channel. Nếu ephemeral private keys bị discard, later compromise long-term key không necessarily decrypt past captured sessions — forward secrecy.

TLS modern commonly uses ephemeral key exchange + certificates for authentication.

## Randomness

Cryptographic keys/nonces cần cryptographically secure random generator. `Math.random()`-style PRNG không thích hợp cho secrets nếu predictable. CSPRNG seed/state security là foundational.

## Checksums vs hashes

CRC detects accidental transmission errors efficiently but attacker có thể deliberately alter message và recompute CRC. Cryptographic integrity primitives assume adversary and are computationally stronger.

## Crypto engineering

“Do not roll your own crypto” không chỉ vì math khó; protocol composition, nonce management, side channels, key rotation, encoding, error behavior đều dễ sai. Use mature libraries/protocols and safe APIs.

## Mental Model

> Hash = fingerprint không key. MAC = integrity/authenticity với shared key. Encryption = confidentiality. AEAD = confidentiality + integrity. Signature = authenticity/integrity với asymmetric key. **Key management quyết định security thực tế nhiều như algorithm.**

## Common Misconceptions

**“Hash là encryption one-way.”** Hash không phải encryption; goal/interface khác và không có decryption key.

**“Base64 là encryption.”** Chỉ encoding reversible không secret.

**“Encrypt rồi là không cần integrity.”** Malleability/tampering có thể nguy hiểm; authenticated encryption preferred.

## Kết nối

[Information/encoding](../00_computation_information/01_information_bits_and_encoding.md) phân biệt representation. [TLS web request](../06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) compose these primitives. [Identity](./02_identity_authentication_and_authorization.md) dùng passwords/tokens/certificates nhưng authentication semantics không đồng nhất cryptography.
