# 화면 설계 및 UI·UX·HCI (Thiết kế Giao diện người dùng và Tương tác UI/UX/HCI)

## 학습 목표 (Mục tiêu)
- Nắm vững phân loại 4 loại hình giao diện người dùng (`CLI, GUI, NUI, OUI`) và hệ thống các cử chỉ cảm ứng trên thiết bị di động (`모바일 제스처`).
- Thuộc nằm lòng 4 nguyên tắc vàng trong thiết kế giao diện người dùng (`UI 4대 기본 원칙: 직관성, 유효성, 학습성, 유연성`).
- Phân biệt chính xác chuỗi sản phẩm thiết kế giao diện theo mức độ chi tiết và tương tác: Khung dây (`와이어프레임`), Bản dựng tĩnh (`목업`), Kịch bản thao tác (`스토리보드`), và Bản mẫu tương tác (`프로토타입`).
- Phân tích sâu sắc mối quan hệ đa tầng giữa Tương tác người - máy tính (`HCI`), Trải nghiệm người dùng (`UX`), và Giao diện người dùng (`UI`); làm chủ tiêu chuẩn tính khả dụng ISO 9241.

## 핵심 키워드 (Từ khóa)
- 사용자 인터페이스 (User Interface - UI: CLI, GUI, NUI, OUI)
- 모바일 제스처 (Cử chỉ cảm ứng di động: Tap, Double Tap, Drag, Pan, Flick, Pinch)
- UI 4대 기본 원칙 (4 nguyên tắc vàng UI: 직관성 - Intuitiveness, 유효성 - Effectiveness, 학습성 - Learnability, 유연성 - Flexibility)
- 와이어프레임 (Khung xương layout / Wireframe / 레이아웃 뼈대)
- 목업 (Bản dựng đồ họa tĩnh / Mockup / 정적 모형 / 시각 디자인)
- 스토리보드 (Kịch bản thao tác / Storyboard / 와이어프레임 + 디스크립션)
- 프로토타입 (Bản mẫu tương tác / Prototype / 인터랙션 동작 검증)
- HCI vs UX vs UI (인간-컴퓨터 상호작용 vs 사용자 경험 vs 사용자 인터페이스)
- 사용성 (Tính khả dụng / Usability / ISO 9241: 유효성, 효율성, 만족도)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ [04-mo-hinh-hoa-uml-va-bieu-do.md](04-mo-hinh-hoa-uml-va-bieu-do.md), sau khi biểu đồ trường hợp sử dụng (Use Case Diagram) xác định rõ các tác nhân bên ngoài tương tác với hệ thống như thế nào, đội dự án cần cụ thể hóa các Use Case đó thành các màn hình giao diện trực quan cho người dùng cuối.
- **Đang giải quyết gì (Current Problem):** Bài học này thuộc phạm vi trọng tâm của **Chương 2: 화면 설계 (Thiết kế màn hình)** trong chuẩn đề thi 정보처리기사, giải quyết bài toán làm thế nào để xây dựng giao diện trực quan, dễ học, giảm thiểu tối đa sai sót thao tác của người dùng và chuyển giao từ bản phác thảo khung xương sang bản mẫu chạy thử nghiệm.
- **Dùng đi đâu (Forward Handoff):** Sau khi giao diện màn hình và luồng tương tác của người dùng được xác định, kiến thức bàn giao sang **Chương 3: 애플리케이션 설계 (Thiết kế ứng dụng)** bắt đầu từ bài [06-thiet-ke-kien-truc-va-chat-luong-phan-mem.md](06-thiet-ke-kien-truc-va-chat-luong-phan-mem.md) để thiết kế kiến trúc phần mềm tổng thể bên dưới màn hình giao diện.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc nằm lòng 4 nguyên tắc UI bằng câu thần chú "Trực - Hiệu - Học - Hoạt" (`직 - 유 - 학 - 유`); thứ tự phân cấp 4 sản phẩm thiết kế màn hình; và bảng so sánh 3 khái niệm HCI - UX - UI.
- Đọc TẦNG B để hiểu sâu tiêu chuẩn khả dụng ISO 9241 và các nguyên tắc thiết kế giao diện tiếp cận bình đẳng (Web Accessibility Guidelines).

---

