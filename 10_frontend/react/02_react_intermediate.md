# React Master ghi chú (note / 노트) — Intermediate

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **React Master ghi chú (note / 노트) — Intermediate**. Route đi từ state modeling → Rules of React/Hooks → effects, refs, reducers và context → custom Hooks, data flow và feature architecture → debugging/performance, để ứng dụng lớn vẫn giữ được invariant dữ liệu.

> Mục tiêu của mức (level / 수준) này là chuyển từ “biết viết thành phần (component / 컴포넌트)” sang “hiểu vòng đời dữ liệu, tác động (effect / 효과), ref, reducer, ngữ cảnh (context / 맥락), custom Hook, luồng dữ liệu (data flow / 데이터 흐름) và kiến trúc tính năng (feature / 기능) ở mức ứng dụng thật”.

> ### phiên bản (version / 버전) orientation cho mức (level / 수준) Intermediate
>
> Các Hook nền tảng `useState`, `useEffect`, `useRef`, `useContext`, `useReducer`, `useMemo`, `useCallback` đã tồn tại từ thời React 16.8, nhưng cách React scheduling/rendering chúng đã tiến hóa mạnh ở React 18+. Khi học tệp (file / 파일) này, hãy dùng **React 19.3 ngữ nghĩa (semantics / 의미론)** làm chuẩn và chỉ quan tâm phiên bản (version / 버전) khi API thật sự được thêm hoặc thay đổi đặc tả hợp đồng (contract / 계약).

## 1. Mô hình hóa trạng thái (state / 상태) trước khi học Hook nâng cao

Trước khi thêm `useEffect`, `useMemo`, ngữ cảnh (context / 맥락) hoặc store, hãy phân loại dữ liệu. Nhiều mã (code / 코드) React phức tạp không phải vì thiếu Hook mà vì trạng thái (state / 상태) được mô hình hóa sai. Một giá trị nên là trạng thái (state / 상태) khi nó thay đổi theo thời gian và thay đổi đó phải ảnh hưởng kết xuất (render / 렌더링). Nếu có thể tính trực tiếp từ props/trạng thái (state / 상태) hiện có, nó thường là derived giá trị (value / 값). Nếu cần tồn tại qua kết xuất (render / 렌더링) nhưng thay đổi không cần kết xuất (render / 렌더링) lại, `ref` thường phù hợp. Nếu dữ liệu thuộc máy chủ (server / 서버), URL hoặc bộ nhớ đệm (cache / 캐시) ngoài React, đừng mặc định biến nó thành cục bộ (local / 로컬) trạng thái (state / 상태).

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

Nguyên tắc này giảm duplicate nguồn chuẩn (source of truth / 정본) và giảm tác động (effect / 효과) không cần thiết.

> **Nối mạch:** State model xác định invariant trước khi Hook được chọn; Rules of React/Hooks biến invariant đó thành điều kiện để component render thuần và Hook gọi đúng vị trí. `useEffect` tiếp theo chỉ xử lý synchronization với hệ thống bên ngoài.

## 1A. Rules of React và Rules of Hooks

Hook phải gọi ở top mức (level / 수준) của hàm (function / 함수) thành phần (component / 컴포넌트) hoặc Custom Hook, không tùy ý trong điều kiện (condition / 조건), vòng lặp (loop / 루프), nested hàm (function / 함수) hay sự kiện (event / 이벤트) handler. React dựa vào thứ tự lời gọi (call / 호출) ổn định để ghép mỗi Hook với trạng thái (state / 상태) tương ứng giữa các kết xuất (render / 렌더링); vì vậy `eslint-plugin-react-hooks` là tính đúng đắn (correctness / 정확성) tooling, không chỉ style.

Trước React 16.8, tái sử dụng stateful lô-gic (logic / 논리) chủ yếu qua lớp (class / 클래스), HOC và kết xuất (render / 렌더링) props. Hooks giảm wrapper nesting và colocate concern tốt hơn nhưng không làm HOC/kết xuất (render / 렌더링) props sai; chúng vẫn gặp trong Redux/router/thư viện (library / 라이브러리) cũ. di chuyển (migration / 마이그레이션) nên chuyển concern chứ không search-replace cú pháp (syntax / 문법).

> **Nối mạch:** Rules of Hooks đặt điều kiện gọi Hook; `useEffect` áp dụng điều kiện đó cho setup/cleanup và external sync. Phần class lifecycle tiếp theo đối chiếu cùng intent trong code React cũ.

## 2. `useEffect`: synchronization chứ không phải “mã (code / 코드) chạy sau kết xuất (render / 렌더링)”

`useEffect` dùng để đồng bộ thành phần (component / 컴포넌트) với một hệ thống nằm ngoài mô hình kết xuất (render / 렌더링) React, ví dụ mạng (network / 네트워크) liên kết (connection / 연결), timer, trình duyệt (browser / 브라우저) sự kiện (event / 이벤트), WebSocket, observer, analytics tích hợp (integration / 통합) hoặc widget imperative.

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

Mô hình tư duy (mental model / 사고 모델) đúng là setup/cleanup synchronization. Khi `roomId` đổi, React cleanup liên kết (connection / 연결) cũ rồi setup liên kết (connection / 연결) mới.

Không truyền phụ thuộc (dependency / 의존성) array nghĩa tác động (effect / 효과) có thể chạy sau mỗi lần ghi nhận (commit / 커밋) phù hợp. `[]` thường biểu diễn setup theo thời gian tồn tại (lifetime / 수명) instance. `[roomId]` nghĩa synchronization phụ thuộc `roomId`. phụ thuộc (dependency / 의존성) không phải công cụ để “ép chạy ít lần”; nó phải phản ánh reactive giá trị (value / 값) tác động (effect / 효과) đọc.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — `useEffect` không đổi thành “vòng đời (lifecycle / 생명주기) mới”
>
> `useEffect` có từ React 16.8, nhưng React 18 Strict chế độ (mode / 모드) khiến các tác động (effect / 효과) viết sai cleanup dễ lộ hơn vì development có thể setup/cleanup thêm để kiểm tra. Vì vậy các tutorial cũ mô tả `useEffect(..., [])` đơn giản là “`componentDidMount` cho hàm (function / 함수) thành phần (component / 컴포넌트)” là cách hiểu thiếu chính xác. mô hình tư duy (mental model / 사고 모델) synchronization trong tài liệu này phù hợp hơn với React 18/19 và tính đồng thời (concurrency / 동시성).

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **2. useEffect: synchronization chứ không phải “mã (code / 코드) chạy sau kết xuất (render / 렌더링)”** đặt đầu vào cho **2A. lớp (class / 클래스) vòng đời (lifecycle / 생명주기) đầy đủ và cách đọc mã (code / 코드) React cũ**, rồi **2B. tác động (effect / 효과) có vòng đời (lifecycle / 생명주기) start/stop riêng, không phải bản sao vòng đời (lifecycle / 생명주기) thành phần (component / 컴포넌트)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2A. lớp (class / 클래스) vòng đời (lifecycle / 생명주기) đầy đủ và cách đọc mã (code / 코드) React cũ

Trước Hooks, vòng đời (lifecycle / 생명주기) methods là cách chính để chạy lô-gic (logic / 논리) theo các giai đoạn của lớp (class / 클래스) thành phần (component / 컴포넌트). Khi bảo trì mã (code / 코드) cũ, đừng chỉ nhớ tên phương thức (method / 메서드); cần hiểu phương thức (method / 메서드) thuộc kết xuất (render / 렌더링) phase hay lần ghi nhận (commit / 커밋) phase và vì sao một số vòng đời (lifecycle / 생명주기) bị đánh dấu `UNSAFE_`.

