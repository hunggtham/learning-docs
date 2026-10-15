# 097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và ý nghĩa của Môi trường Phát triển Tích hợp (IDE - Integrated Development Environment): công cụ phần mềm cung cấp gói tiện ích toàn diện hỗ trợ lập trình viên xây dựng ứng dụng trong một giao diện hợp nhất.
- Ghi nhớ 4 chức năng cốt lõi của một hệ thống IDE tiêu chuẩn: Soạn thảo mã (코딩 - Coding), Biên dịch (컴파일 - Compile), Gỡ lỗi (디버깅 - Debugging), và Đóng gói triển khai (배포 - Deployment).
- Nhớ tên, nhà phát triển và nền tảng hỗ trợ của các IDE thông dụng xuất hiện trong đề thi: Eclipse, IntelliJ IDEA, Visual Studio, Xcode, và Android Studio.

## 핵심 키워드 (Từ khóa)
- 통합 개발 환경 (IDE - Integrated Development Environment)
- 코딩 (Coding / 구문 강조, 코드 자동 완성)
- 컴파일 (Compile / 빌드 자동화)
- 디버깅 (Debugging / 중단점 Breakpoint, 변수 감시)
- 배포 (Deployment / 패키징)
- 이클립스 (Eclipse / IBM, Java)
- 인텔리제이 (IntelliJ IDEA / JetBrains, Java/Kotlin)
- 비주얼 스튜디오 (Visual Studio / Microsoft, C#/.NET)
- 엑스코드 (Xcode / Apple, Swift/Objective-C)
- 안드로이드 스튜디오 (Android Studio / Google, Kotlin/Java)

## 선행·연결 개념 (Kiến thức liên kết)
- [96-bai-hoc.md](96-bai-hoc.md): Lập trình SQL thủ tục và kỹ thuật gỡ lỗi.
- [98-bai-hoc.md](98-bai-hoc.md): Công cụ xây dựng và công cụ hợp tác phát triển phần mềm.
- [38-bai-hoc.md](38-bai-hoc.md): Bốn trụ cột của môi trường IDE và quy trình quản lý cấu hình.

## 읽는 방법 (Cách đọc)
- Phân biệt các chức năng trụ cột:
  - **Coding:** Bộ soạn thảo thông minh (IntelliSense) hỗ trợ highlight cú pháp và gợi ý hàm.
  - **Compile:** Tự động chuyển đổi mã nguồn thành tệp thực thi nhị phân hoặc bytecode.
  - **Debugging:** Cho phép đặt điểm ngắt (Breakpoint), chạy từng dòng lệnh (Step Into/Over) để soi giá trị biến trong bộ nhớ.
  - **Deployment:** Hỗ trợ xuất tệp cài đặt, đóng gói thư viện (JAR, WAR, APK, EXE) và đẩy lên máy chủ.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bốn chức năng cốt lõi của môi trường phát triển tích hợp (IDE 4대 기능):**

| Chức năng | Tên tiếng Hàn & Anh | Trách nhiệm và hành vi của công cụ |
| :--- | :--- | :--- |
| **1. 코딩** | **Coding (Soạn thảo mã)** | Cung cấp trình soạn thảo mã nguồn có tô màu cú pháp (Syntax Highlighting), tự động thụt lề, kiểm tra lỗi cú pháp thời gian thực, và gợi ý hoàn thành mã tự động (Auto-completion) |
| **2. 컴파일** | **Compile (Biên dịch)** | Tự động dịch mã nguồn người viết thành mã máy hoặc Bytecode trung gian; tích hợp trình liên kết (Linker) để tạo tệp thực thi |
| **3. 디버깅** | **Debugging (Gỡ lỗi)** | Cho phép đặt điểm dừng (**중단점 - Breakpoint**), theo dõi giá trị biến (Watch), thực thi từng bước (Step by Step) nhằm tìm và sửa các lỗi logic khi chạy |
| **4. 배포** | **Deployment (Triển khai)** | Tự động hóa quá trình đóng gói phần mềm thành gói phân phối (Package) và tải lên máy chủ lưu trữ hoặc chợ ứng dụng |

- **Bảng tổng hợp các IDE tiêu biểu chuẩn đề thi:**

| Tên IDE | Nhà phát triển | Ngôn ngữ / Nền tảng chuyên dụng | Đặc điểm nổi bật |
| :--- | :--- | :--- | :--- |
| **Eclipse (이클립스)** | IBM khởi xướng / Eclipse Foundation | Đa nền tảng (Java chủ đạo, C++, PHP) | Mã nguồn mở, kiến trúc mở rộng mạnh mẽ dựa trên hệ thống Plugin đồ sộ |
| **IntelliJ IDEA** | JetBrains | Đa nền tảng (Java, Kotlin, Groovy) | Trí tuệ phân tích mã thông minh, công cụ chuẩn của lập trình viên Java/Spring hiện đại |
| **Visual Studio** | Microsoft | Windows (C#, C++, Visual Basic, .NET) | Hệ sinh thái hoàn chỉnh, công cụ kéo thả GUI và tối ưu hóa hệ thống Windows mạnh mẽ |
| **Xcode (엑스코드)** | Apple | macOS, iOS, iPadOS (Swift, Objective-C) | Môi trường độc quyền để phát triển ứng dụng cho toàn bộ thiết bị của Apple |
| **Android Studio** | Google (dựa trên IntelliJ) | Android OS (Kotlin, Java) | IDE tiêu chuẩn chính thức để lập trình và giả lập ứng dụng di động Android |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tiêu chuẩn lựa chọn IDE cho dự án phần mềm:**
  - Cần đánh giá dựa trên: Ngôn ngữ lập trình chính, Mức độ hỗ trợ hệ thống quản lý mã nguồn (Git/SVN), Khả năng tích hợp công cụ kiểm thử (JUnit) và Công cụ quản lý phụ thuộc (Gradle/Maven), cùng với mức độ tiêu tốn tài nguyên phần cứng (RAM/CPU) của máy trạm lập trình viên.

### 복습 체크리스트
- [ ] Kể tên 4 chức năng cốt lõi của IDE: 코딩 (Coding), 컴파일 (Compile), 디버깅 (Debugging), 배포 (Deployment).
- [ ] Nhớ Eclipse do IBM sáng lập chuyên Java mã nguồn mở.
- [ ] Nhớ Xcode độc quyền của Apple, Android Studio của Google.
- [ ] Nhớ Visual Studio của Microsoft cho môi trường .NET / Windows.
