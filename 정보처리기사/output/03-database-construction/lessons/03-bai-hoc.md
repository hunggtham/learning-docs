# 103. 물리적 설계 (Physical Design)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **103. 물리적 설계 (Physical Design)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **103. 물리적 설계 (Physical Design)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **163-167. 데이터베이스 설계 순서 (Database Design Process)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

물리적, 설계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **102. 논리적 설계 (Logical Design / Data Modeling)**에서 만든 기준을 이어받아 **103. 물리적 설계 (Physical Design)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **103. 물리적 설계 (Physical Design)** và nối nó với **163-167. 데이터베이스 설계 순서 (Database Design Process)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 103. 물리적 설계 (Physical Design)

Từ **102. 논리적 설계 (Logical Design / Data Modeling)**, ta đã có điểm tựa để bước vào **103. 물리적 설계 (Physical Design)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/56 trước khi đi vào chi tiết.

Để đọc **103. 물리적 설계 (Physical Design)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 논리적 구조로 표현된 데이터를 물리적 구조의 데이터로 변환하는 과정이다.
- 데이터베이스 파일의 저장 구조 및 액세스 경로를 결정한다.
- **VI (Vietnamese) (Tiếng Việt):** Thiết kế vật lý. Quá trình chuyển đổi dữ liệu cấu trúc logic thành cấu trúc vật lý (lưu trữ ổ đĩa, đường dẫn truy cập).
- **Example (Korean/Vietnamese):** 테이블에 인덱스를 생성하여 검색 속도를 높이는 것. / Tạo chỉ mục (index) trên bảng để tăng tốc độ tìm kiếm.
- 💡 **Mẹo ghi nhớ:** Vật-Lưu (Thiết kế Vật lý = Cấu trúc Lưu trữ).

Điểm chốt của **103. 물리적 설계 (Physical Design)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **163-167. 데이터베이스 설계 순서 (Database Design Process)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.