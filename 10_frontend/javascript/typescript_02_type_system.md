# TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Structural typing: compatible vì shape, không phải vì tên** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Assignability là câu hỏi trung tâm của checker** để mở câu hỏi trung tâm cho phần kế tiếp. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> Prerequisite: [Foundations & Runtime Boundary](typescript_01_foundations.md). Chapter này tập trung vào cách checker lập luận (reasoning / 추론), không phải sưu tầm kiểu (type / 타입) trick.

## 1. Structural typing: compatible vì shape, không phải vì tên

Trong nominal hệ kiểu (type system / 타입 시스템), hai lớp (class / 클래스)/kiểu (type / 타입) có thể khác nhau chỉ vì chúng mang định danh (identity / 식별자) khác. TypeScript chủ yếu dùng **kiểu cấu trúc (structural typing / 구조적 타이핑)** để phù hợp JavaScript ecosystem: nếu nguồn (source / 소스) có đủ năng lực (capability / 역량) mục tiêu (target / 대상) yêu cầu, assignment thường hợp lệ.

```ts
type Point = {
  x: number;
  y: number;
};

const pixel = {
  x: 10,
  y: 20,
  color: "red"
};

const point: Point = pixel;
```

`pixel` không cần `implements Point`; shape đủ là được. Điều này làm composition tự nhiên và thư viện (library / 라이브러리) interoperability tốt, nhưng cũng có nghĩa kiểu (type / 타입) name không tự tạo lĩnh vực (domain / 도메인) định danh (identity / 식별자).

Ví dụ `UserId` và `OrderId` cùng là `string` sẽ assign được cho nhau nếu chỉ alias:

```ts
type UserId = string;
type OrderId = string;
```

Khi lĩnh vực (domain / 도메인) cần phân biệt định danh (identity / 식별자), có thể dùng branded/opaque-like mẫu (pattern / 패턴):

```ts
declare const userIdBrand: unique symbol;

type UserId = string & {
  readonly [userIdBrand]: "UserId";
};
```

Đây là compile-time modeling, không tự thêm thời gian chạy (runtime / 런타임) tag. ranh giới (boundary / 경계) tạo `UserId` vẫn phải validate string format nếu format có bất biến (invariant / 불변식).

> **Chuyển mạch:** Structural typing xác định compatibility theo shape; assignability mô tả checker dùng shape đó để quyết định nhận/gán. Generic tiếp theo giữ quan hệ giữa input/output thay vì hạ mọi thứ xuống `any`.

## 2. Assignability là câu hỏi trung tâm của checker

Nhiều diagnostic thực chất hỏi: kiểu ở mã nguồn (source type / 소스 타입) có **assignable** tới mục tiêu (target / 대상) kiểu (type / 타입) không? Với đối tượng (object / 객체), checker xét required properties, thuộc tính (property / 속성) types, readonly/optional rules, chỉ mục (index / 인덱스) signatures, lời gọi (call / 호출) signatures và generic relationships.

Khi lỗi (error / 오류) quá dài, giảm nó thành nguồn (source / 소스) → mục tiêu (target / 대상):

```text
Source<TActual>
     ↓ assignable?
Target<TExpected>
```

Sau đó tìm thuộc tính (property / 속성)/kiểu (type / 타입) parameter đầu tiên làm quan hệ vỡ. Đây hiệu quả hơn đọc hàng chục dòng nested diagnostic như prose.

> **Chuyển mạch:** Assignability xác định checker có thể truyền type nào qua boundary; generic giữ quan hệ giữa các type parameter. Constraints tiếp theo giới hạn capability mà abstraction được phép yêu cầu.

## 3. Generic không phải “any có kiểu (type / 타입) đẹp hơn”

Generic dùng khi nhiều đầu vào (input / 입력)/đầu ra (output / 출력) có quan hệ mà bạn muốn giữ.

```ts
function identity<T>(value: T): T {
  return value;
}

const a = identity("hello"); // string
const b = identity(42);      // number
```

Nếu viết:

```ts
function badIdentity(value: any): any {
  return value;
}
```

relationship giữa đầu vào (input / 입력) và đầu ra (output / 출력) bị mất. Generic giữ thông tin (information / 정보) xuyên qua lớp trừu tượng (abstraction / 추상화).

Một generic có ý nghĩa khi kiểu (type / 타입) parameter xuất hiện ở quan hệ thực. hàm (function / 함수) dưới đây không cần generic:

```ts
function logValue<T>(value: T): void {
  console.log(value);
}
```

Nếu `T` không giúp caller hay hiện thực (implementation / 구현) duy trì quan hệ (relation / 관계) nào, `unknown` có thể rõ hơn:

```ts
function logValue(value: unknown): void {
  console.log(value);
}
```

> **Chuyển mạch:** Generic giữ quan hệ giữa input/output, không phải `any`; constraint tiếp theo giới hạn capability và giúp inference lấy bằng chứng an toàn hơn.

## 4. ràng buộc (constraint / 제약조건): lớp trừu tượng (abstraction / 추상화) vẫn cần năng lực (capability / 역량)

Generic `T` có thể quá rộng để dùng thuộc tính (property / 속성) cụ thể:

```ts
function getLength<T>(value: T) {
  // value.length không chắc tồn tại
}
```

Ràng buộc (constraint / 제약조건) nói mọi T hợp lệ phải có năng lực (capability / 역량) nào:

```ts
function getLength<T extends { length: number }>(value: T): number {
  return value.length;
}
```

`extends` ở đây không có nghĩa lớp (class / 클래스) inheritance thời gian chạy (runtime / 런타임). Nó đặt quan hệ (relation / 관계) ở hệ kiểu (type system / 타입 시스템).

Một mẫu (pattern / 패턴) thường gặp:

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

