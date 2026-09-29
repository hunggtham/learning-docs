# 49. 테스트 하네스 구성 요소 (Test Harness Components)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **49. 테스트 하네스 구성 요소 (Test Harness Components)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **49. 테스트 하네스 구성 요소 (Test Harness Components)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

테스트, 하네스, 구성, 요소

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **48. 테스트 자동화 도구 (Test Automation Tools)**에서 만든 기준을 이어받아 **49. 테스트 하네스 구성 요소 (Test Harness Components)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **49. 테스트 하네스 구성 요소 (Test Harness Components)** và nối nó với **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 49. 테스트 하네스 구성 요소 (Test Harness Components)

Ở bước 52/95, **49. 테스트 하네스 구성 요소 (Test Harness Components)** xuất hiện như phần tiếp nối của **48. 테스트 자동화 도구 (Test Automation Tools)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **49. 테스트 하네스 구성 요소 (Test Harness Components)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **드라이버(Driver)**, **스텁(Stub)**, **슈트(Suites)**, **케이스(Case)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **드라이버(Driver)**: 하위 모듈 호출 (상향식).
* **스텁(Stub)**: 가짜 하위 모듈 (하향식).
* **슈트(Suites)**: 테스트 케이스의 집합.
* **케이스(Case)**: 입력 값, 실행 조건, 기대 결과 명세.
* **스크립트(Script)**: 테스트 실행 절차 명세(자동화).
* **목 오브젝트(Mock Object)**: 조건부 입력에 따라 상황에 맞는 행위를 수행하는 가짜 객체.
* **VI (Vietnamese) (Tiếng Việt):** Thành phần của Test Harness: Driver (gọi cấp dưới), Stub (giả cấp dưới), Suites (tập hợp TC), Case (kịch bản), Script (mã chạy tự động), Mock Object (đối tượng giả).

Như vậy, **49. 테스트 하네스 구성 요소 (Test Harness Components)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.