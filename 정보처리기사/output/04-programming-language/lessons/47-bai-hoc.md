# 189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

구조적, 설계의, 주요, 기본, 원리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)**에서 만든 기준을 이어받아 **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)** và nối nó với **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)

Sau khi đã đặt nền bằng **309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)**, ta chuyển sang **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)**. Đây là mắt xích 47/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **추상화 (Abstraction)**, **정보 은닉 (Information Hiding)**, **프로그램 구조 (Program Structure)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모듈화 (Modularity)**: 시스템을 모듈 단위로 나눔.
- **추상화 (Abstraction)**: 포괄적 개념 먼저 설계 후 세분화 (기능, 제어, 자료 추상화).
- **정보 은닉 (Information Hiding)**: 모듈 내부의 세부 정보를 감추어 다른 모듈이 변경하지 못하게 함 (유지보수 용이).
- **프로그램 구조 (Program Structure)**: 제어 계층 구조 (트리 형태).
  - 공유도(Fan-In): 나를 호출하는 상위 모듈 수.
  - 제어도(Fan-Out): 내가 호출하는 하위 모듈 수.

**Giải thích (Vietnamese):**
Khi thiết kế phần mềm, ta chia nhỏ thành các hàm/chức năng (Modularity). Dùng "Che giấu thông tin" (Information Hiding) như tính đóng gói (Encapsulation) trong OOP để các hàm không can thiệp sai vào dữ liệu của nhau.
- Fan-In (Đi vào): Có bao nhiêu hàm gọi đến mình. Fan-In cao là tốt vì tính tái sử dụng cao.
- Fan-Out (Đi ra): Mình gọi bao nhiêu hàm khác. Fan-Out cao nghĩa là hàm này quá phức tạp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**모추정** (Mô - Trừu - Thông): **모**듈화(Modularity), **추**상화(Abstraction), **정**보 은닉(Information Hiding).

---

Ta có thể khép mục **189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.