`K` không phải string tùy ý; nó bị ràng buộc (constraint / 제약조건) bởi key không gian (space / 공간) của T. Return kiểu (type / 타입) giữ chính xác kiểu (type / 타입) của thuộc tính (property / 속성) được chọn.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **4. ràng buộc (constraint / 제약조건): lớp trừu tượng (abstraction / 추상화) vẫn cần năng lực (capability / 역량)** nêu điều cần giải thích; **5. Generic suy luận (inference / 추론) lấy bằng chứng (evidence / 증거) từ nhiều phía** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. Variance: vì sao callback kiểu (type / 타입) có thể nguy hiểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Generic suy luận (inference / 추론) lấy bằng chứng (evidence / 증거) từ nhiều phía

TypeScript suy kiểu (type / 타입) argument từ actual arguments, contextual mục tiêu (target / 대상) và các ràng buộc (constraints / 제약조건들). Khi suy luận (inference / 추론) thất bại, đừng lập tức viết tường minh (explicit / 명시적) `<SomeType>`; hãy hỏi thông tin (information / 정보) bị mất ở ranh giới (boundary / 경계) nào.

```ts
function pair<T>(left: T, right: T): [T, T] {
  return [left, right];
}
```

Nếu two arguments không thể tìm dùng chung (common / 공통) suy luận (inference / 추론) phù hợp, diagnostic cho thấy lớp trừu tượng (abstraction / 추상화) đang nói “hai giá trị cùng T” trong khi lĩnh vực (domain / 도메인) có thể cần hai kiểu (type / 타입) parameters:

```ts
function pair<A, B>(left: A, right: B): [A, B] {
  return [left, right];
}
```

Đừng nới generic chỉ để trình biên dịch (compiler / 컴파일러) im; sửa relationship cho đúng intent.

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **5. Generic suy luận (inference / 추론) lấy bằng chứng (evidence / 증거) từ nhiều phía** nêu điều cần giải thích; **6. Variance: vì sao callback kiểu (type / 타입) có thể nguy hiểm** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. keyof, indexed truy cập (access / 접근) và typeof là cầu nối cấu trúc (structure / 구조) → kiểu (type / 타입)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Variance: vì sao callback kiểu (type / 타입) có thể nguy hiểm

Giả sử `Dog` assignable tới `Animal`. Câu hỏi `Box<Dog>` có assignable tới `Box<Animal>` không phụ thuộc `Box` dùng T như thế nào.

Nếu T chỉ đi ra:

```ts
type Producer<T> = () => T;
```

Producer thường có xu hướng covariance: producer Dog có thể dùng nơi cần producer Animal.

Nếu T chỉ đi vào:

```ts
type Consumer<T> = (value: T) => void;
```

Quan hệ (relation / 관계) đi chiều khác vì một bên tiêu thụ (consumer / 소비자) chỉ biết xử lý Dog không an toàn ở nơi hệ thống có thể đưa bất kỳ Animal nào.

Nếu T vừa vào vừa ra, bộ chứa (container / 컨테이너) thường cần invariant-like lập luận (reasoning / 추론) hơn.

Array là ví dụ JavaScript thực dụng khiến variance có trường hợp biên (edge case / 경계 사례). Mutable collection có ghi (write / 쓰기) operations, nên quan hệ (relation / 관계) subtype trực giác có thể dẫn tới unsafe mutation nếu hệ thống (system / 시스템) quá permissive. `readonly` collection giảm ghi (write / 쓰기) năng lực (capability / 역량) và làm quan hệ (relation / 관계) dễ lập luận (reasoning / 추론) hơn.

Cấp cao (senior / 시니어) lesson: variance không phải từ học thuật để nhớ. Nó trả lời “generic lớp trừu tượng (abstraction / 추상화) này cho phép dữ liệu (data / 데이터) chảy vào hay ra theo hướng nào?”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **7. keyof, indexed truy cập (access / 접근) và typeof là cầu nối cấu trúc (structure / 구조) → kiểu (type / 타입)** tiếp nhận điểm tựa từ **6. Variance: vì sao callback kiểu (type / 타입) có thể nguy hiểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Mapped kiểu (type / 타입): transform từng thuộc tính (property / 속성) theo key không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. `keyof`, indexed truy cập (access / 접근) và `typeof` là cầu nối cấu trúc (structure / 구조) → kiểu (type / 타입)

`keyof` biến đối tượng (object / 객체) kiểu (type / 타입) thành union keys:

```ts
type User = {
  id: string;
  age: number;
};

type UserKey = keyof User; // "id" | "age"
```

Indexed truy cập (access / 접근) lấy thuộc tính (property / 속성) kiểu (type / 타입):

```ts
type Id = User["id"]; // string
```

`typeof` trong kiểu (type / 타입) position lấy static kiểu (type / 타입) của giá trị (value / 값) binding:

```ts
const config = {
  retry: 3,
  mode: "safe"
} as const;

type Config = typeof config;
```

Đây là mẫu (pattern / 패턴) tốt khi thời gian chạy (runtime / 런타임) cấu hình (config / 설정) là nguồn chuẩn (source of truth / 정본) và bạn muốn derive kiểu (type / 타입) từ nó, thay vì maintain hai definitions dễ drift.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **8. Mapped kiểu (type / 타입): transform từng thuộc tính (property / 속성) theo key không gian (space / 공간)** tiếp nhận điểm tựa từ **7. keyof, indexed truy cập (access / 접근) và typeof là cầu nối cấu trúc (structure / 구조) → kiểu (type / 타입)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Conditional kiểu (type / 타입): branch ở tầng kiểu (type / 타입)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Mapped kiểu (type / 타입): transform từng thuộc tính (property / 속성) theo key không gian (space / 공간)

Mapped kiểu (type / 타입) giống một phép biến đổi trên keys:

```ts
type Optional<T> = {
  [K in keyof T]?: T[K];
};
```

Mô hình tư duy (mental model / 사고 모델):

```text
key space của T
  ↓ iterate K
property mới cho từng K
  ↓
shape transformed
```

Built-in utilities như `Partial<T>`, `Required<T>`, `Readonly<T>` dựa trên cơ chế này. Học hiện thực (implementation / 구현) conceptually giúp bạn tự thiết kế transformation nhưng không nên bản sao (copy / 복사) kiểu (type / 타입) gymnastics nếu utility chuẩn đã diễn đạt intent.

