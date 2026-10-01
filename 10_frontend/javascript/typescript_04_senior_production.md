# TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Trust ranh giới (boundary / 경계): mọi dữ liệu bên ngoài tiến trình (process / 프로세스) đều bắt đầu như unknown** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **2. DTO và lĩnh vực (domain / 도메인) mô hình (model / 모델) không nên bị đồng nhất tự động** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> Prerequisite: [Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md). Mục tiêu của chapter này là nối static mô hình (model / 모델) với bằng chứng (evidence / 증거) môi trường vận hành (production / 운영 환경) thay vì dừng ở type-level elegance.

## 1. Trust ranh giới (boundary / 경계): mọi dữ liệu bên ngoài tiến trình (process / 프로세스) đều bắt đầu như `unknown`

HTTP phản hồi (response / 응답), localStorage, URL params, postMessage, bản địa (native / 네이티브) cầu nối (bridge / 브리지) payload, cơ sở dữ liệu (database / 데이터베이스) row qua untyped driver, hàng đợi (queue / 큐) sự kiện (event / 이벤트) và JSON tệp (file / 파일) đều có thể khác giả định (assumption / 가정). TypeScript chỉ biết declarations bạn cung cấp.

Một ranh giới (boundary / 경계) trung thực:

```ts
type User = {
  id: string;
  age: number;
};

function decodeUser(value: unknown): User {
  if (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    typeof value.id === "string" &&
    "age" in value &&
    typeof value.age === "number"
  ) {
    return {
      id: value.id,
      age: value.age
    };
  }

  throw new Error("Invalid user payload");
}
```

Real dự án (project / 프로젝트) có thể dùng lược đồ (schema / 스키마)/validator thư viện (library / 라이브러리), nhưng mô hình tư duy (mental model / 사고 모델) không đổi: **parse/validate bên ngoài (external / 외부) biểu diễn (representation / 표현) → create trusted lĩnh vực (domain / 도메인) giá trị (value / 값)**. `as User` không thay parser.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **1. Trust ranh giới (boundary / 경계): mọi dữ liệu bên ngoài tiến trình (process / 프로세스) đều bắt đầu như unknown** đã nêu tiêu chí phân biệt, còn **2. DTO và lĩnh vực (domain / 도메인) mô hình (model / 모델) không nên bị đồng nhất tự động** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **3. Branded ID ngăn cross-domain mix-up nhưng không validate format** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. DTO và lĩnh vực (domain / 도메인) mô hình (model / 모델) không nên bị đồng nhất tự động

API DTO thường phản ánh vận chuyển (transport / 전송) concerns: nullable fields, string dates, legacy names, partial dữ liệu (data / 데이터). lĩnh vực (domain / 도메인) mô hình (model / 모델) nên phản ánh bất biến (invariant / 불변식) ứng dụng (application / 애플리케이션).

```ts
type UserDto = {
  user_id: string;
  created_at: string;
};

type User = {
  id: UserId;
  createdAt: Date;
};
```

Adapter ranh giới (boundary / 경계) làm conversion + kiểm tra hợp lệ (validation / 검증). Lợi ích là nếu backend đổi format, damage được cô lập; UI/nghiệp vụ (business / 비즈니스) mã (code / 코드) không phải carry vận chuyển (transport / 전송) quirks khắp codebase.

> **Chuyển mạch:** DTO/domain boundary quyết định dữ liệu nào cần chuyển đổi; branded ID ngăn trộn sai domain nhưng không thay runtime validation. Discriminated union tiếp theo mã hóa illegal state ngay trong type model.

## 3. Branded ID ngăn cross-domain mix-up nhưng không validate format

```ts
declare const userIdBrand: unique symbol;
type UserId = string & { readonly [userIdBrand]: true };
```

Mẫu (pattern / 패턴) này giúp trình biên dịch (compiler / 컴파일러) phân biệt `UserId` và `OrderId`, nhưng thời gian chạy (runtime / 런타임) vẫn là string. Constructor/factory phải validate nếu ID có format bất biến (invariant / 불변식):

```ts
function parseUserId(value: string): UserId {
  if (!value.startsWith("usr_")) {
    throw new Error("Invalid UserId");
  }

  return value as UserId;
}
```

Assertion ở đây được đặt sau thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거), nên proof obligation rõ.

> **Chuyển mạch:** Branded IDs protect domain identity but still need runtime validation; discriminated unions encode legal state transitions. Error modeling tiếp theo phân biệt failure categories thay vì dồn mọi kết quả vào một nullable union.

## 4. Illegal trạng thái (state / 상태) khó represent hơn bằng discriminated union

Checkout trạng thái (state / 상태), websocket liên kết (connection / 연결), async mutation hay permission trạng thái (state / 상태) thường tốt hơn khi mô hình (model / 모델) bằng finite states thay vì nhiều optional booleans.

```ts
type UploadState =
  | { kind: "idle" }
  | { kind: "uploading"; progress: number }
  | { kind: "done"; assetId: string }
  | { kind: "failed"; error: Error };
```

Một reducer/switch exhaustive có thể giữ chuyển tiếp (transition / 전이) lô-gic (logic / 논리) rõ. Khi nghiệp vụ (business / 비즈니스) thêm `cancelled`, trình biên dịch (compiler / 컴파일러) chỉ ra nơi cần rà soát (review / 검토) thay vì để trạng thái (state / 상태) mới silently rơi qua default branch.

> **Chuyển mạch:** Discriminated union làm illegal state khó biểu diễn; error modeling tiếp theo giữ failure taxonomy rõ trước khi đặt component contract cho React.

## 5. lỗi (error / 오류) modeling: đừng biến mọi thất bại (failure / 실패) thành `Error | null | undefined`

Trong ranh giới (boundary / 경계) quan trọng, lỗi (error / 오류) category có thể là lĩnh vực (domain / 도메인) dữ liệu (data / 데이터):

```ts
type LoginResult =
  | { ok: true; token: string }
  | { ok: false; reason: "invalid_credentials" }
  | { ok: false; reason: "locked"; retryAfterMs: number };
```

Nhưng không phải mọi exception cần union khổng lồ. Unexpected programmer/thời gian chạy (runtime / 런타임) faults vẫn có thể throw. Hãy phân biệt expected nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과) với exceptional thất bại (failure / 실패); kiểu (type / 타입) mô hình (model / 모델) nên phản ánh chiến lược khôi phục (recovery strategy / 복구 전략).

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **6. React + TypeScript: kiểu (type / 타입) thành phần (component / 컴포넌트) đặc tả hợp đồng (contract / 계약), không kiểu (type / 타입) khung phần mềm (framework / 프레임워크) theo cảm giác** tiếp nhận điểm tựa từ **5. lỗi (error / 오류) modeling: đừng biến mọi thất bại (failure / 실패) thành Error | null | undefined** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. sự kiện (event / 이벤트) và ref types: derive từ API thay vì nhớ bằng rote** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. React + TypeScript: kiểu (type / 타입) thành phần (component / 컴포넌트) đặc tả hợp đồng (contract / 계약), không kiểu (type / 타입) khung phần mềm (framework / 프레임워크) theo cảm giác

React thành phần (component / 컴포넌트) props là API công khai (public API / 공개 API) nhỏ. Discriminated props loại invalid combinations tốt hơn optional soup:

```ts
type ButtonProps =
  | {
      kind: "link";
      href: string;
      onClick?: never;
    }
  | {
      kind: "action";
      onClick: () => void;
      href?: never;
    };
```

