# Trường hợp (case / 사례) 16 — Android App Bundle, Split APK, Play Delivery và phân phối (distribution / 분포) kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 16 — Android App Bundle, Split APK, Play Delivery và phân phối (distribution / 분포) kỹ thuật (engineering / 엔지니어링)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. APK là installable sản phẩm tạo ra (artifact / 산출물), AAB là publishing sản phẩm tạo ra (artifact / 산출물)** sang **2. Tại sao split APK tồn tại**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Một Android app môi trường vận hành (production / 운영 환경) không kết thúc ở bước `assembleRelease`. sản phẩm tạo ra (artifact / 산출물) phải được đóng gói, ký, upload, phân phối theo thiết bị (device / 장치) cấu hình (configuration / 구성), có khả năng rollout dần, quay lui (rollback / 롤백) hoặc disable tính năng (feature / 기능), và vẫn hoạt động khi mã (code / 코드)/resources được chia thành nhiều split. Đây là lớp thường bị tutorial bỏ qua vì mẫu (sample / 표본) app chỉ cài trực tiếp một APK từ Android Studio.

Chapter này tập trung vào mô hình tư duy (mental model / 사고 모델) của **sản phẩm tạo ra (artifact / 산출물) và delivery**: APK khác AAB thế nào, split được tạo ra sao, động (dynamic / 동적) tính năng (feature / 기능) mô-đun (module / 모듈) dùng khi nào, Play App Signing ảnh hưởng key quyền sở hữu (ownership / 소유권) thế nào, và tại sao delivery kiến trúc (architecture / 아키텍처) phải được nghĩ cùng modularization/bản dựng (build / 빌드)/bản phát hành (release / 릴리스).

## 1. APK là installable sản phẩm tạo ra (artifact / 산출물), AAB là publishing sản phẩm tạo ra (artifact / 산출물)

**APK** chứa mã (code / 코드)/resources/bản địa (native / 네이티브) libraries đủ để Android trình quản lý gói (package manager / 패키지 관리자) cài một gói (package / 패키지) cụ thể lên thiết bị (device / 장치).

**Android App Bundle — AAB** là publishing format. Khi upload AAB lên Google Play, Play dùng thông tin trong bundle để generate APK set tối ưu theo thiết bị (device / 장치) cấu hình (configuration / 구성). Người dùng thường không tải toàn bộ mọi density/ngôn ngữ (language / 언어)/ABI nếu không cần.

Mô hình tư duy (mental model / 사고 모델):

```text
source
→ Gradle/AGP
→ app-release.aab
→ Play processing/signing
→ device-specific APK splits
→ install session trên device
```

Vì vậy kiểm thử (test / 테스트) một universal/cục bộ (local / 로컬) APK không hoàn toàn giống kiểm thử (test / 테스트) sản phẩm tạo ra (artifact / 산출물) do Play generate từ AAB. quy trình phát hành (release process / 릴리스 프로세스) nên có bước kiểm thử (test / 테스트) bundle-derived APKs bằng `bundletool` hoặc nhánh học (track / 트랙) testing phù hợp.

## 2. Tại sao split APK tồn tại

Một app có thể chứa nhiều loại tài nguyên (resource / 자원) theo cấu hình (configuration / 구성): density, ABI, ngôn ngữ (language / 언어) và tính năng (feature / 기능). Nếu ship tất cả trong một APK monolithic, thiết bị (device / 장치) nhận nhiều byte không bao giờ dùng.

Play có thể chia thành:

- **cơ sở (base / 기반) APK** chứa phần bắt buộc;
- cấu hình (configuration / 구성) splits cho ABI/density/ngôn ngữ (language / 언어);
- tính năng (feature / 기능) splits cho động (dynamic / 동적) tính năng (feature / 기능) mô-đun (module / 모듈);
- asset packs trong mô hình phù hợp.

Trình quản lý gói (package manager / 패키지 관리자) nhìn cả tập split như một app logical gói (package / 패키지). mã (code / 코드) không nên giả định “mọi tài nguyên (resource / 자원)/mã (code / 코드) đều nằm trong một vật lý (physical / 물리적) APK tệp (file / 파일)”.

## 3. `bundletool` là cách quan sát AAB thay vì coi Play như black box

`bundletool` là công cụ (tool / 도구) nền tảng dùng để thao tác App Bundle. Một workflow học và gỡ lỗi (debug / 디버그) hữu ích:

