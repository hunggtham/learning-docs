# Trường hợp (case / 사례) 17 — Android NDK, JNI, ABI, bản địa (native / 네이티브) bộ nhớ (memory / 메모리) và 16 KB Page kích thước (size / 크기)

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 17 — Android NDK, JNI, ABI, bản địa (native / 네이티브) bộ nhớ (memory / 메모리) và 16 KB Page kích thước (size / 크기)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Android SDK và NDK giải quyết hai thế giới khác nhau** sang **2. bản địa (native / 네이티브) thư viện (library / 라이브러리) .so là dùng chung (shared / 공유) đối tượng (object / 객체) theo ABI**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Phần lớn Android app nghiệp vụ (business / 비즈니스) không cần viết C/C++. Kotlin/Java + Android SDK đủ cho UI, mạng (network / 네트워크), cơ sở dữ liệu (database / 데이터베이스), background công việc (work / 작업) và phần lớn media/hardware use trường hợp (case / 사례). Tuy nhiên khi app dùng codec, computer vision, cryptography thư viện (library / 라이브러리), game engine, ML thời gian chạy (runtime / 런타임), vendor SDK hoặc legacy C/C++ mã (code / 코드), bản địa (native / 네이티브) tầng (layer / 계층) trở thành một phần của môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템). Khi đó bug không còn chỉ là Kotlin exception; nó có thể là `SIGSEGV`, missing symbol, ABI mismatch, use-after-free, double free, JNI tham chiếu (reference / 참조) leak hoặc bản địa (native / 네이티브) nhị phân (binary / 이진) không compatible với nền tảng (platform / 플랫폼) mới.

Chapter này không biến người đọc thành C++ expert. Mục tiêu là hiểu ranh giới (boundary / 경계) JVM/ART ↔ bản địa (native / 네이티브) đủ sâu để integrate, gỡ lỗi (debug / 디버그) và rà soát (review / 검토) rủi ro (risk / 위험) đúng cách.

## 1. Android SDK và NDK giải quyết hai thế giới khác nhau

Android SDK cung cấp API Java/Kotlin-level. Android NDK cung cấp headers/toolchain/API C/C++ cho bản địa (native / 네이티브) mã (code / 코드).

Một app có thể chạy toàn bộ bằng managed mã (code / 코드). bản địa (native / 네이티브) mã (code / 코드) chỉ nên được thêm khi có lý do cụ thể: reuse thư viện C/C++, low-level hiệu năng (performance / 성능) tải công việc (workload / 워크로드) đã đo, engine có sẵn, vendor yêu cầu (requirement / 요구사항) hoặc API bản địa (native / 네이티브) đặc thù.

“C++ nhanh hơn Kotlin” không phải justification đủ. JNI crossing, manual bộ nhớ (memory / 메모리), nhị phân (binary / 이진) kích thước (size / 크기) và portability có chi phí (cost / 비용) lớn.

## 2. bản địa (native / 네이티브) thư viện (library / 라이브러리) `.so` là dùng chung (shared / 공유) đối tượng (object / 객체) theo ABI

Android gói (package / 패키지) có thể chứa bản địa (native / 네이티브) thư viện (library / 라이브러리) như:

```text
lib/
├── arm64-v8a/
│   └── libnativecore.so
├── armeabi-v7a/
│   └── libnativecore.so
├── x86_64/
│   └── libnativecore.so
└── ...
```

Mỗi `.so` được compile cho ABI cụ thể. thiết bị (device / 장치) chỉ tải (load / 로드) nhị phân (binary / 이진) matching kiến trúc (architecture / 아키텍처).

ABI không chỉ là CPU name; nó là đặc tả hợp đồng (contract / 계약) về instruction set, calling convention, dữ liệu (data / 데이터) bố cục (layout / 레이아웃) và nhị phân (binary / 이진) giao diện (interface / 인터페이스).

## 3. Các ABI phổ biến cần nhận diện

