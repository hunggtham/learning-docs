# 슬라이스 (Slice)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **슬라이스 (Slice)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **슬라이스 (Slice)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python 제어문 (Control Statements): if문, for문** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

슬라이스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**에서 만든 기준을 이어받아 **슬라이스 (Slice)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **슬라이스 (Slice)** và nối nó với **Python 제어문 (Control Statements): if문, for문**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 슬라이스 (Slice)

Ở bước 49/86, **슬라이스 (Slice)** xuất hiện như phần tiếp nối của **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **슬라이스 (Slice)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **형식** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “슬라이스 (Slice)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 문자열이나 리스트와 같은 순차형 객체에서 일부를 잘라(Slicing) 반환하는 기능입니다.
- **형식**: `객체명[초기위치:최종위치:증가값]`
  - `초기위치`에서 `최종위치 - 1` 까지의 요소들을 가져옵니다.
  - 인수를 생략하면 전체를 의미하거나, 기본값(처음, 끝, 1씩 증가)이 적용됩니다.

> **Vietnamese Explanation**:
> Slice (cắt lát) giúp lấy ra một phần của List hoặc String một cách dễ dàng. Nhớ là vị trí kết thúc không bao giờ được bao gồm (chỉ lấy đến `cuối - 1`).

**예시 / Ví dụ:**
```python
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:3])    # ['b', 'c']
print(a[0:5:2])  # ['a', 'c', 'e'] (Lấy cách nhau 2 bước)
print(a[::-1])   # Lật ngược list (âm là đi lùi)
```

Như vậy, **슬라이스 (Slice)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **Python 제어문 (Control Statements): if문, for문**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.