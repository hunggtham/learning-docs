# React Master ghi chú (note / 노트) — Master

> **Mạch đọc:** Đọc **React Master ghi chú (note / 노트) — Master** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. phiên bản (version / 버전) map React 15 → 19.3 và cách đọc phiên bản (version / 버전) đúng** sang **phiên bản (version / 버전) ma trận (matrix / 행렬) dùng khi rà soát (review / 검토) kiến trúc (architecture / 아키텍처)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> Mục tiêu của mức (level / 수준) Master không phải “thuộc mọi API”, mà là hiểu sâu invariants của React, trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계), máy chủ (server / 서버) kiến trúc (architecture / 아키텍처), thư viện (library / 라이브러리) thiết kế (design / 설계), di chuyển (migration / 마이그레이션), khả năng quan sát (observability / 관측 가능성), bảo mật (security / 보안) và cách ra quyết định khi ecosystem tiếp tục thay đổi.

## 1. phiên bản (version / 버전) map React 15 → 19.3 và cách đọc phiên bản (version / 버전) đúng

Tại thời điểm biên soạn, React 19.3 là stable hiện hành. Đây là chi tiết quan trọng vì React 19.x đã bổ sung tính năng (feature / 기능) qua minor bản phát hành (release / 릴리스) chứ không chỉ sửa bug. Vì vậy câu “dự án (project / 프로젝트) dùng React 19” chưa đủ để suy ra dự án (project / 프로젝트) có thể dùng API nào.

Khi rà soát (review / 검토) một codebase, hãy xác định đồng thời:

```text
React core version
React DOM version
framework version
bundler/compiler version
library peer dependency
runtime target
```

Một gói (package / 패키지) import API chỉ có từ React 19.3 nhưng khai peer phụ thuộc (dependency / 의존성) `react >=19.0` có thể làm bên tiêu thụ (consumer / 소비자) 19.0 crash. thư viện (library / 라이브러리) author phải encode minimum phiên bản (version / 버전) thật sự cần.

React docs hiện hành bám latest, trong khi enterprise codebase có thể vẫn ở React 18. Kỹ năng quan trọng là đọc API theo phiên bản (version / 버전) thay vì ghi nhớ tuyệt đối.

### Phiên bản (version / 버전) ma trận (matrix / 행렬) dùng khi rà soát (review / 검토) kiến trúc (architecture / 아키텍처)

Ở cấp Master, nên phân biệt ba loại phiên bản (version / 버전): **React thời gian chạy (runtime / 런타임)**, **React DOM/máy chủ (server / 서버) packages**, và **tooling/khung phần mềm (framework / 프레임워크)**. Một tính năng (feature / 기능) chỉ thật sự dùng được khi cả ba lớp tương thích.

| tính năng (feature / 기능)/năng lực (capability / 역량) | Minimum mốc nên nhớ | Ghi chú kiến trúc |
|---|---|---|
| Hooks | 16.8 | hàm (function / 함수) thành phần (component / 컴포넌트) trở thành hướng chính cho stateful UI. |
| hiện đại (modern / 현대적) gốc (root / 루트)/tính đồng thời (concurrency / 동시성) foundation | 18 | `createRoot` là prerequisite thực tế cho ngữ nghĩa (semantics / 의미론) React 18 hiện đại. |
| Actions/`use`/`useActionState`/`useOptimistic` | 19.0 | Full-stack ngữ nghĩa (semantics / 의미론) còn phụ thuộc khung phần mềm (framework / 프레임워크)/máy chủ (server / 서버) tích hợp (integration / 통합). |
| ref-as-prop và ngữ cảnh (context / 맥락) provider shorthand | 19.0 | Tác động trực tiếp đến thành phần (component / 컴포넌트)/thư viện (library / 라이브러리) API tính tương thích (compatibility / 호환성). |
| `<Activity />`, `useEffectEvent`, `cacheSignal` | 19.2 | Không có trong 19.0/19.1. |
| Stable View Transitions, Fragment refs | 19.3 | tính năng (feature / 기능) mới nhất trong baseline này; cần kiểm tra trình duyệt (browser / 브라우저)/khung phần mềm (framework / 프레임워크) hỗ trợ (support / 지원) riêng. |
| React trình biên dịch (compiler / 컴파일러) stable | trình biên dịch (compiler / 컴파일러) 1.0 | Tooling phiên bản (version / 버전) độc lập React; không suy ra từ `react` gói (package / 패키지) phiên bản (version / 버전). |

Một nguyên tắc tốt khi rà soát (review / 검토) PR là yêu cầu nhà phát triển (developer / 개발자) nói rõ “API này xuất hiện từ phiên bản (version / 버전) nào và gói (package / 패키지) nào cung cấp”, thay vì chỉ nói “React hỗ trợ”.

## 1A. Timeline chi tiết React 15 → 19 để định vị API

### React 15.x

React 15 là thời kỳ nhiều codebase enterprise cũ bắt đầu ổn định. `React.createClass`, ES6 classes, `React.PropTypes`, vòng đời (lifecycle / 생명주기) lớp (class / 클래스) và string refs đều có thể xuất hiện. React 15.5 là cột mốc di chuyển (migration / 마이그레이션) lớn: `React.createClass` và `React.PropTypes` bị deprecate khỏi cốt lõi (core / 핵심), lần lượt chuyển hướng sang `create-react-class` và `prop-types`.

### React 16.0

React 16 đưa renderer Fiber mới vào môi trường vận hành (production / 운영 환경). Với ứng dụng (application / 애플리케이션) nhà phát triển (developer / 개발자), các thay đổi dễ nhìn thấy gồm lỗi (error / 오류) Boundaries, portals và khả năng kết xuất (render / 렌더링) nhiều dạng React nút (node / 노드) linh hoạt hơn. Đây là nền tảng cho các cải tiến async/concurrent sau này.

### React 16.2

Fragment trở thành lớp trừu tượng (abstraction / 추상화) chính thức để group children mà không thêm DOM wrapper:

```jsx
<React.Fragment>
  <td>A</td>
  <td>B</td>
</React.Fragment>
```

Short cú pháp (syntax / 문법) `<>...</>` trở thành cú pháp quen thuộc về sau.

### React 16.3

Đây là minor rất quan trọng đối với mã (code / 코드) legacy: new ngữ cảnh (context / 맥락) API (`createContext`), `createRef`, `forwardRef` và `StrictMode` xuất hiện. String refs bắt đầu đi vào deprecation đường dẫn (path / 경로). Đây cũng là giai đoạn React giới thiệu vòng đời (lifecycle / 생명주기) mới để thay các giả định (assumptions / 가정들) từ `componentWill*`.

### React 16.6

`React.memo`, `React.lazy`, Suspense cho mã (code / 코드) splitting, `contextType` và `getDerivedStateFromError` xuất hiện. `findDOMNode` và legacy ngữ cảnh (context / 맥락) bước sâu hơn vào deprecation đường dẫn (path / 경로).

### React 16.8

Hooks xuất hiện: `useState`, `useEffect`, `useContext`, `useReducer`, `useMemo`, `useCallback`, `useRef`, `useImperativeHandle`, `useLayoutEffect`, `useDebugValue`. Đây là mốc lớn nhất khi so mã (code / 코드) lớp (class / 클래스) với mã (code / 코드) hàm (function / 함수) hiện đại.

### React 16.9

Các vòng đời (lifecycle / 생명주기) nguy hiểm được nhấn mạnh bằng tên `UNSAFE_*`; Profiler/tooling trưởng thành hơn. Module-pattern factory thành phần (component / 컴포넌트) cũng đi vào deprecation đường dẫn (path / 경로).

### React 16.13–16.14

`React.createFactory` bị deprecate ở 16.13. React 16.14 chủ yếu là tính tương thích (compatibility / 호환성) cầu nối (bridge / 브리지) trước React 17.

### React 17

React 17 là bản phát hành (release / 릴리스) chuyển tiếp hơn là một bản phát hành (release / 릴리스) feature-heavy. Gradual upgrade và thay đổi sự kiện (event / 이벤트) hệ thống (system / 시스템) là các điểm quan trọng. hiện đại (modern / 현대적) JSX transform xuất hiện trong cùng thời kỳ và cho phép JSX không bắt buộc `import React` chỉ để transform. Web SyntheticEvent pooling kiểu cũ không còn, nên `event.persist()` không còn cần cho mục đích chống pooling.

### React 18

Hiện đại (modern / 현대적) gốc (root / 루트) (`createRoot`, `hydrateRoot`), automatic batching, transitions, `useDeferredValue`, `useId`, `useSyncExternalStore`, `useInsertionEffect` và streaming SSR đánh dấu thế hệ concurrent foundations. `ReactDOM.render`, `hydrate` và `unmountComponentAtNode` bị deprecate.

### React 18.3

Hành vi (behavior / 동작) chủ yếu tương thích 18.2 nhưng thêm warning để chuẩn bị React 19. Đây là phiên bản (version / 버전) hợp lý làm bước di chuyển (migration / 마이그레이션) trung gian.

### React 19.0

Actions, `use`, `useActionState`, `useOptimistic`, form Actions, ref-as-prop và ngữ cảnh (context / 맥락) provider shorthand xuất hiện. React 19 cũng remove hàng loạt deprecated APIs: legacy gốc (root / 루트) APIs, string refs, legacy ngữ cảnh (context / 맥락), `findDOMNode`, `createFactory`, mô-đun (module / 모듈) mẫu (pattern / 패턴) factories và hỗ trợ (support / 지원) cũ liên quan hàm (function / 함수) thành phần (component / 컴포넌트) `propTypes/defaultProps`.