`arm64-v8a` là 64-bit ARM phổ biến trên phone/tablet hiện đại. `armeabi-v7a` là ARM 32-bit legacy hơn. `x86_64` thường gặp ở emulator và một số môi trường (environment / 환경).

Không nên ship mọi ABI theo thói quen. Hỗ trợ ABI nào phụ thuộc sản phẩm (product / 제품)/thiết bị (device / 장치) chính sách (policy / 정책) và phụ thuộc (dependency / 의존성) availability.

AAB giúp Play phân phối ABI split phù hợp, nhưng nguồn (source / 소스) bundle vẫn phải chứa bản địa (native / 네이티브) sản phẩm tạo ra (artifact / 산출물) đúng cho ABI cần hỗ trợ (support / 지원).

## 4. JNI là cầu nối (bridge / 브리지), không phải nghiệp vụ (business / 비즈니스) kiến trúc (architecture / 아키텍처)

**Java bản địa (native / 네이티브) giao diện (interface / 인터페이스) — JNI** cho managed mã (code / 코드) gọi bản địa (native / 네이티브) hàm (function / 함수) và bản địa (native / 네이티브) mã (code / 코드) tương tác JVM/ART objects.

Kotlin:

```kotlin
object NativeCore {
    init {
        System.loadLibrary("nativecore")
    }

    external fun checksum(data: ByteArray): Long
}
```

C/C++ side có symbol tương ứng hoặc dùng tường minh (explicit / 명시적) registration.

JNI nên được bọc sau một Kotlin-facing API nhỏ. Không để ViewModel/UI rải `external` lời gọi (call / 호출) khắp codebase. ranh giới (boundary / 경계) nhỏ giúp kiểm thử (test / 테스트), fallback, crash isolation lập luận (reasoning / 추론) và di chuyển (migration / 마이그레이션) dễ hơn.

## 5. `System.loadLibrary()` và thư viện (library / 라이브러리) loading

`System.loadLibrary("nativecore")` tìm `libnativecore.so`. tải (load / 로드) có thể thất bại (fail / 실패) vì:

- ABI không có;
- dependent `.so` thiếu;
- symbol/phiên bản (version / 버전) mismatch;
- packaging sai;
- page alignment/nền tảng (platform / 플랫폼) incompatibility;
- thư viện (library / 라이브러리) name sai.

`UnsatisfiedLinkError` là dấu hiệu ranh giới (boundary / 경계) packaging/linking, không phải Kotlin lô-gic (logic / 논리) lỗi (error / 오류) thông thường.

## 6. Static registration và động (dynamic / 동적) registration

JNI hàm (function / 함수) có thể được tìm bằng naming convention hoặc đăng ký bằng `RegisterNatives`.

Naming convention đơn giản cho demo nhưng tên symbol dài và coupling lớp (class / 클래스)/gói (package / 패키지) name cao. tường minh (explicit / 명시적) registration cho phép kiểm soát ranh giới (boundary / 경계) rõ hơn và thường được thư viện (library / 라이브러리) lớn dùng.

Dù cách nào, R8/obfuscation có thể ảnh hưởng lớp (class / 클래스)/phương thức (method / 메서드) name nếu bản địa (native / 네이티브) mã (code / 코드) dựa reflection/name. thư viện (library / 라이브러리) cần keep rules đúng hoặc registration chiến lược (strategy / 전략) phù hợp.

## 7. JNI types không giống Kotlin types về quyền sở hữu (ownership / 소유권)

JNI dùng `jobject`, `jstring`, `jbyteArray`, `jclass`... Đây là handles managed objects, không phải raw pointer vào đối tượng (object / 객체) bố cục (layout / 레이아웃) JVM.

Bản địa (native / 네이티브) mã (code / 코드) phải dùng `JNIEnv*` APIs để thao tác. Không cast tùy tiện `jobject` thành struct pointer.

Managed GC có quyền di chuyển/collect đối tượng (object / 객체) theo đặc tả hợp đồng (contract / 계약) thời gian chạy (runtime / 런타임). JNI API tồn tại để giữ lớp trừu tượng (abstraction / 추상화) này.

