# 핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

핵심, 애플리케이션, 테스트, 원리, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)

### 테스트의 기본 원리 (Các nguyên lý cơ bản)
- **완벽한 테스팅은 불가능:** Không bao giờ test ra 100% không còn lỗi.
- **결함 집중 (Defect Clustering):** Lỗi thường tập trung ở 20% các module cốt lõi (Quy tắc Pareto 80/20).
- **살충제 패러독스 (Pesticide Paradox):** Nghịch lý thuốc trừ sâu. Dùng mãi một bài test thì không tìm ra lỗi mới. Cần liên tục thay đổi bộ test.
- **정황 의존성 (Context Dependency):** Tùy bối cảnh (web, app, game) mà cách test phải khác nhau.
- **오류-부재의 궤변 (Absence of Errors Fallacy):** App không có lỗi nhưng không đúng ý khách hàng thì vẫn là rác.

### 정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)
- **정적 테스트 (Static):** Không chạy code. Đọc và review code/tài liệu. (Walkthrough, Inspection, Review). Phát hiện lỗi sớm, tiết kiệm tiền.
- **동적 테스트 (Dynamic):** Phải chạy chương trình. Gồm Black Box và White Box testing.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Thuốc trừ sâu (Pesticide) = Cần thay mới bộ Test. Đám mây lỗi (Clustering) = 20% code gây ra 80% lỗi.

---