Trạng thái (state / 상태)/reducer actions cũng hưởng lợi từ discriminated unions. Generic thành phần (component / 컴포넌트) chỉ nên generic khi quan hệ (relation / 관계) thật cần giữ, ví dụ bảng (table / 테이블) `row` và accessor keys. Đừng biến mọi thành phần (component / 컴포넌트) thành `<TData, TValue, TMeta>` nếu thành phần (component / 컴포넌트) chỉ hiển thị vài fields cố định.

Các mô hình tư duy (mental model / 사고 모델) kết xuất (render / 렌더링)/trạng thái (state / 상태)/tác động (effect / 효과) thuộc [React canonical docs](../react/00_index.md); TypeScript không thay React ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **7. sự kiện (event / 이벤트) và ref types: derive từ API thay vì nhớ bằng rote** tiếp nhận điểm tựa từ **6. React + TypeScript: kiểu (type / 타입) thành phần (component / 컴포넌트) đặc tả hợp đồng (contract / 계약), không kiểu (type / 타입) khung phần mềm (framework / 프레임워크) theo cảm giác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. nút (node / 노드)/backend TypeScript: static types không thay kiểm tra hợp lệ (validation / 검증)/authorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. sự kiện (event / 이벤트) và ref types: derive từ API thay vì nhớ bằng rote

Với khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) types, ưu tiên derive/import chuẩn gốc (canonical / 정본) types từ thư viện (library / 라이브러리) declarations. Nếu callback kiểu (type / 타입) quá phức tạp, hover/go-to-definition để xem đặc tả hợp đồng (contract / 계약) thay vì tự viết gần giống. bản sao (copy / 복사) kiểu (type / 타입) thủ công dễ drift theo phiên bản (version / 버전).

Khi suy luận (inference / 추론) đủ tốt, không cần annotate từng sự kiện (event / 이벤트). Annotation nên được dùng ở exported helpers hoặc chỗ contextual typing mất thông tin.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **8. nút (node / 노드)/backend TypeScript: static types không thay kiểm tra hợp lệ (validation / 검증)/authorization** tiếp nhận điểm tựa từ **7. sự kiện (event / 이벤트) và ref types: derive từ API thay vì nhớ bằng rote** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. bảo mật (security / 보안): những gì TypeScript không bảo vệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. nút (node / 노드)/backend TypeScript: static types không thay kiểm tra hợp lệ (validation / 검증)/authorization

Controller nhận yêu cầu (request / 요청) body không nên cast thẳng thành lĩnh vực (domain / 도메인) command. Auth claims cũng là bên ngoài (external / 외부)/ranh giới bảo mật (security boundary / 보안 경계). TypeScript không chứng minh người dùng (user / 사용자) có permission; nó chỉ có thể giúp mô hình (model / 모델) đầu ra (output / 출력) của một authorization step đã chạy.

```text
request bytes
→ parse
→ authenticate
→ authorize
→ validate command
→ domain operation
```

Mỗi arrow là một ranh giới (boundary / 경계) có dạng thất bại (failure mode / 실패 모드) riêng. kiểu (type / 타입) alias `AdminUser` không tự biến JWT thành admin.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **9. bảo mật (security / 보안): những gì TypeScript không bảo vệ** tiếp nhận điểm tựa từ **8. nút (node / 노드)/backend TypeScript: static types không thay kiểm tra hợp lệ (validation / 검증)/authorization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. @ts-expect-error tốt hơn @ts-ignore khi kiểm thử (test / 테스트) known invalid mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. bảo mật (security / 보안): những gì TypeScript không bảo vệ

TypeScript không ngăn XSS, CSRF, SQL injection, prototype pollution, SSRF hay broken kiểm soát truy cập (access control / 접근 제어) chỉ bằng static types. Nó có thể giúp tạo safer APIs—ví dụ tách `TrustedHtml` khỏi raw string hoặc parameterize truy vấn (query / 쿼리) builder—nhưng thời gian chạy (runtime / 런타임) sanitization/escaping/authorization vẫn phải tồn tại.

