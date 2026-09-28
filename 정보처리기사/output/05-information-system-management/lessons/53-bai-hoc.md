# 3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

사이트, 요청, 위조

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh hệ điều hành)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)** và nối nó với **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)
- **개념**: 로그인 세션이나 쿠키가 남아 있는 사용자의 브라우저가 공격자가 의도한 상태 변경 요청을 보내도록 유도하는 취약점.
- **Tiếng Việt**: Lợi dụng phiên đăng nhập (session) hợp lệ của người dùng để thực hiện các yêu cầu không mong muốn.
- **예시 (Example)**:
  - (KR) 로그인된 상태에서 공격자가 보낸 링크를 클릭하면 내 계정에서 몰래 송금이 됨.
  - (VN) Khi đang đăng nhập ngân hàng, lỡ click vào link của hacker thì bị tự động chuyển tiền.
- **대책**: CSRF 토큰과 SameSite 쿠키를 사용하고, 서버에서 Origin/Referer와 인증 상태를 검증한다. POST만으로는 충분하지 않다.
- 💡 **Mẹo ghi nhớ**: C-S-R-F = Cứ Sợ Rằng Fake (Sợ người dùng thật nhưng gửi request fake).
