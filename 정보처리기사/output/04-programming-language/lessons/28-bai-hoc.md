# A+ Deep Dive: Java 비교 연산과 Python 제어 흐름

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **라이브러리 및 예외 처리 (Libraries & Exception Handling)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

Deep, Dive, Java, 비교, 연산과, Python, 제어, 흐름

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **264 - 274. 파이썬 문법 (Python Syntax & Basics)**에서 만든 기준을 이어받아 **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름** và nối nó với **라이브러리 및 예외 처리 (Libraries & Exception Handling)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## A+ Deep Dive: Java 비교 연산과 Python 제어 흐름

Ở bước 28/78, **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름** xuất hiện như phần tiếp nối của **264 - 274. 파이썬 문법 (Python Syntax & Basics)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. Java의 `==`는 문맥을 먼저 본다** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. Java의 `==`는 문맥을 먼저 본다** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. Java의 `==`는 문맥을 먼저 본다

Bây giờ ta đi vào nội dung của **1. Java의 `==`는 문맥을 먼저 본다**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

```java
int a = 1;
double b = 1.0;
System.out.println(a == b);        // true: 수치 승격 후 비교
String x = new String("A");
String y = new String("A");
System.out.println(x == y);        // false: 서로 다른 객체 참조
System.out.println(x.equals(y));   // true: 내용 비교
```

- 숫자형 피연산자는 binary numeric promotion 후 비교한다.
- 참조형 `==`는 같은 객체를 가리키는지 비교하고, 문자열 내용 비교에는 `equals`를 사용한다.
- `a == b == c`는 “세 값이 모두 같은가”가 아니라 왼쪽부터 계산되므로 별도 비교식이 필요하다.

Với **1. Java의 `==`는 문맥을 먼저 본다**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. Java의 `==`는 문맥을 먼저 본다** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. Python `for`와 `while`의 trace 포인트** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. Python `for`와 `while`의 trace 포인트**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. Python `for`와 `while`의 trace 포인트

Phần nguồn của **2. Python `for`와 `while`의 trace 포인트** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

```python
items = [1, 2, 3]
total = 0
for value in items:
    if value == 2:
        continue
    total += value
print(total)  # 4
```

`continue`는 현재 반복의 나머지를 건너뛰고 다음 반복으로 이동한다. `break`는 반복문 전체를 종료한다. 문제를 풀 때 초기값, 조건 검사 시점, 증감/자료 갱신 위치를 표로 추적한다.

> **시험 함정:** Java 문자열의 `==`와 `equals`, Python의 `continue`와 `break`를 섞지 않는다.

Với **2. Python `for`와 `while`의 trace 포인트**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **2. Python `for`와 `while`의 trace 포인트**, đừng bắt đầu lại từ số không. **자주 혼동하는 판별 포인트** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **자주 혼동하는 판별 포인트** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 자주 혼동하는 판별 포인트

Các ý ngay dưới **자주 혼동하는 판별 포인트** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- C 반복문은 초기값·조건·증감식과 실제 접근 인덱스를 따로 표로 적는다. `i += 2`이면 짝수 인덱스만 방문할 수 있다.
- Java의 후위 감소 `y--`는 비교에 현재 값을 사용한 뒤 값을 줄인다. 반복 종료 시점의 변수값을 마지막 조건 평가까지 반영한다.
- Python `split(delimiter)`는 지정한 구분자로 문자열을 나누고, `map(int, ...)`는 각 조각을 정수로 바꾼다.
- IPv6는 128비트 주소와 anycast를 사용한다. IPv6 패킷/헤더 크기를 무제한으로 해석하거나 IPv4의 32비트와 혼동하지 않는다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **자주 혼동하는 판별 포인트** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **라이브러리 및 예외 처리 (Libraries & Exception Handling)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.