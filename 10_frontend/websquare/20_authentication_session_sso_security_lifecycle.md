# 20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bốn khái niệm phải tách riêng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. bảo mật (security / 보안) máy trạng thái (state machine / 상태 머신) thay vì boolean isLogin** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối authentication với session, SSO và security lifecycle, để phân biệt danh tính, phiên đăng nhập, token và quyền sử dụng.

Một màn hình WebSquare có thể chạy đúng về UI, DataList và Submission nhưng vẫn sai ở cấp hệ thống nếu nhà phát triển (developer / 개발자) không phân biệt **định danh (identity / 식별자)**, **authentication**, **session**, **authorization** và **screen trạng thái (state / 상태)**. Đây là một trong những nguồn bug khó nhất ở ứng dụng enterprise vì trình duyệt (browser / 브라우저) thường giữ page instance rất lâu, trong khi session phía máy chủ (server / 서버) có thời gian tồn tại (lifetime / 수명) khác.

Chapter này không biến WebSquare thành bảo mật (security / 보안) khung phần mềm (framework / 프레임워크). Authentication và authorization thật sự thuộc máy chủ (server / 서버)/định danh (identity / 식별자) nền tảng (platform / 플랫폼). Mục tiêu ở đây là hiểu **máy khách (client / 클라이언트) vòng đời (lifecycle / 생명주기) phải phản ứng thế nào khi bảo mật (security / 보안) trạng thái (state / 상태) thay đổi**, đặc biệt trong SPA, multi-tab, popup, hybrid app và Submission đang chạy.

> mô hình tư duy (mental model / 사고 모델) chính: `UI state != authentication state != authorization state != server session state`.

## 1. Bốn khái niệm phải tách riêng

**định danh (identity / 식별자)** trả lời “người dùng hoặc dịch vụ (service / 서비스) principal này là ai?”.

**Authentication** trả lời “hệ thống đã xác minh định danh (identity / 식별자) bằng cơ chế nào?”.

**Session** là trạng thái liên tục cho phép nhiều yêu cầu (request / 요청) thuộc cùng một authenticated tương tác (interaction / 상호작용). Session có thể dựa trên server-side session cookie, đơn vị từ (token / 토큰) hoặc kiến trúc khác.

**Authorization** trả lời “định danh (identity / 식별자) hiện tại được phép thực hiện thao tác (operation / 연산) nào trên tài nguyên (resource / 자원) nào?”.

Một menu bị ẩn chỉ là presentation. Một button disabled chỉ là UX. Một DataMap chứa `role=ADMIN` chỉ là máy khách (client / 클라이언트) trạng thái (state / 상태). Không thứ nào trong số đó thay thế máy chủ (server / 서버) authorization.

> **Nối mạch:** Authentication, session, SSO và authorization là bốn khái niệm riêng; state machine tiếp theo biểu diễn chuyển trạng thái, còn session lifetime không trùng page lifetime.

## 2. bảo mật (security / 보안) máy trạng thái (state machine / 상태 머신) thay vì boolean `isLogin`

Trong app lớn, `isLogin = true/false` quá nghèo thông tin. Một mô hình (model / 모델) thực tế hơn:

```text
UNKNOWN
→ AUTHENTICATING
→ AUTHENTICATED
→ ACTIVE
→ EXPIRING
→ EXPIRED
→ REAUTHENTICATING
→ LOGGED_OUT
```

Có thể thêm `LOCKED`, `MFA_REQUIRED`, `PASSWORD_CHANGE_REQUIRED` hoặc `TERMS_REQUIRED` tùy hệ thống.

Điểm quan trọng là mỗi trạng thái (state / 상태) cho phép một tập hành động (action / 동작) khác nhau. `AUTHENTICATED` chưa chắc đã đồng nghĩa ứng dụng (application / 애플리케이션) shell và permission dữ liệu (data / 데이터) đã ready. `EXPIRED` không có nghĩa page instance tự biến mất. `REAUTHENTICATING` không nên để Save tiếp tục như chưa có gì xảy ra.

> **Nối mạch:** State machine phân biệt auth states; session lifetime và page lifetime chạy trên hai clock, nên expiration phải phát thành application-level event.

## 3. Session thời gian tồn tại (lifetime / 수명) và page thời gian tồn tại (lifetime / 수명) là hai đồng hồ khác nhau

