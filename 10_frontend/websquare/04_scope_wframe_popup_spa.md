# 04 — phạm vi (scope / 범위), WFrame, Popup & SPA

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Vì sao WebSquare cần phạm vi (scope / 범위)?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. scwin không phải toàn cục (global / 전역) singleton của toàn app** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối scope, WFrame, popup và SPA, để xác định owner của lifecycle, context và state khi nhiều màn hình cùng tồn tại.

## 1. Vì sao WebSquare cần phạm vi (scope / 범위)?

Một enterprise ứng dụng (application / 애플리케이션) hiếm khi chỉ có một page độc lập. Nó có shell, menu, tab, popup, content frame và nhiều màn hình có thể mở đồng thời. Nếu mọi thành phần (component / 컴포넌트) ID và hàm (function / 함수) đều sống ở toàn cục (global / 전역) không gian tên (namespace / 네임스페이스), hai page cùng có `input1` hoặc `scwin.search` sẽ collision.

WebSquare giải quyết bằng **phạm vi (scope / 범위)**. Mỗi page được tải (load / 로드) trong cấu trúc WFrame có thể có một phạm vi (scope / 범위) riêng. thành phần (component / 컴포넌트) và script của page đó được resolve trong phạm vi (scope / 범위) tương ứng.

```text
main page scope
├─ wframeA scope
│  ├─ inputName
│  └─ scwin.search
└─ wframeB scope
   ├─ inputName
   └─ scwin.search
```

Hai `inputName` có cùng logical ID nhưng không phải cùng đối tượng (object / 객체).

> **Nối mạch:** Page scope giải quyết ownership của script và component trong một Page; scwin làm rõ local behavior, còn $p tiếp theo cung cấp utility biết page boundary.

## 2. `scwin` không phải toàn cục (global / 전역) singleton của toàn app

Trong dự án (project / 프로젝트) dùng phạm vi (scope / 범위), `scwin` là phạm vi (scope / 범위) variable của **page hiện tại**. Hai WFrame khác nhau có hai `scwin` khác nhau dù mã (code / 코드) nguồn (source / 소스) đều dùng tên `scwin`.

Điều này giống mô-đun (module / 모듈) instance hơn là một đối tượng (object / 객체) toàn cục (global / 전역) duy nhất. Khi debugging ở console, đừng hỏi “`scwin` có hàm (function / 함수) này không?” trước khi xác định expression đang resolve phạm vi (scope / 범위) nào.

> **Nối mạch:** `scwin` giữ local behavior còn `$p` hiểu page scope; `parent()` tiếp theo là boundary traversal và chỉ nên dùng khi ownership đã rõ.

## 3. `$p` là page-aware utility

WebSquare cho phép dùng `$p` như utility gắn với phạm vi (scope / 범위) hiện tại. Điều này giải quyết vấn đề ngữ cảnh (context / 맥락): cùng một lệnh `parent()` từ hai page con khác nhau phải trả về hai parent khác nhau.

Các API quan trọng về lập luận (reasoning / 추론) gồm:

```javascript
$p.parent();
$p.top();
$p.main();
```

Ngoài ra WFrame/TabControl có `getWindow()` để lấy phạm vi (scope / 범위) đối tượng (object / 객체) của content tương ứng. Đừng học các API này như synonym; chúng biểu diễn quan hệ khác nhau trong page đồ thị (graph / 그래프).

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **3. $p là page-aware utility** đặt tiêu chí; **4. parent(): đi một ranh giới (boundary / 경계) lên** dùng tiêu chí đó để kiểm tra ranh giới, rồi **5. top() và main() không phải lúc nào cũng đồng nghĩa** mở rộng hệ quả.

## 4. `parent()`: đi một ranh giới (boundary / 경계) lên

`$p.parent()` trả phạm vi (scope / 범위) của page cha theo frame relationship.

```javascript
$p.parent().scwin.refreshList();
```

Cách này tốt hơn truy cập thẳng thành phần (component / 컴포넌트) parent:

```javascript
$p.parent().grdUser.setCellData(...); // coupling cao
```

Parent hàm (function / 함수) là đặc tả hợp đồng (contract / 계약). Parent thành phần (component / 컴포넌트) ID là hiện thực (implementation / 구현) detail. Nếu mã (code / 코드) có chuỗi (chain / 사슬) `parent().parent().parent()`, đó là thiết kế (design / 설계) smell vì page đang biết quá nhiều về nesting topology.

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **4. parent(): đi một ranh giới (boundary / 경계) lên** đặt tiêu chí; **5. top() và main() không phải lúc nào cũng đồng nghĩa** dùng tiêu chí đó để kiểm tra ranh giới, rồi **6. getWindow(): tìm đúng phạm vi (scope / 범위) thay vì đoán đường đi** mở rộng hệ quả.

