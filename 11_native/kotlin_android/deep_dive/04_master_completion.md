# Kotlin + Android Master — kỹ thuật (engineering / 엔지니어링) & quản trị (governance / 거버넌스) Deep Dive

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Kotlin + Android Master — kỹ thuật (engineering / 엔지니어링) & quản trị (governance / 거버넌스) Deep Dive**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. Bắt đầu ở **Kotlin + Android Master — kỹ thuật (engineering / 엔지니어링) & quản trị (governance / 거버넌스) Deep Dive** để mở đối tượng chính của file và câu hỏi cần theo dõi, rồi dùng kết luận đó khi quay về lộ trình rộng hơn.

> tệp (file / 파일) này bổ sung cho [`../04_kotlin_master.md`](../04_kotlin_master.md). Mục tiêu là hoàn thiện lớp kiến thức môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링) mà một codebase Android sống nhiều năm cần có: bản dựng (build / 빌드) kỹ thuật (engineering / 엔지니어링), phụ thuộc (dependency / 의존성)/supply-chain quản trị (governance / 거버넌스), ABI, di chuyển (migration / 마이그레이션), khả năng quan sát (observability / 관측 가능성), hiệu năng (performance / 성능) ngân sách (budget / 예산), bảo mật (security / 보안)/integrity, privacy, khả năng tiếp cận (accessibility / 접근성)/adaptive UI, ADR/quyền sở hữu (ownership / 소유권), cổng chất lượng (quality gate / 품질 게이트) và Kotlin Multiplatform chiến lược (strategy / 전략).

# 1. bản dựng (build / 빌드) kỹ thuật (engineering / 엔지니어링) là một phần của kiến trúc (architecture / 아키텍처)

Ở codebase lớn, hệ thống dựng (build system / 빌드 시스템) ảnh hưởng trực tiếp nhà phát triển (developer / 개발자) productivity, CI chi phí (cost / 비용) và khả năng nâng phiên bản (version / 버전). Gradle có cấu hình (configuration / 구성) phase và thực thi (execution / 실행) phase. **cấu hình (configuration / 구성) bộ nhớ đệm (cache / 캐시)** giảm việc cấu hình lại tác vụ (task / 작업) đồ thị (graph / 그래프) khi đầu vào (input / 입력) phù hợp; **bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시)** tái sử dụng đầu ra (output / 출력) tác vụ (task / 작업) nếu đầu vào (input / 입력) fingerprint giống nhau. Custom tác vụ (task / 작업)/plugin không tương thích bộ nhớ đệm (cache / 캐시) có thể làm mất lợi ích toàn repo.

Convention plugin trong `build-logic` giúp gom cấu hình Android/Kotlin/Compose chung mà không bản sao (copy / 복사) hàng trăm dòng giữa mô-đun (module / 모듈). Tuy nhiên convention plugin cũng là mã (code / 코드) môi trường vận hành (production / 운영 환경) của toolchain: nó cần kiểm thử (test / 테스트), phiên bản (version / 버전) awareness và API nhỏ.

# 2. phiên bản (version / 버전) danh mục (catalog / 카탈로그), BOM và phụ thuộc (dependency / 의존성) ràng buộc (constraint / 제약조건)

Phiên bản (version / 버전) danh mục (catalog / 카탈로그) giúp đặt alias/phiên bản (version / 버전) phụ thuộc (dependency / 의존성) tập trung trong `libs.versions.toml`, nhưng nó không tự giải quyết tính tương thích (compatibility / 호환성). BOM/nền tảng (platform / 플랫폼) giúp một họ thư viện dùng tập phiên bản (version / 버전) đã được kiểm tra cùng nhau. phụ thuộc (dependency / 의존성) ràng buộc (constraint / 제약조건) giới hạn phiên bản (version / 버전) có thể resolve.

Tại snapshot 2026-09-20, Compose stable BOM là `2026.09.00`. BOM giúp align Compose thư viện (library / 라이브러리) versions, nhưng không có nghĩa “thêm BOM là tự có mọi Compose phụ thuộc (dependency / 의존성)”; từng sản phẩm tạo ra (artifact / 산출물) vẫn phải khai báo riêng.

# 3. bản dựng (build / 빌드) reproducibility và phụ thuộc (dependency / 의존성) locking