Key remapping cho phép đổi/lọc key:

```ts
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
```

Khi mapped kiểu (type / 타입) trở nên khó đọc hơn nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) nó mô tả, hãy cân nhắc tường minh (explicit / 명시적) giao diện (interface / 인터페이스). Type-level lớp trừu tượng (abstraction / 추상화) cũng có maintenance chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **9. Conditional kiểu (type / 타입): branch ở tầng kiểu (type / 타입)** tiếp nhận điểm tựa từ **8. Mapped kiểu (type / 타입): transform từng thuộc tính (property / 속성) theo key không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. infer: đặt tên phần cấu trúc đang match** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Conditional kiểu (type / 타입): branch ở tầng kiểu (type / 타입)

```ts
type ElementType<T> = T extends readonly (infer U)[] ? U : T;
```

Conditional kiểu (type / 타입) hỏi quan hệ (relation / 관계) assignability và chọn branch. Với naked kiểu (type / 타입) parameter, nó có thể **phân phối (distribute)** qua union:

```ts
type ToArray<T> = T extends unknown ? T[] : never;
type Result = ToArray<string | number>;
// string[] | number[]
```

Nếu muốn đánh giá union như một khối, wrap hai phía:

```ts
type ToArrayNonDistributed<T> = [T] extends [unknown] ? T[] : never;
```

Phân phối (distribution / 분포) là nguồn của cả sức mạnh lẫn diagnostic độ phức tạp (complexity / 복잡도). Khi conditional kiểu (type / 타입) lồng sâu, luôn tự hỏi đầu vào (input / 입력) lĩnh vực (domain / 도메인) có thật sự cần type-level branching đó không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **10. infer: đặt tên phần cấu trúc đang match** tiếp nhận điểm tựa từ **9. Conditional kiểu (type / 타입): branch ở tầng kiểu (type / 타입)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Template literal kiểu (type / 타입): string mẫu (pattern / 패턴) ở kiểu (type / 타입) mức (level / 수준)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. `infer`: đặt tên phần cấu trúc đang match

`infer` chỉ xuất hiện trong conditional kiểu (type / 타입) matching ngữ cảnh (context / 맥락). Nó không “đoán mọi thứ”; nó capture một phần của cấu trúc (structure / 구조) nếu quan hệ (relation / 관계) match.

```ts
type Return<T> = T extends (...args: any[]) => infer R ? R : never;
```

Với Promise-like:

```ts
type UnwrapPromise<T> = T extends Promise<infer U> ? U : T;
```

Khi nested promise/thenable ngữ nghĩa (semantics / 의미론) phức tạp, built-in `Awaited<T>` thường đúng hơn custom utility vì nó mô hình (model / 모델) edge cases chuẩn hơn.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **11. Template literal kiểu (type / 타입): string mẫu (pattern / 패턴) ở kiểu (type / 타입) mức (level / 수준)** tiếp nhận điểm tựa từ **10. infer: đặt tên phần cấu trúc đang match** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Recursive kiểu (type / 타입) và giới hạn trình biên dịch (compiler / 컴파일러)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Template literal kiểu (type / 타입): string mẫu (pattern / 패턴) ở kiểu (type / 타입) mức (level / 수준)

```ts
type EventName = "created" | "updated";
type HandlerName = `on${Capitalize<EventName>}`;
// "onCreated" | "onUpdated"
```