## 8. cục bộ (local / 로컬) tham chiếu (reference / 참조) và toàn cục (global / 전역) tham chiếu (reference / 참조)

JNI cục bộ (local / 로컬) references thường valid trong bản địa (native / 네이티브) lời gọi (call / 호출)/frame hiện tại và được cleanup khi return. Nếu vòng lặp (loop / 루프) tạo rất nhiều cục bộ (local / 로컬) ref mà không giải phóng sớm, cục bộ (local / 로컬) tham chiếu (reference / 참조) bảng (table / 테이블) có thể overflow.

Toàn cục (global / 전역) tham chiếu (reference / 참조) sống qua lời gọi (call / 호출) và phải `DeleteGlobalRef` khi không còn dùng. Quên xóa tạo managed-object leak từ bản địa (native / 네이티브) side.

Weak toàn cục (global / 전역) tham chiếu (reference / 참조) có ngữ nghĩa (semantics / 의미론) khác và chỉ dùng khi hiểu vòng đời (lifecycle / 생명주기).

Quyền sở hữu (ownership / 소유권) quy tắc (rule / 규칙) phải được document giống tài nguyên (resource / 자원) khác.

## 9. `JNIEnv*` là thread-affine

`JNIEnv*` không được lấy ở luồng thực thi (thread / 스레드) A rồi dùng ở luồng thực thi (thread / 스레드) B. bản địa (native / 네이티브) luồng thực thi (thread / 스레드) muốn gọi JVM phải attach với `JavaVM`, lấy môi trường (environment / 환경) đúng luồng thực thi (thread / 스레드), rồi detach theo vòng đời (lifecycle / 생명주기) phù hợp.

Sai luồng thực thi (thread / 스레드) quyền sở hữu (ownership / 소유권) là nguồn crash khó reproduce.

Một thiết kế (design / 설계) tốt centralize attach/detach lô-gic (logic / 논리), không rải manual JNI luồng thực thi (thread / 스레드) handling ở nhiều nơi.

## 10. JavaVM, luồng thực thi (thread / 스레드) và callback về Kotlin

Bản địa (native / 네이티브) engine có thể tạo worker luồng thực thi (thread / 스레드) và muốn callback lên Kotlin. luồng (flow / 흐름) điển hình:

```text
native worker
→ AttachCurrentThread
→ obtain JNIEnv
→ resolve/call Java method
→ handle exception
→ release refs
→ DetachCurrentThread nếu ownership yêu cầu
```

Callback không tự động chạy main luồng thực thi (thread / 스레드). Nếu callback ảnh hưởng UI/trạng thái (state / 상태) main-confined, Kotlin ranh giới (boundary / 경계) phải dispatch phù hợp.

## 11. bản địa (native / 네이티브) exception và Java exception không tự map an toàn

C++ exception không nên xuyên JNI ranh giới (boundary / 경계) một cách không kiểm soát. Java exception pending trong JNI cũng phải được check/clear/propagate đúng.

Ranh giới (boundary / 경계) nên chuyển thất bại (failure / 실패) thành tường minh (explicit / 명시적) lỗi (error / 오류)/kết quả (result / 결과) đặc tả hợp đồng (contract / 계약).

Ví dụ bản địa (native / 네이티브) parser có thể trả status mã (code / 코드) + message, Kotlin wrapper map thành lĩnh vực (domain / 도메인) lỗi (error / 오류) thay vì để undefined exception hành vi (behavior / 동작) xuyên tầng (layer / 계층).

## 12. String conversion có encoding và thời gian tồn tại (lifetime / 수명)

`jstring` ↔ UTF biểu diễn (representation / 표현) cần API JNI. Pointer từ `GetStringUTFChars` có thời gian tồn tại (lifetime / 수명) cần bản phát hành (release / 릴리스).

