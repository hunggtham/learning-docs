# React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**. Route đi từ rendering/Fiber mental model → render/commit phases → concurrency, Suspense và server/client boundaries → architecture, performance và security → production failure modes, để invariants nối các quyết định nâng cao.

> React 19.3 là mốc stable hiện hành cho API mới; tệp (file / 파일) này tập trung invariants xuyên phiên bản (version / 버전): reconciliation/định danh (identity / 식별자), tính đồng thời (concurrency / 동시성), Suspense, máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계), kiến trúc (architecture / 아키텍처), hiệu năng (performance / 성능), bảo mật (security / 보안) và môi trường vận hành (production / 운영 환경) practices.

## 1. kết xuất (render / 렌더링) kiến trúc (architecture / 아키텍처) và Fiber mô hình tư duy (mental model / 사고 모델)

React không cập nhật DOM ngay khi setter được gọi. Nó schedule công việc (work / 작업), thực hiện kết xuất (render / 렌더링) để tính cây UI mới, rồi lần ghi nhận (commit / 커밋) thay đổi host cần thiết. hiện thực (implementation / 구현) hiện đại dùng Fiber làm unit-of-work cấu trúc (structure / 구조) để hỗ trợ scheduling. ứng dụng (application / 애플리케이션) nhà phát triển (developer / 개발자) không nên phụ thuộc trường dữ liệu (field / 필드)/nội bộ (internal / 내부) API của Fiber, nhưng phải hiểu ba hệ quả: kết xuất (render / 렌더링) có thể chạy lại; kết xuất (render / 렌더링) có thể bắt đầu rồi bị bỏ; và chỉ lần ghi nhận (commit / 커밋) mới làm thay đổi DOM trở thành hiệu lực.

Do đó kết xuất (render / 렌더링) phải pure. Không gửi yêu cầu (request / 요청) thanh toán, mutate toàn cục (global / 전역) đối tượng (object / 객체), log kiểm tra (audit / 감사) hay điều khiển DOM bên ngoài trong kết xuất (render / 렌더링).

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **2. kết xuất (render / 렌더링) phase và lần ghi nhận (commit / 커밋) phase** gom các mảnh từ **1. kết xuất (render / 렌더링) kiến trúc (architecture / 아키텍처) và Fiber mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **3. định danh trạng thái (state identity / 상태 식별성), preserve và reset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. kết xuất (render / 렌더링) phase và lần ghi nhận (commit / 커밋) phase

Kết xuất (render / 렌더링) phase chạy thành phần (component / 컴포넌트) hàm (function / 함수) và tính React element cây (tree / 트리). lần ghi nhận (commit / 커밋) phase áp dụng host changes, ref và tác động (effect / 효과) theo timing tương ứng.

```jsx
function Product({ product }) {
  const price = formatPrice(product.price);
  return <strong>{price}</strong>;
}
```

`formatPrice` nên pure. Analytics do người dùng (user / 사용자) click đặt ở sự kiện (event / 이벤트). Analytics gắn với việc screen được đồng bộ/hiển thị có thể dùng tác động (effect / 효과) tùy ngữ nghĩa (semantics / 의미론). cấp cao (senior / 시니어) rà soát mã (code review / 코드 리뷰) nên hỏi “lô-gic (logic / 논리) này thuộc kết xuất (render / 렌더링), sự kiện (event / 이벤트) hay synchronization?” trước khi hỏi “dùng Hook nào?”.

> **Chuyển mạch:** Render/commit phases xác định khi UI work có thể restart; state identity quyết định state nào được preserve/reset qua các lần đó. Concurrent rendering tiếp theo đặt hai constraint này dưới scheduling thực tế.

## 3. định danh trạng thái (state identity / 상태 식별성), preserve và reset

Trạng thái (state / 상태) được lưu theo định danh (identity / 식별자) của thành phần (component / 컴포넌트) trong cây React, không “nằm trong hàm (function / 함수)”.

```jsx
{mode === "a"
  ? <Editor key="a" />
  : <Editor key="b" />}
```

Hai key khác nhau ép định danh (identity / 식별자) khác và reset cục bộ (local / 로컬) trạng thái (state / 상태).

Nếu chỉ đổi prop:

```jsx
<Editor documentId={documentId} />
```

Trạng thái (state / 상태) thường được preserve. Nếu draft phải reset khi document đổi, có thể mô hình (model / 모델) draft theo ID, chủ động reset hoặc `key={documentId}` nếu muốn remount subtree. `key` là công cụ định danh (identity / 식별자), không chỉ là danh sách (list / 목록) warning.

> **Chuyển mạch:** State identity bảo vệ mental model khi render bị gián đoạn; concurrent rendering quyết định work nào được ưu tiên hoặc bỏ. Reconciliation tiếp theo giải thích cách tree diff giữ invariant trong quá trình đó.

## 4. Concurrent rendering

Concurrent React không có nghĩa thành phần (component / 컴포넌트) JavaScript chạy multi-thread. Nó nghĩa React có thể làm kết xuất (render / 렌더링) công việc (work / 작업) theo cách interruptible/prioritized. cập nhật (update / 업데이트) có priority khác nhau, nên một kết xuất (render / 렌더링) non-urgent có thể bị urgent đầu vào (input / 입력) chen vào.

Tính đồng thời (concurrency / 동시성) API không thay kiến trúc tốt. Trước tiên giảm công việc (work / 작업), tránh waterfall và profile.

> **Chuyển mạch:** Concurrent scheduling quyết định khi nào work được tiếp tục; reconciliation quyết định tree nào có thể commit mà không phá identity. `useTransition` tiếp theo cho application một cách đánh dấu non-urgent work.

## 4A. Reconciliation dưới concurrent rendering

Concurrent rendering không thay định danh (identity / 식별자) rules; nó thay cách kết xuất (render / 렌더링) công việc (work / 작업) được schedule. React có thể bắt đầu, pause, restart hoặc abandon kết xuất (render / 렌더링) trước lần ghi nhận (commit / 커밋), nên kết xuất (render / 렌더링) phải pure. Reconciliation trả lời cây (tree / 트리) nào là cùng định danh (identity / 식별자) và cần thay gì; scheduling trả lời công việc (work / 작업) nào ưu tiên và có thể ngắt. bên ngoài (external / 외부) store cần snapshot nhất quán với tính đồng thời (concurrency / 동시성), là lý do React 18 có `useSyncExternalStore` thay cho subscription tác động (effect / 효과) tự chế dễ tearing.

> **Chuyển mạch:** Concurrent reconciliation tách render work; `useTransition`/`startTransition` tiếp theo hạ priority cho update không khẩn cấp, còn `useDeferredValue` trì hoãn giá trị đọc.

## 5. `useTransition` và `startTransition`
Phần này nối mạch bài học với “5. `useTransition` và `startTransition`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
const [isPending, startTransition] = useTransition();

function handleChange(event) {
  const value = event.target.value;
  setQuery(value); // urgent

  startTransition(() => {
    setFilter(value); // non-urgent
  });
}
```

Chuyển tiếp (transition / 전이) không phải debounce. Debounce trì hoãn theo thời gian; chuyển tiếp (transition / 전이) biểu đạt priority. `startTransition` standalone dùng khi không cần pending trạng thái (state / 상태) tại caller.

> **Chuyển mạch:** `startTransition` lowers update priority; `useDeferredValue` lets a consumer lag, while debounce controls input frequency rather than render priority.

## 6. `useDeferredValue`
Phần này nối mạch bài học với “6. `useDeferredValue`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
const deferredQuery = useDeferredValue(query);
return <SearchResults query={deferredQuery} />;
```

Đầu vào (input / 입력) cập nhật ngay theo `query`, subtree nặng có thể dùng giá trị (value / 값) cũ tạm thời. chuyển tiếp (transition / 전이) phù hợp khi bạn kiểm soát setter; deferred giá trị (value / 값) hữu ích khi giá trị (value / 값) đến từ parent hoặc cần defer bên tiêu thụ (consumer / 소비자).

> ### phiên bản (version / 버전) ghi chú (note / 노트) — chuyển tiếp (transition / 전이) là nền tảng React 18
>
> `startTransition`, `useTransition` và `useDeferredValue` thuộc wave React 18. Chúng không phải “React 19 tối ưu hóa (optimization / 최적화)”. React 19 tiếp tục xây Actions/Suspense/máy chủ (server / 서버) features trên concurrent foundations này, nên hiểu chuyển tiếp (transition / 전이) trước khi học Actions và Activity sẽ giúp luồng học tự nhiên hơn.

> **Chuyển mạch:** Transition changes scheduling priority, deferred value changes what a consumer reads, and debounce changes event frequency; Suspense then coordinates async reveal.

## 6A. chuyển tiếp (transition / 전이), deferred giá trị (value / 값) và debounce giải quyết ba vấn đề khác nhau

`startTransition`/`useTransition` gắn **priority ngữ nghĩa (semantic / 의미적)** cho cập nhật (update / 업데이트): đầu vào (input / 입력) trực tiếp vẫn urgent, còn kết xuất (render / 렌더링) kết quả nặng có thể non-urgent. `useDeferredValue` cho bên tiêu thụ (consumer / 소비자) dùng một giá trị (value / 값) chậm hơn nguồn (source / 소스) hiện tại khi caller không kiểm soát setter. Debounce lại là kỹ thuật thời gian: chỉ thực hiện công việc sau một khoảng yên lặng. Ba công cụ có thể kết hợp nhưng không thay thế nhau.

Ví dụ tìm kiếm (search / 검색) box có thể cập nhật văn bản (text / 텍스트) ngay, defer kết xuất (render / 렌더링) danh sách lớn để typing mượt, đồng thời debounce mạng (network / 네트워크) yêu cầu (request / 요청) để giảm traffic. Nếu chỉ debounce toàn bộ trạng thái (state / 상태) đầu vào (input / 입력), UI có thể cảm giác lag; nếu chỉ chuyển tiếp (transition / 전이) yêu cầu (request / 요청), bạn vẫn có thể gửi quá nhiều HTTP calls. cấp cao (senior / 시니어) thiết kế (design / 설계) phải tách **responsiveness**, **kết xuất (render / 렌더링) priority** và **I/O tỷ lệ (rate / 비율) limiting**.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **7. Suspense nâng cao** tiếp nhận điểm tựa từ **6A. chuyển tiếp (transition / 전이), deferred giá trị (value / 값) và debounce giải quyết ba vấn đề khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. use** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Suspense nâng cao
Phần này nối mạch bài học với “7. Suspense nâng cao”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
<Suspense fallback={<Skeleton />}>
  <Profile />
