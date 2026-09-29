# 핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 매뉴얼, 빌드, 배포, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**에서 만든 기준을 이어받아 **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)

Từ **41. 빌드 자동화 도구 심화: Jenkins vs Gradle**, ta đã có điểm tựa để bước vào **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 36/95 trước khi đi vào chi tiết.

Để đọc **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **제품 소프트웨어 매뉴얼 (Tài liệu hướng dẫn)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 제품 소프트웨어 매뉴얼 (Tài liệu hướng dẫn)

Các ý ngay dưới **제품 소프트웨어 매뉴얼 (Tài liệu hướng dẫn)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **설치 매뉴얼 (Installation Manual):** Hướng dẫn cài đặt. (Lưu ý cách cài, cấu hình hệ thống, cách xóa cài đặt - Uninstall).
- **사용자 매뉴얼 (User Manual):** Hướng dẫn sử dụng. (Giao diện UI, cấu hình tối thiểu, cách dùng tính năng).
- Cả hai đều phải viết theo góc nhìn của **사용자 (Người dùng)**.

Các bullet của **제품 소프트웨어 매뉴얼 (Tài liệu hướng dẫn)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **제품 소프트웨어 매뉴얼 (Tài liệu hướng dẫn)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **빌드 및 모니터링 도구 (Công cụ Build & Monitoring)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **빌드 및 모니터링 도구 (Công cụ Build & Monitoring)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 빌드 및 모니터링 도구 (Công cụ Build & Monitoring)

Bây giờ ta đi vào nội dung của **빌드 및 모니터링 도구 (Công cụ Build & Monitoring)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **빌드 자동화 도구 (Build Automation):** Biến source code thành file chạy một cách tự động. Ví dụ: Ant, Maven, Gradle, **Jenkins**.
- **버전 관리 도구 (Version Control):** Git, SVN.
- **정적 분석 도구 (Static Analysis):** Phân tích code tìm lỗi mà **KHÔNG CHẠY** chương trình. Ví dụ: PMD, Cppcheck, SonarQube.
- **동적 분석 도구 (Dynamic Analysis):** Vừa **CHẠY** chương trình vừa tìm lỗi (tràn bộ nhớ, v.v.). Ví dụ: Avalanche, Valgrind.

- **Vietnamese Explanation:** "Tĩnh" (Static) nghĩa là code nằm im trên giấy, dùng tool soi từng dòng xem có viết sai cú pháp hay không. "Động" (Dynamic) là bấm nút chạy phần mềm rồi xem nó có bị sập hay tốn RAM không.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Tĩnh (Static) = PMD, SonarQube (Soi code). Động (Dynamic) = Valgrind (Chạy thử). Build = Jenkins (Ông quản gia tự động).

---

Với **빌드 및 모니터링 도구 (Công cụ Build & Monitoring)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **빌드 및 모니터링 도구 (Công cụ Build & Monitoring)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.