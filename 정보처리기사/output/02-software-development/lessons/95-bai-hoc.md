# 091: 스키마 (Schema)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **091: 스키마 (Schema)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **091: 스키마 (Schema)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **091-1: 절차형 SQL (Procedural SQL)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

스키마

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **090-1: 데이터의 독립성 (Data Independence)**에서 만든 기준을 이어받아 **091: 스키마 (Schema)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **091: 스키마 (Schema)** và nối nó với **091-1: 절차형 SQL (Procedural SQL)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 091: 스키마 (Schema)

Sau khi đã đặt nền bằng **090-1: 데이터의 독립성 (Data Independence)**, ta chuyển sang **091: 스키마 (Schema)**. Đây là mắt xích 95/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **091: 스키마 (Schema)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

스키마 là bộ khung (Cấu trúc, ràng buộc) của Database. Có 3 góc nhìn:
- **외부 스키마 (External Schema):** User view. (User nhìn thấy gì, vd: Màn hình nhân viên chỉ thấy Lương của mình).
- **개념 스키마 (Conceptual Schema):** DB Admin view. (Toàn bộ logic, cấu trúc của doanh nghiệp. Thường gọi tắt là "Schema").
- **내부 스키마 (Internal Schema):** System view. (Cấu trúc vật lý, lưu trên đĩa như thế nào).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Ngoại (User/App) - Khái niệm (Toàn cục/Admin) - Nội (Máy móc/Ổ cứng).

---

Ta có thể khép mục **091: 스키마 (Schema)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **091-1: 절차형 SQL (Procedural SQL)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.