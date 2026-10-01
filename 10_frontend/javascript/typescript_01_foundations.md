# TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. TypeScript giải quyết vấn đề nào?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Compile-time và thời gian chạy (runtime / 런타임) là hai thế giới nối nhau bằng đặc tả hợp đồng (contract / 계약)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> chuẩn gốc (canonical / 정본) điều hướng (navigation / 내비게이션): [TypeScript Index](typescript_00_index.md) → Foundations → [Type System Internals](typescript_02_type_system.md) → [Compiler & Tooling](typescript_03_tooling_modules_runtime.md) → [Senior Production](typescript_04_senior_production.md).

## 1. TypeScript giải quyết vấn đề nào?

JavaScript quyết định phần lớn lỗi theo thời gian chạy (runtime / 런타임). Nếu một hàm (function / 함수) mong nhận đối tượng (object / 객체) có `email` nhưng caller truyền đối tượng (object / 객체) khác shape, chương trình có thể chỉ phát hiện khi branch đó thật sự chạy. Với dự án (project / 프로젝트) nhỏ, nhà phát triển (developer / 개발자) có thể giữ đặc tả hợp đồng (contract / 계약) trong đầu. Với dự án (project / 프로젝트) lớn, đặc tả hợp đồng (contract / 계약) bị phân tán qua mô-đun (module / 모듈), API, thành phần (component / 컴포넌트), kiểm thử (test / 테스트) và nhiều người cùng sửa; chi phí lập luận (reasoning / 추론) tăng nhanh hơn số dòng mã (code / 코드).

TypeScript thêm một lớp mô hình tĩnh để trình biên dịch (compiler / 컴파일러) có thể hỏi trước khi chạy: expression này có thể tạo ra những giá trị (value / 값) nào, thuộc tính (property / 속성) này có chắc tồn tại không, hàm (function / 함수) này có thể return `undefined` không, caller có đang đưa đúng đặc tả hợp đồng (contract / 계약) không? Giá trị lớn nhất không phải “viết thêm `: string`”, mà là biến implicit các giả định (assumptions / 가정들) thành thứ toolchain có thể kiểm tra và refactor cùng bạn.

Điểm quan trọng nhất: TypeScript **không thay đổi bản chất thời gian chạy (runtime / 런타임) của JavaScript**. Ví dụ:

```ts
type User = {
  id: string;
  name: string;
};

function greet(user: User) {
  return `Hello ${user.name}`;
}
```

Sau khi compile, `type User` không trở thành một thời gian chạy (runtime / 런타임) lớp (class / 클래스) hay kiểm tra hợp lệ (validation / 검증) hàm (function / 함수). thời gian chạy (runtime / 런타임) vẫn xử lý JavaScript đối tượng (object / 객체). Đây là **xóa kiểu (type erasure / 타입 소거)**. Vì thế một assertion như sau không kiểm tra gì ở thời gian chạy (runtime / 런타임):

```ts
const data = JSON.parse(raw) as User;
```

Nếu `raw` thiếu `name`, trình biên dịch (compiler / 컴파일러) vẫn tin assertion của bạn. Bạn đã tự cung cấp “bằng chứng” mà không kiểm chứng nó.

> **Chuyển mạch:** TypeScript giải quyết feedback tại compile-time; phần tiếp theo đặt compile-time và runtime cạnh nhau để xác định contract nào còn phải validate khi chạy. Annotation/inference sau đó chọn mức explicitness phù hợp.

## 2. Compile-time và thời gian chạy (runtime / 런타임) là hai thế giới nối nhau bằng đặc tả hợp đồng (contract / 계약)

Hãy dùng mô hình tư duy (mental model / 사고 모델) hai tầng:

```text
source .ts
  ↓
TypeScript parser + binder + checker
  ↓ diagnostics / inferred types
emit hoặc noEmit
  ↓
JavaScript + runtime environment
```

