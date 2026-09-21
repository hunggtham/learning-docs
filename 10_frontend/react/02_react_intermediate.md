# React Master Note — Intermediate

> Mục tiêu của level này là chuyển từ “biết viết component” sang “hiểu vòng đời dữ liệu, Effect, ref, reducer, context, custom Hook, data flow và kiến trúc feature ở mức ứng dụng thật”.

> ### Version orientation cho level Intermediate
>
> Các Hook nền tảng `useState`, `useEffect`, `useRef`, `useContext`, `useReducer`, `useMemo`, `useCallback` đã tồn tại từ thời React 16.8, nhưng cách React scheduling/rendering chúng đã tiến hóa mạnh ở React 18+. Khi học file này, hãy dùng **React 19.3 semantics** làm chuẩn và chỉ quan tâm version khi API thật sự được thêm hoặc thay đổi contract.

## 1. Mô hình hóa state trước khi học Hook nâng cao

Trước khi thêm `useEffect`, `useMemo`, Context hoặc store, hãy phân loại dữ liệu. Nhiều code React phức tạp không phải vì thiếu Hook mà vì state được mô hình hóa sai. Một giá trị nên là state khi nó thay đổi theo thời gian và thay đổi đó phải ảnh hưởng render. Nếu có thể tính trực tiếp từ props/state hiện có, nó thường là derived value. Nếu cần tồn tại qua render nhưng thay đổi không cần render lại, `ref` thường phù hợp. Nếu dữ liệu thuộc server, URL hoặc cache ngoài React, đừng mặc định biến nó thành local state.

Không nên:

```jsx
const [items, setItems] = useState([]);
const [completedItems, setCompletedItems] = useState([]);

useEffect(() => {
  setCompletedItems(items.filter(item => item.done));
}, [items]);
```

Tốt hơn:

```jsx
const completedItems = items.filter(item => item.done);
```

Nguyên tắc này giảm duplicate source of truth và giảm Effect không cần thiết.

## 1A. Rules of React và Rules of Hooks

Hook phải gọi ở top level của Function Component hoặc Custom Hook, không tùy ý trong condition, loop, nested function hay event handler. React dựa vào thứ tự call ổn định để ghép mỗi Hook với state tương ứng giữa các render; vì vậy `eslint-plugin-react-hooks` là correctness tooling, không chỉ style.

Trước React 16.8, tái sử dụng stateful logic chủ yếu qua class, HOC và render props. Hooks giảm wrapper nesting và colocate concern tốt hơn nhưng không làm HOC/render props sai; chúng vẫn gặp trong Redux/router/library cũ. Migration nên chuyển concern chứ không search-replace syntax.

## 2. `useEffect`: synchronization chứ không phải “code chạy sau render”

`useEffect` dùng để đồng bộ component với một hệ thống nằm ngoài mô hình render React, ví dụ network connection, timer, browser event, WebSocket, observer, analytics integration hoặc widget imperative.

```jsx
import { useEffect } from "react";

function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = createConnection(roomId);
    connection.connect();

    return () => {
      connection.disconnect();
    };
  }, [roomId]);

  return <h1>Room {roomId}</h1>;
}
```

Mental model đúng là setup/cleanup synchronization. Khi `roomId` đổi, React cleanup connection cũ rồi setup connection mới.

Không truyền dependency array nghĩa Effect có thể chạy sau mỗi commit phù hợp. `[]` thường biểu diễn setup theo lifetime instance. `[roomId]` nghĩa synchronization phụ thuộc `roomId`. Dependency không phải công cụ để “ép chạy ít lần”; nó phải phản ánh reactive value Effect đọc.

> ### Version Note — `useEffect` không đổi thành “lifecycle mới”
>
> `useEffect` có từ React 16.8, nhưng React 18 Strict Mode khiến các Effect viết sai cleanup dễ lộ hơn vì development có thể setup/cleanup thêm để kiểm tra. Vì vậy các tutorial cũ mô tả `useEffect(..., [])` đơn giản là “`componentDidMount` cho function component” là cách hiểu thiếu chính xác. Mental model synchronization trong tài liệu này phù hợp hơn với React 18/19 và concurrency.

## 2A. Class lifecycle đầy đủ và cách đọc code React cũ

