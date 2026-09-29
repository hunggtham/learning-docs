# 27. JSON 및 AJAX (JSON & AJAX)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **27. JSON 및 AJAX (JSON & AJAX)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **27. JSON 및 AJAX (JSON & AJAX)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

JSON, AJAX

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **25. 트립와이어 (tripwire)**에서 만든 기준을 이어받아 **27. JSON 및 AJAX (JSON & AJAX)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 27. JSON 및 AJAX (JSON & AJAX)

Từ **25. 트립와이어 (tripwire)**, ta đã có điểm tựa để bước vào **27. JSON 및 AJAX (JSON & AJAX)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 78/95 trước khi đi vào chi tiết.

Để đọc **27. JSON 및 AJAX (JSON & AJAX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **JSON (JavaScript Object Notation)**, **AJAX (Asynchronous JavaScript and XML)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **JSON (JavaScript Object Notation)**: 속성-값 쌍(Attribute-Value Pairs)으로 이루어진 데이터 객체를 전달하기 위한 개방형 표준 포맷. 사람이 읽기 쉬움.
* **AJAX (Asynchronous JavaScript and XML)**: 자바스크립트를 이용한 비동기 통신 기술. 클라이언트-서버 간 XML(또는 JSON) 데이터를 교환 및 제어.
* **VI (Vietnamese) (Tiếng Việt):**
  * JSON: Định dạng dữ liệu dạng Key-Value dễ đọc.
  * AJAX: Công nghệ giao tiếp bất đồng bộ, tải dữ liệu mà không cần tải lại toàn bộ trang.
* **Example**: 좋아요 버튼을 눌렀을 때 페이지 이동 없이 하트가 채워지는 것이 AJAX 기술입니다.

Điểm chốt của **27. JSON 및 AJAX (JSON & AJAX)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **28. 선형 리스트 심화: 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.