Không giữ pointer sau bản phát hành (release / 릴리스). Không assume mọi string lĩnh vực (domain / 도메인) phù hợp modified UTF-8 ngữ nghĩa (semantics / 의미론) của JNI API mà không kiểm tra use trường hợp (case / 사례).

Với nhị phân (binary / 이진) dữ liệu (data / 데이터), dùng `ByteArray`/buffer đặc tả hợp đồng (contract / 계약) rõ thay vì lạm dụng string.

## 13. Array bản sao (copy / 복사) vs pinning

JNI API truy cập thành phần nguyên thủy (primitive / 기본 요소) array có thể bản sao (copy / 복사) hoặc pin tùy thời gian chạy (runtime / 런타임). Không nên assume pointer luôn trỏ trực tiếp vùng nhớ động (heap / 힙) đối tượng (object / 객체).

Trọng yếu (critical / 중요) sections phải ngắn. Giữ array pinned lâu có thể ảnh hưởng GC/thời gian chạy (runtime / 런타임).

Large streaming dữ liệu (data / 데이터) nên cân nhắc direct buffers hoặc native-owned bộ nhớ (memory / 메모리) với đặc tả hợp đồng (contract / 계약) rõ thay vì bản sao (copy / 복사) liên tục qua JNI.

## 14. Direct `ByteBuffer`

Direct buffer có thể cung cấp bộ nhớ (memory / 메모리) region thuận lợi cho bản địa (native / 네이티브) interoperability, giảm một số bản sao (copy / 복사) trong tải công việc (workload / 워크로드) phù hợp.

Nhưng zero-copy không tự động đồng nghĩa nhanh hơn. Allocation, quyền sở hữu (ownership / 소유권), synchronization và bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) vẫn cần đo.

Nếu bản địa (native / 네이티브) giữ pointer tới direct buffer, thời gian tồn tại (lifetime / 수명) của buffer phía managed phải đảm bảo đủ lâu.

## 15. bản địa (native / 네이티브) bộ nhớ (memory / 메모리) không nằm hoàn toàn trong JVM vùng nhớ động (heap / 힙) chỉ số (metric / 지표)

C++ `malloc/new`, mmap, graphics/bản địa (native / 네이티브) buffers có thể tăng tiến trình (process / 프로세스) RSS/bản địa (native / 네이티브) vùng nhớ động (heap / 힙) dù Java vùng nhớ động (heap / 힙) nhìn bình thường.

OOM diagnosis phải xem:

- managed vùng nhớ động (heap / 힙);
- bản địa (native / 네이티브) vùng nhớ động (heap / 힙);
- graphics/buffer bộ nhớ (memory / 메모리);
- mã (code / 코드)/mapped files;
- luồng thực thi (thread / 스레드) stacks;
- dùng chung (shared / 공유) bộ nhớ (memory / 메모리).

Trường hợp (case / 사례) 09 đã xây tiến trình (process / 프로세스)/bộ nhớ (memory / 메모리) mô hình tư duy (mental model / 사고 모델); bản địa (native / 네이티브) tầng (layer / 계층) là lý do quan trọng cần nhìn process-level bằng chứng (evidence / 증거) thay vì chỉ Android Studio Java vùng nhớ động (heap / 힙).

## 16. RAII và quyền sở hữu (ownership / 소유권) trong C++

C++ môi trường vận hành (production / 운영 환경) mã (code / 코드) nên ưu tiên RAII và smart pointers để tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) gắn đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명).

`std::unique_ptr` biểu diễn single quyền sở hữu (ownership / 소유권). `std::shared_ptr` chỉ dùng khi quyền sở hữu (ownership / 소유권) thật sự dùng chung (shared / 공유); dùng mọi nơi có thể tạo cycle và atomic overhead.

JNI handles/tệp (file / 파일) descriptors/mutex/bản địa (native / 네이티브) cửa sổ (window / 윈도우) cũng nên được wrap trong RAII đối tượng (object / 객체) khi hợp lý.