### React 19.1–19.3

Các minor này tiếp tục mở rộng máy chủ (server / 서버)/RSC/prerender, rồi thêm `Activity`, `useEffectEvent`, hiệu năng (performance / 성능)/máy chủ (server / 서버) capabilities và đến 19.3 có stable View chuyển tiếp (transition / 전이) tích hợp (integration / 통합), Fragment refs cùng các năng lực (capability / 역량) React DOM mới. Vì tính năng (feature / 기능) có thể xuất hiện ở minor, thư viện (library / 라이브러리) author phải khai minimum peer phiên bản (version / 버전) chính xác.

## 2. React trình biên dịch (compiler / 컴파일러) 1.0

React trình biên dịch (compiler / 컴파일러) 1.0 đã stable. Đây là build-time optimizer hiểu Rules of React và có thể tự động memoize thành phần (component / 컴포넌트)/giá trị (value / 값) để giảm nhu cầu tự viết `useMemo`, `useCallback` và `memo` trong nhiều trường hợp.

Trình biên dịch (compiler / 컴파일러) không nên được hiểu đơn giản là “plugin tự thêm memo”. Nó phân tích mã (code / 코드) React dựa trên purity/reactivity các ràng buộc (constraints / 제약조건들) rồi sinh đầu ra (output / 출력) tối ưu. Babel plugin là một tích hợp (integration / 통합) phổ biến, nhưng trình biên dịch (compiler / 컴파일러) cốt lõi (core / 핵심) được thiết kế tách khỏi Babel và ecosystem đang tích hợp nhiều bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) khác nhau.

Trình biên dịch (compiler / 컴파일러) hỗ trợ React 17, 18 và 19 với cấu hình phù hợp, nhưng React 19 là baseline tự nhiên nhất cho mã (code / 코드) mới.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — React trình biên dịch (compiler / 컴파일러) không đi cùng số phiên bản (version / 버전) React
>
> Trước khi stable, các gói (package / 패키지)/trình biên dịch (compiler / 컴파일러) prerelease từng có cách đánh phiên bản (version / 버전) dễ gây nhầm với React 19.x. Từ trình biên dịch (compiler / 컴파일러) 1.0, hãy xem trình biên dịch (compiler / 컴파일러) là toolchain có vòng đời (lifecycle / 생명주기) riêng. Khi nâng `react` từ 19.2 lên 19.3 không có nghĩa bạn tự động “nâng trình biên dịch (compiler / 컴파일러)”; và ngược lại, nâng trình biên dịch (compiler / 컴파일러) phải kiểm tra tính tương thích (compatibility / 호환성)/cấu hình (configuration / 구성) riêng.

## 3. trình biên dịch (compiler / 컴파일러) mô hình tư duy (mental model / 사고 모델)

Trước trình biên dịch (compiler / 컴파일러), nhà phát triển (developer / 개발자) thường tự tạo bộ nhớ đệm (cache / 캐시) ranh giới (boundary / 경계):

```jsx
const value = useMemo(() => expensive(a, b), [a, b]);

const handleClick = useCallback(() => {
  submit(id);
}, [id]);

const Child = memo(...);
```

Trình biên dịch (compiler / 컴파일러) có thể phân tích phụ thuộc (dependency / 의존성) và tự tạo memoization phù hợp. Điều này làm thay đổi tối ưu hóa (optimization / 최적화) idiom: mã (code / 코드) mới nên được viết pure, đơn giản và đúng Rules of React trước, rồi để trình biên dịch (compiler / 컴파일러) tối ưu.

Manual memoization vẫn hợp lệ khi cần định danh (identity / 식별자) đặc tả hợp đồng (contract / 계약) cụ thể, tác động (effect / 효과) phụ thuộc (dependency / 의존성) stability, hoặc khi profiler cho thấy trình biên dịch (compiler / 컴파일러) không tối ưu đúng bottleneck. Không xóa hàng loạt `useMemo`/`useCallback` trong mã (code / 코드) cũ chỉ vì bật trình biên dịch (compiler / 컴파일러); existing memoization có thể ảnh hưởng hành vi (behavior / 동작) hoặc đầu ra (output / 출력) compilation.

## 4. Rules of React là trình biên dịch (compiler / 컴파일러) đặc tả hợp đồng (contract / 계약)

Rules of React không chỉ là style convention. Chúng tạo điều kiện để thời gian chạy (runtime / 런타임) và trình biên dịch (compiler / 컴파일러) suy luận mã (code / 코드) an toàn.

Thành phần (component / 컴포넌트)/Hook phải pure trong kết xuất (render / 렌더링). Props/trạng thái (state / 상태) được coi immutable theo mô hình (model / 모델). Hook calls phải tuân rules. Không mutate giá trị (value / 값) thuộc kết xuất (render / 렌더링) khác. Không giấu side tác động (effect / 효과) trong helper tưởng như pure.

Ví dụ không tốt:

```jsx
function calculateTotal(cart) {
  cart.sort(comparePrice);
  return cart.reduce(sum, 0);
}
```

Nếu `cart` là prop/trạng thái (state / 상태), helper mutate đầu vào (input / 입력). Tốt hơn:

```jsx
function calculateTotal(cart) {
  return [...cart]
    .sort(comparePrice)
    .reduce(sum, 0);
}
```

Hoặc dùng non-mutating API khi môi trường (environment / 환경) hỗ trợ:

```js
cart.toSorted(comparePrice)
```

## 5. Manual memoization trong thời đại trình biên dịch (compiler / 컴파일러)

Manual memoization vẫn có chỗ đứng.

Một bên ngoài (external / 외부) tích hợp (integration / 통합) có thể yêu cầu callback định danh (identity / 식별자) ổn định. Một tác động (effect / 효과) có thể cần đối tượng (object / 객체)/hàm (function / 함수) ổn định để không restart synchronization. Một phép tính rất nặng có thể cần bộ nhớ đệm (cache / 캐시) mà profiler xác nhận. thư viện (library / 라이브러리) có thể chạy trong app không bật trình biên dịch (compiler / 컴파일러) nên vẫn cần hiệu năng (performance / 성능) chiến lược (strategy / 전략) riêng.

Cấp cao (senior / 시니어) mã (code / 코드) không được đánh giá bằng số lượng `useMemo`; thường mã (code / 코드) càng đơn giản càng tốt nếu trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) đã xử lý phần tối ưu.

## 6. Chiến lược adopt trình biên dịch (compiler / 컴파일러)

Với codebase lớn, adoption nên incremental:

1. Bật lint rules liên quan React/trình biên dịch (compiler / 컴파일러).
2. Sửa purity và Hook quy tắc (rule / 규칙) violations.
3. Bật trình biên dịch (compiler / 컴파일러) cho phạm vi (scope / 범위) nhỏ hoặc theo cấu hình incremental.
4. Chạy kiểm thử (test / 테스트) và so sánh hành vi (behavior / 동작).
5. Profile hiệu năng (performance / 성능) trọng yếu (critical / 중요) luồng (flow / 흐름).
6. Theo dõi bản dựng (build / 빌드) thời gian (time / 시간) và bundle/thời gian chạy (runtime / 런타임) regression.
7. Mở rộng phạm vi khi ổn định.

Không nên bật trình biên dịch (compiler / 컴파일러) rồi bỏ qua warning. Một số mã (code / 코드) có thể bị skip; mục tiêu là codebase tuân Rules of React, không chỉ “bản dựng (build / 빌드) thành công”.

## 7. trình biên dịch (compiler / 컴파일러) directives và compilation ranh giới (boundary / 경계)

React trình biên dịch (compiler / 컴파일러) có directives/cấu hình (configuration / 구성) để điều khiển compilation trong các trường hợp cần thiết. Đây là exception cơ chế (mechanism / 메커니즘), không phải default coding style. Nếu codebase phải rải directive tắt trình biên dịch (compiler / 컴파일러) khắp nơi, thường cần refactor lô-gic (logic / 논리) vi phạm Rules of React hoặc tích hợp (integration / 통합) ranh giới (boundary / 경계) chưa đúng.

Vì directives có thể tiến hóa, luôn đọc tham chiếu (reference / 참조) đúng trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전) thay vì bản sao (copy / 복사) cấu hình (config / 설정) cũ từ blog.

## 8. Scheduling và priority ở mức ứng dụng (application / 애플리케이션)

Ứng dụng (application / 애플리케이션) nhà phát triển (developer / 개발자) không cần thao tác scheduler nội bộ (internal / 내부) API. công khai (public / 공개) primitives như transitions và deferred giá trị (value / 값) cho phép biểu đạt priority ở mức UX.

Có thể nghĩ thành hai nhóm:

```text
Urgent: typing, pointer feedback, direct manipulation
Non-urgent: render result lớn, đổi tab nặng, background refresh
```

Một lỗi là biến mọi cập nhật (update / 업데이트) thành chuyển tiếp (transition / 전이). Nếu người dùng (user / 사용자) bấm toggle mà visual phản hồi (feedback / 피드백) bị trì hoãn, UX xấu. Priority là ngữ nghĩa (semantic / 의미적) UX, không chỉ hiệu năng (performance / 성능) knob.