Trước Hooks, lifecycle methods là cách chính để chạy logic theo các giai đoạn của Class Component. Khi bảo trì code cũ, đừng chỉ nhớ tên method; cần hiểu method thuộc render phase hay commit phase và vì sao một số lifecycle bị đánh dấu `UNSAFE_`.

### Mount lifecycle

```jsx
class ChatRoom extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      messages: [],
    };
  }

  componentDidMount() {
    this.connection = createConnection(
      this.props.roomId
    );

    this.connection.connect();
  }

  componentWillUnmount() {
    this.connection.disconnect();
  }

  render() {
    return (
      <MessageList
        messages={this.state.messages}
      />
    );
  }
}
```

`constructor` dùng để khởi tạo state/bind. `render` tính UI. `componentDidMount` chạy sau commit và thường dùng setup subscription, network integration hoặc DOM work. `componentWillUnmount` cleanup resource.

Function Component thường gom setup/cleanup của cùng một concern:

```jsx
useEffect(() => {
  const connection =
    createConnection(roomId);

  connection.connect();

  return () => {
    connection.disconnect();
  };
}, [roomId]);
```

Đây là lý do không nên nghĩ `useEffect(..., [])` đơn giản là bản thay thế `componentDidMount`.

### Update lifecycle: `componentDidUpdate`

```jsx
componentDidUpdate(prevProps) {
  if (
    prevProps.roomId !==
    this.props.roomId
  ) {
    this.connection.disconnect();

    this.connection =
      createConnection(
        this.props.roomId
      );

    this.connection.connect();
  }
}
```

Class developer phải tự so sánh previous/current props. Effect dependency hiện đại biểu đạt intent đồng bộ theo `roomId` trực tiếp hơn.

### `shouldComponentUpdate`

```jsx
shouldComponentUpdate(
  nextProps,
  nextState
) {
  return (
    nextProps.user !==
      this.props.user ||
    nextState.open !==
      this.state.open
  );
}
```

Method này cho phép bỏ qua update. `PureComponent` làm shallow comparison tự động. Với Function Component, `memo` là khái niệm gần; `useMemo` và `useCallback` kiểm soát value/function identity.

### `getSnapshotBeforeUpdate`

API này chạy ngay trước DOM commit và giá trị trả về được truyền vào `componentDidUpdate`. Use case điển hình là giữ vị trí scroll.

```jsx
getSnapshotBeforeUpdate(prevProps) {
  if (
    prevProps.items.length <
    this.props.items.length
  ) {
    const list = this.listRef.current;

    return (
      list.scrollHeight -
      list.scrollTop
    );
  }

  return null;
}

componentDidUpdate(
  prevProps,
  prevState,
  snapshot
) {
  if (snapshot !== null) {
    const list = this.listRef.current;

    list.scrollTop =
      list.scrollHeight - snapshot;
  }
}
```

Không có Hook một-một hoàn toàn tương đương mọi chi tiết lifecycle này. Tùy mục tiêu có thể dùng `useLayoutEffect`, refs hoặc thay đổi data model.

### `static getDerivedStateFromProps`

```jsx
static getDerivedStateFromProps(
  props,
  state
) {
  if (
    props.userId !==
    state.prevUserId
  ) {
    return {
      prevUserId: props.userId,
      draft: "",
    };
  }

  return null;
}
```

API này xử lý một số derived-state cases nhưng dễ tạo duplicated state. Với code hiện đại, thường nên cân nhắc derive trực tiếp, reset bằng `key`, controlled model hoặc reducer trước.

### Các lifecycle cũ `componentWill*`

Code legacy có thể có:

```jsx
componentWillMount()
componentWillReceiveProps(nextProps)
componentWillUpdate(nextProps, nextState)
```

Các method này được đổi sang:

```jsx
UNSAFE_componentWillMount()
UNSAFE_componentWillReceiveProps()
UNSAFE_componentWillUpdate()
```

Vấn đề của chúng là side effect hoặc assumptions trong render-phase work không an toàn với rendering có thể bị restart, suspend hoặc bỏ. Không migrate bằng search-replace. `componentWillMount` thường tách initialization vào constructor/state initializer và side effect vào mount Effect/lifecycle; `componentWillReceiveProps` thường thay bằng render derivation, controlled data hoặc reducer; `componentWillUpdate` thường chuyển sang `componentDidUpdate`, `getSnapshotBeforeUpdate` hoặc layout/effect logic tùy mục tiêu.

