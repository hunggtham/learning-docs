# React Master ghi chú (note / 노트) — Beginner

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **React Master ghi chú (note / 노트) — Beginner**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. React là gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. JavaScript nền tảng cần biết** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> React 19.3 là mốc stable hiện hành để đối chiếu API mới, nhưng tệp (file / 파일) này dạy mô hình tư duy (mental model / 사고 모델) xuyên phiên bản (version / 버전). Mục tiêu là hiểu rendering và trạng thái (state / 상태) trước khi học Hooks như một danh sách API.

## 1. React là gì?

React là thư viện JavaScript dùng để xây dựng giao diện người dùng theo mô hình khai báo và thành phần (component / 컴포넌트). Điểm quan trọng nhất của React không phải JSX hay Hook, mà là tư duy “dữ liệu hiện tại quyết định giao diện hiện tại”. Thay vì trực tiếp tìm DOM nút (node / 노드) rồi ra lệnh sửa từng phần tử khi dữ liệu thay đổi, bạn mô tả UI cần trông như thế nào đối với props và trạng thái (state / 상태) hiện tại. React chạy lại lô-gic (logic / 논리) kết xuất (render / 렌더링), so sánh kết quả mới với cây hiện tại và lần ghi nhận (commit / 커밋) những thay đổi cần thiết xuống DOM.

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

React cho phép mô tả UI từ trạng thái (state / 상태):

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

React là thư viện UI chứ không phải một full-stack khung phần mềm (framework / 프레임워크). Routing, dữ liệu (data / 데이터) bộ nhớ đệm (cache / 캐시), authentication, máy chủ (server / 서버) thời gian chạy (runtime / 런타임), cơ sở dữ liệu (database / 데이터베이스) và triển khai (deployment / 배포) thường đến từ thư viện hoặc khung phần mềm (framework / 프레임워크) khác. Vì vậy cần phân biệt React cốt lõi (core / 핵심) với ecosystem.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — nên học phiên bản (version / 버전) nào trước?
>
> Nếu bắt đầu mới, hãy học theo cú pháp và mô hình tư duy (mental model / 사고 모델) React 19.3 trong tài liệu này. Phần lớn kiến thức nền như thành phần (component / 컴포넌트), props, trạng thái (state / 상태), sự kiện (event / 이벤트), danh sách (list / 목록) và form vẫn áp dụng cho React 18 và cả nhiều mã (code / 코드) React 16.8/17. Sự khác nhau lớn nhất khi đọc mã (code / 코드) cũ thường nằm ở entry API, lớp (class / 클래스) thành phần (component / 컴포넌트), JSX transform và một số API mới của React 19; vì vậy không cần học từng phiên bản (version / 버전) theo thứ tự lịch sử trước khi học React.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **2. JavaScript nền tảng cần biết** tiếp nhận điểm tựa từ **1. React là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. React app hoạt động như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. JavaScript nền tảng cần biết

React sử dụng JavaScript thật. Nếu không hiểu JavaScript, người học rất dễ thuộc cú pháp React nhưng không biết vì sao mã (code / 코드) chạy hoặc hỏng.

`const` nên là lựa chọn mặc định cho binding không cần gán lại; `let` dùng khi biến thực sự phải đổi trong cùng thực thi (execution / 실행) phạm vi (scope / 범위). `const` không làm đối tượng (object / 객체) bất biến:

```js
const user = { name: "An" };
user.name = "Bình"; // hợp lệ
```

Hàm (function / 함수) và arrow hàm (function / 함수) xuất hiện liên tục:

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

Spread cú pháp (syntax / 문법) rất quan trọng vì trạng thái (state / 상태) React thường được cập nhật theo kiểu tạo đối tượng (object / 객체)/array mới:

```js
const nextUser = { ...user, name: "Bình" };
const nextItems = [...items, newItem];
```

Các array phương thức (method / 메서드) phải quen gồm `map`, `filter`, `find`, `some`, `every`, `reduce`. Trong React, `map` dùng rất nhiều để kết xuất (render / 렌더링) danh sách (list / 목록).

Mô-đun (module / 모듈) ES:

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

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **3. React app hoạt động như thế nào?** tiếp nhận điểm tựa từ **2. JavaScript nền tảng cần biết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3A. mô hình tư duy (mental model / 사고 모델) cốt lõi trước Hooks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. React app hoạt động như thế nào?

Ứng dụng web React thường dùng `react` cho mô hình (model / 모델) thành phần (component / 컴포넌트)/Hooks và `react-dom` để kết nối với DOM.

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

Có thể hiểu một cập nhật (update / 업데이트) qua ba bước lớn: một sự kiện (event / 이벤트) hoặc nguồn dữ liệu làm props/trạng thái (state / 상태) thay đổi; React kết xuất (render / 렌더링) để tính cây UI mới; React lần ghi nhận (commit / 커밋) thay đổi cần thiết xuống DOM. trình duyệt (browser / 브라우저) sau đó bố cục (layout / 레이아웃) và paint. “thành phần (component / 컴포넌트) kết xuất (render / 렌더링) lại” không đồng nghĩa toàn bộ DOM bị dựng lại.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — `createRoot`
>
> `createRoot` là API máy khách (client / 클라이언트) gốc (root / 루트) hiện đại từ **React 18**. Tutorial React 17 trở xuống thường dùng `ReactDOM.render(<App />, container)`. React 18 đã deprecate cách cũ và nếu vẫn dùng nó, app không nhận đầy đủ hành vi (behavior / 동작) mới của gốc (root / 루트) React 18; tới React 19, API kết xuất (render / 렌더링)/hydrate legacy đã bị loại bỏ. Vì vậy mã (code / 코드) mới nên luôn nghĩ theo `createRoot` hoặc `hydrateRoot` nếu đang hydrate HTML từ máy chủ (server / 서버).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **3A. mô hình tư duy (mental model / 사고 모델) cốt lõi trước Hooks** gom các mảnh từ **3. React app hoạt động như thế nào?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **3B. kết xuất (render / 렌더링) cây (tree / 트리), thành phần (component / 컴포넌트) lời gọi (call / 호출) và DOM cập nhật (update / 업데이트) là ba chuyện khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3A. mô hình tư duy (mental model / 사고 모델) cốt lõi trước Hooks

