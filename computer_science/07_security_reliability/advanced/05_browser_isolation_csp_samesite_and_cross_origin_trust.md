# Browser isolation, CSP, SameSite và cross-origin trust

Browser chạy code từ nhiều origins trên cùng máy và cùng lúc giữ cookies, credentials, camera/microphone permissions. Security model của web vì thế xoay quanh việc ngăn một origin tùy ý đọc/điều khiển authority của origin khác.

## Origin là boundary cơ bản

Origin thường được xác định bởi scheme, host và port. **Same-Origin Policy (SOP)** hạn chế script từ origin A đọc response/state nhạy cảm của origin B.

SOP không ngăn mọi cross-origin request; nhiều request vẫn có thể được gửi. Điều quan trọng thường là quyền đọc response và access DOM/state.

## CORS

**CORS** là protocol để server nói browser rằng origin nào được phép đọc cross-origin response. Nó không phải authentication và không ngăn non-browser client gọi API.

Cấu hình `Access-Control-Allow-Origin: *` có thể hợp lệ cho public resource nhưng nguy hiểm nếu developer tưởng nó thay thế authorization.

## CSRF và SameSite

Cookie có thể được browser tự động gửi kèm request, tạo nguy cơ Cross-Site Request Forgery nếu attacker khiến browser user gửi state-changing request tới site đang login.

`SameSite` cookie giảm một số cross-site sending contexts. CSRF token vẫn hữu ích trong architecture cần bảo vệ các flow không được SameSite cover đầy đủ.

## XSS và CSP

Cross-Site Scripting cho attacker chạy script trong origin của application, nghĩa script thừa hưởng quyền origin đó. Output encoding, safe DOM APIs và framework escaping là primary defense.

**Content Security Policy (CSP)** giới hạn nguồn script/resource và có thể giảm impact khi injection xảy ra. CSP tốt là defense-in-depth, không thay thế fix XSS.

## iframe và embedding

Iframe tạo browsing context riêng nhưng parent/child communication qua `postMessage` cần validate `origin` và message schema. Dùng wildcard target origin hoặc tin mọi incoming message làm boundary yếu đi.

Frame-ancestors/CSP hoặc X-Frame-Options giúp chống clickjacking bằng cách kiểm soát ai được embed page.

## Browser storage

LocalStorage dễ dùng nhưng script cùng origin có thể đọc, nên XSS có thể lấy bearer token lưu ở đó. HttpOnly cookie không cho JavaScript đọc trực tiếp nhưng vẫn cần CSRF reasoning.

Không có storage choice “an toàn tuyệt đối”; threat model quyết định trade-off giữa XSS exposure, CSRF và UX/session architecture.

## Site isolation

Modern browsers còn dùng process isolation để tách sites/origins ở OS process level, giảm blast radius của renderer compromise và side-channel classes. Đây là ví dụ security boundary được reinforce qua nhiều layers: web policy + process sandbox + hardware mitigations.

## Mental Model

> Web security là quản lý authority giữa origins. SOP đặt default boundary; CORS mở quyền đọc có kiểm soát; SameSite/CSRF bảo vệ ambient credentials; CSP giảm script authority khi injection xảy ra. Mỗi mechanism xử lý threat khác nhau.