</Suspense>
```

Suspense là ranh giới (boundary / 경계) cho rendering có thể suspend qua cơ chế (mechanism / 메커니즘) được React/khung phần mềm (framework / 프레임워크) hỗ trợ. ranh giới (boundary / 경계) placement là quyết định UX. Một ranh giới (boundary / 경계) quá cao làm cả màn hình biến thành spinner; quá nhiều ranh giới (boundary / 경계) nhỏ tạo “popcorn loading”. Skeleton nên giữ bố cục (layout / 레이아웃) ổn định để giảm bố cục (layout / 레이아웃) shift.

Suspense kết hợp chuyển tiếp (transition / 전이) cho phép giữ content cũ trong khi content mới chuẩn bị tùy kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **8. use** tiếp nhận điểm tựa từ **7. Suspense nâng cao** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Actions và form APIs React 19** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. `use`

React 19 có `use(resource)` để đọc Promise hoặc ngữ cảnh (context / 맥락) theo ngữ nghĩa (semantics / 의미론) React hỗ trợ.

```jsx
function Comments({ commentsPromise }) {
  const comments = use(commentsPromise);
  return comments.map(c => <p key={c.id}>{c.text}</p>);
}
```

Promise pending làm thành phần (component / 컴포넌트) suspend. Không tạo Promise mới vô điều kiện mỗi máy khách (client / 클라이언트) kết xuất (render / 렌더링) vì dễ gây suspend vòng lặp (loop / 루프)/waterfall. Promise nên đến từ bộ nhớ đệm (cache / 캐시)/khung phần mềm (framework / 프레임워크)/máy chủ (server / 서버) hoặc một nguồn (source / 소스) có định danh (identity / 식별자)/vòng đời (lifecycle / 생명주기) ổn định.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — `use` là React 19
>
> API `use` thuộc React 19. Nếu dự án (project / 프로젝트) React 18, bạn không thể bản sao (copy / 복사) mã (code / 코드) `use(promise)` từ docs React mới vào trực tiếp. Ngoài ra `use` không biến mọi Promise tùy ý thành dữ liệu (data / 데이터) tầng (layer / 계층) môi trường vận hành (production / 운영 환경); cách tạo/bộ nhớ đệm (cache / 캐시) Promise và tích hợp (integration / 통합) với khung phần mềm (framework / 프레임워크) vẫn quyết định tính đúng đắn.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **9. Actions và form APIs React 19** tiếp nhận điểm tựa từ **8. use** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. useActionState** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Actions và form APIs React 19

React 19 mở rộng async mutation qua Actions. Trong môi trường hỗ trợ, form `action` có thể nhận hàm (function / 함수):

```jsx
<form action={saveAction}>
  <input name="title" />
  <button type="submit">Lưu</button>
</form>
```

Không phải cứ viết `"use server"` trong Vite SPA là có máy chủ (server / 서버) thời gian chạy (runtime / 런타임). máy chủ (server / 서버) Actions/Functions cần RSC/khung phần mềm (framework / 프레임워크) tích hợp (integration / 통합).

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **10. useActionState** tiếp nhận điểm tựa từ **9. Actions và form APIs React 19** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. useFormStatus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. `useActionState`
Phần này nối mạch bài học với “10. `useActionState`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
const [state, submitAction, isPending] =
  useActionState(action, initialState);

return (
  <form action={submitAction}>
    <input name="email" />
    <button disabled={isPending}>
      {isPending ? "Đang gửi..." : "Gửi"}
    </button>
    {state?.error && <p>{state.error}</p>}
  </form>
);
```

Dùng khi kết quả mutation cần trở thành form/hành động (action / 동작) trạng thái (state / 상태) có pending/lỗi (error / 오류)/kết quả (result / 결과) rõ ràng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **11. useFormStatus** tiếp nhận điểm tựa từ **10. useActionState** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. useOptimistic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. `useFormStatus`

Từ `react-dom`:

```jsx
import { useFormStatus } from "react-dom";

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? "Đang lưu..." : "Lưu"}
    </button>
  );
}
```

Thành phần (component / 컴포넌트) đọc status phải nằm trong form ngữ cảnh (context / 맥락) đúng cấu trúc.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **12. useOptimistic** tiếp nhận điểm tựa từ **11. useFormStatus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. useEffectEvent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. `useOptimistic`
Phần này nối mạch bài học với “12. `useOptimistic`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
const [optimisticMessages, addOptimisticMessage] =
  useOptimistic(
    messages,
    (current, newMessage) => [
      ...current,
      { ...newMessage, sending: true },
    ]
  );
```

Optimistic UI chỉ nên dùng khi quay lui (rollback / 롤백)/reconciliation rõ. Với giao dịch tài chính hoặc thao tác không thể hoàn tác, UI phải phân biệt “đã gửi yêu cầu” với “đã xác nhận thành công”.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **13. useEffectEvent** tiếp nhận điểm tựa từ **12. useOptimistic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. <Activity />** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. `useEffectEvent`

React 19.2 thêm `useEffectEvent` để tách lô-gic (logic / 논리) event-like không reactive khỏi tác động (effect / 효과) synchronization.

```jsx
const onConnected = useEffectEvent(() => {
  showNotification("Connected", theme);
});

useEffect(() => {
  const connection = createConnection(roomId);
  connection.on("connected", onConnected);
  connection.connect();
  return () => connection.disconnect();
}, [roomId]);
```

Liên kết (connection / 연결) phụ thuộc `roomId`; notification đọc `theme` mới nhất mà không reconnect chỉ vì theme đổi. Không dùng API này để lách phụ thuộc (dependency / 의존성) sai.

### 13A. tác động (effect / 효과) sự kiện (event / 이벤트) là sự kiện (event / 이벤트) do tác động (effect / 효과) phát ra, không phải “callback ổn định để khỏi thêm phụ thuộc (dependency / 의존성)”

Điểm khó của `useEffectEvent` là nó giải quyết **hai loại reactivity khác nhau trong cùng một tác động (effect / 효과)**. Phần setup liên kết (connection / 연결) phải reactive theo `roomId`: đổi room thì tài nguyên (resource / 자원) bên ngoài phải disconnect/reconnect. Callback notification lại chỉ cần đọc `theme` mới nhất tại thời điểm sự kiện `connected` xảy ra; `theme` không phải cấu hình (configuration / 구성) của liên kết (connection / 연결). Nếu cho `theme` vào phụ thuộc (dependency / 의존성), đổi theme làm reconnect vô nghĩa. Nếu cố tình bỏ `theme` khỏi phụ thuộc (dependency / 의존성), closure có thể stale và linter mất khả năng bảo vệ.

Tác động (effect / 효과) sự kiện (event / 이벤트) tách hai ngữ nghĩa (semantics / 의미론) đó. Callback được khai báo bằng `useEffectEvent` luôn đọc props/trạng thái (state / 상태) mới nhất khi được gọi, nhưng chính tác động (effect / 효과) sự kiện (event / 이벤트) **không được đưa vào phụ thuộc (dependency / 의존성) array**. Nó cũng chỉ được khai báo trong cùng thành phần (component / 컴포넌트) hoặc Custom Hook với tác động (effect / 효과) sở hữu nó. Vì đây là đặc tả hợp đồng (contract / 계약) tính đúng đắn (correctness / 정확성), dự án (project / 프로젝트) dùng API này nên chạy phiên bản `eslint-plugin-react-hooks` đủ mới để linter hiểu tác động (effect / 효과) Events.

Một dấu hiệu dùng sai là bọc gần như mọi hàm (function / 함수) bằng `useEffectEvent` chỉ để phụ thuộc (dependency / 의존성) array ngắn lại. Hãy hỏi trước: “Đây có thật sự là một sự kiện (event / 이벤트) phát sinh từ synchronization tiến trình (process / 프로세스) không?” Nếu giá trị (value / 값) quyết định tài nguyên (resource / 자원) nào được mở, URL nào được subscribe, timer interval bao nhiêu hoặc observer theo dõi nút (node / 노드) nào, giá trị (value / 값) đó vẫn là phụ thuộc (dependency / 의존성) của tác động (effect / 효과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **14. <Activity />** tiếp nhận điểm tựa từ **13. useEffectEvent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. View Transitions trong React 19.3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. `<Activity />`

React 19.2 giới thiệu Activity để quản lý subtree visible/hidden theo ngữ nghĩa (semantics / 의미론) React hiểu, cho phép giữ trạng thái (state / 상태) trong những luồng (flow / 흐름) phù hợp thay vì unmount hoàn toàn.

```jsx
<Activity mode={tab === "messages" ? "visible" : "hidden"}>
  <Messages />
</Activity>
```

Khác conditional rendering vì conditional có thể unmount và mất trạng thái (state / 상태). API mới cần kiểm tra phiên bản (version / 버전) tính tương thích (compatibility / 호환성) trước khi dùng trong thư viện (library / 라이브러리) công khai (public / 공개).

### 14A. Hidden không có nghĩa “thành phần (component / 컴포넌트) vẫn chạy bình thường nhưng CSS `display:none`”

Khi Activity chuyển sang `hidden`, React ẩn children, unmount các tác động (effect / 효과) của subtree và trì hoãn các cập nhật (update / 업데이트) của phần ẩn tới lúc scheduler không còn việc quan trọng hơn. trạng thái (state / 상태) của subtree vẫn được giữ, nên khi quay lại `visible`, người dùng có thể nhận lại draft/đầu vào (input / 입력) trạng thái (state / 상태) thay vì bắt đầu từ đầu. Đây là điểm khác cả với conditional rendering — vốn unmount subtree — lẫn một wrapper CSS đơn thuần — vốn thường để subscriptions, timers và Effects tiếp tục chạy dù UI không nhìn thấy.

Mô hình tư duy (mental model / 사고 모델) hữu ích là **“preserve trạng thái (state / 상태), suspend active side effects, lower scheduling priority”**. Điều này làm Activity phù hợp cho tab/screen có khả năng quay lại, hoặc pre-render màn hình có khả năng được mở tiếp theo. Nhưng giữ trạng thái (state / 상태) và cây (tree / 트리) cũng tiêu tốn bộ nhớ (memory / 메모리); nếu subtree chứa dữ liệu lớn và xác suất quay lại thấp, unmount thật có thể rẻ hơn. Activity là một sự đánh đổi (trade-off / 트레이드오프) giữa resume độ trễ (latency / 지연 시간), background công việc (work / 작업) và bộ nhớ (memory / 메모리) footprint chứ không phải mặc định thay thế mọi `condition ? <Page /> : null`.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — React 19.2
>
> `useEffectEvent` và `<Activity />` được thêm ở **React 19.2**. Nếu gói (package / 패키지) khai hỗ trợ React 19.0+, không được import chúng vô điều kiện rồi kỳ vọng bên tiêu thụ (consumer / 소비자) 19.0/19.1 chạy được. Đây là ví dụ điển hình cho việc minor phiên bản (version / 버전) React 19 có thể bổ sung công khai (public / 공개) tính năng (feature / 기능) chứ không chỉ bug fix.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **15. View Transitions trong React 19.3** tiếp nhận điểm tựa từ **14. <Activity />** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Fragment refs trong React 19.3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. View Transitions trong React 19.3

React 19.3 đưa `<ViewTransition>` thành API stable để React phối hợp với trình duyệt (browser / 브라우저) View chuyển tiếp (transition / 전이) API khi UI enter, exit, thay đổi hoặc một named element được “share” giữa hai vị trí.

Điểm quan trọng là **không phải mọi trạng thái (state / 상태) cập nhật (update / 업데이트) đều animate**. React chỉ kích hoạt View chuyển tiếp (transition / 전이) khi thay đổi đó thuộc một chuyển tiếp (transition / 전이), ví dụ cập nhật (update / 업데이트) bên trong `startTransition`, reveal của Suspense hoặc cập nhật (update / 업데이트) đi qua `useDeferredValue`. Urgent cập nhật (update / 업데이트) không bị buộc chờ animation vì phản hồi trực tiếp với đầu vào (input / 입력) vẫn phải xuất hiện ngay.

```jsx
import {
  startTransition,
  ViewTransition,
} from "react";