### Mount lifecycle
Phần này nối mạch bài học với “Mount lifecycle”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

`constructor` dùng để khởi tạo trạng thái (state / 상태)/bind. `render` tính UI. `componentDidMount` chạy sau lần ghi nhận (commit / 커밋) và thường dùng setup subscription, mạng (network / 네트워크) tích hợp (integration / 통합) hoặc DOM công việc (work / 작업). `componentWillUnmount` cleanup tài nguyên (resource / 자원).

Hàm (function / 함수) thành phần (component / 컴포넌트) thường gom setup/cleanup của cùng một concern:

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
Phần này nối mạch bài học với “Update lifecycle: `componentDidUpdate`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Lớp (class / 클래스) nhà phát triển (developer / 개발자) phải tự so sánh previous/hiện tại (current / 현재) props. tác động (effect / 효과) phụ thuộc (dependency / 의존성) hiện đại biểu đạt intent đồng bộ theo `roomId` trực tiếp hơn.

### `shouldComponentUpdate`
Phần này nối mạch bài học với “`shouldComponentUpdate`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Phương thức (method / 메서드) này cho phép bỏ qua cập nhật (update / 업데이트). `PureComponent` làm shallow comparison tự động. Với hàm (function / 함수) thành phần (component / 컴포넌트), `memo` là khái niệm gần; `useMemo` và `useCallback` kiểm soát giá trị (value / 값)/hàm (function / 함수) định danh (identity / 식별자).

### `getSnapshotBeforeUpdate`

API này chạy ngay trước DOM lần ghi nhận (commit / 커밋) và giá trị trả về được truyền vào `componentDidUpdate`. Use trường hợp (case / 사례) điển hình là giữ vị trí scroll.

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

Không có Hook một-một hoàn toàn tương đương mọi chi tiết vòng đời (lifecycle / 생명주기) này. Tùy mục tiêu có thể dùng `useLayoutEffect`, refs hoặc thay đổi mô hình dữ liệu (data model / 데이터 모델).

### `static getDerivedStateFromProps`
Phần này nối mạch bài học với “`static getDerivedStateFromProps`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

API này xử lý một số derived-state cases nhưng dễ tạo duplicated trạng thái (state / 상태). Với mã (code / 코드) hiện đại, thường nên cân nhắc derive trực tiếp, reset bằng `key`, controlled mô hình (model / 모델) hoặc reducer trước.

### Các vòng đời (lifecycle / 생명주기) cũ `componentWill*`

Mã (code / 코드) legacy có thể có:

```jsx
componentWillMount()
componentWillReceiveProps(nextProps)
componentWillUpdate(nextProps, nextState)
```

Các phương thức (method / 메서드) này được đổi sang:

```jsx
UNSAFE_componentWillMount()
UNSAFE_componentWillReceiveProps()
UNSAFE_componentWillUpdate()
```

Vấn đề của chúng là side tác động (effect / 효과) hoặc các giả định (assumptions / 가정들) trong render-phase công việc (work / 작업) không an toàn với rendering có thể bị restart, suspend hoặc bỏ. Không migrate bằng search-replace. `componentWillMount` thường tách initialization vào constructor/trạng thái (state / 상태) initializer và side tác động (effect / 효과) vào mount tác động (effect / 효과)/vòng đời (lifecycle / 생명주기); `componentWillReceiveProps` thường thay bằng kết xuất (render / 렌더링) derivation, controlled dữ liệu (data / 데이터) hoặc reducer; `componentWillUpdate` thường chuyển sang `componentDidUpdate`, `getSnapshotBeforeUpdate` hoặc bố cục (layout / 레이아웃)/tác động (effect / 효과) lô-gic (logic / 논리) tùy mục tiêu.

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, **2A. lớp (class / 클래스) vòng đời (lifecycle / 생명주기) đầy đủ và cách đọc mã (code / 코드) React cũ** đặt đầu vào cho **2B. tác động (effect / 효과) có vòng đời (lifecycle / 생명주기) start/stop riêng, không phải bản sao vòng đời (lifecycle / 생명주기) thành phần (component / 컴포넌트)**, rồi **3. phụ thuộc (dependency / 의존성) và stale closure** mở rộng hệ quả hoặc giới hạn liên quan.

## 2B. tác động (effect / 효과) có vòng đời (lifecycle / 생명주기) start/stop riêng, không phải bản sao vòng đời (lifecycle / 생명주기) thành phần (component / 컴포넌트)

Thành phần (component / 컴포넌트) được mô tả bằng mount/cập nhật (update / 업데이트)/unmount, nhưng một tác động (effect / 효과) nên được đọc như một **synchronization tiến trình (process / 프로세스)** có hai hành động: bắt đầu đồng bộ và dừng đồng bộ. Khi phụ thuộc (dependency / 의존성) thay đổi, React có thể stop tiến trình (process / 프로세스) cũ rồi start tiến trình (process / 프로세스) mới dù thành phần (component / 컴포넌트) vẫn là cùng một instance. Vì vậy một tác động (effect / 효과) kết nối room theo `roomId` nên được hiểu là “giữ liên kết (connection / 연결) bên ngoài khớp với `roomId` hiện tại”, không phải “chạy đoạn mã (code / 코드) này khi cập nhật (update / 업데이트)”.

Phụ thuộc (dependency / 의존성) array không phải lịch hẹn do nhà phát triển (developer / 개발자) tùy chọn. Nó là mô tả các reactive values mà tiến trình (process / 프로세스) đọc. Nếu phải tắt lint để giữ phụ thuộc (dependency / 의존성) thiếu, thường mô hình tư duy (mental model / 사고 모델) đang sai: hoặc lô-gic (logic / 논리) là sự kiện (event / 이벤트) nên đặt trong sự kiện (event / 이벤트) handler, hoặc giá trị (value / 값) nên được derive trong kết xuất (render / 렌더링), hoặc tác động (effect / 효과) đang gộp nhiều tiến trình (process / 프로세스) độc lập. Một tác động (effect / 효과) tốt thường có setup/cleanup đối xứng và có thể chạy lại mà không làm hệ thống ngoài bị leak hoặc nhân đôi subscription.

Khi migrate lớp (class / 클래스), đừng ghép máy móc `componentDidMount + componentDidUpdate + componentWillUnmount` vào một tác động (effect / 효과) chỉ vì tên vòng đời (lifecycle / 생명주기) tương ứng. Hãy xác định tài nguyên (resource / 자원) nào cần synchronize, phụ thuộc (dependency / 의존성) nào làm cấu hình (configuration / 구성) của tài nguyên (resource / 자원) đó, rồi viết một start/stop cycle cho chính tài nguyên (resource / 자원) ấy.

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **2B. tác động (effect / 효과) có vòng đời (lifecycle / 생명주기) start/stop riêng, không phải bản sao vòng đời (lifecycle / 생명주기) thành phần (component / 컴포넌트)** đặt đầu vào cho **3. phụ thuộc (dependency / 의존성) và stale closure**, rồi **4. Cleanup, race điều kiện (condition / 조건) và AbortController** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. phụ thuộc (dependency / 의존성) và stale closure

