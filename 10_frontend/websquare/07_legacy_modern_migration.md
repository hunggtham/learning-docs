# 07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Vì sao di chuyển (migration / 마이그레이션) kiến thức (knowledge / 지식) quan trọng với WebSquare** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Đừng migrate cú pháp (syntax / 문법) trước mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình chung và giới hạn. Mạch này nối legacy với hiện đại hóa và migration, để kiểm soát tương thích, dữ liệu và rollback trong từng bước chuyển đổi.

## 1. Vì sao di chuyển (migration / 마이그레이션) kiến thức (knowledge / 지식) quan trọng với WebSquare

WebSquare thường xuất hiện trong hệ thống enterprise sống nhiều năm. Một dự án (project / 프로젝트) có thể chứa page được viết ở nhiều thời kỳ, dùng chung (common / 공통) mô-đun (module / 모듈) đã tích lũy workaround cũ, API mới và cũ cùng tồn tại, và engine upgrade diễn ra chậm hơn ứng dụng (application / 애플리케이션) mã (code / 코드).

Vì vậy “mã (code / 코드) mới nhất” không đủ. nhà phát triển (developer / 개발자) cần đọc được cả mã (code / 코드) legacy và biết **hành vi (behavior / 동작) nào là historical ràng buộc (constraint / 제약조건), hành vi (behavior / 동작) nào vẫn là bất biến (invariant / 불변식), và hành vi (behavior / 동작) nào chỉ còn vì chưa refactor**.

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **2. Đừng migrate cú pháp (syntax / 문법) trước mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **1. Vì sao di chuyển (migration / 마이그레이션) kiến thức (knowledge / 지식) quan trọng với WebSquare** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **3. Global-style page và Scope-style page** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Đừng migrate cú pháp (syntax / 문법) trước mô hình tư duy (mental model / 사고 모델)

Một di chuyển (migration / 마이그레이션) an toàn không bắt đầu bằng tìm kiếm (search / 검색)/replace `$w` thành `$p` hay IFrame thành WFrame. Trước tiên phải hiểu page topology, quyền sở hữu trạng thái (state ownership / 상태 소유권) và communication đường dẫn (path / 경로) hiện tại.

Với mỗi screen, lập bản đồ:

```text
entry page
frame/container tree
global variables
DataCollection
Submission
popup contract
cross-page calls
common utility dependency
browser-specific workaround
```

Sau đó mới quyết định refactor ranh giới (boundary / 경계).

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **3. Global-style page và Scope-style page** tổng hợp từ **2. Đừng migrate cú pháp (syntax / 문법) trước mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **4. $w và $p** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. Global-style page và Scope-style page

Mã (code / 코드) cũ có thể dựa mạnh vào toàn cục (global / 전역) ID/hàm (function / 함수). Điều này chạy khi mỗi page độc lập hoặc IFrame tách toàn cục (global / 전역) ngữ cảnh (context / 맥락).

Scope-style kiến trúc (architecture / 아키텍처) đặt page hành vi (behavior / 동작) vào `scwin`, dùng WFrame phạm vi (scope / 범위) để tránh collision và `$p` cho page-aware utility.

Di chuyển (migration / 마이그레이션) không chỉ là đổi tên hàm (function / 함수):

```text
global function
→ page-local function

global component lookup
→ scope-local component lookup

implicit cross-page dependency
→ explicit parent/window contract
```

Nếu chỉ thêm `scwin.` nhưng vẫn giữ toàn cục (global / 전역) trạng thái (state / 상태) và `top.someComponent`, isolation chưa thật sự đạt được.

> **Nối mạch:** Global-style page và scope-style page cho thấy migration boundary; $w/$p tiếp theo là hai API cần map theo ownership trước khi đổi IFrame SPA sang WFrame SPA.

## 4. `$w` và `$p`

Trong phạm vi (scope / 범위) mô hình (model / 모델), `$p` được dùng như page-aware ánh xạ (mapping / 매핑) cho utility vốn liên quan `$w`. mã (code / 코드) legacy có thể còn `$w.*` ở toàn cục (global / 전역) ngữ cảnh (context / 맥락).

Không nên blindly replace mọi `$w` bằng `$p`. Cần xác định hàm (function / 함수) đó đang chạy ở page phạm vi (scope / 범위) nào và utility đó có page-relative ngữ nghĩa (semantics / 의미론) hay không.

