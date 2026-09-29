# 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

취약한, API, 사용

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**에서 만든 기준을 이어받아 **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** và nối nó với **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)

Sau khi đã đặt nền bằng **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**, ta chuyển sang **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**. Đây là mắt xích 80/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념**, **Tiếng Việt**, **예시 (Example)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 입력 길이·권한·오류 조건을 충분히 검증하지 않는 API를 사용하여 취약점을 만드는 것 (예: C언어의 `strcpy`, `strcat`).
- **Tiếng Việt**: Sử dụng các hàm không an toàn, dễ gây lỗi tràn bộ đệm (như `strcpy`).
- **예시 (Example)**:
  - (KR) 길이 제한이 없는 `strcpy()` 대신 입력 길이와 널 종료를 명시적으로 검증한다. `strncpy()`도 널 종료가 보장되지 않을 수 있으므로 무조건 안전한 대체재로 보지 않는다.
  - (VN) Dùng `strncpy()` (có giới hạn độ dài) thay cho `strcpy()` (copy không giới hạn).

---

Ta có thể khép mục **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **106 암호 알고리즘 (Cryptography Algorithms / Thuật toán mã hoá)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.