function ProductSwitcher() {
  const [productId, setProductId] = useState("a");

  function openProduct(nextId) {
    startTransition(() => {
      setProductId(nextId);
    });
  }

  return (
    <>
      <ProductPicker onSelect={openProduct} />
      <ViewTransition>
        <ProductDetails productId={productId} />
      </ViewTransition>
    </>
  );
}
```

Default hành vi (behavior / 동작) là cross-fade; môi trường vận hành (production / 운영 환경) UI có thể cấu hình riêng enter/exit/cập nhật (update / 업데이트)/share và, khi cần, gắn **chuyển tiếp (transition / 전이) kiểu (type / 타입)** bằng `addTransitionType` để phân biệt nguyên nhân như next/previous. Đây là ngữ nghĩa (semantic / 의미적) tốt hơn việc animation mã (code / 코드) tự suy luận direction từ DOM cũ. Tuy vậy View chuyển tiếp (transition / 전이) hiện là DOM năng lực (capability / 역량): phải kiểm tra mức hỗ trợ trình duyệt (browser support / 브라우저 지원), tôn trọng `prefers-reduced-motion`, và đảm bảo tính đúng đắn (correctness / 정확성) không phụ thuộc animation có chạy hay không.

Cấp cao (senior / 시니어) rà soát (review / 검토) cũng cần kiểm tra interruption. người dùng (user / 사용자) có thể click tiếp khi chuyển tiếp (transition / 전이) trước chưa kết thúc, Suspense có thể reveal ở thời điểm khác dự kiến, hoặc điều hướng (navigation / 내비게이션) có thể thất bại (fail / 실패). Animation tầng (layer / 계층) phải là progressive enhancement bên trên trạng thái (state / 상태)/điều hướng (navigation / 내비게이션) kiến trúc (architecture / 아키텍처), không được trở thành nguồn chuẩn (source of truth / 정본).

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **16. Fragment refs trong React 19.3** tiếp nhận điểm tựa từ **15. View Transitions trong React 19.3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. External store và useSyncExternalStore** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Fragment refs trong React 19.3

Fragment refs giải quyết trường hợp một hành vi (behavior / 동작) cần thao tác với **một nhóm sibling DOM nodes** nhưng không muốn thêm wrapper chỉ để có ref, hoặc children đến từ thành phần (component / 컴포넌트) không expose raw DOM ref.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **17. External store và useSyncExternalStore** tiếp nhận điểm tựa từ **16. Fragment refs trong React 19.3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. useInsertionEffect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. External store và `useSyncExternalStore`
Phần này nối mạch bài học với “17. External store và `useSyncExternalStore`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
const snapshot = useSyncExternalStore(
  store.subscribe,
  store.getSnapshot,
  store.getServerSnapshot
);
```

API này cung cấp đặc tả hợp đồng (contract / 계약) để React đọc store ngoài React nhất quán với tính đồng thời (concurrency / 동시성)/SSR. thư viện (library / 라이브러리) trạng thái (state / 상태) management thường bọc nó. `getSnapshot` phải trả snapshot ổn định khi store không đổi; trả đối tượng (object / 객체) mới mọi lần dễ gây kết xuất (render / 렌더링) vòng lặp (loop / 루프) hoặc kết xuất (render / 렌더링) dư.

Một bên ngoài (external / 외부) store có thể thay đổi giữa lúc React đang kết xuất (render / 렌더링). Nếu thành phần (component / 컴포넌트) tự `subscribe` bằng tác động (effect / 효과) rồi đọc mutable singleton trực tiếp, hai thành phần (component / 컴포넌트) trong cùng một kết xuất (render / 렌더링) có thể quan sát hai phiên bản store khác nhau — hiện tượng thường được gọi là tearing. `useSyncExternalStore` tồn tại để store cung cấp snapshot/subscribe đặc tả hợp đồng (contract / 계약) mà React có thể phối hợp với concurrent rendering và hydration.

`getServerSnapshot` không chỉ là “fallback cho SSR”. Giá trị máy chủ (server / 서버) snapshot phải tương thích với initial máy khách (client / 클라이언트) snapshot dùng trong hydration; nếu máy chủ (server / 서버) trả `0` nhưng máy khách (client / 클라이언트) ngay lần đầu trả `42`, bạn lại tạo mismatch ở một tầng (layer / 계층) khó nhìn thấy. Với selector thư viện (library / 라이브러리), định danh (identity / 식별자) của snapshot và equality ngữ nghĩa (semantics / 의미론) cũng là một phần hiệu năng (performance / 성능) đặc tả hợp đồng (contract / 계약).

### 17A. `cacheSignal`: thời gian tồn tại (lifetime / 수명) của RSC bộ nhớ đệm (cache / 캐시) phải đi xuống I/O

React 19.2 thêm `cacheSignal()` cho **React máy chủ (server / 서버) Components**. Khi một thao tác (operation / 연산) nằm trong thời gian tồn tại (lifetime / 수명) của `cache()`, tín hiệu (signal / 신호) cho phép I/O bên dưới biết lúc kết quả bộ nhớ đệm (cache / 캐시) không còn được dùng — ví dụ kết xuất (render / 렌더링) đã hoàn thành, bị abort hoặc thất bại (fail / 실패) — để dừng yêu cầu (request / 요청)/tài nguyên (resource / 자원) tương ứng.

```jsx
import {
  cache,
  cacheSignal,
} from "react";

const load = cache(async url => {
  const response = await fetch(url, {
    signal: cacheSignal(),
  });

  return response.json();
});
```

Điểm bản chất không phải API `AbortSignal` mới, mà là **tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) propagation**. Nếu kết xuất (render / 렌더링)/cached computation bị hủy nhưng cơ sở dữ liệu (database / 데이터베이스)/HTTP lời gọi (call / 호출) vẫn chạy đến cùng, máy chủ (server / 서버) vẫn tiêu liên kết (connection / 연결), CPU và upstream quota cho kết quả không còn bên tiêu thụ (consumer / 소비자). Khi khung phần mềm (framework / 프레임워크) hỗ trợ, cancellation tín hiệu (signal / 신호) nên được truyền sâu qua máy khách (client / 클라이언트) HTTP, cơ sở dữ liệu (database / 데이터베이스) adapter hoặc dịch vụ (service / 서비스) lời gọi (call / 호출) có khả năng abort. `cacheSignal` không dành cho máy khách (client / 클라이언트) thành phần (component / 컴포넌트) fetch tác động (effect / 효과); ở máy khách (client / 클라이언트) vẫn dùng vòng đời (lifecycle / 생명주기)/cancellation của dữ liệu (data / 데이터) tầng (layer / 계층) hoặc `AbortController` phù hợp.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **18. useInsertionEffect** tiếp nhận điểm tựa từ **17. External store và useSyncExternalStore** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. useImperativeHandle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. `useInsertionEffect`

`useInsertionEffect` chủ yếu dành cho CSS-in-JS thư viện (library / 라이브러리) cần insert styles ở timing đặc biệt trước bố cục (layout / 레이아웃) effects. ứng dụng (application / 애플리케이션) lô-gic nghiệp vụ (business logic / 비즈니스 로직) gần như không nên dùng.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — thư viện (library / 라이브러리) Hooks của React 18
>
> `useSyncExternalStore` và `useInsertionEffect` được giới thiệu cùng React 18 chủ yếu để bên ngoài (external / 외부) store và CSS-in-JS thư viện (library / 라이브러리) tương thích tốt với concurrent rendering. ứng dụng (application / 애플리케이션) mã (code / 코드) bình thường hiếm khi cần tự dùng `useInsertionEffect`, còn `useSyncExternalStore` thường nằm phía dưới các state-management libraries.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **19. useImperativeHandle** tiếp nhận điểm tựa từ **18. useInsertionEffect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. lỗi (error / 오류) kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. `useImperativeHandle`
Phần này nối mạch bài học với “19. `useImperativeHandle`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
function MyInput({ ref }) {
  const inputRef = useRef(null);

  useImperativeHandle(ref, () => ({
    focus() {
      inputRef.current?.focus();
    },
  }), []);

  return <input ref={inputRef} />;
}
```

Expose năng lực (capability / 역량) nhỏ giúp giữ encapsulation tốt hơn việc expose raw DOM nút (node / 노드). Imperative API là escape hatch; declarative API vẫn nên là mặc định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **20. lỗi (error / 오류) kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **19. useImperativeHandle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20A. Async UI cần phân biệt pending, expected lỗi (error / 오류) và unexpected kết xuất (render / 렌더링) thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. lỗi (error / 오류) kiến trúc (architecture / 아키텍처)

Phân biệt kết xuất (render / 렌더링) lỗi (error / 오류), async mutation lỗi (error / 오류), loading lỗi (error / 오류), expected lĩnh vực (domain / 도메인) kiểm tra hợp lệ (validation / 검증) và unexpected hạ tầng (infrastructure / 인프라) lỗi (error / 오류). Expected kiểm tra hợp lệ (validation / 검증) thường nên trở thành trạng thái (state / 상태)/hành động (action / 동작) kết quả (result / 결과) thay vì ném lên toàn cục (global / 전역) lỗi (error / 오류) ranh giới (boundary / 경계). Unexpected kết xuất (render / 렌더링) thất bại (failure / 실패) nên bị ranh giới (boundary / 경계) ở phạm vi (scope / 범위) phù hợp bắt và report.

Môi trường vận hành (production / 운영 환경) app cần khả năng quan sát (observability / 관측 가능성), correlation ID và fallback theo tuyến (route / 경로)/tính năng (feature / 기능). Một ranh giới (boundary / 경계) duy nhất ở gốc (root / 루트) thường quá thô.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **20A. Async UI cần phân biệt pending, expected lỗi (error / 오류) và unexpected kết xuất (render / 렌더링) thất bại (failure / 실패)** tiếp nhận điểm tựa từ **20. lỗi (error / 오류) kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. SSR, streaming và hydration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20A. Async UI cần phân biệt pending, expected lỗi (error / 오류) và unexpected kết xuất (render / 렌더링) thất bại (failure / 실패)

Suspense ranh giới (boundary / 경계) xử lý “chưa sẵn sàng để kết xuất (render / 렌더링)” theo giao thức (protocol / 프로토콜) được hỗ trợ; lỗi (error / 오류) ranh giới (boundary / 경계) xử lý lỗi kết xuất (render / 렌더링) bất ngờ trong subtree; form/hành động (action / 동작) trạng thái (state / 상태) thường biểu diễn kiểm tra hợp lệ (validation / 검증) hoặc expected mutation thất bại (failure / 실패). Gộp tất cả thành `try/catch + global toast` làm mất ngữ nghĩa (semantics / 의미론) và khiến khôi phục (recovery / 복구) khó dự đoán.

Với dữ liệu (data / 데이터) tầng (layer / 계층) môi trường vận hành (production / 운영 환경), cần xác định ranh giới (boundary / 경계) nào thử lại (retry / 재시도), ranh giới (boundary / 경계) nào giữ stale content, ranh giới (boundary / 경계) nào reset khi tuyến (route / 경로)/key đổi và lỗi nào phải report khả năng quan sát (observability / 관측 가능성). chuyển tiếp (transition / 전이) có thể giữ UI cũ trong lúc điều hướng (navigation / 내비게이션)/dữ liệu (data / 데이터) mới chuẩn bị; nhưng nếu yêu cầu (request / 요청) thất bại, UX cần tuyến (route / 경로)/action-specific khôi phục (recovery / 복구) thay vì chỉ spinner biến mất.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **21. SSR, streaming và hydration** tiếp nhận điểm tựa từ **20A. Async UI cần phân biệt pending, expected lỗi (error / 오류) và unexpected kết xuất (render / 렌더링) thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Hydration mismatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. SSR, streaming và hydration

SSR tạo HTML trên máy chủ (server / 서버). trình duyệt (browser / 브라우저) nhận HTML trước, sau đó React hydrate để gắn interactivity. Streaming cho phép gửi HTML từng phần thay vì chờ toàn cây (tree / 트리).

Các API máy chủ (server / 서버) hiện đại gồm `renderToReadableStream`, `renderToPipeableStream` và nhóm prerender/resume tùy môi trường (environment / 환경)/phiên bản (version / 버전). ứng dụng (application / 애플리케이션) khung phần mềm (framework / 프레임워크) thường gọi thay bạn.

SSR không đồng nghĩa máy chủ (server / 서버) Components. SSR là kết xuất (render / 렌더링) thành HTML initial; RSC là mô hình thành phần (component / 컴포넌트) chạy máy chủ (server / 서버)/bản dựng (build / 빌드) và compose qua giao thức (protocol / 프로토콜) với máy khách (client / 클라이언트) Components.

### 21A. React DOM `browser()` trong React 19.3: opt-out SSR bằng Suspense thay vì đoán môi trường (environment / 환경)

Phần lớn thành phần (component / 컴포넌트) SSR phải tạo initial HTML tương thích với initial máy khách (client / 클라이언트) kết xuất (render / 렌더링). Nhưng có thành phần (component / 컴포넌트) thực sự không thể tạo UI có nghĩa trên máy chủ (server / 서버), ví dụ nó cần `localStorage`, trình duyệt (browser / 브라우저) timezone hoặc một browser-only dữ liệu (data / 데이터) nguồn (source / 소스). Trước đây nhà phát triển (developer / 개발자) thường thêm `mounted` trạng thái (state / 상태) trong tác động (effect / 효과) hoặc rải `typeof window !== "undefined"`, dễ tạo hai kết xuất (render / 렌더링) đường dẫn (path / 경로) thiếu cấu trúc và dễ che hydration bug.

React DOM 19.3 thêm `browser()` để biểu đạt ranh giới (boundary / 경계) này trực tiếp qua `use`:

```jsx
import {
  Suspense,
  use,
} from "react";
import { browser } from "react-dom";