## 5. `top()` và `main()` không phải lúc nào cũng đồng nghĩa

Không nên chọn `top()` chỉ vì “nó chắc tìm được”. Đi thẳng lên top làm page con phụ thuộc ứng dụng (application / 애플리케이션) shell và khó reuse.

Quy tắc (rule / 규칙) lập luận (reasoning / 추론):

```text
Nếu cần parent trực tiếp → parent()
Nếu cần content của frame/tab cụ thể → getWindow() trên owner component
Nếu cần app shell thật sự → main()/top() sau khi hiểu topology và scopeInherit
```

Điểm đặc biệt quan trọng là hành vi (behavior / 동작) của `$p.main()` có thể thay đổi theo `scopeInherit`. Vì vậy không thể định nghĩa `main()` chỉ bằng một câu “luôn trả main page” rồi áp dụng cho mọi WFrame.

> **Nối mạch:** `top()`/`main()` có thể khác topology thực; `getWindow()` cần resolve đúng scope trước khi áp dụng strict boundary và tránh implicit cross-scope lookup.

## 6. `getWindow()`: tìm đúng phạm vi (scope / 범위) thay vì đoán đường đi

WFrame có `getWindow()` trả phạm vi (scope / 범위) đối tượng (object / 객체) của page đang nằm trong WFrame. TabControl cũng có `getWindow(tabId/tabIndex)` cho tab tương ứng ở các bản dựng (build / 빌드) hỗ trợ.

Conceptual example:

```javascript
var detailScope = wframeDetail.getWindow();
detailScope.scwin.loadUser(userId);
```

Mô hình tư duy (mental model / 사고 모델) là **đơn vị sở hữu (owner / 오너) thành phần (component / 컴포넌트) → hiện tại (current / 현재) child phạm vi (scope / 범위)**. Khi content động (dynamic / 동적), đối tượng (object / 객체) này gắn với instance hiện tại chứ không phải tên page vĩnh viễn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **6. getWindow(): tìm đúng phạm vi (scope / 범위) thay vì đoán đường đi** đặt tiêu chí; **7. Strict ranh giới (boundary / 경계) và lý do nên tránh implicit cross-scope lookup** dùng tiêu chí đó để kiểm tra ranh giới, rồi **8. WFrame là composition thành phần nguyên thủy (primitive / 기본 요소), không chỉ iframe đẹp hơn** mở rộng hệ quả.

## 7. Strict ranh giới (boundary / 경계) và lý do nên tránh implicit cross-scope lookup

Nếu thời gian chạy (runtime / 런타임)/cấu hình (config / 설정) cho phép thành phần (component / 컴포넌트) ở phạm vi (scope / 범위) khác được tìm thấy implicit, mã (code / 코드) có thể “vô tình chạy” đến khi page khác có cùng ID hoặc topology đổi. ranh giới (boundary / 경계) rõ làm phụ thuộc (dependency / 의존성) lộ sớm hơn.

Tư duy tương tự strict chế độ (mode / 모드)/kiểu (type / 타입) checking: hạn chế tiện lợi mơ hồ để đổi lấy predictability.

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **7. Strict ranh giới (boundary / 경계) và lý do nên tránh implicit cross-scope lookup** đặt tiêu chí; **8. WFrame là composition thành phần nguyên thủy (primitive / 기본 요소), không chỉ iframe đẹp hơn** dùng tiêu chí đó để kiểm tra ranh giới, rồi **9. setSrc() và vòng đời (lifecycle / 생명주기)** mở rộng hệ quả.

## 8. WFrame là composition thành phần nguyên thủy (primitive / 기본 요소), không chỉ iframe đẹp hơn

WFrame cho phép tải (load / 로드) page nguồn (source / 소스) vào một vùng của page và kết hợp với phạm vi (scope / 범위). Nó giải quyết composition, isolation và điều hướng (navigation / 내비게이션)/reuse. `src` hoặc `setSrc()` thay content mà không cần reload toàn WebSquare engine.

Do đó WFrame là kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계), không chỉ bố cục (layout / 레이아웃) thành phần (component / 컴포넌트).

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **8. WFrame là composition thành phần nguyên thủy (primitive / 기본 요소), không chỉ iframe đẹp hơn** đặt đầu vào cho **9. setSrc() và vòng đời (lifecycle / 생명주기)**, rồi **10. Parameter passing bằng dataObject** mở rộng hệ quả hoặc giới hạn liên quan.

## 9. `setSrc()` và vòng đời (lifecycle / 생명주기)

Khi gọi:

```javascript
wframeDetail.setSrc("/user/detail.xml", options);
```

