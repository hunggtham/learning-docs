# 14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Shell là thời gian chạy (runtime / 런타임) host, không phải “page cha biết mọi thứ”** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Screen definition khác screen instance** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối application shell với screen definition và screen instance, giúp phân biệt nơi sở hữu navigation, tab reuse và state.

WebSquare enterprise ứng dụng (application / 애플리케이션) thường không phải tập hợp các XML page độc lập. Phía trên các screen nghiệp vụ còn có **ứng dụng (application / 애플리케이션) shell**: menu, header, tab/cửa sổ (window / 윈도우) bộ chứa (container / 컨테이너), permission ngữ cảnh (context / 맥락), toàn cục (global / 전역) message/loading tầng (layer / 계층), điều hướng (navigation / 내비게이션) lịch sử (history / 이력) và cơ chế mở/đóng/reuse screen.

Chapter 04 đã giải thích phạm vi (scope / 범위)/WFrame ở mức page composition. Chapter này đi lên một tầng kiến trúc (architecture / 아키텍처): **khi hàng chục hoặc hàng trăm screen cùng sống trong một shell, ai sở hữu điều hướng (navigation / 내비게이션) trạng thái (state / 상태), page instance được định danh thế nào, khi nào reuse tab, khi nào tạo instance mới, và trạng thái (state / 상태) nào được phép toàn cục (global / 전역)?**

## 1. Shell là thời gian chạy (runtime / 런타임) host, không phải “page cha biết mọi thứ”

Mô hình tư duy (mental model / 사고 모델) tốt:

```text
Application Shell
├─ authentication/session context
├─ menu/navigation registry
├─ tab/window host
├─ common message/loading service
└─ screen instances
   ├─ customer-list scope
   ├─ customer-detail scope
   └─ order-list scope
```

Shell cung cấp năng lực (capability / 역량) chung. Screen nghiệp vụ giữ nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) của chính nó. Nếu shell biết ID của mọi Grid/đầu vào (input / 입력) trong mọi screen, kiến trúc (architecture / 아키텍처) đã đảo ngược phụ thuộc (dependency / 의존성).

Shell nên biết **screen đặc tả hợp đồng (contract / 계약)**, không biết **screen internals**.

> **Nối mạch:** Shell là runtime host; screen definition mô tả loại màn hình, còn screen instance mang lifecycle cụ thể. Navigation identity tiếp theo phải gắn với instance đó.

## 2. Screen definition khác screen instance

`/ui/order/list.xml` là screen definition/nguồn (source / 소스). Khi mở nó hai lần với hai parameter khác nhau, có thể có hai instance.

```text
screen definition: order/list.xml

instance A: order/list.xml?customer=C001
instance B: order/list.xml?customer=C999
```

Trong WFrame/phạm vi (scope / 범위) kiến trúc (architecture / 아키텍처), mỗi instance có thể có `scwin`, DataCollection, hiện tại (current / 현재) row, pending Submission và unsaved trạng thái (state / 상태) riêng.

Nếu điều hướng (navigation / 내비게이션) registry chỉ key theo nguồn (source / 소스) đường dẫn (path / 경로), instance B có thể vô tình activate A. Vì vậy cần quyết định định danh (identity / 식별자) chính sách (policy / 정책) của screen.

> **Nối mạch:** Screen instance là đối tượng runtime; navigation identity phải được tạo từ rule ổn định để `openAction/reuse` không mở nhầm hoặc nhân bản màn hình.

## 3. điều hướng (navigation / 내비게이션) định danh (identity / 식별자) là sản phẩm (product / 제품) quy tắc (rule / 규칙)

Một menu “Employee Management” có thể chỉ cho phép một tab duy nhất. Một màn hình “thứ tự (order / 순서) Detail” có thể cho phép nhiều thứ tự (order / 순서) mở song song.

Do đó tab/cửa sổ (window / 윈도우) key nên phản ánh intent:

```text
single-instance screen
key = MENU_EMPLOYEE

multi-instance detail
key = ORDER_DETAIL:ORD-1001
key = ORDER_DETAIL:ORD-1002
```

