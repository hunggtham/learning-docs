# 12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. mô hình tư duy (mental model / 사고 모델): nguồn (source / 소스) không phải thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. Ba định danh (identity / 식별자) cần phân biệt** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối source, build artifact, configuration và runtime environment, để truy nguyên khác biệt triển khai từ đầu vào đến hành vi thực tế.

WebSquare nhà phát triển (developer / 개발자) thường dành phần lớn thời gian trong XML page và JavaScript, nhưng môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작) không chỉ đến từ mã nguồn (source code / 소스 코드). Một page có thể đúng trong Studio và sai ở UAT vì W-Pack sản phẩm tạo ra (artifact / 산출물) khác; cùng sản phẩm tạo ra (artifact / 산출물) có thể chạy khác vì máy khách (client / 클라이언트)/máy chủ (server / 서버) cấu hình (config / 설정); cùng cấu hình (config / 설정) có thể cho kết quả khác vì ngữ cảnh (context / 맥락) gốc (root / 루트), bộ nhớ đệm (cache / 캐시), reverse proxy hoặc engine bản dựng (build / 빌드).

Vì vậy triển khai (deployment / 배포) phải được hiểu như một **chuỗi biến đổi có provenance**, không phải thao tác “bản sao (copy / 복사) tệp (file / 파일) lên máy chủ (server / 서버)”.

> Prerequisite: [01 — Platform, Runtime & Page Model](01_platform_runtime_page_model.md), [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md) và [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

## 1. mô hình tư duy (mental model / 사고 모델): nguồn (source / 소스) không phải thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물)

Trong WebSquare5 SP5, page thường được author bằng XML nhưng W-Pack chuyển nguồn (source / 소스) thành JavaScript để engine/trình duyệt (browser / 브라우저) sử dụng. Official guide mô tả sản phẩm tạo ra (artifact / 산출물) page dưới `_wpack_` và dùng chung (common / 공통) tài nguyên (resource / 자원) được chuyển tương ứng.

Chuỗi xử lý (pipeline / 파이프라인) cần lập luận (reasoning / 추론) như sau:

```text
XML/JS/CSS source
→ WebSquare configuration
→ W-Pack/build
→ generated artifact
→ package/deploy
→ web server/WAS/reverse proxy
→ browser cache/network
→ WebSquare Engine
→ runtime page
```

Bug môi trường vận hành (production / 운영 환경) có thể xuất hiện ở bất kỳ mũi tên nào. Vì vậy “Git nguồn (source / 소스) đúng” chưa chứng minh “trình duyệt (browser / 브라우저) đang chạy đúng mã (code / 코드)”.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **1. mô hình tư duy (mental model / 사고 모델): nguồn (source / 소스) không phải thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물)** đặt vấn đề; **2. Ba định danh (identity / 식별자) cần phân biệt** đối chiếu bằng chứng, rồi **3. Studio bản dựng (build / 빌드) và CI bản dựng (build / 빌드) là hai thực thi (execution / 실행) môi trường (environment / 환경)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Ba định danh (identity / 식별자) cần phân biệt

Một bản phát hành (release / 릴리스) nên có ít nhất ba định danh (identity / 식별자) rõ.

**nguồn (source / 소스) định danh (identity / 식별자)** trả lời nguồn (source / 소스) lần ghi nhận (commit / 커밋) nào được chọn.

**bản dựng (build / 빌드) định danh (identity / 식별자)** trả lời nguồn (source / 소스) đó được bản dựng (build / 빌드) bằng engine/công cụ (tool / 도구)/cấu hình (config / 설정) nào và tạo sản phẩm tạo ra (artifact / 산출물) nào.

**triển khai (deployment / 배포) định danh (identity / 식별자)** trả lời sản phẩm tạo ra (artifact / 산출물) nào đang thực sự phục vụ ở môi trường (environment / 환경) nào.

Nếu ba định danh (identity / 식별자) này bị trộn, nhóm (team / 팀) dễ rơi vào tình huống:

```text
“commit đã merge”
≠ “artifact đã rebuild”
≠ “artifact mới đã deploy”
≠ “browser user đã nhận artifact mới”
```

Môi trường vận hành (production / 운영 환경) troubleshooting phải biết mình đang đứng ở bước nào.

> **Nối mạch:** Ba identity (source, build artifact, deployed app) phải được truy vết; Studio và CI là hai execution environment, còn W-Pack đặt compiler-like boundary giữa chúng.

## 3. Studio bản dựng (build / 빌드) và CI bản dựng (build / 빌드) là hai thực thi (execution / 실행) môi trường (environment / 환경)

SP5 Studio có thể tự W-Pack khi dự án (project / 프로젝트) bản dựng (build / 빌드)/rebuild. Tài liệu chính thức cũng cung cấp stand-alone W-Pack để chạy từ command line và tích hợp CI/máy chủ (server / 서버) batch conversion.

Điều này tạo một yêu cầu (requirement / 요구사항) quan trọng: **CI bản dựng (build / 빌드) phải là bản dựng (build / 빌드) có thể tái tạo**, không phụ thuộc một nhà phát triển (developer / 개발자) đã click menu nào trong Studio.

Nếu cục bộ (local / 로컬) Studio tạo sản phẩm tạo ra (artifact / 산출물) khác CI, cần so:

```text
Studio/W-Pack version
engine/build package
W-Pack options
source include/exclude
common resource configuration
minification/obfuscation mode
path/context-root assumptions
```

Đừng chữa bằng cách lần ghi nhận (commit / 커밋) sản phẩm tạo ra (artifact / 산출물) được tạo thủ công từ một máy mà chưa hiểu khác biệt.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **3. Studio bản dựng (build / 빌드) và CI bản dựng (build / 빌드) là hai thực thi (execution / 실행) môi trường (environment / 환경)** đặt tiêu chí; **4. W-Pack là compiler-like ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **5. bản dựng (build / 빌드) reproducibility** mở rộng hệ quả.

## 4. W-Pack là compiler-like ranh giới (boundary / 경계)

W-Pack không phải JavaScript trình biên dịch (compiler / 컴파일러) theo nghĩa ECMAScript ngôn ngữ (language / 언어) trình biên dịch (compiler / 컴파일러), nhưng trong delivery chuỗi xử lý (pipeline / 파이프라인) nó đóng vai trò tương tự một transformation ranh giới (boundary / 경계): nguồn (source / 소스) authoring được chuyển thành thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물).

Điều đó có ba consequence.

Thứ nhất, bản dựng (build / 빌드) lỗi (error / 오류) phải thất bại (fail / 실패) chuỗi xử lý (pipeline / 파이프라인) thay vì bị bỏ qua rồi deploy sản phẩm tạo ra (artifact / 산출물) cũ.

Thứ hai, generated đầu ra (output / 출력) cần dấu vết (trace / 추적) về nguồn (source / 소스)/bản dựng (build / 빌드) phiên bản (version / 버전).

Thứ ba, kiểm thử (test / 테스트) phải chạy trên sản phẩm tạo ra (artifact / 산출물) gần với thứ sẽ deploy, không chỉ trên XML nguồn (source / 소스) trong development chế độ (mode / 모드).