Trình biên dịch (compiler / 컴파일러) nhìn nguồn (source / 소스) và declaration files. thời gian chạy (runtime / 런타임) nhìn values thật. Một HTTP phản hồi (response / 응답), row cơ sở dữ liệu (database / 데이터베이스) hay message từ bản địa (native / 네이티브) cầu nối (bridge / 브리지) không tự nhiên đáng tin chỉ vì variable phía TypeScript được annotation đẹp.

Ví dụ môi trường vận hành (production / 운영 환경):

```ts
interface ProfileResponse {
  userId: string;
  age: number;
}

async function loadProfile(): Promise<ProfileResponse> {
  const response = await fetch("/api/profile");
  return response.json();
}
```

Signature trên chỉ mô tả điều nhà phát triển (developer / 개발자) mong muốn. `response.json()` có thể trả bất kỳ JSON giá trị (value / 값) nào. cấp cao (senior / 시니어) mã (code / 코드) cần tách `unknown external data` khỏi `validated domain data`; phần này sẽ được làm đầy đủ ở chapter cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경).

> **Chuyển mạch:** Compile/runtime contract xác định chỗ cần validation; annotation và inference chọn bằng chứng tĩnh tối thiểu. Literal/widening tiếp theo cho thấy inference giữ hoặc làm mất specificity ở đâu.

## 3. Annotation và suy luận (inference / 추론): đừng annotate mọi thứ

TypeScript có **suy luận kiểu (type inference / 타입 추론)**. Với:

```ts
const retryCount = 3;
const endpoint = "/api/users";
const enabled = true;
```

Trình biên dịch (compiler / 컴파일러) đã biết kiểu (type / 타입) cần thiết. Annotation lặp lại như `const retryCount: number = 3` thường không thêm thông tin.

Annotation có giá trị khi nó đặt đặc tả hợp đồng (contract / 계약) tại ranh giới (boundary / 경계):

```ts
function calculateTotal(price: number, quantity: number): number {
  return price * quantity;
}
```

Hoặc khi muốn chống accidental widening hay xác nhận một công khai (public / 공개) shape. Quy tắc thực dụng là: **để suy luận (inference / 추론) làm việc bên trong hiện thực (implementation / 구현), viết đặc tả hợp đồng (contract / 계약) rõ ở công khai (public / 공개)/mô-đun (module / 모듈) boundaries**.

> **Chuyển mạch:** Inference giảm annotation noise; literal widening và `as const` tiếp theo kiểm soát độ rộng của type trước khi phân biệt primitive với boxed object.

## 4. Literal kiểu (type / 타입), widening và `as const`

TypeScript phân biệt `string` với literal kiểu (type / 타입) như `"idle"`. Với mutable binding, trình biên dịch (compiler / 컴파일러) thường widen:

```ts
let status = "idle"; // string
status = "running";
```

Với `const`, trình biên dịch (compiler / 컴파일러) có thể giữ literal hẹp hơn vì binding không được reassign:

```ts
const status = "idle"; // "idle"
```

Đối tượng (object / 객체) vẫn mutable nên thuộc tính (property / 속성) thường widen:

```ts
const request = {
  method: "GET"
};
// request.method thường là string
```

Khi muốn giữ literal cấu trúc (structure / 구조) sâu hơn:

```ts
const request = {
  method: "GET",
  retry: 2
} as const;
```

`as const` làm các literal được giữ hẹp và properties/tuple trở nên readonly ở kiểu (type / 타입) mức (level / 수준). Nó không `Object.freeze()` thời gian chạy (runtime / 런타임) đối tượng (object / 객체); đây tiếp tục là kiểu (type / 타입)/thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계).

> **Chuyển mạch:** Trong **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **5. thành phần nguyên thủy (primitive / 기본 요소), đối tượng (object / 객체) và sự khác biệt giữa string với String** tiếp nhận điểm tựa từ **4. Literal kiểu (type / 타입), widening và as const** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. any, unknown, never: ba kiểu (type / 타입) dễ dùng sai nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. thành phần nguyên thủy (primitive / 기본 요소), đối tượng (object / 객체) và sự khác biệt giữa `string` với `String`

