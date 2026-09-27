# 15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

객체지향, 모듈화, 방법론

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)

### 객체지향 분석 방법론 종류 (Các phương pháp phân tích OOP)
- **Rumbaugh (럼바우):** 객체(Object), 동적(Dynamic), 기능(Functional) 모델로 나누어 분석. (Chia làm 3 mô hình).
- **Booch (부치):** 미시적(Micro) 개발과 거시적(Macro) 개발 프로세스 모두 사용. (Dùng cả quy trình vĩ mô và vi mô).
- **Jacobson (제이콥슨):** Use Case(유스케이스)를 강조. (Nhấn mạnh vào Use Case).
- **Coad와 Yourdon:** E-R 다이어그램 사용. (Dùng sơ đồ ER).
- **Wirfs-Brock:** 분석과 설계 간 구분이 없고 연속적으로 수행. (Không phân biệt rõ phân tích và thiết kế, làm liên tục).
- 💡 **Mẹo ghi nhớ (Mnemonic):** R-O, B-M, J-U, C-E, W-L -> **Ra Ôm Bạn Mới, Giữ Út, Cho Em Vui Lây** (Rumbaugh-Object, Booch-Micro, Jacobson-Use case, Coad-ER, Wirfs-Liên tục).

### 공통 모듈 명세 기법 (Kỹ thuật đặc tả Module chung)
- **정확성 (Correctness):** 기능이 필요하다는 것을 알 수 있도록 정확히 작성. (Chính xác, biết rõ cần thiết).
- **명확성 (Clarity):** 중의적으로 해석되지 않도록 명확하게. (Rõ ràng, không hiểu 2 nghĩa).
- **완전성 (Completeness):** 구현에 필요한 모든 것을 기술. (Đầy đủ mọi thứ cần thiết).
- **일관성 (Consistency):** 기능들 간 상호 충돌이 발생하지 않도록. (Nhất quán, không xung đột).
- **추적성 (Traceability):** 요구사항 출처, 관련 시스템 등 관계 파악. (Có thể truy xuất nguồn gốc).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **CMHNT** (Chính - Minh - Hoàn - Nhất - Truy): **Chỉ Mong Học Nhất Trường**.

### 코드(Code)의 주요 기능 (Chức năng chính của Code)
- 식별 기능 (Nhận diện), 분류 기능 (Phân loại), 배열 기능 (Sắp xếp), 표준화 기능 (Chuẩn hóa), 간소화 기능 (Đơn giản hóa).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **TPBTG** (Thức - Phân - Bài - Tiêu - Giản): **Thích Phá Bài Thì Giảm**.

### 코드의 종류 심화 (Các loại Code chi tiết)
- **순차 코드 (Sequence Code):** 1, 2, 3... (Theo thứ tự).
- **블록 코드 (Block Code):** 공통성 있는 것끼리 블록으로 구분 (1000~1100: Phòng Nhân sự, 1101~1200: Phòng IT).
- **10진 코드 (Decimal Code):** 0~9 분할 반복 (Ví dụ: Mã phân loại sách thư viện Dewey).
- **그룹 분류 코드 (Group Classification):** 대/중/소 분류 (1-01-001).
- **연상 코드 (Mnemonic Code):** 명칭/약호와 관계있는 문자/숫자 (TV-40). (Gợi nhớ).
- **표의 숫자 코드 (Significant Digit):** 물리적 수치 적용 (120-720).
- **합성 코드 (Combined Code):** 2개 이상 코드 조합 (KE-711).
