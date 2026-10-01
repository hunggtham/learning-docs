# Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. bản dựng (build / 빌드) thất bại (failure / 실패) và thời gian chạy (runtime / 런타임) thất bại (failure / 실패) có thể cùng nguồn gốc nhưng khác phase** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. Gradle cấu hình (configuration / 구성) đồ thị (graph / 그래프) khác tác vụ (task / 작업) thực thi (execution / 실행) đồ thị (graph / 그래프)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một Android app môi trường vận hành (production / 운영 환경) không chỉ là mã nguồn (source code / 소스 코드) Kotlin chạy đúng trong IDE. mã (code / 코드) phải đi qua Gradle/AGP/Kotlin trình biên dịch (compiler / 컴파일러), tài nguyên (resource / 자원)/manifest merge, D8/R8, packaging, signing, phân phối (distribution / 분포) và nền tảng (platform / 플랫폼) tính tương thích (compatibility / 호환성) trước khi người dùng (user / 사용자) thực sự chạy nó. Nhiều bug chỉ xuất hiện ở bản phát hành (release / 릴리스) bản dựng (build / 빌드), một variant cụ thể, một API mức (level / 수준) mới hoặc sau khi mục tiêu (target / 대상) SDK tăng.

Độ sâu (depth / 깊이) Lab này đào sâu cách lập luận (reasoning / 추론) từ **nguồn (source / 소스) -> bản dựng (build / 빌드) đồ thị (graph / 그래프) -> sản phẩm tạo ra (artifact / 산출물) -> install -> startup -> thời gian chạy (runtime / 런타임) tính tương thích (compatibility / 호환성) -> bản phát hành (release / 릴리스)**.

---

## 1. bản dựng (build / 빌드) thất bại (failure / 실패) và thời gian chạy (runtime / 런타임) thất bại (failure / 실패) có thể cùng nguồn gốc nhưng khác phase

Ví dụ annotation processor generated mã (code / 코드) sai có thể thất bại (fail / 실패) compile.

R8 remove lớp (class / 클래스) dùng reflection có thể compile/bản dựng (build / 빌드) thành công nhưng crash thời gian chạy (runtime / 런타임) bản phát hành (release / 릴리스).

Manifest merge có thể khiến app install được nhưng thành phần (component / 컴포넌트) exported sai.

Hãy luôn hỏi bug xuất hiện ở phase nào:

```text
configuration
compilation
code generation
resource processing
DEX/shrinking
packaging
signing
installation
class loading
startup
runtime behavior
```

Phase xác định loại bằng chứng (evidence / 증거) cần thu thập.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **1. bản dựng (build / 빌드) thất bại (failure / 실패) và thời gian chạy (runtime / 런타임) thất bại (failure / 실패) có thể cùng nguồn gốc nhưng khác phase** nêu điều cần giải thích; **2. Gradle cấu hình (configuration / 구성) đồ thị (graph / 그래프) khác tác vụ (task / 작업) thực thi (execution / 실행) đồ thị (graph / 그래프)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Convention plugin giúp tập trung chính sách (policy / 정책), không chỉ giảm copy-paste** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Gradle cấu hình (configuration / 구성) đồ thị (graph / 그래프) khác tác vụ (task / 작업) thực thi (execution / 실행) đồ thị (graph / 그래프)

Gradle phải đọc bản dựng (build / 빌드) lô-gic (logic / 논리) và tạo mô hình (model / 모델) tác vụ (task / 작업) trước khi execute tác vụ (task / 작업) cần thiết.

Bản dựng (build / 빌드) chậm có thể đến từ:

```text
configuration quá nặng
plugin làm I/O trong configuration
nhiều project/module
non-cacheable task
poor incremental inputs
```

Không phải mọi build-slow issue đều do trình biên dịch (compiler / 컴파일러).

---

> **Chuyển mạch:** Configuration graph và execution graph trả lời hai câu hỏi khác nhau; convention plugin gom policy, còn version catalog chỉ quản lý coordinates chứ không thay dependency policy.

## 3. Convention plugin giúp tập trung chính sách (policy / 정책), không chỉ giảm copy-paste

Nếu 30 mô-đun (module / 모듈) đều bản sao (copy / 복사):

```kotlin
android {
    compileSdk = ...
    kotlinOptions ...
}
```

Cấu hình (config / 설정) dễ drift.

Convention plugin có thể encode chính sách (policy / 정책):

```text
Android library baseline
Compose module baseline
feature module baseline
testing baseline
lint baseline
```

Lợi ích lớn nhất là **quản trị (governance / 거버넌스)**: upgrade toolchain có một số ranh giới (boundary / 경계) rõ thay vì sửa từng mô-đun (module / 모듈) tùy ý.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **4. phiên bản (version / 버전) danh mục (catalog / 카탈로그) quản lý coordinates, không thay phụ thuộc (dependency / 의존성) chính sách (policy / 정책)** tiếp nhận điểm tựa từ **3. Convention plugin giúp tập trung chính sách (policy / 정책), không chỉ giảm copy-paste** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. api vs implementation ảnh hưởng compile đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. phiên bản (version / 버전) danh mục (catalog / 카탈로그) quản lý coordinates, không thay phụ thuộc (dependency / 의존성) chính sách (policy / 정책)

