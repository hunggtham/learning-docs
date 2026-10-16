# Môn 2 · Bài 14 — Nguyên lý, phân loại và quy trình kiểm thử phần mềm

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Trong hệ thống vòng đời phát triển phần mềm, sau khi hoàn thành đóng gói, quản lý cấu hình và tự động hóa bản dựng, trọng tâm chất lượng được chuyển hoàn toàn sang **애플리케이션 테스트 관리 (Quản lý kiểm thử ứng dụng)**. Bài học này đóng vai trò mở màn cho Chương 4, thiết lập các nguyên lý nền tảng, hệ thống phân loại đa chiều và quy trình kiểm thử 5 bước chuẩn quốc tế ISTQB trước khi đi sâu vào kỹ thuật kiểm thử hộp trắng và hộp đen ở các bài kế tiếp.

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `57-bai-hoc.md`, `58-bai-hoc.md`, `61-bai-hoc.md`, `62-bai-hoc.md`, `63-bai-hoc.md` và `72-bai-hoc.md` (tương ứng với các mục 14, 42, 43, 097-2, 105, 120-2 ~ 126 trong tài liệu chuẩn gốc). Toàn bộ thuật ngữ tiếng Hàn thi cử được đối chiếu với chuẩn khảo thí HRDK và chuẩn ISTQB.

> **Mạch kiến thức:** Kiểm thử không phải là công việc mò tìm lỗi ngẫu nhiên mà là một quy trình kỹ thuật có phương pháp luận. Bài học này giải quyết ba vấn đề cốt lõi: (1) Kiểm thử có thể và không thể chứng minh điều gì? (2) Làm sao phân biệt góc nhìn nhà phát triển (Verification) với người dùng (Validation) và các loại hình kiểm thử chuyên biệt? (3) Một tiến trình kiểm thử chuẩn mực đi qua những bước nào để sinh ra Test Case và Test Procedure?

---

## 1. 소프트웨어 테스트 7대 원리 — Bảy nguyên lý kiểm thử phần mềm

**테스팅은 결함이 존재함을 밝히는 활동이지, 결함이 없음을 증명할 수는 없다.**

Kiểm thử phần mềm là hoạt động chứng minh sự tồn tại của khiếm khuyết (결함 존재 증명), tuyệt đối không thể chứng minh phần mềm hoàn toàn sạch bóng lỗi 100%. Dù trải qua hàng triệu ca kiểm thử không phát sinh lỗi, ta chỉ có thể kết luận chưa tìm thấy lỗi trong phạm vi kiểm tra đó, chứ không thể cam kết hệ thống hoàn hảo tuyệt đối.

### Bảy nguyên lý nền tảng theo chuẩn quốc tế ISTQB

1. **결함 존재 증명 (Testing shows presence of defects — Chứng minh sự hiện diện của lỗi):**
   - [한국어]: `테스팅은 결함이 존재함을 보여줄 수 있지만, 결함이 없음을 증명할 수는 없다.`
   - [Tiếng Việt]: Kiểm thử làm giảm xác suất lỗi còn sót lại trong phần mềm nhưng không bao giờ là bằng chứng khẳng định phần mềm đúng tuyệt đối không còn lỗi.
2. **완벽한 테스팅 불가능 (Exhaustive testing is impossible — Kiểm thử kiệt quệ là bất khả thi):**
   - [한국어]: `모든 가능한 입력과 사전 조건의 조합을 테스트하는 것은 불가능하다.`
   - [Tiếng Việt]: Không thể kiểm thử toàn bộ mọi tổ hợp dữ liệu vào, điều kiện tiên quyết và nhánh rẽ thực thi (trừ các trường hợp cực kỳ nhỏ và tầm thường). Do đó kiểm thử phải dựa trên phân tích rủi ro và độ ưu tiên để phân bổ nguồn lực.
