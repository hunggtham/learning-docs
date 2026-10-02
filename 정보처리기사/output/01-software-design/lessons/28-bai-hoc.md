# 1. 객체지향 설계 5대 원칙 (SOLID)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **1. 객체지향 설계 5대 원칙 (SOLID)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối data modeling với entity, relation, normalization và query, để dữ liệu có cấu trúc trước khi chọn công cụ.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **1. 객체지향 설계 5대 원칙 (SOLID)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **1. 객체지향 설계 5대 원칙 (SOLID)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **1. 객체지향 설계 5대 원칙 (SOLID)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

객체지향, 설계, 원칙

> **Chuyển mạch:** Ở chặng này của **1. 객체지향 설계 5대 원칙 (SOLID)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 객체지향 (OOP - Object Oriented Programming)**에서 만든 기준을 이어받아 **1. 객체지향 설계 5대 원칙 (SOLID)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **1. 객체지향 설계 5대 원칙 (SOLID)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1. 객체지향 설계 5대 원칙 (SOLID)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **1. 객체지향 설계 5대 원칙 (SOLID)**, **1. 객체지향 설계 5대 원칙 (SOLID)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 1. 객체지향 설계 5대 원칙 (SOLID)

Ở bước 28/69, **1. 객체지향 설계 5대 원칙 (SOLID)** xuất hiện như phần tiếp nối của **2. 객체지향 (OOP - Object Oriented Programming)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **1. 객체지향 설계 5대 원칙 (SOLID)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 시스템의 변경이나 확장에 유연하게 대응하기 위해 지켜야 할 5가지 원칙 (5 nguyên tắc thiết kế hướng đối tượng giúp hệ thống linh hoạt trước các thay đổi và mở rộng).

*   **SRP (Single Responsibility Principle - 단일 책임 원칙):**
    *   **Korean:** 객체는 '단 하나의 책임'만 가져야 함. 클래스를 수정해야 할 이유는 단 하나여야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đơn trách nhiệm. Một đối tượng (hoặc lớp) chỉ nên có một trách nhiệm duy nhất. Lý do để sửa đổi một lớp chỉ nên có một.
    *   **Example:**
        *   *KR:* 보고서를 생성하는 클래스와 출력하는 클래스를 분리.
        *   *VN:* Tách biệt lớp tạo báo cáo và lớp in báo cáo, không để chung một lớp.
*   **OCP (Open-Closed Principle - 개방-폐쇄 원칙):**
    *   **Korean:** 기능 추가에는 열려(Open) 있어야 하고, 기존 코드 변경에는 닫혀(Closed) 있어야 함. 인터페이스로 캡슐화.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đóng - Mở. Mở rộng chức năng thì dễ dàng (Open), nhưng không được sửa đổi mã nguồn hiện tại (Closed). Thường dùng Interface để đóng gói.
    *   **Example:**
        *   *KR:* 결제 수단(카드, 페이 등)을 인터페이스로 구현하여 새로운 결제 수단 추가 시 기존 코드 수정 없이 확장.
        *   *VN:* Dùng Interface cho phương thức thanh toán, khi thêm phương thức mới (ví dụ: ví điện tử) thì không cần sửa mã cũ.
*   **LSP (Liskov Substitution Principle - 리스코프 치환 원칙):**
    *   **Korean:** 자식 클래스는 최소한 부모 클래스의 행위를 수행할 수 있어야 함. 부모의 의도를 훼손하지 않고 확장.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Thay thế Liskov. Lớp con phải có thể thay thế lớp cha mà không làm hỏng tính đúng đắn của chương trình. Lớp con chỉ nên mở rộng, không làm sai lệch ý định của lớp cha.
    *   **Example:**
        *   *KR:* 새(Bird) 부모 클래스를 상속받은 펭귄(Penguin)이 날기(fly) 메서드를 가지면 LSP 위반.
        *   *VN:* Chim cánh cụt kế thừa từ lớp Chim, nhưng nếu gọi hàm bay() sẽ bị lỗi, vi phạm LSP. Cần thiết kế lại.
*   **ISP (Interface Segregation Principle - 인터페이스 분리 원칙):**
    *   **Korean:** 사용하지 않는 인터페이스에 의존하지 않도록 분리.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Phân tách Interface. Không nên ép các lớp phụ thuộc vào những interface mà chúng không sử dụng. Hãy chia nhỏ interface khổng lồ thành các interface cụ thể.
    *   **Example:**
        *   *KR:* 복합기 인터페이스를 프린터, 스캐너, 팩스 인터페이스로 분리.
        *   *VN:* Tách interface của máy photocopy đa năng thành các interface riêng: In, Quét, Fax.
*   **DIP (Dependency Inversion Principle - 의존 역전 원칙):**
    *   **Korean:** 구체적인 클래스보다 추상화된 클래스(인터페이스)에 의존해야 함.
    *   **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc Đảo ngược phụ thuộc. Các module cấp cao không nên phụ thuộc vào module cấp thấp, cả hai nên phụ thuộc vào abstractions (interface).
    *   **Example:**
        *   *KR:* 자동차가 스노우타이어(구체) 대신 타이어(추상) 인터페이스에 의존.
        *   *VN:* Lớp xe hơi phụ thuộc vào interface "Lốp xe" nói chung, thay vì phụ thuộc trực tiếp vào "Lốp đi tuyết".

💡 **Mẹo ghi nhớ (Mnemonics):** **SOLID** (S = Single, O = Open, L = Liskov, I = Interface, D = Dependency)

---

Như vậy, **1. 객체지향 설계 5대 원칙 (SOLID)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **1. 객체지향 설계 5대 원칙 (SOLID)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