function LocalTimeZone() {
  use(browser());

  const zone = new Intl.DateTimeFormat()
    .resolvedOptions()
    .timeZone;

  return <p>{zone}</p>;
}

function Page() {
  return (
    <Suspense fallback={<p>Đang xác định múi giờ...</p>}>
      <LocalTimeZone />
    </Suspense>
  );
}
```

Trên máy chủ (server / 서버), `use(browser())` suspend nên nearest Suspense fallback đi vào HTML. Trên máy khách (client / 클라이언트) nó không suspend, vì vậy thành phần (component / 컴포넌트) tiếp tục kết xuất (render / 렌더링) khi hydrate. Vì đây là `use`, lời gọi (call / 호출) có thể nằm sau early return hoặc trong điều kiện (condition / 조건) theo Rules của `use`; ví dụ nếu máy chủ (server / 서버) đã có `initialData`, thành phần (component / 컴포넌트) có thể kết xuất (render / 렌더링) ngay và chỉ opt-out SSR khi thiếu dữ liệu ban đầu.

Sự đánh đổi (trade-off / 트레이드오프) phải được nhìn rõ: opt-out nghĩa máy chủ (server / 서버) không gửi content thật của subtree đó, nên có thể làm initial content/SEO kém hơn và đẩy công việc (work / 작업) sang máy khách (client / 클라이언트). `browser()` vì vậy không phải cách “sửa nhanh mọi hydration mismatch”; trước tiên hãy làm kết xuất (render / 렌더링) deterministic. Chỉ dùng khi trình duyệt (browser / 브라우저) môi trường (environment / 환경) thật sự là một phần của dữ liệu cần kết xuất (render / 렌더링).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **22. Hydration mismatch** tiếp nhận điểm tựa từ **21. SSR, streaming và hydration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. máy chủ (server / 서버) Components** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Hydration mismatch

Initial máy khách (client / 클라이언트) kết xuất (render / 렌더링) phải tương thích máy chủ (server / 서버) HTML. Các nguồn mismatch phổ biến:

```jsx
<div>{Date.now()}</div>
<div>{Math.random()}</div>
```

hoặc đọc browser-only trạng thái (state / 상태) khi máy chủ (server / 서버) không có. Hãy làm initial kết xuất (render / 렌더링) deterministic hoặc dùng khung phần mềm (framework / 프레임워크) mẫu (pattern / 패턴) thích hợp. `suppressHydrationWarning` chỉ là escape hatch phạm vi nhỏ, không phải cách che bug hệ thống.

### 22A. gỡ lỗi (debug / 디버그) hydration bằng bằng chứng (evidence / 증거), không bằng việc thêm `suppressHydrationWarning`

Hydration bug thường chỉ xuất hiện ở môi trường vận hành (production / 운영 환경) vì máy chủ (server / 서버) và trình duyệt (browser / 브라우저) khác timezone, locale, cookie, extension, CDN mutation hoặc bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물). Cách gỡ lỗi (debug / 디버그) tốt là so ba thứ: **HTML máy chủ (server / 서버) thực sự gửi**, **đầu vào (input / 입력) serialized dùng cho initial máy khách (client / 클라이언트) kết xuất (render / 렌더링)**, và **đầu ra (output / 출력) máy khách (client / 클라이언트) ở lần kết xuất (render / 렌더링) đầu tiên trước tác động (effect / 효과)**. Nếu ba lớp này không cùng một snapshot, React chỉ đang phơi ra inconsistency đã tồn tại.

Các nguồn cần kiểm tra theo thứ tự gồm dữ liệu nondeterministic (`Date.now`, random, ID tự sinh), locale/timezone, invalid HTML nesting bị trình duyệt (browser / 브라우저) tự sửa, conditional dựa vào `window`, bộ nhớ đệm (cache / 캐시) trả hai phiên bản (version / 버전) dữ liệu (data / 데이터) khác nhau, và triển khai (deployment / 배포) nơi HTML cũ trỏ tới JS bundle mới. Đừng chỉ nhìn thành phần (component / 컴포넌트) ngăn xếp (stack / 스택); mạng (network / 네트워크)/View nguồn (source / 소스)/CDN headers và bản phát hành (release / 릴리스) ID thường mới là bằng chứng (evidence / 증거) quyết định.

Một nguyên tắc môi trường vận hành (production / 운영 환경) hữu ích là máy chủ (server / 서버) kết xuất (render / 렌더링) và initial máy khách (client / 클라이언트) kết xuất (render / 렌더링) phải cùng một **logical snapshot**. Sau hydration, tác động (effect / 효과) hoặc normal cập nhật (update / 업데이트) có thể chuyển sang browser-specific trạng thái (state / 상태). Nếu thành phần (component / 컴포넌트) không thể tuân bất biến (invariant / 불변식) đó một cách có nghĩa, `browser()`/Suspense hoặc khung phần mềm (framework / 프레임워크) client-only ranh giới (boundary / 경계) mới là lựa chọn rõ ràng hơn.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **23. máy chủ (server / 서버) Components** tiếp nhận điểm tựa từ **22. Hydration mismatch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. 'use client' và 'use server'** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. máy chủ (server / 서버) Components

Máy chủ (server / 서버) Components chạy trong máy chủ (server / 서버)/bản dựng (build / 빌드) môi trường (environment / 환경) và không nhất thiết gửi mã (code / 코드) của chính chúng vào máy khách (client / 클라이언트) bundle.

```jsx
async function ProductPage({ id }) {
  const product = await db.products.get(id);

  return (
    <article>
      <h1>{product.name}</h1>
      <AddToCartButton productId={id} />
    </article>
  );
}
```

`ProductPage` có thể chạy máy chủ (server / 서버); `AddToCartButton` là máy khách (client / 클라이언트) thành phần (component / 컴포넌트) để có trạng thái (state / 상태)/sự kiện (event / 이벤트) trình duyệt (browser / 브라우저).

Máy chủ (server / 서버) Components có thể `await` trong kết xuất (render / 렌더링). mô hình (model / 모델) RSC trong React 19 stable cho ứng dụng (application / 애플리케이션) usage, nhưng bundler/khung phần mềm (framework / 프레임워크) hiện thực (implementation / 구현) APIs có versioning các ràng buộc (constraints / 제약조건들) riêng; app nên dùng khung phần mềm (framework / 프레임워크) hỗ trợ chính thức.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — React 19 và RSC
>
> React 19 đưa React máy chủ (server / 서버) Components/máy chủ (server / 서버) Functions vào thế hệ môi trường vận hành (production / 운영 환경) hiện đại, nhưng **application-facing mô hình (model / 모델) ổn định không đồng nghĩa hiện thực (implementation / 구현) giao thức (protocol / 프로토콜) cho bundler/khung phần mềm (framework / 프레임워크) là một API bất biến giữa mọi minor/patch**. Nếu dùng Next.js hoặc khung phần mềm (framework / 프레임워크) RSC khác, phiên bản (version / 버전) khung phần mềm (framework / 프레임워크) và patch React máy chủ (server / 서버) DOM packages quan trọng không kém phiên bản (version / 버전) `react` chính.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **24. 'use client' và 'use server'** tiếp nhận điểm tựa từ **23. máy chủ (server / 서버) Components** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24A. máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계) là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. `'use client'` và `'use server'`

`'use client'` tạo máy khách (client / 클라이언트) ranh giới mô-đun (module boundary / 모듈 경계):

```jsx
"use client";

import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

`'use server'` không đánh dấu máy chủ (server / 서버) thành phần (component / 컴포넌트). Nó đánh dấu máy chủ (server / 서버) hàm (function / 함수) trong môi trường hỗ trợ:

```jsx
async function updateUser(formData) {
  "use server";
  // ...
}
```

Máy chủ (server / 서버) thành phần (component / 컴포넌트) không cần directive `"use server"`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **24. 'use client' và 'use server'** đã nêu tiêu chí phân biệt, còn **24A. máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계) là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **24B. SSR, hydration và RSC là các trục khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24A. máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계) là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)

Trong RSC, `'use client'` tạo ranh giới mô-đun (module boundary / 모듈 경계); phụ thuộc (dependency / 의존성) dưới máy khách (client / 클라이언트) ranh giới (boundary / 경계) có khả năng đi vào máy khách (client / 클라이언트) bundle. Vì vậy không import cơ sở dữ liệu (database / 데이터베이스) SDK, filesystem hay secret-bearing mô-đun (module / 모듈) vào máy khách (client / 클라이언트) đồ thị (graph / 그래프). Props máy chủ (server / 서버) → máy khách (client / 클라이언트) phải tuân serialization đặc tả hợp đồng (contract / 계약); máy chủ (server / 서버) hàm (function / 함수) tham chiếu (reference / 참조) là trường hợp giao thức (protocol / 프로토콜) riêng, không có nghĩa hàm (function / 함수) JavaScript bất kỳ truyền được qua mạng (network / 네트워크).

Evolution đi từ SPA mọi thành phần (component / 컴포넌트) chạy máy khách (client / 클라이언트), qua SSR kết xuất (render / 렌더링) HTML máy chủ (server / 서버) rồi hydrate máy khách (client / 클라이언트), tới RSC nơi một phần thành phần (component / 컴포넌트) chỉ chạy máy chủ (server / 서버). di chuyển (migration / 마이그레이션) nên đặt interactive ranh giới (boundary / 경계) nhỏ nhất hợp lý thay vì thêm `'use client'` lên gốc (root / 루트) cho hết lỗi.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **24A. máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계) là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** đã nêu tiêu chí phân biệt, còn **24B. SSR, hydration và RSC là các trục khác nhau** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **25. máy chủ (server / 서버) Functions và bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24B. SSR, hydration và RSC là các trục khác nhau