3. **조기 테스팅 (Early Testing — Kiểm thử sớm):**
   - [한국어]: `테스팅 활동은 소프트웨어 생명 주기 초기 단계에서부터 시작되어야 한다.`
   - [Tiếng Việt]: Hoạt động kiểm thử phải được tiến hành càng sớm càng tốt ngay từ pha phân tích yêu cầu và thiết kế. Chi phí sửa lỗi ở giai đoạn yêu cầu là $1\times$, nhưng nếu lỗi đó lọt tới pha vận hành bảo trì mới phát hiện, chi phí khắc phục có thể đội lên gấp $60 \sim 100$ lần.
4. **결함 집중 (Defect Clustering — Tập trung lỗi / 파레토 법칙 Pareto 80:20):**
   - [한국어]: `대부분의 결함은 소수의 특정 모듈에 집중되어 발견된다.`
   - [Tiếng Việt]: Hiện tượng lỗi kết cụm theo quy luật Pareto: khoảng 80% tổng số khiếm khuyết thường nằm trong khoảng 20% số mô-đun phức tạp nhất. Khi phát hiện một lỗi trong một mô-đun, xác suất cao mô-đun đó còn chứa nhiều lỗi khác chưa lộ diện.
5. **살충제 패러독스 (Pesticide Paradox — Nghịch lý thuốc trừ sâu):**
   - [한국어]: `동일한 테스트를 반복하면 더 이상 새로운 결함을 찾아낼 수 없다.`
   - [Tiếng Việt]: Giống như việc phun mãi một loại thuốc trừ sâu sẽ làm sâu bọ kháng thuốc, nếu liên tục chạy lặp đi lặp lại một bộ Test Case cũ giống nhau thì hệ thống kiểm thử sẽ mất khả năng phát hiện lỗi mới. Vì vậy, bắt buộc phải định kỳ rà soát, cập nhật và bổ sung các ca kiểm thử mới với các góc nhìn dị thường.
6. **정황 의존성 (Testing is context dependent — Kiểm thử phụ thuộc ngữ cảnh):**
   - [한국어]: `테스팅은 정황과 환경에 따라 다르게 수행되어야 한다.`
   - [Tiếng Việt]: Không có một chiến lược kiểm thử duy nhất áp dụng cho mọi sản phẩm. Kiểm thử phần mềm y tế, ngân hàng hay an toàn hàng không đòi hỏi tiêu chuẩn nghiêm ngặt và độ tin cậy cao hơn rất nhiều so với một ứng dụng mạng xã hội thông thường.
7. **오류-부재의 궤변 (Absence-of-Errors Fallacy — Ngụy biện về sự vắng bóng lỗi):**
   - [한국어]: `결함을 모두 제거했다고 하더라도 사용자의 요구사항을 만족시키지 못하면 성공적인 소프트웨어라 할 수 없다.`
   - [Tiếng Việt]: Việc tìm và sửa sạch sẽ 100% các lỗi kỹ thuật được phát hiện không đồng nghĩa với việc phần mềm sẽ thành công, nếu hệ thống đó không giải quyết đúng bài toán nghiệp vụ và kỳ vọng thực tế của người dùng.

### Keyword cần nhớ
- **결함 존재 증명 (Shows presence of defects):** Kiểm thử tìm ra lỗi, không chứng minh hết sạch lỗi.
- **결함 집중 (Defect Clustering / 파레토 80:20):** 80% lỗi nằm ở 20% mô-đun phức tạp.
- **살충제 패러독스 (Pesticide Paradox):** Test Case cũ bị "nhờn lỗi", phải định kỳ cải tiến.
- **오류-부재의 궤변 (Absence-of-Errors Fallacy):** Phần mềm không lỗi kỹ thuật nhưng sai nhu cầu khách hàng thì vẫn thất bại.

### Điểm dễ nhầm trong đề
- Đề thi hay hỏi: *"Một nhóm kiểm thử chạy bộ kiểm thử 3 tháng liền không phát sinh thêm lỗi nào và kết luận phần mềm sạch lỗi 100%, họ đã vi phạm nguyên lý nào?"* $\rightarrow$ Đáp án là vi phạm cả **결함 존재 증명** (không thể chứng minh hết lỗi) và rơi vào bẫy **살충제 패러독스** (không cập nhật Test Case).
- Nhầm lẫn giữa **Defect Clustering** và **Pesticide Paradox**: Defect Clustering nói về vị trí tập trung của lỗi (nằm ở đâu), còn Pesticide Paradox nói về sự suy giảm hiệu quả của Test Case theo thời gian (cách thức kiểm thử).