Bản dựng (build / 빌드) môi trường vận hành (production / 운영 환경) nên biết chính xác phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) nào đã tạo sản phẩm tạo ra (artifact / 산출물). động (dynamic / 동적) phiên bản (version / 버전) như `1.+` hay “latest.bản phát hành (release / 릴리스)” làm cùng một lần ghi nhận (commit / 커밋) có thể bản dựng (build / 빌드) ra nhị phân (binary / 이진) khác nhau ở hai thời điểm, gây khó reproduce sự cố (incident / 인시던트).

Phụ thuộc (dependency / 의존성) locking hoặc phụ thuộc (dependency / 의존성) xác minh (verification / 확인) tăng khả năng reproducibility/supply-chain điều khiển (control / 제어). Reproducible bản dựng (build / 빌드) không có nghĩa byte-for-byte luôn giống trong mọi toolchain nếu ecosystem chưa bảo đảm; mục tiêu thực tế là đầu vào (input / 입력)/phiên bản (version / 버전)/bản dựng (build / 빌드) cấu hình (configuration / 구성) được kiểm soát và kiểm tra (audit / 감사) được.

# 4. Supply-chain bảo mật (security / 보안) và phụ thuộc (dependency / 의존성) vòng đời (lifecycle / 생명주기)

Ứng dụng mobile mang theo nhiều transitive phụ thuộc (dependency / 의존성). Mỗi phụ thuộc (dependency / 의존성) là mã (code / 코드) chạy trong tiến trình (process / 프로세스), có thể thêm permission, bản địa (native / 네이티브) thư viện (library / 라이브러리), mạng (network / 네트워크) hành vi (behavior / 동작) hoặc vulnerability. quản trị (governance / 거버넌스) tốt không phải cấm thư viện (library / 라이브러리); nó yêu cầu biết đơn vị sở hữu (owner / 오너), lý do dùng, maintenance status và plan nâng phiên bản (version / 버전).

Khi chọn phụ thuộc (dependency / 의존성) mới, ngoài API convenience còn phải nhìn license, bản phát hành (release / 릴리스) cadence, bus factor, bảo mật (security / 보안) lịch sử (history / 이력), nhị phân (binary / 이진) kích thước (size / 크기), minSdk/compileSdk yêu cầu (requirement / 요구사항), KMP/Java tính tương thích (compatibility / 호환성) và di chuyển (migration / 마이그레이션) chi phí (cost / 비용) nếu thư viện (library / 라이브러리) bị bỏ.

# 5. SBOM

**SBOM (Software Bill of Materials)** là inventory machine-readable về thành phần (component / 컴포넌트)/phiên bản (version / 버전) trong sản phẩm tạo ra (artifact / 산출물). Tổ chức có compliance/bảo mật (security / 보안) yêu cầu (requirement / 요구사항) có thể dùng SBOM cùng vulnerability scanning để biết một CVE ảnh hưởng sản phẩm tạo ra (artifact / 산출물) nào.

Scanner chỉ là tín hiệu (signal / 신호). Một CVE có thể không reachable trong app của bạn hoặc chỉ ảnh hưởng môi trường (environment / 환경) khác; ngược lại một phụ thuộc (dependency / 의존성) không có CVE công khai vẫn có hành vi (behavior / 동작)/privacy rủi ro (risk / 위험). Vì vậy phụ thuộc (dependency / 의존성) bảo mật (security / 보안) cần triage, không phải auto-upgrade mù quáng.

# 6. Kotlin API công khai (public API / 공개 API) và ranh giới mô-đun (module boundary / 모듈 경계)

Ở app multi-module, `public` tạo coupling. API surface càng lớn, thay đổi càng lan rộng và incremental bản dựng (build / 빌드) càng tệ. Ưu tiên expose đặc tả hợp đồng (contract / 계약)/mô hình (model / 모델) nhỏ, giữ hiện thực (implementation / 구현) `internal` khi có thể.

Nhưng không tạo giao diện (interface / 인터페이스) chỉ để giảm công khai (public / 공개) lớp (class / 클래스) count. giao diện (interface / 인터페이스) có giá trị khi ranh giới (boundary / 경계) phản ánh quyền sở hữu (ownership / 소유권), volatility, nền tảng (platform / 플랫폼) lớp trừu tượng (abstraction / 추상화) hoặc kiểm thử (test / 테스트) seam thực sự.

Một tính năng (feature / 기능) mô-đun (module / 모듈) tốt không cần export mọi ViewModel, DTO, DAO và mapper. Phần lớn hiện thực (implementation / 구현) nên ở bên trong; mô-đun (module / 모듈) khác chỉ thấy đặc tả hợp đồng (contract / 계약) cần thiết.

