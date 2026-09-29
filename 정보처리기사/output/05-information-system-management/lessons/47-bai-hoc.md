# 입력 값의 형변환 (Type Casting)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **입력 값의 형변환 (Type Casting)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **입력 값의 형변환 (Type Casting)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

입력, 값의, 형변환

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **Python 데이터 입·출력 함수 (Python Input/Output Functions)**에서 만든 기준을 이어받아 **입력 값의 형변환 (Type Casting)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **입력 값의 형변환 (Type Casting)** và nối nó với **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 입력 값의 형변환 (Type Casting)

Sau khi đã đặt nền bằng **Python 데이터 입·출력 함수 (Python Input/Output Functions)**, ta chuyển sang **입력 값의 형변환 (Type Casting)**. Đây là mắt xích 47/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **입력 값의 형변환 (Type Casting)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **변환할 데이터가 1개일 때**, **변환할 데이터가 2개 이상일 때** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “입력 값의 형변환 (Type Casting)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `input()` 함수는 입력되는 값을 무조건 문자열(String)로 저장하므로, 숫자로 사용하기 위해서는 형(Type)을 변환해야 합니다.
- **변환할 데이터가 1개일 때**: `int()`, `float()` 사용
- **변환할 데이터가 2개 이상일 때**: `map()`과 `split()` 사용
  - 형식: `변수1, 변수2 = map(int, input().split())`

> **Vietnamese Explanation**:
> Vì `input()` trả về chuỗi, bạn phải ép kiểu sang số thực (`float`) hoặc số nguyên (`int`). Để nhập nhiều số cùng lúc trên một dòng, dùng `split()` để tách chuỗi và `map()` để ép kiểu hàng loạt cho tất cả các phần tử.

**예시 / Ví dụ:**
```python
a, b = map(int, input("Nhập 2 số: ").split())
# Nếu nhập "10 20", a=10, b=20
```

💡 **Mẹo ghi nhớ (Mnemonics):**
**M.I.S** - **M**ap **I**nt **S**plit để nhập nhiều số nguyên cùng lúc.

Ta có thể khép mục **입력 값의 형변환 (Type Casting)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **Python 자료구조 (Data Structures): 리스트(List)와 딕셔너리(Dictionary)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.