SPA WebSquare có thể giữ shell nhiều giờ. Session máy chủ (server / 서버) có thể hết thời gian chờ (timeout / 타임아웃) sau 30 phút inactivity. Tab trình duyệt (browser / 브라우저) có thể sleep rồi resume. Laptop có thể suspend. Hybrid WebView có thể background rồi quay lại sau vài giờ.

Do đó:

```text
page lifetime      ───────────────────────────────>
server session     ───────────────X
pending UI state   ───────────────────────────────>
```

Sau điểm `X`, DataList và Grid vẫn còn trong trình duyệt (browser / 브라우저) nhưng máy chủ (server / 서버) không còn coi yêu cầu (request / 요청) là authenticated.

Đây là lý do không được suy luận “màn hình vẫn mở nên session còn sống”.

> **Nối mạch:** Expiration là app event để mọi page phản ứng nhất quán; khi xử lý, phân biệt 401/403 với business error để chọn recovery đúng.

## 4. Session expiration phải là application-level sự kiện (event / 이벤트)

Nếu mỗi Submission tự xử lý session expiration bằng một alert khác nhau, ứng dụng (application / 애플리케이션) sẽ nhanh chóng hỗn loạn.

Một kiến trúc tốt thường có dùng chung (common / 공통) communication tầng (layer / 계층) nhận diện auth thất bại (failure / 실패) và phát một sự kiện (event / 이벤트)/chuyển tiếp (transition / 전이) thống nhất:

```text
Submission response
→ classify transport/business/auth error
→ AUTH_EXPIRED event
→ block new protected commands
→ preserve/discard working state theo policy
→ redirect/re-authenticate
→ restore/reload theo contract
```

Không nên để 20 page cùng lúc mở 20 login popup khi session hết hạn.

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **5. 401, 403 và nghiệp vụ (business / 비즈니스) lỗi (error / 오류) không giống nhau** nối từ **4. Session expiration phải là application-level sự kiện (event / 이벤트)** sang **6. Submission interceptor/dùng chung (common / 공통) handler**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. 401, 403 và nghiệp vụ (business / 비즈니스) lỗi (error / 오류) không giống nhau

Một convention phổ biến:

```text
401 / unauthenticated
→ credential/session không còn hợp lệ

403 / forbidden
→ identity hợp lệ nhưng không có quyền

409 / conflict
→ version/concurrency conflict

422 hoặc business envelope
→ validation/business rule failure
```

Chính xác (exact / 정확한) HTTP đặc tả hợp đồng (contract / 계약) phụ thuộc backend, nhưng frontend phải phân loại được ý nghĩa. Nếu mọi lỗi đều hiện “hệ thống (system / 시스템) lỗi (error / 오류)”, người dùng không biết cần login lại, sửa dữ liệu hay liên hệ hỗ trợ (support / 지원).

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **6. Submission interceptor/dùng chung (common / 공통) handler** nối từ **5. 401, 403 và nghiệp vụ (business / 비즈니스) lỗi (error / 오류) không giống nhau** sang **7. Không thử lại (retry / 재시도) mù yêu cầu (request / 요청) sau login**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Submission interceptor/dùng chung (common / 공통) handler

WebSquare SP5 cho phép cấu hình và handler quanh Submission; chính xác (exact / 정확한) API/thuộc tính (property / 속성) phải kiểm tra theo engine bản dựng (build / 빌드). Về kiến trúc (architecture / 아키텍처), mục tiêu là có một ranh giới (boundary / 경계) chung:

```javascript
scwin.handleCommunicationError = function(error) {
    var type = appErrorClassifier.classify(error);

    if (type === "AUTH_EXPIRED") {
        authCoordinator.expire();
        return;
    }

    if (type === "FORBIDDEN") {
        permissionCoordinator.showDenied();
        return;
    }

    errorPresenter.show(error);
};
```

Tên API ở trên là dự án (project / 프로젝트) lớp trừu tượng (abstraction / 추상화), không phải WebSquare built-in API. Điều quan trọng là **classification và orchestration không bị bản sao (copy / 복사) vào từng screen**.

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **7. Không thử lại (retry / 재시도) mù yêu cầu (request / 요청) sau login** nối từ **6. Submission interceptor/dùng chung (common / 공통) handler** sang **8. Working trạng thái (state / 상태) khi session hết hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Không thử lại (retry / 재시도) mù yêu cầu (request / 요청) sau login