## 9. Suspense kiến trúc (architecture / 아키텍처) và reveal chiến lược (strategy / 전략)

Suspense ranh giới (boundary / 경계) nên phản ánh “reveal đơn vị (unit / 단위)”: nhóm nội dung nào nên xuất hiện cùng nhau.

```jsx
<PageShell>
  <Header />

  <Suspense fallback={<ProductSkeleton />}>
    <Product />
  </Suspense>

  <Suspense fallback={<ReviewsSkeleton />}>
    <Reviews />
  </Suspense>
</PageShell>
```

Nếu sản phẩm (product / 제품) trọng yếu (critical / 중요) còn reviews secondary, hai ranh giới (boundary / 경계) riêng cho phép progressive reveal. ranh giới (boundary / 경계) quá cao khiến toàn màn hình đổi spinner; ranh giới (boundary / 경계) quá nhỏ tạo loading rời rạc. Skeleton nên giữ bố cục (layout / 레이아웃) để tránh CLS.

## 10. Streaming kiến trúc (architecture / 아키텍처)

SSR streaming gửi phần HTML sẵn sàng trước thay vì chờ toàn cây (tree / 트리). nút (node / 노드) thường dùng `renderToPipeableStream`; Web Streams môi trường (environment / 환경) dùng `renderToReadableStream`. React 19.x còn có nhóm prerender/resume cho kiến trúc (architecture / 아키텍처) máy chủ (server / 서버) phức tạp hơn.

Tự xây SSR khung phần mềm (framework / 프레임워크) đòi hỏi xử lý asset injection, abort, lỗi (error / 오류) status, CSP nonce, hydration dữ liệu (data / 데이터), bộ nhớ đệm (cache / 캐시), routing và triển khai (deployment / 배포). ứng dụng (application / 애플리케이션) nhóm (team / 팀) thường nên dùng khung phần mềm (framework / 프레임워크) thay vì tự viết toàn bộ giao thức (protocol / 프로토콜).

## 11. Partial pre-rendering và prerender/resume

React 19.x tiếp tục mở rộng máy chủ (server / 서버) rendering để kết hợp pre-rendered shell với động (dynamic / 동적)/resumable content. Master-level concern ở đây là phân biệt thành phần nguyên thủy (primitive / 기본 요소) của React DOM với tính năng (feature / 기능) marketing/hiện thực (implementation / 구현) của khung phần mềm (framework / 프레임워크).

Khi thiết kế máy chủ (server / 서버) rendering/bộ nhớ đệm (cache / 캐시), cần trả lời:

```text
phần nào static ở build time?
phần nào static theo request?
phần nào personalized?
cache key là gì?
invalidated lúc nào?
HTML nào có thể dùng chung?
data nào tuyệt đối không được cache cross-user?
```

Nếu không trả lời rõ bộ nhớ đệm (cache / 캐시) key và phạm vi (scope / 범위), chưa nên bộ nhớ đệm (cache / 캐시).

## 12. React máy chủ (server / 서버) Components kiến trúc (architecture / 아키텍처)

RSC chuyển một phần thành phần (component / 컴포넌트) thực thi (execution / 실행) sang máy chủ (server / 서버)/bản dựng (build / 빌드) môi trường (environment / 환경) và chỉ gửi máy khách (client / 클라이언트) những gì cần cho interactivity.

Lợi ích tiềm năng: giảm máy khách (client / 클라이언트) JavaScript; colocate máy chủ (server / 서버) dữ liệu (data / 데이터) truy cập (access / 접근); stream composition; tránh gửi server-only phụ thuộc (dependency / 의존성) vào máy khách (client / 클라이언트) bundle nếu ranh giới (boundary / 경계) đúng.

Chi phí: mô hình tư duy (mental model / 사고 모델) hai môi trường; serializability ranh giới (boundary / 경계); khung phần mềm (framework / 프레임워크) coupling; bộ nhớ đệm (cache / 캐시) ngữ nghĩa (semantics / 의미론) phức tạp; bảo mật (security / 보안) surface mới; gỡ lỗi (debug / 디버그)/tooling khó hơn SPA thuần.

Không chọn RSC chỉ vì “mới”. Chọn khi sản phẩm (product / 제품) và khung phần mềm (framework / 프레임워크) thực sự hưởng lợi.

## 13. RSC payload và máy khách (client / 클라이언트) ranh giới (boundary / 경계)

Máy chủ (server / 서버) Components không chỉ “kết xuất (render / 렌더링) thành HTML”. khung phần mềm (framework / 프레임워크) sử dụng RSC giao thức (protocol / 프로토콜)/payload để biểu diễn rendered máy chủ (server / 서버) cây (tree / 트리), references tới máy khách (client / 클라이언트) Components và dữ liệu serializable. SSR có thể phối hợp để tạo initial HTML.

`"use client"` tạo máy khách (client / 클라이언트) ranh giới mô-đun (module boundary / 모듈 경계). Props từ máy chủ (server / 서버) đi qua máy khách (client / 클라이언트) thành phần (component / 컴포넌트) ranh giới (boundary / 경계) phải serializable theo đặc tả hợp đồng (contract / 계약) hỗ trợ. Không truyền tùy tiện lớp (class / 클래스) instance, DB liên kết (connection / 연결) hoặc hàm (function / 함수) thường. máy chủ (server / 서버) hàm (function / 함수) tham chiếu (reference / 참조) là trường hợp giao thức (protocol / 프로토콜) xử lý riêng.

## 14. bộ nhớ đệm (cache / 캐시)/dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) trong RSC/full-stack React

Một hệ thống có thể có nhiều lớp bộ nhớ đệm (cache / 캐시):

```text
browser HTTP cache
CDN/edge cache
framework route/data cache
React request/cache primitive
database cache
client query cache
```

Sai lầm nghiêm trọng là bộ nhớ đệm (cache / 캐시) toàn cục (global / 전역) dữ liệu theo người dùng (user / 사용자) nhưng key không chứa người dùng (user / 사용자) định danh (identity / 식별자), dẫn tới dữ liệu (data / 데이터) leak. Mỗi bộ nhớ đệm (cache / 캐시) phải có phạm vi (scope / 범위), key, thời gian tồn tại (lifetime / 수명) và vô hiệu hóa (invalidation / 무효화) rõ.

Một idiom tốt: “Nếu không mô tả được bộ nhớ đệm (cache / 캐시) key bằng một câu hoàn chỉnh, chưa nên bộ nhớ đệm (cache / 캐시).”

## 15. bảo mật (security / 보안) cho RSC và máy chủ (server / 서버) Functions

Máy chủ (server / 서버) hàm (function / 함수) phải được coi là mạng (network / 네트워크) entry điểm (point / 지점) dù cú pháp (syntax / 문법) trông như gọi hàm (function / 함수) cục bộ (local / 로컬).

Checklist tối thiểu:

```text
authenticate
authorize
validate input
rate-limit khi cần
protect theo CSRF/threat model của framework
avoid secret leakage
avoid mass assignment
sanitize/encode đúng context
log audit action quan trọng
patch security advisory
```

Không tin hidden trường dữ liệu (field / 필드), role gửi từ máy khách (client / 클라이언트) hay serialized đối tượng (object / 객체). máy chủ (server / 서버) thành phần (component / 컴포넌트) cũng có thể leak secret nếu vô tình truyền secret thành máy khách (client / 클라이언트) thành phần (component / 컴포넌트) prop.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — patch phiên bản (version / 버전) là một phần của kiến trúc (architecture / 아키텍처) bảo mật (security / 보안)
>
> Các advisory React máy chủ (server / 서버) Components cuối năm 2025 cho thấy một major/minor label như `19.1` không đủ để đánh giá an toàn; fix đã được backport qua nhiều patch branch và một số bản fix ban đầu còn tiếp tục được cập nhật. Với RSC, quy trình bản phát hành (release / 릴리스) phải bao gồm phụ thuộc (dependency / 의존성)/bảo mật (security / 보안) monitoring và upgrade theo advisory chính thức của React/khung phần mềm (framework / 프레임워크). Baseline 19.3 của tài liệu giúp học API mới nhất, nhưng môi trường vận hành (production / 운영 환경) vẫn phải theo patch bản phát hành (release / 릴리스) hiện hành thay vì “đóng băng vì đã ở 19.3”.

## 16. Trusted Types và XSS ranh giới (boundary / 경계)

React escape văn bản (text / 텍스트) mặc định nhưng XSS vẫn có thể xuất hiện qua `dangerouslySetInnerHTML`, URL nguy hiểm, third-party DOM thư viện (library / 라이브러리), raw HTML renderer hoặc máy chủ (server / 서버) đầu ra (output / 출력) không sanitize.

React 19.3 có cải tiến liên quan Trusted Types. Trusted Types + CSP + sanitization là defense-in-depth; không nên coi React escaping là lớp bảo vệ toàn diện.

## 17. Large-scale trạng thái (state / 상태) kiến trúc (architecture / 아키텍처)

Ở quy mô (scale / 규모) lớn, trạng thái (state / 상태) nên theo lĩnh vực (domain / 도메인) và quyền sở hữu (ownership / 소유권) thay vì theo một thư viện (library / 라이브러리) duy nhất.

```text
Route / URL
 ├─ search / filter / page
Feature server data
 ├─ query cache / RSC
Feature form
 ├─ local / form library
Feature UI state
 ├─ local reducer
Cross-feature client state
 └─ external store
```