```text
AAB
→ bundletool build-apks
→ .apks archive
→ inspect split set
→ install-apks lên device/emulator
```

Điều này giúp reproduce issue như missing ABI, động (dynamic / 동적) tính năng (feature / 기능) không được đóng gói, tài nguyên (resource / 자원) split khác expectation hoặc universal APK khác device-specific install.

Bản phát hành (release / 릴리스) engineer nên biết inspect sản phẩm tạo ra (artifact / 산출물) thực tế thay vì chỉ nhìn Gradle cấu hình (configuration / 구성).

## 4. App kích thước (size / 크기) là sản phẩm (product / 제품) chỉ số (metric / 지표), không chỉ bản dựng (build / 빌드) chỉ số (metric / 지표)

AAB giúp Play tối ưu download, nhưng không miễn trừ nhà phát triển (developer / 개발자) khỏi kích thước (size / 크기) discipline. Những nguồn tăng kích thước (size / 크기) thường gặp:

- ảnh (image / 이미지)/audio/video asset lớn;
- nhiều bản địa (native / 네이티브) ABI;
- duplicate phụ thuộc (dependency / 의존성)/resources;
- mô hình (model / 모델) ML lớn;
- gỡ lỗi (debug / 디버그) siêu dữ liệu (metadata / 메타데이터) vô tình ship;
- tính năng (feature / 기능) hiếm dùng nằm trong cơ sở (base / 기반) mô-đun (module / 모듈);
- R8/tài nguyên (resource / 자원) shrinking chưa hoạt động đúng;
- embedded web/assets không kiểm soát.

APK Analyzer và bundle reports giúp phân tích contribution theo DEX/tài nguyên (resource / 자원)/bản địa (native / 네이티브) thư viện (library / 라이브러리).

Cấp cao (senior / 시니어) quy tắc (rule / 규칙): đo **download kích thước (size / 크기) và installed kích thước (size / 크기) theo cohort/thiết bị (device / 장치)**, không chỉ tệp (file / 파일) `.aab` kích thước (size / 크기). AAB upload kích thước (size / 크기) không bằng bytes người dùng (user / 사용자) tải.

## 5. động (dynamic / 동적) tính năng (feature / 기능) mô-đun (module / 모듈) giải quyết delivery, không phải mặc định modularization

Một dự án (project / 프로젝트) có thể có nhiều Gradle thư viện (library / 라이브러리) modules mà tất cả vẫn được install-time trong cơ sở (base / 기반) app. **động (dynamic / 동적) tính năng (feature / 기능) mô-đun (module / 모듈)** là mô-đun (module / 모듈) tham gia Play tính năng (feature / 기능) Delivery và có delivery ngữ nghĩa (semantics / 의미론) riêng.

```kotlin
plugins {
    id("com.android.dynamic-feature")
    kotlin("android")
}

dependencies {
    implementation(project(":app"))
}
```

Cơ sở (base / 기반) app khai báo động (dynamic / 동적) tính năng (feature / 기능) modules tương ứng. tính năng (feature / 기능) mô-đun (module / 모듈) phụ thuộc cơ sở (base / 기반); cơ sở (base / 기반) biết danh sách tính năng (feature / 기능) để bundle packaging.

Không chuyển mọi tính năng (feature / 기능) thành động (dynamic / 동적) chỉ để “modular hiện đại”. động (dynamic / 동적) delivery thêm trạng thái (state / 상태), install thất bại (failure / 실패), điều hướng (navigation / 내비게이션) điều kiện (condition / 조건), offline hành vi (behavior / 동작), testing và Play phụ thuộc (dependency / 의존성).

## 6. Install-time, on-demand và conditional delivery

**Install-time**: tính năng (feature / 기능) có ngay khi app được cài. Đây là hành vi (behavior / 동작) đơn giản nhất.

**On-demand**: tính năng (feature / 기능) được tải khi người dùng (user / 사용자) cần. Phù hợp tính năng (feature / 기능) lớn nhưng ít người dùng, ví dụ editor nâng cao hoặc region-specific workflow.

**Conditional delivery**: tính năng (feature / 기능) chỉ install nếu thiết bị (device / 장치)/người dùng (user / 사용자) thỏa điều kiện như locale, thiết bị (device / 장치) tính năng (feature / 기능) hoặc API mức (level / 수준).

