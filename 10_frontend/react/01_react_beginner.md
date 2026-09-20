# React Master Note — Beginner

> Baseline: React 19.3. Mục tiêu của file này là giúp người gần như bắt đầu từ số 0 hiểu React bằng mental model đúng trước khi học các Hook và architecture nâng cao.

## 1. React là gì?

React là thư viện JavaScript dùng để xây dựng giao diện người dùng theo mô hình khai báo và component. Điểm quan trọng nhất của React không phải JSX hay Hook, mà là tư duy “dữ liệu hiện tại quyết định giao diện hiện tại”. Thay vì trực tiếp tìm DOM node rồi ra lệnh sửa từng phần tử khi dữ liệu thay đổi, bạn mô tả UI cần trông như thế nào đối với props và state hiện tại. React chạy lại logic render, so sánh kết quả mới với cây hiện tại và commit những thay đổi cần thiết xuống DOM.

JavaScript DOM thuần thường mang tính imperative:

```js
const button = document.querySelector("#btn");
const label = document.querySelector("#count");
let count = 0;

button.addEventListener("click", () => {
  count += 1;
  label.textContent = count;
});
```

React cho phép mô tả UI từ state:

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Số lần bấm: {count}
    </button>
  );
}
```

React là thư viện UI chứ không phải một full-stack framework. Routing, data cache, authentication, server runtime, database và deployment thường đến từ thư viện hoặc framework khác. Vì vậy cần phân biệt React core với ecosystem.

> ### Version Note — nên học version nào trước?
>
> Nếu bắt đầu mới, hãy học theo cú pháp và mental model React 19.3 trong tài liệu này. Phần lớn kiến thức nền như component, props, state, event, list và form vẫn áp dụng cho React 18 và cả nhiều code React 16.8/17. Sự khác nhau lớn nhất khi đọc code cũ thường nằm ở entry API, Class Component, JSX transform và một số API mới của React 19; vì vậy không cần học từng version theo thứ tự lịch sử trước khi học React.

## 2. JavaScript nền tảng cần biết

React sử dụng JavaScript thật. Nếu không hiểu JavaScript, người học rất dễ thuộc cú pháp React nhưng không biết vì sao code chạy hoặc hỏng.

`const` nên là lựa chọn mặc định cho binding không cần gán lại; `let` dùng khi biến thực sự phải đổi trong cùng execution scope. `const` không làm object bất biến:

```js
const user = { name: "An" };
user.name = "Bình"; // hợp lệ
```

Function và arrow function xuất hiện liên tục:

```js
function add(a, b) {
  return a + b;
}

const multiply = (a, b) => a * b;
```

Destructuring được dùng để đọc props và kết quả Hook:

```js
const user = { id: 1, name: "Lan" };
const { id, name } = user;

const [first, second] = ["red", "blue"];
```

Spread syntax rất quan trọng vì state React thường được cập nhật theo kiểu tạo object/array mới:

```js
const nextUser = { ...user, name: "Bình" };
const nextItems = [...items, newItem];
```

Các array method phải quen gồm `map`, `filter`, `find`, `some`, `every`, `reduce`. Trong React, `map` dùng rất nhiều để render list.

Module ES:

```js
// Button.jsx
export default function Button() {
  return <button>OK</button>;
}

// App.jsx
import Button from "./Button.jsx";
```

Named export:

```js
export function Button() {}
export function Input() {}
```

Optional chaining và nullish coalescing:

```js
const city = user?.address?.city ?? "Chưa có";
```

`?.` dừng truy cập nếu giá trị trước là `null`/`undefined`. `??` chỉ fallback cho `null`/`undefined`, khác `||` vì `||` còn fallback cho `0`, `""`, `false`.

Promise và `async/await` cần thiết cho API:

```js
async function loadUsers() {
  const response = await fetch("/api/users");
  if (!response.ok) throw new Error("Không tải được dữ liệu");
  return response.json();
}
```

## 3. React app hoạt động như thế nào?

Ứng dụng web React thường dùng `react` cho model component/Hooks và `react-dom` để kết nối với DOM.

```jsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