Mỗi kết xuất (render / 렌더링) tạo closure mới. hàm (function / 함수) trong kết xuất (render / 렌더링) nhìn thấy props/trạng thái (state / 상태) của kết xuất (render / 렌더링) đó.

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

Interval giữ `count` của kết xuất (render / 렌더링) đầu tiên. Tắt lint quy tắc (rule / 규칙) không sửa bản chất. Nếu interval phải phụ thuộc count, thêm phụ thuộc (dependency / 의존성). Nếu liên kết (connection / 연결) phải ổn định nhưng callback cần đọc giá trị (value / 값) mới nhất, React 19.2+ có `useEffectEvent`, sẽ học ở Advanced.

Đối tượng (object / 객체)/hàm (function / 함수) tạo trong kết xuất (render / 렌더링) có định danh (identity / 식별자) mới:

```jsx
const options = { serverUrl, roomId };

useEffect(() => {
  return connect(options);
}, [options]);
```

Tác động (effect / 효과) restart mỗi kết xuất (render / 렌더링). Thường tốt hơn:

```jsx
useEffect(() => {
  const options = { serverUrl, roomId };
  return connect(options);
}, [serverUrl, roomId]);
```

Không dùng `useMemo` theo phản xạ chỉ để “làm phụ thuộc (dependency / 의존성) yên”. Trước tiên sửa cấu trúc.

> **Nối mạch:** Dependency và stale closure giải thích vì sao effect đọc dữ liệu cũ; cleanup, race control và `AbortController` tiếp theo bảo vệ request lifecycle.

## 4. Cleanup, race điều kiện (condition / 조건) và `AbortController`

Fetch trong tác động (effect / 효과) có thể gặp race điều kiện (condition / 조건): yêu cầu (request / 요청) cũ trả sau yêu cầu (request / 요청) mới rồi ghi đè dữ liệu. Có thể guard bằng flag hoặc tốt hơn, hủy yêu cầu (request / 요청) nếu API hỗ trợ.

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

Ở môi trường vận hành (production / 운영 환경), server-state thư viện (library / 라이브러리) hoặc khung phần mềm (framework / 프레임워크) dữ liệu (data / 데이터) tầng (layer / 계층) thường xử lý caching, dedupe, thử lại (retry / 재시도) và race điều kiện (condition / 조건) tốt hơn fetch tác động (effect / 효과) tự viết ở mọi thành phần (component / 컴포넌트).

> **Nối mạch:** Cleanup/AbortController close the request lifecycle; the next question is whether the effect is needed at all, before Hooks are modeled as identity-indexed state slots.

## 5. Khi nào không cần tác động (effect / 효과)?

Không dùng tác động (effect / 효과) để tính derived trạng thái (state / 상태):

```jsx
const fullName = `${firstName} ${lastName}`;
```

Không dùng tác động (effect / 효과) để phản ứng với sự kiện (event / 이벤트) mà bạn đã biết nguyên nhân:

```jsx
async function handleSubmit(event) {
  event.preventDefault();
  await postForm();
}
```

thường tốt hơn mẫu (pattern / 패턴) set một flag rồi tác động (effect / 효과) nhìn flag để gọi `postForm()`.

Tác động (effect / 효과) phù hợp khi ngữ nghĩa (semantics / 의미론) là: “Vì thành phần (component / 컴포넌트) hiện đang tồn tại với cấu hình X nên tài nguyên (resource / 자원) bên ngoài phải được đồng bộ với X.”

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **5A. Hook mô hình tư duy (mental model / 사고 모델): bộ nhớ (memory / 메모리) slot theo thành phần (component / 컴포넌트) định danh (identity / 식별자)** tổng hợp từ **5. Khi nào không cần tác động (effect / 효과)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **6. useRef** mở rộng hệ quả hoặc giới hạn liên quan.

## 5A. Hook mô hình tư duy (mental model / 사고 모델): bộ nhớ (memory / 메모리) slot theo thành phần (component / 컴포넌트) định danh (identity / 식별자)

Hooks không phải magic hàm (function / 함수) toàn cục. React gắn trạng thái (state / 상태)/ref/tác động (effect / 효과) bookkeeping với thành phần (component / 컴포넌트) định danh (identity / 식별자) và dựa vào **thứ tự Hook lời gọi (call / 호출) ổn định** để nối lần kết xuất (render / 렌더링) hiện tại với dữ liệu của lần kết xuất (render / 렌더링) trước. Đây là lý do Hook phải được gọi ở top mức (level / 수준) thay vì điều kiện (condition / 조건) hoặc vòng lặp (loop / 루프).

Mỗi kết xuất (render / 렌더링) tạo closure mới. Hook không “cập nhật biến cũ”; React gọi thành phần (component / 컴포넌트) lại, trả snapshot mới và các callback của kết xuất (render / 렌더링) đó đóng trên snapshot tương ứng. `useRef` là ngoại lệ có đối tượng (object / 객체) định danh (identity / 식별자) ổn định nhưng mutation `current` không yêu cầu kết xuất (render / 렌더링), vì thế ref phù hợp dữ liệu kỹ thuật chứ không phải nguồn chuẩn (source of truth / 정본) cho UI.

Custom Hook chia sẻ **lô-gic (logic / 논리) và giao thức (protocol / 프로토콜)**, không chia sẻ một trạng thái (state / 상태) instance mặc định. Hai thành phần (component / 컴포넌트) gọi `useOnlineStatus()` thường có hai Hook instances; nếu chúng cùng subscribe một bên ngoài (external / 외부) store thì nguồn (source / 소스) dữ liệu được chia sẻ nằm ở store/subscription tầng (layer / 계층), không phải do “Hook là toàn cục (global / 전역)”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **6. useRef** tổng hợp từ **5A. Hook mô hình tư duy (mental model / 사고 모델): bộ nhớ (memory / 메모리) slot theo thành phần (component / 컴포넌트) định danh (identity / 식별자)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **7. DOM ref và imperative escape hatch** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. `useRef`

`useRef(initialValue)` trả đối tượng (object / 객체) ổn định `{ current }`. Thay đổi `ref.current` không trigger kết xuất (render / 렌더링).

```jsx
const timerRef = useRef(null);

function start() {
  timerRef.current = setInterval(...);
}
```

Ref phù hợp với timer ID, DOM nút (node / 노드), instance thư viện, observer, mutable technical giá trị (value / 값). Không dùng ref thay trạng thái (state / 상태) nếu UI cần phản ánh giá trị đó.

> **Nối mạch:** `useRef` giữ mutable handle mà không tạo render; DOM ref dùng handle đó cho focus, measurement và imperative integration. `forwardRef`/ref-as-prop tiếp theo mở handle qua component boundary.

## 7. DOM ref và imperative escape hatch
Phần này nối mạch bài học với “7. DOM ref và imperative escape hatch”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Ref phù hợp cho focus, selection, scroll, đo lường (measurement / 측정) hoặc tích hợp DOM thư viện (library / 라이브러리) imperative. Không mutate DOM mà React đang quản lý theo cách xung đột với kết xuất (render / 렌더링).

> **Nối mạch:** DOM ref là imperative boundary; `forwardRef` và ref-as-prop quyết định boundary đó được expose thế nào. Lịch sử refs tiếp theo giải thích vì sao các dạng cũ vẫn còn trong codebase React 18.

## 8. `forwardRef` và ref-as-prop

React 18/mã (code / 코드) cũ thường dùng:

```jsx
const MyInput = forwardRef(function MyInput(props, ref) {
  return <input {...props} ref={ref} />;
});
```

