# 클린 코드와 리팩토링 및 정적 분석 (Mã nguồn sạch, Tái cấu trúc và Phân tích tĩnh)

## 학습 목표
- Nắm vững định nghĩa Clean Code (`클린 코드`) và 5 nguyên tắc vàng chuẩn thi: Tính dễ đọc (`가독성`), Tính đơn giản (`단순성`), Loại trừ phụ thuộc (`의존성 배제`), Trùng lặp tối thiểu (`중복 최소화` - DRY), Tính trừu tượng hóa (`추상화`).
- Phân biệt 3 dạng mã nguồn có vấn đề: Mã ngoài hành tinh (`외계인 코드 / Alien Code` - tác giả đã nghỉ việc, không có tài liệu), Mã mì sợi (`스파게티 코드 / Spaghetti Code` - luồng rối rắm, lạm dụng goto), Mã di sản (`레거시 코드 / Legacy Code` - mã cũ đang vận hành, thiếu unit test).
- Nắm vững định nghĩa chuẩn thi của Refactoring (`리팩토링`): cải thiện cấu trúc bên trong nhằm nâng cao khả năng bảo trì (`유지보수성 향상`), tuyệt đối không làm thay đổi hành vi bên ngoài (`외부 동작 변경 없음`).
- Phân biệt Phân tích tĩnh (`정적 분석 / Static Analysis` - không chạy mã nguồn) và Phân tích động (`동적 분석 / Dynamic Analysis` - bắt buộc chạy mã nguồn).
- Nhận diện các công cụ phân tích tĩnh tiêu biểu trong đề thi: PMD (tìm biến không dùng `미사용 변수`), Checkstyle (chuẩn coding standard), Cppcheck (C/C++), SonarQube (nền tảng quản lý chất lượng toàn diện).

## 핵심 키워드
- 클린 코드 5대 원칙 (가독성 Readability, 단순성 Simplicity, 의존성 배제 Loose Coupling, 중복 최소화 DRY, 추상화 Abstraction)
- 외계인 코드 (Alien Code / 개발자 부재, 참고 문서 없음)
- 스파게티 코드 (Spaghetti Code / goto 남용, 복잡한 제어 흐름)
- 레거시 코드 (Legacy Code / 테스트 부재, 구버전 소프트웨어)
- 리팩토링 (Refactoring / 유지보수성 향상, 외부 동작 불변)
- 정적 분석 vs 동적 분석 (Static - 코드 미실행 vs Dynamic - 프로그램 실행 중)
- 정적 분석 도구 (PMD 미사용 변수, Checkstyle 코딩 표준, SonarQube 통합 관리)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [17-v-model-kiem-thu-tich-hop-va-oracle.md](17-v-model-kiem-thu-tich-hop-va-oracle.md), chúng ta đã khảo sát các cấp độ kiểm thử theo mô hình V-Model và cơ chế thẩm định bằng Test Oracle.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc nâng cao chất lượng nội tại của mã nguồn, triệt tiêu nợ kỹ thuật bằng 5 nguyên tắc Clean Code, kỹ thuật tái cấu trúc Refactoring an toàn và phát hiện lỗi sớm bằng các công cụ phân tích tĩnh/động.
- **Dùng đi đâu (Forward Handoff):** Sau khi hoàn thiện tầng mã nguồn logic, bài học tiếp theo [19-phan-cap-bo-nho-va-phan-cung-lien-ket.md](19-phan-cap-bo-nho-va-phan-cung-lien-ket.md) sẽ đưa ta xuống tầng vật lý phần cứng để tìm hiểu về phân cấp bộ nhớ, Cache locality và kiến trúc máy tính theo Flynn.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng 5 nguyên tắc Clean Code, bảng phân biệt Alien vs Spaghetti vs Legacy Code, bảng so sánh Static vs Dynamic Analysis, và nhận diện chính xác công cụ PMD/SonarQube.
- Đọc TẦNG B để hiểu sâu các kỹ thuật Refactoring (Extract Method, Rename), chi tiết phân tích động (Valgrind, Profiling) và bẫy trắc nghiệm thực chiến.

---

