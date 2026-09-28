# 13. 형상 관리 (SCM - Software Configuration Management)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **13. 형상 관리 (SCM - Software Configuration Management)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

형상, 관리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **13. 형상 관리 (SCM - Software Configuration Management)** và nối nó với **40. 형상 관리 (SCM) 및 버전 관리 방식 (Version Control Methods)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 13. 형상 관리 (SCM - Software Configuration Management)
* 변경 사항을 관리하기 위해 개발된 일련의 활동. 목적: 개발 비용 감소, 방해 요인 최소화.
* **도구 (Tools)**: Git, CVS, Subversion(SVN).
* **주요 기능 (Key Functions)**:
  * **Check-Out**: 저장소에서 파일을 받아옴.
  * **Check-In**: 수정을 완료한 후 저장소에 새로운 버전으로 갱신.
  * **lần ghi nhận (commit / 커밋)**: 갱신 시 충돌을 알리고 수정한 후 완료함.
* **VI (Vietnamese) (Tiếng Việt):** Quản lý cấu hình phần mềm (quản lý thay đổi/version).
  * Check-out: Lấy tệp (file / 파일) về.
  * Check-in: Lưu tệp (file / 파일) lên.
  * lần ghi nhận (commit / 커밋): Lưu thay đổi (xử lý xung đột nếu có).
* **Example**: Git에서 코드를 가져오는 것이 Checkout, 수정 후 서버에 올리는 것이 lần ghi nhận (commit / 커밋)/Check-in입니다.
* 💡 **Mẹo ghi nhớ**: In = vào kho, Out = ra khỏi kho.