page mới không xuất hiện đồng bộ như gán một đối tượng (object / 객체) cục bộ (local / 로컬). Engine phải resolve/tải (load / 로드) sản phẩm tạo ra (artifact / 산출물), tạo phạm vi (scope / 범위)/thành phần (component / 컴포넌트)/binding và chạy vòng đời (lifecycle / 생명주기).

Sai mẫu (pattern / 패턴):

```javascript
wframeDetail.setSrc("/user/detail.xml");
var value = wframeDetail.getWindow().inputUserId.getValue();
```

Nếu page chưa ready, đối tượng (object / 객체) chưa tồn tại. Dùng sự kiện (event / 이벤트)/callback vòng đời (lifecycle / 생명주기) phù hợp với thành phần (component / 컴포넌트)/bản dựng (build / 빌드) thay vì delay bằng `setTimeout(500)`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, cơ chế trong **9. setSrc() và vòng đời (lifecycle / 생명주기)** cần được kiểm chứng bằng dấu vết cụ thể; **10. Parameter passing bằng dataObject** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **11. ranh giới (boundary / 경계) dữ liệu (data / 데이터) nên là plain dữ liệu (data / 데이터)** mở rộng hệ quả hoặc giới hạn liên quan.

## 10. Parameter passing bằng `dataObject`

WebSquare hỗ trợ `dataObject` khi tạo WFrame, popup, tab hoặc WindowContainer. Page nhận dữ liệu bằng `$p.getParameter(...)`.

```javascript
var dataObject = {
    type: "json",
    name: "userParam",
    data: {
        userId: "U1001",
        mode: "EDIT"
    }
};

wframeDetail.setSrc("/user/detail.xml", {
    dataObject: dataObject
});
```

Page con:

```javascript
var param = $p.getParameter("userParam");
console.log(param.userId);
```

Điểm quan trọng: parameter là **ranh giới (boundary / 경계) dữ liệu (data / 데이터)**, không phải đường tắt để chia sẻ toàn bộ đối tượng (object / 객체) đồ thị (graph / 그래프) của page cha.

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **10. Parameter passing bằng dataObject** đặt tiêu chí; **11. ranh giới (boundary / 경계) dữ liệu (data / 데이터) nên là plain dữ liệu (data / 데이터)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **12. Callback bằng string/eval là legacy smell** mở rộng hệ quả.

## 11. ranh giới (boundary / 경계) dữ liệu (data / 데이터) nên là plain dữ liệu (data / 데이터)

Hàm (function / 함수), DOM nút (node / 노드), thành phần (component / 컴포넌트) instance, `window` và đối tượng (object / 객체) đồ thị (graph / 그래프) có circular/tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) phức tạp là payload kém cho frame ranh giới (boundary / 경계). Chúng làm quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명) mơ hồ, đồng thời có thể giữ tham chiếu (reference / 참조) sang page đã đóng.

Guide SP5 còn cảnh báo khi gọi hàm (function / 함수) qua Frame không nên gán trực tiếp đối tượng (object / 객체) không phải String/JSON-like ranh giới (boundary / 경계) đối tượng (object / 객체) sang Frame khác theo cách tạo tham chiếu (reference / 참조) lâu dài, vì một số trình duyệt (browser / 브라우저) có thể phát sinh bộ nhớ (memory / 메모리) leak. Ý nghĩa kiến trúc (architecture / 아키텍처) rộng hơn là: **truyền giá trị, không chia sẻ internals**.

```text
Tốt: { userId, mode, filters }
Xấu: { gridInstance, window, childScope, callbackClosure }
```

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **11. ranh giới (boundary / 경계) dữ liệu (data / 데이터) nên là plain dữ liệu (data / 데이터)** đặt tiêu chí; **12. Callback bằng string/eval là legacy smell** dùng tiêu chí đó để kiểm tra ranh giới, rồi **13. Popup là một ranh giới (boundary / 경계) tương tự page con** mở rộng hệ quả.

## 12. Callback bằng string/eval là legacy smell

Một số codebase truyền tên callback dưới dạng string rồi page con `eval` hoặc resolve ngược parent. mẫu (pattern / 패턴) này có rủi ro bảo mật (security / 보안), refactorability và static lập luận (reasoning / 추론).

Nếu dự án (project / 프로젝트) convention bắt buộc dùng, giới hạn callback vào allowlist nội bộ, không eval string từ máy chủ (server / 서버)/người dùng (user / 사용자). Nếu có thể refactor, ưu tiên tường minh (explicit / 명시적) parent API hoặc sự kiện (event / 이벤트)/kết quả (result / 결과) đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **12. Callback bằng string/eval là legacy smell** đặt tiêu chí; **13. Popup là một ranh giới (boundary / 경계) tương tự page con** dùng tiêu chí đó để kiểm tra ranh giới, rồi **14. Popup kết quả (result / 결과) đặc tả hợp đồng (contract / 계약)** mở rộng hệ quả.