React 19 hỗ trợ ref như prop trong hàm (function / 함수) thành phần (component / 컴포넌트) theo mô hình (model / 모델) mới:

```jsx
function MyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}
```

Không xóa `forwardRef` tùy tiện trong thư viện (library / 라이브러리) hỗ trợ React 18.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — ref API thay đổi đáng chú ý ở React 19
>
> `useRef` bản thân không phải API mới của React 19. Thay đổi đáng chú ý là **hàm (function / 함수) thành phần (component / 컴포넌트) có thể nhận `ref` như prop trong React 19**, làm giảm nhu cầu dùng `forwardRef` trong mã (code / 코드) mới. Tuy vậy `forwardRef` vẫn xuất hiện dày đặc trong thư viện (library / 라이브러리) và codebase React 18, nên cần biết cả hai dạng.

> **Nối mạch:** `forwardRef`/ref-as-prop expose an imperative handle; ref history explains the evolution, while `findDOMNode` remains a legacy escape hatch with weaker ownership.

## 7A. Lịch sử refs: string refs → callback refs → `createRef` → `useRef` → ref-as-prop

Refs thay đổi nhiều qua lịch sử React.

### String refs — legacy và đã bị remove
Phần này nối mạch bài học với “String refs — legacy và đã bị remove”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

React lưu nút (node / 노드) vào `this.refs.input`. String refs có hạn chế về đơn vị sở hữu (owner / 오너), static phân tích (analysis / 분석) và composition; bị deprecate từ React 16.3 và remove trong React 19.

### Callback refs
Phần này nối mạch bài học với “Callback refs”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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
Phần này nối mạch bài học với “`React.createRef` — React 16.3+”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

`createRef` thường dùng cho lớp (class / 클래스) thành phần (component / 컴포넌트); mỗi lần gọi tạo đối tượng (object / 객체) mới nên thường khởi tạo một lần.

### `useRef` — React 16.8+
Phần này nối mạch bài học với “`useRef` — React 16.8+”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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
Phần này nối mạch bài học với “`forwardRef` — React 16.3+”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

React 19 cho hàm (function / 함수) thành phần (component / 컴포넌트) nhận `ref` như prop:

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

Thư viện (library / 라이브러리) hỗ trợ (support / 지원) React 18 vẫn cần `forwardRef`, vì vậy không nên xóa nó chỉ vì dự án (project / 프로젝트) chính đã lên React 19.

> **Nối mạch:** Ref history cho thấy boundary ngày càng explicit; `findDOMNode` là escape hatch phá boundary đó. `useReducer` tiếp theo chuyển từ imperative node access sang explicit state transitions.

## 7B. `findDOMNode`: escape hatch legacy

Lớp (class / 클래스) mã (code / 코드) cũ hoặc third-party thư viện (library / 라이브러리) có thể dùng:

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

`findDOMNode` đi xuyên lớp trừu tượng (abstraction / 추상화) từ thành phần (component / 컴포넌트) instance xuống DOM, phụ thuộc cấu trúc (structure / 구조) kết xuất (render / 렌더링) và khó tương thích với refactoring/concurrent kiến trúc (architecture / 아키텍처). API bị deprecate từ React 16.6 và remove trong React 19.

Thay bằng tường minh (explicit / 명시적) ref:

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

Nếu Strict chế độ (mode / 모드) báo warning `findDOMNode`, phụ thuộc (dependency / 의존성) cũ có thể là nguồn warning; cần upgrade hoặc thay tích hợp (integration / 통합).

> **Nối mạch:** `useReducer` thay imperative escape hatch bằng state machine cục bộ có action và transition rõ. Phần 9A làm rõ reducer không phải Redux thu nhỏ mà là pure transition function.

## 9. `useReducer`

`useReducer` phù hợp khi trạng thái (state / 상태) có nhiều chuyển tiếp (transition / 전이) liên quan hoặc lô-gic (logic / 논리) cập nhật (update / 업데이트) phức tạp.

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

Reducer phải pure. hành động (action / 동작) nên mô tả intent hoặc điều xảy ra thay vì cách mutate chi tiết.

> **Nối mạch:** `useReducer` cung cấp state transition thuần và action intent; context tiếp theo quyết định cách truyền state/dispatch qua subtree mà không prop-drill.

## 9A. Reducer là chuyển tiếp (transition / 전이) hàm (function / 함수), không phải Redux thu nhỏ

`useReducer` hữu ích khi nhiều sự kiện (event / 이벤트) cùng thay đổi một trạng thái (state / 상태) mô hình (model / 모델) có quy tắc (rule / 규칙) rõ. Reducer nên trả next trạng thái (state / 상태) từ `(state, action)` mà không làm side tác động (effect / 효과). sự kiện (event / 이벤트) handler chịu trách nhiệm tạo hành động (action / 동작); reducer chịu trách nhiệm tính chuyển tiếp (transition / 전이); tác động (effect / 효과) chỉ dùng nếu chuyển tiếp (transition / 전이) cần đồng bộ một hệ thống bên ngoài sau lần ghi nhận (commit / 커밋).

```jsx
function reducer(state, action) {
  switch (action.type) {
    case 'renamed':
      return { ...state, name: action.name };
    case 'submitted':
      return { ...state, status: 'submitting' };
    case 'succeeded':
      return { ...state, status: 'success' };
    default:
      return state;
  }
}
```

Khi trạng thái (state / 상태) bắt đầu có các trạng thái loại trừ nhau như `idle/loading/success/error`, một trường dữ liệu (field / 필드) `status` hoặc máy trạng thái (state machine / 상태 머신) rõ ràng thường tốt hơn nhiều boolean có thể rơi vào tổ hợp vô nghĩa. Reducer không bắt buộc cho mọi form; nó đáng giá khi chuyển tiếp (transition / 전이) ngữ nghĩa (semantics / 의미론) quan trọng hơn độ ngắn của setter.

> **Nối mạch:** Reducer mô tả state transition; `useContext` đưa state và dispatch tới consumer theo subtree boundary. Legacy context tiếp theo giải thích cùng nhu cầu trong API cũ và rủi ro migration.

## 10. ngữ cảnh (context / 맥락) và `useContext`

Ngữ cảnh (context / 맥락) truyền dữ liệu xuyên subtree mà không phải prop drilling qua các tầng không cần dữ liệu đó.

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

React 19 cho phép kết xuất (render / 렌더링) ngữ cảnh (context / 맥락) đối tượng (object / 객체) trực tiếp như provider. React 18 thường dùng `<ThemeContext.Provider value="dark">`.

Ngữ cảnh (context / 맥락) phù hợp theme, locale, auth/session view-model hoặc phụ thuộc (dependency / 의존성) theo subtree. Không nên biến mọi trạng thái (state / 상태) thành ngữ cảnh (context / 맥락). Provider giá trị (value / 값) đổi định danh (identity / 식별자) có thể làm bên tiêu thụ (consumer / 소비자) kết xuất (render / 렌더링) lại; giant ngữ cảnh (context / 맥락) tạo coupling lớn.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — Provider cú pháp (syntax / 문법) của React 19
>
> Với React 18 và mã (code / 코드) cũ, provider thường viết `<ThemeContext.Provider value={theme}>`. React 19 cho phép viết ngắn trực tiếp `<ThemeContext value={theme}>`. Hai đoạn mã (code / 코드) thể hiện cùng ý tưởng luồng dữ liệu (data flow / 데이터 흐름); khác biệt chủ yếu là cú pháp (syntax / 문법)/phiên bản (version / 버전). Khi viết thư viện (library / 라이브러리) phải cân nhắc phiên bản (version / 버전) tối thiểu mà gói (package / 패키지) hỗ trợ.

