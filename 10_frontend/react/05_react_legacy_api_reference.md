# React Legacy API tham chiếu (reference / 참조) — React 15 → 18

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **React Legacy API tham chiếu (reference / 참조) — React 15 → 18**. Route đi từ cách tra cứu legacy file → old pattern và modern replacement → reason, migration và compatibility → khi còn gặp trong codebase → giới hạn/version notes, để tài liệu giúp đọc và nâng cấp mã cũ.

> tệp (file / 파일) này là phần bổ sung cho bốn mức (level / 수준) chính. Không nên đọc trước Beginner. Mục tiêu là tra cứu nhanh nhưng vẫn đủ giải thích khi gặp dự án (project / 프로젝트) cũ.

## 1. Cách dùng tệp (file / 파일) này

> **Chuyển mạch:** Cách dùng file xác định đây là tài liệu tra cứu sau Beginner; **Old → new → reason → migration** biến mỗi API thành một quyết định có ngữ nghĩa, không phải bảng thay tên.

## 1A. Old pattern → new pattern → reason → migration → khi còn gặp
Phần này nối mạch bài học với “1A. Old pattern → new pattern → reason → migration → khi còn gặp”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

> **Chuyển mạch:** Bảng migration đặt intent trước API; phần component creation/composition tiếp theo áp dụng nguyên tắc đó vào createClass, mixins, HOC và render props.

## 1A. Old mẫu (pattern / 패턴) → new mẫu (pattern / 패턴) → reason → di chuyển (migration / 마이그레이션) → khi còn gặp

| Old | New/default | Reason và di chuyển (migration / 마이그레이션) | Khi còn gặp |
|---|---|---|---|
| `createClass` + mixins | lớp (class / 클래스) rồi hàm (function / 함수) thành phần (component / 컴포넌트) + Hooks | mixin phụ thuộc (dependency / 의존성)/autobind khó compose; tách concern từng phần trước khi đổi thành phần (component / 컴포넌트) form | React 0.x–15 |
| lớp (class / 클래스) trạng thái (state / 상태)/vòng đời (lifecycle / 생명주기) | hàm (function / 함수) thành phần (component / 컴포넌트) + Hooks | colocate concern; map quyền sở hữu trạng thái (state ownership / 상태 소유권) trước, không đổi vòng đời (lifecycle / 생명주기) 1:1 sang tác động (effect / 효과) | React 15–18 enterprise |
| `componentWill*` | derivation/reducer/`componentDidUpdate`/tác động (effect / 효과) tùy intent | kết xuất (render / 렌더링) phase có thể restart; xác định derive, reset, DOM hay mạng (network / 네트워크) rồi chọn thành phần nguyên thủy (primitive / 기본 요소) | `UNSAFE_*` legacy |
| HOC / kết xuất (render / 렌더링) props | Custom Hook/composition khi phù hợp | giảm wrapper/prop collision; giữ old mẫu (pattern / 패턴) nếu là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) | Redux/router/headless libraries |
| `ReactDOM.render`/`hydrate` | `createRoot`/`hydrateRoot` | hiện đại (modern / 현대적) gốc (root / 루트) mở React 18 scheduling/batching; nâng 18.3 trước 19 và retest | React ≤17 bootstrap |
| string refs / `findDOMNode` | tường minh (explicit / 명시적) refs | quyền sở hữu (ownership / 소유권)/composition/tính đồng thời (concurrency / 동시성) rõ hơn | animation/UI libs cũ |
| legacy ngữ cảnh (context / 맥락) | `createContext` + hiện đại (modern / 현대적) consumers | propagation/composition rõ hơn | pre-16.3 |
| mount-lifecycle fetch | tác động (effect / 효과) hoặc truy vấn (query / 쿼리)/tuyến (route / 경로)/máy chủ (server / 서버) tầng (layer / 계층) | cancellation/bộ nhớ đệm (cache / 캐시)/dedupe/vô hiệu hóa (invalidation / 무효화) tốt hơn | React 15–17 screens |
| giant Redux store | cục bộ (local / 로컬) + URL + form + server-state + bên ngoài (external / 외부) store theo quyền sở hữu (ownership / 소유권) | các dữ liệu có vòng đời (lifecycle / 생명주기) khác nhau không nên mặc định chung store | enterprise Redux |
| Enzyme/shallow instance tests | DOM hành vi (behavior / 동작)/tích hợp (integration / 통합)/E2E | giảm coupling hiện thực (implementation / 구현); migrate assertion trước khi refactor thành phần (component / 컴포넌트) | class-era kiểm thử (test / 테스트) suites |

