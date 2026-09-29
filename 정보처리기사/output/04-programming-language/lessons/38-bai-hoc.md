# 083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

메모리, 관리, 기법, 배치, 전략

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**에서 만든 기준을 이어받아 **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** và nối nó với **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)

Sau khi đã đặt nền bằng **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**, ta chuyển sang **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**. Đây là mắt xích 38/78 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **최초 적합 (First fit)**, **최적 적합 (Best fit)**, **최악 적합 (Worst fit)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **최초 적합 (First fit)**: 가장 처음 만나는 빈 공간에 할당 (빠름).
- **최적 적합 (Best fit)**: 자원 낭비(단편화)가 가장 적은 핏(딱 맞는) 공간에 할당.
- **최악 적합 (Worst fit)**: 단편화가 가장 큰(넓은) 공간에 할당 (남은 공간을 다시 쓰기 위해).

**Giải thích (Vietnamese):**
Khi một phần mềm cần RAM, OS sẽ nhét nó vào đâu?
- First fit: Thấy chỗ nào trống nhét vào luôn (Nhanh).
- Best fit: Tìm chỗ nào vừa khít nhất để nhét (Tiết kiệm chỗ).
- Worst fit: Cố tình nhét vào chỗ rộng nhất (Để chừa lại không gian rộng cho các app sau).

---

Ta có thể khép mục **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.