Một quy trình phát hành (release process / 릴리스 프로세스) chỉ kiểm thử (test / 테스트) Studio preview nhưng môi trường vận hành (production / 운영 환경) chạy minified W-Pack đầu ra (output / 출력) đang bỏ qua một ranh giới (boundary / 경계) quan trọng.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **4. W-Pack là compiler-like ranh giới (boundary / 경계)** đặt tiêu chí; **5. bản dựng (build / 빌드) reproducibility** dùng tiêu chí đó để kiểm tra ranh giới, rồi **6. máy khách (client / 클라이언트) cấu hình (configuration / 구성) và máy chủ (server / 서버) cấu hình (configuration / 구성) là hai ranh giới (boundary / 경계) khác nhau** mở rộng hệ quả.

## 5. bản dựng (build / 빌드) reproducibility

Một bản dựng (build / 빌드) có thể gọi là reproducible về mặt vận hành khi cùng nguồn (source / 소스) + cùng toolchain + cùng cấu hình (config / 설정) đầu vào (input / 입력) tạo ra sản phẩm tạo ra (artifact / 산출물) tương đương về hành vi (behavior / 동작).

Không nhất thiết byte-for-byte giống nếu công cụ (tool / 도구) chèn timestamp/băm (hash / 해시), nhưng hành vi (behavior / 동작) và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) phải deterministic.

Hãy phiên bản (version / 버전) hóa hoặc quản lý rõ:

```text
WebSquare engine/tool build
W-Pack executable/version
build arguments
client/server config source
common modules/resources
third-party JS/CSS versions
browser support target
```

“Máy anh A bản dựng (build / 빌드) được” không phải bản dựng (build / 빌드) specification.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **5. bản dựng (build / 빌드) reproducibility** đặt tiêu chí; **6. máy khách (client / 클라이언트) cấu hình (configuration / 구성) và máy chủ (server / 서버) cấu hình (configuration / 구성) là hai ranh giới (boundary / 경계) khác nhau** dùng tiêu chí đó để kiểm tra ranh giới, rồi **7. cấu hình (configuration / 구성) is mã (code / 코드)** mở rộng hệ quả.

## 6. máy khách (client / 클라이언트) cấu hình (configuration / 구성) và máy chủ (server / 서버) cấu hình (configuration / 구성) là hai ranh giới (boundary / 경계) khác nhau

SP5 Studio cung cấp `client.config.xml` và `server.config.xml` trong WebSquare Configure. Tài liệu chính thức mô tả máy khách (client / 클라이언트) cấu hình (config / 설정) là nhóm setting liên quan trình duyệt (browser / 브라우저)/UI/thời gian chạy (runtime / 런타임) phía máy khách (client / 클라이언트), còn máy chủ (server / 서버) cấu hình (config / 설정) là nhóm setting cho WebSquare Engine/máy chủ (server / 서버) hành vi (behavior / 동작) như mô-đun (module / 모듈) processing, Excel/CSV, khung phần mềm (framework / 프레임워크) adaptor, multilingual và Hybrid.

Trong sản phẩm tạo ra (artifact / 산출물)/thời gian chạy (runtime / 런타임), các tệp (file / 파일) nền như `config.xml` và `websquare.xml` vẫn xuất hiện trong documentation/cấu hình (config / 설정) mô hình (model / 모델). Tên tệp (file / 파일) cụ thể và cách Studio materialize chúng có thể khác theo dự án (project / 프로젝트)/generation, vì vậy hãy phân biệt **logical cấu hình (configuration / 구성) role** với **một filename bạn nhớ từ dự án (project / 프로젝트) cũ**.

Mô hình tư duy (mental model / 사고 모델):

```text
client configuration
→ browser/runtime/page behavior

server configuration
→ engine/server-side behavior
```

Một thuộc tính (property / 속성) ở máy khách (client / 클라이언트) không thể thay thế máy chủ (server / 서버) bảo mật (security / 보안) chính sách (policy / 정책); một máy chủ (server / 서버) setting cũng không tự sửa page JavaScript lô-gic (logic / 논리).

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **6. máy khách (client / 클라이언트) cấu hình (configuration / 구성) và máy chủ (server / 서버) cấu hình (configuration / 구성) là hai ranh giới (boundary / 경계) khác nhau** đặt tiêu chí; **7. cấu hình (configuration / 구성) is mã (code / 코드)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **8. Environment-specific cấu hình (config / 설정) không nên biến nguồn (source / 소스) thành nhiều fork** mở rộng hệ quả.

## 7. cấu hình (configuration / 구성) is mã (code / 코드)

Cấu hình (config / 설정) thay đổi hành vi (behavior / 동작) môi trường vận hành (production / 운영 환경), nên cần rà soát (review / 검토), phiên bản (version / 버전) lịch sử (history / 이력) và quay lui (rollback / 롤백) giống mã (code / 코드).

Một thay đổi nhỏ như ngữ cảnh (context / 맥락) gốc (root / 루트), gỡ lỗi (debug / 디버그) chế độ (mode / 모드), Submission default, engine kiểu (type / 타입), bộ nhớ đệm (cache / 캐시) hoặc locale có thể ảnh hưởng hàng trăm page mà không sửa một dòng XML page nào.

Do đó cấu hình (config / 설정) thay đổi (change / 변경) nên trả lời:

```text
vì sao đổi
scope environment nào
default cũ/mới
backward compatibility
security/performance consequence
rollback path
regression area
```

Không nên chỉnh trực tiếp môi trường vận hành (production / 운영 환경) cấu hình (config / 설정) rồi “sau này cập nhật Git”. Khi đó nguồn chuẩn (source of truth / 정본) đã bị đảo ngược.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **7. cấu hình (configuration / 구성) is mã (code / 코드)** đặt vấn đề; **8. Environment-specific cấu hình (config / 설정) không nên biến nguồn (source / 소스) thành nhiều fork** đối chiếu bằng chứng, rồi **9. Secret không thuộc máy khách (client / 클라이언트) cấu hình (config / 설정)** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. Environment-specific cấu hình (config / 설정) không nên biến nguồn (source / 소스) thành nhiều fork

Cục bộ (local / 로컬), DEV, UAT và PROD cần endpoint/ngữ cảnh (context / 맥락)/log mức (level / 수준) khác nhau. Cách nguy hiểm là bản sao (copy / 복사) cả dự án (project / 프로젝트) thành bốn phiên bản rồi sửa tay.

Tốt hơn là có chuẩn gốc (canonical / 정본) nguồn (source / 소스) và tường minh (explicit / 명시적) môi trường (environment / 환경) đầu vào (input / 입력)/overlay theo chuỗi xử lý (pipeline / 파이프라인) của tổ chức.

Mô hình tư duy (mental model / 사고 모델):

```text
canonical application source
+
environment-specific values
→ resolved deploy configuration
```

Không hard-code môi trường vận hành (production / 운영 환경) URL trong page nếu môi trường (environment / 환경) cơ chế (mechanism / 메커니즘) đã tồn tại.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **8. Environment-specific cấu hình (config / 설정) không nên biến nguồn (source / 소스) thành nhiều fork** đặt vấn đề; **9. Secret không thuộc máy khách (client / 클라이언트) cấu hình (config / 설정)** đối chiếu bằng chứng, rồi **10. ngữ cảnh (context / 맥락) gốc (root / 루트) là routing đặc tả hợp đồng (contract / 계약)** mở rộng hệ quả hoặc giới hạn liên quan.

## 9. Secret không thuộc máy khách (client / 클라이언트) cấu hình (config / 설정)

Bất cứ thứ gì trình duyệt (browser / 브라우저) tải được đều có thể bị người dùng (user / 사용자) inspect. Vì vậy API secret, private key, cơ sở dữ liệu (database / 데이터베이스) password hoặc credential privileged không được đặt vào client-side WebSquare cấu hình (config / 설정), JavaScript hay DataCollection với hy vọng “obfuscation sẽ che”.