## 13. Popup là một ranh giới (boundary / 경계) tương tự page con

`$p.openPopup()` có thể mở page với options và parameter. Hãy coi popup như một mô-đun (module / 모듈) có đầu vào (input / 입력)/đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약).

```javascript
var options = {
    id: "userDetailPopup",
    modal: true,
    width: "720px",
    height: "560px",
    dataObject: {
        type: "json",
        name: "param",
        data: {
            userId: selectedUserId
        }
    }
};

$p.openPopup("/user/detail.xml", options);
```

Popup không nên tự mò khắp parent để lấy 20 thành phần (component / 컴포넌트). Nhận đầu vào (input / 입력) cần thiết qua parameter sẽ giảm coupling.

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **13. Popup là một ranh giới (boundary / 경계) tương tự page con** đặt tiêu chí; **14. Popup kết quả (result / 결과) đặc tả hợp đồng (contract / 계약)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **15. Chọn popup kiểu (type / 타입) theo ranh giới (boundary / 경계) thật** mở rộng hệ quả.

## 14. Popup kết quả (result / 결과) đặc tả hợp đồng (contract / 계약)

Một popup chọn người dùng (user / 사용자) có thể trả:

```javascript
{
    userId: "U1001",
    userName: "Kim"
}
```

Parent nhận kết quả (result / 결과) và tự quyết định cập nhật (update / 업데이트) mô hình (model / 모델) nào. quy tắc (rule / 규칙): **popup nên trả kết quả, không nên điều khiển internals của parent nếu không cần**.

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **14. Popup kết quả (result / 결과) đặc tả hợp đồng (contract / 계약)** đặt tiêu chí; **15. Chọn popup kiểu (type / 타입) theo ranh giới (boundary / 경계) thật** dùng tiêu chí đó để kiểm tra ranh giới, rồi **16. TabControl và WindowContainer cũng tạo page topology** mở rộng hệ quả.

## 15. Chọn popup kiểu (type / 타입) theo ranh giới (boundary / 경계) thật

SP5 guide phân biệt `wframePopup`, `iframePopup` và `browserPopup`, trong đó `wframePopup` được khuyến nghị cho phần lớn màn hình WebSquare vì hỗ trợ phạm vi (scope / 범위) và nằm trong thời gian chạy (runtime / 런타임) composition của ứng dụng (application / 애플리케이션).

`iframePopup` hợp lý hơn khi cần isolation của IFrame, ví dụ tích hợp bên ngoài (external / 외부) lĩnh vực (domain / 도메인)/solution. `browserPopup` tạo bản địa (native / 네이티브) trình duyệt (browser / 브라우저) cửa sổ (window / 윈도우)/tiến trình (process / 프로세스) ranh giới (boundary / 경계) và chỉ nên dùng khi yêu cầu (requirement / 요구사항) thực sự cần cửa sổ riêng.

Đừng chọn IFrame/trình duyệt (browser / 브라우저) popup chỉ vì mã (code / 코드) legacy đã quen `window.parent` hoặc vì nó “dễ tách”. Isolation mạnh hơn cũng kéo theo communication, vòng đời (lifecycle / 생명주기), bảo mật (security / 보안) và debugging chi phí (cost / 비용) lớn hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **15. Chọn popup kiểu (type / 타입) theo ranh giới (boundary / 경계) thật** đặt tiêu chí; **16. TabControl và WindowContainer cũng tạo page topology** dùng tiêu chí đó để kiểm tra ranh giới, rồi **17. SPA trong WebSquare** mở rộng hệ quả.

## 16. TabControl và WindowContainer cũng tạo page topology

Tab/cửa sổ (window / 윈도우) bộ chứa (container / 컨테이너) thường chứa nhiều page. Khi mỗi tab/cửa sổ (window / 윈도우) là WFrame/phạm vi (scope / 범위), cùng một screen có thể tồn tại nhiều instance.

Điều này làm toàn cục (global / 전역) mutable trạng thái (state / 상태) nguy hiểm. Nếu `window.currentUserId` được dùng chung cho mọi tab, tab B có thể ghi đè tab A. Scope-local trạng thái (state / 상태) trong `scwin` hoặc DataCollection của page instance an toàn hơn.

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **17. SPA trong WebSquare** nối từ **16. TabControl và WindowContainer cũng tạo page topology** sang **18. SPA tạo thời gian tồn tại (lifetime / 수명) dài hơn — bộ nhớ (memory / 메모리) leak trở nên quan trọng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. SPA trong WebSquare

Single Page ứng dụng (application / 애플리케이션) ở đây không nhất thiết giống React Router. Ý tưởng chính là **engine shell được giữ lại**, còn content page được thay trong frame/bộ chứa (container / 컨테이너) để tránh reload toàn engine.

