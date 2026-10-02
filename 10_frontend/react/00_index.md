# React Master ghi chú (note / 노트) — chỉ mục (index / 인덱스)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **React Master ghi chú (note / 노트) — chỉ mục (index / 인덱스)**. Route đi từ baseline/version scope → JavaScript prerequisites → Beginner, Intermediate, Advanced và Legacy tracks → migration, references và cross-links, để chỉ mục điều phối một lộ trình React xuyên phiên bản.

Baseline của bộ tài liệu: React 19.3 (stable ngày 09/09/2026). Cách viết mặc định là hàm (function / 함수) thành phần (component / 컴포넌트) + Hooks; lớp (class / 클래스) thành phần (component / 컴포넌트) được giữ lại để đọc và migrate mã (code / 코드) cũ thay vì bị xóa khỏi lộ trình.

React không đứng một mình. Nếu chưa chắc về closure, đối tượng (object / 객체) định danh (identity / 식별자), Promise/vòng lặp sự kiện (event loop / 이벤트 루프), mô-đun (module / 모듈) hoặc trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임), nên học [JavaScript Beginner](../javascript/javascript_beginner_rebuilt.md) và [JavaScript Intermediate](../javascript/javascript_intermediate.md) trước hoặc song song. Nếu dự án (project / 프로젝트) dùng TypeScript, học hệ kiểu (type system / 타입 시스템) ở [TypeScript canonical track](../javascript/typescript_00_index.md). React docs chỉ giải thích kiểu (type / 타입) ở nơi kiểu (type / 타입) làm thay đổi thành phần (component / 컴포넌트)/API lập luận (reasoning / 추론); structural typing, narrowing, generic, declaration, mô-đun (module / 모듈) resolution và thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증) được giữ ở TypeScript chuẩn gốc (canonical / 정본) nguồn (source / 소스) để tránh duplicate.

## Thứ tự học chuẩn gốc (canonical / 정본)

1. [01 — React Beginner](01_react_beginner.md) — nền tảng, JSX, thành phần (component / 컴포넌트), props, sự kiện (event / 이벤트), trạng thái (state / 상태), kết xuất (render / 렌더링), form, danh sách (list / 목록), composition, styling và mô hình tư duy (mental model / 사고 모델) cơ bản.
2. [02 — React Intermediate](02_react_intermediate.md) — tác động (effect / 효과), ref, reducer, ngữ cảnh (context / 맥락), custom Hook, memoization, portal, Suspense, dữ liệu (data / 데이터) fetching, routing, form môi trường vận hành (production / 운영 환경), khả năng tiếp cận (accessibility / 접근성) và testing.
3. [03 — React Advanced / Senior](03_react_advanced_senior.md) — tính đồng thời (concurrency / 동시성), Actions, `use`, optimistic UI, `useEffectEvent`, Activity, View Transitions, Fragment refs, bên ngoài (external / 외부) store, SSR, hydration, RSC, hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처) môi trường vận hành (production / 운영 환경).
4. [04 — React Master](04_react_master.md) — React trình biên dịch (compiler / 컴파일러) 1.0, máy chủ (server / 서버) kiến trúc (architecture / 아키텍처), bộ nhớ đệm (cache / 캐시)/bảo mật (security / 보안), large-scale trạng thái (state / 상태), thiết kế (design / 설계) hệ thống (system / 시스템), thư viện (library / 라이브러리) authoring, di chuyển (migration / 마이그레이션), khả năng quan sát (observability / 관측 가능성), hiệu năng (performance / 성능) ngân sách (budget / 예산) và Master/cấp cao (senior / 시니어) idioms.
5. [05 — React Legacy API Reference](05_react_legacy_api_reference.md) — tham chiếu (reference / 참조) riêng cho React 15–18 và các API/mẫu (pattern / 패턴) cũ, dùng khi đọc hoặc migrate dự án (project / 프로젝트) enterprise.