Không có một key chiến lược (strategy / 전략) đúng cho mọi screen. Nhưng chiến lược (strategy / 전략) phải tường minh (explicit / 명시적) để tránh duplicate tab hoặc reuse nhầm trạng thái (state / 상태).

> **Nối mạch:** Navigation identity quyết định reuse policy; TabControl và WindowContainer tiếp theo là hai host có lifecycle khác nhau, nên phải chọn owner instance rõ.

## 4. `openAction`/reuse chính sách (policy / 정책) phải khớp định danh (identity / 식별자) chính sách (policy / 정책)

TabControl/WindowContainer có option để quyết định hành vi (behavior / 동작) khi mục tiêu (target / 대상) đã tồn tại tùy API/bản dựng (build / 빌드). Đừng chọn “exist/reuse” chỉ vì muốn tránh mở nhiều tab.

Reuse chỉ đúng nếu existing instance đại diện cùng logical tác vụ (task / 작업). Nếu người dùng (user / 사용자) mở detail của thực thể (entity / 엔터티) khác mà app chỉ focus tab cũ không reload parameter, UI sẽ hiển thị thực thể (entity / 엔터티) sai.

Lập luận (reasoning / 추론) trước khi mở:

```text
logical key đã tồn tại?
→ có: activate hay refresh/reparameterize?
→ không: create instance mới
```

> **Nối mạch:** Trong **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **4. openAction/reuse chính sách (policy / 정책) phải khớp định danh (identity / 식별자) chính sách (policy / 정책)** đặt đầu vào cho **5. TabControl và WindowContainer là host có vòng đời (lifecycle / 생명주기)**, rồi **6. dataObject là điều hướng (navigation / 내비게이션) đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약)** mở rộng hệ quả hoặc giới hạn liên quan.

## 5. TabControl và WindowContainer là host có vòng đời (lifecycle / 생명주기)

SP5 hỗ trợ `wframe` frame chế độ (mode / 모드) cho TabControl/WindowContainer để screen có phạm vi (scope / 범위) riêng. WindowContainer còn phục vụ MDI-style cửa sổ (window / 윈도우) hierarchy. Đây không chỉ là bố cục (layout / 레이아웃) choice; nó quyết định isolation, `getWindow()` ngữ nghĩa (semantics / 의미론) và cleanup ranh giới (boundary / 경계).

Khi tạo tab/cửa sổ (window / 윈도우) bằng `src`, screen cần thời gian tải (load / 로드). Shell không được giả định `addTab()`/`createWindow()` return là nghiệp vụ (business / 비즈니스) screen đã data-ready.

```text
container created
→ WFrame source load
→ Scope/object ready
→ render ready
→ screen init
→ initial Submission
→ business data ready
```

Nếu shell cần gọi screen sau tải (load / 로드), hãy dùng ready đặc tả hợp đồng (contract / 계약) phù hợp thay vì timer.

> **Nối mạch:** Ở chặng này của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, cơ chế trong **5. TabControl và WindowContainer là host có vòng đời (lifecycle / 생명주기)** cần được kiểm chứng bằng dấu vết cụ thể; **6. dataObject là điều hướng (navigation / 내비게이션) đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **7. điều hướng (navigation / 내비게이션) command tốt hơn direct bộ chứa (container / 컨테이너) manipulation rải rác** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. `dataObject` là điều hướng (navigation / 내비게이션) đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약)

Khi shell mở screen, parameter nên là plain dữ liệu (data / 데이터):

```javascript
var dataObject = {
    type: "json",
    name: "pageParam",
    data: {
        orderId: "ORD-1001",
        mode: "EDIT"
    }
};
```

Screen đọc bằng `$p.getParameter()` theo đặc tả hợp đồng (contract / 계약) của bản dựng (build / 빌드).

Parameter nên mô tả **ý định mở screen**, không truyền thành phần (component / 컴포넌트) instance hoặc mutable đối tượng (object / 객체) của parent. Điều này cho phép cùng screen được host bởi TabControl, WindowContainer hoặc popup mà không biết topology cụ thể.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **7. điều hướng (navigation / 내비게이션) command tốt hơn direct bộ chứa (container / 컨테이너) manipulation rải rác** nối từ **6. dataObject là điều hướng (navigation / 내비게이션) đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약)** sang **8. toàn cục (global / 전역) trạng thái (state / 상태) phải nhỏ và có đơn vị sở hữu (owner / 오너) rõ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. điều hướng (navigation / 내비게이션) command tốt hơn direct bộ chứa (container / 컨테이너) manipulation rải rác