Quy tắc là **migrate ngữ nghĩa (semantics / 의미론), không migrate tên API**. Một vòng đời (lifecycle / 생명주기) cũ có thể làm nhiều việc; tách kết xuất (render / 렌더링) derivation, người dùng (user / 사용자) sự kiện (event / 이벤트) và bên ngoài (external / 외부) synchronization trước khi chọn API mới.

> **Chuyển mạch:** Composition cho thấy legacy API tạo và chia sẻ behavior thế nào; class APIs tiếp theo tập trung vào state, setState và escape hatches của chính class.

## 2. thành phần (component / 컴포넌트) creation và composition

### `React.createClass`

`React.createClass(spec)` tạo thành phần (component / 컴포넌트) từ đối tượng (object / 객체) specification. API này từng cung cấp `getInitialState`, `getDefaultProps`, vòng đời (lifecycle / 생명주기), methods và mixins. Methods được autobind. React 15.5 deprecate nó khỏi cốt lõi (core / 핵심); legacy mã (code / 코드) có thể dùng gói (package / 패키지) `create-react-class`.

```jsx
const Counter = React.createClass({
  getInitialState() {
    return { count: 0 };
  },

  render() {
    return (
      <button
        onClick={() =>
          this.setState({
            count:
              this.state.count + 1,
          })
        }
      >
        {this.state.count}
      </button>
    );
  },
});
```

### Mixins

Mixins bản sao (copy / 복사) một nhóm methods/vòng đời (lifecycle / 생명주기) vào nhiều `createClass` components. Chúng dễ tạo name collision và hidden phụ thuộc (dependency / 의존성). Về lịch sử, HOC/kết xuất (render / 렌더링) props và sau đó Hooks là các cách composition rõ hơn.

### Higher-Order Component
Phần này nối mạch bài học với “Higher-Order Component”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
const Enhanced =
  withFeature(Component);
```

HOC không bị remove. Đây là mẫu (pattern / 패턴) vẫn có thể hợp lệ, đặc biệt khi thư viện (library / 라이브러리) API được thiết kế từ thời pre-Hooks.

### Render props
Phần này nối mạch bài học với “Render props”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
<DataProvider>
  {data => <View data={data} />}
</DataProvider>
```

Vẫn hợp lệ. Hooks thường thuận tiện hơn khi mục tiêu là chia sẻ stateful lô-gic (logic / 논리).

> **Chuyển mạch:** Class APIs xác định state ownership và update contract; lifecycle APIs tiếp theo đặt các phương thức đó vào mount, update, unmount và error phases.

## 3. lớp (class / 클래스) APIs

### `this.state`

Cục bộ (local / 로컬) trạng thái (state / 상태) đối tượng (object / 객체) của lớp (class / 클래스).

### `this.setState(partialStateOrUpdater, callback?)`

Đối tượng (object / 객체) form shallow-merges. Updater form nên dùng khi trạng thái (state / 상태) mới phụ thuộc trạng thái (state / 상태) cũ.

```jsx
this.setState(
  state => ({
    count: state.count + 1,
  }),
  () => {
    console.log("committed");
  }
);
```

Callback của `setState` là API lớp (class / 클래스); Hook setter không có callback parameter tương đương.

### `this.forceUpdate(callback?)`

Ép cập nhật (update / 업데이트) khi dữ liệu bên ngoài React thay đổi mà thành phần (component / 컴포넌트) không nhận trạng thái (state / 상태)/props cập nhật (update / 업데이트) bình thường. Đây là escape hatch, không nên là luồng dữ liệu (data flow / 데이터 흐름) chính.

