# 12. 요구사항 (Requirements)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **12. 요구사항 (Requirements)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **12. 요구사항 (Requirements)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 현행 시스템 분석 (Current System Analysis)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

요구사항

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)**에서 만든 기준을 이어받아 **12. 요구사항 (Requirements)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 12. 요구사항 (Requirements)

Từ **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)**, ta đã có điểm tựa để bước vào **12. 요구사항 (Requirements)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 9/55 trước khi đi vào chi tiết.

Để đọc **12. 요구사항 (Requirements)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **요구사항 분석 (Requirements Analysis)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 요구사항 분석 (Requirements Analysis)

Các ý ngay dưới **요구사항 분석 (Requirements Analysis)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

*   **분류 (Phân loại):** 기능적(Functional) / 비기능적(Non-functional)으로 조직화.
*   **절차 (Quy trình 5 bước):** 선별(목록 작성) -> 자료 준비 -> 분류(기능/비기능) -> 분석 및 수정 -> 전달 (Lọc -> Chuẩn bị -> Phân loại -> Phân tích/Sửa -> Truyền đạt).

Các bullet của **요구사항 분석 (Requirements Analysis)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **요구사항 분석 (Requirements Analysis)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **요구사항 검증 (Requirements Verification)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **요구사항 검증 (Requirements Verification)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 요구사항 검증 (Requirements Verification)

Bây giờ ta đi vào nội dung của **요구사항 검증 (Requirements Verification)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

**설계 및 구현 전에 베이스라인(Baseline) 설정** (Xác minh trước khi thiết kế/code để chốt Baseline làm chuẩn).
*   **검증 방법 (Các phương pháp kiểm tra):**
    *   수작업: 동료검토(Peer Review), 워크스루(Walkthrough), 인스펙션(Inspection).
    *   **프로토타이핑 (Prototyping):** 견본 제작 (Làm bản mẫu dùng thử).
    *   **테스트 설계 (Test Design):** 테스트 케이스 생성 (Viết test case trước để xem có test được không).
    *   **CASE 도구:** 자동화 도구로 일관성 분석 (Dùng phần mềm check logic).

Các bullet của **요구사항 검증 (Requirements Verification)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **요구사항 검증 (Requirements Verification)**, đừng bắt đầu lại từ số không. **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)

Phần nguồn của **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

1.  **완전성 (Completeness):** 누락 없이 (Đầy đủ).
2.  **일관성 (Consistency):** 충돌 없이 (Nhất quán).
3.  **명확성 (Unambiguity):** 똑같이 이해되게 (Rõ ràng).
4.  **기능성 (Functionality):** '어떻게'보다 '무엇을(What)' (Tập trung vào tính năng "Làm gì" hơn là "Làm như thế nào").
5.  **검증 가능성 (Verifiability):** 테스트 가능 여부 (Có thể kiểm chứng/test được).
6.  **추적 가능성 (Traceability):** 설계서와 연결 (Có thể truy xuất).
7.  **변경 용이성 (Easily Changeable):** 수정 용이 (Dễ thay đổi).

---

Phần **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Như vậy, **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **12. 요구사항 (Requirements)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **1. 현행 시스템 분석 (Current System Analysis)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.