Có thể tạm nghĩ `UI = render(props, state, context)`. kết xuất (render / 렌더링) đọc snapshot hiện tại và mô tả UI; sự kiện (event / 이벤트) handler hoặc tác động (effect / 효과) mới là nơi yêu cầu trạng thái (state / 상태) mới hay đồng bộ hệ thống ngoài React.

Một cập nhật (update / 업데이트) đi qua `trigger → render → reconciliation → commit → browser layout/paint`. kết xuất (render / 렌더링) tạo cây (tree / 트리) mới. Reconciliation dùng kiểu (type / 타입), vị trí và `key` để quyết định định danh (identity / 식별자) nào được giữ hay thay. lần ghi nhận (commit / 커밋) mới áp host mutation xuống DOM, refs và tác động (effect / 효과). Vì vậy thành phần (component / 컴포넌트) kết xuất (render / 렌더링) lại không đồng nghĩa DOM bị tạo lại.

Trạng thái (state / 상태) cũng không nằm trong biến cục bộ (local / 로컬). `count` từ `useState` là snapshot của kết xuất (render / 렌더링) hiện tại; React giữ trạng thái (state / 상태) gắn với định danh (identity / 식별자) trong cây (tree / 트리). Setter hàng đợi (queue / 큐) cập nhật (update / 업데이트) chứ không mutate biến JavaScript. lớp (class / 클래스) `this.state`/`this.setState` và Hooks khác API nhưng cùng bất biến (invariant / 불변식) này. mô hình tư duy (mental model / 사고 모델) này giải thích immutable cập nhật (update / 업데이트), stale closure, preserve/reset trạng thái (state / 상태), batching và `key`.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **3B. kết xuất (render / 렌더링) cây (tree / 트리), thành phần (component / 컴포넌트) lời gọi (call / 호출) và DOM cập nhật (update / 업데이트) là ba chuyện khác nhau** gom các mảnh từ **3A. mô hình tư duy (mental model / 사고 모델) cốt lõi trước Hooks** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **4. Tạo dự án (project / 프로젝트) React hiện đại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3B. kết xuất (render / 렌더링) cây (tree / 트리), thành phần (component / 컴포넌트) lời gọi (call / 호출) và DOM cập nhật (update / 업데이트) là ba chuyện khác nhau

Khi React kết xuất (render / 렌더링) một thành phần (component / 컴포넌트), React đang gọi thành phần (component / 컴포넌트) để lấy mô tả UI cho snapshot props/trạng thái (state / 상태) hiện tại. Kết quả này tạo **kết xuất (render / 렌더링) cây (tree / 트리)** gồm React elements và thành phần (component / 컴포넌트) boundaries; nó chưa đồng nghĩa trình duyệt (browser / 브라우저) DOM đã đổi. Parent kết xuất (render / 렌더링) thường khiến React đi xuống kết xuất (render / 렌더링) children để tính cây (tree / 트리) mới, nhưng sau reconciliation React chỉ lần ghi nhận (commit / 커밋) host changes thực sự cần thiết. Vì vậy `console.log` trong thành phần (component / 컴포넌트) có thể chạy dù DOM cuối cùng không đổi.

Điều này dẫn đến ba câu hỏi khác nhau khi gỡ lỗi (debug / 디버그): **vì sao thành phần (component / 컴포넌트) được kết xuất (render / 렌더링)?**, **kết quả kết xuất (render / 렌더링) mới khác cây (tree / 트리) cũ ở đâu?**, và **lần ghi nhận (commit / 커밋) có thay DOM hay chạy tác động (effect / 효과)/ref nào không?**. Gộp ba câu hỏi thành “React kết xuất (render / 렌더링) lại quá nhiều” thường dẫn tới tối ưu sai chỗ.

Kết xuất (render / 렌더링) cũng không phải vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트) để làm side tác động (effect / 효과). React hiện đại có thể gọi kết xuất (render / 렌더링) nhiều lần để kiểm tra purity, hoặc chuẩn bị công việc (work / 작업) rồi bỏ kết quả trước lần ghi nhận (commit / 커밋). mã (code / 코드) trong kết xuất (render / 렌더링) vì vậy phải có tính chất tính toán: cùng đầu vào (input / 입력) phải cho đầu ra (output / 출력) tương thích và không để lại mutation bên ngoài.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **4. Tạo dự án (project / 프로젝트) React hiện đại** tiếp nhận điểm tựa từ **3B. kết xuất (render / 렌더링) cây (tree / 트리), thành phần (component / 컴포넌트) lời gọi (call / 호출) và DOM cập nhật (update / 업데이트) là ba chuyện khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. JSX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Tạo dự án (project / 프로젝트) React hiện đại

Create React App không còn là lựa chọn khuyến nghị cho dự án (project / 프로젝트) mới. Với học React cốt lõi (core / 핵심) hoặc SPA client-side, Vite là lựa chọn phổ biến:

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

> ### phiên bản (version / 버전) ghi chú (note / 노트) — Create React App không phải “React cũ”
>
> Create React App là toolchain, không phải React cốt lõi (core / 핵심). React nhóm (team / 팀) đã deprecate Create React App cho dự án (project / 프로젝트) mới vào năm 2025 và khuyến nghị khung phần mềm (framework / 프레임워크) hoặc bản dựng (build / 빌드) công cụ (tool / 도구) hiện đại như Vite/Parcel/RSBuild tùy nhu cầu. Một codebase CRA vẫn có thể chạy React 18 hoặc 19, nên hãy tách hai khái niệm: “phiên bản (version / 버전) React” và “công cụ tạo/bản dựng (build / 빌드) dự án (project / 프로젝트)”.

### Gốc (root / 루트) API cũ: `ReactDOM.render`, `hydrate`, `unmountComponentAtNode`

React 17 trở xuống thường khởi động app bằng:

```jsx
import ReactDOM from "react-dom";

ReactDOM.render(
  <App />,
  document.getElementById("root")
);
```

React 18 giới thiệu gốc (root / 루트) API mới:

```jsx
import { createRoot } from "react-dom/client";

const root = createRoot(
  document.getElementById("root")
);

root.render(<App />);
```

`ReactDOM.render` bị deprecate từ React 18 và bị remove ở React 19. Nếu dùng API cũ trong React 18, app chạy theo tính tương thích (compatibility / 호환성) hành vi (behavior / 동작) gần React 17 và không có đầy đủ hiện đại (modern / 현대적) gốc (root / 루트) ngữ nghĩa (semantics / 의미론).

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

