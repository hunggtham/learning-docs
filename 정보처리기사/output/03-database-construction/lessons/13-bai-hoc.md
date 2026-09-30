# 5. 스키마 (Schema - Lược đồ)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **5. 스키마 (Schema - Lược đồ)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **5. 스키마 (Schema - Lược đồ)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

스키마

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**에서 만든 기준을 이어받아 **5. 스키마 (Schema - Lược đồ)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **5. 스키마 (Schema - Lược đồ)** và nối nó với **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 5. 스키마 (Schema - Lược đồ)

Ở bước 13/54, **5. 스키마 (Schema - Lược đồ)** xuất hiện như phần tiếp nối của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **5. 스키마 (Schema - Lược đồ)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “5. 스키마 (Schema - Lược đồ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **외부 스키마 (External Schema - Lược đồ ngoại):** 사용자나 개발자의 관점 (Góc nhìn người dùng). Nhiều lược đồ ngoại tồn tại cùng lúc (Mỗi người nhìn hệ thống một kiểu).
- **개념 스키마 (Conceptual Schema - Lược đồ khái niệm):** 조직 전체의 논리적 구조, 단 하나만 존재 (Cấu trúc logic của toàn bộ tổ chức, chỉ có 1). Quản lý quan hệ, quyền, bảo mật.
- **내부 스키마 (Internal Schema - Lược đồ nội):** 물리적 저장장치의 관점 (Góc nhìn lưu trữ vật lý). Tổ chức các bản ghi, chỉ mục trên ổ đĩa.

> 💡 **Mẹo ghi nhớ:** **Ngoại - Khái - Nội** (Người dùng (Ngoại) -> Thiết kế CSDL (Khái) -> Ổ cứng (Nội)).

---

Như vậy, **5. 스키마 (Schema - Lược đồ)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.