## 3. Dependency và stale closure

Mỗi render tạo closure mới. Function trong render nhìn thấy props/state của render đó.

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      console.log(count);
    }, 1000);

    return () => clearInterval(id);
  }, []);
}
```

Interval giữ `count` của render đầu tiên. Tắt lint rule không sửa bản chất. Nếu interval phải phụ thuộc count, thêm dependency. Nếu connection phải ổn định nhưng callback cần đọc value mới nhất, React 19.2+ có `useEffectEvent`, sẽ học ở Advanced.

Object/function tạo trong render có identity mới:

```jsx
const options = { serverUrl, roomId };

useEffect(() => {
  return connect(options);
}, [options]);
```

Effect restart mỗi render. Thường tốt hơn:

```jsx
useEffect(() => {
  const options = { serverUrl, roomId };
  return connect(options);
}, [serverUrl, roomId]);
```

Không dùng `useMemo` theo phản xạ chỉ để “làm dependency yên”. Trước tiên sửa cấu trúc.

## 4. Cleanup, race condition và `AbortController`

Fetch trong Effect có thể gặp race condition: request cũ trả sau request mới rồi ghi đè dữ liệu. Có thể guard bằng flag hoặc tốt hơn, hủy request nếu API hỗ trợ.

```jsx
useEffect(() => {
  const controller = new AbortController();

  async function load() {
    try {
      const response = await fetch(`/api/users/${userId}`, {
        signal: controller.signal,
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const data = await response.json();
      setUser(data);
    } catch (error) {
      if (error.name !== "AbortError") {
        setError(error);
      }
    }
  }

  load();
  return () => controller.abort();
}, [userId]);
```

Ở production, server-state library hoặc framework data layer thường xử lý caching, dedupe, retry và race condition tốt hơn fetch Effect tự viết ở mọi component.

## 5. Khi nào không cần Effect?

Không dùng Effect để tính derived state:

```jsx
const fullName = `${firstName} ${lastName}`;
```

Không dùng Effect để phản ứng với event mà bạn đã biết nguyên nhân:

```jsx
async function handleSubmit(event) {
  event.preventDefault();
  await postForm();
}
```

thường tốt hơn pattern set một flag rồi Effect nhìn flag để gọi `postForm()`.

Effect phù hợp khi semantics là: “Vì component hiện đang tồn tại với cấu hình X nên resource bên ngoài phải được đồng bộ với X.”

## 6. `useRef`

`useRef(initialValue)` trả object ổn định `{ current }`. Thay đổi `ref.current` không trigger render.

```jsx
const timerRef = useRef(null);

function start() {
  timerRef.current = setInterval(...);
}
```

Ref phù hợp với timer ID, DOM node, instance thư viện, observer, mutable technical value. Không dùng ref thay state nếu UI cần phản ánh giá trị đó.

## 7. DOM ref và imperative escape hatch

```jsx
function SearchBox() {
  const inputRef = useRef(null);

  function focusInput() {
    inputRef.current?.focus();
  }

  return (
    <>
      <input ref={inputRef} />
      <button onClick={focusInput}>Focus</button>
    </>
  );
}
```

Ref phù hợp cho focus, selection, scroll, measurement hoặc tích hợp DOM library imperative. Không mutate DOM mà React đang quản lý theo cách xung đột với render.

## 8. `forwardRef` và ref-as-prop

React 18/code cũ thường dùng:

```jsx
const MyInput = forwardRef(function MyInput(props, ref) {
  return <input {...props} ref={ref} />;
});
```

React 19 hỗ trợ ref như prop trong function component theo model mới:

```jsx
function MyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}
```

Không xóa `forwardRef` tùy tiện trong library hỗ trợ React 18.

> ### Version Note — ref API thay đổi đáng chú ý ở React 19
>
> `useRef` bản thân không phải API mới của React 19. Thay đổi đáng chú ý là **Function Component có thể nhận `ref` như prop trong React 19**, làm giảm nhu cầu dùng `forwardRef` trong code mới. Tuy vậy `forwardRef` vẫn xuất hiện dày đặc trong library và codebase React 18, nên cần biết cả hai dạng.

## 7A. Lịch sử refs: string refs → callback refs → `createRef` → `useRef` → ref-as-prop

Refs thay đổi nhiều qua lịch sử React.

### String refs — legacy và đã bị remove

```jsx
class Search extends React.Component {
  componentDidMount() {
    this.refs.input.focus();
  }

  render() {
    return <input ref="input" />;
  }
}
```

React lưu node vào `this.refs.input`. String refs có hạn chế về owner, static analysis và composition; bị deprecate từ React 16.3 và remove trong React 19.

### Callback refs

```jsx
class Search extends React.Component {
  componentDidMount() {
    this.input.focus();
  }

  render() {
    return (
      <input
        ref={node => {
          this.input = node;
        }}
      />
    );
  }
}
```

Callback refs vẫn là API hợp lệ và rất linh hoạt.

### `React.createRef` — React 16.3+

```jsx
class Search extends React.Component {
  inputRef = React.createRef();

  componentDidMount() {
    this.inputRef.current.focus();
  }

  render() {
    return (
      <input ref={this.inputRef} />
    );
  }
}
```

`createRef` thường dùng cho Class Component; mỗi lần gọi tạo object mới nên thường khởi tạo một lần.

### `useRef` — React 16.8+

```jsx
function Search() {
  const inputRef = useRef(null);

  return (
    <button
      onClick={() =>
        inputRef.current?.focus()
      }
    >
      Focus
    </button>
  );
}
```

### `forwardRef` — React 16.3+

```jsx
const MyInput = forwardRef(
  function MyInput(props, ref) {
    return (
      <input
        {...props}
        ref={ref}
      />
    );
  }
);
```

React 19 cho Function Component nhận `ref` như prop:

```jsx
function MyInput({
  ref,
  ...props
}) {
  return (
    <input
      {...props}
      ref={ref}
    />
  );
}
```

Library support React 18 vẫn cần `forwardRef`, vì vậy không nên xóa nó chỉ vì project chính đã lên React 19.

## 7B. `findDOMNode`: escape hatch legacy

Class code cũ hoặc third-party library có thể dùng:

```jsx
import {
  findDOMNode,
} from "react-dom";

class AutoFocus extends React.Component {
  componentDidMount() {
    const node = findDOMNode(this);
    node.focus();
  }

  render() {
    return <input />;
  }
}
```

`findDOMNode` đi xuyên abstraction từ component instance xuống DOM, phụ thuộc structure render và khó tương thích với refactoring/concurrent architecture. API bị deprecate từ React 16.6 và remove trong React 19.

Thay bằng explicit ref:

```jsx
function AutoFocus() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return (
    <input ref={inputRef} />
  );
}
```

Nếu Strict Mode báo warning `findDOMNode`, dependency cũ có thể là nguồn warning; cần upgrade hoặc thay integration.

## 9. `useReducer`

`useReducer` phù hợp khi state có nhiều transition liên quan hoặc logic update phức tạp.

```jsx
function reducer(state, action) {
  switch (action.type) {
    case "added":
      return [...state, {
        id: action.id,
        text: action.text,
        done: false,
      }];

    case "toggled":
      return state.map(todo =>
        todo.id === action.id
          ? { ...todo, done: !todo.done }
          : todo
      );

    case "deleted":
      return state.filter(todo => todo.id !== action.id);

    default:
      throw new Error(`Unknown action: ${action.type}`);
  }
}
```

Dùng:

```jsx
const [todos, dispatch] = useReducer(reducer, []);