```text
websquare engine shell stays alive
        │
        ├─ menu/common state
        ├─ shared resources
        └─ WFrame/tab/window content changes
```

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **18. SPA tạo thời gian tồn tại (lifetime / 수명) dài hơn — bộ nhớ (memory / 메모리) leak trở nên quan trọng** nối từ **17. SPA trong WebSquare** sang **19. scopeInherit: phải hiểu theo hai trục độc lập**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. SPA tạo thời gian tồn tại (lifetime / 수명) dài hơn — bộ nhớ (memory / 메모리) leak trở nên quan trọng

Trong full reload, trình duyệt (browser / 브라우저) giải phóng phần lớn page trạng thái (state / 상태) khi điều hướng (navigation / 내비게이션). Trong SPA, shell có thể sống hàng giờ. Nếu page đăng ký timer, toàn cục (global / 전역) sự kiện (event / 이벤트) listener hoặc giữ tham chiếu (reference / 참조) sang đối tượng (object / 객체) đã đóng mà không cleanup, bộ nhớ (memory / 메모리) tăng dần.

```text
setInterval không clear
window/document listener không unbind
cache global giữ page scope
closure giữ large DataList
popup/frame đóng nhưng reference vẫn tồn tại
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **19. scopeInherit: phải hiểu theo hai trục độc lập** nối từ **18. SPA tạo thời gian tồn tại (lifetime / 수명) dài hơn — bộ nhớ (memory / 메모리) leak trở nên quan trọng** sang **20. recursive là evolution mới và không nên giả định mọi engine có**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. `scopeInherit`: phải hiểu theo hai trục độc lập

SP5 định nghĩa `scopeInherit` không chỉ bằng câu “child inherit parent”. Có hai câu hỏi độc lập:

```text
A. Child có tự động resolve object/component của parent như local không?
B. $p.main() từ child trỏ về parent WFrame area hay top page?
```

Với các option phổ biến:

| `scopeInherit` | Tự động tham chiếu đối tượng (object / 객체) parent | `$p.main()` |
|---|---|---|
| `none` | Không | top page |
| `api` | Không | parent WFrame area |
| `component` | Có | top page |
| `all` | Có | parent WFrame area |

`none` là default trong guide SP5. Bảng này quan trọng vì `api` và `component` cố ý tách hai trục. Nếu chỉ nhớ “all = inherit, none = không” thì bạn chưa hiểu tính năng (feature / 기능).

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **20. recursive là evolution mới và không nên giả định mọi engine có** nối từ **19. scopeInherit: phải hiểu theo hai trục độc lập** sang **21. phạm vi (scope / 범위) inheritance là convenience có sự đánh đổi (trade-off / 트레이드오프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. `recursive` là evolution mới và không nên giả định mọi engine có

Bản phát hành (release / 릴리스) ghi chú (note / 노트) SP5 engine 2026 bổ sung `scopeInherit="recursive"`. Option này cho phép tự động tham chiếu đối tượng (object / 객체) qua các ancestor WFrame cũng cấu hình `recursive`, trong khi `$p.main()` vẫn đi về top page. `all` và `recursive` vì vậy không phải synonym.

Consequence môi trường vận hành (production / 운영 환경): một codebase chạy trên engine trước tính năng (feature / 기능) này không thể dùng `recursive` chỉ vì Studio/documentation mới có. Đây là ví dụ điển hình của nguyên tắc **engine bản dựng (build / 빌드) > tên generation**.

Khi upgrade, regression kiểm thử (test / 테스트) phải có nested topology thật:

```text
Shell
└─ WFrame A
   └─ WFrame B
      └─ WFrame C