Manual `new/delete` rải rác qua callback paths là mùi mã (code / 코드) mạnh.

## 17. Use-after-free và double free

Managed mã (code / 코드) thường được bảo vệ khỏi raw bộ nhớ (memory / 메모리) bugs; C/C++ không. Một callback async giữ raw pointer tới đối tượng (object / 객체) đã destroy có thể crash random sau vài phút.

Bản địa (native / 네이티브) async API cần tường minh (explicit / 명시적) quyền sở hữu (ownership / 소유권):

```text
request owns operation
operation owns callback state
cancel/destroy transitions state
callback checks liveness/generation
```

Không fix use-after-free bằng sleep hoặc null check ngẫu nhiên.

## 18. Race điều kiện (condition / 조건) bản địa (native / 네이티브) và Kotlin vẫn là cùng một tính đồng thời (concurrency / 동시성) bài toán (problem / 문제)

JNI không tạo automatic synchronization. Nếu Kotlin luồng thực thi (thread / 스레드) và bản địa (native / 네이티브) worker cùng truy cập (access / 접근) bản địa (native / 네이티브) trạng thái (state / 상태), cần mutex/atomic/message passing theo bất biến (invariant / 불변식) rõ.

Một Kotlin `Mutex` không bảo vệ mã (code / 코드) C++ nếu bản địa (native / 네이티브) truy cập trạng thái (state / 상태) bên ngoài trọng yếu (critical / 중요) section đó. khóa (lock / 잠금) ranh giới (boundary / 경계) phải bao trùm đúng trạng thái dùng chung (shared state / 공유 상태) ở đúng tầng (layer / 계층).

## 19. CMake và `externalNativeBuild`

Android Gradle Plugin có thể integrate CMake/NDK bản dựng (build / 빌드).

```kotlin
android {
    externalNativeBuild {
        cmake {
            path = file("src/main/cpp/CMakeLists.txt")
        }
    }
}
```

CMakeLists ví dụ:

```cmake
cmake_minimum_required(VERSION 3.22.1)
project(nativecore)

add_library(nativecore SHARED native_core.cpp)

find_library(log-lib log)

target_link_libraries(nativecore ${log-lib})
```

Phiên bản (version / 버전)/toolchain thực tế phải theo dự án (project / 프로젝트) baseline, không bản sao (copy / 복사) con số mẫu (sample / 표본) một cách máy móc.

## 20. Prebuilt `.so` và `jniLibs`

Vendor SDK có thể ship prebuilt libraries trong `src/main/jniLibs/<abi>/` hoặc AAR.

Prebuilt nhị phân (binary / 이진) là supply-chain sản phẩm tạo ra (artifact / 산출물). nhóm (team / 팀) cần biết:

- ABI ma trận (matrix / 행렬);
- NDK/toolchain origin nếu có thể;
- gỡ lỗi (debug / 디버그) symbols;
- license;
- CVE/cập nhật (update / 업데이트) chính sách (policy / 정책);
- 16 KB page tính tương thích (compatibility / 호환성);
- transitive bản địa (native / 네이티브) dependencies.

Một AAR upgrade có thể đổi `.so` mà Gradle phụ thuộc (dependency / 의존성) diff không làm rủi ro (risk / 위험) này hiển nhiên.

## 21. 16 KB bộ nhớ (memory / 메모리) page kích thước (size / 크기) là tính tương thích (compatibility / 호환성) yêu cầu (requirement / 요구사항) quan trọng

Android ecosystem đang hỗ trợ thiết bị (device / 장치) có page kích thước (size / 크기) lớn hơn 4 KB. bản địa (native / 네이티브) dùng chung (shared / 공유) libraries phải có ELF segment alignment phù hợp để chạy đúng trên thiết bị (device / 장치) 16 KB page kích thước (size / 크기).