Assertion, `any`, `@ts-ignore` và declaration giả đặc biệt nguy hiểm ở security-sensitive ranh giới (boundary / 경계) vì chúng làm checker im đúng nơi bằng chứng (evidence / 증거) yếu nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **10. @ts-expect-error tốt hơn @ts-ignore khi kiểm thử (test / 테스트) known invalid mã (code / 코드)** tiếp nhận điểm tựa từ **9. bảo mật (security / 보안): những gì TypeScript không bảo vệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Compile-time đặc tả hợp đồng (contract / 계약) tests cho thư viện (library / 라이브러리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. `@ts-expect-error` tốt hơn `@ts-ignore` khi kiểm thử (test / 테스트) known invalid mã (code / 코드)

Nếu intentionally kiểm thử (test / 테스트) compile-time rejection:

```ts
// @ts-expect-error invalid id type must be rejected
loadUser(123);
```

`@ts-expect-error` sẽ báo nếu dòng đó không còn lỗi (error / 오류), giúp kiểm thử (test / 테스트) không silently obsolete. `@ts-ignore` chỉ suppress và dễ sống mãi. Comment phải nói bất biến (invariant / 불변식) gì đang được kiểm thử (test / 테스트), không chỉ “fix TS”.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **11. Compile-time đặc tả hợp đồng (contract / 계약) tests cho thư viện (library / 라이브러리)** tiếp nhận điểm tựa từ **10. @ts-expect-error tốt hơn @ts-ignore khi kiểm thử (test / 테스트) known invalid mã (code / 코드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. API công khai (public API / 공개 API) kiểu (type / 타입) nên nhỏ, stable và explainable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Compile-time đặc tả hợp đồng (contract / 계약) tests cho thư viện (library / 라이브러리)

Thư viện (library / 라이브러리) có thể cần kiểm thử (test / 테스트) cả hành vi thời gian chạy (runtime behavior / 런타임 동작) và kiểu (type / 타입) surface. Một API generic có thể thời gian chạy (runtime / 런타임) pass nhưng suy luận (inference / 추론) regression phá bên tiêu thụ (consumer / 소비자). kiểm thử (test / 테스트) fixtures nên cover valid suy luận (inference / 추론), expected invalid calls và declaration đầu ra (output / 출력).

Công khai (public / 공개) kiểu (type / 타입) changes cần semantic-version lập luận (reasoning / 추론) tương tự thời gian chạy (runtime / 런타임) API. Một “refactor kiểu (type / 타입) only” có thể là breaking thay đổi (change / 변경) nếu bên tiêu thụ (consumer / 소비자) nguồn (source / 소스) không compile.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **12. API công khai (public API / 공개 API) kiểu (type / 타입) nên nhỏ, stable và explainable** tiếp nhận điểm tựa từ **11. Compile-time đặc tả hợp đồng (contract / 계약) tests cho thư viện (library / 라이브러리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. thời gian chạy (runtime / 런타임) lược đồ (schema / 스키마) và static kiểu (type / 타입) nên có một nguồn chuẩn (source of truth / 정본) khi có thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. API công khai (public API / 공개 API) kiểu (type / 타입) nên nhỏ, stable và explainable

Exporting giant inferred nội bộ (internal / 내부) kiểu (type / 타입) làm hiện thực (implementation / 구현) leak ra công khai (public / 공개) đặc tả hợp đồng (contract / 계약). Khi nội bộ (internal / 내부) refactor đổi inferred shape, bên tiêu thụ (consumer / 소비자) bị break ngoài ý muốn.

Nên đặt tường minh (explicit / 명시적) công khai (public / 공개) aliases/interfaces ở ranh giới (boundary / 경계) và giữ helper conditional/mapped types private khi có thể. công khai (public / 공개) generic các ràng buộc (constraints / 제약조건들) phải phản ánh concept lĩnh vực (domain / 도메인), không expose checker hiện thực (implementation / 구현) details.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **12. API công khai (public API / 공개 API) kiểu (type / 타입) nên nhỏ, stable và explainable** nêu điều cần giải thích; **13. thời gian chạy (runtime / 런타임) lược đồ (schema / 스키마) và static kiểu (type / 타입) nên có một nguồn chuẩn (source of truth / 정본) khi có thể** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. API máy khách (client / 클라이언트): normalize lỗi (error / 오류) và dữ liệu (data / 데이터) một lần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. thời gian chạy (runtime / 런타임) lược đồ (schema / 스키마) và static kiểu (type / 타입) nên có một nguồn chuẩn (source of truth / 정본) khi có thể

Nếu maintain lược đồ (schema / 스키마) thời gian chạy (runtime / 런타임) và TypeScript kiểu (type / 타입) độc lập, chúng có thể drift. Tùy ngăn xếp (stack / 스택), có thể derive kiểu (type / 타입) từ lược đồ (schema / 스키마) hoặc lược đồ (schema / 스키마) từ mô hình (model / 모델)/codegen. Nhưng “single nguồn (source / 소스)” cũng có sự đánh đổi (trade-off / 트레이드오프): generated đầu ra (output / 출력) khó đọc, công cụ (tool / 도구) lock-in, thời gian chạy (runtime / 런타임) bundle kích thước (size / 크기) hoặc lược đồ (schema / 스키마) expressiveness khác hệ kiểu (type system / 타입 시스템).

Quyết định đúng dựa trên trust ranh giới (boundary / 경계) và quyền sở hữu (ownership / 소유권). Quan trọng nhất là có automated bằng chứng (evidence / 증거) rằng thời gian chạy (runtime / 런타임) validator và static đặc tả hợp đồng (contract / 계약) không lệch.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **13. thời gian chạy (runtime / 런타임) lược đồ (schema / 스키마) và static kiểu (type / 타입) nên có một nguồn chuẩn (source of truth / 정본) khi có thể** nêu điều cần giải thích; **14. API máy khách (client / 클라이언트): normalize lỗi (error / 오류) và dữ liệu (data / 데이터) một lần** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Async kiểu (type / 타입) không loại race điều kiện (condition / 조건)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. API máy khách (client / 클라이언트): normalize lỗi (error / 오류) và dữ liệu (data / 데이터) một lần

Thay vì mỗi thành phần (component / 컴포넌트) tự `fetch` rồi cast:

```ts
async function getUser(id: UserId): Promise<User> {
  const response = await fetch(`/api/users/${id}`);

  if (!response.ok) {
    throw new HttpError(response.status);
  }

  const raw: unknown = await response.json();
  return decodeUser(raw);
}
```

Ranh giới (boundary / 경계) này tập trung HTTP status, JSON parse, kiểm tra hợp lệ (validation / 검증) và ánh xạ (mapping / 매핑). Downstream mã (code / 코드) làm việc với trusted `User` thay vì lặp defensive checks.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **14. API máy khách (client / 클라이언트): normalize lỗi (error / 오류) và dữ liệu (data / 데이터) một lần** nêu điều cần giải thích; **15. Async kiểu (type / 타입) không loại race điều kiện (condition / 조건)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. hiệu năng (performance / 성능): type-check thời gian (time / 시간) là môi trường vận hành (production / 운영 환경) nhà phát triển (developer / 개발자) experience** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Async kiểu (type / 타입) không loại race điều kiện (condition / 조건)

`Promise<User>` nói eventual giá trị (value / 값) kiểu (type / 타입), không nói yêu cầu (request / 요청) nào thắng nếu hai yêu cầu (request / 요청) chạy song song. TypeScript không ngăn stale phản hồi (response / 응답) overwrite newer trạng thái (state / 상태). thời gian chạy (runtime / 런타임) tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) vẫn cần AbortController, yêu cầu (request / 요청) định danh (identity / 식별자), máy trạng thái (state machine / 상태 머신) hoặc framework-level dữ liệu (data / 데이터) tầng (layer / 계층).

Đây là ví dụ điển hình của liên kết (connection / 연결) với JavaScript async thời gian chạy (runtime / 런타임): static kiểu (type / 타입) đúng nhưng temporal hành vi (behavior / 동작) sai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **16. hiệu năng (performance / 성능): type-check thời gian (time / 시간) là môi trường vận hành (production / 운영 환경) nhà phát triển (developer / 개발자) experience** tiếp nhận điểm tựa từ **15. Async kiểu (type / 타입) không loại race điều kiện (condition / 조건)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. any debt phải được quản lý như di chuyển (migration / 마이그레이션) debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. hiệu năng (performance / 성능): type-check thời gian (time / 시간) là môi trường vận hành (production / 운영 환경) nhà phát triển (developer / 개발자) experience

Large codebase phải theo dõi cold check, incremental check, editor độ trễ (latency / 지연 시간) và bộ nhớ (memory / 메모리). TypeScript 7.0 giảm đáng kể trình biên dịch (compiler / 컴파일러) chi phí (cost / 비용) trong nhiều tải công việc (workload / 워크로드) nhờ bản địa (native / 네이티브) kiến trúc (architecture / 아키텍처), nhưng pathological kiểu (type / 타입) definitions vẫn có thể đắt.

Khi một tệp (file / 파일) tạo giant union/recursive conditional, không nên nói “trình biên dịch (compiler / 컴파일러) 7 nhanh rồi nên bỏ qua”. Fast trình biên dịch (compiler / 컴파일러) tăng ngân sách (budget / 예산), không xóa asymptotic/problem-shape chi phí (cost / 비용).

Bằng chứng (evidence / 증거) nên gồm `--extendedDiagnostics`, dấu vết (trace / 추적) khi cần, diff before/after PR và editor reproduction. Tối ưu bằng cách giảm kiểu (type / 타입) instantiation, chia công khai (public / 공개) surface, tránh huge generated unions, hoặc chuyển kiểm tra hợp lệ (validation / 검증) lô-gic (logic / 논리) phù hợp về thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **17. any debt phải được quản lý như di chuyển (migration / 마이그레이션) debt** tiếp nhận điểm tựa từ **16. hiệu năng (performance / 성능): type-check thời gian (time / 시간) là môi trường vận hành (production / 운영 환경) nhà phát triển (developer / 개발자) experience** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. di chuyển (migration / 마이그레이션) JavaScript → TypeScript theo rủi ro (risk / 위험), không theo folder alphabet** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. `any` debt phải được quản lý như di chuyển (migration / 마이그레이션) debt

`any` ở một leaf adapter có thể chấp nhận tạm thời; `any` ở dùng chung (shared / 공유) thư viện (library / 라이브러리) ranh giới (boundary / 경계) có blast radius lớn. Khi migrate legacy mã (code / 코드), nhánh học (track / 트랙) số `any` thôi chưa đủ. Phân loại:

```text
boundary any     → ưu tiên thay bằng unknown + validation
library any      → ưu tiên cao vì lan sang consumer
local migration  → có thể tạm chấp nhận với TODO/owner
third-party gap  → isolate bằng adapter/declaration patch
```

Mục tiêu là containment và bằng chứng (evidence / 증거), không phải “zero any” bằng cast tinh vi hơn.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **18. di chuyển (migration / 마이그레이션) JavaScript → TypeScript theo rủi ro (risk / 위험), không theo folder alphabet** tiếp nhận điểm tựa từ **17. any debt phải được quản lý như di chuyển (migration / 마이그레이션) debt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Legacy patterns phải biết đọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. di chuyển (migration / 마이그레이션) JavaScript → TypeScript theo rủi ro (risk / 위험), không theo folder alphabet

Một chiến lược thực dụng:

```text
1. bật project graph / allowJs
2. type shared contracts và domain boundaries
3. type API/data adapters
4. type utilities/core logic
5. migrate feature modules dần
6. tighten strict flags theo evidence
7. loại escape hatches còn lại
```

Nếu bật toàn bộ strict flags trên codebase lớn rồi thêm hàng nghìn `as any`, bạn đạt cấu hình (config / 설정) strict nhưng không đạt kiểu (type / 타입) an toàn (safety / 안전).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **19. Legacy patterns phải biết đọc** tiếp nhận điểm tựa từ **18. di chuyển (migration / 마이그레이션) JavaScript → TypeScript theo rủi ro (risk / 위험), không theo folder alphabet** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Debugging môi trường vận hành (production / 운영 환경) kiểu (type / 타입)/thời gian chạy (runtime / 런타임) mismatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Legacy patterns phải biết đọc

Bạn vẫn có thể gặp `namespace`, triple-slash references, ambient globals, old decorator chế độ (mode / 모드), `enum`-heavy mã (code / 코드), non-strict null handling, `moduleResolution` legacy modes và CommonJS interop workaround. Mục tiêu không phải rewrite ngay; trước tiên hiểu thời gian chạy (runtime / 런타임)/gói (package / 패키지) các giả định (assumptions / 가정들), thêm tests, rồi migrate theo seam nhỏ.

`enum` là ví dụ cần lập luận (reasoning / 추론). Nó có thời gian chạy (runtime / 런타임) biểu diễn (representation / 표현) khác type-only union. Literal union + `as const` đối tượng (object / 객체) thường phù hợp cấu hình (config / 설정)/lĩnh vực (domain / 도메인) constants hiện đại, nhưng existing enum có thể là công khai (public / 공개) ABI hoặc phụ thuộc (dependency / 의존성) expectation. Đừng đổi chỉ vì style.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **20. Debugging môi trường vận hành (production / 운영 환경) kiểu (type / 타입)/thời gian chạy (runtime / 런타임) mismatch** tiếp nhận điểm tựa từ **19. Legacy patterns phải biết đọc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. khả năng quan sát (observability / 관측 가능성): log ranh giới (boundary / 경계) facts, không log kiểu (type / 타입) name** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Debugging môi trường vận hành (production / 운영 환경) kiểu (type / 타입)/thời gian chạy (runtime / 런타임) mismatch

Khi môi trường vận hành (production / 운영 환경) crash dù CI type-check pass, dấu vết (trace / 추적) theo ranh giới (boundary / 경계):

```text
1. runtime value thật là gì?
2. value đi vào typed world qua chỗ nào?
3. có assertion/any/declaration nào tạo false proof?
4. validator/schema version có khớp producer không?
5. emitted/bundled artifact có khác source assumptions không?
```

Ví dụ ngăn xếp (stack / 스택) `Cannot read properties of undefined` trên `user.profile.name` thường không cần “kiểu (type / 타입) phức tạp hơn”; cần tìm nơi `user` được tạo từ bên ngoài (external / 외부) dữ liệu (data / 데이터) mà không validate.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **20. Debugging môi trường vận hành (production / 운영 환경) kiểu (type / 타입)/thời gian chạy (runtime / 런타임) mismatch** đã nêu tiêu chí phân biệt, còn **21. khả năng quan sát (observability / 관측 가능성): log ranh giới (boundary / 경계) facts, không log kiểu (type / 타입) name** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **22. gói (package / 패키지)/thư viện (library / 라이브러리) authoring với TypeScript 7** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. khả năng quan sát (observability / 관측 가능성): log ranh giới (boundary / 경계) facts, không log kiểu (type / 타입) name

Thời gian chạy (runtime / 런타임) không biết `User` giao diện (interface / 인터페이스). Khi gỡ lỗi (debug / 디버그), log safe siêu dữ liệu (metadata / 메타데이터) thực: lược đồ (schema / 스키마)/phiên bản (version / 버전), endpoint, status, discriminant, kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) đường dẫn (path / 경로), yêu cầu (request / 요청) ID. Đừng log sensitive payload chỉ để chứng minh “kiểu (type / 타입) sai”. bảo mật (security / 보안) và khả năng quan sát (observability / 관측 가능성) phải phối hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **21. khả năng quan sát (observability / 관측 가능성): log ranh giới (boundary / 경계) facts, không log kiểu (type / 타입) name** đã nêu tiêu chí phân biệt, còn **22. gói (package / 패키지)/thư viện (library / 라이브러리) authoring với TypeScript 7** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **23. cấp cao (senior / 시니어) rà soát mã (code review / 코드 리뷰) checklist dưới dạng lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. gói (package / 패키지)/thư viện (library / 라이브러리) authoring với TypeScript 7

TypeScript 7.0 tập trung mạnh vào bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러)/tooling và hiện tại không cung cấp programmatic API giống 6.x. Nếu thư viện (library / 라이브러리) bản dựng (build / 빌드) chuỗi (chain / 사슬) hoặc plugin cần trình biên dịch (compiler / 컴파일러) API, có thể phải chạy 6.0 tính tương thích (compatibility / 호환성) gói (package / 패키지) side-by-side trong di chuyển (migration / 마이그레이션) period. Đây là toolchain concern, không có nghĩa nguồn (source / 소스) thư viện (library / 라이브러리) phải hạ type-system kiến thức (knowledge / 지식) về 6.0.

