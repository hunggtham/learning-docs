# Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Origin là ranh giới (boundary / 경계) cơ bản** làm rõ cặp khái niệm dễ lẫn và giới hạn của cách giải thích; sau đó sang **CORS** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Trình duyệt (browser / 브라우저) chạy mã (code / 코드) từ nhiều origins trên cùng máy và cùng lúc giữ cookies, credentials, camera/microphone permissions. bảo mật (security / 보안) mô hình (model / 모델) của web vì thế xoay quanh việc ngăn một origin tùy ý đọc/điều khiển authority của origin khác.

## Origin là ranh giới (boundary / 경계) cơ bản

Origin thường được xác định bởi scheme, host và cổng (port / 포트). **Same-Origin chính sách (policy / 정책) (SOP)** hạn chế script từ origin A đọc phản hồi (response / 응답)/trạng thái (state / 상태) nhạy cảm của origin B.

SOP không ngăn mọi cross-origin yêu cầu (request / 요청); nhiều yêu cầu (request / 요청) vẫn có thể được gửi. Điều quan trọng thường là quyền đọc phản hồi (response / 응답) và truy cập (access / 접근) DOM/trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust**, **Origin là ranh giới (boundary / 경계) cơ bản** đã nêu tiêu chí phân biệt, còn **CORS** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **CSRF và SameSite** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CORS

**CORS** là giao thức (protocol / 프로토콜) để máy chủ (server / 서버) nói trình duyệt (browser / 브라우저) rằng origin nào được phép đọc cross-origin phản hồi (response / 응답). Nó không phải authentication và không ngăn non-browser máy khách (client / 클라이언트) gọi API.

Cấu hình `Access-Control-Allow-Origin: *` có thể hợp lệ cho công khai (public / 공개) tài nguyên (resource / 자원) nhưng nguy hiểm nếu nhà phát triển (developer / 개발자) tưởng nó thay thế authorization.

> **Chuyển mạch:** Ở chặng này của **Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust**, **CSRF và SameSite** tiếp nhận điểm tựa từ **CORS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **XSS và CSP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSRF và SameSite

Cookie có thể được trình duyệt (browser / 브라우저) tự động gửi kèm yêu cầu (request / 요청), tạo nguy cơ Cross-Site yêu cầu (request / 요청) Forgery nếu attacker khiến trình duyệt (browser / 브라우저) người dùng (user / 사용자) gửi state-changing yêu cầu (request / 요청) tới site đang login.

`SameSite` cookie giảm một số cross-site sending contexts. CSRF đơn vị từ (token / 토큰) vẫn hữu ích trong kiến trúc (architecture / 아키텍처) cần bảo vệ các luồng (flow / 흐름) không được SameSite cover đầy đủ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust**, **XSS và CSP** tiếp nhận điểm tựa từ **CSRF và SameSite** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **iframe và embedding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## XSS và CSP

Cross-Site Scripting cho attacker chạy script trong origin của ứng dụng (application / 애플리케이션), nghĩa script thừa hưởng quyền origin đó. đầu ra (output / 출력) encoding, safe DOM APIs và khung phần mềm (framework / 프레임워크) escaping là primary defense.

**Content bảo mật (security / 보안) chính sách (policy / 정책) (CSP)** giới hạn nguồn script/tài nguyên (resource / 자원) và có thể giảm impact khi injection xảy ra. CSP tốt là defense-in-depth, không thay thế fix XSS.

> **Chuyển mạch:** Trong **Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust**, **iframe và embedding** tiếp nhận điểm tựa từ **XSS và CSP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lưu trữ trình duyệt (browser storage / 브라우저 저장소)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## iframe và embedding

Iframe tạo browsing ngữ cảnh (context / 맥락) riêng nhưng parent/child communication qua `postMessage` cần validate `origin` và message lược đồ (schema / 스키마). Dùng wildcard mục tiêu (target / 대상) origin hoặc tin mọi incoming message làm ranh giới (boundary / 경계) yếu đi.

Frame-ancestors/CSP hoặc X-Frame-Options giúp chống clickjacking bằng cách kiểm soát ai được embed page.

> **Chuyển mạch:** Ở chặng này của **Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust**, **Lưu trữ trình duyệt (browser storage / 브라우저 저장소)** tiếp nhận điểm tựa từ **iframe và embedding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Site isolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lưu trữ trình duyệt (browser storage / 브라우저 저장소)

LocalStorage dễ dùng nhưng script cùng origin có thể đọc, nên XSS có thể lấy bearer đơn vị từ (token / 토큰) lưu ở đó. HttpOnly cookie không cho JavaScript đọc trực tiếp nhưng vẫn cần CSRF lập luận (reasoning / 추론).

Không có lưu trữ (storage / 저장소) choice “an toàn tuyệt đối”; threat mô hình (model / 모델) quyết định sự đánh đổi (trade-off / 트레이드오프) giữa XSS exposure, CSRF và UX/session kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust**, **Site isolation** tiếp nhận điểm tựa từ **Lưu trữ trình duyệt (browser storage / 브라우저 저장소)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Site isolation

Hiện đại (modern / 현대적) browsers còn dùng tiến trình (process / 프로세스) isolation để tách sites/origins ở OS tiến trình (process / 프로세스) mức (level / 수준), giảm blast radius của renderer compromise và side-channel classes. Đây là ví dụ ranh giới bảo mật (security boundary / 보안 경계) được reinforce qua nhiều layers: web chính sách (policy / 정책) + tiến trình (process / 프로세스) sandbox + hardware mitigations.

> **Chuyển mạch:** Trong **Trình duyệt (browser / 브라우저) isolation, CSP, SameSite và cross-origin trust**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Site isolation** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Web bảo mật (security / 보안) là quản lý authority giữa origins. SOP đặt default ranh giới (boundary / 경계); CORS mở quyền đọc có kiểm soát; SameSite/CSRF bảo vệ ambient credentials; CSP giảm script authority khi injection xảy ra. Mỗi cơ chế (mechanism / 메커니즘) xử lý threat khác nhau.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
