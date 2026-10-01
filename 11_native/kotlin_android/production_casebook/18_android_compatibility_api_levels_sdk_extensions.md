# Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. API mức (level / 수준) là versioned nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Bốn phiên bản (version / 버전) axis thường bị trộn lẫn** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Android tính tương thích (compatibility / 호환성) không đơn giản là “mã (code / 코드) chạy trên API 26 tới API 37”. Một app phải đồng thời xử lý nhiều trục: OS phiên bản (version / 버전) của thiết bị (device / 장치), `minSdk`, `compileSdk`, `targetSdk`, Jetpack/thư viện (library / 라이브러리) phiên bản (version / 버전), hardware năng lực (capability / 역량), OEM hành vi (behavior / 동작) và các nền tảng (platform / 플랫폼) hành vi (behavior / 동작) changes có thể áp dụng cho tất cả app hoặc chỉ app mục tiêu (target / 대상) phiên bản (version / 버전) mới.

Chapter này xây quy trình nâng Android nền tảng (platform / 플랫폼) có chủ đích: hiểu loại thay đổi nào đang tác động, kiểm thử (test / 테스트) bằng tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크), guard API đúng, tránh non-SDK phụ thuộc (dependency / 의존성) và thiết kế bản phát hành (release / 릴리스) sao cho người dùng (user / 사용자) cập nhật (update / 업데이트) OS trước hay app trước đều không làm hệ thống vỡ.

## 1. API mức (level / 수준) là versioned nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약)

Mỗi Android nền tảng (platform / 플랫폼) bản phát hành (release / 릴리스) có API mức (level / 수준). API mức (level / 수준) giúp compile-time/thời gian chạy (runtime / 런타임) mã (code / 코드) biết API nào tồn tại.

Nhưng chỉ biết `Build.VERSION.SDK_INT` không đủ. hành vi (behavior / 동작) của cùng một API có thể thay đổi theo OS phiên bản (version / 버전) và mục tiêu (target / 대상) SDK. Một permission, background quy tắc (rule / 규칙) hoặc UI hành vi (behavior / 동작) có thể tồn tại lâu nhưng ngữ nghĩa (semantics / 의미론) thay đổi qua nhiều bản phát hành (release / 릴리스).

Tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링) vì thế là quản lý **hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약)**, không chỉ phương thức (method / 메서드) availability.

> **Chuyển mạch:** API level là platform contract; tiếp theo phải tách compile/min/target SDK và SDK Extensions, rồi mới phân loại behavior change khi migration.

## 2. Bốn phiên bản (version / 버전) axis thường bị trộn lẫn

### `minSdk`

OS thấp nhất được hỗ trợ (support / 지원) để cài app.

### `compileSdk`

API surface dùng để compile nguồn (source / 소스).

### `targetSdk`

Phiên bản (version / 버전) hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약) app tuyên bố đã tương thích.

### Thiết bị (device / 장치) OS/API mức (level / 수준)

Nền tảng (platform / 플랫폼) thực tế app đang chạy.

Ví dụ app có thể compile SDK 37, mục tiêu (target / 대상) 36, min 26 và chạy trên thiết bị (device / 장치) API 37. Mỗi con số trả lời câu hỏi khác nhau.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **3. Hai nhóm nền tảng (platform / 플랫폼) hành vi (behavior / 동작) changes** tiếp nhận điểm tựa từ **2. Bốn phiên bản (version / 버전) axis thường bị trộn lẫn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. tính tương thích (compatibility / 호환성) calendar nên bắt đầu từ preview/beta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Hai nhóm nền tảng (platform / 플랫폼) hành vi (behavior / 동작) changes

Android tính tương thích (compatibility / 호환성) guidance phân biệt quan trọng:

**Changes affecting all apps**: hành vi (behavior / 동작) thay đổi khi app chạy trên OS mới dù targetSdk chưa tăng.

**Targeted changes**: chỉ bật khi app mục tiêu (target / 대상) API mức (level / 수준) tương ứng hoặc cao hơn.

Điều này dẫn tới hai workstream khác nhau:

```text
OS compatibility testing
= chạy current production app trên OS mới

Target SDK migration
= build app target mới và test targeted changes
```

Chỉ làm workstream thứ hai là quá muộn vì người dùng (user / 사용자) có thể upgrade OS trước khi nhóm (team / 팀) tăng mục tiêu (target / 대상).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **4. tính tương thích (compatibility / 호환성) calendar nên bắt đầu từ preview/beta** tiếp nhận điểm tựa từ **3. Hai nhóm nền tảng (platform / 플랫폼) hành vi (behavior / 동작) changes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) giúp kiểm thử (test / 테스트) thay đổi (change / 변경) riêng lẻ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. tính tương thích (compatibility / 호환성) calendar nên bắt đầu từ preview/beta