W-Pack obfuscation/minification làm nguồn (source / 소스) khó đọc hơn, không tạo ranh giới bảo mật (security boundary / 보안 경계).

Secret management thuộc máy chủ (server / 서버)/triển khai (deployment / 배포) nền tảng (platform / 플랫폼).

> **Nối mạch:** Secret phải ở server-side; root context tiếp theo quyết định routing contract, còn build engine dependency phải được pin và truy vết trong production.

## 10. ngữ cảnh (context / 맥락) gốc (root / 루트) là routing đặc tả hợp đồng (contract / 계약)

Ngữ cảnh (context / 맥락) gốc (root / 루트) ảnh hưởng cách page/tài nguyên (resource / 자원)/yêu cầu (request / 요청) được resolve. Một app chạy ở `/` cục bộ (local / 로컬) nhưng môi trường vận hành (production / 운영 환경) ở `/bank/app/` có thể lộ hard-coded absolute đường dẫn (path / 경로).

Kiểm thử (test / 테스트) cần bao phủ:

```text
WFrame src
Submission action
image/static resource
common JS/CSS
popup/page navigation
upload/download endpoint
```

Không phải mọi servlet/tài nguyên (resource / 자원) đều nhất thiết áp dụng cùng context-root quy tắc (rule / 규칙) trong mọi bản dựng (build / 빌드). bản phát hành (release / 릴리스) ghi chú (note / 노트) SP5 từng thay đổi hành vi (behavior / 동작) `contextRoot` cho nhiều loại tài nguyên (resource / 자원), nên chính xác (exact / 정확한) hành vi (behavior / 동작) phải kiểm chứng theo engine bản dựng (build / 빌드).

Cấp cao (senior / 시니어) ghi chú (note / 노트): đường dẫn (path / 경로) bug thường bị hiểu nhầm thành “WFrame không tải (load / 로드)” hoặc “Submission lỗi”, trong khi nguyên nhân gốc (root cause / 근본 원인) là URL resolution.

> **Nối mạch:** Root context xác định route và asset boundary; engine build dependency kế tiếp giải thích vì sao `engineType` có thể khác behavior giữa development và production.

## 11. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경)

Hai môi trường (environment / 환경) cùng ứng dụng (application / 애플리케이션) nguồn (source / 소스) nhưng khác WebSquare engine bản dựng (build / 빌드) không phải cùng thời gian chạy (runtime / 런타임).

Bản phát hành (release / 릴리스) ghi chú (note / 노트) SP5 cho thấy engine liên tục sửa hành vi (behavior / 동작) của WFrame, TabControl, cấu hình (config / 설정), W-Pack, bộ nhớ đệm (cache / 캐시) và nhiều thành phần (component / 컴포넌트). Vì vậy sự cố (incident / 인시던트) report nên ghi chính xác (exact / 정확한) engine bản dựng (build / 빌드), không chỉ “WebSquare5 SP5”.

Phiên bản (version / 버전) inventory tối thiểu:

```text
application release
WebSquare engine build
Studio/W-Pack build dùng để tạo artifact
browser version
server/WAS relevant version
```

Nếu UAT và PROD khác engine bản dựng (build / 빌드), regression kết quả (result / 결과) UAT không hoàn toàn đại diện PROD.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **12. engineType và development/môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작)** nối từ **11. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) môi trường vận hành (production / 운영 환경)** sang **13. gỡ lỗi (debug / 디버그) cấu hình (configuration / 구성) không được leak sang môi trường vận hành (production / 운영 환경) vô thức**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. `engineType` và development/môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작)

SP5 máy chủ (server / 서버) cấu hình (configuration / 구성) có `engineType` với các mức remapping/gỡ lỗi (debug / 디버그)/log khác nhau. Official guide khuyến nghị development và môi trường vận hành (production / 운영 환경) dùng chế độ (mode / 모드) phù hợp khác nhau; môi trường vận hành (production / 운영 환경) thường dùng engine đã loại bớt gỡ lỗi (debug / 디버그) thông tin (information / 정보) để giảm footprint.

Đừng học con số như magic constant. Điều cần hiểu là sự đánh đổi (trade-off / 트레이드오프):

```text
nhiều debug metadata/log
→ dễ diagnose hơn
→ artifact/runtime nặng hơn hoặc lộ nhiều detail hơn

production-optimized engine
→ nhỏ/gọn hơn
→ diagnosis có thể cần source map/log strategy tốt hơn
```

Trước khi đổi engine kiểu (type / 타입), kiểm tra tính tương thích (compatibility / 호환성) và khả năng quan sát (observability / 관측 가능성) yêu cầu (requirement / 요구사항) của site.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **13. gỡ lỗi (debug / 디버그) cấu hình (configuration / 구성) không được leak sang môi trường vận hành (production / 운영 환경) vô thức** nối từ **12. engineType và development/môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작)** sang **14. bộ nhớ đệm (cache / 캐시) là một phần của triển khai (deployment / 배포) ngữ nghĩa (semantics / 의미론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. gỡ lỗi (debug / 디버그) cấu hình (configuration / 구성) không được leak sang môi trường vận hành (production / 운영 환경) vô thức

Máy khách (client / 클라이언트) cấu hình (config / 설정) có các setting liên quan gỡ lỗi (debug / 디버그)/console/gỡ lỗi (debug / 디버그) menu ở các bản dựng (build / 빌드) tương ứng. Chúng hữu ích ở development nhưng có thể tạo noise hoặc expose operational detail nếu bật không chủ đích ở môi trường vận hành (production / 운영 환경).

Môi trường vận hành (production / 운영 환경) chính sách (policy / 정책) nên quyết định rõ:

```text
console logging mức nào
remote log có hay không
context debug menu có cho phép không
source map public/private
PII redaction
client exception reporting
```

Không phải “môi trường vận hành (production / 운영 환경) thì tắt hết log”. môi trường vận hành (production / 운영 환경) cần khả năng quan sát (observability / 관측 가능성), nhưng tín hiệu (signal / 신호) phải có chủ đích và an toàn.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **14. bộ nhớ đệm (cache / 캐시) là một phần của triển khai (deployment / 배포) ngữ nghĩa (semantics / 의미론)** nối từ **13. gỡ lỗi (debug / 디버그) cấu hình (configuration / 구성) không được leak sang môi trường vận hành (production / 운영 환경) vô thức** sang **15. bộ nhớ đệm (cache / 캐시) key phải gắn với sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. bộ nhớ đệm (cache / 캐시) là một phần của triển khai (deployment / 배포) ngữ nghĩa (semantics / 의미론)

WebSquare app có nhiều lớp bộ nhớ đệm (cache / 캐시) có thể cùng tồn tại:

```text
browser HTTP cache
reverse proxy/CDN cache
web server static cache
engine/config cache
service worker nếu application dùng
```

Deploy nguồn (source / 소스) mới nhưng bộ nhớ đệm (cache / 캐시) cũ vẫn phục vụ sản phẩm tạo ra (artifact / 산출물) cũ tạo trạng thái khó hiểu: HTML shell mới + dùng chung (common / 공통) JS cũ + page W-Pack mới, hoặc ngược lại.

Vì vậy bản phát hành (release / 릴리스) phải có bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화)/versioning chiến lược (strategy / 전략). “Ctrl+F5 là được” không phải môi trường vận hành (production / 운영 환경) chiến lược (strategy / 전략).

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **15. bộ nhớ đệm (cache / 캐시) key phải gắn với sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)** nối từ **14. bộ nhớ đệm (cache / 캐시) là một phần của triển khai (deployment / 배포) ngữ nghĩa (semantics / 의미론)** sang **16. Static compression và mạng (network / 네트워크) cấu hình (configuration / 구성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. bộ nhớ đệm (cache / 캐시) key phải gắn với sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)