Tính năng (feature / 기능) này hữu ích khi thời gian chạy (runtime / 런타임) API thật sự có naming convention ổn định. Nhưng nếu bạn tạo union hàng nghìn combination, trình biên dịch (compiler / 컴파일러) phải materialize/compare nhiều kiểu (type / 타입) hơn. Dùng template literal types để encode giao thức (protocol / 프로토콜) nhỏ, không để tạo “kiểu (type / 타입) programming ngôn ngữ (language / 언어)” vô hạn.

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **11. Template literal kiểu (type / 타입): string mẫu (pattern / 패턴) ở kiểu (type / 타입) mức (level / 수준)** đã nêu tiêu chí phân biệt, còn **12. Recursive kiểu (type / 타입) và giới hạn trình biên dịch (compiler / 컴파일러)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. Utility types nên hiểu từ thành phần nguyên thủy (primitive / 기본 요소) thao tác (operation / 연산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Recursive kiểu (type / 타입) và giới hạn trình biên dịch (compiler / 컴파일러)

Kiểu (type / 타입) có thể tham chiếu cấu trúc lặp:

```ts
type Json =
  | null
  | boolean
  | number
  | string
  | Json[]
  | { [key: string]: Json };
```

Recursive conditional/mapped types mạnh hơn nhưng có thể chạm instantiation độ sâu (depth / 깊이), tăng bộ nhớ (memory / 메모리)/check thời gian (time / 시간) hoặc tạo diagnostic rất khó đọc. Đây là nơi hiệu năng (performance / 성능) pressure thay đổi thiết kế (design / 설계): kiểu (type / 타입) chính xác hơn một chút chưa chắc đáng đổi bản dựng (build / 빌드) độ trễ (latency / 지연 시간) và cognitive tải (load / 로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **12. Recursive kiểu (type / 타입) và giới hạn trình biên dịch (compiler / 컴파일러)** đã nêu tiêu chí phân biệt, còn **13. Utility types nên hiểu từ thành phần nguyên thủy (primitive / 기본 요소) thao tác (operation / 연산)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. never trong conditional kiểu (type / 타입) và union filtering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Utility types nên hiểu từ thành phần nguyên thủy (primitive / 기본 요소) thao tác (operation / 연산)

`Pick<T, K>` giữ subset keys. `Omit<T, K>` loại keys. `Record<K, V>` tạo map shape. `Exclude<A, B>` loại union members assignable tới B. `Extract<A, B>` giữ phần assignable. `Parameters<F>` và `ReturnType<F>` phân tích hàm (function / 함수) signature. `Awaited<T>` unwrap async/thenable ngữ nghĩa (semantics / 의미론).

Không học utilities như flashcard. Hãy hỏi utility đang thao tác trên key không gian (space / 공간), union không gian (space / 공간) hay hàm (function / 함수) cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **14. never trong conditional kiểu (type / 타입) và union filtering** tiếp nhận điểm tựa từ **13. Utility types nên hiểu từ thành phần nguyên thủy (primitive / 기본 요소) thao tác (operation / 연산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. unknown trong generic ranh giới (boundary / 경계) tốt hơn any** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. `never` trong conditional kiểu (type / 타입) và union filtering

`never` biến mất khỏi union:

```ts
type OnlyString<T> = T extends string ? T : never;
type R = OnlyString<string | number | boolean>; // string
```

Đây là nền của nhiều filter utilities. Khi kết quả bất ngờ thành `never`, dấu vết (trace / 추적) từng branch: đầu vào (input / 입력) kiểu (type / 타입) đã bị ràng buộc (constraint / 제약조건) quá hẹp, thuộc tính (property / 속성) intersection mâu thuẫn, hay conditional đã distribute ngoài ý muốn?

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **14. never trong conditional kiểu (type / 타입) và union filtering** đã nêu tiêu chí phân biệt, còn **15. unknown trong generic ranh giới (boundary / 경계) tốt hơn any** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. hàm (function / 함수) overload và union/generic: chọn theo relationship** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. `unknown` trong generic ranh giới (boundary / 경계) tốt hơn `any`

Ví dụ parser generic thường bị viết sai:

```ts
function parse<T>(raw: string): T {
  return JSON.parse(raw);
}
```

Hàm (function / 함수) này hứa rằng caller chọn T nào cũng được và hiện thực (implementation / 구현) sẽ tạo đúng T, nhưng hiện thực (implementation / 구현) không có kiểm tra hợp lệ (validation / 검증). Generic đang tạo false proof.

API trung thực hơn:

```ts
function parse(raw: string): unknown {
  return JSON.parse(raw);
}
```

Sau đó validate/narrow ở ranh giới (boundary / 경계). Generic không nên được dùng để “teleport” bên ngoài (external / 외부) dữ liệu (data / 데이터) vào lĩnh vực (domain / 도메인) kiểu (type / 타입).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **15. unknown trong generic ranh giới (boundary / 경계) tốt hơn any** đã nêu tiêu chí phân biệt, còn **16. hàm (function / 함수) overload và union/generic: chọn theo relationship** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. Declaration merging và mô-đun (module / 모듈) augmentation: sức mạnh có toàn cục (global / 전역) chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. hàm (function / 함수) overload và union/generic: chọn theo relationship

Overload hữu ích khi API có vài lời gọi (call / 호출) shapes rời rạc với return quan hệ (relation / 관계) rõ:

```ts
function parseValue(value: string): number;
function parseValue(value: number): string;
function parseValue(value: string | number): string | number {
  return typeof value === "string" ? Number(value) : String(value);
}
```

Nếu lời gọi (call / 호출) shapes có một generic quan hệ (relation / 관계) liên tục, generic thường quy mô (scale / 규모) tốt hơn. Nếu chỉ cần “A hoặc B” mà đầu ra (output / 출력) không phụ thuộc đầu vào (input / 입력) member, union đơn giản hơn overload. Đừng chọn overload chỉ vì trông “cấp cao (senior / 시니어)”.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **17. Declaration merging và mô-đun (module / 모듈) augmentation: sức mạnh có toàn cục (global / 전역) chi phí (cost / 비용)** tiếp nhận điểm tựa từ **16. hàm (function / 함수) overload và union/generic: chọn theo relationship** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Exactness: TypeScript đối tượng (object / 객체) kiểu (type / 타입) thường là minimum requirements, không phải sealed đối tượng (object / 객체)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Declaration merging và mô-đun (module / 모듈) augmentation: sức mạnh có toàn cục (global / 전역) chi phí (cost / 비용)

`interface` có thể merge khi declarations cùng tên/phạm vi (scope / 범위):

```ts
interface Window {
  appVersion: string;
}
```

Mô-đun (module / 모듈) augmentation cho phép bổ sung kiểu (type / 타입) vào mô-đun (module / 모듈) bên ngoài. Đây hữu ích cho plugin ecosystem nhưng có thể làm đặc tả hợp đồng (contract / 계약) xuất hiện “từ xa”, khó dấu vết (trace / 추적). ứng dụng (application / 애플리케이션) mã (code / 코드) nên giữ augmentation tập trung, tên tệp (file / 파일) rõ, kiểm thử (test / 테스트) compile và tránh dùng nó thay cho tường minh (explicit / 명시적) adapter.

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **18. Exactness: TypeScript đối tượng (object / 객체) kiểu (type / 타입) thường là minimum requirements, không phải sealed đối tượng (object / 객체)** tiếp nhận điểm tựa từ **17. Declaration merging và mô-đun (module / 모듈) augmentation: sức mạnh có toàn cục (global / 전역) chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. noUncheckedIndexedAccess thay đổi mô hình tư duy (mental model / 사고 모델) của lookup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Exactness: TypeScript đối tượng (object / 객체) kiểu (type / 타입) thường là minimum requirements, không phải sealed đối tượng (object / 객체)

`type User = { id: string }` thường có nghĩa “ít nhất có id string” trong structural quan hệ (relation / 관계), không có nghĩa đối tượng (object / 객체) thời gian chạy (runtime / 런타임) chỉ được đúng một thuộc tính (property / 속성). Excess thuộc tính (property / 속성) checking trên fresh literal là diagnostic convenience, không biến đối tượng (object / 객체) kiểu (type / 타입) thành chính xác (exact / 정확한)/sealed bản ghi (record / 레코드).

Nếu giao thức (protocol / 프로토콜) cần reject extra properties, đó là thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증)/lược đồ (schema / 스키마) concern. Đừng kỳ vọng kiểu (type / 타입) alias thay parser.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **19. noUncheckedIndexedAccess thay đổi mô hình tư duy (mental model / 사고 모델) của lookup** gom các mảnh từ **18. Exactness: TypeScript đối tượng (object / 객체) kiểu (type / 타입) thường là minimum requirements, không phải sealed đối tượng (object / 객체)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **20. exactOptionalPropertyTypes làm optional gần ngữ nghĩa (semantics / 의미론) thời gian chạy (runtime / 런타임) hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. `noUncheckedIndexedAccess` thay đổi mô hình tư duy (mental model / 사고 모델) của lookup

Mặc định, indexed truy cập (access / 접근) vào `Record<string, User>` có thể cho cảm giác key luôn tồn tại. Khi bật `noUncheckedIndexedAccess`, lookup thường thêm `undefined`, phản ánh đúng hơn thời gian chạy (runtime / 런타임) map truy cập (access / 접근):

```ts
const user = usersById[id];
if (!user) {
  // handle missing
}
```

Strict flag này làm mã (code / 코드) verbose hơn nhưng buộc missing-key bất biến (invariant / 불변식) trở thành tường minh (explicit / 명시적). Với cấu trúc dữ liệu (data structure / 자료구조) thật sự total, hãy mô hình (model / 모델) key không gian (space / 공간) hữu hạn hoặc xây lớp trừu tượng (abstraction / 추상화) chứng minh bất biến (invariant / 불변식) thay vì cast sau mỗi lookup.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **20. exactOptionalPropertyTypes làm optional gần ngữ nghĩa (semantics / 의미론) thời gian chạy (runtime / 런타임) hơn** gom các mảnh từ **19. noUncheckedIndexedAccess thay đổi mô hình tư duy (mental model / 사고 모델) của lookup** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **21. kiểu (type / 타입) hiệu năng (performance / 성능): trình biên dịch (compiler / 컴파일러) cũng là một bên tiêu thụ (consumer / 소비자) của API thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. `exactOptionalPropertyTypes` làm optional gần ngữ nghĩa (semantics / 의미론) thời gian chạy (runtime / 런타임) hơn

Khi bật option này, `{ value?: string }` không còn tự động đồng nghĩa “giá trị (value / 값) có thể được gán undefined” theo cách rộng trước đây. Nó nhấn mạnh distinction giữa absent thuộc tính (property / 속성) và present-with-undefined, rất hữu ích cho PATCH payload, cấu hình (config / 설정) merge và serialization.

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **21. kiểu (type / 타입) hiệu năng (performance / 성능): trình biên dịch (compiler / 컴파일러) cũng là một bên tiêu thụ (consumer / 소비자) của API thiết kế (design / 설계)** tiếp nhận điểm tựa từ **20. exactOptionalPropertyTypes làm optional gần ngữ nghĩa (semantics / 의미론) thời gian chạy (runtime / 런타임) hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. API thiết kế (design / 설계): giữ generic ở ranh giới (boundary / 경계) nhỏ nhất có ích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. kiểu (type / 타입) hiệu năng (performance / 성능): trình biên dịch (compiler / 컴파일러) cũng là một bên tiêu thụ (consumer / 소비자) của API thiết kế (design / 설계)

Một kiểu (type / 타입) definition có thể correct nhưng đắt. Dấu hiệu: editor hover chậm, autocomplete delay, `tsc` check thời gian (time / 시간) tăng mạnh, diagnostic có kiểu (type / 타입) khổng lồ. Nguyên nhân thường gặp gồm giant unions, deeply recursive conditional types, distributive transformations trên union lớn, repeated anonymous intersections và generic APIs bắt checker suy luận quá nhiều đường dẫn (path / 경로).

Cấp cao (senior / 시니어) practice là profile trước khi tối ưu, rồi đơn giản hóa công khai (public / 공개) types, đặt alias cho intermediate kết quả (result / 결과), tránh union explosion, và đôi khi chấp nhận kiểu (type / 타입) ít “ma thuật” hơn để bản dựng (build / 빌드) predictable hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **21. kiểu (type / 타입) hiệu năng (performance / 성능): trình biên dịch (compiler / 컴파일러) cũng là một bên tiêu thụ (consumer / 소비자) của API thiết kế (design / 설계)** đã nêu tiêu chí phân biệt, còn **22. API thiết kế (design / 설계): giữ generic ở ranh giới (boundary / 경계) nhỏ nhất có ích** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **23. cấp cao (senior / 시니어) ghi chú (note / 노트): hệ kiểu (type system / 타입 시스템) là công cụ mô hình hóa bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. API thiết kế (design / 설계): giữ generic ở ranh giới (boundary / 경계) nhỏ nhất có ích

Kiểu (type / 타입) parameter quá nhiều làm caller phải giải puzzle. Một thư viện (library / 라이브러리) API tốt thường để caller truyền dữ liệu (data / 데이터) tự nhiên, suy luận (inference / 추론) lấy phần lớn thông tin, và chỉ expose tường minh (explicit / 명시적) generic khi thật sự cần điều khiển (control / 제어).

Ví dụ repository giao diện (interface / 인터페이스):

```ts
interface Repository<TEntity, TId> {
  getById(id: TId): Promise<TEntity | null>;
  save(entity: TEntity): Promise<void>;
}
```

Hai parameters có relationship rõ. Nếu thêm `TContext`, `TError`, `TOptions`, `TTransport`, `TMeta` chỉ để “future proof”, lớp trừu tượng (abstraction / 추상화) có thể đang vượt quá lĩnh vực (domain / 도메인) bằng chứng (evidence / 증거) hiện có.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **22. API thiết kế (design / 설계): giữ generic ở ranh giới (boundary / 경계) nhỏ nhất có ích** đã nêu tiêu chí phân biệt, còn **23. cấp cao (senior / 시니어) ghi chú (note / 노트): hệ kiểu (type system / 타입 시스템) là công cụ mô hình hóa bất biến (invariant / 불변식)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **24. Control-flow phân tích (analysis / 분석) là data-flow proof, không chỉ là typeof** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. cấp cao (senior / 시니어) ghi chú (note / 노트): hệ kiểu (type system / 타입 시스템) là công cụ mô hình hóa bất biến (invariant / 불변식)

Một advanced kiểu (type / 타입) chỉ có giá trị nếu nó làm illegal trạng thái (state / 상태) khó represent hơn, giữ relationship quan trọng qua lớp trừu tượng (abstraction / 추상화), hoặc giúp refactor an toàn. Nếu người đọc phải chạy mental trình biên dịch (compiler / 컴파일러) để hiểu nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙), bạn đã chuyển độ phức tạp (complexity / 복잡도) từ thời gian chạy (runtime / 런타임) sang nguồn (source / 소스) mà chưa chắc giảm tổng độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, biết phải giữ gì trong **23. cấp cao (senior / 시니어) ghi chú (note / 노트): hệ kiểu (type system / 타입 시스템) là công cụ mô hình hóa bất biến (invariant / 불변식)**, ta theo dõi trong **24. Control-flow phân tích (analysis / 분석) là data-flow proof, không chỉ là typeof** cách hệ thống thực hiện và phản hồi qua từng bước. Từ đây, **25. kiểu (type / 타입) predicate và assertion hàm (function / 함수): biến thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) thành proof có tên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Control-flow phân tích (analysis / 분석) là data-flow proof, không chỉ là `typeof`