Luồng lập luận (reasoning / 추론) nên đi theo **kết xuất (render / 렌더링) cây (tree / 트리) → props/trạng thái (state / 상태)/ngữ cảnh (context / 맥락) → trạng thái (state / 상태) snapshot/cập nhật (update / 업데이트) hàng đợi (queue / 큐) → reconciliation/định danh (identity / 식별자)/key → lần ghi nhận (commit / 커밋) → sự kiện (event / 이벤트)/tác động (effect / 효과) → tính đồng thời (concurrency / 동시성)/Suspense → máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계) → bằng chứng vận hành (production evidence / 운영 증거)**. Hooks không được học như một danh sách API trước khi hiểu rendering và quyền sở hữu trạng thái (state ownership / 상태 소유권).

> **Chuyển mạch:** Thứ tự canonical trước hết xác định prerequisite; phạm vi phiên bản sau đó giải thích vì sao phải đọc cả legacy và modern React. Cách đọc notes tiếp theo dùng distinction này để chọn đúng file và mốc API.

## Phạm vi phiên bản (version / 버전): học cả React cũ lẫn React hiện đại

Bộ tài liệu này không được tổ chức theo kiểu “chỉ học React 19.3 rồi ghi vài chú thích React 18”. React 19.3 vẫn là mốc hiện hành để biết cách viết mã (code / 코드) mới, nhưng các API cũ từ thời React 15, React 16 và React 17 được giữ lại ở đúng phần kiến thức tương ứng để người đọc có thể hiểu codebase legacy.

Khi một API đã lỗi thời, tài liệu vẫn giải thích cú pháp và cách hoạt động của nó nếu API đó đủ phổ biến để còn xuất hiện trong dự án (project / 프로젝트) thực tế. Sau phần giải thích sẽ có trạng thái như `Legacy`, `Deprecated` hoặc `Removed`, phiên bản (version / 버전) liên quan và cách chuyển sang API hiện đại. Cách trình bày này có chủ đích: học React theo một mô hình tư duy (mental model / 사고 모델) liên tục, nhưng vẫn đọc được mã (code / 코드) được viết ở nhiều thế hệ.

### Bản đồ lịch sử React nên nhớ
Phần này nối mạch bài học với “Bản đồ lịch sử React nên nhớ”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

| Thời kỳ | Những thứ thường gặp trong mã (code / 코드) |
|---|---|
| React 0.x–14 | `React.createClass`, mixins, JSX transform cũ, string refs và nhiều API đời đầu. Đây chủ yếu là kiến thức đọc legacy. |
| React 15.x | lớp (class / 클래스) thành phần (component / 컴포넌트) đã phổ biến; `React.createClass` và `React.PropTypes` còn xuất hiện nhiều. React 15.5 tách `createClass` và `PropTypes` ra gói (package / 패키지) riêng và bắt đầu deprecate cách cũ. |
| React 16.0–16.2 | Fiber trở thành renderer mới; lỗi (error / 오류) Boundaries, portals và Fragment làm thành phần (component / 컴포넌트) composition linh hoạt hơn. |
| React 16.3–16.6 | New ngữ cảnh (context / 맥락) API, `createRef`, `forwardRef`, `StrictMode`, `memo`, `lazy`, Suspense cho mã (code / 코드) splitting, `contextType` và vòng đời (lifecycle / 생명주기) mới xuất hiện. |
| React 16.8–16.14 | Hooks xuất hiện từ 16.8 và dần trở thành cách viết chính. Các vòng đời (lifecycle / 생명주기) nguy hiểm được đổi tên `UNSAFE_*`; nhiều API legacy bắt đầu rời khỏi hướng học mới. |
| React 17 | bản phát hành (release / 릴리스) chuyển tiếp. hiện đại (modern / 현대적) JSX transform và gradual upgrade là các điểm quan trọng; sự kiện (event / 이벤트) hệ thống (system / 시스템) cũng thay đổi so với các phiên bản (version / 버전) trước. |
| React 18 | `createRoot`, automatic batching, concurrent foundations, transitions, `useDeferredValue`, `useId`, `useSyncExternalStore`, `useInsertionEffect`, streaming SSR. |
| React 19.x | Actions, `use`, `useActionState`, `useOptimistic`, ref-as-prop, ngữ cảnh (context / 맥락) provider shorthand, RSC/máy chủ (server / 서버) improvements và tiếp tục loại bỏ API legacy; các minor 19.2/19.3 tiếp tục thêm công khai (public / 공개) năng lực (capability / 역량) nên phải kiểm tra minimum minor phiên bản (version / 버전). |

