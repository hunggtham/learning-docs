# 074. 데이터 입출력 (Data Input/Output)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **074. 데이터 입출력 (Data Input/Output)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **074. 데이터 입출력 (Data Input/Output)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터, 입출력

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **입출력 심화 (Input/Output - Advanced)**에서 만든 기준을 이어받아 **074. 데이터 입출력 (Data Input/Output)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **074. 데이터 입출력 (Data Input/Output)** và nối nó với **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 074. 데이터 입출력 (Data Input/Output)

Sau khi đã đặt nền bằng **입출력 심화 (Input/Output - Advanced)**, ta chuyển sang **074. 데이터 입출력 (Data Input/Output)**. Đây là mắt xích 14/78 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **074. 데이터 입출력 (Data Input/Output)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **표준 입력 함수 (C언어)**, **표준 출력 함수 (C언어)**, **서식 문자열 유형 (Format Strings)**, **이스케이프 문자** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **표준 입력 함수 (C언어)**: `scanf("서식 문자열", &변수명);` (변수의 주소 `&`를 붙임).
- **표준 출력 함수 (C언어)**: `printf("서식 문자열", 변수);`
- **서식 문자열 유형 (Format Strings)**:
  - `%d`: 정수형 10진수 (Decimal)
  - `%f`: 실수형 (Float)
  - `%c`: 문자형 1개 (Character)
  - `%s`: 문자열 (String)
- **이스케이프 문자**: `\n` (줄바꿈), `\t` (탭), `\b` (백스페이스).
- **JAVA 입출력**: `System.out.println()` (출력 후 자동 개행), `System.out.print()` (개행 없음).
- **Python 입출력**: `print(문자열, end='')` (끝에 개행 대신 다른 문자 삽입).

**Giải thích (Vietnamese):**
Khi lập trình bằng C, bạn dùng `scanf` để nhận dữ liệu người dùng nhập (nhớ có dấu `&` trước tên biến) và `printf` để in ra màn hình. Dấu `%d` dùng cho số nguyên, `%f` cho số thập phân. Java dùng `System.out.println()`. Python thì ngắn gọn hơn chỉ cần `print()`.

---

Ta có thể khép mục **074. 데이터 입출력 (Data Input/Output)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.