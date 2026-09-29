# 6. N-S 차트 (Nassi-Schneiderman Chart)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **6. N-S 차트 (Nassi-Schneiderman Chart)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **6. N-S 차트 (Nassi-Schneiderman Chart)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **8. 재사용 (Reuse)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

N-S, 차트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. Fan-In / Fan-Out (팬인 / 팬아웃)**에서 만든 기준을 이어받아 **6. N-S 차트 (Nassi-Schneiderman Chart)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 6. N-S 차트 (Nassi-Schneiderman Chart)

Sau khi đã đặt nền bằng **5. Fan-In / Fan-Out (팬인 / 팬아웃)**, ta chuyển sang **6. N-S 차트 (Nassi-Schneiderman Chart)**. Đây là mắt xích 53/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **6. N-S 차트 (Nassi-Schneiderman Chart)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 논리 기술 중점의 박스 다이어그램 (Biểu đồ dạng hộp tập trung mô tả logic).

*   **Korean:** GOTO나 화살표를 사용하지 않음. 단일 입구/단일 출구. Box Diagram, Chapin Chart라고도 부름. 순차, 선택, 반복 논리 구조 시각화.
*   **VI (Vietnamese) (Tiếng Việt):** Đặc điểm quan trọng nhất: **KHÔNG DÙNG GOTO và KHÔNG CÓ MŨI TÊN**. Có một lối vào và một lối ra duy nhất. Còn gọi là Box Diagram hoặc Chapin Chart. Gồm 3 cấu trúc: Tuần tự, Lựa chọn (If-else), Lặp (Loop). Dễ chuyển sang code nhưng khó vẽ.

---

Ta có thể khép mục **6. N-S 차트 (Nassi-Schneiderman Chart)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **8. 재사용 (Reuse)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.