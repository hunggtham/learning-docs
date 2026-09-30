# Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **슬라이스 (Slice)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

Python, 자료구조

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **입력 값의 형변환 (Type Casting)**에서 만든 기준을 이어받아 **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** và nối nó với **슬라이스 (Slice)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)

Từ **입력 값의 형변환 (Type Casting)**, ta đã có điểm tựa để bước vào **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/86 trước khi đi vào chi tiết.

Để đọc **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **형식**, **형식**, **List**, **Dict** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 리스트 (List / Danh sách)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 리스트 (List / Danh sách)

Các ý ngay dưới **1. 리스트 (List / Danh sách)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “1. 리스트 (List / Danh sách)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- C/Java의 배열(Array)과 달리 크기를 지정하지 않으며, 정수/실수/문자열 등 다양한 자료형을 섞어서 저장할 수 있습니다.
- 위치(Index)는 0부터 시작합니다.
- **형식**: `리스트명 = [값1, 값2, ...]` 또는 `list([값1, 값2, ...])`

Với **1. 리스트 (List / Danh sách)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **1. 리스트 (List / Danh sách)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 딕셔너리 (Dictionary / Từ điển)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. 딕셔너리 (Dictionary / Từ điển)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. 딕셔너리 (Dictionary / Từ điển)

Bây giờ ta đi vào nội dung của **2. 딕셔너리 (Dictionary / Từ điển)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “2. 딕셔너리 (Dictionary / Từ điển)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 연관된 값을 묶어서 저장하는 용도로, 인덱스 대신 사용자가 원하는 값을 키(Key)로 지정해 사용합니다. 키-값 쌍(Key-Value pairs) 형태로 저장합니다.
- **형식**: `딕셔너리명 = {키1:값1, 키2:값2, ...}` 또는 `dict(...)`

> **Vietnamese Explanation**:
> List giống như Array nhưng linh hoạt hơn nhiều (có thể chứa nhiều kiểu dữ liệu cùng lúc, tự động thay đổi kích thước). Dictionary lưu dữ liệu theo dạng Cặp Chìa khóa - Giá trị (Key-Value), cho phép tra cứu nhanh theo Key.

**예시 / Ví dụ:**
```python
# List
my_list = [10, "mike", 23.45]
# Dictionary
my_dict = {"이름": "홍길동", "나이": 25}
my_dict["주소"] = "서울" # Thêm phần tử
```

💡 **Mẹo ghi nhớ (Mnemonics):**
- **List**: Ngoặc vuông `[]` (Ví dụ: cái hộp hình vuông chứa đủ đồ).
- **Dict**: Ngoặc nhọn `{}` (Có dạng `Key: Value`).

Với **2. 딕셔너리 (Dictionary / Từ điển)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **2. 딕셔너리 (Dictionary / Từ điển)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **슬라이스 (Slice)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.