Giant toàn cục (global / 전역) store chứa tuyến (route / 경로), API bộ nhớ đệm (cache / 캐시), modal, form draft, người dùng (user / 사용자) profile và mọi thực thể (entity / 엔터티) trở thành coupling hub. Maturity kiến trúc (architecture / 아키텍처) thể hiện ở khả năng không globalize dữ liệu không cần toàn cục (global / 전역).

## 18. máy trạng thái (state machine / 상태 머신) và reducer thiết kế (design / 설계)

Boolean trạng thái (state / 상태) dễ tạo impossible states:

```js
{
  loading: true,
  success: true,
  error: true
}
```

Tốt hơn:

```ts
type State =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: Data }
  | { status: "error"; error: Error };
```

Workflow phức tạp có thể dùng máy trạng thái (state machine / 상태 머신). máy trạng thái (state machine / 상태 머신) phù hợp khi chuyển tiếp (transition / 전이) quy tắc (rule / 규칙) chặt, nhiều side tác động (effect / 효과) và cần mô hình (model / 모델) rõ. Không dùng cho counter đơn giản.

## 19. Event-driven UI kiến trúc (architecture / 아키텍처)

Event-driven mô hình (model / 모델) tách “điều gì xảy ra” khỏi “trạng thái (state / 상태) thay đổi ra sao”:

```js
dispatch({
  type: "checkout_submitted",
  payload: formData,
});
```

Reducer/máy trạng thái (state machine / 상태 머신) xử lý chuyển tiếp (transition / 전이); tác động (effect / 효과)/dịch vụ (service / 서비스) tầng (layer / 계층) xử lý I/O. mẫu (pattern / 패턴) này hữu ích ở workflow enterprise nhưng không nên tự xây khung phần mềm (framework / 프레임워크) sự kiện (event / 이벤트) bus riêng nếu thư viện (library / 라이브러리) hiện có đã giải quyết tốt.

## 20. thiết kế (design / 설계) hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처)

Một thiết kế (design / 설계) hệ thống (system / 시스템) môi trường vận hành (production / 운영 환경) có nhiều lớp:

```text
design tokens
primitive components
accessible behavior
composite components
patterns/templates
documentation
visual regression
versioning
```

Thành phần nguyên thủy (primitive / 기본 요소) như Button/đầu vào (input / 입력)/Dialog phải rất ổn định vì hàng trăm bên tiêu thụ (consumer / 소비자) phụ thuộc. API quá mở làm phá consistency; API quá đóng làm nhóm (team / 팀) fork thành phần (component / 컴포넌트). Headless thành phần nguyên thủy (primitive / 기본 요소) + đơn vị từ (token / 토큰)/variant tầng (layer / 계층) thường cân bằng tốt.

## 21. thư viện (library / 라이브러리) authoring

React thư viện (library / 라이브러리) phải cân nhắc công khai (public / 공개) kiểu (type / 타입) surface, peer phụ thuộc (dependency / 의존성), SSR tính tương thích (compatibility / 호환성), ESM/CJS chiến lược (strategy / 전략), cây (tree / 트리) shaking, side effects, styling injection, khả năng tiếp cận (accessibility / 접근성), ref API, trình biên dịch (compiler / 컴파일러) tính tương thích (compatibility / 호환성) và phiên bản (version / 버전) hỗ trợ (support / 지원).

Không nên bundle React vào thư viện (library / 라이브러리) thông thường; React thường là peer phụ thuộc (dependency / 의존성) để tránh duplicate React và Hook thất bại (failure / 실패). Không truy cập `window` ở mô-đun (module / 모듈) top mức (level / 수준) nếu thư viện (library / 라이브러리) cần SSR.

## 22. gói (package / 패키지) exports và peer dependencies

Ví dụ conceptual:

```json
{
  "name": "@acme/ui",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  },
  "peerDependencies": {
    "react": ">=19.3.0",
    "react-dom": ">=19.3.0"
  }
}
```

Nếu dùng API 19.3-only, minimum peer phiên bản (version / 버전) phải phản ánh điều đó. Dual ESM/CJS cần kiểm thử (test / 테스트) trên bundler/nút (node / 노드)/kiểm thử (test / 테스트) runner thật; gói (package / 패키지) resolution khác nhau giữa toolchains.

## 23. React phiên bản (version / 버전) di chuyển (migration / 마이그레이션)

Di chuyển (migration / 마이그레이션) tốt gồm:

```text
đọc official upgrade guide
update react + react-dom đồng bộ
update types
update framework
chạy codemod nếu được khuyến nghị
fix deprecated API
run test
run production build
profile critical flow
canary release
monitor production errors
```

Với RSC khung phần mềm (framework / 프레임워크), React có thể bị khung phần mềm (framework / 프레임워크) pin. Không force React upgrade độc lập nếu khung phần mềm (framework / 프레임워크) chưa hỗ trợ (support / 지원).

### Di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) thực tế giữa các thế hệ

Nếu đang ở React 17, bước đầu là chuyển gốc (root / 루트) API và ecosystem tương thích React 18, sau đó kiểm tra Strict chế độ (mode / 모드)/automatic batching/tính đồng thời (concurrency / 동시성) các giả định (assumptions / 가정들). Nếu đang ở React 18.2, có thể đi qua **18.3** để nhận warning di chuyển (migration / 마이그레이션) rồi mới lên React 19. Với React 19, phải cập nhật `react` và `react-dom` đồng bộ, TypeScript types tương ứng, chạy codemod được React nhóm (team / 팀) khuyến nghị và kiểm tra khung phần mềm (framework / 프레임워크) peer phụ thuộc (dependency / 의존성).

Một di chuyển (migration / 마이그레이션) không nên được đánh giá thành công chỉ vì app “kết xuất (render / 렌더링) được”. Các thay đổi như batching, hydration, ref callback cleanup, TypeScript typings, removed legacy APIs hoặc third-party thư viện (library / 라이브러리) dựa vào React internals có thể chỉ lộ trong kiểm thử (test / 테스트), SSR hoặc môi trường vận hành (production / 운영 환경).

Đối với khung phần mềm (framework / 프레임워크) RSC, không force một React minor/patch mới hơn khung phần mềm (framework / 프레임워크) hỗ trợ (support / 지원) ma trận (matrix / 행렬). khung phần mềm (framework / 프레임워크) có thể pin hoặc thử nghiệm một bản dựng (build / 빌드) React cụ thể để đồng bộ giao thức (protocol / 프로토콜)/máy chủ (server / 서버) thời gian chạy (runtime / 런타임).

## 23A. di chuyển (migration / 마이그레이션) là behavior-preserving transformation, không phải đổi cú pháp (syntax / 문법) hàng loạt

Một di chuyển (migration / 마이그레이션) React tốt giữ hành vi (behavior / 동작) và quyền sở hữu (ownership / 소유권) ổn định trước khi đổi lớp trừu tượng (abstraction / 추상화). Với lớp (class / 클래스) mã (code / 코드), hãy inventory trạng thái (state / 상태), derived values, subscriptions, DOM refs, async requests, lỗi (error / 오류) boundaries và công khai (public / 공개) thành phần (component / 컴포넌트) đặc tả hợp đồng (contract / 계약). Sau đó tách lô-gic (logic / 논리) theo intent: kết xuất (render / 렌더링) derivation ở kết xuất (render / 렌더링), user-caused công việc (work / 작업) ở sự kiện (event / 이벤트) handler, bên ngoài (external / 외부) synchronization ở tác động (effect / 효과), complex chuyển tiếp trạng thái (state transition / 상태 전이) ở reducer, dùng chung (shared / 공유) cross-tree phụ thuộc (dependency / 의존성) ở ngữ cảnh (context / 맥락)/store.

Không cần đổi toàn bộ cây (tree / 트리) trong một PR. Leaf thành phần (component / 컴포넌트) ít phụ thuộc (dependency / 의존성) là điểm bắt đầu tốt; wrapper/HOC có thể tiếp tục bao quanh hàm (function / 함수) thành phần (component / 컴포넌트) mới. lỗi (error / 오류) ranh giới (boundary / 경계) lớp (class / 클래스) có thể được giữ lại nếu đang hoạt động ổn. Snapshot/tích hợp (integration / 통합)/E2E tests dùng làm an toàn (safety / 안전) net cho hành vi (behavior / 동작), còn codemod chỉ giải quyết mechanical API changes.

Khi nâng phiên bản (version / 버전) đồng thời với refactor thành phần (component / 컴포넌트) mô hình (model / 모델), rủi ro tăng vì khó phân biệt lỗi do hành vi thời gian chạy (runtime behavior / 런타임 동작) thay đổi (change / 변경) hay do rewrite. Với codebase lớn, tách **phiên bản (version / 버전) di chuyển (migration / 마이그레이션)**, **deprecated API removal** và **kiến trúc (architecture / 아키텍처) refactor** thành các bước quan sát được thường an toàn hơn.

## 24. Legacy lớp (class / 클래스) thành phần (component / 컴포넌트)

Enterprise mã (code / 코드) vẫn có lớp (class / 클래스):

```jsx
class Counter extends React.Component {
  state = { count: 0 };

  componentDidMount() {
    // setup
  }

  componentWillUnmount() {
    // cleanup
  }

  render() {
    return (
      <button
        onClick={() =>
          this.setState(s => ({ count: s.count + 1 }))
        }
      >
        {this.state.count}
      </button>
    );
  }
}
```

