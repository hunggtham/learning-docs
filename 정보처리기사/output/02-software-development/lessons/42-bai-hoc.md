# 17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

테스트, 오라클, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **16. 소프트웨어 테스트 단계 (Software Testing Phases)**에서 만든 기준을 이어받아 **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)** và nối nó với **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)

Từ **16. 소프트웨어 테스트 단계 (Software Testing Phases)**, ta đã có điểm tựa để bước vào **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/95 trước khi đi vào chi tiết.

Để đọc **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **테스트 오라클 (Test Oracle)**, **테스트 드라이버 (Test Driver)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **테스트 오라클 (Test Oracle)**: 테스트 결과가 참인지 판단하기 위해 사전에 정의된 참 값을 대입하여 비교. (참, 샘플링, 추정, 일관성 검사 오라클).
* **테스트 드라이버 (Test Driver)**: (상향식 테스트에서) 하위 모듈을 호출하고 매개 변수를 전달하여 결과를 도출하는 도구. (가짜 메인 프로그램).
* **VI (Vietnamese) (Tiếng Việt):**
  * Test Oracle: Cơ chế/Nguồn chân lý để xác định kết quả đúng hay sai.
  * Test Driver: Chương trình giả lập gọi module con (dùng trong Bottom-up).
* **Example**: 테스트 오라클은 정답지 역할을 합니다.
* 💡 **Mẹo ghi nhớ**: Oracle = Nhà tiên tri/Chân lý. Driver = Người lái xe (Gọi cấp dưới).

Điểm chốt của **17. 테스트 오라클 및 테스트 도구 (Test Oracle & Tools)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **20. 하향식 통합 테스트와 테스트 스텁 (Top-down Integration Test & Test Stub)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.