Narrowing nên được hiểu như một bài toán luồng dữ liệu. Checker theo dõi những facts đã được chứng minh trên từng nhánh, assignment nào có thể làm fact mất hiệu lực và điểm merge điều khiển (control / 제어) luồng (flow / 흐름) nơi nhiều possibility phải hợp lại.

```ts
function format(value: string | null) {
  if (value === null) {
    return "-";
  }

  // Ở đây checker biết value là string vì nhánh null đã return.
  return value.trim();
}
```

Đây là **reachability phân tích (analysis / 분석)**: trình biên dịch (compiler / 컴파일러) không chỉ nhìn điều kiện (condition / 조건) mà còn biết branch nào không thể tiếp tục. Early return vì thế vừa làm mã (code / 코드) thời gian chạy (runtime / 런타임) dễ đọc, vừa làm proof static đơn giản hơn.

Assignment có thể thay đổi proof:

```ts
let value: string | number = "10";

if (typeof value === "string") {
  value = 10;
  // Sau assignment, value không còn được xem là string.
}
```

Cấp cao (senior / 시니어) debugging nên hỏi: “fact nào khiến checker narrow ở đây, và thao tác (operation / 연산) nào làm fact đó hết đáng tin?” thay vì nghĩ kiểu (type / 타입) là một label cố định dán vào variable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, cơ chế trong **24. Control-flow phân tích (analysis / 분석) là data-flow proof, không chỉ là typeof** cần được kiểm chứng bằng dấu vết cụ thể; **25. kiểu (type / 타입) predicate và assertion hàm (function / 함수): biến thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) thành proof có tên** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **26. Tuple: array có positional đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. kiểu (type / 타입) predicate và assertion hàm (function / 함수): biến thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) thành proof có tên