### `React.PureComponent`

Thêm shallow comparison mặc định cho props/trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **React Legacy API tham chiếu (reference / 참조) — React 15 → 18**, **3. lớp (class / 클래스) APIs** xác định đầu vào; **4. vòng đời (lifecycle / 생명주기) APIs** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. Refs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. vòng đời (lifecycle / 생명주기) APIs

### Mount

`constructor` → `render` → `componentDidMount`.

### Cập nhật (update / 업데이트)

`shouldComponentUpdate` → `render` → `getSnapshotBeforeUpdate` → `componentDidUpdate`, với `getDerivedStateFromProps` tham gia theo vòng đời (lifecycle / 생명주기) phù hợp.

### Unmount

`componentWillUnmount`.

### Lỗi (error / 오류)

`getDerivedStateFromError` + `componentDidCatch`.

### Unsafe legacy lifecycles

`componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` là tên cũ. Các tên `UNSAFE_...` tồn tại để làm rõ rằng các giả định (assumptions / 가정들) của chúng không an toàn với rendering hiện đại. Không migrate bằng search-replace sang tác động (effect / 효과); phải xác định intent.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Legacy API tham chiếu (reference / 참조) — React 15 → 18**, **4. vòng đời (lifecycle / 생명주기) APIs** xác định đầu vào; **5. Refs** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Refs

### String refs
Phần này nối mạch bài học với “String refs”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
<input ref="input" />
```

Đọc qua `this.refs.input`. Deprecated 16.3, removed 19.

### Callback refs
Phần này nối mạch bài học với “Callback refs”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
<input
  ref={node => {
    this.input = node;
  }}
/>
```

Vẫn hợp lệ.

### `createRef`

React 16.3+, thường dùng cho lớp (class / 클래스).

### `forwardRef`

React 16.3+, đặc biệt quan trọng cho React 18/thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성).

### `useRef`

React 16.8+, dùng trong hàm (function / 함수) thành phần (component / 컴포넌트).

### ref-as-prop

React 19 cho hàm (function / 함수) thành phần (component / 컴포넌트) nhận `ref` như prop.

### `findDOMNode`

Escape hatch tìm DOM từ thành phần (component / 컴포넌트) instance. Deprecated 16.6, removed 19. Thay bằng tường minh (explicit / 명시적) ref.

> **Chuyển mạch:** Refs giữ imperative handle tới node/instance; context truyền dependency qua cây mà không biến ref thành global state. React element APIs tiếp theo mô tả object được tạo ra từ render.

## 6. ngữ cảnh (context / 맥락)

### Legacy ngữ cảnh (context / 맥락)

`getChildContext`, `childContextTypes`, `contextTypes`. Deprecated 16.6, removed 19.

### New ngữ cảnh (context / 맥락)

`createContext`, `.Provider`, `.Consumer`, lớp (class / 클래스) `contextType`, Hook `useContext`. React 19 thêm provider shorthand `<Context value={...}>`.

> **Chuyển mạch:** Context giải thích dữ liệu đi qua component tree; element APIs mô tả giá trị render tương ứng. ReactDOM legacy APIs tiếp theo đặt element vào root và DOM lifecycle.

## 7. React element APIs

### `createElement`

Vẫn hợp lệ và là thành phần nguyên thủy (primitive / 기본 요소) nền của JSX.

```jsx
React.createElement(
  "div",
  { className: "card" },
  "Hello"
);
```

### `cloneElement`

Vẫn tồn tại nhưng nên dùng cẩn thận vì implicit luồng dữ liệu (data flow / 데이터 흐름).

### `isValidElement`

Kiểm tra giá trị (value / 값) có phải React element hay không.

### `Children`

Nhóm API thường gặp:

```text
Children.map
Children.forEach
Children.count
Children.only
Children.toArray
```

Các API này vẫn tồn tại và hay gặp trong thành phần (component / 컴포넌트) thư viện (library / 라이브러리) cũ.

### `createFactory`

