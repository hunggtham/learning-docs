# 258 - 261. 배열과 문자열 (Arrays & Strings)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **258 - 261. 배열과 문자열 (Arrays & Strings)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **258 - 261. 배열과 문자열 (Arrays & Strings)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **262 - 263. 포인터 (Pointers)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

배열과, 문자열

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**에서 만든 기준을 이어받아 **258 - 261. 배열과 문자열 (Arrays & Strings)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **258 - 261. 배열과 문자열 (Arrays & Strings)** và nối nó với **262 - 263. 포인터 (Pointers)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 258 - 261. 배열과 문자열 (Arrays & Strings)

Sau khi đã đặt nền bằng **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**, ta chuyển sang **258 - 261. 배열과 문자열 (Arrays & Strings)**. Đây là mắt xích 23/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **258 - 261. 배열과 문자열 (Arrays & Strings)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **배열 (Array)**, **2차원 배열**, **배열 초기화**, **배열 형태의 문자열 (C언어)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “258 - 261. 배열과 문자열 (Arrays & Strings)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **배열 (Array)**: **동일한 자료형**의 변수들을 연속된 메모리에 모아둔 것. `인덱스(첨자)`는 0부터 시작. 배열 이름 자체가 **첫 번째 요소의 시작 주소**를 의미.
- **2차원 배열**: 행과 열의 평면 구조 (예: `a[3][4]`는 3행 4열로 총 12개).
- **배열 초기화**: 선언과 동시에 값을 넣는 것. 크기를 생략해도 값의 개수만큼 자동 결정됨. 초기화되지 않은 빈칸은 자동으로 `0`으로 채워짐.
- **배열 형태의 문자열 (C언어)**: C언어는 문자열 자료형이 없어 `char` 배열을 사용. 문자열 끝에는 반드시 **널 문자(`\0`)**가 포함되어야 함 (글자수 + 1바이트 크기 필요).

**Giải thích (Vietnamese):**
Trong C, chuỗi "love" sẽ chiếm 5 ô nhớ (l, o, v, e, `\0`). Ký tự `\0` (Null) báo hiệu cho máy tính biết "đây là kết thúc của chuỗi".

---

Ta có thể khép mục **258 - 261. 배열과 문자열 (Arrays & Strings)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **262 - 263. 포인터 (Pointers)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.