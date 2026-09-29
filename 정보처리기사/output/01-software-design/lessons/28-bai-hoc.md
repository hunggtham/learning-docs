# 14. 객체지향 심화 (OOP chuyên sâu)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **14. 객체지향 심화 (OOP chuyên sâu)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **14. 객체지향 심화 (OOP chuyên sâu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

객체지향, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. 객체지향 (Hướng Đối Tượng - OOP)**에서 만든 기준을 이어받아 **14. 객체지향 심화 (OOP chuyên sâu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **14. 객체지향 심화 (OOP chuyên sâu)** và nối nó với **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 14. 객체지향 심화 (OOP chuyên sâu)

Ở bước 28/57, **14. 객체지향 심화 (OOP chuyên sâu)** xuất hiện như phần tiếp nối của **6. 객체지향 (Hướng Đối Tượng - OOP)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **14. 객체지향 심화 (OOP chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **다형성 (Polymorphism) 추가 설명** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **다형성 (Polymorphism) 추가 설명** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 다형성 (Polymorphism) 추가 설명

Bây giờ ta đi vào nội dung của **다형성 (Polymorphism) 추가 설명**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **오버로딩 (Overloading):** 인수를 받는 자료형과 개수를 달리하여 여러 기능을 정의. (Cùng tên hàm, khác tham số).
- **오버라이딩 (Overriding / 메소드 재정의):** 상위 클래스의 메소드 안의 코드를 자식 클래스에서 재정의. (Lớp con định nghĩa lại hàm của lớp cha).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **Over-load** = Chở thêm đồ (Thêm tham số). **Over-ride** = Lái đè lên vết xe cũ (Ghi đè nội dung hàm).

Với **다형성 (Polymorphism) 추가 설명**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **다형성 (Polymorphism) 추가 설명**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **14. 객체지향 심화 (OOP chuyên sâu)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.