Giả sử Save yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) vì session expired. người dùng (user / 사용자) login lại. Có nên tự động gửi lại Save?

Không thể trả lời chỉ từ frontend.

Nếu thao tác (operation / 연산) có side tác động (effect / 효과) và yêu cầu (request / 요청) cũ có thể đã lần ghi nhận (commit / 커밋) trước khi auth tầng (layer / 계층) trả lỗi, thử lại (retry / 재시도) mù có thể duplicate. Chapter 15 đã giải thích idempotency; bảo mật (security / 보안) vòng đời (lifecycle / 생명주기) phải nối với đặc tả hợp đồng (contract / 계약) đó.

Safe thử lại (retry / 재시도) cần biết:

```text
operation read-only hay mutating?
idempotency key có không?
server có commit trước failure không?
request body còn hợp lệ sau re-auth không?
entity version có thay đổi không?
```

Read truy vấn (query / 쿼리) thường dễ thử lại (retry / 재시도) hơn Save/Approve/Transfer.

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **8. Working trạng thái (state / 상태) khi session hết hạn** nối từ **7. Không thử lại (retry / 재시도) mù yêu cầu (request / 요청) sau login** sang **9. SSO không loại bỏ session vòng đời (lifecycle / 생명주기)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Working trạng thái (state / 상태) khi session hết hạn

Một screen edit có thể chứa 20 phút thay đổi chưa save. Khi session expire, có ba chính sách (policy / 정책) thường gặp:

**Discard** — phù hợp dữ liệu nhạy cảm hoặc workflow yêu cầu reload.

**Preserve locally in bộ nhớ (memory / 메모리)** — sau login lại có thể cho người dùng (user / 사용자) rà soát (review / 검토) và save nếu máy chủ (server / 서버) phiên bản (version / 버전) còn phù hợp.

**Persist draft** — chỉ dùng nếu bảo mật (security / 보안)/privacy cho phép và có thiết kế rõ; không tự ý lưu PII vào localStorage.

Chính sách (policy / 정책) phải được quyết định theo lĩnh vực (domain / 도메인), không phải nhà phát triển (developer / 개발자) tự chọn trong từng page.

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **8. Working trạng thái (state / 상태) khi session hết hạn** đặt đầu vào cho **9. SSO không loại bỏ session vòng đời (lifecycle / 생명주기)**, rồi **10. OIDC/OAuth2 và SAML: hiểu ranh giới (boundary / 경계), không nhét giao thức (protocol / 프로토콜) vào page** mở rộng hệ quả hoặc giới hạn liên quan.

## 9. SSO không loại bỏ session vòng đời (lifecycle / 생명주기)

Single Sign-On (SSO / 통합 인증) chỉ làm nhiều ứng dụng (application / 애플리케이션) dùng chung định danh (identity / 식별자) provider hoặc authentication luồng (flow / 흐름). Nó không có nghĩa mỗi ứng dụng (application / 애플리케이션) session tồn tại mãi.

Có thể có:

```text
Identity Provider session = active
Application session = expired
```

Khi app redirect/re-authenticate, IdP có thể xác nhận người dùng (user / 사용자) mà không hỏi password lại. Với người dùng (user / 사용자) cảm giác như “tự login lại”, nhưng ứng dụng (application / 애플리케이션) vẫn phải xử lý pending yêu cầu (request / 요청) và working trạng thái (state / 상태) đúng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **9. SSO không loại bỏ session vòng đời (lifecycle / 생명주기)** đặt tiêu chí; **10. OIDC/OAuth2 và SAML: hiểu ranh giới (boundary / 경계), không nhét giao thức (protocol / 프로토콜) vào page** dùng tiêu chí đó để kiểm tra ranh giới, rồi **11. Cookie-based session và CSRF** mở rộng hệ quả.

## 10. OIDC/OAuth2 và SAML: hiểu ranh giới (boundary / 경계), không nhét giao thức (protocol / 프로토콜) vào page