---

## 2. 검증(Verification) vs 확인(Validation) — Góc nhìn kiểm thử

Trong kỹ nghệ phần mềm, chất lượng sản phẩm được xem xét từ hai góc độ hoàn toàn khác nhau: góc nhìn kỹ thuật của nhà phát triển và góc nhìn giá trị thực tế của khách hàng. Barry Boehm đã định nghĩa sự khác biệt này bằng hai câu hỏi kinh điển:

- **검증 (Verification — Kiểm tra xác minh):** *"Are we building the product right?"* (Chúng ta có đang xây dựng sản phẩm đúng quy chuẩn kỹ thuật không?)
- **확인 (Validation — Kiểm tra xác nhận):** *"Are we building the right product?"* (Chúng ta có đang xây dựng đúng sản phẩm mà khách hàng thực sự cần không?)

### Bảng so sánh đối đầu Verification vs Validation

| Tiêu chí | 검증 (Verification - Xác minh kỹ thuật) | 확인 (Validation - Xác nhận người dùng) |
| :--- | :--- | :--- |
| **Góc nhìn chủ thể** | **Nhà phát triển (Developer / Engineer)** | **Người dùng cuối (User / Customer)** |
| **Câu hỏi triết lý** | *"Are we building the product right?"* | *"Are we building the right product?"* |
| **Mục đích** | Đảm bảo sản phẩm tuân thủ đúng tài liệu thiết kế và đặc tả kỹ thuật của giai đoạn trước | Đảm bảo sản phẩm đáp ứng đúng nhu cầu và kỳ vọng thực tế của người dùng |
| **Đối tượng căn cứ** | Đặc tả kiến trúc, tài liệu thiết kế chi tiết, coding standard | Nhu cầu kinh doanh thực tế, trải nghiệm người dùng |
| **Hoạt động tiêu biểu** | Code Review, Inspection, Walkthrough, **Unit Test, Integration Test** | **System Test, Acceptance Test**, Alpha Test, Beta Test |

### Bẫy đề thi trắc nghiệm
- Đề thi thường yêu cầu phân loại các hoạt động kiểm thử:
  - Các hoạt động thuộc **검증 (Verification)**: Rà soát mã nguồn, kiểm tra thiết kế, kiểm thử đơn vị (Unit Test), kiểm thử tích hợp (Integration Test).
  - Các hoạt động thuộc **확인 (Validation)**: Kiểm thử hệ thống (System Test), kiểm thử chấp nhận (Acceptance Test), thử nghiệm người dùng thực tế (Alpha/Beta Test).

---

## 3. 테스트 분류 체계 — Hệ thống phân loại kiểm thử đa chiều

Kiểm thử ứng dụng phần mềm được phân loại dựa trên ba trục tiêu chuẩn độc lập: theo trạng thái thực thi chương trình, theo cơ sở thiết kế ca kiểm thử và theo mục đích kiểm tra chuyên biệt.

### 3.1. Phân loại theo trạng thái thực thi (프로그램 실행 여부)

- **정적 테스트 (Static Testing — Kiểm thử tĩnh):**
  - **Đặc trưng:** Thực hiện rà soát tài liệu, cấu trúc và mã nguồn **mà không cần nạp hay chạy chương trình trên máy tính**.
  - **Hình thức chính:**
    - **워크스루 (Walkthrough):** Buổi trao đổi bán chính thức do chính tác giả mã nguồn chủ trì để trình bày giải thuật và tiếp nhận phản hồi từ đồng nghiệp.
    - **인스펙션 (Inspection):** Buổi thẩm định chính thức cực kỳ nghiêm ngặt do một chuyên gia độc lập (Moderator) điều phối, sử dụng danh mục kiểm tra (Checklist) chuẩn hóa để soi từng dòng code và lập biên bản lỗi chính thức.
    - **정적 코드 분석 (Static Code Analysis):** Dùng công cụ phần mềm tự động quét quy tắc mã, lỗ hổng cú pháp và bảo mật (SonarQube, PMD).
