# Nền tảng Web (web platform / 웹 플랫폼): mô hình (model / 모델), boundaries và bất biến (invariant / 불변식)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Nền tảng Web (web platform / 웹 플랫폼): mô hình (model / 모델), boundaries và bất biến (invariant / 불변식)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ tài nguyên (resource / 자원) đến hành vi (behavior / 동작)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Ba lớp cần tách** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của web platform core, rồi nối runtime, rendering, events, framework và performance thành một mô hình thống nhất.

Nền tảng Web (web platform / 웹 플랫폼) không chỉ là tập API của trình duyệt (browser / 브라우저). Nó là hợp đồng giữa tài nguyên (resource / 자원)
được tải, parser tạo ra cây (tree / 트리), thời gian chạy (runtime / 런타임) thực thi script, renderer tạo ra pixels,
đầu vào (input / 입력) tạo ra events và bảo mật (security / 보안) mô hình (model / 모델) giới hạn dữ liệu nào được phép đi qua
ranh giới (boundary / 경계) nào.

## Từ tài nguyên (resource / 자원) đến hành vi (behavior / 동작)

Một màn hình thật thường có chuỗi nhân quả (causal / 인과적) như sau:

```text
URL/navigation
→ response và resource graph
→ HTML/CSS parse
→ DOM/CSSOM + style state
→ layout/paint/composite
→ input/event
→ JavaScript và async work
→ state/data update
→ render invalidation
```

Đây là đồ thị (graph / 그래프) có thể quay lại, không phải danh sách bước tuyến tính. Font tải (load / 로드),
resize, biểu định kiểu (stylesheet / 스타일시트) mới, mạng (network / 네트워크) phản hồi (response / 응답) hoặc trạng thái (state / 상태) cập nhật (update / 업데이트) có thể invalid một
phần cây (tree / 트리) và kích hoạt lại công việc (work / 작업). Vì vậy câu hỏi gỡ lỗi (debug / 디버그) tốt là “ranh giới (boundary / 경계) nào
đổi trạng thái (state / 상태) và bằng chứng (evidence / 증거) nào chứng minh nó?” thay vì chỉ hỏi “thành phần (component / 컴포넌트) nào lỗi?”.

> **Chuyển mạch:** Trong **Nền tảng Web (web platform / 웹 플랫폼): mô hình (model / 모델), boundaries và bất biến (invariant / 불변식)**, **Từ tài nguyên (resource / 자원) đến hành vi (behavior / 동작)** nêu điều cần giải thích; **Ba lớp cần tách** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Bất biến (invariant / 불변식) cấp lĩnh vực (domain / 도메인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ba lớp cần tách

**thành phần nguyên thủy (primitive / 기본 요소) của nền tảng (platform / 플랫폼)** gồm HTML ngữ nghĩa (semantics / 의미론), DOM định danh (identity / 식별자), CSS cascade,
sự kiện (event / 이벤트) dispatch, URL/fetch, lưu trữ (storage / 저장소), timers, cây khả năng tiếp cận (accessibility tree / 접근성 트리) và origin
chính sách (policy / 정책). **ngữ nghĩa khung phần mềm (framework semantics / 프레임워크 의미론)** thêm thành phần (component / 컴포넌트)/page định danh (identity / 식별자), vòng đời (lifecycle / 생명주기),
subscription, scheduling và rendering lớp trừu tượng (abstraction / 추상화). **đặc tả ứng dụng (application contract / 애플리케이션 계약)**
định nghĩa nghiệp vụ (business / 비즈니스) trạng thái (state / 상태), máy chủ (server / 서버) authorization, lỗi (error / 오류) meaning và bản phát hành (release / 릴리스)
sản phẩm tạo ra (artifact / 산출물). Một khung phần mềm (framework / 프레임워크) không thể biến dữ liệu không đáng tin thành trusted dữ liệu (data / 데이터)
chỉ bằng kiểu (type / 타입) hoặc thành phần (component / 컴포넌트) ranh giới (boundary / 경계).

> **Chuyển mạch:** Ba lớp tách host, browser và application responsibilities. **Domain invariant** dùng boundary đó để xác định điều ứng dụng phải giữ dù rendering, network hay framework thay đổi.

## Bất biến (invariant / 불변식) cấp lĩnh vực (domain / 도메인)

- Mỗi tài nguyên (resource / 자원), yêu cầu (request / 요청), DOM nút (node / 노드), thành phần (component / 컴포넌트)/page instance và async thao tác (operation / 연산)
  có định danh (identity / 식별자) và thời gian tồn tại (lifetime / 수명) rõ ràng.
- trạng thái (state / 상태) có một nguồn chuẩn (source of truth / 정본); derived view, bộ nhớ đệm (cache / 캐시) và optimistic projection
  không được âm thầm trở thành chuẩn gốc (canonical / 정본) trạng thái (state / 상태).
- Kết quả cũ không được ghi đè intent mới; cancellation hoặc generation check
  phải bảo vệ stale phản hồi (response / 응답).
- ngữ nghĩa (semantics / 의미론), keyboard/focus và accessible name là hành vi (behavior / 동작) công khai, không
  phải polish chỉ kiểm tra khi gần bản phát hành (release / 릴리스).
- Dữ liệu từ URL, DOM, lưu trữ (storage / 저장소), message, iframe, WebView cầu nối (bridge / 브리지) và backend đều
  phải có trust ranh giới (boundary / 경계) trước khi đi vào sink hoặc side tác động (effect / 효과).
- hiệu năng (performance / 성능) claim phải có dấu vết (trace / 추적)/chỉ số (metric / 지표)/profile; không suy ra từ một CSS
  thuộc tính (property / 속성) hoặc cảm giác “nhanh hơn”.

Các chapter tiếp theo triển khai những bất biến (invariant / 불변식) này ở thời gian chạy (runtime / 런타임), renderer,
tương tác (interaction / 상호작용)/mạng (network / 네트워크) và môi trường vận hành (production / 운영 환경) các ràng buộc (constraints / 제약조건들).

> **Bàn giao:** Sau **Bất biến (invariant / 불변식) cấp lĩnh vực (domain / 도메인)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
