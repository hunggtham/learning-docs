# OAuth, OIDC, token lifecycle và federation threats

OAuth 2.x và OpenID Connect thường bị gom thành “đăng nhập bằng token”, nhưng chúng giải quyết các bài toán khác nhau. OAuth chủ yếu là delegated authorization; OIDC thêm identity layer để client biết user đã authenticate là ai.

## Resource owner, client, authorization server và resource server

OAuth tách application muốn gọi API khỏi server phát quyền. Client nhận access token có scope/audience nhất định rồi trình token cho resource server.

Token không nên được hiểu là “password mới dùng ở mọi nơi”. Nó có issuer, audience, expiry và privileges cụ thể.

## Authorization Code + PKCE

Public clients như mobile app/browser không thể giữ client secret thật sự bí mật. PKCE tạo verifier/challenge để authorization code bị intercept khó bị đổi token bởi attacker khác.

Security đến từ binding code exchange với client instance, không phải từ việc nhét static secret vào app binary.

## OIDC và ID token

OIDC thêm ID token chứa claims về authentication event/user. ID token dành cho client xác minh identity; access token dành cho API authorization. Dùng ID token như generic API bearer token làm lẫn trust boundary và audience.

## Token validation

Resource server cần validate signature/MAC theo protocol, issuer, audience, expiry và các claims liên quan. Chỉ decode JWT base64 không phải validation.

Key rotation yêu cầu JWKS/cache strategy. Cache quá lâu có thể giữ key revoked; fetch mỗi request lại tạo dependency/latency mới.

## Refresh token

Access token ngắn hạn giảm exposure window nhưng cần refresh mechanism. Refresh token có quyền mạnh và sống lâu hơn, nên rotation, revocation và secure storage quan trọng.

Refresh-token reuse detection có thể phát hiện token family bị đánh cắp trong rotation scheme.

## Bearer token và proof-of-possession

Bearer token trao quyền cho bất kỳ ai cầm token. Nếu leak qua logs, browser storage hoặc proxy, attacker có thể replay trong thời hạn token.

mTLS-bound token hoặc DPoP-like mechanisms cố bind token với key/client proof, giảm replay nhưng tăng complexity.

## Federation threats

Open redirect, mix-up attack, CSRF trên redirect flow, nonce/state misuse và confused-deputy problems xuất hiện vì nhiều parties trao đổi qua browser/front-channel/back-channel.

`state` giúp bind authorization response với client transaction; OIDC `nonce` giúp bind ID token với authentication request. Mỗi field bảo vệ threat khác nhau.

## Scope không thay thế authorization model

Scope thường coarse-grained. API vẫn cần object-level authorization: user có `read:account` không nghĩa được đọc account của người khác.

Authentication trả lời “ai”; authorization trả lời “được làm gì với resource nào trong context nào”.

## Mental Model

> OAuth/OIDC là federation protocol giữa nhiều trust boundaries. Token chỉ an toàn khi issuer, audience, lifetime, binding và redirect flow đều đúng. Đừng reasoning từ hình dạng JWT; hãy reasoning từ authority được trao và nơi token có thể bị replay.