dispatch({
  type: "added",
  id: crypto.randomUUID(),
  text,
});
```

Reducer phải pure. Action nên mô tả intent hoặc điều xảy ra thay vì cách mutate chi tiết.

## 10. Context và `useContext`

Context truyền dữ liệu xuyên subtree mà không phải prop drilling qua các tầng không cần dữ liệu đó.

```jsx
import { createContext, useContext } from "react";

const ThemeContext = createContext("light");

function App() {
  return (
    <ThemeContext value="dark">
      <Toolbar />
    </ThemeContext>
  );
}

function Button() {
  const theme = useContext(ThemeContext);
  return <button className={theme}>Save</button>;
}
```

React 19 cho phép render Context object trực tiếp như provider. React 18 thường dùng `<ThemeContext.Provider value="dark">`.

Context phù hợp theme, locale, auth/session view-model hoặc dependency theo subtree. Không nên biến mọi state thành Context. Provider value đổi identity có thể làm consumer render lại; giant context tạo coupling lớn.

> ### Version Note — Provider syntax của React 19
>
> Với React 18 và code cũ, provider thường viết `<ThemeContext.Provider value={theme}>`. React 19 cho phép viết ngắn trực tiếp `<ThemeContext value={theme}>`. Hai đoạn code thể hiện cùng ý tưởng data flow; khác biệt chủ yếu là syntax/version. Khi viết library phải cân nhắc version tối thiểu mà package hỗ trợ.

## 10A. Context cũ: `contextTypes` và `getChildContext`

Trước new Context API, Class Component dùng legacy context mechanism:

```jsx
class ThemeProvider extends React.Component {
  getChildContext() {
    return {
      theme: "dark",
    };
  }