NDK mới hỗ trợ bản dựng (build / 빌드) alignment phù hợp tốt hơn; nhưng prebuilt `.so` cũ vẫn có thể không compatible. Vì vậy dự án (project / 프로젝트) có bản địa (native / 네이티브) phụ thuộc (dependency / 의존성) phải inventory **tất cả bản địa (native / 네이티브) libraries**, không chỉ mã (code / 코드) C++ tự bản dựng (build / 빌드).

Kiểm thử (test / 테스트) nên gồm emulator/thiết bị (device / 장치) cấu hình (configuration / 구성) hỗ trợ 16 KB page kích thước (size / 크기) và inspect bundle/bản địa (native / 네이티브) alignment trong bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인).

## 22. NDK phiên bản (version / 버전) là toolchain phụ thuộc (dependency / 의존성), không phải chi tiết cục bộ (local / 로컬) machine

Pin NDK phiên bản (version / 버전) để cục bộ (local / 로컬)/CI reproducible:

```kotlin
android {
    ndkVersion = "<approved-version>"
}
```

Upgrade NDK có thể thay trình biên dịch (compiler / 컴파일러)/linker hành vi (behavior / 동작), libc++ hiện thực (implementation / 구현), warning, symbol hoặc nhị phân (binary / 이진) đầu ra (output / 출력). Với native-heavy app, NDK upgrade nên có benchmark/crash/thiết bị (device / 장치) kiểm tra hợp lệ (validation / 검증) riêng.

## 23. STL và C++ thời gian chạy (runtime / 런타임)

Hiện đại (modern / 현대적) NDK dùng libc++ cho C++ thư viện chuẩn (standard library / 표준 라이브러리). Static/dùng chung (shared / 공유) thời gian chạy (runtime / 런타임) choice có packaging implications khi nhiều `.so` cùng dùng C++ thời gian chạy (runtime / 런타임).

Không trộn prebuilt bản địa (native / 네이티브) libraries có incompatible STL/thời gian chạy (runtime / 런타임) các giả định (assumptions / 가정들) mà không verify vendor guidance.

Bản địa (native / 네이티브) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) giống managed dependencies: transitive nhị phân (binary / 이진) đặc tả hợp đồng (contract / 계약) có thể gây thời gian chạy (runtime / 런타임) thất bại (failure / 실패) dù link bản dựng (build / 빌드) pass.

## 24. API mức (level / 수준) trong bản địa (native / 네이티브) mã (code / 코드)

NDK API availability cũng phụ thuộc Android API mức (level / 수준). Compile against symbol mới không có nghĩa thiết bị (device / 장치) minSdk cũ có symbol thời gian chạy (runtime / 런타임) đó.

Cần guard API hoặc động (dynamic / 동적) lookup phù hợp khi hỗ trợ (support / 지원) OS cũ.

Không sử dụng private/non-NDK vendor thư viện (library / 라이브러리) như stable API công khai (public API / 공개 API). nền tảng (platform / 플랫폼) restrictions với non-public bản địa (native / 네이티브) libraries đã chặt hơn qua các Android versions.

## 25. tệp (file / 파일) descriptor là cầu nối (bridge / 브리지) mạnh giữa managed và bản địa (native / 네이티브)

Nhiều Android APIs expose tệp (file / 파일) descriptor qua ParcelFileDescriptor. bản địa (native / 네이티브) mã (code / 코드) có thể làm việc với fd mà không cần raw filesystem đường dẫn (path / 경로).

Điều này đặc biệt hữu ích với content URI/SAF nơi “real đường dẫn (path / 경로)” không tồn tại hoặc không nên được truy tìm.

Thiết kế (design / 설계) đúng:

```text
ContentResolver opens descriptor
→ transfer/dup fd ownership rõ
→ native reads/writes fd
→ close exactly once
```

Quyền sở hữu (ownership / 소유권) fd phải tường minh (explicit / 명시적) để tránh leak/double close.

## 26. AHardwareBuffer và graphics/media bộ nhớ (memory / 메모리)

Advanced camera/graphics/ML pipelines có thể dùng hardware buffers để chia bộ nhớ (memory / 메모리) giữa components/hardware paths hiệu quả hơn.