Có thể hiểu một update qua ba bước lớn: một event hoặc nguồn dữ liệu làm props/state thay đổi; React render để tính cây UI mới; React commit thay đổi cần thiết xuống DOM. Browser sau đó layout và paint. “Component render lại” không đồng nghĩa toàn bộ DOM bị dựng lại.

> ### Version Note — `createRoot`
>
> `createRoot` là API client root hiện đại từ **React 18**. Tutorial React 17 trở xuống thường dùng `ReactDOM.render(<App />, container)`. React 18 đã deprecate cách cũ và nếu vẫn dùng nó, app không nhận đầy đủ behavior mới của root React 18; tới React 19, API render/hydrate legacy đã bị loại bỏ. Vì vậy code mới nên luôn nghĩ theo `createRoot` hoặc `hydrateRoot` nếu đang hydrate HTML từ server.

## 4. Tạo project React hiện đại

Create React App không còn là lựa chọn khuyến nghị cho project mới. Với học React core hoặc SPA client-side, Vite là lựa chọn phổ biến:

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

TypeScript:

```bash
npm create vite@latest my-react-app -- --template react-ts
```

Cấu trúc cơ bản:

```text
my-react-app/
├─ src/
│  ├─ App.jsx
│  ├─ main.jsx
│  └─ assets/
├─ public/
├─ index.html
├─ package.json
└─ vite.config.js
```

`.jsx` là JavaScript có JSX; `.tsx` là TypeScript có JSX.

> ### Version Note — Create React App không phải “React cũ”
>
> Create React App là toolchain, không phải React core. React team đã deprecate Create React App cho project mới vào năm 2025 và khuyến nghị framework hoặc build tool hiện đại như Vite/Parcel/RSBuild tùy nhu cầu. Một codebase CRA vẫn có thể chạy React 18 hoặc 19, nên hãy tách hai khái niệm: “version React” và “công cụ tạo/build project”.

### Root API cũ: `ReactDOM.render`, `hydrate`, `unmountComponentAtNode`

React 17 trở xuống thường khởi động app bằng:

```jsx
import ReactDOM from "react-dom";

ReactDOM.render(
  <App />,
  document.getElementById("root")
);
```

React 18 giới thiệu root API mới:

```jsx
import { createRoot } from "react-dom/client";

const root = createRoot(
  document.getElementById("root")
);

root.render(<App />);
```

`ReactDOM.render` bị deprecate từ React 18 và bị remove ở React 19. Nếu dùng API cũ trong React 18, app chạy theo compatibility behavior gần React 17 và không có đầy đủ modern root semantics.

SSR hydration cũ:

```jsx
ReactDOM.hydrate(
  <App />,
  document.getElementById("root")
);
```

được thay bằng:

```jsx
import { hydrateRoot } from "react-dom/client";

hydrateRoot(
  document.getElementById("root"),
  <App />
);
```

Unmount cũ:

```jsx
ReactDOM.unmountComponentAtNode(container);
```

được thay bằng:

```jsx
root.unmount();
```

Ba API legacy trên rất thường gặp trong project React 16/17 và tài liệu cũ, nên cần đọc được dù không dùng cho code mới.

## 5. JSX

JSX là cú pháp mở rộng của JavaScript cho phép viết cấu trúc gần giống HTML. Browser không hiểu JSX trực tiếp; build tool chuyển JSX thành mã JavaScript/runtime React.

```jsx
const element = <h1>Xin chào React</h1>;
```

JSX phải có một root hợp lệ. Nếu không muốn thêm DOM wrapper, dùng Fragment:

```jsx
return (
  <>
    <h1>Title</h1>
    <p>Content</p>
  </>
);
```

Nhúng JavaScript expression bằng `{}`:

