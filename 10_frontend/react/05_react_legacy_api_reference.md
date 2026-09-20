# React Legacy API Reference — React 15 → 18

> File này là phần bổ sung cho bốn level chính. Không nên đọc trước Beginner. Mục tiêu là tra cứu nhanh nhưng vẫn đủ giải thích khi gặp project cũ.

## 1. Cách dùng file này

Nếu gặp API lạ trong codebase cũ, hãy tìm ở đây để biết nó từng làm gì, version nào thường dùng, trạng thái hiện tại và hướng migrate. Việc một API được giữ trong tài liệu không có nghĩa API đó được khuyên dùng cho code mới.

## 2. Component creation và composition

### `React.createClass`

`React.createClass(spec)` tạo component từ object specification. API này từng cung cấp `getInitialState`, `getDefaultProps`, lifecycle, methods và mixins. Methods được autobind. React 15.5 deprecate nó khỏi core; legacy code có thể dùng package `create-react-class`.

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

Mixins copy một nhóm methods/lifecycle vào nhiều `createClass` components. Chúng dễ tạo name collision và hidden dependency. Về lịch sử, HOC/render props và sau đó Hooks là các cách composition rõ hơn.

### Higher-Order Component

```jsx
const Enhanced =
  withFeature(Component);
```

HOC không bị remove. Đây là pattern vẫn có thể hợp lệ, đặc biệt khi library API được thiết kế từ thời pre-Hooks.

### Render props

```jsx
<DataProvider>
  {data => <View data={data} />}
</DataProvider>
```

Vẫn hợp lệ. Hooks thường thuận tiện hơn khi mục tiêu là chia sẻ stateful logic.

## 3. Class APIs

### `this.state`

Local state object của class.

### `this.setState(partialStateOrUpdater, callback?)`

Object form shallow-merges. Updater form nên dùng khi state mới phụ thuộc state cũ.

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

Callback của `setState` là API class; Hook setter không có callback parameter tương đương.

### `this.forceUpdate(callback?)`

Ép update khi dữ liệu bên ngoài React thay đổi mà component không nhận state/props update bình thường. Đây là escape hatch, không nên là data flow chính.

### `React.PureComponent`

Thêm shallow comparison mặc định cho props/state.

## 4. Lifecycle APIs

### Mount

`constructor` → `render` → `componentDidMount`.

### Update

`shouldComponentUpdate` → `render` → `getSnapshotBeforeUpdate` → `componentDidUpdate`, với `getDerivedStateFromProps` tham gia theo lifecycle phù hợp.

### Unmount

`componentWillUnmount`.

### Error

`getDerivedStateFromError` + `componentDidCatch`.

### Unsafe legacy lifecycles

`componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` là tên cũ. Các tên `UNSAFE_...` tồn tại để làm rõ rằng assumptions của chúng không an toàn với rendering hiện đại. Không migrate bằng search-replace sang Effect; phải xác định intent.

## 5. Refs

### String refs

```jsx
<input ref="input" />
```

Đọc qua `this.refs.input`. Deprecated 16.3, removed 19.

### Callback refs

```jsx
<input
  ref={node => {
    this.input = node;
  }}
/>
```

Vẫn hợp lệ.

### `createRef`

React 16.3+, thường dùng cho class.

### `forwardRef`

React 16.3+, đặc biệt quan trọng cho React 18/library compatibility.

### `useRef`

React 16.8+, dùng trong Function Component.

### ref-as-prop

React 19 cho Function Component nhận `ref` như prop.

### `findDOMNode`

Escape hatch tìm DOM từ component instance. Deprecated 16.6, removed 19. Thay bằng explicit ref.

## 6. Context

### Legacy Context

`getChildContext`, `childContextTypes`, `contextTypes`. Deprecated 16.6, removed 19.

### New Context

`createContext`, `.Provider`, `.Consumer`, class `contextType`, Hook `useContext`. React 19 thêm provider shorthand `<Context value={...}>`.

## 7. React element APIs

### `createElement`

Vẫn hợp lệ và là primitive nền của JSX.

```jsx
React.createElement(
  "div",
  { className: "card" },
  "Hello"
);
```