Các API cần biết để đọc mã (code / 코드) cũ: `props`, `state`, `setState`, `render`, `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`, `getDerivedStateFromProps`, `getSnapshotBeforeUpdate`, `componentDidCatch`.

Không migrate vòng đời (lifecycle / 생명주기) sang `useEffect` theo ánh xạ (mapping / 매핑) một-một máy móc. Hook mô hình (model / 모델) dựa trên synchronization và luồng dữ liệu (data flow / 데이터 흐름) khác vòng đời (lifecycle / 생명주기) mô hình (model / 모델) của lớp (class / 클래스).

## 24A. Legacy React tham chiếu (reference / 참조) — đủ để đọc dự án (project / 프로젝트) React 15–18

Phần này là tham chiếu (reference / 참조) có giải thích cho các API đời cũ quan trọng. Mục tiêu không phải khuyên viết mã (code / 코드) mới bằng chúng mà để khi mở một dự án (project / 프로젝트) enterprise lâu năm, bạn hiểu chính xác mã (code / 코드) đang làm gì.

### Thành phần (component / 컴포넌트) creation

#### `React.createClass(spec)`

Tạo thành phần (component / 컴포넌트) theo đối tượng (object / 객체) specification. Các key phổ biến gồm `render`, `getInitialState`, `getDefaultProps`, vòng đời (lifecycle / 생명주기) methods, custom methods và `mixins`. Methods được autobind. Từ React 15.5 API được đưa ra khỏi cốt lõi (core / 핵심); gói (package / 패키지) `create-react-class` tồn tại cho di chuyển (migration / 마이그레이션).

#### `React.Component`

Cơ sở (base / 기반) lớp (class / 클래스) cho ES6 lớp (class / 클래스) thành phần (component / 컴포넌트):

```jsx
class App extends React.Component {
  render() {
    return <div />;
  }
}
```

Các instance trường dữ liệu (field / 필드) quan trọng là `this.props`, `this.state`, `this.context`; API cập nhật (update / 업데이트) chính là `this.setState` và `this.forceUpdate`.

#### `React.PureComponent`

Giống `Component` nhưng có shallow props/trạng thái (state / 상태) comparison tương đương một hiện thực (implementation / 구현) thông thường của `shouldComponentUpdate`.

### Lớp (class / 클래스) trạng thái (state / 상태) APIs

#### `this.setState(nextStateOrUpdater, callback?)`

Đối tượng (object / 객체) form shallow-merges trạng thái (state / 상태). Updater form nhận previous trạng thái (state / 상태) và props:

```jsx
this.setState(
  (state, props) => ({
    count:
      state.count +
      props.step,
  }),
  () => {
    console.log("committed");
  }
);
```

Callback tồn tại trong lớp (class / 클래스) API cũ nhưng Hook setter không có callback tương đương. Với Hooks, lô-gic (logic / 논리) “sau trạng thái (state / 상태) lần ghi nhận (commit / 커밋)” phải được mô hình (model / 모델) theo tác động (effect / 효과)/sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론) chứ không truyền callback vào setter.

#### `this.forceUpdate(callback?)`

Yêu cầu thành phần (component / 컴포넌트) re-render dù React không được báo trạng thái (state / 상태) thay đổi (change / 변경) thông thường. Đây là escape hatch. Nếu app cần `forceUpdate` thường xuyên, có thể dữ liệu (data / 데이터) nguồn (source / 소스) nằm ngoài React mà không có subscription đúng. Với bên ngoài (external / 외부) store hiện đại, `useSyncExternalStore` là lớp trừu tượng (abstraction / 추상화) phù hợp hơn.

### Lớp (class / 클래스) vòng đời (lifecycle / 생명주기) tham chiếu (reference / 참조)

```text
constructor
static getDerivedStateFromProps
render
componentDidMount

shouldComponentUpdate
static getDerivedStateFromProps
render
getSnapshotBeforeUpdate
componentDidUpdate

componentWillUnmount

static getDerivedStateFromError
componentDidCatch
```

Legacy names:

```text
UNSAFE_componentWillMount
UNSAFE_componentWillReceiveProps
UNSAFE_componentWillUpdate
```

Các tên không có `UNSAFE_` từng tồn tại trong mã (code / 코드) cũ và dần bị deprecate. “UNSAFE” nói về incompatibility của các giả định (assumptions / 가정들) trong async/concurrent rendering, không có nghĩa phương thức (method / 메서드) luôn gây crash.

### Lỗi (error / 오류) ranh giới (boundary / 경계) lớp (class / 클래스) APIs

`static getDerivedStateFromError(error)` dùng để cập nhật fallback trạng thái (state / 상태) từ lỗi kết xuất (render / 렌더링). `componentDidCatch(error, info)` dùng side tác động (effect / 효과) như logging. lỗi (error / 오류) ranh giới (boundary / 경계) lớp (class / 클래스) vẫn là kiến thức thực tế vì React cốt lõi (core / 핵심) chưa cung cấp một Hook thay thế trực tiếp cho toàn bộ lỗi (error / 오류) ranh giới (boundary / 경계) hành vi (behavior / 동작).

### React element APIs

`createElement` vẫn là thành phần nguyên thủy (primitive / 기본 요소) hợp lệ. `cloneElement`, `isValidElement` và nhóm `Children` vẫn xuất hiện trong thư viện (library / 라이브러리) mã (code / 코드). Tuy nhiên `Children`/`cloneElement` thường làm thành phần (component / 컴포넌트) cấu trúc (structure / 구조) opaque hơn và nên được cân nhắc so với tường minh (explicit / 명시적) composition/ngữ cảnh (context / 맥락).

`createFactory` và old DOM factories là legacy/removed như đã giải thích.

### Ref APIs theo thời đại

```text
string ref
→ callback ref
→ createRef
→ forwardRef
→ useRef
→ React 19 ref-as-prop
```

Không phải bước sau luôn “xóa” bước trước. Callback ref vẫn hữu ích; `createRef` vẫn phù hợp lớp (class / 클래스); `forwardRef` vẫn quan trọng cho React 18 tính tương thích (compatibility / 호환성); ref-as-prop là API mới cho hàm (function / 함수) thành phần (component / 컴포넌트) React 19.

### ReactDOM legacy gốc (root / 루트) APIs

```jsx
ReactDOM.render(element, container);
ReactDOM.hydrate(element, container);
ReactDOM.unmountComponentAtNode(container);
ReactDOM.findDOMNode(component);
```

Các API này là dấu hiệu rõ nhất của codebase pre-modern gốc (root / 루트). React 18 deprecate gốc (root / 루트) legacy APIs và React 19 remove chúng. di chuyển (migration / 마이그레이션) mục tiêu (target / 대상) là `createRoot`, `hydrateRoot`, `root.unmount` và tường minh (explicit / 명시적) refs.

### Legacy ngữ cảnh (context / 맥락)

```text
childContextTypes
getChildContext()
contextTypes
```

Legacy ngữ cảnh (context / 맥락) bị remove ở React 19. New ngữ cảnh (context / 맥락) API có từ React 16.3, sau đó hàm (function / 함수) thành phần (component / 컴포넌트) đọc bằng `useContext`; React 19 cho kết xuất (render / 렌더링) ngữ cảnh (context / 맥락) đối tượng (object / 객체) trực tiếp như provider.

### Kiểu (type / 타입)/thời gian chạy (runtime / 런타임) checking legacy

`React.PropTypes` chuyển sang `prop-types` từ React 15.5. Function-component `propTypes` không còn được React 19 xử lý. Điều này không có nghĩa thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증) luôn vô dụng: dữ liệu ở mạng (network / 네트워크)/form ranh giới (boundary / 경계) vẫn có thể cần lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증); TypeScript chỉ kiểm tra compile thời gian (time / 시간).

### Legacy reuse patterns

Mixins → HOC → kết xuất (render / 렌더링) props → Custom Hooks là một lịch sử composition dễ gặp. Không có nghĩa HOC/kết xuất (render / 렌더링) props bị remove. Redux `connect`, decorators hoặc thành phần (component / 컴포넌트) APIs cũ vẫn có thể dùng HOC hợp lệ.

### Legacy testing

Enzyme/shallow-rendering-style kiểm thử (test / 테스트) từng rất phổ biến vì lớp (class / 클래스) thành phần (component / 컴포넌트) và hiện thực (implementation / 구현) detail dễ inspect. React hiện đại khuyến nghị kiểm thử (test / 테스트) hành vi (behavior / 동작) qua DOM/bản địa (native / 네이티브) môi trường (environment / 환경) hơn. Khi migrate, đừng chỉ đổi kiểm thử (test / 테스트) API; hãy chuyển assertion từ trạng thái nội bộ (internal state / 내부 상태)/instance phương thức (method / 메서드) sang đầu ra (output / 출력) và người dùng (user / 사용자) tương tác (interaction / 상호작용) khi có thể.

## 25. Legacy APIs và deprecation mindset

Mã (code / 코드) cũ có thể chứa string refs, old ngữ cảnh (context / 맥락), `findDOMNode`, legacy gốc (root / 루트) hoặc vòng đời (lifecycle / 생명주기) `UNSAFE_...`. Không chỉ thay tên API; cần hiểu vì sao API cũ xung đột với concurrent kiến trúc (architecture / 아키텍처), encapsulation hoặc new rendering mô hình (model / 모델).