> **Nối mạch:** Legacy context có cùng mục tiêu truyền dependency nhưng boundary và typing kém explicit hơn. Reducer + context tiếp theo ghép state transition với provider scope rõ ràng.

## 10A. ngữ cảnh (context / 맥락) cũ: `contextTypes` và `getChildContext`

Trước new ngữ cảnh (context / 맥락) API, lớp (class / 클래스) thành phần (component / 컴포넌트) dùng legacy ngữ cảnh (context / 맥락) cơ chế (mechanism / 메커니즘):

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

Bên tiêu thụ (consumer / 소비자):

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

Legacy ngữ cảnh (context / 맥락) khó refactor và có hành vi (behavior / 동작) dễ gây lỗi. React 16.3 giới thiệu new ngữ cảnh (context / 맥락) API:

```jsx
const ThemeContext =
  React.createContext("light");
```

Lớp (class / 클래스) bên tiêu thụ (consumer / 소비자):

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

Hàm (function / 함수) thành phần (component / 컴포넌트):

```jsx
const theme =
  useContext(ThemeContext);
```

Legacy `contextTypes`/`getChildContext` bị deprecate từ React 16.6 và remove trong React 19.

> **Nối mạch:** Provider scope quyết định state ownership và rerender fan-out; custom hooks tiếp theo đóng gói logic dùng lại mà vẫn tạo state riêng cho từng component instance.

## 11. Reducer + ngữ cảnh (context / 맥락)

Một mẫu (pattern / 패턴) client-state theo subtree:

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

Mẫu (pattern / 패턴) này tốt khi phạm vi (scope / 범위) rõ. Nếu trạng thái (state / 상태) lớn, cập nhật (update / 업데이트) liên tục và nhiều bên tiêu thụ (consumer / 소비자) cần selector, bên ngoài (external / 외부) store có thể phù hợp hơn.

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, **12. Custom Hooks** nối từ **11. Reducer + ngữ cảnh (context / 맥락)** sang **12A. HOC và kết xuất (render / 렌더링) Props: mẫu (pattern / 패턴) tái sử dụng lô-gic (logic / 논리) trước Custom Hooks**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Custom Hooks

Custom Hook là hàm (function / 함수) bắt đầu bằng `use` và có thể gọi Hook khác. Nó tái sử dụng stateful lô-gic (logic / 논리) chứ không chia sẻ cùng trạng thái (state / 상태) instance.

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

Mỗi caller có trạng thái (state / 상태) riêng. Nếu cần một store chia sẻ thật, phải dùng ngữ cảnh (context / 맥락)/bên ngoài (external / 외부) store hoặc nguồn dữ liệu chung.

API Hook nên rõ đầu vào (input / 입력)/đầu ra (output / 출력):

```jsx
const { data, error, status, refetch } = useUser(userId);
```

Đừng expose quá nhiều setter nội bộ nếu cần giữ bất biến (invariant / 불변식).

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **12A. HOC và kết xuất (render / 렌더링) Props: mẫu (pattern / 패턴) tái sử dụng lô-gic (logic / 논리) trước Custom Hooks** nối từ **12. Custom Hooks** sang **12B. Custom Hook đặc tả hợp đồng (contract / 계약): đầu vào (input / 입력), đầu ra (output / 출력), quyền sở hữu (ownership / 소유권) và tác động (effect / 효과) ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12A. HOC và kết xuất (render / 렌더링) Props: mẫu (pattern / 패턴) tái sử dụng lô-gic (logic / 논리) trước Custom Hooks

Trước Hooks, hai mẫu (pattern / 패턴) rất phổ biến để tái sử dụng stateful lô-gic (logic / 논리) là Higher-Order thành phần (component / 컴포넌트) và kết xuất (render / 렌더링) Props.

### Higher-Order thành phần (component / 컴포넌트)

HOC là hàm (function / 함수) nhận thành phần (component / 컴포넌트) và trả thành phần (component / 컴포넌트) mới:

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

HOC từng rất phổ biến trong Redux, routing và analytics. Nhược điểm thường gặp là wrapper hell, prop collision và phụ thuộc (dependency / 의존성) khó truy vết.

### Render Props
Phần này nối mạch bài học với “Render Props”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Thành phần (component / 컴포넌트) sở hữu lô-gic (logic / 논리) nhưng giao quyền kết xuất (render / 렌더링) cho bên tiêu thụ (consumer / 소비자) qua hàm (function / 함수) prop.

### Custom Hook thay đổi điều gì?
Phần này nối mạch bài học với “Custom Hook thay đổi điều gì?”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Custom Hook tái sử dụng stateful lô-gic (logic / 논리) mà không tạo thêm wrapper thành phần (component / 컴포넌트). Tuy nhiên HOC/kết xuất (render / 렌더링) props không phải API bị remove; chúng vẫn hợp lệ khi thư viện (library / 라이브러리)/API phù hợp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **12A. HOC và kết xuất (render / 렌더링) Props: mẫu (pattern / 패턴) tái sử dụng lô-gic (logic / 논리) trước Custom Hooks** đặt tiêu chí; **12B. Custom Hook đặc tả hợp đồng (contract / 계약): đầu vào (input / 입력), đầu ra (output / 출력), quyền sở hữu (ownership / 소유권) và tác động (effect / 효과) ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **13. useMemo, useCallback, memo** mở rộng hệ quả.

## 12B. Custom Hook đặc tả hợp đồng (contract / 계약): đầu vào (input / 입력), đầu ra (output / 출력), quyền sở hữu (ownership / 소유권) và tác động (effect / 효과) ranh giới (boundary / 경계)

Một Custom Hook tốt không chỉ gom vài Hook calls vào một hàm (function / 함수). Nó phải có đặc tả hợp đồng (contract / 계약) rõ: đầu vào (input / 입력) reactive nào điều khiển hành vi (behavior / 동작), đầu ra (output / 출력) nào là dữ liệu (data / 데이터) hay command, ai sở hữu trạng thái (state / 상태), và side tác động (effect / 효과) nằm ở đâu. Tên `use...` nói rằng hàm (function / 함수) tham gia React Hook mô hình (model / 모델); nó không đảm bảo lớp trừu tượng (abstraction / 추상화) tốt.

Nếu Hook trả một đối tượng (object / 객체) mới với nhiều callback mỗi kết xuất (render / 렌더링), bên tiêu thụ (consumer / 소비자) dùng memoization có thể bị vô hiệu hóa (invalidation / 무효화) liên tục. Nếu Hook giấu mạng (network / 네트워크) mutation, caller cần biết pending/lỗi (error / 오류)/cancellation ngữ nghĩa (semantics / 의미론). Nếu Hook chỉ bọc một dòng `useState`, lớp trừu tượng (abstraction / 추상화) có thể không mang thêm lĩnh vực (domain / 도메인) meaning.

