# Python 제어문 (Control Statements): if문, for문

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Python 제어문 (Control Statements): if문, for문**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy theo điều kiện, nhánh lặp và trạng thái biến để thấy if và for điều khiển luồng Python bằng những quy tắc khác nhau.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **Python 제어문 (Control Statements): if문, for문**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **Python 제어문 (Control Statements): if문, for문** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python 클래스 (Class) - 기초 (Cơ bản)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **Python 제어문 (Control Statements): if문, for문**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

Python, 제어문

> **Chuyển mạch:** Ở chặng này của **Python 제어문 (Control Statements): if문, for문**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **슬라이스 (Slice)**에서 만든 기준을 이어받아 **Python 제어문 (Control Statements): if문, for문**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python 제어문 (Control Statements): if문, for문**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Python 제어문 (Control Statements): if문, for문** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **Python 제어문 (Control Statements): if문, for문**, **Python 제어문 (Control Statements): if문, for문** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Python 제어문 (Control Statements): if문, for문

Sau khi đã đặt nền bằng **슬라이스 (Slice)**, ta chuyển sang **Python 제어문 (Control Statements): if문, for문**. Đây là mắt xích 50/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **Python 제어문 (Control Statements): if문, for문** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **형식**, **형식 1 (range 이용)**, **형식 2 (리스트 이용)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. if문 (if Statement / Câu lệnh điều kiện)**. Hãy xác định **1. if문 (if Statement / Câu lệnh điều kiện)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. if문 (if Statement / Câu lệnh điều kiện)

Phần nguồn của **1. if문 (if Statement / Câu lệnh điều kiện)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. if문 (if Statement / Câu lệnh điều kiện)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식**:
  ```python
  if 조건:
      실행할 문장
  ```
- 조건 뒤에 콜론(`:`)을 붙이고, 실행할 문장은 반드시 여백(Indentation)을 주어야 합니다.

Các bullet của **1. if문 (if Statement / Câu lệnh điều kiện)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. if문 (if Statement / Câu lệnh điều kiện)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. for문 (for Statement / Vòng lặp for)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. for문 (for Statement / Vòng lặp for)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. for문 (for Statement / Vòng lặp for)

Các ý ngay dưới **2. for문 (for Statement / Vòng lặp for)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2. for문 (for Statement / Vòng lặp for)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **형식 1 (range 이용)**:
  ```python
  for 변수 in range(초기값, 최종값, 증가값):
      실행할 문장
  ```
  - `최종값` - 1 까지 반복합니다.
- **형식 2 (리스트 이용)**:
  ```python
  for 변수 in 리스트:
      실행할 문장
  ```

> **Vietnamese Explanation**:
> `if` dùng để rẽ nhánh điều kiện. `for` dùng để lặp. Hàm `range(start, end, step)` sinh ra một dãy số từ `start` tới `end-1` với khoảng cách là `step`.

**예시 / Ví dụ:**
```python
# Tính tổng các số từ 1 đến 4
sum = 0
for i in range(1, 5):
    sum += i
print(sum) # Output: 10 (1+2+3+4)
```

Với **2. for문 (for Statement / Vòng lặp for)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **2. for문 (for Statement / Vòng lặp for)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **Python 제어문 (Control Statements): if문, for문** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **Python 클래스 (Class) - 기초 (Cơ bản)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **Python 제어문 (Control Statements): if문, for문**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