Khi kiểm tra hợp lệ (validation / 검증) lô-gic (logic / 논리) lặp lại, có thể đóng gói bằng **kiểu (type / 타입) predicate**:

```ts
type User = {
  id: string;
  name: string;
};

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    typeof value.id === "string" &&
    "name" in value &&
    typeof value.name === "string"
  );
}
```

`value is User` không tự kiểm tra gì thêm; hiện thực (implementation / 구현) của predicate vẫn phải đúng. Nếu predicate nói dối, checker sẽ tin proof sai. Vì vậy predicate là một **trusted proof-producing hàm (function / 함수)** và cần kiểm thử (test / 테스트) kỹ hơn helper thông thường.

Assertion hàm (function / 함수) đi xa hơn: nếu hàm (function / 함수) return bình thường, checker xem bất biến (invariant / 불변식) đã được chứng minh.

```ts
function assertUser(value: unknown): asserts value is User {
  if (!isUser(value)) {
    throw new Error("Invalid User");
  }
}
```

Sau `assertUser(raw)`, `raw` được narrow thành `User`. mẫu (pattern / 패턴) này hữu ích ở yêu cầu (request / 요청) ranh giới (boundary / 경계), cấu hình (config / 설정) bootstrap và kiểm thử (test / 테스트) setup, nhưng không nên dùng assertion để che parsing thiếu bằng chứng (evidence / 증거).

TypeScript từ 5.5 còn có thể suy ra kiểu (type / 타입) predicate trong một số hàm (function / 함수) đơn giản. Dù vậy, công khai (public / 공개) kiểm tra hợp lệ (validation / 검증) API nên ưu tiên signature dễ đọc và kiểm thử (test / 테스트) được thay vì dựa hoàn toàn vào suy luận (inference / 추론) tinh vi.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **25. kiểu (type / 타입) predicate và assertion hàm (function / 함수): biến thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) thành proof có tên** nêu điều cần giải thích; **26. Tuple: array có positional đặc tả hợp đồng (contract / 계약)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **27. lớp (class / 클래스) typing: instance side khác constructor side** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Tuple: array có positional đặc tả hợp đồng (contract / 계약)

Tuple không chỉ là “array ngắn”. Nó encode ý nghĩa theo vị trí:

```ts
type Coordinate = readonly [x: number, y: number];
```

Named tuple labels giúp documentation nhưng không tạo thời gian chạy (runtime / 런타임) keys. giá trị (value / 값) vẫn là array `[10, 20]`.

Variadic tuple cho phép giữ quan hệ (relation / 관계) qua hàm (function / 함수) composition:

```ts
type WithContext<TArgs extends readonly unknown[]> =
  [context: RequestContext, ...args: TArgs];
```

