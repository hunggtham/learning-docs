# Python 기초 (Python Basics)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **Python 기초 (Python Basics)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **Python 기초 (Python Basics)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python 기본 문법 (Python Basic Syntax)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

Python, 기초

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **262 - 263. 포인터 (Pointers)**에서 만든 기준을 이어받아 **Python 기초 (Python Basics)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **Python 기초 (Python Basics)** và nối nó với **Python 기본 문법 (Python Basic Syntax)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## Python 기초 (Python Basics)

Ở bước 25/91, **Python 기초 (Python Basics)** xuất hiện như phần tiếp nối của **262 - 263. 포인터 (Pointers)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **Python 기초 (Python Basics)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **리스트 (List)**, **튜플 (Tuple)**, **range**, **range를 이용하는 방식 (Dùng range)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)

Bây giờ ta đi vào nội dung của **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **리스트 (List)**: 요소의 추가, 삭제, 변경 가능 (Có thể thêm, xóa, sửa phần tử).
- **튜플 (Tuple)**: 요소의 추가, 삭제, 변경 불가능함 (Không thể thay đổi phần tử).
- **range**: 연속된 숫자를 생성함 (Tạo dãy số liên tiếp).
  - *Example / Ví dụ*: List `[1, 2]`, Tuple `(1, 2)`.
  - 💡 *Mẹo ghi nhớ*: List dùng `[]` và linh hoạt. Tuple dùng `()` và cố định (bất biến).

Các ý về **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **185. Python의 리스트 (Python List / Danh sách trong Python)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **185. Python의 리스트 (Python List / Danh sách trong Python)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 185. Python의 리스트 (Python List / Danh sách trong Python)

Phần nguồn của **185. Python의 리스트 (Python List / Danh sách trong Python)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “185. Python의 리스트 (Python List / Danh sách trong Python)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 크기를 지정하지 않는다. 하나의 리스트에 다양한 자료형을 섞어 저장할 수 저장할 수 있다. (Không cần chỉ định kích thước. Có thể chứa nhiều kiểu dữ liệu khác nhau).
- 위치는 0부터 시작한다. (Chỉ số bắt đầu từ 0).
  - *Example / Ví dụ*: `a = [10, 'mike', 23.45]`
  - 💡 *Mẹo ghi nhớ*: Python List giống như một cái túi thần kỳ, có thể bỏ bất cứ thứ gì vào.

Với **185. Python의 리스트 (Python List / Danh sách trong Python)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **185. Python의 리스트 (Python List / Danh sách trong Python)**, đừng bắt đầu lại từ số không. **186. Python의 딕셔너리 (Dictionary / Từ điển)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **186. Python의 딕셔너리 (Dictionary / Từ điển)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 186. Python의 딕셔너리 (Dictionary / Từ điển)

Các ý ngay dưới **186. Python의 딕셔너리 (Dictionary / Từ điển)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “186. Python의 딕셔너리 (Dictionary / Từ điển)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 연관된 값을 묶어서 저장하는 용도. (Dùng để lưu trữ dữ liệu theo cặp Khóa - Giá trị).
- 위치값 대신 사용자가 원하는 키를 직접 지정하여 사용한다. (Dùng Khóa tự định nghĩa thay vì chỉ số số học).
  - *Example / Ví dụ*: `d = {'name': 'John', 'age': 25}`
  - 💡 *Mẹo ghi nhớ*: Key-Value (Khóa-Giá trị). Dùng `{}` giống như một từ điển thực sự (tra từ -> ra nghĩa).

Với **186. Python의 딕셔너리 (Dictionary / Từ điển)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**186. Python의 딕셔너리 (Dictionary / Từ điển)** vừa cho ta cách đặt câu hỏi. Bây giờ **187. Python의 Range (Python Range / Dãy số)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **187. Python의 Range (Python Range / Dãy số)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 187. Python의 Range (Python Range / Dãy số)

Bây giờ ta đi vào nội dung của **187. Python의 Range (Python Range / Dãy số)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “187. Python의 Range (Python Range / Dãy số)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 연속된 숫자를 생성하는 것. (Tạo dãy số liên tiếp).
  - `range(5)` -> 0, 1, 2, 3, 4
  - `range(4, 9)` -> 4, 5, 6, 7, 8
  - `range(1, 15, 3)` -> 1, 4, 7, 10, 13
  - 💡 *Mẹo ghi nhớ*: `range(start, stop, step)`. Bao gồm `start`, nhưng **không** bao gồm `stop`.

Các bullet của **187. Python의 Range (Python Range / Dãy số)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **187. Python의 Range (Python Range / Dãy số)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)

