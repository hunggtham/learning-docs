# 44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

화이트박스, 테스트, 검증, 기준

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **43. 테스트 분류 방식 (Test Classification)**에서 만든 기준을 이어받아 **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)

Sau khi đã đặt nền bằng **43. 테스트 분류 방식 (Test Classification)**, ta chuyển sang **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)**. Đây là mắt xích 47/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **문장(구문) 검증 기준 (Statement Coverage)**, **결정/분기 검증 기준 (Decision/Branch Coverage)**, **조건 검증 기준 (Condition Coverage)**, **분기/조건 기준 (Branch/Condition Coverage)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **문장(구문) 검증 기준 (Statement Coverage)**: 소스 코드의 **모든 구문**이 한 번 이상 수행되도록 설계.
* **결정/분기 검증 기준 (Decision/Branch Coverage)**: 모든 조건문에 대해 조건이 **True인 경우와 False인 경우**가 한 번 이상 수행되도록 설계.
* **조건 검증 기준 (Condition Coverage)**: 조건문에 포함된 **개별 조건식**의 결과가 T/F 한 번 이상 수행되도록 설계.
* **분기/조건 기준 (Branch/Condition Coverage)**: 위 두 가지를 모두 만족하는 설계.
* **VI (Vietnamese) (Tiếng Việt):** Các tiêu chí độ phủ (Coverage) trong kiểm thử hộp trắng: Bao phủ cú pháp (Statement), Bao phủ nhánh/quyết định (Branch - lệnh IF chạy cả T/F), Bao phủ điều kiện (Condition - từng điều kiện nhỏ chạy cả T/F), Bao phủ nhánh/điều kiện.
* 💡 **Mẹo ghi nhớ**: Statement = Dòng code. Branch = Ngã rẽ (IF). Condition = Điều kiện nhỏ trong IF.

Ta có thể khép mục **44. 화이트박스 테스트 검증 기준 (White Box Test Coverage Criteria)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **45. V-모델 (V-Model) 기반 애플리케이션 테스트 단계**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.