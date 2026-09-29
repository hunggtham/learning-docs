# 195-196. 분산 데이터베이스 목표 (Distributed DB Goals)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

분산, 데이터베이스, 목표

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **136-137. 분산 데이터베이스 (Distributed DB)**에서 만든 기준을 이어받아 **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 195-196. 분산 데이터베이스 목표 (Distributed DB Goals)

Sau khi đã đặt nền bằng **136-137. 분산 데이터베이스 (Distributed DB)**, ta chuyển sang **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**. Đây là mắt xích 35/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 위치 투명성(Location), 중복 투명성(Replication), 병행 투명성(Concurrency), 장애 투명성(Failure).
- **VI (Vietnamese) (Tiếng Việt):** Mục tiêu CSDL phân tán (Tính trong suốt về: vị trí, nhân bản, đồng thời, sự cố).

Ta có thể khép mục **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.