> **Chuyển mạch:** Khi đã phân biệt mốc legacy/modern, cách đọc notes chỉ rõ phần nào là concept, phần nào là API hoặc migration detail. Conceptual boundary tiếp theo ngăn React core lấn sang web platform, TypeScript hay framework owner khác.

## Cách đọc các phiên bản (version / 버전) ghi chú (note / 노트) trong bộ tài liệu

Bộ ghi chú (note / 노트) lấy **React 19.3** làm baseline hiện hành, nhưng không giả định rằng mọi dự án (project / 프로젝트) đều đang ở 19.3. Khi một kiến thức thay đổi đáng kể theo phiên bản (version / 버전), tài liệu chèn `Version Note` sau phần giải thích chính. Quy tắc đọc là: trước tiên hiểu mô hình tư duy (mental model / 사고 모델) và cách dùng hiện đại; sau đó mới đọc khác biệt phiên bản (version / 버전) để biết vì sao mã (code / 코드) cũ có cú pháp khác. Nhờ vậy lịch sử React không chen ngang luồng học.

Các mốc dưới đây đủ để đọc phần lớn mã (code / 코드) React hiện đại:

| phiên bản (version / 버전) | Ý nghĩa đối với người học |
|---|---|
| React 16.8 | Hooks như `useState`, `useEffect` xuất hiện. Đây là mốc quan trọng nhất khi đọc tutorial cũ vì mã (code / 코드) trước đó thường dựa nhiều vào lớp (class / 클래스) thành phần (component / 컴포넌트). |
| React 17 | Chủ yếu là bản phát hành (release / 릴리스) chuyển tiếp; giai đoạn này phổ biến hiện đại (modern / 현대적) JSX transform, nên dự án (project / 프로젝트) hiện đại không cần `import React` chỉ để dùng JSX. |
| React 18 | `createRoot`, automatic batching, tính đồng thời (concurrency / 동시성) primitives như `startTransition`/`useTransition`, `useDeferredValue`, `useId`, streaming SSR và Strict chế độ (mode / 모드) development checks mới trở thành nền tảng của React hiện đại. |
| React 18.3 | Bản cầu nối để nâng cấp lên React 19; hành vi gần React 18.2 nhưng thêm warning cho API/deprecation cần sửa trước React 19. |
| React 19.0 | Actions, `use`, `useActionState`, `useOptimistic`, form Actions, ref-as-prop, ngữ cảnh (context / 맥락) provider shorthand và nhiều thay đổi SSR/RSC. React 19 cũng yêu cầu hiện đại (modern / 현대적) JSX transform và loại bỏ một số API legacy đã deprecated từ trước. |
| React 19.1 | Chủ yếu tiếp tục cải thiện nhánh máy chủ (server / 서버)/RSC/prerender và sửa lỗi. Với lộ trình học, có thể xem đây là bước tiến hóa giữa 19.0 và 19.2 thay vì một mô hình tư duy (mental model / 사고 모델) mới cho beginner. |
| React 19.2 | Thêm `<Activity />`, `useEffectEvent`, `cacheSignal`, React hiệu năng (performance / 성능) Tracks và Partial Pre-rendering/máy chủ (server / 서버) improvements. |
| React 19.3 | Baseline của bộ ghi chú (note / 노트) này. `<ViewTransition>` và Fragment refs trở thành stable; React DOM thêm `browser()` và Trusted Types hỗ trợ (support / 지원); RSC cho phép kết xuất (render / 렌더링) ngữ cảnh (context / 맥락) trực tiếp trong máy chủ (server / 서버) Components theo ranh giới (boundary / 경계) phù hợp. |
| React trình biên dịch (compiler / 컴파일러) 1.0 | Stable từ năm 2025 và **có phiên bản (version / 버전) độc lập với React cốt lõi (core / 핵심)**. trình biên dịch (compiler / 컴파일러) tự động tối ưu nhiều trường hợp memoization, vì vậy không nên hiểu “React 19.3” đồng nghĩa “trình biên dịch (compiler / 컴파일러) 19.3”. |