Một cách phổ biến là phiên bản (version / 버전)/băm (hash / 해시) trong tài nguyên (resource / 자원) URL hoặc postfix theo cơ chế (mechanism / 메커니즘) của nền tảng (platform / 플랫폼)/dự án (project / 프로젝트). SP5 bản phát hành (release / 릴리스) ghi chú (note / 노트) có các năng lực (capability / 역량) liên quan cấu hình (config / 설정)/W-Pack caching ở từng bản dựng (build / 빌드), nhưng chính xác (exact / 정확한) setting thay đổi theo phiên bản (version / 버전).

Mô hình tư duy (mental model / 사고 모델) quan trọng:

```text
artifact content thay đổi
→ cache identity phải thay đổi hoặc cache phải được invalidated
```

Nếu content đổi nhưng URL/bộ nhớ đệm (cache / 캐시) key không đổi và TTL dài, người dùng (user / 사용자) có thể chạy mixed bản phát hành (release / 릴리스).

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **16. Static compression và mạng (network / 네트워크) cấu hình (configuration / 구성)** nối từ **15. bộ nhớ đệm (cache / 캐시) key phải gắn với sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자)** sang **17. sản phẩm tạo ra (artifact / 산출물) manifest**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Static compression và mạng (network / 네트워크) cấu hình (configuration / 구성)

Official hiệu năng (performance / 성능) guide khuyến nghị bộ nhớ đệm (cache / 캐시) header và compression cho static tài nguyên (resource / 자원); mạng (network / 네트워크)/máy chủ (server / 서버) cấu hình (configuration / 구성) có thể ảnh hưởng lớn đến initial tải (load / 로드).

Đừng tối ưu JavaScript vòng lặp (loop / 루프) 20 ms khi môi trường vận hành (production / 운영 환경) đang tải nhiều MB tài nguyên (resource / 자원) không gzip hoặc thực hiện handshake không cần thiết cho hàng chục yêu cầu (request / 요청).

