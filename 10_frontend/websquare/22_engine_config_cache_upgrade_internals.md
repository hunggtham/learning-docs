# 22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. thời gian chạy (runtime / 런타임) không phải một tệp (file / 파일)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. trình duyệt (browser / 브라우저) lời gọi (call / 호출) chuỗi (chain / 사슬)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối engine, config, cache và upgrade, để truy nguyên thay đổi runtime từ cấu hình đọc vào đến artifact và trạng thái đã cache.

Một trong những câu khó nhất trong môi trường vận hành (production / 운영 환경) WebSquare là: **trình duyệt (browser / 브라우저) đang chạy chính xác cái gì?**

Nhà phát triển (developer / 개발자) thường nhìn XML nguồn (source / 소스) trên Git và nghĩ đó là thời gian chạy (runtime / 런타임). Nhưng WebSquare5 có Engine, W-Pack sản phẩm tạo ra (artifact / 산출물), máy khách (client / 클라이언트)/máy chủ (server / 서버) cấu hình (configuration / 구성), tài nguyên (resource / 자원) bộ nhớ đệm (cache / 캐시), web máy chủ (server / 서버)/proxy bộ nhớ đệm (cache / 캐시) và trình duyệt (browser / 브라우저) bộ nhớ đệm (cache / 캐시). Cùng một lần ghi nhận (commit / 커밋) có thể tạo hành vi (behavior / 동작) khác nếu engine bản dựng (build / 빌드) hoặc cấu hình (config / 설정) khác; cùng một môi trường (environment / 환경) có thể phục vụ sản phẩm tạo ra (artifact / 산출물) khác cho hai trình duyệt (browser / 브라우저) nếu bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자) không được kiểm soát.

Chapter 12 đã giải thích bản dựng (build / 빌드)/triển khai (deployment / 배포) chuỗi xử lý (pipeline / 파이프라인). Chapter này đi sâu hơn vào **thời gian chạy (runtime / 런타임) composition, cấu hình (configuration / 구성) precedence, bộ nhớ đệm (cache / 캐시) layers, engine bản dựng (build / 빌드) định danh (identity / 식별자) và upgrade lập luận (reasoning / 추론)**.

> mô hình tư duy (mental model / 사고 모델) chính: `runtime behavior = source + generated artifact + engine build + configuration + resource resolution + browser state`.

## 1. thời gian chạy (runtime / 런타임) không phải một tệp (file / 파일)

Một WebSquare screen có thể phụ thuộc:

```text
websquare.html / bootstrap
WebSquare Engine resources
client configuration
server/engine configuration
W-Pack JS artifact
common JS/component
UDC/template-derived source
language pack
CSS/image/font
business API
browser cache/state
```

Khi chỉ một tầng (layer / 계층) stale, symptom có thể trông như mã (code / 코드) bug.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **1. thời gian chạy (runtime / 런타임) không phải một tệp (file / 파일)** xác định đầu vào; **2. trình duyệt (browser / 브라우저) lời gọi (call / 호출) chuỗi (chain / 사슬)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. nguồn (source / 소스) đồ thị (graph / 그래프) và thời gian chạy (runtime / 런타임) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. trình duyệt (browser / 브라우저) lời gọi (call / 호출) chuỗi (chain / 사슬)

Official SP5 guide mô tả luồng (flow / 흐름) ở mức khái niệm:

```text
browser calls page
→ WebSquare bootstrap/engine starts
→ page source path resolved
→ W-Pack-generated JavaScript loaded
→ Engine creates/render page
```

Điều quan trọng là XML authoring nguồn (source / 소스) và JS thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물) không phải cùng định danh (identity / 식별자).

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **2. trình duyệt (browser / 브라우저) lời gọi (call / 호출) chuỗi (chain / 사슬)** nêu điều cần giải thích; **3. nguồn (source / 소스) đồ thị (graph / 그래프) và thời gian chạy (runtime / 런타임) đồ thị (graph / 그래프)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) thực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. nguồn (source / 소스) đồ thị (graph / 그래프) và thời gian chạy (runtime / 런타임) đồ thị (graph / 그래프)

Nguồn (source / 소스) đồ thị (graph / 그래프):

```text
XML
JS source
CSS
config source
```

Thời gian chạy (runtime / 런타임) đồ thị (graph / 그래프):

```text
engine bundle
config.js/runtime config
_wpack_ artifact
common modules
cached resources
```

Gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경) phải quan sát thời gian chạy (runtime / 런타임) đồ thị (graph / 그래프).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **3. nguồn (source / 소스) đồ thị (graph / 그래프) và thời gian chạy (runtime / 런타임) đồ thị (graph / 그래프)** nêu điều cần giải thích; **4. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) thực** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. engineType và dev/prod hành vi (behavior / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Engine bản dựng (build / 빌드) là phụ thuộc (dependency / 의존성) thực

Tên “WebSquare5 SP5” chưa đủ.

Bản phát hành (release / 릴리스) ghi chú (note / 노트) dùng bản dựng (build / 빌드) định danh (identity / 식별자) chi tiết. thuộc tính (property / 속성), default, bug fix, bảo mật (security / 보안) hành vi (behavior / 동작) và thành phần (component / 컴포넌트) internals có thể thay đổi giữa bản dựng (build / 빌드).

Do đó sự cố (incident / 인시던트) report nên có:

```text
product generation
SP/build version
Studio/build tool version nếu liên quan
W-Pack build identity
browser version
```

> **Chuyển mạch:** Engine build là dependency thực; engineType và dev/prod behavior phải được kiểm chứng trước khi tách client config khỏi server config.

## 5. `engineType` và dev/prod hành vi (behavior / 동작)

SP5 máy chủ (server / 서버) cấu hình (configuration / 구성) có `engineType` để điều khiển mức ánh xạ (mapping / 매핑)/minification/gỡ lỗi (debug / 디버그)/log hành vi (behavior / 동작) của engine. Official guide khuyến nghị cấu hình (configuration / 구성) khác cho development và môi trường vận hành (production / 운영 환경) ở các mức tương ứng.

Không học thuộc một con số mà bỏ qua bản dựng (build / 빌드). mô hình tư duy (mental model / 사고 모델) là:

```text
development engine
→ debug visibility cao hơn

production engine
→ optimized/minified/log behavior khác
```

Nếu PROD dấu vết ngăn xếp (stack trace / 스택 트레이스) khác DEV, có thể do engine bản dựng (build / 빌드)/kiểu (type / 타입) chứ không phải exception khác.

> **Chuyển mạch:** `engineType` giải thích behavior theo environment; tách client/server config tiếp theo để xác định phần nào có thể public và phần nào là operational code.

## 6. máy khách (client / 클라이언트) cấu hình (config / 설정) vs máy chủ (server / 서버) cấu hình (config / 설정)

SP5 tách cấu hình (configuration / 구성) phía máy khách (client / 클라이언트) và engine/máy chủ (server / 서버).

**máy khách (client / 클라이언트) cấu hình (configuration / 구성)** ảnh hưởng hành vi (behavior / 동작) phía trình duyệt (browser / 브라우저)/thành phần (component / 컴포넌트)/Submission/tài nguyên (resource / 자원) resolution.

**máy chủ (server / 서버) cấu hình (configuration / 구성)** ảnh hưởng engine processing, W-Pack, upload/download, encoding và integration-related hành vi (behavior / 동작).

Tên tệp (file / 파일)/generated biểu diễn (representation / 표현) có thể khác theo dự án (project / 프로젝트)/tooling; hãy dựa vào Studio/official guide đúng bản dựng (build / 빌드).

> **Chuyển mạch:** Config là operational code nên phải review như code; provenance tiếp theo ghi nguồn, version và override chain để debug reproducibly.

## 7. cấu hình (configuration / 구성) là mã (code / 코드) vận hành

Cấu hình (config / 설정) thay đổi hành vi (behavior / 동작) môi trường vận hành (production / 운영 환경) nên phải được rà soát (review / 검토)/phiên bản (version / 버전)/điều khiển (control / 제어) tương tự nguồn (source / 소스).

Anti-pattern:

```text
DEV chỉnh bằng Studio
UAT chỉnh tay trên server
PROD có XML khác nhưng không commit
```

Khi sự cố (incident / 인시던트) xảy ra không ai biết chuẩn gốc (canonical / 정본) cấu hình (config / 설정).

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **8. cấu hình (config / 설정) provenance** tiếp nhận điểm tựa từ **7. cấu hình (configuration / 구성) là mã (code / 코드) vận hành** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. ngữ cảnh (context / 맥락) gốc (root / 루트) là part of tài nguyên (resource / 자원) định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. cấu hình (config / 설정) provenance

Một bản phát hành (release / 릴리스) nên dấu vết (trace / 추적):

```text
source commit
+ config commit/version
+ W-Pack tool/build
+ engine build
→ artifact set
→ environment
```

Nếu cấu hình (config / 설정) được inject theo môi trường (environment / 환경), cần biết đầu vào (input / 입력) nào tạo thời gian chạy (runtime / 런타임) cấu hình (config / 설정) cuối cùng.

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **8. cấu hình (config / 설정) provenance** nêu điều cần giải thích; **9. ngữ cảnh (context / 맥락) gốc (root / 루트) là part of tài nguyên (resource / 자원) định danh (identity / 식별자)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. W-Pack là compiler-like ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. ngữ cảnh (context / 맥락) gốc (root / 루트) là part of tài nguyên (resource / 자원) định danh (identity / 식별자)

Ngữ cảnh (context / 맥락) gốc (root / 루트) ảnh hưởng đường dẫn (path / 경로) resolution của page/tài nguyên (resource / 자원)/API.

Bug điển hình:

```text
DEV: /
PROD: /app
```

Hard-coded absolute/relative đường dẫn (path / 경로) có thể hoạt động ở DEV nhưng 404 ở PROD.

Không fix bằng thêm `../` ngẫu nhiên. Hãy xác định chuẩn gốc (canonical / 정본) path-resolution quy tắc (rule / 규칙).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **9. ngữ cảnh (context / 맥락) gốc (root / 루트) là part of tài nguyên (resource / 자원) định danh (identity / 식별자)** đã nêu tiêu chí phân biệt, còn **10. W-Pack là compiler-like ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **11. Generated sản phẩm tạo ra (artifact / 산출물) không nên sửa tay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. W-Pack là compiler-like ranh giới (boundary / 경계)

W-Pack chuyển page XML thành JavaScript sản phẩm tạo ra (artifact / 산출물) tối ưu cho thời gian chạy (runtime / 런타임).

Hãy lập luận (reasoning / 추론) như trình biên dịch (compiler / 컴파일러) chuỗi xử lý (pipeline / 파이프라인):

```text
source
→ transform
→ generated artifact
→ runtime load
```

Bug có thể ở nguồn (source / 소스), transform cấu hình (config / 설정), stale sản phẩm tạo ra (artifact / 산출물) hoặc thời gian chạy (runtime / 런타임) engine.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **10. W-Pack là compiler-like ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **11. Generated sản phẩm tạo ra (artifact / 산출물) không nên sửa tay** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **12. Clean bản dựng (build / 빌드) khi nào cần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Generated sản phẩm tạo ra (artifact / 산출물) không nên sửa tay

Nếu `_wpack_` JS được generate, sửa trực tiếp tệp (file / 파일) generated tạo divergence:

```text
source says A
generated file manually says B
next build returns A
```

Fix phải ở chuẩn gốc (canonical / 정본) nguồn (source / 소스)/cấu hình (config / 설정)/bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **12. Clean bản dựng (build / 빌드) khi nào cần** tiếp nhận điểm tựa từ **11. Generated sản phẩm tạo ra (artifact / 산출물) không nên sửa tay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. bộ nhớ đệm (cache / 캐시) có nhiều tầng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Clean bản dựng (build / 빌드) khi nào cần

Incremental bản dựng (build / 빌드) nhanh nhưng có thể che stale sản phẩm tạo ra (artifact / 산출물) khi phụ thuộc (dependency / 의존성)/cấu hình (config / 설정) thay đổi.

Khi gặp hành vi (behavior / 동작) không giải thích được:

```text
capture evidence
→ clean generated output
→ rebuild deterministic
→ compare artifact hash/content
```

Không biến “clean everything” thành nghi thức cho mọi bug; dùng khi sản phẩm tạo ra (artifact / 산출물) provenance đáng nghi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **13. bộ nhớ đệm (cache / 캐시) có nhiều tầng** tiếp nhận điểm tựa từ **12. Clean bản dựng (build / 빌드) khi nào cần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. bộ nhớ đệm (cache / 캐시) key là đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. bộ nhớ đệm (cache / 캐시) có nhiều tầng

Ít nhất có thể có:

```text
browser memory cache
browser disk cache
service worker nếu project có
reverse proxy/CDN cache
web server cache
WebSquare engine/resource cache
W-Pack/resource postfix strategy
application cache riêng
```

“Đã Ctrl+F5” không chứng minh mọi tầng đã invalidated.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **14. bộ nhớ đệm (cache / 캐시) key là đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **13. bộ nhớ đệm (cache / 캐시) có nhiều tầng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Postfix per tài nguyên (resource / 자원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. bộ nhớ đệm (cache / 캐시) key là đặc tả hợp đồng (contract / 계약)

Bộ nhớ đệm (cache / 캐시) chỉ đúng khi key thay đổi khi content ngữ nghĩa (semantic / 의미적) thay đổi.

Nếu `common.js` content đổi nhưng URL/bộ nhớ đệm (cache / 캐시) key không đổi và TTL dài, trình duyệt (browser / 브라우저) có thể chạy mã (code / 코드) cũ.

Mẫu (pattern / 패턴) phổ biến:

```text
resource URL + version/postfix/hash
```

SP5 có engine bộ nhớ đệm (cache / 캐시)/postfix cấu hình (configuration / 구성) và các bản dựng (build / 빌드) mới hỗ trợ ánh xạ (mapping / 매핑) postfix theo tệp (file / 파일). chính xác (exact / 정확한) option phải kiểm tra bản phát hành (release / 릴리스) ghi chú (note / 노트)/bản dựng (build / 빌드).

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **14. bộ nhớ đệm (cache / 캐시) key là đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **15. Postfix per tài nguyên (resource / 자원)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. config.js cũng có bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Postfix per tài nguyên (resource / 자원)

Bản phát hành (release / 릴리스) ghi chú (note / 노트) SP5 hiện đại mô tả khả năng cấu hình postfix khác nhau theo tệp (file / 파일). mô hình tư duy (mental model / 사고 모델):

```text
artifact A hash/version → URL A?v=A1
artifact B hash/version → URL B?v=B7
```

Điều này giảm vô hiệu hóa (invalidation / 무효화) toàn bộ khi chỉ một tài nguyên (resource / 자원) đổi, nhưng tăng yêu cầu bản dựng (build / 빌드) manifest/provenance rõ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **15. Postfix per tài nguyên (resource / 자원)** nêu điều cần giải thích; **16. config.js cũng có bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. thành phần (component / 컴포넌트) bộ nhớ đệm (cache / 캐시) và reusable tài nguyên (resource / 자원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. `config.js` cũng có bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자)

Nếu thời gian chạy (runtime / 런타임) cấu hình (configuration / 구성) được materialize thành JS/cấu hình (config / 설정) tài nguyên (resource / 자원), chính cấu hình (config / 설정) cũng có thể bị bộ nhớ đệm (cache / 캐시).

Symptom:

```text
server config đã deploy
browser vẫn dùng config cũ
```

Do đó verify mạng (network / 네트워크) phản hồi (response / 응답)/thời gian chạy (runtime / 런타임) giá trị (value / 값), không chỉ tệp (file / 파일) trên máy chủ (server / 서버).

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **16. config.js cũng có bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자)** nêu điều cần giải thích; **17. thành phần (component / 컴포넌트) bộ nhớ đệm (cache / 캐시) và reusable tài nguyên (resource / 자원)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. API công khai (public API / 공개 API) vs observed nội bộ (internal / 내부) API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. thành phần (component / 컴포넌트) bộ nhớ đệm (cache / 캐시) và reusable tài nguyên (resource / 자원)

Một số SP5 bản phát hành (release / 릴리스) thay đổi cách UDC/TTC/EXC hoặc dùng chung (common / 공통) tài nguyên (resource / 자원) được bộ nhớ đệm (cache / 캐시) trong engine thời gian chạy (runtime / 런타임). Đây là lý do không dựa vào private bộ nhớ đệm (cache / 캐시) internals như công khai (public / 공개) đặc tả hợp đồng (contract / 계약).

Nếu hành vi (behavior / 동작) đổi sau engine upgrade, kiểm tra bản phát hành (release / 릴리스) ghi chú (note / 노트) trước khi workaround bằng toàn cục (global / 전역) reset/hack.

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **17. thành phần (component / 컴포넌트) bộ nhớ đệm (cache / 캐시) và reusable tài nguyên (resource / 자원)** nêu điều cần giải thích; **18. API công khai (public API / 공개 API) vs observed nội bộ (internal / 내부) API** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. Evergreen trình duyệt (browser / 브라우저) làm thời gian chạy (runtime / 런타임) tiếp tục thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. API công khai (public API / 공개 API) vs observed nội bộ (internal / 내부) API

DevTools có thể cho thấy nhiều thuộc tính (property / 속성)/hàm (function / 함수) không có trong official API tham chiếu (reference / 참조).

Không dùng chúng chỉ vì “chạy được”. Official hiệu năng (performance / 성능) guide cũng cảnh báo API không công khai có thể thay đổi và gây khó gỡ lỗi (debug / 디버그) sau upgrade.

Quy tắc (rule / 규칙):

```text
official public API
> documented configuration
> project abstraction
> observed private internals
```

Private nội bộ (internal / 내부) chỉ nên dùng khi vendor hỗ trợ (support / 지원) xác nhận và có tính tương thích (compatibility / 호환성) plan.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **19. Evergreen trình duyệt (browser / 브라우저) làm thời gian chạy (runtime / 런타임) tiếp tục thay đổi** tiếp nhận điểm tựa từ **18. API công khai (public API / 공개 API) vs observed nội bộ (internal / 내부) API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Upgrade là phụ thuộc (dependency / 의존성) di chuyển (migration / 마이그레이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Evergreen trình duyệt (browser / 브라우저) làm thời gian chạy (runtime / 런타임) tiếp tục thay đổi

Ngay cả khi WebSquare bản dựng (build / 빌드) không đổi, Chrome/Edge/Safari/Firefox có thể tự cập nhật (update / 업데이트).

Trình duyệt (browser / 브라우저) thay đổi (change / 변경) có thể ảnh hưởng:

```text
layout
focus
clipboard
download
cookie policy
CORS/security
WebView behavior
performance scheduling
```

Vì vậy tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) phải có trình duyệt (browser / 브라우저) dimension.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **20. Upgrade là phụ thuộc (dependency / 의존성) di chuyển (migration / 마이그레이션)** tiếp nhận điểm tựa từ **19. Evergreen trình duyệt (browser / 브라우저) làm thời gian chạy (runtime / 런타임) tiếp tục thay đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. bản phát hành (release / 릴리스) ghi chú (note / 노트) phải đọc theo impact, không theo số lượng tính năng (feature / 기능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Upgrade là phụ thuộc (dependency / 의존성) di chuyển (migration / 마이그레이션)

Engine upgrade không chỉ là bản sao (copy / 복사) engine folder.

Phải inventory:

```text
public APIs used
version-sensitive properties
legacy `$w`/Scope behavior
private APIs/hacks
Grid event assumptions
WFrame lifecycle assumptions
upload/download config
W-Pack config
hybrid bridge
browser support
```

Sau đó map bản phát hành (release / 릴리스) ghi chú (note / 노트) vào phụ thuộc (dependency / 의존성) thực của dự án (project / 프로젝트).

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **21. bản phát hành (release / 릴리스) ghi chú (note / 노트) phải đọc theo impact, không theo số lượng tính năng (feature / 기능)** tiếp nhận điểm tựa từ **20. Upgrade là phụ thuộc (dependency / 의존성) di chuyển (migration / 마이그레이션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. bản phát hành (release / 릴리스) ghi chú (note / 노트) phải đọc theo impact, không theo số lượng tính năng (feature / 기능)

Một bản phát hành (release / 릴리스) ghi chú (note / 노트) 200 item không cần kiểm thử (test / 테스트) 200 item như nhau.

Classify:

```text
DIRECT — project dùng feature đó
TRANSITIVE — engine/component internal thay đổi có thể ảnh hưởng
SECURITY — phải review dù chưa thấy usage
IRRELEVANT — project không có boundary đó
```

Regression priority dựa trên impact.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **22. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **21. bản phát hành (release / 릴리스) ghi chú (note / 노트) phải đọc theo impact, không theo số lượng tính năng (feature / 기능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Canary/smoke trước full rollout** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)

Ví dụ:

| tầng (layer / 계층) | hiện tại (current / 현재) | mục tiêu (target / 대상) | rủi ro (risk / 위험) |
|---|---|---|---|
| WebSquare Engine | SP5 bản dựng (build / 빌드) A | SP5 bản dựng (build / 빌드) B | sự kiện (event / 이벤트)/bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) |
| W-Pack | công cụ (tool / 도구) A | công cụ (tool / 도구) B | generated sản phẩm tạo ra (artifact / 산출물) |
| trình duyệt (browser / 브라우저) | Chrome N | N+1 | focus/download |
| Hybrid bản địa (native / 네이티브) | app 4.2 | app 4.3 | cầu nối (bridge / 브리지) năng lực (capability / 역량) |
| Backend API | v3 | v3/v4 compat | lược đồ (schema / 스키마) |
| dùng chung (common / 공통) UDC | 7 | 8 | công khai (public / 공개) đặc tả hợp đồng (contract / 계약) |

Ma trận (matrix / 행렬) buộc nhóm (team / 팀) nhìn upgrade như hệ thống (system / 시스템) thay đổi (change / 변경).

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **23. Canary/smoke trước full rollout** tiếp nhận điểm tựa từ **22. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. bộ nhớ đệm (cache / 캐시) rollout và backward tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Canary/smoke trước full rollout

Nếu hạ tầng cho phép, engine/sản phẩm tạo ra (artifact / 산출물) upgrade nên có smoke/canary bằng chứng (evidence / 증거) trước full rollout.

Trọng yếu (critical / 중요) luồng (flow / 흐름):

```text
login
shell load
Search
Grid edit
Save
popup/WFrame
Excel/file
logout
hybrid capability nếu có
```

Không chỉ mở homepage rồi kết luận pass.

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **24. bộ nhớ đệm (cache / 캐시) rollout và backward tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **23. Canary/smoke trước full rollout** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. bản dựng (build / 빌드) định danh (identity / 식별자) phải visible** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. bộ nhớ đệm (cache / 캐시) rollout và backward tính tương thích (compatibility / 호환성)

Trong rollout, trình duyệt (browser / 브라우저) cũ có thể giữ sản phẩm tạo ra (artifact / 산출물) cũ trong khi máy chủ (server / 서버) mới đã deploy.

Do đó API/cấu hình (config / 설정)/tài nguyên (resource / 자원) đặc tả hợp đồng (contract / 계약) phải chịu được overlap hoặc có chiến lược (strategy / 전략) force reload/phiên bản (version / 버전) gate rõ.

Không giả định deploy là atomic đối với mọi trình duyệt (browser / 브라우저).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **25. bản dựng (build / 빌드) định danh (identity / 식별자) phải visible** tiếp nhận điểm tựa từ **24. bộ nhớ đệm (cache / 캐시) rollout và backward tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. thời gian chạy (runtime / 런타임) manifest** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. bản dựng (build / 빌드) định danh (identity / 식별자) phải visible

Hỗ trợ (support / 지원) nên có cách lấy ít nhất:

```text
application build/version
W-Pack/source commit identity
WebSquare engine build
config/environment identity
```

Có thể expose qua diagnostics screen/log header tùy bảo mật (security / 보안) chính sách (policy / 정책).

Không bắt hỗ trợ (support / 지원) hỏi người dùng (user / 사용자) “anh đã clear bộ nhớ đệm (cache / 캐시) chưa?” như bước đầu tiên.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **26. thời gian chạy (runtime / 런타임) manifest** tiếp nhận điểm tựa từ **25. bản dựng (build / 빌드) định danh (identity / 식별자) phải visible** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Diagnostic page** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. thời gian chạy (runtime / 런타임) manifest

Một dự án (project / 프로젝트) mature có thể tạo thời gian chạy (runtime / 런타임) manifest:

```json
{
  "appBuild": "2026.09.22.3",
  "gitCommit": "abc123",
  "websquareEngine": "5.0_5.xxxx",
  "wpackBuild": "...",
  "configVersion": "prod-42"
}
```

Đây là dự án (project / 프로젝트) mẫu (pattern / 패턴), không phải built-in WebSquare format.

Mục tiêu là provenance.

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **27. Diagnostic page** tiếp nhận điểm tựa từ **26. thời gian chạy (runtime / 런타임) manifest** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. hiệu năng (performance / 성능) cấu hình (config / 설정) và bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Diagnostic page

Một nội bộ (internal / 내부) diagnostics screen có thể hiển thị non-secret siêu dữ liệu (metadata / 메타데이터):

```text
screen instance
engine/build
app artifact
config version
API base logical name
browser version
locale
hybrid capability version
```

Không hiển thị đơn vị từ (token / 토큰)/session secret.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **28. hiệu năng (performance / 성능) cấu hình (config / 설정) và bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **27. Diagnostic page** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. engineCache không phải nghiệp vụ (business / 비즈니스) bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. hiệu năng (performance / 성능) cấu hình (config / 설정) và bộ nhớ đệm (cache / 캐시)

Official hiệu năng (performance / 성능) guide nhấn mạnh gzip/compression, static tài nguyên (resource / 자원) caching, keep-alive và WebSquare engine/bộ nhớ đệm (cache / 캐시) cấu hình (configuration / 구성).

Nhưng hiệu năng (performance / 성능) tuning phải đo:

```text
transfer size
cache hit/miss
TTFB
parse/execute
render
```

Bật bộ nhớ đệm (cache / 캐시) không sửa formatter O(n²).

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **29. engineCache không phải nghiệp vụ (business / 비즈니스) bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **28. hiệu năng (performance / 성능) cấu hình (config / 설정) và bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. cấu hình (config / 설정) precedence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. `engineCache` không phải nghiệp vụ (business / 비즈니스) bộ nhớ đệm (cache / 캐시)

Engine/tài nguyên (resource / 자원) bộ nhớ đệm (cache / 캐시) tối ưu tài nguyên (resource / 자원) loading. Nó không thay bộ nhớ đệm (cache / 캐시) cho nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터).

Không dùng cùng từ “bộ nhớ đệm (cache / 캐시)” rồi trộn:

```text
engine resource cache
browser HTTP cache
code-list cache
business entity cache
```

Mỗi bộ nhớ đệm (cache / 캐시) có đơn vị sở hữu (owner / 오너)/vô hiệu hóa (invalidation / 무효화) khác nhau.

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **30. cấu hình (config / 설정) precedence** tiếp nhận điểm tựa từ **29. engineCache không phải nghiệp vụ (business / 비즈니스) bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. môi trường (environment / 환경) drift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. cấu hình (config / 설정) precedence

Khi một hành vi (behavior / 동작) có thể cấu hình ở thành phần (component / 컴포넌트), dự án (project / 프로젝트) cấu hình (config / 설정) hoặc default, phải biết precedence đúng bản dựng (build / 빌드).

Ví dụ escape/khả năng tiếp cận (accessibility / 접근성)/kết xuất (render / 렌더링) setting có thể có nhiều mức (level / 수준). Không suy luận từ một dự án (project / 프로젝트) khác.

Khi gỡ lỗi (debug / 디버그):

```text
inspect component explicit value
→ project/runtime config
→ engine default/build behavior
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **31. môi trường (environment / 환경) drift** tiếp nhận điểm tựa từ **30. cấu hình (config / 설정) precedence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): nguồn (source / 소스) mới, UI cũ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. môi trường (environment / 환경) drift

Hai môi trường (environment / 환경) có cùng WAR/nguồn (source / 소스) nhưng khác:

```text
engine build
config
proxy
headers
JVM/server setting
cache
API endpoint
```

thì chúng không phải cùng thời gian chạy (runtime / 런타임) hệ thống (system / 시스템).

Diff môi trường (environment / 환경) phải bao gồm những tầng (layer / 계층) này.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **31. môi trường (environment / 환경) drift** nêu điều cần giải thích; **32. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): nguồn (source / 소스) mới, UI cũ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **33. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): chỉ một người dùng (user / 사용자) lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): nguồn (source / 소스) mới, UI cũ

Bằng chứng (evidence / 증거) chuỗi (chain / 사슬):

```text
Git commit correct
→ artifact built?
→ artifact deployed?
→ URL resolves artifact nào?
→ response cache headers?
→ browser received content/hash nào?
→ engine loaded artifact nào?
```

Không dừng ở “GitHub đã có mã (code / 코드)”.

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **32. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): nguồn (source / 소스) mới, UI cũ** nêu điều cần giải thích; **33. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): chỉ một người dùng (user / 사용자) lỗi** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **34. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): chỉ PROD lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): chỉ một người dùng (user / 사용자) lỗi

Khả năng:

```text
stale browser cache
old tab/runtime
browser extension
browser version
local storage/state
hybrid app version
```

So sánh thời gian chạy (runtime / 런타임) định danh (identity / 식별자) giữa người dùng (user / 사용자) lỗi và người dùng (user / 사용자) bình thường trước khi quay lui (rollback / 롤백) máy chủ (server / 서버).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **34. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): chỉ PROD lỗi** tiếp nhận điểm tựa từ **33. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): chỉ một người dùng (user / 사용자) lỗi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): engine upgrade làm Grid khác hành vi (behavior / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): chỉ PROD lỗi

So sánh:

```text
engine build
client config
server config
W-Pack artifact hash
context root
proxy/cache headers
API route
browser policy
```

Nếu UAT và PROD nguồn (source / 소스) giống nhau nhưng thời gian chạy (runtime / 런타임) inputs khác, nguồn (source / 소스) diff không giúp nhiều.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **35. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): engine upgrade làm Grid khác hành vi (behavior / 동작)** tiếp nhận điểm tựa từ **34. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): chỉ PROD lỗi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. quay lui (rollback / 롤백) phải quay lui (rollback / 롤백) đúng tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): engine upgrade làm Grid khác hành vi (behavior / 동작)

Luồng (flow / 흐름):

```text
capture old/new event trace
→ identify exact build diff
→ search release note/API change
→ reproduce minimal screen
→ remove hidden assumption hoặc set explicit supported config
→ add regression
```

Không pin engine cũ vô thời hạn chỉ vì chưa hiểu nguyên nhân gốc (root cause / 근본 원인).

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **36. quay lui (rollback / 롤백) phải quay lui (rollback / 롤백) đúng tầng (layer / 계층)** tiếp nhận điểm tựa từ **35. môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트): engine upgrade làm Grid khác hành vi (behavior / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. bảo mật (security / 보안) patch và tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. quay lui (rollback / 롤백) phải quay lui (rollback / 롤백) đúng tầng (layer / 계층)

Nếu issue nằm ở cấu hình (config / 설정), quay lui (rollback / 롤백) app sản phẩm tạo ra (artifact / 산출물) có thể không giúp. Nếu issue nằm ở engine, quay lui (rollback / 롤백) nghiệp vụ (business / 비즈니스) mã (code / 코드) có thể che symptom nhưng không sửa phụ thuộc (dependency / 의존성).

Runbook phải biết quay lui (rollback / 롤백) đơn vị (unit / 단위):

```text
application artifact
config
engine build
common resource
backend API
hybrid native release
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **37. bảo mật (security / 보안) patch và tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **36. quay lui (rollback / 롤백) phải quay lui (rollback / 롤백) đúng tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Reproducible bản dựng (build / 빌드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. bảo mật (security / 보안) patch và tính tương thích (compatibility / 호환성)

Bảo mật (security / 보안) bản phát hành (release / 릴리스) có thể thay hành vi (behavior / 동작) tưởng như unrelated, ví dụ logging, upload, IFrame, sanitization hoặc private API.

Không bỏ bảo mật (security / 보안) patch chỉ vì regression kiểm thử (test / 테스트) thất bại (fail / 실패). Cần xác định phụ thuộc (dependency / 의존성) sai/hack nào bị lộ và migrate sang supported đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **38. Reproducible bản dựng (build / 빌드)** tiếp nhận điểm tựa từ **37. bảo mật (security / 보안) patch và tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Branch/bản phát hành (release / 릴리스) hygiene cho thư viện kiến thức (knowledge library / 지식 라이브러리) này** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Reproducible bản dựng (build / 빌드)

Cùng nguồn (source / 소스)/cấu hình (config / 설정)/công cụ (tool / 도구) phiên bản (version / 버전) nên tạo sản phẩm tạo ra (artifact / 산출물) có thể xác định được.

Nếu bản dựng (build / 빌드) phụ thuộc tệp (file / 파일) cục bộ (local / 로컬) không versioned hoặc Studio manual trạng thái (state / 상태), provenance yếu.

W-Pack command-line/CI workflow có giá trị vì giảm hidden workstation trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **39. Branch/bản phát hành (release / 릴리스) hygiene cho thư viện kiến thức (knowledge library / 지식 라이브러리) này** tiếp nhận điểm tựa từ **38. Reproducible bản dựng (build / 빌드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Master thời gian chạy (runtime / 런타임) equation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Branch/bản phát hành (release / 릴리스) hygiene cho thư viện kiến thức (knowledge library / 지식 라이브러리) này

Khi ghi tài liệu WebSquare:

```text
mental model ổn định → canonical chapter
exact API/property → note build-dependent
release-specific change → cite official release note
project workaround → project runbook, không canonicalize mù
```

Thư viện (library / 라이브러리) không nên trở thành bản bản sao (copy / 복사) bản phát hành (release / 릴리스) ghi chú (note / 노트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **40. Master thời gian chạy (runtime / 런타임) equation** tiếp nhận điểm tựa từ **39. Branch/bản phát hành (release / 릴리스) hygiene cho thư viện kiến thức (knowledge library / 지식 라이브러리) này** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Upgrade kiểm thử (test / 테스트) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Master thời gian chạy (runtime / 런타임) equation

Một cách lập luận (reasoning / 추론) hữu ích:

```text
Observed Behavior
= f(
  Source,
  Generated Artifact,
  Engine Build,
  Client Config,
  Server Config,
  Resource Version,
  Browser Runtime,
  Backend Contract,
  Persistent Client State
)
```

Nếu chỉ kiểm tra `Source`, bạn mới kiểm tra một biến.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **41. Upgrade kiểm thử (test / 테스트) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **40. Master thời gian chạy (runtime / 런타임) equation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. liên kết (connection / 연결) map** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Upgrade kiểm thử (test / 테스트) ma trận (matrix / 행렬)

Ít nhất kiểm thử (test / 테스트):

```text
cold cache
warm cache
old tab → deploy → action
new tab after deploy
nested WFrame
lazy tab/preload
Grid edit/save
file/Excel
session expiry
browser current/current-1 theo support policy
hybrid app old/new capability nếu có
```

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **42. liên kết (connection / 연결) map** tiếp nhận điểm tựa từ **41. Upgrade kiểm thử (test / 테스트) ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Master synthesis: 20–22 nối vào toàn thư viện (library / 라이브러리) như thế nào** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. liên kết (connection / 연결) map

Thời gian chạy (runtime / 런타임)/page: [01 — Platform, Runtime & Page Model](01_platform_runtime_page_model.md).

Di chuyển (migration / 마이그레이션): [07 — Legacy, Modern Evolution & Migration](07_legacy_modern_migration.md).

Tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명): [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

Regression kỹ thuật (engineering / 엔지니어링): [11 — Testing, Testability & Regression](11_testing_testability_regression.md).

Bản dựng (build / 빌드)/deploy foundation: [12 — Build, Configuration & Deployment](12_build_config_deployment.md).

Hybrid phiên bản (version / 버전) skew: [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md).

Khả năng quan sát (observability / 관측 가능성): [19 — Observability, Logging & Incident Response](19_observability_incident_response.md).

Tích hợp (integration / 통합)/máy khách (client / 클라이언트) phiên bản (version / 버전) skew: [21 — Integration Topology, MSA, Real-Time & Resilience](21_integration_topology_msa_realtime_resilience.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **43. Master synthesis: 20–22 nối vào toàn thư viện (library / 라이브러리) như thế nào** gom các mảnh từ **42. liên kết (connection / 연결) map** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **44. Capstone Master mở rộng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Master synthesis: 20–22 nối vào toàn thư viện (library / 라이브러리) như thế nào

Ba chapter mới bổ sung ba đồ thị (graph / 그래프) mà một WebSquare Master phải giữ cùng lúc:

```text
Security graph
principal → auth → session → permission → protected command

Integration graph
screen → Submission → gateway/BFF/service → event/result

Runtime provenance graph
source → W-Pack → engine/config → cache → browser
```

Ba đồ thị (graph / 그래프) này giao nhau trong sự cố (incident / 인시던트) thực.

Ví dụ người dùng (user / 사용자) bấm Save sau khi laptop sleep:

```text
Security graph: session đã expire
Integration graph: request đi qua gateway, có thể timeout/retry
Runtime graph: browser tab vẫn giữ page/artifact cũ
```

Nếu chỉ nhìn một đồ thị (graph / 그래프), fix dễ sai.

> **Chuyển mạch:** Trong **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **44. Capstone Master mở rộng** gom các mảnh từ **43. Master synthesis: 20–22 nối vào toàn thư viện (library / 라이브러리) như thế nào** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **45. Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Capstone Master mở rộng

Nâng mini enterprise app của chapter 16 bằng các fault injection:

```text
session expire khi Save
permission bị revoke khi tab đang mở
logout user A → login user B không reload browser
API Gateway timeout sau downstream commit
polling overlap sau browser resume
real-time duplicate/out-of-order event
browser giữ W-Pack cũ sau deploy
engine build UAT/PROD khác nhau
config.js stale trong một browser
hybrid app version cũ gọi web build mới
```

Với mỗi trường hợp (case / 사례) phải trả lời:

```text
invariant nào bị đe dọa?
owner ở layer nào?
identity nào cần log?
operation có thể retry không?
state nào phải invalidate?
evidence nào chứng minh root cause?
regression test nào ngăn tái diễn?
```

> **Chuyển mạch:** Ở chặng này của **22 — Engine, cấu hình (configuration / 구성), bộ nhớ đệm (cache / 캐시) & Upgrade Internals**, **45. Kết luận** gom các mảnh từ **44. Capstone Master mở rộng** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 45. Kết luận

WebSquare Master không coi engine/cấu hình (config / 설정)/bộ nhớ đệm (cache / 캐시) là “phần DevOps bên ngoài mã (code / 코드)”. Chúng là đầu vào (input / 입력) trực tiếp của hành vi thời gian chạy (runtime behavior / 런타임 동작).

Khi có sự cố (incident / 인시던트), câu hỏi đúng không phải chỉ là “mã (code / 코드) nào chạy?”, mà là:

**nguồn (source / 소스) nào → được bản dựng (build / 빌드) thành sản phẩm tạo ra (artifact / 산출물) nào → bằng công cụ (tool / 도구)/cấu hình (config / 설정) nào → chạy trên engine bản dựng (build / 빌드) nào → được resolve/bộ nhớ đệm (cache / 캐시) thành tài nguyên (resource / 자원) nào → trong trình duyệt (browser / 브라우저)/session/bảo mật (security / 보안) trạng thái (state / 상태) nào → gọi đặc tả hợp đồng (contract / 계약) qua topology nào**.

Đó là mức lập luận (reasoning / 추론) giúp phân biệt một workaround tạm thời với một root-cause fix.

> **Bàn giao:** Sau **45. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