Một nguyên tắc quan trọng là **major/minor của React không hoàn toàn thay thế patch phiên bản (version / 버전)**. Đặc biệt với React máy chủ (server / 서버) Components, bảo mật (security / 보안) fix từng được backport vào nhiều nhánh 19.0.x, 19.1.x và 19.2.x. Trong môi trường vận hành (production / 운영 환경) phải theo patch/bảo mật (security / 보안) advisory của khung phần mềm (framework / 프레임워크) và React, không chỉ nhìn “19.x”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — chỉ mục (index / 인덱스)**, **Cách đọc các phiên bản (version / 버전) ghi chú (note / 노트) trong bộ tài liệu** đã nêu tiêu chí phân biệt, còn **Conceptual ranh giới (boundary / 경계) với lĩnh vực (domain / 도메인) khác** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Coverage kiểm tra (audit / 감사) — 22/09/2026** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conceptual ranh giới (boundary / 경계) với lĩnh vực (domain / 도메인) khác

React chịu trách nhiệm chính cho thành phần (component / 컴포넌트)/rendering mô hình (model / 모델), trạng thái (state / 상태)/tác động (effect / 효과)/ref/ngữ cảnh (context / 맥락) và các React-specific tính đồng thời (concurrency / 동시성)/máy chủ (server / 서버) primitives. JavaScript chuẩn gốc (canonical / 정본) docs chịu trách nhiệm cho closure, promise, vòng lặp sự kiện (event loop / 이벤트 루프), prototype, đối tượng (object / 객체) định danh (identity / 식별자) và trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임). TypeScript chuẩn gốc (canonical / 정본) docs chịu trách nhiệm cho static kiểu (type / 타입) mô hình (model / 모델). CSS lĩnh vực (domain / 도메인) chịu trách nhiệm bố cục (layout / 레이아웃)/paint/styling mechanics. Khoa học máy tính (computer science / 컴퓨터 과학) và backend/máy chủ (server / 서버) docs chịu trách nhiệm cho scheduling tổng quát, mạng (network / 네트워크)/bộ nhớ đệm (cache / 캐시)/cơ sở dữ liệu (database / 데이터베이스)/bảo mật (security / 보안) principles ở mức không phụ thuộc React.

Khi một chapter React cần những kiến thức đó, tài liệu giải thích đủ để người đọc tiếp tục lập luận (reasoning / 추론) tại chỗ, nhưng không bản sao (copy / 복사) toàn bộ lĩnh vực (domain / 도메인) khác. Cách này giữ React là chuẩn gốc (canonical / 정본) nguồn (source / 소스) cho **React ngữ nghĩa (semantics / 의미론)**, còn cross-domain kiến thức (knowledge / 지식) được link về nơi sở hữu khái niệm.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — chỉ mục (index / 인덱스)**, **Conceptual ranh giới (boundary / 경계) với lĩnh vực (domain / 도메인) khác** đã nêu tiêu chí phân biệt, còn **Coverage kiểm tra (audit / 감사) — 22/09/2026** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Nguyên tắc học sau kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coverage kiểm tra (audit / 감사) — 22/09/2026

