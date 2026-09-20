# Case 17 — Android NDK, JNI, ABI, Native Memory và 16 KB Page Size

Phần lớn Android app business không cần viết C/C++. Kotlin/Java + Android SDK đủ cho UI, network, database, background work và phần lớn media/hardware use case. Tuy nhiên khi app dùng codec, computer vision, cryptography library, game engine, ML runtime, vendor SDK hoặc legacy C/C++ code, native layer trở thành một phần của production system. Khi đó bug không còn chỉ là Kotlin exception; nó có thể là `SIGSEGV`, missing symbol, ABI mismatch, use-after-free, double free, JNI reference leak hoặc native binary không compatible với platform mới.

Chapter này không biến người đọc thành C++ expert. Mục tiêu là hiểu boundary JVM/ART ↔ native đủ sâu để integrate, debug và review risk đúng cách.

## 1. Android SDK và NDK giải quyết hai thế giới khác nhau

Android SDK cung cấp API Java/Kotlin-level. Android NDK cung cấp headers/toolchain/API C/C++ cho native code.

Một app có thể chạy toàn bộ bằng managed code. Native code chỉ nên được thêm khi có lý do cụ thể: reuse thư viện C/C++, low-level performance workload đã đo, engine có sẵn, vendor requirement hoặc API native đặc thù.

“C++ nhanh hơn Kotlin” không phải justification đủ. JNI crossing, manual memory, binary size và portability có cost lớn.

## 2. Native library `.so` là shared object theo ABI

Android package có thể chứa native library như:

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

Mỗi `.so` được compile cho ABI cụ thể. Device chỉ load binary matching architecture.

ABI không chỉ là CPU name; nó là contract về instruction set, calling convention, data layout và binary interface.

## 3. Các ABI phổ biến cần nhận diện

`arm64-v8a` là 64-bit ARM phổ biến trên phone/tablet hiện đại. `armeabi-v7a` là ARM 32-bit legacy hơn. `x86_64` thường gặp ở emulator và một số environment.

Không nên ship mọi ABI theo thói quen. Hỗ trợ ABI nào phụ thuộc product/device policy và dependency availability.

AAB giúp Play phân phối ABI split phù hợp, nhưng source bundle vẫn phải chứa native artifact đúng cho ABI cần support.

## 4. JNI là bridge, không phải business architecture

**Java Native Interface — JNI** cho managed code gọi native function và native code tương tác JVM/ART objects.

Kotlin:

```kotlin
object NativeCore {
    init {
        System.loadLibrary("nativecore")
    }

    external fun checksum(data: ByteArray): Long
}
```

C/C++ side có symbol tương ứng hoặc dùng explicit registration.

JNI nên được bọc sau một Kotlin-facing API nhỏ. Không để ViewModel/UI rải `external` call khắp codebase. Boundary nhỏ giúp test, fallback, crash isolation reasoning và migration dễ hơn.

## 5. `System.loadLibrary()` và library loading

`System.loadLibrary("nativecore")` tìm `libnativecore.so`. Load có thể fail vì:

- ABI không có;
- dependent `.so` thiếu;
- symbol/version mismatch;
- packaging sai;
- page alignment/platform incompatibility;
- library name sai.

`UnsatisfiedLinkError` là dấu hiệu boundary packaging/linking, không phải Kotlin logic error thông thường.

## 6. Static registration và dynamic registration

JNI function có thể được tìm bằng naming convention hoặc đăng ký bằng `RegisterNatives`.

Naming convention đơn giản cho demo nhưng tên symbol dài và coupling class/package name cao. Explicit registration cho phép kiểm soát boundary rõ hơn và thường được library lớn dùng.

Dù cách nào, R8/obfuscation có thể ảnh hưởng class/method name nếu native code dựa reflection/name. Library cần keep rules đúng hoặc registration strategy phù hợp.

## 7. JNI types không giống Kotlin types về ownership

JNI dùng `jobject`, `jstring`, `jbyteArray`, `jclass`... Đây là handles managed objects, không phải raw pointer vào object layout JVM.

Native code phải dùng `JNIEnv*` APIs để thao tác. Không cast tùy tiện `jobject` thành struct pointer.