```jsx
const user = { name: "An", age: 25 };
return <p>{user.name} — {user.age + 1}</p>;
```

Không đặt statement như `if` trực tiếp trong `{}`; dùng `if` trước return hoặc expression như ternary.

Một số attribute khác HTML:

```jsx
<div className="card">
  <label htmlFor="email">Email</label>
  <input id="email" tabIndex={0} />
</div>
```

Event dùng camelCase như `onClick`, `onChange`, `onSubmit`.

Boolean prop:

```jsx
<input disabled />
```

Inline style nhận object JavaScript và property camelCase:

```jsx
<div style={{ backgroundColor: "black", fontSize: 18 }} />
```

React escape giá trị text mặc định, giúp giảm nhiều XSS case:

```jsx
<p>{userInput}</p>
```

`dangerouslySetInnerHTML` bỏ lớp bảo vệ đó cho HTML raw và chỉ nên dùng với dữ liệu đã sanitize/trusted:

```jsx
<div dangerouslySetInnerHTML={{ __html: trustedHtml }} />
```

> ### Version Note — JSX transform
>
> Tutorial rất cũ thường bắt đầu file bằng `import React from "react";` dù biến `React` không được dùng trực tiếp. Lý do là JSX transform cũ biên dịch JSX thành lời gọi như `React.createElement(...)`. Modern JSX transform, được phổ biến từ giai đoạn React 17 và đã được backport cho một số version cũ hơn, cho phép JSX hoạt động mà không cần import React chỉ vì JSX. **React 19 yêu cầu modern JSX transform**, nên code mới không nên học thói quen import React chỉ để “JSX chạy”.

## 5A. JSX thực chất tạo React element: `createElement`, `cloneElement` và API cũ

JSX không phải requirement bắt buộc. JSX:

```jsx
<button className="primary">
  Save
</button>
```

về mặt ý tưởng tương đương:

```jsx
React.createElement(
  "button",
  { className: "primary" },
  "Save"
);
```

`React.createElement(type, props, ...children)` là API nền tảng tồn tại lâu đời và vẫn hữu ích để hiểu JSX transform, code generated hoặc trường hợp không dùng JSX.

Bạn cũng có thể gặp `React.cloneElement(element, props, ...children)`:

```jsx
const original = <Button size="sm" />;

const enhanced = React.cloneElement(original, {
  disabled: true,
});
```

`cloneElement` tạo element mới dựa trên element cũ và merge props. API vẫn tồn tại nhưng thường làm data flow khó theo dõi hơn composition/context/render prop, nên code mới chỉ dùng khi có lý do rõ.

### `React.createFactory` — legacy trước khi JSX phổ biến

```jsx
const Button = React.createFactory("button");

const element = Button(
  { className: "primary" },
  "Save"
);
```

`createFactory` là helper tạo function chuyên gọi `createElement` cho một type. Khi JSX trở thành chuẩn, API gần như không còn cần; nó bị deprecate ở React 16.13 và bị loại bỏ trong React 19.

### `React.DOM.*`

Trong code React rất cũ còn có thể thấy:

```jsx
React.DOM.div(
  { className: "card" },
  "Hello"
);
```

Hãy hiểu nó như tiền thân của JSX `<div className="card">Hello</div>`, không phải API nên dùng trong code mới.

## 6. Component

Function Component là function JavaScript trả JSX:

```jsx
function Avatar() {
  return <img src="/avatar.png" alt="Ảnh đại diện" />;
}
```

Tên component phải bắt đầu bằng chữ hoa. `<Avatar />` được React hiểu là component, còn `<avatar />` được hiểu như host/custom element.

Không cần tách mỗi `<div>` thành component. Nên tách khi phần UI có responsibility, tên nghiệp vụ, logic riêng hoặc được tái sử dụng.

```jsx
function UserCard({ user }) {
  return (
    <article>
      <Avatar user={user} />
      <UserInfo user={user} />
    </article>
  );
}
```