  render() {
    return this.props.children;
  }
}

ThemeProvider.childContextTypes = {
  theme: PropTypes.string,
};
```

Consumer:

```jsx
class Button extends React.Component {
  render() {
    return (
      <button
        className={
          this.context.theme
        }
      >
        Save
      </button>
    );
  }
}

Button.contextTypes = {
  theme: PropTypes.string,
};
```

Legacy Context khó refactor và có behavior dễ gây lỗi. React 16.3 giới thiệu new Context API:

```jsx
const ThemeContext =
  React.createContext("light");
```

Class consumer:

```jsx
class Button extends React.Component {
  static contextType =
    ThemeContext;

  render() {
    return (
      <button
        className={this.context}
      >
        Save
      </button>
    );
  }
}
```

Function Component:

```jsx
const theme =
  useContext(ThemeContext);
```

Legacy `contextTypes`/`getChildContext` bị deprecate từ React 16.6 và remove trong React 19.

## 11. Reducer + Context

Một pattern client-state theo subtree:

```jsx
const TodosContext = createContext(null);
const TodosDispatchContext = createContext(null);

function TodosProvider({ children }) {
  const [todos, dispatch] = useReducer(todosReducer, []);

  return (
    <TodosContext value={todos}>
      <TodosDispatchContext value={dispatch}>
        {children}
      </TodosDispatchContext>
    </TodosContext>
  );
}
```

Pattern này tốt khi scope rõ. Nếu state lớn, update liên tục và nhiều consumer cần selector, external store có thể phù hợp hơn.

## 12. Custom Hooks

Custom Hook là function bắt đầu bằng `use` và có thể gọi Hook khác. Nó tái sử dụng stateful logic chứ không chia sẻ cùng state instance.

```jsx
function useOnlineStatus() {
  const [online, setOnline] = useState(navigator.onLine);

  useEffect(() => {
    function onOnline() { setOnline(true); }
    function onOffline() { setOnline(false); }

    window.addEventListener("online", onOnline);
    window.addEventListener("offline", onOffline);

    return () => {
      window.removeEventListener("online", onOnline);
      window.removeEventListener("offline", onOffline);
    };
  }, []);

  return online;
}
```

Mỗi caller có state riêng. Nếu cần một store chia sẻ thật, phải dùng Context/external store hoặc nguồn dữ liệu chung.

API Hook nên rõ input/output:

```jsx
const { data, error, status, refetch } = useUser(userId);
```

Đừng expose quá nhiều setter nội bộ nếu cần giữ invariant.

## 12A. HOC và Render Props: pattern tái sử dụng logic trước Custom Hooks

Trước Hooks, hai pattern rất phổ biến để tái sử dụng stateful logic là Higher-Order Component và Render Props.

### Higher-Order Component

HOC là function nhận component và trả component mới:

```jsx
function withOnlineStatus(
  Component
) {
  return class
    extends React.Component {
    state = {
      online:
        navigator.onLine,
    };

    render() {
      return (
        <Component
          {...this.props}
          online={
            this.state.online
          }
        />
      );
    }
  };
}

const OnlineUser =
  withOnlineStatus(User);
```

HOC từng rất phổ biến trong Redux, routing và analytics. Nhược điểm thường gặp là wrapper hell, prop collision và dependency khó truy vết.

### Render Props

```jsx
<MousePosition>
  {position => (
    <Tooltip
      x={position.x}
      y={position.y}
    />
  )}