Khi publish, kiểm tra declarations, ESM/CJS exports, thời gian chạy (runtime / 런타임) mục tiêu (target / 대상), gói (package / 패키지) conditions và bên tiêu thụ (consumer / 소비자) compile fixture. TypeScript phiên bản (version / 버전) minimum nên được document khi công khai (public / 공개) types dùng tính năng (feature / 기능) mới mà trình biên dịch (compiler / 컴파일러) cũ không parse/understand.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **23. cấp cao (senior / 시니어) rà soát mã (code review / 코드 리뷰) checklist dưới dạng lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **22. gói (package / 패키지)/thư viện (library / 라이브러리) authoring với TypeScript 7** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — API trường dữ liệu (field / 필드) đổi từ required sang nullable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. cấp cao (senior / 시니어) rà soát mã (code review / 코드 리뷰) checklist dưới dạng lập luận (reasoning / 추론)

Thay vì checklist máy móc, rà soát (review / 검토) TypeScript nên hỏi theo chuỗi: kiểu (type / 타입) này mô hình bất biến (invariant / 불변식) thật hay chỉ mô tả dữ liệu (data / 데이터) hiện tại; bên ngoài (external / 외부) giá trị (value / 값) đã được validate chưa; generic giữ quan hệ (relation / 관계) nào; assertion có bằng chứng (evidence / 증거) ở đâu; cấu hình (config / 설정)/mô-đun (module / 모듈) hành vi (behavior / 동작) có khớp thời gian chạy (runtime / 런타임) không; công khai (public / 공개) kiểu (type / 타입) có expose hiện thực (implementation / 구현) detail không; và advanced kiểu (type / 타입) có đáng chi phí (cost / 비용) trình biên dịch (compiler / 컴파일러)/cognitive không?