# 7. nguồn (source / 소스), nhị phân (binary / 이진) và behavioral tính tương thích (compatibility / 호환성)

Một thay đổi có thể source-compatible nhưng binary-incompatible, hoặc compile được nhưng hành vi (behavior / 동작) thay đổi. công khai (public / 공개) thư viện (library / 라이브러리) phải phân biệt ba lớp này.

Đổi JVM name, generic signature, visibility, inheritance hierarchy, inline công khai (public / 공개) hàm (function / 함수), default argument hoặc generated API có thể ảnh hưởng caller theo cách khác nhau. Với thư viện (library / 라이브러리) publish cho nhiều app, API dump/nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) kiểm tra hợp lệ (validation / 검증) nên trở thành CI gate.

Behavioral tính tương thích (compatibility / 호환성) thường còn quan trọng hơn. Repository phương thức (method / 메서드) giữ nguyên signature nhưng đổi từ cache-first sang network-only có thể phá UX dù trình biên dịch (compiler / 컴파일러) không báo lỗi.

# 8. Toolchain di chuyển (migration / 마이그레이션) là một tính tương thích (compatibility / 호환성) đồ thị (graph / 그래프)

JDK ↔ Gradle ↔ AGP ↔ Kotlin ↔ KSP/trình biên dịch (compiler / 컴파일러) plugin ↔ Compose ↔ compileSdk/targetSdk tạo tính tương thích (compatibility / 호환성) đồ thị (graph / 그래프). Một di chuyển (migration / 마이그레이션) an toàn chia thành lát nhỏ và giữ bản dựng (build / 빌드) xanh sau mỗi lát.

Một workflow thực dụng là nâng wrapper/toolchain trước, giải warning/deprecation, nâng processor/thư viện (library / 라이브러리), kiểm thử (test / 테스트) hiệu năng (performance / 성능), sau đó nâng mục tiêu (target / 대상) SDK và xử lý hành vi (behavior / 동작) thay đổi (change / 변경). Nếu thay mọi thứ cùng lúc, nguyên nhân gốc (root cause / 근본 원인) phân tích (analysis / 분석) trở nên đắt.

Snapshot hiện tại của bộ ghi chú (note / 노트) là Kotlin 2.4.20, Android Studio Quail 4 / 2026.1.4 Patch 1 và AGP 9.4.1. Android 17 là API 37. Google Play từ 2026-08-31 yêu cầu app/cập nhật (update / 업데이트) Android thông thường mục tiêu (target / 대상) API 36 trở lên; đây là minimum Play yêu cầu (requirement / 요구사항) chứ không phải latest nền tảng (platform / 플랫폼) API.

# 9. mục tiêu (target / 대상) SDK di chuyển (migration / 마이그레이션) khác thư viện (library / 라이브러리) upgrade

Nâng `compileSdk` chủ yếu cho trình biên dịch (compiler / 컴파일러) biết API mới. Nâng `targetSdk` có thể bật hành vi (behavior / 동작) thay đổi (change / 변경) nền tảng (platform / 플랫폼). Vì vậy mục tiêu (target / 대상) SDK upgrade cần kiểm thử (test / 테스트) hành vi (behavior / 동작) chứ không chỉ bản dựng (build / 빌드) thành công.

Mỗi Android bản phát hành (release / 릴리스) có hai nhóm thay đổi: thay đổi áp dụng cho mọi app chạy trên OS mới và thay đổi chỉ áp dụng khi app mục tiêu (target / 대상) API mới. di chuyển (migration / 마이그레이션) plan phải đọc cả hai nhóm.

# 10. khả năng quan sát (observability / 관측 가능성): crash chỉ là một phần

Khả năng quan sát (observability / 관측 가능성) mobile phải trả lời được người dùng (user / 사용자)/session nào bị gì, ở app phiên bản (version / 버전)/thiết bị (device / 장치)/API nào, trước đó sự kiện (event / 이벤트) nào xảy ra và backend yêu cầu (request / 요청) tương ứng là gì. Crash report chỉ là một phần. ANR, startup, jank, mạng (network / 네트워크) thất bại (failure / 실패), sync backlog và tính năng (feature / 기능) success tỷ lệ (rate / 비율) cũng có thể cần telemetry.

Structured log nên có sự kiện (event / 이벤트) name và trường dữ liệu (field / 필드) ổn định thay vì concat string tùy ý. Correlation/yêu cầu (request / 요청) ID giúp nối mobile log với backend dấu vết (trace / 추적) nếu privacy chính sách (policy / 정책) cho phép.

