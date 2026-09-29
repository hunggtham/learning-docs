# 193. 뷰 (View)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **193. 뷰 (View)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **193. 뷰 (View)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **8. 서브쿼리와 뷰 (Truy vấn con và View)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

193. 뷰 (View)

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**에서 만든 기준을 이어받아 **193. 뷰 (View)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 193. 뷰 (View)

Ở bước 31/55, **193. 뷰 (View)** xuất hiện như phần tiếp nối của **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **193. 뷰 (View)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 기본 테이블로부터 유도된 가상 테이블 (물리적 구현 X). 
- 장점: 논리적 데이터 독립성, 보안 강화. 단점: 인덱스 불가, 뷰 정의 변경 불가, 갱신 제약.
- **VI (Vietnamese) (Tiếng Việt):** Khung nhìn (View). Bảng ảo. Ưu điểm: Độc lập dữ liệu, bảo mật. Nhược điểm: Không có index độc lập, khó cập nhật.

Như vậy, **193. 뷰 (View)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **8. 서브쿼리와 뷰 (Truy vấn con và View)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.