Render logic phải pure. Không gửi request, mutate global state hoặc điều khiển DOM bên ngoài trong lúc render.

## 6A. Function Component và Class Component qua các thế hệ React

React hiện đại ưu tiên Function Component, nhưng để đọc codebase cũ bạn phải hiểu Class Component vì trước React 16.8 đây là cách chính để component có state và lifecycle.

Function Component hiện đại:

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(c => c + 1)}>
      {count}
    </button>
  );
}
```

Class Component tương đương về mặt ý tưởng:

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
    };
  }

  handleClick = () => {
    this.setState(state => ({
      count: state.count + 1,
    }));
  };

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.count}
      </button>
    );
  }
}
```

Class Component nhận input qua `this.props`, giữ local state trong `this.state` và thay đổi state bằng `this.setState`. `render()` trả về React node giống vai trò return của Function Component. Điểm khác lớn là lifecycle và việc method thường liên quan tới `this`.

### `constructor`, `super(props)` và binding

Trong class đời cũ, constructor thường được dùng để tạo state và bind method:

```jsx
class Form extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      value: "",
    };

    this.handleChange =
      this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({
      value: event.target.value,
    });
  }

  render() {
    return (
      <input
        value={this.state.value}
        onChange={this.handleChange}
      />
    );
  }
}
```

JavaScript class method không tự bind `this`. Vì vậy code React cũ rất hay có `.bind(this)`. Khi class fields trở nên phổ biến, code thường chuyển sang arrow field.

### `setState` của class khác setter của `useState`

Class `this.setState` với object sẽ **shallow merge**:

```jsx
this.state = {
  name: "An",
  age: 20,
};

this.setState({
  age: 21,
});
```

Sau update, `name` vẫn còn. Ngược lại, setter từ `useState` thay thế value được lưu:

```jsx
setUser({
  age: 21,
});
```

Nếu state cũ có `name`, nó sẽ mất. Với Hook phải tự merge khi đó là điều bạn muốn:

```jsx
setUser(user => ({
  ...user,
  age: 21,
}));
```

### `React.PureComponent`

```jsx
class UserCard extends React.PureComponent {
  render() {
    return <div>{this.props.user.name}</div>;
  }
}
```

`PureComponent` shallow-compare props và state để có thể bỏ qua render. Với Function Component, khái niệm gần là `memo`; tuy nhiên React Compiler hiện đại có thể tự động hóa nhiều memoization.

> **Version status:** Class Component vẫn được hỗ trợ để bảo trì code cũ. React hiện tại không khuyến nghị dùng class cho code mới, nhưng class không phải syntax “đã bị remove”.

## 6B. `React.createClass`: component trước ES6 class

Trong React rất cũ, trước khi ES6 class trở thành chuẩn, component có state thường được tạo bằng `React.createClass`:

```jsx
var Counter = React.createClass({
  getInitialState: function () {
    return {
      count: 0,
    };
  },

  handleClick: function () {
    this.setState({
      count: this.state.count + 1,
    });
  },

  render: function () {
    return (
      <button onClick={this.handleClick}>
        {this.state.count}
      </button>
    );
  },
});
```

`getInitialState()` trả state ban đầu. Khác ES6 class, methods của `createClass` được autobind nên thường không cần `.bind(this)`.

`createClass` còn hỗ trợ **mixins**:

```jsx
var TimerMixin = {
  componentDidMount: function () {
    this.timer = setInterval(
      this.tick,
      1000
    );
  },

  componentWillUnmount: function () {
    clearInterval(this.timer);
  },
};

var Clock = React.createClass({
  mixins: [TimerMixin],

  getInitialState: function () {
    return { count: 0 };
  },

  tick: function () {
    this.setState({
      count: this.state.count + 1,
    });
  },

  render: function () {
    return <span>{this.state.count}</span>;
  },
});
```

Mixins cho phép chia sẻ logic nhưng tạo dependency ẩn và conflict tên. HOC, render props và sau này Custom Hooks lần lượt trở thành các cách composition rõ ràng hơn.