### `cloneElement`

Vẫn tồn tại nhưng nên dùng cẩn thận vì implicit data flow.

### `isValidElement`

Kiểm tra value có phải React element hay không.

### `Children`

Nhóm API thường gặp:

```text
Children.map
Children.forEach
Children.count
Children.only
Children.toArray
```

Các API này vẫn tồn tại và hay gặp trong component library cũ.

### `createFactory`

Deprecated 16.13, removed 19.

### `React.DOM.*`

DOM factory đời rất cũ; hiểu như tiền thân của JSX.

## 8. ReactDOM legacy APIs

### `ReactDOM.render`

Entry root cũ; deprecated 18, removed 19.

### `ReactDOM.hydrate`

Hydration cũ; deprecated 18, removed 19.

### `unmountComponentAtNode`

Unmount root cũ; deprecated 18, removed 19.

### `findDOMNode`

Deprecated 16.6, removed 19.

### Render callback

`ReactDOM.render` cũ từng nhận callback sau render. Modern root không có one-to-one replacement; phải chọn Effect/ref/callback phù hợp mục tiêu thực tế.

## 9. Runtime typing và defaults

### `React.PropTypes`

Deprecated 15.5; chuyển sang package `prop-types`.

### `Component.propTypes`

Phổ biến từ React 15–18. Function Component `propTypes` không còn được React 19 xử lý.

### `Component.defaultProps`

Function Component `defaultProps` bị loại trong React 19; dùng default parameter. Class `defaultProps` vẫn có thể tồn tại.

## 10. Events

React web cũ dùng pooled `SyntheticEvent`, nên code async từng cần `event.persist()`. React 17 bỏ pooling behavior đó trên web; code hiện đại thường không cần `persist()`.

## 11. Testing legacy

`react-test-renderer` bị deprecate ở React 19. `react-test-renderer/shallow` bị remove khỏi path đó. `react-dom/test-utils` helpers bị cắt giảm; `act` chuyển về `react`. Codebase Enzyme/shallow-heavy nên migrate về test hành vi khi có thể.

## 12. JSX transform và import React

JSX transform cũ thường yêu cầu:

```jsx
import React from "react";
```

ngay cả khi code không gọi biến `React` trực tiếp, vì JSX được transform thành `React.createElement(...)`.

Modern JSX transform cho phép JSX không cần import React chỉ vì transform. React 19 yêu cầu modern transform.

## 13. UMD builds

Các project rất cũ có thể load React bằng script UMD trong HTML. React 19 không còn phát hành UMD build như trước; code hiện đại ưu tiên module/ESM hoặc bundler/framework.

## 14. Migration checklist

Khi nâng một codebase cũ, đừng cố nhảy thẳng từ “API cũ” sang “API mới” bằng mechanical replacement. Trước hết xác định project đang ở React version nào, renderer/root API nào, framework pin version gì và third-party library nào dựa vào internals.

Một flow thực tế là: root API → deprecated class/context/ref APIs → tests → TypeScript/types → Strict Mode/concurrency assumptions → framework/server integration. Với React 18 lên 19, React team khuyến nghị dùng 18.3 như bước cảnh báo trung gian.

## 15. Bảng version nhanh

| API / khái niệm | Mốc version cần nhớ |
|---|---|
| `React.createClass` deprecate khỏi core | 15.5 |
| `React.PropTypes` deprecate khỏi core | 15.5 |
| Error Boundary / portals / Fiber generation | 16.0 |
| Fragment | 16.2 |
| new Context / `createRef` / `forwardRef` / `StrictMode` | 16.3 |
| `memo` / `lazy` / Suspense code splitting / `contextType` | 16.6 |
| Hooks | 16.8 |
| `UNSAFE_*` lifecycle era | 16.9+ |
| `createFactory` deprecated | 16.13 |
| React 17 event/gradual-upgrade generation | 17 |
| `createRoot`, automatic batching, transitions | 18 |
| 18.3 migration warnings | 18.3 |
| Actions, `use`, ref-as-prop, legacy removals | 19.0 |
| `Activity`, `useEffectEvent` | 19.2 |
| stable View Transition integration, Fragment refs | 19.3 |
