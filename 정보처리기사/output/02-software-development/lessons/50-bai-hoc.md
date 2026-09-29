# 47. 테스트 오라클의 종류 (Types of Test Oracles)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **47. 테스트 오라클의 종류 (Types of Test Oracles)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **47. 테스트 오라클의 종류 (Types of Test Oracles)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **48. 테스트 자동화 도구 (Test Automation Tools)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

테스트, 오라클의, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **46. 애플리케이션 테스트 프로세스 (Test Process)**에서 만든 기준을 이어받아 **47. 테스트 오라클의 종류 (Types of Test Oracles)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 47. 테스트 오라클의 종류 (Types of Test Oracles)

Sau khi đã đặt nền bằng **46. 애플리케이션 테스트 프로세스 (Test Process)**, ta chuyển sang **47. 테스트 오라클의 종류 (Types of Test Oracles)**. Đây là mắt xích 50/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **47. 테스트 오라클의 종류 (Types of Test Oracles)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **참(True) 오라클**, **샘플링(Sampling) 오라클**, **추정(Heuristic) 오라클**, **일관성 검사(Consistent) 오라클** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **참(True) 오라클**: 모든 입력값에 대해 결과를 제공 (모든 오류 검출).
* **샘플링(Sampling) 오라클**: 특정한 몇몇 입력값에 대해서만 결과 제공.
* **추정(Heuristic) 오라클**: 샘플링 + 나머지 값들은 추정(직관)으로 처리.
* **일관성 검사(Consistent) 오라클**: 변경 전후의 결과값이 동일한지 확인.
* **VI (Vietnamese) (Tiếng Việt):** Các loại Test Oracle: Chân lý (True - biết hết kết quả), Lấy mẫu (Sampling - biết vài cái), Ước lượng (Heuristic - kết hợp lấy mẫu và đoán), Nhất quán (Consistent - trước sau như một).

Ta có thể khép mục **47. 테스트 오라클의 종류 (Types of Test Oracles)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **48. 테스트 자동화 도구 (Test Automation Tools)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.