Di chuyển (migration / 마이그레이션) checklist:

```text
Call có cần current page context?
Code có chạy trong common global module?
Target object có nằm trong child/parent Scope?
Build hiện tại document API nào?
```

> **Nối mạch:** `$w/$p` là API ownership cần map trước; IFrame SPA → WFrame SPA tiếp theo thay đổi lifecycle và scope boundary, nên `window.parent` không còn là contract mặc định.

## 5. IFrame SPA → WFrame SPA

Các WebSquare đời cũ có thể dùng IFrame để isolate page và tái sử dụng engine/frame bằng cơ chế (mechanism / 메커니즘) như `spaInitCount`/`spaAuto`. Từ các dòng SP3+, WFrame + phạm vi (scope / 범위) cho phép SPA composition đơn giản hơn.

IFrame tạo trình duyệt (browser / 브라우저) ngữ cảnh (context / 맥락) tương đối độc lập; WFrame phạm vi (scope / 범위) vẫn sống trong cùng broader thời gian chạy (runtime / 런타임). Vì vậy di chuyển (migration / 마이그레이션) ảnh hưởng:

```text
global variable isolation
window/top/parent semantics
CSS/resource sharing
memory lifecycle
cross-frame call
DOM access
```

Không thay IFrame bằng WFrame rồi giả định `window.parent` hành vi (behavior / 동작) giống hệt.

> **Nối mạch:** WFrame scope thay thế implicit `window.parent` traversal bằng navigation contract; inline DOM manipulation tiếp theo nên chuyển thành component API có owner rõ.

## 6. `window.parent` → WebSquare phạm vi (scope / 범위) điều hướng (navigation / 내비게이션)

Legacy mã (code / 코드) có thể:

```javascript
window.parent.someFunction();
```

Trong WFrame phạm vi (scope / 범위) kiến trúc (architecture / 아키텍처), tường minh (explicit / 명시적) WebSquare quan hệ (relation / 관계) như `$p.parent()` phù hợp hơn vì nó hiểu page phạm vi (scope / 범위), không chỉ trình duyệt (browser / 브라우저) cửa sổ (window / 윈도우) hierarchy.

Di chuyển (migration / 마이그레이션) tốt:

```javascript
$p.parent().scwin.someFunction();
```

Nhưng bước tiếp theo nên là giảm coupling bằng công khai (public / 공개) parent hàm (function / 함수) đặc tả hợp đồng (contract / 계약), không chỉ thay điều hướng (navigation / 내비게이션) thành phần nguyên thủy (primitive / 기본 요소).

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **7. Inline DOM manipulation → thành phần (component / 컴포넌트) API** nối từ **6. window.parent → WebSquare phạm vi (scope / 범위) điều hướng (navigation / 내비게이션)** sang **8. jQuery hỗ trợ (support / 지원) là tính tương thích (compatibility / 호환성), không nên là default mới**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Inline DOM manipulation → thành phần (component / 컴포넌트) API

Mã (code / 코드) cũ thường chứa jQuery selector hoặc raw DOM vì thành phần (component / 컴포넌트) API thời đó thiếu tính năng (feature / 기능) hoặc nhóm (team / 팀) quen web development cũ.

Khi engine mới đã có API công khai (public API / 공개 API), ưu tiên migrate về thành phần (component / 컴포넌트) đặc tả hợp đồng (contract / 계약).

Ví dụ:

```text
$('#someInternalInput').val(x)
→ inputComponent.setValue(x)
```

Không phải vì jQuery “xấu”, mà vì thành phần (component / 컴포넌트) API giữ khung phần mềm (framework / 프레임워크) trạng thái (state / 상태)/binding/vòng đời (lifecycle / 생명주기) đúng hơn và bền hơn khi renderer đổi.

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **8. jQuery hỗ trợ (support / 지원) là tính tương thích (compatibility / 호환성), không nên là default mới** nối từ **7. Inline DOM manipulation → thành phần (component / 컴포넌트) API** sang **9. Callback string và eval**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. jQuery hỗ trợ (support / 지원) là tính tương thích (compatibility / 호환성), không nên là default mới

