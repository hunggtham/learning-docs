# 13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **105. E-R 다이어그램 (E-R Diagram)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터, 모델과, E-R, 다이어그램

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**에서 만든 기준을 이어받아 **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)

Từ **12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)**, ta đã có điểm tựa để bước vào **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 9/55 trước khi đi vào chi tiết.

Để đọc **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)

Các ý ngay dưới **데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **개체 (Entity):** Đối tượng thực tế (ví dụ: Sinh viên, Môn học).
- **속성 (Attribute):** Đặc điểm của đối tượng (ví dụ: Mã SV, Tên).
- **관계 (Relationship):** Sự liên kết giữa các đối tượng (ví dụ: Đăng ký).
- *Lưu ý: 3 yếu tố cơ bản của mô hình là Cấu trúc (Structure), Phép toán (Operation), và Ràng buộc (Constraint).*

Các ý về **데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)

Bây giờ ta đi vào nội dung của **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

| 기호 (Ký hiệu) | 의미 (Ý nghĩa) | Giải thích (VN) |
|---|---|---|
| **사각형 (Hình chữ nhật)** | 개체 (Entity) | Đối tượng thực thể. |
| **마름모 (Hình thoi)** | 관계 (Relationship) | Mối quan hệ giữa các thực thể (1:1, 1:N, N:M). |
| **타원 (Hình bầu dục)** | 속성 (Attribute) | Thuộc tính. |
| **밑줄 타원 (Bầu dục gạch dưới)** | 기본키 (Primary Key) | Thuộc tính Khóa chính. |
| **이중 타원 (Bầu dục kép)** | 다중 값 속성 (Multi-valued) | Thuộc tính đa trị (có thể chứa nhiều giá trị, vd: Số điện thoại). |
| **선 (Đường thẳng)** | 링크 (Link) | Đường nối kết. |

---

Bảng trong **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào và trong điều kiện nào sự khác biệt đó có ý nghĩa.

Điểm chốt của **E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **105. E-R 다이어그램 (E-R Diagram)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.