Chuẩn gốc (canonical / 정본) nhánh học (track / 트랙) hiện đã phủ bốn lớp liên tục. Beginner xây mô hình tư duy (mental model / 사고 모델) declarative rendering, trạng thái (state / 상태) snapshot, cập nhật (update / 업데이트) hàng đợi (queue / 큐), định danh (identity / 식별자)/key và immutable cập nhật (update / 업데이트). Intermediate đào sâu tác động (effect / 효과) như synchronization tiến trình (process / 프로세스), closure/phụ thuộc (dependency / 의존성), reducer/ngữ cảnh (context / 맥락)/custom Hook, refs, lỗi (error / 오류) ranh giới (boundary / 경계), Suspense cơ bản, server-state quyền sở hữu (ownership / 소유권), routing/form/testing. Advanced/cấp cao (senior / 시니어) nối các bất biến (invariant / 불변식) đó với concurrent rendering, Actions, bên ngoài (external / 외부) stores, SSR/hydration/RSC, bảo mật (security / 보안), khả năng tiếp cận (accessibility / 접근성) và bằng chứng hiệu năng (performance evidence / 성능 증거). Master chuyển sang trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계), máy chủ (server / 서버) kiến trúc (architecture / 아키텍처), thư viện (library / 라이브러리)/design-system authoring, large-scale di chuyển (migration / 마이그레이션), khả năng quan sát (observability / 관측 가능성) và môi trường vận hành (production / 운영 환경) quản trị (governance / 거버넌스).

Kiểm tra (audit / 감사) mới nhất đã đào sâu những năng lực (capability / 역량) React 19.2/19.3 trước đây chỉ được nhắc tên: `useEffectEvent` được đặt trong reactive-vs-event ngữ nghĩa (semantics / 의미론); `<Activity />` được giải thích theo trạng thái (state / 상태) preservation, tác động (effect / 효과) vòng đời (lifecycle / 생명주기), priority và bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프); `cacheSignal` được nối với resource-lifetime cancellation trong RSC; React hiệu năng (performance / 성능) Tracks được dùng như bằng chứng vận hành (production evidence / 운영 증거); `<ViewTransition>` được nối với chuyển tiếp (transition / 전이) ngữ nghĩa (semantics / 의미론); Fragment refs được giải thích theo năng lực (capability / 역량) thay vì “ref cho nhiều nút (node / 노드)”; `browser()` được đặt trong SSR/Suspense/hydration ranh giới (boundary / 경계); Trusted Types được đặt đúng vị trí defense-in-depth thay vì hiểu thành sanitizer; RSC ngữ cảnh (context / 맥락) 19.3 được giải thích theo phụ thuộc (dependency / 의존성)/máy khách (client / 클라이언트) ranh giới (boundary / 경계).

Những phần cố ý **không duplicate** gồm hiện thực (implementation / 구현) chi tiết của JavaScript thời gian chạy (runtime / 런타임), TypeScript hệ kiểu (type system / 타입 시스템), router/khung phần mềm (framework / 프레임워크) bộ nhớ đệm (cache / 캐시) ngữ nghĩa (semantics / 의미론) cụ thể, CSS rendering engine và backend authorization/lưu trữ (storage / 저장소). Khi cần học sâu các phần đó, dùng chuẩn gốc (canonical / 정본) lĩnh vực (domain / 도메인) tương ứng thay vì mở React chapter mới.

Coverage được coi là đạt mục tiêu khi người đọc có thể tự trả lời bằng lập luận (reasoning / 추론), không chỉ nhớ API: trạng thái (state / 상태) thuộc định danh (identity / 식별자) nào; cập nhật (update / 업데이트) được schedule/lần ghi nhận (commit / 커밋) ra sao; tác động (effect / 효과) đang synchronize tài nguyên (resource / 자원) gì; khi nào closure phải reactive và khi nào lô-gic (logic / 논리) là tác động (effect / 효과) sự kiện (event / 이벤트); tại sao bên ngoài (external / 외부) store cần snapshot đặc tả hợp đồng (contract / 계약); Suspense/lỗi (error / 오류)/Activity/ViewTransition giải quyết ranh giới (boundary / 경계) nào; SSR, hydration và RSC khác nhau ở đâu; browser-only subtree nên mô hình (model / 모델) thế nào; máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계) ảnh hưởng bundle và secret ra sao; hiệu năng (performance / 성능) bottleneck nằm ở kết xuất (render / 렌더링), lần ghi nhận (commit / 커밋), trình duyệt (browser / 브라우저) hay I/O; và bằng chứng (evidence / 증거) nào chứng minh giả thuyết môi trường vận hành (production / 운영 환경).