WebSquare có jQuery hỗ trợ (support / 지원) ở nhiều dòng. Với mã (code / 코드) mới, nếu WebSquare API hoặc hiện đại (modern / 현대적) trình duyệt (browser / 브라우저) API đủ, không cần thêm jQuery chỉ vì dự án (project / 프로젝트) legacy có sẵn.

Tuy nhiên không nên xóa jQuery hàng loạt nếu plugin/dùng chung (common / 공통) thư viện (library / 라이브러리) phụ thuộc. di chuyển (migration / 마이그레이션) theo usage đồ thị (graph / 그래프) và kiểm thử (test / 테스트) hành vi (behavior / 동작).

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **9. Callback string và eval** nối từ **8. jQuery hỗ trợ (support / 지원) là tính tương thích (compatibility / 호환성), không nên là default mới** sang **10. Synchronous Submission**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Callback string và `eval`

Legacy popup/dùng chung (common / 공통) mô-đun (module / 모듈) có thể truyền callback string:

```javascript
{
    callback: "$p.parent().scwin.onSelected"
}
```

rồi `eval` ở child.

Di chuyển (migration / 마이그레이션) mục tiêu (target / 대상) tốt hơn:

```text
input data contract
→ child operation
→ result data contract
→ parent handler
```

Nếu nền tảng (platform / 플랫폼) API chỉ cho string ở một điểm, ít nhất giới hạn callback vào nội bộ (internal / 내부) allowlist và tách nó khỏi arbitrary bên ngoài (external / 외부) dữ liệu (data / 데이터).

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **10. Synchronous Submission** nối từ **9. Callback string và eval** sang **11. dùng chung (common / 공통) utility wrapper và lớp trừu tượng (abstraction / 추상화) debt**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Synchronous Submission

Legacy mã (code / 코드) có thể dùng synchronous yêu cầu (request / 요청) vì dễ lập luận (reasoning / 추론) theo nguồn (source / 소스) thứ tự (order / 순서). Synchronous XHR-style communication khối (block / 블록) UI luồng thực thi (thread / 스레드) và không phù hợp web hiện đại.

Di chuyển (migration / 마이그레이션) sang asynchronous đòi hỏi đổi điều khiển (control / 제어) luồng (flow / 흐름):

Legacy mô hình tư duy (mental model / 사고 모델):

```javascript
execute();
useResult();
```

Async mô hình (model / 모델):

```text
execute
→ return
→ response callback
→ useResult
```

Không thể chỉ đổi `mode="asynchronous"` mà giữ mã (code / 코드) phía sau như cũ.

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **11. dùng chung (common / 공통) utility wrapper và lớp trừu tượng (abstraction / 추상화) debt** nối từ **10. Synchronous Submission** sang **12. Magic cấu hình (config / 설정) và historical workaround**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. dùng chung (common / 공통) utility wrapper và lớp trừu tượng (abstraction / 추상화) debt

Dự án (project / 프로젝트) lâu năm thường có wrapper như:

```text
gfn_search
gfn_save
gfn_popup
gfn_message
gfn_grid...
```

Wrapper tốt khi chuẩn hóa logging, auth header, dùng chung (common / 공통) lỗi (error / 오류) handling hoặc UX convention. Wrapper xấu khi che quá nhiều parameter, tự sửa DataCollection hoặc chứa exception cho từng screen.

Kiểm tra (audit / 감사) wrapper bằng câu hỏi:

```text
Nó giảm duplication thật hay chỉ đổi tên API?
Nó giữ abstraction ổn định không?
Nó có hidden side effect không?
Có hàng chục flag boolean không?
Screen mới có buộc hiểu internal wrapper mới dùng được không?
```

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **12. Magic cấu hình (config / 설정) và historical workaround** nối từ **11. dùng chung (common / 공통) utility wrapper và lớp trừu tượng (abstraction / 추상화) debt** sang **13. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) cần phiên bản (version / 버전) điều khiển (control / 제어)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Magic cấu hình (config / 설정) và historical workaround

Một cấu hình (config / 설정) có thể tồn tại vì bug engine 8 năm trước. Trước khi giữ hoặc xóa, tìm bằng chứng (evidence / 증거):

```text
comment/issue history
release note
engine build hiện tại
reproduction test
```