Khi đọc mã (code / 코드) cũ, HOC và kết xuất (render / 렌더링) props thường giải quyết cùng bài toán tái sử dụng stateful lô-gic (logic / 논리). di chuyển (migration / 마이그레이션) sang Hook nên giữ nguyên đặc tả hợp đồng (contract / 계약) nghiệp vụ trước, sau đó mới giảm wrapper hoặc prop injection; không cần rewrite HOC ổn định chỉ để “trông hiện đại”.

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, **12B. Custom Hook đặc tả hợp đồng (contract / 계약): đầu vào (input / 입력), đầu ra (output / 출력), quyền sở hữu (ownership / 소유권) và tác động (effect / 효과) ranh giới (boundary / 경계)** đặt tiêu chí; **13. useMemo, useCallback, memo** dùng tiêu chí đó để kiểm tra ranh giới, rồi **14. useId** mở rộng hệ quả.

## 13. `useMemo`, `useCallback`, `memo`

`useMemo` memoize giá trị (value / 값):

```jsx
const visibleItems = useMemo(
  () => filterItems(items, filter),
  [items, filter]
);
```

`useCallback` memoize hàm (function / 함수) định danh (identity / 식별자):

```jsx
const handleSelect = useCallback(id => {
  setSelectedId(id);
}, []);
```

`memo` cho thành phần (component / 컴포넌트) có thể skip kết xuất (render / 렌더링) khi props được xem là không đổi:

```jsx
const Row = memo(function Row({ item, onSelect }) {
  return <button onClick={() => onSelect(item.id)}>{item.name}</button>;
});
```

Không memo hóa theo nghi thức. Memoization làm mã (code / 코드) phức tạp hơn và có chi phí. Profile trước. React trình biên dịch (compiler / 컴파일러) stable càng làm manual memoization ít cần hơn trong mã (code / 코드) mới, nhưng manual API vẫn có vai trò escape hatch.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — React trình biên dịch (compiler / 컴파일러) thay đổi “best practice” memoization
>
> `memo`, `useMemo` và `useCallback` tồn tại từ trước React 19. Tuy nhiên **React trình biên dịch (compiler / 컴파일러) 1.0** đã stable và có thể tự động memoize nhiều thành phần (component / 컴포넌트)/giá trị (value / 값). Vì vậy với codebase có trình biên dịch (compiler / 컴파일러), “bọc mọi thứ bằng `useMemo`/`useCallback`” càng không phải best practice. Vẫn phải hiểu ba API này để đọc mã (code / 코드) cũ, viết thư viện (library / 라이브러리), xử lý định danh (identity / 식별자) đặc tả hợp đồng (contract / 계약) và tối ưu bottleneck đã profile.

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **14. useId** nối từ **13. useMemo, useCallback, memo** sang **15. useLayoutEffect**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. `useId`

`useId` tạo ID ổn định phù hợp khả năng tiếp cận (accessibility / 접근성) và hydration:

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

Không dùng `useId` làm danh sách (list / 목록) key. Key phải đến từ dữ liệu (data / 데이터) định danh (identity / 식별자).

> ### phiên bản (version / 버전) ghi chú (note / 노트) — `useId` là API React 18
>
> `useId` được thêm ở React 18 để tạo ID ổn định giữa máy khách (client / 클라이언트)/máy chủ (server / 서버), đặc biệt hữu ích cho khả năng tiếp cận (accessibility / 접근성) và streaming SSR. Nếu dự án (project / 프로젝트) React 17 trở xuống, Hook này không tồn tại. Dù ở phiên bản (version / 버전) nào, `useId` **không dùng để tạo `key` cho danh sách (list / 목록)**; key phải đến từ định danh (identity / 식별자) của dữ liệu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **15. useLayoutEffect** nối từ **14. useId** sang **16. Portals**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. `useLayoutEffect`

`useLayoutEffect` chạy ở timing cho phép đo bố cục (layout / 레이아웃) và cập nhật trước paint thích hợp:

```jsx
useLayoutEffect(() => {
  const rect = ref.current.getBoundingClientRect();
  setHeight(rect.height);
}, []);
```

Chỉ dùng khi thật sự cần đo lường (measurement / 측정) hoặc tránh visual flicker. Nó có thể khối (block / 블록) paint; `useEffect` vẫn là mặc định.

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, **16. Portals** nối từ **15. useLayoutEffect** sang **17. lỗi (error / 오류) ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Portals
Phần này nối mạch bài học với “16. Portals”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
import { createPortal } from "react-dom";