Không ghi đơn vị từ (token / 토큰), password, raw PII hoặc document nhạy cảm chỉ để gỡ lỗi (debug / 디버그) dễ hơn.

# 11. Telemetry lược đồ (schema / 스키마) cũng là API

Analytics/khả năng quan sát (observability / 관측 가능성) sự kiện (event / 이벤트) cần đơn vị sở hữu (owner / 오너) và lược đồ (schema / 스키마) ổn định. Nếu mỗi nhà phát triển (developer / 개발자) tự đổi tên sự kiện (event / 이벤트)/thuộc tính (property / 속성), dashboard và alert nhanh chóng mất độ tin cậy.

Sampling cần thiết vì gửi mọi sự kiện (event / 이벤트) tốn pin/dữ liệu (data / 데이터) và tạo chi phí. sự kiện (event / 이벤트) high-volume như frame chỉ số (metric / 지표) có thể cần sampling mạnh; bảo mật (security / 보안)/kiểm tra (audit / 감사) sự kiện (event / 이벤트) có chính sách (policy / 정책) khác.

# 12. hiệu năng (performance / 성능) ngân sách (budget / 예산)

Hiệu năng (performance / 성능) môi trường vận hành (production / 운영 환경) nên có ngân sách (budget / 예산): cold-start percentile, frame/jank threshold, bộ nhớ (memory / 메모리) peak, nhị phân (binary / 이진) kích thước (size / 크기), battery/mạng (network / 네트워크) ngân sách (budget / 예산). Không có ngân sách (budget / 예산), “hiệu năng (performance / 성능) tốt” trở thành cảm giác.

Ngân sách (budget / 예산) phải gắn với thiết bị (device / 장치) lớp (class / 클래스) và percentile. Một app trung bình 10 ms/frame nhưng thỉnh thoảng spike 150 ms vẫn cho cảm giác giật.

# 13. Macrobenchmark, Baseline Profile và Perfetto

Macrobenchmark đo journey như startup/scroll/tương tác (interaction / 상호작용) ở app mức (level / 수준). Baseline Profile ghi lại đường đi mã (code path / 코드 경로) quan trọng để ART compile tối ưu sớm hơn. Perfetto giúp nhìn scheduling, binder, I/O, frame timeline và hệ thống (system / 시스템) sự kiện (event / 이벤트).

Hiệu năng (performance / 성능) workflow đúng là hypothesis → đo lường (measurement / 측정) → thay đổi (change / 변경) → đo lường (measurement / 측정) lại. Không bắt đầu bằng “thêm `remember`”, “đổi danh sách (list / 목록) sang chuỗi (sequence / 시퀀스)” hoặc “bật profile” nếu chưa biết bottleneck.

# 14. Regression quản trị (governance / 거버넌스)

Benchmark CI cần kiểm soát thiết bị (device / 장치)/thermal trạng thái (state / 상태) để giảm noise. So một lần chạy duy nhất không đủ. Có thể dùng threshold/baseline theo percentile hoặc rolling median tùy chuỗi xử lý (pipeline / 파이프라인).

Không phải mọi PR đều cần full macrobenchmark; affected-path hoặc nightly benchmark có thể hợp lý hơn. Nhưng bản phát hành (release / 릴리스) cần có hiệu năng (performance / 성능) tín hiệu (signal / 신호) đủ để phát hiện regression lớn.

# 15. Authentication, authorization và integrity

Authentication trả lời “ai”; authorization trả lời “được phép làm gì”; app/thiết bị (device / 장치) integrity chỉ là thêm tín hiệu (signal / 신호). Play Integrity hoặc attestation có thể giúp backend đánh giá rủi ro (risk / 위험), nhưng không nên dùng như bằng chứng tuyệt đối rằng máy khách (client / 클라이언트) không bị sửa.

Authorization phải thực thi phía máy chủ (server / 서버). Client-side role check chỉ phục vụ UX. APK nằm trên thiết bị người dùng nên phải coi là môi trường không đáng tin.

# 16. Android Keystore và BiometricPrompt

Android Keystore giúp tạo/lưu key mà app không cần đọc raw key material trực tiếp trong nhiều cấu hình. Hardware-backed key nếu thiết bị hỗ trợ tăng protection nhưng vẫn phải có threat mô hình (model / 모델) và fallback phù hợp.