Không xóa workaround chỉ vì không hiểu. Cũng không giữ vĩnh viễn chỉ vì “hệ thống đang chạy”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **13. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) cần phiên bản (version / 버전) điều khiển (control / 제어)** nối từ **12. Magic cấu hình (config / 설정) và historical workaround** sang **14. bản phát hành (release / 릴리스) ghi chú (note / 노트) phải đi cùng upgrade kiểm thử (test / 테스트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) cần phiên bản (version / 버전) điều khiển (control / 제어)

WebSquare API docs được phát hành theo engine bản dựng (build / 빌드). Một môi trường vận hành (production / 운영 환경) issue có thể chỉ xuất hiện ở bản dựng (build / 빌드) cụ thể.

Repository/app documentation nên ghi:

```text
engine generation
SP/build version
Studio version nếu liên quan
known browser matrix
important config toggles
```

Đây là phụ thuộc (dependency / 의존성) inventory giống Java phiên bản (version / 버전) hoặc Spring Boot phiên bản (version / 버전).

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **14. bản phát hành (release / 릴리스) ghi chú (note / 노트) phải đi cùng upgrade kiểm thử (test / 테스트)** nối từ **13. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) cần phiên bản (version / 버전) điều khiển (control / 제어)** sang **15. W-Pack sản phẩm tạo ra (artifact / 산출물) và triển khai (deployment / 배포) di chuyển (migration / 마이그레이션)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. bản phát hành (release / 릴리스) ghi chú (note / 노트) phải đi cùng upgrade kiểm thử (test / 테스트)

Khi upgrade engine:

```text
1. đọc release note từ current → target
2. liệt kê deprecated/changed behavior
3. chạy smoke test core screens
4. chạy regression cho Grid, popup, WFrame, Submission
5. đo performance/memory
6. test browser matrix
7. so sánh console warning/error
```

Upgrade UI engine không nên được coi là “thay vài JAR rồi xong”.

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **15. W-Pack sản phẩm tạo ra (artifact / 산출물) và triển khai (deployment / 배포) di chuyển (migration / 마이그레이션)** nối từ **14. bản phát hành (release / 릴리스) ghi chú (note / 노트) phải đi cùng upgrade kiểm thử (test / 테스트)** sang **16. CSS di chuyển (migration / 마이그레이션)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. W-Pack sản phẩm tạo ra (artifact / 산출물) và triển khai (deployment / 배포) di chuyển (migration / 마이그레이션)

Khi bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) thay đổi W-Pack/minify/obfuscation, cần verify:

```text
source → artifact mapping
cache busting
source map
resource path/context root
incremental build
CI packaging
rollback artifact
```

Một di chuyển (migration / 마이그레이션) nguồn (source / 소스) thành công nhưng sản phẩm tạo ra (artifact / 산출물) stale vẫn thất bại môi trường vận hành (production / 운영 환경).

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **16. CSS di chuyển (migration / 마이그레이션)** nối từ **15. W-Pack sản phẩm tạo ra (artifact / 산출물) và triển khai (deployment / 배포) di chuyển (migration / 마이그레이션)** sang **17. trình duyệt (browser / 브라우저) modernization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. CSS di chuyển (migration / 마이그레이션)

Renderer/phiên bản (version / 버전) mới có thể thay nội bộ (internal / 내부) DOM/lớp (class / 클래스). CSS selector dựa sâu vào nội bộ (internal / 내부) markup dễ vỡ.

Trước engine upgrade, tìm kiếm (search / 검색):

```text
#generated-id
very deep selectors
engine-internal class name
!important workaround
browser-specific hacks
```

Ưu tiên application-owned lớp (class / 클래스) và visual regression kiểm thử (test / 테스트).

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **17. trình duyệt (browser / 브라우저) modernization** nối từ **16. CSS di chuyển (migration / 마이그레이션)** sang **18. bảo mật (security / 보안) modernization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. trình duyệt (browser / 브라우저) modernization

Dự án (project / 프로젝트) WebSquare lâu năm có thể chứa:

```text
IE branch
ActiveX integration
document.all
attachEvent
old polyfill
vendor CSS prefix workaround
```

