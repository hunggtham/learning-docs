# 179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

정규화와, 이상, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)
- **정규화 목적 (180):** 데이터 중복 배제, 무결성 유지, 이상 발생 방지. 논리적 설계 단계 수행.
- **이상 (Anomaly - 181):**
  - 삽입 이상 (Insertion Anomaly): 원하지 않는 값까지 삽입해야 하는 현상.
  - 삭제 이상 (Deletion Anomaly): 의도치 않은 연쇄 삭제(Cascade).
  - 갱신 이상 (Update Anomaly): 일부만 갱신되어 정보 모순 발생.
- **정규화 단계 암기 요령 (182):** 두부이결다조 (도메인 원자값, 부분 함수 종속 제거, 이행적 함수 종속 제거, 결정자이면서 후보키 아닌 것 제거, 다치 종속 제거, 조인 종속).
- **VI (Vietnamese) (Tiếng Việt):** Chuẩn hóa và Dị thường dữ liệu (Sâu hơn).
  - Dị thường: Thêm (phải thêm dữ liệu không cần thiết), Xóa (bị mất dữ liệu liên quan), Sửa (cập nhật không đồng bộ gây mâu thuẫn).
  - Quy tắc ghi nhớ các chuẩn: Do-Bu-I-Gyeol-Da-Jo (Nguyên tử - Phần - Bắc cầu - Định thức - Đa trị - Kết nối).
- **Example:** 학번만 지우려다 이름과 학과 정보까지 다 지워지는 것이 '삭제 이상'. / Định xóa mã SV nhưng vô tình xóa luôn tên và khoa là 'Dị thường xóa'.