Trong TypeScript mã (code / 코드) hiện đại, dùng thành phần nguyên thủy (primitive / 기본 요소) types `string`, `number`, `boolean`, `bigint`, `symbol`. Các wrapper đối tượng (object / 객체) types `String`, `Number`, `Boolean` đại diện cho boxed objects và gần như không phải thứ bạn muốn cho đặc tả ứng dụng (application contract / 애플리케이션 계약).

```ts
function normalize(value: string) {
  return value.trim().toLowerCase();
}
```

Đừng nhầm `object` với “đối tượng (object / 객체) có thuộc tính (property / 속성) nào đó”. `object` chỉ loại thành phần nguyên thủy (primitive / 기본 요소) ra. `{}` lại mang ngữ nghĩa (semantics / 의미론) khác và quá rộng cho nhiều use trường hợp (case / 사례). Khi chưa biết shape bên ngoài (external / 외부) dữ liệu (data / 데이터), `unknown` thường đúng hơn.

> **Chuyển mạch:** Ở chặng này của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **6. any, unknown, never: ba kiểu (type / 타입) dễ dùng sai nhất** tiếp nhận điểm tựa từ **5. thành phần nguyên thủy (primitive / 기본 요소), đối tượng (object / 객체) và sự khác biệt giữa string với String** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Union kiểu (type / 타입) và narrowing bằng điều khiển (control / 제어) luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. `any`, `unknown`, `never`: ba kiểu (type / 타입) dễ dùng sai nhất

`any` nói với checker: “đừng kiểm tra nữa”. Nó lan truyền rất nhanh:

```ts
let payload: any = getSomething();
payload.user.profile.name.toUpperCase(); // compiler im lặng
```

`unknown` nói: “có giá trị (value / 값), nhưng chưa có bằng chứng về shape”. Bạn buộc phải narrow trước:

```ts
function printLength(value: unknown) {
  if (typeof value === "string") {
    console.log(value.length);
  }
}
```

`never` đại diện cho tập giá trị (value / 값) rỗng: branch không thể xảy ra nếu mô hình (model / 모델) đúng, hoặc hàm (function / 함수) không hoàn tất bình thường.

```ts
function fail(message: string): never {
  throw new Error(message);
}
```

`never` đặc biệt hữu ích cho exhaustive checking của discriminated union.

Mô hình tư duy (mental model / 사고 모델):

```text
any     = tắt phần lớn bằng chứng
unknown = chưa biết, phải chứng minh
never   = không có value hợp lệ nào còn lại
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **6. any, unknown, never: ba kiểu (type / 타입) dễ dùng sai nhất** xác định đầu vào; **7. Union kiểu (type / 타입) và narrowing bằng điều khiển (control / 제어) luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **8. Discriminated union: mô hình (model / 모델) trạng thái (state / 상태) thay vì ghép boolean** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Union kiểu (type / 타입) và narrowing bằng điều khiển (control / 제어) luồng (flow / 흐름)

Union `A | B` nghĩa giá trị (value / 값) có thể thuộc một trong nhiều possibility. Bạn chỉ được dùng thao tác (operation / 연산) an toàn cho mọi possibility cho tới khi có bằng chứng (evidence / 증거).

```ts
function normalizeId(id: string | number) {
  if (typeof id === "number") {
    return id.toString();
  }

  return id.trim();
}
```

Checker theo dõi điều khiển (control / 제어) luồng (flow / 흐름), assignment, `typeof`, equality, `in`, `instanceof`, truthiness và user-defined kiểu (type / 타입) predicates để thu hẹp kiểu.

Một lỗi lập luận (reasoning / 추론) phổ biến là narrow xong rồi gọi callback có thể chạy sau, trong khi mutable trạng thái (state / 상태) đã thay đổi. Hãy nhớ narrowing là proof gắn với control-flow các giả định (assumptions / 가정들) của trình biên dịch (compiler / 컴파일러); async/callback boundaries và mutation có thể khiến proof không còn mạnh như bạn tưởng. Cách tốt thường là capture giá trị (value / 값) đã được validate vào immutable cục bộ (local / 로컬) binding.

> **Chuyển mạch:** Trong **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **7. Union kiểu (type / 타입) và narrowing bằng điều khiển (control / 제어) luồng (flow / 흐름)** xác định đầu vào; **8. Discriminated union: mô hình (model / 모델) trạng thái (state / 상태) thay vì ghép boolean** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **9. Intersection kiểu (type / 타입) không phải đối tượng (object / 객체) spread** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Discriminated union: mô hình (model / 모델) trạng thái (state / 상태) thay vì ghép boolean

Giả sử yêu cầu (request / 요청) trạng thái (state / 상태) dùng ba trường dữ liệu (field / 필드):

```ts
type BadState = {
  loading: boolean;
  data?: User[];
  error?: Error;
};
```

Shape này cho phép những combination vô lý như `loading: true` đồng thời có cả `data` và `error`.

Mô hình (model / 모델) tốt hơn:

```ts
type RequestState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: User[] }
  | { status: "error"; error: Error };
