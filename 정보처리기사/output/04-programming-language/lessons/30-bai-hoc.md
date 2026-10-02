# 080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy nối thư viện với khả năng tái sử dụng, rồi nối exception với phát hiện, truyền và xử lý lỗi trong chương trình.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **279 - 280. 라이브러리 (Library)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

라이브러리와, 예외처리

> **Chuyển mạch:** Ở chặng này của **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름**에서 만든 기준을 이어받아 **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**, **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)

Từ **A+ Deep Dive: Java 비교 연산과 Python 제어 흐름**, ta đã có điểm tựa để bước vào **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/91 trước khi đi vào chi tiết.

Để đọc **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **C언어 표준 라이브러리**, **예외처리 (Exception Handling)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **C언어 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`).
  - `stdlib.h`: 자료형 변환 (`atoi`: char->int).
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`).
  - `math.h`: 수학 함수 (`sqrt`: 제곱근).
- **예외처리 (Exception Handling)**:
  - JAVA: `try { 실행 } catch (예외객체 e) { 에러처리 } finally { 무조건 실행 }`
  - Python: `try: ... except 예외객체: ... finally: ...`
  - 주요 예외객체: `NullPointerException` (객체가 없을 때), `ZeroDivisionError` (0으로 나눌 때).

---

Điểm chốt của **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **279 - 280. 라이브러리 (Library)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
