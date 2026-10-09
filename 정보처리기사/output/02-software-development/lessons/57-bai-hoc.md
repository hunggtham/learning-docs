# 42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối test principles với oracle, independence, defect clustering và terms, để thiết kế test có cơ sở.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **43. 테스트 분류 방식 (Test Classification)** khi chuyển sang phần tiếp theo.

Mục tiêu giải thích các nguyên lý test như pesticide paradox, absence of errors và defect clustering; từ khóa khoanh vùng rủi ro và bằng chứng.

## 핵심 키워드 (Từ khóa)

애플리케이션, 테스트, 원리, 관련, 용어

Kiến thức liên kết đặt nguyên lý test trên nền test case và oracle; cách đọc tiếp theo giúp nối nguyên lý với quyết định thiết kế suite.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **35. 테스트 케이스 (Test Case)**에서 만든 기준을 이어받아 **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần nguyên lý dùng khung đó để nối lựa chọn test với rủi ro còn sót.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng giới hạn của mọi suite test; khi sang phân loại test, hãy chọn trục phân loại theo câu hỏi cần trả lời.

## 42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)

Từ **35. 테스트 케이스 (Test Case)**, ta đã có điểm tựa để bước vào **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 57/101 trước khi đi vào chi tiết.

Để đọc **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **결함 집중 (Defect Clustering) & 파레토 법칙**, **살충제 패러독스 (Pesticide Paradox)**, **오류-부재의 궤변 (Absence of Errors Fallacy)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **결함 집중 (Defect Clustering) & 파레토 법칙**: 오류의 80%는 20%의 모듈에 집중됨.
* **살충제 패러독스 (Pesticide Paradox)**: 동일한 테스트 케이스로 반복 테스트하면 더 이상 새로운 결함을 찾을 수 없음. 주기적인 테스트 케이스 개선 필요.
* **오류-부재의 궤변 (Absence of Errors Fallacy)**: 결함이 0이더라도 사용자의 요구사항을 만족시키지 못하면 품질이 높다고 할 수 없음.
* **확인 (Validation)** vs **검증 (Verification)**:
  * 확인(Validation): **사용자** 입장에서 요구사항에 맞는지 테스트.
  * 검증(Verification): **개발자** 입장에서 명세서(스펙)에 맞는지 테스트.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên lý kiểm thử:
  * Pesticide Paradox (Nghịch lý thuốc trừ sâu): Dùng mãi 1 kịch bản thì không bắt được lỗi mới.
  * Absence of Errors Fallacy: Không có lỗi không có nghĩa là phần mềm tốt nếu sai yêu cầu của khách hàng.
  * Validation: Đúng yêu cầu người dùng (Build the right product). Verification: Làm đúng kỹ thuật/tài liệu (Build the product right).
* **Example**: 로그인 버튼을 예쁘게 만들었지만(결함 없음), 고객이 원한 건 지문 인식 로그인이라면 이는 '오류-부재의 궤변'입니다.

Điểm chốt của **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **43. 테스트 분류 방식 (Test Classification)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
