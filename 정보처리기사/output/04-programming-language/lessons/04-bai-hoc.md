# 233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối data type size trong C/C++ với alignment, ABI và portability, để kích thước bộ nhớ được hiểu theo nền tảng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

데이터, 타입, 크기

> **Nối mạch:** Ở chặng này của **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**에서 만든 기준을 이어받아 **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)

Ở bước 4/91, **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** xuất hiện như phần tiếp nối của **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `char`: 1바이트 (문자 하나)
- `short`: 2바이트 (짧은 정수)
- `int` / `long`: 4바이트 (기본 정수)
- `long long`: 8바이트 (긴 정수)
- `float`: 4바이트 (실수)
- `double`: 8바이트 (정밀도 높은 실수)

**Giải thích (Vietnamese):**
Kích thước bộ nhớ các biến trong C/C++. Chữ cái (char) chiếm 1 byte. Số nguyên (int) chiếm 4 byte. Số thực (float) 4 byte, double (gấp đôi) là 8 byte.

---

Như vậy, **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