```

và xác nhận đối tượng (object / 객체) resolution cùng `$p.main()` ở từng mức (level / 수준).

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **21. phạm vi (scope / 범위) inheritance là convenience có sự đánh đổi (trade-off / 트레이드오프)** nối từ **20. recursive là evolution mới và không nên giả định mọi engine có** sang **22. scopeInherit không chỉ thuộc WFrame tĩnh**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. phạm vi (scope / 범위) inheritance là convenience có sự đánh đổi (trade-off / 트레이드오프)

`scopeInherit="all"` hoặc `recursive` có thể giảm mã (code / 코드) điều hướng (navigation / 내비게이션) nhưng cũng làm phụ thuộc (dependency / 의존성) ẩn. Child gọi `inputParent` như cục bộ (local / 로컬) đối tượng (object / 객체) thì nguồn (source / 소스) tệp (file / 파일) không cho người đọc biết đối tượng (object / 객체) đó thuộc parent.

Với mã (code / 코드) mới, ưu tiên tường minh (explicit / 명시적) page đặc tả hợp đồng (contract / 계약). Dùng inheritance khi dự án (project / 프로젝트) có reason rõ như di chuyển (migration / 마이그레이션), dùng chung (common / 공통) shell convention hoặc composition mẫu (pattern / 패턴) được kiểm soát; đừng dùng để “chữa” mọi lỗi object-not-found.

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **22. scopeInherit không chỉ thuộc WFrame tĩnh** nối từ **21. phạm vi (scope / 범위) inheritance là convenience có sự đánh đổi (trade-off / 트레이드오프)** sang **23. vòng đời (lifecycle / 생명주기) thứ tự (ordering / 순서) giữa parent và child**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. `scopeInherit` không chỉ thuộc WFrame tĩnh

Các SP5 bản dựng (build / 빌드) mới đưa cùng mô hình tư duy (mental model / 사고 모델) inheritance vào WFrame popup, TabControl contents và WindowContainer WFrame. Vì vậy topology có thể đổi hành vi (behavior / 동작) tùy **cách page được host**.

Một screen chạy đúng trong WFrame thường nhưng thất bại (fail / 실패) khi mở trong popup/tab có thể không phải bug của screen lô-gic (logic / 논리); host options có thể tạo phạm vi (scope / 범위) relationship khác.

Đây là lý do kiểm thử (test / 테스트) reusable screen ở nhiều host topology thay vì chỉ kiểm thử (test / 테스트) một đường điều hướng (navigation / 내비게이션).

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **22. scopeInherit không chỉ thuộc WFrame tĩnh** đặt đầu vào cho **23. vòng đời (lifecycle / 생명주기) thứ tự (ordering / 순서) giữa parent và child**, rồi **24. onpageload chỉ chứng minh page vòng đời (lifecycle / 생명주기) đã đến một mốc** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. vòng đời (lifecycle / 생명주기) thứ tự (ordering / 순서) giữa parent và child

Một parent page có thể tải (load / 로드) WFrame; child lại tải (load / 로드) DataCollection/Submission; parent muốn gọi child sau khi sẵn sàng. Đây là phân tán (distributed / 분산) vòng đời (lifecycle / 생명주기) trong cùng trình duyệt (browser / 브라우저).

```text
parent script parsed
≠ parent rendered
≠ child source requested
≠ child scope ready
≠ child UI ready
≠ child data ready
```

Nếu parent cần child “ready with dữ liệu (data / 데이터)”, hãy định nghĩa ready đặc tả hợp đồng (contract / 계약) ở đúng mức, không chỉ frame-load nếu dữ liệu (data / 데이터) tải (load / 로드) còn asynchronous.

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **23. vòng đời (lifecycle / 생명주기) thứ tự (ordering / 순서) giữa parent và child** đặt đầu vào cho **24. onpageload chỉ chứng minh page vòng đời (lifecycle / 생명주기) đã đến một mốc**, rồi **25. động (dynamic / 동적) page instance và stale tham chiếu (reference / 참조)** mở rộng hệ quả hoặc giới hạn liên quan.

## 24. `onpageload` chỉ chứng minh page vòng đời (lifecycle / 생명주기) đã đến một mốc

SP5 guide mô tả `scwin.onpageload` là sự kiện (event / 이벤트) chạy sau page loading. Điều đó hữu ích nhưng không có nghĩa mọi nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) async đã sẵn sàng. Nếu `onpageload` tự execute Submission, callback của Submission vẫn là một readiness stage khác.

Do đó nên đặt tên trạng thái (state / 상태) rõ:

```text
pageReady
referenceDataReady
businessDataReady
interactiveReady
```

thay vì một boolean `loaded` dùng cho mọi thứ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **24. onpageload chỉ chứng minh page vòng đời (lifecycle / 생명주기) đã đến một mốc** đặt đầu vào cho **25. động (dynamic / 동적) page instance và stale tham chiếu (reference / 참조)**, rồi **26. Cross-scope lời gọi (call / 호출) là synchronous hay asynchronous?** mở rộng hệ quả hoặc giới hạn liên quan.

## 25. động (dynamic / 동적) page instance và stale tham chiếu (reference / 참조)

Giả sử:

```javascript
var detail = wframeDetail.getWindow();
```

Sau đó `wframeDetail.setSrc()` chuyển sang page khác. Biến `detail` cũ có thể trỏ phạm vi (scope / 범위) không còn đại diện hiện tại (current / 현재) page.

Nếu topology động (dynamic / 동적), resolve phạm vi (scope / 범위) gần thời điểm sử dụng thay vì bộ nhớ đệm (cache / 캐시) vô thời hạn. Nếu buộc bộ nhớ đệm (cache / 캐시), bộ nhớ đệm (cache / 캐시) phải có vô hiệu hóa (invalidation / 무효화) theo vòng đời (lifecycle / 생명주기).

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **26. Cross-scope lời gọi (call / 호출) là synchronous hay asynchronous?** nối từ **25. động (dynamic / 동적) page instance và stale tham chiếu (reference / 참조)** sang **27. lỗi (error / 오류) handling qua frame ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Cross-scope lời gọi (call / 호출) là synchronous hay asynchronous?

Nếu hai phạm vi (scope / 범위) đã tồn tại trong cùng JavaScript thời gian chạy (runtime / 런타임) và bạn gọi trực tiếp hàm (function / 함수), lời gọi (call / 호출) bản thân nó thường synchronous như JavaScript bình thường. Nhưng hàm (function / 함수) bên kia có thể bắt đầu Submission hoặc frame tải (load / 로드) async.

```javascript
$p.parent().scwin.refresh();
// refresh() có thể chỉ schedule network call rồi return ngay
```

Đừng nhầm “hàm (function / 함수) lời gọi (call / 호출) synchronous” với “nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) synchronous”.

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **26. Cross-scope lời gọi (call / 호출) là synchronous hay asynchronous?** đặt tiêu chí; **27. lỗi (error / 오류) handling qua frame ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **28. gỡ lỗi (debug / 디버그) phạm vi (scope / 범위) bằng DOM element** mở rộng hệ quả.

## 27. lỗi (error / 오류) handling qua frame ranh giới (boundary / 경계)

Nếu child gọi parent hàm (function / 함수) và parent throw exception ngay, exception có thể bubble theo JavaScript lời gọi (call / 호출) đường dẫn (path / 경로). Nhưng mạng (network / 네트워크)/vòng đời (lifecycle / 생명주기) lỗi (error / 오류) xảy ra sau đó không thể catch bằng outer `try/catch` quanh hàm (function / 함수) lời gọi (call / 호출).

Async thất bại (failure / 실패) phải được xử lý ở callback/sự kiện (event / 이벤트) tương ứng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **27. lỗi (error / 오류) handling qua frame ranh giới (boundary / 경계)** đặt tiêu chí; **28. gỡ lỗi (debug / 디버그) phạm vi (scope / 범위) bằng DOM element** dùng tiêu chí đó để kiểm tra ranh giới, rồi **29. Anti-pattern: singleton dùng chung (common / 공통) đối tượng (object / 객체) biết mọi screen** mở rộng hệ quả.

## 28. gỡ lỗi (debug / 디버그) phạm vi (scope / 범위) bằng DOM element

SP5 có gỡ lỗi (debug / 디버그) utility như `$p.debug.getScope($0)` và `$p.debug.getFrame($0)` ở các bản dựng (build / 빌드) tương ứng. Đây là công cụ hữu ích khi nhìn một element nhưng không biết nó thuộc WFrame nào.

```text
Inspect element
→ $0
→ resolve WebSquare scope/frame
→ inspect scwin/component/DataCollection trong đúng scope
```

Đừng đoán bằng vật lý (physical / 물리적) DOM id.

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **29. Anti-pattern: singleton dùng chung (common / 공통) đối tượng (object / 객체) biết mọi screen** nối từ **28. gỡ lỗi (debug / 디버그) phạm vi (scope / 범위) bằng DOM element** sang **30. Anti-pattern: dùng top() để “chữa” lỗi phạm vi (scope / 범위)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Anti-pattern: singleton dùng chung (common / 공통) đối tượng (object / 객체) biết mọi screen

Một số dự án (project / 프로젝트) tạo `com`/`gcm` toàn cục (global / 전역) utility rồi dần biến nó thành đối tượng (object / 객체) biết ID và hành vi (behavior / 동작) của mọi page. dùng chung (common / 공통) utility hợp lý cho logging, message, date formatting, submission wrapper hoặc auth ngữ cảnh (context / 맥락). Nhưng screen-specific lô-gic (logic / 논리) không nên chảy hết vào toàn cục (global / 전역) god đối tượng (object / 객체).

Dùng chung (common / 공통) mô-đun (module / 모듈) nên phụ thuộc lớp trừu tượng (abstraction / 추상화) ổn định; screen/lĩnh vực (domain / 도메인) lô-gic (logic / 논리) ở screen/lĩnh vực (domain / 도메인) mô-đun (module / 모듈).

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **30. Anti-pattern: dùng top() để “chữa” lỗi phạm vi (scope / 범위)** nối từ **29. Anti-pattern: singleton dùng chung (common / 공통) đối tượng (object / 객체) biết mọi screen** sang **31. Thiết kế page đặc tả hợp đồng (contract / 계약) như hàm (function / 함수) đặc tả hợp đồng (contract / 계약)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Anti-pattern: dùng `top()` để “chữa” lỗi phạm vi (scope / 범위)

Khi thành phần (component / 컴포넌트) cục bộ (local / 로컬) không tìm thấy, nhà phát triển (developer / 개발자) có thể thử `$p.top().someComponent`. Nếu chạy, bug tạm biến mất nhưng phụ thuộc (dependency / 의존성) bị đẩy lên app shell.

Trước khi dùng `top()`, trả lời đối tượng (object / 객체) thực sự thuộc page nào, vì sao hiện tại (current / 현재) page cần nó và có công khai (public / 공개) hàm (function / 함수)/dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) thay cho thành phần (component / 컴포넌트) truy cập (access / 접근) không.

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **31. Thiết kế page đặc tả hợp đồng (contract / 계약) như hàm (function / 함수) đặc tả hợp đồng (contract / 계약)** nối từ **30. Anti-pattern: dùng top() để “chữa” lỗi phạm vi (scope / 범위)** sang **32. Ví dụ: tìm kiếm (search / 검색) → Detail popup → Refresh**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Thiết kế page đặc tả hợp đồng (contract / 계약) như hàm (function / 함수) đặc tả hợp đồng (contract / 계약)

Hãy coi một page con như hàm (function / 함수):

```text
Input: parameter/dataObject
Internal state: scwin + DataCollection
Output: result/event/public API
Side effects: Submission / navigation
Lifetime: create → ready stages → dispose
```

Một page đặc tả hợp đồng (contract / 계약) tốt giúp screen reuse được ở tab, popup hoặc WFrame khác mà không phụ thuộc parent cấu trúc (structure / 구조) cụ thể.

> **Nối mạch:** Trong **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **31. Thiết kế page đặc tả hợp đồng (contract / 계약) như hàm (function / 함수) đặc tả hợp đồng (contract / 계약)** nêu quy tắc; **32. Ví dụ: tìm kiếm (search / 검색) → Detail popup → Refresh** thử quy tắc trong tình huống, rồi **33. môi trường vận hành (production / 운영 환경) checklist cho phạm vi (scope / 범위) kiến trúc (architecture / 아키텍처)** mở rộng hệ quả.

## 32. Ví dụ: tìm kiếm (search / 검색) → Detail popup → Refresh

```text
List page
  │ selected userId
  ▼
