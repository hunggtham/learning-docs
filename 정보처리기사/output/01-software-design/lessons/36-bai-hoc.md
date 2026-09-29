# 9. 효과적인 모듈 설계 방안 (Effective Module Design)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **9. 효과적인 모듈 설계 방안 (Effective Module Design)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **9. 효과적인 모듈 설계 방안 (Effective Module Design)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **9. 소프트웨어 품질 특성 (ISO/IEC 9126)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

효과적인, 모듈, 설계, 방안

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **7. 공통 모듈 (Common Module)**에서 만든 기준을 이어받아 **9. 효과적인 모듈 설계 방안 (Effective Module Design)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **9. 효과적인 모듈 설계 방안 (Effective Module Design)** và nối nó với **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 9. 효과적인 모듈 설계 방안 (Effective Module Design)

Từ **7. 공통 모듈 (Common Module)**, ta đã có điểm tựa để bước vào **9. 효과적인 모듈 설계 방안 (Effective Module Design)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 36/57 trước khi đi vào chi tiết.

Để đọc **9. 효과적인 모듈 설계 방안 (Effective Module Design)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

*   **Korean:** 결합도↓, 응집도↑. 모듈의 영향 영역(Scope of Effect)이 제어 영역(Scope of Control) 안에 있어야 함. 단일 입구/단일 출구(Single Entry, Single Exit). 복잡도와 중복성 감소.
*   **VI (Vietnamese) (Tiếng Việt):** Coupling thấp, Cohesion cao. **Phạm vi ảnh hưởng (Scope of Effect) phải nằm TRONG Phạm vi kiểm soát (Scope of Control)** của module. Chỉ có 1 đầu vào và 1 đầu ra. Giảm độ phức tạp và dư thừa.
*   **Example:** Một hàm sắp xếp chỉ nên thay đổi mảng truyền vào nó (trong vùng kiểm soát), không nên vô tình thay đổi giao diện UI (vùng ảnh hưởng ngoài kiểm soát).

---

Điểm chốt của **9. 효과적인 모듈 설계 방안 (Effective Module Design)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.