`BiometricPrompt` có thể gate người dùng (user / 사용자) authentication cho thao tác (operation / 연산) nhạy cảm. Nhưng biometric UI không tự biến yêu cầu (request / 요청) backend thành authorized yêu cầu (request / 요청). máy chủ (server / 서버) vẫn cần đơn vị từ (token / 토큰)/authorization đặc tả hợp đồng (contract / 계약) riêng.

# 17. mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정)

Mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정) cho phép định nghĩa cleartext chính sách (policy / 정책), trust anchor và gỡ lỗi (debug / 디버그) override có kiểm soát. Đây là cách tốt hơn tự viết trust manager tùy tiện.

Gỡ lỗi (debug / 디버그) CA chỉ nên tồn tại trong debug-specific cấu hình (config / 설정). Không đưa “trust all certificate” vào môi trường vận hành (production / 운영 환경) để xử lý certificate issue.

# 18. WebView là trình duyệt (browser / 브라우저) nhúng

WebView cần xem như ranh giới bảo mật (security boundary / 보안 경계). JavaScript giao diện (interface / 인터페이스), truy cập tệp (file access / 파일 접근), điều hướng (navigation / 내비게이션) và origin cần được giới hạn. Không tải (load / 로드) content không tin cậy cùng bản địa (native / 네이티브) năng lực (capability / 역량) mạnh mà không rà soát (review / 검토) threat mô hình (model / 모델).

Nếu dùng `addJavascriptInterface`, chỉ expose API tối thiểu và hiểu phiên bản (version / 버전)/bảo mật (security / 보안) implication. Deep link từ web vào bản địa (native / 네이티브) cũng phải validate đầu vào (input / 입력) như bên ngoài (external / 외부) đầu vào (input / 입력).

# 19. Privacy kỹ thuật (engineering / 엔지니어링)

Privacy không phải form cuối dự án. dữ liệu (data / 데이터) inventory phải biết dữ liệu nào thu thập, mục đích, nơi lưu, thời gian giữ, có gửi third party hay không và người dùng (user / 사용자) có thể xóa/export thế nào.

Những câu trả lời này ảnh hưởng lược đồ (schema / 스키마), logging, analytics, backup và API. Thêm một SDK analytics có thể đổi privacy inventory dù tính năng (feature / 기능) nghiệp vụ (business / 비즈니스) không thay đổi.

# 20. Backup và thiết bị (device / 장치) transfer

Dữ liệu có thể được restore trên thiết bị khác nếu backup cấu hình (config / 설정) cho phép. Vì vậy giả định (assumption / 가정) “tệp (file / 파일) này chỉ tồn tại trên thiết bị gốc” có thể sai.

Đơn vị từ (token / 토큰), key, encrypted cơ sở dữ liệu (database / 데이터베이스) và credential-derived dữ liệu (data / 데이터) cần backup chính sách (policy / 정책) rõ. Nếu key không restore nhưng ciphertext có restore, app phải xử lý khôi phục (recovery / 복구) thay vì rơi vào trạng thái dữ liệu không đọc được.

# 21. Google Play dữ liệu (data / 데이터) an toàn (safety / 안전) và permission quản trị (governance / 거버넌스)

Dữ liệu (data / 데이터) an toàn (safety / 안전)/permission declaration phải phản ánh hành vi (behavior / 동작) thật của app và SDK. Một SDK có thể thu thiết bị (device / 장치) identifier/mạng (network / 네트워크) dữ liệu (data / 데이터) mà sản phẩm (product / 제품) nhóm (team / 팀) không nhận ra nếu chỉ nhìn mã (code / 코드) tính năng (feature / 기능).

Permission nên theo least privilege. Nếu hệ thống (system / 시스템) picker có thể cung cấp năng lực (capability / 역량) cần thiết, đôi khi tốt hơn xin quyền rộng như toàn bộ photo/contact lưu trữ (storage / 저장소).

# 22. khả năng tiếp cận (accessibility / 접근성) là yêu cầu (requirement / 요구사항) kiến trúc UI

Khả năng tiếp cận (accessibility / 접근성) không nên là checklist sau cùng. Compose ngữ nghĩa (semantics / 의미론), content description, role, trạng thái (state / 상태) description, focus thứ tự (order / 순서), touch mục tiêu (target / 대상) và contrast ảnh hưởng TalkBack, switch truy cập (access / 접근) và kiểm thử (test / 테스트) automation.