Enterprise SSO thường gặp OpenID Connect/OAuth 2.0 hoặc SAML. WebSquare page không nên tự implement cryptography, đơn vị từ (token / 토큰) kiểm tra hợp lệ (validation / 검증) hoặc giao thức (protocol / 프로토콜) exchange.

Page cần biết đặc tả hợp đồng (contract / 계약) ở mức:

```text
auth state
current principal summary
permission/capability
session expiry/re-auth event
logout command
```

Đơn vị từ (token / 토큰) signature kiểm tra hợp lệ (validation / 검증), authorization mã (code / 코드) exchange, refresh đơn vị từ (token / 토큰) chính sách (policy / 정책), SAML assertion kiểm tra hợp lệ (validation / 검증) và key rotation thuộc auth/backend/hạ tầng (infrastructure / 인프라) tầng (layer / 계층).

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **10. OIDC/OAuth2 và SAML: hiểu ranh giới (boundary / 경계), không nhét giao thức (protocol / 프로토콜) vào page** đặt tiêu chí; **11. Cookie-based session và CSRF** dùng tiêu chí đó để kiểm tra ranh giới, rồi **12. HttpOnly, Secure, SameSite và vì sao page không nên đọc session secret** mở rộng hệ quả.

## 11. Cookie-based session và CSRF

Nếu trình duyệt (browser / 브라우저) tự gửi session cookie, một yêu cầu (request / 요청) thay đổi dữ liệu có thể cần CSRF protection tùy kiến trúc. UI không thể “chống CSRF” chỉ bằng hidden button.

Mô hình tư duy (mental model / 사고 모델):

```text
browser credential automatically attached
+ attacker-controlled cross-site request
= cần server-side CSRF defense phù hợp
```

Frontend có thể tham gia bằng CSRF đơn vị từ (token / 토큰)/header đặc tả hợp đồng (contract / 계약), nhưng máy chủ (server / 서버) phải verify. chính xác (exact / 정확한) cơ chế (mechanism / 메커니즘) phụ thuộc bảo mật (security / 보안) ngăn xếp (stack / 스택).

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **12. HttpOnly, Secure, SameSite và vì sao page không nên đọc session secret** nối từ **11. Cookie-based session và CSRF** sang **13. Authorization phải theo năng lực (capability / 역량)/tài nguyên (resource / 자원)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. `HttpOnly`, `Secure`, `SameSite` và vì sao page không nên đọc session secret

Session cookie nhạy cảm thường nên được bảo vệ bằng trình duyệt (browser / 브라우저) cookie attributes phù hợp. Nếu credential được thiết kế `HttpOnly`, JavaScript không đọc được nó — đó là tính năng (feature / 기능) bảo mật, không phải limitation cần workaround.

Không bản sao (copy / 복사) session/đơn vị từ (token / 토큰) secret vào DataMap chỉ để “dễ dùng”. DataCollection có thể bị inspect, log hoặc serialize nhầm qua Submission.

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **12. HttpOnly, Secure, SameSite và vì sao page không nên đọc session secret** đặt vấn đề; **13. Authorization phải theo năng lực (capability / 역량)/tài nguyên (resource / 자원)** đối chiếu bằng chứng, rồi **14. Permission snapshot có thể stale** mở rộng hệ quả hoặc giới hạn liên quan.

## 13. Authorization phải theo năng lực (capability / 역량)/tài nguyên (resource / 자원)

Anti-pattern:

```javascript
if (dmUser.get("role") === "ADMIN") {
    btnApprove.show();
}
```

Điều này có thể dùng cho presentation, nhưng máy chủ (server / 서버) vẫn phải authorize `APPROVE_ORDER` trên thứ tự (order / 순서) cụ thể.

Frontend kiến trúc (architecture / 아키텍처) tốt hơn khi dùng năng lực (capability / 역량):

```text
canSearchEmployee
canEditEmployee
canApproveOrder
canExportPersonalData
```

Năng lực (capability / 역량) dễ map vào UI hơn role name, và giảm coupling với mô hình role phía máy chủ (server / 서버).

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **13. Authorization phải theo năng lực (capability / 역량)/tài nguyên (resource / 자원)** đặt vấn đề; **14. Permission snapshot có thể stale** đối chiếu bằng chứng, rồi **15. Multi-tab trình duyệt (browser / 브라우저) và logout propagation** mở rộng hệ quả hoặc giới hạn liên quan.