Nhóm (team / 팀) môi trường vận hành (production / 운영 환경) không nên đợi Play deadline mới tăng mục tiêu (target / 대상). Một cadence tốt:

1. OS preview/beta xuất hiện → chạy smoke/trọng yếu (critical / 중요) flows với hiện tại (current / 현재) app.
2. Inventory hành vi (behavior / 동작) changes for all apps.
3. Inventory targeted hành vi (behavior / 동작) changes.
4. Upgrade compileSdk/libraries nếu cần.
5. Fix all-app regressions trước.
6. Tạo branch/flag targetSdk di chuyển (migration / 마이그레이션).
7. Enable targeted changes dần bằng compat khung phần mềm (framework / 프레임워크).
8. kiểm thử (test / 테스트) thiết bị (device / 장치)/OEM ma trận (matrix / 행렬).
9. Rollout mục tiêu (target / 대상) upgrade trước chính sách (policy / 정책) deadline đủ xa.

Mục tiêu là tách nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션) khỏi nghiệp vụ (business / 비즈니스) bản phát hành (release / 릴리스) pressure.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **5. tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) giúp kiểm thử (test / 테스트) thay đổi (change / 변경) riêng lẻ** tiếp nhận điểm tựa từ **4. tính tương thích (compatibility / 호환성) calendar nên bắt đầu từ preview/beta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. API availability guard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) giúp kiểm thử (test / 테스트) thay đổi (change / 변경) riêng lẻ

Android cung cấp tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) cho nhiều hành vi (behavior / 동작) changes. nhà phát triển (developer / 개발자) có thể bật/tắt một thay đổi (change / 변경) bằng nhà phát triển (developer / 개발자) Options hoặc ADB trên supported versions mà không luôn phải đổi mục tiêu (target / 대상)/recompile ngay.

Điều này rất hữu ích để isolate regression:

```text
current app
+ new OS
+ enable one compat change
→ test critical flow
```

Thay vì tăng mục tiêu (target / 대상) rồi gặp 15 hành vi (behavior / 동작) changes cùng lúc.

ADB command cụ thể thay đổi theo nền tảng (platform / 플랫폼)/thay đổi (change / 변경) ID; luôn lấy ID và command từ Android behavior-changes documentation của phiên bản (version / 버전) đang kiểm thử (test / 테스트).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **5. tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크) giúp kiểm thử (test / 테스트) thay đổi (change / 변경) riêng lẻ** cho ta quy tắc; **6. API availability guard** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. @RequiresApi và lint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. API availability guard

Nếu API chỉ có từ phiên bản (version / 버전) mới hơn minSdk:

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    // call API introduced/required on this level
} else {
    // legacy path
}
```

Đừng chỉ guard để trình biên dịch (compiler / 컴파일러) hết warning; legacy đường dẫn (path / 경로) phải có hành vi (behavior / 동작) nghiệp vụ (business / 비즈니스) hợp lệ.

Nếu tính năng (feature / 기능) không thể hỗ trợ (support / 지원) OS cũ, có thể degrade gracefully thay vì giả lập hành vi (behavior / 동작) nguy hiểm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **6. API availability guard** cho ta quy tắc; **7. @RequiresApi và lint** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **8. API-specific hiện thực (implementation / 구현) bằng lớp (class / 클래스) isolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. `@RequiresApi` và lint

`@RequiresApi` document đặc tả hợp đồng (contract / 계약) rằng caller phải chạy trên API tối thiểu. Android Lint giúp phát hiện lời gọi (call / 호출) site không guard.

```kotlin
@RequiresApi(Build.VERSION_CODES.TIRAMISU)
fun useNewApi() { ... }
```

Annotation không tự runtime-check. Nó là static đặc tả hợp đồng (contract / 계약). Caller vẫn chịu trách nhiệm guard.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **8. API-specific hiện thực (implementation / 구현) bằng lớp (class / 클래스) isolation** tiếp nhận điểm tựa từ **7. @RequiresApi và lint** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Jetpack compat lớp trừu tượng (abstraction / 추상화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. API-specific hiện thực (implementation / 구현) bằng lớp (class / 클래스) isolation

Đôi khi verifier/nạp lớp (class loading / 클래스 로딩) hoặc mã (code / 코드) readability tốt hơn nếu tách hiện thực (implementation / 구현) theo phiên bản (version / 버전):

```kotlin
object NotificationPermissionCompat {
    fun isGranted(context: Context): Boolean {
        return if (Build.VERSION.SDK_INT >= 33) {
            Api33Impl.isGranted(context)
        } else {
            true
        }
    }

