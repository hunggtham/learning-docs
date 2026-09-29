# 190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **191. 결합도 (Coupling / Mức độ phụ thuộc)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

바람직한, 설계의, 특징

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)**에서 만든 기준을 이어받아 **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)** và nối nó với **191. 결합도 (Coupling / Mức độ phụ thuộc)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)

Từ **프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)**, ta đã có điểm tựa để bước vào **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/91 trước khi đi vào chi tiết.

Để đọc **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 적당한 모듈 크기를 유지.
- **결합도(Coupling)는 약하게, 응집도(Cohesion)는 강하게 설계한다**.

**Giải thích (Vietnamese):**
Một thiết kế phần mềm chuẩn mực phải đảm bảo: "Mối liên kết giữa các module càng lỏng lẻo càng tốt (Low Coupling), nhưng sự gắn kết nhiệm vụ bên trong một module phải càng chặt chẽ càng tốt (High Cohesion)".

---

Điểm chốt của **190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **191. 결합도 (Coupling / Mức độ phụ thuộc)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.