Nếu mọi screen tự gọi `mainTab.addTab(...)` với option khác nhau, điều hướng (navigation / 내비게이션) chính sách (policy / 정책) bị phân tán.

Một dùng chung (common / 공통) điều hướng (navigation / 내비게이션) dịch vụ (service / 서비스) có thể expose năng lực (capability / 역량):

```javascript
appNav.openScreen({
    screenId: "ORDER_DETAIL",
    instanceKey: orderId,
    params: { orderId: orderId }
});
```

Bên trong dịch vụ (service / 서비스) mới quyết định bộ chứa (container / 컨테이너), tab ID, title, duplicate chính sách (policy / 정책) và telemetry.

Điểm quan trọng là dùng chung (common / 공통) dịch vụ (service / 서비스) không được biết `grdOrder` hoặc `dmSearch` của screen. Nó quản điều hướng (navigation / 내비게이션), không quản nghiệp vụ (business / 비즈니스) UI.

> **Nối mạch:** Trong **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, sau nội dung của **7. điều hướng (navigation / 내비게이션) command tốt hơn direct bộ chứa (container / 컨테이너) manipulation rải rác**, **8. toàn cục (global / 전역) trạng thái (state / 상태) phải nhỏ và có đơn vị sở hữu (owner / 오너) rõ** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **9. Permission menu khác authorization** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. toàn cục (global / 전역) trạng thái (state / 상태) phải nhỏ và có đơn vị sở hữu (owner / 오너) rõ

Một số trạng thái (state / 상태) hợp lý ở shell/session mức (level / 수준):

```text
current authenticated user identity
locale/theme
menu/permission snapshot
feature/config flags phù hợp client
navigation registry
correlation/session metadata không nhạy cảm
```

Trạng thái (state / 상태) không nên toàn cục (global / 전역) tùy tiện:

```text
current selected customer của một tab
search condition của một screen
Grid row index
popup temporary form
pending Save flag của một page
```

Toàn cục (global / 전역) mutable trạng thái (state / 상태) làm nhiều instance ghi đè nhau và kéo thời gian tồn tại (lifetime / 수명) đối tượng (object / 객체) dài hơn cần thiết.

> **Nối mạch:** Ở chặng này của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **9. Permission menu khác authorization** nối từ **8. toàn cục (global / 전역) trạng thái (state / 상태) phải nhỏ và có đơn vị sở hữu (owner / 오너) rõ** sang **10. Unsaved-change guard thuộc điều hướng (navigation / 내비게이션) giao thức (protocol / 프로토콜)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Permission menu khác authorization

Shell thường ẩn menu người dùng (user / 사용자) không có quyền. Đây là UX/điều hướng (navigation / 내비게이션) filtering, không phải ranh giới bảo mật (security boundary / 보안 경계).

```text
menu permission → user có thấy/mở screen dễ dàng không
server authorization → request có được phép thực thi không
```

Người dùng (user / 사용자) có thể gọi endpoint trực tiếp hoặc sửa máy khách (client / 클라이언트) trạng thái (state / 상태). máy chủ (server / 서버) vẫn phải enforce permission.

Menu bộ nhớ đệm (cache / 캐시) cũng cần vô hiệu hóa (invalidation / 무효화) chính sách (policy / 정책) nếu quyền có thể thay đổi trong session.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **10. Unsaved-change guard thuộc điều hướng (navigation / 내비게이션) giao thức (protocol / 프로토콜)** nối từ **9. Permission menu khác authorization** sang **11. Close không đồng nghĩa đối tượng (object / 객체) đã garbage-collected**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Unsaved-change guard thuộc điều hướng (navigation / 내비게이션) giao thức (protocol / 프로토콜)

