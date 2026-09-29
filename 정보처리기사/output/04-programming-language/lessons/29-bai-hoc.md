# 라이브러리 및 예외 처리 (Libraries & Exception Handling)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **라이브러리 및 예외 처리 (Libraries & Exception Handling)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **라이브러리 및 예외 처리 (Libraries & Exception Handling)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

라이브러리, 예외, 처리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **264 - 274. 파이썬 문법 (Python Syntax & Basics)**에서 만든 기준을 이어받아 **라이브러리 및 예외 처리 (Libraries & Exception Handling)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 라이브러리 및 예외 처리 (Libraries & Exception Handling)

Sau khi đã đặt nền bằng **264 - 274. 파이썬 문법 (Python Syntax & Basics)**, ta chuyển sang **라이브러리 및 예외 처리 (Libraries & Exception Handling)**. Đây là mắt xích 29/77 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **라이브러리 및 예외 처리 (Libraries & Exception Handling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **stdio.h**, **math.h**, **string.h**, **stdlib.h** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **280. C언어의 표준 라이브러리 (C Standard Libraries / Thư viện chuẩn C)**. Hãy xác định **280. C언어의 표준 라이브러리 (C Standard Libraries / Thư viện chuẩn C)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 280. C언어의 표준 라이브러리 (C Standard Libraries / Thư viện chuẩn C)

Phần nguồn của **280. C언어의 표준 라이브러리 (C Standard Libraries / Thư viện chuẩn C)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **stdio.h**: 입출력 (`printf`, `scanf`, `fopen`).
- **math.h**: 수학 함수 (`sqrt`, `pow`, `abs`).
- **string.h**: 문자열 처리 (`strlen`, `strcpy`, `strcmp`).
- **stdlib.h**: 자료형 변환, 메모리 할당, 난수 (`atoi`, `rand`, `malloc`, `free`).
- **time.h**: 시간 처리 (`time`, `clock`).
  - 💡 *Mẹo ghi nhớ*: io = Input/Output, lib = Library (chung chung như cấp phát bộ nhớ), str = String.

Với **280. C언어의 표준 라이브러리 (C Standard Libraries / Thư viện chuẩn C)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **280. C언어의 표준 라이브러리 (C Standard Libraries / Thư viện chuẩn C)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **281. 예외 처리 (Exception Handling / Xử lý ngoại lệ)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **281. 예외 처리 (Exception Handling / Xử lý ngoại lệ)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 281. 예외 처리 (Exception Handling / Xử lý ngoại lệ)

Các ý ngay dưới **281. 예외 처리 (Exception Handling / Xử lý ngoại lệ)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 프로그램의 정상적인 실행을 방해하는 조건을 예외라고 한다. (Điều kiện làm gián đoạn chương trình gọi là ngoại lệ).
- 예외 발생 시 대처하는 루틴을 작성하는 것 (Viết mã để xử lý các sự cố này mà không làm sập chương trình).
- C++, Java, JS는 내장 기능 제공. (Các ngôn ngữ hiện đại có tích hợp sẵn như `try-catch`).
  - 💡 *Mẹo ghi nhớ*: Exception = Bắt lỗi chủ động.

Với **281. 예외 처리 (Exception Handling / Xử lý ngoại lệ)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **281. 예외 처리 (Exception Handling / Xử lý ngoại lệ)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **라이브러리 및 예외 처리 (Libraries & Exception Handling)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.