Hiệu năng (performance / 성능) diagnosis phải nhìn waterfall trước khi kết luận khung phần mềm (framework / 프레임워크) chậm.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **17. sản phẩm tạo ra (artifact / 산출물) manifest** nối từ **16. Static compression và mạng (network / 네트워크) cấu hình (configuration / 구성)** sang **18. Generated sản phẩm tạo ra (artifact / 산출물) không phải nơi sửa nguồn (source / 소스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. sản phẩm tạo ra (artifact / 산출물) manifest

Một triển khai (deployment / 배포) mature nên có manifest hoặc siêu dữ liệu (metadata / 메타데이터) tương đương để trả lời:

```text
source commit
build timestamp/id
WebSquare/W-Pack version
config profile
artifact checksum/version
release number
```

Không cần format cụ thể. Mục tiêu là khi người dùng (user / 사용자) gửi screenshot lúc 14:32, nhóm (team / 팀) có thể biết trình duyệt (browser / 브라우저) có khả năng đang chạy bản phát hành (release / 릴리스) nào.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **17. sản phẩm tạo ra (artifact / 산출물) manifest** đặt vấn đề; **18. Generated sản phẩm tạo ra (artifact / 산출물) không phải nơi sửa nguồn (source / 소스)** đối chiếu bằng chứng, rồi **19. bản dựng (build / 빌드) phải thất bại (fail / 실패) khi sản phẩm tạo ra (artifact / 산출물) không đầy đủ** mở rộng hệ quả hoặc giới hạn liên quan.

## 18. Generated sản phẩm tạo ra (artifact / 산출물) không phải nơi sửa nguồn (source / 소스)

Nếu bug được “hotfix” trực tiếp trong `_wpack_/*.js`, nguồn (source / 소스) XML/JS chuẩn gốc (canonical / 정본) không biết thay đổi đó. Lần rebuild sau hotfix biến mất.

Emergency patch đôi khi có operational ràng buộc (constraint / 제약조건) riêng, nhưng sau đó phải reconcile về chuẩn gốc (canonical / 정본) nguồn (source / 소스) ngay và dấu vết (trace / 추적) rõ divergence.

Nguyên tắc:

```text
source là nơi author
artifact là output
production là deployment của artifact
```

Đảo ba vai trò này tạo cấu hình (configuration / 구성)/bản dựng (build / 빌드) debt rất nhanh.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **18. Generated sản phẩm tạo ra (artifact / 산출물) không phải nơi sửa nguồn (source / 소스)** đặt vấn đề; **19. bản dựng (build / 빌드) phải thất bại (fail / 실패) khi sản phẩm tạo ra (artifact / 산출물) không đầy đủ** đối chiếu bằng chứng, rồi **20. dùng chung (common / 공통) tài nguyên (resource / 자원) thay đổi có blast radius lớn** mở rộng hệ quả hoặc giới hạn liên quan.

## 19. bản dựng (build / 빌드) phải thất bại (fail / 실패) khi sản phẩm tạo ra (artifact / 산출물) không đầy đủ

Một chuỗi xử lý (pipeline / 파이프라인) không nên thành công nếu W-Pack báo lỗi nhưng giữ tệp (file / 파일) đầu ra (output / 출력) cũ từ bản dựng (build / 빌드) trước.

Dùng clean đầu ra (output / 출력) hoặc sản phẩm tạo ra (artifact / 산출물) directory mới theo bản dựng (build / 빌드) để tránh stale tệp (file / 파일) masquerade.

Kiểm tra sau bản dựng (build / 빌드):

```text
expected page artifact tồn tại
common module artifact tồn tại
không có fatal build error
manifest trỏ đúng source/build
artifact package không chứa file dev ngoài policy
```

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **19. bản dựng (build / 빌드) phải thất bại (fail / 실패) khi sản phẩm tạo ra (artifact / 산출물) không đầy đủ** đặt vấn đề; **20. dùng chung (common / 공통) tài nguyên (resource / 자원) thay đổi có blast radius lớn** đối chiếu bằng chứng, rồi **21. tải (load / 로드) thứ tự (order / 순서) là phụ thuộc (dependency / 의존성) đặc tả hợp đồng (contract / 계약)** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. dùng chung (common / 공통) tài nguyên (resource / 자원) thay đổi có blast radius lớn

Một dùng chung (common / 공통) JS/CSS/UDC được dùng hàng trăm screen. bản dựng (build / 빌드)/deploy dùng chung (common / 공통) tầng (layer / 계층) vì vậy có rủi ro (risk / 위험) khác page riêng lẻ.

Bản phát hành (release / 릴리스) impact phân tích (analysis / 분석) nên hỏi:

```text
consumer nào dùng resource này
public contract có đổi không
cache key có đổi không
load order có đổi không
Scope/global assumption có đổi không
```

Regression suite phải ưu tiên representative consumers, không chỉ kiểm thử (test / 테스트) demo page của dùng chung (common / 공통) mô-đun (module / 모듈).

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **20. dùng chung (common / 공통) tài nguyên (resource / 자원) thay đổi có blast radius lớn** đặt vấn đề; **21. tải (load / 로드) thứ tự (order / 순서) là phụ thuộc (dependency / 의존성) đặc tả hợp đồng (contract / 계약)** đối chiếu bằng chứng, rồi **22. bên ngoài (external / 외부) JavaScript và third-party phụ thuộc (dependency / 의존성)** mở rộng hệ quả hoặc giới hạn liên quan.

## 21. tải (load / 로드) thứ tự (order / 순서) là phụ thuộc (dependency / 의존성) đặc tả hợp đồng (contract / 계약)

Legacy enterprise app thường có dùng chung (common / 공통) toàn cục (global / 전역) JS phụ thuộc thứ tự tải (load / 로드). W-Pack/dùng chung (common / 공통) mô-đun (module / 모듈) cấu hình (config / 설정) thay đổi có thể làm hidden phụ thuộc (dependency / 의존성) lộ ra.

Nếu `commonB.js` chỉ chạy vì `commonA.js` tình cờ tạo toàn cục (global / 전역) trước, kiến trúc (architecture / 아키텍처) đang phụ thuộc implicit tải (load / 로드) thứ tự (order / 순서).

Hướng tốt hơn là tường minh (explicit / 명시적) phụ thuộc (dependency / 의존성)/mô-đun (module / 모듈) đặc tả hợp đồng (contract / 계약). Nếu chưa thể refactor, ít nhất bản dựng (build / 빌드)/kiểm thử (test / 테스트) phải khóa (lock / 잠금) và kiểm tra thứ tự (order / 순서) có chủ đích.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **22. bên ngoài (external / 외부) JavaScript và third-party phụ thuộc (dependency / 의존성)** nối từ **21. tải (load / 로드) thứ tự (order / 순서) là phụ thuộc (dependency / 의존성) đặc tả hợp đồng (contract / 계약)** sang **23. Deploy atomically khi có thể**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. bên ngoài (external / 외부) JavaScript và third-party phụ thuộc (dependency / 의존성)

Third-party widget/thư viện (library / 라이브러리) cần phiên bản (version / 버전) pinning và quyền sở hữu (ownership / 소유권). CDN URL “latest” làm thời gian chạy (runtime / 런타임) thay đổi mà ứng dụng (application / 애플리케이션) không deploy.

Nếu bên ngoài (external / 외부) script được đưa qua W-Pack cơ chế (mechanism / 메커니즘) ở bản dựng (build / 빌드) hỗ trợ, vẫn phải biết nguồn (source / 소스) phiên bản (version / 버전) và license/bảo mật (security / 보안) chính sách (policy / 정책).

Phụ thuộc (dependency / 의존성) upgrade phải có regression ở screen thật, đặc biệt nếu thư viện (library / 라이브러리) thao tác DOM mà WebSquare cũng quản lý.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **23. Deploy atomically khi có thể** nối từ **22. bên ngoài (external / 외부) JavaScript và third-party phụ thuộc (dependency / 의존성)** sang **24. Backward tính tương thích (compatibility / 호환성) trong rolling triển khai (deployment / 배포)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Deploy atomically khi có thể

Mixed sản phẩm tạo ra (artifact / 산출물) là dạng thất bại (failure mode / 실패 모드) nguy hiểm. Nếu deploy ghi đè tệp (file / 파일) từng phần trong khi người dùng (user / 사용자) đang tải (load / 로드) app, yêu cầu (request / 요청) đầu có thể lấy dùng chung (common / 공통) tệp (file / 파일) cũ, yêu cầu (request / 요청) sau lấy page mới.

Một triển khai (deployment / 배포) tốt cố tạo atomic bản phát hành (release / 릴리스) ranh giới (boundary / 경계) bằng versioned directory, gói (package / 패키지) switch, immutable sản phẩm tạo ra (artifact / 산출물) hoặc cơ chế (mechanism / 메커니즘) tương đương của hạ tầng.

Nếu nền tảng (platform / 플랫폼) không hỗ trợ atomic deploy hoàn toàn, maintenance/bộ nhớ đệm (cache / 캐시) chiến lược (strategy / 전략) phải giảm cửa sổ mixed-version.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **24. Backward tính tương thích (compatibility / 호환성) trong rolling triển khai (deployment / 배포)** nối từ **23. Deploy atomically khi có thể** sang **25. cơ sở dữ liệu (database / 데이터베이스)/backend giao dịch (transaction / 트랜잭션) không thuộc frontend triển khai (deployment / 배포) nhưng ảnh hưởng quay lui (rollback / 롤백)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Backward tính tương thích (compatibility / 호환성) trong rolling triển khai (deployment / 배포)

Nếu frontend mới được phục vụ trong khi backend cũ/mới cùng tồn tại, Đặc tả API (API contract / API 계약) phải tương thích trong rollout cửa sổ (window / 윈도우).

Ví dụ frontend mới gửi trường dữ liệu (field / 필드) `statusReason` nhưng một số backend nút (node / 노드) cũ reject unknown trường dữ liệu (field / 필드). Đây không phải WebSquare bug mà là triển khai (deployment / 배포) tính tương thích (compatibility / 호환성) bug.

Bản phát hành (release / 릴리스) planning phải xem frontend/backend như hệ thống phân tán (distributed system / 분산 시스템) nếu rollout không đồng thời.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **24. Backward tính tương thích (compatibility / 호환성) trong rolling triển khai (deployment / 배포)** đặt vấn đề; **25. cơ sở dữ liệu (database / 데이터베이스)/backend giao dịch (transaction / 트랜잭션) không thuộc frontend triển khai (deployment / 배포) nhưng ảnh hưởng quay lui (rollback / 롤백)** đối chiếu bằng chứng, rồi **26. triển khai (deployment / 배포) smoke kiểm thử (test / 테스트) dựa trên ranh giới (boundary / 경계)** mở rộng hệ quả hoặc giới hạn liên quan.

## 25. cơ sở dữ liệu (database / 데이터베이스)/backend giao dịch (transaction / 트랜잭션) không thuộc frontend triển khai (deployment / 배포) nhưng ảnh hưởng quay lui (rollback / 롤백)

Frontend quay lui (rollback / 롤백) dễ hơn khi API/backend vẫn backward compatible. Nếu bản phát hành (release / 릴리스) đi kèm DB di chuyển (migration / 마이그레이션) destructive, chỉ quay lui (rollback / 롤백) WebSquare sản phẩm tạo ra (artifact / 산출물) có thể không đủ.

Do đó bản phát hành (release / 릴리스) plan trọng yếu (critical / 중요) luồng (flow / 흐름) cần biết:

```text
frontend artifact compatibility
API compatibility
DB migration direction
feature flag nếu có
rollback/roll-forward strategy
```

WebSquare thư viện (library / 라이브러리) không giải thích DB di chuyển (migration / 마이그레이션) internals; hãy dùng backend/cơ sở dữ liệu (database / 데이터베이스) chuẩn gốc (canonical / 정본) docs cho phần đó.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **25. cơ sở dữ liệu (database / 데이터베이스)/backend giao dịch (transaction / 트랜잭션) không thuộc frontend triển khai (deployment / 배포) nhưng ảnh hưởng quay lui (rollback / 롤백)** đặt tiêu chí; **26. triển khai (deployment / 배포) smoke kiểm thử (test / 테스트) dựa trên ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **27. Canary và representative người dùng (user / 사용자) đường dẫn (path / 경로)** mở rộng hệ quả.

## 26. triển khai (deployment / 배포) smoke kiểm thử (test / 테스트) dựa trên ranh giới (boundary / 경계)

Sau deploy, đừng chỉ mở home page. Smoke kiểm thử (test / 테스트) phải chạm các ranh giới (boundary / 경계) dễ sai vì cấu hình (config / 설정)/sản phẩm tạo ra (artifact / 산출물):

```text
engine boot
common CSS/JS load
WFrame child load
Submission action resolve đúng path
DataCollection target mapping
Grid render
popup/navigation
locale resource nếu critical
upload/download nếu release đụng config tương ứng
```

Mục tiêu là phát hiện bản phát hành (release / 릴리스)/cấu hình (config / 설정) issue trong vài phút.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **26. triển khai (deployment / 배포) smoke kiểm thử (test / 테스트) dựa trên ranh giới (boundary / 경계)** đặt tiêu chí; **27. Canary và representative người dùng (user / 사용자) đường dẫn (path / 경로)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **28. quay lui (rollback / 롤백) phải được diễn tập** mở rộng hệ quả.

## 27. Canary và representative người dùng (user / 사용자) đường dẫn (path / 경로)

Nếu hạ tầng cho phép, canary một phần traffic/người dùng (user / 사용자) trước rollout rộng giúp phát hiện trình duyệt (browser / 브라우저)/cấu hình (config / 설정)/môi trường (environment / 환경) issue.

Canary tín hiệu (signal / 신호) nên gồm máy khách (client / 클라이언트) exception, page-load thất bại (failure / 실패), Submission lỗi (error / 오류) tỷ lệ (rate / 비율) và độ trễ (latency / 지연 시간) của trọng yếu (critical / 중요) screen.

Không cần một nền tảng (platform / 플랫폼) khả năng quan sát (observability / 관측 가능성) phức tạp để áp dụng mô hình tư duy (mental model / 사고 모델): bản phát hành (release / 릴리스) nhỏ → quan sát bằng chứng (evidence / 증거) → mở rộng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **27. Canary và representative người dùng (user / 사용자) đường dẫn (path / 경로)** đặt đầu vào cho **28. quay lui (rollback / 롤백) phải được diễn tập**, rồi **29. cấu hình (config / 설정) diff là first-class sự cố (incident / 인시던트) bằng chứng (evidence / 증거)** mở rộng hệ quả hoặc giới hạn liên quan.

## 28. quay lui (rollback / 롤백) phải được diễn tập

Một quay lui (rollback / 롤백) plan chưa từng chạy chỉ là giả thuyết.

Cần biết:

```text
artifact trước nằm ở đâu
cache invalidation khi rollback
config có rollback cùng không
backend/API còn compatible không
session/user state có ảnh hưởng không
```

Nếu quay lui (rollback / 롤백) mất 40 phút vì phải tìm tệp (file / 파일) WAR cũ trên laptop, quy trình phát hành (release process / 릴리스 프로세스) chưa mature.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **28. quay lui (rollback / 롤백) phải được diễn tập** đặt vấn đề; **29. cấu hình (config / 설정) diff là first-class sự cố (incident / 인시던트) bằng chứng (evidence / 증거)** đối chiếu bằng chứng, rồi **30. bảo mật (security / 보안) header và trình duyệt (browser / 브라우저) chính sách (policy / 정책)** mở rộng hệ quả hoặc giới hạn liên quan.

## 29. cấu hình (config / 설정) diff là first-class sự cố (incident / 인시던트) bằng chứng (evidence / 증거)

Khi “DEV chạy, PROD lỗi”, nguồn (source / 소스) diff thường bằng zero. Hãy diff môi trường (environment / 환경):

```text
engine build
client config
server config
context root
reverse proxy rules
security headers
cache/compression
common resource version
backend endpoint
browser policy
```

Đây là cách biến “chỉ môi trường vận hành (production / 운영 환경) mới lỗi” thành một finite tìm kiếm (search / 검색) không gian (space / 공간).

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **29. cấu hình (config / 설정) diff là first-class sự cố (incident / 인시던트) bằng chứng (evidence / 증거)** đặt vấn đề; **30. bảo mật (security / 보안) header và trình duyệt (browser / 브라우저) chính sách (policy / 정책)** đối chiếu bằng chứng, rồi **31. tệp (file / 파일) upload/download cấu hình (configuration / 구성) có operational rủi ro (risk / 위험) riêng** mở rộng hệ quả hoặc giới hạn liên quan.

## 30. bảo mật (security / 보안) header và trình duyệt (browser / 브라우저) chính sách (policy / 정책)

CSP, cookie chính sách (policy / 정책), CORS, SameSite, frame restrictions và proxy header có thể làm hành vi (behavior / 동작) khác cục bộ (local / 로컬).

Ví dụ bên ngoài (external / 외부) script chạy cục bộ (local / 로컬) nhưng bị CSP khối (block / 블록) môi trường vận hành (production / 운영 환경); popup/frame tích hợp (integration / 통합) có thể bị trình duyệt (browser / 브라우저) chính sách (policy / 정책) chặn; cookie session có thể không gửi vì SameSite/lĩnh vực (domain / 도메인)/đường dẫn (path / 경로).

Đừng disable bảo mật (security / 보안) header để “WebSquare chạy được” trước khi hiểu phụ thuộc (dependency / 의존성). Fix phải giữ bảo mật (security / 보안) bất biến (invariant / 불변식) và điều chỉnh tài nguyên (resource / 자원)/tích hợp (integration / 통합) đặc tả hợp đồng (contract / 계약) phù hợp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **31. tệp (file / 파일) upload/download cấu hình (configuration / 구성) có operational rủi ro (risk / 위험) riêng** nối từ **30. bảo mật (security / 보안) header và trình duyệt (browser / 브라우저) chính sách (policy / 정책)** sang **32. Encoding và locale drift**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. tệp (file / 파일) upload/download cấu hình (configuration / 구성) có operational rủi ro (risk / 위험) riêng

SP5 máy chủ (server / 서버) cấu hình (config / 설정) chứa nhiều setting cho upload, Excel và CSV. Những luồng (flow / 흐름) này liên quan temp directory, kích thước (size / 크기), extension/content kiểm tra hợp lệ (validation / 검증), encoding và bộ nhớ (memory / 메모리).

Bản phát hành (release / 릴리스) đụng upload/download cần kiểm thử (test / 테스트) trên môi trường (environment / 환경) gần môi trường vận hành (production / 운영 환경) vì filesystem permission, proxy limit và máy chủ (server / 서버) bộ nhớ (memory / 메모리) khác cục bộ (local / 로컬).

Máy khách (client / 클라이언트) success không chứng minh tệp (file / 파일) đã được lưu/validate an toàn; ranh giới bảo mật (security boundary / 보안 경계) vẫn ở máy chủ (server / 서버).

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **32. Encoding và locale drift** nối từ **31. tệp (file / 파일) upload/download cấu hình (configuration / 구성) có operational rủi ro (risk / 위험) riêng** sang **33. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) ma trận (matrix / 행렬) là bản phát hành (release / 릴리스) đầu vào (input / 입력)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Encoding và locale drift