```

`status` là discriminant. Khi kiểm tra `status`, trình biên dịch (compiler / 컴파일러) narrow toàn đối tượng (object / 객체). Đây không chỉ là “kiểu (type / 타입) trick”; nó biến bất biến (invariant / 불변식) nghiệp vụ (business / 비즈니스) thành cấu trúc mà trình biên dịch (compiler / 컴파일러) giữ giúp bạn.

```ts
function renderState(state: RequestState) {
  switch (state.status) {
    case "idle":
      return "Idle";
    case "loading":
      return "Loading";
    case "success":
      return `${state.data.length} users`;
    case "error":
      return state.error.message;
    default: {
      const impossible: never = state;
      return impossible;
    }
  }
}
```

Nếu thêm trạng thái (state / 상태) mới mà quên xử lý, `never` biến omission thành diagnostic.

> **Chuyển mạch:** Ở chặng này của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **9. Intersection kiểu (type / 타입) không phải đối tượng (object / 객체) spread** tiếp nhận điểm tựa từ **8. Discriminated union: mô hình (model / 모델) trạng thái (state / 상태) thay vì ghép boolean** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. interface và type: chọn theo ngữ nghĩa (semantics / 의미론), không theo giáo điều** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Intersection kiểu (type / 타입) không phải đối tượng (object / 객체) spread

`A & B` yêu cầu một giá trị (value / 값) thỏa cả A và B. Nó không đồng nghĩa thời gian chạy (runtime / 런타임) merge hai objects.

```ts
type Timestamped = { createdAt: Date };
type Entity = { id: string };

type PersistedEntity = Entity & Timestamped;
```

Nếu hai kiểu (type / 타입) có thuộc tính (property / 속성) cùng tên nhưng incompatible, intersection có thể tạo thuộc tính (property / 속성) thành `never` hoặc kiểu (type / 타입) rất khó dùng. Đây là dấu hiệu mô hình (model / 모델) đang mâu thuẫn, không phải trình biên dịch (compiler / 컴파일러) “ngu”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **10. interface và type: chọn theo ngữ nghĩa (semantics / 의미론), không theo giáo điều** tiếp nhận điểm tựa từ **9. Intersection kiểu (type / 타입) không phải đối tượng (object / 객체) spread** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Optional thuộc tính (property / 속성) và undefined không hoàn toàn giống nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. `interface` và `type`: chọn theo ngữ nghĩa (semantics / 의미론), không theo giáo điều

Cả hai đều mô tả đối tượng (object / 객체) shape tốt trong phần lớn trường hợp.

```ts
interface User {
  id: string;
  name: string;
}