- **동적 테스트 (Dynamic Testing — Kiểm thử động):**
  - **Đặc trưng:** **Trực tiếp nạp và chạy chương trình trên máy tính**, truyền dữ liệu đầu vào và quan sát hành vi, ngõ ra thực tế.
  - Bao gồm cả kiểm thử hộp trắng (White-box) và kiểm thử hộp đen (Black-box).

### 3.2. Phân loại theo cơ sở thiết kế ca kiểm thử (테스트 설계 기반)

- **명세 기반 (Specification-based — Dựa trên đặc tả):** Dựa vào tài liệu yêu cầu chức năng bên ngoài mà không nhìn vào code (Black-box Testing: Phân vùng tương đương, Phân tích giá trị biên).
- **구조 기반 (Structure-based — Dựa trên cấu trúc):** Dựa vào logic luồng điều khiển bên trong mã nguồn (White-box Testing: Phủ câu lệnh, Phủ nhánh, Phủ điều kiện).
- **경험 기반 (Experience-based — Dựa trên kinh nghiệm):** Dựa vào trực giác và kinh nghiệm tích lũy của kiểm thử viên (Error Guessing / 오류 예측, Exploratory Testing / 탐색적 테스팅).

### 3.3. Phân loại theo mục đích kiểm tra chuyên biệt (목적에 따른 테스트)

| Loại kiểm thử | Tên Hàn / Anh | Mục đích và cơ chế nhận diện trong đề |
| :--- | :--- | :--- |
| **Kiểm thử phục hồi** | **회복 테스트 (Recovery)** | Cố tình gây lỗi hệ thống (ngắt điện, đứt mạng) để đo khả năng và thời gian tự khôi phục dữ liệu |
| **Kiểm thử an toàn** | **안전 테스트 (Security)** | Kiểm tra các lỗ hổng bảo mật, cơ chế phân quyền, chống thâm nhập trái phép từ bên ngoài |
| **Kiểm thử áp lực** | **강도 테스트 (Stress)** | Đưa hệ thống vào trạng thái **quá tải cực đoan (과부하)** vượt ngưỡng thiết kế tối đa để xem hành vi sụp đổ |
| **Kiểm thử hiệu năng** | **성능 테스트 (Performance)** | Đo lường thời gian phản hồi (Response Time), thông lượng (Throughput) và mức chiếm dụng tài nguyên trong điều kiện chuẩn |
| **Kiểm thử hồi quy** | **회귀 테스트 (Regression)** | Sau khi sửa lỗi hoặc thêm tính năng mới, **chạy lại kiểm thử để đảm bảo việc sửa code không sinh ra lỗi mới (새로운 결함)** |
| **Kiểm thử song song** | **병행 테스트 (Parallel)** | Nhập cùng một tập dữ liệu vào cả hệ thống mới và hệ thống cũ để so sánh đối chiếu kết quả đầu ra |

---

## 4. 테스트 프로세스 — Quy trình kiểm thử 5 bước chuẩn ISTQB

Tiến trình kiểm thử phần mềm chuyên nghiệp được tổ chức tuần tự qua 5 giai đoạn:

$$\mathbf{계획\ 및\ 제어} \longrightarrow \mathbf{분석\ 및\ 설계} \longrightarrow \mathbf{구현\ 및\ 실현} \longrightarrow \mathbf{평가} \longrightarrow \mathbf{완료}$$

1. **계획 및 제어 (Test Planning & Control — Lập kế hoạch & Kiểm soát):**
   - Xác định phạm vi kiểm thử, phân tích rủi ro, dự trù tài nguyên và thiết lập lịch trình.
   - Định nghĩa **Tiêu chí kết thúc kiểm thử (종료 조건 / Exit Criteria)**: Quy định ngưỡng định lượng khi nào được phép dừng test (ví dụ: Statement Coverage $\ge 90\%$, 100% ca test mức Critical đều PASS, hết ngân sách/thời gian cho phép).
