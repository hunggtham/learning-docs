# 포인터와 배열 (Pointer and Array)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **포인터와 배열 (Pointer and Array)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **포인터와 배열 (Pointer and Array)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **Python의 기본 문법 (Python Basic Syntax)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

포인터와, 배열

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 262: 포인터와 포인터 변수 (Pointer)**에서 만든 기준을 이어받아 **포인터와 배열 (Pointer and Array)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **포인터와 배열 (Pointer and Array)** và nối nó với **Python의 기본 문법 (Python Basic Syntax)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 포인터와 배열 (Pointer and Array)

Sau khi đã đặt nền bằng **핵심 262: 포인터와 포인터 변수 (Pointer)**, ta chuyển sang **포인터와 배열 (Pointer and Array)**. Đây là mắt xích 44/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **포인터와 배열 (Pointer and Array)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **특징** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “포인터와 배열 (Pointer and Array)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: C언어에서 배열을 포인터(Pointer/Con trỏ) 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있습니다.
- **특징**:
  - 배열 위치를 나타내는 첨자를 생략하고 배열의 대표명만 지정하면 배열의 첫 번째 요소의 주소를 지정하는 것과 같습니다. (예: `b = a;` 는 `b = &a[0];` 와 동일)
  - 배열 요소에 대한 주소를 지정할 때는 일반 변수와 동일하게 `&` 연산자를 사용합니다.
  - 배열의 요소가 포인터인 포인터형 배열을 선언할 수 있습니다.
  - 포인터 값에 정수를 더하면, 포인터가 가리키는 자료형의 크기(예: 정수형은 4바이트)만큼 물리적 주소가 증가합니다. (예: `p+1`은 4바이트 뒤의 주소)

> **Vietnamese Explanation**:
> Trong C, tên của mảng (array) chính là con trỏ (pointer) trỏ đến phần tử đầu tiên của mảng đó. Bạn có thể gán mảng cho một biến con trỏ, từ đó dùng con trỏ để truy cập các phần tử thay vì dùng chỉ số (index). Khi cộng 1 vào con trỏ, địa chỉ bộ nhớ sẽ tăng thêm số byte tương ứng với kiểu dữ liệu của nó (ví dụ int tăng 4 byte).

**예시 / Ví dụ:**
```c
int a[5] = {10, 11, 12, 13, 14};
int *p = a; // p trỏ tới a[0]
printf("%d", *(p+1)); // 출력/Output: 11
```

💡 **Mẹo ghi nhớ (Mnemonics):**
**Tên mảng = Địa chỉ đầu**. Mảng không cần `&` khi trỏ vào, nhưng phần tử thì cần (ví dụ `&a[0]`).

Ta có thể khép mục **포인터와 배열 (Pointer and Array)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **Python의 기본 문법 (Python Basic Syntax)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.