Nếu người dùng (user / 사용자) đóng tab đang có dirty DataList, screen biết “tôi có unsaved thay đổi (change / 변경)”, còn shell biết “người dùng (user / 사용자) đang yêu cầu close/điều hướng (navigation / 내비게이션)”. Hai bên cần đặc tả hợp đồng (contract / 계약).

Mẫu (pattern / 패턴) tốt:

```text
shell asks screen: canClose?
screen checks dirty state
→ yes: close
→ no/confirm required: prompt/decision
```

Mẫu (pattern / 패턴) xấu là shell tự inspect mọi `dl*` đối tượng (object / 객체) của child. Điều đó couple shell vào hiện thực (implementation / 구현) screen.

Screen có thể expose công khai (public / 공개) hàm (function / 함수):

```javascript
scwin.canClose = function () {
    return !scwin.hasUnsavedChanges();
};
```

Chính xác (exact / 정확한) invocation qua phạm vi (scope / 범위)/bộ chứa (container / 컨테이너) phụ thuộc topology, nhưng quyền sở hữu (ownership / 소유권) rõ: screen đánh giá nghiệp vụ (business / 비즈니스) trạng thái (state / 상태), shell điều phối điều hướng (navigation / 내비게이션).

> **Nối mạch:** Trong **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **11. Close không đồng nghĩa đối tượng (object / 객체) đã garbage-collected** nối từ **10. Unsaved-change guard thuộc điều hướng (navigation / 내비게이션) giao thức (protocol / 프로토콜)** sang **12. Reuse tab và refresh trạng thái (state / 상태) phải có đặc tả hợp đồng (contract / 계약)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Close không đồng nghĩa đối tượng (object / 객체) đã garbage-collected

Khi tab/cửa sổ (window / 윈도우) đóng, UI biến mất nhưng bộ nhớ (memory / 메모리) chỉ được giải phóng khi không còn tham chiếu (reference / 참조) reachable.

Nếu shell giữ registry:

```javascript
scwin.openScreens[screenKey] = childScope;
```

mà không remove entry khi close, child phạm vi (scope / 범위) có thể bị giữ sống. Registry nên giữ siêu dữ liệu (metadata / 메타데이터)/định danh (identity / 식별자) tối thiểu hoặc cleanup tham chiếu (reference / 참조) đúng vòng đời (lifecycle / 생명주기).

Đây là liên kết (connection / 연결) trực tiếp với chapter 10 về tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명).

> **Nối mạch:** Ở chặng này của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **12. Reuse tab và refresh trạng thái (state / 상태) phải có đặc tả hợp đồng (contract / 계약)** nối từ **11. Close không đồng nghĩa đối tượng (object / 객체) đã garbage-collected** sang **13. Back/forward lịch sử (history / 이력) cần định nghĩa ngữ nghĩa (semantic / 의미적)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Reuse tab và refresh trạng thái (state / 상태) phải có đặc tả hợp đồng (contract / 계약)

Giả sử tab thứ tự (order / 순서) danh sách (list / 목록) đã mở. người dùng (user / 사용자) từ menu khác yêu cầu mở lại với filter mới.

Có ba chính sách (policy / 정책) khác nhau:

```text
activate only
activate + refresh with new params
close old + create new instance
```

Không nên ngầm chọn một. Nếu refresh, screen cần công khai (public / 공개) năng lực (capability / 역량) như `applyNavigation(params)` thay vì shell set trực tiếp `dmSearch` và click button hộ.

