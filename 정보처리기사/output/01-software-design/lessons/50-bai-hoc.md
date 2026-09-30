# 7. 자료 구조 (Data Structures)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **7. 자료 구조 (Data Structures)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **7. 자료 구조 (Data Structures)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **8. 연결 리스트, 스택, 큐, 데크 (Data Structure Types)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

자료, 구조

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. 분산 데이터베이스 (Distributed Database)**에서 만든 기준을 이어받아 **7. 자료 구조 (Data Structures)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **7. 자료 구조 (Data Structures)** và nối nó với **8. 연결 리스트, 스택, 큐, 데크 (Data Structure Types)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 7. 자료 구조 (Data Structures)

Sau khi đã đặt nền bằng **6. 분산 데이터베이스 (Distributed Database)**, ta chuyển sang **7. 자료 구조 (Data Structures)**. Đây là mắt xích 50/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **7. 자료 구조 (Data Structures)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **선형 구조 (Linear)**, **비선형 구조 (Non-Linear)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “7. 자료 구조 (Data Structures)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **선형 구조 (Linear)**: 배열 (Array), 연결 리스트 (Linked List), 스택 (Stack), 큐 (Queue), 데크 (Deque).
- **비선형 구조 (Non-Linear)**: 트리 (Tree), 그래프 (Graph).
- 💡 **Mẹo ghi nhớ**: 비선형 (Non-linear) là Tree & Graph, còn lại là 선형.

Ta có thể khép mục **7. 자료 구조 (Data Structures)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **8. 연결 리스트, 스택, 큐, 데크 (Data Structure Types)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.