Di chuyển (migration / 마이그레이션) tốt sửa mô hình tư duy (mental model / 사고 모델), không chỉ làm warning biến mất.

## 26. Hydration at quy mô (scale / 규모)

Hydration chi phí (cost / 비용) lớn nếu page có quá nhiều máy khách (client / 클라이언트) Components. Các chiến lược gồm giảm máy khách (client / 클라이언트) ranh giới (boundary / 경계), máy chủ (server / 서버) kết xuất (render / 렌더링) static content, mã (code / 코드) split, defer non-critical tương tác (interaction / 상호작용), stream, tránh gốc (root / 루트) provider quá lớn và không serialize dữ liệu (data / 데이터) khổng lồ.

Hydration mismatch nên được monitor ở môi trường vận hành (production / 운영 환경). Lỗi timezone/locale/ngẫu nhiên có thể rất khó tái hiện cục bộ (local / 로컬).

## 27. hiệu năng (performance / 성능) ngân sách (budget / 예산)

Nhóm (team / 팀) nên có hiệu năng (performance / 성능) ngân sách (budget / 예산) thay vì “cảm giác nhanh”:

```text
initial JS
route JS
LCP
INP
CLS
API latency
interaction readiness
long tasks
React commit duration
```

Ngân sách (budget / 예산) phải dựa trên thiết bị (device / 장치)/mạng (network / 네트워크) mục tiêu (target / 대상) thật. Máy desktop mạnh của nhà phát triển (developer / 개발자) không đại diện người dùng (user / 사용자) mobile mid-range.

## 28. tương tác (interaction / 상호작용) hiệu năng (performance / 성능)

INP/tương tác (interaction / 상호작용) độ trễ (latency / 지연 시간) có thể xấu khi sự kiện (event / 이벤트) kích hoạt JS/kết xuất (render / 렌더링)/bố cục (layout / 레이아웃) dài. Các hướng xử lý: giảm công việc (work / 작업) trong sự kiện (event / 이벤트); chuyển non-urgent công việc (work / 작업) sang chuyển tiếp (transition / 전이); virtualize; split computation; tránh bố cục (layout / 레이아웃) thrash; dùng Web Worker nếu CPU-heavy thích hợp; tối ưu thuật toán (algorithm / 알고리즘) trước memo.

React tối ưu hóa (optimization / 최적화) không thay algorithmic tối ưu hóa (optimization / 최적화).

## 29. bộ nhớ (memory / 메모리) leak và tài nguyên (resource / 자원) vòng đời (lifecycle / 생명주기)

Leak thường đến từ tài nguyên (resource / 자원) không cleanup: listener, timer, observer, subscription, WebSocket, retained bộ nhớ đệm (cache / 캐시) hoặc DOM tham chiếu (reference / 참조) lớn.

```jsx
useEffect(() => {
  const observer = new ResizeObserver(handleResize);
  observer.observe(node);

  return () => observer.disconnect();
}, [node]);
```

Cleanup phải đối xứng setup. Abort yêu cầu (request / 요청) cũng giảm tài nguyên (resource / 자원)/mạng (network / 네트워크) lãng phí khi phù hợp.

## 30. khả năng quan sát (observability / 관측 가능성)

Môi trường vận hành (production / 운영 환경) React cần lỗi (error / 오류) tracking và hiệu năng (performance / 성능) telemetry. Một lỗi (error / 오류) sự kiện (event / 이벤트) hữu ích có thể chứa bản phát hành (release / 릴리스) phiên bản (version / 버전), tuyến (route / 경로), tính năng (feature / 기능), pseudonymous session/người dùng (user / 사용자) identifier nếu chính sách (policy / 정책) cho phép, correlation/yêu cầu (request / 요청) ID, thành phần (component / 컴포넌트) ranh giới (boundary / 경계), ngăn xếp (stack / 스택), trình duyệt (browser / 브라우저)/thiết bị (device / 장치) và mạng (network / 네트워크) ngữ cảnh (context / 맥락).

Không log đơn vị từ (token / 토큰), password, PII nhạy cảm hoặc toàn bộ form payload. lỗi (error / 오류) ranh giới (boundary / 경계) nên report unexpected kết xuất (render / 렌더링) lỗi (error / 오류) nhưng tránh duplicate flood.

## 31. Testing pyramid ở quy mô (scale / 규모) lớn

Một nền tảng (platform / 플랫폼) trưởng thành thường có:

```text
Static      -> TypeScript, ESLint, React/Compiler lint
Unit        -> domain functions, reducers
Component   -> accessible interaction
Integration -> feature + network mock
E2E         -> critical journeys
Visual      -> design system/pages
Performance -> budget regression
A11y        -> automated + manual
```

Mục tiêu là confidence/thời gian (time / 시간) ratio, không phải số kiểm thử (test / 테스트) tối đa.

## 32. khả năng tiếp cận (accessibility / 접근성) quản trị (governance / 거버넌스)

Ở organization quy mô (scale / 규모), khả năng tiếp cận (accessibility / 접근성) phải được encode vào thành phần nguyên thủy (primitive / 기본 요소)/thiết kế (design / 설계) hệ thống (system / 시스템) và CI thay vì phụ thuộc từng nhà phát triển (developer / 개발자) nhớ ARIA. thiết kế (design / 설계) hệ thống (system / 시스템) nên cung cấp Dialog, Menu, Tabs, Tooltip, Combobox có hành vi (behavior / 동작) accessible.

PR checklist nên bao gồm keyboard, focus và accessible name. Automated khả năng tiếp cận (accessibility / 접근성) kiểm thử (test / 테스트) chỉ bắt một phần lỗi; manual testing vẫn cần.

## 33. Internationalization

React chỉ kết xuất (render / 렌더링) văn bản (text / 텍스트); i18n cần kiến trúc (architecture / 아키텍처) riêng. Cần xử lý translation message, plural, number/currency, date/thời gian (time / 시간)/timezone, RTL, văn bản (text / 텍스트) expansion, locale tuyến (route / 경로) và máy chủ (server / 서버)/máy khách (client / 클라이언트) locale consistency.

Không nối string kiểu:

```js
`${count} items`
```

nếu cần plural đa ngôn ngữ. Dùng message formatter. SSR/hydration phải dùng locale/timezone nhất quán hoặc có kết xuất (render / 렌더링) chiến lược (strategy / 전략) rõ.

## 34. Forms ở quy mô (scale / 규모) lớn

Large form không nhất thiết dùng một trạng thái (state / 상태) đối tượng (object / 객체) khổng lồ khiến toàn form kết xuất (render / 렌더링) mỗi keystroke. Có thể dùng uncontrolled/bản địa (native / 네이티브) FormData, field-level subscription, lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증), máy chủ (server / 서버) Actions hoặc máy trạng thái (state machine / 상태 머신) cho multi-step luồng (flow / 흐름).

Async kiểm tra hợp lệ (validation / 검증) cần debounce/cancel. kiểm tra hợp lệ (validation / 검증) lược đồ (schema / 스키마) có thể dùng chung máy khách (client / 클라이언트)/máy chủ (server / 서버) nếu hợp lý, nhưng authorization luôn ở máy chủ (server / 서버). lỗi (error / 오류) summary và focus tới trường dữ liệu (field / 필드) lỗi là khả năng tiếp cận (accessibility / 접근성) yêu cầu (requirement / 요구사항) quan trọng.

## 35. React + TypeScript advanced patterns

Polymorphic thành phần (component / 컴포넌트):

```tsx
type BoxProps<T extends React.ElementType> = {
  as?: T;
  children?: React.ReactNode;
} & Omit<
  React.ComponentPropsWithoutRef<T>,
  "as" | "children"
>;

function Box<T extends React.ElementType = "div">(
  props: BoxProps<T>
) {
  const { as, children, ...rest } = props;
  const Component = as ?? "div";
  return <Component {...rest}>{children}</Component>;
}
```

Mẫu (pattern / 패턴) mạnh nhưng kiểu (type / 타입) độ phức tạp (complexity / 복잡도) cao; chỉ dùng khi thiết kế (design / 설계) hệ thống (system / 시스템) thật sự cần.

Discriminated prop union:

```tsx
type AlertProps =
  | { kind: "success"; retry?: never }
  | { kind: "error"; retry: () => void };
```

Generic danh sách (list / 목록):

```tsx
type ListProps<T> = {
  items: T[];
  getKey: (item: T) => React.Key;
  renderItem: (item: T) => React.ReactNode;
};
```

Generic lớp trừu tượng (abstraction / 추상화) chỉ nên dùng khi có reuse thật; ứng dụng (application / 애플리케이션) lĩnh vực (domain / 도메인) mã (code / 코드) không cần generic hóa mọi thứ.

## 36. API stability và ngữ nghĩa (semantic / 의미적) versioning

Công khai (public / 공개) thành phần (component / 컴포넌트) API là đặc tả hợp đồng (contract / 계약). Breaking thay đổi (change / 변경) không chỉ là đổi prop name. Thay DOM cấu trúc (structure / 구조), focus hành vi (behavior / 동작), default controlled chế độ (mode / 모드), CSS specificity hoặc sự kiện (event / 이벤트) timing cũng có thể break bên tiêu thụ (consumer / 소비자).

Thiết kế (design / 설계) hệ thống (system / 시스템) cần changelog, di chuyển (migration / 마이그레이션) guide và codemod cho breaking thay đổi (change / 변경) lớn. cờ tính năng (feature flag / 기능 플래그)/canary triển khai (deployment / 배포) giảm blast radius.