## 14. Permission snapshot có thể stale

Permission có thể thay đổi trong khi người dùng (user / 사용자) đang mở app. Vì vậy máy khách (client / 클라이언트) permission chỉ là snapshot phục vụ UX.

Nếu admin thu hồi quyền, yêu cầu (request / 요청) tiếp theo vẫn phải bị máy chủ (server / 서버) reject dù button hiện tại còn visible.

Khi nhận forbidden phản hồi (response / 응답), frontend nên reconcile UI hoặc refresh permission snapshot thay vì kết luận “backend bug vì button đang hiện”.

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **15. Multi-tab trình duyệt (browser / 브라우저) và logout propagation** nối từ **14. Permission snapshot có thể stale** sang **16. App shell phải sở hữu auth coordination**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Multi-tab trình duyệt (browser / 브라우저) và logout propagation

Người dùng (user / 사용자) có thể mở nhiều trình duyệt (browser / 브라우저) tab cùng ứng dụng (application / 애플리케이션).

Tab A logout nhưng Tab B vẫn giữ DataList và UI cũ. yêu cầu (request / 요청) tiếp theo ở Tab B phải thất bại (fail / 실패) theo máy chủ (server / 서버) trạng thái (state / 상태).

Có thể dùng trình duyệt (browser / 브라우저) coordination cơ chế (mechanism / 메커니즘) phù hợp để cải thiện UX, nhưng tính đúng đắn (correctness / 정확성) không được phụ thuộc vào việc sự kiện (event / 이벤트) logout luôn truyền được giữa tab.

Bất biến (invariant / 불변식):