## 클린 코드와 리팩토링 및 정적 분석

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tổng quan về Clean Code (클린 코드) và 5 nguyên tắc vàng
- **Định nghĩa:**
  - [한국어]: **클린 코드는 잘 작성되어 가독성이 높고, 단순하며, 의존성을 줄이고, 중복을 최소화하여 유지보수가 용이한 코드를 의미한다.**
  - [Tiếng Việt]: Clean Code là mã nguồn có cấu trúc rõ ràng, dễ đọc, mạch lạc, dễ kiểm thử và mở rộng, giúp bất kỳ lập trình viên nào trong nhóm cũng có thể nắm bắt và bảo trì thuận lợi.

```
[1. 가독성 (Dễ đọc)] ──────► [2. 단순성 (Đơn giản)] ──────► [3. 의존성 배제 (Giảm phụ thuộc)]
                                                                      │
                      [5. 추상화 (Trừu tượng hóa)] ◄────── [4. 중복 최소화 (Tránh trùng lặp)]
```

#### Bảng 5 nguyên tắc viết Clean Code chuẩn thi (클린 코드 5대 원칙)
| Nguyên tắc | Tên tiếng Hàn & Anh | Mục tiêu định hướng kỹ thuật | Biểu hiện vi phạm (Code Smell) |
| :--- | :--- | :--- | :--- |
| **Tính dễ đọc** | **가독성 (Readability)** | Bất kỳ ai đọc vào cũng hiểu ngay mục đích và hành vi; tên biến/hàm biểu cảm cao, thụt lề chuẩn | Đặt tên tắt tối nghĩa (`int a, b;`), viết nhiều câu lệnh trên một dòng, định dạng lộn xộn |
| **Tính đơn giản** | **단순성 (Simplicity)** | Tuân thủ triết lý K.I.S.S (*Keep It Simple*); mỗi hàm chỉ giải quyết duy nhất một công việc (**단일 책임**) | Hàm quá dài hàng trăm dòng, lồng ghép quá nhiều vòng lặp `for`/`if` phức tạp |
| **Loại trừ phụ thuộc** | **의존성 배제 (Loose Coupling)** | Giảm thiểu gắn kết cứng giữa các module/lớp; thay đổi ở một lớp không làm vỡ lớp khác | Phụ thuộc trực tiếp vào triển khai chi tiết thay vì thông qua Interface |
| **Trùng lặp tối thiểu** | **중복 최소화 (DRY - Don't Repeat)** | Tuyệt đối không sao chép - dán (Copy-Paste) logic; gom các đoạn mã lặp lại thành hàm/lớp chung | Cùng một đoạn thuật toán xác thực xuất hiện rải rác ở nhiều tệp mã nguồn khác nhau |
| **Tính trừu tượng hóa** | **추상화 (Abstraction)** | Ẩn giấu chi tiết cài đặt phức tạp đằng sau các giao diện (Interface/API) cấp cao | Phơi bày toàn bộ cấu trúc dữ liệu nội bộ, phá vỡ nguyên lý che giấu thông tin |

#### 2. Phân biệt 3 dạng mã nguồn có vấn đề: Alien vs Spaghetti vs Legacy
| Thuật ngữ | Tên tiếng Hàn & Anh | Bản chất nguyên nhân hình thành | Hệ quả trong công tác bảo trì |
| :--- | :--- | :--- | :--- |
| **Mã ngoài hành tinh** | **외계인 코드 (Alien Code)** | Mã nguồn cũ, **tác giả đã nghỉ việc (개발자 부재)** và **hoàn toàn không có tài liệu kỹ thuật (참고 문서 없음)** | Người tiếp quản không thể hiểu nổi logic; chỉnh sửa một dòng có thể làm đổ vỡ toàn bộ |
| **Mã mì sợi** | **스파게티 코드 (Spaghetti Code)** | Cấu trúc luồng điều khiển cực kỳ rối rắm, lạm dụng lệnh nhảy tùy tiện (`goto`) hoặc phụ thuộc chéo | Cực kỳ khó gỡ lỗi (Debugging), khó theo dõi luồng dữ liệu, vi phạm lập trình cấu trúc |
| **Mã di sản** | **레거시 코드 (Legacy Code)** | Mã nguồn cũ được viết bằng công nghệ lỗi thời nhưng hiện vẫn đang vận hành sinh doanh thu | Thiếu các bộ kiểm thử tự động (Unit Test), tiềm ẩn rủi ro cao khi phải tích hợp công nghệ mới |

#### 3. Tái cấu trúc mã nguồn (리팩토링 - Refactoring)
- **Định nghĩa chuẩn thi:**
  - [한국어]: **리팩토링은 소프트웨어의 유지보수성을 향상시키기 위해 외부 동작을 변경하지 않고 내부 구조를 개선하는 활동이다.**
  - [Tiếng Việt]: Refactoring là quá trình tái cấu trúc lại mã nguồn phần mềm nhằm nâng cao khả năng bảo trì, cải thiện tính dễ đọc và loại bỏ các mùi hôi của mã (Code Smells), nhưng **tuyệt đối KHÔNG làm thay đổi hành vi bên ngoài của chương trình**.
- **Kỹ thuật tiêu biểu:**
  - *Extract Method (Trích xuất phương thức):* Tách một đoạn mã dài, phức tạp thành một hàm con độc lập có tên gọi rõ nghĩa.
  - *Rename Variable/Method (Đổi tên có ý nghĩa):* Đổi tên biến và hàm cho đúng với trách nhiệm thực tế.
  - *Replace Temp with Query:* Thay thế các biến tạm tính toán trung gian bằng một hàm truy vấn.

#### 4. Sơ đồ phân nhánh và Bảng so sánh Phân tích tĩnh vs Phân tích động
```
                              ┌──────────────────────────────────────────────┐
                              │     ĐÁNH GIÁ CHẤT LƯỢNG MÃ NGUỒN             │
                              └──────────────────────┬───────────────────────┘
                                                     │
                         ┌───────────────────────────┴───────────────────────────┐
                         ▼                                                       ▼
            ┌───────────────────────────┐                           ┌───────────────────────────┐
            │  정적 분석 (Static)        │                           │  동적 분석 (Dynamic)       │
            │  - KHÔNG CHẠY mã nguồn    │                           │  - BẮT BUỘC CHẠY mã nguồn │
            │  - Tìm vi phạm quy chuẩn, │                           │  - Đo rò rỉ bộ nhớ,       │
            │    biến thừa, AST syntax  │                           │    profiling CPU, coverage│
            └────────────┬──────────────┘                           └────────────┬──────────────┘
                         │                                                       │
                 PMD, Checkstyle, SonarQube                              Valgrind, Profiler
```

| Tiêu chí | 정적 분석 도구 (Static Analysis) | 동적 분석 도구 (Dynamic Analysis) |
| :--- | :--- | :--- |
| **Trạng thái thực thi** | **Không chạy chương trình (코드를 실행하지 않음)** | **Bắt buộc phải chạy chương trình (프로그램 실행 중)** |
| **Đối tượng phân tích** | Tệp mã nguồn (Source Code), cây cú pháp trừu tượng (AST) | Tiến trình thực thi (Process), bộ nhớ RAM, hành vi I/O |
| **Mục tiêu phát hiện** | Biến khai báo không dùng / Khối lệnh rỗng / Vi phạm chuẩn coding / Nguy cơ tràn bộ đệm | Rò rỉ bộ nhớ (메모리 누수) / Deadlock đa luồng / Độ bao phủ Code Coverage / Profiling CPU |
| **Thời điểm áp dụng** | Giai đoạn viết mã (Coding) hoặc tiền biên dịch (Pre-commit) | Giai đoạn kiểm thử đơn vị, kiểm thử tích hợp và kiểm thử tải |

#### 5. Các công cụ phân tích tĩnh tiêu biểu trong đề thi
| Tên công cụ | Nền tảng / Ngôn ngữ | Đặc điểm kỹ thuật nhận diện đề thi |
| :--- | :--- | :--- |
| **PMD** | Java | Quét mã Java phát hiện: **biến không sử dụng (미사용 변수)**, khối `catch` rỗng, phương thức chưa hoàn thiện |
| **Checkstyle** | Java | Kiểm tra việc tuân thủ các quy tắc chuẩn mực viết mã (**코딩 표준 준수 여부**): thụt lề, đặt tên, khoảng trắng |
| **Cppcheck** | C / C++ | Phân tích tĩnh mã C/C++: phát hiện lỗi con trỏ null, tràn bộ đệm ngoài giới hạn mảng, rò rỉ tài nguyên |
| **SonarQube** | Đa ngôn ngữ | Nền tảng quản lý chất lượng mã nguồn tập trung: theo dõi nợ kỹ thuật, lỗi bảo mật và độ bao phủ test |

#### 6. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Nhận diện Alien Code:** Câu hỏi nhắc đến *"Một đoạn mã nguồn cũ, người phát triển ban đầu đã rời đi (**개발자 부재**), tài liệu tham khảo hoàn toàn không tồn tại (**참고 문서 없음**)"* $\rightarrow$ Đáp án chắc chắn là **외계인 코드 (Alien Code)**.
- **Bẫy 2: Bản chất Refactoring:** Câu hỏi khẳng định *"Refactoring là quá trình viết lại mã nguồn để bổ sung thêm các tính năng nghiệp vụ mới"* $\rightarrow$ **SAI**. Refactoring chỉ tái cấu trúc nội bộ nhằm tăng khả năng bảo trì (**유지보수성**), **tuyệt đối không làm thay đổi hành vi bên ngoài (외부 동작 불변)**.
- **Bẫy 3: Phân biệt Static vs Dynamic:** Công cụ quét mã nguồn mà **không chạy chương trình** $\rightarrow$ **정적 분석 도구 (Static)**. Công cụ đo rò rỉ bộ nhớ khi chương trình đang chạy $\rightarrow$ **동적 분석 도구 (Dynamic)**.
- **Bẫy 4: Nhận diện PMD:** Công cụ phân tích tĩnh Java chuyên tìm biến khai báo không dùng (**미사용 변수**) $\rightarrow$ **PMD**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Chi tiết các mùi hôi mã nguồn (Code Smells)
- **Long Method:** Hàm quá dài, chứa quá nhiều nhánh rẽ $\rightarrow$ Áp dụng *Extract Method*.
- **Large Class (God Class):** Một lớp nắm giữ quá nhiều trách nhiệm, vi phạm Single Responsibility Principle $\rightarrow$ Tách thành nhiều lớp chuyên biệt.
- **Data Clumps:** Các biến luôn đi cùng nhau từng nhóm 3-4 biến (ví dụ: `startDate, endDate, reason`) $\rightarrow$ Gom thành một Value Object độc lập.

#### 2. Kỹ thuật phân tích động (Dynamic Analysis)
- **Memory Leak Detection (Valgrind):** Theo dõi việc cấp phát (`malloc`/`new`) và giải phóng (`free`/`delete`) vùng nhớ heap để phát hiện các con trỏ bị mất tham chiếu.
- **Thread Profiling:** Bắt giữ các hiện tượng nghẽn luồng (Thread Deadlock, Race Condition) khi nhiều luồng truy cập đồng thời vào vùng nhớ tranh chấp.

---

### 복습 체크리스트
- [ ] Nêu định nghĩa Clean Code và 5 nguyên tắc vàng: 가독성, 단순성, 의존성 배제, 중복 최소화, 추상화.
- [ ] Phân biệt rõ 3 dạng mã có vấn đề: Alien Code (vắng tác giả, thiếu tài liệu), Spaghetti Code (rối như mì), Legacy Code.
- [ ] Nhớ bản chất sống còn của Refactoring: Tăng tính bảo trì, tuyệt đối không thay đổi hành vi bên ngoài.
- [ ] Phân biệt Static Analysis (không chạy code) và Dynamic Analysis (bắt buộc chạy code).
- [ ] Nhớ PMD chuyên tìm lỗi biến không dùng (미사용 변수) trong Java.
- [ ] Nhớ Checkstyle chuyên kiểm tra tuân thủ chuẩn viết mã (코딩 표준 준수).
- [ ] Kể tên công cụ quản lý chất lượng tập trung đa ngôn ngữ: SonarQube.