## 화면 설계 및 UI·UX·HCI

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Phân loại các dạng Giao diện người dùng (UI Types)
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `사용자 인터페이스(UI)는 사용자와 시스템 간의 상호작용이 원활하게 이루어지도록 돕는 장치나 소프트웨어를 의미하며, CLI, GUI, NUI, OUI로 구분된다.`
  - [Tiếng Việt]: Giao diện người dùng (UI) là cầu nối vật lý hoặc phần mềm cho phép con người tương tác, điều khiển và nhận phản hồi từ hệ thống máy tính.
- **4 Loại hình giao diện qua các thời kỳ:**
  1. `CLI (Command Line Interface — Giao diện dòng lệnh)`: Người dùng ra lệnh bằng các dòng văn bản (Text Commands) qua bàn phím (ví dụ: Linux Terminal, DOS). Đòi hỏi phải nhớ lệnh.
  2. `GUI (Graphical User Interface — Giao diện đồ họa)`: Người dùng thao tác với các phần tử đồ họa trực quan như Cửa sổ (Window), Biểu tượng (Icon), Menu, Con trỏ chuột (Mouse pointer). Dễ dùng, phổ biến trên Windows, macOS.
  3. `NUI (Natural User Interface — Giao diện tự nhiên)`: Người dùng điều khiển máy tính bằng các hành vi tự nhiên của con người như Giọng nói (Voice), Cử chỉ cơ thể (Body Gesture), Ánh mắt, Chạm đa điểm (Multi-touch) (ví dụ: Siri, Apple Vision Pro, Microsoft Kinect).
  4. `OUI (Organic User Interface — Giao diện hữu cơ)`: Giao diện linh hoạt biến đổi theo hình thái vật lý của vật liệu trong thế giới thực; màn hình có thể uốn cong, gập lại, co giãn (ví dụ: Màn hình điện thoại gập dẻo Foldable, thiết bị đeo uốn dẻo).

- **Hệ thống Cử chỉ cảm ứng trên thiết bị di động (Mobile Touch Gestures):**
  - `Tap (탭)`: Chạm nhẹ ngón tay vào màn hình rồi nhấc lên ngay (tương đương Click chuột).
  - `Double Tap (더블 탭)`: Chạm nhanh 2 lần liên tiếp (thường dùng để phóng to/thu nhỏ văn bản, hình ảnh).
  - `Drag (드래그)`: Chạm ngón tay, giữ và kéo trượt đối tượng sang vị trí khác.
  - `Pan (팬)`: Chạm ngón tay và di chuyển liên tục để cuộn hoặc di dời góc nhìn bản đồ/trang web mà không làm mất điểm chạm.
  - `Flick (플릭)`: Vuốt lướt ngón tay thật nhanh rồi thả tay ra (dùng để cuộn lướt nhanh danh sách dài hoặc chuyển trang sách).
  - `Pinch (핀치)`: Sử dụng 2 ngón tay chạm vào màn hình rồi chụm lại (Pinch-in để thu nhỏ) hoặc mở rộng ra (Pinch-out để phóng to hình ảnh).

---

#### 2. 4 Nguyên tắc vàng trong Thiết kế Giao diện người dùng (UI 4대 원칙)

| Nguyên tắc | Tên tiếng Hàn & Tiếng Anh | Định nghĩa chuẩn xác đề thi |
|:---|:---|:---|
| **Tính trực quan** | `직관성 (Intuitiveness)` | **[Hàn/Anh]:** `누구나 쉽게 이해하고 사용할 수 있어야 한다.` — **[Tiếng Việt]:** Người dùng nhìn vào là **hiểu ngay cách sử dụng một cách tự nhiên** mà không cần phải đọc tài liệu hướng dẫn dày đặc hay qua đào tạo phức tạp. |
| **Tính hữu hiệu** | `유효성 (Effectiveness)` | **[Hàn/Anh]:** `사용자의 목적을 정확하고 완전하게 달성할 수 있어야 한다.` — **[Tiếng Việt]:** Giúp người dùng **đạt được chính xác và trọn vẹn mục đích nghiệp vụ** của mình mà không gặp phải rào cản hay lỗi sai hệ thống. |
| **Tính dễ học** | `학습성 (Learnability)` | **[Hàn/Anh]:** `누구나 쉽게 배우고 익힐 수 있어야 한다.` — **[Tiếng Việt]:** Bất kỳ ai cũng có thể **dễ dàng học và thuần thục cách thao tác trong thời gian ngắn**, đồng thời duy trì được trí nhớ thao tác sau một thời gian dài không sử dụng. |
| **Tính linh hoạt** | `유연성 (Flexibility)` | **[Hàn/Anh]:** `사용자의 요구사항을 최대한 수용하며 오류를 방지하고 제어할 수 있어야 한다.` — **[Tiếng Việt]:** Có khả năng **thích ứng linh hoạt với nhiều đối tượng người dùng** (từ người mới bắt đầu đến chuyên gia qua hệ thống phím tắt), đồng thời có cơ chế bao dung và xử lý lỗi mềm dẻo (Undo/Redo). |

