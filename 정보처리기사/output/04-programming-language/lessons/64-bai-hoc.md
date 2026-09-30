# 204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

객체지향, 분석, 럼바우, 기법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)**에서 만든 기준을 이어받아 **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)** và nối nó với **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)

Ở bước 64/91, **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)** xuất hiện như phần tiếp nối của **201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **객체지향 분석**, **분석 방법론**, **Booch**, **Jacobson** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **객체지향 분석**: 사용자의 요구사항을 분석하여 클래스(객체), 속성, 연산, 관계 등을 정의하는 작업.
- **분석 방법론**:
  - **Booch**: 미시적/거시적 개발 프로세스 모두 사용.
  - **Jacobson**: Use Case 강조.
  - **Coad/Yourdon**: E-R 다이어그램 사용.
  - **Wirfs-Brock**: 분석과 설계 간 구분 없음.
- **🌟 럼바우(Rumbaugh)의 분석 기법 (객체 모델링 기법, OMT)**:
  - 분석 순서: **객동기** (객체 -> 동적 -> 기능).
  1. **객체 모델링 (Object Modeling)**: 객체 식별, 구조 및 관계 규정 (객체 다이어그램 / 정보 모델링).
  2. **동적 모델링 (Dynamic Modeling)**: 시간 흐름에 따른 상태 변화, 제어 흐름 표현 (상태도).
  3. **기능 모델링 (Functional Modeling)**: 데이터 흐름을 중심으로 처리 과정 표현 (자료 흐름도, DFD).

**Giải thích (Vietnamese):**
Phương pháp phân tích của Rumbaugh là kinh điển nhất trong thi. Gồm 3 bước:
1. Object (Khách hàng, Tài khoản).
2. Dynamic (Tài khoản từ Đang mở -> Bị khóa khi nhập sai pass 3 lần).
3. Functional (Dữ liệu tiền chạy từ hệ thống ra ATM như thế nào).

**💡 Mẹo ghi nhớ (Mnemonics):**
**객동기** (Khách - Động - Cơ): **객**체(Object) -> **동**적(Dynamic) -> **기**능(Functional).

---

Như vậy, **204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.