## 37. cấp cao (senior / 시니어)/Master coding idioms

### Derive, do not synchronize

Nếu giá trị (value / 값) tính được từ kết xuất (render / 렌더링) inputs, tính trực tiếp thay vì trạng thái (state / 상태) + tác động (effect / 효과).

### Sự kiện (event / 이벤트) lô-gic (logic / 논리) stays in sự kiện (event / 이벤트)

Nếu lô-gic (logic / 논리) xảy ra vì người dùng (user / 사용자) hành động (action / 동작), xử lý trong sự kiện (event / 이벤트)/hành động (action / 동작) thay vì trạng thái (state / 상태) flag + tác động (effect / 효과).

### Trạng thái (state / 상태) colocation

Trạng thái (state / 상태) ở gần bên tiêu thụ (consumer / 소비자) nhất, chỉ lift khi cần phối hợp.

### Composition over boolean explosion

Cho bên tiêu thụ (consumer / 소비자) ghép cấu trúc (structure / 구조) thay vì hàng chục boolean bố cục (layout / 레이아웃) props.

### Boundary-oriented kiến trúc (architecture / 아키텍처)

Tuyến (route / 경로), Suspense, lỗi (error / 오류), máy khách (client / 클라이언트)/máy chủ (server / 서버), dữ liệu (data / 데이터) và tính năng (feature / 기능) đều là ranh giới (boundary / 경계). ranh giới (boundary / 경계) rõ giúp kiểm soát thất bại (failure / 실패)/hiệu năng (performance / 성능)/bảo mật (security / 보안).

### Make impossible states impossible

Dùng reducer, discriminated union hoặc máy trạng thái (state machine / 상태 머신).

### Measure before memo

Không tối ưu theo intuition.

### Khung phần mềm (framework / 프레임워크) APIs are not React APIs

Bộ nhớ đệm (cache / 캐시)/revalidate/router ngữ nghĩa (semantics / 의미론) của một khung phần mềm (framework / 프레임워크) không nên được mô tả là hành vi (behavior / 동작) chung của React.

## 38. Anti-pattern danh mục (catalog / 카탈로그)

### Tác động (effect / 효과) như sự kiện (event / 이벤트) bus

Không nên:

```jsx
setShouldSave(true);

useEffect(() => {
  if (shouldSave) save();
}, [shouldSave]);
```

Thường nên gọi `save()` từ sự kiện (event / 이벤트)/hành động (action / 동작).

### Mirrored props

```jsx
const [value, setValue] = useState(propValue);
```

mà không có ngữ nghĩa (semantics / 의미론) cục bộ (local / 로컬) draft rõ.

### Toàn cục (global / 전역) mutable singleton

```js
export const state = {};
```

Thành phần (component / 컴포넌트) đọc trực tiếp rồi mong React tự biết cập nhật (update / 업데이트).

### Giant ngữ cảnh (context / 맥락)

Một provider chứa hàng chục trường dữ liệu (field / 필드) cập nhật (update / 업데이트) với tần suất khác nhau.

### Premature lớp trừu tượng (abstraction / 추상화)

Tạo khung phần mềm (framework / 프레임워크) generic sau use trường hợp (case / 사례) đầu tiên.

### Memo cargo cult

Mọi hàm (function / 함수) đều `useCallback`, mọi đối tượng (object / 객체) đều `useMemo`.

### Chỉ mục (index / 인덱스) key trong editable/reorderable danh sách (list / 목록)

Dễ gây định danh trạng thái (state identity / 상태 식별성) bug.

### Side tác động (effect / 효과) trong kết xuất (render / 렌더링)

Gọi API, analytics, mutate toàn cục (global / 전역).

### Trình duyệt (browser / 브라우저) API trong máy chủ (server / 서버) kết xuất (render / 렌더링)

Đọc `window`/`localStorage` không guard.

### Authentication-only UI

Ẩn nút nhưng máy chủ (server / 서버) không authorize.

## 38A. môi trường vận hành (production / 운영 환경) triển khai (deployment / 배포): bản dựng (build / 빌드) → canary → quay lui (rollback / 롤백)

Triển khai (deployment / 배포) React không chỉ là `npm run build`. SPA/static hosting cần asset hashing, bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) khác nhau giữa HTML entry và immutable JS/CSS, cùng lịch sử (history / 이력) fallback để deep link không 404. Giá trị môi trường (environment / 환경) bundle vào máy khách (client / 클라이언트) phải xem là công khai (public / 공개); secret chỉ ở máy chủ (server / 서버) thời gian chạy (runtime / 런타임).

SSR/RSC còn có máy chủ (server / 서버) thời gian chạy (runtime / 런타임), streaming, máy chủ (server / 서버)/máy khách (client / 클라이언트) manifests, bộ nhớ đệm (cache / 캐시)/vô hiệu hóa (invalidation / 무효화) và tính tương thích (compatibility / 호환성) giữa khung phần mềm (framework / 프레임워크) với React máy chủ (server / 서버) packages. CDN bộ nhớ đệm (cache / 캐시) key phải phân biệt công khai (public / 공개) với personalized dữ liệu (data / 데이터) để tránh cross-user leak.

Chuỗi xử lý (pipeline / 파이프라인) môi trường vận hành (production / 운영 환경) nên có lint/typecheck/kiểm thử (test / 테스트)/bản dựng (build / 빌드), phụ thuộc (dependency / 의존성)/bảo mật (security / 보안) scan, khả năng tiếp cận (accessibility / 접근성)/hiệu năng (performance / 성능) checks cho trọng yếu (critical / 중요) luồng (flow / 흐름), preview/canary, bản phát hành (release / 릴리스) ID cho nguồn (source / 소스) maps/logs, health check, lỗi (error / 오류)/Web Vitals monitoring và quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물) known-good. cờ tính năng (feature flag / 기능 플래그) tách deploy mã (code / 코드) khỏi enable hành vi (behavior / 동작). Khi migrate CRA → Vite/khung phần mềm (framework / 프레임워크) cần kiểm tra (audit / 감사) env ngữ nghĩa (semantics / 의미론), công khai (public / 공개) đường dẫn (path / 경로), router fallback, động (dynamic / 동적) imports, dịch vụ (service / 서비스) worker/PWA, kiểm thử (test / 테스트) runner và triển khai (deployment / 배포) cơ sở (base / 기반) đường dẫn (path / 경로).

## 38B. kiến trúc vận hành (production architecture / 운영 아키텍처) phải có ranh giới (boundary / 경계), ngân sách (budget / 예산) và khôi phục (recovery / 복구) đường dẫn (path / 경로)

Một React kiến trúc vận hành (production architecture / 운영 아키텍처) nên mô tả rõ ít nhất năm ranh giới (boundary / 경계): **kết xuất (render / 렌더링) ranh giới (boundary / 경계)** (component/Suspense/Error Boundary), **quyền sở hữu trạng thái (state ownership / 상태 소유권) ranh giới (boundary / 경계)**, **mạng (network / 네트워크)/bộ nhớ đệm (cache / 캐시) ranh giới (boundary / 경계)**, **máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới mô-đun (module boundary / 모듈 경계)**, và **triển khai (deployment / 배포)/khả năng quan sát (observability / 관측 가능성) ranh giới (boundary / 경계)**. Nếu mọi concern hội tụ ở gốc (root / 루트) provider hoặc một toàn cục (global / 전역) store, thất bại (failure / 실패) blast radius và vô hiệu hóa (invalidation / 무효화) phạm vi (scope / 범위) thường quá lớn.

Mỗi trọng yếu (critical / 중요) luồng (flow / 흐름) nên có ngân sách (budget / 예산) và khôi phục (recovery / 복구) đường dẫn (path / 경로): loading bao lâu thì đổi UX, thử lại (retry / 재시도) ở đâu, stale dữ liệu (data / 데이터) được giữ bao lâu, lỗi nào người dùng (user / 사용자) có thể sửa, lỗi nào cần report, bundle/tương tác (interaction / 상호작용) ngân sách (budget / 예산) là bao nhiêu, quay lui (rollback / 롤백) phiên bản (version / 버전) nào là known-good. cờ tính năng (feature flag / 기능 플래그) giúp tách deploy khỏi bản phát hành (release / 릴리스) hành vi (behavior / 동작); bản phát hành (release / 릴리스) ID nối bản đồ mã nguồn (source map / 소스 맵), log và chỉ số (metric / 지표) với đúng sản phẩm tạo ra (artifact / 산출물).

Môi trường vận hành (production / 운영 환경) rà soát (review / 검토) cũng phải kiểm tra bộ nhớ đệm (cache / 캐시) quyền sở hữu (ownership / 소유권). trình duyệt (browser / 브라우저)/CDN/máy chủ (server / 서버)/truy vấn (query / 쿼리) bộ nhớ đệm (cache / 캐시) cùng tồn tại có thể tạo nhiều lớp stale dữ liệu (data / 데이터). Không bộ nhớ đệm (cache / 캐시) personalized HTML/dữ liệu (data / 데이터) bằng key chung. Mutation phải xác định vô hiệu hóa (invalidation / 무효화) hoặc optimistic reconciliation rõ; nếu không, UI có thể “nhanh” nhưng sai consistency.

## 39. kiến trúc (architecture / 아키텍처) rà soát (review / 검토) checklist

