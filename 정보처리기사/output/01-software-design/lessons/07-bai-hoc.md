# 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

요구사항, 분석기법, 자동화, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 요구사항 정의 (Requirements Definition)**에서 만든 기준을 이어받아 **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)

Ở bước 7/55, **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** xuất hiện như phần tiếp nối của **2. 요구사항 정의 (Requirements Definition)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô. Trong khối này, **자료 흐름도 (DFD - Data Flow Diagram)**, **자료 사전 (DD - Data Dictionary)**, **CASE 도구 (CASE Tools)**, **HIPO (Hierarchical Input Process Output)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **자료 흐름도 (DFD - Data Flow Diagram)**:
  - 프로세스 (Process - Tròn), 자료 흐름 (Data Flow - Mũi tên), 자료 저장소 (Data Store - Đường thẳng), 단말 (Terminator - Vuông).
- **자료 사전 (DD - Data Dictionary)**: 
  - `=`: Định nghĩa (is composed of)
  - `+`: Kết nối (and)
  - `( )`: Tùy chọn (Optional)
  - `[ | ]`: Lựa chọn (or)
  - `{ }`: Lặp lại (Iteration)
  - `**`: Ghi chú (Comment)
- **CASE 도구 (CASE Tools)**: SADT, SREM, PSL/PSA.
- **HIPO (Hierarchical Input Process Output)**: Phân tích Top-down (가시적 도표, 총체적 도표, 세부적 도표).

Như vậy, **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **1. 요구사항 개발 기법 (Requirements Elicitation Techniques)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.