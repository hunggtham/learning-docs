# 163-167. 데이터베이스 설계 순서 (Database Design Process)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **163-167. 데이터베이스 설계 순서 (Database Design Process)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

데이터베이스, 설계, 순서

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 163-167. 데이터베이스 설계 순서 (Database Design Process)
- **요구 조건 분석 (Requirements Analysis):** 요구 조건 명세서 작성.
- **개념적 설계 (Conceptual Design - 164):** 개념 스키마, E-R 모델, DBMS 독립적.
- **논리적 설계 (Logical Design - 165):** 논리 스키마 설계, 매핑.
- **물리적 설계 (Physical Design - 166):** 물리적 구조 변환, 접근 경로, 저장 레코드 양식 결정.
- **구현 (Implementation):** DDL로 DB 생성.
- **VI (Vietnamese) (Tiếng Việt):** Quy trình thiết kế CSDL.
  - Phân tích yêu cầu -> Thiết kế Khái niệm (E-R) -> Thiết kế Logic (Bảng/Lược đồ logic) -> Thiết kế Vật lý (Lưu trữ) -> Triển khai (Code DDL).
- 💡 **Mẹo ghi nhớ:** Yêu-Khái-Lo-Vật-Cài (Yêu cầu -> Khái niệm -> Logic -> Vật lý -> Cài đặt).