function Modal({ children }) {
  return createPortal(
    <div className="modal">{children}</div>,
    document.body
  );
}
```

Portal kết xuất (render / 렌더링) host DOM ở nơi khác nhưng vẫn thuộc React cây (tree / 트리). sự kiện (event / 이벤트) bubble theo React cây (tree / 트리). Phù hợp modal, tooltip, popover, overlay.

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **16. Portals** đặt tiêu chí; **17. lỗi (error / 오류) ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **18. lazy và Suspense cơ bản** mở rộng hệ quả.

## 17. lỗi (error / 오류) ranh giới (boundary / 경계)

Lỗi (error / 오류) ranh giới (boundary / 경계) bắt kết xuất (render / 렌더링)/vòng đời (lifecycle / 생명주기) lỗi (error / 오류) trong subtree và hiển thị fallback. cốt lõi (core / 핵심) React vẫn dùng lớp (class / 클래스) cho lỗi (error / 오류) ranh giới (boundary / 경계) truyền thống:

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

Lỗi (error / 오류) ranh giới (boundary / 경계) không thay `try/catch` cho sự kiện (event / 이벤트) handler hoặc async thao tác (operation / 연산) tự gọi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **17. lỗi (error / 오류) ranh giới (boundary / 경계)** đặt tiêu chí; **18. lazy và Suspense cơ bản** dùng tiêu chí đó để kiểm tra ranh giới, rồi **19. dữ liệu (data / 데이터) fetching phía máy khách (client / 클라이언트)** mở rộng hệ quả.

## 18. `lazy` và Suspense cơ bản
Phần này nối mạch bài học với “18. `lazy` và Suspense cơ bản”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

`lazy` thường cần mô-đun (module / 모듈) default export thành phần (component / 컴포넌트). Suspense không phải wrapper tùy ý cho mọi Promise; dữ liệu (data / 데이터) nguồn (source / 소스)/khung phần mềm (framework / 프레임워크) phải tích hợp với cơ chế suspend.

> ### phiên bản (version / 버전) ghi chú (note / 노트) — Suspense đã tiến hóa qua nhiều phiên bản (version / 버전)
>
> `React.lazy` và Suspense cho mã (code / 코드) splitting xuất hiện từ React 16.6, nhưng Suspense cho máy chủ (server / 서버) rendering/tính đồng thời (concurrency / 동시성) được mở rộng mạnh ở React 18 và tiếp tục phát triển ở React 19. Vì vậy khi đọc blog cũ, đừng suy ra rằng mọi ví dụ Suspense đều hỗ trợ dữ liệu (data / 데이터) fetching giống nhau. dữ liệu (data / 데이터) nguồn (source / 소스) phải tích hợp Suspense hoặc đi qua khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) hỗ trợ.

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, **18. lazy và Suspense cơ bản** đặt vấn đề; **19. dữ liệu (data / 데이터) fetching phía máy khách (client / 클라이언트)** đối chiếu bằng chứng, rồi **19A. dữ liệu (data / 데이터) fetching evolution: vòng đời (lifecycle / 생명주기) → tác động (effect / 효과) → dữ liệu (data / 데이터) tầng (layer / 계층) → Suspense/RSC** mở rộng hệ quả hoặc giới hạn liên quan.

## 19. dữ liệu (data / 데이터) fetching phía máy khách (client / 클라이언트)

Fetch trong tác động (effect / 효과) hữu ích để học nhưng server-state môi trường vận hành (production / 운영 환경) thường cần nhiều hơn: bộ nhớ đệm (cache / 캐시), dedupe, stale thời gian (time / 시간), thử lại (retry / 재시도), mutation, vô hiệu hóa (invalidation / 무효화), pagination, optimistic cập nhật (update / 업데이트).

Một hiện thực (implementation / 구현) thủ công tối thiểu:

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

Máy chủ (server / 서버) trạng thái (state / 상태) có đơn vị sở hữu (owner / 오너) nằm ngoài máy khách (client / 클라이언트) và có thể stale; máy khách (client / 클라이언트) UI trạng thái (state / 상태) như modal open lại thuộc app hiện tại. Không trộn tùy tiện hai loại này.

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **19. dữ liệu (data / 데이터) fetching phía máy khách (client / 클라이언트)** đặt vấn đề; **19A. dữ liệu (data / 데이터) fetching evolution: vòng đời (lifecycle / 생명주기) → tác động (effect / 효과) → dữ liệu (data / 데이터) tầng (layer / 계층) → Suspense/RSC** đối chiếu bằng chứng, rồi **20. Router và URL trạng thái (state / 상태)** mở rộng hệ quả hoặc giới hạn liên quan.

## 19A. dữ liệu (data / 데이터) fetching evolution: vòng đời (lifecycle / 생명주기) → tác động (effect / 효과) → dữ liệu (data / 데이터) tầng (layer / 계층) → Suspense/RSC

Lớp (class / 클래스) mã (code / 코드) cũ thường fetch ở `componentDidMount`/`componentDidUpdate`; Hooks chuyển synchronization tương tự sang `useEffect`. Fetch tác động (effect / 효과) thủ công vẫn phải tự xử lý cancellation, race, bộ nhớ đệm (cache / 캐시), thử lại (retry / 재시도), dedupe và vô hiệu hóa (invalidation / 무효화), nên môi trường vận hành (production / 운영 환경) thường chuyển máy chủ (server / 서버) trạng thái (state / 상태) sang truy vấn (query / 쿼리)/khung phần mềm (framework / 프레임워크) dữ liệu (data / 데이터) tầng (layer / 계층). Suspense/RSC lại thay nơi yêu cầu (request / 요청) bắt đầu và cách loading được reveal; Suspense không tự biến mọi `fetch()` thành bộ nhớ đệm (cache / 캐시).

Old vòng đời (lifecycle / 생명주기) fetch vẫn gặp nhiều trong React 15–17 và không cần rewrite chỉ vì dùng lớp (class / 클래스). Migrate khi quyền sở hữu (ownership / 소유권), cancellation, bộ nhớ đệm (cache / 캐시) hoặc routing kiến trúc (architecture / 아키텍처) thực sự tốt hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **19A. dữ liệu (data / 데이터) fetching evolution: vòng đời (lifecycle / 생명주기) → tác động (effect / 효과) → dữ liệu (data / 데이터) tầng (layer / 계층) → Suspense/RSC** đặt vấn đề; **20. Router và URL trạng thái (state / 상태)** đối chiếu bằng chứng, rồi **21. Form thực tế** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. Router và URL trạng thái (state / 상태)

Routing không thuộc React cốt lõi (core / 핵심). React Router phổ biến trong SPA; khung phần mềm (framework / 프레임워크) như Next.js có router riêng.

Tìm kiếm (search / 검색) truy vấn (query / 쿼리), page, sort, filter và tab có ý nghĩa điều hướng thường nên nằm ở URL:

```text
/products?q=keyboard&page=2&sort=price
```

Nếu reload/back/forward phải khôi phục cùng màn hình, URL thường là nguồn chuẩn (source of truth / 정본) tốt hơn cục bộ (local / 로컬) trạng thái (state / 상태).

Học router theo đúng major phiên bản (version / 버전) vì API có thể thay đổi giữa các phiên bản (version / 버전).

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, **21. Form thực tế** nối từ **20. Router và URL trạng thái (state / 상태)** sang **21A. Forms qua các thế hệ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Form thực tế

Không phải đầu vào (input / 입력) nào cũng cần controlled trạng thái (state / 상태). Có thể dùng `FormData`:

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

Trình duyệt (browser / 브라우저) kiểm tra hợp lệ (validation / 검증) dùng `required`, `minLength`, `pattern`, `type="email"`. kiểm tra hợp lệ (validation / 검증) nghiệp vụ phức tạp có thể dùng lược đồ (schema / 스키마) validator/form thư viện (library / 라이브러리). máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) cải thiện UX; máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증) mới bảo vệ integrity/bảo mật (security / 보안).

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **21A. Forms qua các thế hệ** nối từ **21. Form thực tế** sang **22. khả năng tiếp cận (accessibility / 접근성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21A. Forms qua các thế hệ

Controlled form có từ thời lớp (class / 클래스): trường dữ liệu (field / 필드) nằm trong `this.state`; Hooks chuyển API sang `useState`/reducer nhưng source-of-truth mô hình (model / 모델) không đổi. môi trường vận hành (production / 운영 환경) form không nhất thiết controlled mọi trường dữ liệu (field / 필드): `FormData`, bản địa (native / 네이티브) kiểm tra hợp lệ (validation / 검증) hoặc trường dữ liệu (field / 필드) subscription có thể giảm coupling. React 19 Actions/`useActionState`/`useFormStatus`/`useOptimistic` thêm async mutation workflow nhưng không xóa controlled/uncontrolled fundamentals.

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **22. khả năng tiếp cận (accessibility / 접근성)** nối từ **21A. Forms qua các thế hệ** sang **23. Testing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. khả năng tiếp cận (accessibility / 접근성)

React không tự làm UI accessible. ngữ nghĩa (semantic / 의미적) HTML là nền tảng.

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

Modal cần accessible name, focus management, escape hành vi (behavior / 동작) và restore focus. ARIA không thay ngữ nghĩa (semantic / 의미적) HTML.

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, **23. Testing** nối từ **22. khả năng tiếp cận (accessibility / 접근성)** sang **24. Cấu trúc dự án (project / 프로젝트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Testing

Kiểm thử (test / 테스트) React nên ưu tiên hành vi người dùng hơn hiện thực (implementation / 구현) detail.

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

Đơn vị (unit / 단위) kiểm thử (test / 테스트) phù hợp reducer/formatter. thành phần (component / 컴포넌트)/kiểm thử tích hợp (integration test / 통합 테스트) kiểm tra UI phối hợp. E2E kiểm tra trọng yếu (critical / 중요) luồng (flow / 흐름) bằng trình duyệt (browser / 브라우저) thật. Coverage 100% không phải mục tiêu nếu kiểm thử (test / 테스트) không mang confidence.

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **24. Cấu trúc dự án (project / 프로젝트)** nối từ **23. Testing** sang **25. Kiến trúc feature điển hình**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Cấu trúc dự án (project / 프로젝트)

Không có folder cấu trúc (structure / 구조) React duy nhất. Với app vừa/lớn, feature-first thường quy mô (scale / 규모) tốt:

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

Không đưa mã (code / 코드) vào `shared` quá sớm. Generalize sau khi nhu cầu tái sử dụng thật sự xuất hiện.

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **25. Kiến trúc feature điển hình** nối từ **24. Cấu trúc dự án (project / 프로젝트)** sang **25A. trạng thái (state / 상태) management bắt đầu từ quyền sở hữu (ownership / 소유권)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Kiến trúc feature điển hình
Phần này nối mạch bài học với “25. Kiến trúc feature điển hình”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
UI component
   ↓
feature hook / controller hook
   ↓
server-state library / API client
   ↓
HTTP API
```