```javascript
scwin.applyNavigation = function (params) {
    scwin.setSearchCondition(params);
    scwin.search();
};
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **13. Back/forward lịch sử (history / 이력) cần định nghĩa ngữ nghĩa (semantic / 의미적)** nối từ **12. Reuse tab và refresh trạng thái (state / 상태) phải có đặc tả hợp đồng (contract / 계약)** sang **14. Deep link cần tách tuyến (route / 경로) định danh (identity / 식별자) và thời gian chạy (runtime / 런타임) instance**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Back/forward lịch sử (history / 이력) cần định nghĩa ngữ nghĩa (semantic / 의미적)

SPA shell giữ engine sống nên trình duyệt (browser / 브라우저) lịch sử (history / 이력) không tự động hiểu mọi tab switch là điều hướng (navigation / 내비게이션) meaningful. Legacy IFrame còn có lịch sử (history / 이력) riêng.

Trước khi thêm back button, xác định:

```text
browser Back quay route/screen nào?
tab switch có push history không?
popup có history không?
filter/search có history không?
```

Không cố map mọi UI trạng thái (state / 상태) vào URL/lịch sử (history / 이력). Chỉ trạng thái (state / 상태) cần deep-link/khôi phục (recovery / 복구)/share mới nên có điều hướng (navigation / 내비게이션) biểu diễn (representation / 표현) ổn định.

> **Nối mạch:** Trong **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **14. Deep link cần tách tuyến (route / 경로) định danh (identity / 식별자) và thời gian chạy (runtime / 런타임) instance** nối từ **13. Back/forward lịch sử (history / 이력) cần định nghĩa ngữ nghĩa (semantic / 의미적)** sang **15. Menu siêu dữ liệu (metadata / 메타데이터) không nên trở thành god cấu hình (configuration / 구성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Deep link cần tách tuyến (route / 경로) định danh (identity / 식별자) và thời gian chạy (runtime / 런타임) instance

Một deep link có thể biểu diễn:

```text
screen = ORDER_DETAIL
orderId = ORD-1001
```

Khi app boot, shell resolve permission, tải (load / 로드) screen definition, tạo instance rồi truyền parameter. URL không nên chứa vật lý (physical / 물리적) WFrame ID sinh ngẫu nhiên hay Grid row chỉ mục (index / 인덱스).

Stable tuyến (route / 경로) dùng nghiệp vụ (business / 비즈니스)/điều hướng (navigation / 내비게이션) định danh (identity / 식별자); thời gian chạy (runtime / 런타임) ID chỉ là hiện thực (implementation / 구현) detail.

> **Nối mạch:** Ở chặng này của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **14. Deep link cần tách tuyến (route / 경로) định danh (identity / 식별자) và thời gian chạy (runtime / 런타임) instance** đặt vấn đề; **15. Menu siêu dữ liệu (metadata / 메타데이터) không nên trở thành god cấu hình (configuration / 구성)** đối chiếu bằng chứng, rồi **16. Loading indicator cần đúng ranh giới (boundary / 경계)** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. Menu siêu dữ liệu (metadata / 메타데이터) không nên trở thành god cấu hình (configuration / 구성)

Enterprise app thường có menu bảng (table / 테이블) chứa screen URL, title, permission, icon, open chế độ (mode / 모드). siêu dữ liệu (metadata / 메타데이터) hữu ích nhưng nếu nhét mọi hành vi (behavior / 동작) nghiệp vụ (business / 비즈니스) vào menu cấu hình (config / 설정), debugging trở nên khó.

Menu siêu dữ liệu (metadata / 메타데이터) nên trả lời điều hướng (navigation / 내비게이션) concern. Screen hành vi (behavior / 동작) vẫn thuộc screen/lĩnh vực (domain / 도메인) mã (code / 코드).

```text
menu config: screenId, src, title, single/multi-instance
screen code: validation, DataCollection, Submission, CRUD
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **15. Menu siêu dữ liệu (metadata / 메타데이터) không nên trở thành god cấu hình (configuration / 구성)** đặt tiêu chí; **16. Loading indicator cần đúng ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **17. Concurrent tabs làm race điều kiện (condition / 조건) rõ hơn** mở rộng hệ quả.

## 16. Loading indicator cần đúng ranh giới (boundary / 경계)

Một toàn cục (global / 전역) spinner cho mọi yêu cầu (request / 요청) có thể tạo UX khó hiểu: background refresh ở tab A làm khối (block / 블록) tab B. Ngược lại, spinner chỉ trong Grid có thể không đủ cho thao tác (operation / 연산) khóa toàn screen.

Chọn loading phạm vi (scope / 범위) theo thao tác (operation / 연산) quyền sở hữu (ownership / 소유권):

```text
component-level
screen/WFrame-level
application-level
```

