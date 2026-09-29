# Python 데이터 입·출력 함수 (Python Input/Output Functions)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **Python 데이터 입·출력 함수 (Python Input/Output Functions)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **Python 데이터 입·출력 함수 (Python Input/Output Functions)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **입력 값의 형변환 (Type Casting)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

Python, 데이터, 출력, 함수

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **Python의 기본 문법 (Python Basic Syntax)**에서 만든 기준을 이어받아 **Python 데이터 입·출력 함수 (Python Input/Output Functions)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **Python 데이터 입·출력 함수 (Python Input/Output Functions)** và nối nó với **입력 값의 형변환 (Type Casting)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## Python 데이터 입·출력 함수 (Python Input/Output Functions)

Ở bước 46/86, **Python 데이터 입·출력 함수 (Python Input/Output Functions)** xuất hiện như phần tiếp nối của **Python의 기본 문법 (Python Basic Syntax)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **Python 데이터 입·출력 함수 (Python Input/Output Functions)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **형식**, **형식** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. input( ) 함수** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. input( ) 함수** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. input( ) 함수

Bây giờ ta đi vào nội dung của **1. input( ) 함수**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. input( ) 함수” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Python의 표준 입력 함수로, 키보드로 입력받아 변수에 문자열(String) 형태로 저장합니다.
- **형식**: `변수 = input('출력문자')`

Với **1. input( ) 함수**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. input( ) 함수** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. print( ) 함수** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. print( ) 함수**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. print( ) 함수

Phần nguồn của **2. print( ) 함수** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. print( ) 함수” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식**: `print(출력값1, 출력값2, ..., sep='분리문자', end='종료문자')`
  - `sep`: 여러 값을 출력할 때 값 사이를 구분하는 문자 (기본값: 공백 한 칸)
  - `end`: 맨 마지막에 표시할 문자 (기본값: 줄 바꿈 `\n`)

> **Vietnamese Explanation**:
> Hàm `input()` dùng để nhận dữ liệu nhập từ bàn phím (mặc định luôn là chuỗi string). Hàm `print()` dùng để in ra màn hình, có thể tùy chỉnh dấu ngăn cách giữa các giá trị `sep` và ký tự kết thúc `end`.

**예시 / Ví dụ:**
```python
print(82, 24, sep='-', end=',')
# 출력/Output: 82-24,
```

Các ý về **2. print( ) 함수** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **2. print( ) 함수** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **Python 데이터 입·출력 함수 (Python Input/Output Functions)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **입력 값의 형변환 (Type Casting)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.