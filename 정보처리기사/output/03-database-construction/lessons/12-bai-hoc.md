# 173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối key, integrity và relational algebra, để đọc định danh, ràng buộc và phép biến đổi quan hệ trong cùng một mô hình dữ liệu.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 스키마 (Schema - Lược đồ)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

키와, 무결성, 관계대수, 요약

> **Chuyển mạch:** Ở chặng này của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **110-114. 키 (Keys)**에서 만든 기준을 이어받아 **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**, **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)

Từ **110-114. 키 (Keys)**, ta đã có điểm tựa để bước vào **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 12/54 trước khi đi vào chi tiết.

Để đọc **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

*Note: Includes duplicated points consolidated.*
- **도메인 무결성 (Domain Integrity):** 속성 값이 정의된 도메인에 속해야 함.
- **사용자 정의 무결성 (User-Defined Integrity):** 사용자가 정의한 제약 조건 만족.
- **순수 관계 연산자 (Pure Relational Operators):**
  - Select (σ): 수평 연산 (Horizontal) - 튜플 구함.
  - Project (π): 수직 연산 (Vertical) - 속성 구함.
  - Join (⋈) / Division (÷).
- **일반 집합 연산자 (Set Operators):** UNION (합집합), INTERSECTION (교집합), DIFFERENCE (차집합), CARTESIAN PRODUCT (교차곱).
- **VI (Vietnamese) (Tiếng Việt):** Các ràng buộc và Đại số quan hệ (nhắc lại).
  - Toàn vẹn miền (Domain): Giá trị phải nằm trong miền cho phép.
  - Select: Phép toán ngang (lọc hàng).
  - Project: Phép toán dọc (lọc cột).
  - Phép toán tập hợp: Hợp, Giao, Hiệu, Tích Đề-các.

Điểm chốt của **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **5. 스키마 (Schema - Lược đồ)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **173-177. 키와 무결성, 관계대수 요약 (Keys, Integrity, Relational Algebra)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