Nếu trình duyệt (browser / 브라우저) chính sách (policy / 정책) đã bỏ IE, những branch này trở thành maintenance chi phí (cost / 비용). Nhưng xóa theo kiểm thử (test / 테스트) coverage, không theo cảm giác.

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **18. bảo mật (security / 보안) modernization** nối từ **17. trình duyệt (browser / 브라우저) modernization** sang **19. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) di chuyển (migration / 마이그레이션)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. bảo mật (security / 보안) modernization

Legacy enterprise mã (code / 코드) thường cần kiểm tra (audit / 감사):

```text
eval
innerHTML
unescaped server message
URL parameter injection
weak popup origin assumption
client-side authorization
old upload endpoint
sensitive console log
```

Engine upgrade không tự sửa ứng dụng (application / 애플리케이션) bảo mật (security / 보안) mẫu (pattern / 패턴).

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **18. bảo mật (security / 보안) modernization** đặt vấn đề; **19. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) di chuyển (migration / 마이그레이션)** đối chiếu bằng chứng, rồi **20. WebSquare5 SP5 và dòng 6.0/WebSquare AI** mở rộng hệ quả hoặc giới hạn liên quan.

## 19. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) di chuyển (migration / 마이그레이션)

Khi backend đổi XML → JSON hoặc trường dữ liệu (field / 필드) lược đồ (schema / 스키마), tránh làm mỗi screen tự convert thủ công.

Tạo tính tương thích (compatibility / 호환성) ranh giới (boundary / 경계) ở dữ liệu (data / 데이터)/dịch vụ (service / 서비스) tầng (layer / 계층) nếu dự án (project / 프로젝트) kiến trúc (architecture / 아키텍처) cho phép. Mục tiêu là screen lập luận (reasoning / 추론) vẫn trên chuẩn gốc (canonical / 정본) lĩnh vực (domain / 도메인) mô hình (model / 모델).

```text
legacy response
→ adapter
→ canonical DataCollection shape
→ screen
```

Adapter tạm phải có kế hoạch remove; nếu không, tính tương thích (compatibility / 호환성) tầng (layer / 계층) trở thành permanent độ phức tạp (complexity / 복잡도).

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **19. dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) di chuyển (migration / 마이그레이션)** đặt vấn đề; **20. WebSquare5 SP5 và dòng 6.0/WebSquare AI** đối chiếu bằng chứng, rồi **21. Strangler di chuyển (migration / 마이그레이션) cho screen lớn** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. WebSquare5 SP5 và dòng 6.0/WebSquare AI

Tài liệu chính thức năm 2026 có cả WebSquare5 SP5 và API 6.0. Dòng 6.0 vẫn giữ nhiều concept quen thuộc như thành phần (component / 컴포넌트) đối tượng (object / 객체), `getValue/setValue`, DataMap và mạng (network / 네트워크) utility, nhưng có API/tham chiếu (reference / 참조) generation riêng.

Không nên diễn giải “6.0” như chỉ đổi tên SP5. Khi dự án (project / 프로젝트) thực sự migrate, hãy diff API/thuộc tính (property / 속성)/sự kiện (event / 이벤트) của các thành phần (component / 컴포넌트) trọng yếu (critical / 중요) bằng official tham chiếu (reference / 참조) đúng bản dựng (build / 빌드).

Mô hình tư duy (mental model / 사고 모델) trong thư viện (library / 라이브러리) này được giữ ở mức bền hơn phiên bản (version / 버전):

```text
page/component abstraction
data model
scope
communication
frame composition
browser/runtime boundary
```

Các concept này giúp đọc cả mã (code / 코드) cũ và mới, dù API chi tiết thay đổi.

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **21. Strangler di chuyển (migration / 마이그레이션) cho screen lớn** nối từ **20. WebSquare5 SP5 và dòng 6.0/WebSquare AI** sang **22. Characterization kiểm thử (test / 테스트) trước refactor**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Strangler di chuyển (migration / 마이그레이션) cho screen lớn

Một screen 5.000 dòng không nên rewrite một lần nếu không có kiểm thử (test / 테스트) mạnh. Có thể di chuyển (migration / 마이그레이션) dần:

```text
1. thêm observability/test
2. tách handler lớn thành function có tên
3. gom DataCollection contract
4. giảm direct parent component access
5. thay DOM hack bằng component API
6. chuyển async flow
7. bật stricter Scope/config
8. nâng engine
```