```text
server authorization/session = canonical
cross-tab notification = UX optimization
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **16. App shell phải sở hữu auth coordination** nối từ **15. Multi-tab trình duyệt (browser / 브라우저) và logout propagation** sang **17. Popup và nested WFrame khi auth trạng thái (state / 상태) đổi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. App shell phải sở hữu auth coordination

Trong WebSquare SPA, shell thường là nơi hợp lý để sở hữu:

```text
auth state
principal summary
permission snapshot
session-expiry dialog
reauth flow
logout flow
cross-screen notification
```

Child screen không nên tự redirect trình duyệt (browser / 브라우저) hoặc destroy shell theo cách riêng.

Điều này nối trực tiếp với [14 — Application Shell](14_application_shell_navigation_state.md).

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **17. Popup và nested WFrame khi auth trạng thái (state / 상태) đổi** nối từ **16. App shell phải sở hữu auth coordination** sang **18. Hybrid/WebView authentication**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Popup và nested WFrame khi auth trạng thái (state / 상태) đổi

Nếu session expire khi popup đang mở:

```text
popup owner
→ auth coordinator
→ popup command blocked
→ reauth
→ owner quyết định reload/close/resume
```

Không nên để popup tự login rồi parent vẫn ở auth trạng thái (state / 상태) cũ.

Bảo mật (security / 보안) trạng thái (state / 상태) là cross-screen concern, nhưng UI working trạng thái (state / 상태) vẫn có đơn vị sở hữu (owner / 오너) riêng.

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **18. Hybrid/WebView authentication** nối từ **17. Popup và nested WFrame khi auth trạng thái (state / 상태) đổi** sang **19. Deep link vào protected screen**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Hybrid/WebView authentication

Hybrid app tạo thêm ít nhất ba bảo mật (security / 보안) trạng thái (state / 상태):

```text
native app auth state
WebView/browser auth state
backend session/token state
```

Chúng có thể lệch nhau sau background/resume, app upgrade hoặc deep link.

Không truyền long-lived secret qua cầu nối (bridge / 브리지) message nếu không cần. bản địa (native / 네이티브) secure lưu trữ (storage / 저장소), WebView cookie store và backend đơn vị từ (token / 토큰)/session chính sách (policy / 정책) phải có quyền sở hữu (ownership / 소유권) rõ.

Chapter [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md) giải thích cầu nối (bridge / 브리지) vòng đời (lifecycle / 생명주기); chapter này bổ sung auth reconciliation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **19. Deep link vào protected screen** nối từ **18. Hybrid/WebView authentication** sang **20. Step-up authentication**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Deep link vào protected screen

Deep link không được bypass shell bảo mật (security / 보안) luồng (flow / 흐름).

```text
deep link received
→ parse route
→ auth readiness
→ permission check
→ load screen
→ load business data
```

Nếu chưa authenticated, giữ **điều hướng (navigation / 내비게이션) intent** chứ không nhất thiết giữ toàn bộ screen instance.

Sau re-auth, shell có thể resume intent nếu chính sách (policy / 정책) cho phép.

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **20. Step-up authentication** nối từ **19. Deep link vào protected screen** sang **21. Logout là destructive vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Step-up authentication

Một số thao tác (operation / 연산) nhạy cảm như transfer, approve, export PII có thể yêu cầu authentication mạnh hơn session thông thường.

Frontend nên mô hình (model / 모델) step-up như chuyển tiếp trạng thái (state transition / 상태 전이):

```text
ACTIVE
→ STEP_UP_REQUIRED
→ STEP_UP_IN_PROGRESS
→ ACTIVE_WITH_ASSURANCE
→ execute command
```

Không hard-code “nếu amount > X thì mở OTP popup” rải rác trong screen. quy tắc (rule / 규칙) trigger nên đến từ lĩnh vực (domain / 도메인)/bảo mật (security / 보안) đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **20. Step-up authentication** đặt đầu vào cho **21. Logout là destructive vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트)**, rồi **22. định danh (identity / 식별자) switch là trường hợp (case / 사례) nguy hiểm** mở rộng hệ quả hoặc giới hạn liên quan.

## 21. Logout là destructive vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트)

Logout không chỉ là gọi endpoint rồi redirect.

Cần xác định:

```text
pending Submission xử lý thế nào?
unsaved DataList có xóa không?
file upload staging có cleanup không?
native bridge operation có cancel không?
local/session storage nào cần clear?
app shell cache nào cần reset?
telemetry context nào phải rotate?
```

Sau logout, đối tượng (object / 객체) cũ không được vô tình dùng lại dưới định danh (identity / 식별자) mới.

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, sau khi thấy quy trình trong **21. Logout là destructive vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트)**, **22. định danh (identity / 식별자) switch là trường hợp (case / 사례) nguy hiểm** đặt nó vào một trường hợp đủ cụ thể để nhận ra điều kiện thành công và chỗ dễ sai. Từ đây, **23. lỗi (error / 오류) taxonomy cho auth vòng đời (lifecycle / 생명주기)** mở rộng hệ quả hoặc giới hạn liên quan.

## 22. định danh (identity / 식별자) switch là trường hợp (case / 사례) nguy hiểm

Máy dùng chung có thể logout người dùng (user / 사용자) A rồi login người dùng (user / 사용자) B trong cùng trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임).

Nếu toàn cục (global / 전역) DataMap/bộ nhớ đệm (cache / 캐시) giữ dữ liệu A, người dùng (user / 사용자) B có thể nhìn thấy stale sensitive dữ liệu (data / 데이터).

Bất biến (invariant / 불변식) quan trọng:

```text
principal change
→ invalidate principal-scoped client state
```

Đây là bảo mật (security / 보안) reason để tránh toàn cục (global / 전역) mutable bộ nhớ đệm (cache / 캐시) không có đơn vị sở hữu (owner / 오너).

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **22. định danh (identity / 식별자) switch là trường hợp (case / 사례) nguy hiểm** nêu quy tắc; **23. lỗi (error / 오류) taxonomy cho auth vòng đời (lifecycle / 생명주기)** thử quy tắc trong tình huống, rồi **24. khả năng quan sát (observability / 관측 가능성) không được log credential** mở rộng hệ quả.

## 23. lỗi (error / 오류) taxonomy cho auth vòng đời (lifecycle / 생명주기)

Nên phân biệt ít nhất:

```text
AUTH_REQUIRED
SESSION_EXPIRED
TOKEN_INVALID
FORBIDDEN
STEP_UP_REQUIRED
ACCOUNT_LOCKED
AUTH_SERVICE_UNAVAILABLE
CSRF_REJECTED
```

Người dùng (user / 사용자) message có thể đơn giản hơn, nhưng telemetry và orchestration cần category đủ chính xác.

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **23. lỗi (error / 오류) taxonomy cho auth vòng đời (lifecycle / 생명주기)** đặt đầu vào cho **24. khả năng quan sát (observability / 관측 가능성) không được log credential**, rồi **25. Testing ma trận (matrix / 행렬)** mở rộng hệ quả hoặc giới hạn liên quan.

## 24. khả năng quan sát (observability / 관측 가능성) không được log credential

Correlation ID, principal surrogate ID và permission quyết định (decision / 결정) có thể hữu ích, nhưng password, raw đơn vị từ (token / 토큰), session cookie, OTP và secret không được log.

PII cũng phải được mask theo chính sách (policy / 정책).

Chapter [19 — Observability](19_observability_incident_response.md) phải được áp dụng cùng bảo mật (security / 보안) classification.

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **25. Testing ma trận (matrix / 행렬)** nối từ **24. khả năng quan sát (observability / 관측 가능성) không được log credential** sang **26. dạng thất bại (failure mode / 실패 모드): redirect vòng lặp (loop / 루프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Testing ma trận (matrix / 행렬)

Auth regression suite nên có:

```text
session expire khi idle
session expire trong Search
session expire trong Save
reauth thành công
reauth fail
403 sau permission revoke
logout ở tab khác
principal A → logout → principal B
protected deep link khi chưa login
step-up success/failure
hybrid background → session expire → resume
```

Với Save, phải kiểm thử (test / 테스트) cả trường hợp (case / 사례) máy chủ (server / 서버) đã lần ghi nhận (commit / 커밋) nhưng máy khách (client / 클라이언트) nhận auth/mạng (network / 네트워크) thất bại (failure / 실패) để kiểm chứng idempotency/reconciliation.

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **26. dạng thất bại (failure mode / 실패 모드): redirect vòng lặp (loop / 루프)** nối từ **25. Testing ma trận (matrix / 행렬)** sang **27. dạng thất bại (failure mode / 실패 모드): 20 popup login cùng lúc**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. dạng thất bại (failure mode / 실패 모드): redirect vòng lặp (loop / 루프)

Luồng (flow / 흐름):

```text
app → auth redirect → app
app chưa nhận diện auth-ready
→ auth redirect lần nữa
```

Nguyên nhân gốc (root cause / 근본 원인) thường là readiness hoặc callback trạng thái (state / 상태) bị nhầm, không phải “SSO chậm”.

Log cần có điều hướng (navigation / 내비게이션) intent, auth chuyển tiếp (transition / 전이) và correlation ID.

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **27. dạng thất bại (failure mode / 실패 모드): 20 popup login cùng lúc** nối từ **26. dạng thất bại (failure mode / 실패 모드): redirect vòng lặp (loop / 루프)** sang **28. dạng thất bại (failure mode / 실패 모드): người dùng (user / 사용자) B thấy dữ liệu người dùng (user / 사용자) A**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. dạng thất bại (failure mode / 실패 모드): 20 popup login cùng lúc

Nhiều Submission thất bại (fail / 실패) đồng thời và mỗi handler tự mở login.

Fix bằng single-flight reauthentication coordinator:

```text
first auth failure → start reauth
other failures → join/wait
reauth success/fail → broadcast one result
```

Đây là tính đồng thời (concurrency / 동시성) bài toán (problem / 문제) ở máy khách (client / 클라이언트) kiến trúc (architecture / 아키텍처).

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **27. dạng thất bại (failure mode / 실패 모드): 20 popup login cùng lúc** đặt vấn đề; **28. dạng thất bại (failure mode / 실패 모드): người dùng (user / 사용자) B thấy dữ liệu người dùng (user / 사용자) A** đối chiếu bằng chứng, rồi **29. dạng thất bại (failure mode / 실패 모드): Save tự chạy lại sau login và tạo duplicate** mở rộng hệ quả hoặc giới hạn liên quan.

## 28. dạng thất bại (failure mode / 실패 모드): người dùng (user / 사용자) B thấy dữ liệu người dùng (user / 사용자) A

Nguyên nhân có thể là shell bộ nhớ đệm (cache / 캐시)/DataList toàn cục (global / 전역) không clear khi principal thay đổi (change / 변경).

Fix không phải chỉ refresh Grid; phải xác định toàn bộ trạng thái (state / 상태) có phạm vi (scope / 범위) theo principal và invalidate đúng ranh giới (boundary / 경계).

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **28. dạng thất bại (failure mode / 실패 모드): người dùng (user / 사용자) B thấy dữ liệu người dùng (user / 사용자) A** đặt vấn đề; **29. dạng thất bại (failure mode / 실패 모드): Save tự chạy lại sau login và tạo duplicate** đối chiếu bằng chứng, rồi **30. Master checklist** mở rộng hệ quả hoặc giới hạn liên quan.

## 29. dạng thất bại (failure mode / 실패 모드): Save tự chạy lại sau login và tạo duplicate

Nguyên nhân gốc (root cause / 근본 원인) là frontend coi auth khôi phục (recovery / 복구) như thử lại (retry / 재시도) vận chuyển (transport / 전송) thông thường.

Fix bằng thao tác (operation / 연산) classification + idempotency đặc tả hợp đồng (contract / 계약) + tường minh (explicit / 명시적) người dùng (user / 사용자) reconciliation cho mutating yêu cầu (request / 요청) không chắc kết quả.

> **Nối mạch:** Ở chặng này của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **30. Master checklist** nối từ **29. dạng thất bại (failure mode / 실패 모드): Save tự chạy lại sau login và tạo duplicate** sang **31. liên kết (connection / 연결) map**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Master checklist

Trước khi coi auth tích hợp (integration / 통합) là production-ready, phải trả lời được:

```text
Ai sở hữu auth state trong SPA?
Server session/token lifetime bao lâu?
Client nhận diện expiration bằng contract nào?
401/403/business error được phân loại ở đâu?
Reauth có single-flight không?
Mutating request có auto-retry không, vì sao?
Unsaved state xử lý thế nào khi expire?
Principal switch invalidates state nào?
Permission UI có được coi là authorization không?
Deep link đi qua auth readiness chưa?
Hybrid native/WebView auth reconcile thế nào?
Log có vô tình chứa credential/PII không?
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, sau nội dung của **30. Master checklist**, **31. liên kết (connection / 연결) map** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **32. Kết luận** mở rộng hệ quả hoặc giới hạn liên quan.

