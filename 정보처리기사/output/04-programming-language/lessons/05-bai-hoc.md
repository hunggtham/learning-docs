# 235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터, 타입, 크기

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**에서 만든 기준을 이어받아 **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)** và nối nó với **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)

Sau khi đã đặt nền bằng **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, ta chuyển sang **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**. Đây là mắt xích 5/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `byte`: 1바이트 (작은 숫자)
- `boolean`: 1바이트 (참/거짓)
- **`char`: 2바이트** (유니코드 지원으로 인해 C언어와 달리 2바이트를 차지함)
- `int`: 4바이트
- `long`: 8바이트 (C언어는 보통 4바이트지만 JAVA는 8바이트)
- `float`: 4바이트 / `double`: 8바이트

**Giải thích (Vietnamese):**
Java có 2 điểm khác biệt lớn với C: `char` chiếm 2 byte (để lưu bảng mã Unicode đa ngôn ngữ), và có kiểu `boolean` (chỉ lưu True/False).

---

Ta có thể khép mục **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.