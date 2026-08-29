# 168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

관계형, 데이터, 모델, E-R, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)
- **E-R 모델 (168-169):** 피터 첸 제안. 기본키 속성은 '밑줄 타원(Underlined Oval)', 복합 속성은 '복수 타원(Multiple Ovals)'. 1:1, 1:N, N:M 표현.
- **관계형 데이터 모델 (170):** 2차원 표(Table) 형태.
- **릴레이션 특징 (172):**
  - 똑같은 튜플 포함 불가 (튜플의 유일성).
  - 튜플 사이, 속성 사이 순서 없음.
  - 속성 이름은 유일, 속성 값은 중복 가능.
  - 원자값(Atomic)만 허용.
- **VI (Vietnamese) (Tiếng Việt):** Mô hình E-R và Mô hình quan hệ.
  - E-R: Thuộc tính khóa chính có gạch chân, thuộc tính phức hợp có nhiều vòng bầu dục.
  - Đặc điểm quan hệ (Bảng): Hàng không trùng lặp (duy nhất), không quan trọng thứ tự hàng/cột, chỉ chứa giá trị nguyên tử.