Ba API legacy trên rất thường gặp trong dự án (project / 프로젝트) React 16/17 và tài liệu cũ, nên cần đọc được dù không dùng cho mã (code / 코드) mới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **5. JSX** tiếp nhận điểm tựa từ **4. Tạo dự án (project / 프로젝트) React hiện đại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5A. JSX thực chất tạo React element: createElement, cloneElement và API cũ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. JSX

JSX là cú pháp mở rộng của JavaScript cho phép viết cấu trúc gần giống HTML. trình duyệt (browser / 브라우저) không hiểu JSX trực tiếp; bản dựng (build / 빌드) công cụ (tool / 도구) chuyển JSX thành mã JavaScript/thời gian chạy (runtime / 런타임) React.

```jsx
const element = <h1>Xin chào React</h1>;
```

JSX phải có một gốc (root / 루트) hợp lệ. Nếu không muốn thêm DOM wrapper, dùng Fragment:

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

Sự kiện (event / 이벤트) dùng camelCase như `onClick`, `onChange`, `onSubmit`.

Boolean prop:

```jsx
<input disabled />
```

Inline style nhận đối tượng (object / 객체) JavaScript và thuộc tính (property / 속성) camelCase:

```jsx
<div style={{ backgroundColor: "black", fontSize: 18 }} />
```

React escape giá trị văn bản (text / 텍스트) mặc định, giúp giảm nhiều XSS trường hợp (case / 사례):

```jsx
<p>{userInput}</p>
```

`dangerouslySetInnerHTML` bỏ lớp bảo vệ đó cho HTML raw và chỉ nên dùng với dữ liệu đã sanitize/trusted:

```jsx
<div dangerouslySetInnerHTML={{ __html: trustedHtml }} />
```