> **Chuyển mạch:** Coverage audit xác định phần nào đã có owner và phần nào còn thiếu. Nguyên tắc học sau audit biến kết quả đó thành thứ tự đọc; Cách dùng notes tiếp theo giữ người học trong đúng owner thay vì mở rộng tùy ý.

## Nguyên tắc học sau kiểm tra (audit / 감사)

Với kiến thức qua nhiều phiên bản (version / 버전), luôn đọc theo chuỗi **old mẫu (pattern / 패턴) → new mẫu (pattern / 패턴) → reason → di chuyển (migration / 마이그레이션) → khi còn gặp old mã (code / 코드)**. lớp (class / 클래스) thành phần (component / 컴포넌트), vòng đời (lifecycle / 생명주기), HOC, kết xuất (render / 렌더링) props và legacy APIs được giữ lại vì vẫn xuất hiện trong mã (code / 코드) enterprise.

Không tối ưu theo nghi thức. `memo`, `useMemo`, `useCallback`, transitions, trình biên dịch (compiler / 컴파일러) hay virtualization chỉ có giá trị khi đúng bottleneck/đặc tả hợp đồng (contract / 계약). Không dùng tác động (effect / 효과) để chữa trạng thái (state / 상태) mô hình (model / 모델) sai. Không dùng máy khách (client / 클라이언트) UI để thay authorization máy chủ (server / 서버). Không coi framework-specific router/bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) là React cốt lõi (core / 핵심).

> **Chuyển mạch:** Cách dùng notes kết thúc bằng quy tắc chọn file, ghi mốc version và kiểm tra owner. Nguồn chuẩn tiếp theo là nơi xác minh claim API/version, không phải một phần prose được suy đoán từ index.

## Cách dùng bộ ghi chú (note / 노트)

Đây là tài liệu học, không phải cheat sheet. Hãy đọc tuần tự. Sau mỗi mức (level / 수준) nên tự xây một dự án (project / 프로젝트) nhỏ và giải thích lại được các quyết định về quyền sở hữu trạng thái (state ownership / 상태 소유권), kết xuất (render / 렌더링) purity, tác động (effect / 효과) synchronization và thành phần (component / 컴포넌트) định danh (identity / 식별자) trước khi đi tiếp.

Ở Advanced/cấp cao (senior / 시니어) trở lên, dự án (project / 프로젝트) luyện tập nên có ít nhất một bên ngoài (external / 외부) subscription, một async mutation có thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론), một SSR/hydration ranh giới (boundary / 경계) hoặc khung phần mềm (framework / 프레임워크) dữ liệu (data / 데이터) ranh giới (boundary / 경계), profiling bằng production-like bản dựng (build / 빌드) và một quyết định kiến trúc được ghi lại theo “bài toán (problem / 문제) → bất biến (invariant / 불변식) → cơ chế (mechanism / 메커니즘) → sự đánh đổi (trade-off / 트레이드오프) → bằng chứng (evidence / 증거)”.

> **Chuyển mạch:** Index khép lại bằng source-of-truth rule: mọi claim phiên bản/API phải quay về canonical documentation và file owner tương ứng. Các lesson cụ thể bắt đầu từ route đã định ở trên.

## Nguồn chuẩn để kiểm chứng phiên bản (version / 버전)

Ưu tiên React Learn/API tham chiếu (reference / 참조) và React Blog bản phát hành (release / 릴리스) notes. Với React trình biên dịch (compiler / 컴파일러), đọc documentation/bản phát hành (release / 릴리스) tương ứng của trình biên dịch (compiler / 컴파일러) vì vòng đời (lifecycle / 생명주기) phiên bản (version / 버전) độc lập React cốt lõi (core / 핵심). Với RSC/khung phần mềm (framework / 프레임워크) tích hợp (integration / 통합), đọc hỗ trợ (support / 지원) ma trận (matrix / 행렬) và bảo mật (security / 보안) advisory của khung phần mềm (framework / 프레임워크) đang dùng; không suy ra tính tương thích (compatibility / 호환성) chỉ từ phiên bản (version / 버전) `react`.

> **Bàn giao:** Sau **Nguồn chuẩn để kiểm chứng phiên bản (version / 버전)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
