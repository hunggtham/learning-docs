# 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 chỉ dẫn thiết kế giao diện người dùng cốt lõi: Lấy người dùng làm trung tâm (`사용자 중심`), Tính khả dụng (`사용성`), Tính thẩm mỹ (`심미성`), và Khả năng khắc phục lỗi (`오류 발생 해결`).
- Khắc sâu các công nghệ giao diện tiên tiến: Giao diện giọng nói (`VUI`) và Giao diện hữu cơ tương tác vật thể (`OUI`).
- Nắm vững chu trình 5 bước phát triển thiết kế cơ sở dữ liệu (`요구조건 분석` -> `개념적 설계` -> `논리적 설계` -> `물리적 설계` -> `구현`) làm cầu nối chuyển giao sang kiến trúc phần mềm.

## 핵심 키워드 (Từ khóa)
- UI 설계 지침 (Chỉ dẫn thiết kế UI: 사용자 중심, 사용성, 심미성, 오류 해결)
- VUI / OUI (Voice / Organic User Interface)
- 사용성 (Tính khả dụng / Usability: ISO 9241)
- 데이터베이스 설계 5단계 (5 bước thiết kế CSDL: 요구 -> 개념 -> 논리 -> 물리 -> 구현)
- 아키텍처 전이 (Chuyển tiếp kiến trúc / Architecture Transition)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([1. 사용자 인터페이스](20-bai-hoc.md)):** Sau khi xem xét các cử chỉ di động và 4 công cụ thiết kế UI (Wireframe, Mockup, Storyboard, Prototype), bài này đúc kết thành các chỉ dẫn thiết kế chuyên sâu.
- **Tiếp nối sang cụm sau ([5. 요구공학](22-bai-hoc.md)):** Chuyển từ tầng giao diện sang kỹ nghệ yêu cầu nâng cao và các mẫu kiến trúc phần mềm (Software Architecture Patterns).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ 4 tiêu chí chỉ dẫn thiết kế UI và câu thần chú 5 bước thiết kế CSDL: **Yêu - Khái - Logic - Vật - Cụ**.
- Đọc TẦNG B để hiểu tầm quan trọng của việc thiết kế phòng ngừa và thông báo lỗi thân thiện cho người dùng.

---

## 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 사용자 인터페이스 설계 지침 (4 chỉ dẫn thiết kế UI cốt lõi):**
  1. `사용자 중심 (User-Centric - Lấy người dùng làm trung tâm)`: Thiết kế phải dựa trên sự thấu hiểu sâu sắc về thói quen, tâm lý và nhu cầu thực tế của người sử dụng; tránh áp đặt tư duy kỹ thuật của lập trình viên lên người dùng.
  2. `사용성 (Usability - Tính khả dụng)`: **Là yếu tố cần được ưu tiên hàng đầu (`가장 우선적으로 고려`)**. Hệ thống phải dễ học, dễ nhớ, cho phép hoàn thành công việc nhanh chóng với sự hài lòng cao.
  3. `심미성 (Aesthetics - Tính thẩm mỹ)`: Bố trí các thành phần đồ họa hài hòa, màu sắc chuẩn mực, tạo cảm giác chuyên nghiệp, không gây rối mắt hoặc mỏi mắt khi làm việc lâu.
  4. `오류 발생 해결 (Error Recovery - Khắc phục sự cố/lỗi)`: Khi người dùng thao tác sai, hệ thống phải phát thông báo lỗi rõ ràng, mang tính xây dựng, chỉ dẫn cách khắc phục cụ thể và bảo vệ dữ liệu đã nhập, tránh mất mát thông tin.
- **2. Các giao diện thế hệ mới:**
  - `VUI (Voice User Interface)`: Điều khiển và tương tác với thiết bị hoàn toàn bằng giọng nói con người (Bixby, Google Assistant, Siri).
  - `OUI (Organic User Interface)`: Tương tác người - máy trên nền tảng các vật thể vật lý thực, tận dụng màn hình dẻo uốn cong (Flexible display), thiết bị gập, vật liệu co giãn và cảm biến môi trường.
- **3. Cầu nối sang Kiến trúc dữ liệu - 5 bước thiết kế CSDL chuẩn:**
  1. `요구조건 분석 (Phân tích yêu cầu)`: Xác định rõ người dùng cần lưu trữ và truy vấn những dữ liệu gì.
  2. `개념적 설계 (Thiết kế khái niệm)`: Mô hình hóa thế giới thực thành các khái niệm trừu tượng độc lập DBMS -> Sản phẩm cốt lõi là **Sơ đồ E-R (`E-R 다이어그램`)**.
  3. `논리적 설계 (Thiết kế logic)`: Ánh xạ sơ đồ E-R thành các bảng dữ liệu quan hệ (Mapping), chuẩn hóa dữ liệu (`정규화`), xác định khóa chính/khóa ngoại.
  4. `물리적 설계 (Thiết kế vật lý)`: Thiết kế cấu trúc lưu trữ trên ổ đĩa vật lý (B-Tree Index, Partition, Clustering) nhằm tối ưu hóa hiệu năng truy xuất và thời gian đáp ứng.
  5. `구현 (Hiện thực / Cài đặt)`: Sử dụng câu lệnh DDL (`CREATE TABLE`) để tạo cấu trúc cơ sở dữ liệu thực sự trong DBMS mục tiêu.
  - 💡 **Mẹo nhớ 5 bước thiết kế CSDL:** **Y-K-L-V-C** (Yêu cầu -> Khái niệm -> Logic -> Vật lý -> Cài đặt).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Yếu tố nào cần được ưu tiên hàng đầu khi thiết kế giao diện UI?"* -> **사용성 (Tính khả dụng / Usability)**.
  - **Bẫy 2 (Thứ tự thiết kế CSDL):** Thiết kế vật lý diễn ra trước hay sau thiết kế logic? -> **Sau thiết kế logic (Khái niệm -> Logic -> Vật lý)**.
  - **Bẫy 3:** *"Thông báo lỗi trong UI nên hiển thị mã lỗi nội bộ hệ thống như 'Error 0x80004005: NullPointer'?"* -> **Sai**. Thông báo lỗi phải thân thiện, chỉ rõ nguyên nhân và hướng dẫn user cách xử lý (오류 발생 해결).
- **한 문장 설명 (Câu chốt ghi nhớ):** "Thiết kế UI lấy người dùng làm trung tâm, ưu tiên tính khả dụng; thiết kế CSDL chuẩn qua 5 bước Yêu - Khái - Logic - Vật - Cài đặt".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tiêu chuẩn tính khả dụng theo ISO 9241-11:**
  - Tiêu chuẩn quốc tế định nghĩa tính khả dụng (Usability) qua 3 thước đo:
    1. `효과성 (Effectiveness)`: Mức độ chính xác và trọn vẹn mà người dùng đạt được mục tiêu.
    2. `효율성 (Efficiency)`: Lượng tài nguyên và thời gian tiêu tốn để đạt được mục tiêu đó.
    3. `만족도 (Satisfaction)`: Cảm giác thoải mái và tích cực khi trải nghiệm sản phẩm.

### 복습 체크리스트
- [ ] Nhớ 4 chỉ dẫn thiết kế UI: 사용자 중심, 사용성, 심미성, 오류 발생 해결.
- [ ] Khẳng định được 사용성 (Usability) là tiêu chí ưu tiên số một trong thiết kế UI.
- [ ] Phân biệt được đặc trưng của VUI và OUI.
- [ ] Đọc đúng thứ tự 5 bước thiết kế cơ sở dữ liệu (요구 -> 개념 -> 논리 -> 물리 -> 구현).