SSR trả HTML từ máy chủ (server / 서버) để có initial content sớm; hydration gắn React máy khách (client / 클라이언트) thời gian chạy (runtime / 런타임) vào HTML đó; React máy chủ (server / 서버) Components cho phép một phần thành phần (component / 컴포넌트) cây (tree / 트리) chạy máy chủ (server / 서버) và truyền payload để compose với máy khách (client / 클라이언트) Components. Một app có thể SSR mà không dùng RSC, và RSC khung phần mềm (framework / 프레임워크) vẫn phải quyết định phần nào hydrate trên máy khách (client / 클라이언트).

Khi gỡ lỗi (debug / 디버그), cần hỏi đúng ranh giới (boundary / 경계): mismatch là vấn đề máy chủ (server / 서버) HTML khác initial máy khách (client / 클라이언트) kết xuất (render / 렌더링); bundle lớn là vấn đề máy khách (client / 클라이언트) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프); secret leak là vấn đề ranh giới mô-đun (module boundary / 모듈 경계)/serialization; waterfall có thể nằm ở routing/dữ liệu (data / 데이터) kiến trúc (architecture / 아키텍처). Gọi tất cả là “SSR issue” làm di chuyển (migration / 마이그레이션) và profiling thiếu chính xác.

### 24C. ngữ cảnh (context / 맥락) qua RSC ranh giới (boundary / 경계) trong React 19.3

Máy chủ (server / 서버) thành phần (component / 컴포넌트) không thể tự gọi `createContext` để tạo một ngữ cảnh (context / 맥락) server-native. Nhưng từ React 19.3, nó có thể import một ngữ cảnh (context / 맥락) được khai báo trong mô-đun (module / 모듈) `'use client'` rồi kết xuất (render / 렌더링) ngữ cảnh (context / 맥락) đó trực tiếp làm provider.

```jsx
// user-context.js
"use client";

import { createContext } from "react";

export const UserContext = createContext(null);
```

```jsx
// Layout.server.jsx
import { UserContext } from "./user-context.js";

export async function Layout({ children }) {
  const currentUser = await getCurrentUser();

  return (
    <UserContext value={currentUser}>
      {children}
    </UserContext>
  );
}
```

Trước đó khung phần mềm (framework / 프레임워크)/app thường cần một máy khách (client / 클라이언트) wrapper chỉ để nhận prop từ máy chủ (server / 서버) rồi kết xuất (render / 렌더링) provider. năng lực (capability / 역량) mới giảm wrapper nhưng không xóa máy khách (client / 클라이언트) ranh giới (boundary / 경계): ngữ cảnh (context / 맥락) vẫn được tạo từ mô-đun (module / 모듈) máy khách (client / 클라이언트) và giá trị truyền qua ranh giới (boundary / 경계) vẫn phải phù hợp serialization/bảo mật (security / 보안) các ràng buộc (constraints / 제약조건들). Đừng truyền cơ sở dữ liệu (database / 데이터베이스) thực thể (entity / 엔터티) chứa secret hoặc đối tượng (object / 객체) lớn chỉ vì provider cú pháp (syntax / 문법) ngắn hơn.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **25. máy chủ (server / 서버) Functions và bảo mật (security / 보안)** tiếp nhận điểm tựa từ **24B. SSR, hydration và RSC là các trục khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. dữ liệu (data / 데이터) kiến trúc (architecture / 아키텍처) môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. máy chủ (server / 서버) Functions và bảo mật (security / 보안)

Máy chủ (server / 서버) hàm (function / 함수) phải được coi như công khai (public / 공개) mạng (network / 네트워크) surface dù cú pháp (syntax / 문법) trông giống hàm (function / 함수) lời gọi (call / 호출). Dữ liệu từ máy khách (client / 클라이언트) luôn là untrusted đầu vào (input / 입력).

Không đủ an toàn:

```js
async function deleteUser(userId) {
  "use server";
  await db.user.delete(userId);
}
```

Cần authenticate, authorize tài nguyên (resource / 자원)/hành động (action / 동작), validate đầu vào (input / 입력), giới hạn lỗi (error / 오류) leakage và bảo vệ secrets. Serialized argument từ máy khách (client / 클라이언트) không chứng minh người dùng (user / 사용자) có quyền. máy khách (client / 클라이언트) UI có thể ẩn button nhưng authorization thật phải nằm ở máy chủ (server / 서버).

RSC ecosystem từng có bảo mật (security / 보안) advisory quan trọng, vì vậy môi trường vận hành (production / 운영 환경) khung phần mềm (framework / 프레임워크)/React gói (package / 패키지) phải được patch theo advisory chính thức, không chỉ “đúng major phiên bản (version / 버전)”.

### 25A. Trusted Types trong React 19.3: React hỗ trợ chính sách (policy / 정책), không thay bạn sanitize

React vốn escape văn bản (text / 텍스트) nút (node / 노드)/attribute thông thường, nhưng XSS ranh giới (boundary / 경계) thay đổi khi app cố ý đi vào injection sink như `innerHTML`. trình duyệt (browser / 브라우저) Trusted Types cho phép CSP yêu cầu những sink này chỉ nhận đối tượng (object / 객체) đã đi qua chính sách (policy / 정책), chẳng hạn `TrustedHTML`, thay vì raw string.

Trước React 19.3, React có thể coerce Trusted Types đối tượng (object / 객체) thành string trước khi đưa xuống DOM, làm trình duyệt (browser / 브라우저) mất bằng chứng (evidence / 증거) rằng giá trị (value / 값) đã qua chính sách (policy / 정책). React 19.3 truyền đối tượng (object / 객체) Trusted Types xuống injection sink mà không phá kiểu (type / 타입) marker đó, nên app có thể dùng CSP như `require-trusted-types-for 'script'` cùng chính sách (policy / 정책)/sanitizer của mình.

Điều này **không có nghĩa `dangerouslySetInnerHTML` trở nên an toàn tự động**. React không chứng minh HTML của bạn sạch; Trusted Types cũng chỉ mạnh bằng chính sách (policy / 정책) tạo ra đối tượng (object / 객체) trusted. môi trường vận hành (production / 운영 환경) bảo mật (security / 보안) vẫn cần sanitize đúng ngữ cảnh (context / 맥락), CSP hợp lý, tránh URL/script sink nguy hiểm và kiểm tra (audit / 감사) third-party mã (code / 코드). Hãy coi React 19.3 là sửa plumbing để trình duyệt (browser / 브라우저) ranh giới bảo mật (security boundary / 보안 경계) hoạt động đúng, không phải một sanitizer mới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **25. máy chủ (server / 서버) Functions và bảo mật (security / 보안)** nêu điều cần giải thích; **26. dữ liệu (data / 데이터) kiến trúc (architecture / 아키텍처) môi trường vận hành (production / 운영 환경)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **27. trạng thái (state / 상태) management quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. dữ liệu (data / 데이터) kiến trúc (architecture / 아키텍처) môi trường vận hành (production / 운영 환경)

Một kiến trúc (architecture / 아키텍처) khỏe mạnh phân biệt rõ:

```text
remote/server state -> query cache hoặc framework data layer
URL state           -> router/search params
form state          -> form abstraction/local state
UI ephemeral state  -> component state
shared client state -> Context/external store khi cần
derived state       -> tính từ source of truth
```

Quyết định “Redux, Zustand hay ngữ cảnh (context / 맥락)?” chỉ nên đặt sau khi phân loại trạng thái (state / 상태). Nhiều app không cần giant toàn cục (global / 전역) store nếu máy chủ (server / 서버) dữ liệu (data / 데이터) đã ở truy vấn (query / 쿼리) bộ nhớ đệm (cache / 캐시) và điều hướng (navigation / 내비게이션) trạng thái (state / 상태) đã ở URL.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **26. dữ liệu (data / 데이터) kiến trúc (architecture / 아키텍처) môi trường vận hành (production / 운영 환경)** nêu điều cần giải thích; **27. trạng thái (state / 상태) management quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **27A. State-management evolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. trạng thái (state / 상태) management quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)

Cục bộ (local / 로컬) trạng thái (state / 상태) là mặc định vì locality dễ hiểu và dễ xóa. ngữ cảnh (context / 맥락) phù hợp phụ thuộc (dependency / 의존성)/giá trị (value / 값) theo subtree. Reducer phù hợp chuyển tiếp trạng thái (state transition / 상태 전이) phức tạp trong một phạm vi (scope / 범위). bên ngoài (external / 외부) store như Zustand/Redux phù hợp khi nhiều nhánh xa nhau cùng đọc/ghi máy khách (client / 클라이언트) trạng thái (state / 상태), cần selector, middleware, devtools hoặc convention mạnh.

Redux Toolkit hợp với lĩnh vực (domain / 도메인)/hành động (action / 동작) luồng (flow / 흐름) lớn và nhóm (team / 팀) cần cấu trúc chặt. Zustand nhẹ hơn nhưng convention do nhóm (team / 팀) tự quyết định nhiều hơn. Không nên tự xây HTTP bộ nhớ đệm (cache / 캐시) bên trong toàn cục (global / 전역) store khi server-state thư viện (library / 라이브러리) đã giải quyết stale/thử lại (retry / 재시도)/vô hiệu hóa (invalidation / 무효화) tốt hơn.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **27A. State-management evolution** tiếp nhận điểm tựa từ **27. trạng thái (state / 상태) management quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. thành phần (component / 컴포넌트) API thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27A. State-management evolution

Flux/Redux giải quyết predictable trạng thái dùng chung (shared state / 공유 상태) trong thời lớp (class / 클래스). Hooks giảm nhu cầu bộ chứa (container / 컨테이너)/HOC cho cục bộ (local / 로컬) lô-gic (logic / 논리); ngữ cảnh (context / 맥락) lo phụ thuộc (dependency / 의존성) theo subtree; truy vấn (query / 쿼리)/router/form layers tách máy chủ (server / 서버), URL và form trạng thái (state / 상태) khỏi toàn cục (global / 전역) store. Redux không obsolete: bên ngoài (external / 외부) store vẫn phù hợp khi lĩnh vực (domain / 도메인) máy khách (client / 클라이언트) trạng thái (state / 상태) lớn, nhiều nhánh cùng đọc/ghi và cần selector, middleware, sự kiện (event / 이벤트) log hoặc convention tổ chức mạnh. Chọn theo quyền sở hữu (ownership / 소유권)/cập nhật (update / 업데이트) topology, không theo thời thượng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **28. thành phần (component / 컴포넌트) API thiết kế (design / 설계)** tiếp nhận điểm tựa từ **27A. State-management evolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Các mẫu thiết kế (design pattern / 디자인 패턴) phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. thành phần (component / 컴포넌트) API thiết kế (design / 설계)

API thành phần (component / 컴포넌트) nên composable và tránh boolean explosion.

Không tốt:

```jsx
<Card
  isBlue
  isCompact
  isClickable
  isLoading
  specialCase2
/>
```

Tốt hơn có thể dùng variant:

```jsx
<Card variant="info" size="compact" interactive />
```

hoặc composition:

```jsx
<Card>
  <Card.Header>...</Card.Header>
  <Card.Body>...</Card.Body>
</Card>
```

