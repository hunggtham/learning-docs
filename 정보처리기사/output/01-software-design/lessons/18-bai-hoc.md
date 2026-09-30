# 7. UML 심화 (Advanced UML)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **7. UML 심화 (Advanced UML)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **7. UML 심화 (Advanced UML)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. 사용자 인터페이스 (Giao diện người dùng - UI)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

UML, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. UML 구성요소 상세 (UML Components Detail)**에서 만든 기준을 이어받아 **7. UML 심화 (Advanced UML)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **7. UML 심화 (Advanced UML)** và nối nó với **4. 사용자 인터페이스 (Giao diện người dùng - UI)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 7. UML 심화 (Advanced UML)

Từ **5. UML 구성요소 상세 (UML Components Detail)**, ta đã có điểm tựa để bước vào **7. UML 심화 (Advanced UML)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 18/69 trước khi đi vào chi tiết.

Để đọc **7. UML 심화 (Advanced UML)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **다이어그램 (Diagrams)**, **스테레오 타입 (Stereotype)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “7. UML 심화 (Advanced UML)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Do OMG chuẩn hóa từ phương pháp của Rumbaugh, Booch, Jacobson.
- **다이어그램 (Diagrams)**:
  - 구조적 (Structural / Tĩnh): Class, Object, Component, Deployment, Composite, Package.
  - 행위적 (Behavioral / Động): Use Case, Sequence, Communication, State, Activity, Timing.
- **스테레오 타입 (Stereotype)**: Mở rộng UML bằng dấu `<< >>` (Guillemet). Ví dụ: `<<include>>`, `<<extend>>`.

Điểm chốt của **7. UML 심화 (Advanced UML)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **4. 사용자 인터페이스 (Giao diện người dùng - UI)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.