Đây là high-complexity API. Chỉ dùng khi profiling chứng minh bản sao (copy / 복사)/bandwidth là bottleneck và nhóm (team / 팀) hiểu synchronization/fence/thời gian tồn tại (lifetime / 수명).

Một lớp trừu tượng (abstraction / 추상화) “zero-copy” sai có thể tạo corruption hoặc GPU/CPU sync stall khó gỡ lỗi (debug / 디버그).

## 27. bản địa (native / 네이티브) logging và symbolication

`__android_log_print` hoặc logging wrapper giúp bản địa (native / 네이티브) log, nhưng môi trường vận hành (production / 운영 환경) crash cần bản địa (native / 네이티브) symbols.

Bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인) nên archive unstripped symbols hoặc symbol gói (package / 패키지) tương ứng phiên bản (version / 버전). Crash address không có symbol gần như vô dụng.

R8 ánh xạ (mapping / 매핑) giải Java/Kotlin obfuscation; bản địa (native / 네이티브) symbols giải C/C++ ngăn xếp (stack / 스택). Hai sản phẩm tạo ra (artifact / 산출물) khác nhau.

## 28. Tombstone và bản địa (native / 네이티브) crash

Bản địa (native / 네이티브) crash có tín hiệu (signal / 신호) như `SIGSEGV`, `SIGABRT`, `SIGBUS`. Tombstone/bản địa (native / 네이티브) crash report có register, fault address, ngăn xếp (stack / 스택) frames, loaded libraries.

Gỡ lỗi (debug / 디버그) luồng (flow / 흐름):

```text
identify exact build/version/ABI
→ obtain matching symbols
→ symbolize stack
→ inspect faulting thread
→ classify memory/race/assert/linking
→ reproduce with sanitizer if possible
```

Không kết luận “NDK bug” chỉ vì ngăn xếp (stack / 스택) có bản địa (native / 네이티브) frame.

## 29. Sanitizers

AddressSanitizer/HWASan hoặc các sanitizer phù hợp có thể phát hiện bộ nhớ (memory / 메모리) bug như buffer overflow/use-after-free trong kiểm thử (test / 테스트)/dev môi trường (environment / 환경).

ThreadSanitizer hỗ trợ (support / 지원)/use trường hợp (case / 사례) tùy nền tảng (platform / 플랫폼)/toolchain; overhead cao nên không phải môi trường vận hành (production / 운영 환경) default.

Native-heavy codebase nên có sanitizer chiến lược (strategy / 전략) trong CI/thiết bị (device / 장치) testing cho trọng yếu (critical / 중요) libraries.

## 30. hiệu năng (performance / 성능): JNI lời gọi (call / 호출) overhead và batching

JNI crossing có chi phí (cost / 비용). Gọi bản địa (native / 네이티브) hàm (function / 함수) hàng triệu lần với payload nhỏ có thể chậm hơn batch processing.

Thay vì:

```text
for every pixel → JNI call
```

nên cân nhắc:

```text
pass buffer/frame → native processes whole batch → one result
```

Nhưng batch quá lớn tăng độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리). Đo tải công việc (workload / 워크로드) thật.

## 31. bản địa (native / 네이티브) luồng thực thi (thread / 스레드) priority và hiệu năng (performance / 성능) hint

Real-time-ish media/game tải công việc (workload / 워크로드) đôi khi cần luồng thực thi (thread / 스레드) scheduling/hiệu năng (performance / 성능) hint APIs. Đây là platform-level tối ưu hóa (optimization / 최적화), không phải thứ nghiệp vụ (business / 비즈니스) app nên dùng mặc định.

Trước khi điều chỉnh priority/hint, đo frame deadline, CPU utilization, thermal throttling và battery impact.

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) bản địa (native / 네이티브) không tách khỏi thiết bị (device / 장치) thermal/power chính sách (policy / 정책).

## 32. bản địa (native / 네이티브) thư viện (library / 라이브러리) bảo mật (security / 보안)

