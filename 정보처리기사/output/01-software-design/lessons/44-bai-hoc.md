# 1. 회복 (Recovery)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **1. 회복 (Recovery)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **1. 회복 (Recovery)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. Commit & Rollback 연산** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

회복

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)**에서 만든 기준을 이어받아 **1. 회복 (Recovery)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **1. 회복 (Recovery)** và nối nó với **2. Commit & Rollback 연산**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 1. 회복 (Recovery)

Sau khi đã đặt nền bằng **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)**, ta chuyển sang **1. 회복 (Recovery)**. Đây là mắt xích 44/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **1. 회복 (Recovery)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념 (Concept)**, **장애의 유형 (Types of Failures)**, **트랜잭션 장애 (Transaction Failure)**, **시스템 장애 (System Failure)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 회복 (Recovery)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Concept)**: 트랜잭션 도중 장애 발생 시 정상 상태로 복구 (Phục hồi về trạng thái bình thường khi có lỗi).
- **장애의 유형 (Types of Failures)**:
  - **트랜잭션 장애 (Transaction Failure)**: Lỗi nội bộ của giao dịch (ví dụ: dữ liệu sai).
  - **시스템 장애 (System Failure)**: Lỗi phần cứng/phần mềm ảnh hưởng đến tất cả giao dịch.
  - **미디어 장애 (Media Failure)**: Lỗi vật lý của thiết bị lưu trữ (ví dụ: hỏng đĩa).
- **회복 기법 (Recovery Techniques)**: 연기 갱신 (Deferred Update), 즉각 갱신 (Immediate Update), 그림자 페이지 (Shadow Paging), 검사점 (Check Point).
- **Ví dụ**: Hệ thống ngân hàng bị sập khi đang chuyển tiền (hệ thống lỗi), cần hoàn tác (Undo) hoặc chạy lại để khôi phục.
- 💡 **Mẹo ghi nhớ**: 장애 유형: T/S/M (Transaction, System, Media) -> **Tưởng Sợ Ma**

Ta có thể khép mục **1. 회복 (Recovery)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **2. Commit & Rollback 연산**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.