Boolean props nhiều tạo trạng thái (state / 상태) không gian (space / 공간) khổng lồ và combination vô nghĩa. API thiết kế (design / 설계) phải cân bằng convenience với extensibility.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **29. Các mẫu thiết kế (design pattern / 디자인 패턴) phổ biến** tiếp nhận điểm tựa từ **28. thành phần (component / 컴포넌트) API thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Headless và compound components** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Các mẫu thiết kế (design pattern / 디자인 패턴) phổ biến

React hiện đại ưu tiên composition hơn inheritance. mẫu (pattern / 패턴) thường gặp gồm custom hooks, provider mẫu (pattern / 패턴), compound components, controlled thành phần (component / 컴포넌트), headless thành phần (component / 컴포넌트), kết xuất (render / 렌더링) props và trạng thái (state / 상태) reducer mẫu (pattern / 패턴).

HOC vẫn tồn tại trong mã (code / 코드) cũ/thư viện (library / 라이브러리):

```jsx
const Enhanced = withSomething(Component);
```

Nhưng custom Hook thường dễ compose hơn cho reusable stateful lô-gic (logic / 논리).

Kết xuất (render / 렌더링) prop vẫn hữu ích khi bên tiêu thụ (consumer / 소비자) cần kiểm soát đầu ra (output / 출력):

```jsx
<DataProvider>
  {data => <View data={data} />}
</DataProvider>
```

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **30. Headless và compound components** tiếp nhận điểm tựa từ **29. Các mẫu thiết kế (design pattern / 디자인 패턴) phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Controlled và uncontrolled thành phần (component / 컴포넌트) API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Headless và compound components

Headless thành phần (component / 컴포넌트) quản lý hành vi (behavior / 동작)/trạng thái (state / 상태)/khả năng tiếp cận (accessibility / 접근성) nhưng không ép style. Compound thành phần (component / 컴포넌트) tạo API có quan hệ rõ:

```jsx
<Tabs defaultValue="account">
  <Tabs.List>
    <Tabs.Trigger value="account">Account</Tabs.Trigger>
    <Tabs.Trigger value="security">Security</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="account">...</Tabs.Content>
  <Tabs.Content value="security">...</Tabs.Content>
</Tabs>
```

Hiện thực (implementation / 구현) có thể dùng ngữ cảnh (context / 맥락) nội bộ, roving tabindex, keyboard điều hướng (navigation / 내비게이션) và máy trạng thái (state machine / 상태 머신). Đây là mẫu (pattern / 패턴) mạnh cho thiết kế (design / 설계) hệ thống (system / 시스템).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **31. Controlled và uncontrolled thành phần (component / 컴포넌트) API** tiếp nhận điểm tựa từ **30. Headless và compound components** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Controlled và uncontrolled thành phần (component / 컴포넌트) API

Controlled:

```jsx
<Dialog open={open} onOpenChange={setOpen} />
```

Uncontrolled:

```jsx
<Dialog defaultOpen />
```

Controlled nghĩa parent là nguồn chuẩn (source of truth / 정본); uncontrolled nghĩa thành phần (component / 컴포넌트) giữ trạng thái (state / 상태) nội bộ. Không nên chuyển qua lại hai chế độ (mode / 모드) mơ hồ trong cùng thời gian tồn tại (lifetime / 수명). thư viện (library / 라이브러리) phải document precedence và callback hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **32. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링)** tiếp nhận điểm tựa từ **31. Controlled và uncontrolled thành phần (component / 컴포넌트) API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32A. hiệu năng (performance / 성능) chi phí (cost / 비용) mô hình (model / 모델): kết xuất (render / 렌더링) công việc (work / 작업), lần ghi nhận (commit / 커밋) công việc (work / 작업) và bên ngoài (external / 외부) công việc (work / 작업)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링)

React hiệu năng (performance / 성능) không chỉ là re-render. Bottleneck lớn thường là mạng (network / 네트워크) waterfall, initial bundle lớn, danh sách (list / 목록) hàng nghìn item, thuật toán (algorithm / 알고리즘) nặng, ảnh (image / 이미지)/font, bố cục (layout / 레이아웃) thrash hoặc backend độ trễ (latency / 지연 시간).

Quy trình đúng: đo trải nghiệm, profile bằng React DevTools và trình duyệt (browser / 브라우저) hiệu năng (performance / 성능), xác định bottleneck, giảm công việc (work / 작업) ở tầng (layer / 계층) đúng, rồi đo lại. Memo một thành phần (component / 컴포넌트) 0.1 ms trong khi tải 4 MB JS là tối ưu sai chỗ.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **32A. hiệu năng (performance / 성능) chi phí (cost / 비용) mô hình (model / 모델): kết xuất (render / 렌더링) công việc (work / 작업), lần ghi nhận (commit / 커밋) công việc (work / 작업) và bên ngoài (external / 외부) công việc (work / 작업)** tiếp nhận điểm tựa từ **32. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Profiling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32A. hiệu năng (performance / 성능) chi phí (cost / 비용) mô hình (model / 모델): kết xuất (render / 렌더링) công việc (work / 작업), lần ghi nhận (commit / 커밋) công việc (work / 작업) và bên ngoài (external / 외부) công việc (work / 작업)

Trước khi memoize, xác định bottleneck thuộc loại nào. **kết xuất (render / 렌더링) công việc (work / 작업)** là thời gian gọi thành phần (component / 컴포넌트) và tính cây (tree / 트리); **lần ghi nhận (commit / 커밋) công việc (work / 작업)** là DOM mutation, bố cục (layout / 레이아웃) tác động (effect / 효과)/ref công việc (work / 작업); **bên ngoài (external / 외부) công việc (work / 작업)** gồm mạng (network / 네트워크), parse dữ liệu, ảnh (image / 이미지), third-party widget và trình duyệt (browser / 브라우저) bố cục (layout / 레이아웃)/paint. `memo` không sửa yêu cầu (request / 요청) waterfall, còn mã (code / 코드) splitting không giúp một tác động (effect / 효과) vòng lặp (loop / 루프) vô hạn.

Một workflow tối ưu hợp lý là: tái hiện tương tác (interaction / 상호작용) chậm → đo bằng React DevTools Profiler và trình duyệt (browser / 브라우저) hiệu năng (performance / 성능) tools → xác định thành phần (component / 컴포넌트) hoặc bên ngoài (external / 외부) tác vụ (task / 작업) chiếm thời gian → sửa kiến trúc (architecture / 아키텍처) trước → chỉ thêm memoization khi định danh (identity / 식별자) ổn định và kết xuất (render / 렌더링) thực sự đắt → đo lại. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) không được trở thành phụ thuộc (dependency / 의존성) cho tính đúng đắn (correctness / 정확성).

Các tối ưu structural thường thắng memoization rải rác: giữ trạng thái (state / 상태) gần nơi dùng, tránh tác động (effect / 효과) chuỗi (chain / 사슬) set trạng thái (state / 상태), chia ngữ cảnh (context / 맥락) theo volatility, virtualize danh sách (list / 목록) lớn, tránh kết xuất (render / 렌더링) subtree không cần thiết, và đặt Suspense/code-split ranh giới (boundary / 경계) theo tương tác (interaction / 상호작용) thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **33. Profiling** tiếp nhận điểm tựa từ **32A. hiệu năng (performance / 성능) chi phí (cost / 비용) mô hình (model / 모델): kết xuất (render / 렌더링) công việc (work / 작업), lần ghi nhận (commit / 커밋) công việc (work / 작업) và bên ngoài (external / 외부) công việc (work / 작업)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. danh sách (list / 목록) virtualization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Profiling

React DevTools Profiler cho biết thành phần (component / 컴포넌트) kết xuất (render / 렌더링)/lần ghi nhận (commit / 커밋) chi phí (cost / 비용) và các thông tin liên quan. trình duyệt (browser / 브라우저) hiệu năng (performance / 성능) panel cần dùng khi bottleneck gồm scripting, bố cục (layout / 레이아웃), paint, mạng (network / 네트워크). Hãy profile production-like bản dựng (build / 빌드) vì development chế độ (mode / 모드) có Strict chế độ (mode / 모드)/gỡ lỗi (debug / 디버그) overhead.

### 33A. React hiệu năng (performance / 성능) Tracks: nối Scheduler bằng chứng (evidence / 증거) với trình duyệt (browser / 브라우저) timeline

Từ React 19.2, Chrome DevTools hiệu năng (performance / 성능) có React-specific tracks giúp nhìn scheduling thay vì chỉ thấy một khối JavaScript dài. **Scheduler nhánh học (track / 트랙)** cho biết công việc (work / 작업) nào thuộc blocking/người dùng (user / 사용자) tương tác (interaction / 상호작용), công việc (work / 작업) nào thuộc chuyển tiếp (transition / 전이), cập nhật (update / 업데이트) nào đang bị công việc (work / 작업) priority khác chặn và React đang chờ paint ở đâu. **Components nhánh học (track / 트랙)** cho thấy thành phần (component / 컴포넌트) cây (tree / 트리) đang kết xuất (render / 렌더링) hoặc chạy Effects, kèm các trạng thái như mount/blocked và thời gian tương ứng.

Điều này thay đổi cách gỡ lỗi (debug / 디버그) câu “chuyển tiếp (transition / 전이) không giúp gì”. React DevTools Profiler trả lời tốt câu hỏi thành phần (component / 컴포넌트) nào kết xuất (render / 렌더링) tốn thời gian; trình duyệt (browser / 브라우저) hiệu năng (performance / 성능) trả lời main luồng thực thi (thread / 스레드) còn bận bởi bố cục (layout / 레이아웃)/paint/third-party tác vụ (task / 작업) nào; React hiệu năng (performance / 성능) Tracks nối thêm câu hỏi scheduler đã phân loại và xen kẽ React công việc (work / 작업) ra sao. cấp cao (senior / 시니어) investigation nên đối chiếu cả ba thay vì nhìn một flame chart rồi đoán.

Một worked lập luận (reasoning / 추론) đơn giản: nếu Scheduler cho thấy chuyển tiếp (transition / 전이) công việc (work / 작업) thường xuyên yield đúng cách nhưng INP vẫn xấu vì sự kiện (event / 이벤트) handler tự parse 20 MB JSON trước khi gọi setter, đổi thêm `startTransition` không giải quyết được. Ngược lại, nếu CPU chi phí (cost / 비용) nằm trong một kết xuất (render / 렌더링) subtree non-urgent và đầu vào (input / 입력) bị cạnh tranh với nó, chuyển tiếp (transition / 전이)/structural split mới là hướng có bằng chứng (evidence / 증거).

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **34. danh sách (list / 목록) virtualization** tiếp nhận điểm tựa từ **33. Profiling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Referential equality và định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. danh sách (list / 목록) virtualization

Danh sách hàng nghìn item không nên kết xuất (render / 렌더링) toàn bộ nếu viewport chỉ thấy vài chục. Virtualization kết xuất (render / 렌더링) một cửa sổ (window / 윈도우) gần viewport. Thư viện hiện hành như TanStack Virtual hoặc giải pháp tương tự có thể dùng tùy ngăn xếp (stack / 스택).

Cần kiểm tra động (dynamic / 동적) row height, keyboard điều hướng (navigation / 내비게이션), khả năng tiếp cận (accessibility / 접근성), sticky rows, trình duyệt (browser / 브라우저) find và đo lường (measurement / 측정). Virtualization không “miễn phí”.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **35. Referential equality và định danh (identity / 식별자)** tiếp nhận điểm tựa từ **34. danh sách (list / 목록) virtualization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35A. Memoization ranh giới (boundary / 경계) trong thời React trình biên dịch (compiler / 컴파일러)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Referential equality và định danh (identity / 식별자)

Trong JavaScript:

