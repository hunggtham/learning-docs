# 3. 모듈 (Module)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 모듈 (Module)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **3. 모듈 (Module)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 모듈 (Module) & 독립성 (Independence)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

모듈

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**에서 만든 기준을 이어받아 **3. 모듈 (Module)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 모듈 (Module)

Ở bước 31/55, **3. 모듈 (Module)** xuất hiện như phần tiếp nối của **7. 설계 도구 및 모듈화 심화 (Công cụ thiết kế & Mô-đun hóa chuyên sâu)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **3. 모듈 (Module)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **결합도 (Coupling - Độ kết dính giữa các module)**, **응집도 (Cohesion - Độ gắn kết trong 1 module)**, **팬인 (Fan-In) / 팬아웃 (Fan-Out)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **결합도 (Coupling - Độ kết dính giữa các module)**: Càng thấp càng tốt.
  - 자료 (Data - Tốt nhất) < 스탬프 (Stamp) < 제어 (Control) < 외부 (External) < 공통 (Common) < 내용 (Content - Tệ nhất).
  - 💡 **Mẹo ghi nhớ**: T/S/C/N/C/N (Tốt -> Tệ) -> **Tính Sao Cho Nhẹ Cả Người**
- **응집도 (Cohesion - Độ gắn kết trong 1 module)**: Càng cao càng tốt.
  - 기능적 (Functional - Tốt nhất) > 순차적 (Sequential) > 통신적 (Communication) > 절차적 (Procedural) > 시간적 (Temporal) > 논리적 (Logical) > 우연적 (Coincidental - Tệ nhất).
  - 💡 **Mẹo ghi nhớ**: K/T/T/T/T/L/N (Tốt -> Tệ) -> **Không Thể Tin Thằng Trẻ Làm Ngốc**
- **팬인 (Fan-In) / 팬아웃 (Fan-Out)**:
  - Fan-in (Số module gọi nó): Cao thì tốt (tái sử dụng nhiều).
  - Fan-out (Số module nó gọi): Càng thấp càng tốt.

Như vậy, **3. 모듈 (Module)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **2. 모듈 (Module) & 독립성 (Independence)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.