Một PR tốt có thể xóa type-level độ phức tạp (complexity / 복잡도) nếu thời gian chạy (runtime / 런타임) mô hình (model / 모델) đã đơn giản hơn. “Nhiều kiểu (type / 타입)” không đồng nghĩa “type-safe hơn”.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **23. cấp cao (senior / 시니어) rà soát mã (code review / 코드 리뷰) checklist dưới dạng lập luận (reasoning / 추론)** cho ta quy tắc; **24. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — API trường dữ liệu (field / 필드) đổi từ required sang nullable** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **25. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — mô-đun (module / 모듈) kiểu (type / 타입) pass, thời gian chạy (runtime / 런타임) import thất bại (fail / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — API trường dữ liệu (field / 필드) đổi từ required sang nullable

Giả sử backend đổi `middleName: string` thành `string | null`. Nếu generated/handwritten DTO được cập nhật đúng, trình biên dịch (compiler / 컴파일러) sẽ đẩy diagnostic tới mapper và bên tiêu thụ (consumer / 소비자). Mapper có thể quyết định lĩnh vực (domain / 도메인) biểu diễn (representation / 표현) là `string | null`, `Option`-like union, hoặc normalize thành empty display văn bản (text / 텍스트) ở UI ranh giới (boundary / 경계).

Nếu nhóm (team / 팀) chỉ sửa bằng `as string`, bản dựng (build / 빌드) xanh nhưng thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) bị bỏ. TypeScript có giá trị khi thay đổi (change / 변경) propagation ép nhóm (team / 팀) ra quyết định tại đúng tầng (layer / 계층).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **24. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — API trường dữ liệu (field / 필드) đổi từ required sang nullable** cho ta quy tắc; **25. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — mô-đun (module / 모듈) kiểu (type / 타입) pass, thời gian chạy (runtime / 런타임) import thất bại (fail / 실패)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **26. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — type-level lớp trừu tượng (abstraction / 추상화) làm editor lag** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — mô-đun (module / 모듈) kiểu (type / 타입) pass, thời gian chạy (runtime / 런타임) import thất bại (fail / 실패)

IDE resolve alias `@domain/user` nhờ `paths`, nhưng bundler/nút (node / 노드) không có alias tương ứng. Static kiểu (type / 타입) đồ thị (graph / 그래프) pass, thời gian chạy (runtime / 런타임) thất bại (fail / 실패). gỡ lỗi (debug / 디버그) đúng là inspect resolver configs/gói (package / 패키지) exports, không chỉnh giao diện (interface / 인터페이스). Đây là lý do chapter tooling nằm trong TypeScript nhánh học (track / 트랙): kiểu (type / 타입) tính đúng đắn (correctness / 정확성) và mô-đun (module / 모듈) thực thi (execution / 실행) phải khớp.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **25. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — mô-đun (module / 모듈) kiểu (type / 타입) pass, thời gian chạy (runtime / 런타임) import thất bại (fail / 실패)** cho ta quy tắc; **26. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — type-level lớp trừu tượng (abstraction / 추상화) làm editor lag** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **27. Kết nối với JavaScript và React chuẩn gốc (canonical / 정본) docs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — type-level lớp trừu tượng (abstraction / 추상화) làm editor lag

Một design-system utility tạo template literal union từ hàng trăm đơn vị từ (token / 토큰) × variants × breakpoints. kiểu (type / 타입) auto-complete rất “thông minh” nhưng editor độ trễ (latency / 지연 시간) tăng. cấp cao (senior / 시니어) phản hồi (response / 응답) là đo checker dấu vết (trace / 추적), giảm combinatorial union, chuyển một phần kiểm tra hợp lệ (validation / 검증) sang thời gian chạy (runtime / 런타임)/lược đồ (schema / 스키마) hoặc giới hạn key không gian (space / 공간). nhà phát triển (developer / 개발자) experience là một môi trường vận hành (production / 운영 환경) ràng buộc (constraint / 제약조건) của kiểu (type / 타입) thiết kế (design / 설계).

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **26. môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) — type-level lớp trừu tượng (abstraction / 추상화) làm editor lag** cho ta quy tắc; **27. Kết nối với JavaScript và React chuẩn gốc (canonical / 정본) docs** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **28. kiểm tra hợp lệ (validation / 검증) là giao thức (protocol / 프로토콜) chuyển tiếp (transition / 전이), không chỉ là schema.parse()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Kết nối với JavaScript và React chuẩn gốc (canonical / 정본) docs

TypeScript không thay phạm vi (scope / 범위)/closure, prototype, vòng lặp sự kiện (event loop / 이벤트 루프), Promise thứ tự (ordering / 순서) hay trình duyệt (browser / 브라우저) bảo mật (security / 보안) mô hình (model / 모델); xem [JavaScript Intermediate](javascript_intermediate.md) và [JavaScript Senior](javascript_senior.md). TypeScript cũng không thay React kết xuất (render / 렌더링)/lần ghi nhận (commit / 커밋)/tác động (effect / 효과) ngữ nghĩa (semantics / 의미론); xem [React Index](../react/00_index.md).

Nếu một bug xảy ra sau khi mã (code / 코드) đã compile, quay lại thời gian chạy (runtime / 런타임) tầng (layer / 계층) trước khi thêm kiểu (type / 타입) annotation. Nếu bug là invalid trạng thái (state / 상태) được trình biên dịch (compiler / 컴파일러) cho qua, quay lại mô hình (model / 모델)/bất biến (invariant / 불변식). Nếu IDE và thời gian chạy (runtime / 런타임) disagree về import, quay lại mô-đun (module / 모듈)/tooling tầng (layer / 계층). Đây là cách tách dạng thất bại (failure mode / 실패 모드) có hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **28. kiểm tra hợp lệ (validation / 검증) là giao thức (protocol / 프로토콜) chuyển tiếp (transition / 전이), không chỉ là schema.parse()** tiếp nhận điểm tựa từ **27. Kết nối với JavaScript và React chuẩn gốc (canonical / 정본) docs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Serialization ranh giới (boundary / 경계): TypeScript kiểu (type / 타입) không bảo đảm giá trị (value / 값) truyền qua JSON được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. kiểm tra hợp lệ (validation / 검증) là giao thức (protocol / 프로토콜) chuyển tiếp (transition / 전이), không chỉ là `schema.parse()`

Một ranh giới (boundary / 경계) tốt không chỉ hỏi “shape có đúng không?” mà còn hỏi dữ liệu (data / 데이터) đang ở **giao thức (protocol / 프로토콜) phiên bản (version / 버전) nào**, ngữ nghĩa (semantic / 의미적) bất biến (invariant / 불변식) có đúng không, và sau parse giá trị (value / 값) có được normalize về biểu diễn (representation / 표현) ổn định hay không.

Ví dụ timestamp string có thể đúng shape nhưng invalid date; amount có thể là number nhưng âm trong lĩnh vực (domain / 도메인) không cho phép; status có thể là string hợp lược đồ (schema / 스키마) cũ nhưng không còn được nghiệp vụ (business / 비즈니스) chấp nhận.

```text
bytes / unknown value
→ syntactic parse
→ structural validation
→ semantic validation
→ normalization
→ domain value
```

TypeScript thường bắt đầu có giá trị mạnh nhất từ lĩnh vực (domain / 도메인) giá trị (value / 값) trở đi. Nếu nhóm (team / 팀) gọi lược đồ (schema / 스키마) validator nhưng lược đồ (schema / 스키마) quá permissive hoặc bỏ ngữ nghĩa (semantic / 의미적) step, static kiểu (type / 타입) phía sau vẫn có thể trở thành false confidence.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **28. kiểm tra hợp lệ (validation / 검증) là giao thức (protocol / 프로토콜) chuyển tiếp (transition / 전이), không chỉ là schema.parse()** đã nêu tiêu chí phân biệt, còn **29. Serialization ranh giới (boundary / 경계): TypeScript kiểu (type / 타입) không bảo đảm giá trị (value / 값) truyền qua JSON được** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **30. lược đồ (schema / 스키마) evolution: backward/forward tính tương thích (compatibility / 호환성) không nằm trong union kiểu (type / 타입) đơn lẻ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Serialization ranh giới (boundary / 경계): TypeScript kiểu (type / 타입) không bảo đảm giá trị (value / 값) truyền qua JSON được