---

#### 3. Chuỗi 4 Sản phẩm thiết kế màn hình (UI Design Artifacts)
Đề thi trắc nghiệm luôn kiểm tra khả năng phân biệt mức độ hoàn thiện đồ họa và tính năng giữa 4 loại tài liệu thiết kế:

```
[Khung sơ lược]                                                          [Sản phẩm tương tác]
와이어프레임 (Wireframe) ──► 목업 (Mockup) ──► 스토리보드 (Storyboard) ──► 프로토타입 (Prototype)
(Layout đen trắng)       (Đồ họa tĩnh)      (Kịch bản + Logic)        (Bấm chuyển động thử)
```

1. **와이어프레임 (Wireframe — Khung xương layout):**
   - Bản vẽ phác thảo sơ bộ ở giai đoạn đầu, tập trung vào **bố cục không gian (`레이아웃`), cấu trúc phân vùng nội dung và vị trí đặt các nút bấm/menu**.
   - Thường vẽ bằng đường nét đen trắng, không dùng màu sắc bắt mắt, không chứa hình ảnh hoàn chỉnh.
2. **목업 (Mockup — Bản dựng đồ họa tĩnh):**
   - Bản vẽ tĩnh hoàn thiện đầy đủ về mặt thiết kế thị giác (`시각 디자인`): màu sắc thương hiệu, kiểu chữ (typography), icon và hình ảnh thực tế.
   - **Đặc điểm sống còn đề thi:** Mockup là **bản vẽ tĩnh không có tương tác** (người dùng bấm vào các nút không có phản hồi chuyển động).
3. **스토리보드 (Storyboard — Kịch bản thao tác màn hình):**
   - Là tài liệu hướng dẫn hoàn chỉnh nhất dành cho lập trình viên phát triển giao diện.
   - Cấu trúc gồm: **Hình ảnh Wireframe/Mockup + Mô tả kịch bản tương tác (Description) + Quy tắc nghiệp vụ (Business Logic) khi người dùng bấm vào từng nút**.
4. **프로토타입 (Prototype — Bản mẫu tương tác thử nghiệm):**
   - Là sản phẩm mô phỏng động, cho phép người dùng **trực tiếp bấm chuột hoặc chạm tay để trải nghiệm luồng thao tác thực tế (Interactive Simulation)**.
   - Dùng để làm kiểm thử khả dụng (`사용성 테스트 - Usability Testing`) với khách hàng nhằm phát hiện lỗi giao diện trước khi lập trình viên bắt đầu viết code thực tế.

---

#### 4. Phân biệt bộ ba tương tác: HCI vs UX vs UI
- **인간-컴퓨터 상호작용 (HCI — Human-Computer Interaction):**
  - Ngành khoa học nghiên cứu cách thiết kế hệ thống máy tính sao cho con người có thể tương tác một cách tối ưu, an toàn và thuận tiện nhất. Trọng tâm là mối quan hệ giữa người và máy.
- **사용자 경험 (UX — User Experience):**
  - Toàn bộ cảm xúc, thái độ, nhận thức chủ quan và sự thỏa mãn của người dùng trải qua trước, trong và sau khi tương tác với sản phẩm hoặc dịch vụ.
  - Mang tính chủ quan, bao quát toàn diện (tốc độ tải trang, sự tiện lợi, tính thẩm mỹ, dịch vụ chăm sóc khách hàng).
- **사용자 인터페이스 (UI — User Interface):**
  - Tập hợp các công cụ hữu hình trực quan (màn hình hiển thị, nút bấm, màu sắc, phông chữ, biểu mẫu nhập liệu) giúp con người giao tiếp vật lý với phần mềm.
- **Mối quan hệ bản chất:** UI là phương tiện hữu hình nằm bên trong UX; tối ưu hóa UI và tuân thủ các nguyên lý HCI là điều kiện tiên quyết để tạo nên một UX xuất sắc.