```js
{} !== {}
(() => {}) !== (() => {})
```

Đối tượng (object / 객체)/hàm (function / 함수) mới có định danh (identity / 식별자) mới, ảnh hưởng phụ thuộc (dependency / 의존성), memo và selector. Nhưng không vì vậy mà mọi hàm (function / 함수) cần `useCallback`. Nếu child không memo và hàm (function / 함수) không làm phụ thuộc (dependency / 의존성) cần stability thì callback memo thường không mang lợi ích.

React trình biên dịch (compiler / 컴파일러) có thể tự xử lý nhiều memoization, nhưng định danh (identity / 식별자) đặc tả hợp đồng (contract / 계약) với hệ thống bên ngoài (external system / 외부 시스템) vẫn cần hiểu rõ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **35. Referential equality và định danh (identity / 식별자)** đã nêu tiêu chí phân biệt, còn **35A. Memoization ranh giới (boundary / 경계) trong thời React trình biên dịch (compiler / 컴파일러)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **36. mã (code / 코드) splitting chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35A. Memoization ranh giới (boundary / 경계) trong thời React trình biên dịch (compiler / 컴파일러)

`memo`, `useMemo` và `useCallback` đều có chi phí về phụ thuộc (dependency / 의존성) lập luận (reasoning / 추론) và bộ nhớ đệm (cache / 캐시) bookkeeping. Chúng hữu ích khi một expensive subtree thường nhận cùng props, một calculation thực sự đắt, hoặc bên ngoài (external / 외부) API yêu cầu stable định danh (identity / 식별자). Chúng không nên được dùng như nghi thức cho mọi đối tượng (object / 객체)/hàm (function / 함수).

React trình biên dịch (compiler / 컴파일러) có thể tự động hóa nhiều memoization, nhưng điều đó làm **purity và luồng dữ liệu (data flow / 데이터 흐름)** quan trọng hơn chứ không ít đi. trình biên dịch (compiler / 컴파일러) không sửa quyền sở hữu trạng thái (state ownership / 상태 소유권) sai, tác động (effect / 효과) vòng lặp (loop / 루프), ngữ cảnh (context / 맥락) giá trị (value / 값) thay đổi vô ích hay mạng (network / 네트워크) waterfall. thư viện (library / 라이브러리) cũng không thể giả định mọi bên tiêu thụ (consumer / 소비자) bật trình biên dịch (compiler / 컴파일러), nên API công khai (public API / 공개 API) vẫn cần định danh (identity / 식별자) đặc tả hợp đồng (contract / 계약) rõ và benchmark trên thời gian chạy (runtime / 런타임) hỗ trợ (support / 지원) thực tế.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **35A. Memoization ranh giới (boundary / 경계) trong thời React trình biên dịch (compiler / 컴파일러)** đã nêu tiêu chí phân biệt, còn **36. mã (code / 코드) splitting chiến lược (strategy / 전략)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **37. khả năng tiếp cận (accessibility / 접근성) môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. mã (code / 코드) splitting chiến lược (strategy / 전략)

Không split từng thành phần (component / 컴포넌트) nhỏ. ranh giới (boundary / 경계) tốt thường theo tuyến (route / 경로), tính năng (feature / 기능) nặng hoặc widget hiếm dùng.

```jsx
const AdminPage = lazy(() => import("./AdminPage.jsx"));
```

Preload/prefetch theo intent hoặc khung phần mềm (framework / 프레임워크) năng lực (capability / 역량) có thể giảm delay. Bundle phân tích (analysis / 분석) nên kiểm tra phụ thuộc (dependency / 의존성) lớn, duplicate gói (package / 패키지), locale dữ liệu (data / 데이터) và dead mã (code / 코드).

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **37. khả năng tiếp cận (accessibility / 접근성) môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **36. mã (code / 코드) splitting chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Testing chiến lược (strategy / 전략) môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. khả năng tiếp cận (accessibility / 접근성) môi trường vận hành (production / 운영 환경)

Khả năng tiếp cận (accessibility / 접근성) là hành vi (behavior / 동작), không chỉ ARIA. rà soát (review / 검토) phải kiểm tra ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조), heading hierarchy, keyboard, focus, screen-reader announcement, lỗi (error / 오류) association, contrast và reduced motion.

Dialog cần focus containment/trap phù hợp, focus restore, accessible title và escape ngữ nghĩa (semantics / 의미론). Dùng thành phần nguyên thủy (primitive / 기본 요소) khả năng tiếp cận (accessibility / 접근성) đã được kiểm chứng thường tốt hơn tự implement widget phức tạp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **38. Testing chiến lược (strategy / 전략) môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **37. khả năng tiếp cận (accessibility / 접근성) môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. TypeScript với React** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Testing chiến lược (strategy / 전략) môi trường vận hành (production / 운영 환경)

Kiểm thử (test / 테스트) theo rủi ro (risk / 위험). trọng yếu (critical / 중요) luồng (flow / 흐름) cần tích hợp (integration / 통합)/E2E; reducer/formatter có trường hợp biên (edge case / 경계 사례) cần đơn vị (unit / 단위); thiết kế (design / 설계) hệ thống (system / 시스템) có thể cần visual regression; khả năng tiếp cận (accessibility / 접근성) cần automated axe cộng manual keyboard/screen-reader testing.

Mock quá sâu tạo kiểm thử (test / 테스트) “xanh” nhưng không phản ánh tích hợp (integration / 통합). mạng (network / 네트워크) mocking ở ranh giới (boundary / 경계) HTTP thường tốt hơn mock từng custom Hook hiện thực (implementation / 구현).

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **39. TypeScript với React** tiếp nhận điểm tựa từ **38. Testing chiến lược (strategy / 전략) môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. phiên bản (version / 버전) tính tương thích (compatibility / 호환성): React 16.8 → 19.3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. TypeScript với React

Props:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary";
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
};