Một đối tượng (object / 객체) TypeScript có thể chứa `Date`, `Map`, `Set`, `bigint`, hàm (function / 함수), lớp (class / 클래스) instance hoặc cyclic references. `JSON.stringify` không preserve toàn bộ ngữ nghĩa (semantics / 의미론) đó; `bigint` còn gây lỗi nếu không có chiến lược (strategy / 전략) riêng.

Vì vậy DTO qua HTTP/lưu trữ (storage / 저장소) nên dùng biểu diễn (representation / 표현) serialization-safe có chủ đích:

```ts
type UserDto = {
  id: string;
  createdAt: string;
};

type User = {
  id: UserId;
  createdAt: Date;
};
```

Nếu dùng cùng một `User` kiểu (type / 타입) cho lĩnh vực (domain / 도메인) đối tượng (object / 객체) lẫn vận chuyển (transport / 전송) payload, bạn đang che mất một chuyển tiếp trạng thái (state transition / 상태 전이) thật. Mapper không phải boilerplate vô ích; nó là nơi quyền sở hữu (ownership / 소유권) của biểu diễn (representation / 표현) được xác định.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **29. Serialization ranh giới (boundary / 경계): TypeScript kiểu (type / 타입) không bảo đảm giá trị (value / 값) truyền qua JSON được** đã nêu tiêu chí phân biệt, còn **30. lược đồ (schema / 스키마) evolution: backward/forward tính tương thích (compatibility / 호환성) không nằm trong union kiểu (type / 타입) đơn lẻ** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **31. Generated types: generated không đồng nghĩa verified** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. lược đồ (schema / 스키마) evolution: backward/forward tính tương thích (compatibility / 호환성) không nằm trong union kiểu (type / 타입) đơn lẻ

Sự kiện (event / 이벤트)/hàng đợi (queue / 큐) payload thường sống lâu hơn một deploy. Producer v2 có thể gửi trường dữ liệu (field / 필드) mới khi bên tiêu thụ (consumer / 소비자) v1 vẫn chạy. Một kiểu (type / 타입) alias mới nhất không mô tả triển khai (deployment / 배포) topology này.

Có thể mô hình (model / 모델) phiên bản (version / 버전) rõ:

```ts
type UserCreatedV1 = {
  version: 1;
  userId: string;
};

type UserCreatedV2 = {
  version: 2;
  userId: string;
  source: string;
};

type UserCreatedEvent = UserCreatedV1 | UserCreatedV2;
```

Decoder xử lý phiên bản (version / 버전), normalize về lĩnh vực (domain / 도메인) command hiện tại. Khi xóa hỗ trợ (support / 지원) V1, đó là tính tương thích (compatibility / 호환성) quyết định (decision / 결정) có telemetry/di chuyển (migration / 마이그레이션) bằng chứng (evidence / 증거), không chỉ là “remove union member cho mã (code / 코드) sạch”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **31. Generated types: generated không đồng nghĩa verified** tiếp nhận điểm tựa từ **30. lược đồ (schema / 스키마) evolution: backward/forward tính tương thích (compatibility / 호환성) không nằm trong union kiểu (type / 타입) đơn lẻ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. lĩnh vực (domain / 도메인) utility kiểu (type / 타입) có thể vô tình phá bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Generated types: generated không đồng nghĩa verified

OpenAPI, GraphQL, Protobuf hoặc cơ sở dữ liệu (database / 데이터베이스) codegen có thể tạo TypeScript rất chính xác **so với lược đồ (schema / 스키마) đầu vào (input / 입력)**, nhưng lược đồ (schema / 스키마) đầu vào (input / 입력) có thể stale so với deployed producer. mã (code / 코드) generation chứng minh consistency giữa mã (code / 코드) và lược đồ (schema / 스키마) snapshot, không chứng minh môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) đang chạy đúng snapshot đó.

Chuỗi xử lý (pipeline / 파이프라인) đáng tin hơn thường có:

```text
source schema có ownership/version
→ deterministic codegen
→ generated diff review
→ compile
→ contract/integration test với producer hoặc fixture chuẩn
```

Đừng edit generated tệp (file / 파일) bằng tay để “fix TypeScript”; hãy sửa nguồn (source / 소스) lược đồ (schema / 스키마)/generator hoặc adapter tầng (layer / 계층). Nếu phải patch generated đầu ra (output / 출력) tạm thời, patch phải có đơn vị sở hữu (owner / 오너) và kiểm thử (test / 테스트) để không biến mất âm thầm ở lần regenerate sau.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **32. lĩnh vực (domain / 도메인) utility kiểu (type / 타입) có thể vô tình phá bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **31. Generated types: generated không đồng nghĩa verified** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. năng lực (capability / 역량) typing cho bảo mật (security / 보안) tốt hơn role string lan khắp codebase** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. lĩnh vực (domain / 도메인) utility kiểu (type / 타입) có thể vô tình phá bất biến (invariant / 불변식)

`Partial<User>` rất tiện, nhưng một nghiệp vụ (business / 비즈니스) PATCH command không nhất thiết là “mọi thuộc tính (property / 속성) của người dùng (user / 사용자) đều optional”. Có trường dữ liệu (field / 필드) không được đổi, trường dữ liệu (field / 필드) đổi theo nhóm, hoặc null/absent có ngữ nghĩa (semantics / 의미론) khác nhau.

```ts
type UpdateUserCommand = {
  displayName?: string;
  locale?: Locale;
};
```

Tường minh (explicit / 명시적) command thường tốt hơn:

```ts
type UpdateUserCommand = Partial<User>;
```

nếu `User` còn chứa `id`, kiểm tra (audit / 감사) siêu dữ liệu (metadata / 메타데이터) hoặc derived fields.

Utility types nên transform technical shapes; lĩnh vực (domain / 도메인) command quan trọng nên encode thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론) trực tiếp.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **33. năng lực (capability / 역량) typing cho bảo mật (security / 보안) tốt hơn role string lan khắp codebase** tiếp nhận điểm tựa từ **32. lĩnh vực (domain / 도메인) utility kiểu (type / 타입) có thể vô tình phá bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. React máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계): serializability và thực thi (execution / 실행) placement là thời gian chạy (runtime / 런타임) ràng buộc (constraint / 제약조건)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. năng lực (capability / 역량) typing cho bảo mật (security / 보안) tốt hơn role string lan khắp codebase

Một `role: "admin"` không tự bảo đảm hành động (action / 동작) đã được authorize. Một mẫu (pattern / 패턴) tốt hơn là authorization tầng (layer / 계층) tạo năng lực (capability / 역량)/đơn vị từ (token / 토큰) đối tượng (object / 객체) chỉ khi chính sách (policy / 정책) pass:

```ts
declare const deleteUserCapability: unique symbol;

type DeleteUserCapability = {
  readonly [deleteUserCapability]: true;
  actorId: UserId;
};
```

Lĩnh vực (domain / 도메인) thao tác (operation / 연산) nhận năng lực (capability / 역량) thay vì raw role. TypeScript giúp API khó gọi sai hơn, nhưng năng lực (capability / 역량) chỉ đáng tin nếu constructor/factory nằm sau thời gian chạy (runtime / 런타임) authorization và không export escape hatch assertion.

Đây là ví dụ TypeScript hỗ trợ bảo mật (security / 보안) kiến trúc (architecture / 아키텍처), không thay thế bảo mật (security / 보안) check.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **33. năng lực (capability / 역량) typing cho bảo mật (security / 보안) tốt hơn role string lan khắp codebase** đã nêu tiêu chí phân biệt, còn **34. React máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계): serializability và thực thi (execution / 실행) placement là thời gian chạy (runtime / 런타임) ràng buộc (constraint / 제약조건)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **35. Monorepo: nội bộ (internal / 내부) import đường dẫn (path / 경로) có thể phá gói (package / 패키지) ranh giới (boundary / 경계) dù type-check pass** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. React máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계): serializability và thực thi (execution / 실행) placement là thời gian chạy (runtime / 런타임) ràng buộc (constraint / 제약조건)