Một tính năng (feature / 기능) on-demand tạo thêm máy trạng thái (state machine / 상태 머신):

```text
NotInstalled
→ Requesting
→ Downloading(progress)
→ Installed
→ Ready

hoặc

→ Failed(retryable/non-retryable)
```

UI/điều hướng (navigation / 내비게이션) phải xử lý install pending/thất bại (fail / 실패); không được `Class.forName()` hoặc navigate thẳng vào mã (code / 코드) chưa có trên thiết bị (device / 장치).

## 7. cơ sở (base / 기반) mô-đun (module / 모듈) phải giữ đặc tả hợp đồng (contract / 계약) tối thiểu ổn định

Động (dynamic / 동적) tính năng (feature / 기능) phụ thuộc cơ sở (base / 기반), nên đặc tả hợp đồng (contract / 계약) giữa cơ sở (base / 기반) và tính năng (feature / 기능) cần nhỏ và ổn định. Nếu tính năng (feature / 기능) trực tiếp chạm mọi hiện thực (implementation / 구현) nội bộ của cơ sở (base / 기반), modularization chỉ tồn tại trên filesystem.

Có thể dùng giao diện (interface / 인터페이스)/API mô-đun (module / 모듈) hoặc điều hướng (navigation / 내비게이션) đặc tả hợp đồng (contract / 계약) để giảm coupling. Tuy nhiên đừng tạo lớp trừu tượng (abstraction / 추상화) chỉ để chiều phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) đẹp; lớp trừu tượng (abstraction / 추상화) phải đại diện đặc tả hợp đồng (contract / 계약) thật sự.

## 8. tài nguyên (resource / 자원) và điều hướng (navigation / 내비게이션) khi tính năng (feature / 기능) chưa được cài

Mã (code / 코드)/tài nguyên (resource / 자원) của động (dynamic / 동적) mô-đun (module / 모듈) không đảm bảo tồn tại trước install. cơ sở (base / 기반) UI phải có fallback và loading trạng thái (state / 상태).

Deep link vào tính năng (feature / 기능) on-demand là trường hợp (case / 사례) quan trọng: app có thể được mở từ URL/notification trong trạng thái tính năng (feature / 기능) chưa cài. Router cần resolve intent → xác định tính năng (feature / 기능) → install → validate destination → navigate.

Tiến trình (process / 프로세스) có thể chết giữa download/install. Vì vậy không giữ trọng yếu (critical / 중요) trạng thái (state / 상태) chỉ trong bộ nhớ (memory / 메모리).

## 9. Play Asset Delivery và large assets

Một số app/game có asset lớn hơn nhiều so với app mã (code / 코드). Asset delivery tách concern “nhị phân (binary / 이진) tính năng (feature / 기능) mã (code / 코드)” và “large dữ liệu (data / 데이터) asset”. Delivery chế độ (mode / 모드) có thể khác nhau tùy use trường hợp (case / 사례).

Không nên dùng động (dynamic / 동적) tính năng (feature / 기능) chỉ để chở tệp (file / 파일) dữ liệu lớn nếu nền tảng (platform / 플랫폼) có delivery thành phần nguyên thủy (primitive / 기본 요소) phù hợp hơn. Ngược lại, backend download riêng cũng có sự đánh đổi (trade-off / 트레이드오프) auth/CDN/bộ nhớ đệm (cache / 캐시)/versioning mà Play-managed delivery có thể giải quyết một phần.

Chọn cơ chế dựa vào quyền sở hữu (ownership / 소유권), kích thước (size / 크기), cập nhật (update / 업데이트) cadence, offline yêu cầu (requirement / 요구사항) và store phụ thuộc (dependency / 의존성).

## 10. ABI splits và bản địa (native / 네이티브) thư viện (library / 라이브러리) consequence

Nếu app có `.so`, AAB có thể cho Play ship ABI phù hợp thiết bị (device / 장치). Điều này giảm download nhưng đòi hỏi bản địa (native / 네이티브) phụ thuộc (dependency / 의존성) phải có ABI ma trận (matrix / 행렬) đúng.

Ví dụ dự án (project / 프로젝트) có `arm64-v8a` và `x86_64` nhưng một third-party `.so` chỉ có ARM. Emulator x86_64 có thể thất bại (fail / 실패) tải (load / 로드) thư viện (library / 라이브러리) dù phone thật chạy tốt.

