# 262 - 263. 포인터 (Pointers)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **262 - 263. 포인터 (Pointers)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **262 - 263. 포인터 (Pointers)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python 기초 (Python Basics)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

포인터

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **258 - 261. 배열과 문자열 (Arrays & Strings)**에서 만든 기준을 이어받아 **262 - 263. 포인터 (Pointers)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **262 - 263. 포인터 (Pointers)** và nối nó với **Python 기초 (Python Basics)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 262 - 263. 포인터 (Pointers)

Sau khi đã đặt nền bằng **258 - 261. 배열과 문자열 (Arrays & Strings)**, ta chuyển sang **262 - 263. 포인터 (Pointers)**. Đây là mắt xích 23/78 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **262 - 263. 포인터 (Pointers)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **포인터 (Pointer)**, **포인터와 배열** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **포인터 (Pointer)**: 변수의 실제 **메모리 주소값**을 저장하는 특수 변수.
- `*` (간접 참조 연산자): 포인터가 가리키는 주소의 '값'.
- `&` (주소 연산자): 변수의 '주소'.
- **포인터와 배열**: 배열 이름은 포인터와 같음 (`배열명 == &배열명[0]`). 포인터 연산(`p+i`)으로 배열 요소에 접근 가능.

**Giải thích (Vietnamese):**
Pointer (Con trỏ) không lưu giá trị (như số 5), mà lưu "địa chỉ nhà" (ví dụ: nhà số 100A).
`&a` là lấy địa chỉ nhà của a. `*p` là mở cửa vào nhà để lấy đồ (lấy giá trị).

---

Ta có thể khép mục **262 - 263. 포인터 (Pointers)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **Python 기초 (Python Basics)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.