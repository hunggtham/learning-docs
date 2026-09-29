# 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 재사용, 기법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**에서 만든 기준을 이어받아 **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** và nối nó với **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

Ở bước 88/95, **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** xuất hiện như phần tiếp nối của **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **재사용 (Reuse):** 이미 개발되어 인정받았던 소프트웨어의 전체 또는 일부분을 다시 사용하는 기법. (Sử dụng lại code/phần mềm cũ đã được kiểm chứng để tiết kiệm thời gian, chi phí và giảm lỗi.)
- **Phân loại theo kỹ thuật:**
  - **분석 (Analysis):** Hiểu code cũ để chọn cái cần tái sử dụng.
  - **재구조 (Restructuring):** Đổi cấu trúc, không đổi chức năng.
  - **역공학 (Reverse Engineering):** Dịch ngược từ code ra bản thiết kế.
  - **이식 (Migration):** Chuyển sang môi trường / phần cứng mới.
  - **재개발 (Re-Development):** Đập đi xây lại có tham khảo cái cũ.
- **Phân loại theo phạm vi:**
  - Hàm & Đối tượng (Function/Class), Component, Ứng dụng (Application).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Reverse Engineering (Dịch ngược) = Từ Code -> Bản thiết kế. Migration = Chuyển nhà (môi trường).

---

Như vậy, **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.