`libs.versions.toml` giúp centralize phiên bản (version / 버전)/alias.

Nhưng nó không tự trả lời:

```text
module nào được phép phụ thuộc library nào?
version nào approved?
transitive dependency nào rủi ro?
```

Danh mục (catalog / 카탈로그) là cú pháp (syntax / 문법)/management công cụ (tool / 도구). phụ thuộc (dependency / 의존성) quản trị (governance / 거버넌스) vẫn cần quy tắc (rule / 규칙) và quyền sở hữu (ownership / 소유권).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **5. api vs implementation ảnh hưởng compile đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **4. phiên bản (version / 버전) danh mục (catalog / 카탈로그) quản lý coordinates, không thay phụ thuộc (dependency / 의존성) chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. bản dựng (build / 빌드) variant là sản phẩm (product / 제품) trạng thái (state / 상태) không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. `api` vs `implementation` ảnh hưởng compile đồ thị (graph / 그래프)

Nếu thư viện (library / 라이브러리) mô-đun (module / 모듈) expose phụ thuộc (dependency / 의존성) kiểu (type / 타입) trong API công khai (public API / 공개 API), bên tiêu thụ (consumer / 소비자) cần phụ thuộc (dependency / 의존성) đó trên compile classpath.

Dùng `api` mở rộng công khai (public / 공개) phụ thuộc (dependency / 의존성) surface.

Dùng `implementation` giữ phụ thuộc (dependency / 의존성) private hơn và có thể giảm recompilation downstream.

Quy tắc (rule / 규칙):

> phụ thuộc (dependency / 의존성) visibility nên phản ánh công khai (public / 공개) ABI, không chỉ “dùng cái nào bản dựng (build / 빌드) được”.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **6. bản dựng (build / 빌드) variant là sản phẩm (product / 제품) trạng thái (state / 상태) không gian (space / 공간)** tiếp nhận điểm tựa từ **5. api vs implementation ảnh hưởng compile đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. nguồn (source / 소스) set precedence cần được hiểu như override đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. bản dựng (build / 빌드) variant là sản phẩm (product / 제품) trạng thái (state / 상태) không gian (space / 공간)

Nếu có:

```text
buildType: debug/release
flavor: free/paid
region: kr/global
```

variant có thể tăng theo tích Descartes:

```text
2 x 2 x 2 = 8 variants
```

Mỗi dimension làm tăng:

```text
CI matrix
manifest/resource override
signing config
test coverage
release complexity
```

Đừng dùng flavor để encode mọi thời gian chạy (runtime / 런타임) cờ tính năng (feature flag / 기능 플래그).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **6. bản dựng (build / 빌드) variant là sản phẩm (product / 제품) trạng thái (state / 상태) không gian (space / 공간)** nêu điều cần giải thích; **7. nguồn (source / 소스) set precedence cần được hiểu như override đồ thị (graph / 그래프)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. Manifest merger là hidden kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. nguồn (source / 소스) set precedence cần được hiểu như override đồ thị (graph / 그래프)

Ví dụ:

```text
src/main
src/free
src/release
src/freeRelease
```

Một tài nguyên (resource / 자원)/lớp (class / 클래스)/cấu hình (config / 설정) có thể được override ở nguồn (source / 소스) set cụ thể.

Bug “gỡ lỗi (debug / 디버그) đúng, bản phát hành (release / 릴리스) sai” thường đến từ source-set divergence.

Khi gỡ lỗi (debug / 디버그) variant-specific issue, inspect merged nguồn (source / 소스)/tài nguyên (resource / 자원)/manifest đầu ra (output / 출력) thay vì chỉ đọc `main`.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **7. nguồn (source / 소스) set precedence cần được hiểu như override đồ thị (graph / 그래프)** đã nêu tiêu chí phân biệt, còn **8. Manifest merger là hidden kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. tài nguyên (resource / 자원) merge cũng có collision và override ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Manifest merger là hidden kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계)

Thư viện (library / 라이브러리) có thể đóng góp:

```text
provider
receiver
service
permission
metadata
```

App final manifest là merge kết quả (result / 결과).

Một SDK thêm auto-init ContentProvider có thể ảnh hưởng startup mà app mã (code / 코드) không gọi trực tiếp.

Do đó final merged manifest là sản phẩm tạo ra (artifact / 산출물) cần rà soát (review / 검토) trong bản phát hành (release / 릴리스) forensic.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **8. Manifest merger là hidden kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **9. tài nguyên (resource / 자원) merge cũng có collision và override ngữ nghĩa (semantics / 의미론)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **10. Generated mã (code / 코드) là part của bản dựng (build / 빌드) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. tài nguyên (resource / 자원) merge cũng có collision và override ngữ nghĩa (semantics / 의미론)

Tên tài nguyên (resource / 자원) toàn cục (global / 전역) trong ứng dụng (application / 애플리케이션) gói (package / 패키지) có thể collision giữa app/thư viện (library / 라이브러리).

Thư viện (library / 라이브러리) author nên prefix tài nguyên (resource / 자원) khi phù hợp.

