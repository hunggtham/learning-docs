# 193. 뷰 (View)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **193. 뷰 (View)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **193. 뷰 (View)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **8. 서브쿼리와 뷰 (Truy vấn con và View)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

193. 뷰 (View)

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**에서 만든 기준을 이어받아 **193. 뷰 (View)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **193. 뷰 (View)** và nối nó với **8. 서브쿼리와 뷰 (Truy vấn con và View)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 193. 뷰 (View)

Sau khi đã đặt nền bằng **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**, ta chuyển sang **193. 뷰 (View)**. Đây là mắt xích 32/56 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **193. 뷰 (View)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 기본 테이블로부터 유도된 가상 테이블 (물리적 구현 X).
- 장점: 논리적 데이터 독립성, 보안 강화. 단점: 인덱스 불가, 뷰 정의 변경 불가, 갱신 제약.
- **VI (Vietnamese) (Tiếng Việt):** Khung nhìn (View). Bảng ảo. Ưu điểm: Độc lập dữ liệu, bảo mật. Nhược điểm: Không có index độc lập, khó cập nhật.

Ta có thể khép mục **193. 뷰 (View)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **8. 서브쿼리와 뷰 (Truy vấn con và View)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.