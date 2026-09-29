# 2. 요구사항 정의 (Requirements Definition)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **2. 요구사항 정의 (Requirements Definition)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **2. 요구사항 정의 (Requirements Definition)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

요구사항, 정의

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **10. 요구사항 심화 (Yêu cầu chuyên sâu)**에서 만든 기준을 이어받아 **2. 요구사항 정의 (Requirements Definition)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 2. 요구사항 정의 (Requirements Definition)

Từ **10. 요구사항 심화 (Yêu cầu chuyên sâu)**, ta đã có điểm tựa để bước vào **2. 요구사항 정의 (Requirements Definition)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 6/55 trước khi đi vào chi tiết.

Để đọc **2. 요구사항 정의 (Requirements Definition)** như một bài học cho người mới, hãy giữ câu hỏi: **một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **기능 요구사항 (Functional)**, **비기능 요구사항 (Non-Functional)**, **개발 프로세스 (Development Process)**, **명세 기법 (Specification Techniques)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **기능 요구사항 (Functional)**: Chức năng hệ thống phải có (Ví dụ: Đăng nhập).
- **비기능 요구사항 (Non-Functional)**: Hiệu năng, bảo mật, chất lượng, ràng buộc (Ví dụ: Phản hồi dưới 1s).
- **개발 프로세스 (Development Process)**: 
  1. 도출 (Elicitation) -> 2. 분석 (Analysis) -> 3. 명세 (Specification) -> 4. 확인/검증 (Validation).
- 💡 **Mẹo ghi nhớ**: Đ/P/M/X (Elicitation, Analysis, Spec, Validation) -> **Đi Phượt Một Xe**
- **명세 기법 (Specification Techniques)**:
  - 정형 (Formal): Ký hiệu toán học (Toán học, VDM, Z-schema). Rõ ràng nhưng khó hiểu với user.
  - 비정형 (Informal): Ngôn ngữ tự nhiên (Natural language, FSM, ERD). Dễ hiểu nhưng có thể mơ hồ.

Điểm chốt của **2. 요구사항 정의 (Requirements Definition)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **3. 요구사항 분석기법 및 자동화 도구 (Analysis Techniques & CASE)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.