</MousePosition>
```

Component sở hữu logic nhưng giao quyền render cho consumer qua function prop.

### Custom Hook thay đổi điều gì?

```jsx
function Tooltip() {
  const position =
    useMousePosition();

  return (
    <div>
      {position.x},
      {position.y}
    </div>
  );
}
```

Custom Hook tái sử dụng stateful logic mà không tạo thêm wrapper component. Tuy nhiên HOC/render props không phải API bị remove; chúng vẫn hợp lệ khi library/API phù hợp.

## 13. `useMemo`, `useCallback`, `memo`

`useMemo` memoize value:

```jsx
const visibleItems = useMemo(
  () => filterItems(items, filter),
  [items, filter]
);
```

`useCallback` memoize function identity:

```jsx
const handleSelect = useCallback(id => {
  setSelectedId(id);
}, []);
```

`memo` cho component có thể skip render khi props được xem là không đổi:

```jsx
const Row = memo(function Row({ item, onSelect }) {
  return <button onClick={() => onSelect(item.id)}>{item.name}</button>;
});
```

Không memo hóa theo nghi thức. Memoization làm code phức tạp hơn và có chi phí. Profile trước. React Compiler stable càng làm manual memoization ít cần hơn trong code mới, nhưng manual API vẫn có vai trò escape hatch.

> ### Version Note — React Compiler thay đổi “best practice” memoization
>
> `memo`, `useMemo` và `useCallback` tồn tại từ trước React 19. Tuy nhiên **React Compiler 1.0** đã stable và có thể tự động memoize nhiều component/value. Vì vậy với codebase có Compiler, “bọc mọi thứ bằng `useMemo`/`useCallback`” càng không phải best practice. Vẫn phải hiểu ba API này để đọc code cũ, viết library, xử lý identity contract và tối ưu bottleneck đã profile.

## 14. `useId`

`useId` tạo ID ổn định phù hợp accessibility và hydration:

```jsx
function PasswordField() {
  const hintId = useId();

  return (
    <>
      <input type="password" aria-describedby={hintId} />
      <p id={hintId}>Ít nhất 12 ký tự.</p>
    </>
  );
}
```

Không dùng `useId` làm list key. Key phải đến từ data identity.

> ### Version Note — `useId` là API React 18
>
> `useId` được thêm ở React 18 để tạo ID ổn định giữa client/server, đặc biệt hữu ích cho accessibility và streaming SSR. Nếu project React 17 trở xuống, Hook này không tồn tại. Dù ở version nào, `useId` **không dùng để tạo `key` cho list**; key phải đến từ identity của dữ liệu.

## 15. `useLayoutEffect`

`useLayoutEffect` chạy ở timing cho phép đo layout và cập nhật trước paint thích hợp:

```jsx
useLayoutEffect(() => {
  const rect = ref.current.getBoundingClientRect();
  setHeight(rect.height);
}, []);
```

Chỉ dùng khi thật sự cần measurement hoặc tránh visual flicker. Nó có thể block paint; `useEffect` vẫn là mặc định.

## 16. Portals

```jsx
import { createPortal } from "react-dom";

function Modal({ children }) {
  return createPortal(
    <div className="modal">{children}</div>,
    document.body
  );
}
```

Portal render host DOM ở nơi khác nhưng vẫn thuộc React tree. Event bubble theo React tree. Phù hợp modal, tooltip, popover, overlay.

## 17. Error Boundary

Error Boundary bắt render/lifecycle error trong subtree và hiển thị fallback. Core React vẫn dùng class cho Error Boundary truyền thống:

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    console.error(error, info);
  }

  render() {
    if (this.state.hasError) return <p>Đã có lỗi.</p>;
    return this.props.children;
  }
}
```

Error Boundary không thay `try/catch` cho event handler hoặc async operation tự gọi.

## 18. `lazy` và Suspense cơ bản

```jsx
import { lazy, Suspense } from "react";

const SettingsPage = lazy(() => import("./SettingsPage.jsx"));

function App() {
  return (
    <Suspense fallback={<p>Đang tải...</p>}>
      <SettingsPage />
    </Suspense>
  );
}
```

`lazy` thường cần module default export component. Suspense không phải wrapper tùy ý cho mọi Promise; data source/framework phải tích hợp với cơ chế suspend.