> ### phiên bản (version / 버전) ghi chú (note / 노트) — JSX transform
>
> Tutorial rất cũ thường bắt đầu tệp (file / 파일) bằng `import React from "react";` dù biến `React` không được dùng trực tiếp. Lý do là JSX transform cũ biên dịch JSX thành lời gọi như `React.createElement(...)`. hiện đại (modern / 현대적) JSX transform, được phổ biến từ giai đoạn React 17 và đã được backport cho một số phiên bản (version / 버전) cũ hơn, cho phép JSX hoạt động mà không cần import React chỉ vì JSX. **React 19 yêu cầu hiện đại (modern / 현대적) JSX transform**, nên mã (code / 코드) mới không nên học thói quen import React chỉ để “JSX chạy”.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **5A. JSX thực chất tạo React element: createElement, cloneElement và API cũ** tiếp nhận điểm tựa từ **5. JSX** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. thành phần (component / 컴포넌트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5A. JSX thực chất tạo React element: `createElement`, `cloneElement` và API cũ

JSX không phải yêu cầu (requirement / 요구사항) bắt buộc. JSX:

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

`React.createElement(type, props, ...children)` là API nền tảng tồn tại lâu đời và vẫn hữu ích để hiểu JSX transform, mã (code / 코드) generated hoặc trường hợp không dùng JSX.

Bạn cũng có thể gặp `React.cloneElement(element, props, ...children)`:

```jsx
const original = <Button size="sm" />;

const enhanced = React.cloneElement(original, {
  disabled: true,
});
```

`cloneElement` tạo element mới dựa trên element cũ và merge props. API vẫn tồn tại nhưng thường làm luồng dữ liệu (data flow / 데이터 흐름) khó theo dõi hơn composition/ngữ cảnh (context / 맥락)/kết xuất (render / 렌더링) prop, nên mã (code / 코드) mới chỉ dùng khi có lý do rõ.

### `React.createFactory` — legacy trước khi JSX phổ biến
Phần này nối mạch bài học với “`React.createFactory` — legacy trước khi JSX phổ biến”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
const Button = React.createFactory("button");

const element = Button(
  { className: "primary" },
  "Save"
);
```

`createFactory` là helper tạo hàm (function / 함수) chuyên gọi `createElement` cho một kiểu (type / 타입). Khi JSX trở thành chuẩn, API gần như không còn cần; nó bị deprecate ở React 16.13 và bị loại bỏ trong React 19.

### `React.DOM.*`

Trong mã (code / 코드) React rất cũ còn có thể thấy:

```jsx
React.DOM.div(
  { className: "card" },
  "Hello"
);
```

Hãy hiểu nó như tiền thân của JSX `<div className="card">Hello</div>`, không phải API nên dùng trong mã (code / 코드) mới.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **6. thành phần (component / 컴포넌트)** tiếp nhận điểm tựa từ **5A. JSX thực chất tạo React element: createElement, cloneElement và API cũ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6A. hàm (function / 함수) thành phần (component / 컴포넌트) và lớp (class / 클래스) thành phần (component / 컴포넌트) qua các thế hệ React** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. thành phần (component / 컴포넌트)

Hàm (function / 함수) thành phần (component / 컴포넌트) là hàm (function / 함수) JavaScript trả JSX:

```jsx
function Avatar() {
  return <img src="/avatar.png" alt="Ảnh đại diện" />;
}
```

Tên thành phần (component / 컴포넌트) phải bắt đầu bằng chữ hoa. `<Avatar />` được React hiểu là thành phần (component / 컴포넌트), còn `<avatar />` được hiểu như host/custom element.

Không cần tách mỗi `<div>` thành thành phần (component / 컴포넌트). Nên tách khi phần UI có responsibility, tên nghiệp vụ, lô-gic (logic / 논리) riêng hoặc được tái sử dụng.

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

Kết xuất (render / 렌더링) lô-gic (logic / 논리) phải pure. Không gửi yêu cầu (request / 요청), mutate toàn cục (global / 전역) trạng thái (state / 상태) hoặc điều khiển DOM bên ngoài trong lúc kết xuất (render / 렌더링).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **6A. hàm (function / 함수) thành phần (component / 컴포넌트) và lớp (class / 클래스) thành phần (component / 컴포넌트) qua các thế hệ React** tiếp nhận điểm tựa từ **6. thành phần (component / 컴포넌트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6B. React.createClass: thành phần (component / 컴포넌트) trước ES6 lớp (class / 클래스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6A. hàm (function / 함수) thành phần (component / 컴포넌트) và lớp (class / 클래스) thành phần (component / 컴포넌트) qua các thế hệ React

React hiện đại ưu tiên hàm (function / 함수) thành phần (component / 컴포넌트), nhưng để đọc codebase cũ bạn phải hiểu lớp (class / 클래스) thành phần (component / 컴포넌트) vì trước React 16.8 đây là cách chính để thành phần (component / 컴포넌트) có trạng thái (state / 상태) và vòng đời (lifecycle / 생명주기).

Hàm (function / 함수) thành phần (component / 컴포넌트) hiện đại:

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

Lớp (class / 클래스) thành phần (component / 컴포넌트) tương đương về mặt ý tưởng:

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

Lớp (class / 클래스) thành phần (component / 컴포넌트) nhận đầu vào (input / 입력) qua `this.props`, giữ cục bộ (local / 로컬) trạng thái (state / 상태) trong `this.state` và thay đổi trạng thái (state / 상태) bằng `this.setState`. `render()` trả về React nút (node / 노드) giống vai trò return của hàm (function / 함수) thành phần (component / 컴포넌트). Điểm khác lớn là vòng đời (lifecycle / 생명주기) và việc phương thức (method / 메서드) thường liên quan tới `this`.

### `constructor`, `super(props)` và binding

Trong lớp (class / 클래스) đời cũ, constructor thường được dùng để tạo trạng thái (state / 상태) và bind phương thức (method / 메서드):

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

JavaScript lớp (class / 클래스) phương thức (method / 메서드) không tự bind `this`. Vì vậy mã (code / 코드) React cũ rất hay có `.bind(this)`. Khi lớp (class / 클래스) fields trở nên phổ biến, mã (code / 코드) thường chuyển sang arrow trường dữ liệu (field / 필드).

### `setState` của lớp (class / 클래스) khác setter của `useState`

Lớp (class / 클래스) `this.setState` với đối tượng (object / 객체) sẽ **shallow merge**:

```jsx
this.state = {
  name: "An",
  age: 20,
};

this.setState({
  age: 21,
});
```

Sau cập nhật (update / 업데이트), `name` vẫn còn. Ngược lại, setter từ `useState` thay thế giá trị (value / 값) được lưu:

```jsx
setUser({
  age: 21,
});
```

Nếu trạng thái (state / 상태) cũ có `name`, nó sẽ mất. Với Hook phải tự merge khi đó là điều bạn muốn:

```jsx
setUser(user => ({
  ...user,
  age: 21,
}));
```

### `React.PureComponent`
Phần này nối mạch bài học với “`React.PureComponent`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
class UserCard extends React.PureComponent {
  render() {
    return <div>{this.props.user.name}</div>;
  }
}
```

`PureComponent` shallow-compare props và trạng thái (state / 상태) để có thể bỏ qua kết xuất (render / 렌더링). Với hàm (function / 함수) thành phần (component / 컴포넌트), khái niệm gần là `memo`; tuy nhiên React trình biên dịch (compiler / 컴파일러) hiện đại có thể tự động hóa nhiều memoization.

> **phiên bản (version / 버전) status:** lớp (class / 클래스) thành phần (component / 컴포넌트) vẫn được hỗ trợ để bảo trì mã (code / 코드) cũ. React hiện tại không khuyến nghị dùng lớp (class / 클래스) cho mã (code / 코드) mới, nhưng lớp (class / 클래스) không phải cú pháp (syntax / 문법) “đã bị remove”.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **6B. React.createClass: thành phần (component / 컴포넌트) trước ES6 lớp (class / 클래스)** tiếp nhận điểm tựa từ **6A. hàm (function / 함수) thành phần (component / 컴포넌트) và lớp (class / 클래스) thành phần (component / 컴포넌트) qua các thế hệ React** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Props** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6B. `React.createClass`: thành phần (component / 컴포넌트) trước ES6 lớp (class / 클래스)

Trong React rất cũ, trước khi ES6 lớp (class / 클래스) trở thành chuẩn, thành phần (component / 컴포넌트) có trạng thái (state / 상태) thường được tạo bằng `React.createClass`:

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

`getInitialState()` trả trạng thái (state / 상태) ban đầu. Khác ES6 lớp (class / 클래스), methods của `createClass` được autobind nên thường không cần `.bind(this)`.

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

Mixins cho phép chia sẻ lô-gic (logic / 논리) nhưng tạo phụ thuộc (dependency / 의존성) ẩn và xung đột (conflict / 충돌) tên. HOC, kết xuất (render / 렌더링) props và sau này Custom Hooks lần lượt trở thành các cách composition rõ ràng hơn.

Từ React 15.5, `React.createClass` bị deprecate khỏi cốt lõi (core / 핵심) và được tách sang gói (package / 패키지) `create-react-class` cho mã (code / 코드) legacy.

```text
React.createClass + mixins
        ↓
ES6 class + composition/HOC/render props
        ↓
Function Component + Custom Hooks
```

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **7. Props** tiếp nhận điểm tựa từ **6B. React.createClass: thành phần (component / 컴포넌트) trước ES6 lớp (class / 클래스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. sự kiện (event / 이벤트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Props

Props là dữ liệu cha truyền xuống con. thành phần (component / 컴포넌트) nhận props phải coi chúng read-only.

```jsx
function Greeting({ name, age }) {
  return <p>Xin chào {name}, {age} tuổi.</p>;
}

function App() {
  return <Greeting name="An" age={25} />;
}
```

Default giá trị (value / 값):

```jsx
function Button({ type = "button", children }) {
  return <button type={type}>{children}</button>;
}
```

Default chỉ áp dụng khi prop là `undefined`, không phải `null`.

Spread props hữu ích cho wrapper thành phần nguyên thủy (primitive / 기본 요소):

```jsx
function Input(props) {
  return <input {...props} />;
}
```

Nhưng thành phần (component / 컴포넌트) nghiệp vụ nên có API rõ ràng thay vì truyền mọi props không kiểm soát.

### Props legacy: `propTypes` và `defaultProps`

Mã (code / 코드) React 15–18 thường dùng thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증) với `prop-types`:

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

React 15.5 deprecate `React.PropTypes` và chuyển validator sang gói (package / 패키지) `prop-types`. React 19 bỏ việc xử lý `propTypes` cho hàm (function / 함수) thành phần (component / 컴포넌트) và bỏ `defaultProps` cho hàm (function / 함수) thành phần (component / 컴포넌트). mã (code / 코드) hiện đại thường dùng TypeScript và default parameter.

Lớp (class / 클래스) thành phần (component / 컴포넌트) vẫn có thể có `defaultProps`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **8. sự kiện (event / 이벤트)** tiếp nhận điểm tựa từ **7. Props** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. trạng thái (state / 상태) với useState** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. sự kiện (event / 이벤트)

Sự kiện (event / 이벤트) handler phải là hàm (function / 함수):

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

Sự kiện (event / 이벤트) đối tượng (object / 객체):

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

Không lạm dụng `stopPropagation`; sự kiện (event / 이벤트) luồng (flow / 흐름) rõ ràng thường tốt hơn.

### Sự kiện (event / 이벤트) cũ: SyntheticEvent pooling và `event.persist()`

Ở React web trước React 17, `SyntheticEvent` từng được pool để tái sử dụng đối tượng (object / 객체) sự kiện (event / 이벤트). Vì vậy mã (code / 코드) async đôi khi phải gọi:

```jsx
function handleChange(event) {
  event.persist();

  setTimeout(() => {
    console.log(event.target.value);
  }, 100);
}
```

Từ React 17 trên web, sự kiện (event / 이벤트) pooling kiểu này đã bị bỏ nên `event.persist()` không còn cần cho use trường hợp (case / 사례) đó. Khi thấy `persist()` trong mã (code / 코드) cũ, đừng bản sao (copy / 복사) nó như best practice hiện đại.

Một mẫu (pattern / 패턴) dễ hiểu ở mọi phiên bản (version / 버전) là lấy dữ liệu cần dùng ra ngay:

```jsx
function handleChange(event) {
  const value = event.target.value;

  setTimeout(() => {
    console.log(value);
  }, 100);
}
```

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **9. trạng thái (state / 상태) với useState** tiếp nhận điểm tựa từ **8. sự kiện (event / 이벤트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9A. cập nhật (update / 업데이트) hàng đợi (queue / 큐) và updater hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. trạng thái (state / 상태) với `useState`

Trạng thái (state / 상태) là dữ liệu riêng của thành phần (component / 컴포넌트) có thể thay đổi theo thời gian và ảnh hưởng đến kết xuất (render / 렌더링).

```jsx
const [count, setCount] = useState(0);
```

`useState(initialState)` trả `[state, setter]`. Gọi setter không biến đổi biến trạng thái (state / 상태) hiện tại ngay lập tức; nó yêu cầu React kết xuất (render / 렌더링) với trạng thái (state / 상태) mới.

### State là snapshot
Phần này nối mạch bài học với “State là snapshot”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
function handleClick() {
  setCount(count + 1);
  console.log(count);
}
```

`console.log` vẫn nhìn thấy snapshot của kết xuất (render / 렌더링) hiện tại.

Khi trạng thái (state / 상태) mới phụ thuộc trạng thái (state / 상태) trước, dùng updater hàm (function / 함수):

```jsx
setCount(c => c + 1);
```

Ba cập nhật (update / 업데이트) nối tiếp:

```jsx
setCount(c => c + 1);
setCount(c => c + 1);
setCount(c => c + 1);
```

sẽ tăng 3.

### Đối tượng (object / 객체) trạng thái (state / 상태)

Sai:

```jsx
user.age = 26;
setUser(user);
```

Đúng:

```jsx
setUser(prev => ({ ...prev, age: 26 }));
```

### Array trạng thái (state / 상태)

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

> ### phiên bản (version / 버전) ghi chú (note / 노트) — Hooks bắt đầu từ React 16.8
>
> `useState` và các Hooks nền tảng xuất hiện từ **React 16.8**. Nếu bạn gặp tutorial React 15/16 đời đầu, trạng thái (state / 상태) thường nằm trong lớp (class / 클래스) thành phần (component / 컴포넌트) và được cập nhật bằng `this.setState`. Không cần học lớp (class / 클래스) thành phần (component / 컴포넌트) trước để hiểu React hiện đại; hãy học hàm (function / 함수) thành phần (component / 컴포넌트) + Hooks trước, rồi đọc lớp (class / 클래스) ở mức (level / 수준) Master để bảo trì mã (code / 코드) legacy.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **9A. cập nhật (update / 업데이트) hàng đợi (queue / 큐) và updater hàm (function / 함수)** tiếp nhận điểm tựa từ **9. trạng thái (state / 상태) với useState** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9B. quyền sở hữu trạng thái (state ownership / 상태 소유권), minimal trạng thái (state / 상태) và nguồn chuẩn (source of truth / 정본)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9A. cập nhật (update / 업데이트) hàng đợi (queue / 큐) và updater hàm (function / 함수)

Setter thêm cập nhật (update / 업데이트) vào hàng đợi. Nhiều `setCount(count + 1)` trong cùng handler đều đọc cùng snapshot; `setCount(c => c + 1)` nhận kết quả queued trước nên đúng khi trạng thái (state / 상태) mới phụ thuộc trạng thái (state / 상태) cũ. lớp (class / 클래스) `setState(state => ...)` có cùng mục đích, nhưng đối tượng (object / 객체) `setState` của lớp (class / 클래스) shallow-merge còn Hook setter replace giá trị (value / 값). React 18 với hiện đại (modern / 현대적) gốc (root / 루트) mở rộng automatic batching sang nhiều async sources; tính đúng đắn (correctness / 정확성) không nên dựa vào giả định mỗi setter kết xuất (render / 렌더링) ngay một lần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **9A. cập nhật (update / 업데이트) hàng đợi (queue / 큐) và updater hàm (function / 함수)** nêu điều cần giải thích; **9B. quyền sở hữu trạng thái (state ownership / 상태 소유권), minimal trạng thái (state / 상태) và nguồn chuẩn (source of truth / 정본)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. kết xuất (render / 렌더링), re-render và batching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9B. quyền sở hữu trạng thái (state ownership / 상태 소유권), minimal trạng thái (state / 상태) và nguồn chuẩn (source of truth / 정본)

Một trạng thái (state / 상태) tốt phải có **đơn vị sở hữu (owner / 오너)** rõ: thành phần (component / 컴포넌트) nào chịu trách nhiệm thay đổi nó và subtree nào cần đọc nó. Nếu hai sibling cần cùng một giá trị, thường nâng trạng thái (state / 상태) lên nearest dùng chung (common / 공통) đơn vị sở hữu (owner / 오너) thay vì tạo hai bản sao rồi dùng tác động (effect / 효과) để đồng bộ. Nếu giá trị có thể tính từ props/trạng thái (state / 상태) hiện có, hãy derive trong kết xuất (render / 렌더링) thay vì lưu thêm một nguồn chuẩn (source of truth / 정본).

Ví dụ không nên lưu cả `items` lẫn `visibleItems` nếu `visibleItems` chỉ là `items.filter(...)`. Duplicate trạng thái (state / 상태) tạo bài toán đồng bộ, còn derived giá trị (value / 값) tự cập nhật theo kết xuất (render / 렌더링). Tương tự, trạng thái (state / 상태) nên mô tả dữ liệu nghiệp vụ tối thiểu chứ không mô tả mọi biến trung gian của UI.

Trạng thái (state / 상태) cập nhật (update / 업데이트) phải được hiểu theo snapshot. sự kiện (event / 이벤트) handler của một kết xuất (render / 렌더링) nhìn thấy snapshot của kết xuất (render / 렌더링) đó; setter hàng đợi (queue / 큐) trạng thái (state / 상태) cho kết xuất (render / 렌더링) tiếp theo. Khi trạng thái (state / 상태) mới phụ thuộc trạng thái (state / 상태) cũ, updater hàm (function / 함수) như `setCount(c => c + 1)` mô tả chuyển tiếp (transition / 전이) chính xác hơn việc đọc snapshot cũ nhiều lần. Đây là bất biến (invariant / 불변식) chung dù cú pháp (syntax / 문법) là lớp (class / 클래스) `setState` hay Hook setter.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **9B. quyền sở hữu trạng thái (state ownership / 상태 소유권), minimal trạng thái (state / 상태) và nguồn chuẩn (source of truth / 정본)** nêu điều cần giải thích; **10. kết xuất (render / 렌더링), re-render và batching** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10A. Reconciliation, định danh (identity / 식별자) và preserve/reset trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. kết xuất (render / 렌더링), re-render và batching

Thành phần (component / 컴포넌트) kết xuất (render / 렌더링) lần đầu khi mount. Sau đó nó có thể kết xuất (render / 렌더링) lại khi trạng thái (state / 상태) thay đổi, parent kết xuất (render / 렌더링), ngữ cảnh (context / 맥락) đọc được thay đổi hoặc các cơ chế liên quan khác kích hoạt cập nhật (update / 업데이트).

Re-render không tự động là hiệu năng (performance / 성능) bài toán (problem / 문제). Đây là cơ chế bình thường. Chỉ tối ưu khi có bằng chứng bottleneck.

React có thể batch nhiều cập nhật (update / 업데이트) để giảm lần ghi nhận (commit / 커밋) không cần thiết:

```jsx
function handleClick() {
  setLoading(true);
  setError(null);
  setPage(p => p + 1);
}
```

Không nên giả định mỗi setter tạo một kết xuất (render / 렌더링) ngay lập tức.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — automatic batching từ React 18
>
> Trước React 18, batching mặc định hẹp hơn và thường gắn với React sự kiện (event / 이벤트) handler. Từ **React 18 khi dùng `createRoot`**, updates trong Promise, `setTimeout`, bản địa (native / 네이티브) sự kiện (event / 이벤트) handler và nhiều nguồn khác cũng được automatic batch. Vì vậy đừng dùng số lần kết xuất (render / 렌더링) quan sát được trong tutorial React 17 làm “quy luật” cho React hiện đại. Nếu thật sự cần ép DOM lần ghi nhận (commit / 커밋) đồng bộ, React DOM có `flushSync`, nhưng đây là escape hatch và không phải API nên dùng thường xuyên.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **10A. Reconciliation, định danh (identity / 식별자) và preserve/reset trạng thái (state / 상태)** tiếp nhận điểm tựa từ **10. kết xuất (render / 렌더링), re-render và batching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10B. Reconciliation bằng ví dụ: kiểu (type / 타입), position và key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10A. Reconciliation, định danh (identity / 식별자) và preserve/reset trạng thái (state / 상태)

Reconciliation so cây (tree / 트리) mới với cây (tree / 트리) trước. mô hình tư duy (mental model / 사고 모델) dành cho ứng dụng (application / 애플리케이션) mã (code / 코드) là **kiểu (type / 타입) + position + key**. Cùng kiểu (type / 타입) ở cùng vị trí thường giữ cục bộ (local / 로컬) trạng thái (state / 상태) khi props đổi; đổi kiểu (type / 타입) thường thay subtree và reset trạng thái (state / 상태). `key` thêm định danh (identity / 식별자) nghiệp vụ ngoài vị trí, nên `<Editor key={document.id} />` có thể chủ động reset draft khi đổi document mà không cần tác động (effect / 효과) chỉ để `setDraft('')`.

React 16 đưa Fiber để kết xuất (render / 렌더링) công việc (work / 작업) có thể được chia và schedule linh hoạt hơn; ứng dụng (application / 애플리케이션) mã (code / 코드) không truy cập Fiber internals. bất biến (invariant / 불변식) xuyên React cũ và mới vẫn là kết xuất (render / 렌더링) purity và định danh (identity / 식별자) qua kiểu (type / 타입)/position/key.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **10A. Reconciliation, định danh (identity / 식별자) và preserve/reset trạng thái (state / 상태)** cho ta quy tắc; **10B. Reconciliation bằng ví dụ: kiểu (type / 타입), position và key** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **11. Conditional rendering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10B. Reconciliation bằng ví dụ: kiểu (type / 타입), position và key

Reconciliation không phải “deep compare toàn bộ DOM”. Ở mức mô hình tư duy (mental model / 사고 모델), React dùng cấu trúc cây (tree / 트리) để quyết định định danh (identity / 식별자). Nếu cùng thành phần (component / 컴포넌트) kiểu (type / 타입) tiếp tục xuất hiện ở cùng vị trí lô-gic (logic / 논리), React thường preserve cục bộ (local / 로컬) trạng thái (state / 상태). Nếu kiểu (type / 타입) đổi, subtree tương ứng thường được thay và trạng thái (state / 상태) bên trong reset. `key` cho phép bạn nói rõ định danh (identity / 식별자) khi vị trí không đủ.

Một lỗi khó thấy là khai báo thành phần (component / 컴포넌트) bên trong thành phần (component / 컴포넌트) khác:

```jsx
function Page() {
  function Editor() {
    const [text, setText] = useState('');
    return <input value={text} onChange={e => setText(e.target.value)} />;
  }

  return <Editor />;
}
```

Mỗi kết xuất (render / 렌더링) của `Page` tạo một hàm (function / 함수) thành phần (component / 컴포넌트) kiểu (type / 타입) mới, nên React có thể coi `Editor` là kiểu (type / 타입) khác và reset trạng thái (state / 상태). Hãy khai báo thành phần (component / 컴포넌트) ở mô-đun (module / 모듈) phạm vi (scope / 범위) trừ khi bạn thật sự cần một hàm (function / 함수) helper không phải thành phần (component / 컴포넌트).

`key` cũng không chỉ dành cho danh sách (list / 목록). Nếu `documentId` đổi và draft phải bắt đầu như một editor instance mới, `<Editor key={documentId} />` biểu đạt reset định danh (identity / 식별자) trực tiếp. Ngược lại, dùng key ngẫu nhiên khiến subtree remount mỗi kết xuất (render / 렌더링), làm mất trạng thái (state / 상태), focus và có thể tăng chi phí DOM.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **10B. Reconciliation bằng ví dụ: kiểu (type / 타입), position và key** cho ta quy tắc; **11. Conditional rendering** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **12. List và key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi length bằng `0`, React có thể kết xuất (render / 렌더링) `0`. Viết rõ:

```jsx
{items.length > 0 && <List items={items} />}
```

Thành phần (component / 컴포넌트) có thể return `null` nếu không muốn kết xuất (render / 렌더링) DOM đầu ra (output / 출력).

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **12. List và key** tiếp nhận điểm tựa từ **11. Conditional rendering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12A. key là định danh (identity / 식별자), không chỉ để xóa warning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. List và `key`
Phần này nối mạch bài học với “12. List và `key`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
<ul>
  {users.map(user => (
    <li key={user.id}>{user.name}</li>
  ))}
</ul>
```

`key` giúp React xác định định danh (identity / 식별자) của sibling giữa các lần kết xuất (render / 렌더링). Key phải ổn định và unique trong cùng danh sách (list / 목록) sibling.

Không dùng `Math.random()` làm key vì định danh (identity / 식별자) đổi mỗi kết xuất (render / 렌더링). chỉ mục (index / 인덱스) chỉ an toàn khi danh sách (list / 목록) thực sự tĩnh, không reorder/insert/delete và row không có trạng thái (state / 상태)/DOM định danh (identity / 식별자) cần giữ.

`key` không được truyền xuống như prop bình thường. Nếu thành phần (component / 컴포넌트) cần ID, truyền riêng:

```jsx
<Item key={item.id} id={item.id} />
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **12A. key là định danh (identity / 식별자), không chỉ để xóa warning** tiếp nhận điểm tựa từ **12. List và key** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Form cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12A. `key` là định danh (identity / 식별자), không chỉ để xóa warning

Chỉ mục (index / 인덱스) key có thể làm cục bộ (local / 로컬) trạng thái (state / 상태), uncontrolled đầu vào (input / 입력), focus hoặc animation đi theo vị trí sai khi danh sách (list / 목록) reorder/insert/delete. ID ổn định từ dữ liệu là mặc định tốt hơn. chỉ mục (index / 인덱스) chỉ hợp lý khi danh sách (list / 목록) thật sự tĩnh. `key` cũng dùng ngoài danh sách (list / 목록) để reset subtree có chủ đích, ví dụ `<Chat key={contact.id} />`.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **13. Form cơ bản** tiếp nhận điểm tựa từ **12A. key là định danh (identity / 식별자), không chỉ để xóa warning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Lifting trạng thái (state / 상태) up và single nguồn chuẩn (source of truth / 정본)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Form cơ bản

Controlled đầu vào (input / 입력):

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

Button trong form thường mặc định là submit. Nếu chỉ là hành động (action / 동작) phụ, ghi `type="button"`.

Controlled đầu vào (input / 입력) dùng React trạng thái (state / 상태) làm nguồn chuẩn (source of truth / 정본). Uncontrolled đầu vào (input / 입력) để DOM giữ giá trị (value / 값) và đọc qua ref/FormData. Cả hai đều hợp lệ; beginner nên nắm controlled trước.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **13. Form cơ bản** nêu điều cần giải thích; **14. Lifting trạng thái (state / 상태) up và single nguồn chuẩn (source of truth / 정본)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Composition và children** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Lifting trạng thái (state / 상태) up và single nguồn chuẩn (source of truth / 정본)

Khi hai thành phần (component / 컴포넌트) cần đồng bộ cùng dữ liệu, đưa trạng thái (state / 상태) lên ancestor chung gần nhất.

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

Mỗi mẩu trạng thái (state / 상태) quan trọng nên có một đơn vị sở hữu (owner / 오너) rõ ràng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **14. Lifting trạng thái (state / 상태) up và single nguồn chuẩn (source of truth / 정본)** nêu điều cần giải thích; **15. Composition và children** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Styling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Composition và `children`
Phần này nối mạch bài học với “15. Composition và `children`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

`children` là prop chứa nội dung giữa opening/closing tag. Có thể truyền JSX qua prop tên riêng khi ngữ nghĩa (semantic / 의미적) rõ hơn.

React ưu tiên composition hơn inheritance cho UI.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **16. Styling** tiếp nhận điểm tựa từ **15. Composition và children** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Strict chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Ứng dụng lớn có thể dùng utility CSS hoặc thành phần (component / 컴포넌트) thư viện (library / 라이브러리); đó là ecosystem, không phải React cốt lõi (core / 핵심).

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **17. Strict chế độ (mode / 모드)** tiếp nhận điểm tựa từ **16. Styling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. gỡ lỗi (debug / 디버그)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Strict chế độ (mode / 모드)

`<StrictMode>` bật các kiểm tra development. React có thể chạy lại một số lô-gic (logic / 논리) để phát hiện kết xuất (render / 렌더링) không pure hoặc cleanup sai. Vì vậy beginner có thể thấy log/tác động (effect / 효과) nhiều hơn mong đợi trong development.

Không tắt Strict chế độ (mode / 모드) chỉ để “hết chạy hai lần”. Hãy sửa purity và cleanup. môi trường vận hành (production / 운영 환경) không chạy các development checks theo cùng cách.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — Strict chế độ (mode / 모드) từ React 18 dễ làm người mới hiểu nhầm
>
> React 18 thêm development-only check mô phỏng việc setup/cleanup rồi setup lại một số tác động (effect / 효과) khi thành phần (component / 컴포넌트) mount lần đầu trong Strict chế độ (mode / 모드). Mục tiêu là phát hiện tác động (effect / 효과) không cleanup đúng và chuẩn bị mã (code / 코드) cho kiến trúc có thể preserve/reuse trạng thái (state / 상태). Vì vậy khi development thấy tác động (effect / 효과) hoặc log xuất hiện nhiều lần, đừng vội kết luận React bị lỗi hoặc tắt Strict chế độ (mode / 모드); trước tiên kiểm tra purity và cleanup. môi trường vận hành (production / 운영 환경) không chạy cùng kiểu kiểm tra development này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **18. gỡ lỗi (debug / 디버그)** tiếp nhận điểm tựa từ **17. Strict chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Mini project Todo hoàn chỉnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. gỡ lỗi (debug / 디버그)

Phân biệt bốn lớp lỗi: JavaScript thời gian chạy (runtime / 런타임), React trạng thái (state / 상태)/kết xuất (render / 렌더링), DOM/CSS và mạng (network / 네트워크)/API. trình duyệt (browser / 브라우저) DevTools dùng Console, mạng (network / 네트워크), Elements, hiệu năng (performance / 성능); React DevTools cho thành phần (component / 컴포넌트) cây (tree / 트리), props/trạng thái (state / 상태) và profiler.

Khi gỡ lỗi (debug / 디버그) trạng thái (state / 상태), log đầu vào (input / 입력) và chuyển tiếp (transition / 전이) thay vì chỉ log trạng thái (state / 상태) ngay sau setter.

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **19. Mini project Todo hoàn chỉnh** tiếp nhận điểm tựa từ **18. gỡ lỗi (debug / 디버그)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Các lỗi beginner thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Mini project Todo hoàn chỉnh
Phần này nối mạch bài học với “19. Mini project Todo hoàn chỉnh”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

`nextId` ngoài thành phần (component / 컴포넌트) chỉ phù hợp demo cục bộ (local / 로컬). môi trường vận hành (production / 운영 환경) thường dùng ID máy chủ (server / 서버)/cơ sở dữ liệu (database / 데이터베이스) hoặc chiến lược định danh phù hợp.

> **Chuyển mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Beginner**, **20. Các lỗi beginner thường gặp** tiếp nhận điểm tựa từ **19. Mini project Todo hoàn chỉnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Kết thúc mức (level / 수준) Beginner** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Các lỗi beginner thường gặp

### Gọi handler trong kết xuất (render / 렌더링)

Sai:

```jsx
<button onClick={save()}>Save</button>
```

Đúng:

```jsx
<button onClick={save}>Save</button>
```

### Mutate trạng thái (state / 상태)

Sai:

```jsx
items.push(newItem);
setItems(items);
```

Đúng:

```jsx
setItems(prev => [...prev, newItem]);
```

### Trạng thái (state / 상태) dư thừa

Không nên lưu `fullName` nếu có thể tính từ `firstName` và `lastName`:

```jsx
const fullName = `${firstName} ${lastName}`.trim();
```

### Định nghĩa component bên trong component
Phần này nối mạch bài học với “Định nghĩa component bên trong component”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
function App() {
  function Child() {
    return <div>Child</div>;
  }
  return <Child />;
}
```

Mỗi kết xuất (render / 렌더링) có thể tạo thành phần (component / 컴포넌트) định danh (identity / 식별자) mới và gây reset trạng thái (state / 상태). thành phần (component / 컴포넌트) thường nên được định nghĩa top-level.

### Hiểu sai setter là assignment đồng bộ

`setCount(count + 1)` không làm biến `count` trong closure hiện tại thay đổi ngay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Beginner**, **21. Kết thúc mức (level / 수준) Beginner** tiếp nhận điểm tựa từ **20. Các lỗi beginner thường gặp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phiên bản (version / 버전) Map cho mức (level / 수준) Beginner** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Kết thúc mức (level / 수준) Beginner

Bạn nên tự giải thích được: React khác DOM imperative ở đâu; JSX là gì; thành phần (component / 컴포넌트), props và trạng thái (state / 상태) khác nhau thế nào; vì sao trạng thái (state / 상태) cập nhật (update / 업데이트) phải immutable; vì sao trạng thái (state / 상태) là snapshot; `key` ảnh hưởng định danh (identity / 식별자) thế nào; controlled form hoạt động ra sao; khi nào nên derive giá trị thay vì lưu trạng thái (state / 상태).

Bạn cũng nên tự xây được CRUD nhỏ client-side mà không bản sao (copy / 복사) kiến trúc (architecture / 아키텍처), và chỉ ra rõ đơn vị sở hữu (owner / 오너) của từng trạng thái (state / 상태).

> **Chuyển mạch:** Trong **React Master ghi chú (note / 노트) — Beginner**, **Phiên bản (version / 버전) Map cho mức (level / 수준) Beginner** tiếp nhận điểm tựa từ **21. Kết thúc mức (level / 수준) Beginner** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Phiên bản (version / 버전) Map cho mức (level / 수준) Beginner

Ở mức (level / 수준) Beginner, chỉ cần ghi nhớ bốn mốc để không bị rối khi đọc tài liệu trên Internet. **React 16.8** là lúc Hooks xuất hiện; **React 18** là lúc `createRoot`, automatic batching và concurrent foundations trở thành chuẩn hiện đại; **React 18.3** là bước đệm cảnh báo trước khi nâng lên 19; **React 19.x** mở rộng Actions/máy chủ (server / 서버) APIs và đơn giản hóa một số cú pháp (syntax / 문법) như ref-as-prop. Baseline của bộ ghi chú (note / 노트) là **React 19.3**.

Nếu một đoạn mã (code / 코드) khác tài liệu này, hãy kiểm tra `package.json` trước khi cho rằng cú pháp nào “đúng” hay “sai”:

```json
{
  "dependencies": {
    "react": "...",
    "react-dom": "..."
  }
}
```

React và React DOM nên được xem như một cặp phiên bản (version / 버전) tương thích. Với khung phần mềm (framework / 프레임워크) như Next.js, còn phải kiểm tra khung phần mềm (framework / 프레임워크) đang hỗ trợ/pin React phiên bản (version / 버전) nào; không tự nâng React độc lập chỉ vì thấy API mới trên react.dev.

> **Bàn giao:** Sau **Phiên bản (version / 버전) Map cho mức (level / 수준) Beginner**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