---

#### 5. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (4 Nguyên tắc vàng của UI):** Đề thi trắc nghiệm thường chèn các từ gây nhiễu như `복잡성 (Tính phức tạp)`, `심미성 (Tính thẩm mỹ)`, `보안성 (Tính bảo mật)` và hỏi có phải là 1 trong 4 nguyên tắc cơ bản của UI không $\rightarrow$ **SAI**. Bộ 4 nguyên tắc chuẩn chỉ gồm: **직관성 (Trực quan), 유효성 (Hữu hiệu), 학습성 (Dễ học), 유연성 (Linh hoạt)**.
- **Bẫy 2 (Mockup vs Prototype):**
  - Bản dựng đồ họa tĩnh, không chuyển động được $\rightarrow$ **목업 (Mockup)**.
  - Bản dựng có tương tác, bấm chuyển màn hình chạy thử nghiệm được $\rightarrow$ **프로토타입 (Prototype)**.
- **Bẫy 3 (NUI vs OUI):** Điều khiển bằng cử chỉ tay, giọng nói $\rightarrow$ **NUI (Natural UI)**; thiết bị màn hình uốn dẻo, co giãn vật lý $\rightarrow$ **OUI (Organic UI)**.

- **한 문장 설명 (Câu chốt ghi nhớ):** "UI có 4 nguyên tắc Trực - Hiệu - Học - Hoạt; Wireframe khung xương, Mockup tĩnh đồ họa, Storyboard kịch bản, Prototype bấm chạy thử".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Tiêu chuẩn Tính khả dụng ISO 9241 (Usability Standard)
Theo tiêu chuẩn quốc tế ISO 9241-11, tính khả dụng của một giao diện phần mềm được đo lường dựa trên 3 trụ cột khoa học:
1. **유효성 (Effectiveness - Tính hữu hiệu):** Tỷ lệ phần trăm người dùng hoàn thành chính xác nhiệm vụ được giao (ví dụ: 98% người dùng đăng ký tài khoản thành công mà không bị lỗi hệ thống).
2. **효율성 (Efficiency - Tính hiệu quả):** Lượng tài nguyên tiêu hao (thời gian thao tác, số lần bấm chuột) để hoàn thành nhiệm vụ đó (ví dụ: thời gian hoàn tất đơn hàng giảm từ 3 phút xuống còn 45 giây).
3. **만족도 (Satisfaction - Sự hài lòng):** Mức độ thoải mái và thái độ tích cực của người dùng khi trải nghiệm hệ thống, thường đo lường qua thang điểm CSAT hoặc SUS (System Usability Scale).

#### 2. Nguyên tắc Thiết kế Tiếp cận Web bình đẳng (Web Content Accessibility Guidelines - WCAG)
Đề thi trắc nghiệm nâng cao có thể hỏi về các tiêu chuẩn tiếp cận dành cho người khuyết tật:
1. **인식의 용이성 (Perceivable - Dễ nhận thức):** Mọi thông tin trực quan phải có văn bản thay thế (Thẻ `alt` cho hình ảnh để phần mềm đọc màn hình cho người khiếm thị đọc được); tỷ lệ tương phản màu sắc chữ và nền phải đạt tối thiểu 4.5:1.
2. **운용의 용이성 (Operable - Dễ vận hành):** Mọi chức năng trên màn hình phải điều khiển được hoàn toàn bằng **Bàn phím (Keyboard Navigation)** mà không bắt buộc phải có chuột.
3. **이해의 용이성 (Understandable - Dễ hiểu):** Bố cục và cơ chế điều hướng trang web phải nhất quán; thông báo lỗi phải chỉ rõ vị trí và cách khắc phục.
4. **견고성 (Robust - Tính bền vững):** Mã HTML phải đạt chuẩn kỹ thuật W3C để các công nghệ hỗ trợ (Screen Reader) có thể phân tích cú pháp chính xác.

#### 3. Sơ đồ ma trận 4 Nguyên tắc vàng UI (직관성·유효성·학습성·유연성)