Tuple mạnh khi giao thức (protocol / 프로토콜) thực sự positional, như `[error, result]`, coordinate hoặc parameter danh sách (list / 목록). Nếu các vị trí có nhiều optional branch và người đọc phải đếm chỉ mục (index / 인덱스), đối tượng (object / 객체) thường tốt hơn vì trường dữ liệu (field / 필드) names giữ meaning ở thời gian chạy (runtime / 런타임) lẫn nguồn (source / 소스).

`readonly` tuple đặc biệt hữu ích cho suy luận (inference / 추론) literal và covariance-like read-only luồng (flow / 흐름). Nó không freeze thời gian chạy (runtime / 런타임) array.

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **27. lớp (class / 클래스) typing: instance side khác constructor side** tiếp nhận điểm tựa từ **26. Tuple: array có positional đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. this typing: JavaScript quyết định thời gian chạy (runtime / 런타임), TypeScript chỉ mô hình đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. lớp (class / 클래스) typing: instance side khác constructor side

Một `class` tạo ra ít nhất hai khái niệm liên quan: thời gian chạy (runtime / 런타임) constructor giá trị (value / 값) và instance kiểu (type / 타입).

```ts
class UserService {
  constructor(readonly endpoint: string) {}

  load(): Promise<void> {
    return Promise.resolve();
  }
}
```

`UserService` trong giá trị (value / 값) position là constructor. `UserService` trong kiểu (type / 타입) position thường nói về instance. Khi generic factory cần constructor, đặc tả hợp đồng (contract / 계약) phải mô tả constructor side:

```ts
type Constructor<T> = new (...args: any[]) => T;

function create<T>(Ctor: Constructor<T>): T {
  return new Ctor();
}
```

`private`/`protected` của TypeScript ảnh hưởng assignability và truy cập (access / 접근) checking, nhưng không phải ranh giới bảo mật (security boundary / 보안 경계). ECMAScript `#private` fields mới có thời gian chạy (runtime / 런타임) privacy ngữ nghĩa (semantics / 의미론). Hai thứ không nên bị nhập làm một.

`abstract` lớp (class / 클래스) cũng là static đặc tả hợp đồng (contract / 계약): nó ngăn instantiate trực tiếp và yêu cầu subclass implement members, nhưng thời gian chạy (runtime / 런타임) inheritance vẫn là JavaScript prototype/lớp (class / 클래스) ngữ nghĩa (semantics / 의미론). Vì vậy mọi vấn đề về `this`, prototype chuỗi (chain / 사슬) và initialization thứ tự (order / 순서) vẫn quay về JavaScript chuẩn gốc (canonical / 정본) docs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **28. this typing: JavaScript quyết định thời gian chạy (runtime / 런타임), TypeScript chỉ mô hình đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **27. lớp (class / 클래스) typing: instance side khác constructor side** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. const kiểu (type / 타입) parameter: yêu cầu suy luận (inference / 추론) giữ literal thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. `this` typing: JavaScript quyết định thời gian chạy (runtime / 런타임), TypeScript chỉ mô hình đặc tả hợp đồng (contract / 계약)

TypeScript có thể mô tả `this` parameter giả, không được emit thành JavaScript argument:

```ts
interface HandlerContext {
  requestId: string;
}

function handle(this: HandlerContext, value: string) {
  console.log(this.requestId, value);
}
```

Signature trên giúp checker yêu cầu cách gọi có `this` phù hợp, nhưng thời gian chạy (runtime / 런타임) `this` vẫn tuân theo call-site ngữ nghĩa (semantics / 의미론) của JavaScript. Arrow hàm (function / 함수) vẫn capture lexical `this`; phương thức (method / 메서드) extraction vẫn có thể mất receiver nếu thời gian chạy (runtime / 런타임) lời gọi (call / 호출) thay đổi.

Trong callback API, `this: void` có thể nói callback không được phụ thuộc receiver. Đây là type-level documentation cho một thời gian chạy (runtime / 런타임) bất biến (invariant / 불변식), không phải cơ chế bind.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **29. const kiểu (type / 타입) parameter: yêu cầu suy luận (inference / 추론) giữ literal thông tin (information / 정보)** tiếp nhận điểm tựa từ **28. this typing: JavaScript quyết định thời gian chạy (runtime / 런타임), TypeScript chỉ mô hình đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. NoInfer<T>: ngăn một vị trí tham gia suy luận generic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. `const` kiểu (type / 타입) parameter: yêu cầu suy luận (inference / 추론) giữ literal thông tin (information / 정보)

Từ TypeScript 5.0, generic API có thể dùng `const` modifier để ưu tiên const-like suy luận (inference / 추론):

```ts
function defineRoutes<const T extends readonly string[]>(routes: T) {
  return routes;
}

const routes = defineRoutes(["/", "/users", "/settings"]);
// T giữ tuple/literal information tốt hơn so với inference rộng thông thường.
```

Điểm quan trọng là `const T` không làm thời gian chạy (runtime / 런타임) giá trị (value / 값) immutable. Nó thay chiến lược suy luận (inference / 추론) ở lời gọi (call / 호출) site. ràng buộc (constraint / 제약조건) vẫn phải phù hợp; nếu ràng buộc (constraint / 제약조건) mutable nhưng argument suy luận (inference / 추론) muốn readonly, checker có thể fallback theo cách gây bất ngờ.

Dùng tính năng (feature / 기능) này cho config-builder, tuyến (route / 경로) definitions và schema-like APIs nơi literal định danh (identity / 식별자) mang meaning. Đừng thêm `const` vào mọi generic chỉ vì “chính xác hơn”; công khai (public / 공개) kiểu (type / 타입) càng literal-heavy càng dễ tạo union lớn và diagnostic dài.

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **30. NoInfer<T>: ngăn một vị trí tham gia suy luận generic** tiếp nhận điểm tựa từ **29. const kiểu (type / 타입) parameter: yêu cầu suy luận (inference / 추론) giữ literal thông tin (information / 정보)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. hàm (function / 함수) tính tương thích (compatibility / 호환성): parameter count, bivariance legacy và strictFunctionTypes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. `NoInfer<T>`: ngăn một vị trí tham gia suy luận generic

