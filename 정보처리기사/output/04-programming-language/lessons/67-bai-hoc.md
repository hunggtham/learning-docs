# 209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **210. CASE (Computer-Aided Software Engineering)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

소프트웨어, 재공학

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**에서 만든 기준을 이어받아 **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** và nối nó với **210. CASE (Computer-Aided Software Engineering)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)

Ở bước 67/91, **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** xuất hiện như phần tiếp nối của **208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **주요 활동**, **분석 (Analysis)**, **재구성/개조 (Restructuring)**, **역공학 (Reverse Engineering)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기존 시스템을 수정 보완하거나 기능을 추가하여 성능을 향상 (예방 유지보수).
- 목적: 유지보수 비용 절감, 품질 향상, 소프트웨어 위기 해결.
- **주요 활동**:
  - **분석 (Analysis)**: 기존 명세서 확인.
  - **재구성/개조 (Restructuring)**: 기능은 그대로 두고 코드 구조만 향상 (Refactoring).
  - **역공학 (Reverse Engineering)**: 기존 코드를 분석하여 설계/명세서(문서)를 다시 뽑아내는 것 (복구). 가장 오래된 형태는 재문서화.
  - **이식 (Migration)**: 다른 OS나 하드웨어 환경으로 변환.

**Giải thích (Vietnamese):**
Reengineering là đập đi xây lại hoặc tu sửa lại nhà cũ cho hiện đại hơn.
- Restructuring: Cấu trúc lại bên trong nhà (mở rộng bếp, đập vách ngăn) nhưng nhìn bề ngoài vẫn là cái nhà đó.
- Reverse Engineering: Có một cái nhà cũ xây từ thời xưa không có bản vẽ. Nhìn vào cái nhà thực tế để vẽ lại bản vẽ kỹ thuật (Dịch ngược code thành tài liệu thiết kế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**분재역이** (Phân - Tái - Nghịch - Di): 분석, 재구성, 역공학, 이식.

---

Như vậy, **209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **210. CASE (Computer-Aided Software Engineering)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.