##### A. Sơ đồ ASCII cấu trúc 4 trụ cột tương tác người - máy
```
               ┌───────────────────────────────────────────────────┐
               │         UI 4대 기본 원칙 (4 Nguyên tắc vàng UI)    │
               │               (Mẹo: 직 - 유 - 학 - 유)             │
               └─────────────────────────┬─────────────────────────┘
                                         │
         ┌───────────────────────┬───────┴───────┬───────────────────────┐
         ▼                       ▼               ▼                       ▼
   ┌───────────┐           ┌───────────┐   ┌───────────┐           ┌───────────┐
   │  직관성   │           │  유효성   │   │  학습성   │           │  유연성   │
   │(Intuitive)│           │(Effective)│   │(Learnable)│           │(Flexible) │
   ├───────────┤           ├───────────┤   ├───────────┤           ├───────────┤
   │ 누구나    │           │ 목적을    │   │ 쉽게      │           │ 오류 방지 │
   │ 쉽게 이해 │           │ 정확/완전 │   │ 배우고    │           │ 및 제어   │
   │           │           │ 달성      │   │ 익힘      │           │ 요구 수용 │
   ├───────────┤           ├───────────┤   ├───────────┤           ├───────────┤
   │ Nhìn là   │           │ Đạt mục   │   │ Học nhanh │           │ Bao dung  │
   │ hiểu ngay │           │ tiêu trọn │   │ nhớ lâu,  │           │ sai sót,  │
   │ không cần │           │ vẹn không │   │ giao diện │           │ phím tắt  │
   │ đào tạo   │           │ sai lệch  │   │ nhất quán │           │ linh hoạt │
   └───────────┘           └───────────┘   └───────────┘           └───────────┘
```

##### B. Ma trận đối chiếu tình huống thực tế và bẫy trắc nghiệm
| Nguyên tắc UI | Tình huống thiết kế đạt chuẩn (Best Practice) | Tình huống vi phạm điển hình (Bad Design) |
|:---|:---|:---|
| **직관성 (Intuitiveness)** | Biểu tượng kính lúp đại diện cho ô Tìm kiếm; nút giỏ hàng đại diện cho thanh toán; nút màu đỏ cảnh báo thao tác Xóa dữ liệu. | Nút "Lưu file" nhưng lại vẽ biểu tượng hình chiếc kéo; icon không gợi liên tưởng tới hành vi thực tế. |
| **유효성 (Effectiveness)** | Form thanh toán xác thực thẻ thành công và xuất hóa đơn đúng số tiền; người dùng hoàn thành giao dịch mà không gặp lỗi nghẽn. | Bấm nút "Đặt mua" nhưng hệ thống trừ tiền mà không ghi nhận đơn hàng hoặc báo lỗi không rõ nguyên nhân. |
| **학습성 (Learnability)** | Mọi trang con trong website đều đặt thanh menu điều hướng ở cạnh trên cùng và logo ở góc trên bên trái; thao tác quen thuộc từ trang trước dùng ngay cho trang sau. | Trang chủ đặt nút menu ở trên cùng, nhưng vào trang chi tiết sản phẩm lại giấu nút menu xuống đáy góc phải khiến người dùng phải học lại cách dùng. |
| **유연성 (Flexibility)** | Cho phép người dùng mới bấm chuột vào menu, đồng thời cung cấp tổ hợp phím tắt (Ctrl+S, Ctrl+Z) cho người dùng thành thạo; có nút "Hoàn tác" (Undo) khi lỡ xóa nhầm. | Bắt buộc mọi đối tượng chỉ được thao tác qua một luồng duy nhất; lỡ bấm nút xóa là mất vĩnh viễn không thể khôi phục lại dữ liệu. |

---

#### 4. Quy trình thiết kế UI 3 bước chuẩn kỹ nghệ phần mềm

##### A. Sơ đồ ASCII quy trình thiết kế giao diện khép kín
```
┌────────────────────────────────┐
│ 1단계: 사용자 요구사항 확인      │
│ (User Research & Analysis)     │
└───────────────┬────────────────┘
                │ • Khảo sát nhu cầu người dùng (Survey, Interview)
                │ • Xây dựng chân dung người dùng đại diện (페르소나 - Persona)
                │ • Xác định bối cảnh sử dụng & kịch bản người dùng (User Scenario)
                ▼
┌────────────────────────────────┐
│ 2단계: UI 설계 및 문서화        │
│ (UI Architecture & Design)     │
└───────────────┬────────────────┘
                │ • Thiết kế cấu trúc thông tin (정보 구조 - IA) & Cây chức năng
                │ • Vẽ khung xương màn hình (와이어프레임 - Wireframe)
                │ • Thiết kế kịch bản chi tiết (스토리보드 - Storyboard)
                │ • Ban hành Quy tắc giao diện chung (UI 공통 규칙)
                ▼
┌────────────────────────────────┐
│ 3단계: UI 구현 및 사용성 평가   │
│ (Implementation & Evaluation)  │
└────────────────────────────────┘
                  • Tạo bản mẫu tương tác động (프로토타입 - Prototype)
                  • Thử nghiệm với người dùng thật (사용성 테스트 - Usability Test)
                  • Thu thập chỉ số hoàn thành (Effectiveness, Efficiency, CSAT)
                  • Tinh chỉnh vòng lặp trước khi bàn giao cho đội lập trình
```

