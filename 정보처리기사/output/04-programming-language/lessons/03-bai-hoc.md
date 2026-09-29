# 233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터, 타입, 크기

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**에서 만든 기준을 이어받아 **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** và nối nó với **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)

Từ **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**, ta đã có điểm tựa để bước vào **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/78 trước khi đi vào chi tiết.

Để đọc **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- `char`: 1바이트 (문자 하나)
- `short`: 2바이트 (짧은 정수)
- `int` / `long`: 4바이트 (기본 정수)
- `long long`: 8바이트 (긴 정수)
- `float`: 4바이트 (실수)
- `double`: 8바이트 (정밀도 높은 실수)

**Giải thích (Vietnamese):**
Kích thước bộ nhớ các biến trong C/C++. Chữ cái (char) chiếm 1 byte. Số nguyên (int) chiếm 4 byte. Số thực (float) 4 byte, double (gấp đôi) là 8 byte.

---

Điểm chốt của **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.