Bản địa (native / 네이티브) sản phẩm tạo ra (artifact / 산출물) kiểm tra hợp lệ (validation / 검증) phải kiểm tra ABI availability, symbol, page-size alignment và packaging cho đúng bản phát hành (release / 릴리스) bundle.

## 11. ngôn ngữ (language / 언어) split và thời gian chạy (runtime / 런타임) locale

Play có thể tối ưu ngôn ngữ (language / 언어) resources. Nếu app có động (dynamic / 동적) ngôn ngữ (language / 언어) hành vi (behavior / 동작), per-app ngôn ngữ (language / 언어) hoặc tải locale sau install, cần hiểu tài nguyên (resource / 자원) availability/delivery mô hình (model / 모델).

Không nên giả định tất cả translations luôn được cài nếu bundle cấu hình (configuration / 구성) tách ngôn ngữ (language / 언어) splits. Nếu sản phẩm (product / 제품) cần mọi locale offline ngay từ đầu, cấu hình (configuration / 구성) delivery phải phản ánh yêu cầu (requirement / 요구사항) đó.

## 12. Play App Signing: app signing key và upload key

Trong Play App Signing, Google Play quản lý **app signing key** dùng để ký APK tới người dùng (user / 사용자). nhà phát triển (developer / 개발자) thường dùng **upload key** để authenticate sản phẩm tạo ra (artifact / 산출물) upload.

Hai key có vai trò khác nhau. Mất upload key có khôi phục (recovery / 복구) đường dẫn (path / 경로) khác với mất điều khiển (control / 제어) app signing định danh (identity / 식별자) trong mô hình tự quản lý.

Nhóm (team / 팀) phải document:

- ai sở hữu upload credential;
- CI ký/upload thế nào;
- rotation/khôi phục (recovery / 복구) procedure;
- gói (package / 패키지) định danh (identity / 식별자) nào dùng key nào;
- gỡ lỗi (debug / 디버그)/nội bộ (internal / 내부) phân phối (distribution / 분포) không được nhầm môi trường vận hành (production / 운영 환경) key.

## 13. Signing lineage và cập nhật (update / 업데이트) tính tương thích (compatibility / 호환성)

Android cập nhật (update / 업데이트) một gói (package / 패키지) dựa gói (package / 패키지) định danh (identity / 식별자)/signing relationship và phiên bản (version / 버전) rules. bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) ký sai có thể không upgrade được app đang cài.

Kiểm thử (test / 테스트) bản phát hành (release / 릴리스) không chỉ `fresh install`; phải kiểm thử (test / 테스트) **upgrade từ phiên bản (version / 버전) môi trường vận hành (production / 운영 환경) đang phổ biến**. Đặc biệt khi thay signing setup, split mô hình (model / 모델), bản địa (native / 네이티브) thư viện (library / 라이브러리) hoặc cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마).

## 14. `versionCode` và `versionName`

`versionName` là user-facing ngữ nghĩa (semantic / 의미적) label, ví dụ `3.4.0`. `versionCode` là monotonically increasing integer Android/Play dùng để so phiên bản (version / 버전) sản phẩm tạo ra (artifact / 산출물).

Không derive trọng yếu (critical / 중요) di chuyển (migration / 마이그레이션) lô-gic (logic / 논리) từ `versionName` string nếu hệ thống (system / 시스템) đã có lược đồ (schema / 스키마)/API-specific phiên bản (version / 버전) riêng. App phiên bản (version / 버전), DB lược đồ (schema / 스키마) phiên bản (version / 버전) và backend API phiên bản (version / 버전) là những axes khác nhau.

CI nên tạo phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터) reproducibly và dấu vết (trace / 추적) về lần ghi nhận (commit / 커밋)/bản phát hành (release / 릴리스) tag.

## 15. nội bộ (internal / 내부), closed, open và môi trường vận hành (production / 운영 환경) tracks là triển khai (deployment / 배포) environments

Store nhánh học (track / 트랙) không chỉ để “QA tải app”. Nó là triển khai (deployment / 배포) điều khiển (control / 제어) plane. Tùy organization, có thể dùng:

```text
internal
→ closed/beta
→ staged production rollout
→ wider rollout
```