Bên tiêu thụ (consumer / 소비자) cần hiểu tài nguyên (resource / 자원) override có thể thay thư viện (library / 라이브러리) hành vi (behavior / 동작) nếu thư viện (library / 라이브러리) dùng công khai (public / 공개) tài nguyên (resource / 자원) hook.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **9. tài nguyên (resource / 자원) merge cũng có collision và override ngữ nghĩa (semantics / 의미론)** nêu điều cần giải thích; **10. Generated mã (code / 코드) là part của bản dựng (build / 빌드) đặc tả hợp đồng (contract / 계약)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. KSP di chuyển (migration / 마이그레이션) không chỉ là đổi plugin name** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Generated mã (code / 코드) là part của bản dựng (build / 빌드) đặc tả hợp đồng (contract / 계약)

KSP/trình biên dịch (compiler / 컴파일러) plugin/codegen tạo nguồn (source / 소스) app không viết tay.

Khi generated mã (code / 코드) thất bại (fail / 실패):

```text
input annotation/API changed?
processor/plugin version compatible với Kotlin/AGP?
incremental processing invalidation đúng?
generated source ở đâu?
```

Gỡ lỗi (debug / 디버그) generated mã (code / 코드) bằng cách inspect đầu ra (output / 출력), không coi plugin là “magic”.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **11. KSP di chuyển (migration / 마이그레이션) không chỉ là đổi plugin name** tiếp nhận điểm tựa từ **10. Generated mã (code / 코드) là part của bản dựng (build / 빌드) đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. D8 và R8 giải quyết hai vấn đề khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. KSP di chuyển (migration / 마이그레이션) không chỉ là đổi plugin name

Processor phải hỗ trợ (support / 지원) KSP.

Generated API/hành vi (behavior / 동작) có thể khác.

Bản dựng (build / 빌드) hiệu năng (performance / 성능) có thể tốt hơn, nhưng tính đúng đắn (correctness / 정확성) và tính tương thích (compatibility / 호환성) cần kiểm thử (test / 테스트).