Phần nguồn của **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 객체에서 일부를 잘라 반환하는 기능. (Trích xuất một phần của chuỗi hoặc mảng).
- `a[1:3]`: Lấy từ index 1 đến 2.
- `a[0:5:2]`: Lấy từ 0 đến 4, bước nhảy 2.
- `a[3:]`: Lấy từ index 3 đến cuối.
- `a[:3]`: Lấy từ đầu đến index 2.
- `a[::-1]`: Đảo ngược mảng.
  - 💡 *Mẹo ghi nhớ*: `[start : stop : step]`. Giống range, không bao gồm `stop`.

Các bullet của **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)**, đừng bắt đầu lại từ số không. **182. Python의 input() 함수 (Python input() Function / Hàm nhập)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **182. Python의 input() 함수 (Python input() Function / Hàm nhập)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 182. Python의 input() 함수 (Python input() Function / Hàm nhập)

Các ý ngay dưới **182. Python의 input() 함수 (Python input() Function / Hàm nhập)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “182. Python의 input() 함수 (Python input() Function / Hàm nhập)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 키보드로 입력받아 변수에 저장하는 함수이다. (Nhập từ bàn phím và lưu vào biến).
- 입력되는 값은 기본적으로 문자열로 취급된다. (Giá trị mặc định luôn là chuỗi).
  - *Example / Ví dụ*: `a = input('Nhập tên:')`

Với **182. Python의 input() 함수 (Python input() Function / Hàm nhập)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**182. Python의 input() 함수 (Python input() Function / Hàm nhập)** vừa cho ta cách đặt câu hỏi. Bây giờ **183. Python의 print() 함수 (Python print() Function / Hàm in)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **183. Python의 print() 함수 (Python print() Function / Hàm in)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 183. Python의 print() 함수 (Python print() Function / Hàm in)

Bây giờ ta đi vào nội dung của **183. Python의 print() 함수 (Python print() Function / Hàm in)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “183. Python의 print() 함수 (Python print() Function / Hàm in)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 인수로 주어진 값을 출력한다. (In giá trị ra màn hình).
  - *Example / Ví dụ*: `print(82, 24, sep='-', end=',')` -> `82-24,`
  - 💡 *Mẹo ghi nhớ*: `sep` = phân cách giữa các đối số, `end` = ký tự kết thúc (mặc định là xuống dòng `\n`).

Với **183. Python의 print() 함수 (Python print() Function / Hàm in)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **183. Python의 print() 함수 (Python print() Function / Hàm in)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)

Phần nguồn của **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `input()` 함수는 무조건 문자열로 저장하므로, 숫자로 사용하려면 형 변환이 필요하다. (Vì `input()` trả về chuỗi, cần ép kiểu nếu muốn dùng số).
- 변환할 데이터가 1개: `a = int(input())`
- 변환할 데이터가 2개 이상: `a, b = map(int, input().split())`
  - 💡 *Mẹo ghi nhớ*: `split()` để cắt khoảng trắng, `map()` để ép tất cả sang kiểu nguyên `int`.

Với **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)**, đừng bắt đầu lại từ số không. **189. Python의 for문 (Python for loop)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **189. Python의 for문 (Python for loop)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 189. Python의 for문 (Python for loop)

Các ý ngay dưới **189. Python의 for문 (Python for loop)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “189. Python의 for문 (Python for loop)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **range를 이용하는 방식 (Dùng range)**: `for i in range(1, 11): sum = sum + i`
- **리스트를 이용하는 방식 (Dùng list)**: `for i in a:` (với `a` là list).
  - 💡 *Mẹo ghi nhớ*: `for item in tập_hợp`. Lặp qua từng phần tử.

Với **189. Python의 for문 (Python for loop)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**189. Python의 for문 (Python for loop)** vừa cho ta cách đặt câu hỏi. Bây giờ **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)

Bây giờ ta đi vào nội dung của **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 클래스 없이 메소드만 단독으로 사용할 수 있다. (Có thể sử dụng phương thức độc lập mà không cần lớp).
- 클래스를 사용하려면 속성과 메소드를 정의한 후 객체를 선언한다. (Để dùng lớp, định nghĩa thuộc tính và phương thức, sau đó khởi tạo đối tượng).
  - *Example / Ví dụ*: `def calc(x, y): return x * y` (Hàm độc lập). `class Cls: x = 10` (Lớp).
  - 💡 *Mẹo ghi nhớ*: Python hỗ trợ cả lập trình thủ tục (như C) và hướng đối tượng (OOP). Tham số đầu tiên của hàm trong lớp luôn là `self`.

Với **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **Python 기초 (Python Basics)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **Python 기본 문법 (Python Basic Syntax)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.