Mỗi bước cần clear promotion criteria. sản phẩm tạo ra (artifact / 산출물) được promote nên là cùng sản phẩm tạo ra (artifact / 산출물) đã kiểm thử (test / 테스트), tránh rebuild nhị phân (binary / 이진) khác ở mỗi môi trường (environment / 환경) nếu không cần.

Nếu môi trường (environment / 환경) backend khác nhau, cân nhắc bản dựng (build / 빌드) variant/cấu hình (configuration / 구성) chiến lược (strategy / 전략) cẩn thận. “Promote same sản phẩm tạo ra (artifact / 산출물)” và “different endpoint per môi trường (environment / 환경)” đôi khi xung đột; giải pháp phải phù hợp threat mô hình (model / 모델) và quy trình phát hành (release process / 릴리스 프로세스).

## 16. Staged rollout không thay cờ tính năng (feature flag / 기능 플래그)

Staged rollout kiểm soát tỷ lệ người dùng (user / 사용자) nhận **app nhị phân (binary / 이진) phiên bản (version / 버전)**. cờ tính năng (feature flag / 기능 플래그) kiểm soát hành vi (behavior / 동작) **bên trong nhị phân (binary / 이진)** theo thời gian chạy (runtime / 런타임) chính sách (policy / 정책).

Nếu crash do nhị phân (binary / 이진) initialization trước khi remote cấu hình (config / 설정) tải (load / 로드), cờ tính năng (feature flag / 기능 플래그) có thể không cứu được. Nếu bug chỉ nằm tính năng (feature / 기능) mới, flag có thể disable nhanh hơn store quay lui (rollback / 롤백).

Một bản phát hành (release / 릴리스) resilient thường dùng cả hai ở các tầng (layer / 계층) khác nhau.

## 17. quay lui (rollback / 롤백) trên mobile khó hơn máy chủ (server / 서버) quay lui (rollback / 롤백)

Không thể giả định người dùng (user / 사용자) sẽ downgrade APK ngay. Nhiều người dùng (user / 사용자) giữ phiên bản (version / 버전) lỗi offline trong nhiều ngày. Vì vậy “quay lui (rollback / 롤백)” mobile thường là:

- stop rollout;
- ship hotfix với versionCode cao hơn;
- disable remote tính năng (feature / 기능);
- backend giữ backward tính tương thích (compatibility / 호환성);
- DB/tệp (file / 파일) format phải chịu được phiên bản (version / 버전) skew.

Di chuyển (migration / 마이그레이션) destructive hoặc backend đặc tả hợp đồng (contract / 계약) one-way khiến quay lui (rollback / 롤백) gần như không thể.

## 18. In-app cập nhật (update / 업데이트) không phải default solution cho mọi app

In-app cập nhật (update / 업데이트) APIs có thể giúp prompt/cập nhật (update / 업데이트) luồng (flow / 흐름) trong use trường hợp (case / 사례) phù hợp, nhưng sản phẩm (product / 제품) không nên cưỡng ép cập nhật (update / 업데이트) chỉ vì nhà phát triển (developer / 개발자) muốn giảm hỗ trợ (support / 지원) ma trận (matrix / 행렬).

Máy chủ (server / 서버) giao thức (protocol / 프로토콜) nên có tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우). Nếu bắt buộc minimum phiên bản (version / 버전) vì bảo mật (security / 보안)/dữ liệu (data / 데이터) integrity, UI phải giải thích rõ và backend chính sách (policy / 정책) phải có operational plan.

Cập nhật (update / 업데이트) luồng (flow / 흐름) bản thân cũng là failure-prone trạng thái (state / 상태): Play availability, download, restart, người dùng (user / 사용자) cancel, mạng (network / 네트워크) thất bại (fail / 실패).

## 19. rà soát (review / 검토), integrity và Play-specific services là optional hạ tầng (infrastructure / 인프라)

In-app rà soát (review / 검토), Play Integrity, cập nhật (update / 업데이트) API và delivery libraries cung cấp năng lực (capability / 역량) hữu ích nhưng tăng coupling với Google Play môi trường (environment / 환경). cốt lõi (core / 핵심) nghiệp vụ (business / 비즈니스) kiến trúc (architecture / 아키텍처) không nên giả định mọi installation channel đều có Play services nếu sản phẩm (product / 제품) có sideload/enterprise/other-store yêu cầu (requirement / 요구사항).

