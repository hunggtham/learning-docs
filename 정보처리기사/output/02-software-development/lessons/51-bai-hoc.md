# 48. 테스트 자동화 도구 (Test Automation Tools)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **48. 테스트 자동화 도구 (Test Automation Tools)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **48. 테스트 자동화 도구 (Test Automation Tools)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **49. 테스트 하네스 구성 요소 (Test Harness Components)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

테스트, 자동화, 도구

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **47. 테스트 오라클의 종류 (Types of Test Oracles)**에서 만든 기준을 이어받아 **48. 테스트 자동화 도구 (Test Automation Tools)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 48. 테스트 자동화 도구 (Test Automation Tools)

Từ **47. 테스트 오라클의 종류 (Types of Test Oracles)**, ta đã có điểm tựa để bước vào **48. 테스트 자동화 도구 (Test Automation Tools)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/95 trước khi đi vào chi tiết.

Để đọc **48. 테스트 자동화 도구 (Test Automation Tools)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **정적 분석 도구**, **테스트 케이스 생성 도구**, **테스트 실행 도구**, **성능 테스트 도구** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **정적 분석 도구**: 실행 없이 코드 표준/스타일/복잡도 검사.
* **테스트 케이스 생성 도구**: 자료 흐름도, 기능 테스트, 도메인 분석, 랜덤 등으로 TC 자동 생성.
* **테스트 실행 도구**: 데이터 주도(Data-driven) 및 키워드 주도(Keyword-driven) 스크립트 실행.
* **성능 테스트 도구**: 가상의 사용자를 만들어 부하를 줌.
* **테스트 통제 도구**: 테스트 계획, 형상 관리, 결함 관리.
* **테스트 하네스 도구**: 테스트 환경 시뮬레이션.
* **VI (Vietnamese) (Tiếng Việt):** Các công cụ tự động hóa kiểm thử: Phân tích tĩnh, Tạo TC, Chạy TC, Đo hiệu năng, Quản lý, Test Harness (Môi trường giả lập).

Điểm chốt của **48. 테스트 자동화 도구 (Test Automation Tools)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **49. 테스트 하네스 구성 요소 (Test Harness Components)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.