UI phải hoạt động khi font quy mô (scale / 규모) lớn. Nếu bố cục (layout / 레이아웃) chỉ đúng ở 1.0x font, kiến trúc (architecture / 아키텍처)/bố cục (layout / 레이아웃) ràng buộc (constraint / 제약조건) đang quá cứng.

# 23. Adaptive UI và large screen

Adaptive UI không đồng nghĩa tạo bố cục (layout / 레이아웃) riêng cho từng tablet. Thiết kế theo available không gian (space / 공간)/cửa sổ (window / 윈도우) kích thước (size / 크기) và posture giúp phone, tablet, foldable và desktop-windowed chế độ (mode / 모드) dùng cùng thông tin (information / 정보) kiến trúc (architecture / 아키텍처) nhưng phân bố pane khác nhau.

Trạng thái (state / 상태)/điều hướng (navigation / 내비게이션) mô hình (model / 모델) phải không phụ thuộc giả định “mỗi lúc chỉ có một screen full-width”. Hai-pane UI có thể cần selection trạng thái (state / 상태) tách khỏi điều hướng (navigation / 내비게이션) destination.

# 24. Android 17 và large-screen adaptivity

Android 17 tiếp tục đẩy mạnh adaptive hành vi (behavior / 동작). Với app mục tiêu (target / 대상) API 37 trên large screen, một số khả năng opt-out orientation/resizing trước đây bị hạn chế hơn. Điều cần học không phải thuộc một flag, mà là thiết kế UI không phụ thuộc orientation khóa (lock / 잠금) và kích thước cố định.

Mỗi mục tiêu (target / 대상) SDK upgrade phải rà soát (review / 검토) hành vi (behavior / 동작) thay đổi (change / 변경) vì nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약) có thể thay đổi mà mã nguồn (source code / 소스 코드) không đổi.

# 25. kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드)

Ở quy mô (scale / 규모) tổ chức, kiến trúc thất bại nhiều khi do quyết định (decision / 결정) không có ngữ cảnh (context / 맥락) chứ không do mẫu (pattern / 패턴) sai. **ADR (architecture decision record)** ghi bài toán (problem / 문제), ràng buộc (constraint / 제약조건), quyết định (decision / 결정), alternative và consequence.

Ví dụ quyết định “Room là cục bộ (local / 로컬) nguồn chuẩn (source of truth / 정본)” nên ghi lý do offline yêu cầu (requirement / 요구사항), dữ liệu (data / 데이터) volume, sync ngữ nghĩa (semantics / 의미론) và alternative đã loại. Người sau sẽ biết khi nào quyết định (decision / 결정) còn hợp lệ thay vì giữ mẫu (pattern / 패턴) như giáo điều.

# 26. quyền sở hữu (ownership / 소유권)

Mỗi cốt lõi (core / 핵심) mô-đun (module / 모듈)/nền tảng (platform / 플랫폼) năng lực (capability / 역량) cần đơn vị sở hữu (owner / 오너). dùng chung (shared / 공유) mã (code / 코드) “mọi người đều sở hữu” thường thực tế là không ai sở hữu. quyền sở hữu (ownership / 소유권) rõ làm phụ thuộc (dependency / 의존성) upgrade, sự cố (incident / 인시던트) phản hồi (response / 응답) và deprecation có nơi chịu trách nhiệm.

Quyền sở hữu (ownership / 소유권) không có nghĩa một người duy nhất được sửa. Nó nghĩa có nhóm chịu trách nhiệm về roadmap, chất lượng (quality / 품질) và tính tương thích (compatibility / 호환성).

# 27. cổng chất lượng (quality gate / 품질 게이트) từ cục bộ (local / 로컬) đến bản phát hành (release / 릴리스)

Một chuỗi xử lý (pipeline / 파이프라인) mature có tầng phản hồi (feedback / 피드백) tăng dần: formatter/trình biên dịch (compiler / 컴파일러) → đơn vị (unit / 단위) kiểm thử (test / 테스트)/static phân tích (analysis / 분석) → mô-đun (module / 모듈) tích hợp (integration / 통합) → instrumented/UI kiểm thử (test / 테스트) → benchmark/bảo mật (security / 보안) scan → bản phát hành (release / 릴리스) kiểm tra hợp lệ (validation / 검증).

Không phải mọi PR chạy toàn bộ suite đắt tiền. Có thể shard, affected-module selection hoặc nightly chuỗi xử lý (pipeline / 파이프라인). Nhưng sản phẩm tạo ra (artifact / 산출물) bản phát hành (release / 릴리스) phải đi qua gate phù hợp rủi ro (risk / 위험).