Trạng thái (state / 상태) nên ở gần nơi dùng. URL trạng thái (state / 상태) ở URL. máy chủ (server / 서버) dữ liệu (data / 데이터) ở server-state bộ nhớ đệm (cache / 캐시). Form trạng thái (state / 상태) ở form. Truly toàn cục (global / 전역) máy khách (client / 클라이언트) trạng thái (state / 상태) chỉ đưa vào store/ngữ cảnh (context / 맥락) khi thực sự toàn cục (global / 전역).

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, sau nội dung của **25. Kiến trúc feature điển hình**, **25A. trạng thái (state / 상태) management bắt đầu từ quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **26. Anti-pattern thường gặp** mở rộng hệ quả hoặc giới hạn liên quan.

## 25A. trạng thái (state / 상태) management bắt đầu từ quyền sở hữu (ownership / 소유권)

Trước khi chọn ngữ cảnh (context / 맥락), Redux hay Zustand, hãy phân loại: cục bộ (local / 로컬) UI trạng thái (state / 상태) ở thành phần (component / 컴포넌트); form trạng thái (state / 상태) ở form; filter/page shareable ở URL; máy chủ (server / 서버) dữ liệu (data / 데이터) ở truy vấn (query / 쿼리)/khung phần mềm (framework / 프레임워크) bộ nhớ đệm (cache / 캐시); cross-feature máy khách (client / 클라이언트) trạng thái (state / 상태) mới là ứng viên bên ngoài (external / 외부) store. Redux/Flux đời cũ thường chứa mọi loại trạng thái (state / 상태) vì ecosystem thiếu specialized layers. Old Redux vẫn hợp lý khi lĩnh vực (domain / 도메인) cần selector, middleware, devtools hoặc toàn cục (global / 전역) sự kiện (event / 이벤트) luồng (flow / 흐름); không migrate chỉ vì thư viện (library / 라이브러리) mới ngắn hơn.

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **26. Anti-pattern thường gặp** nối từ **25A. trạng thái (state / 상태) management bắt đầu từ quyền sở hữu (ownership / 소유권)** sang **27. Checklist Intermediate**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Anti-pattern thường gặp

**tác động (effect / 효과) chuỗi (chain / 사슬):** tác động (effect / 효과) A set trạng thái (state / 상태) làm tác động (effect / 효과) B chạy rồi tác động (effect / 효과) C chạy. Thường có thể tính trong kết xuất (render / 렌더링) hoặc xử lý chuyển tiếp (transition / 전이) trong sự kiện (event / 이벤트)/reducer.

**God thành phần (component / 컴포넌트):** vừa fetch, validate, transform, kết xuất (render / 렌더링), điều khiển nhiều modal. Tách theo responsibility, không theo số dòng máy móc.

**Premature ngữ cảnh (context / 맥락):** đưa trạng thái (state / 상태) lên provider dù chỉ hai thành phần (component / 컴포넌트) gần nhau dùng.

**Manual memo everywhere:** làm phụ thuộc (dependency / 의존성) phức tạp và khó maintain.

**bản sao (copy / 복사) props into trạng thái (state / 상태):**

```jsx
const [name, setName] = useState(props.name);
```

Nếu muốn luôn phản ánh prop, đây là lỗi. Chỉ bản sao (copy / 복사) khi cố ý tạo cục bộ (local / 로컬) draft có vòng đời (lifecycle / 생명주기) reset rõ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **React Master ghi chú (note / 노트) — Intermediate**, **27. Checklist Intermediate** nối từ **26. Anti-pattern thường gặp** sang **Phiên bản (version / 버전) checkpoint trước khi sang Advanced**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Checklist Intermediate

Bạn nên giải thích được tác động (effect / 효과) là synchronization chứ không phải vòng đời (lifecycle / 생명주기) callback chung; hiểu stale closure; phân biệt ref và trạng thái (state / 상태); biết reducer phù hợp ở đâu; hiểu ngữ cảnh (context / 맥락) không đồng nghĩa toàn cục (global / 전역) store; viết custom Hook có đặc tả hợp đồng (contract / 계약) rõ; hiểu manual memoization chỉ có lý do khi có hiệu năng (performance / 성능)/định danh (identity / 식별자) yêu cầu (requirement / 요구사항); phân biệt máy chủ (server / 서버) trạng thái (state / 상태) với máy khách (client / 클라이언트) trạng thái (state / 상태); xây form/routing/data-fetching luồng (flow / 흐름) có loading/lỗi (error / 오류)/cancellation; và viết kiểm thử (test / 테스트) theo hành vi người dùng (user / 사용자).

> **Nối mạch:** Trong **React Master ghi chú (note / 노트) — Intermediate**, **Phiên bản (version / 버전) checkpoint trước khi sang Advanced** nối từ **27. Checklist Intermediate** sang **Cấp cao (senior / 시니어) ghi chú (note / 노트) chuyển tiếp**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phiên bản (version / 버전) checkpoint trước khi sang Advanced

Đến đây, phiên bản (version / 버전) nên được hiểu theo “khả năng nào có sẵn” chứ không phải học lại React từ đầu cho từng bản phát hành (release / 릴리스). Nếu dự án (project / 프로젝트) là React 18, bạn vẫn dùng hầu hết tư duy của tệp (file / 파일) này nhưng chưa có ref-as-prop React 19, ngữ cảnh (context / 맥락) provider shorthand và các hành động (action / 동작) APIs mới. Nếu là React 19.0/19.1, bạn có nền Actions/`use` nhưng chưa có các API được thêm ở 19.2 như `useEffectEvent`/`Activity`, và chưa có stable View Transitions/Fragment refs của 19.3.

Khi bản sao (copy / 복사) mã (code / 코드) từ tài liệu hiện hành, luôn kiểm tra API đó thuộc `react`, `react-dom`, React máy chủ (server / 서버) Components hay khung phần mềm (framework / 프레임워크). Đây là kỹ năng versioning quan trọng hơn việc thuộc bảng changelog.

> **Nối mạch:** Ở chặng này của **React Master ghi chú (note / 노트) — Intermediate**, **Cấp cao (senior / 시니어) ghi chú (note / 노트) chuyển tiếp** nối từ **Phiên bản (version / 버전) checkpoint trước khi sang Advanced** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Cấp cao (senior / 시니어) ghi chú (note / 노트) chuyển tiếp

Khi ứng dụng có Suspense, chuyển tiếp (transition / 전이), streaming, Actions hoặc máy chủ (server / 서버) Components, mô hình tư duy (mental model / 사고 모델) “mount/cập nhật (update / 업데이트)/unmount” kiểu lớp (class / 클래스) cũ không còn đủ. mức (level / 수준) Advanced/cấp cao (senior / 시니어) sẽ tập trung vào kết xuất (render / 렌더링)/lần ghi nhận (commit / 커밋), tính đồng thời (concurrency / 동시성), quyền sở hữu (ownership / 소유권), boundaries và kiến trúc vận hành (production architecture / 운영 아키텍처).

> **Bàn giao:** Sau **Cấp cao (senior / 시니어) ghi chú (note / 노트) chuyển tiếp**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