Managed GC có quyền di chuyển/collect object theo contract runtime. JNI API tồn tại để giữ abstraction này.

## 8. Local reference và global reference

JNI local references thường valid trong native call/frame hiện tại và được cleanup khi return. Nếu loop tạo rất nhiều local ref mà không giải phóng sớm, local reference table có thể overflow.

Global reference sống qua call và phải `DeleteGlobalRef` khi không còn dùng. Quên xóa tạo managed-object leak từ native side.

Weak global reference có semantics khác và chỉ dùng khi hiểu lifecycle.

Ownership rule phải được document giống resource khác.

## 9. `JNIEnv*` là thread-affine

`JNIEnv*` không được lấy ở thread A rồi dùng ở thread B. Native thread muốn gọi JVM phải attach với `JavaVM`, lấy environment đúng thread, rồi detach theo lifecycle phù hợp.

Sai thread ownership là nguồn crash khó reproduce.

Một design tốt centralize attach/detach logic, không rải manual JNI thread handling ở nhiều nơi.

## 10. JavaVM, thread và callback về Kotlin

Native engine có thể tạo worker thread và muốn callback lên Kotlin. Flow điển hình:

```text
native worker
→ AttachCurrentThread
→ obtain JNIEnv
→ resolve/call Java method
→ handle exception
→ release refs
→ DetachCurrentThread nếu ownership yêu cầu
```

Callback không tự động chạy main thread. Nếu callback ảnh hưởng UI/state main-confined, Kotlin boundary phải dispatch phù hợp.

## 11. Native exception và Java exception không tự map an toàn

C++ exception không nên xuyên JNI boundary một cách không kiểm soát. Java exception pending trong JNI cũng phải được check/clear/propagate đúng.

Boundary nên chuyển failure thành explicit error/result contract.

Ví dụ native parser có thể trả status code + message, Kotlin wrapper map thành domain error thay vì để undefined exception behavior xuyên layer.

## 12. String conversion có encoding và lifetime

`jstring` ↔ UTF representation cần API JNI. Pointer từ `GetStringUTFChars` có lifetime cần release.

Không giữ pointer sau release. Không assume mọi string domain phù hợp modified UTF-8 semantics của JNI API mà không kiểm tra use case.

Với binary data, dùng `ByteArray`/buffer contract rõ thay vì lạm dụng string.

## 13. Array copy vs pinning

JNI API truy cập primitive array có thể copy hoặc pin tùy runtime. Không nên assume pointer luôn trỏ trực tiếp heap object.

Critical sections phải ngắn. Giữ array pinned lâu có thể ảnh hưởng GC/runtime.

Large streaming data nên cân nhắc direct buffers hoặc native-owned memory với contract rõ thay vì copy liên tục qua JNI.

## 14. Direct `ByteBuffer`

Direct buffer có thể cung cấp memory region thuận lợi cho native interoperability, giảm một số copy trong workload phù hợp.

Nhưng zero-copy không tự động đồng nghĩa nhanh hơn. Allocation, ownership, synchronization và cache behavior vẫn cần đo.

Nếu native giữ pointer tới direct buffer, lifetime của buffer phía managed phải đảm bảo đủ lâu.

## 15. Native memory không nằm hoàn toàn trong JVM heap metric

C++ `malloc/new`, mmap, graphics/native buffers có thể tăng process RSS/native heap dù Java heap nhìn bình thường.

OOM diagnosis phải xem:

- managed heap;
- native heap;
- graphics/buffer memory;
- code/mapped files;
- thread stacks;
- shared memory.

Case 09 đã xây process/memory mental model; native layer là lý do quan trọng cần nhìn process-level evidence thay vì chỉ Android Studio Java heap.

## 16. RAII và ownership trong C++

C++ production code nên ưu tiên RAII và smart pointers để resource lifetime gắn object lifetime.

`std::unique_ptr` biểu diễn single ownership. `std::shared_ptr` chỉ dùng khi ownership thật sự shared; dùng mọi nơi có thể tạo cycle và atomic overhead.

JNI handles/file descriptors/mutex/native window cũng nên được wrap trong RAII object khi hợp lý.

Manual `new/delete` rải rác qua callback paths là mùi code mạnh.