# 28. Flaky kiểm thử (test / 테스트) là defect của kiểm thử (test / 테스트) hệ thống (system / 시스템)

Flaky kiểm thử (test / 테스트) không phải “chuyện bình thường của CI”. Quarantine có thể cần tạm thời để unblock chuỗi xử lý (pipeline / 파이프라인), nhưng phải có đơn vị sở hữu (owner / 오너)/root-cause.

Nếu nhóm (team / 팀) quen bấm rerun đến xanh, CI mất vai trò tín hiệu (signal / 신호) và sự cố (incident / 인시던트) môi trường vận hành (production / 운영 환경) sẽ khó phân biệt regression thật khỏi noise.

# 29. Kotlin Multiplatform: chia sẻ đúng thứ cần chia sẻ

KMP có giá trị khi lô-gic nghiệp vụ (business logic / 비즈니스 로직), mô hình dữ liệu (data model / 데이터 모델), networking hoặc persistence lớp trừu tượng (abstraction / 추상화) thật sự chung giữa nền tảng (platform / 플랫폼). Không nên ép UI/nền tảng (platform / 플랫폼) API khác biệt vào lớp trừu tượng (abstraction / 추상화) quá chung chỉ để tăng phần trăm dùng chung (shared / 공유) mã (code / 코드).

Chỉ số (metric / 지표) tốt hơn là giảm duplicated nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) và maintenance chi phí (cost / 비용).

# 30. `expect/actual` và nền tảng (platform / 플랫폼) ranh giới (boundary / 경계)

`expect/actual` hữu ích cho nền tảng (platform / 플랫폼) năng lực (capability / 역량) nhỏ nhưng lạm dụng sẽ tạo lớp trừu tượng (abstraction / 추상화) khó hiểu. ranh giới (boundary / 경계) cần rõ về dispatcher/threading, serialization, date/thời gian (time / 시간), tệp (file / 파일)/mạng (network / 네트워크) API và lỗi (error / 오류) mô hình (model / 모델).

Dùng chung (shared / 공유) mô-đun (module / 모듈) nên có kiểm thử (test / 테스트) riêng, API công khai (public API / 공개 API) nhỏ và bản phát hành (release / 릴리스)/phiên bản (version / 버전) discipline giống mọi thư viện (library / 라이브러리) khác.

# 31. Operating mô hình (model / 모델) cho codebase sống nhiều năm

Một hệ thống bền không chỉ có kiến trúc (architecture / 아키텍처) diagram. Nó cần phụ thuộc (dependency / 의존성) cập nhật (update / 업데이트) cadence, deprecation ngân sách (budget / 예산), cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트), mục tiêu (target / 대상) SDK plan, hiệu năng (performance / 성능) baseline, crash/ANR SLO, bảo mật (security / 보안) patch tiến trình (process / 프로세스) và cleanup chính sách (policy / 정책) cho cờ tính năng (feature flag / 기능 플래그)/legacy đường dẫn (path / 경로).

Nếu dự án (project / 프로젝트) chỉ nâng phiên bản (version / 버전) khi Play Console bắt buộc, di chuyển (migration / 마이그레이션) debt sẽ tích tụ thành big-bang upgrade. Cadence nhỏ và thường xuyên rẻ hơn nhiều so với vài năm một lần.

# 32. cờ tính năng (feature flag / 기능 플래그) vòng đời (lifecycle / 생명주기)

Cờ tính năng (feature flag / 기능 플래그) hỗ trợ staged rollout/quay lui (rollback / 롤백) nhưng cũng tạo trạng thái (state / 상태) không gian (space / 공간). Mỗi flag nên có đơn vị sở hữu (owner / 오너), default, telemetry, expiration date và cleanup ticket.

Flag không được cleanup sẽ khiến đường đi mã (code path / 코드 경로) cũ/mới cùng tồn tại, kiểm thử (test / 테스트) ma trận (matrix / 행렬) tăng và nhà phát triển (developer / 개발자) sau không biết đường dẫn (path / 경로) nào còn được dùng.

# 33. bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) traceability

Mỗi sản phẩm tạo ra (artifact / 산출물) môi trường vận hành (production / 운영 환경) nên dấu vết (trace / 추적) được về lần ghi nhận (commit / 커밋), bản dựng (build / 빌드) cấu hình (config / 설정), phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), signing định danh (identity / 식별자), ánh xạ (mapping / 매핑) tệp (file / 파일) và tính năng (feature / 기능)/cấu hình (config / 설정) trạng thái (state / 상태). Khi crash xảy ra, phải biết nhị phân (binary / 이진) nào thật sự đang chạy chứ không chỉ “branch main lúc đó”.