Deprecated 16.13, removed 19.

### `React.DOM.*`

DOM factory đời rất cũ; hiểu như tiền thân của JSX.

> **Chuyển mạch:** Element APIs tạo render values; ReactDOM legacy APIs quyết định root/hydration behavior. Runtime typing/defaults tiếp theo kiểm tra assumptions của component boundary.

## 8. ReactDOM legacy APIs

### `ReactDOM.render`

Entry gốc (root / 루트) cũ; deprecated 18, removed 19.

### `ReactDOM.hydrate`

Hydration cũ; deprecated 18, removed 19.

### `unmountComponentAtNode`

Unmount gốc (root / 루트) cũ; deprecated 18, removed 19.

### `findDOMNode`

Deprecated 16.6, removed 19.

### Kết xuất (render / 렌더링) callback

`ReactDOM.render` cũ từng nhận callback sau kết xuất (render / 렌더링). hiện đại (modern / 현대적) gốc (root / 루트) không có one-to-one replacement; phải chọn tác động (effect / 효과)/ref/callback phù hợp mục tiêu thực tế.

> **Chuyển mạch:** Root APIs expose runtime assumptions about props/types/defaults; Events tiếp theo đưa input người dùng vào cùng contract và propagation model.

## 9. thời gian chạy (runtime / 런타임) typing và defaults

### `React.PropTypes`

Deprecated 15.5; chuyển sang gói (package / 패키지) `prop-types`.

### `Component.propTypes`

Phổ biến từ React 15–18. hàm (function / 함수) thành phần (component / 컴포넌트) `propTypes` không còn được React 19 xử lý.

### `Component.defaultProps`

Hàm (function / 함수) thành phần (component / 컴포넌트) `defaultProps` bị loại trong React 19; dùng default parameter. lớp (class / 클래스) `defaultProps` vẫn có thể tồn tại.

> **Chuyển mạch:** Runtime defaults define the input shape; events exercise that shape through propagation and handler identity. Legacy testing tiếp theo kiểm tra behavior mà không khóa vào implementation trivia.

## 10. Events

React web cũ dùng pooled `SyntheticEvent`, nên mã (code / 코드) async từng cần `event.persist()`. React 17 bỏ pooling hành vi (behavior / 동작) đó trên web; mã (code / 코드) hiện đại thường không cần `persist()`.

> **Chuyển mạch:** Event behavior cung cấp test surface; JSX transform/import React tiếp theo giải thích source syntax nào tạo ra element và vì sao legacy build cần khác modern build.

## 11. Testing legacy

`react-test-renderer` bị deprecate ở React 19. `react-test-renderer/shallow` bị remove khỏi đường dẫn (path / 경로) đó. `react-dom/test-utils` helpers bị cắt giảm; `act` chuyển về `react`. Codebase Enzyme/shallow-heavy nên migrate về kiểm thử (test / 테스트) hành vi khi có thể.

> **Chuyển mạch:** Testing legacy giữ behavior ổn định trong khi JSX transform thay đổi compilation step. UMD builds tiếp theo đặt artifact đó vào môi trường không dùng module bundler.

## 12. JSX transform và import React

JSX transform cũ thường yêu cầu:

```jsx
import React from "react";
```

ngay cả khi mã (code / 코드) không gọi biến `React` trực tiếp, vì JSX được transform thành `React.createElement(...)`.

Hiện đại (modern / 현대적) JSX transform cho phép JSX không cần import React chỉ vì transform. React 19 yêu cầu hiện đại (modern / 현대적) transform.

> **Chuyển mạch:** UMD clarifies the distribution boundary of legacy React; 13A chuyển từ artifact compatibility sang lifecycle intent, để migration không thành search-and-replace.

## 13. UMD builds