## 17. Use-after-free và double free

Managed code thường được bảo vệ khỏi raw memory bugs; C/C++ không. Một callback async giữ raw pointer tới object đã destroy có thể crash random sau vài phút.

Native async API cần explicit ownership:

```text
request owns operation
operation owns callback state
cancel/destroy transitions state
callback checks liveness/generation
```

Không fix use-after-free bằng sleep hoặc null check ngẫu nhiên.

## 18. Race condition native và Kotlin vẫn là cùng một concurrency problem

JNI không tạo automatic synchronization. Nếu Kotlin thread và native worker cùng access native state, cần mutex/atomic/message passing theo invariant rõ.

Một Kotlin `Mutex` không bảo vệ code C++ nếu native truy cập state bên ngoài critical section đó. Lock boundary phải bao trùm đúng shared state ở đúng layer.

## 19. CMake và `externalNativeBuild`

Android Gradle Plugin có thể integrate CMake/NDK build.

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

Version/toolchain thực tế phải theo project baseline, không copy con số sample một cách máy móc.

## 20. Prebuilt `.so` và `jniLibs`

Vendor SDK có thể ship prebuilt libraries trong `src/main/jniLibs/<abi>/` hoặc AAR.

Prebuilt binary là supply-chain artifact. Team cần biết:

- ABI matrix;
- NDK/toolchain origin nếu có thể;
- debug symbols;
- license;
- CVE/update policy;
- 16 KB page compatibility;
- transitive native dependencies.

Một AAR upgrade có thể đổi `.so` mà Gradle dependency diff không làm risk này hiển nhiên.

## 21. 16 KB memory page size là compatibility requirement quan trọng

Android ecosystem đang hỗ trợ device có page size lớn hơn 4 KB. Native shared libraries phải có ELF segment alignment phù hợp để chạy đúng trên device 16 KB page size.

NDK mới hỗ trợ build alignment phù hợp tốt hơn; nhưng prebuilt `.so` cũ vẫn có thể không compatible. Vì vậy project có native dependency phải inventory **tất cả native libraries**, không chỉ code C++ tự build.

Test nên gồm emulator/device configuration hỗ trợ 16 KB page size và inspect bundle/native alignment trong release pipeline.

## 22. NDK version là toolchain dependency, không phải chi tiết local machine

Pin NDK version để local/CI reproducible:

```kotlin
android {
    ndkVersion = "<approved-version>"
}
```

Upgrade NDK có thể thay compiler/linker behavior, libc++ implementation, warning, symbol hoặc binary output. Với native-heavy app, NDK upgrade nên có benchmark/crash/device validation riêng.

## 23. STL và C++ runtime

Modern NDK dùng libc++ cho C++ standard library. Static/shared runtime choice có packaging implications khi nhiều `.so` cùng dùng C++ runtime.

Không trộn prebuilt native libraries có incompatible STL/runtime assumptions mà không verify vendor guidance.

Native dependency graph giống managed dependencies: transitive binary contract có thể gây runtime failure dù link build pass.

## 24. API level trong native code

NDK API availability cũng phụ thuộc Android API level. Compile against symbol mới không có nghĩa device minSdk cũ có symbol runtime đó.

Cần guard API hoặc dynamic lookup phù hợp khi support OS cũ.

Không sử dụng private/non-NDK vendor library như stable public API. Platform restrictions với non-public native libraries đã chặt hơn qua các Android versions.

## 25. File descriptor là bridge mạnh giữa managed và native

Nhiều Android APIs expose file descriptor qua ParcelFileDescriptor. Native code có thể làm việc với fd mà không cần raw filesystem path.

Điều này đặc biệt hữu ích với content URI/SAF nơi “real path” không tồn tại hoặc không nên được truy tìm.

Design đúng:

```text
ContentResolver opens descriptor
→ transfer/dup fd ownership rõ
→ native reads/writes fd
→ close exactly once
```

Ownership fd phải explicit để tránh leak/double close.

## 26. AHardwareBuffer và graphics/media memory

Advanced camera/graphics/ML pipelines có thể dùng hardware buffers để chia memory giữa components/hardware paths hiệu quả hơn.