Mỗi bước giảm rủi ro (risk / 위험) và tạo checkpoint quay lui (rollback / 롤백).

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **22. Characterization kiểm thử (test / 테스트) trước refactor** nối từ **21. Strangler di chuyển (migration / 마이그레이션) cho screen lớn** sang **23. di chuyển (migration / 마이그레이션) anti-pattern: rewrite vì “mã (code / 코드) cũ xấu”**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Characterization kiểm thử (test / 테스트) trước refactor

Với legacy mã (code / 코드) khó hiểu, kiểm thử (test / 테스트) hành vi (behavior / 동작) hiện tại trước khi sửa:

```text
Given condition A
When click Search
Then request payload X
And grid result Y
```

Đây là characterization kiểm thử (test / 테스트): ghi lại hành vi (behavior / 동작) thật, kể cả hiện thực (implementation / 구현) xấu. Sau refactor, giữ nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작) trừ phần bug chủ đích sửa.

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **23. di chuyển (migration / 마이그레이션) anti-pattern: rewrite vì “mã (code / 코드) cũ xấu”** nối từ **22. Characterization kiểm thử (test / 테스트) trước refactor** sang **24. di chuyển (migration / 마이그레이션) anti-pattern: preserve mọi hành vi (behavior / 동작) vì sợ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. di chuyển (migration / 마이그레이션) anti-pattern: rewrite vì “mã (code / 코드) cũ xấu”

Full rewrite thường đánh mất hidden nghiệp vụ (business / 비즈니스) rules nằm trong handler, dùng chung (common / 공통) util và máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약).

Trước rewrite, inventory quy tắc (rule / 규칙):

```text
validation
format
permission
special customer case
batch semantics
error handling
popup callback
legacy browser requirement
```

Nếu không liệt kê được, bạn chưa hiểu đủ để rewrite an toàn.

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **24. di chuyển (migration / 마이그레이션) anti-pattern: preserve mọi hành vi (behavior / 동작) vì sợ** nối từ **23. di chuyển (migration / 마이그레이션) anti-pattern: rewrite vì “mã (code / 코드) cũ xấu”** sang **25. API inventory cho trọng yếu (critical / 중요) screen**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. di chuyển (migration / 마이그레이션) anti-pattern: preserve mọi hành vi (behavior / 동작) vì sợ

Ngược lại, giữ tất cả historical hành vi (behavior / 동작) cũng nguy hiểm. Một workaround cho IE8 không nên dictate kiến trúc (architecture / 아키텍처) năm 2026.

Phân loại:

```text
business invariant → preserve
platform constraint còn tồn tại → preserve
obsolete workaround → remove có test
accidental bug → fix có requirement
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **25. API inventory cho trọng yếu (critical / 중요) screen** nối từ **24. di chuyển (migration / 마이그레이션) anti-pattern: preserve mọi hành vi (behavior / 동작) vì sợ** sang **26. Deprecation chiến lược (strategy / 전략)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. API inventory cho trọng yếu (critical / 중요) screen

Trước upgrade, lập bảng:

| Area | API/thuộc tính (property / 속성) đang dùng | rủi ro (risk / 위험) |
|---|---|---|
| phạm vi (scope / 범위) | `$p.parent`, `getWindow` | topology/vòng đời (lifecycle / 생명주기) |
| đầu vào (input / 입력) | `getValue`, `setValue`, format | sự kiện (event / 이벤트)/format hành vi (behavior / 동작) |
| DataList | row status, insert/delete, JSON | CRUD ngữ nghĩa (semantics / 의미론) |
| Submission | chế độ (mode / 모드), ref/mục tiêu (target / 대상), callbacks | async/mạng (network / 네트워크) |
| GridView | edit, filter, Excel | rendering/hiệu năng (performance / 성능) |
| Popup/WFrame | dataObject, setSrc | serialization/vòng đời (lifecycle / 생명주기) |

Sau đó tra đúng mục tiêu (target / 대상) bản dựng (build / 빌드).

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **26. Deprecation chiến lược (strategy / 전략)** nối từ **25. API inventory cho trọng yếu (critical / 중요) screen** sang **27. rà soát mã (code review / 코드 리뷰) khi có cả legacy và hiện đại (modern / 현대적) style**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Deprecation chiến lược (strategy / 전략)

Khi API deprecated:

```text
Không xóa ngay nếu production còn dùng.
Đánh dấu usage.
Xác định replacement và semantic difference.
Migrate screen nhỏ trước.
Đo regression.
Sau khi usage = 0 mới remove compatibility wrapper.
```

Deprecation không đồng nghĩa broken ngay, nhưng là debt có deadline.

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **27. rà soát mã (code review / 코드 리뷰) khi có cả legacy và hiện đại (modern / 현대적) style** nối từ **26. Deprecation chiến lược (strategy / 전략)** sang **28. Checklist đọc một tệp (file / 파일) WebSquare lạ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. rà soát mã (code review / 코드 리뷰) khi có cả legacy và hiện đại (modern / 현대적) style

Reviewer không nên yêu cầu mọi tệp (file / 파일) cũ chuyển hiện đại (modern / 현대적) style trong PR tính năng (feature / 기능) nhỏ. phạm vi (scope / 범위) thay đổi (change / 변경) quá lớn tăng regression rủi ro (risk / 위험).

Thay vào đó:

```text
không thêm legacy pattern mới
refactor phần chạm vào nếu đủ test
ghi debt có boundary rõ
migrate theo module/screen
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **28. Checklist đọc một tệp (file / 파일) WebSquare lạ** nối từ **27. rà soát mã (code review / 코드 리뷰) khi có cả legacy và hiện đại (modern / 현대적) style** sang **29. Checklist di chuyển (migration / 마이그레이션) môi trường vận hành (production / 운영 환경)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Checklist đọc một tệp (file / 파일) WebSquare lạ