Các dự án (project / 프로젝트) rất cũ có thể tải (load / 로드) React bằng script UMD trong HTML. React 19 không còn phát hành UMD bản dựng (build / 빌드) như trước; mã (code / 코드) hiện đại ưu tiên mô-đun (module / 모듈)/ESM hoặc bundler/khung phần mềm (framework / 프레임워크).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Legacy API tham chiếu (reference / 참조) — React 15 → 18**, **13. UMD builds** xác định đầu vào; **13A. Migrate vòng đời (lifecycle / 생명주기) theo intent thay vì map tên phương thức (method / 메서드) một-một** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **14. di chuyển (migration / 마이그레이션) checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13A. Migrate vòng đời (lifecycle / 생명주기) theo intent thay vì map tên phương thức (method / 메서드) một-một

Lớp (class / 클래스) vòng đời (lifecycle / 생명주기) thường chứa nhiều concern trong cùng phương thức (method / 메서드), nên bảng “phương thức (method / 메서드) cũ → Hook mới” chỉ là gợi ý đọc mã (code / 코드), không phải di chuyển (migration / 마이그레이션) recipe.

| Intent trong mã (code / 코드) cũ | Hướng hiện đại thường phù hợp | Ghi chú |
|---|---|---|
| Tính giá trị (value / 값) từ props/trạng thái (state / 상태) | tính trực tiếp trong kết xuất (render / 렌더링), đôi khi `useMemo` nếu thực sự đắt | tránh bản sao (copy / 복사) props vào trạng thái (state / 상태) rồi tác động (effect / 효과) sync |
| Setup/cleanup subscription | `useEffect` với phụ thuộc (dependency / 의존성) mô tả cấu hình (configuration / 구성) | nghĩ theo start/stop tiến trình (process / 프로세스) |
| DOM đo lường (measurement / 측정) trước paint | ref + `useLayoutEffect` | dùng tối thiểu vì khối (block / 블록) paint |
| người dùng (user / 사용자) click gây POST/điều hướng (navigation / 내비게이션) | sự kiện (event / 이벤트) handler / hành động (action / 동작) | không vòng qua flag + tác động (effect / 효과) |
| Nhiều sự kiện (event / 이벤트) cập nhật trạng thái (state / 상태) phức tạp | `useReducer` hoặc máy trạng thái (state machine / 상태 머신) | reducer phải pure |
| Reset cục bộ (local / 로컬) trạng thái (state / 상태) khi thực thể (entity / 엔터티) đổi | đổi định danh (identity / 식별자) bằng `key` hoặc mô hình (model / 모델) trạng thái (state / 상태) theo ID | thường rõ hơn tác động (effect / 효과) `setState` reset |
| lỗi (error / 오류) ranh giới (boundary / 경계) | có thể giữ lớp (class / 클래스) ranh giới (boundary / 경계) hiện hữu | không cần rewrite chỉ vì thành phần (component / 컴포넌트) con dùng Hooks |

Khi còn gặp `componentDidMount`/`componentDidUpdate`, hãy đọc side tác động (effect / 효과) cụ thể: một phương thức (method / 메서드) có thể vừa fetch, vừa log analytics, vừa sync DOM. di chuyển (migration / 마이그레이션) tốt thường tách chúng thành sự kiện (event / 이벤트)/tác động (effect / 효과)/ranh giới (boundary / 경계) riêng theo ngữ nghĩa (semantics / 의미론), nhờ đó phụ thuộc (dependency / 의존성) và cleanup trở nên rõ hơn.

> **Chuyển mạch:** Trong **React Legacy API tham chiếu (reference / 참조) — React 15 → 18**, **13A. Migrate vòng đời (lifecycle / 생명주기) theo intent thay vì map tên phương thức (method / 메서드) một-một** xác định đầu vào; **14. di chuyển (migration / 마이그레이션) checklist** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **14A. Khi nào nên giữ old mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. di chuyển (migration / 마이그레이션) checklist

Khi nâng một codebase cũ, đừng cố nhảy thẳng từ “API cũ” sang “API mới” bằng mechanical replacement. Trước hết xác định dự án (project / 프로젝트) đang ở React phiên bản (version / 버전) nào, renderer/gốc (root / 루트) API nào, khung phần mềm (framework / 프레임워크) pin phiên bản (version / 버전) gì và third-party thư viện (library / 라이브러리) nào dựa vào internals.