C/C++ tăng attack surface memory-safety. đầu vào (input / 입력) từ mạng (network / 네트워크)/tệp (file / 파일)/media phải được coi untrusted.

Best practices gồm:

- cập nhật third-party bản địa (native / 네이티브) dependencies;
- fuzz parser nếu rủi ro (risk / 위험) cao;
- validate length/offset;
- tránh unsafe C APIs;
- compile hardening flags theo toolchain defaults/recommendations;
- giảm exposed JNI surface;
- không parse attacker-controlled nhị phân (binary / 이진) bằng legacy thư viện (library / 라이브러리) không maintained.

## 33. Khi nào không nên viết NDK

Không dùng NDK chỉ để:

- “giấu secret” — bản địa (native / 네이티브) nhị phân (binary / 이진) vẫn reverse-engineer được;
- gọi HTTP nhanh hơn;
- viết nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) thông thường;
- tránh học coroutine;
- micro-optimize trước khi profile.

Managed mã (code / 코드) thường an toàn, maintainable và portable hơn.

## 34. ranh giới (boundary / 경계) thiết kế (design / 설계) mẫu

```kotlin
interface ImageEngine {
    suspend fun analyze(frame: Frame): AnalysisResult
}

class NativeImageEngine : ImageEngine {
    override suspend fun analyze(frame: Frame): AnalysisResult =
        withContext(Dispatchers.Default) {
            nativeAnalyze(frame.bytes).toDomain()
        }

    private external fun nativeAnalyze(bytes: ByteArray): NativeResult
}
```

Môi trường vận hành (production / 운영 환경) hiện thực (implementation / 구현) có thể cần direct buffer/tài nguyên (resource / 자원) pool, nhưng idea quan trọng là bản địa (native / 네이티브) detail không leak vào toàn kiến trúc (architecture / 아키텍처).

Kiểm thử (test / 테스트) có thể dùng fake `ImageEngine` mà không tải (load / 로드) `.so`.

## 35. bản phát hành (release / 릴리스) checklist bản địa (native / 네이티브)

Trước bản phát hành (release / 릴리스) app có bản địa (native / 네이티브) mã (code / 코드), verify:

1. ABI hỗ trợ (support / 지원) ma trận (matrix / 행렬) đúng.
2. AAB/APK chứa `.so` expected.
3. 16 KB page-size tính tương thích (compatibility / 호환성) nếu applicable.
4. Symbols archive theo bản phát hành (release / 릴리스).
5. R8/JNI keep rules đúng.
6. Upgrade trên representative devices.
7. minSdk/bản địa (native / 네이티브) API guards đúng.
8. sanitizer/static phân tích (analysis / 분석) cho mã (code / 코드) trọng yếu (critical / 중요).
9. bản địa (native / 네이티브) bộ nhớ (memory / 메모리)/leak benchmark.
10. third-party bản địa (native / 네이티브) thư viện (library / 라이브러리) inventory/CVE/license.

## 36. Official references

- Android NDK guides: https://nhà phát triển (developer / 개발자).android.com/ndk/guides
- NDK API tham chiếu (reference / 참조): https://nhà phát triển (developer / 개발자).android.com/ndk/tham chiếu (reference / 참조)
- JNI tips: https://nhà phát triển (developer / 개발자).android.com/huấn luyện (training / 학습)/articles/perf-jni
- 16 KB page sizes: https://nhà phát triển (developer / 개발자).android.com/guide/practices/page-sizes

Bản địa (native / 네이티브) toolchain và nền tảng (platform / 플랫폼) các ràng buộc (constraints / 제약조건들) thay đổi theo Android/NDK bản phát hành (release / 릴리스). Luôn kiểm tra documentation của NDK phiên bản (version / 버전) và thiết bị (device / 장치) mục tiêu (target / 대상) thực tế khi ship.

> **Bàn giao:** Sau **36. Official references**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture end to end](./01_architecture_end_to_end.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
