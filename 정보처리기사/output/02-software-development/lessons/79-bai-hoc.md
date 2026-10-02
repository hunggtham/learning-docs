# 27. JSON 및 AJAX (JSON & AJAX)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **27. JSON 및 AJAX (JSON & AJAX)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối JSON/AJAX với serialization, request, response và asynchronous state, để giao tiếp web có hợp đồng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **27. JSON 및 AJAX (JSON & AJAX)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **27. JSON 및 AJAX (JSON & AJAX)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **27. JSON 및 AJAX (JSON & AJAX)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

JSON, AJAX

> **Chuyển mạch:** Ở chặng này của **27. JSON 및 AJAX (JSON & AJAX)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **25. 트립와이어 (tripwire)**에서 만든 기준을 이어받아 **27. JSON 및 AJAX (JSON & AJAX)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **27. JSON 및 AJAX (JSON & AJAX)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. JSON 및 AJAX (JSON & AJAX)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **27. JSON 및 AJAX (JSON & AJAX)**, **27. JSON 및 AJAX (JSON & AJAX)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 27. JSON 및 AJAX (JSON & AJAX)

Ở bước 79/101, **27. JSON 및 AJAX (JSON & AJAX)** xuất hiện như phần tiếp nối của **25. 트립와이어 (tripwire)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **27. JSON 및 AJAX (JSON & AJAX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **JSON (JavaScript Object Notation)**, **AJAX (Asynchronous JavaScript and XML)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “27. JSON 및 AJAX (JSON & AJAX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **JSON (JavaScript Object Notation)**: 속성-값 쌍(Attribute-Value Pairs)으로 이루어진 데이터 객체를 전달하기 위한 개방형 표준 포맷. 사람이 읽기 쉬움.
* **AJAX (Asynchronous JavaScript and XML)**: 자바스크립트를 이용한 비동기 통신 기술. 클라이언트-서버 간 XML(또는 JSON) 데이터를 교환 및 제어.
* **VI (Vietnamese) (Tiếng Việt):**
  * JSON: Định dạng dữ liệu dạng Key-Value dễ đọc.
  * AJAX: Công nghệ giao tiếp bất đồng bộ, tải dữ liệu mà không cần tải lại toàn bộ trang.
* **Example**: 좋아요 버튼을 눌렀을 때 페이지 이동 없이 하트가 채워지는 것이 AJAX 기술입니다.

Như vậy, **27. JSON 및 AJAX (JSON & AJAX)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **27. JSON 및 AJAX (JSON & AJAX)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