Một luồng (flow / 흐름) thực tế là: gốc (root / 루트) API → deprecated lớp (class / 클래스)/ngữ cảnh (context / 맥락)/ref APIs → tests → TypeScript/types → Strict chế độ (mode / 모드)/tính đồng thời (concurrency / 동시성) các giả định (assumptions / 가정들) → khung phần mềm (framework / 프레임워크)/máy chủ (server / 서버) tích hợp (integration / 통합). Với React 18 lên 19, React nhóm (team / 팀) khuyến nghị dùng 18.3 như bước cảnh báo trung gian.

> **Chuyển mạch:** Migration checklist ghi lại risk và rollback; 14A quyết định khi nào giữ legacy pattern vì public contract hoặc dependency chưa thể đổi. Version table sau đó tóm tắt mốc cần tra cứu.

## 14A. Khi nào nên giữ old mẫu (pattern / 패턴)

Legacy không đồng nghĩa phải rewrite. lớp (class / 클래스) thành phần (component / 컴포넌트) ổn định, có kiểm thử (test / 테스트) tốt và ít thay đổi có thể tiếp tục tồn tại; HOC/kết xuất (render / 렌더링) props vẫn hợp lệ nếu đó là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) của thư viện (library / 라이브러리); Redux cũ vẫn có giá trị khi lĩnh vực (domain / 도메인) cần centralized sự kiện (event / 이벤트) luồng (flow / 흐름), middleware hoặc selector ecosystem. Chi phí di chuyển (migration / 마이그레이션) phải được so với rủi ro và lợi ích thực tế.

Nên ưu tiên migrate khi old API đã bị remove ở mục tiêu (target / 대상) React, khi Strict/concurrent ngữ nghĩa (semantics / 의미론) phơi ra bug cleanup/purity, khi phụ thuộc (dependency / 의존성) cũ chặn bảo mật (security / 보안)/khung phần mềm (framework / 프레임워크) upgrade, hoặc khi mã (code / 코드) thay đổi thường xuyên và lớp trừu tượng (abstraction / 추상화) hiện tại làm tính năng (feature / 기능) công việc (work / 작업) ngày càng khó. Mục tiêu là giảm rủi ro (risk / 위험) và độ phức tạp (complexity / 복잡도) chứ không phải đạt “100% hàm (function / 함수) thành phần (component / 컴포넌트)”.

> **Chuyển mạch:** Version table chốt mốc API và boundary của tài liệu; khi gặp claim ngoài các mốc này, quay về canonical React source thay vì suy luận từ legacy behavior.

## 15. Bảng version nhanh
Phần này nối mạch bài học với “15. Bảng version nhanh”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

| API / khái niệm | Mốc phiên bản (version / 버전) cần nhớ |
|---|---|
| `React.createClass` deprecate khỏi cốt lõi (core / 핵심) | 15.5 |
| `React.PropTypes` deprecate khỏi cốt lõi (core / 핵심) | 15.5 |
| lỗi (error / 오류) ranh giới (boundary / 경계) / portals / Fiber generation | 16.0 |
| Fragment | 16.2 |
| new ngữ cảnh (context / 맥락) / `createRef` / `forwardRef` / `StrictMode` | 16.3 |
| `memo` / `lazy` / Suspense mã (code / 코드) splitting / `contextType` | 16.6 |
| Hooks | 16.8 |
| `UNSAFE_*` vòng đời (lifecycle / 생명주기) era | 16.9+ |
| `createFactory` deprecated | 16.13 |
| React 17 sự kiện (event / 이벤트)/gradual-upgrade generation | 17 |
| `createRoot`, automatic batching, transitions | 18 |
| 18.3 di chuyển (migration / 마이그레이션) warnings | 18.3 |
| Actions, `use`, ref-as-prop, legacy removals | 19.0 |
| `Activity`, `useEffectEvent` | 19.2 |
| stable View chuyển tiếp (transition / 전이) tích hợp (integration / 통합), Fragment refs | 19.3 |

> **Bàn giao:** Sau **15. Bảng version nhanh**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
