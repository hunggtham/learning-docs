# 16. 소프트웨어 테스트 단계 (Software Testing Phases)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **16. 소프트웨어 테스트 단계 (Software Testing Phases)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

소프트웨어, 테스트, 단계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 16. 소프트웨어 테스트 단계 (Software Testing Phases)
* **단위 테스트 (Unit Test)**: 코딩 직후 최소 단위인 모듈/컴포넌트 테스트. (알고리즘 오류, 탈출구 없는 반복문 등 발견).
* **통합 테스트 (Integration Test)**:
  * 하향식 (Top-down): 상위에서 하위로 (스텁/Stub 사용).
  * 상향식 (Bottom-up): 하위에서 상위로 (드라이버/Driver 사용).
* **인수 테스트 (Acceptance Test)**: 사용자가 시스템을 수락하기 전 수행.
  * **알파 테스트**: 개발자 앞에서 사용자가 수행.
  * **베타 테스트 (Field Testing)**: 최종 사용자가 실제 환경에서 여러 사용자 앞에서 수행.
* **VI (Vietnamese) (Tiếng Việt):**
  * Unit Test: Kiểm thử từng module nhỏ (tìm lỗi thuật toán, lặp vô hạn).
  * Integration Test: Kiểm thử tích hợp. Top-down (từ trên xuống), Bottom-up (từ dưới lên).
  * Acceptance Test: Kiểm thử chấp nhận. Alpha (cùng dev), Beta (không có dev, real-world).
* **Example**: 게임 개발 후 회사 내부에서 해보는 것이 알파 테스트, 유저들에게 먼저 공개하는 것이 오픈 베타 테스트입니다.
* 💡 **Mẹo ghi nhớ**: Alpha = có người tạo ra (Dev) giám sát. Beta = thả ra tự nhiên cho User.