Đây là high-complexity API. Chỉ dùng khi profiling chứng minh copy/bandwidth là bottleneck và team hiểu synchronization/fence/lifetime.

Một abstraction “zero-copy” sai có thể tạo corruption hoặc GPU/CPU sync stall khó debug.

## 27. Native logging và symbolication

`__android_log_print` hoặc logging wrapper giúp native log, nhưng production crash cần native symbols.

Release pipeline nên archive unstripped symbols hoặc symbol package tương ứng version. Crash address không có symbol gần như vô dụng.

R8 mapping giải Java/Kotlin obfuscation; native symbols giải C/C++ stack. Hai artifact khác nhau.

## 28. Tombstone và native crash

Native crash có signal như `SIGSEGV`, `SIGABRT`, `SIGBUS`. Tombstone/native crash report có register, fault address, stack frames, loaded libraries.

Debug flow:

```text
identify exact build/version/ABI
→ obtain matching symbols
→ symbolize stack
→ inspect faulting thread
→ classify memory/race/assert/linking
→ reproduce with sanitizer if possible
```

Không kết luận “NDK bug” chỉ vì stack có native frame.

## 29. Sanitizers

AddressSanitizer/HWASan hoặc các sanitizer phù hợp có thể phát hiện memory bug như buffer overflow/use-after-free trong test/dev environment.

ThreadSanitizer support/use case tùy platform/toolchain; overhead cao nên không phải production default.

Native-heavy codebase nên có sanitizer strategy trong CI/device testing cho critical libraries.

## 30. Performance: JNI call overhead và batching

JNI crossing có cost. Gọi native function hàng triệu lần với payload nhỏ có thể chậm hơn batch processing.

Thay vì:

```text
for every pixel → JNI call
```

nên cân nhắc:

```text
pass buffer/frame → native processes whole batch → one result
```

Nhưng batch quá lớn tăng latency/memory. Đo workload thật.

## 31. Native thread priority và performance hint

Real-time-ish media/game workload đôi khi cần thread scheduling/performance hint APIs. Đây là platform-level optimization, không phải thứ business app nên dùng mặc định.

Trước khi điều chỉnh priority/hint, đo frame deadline, CPU utilization, thermal throttling và battery impact.

Performance optimization native không tách khỏi device thermal/power policy.

## 32. Native library security

C/C++ tăng attack surface memory-safety. Input từ network/file/media phải được coi untrusted.

Best practices gồm:

- cập nhật third-party native dependencies;
- fuzz parser nếu risk cao;
- validate length/offset;
- tránh unsafe C APIs;
- compile hardening flags theo toolchain defaults/recommendations;
- giảm exposed JNI surface;
- không parse attacker-controlled binary bằng legacy library không maintained.

## 33. Khi nào không nên viết NDK

Không dùng NDK chỉ để:

- “giấu secret” — native binary vẫn reverse-engineer được;
- gọi HTTP nhanh hơn;
- viết business rule thông thường;
- tránh học coroutine;
- micro-optimize trước khi profile.

Managed code thường an toàn, maintainable và portable hơn.

## 34. Boundary design mẫu

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

Production implementation có thể cần direct buffer/resource pool, nhưng idea quan trọng là native detail không leak vào toàn architecture.

Test có thể dùng fake `ImageEngine` mà không load `.so`.

## 35. Release checklist native

Trước release app có native code, verify:

1. ABI support matrix đúng.
2. AAB/APK chứa `.so` expected.
3. 16 KB page-size compatibility nếu applicable.
4. Symbols archive theo release.
5. R8/JNI keep rules đúng.
6. Upgrade trên representative devices.
7. minSdk/native API guards đúng.
8. sanitizer/static analysis cho code critical.
9. native memory/leak benchmark.
10. third-party native library inventory/CVE/license.

## 36. Official references

- Android NDK guides: https://developer.android.com/ndk/guides
- NDK API reference: https://developer.android.com/ndk/reference
- JNI tips: https://developer.android.com/training/articles/perf-jni
- 16 KB page sizes: https://developer.android.com/guide/practices/page-sizes

Native toolchain và platform constraints thay đổi theo Android/NDK release. Luôn kiểm tra documentation của NDK version và device target thực tế khi ship.