    @RequiresApi(33)
    private object Api33Impl {
        fun isGranted(context: Context): Boolean =
            ContextCompat.checkSelfPermission(
                context,
                Manifest.permission.POST_NOTIFICATIONS
            ) == PackageManager.PERMISSION_GRANTED
    }
}
```

Mẫu (pattern / 패턴) này giữ new API tham chiếu (reference / 참조) trong hiện thực (implementation / 구현) isolated và làm tính tương thích (compatibility / 호환성) intent rõ.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **9. Jetpack compat lớp trừu tượng (abstraction / 추상화)** tiếp nhận điểm tựa từ **8. API-specific hiện thực (implementation / 구현) bằng lớp (class / 클래스) isolation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Desugaring là compile/toolchain tính tương thích (compatibility / 호환성), không phải OS magic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Jetpack compat lớp trừu tượng (abstraction / 추상화)

Không phải mọi API-level difference cần tự viết `if SDK_INT`. Jetpack cốt lõi (core / 핵심)/Activity/cửa sổ (window / 윈도우)/Media/Camera... cung cấp tính tương thích (compatibility / 호환성) lớp trừu tượng (abstraction / 추상화) đã encode nhiều nền tảng (platform / 플랫폼) differences.

Ưu tiên stable Jetpack API khi nó thực sự giải quyết tính tương thích (compatibility / 호환성) concern. Tự bản dựng (build / 빌드) wrapper nền tảng (platform / 플랫폼) có maintenance chi phí (cost / 비용) dài hạn.

Tuy nhiên wrapper không loại bỏ need hiểu underlying hành vi (behavior / 동작) khi debugging OEM/nền tảng (platform / 플랫폼) trường hợp biên (edge case / 경계 사례).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **10. Desugaring là compile/toolchain tính tương thích (compatibility / 호환성), không phải OS magic** tiếp nhận điểm tựa từ **9. Jetpack compat lớp trừu tượng (abstraction / 추상화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. compileSdk upgrade thường ít risky hơn targetSdk upgrade nhưng không risk-free** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Desugaring là compile/toolchain tính tương thích (compatibility / 호환성), không phải OS magic

Java ngôn ngữ (language / 언어)/API desugaring cho phép một số ngôn ngữ (language / 언어)/API constructs hoạt động trên OS cũ thông qua bytecode transformation/thư viện (library / 라이브러리) hỗ trợ (support / 지원).

Cốt lõi (core / 핵심) thư viện (library / 라이브러리) desugaring có thể backport một số Java APIs, nhưng không backport Android khung phần mềm (framework / 프레임워크) API tùy ý.

Không nhìn thấy compile lỗi (error / 오류) không có nghĩa phương thức (method / 메서드) khung phần mềm (framework / 프레임워크) mới sẽ chạy trên minSdk cũ.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **11. compileSdk upgrade thường ít risky hơn targetSdk upgrade nhưng không risk-free** tiếp nhận điểm tựa từ **10. Desugaring là compile/toolchain tính tương thích (compatibility / 호환성), không phải OS magic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. nền tảng (platform / 플랫폼) hành vi (behavior / 동작) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. `compileSdk` upgrade thường ít risky hơn `targetSdk` upgrade nhưng không risk-free

Tăng compileSdk chủ yếu mở API surface mới, nhưng đi kèm AGP/thư viện (library / 라이브러리)/toolchain các ràng buộc (constraints / 제약조건들) và có thể expose new lint/tài nguyên (resource / 자원) hành vi (behavior / 동작).

Tăng targetSdk bật hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약) mới và cần full di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트).

Nhóm (team / 팀) nên tách hai thay đổi (change / 변경) nếu dự án (project / 프로젝트) rủi ro (risk / 위험) cao, để nguyên nhân gốc (root cause / 근본 원인) rõ hơn.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **12. nền tảng (platform / 플랫폼) hành vi (behavior / 동작) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **11. compileSdk upgrade thường ít risky hơn targetSdk upgrade nhưng không risk-free** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Permission changes là tính tương thích (compatibility / 호환성) di chuyển (migration / 마이그레이션) điển hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. nền tảng (platform / 플랫폼) hành vi (behavior / 동작) ma trận (matrix / 행렬)

Cho mỗi Android upgrade, tạo bảng:

| thay đổi (change / 변경) | Affects all apps? | Target-gated? | tính năng (feature / 기능) impacted | kiểm thử (test / 테스트) đơn vị sở hữu (owner / 오너) | Mitigation |
|---|---|---|---|---|---|
| background restriction | maybe | yes/no | sync/media | nền tảng (platform / 플랫폼) nhóm (team / 팀) | WorkManager/FGS thay đổi (change / 변경) |
| permission hành vi (behavior / 동작) | maybe | yes | location/notification | tính năng (feature / 기능) nhóm (team / 팀) | permission máy trạng thái (state machine / 상태 머신) |
| edge-to-edge | target-dependent | yes | UI | UI nhóm (team / 팀) | insets |
| cục bộ (local / 로컬) mạng (network / 네트워크) | target-dependent | yes | discovery | thiết bị (device / 장치) nhóm (team / 팀) | permission luồng (flow / 흐름) |

Không để kiến thức (knowledge / 지식) chỉ nằm trong bản phát hành (release / 릴리스) notes trình duyệt (browser / 브라우저) tab của một nhà phát triển (developer / 개발자).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **13. Permission changes là tính tương thích (compatibility / 호환성) di chuyển (migration / 마이그레이션) điển hình** tiếp nhận điểm tựa từ **12. nền tảng (platform / 플랫폼) hành vi (behavior / 동작) ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Background thực thi (execution / 실행) thay đổi qua nền tảng (platform / 플랫폼) versions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Permission changes là tính tương thích (compatibility / 호환성) di chuyển (migration / 마이그레이션) điển hình

Permission có thể split thành nhiều permission mới, đổi grant hành vi (behavior / 동작), auto-reset, add one-time/approximate chế độ (mode / 모드) hoặc thay background truy cập (access / 접근) luồng (flow / 흐름).

Di chuyển (migration / 마이그레이션) phải kiểm thử (test / 테스트):

- fresh install trên OS mới;
- upgrade app trên OS cũ;
- OS upgrade khi app đã cài;
- app upgrade sau OS upgrade;
- permission previously granted/denied;
- người dùng (user / 사용자) revoke từ Settings;
- enterprise/thiết bị (device / 장치) chính sách (policy / 정책) nếu applicable.

Đây là lý do trường hợp (case / 사례) 10 mô hình (model / 모델) permission như máy trạng thái (state machine / 상태 머신) thay vì boolean.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **14. Background thực thi (execution / 실행) thay đổi qua nền tảng (platform / 플랫폼) versions** tiếp nhận điểm tựa từ **13. Permission changes là tính tương thích (compatibility / 호환성) di chuyển (migration / 마이그레이션) điển hình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. UI tính tương thích (compatibility / 호환성) không chỉ screen kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Background thực thi (execution / 실행) thay đổi qua nền tảng (platform / 플랫폼) versions

Dịch vụ (service / 서비스)/background start restrictions, chính xác (exact / 정확한) alarm, foreground-service types, JobScheduler/WorkManager hành vi (behavior / 동작) và battery chính sách (policy / 정책) đã evolve nhiều bản phát hành (release / 릴리스).

Mã (code / 코드) kiểu “dịch vụ (service / 서비스) chạy được trên phone tôi” không đủ. Background kiến trúc (architecture / 아키텍처) phải map yêu cầu (requirement / 요구사항) sang platform-supported thành phần nguyên thủy (primitive / 기본 요소) theo mục tiêu (target / 대상)/OS.

Nếu tác vụ (task / 작업) durable nhưng không exact-time, WorkManager thường phù hợp hơn giữ tiến trình (process / 프로세스)/dịch vụ (service / 서비스) sống.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **15. UI tính tương thích (compatibility / 호환성) không chỉ screen kích thước (size / 크기)** tiếp nhận điểm tựa từ **14. Background thực thi (execution / 실행) thay đổi qua nền tảng (platform / 플랫폼) versions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Predictive back và hệ thống (system / 시스템) điều hướng (navigation / 내비게이션) contracts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. UI tính tương thích (compatibility / 호환성) không chỉ screen kích thước (size / 크기)

Nền tảng (platform / 플랫폼) changes có thể ảnh hưởng status/điều hướng (navigation / 내비게이션) bar, edge-to-edge, predictive back, font, khả năng tiếp cận (accessibility / 접근성), gesture điều hướng (navigation / 내비게이션) và cửa sổ (window / 윈도우) management.

UI regression kiểm thử (test / 테스트) khi mục tiêu (target / 대상) upgrade phải cover hệ thống (system / 시스템) bars/insets, keyboard, back gesture, rotation/resizing, large screen và khả năng tiếp cận (accessibility / 접근성)—not chỉ screenshot main trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **16. Predictive back và hệ thống (system / 시스템) điều hướng (navigation / 내비게이션) contracts** tiếp nhận điểm tựa từ **15. UI tính tương thích (compatibility / 호환성) không chỉ screen kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. SDK Extensions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Predictive back và hệ thống (system / 시스템) điều hướng (navigation / 내비게이션) contracts

Back hành vi (behavior / 동작) đã evolve từ hardware button mô hình tư duy (mental model / 사고 모델) sang gesture/hệ thống (system / 시스템) animation đặc tả hợp đồng (contract / 계약). hiện đại (modern / 현대적) điều hướng (navigation / 내비게이션) nên dùng nền tảng (platform / 플랫폼)/AndroidX back APIs thay vì intercept key sự kiện (event / 이벤트) thủ công.

Nếu app custom back ngăn xếp (stack / 스택), kiểm thử (test / 테스트) back callback registration/vòng đời (lifecycle / 생명주기) và điều hướng (navigation / 내비게이션) transitions trên OS mới.

Tính tương thích (compatibility / 호환성) principle: integrate hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약) ở lớp trừu tượng (abstraction / 추상화) mức (level / 수준) chính thức, tránh hack dựa hiện thực (implementation / 구현) detail.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **17. SDK Extensions** tiếp nhận điểm tựa từ **16. Predictive back và hệ thống (system / 시스템) điều hướng (navigation / 내비게이션) contracts** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Extension phiên bản (version / 버전) check phải gắn Đặc tả API (API contract / API 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. SDK Extensions

Android có **SDK Extensions** để một số API capabilities được cập nhật ngoài traditional annual nền tảng (platform / 플랫폼) API mức (level / 수준) trên supported components.

Điều này tạo thêm phiên bản (version / 버전) axis: thiết bị (device / 장치) có API mức (level / 수준) X nhưng extension phiên bản (version / 버전) Y.

Khi dùng API gated bởi extension, check extension phiên bản (version / 버전) theo official API guidance thay vì chỉ `SDK_INT`.

Không cần mọi app dùng extension check; chỉ khi API documentation nói năng lực (capability / 역량) thuộc extension.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **18. Extension phiên bản (version / 버전) check phải gắn Đặc tả API (API contract / API 계약)** tiếp nhận điểm tựa từ **17. SDK Extensions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Mainline mô-đun (module / 모듈) và updatable hệ thống (system / 시스템) components** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Extension phiên bản (version / 버전) check phải gắn Đặc tả API (API contract / API 계약)

Pseudo-pattern:

```kotlin
val extension = SdkExtensions.getExtensionVersion(/* extension id */)
if (extension >= REQUIRED_VERSION) {
    // safe path documented for extension
}
```

ID/phiên bản (version / 버전) cụ thể phải lấy từ docs của API. Không hardcode magic number không nguồn.

Kiểm thử (test / 테스트) thiết bị (device / 장치)/emulator cần representative extension trạng thái (state / 상태) nếu tính năng (feature / 기능) phụ thuộc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **19. Mainline mô-đun (module / 모듈) và updatable hệ thống (system / 시스템) components** tiếp nhận điểm tựa từ **18. Extension phiên bản (version / 버전) check phải gắn Đặc tả API (API contract / API 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Non-SDK giao diện (interface / 인터페이스) là technical debt nguy hiểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Mainline mô-đun (module / 모듈) và updatable hệ thống (system / 시스템) components

Một số Android components có thể cập nhật (update / 업데이트) qua hệ thống (system / 시스템) mô-đun (module / 모듈) cơ chế (mechanism / 메커니즘) mà không chờ full OS OTA. Vì vậy two devices cùng API mức (level / 수준) không phải lúc nào có identical thành phần (component / 컴포넌트) hành vi (behavior / 동작)/phiên bản (version / 버전).

App nên dựa công khai (public / 공개) năng lực (capability / 역량)/phiên bản (version / 버전) checks thay vì manufacturer bản dựng (build / 빌드) fingerprint các giả định (assumptions / 가정들).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **20. Non-SDK giao diện (interface / 인터페이스) là technical debt nguy hiểm** tiếp nhận điểm tựa từ **19. Mainline mô-đun (module / 모듈) và updatable hệ thống (system / 시스템) components** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Reflection vào nền tảng (platform / 플랫폼) internals và R8 là hai rủi ro (risk / 위험) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Non-SDK giao diện (interface / 인터페이스) là technical debt nguy hiểm

Reflection vào hidden/private Android APIs có thể từng “chạy được” nhưng bị restriction ở bản phát hành (release / 릴리스) mới.

Non-SDK giao diện (interface / 인터페이스) chính sách (policy / 정책) ngày càng hạn chế truy cập (access / 접근). Nếu app/thư viện (library / 라이브러리) phụ thuộc hidden API:

- inventory ngay;
- tìm công khai (public / 공개) replacement;
- cập nhật (update / 업데이트) vendor SDK;
- isolate rủi ro (risk / 위험);
- kiểm thử (test / 테스트) latest OS preview.

Không xây cốt lõi (core / 핵심) tính năng (feature / 기능) dựa private khung phần mềm (framework / 프레임워크) phương thức (method / 메서드) chỉ vì StackOverflow có reflection snippet.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **21. Reflection vào nền tảng (platform / 플랫폼) internals và R8 là hai rủi ro (risk / 위험) khác nhau** tiếp nhận điểm tựa từ **20. Non-SDK giao diện (interface / 인터페이스) là technical debt nguy hiểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. OEM tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Reflection vào nền tảng (platform / 플랫폼) internals và R8 là hai rủi ro (risk / 위험) khác nhau

Reflection app-internal có shrinker/keep-rule concern. Reflection vào Android hidden API có nền tảng (platform / 플랫폼) tính tương thích (compatibility / 호환성) restriction concern. Có thể gặp cả hai nhưng không được nhầm.

Một reflection lời gọi (call / 호출) thất bại (fail / 실패) sau OS cập nhật (update / 업데이트) không nhất thiết do R8.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **22. OEM tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **21. Reflection vào nền tảng (platform / 플랫폼) internals và R8 là hai rủi ro (risk / 위험) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. WebView là independently evolving thời gian chạy (runtime / 런타임)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. OEM tính tương thích (compatibility / 호환성)

Android tính tương thích (compatibility / 호환성) Definition/bộ kiểm thử (test suite / 테스트 스위트) giảm fragmentation nhưng OEM/device-specific hiện thực (implementation / 구현) vẫn có khác biệt: camera, BLE, background scheduling, battery manager, WebView phiên bản (version / 버전), graphics driver.

Không mã (code / 코드) theo brand hack ngay từ đầu. Trước tiên xác định:

1. API công khai (public API / 공개 API) đặc tả hợp đồng (contract / 계약);
2. bug có reproduce AOSP/tham chiếu (reference / 참조) thiết bị (device / 장치) không;
3. OEM/phiên bản (version / 버전) cohort cụ thể;
4. workaround có bounded và observable không.

Cờ tính năng (feature flag / 기능 플래그)/remote cấu hình (config / 설정) có thể giúp disable workaround theo cohort, nhưng workaround phải có expiry/cleanup đơn vị sở hữu (owner / 오너).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **23. WebView là independently evolving thời gian chạy (runtime / 런타임)** tiếp nhận điểm tựa từ **22. OEM tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. thư viện (library / 라이브러리) minSdk và transitive các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. WebView là independently evolving thời gian chạy (runtime / 런타임)

WebView hành vi (behavior / 동작)/phiên bản (version / 버전) có thể cập nhật (update / 업데이트) độc lập OS trên nhiều devices. Hybrid app phải log WebView phiên bản (version / 버전) và kiểm thử (test / 테스트) representative channels.

Tính tương thích (compatibility / 호환성) issue JavaScript cầu nối (bridge / 브리지), cookie, TLS, tệp (file / 파일) chooser hoặc rendering không chỉ phụ thuộc API mức (level / 수준).

Do đó bug report nên capture OS + thiết bị (device / 장치) + WebView gói (package / 패키지)/phiên bản (version / 버전).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **24. thư viện (library / 라이브러리) minSdk và transitive các ràng buộc (constraints / 제약조건들)** tiếp nhận điểm tựa từ **23. WebView là independently evolving thời gian chạy (runtime / 런타임)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. minSdk increase là sản phẩm (product / 제품) quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. thư viện (library / 라이브러리) minSdk và transitive các ràng buộc (constraints / 제약조건들)

Upgrade một Jetpack/third-party thư viện (library / 라이브러리) có thể tăng minSdk hoặc yêu cầu compileSdk/toolchain mới. phụ thuộc (dependency / 의존성) upgrade vì thế có thể là platform-support quyết định (decision / 결정).

Before upgrade:

- đọc bản phát hành (release / 릴리스) notes;
- inspect minSdk/compile yêu cầu (requirement / 요구사항);
- check removed/deprecated APIs;
- kiểm thử (test / 테스트) nhị phân (binary / 이진)/nguồn (source / 소스) tính tương thích (compatibility / 호환성);
- run minSdk thiết bị (device / 장치)/emulator suite.

Không merge Renovate/Dependabot-style upgrade chỉ vì compile pass.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **25. minSdk increase là sản phẩm (product / 제품) quyết định (decision / 결정)** tiếp nhận điểm tựa từ **24. thư viện (library / 라이브러리) minSdk và transitive các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. mục tiêu (target / 대상) API chính sách (policy / 정책) và nền tảng (platform / 플랫폼) bản phát hành (release / 릴리스) không cùng timeline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. `minSdk` increase là sản phẩm (product / 제품) quyết định (decision / 결정)

Tăng minSdk có thể giảm tính tương thích (compatibility / 호환성) burden và cho phép API hiện đại hơn, nhưng loại người dùng (user / 사용자)/thiết bị (device / 장치) cũ khỏi future updates/install.

Quyết định (decision / 결정) cần usage telemetry, bảo mật (security / 보안) hỗ trợ (support / 지원), kỹ thuật (engineering / 엔지니어링) chi phí (cost / 비용), thị trường (market / 시장)/thiết bị (device / 장치) cohort và Play chính sách (policy / 정책)—not nhà phát triển (developer / 개발자) preference.

Khi drop old OS, clean tính tương thích (compatibility / 호환성) branches/dependencies dần để giảm permanent dead mã (code / 코드).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **26. mục tiêu (target / 대상) API chính sách (policy / 정책) và nền tảng (platform / 플랫폼) bản phát hành (release / 릴리스) không cùng timeline** tiếp nhận điểm tựa từ **25. minSdk increase là sản phẩm (product / 제품) quyết định (decision / 결정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. tính tương thích (compatibility / 호환성) testing với ADB toggles** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. mục tiêu (target / 대상) API chính sách (policy / 정책) và nền tảng (platform / 플랫폼) bản phát hành (release / 릴리스) không cùng timeline

Google Play mục tiêu (target / 대상) API yêu cầu (requirement / 요구사항) có deadline riêng. Latest OS có thể mới hơn mục tiêu (target / 대상) yêu cầu (requirement / 요구사항) tại một thời điểm.

Nhóm (team / 팀) nên nhánh học (track / 트랙):

```text
latest stable Android
latest preview/beta Android
current compileSdk
current targetSdk
Play minimum target requirement + deadline
minSdk support floor
```

Đừng chờ console warning mới lập kế hoạch.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **27. tính tương thích (compatibility / 호환성) testing với ADB toggles** tiếp nhận điểm tựa từ **26. mục tiêu (target / 대상) API chính sách (policy / 정책) và nền tảng (platform / 플랫폼) bản phát hành (release / 릴리스) không cùng timeline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. OS upgrade đường dẫn (path / 경로) khác fresh install** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. tính tương thích (compatibility / 호환성) testing với ADB toggles

Ngoài compat khung phần mềm (framework / 프레임워크), ADB giúp mô phỏng/revoke permission, force-stop, background trạng thái (state / 상태), tiến trình (process / 프로세스) death và app ops tùy API.

Kiểm thử (test / 테스트) script có thể encode regression scenario, nhưng ADB command là platform-specific công cụ (tool / 도구). Giữ scripts versioned và document API phạm vi (range / 범위).

Automation tốt biến di chuyển (migration / 마이그레이션) checklist thành repeatable bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **27. tính tương thích (compatibility / 호환성) testing với ADB toggles** xác định đầu vào; **28. OS upgrade đường dẫn (path / 경로) khác fresh install** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **29. App downgrade thường không phải supported quay lui (rollback / 롤백) đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. OS upgrade đường dẫn (path / 경로) khác fresh install

Một app cài trên Android N rồi thiết bị (device / 장치) upgrade lên N+1 có thể giữ permission/dữ liệu (data / 데이터)/trạng thái (state / 상태) khác fresh install N+1.

Trọng yếu (critical / 중요) tính năng (feature / 기능) nên kiểm thử (test / 테스트) cả:

```text
fresh N+1
install app on N → configure state → OS upgrade → launch on N+1
```

CI emulator upgrade automation không phải lúc nào đơn giản, nhưng bản phát hành (release / 릴리스) qualification lab/manual ma trận (matrix / 행렬) có thể cover representative đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **28. OS upgrade đường dẫn (path / 경로) khác fresh install** xác định đầu vào; **29. App downgrade thường không phải supported quay lui (rollback / 롤백) đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **30. Backend phiên bản (version / 버전) skew** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. App downgrade thường không phải supported quay lui (rollback / 롤백) đường dẫn (path / 경로)

Android trình quản lý gói (package manager / 패키지 관리자) thường không cho normal downgrade versionCode trên môi trường vận hành (production / 운영 환경) thiết bị (device / 장치). dữ liệu (data / 데이터) lược đồ (schema / 스키마) mới cũng có thể không readable bởi old nhị phân (binary / 이진).

Vì vậy tính tương thích (compatibility / 호환성) phải hướng **forward fix** và **backward-compatible dữ liệu (data / 데이터)/backend** hơn là dựa người dùng (user / 사용자) downgrade.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **29. App downgrade thường không phải supported quay lui (rollback / 롤백) đường dẫn (path / 경로)** xác định đầu vào; **30. Backend phiên bản (version / 버전) skew** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. tính tương thích (compatibility / 호환성) telemetry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Backend phiên bản (version / 버전) skew

Mobile fleet luôn có nhiều app versions cùng lúc. Backend đặc tả hợp đồng (contract / 계약) phải hỗ trợ (support / 지원) phiên bản (version / 버전) skew trong cửa sổ (window / 윈도우) hợp lý.

Khi mục tiêu (target / 대상) SDK di chuyển (migration / 마이그레이션) buộc app luồng (flow / 흐름) thay đổi, backend rollout cũng phải xem old clients.

Một máy chủ (server / 서버) deploy phá old app còn nguy hiểm hơn mục tiêu (target / 대상) SDK bug vì người dùng (user / 사용자) không cập nhật (update / 업데이트) ngay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **31. tính tương thích (compatibility / 호환성) telemetry** tiếp nhận điểm tựa từ **30. Backend phiên bản (version / 버전) skew** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. di chuyển (migration / 마이그레이션) playbook mẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. tính tương thích (compatibility / 호환성) telemetry

Crash/ANR/tính năng (feature / 기능) thất bại (failure / 실패) nên segment theo:

- app phiên bản (version / 버전);
- OS/API mức (level / 수준);
- mục tiêu (target / 대상) di chuyển (migration / 마이그레이션) cohort nếu staged;
- thiết bị (device / 장치) mô hình (model / 모델)/OEM;
- WebView/thư viện (library / 라이브러리) relevant phiên bản (version / 버전);
- cờ tính năng (feature flag / 기능 플래그) trạng thái (state / 상태).

Nếu chỉ xem toàn cục (global / 전역) crash tỷ lệ (rate / 비율), regression chỉ xảy ra API 37 có thể bị che bởi majority API 34–36.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **32. di chuyển (migration / 마이그레이션) playbook mẫu** tiếp nhận điểm tựa từ **31. tính tương thích (compatibility / 호환성) telemetry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. cấp cao (senior / 시니어) checklist cho một Android phiên bản (version / 버전) mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. di chuyển (migration / 마이그레이션) playbook mẫu

### Phase A — inventory

Liệt kê hành vi (behavior / 동작) changes, permissions, background APIs, hệ thống (system / 시스템) UI, lưu trữ (storage / 저장소), hardware integrations, hidden APIs.

### Phase B — current-app tính tương thích (compatibility / 호환성)

Chạy production-target app trên OS mới và fix all-app changes.

### Phase C — target-gated enablement

Dùng compat khung phần mềm (framework / 프레임워크)/toggle để bật thay đổi (change / 변경) riêng khi có thể.

### Phase D — mục tiêu (target / 대상) bump

Tăng mục tiêu (target / 대상), compile bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물), run full ma trận (matrix / 행렬).

### Phase E — staged rollout

Monitor API-level segmented metrics.

### Phase F — cleanup

Xóa tính tương thích (compatibility / 호환성) workaround obsolete, cập nhật (update / 업데이트) documentation và baseline.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, **33. cấp cao (senior / 시니어) checklist cho một Android phiên bản (version / 버전) mới** tiếp nhận điểm tựa từ **32. di chuyển (migration / 마이그레이션) playbook mẫu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Official references** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. cấp cao (senior / 시니어) checklist cho một Android phiên bản (version / 버전) mới

Hỏi:

- all-app hành vi (behavior / 동작) thay đổi (change / 변경) nào ảnh hưởng ngay;
- target-gated thay đổi (change / 변경) nào sẽ bật;
- permission/hệ thống (system / 시스템) UI/background/lưu trữ (storage / 저장소) có đổi không;
- third-party SDK đã certified chưa;
- non-SDK/reflection nào còn tồn tại;
- bản địa (native / 네이티브) `.so` compatible không;
- minSdk thiết bị (device / 장치) vẫn chạy sau thư viện (library / 라이브러리)/toolchain upgrade không;
- kiểm thử (test / 테스트) OS upgrade/fresh install đã có chưa;
- metrics có segment API/OEM không;
- quay lui (rollback / 롤백)/hotfix đường dẫn (path / 경로) là gì.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 18 — Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링): API mức (level / 수준), targetSdk, SDK Extensions và nền tảng (platform / 플랫폼) di chuyển (migration / 마이그레이션)**, sau nội dung của **33. cấp cao (senior / 시니어) checklist cho một Android phiên bản (version / 버전) mới**, **34. Official references** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 34. Official references
Phần này nối mạch Android vừa học với “34. Official references”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

- App tính tương thích (compatibility / 호환성): https://nhà phát triển (developer / 개발자).android.com/guide/app-compatibility
- nền tảng (platform / 플랫폼) hành vi (behavior / 동작) changes: https://nhà phát triển (developer / 개발자).android.com/about/versions
- kiểm thử (test / 테스트)/gỡ lỗi (debug / 디버그) hành vi (behavior / 동작) changes: https://nhà phát triển (developer / 개발자).android.com/guide/app-compatibility/test-debug
- SDK Extensions: https://nhà phát triển (developer / 개발자).android.com/guide/sdk-extensions
- mục tiêu (target / 대상) API requirements: https://nhà phát triển (developer / 개발자).android.com/google/play/requirements/target-sdk

Compatibility documentation là versioned source of truth. Mỗi lần target/OS upgrade phải đọc release-specific pages, không dựa duy nhất vào memory từ release trước.

> **Bàn giao:** Sau **34. Official references**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