Korean enterprise hệ thống (system / 시스템) có thể gặp UTF-8, legacy encoding hoặc byte-length kiểm tra hợp lệ (validation / 검증) khác nhau. Một cấu hình (config / 설정) encoding khác giữa môi trường (environment / 환경) có thể tạo lỗi chỉ với Korean/Vietnamese văn bản (text / 텍스트).

Regression dữ liệu (data / 데이터) nên chứa:

```text
한글
Tiếng Việt có dấu
ASCII
emoji nếu business cho phép
boundary byte length
```

Đừng chỉ kiểm thử (test / 테스트) `TEST123` rồi kết luận encoding đúng.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **33. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) ma trận (matrix / 행렬) là bản phát hành (release / 릴리스) đầu vào (input / 입력)** nối từ **32. Encoding và locale drift** sang **34. khả năng quan sát (observability / 관측 가능성) phải sống qua minification**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) ma trận (matrix / 행렬) là bản phát hành (release / 릴리스) đầu vào (input / 입력)

Official WebSquare engine documentation có mức hỗ trợ trình duyệt (browser support / 브라우저 지원) chính sách (policy / 정책) theo engine generation. ứng dụng (application / 애플리케이션) thực tế có thể đặt chính sách (policy / 정책) hẹp hơn hoặc còn legacy yêu cầu (requirement / 요구사항).

