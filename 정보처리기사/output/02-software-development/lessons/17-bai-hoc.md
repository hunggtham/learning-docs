# 32. 추가 해싱 함수 (Additional Hashing Functions)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **32. 추가 해싱 함수 (Additional Hashing Functions)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **32. 추가 해싱 함수 (Additional Hashing Functions)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

추가, 해싱, 함수

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **8. 주요 해싱 함수 (Hashing Functions)**에서 만든 기준을 이어받아 **32. 추가 해싱 함수 (Additional Hashing Functions)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **32. 추가 해싱 함수 (Additional Hashing Functions)** và nối nó với **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 32. 추가 해싱 함수 (Additional Hashing Functions)

Sau khi đã đặt nền bằng **8. 주요 해싱 함수 (Hashing Functions)**, ta chuyển sang **32. 추가 해싱 함수 (Additional Hashing Functions)**. Đây là mắt xích 17/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **32. 추가 해싱 함수 (Additional Hashing Functions)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **기수 변환법 (Radix)**, **대수적 코딩법 (Algebraic Coding)**, **무작위법 (Random)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **기수 변환법 (Radix)**: 키 숫자의 진수를 다른 진수로 변환.
* **대수적 코딩법 (Algebraic Coding)**: 다항식의 계수로 간주하여 나눈 나머지 사용.
* **무작위법 (Random)**: 난수를 발생시켜 홈 주소로 사용.
* **VI (Vietnamese) (Tiếng Việt):** Các hàm băm khác: Cơ số (Radix), Đại số (Algebraic), Ngẫu nhiên (Random).

Ta có thể khép mục **32. 추가 해싱 함수 (Additional Hashing Functions)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.