Trong React ecosystem hiện đại, máy chủ (server / 서버)/máy khách (client / 클라이언트) thành phần (component / 컴포넌트) ranh giới (boundary / 경계) có rules về nơi mã (code / 코드) chạy và giá trị (value / 값) nào được truyền qua giao thức (protocol / 프로토콜) của khung phần mềm (framework / 프레임워크). TypeScript prop kiểu (type / 타입) có thể đúng nhưng giá trị (value / 값) vẫn không serializable hoặc đối tượng (object / 객체) định danh (identity / 식별자)/thời gian chạy (runtime / 런타임) API không tồn tại phía bên kia.

TypeScript nên mô hình (model / 모델) DTO/máy chủ (server / 서버) hành động (action / 동작) kết quả (result / 결과) rõ, nhưng chuẩn gốc (canonical / 정본) ngữ nghĩa (semantics / 의미론) của kết xuất (render / 렌더링), RSC, hydration và Actions vẫn thuộc [React docs](../react/00_index.md). Khi lỗi chỉ xuất hiện máy chủ (server / 서버) bản dựng (build / 빌드)/hydration, đừng thêm assertion vào prop; kiểm tra thực thi (execution / 실행) ranh giới (boundary / 경계) và khung phần mềm (framework / 프레임워크) serialization rules trước.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **34. React máy chủ (server / 서버)/máy khách (client / 클라이언트) ranh giới (boundary / 경계): serializability và thực thi (execution / 실행) placement là thời gian chạy (runtime / 런타임) ràng buộc (constraint / 제약조건)** đã nêu tiêu chí phân biệt, còn **35. Monorepo: nội bộ (internal / 내부) import đường dẫn (path / 경로) có thể phá gói (package / 패키지) ranh giới (boundary / 경계) dù type-check pass** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **36. công khai (public / 공개) kiểu (type / 타입) thay đổi (change / 변경) cần tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), không chỉ ngữ nghĩa (semantic / 의미적) phiên bản (version / 버전) intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Monorepo: nội bộ (internal / 내부) import đường dẫn (path / 경로) có thể phá gói (package / 패키지) ranh giới (boundary / 경계) dù type-check pass

Trong workspace, nhà phát triển (developer / 개발자) dễ import sâu:

```ts
import { internalHelper } from "../../packages/domain/src/internal";
```

TypeScript resolve được nên mọi thứ xanh, nhưng kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계) đã bị bypass. Khi gói (package / 패키지) đổi bố cục (layout / 레이아웃), bản dựng (build / 빌드)/publish tách riêng hoặc dự án (project / 프로젝트) references được siết, phụ thuộc (dependency / 의존성) vỡ.

Môi trường vận hành (production / 운영 환경) practice là import qua công khai (public / 공개) gói (package / 패키지) surface và dùng `exports`/lint/phụ thuộc (dependency / 의존성) rules để enforce. TypeScript đồ thị (graph / 그래프) chỉ nói phụ thuộc (dependency / 의존성) **có thể resolve**, không nói phụ thuộc (dependency / 의존성) **được phép tồn tại theo kiến trúc (architecture / 아키텍처)**.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **35. Monorepo: nội bộ (internal / 내부) import đường dẫn (path / 경로) có thể phá gói (package / 패키지) ranh giới (boundary / 경계) dù type-check pass** đã nêu tiêu chí phân biệt, còn **36. công khai (public / 공개) kiểu (type / 타입) thay đổi (change / 변경) cần tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), không chỉ ngữ nghĩa (semantic / 의미적) phiên bản (version / 버전) intuition** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **37. satisfies cho cấu hình (config / 설정) tốt khi cấu hình (config / 설정) vẫn cần thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. công khai (public / 공개) kiểu (type / 타입) thay đổi (change / 변경) cần tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), không chỉ ngữ nghĩa (semantic / 의미적) phiên bản (version / 버전) intuition

Một kiểu (type / 타입) refactor có thể breaking theo nhiều chiều:

```text
consumer compiler version
× moduleResolution mode
× ESM/CJS package condition
× strict flags
× runtime target
```

Ví dụ `.d.ts` dùng cú pháp (syntax / 문법) mới có thể làm TypeScript cũ parse thất bại (fail / 실패); conditional export có thể khiến `bundler` thấy kiểu (type / 타입) khác `nodenext`; thêm required generic parameter có thể phá suy luận (inference / 추론) dù JavaScript thời gian chạy (runtime / 런타임) API không đổi.

Thư viện (library / 라이브러리) bản phát hành (release / 릴리스) quan trọng nên có bên tiêu thụ (consumer / 소비자) fixtures ở minimum supported TypeScript + hiện tại (current / 현재) TypeScript và mô-đun (module / 모듈) modes được tuyên bố hỗ trợ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **37. satisfies cho cấu hình (config / 설정) tốt khi cấu hình (config / 설정) vẫn cần thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증)** tiếp nhận điểm tựa từ **36. công khai (public / 공개) kiểu (type / 타입) thay đổi (change / 변경) cần tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), không chỉ ngữ nghĩa (semantic / 의미적) phiên bản (version / 버전) intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. môi trường (environment / 환경) variables: process.env.X as string là một môi trường vận hành (production / 운영 환경) smell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. `satisfies` cho cấu hình (config / 설정) tốt khi cấu hình (config / 설정) vẫn cần thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증)

`satisfies` rất hữu ích với in-repo cấu hình (config / 설정) do nhà phát triển (developer / 개발자) viết vì nó giữ literal suy luận (inference / 추론) và bắt typo. Nhưng cấu hình (config / 설정) đến từ môi trường (environment / 환경) variable, JSON deploy tệp (file / 파일) hoặc remote cờ tính năng (feature flag / 기능 플래그) vẫn là bên ngoài (external / 외부) đầu vào (input / 입력).

```ts
const routes = {
  users: { method: "GET", secure: true }
} satisfies RouteConfig;
```

Đây là static proof cho nguồn (source / 소스) literal. Nếu cùng cấu trúc (structure / 구조) được tải (load / 로드) từ JSON, cần parser/validator riêng. Đừng bản sao (copy / 복사) kiểu (type / 타입) và tin dữ liệu (data / 데이터) chỉ vì shape “giống cấu hình (config / 설정) trong nguồn (source / 소스)”.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **37. satisfies cho cấu hình (config / 설정) tốt khi cấu hình (config / 설정) vẫn cần thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증)** xác định đầu vào; **38. môi trường (environment / 환경) variables: process.env.X as string là một môi trường vận hành (production / 운영 환경) smell** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **39. Async kết quả (result / 결과) kiểu (type / 타입) không mô hình (model / 모델) cancellation, deadline hay quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. môi trường (environment / 환경) variables: `process.env.X as string` là một môi trường vận hành (production / 운영 환경) smell

Môi trường (environment / 환경) variable có thể absent, malformed hoặc khác giữa cục bộ (local / 로컬)/CI/bộ chứa (container / 컨테이너). Cast từng chỗ phân tán proof giả khắp codebase.

Tốt hơn là parse một lần ở startup:

```ts
type AppConfig = {
  apiBaseUrl: URL;
  timeoutMs: number;
};

function loadConfig(env: Record<string, string | undefined>): AppConfig {
  // validate + normalize, fail fast nếu cấu hình sai
  // ...
  throw new Error("example");
}
```

