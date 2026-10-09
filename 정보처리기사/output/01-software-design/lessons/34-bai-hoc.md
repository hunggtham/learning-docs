# 9. 소프트웨어 품질 특성 (ISO/IEC 9126)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối ISO/IEC 9126 với quality attributes, measurement và trade-off, để chất lượng được đánh giá theo thuộc tính cụ thể.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **9. 소프트웨어 품질 특성 (ISO/IEC 9126)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **8. 디자인 패턴 (Design Patterns)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định quality attribute được mô tả và đo lường ra sao; từ khóa khoanh vùng thuộc tính, metric và trade-off.

## 핵심 키워드 (Từ khóa)

소프트웨어, 품질, 특성

Kiến thức liên kết đặt quality characteristics trên nền architecture và testing; cách đọc tiếp theo giúp tách thuộc tính khỏi metric cụ thể.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **9. 효과적인 모듈 설계 방안 (Effective Module Design)**에서 만든 기준을 이어받아 **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần ISO/IEC 9126 dùng khung đó để nối quality attribute với evidence.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng tiêu chí đo lường và trade-off; khi sang design pattern, hãy giữ lại quality attribute cần bảo vệ.

## 9. 소프트웨어 품질 특성 (ISO/IEC 9126)

Ở bước 34/69, **9. 소프트웨어 품질 특성 (ISO/IEC 9126)** xuất hiện như phần tiếp nối của **9. 효과적인 모듈 설계 방안 (Effective Module Design)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **9. 소프트웨어 품질 특성 (ISO/IEC 9126)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “9. 소프트웨어 품질 특성 (ISO/IEC 9126)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 6 tiêu chuẩn chất lượng:
  1. **기능성 (Functionality - Chức năng)**: Bảo mật, Tương tác, Chính xác.
  2. **신뢰성 (Reliability - Độ tin cậy)**: Không lỗi, Phục hồi (회복성), Chịu lỗi (고장 허용성).
  3. **사용성 (Usability - Khả năng sử dụng)**: Dễ học, Dễ hiểu, Hấp dẫn.
  4. **효율성 (Efficiency - Hiệu quả)**: Thời gian phản hồi, Tiết kiệm tài nguyên.
  5. **유지 보수성 (Maintainability - Khả năng bảo trì)**: Dễ phân tích, Dễ thay đổi, Ổn định.
  6. **이식성 (Portability - Khả năng thay thế/di chuyển)**: Cài đặt dễ, Tương thích, Thay thế.

Như vậy, **9. 소프트웨어 품질 특성 (ISO/IEC 9126)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **8. 디자인 패턴 (Design Patterns)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **9. 소프트웨어 품질 특성 (ISO/IEC 9126)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
