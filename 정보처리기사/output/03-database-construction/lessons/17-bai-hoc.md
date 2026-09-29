# 123-125. 정규화 (Normalization)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **123-125. 정규화 (Normalization)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **123-125. 정규화 (Normalization)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

정규화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **116-121. 관계대수 (Relational Algebra)**에서 만든 기준을 이어받아 **123-125. 정규화 (Normalization)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 123-125. 정규화 (Normalization)

Sau khi đã đặt nền bằng **116-121. 관계대수 (Relational Algebra)**, ta chuyển sang **123-125. 정규화 (Normalization)**. Đây là mắt xích 17/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **123-125. 정규화 (Normalization)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 데이터 중복을 배제하여 이상(Anomaly: 삽입, 삭제, 갱신 이상) 발생을 방지하는 과정. 논리적 설계 단계에서 수행.
- **1NF:** 도메인이 원자값 (Domain is Atomic).
- **2NF:** 부분적 함수 종속 제거 (Remove Partial Dependency).
- **3NF:** 이행적 함수 종속 제거 (Remove Transitive Dependency).
- **BCNF:** 결정자이면서 후보키가 아닌 것 제거.
- **4NF:** 다치 종속 제거 (Remove Multivalued Dependency).
- **5NF:** 조인 종속성 이용.
- **VI (Vietnamese) (Tiếng Việt):** Chuẩn hóa. Giảm thiểu dư thừa dữ liệu để ngăn ngừa dị thường (Anomaly).
- 💡 **Mẹo ghi nhớ:** Nguyên-Phần-Bắc-Quyết-Đa-Chung (Nguyên tử -> Từng phần -> Bắc cầu -> Quyết định -> Đa trị -> Chung).

Ta có thể khép mục **123-125. 정규화 (Normalization)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.