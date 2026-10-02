# Python 클래스와 함수 (Class and Functions)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Python 클래스와 함수 (Class and Functions)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Python class/function với object, scope, parameter và reuse, để mã tổ chức theo trách nhiệm.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **Python 클래스와 함수 (Class and Functions)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **Python 클래스와 함수 (Class and Functions)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python 제어문: while문 (While Loop)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **Python 클래스와 함수 (Class and Functions)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

Python, 클래스와, 함수

> **Chuyển mạch:** Ở chặng này của **Python 클래스와 함수 (Class and Functions)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **Python 클래스 (Class) - 기초 (Cơ bản)**에서 만든 기준을 이어받아 **Python 클래스와 함수 (Class and Functions)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python 클래스와 함수 (Class and Functions)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Python 클래스와 함수 (Class and Functions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **Python 클래스와 함수 (Class and Functions)**, **Python 클래스와 함수 (Class and Functions)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Python 클래스와 함수 (Class and Functions)

Ở bước 52/86, **Python 클래스와 함수 (Class and Functions)** xuất hiện như phần tiếp nối của **Python 클래스 (Class) - 기초 (Cơ bản)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **Python 클래스와 함수 (Class and Functions)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **클래스 기반 객체 생성**, **함수 (클래스 없는 메소드)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 객체 생성 및 메소드 (Objects and Methods)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 객체 생성 및 메소드 (Objects and Methods)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 객체 생성 및 메소드 (Objects and Methods)

Bây giờ ta đi vào nội dung của **1. 객체 생성 및 메소드 (Objects and Methods)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. 객체 생성 및 메소드 (Objects and Methods)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **클래스 기반 객체 생성**: `변수명 = 클래스명()`
  - 예: `a = Cls()` (Cls 클래스의 객체 a를 생성)
  - 객체의 속성(변수)이나 메소드(함수)에 접근할 때는 마침표(`.`)를 사용합니다. (예: `a.x`, `a.chg()`)
- **함수 (클래스 없는 메소드)**: C언어의 함수처럼 클래스 없이 독립적으로 `def`를 이용해 메소드를 선언하고 사용할 수 있습니다.

> **Vietnamese Explanation**:
> Bạn có thể tạo đối tượng (object) từ một class bằng cú pháp `tên_biến = TênClass()`. Để truy cập biến hay hàm bên trong, ta dùng dấu chấm `.`. Ngoài ra, Python cũng cho phép định nghĩa các hàm độc lập không cần nằm trong class bằng từ khóa `def`.

**예시 / Ví dụ:**
```python
# Hàm độc lập (Function)
def calc(x, y):
    return x * y

a = calc(3, 4) # a = 12
```

Với **1. 객체 생성 및 메소드 (Objects and Methods)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **1. 객체 생성 및 메소드 (Objects and Methods)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **Python 클래스와 함수 (Class and Functions)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **Python 제어문: while문 (While Loop)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **Python 클래스와 함수 (Class and Functions)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