Sau bootstrap, ứng dụng (application / 애플리케이션) nhận `AppConfig` trusted. Điều này biến lỗi cấu hình (config / 설정) từ random thời gian chạy (runtime / 런타임) branch thành startup thất bại (failure / 실패) có log rõ.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **38. môi trường (environment / 환경) variables: process.env.X as string là một môi trường vận hành (production / 운영 환경) smell** xác định đầu vào; **39. Async kết quả (result / 결과) kiểu (type / 타입) không mô hình (model / 모델) cancellation, deadline hay quyền sở hữu (ownership / 소유권)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **40. khả năng quan sát (observability / 관측 가능성) cho kiểm tra hợp lệ (validation / 검증)/kiểu (type / 타입) ranh giới (boundary / 경계) cần cardinality và privacy discipline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Async kết quả (result / 결과) kiểu (type / 타입) không mô hình (model / 모델) cancellation, deadline hay quyền sở hữu (ownership / 소유권)

`Promise<User>` không nói thao tác (operation / 연산) có thể bị cancel, hết thời gian chờ (timeout / 타임아웃) hay yêu cầu (request / 요청) nào owns kết quả (result / 결과). Nếu API vòng đời (lifecycle / 생명주기) quan trọng, đặc tả hợp đồng (contract / 계약) thời gian chạy (runtime / 런타임) nên expose `AbortSignal`, deadline/ngữ cảnh (context / 맥락) hoặc máy trạng thái (state machine / 상태 머신) phù hợp.

```ts
function loadUser(id: UserId, signal: AbortSignal): Promise<User> {
  // ...
}
```

Ngay cả signature này cũng không “chứng minh cancellation”; nó chỉ tạo năng lực (capability / 역량) để thời gian chạy (runtime / 런타임) hiện thực (implementation / 구현) phối hợp. TypeScript giúp lời gọi (call / 호출) site không quên channel, còn temporal tính đúng đắn (correctness / 정확성) vẫn phải kiểm thử (test / 테스트) bằng tính đồng thời (concurrency / 동시성) hành vi (behavior / 동작).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **39. Async kết quả (result / 결과) kiểu (type / 타입) không mô hình (model / 모델) cancellation, deadline hay quyền sở hữu (ownership / 소유권)** đã nêu tiêu chí phân biệt, còn **40. khả năng quan sát (observability / 관측 가능성) cho kiểm tra hợp lệ (validation / 검증)/kiểu (type / 타입) ranh giới (boundary / 경계) cần cardinality và privacy discipline** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **41. TypeScript 7 adoption: CLI, editor và embedded tooling có thể không cùng phiên bản (version / 버전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. khả năng quan sát (observability / 관측 가능성) cho kiểm tra hợp lệ (validation / 검증)/kiểu (type / 타입) ranh giới (boundary / 경계) cần cardinality và privacy discipline

Kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) rất hữu ích nếu log `schemaVersion`, lỗi (error / 오류) mã (code / 코드)/đường dẫn (path / 경로), producer, endpoint, yêu cầu (request / 요청) ID. Nhưng log toàn raw payload có thể rò PII/secret và tăng cardinality/chi phí (cost / 비용).

Một mẫu (pattern / 패턴) môi trường vận hành (production / 운영 환경) tốt là validator trả structured thất bại (failure / 실패) reason đã sanitize. Metrics aggregate theo reason/phiên bản (version / 버전); dấu vết (trace / 추적) gắn correlation ID; mẫu (sample / 표본) payload chỉ khi chính sách (policy / 정책) cho phép. TypeScript có thể kiểu (type / 타입) structured diagnostic để logging API không nhận raw lĩnh vực (domain / 도메인) secret ngoài ý muốn.

> **Chuyển mạch:** Trong **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **40. khả năng quan sát (observability / 관측 가능성) cho kiểm tra hợp lệ (validation / 검증)/kiểu (type / 타입) ranh giới (boundary / 경계) cần cardinality và privacy discipline** đã nêu tiêu chí phân biệt, còn **41. TypeScript 7 adoption: CLI, editor và embedded tooling có thể không cùng phiên bản (version / 버전)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **42. môi trường vận hành (production / 운영 환경) debugging runbook: đi từ bằng chứng (evidence / 증거) thời gian chạy (runtime / 런타임) ngược về proof nguồn (source / 소스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. TypeScript 7 adoption: CLI, editor và embedded tooling có thể không cùng phiên bản (version / 버전)

TypeScript 7.0 có bản địa (native / 네이티브) CLI/ngôn ngữ (language / 언어) máy chủ (server / 서버) nhưng chưa có stable programmatic trình biên dịch (compiler / 컴파일러) API. Vì vậy khung phần mềm (framework / 프레임워크)/tooling nhúng TypeScript có thể vẫn cần TypeScript 6 trong một thời gian.

Một repo có thể chạy:

```text
TS7 tsc trong CI
TS7 language server cho file .ts/.tsx thông thường
TS6 compatibility/API cho typescript-eslint hoặc embedded framework tooling
```

Điều này không sai nếu được quản lý rõ. dạng thất bại (failure mode / 실패 모드) là tưởng tất cả diagnostics đến từ cùng trình biên dịch (compiler / 컴파일러) rồi chase khác biệt hành vi (behavior / 동작) như bug mã nguồn (source code / 소스 코드). Upgrade plan phải ghi công cụ (tool / 도구) → compiler-version ánh xạ (mapping / 매핑) và chỉ bỏ TS6 khi phụ thuộc (dependency / 의존성) ecosystem đã hỗ trợ API mới.

> **Chuyển mạch:** Ở chặng này của **TypeScript 04 — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)**, **41. TypeScript 7 adoption: CLI, editor và embedded tooling có thể không cùng phiên bản (version / 버전)** nêu điều cần giải thích; **42. môi trường vận hành (production / 운영 환경) debugging runbook: đi từ bằng chứng (evidence / 증거) thời gian chạy (runtime / 런타임) ngược về proof nguồn (source / 소스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 42. môi trường vận hành (production / 운영 환경) debugging runbook: đi từ bằng chứng (evidence / 증거) thời gian chạy (runtime / 런타임) ngược về proof nguồn (source / 소스)

Khi một lỗi “TypeScript lẽ ra phải bắt” xuất hiện, dấu vết (trace / 추적) ngược:

```text
runtime failure
↑ artifact/module actually deployed
↑ serialized/external value actually received
↑ validator/adapter that created trusted value
↑ assertion/declaration/generic proof source
↑ source type model
```

Nếu proof nguồn (source / 소스) là `as`, `any`, ambient `.d.ts` hoặc generated declaration, ưu tiên kiểm tra (audit / 감사) nó trước khi làm kiểu (type / 타입) phức tạp hơn. Nếu proof hoàn toàn do checker suy ra nhưng thời gian chạy (runtime / 런타임) vẫn khác, kiểm tra sản phẩm tạo ra (artifact / 산출물)/phiên bản (version / 버전)/mô-đun (module / 모듈) mismatch. Nếu mô hình (model / 모델) đúng mà temporal hành vi (behavior / 동작) sai, quay về JavaScript tính đồng thời (concurrency / 동시성)/thời gian chạy (runtime / 런타임).

Cấp cao (senior / 시니어) TypeScript là khả năng nối **proof tĩnh** với **bằng chứng (evidence / 증거) động** và biết chính xác chỗ hai thế giới tách nhau.

---

Hoàn tất nhánh học (track / 트랙): quay lại [TypeScript Index](typescript_00_index.md) để rà soát (review / 검토) coverage và glossary.

> **Bàn giao:** Sau **42. môi trường vận hành (production / 운영 환경) debugging runbook: đi từ bằng chứng (evidence / 증거) thời gian chạy (runtime / 런타임) ngược về proof nguồn (source / 소스)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