type UserId = string;
type LoadState = "idle" | "loading" | "done";
```

`interface` có declaration merging và phù hợp công khai (public / 공개) extensible đối tượng (object / 객체) contracts trong một số thư viện (library / 라이브러리) mẫu (pattern / 패턴). `type` diễn đạt union, intersection, thành phần nguyên thủy (primitive / 기본 요소) alias, tuple và kiểu (type / 타입) transformations linh hoạt hơn. Đừng biến lựa chọn này thành style war; hãy chọn cấu trúc phản ánh intent và tránh accidental merging ở ứng dụng (application / 애플리케이션) mã (code / 코드) nếu bạn không cần nó.

> **Chuyển mạch:** Trong **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **11. Optional thuộc tính (property / 속성) và undefined không hoàn toàn giống nhau** tiếp nhận điểm tựa từ **10. interface và type: chọn theo ngữ nghĩa (semantics / 의미론), không theo giáo điều** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. readonly là compile-time restriction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Optional thuộc tính (property / 속성) và `undefined` không hoàn toàn giống nhau

```ts
type A = { value?: string };
type B = { value: string | undefined };
```

A cho phép thuộc tính (property / 속성) không tồn tại. B yêu cầu thuộc tính (property / 속성) tồn tại nhưng giá trị (value / 값) có thể là `undefined`. Sự khác biệt quan trọng khi serialize, spread, check `"value" in obj`, patch DTO và khi bật `exactOptionalPropertyTypes`.

Với strict modeling, đừng dùng optional chỉ để “cho trình biên dịch (compiler / 컴파일러) im”. Hỏi lĩnh vực (domain / 도메인) thật: trường dữ liệu (field / 필드) có thể absent hay luôn present nhưng unknown/empty?

> **Chuyển mạch:** Ở chặng này của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **12. readonly là compile-time restriction** tiếp nhận điểm tựa từ **11. Optional thuộc tính (property / 속성) và undefined không hoàn toàn giống nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. hàm (function / 함수) types, optional parameter và callback đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. `readonly` là compile-time restriction

```ts
type Config = {
  readonly apiUrl: string;
};
```

`readonly` ngăn một số assignment qua kiểu (type / 타입) surface đó, nhưng không biến đối tượng (object / 객체) thành immutable thời gian chạy (runtime / 런타임) đối tượng (object / 객체). Nếu cùng đối tượng (object / 객체) được tham chiếu qua kiểu (type / 타입) mutable khác, thời gian chạy (runtime / 런타임) vẫn có thể thay đổi. Đây là ví dụ khác về việc static mô hình (model / 모델) không tự tạo thời gian chạy (runtime / 런타임) guarantee.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **13. hàm (function / 함수) types, optional parameter và callback đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **12. readonly là compile-time restriction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. kiểu (type / 타입) assertion và non-null assertion là lời hứa của nhà phát triển (developer / 개발자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. hàm (function / 함수) types, optional parameter và callback đặc tả hợp đồng (contract / 계약)

```ts
type Formatter = (value: number, locale?: string) => string;
```

Hàm (function / 함수) kiểu (type / 타입) là đặc tả hợp đồng (contract / 계약) về parameter và return. Callback assignability có các quy tắc (rule / 규칙) riêng để phù hợp JavaScript ecosystem; khi `strictFunctionTypes` hoạt động, hàm (function / 함수) parameter variance được kiểm tra chặt hơn ở nhiều ngữ cảnh (context / 맥락). Chi tiết variance nằm ở chapter 02.

Một anti-pattern là khai báo return kiểu (type / 타입) quá rộng:

```ts
function findUser(id: string): User | null | undefined {
  // ...
}
```

Nếu lĩnh vực (domain / 도메인) thực chỉ có “found hoặc not found”, chọn một biểu diễn (representation / 표현) duy nhất. kiểu (type / 타입) càng rộng, mọi caller càng phải carry ambiguity.

> **Chuyển mạch:** Trong **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **14. kiểu (type / 타입) assertion và non-null assertion là lời hứa của nhà phát triển (developer / 개발자)** tiếp nhận điểm tựa từ **13. hàm (function / 함수) types, optional parameter và callback đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. satisfies: kiểm tra shape mà vẫn giữ suy luận (inference / 추론) hữu ích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. kiểu (type / 타입) assertion và non-null assertion là lời hứa của nhà phát triển (developer / 개발자)

```ts
const input = document.querySelector("#name") as HTMLInputElement;
const token = maybeToken!;
```

Assertion không thêm thời gian chạy (runtime / 런타임) check. `!` cũng không làm giá trị (value / 값) bớt `null`. Nó chỉ nói checker tin bạn. Dùng assertion hợp lý khi bạn có bằng chứng (evidence / 증거) trình biên dịch (compiler / 컴파일러) không biểu diễn được, nhưng mỗi assertion nên được nhìn như một **proof obligation**: bằng chứng (evidence / 증거) nằm ở đâu? kiểm thử (test / 테스트) nào giữ bất biến (invariant / 불변식)? thời gian chạy (runtime / 런타임) nào có thể phá giả định (assumption / 가정)?

Khi assertion xuất hiện hàng loạt, thường mô hình (model / 모델) hoặc ranh giới (boundary / 경계) kiểm tra hợp lệ (validation / 검증) đang yếu.

> **Chuyển mạch:** Ở chặng này của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **15. satisfies: kiểm tra shape mà vẫn giữ suy luận (inference / 추론) hữu ích** tiếp nhận điểm tựa từ **14. kiểu (type / 타입) assertion và non-null assertion là lời hứa của nhà phát triển (developer / 개발자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Excess thuộc tính (property / 속성) checking và “tại sao cùng đối tượng (object / 객체) mà lúc lỗi, lúc không?”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. `satisfies`: kiểm tra shape mà vẫn giữ suy luận (inference / 추론) hữu ích

Giả sử muốn cấu hình (config / 설정) phải khớp một đặc tả hợp đồng (contract / 계약) nhưng vẫn giữ literal keys/giá trị (value / 값) để dùng tiếp:

```ts
type RouteConfig = Record<string, {
  method: "GET" | "POST";
  secure: boolean;
}>;

