# 2. 요구사항 정의 (Requirements Definition)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **2. 요구사항 정의 (Requirements Definition)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối requirements definition với stakeholder, scope, constraint và acceptance, để yêu cầu có thể xác minh.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 요구사항 정의 (Requirements Definition)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 요구사항 정의 (Requirements Definition)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định yêu cầu cần đạt; từ khóa khoanh vùng definition trước khi nối sang kiến thức liên kết.

## 핵심 키워드 (Từ khóa)

요구사항, 정의

Kiến thức liên kết đặt requirement definition trên nền requirements chuyên sâu; cách đọc tiếp theo giữ rõ stakeholder, scope, constraint và acceptance.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **10. 요구사항 심화 (Yêu cầu chuyên sâu)**에서 만든 기준을 이어받아 **2. 요구사항 정의 (Requirements Definition)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt tiêu chí đối tượng–điều kiện–hệ quả; phần definition dùng tiêu chí đó để biến nhu cầu thành yêu cầu có thể kiểm tra.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng tiêu chí xác minh và bàn giao; khi sang requirements analysis, hãy giữ lại scope và acceptance làm ranh giới.

## 2. 요구사항 정의 (Requirements Definition)

Ở bước 7/69, **2. 요구사항 정의 (Requirements Definition)** xuất hiện như phần tiếp nối của **10. 요구사항 심화 (Yêu cầu chuyên sâu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 요구사항 정의 (Requirements Definition)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **기능 요구사항 (Functional)**, **비기능 요구사항 (Non-Functional)**, **개발 프로세스 (Development Process)**, **명세 기법 (Specification Techniques)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 요구사항 정의 (Requirements Definition)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **기능 요구사항 (Functional)**: Chức năng hệ thống phải có (Ví dụ: Đăng nhập).
- **비기능 요구사항 (Non-Functional)**: Hiệu năng, bảo mật, chất lượng, ràng buộc (Ví dụ: Phản hồi dưới 1s).
- **개발 프로세스 (Development Process)**:
  1. 도출 (Elicitation) -> 2. 분석 (Analysis) -> 3. 명세 (Specification) -> 4. 확인/검증 (Validation).
- 💡 **Mẹo ghi nhớ**: Đ/P/M/X (Elicitation, Analysis, Spec, Validation) -> **Đi Phượt Một Xe**
- **명세 기법 (Specification Techniques)**:
  - 정형 (Formal): Ký hiệu toán học (Toán học, VDM, Z-schema). Rõ ràng nhưng khó hiểu với user.
  - 비정형 (Informal): Ngôn ngữ tự nhiên (Natural language, FSM, ERD). Dễ hiểu nhưng có thể mơ hồ.

Như vậy, **2. 요구사항 정의 (Requirements Definition)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **2. 요구사항 정의 (Requirements Definition)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
