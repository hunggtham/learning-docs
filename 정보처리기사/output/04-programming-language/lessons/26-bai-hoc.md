# Python 기본 문법 (Python Basic Syntax)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **Python 기본 문법 (Python Basic Syntax)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **Python 기본 문법 (Python Basic Syntax)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

Python, 기본, 문법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **Python 기초 (Python Basics)**에서 만든 기준을 이어받아 **Python 기본 문법 (Python Basic Syntax)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## Python 기본 문법 (Python Basic Syntax)

Sau khi đã đặt nền bằng **Python 기초 (Python Basics)**, ta chuyển sang **Python 기본 문법 (Python Basic Syntax)**. Đây là mắt xích 26/77 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **Python 기본 문법 (Python Basic Syntax)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **자료형 선언 없음**, **세미콜론 생략**, **연속 할당**, **코드 블록** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)**. Hãy xác định **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)

Phần nguồn của **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **자료형 선언 없음**: 변수 선언 시 타입을 명시하지 않는다. (Không cần khai báo kiểu dữ liệu).
- **세미콜론 생략**: 문장 끝에 `;`이 필요 없다. (Không cần dấu chấm phẩy ở cuối câu).
- **연속 할당**: `x, y, z = 10, 20, 30` (Có thể gán liên tiếp nhiều biến).
- **코드 블록**: 콜론(`:`)과 여백(Indentation)으로 구분한다. (Dùng dấu hai chấm và thụt lề để xác định khối lệnh, thay vì dùng `{ }`).
  - 💡 *Mẹo ghi nhớ*: Python yêu cầu thụt lề (thường là 4 spaces) vô cùng khắt khe. Sai thụt lề = Lỗi (IndentationError).

Với **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)

Các ý ngay dưới **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

*(Các khái niệm này đã được đề cập kỹ ở phần trước, dưới đây là tóm tắt nhanh các điểm chú ý)*:
- **`input()`**: Luôn trả về chuỗi. Dùng `int(input())` để ép kiểu. Đa trị: `map(int, input().split())`.
- **`print()`**: Có thể dùng `sep` (ký tự phân tách) và `end` (ký tự kết thúc).
- **리스트 (List)**: Khai báo bằng `[]` hoặc `list()`. Hỗ trợ chứa nhiều kiểu dữ liệu hỗn hợp.
- **딕셔너리 (Dictionary)**: Khai báo bằng `{}` hoặc `dict()`. Cấu trúc Key:Value.
- **슬라이스 (Slice)**: Cắt `[start:stop:step]`. Nếu bỏ trống `start` thì lấy từ đầu, bỏ trống `stop` thì lấy đến cuối.

Các bullet của **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **Python 기본 문법 (Python Basic Syntax)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **236. Python의 시퀀스 자료형 (Sequence Data Types in Python)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.