Bản phát hành (release / 릴리스) phải biết trình duyệt (browser / 브라우저) nào là supported mục tiêu (target / 대상). Nếu mã (code / 코드) dùng hiện đại (modern / 현대적) JavaScript cú pháp (syntax / 문법)/thư viện (library / 라이브러리), W-Pack/engine/toolchain và trình duyệt (browser / 브라우저) ma trận (matrix / 행렬) phải thống nhất.

Không giữ workaround IE vô hạn chỉ vì mã (code / 코드) cũ có nó; cũng không xóa tính tương thích (compatibility / 호환성) mã (code / 코드) nếu nghiệp vụ (business / 비즈니스) vẫn hỗ trợ trình duyệt (browser / 브라우저) đó.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **34. khả năng quan sát (observability / 관측 가능성) phải sống qua minification** nối từ **33. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) ma trận (matrix / 행렬) là bản phát hành (release / 릴리스) đầu vào (input / 입력)** sang **35. bản phát hành (release / 릴리스) checklist không thay lập luận (reasoning / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. khả năng quan sát (observability / 관측 가능성) phải sống qua minification

Môi trường vận hành (production / 운영 환경) sản phẩm tạo ra (artifact / 산출물) minify/obfuscate làm ngăn xếp (stack / 스택) khó đọc. Vì vậy cần lỗi (error / 오류) correlation, bản dựng (build / 빌드) ID và nguồn (source / 소스) ánh xạ (mapping / 매핑) chiến lược (strategy / 전략) phù hợp.

Một máy khách (client / 클라이언트) lỗi (error / 오류) report hữu ích:

```text
release/build id
engine build
page/scope id
operation
correlation id
sanitized stack/error code
browser
```

Không log full DataList chứa PII chỉ để gỡ lỗi (debug / 디버그) dễ hơn.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **35. bản phát hành (release / 릴리스) checklist không thay lập luận (reasoning / 추론)** nối từ **34. khả năng quan sát (observability / 관측 가능성) phải sống qua minification** sang **36. Example: nguồn (source / 소스) đã sửa nhưng môi trường vận hành (production / 운영 환경) vẫn chạy mã (code / 코드) cũ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. bản phát hành (release / 릴리스) checklist không thay lập luận (reasoning / 추론)

Checklist hữu ích để không quên bước, nhưng không được biến thành ritual.

Ví dụ “clear bộ nhớ đệm (cache / 캐시)” không phải câu trả lời nếu nhóm (team / 팀) không biết bộ nhớ đệm (cache / 캐시) tầng (layer / 계층) nào và vì sao cần clear. “Rebuild W-Pack” không đủ nếu không biết công cụ (tool / 도구) phiên bản (version / 버전) và đầu ra (output / 출력) nào được deploy.

Mỗi bước bản phát hành (release / 릴리스) nên gắn với dạng thất bại (failure mode / 실패 모드) mà nó phòng ngừa.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **35. bản phát hành (release / 릴리스) checklist không thay lập luận (reasoning / 추론)** nêu quy tắc; **36. Example: nguồn (source / 소스) đã sửa nhưng môi trường vận hành (production / 운영 환경) vẫn chạy mã (code / 코드) cũ** thử quy tắc trong tình huống, rồi **37. Example: UAT pass, PROD WFrame 404** mở rộng hệ quả.

## 36. Example: nguồn (source / 소스) đã sửa nhưng môi trường vận hành (production / 운영 환경) vẫn chạy mã (code / 코드) cũ

Triệu chứng: nhà phát triển (developer / 개발자) thấy lần ghi nhận (commit / 커밋) mới, máy chủ (server / 서버) cũng có XML mới, nhưng trình duyệt (browser / 브라우저) hành vi (behavior / 동작) không đổi.

Lập luận (reasoning / 추론) theo chuỗi xử lý (pipeline / 파이프라인):

```text
source commit đúng?
→ W-Pack có rebuild page không?
→ _wpack_ artifact timestamp/hash đúng?
→ package có artifact mới không?
→ server đang serve đúng release directory không?
→ proxy/CDN/browser cache có giữ URL cũ không?
→ Network response body/build marker là version nào?
```

Đừng tiếp tục sửa JavaScript cho đến khi xác định trình duyệt (browser / 브라우저) thực sự chạy sản phẩm tạo ra (artifact / 산출물) nào.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **36. Example: nguồn (source / 소스) đã sửa nhưng môi trường vận hành (production / 운영 환경) vẫn chạy mã (code / 코드) cũ** nêu quy tắc; **37. Example: UAT pass, PROD WFrame 404** thử quy tắc trong tình huống, rồi **38. Example: bản phát hành (release / 릴리스) mới làm initial tải (load / 로드) chậm gấp đôi** mở rộng hệ quả.

## 37. Example: UAT pass, PROD WFrame 404

Nếu cùng nguồn (source / 소스) nhưng WFrame `src` 404 ở PROD, hypothesis đầu tiên nên là routing/cấu hình (config / 설정) chứ không phải phạm vi (scope / 범위).

So:

```text
context root
reverse proxy prefix
resolved WFrame URL
case sensitivity filesystem
artifact path
cache/rewrite rule
```

Sau khi page tải (load / 로드) được mới gỡ lỗi (debug / 디버그) phạm vi (scope / 범위)/vòng đời (lifecycle / 생명주기). Đây là ví dụ của tầng (layer / 계층) thứ tự (ordering / 순서) trong troubleshooting.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **37. Example: UAT pass, PROD WFrame 404** nêu quy tắc; **38. Example: bản phát hành (release / 릴리스) mới làm initial tải (load / 로드) chậm gấp đôi** thử quy tắc trong tình huống, rồi **39. CI/CD gate gợi ý theo bằng chứng (evidence / 증거)** mở rộng hệ quả.

## 38. Example: bản phát hành (release / 릴리스) mới làm initial tải (load / 로드) chậm gấp đôi

Tách chi phí (cost / 비용):

```text
artifact size tăng?
request count tăng?
compression mất?
cache miss toàn bộ?
common module load thêm?
eager Tab/WFrame render tăng?
engine/config đổi?
```

Một bản phát hành (release / 릴리스) có thể không đổi nghiệp vụ (business / 비즈니스) mã (code / 코드) nhưng cấu hình (config / 설정) `alwaysDraw`, dùng chung (common / 공통) tài nguyên (resource / 자원) hoặc bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) làm startup chậm mạnh.

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **38. Example: bản phát hành (release / 릴리스) mới làm initial tải (load / 로드) chậm gấp đôi** nêu quy tắc; **39. CI/CD gate gợi ý theo bằng chứng (evidence / 증거)** thử quy tắc trong tình huống, rồi **40. Promote sản phẩm tạo ra (artifact / 산출물), không rebuild vô thức** mở rộng hệ quả.

