# 10. 소프트웨어 설계 원리 (Software Design Principles)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **10. 소프트웨어 설계 원리 (Software Design Principles)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối software design principles với cohesion, coupling, abstraction và change, để nguyên tắc dẫn tới quyết định cụ thể.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **10. 소프트웨어 설계 원리 (Software Design Principles)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **10. 소프트웨어 설계 원리 (Software Design Principles)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 결합도 (Coupling - Độ phụ thuộc)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **10. 소프트웨어 설계 원리 (Software Design Principles)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

소프트웨어, 설계, 원리

> **Chuyển mạch:** Ở chặng này của **10. 소프트웨어 설계 원리 (Software Design Principles)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. 구조적 분석 도구 (Structured Analysis Tools)**에서 만든 기준을 이어받아 **10. 소프트웨어 설계 원리 (Software Design Principles)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10. 소프트웨어 설계 원리 (Software Design Principles)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. 소프트웨어 설계 원리 (Software Design Principles)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **10. 소프트웨어 설계 원리 (Software Design Principles)**, **10. 소프트웨어 설계 원리 (Software Design Principles)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 10. 소프트웨어 설계 원리 (Software Design Principles)

Từ **6. 구조적 분석 도구 (Structured Analysis Tools)**, ta đã có điểm tựa để bước vào **10. 소프트웨어 설계 원리 (Software Design Principles)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 63/69 trước khi đi vào chi tiết.

Để đọc **10. 소프트웨어 설계 원리 (Software Design Principles)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **모듈화 (Modularity)**, **추상화 (Abstraction)**, **단계적 분해 (Stepwise Refinement)**, **정보 은닉 (Information Hiding)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “10. 소프트웨어 설계 원리 (Software Design Principles)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **모듈화 (Modularity)**:
  - Module quá nhỏ -> Chi phí tích hợp (Integration Cost) tăng.
  - Module quá lớn -> Chi phí phát triển từng module (Development Cost) tăng.
- **추상화 (Abstraction)**: 3 loại (과정 - Quá trình, 데이터 - Dữ liệu, 제어 - Điều khiển).
- **단계적 분해 (Stepwise Refinement)**: Đi từ trên xuống (Top-down).
- **정보 은닉 (Information Hiding)**: Giấu thông tin để giảm phụ thuộc.
- **시스템 타입 (System Types)**:
  - **대화형 (Interactive)**: Tương tác (VD: Web bán hàng).
  - **이벤트 중심 (Event-driven)**: Dựa trên sự kiện (VD: Chuông báo cháy).
  - **변환형 (Transformational)**: Biến đổi dữ liệu (VD: Trình biên dịch - Compiler).
  - **객체 영속형 (Object Persistence)**: Lưu trữ lâu dài (VD: Database Server).

Điểm chốt của **10. 소프트웨어 설계 원리 (Software Design Principles)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **3. 결합도 (Coupling - Độ phụ thuộc)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **10. 소프트웨어 설계 원리 (Software Design Principles)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
