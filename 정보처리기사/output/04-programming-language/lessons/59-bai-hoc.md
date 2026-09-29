# 196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

화이트, 박스, 테스트

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)**에서 만든 기준을 이어받아 **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)** và nối nó với **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)

Sau khi đã đặt nền bằng **195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)**, ta chuyển sang **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)**. Đây là mắt xích 59/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)** như một bài học cho người mới, hãy giữ câu hỏi: **ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈의 **원시 코드(Source Code)를 오픈시킨 상태**에서 논리적인 모든 경로를 검사.
- 내부 구조, 제어 흐름, 논리 흐름(루프)을 직접 관찰하며 테스트.
- 조건의 참/거짓 경로를 적어도 한 번 이상 실행.
- 테스트 과정 **초기**에 적용됨.
- 종류: 기초 경로 검사 (Basic Path Testing), 조건 검사, 루프 검사, 데이터 흐름 검사.

**Giải thích (Vietnamese):**
Kiểm thử hộp trắng là bạn (thường là Dev) nhìn thấy toàn bộ source code và viết test case để đảm bảo mọi dòng code (if, else, vòng lặp) đều được chạy qua ít nhất 1 lần.

**💡 Mẹo ghi nhớ (Mnemonics):**
Hộp trắng trong suốt -> Nhìn thấu được code bên trong. Trọng tâm là "Logic đường đi" (경로).

---

Ta có thể khép mục **196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.