Khi rà soát (review / 검토) tính năng (feature / 기능) React môi trường vận hành (production / 운영 환경), phải trả lời được các câu dưới đây bằng kiến trúc (architecture / 아키텍처) cụ thể thay vì chỉ tên thư viện (library / 라이브러리).

**dữ liệu (data / 데이터):** nguồn chuẩn (source of truth / 정본) ở đâu, bộ nhớ đệm (cache / 캐시) ở đâu, vô hiệu hóa (invalidation / 무효화) ra sao, quyền sở hữu (ownership / 소유권) là ai.

**Rendering:** CSR/SSR/RSC, ranh giới (boundary / 경계) nào suspend, tuyến (route / 경로) nào mã (code / 코드) split.

**trạng thái (state / 상태):** cục bộ (local / 로컬)/URL/form/máy chủ (server / 서버)/toàn cục (global / 전역) nào thực sự cần.

**Effects:** mỗi tác động (effect / 효과) đang synchronize tài nguyên (resource / 자원) nào.

**Errors:** expected lỗi (error / 오류) hiển thị đâu, unexpected lỗi (error / 오류) ranh giới (boundary / 경계) nào bắt.

**bảo mật (security / 보안):** authn/authz/kiểm tra hợp lệ (validation / 검증) ở máy chủ (server / 서버) nào.

**hiệu năng (performance / 성능):** đường găng (critical path / 임계 경로), bundle, danh sách (list / 목록), tương tác (interaction / 상호작용) và profiler bằng chứng (evidence / 증거).

**khả năng tiếp cận (accessibility / 접근성):** keyboard, focus, ngữ nghĩa (semantic / 의미적), live announcement.

**Testing:** rủi ro (risk / 위험) nào được kiểm thử (test / 테스트) ở tầng (layer / 계층) nào.

**Versioning:** API có tương thích React/khung phần mềm (framework / 프레임워크) mục tiêu (target / 대상) không.

## 40. Lộ trình sau React cốt lõi (core / 핵심)

SPA enterprise nên học sâu router, TanStack truy vấn (query / 쿼리) hoặc server-state equivalent, form thư viện (library / 라이브러리), khả năng tiếp cận (accessibility / 접근성) primitives, TypeScript, testing và khả năng quan sát (observability / 관측 가능성).

Full-stack React nên học khung phần mềm (framework / 프레임워크) có SSR/RSC/streaming phù hợp và hiểu caching/triển khai (deployment / 배포) của chính khung phần mềm (framework / 프레임워크) đó.

Thiết kế (design / 설계) hệ thống (system / 시스템) engineer nên học ARIA Authoring Practices, headless primitives, CSS kiến trúc (architecture / 아키텍처), tokens, gói (package / 패키지) publishing và visual regression.

Hiệu năng (performance / 성능) engineer nên học trình duyệt (browser / 브라우저) rendering, cốt lõi (core / 핵심) Web Vitals, hiệu năng (performance / 성능) API, mạng (network / 네트워크) giao thức (protocol / 프로토콜), bundler và profiling.

React bản địa (native / 네이티브) cần học host môi trường (environment / 환경) riêng; DOM kiến thức (knowledge / 지식) không áp dụng nguyên xi.

## 41. Bản đồ API quan trọng

| Nhóm | API / thành phần | Vai trò |
|---|---|---|
| thành phần (component / 컴포넌트) | hàm (function / 함수) thành phần (component / 컴포넌트), Fragment | Mô tả UI |
| trạng thái (state / 상태) | `useState`, `useReducer` | cục bộ (local / 로컬) trạng thái (state / 상태) / chuyển tiếp (transition / 전이) |
| ngữ cảnh (context / 맥락) | `createContext`, `useContext`, `use` | Dữ liệu theo subtree |
| tác động (effect / 효과) | `useEffect`, `useLayoutEffect`, `useEffectEvent`, `useInsertionEffect` | bên ngoài (external / 외부) synchronization |
| Ref | `useRef`, `useImperativeHandle` | Mutable giá trị (value / 값) / imperative API |
| định danh (identity / 식별자) | `key`, `useId` | thành phần (component / 컴포넌트) định danh (identity / 식별자) / stable ID |
| Memoization | `memo`, `useMemo`, `useCallback` | Manual tối ưu hóa (optimization / 최적화) |
| tính đồng thời (concurrency / 동시성) | `startTransition`, `useTransition`, `useDeferredValue` | Priority |
| Async UI | `Suspense`, `lazy`, `use` | Suspension / code-data coordination |
| Actions | `useActionState`, `useOptimistic`, form hành động (action / 동작) | Mutation workflow |
| React DOM form | `useFormStatus` | Form pending/status |
| DOM | `createPortal` | kết xuất (render / 렌더링) sang host nút (node / 노드) khác |
| gốc (root / 루트) | `createRoot`, `hydrateRoot` | máy khách (client / 클라이언트) gốc (root / 루트) / hydration |
| máy chủ (server / 서버) DOM | `renderToPipeableStream`, `renderToReadableStream`, prerender/resume family | SSR/streaming |
| bên ngoài (external / 외부) store | `useSyncExternalStore` | Store ngoài React |
| RSC | `"use client"`, `"use server"` | máy khách (client / 클라이언트) ranh giới (boundary / 경계) / máy chủ (server / 서버) hàm (function / 함수) |
| React 19.2+ | `<Activity />` | Visible/hidden activity subtree |
| React 19.3 | View Transitions, Fragment refs và năng lực (capability / 역량) mới theo bản phát hành (release / 릴리스) | hiện đại (modern / 현대적) UI/máy chủ (server / 서버) primitives |
| Build-time | React trình biên dịch (compiler / 컴파일러) 1.0 | Automatic memoization/tối ưu hóa (optimization / 최적화) |

## Versioning principles cần mang theo sau khi học xong

React versioning nên được nhìn như một ma trận năng lực (capability / 역량) chứ không phải một chuỗi tutorial riêng biệt. thành phần (component / 컴포넌트)/props/trạng thái (state / 상태)/purity vẫn là nền xuyên phiên bản (version / 버전); React 18 thay đổi nền scheduling/gốc (root / 루트); React 19 mở rộng async/máy chủ (server / 서버) mô hình (model / 모델); minor 19.2 và 19.3 tiếp tục thêm API công khai (public API / 공개 API). Vì vậy lộ trình đúng là học mô hình tư duy (mental model / 사고 모델) bền vững trước, sau đó gắn phiên bản (version / 버전) vào đúng API.

Khi gặp mã (code / 코드) lạ, hãy kiểm tra theo thứ tự: `react` → `react-dom` → khung phần mềm (framework / 프레임워크) → trình biên dịch (compiler / 컴파일러)/bundler → thư viện (library / 라이브러리) peer phụ thuộc (dependency / 의존성) → patch/bảo mật (security / 보안) advisory. Cách này đáng tin hơn việc nhớ “React 19 có gì” vì ecosystem và patch mức (level / 수준) có thể thay đổi độc lập.

## 42. Kết luận

Master React không phải nhớ càng nhiều Hook càng tốt. Cốt lõi là hiểu React như một hệ thống kết xuất (render / 렌더링) khai báo có invariants về purity, định danh (identity / 식별자), quyền sở hữu (ownership / 소유권) và synchronization.

Người mới thường hỏi “Hook nào giải quyết việc này?”. Engineer có kinh nghiệm hơn hỏi “dữ liệu này thuộc ai, chuyển tiếp (transition / 전이) nào xảy ra, hệ thống bên ngoài (external system / 외부 시스템) nào cần synchronize, ranh giới (boundary / 경계) nào chịu trách nhiệm và thất bại (failure / 실패)/hiệu năng (performance / 성능)/bảo mật (security / 보안) ngữ nghĩa (semantics / 의미론) là gì?”. Khi câu hỏi thay đổi theo hướng đó, React thường trở nên đơn giản hơn vì Hook chỉ còn là công cụ biểu đạt kiến trúc (architecture / 아키텍처).

## Phiên bản (version / 버전) Notes

Bộ tài liệu lấy React 19.3 làm baseline. React 19.3 phát hành ngày 09/09/2026. React trình biên dịch (compiler / 컴파일러) 1.0 đã stable và production-ready. máy chủ (server / 서버) Components trong React 19 có mô hình (model / 모델) ổn định cho ứng dụng (application / 애플리케이션) usage, trong khi APIs dành cho bundler/khung phần mềm (framework / 프레임워크) implement RSC có versioning các ràng buộc (constraints / 제약조건들) riêng. bảo mật (security / 보안) advisory phải được theo dõi theo patch/minor thực tế, không chỉ major phiên bản (version / 버전).

## Nguồn chuẩn để kiểm chứng

Ưu tiên tài liệu chính thức React: React Versions, React Blog bản phát hành (release / 릴리스) notes, Learn, API tham chiếu (reference / 참조), React DOM máy chủ (server / 서버), React máy chủ (server / 서버) Components và React trình biên dịch (compiler / 컴파일러). Với khung phần mềm (framework / 프레임워크), phải đọc tài liệu đúng phiên bản (version / 버전) của khung phần mềm (framework / 프레임워크) vì router, bộ nhớ đệm (cache / 캐시), triển khai (deployment / 배포) và RSC tích hợp (integration / 통합) không hoàn toàn thuộc React cốt lõi (core / 핵심).

> **Bàn giao:** Sau **Nguồn chuẩn để kiểm chứng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 index](./00_index.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