open Detail popup(userId)
  │
  ▼
Detail page loads user
  │ user edits + saves
  ▼
popup returns { changed: true, userId }
  │
  ▼
List page decides to re-query
```

Popup không cần biết GridView của parent tên gì. Parent không cần biết nội bộ (internal / 내부) thành phần (component / 컴포넌트) của popup.

> **Nối mạch:** Ở chặng này của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **32. Ví dụ: tìm kiếm (search / 검색) → Detail popup → Refresh** nêu quy tắc; **33. môi trường vận hành (production / 운영 환경) checklist cho phạm vi (scope / 범위) kiến trúc (architecture / 아키텍처)** thử quy tắc trong tình huống, rồi **34. Kết nối** mở rộng hệ quả.

## 33. môi trường vận hành (production / 운영 환경) checklist cho phạm vi (scope / 범위) kiến trúc (architecture / 아키텍처)

Trước khi merge screen mới, kiểm tra page có truy cập thành phần (component / 컴포넌트) ngoài phạm vi (scope / 범위) trực tiếp không; có chuỗi (chain / 사슬) parent dài không; `scopeInherit` có làm phụ thuộc (dependency / 의존성) ẩn không; host popup/tab/cửa sổ (window / 윈도우) có cùng topology giả định (assumption / 가정) không; parameter có chứa đối tượng (object / 객체)/tham chiếu (reference / 참조) khó quản thời gian tồn tại (lifetime / 수명) không; toàn cục (global / 전역) mutable trạng thái (state / 상태) có bị dùng chung giữa nhiều instance không; frame tải (load / 로드) có race với mã (code / 코드) gọi child không; và SPA page có cleanup timer/listener/tài nguyên (resource / 자원) không.

> **Nối mạch:** Đặt trong câu hỏi lớn của **04 — phạm vi (scope / 범위), WFrame, Popup & SPA**, **34. Kết nối** nối từ **33. môi trường vận hành (production / 운영 환경) checklist cho phạm vi (scope / 범위) kiến trúc (architecture / 아키텍처)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 34. Kết nối

Sau khi hiểu phạm vi (scope / 범위), bạn có thể lập luận (reasoning / 추론) GridView/CRUD trong screen lớn mà không nhầm mô hình dữ liệu (data model / 데이터 모델) và page instance. Tiếp theo: [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md).

Để hiểu object-ready/render-ready/preload sâu hơn, đọc [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md). Để regression-test nested WFrame, popup và host topology, đọc [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md).

> **Bàn giao:** Sau **34. Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