##### B. Chi tiết 3 bước thiết kế UI trong chuẩn đề thi
1. **1단계: 사용자 요구사항 확인 및 분석 (Xác nhận & Phân tích yêu cầu người dùng):**
   - **Xây dựng 페르소나 (Persona):** Tạo lập một nhân vật giả định mang đầy đủ các đặc tính nhân khẩu học, thói quen thao tác, mục tiêu và rào cản tâm lý đại diện cho nhóm người dùng mục tiêu.
   - **Lập 사용자 여정 맵 (Customer Journey Map):** Lược đồ từng bước trải nghiệm của người dùng từ khi mở ứng dụng đến khi hoàn tất tác vụ cốt lõi, giúp phát hiện các điểm nghẽn trải nghiệm (Pain Points).
2. **2단계: UI 아키텍처 및 화면 설계 (Thiết kế Kiến trúc UI & Màn hình):**
   - **Cấu trúc thông tin (`정보 구조 - IA / Information Architecture`):** Phân loại và tổ chức nội dung hệ thống thành dạng cây phân cấp (Tree Structure) logic, giúp người dùng dễ dàng định hướng vị trí hiện tại.
   - **Soạn thảo UI 시나리오 문서 (UI Scenario Document):** Là tài liệu bàn giao kỹ thuật hoàn chỉnh gồm Wireframe/Mockup kết hợp mô tả kịch bản (Description) cho từng nút bấm, trường hợp ngoại lệ (Exception Case) và luồng điều hướng màn hình.
3. **3단계: UI 구현 및 사용성 평가 (Hiện thực hóa UI & Đánh giá khả dụng):**
   - **Tạo bản mẫu (`프로토타입 - Prototype`):** Chuyển giao kịch bản Storyboard thành bản mẫu tương tác chạy thử (Interactive Mockup/Code) để khách hàng và lập trình viên trải nghiệm trước.
   - **Kiểm thử khả dụng (`사용성 평가 - Usability Testing`):** Mời nhóm người dùng đại diện thực hiện các kịch bản thực tế, ghi lại thời gian hoàn tất tác vụ (Efficiency) và tỷ lệ lỗi sai (Effectiveness) để hoàn thiện bản thiết kế cuối cùng trước khi lập trình diện rộng.

---

### 복습 체크리스트
- [ ] Phân biệt được 4 loại hình giao diện CLI (dòng lệnh), GUI (đồ họa), NUI (tự nhiên: giọng nói/cử chỉ), OUI (hữu cơ uốn dẻo).
- [ ] Gọi tên chính xác 6 cử chỉ cảm ứng di động: Tap, Double Tap, Drag, Pan, Flick, Pinch.
- [ ] Đọc vanh vách 4 nguyên tắc vàng của UI: 직관성 (Trực quan), 유효성 (Hữu hiệu), 학습성 (Dễ học), 유연성 (Linh hoạt).
- [ ] Xếp đúng thứ tự 4 sản phẩm thiết kế màn hình: Wireframe (khung xương) $\rightarrow$ Mockup (tĩnh) $\rightarrow$ Storyboard (kịch bản) $\rightarrow$ Prototype (tương tác động).
- [ ] Phân biệt được bản chất giữa HCI (khoa học tương tác), UX (trải nghiệm toàn diện của người dùng), UI (giao diện cụ thể).
- [ ] Nhớ 3 tiêu chí đo lường tính khả dụng của chuẩn ISO 9241: 유효성 (Hữu hiệu), 효율성 (Hiệu quả), 만족도 (Sự hài lòng).
- [ ] Nhớ nguyên tắc quan trọng nhất của Web Accessibility: mọi tính năng đều phải thao tác được bằng bàn phím.