TabControl/WindowContainer có cơ chế (mechanism / 메커니즘) hiển thị tiến trình (process / 프로세스) message trong frame ở các cấu hình (configuration / 구성) tương ứng. Hãy dùng ranh giới (boundary / 경계) phù hợp thay vì một toàn cục (global / 전역) boolean duy nhất.

> **Nối mạch:** Trong **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **16. Loading indicator cần đúng ranh giới (boundary / 경계)** đặt tiêu chí; **17. Concurrent tabs làm race điều kiện (condition / 조건) rõ hơn** dùng tiêu chí đó để kiểm tra ranh giới, rồi **18. Cross-screen communication nên qua intent/sự kiện (event / 이벤트), không qua internals** mở rộng hệ quả.

## 17. Concurrent tabs làm race điều kiện (condition / 조건) rõ hơn

Hai tab cùng gọi endpoint không nhất thiết có vấn đề. Vấn đề xảy ra khi chúng chia sẻ mutable máy khách (client / 클라이언트) trạng thái (state / 상태) hoặc máy chủ (server / 서버) thao tác (operation / 연산) không hỗ trợ tính đồng thời (concurrency / 동시성).

Ví dụ:

```text
Tab A edit customer C001
Tab B cũng edit C001
```

Máy khách (client / 클라이언트) phạm vi (scope / 범위) isolation giữ hai form riêng, nhưng máy chủ (server / 서버) vẫn cần optimistic locking/phiên bản (version / 버전). WFrame isolation không giải quyết cơ sở dữ liệu (database / 데이터베이스) tính đồng thời (concurrency / 동시성).