Từ React 15.5, `React.createClass` bị deprecate khỏi core và được tách sang package `create-react-class` cho code legacy.

```text
React.createClass + mixins
        ↓
ES6 class + composition/HOC/render props
        ↓
Function Component + Custom Hooks
```

## 7. Props

Props là dữ liệu cha truyền xuống con. Component nhận props phải coi chúng read-only.

```jsx
function Greeting({ name, age }) {
  return <p>Xin chào {name}, {age} tuổi.</p>;
}

function App() {
  return <Greeting name="An" age={25} />;
}
```

Default value:

```jsx
function Button({ type = "button", children }) {
  return <button type={type}>{children}</button>;
}
```

Default chỉ áp dụng khi prop là `undefined`, không phải `null`.

Spread props hữu ích cho wrapper primitive:

```jsx
function Input(props) {
  return <input {...props} />;
}
```

Nhưng component nghiệp vụ nên có API rõ ràng thay vì truyền mọi props không kiểm soát.

### Props legacy: `propTypes` và `defaultProps`

Code React 15–18 thường dùng runtime validation với `prop-types`:

```jsx
import PropTypes from "prop-types";

function UserCard({ name, age }) {
  return <p>{name} - {age}</p>;
}

UserCard.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number,
};

UserCard.defaultProps = {
  age: 0,
};
```

Ở React rất cũ, trước React 15.5, có thể gặp:

```jsx
MyComponent.propTypes = {
  name: React.PropTypes.string,
};
```

React 15.5 deprecate `React.PropTypes` và chuyển validator sang package `prop-types`. React 19 bỏ việc xử lý `propTypes` cho Function Component và bỏ `defaultProps` cho Function Component. Code hiện đại thường dùng TypeScript và default parameter.

Class Component vẫn có thể có `defaultProps`.

## 8. Event

Event handler phải là function:

```jsx
function Button() {
  function handleClick() {
    alert("Đã bấm");
  }

  return <button onClick={handleClick}>Bấm</button>;
}
```

Thông thường sai:

```jsx
<button onClick={handleClick()}>Bấm</button>
```

Đúng nếu cần tham số:

```jsx
<button onClick={() => handleDelete(user.id)}>Xóa</button>
```

Event object:

```jsx
function handleChange(event) {
  console.log(event.target.value);
}
```

Ngăn hành vi mặc định:

```jsx
function handleSubmit(event) {
  event.preventDefault();
}
```

Dừng propagation:

```jsx
event.stopPropagation();
```

Không lạm dụng `stopPropagation`; event flow rõ ràng thường tốt hơn.

### Event cũ: SyntheticEvent pooling và `event.persist()`

Ở React web trước React 17, `SyntheticEvent` từng được pool để tái sử dụng object event. Vì vậy code async đôi khi phải gọi:

```jsx
function handleChange(event) {
  event.persist();

  setTimeout(() => {
    console.log(event.target.value);
  }, 100);
}
```

Từ React 17 trên web, event pooling kiểu này đã bị bỏ nên `event.persist()` không còn cần cho use case đó. Khi thấy `persist()` trong code cũ, đừng copy nó như best practice hiện đại.

Một pattern dễ hiểu ở mọi version là lấy dữ liệu cần dùng ra ngay:

```jsx
function handleChange(event) {
  const value = event.target.value;

  setTimeout(() => {
    console.log(value);
  }, 100);
}
```

## 9. State với `useState`

State là dữ liệu riêng của component có thể thay đổi theo thời gian và ảnh hưởng đến render.

```jsx
const [count, setCount] = useState(0);
```

`useState(initialState)` trả `[state, setter]`. Gọi setter không biến đổi biến state hiện tại ngay lập tức; nó yêu cầu React render với state mới.

### State là snapshot

```jsx
function handleClick() {
  setCount(count + 1);
  console.log(count);
}
```

