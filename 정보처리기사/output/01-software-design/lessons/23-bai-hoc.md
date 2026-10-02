# 8. UI 및 UX, HCI (UI, UX, HCI)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **8. UI 및 UX, HCI (UI, UX, HCI)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối UI, UX và HCI với task, feedback, accessibility và context, để giao diện được đánh giá qua người dùng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **8. UI 및 UX, HCI (UI, UX, HCI)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **8. UI 및 UX, HCI (UI, UX, HCI)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **8. UI 및 UX, HCI (UI, UX, HCI)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

HCI

> **Chuyển mạch:** Ở chặng này của **8. UI 및 UX, HCI (UI, UX, HCI)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. 요구공학 (Requirements Engineering)**에서 만든 기준을 이어받아 **8. UI 및 UX, HCI (UI, UX, HCI)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **8. UI 및 UX, HCI (UI, UX, HCI)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. UI 및 UX, HCI (UI, UX, HCI)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **8. UI 및 UX, HCI (UI, UX, HCI)**, **8. UI 및 UX, HCI (UI, UX, HCI)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 8. UI 및 UX, HCI (UI, UX, HCI)

Sau khi đã đặt nền bằng **5. 요구공학 (Requirements Engineering)**, ta chuyển sang **8. UI 및 UX, HCI (UI, UX, HCI)**. Đây là mắt xích 23/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. UI 및 UX, HCI (UI, UX, HCI)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **UI 유형**, **UI 설계 도구**, **HCI (Human Computer Interaction)**, **UX (User Experience - Trải nghiệm người dùng)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “8. UI 및 UX, HCI (UI, UX, HCI)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **UI 유형**: CLI (Văn bản), GUI (Đồ họa), NUI (Tự nhiên - Giọng nói/Hành động), OUI (Hữu cơ - Gắn với đồ vật vật lý).
- **UI 설계 도구**: Wireframe (Khung xương), Mockup (Mô hình tĩnh giống thật), Storyboard (Kịch bản chi tiết), Prototype (Mô hình động tương tác).
- **HCI (Human Computer Interaction)**: Nghiên cứu tương tác người-máy tính để mang lại trải nghiệm tốt nhất (UX).
- **UX (User Experience - Trải nghiệm người dùng)**:
  - **주관성 (Subjectivity)**: Tính chủ quan.
  - **정황성 (Contextuality)**: Phụ thuộc vào hoàn cảnh (thời gian, địa điểm).
  - **총체성 (Holistic)**: Trải nghiệm tổng thể.
- **감성공학 (Affective Engineering)**: Khoa học kết hợp cảm xúc con người vào thiết kế (Dựa trên -> Thực hiện -> Ứng dụng).

Ta có thể khép mục **8. UI 및 UX, HCI (UI, UX, HCI)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **8. UI 및 UX, HCI (UI, UX, HCI)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
