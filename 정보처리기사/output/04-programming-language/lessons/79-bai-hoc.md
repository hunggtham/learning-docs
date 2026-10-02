# 250. JAVA에서의 표준 출력 (Standard Output in JAVA)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy theo luồng `System.out`, bộ đệm và định dạng để thấy dữ liệu Java đi từ chương trình ra thiết bị như thế nào.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **251. 단순 if문 (Simple if Statement)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

에서의, 표준, 출력

> **Chuyển mạch:** Ở chặng này của **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **238. 가비지 콜렉터 (Garbage Collector)**에서 만든 기준을 이어받아 **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**, **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 250. JAVA에서의 표준 출력 (Standard Output in JAVA)

Ở bước 79/91, **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** xuất hiện như phần tiếp nối của **238. 가비지 콜렉터 (Garbage Collector)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “250. JAVA에서의 표준 출력 (Standard Output in JAVA)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `System.out.print()`: 형식 없이 그대로 출력 (줄바꿈 없음).
- `System.out.println()`: 출력 후 자동으로 줄바꿈(Enter) 수행.
- `System.out.printf()`: C언어처럼 서식 문자열(`%d` 등)을 사용하여 출력.
- 문자열과 변수를 섞어 쓸 때 `+` 연산자로 연결 가능.

---

Như vậy, **250. JAVA에서의 표준 출력 (Standard Output in JAVA)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **251. 단순 if문 (Simple if Statement)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **250. JAVA에서의 표준 출력 (Standard Output in JAVA)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