Bọc Play-specific tích hợp (integration / 통합) sau ranh giới (boundary / 경계) rõ ràng nếu app phải hỗ trợ nhiều phân phối (distribution / 분포) channel.

## 20. phân phối (distribution / 분포) channel là ranh giới bảo mật (security boundary / 보안 경계)

Bản phát hành (release / 릴리스) nhị phân (binary / 이진) có thể đi qua Play, enterprise MDM, direct APK hoặc nội bộ (internal / 내부) phân phối (distribution / 분포). Mỗi channel khác signing/cập nhật (update / 업데이트)/trust mô hình (model / 모델).

Bảo mật (security / 보안) lô-gic (logic / 논리) không được chỉ hỏi “app được cài từ Play nên trusted”. máy khách (client / 클라이언트) vẫn nằm trên user-controlled thiết bị (device / 장치). Integrity tín hiệu (signal / 신호) là một đầu vào (input / 입력) rủi ro (risk / 위험) tín hiệu (signal / 신호), không thay backend authorization.

## 21. Offline và động (dynamic / 동적) delivery

On-demand tính năng (feature / 기능) yêu cầu mạng (network / 네트워크) để tải lần đầu, vì vậy tính năng (feature / 기능) business-critical offline không nên phụ thuộc động (dynamic / 동적) install chưa có.

Nếu người dùng (user / 사용자) chuẩn bị đi offline, sản phẩm (product / 제품) có thể prefetch tính năng (feature / 기능)/asset khi online. Nhưng phải xử lý lưu trữ (storage / 저장소) pressure và mô-đun (module / 모듈) uninstall hành vi (behavior / 동작).

Kiến trúc (architecture / 아키텍처) nên phân biệt:

- tính năng (feature / 기능) năng lực (capability / 역량) tồn tại trong sản phẩm (product / 제품);
- nhị phân (binary / 이진) mô-đun (module / 모듈) đã installed trên thiết bị (device / 장치);
- người dùng (user / 사용자) có entitlement;
- backend tính năng (feature / 기능) enabled;
- permission/hardware available.

Năm trạng thái này không đồng nghĩa.

## 22. kiểm thử (test / 테스트) AAB/delivery đúng cách

Bản phát hành (release / 릴리스) kiểm thử (test / 테스트) ma trận (matrix / 행렬) nên có ít nhất:

1. bản dựng (build / 빌드) AAB production-like;
2. generate/install APK set theo representative thiết bị (device / 장치) specs;
3. fresh install;
4. upgrade từ prior môi trường vận hành (production / 운영 환경) sản phẩm tạo ra (artifact / 산출물);
5. ngôn ngữ (language / 언어)/density/ABI representative;
6. động (dynamic / 동적) tính năng (feature / 기능) install/uninstall/thất bại (failure / 실패) nếu dùng;
7. offline launch sau install;
8. tiến trình (process / 프로세스) death trong delivery luồng (flow / 흐름);
9. minified/R8 bản phát hành (release / 릴리스) hành vi (behavior / 동작);
10. verify signing/gói (package / 패키지)/phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터).

Cài `debug.apk` từ IDE không cover phần lớn rủi ro (risk / 위험) này.

## 23. App Bundle và bản địa (native / 네이티브) 16 KB page kích thước (size / 크기)

Khi app chứa bản địa (native / 네이티브) `.so`, phân phối (distribution / 분포) tính đúng đắn (correctness / 정확성) còn phụ thuộc nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) với page-size requirements trên Android mới. NDK mới hỗ trợ alignment phù hợp tốt hơn, nhưng **mọi prebuilt bản địa (native / 네이티브) thư viện (library / 라이브러리)** cũng phải compatible.

Đây là ví dụ điển hình cho việc AAB “bản dựng (build / 빌드) thành công” chưa đủ; sản phẩm tạo ra (artifact / 산출물) cần được validate trên thiết bị (device / 장치)/nền tảng (platform / 플랫폼) mục tiêu (target / 대상) thực tế.

Trường hợp (case / 사례) 17 sẽ đi sâu JNI/ABI/bản địa (native / 네이티브) bộ nhớ (memory / 메모리) và 16 KB page-size kỹ thuật (engineering / 엔지니어링).

## 24. động (dynamic / 동적) tính năng (feature / 기능) thất bại (failure / 실패) modes

