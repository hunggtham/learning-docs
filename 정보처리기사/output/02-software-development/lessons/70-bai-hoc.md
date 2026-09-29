# 9. 스키마 3계층 (Three-Schema Architecture)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **9. 스키마 3계층 (Three-Schema Architecture)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **9. 스키마 3계층 (Three-Schema Architecture)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **14. 파레토 법칙 (Pareto Principle)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

스키마, 계층

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)**에서 만든 기준을 이어받아 **9. 스키마 3계층 (Three-Schema Architecture)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 9. 스키마 3계층 (Three-Schema Architecture)

Ở bước 70/95, **9. 스키마 3계층 (Three-Schema Architecture)** xuất hiện như phần tiếp nối của **핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **9. 스키마 3계층 (Three-Schema Architecture)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **외부 스키마 (External Schema)**, **개념 스키마 (Conceptual Schema)**, **내부 스키마 (Internal Schema)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **외부 스키마 (External Schema)**: 사용자나 프로그래머 입장에서 필요한 논리적 구조.
* **개념 스키마 (Conceptual Schema)**: 전체적인 논리적 구조, 개체 간 관계/제약조건, 보안/무결성 규칙.
* **내부 스키마 (Internal Schema)**: 물리적 저장장치 입장에서 본 구조 (레코드 형식, 물리적 순서).
* **VI (Vietnamese) (Tiếng Việt):**
  * External: Góc nhìn của người dùng (User view).
  * Conceptual: Cấu trúc logic tổng thể, quan hệ, bảo mật.
  * Internal: Cấu trúc lưu trữ vật lý.
* **Example**: DB의 전체 테이블 구조는 개념 스키마, 사용자가 보는 뷰(View)는 외부 스키마, 파일 저장 방식은 내부 스키마.
* 💡 **Mẹo ghi nhớ**: Ngoài (Người dùng) - Giữa/Khái niệm (Tổng thể logic) - Trong (Lưu trữ vật lý).

Như vậy, **9. 스키마 3계층 (Three-Schema Architecture)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **14. 파레토 법칙 (Pareto Principle)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.