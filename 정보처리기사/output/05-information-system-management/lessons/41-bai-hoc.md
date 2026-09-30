# 핵심 258, 259, 260: 배열 (Array)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 258, 259, 260: 배열 (Array)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 258, 259, 260: 배열 (Array)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 261: C언어의 문자열 배열** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 배열

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 257: 분기/제어 (break, continue)**에서 만든 기준을 이어받아 **핵심 258, 259, 260: 배열 (Array)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 258, 259, 260: 배열 (Array)** và nối nó với **핵심 261: C언어의 문자열 배열**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 258, 259, 260: 배열 (Array)

Sau khi đã đặt nền bằng **핵심 257: 분기/제어 (break, continue)**, ta chuyển sang **핵심 258, 259, 260: 배열 (Array)**. Đây là mắt xích 41/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 258, 259, 260: 배열 (Array)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **특징**, **초기화** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 258, 259, 260: 배열 (Array)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 동일한 자료형의 여러 변수를 연속된 메모리 공간에 묶어서 하나의 이름으로 관리. (Mảng: Tập hợp các biến cùng kiểu).
- **특징**:
  - C언어에서 인덱스(첨자)는 **0부터 시작**. (Chỉ số bắt đầu từ 0).
  - 1차원 배열: `int a[5];` (Mảng 1 chiều).
  - 2차원 배열: `int a[3][4];` (행(Row)과 열(Column)로 구성 / Mảng 2 chiều: Dòng và Cột).
- **초기화**:
  - `int a[3] = {1, 2, 3};`
  - 지정한 요소 개수보다 초기값이 적으면 나머지는 **0으로 채워짐**. (Nếu khai báo thiếu giá trị, các phần tử còn lại tự động bằng 0).

Ta có thể khép mục **핵심 258, 259, 260: 배열 (Array)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **핵심 261: C언어의 문자열 배열**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.