Các lỗi thường gặp:

### Tính năng (feature / 기능) mã (code / 코드) được tham chiếu (reference / 참조) trực tiếp trước install

Cơ sở (base / 기반) mã (code / 코드) có compile-time/thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) không đúng ranh giới (boundary / 경계). Cần tuyến (route / 경로) qua install trạng thái (state / 상태)/đặc tả hợp đồng (contract / 계약).

### Deep link vào mô-đun (module / 모듈) chưa có

Router phải defer điều hướng (navigation / 내비게이션) và preserve intent sau install.

### R8 removes reflection entry điểm (point / 지점)

Động (dynamic / 동적) delivery + reflection cần keep quy tắc (rule / 규칙)/kiểm thử (test / 테스트) bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물).

### Người dùng (user / 사용자) offline lần đầu mở tính năng (feature / 기능)

UI cần graceful trạng thái (state / 상태), không spinner vô hạn.

### Mô-đun (module / 모듈) phiên bản (version / 버전) mismatch

Tính năng (feature / 기능)/cơ sở (base / 기반) trong một installed app bundle phải cùng bản phát hành (release / 릴리스) set; đừng tự thiết kế hot-swap mã (code / 코드) ngoài supported nền tảng (platform / 플랫폼) mô hình (model / 모델).

## 25. cấp cao (senior / 시니어) quyết định (decision / 결정) khung phần mềm (framework / 프레임워크): có nên dùng động (dynamic / 동적) delivery?

Hỏi lần lượt:

- tính năng (feature / 기능) kích thước (size / 크기) có đáng kể không;
- tỷ lệ người dùng (user / 사용자) dùng tính năng (feature / 기능) thấp hay cao;
- tính năng (feature / 기능) có cần offline ngay không;
- install độ trễ (latency / 지연 시간) có chấp nhận được không;
- deep link/cold start có cần tính năng (feature / 기능) này không;
- nhóm (team / 팀) có khả năng kiểm thử (test / 테스트) delivery states không;
- phân phối (distribution / 분포) channel có phải Google Play không;
- ranh giới mô-đun (module boundary / 모듈 경계) có thật sự rõ không.

Nếu hầu hết người dùng (user / 사용자) cần tính năng (feature / 기능) và kích thước (size / 크기) nhỏ, install-time đơn giản thường tốt hơn.

## 26. sản phẩm tạo ra (artifact / 산출물) provenance và bản phát hành (release / 릴리스) bằng chứng (evidence / 증거)

Mỗi môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스) nên có thể truy ngược:

```text
release version
→ AAB checksum
→ source commit/tag
→ dependency lock/SBOM
→ toolchain
→ signing/upload identity
→ mapping/native symbols
→ CI run
→ rollout timeline
```

Crash symbolication và R8 deobfuscation cần ánh xạ (mapping / 매핑) tệp (file / 파일) đúng phiên bản (version / 버전). bản địa (native / 네이티브) crash cần symbols tương ứng nhị phân (binary / 이진). Nếu sản phẩm tạo ra (artifact / 산출물) siêu dữ liệu (metadata / 메타데이터) bị mất, sự cố (incident / 인시던트) phản hồi (response / 응답) khó hơn nhiều.

## 27. Official references

- Android App Bundle: https://nhà phát triển (developer / 개발자).android.com/guide/app-bundle
- Play tính năng (feature / 기능) Delivery: https://nhà phát triển (developer / 개발자).android.com/guide/playcore/feature-delivery
- Reduce app kích thước (size / 크기): https://nhà phát triển (developer / 개발자).android.com/topic/hiệu năng (performance / 성능)/reduce-apk-size
- `bundletool`: https://nhà phát triển (developer / 개발자).android.com/tools/bundletool
- mục tiêu (target / 대상) API requirements: https://nhà phát triển (developer / 개발자).android.com/google/play/requirements/target-sdk

Store chính sách (policy / 정책) và delivery API thay đổi theo thời gian. Khi bản phát hành (release / 릴리스) thật, luôn kiểm tra documentation/chính sách (policy / 정책) mới nhất thay vì dùng snapshot trong ghi chú (note / 노트) như nguồn (source / 소스) duy nhất.

> **Bàn giao:** Sau **27. Official references**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture end to end](./01_architecture_end_to_end.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
