# 195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

구현, 구조적, 프로그래밍, 제어, 흐름도

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)**에서 만든 기준을 이어받아 **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)** và nối nó với **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)

Ở bước 58/91, **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)** xuất hiện như phần tiếp nối của **193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **구현(코딩)**, **구조적 프로그래밍**, **순환 복잡도 (Cyclomatic Complexity)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **구현(코딩)**: 설계 명세서를 컴퓨터가 알 수 있는 코드로 변환.
- **구조적 프로그래밍**: 순차(Sequence), 선택(Selection), 반복(Iteration)의 3가지 제어 구조만 사용하여 코딩 (Dijkstra 제안). 신뢰성 향상.
- **순환 복잡도 (Cyclomatic Complexity)**: 프로그램의 논리적 복잡도 척도.
  - V(G) = E - N + 2 (E: 화살표 수, N: 노드 수). 또는 닫힌 영역의 수 + 1.

**Giải thích (Vietnamese):**
Lập trình có cấu trúc chỉ dùng 3 luồng: Chạy tuần tự từ trên xuống (Sequence), Lệnh rẽ nhánh If/Else (Selection), và Vòng lặp For/While (Iteration). Độ phức tạp McCabe tính xem hàm có bao nhiêu đường đi (nhánh) độc lập.

**Ví dụ (Example):**
Nếu biểu đồ luồng có 5 Node (N=5) và 6 Cạnh/Mũi tên (E=6).
Độ phức tạp Cyclomatic V(G) = 6 - 5 + 2 = 3. Số 3 nghĩa là hàm này cần ít nhất 3 test case để phủ toàn bộ các đường đi.

---

Như vậy, **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.