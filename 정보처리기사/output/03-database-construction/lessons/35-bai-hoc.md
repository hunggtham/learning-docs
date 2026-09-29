# 136-137. 분산 데이터베이스 (Distributed DB)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **136-137. 분산 데이터베이스 (Distributed DB)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **136-137. 분산 데이터베이스 (Distributed DB)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

분산, 데이터베이스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **191-192. 인덱스 (Index)**에서 만든 기준을 이어받아 **136-137. 분산 데이터베이스 (Distributed DB)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **136-137. 분산 데이터베이스 (Distributed DB)** và nối nó với **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 136-137. 분산 데이터베이스 (Distributed DB)

Sau khi đã đặt nền bằng **191-192. 인덱스 (Index)**, ta chuyển sang **136-137. 분산 데이터베이스 (Distributed DB)**. Đây là mắt xích 35/56 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **136-137. 분산 데이터베이스 (Distributed DB)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 논리적으로는 하나이나 물리적으로 분산된 데이터베이스.
- **목표 (Goals):** 위치 투명성 (Location), 중복 투명성 (Replication), 병행 투명성 (Concurrency), 장애 투명성 (Failure).
- **VI (Vietnamese) (Tiếng Việt):** Cơ sở dữ liệu phân tán. Tính trong suốt về: Vị trí, Nhân bản, Đồng thời, Lỗi.

Ta có thể khép mục **136-137. 분산 데이터베이스 (Distributed DB)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **195-196. 분산 데이터베이스 목표 (Distributed DB Goals)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.