const routes = {
  users: { method: "GET", secure: true },
  login: { method: "POST", secure: false }
} satisfies RouteConfig;
```

`satisfies` kiểm tra expression có assignable tới mục tiêu (target / 대상) kiểu (type / 타입) hay không nhưng không ép variable nhận chính mục tiêu (target / 대상) kiểu (type / 타입) như annotation thường làm. Đây là công cụ rất mạnh cho cấu hình (config / 설정) maps, tuyến (route / 경로) tables và siêu dữ liệu (metadata / 메타데이터) khi bạn muốn kiểm tra hợp lệ (validation / 검증) + rich suy luận (inference / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **16. Excess thuộc tính (property / 속성) checking và “tại sao cùng đối tượng (object / 객체) mà lúc lỗi, lúc không?”** tiếp nhận điểm tựa từ **15. satisfies: kiểm tra shape mà vẫn giữ suy luận (inference / 추론) hữu ích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Strict chế độ (mode / 모드) là baseline lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Excess thuộc tính (property / 속성) checking và “tại sao cùng đối tượng (object / 객체) mà lúc lỗi, lúc không?”

TypeScript có kiểm tra đặc biệt với đối tượng (object / 객체) literal ở một số ngữ cảnh (context / 맥락):

```ts
type User = { id: string };