> ### Version Note — Suspense đã tiến hóa qua nhiều version
>
> `React.lazy` và Suspense cho code splitting xuất hiện từ React 16.6, nhưng Suspense cho server rendering/concurrency được mở rộng mạnh ở React 18 và tiếp tục phát triển ở React 19. Vì vậy khi đọc blog cũ, đừng suy ra rằng mọi ví dụ Suspense đều hỗ trợ data fetching giống nhau. Data source phải tích hợp Suspense hoặc đi qua framework/library hỗ trợ.

## 19. Data fetching phía client

Fetch trong Effect hữu ích để học nhưng server-state production thường cần nhiều hơn: cache, dedupe, stale time, retry, mutation, invalidation, pagination, optimistic update.

Một implementation thủ công tối thiểu:

```jsx
function UserPage({ userId }) {
  const [state, setState] = useState({
    status: "loading",
    data: null,
    error: null,
  });

  useEffect(() => {
    const controller = new AbortController();

    async function load() {
      setState({ status: "loading", data: null, error: null });

      try {
        const response = await fetch(`/api/users/${userId}`, {
          signal: controller.signal,
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        setState({ status: "success", data, error: null });
      } catch (error) {
        if (error.name === "AbortError") return;
        setState({ status: "error", data: null, error });
      }
    }

    load();
    return () => controller.abort();
  }, [userId]);
}
```

Server state có owner nằm ngoài client và có thể stale; client UI state như modal open lại thuộc app hiện tại. Không trộn tùy tiện hai loại này.

## 19A. Data fetching evolution: lifecycle → Effect → data layer → Suspense/RSC

Class code cũ thường fetch ở `componentDidMount`/`componentDidUpdate`; Hooks chuyển synchronization tương tự sang `useEffect`. Fetch Effect thủ công vẫn phải tự xử lý cancellation, race, cache, retry, dedupe và invalidation, nên production thường chuyển server state sang query/framework data layer. Suspense/RSC lại thay nơi request bắt đầu và cách loading được reveal; Suspense không tự biến mọi `fetch()` thành cache.

Old lifecycle fetch vẫn gặp nhiều trong React 15–17 và không cần rewrite chỉ vì dùng class. Migrate khi ownership, cancellation, cache hoặc routing architecture thực sự tốt hơn.

## 20. Router và URL state

Routing không thuộc React core. React Router phổ biến trong SPA; framework như Next.js có router riêng.

Search query, page, sort, filter và tab có ý nghĩa điều hướng thường nên nằm ở URL:

```text
/products?q=keyboard&page=2&sort=price
```

Nếu reload/back/forward phải khôi phục cùng màn hình, URL thường là source of truth tốt hơn local state.

Học router theo đúng major version vì API có thể thay đổi giữa các version.

## 21. Form thực tế

Không phải input nào cũng cần controlled state. Có thể dùng `FormData`:

```jsx
async function handleSubmit(event) {
  event.preventDefault();
  const formData = new FormData(event.currentTarget);

  const payload = {
    email: formData.get("email"),
    role: formData.get("role"),
  };

  await save(payload);
}
```

Browser validation dùng `required`, `minLength`, `pattern`, `type="email"`. Validation nghiệp vụ phức tạp có thể dùng schema validator/form library. Client validation cải thiện UX; server validation mới bảo vệ integrity/security.

## 21A. Forms qua các thế hệ

Controlled form có từ thời class: field nằm trong `this.state`; Hooks chuyển API sang `useState`/reducer nhưng source-of-truth model không đổi. Production form không nhất thiết controlled mọi field: `FormData`, native validation hoặc field subscription có thể giảm coupling. React 19 Actions/`useActionState`/`useFormStatus`/`useOptimistic` thêm async mutation workflow nhưng không xóa controlled/uncontrolled fundamentals.

## 22. Accessibility

React không tự làm UI accessible. Semantic HTML là nền tảng.

Tốt:

```jsx
<button onClick={save}>Lưu</button>
```

Không nên dùng `<div onClick>` để giả button nếu không có lý do rất đặc biệt, vì bạn sẽ phải tự xử lý role, keyboard, focus và states.

Label:

```jsx
<label htmlFor={emailId}>Email</label>
<input id={emailId} type="email" />
```

Modal cần accessible name, focus management, escape behavior và restore focus. ARIA không thay semantic HTML.

## 23. Testing

Test React nên ưu tiên hành vi người dùng hơn implementation detail.

