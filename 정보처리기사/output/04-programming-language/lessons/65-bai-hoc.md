# 206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

객체지향, 설계, 프로그래밍

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)**에서 만든 기준을 이어받아 **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)** và nối nó với **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)

Sau khi đã đặt nền bằng **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)**, ta chuyển sang **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**. Đây là mắt xích 65/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **설계 (OOD)**, **프로그래밍 (OOP)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **설계 (OOD)**: 분석 모델을 설계 모델로 변환 (추상화, 정보 은닉, 상속 등 활용). 가장 중요한 것은 **모듈화**. 설계 명세서를 작성.
- **프로그래밍 (OOP)**: 현실 세계에 가까운 방식으로 프로그래밍. 유지보수/재사용성 향상.
  - 객체지향성 언어: Simula (최초), Smalltalk, C++, Java 등.

---

Ta có thể khép mục **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.