Đôi khi nhiều arguments cùng “bỏ phiếu” cho T nhưng chỉ một nguồn nên quyết định kiểu (type / 타입). `NoInfer<T>` cho phép giữ ràng buộc (constraint / 제약조건) mà không dùng vị trí đó làm suy luận (inference / 추론) nguồn (source / 소스).

```ts
function createFSM<TState extends string>(
  states: readonly TState[],
  initial: NoInfer<TState>
) {
  return { states, initial };
}

createFSM(["open", "closed"] as const, "open");
// "missing" sẽ không được dùng để làm rộng TState rồi hợp thức hóa chính nó.
```

Mô hình tư duy (mental model / 사고 모델) là **điều khiển (control / 제어) suy luận (inference / 추론) direction**, không phải đổi assignability cuối cùng. Đây là công cụ API thiết kế (design / 설계) tốt hơn các generic phụ chỉ được tạo để “hack suy luận (inference / 추론)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **31. hàm (function / 함수) tính tương thích (compatibility / 호환성): parameter count, bivariance legacy và strictFunctionTypes** tiếp nhận điểm tựa từ **30. NoInfer<T>: ngăn một vị trí tham gia suy luận generic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. chỉ mục (index / 인덱스) signature và key không gian (space / 공간): “mọi string key” là một lời hứa rất lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. hàm (function / 함수) tính tương thích (compatibility / 호환성): parameter count, bivariance legacy và `strictFunctionTypes`

JavaScript thường bỏ qua extra callback arguments, nên TypeScript cho phép một số hàm (function / 함수) assignment mà nominal ngôn ngữ (language / 언어) có thể không cho. Tuy nhiên với `strictFunctionTypes`, parameter types của hàm (function / 함수) properties/callbacks được kiểm tra chặt hơn để tránh bên tiêu thụ (consumer / 소비자) quá hẹp.

Một subtlety là phương thức (method / 메서드) cú pháp (syntax / 문법) có historical bivariance hành vi (behavior / 동작) ở một số ngữ cảnh (context / 맥락) để giữ tính tương thích (compatibility / 호환성) với ecosystem. Vì vậy hai signatures trông gần giống nhưng viết dạng phương thức (method / 메서드) hay thuộc tính (property / 속성) hàm (function / 함수) có thể cho assignability khác nhau.

Cấp cao (senior / 시니어) lesson không phải thuộc từng exception, mà là: khi callback variance tạo diagnostic bất ngờ, kiểm tra **dữ liệu (data / 데이터) direction**, `strictFunctionTypes`, và xem signature được khai báo như phương thức (method / 메서드) hay hàm (function / 함수) thuộc tính (property / 속성). Đừng cast callback chỉ vì hai parameter “trông gần giống”.

> **Chuyển mạch:** Trong **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **32. chỉ mục (index / 인덱스) signature và key không gian (space / 공간): “mọi string key” là một lời hứa rất lớn** tiếp nhận điểm tựa từ **31. hàm (function / 함수) tính tương thích (compatibility / 호환성): parameter count, bivariance legacy và strictFunctionTypes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Type-system dạng thất bại (failure mode / 실패 모드): proof quá mạnh hơn thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. chỉ mục (index / 인덱스) signature và key không gian (space / 공간): “mọi string key” là một lời hứa rất lớn

```ts
type UserMap = {
  [id: string]: User;
};
```

Kiểu (type / 타입) này nói bất kỳ string key nào cũng có giá trị (value / 값) theo declared kiểu (type / 타입) ở kiểu (type / 타입) mức (level / 수준). thời gian chạy (runtime / 런타임) đối tượng (object / 객체) thì key có thể thiếu. Đây là lý do `noUncheckedIndexedAccess` quan trọng.

Nếu key không gian (space / 공간) hữu hạn, `Record<UserRole, Permission[]>` hoặc mapped kiểu (type / 타입) trên literal union diễn đạt bất biến (invariant / 불변식) mạnh hơn `Record<string, ...>`. Nếu map thật sự sparse/động (dynamic / 동적), hãy chấp nhận `undefined` trong lookup hoặc dùng `Map` với API thời gian chạy (runtime / 런타임) rõ ràng.

Chỉ mục (index / 인덱스) signature cũng constrain named properties: nếu mọi string thuộc tính (property / 속성) phải là `number`, một named thuộc tính (property / 속성) `name: string` sẽ mâu thuẫn. Đây là consequence trực tiếp của câu “mọi string key”.

> **Chuyển mạch:** Ở chặng này của **TypeScript 02 — hệ kiểu (type system / 타입 시스템) Internals & Generic Modeling**, **32. chỉ mục (index / 인덱스) signature và key không gian (space / 공간): “mọi string key” là một lời hứa rất lớn** nêu điều cần giải thích; **33. Type-system dạng thất bại (failure mode / 실패 모드): proof quá mạnh hơn thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 33. Type-system dạng thất bại (failure mode / 실패 모드): proof quá mạnh hơn thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거)

Một codebase có thể “100% strict” nhưng vẫn unsound ở ranh giới (boundary / 경계) nếu nhà phát triển (developer / 개발자) liên tục tạo proof bằng assertion, predicate sai, ambient declaration sai hoặc generic parser kiểu `parse<T>()`.

Hãy phân biệt:

```text
proof được compiler suy ra từ code
proof được runtime validator tạo ra
proof developer tự tuyên bố bằng assertion/declaration
```

Ba loại proof có mức trust khác nhau. cấp cao (senior / 시니어) TypeScript không chỉ giảm số lỗi (error / 오류); nó quản lý **nguồn gốc của bằng chứng** và blast radius khi bằng chứng sai.

---

Tiếp theo: [TypeScript 03 — Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md).

> **Bàn giao:** Sau **33. Type-system dạng thất bại (failure mode / 실패 모드): proof quá mạnh hơn thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