const direct: User = {
  id: "u1",
  name: "Kim" // diagnostic
};
```

Nhưng nếu đối tượng (object / 객체) đi qua variable trước, structural assignability có thể chấp nhận extra fields:

```ts
const source = { id: "u1", name: "Kim" };
const user: User = source; // thường hợp lệ
```

Đây không phải inconsistency ngẫu nhiên. Fresh đối tượng (object / 객체) literal được kiểm tra excess thuộc tính (property / 속성) để bắt typo/cấu hình (config / 설정) mistake, trong khi structural typing nói đối tượng (object / 객체) có thể có nhiều năng lực (capability / 역량) hơn mục tiêu (target / 대상) yêu cầu. Hiểu hai quy tắc (rule / 규칙) này giúp tránh “fix” bằng `as User` chỉ để tắt lỗi.

> **Chuyển mạch:** Trong **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **17. Strict chế độ (mode / 모드) là baseline lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **16. Excess thuộc tính (property / 속성) checking và “tại sao cùng đối tượng (object / 객체) mà lúc lỗi, lúc không?”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Debugging một kiểu (type / 타입) lỗi (error / 오류) theo tầng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Strict chế độ (mode / 모드) là baseline lập luận (reasoning / 추론)

Dự án (project / 프로젝트) hiện đại nên coi strict checking là baseline. `strictNullChecks` buộc `null`/`undefined` trở thành phần tường minh (explicit / 명시적) của mô hình (model / 모델). Các strict-family flags giúp trình biên dịch (compiler / 컴파일러) giữ bất biến (invariant / 불변식) thay vì cho implicit `any` hoặc unsafe truy cập (access / 접근) lọt qua.

TypeScript 6.0/7.0 còn đi xa hơn về default strictness và hiện đại (modern / 현대적) mô-đun (module / 모듈) các giả định (assumptions / 가정들). Tuy nhiên dự án (project / 프로젝트) upgrade phải đọc bản phát hành (release / 릴리스) notes và cấu hình (config / 설정) hiện hữu, vì đổi trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전) có thể thay diagnostic mà không đổi thời gian chạy (runtime / 런타임) mã (code / 코드).

> **Chuyển mạch:** Ở chặng này của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **18. Debugging một kiểu (type / 타입) lỗi (error / 오류) theo tầng** tiếp nhận điểm tựa từ **17. Strict chế độ (mode / 모드) là baseline lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. thất bại (failure / 실패) modes cần nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Debugging một kiểu (type / 타입) lỗi (error / 오류) theo tầng

Khi gặp diagnostic dài, đừng đọc từ câu cuối rồi cast. Hãy dấu vết (trace / 추적):

```text
1. Value/runtime intent thật là gì?
2. Type hiện tại được infer từ đâu?
3. Target contract yêu cầu gì?
4. Union/generic nào đã mở rộng hoặc mất thông tin?
5. Diagnostic đầu tiên nơi information bị mất là đâu?
```

Ví dụ một React prop lỗi (error / 오류) có thể bắt nguồn từ API DTO typed `any` quá sớm; một mô-đun (module / 모듈) kiểu (type / 타입) lỗi (error / 오류) có thể đến từ wrong resolution chế độ (mode / 모드) chứ không phải giao diện (interface / 인터페이스). Chapter sau sẽ đào sâu assignability và generic suy luận (inference / 추론) để dấu vết (trace / 추적) các lỗi (error / 오류) kiểu này có hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 01 — Foundations & thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계)**, **19. thất bại (failure / 실패) modes cần nhớ** tiếp nhận điểm tựa từ **18. Debugging một kiểu (type / 타입) lỗi (error / 오류) theo tầng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 19. thất bại (failure / 실패) modes cần nhớ

TypeScript không cứu được bạn khỏi lô-gic (logic / 논리) sai nhưng type-correct, race điều kiện (condition / 조건), stale bộ nhớ đệm (cache / 캐시), SQL bug, authorization bug hay malformed bên ngoài (external / 외부) dữ liệu (data / 데이터) nếu bạn tự cast. Nó cũng không làm đối tượng (object / 객체) immutable thời gian chạy (runtime / 런타임) chỉ vì `readonly`, không làm array bounds-safe mặc định, và không biến `private` kiểu (type / 타입) ngữ nghĩa (semantics / 의미론) thành ranh giới bảo mật (security boundary / 보안 경계).

Giá trị của TypeScript xuất hiện mạnh nhất khi mô hình (model / 모델) phản ánh bất biến (invariant / 불변식) thật và escape hatch được giữ ở ranh giới (boundary / 경계) nhỏ, có bằng chứng (evidence / 증거) rõ.

---

Tiếp theo: [TypeScript 02 — Type System Internals & Generic Modeling](typescript_02_type_system.md).

> **Bàn giao:** Sau **19. thất bại (failure / 실패) modes cần nhớ**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