## 31. liên kết (connection / 연결) map

Submission vòng đời (lifecycle / 생명주기) và lỗi (error / 오류) classification: [03 — DataCollection & Submission](03_data_collection_submission.md).

Bảo mật (security / 보안) trust ranh giới (boundary / 경계): [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md).

Testing: [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md).

Ứng dụng (application / 애플리케이션) shell: [14 — Application Shell, Navigation & Multi-Screen State](14_application_shell_navigation_state.md).

Idempotency/tính đồng thời (concurrency / 동시성): [15 — Backend Contract, Transaction & Concurrency](15_backend_contract_transaction_concurrency.md).

Hybrid auth: [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md).

Sự cố (incident / 인시던트) bằng chứng (evidence / 증거): [19 — Observability, Logging & Incident Response](19_observability_incident_response.md).

> **Nối mạch:** Trong **20 — Authentication, Session, SSO & bảo mật (security / 보안) vòng đời (lifecycle / 생명주기)**, **32. Kết luận** tổng hợp từ **31. liên kết (connection / 연결) map** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 32. Kết luận

Bảo mật (security / 보안) vòng đời (lifecycle / 생명주기) trong WebSquare không phải là “có login page”. Nó là bài toán đồng bộ nhiều thời gian tồn tại (lifetime / 수명) và trust ranh giới (boundary / 경계):

```text
Principal
→ Authentication
→ Session
→ Permission snapshot
→ Screen capability
→ Submission
→ Server authorization
→ Result
→ Security-state reconciliation
```

Master-level nhà phát triển (developer / 개발자) không tin máy khách (client / 클라이언트) trạng thái (state / 상태) chỉ vì UI đang hiển thị hợp lệ. Họ luôn hỏi **bảo mật (security / 보안) truth nằm ở đâu, trạng thái (state / 상태) có thể stale khi nào, thao tác (operation / 연산) có thể được thử lại (retry / 재시도) an toàn không, principal thay đổi (change / 변경) invalidates những gì và bằng chứng (evidence / 증거) nào chứng minh bảo mật (security / 보안) chuyển tiếp (transition / 전이) đã xảy ra đúng**.

> **Bàn giao:** Sau **32. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
