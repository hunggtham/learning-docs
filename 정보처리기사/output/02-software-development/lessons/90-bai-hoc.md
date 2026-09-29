# 핵심 클린 코드 작성 원칙 (Clean Code Principles)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 클린 코드 작성 원칙 (Clean Code Principles)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 클린 코드 작성 원칙 (Clean Code Principles)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 클린, 코드, 작성, 원칙

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**에서 만든 기준을 이어받아 **핵심 클린 코드 작성 원칙 (Clean Code Principles)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 클린 코드 작성 원칙 (Clean Code Principles)** và nối nó với **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 클린 코드 작성 원칙 (Clean Code Principles)

Từ **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**, ta đã có điểm tựa để bước vào **핵심 클린 코드 작성 원칙 (Clean Code Principles)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 90/95 trước khi đi vào chi tiết.

Để đọc **핵심 클린 코드 작성 원칙 (Clean Code Principles)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **클린 코드 (Clean Code):** 누구나 쉽게 이해하고 수정 및 추가할 수 있는 단순 명료한 코드. (Code sạch: Dễ hiểu, dễ sửa, dễ thêm tính năng.)
- **배드 코드 (Bad code):** 프로그램의 로직이 복잡하고 이해하기 어려운 코드. (Code rác: Lộn xộn, logic phức tạp.)
- **외계인 코드 (Alien Code):** 매우 오래되거나 참고 문서 또는 개발자가 없어 유지보수 작업이 매우 어려운 코드. (Code "người ngoài hành tinh": Code cổ đại, người viết đã nghỉ việc, không có tài liệu, đụng vào là hỏng.)

| 작성 원칙 (Nguyên tắc) | 설명 (Giải thích) |
|---|---|
| **가독성 (Readability)** | 누구든지 코드를 쉽게 읽을 수 있도록 작성. 이해하기 쉬운 용어, 들여쓰기. (Dễ đọc: Tên biến rõ ràng, thụt lề chuẩn.) |
| **단순성 (Simplicity)** | 한 번에 한 가지를 처리하도록 작성, 최소 단위로 분리. (Đơn giản: Mỗi hàm chỉ làm 1 việc duy nhất.) |
| **의존성 배제 (Independence)** | 다른 모듈에 미치는 영향을 최소화. (Độc lập: Đổi chỗ này không làm sập chỗ khác.) |
| **중복성 최소화 (Minimizing Duplication)** | 코드의 중복을 최소화, 공통된 코드 사용. (DRY - Don't Repeat Yourself: Không copy-paste code.) |
| **추상화 (Abstraction)** | 상위 수준에선 간략하게, 상세 내용은 하위에서 구현. (Trừu tượng hóa: Cái chung ở trên, cái chi tiết ở dưới.) |

- **Vietnamese Explanation:** Clean Code là "đạo đức" của lập trình viên. Đừng viết Alien Code (code không ai hiểu nổi trừ người viết ban đầu).
- 💡 **Mẹo ghi nhớ (Mnemonics):** 5 nguyên tắc: Đọc - Đơn - Độc - Lặp - Trừu. (Đọc Đơn Độc Lặp Trừu (Đọc hiểu - Đơn giản - Độc lập - Không lặp - Trừu tượng)).

---

Điểm chốt của **핵심 클린 코드 작성 원칙 (Clean Code Principles)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.