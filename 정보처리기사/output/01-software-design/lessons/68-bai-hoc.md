# 8. 재사용 (Reuse)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **8. 재사용 (Reuse)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối distributed systems với node, message, consistency và failure, để kiến trúc được đọc qua những gì có thể hỏng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **8. 재사용 (Reuse)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **8. 재사용 (Reuse)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **10. 코드 (Code) 개요 & 종류** khi chuyển sang phần tiếp theo.

Mục tiêu xác định reuse chia sẻ giá trị mà không làm mất boundary và ownership ra sao; từ khóa khoanh vùng các lựa chọn tái sử dụng.

## 핵심 키워드 (Từ khóa)

재사용

Kiến thức liên kết đặt reuse trên nền module và architecture; cách đọc tiếp theo giúp cân bằng chia sẻ với coupling và thay đổi.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. N-S 차트 (Nassi-Schneiderman Chart)**에서 만든 기준을 이어받아 **8. 재사용 (Reuse)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần reuse dùng khung đó để nối lợi ích với chi phí ownership.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng boundary và ownership của thành phần tái sử dụng; khi sang code hoặc maintenance, hãy giữ lại chi phí thay đổi.

## 8. 재사용 (Reuse)

Sau khi đã đặt nền bằng **6. N-S 차트 (Nassi-Schneiderman Chart)**, ta chuyển sang **8. 재사용 (Reuse)**. Đây là mắt xích 68/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. 재사용 (Reuse)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 기존 기능을 최적화하여 다시 쓰는 것 (Tái sử dụng chức năng để tiết kiệm thời gian và chi phí).

*   **Korean:** 결합도는 낮고 응집도는 높아야 함.
*   **VI (Vietnamese) (Tiếng Việt):** Yêu cầu: Độ phụ thuộc (Coupling) THẤP và Độ gắn kết (Cohesion) CAO.
*   **분류 (Phân loại):**
    *   **함수와 객체 (Function & Object):** 소스 코드 단위 (Mức mã nguồn / Class).
    *   **컴포넌트 (Component):** 인터페이스 통신 (Mức Interface, không sửa code gốc).
    *   **애플리케이션 (Application):** 시스템 전체 (Mức ứng dụng hoàn chỉnh).

---

Ta có thể khép mục **8. 재사용 (Reuse)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **10. 코드 (Code) 개요 & 종류**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **8. 재사용 (Reuse)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