Khi mở một page chưa từng thấy:

```text
1. Page nằm trong frame nào?
2. Có Scope/scwin không?
3. DataMap/DataList nào là source of truth?
4. Submission nào query/save?
5. Grid bind model nào?
6. Event entry point là gì?
7. Cross-page dependency ở đâu?
8. Common util nào có side effect?
9. API nào legacy/version-sensitive?
10. Có DOM/jQuery hack không?
```

Trả lời mười câu này trước khi sửa sâu.

> **Nối mạch:** Trong **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **29. Checklist di chuyển (migration / 마이그레이션) môi trường vận hành (production / 운영 환경)** nối từ **28. Checklist đọc một tệp (file / 파일) WebSquare lạ** sang **30. Kết thúc nhánh học (track / 트랙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Checklist di chuyển (migration / 마이그레이션) môi trường vận hành (production / 운영 환경)

```text
Engine/build target được ghi rõ
Release notes reviewed
Config diff reviewed
Critical API inventory done
Async behavior tested
Scope/frame navigation tested
Grid CRUD regression done
Popup parameter/result tested
Large data performance measured
Memory leak soak test done
Security regression reviewed
Cache/W-Pack deployment verified
Rollback plan available
```

> **Nối mạch:** Ở chặng này của **07 — Legacy, hiện đại (modern / 현대적) Evolution & di chuyển (migration / 마이그레이션)**, **30. Kết thúc nhánh học (track / 트랙)** nối từ **29. Checklist di chuyển (migration / 마이그레이션) môi trường vận hành (production / 운영 환경)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 30. Kết thúc nhánh học (track / 트랙)

Sau bảy chapter, mục tiêu không phải là bạn nhớ mọi thuộc tính (property / 속성) của mọi thành phần (component / 컴포넌트). API tham chiếu (reference / 참조) tồn tại cho việc đó. Mục tiêu là bạn có một mô hình tư duy (mental model / 사고 모델) đủ mạnh để mở một screen WebSquare lạ và trả lời:

```text
Page được tạo và chạy thế nào?
State nằm ở đâu?
Scope nào sở hữu object?
Event nào kích hoạt flow?
Data đi qua DataCollection/Submission ra sao?
Grid đang hiển thị model nào?
Failure có thể nằm ở boundary nào?
Evidence nào kiểm chứng giả thuyết?
Code này là modern contract hay legacy workaround?
```

Hãy dùng [Glossary & Coverage Audit](GLOSSARY_AND_COVERAGE.md) để rà coverage và quay lại chapter còn yếu.

> **Bàn giao:** Sau **30. Kết thúc nhánh học (track / 트랙)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
