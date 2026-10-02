# 12. 요구사항 (Requirements)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **12. 요구사항 (Requirements)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối requirements với stakeholder need, constraint và acceptance criteria, để yêu cầu trở thành đầu vào thiết kế có thể kiểm tra.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **12. 요구사항 (Requirements)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **12. 요구사항 (Requirements)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **A+ Deep Dive: 개발 모형 선택과 요구사항 검증** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **12. 요구사항 (Requirements)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

요구사항

> **Chuyển mạch:** Ở chặng này của **12. 요구사항 (Requirements)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)**에서 만든 기준을 이어받아 **12. 요구사항 (Requirements)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **12. 요구사항 (Requirements)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. 요구사항 (Requirements)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **12. 요구사항 (Requirements)**, **12. 요구사항 (Requirements)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 12. 요구사항 (Requirements)

Ở bước 10/69, **12. 요구사항 (Requirements)** xuất hiện như phần tiếp nối của **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **12. 요구사항 (Requirements)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **요구사항 분석 (Requirements Analysis)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **요구사항 분석 (Requirements Analysis)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 요구사항 분석 (Requirements Analysis)

Bây giờ ta đi vào nội dung của **요구사항 분석 (Requirements Analysis)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “요구사항 분석 (Requirements Analysis)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

*   **분류 (Phân loại):** 기능적(Functional) / 비기능적(Non-functional)으로 조직화.
*   **절차 (Quy trình 5 bước):** 선별(목록 작성) -> 자료 준비 -> 분류(기능/비기능) -> 분석 및 수정 -> 전달 (Lọc -> Chuẩn bị -> Phân loại -> Phân tích/Sửa -> Truyền đạt).

Các bullet của **요구사항 분석 (Requirements Analysis)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **요구사항 분석 (Requirements Analysis)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **요구사항 검증 (Requirements Verification)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **요구사항 검증 (Requirements Verification)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 요구사항 검증 (Requirements Verification)

Phần nguồn của **요구사항 검증 (Requirements Verification)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

**설계 및 구현 전에 베이스라인(Baseline) 설정** (Xác minh trước khi thiết kế/code để chốt Baseline làm chuẩn).
*   **검증 방법 (Các phương pháp kiểm tra):**
    *   수작업: 동료검토(Peer Review), 워크스루(Walkthrough), 인스펙션(Inspection).
    *   **프로토타이핑 (Prototyping):** 견본 제작 (Làm bản mẫu dùng thử).
    *   **테스트 설계 (Test Design):** 테스트 케이스 생성 (Viết test case trước để xem có test được không).
    *   **CASE 도구:** 자동화 도구로 일관성 분석 (Dùng phần mềm check logic).

Các bullet của **요구사항 검증 (Requirements Verification)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **요구사항 검증 (Requirements Verification)**, đừng bắt đầu lại từ số không. **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)

Các ý ngay dưới **요구사항 품질 기준 7개 (7 Tiêu chí chất lượng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

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

Như vậy, **12. 요구사항 (Requirements)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **A+ Deep Dive: 개발 모형 선택과 요구사항 검증**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **12. 요구사항 (Requirements)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
