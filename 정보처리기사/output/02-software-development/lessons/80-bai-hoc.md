# 33. DBMS (데이터베이스 관리 시스템)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **33. DBMS (데이터베이스 관리 시스템)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **33. DBMS (데이터베이스 관리 시스템)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **38. 릴리즈 노트 (Release Note)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

DBMS

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)**에서 만든 기준을 이어받아 **33. DBMS (데이터베이스 관리 시스템)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 33. DBMS (데이터베이스 관리 시스템)

Sau khi đã đặt nền bằng **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)**, ta chuyển sang **33. DBMS (데이터베이스 관리 시스템)**. Đây là mắt xích 80/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **33. DBMS (데이터베이스 관리 시스템)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **필수 기능 3가지**, **정의 기능 (Definition)**, **조작 기능 (Manipulation)**, **제어 기능 (Control)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* 사용자와 데이터베이스 사이에서 정보를 생성하고 데이터베이스를 관리해 주는 소프트웨어.
* **필수 기능 3가지**:
  * **정의 기능 (Definition)**: 데이터 형, 구조, 제약조건 등 명시.
  * **조작 기능 (Manipulation)**: 데이터 검색, 갱신, 삽입, 삭제(인터페이스 제공).
  * **제어 기능 (Control)**: 데이터 무결성 유지, 보안, 정확성 제어.
* **장점**: 데이터 중복 최소화, 독립성 보장, 일관성/무결성/보안 유지, 실시간 처리.
* **단점**: 전문가 부족, 전산화 비용 증가, 과부하 발생 시 백업/회복 어려움, 시스템 복잡.
* **VI (Vietnamese) (Tiếng Việt):** Hệ quản trị CSDL.
  * 3 chức năng: Định nghĩa (Cấu trúc), Thao tác (Thêm/Sửa/Xóa/Tìm), Điều khiển (Bảo mật, toàn vẹn).
  * Ưu điểm: Giảm trùng lặp, nhất quán. Nhược điểm: Tốn kém, phức tạp.
* **Example**: Oracle, MySQL 등이 대표적인 DBMS입니다.
* 💡 **Mẹo ghi nhớ**: Đ-T-Đ (Định nghĩa, Thao tác, Điều khiển) = D-M-C (Define, Manipulate, Control).

Ta có thể khép mục **33. DBMS (데이터베이스 관리 시스템)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **38. 릴리즈 노트 (Release Note)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.