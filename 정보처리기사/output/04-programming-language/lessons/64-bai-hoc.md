# 234. C언어의 구조체 (struct in C)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **234. C언어의 구조체 (struct in C)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **234. C언어의 구조체 (struct in C)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **238. 가비지 콜렉터 (Garbage Collector)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

언어의, 구조체

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **232. 배치 프로그램 (Batch Program)**에서 만든 기준을 이어받아 **234. C언어의 구조체 (struct in C)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **234. C언어의 구조체 (struct in C)** và nối nó với **238. 가비지 콜렉터 (Garbage Collector)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 234. C언어의 구조체 (struct in C)

Ở bước 64/78, **234. C언어의 구조체 (struct in C)** xuất hiện như phần tiếp nối của **232. 배치 프로그램 (Batch Program)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **234. C언어의 구조체 (struct in C)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 서로 다른 데이터 유형을 가진 변수들을 하나로 묶어 관리하는 사용자 정의 자료형.
- 배열(Array)은 **동일한 자료형**만 모으지만, 구조체(Struct)는 **상이한 자료형**을 모을 수 있음.

**Giải thích (Vietnamese):**
Struct (Cấu trúc) dùng để gom nhóm nhiều biến khác kiểu lại với nhau. Ví dụ tạo kiểu `SinhVien` gồm tên (chuỗi) và tuổi (số). Trong khi Mảng (Array) chỉ được lưu cùng một kiểu (hoặc toàn chuỗi, hoặc toàn số).

---

Như vậy, **234. C언어의 구조체 (struct in C)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **238. 가비지 콜렉터 (Garbage Collector)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.