function Button({
  variant = "primary",
  disabled = false,
  children,
  onClick,
}: ButtonProps) {
  return (
    <button data-variant={variant} disabled={disabled} onClick={onClick}>
      {children}
    </button>
  );
}
```

Discriminated union giúp loại impossible trạng thái (state / 상태):

```tsx
type LoadState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: Error };
```

Ref:

```tsx
const inputRef = useRef<HTMLInputElement>(null);
```

Không cần dùng `React.FC` cho mọi thành phần (component / 컴포넌트); typed props trực tiếp thường đơn giản hơn.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **40. phiên bản (version / 버전) tính tương thích (compatibility / 호환성): React 16.8 → 19.3** tiếp nhận điểm tựa từ **39. TypeScript với React** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40A. Ma trận API cũ, trạng thái và cách thay thế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. phiên bản (version / 버전) tính tương thích (compatibility / 호환성): React 16.8 → 19.3

Ở mức (level / 수준) cấp cao (senior / 시니어), versioning không nên chỉ là “phiên bản (version / 버전) mới hơn có nhiều API hơn”. Mỗi mốc thay đổi một phần mô hình tư duy (mental model / 사고 모델) hoặc tính tương thích (compatibility / 호환성) surface.

| Mốc | Thay đổi đáng học | Ý nghĩa khi đọc mã (code / 코드) |
|---|---|---|
| React 16.8 | Hooks | mã (code / 코드) hiện đại chuyển dần từ lớp (class / 클래스) vòng đời (lifecycle / 생명주기) sang hàm (function / 함수) thành phần (component / 컴포넌트) + Hooks. |
| React 17 | bản phát hành (release / 릴리스) chuyển tiếp, gradual upgrade, hiện đại (modern / 현대적) JSX transform phổ biến | Nhiều mã (code / 코드) React 17 trông gần React 18 về thành phần (component / 컴포넌트) cú pháp (syntax / 문법) nhưng entry gốc (root / 루트) và batching vẫn khác. |
| React 18 | `createRoot`, automatic batching, transitions, `useDeferredValue`, `useId`, streaming SSR, Strict chế độ (mode / 모드) checks | Đây là nền tính đồng thời (concurrency / 동시성) hiện đại. App dùng legacy `ReactDOM.render` không có đầy đủ ngữ nghĩa (semantics / 의미론) gốc (root / 루트) mới. |
| React 18.3 | Warning cầu nối (bridge / 브리지) trước React 19 | Rất hữu ích cho di chuyển (migration / 마이그레이션) vì chỉ ra API/deprecation phải sửa trước khi nâng major. |
| React 19.0 | Actions, `use`, `useActionState`, `useOptimistic`, hàm (function / 함수) form Actions, ref-as-prop, ngữ cảnh (context / 맥락) shorthand, hiện đại (modern / 현대적) JSX transform required, removal của một số legacy APIs | Bắt đầu thế hệ async mutation/RSC API mới. |
| React 19.1 | Chủ yếu cải thiện máy chủ (server / 서버)/RSC/prerender và độ ổn định của nhánh 19 | Ít thay đổi mô hình tư duy (mental model / 사고 모델) phía beginner; vẫn phải theo patch nếu dùng RSC. |
| React 19.2 | `<Activity />`, `useEffectEvent`, `cacheSignal`, hiệu năng (performance / 성능) Tracks, Partial Pre-rendering/máy chủ (server / 서버) improvements | App/thư viện (library / 라이브러리) phải kiểm tra minimum minor phiên bản (version / 버전) nếu dùng các API này. |
| React 19.3 | Stable View Transitions, Fragment refs; React DOM `browser` và Trusted Types hỗ trợ (support / 지원); RSC ngữ cảnh (context / 맥락) năng lực (capability / 역량) mới | Baseline hiện tại của tài liệu. Các API 19.3 không nên vô tình lọt vào gói (package / 패키지) tuyên bố hỗ trợ (support / 지원) 19.0. |
| React trình biên dịch (compiler / 컴파일러) 1.0 | Automatic memoization, stable từ 2025; phiên bản (version / 버전) độc lập React cốt lõi (core / 핵심) | Không đồng nhất phiên bản (version / 버전) trình biên dịch (compiler / 컴파일러) với React. Có thể hỗ trợ nhiều React major theo cấu hình (configuration / 구성). |

### Cách đọc tutorial cũ

Nếu thấy `ReactDOM.render`, hãy nghĩ “pre-React-18 gốc (root / 루트) API”. Nếu thấy lớp (class / 클래스) thành phần (component / 컴포넌트) với `componentDidMount`, đừng dịch máy móc từng vòng đời (lifecycle / 생명주기) sang một `useEffect`; hãy xác định synchronization thật sự. Nếu thấy `forwardRef`, mã (code / 코드) chưa chắc cũ hoặc sai: đó vẫn là lựa chọn cần thiết cho tính tương thích (compatibility / 호환성) React 18. Nếu thấy `useEffectEvent` hay `<Activity>`, dự án (project / 프로젝트) phải ít nhất ở React 19.2. Nếu thấy stable View chuyển tiếp (transition / 전이) tích hợp (integration / 통합) hoặc Fragment ref API mới, dự án (project / 프로젝트) cần React 19.3.

### Phiên bản (version / 버전) và bảo mật (security / 보안) không phải cùng một việc

React 19 từng có các bảo mật (security / 보안) advisory nghiêm trọng liên quan React máy chủ (server / 서버) Components và các bản sửa được backport vào nhiều nhánh patch. Bài học môi trường vận hành (production / 운영 환경) là không chỉ nói “chúng ta đang ở React 19.1/19.2”; phải theo **patch phiên bản (version / 버전) đã được khung phần mềm (framework / 프레임워크)/React khuyến nghị**, đặc biệt khi dùng `react-server-dom-*`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **40A. Ma trận API cũ, trạng thái và cách thay thế** tiếp nhận điểm tựa từ **40. phiên bản (version / 버전) tính tương thích (compatibility / 호환성): React 16.8 → 19.3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40B. di chuyển (migration / 마이그레이션) thực tế: cùng một tính năng (feature / 기능) qua ba thế hệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40A. Ma trận API cũ, trạng thái và cách thay thế

Bảng này dùng để tra cứu khi gặp mã (code / 코드) legacy. `Removed` nghĩa là API không còn được hỗ trợ ở phiên bản (version / 버전) được nêu; `Deprecated` nghĩa là có thể còn hoạt động ở một số phiên bản (version / 버전) nhưng không nên dùng cho mã (code / 코드) mới.

| API / mẫu (pattern / 패턴) cũ | Thường gặp ở | Trạng thái | Thay thế / cách hiểu hiện đại |
|---|---|---|---|
| `React.createClass` | React 0.x–15 | Deprecated khỏi cốt lõi (core / 핵심) từ 15.5 | ES6 lớp (class / 클래스); hiện nay ưu tiên hàm (function / 함수) thành phần (component / 컴포넌트) |
| mixins trong `createClass` | React cũ | Legacy | Composition, HOC/kết xuất (render / 렌더링) props, Custom Hooks |
| `React.PropTypes` | Trước 15.5 | Deprecated 15.5 | gói (package / 패키지) `prop-types`; với mã (code / 코드) mới thường TypeScript |
| `propTypes` trên hàm (function / 함수) thành phần (component / 컴포넌트) | 15.x–18 | React 19 không còn xử lý | TypeScript/lược đồ (schema / 스키마)/thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증) ở ranh giới (boundary / 경계) |
| `defaultProps` trên hàm (function / 함수) thành phần (component / 컴포넌트) | 15.x–18 | Removed hành vi (behavior / 동작) trong React 19 | default parameters |
| string refs `ref="x"` | React cũ | Deprecated 16.3, removed 19 | callback refs, `createRef`, `useRef` |
| `findDOMNode` | lớp (class / 클래스)/thư viện (library / 라이브러리) cũ | Deprecated 16.6, removed 19 | tường minh (explicit / 명시적) DOM refs |
| legacy ngữ cảnh (context / 맥락) `contextTypes`, `getChildContext` | Trước 16.3 | Deprecated 16.6, removed 19 | `createContext`, `contextType`, `useContext` |
| `componentWillMount` | lớp (class / 클래스) cũ | Deprecated name; `UNSAFE_*` legacy | initialization + mount synchronization phù hợp |
| `componentWillReceiveProps` | lớp (class / 클래스) cũ | Deprecated name; `UNSAFE_*` legacy | derive during kết xuất (render / 렌더링), reducer, controlled mô hình (model / 모델), rare `getDerivedStateFromProps` |
| `componentWillUpdate` | lớp (class / 클래스) cũ | Deprecated name; `UNSAFE_*` legacy | `componentDidUpdate`, `getSnapshotBeforeUpdate`, bố cục (layout / 레이아웃)/tác động (effect / 효과) lô-gic (logic / 논리) |
| `ReactDOM.render` | React 17 trở xuống | Deprecated 18, removed 19 | `createRoot(...).render(...)` |
| `ReactDOM.hydrate` | SSR React 17 trở xuống | Deprecated 18, removed 19 | `hydrateRoot` |
| `unmountComponentAtNode` | ReactDOM legacy gốc (root / 루트) | Deprecated 18, removed 19 | `root.unmount()` |
| kết xuất (render / 렌더링) callback của `ReactDOM.render` | Legacy gốc (root / 루트) | Không có one-to-one replacement | tác động (effect / 효과)/ref/callback theo ngữ nghĩa (semantics / 의미론) thực sự cần |
| `React.createFactory` | Pre-JSX / legacy | Deprecated 16.13, removed 19 | JSX / `createElement` |
| mô-đun (module / 모듈) mẫu (pattern / 패턴) factory thành phần (component / 컴포넌트) | Rare legacy | Deprecated 16.9, removed 19 | hàm (function / 함수) thành phần (component / 컴포넌트) bình thường |
| `react-dom/test-utils` helpers | kiểm thử (test / 테스트) cũ | Hầu hết removed/deprecated trong 19 | `act` từ `react`, Testing thư viện (library / 라이브러리) |
| `react-test-renderer` | đơn vị (unit / 단위)/thành phần (component / 컴포넌트) kiểm thử (test / 테스트) cũ | Deprecated trong React 19 | Testing thư viện (library / 라이브러리) hoặc môi trường (environment / 환경) gần người dùng (user / 사용자) hơn |
| `react-test-renderer/shallow` | shallow kiểm thử (test / 테스트) | Removed khỏi React 19 gói (package / 패키지) đường dẫn (path / 경로) | Tránh shallow nếu có thể |
| old JSX transform yêu cầu `import React` | React/toolchain cũ | React 19 yêu cầu hiện đại (modern / 현대적) transform | hiện đại (modern / 현대적) JSX transform |
| UMD React builds | script-tag legacy | React 19 ngừng phát hành UMD | ESM/CDN hoặc bản dựng (build / 빌드) công cụ (tool / 도구) |
| `element.ref` | element introspection | Deprecated React 19 | đọc `element.props.ref` nếu thật sự cần introspection |

### Cách dùng bảng này

Không nên nhìn cột “thay thế” như một bảng search-and-replace. Ví dụ `componentWillReceiveProps` có thể đã được dùng để đồng bộ prop vào trạng thái (state / 상태), gọi API, reset draft hoặc tính derived giá trị (value / 값); mỗi intent có một hướng migrate khác nhau. cấp cao (senior / 시니어) di chuyển (migration / 마이그레이션) luôn bắt đầu bằng việc xác định **ngữ nghĩa (semantics / 의미론)**, sau đó mới chọn API mới.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **40B. di chuyển (migration / 마이그레이션) thực tế: cùng một tính năng (feature / 기능) qua ba thế hệ** tiếp nhận điểm tựa từ **40A. Ma trận API cũ, trạng thái và cách thay thế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. cấp cao (senior / 시니어) Notes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40B. di chuyển (migration / 마이그레이션) thực tế: cùng một tính năng (feature / 기능) qua ba thế hệ

Giả sử cần subscribe một room theo `roomId`.

### React Class Component
Phần này nối mạch bài học với “React Class Component”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
class ChatRoom extends React.Component {
  componentDidMount() {
    this.connect(
      this.props.roomId
    );
  }

  componentDidUpdate(
    prevProps
  ) {
    if (
      prevProps.roomId !==
      this.props.roomId
    ) {
      this.disconnect();

      this.connect(
        this.props.roomId
      );
    }
  }

  componentWillUnmount() {
    this.disconnect();
  }

  connect(roomId) {
    this.connection =
      createConnection(roomId);

    this.connection.connect();
  }

  disconnect() {
    this.connection
      ?.disconnect();
  }

  render() {
    return <Chat />;
  }
}
```

### Function Component với Hooks
Phần này nối mạch bài học với “Function Component với Hooks”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
function ChatRoom({
  roomId,
}) {
  useEffect(() => {
    const connection =
      createConnection(roomId);

    connection.connect();

    return () => {
      connection.disconnect();
    };
  }, [roomId]);

  return <Chat />;
}
```

Hooks không chỉ “rút ngắn lớp (class / 클래스)”. Chúng gom lô-gic (logic / 논리) của cùng một synchronization concern lại thay vì chia `connect`/`disconnect` qua ba vòng đời (lifecycle / 생명주기).

### React 19.2+ với `useEffectEvent`

Nếu tác động (effect / 효과) chỉ cần restart khi `roomId` đổi nhưng callback muốn đọc `theme` mới nhất:

```jsx
function ChatRoom({
  roomId,
  theme,
}) {
  const onConnected =
    useEffectEvent(() => {
      showToast(
        "Connected",
        theme
      );
    });

  useEffect(() => {
    const connection =
      createConnection(roomId);

    connection.on(
      "connected",
      onConnected
    );

    connection.connect();

    return () => {
      connection.disconnect();
    };
  }, [roomId]);

  return <Chat />;
}
```

Điểm cần học không phải “phiên bản (version / 버전) mới luôn ngắn hơn”, mà là mỗi thế hệ React biểu đạt phụ thuộc (dependency / 의존성) và side tác động (effect / 효과) chính xác hơn.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **41. cấp cao (senior / 시니어) Notes** tiếp nhận điểm tựa từ **40B. di chuyển (migration / 마이그레이션) thực tế: cùng một tính năng (feature / 기능) qua ba thế hệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checklist Advanced/cấp cao (senior / 시니어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. cấp cao (senior / 시니어) Notes

**quyền sở hữu (ownership / 소유권) quan trọng hơn Hook.** Khi bug trạng thái (state / 상태) xảy ra, hỏi dữ liệu thuộc ai trước khi đổi Hook.

**tác động (effect / 효과) là tích hợp (integration / 통합) ranh giới (boundary / 경계).** Mỗi tác động (effect / 효과) nên có một bên ngoài (external / 외부) synchronization story rõ.

**máy chủ (server / 서버) trạng thái (state / 상태) không phải toàn cục (global / 전역) máy khách (client / 클라이언트) trạng thái (state / 상태).** truy vấn (query / 쿼리) bộ nhớ đệm (cache / 캐시) có stale/thử lại (retry / 재시도)/invalidate ngữ nghĩa (semantics / 의미론) riêng.

**thiết kế (design / 설계) hệ thống (system / 시스템) là API sản phẩm (product / 제품).** thành phần (component / 컴포넌트) thư viện (library / 라이브러리) có versioning, khả năng tiếp cận (accessibility / 접근성), composition và backward tính tương thích (compatibility / 호환성).

**hiệu năng (performance / 성능) phải đo.** Memoization không có profiler bằng chứng (evidence / 증거) thường chỉ là phỏng đoán.

**ranh giới bảo mật (security boundary / 보안 경계) nằm ở máy chủ (server / 서버).** máy khách (client / 클라이언트) không tạo authorization.

**khung phần mềm (framework / 프레임워크) matters.** RSC, router, bộ nhớ đệm (cache / 캐시) và triển khai (deployment / 배포) ngữ nghĩa (semantics / 의미론) thường do khung phần mềm (framework / 프레임워크) quyết định; không nên gọi tất cả là “React hành vi (behavior / 동작)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **Checklist Advanced/cấp cao (senior / 시니어)** tiếp nhận điểm tựa từ **41. cấp cao (senior / 시니어) Notes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Checklist Advanced/cấp cao (senior / 시니어)

Bạn nên có thể thiết kế app môi trường vận hành (production / 운영 환경) với ranh giới (boundary / 경계) rõ, chọn đúng cục bộ (local / 로컬)/ngữ cảnh (context / 맥락)/store/server-state/URL trạng thái (state / 상태), giải thích tính đồng thời (concurrency / 동시성)/Suspense, viết optimistic mutation có thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론), hiểu SSR/hydration/RSC, profile bottleneck thật, thiết kế reusable thành phần (component / 컴포넌트) API, xử lý khả năng tiếp cận (accessibility / 접근성) và kiểm thử (test / 테스트) theo rủi ro (risk / 위험).

Bạn cũng phải phân biệt được API thuộc React cốt lõi (core / 핵심), React DOM, RSC hay khung phần mềm (framework / 프레임워크) trước khi đưa vào codebase.

> **Bàn giao:** Sau **Checklist Advanced/cấp cao (senior / 시니어)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
