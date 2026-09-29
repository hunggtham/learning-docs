# 10. 소프트웨어 설계 원리 (Software Design Principles)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **10. 소프트웨어 설계 원리 (Software Design Principles)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **10. 소프트웨어 설계 원리 (Software Design Principles)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 결합도 (Coupling - Độ phụ thuộc)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 설계, 원리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. 구조적 분석 도구 (Structured Analysis Tools)**에서 만든 기준을 이어받아 **10. 소프트웨어 설계 원리 (Software Design Principles)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 10. 소프트웨어 설계 원리 (Software Design Principles)

Ở bước 49/55, **10. 소프트웨어 설계 원리 (Software Design Principles)** xuất hiện như phần tiếp nối của **6. 구조적 분석 도구 (Structured Analysis Tools)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **10. 소프트웨어 설계 원리 (Software Design Principles)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **추상화 (Abstraction)**, **단계적 분해 (Stepwise Refinement)**, **정보 은닉 (Information Hiding)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **모듈화 (Modularity)**: 
  - Module quá nhỏ -> Chi phí tích hợp (Integration Cost) tăng.
  - Module quá lớn -> Chi phí phát triển từng module (Development Cost) tăng.
- **추상화 (Abstraction)**: 3 loại (과정 - Quá trình, 데이터 - Dữ liệu, 제어 - Điều khiển).
- **단계적 분해 (Stepwise Refinement)**: Đi từ trên xuống (Top-down).
- **정보 은닉 (Information Hiding)**: Giấu thông tin để giảm phụ thuộc.
- **시스템 타입 (System Types)**:
  - **대화형 (Interactive)**: Tương tác (VD: Web bán hàng).
  - **이벤트 중심 (Event-driven)**: Dựa trên sự kiện (VD: Chuông báo cháy).
  - **변환형 (Transformational)**: Biến đổi dữ liệu (VD: Trình biên dịch - Compiler).
  - **객체 영속형 (Object Persistence)**: Lưu trữ lâu dài (VD: Database Server).

# Subject 1 - Part 3

Như vậy, **10. 소프트웨어 설계 원리 (Software Design Principles)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 결합도 (Coupling - Độ phụ thuộc)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.