Di chuyển (migration / 마이그레이션) toolchain luôn cần bản phát hành (release / 릴리스) ghi chú (note / 노트) + mẫu (sample / 표본) bản dựng (build / 빌드) + full CI.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **12. D8 và R8 giải quyết hai vấn đề khác nhau** tiếp nhận điểm tựa từ **11. KSP di chuyển (migration / 마이그레이션) không chỉ là đổi plugin name** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Reflection phá static reachability giả định (assumption / 가정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. D8 và R8 giải quyết hai vấn đề khác nhau

Mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
JVM bytecode -> D8 -> DEX
release shrink/optimize/obfuscate -> R8
```

R8 có thể:

```text
remove unused code
inline
rename
rewrite/optimize
```

Vì vậy release-only crash phải nghĩ tới shrinker/reflection/generated siêu dữ liệu (metadata / 메타데이터).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **13. Reflection phá static reachability giả định (assumption / 가정)** tiếp nhận điểm tựa từ **12. D8 và R8 giải quyết hai vấn đề khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Serialization và reflection cần bên tiêu thụ (consumer / 소비자) rules đúng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Reflection phá static reachability giả định (assumption / 가정)

Mã (code / 코드):

```kotlin
Class.forName("com.example.PluginImpl")
```

R8 không luôn suy ra lớp (class / 클래스) cần giữ nếu tham chiếu (reference / 참조) chỉ là string/động (dynamic / 동적) siêu dữ liệu (metadata / 메타데이터).

Keep quy tắc (rule / 규칙) phải càng hẹp càng tốt.

Bad:

```proguard
-keep class ** { *; }
```

sẽ phá shrink benefit.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **14. Serialization và reflection cần bên tiêu thụ (consumer / 소비자) rules đúng** tiếp nhận điểm tựa từ **13. Reflection phá static reachability giả định (assumption / 가정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. ánh xạ (mapping / 매핑) tệp (file / 파일) là môi trường vận hành (production / 운영 환경) debugging sản phẩm tạo ra (artifact / 산출물)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Serialization và reflection cần bên tiêu thụ (consumer / 소비자) rules đúng

SDK/thư viện (library / 라이브러리) có thể cần ship bên tiêu thụ (consumer / 소비자) ProGuard quy tắc (rule / 규칙) để bên tiêu thụ (consumer / 소비자) app không phải tự biết internals.

Thư viện (library / 라이브러리) author phải kiểm thử (test / 테스트):

```text
sample consumer release + minifyEnabled true
```

Không chỉ kiểm thử (test / 테스트) thư viện (library / 라이브러리) mô-đun (module / 모듈) compile.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **15. ánh xạ (mapping / 매핑) tệp (file / 파일) là môi trường vận hành (production / 운영 환경) debugging sản phẩm tạo ra (artifact / 산출물)** tiếp nhận điểm tựa từ **14. Serialization và reflection cần bên tiêu thụ (consumer / 소비자) rules đúng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Signing key là long-term định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. ánh xạ (mapping / 매핑) tệp (file / 파일) là môi trường vận hành (production / 운영 환경) debugging sản phẩm tạo ra (artifact / 산출물)

Sau obfuscation, dấu vết ngăn xếp (stack trace / 스택 트레이스) cần ánh xạ (mapping / 매핑) để deobfuscate.

Bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인) phải lưu/upload ánh xạ (mapping / 매핑) theo bản dựng (build / 빌드) id/phiên bản (version / 버전).

Nếu sản phẩm tạo ra (artifact / 산출물) đã rollout nhưng ánh xạ (mapping / 매핑) thất lạc, crash forensic khó hơn nhiều.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **16. Signing key là long-term định danh (identity / 식별자)** tiếp nhận điểm tựa từ **15. ánh xạ (mapping / 매핑) tệp (file / 파일) là môi trường vận hành (production / 운영 환경) debugging sản phẩm tạo ra (artifact / 산출물)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. bản dựng (build / 빌드) reproducibility giúp forensic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Signing key là long-term định danh (identity / 식별자)

Cập nhật (update / 업데이트) app cần compatible signing định danh (identity / 식별자).

Signing key mất mát (loss / 손실)/rotation là release-engineering sự cố (incident / 인시던트), không phải bản dựng (build / 빌드) detail nhỏ.

Môi trường vận hành (production / 운영 환경) key không nên nằm plain trong repo.

Quyền truy cập signing material cần least privilege/kiểm tra (audit / 감사).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **17. bản dựng (build / 빌드) reproducibility giúp forensic** tiếp nhận điểm tựa từ **16. Signing key là long-term định danh (identity / 식별자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. phụ thuộc (dependency / 의존성) khóa (lock / 잠금) giúp giảm “same nguồn (source / 소스), different nhị phân (binary / 이진)”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. bản dựng (build / 빌드) reproducibility giúp forensic

Khi sự cố (incident / 인시던트) xảy ra, cần trả lời:

```text
source commit nào tạo artifact này?
dependency version chính xác?
toolchain version?
feature config?
signing lineage?
```

Sản phẩm tạo ra (artifact / 산출물) siêu dữ liệu (metadata / 메타데이터) nên nối về nguồn (source / 소스) lần ghi nhận (commit / 커밋) và CI run.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **17. bản dựng (build / 빌드) reproducibility giúp forensic** nêu điều cần giải thích; **18. phụ thuộc (dependency / 의존성) khóa (lock / 잠금) giúp giảm “same nguồn (source / 소스), different nhị phân (binary / 이진)”** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. minSdk, compileSdk, targetSdk là ba contract khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. phụ thuộc (dependency / 의존성) khóa (lock / 잠금) giúp giảm “same nguồn (source / 소스), different nhị phân (binary / 이진)”

Nếu động (dynamic / 동적)/transitive resolution thay đổi theo thời gian, rebuild lần ghi nhận (commit / 커밋) cũ có thể ra phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) khác.

Phụ thuộc (dependency / 의존성) locking/phiên bản (version / 버전) pinning giúp forensic và supply-chain điều khiển (control / 제어).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **18. phụ thuộc (dependency / 의존성) khóa (lock / 잠금) giúp giảm “same nguồn (source / 소스), different nhị phân (binary / 이진)”** nêu điều cần giải thích; **19. minSdk, compileSdk, targetSdk là ba contract khác nhau** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) nên tách compile di chuyển (migration / 마이그레이션) và hành vi (behavior / 동작) di chuyển (migration / 마이그레이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. `minSdk`, `compileSdk`, `targetSdk` là ba contract khác nhau
Phần này nối mạch Android vừa học với “19. `minSdk`, `compileSdk`, `targetSdk` là ba contract khác nhau”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```text
minSdk -> device cũ nhất app hỗ trợ
compileSdk -> API surface compiler biết
 targetSdk -> behavior contract app opt-in với platform mới
```

Tăng compileSdk có thể không đổi hành vi thời gian chạy (runtime behavior / 런타임 동작) ngay.

Tăng targetSdk có thể activate hành vi (behavior / 동작) changes dù mã nguồn (source code / 소스 코드) gần như không đổi.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **20. nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) nên tách compile di chuyển (migration / 마이그레이션) và hành vi (behavior / 동작) di chuyển (migration / 마이그레이션)** tiếp nhận điểm tựa từ **19. minSdk, compileSdk, targetSdk là ba contract khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. hành vi (behavior / 동작) thay đổi (change / 변경) có thể apply cho mọi app hoặc target-gated** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) nên tách compile di chuyển (migration / 마이그레이션) và hành vi (behavior / 동작) di chuyển (migration / 마이그레이션)

Một chiến lược:

```text
Step 1: upgrade toolchain/compileSdk
Step 2: fix compile/deprecation
Step 3: giữ targetSdk cũ, regression test
Step 4: enable target behavior changes có kiểm soát
Step 5: bump targetSdk
Step 6: device/API matrix test
```

Tách dimension giúp giảm số biến thay đổi cùng lúc.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **21. hành vi (behavior / 동작) thay đổi (change / 변경) có thể apply cho mọi app hoặc target-gated** tiếp nhận điểm tựa từ **20. nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) nên tách compile di chuyển (migration / 마이그레이션) và hành vi (behavior / 동작) di chuyển (migration / 마이그레이션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) là di chuyển (migration / 마이그레이션) công cụ (tool / 도구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. hành vi (behavior / 동작) thay đổi (change / 변경) có thể apply cho mọi app hoặc target-gated

Khi đọc Android bản phát hành (release / 릴리스) notes, phân biệt:

```text
changes affecting all apps running on version X
changes only if targetSdk >= X
```

Nếu không phân biệt, nhóm (team / 팀) có thể bỏ lỡ regression trên thiết bị (device / 장치) mới dù chưa bump mục tiêu (target / 대상).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **22. tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) là di chuyển (migration / 마이그레이션) công cụ (tool / 도구)** tiếp nhận điểm tựa từ **21. hành vi (behavior / 동작) thay đổi (change / 변경) có thể apply cho mọi app hoặc target-gated** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. API guard bảo vệ class loading/runtime access** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) là di chuyển (migration / 마이그레이션) công cụ (tool / 도구)

Android có tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) cho phép một số hành vi (behavior / 동작) thay đổi (change / 변경) được toggle trong dev/kiểm thử (test / 테스트).

Điều này giúp isolate:

```text
bug do OS mới?
hay do target behavior cụ thể?
```

Dùng toggle như diagnostic/di chuyển (migration / 마이그레이션) aid, không phải môi trường vận hành (production / 운영 환경) long-term bypass.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **23. API guard bảo vệ class loading/runtime access** tiếp nhận điểm tựa từ **22. tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) là di chuyển (migration / 마이그레이션) công cụ (tool / 도구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Desugaring mang một số ngôn ngữ (language / 언어)/thư viện (library / 라이브러리) tính năng (feature / 기능) xuống API cũ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. API guard bảo vệ class loading/runtime access
Phần này nối mạch Android vừa học với “23. API guard bảo vệ class loading/runtime access”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
if (Build.VERSION.SDK_INT >= 33) {
    useNewApi()
}
```

Nhưng cần cẩn thận với static initialization/lớp (class / 클래스) xác minh (verification / 확인) ở một số mẫu (pattern / 패턴) cũ.

Tách API-specific mã (code / 코드) vào phương thức (method / 메서드)/lớp (class / 클래스) rõ có thể giúp tính tương thích (compatibility / 호환성) và readability.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **24. Desugaring mang một số ngôn ngữ (language / 언어)/thư viện (library / 라이브러리) tính năng (feature / 기능) xuống API cũ** tiếp nhận điểm tựa từ **23. API guard bảo vệ class loading/runtime access** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. SDK Extensions làm API availability không còn chỉ là API mức (level / 수준)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Desugaring mang một số ngôn ngữ (language / 언어)/thư viện (library / 라이브러리) tính năng (feature / 기능) xuống API cũ

Nhà phát triển (developer / 개발자) có thể dùng hiện đại (modern / 현대적) Java API trên minSdk thấp nếu desugaring hỗ trợ.

Nhưng không phải mọi Android khung phần mềm (framework / 프레임워크) API đều được “backport”.

Phải phân biệt:

```text
Java language/library desugaring
vs
Android framework API availability
```

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **24. Desugaring mang một số ngôn ngữ (language / 언어)/thư viện (library / 라이브러리) tính năng (feature / 기능) xuống API cũ** cho ta quy tắc; **25. SDK Extensions làm API availability không còn chỉ là API mức (level / 수준)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **26. Non-SDK giao diện (interface / 인터페이스) là tính tương thích (compatibility / 호환성) rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. SDK Extensions làm API availability không còn chỉ là API mức (level / 수준)

Một API có thể available theo extension phiên bản (version / 버전) trên cùng Android API mức (level / 수준).

Check cần dựa đặc tả hợp đồng (contract / 계약) của API, không luôn chỉ `SDK_INT`.

Mô hình tư duy (mental model / 사고 모델) tính tương thích (compatibility / 호환성) ngày càng là năng lực (capability / 역량) check hơn integer check đơn giản.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **25. SDK Extensions làm API availability không còn chỉ là API mức (level / 수준)** cho ta quy tắc; **26. Non-SDK giao diện (interface / 인터페이스) là tính tương thích (compatibility / 호환성) rủi ro (risk / 위험)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **27. OEM hành vi (behavior / 동작) là dimension ngoài API mức (level / 수준)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Non-SDK giao diện (interface / 인터페이스) là tính tương thích (compatibility / 호환성) rủi ro (risk / 위험)

Reflection/nội bộ (internal / 내부) nền tảng (platform / 플랫폼) API có thể bị restrict theo Android phiên bản (version / 버전).

Nếu thư viện (library / 라이브러리) phụ thuộc hidden API, app có thể vỡ khi OS mới dù nguồn (source / 소스) không đổi.

Môi trường vận hành (production / 운영 환경) mã (code / 코드) nên ưu tiên công khai (public / 공개) SDK đặc tả hợp đồng (contract / 계약).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **27. OEM hành vi (behavior / 동작) là dimension ngoài API mức (level / 수준)** tiếp nhận điểm tựa từ **26. Non-SDK giao diện (interface / 인터페이스) là tính tương thích (compatibility / 호환성) rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. WebView là independently updated thời gian chạy (runtime / 런타임)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. OEM hành vi (behavior / 동작) là dimension ngoài API mức (level / 수준)

Hai thiết bị (device / 장치) cùng API mức (level / 수준) có thể khác:

```text
battery manager
camera implementation
background restriction
Bluetooth stack
WebView version
```

Tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트) ma trận (matrix / 행렬) cần OEM risk-based, không chỉ emulator API ma trận (matrix / 행렬).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **28. WebView là independently updated thời gian chạy (runtime / 런타임)** tiếp nhận điểm tựa từ **27. OEM hành vi (behavior / 동작) là dimension ngoài API mức (level / 수준)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Startup phải được xem như phụ thuộc (dependency / 의존성) đường găng (critical path / 임계 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. WebView là independently updated thời gian chạy (runtime / 런타임)

WebView hành vi (behavior / 동작) có thể đổi qua cập nhật (update / 업데이트) thành phần (component / 컴포넌트) mà không đổi Android OS phiên bản (version / 버전).

Hybrid app cần log WebView phiên bản (version / 버전) khi gỡ lỗi (debug / 디버그) issue rendering/JS cầu nối (bridge / 브리지)/mạng (network / 네트워크).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **28. WebView là independently updated thời gian chạy (runtime / 런타임)** xác định đầu vào; **29. Startup phải được xem như phụ thuộc (dependency / 의존성) đường găng (critical path / 임계 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **30. TTID và TTFD trả lời hai câu khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Startup phải được xem như phụ thuộc (dependency / 의존성) đường găng (critical path / 임계 경로)

Cold start đường dẫn (path / 경로):

```text
process fork
-> Application
-> providers/initializers
-> DI graph
-> Activity creation
-> first composition/layout/draw
-> first frame
-> usable content
```

Mọi eager initializer nằm trên đường găng (critical path / 임계 경로) đều cộng độ trễ (latency / 지연 시간).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **29. Startup phải được xem như phụ thuộc (dependency / 의존성) đường găng (critical path / 임계 경로)** xác định đầu vào; **30. TTID và TTFD trả lời hai câu khác nhau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. Eager initialization phải có lý do** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. TTID và TTFD trả lời hai câu khác nhau

TTID:

```text
khi nào frame đầu xuất hiện?
```

TTFD:

```text
khi nào UI thực sự usable/full content?
```

Một app có TTID rất nhanh nhờ splash/placeholder nhưng dữ liệu (data / 데이터) usable sau 5 giây vẫn có UX tệ.

Nhánh học (track / 트랙) cả hai khi phù hợp.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **31. Eager initialization phải có lý do** tiếp nhận điểm tựa từ **30. TTID và TTFD trả lời hai câu khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. ContentProvider auto-init có thể ẩn startup công việc (work / 작업)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Eager initialization phải có lý do

Một SDK analytics không nhất thiết cần fully initialize trước first frame.

Một bảo mật (security / 보안)/session phụ thuộc (dependency / 의존성) có thể cần sớm hơn.

Classify initializer:

```text
required before first frame
required before first interaction
can defer background
demand-driven lazy
```

Đây là phụ thuộc (dependency / 의존성) scheduling bài toán (problem / 문제).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **32. ContentProvider auto-init có thể ẩn startup công việc (work / 작업)** tiếp nhận điểm tựa từ **31. Eager initialization phải có lý do** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. App Startup giúp declare initializer dependencies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. ContentProvider auto-init có thể ẩn startup công việc (work / 작업)

Một thư viện (library / 라이브러리) có thể auto-init qua manifest provider.

App nhóm (team / 팀) không thấy lời gọi (call / 호출) trong ứng dụng (application / 애플리케이션) nhưng startup vẫn chậm.

Forensic cần inspect merged manifest + startup dấu vết (trace / 추적).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **33. App Startup giúp declare initializer dependencies** tiếp nhận điểm tựa từ **32. ContentProvider auto-init có thể ẩn startup công việc (work / 작업)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. DI bộ chứa (container / 컨테이너) creation có thể nằm đường găng (critical path / 임계 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. App Startup giúp declare initializer dependencies

Initializer có thể phụ thuộc initializer khác.

Nhưng dùng khung phần mềm (framework / 프레임워크) không tự làm initialization rẻ hơn.

Cần vẫn phân loại eager/lazy và đo chi phí (cost / 비용).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **33. App Startup giúp declare initializer dependencies** xác định đầu vào; **34. DI bộ chứa (container / 컨테이너) creation có thể nằm đường găng (critical path / 임계 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **35. Startup I/O trên main luồng thực thi (thread / 스레드) là red flag** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. DI bộ chứa (container / 컨테이너) creation có thể nằm đường găng (critical path / 임계 경로)

Large phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), reflection hoặc eager singleton construction có thể làm startup chậm.

Rà soát (review / 검토) đối tượng (object / 객체) nào thực sự cần instantiate trước first screen.

Lazy provider không phải lúc nào xấu; nó có thể chuyển chi phí (cost / 비용) tới đúng tính năng (feature / 기능) usage.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **34. DI bộ chứa (container / 컨테이너) creation có thể nằm đường găng (critical path / 임계 경로)** xác định đầu vào; **35. Startup I/O trên main luồng thực thi (thread / 스레드) là red flag** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **36. Nhưng “move everything background” cũng không đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Startup I/O trên main luồng thực thi (thread / 스레드) là red flag

Examples:

```text
large SharedPreferences read
DB query
file scan
network wait
JSON parse lớn
```

Main luồng thực thi (thread / 스레드) cần tạo first frame nhanh.

StrictMode và Perfetto giúp phát hiện blocking công việc (work / 작업).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **36. Nhưng “move everything background” cũng không đủ** tiếp nhận điểm tựa từ **35. Startup I/O trên main luồng thực thi (thread / 스레드) là red flag** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Baseline Profile tối ưu mã (code / 코드) compilation đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Nhưng “move everything background” cũng không đủ

Nếu first screen bắt buộc dữ liệu (data / 데이터) A trước khi meaningful kết xuất (render / 렌더링), dữ liệu (data / 데이터) A vẫn nằm trọng yếu (critical / 중요) người dùng (user / 사용자) đường dẫn (path / 경로) dù chạy background.

Tối ưu hóa (optimization / 최적화) cần:

```text
less work
cache
precompute
progressive rendering
parallelism phù hợp
```

không chỉ đổi luồng thực thi (thread / 스레드).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **36. Nhưng “move everything background” cũng không đủ** xác định đầu vào; **37. Baseline Profile tối ưu mã (code / 코드) compilation đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **38. Macrobenchmark startup cần điều khiển (control / 제어) compilation chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Baseline Profile tối ưu mã (code / 코드) compilation đường dẫn (path / 경로)

Profile giúp thời gian chạy (runtime / 런타임) compile/precompile trọng yếu (critical / 중요) methods/classes.

Nó không loại bỏ I/O/nghiệp vụ (business / 비즈니스) công việc (work / 작업).

Benchmark tác động (effect / 효과) thay vì assume.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **37. Baseline Profile tối ưu mã (code / 코드) compilation đường dẫn (path / 경로)** xác định đầu vào; **38. Macrobenchmark startup cần điều khiển (control / 제어) compilation chế độ (mode / 모드)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **39. Release-only issue forensic checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Macrobenchmark startup cần điều khiển (control / 제어) compilation chế độ (mode / 모드)

Đo cold startup nhiều lần với profile/compilation trạng thái (state / 상태) phù hợp giúp phân biệt trình biên dịch (compiler / 컴파일러) benefit và ứng dụng (application / 애플리케이션) công việc (work / 작업).

Benchmark phải stable enough để regression meaningful.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **39. Release-only issue forensic checklist** tiếp nhận điểm tựa từ **38. Macrobenchmark startup cần điều khiển (control / 제어) compilation chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Variant-only bug checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Release-only issue forensic checklist

Khi gỡ lỗi (debug / 디버그) “gỡ lỗi (debug / 디버그) OK, bản phát hành (release / 릴리스) crash”:

```text
R8/minification?
resource shrink?
reflection?
consumer rules?
signing/config?
BuildConfig/flavor value?
manifest merge?
network security config?
proguard mapping?
```

Đừng gỡ lỗi (debug / 디버그) nghiệp vụ (business / 비즈니스) mã (code / 코드) trước khi loại trừ build-mode difference.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **40. Variant-only bug checklist** tiếp nhận điểm tựa từ **39. Release-only issue forensic checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Upgrade forensic nên thay đổi (change / 변경) one axis at a thời gian (time / 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Variant-only bug checklist
Phần này nối mạch Android vừa học với “40. Variant-only bug checklist”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```text
sourceSet override?
manifest placeholder?
resource override?
different dependency?
different endpoint?
signing certificate-dependent API?
feature flag default?
```

Always reproduce chính xác (exact / 정확한) variant.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **41. Upgrade forensic nên thay đổi (change / 변경) one axis at a thời gian (time / 시간)** tiếp nhận điểm tựa từ **40. Variant-only bug checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) diff là sản phẩm tạo ra (artifact / 산출물) rà soát (review / 검토) hữu ích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Upgrade forensic nên thay đổi (change / 변경) one axis at a thời gian (time / 시간)

Nếu cùng lúc nâng:

```text
Kotlin
AGP
Gradle
Compose
compileSdk
targetSdk
Room
```

và bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임) hỏng, tìm kiếm (search / 검색) không gian (space / 공간) rất lớn.

Upgrade theo compatible slices khi có thể, lần ghi nhận (commit / 커밋) nhỏ và CI sau mỗi slice.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **42. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) diff là sản phẩm tạo ra (artifact / 산출물) rà soát (review / 검토) hữu ích** tiếp nhận điểm tựa từ **41. Upgrade forensic nên thay đổi (change / 변경) one axis at a thời gian (time / 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. AAB khiến installed APK phụ thuộc thiết bị (device / 장치) cấu hình (configuration / 구성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) diff là sản phẩm tạo ra (artifact / 산출물) rà soát (review / 검토) hữu ích

Trước/after toolchain upgrade, compare:

```text
resolved versions
new transitive deps
removed deps
native libraries
license/security metadata
```

Một indirect cập nhật (update / 업데이트) có thể đổi hành vi thời gian chạy (runtime behavior / 런타임 동작).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **43. AAB khiến installed APK phụ thuộc thiết bị (device / 장치) cấu hình (configuration / 구성)** tiếp nhận điểm tựa từ **42. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) diff là sản phẩm tạo ra (artifact / 산출물) rà soát (review / 검토) hữu ích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. sản phẩm tạo ra (artifact / 산출물) provenance nên xuyên từ lần ghi nhận (commit / 커밋) tới installed bản dựng (build / 빌드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. AAB khiến installed APK phụ thuộc thiết bị (device / 장치) cấu hình (configuration / 구성)

Upload sản phẩm tạo ra (artifact / 산출물) không nhất thiết giống byte-for-byte gói (package / 패키지) người dùng (user / 사용자) cài.

Delivery có thể split theo:

```text
ABI
density
language
feature module
```

Bản phát hành (release / 릴리스) kiểm thử (test / 테스트) nên dùng bundletool/Play nhánh học (track / 트랙) để kiểm thử (test / 테스트) actual delivery đường dẫn (path / 경로) khi relevant.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **44. sản phẩm tạo ra (artifact / 산출물) provenance nên xuyên từ lần ghi nhận (commit / 커밋) tới installed bản dựng (build / 빌드)** tiếp nhận điểm tựa từ **43. AAB khiến installed APK phụ thuộc thiết bị (device / 장치) cấu hình (configuration / 구성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. bản phát hành (release / 릴리스) gate nên verify sản phẩm tạo ra (artifact / 산출물), không chỉ nguồn (source / 소스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. sản phẩm tạo ra (artifact / 산출물) provenance nên xuyên từ lần ghi nhận (commit / 커밋) tới installed bản dựng (build / 빌드)

Useful fields:

```text
versionName
versionCode
git SHA
CI build id
build time/toolchain hash
feature config version
```

Không expose secret; mục tiêu là forensic traceability.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **44. sản phẩm tạo ra (artifact / 산출물) provenance nên xuyên từ lần ghi nhận (commit / 커밋) tới installed bản dựng (build / 빌드)** nêu điều cần giải thích; **45. bản phát hành (release / 릴리스) gate nên verify sản phẩm tạo ra (artifact / 산출물), không chỉ nguồn (source / 소스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **46. Build/compatibility checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. bản phát hành (release / 릴리스) gate nên verify sản phẩm tạo ra (artifact / 산출물), không chỉ nguồn (source / 소스)

Gate:

```text
assemble/bundle release
run lint/tests
R8 success
mapping captured
signing verified
bundle/APK inspected
smoke install
critical journey
```

Nguồn (source / 소스) kiểm thử (test / 테스트) pass chưa chứng minh final sản phẩm tạo ra (artifact / 산출물) đúng.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **45. bản phát hành (release / 릴리스) gate nên verify sản phẩm tạo ra (artifact / 산출물), không chỉ nguồn (source / 소스)** nêu điều cần giải thích; **46. Build/compatibility checklist** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **47. Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Build/compatibility checklist
Phần này nối mạch Android vừa học với “46. Build/compatibility checklist”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Câu hỏi | bằng chứng (evidence / 증거) |
|---|---|
| Variant đồ thị (graph / 그래프) có cần thiết không? | sản phẩm (product / 제품) ma trận (matrix / 행렬) |
| nguồn (source / 소스) set override rõ không? | merged đầu ra (output / 출력) |
| phụ thuộc (dependency / 의존성) API surface tối thiểu chưa? | api vs hiện thực (implementation / 구현) |
| bản phát hành (release / 릴리스) minify đã kiểm thử (test / 테스트) chưa? | R8 mẫu (sample / 표본) run |
| ánh xạ (mapping / 매핑)/sản phẩm tạo ra (artifact / 산출물) lưu chưa? | CI sản phẩm tạo ra (artifact / 산출물) |
| mục tiêu (target / 대상) di chuyển (migration / 마이그레이션) tách hành vi (behavior / 동작) chưa? | tính tương thích (compatibility / 호환성) plan |
| API availability check đúng đặc tả hợp đồng (contract / 계약) chưa? | SDK/extension guard |
| OEM/WebView rủi ro (risk / 위험) có kiểm thử (test / 테스트) không? | thiết bị (device / 장치) ma trận (matrix / 행렬) |
| Startup đường găng (critical path / 임계 경로) đã dấu vết (trace / 추적) chưa? | Perfetto/Macrobenchmark |
| quay lui (rollback / 롤백) sản phẩm tạo ra (artifact / 산출물)/dữ liệu (data / 데이터) compatible không? | bản phát hành (release / 릴리스) drill |

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 06 — bản dựng (build / 빌드), tính tương thích (compatibility / 호환성), Startup và bản phát hành (release / 릴리스) Forensics**, **47. Kết luận** gom các mảnh từ **46. Build/compatibility checklist** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 47. Kết luận

Android bản dựng (build / 빌드) và nền tảng (platform / 플랫폼) tính tương thích (compatibility / 호환성) nên được xem như một continuous trình biên dịch (compiler / 컴파일러)/phân phối (distribution / 분포)/thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약).

Mô hình tư duy (mental model / 사고 모델):

```text
source
-> dependency graph
-> variant
-> generated/merged inputs
-> compiler/DEX/R8
-> signed artifact
-> delivery
-> platform behavior
-> startup critical path
-> production evidence
```

Khi debug theo phase và artifact thay vì chỉ đọc source code, nhiều bug “chỉ xảy ra trên release/device X” trở nên có cấu trúc để điều tra.

> **Bàn giao:** Sau **47. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
