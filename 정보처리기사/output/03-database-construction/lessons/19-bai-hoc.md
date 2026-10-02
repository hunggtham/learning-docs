# 184-185. 반정규화 (Denormalization)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **184-185. 반정규화 (Denormalization)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối denormalization với read performance, redundancy và consistency, để đánh đổi được quyết định theo workload.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **184-185. 반정규화 (Denormalization)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **184-185. 반정규화 (Denormalization)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **16. 정규화(Normalization)와 이상 현상(Anomaly)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **184-185. 반정규화 (Denormalization)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

반정규화

> **Chuyển mạch:** Ở chặng này của **184-185. 반정규화 (Denormalization)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**에서 만든 기준을 이어받아 **184-185. 반정규화 (Denormalization)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **184-185. 반정규화 (Denormalization)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **184-185. 반정규화 (Denormalization)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **184-185. 반정규화 (Denormalization)**, **184-185. 반정규화 (Denormalization)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 184-185. 반정규화 (Denormalization)

Ở bước 19/54, **184-185. 반정규화 (Denormalization)** xuất hiện như phần tiếp nối của **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **184-185. 반정규화 (Denormalization)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “184-185. 반정규화 (Denormalization)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 시스템 성능 향상을 위해 정규화 원칙을 의도적으로 위배 (통합, 중복, 분리).
- **방법:** 테이블 통합, 테이블 분할 (수평/수직 분할), 중복 테이블/속성 추가.
- **VI (Vietnamese) (Tiếng Việt):** Phi chuẩn hóa.
  - Cố tình phá vỡ quy tắc chuẩn hóa để tăng hiệu suất truy vấn.
  - Phương pháp: Gộp bảng, Chia bảng (ngang/dọc), Thêm cột/bảng dư thừa.
- **Example:** 조인(Join)을 피하기 위해 부서 테이블의 '부서명'을 사원 테이블에 중복 저장. / Thêm cột 'Tên phòng' vào bảng 'Nhân viên' để tránh phải Join.

Như vậy, **184-185. 반정규화 (Denormalization)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **16. 정규화(Normalization)와 이상 현상(Anomaly)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **184-185. 반정규화 (Denormalization)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