```jsx
render(<LoginForm />);

await user.type(
  screen.getByLabelText(/email/i),
  "a@example.com"
);

await user.click(
  screen.getByRole("button", { name: /đăng nhập/i })
);

expect(
  await screen.findByText(/thành công/i)
).toBeInTheDocument();
```

Unit test phù hợp reducer/formatter. Component/integration test kiểm tra UI phối hợp. E2E kiểm tra critical flow bằng browser thật. Coverage 100% không phải mục tiêu nếu test không mang confidence.

## 24. Cấu trúc project

Không có folder structure React duy nhất. Với app vừa/lớn, feature-first thường scale tốt:

```text
src/
├─ app/
│  ├─ App.jsx
│  ├─ router.jsx
│  └─ providers.jsx
├─ features/
│  ├─ auth/
│  │  ├─ api/
│  │  ├─ components/
│  │  ├─ hooks/
│  │  └─ pages/
│  └─ products/
├─ shared/
│  ├─ components/
│  ├─ hooks/
│  ├─ lib/
│  └─ styles/
└─ main.jsx
```

Không đưa code vào `shared` quá sớm. Generalize sau khi nhu cầu tái sử dụng thật sự xuất hiện.

## 25. Kiến trúc feature điển hình

```text
UI component
   ↓
feature hook / controller hook
   ↓
server-state library / API client
   ↓
HTTP API
```

State nên ở gần nơi dùng. URL state ở URL. Server data ở server-state cache. Form state ở form. Truly global client state chỉ đưa vào store/context khi thực sự global.

## 25A. State management bắt đầu từ ownership

Trước khi chọn Context, Redux hay Zustand, hãy phân loại: local UI state ở component; form state ở form; filter/page shareable ở URL; server data ở query/framework cache; cross-feature client state mới là ứng viên external store. Redux/Flux đời cũ thường chứa mọi loại state vì ecosystem thiếu specialized layers. Old Redux vẫn hợp lý khi domain cần selector, middleware, devtools hoặc global event flow; không migrate chỉ vì library mới ngắn hơn.

## 26. Anti-pattern thường gặp

**Effect chain:** Effect A set state làm Effect B chạy rồi Effect C chạy. Thường có thể tính trong render hoặc xử lý transition trong event/reducer.

**God component:** vừa fetch, validate, transform, render, điều khiển nhiều modal. Tách theo responsibility, không theo số dòng máy móc.

**Premature context:** đưa state lên provider dù chỉ hai component gần nhau dùng.

**Manual memo everywhere:** làm dependency phức tạp và khó maintain.

**Copy props into state:**

```jsx
const [name, setName] = useState(props.name);
```

Nếu muốn luôn phản ánh prop, đây là lỗi. Chỉ copy khi cố ý tạo local draft có lifecycle reset rõ.

## 27. Checklist Intermediate

Bạn nên giải thích được Effect là synchronization chứ không phải lifecycle callback chung; hiểu stale closure; phân biệt ref và state; biết reducer phù hợp ở đâu; hiểu Context không đồng nghĩa global store; viết custom Hook có contract rõ; hiểu manual memoization chỉ có lý do khi có performance/identity requirement; phân biệt server state với client state; xây form/routing/data-fetching flow có loading/error/cancellation; và viết test theo hành vi user.

## Version checkpoint trước khi sang Advanced

Đến đây, version nên được hiểu theo “khả năng nào có sẵn” chứ không phải học lại React từ đầu cho từng release. Nếu project là React 18, bạn vẫn dùng hầu hết tư duy của file này nhưng chưa có ref-as-prop React 19, Context provider shorthand và các Action APIs mới. Nếu là React 19.0/19.1, bạn có nền Actions/`use` nhưng chưa có các API được thêm ở 19.2 như `useEffectEvent`/`Activity`, và chưa có stable View Transitions/Fragment refs của 19.3.

Khi copy code từ tài liệu hiện hành, luôn kiểm tra API đó thuộc `react`, `react-dom`, React Server Components hay framework. Đây là kỹ năng versioning quan trọng hơn việc thuộc bảng changelog.

## Senior Note chuyển tiếp

Khi ứng dụng có Suspense, transition, streaming, Actions hoặc Server Components, mental model “mount/update/unmount” kiểu class cũ không còn đủ. Level Advanced/Senior sẽ tập trung vào render/commit, concurrency, ownership, boundaries và production architecture.