2. **분석 및 설계 (Test Analysis & Design — Phân tích & Thiết kế):**
   - Rà soát tài liệu yêu cầu, xác định các điều kiện kiểm thử (Test Conditions).
   - Thiết kế kịch bản kiểm thử (Test Scenario) và chi tiết hóa thành các **Ca kiểm thử (테스트 케이스 — Test Case)**.
3. **구현 및 실현 (Test Implementation & Execution — Triển khai & Thực thi):**
   - Chuẩn bị dữ liệu và môi trường thử nghiệm.
   - Soạn thảo **Thủ tục kiểm thử (테스트 프로시저 — Test Procedure)** xác định trình tự thực hiện các ca test.
   - Thực thi ca kiểm thử, ghi nhận nhật ký kiểm thử (Test Log) và lập báo cáo khiếm khuyết (Defect Report).
4. **평가 (Test Evaluation — Đánh giá):**
   - So sánh kết quả thực tế với mục tiêu ban đầu; đánh giá xem đã đạt tiêu chí kết thúc (Exit Criteria) hay chưa để quyết định nghiệm thu hay tiếp tục kiểm thử.
5. **완료 (Test Completion — Hoàn tất):**
   - Lưu trữ toàn bộ sản phẩm bàn giao (Test Deliverables); đúc kết bài học kinh nghiệm (Lessons Learned); bàn giao cho đơn vị vận hành.

### Phân biệt Test Case vs Test Procedure
- **테스트 케이스 (Test Case):** Xác định *CẦN TEST CÁI GÌ* (Gồm điều kiện tiên quyết, dữ liệu đầu vào và kết quả mong đợi Expected Output). Được tạo ra ở bước **분석 및 설계**.
- **테스트 프로시저 (Test Procedure):** Xác định *THỰC HIỆN TEST NHƯ THẾ NÀO* (Quy trình các bước thao tác, thứ tự chạy các Test Case). Được tạo ra ở bước **구현 및 실현**.

---

## 5. Nối mạch kiến thức sang bài tiếp theo

Từ việc nắm vững 7 nguyên lý kiểm thử, phân biệt góc nhìn Verification vs Validation và quy trình 5 bước, người học đã có được khung tư duy phương pháp luận vững chắc. Trong các cơ sở thiết kế ca kiểm thử:
- Cơ sở cấu trúc bên trong mã nguồn dẫn trực tiếp sang **[Bài 15: Kiểm thử hộp trắng và độ bao phủ kiểm thử](15-kiem-thu-hop-trang-va-coverage.md)**, nơi ta sẽ phân tích logic luồng điều khiển, các tiêu chí độ phủ Coverage và công thức tính độ phức tạp McCabe.
- Sau đó, cơ sở đặc tả chức năng bên ngoài sẽ được phân tích toàn diện trong **[Bài 16: Kiểm thử hộp đen và kỹ thuật thiết kế Test Case](16-kiem-thu-hop-den-va-test-case.md)**.

---

## 6. 복습 체크리스트 (Checklist ôn tập)

- [ ] Nêu đầy đủ 7 nguyên lý kiểm thử phần mềm theo chuẩn ISTQB.
- [ ] Giải thích hiện tượng 결함 집중 (Defect Clustering) và quy luật Pareto 80:20.
- [ ] Phân biệt bản chất câu hỏi của 검증 (Verification) và 확인 (Validation) theo Barry Boehm.
- [ ] Phân biệt 워크스루 (Walkthrough - không chính thức) và 인스펙션 (Inspection - chính thức dùng checklist) trong kiểm thử tĩnh.
- [ ] Nhận diện 강도 테스트 (Stress Testing) qua từ khóa ép tải quá mức (과부하).
- [ ] Nhận diện 회귀 테스트 (Regression Testing) qua từ khóa kiểm tra phát sinh lỗi mới sau khi sửa đổi mã nguồn.
- [ ] Nhớ thứ tự 5 giai đoạn kiểm thử: 계획/제어 $\rightarrow$ 분석/설계 $\rightarrow$ 구현/실현 $\rightarrow$ 평가 $\rightarrow$ 완료.
- [ ] Nhớ đúng: Test Case sinh ra ở bước Phân tích & Thiết kế; Test Procedure sinh ra ở bước Triển khai & Thực thi.