> **Nối mạch:** Ở chặng này của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **18. Cross-screen communication nên qua intent/sự kiện (event / 이벤트), không qua internals** nối từ **17. Concurrent tabs làm race điều kiện (condition / 조건) rõ hơn** sang **19. Broadcast sự kiện (event / 이벤트) cũng có sự đánh đổi (trade-off / 트레이드오프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Cross-screen communication nên qua intent/sự kiện (event / 이벤트), không qua internals

Trường hợp (case / 사례): Detail popup save xong, danh sách (list / 목록) tab cần refresh.

Đặc tả hợp đồng (contract / 계약) tốt:

```text
Detail emits/returns { type: "ORDER_CHANGED", orderId }
List decides whether/how to refresh
```

Đặc tả hợp đồng (contract / 계약) xấu:

```text
Detail finds top tab
→ finds list frame
→ finds grdOrder
→ mutates row 7
```

Đặc tả hợp đồng (contract / 계약) tốt giữ quyền sở hữu (ownership / 소유권) và cho danh sách (list / 목록) quyết định re-query hay cục bộ (local / 로컬) patch.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **19. Broadcast sự kiện (event / 이벤트) cũng có sự đánh đổi (trade-off / 트레이드오프)** nối từ **18. Cross-screen communication nên qua intent/sự kiện (event / 이벤트), không qua internals** sang **20. Screen registry nên lưu siêu dữ liệu (metadata / 메타데이터) hơn đối tượng (object / 객체) đồ thị (graph / 그래프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Broadcast sự kiện (event / 이벤트) cũng có sự đánh đổi (trade-off / 트레이드오프)

Sự kiện (event / 이벤트) bus/toàn cục (global / 전역) publish-subscribe giảm direct tham chiếu (reference / 참조) nhưng có thể tạo hidden phụ thuộc (dependency / 의존성) nếu dùng quá mức.

Nếu `ORDER_CHANGED` có 12 subscriber, một Save có thể trigger nhiều yêu cầu (request / 요청) ngoài dự kiến. sự kiện (event / 이벤트) đặc tả hợp đồng (contract / 계약) cần naming, payload lược đồ (schema / 스키마), quyền sở hữu (ownership / 소유권) và unsubscribe vòng đời (lifecycle / 생명주기).

Đừng thay `parent().parent()` coupling bằng “magic toàn cục (global / 전역) sự kiện (event / 이벤트)” coupling khó dấu vết (trace / 추적) hơn.

> **Nối mạch:** Trong **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **19. Broadcast sự kiện (event / 이벤트) cũng có sự đánh đổi (trade-off / 트레이드오프)** đặt vấn đề; **20. Screen registry nên lưu siêu dữ liệu (metadata / 메타데이터) hơn đối tượng (object / 객체) đồ thị (graph / 그래프)** đối chiếu bằng chứng, rồi **21. Adaptive frame và responsive responsibility** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. Screen registry nên lưu siêu dữ liệu (metadata / 메타데이터) hơn đối tượng (object / 객체) đồ thị (graph / 그래프)

Registry hữu ích:

```text
screenKey
containerId/tabId
screenId/src
business instance key
title
openedAt
```

Cẩn thận khi lưu direct phạm vi (scope / 범위)/thành phần (component / 컴포넌트) tham chiếu (reference / 참조) dài hạn. Nếu bộ chứa (container / 컨테이너) recreate WFrame bằng `setSrc()`, cached tham chiếu (reference / 참조) có thể stale và giữ old đối tượng (object / 객체) sống.

Resolve phạm vi (scope / 범위) gần thời điểm sử dụng qua bộ chứa (container / 컨테이너)/API công khai (public API / 공개 API) khi topology động (dynamic / 동적).

> **Nối mạch:** Ở chặng này của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **20. Screen registry nên lưu siêu dữ liệu (metadata / 메타데이터) hơn đối tượng (object / 객체) đồ thị (graph / 그래프)** đặt vấn đề; **21. Adaptive frame và responsive responsibility** đối chiếu bằng chứng, rồi **22. ứng dụng (application / 애플리케이션) shell cũng cần khả năng quan sát (observability / 관측 가능성)** mở rộng hệ quả hoặc giới hạn liên quan.

## 21. Adaptive frame và responsive responsibility

SP5 có `adaptiveFrame` trong TabControl/WindowContainer scenario để adaptive bố cục (layout / 레이아웃) có thể dựa kích thước frame thay vì trình duyệt (browser / 브라우저). Điều này quan trọng khi một screen sống trong cửa sổ (window / 윈도우) nhỏ hơn viewport.

Mô hình tư duy (mental model / 사고 모델):

```text
browser viewport size
≠ tab/window content size
```

Responsive lô-gic (logic / 논리) cần biết ranh giới (boundary / 경계) nào quyết định bố cục (layout / 레이아웃). Đừng hard-code `window.innerWidth` nếu screen thực tế phải thích ứng theo bộ chứa (container / 컨테이너).

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **22. ứng dụng (application / 애플리케이션) shell cũng cần khả năng quan sát (observability / 관측 가능성)** nối từ **21. Adaptive frame và responsive responsibility** sang **23. Shell failure-mode ma trận (matrix / 행렬)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. ứng dụng (application / 애플리케이션) shell cũng cần khả năng quan sát (observability / 관측 가능성)

Metrics/log hữu ích:

```text
screen open duration
screen ready duration
open screen count
close count
duplicate-open prevention
navigation failure
unsaved-close cancellation
per-screen memory/request growth
```

Khi người dùng (user / 사용자) nói “mở càng nhiều tab càng chậm”, cần bằng chứng (evidence / 증거) shell-level chứ không chỉ profile một screen riêng lẻ.

> **Nối mạch:** Trong **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **23. Shell failure-mode ma trận (matrix / 행렬)** nối từ **22. ứng dụng (application / 애플리케이션) shell cũng cần khả năng quan sát (observability / 관측 가능성)** sang **24. trường hợp (case / 사례) study: menu → multi-tab detail → save → refresh**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Shell failure-mode ma trận (matrix / 행렬)

```text
Mở menu nhưng tab cũ hiện data khác
→ instance key/reuse policy sai

Đóng tab rồi request vẫn chạy
→ child lifetime/cleanup chưa kết thúc

Mở cùng screen hai lần state đè nhau
→ global mutable state hoặc Scope boundary sai

Tab mới đôi lúc gọi function không tồn tại
→ object/render/data readiness race

Back button đi qua lịch sử lạ
→ browser/IFrame/SPA history semantics chưa định nghĩa

Mở 30 tab memory tăng không giảm
→ registry/listener/timer/reference leak
```

Mỗi triệu chứng nên được gỡ lỗi (debug / 디버그) bằng topology + thời gian tồn tại (lifetime / 수명) bằng chứng (evidence / 증거) trước khi sửa ngẫu nhiên.

> **Nối mạch:** Ở chặng này của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **23. Shell failure-mode ma trận (matrix / 행렬)** nêu quy tắc; **24. trường hợp (case / 사례) study: menu → multi-tab detail → save → refresh** thử quy tắc trong tình huống, rồi **25. Master quy tắc (rule / 규칙) cho multi-screen WebSquare** mở rộng hệ quả.

## 24. trường hợp (case / 사례) study: menu → multi-tab detail → save → refresh

Giả sử app có thứ tự (order / 순서) danh sách (list / 목록) và cho mở nhiều thứ tự (order / 순서) Detail.

Shell nhận command `openScreen(ORDER_DETAIL, ORD-1001)`. điều hướng (navigation / 내비게이션) key là `ORDER_DETAIL:ORD-1001`. Nếu chưa tồn tại, shell tạo WFrame tab và truyền `{orderId}`. Nếu đã tồn tại, shell activate tab đó.

Detail page giữ DataMap/DataList và Submission trong phạm vi (scope / 범위) riêng. Save gửi phiên bản (version / 버전) để máy chủ (server / 서버) kiểm tra tính đồng thời (concurrency / 동시성). Khi thành công, detail trả/publish một lĩnh vực (domain / 도메인) sự kiện (event / 이벤트) nhỏ `{type:"ORDER_CHANGED", orderId:"ORD-1001"}`. danh sách (list / 목록) page nếu đang mở có thể đánh dấu stale hoặc re-query theo chính sách (policy / 정책). Shell không chạm Grid của danh sách (list / 목록).

Khi người dùng (user / 사용자) đóng Detail còn dirty, shell gọi công khai (public / 공개) `canClose()` của instance. Nếu được đóng, registry xóa siêu dữ liệu (metadata / 메타데이터)/tham chiếu (reference / 참조) và page cleanup timer/listener. Đây là một luồng (flow / 흐름) hoàn chỉnh trong đó điều hướng (navigation / 내비게이션), nghiệp vụ (business / 비즈니스) trạng thái (state / 상태), máy chủ (server / 서버) tính đồng thời (concurrency / 동시성) và thời gian tồn tại (lifetime / 수명) có đơn vị sở hữu (owner / 오너) khác nhau nhưng đặc tả hợp đồng (contract / 계약) nối chúng rõ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **24. trường hợp (case / 사례) study: menu → multi-tab detail → save → refresh** nêu quy tắc; **25. Master quy tắc (rule / 규칙) cho multi-screen WebSquare** thử quy tắc trong tình huống, rồi **26. Kết nối** mở rộng hệ quả.

## 25. Master quy tắc (rule / 규칙) cho multi-screen WebSquare

Hãy giữ bốn định danh (identity / 식별자) riêng:

```text
screen definition identity
screen instance identity
business entity identity
runtime frame/scope identity
```

Nhiều bug enterprise xuất hiện vì bốn định danh (identity / 식별자) này bị trộn thành một string hoặc một row chỉ mục (index / 인덱스).

Khi kiến trúc (architecture / 아키텍처) rõ, shell có thể thay TabControl bằng WindowContainer hoặc đổi điều hướng (navigation / 내비게이션) chính sách (policy / 정책) mà nghiệp vụ (business / 비즈니스) screen ít bị ảnh hưởng.

> **Nối mạch:** Trong **14 — ứng dụng (application / 애플리케이션) Shell, điều hướng (navigation / 내비게이션) & Multi-Screen trạng thái (state / 상태)**, **26. Kết nối** nối từ **25. Master quy tắc (rule / 규칙) cho multi-screen WebSquare** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 26. Kết nối

Ứng dụng (application / 애플리케이션) shell điều phối screen, nhưng mọi mutation cuối cùng vẫn đi qua máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) và giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계). Tiếp theo đọc [15 — Backend Contract, Transaction & Concurrency Integration](15_backend_contract_transaction_concurrency.md).

> **Bàn giao:** Sau **26. Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