`console.log` vẫn nhìn thấy snapshot của render hiện tại.

Khi state mới phụ thuộc state trước, dùng updater function:

```jsx
setCount(c => c + 1);
```

Ba update nối tiếp:

```jsx
setCount(c => c + 1);
setCount(c => c + 1);
setCount(c => c + 1);
```

sẽ tăng 3.

### Object state

Sai:

```jsx
user.age = 26;
setUser(user);
```

Đúng:

```jsx
setUser(prev => ({ ...prev, age: 26 }));
```

### Array state

Thêm:

```jsx
setItems(prev => [...prev, newItem]);
```

Xóa:

```jsx
setItems(prev => prev.filter(item => item.id !== id));
```

Sửa:

```jsx
setItems(prev =>
  prev.map(item =>
    item.id === id ? { ...item, done: !item.done } : item
  )
);
```

Lazy initializer:

```jsx
const [items, setItems] = useState(() => createInitialItems());
```

> ### Version Note — Hooks bắt đầu từ React 16.8
>
> `useState` và các Hooks nền tảng xuất hiện từ **React 16.8**. Nếu bạn gặp tutorial React 15/16 đời đầu, state thường nằm trong Class Component và được cập nhật bằng `this.setState`. Không cần học Class Component trước để hiểu React hiện đại; hãy học Function Component + Hooks trước, rồi đọc class ở level Master để bảo trì code legacy.

## 10. Render, re-render và batching

Component render lần đầu khi mount. Sau đó nó có thể render lại khi state thay đổi, parent render, context đọc được thay đổi hoặc các cơ chế liên quan khác kích hoạt update.

Re-render không tự động là performance problem. Đây là cơ chế bình thường. Chỉ tối ưu khi có bằng chứng bottleneck.

React có thể batch nhiều update để giảm commit không cần thiết:

```jsx
function handleClick() {
  setLoading(true);
  setError(null);
  setPage(p => p + 1);
}
```

Không nên giả định mỗi setter tạo một render ngay lập tức.

> ### Version Note — automatic batching từ React 18
>
> Trước React 18, batching mặc định hẹp hơn và thường gắn với React event handler. Từ **React 18 khi dùng `createRoot`**, updates trong Promise, `setTimeout`, native event handler và nhiều nguồn khác cũng được automatic batch. Vì vậy đừng dùng số lần render quan sát được trong tutorial React 17 làm “quy luật” cho React hiện đại. Nếu thật sự cần ép DOM commit đồng bộ, React DOM có `flushSync`, nhưng đây là escape hatch và không phải API nên dùng thường xuyên.

## 11. Conditional rendering

Dùng JavaScript để quyết định UI.

`if`:

```jsx
if (!loggedIn) return <Login />;
return <Dashboard />;
```

Ternary:

```jsx
<p>{online ? "Đang online" : "Offline"}</p>
```

`&&`:

```jsx
{isAdmin && <AdminPanel />}
```

Cẩn thận:

```jsx
{items.length && <List items={items} />}
```

Khi length bằng `0`, React có thể render `0`. Viết rõ:

```jsx
{items.length > 0 && <List items={items} />}
```

Component có thể return `null` nếu không muốn render DOM output.

## 12. List và `key`

```jsx
<ul>
  {users.map(user => (
    <li key={user.id}>{user.name}</li>
  ))}
</ul>
```

`key` giúp React xác định identity của sibling giữa các lần render. Key phải ổn định và unique trong cùng list sibling.

Không dùng `Math.random()` làm key vì identity đổi mỗi render. Index chỉ an toàn khi list thực sự tĩnh, không reorder/insert/delete và row không có state/DOM identity cần giữ.

`key` không được truyền xuống như prop bình thường. Nếu component cần ID, truyền riêng:

```jsx
<Item key={item.id} id={item.id} />
```

## 13. Form cơ bản

Controlled input:

```jsx
const [email, setEmail] = useState("");

<input
  type="email"
  value={email}
  onChange={event => setEmail(event.target.value)}
/>
```