## 39. CI/CD gate gợi ý theo bằng chứng (evidence / 증거)

Một chuỗi xử lý (pipeline / 파이프라인) production-oriented có thể đi theo:

```text
source checkout tại commit cố định
→ static/syntax checks
→ W-Pack clean build
→ artifact integrity check
→ logic/integration tests
→ package immutable artifact
→ deploy DEV/UAT
→ smoke/regression
→ promote cùng artifact
→ production smoke
→ observe release metrics
```

Điểm quan trọng là **promote cùng sản phẩm tạo ra (artifact / 산출물)** khi có thể. Nếu UAT bản dựng (build / 빌드) một lần rồi PROD rebuild lại từ nguồn (source / 소스), bạn đã kiểm thử (test / 테스트) sản phẩm tạo ra (artifact / 산출물) A nhưng deploy sản phẩm tạo ra (artifact / 산출물) B.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **39. CI/CD gate gợi ý theo bằng chứng (evidence / 증거)** đặt vấn đề; **40. Promote sản phẩm tạo ra (artifact / 산출물), không rebuild vô thức** đối chiếu bằng chứng, rồi **41. môi trường vận hành (production / 운영 환경) thay đổi (change / 변경) log nên ghi hành vi (behavior / 동작), không chỉ lần ghi nhận (commit / 커밋)** mở rộng hệ quả hoặc giới hạn liên quan.

## 40. Promote sản phẩm tạo ra (artifact / 산출물), không rebuild vô thức

Build-once-promote là mô hình tư duy (mental model / 사고 모델) mạnh cho reproducibility:

```text
commit C
→ artifact A
→ test A ở UAT
→ deploy chính A lên PROD
```

Environment-specific secret/cấu hình (config / 설정) có thể được inject/resolve theo nền tảng (platform / 플랫폼), nhưng ứng dụng (application / 애플리케이션) sản phẩm tạo ra (artifact / 산출물) cốt lõi (core / 핵심) không nên thay đổi không dấu vết (trace / 추적) giữa stage.

Nếu bắt buộc rebuild mỗi môi trường (environment / 환경), phải chứng minh bản dựng (build / 빌드) inputs deterministic và diff đầu ra (output / 출력) được kiểm soát.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **41. môi trường vận hành (production / 운영 환경) thay đổi (change / 변경) log nên ghi hành vi (behavior / 동작), không chỉ lần ghi nhận (commit / 커밋)** nối từ **40. Promote sản phẩm tạo ra (artifact / 산출물), không rebuild vô thức** sang **42. cấp cao (senior / 시니어) ghi chú (note / 노트): triển khai (deployment / 배포) kiến trúc (architecture / 아키텍처) là một phần của frontend tính đúng đắn (correctness / 정확성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. môi trường vận hành (production / 운영 환경) thay đổi (change / 변경) log nên ghi hành vi (behavior / 동작), không chỉ lần ghi nhận (commit / 커밋)

Một bản phát hành (release / 릴리스) ghi chú (note / 노트) nội bộ tốt cho WebSquare có thể ghi:

```text
changed pages/UDC/common modules
engine/config change
W-Pack/toolchain change
API contract dependency
cache/context-root impact
migration/rollback note
known risk
```

Điều này giúp sự cố (incident / 인시던트) responder biết nơi tìm trước khi đọc hàng trăm lần ghi nhận (commit / 커밋).

> **Nối mạch:** Ở chặng này của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **42. cấp cao (senior / 시니어) ghi chú (note / 노트): triển khai (deployment / 배포) kiến trúc (architecture / 아키텍처) là một phần của frontend tính đúng đắn (correctness / 정확성)** nối từ **41. môi trường vận hành (production / 운영 환경) thay đổi (change / 변경) log nên ghi hành vi (behavior / 동작), không chỉ lần ghi nhận (commit / 커밋)** sang **43. mô hình tư duy (mental model / 사고 모델) cuối chapter**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. cấp cao (senior / 시니어) ghi chú (note / 노트): triển khai (deployment / 배포) kiến trúc (architecture / 아키텍처) là một phần của frontend tính đúng đắn (correctness / 정확성)

Nếu page chỉ chạy khi nhà phát triển (developer / 개발자) tự clear bộ nhớ đệm (cache / 캐시), tính đúng đắn (correctness / 정확성) chưa hoàn chỉnh.

Nếu bản dựng (build / 빌드) chỉ thành công trên một Studio cá nhân, delivery chưa reproducible.

Nếu PROD khác UAT engine bản dựng (build / 빌드) mà không ai biết, regression bằng chứng (evidence / 증거) yếu.

Nếu quay lui (rollback / 롤백) cần sửa tệp (file / 파일) tay, bản phát hành (release / 릴리스) ranh giới (boundary / 경계) không rõ.

Frontend kỹ thuật (engineering / 엔지니어링) môi trường vận hành (production / 운영 환경) không kết thúc ở `scwin` hàm (function / 함수). Nó kết thúc khi đúng sản phẩm tạo ra (artifact / 산출물), đúng cấu hình (config / 설정), đúng phụ thuộc (dependency / 의존성) được phục vụ có thể quan sát và quay lui (rollback / 롤백) được.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **43. mô hình tư duy (mental model / 사고 모델) cuối chapter** tổng hợp từ **42. cấp cao (senior / 시니어) ghi chú (note / 노트): triển khai (deployment / 배포) kiến trúc (architecture / 아키텍처) là một phần của frontend tính đúng đắn (correctness / 정확성)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Nguồn đối chiếu** mở rộng hệ quả hoặc giới hạn liên quan.

## 43. mô hình tư duy (mental model / 사고 모델) cuối chapter

Hãy nhìn mỗi bản phát hành (release / 릴리스) theo chuỗi:

```text
canonical source
→ deterministic build inputs
→ W-Pack/runtime artifact
→ immutable release identity
→ environment configuration
→ deployment/routing/cache
→ browser execution
→ observable evidence
→ rollback or roll-forward
```

Khi có sự cố (incident / 인시던트), đi ngược chuỗi bằng bằng chứng (evidence / 증거). Đừng giả định tầng (layer / 계층) trước đúng chỉ vì tầng (layer / 계층) sau trông quen thuộc.

> **Nối mạch:** Trong **12 — bản dựng (build / 빌드), cấu hình (configuration / 구성), triển khai (deployment / 배포) & môi trường (environment / 환경) lập luận (reasoning / 추론)**, **43. mô hình tư duy (mental model / 사고 모델) cuối chapter** đã nêu tiêu chí phân biệt, còn **Nguồn đối chiếu** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nguồn đối chiếu

Các fact WebSquare-specific trong chapter này dựa trên WebSquare5 SP5 Development Guide, đặc biệt phần dự án (project / 프로젝트) cấu hình (configuration / 구성), JS Conversion/W-Pack, máy khách (client / 클라이언트) cấu hình (configuration / 구성), máy chủ (server / 서버) cấu hình (configuration / 구성), debugging và hiệu năng (performance / 성능) guide; đồng thời bản phát hành (release / 릴리스) ghi chú (note / 노트) SP5 được dùng để nhấn mạnh rằng cấu hình (config / 설정)/W-Pack/WFrame hành vi (behavior / 동작) thay đổi theo engine bản dựng (build / 빌드). chính xác (exact / 정확한) option/default phải luôn được kiểm tra lại với tài liệu của bản dựng (build / 빌드) dự án (project / 프로젝트) đang chạy.

> **Bàn giao:** Sau **Nguồn đối chiếu**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