Bản dựng (build / 빌드) number/versionCode nên monotonic theo bản phát hành (release / 릴리스) channel chính sách (policy / 정책); versionName dành cho người dùng nhưng cũng cần convention nhất quán.

# 34. quay lui (rollback / 롤백) không chỉ là phát lại APK cũ

Nếu bản phát hành (release / 릴리스) mới đã di chuyển (migration / 마이그레이션) cơ sở dữ liệu (database / 데이터베이스), thay máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) hoặc ghi dữ liệu (data / 데이터) lược đồ (schema / 스키마) mới, quay lui (rollback / 롤백) nhị phân (binary / 이진) có thể không đủ. di chuyển (migration / 마이그레이션) phải cân nhắc backward tính tương thích (compatibility / 호환성) và quay lui (rollback / 롤백) cửa sổ (window / 윈도우).

Máy chủ (server / 서버)/mobile phiên bản (version / 버전) skew là trạng thái bình thường vì người dùng (user / 사용자) không cập nhật (update / 업데이트) đồng thời. Đặc tả API (API contract / API 계약) nên chịu được nhiều app phiên bản (version / 버전) trong một khoảng thời gian xác định.

# 35. sự cố (incident / 인시던트) phản hồi (response / 응답) trên mobile

Mobile sự cố (incident / 인시던트) khó hơn web vì không thể patch mọi thiết bị (device / 장치) ngay lập tức. Cần remote cấu hình (config / 설정)/cờ tính năng (feature flag / 기능 플래그) hợp lý, backend mitigation, staged rollout và khả năng quan sát (observability / 관측 가능성) để giảm blast radius.

Khi sự cố (incident / 인시던트) xảy ra, ưu tiên giảm tác động trước rồi mới root-cause. Postmortem nên tạo hành động (action / 동작) về kiểm thử (test / 테스트), telemetry, rollout hoặc kiến trúc (architecture / 아키텍처)—not chỉ “nhà phát triển (developer / 개발자) cẩn thận hơn”.

# 36. Bản đồ mastery cuối cùng

Master Kotlin/Android không có nghĩa nhớ mọi API. Hãy giữ bốn mô hình tư duy (mental model / 사고 모델) xuyên suốt: **kiểu (type / 타입)/đặc tả hợp đồng (contract / 계약)** ở ngôn ngữ (language / 언어) mức (level / 수준); **thời gian tồn tại (lifetime / 수명)/trạng thái (state / 상태)/thất bại (failure / 실패)** ở tính đồng thời (concurrency / 동시성) và UI; **source-of-truth/ranh giới (boundary / 경계)** ở kiến trúc (architecture / 아키텍처)/dữ liệu (data / 데이터); **đo lường (measurement / 측정)/quản trị (governance / 거버넌스)** ở môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링).

Khi gặp thư viện (library / 라이브러리) mới, đặt nó vào bốn mô hình tư duy (mental model / 사고 모델) này sẽ giúp hiểu nhanh hơn học cú pháp (syntax / 문법) riêng lẻ.

# 37. Cách rà soát (review / 검토) một tính năng (feature / 기능) end-to-end

Lần theo từ người dùng (user / 사용자) hành động (action / 동작) → UI trạng thái (state / 상태)/sự kiện (event / 이벤트) → ViewModel/use trường hợp (case / 사례) → repository/nguồn (source / 소스) → mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스) → phản hồi (response / 응답)/lỗi (error / 오류) → trạng thái (state / 상태) mới → telemetry. Sau đó hỏi điều gì xảy ra khi rotate, tiến trình (process / 프로세스) kill, offline, thử lại (retry / 재시도), duplicate đầu vào (input / 입력), app cập nhật (update / 업데이트), lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) và quay lui (rollback / 롤백).

Nếu hệ thống có câu trả lời nhất quán cho chuỗi này, kiến thức đã vượt khỏi mức “biết khung phần mềm (framework / 프레임워크)” và tiến tới kỹ thuật (engineering / 엔지니어링) mastery.

> **Bàn giao:** Sau **Kotlin + Android Master — kỹ thuật (engineering / 엔지니어링) & quản trị (governance / 거버넌스) Deep Dive**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
