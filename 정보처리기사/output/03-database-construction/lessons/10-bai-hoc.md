# 105. E-R 다이어그램 (E-R Diagram)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **105. E-R 다이어그램 (E-R Diagram)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **105. E-R 다이어그램 (E-R Diagram)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **110-114. 키 (Keys)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

E-R, 다이어그램

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**에서 만든 기준을 이어받아 **105. E-R 다이어그램 (E-R Diagram)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **105. E-R 다이어그램 (E-R Diagram)** và nối nó với **110-114. 키 (Keys)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 105. E-R 다이어그램 (E-R Diagram)

Ở bước 10/56, **105. E-R 다이어그램 (E-R Diagram)** xuất hiện như phần tiếp nối của **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **105. E-R 다이어그램 (E-R Diagram)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 사각형 (Rectangle): 개체 (Entity)
- 마름모 (Diamond): 관계 (Relationship)
- 타원 (Oval): 속성 (Attribute)
- 이중 타원 (Double Oval): 다중값 속성 (Multivalued Attribute)
- 선 (Line): 연결 (Link)
- **VI (Vietnamese) (Tiếng Việt):** Sơ đồ E-R. Hình chữ nhật (Thực thể), Hình thoi (Mối quan hệ), Hình bầu dục (Thuộc tính), Hình bầu dục kép (Thuộc tính đa trị).
- **Example:** 고객(사각형)이 상품(사각형)을 구매(마름모)한다. / Khách hàng (HCN) mua (Hình thoi) sản phẩm (HCN).

Như vậy, **105. E-R 다이어그램 (E-R Diagram)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **110-114. 키 (Keys)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.