# 6. N-S 차트 (Nassi-Schneiderman Chart)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **6. N-S 차트 (Nassi-Schneiderman Chart)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối N-S chart với sequence, branch và loop, để control flow được nhìn trực quan qua cấu trúc lồng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **6. N-S 차트 (Nassi-Schneiderman Chart)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **6. N-S 차트 (Nassi-Schneiderman Chart)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **8. 재사용 (Reuse)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **6. N-S 차트 (Nassi-Schneiderman Chart)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

N-S, 차트

> **Chuyển mạch:** Ở chặng này của **6. N-S 차트 (Nassi-Schneiderman Chart)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. Fan-In / Fan-Out (팬인 / 팬아웃)**에서 만든 기준을 이어받아 **6. N-S 차트 (Nassi-Schneiderman Chart)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **6. N-S 차트 (Nassi-Schneiderman Chart)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. N-S 차트 (Nassi-Schneiderman Chart)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **6. N-S 차트 (Nassi-Schneiderman Chart)**, **6. N-S 차트 (Nassi-Schneiderman Chart)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 6. N-S 차트 (Nassi-Schneiderman Chart)

Ở bước 67/69, **6. N-S 차트 (Nassi-Schneiderman Chart)** xuất hiện như phần tiếp nối của **5. Fan-In / Fan-Out (팬인 / 팬아웃)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **6. N-S 차트 (Nassi-Schneiderman Chart)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 논리 기술 중점의 박스 다이어그램 (Biểu đồ dạng hộp tập trung mô tả logic).

*   **Korean:** GOTO나 화살표를 사용하지 않음. 단일 입구/단일 출구. Box Diagram, Chapin Chart라고도 부름. 순차, 선택, 반복 논리 구조 시각화.
*   **VI (Vietnamese) (Tiếng Việt):** Đặc điểm quan trọng nhất: **KHÔNG DÙNG GOTO và KHÔNG CÓ MŨI TÊN**. Có một lối vào và một lối ra duy nhất. Còn gọi là Box Diagram hoặc Chapin Chart. Gồm 3 cấu trúc: Tuần tự, Lựa chọn (If-else), Lặp (Loop). Dễ chuyển sang code nhưng khó vẽ.

---

Như vậy, **6. N-S 차트 (Nassi-Schneiderman Chart)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **8. 재사용 (Reuse)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **6. N-S 차트 (Nassi-Schneiderman Chart)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