Checkbox dùng `checked`:

```jsx
<input
  type="checkbox"
  checked={agreed}
  onChange={e => setAgreed(e.target.checked)}
/>
```

Select:

```jsx
<select value={country} onChange={e => setCountry(e.target.value)}>
  <option value="kr">Korea</option>
  <option value="vn">Vietnam</option>
</select>
```

Submit:

```jsx
function handleSubmit(event) {
  event.preventDefault();
}

<form onSubmit={handleSubmit}>...</form>
```

Button trong form thường mặc định là submit. Nếu chỉ là action phụ, ghi `type="button"`.

Controlled input dùng React state làm source of truth. Uncontrolled input để DOM giữ value và đọc qua ref/FormData. Cả hai đều hợp lệ; beginner nên nắm controlled trước.

## 14. Lifting state up và single source of truth

Khi hai component cần đồng bộ cùng dữ liệu, đưa state lên ancestor chung gần nhất.

```jsx
function TemperatureInput({ value, onChange }) {
  return <input value={value} onChange={e => onChange(e.target.value)} />;
}

function Calculator() {
  const [temperature, setTemperature] = useState("");

  return (
    <>
      <TemperatureInput value={temperature} onChange={setTemperature} />
      <p>{temperature}</p>
    </>
  );
}
```

Mỗi mẩu state quan trọng nên có một owner rõ ràng.

## 15. Composition và `children`

```jsx
function Card({ children }) {
  return <section className="card">{children}</section>;
}

function App() {
  return (
    <Card>
      <h2>Thông tin</h2>
      <p>Nội dung</p>
    </Card>
  );
}
```

`children` là prop chứa nội dung giữa opening/closing tag. Có thể truyền JSX qua prop tên riêng khi semantic rõ hơn.

React ưu tiên composition hơn inheritance cho UI.

## 16. Styling

React không ép một cách CSS duy nhất.

CSS thường:

```jsx
import "./Button.css";
```

CSS Modules:

```jsx
import styles from "./Button.module.css";
<button className={styles.primary}>Lưu</button>
```

Inline style thích hợp cho giá trị động nhỏ:

```jsx
<div style={{ width: `${progress}%` }} />
```

Ứng dụng lớn có thể dùng utility CSS hoặc component library; đó là ecosystem, không phải React core.

## 17. Strict Mode

`<StrictMode>` bật các kiểm tra development. React có thể chạy lại một số logic để phát hiện render không pure hoặc cleanup sai. Vì vậy beginner có thể thấy log/Effect nhiều hơn mong đợi trong development.

Không tắt Strict Mode chỉ để “hết chạy hai lần”. Hãy sửa purity và cleanup. Production không chạy các development checks theo cùng cách.

> ### Version Note — Strict Mode từ React 18 dễ làm người mới hiểu nhầm
>
> React 18 thêm development-only check mô phỏng việc setup/cleanup rồi setup lại một số Effect khi component mount lần đầu trong Strict Mode. Mục tiêu là phát hiện Effect không cleanup đúng và chuẩn bị code cho kiến trúc có thể preserve/reuse state. Vì vậy khi development thấy Effect hoặc log xuất hiện nhiều lần, đừng vội kết luận React bị lỗi hoặc tắt Strict Mode; trước tiên kiểm tra purity và cleanup. Production không chạy cùng kiểu kiểm tra development này.

## 18. Debug

Phân biệt bốn lớp lỗi: JavaScript runtime, React state/render, DOM/CSS và network/API. Browser DevTools dùng Console, Network, Elements, Performance; React DevTools cho component tree, props/state và profiler.

Khi debug state, log input và transition thay vì chỉ log state ngay sau setter.

## 19. Mini project Todo hoàn chỉnh

```jsx
import { useState } from "react";

let nextId = 1;

export default function TodoApp() {
  const [text, setText] = useState("");
  const [todos, setTodos] = useState([]);

  function handleSubmit(event) {
    event.preventDefault();
    const normalized = text.trim();
    if (!normalized) return;

    setTodos(prev => [
      ...prev,
      { id: nextId++, text: normalized, done: false },
    ]);
    setText("");
  }

  function handleToggle(id) {
    setTodos(prev =>
      prev.map(todo =>
        todo.id === id ? { ...todo, done: !todo.done } : todo
      )
    );
  }

  function handleDelete(id) {
    setTodos(prev => prev.filter(todo => todo.id !== id));
  }

  const completedCount = todos.filter(todo => todo.done).length;

  return (
    <main>
      <h1>Todo</h1>
      <form onSubmit={handleSubmit}>
        <input
          value={text}
          onChange={e => setText(e.target.value)}
          placeholder="Việc cần làm"
        />
        <button type="submit">Thêm</button>
      </form>

      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <label>
              <input
                type="checkbox"
                checked={todo.done}
                onChange={() => handleToggle(todo.id)}
              />
              {todo.text}
            </label>
            <button type="button" onClick={() => handleDelete(todo.id)}>
              Xóa
            </button>
          </li>
        ))}
      </ul>

      <p>Hoàn thành: {completedCount}/{todos.length}</p>
    </main>
  );
}
```

`nextId` ngoài component chỉ phù hợp demo local. Production thường dùng ID server/database hoặc chiến lược định danh phù hợp.

## 20. Các lỗi beginner thường gặp

### Gọi handler trong render

Sai:

```jsx
<button onClick={save()}>Save</button>
```

Đúng:

```jsx
<button onClick={save}>Save</button>
```

### Mutate state

Sai:

```jsx
items.push(newItem);
setItems(items);
```

Đúng:

```jsx
setItems(prev => [...prev, newItem]);
```

### State dư thừa

Không nên lưu `fullName` nếu có thể tính từ `firstName` và `lastName`:

```jsx
const fullName = `${firstName} ${lastName}`.trim();
```

### Định nghĩa component bên trong component

```jsx
function App() {
  function Child() {
    return <div>Child</div>;
  }
  return <Child />;
}
```

Mỗi render có thể tạo component identity mới và gây reset state. Component thường nên được định nghĩa top-level.

### Hiểu sai setter là assignment đồng bộ

`setCount(count + 1)` không làm biến `count` trong closure hiện tại thay đổi ngay.

## 21. Kết thúc level Beginner

Bạn nên tự giải thích được: React khác DOM imperative ở đâu; JSX là gì; component, props và state khác nhau thế nào; vì sao state update phải immutable; vì sao state là snapshot; `key` ảnh hưởng identity thế nào; controlled form hoạt động ra sao; khi nào nên derive giá trị thay vì lưu state.

Bạn cũng nên tự xây được CRUD nhỏ client-side mà không copy architecture, và chỉ ra rõ owner của từng state.

## Version Map cho level Beginner

Ở level Beginner, chỉ cần ghi nhớ bốn mốc để không bị rối khi đọc tài liệu trên Internet. **React 16.8** là lúc Hooks xuất hiện; **React 18** là lúc `createRoot`, automatic batching và concurrent foundations trở thành chuẩn hiện đại; **React 18.3** là bước đệm cảnh báo trước khi nâng lên 19; **React 19.x** mở rộng Actions/server APIs và đơn giản hóa một số syntax như ref-as-prop. Baseline của bộ note là **React 19.3**.

Nếu một đoạn code khác tài liệu này, hãy kiểm tra `package.json` trước khi cho rằng cú pháp nào “đúng” hay “sai”:

```json
{
  "dependencies": {
    "react": "...",
    "react-dom": "..."
  }
}
```

React và React DOM nên được xem như một cặp version tương thích. Với framework như Next.js, còn phải kiểm tra framework đang hỗ trợ/pin React version nào; không tự nâng React độc lập chỉ vì thấy API mới trên react.dev.
